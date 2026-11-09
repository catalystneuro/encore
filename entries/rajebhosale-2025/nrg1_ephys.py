"""Loading and electrophysiological features for dandiset 001545.

Rajebhosale et al. (2025), Life Science Alliance 8(7) e202403169, doi:10.26508/lsa.202403169.

Each NWB file holds one dentate granule cell recorded in whole-cell current clamp: one
CurrentClampSeries per current step (volts, 10 kHz, 2 s) and the matching
CurrentClampStimulusSeries. The genotype is in the subject id ("NRG VV..." or "NRG LL...") and
the cell type in the session description ("... -- semilunar" or "... -- not semilunar"). Files
are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from. The Methods say only "Twenty features were extracted from the
responses to current steps as reported in Kim et al (2024)" (Methods, Acute slice
electrophysiology). The claims file (opening comment) fixes the definitions, from Kim et al with
the paper's linked code where Kim et al are silent; the code is
https://github.com/nsdesai/patch_clamp_analysis at commit 5d756c2 (folder
basic_scripts_for_analysis), cited below by file name.

- Analysis window: the first 500 ms of the step (analysis_of_neurophysiology_data.m,
  analysisDuration = 500); in these files the step lasts 500 ms.
- Spike detection: peaks above 0 mV, prominence at least 30 mV, at least 5 ms apart and narrower
  than 5 ms (rheobasecurrent.m, ficurve.m).
- RMP: mean voltage from 10 to 1 ms before step onset, averaged over all sweeps
  (analysis_of_neurophysiology_data.m; claims file, opening comment).
- Rheobase: the smallest positive step with a spike (rheobasecurrent.m).
- First spike at rheobase, on the trace interpolated ten-fold (spikeproperties.m). Threshold: the
  first point where dV/dt exceeds THRESHOLD_KIM (20 mV/ms, Kim et al, per the claims file) from
  3 ms before the peak; the code's 10 mV/ms is the variant THRESHOLD_CODE. Width at half height
  between threshold and peak. Amplitude is peak minus threshold. Latency is the peak time from
  step onset (spikeproperties.m).
- Upstroke and downstroke (claims file, opening comment). Kim et al reading: maximum dV/dt from
  threshold to peak, and minimum dV/dt from the peak until the voltage returns to threshold, on
  the first spike. Code reading: maximum and minimum from 5 ms before the first peak to the end of
  the 500 ms window (spikeproperties.m, where downIdx resolves to the window's end).
- Sag and sag ratio from the -60 pA step, 20 ms median filter (sagpotential.m).
- Input resistance. Kim et al reading (claims file): steady-state deflection to the -20 pA step
  (mean of the last 100 ms of the step minus the mean from 50 to 5 ms before it, as in
  inputresistance.m), averaged over the -20 pA sweeps. Code reading: slope of the steady-state
  deflection against current for steps from -50 to 0 pA (inputresistance.m).
- Tau: exponential fit from 2 ms after onset to the end of the first eligible step from -50 to
  0 pA (inputresistance.m).
- AHP amplitude, latency and width: between the first two spikes of the first step from
  rheobase up with two spikes (afterhyperpolarization.m). Where only one crossing of the half
  level exists the code measures to stopLoc, an absolute index; here the width runs to the end
  of the segment (a standard choice; it can only matter for cells without a second spike).
- f-I slope, maximum firing rate, adaptation index, CV and AHP after the maximal step: ficurve.m
  and spikefrequencyadaptation.m.
- Upstroke-downstroke ratio: upstroke divided by the magnitude of downstroke (claims file).
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy.ndimage import median_filter
from scipy.optimize import curve_fit
from scipy.signal import find_peaks

DANDISET_ID = "001545"
DANDISET_VERSION = "0.250809.1653"
API = "https://api.dandiarchive.org/api"

ANALYSIS_MS = 500.0
THRESHOLD_KIM = 20.0   # mV/ms, Kim et al (claims file)
THRESHOLD_CODE = 10.0  # mV/ms, spikeproperties.m
SAG_STEP = -60.0       # pA, analysis_of_neurophysiology_data.m
RN_STEP = -20.0        # pA, Kim et al (claims file)
RN_RANGE = (-50.0, 0.0)  # pA, inputresistance.m

# The 18 features of Fig S2C (claims file, opening comment).
FEATURES_18 = ["spike_width", "downstroke", "threshold", "rheobase", "ahp_width", "spike_latency",
               "cv", "tau", "upstroke", "input_resistance", "max_rate", "spike_amplitude", "sag",
               "rmp", "ahp_latency", "fi_slope", "ahp_amplitude", "adaptation_index"]
# The code's 21 outputs: the 18 plus sag ratio, spike peak and the AHP after the maximal step.
FEATURES_21 = FEATURES_18 + ["sag_ratio", "spike_peak", "ahp_max"]


def list_assets() -> list[dict]:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return sorted(out, key=lambda a: a["path"])


def _text(h, path):
    v = h[path][()]
    if isinstance(v, np.ndarray):
        v = v[0]
    return v.decode() if isinstance(v, bytes) else v


def load_cell(asset: dict) -> dict:
    """Stream one file and return its sweeps (mV, pA) and metadata."""
    # Files are 4 to 8 MB; one large first chunk streams each file in one request.
    h = h5py.File(remfile.File(f"{API}/assets/{asset['asset_id']}/download/", _min_chunk_size=16 * 2**20), "r")
    acq = sorted(h["acquisition"])
    v, i, raw_hash = [], [], []
    for name in acq:
        resp = h["acquisition"][name]
        stim = h["stimulus/presentation"][resp.attrs["stimulus_description"]]
        data = resp["data"][:] * resp["data"].attrs["conversion"]
        v.append(data * 1e3)  # volts to mV
        i.append(stim["data"][:])  # stored values; see the data check for their unit
    rate = float(h["acquisition"][acq[0]]["starting_time"].attrs["rate"])
    desc = _text(h, "session_description")
    subject = _text(h, "general/subject/subject_id")
    cell = dict(
        path=asset["path"], asset_id=asset["asset_id"], identifier=_text(h, "identifier"),
        subject=subject, genotype="WT" if " VV" in subject else ("V321L" if " LL" in subject else "?"),
        cell_type="SGC" if desc.endswith("-- semilunar") else ("GC" if desc.endswith("not semilunar") else "?"),
        session_description=desc, age=_text(h, "general/subject/age"), sex=_text(h, "general/subject/sex"),
        subject_description=_text(h, "general/subject/description"),
        cell_id=_text(h, "general/intracellular_ephys/elec0/cell_id"),
        surgery=_text(h, "general/surgery"), stimulus_text=_text(h, "general/stimulus"),
        session_start=_text(h, "session_start_time"),
        rate=rate, v=np.array(v), i=np.array(i),
        voltage_unit=h["acquisition"][acq[0]]["data"].attrs["unit"],
        stim_unit=h["stimulus/presentation"][h["acquisition"][acq[0]].attrs["stimulus_description"]]["data"].attrs["unit"],
        bias_current=float(h["acquisition"][acq[0]]["bias_current"][()]),
        # amplifier settings as stored in every sweep (sets of distinct values over the sweeps)
        bias_all=sorted({float(h["acquisition"][n]["bias_current"][()]) for n in acq}),
        bridge_all=sorted({float(h["acquisition"][n]["bridge_balance"][()]) for n in acq}),
        capcomp_all=sorted({float(h["acquisition"][n]["capacitance_compensation"][()]) for n in acq}),
        response_start=float(h["acquisition"][acq[0]]["starting_time"][()]),
        stim_start=float(h["stimulus/presentation"][h["acquisition"][acq[0]].attrs["stimulus_description"]]["starting_time"][()]),
    )
    return cell


def load_all(workers: int = 12) -> list[dict]:
    assets = list_assets()
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_cell, assets))


def step_window(cell: dict) -> tuple[int, int, np.ndarray]:
    """Step onset and last sample of the analysis window, and the step amplitude of each sweep.

    As analysis_of_neurophysiology_data.m: the step is where the stimulus of the largest sweep is
    at its maximum; the window is capped at 500 ms. The amplitude of each sweep is the stimulus
    at the end of the window.
    """
    i = cell["i"]
    big = np.argmax(i.max(axis=1))
    on = np.where(i[big] == i[big].max())[0]
    start, stop = on[0], on[-1]
    n = int(np.ceil(ANALYSIS_MS / (1000.0 / cell["rate"])))
    if n < stop - start:
        stop = start + n - 1
    return int(start), int(stop), i[:, stop].copy()


def detect_peaks(r: np.ndarray, dt: float) -> np.ndarray:
    """Spike peaks as in rheobasecurrent.m: above 0 mV, prominence 30 mV, 5 ms apart, under 5 ms wide."""
    if r.max() < 0:
        return np.array([], dtype=int)
    w = int(round(5 / dt))
    pk, _ = find_peaks(r, height=0, distance=w, prominence=30, width=(None, w))
    return pk


def _first_spike(data, dt, threshold):
    """Threshold index and peak of the first spike on an (interpolated) trace, as spikeproperties.m."""
    pk = detect_peaks(data, dt)
    if len(pk) == 0:
        return None
    p0 = pk[0]
    dvdt = np.gradient(data, dt)
    d = dvdt.copy()
    d[: max(p0 - int(round(3 / dt)), 0)] = 0
    above = np.where(d > threshold)[0]
    if len(above) == 0:
        return None
    return dict(pk=pk, p0=p0, th=above[0], dvdt=dvdt)


def features(cell: dict) -> dict:
    """All features of one cell, under the Kim et al reading and the code's variants."""
    dt = 1000.0 / cell["rate"]
    start, stop, steps = step_window(cell)
    order = np.argsort(steps, kind="stable")
    steps = steps[order]
    v = cell["v"][order]
    out: dict = {}

    out["rmp"] = v[:, start - int(round(10 / dt)): start - int(round(1 / dt))].mean(axis=1).mean()

    # sag (sagpotential.m)
    below = np.where(steps - SAG_STEP <= 0)[0]
    if len(below):
        k = below[-1]
        data = median_filter(v[k], size=int(round(20 / dt)), mode="nearest")
        base = data[start - int(round(20 / dt)): start - int(round(1 / dt))].mean()
        mid = start + int(round((stop - start) / 2))
        mn = data[start: mid + 1].min()
        ss = data[mid: stop].max()
        out["sag"] = max(ss - mn, 0.0)
        out["sag_ratio"] = (mn - base) / (ss - base)
        out["sag_step"] = steps[k]
    else:
        out["sag"] = out["sag_ratio"] = out["sag_step"] = np.nan

    # input resistance and tau (inputresistance.m), and the -20 pA reading
    def vss(k):
        r = v[k, start - int(round(50 / dt)): stop + 1]
        if (r > -20).any():
            return np.nan, r
        v0 = r[-int(round(100 / dt)) - 1:].mean()
        d = v0 - r[: int(round(45 / dt))].mean()
        if abs(d) > 50 or v0 < -150:
            return np.nan, r
        return d, r

    sel = np.where((steps >= RN_RANGE[0]) & (steps <= RN_RANGE[1]))[0]
    xs, ys, tau = [], [], np.nan
    for k in sel:
        d, r = vss(k)
        if np.isnan(d):
            continue
        xs.append(steps[k]); ys.append(d)
        if np.isnan(tau):
            rr = r[int(round(52 / dt)):]
            t = np.arange(len(rr)) * dt
            try:
                p, _ = curve_fit(lambda t, a, b, c: a * np.exp(-b * t) + c, t, rr,
                                 p0=[rr[0] - rr[-1], 0.1, rr[-1]], maxfev=20000)
                tau = 1 / p[1]
            except RuntimeError:
                tau = np.nan
    out["tau"] = tau
    out["input_resistance_code"] = 1000 * np.polyfit(xs, ys, 1)[0] if len(xs) > 1 else (
        1000 * ys[0] / xs[0] if len(xs) == 1 and xs[0] != 0 else np.nan)
    m20 = [vss(k)[0] for k in np.where(steps == RN_STEP)[0]]
    m20 = [x for x in m20 if not np.isnan(x)]
    out["input_resistance_kim"] = 1000 * np.mean(m20) / RN_STEP if m20 else np.nan
    out["input_resistance"] = out["input_resistance_kim"]

    # spike counts per step (ficurve.m)
    n_peaks = np.array([len(detect_peaks(v[k, start: stop + 1], dt)) if steps[k] > 0 else 0
                        for k in range(len(steps))])
    spiking = np.where(n_peaks > 0)[0]
    out["n_sweeps"] = len(steps)
    out["max_step"] = steps.max()
    if len(spiking) == 0:
        out["rheobase"] = np.nan
        return out
    rk = spiking[0]
    out["rheobase"] = steps[rk]
    out["n_spikes_rheobase"] = int(n_peaks[rk])

    # first spike at rheobase, ten-fold interpolation (spikeproperties.m)
    data = v[rk, start: stop + 1]
    t = np.arange(len(data)) * dt
    dti = dt / 10
    ti = np.arange(0, t[-1] + dti / 2, dti)
    di = np.interp(ti, t, data)
    for label, thr in (("kim", THRESHOLD_KIM), ("code", THRESHOLD_CODE)):
        fs = _first_spike(di, dti, thr)
        if fs is None:
            for f in ("threshold", "spike_amplitude", "spike_width", "upstroke", "downstroke"):
                out[f"{f}_{label}"] = np.nan
            continue
        p0, th, dvdt = fs["p0"], fs["th"], fs["dvdt"]
        peak = di[p0]
        vth = di[th]
        half = vth + (peak - vth) / 2
        up = np.where(di[:p0] < half)[0]
        dn = np.where(di[p0:] < half)[0]
        width = ((p0 + dn[0]) - (up[-1] + 1)) * dti if len(up) and len(dn) else np.nan
        out[f"threshold_{label}"] = vth
        out[f"spike_amplitude_{label}"] = peak - vth
        out[f"spike_width_{label}"] = width
        # Kim et al reading: on the first spike only
        back = np.where(di[p0:] <= vth)[0]
        end = p0 + back[0] if len(back) else len(di) - 1
        out[f"upstroke_{label}"] = dvdt[th: p0 + 1].max()
        out[f"downstroke_{label}"] = dvdt[p0: end + 1].min()
        out["spike_peak"] = peak
        out["spike_latency"] = p0 * dti
        if label == "code":
            # code reading: from 5 ms before the first peak to the end of the window
            lo = max(p0 - int(round(5 / dti)), 0)
            out["upstroke_codewin"] = dvdt[lo:].max()
            out["downstroke_codewin"] = dvdt[lo:].min()
    # main features: Kim et al reading
    for f in ("threshold", "spike_amplitude", "spike_width", "upstroke", "downstroke"):
        out[f] = out[f"{f}_kim"]
    out["ud_ratio"] = out["upstroke"] / abs(out["downstroke"])
    out["ud_ratio_code"] = out["upstroke_codewin"] / abs(out["downstroke_codewin"])

    # AHP (afterhyperpolarization.m), on the raw trace with the code's 10 mV/ms threshold
    locs, seg, sth = None, None, None
    for k in range(rk, len(steps)):
        r = v[k, start: stop + 1]
        pk = detect_peaks(r, dt)
        if len(pk) == 0:
            continue
        dvdt = np.gradient(r, dt)
        d = dvdt.copy()
        d[: max(pk[0] - int(round(3 / dt)), 0)] = 0
        above = np.where(d > THRESHOLD_CODE)[0]
        sth = r[above[0]] if len(above) else np.nan
        pk = pk - int(round(0.75 / dt))
        seg = r
        if len(pk) > 1:
            locs = pk[:2]
            break
        locs = np.array([pk[0], stop - start])
    s = seg[locs[0]: locs[1] + 1]
    j = int(np.argmin(s))
    out["ahp_amplitude"] = sth - s[j]
    out["ahp_latency"] = (j + 1) * dt
    halfv = sth - out["ahp_amplitude"] / 2
    x = np.where(s < halfv, -200, 0)
    cr = np.where(np.diff(x))[0]
    out["ahp_width"] = (cr[1] - cr[0]) * dt if len(cr) > 1 else ((len(s) - 1 - cr[0]) * dt if len(cr) == 1 else np.nan)

    # f-I curve (ficurve.m)
    dur = (stop - start + 1) * dt / 1000
    out["max_rate"] = n_peaks.max() / dur
    i0, i1 = max(rk - 1, 0), int(np.argmax(n_peaks))
    xs, ys = steps[i0: i1 + 1], n_peaks[i0: i1 + 1] / dur
    out["fi_slope"] = np.polyfit(xs, ys, 1)[0] if len(xs) > 1 else np.nan

    # adaptation, CV and AHP after the maximal step (spikefrequencyadaptation.m)
    km = int(np.argmax(n_peaks))
    r = v[km, start: stop + 1]
    loc = detect_peaks(r, dt) + 1  # MATLAB indices
    first = int((loc <= len(r) / 2).sum())
    out["adaptation_index"] = (len(loc) - first) / first if first > 0 else np.nan
    out["cv"] = np.std(np.diff(loc) * dt, ddof=1) / np.mean(np.diff(loc) * dt) if len(loc) >= 3 else 0.0
    base = v[km, start - int(round(10 / dt)): start - int(round(1 / dt))].mean()
    tail = v[km, stop: stop + int(round(300 / dt)) + 1]
    out["ahp_max"] = base - median_filter(tail, size=10, mode="nearest").min()
    return out


def phase_plot(cell: dict, threshold: float = THRESHOLD_KIM, before_ms: float = 2.0, after_ms: float = 5.0):
    """Vm minus threshold and dV/dt (first difference over the time step, makephaseplot.m) of the
    first spike at rheobase, on the raw 10 kHz trace."""
    dt = 1000.0 / cell["rate"]
    start, stop, steps = step_window(cell)
    order = np.argsort(steps, kind="stable")
    steps, v = steps[order], cell["v"][order]
    for k in range(len(steps)):
        if steps[k] <= 0:
            continue
        r = v[k, start: stop + 1]
        pk = detect_peaks(r, dt)
        if len(pk):
            dvdt = np.diff(r) / dt
            dvdt = np.append(dvdt, dvdt[-1])
            d = dvdt.copy()
            d[: max(pk[0] - int(round(3 / dt)), 0)] = 0
            th = np.where(d > threshold)[0][0]
            a, b = max(pk[0] - int(round(before_ms / dt)), 0), pk[0] + int(round(after_ms / dt))
            return r[a:b] - r[th], dvdt[a:b]
    return None


def feature_table(cells: list[dict]) -> pd.DataFrame:
    rows = []
    for c in cells:
        f = features(c)
        rows.append(dict(cell=c["identifier"], subject=c["subject"], genotype=c["genotype"],
                         cell_type=c["cell_type"], **f))
    return pd.DataFrame(rows)
