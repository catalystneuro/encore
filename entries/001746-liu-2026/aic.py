"""Loading and electrophysiological measures for the Patch-seq recordings of dandiset 001746.

Liu, Huang, Shen, Shao, Jing et al. (2026), Nature Cell Biology,
doi:10.1038/s41556-026-02009-4.

Each NWB file holds one cell: 50 current-clamp sweeps (`CurrentClampSeries001` to `050`, volts)
and the injected current of each (`CurrentClampStimulusSeries001` to `050`, stated in amperes,
the values are pA), 600 ms steps from -200 pA in 20 pA increments. The files carry the subject,
the cell ID (`IntracellularElectrode/cell_id`, also the file's `identifier`) and the amplifier
(device `AXON recording system`, 50 kHz, or `Heka LIH:8+8`, 25 kHz), and no cell type. The cell
types and transcriptomic clusters come from the paper's code table
metaInfo_ephysio_patchSeq.csv, matched by file name. Files are read whole into memory from the
archive at the pinned version; nothing is written to disk.

Where the parameters come from (M = Methods, "Extraction of electrophysiological features" and
"Calculation of the phase peak index"; S = Supplementary Fig. 10 legend; C = PatchAnaLab 1.0,
doi:10.5281/zenodo.19995355, ElectroLab/createFeatures.m, anaAP.m, findSpikes.m, tauFit.m;
A = an assumption, said why; X = a standard choice for a detail that does not change a result):

- Step onset and offset from the stimulus series (the current is nonzero over the step); C finds
  them from the voltage within fixed sample windows, which `stim_window_check` compares.
- Traces low-pass filtered at 1 kHz (2nd-order Butterworth, zero phase) before the AP and
  passive measures (C, filter_1000Lowpass; M silent). The phase plots use the raw trace
  (C, calPhaseHeightIdx.m reads the unfiltered data).
- Spike detection (C, anaAP.m): a sweep's height threshold is the maximum of its 5 Hz low-passed
  trace, smoothed over 1001 samples, from 10% of the sweep on, plus 30 mV; a spike is a run of
  samples above it inside the step, its peak the run's maximum.
- AP threshold, the sample of maximal third derivative in the 20 ms before the peak (M); the
  derivative chain is C's (5-sample smoothing, then 1 kHz filtering of the 2nd and 3rd
  derivatives), computed on the window padded by 2 ms and searched up to the maximal dV/dt, so
  that filter edge transients at the peak are not taken for the threshold (X). C instead starts the window halfway between step onset and the first peak
  (`threshold_window="code"`). Amplitude, peak minus threshold (M). Half-width, the time
  between the rising and the falling crossing of half the threshold-to-peak height (M; the
  falling crossing is the first one after the peak, X). Rise time, threshold to peak (M); decay
  time, peak to the first return below threshold (C). Latency, step onset to threshold (M).
- AP measures come from the first AP of the rheobase sweep, the first sweep with an AP (M, S).
  AHP, trough after the first AP (to the second AP or the step end) minus threshold (M; C's sign).
- Maximal firing rate, the largest AP count over the step divided by 0.6 s (M).
- RMP, mean voltage before the step over all sweeps without a spike before the step (M).
  Steady state, mean of the last 100 ms of the step (M). Input resistance, slope of steady state
  minus RMP against current over the sweeps below the rheobase sweep without APs (M); C's
  variant takes sweeps 1 to 6 (HEKA) or 7 to 11 (Axon) and the last two thirds of the step.
- Sag at the largest hyperpolarizing step (-200 pA, the first sweep): trough, minimum of the
  first third of the step (C); sag ratio (trough - RMP)/(steady state - RMP) (M); sag value
  RMP - steady state (M); sag time and sag area between the two crossings of the steady state
  (M).
- Sag measures at the largest hyperpolarizing step of the file, -200 pA in most files and -60 to
  -120 pA in the others (`sag_step_pA`).
- Tau, fit of a exp(-t/tau) + C from step onset to the minimum of the first third of the step,
  5-sample smoothing (C); averaged over all hyperpolarizing sweeps (M; S panel f). C takes the
  first sweep only, bounded to 10 to 100 ms (`tau_code`). Fits with tau at a bound or failing are
  dropped from the average (X).
- Rebound, maximum of an exponential fitted from step offset to the trace maximum after it, minus
  RMP, on the first sweep (M; C fits the same segment).
- ISI adaptation index, second ISI over first ISI, and amplitude adaptation index, second AP
  amplitude over first, in the sweep of maximal firing (M; the sweep is C's). Latency slope,
  slope of 1/latency against current over the first five sweeps with APs (S panels j, k).
- ISI CV, std/mean of the ISIs of the maximal-rate sweep (C), and ISI Fano factor, their
  variance over mean in ms (A: PatchAnaLab does not compute it; the code table's values fit
  var/mean, Fano = CV^2 x mean ISI).
- Phase peak index, (Psd - Pais)/(Psd + Pais) on dV/dt (mV/ms, 5-sample smoothing, C) against V,
  on the APs of the maximal-rate sweep (C). On each AP's rising phase (threshold to peak), Pais is
  the first local maximum and Psd the largest maximum after it; with one maximum only, the point
  before it where d2V/dt2 has its lowest local minimum (the shoulder of the rise) stands for
  the missing AIS peak (the claim's criterion). With neither (the AIS phase not resolved), the AIS
  "peak" is the point of the rising phase with the lowest dV/dt (M, "If there was no clear phase
  peak, the point with the lowest derivative value was defined as the phase peak"; A, as the
  criterion leaves this case open), which is where the rising phase starts, so the index is near
  (1 - 0.1)/(1 + 0.1) = 0.82; the variant `_x` leaves such APs out. Local maxima count when their
  prominence is at least `PROMINENCE_FRAC` of the AP's maximal dV/dt (X, against noise; the
  notebook shows 0.02 and 0.10). The rising phase starts where dV/dt first
  exceeds 10% of its maximum (X, so that noise at threshold is not read as the AIS peak).
"""

from __future__ import annotations

import hashlib
import io
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests
from scipy.ndimage import uniform_filter1d
from scipy.optimize import curve_fit
from scipy.signal import butter, filtfilt, find_peaks

DANDISET_ID = "001746"
DANDISET_VERSION = "0.260825.0222"
API = "https://api.dandiarchive.org/api"

CODE_COMMIT = "44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d"
CODE_RAW = f"https://raw.githubusercontent.com/RFLiu2021/AIC_proj/{CODE_COMMIT}"
META_CSV = f"{CODE_RAW}/ephysio/data_ephy/rawdata_ephysio/metaInfo_ephysio_patchSeq.csv"
FEATURE_XLSX = f"{CODE_RAW}/ephysio/data_ephy/Ins_patchseq_ephs.xlsx"
PEAKIDX_XLSX = f"{CODE_RAW}/ephysio/data_ephy/PeakIdx_Fig5e.xlsx"
AIS_MAT = f"{CODE_RAW}/ephysio/data_ephy/NeuronPeakIdx_summary.mat"
MORPH_XLSX = f"{CODE_RAW}/morpho/dataMorph/morphFeatMatrix.xlsx"

# The 10x excitatory neurons with their clusters (GEO GSE319557, member Ext.h5ad of the h5ad archive).
GEO_H5AD_TAR = ("https://ftp.ncbi.nlm.nih.gov/geo/series/GSE319nnn/GSE319557/suppl/"
                "GSE319557_AIC_scRNA_h5ad.tar.gz")
GEO_MEMBER = "AIC_scRNA_h5ad/Ext.h5ad"

STEP_S = 0.6                 # M, 600 ms steps
PRE_SPIKE_OFFSET_MV = 30.0   # C, anaAP.m height = max(smoothed) + 30
THRESH_WINDOW_MS = 20.0      # M, 20 ms before the peak
STEADY_MS = 100.0            # M, last 100 ms of the step
PROMINENCE_FRAC = 0.05       # X, see docstring
TAKEOFF_FRAC = 0.10          # X, see phase_index

# Subclasses by predicted cluster number (calFDR_ephsio.m and the claims file's opening comment).
CLUSTERS = {
    "L2/3 IT HPCAL1": [1, 15, 5],
    "IT RORB": [2, 0, 7, 13, 19],
    "L5 IT FEZF2": [3, 6, 9, 11, 14, 18],
    "L6 PC": [4, 12, 17],
}
GROUPS = ["L2/3 IT HPCAL1", "IT RORB", "L5 IT FEZF2", "VEN", "L5 ET", "L6 PC"]


def code_group(cluster, cell_type):
    """Fig. 2 group of a cell as calFDR_ephsio.m forms it; None when the cell is in none."""
    if cluster is None or np.isnan(cluster):
        return None
    c = int(cluster)
    t = str(cell_type).lower()
    for g, cl in CLUSTERS.items():
        if c in cl:
            return g
    if c == 16:
        if "ven" in t:
            return "VEN"
        if "pc" in t:
            return "L5 ET"
    if c == 8 and "ven" in t:
        return "VEN"
    return None


# ----------------------------------------------------------------------------- archive


def list_assets(version=DANDISET_VERSION):
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return out


def asset_metadata(asset_id, version=DANDISET_VERSION):
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/{asset_id}/",
                        timeout=60).json()


def read_nwb(asset_id):
    """The file's sweeps and metadata, read whole into memory (no disk)."""
    for attempt in range(4):
        try:
            r = requests.get(f"{API}/assets/{asset_id}/download/", timeout=300)
            r.raise_for_status()
            break
        except Exception:
            if attempt == 3:
                raise
    f = h5py.File(io.BytesIO(r.content), "r")
    acq = sorted(f["acquisition"])
    sti = sorted(f["stimulus/presentation"])
    s0 = f["acquisition"][acq[0]]
    dec = lambda x: x.decode() if isinstance(x, bytes) else str(x)
    # every object path (digits replaced by #) and every string value or attribute outside the
    # sweeps and the format specifications, to look for annotations outside the fields read below
    paths, strings = set(), []
    def visit(name, obj):
        paths.add("".join("#" if ch.isdigit() else ch for ch in name))
        if name.startswith("specifications") or "Series" in name:
            return
        vals = list(obj.attrs.values())
        if isinstance(obj, h5py.Dataset) and obj.dtype.kind in "OSU" and obj.size <= 1000:
            vals += list(np.atleast_1d(obj[()]))
        for v in vals:
            for x in np.atleast_1d(v):
                if isinstance(x, (bytes, str)):
                    strings.append((name, x.decode(errors="replace") if isinstance(x, bytes) else x))
    f.visititems(visit)
    out = {
        "h5_paths": paths,
        "h5_strings": strings,
        "V": np.stack([f["acquisition"][k]["data"][:] * f["acquisition"][k]["data"].attrs.get("conversion", 1.0)
                       for k in acq]),
        "I": np.stack([f["stimulus/presentation"][k]["data"][:] for k in sti]),
        "fs": float(s0["starting_time"].attrs["rate"]),
        "v_unit": dec(s0["data"].attrs["unit"]),
        "i_unit": dec(f["stimulus/presentation"][sti[0]]["data"].attrs["unit"]),
        "v_start": float(s0["starting_time"][()]),
        "i_start": float(f["stimulus/presentation"][sti[0]]["starting_time"][()]),
        "sweep_numbers": [int(f["acquisition"][k].attrs["sweep_number"]) for k in acq],
        "device": list(f["general/devices"].keys())[0],
        "cell_id": dec(f["general/intracellular_ephys/IntracellularElectrode/cell_id"][()]),
        "identifier": dec(f["identifier"][()]),
        "subject_id": dec(f["general/subject/subject_id"][()]),
        "sex": dec(f["general/subject/sex"][()]),
        "species": dec(f["general/subject/species"][()]),
        "session_id": dec(f["general/session_id"][()]),
        "session_start": dec(f["session_start_time"][()]),
    }
    f.close()
    return out


# ----------------------------------------------------------------------------- signal helpers


def lowpass(x, fs, fc, order):
    b, a = butter(order, fc / (0.5 * fs), "low")
    return filtfilt(b, a, x, axis=-1)


def smooth(x, span):
    """Moving average (MATLAB `smooth` without its end handling; X)."""
    return uniform_filter1d(np.asarray(x, float), size=int(span), mode="nearest")


def step_indices(I):
    """Onset and offset sample of the step, from the sweep of largest |current|."""
    k = int(np.argmax(np.abs(I).max(axis=1)))
    nz = np.flatnonzero(I[k] != 0)
    return int(nz[0]), int(nz[-1]) + 1


def code_stim_window(vtrace, device):
    """Step onset and offset as findStimPeriod.m finds them in the voltage (C)."""
    raw = [5600, 6200, 35600, 36200] if device.startswith("AXON") else [2300, 2700, 17300, 17700]
    if len(vtrace) < raw[3] + 3:
        return np.nan, np.nan
    ddd = smooth(np.diff(np.diff(vtrace)), 5)
    a = raw[0] + min(np.argmax(ddd[raw[0]:raw[1]]), np.argmin(ddd[raw[0]:raw[1]]))
    b = raw[2] + min(np.argmax(ddd[raw[2]:raw[3]]), np.argmin(ddd[raw[2]:raw[3]]))
    return a, b


def detect_spikes(v, fs, on, off):
    """Peak samples of the APs inside the step (C, anaAP.m and findSpikes.m)."""
    fd = lowpass(v, fs, 5, 1)
    fd = smooth(fd[int(round(len(fd) * 0.1)):], 1001)
    height = fd.max() + PRE_SPIKE_OFFSET_MV
    seg = v[on:off] > height
    if not seg.any():
        return np.array([], int)
    d = np.diff(seg.astype(int))
    starts = list(np.flatnonzero(d == 1) + 1)
    ends = list(np.flatnonzero(d == -1) + 1)
    if seg[0]:
        starts = [0] + starts
    if seg[-1]:
        ends = ends + [len(seg)]
    peaks = np.array([on + s + int(np.argmax(v[on + s:on + e])) for s, e in zip(starts, ends)], int)
    return peaks


def ap_threshold(v, fs, start, peak):
    """Sample of maximal third derivative in v[start:peak] (M; derivative chain of C).

    The derivatives are computed on the window padded by 2 ms on each side, and the maximum is
    sought from the window's start to the point of maximal dV/dt, where the threshold must lie, so
    that neither the zero-phase filters' edge transients at the AP peak, where the window ends,
    nor the curvature near the peak can be taken for the threshold (X).
    """
    if peak + 1 - start < 40:
        return start
    pad = int(0.002 * fs)
    lo, hi = max(start - pad, 0), min(peak + 1 + pad, len(v))
    seg = smooth(v[lo:hi], 5)
    dd = np.diff(seg)
    ddd = lowpass(np.diff(dd), fs, 1000, 2)
    dddd = lowpass(np.diff(ddd), fs, 1000, 2)
    a, b = start - lo, peak - lo  # dddd[i] belongs to sample lo + i (as in the unpadded chain)
    b = a + max(int(np.argmax(dd[a:b])), 1)  # up to the maximal rise
    return start + int(np.argmax(dddd[a:b]))


def ap_measures(v, fs, peaks, k, on, off, window="methods"):
    """Threshold, amplitude, half-width, rise, decay and latency of AP k of a sweep."""
    p = peaks[k]
    if window == "methods":
        start = max(p - int(THRESH_WINDOW_MS * fs / 1000), on if k == 0 else (peaks[k - 1] + p) // 2)
    else:  # C: halfway between the step onset (or previous peak) and the peak
        start = (on + p) // 2 if k == 0 else (peaks[k - 1] + p) // 2
    ti = ap_threshold(v, fs, start, p)
    thr, vp = v[ti], v[p]
    half = (thr + vp) / 2
    end = (p + peaks[k + 1]) // 2 if k + 1 < len(peaks) else off
    left = v[ti:p + 1]
    right = v[p:end]
    below = np.flatnonzero(left < half)
    up = ti + (below[-1] + 1 if len(below) else 0)
    down_idx = np.flatnonzero(right < half)
    hw = (p + down_idx[0] - up) / fs * 1000 if len(down_idx) else np.nan
    dec = np.flatnonzero(right < thr)
    return {
        "threshold": thr, "thr_idx": ti, "amplitude": vp - thr, "half_width": hw,
        "rise": (p - ti) / fs * 1000, "decay": dec[0] / fs * 1000 if len(dec) else np.nan,
        "latency": (ti - on) / fs * 1000,
    }


def _exp(t, a, tau, c):
    return a * np.exp(-t / tau) + c


def fit_tau(v, fs, on, off, bounds=(0.1, 500.0)):
    """Tau (ms) from step onset to the minimum of the first third of the step (C, M)."""
    seg = smooth(v[on:off], 5)
    seg = seg[: len(seg) // 3]
    seg = seg[: int(np.argmin(seg)) + 1]
    if len(seg) < 10:
        return np.nan
    t = np.arange(len(seg)) / fs * 1000
    y = seg - seg.min()
    try:
        p, _ = curve_fit(_exp, t, y, p0=[max(y[0], 1e-3), 20.0, 0.0],
                         bounds=([0, bounds[0], -np.inf], [np.inf, bounds[1], np.inf]), maxfev=5000)
    except Exception:
        return np.nan
    tau = p[1]
    if np.isclose(tau, bounds[0], rtol=1e-3) or np.isclose(tau, bounds[1], rtol=1e-3):
        return np.nan
    return tau


def rebound_value(v, fs, off, rmp):
    seg = lowpass(v[off:], fs, 300, 2)
    m = int(np.argmax(seg))
    seg = smooth(seg[: m + 1], 5)
    if len(seg) < 10:
        return np.nan
    t = np.arange(len(seg)) / fs * 1000
    try:
        p, _ = curve_fit(_exp, t, seg, p0=[seg[0] - seg[-1], 20.0, seg[-1]], maxfev=5000)
        return float(_exp(t, *p).max() - rmp)
    except Exception:
        return float(seg.max() - rmp)


# ----------------------------------------------------------------------------- phase peak index


def phase_index(vraw, fs, thr_idx, peak_idx, prominence_frac=PROMINENCE_FRAC):
    """Automatic phase peak index of one AP; also says whether there were two maxima.

    The rising phase is taken from where dV/dt first exceeds `TAKEOFF_FRAC` of its maximum (X,
    so that noise at threshold is not read as a peak) to the AP peak.
    """
    lo = max(thr_idx - 2, 1)
    seg = vraw[lo - 1:peak_idx + 2]
    dvdt = smooth(np.diff(seg) * fs / 1000.0, 5)  # mV/ms
    if len(dvdt) < 5:
        return np.nan, False
    g = int(np.argmax(dvdt))
    gmax = dvdt[g]
    if gmax <= 0:  # no rise in the raw trace between threshold and peak
        return np.nan, "failed"
    start = int(np.flatnonzero(dvdt >= TAKEOFF_FRAC * gmax)[0])
    rising = dvdt[start:]
    pk, _ = find_peaks(rising, prominence=prominence_frac * gmax if prominence_frac > 0 else None)
    if len(pk) >= 2:
        return (rising[pk[1:]].max() - rising[pk[0]]) / (rising[pk[1:]].max() + rising[pk[0]]), "two"
    g = g - start
    mins = np.array([], int)
    if g >= 3:
        d2 = np.diff(rising[: g + 1])
        mins, _ = find_peaks(-d2)  # interior local minima of d2V/dt2: the shoulder of the rise
    if len(mins):
        j = int(mins[np.argmin(d2[mins])]) + 1
        p_ais = rising[j]
        return (gmax - p_ais) / (gmax + p_ais), "shoulder"
    # No AIS peak and no shoulder: the AIS phase is not resolved. Its "peak" is the point with the
    # lowest derivative value (M), the lowest dV/dt of the rising phase.
    p_ais = rising[: g + 1].min()
    return (gmax - p_ais) / (gmax + p_ais), "none"


# ----------------------------------------------------------------------------- features


def cell_features(rec):
    """Every per-cell measure the notebook uses, from one file's sweeps (see docstring)."""
    fs = rec["fs"]
    Vraw = rec["V"] * 1000.0  # mV
    I = rec["I"]
    on, off = step_indices(I)
    V = lowpass(Vraw, fs, 1000, 2)
    amps = I[:, on + (off - on) // 2]
    n = len(V)
    peaks = [detect_spikes(V[s], fs, on, off) for s in range(n)]
    counts = np.array([len(p) for p in peaks])
    pre = [s for s in range(n) if len(detect_spikes(V[s], fs, 0, on)) == 0] or list(range(n))
    rmp = float(np.mean([V[s, 100:on].mean() for s in pre]))
    ss = np.array([V[s, off - int(STEADY_MS * fs / 1000):off].mean() for s in range(n)])
    out = {"cell_id": rec["cell_id"], "fs": fs, "n_sweeps": n, "on": on, "off": off,
           "step_ms": (off - on) / fs * 1000, "i_min": amps.min(), "i_max": amps.max(),
           "i_step": float(np.median(np.diff(amps))), "RMP": rmp,
           "v_min": float(Vraw.min()), "v_max": float(Vraw.max()),
           "n_spiking_sweeps": int((counts > 0).sum())}
    # clock check: the voltage response to the largest hyperpolarizing step, at the stimulus
    # onset and at a time 100 ms earlier, where no step begins (10 ms windows either side)
    s_neg = int(np.argmin(amps))
    w = int(0.010 * fs)
    resp = lambda t0: float(V[s_neg, t0 + w // 20:t0 + w].mean() - V[s_neg, t0 - w:t0].mean())
    out["resp_at_onset"] = resp(on)
    out["resp_100ms_before"] = resp(on - int(0.1 * fs))
    out["resp_at_offset"] = resp(off)
    c_on, c_off = code_stim_window(Vraw[0], rec["device"])
    out["code_on_minus_stim_on"] = c_on - on
    out["code_off_minus_stim_off"] = c_off - off
    # hyperpolarizing sweeps: tau, sag
    hyp = [s for s in range(n) if amps[s] < 0]
    taus = [fit_tau(V[s], fs, on, off) for s in hyp]
    out["tau_methods"] = float(np.nanmean(taus)) if np.isfinite(taus).any() else np.nan
    out["tau_n_fits"] = int(np.isfinite(taus).sum())
    out["tau_n_sweeps"] = len(hyp)
    out["tau_sweep_median"] = float(np.nanmedian(taus)) if np.isfinite(taus).any() else np.nan
    out["tau_sweep_min"] = float(np.nanmin(taus)) if np.isfinite(taus).any() else np.nan
    out["tau_sweep_max"] = float(np.nanmax(taus)) if np.isfinite(taus).any() else np.nan
    out["sag_step_pA"] = float(amps.min())
    out["tau_code"] = fit_tau(V[0], fs, on, off, bounds=(10.0, 100.0))
    s0 = int(np.argmin(amps))
    first = smooth(V[s0, on:off], 5)
    trough = first[: len(first) // 3].min()
    out["sag_ratio"] = (trough - rmp) / (ss[s0] - rmp)
    out["sag_value"] = rmp - ss[s0]
    below = np.flatnonzero(first < ss[s0])
    if len(below):
        a = below[0]
        tmin = int(np.argmin(first[: len(first) // 3]))
        back = np.flatnonzero(first[tmin:] >= ss[s0])
        b = tmin + back[0] if len(back) else len(first)
        out["sag_time"] = (b - a) / fs * 1000
        out["sag_area"] = float(np.sum(ss[s0] - first[a:b]) / fs * 1000)
    else:
        out["sag_time"] = 0.0
        out["sag_area"] = 0.0
    out["rebound"] = rebound_value(V[s0], fs, off, rmp)
    # input resistance
    spk = np.flatnonzero(counts > 0)
    rh = int(spk[0]) if len(spk) else n
    sub = [s for s in range(rh) if counts[s] == 0]
    if len(sub) >= 2:
        out["Rm_methods"] = float(np.polyfit(amps[sub], ss[sub] - rmp, 1)[0] * 1000)
    else:
        out["Rm_methods"] = np.nan
    code_sw = [s for s in (range(0, 6) if not rec["device"].startswith("AXON") else range(6, 11))
               if s < n and counts[s] == 0]
    if len(code_sw) >= 2:
        L = off - on
        av = [V[s, on + L // 3:off].mean() for s in code_sw]
        out["Rm_code"] = float(np.polyfit(amps[code_sw], av, 1)[0] * 1000)
    else:
        out["Rm_code"] = np.nan
    # AP measures
    out["max_spikes"] = int(counts.max())
    out["max_firing_rate"] = counts.max() / STEP_S
    keys = ["rheobase", "threshold", "amplitude", "half_width", "rise", "decay", "latency", "AHP",
            "ISI_adaptation", "amp_adaptation", "latency_slope", "ISI_CV", "ISI_Fano",
            "threshold_code", "amplitude_code", "half_width_code", "half_width_raw",
            "amplitude_raw", "phase_idx_first", "phase_idx_median", "phase_two_peaks_frac",
            "phase_idx_first_p2", "phase_idx_median_p2", "phase_idx_first_p10",
            "phase_idx_median_p10", "phase_none_frac", "phase_first_kind", "phase_idx_first_x",
            "phase_idx_median_x", "penult_half_width", "penult_amplitude", "max_sweep"]
    for k in keys:
        out.setdefault(k, np.nan)
    if not len(spk):
        return out
    pk = peaks[rh]
    m = ap_measures(V[rh], fs, pk, 0, on, off)
    out["rheobase"] = float(amps[rh])
    for k in ["threshold", "amplitude", "half_width", "rise", "decay", "latency"]:
        out[k] = m[k]
    mc = ap_measures(V[rh], fs, pk, 0, on, off, window="code")
    out["threshold_code"], out["amplitude_code"], out["half_width_code"] = mc["threshold"], mc["amplitude"], mc["half_width"]
    mr = ap_measures(Vraw[rh], fs, pk, 0, on, off)
    out["half_width_raw"], out["amplitude_raw"] = mr["half_width"], mr["amplitude"]
    end = pk[1] if len(pk) > 1 else off
    out["AHP"] = float(V[rh, pk[0]:end].min() - m["threshold"])
    ms = int(np.argmax(counts))
    out["max_sweep"] = ms
    pm = peaks[ms]
    if len(pm) >= 3:
        isi = np.diff(pm) / fs * 1000
        out["ISI_adaptation"] = isi[1] / isi[0]
        out["ISI_CV"] = isi.std(ddof=1) / isi.mean()
        out["ISI_Fano"] = isi.var(ddof=1) / isi.mean()
    allm = [ap_measures(V[ms], fs, pm, k, on, off) for k in range(len(pm))]
    if len(pm) >= 2:
        out["amp_adaptation"] = allm[1]["amplitude"] / allm[0]["amplitude"]
        out["penult_half_width"] = allm[-2]["half_width"]
        out["penult_amplitude"] = allm[-2]["amplitude"]
    lat = []
    for s in spk[:5]:
        ti = ap_measures(V[s], fs, peaks[s], 0, on, off)["latency"]
        lat.append((amps[s], 1.0 / ti if ti > 0 else np.nan))
    lat = np.array(lat)
    ok = np.isfinite(lat[:, 1])
    if ok.sum() >= 2:
        out["latency_slope"] = float(np.polyfit(lat[ok, 0], lat[ok, 1], 1)[0])
    # phase peak index on the raw trace of the maximal-rate sweep
    for frac, suf in [(PROMINENCE_FRAC, ""), (0.02, "_p2"), (0.10, "_p10")]:
        vals, twos = [], []
        for k in range(len(pm)):
            ti = allm[k]["thr_idx"]
            val, kind = phase_index(Vraw[ms], fs, ti, pm[k], frac)
            vals.append(val)
            twos.append(kind)
        vals = np.array(vals)
        twos = np.array(twos)
        out["phase_idx_first" + suf] = vals[0]
        out["phase_idx_median" + suf] = float(np.nanmedian(vals)) if np.isfinite(vals).any() else np.nan
        if suf == "":
            out["phase_two_peaks_frac"] = float(np.mean(twos == "two"))
            out["phase_none_frac"] = float(np.mean(twos == "none"))
            out["phase_first_kind"] = twos[0]
            # variant: APs whose AIS phase is not resolved are left out
            res = vals[twos != "none"]
            out["phase_idx_first_x"] = vals[0] if twos[0] != "none" else np.nan
            out["phase_idx_median_x"] = float(np.median(res)) if len(res) else np.nan
    return out


def load_one(asset):
    rec = read_nwb(asset["asset_id"])
    try:
        feats = cell_features(rec)
    except Exception as e:  # reported in the notebook as a failed extraction
        feats = {"cell_id": rec["cell_id"], "error": repr(e)}
    meta = {k: rec[k] for k in ["fs", "v_unit", "i_unit", "v_start", "i_start", "device", "cell_id",
                                "identifier", "subject_id", "sex", "species", "session_id",
                                "session_start"]}
    meta["n_samples"] = rec["V"].shape[1]
    meta["h5_paths"] = frozenset(rec["h5_paths"])
    meta["h5_strings"] = tuple(rec["h5_strings"])
    meta["sweep_numbers_ok"] = rec["sweep_numbers"] == list(range(1, len(rec["V"]) + 1))
    on, off = step_indices(rec["I"])
    meta["current_steps"] = tuple(np.round(rec["I"][:, (on + off) // 2], 3))
    meta["n_sweeps_file"] = len(rec["V"])
    meta["trace_hash"] = hashlib.md5(rec["V"].tobytes()).hexdigest()
    meta["path"] = asset["path"]
    meta["filename"] = asset["path"].split("/")[-1]
    meta["size"] = asset["size"]
    feats.pop("cell_id")
    return {**meta, **feats}


def load_all(assets, workers=8):
    with ThreadPoolExecutor(workers) as ex:
        rows = list(ex.map(load_one, assets))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- 10x data


def geo_member(url=GEO_H5AD_TAR, member=GEO_MEMBER):
    """One member of the GEO tar.gz, streamed into memory; the stream stops after it (no disk)."""
    import tarfile
    r = requests.get(url, stream=True, timeout=300)
    r.raise_for_status()
    r.raw.decode_content = False
    with tarfile.open(fileobj=r.raw, mode="r|gz") as tf:
        for m in tf:
            if m.name == member:
                return io.BytesIO(tf.extractfile(m).read())
    raise KeyError(member)


def ext_cluster_means(buf, n_genes=500):
    """Per leiden cluster, the mean log2(x + 1) UMI count of the 500 most variable genes.

    Counts are layers/RawCounts of Ext.h5ad (integers). Genes, the 500 of highest normalized
    dispersion (var/dispersions_norm, the file's own highly-variable-gene ranking, X); the variant
    takes the 500 of highest variance of log2(x + 1) over all cells.
    """
    from scipy.sparse import csr_matrix
    f = h5py.File(buf, "r")
    dec = lambda a: np.array([x.decode() if isinstance(x, bytes) else x for x in a])
    obs = f["obs"]
    clusters = dec(obs["leiden"]["categories"][:])[obs["leiden"]["codes"][:]].astype(int)
    labels = dec(obs["cluster_labels"]["categories"][:])[obs["cluster_labels"]["codes"][:]]
    X = f["layers"]["RawCounts"]["X"]
    shape = tuple(X.attrs["shape"])
    m = csr_matrix((X["data"][:], X["indices"][:], X["indptr"][:]), shape=shape)
    genes = dec(f["var"]["_index"][:])
    disp = f["var"]["dispersions_norm"][:]
    f.close()
    m.data = np.log2(m.data + 1.0)
    mean = np.asarray(m.mean(axis=0)).ravel()
    sq = m.copy()
    sq.data **= 2
    var = np.asarray(sq.mean(axis=0)).ravel() - mean ** 2
    out = {}
    for name, score in [("dispersion", disp), ("variance", var)]:
        g = np.argsort(-np.nan_to_num(score, nan=-np.inf))[:n_genes]
        sub = m[:, g].tocsc()
        means = {c: np.asarray(sub[clusters == c].mean(axis=0)).ravel() for c in np.unique(clusters)}
        out[name] = pd.DataFrame(means, index=genes[g]).T
    lab = pd.Series(labels, index=clusters).groupby(level=0).first()
    return out, lab, pd.Series(clusters).value_counts().sort_index()


# ----------------------------------------------------------------------------- statistics


def bh(p):
    """Benjamini-Hochberg adjusted p-values (as MATLAB mafdr with 'BHFDR')."""
    p = np.asarray(p, float)
    out = np.full_like(p, np.nan)
    ok = np.isfinite(p)
    q = p[ok]
    m = len(q)
    o = np.argsort(q)
    r = q[o] * m / np.arange(1, m + 1)
    r = np.minimum.accumulate(r[::-1])[::-1]
    res = np.empty(m)
    res[o] = np.minimum(r, 1)
    out[ok] = res
    return out
