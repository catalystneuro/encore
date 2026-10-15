"""Loading and measures for the torque-perturbation (muscle stretch) trials of dandiset 001636.

Pasquereau & Turner (2013), Frontiers in Systems Neuroscience 7:98, doi:10.3389/fnsys.2013.00098.

Each NWB file holds one recording session of one or two single units in M1 of monkey Venus or
Leu, with a trials table (task events, torque perturbation type and onset), joint angle, torque
command and, in Venus, rectified EMG. Files are streamed from the archive at the pinned version;
nothing is written to disk.

The analog streams of a file are stored back to back: each trial's segment follows the previous
one after a 3 s gap, but the segments are a few ms shorter than the trials, so the analog clock
falls behind the trials table by about 4.5 ms per trial. `load_session` puts each segment back
at the start time of its trial (`realign`), which the notebook checks against the torque
command. Spike times are on the trials table's clock.

Where the parameters come from:

- From the paper's Methods: spike density functions made with a causal gamma kernel (k = 1.5,
  theta = 20 ms) at 1 ms resolution (`GAMMA_K`, `GAMMA_THETA_MS`); baseline as the mean SDF over
  the 500 ms before torque onset (`BASELINE_MS`); a ms-by-ms two-tailed t-test over the 200 ms
  after onset at p < 0.002 (`DETECT_MS`, `P_THRESHOLD`); responses kept only when they begin 20
  to 60 ms after onset (`ONSET_RANGE_MS`); at least 5 perturbations per direction (`MIN_REPS`);
  the DSI and its categories; the three magnitude measures and the FWHM; the velocity
  threshold of 5 deg/s and the 25 Hz low-pass of the joint angle; the EMG baseline (200 ms
  before onset) and the m1 (15 to 40 ms) and m2 (41 to 80 ms) windows.
- Chosen here, as the Methods leave them open (fixed in the claims file before the analysis):
  the t-test compares the trials' SDF values at each ms with the cell's baseline rate (one
  sample); the response ends where the SDF first returns within the threshold, searched to 500
  ms (`OFFSET_SEARCH_MS`); the baseline for detection is that of the direction tested; the
  low-pass is a zero-phase Hamming-window FIR of 101 taps; movement onset is the first time
  after torque onset that velocity in the torque's direction exceeds 5 deg/s, peak velocity the
  maximum in the first 200 ms and amplitude the maximum displacement in the first 300 ms; the
  EMG response lasts while the session mean exceeds its baseline mean by 2 baseline SDs
  (`EMG_SD`), searched from 10 to 150 ms.
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import signal, stats

DANDISET_ID = "001636"
DANDISET_VERSION = "0.260518.1819"

MIN_REPS = 5                    # perturbations per direction for a cell to be studied
GAMMA_K, GAMMA_THETA_MS = 1.5, 20.0
KERNEL_MS = 300                 # kernel length; holds 99.9% of its mass
SPIKE_WINDOW_MS = (-1500, 600)  # spikes kept around each torque onset
SDF_START_MS = -1100            # first ms of the SDF (the kernel needs 300 ms of spikes before)
BASELINE_MS = (-500, 0)
DETECT_MS = (0, 200)
OFFSET_SEARCH_MS = 500
ONSET_RANGE_MS = (20, 60)
P_THRESHOLD = 0.002             # 0.01 / 5 independent comparisons
PSEUDO_SHIFT_MS = -500          # pseudo onset for the false-positive check, within the hold

ANALOG_WINDOW_MS = (-500, 500)
LOWPASS_HZ, FIR_TAPS = 25.0, 101
VEL_THRESHOLD = 5.0             # deg/s
PEAK_VEL_MS, AMPLITUDE_MS, ONSET_SEARCH_MS = 200, 300, 150
EMG_BASELINE_MS = (-200, 0)
M1_MS, M2_MS = (15, 40), (41, 80)
EMG_RESPONSE_MS = (10, 150)
EMG_SD = 2.0
EMG_CHANNELS = ("EMGTricepsLongus1", "EMGTricepsLongus2", "EMGTricepsLateralis")

DIRECTIONS = ("flexion", "extension")
SIGN = {"flexion": 1.0, "extension": -1.0}   # flexion torque raises the joint angle (checked)


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    return value.decode() if isinstance(value, bytes) else str(value)


def _ragged(group, name):
    data, index = group[name][:], group[f"{name}_index"][:]
    return np.split(data, index[:-1])


def realign(timestamps: np.ndarray, trial_starts: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Analog timestamps moved so that each trial's segment begins at its trial's start time.

    Segments are separated by gaps longer than 1 s. Returns the moved timestamps and the index
    of each segment's first sample. Raises if the number of segments differs from the trials.
    """
    breaks = np.flatnonzero(np.diff(timestamps) > 1.0) + 1
    first = np.r_[0, breaks]
    if len(first) != len(trial_starts):
        raise ValueError(f"{len(first)} analog segments for {len(trial_starts)} trials")
    shift = np.repeat(trial_starts - timestamps[first], np.diff(np.r_[first, len(timestamps)]))
    return timestamps + shift, first


def _window(t: np.ndarray, x: np.ndarray, t0: float, ms: tuple[int, int], step_ms: float) -> np.ndarray:
    grid = t0 + np.arange(ms[0], ms[1] + step_ms / 2, step_ms) / 1000
    i0, i1 = np.searchsorted(t, grid[0] - 0.05), np.searchsorted(t, grid[-1] + 0.05)
    tt, xx = t[i0:i1], x[i0:i1]
    if len(tt) < 2:
        return np.full(len(grid), np.nan)
    out = np.interp(grid, tt, xx)
    out[(grid < tt[0]) | (grid > tt[-1])] = np.nan
    return out


def _command_onset_ms(torque: np.ndarray, start_ms: int, threshold: float = 25.0) -> float:
    """First ms where the torque command leaves its baseline (median of the first 100 ms)."""
    base = np.nanmedian(torque[:100])
    dev = np.abs(torque - base) > threshold
    return float(np.argmax(dev) + start_ms) if dev.any() else np.nan


def load_session(path: str, url: str) -> dict:
    """One file: metadata, trials, units with spikes around each torque onset, and analog windows.

    For each perturbation trial the joint angle, the torque command and the triceps EMG are
    taken from -500 to +500 ms around the recorded onset on the realigned clock, at 1 ms steps
    (interpolated; Venus files are at 1 kHz). The torque command's onset is also measured on the
    stored clock (`command_onset_stored_ms`) for the data check. For every trial, the largest
    deviation of the angle from its median over the last 1 s before the lateral target
    (`hold_dev_deg`) shows whether the joint was perturbed during the hold.
    """
    with h5py.File(remfile.File(url), "r") as f:
        general = f["general"]
        session_id = _text(general["session_id"][()])
        tr = f["intervals/trials"]
        trials = pd.DataFrame({
            "start": tr["start_time"][:], "stop": tr["stop_time"][:],
            "center_on": tr["center_target_appearance_time"][:],
            "lateral_on": tr["lateral_target_appearance_time"][:],
            "reward": tr["reward_time"][:],
            "torque": [_text(v) for v in tr["torque_perturbation_type"][:]],
            "onset": tr["torque_perturbation_onset_time"][:],
        })
        un = f["units"]
        spikes = _ragged(un, "spike_times")
        units = []
        for i in range(len(un["id"])):
            units.append({
                "unit_name": int(_text(un["unit_name"][i])),
                "type": _text(un["neuron_projection_type"][i]),
                "antidromic_latency_ms": float(un["antidromic_latency_ms"][i]),
                "also_in": _text(un["unit_also_in_session_id"][i]),
                "is_post_mptp": bool(un["is_post_mptp"][i]),
                "spikes": spikes[i],
            })
        acq = sorted(f["acquisition"].keys())
        analog = {}
        if "ElbowAngle" in acq:
            analog["t_stored"] = f["acquisition/ElbowAngle/timestamps"][:]
            analog["angle"] = f["acquisition/ElbowAngle/data"][:].ravel()
            analog["torque"] = f["acquisition/ElbowTorque/data"][:].ravel()
            analog["emg_same_clock"] = True
            for name in EMG_CHANNELS:
                if name in acq:
                    analog[name] = f[f"acquisition/{name}/data"][:].ravel()
                    ts = f[f"acquisition/{name}/timestamps"]
                    if ts.shape != analog["t_stored"].shape or not np.array_equal(ts[:], analog["t_stored"]):
                        analog["emg_same_clock"] = False
    subject = session_id.split("++")[0]
    date = pd.Timestamp(session_id.split("++")[-1])
    session = {"path": path, "session_id": session_id, "subject": subject, "date": date,
               "post": "PostMPTP" in session_id, "acq": acq, "trials": trials, "units": units,
               "n_flex": int((trials.torque == "flexion").sum()),
               "n_ext": int((trials.torque == "extension").sum())}
    session["unit_post_flags"] = sorted({u["is_post_mptp"] for u in units})
    for u in units:      # every spike falls in a trial
        s = u["spikes"]
        k = np.searchsorted(trials.start.values, s, side="right") - 1
        u["outside_trials"] = int(np.sum((k < 0) | (s > trials.stop.values[np.clip(k, 0, None)] + 0.010)))
        u["sorted"] = bool(np.all(np.diff(s) >= 0))
    if not analog:
        return session
    t_stored = analog["t_stored"]
    session["analog_dt_ms"] = float(np.median(np.diff(t_stored)) * 1000)
    session["torque_all_nan"] = bool(np.isnan(analog["torque"]).all())
    session["emg_same_clock"] = analog["emg_same_clock"]
    session["emg_channels"] = [c for c in EMG_CHANNELS if c in analog]
    t_al, first = realign(t_stored, trials.start.values)
    session["analog_lag_ms"] = (trials.start.values - t_stored[first]) * 1000
    step = 1.0 if session["analog_dt_ms"] < 2 else round(session["analog_dt_ms"])
    hold = []
    for k, row in trials.iterrows():
        if np.isfinite(row.lateral_on):
            a = _window(t_al, analog["angle"], row.lateral_on, (-1000, 0), step)
            hold.append(float(np.nanmax(np.abs(a - np.nanmedian(a)))))
        else:
            hold.append(np.nan)
    trials["hold_dev_deg"] = hold
    pert = []
    for k, row in trials[trials.torque != "none"].iterrows():
        w = {"trial": k, "direction": row.torque, "onset": row.onset}
        w["angle"] = _window(t_al, analog["angle"], row.onset, ANALOG_WINDOW_MS, step)
        w["torque_cmd"] = _window(t_al, analog["torque"], row.onset, ANALOG_WINDOW_MS, step)
        stored = _window(t_stored, analog["torque"], row.onset, ANALOG_WINDOW_MS, step)
        w["command_onset_ms"] = _command_onset_ms(w["torque_cmd"], ANALOG_WINDOW_MS[0])
        w["command_onset_stored_ms"] = _command_onset_ms(stored, ANALOG_WINDOW_MS[0])
        w["lag_ms"] = session["analog_lag_ms"][k]
        for name in session["emg_channels"]:
            w[name] = _window(t_al, analog[name], row.onset, ANALOG_WINDOW_MS, step)
        pert.append(w)
    session["perturbations"] = pert
    return session


def load_all(paths_urls, workers: int = 16) -> list[dict]:
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(lambda pu: load_session(*pu), paths_urls))


# ---------------------------------------------------------------- spikes

def gamma_kernel() -> np.ndarray:
    """Causal gamma kernel at 1 ms steps, in spikes/s per spike."""
    t = np.arange(KERNEL_MS) + 0.5
    k = stats.gamma.pdf(t, a=GAMMA_K, scale=GAMMA_THETA_MS)
    return 1000 * k / k.sum()


_KERNEL = gamma_kernel()


def sdf(spike_ms: np.ndarray, start_ms: int = SDF_START_MS, stop_ms: int = OFFSET_SEARCH_MS) -> np.ndarray:
    """Spike density (spikes/s) from start_ms to stop_ms - 1, from spikes in ms relative to an event."""
    lo = start_ms - KERNEL_MS
    counts = np.bincount(np.floor(spike_ms[(spike_ms >= lo) & (spike_ms < stop_ms)] - lo).astype(int),
                         minlength=stop_ms - lo)[:stop_ms - lo]
    full = np.convolve(counts, _KERNEL)[:stop_ms - lo]
    return full[KERNEL_MS:]


def trial_sdfs(spikes: np.ndarray, onsets: np.ndarray, shift_ms: float = 0.0) -> np.ndarray:
    """One SDF per onset (rows), on the grid SDF_START_MS .. OFFSET_SEARCH_MS - 1 ms."""
    rows = []
    for t0 in onsets:
        rel = (spikes - t0) * 1000 - shift_ms
        rows.append(sdf(rel))
    return np.array(rows)


GRID = np.arange(SDF_START_MS, OFFSET_SEARCH_MS)


def _ms(lo, hi):
    return (GRID >= lo) & (GRID < hi)


def detect(sdfs: np.ndarray, paired: bool = False) -> dict:
    """Response of one cell to one direction, by the Methods' ms-by-ms t-test.

    sdfs: trials x GRID. The baseline is the mean SDF over BASELINE_MS. Each ms from 0 to
    OFFSET_SEARCH_MS is tested two-tailed: one-sample against the baseline rate (main), or
    paired against each trial's own baseline mean (variant, paired=True). A response is the
    first crossing into significance (p < P_THRESHOLD) at 20 to 60 ms; a significant run that
    is already under way at 20 ms is not one. It ends at the first non-significant ms.
    """
    base_trials = sdfs[:, _ms(*BASELINE_MS)].mean(1)
    base = float(base_trials.mean())
    post = sdfs[:, _ms(0, OFFSET_SEARCH_MS)]
    with np.errstate(all="ignore"):
        if paired:
            p = stats.ttest_rel(post, base_trials[:, None], axis=0).pvalue
        else:
            p = stats.ttest_1samp(post, base, axis=0).pvalue
    p = np.where(np.isfinite(p), p, 1.0)
    sig = p < P_THRESHOLD
    mean = post.mean(0)
    out = {"baseline": base, "n_trials": len(sdfs), "mean": mean, "responds": False}
    starts = np.flatnonzero(sig[1:DETECT_MS[1]] & ~sig[:DETECT_MS[1] - 1]) + 1
    starts = starts[(starts >= ONSET_RANGE_MS[0]) & (starts <= ONSET_RANGE_MS[1])]
    # the largest change from baseline in the detection epoch, signed (for the DSI)
    d = mean[:DETECT_MS[1]] - base
    out["max_change_signed"] = float(d[np.argmax(np.abs(d))])
    if not len(starts):
        return out
    on = int(starts[0])
    rest = np.flatnonzero(~sig[on:])
    off = on + int(rest[0]) if len(rest) else OFFSET_SEARCH_MS
    sign = 1.0 if mean[on] > base else -1.0
    change = (mean[on:off] - base) * sign
    signed = (mean - base) * sign
    peak = on + int(np.argmax(change))
    half = signed[peak] / 2
    left = peak
    while left > 0 and signed[left - 1] >= half:
        left -= 1
    right = peak
    while right < len(signed) - 1 and signed[right + 1] >= half:
        right += 1
    out.update(responds=True, latency=on, offset=off, sign=sign,
               mean_change=float(change.mean()), max_change=float(change.max()),
               auc=float(change.sum() / 1000), fwhm=float(right - left + 1))
    return out


def dsi(flex: dict, ext: dict) -> tuple[float, str]:
    """Directional selectivity index and category of a torque-related cell.

    DSI = |1 - NP/P|, with P and NP the signed largest changes from baseline over 0 to 200 ms
    in the preferred (larger) and the other direction. Category: unidirectional when only one
    direction has a response; with both, reciprocal when they have opposite signs, otherwise
    bidirectional when DSI > 0.5 and non-directional when not.
    """
    a, b = flex["max_change_signed"], ext["max_change_signed"]
    p_, np_ = (a, b) if abs(a) >= abs(b) else (b, a)
    index = abs(1 - np_ / p_) if p_ != 0 else np.nan
    if flex["responds"] and ext["responds"]:
        if flex["sign"] != ext["sign"]:
            cat = "reciprocal"
        else:
            cat = "bidirectional" if index > 0.5 else "non-directional"
    elif flex["responds"] or ext["responds"]:
        cat = "unidirectional"
    else:
        cat = "none"
    return float(index), cat


# ---------------------------------------------------------------- kinematics and EMG

_FIR = signal.firwin(FIR_TAPS, LOWPASS_HZ, fs=1000.0, window="hamming")
_AX = np.arange(ANALOG_WINDOW_MS[0], ANALOG_WINDOW_MS[1] + 1)


def kinematics(angle: np.ndarray, direction: str) -> dict:
    """Torque-evoked displacement of one trial, from the angle at 1 ms steps around onset."""
    if np.isnan(angle).any():
        return {"valid": False}
    s = SIGN[direction]
    smooth = signal.filtfilt(_FIR, [1.0], angle)
    vel = np.gradient(smooth) * 1000 * s
    rel = (angle - angle[(_AX >= -50) & (_AX < 0)].mean()) * s
    after = _AX >= 0
    v, a = vel[after], rel[after]
    pre_moving = bool(vel[(_AX >= -10) & (_AX < 0)].max() > VEL_THRESHOLD)
    cross = np.flatnonzero(v[:ONSET_SEARCH_MS] > VEL_THRESHOLD)
    return {"valid": bool(len(cross)) and not pre_moving,
            "pre_moving": pre_moving,
            "latency_ms": float(cross[0]) if len(cross) else np.nan,
            "peak_velocity": float(v[:PEAK_VEL_MS].max()),
            "amplitude": float(a[:AMPLITUDE_MS].max())}


def emg_response(traces: np.ndarray, sd: float = EMG_SD) -> dict:
    """Session-average EMG response, baseline-subtracted, from trials x 1 ms windows."""
    mean = np.nanmean(traces, axis=0)
    b = (_AX >= EMG_BASELINE_MS[0]) & (_AX < EMG_BASELINE_MS[1])
    norm = mean - mean[b].mean()
    thr = sd * mean[b].std()
    win = (_AX >= EMG_RESPONSE_MS[0]) & (_AX <= EMG_RESPONSE_MS[1])
    above = np.flatnonzero(win & (norm > thr))
    return {"m1": float(norm[(_AX >= M1_MS[0]) & (_AX <= M1_MS[1])].mean()),
            "m2": float(norm[(_AX >= M2_MS[0]) & (_AX <= M2_MS[1])].mean()),
            "onset_ms": float(_AX[above[0]]) if len(above) else np.nan,
            "duration_ms": float(_AX[above[-1]] - _AX[above[0]] + 1) if len(above) else np.nan,
            "trace": norm}


def short_type(t: str) -> str:
    return {"pyramidal_tract_neuron": "PTN", "corticostriatal_neuron": "CSN"}.get(t, "other")
