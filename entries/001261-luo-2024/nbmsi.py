"""Loading and electrophysiological features for dandiset 001261.

Luo, Jiang, Desai et al. (2024), "Comparative Physiology and Morphology of BLA-Projecting NBM/SI
Cholinergic Neurons in Mouse and Macaque", J. Comp. Neurol. 532, e70001, doi:10.1002/cne.70001.

Each NWB file holds one neuron: whole-cell current-clamp responses (`acquisition`,
CurrentClampSeries, volts, 10 kHz) to a family of current steps (`stimulus/presentation`, whose
values are in pA although the files label them amperes). The group of the neuron (species,
cholinergic or not) is in `session_description`. Files are read over HTTP into memory from the
archive at the pinned version; nothing is written to disk.

Where the parameters come from. The claims file (claims/001261/10.1002-cne.70001.yaml, opening
comment, "Feature definitions F1 to F18") fixes each feature from Methods 2.5 and the paper's code,
github.com/nsdesai/patch_clamp_analysis at commit 17a3265d280392e73916faee31ee9cea30500c7c
(doi:10.5281/zenodo.10975327). Details it does not give are taken as follows:

- Step onset and the 500 ms analysis window: the code (analysis_of_neurophysiology_data.m) finds
  the step from the largest current step and analyses only its first 500 ms. Here the onset is
  read from each sweep's own stimulus.
- Steps above 200 pA are left out: Methods 2.4, "a family of current steps (500 ms duration, -60
  to 200 pA amplitude)", and Methods 2.5 (16), "a current step between 0 and 200 pA". Some files
  also hold 250 and 300 pA steps; `max_rate_code`, the code's maximum over every step, is kept as a
  variant.
- Most files hold, besides the steps, a short -20 pA pulse (50 or 100 ms, often late in the
  sweep); pulses shorter than `MIN_STEP_MS` are left out as not part of the family of 500 ms
  steps (Methods 2.4). The steps last 500 to 1100 ms; only the first 500 ms are analysed (code).
- A step amplitude recorded more than once (several 200 pA sweeps in some files): a feature defined on one step uses the first sweep of that amplitude in
  recording order, an assumption (the paper gives one sweep per amplitude); `REPEAT` selects the
  other reading, the last sweep, and the notebook shows both. Counting features over all steps
  (rheobase, f-I curve, maximum rate) use every sweep, as the code does once it sorts the steps.
- Spike detection: the code's findpeaks call (height >= 0 mV, prominence >= 30 mV, width <= 5 ms
  at half prominence, peaks >= 5 ms apart), with scipy.signal.find_peaks in place of MATLAB's.
- Median filter of the sag (20 ms) and the fit of tau (a*exp(-t/tau) + c, from 2 ms after onset to
  the end of the step, start values as the code): the code (sagpotential.m, inputresistance.m).
- AHP width (F14) with the Methods' window: the AHP minimum is the one of F12 (100 ms after the
  threshold crossing); the level is threshold minus half the AHP amplitude (code); the width runs
  from the first downward crossing of that level after the threshold crossing to the next upward
  crossing, searched to the end of the step, and to the end of the step when there is none
  (code). The search to the end of the step is an assumption: Methods (14) "the time difference at
  half maximum of the first AHP" gives no window, and the paper's mean AHP width (178 ms, Results
  3.1) is longer than the 100 ms of F12. `ahp_width_window` is the other reading: crossings
  searched within the 100 ms only, and to the end of the step when the potential does not recross
  there.
- Resting potential (F1): the files hold no sweep without bias current. Some file identifiers
  (the original file names) carry a resting potential ("RMP -49.4mV", "_-63mV"); `rmp_from_name`
  reads it, for the neurons that have one.
"""

from __future__ import annotations

import hashlib
import io
import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import requests
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import median_filter
from scipy.optimize import curve_fit
from scipy.signal import find_peaks

DANDISET_ID = "001261"
DANDISET_VERSION = "0.250917.2023"

FS = 10000.0                 # Hz, the files' rate (Methods 2.4, "acquired at 10 kHz")
DT = 1000.0 / FS             # ms
STEP_MS = 500.0              # analysis window (code: analysisDuration = 500)
MIN_STEP_MS = 200.0          # shorter current pulses (50 or 100 ms, -20 pA) are test pulses, not steps
PRE_MS = 100.0               # kept before the step onset
MAX_STEP_PA = 200.0          # Methods 2.4
SAG_STEP = -60.0             # Methods 2.5 (2)
RIN_STEP = -20.0             # Methods 2.5 (3, 4)
DVDT_THRESHOLD = 10.0        # mV/ms, Methods 2.5 (6)
AHP_WINDOW_MS = 100.0        # Methods 2.5 (12)
FEATURES = ["rmp", "sag", "rin", "tau", "rheobase", "threshold", "amplitude", "width", "latency",
            "upstroke", "downstroke", "ahp_amp", "ahp_latency", "ahp_width", "fi_slope",
            "max_rate", "adaptation", "cv_isi"]
LABELS = {"rmp": "resting potential (mV)", "sag": "sag (mV)", "rin": "input resistance (MOhm)",
          "tau": "tau (ms)", "rheobase": "rheobase (pA)", "threshold": "spike threshold (mV)",
          "amplitude": "spike amplitude (mV)", "width": "spike width (ms)",
          "latency": "spike latency (ms)", "upstroke": "upstroke (mV/ms)",
          "downstroke": "downstroke (mV/ms)", "ahp_amp": "AHP amplitude (mV)",
          "ahp_latency": "AHP latency (ms)", "ahp_width": "AHP width (ms)",
          "fi_slope": "f-I slope (Hz/pA)", "max_rate": "max firing rate (Hz)",
          "adaptation": "adaptation index", "cv_isi": "CV of ISI"}


def assets():
    ds = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return sorted(ds.get_assets(), key=lambda a: a.path)


def _text(f, path):
    if path not in f:
        return None
    v = f[path][()]
    return v.decode() if isinstance(v, bytes) else v


def load_file(asset):
    """One neuron: metadata and, per sweep, the step amplitude and the voltage around the step."""
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    raw = requests.get(url, timeout=300).content
    f = h5py.File(io.BytesIO(raw), "r")
    out = {"path": asset.path, "identifier": _text(f, "identifier"),
           "group": _text(f, "session_description"), "subject": _text(f, "general/subject/subject_id"),
           "species": _text(f, "general/subject/species"), "sex": _text(f, "general/subject/sex"),
           "age": _text(f, "general/subject/age"), "notes": _text(f, "general/notes"),
           "session_start": str(_text(f, "session_start_time"))}
    acq, stim = f["acquisition"], f["stimulus/presentation"]
    sweeps = []
    for name in sorted(acq):
        g = acq[name]
        s = stim[g.attrs["stimulus_description"]]
        v = g["data"][:] * float(g["data"].attrs.get("conversion", 1.0))
        i = s["data"][:]
        nz = np.flatnonzero(i)
        sweeps.append({"name": name, "sweep_number": int(g.attrs["sweep_number"]),
                       "rate": float(g["starting_time"].attrs["rate"]), "v_unit": g["data"].attrs["unit"],
                       "i_unit": s["data"].attrs["unit"], "bias": float(g["bias_current"][()]),
                       "n": len(v), "v": v, "i": i, "nz": nz})
    # onset: first sample of the largest step (code: analysis_of_neurophysiology_data.m)
    big = max(sweeps, key=lambda s: np.max(s["i"]))
    onset = int(np.flatnonzero(big["i"] == np.max(big["i"]))[0])
    pre, n_step = int(PRE_MS / DT), int(STEP_MS / DT)
    out["onset_s"] = onset / FS
    out["sweep_s"] = sorted({s["n"] / s["rate"] for s in sweeps})
    out["rates"] = sorted({s["rate"] for s in sweeps})
    out["units"] = sorted({(s["v_unit"], s["i_unit"]) for s in sweeps})
    out["bias"] = sorted({s["bias"] for s in sweeps})
    out["n_sweeps"] = len(sweeps)
    out["hash"] = hashlib.md5(np.concatenate([s["v"] for s in sweeps]).tobytes()).hexdigest()
    out["hash_first"] = hashlib.md5(sweeps[0]["v"].tobytes()).hexdigest()
    keep = []
    for s in sweeps:
        nz = s["nz"]
        amp = float(np.median(s["i"][nz])) if nz.size else 0.0
        on = int(nz[0]) if nz.size else onset  # each sweep's own onset; a 0 pA sweep takes the file's
        keep.append({"sweep_number": s["sweep_number"], "step": amp, "onset_s": on / FS,
                     "duration_ms": nz.size * DT if nz.size else np.nan,
                     "test_pulse": bool(nz.size and nz.size * DT < MIN_STEP_MS),
                     "v": (s["v"][on - pre: on + n_step] * 1000.0).astype(np.float64),
                     "baseline": float(np.mean(s["v"][on - int(10 / DT): on - int(1 / DT)]) * 1000)})
    out["sweeps"] = keep
    return out


def load_all(max_workers=16):
    with ThreadPoolExecutor(max_workers) as ex:
        return list(ex.map(load_file, assets()))


def species_group(group):
    """'Mouse BLA-projecting cholinergic NBM/SI neurons' -> ('mouse', 'C')."""
    sp = "mouse" if group.startswith("Mouse") else "macaque"
    return sp, ("NC" if "noncholinergic" in group else "C")


_RMP = [re.compile(r"RMP\s*-?\s*(\d+(?:\.\d+)?)", re.I), re.compile(r"_(-\d+(?:\.\d+)?)mV")]


def rmp_from_name(identifier):
    """Resting potential written in the file name kept as the NWB identifier, or NaN."""
    for rx in _RMP:
        m = rx.search(identifier)
        if m:
            return -abs(float(m.group(1)))
    return np.nan


# ---------------------------------------------------------------- spike detection (code's findpeaks)

def peaks(v, dt=DT):
    """Indices of spikes in v (mV), the code's findpeaks parameters."""
    w = 5.0 / dt
    p, _ = find_peaks(v, height=0.0, prominence=30.0, distance=max(1, round(w)), width=(None, round(w)))
    return p


def _step_traces(cell, repeat="first"):
    """Sweeps at or below MAX_STEP_PA, sorted by amplitude; for a repeated amplitude, the first
    (or last) sweep in recording order for one-step features."""
    sw = [s for s in cell["sweeps"] if s["step"] <= MAX_STEP_PA + 1e-9 and not s["test_pulse"]]
    sw = sorted(sw, key=lambda s: (s["step"], s["sweep_number"]))
    one = {}
    for s in sw:
        if repeat == "first":
            one.setdefault(s["step"], s)
        else:
            one[s["step"]] = s
    return sw, one


def features(cell, repeat="first"):
    """All features of one neuron, with the variants the claims file names.

    Main readings (Methods 2.5): rin and tau on the -20 pA step; latency to the threshold crossing;
    downstroke from the first peak to 20 ms after it (reading a); AHP on the rheobase step, 100 ms
    after threshold; adaptation and CV on the 200 pA step (reading a). Variants carry a suffix.
    """
    pre, n = int(PRE_MS / DT), int(STEP_MS / DT)
    allsw, one = _step_traces(cell, repeat)
    r = {k: np.nan for k in FEATURES}
    r["rmp"] = rmp_from_name(cell["identifier"])

    # sag, -60 pA step (code: sagpotential.m)
    if SAG_STEP in one:
        v = median_filter(one[SAG_STEP]["v"], size=int(20 / DT), mode="nearest")
        half = n // 2
        sag = np.max(v[pre + half: pre + n - 1]) - np.min(v[pre: pre + half + 1])
        r["sag"] = max(sag, 0.0)

    # input resistance and tau, -20 pA step (Methods; windows of inputresistance.m)
    if RIN_STEP in one:
        v = one[RIN_STEP]["v"]
        base = np.mean(v[pre - int(50 / DT): pre - int(5 / DT)])
        ss = np.mean(v[pre + n - int(100 / DT): pre + n])
        r["rin"] = (ss - base) / RIN_STEP * 1000.0
        r["tau"] = _tau(v, pre, n)
    r["rin_code"], r["tau_code"] = _rin_code(one, pre, n)

    # spikes per sweep over all steps <= 200 pA
    counts = [(s["step"], len(peaks(s["v"][pre: pre + n])), s) for s in allsw]
    spiking = [c for c in counts if c[0] > 0 and c[1] > 0]
    r["n_steps"] = len(one)
    # the code's maximum rate (ficurve.m): over every step, including those above 200 pA
    every = [x for x in cell["sweeps"] if not x["test_pulse"] and x["step"] > 0]
    r["max_rate_code"] = max([len(peaks(x["v"][pre: pre + n])) for x in every], default=0) / (STEP_MS / 1000)
    if not spiking:
        r["max_rate"] = max([c[1] for c in counts if c[0] >= 0], default=0) / (STEP_MS / 1000)
        return r
    rheo_step, _, rheo_sw = spiking[0]
    r["rheobase"] = rheo_step
    rheo_sw = one[rheo_step]  # the chosen sweep of that amplitude
    sp = _spike_shape(rheo_sw["v"][pre: pre + n])
    if sp is None:  # the chosen repeat of the rheobase step has no spike
        rheo_sw = next(s for st, c, s in spiking if st == rheo_step)
        sp = _spike_shape(rheo_sw["v"][pre: pre + n])
    r.update({k: sp[k] for k in ["threshold", "amplitude", "width", "latency", "latency_peak",
                                 "upstroke", "downstroke", "downstroke_code"]})
    # AHP, Methods: rheobase step, 100 ms after threshold
    a = _ahp_methods(rheo_sw["v"][pre: pre + n], sp)
    r["ahp_amp"], r["ahp_latency"], r["ahp_width"] = a
    r["ahp_width_window"] = _ahp_width_window(rheo_sw["v"][pre: pre + n], sp)
    a = _ahp_code([s for st, c, s in counts if st >= rheo_step], pre, n)
    r["ahp_amp_code"], r["ahp_latency_code"], r["ahp_width_code"] = a

    # f-I slope (code: ficurve.m), max firing rate
    dur = STEP_MS / 1000
    steps = np.array([c[0] for c in counts])
    k = np.array([c[1] for c in counts])
    first = int(np.flatnonzero((k > 0) & (steps > 0))[0])
    imax = int(np.argmax(k))
    lo = max(first - 1, 0)
    if imax > lo:
        r["fi_slope"] = np.polyfit(steps[lo: imax + 1], k[lo: imax + 1] / dur, 1)[0]
    pos = steps >= 0
    r["max_rate"] = k[pos].max() / dur
    if MAX_STEP_PA in one:
        r["rate_200"] = len(peaks(one[MAX_STEP_PA]["v"][pre: pre + n])) / dur

    # adaptation and CV: (a) the 200 pA step, (b) the step with the most spikes
    if MAX_STEP_PA in one:
        r["adaptation"], r["cv_isi"] = _adapt(one[MAX_STEP_PA]["v"][pre: pre + n])
    best = counts[imax][2]
    r["adaptation_most"], r["cv_isi_most"] = _adapt(best["v"][pre: pre + n])
    return r


def _tau(v, pre, n):
    """a*exp(-t/tau) + c from 2 ms after onset to the end of the step (inputresistance.m)."""
    y = v[pre + int(2 / DT): pre + n]
    t = np.arange(len(y)) * DT
    try:
        p, _ = curve_fit(lambda t, a, b, c: a * np.exp(-b * t) + c, t, y,
                         p0=[y[0] - y[-1], 0.1, y[-1]], maxfev=20000)
        return 1.0 / p[1] if p[1] > 0 else np.nan
    except RuntimeError:
        return np.nan


def _rin_code(one, pre, n):
    """inputresistance.m: slope of the steady-state deflection over the steps from -50 to 0 pA,
    leaving out steps reaching -20 mV or deflecting more than 50 mV; tau from the first
    (most negative) step kept."""
    steps, vss, tau = [], [], np.nan
    for st in sorted(one):
        if st < -50 or st > 0:
            continue
        r = one[st]["v"][pre - int(50 / DT): pre + n]
        if np.any(r > -20):
            continue
        v0 = np.mean(r[-int(100 / DT):])
        d = v0 - np.mean(r[: int(45 / DT)])
        if abs(d) > 50 or v0 < -150:
            continue
        steps.append(st)
        vss.append(d)
        if np.isnan(tau) and st != 0:
            tau = _tau(one[st]["v"], pre, n)
    steps, vss = np.array(steps), np.array(vss)
    if len(steps) > 1:
        return np.polyfit(steps, vss, 1)[0] * 1000.0, tau
    if len(steps) == 1 and steps[0] != 0:
        return vss[0] / steps[0] * 1000.0, tau
    return np.nan, tau


def _spike_shape(v):
    """First spike of a step (spikeproperties.m): trace interpolated to 10x the rate, threshold
    where dV/dt first exceeds 10 mV/ms from 3 ms before the first peak."""
    t = np.arange(len(v)) * DT
    dt = DT / 10
    t1 = np.arange(0, t[-1] + dt / 2, dt)
    d = np.interp(t1, t, v)
    p = peaks(d, dt)
    if len(p) == 0:
        return None
    p0 = p[0]
    dvdt = np.gradient(d, dt)
    g = dvdt.copy()
    g[: max(p0 - round(3 / dt), 0)] = 0
    above = np.flatnonzero(g > DVDT_THRESHOLD)
    if len(above) == 0:
        return None
    th = int(above[0])
    thr, pk = d[th], d[p0]
    half = thr + (pk - thr) / 2
    cross = np.flatnonzero(np.diff((d >= half).astype(int)))
    width = (cross[1] - cross[0]) * dt if len(cross) > 1 else np.nan
    up0 = max(p0 - round(5 / dt), 0)
    return {"threshold": thr, "amplitude": pk - thr, "width": width, "latency": th * dt,
            "latency_peak": p0 * dt, "upstroke": dvdt[up0: p0 + 1].max(),
            "downstroke": dvdt[p0: p0 + round(20 / dt) + 1].min(),
            "downstroke_code": dvdt[up0:].min(), "th_ms": th * dt}


def _ahp_methods(v, sp):
    """F12 to F14 on the rheobase step: threshold minus the minimum in the 100 ms after the
    threshold crossing; latency from the crossing; width at threshold minus half the amplitude."""
    i0 = int(round(sp["th_ms"] / DT))
    win = v[i0: i0 + int(AHP_WINDOW_MS / DT)]
    imin = int(np.argmin(win))
    amp = sp["threshold"] - win[imin]
    level = sp["threshold"] - amp / 2
    rest = v[i0:]
    below = rest < level
    down = np.flatnonzero(~below[:-1] & below[1:])
    if len(down) == 0:
        return amp, imin * DT, np.nan
    d0 = down[0] + 1
    up = np.flatnonzero(below[d0:-1] & ~below[d0 + 1:])
    end = (up[0] + 1 + d0) if len(up) else len(rest)
    return amp, imin * DT, (end - d0) * DT


def _ahp_width_window(v, sp):
    """Variant of F14: the crossings searched only within the 100 ms window of F12; with no
    upward crossing there, to the end of the step (the code's rule)."""
    i0 = int(round(sp["th_ms"] / DT))
    w = int(AHP_WINDOW_MS / DT)
    win = v[i0: i0 + w]
    amp = sp["threshold"] - win.min()
    below = (win < sp["threshold"] - amp / 2).astype(int)
    cross = np.flatnonzero(np.diff(below))
    if len(cross) > 1:
        return (cross[1] - cross[0]) * DT
    if len(cross) == 1:
        return (len(v) - i0 - cross[0]) * DT
    return np.nan


def _ahp_code(sweeps, pre, n):
    """afterhyperpolarization.m: first step at or above rheobase with two spikes; threshold from
    the raw trace; minimum between 0.75 ms before the first and before the second peak."""
    found = None
    for s in sweeps:
        v = s["v"][pre: pre + n]
        p = peaks(v)
        if len(p) == 0:
            continue
        dvdt = np.gradient(v, DT)
        g = dvdt.copy()
        g[: max(p[0] - round(3 / DT), 0)] = 0
        above = np.flatnonzero(g > DVDT_THRESHOLD)
        if len(above) == 0:
            continue
        thr = v[above[0]]
        locs = p - round(0.75 / DT)
        if len(p) > 1:
            found = (v, thr, locs[0], locs[1])
            break
        found = (v, thr, locs[0], n - 1)
    if found is None:
        return np.nan, np.nan, np.nan
    v, thr, a, b = found
    seg = v[a: b + 1]
    imin = int(np.argmin(seg))
    amp = thr - seg[imin]
    level = thr - amp / 2
    flag = (seg < level).astype(int)
    cross = np.flatnonzero(np.diff(flag))
    if len(cross) > 1:
        w = (cross[1] - cross[0]) * DT
    elif len(cross) == 1:
        w = (len(v) - (a + cross[0])) * DT
    else:
        w = np.nan
    return amp, (imin + 1) * DT, w


def _adapt(v):
    """spikefrequencyadaptation.m: spikes in the second half over the first; CV of the ISIs
    (SD with n - 1 over mean, Methods), 0 with fewer than 3 spikes (code)."""
    p = peaks(v)
    first = int(np.sum(p <= len(v) / 2))
    second = len(p) - first
    ai = second / first if first > 0 else np.nan
    if len(p) < 3:
        return ai, 0.0
    isi = np.diff(p) * DT
    return ai, float(np.std(isi, ddof=1) / np.mean(isi))


# ---------------------------------------------------------------- tables, tests, UMAP and LDA

def responsiveness(cell):
    """Steady-state potential (last 100 ms of the 500 ms window) on the largest step <= 200 pA
    minus that on the most negative step: a cell that follows the injected current depolarises."""
    pre, n = int(PRE_MS / DT), int(STEP_MS / DT)
    sw, one = _step_traces(cell)
    if not one:
        return np.nan
    lo, hi = one[min(one)], one[max(one)]
    ss = lambda s: np.mean(s["v"][pre + n - int(100 / DT): pre + n])
    return ss(hi) - ss(lo)


def onset_contrast(cell, step=SAG_STEP):
    """Mean potential 5 to 25 ms after the stimulus onset minus 20 to 0 ms before it, on the
    -60 pA step; and the same windows 50 ms earlier (-45 to -25 against -70 to -50 ms), where
    nothing should change if the voltage and the stimulus share a clock."""
    s = next((x for x in cell["sweeps"] if x["step"] == step and not x["test_pulse"]), None)
    if s is None:
        return np.nan, np.nan
    pre = int(PRE_MS / DT)
    v = s["v"]
    true = np.mean(v[pre + 50: pre + 250]) - np.mean(v[pre - 200: pre])
    false = np.mean(v[pre - 450: pre - 250]) - np.mean(v[pre - 700: pre - 500])
    return true, false


def ranksum_table(df, mask_a, mask_b, cols):
    """Wilcoxon rank-sum (two-sided, scipy.stats.ranksums, normal approximation as MATLAB ranksum
    uses for these sample sizes) per feature, NaN values dropped; mean +- SD (n - 1) per group."""
    from scipy.stats import ranksums
    rows = []
    for c in cols:
        a = df.loc[mask_a, c].dropna().to_numpy(float)
        b = df.loc[mask_b, c].dropna().to_numpy(float)
        p = ranksums(a, b).pvalue if len(a) > 1 and len(b) > 1 else np.nan
        rows.append({"feature": c, "n_a": len(a), "mean_a": a.mean() if len(a) else np.nan,
                     "sd_a": a.std(ddof=1) if len(a) > 1 else np.nan, "n_b": len(b),
                     "mean_b": b.mean() if len(b) else np.nan, "sd_b": b.std(ddof=1) if len(b) > 1 else np.nan,
                     "p": p})
    import pandas as pd
    return pd.DataFrame(rows).set_index("feature")


def prepare(X, missing):
    """z-score over all neurons of the comparison; missing values (a) 'drop': neurons with any
    missing value dropped, (b) 'impute': set to the feature mean (0 after z-scoring). Returns
    the matrix and the kept rows."""
    X = np.asarray(X, float)
    keep = np.ones(len(X), bool)
    if missing == "drop":
        keep = ~np.isnan(X).any(axis=1)
        X = X[keep]
    mu, sd = np.nanmean(X, axis=0), np.nanstd(X, axis=0, ddof=1)
    Z = (X - mu) / sd
    Z[np.isnan(Z)] = 0.0
    return Z, keep


def pca_keep(Z, min_var=0.01):
    """PCA; components explaining more than 1% of the variance kept (Methods 2.8)."""
    from sklearn.decomposition import PCA
    p = PCA().fit(Z)
    k = int(np.sum(p.explained_variance_ratio_ > min_var))
    return p.transform(Z)[:, :k], k


def misclassified(E, y):
    """Neurons on the wrong side of a linear boundary fitted in the embedding (LDA, resubstitution)."""
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    return int(np.sum(LinearDiscriminantAnalysis().fit(E, y).predict(E) != y))


def umap_separation(X, y, missing, seeds, n_perm, rng):
    """UMAP of the PCA components (Methods 2.8) for each seed; per seed the misclassified count and
    its permutation p (label permutations on the same embedding). UMAP parameters: n_neighbors 15
    and min_dist 0.3, the defaults of Meehan's run_umap that the paper used (a standard choice)."""
    import umap
    Z, keep = prepare(X, missing)
    yk = np.asarray(y)[keep]
    P, k = pca_keep(Z)
    out = []
    for s in seeds:
        E = umap.UMAP(n_neighbors=15, min_dist=0.3, random_state=int(s), n_jobs=1).fit_transform(P)
        m = misclassified(E, yk)
        null = np.array([misclassified(E, rng.permutation(yk)) for _ in range(n_perm)])
        out.append({"seed": s, "n": len(yk), "pcs": k, "misclassified": m,
                     "null_min": int(null.min()), "null_median": float(np.median(null)),
                     "p_perm": (1 + np.sum(null <= m)) / (n_perm + 1)})
    import pandas as pd
    return pd.DataFrame(out)


def lda_separation(X, y, missing, scale, n_shuffle, rng):
    """fitcdiscr-like linear LDA (pooled covariance) on all features; resubstitution accuracy;
    shuffles (i) group labels permuted, (ii) each feature's values permuted across neurons."""
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.model_selection import StratifiedKFold, cross_val_score
    Z, keep = prepare(X, missing)
    yk = np.asarray(y)[keep]
    if scale == "raw":
        Xr = np.asarray(X, float)[keep]
        mu = np.nanmean(Xr, axis=0)
        Z = np.where(np.isnan(Xr), mu, Xr)
    lda = lambda A, b: LinearDiscriminantAnalysis().fit(A, b).score(A, b)
    acc = lda(Z, yk)
    lab = np.array([lda(Z, rng.permutation(yk)) for _ in range(n_shuffle)])
    feat = np.array([lda(np.column_stack([rng.permutation(c) for c in Z.T]), yk) for _ in range(n_shuffle)])
    cv = cross_val_score(LinearDiscriminantAnalysis(), Z, yk,
                         cv=StratifiedKFold(10, shuffle=True, random_state=int(rng.integers(1 << 30)))).mean()
    return {"missing": missing, "scale": scale, "n": len(yk), "accuracy": acc, "cv10_accuracy": cv,
            "label_shuffle_95": np.quantile(lab, 0.95), "label_shuffle_max": lab.max(),
            "p_label": (1 + np.sum(lab >= acc)) / (n_shuffle + 1),
            "feature_shuffle_95": np.quantile(feat, 0.95), "feature_shuffle_max": feat.max(),
            "p_feature": (1 + np.sum(feat >= acc)) / (n_shuffle + 1)}


def lda_weights(X, y, cols, missing):
    """Weights of the z-scored features: (a) |LDA coefficient|, (b) |coefficient x difference of
    the group means| (claims file, opening comment, L)."""
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    import pandas as pd
    Z, keep = prepare(X, missing)
    yk = np.asarray(y)[keep]
    m = LinearDiscriminantAnalysis().fit(Z, yk)
    coef = m.coef_[0]
    diff = Z[yk == m.classes_[1]].mean(0) - Z[yk == m.classes_[0]].mean(0)
    return pd.DataFrame({"a_abs_coef": np.abs(coef), "b_abs_coef_x_diff": np.abs(coef * diff)}, index=cols)
