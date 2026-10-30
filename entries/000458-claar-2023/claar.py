"""Loading and measures for dandiset 000458 (Claar, Rembado et al. 2023, eLife 12:RP84630).

Each NWB file holds one session: the raw 30-channel skull EEG (2.5 kHz, int16 with a
conversion to volts), the raw Neuropixels LFP of each probe, sorted units with their CCF area,
waveform duration and quality metrics, the wheel speed (100 Hz), the isoflurane epochs, and a
trial table with the current, target region and depth, behavioural epoch, `is_running` and
`is_valid` of every pulse. Files are streamed from the archive at the pinned version; nothing is
written to disk.

Where the parameters come from (claims file `claims/000458/10.7554-elife.84630.yaml`, the paper's
Methods, or a stated choice):

- Artifact masking, -2 to 0 ms copied, reversed, into 0 to 2 ms (Methods, Data processing,
  Stimulus artifact masking). In every session the artifact peaks at the EEG sample before the
  first sample at or after the trial onset (k - 1; artifact profiles printed in the EEG notebook),
  so the mask starts there: samples k - 1 to k + 4 (-0.4 to +1.6 ms) are replaced by k - 7 to
  k - 2, reversed. The paper's 2 ms are kept after the onset and the artifact sample is added. Good EEG electrodes are those the file marks `is_data_valid`
  (claims file, header, reading (a)). Common average reference over good electrodes, band pass
  0.1 to 100 Hz, third-order Butterworth, on the continuous signal, epochs -2 to +2 s (Methods,
  Data processing, EEG). The filter is applied forward and backward (zero phase); the Methods do
  not say, and this is a standard choice for ERPs that keeps latencies.
- GFP, its z-score to -2 to 0 s, duration and magnitude above z = 3 in 0 to 2 s (Methods, ERP
  magnitude and duration; readings of the claims file, fig1e and fig1f).
- Behavioural state of a trial: quiet when the wheel speed is 0 cm/s throughout -0.5 to +0.5 s,
  running otherwise (Methods, EEG event-related potentials). Recovery stages split at 30 min
  after the end of the isoflurane epoch (Results, Thalamo-cortical interactions..., paragraph 3:
  "in the first 30 min after cessation of isoflurane ... in the subsequent 30 min").
- Intensity: the paper delivered three currents per stage and does not say which it analysed
  (claims file, header). `intensity_levels` gives the readings "high" (the largest current)
  and "medium" (the middle one, which the Methods say was chosen to give visible responses).
- PCIst: the code the paper cites (github.com/renzocom/PCIst at e495a0a), with the paper's
  parameters (Methods, PCI state-transition). `pcist` calls its preprocessing, SVD and SNR
  selection unchanged and replaces only the threshold search of `state_transition_quantification`
  by an exact count that does not store 100 transition matrices (the original needs several GB
  at 2.5 kHz); `pcist_check` compares the two on small inputs.
- Units: the file holds units that "passed our quality threshold" (dandiset description). Unit
  readings: "dataset" (all units in the file) and "siegle" (also presence ratio > 0.9, the third
  threshold of Siegle et al. 2021; the file's units already meet ISI violations < 0.5 and
  amplitude cutoff < 0.1). RS waveform duration > 0.4 ms, FS <= 0.4 ms (Methods, Spike sorting).
  The file's `waveform_duration` is in ms although its description says s.
- Areas (Methods, Neuropixels insertion): cortex MO, ACA, SS, VIS by CCF acronym prefix; SM-TH is
  AV, CL, MD, PO, RT, VAL, VPL, VPM, VM. Stimulated cortex is MO for MOs stimulation and SS for
  SSp stimulation (claims file, header).
- Spikes from 0 to 2 ms after each pulse are removed (Methods, Spike sorting).
- Modulated units (Methods, Significantly modulated neurons): per unit, trial-wise spike counts
  after and before onset in windows of equal length, two-sided Wilcoxon signed-rank (scipy
  default), Benjamini-Hochberg at 0.05; a unit whose differences are all zero is not
  significant (claims file, a standard choice).
- Bursts: two or more spikes with ISI < 4 ms preceded by at least 100 ms of silence (Results,
  CTC interactions, paragraph 2).
"""

from __future__ import annotations

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import signal as sps
from scipy import stats

DANDISET_ID = "000458"
DANDISET_VERSION = "0.230317.0039"   # the version the paper's Data availability cites

FS_EEG = 2500.0
EPOCH = (-2.0, 2.0)
MASK_SAMPLES = 6                    # k - 1 to k + 4: the artifact sample and 2 ms at 2.5 kHz
MASK_START = -1                     # the artifact peaks one sample before the onset sample k
BAND = (0.1, 100.0)
FILTER_ORDER = 3
Z_THRESHOLD = 3.0
PCIST_PAR = dict(baseline_window=(-0.8, -0.002), response_window=(0.002, 0.8), k=1.2,
                 min_snr=1.6, max_var=99, embed=False, n_steps=100)
RS_MIN_MS = 0.4
SM_TH = ("AV", "CL", "MD", "PO", "RT", "VAL", "VPL", "VPM", "VM")
CORTEX = ("MO", "ACA", "SS", "VIS")
STIM_AREA = {"MOs": "MO", "SSp": "SS"}
WINDOWS = {"early": (0.002, 0.025), "off": (0.025, 0.150), "rebound": (0.150, 0.300)}
RECOVERY_SPLIT_S = 30 * 60


# ---------------------------------------------------------------- files

def asset_urls():
    """(path, url) for every asset of the pinned version, sorted by path."""
    ds = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    out = [(a.path, a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets()]
    return sorted(out)


def open_nwb(url):
    return h5py.File(remfile.File(url), "r")


def _str(a):
    return np.array([x.decode() if isinstance(x, bytes) else str(x) for x in a])


def area_group(acronym):
    """Cortical group (MO, ACA, SS, VIS), 'SM-TH', or None."""
    if acronym in SM_TH:
        return "SM-TH"
    for g in CORTEX:
        if acronym.startswith(g):
            return g
    return None


def read_meta(path, url):
    """Session metadata: trials, epochs, EEG electrodes, unit table (without spikes)."""
    f = open_nwb(url)
    tr = f["intervals/trials"]
    trials = pd.DataFrame({k: (_str(tr[k][:]) if tr[k].dtype == object else tr[k][:])
                           for k in tr.keys() if k != "id"})
    trials["trial"] = np.arange(len(trials))
    ep = f["intervals/epochs"]
    epochs = pd.DataFrame({"tag": _str(ep["tags"][:]), "start": ep["start_time"][:], "stop": ep["stop_time"][:]})
    el = f["general/extracellular_ephys/electrodes"]
    elec = pd.DataFrame({k: (_str(el[k][:]) if el[k].dtype == object else el[k][:])
                         for k in ["group_name", "location", "is_data_valid", "x", "y", "z"]})
    units = None
    if "units" in f:
        u = f["units"]
        units = pd.DataFrame({
            "location": _str(u["location"][:]),
            "waveform_duration": u["waveform_duration"][:],
            "presence_ratio": u["presence_ratio"][:],
            "isi_violations": u["isi_violations"][:],
            "amplitude_cutoff": u["amplitude_cutoff"][:],
            "x": u["x"][:], "y": u["y"][:], "z": u["z"][:],
        })
        units["group"] = [area_group(a) for a in units.location]
        units["rs"] = units.waveform_duration > RS_MIN_MS
    rs = f["processing/behavior/BehavioralTimeSeries/running_speed"]
    speed = rs["data"][:]
    speed_t0 = float(rs["starting_time"][()])
    speed_rate = float(rs["starting_time"].attrs["rate"])
    eeg = f["acquisition/ElectricalSeriesEEG/data"]
    meta = {
        "path": path, "url": url, "subject": f["general/subject/subject_id"][()].decode(),
        "session": path.split("_ses-")[1].split("_")[0], "stimulus": f["general/stimulus"][()].decode(),
        "trials": trials, "epochs": epochs, "electrodes": elec, "units": units,
        "speed": speed, "speed_t0": speed_t0, "speed_rate": speed_rate, "speed_unit": rs["data"].attrs["unit"],
        "eeg_shape": eeg.shape, "eeg_conversion": float(eeg.attrs["conversion"]),
        "probes": [k for k in f["acquisition"] if k.startswith("LFP")],
        "electrode_columns": list(el.keys()),
    }
    f.close()
    label_trials(meta)
    return meta


def label_trials(meta):
    """Add `state` (quiet, running, isoflurane, recovery1, recovery2) and `level` columns."""
    t = meta["trials"]
    el = t[t.stimulus_type == "electrical"].copy()
    el["current"] = el.estim_current.astype(float)
    sp, t0, r = meta["speed"], meta["speed_t0"], meta["speed_rate"]
    i0 = np.clip(np.round((el.start_time.values - 0.5 - t0) * r).astype(int), 0, len(sp))
    i1 = np.clip(np.round((el.start_time.values + 0.5 - t0) * r).astype(int) + 1, 0, len(sp))
    el["speed_max"] = [sp[a:b].max() if b > a else np.nan for a, b in zip(i0, i1)]
    el["speed_mean"] = [sp[a:b].mean() if b > a else np.nan for a, b in zip(i0, i1)]
    iso_stop = meta["epochs"].loc[meta["epochs"].tag == "isoflurane_anesthesia", "stop"].max()
    state = np.where(el.behavioral_epoch == "isoflurane", "isoflurane", "")
    awake = el.behavioral_epoch.values == "awake"
    state = np.where(awake & (el.speed_max.values == 0), "quiet", state)
    state = np.where(awake & (el.speed_max.values > 0), "running", state)
    rec = el.behavioral_epoch.values == "recovery"
    since = el.start_time.values - iso_stop
    state = np.where(rec & (since < RECOVERY_SPLIT_S), "recovery1", state)
    state = np.where(rec & (since >= RECOVERY_SPLIT_S) & (since < 2 * RECOVERY_SPLIT_S), "recovery2", state)
    state = np.where(rec & (since >= 2 * RECOVERY_SPLIT_S), "recovery3", state)
    el["state"] = state
    el["site"] = el.estim_target_region + "-" + el.estim_target_depth
    meta["estim"] = el


def intensity_levels(currents):
    """Readings of the intensity: {'high': largest, 'medium': middle, 'low': smallest} of the distinct currents."""
    c = sorted(set(currents))
    return {"high": c[-1], "medium": c[(len(c) - 1) // 2], "low": c[0]}


def site_trials(meta, site, level, valid_only=True):
    """Electrical trials of one site at one intensity reading."""
    el = meta["estim"]
    el = el[el.site == site]
    cur = intensity_levels(el.current)[level]
    el = el[el.current == cur]
    if valid_only:
        el = el[el.is_valid]
    return el


# ---------------------------------------------------------------- EEG

def _sos():
    return sps.butter(FILTER_ORDER, BAND, btype="bandpass", fs=FS_EEG, output="sos")


def eeg_epochs(meta, onsets_by_key, f=None, ts=None, profile=None):
    """Filtered, average-referenced EEG epochs (-2 to +2 s) on the good electrodes.

    `onsets_by_key` maps a key to an array of onset times. Contiguous spans covering the onsets
    are read, masked at every electrical pulse in the span, re-referenced, filtered, and cut.
    Returns {key: array (trials, channels, 10001)} in microvolts, and the times. If `profile` is
    a list, the raw artifact profile of every pulse in the spans is appended to it before masking:
    the largest |EEG| over good electrodes at samples k - 10 to k + 10 (k the first sample at or
    after the onset), relative to the mean of k - 25 to k - 11.
    """
    close = f is None
    if f is None:
        f = open_nwb(meta["url"])
    if ts is None:
        ts = f["acquisition/ElectricalSeriesEEG/timestamps"][:]
    eeg = f["acquisition/ElectricalSeriesEEG/data"]
    good = np.where(meta["electrodes"].query("group_name == 'EEG array'").is_data_valid.values)[0]
    conv = meta["eeg_conversion"] * 1e6
    all_on = meta["estim"].start_time.values
    n0, n1 = int(round(EPOCH[0] * FS_EEG)), int(round(EPOCH[1] * FS_EEG))
    times = np.arange(n0, n1 + 1) / FS_EEG
    sos = _sos()
    # group onsets into spans separated by more than 60 s
    nonempty = [np.asarray(v) for v in onsets_by_key.values() if len(v)]
    if not nonempty:
        return {k: np.zeros((0, len(good), len(times)), np.float32) for k in onsets_by_key}, times
    allsel = np.sort(np.concatenate(nonempty))
    out = {k: [None] * len(v) for k, v in onsets_by_key.items()}
    breaks = np.where(np.diff(allsel) > 60)[0]
    starts = np.r_[allsel[0], allsel[breaks + 1]]
    stops = np.r_[allsel[breaks], allsel[-1]]
    for s0, s1 in zip(starts, stops):
        i0 = max(int(np.searchsorted(ts, s0 - 5)), 0)
        i1 = min(int(np.searchsorted(ts, s1 + 5)), len(ts))
        x = eeg[i0:i1, :][:, good].astype(np.float64) * conv
        for on in all_on[(all_on >= ts[i0]) & (all_on <= ts[i1 - 1])]:
            k = int(np.searchsorted(ts, on)) - i0
            if profile is not None and k - 25 >= 0 and k + 11 <= len(x):
                profile.append(np.abs(x[k - 10:k + 11] - x[k - 25:k - 10].mean(0)).max(1))
            a = k + MASK_START
            if a - MASK_SAMPLES >= 0 and a + MASK_SAMPLES <= len(x):
                x[a:a + MASK_SAMPLES] = x[a - MASK_SAMPLES:a][::-1]
        x -= x.mean(axis=1, keepdims=True)
        for c in range(x.shape[1]):     # channel by channel, to limit memory
            x[:, c] = sps.sosfiltfilt(sos, x[:, c])
        for key, ons in onsets_by_key.items():
            for j, on in enumerate(ons):
                if s0 <= on <= s1:
                    k = int(np.searchsorted(ts, on)) - i0
                    out[key][j] = x[k + n0:k + n1 + 1].T.astype(np.float32)
        del x
    if close:
        f.close()
    return {k: np.stack(v) if len(v) else np.zeros((0, len(good), len(times)), np.float32)
            for k, v in out.items()}, times


def gfp_z(erp, times):
    """Global field power (SD across electrodes) z-scored to -2 to 0 s."""
    g = erp.std(axis=0)
    base = (times >= -2.0) & (times < 0)
    return (g - g[base].mean()) / g[base].std()


def erp_metrics(erp, times):
    """Duration and magnitude of the z-scored GFP above z = 3 in 0 to 2 s, in each reading.

    duration_a: total time above 3; duration_b: onset to the last sample above 3.
    magnitude_a: area above 3 (SD.s); magnitude_b: magnitude_a divided by the area under |z| in
    the baseline (the area under the signed z of a z-scored baseline is zero by construction).
    """
    z = gfp_z(erp, times)
    dt = 1 / FS_EEG
    resp = (times >= 0) & (times <= 2.0)
    base = (times >= -2.0) & (times < 0)
    zr, tr = z[resp], times[resp]
    above = zr > Z_THRESHOLD
    out = {"duration_a": above.sum() * dt,
           "duration_b": (tr[above].max() if above.any() else 0.0),
           "magnitude_a": (zr[above] - Z_THRESHOLD).sum() * dt}
    out["magnitude_b"] = out["magnitude_a"] / (np.abs(z[base]).sum() * dt)
    out["baseline_signed_area"] = z[base].sum() * dt
    return out


def gfp_peaks(erp, times, early, late):
    """Whether the z-scored GFP has a local maximum above z = 3 in each window."""
    z = gfp_z(erp, times)
    res = {}
    for name, (a, b) in (("early", early), ("late", late)):
        m = (times >= a) & (times <= b)
        idx = np.where(m)[0]
        zz = z[idx]
        loc = (zz[1:-1] > zz[:-2]) & (zz[1:-1] >= zz[2:]) & (zz[1:-1] > Z_THRESHOLD)
        res[name] = bool(loc.any())
        res[name + "_max"] = float(zz.max())
        res[name + "_t"] = float(times[idx][np.argmax(zz)])
    return res


# ---------------------------------------------------------------- PCIst

def _stq_fast(sig, times, k, baseline_window, response_window, n_steps=100, **kwargs):
    """state_transition_quantification of PCIst e495a0a without embedding, by exact counting.

    For each component the original builds |x_i - x_j|, and for each of n_steps thresholds
    counts transitions along rows of (D <= thr). A pair of row neighbours (j, j+1) is a
    transition exactly when min <= thr < max, so the count is #(min <= thr) - #(max <= thr).
    """
    from PCIst.pci_st import get_time_index
    bi, be = get_time_index(times, baseline_window[0]), get_time_index(times, baseline_window[1])
    ri, re_ = get_time_index(times, response_window[0]), get_time_index(times, response_window[1])
    nb, nr = be - bi, re_ - ri
    dnst = []
    for c in range(sig.shape[0]):
        b, r = sig[c, bi:be], sig[c, ri:re_]
        Db = np.abs(b[None, :] - b[:, None])
        Dr = np.abs(r[None, :] - r[:, None])
        thr = np.linspace(np.median(Db), Dr.max(), n_steps)

        def nst(D, n):
            lo = np.minimum(D[:, :-1], D[:, 1:]).ravel()
            hi = np.maximum(D[:, :-1], D[:, 1:]).ravel()
            # value <= thr[j]  <=>  j >= searchsorted(thr, value, 'left')
            cl = np.cumsum(np.bincount(np.searchsorted(thr, lo, side="left"), minlength=n_steps + 1))[:n_steps]
            ch = np.cumsum(np.bincount(np.searchsorted(thr, hi, side="left"), minlength=n_steps + 1))[:n_steps]
            return (cl - ch) / n ** 2

        diff = nst(Dr, nr) - k * nst(Db, nb)
        ix = int(np.argmax(diff))
        dnst.append(max(diff[ix] * nr, 0))
    return np.array(dnst)


def pcist(erp, times, fast=True):
    """PCIst of an ERP (channels x time, times in s) with the paper's parameters."""
    from PCIst import pci_st
    par = dict(PCIST_PAR)
    sig, t = pci_st.preprocess_signal(erp.astype(np.float64), times,
                                      (par["baseline_window"][0], par["response_window"][1]), **par)
    svd, _, _, _ = pci_st.dimensionality_reduction(sig, t, **par)
    if svd.shape[0] == 0:
        return 0.0
    if fast:
        return float(np.sum(_stq_fast(svd, t, **par)))
    return float(np.sum(pci_st.state_transition_quantification(svd, t, **par)["dNST"]))


def pcist_check(erp, times, step=10):
    """PCIst of the original code and of `pcist` on the ERP decimated by `step` (small input)."""
    e, t = erp[:, ::step], times[::step]
    return pcist(e, t, fast=False), pcist(e, t, fast=True)


def match_trials(n_by_state, target, rng, how):
    """Indices of `target` trials for each state: random (seeded) or the first ones."""
    out = {}
    for s, n in n_by_state.items():
        if how == "random":
            out[s] = np.sort(rng.choice(n, size=target, replace=False))
        else:
            out[s] = np.arange(target)
    return out


# ---------------------------------------------------------------- spikes

def read_units(meta, groups=CORTEX + ("SM-TH",), f=None):
    """Spike times (s) of the units in the given area groups, with 0 to 2 ms after each pulse removed."""
    close = f is None
    if f is None:
        f = open_nwb(meta["url"])
    u = meta["units"]
    keep = np.where(u.group.isin(groups).values)[0]
    idx = f["units/spike_times_index"][:]
    st = f["units/spike_times"]
    lo = np.r_[0, idx[:-1]]
    allsp = st[:]
    on = np.sort(meta["estim"].start_time.values)
    spikes = []
    for i in keep:
        s = allsp[lo[i]:idx[i]]
        j = np.searchsorted(on, s, side="right") - 1
        art = (j >= 0) & (s - on[np.clip(j, 0, None)] < 0.002) & (s - on[np.clip(j, 0, None)] >= 0)
        spikes.append(np.sort(s[~art]))
    if close:
        f.close()
    table = u.iloc[keep].reset_index().rename(columns={"index": "unit"})
    return table, spikes


def counts(spk, onsets, a, b):
    """Spike counts of one unit in [onset + a, onset + b) for each onset."""
    return np.searchsorted(spk, onsets + b, side="left") - np.searchsorted(spk, onsets + a, side="left")


def signed_rank_p(post, pre):
    d = post - pre
    if not np.any(d != 0):
        return 1.0
    return float(stats.wilcoxon(post, pre).pvalue)


def bh(p):
    p = np.asarray(p, float)
    if len(p) == 0:
        return p
    from scipy.stats import false_discovery_control
    return false_discovery_control(p, method="bh")


def modulation(spikes, onsets, window, pre="adjacent"):
    """p-value and sign (+1 increase, -1 decrease) per unit for a window (s).

    pre 'adjacent': a pre window of the same length ending at onset; 'mirror': -b to -a.
    """
    a, b = window
    pa, pb = (-(b - a), 0.0) if pre == "adjacent" else (-b, -a)
    ps, sg = [], []
    for s in spikes:
        post = counts(s, onsets, a, b)
        prev = counts(s, onsets, pa, pb)
        ps.append(signed_rank_p(post, prev))
        sg.append(np.sign(post.mean() - prev.mean()))
    return np.array(ps), np.array(sg)


def population_rate(spikes, onsets, t0=-2.0, t1=0.5, bin_s=0.001):
    """Mean over units of the trial-averaged rate (Hz) in bins from t0 to t1."""
    edges = np.arange(t0, t1 + bin_s / 2, bin_s)
    rates = []
    for s in spikes:
        h = np.zeros(len(edges) - 1)
        for on in onsets:
            lo, hi = np.searchsorted(s, [on + t0, on + t1])
            h += np.histogram(s[lo:hi] - on, edges)[0]
        rates.append(h / len(onsets) / bin_s)
    centers = edges[:-1] + bin_s / 2
    return centers, np.mean(rates, axis=0) if rates else np.full(len(centers), np.nan)


def single_trial_rate(spikes, onsets, t0, t1, bin_s):
    """Population rate per trial (trials x bins), mean over units, Hz."""
    edges = np.arange(t0, t1 + bin_s / 2, bin_s)
    out = np.zeros((len(onsets), len(edges) - 1))
    for s in spikes:
        for j, on in enumerate(onsets):
            lo, hi = np.searchsorted(s, [on + t0, on + t1])
            out[j] += np.histogram(s[lo:hi] - on, edges)[0]
    return out / max(len(spikes), 1) / bin_s


def quiescence(t, rate, baseline, after=0.025, zero=False, max_gap=0.0):
    """Length (s) of the first run of bins after `after` with rate below baseline (or zero).

    With `max_gap` > 0, runs of bins at or above baseline shorter than `max_gap` do not end the
    period (a robustness reading, so that one noisy bin does not end it; verifier, round 1).
    """
    m = t >= after
    tt, rr = t[m], rate[m]
    low = (rr == 0) if zero else (rr < baseline)
    if not low.any():
        return 0.0
    dt = t[1] - t[0]
    gap = int(round(max_gap / dt))
    i = int(np.argmax(low))
    j = i
    while j < len(low):
        if low[j]:
            j += 1
            continue
        k = j
        while k < len(low) and not low[k]:
            k += 1
        if k - j < gap and k < len(low):
            j = k
        else:
            break
    return (j - i) * dt


def burst_onsets(s, isi=0.004, silence=0.1):
    """Times of the first spike of each burst in a sorted spike train."""
    if len(s) < 2:
        return np.array([])
    d = np.diff(s)
    prev = np.r_[np.inf, d]          # interval before each spike
    nxt = np.r_[d, np.inf]           # interval after each spike
    first = (prev >= silence) & (nxt < isi)
    return s[first]


def bursts_in_window(burst_times, onsets, a=0.075, b=0.300):
    """Boolean per trial: a burst starts in [onset + a, onset + b)."""
    return counts(burst_times, onsets, a, b) > 0


def first_spike_latency(s, onsets, a, b):
    """Latency (s) of the first spike in [onset + a, onset + b) per trial (nan when none)."""
    i = np.searchsorted(s, onsets + a, side="left")
    lat = np.full(len(onsets), np.nan)
    ok = i < len(s)
    v = np.full(len(onsets), np.inf)
    v[ok] = s[i[ok]] - onsets[ok]
    good = v < b
    lat[good] = v[good]
    return lat


# ---------------------------------------------------------------- per-site EEG summary

LEVELS = ("high", "medium")
STATES = ("quiet", "running", "isoflurane", "recovery1", "recovery2")
SEEDS = {"fig7-match": 701, "fig8b": 802, "fig8d": 804, "fig8e": 805, "fig3": 303}
LATE_WINDOW = (0.075, 0.300)        # Figure 6C legend, late ERP component


def _rng(name, meta, site):
    key = int(meta["subject"]) * 10 + (1 if site.endswith("deep") else 0) + (2 if site.startswith("SSp") else 0)
    return np.random.default_rng([SEEDS[name], key, int(meta["session"])])


def eeg_site_summary(meta, site, f=None, ts=None):
    """Every EEG measure the claims use, for one stimulation site of one session.

    Returns counts, ERPs, GFP metrics (unmatched and state-matched), GFP peaks, PCIst under
    each trial-matching reading, and single-trial late-component amplitudes of awake trials.
    """
    keys, tids = {}, {}
    for lvl in LEVELS:
        tr = site_trials(meta, site, lvl)
        for s in STATES:
            sel = tr[tr.state == s]
            keys[(lvl, s)] = sel.start_time.values
            tids[(lvl, s)] = sel.trial.values
    # read each level once (identical levels share the epochs)
    uniq = {}
    for (lvl, s), v in keys.items():
        uniq.setdefault((tuple(np.round(v, 6)), s), (lvl, s))
    prof = []
    ep, times = eeg_epochs(meta, {k: keys[k] for k in set(uniq.values())}, f=f, ts=ts, profile=prof)
    for (lvl, s) in keys:
        if (lvl, s) not in ep:
            ep[(lvl, s)] = ep[uniq[(tuple(np.round(keys[(lvl, s)], 6)), s)]]
    out = {"site": site, "subject": meta["subject"], "session": meta["session"], "times": times,
           "n": {}, "erp": {}, "metrics": {}, "peaks": {}, "pcist": {}, "single": {},
           "artifact": np.median(prof, axis=0) if prof else None, "n_matched": {}}
    for lvl in LEVELS:
        e = {s: ep[(lvl, s)] for s in STATES}
        # awake trials in time order, so that "first" matching takes the earliest awake trials
        order = np.argsort(np.concatenate([keys[(lvl, "quiet")], keys[(lvl, "running")]]), kind="stable")
        e["awake"] = np.concatenate([e["quiet"], e["running"]])[order]
        awake_ids = np.concatenate([tids[(lvl, "quiet")], tids[(lvl, "running")]])[order]
        awake_state = np.array(["quiet"] * len(e["quiet"]) + ["running"] * len(e["running"]))[order]
        for s, x in e.items():
            out["n"][(lvl, s)] = len(x)
            if len(x) == 0:
                continue
            erp = x.mean(0)
            out["erp"][(lvl, s)] = erp
            out["metrics"][(lvl, s, "all")] = erp_metrics(erp, times)
            out["peaks"][(lvl, s)] = {r: gfp_peaks(erp, times, w[0], w[1]) for r, w in
                                      {"a": ((0.002, 0.05), (0.15, 0.3)), "b": ((0.002, 0.025), (0.1, 0.3))}.items()}
        # Figure 7C/7D: states matched to the smallest of quiet, running, isoflurane
        n3 = {s: len(e[s]) for s in ("quiet", "running", "isoflurane")}
        if min(n3.values()) > 0:
            m = match_trials(n3, min(n3.values()), _rng("fig7-match", meta, site), "random")
            for s, idx in m.items():
                out["metrics"][(lvl, s, "matched")] = erp_metrics(e[s][idx].mean(0), times)
        # PCIst
        pc = out["pcist"]
        if len(e["awake"]):
            pc[(lvl, "fig8c", "awake", "all")] = pcist(e["awake"].mean(0), times)
        for how in ("random", "first"):
            n2 = {s: len(e[s]) for s in ("awake", "isoflurane")}
            if min(n2.values()) > 0:
                m = match_trials(n2, min(n2.values()), _rng("fig8b", meta, site), how)
                out["n_matched"][(lvl, "fig8b")] = min(n2.values())
                for s, idx in m.items():
                    pc[(lvl, "fig8b", s, how)] = pcist(e[s][idx].mean(0), times)
            if len(e["running"]) >= 30:
                m = match_trials(n3, min(n3.values()), _rng("fig8d", meta, site), how)
                out["n_matched"][(lvl, "fig8d")] = min(n3.values())
                for s, idx in m.items():
                    pc[(lvl, "fig8d", s, how)] = pcist(e[s][idx].mean(0), times)
            if len(e["recovery1"]):
                st4 = ("awake", "isoflurane", "recovery1") + (("recovery2",) if len(e["recovery2"]) else ())
                n4 = {s: len(e[s]) for s in st4}
                m = match_trials(n4, min(n4.values()), _rng("fig8e", meta, site), how)
                out["n_matched"][(lvl, "fig8e")] = min(n4.values())
                for s, idx in m.items():
                    pc[(lvl, "fig8e", s, how)] = pcist(e[s][idx].mean(0), times)
        # single-trial late component of awake trials (Figure 6C)
        x = e["awake"]
        if len(x):
            w = (times >= LATE_WINDOW[0]) & (times <= LATE_WINDOW[1])
            erp = x.mean(0)
            ch = int(np.argmax(np.abs(erp[:, w]).max(axis=1)))
            out["single"][lvl] = pd.DataFrame({
                "trial": awake_ids,
                "state": awake_state,
                "late_gfp": x[:, :, w].std(axis=1).max(axis=1),
                "late_electrode": np.abs(x[:, ch, :][:, w]).max(axis=1),
            })
    return out


# ---------------------------------------------------------------- per-site spiking summary

MOD_WINDOWS = {"early": (0.002, 0.025), "off": (0.025, 0.150), "rebound": (0.150, 0.300),
               "2-300": (0.002, 0.300), "late75": (0.075, 0.300), "late100": (0.100, 0.300)}
SPIKE_SETS = ("awake", "quiet", "running", "isoflurane")
PRE_READINGS = ("adjacent", "mirror")


def _rel(s, onsets, t0, t1):
    """Spike times relative to each onset in [t0, t1), and the trial index of each."""
    lo = np.searchsorted(s, onsets + t0)
    hi = np.searchsorted(s, onsets + t1)
    n = hi - lo
    if n.sum() == 0:
        return np.array([]), np.array([], int)
    idx = np.concatenate([np.arange(a, b) for a, b in zip(lo, hi)])
    tr = np.repeat(np.arange(len(onsets)), n)
    return s[idx] - onsets[tr], tr


def trial_rates(spikes, onsets, t0, t1, bin_s):
    """Spike counts per unit, trial and bin: array (units, trials, bins), and bin centres."""
    edges = np.arange(t0, t1 + bin_s / 2, bin_s)
    nb = len(edges) - 1
    out = np.zeros((len(spikes), len(onsets), nb), np.float32)
    for u, s in enumerate(spikes):
        rel, tr = _rel(s, onsets, t0, t1)
        b = np.clip(((rel - t0) / bin_s).astype(int), 0, nb - 1)
        np.add.at(out[u], (tr, b), 1)
    return out, edges[:-1] + bin_s / 2


def unit_psth(spikes, onsets, t0, t1, bin_s):
    """Trial-averaged rate (Hz) per unit and bin: (bin centres, array units x bins)."""
    edges = np.arange(t0, t1 + bin_s / 2, bin_s)
    out = np.zeros((len(spikes), len(edges) - 1))
    for u, s in enumerate(spikes):
        rel, _ = _rel(s, onsets, t0, t1)
        out[u] = np.histogram(rel, edges)[0]
    return edges[:-1] + bin_s / 2, out / len(onsets) / bin_s


def spiking_magnitude(spikes, onsets, rng, span, n_shuffle=1000, bin_s=0.001):
    """Population spiking magnitude of Figure 3 (claims file, fig3d-magnitudes criterion; Methods,
    LFP, CSD, and population spiking magnitude).

    The trial-averaged spike density, averaged over units (equal to the mean of the single-unit
    density functions, which are non-negative, so rectifying changes nothing), Gaussian kernel of
    SD 5 or 10 ms, z-scored to the baseline (-2 to 0 s or -0.5 to 0 s), area under the curve from 0
    to 0.5 s; the same for 1000 sets of shuffled onsets, each onset moved uniformly within -2 to
    +2 s ("epoch") or drawn uniformly over the recording ("recording"); magnitude is (AUC minus the
    mean shuffled AUC) over the SD of the shuffled AUCs. Returns {(shuffle, kernel ms, baseline): value};
    shuffle "none" holds the AUC of the z-scored density itself, in SD.s.
    """
    from scipy.ndimage import gaussian_filter1d
    t0, nbin = -2.0, int(round(2.5 / bin_s))
    t = t0 + (np.arange(nbin) + 0.5) * bin_s
    pooled = np.concatenate(spikes)
    nb_total = int(np.ceil((span[1] + 3.0) / bin_s))
    H = np.bincount(np.clip((pooled / bin_s).astype(int), 0, nb_total - 1), minlength=nb_total).astype(np.float32)
    ar = np.arange(nbin)

    def psth(on):
        i0 = np.clip(np.round((on + t0) / bin_s).astype(int), 0, nb_total - nbin)
        return H[i0[:, None] + ar].mean(0) / (len(spikes) * bin_s)

    true = psth(onsets)
    shuffled = {"epoch": np.stack([psth(onsets + rng.uniform(-2.0, 2.0, len(onsets))) for _ in range(n_shuffle)]),
                "recording": np.stack([psth(rng.uniform(span[0] + 2.0, span[1] - 0.5, len(onsets))) for _ in range(n_shuffle)])}
    resp = (t >= 0) & (t < 0.5)
    out = {}
    for kern in (5, 10):
        sm_true = gaussian_filter1d(true, kern * 1e-3 / bin_s, mode="nearest")
        sm_sh = {k: gaussian_filter1d(v, kern * 1e-3 / bin_s, axis=1, mode="nearest") for k, v in shuffled.items()}
        for bname, (b0, b1) in (("-2-0", (-2.0, 0.0)), ("-0.5-0", (-0.5, 0.0))):
            base = (t >= b0) & (t < b1)

            def auc(x):
                mu, sd = x[..., base].mean(-1, keepdims=True), x[..., base].std(-1, keepdims=True)
                z = (x - mu) / np.where(sd > 0, sd, np.nan)
                return np.nansum(z[..., resp], axis=-1) * bin_s

            a_true = auc(sm_true)
            out[("none", kern, bname)] = float(a_true)     # the AUC itself, SD.s, without the shuffle
            for k, v in sm_sh.items():
                a = auc(v)
                out[(k, kern, bname)] = float((a_true - a.mean()) / a.std())
    return out


def spike_site_summary(meta, site, table, spikes):
    """Every spiking measure the claims use for one stimulation site (see the module docstring)."""
    stim = STIM_AREA[site.split("-")[0]]
    tab = table.copy()
    tab["stim"] = tab.group == stim
    cortex = tab.group.isin(CORTEX).values
    smth = (tab.group == "SM-TH").values
    out = {"site": site, "subject": meta["subject"], "session": meta["session"], "units": tab,
           "n": {}, "p": [], "pop": [], "rate": {}, "burst": {}, "latency": {}, "baseline": {}, "trial_ids": {}}
    bursts = [burst_onsets(s) for s in spikes]
    for lvl in LEVELS:
        tr = site_trials(meta, site, lvl)
        sets = {"quiet": tr[tr.state == "quiet"], "running": tr[tr.state == "running"],
                "isoflurane": tr[tr.state == "isoflurane"]}
        sets["awake"] = pd.concat([sets["quiet"], sets["running"]]).sort_values("start_time")
        for name, sel in sets.items():
            on = sel.start_time.values
            out["n"][(lvl, name)] = len(on)
            out["trial_ids"][(lvl, name)] = sel.trial.values
            if len(on) == 0:
                continue
            for w, (a, b) in MOD_WINDOWS.items():
                for pre in PRE_READINGS:
                    if name in ("running",) and pre == "mirror":
                        continue
                    p, sg = modulation(spikes, on, (a, b), pre)
                    out["p"].append(pd.DataFrame({"unit": tab.unit.values, "level": lvl, "trials": name, "window": w,
                                                  "pre": pre, "p": p, "sign": sg}))
            # summed spike counts of the RS units of stimulated and other cortex, signed-rank test
            for area, mask in (("stim", (tab.stim & tab.rs).values), ("nonstim", (~tab.stim & tab.rs & tab.group.isin(CORTEX)).values)):
                if name == "running" or mask.sum() == 0:
                    continue
                for w in ("off", "rebound"):
                    a, b = MOD_WINDOWS[w]
                    for pre in PRE_READINGS:
                        pa, pb = (-(b - a), 0.0) if pre == "adjacent" else (-b, -a)
                        post = sum(counts(x, on, a, b) for x, k in zip(spikes, mask) if k)
                        prev = sum(counts(x, on, pa, pb) for x, k in zip(spikes, mask) if k)
                        out["pop"].append({"level": lvl, "trials": name, "window": w, "pre": pre, "area": area,
                                           "p": signed_rank_p(post, prev), "sign": np.sign(post.mean() - prev.mean())})
            # population rates, 1 ms bins from -2 to +0.5 s, per unit (trial-averaged)
            out["rate"][(lvl, name)] = unit_psth(spikes, on, -2.0, 0.5, 0.001)   # (centres, units x bins in Hz)
            # baseline rates per unit
            out["baseline"][(lvl, name)] = {
                "-2-0": np.array([counts(s, on, -2.0, 0.0).mean() / 2.0 for s in spikes]),
                "-0.5-0": np.array([counts(s, on, -0.5, 0.0).mean() / 0.5 for s in spikes])}
            # bursts (units x trials) in 75-300 ms
            out["burst"][(lvl, name)] = np.array([bursts_in_window(bt, on) for bt in bursts]) if len(spikes) else np.zeros((0, len(on)), bool)
            # first-spike latencies (units x trials)
            for w in ("early", "late75", "late100"):
                a, b = MOD_WINDOWS[w]
                out["latency"][(lvl, name, w)] = np.array([first_spike_latency(s, on, a, b) for s in spikes])
            if name == "awake":
                # single-trial population rates in 75-300 ms, 5 and 10 ms bins
                for bs in (0.005, 0.010):
                    c, _ = trial_rates(spikes, on, 0.075, 0.300, bs)
                    rs_stim = (tab.stim & tab.rs).values
                    out["rate"][(lvl, "single", bs, "stimRS")] = c[rs_stim].mean(axis=0).max(axis=1) / bs if rs_stim.any() else None
                    out["rate"][(lvl, "single", bs, "smth")] = c[smth].mean(axis=0).max(axis=1) / bs if smth.any() else None
    # the lowest current, for the reading that pools the three currents (Figure 4 counts, verifier round 1)
    tr = site_trials(meta, site, "low")
    for name, sel in (("awake", tr[tr.state.isin(["quiet", "running"])]), ("quiet", tr[tr.state == "quiet"])):
        on = np.sort(sel.start_time.values)
        out["n"][("low", name)] = len(on)
        if len(on) == 0:
            continue
        for w in ("early", "off", "rebound"):
            for pre in PRE_READINGS:
                p, sg = modulation(spikes, on, MOD_WINDOWS[w], pre)
                out["p"].append(pd.DataFrame({"unit": tab.unit.values, "level": "low", "trials": name, "window": w,
                                              "pre": pre, "p": p, "sign": sg}))
    # Figure 3 spiking magnitudes of the RS units of each cortical area, all awake trials
    out["magnitude"] = []
    span = (0.0, max((x[-1] for x in spikes if len(x)), default=0.0))
    for lvl in LEVELS:
        tr = site_trials(meta, site, lvl)
        on = np.sort(tr[tr.state.isin(["quiet", "running"])].start_time.values)
        if len(on) == 0:
            continue
        for g in CORTEX:
            mask = ((tab.group == g) & tab.rs).values
            if mask.sum() == 0:
                continue
            rng = np.random.default_rng([SEEDS["fig3"], int(meta["subject"]), int(meta["session"]), CORTEX.index(g),
                                         LEVELS.index(lvl), 1 if site.endswith("deep") else 0, 1 if site.startswith("SSp") else 0])
            mg = spiking_magnitude([x for x, k in zip(spikes, mask) if k], on, rng, span)
            for key, v in mg.items():
                out["magnitude"].append({"level": lvl, "group": g, "stim": g == stim, "units": int(mask.sum()),
                                         "shuffle": key[0], "kernel ms": key[1], "baseline": key[2], "magnitude": v})
    out["magnitude"] = pd.DataFrame(out["magnitude"])
    out["p"] = pd.concat(out["p"]) if out["p"] else pd.DataFrame(columns=["unit", "level", "trials", "window", "pre", "p", "sign"])
    out["pop"] = pd.DataFrame(out["pop"])
    return out


def late_amplitudes(meta, site):
    """Single-trial late ERP amplitudes (75-300 ms) of the awake trials of one site, per level."""
    keys = {}
    for lvl in LEVELS:
        tr = site_trials(meta, site, lvl)
        keys[lvl] = tr[tr.state.isin(["quiet", "running"])].sort_values("start_time")
    ep, times = eeg_epochs(meta, {lvl: v.start_time.values for lvl, v in keys.items()})
    out = {}
    w = (times >= LATE_WINDOW[0]) & (times <= LATE_WINDOW[1])
    for lvl, x in ep.items():
        erp = x.mean(0)
        ch = int(np.argmax(np.abs(erp[:, w]).max(axis=1)))
        out[lvl] = pd.DataFrame({"trial": keys[lvl].trial.values,
                                 "late_gfp": x[:, :, w].std(axis=1).max(axis=1),
                                 "late_electrode": np.abs(x[:, ch, :][:, w]).max(axis=1)})
    return out
