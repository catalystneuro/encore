"""Load the Patch-seq recordings of dandiset 001893 and compute the measures of
Su, Kosillo, Jung et al. (2026), Extended Data Fig. 11k.

Sources of every parameter:

- Dataset and version: DANDI 001893 at 0.260817.1647, the only published version,
  and the one the paper's code (LCNE-patchseq-figures at 79fa20a,
  code/dandi_assets.py) reads.
- Spike waveform (rheobase sweep choice, -10 mV eFEL peaks, -5 to 10 ms average,
  min-max normalisation over -2 to 4 ms, PCA input -3 to 6 ms, SVD): the claim's
  criterion, which takes them from LCNE-patchseq-figures at 79fa20a, code/spikes.py.
  The functions `infer_main_stimulus_pulse`, `detect_efel_peak_indices`,
  `detect_efel_peak_times` and `compute_pc1` follow that file line by line.
- Sweep inclusion rule (bridge balance < 20 MOhm and < 15% of input resistance,
  bias current within +-100 pA, RMS noise < 0.07 mV over 1.5 ms and < 0.5 mV over
  500 ms): Methods, Patch-seq recordings, as the criterion asks. Where the windows
  sit is not in the Methods; they are IPFX's (ipfx.epochs: NOISE_EPOCH = 1.5 ms at
  the start of the experiment epoch, which begins 500 ms before the stimulus;
  PRESTIM_STABILITY_EPOCH = 500 ms ending at the stimulus), because the Methods
  say the features were computed with IPFX (Methods, Patch-seq recordings, last
  sentence) and these are IPFX's QC measures of the same names.
- Input resistance for the 15% rule: IPFX's `input_resistance` over the
  hyperpolarizing subthreshold long squares (stimulus amplitude in (-100, 0) pA),
  as IPFX's LongSquareAnalysis computes it. Which sweeps it is taken from, before
  the bridge rule can be applied, is an assumption: those that pass the noise and
  bias parts of the rule (see `cell_input_resistance`).
- Membrane time constant: IPFX's LongSquareAnalysis.analyze_subthreshold at its
  defaults (subthreshold sweeps with no spike between stimulus start and end,
  amplitude in (-100, 0) pA, fit end capped at the median time of peak
  deflection, tau_frac 0.1, baseline 100 ms, SNR >= 20, mean over sweeps), as the
  criterion asks. Which stimulus sets count as long squares is not stated
  anywhere; the 1 s steps of X1PS_SubThresh, X3LP_Rheo, X4PS_SupraThresh and
  X5LP_Rheo are used (any sweep of these sets whose main pulse lasts at least
  0.8 s), an assumption.
- Cell inclusion (seal > 1 GOhm, initial access resistance < 20 MOhm and < 15%
  of input resistance): Methods, Patch-seq recordings; measured with IPFX's
  qc_features.measure_seal, measure_input_resistance and
  measure_initial_access_resistance on the last cell-attached (EXTPCllATT) and
  last break-in (EXTPBREAKN) voltage-clamp sweeps, as IPFX's
  qc_feature_extractor does.
"""

from __future__ import annotations

import hashlib
import io
import json
import urllib.request

import h5py
import numpy as np
import pandas as pd
import remfile

DANDISET_ID = "001893"
DANDISET_VERSION = "0.260817.1647"
API = "https://api.dandiarchive.org/api"

RHEO_SETS = ("X3LP_Rheo_DA_0", "X5LP_Rheo_DA_0")          # code/spikes.py
LONG_SQUARE_SETS = ("X1PS_SubThresh_DA_0", "X3LP_Rheo_DA_0",
                    "X4PS_SupraThresh_DA_0", "X5LP_Rheo_DA_0")  # assumption, see docstring
SPIKE_THRESHOLD_MV = -10.0                                # code/spikes.py
SPIKE_WINDOW_MS = (-5.0, 10.0)                            # code/spikes.py
MIN_PULSE_S = 0.8                                         # code/spikes.py

# Methods, Patch-seq recordings
BRIDGE_MAX_MOHM = 20.0
BRIDGE_MAX_FRAC_RIN = 0.15
BIAS_MAX_PA = 100.0
PRE_NOISE_MAX_MV = 0.07
SLOW_NOISE_MAX_MV = 0.5
SEAL_MIN_GOHM = 1.0
ACCESS_MAX_MOHM = 20.0
ACCESS_MAX_FRAC_RIN = 0.15

# IPFX defaults (ipfx.epochs, ipfx.stimulus_protocol_analysis.LongSquareAnalysis)
NOISE_EPOCH_S = 0.0015
PRESTIM_STABILITY_S = 0.5
SUBTHRESH_MIN_AMP = -100.0
SUBTHRESH_MAX_AMP = 0.0
TAU_FRAC = 0.1
BASELINE_INTERVAL_S = 0.1


# ----------------------------------------------------------------------------- archive
def _get_json(url):
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def list_assets() -> pd.DataFrame:
    """Every asset of the pinned version, with its path, size and id."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    rows = []
    while url:
        page = _get_json(url)
        rows += page["results"]
        url = page["next"]
    return pd.DataFrame([{"path": a["path"], "size": a["size"], "asset_id": a["asset_id"]}
                         for a in rows])


def asset_url(asset_id: str) -> str:
    return f"{API}/assets/{asset_id}/download/"


def read_text_asset(assets: pd.DataFrame, path: str) -> str:
    aid = assets.loc[assets.path == path, "asset_id"].item()
    with urllib.request.urlopen(asset_url(aid)) as r:
        return r.read().decode()


def read_tsv_asset(assets: pd.DataFrame, path: str) -> pd.DataFrame:
    return pd.read_csv(io.StringIO(read_text_asset(assets, path)), sep="\t", dtype=str)


def nwb_table(assets: pd.DataFrame) -> pd.DataFrame:
    """One row per NWB file: subject, session (the paper's ephys_roi_id), asset id."""
    nwb = assets[assets.path.str.endswith("_icephys.nwb")].copy()
    parts = nwb.path.str.extract(r"sourcedata/raw/(sub-\d+)/sub-\d+_ses-(\d+)_icephys\.nwb")
    nwb["participants_id"] = parts[0]
    nwb["ephys_roi_id"] = parts[1]
    return nwb.reset_index(drop=True)


# ----------------------------------------------------------------------------- code/spikes.py
def infer_main_stimulus_pulse(stimulus_pa):
    """Longest finite pulse relative to the modal baseline (code/spikes.py)."""
    stimulus_pa = np.asarray(stimulus_pa, dtype=float)
    finite = np.isfinite(stimulus_pa)
    edge = max(1, len(stimulus_pa) // 20)
    baseline = float(np.nanmedian(np.concatenate((stimulus_pa[:edge], stimulus_pa[-edge:]))))
    active = finite & ~np.isclose(stimulus_pa, baseline, atol=1e-6, rtol=0.0)
    starts = np.flatnonzero(active & np.r_[True, ~active[:-1]])
    stops = np.flatnonzero(active & np.r_[~active[1:], True]) + 1
    if not len(starts):
        return None
    start, stop = max(zip(starts, stops), key=lambda b: b[1] - b[0])
    amplitude = float(np.nanmedian(stimulus_pa[start:stop]) - baseline)
    return int(start), int(stop), amplitude


def detect_efel_peak_indices(v, threshold_mv=SPIKE_THRESHOLD_MV):
    """eFEL's strict threshold-crossing pairs, maximum in each span (code/spikes.py)."""
    v = np.asarray(v, dtype=float)
    up = np.flatnonzero((v[1:] > threshold_mv) & (v[:-1] < threshold_mv)) + 1
    down = np.flatnonzero((v[1:] < threshold_mv) & (v[:-1] > threshold_mv)) + 1
    while len(up) and len(down) and down[0] < up[0]:
        down = down[1:]
    if len(up) > len(down):
        up = up[:len(down)]
    peaks = []
    for a, b in zip(up, down):
        seg = v[a:b + 1]
        if np.isfinite(seg).any():
            peaks.append(int(a + np.nanargmax(seg)))
    return np.asarray(peaks, dtype=int)


def detect_efel_peak_times(v, rate, threshold_mv=SPIKE_THRESHOLD_MV):
    """Interpolate at the sampling step as eFEL does; peak times in ms (code/spikes.py)."""
    step = 1000.0 / rate
    raw_t = np.arange(len(v)) * step
    n = int(np.ceil(raw_t[-1] / step))
    inc = np.full(n, step)
    inc[0] = 0.0
    it = np.cumsum(inc)
    if it[-1] < raw_t[-1]:
        it = np.append(it, it[-1] + step)
    iv = np.interp(it, raw_t, np.asarray(v, dtype=float))
    return it[detect_efel_peak_indices(iv, threshold_mv)]


def average_spike(v, rate):
    """Mean raw voltage from -5 to 10 ms around every peak of the sweep (code/spikes.py)."""
    peaks = detect_efel_peak_times(v, rate)
    before = round(abs(SPIKE_WINDOW_MS[0]) * rate / 1000.0)
    after = round(SPIKE_WINDOW_MS[1] * rate / 1000.0)
    raw_t = np.arange(len(v)) * 1000.0 / rate
    waves = []
    for p in peaks:
        idx = np.flatnonzero((raw_t >= p + SPIKE_WINDOW_MS[0]) & (raw_t < p + SPIKE_WINDOW_MS[1]))
        if len(idx) == before + after:
            waves.append(v[idx])
    return np.mean(waves, axis=0), len(peaks)


def spike_time_axis(rate=50000.0):
    return np.arange(SPIKE_WINDOW_MS[0], SPIKE_WINDOW_MS[1], 1000.0 / rate)


def compute_pc1(waveforms: pd.DataFrame) -> pd.Series:
    """PC1 of the normalised waveforms (code/spikes.py compute_pc1)."""
    t = np.asarray(waveforms.columns, dtype=float)
    x = waveforms.to_numpy(dtype=float)
    norm = (t >= -2) & (t <= 4)
    x = (x - x[:, norm].min(axis=1, keepdims=True)) / np.ptp(x[:, norm], axis=1, keepdims=True)
    sel = (t >= -3) & (t <= 6)
    c = x[:, sel] - x[:, sel].mean(axis=0)
    u, s, vt = np.linalg.svd(c, full_matrices=False)
    signs = np.sign(vt[np.arange(len(vt)), np.argmax(np.abs(vt), axis=1)])
    signs[signs == 0] = 1
    return pd.Series((u * signs * s)[:, 0], index=waveforms.index, name="PC1")


# ----------------------------------------------------------------------------- reading one cell
def _txt(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def _scaled(ds, scale):
    return (np.asarray(ds, dtype=float) * float(ds.attrs.get("conversion", 1.0))
            + float(ds.attrs.get("offset", 0.0))) * scale


def _ipfx_qc(v, i, rate):
    """IPFX's pre-stimulus noise measures for one current-clamp sweep.

    pre_noise: RMS over the 1.5 ms that open the experiment epoch (500 ms before the
    stimulus onset); slow_noise: RMS over the 500 ms before the stimulus onset
    (ipfx.qc_feature_extractor.current_clamp_sweep_qc_features)."""
    from ipfx import epochs as ep
    from ipfx import qc_features as qcf
    i0 = np.nan_to_num(i)
    stim = ep.get_stim_epoch(i0, test_pulse=True)
    if stim is None:
        return np.nan, np.nan
    s0 = stim[0]
    e0 = s0 - int(ep.PRESTIM_STABILITY_EPOCH * rate)
    a, b = ep.get_first_noise_epoch(e0, rate)
    _, pre = qcf.measure_vm(v[a:b])
    a, b = ep.get_first_stability_epoch(s0, rate)
    _, slow = qcf.measure_vm(v[a:b])
    return pre, slow


def _ipfx_spike_count(t, v, i, start, end):
    from ipfx.feature_extractor import SpikeFeatureExtractor
    try:
        spx = SpikeFeatureExtractor(start=start, end=end)
        return len(spx.process(t, v, i))
    except Exception:
        return -1


def _vc_resistances(h, kind):
    """IPFX measures on the last voltage-clamp sweep of a stimulus set."""
    from ipfx import qc_features as qcf
    names = []
    for k, g in h["acquisition"].items():
        if _txt(g.attrs.get("neurodata_type", "")) == "VoltageClampSeries" and \
                _txt(g.attrs.get("stimulus_description", "")).startswith(kind):
            names.append((int(g.attrs["sweep_number"]), k))
    if not names:
        return None
    sn, k = max(names)
    g = h["acquisition"][k]
    s = h[f"stimulus/presentation/data_{sn:05}_DA0"]
    rate = float(g["starting_time"].attrs["rate"])
    cur = _scaled(g["data"], 1e12)       # pA
    cmd = _scaled(s["data"], 1e3)        # mV
    ok = np.isfinite(cur) & np.isfinite(cmd)
    cur, cmd = cur[ok], cmd[ok]
    t = np.arange(len(cur)) / rate
    out = {"sweep": sn}
    try:
        if kind == "EXTPCllATT":
            out["seal_gohm"] = qcf.measure_seal(cmd, cur, t)
        else:
            out["breakin_rin_mohm"] = qcf.measure_input_resistance(cmd, cur, t)
            out["access_mohm"] = qcf.measure_initial_access_resistance(cmd, cur, t)
    except Exception as e:  # recorded, not hidden
        out["error"] = repr(e)
    return out


def extract_cell(asset_id: str) -> dict:
    """Read what the analysis needs from one NWB file, streamed from DANDI.

    Returns a dict with the sweep table of every current-clamp sweep, the averaged
    spike of every spiking rheobase sweep whose main pulse lasts >= 0.8 s, the
    voltage of every long-square sweep in the subthreshold range (for tau), the
    cell-level resistances, and a digest of the first rheobase sweep's voltage (to
    find recordings deposited twice)."""
    from ipfx.subthresh_features import voltage_deflection  # noqa: F401  (import check)
    f = remfile.File(asset_url(asset_id))
    h = h5py.File(f, "r")
    out = {"asset_id": asset_id,
           "session_start_time": _txt(h["session_start_time"][()]),
           "subject_id": _txt(h["general/subject/subject_id"][()]),
           "subject_sex": _txt(h["general/subject/sex"][()]),
           "subject_age": _txt(h["general/subject/age"][()]),
           "subject_genotype": _txt(h["general/subject/genotype"][()]),
           "filtering": _txt(h["general/intracellular_ephys/filtering"][0])
           if "filtering" in h["general/intracellular_ephys"] else None}
    rows, spikes, subthresh = [], {}, {}
    digest = None
    for k, g in h["acquisition"].items():
        if _txt(g.attrs.get("neurodata_type", "")) != "CurrentClampSeries":
            continue
        sn = int(g.attrs["sweep_number"])
        desc = _txt(g.attrs.get("stimulus_description", ""))
        rate = float(g["starting_time"].attrs["rate"])
        row = {"sweep_number": sn, "stimulus": desc, "rate": rate,
               "n_samples": g["data"].shape[0],
               "unit": _txt(g["data"].attrs.get("unit", "")),
               "bridge_balance_mohm": float(g["bridge_balance"][0]) if "bridge_balance" in g else np.nan,
               "bias_current_pa": float(g["bias_current"][0]) if "bias_current" in g else np.nan}
        if desc in LONG_SQUARE_SETS:
            s = h[f"stimulus/presentation/data_{sn:05}_DA0"]
            i = _scaled(s["data"], 1e12)
            v = _scaled(g["data"], 1e3)
            pulse = infer_main_stimulus_pulse(i)
            row["n_nan"] = int(np.isnan(v).sum())
            row["v_min"], row["v_max"] = float(np.nanmin(v)), float(np.nanmax(v))
            if pulse is not None:
                a, b, amp = pulse
                row.update(pulse_start_s=a / rate, pulse_dur_s=(b - a) / rate, amplitude_pa=amp)
                row["pre_noise_mv"], row["slow_noise_mv"] = _ipfx_qc(v, i, rate)
                long_enough = (b - a) >= MIN_PULSE_S * rate
                peaks = detect_efel_peak_times(v, rate)
                in_pulse = peaks[(peaks >= a * 1000 / rate) & (peaks < b * 1000 / rate)]
                row["n_peaks_pulse"] = len(in_pulse)
                # aborted sweeps: NaN voltage inside the pulse or the 0.5 s after it
                row["aborted"] = bool(np.isnan(v[a:min(len(v), b + int(0.5 * rate))]).any())
                # a stimulus-response check: mean deflection during the first 100 ms of the
                # pulse against the 100 ms before it
                pre = np.nanmean(v[a - int(0.1 * rate):a])
                row["v_base"] = pre
                row["deflection_mv"] = np.nanmean(v[a:a + int(0.1 * rate)]) - pre
                # the same measure with the window moved 200 ms earlier, before the pulse
                sh = a - int(0.2 * rate)
                row["deflection_shifted_mv"] = (np.nanmean(v[sh:sh + int(0.1 * rate)])
                                                - np.nanmean(v[sh - int(0.1 * rate):sh])) if sh > int(0.1 * rate) else np.nan
                if desc in RHEO_SETS and long_enough and len(in_pulse):
                    w, n = average_spike(v, rate)
                    spikes[sn] = w
                    if digest is None:
                        digest = hashlib.sha1(np.nan_to_num(v).tobytes()).hexdigest()
                if long_enough and SUBTHRESH_MIN_AMP < amp < SUBTHRESH_MAX_AMP:
                    lo = max(0, a - int(0.2 * rate))
                    hi = min(len(v), b + int(0.05 * rate))
                    seg_v, seg_i = v[lo:hi], i[lo:hi]
                    t = np.arange(hi - lo) / rate
                    st, en = (a - lo) / rate, (b - lo) / rate
                    row["n_spikes_ipfx"] = _ipfx_spike_count(t, seg_v, seg_i, st, en)
                    subthresh[sn] = (t, seg_v, seg_i, st, en)
        rows.append(row)
    out["sweeps"] = pd.DataFrame(rows).sort_values("sweep_number").reset_index(drop=True)
    out["spikes"] = spikes
    out["subthresh"] = subthresh
    out["rheo_digest"] = digest
    out["seal"] = _vc_resistances(h, "EXTPCllATT")
    out["breakin"] = _vc_resistances(h, "EXTPBREAKN")
    h.close()
    return out


# ----------------------------------------------------------------------------- measures
def noise_bias_pass(sw: pd.DataFrame) -> pd.Series:
    """Parts (2) and (3) of the Methods' sweep rule."""
    return ((sw.bias_current_pa.abs() <= BIAS_MAX_PA)
            & (sw.pre_noise_mv < PRE_NOISE_MAX_MV)
            & (sw.slow_noise_mv < SLOW_NOISE_MAX_MV))


def _subthresh_sweeps(cell, numbers):
    sw = cell["sweeps"].set_index("sweep_number")
    keep = []
    for sn in numbers:
        if sn in cell["subthresh"] and sw.loc[sn, "n_spikes_ipfx"] == 0 and not sw.loc[sn, "aborted"]:
            keep.append(sn)
    return keep


def cell_input_resistance(cell, numbers=None):
    """IPFX input_resistance (MOhm) over the subthreshold hyperpolarizing long squares.

    `numbers`: the sweeps allowed; default all of them."""
    from ipfx.subthresh_features import input_resistance
    if numbers is None:
        numbers = list(cell["subthresh"])
    keep = _subthresh_sweeps(cell, numbers)
    if not keep:
        return np.nan
    ts, is_, vs = [], [], []
    for sn in keep:
        t, v, i, st, en = cell["subthresh"][sn]
        ts.append(t); vs.append(v); is_.append(i)
    st, en = cell["subthresh"][keep[0]][3:5]
    try:
        return float(input_resistance(ts, is_, vs, st, en, BASELINE_INTERVAL_S))
    except Exception:
        return np.nan


def sweep_rule(cell) -> tuple[pd.Series, float]:
    """The Methods' sweep rule for every long-square sweep; returns (pass, Rin used).

    Rin comes from the subthreshold sweeps passing the noise and bias parts (assumption)."""
    sw = cell["sweeps"]
    nb = noise_bias_pass(sw)
    rin = cell_input_resistance(cell, sw.loc[nb, "sweep_number"].tolist())
    bb = sw.bridge_balance_mohm
    ok = nb & (bb < BRIDGE_MAX_MOHM) & (bb < BRIDGE_MAX_FRAC_RIN * rin) & ~sw.get("aborted", False).fillna(False).astype(bool)
    return ok.fillna(False), rin


def rheobase_sweep(cell, allowed=None):
    """Lowest-|amplitude| spiking rheobase sweep with a >= 0.8 s pulse (code/spikes.py).

    `allowed`: sweep numbers that may be chosen (None for the code's reading)."""
    sw = cell["sweeps"].set_index("sweep_number")
    cands = [(abs(sw.loc[sn, "amplitude_pa"]), sn) for sn in cell["spikes"]
             if allowed is None or sn in allowed]
    if not cands:
        return None
    return min(cands)[1]


def ipfx_tau(cell, allowed=None):
    """IPFX LongSquareAnalysis tau (ms) and the number of sweeps it averages."""
    from ipfx.subthresh_features import time_constant, voltage_deflection
    numbers = list(cell["subthresh"]) if allowed is None else [s for s in cell["subthresh"] if s in allowed]
    keep = _subthresh_sweeps(cell, numbers)
    if not keep:
        return np.nan, 0
    peak_times = []
    for sn in keep:
        t, v, i, st, en = cell["subthresh"][sn]
        peak_times.append(t[voltage_deflection(t, v, i, st, en, "min")[1]])
    # sweeps share a layout within a set; the fit end is relative to each sweep's own start
    rel = np.median([pt - cell["subthresh"][sn][3] for pt, sn in zip(peak_times, keep)])
    taus = []
    for sn in keep:
        t, v, i, st, en = cell["subthresh"][sn]
        try:
            taus.append(time_constant(t, v, i, st, en, st + rel, TAU_FRAC, BASELINE_INTERVAL_S))
        except Exception:
            taus.append(np.nan)
    taus = np.asarray(taus, dtype=float)
    return float(np.nanmean(taus) * 1000) if np.isfinite(taus).any() else np.nan, int(np.isfinite(taus).sum())


def welch(a, b):
    from scipy.stats import ttest_ind
    a, b = np.asarray(a, float), np.asarray(b, float)
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    r = ttest_ind(a, b, equal_var=False)
    return {"n_a": len(a), "n_b": len(b), "mean_a": a.mean(), "mean_b": b.mean(),
            "t": float(r.statistic), "df": float(r.df), "p": float(r.pvalue)}


def _extract_quiet(asset_id):
    import warnings
    warnings.filterwarnings("ignore")
    try:
        return extract_cell(asset_id)
    except Exception as e:  # reported by the notebook, never dropped silently
        return repr(e)


def extract_all(asset_ids, workers=12) -> dict:
    """extract_cell for every asset, in parallel processes (the work is network-bound)."""
    import multiprocessing as mp
    from concurrent.futures import ProcessPoolExecutor
    asset_ids = list(asset_ids)
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as pool:
        return dict(zip(asset_ids, pool.map(_extract_quiet, asset_ids)))
