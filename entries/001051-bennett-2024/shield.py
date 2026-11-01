"""Loading and measures for the SHIELD recordings of dandiset 001051.

Bennett, Ouellette, Ramirez et al. (2024), Neuron 112, 2869-2885, doi:10.1016/j.neuron.2024.06.015.

Each session NWB holds one recording: the units table (quality metrics, spike times, the peak
channel), the electrodes table (CCF structure and coordinates per channel), the stimulus tables,
trials, licks, rewards, running and eye tracking. Files are streamed from the archive at the
pinned version with remfile and h5py; nothing is written to disk.

Where the parameters come from:

- `QC`: isi_violations < 0.5, amplitude_cutoff < 0.1, presence_ratio > 0.95 (STAR Methods,
  "Quality metric criteria for unit inclusion"); non-noise is quality == "good" (same passage:
  "all units were included except those with non-physiological waveforms"; the code's
  quality == 'good').
- `passing_session_ids()`: the 87 sessions passing ephys QC, read from the paper's analysis code,
  DynamicGating_ephys_metrics.ipynb (the cell defining PASSING_EPHYS_SESSION_IDS; cell 26 in the
  claims file's count), repository https://github.com/AllenInstitute/SHIELD_Dynamic_Gating_Analysis at commit
  3c09a0dc2972381f06393ddf5c000e16462c7037. The claims file names this list as the session set.
- `NOT_IN_AREA`: the code's exclusion of 'No Area', 'out of brain' and 'Track not annotated'
  (same notebook, the cell defining dg_metrics_inarea; claim fig4b-units-areas-per-session).
- Receptive fields (`rf_pvalues`): spike counts in the 250 ms of each Gabor presentation summed
  per position on the 9 x 9 grid; chi-square statistic of the map against a uniform expectation
  weighted by the number of presentations per position (Methods, "Receptive Field Mapping",
  which cites reference 18, Siegle et al. 2021; the chi-square test of that paper, as in the
  AllenSDK receptive-field code, compares the summed counts per position with the counts expected
  from the mean). The p value is the AllenSDK bootstrap (compute_chi_shuffle, 1000 resamplings
  of presentations), as the code's p_value_rf is, not the analytic chi-square p value. p < 0.01
  is significant (Methods).
- Alpha events (`detect_alpha_events`): STAR Methods, "Identification of alpha events", with the
  window, stepping and the event rule readings given in the claims file's header (from
  run_4Hz_bursts.py and analysis_utils.py of the same repository).
- Population rates: events are detected on the smoothed rate (the header's symmetrical
  exponential filter, inside `find_events`). The autocorrelogram threshold, the CCGs and the
  coherence are computed on the unsmoothed 10 ms rate. The claims file defines the population
  rate as smoothed but does not say which steps use the smoothed trace; the detail is taken from
  the code's printed output that the claims file's header quotes (1653 VISp and 113 MOp
  qualifying events, code cell 12), which the unsmoothed autocorrelogram matches and the smoothed
  one does not (`auto_power_smooth`, kept to show its counts).
- `freq_auto`: the peak of the spectrum of the 2 s autocorrelogram (200 samples, 0.5 Hz steps).
  `freq_auto_pad` is the same spectrum zero-padded to 2048 samples (0.049 Hz steps), a standard
  interpolation of the peak, shown because the 0.5 Hz grid ties the values.
- Clock check (`clock`): running speed around the change time of hit and miss trials (-2 to 3 s)
  and pupil area around full-field white and black flashes (-0.5 to 1.5 s), on the 10 ms grid,
  to show that the running and eye-tracking streams share the stimulus clock (protocol, data
  check). Mice slow down to lick after a detected change, and the pupil constricts after a white
  flash, so the contrasts should start only after time 0.
"""

from __future__ import annotations

import json
import urllib.request
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile

DANDISET_ID = "001051"
DANDISET_VERSION = "0.260922.1827"
API = "https://api.dandiarchive.org/api"

CODE_REPO = "https://github.com/AllenInstitute/SHIELD_Dynamic_Gating_Analysis"
CODE_COMMIT = "3c09a0dc2972381f06393ddf5c000e16462c7037"
CODE_RAW = f"https://raw.githubusercontent.com/AllenInstitute/SHIELD_Dynamic_Gating_Analysis/{CODE_COMMIT}"

CODE_METRICS_NOTEBOOK = "analysis_code/analysis_notebooks/DynamicGating_ephys_metrics.ipynb"


def passing_session_ids():
    """The 87 sessions passing ephys QC, read from the code's notebook at the pinned commit."""
    import re
    with urllib.request.urlopen(f"{CODE_RAW}/{CODE_METRICS_NOTEBOOK}", timeout=120) as r:
        nb = json.loads(r.read())
    for cell in nb["cells"]:
        src = "".join(cell["source"])
        if "PASSING_EPHYS_SESSION_IDS = [" in src:
            body = src.split("PASSING_EPHYS_SESSION_IDS = [", 1)[1].split("]", 1)[0]
            return [int(x) for x in re.findall(r"\d+", body)]
    raise ValueError("session list not found in the code's notebook")

NOT_IN_AREA = ["No Area", "out of brain", "Track not annotated"]
QC_ISI, QC_AMP, QC_PRESENCE = 0.5, 0.1, 0.95

UNIT_SCALARS = ["PT_ratio", "amplitude", "amplitude_cutoff", "cluster_id", "cumulative_drift",
                "d_prime", "firing_rate", "isi_label", "isi_violations", "isolation_distance",
                "l_ratio", "local_index", "max_drift", "nn_hit_rate", "nn_miss_rate",
                "peak_channel_id", "presence_ratio", "quality", "recovery_slope",
                "repolarization_slope", "silhouette_score", "snr", "spread", "structure_layer",
                "velocity_above", "velocity_below", "waveform_duration"]


def _get(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.loads(r.read())


def list_assets():
    """All assets of the pinned version: path, asset id, size."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    out = []
    while url:
        d = _get(url)
        out += [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in d["results"]]
        url = d.get("next")
    return pd.DataFrame(out).sort_values("path").reset_index(drop=True)


def version_metadata():
    return _get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/")


def asset_url(asset_id):
    return f"{API}/assets/{asset_id}/download/"


def open_nwb(asset_id):
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def _col(g, name):
    v = g[name][:]
    if v.dtype.kind in "OS":
        v = np.array([_s(t) for t in v], dtype=object)
    return v


def read_table(g, cols=None):
    """A DynamicTable's scalar columns (no ragged ones) as a DataFrame indexed by id."""
    cols = cols or [c for c in g.attrs["colnames"] if c + "_index" not in g]
    df = pd.DataFrame({c: _col(g, c) for c in cols if c in g and g[c].ndim == 1})
    df.index = g["id"][:]
    return df


def scan_session(asset_id):
    """Everything but the spike times and the continuous streams, for one session file."""
    f = open_nwb(asset_id)
    try:
        md = dict(f["general/metadata"].attrs)
        subj = {k: _s(f["general/subject"][k][()]) for k in ["age", "genotype", "sex", "subject_id"]}
        sess = {"session_id": int(_s(f["identifier"][()])), "session_type": md.get("session_type"),
                "equipment": md.get("equipment_name"), "start": _s(f["session_start_time"][()]),
                "description": _s(f["session_description"][()]), **subj}
        el = read_table(f["general/extracellular_ephys/electrodes"],
                        ["location", "group_name", "probe_id", "probe_channel_number",
                         "probe_vertical_position", "valid_data", "x", "y", "z"])
        u = read_table(f["units"], UNIT_SCALARS)
        idx = f["units/spike_times_index"][:]
        u["n_spikes"] = np.diff(np.concatenate([[0], idx]))
        u["spk_end"] = idx
        u = u.join(el.rename(columns={"location": "structure_acronym", "group_name": "probe"}),
                   on="peak_channel_id")
        u["session_id"] = sess["session_id"]
        tr = read_table(f["intervals/trials"])
        sess["n_trials"] = len(tr)
        sess["n_hit"] = int(tr["hit"].sum())
        sess["n_auto_rewarded_trials"] = int(tr["auto_rewarded"].sum())
        rw = f["processing/rewards"]
        auto = rw["autorewarded/data"][:].astype(bool)
        sess["n_rewards"] = int(len(auto))
        sess["n_rewards_auto"] = int(auto.sum())
        sess["n_rewards_earned"] = int((~auto).sum())
        sess["n_licks"] = int(f["processing/licking/licks/timestamps"].shape[0])
        stim = {}
        for k in f["intervals"]:
            if k.endswith("_presentations"):
                g = f[f"intervals/{k}"]
                st = g["start_time"][:]
                stim[k] = {"n": len(st), "t0": float(st.min()), "t1": float(g["stop_time"][:].max()),
                           "active": int(g["active"][:].sum()) if "active" in g else None}
        sess["stimuli"] = stim
        devs = f["general/devices"]
        sess["probes"] = sorted(k for k in devs if k.startswith("probe"))
        opto = {}
        if "processing/optotagging" in f:
            g = f["processing/optotagging/optogenetic_stimulation"]
            o = read_table(g, ["condition", "level", "stimulus_name", "duration"])
            opto = o.groupby(["stimulus_name", "level", "duration"]).size().to_dict()
        sess["opto"] = {str(k): v for k, v in opto.items()}
        sess["has_eye"] = "acquisition/EyeTracking" in f
        sess["n_units"] = len(u)
        return sess, u
    finally:
        f.close()


def scan_all(asset_ids, workers=8):
    """Scan many sessions in parallel processes (h5py serialises threads)."""
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(scan_session, asset_ids))
    sessions = pd.DataFrame([r[0] for r in res])
    sessions["asset_id"] = list(asset_ids)
    units = pd.concat([r[1] for r in res])
    units.index.name = "unit_id"
    return sessions, units


def qc_pass(u):
    return ((u["isi_violations"] < QC_ISI) & (u["amplitude_cutoff"] < QC_AMP)
            & (u["presence_ratio"] > QC_PRESENCE) & (u["quality"] == "good"))


def read_code_csv(path):
    """A table from the paper's repository at the pinned commit."""
    return pd.read_csv(f"{CODE_RAW}/{path}")


# ----------------------------------------------------------------------------------------------
# One pass over the spikes of a session.
#
# Every spike-based measure is computed here, from one read of the session's spike times, so the
# 640 MB or so of spikes per session are streamed once. The function returns only summaries.

BIN = 0.01                 # population rate bins, 10 ms (Methods, Identification of alpha events)
MIN_UNITS = 20             # areas with fewer units are excluded (Methods); the code needs more than 20
RF_WINDOW = 0.25           # Gabor presentations last 250 ms (Methods, Visual stimulation)
RF_SHUFFLES = 1000         # AllenSDK chi-square bootstrap, as in the code's p_value_rf (steps of 0.001)
RF_ALPHA = 0.01            # Methods, Receptive Field Mapping
WIN_DETECT, STEP_DETECT = 1.25, 0.25   # code, find_4Hz_bursts_for_area_just_spike_minima
REFRACTORY = 2.0           # Methods and code
CCG_HALF = 1.0             # 2 s CCG windows (Methods)
COH_HALF = 2.0             # 4 s coherence windows (Methods)
AUTO_THRESHOLD = 0.1       # Methods; code get_qualifying_autoccgs
REFERENCE_AREAS = ("VISp", "MOp")
LAG_PAIRS = {"VISp": ["VISl", "VISal", "LGd", "LP", "CP"], "MOp": ["SSp", "PO"]}  # code cell 26


def exponential_convolve(x, tau=1, axis=-1):
    """The code's analysis_utils.exponential_convolve with symmetrical=True."""
    from scipy.ndimage import convolve1d
    from scipy.signal.windows import exponential
    w = exponential(10 * tau, center=None, tau=tau, sym=True)
    w = w / w.sum()
    return convolve1d(x, w[::-1], axis=axis)


def find_events(rate, rule):
    """Alpha events on one population rate (10 ms bins from time 0).

    rate: the area's mean rate per unit, spikes/s. Smoothed, inverted, and searched in 1.25 s
    windows stepped by 0.25 s, as in the code. rule "E2" (code): a window with more than three
    maxima of which three successive ones have both intervals in [125, 350) ms; "E1" (Methods):
    four successive maxima with all three intervals in [125, 350] ms. The event time is the
    first of those maxima; events closer than 2 s to an earlier one are dropped (code: the
    minimum of event time minus all earlier events must exceed 2 s).
    Returns event times (s) and, per event, the times of the window's maxima.
    """
    from scipy.signal import find_peaks
    inv = -exponential_convolve(rate)
    n = len(inv)
    wlen = int(round(WIN_DETECT / BIN))
    cand = [-1.0]
    peaks_out = []
    for start in range(0, n, int(round(STEP_DETECT / BIN))):
        seg = inv[start:start + wlen]
        pk = find_peaks(seg, prominence=5, height=-1, width=[0.1 / BIN, 0.3 / BIN])[0]
        if len(pk) <= 3:
            continue
        pk = np.sort(pk)
        first = None
        if rule == "E2":
            for i in range(len(pk) - 2):
                iv = np.diff(pk[i:i + 3])
                if iv.min() >= 0.125 / BIN and iv.max() < 0.35 / BIN:
                    first = i
                    break
        else:
            for i in range(len(pk) - 3):
                iv = np.diff(pk[i:i + 4])
                if iv.min() >= 0.125 / BIN - 1e-9 and iv.max() <= 0.35 / BIN + 1e-9:
                    first = i
                    break
        if first is None:
            continue
        t = (start + pk[first]) * BIN
        if np.min(t - np.array(cand)) > REFRACTORY:
            cand.append(t)
            peaks_out.append((start + pk) * BIN)
    return np.array(cand[1:]), peaks_out


def crosscorrelogram(x, y):
    """The code's analysis_utils.crosscorrelogram."""
    from scipy.signal import correlate
    x1, y1 = x - x.mean(), y - y.mean()
    den = np.sqrt(np.sum(x1 ** 2) * np.sum(y1 ** 2))
    c = correlate(x1, y1, "same")
    return c / den if den > 0 else np.full(len(x), np.nan)


def auto_band_power(ccg):
    """Peak of the squared 3-7 Hz band-passed autocorrelogram (code get_qualifying_autoccgs)."""
    from scipy.signal import butter, filtfilt
    b, a = butter(2, [3 / 50, 7 / 50], btype="band")
    return float(np.max(filtfilt(b, a, ccg) ** 2))


def window(rate, t, half):
    """Bins of a 10 ms rate from t - half to t + half (nearest bin; empty when off the record)."""
    i0 = int(round((t - half) / BIN))
    n = int(round(2 * half / BIN))
    if i0 < 0 or i0 + n > rate.shape[-1]:
        return None
    return rate[..., i0:i0 + n]


def rf_pvalues(spk, units_idx, pres, rng, n_shuffles=RF_SHUFFLES):
    """Chi-square RF significance with the AllenSDK bootstrap (compute_chi_shuffle).

    Spike counts in the 250 ms of each Gabor presentation; categories are the 81 positions
    (orientations pooled); expected = mean count per presentation times presentations per
    position; p = fraction of 1000 resamplings of presentations (with replacement) whose
    statistic exceeds the observed one. Returns p values, and the azimuth and elevation of the
    position with the largest summed count.
    """
    starts = pres["start_time"].values
    pos = pd.MultiIndex.from_arrays([pres["position_x"].values, pres["position_y"].values])
    cats, keys = pd.factorize(pos)
    ncat = cats.max() + 1
    dummy = np.zeros((len(starts), ncat), np.float32)
    dummy[np.arange(len(starts)), cats] = 1
    counts = np.zeros((len(starts), len(units_idx)), np.float32)
    for j, (a, b) in enumerate(units_idx):
        st = spk[a:b]
        counts[:, j] = np.searchsorted(st, starts + RF_WINDOW) - np.searchsorted(st, starts)
    per_cat = dummy.sum(0)

    def chi(c):
        obs = c.T @ dummy
        exp = np.outer(c.mean(0), per_cat)
        with np.errstate(divide="ignore", invalid="ignore"):
            x = np.where(exp > 0, (obs - exp) ** 2 / exp, 0.0)
        return x.sum(1)

    actual = chi(counts)
    exceed = np.zeros(len(units_idx))
    for _ in range(n_shuffles):
        idx = rng.integers(0, len(starts), len(starts))
        exceed += actual < chi(counts[idx])
    p = exceed / n_shuffles
    obs = counts.T @ dummy
    best = [keys[k] for k in obs.argmax(1)] if len(units_idx) else []
    return p, np.array([b[0] for b in best]), np.array([b[1] for b in best])


def _read_table_times(f, name, cols):
    g = f[f"intervals/{name}"]
    return pd.DataFrame({c: _col(g, c) for c in cols if c in g})


def _resample_ffill(ts, vals, step=BIN):
    """The code's resample_df: a 10 ms grid from the first timestamp, forward filled."""
    order = np.argsort(ts)
    ts, vals = ts[order], vals[order]
    grid = ts[0] + np.arange(int((ts[-1] - ts[0]) / step) + 1) * step
    idx = np.searchsorted(ts, grid + 1e-9, side="right") - 1
    return grid, vals[np.clip(idx, 0, len(vals) - 1)]


def _triggered(grid, vals, times, before=5.0, after=5.0):
    out = []
    for t in times:
        m = (grid >= t - before) & (grid < t + after)
        out.append(vals[m])
    return out


def session_spike_products(asset_id, units, session_id, seed=0, cp_rf_sessions=()):
    """All spike-based measures of one session.

    units: this session's rows of the scanned units table (index unit id), with spk_end and
    n_spikes. Returns a dict of summaries (see the notebook for what each claim uses).
    """
    from nitime.analysis import CoherenceAnalyzer, MTCoherenceAnalyzer
    import nitime.timeseries as nts

    out = {"session_id": session_id}
    f = open_nwb(asset_id)
    try:
        spk = f["units/spike_times"][:]
        u = units.copy()
        u["a"] = (u["spk_end"] - u["n_spikes"]).astype(np.int64)
        u["b"] = u["spk_end"].astype(np.int64)
        u["qc"] = qc_pass(u)
        u["qc90"] = ((u["isi_violations"] < QC_ISI) & (u["amplitude_cutoff"] < QC_AMP)
                     & (u["presence_ratio"] > 0.9))
        isi = u["isi_label"].fillna("No label")
        u["label_l1"] = np.where(isi.isin(["No label", ""]), u["structure_acronym"], isi)
        rng_rf = np.random.default_rng([seed, session_id, 1])

        # stimulus tables
        tabs = [k for k in f["intervals"] if k.endswith("_presentations")]
        img_name = [k for k in tabs if "image" in k][0]
        img = _read_table_times(f, img_name, ["start_time", "stop_time", "image_name", "active", "omitted"])
        img = img.sort_values("start_time").reset_index(drop=True)
        first_stim = min(float(f[f"intervals/{k}/start_time"][:].min()) for k in tabs)
        last_stim_end = max(float(f[f"intervals/{k}/stop_time"][:].max()) for k in tabs)
        act = img[img["active"].astype(bool)]
        beh_start, beh_end = float(act["start_time"].min()), float(act["stop_time"].max())
        out.update(first_stim=first_stim, last_stim_end=last_stim_end, beh_start=beh_start,
                   beh_end=beh_end, image_names=sorted(img["image_name"].unique()))

        # Figure S4I: summed spikes of QC units in 1 s bins from the first stimulus
        q = u[u["qc"] & (u["n_spikes"] >= 2)]
        allq = np.concatenate([spk[a:b] for a, b in zip(q["a"], q["b"])]) if len(q) else np.array([])
        edges = np.arange(int(first_stim), int(allq.max()) if len(allq) else int(first_stim) + 1)
        out["s4i_counts"] = np.histogram(allq, edges)[0].astype(np.int32)
        out["s4i_n_units"] = len(q)
        del allq

        # receptive fields of VISp-labelled and CP units (QC at presence 0.9; the code's is_sig_rf
        # table covers all units, these are the ones the claims use)
        gab = _read_table_times(f, "gabor_20_deg_250ms_presentations",
                                ["start_time", "position_x", "position_y", "orientation"])
        # (noise CP units are included so that the Figure 8D variant without a noise filter can
        # split them by RF; the resamplings do not depend on the units, so other p values are unchanged)
        rfu = u[u["qc90"] & ((((isi == "VISp") | u["structure_acronym"].str.startswith("VISp"))
                              & (u["quality"] == "good")) | (u["structure_acronym"] == "CP"))]
        p, az, el = rf_pvalues(spk, list(zip(rfu["a"], rfu["b"])), gab, rng_rf)
        out["rf"] = pd.DataFrame({"p_rf": p, "azimuth_peak": az, "elevation_peak": el}, index=rfu.index)
        sig = pd.Series(False, index=u.index)
        sig.loc[rfu.index] = p < RF_ALPHA
        u["sig_rf"] = sig

        # Figure 4G: PSTHs (1 ms) of VISp units to active im115_r-1.0 presentations, -1 to 1.5 s
        im = act[(act["image_name"] == "im115_r-1.0")]["start_time"].values
        v1 = u[u["qc90"] & (u["quality"] == "good") & (isi == "VISp")]
        ps = np.zeros((len(v1), 2500), np.float32)
        for j, (a, b) in enumerate(zip(v1["a"], v1["b"])):
            st = spk[a:b]
            for t0 in im:
                i0, i1 = np.searchsorted(st, [t0 - 1, t0 + 1.5])
                ps[j] += np.bincount(np.minimum(((st[i0:i1] - (t0 - 1)) / 0.001).astype(int), 2499),
                                     minlength=2500)
        out["im115_psth"] = pd.DataFrame(ps / max(len(im), 1) / 0.001, index=v1.index)
        out["im115_n"] = len(im)

        # Figure 8D: mean responses (1 ms, -250 to 500 ms) to every active presentation, CP and VISp
        if session_id in cp_rf_sessions:
            ft = act["start_time"].values
            sel = u[u["qc90"] & ((u["structure_acronym"] == "CP") | (isi == "VISp"))]
            m = np.zeros((len(sel), 750), np.float32)
            for j, (a, b) in enumerate(zip(sel["a"], sel["b"])):
                st = spk[a:b]
                for t0 in ft:
                    i0, i1 = np.searchsorted(st, [t0 - 0.25, t0 + 0.5])
                    m[j] += np.bincount(np.minimum(((st[i0:i1] - (t0 - 0.25)) / 0.001).astype(int), 749),
                                        minlength=750)
            out["fig8d"] = pd.DataFrame(m / len(ft), index=sel.index)

        # population rates (10 ms) over 0 to the end of the last stimulus
        nb = int(round(last_stim_end / BIN))

        def poprate(idx):
            if len(idx) == 0:
                return None
            s = np.concatenate([spk[a:b] for a, b in zip(u.loc[idx, "a"], u.loc[idx, "b"])])
            s = s[(s >= 0) & (s < nb * BIN)]
            return (np.bincount((s / BIN).astype(np.int64), minlength=nb)[:nb] / BIN / len(idx)).astype(np.float32)

        qcu = u[u["qc"]]
        groups = {}
        cnt1 = qcu["label_l1"].value_counts()
        groups["L1"] = {a: qcu.index[qcu["label_l1"] == a] for a in cnt1[cnt1 >= MIN_UNITS].index}
        cnt2 = qcu["structure_acronym"].value_counts()
        groups["L2"] = {a: qcu.index[qcu["structure_acronym"].str.contains(a, regex=False)]
                        for a in cnt2[cnt2 > MIN_UNITS].index}
        out["areas"] = {L: {a: len(ix) for a, ix in g.items()} for L, g in groups.items()}
        cp = qcu[qcu["structure_acronym"] == "CP"]
        extra = {"CP-RF": cp.index[cp["sig_rf"]], "CP-noRF": cp.index[~cp["sig_rf"]]}
        out["cp_counts"] = {k: len(v) for k, v in extra.items()}

        # pupil and running, resampled at 10 ms with forward fill (code run_4Hz_analysis.py)
        out["has_eye"] = "acquisition/EyeTracking" in f
        if out["has_eye"]:
            et = f["acquisition/EyeTracking"]
            pt = et["eye_tracking/timestamps"][:]
            pa = et["pupil_tracking/area"][:]
            blink = et["likely_blink/data"][:].astype(bool)
            pg, pv = _resample_ffill(pt[~blink], pa[~blink])
        else:
            pg, pv = np.array([0.0]), np.array([np.nan])
        rs = f["processing/running/speed"]
        rg, rv = _resample_ffill(rs["timestamps"][:], rs["data"][:])

        # clock check: running around the change time of hit and miss trials; pupil around
        # full-field white and black flashes
        tr = _read_table_times(f, "trials", ["change_time", "hit", "miss", "response_latency"])
        clock = {}
        for cond in ("hit", "miss"):
            ct = tr.loc[tr[cond].astype(bool), "change_time"].dropna().values
            segs = [x for x in _triggered(rg, rv, ct, before=2.0, after=3.0) if x.size >= 500]
            clock[("running", cond)] = np.nanmean([x[:500] for x in segs], 0) if segs else np.full(500, np.nan)
            clock[("n", cond)] = len(ct)
        clock["response_latency"] = float(np.nanmedian(tr.loc[tr["hit"].astype(bool), "response_latency"]))
        fl = _read_table_times(f, "flash_250ms_presentations", ["start_time", "color"])
        for col, nm in ((1.0, "white"), (-1.0, "black")):
            ft_ = fl.loc[fl["color"] == col, "start_time"].values
            segs = [x for x in _triggered(pg, pv, ft_, before=0.5, after=1.5) if x.size >= 200]
            clock[("pupil", nm)] = np.nanmean([x[:200] for x in segs], 0) if segs else np.full(200, np.nan)
            clock[("n", nm)] = len(ft_)
        out["clock"] = clock

        # VISp units for the replay analysis (Figure S6): mean evoked rate per image
        imgs = [n for n in out["image_names"] if n != "omitted"]
        events_out = {}
        for L in ("L1", "L2"):
            g = groups[L]
            rates = {a: poprate(ix) for a, ix in g.items()}
            for k, ix in extra.items():
                rates[k] = poprate(ix) if len(ix) else None
            for ref in REFERENCE_AREAS:
                if ref not in g:
                    continue
                r0 = rates[ref]
                r0s = exponential_convolve(r0)
                for E in ("E1", "E2"):
                    ev, pk = find_events(r0, E)
                    rng = np.random.default_rng([seed, session_id, 10 + ["L1", "L2"].index(L),
                                                 REFERENCE_AREAS.index(ref), int(E[1])])
                    rnd = rng.random(len(ev)) * (beh_end - beh_start) + beh_start
                    rnd = np.round(rnd / BIN) * BIN
                    res = []
                    names = [a for a in rates if rates[a] is not None]
                    stack = np.stack([rates[a] for a in names])
                    lag_names = [a for a in LAG_PAIRS[ref] if a in names]
                    for i, (t, tr) in enumerate(zip(ev, rnd)):
                        w2 = window(r0, t, CCG_HALF)
                        if w2 is None:
                            continue
                        auto = crosscorrelogram(w2, w2)
                        power = auto_band_power(auto)
                        spec = np.abs(np.fft.rfft(auto - auto.mean()))
                        fr = np.fft.rfftfreq(len(auto), BIN)
                        band = (fr >= 1) & (fr <= 20)
                        spec_p = np.abs(np.fft.rfft(auto - auto.mean(), n=2048))
                        fr_p = np.fft.rfftfreq(2048, BIN)
                        band_p = (fr_p >= 1) & (fr_p <= 20)
                        w2s = window(r0s, t, CCG_HALF)
                        ipk = np.diff(pk[i])
                        rec = {"t": t, "t_rand": tr, "auto_power": power,
                               "freq_peaks": 1 / np.median(ipk) if len(ipk) else np.nan,
                               "freq_auto": fr[band][np.argmax(spec[band])],
                               "freq_auto_pad": fr_p[band_p][np.argmax(spec_p[band_p])],
                               "auto_power_smooth": auto_band_power(crosscorrelogram(w2s, w2s)),
                               "n_maxima": len(pk[i])}
                        res.append(rec)
                    evdf = pd.DataFrame(res)
                    entry = {"events": evdf, "n_units": len(g[ref])}
                    if len(evdf):
                        evdf["qual"] = evdf["auto_power"] > AUTO_THRESHOLD
                        qv = evdf[evdf["qual"]]
                        # last active presentation starting before each event
                        st0 = act["start_time"].values
                        k = np.searchsorted(st0, evdf["t"].values) - 1
                        ok = (k >= 0) & (k < len(st0))
                        evdf["since_offset"] = np.where(ok, evdf["t"].values - act["stop_time"].values[np.clip(k, 0, None)], np.nan)
                        evdf["prev_image"] = np.where(ok, act["image_name"].values[np.clip(k, 0, None)], None)
                        # pupil and running, 0 to 1 s after the event (bins 500:600 of -5 to 5 s)
                        for lab, tt in (("", evdf["t"].values), ("_rand", evdf["t_rand"].values)):
                            pw = _triggered(pg, pv, tt)
                            rw = _triggered(rg, rv, tt)
                            evdf["pupil" + lab] = [np.mean(x[500:600]) if x.size > 999 else np.nan for x in pw]
                            evdf["pupil_win_mean" + lab] = [np.nanmean(x) if x.size else np.nan for x in pw]
                            evdf["running" + lab] = [np.mean(x[500:600]) if x.size > 999 else np.nan for x in rw]
                        # coherence, CCGs and lags, for qualifying events
                        coh = {"event": [], "R1": [], "R2": []}
                        ccg_sum = {a: np.zeros(int(2 * CCG_HALF / BIN)) for a in names}
                        ccg_n = 0
                        lags = []
                        trig = []
                        for _, rr in qv.iterrows():
                            we = window(stack, rr["t"], COH_HALF)
                            wr = window(stack, rr["t_rand"], COH_HALF)
                            if we is None or wr is None:
                                continue
                            iref = names.index(ref)
                            for key, A, B in (("event", we[iref], we), ("R1", wr[iref], wr), ("R2", we[iref], wr)):
                                X = np.vstack([A[None], B]).astype(float)
                                X = X - X.mean(1, keepdims=True)
                                c = MTCoherenceAnalyzer(nts.TimeSeries(X, sampling_rate=1 / BIN))
                                ch = c.coherence[0, 1:]
                                freqs = c.frequencies
                                ch = np.array([np.convolve(x, np.ones(4), "same") / 4 for x in ch])
                                lo, hi = np.searchsorted(freqs, 3), np.searchsorted(freqs, 7)
                                coh[key].append(np.nanmean(ch[:, lo:hi], axis=1))
                            wc = window(stack, rr["t"], CCG_HALF)
                            for j, a in enumerate(names):
                                ccg_sum[a] += np.nan_to_num(crosscorrelogram(wc[iref], wc[j]))
                            ccg_n += 1
                            if lag_names:
                                X = np.vstack([we[iref]] + [we[names.index(a)] for a in lag_names]).astype(float)
                                X = X - X.mean(1, keepdims=True)
                                ca = CoherenceAnalyzer(nts.TimeSeries(X, sampling_rate=1 / BIN))
                                lo, hi = np.searchsorted(ca.frequencies, 3), np.searchsorted(ca.frequencies, 7)
                                with np.errstate(all="ignore"):
                                    lags.append([np.median(ca.delay[0, j + 1][lo:hi]) for j in range(len(lag_names))])
                            # event-triggered CP and VISp rates, -0.5 to 2 s (Figure 8E)
                            if ref == "VISp" and rates.get("CP-RF") is not None and rates.get("CP-noRF") is not None:
                                i0 = int(round((rr["t"] - 0.5) / BIN))
                                if i0 >= 0 and i0 + 250 <= nb:
                                    trig.append(np.stack([rates[k][i0:i0 + 250] for k in ("VISp", "CP-RF", "CP-noRF")]))
                        entry["coh_names"] = names
                        entry["coh"] = {k: np.array(v) for k, v in coh.items()}
                        entry["ccg_mean"] = {a: s / max(ccg_n, 1) for a, s in ccg_sum.items()}
                        entry["ccg_n"] = ccg_n
                        entry["lags"] = pd.DataFrame(lags, columns=lag_names) if lags else pd.DataFrame(columns=lag_names)
                        entry["trig_cp"] = np.array(trig)
                        # replay: VISp units' counts after each qualifying event, and evoked by image
                        if ref == "VISp":
                            vu = g[ref]
                            evq = qv["t"].values
                            ev_counts = {}
                            for wl in (1.0, 1.25):
                                mtx = np.zeros((len(vu), len(evq)))
                                for j, (a, b) in enumerate(zip(u.loc[vu, "a"], u.loc[vu, "b"])):
                                    st = spk[a:b]
                                    mtx[j] = (np.searchsorted(st, evq + wl) - np.searchsorted(st, evq)) / wl
                                ev_counts[wl] = mtx
                            evoked = {}
                            for wl in (0.25, 0.5):
                                mtx = np.zeros((len(vu), len(imgs)))
                                for k2, nm in enumerate(imgs):
                                    s0 = act[(act["image_name"] == nm)]["start_time"].values
                                    for j, (a, b) in enumerate(zip(u.loc[vu, "a"], u.loc[vu, "b"])):
                                        st = spk[a:b]
                                        mtx[j, k2] = np.mean(np.searchsorted(st, s0 + wl) - np.searchsorted(st, s0)) / wl
                                evoked[wl] = mtx
                            entry["replay"] = {"event_rates": ev_counts, "evoked": evoked, "images": imgs,
                                               "event_prev_image": evdf.loc[evdf["qual"], "prev_image"].values,
                                               "event_since_offset": evdf.loc[evdf["qual"], "since_offset"].values}
                    events_out[(L, ref, E)] = entry
            del rates
        out["alpha"] = events_out
        return out
    finally:
        f.close()


CP_RF_SESSIONS = [1182628226, 1182871514, 1183071525, 1194850630, 1195036753]  # code cells 31-35


def _spike_job(args):
    asset_id, units, session_id = args
    return session_spike_products(asset_id, units, session_id, cp_rf_sessions=CP_RF_SESSIONS)


def spike_pass_all(sessions, units, workers=4):
    """session_spike_products for every session, in parallel processes; dict by session id."""
    jobs = [(r.asset_id, units[units["session_id"] == r.session_id], r.session_id)
            for r in sessions.itertuples()]
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(_spike_job, jobs))
    return {r["session_id"]: r for r in res}
