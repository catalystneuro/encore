"""Loading and measures for dandiset 000003 (Senzai & Buzsaki 2017, Neuron 93:691).

doi:10.1016/j.neuron.2016.12.011. Each NWB file holds one recording day of one mouse: sorted units
with a `cell_type` label from the authors' unit summary, spike times, per-spike waveforms on the
channels of the unit's shank, sleep and wake periods (`processing/behavior/states`), dentate
spike events (`stimulus/presentation/DS2.*`), light pulse times (`stimulus/presentation/PulseStim_*`),
the LFP at 1250 Hz, and, for sessions with behaviour, the positions in the T-maze and open fields
(`processing/behavior/*Position_position`), the T-maze trials and the epochs.
Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- From the paper's STAR Methods: trough-to-peak latency below 0.425 ms for narrow-waveform
  interneurons, burst index (spikes at 3 to 5 ms over spikes at 200 to 300 ms of the
  autocorrelogram) with the threshold 1.2 of the Methods (the Figure 1A legend says 1.8);
  theta 4 to 10 Hz and gamma 30 to 80 Hz, periods above median + 0.5 SD (theta) or + 1 SD (gamma)
  of the amplitude, Rayleigh p < 0.05 and kappa > 0.1 for inclusion; cross-correlograms in 0.5 ms
  bins, baseline from a Gaussian of SD 10 ms, threshold at the 99.9999th percentile of a Poisson
  at the baseline rate, two consecutive bins at +1.5 to +5 ms (monosynaptic) or -1 to +1 ms
  (synchrony); speed above 3 cm/s; open-field pixels of 0.92 cm, Gaussian smoothing SD 1.84 cm,
  place field of at least 100 pixels above max(20% of the local peak, 1 Hz); T-maze bins of
  1.86 cm, Gaussian smoothing SD 5.57 cm, place field of at least 5 bins above 50% of the local
  peak, peak above 1 Hz; remapping index r(AA') - mean(r(AB), r(BA')); optogenetic suppression of
  at least 20% in +2 to +15 ms after 20 ms light pulses.
- From the dandiset's own conventions, checked in the notebook: open-field positions are
  normalised to 0..1 and scaled by 0.46 m (the stored `conversion`); T-maze linearised
  positions are a central-arm coordinate (0 to 2, scaled by 0.325 m, so 65 cm) and an angle on
  the circular side arms (radius 32.5 cm, so pi radians is 102 cm), matching the maze of the
  Methods.
- Choices made here where the Methods are silent (a common choice, stated in the notebook):
  the baseline window of the light-pulse and dentate-spike histograms, the hollowing of the CCG
  baseline (none, as the Methods describe a plain Gaussian), the burst definition (spikes
  within 6 ms), the T-maze run segment (trial start to the first arrival at the reward port,
  stimulation trials left out), and the waveform reading (the mean of the first 200 stored
  spike waveforms, on the channel with the largest amplitude).
"""

from __future__ import annotations

import re
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import signal, stats
from scipy.interpolate import CubicSpline
from scipy.ndimage import gaussian_filter, gaussian_filter1d, label

DANDISET_ID = "000003"
DANDISET_VERSION = "0.260218.2052"

SPIKE_HZ = 20000.0
LFP_HZ = 1250.0
KEEP = {
    "granule cell": "GC", "mossy cell": "MC", "pyramidal cell": "CA3",
    "narrow waveform cell": "nI",
    "wide waveform cell (narrower, exclude opto tagged SST cell)": "wI",
    "wide waveform cell (wider)": "wI",
    "optogenetically tagged SST cell": "SST",
}
N_WAVEFORMS = 200
THETA, GAMMA = (4.0, 10.0), (30.0, 80.0)
THETA_SD, GAMMA_SD = 0.5, 1.0
TP_NARROW_MS = 0.425
BURST_THRESHOLDS = (1.2, 1.8)        # Methods, Figure 1A legend
SPEED_MIN = 3.0                      # cm/s
OF_SIZE_CM, OF_BINS = 46.0, 50       # 0.92 cm pixels
OF_SMOOTH_CM = 1.84
OF_FIELD_PIXELS, OF_FIELD_FRAC = 100, 0.2
TM_BIN_CM, TM_SMOOTH_CM = 1.86, 5.57
TM_FIELD_BINS, TM_FIELD_FRAC = 5, 0.5
CENTRAL_CM, RADIUS_CM = 65.0, 32.5
REWARD_CM = 102.0 - 18.0             # reward port 18 cm from the end of a 102 cm side arm
OPEN_FIELDS = {"A": "OpenFieldPosition_Old", "B": "OpenFieldPosition_New", "A2": "OpenFieldPosition_Oldlast",
               "Ac": "OpenFieldPosition_Old_Curtain", "Bc": "OpenFieldPosition_New_Curtain"}


def _s(x) -> str:
    v = x[()]
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray):
        return ", ".join(e.decode() if isinstance(e, bytes) else str(e) for e in v.ravel())
    return str(v)


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _intervals(group) -> pd.DataFrame:
    cols = {}
    for c in ("start_time", "stop_time"):
        cols[c] = group[c][:].astype(float)
    for c in ("label", "tags", "condition", "error_run", "stim_run", "both_visit"):
        if c in group:
            v = group[c][:]
            cols[c] = v.astype(str) if v.dtype == object else v
    return pd.DataFrame(cols)


def _mean_waveforms(U, starts, ends, keep, n=N_WAVEFORMS):
    """Mean of the first n stored waveforms of each kept unit, as (channels, 32 samples) arrays.
    Each spike has one row per channel of its shank in `waveforms`; `waveforms_index` gives the
    end row of each spike, in the same order as `spike_times`."""
    out = {}
    wi = U["waveforms_index"]
    wf = U["waveforms"]
    for u in keep:
        s0, s1 = int(starts[u]), min(int(ends[u]), int(starts[u]) + n)
        if s1 <= s0:
            continue
        row_ends = wi[max(s0 - 1, 0):s1].astype(np.int64)
        r0 = 0 if s0 == 0 else int(row_ends[0])
        row_ends = row_ends if s0 == 0 else row_ends[1:]
        nch = int(row_ends[0] - r0)
        block = wf[r0:int(row_ends[-1])]
        if nch <= 0 or block.shape[0] != nch * (s1 - s0):
            continue
        out[u] = block.reshape(s1 - s0, nch, block.shape[1]).mean(axis=0)
    return out


def repair_boundaries(allst: np.ndarray, starts: np.ndarray, ends: np.ndarray):
    """Find units whose spike train restarts after exactly k * 65536 spikes while that first block
    continues the previous unit's train, and give the block back to the previous unit.

    In some files the end index of a unit is short by a multiple of 65536 (an integer overflow at
    conversion), so the next unit's train begins with the previous unit's last spikes. Returns the
    corrected starts and ends and a list of the repairs."""
    starts, ends = starts.copy(), ends.copy()
    repairs = []
    for i in range(1, len(ends)):
        seg = allst[starts[i]:ends[i]]
        drops = np.flatnonzero(np.diff(seg) < 0)
        if len(drops) != 1:
            continue
        p = int(drops[0]) + 1
        prev_ok = ends[i - 1] > starts[i - 1] and allst[ends[i - 1] - 1] <= seg[0]
        if p % 65536 == 0 and prev_ok:
            repairs.append({"unit": i - 1, "moved_spikes": p, "gap_s": float(seg[0] - allst[ends[i - 1] - 1])})
            ends[i - 1] += p
            starts[i] += p
    return starts, ends, repairs


def _awake_lfp(f, states: pd.DataFrame, max_s=3600.0):
    """Theta-reference LFP (volts) during 'awake' periods, up to max_s seconds, with sample times."""
    lfp = f["processing/ecephys/LFP"]
    series = lfp[list(lfp.keys())[0]]
    data = series["data"]
    conv = float(data.attrs["conversion"])
    ref = f["general/extracellular_ephys/electrodes/theta_reference"][:]
    region = series["electrodes"][:]
    cols = np.flatnonzero(ref[region]) if ref.any() else []
    if len(cols) != 1 or not np.isfinite(conv):
        return None
    col = int(cols[0])
    rate = float(series["starting_time"].attrs["rate"])
    t0 = float(series["starting_time"][()])
    pieces, total = [], 0.0
    awake = states[states.label == "awake"].sort_values("start_time")
    for a, b in zip(awake.start_time, awake.stop_time):
        if b - a < 10 or total >= max_s:
            continue
        b = min(b, a + max_s - total)
        i0, i1 = int((a - t0) * rate), int((b - t0) * rate)
        i1 = min(i1, data.shape[0])
        if i1 - i0 < rate * 10:
            continue
        x = data[i0:i1, col].astype(float) * conv
        pieces.append((t0 + np.arange(i0, i1) / rate, x))
        total += (i1 - i0) / rate
    return {"rate": rate, "pieces": pieces, "column": col}


DS2_BASELINE = (-0.036, -0.016)    # Methods, the baseline of the DS2 criterion


def unit_ds2_sites(f, s: dict):
    """For files whose units carry `electrode_group` (the shank): each unit's site, the channel of
    its shank with the largest mean waveform, and the DS2 amplitude there (mean LFP at the DS2
    peaks minus the mean at -36 to -16 ms, Methods). The LFP is read over the two LFP chunks
    (2 x 99368 samples, about 159 s) holding the most DS2 peaks. Waveform channel i is taken to be
    the i-th electrode of the shank in the electrodes table."""
    E = f["general/extracellular_ephys/electrodes"]
    groups = E["group_name"][:].astype(str)
    lfp = f["processing/ecephys/LFP"]
    series = lfp[list(lfp.keys())[0]]
    data = series["data"]
    rate = float(series["starting_time"].attrs["rate"])
    t0 = float(series["starting_time"][()])
    region = series["electrodes"][:]
    conv = float(data.attrs["conversion"])
    chunk = data.chunks[0] if data.chunks else 100000
    idx = ((s["ds2"] - t0) * rate).astype(int)
    rows = np.bincount(idx // chunk)
    best = int(np.argmax(rows[:-1] + rows[1:])) if len(rows) > 1 else 0
    i0, i1 = best * chunk, min((best + 2) * chunk, data.shape[0])
    x = data[i0:i1, :].astype(float) * (conv if np.isfinite(conv) else 1.0)
    ev = idx[(idx >= i0 + int(0.05 * rate)) & (idx < i1 - int(0.05 * rate))] - i0
    b0, b1 = int(DS2_BASELINE[0] * rate), int(DS2_BASELINE[1] * rate)
    amp = np.array([x[ev, c].mean() - np.mean([x[e + b0:e + b1, c].mean() for e in ev]) for c in range(x.shape[1])]) if len(ev) else None
    out = {"n_events": int(len(ev)), "window_s": (i1 - i0) / rate, "channel_amp": amp, "region": region,
           "groups": groups, "units": {}}
    eg = s["units_all"].set_index("unit")["electrode_group"]
    for u, w in s["waveforms"].items():
        rows_e = np.flatnonzero(groups == eg[u])
        ch = int(np.argmax(np.ptp(w, axis=1)))
        if ch >= len(rows_e) or amp is None:
            continue
        cols = np.flatnonzero(region == rows_e[ch])
        out["units"][u] = {"shank": eg[u], "channel": ch, "n_channels": len(rows_e), "waveform_channels": w.shape[0],
                           "ds2_amp": float(amp[cols[0]]) if len(cols) else np.nan}
    return out


def load_session(path: str, url: str, waveforms=True, lfp=True) -> dict:
    """Everything the notebook uses from one file, reduced as it loads."""
    f = h5py.File(remfile.File(url), "r")
    s = {"path": path, "session": path.split("_ses-")[1].split("_")[0]}
    subj = f["general/subject"]
    s["subject"] = _s(subj["subject_id"])
    s["genotype"] = _s(subj["genotype"]) if "genotype" in subj else ""
    s["age"] = _s(subj["age"]) if "age" in subj else ""
    s["format"] = "electrode_group" if "electrode_group" in f["units"] else "standard"
    U = f["units"]
    ct = U["cell_type"][:].astype(str)
    ends = U["spike_times_index"][:].astype(np.int64)
    starts = np.r_[0, ends[:-1]]
    allst = U["spike_times"][:]
    s["unsorted_units_stored"] = [i for i in range(len(ct)) if np.any(np.diff(allst[starts[i]:ends[i]]) < 0)]
    starts, ends, s["repairs"] = repair_boundaries(allst, starts, ends)
    s["unsorted_units_repaired"] = [i for i in range(len(ct)) if np.any(np.diff(allst[starts[i]:ends[i]]) < 0)]
    keep = [i for i, c in enumerate(ct) if c in KEEP]
    units = pd.DataFrame({"unit": np.arange(len(ct)), "cell_type": ct,
                          "global_id": U["global_id"][:].astype(float),
                          "shank_id": U["shank_id"][:], "n_spikes": ends - starts})
    if "electrode_group" in U:
        units["electrode_group"] = [f[r].name.split("/")[-1] for r in U["electrode_group"][:]]
    units["type"] = units.cell_type.map(KEEP).fillna("other")
    s["units_all"] = units
    s["spike_time_range"] = (float(allst.min()), float(allst.max())) if len(allst) else (np.nan, np.nan)
    # spike times lie on the 20 kHz sample grid; kept as sorted int32 sample numbers to halve memory
    s["spikes"] = {i: np.sort(np.round(allst[starts[i]:ends[i]] * SPIKE_HZ)).astype(np.int32) for i in keep}
    s["spike_grid_error"] = max((float(np.max(np.abs(allst[starts[i]:ends[i]] * SPIKE_HZ
                                                     - np.round(allst[starts[i]:ends[i]] * SPIKE_HZ))))
                                 for i in keep if ends[i] > starts[i]), default=0.0)
    del allst
    s["units"] = units[units.unit.isin(keep)].reset_index(drop=True)
    s["waveforms"] = _mean_waveforms(U, starts, ends, keep) if waveforms and "waveforms" in U else {}
    beh = f["processing/behavior"] if "behavior" in f["processing"] else {}
    s["states"] = _intervals(beh["states"]) if "states" in beh else pd.DataFrame(columns=["start_time", "stop_time", "label"])
    s["epochs"] = _intervals(f["intervals/epochs"]) if "intervals" in f and "epochs" in f["intervals"] else None
    s["trials"] = _intervals(f["intervals/trials"]) if "intervals" in f and "trials" in f["intervals"] else None
    pos = {}
    for k in (beh.keys() if hasattr(beh, "keys") else []):
        if not k.endswith("_position"):
            continue
        for kk in beh[k]:
            ser = beh[k][kk]
            pos[kk.replace("_spatial_series", "")] = {
                "t": ser["timestamps"][:], "xy": ser["data"][:],
                "conversion": float(ser["data"].attrs["conversion"]), "unit": ser["data"].attrs["unit"]}
    s["positions"] = pos
    stim = f["stimulus/presentation"]
    ds2 = []
    for k in stim:
        if k.startswith("DS2"):
            lab = stim[k]["data"][:].astype(str)
            ts = stim[k]["timestamps"][:]
            ds2.append(ts[np.char.find(lab, "peak") >= 0])
    s["ds2"] = np.sort(np.concatenate(ds2)) if ds2 else np.array([])
    s["ds2_series"] = [k for k in stim if k.startswith("DS2")]
    s["stim_names"] = {k: int(stim[k]["timestamps"].shape[0]) for k in stim}
    s["pulse20"] = stim["PulseStim_5V_20ms_LD12/timestamps"][:] if "PulseStim_5V_20ms_LD12" in stim else np.array([])
    s["n_electrodes"] = int(f["general/extracellular_ephys/electrodes/id"].shape[0])
    s["electrode_xyz_finite"] = int(sum(np.isfinite(f[f"general/extracellular_ephys/electrodes/{c}"][:]).sum() for c in ("x", "y", "z")))
    s["pulse20_decreasing"] = int(np.sum(np.diff(s["pulse20"]) < 0)) if len(s["pulse20"]) > 1 else 0
    s["pulse20_duplicates"] = int(len(s["pulse20"]) - len(np.unique(s["pulse20"])))
    s["pulse20"] = np.unique(s["pulse20"])
    s["unit_site"] = unit_ds2_sites(f, s) if "electrode_group" in units and s["waveforms"] and len(s["ds2"]) else None
    s["has_raw"] = "ElectricalSeries" in f["acquisition"]
    s["phases"] = spike_phases(_awake_lfp(f, s["states"]), s["spikes"]) if lfp else None
    return s


def times(s: dict, u: int) -> np.ndarray:
    """Spike times of unit u in seconds."""
    return s["spikes"][u] / SPIKE_HZ


def _band(x, rate, band):
    b, a = signal.butter(3, [band[0] / (rate / 2), band[1] / (rate / 2)], btype="band")
    z = signal.hilbert(signal.filtfilt(b, a, x))
    return np.angle(z), np.abs(z)


def spike_phases(lfp, spikes: dict):
    """Theta and gamma phase (radians, 0 = peak of the filtered LFP) of each unit's spikes in awake
    periods where the band's amplitude exceeds median + k SD, as in the Methods. The LFP is the
    file's theta-reference channel (`electrodes.theta_reference`)."""
    if lfp is None or not lfp["pieces"]:
        return None
    out = {"seconds": sum(len(x) for _, x in lfp["pieces"]) / lfp["rate"], "units": {}}
    bands = {}
    for name, band, k in (("theta", THETA, THETA_SD), ("gamma", GAMMA, GAMMA_SD)):
        ph, amp, tt = [], [], []
        for t, x in lfp["pieces"]:
            p, a = _band(x, lfp["rate"], band)
            ph.append(p); amp.append(a); tt.append(t)
        amp_all = np.concatenate(amp)
        thr = np.median(amp_all) + k * amp_all.std()
        bands[name] = (tt, ph, amp, thr)
        out[f"{name}_fraction_above"] = float((amp_all > thr).mean())
    for u, smp in spikes.items():
        st = smp / SPIKE_HZ
        res = {}
        for name, (tt, ph, amp, thr) in bands.items():
            sel = []
            for t, p, a in zip(tt, ph, amp):
                i = np.searchsorted(t, st[(st >= t[0]) & (st < t[-1])])
                i = np.clip(i, 0, len(t) - 1)
                sel.append(p[i][a[i] > thr])
            res[name] = np.concatenate(sel).astype(np.float32) if sel else np.array([], np.float32)
        out["units"][u] = res
    return out


def _load(pu):
    return load_session(*pu)


def load_all(workers=10) -> list[dict]:
    """Every file, in separate processes (h5py serialises threads, so threads do not overlap)."""
    assets = asset_urls()
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_load, assets))


# ---------------------------------------------------------------- unit measures

def interval_mask_count(t: np.ndarray, starts, stops) -> int:
    """Number of times t (sorted) inside the union of [start, stop) intervals."""
    return int(sum(np.searchsorted(t, b) - np.searchsorted(t, a) for a, b in zip(starts, stops)))


def state_rates(s: dict) -> pd.DataFrame:
    """Firing rate of each kept unit in each state label of `states` (spikes / total duration)."""
    st = s["states"]
    rows = []
    dur = {lab: float((g.stop_time - g.start_time).sum()) for lab, g in st.groupby("label")}
    for u in s["spikes"]:
        t = times(s, u)
        r = {"unit": u}
        for lab, g in st.groupby("label"):
            r[f"rate_{lab}"] = interval_mask_count(t, g.start_time, g.stop_time) / dur[lab] if dur[lab] > 0 else np.nan
        span = s["spike_time_range"][1] - s["spike_time_range"][0]
        r["rate_overall"] = len(t) / span if span > 0 else np.nan
        rows.append(r)
    out = pd.DataFrame(rows, columns=["unit"] + (list(rows[0]) [1:] if rows else []))
    for lab in ("awake", "quiet", "nrem", "rem"):
        out[f"dur_{lab}"] = dur.get(lab, 0.0)
        if f"rate_{lab}" not in out:
            out[f"rate_{lab}"] = np.nan
    wake = dur.get("awake", 0) + dur.get("quiet", 0)
    out["rate_wake_all"] = ((out.rate_awake.fillna(0) * dur.get("awake", 0) + out.rate_quiet.fillna(0) * dur.get("quiet", 0))
                            / wake) if wake > 0 else np.nan
    return out


def burst_index(t: np.ndarray) -> float:
    """Mean autocorrelogram count per ms at 3-5 ms over that at 200-300 ms (Methods)."""
    def n_in(lo, hi):
        return float(np.sum(np.searchsorted(t, t + hi, side="right") - np.searchsorted(t, t + lo, side="right")))
    near, far = n_in(0.003, 0.005) / 2.0, n_in(0.200, 0.300) / 100.0
    return near / far if far > 0 else np.nan


def trough_to_peak_ms(w: np.ndarray, hz=SPIKE_HZ, up=100000.0):
    """Trough-to-peak latency (ms) of a mean waveform (channels x samples) on the channel with the
    largest amplitude, after cubic-spline upsampling to 100 kHz. Also returns whether the peak is
    at the last sample (latency then a lower bound) and the upsampled normalised waveform."""
    ch = int(np.argmax(np.ptp(w, axis=1)))
    x = w[ch] - np.median(w[ch][:5])
    n = len(x)
    tt = np.arange(n) / hz
    fine = np.arange(0, tt[-1], 1 / up)
    y = CubicSpline(tt, x)(fine)
    if abs(y.min()) < abs(y.max()):        # positive-going spike: no trough to measure
        return np.nan, False, y / np.abs(y).max()
    i = int(np.argmin(y))
    j = i + int(np.argmax(y[i:]))
    return (fine[j] - fine[i]) * 1000.0, j >= len(y) - 2, y / abs(y[i])


def peth(t: np.ndarray, events: np.ndarray, lo: float, hi: float, binsize: float) -> np.ndarray:
    """Spike counts of t in bins of `binsize` s from lo to hi s around each event, summed over events."""
    edges = np.arange(lo, hi + binsize / 2, binsize)
    i0 = np.searchsorted(t, events + lo)
    i1 = np.searchsorted(t, events + hi)
    n = i1 - i0
    if n.sum() == 0:
        return np.zeros(len(edges) - 1)
    idx = np.repeat(i0 - np.r_[0, n.cumsum()[:-1]], n) + np.arange(n.sum())
    rel = t[idx] - np.repeat(events, n)
    return np.histogram(rel, edges)[0].astype(float)


DS2_WINDOW, DS2_BIN, DS2_PEAK = 0.1, 0.002, 0.02
DS2_BASE = (0.05, 0.1)


def ds2_response(t: np.ndarray, ds2: np.ndarray) -> dict:
    """Peri-DS2 histogram (2 ms bins, +-100 ms). Peak ratio: the largest rate within +-20 ms over
    the mean rate at 50-100 ms on both sides (a choice; the paper does not give its baseline).
    Peak time: the bin centre of that largest rate."""
    c = peth(t, ds2, -DS2_WINDOW, DS2_WINDOW, DS2_BIN) / (len(ds2) * DS2_BIN)
    centres = np.arange(-DS2_WINDOW, DS2_WINDOW, DS2_BIN) + DS2_BIN / 2
    base = c[(np.abs(centres) >= DS2_BASE[0]) & (np.abs(centres) <= DS2_BASE[1])].mean()
    near = np.abs(centres) <= DS2_PEAK
    k = np.argmax(np.where(near, c, -np.inf))
    return {"peak_ratio": c[k] / base if base > 0 else np.nan, "peak_ms": centres[k] * 1000,
            "base_hz": base, "peak_hz": c[k], "n_spikes_window": int(c.sum() * len(ds2) * DS2_BIN), "curve": c}


OPTO_BASE, OPTO_TEST = (-0.020, 0.0), (0.002, 0.015)
OPTO_DROP = 0.2


def opto_response(t: np.ndarray, pulses: np.ndarray, base=OPTO_BASE) -> dict:
    """Rate in +2 to +15 ms after 20 ms light pulses against the rate in the 20 ms before
    (the baseline window is a choice; the Methods say 'baseline PETH'). Suppressed when the rate
    falls by at least 20% (Methods); a one-sided Poisson test of the counts is given as well."""
    def count(lo, hi):
        return float(np.sum(np.searchsorted(t, pulses + hi) - np.searchsorted(t, pulses + lo)))
    nb, nt = count(*base), count(*OPTO_TEST)
    db, dt = base[1] - base[0], OPTO_TEST[1] - OPTO_TEST[0]
    rb, rt = nb / (len(pulses) * db), nt / (len(pulses) * dt)
    expected = nb * dt / db
    p = stats.poisson.cdf(nt, expected) if expected > 0 else np.nan
    return {"base_hz": rb, "test_hz": rt, "change": rt / rb - 1 if rb > 0 else np.nan,
            "p_decrease": p, "n_base": nb, "n_test": nt}


# ---------------------------------------------------------------- pairs of units

CCG_BIN, CCG_HALF = 0.0005, 0.05
CCG_SD = 0.010
CCG_PCTL = 0.999999
MONO_WINDOW, SYNC_WINDOW = (0.0015, 0.005), (-0.001, 0.001)


def ccg(ref: np.ndarray, tgt: np.ndarray, binsize=CCG_BIN, half=CCG_HALF) -> np.ndarray:
    """Counts of tgt spikes at each lag (tgt - ref) in bins of `binsize` from -half to +half."""
    return peth(tgt, ref, -half, half, binsize)


def ccg_test(counts: np.ndarray, binsize=CCG_BIN, half=CCG_HALF, pctl=CCG_PCTL):
    """Baseline from a Gaussian of SD 10 ms, threshold at the 99.9999th percentile of a Poisson at
    the baseline (Methods). Returns the bin left edges, baseline, upper threshold, and for the
    monosynaptic (+1.5 to +5 ms) and synchrony (-1 to +1 ms) windows whether two consecutive bins
    exceed the threshold, and the excess count over the baseline in the window."""
    left = np.arange(-half, half - binsize / 2, binsize)
    base = gaussian_filter1d(counts, CCG_SD / binsize, mode="reflect")
    hi = stats.poisson.ppf(pctl, base)
    above = counts > hi
    out = {"left": left, "base": base, "hi": hi}
    for name, (a, b) in (("mono", MONO_WINDOW), ("sync", SYNC_WINDOW)):
        w = (left >= a - 1e-9) & (left + binsize <= b + 1e-9)
        x = above[w]
        out[name] = bool(np.any(x[1:] & x[:-1]))
        out[f"{name}_excess"] = float((counts[w] - base[w]).sum())
        out[f"{name}_peak_ms"] = float((left[w][np.argmax(counts[w])] + binsize / 2) * 1000)
    return out


def transmission(ref: np.ndarray, tgt: np.ndarray) -> float:
    """Spike transmission probability: excess tgt spikes at +1.5 to +5 ms over the baseline, per ref spike."""
    if len(ref) == 0:
        return np.nan
    return ccg_test(ccg(ref, tgt))["mono_excess"] / len(ref)


BURST_ISI = 0.006


def burst_positions(t: np.ndarray, isi=BURST_ISI) -> np.ndarray:
    """0 for a single spike, else the spike's position (1, 2, 3, ...) within a burst of spikes
    separated by at most `isi` (a choice: the paper does not define its bursts)."""
    d = np.diff(t)
    joined = np.r_[False, d <= isi]                 # spike follows the previous one closely
    starts_next = np.r_[d <= isi, False]
    pos = np.zeros(len(t), int)
    run = 0
    for i in range(len(t)):
        run = run + 1 if joined[i] else (1 if starts_next[i] else 0)
        pos[i] = run
    return pos


# ---------------------------------------------------------------- phase locking

def phase_stats(ph: np.ndarray) -> dict:
    """Mean resultant length, mean phase, Rayleigh p (with the usual small-sample correction) and the
    concentration kappa estimated from the resultant length (Fisher's approximation)."""
    n = len(ph)
    if n < 10:
        return {"n": n, "mrl": np.nan, "phase": np.nan, "p": np.nan, "kappa": np.nan}
    z = np.exp(1j * ph.astype(float)).mean()
    r = float(np.abs(z))
    R = n * r
    p = float(np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - R ** 2)) - (1 + 2 * n)))
    if r < 0.53:
        k = 2 * r + r ** 3 + 5 * r ** 5 / 6
    elif r < 0.85:
        k = -0.4 + 1.39 * r + 0.43 / (1 - r)
    else:
        k = 1 / (r ** 3 - 4 * r ** 2 + 3 * r)
    return {"n": n, "mrl": r, "phase": float(np.angle(z)), "p": min(p, 1.0), "kappa": k}


# ---------------------------------------------------------------- positions and place fields

def speed_cm_s(t: np.ndarray, x_cm: np.ndarray, y_cm: np.ndarray, smooth_s=0.25) -> np.ndarray:
    """Speed from positions smoothed with a Gaussian of SD 0.25 s (a common choice)."""
    dt = np.median(np.diff(t))
    xs = gaussian_filter1d(x_cm, smooth_s / dt)
    ys = gaussian_filter1d(y_cm, smooth_s / dt)
    return np.hypot(np.gradient(xs, t), np.gradient(ys, t))


def _smooth_nan(m: np.ndarray, sd: float) -> np.ndarray:
    """Gaussian smoothing that ignores unvisited (NaN) bins (normalised convolution)."""
    ok = np.isfinite(m)
    num = gaussian_filter(np.where(ok, m, 0.0), sd, mode="constant")
    den = gaussian_filter(ok.astype(float), sd, mode="constant")
    with np.errstate(invalid="ignore", divide="ignore"):
        out = num / den
    out[~ok] = np.nan
    return out


def open_field_maps(s: dict, key: str, units, split=False):
    """Smoothed rate maps (Hz, 50 x 50 pixels of 0.92 cm) of the given units in one open-field
    epoch, from samples with speed above 3 cm/s. With split=True also the maps of the first and
    second halves of the epoch. Returns dict unit -> map (or (full, first, second))."""
    p = s["positions"][f"{key}_twhl_norm"]
    t, xy = p["t"], p["xy"]
    ok = np.all(np.isfinite(xy), axis=1)
    t, xy = t[ok], xy[ok] * OF_SIZE_CM
    sp = speed_cm_s(t, xy[:, 0], xy[:, 1])
    dt = np.median(np.diff(t))
    run = sp > SPEED_MIN
    edges = np.linspace(0, OF_SIZE_CM, OF_BINS + 1)
    ix = np.clip(np.digitize(xy[:, 0], edges) - 1, 0, OF_BINS - 1)
    iy = np.clip(np.digitize(xy[:, 1], edges) - 1, 0, OF_BINS - 1)
    halves = [np.ones(len(t), bool)]
    if split:
        mid = (t[0] + t[-1]) / 2
        halves += [t < mid, t >= mid]
    occ = []
    for h in halves:
        o = np.zeros((OF_BINS, OF_BINS))
        np.add.at(o, (ix[run & h], iy[run & h]), dt)
        occ.append(o)
    sd = OF_SMOOTH_CM / (OF_SIZE_CM / OF_BINS)
    out = {}
    for u in units:
        st = times(s, u)
        st = st[(st >= t[0]) & (st <= t[-1])]
        k = np.clip(np.searchsorted(t, st), 0, len(t) - 1)
        maps = []
        for h, o in zip(halves, occ):
            sel = run[k] & h[k]
            c = np.zeros((OF_BINS, OF_BINS))
            np.add.at(c, (ix[k[sel]], iy[k[sel]]), 1)
            with np.errstate(invalid="ignore", divide="ignore"):
                raw = np.where(o > 0, c / o, np.nan)
            maps.append(_smooth_nan(raw, sd))
        out[u] = tuple(maps) if split else maps[0]
    return out


def map_corr(a: np.ndarray, b: np.ndarray) -> float:
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 10 or np.std(a[ok]) == 0 or np.std(b[ok]) == 0:
        return np.nan
    return float(np.corrcoef(a[ok], b[ok])[0, 1])


def open_field_fields(m: np.ndarray) -> list[np.ndarray]:
    """Place fields of a 2-D map: connected regions (4-neighbour) of at least 100 pixels above the
    larger of 20% of the map's peak and 1 Hz, whose peak is at least 1 Hz. The 'local maximum' of
    the Methods is taken as the map's peak (a choice)."""
    if not np.isfinite(m).any():
        return []
    peak = np.nanmax(m)
    if peak < 1.0:
        return []
    lab, n = label(np.nan_to_num(m, nan=0.0) > max(OF_FIELD_FRAC * peak, 1.0))
    return [lab == i for i in range(1, n + 1) if (lab == i).sum() >= OF_FIELD_PIXELS]


def tmaze_linear(s: dict):
    """T-maze samples as (time, segment, distance cm): segment 0 is the central arm, 1 and 2 the
    side arms with negative and positive angle. Central-arm distance runs from the start of the
    arm (linearised coordinate 2) to the junction (0); side-arm distance from the junction along
    the circle (|angle| x 32.5 cm)."""
    p = s["positions"]["EightMazePosition_twhl_linearized"]
    t, a = p["t"], p["xy"]
    ok = np.all(np.isfinite(a), axis=1)
    t, a = t[ok], a[ok]
    seg = np.where(a[:, 0] > 0, 0, np.where(a[:, 1] < 0, 1, 2))
    dist = np.where(seg == 0, (2.0 - a[:, 0]) * RADIUS_CM, np.abs(a[:, 1]) * RADIUS_CM)
    return t, seg, dist


def tmaze_runs(s: dict, reward_cm=REWARD_CM - 10.0):
    """Outbound runs, one per trial without light stimulation: from the last sample on the first
    5 cm of the central arm before the animal reaches its far end (60 cm), to the first sample
    after that on a side arm within 10 cm of the reward port (84 cm). The ends of the side arms
    (about 95 to 102 cm) lie in the waiting area and are not part of a run. Returns a list of
    (t0, t1, side arm, trial condition)."""
    t, seg, dist = tmaze_linear(s)
    tr = s["trials"]
    runs = []
    for _, r in tr.iterrows():
        if r.get("stim_run", 0) == 1:
            continue
        m = (t >= r.start_time) & (t < r.stop_time)
        tt, sg, dd = t[m], seg[m], dist[m]
        far = np.flatnonzero((sg == 0) & (dd >= 60.0))
        if len(far) == 0:
            continue
        c = far[0]
        start = np.flatnonzero((sg[:c] == 0) & (dd[:c] <= 5.0))
        arrive = np.flatnonzero((sg[c:] > 0) & (dd[c:] >= reward_cm) & (dd[c:] <= REWARD_CM + 6.0))
        if len(start) == 0 or len(arrive) == 0:
            continue
        k = c + arrive[0]
        if np.any((sg[c:k] == 0) & (dd[c:k] <= 5.0)):
            continue
        runs.append((tt[start[-1]], tt[k], int(sg[k]), r.get("condition", "")))
    return runs


def tmaze_maps(s: dict, units, runs=None, trial_maps=False):
    """Linearised T-maze rate maps: central arm (0-65 cm) from all runs, then side arm 1 and side arm
    2 (0-84 cm each), in 1.86 cm bins, speed above 3 cm/s, each segment smoothed on its own with a
    Gaussian of SD 5.57 cm. Returns occupancy, dict unit -> list of three maps, and the runs."""
    t, seg, dist = tmaze_linear(s)
    if runs is None:
        runs = tmaze_runs(s)
    sp = np.abs(np.gradient(gaussian_filter1d(np.where(seg == 0, -dist, dist), 0.25 / np.median(np.diff(t))), t))
    in_run = np.zeros(len(t), bool)
    for a, b, *_ in runs:
        in_run |= (t >= a) & (t <= b)
    use = in_run & (sp > SPEED_MIN)
    dt = np.median(np.diff(t))
    lengths = [CENTRAL_CM, REWARD_CM, REWARD_CM]
    nb = [int(np.ceil(L / TM_BIN_CM)) for L in lengths]
    bins = [np.clip((dist / TM_BIN_CM).astype(int), 0, n - 1) for n in nb]
    occ = []
    for g in range(3):
        o = np.zeros(nb[g])
        sel = use & (seg == g) & (dist <= lengths[g])
        np.add.at(o, bins[g][sel], dt)
        occ.append(o)
    sd = TM_SMOOTH_CM / TM_BIN_CM
    maps = {}
    for u in units:
        st = times(s, u)
        st = st[(st >= t[0]) & (st <= t[-1])]
        k = np.clip(np.searchsorted(t, st), 0, len(t) - 1)
        ms = []
        for g in range(3):
            sel = use[k] & (seg[k] == g) & (dist[k] <= lengths[g])
            c = np.zeros(nb[g])
            np.add.at(c, bins[g][k[sel]], 1)
            with np.errstate(invalid="ignore", divide="ignore"):
                raw = np.where(occ[g] > 0, c / occ[g], np.nan)
            ms.append(_smooth_nan(raw, sd))
        maps[u] = ms
    return occ, maps, runs


def linear_fields(m: np.ndarray, min_bins=TM_FIELD_BINS, frac=TM_FIELD_FRAC) -> list[tuple[int, int, float]]:
    """Fields of a 1-D map: repeatedly take the highest bin not yet assigned; stop below 1 Hz; the
    field is the contiguous run of bins around it above 50% of that local peak; it counts when it
    spans at least 5 bins. Returns (first bin, last bin, peak Hz) of each field."""
    x = np.nan_to_num(m, nan=0.0).copy()
    free = np.ones(len(x), bool)
    fields = []
    while free.any():
        i = int(np.argmax(np.where(free, x, -np.inf)))
        peak = x[i]
        if peak < 1.0:
            break
        a = i
        while a - 1 >= 0 and free[a - 1] and x[a - 1] > frac * peak:
            a -= 1
        b = i
        while b + 1 < len(x) and free[b + 1] and x[b + 1] > frac * peak:
            b += 1
        free[a:b + 1] = False
        if b - a + 1 >= min_bins:
            fields.append((a, b, float(peak)))
    return fields


def spatial_info(rate: np.ndarray, occ: np.ndarray) -> float:
    """Skaggs information (bits/s): sum p_i r_i log2(r_i / r)."""
    ok = np.isfinite(rate) & (occ > 0)
    p = occ[ok] / occ[ok].sum()
    r = rate[ok]
    mean = (p * r).sum()
    if mean <= 0:
        return np.nan
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where(r > 0, p * r * np.log2(r / mean), 0.0)
    return float(terms.sum())


def tmaze_run_rates(s: dict, u: int, runs, seg: int, lo: int, hi: int):
    """Per-run firing rate (Hz) in bins lo..hi of one maze segment (unsmoothed; bins a run did not
    visit at speed are NaN). Returns runs x bins."""
    t, sg, dist = tmaze_linear(s)
    sp = np.abs(np.gradient(gaussian_filter1d(np.where(sg == 0, -dist, dist), 0.25 / np.median(np.diff(t))), t))
    dt = np.median(np.diff(t))
    b = (dist / TM_BIN_CM).astype(int)
    st = times(s, u)
    out = np.full((len(runs), hi - lo + 1), np.nan)
    for i, (a, z, *_) in enumerate(runs):
        m = (t >= a) & (t <= z) & (sg == seg) & (sp > SPEED_MIN) & (b >= lo) & (b <= hi)
        occ = np.bincount(b[m] - lo, minlength=hi - lo + 1) * dt
        k = np.clip(np.searchsorted(t, st[(st >= a) & (st <= z)]), 0, len(t) - 1)
        k = k[m[k]]
        c = np.bincount(b[k] - lo, minlength=hi - lo + 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            out[i] = np.where(occ > 0, c / occ, np.nan)
    return out


def pv_correlation(X: np.ndarray, Y: np.ndarray) -> float:
    """Mean over pixels of the Pearson correlation between the population vectors (cells x pixels)
    of two conditions, over pixels finite in both with some variance."""
    ok = np.all(np.isfinite(X), axis=0) & np.all(np.isfinite(Y), axis=0)
    x, y = X[:, ok], Y[:, ok]
    x = x - x.mean(axis=0)
    y = y - y.mean(axis=0)
    den = np.sqrt((x ** 2).sum(axis=0) * (y ** 2).sum(axis=0))
    good = den > 0
    if good.sum() == 0:
        return np.nan
    return float(((x * y).sum(axis=0)[good] / den[good]).mean())


def pv_remap(maps: list, k: int, rng: np.random.Generator, n=1000) -> np.ndarray:
    """Population-vector remapping index for n random draws of k cells; maps is a list of
    (A, B, A') rate maps of place cells."""
    A = np.stack([m[0].ravel() for m in maps])
    B = np.stack([m[1].ravel() for m in maps])
    C = np.stack([m[2].ravel() for m in maps])
    out = np.empty(n)
    for i in range(n):
        j = rng.choice(len(maps), size=k, replace=False)
        out[i] = pv_correlation(A[j], C[j]) - np.nanmean([pv_correlation(A[j], B[j]), pv_correlation(B[j], C[j])])
    return out
