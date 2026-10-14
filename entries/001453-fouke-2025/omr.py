"""Loading and measures for the freely swimming optomotor data of dandiset 001453.

Fouke, He, Loring & Naumann (2025), Current Biology, doi:10.1016/j.cub.2025.04.027.

Each NWB file holds one fish: x and y position (pixels), heading (`f0_theta`, radians), its
change per frame (`f0_vtheta`; the file says radians/s, the data show radians per frame),
velocity estimates, and per frame the stimulus code and trial number (`stim_index`). Files are
streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Trial processing follows the paper's analysis notebook, Fig1-S1.ipynb, in
  https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit
  33a5c297ff4ab6ff49f6bdd96139e9fdd867025c (the Methods give none of these): Savitzky-Golay
  smoothing of positions (21 frames, order 2); rejection of trials whose absolute cumulative
  heading change exceeds 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or
  whose mean speed exceeds 100 mm/s; measures from 3 s to 35 s after the first tracked frame;
  10 pixels per mm (the code divides pixels per second by 10 to give mm/s); per fish the median
  over trials. The 3 s stationary phase and the 32 s of motion are in the Methods.
- The names of the stimulus codes combine the protocol file sevenrep_twentyonestim.hdf of the
  stimulus software pandastim (https://github.com/Naumann-Lab/pandastim at commit
  7d9d1610be442c5a933e2575c071c64577e6312f), whose stimulus names, in order of first
  appearance, Fig1-S1.ipynb converts to the codes [10, 3, 16, 19, 12, 11, 15, 1, 14, 4, 6, 9,
  18, 8, 5, 13, 7, 2, 17, 0, 20]. Fig1-S1.ipynb itself labels code 9 as lateral right and 11
  as lateral left, the reverse of that conversion (its `remapDict` swaps them);
  `LATERAL_FROM_FIGURE_CODE` keeps the figure code's reading.
- Angular acceleration as the Methods define it (degrees per second squared) uses the heading
  resampled to `COMMON_HZ` (a common choice here, as the files' frame rates differ from 32 to
  171 Hz) and the code's 7-sample rolling medians. `code_angular_acceleration` reproduces what
  Fig1-S1.ipynb computes under that name.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.signal import savgol_filter

DANDISET_ID = "001453"
DANDISET_VERSION = "0.250518.1950"

PX_PER_MM = 10.0          # Fig1-S1.ipynb: pixels per second / 10 = mm/s
SAVGOL_WINDOW, SAVGOL_ORDER = 21, 2
MAX_CUM_ANGLE_10S = 1000.0   # degrees, first 10 s of a trial
MAX_CUM_ANGLE_35S = 2000.0   # degrees, first 35 s
MAX_SPEED_MM_S = 100.0
TRIAL_LIMIT_S = 35.0
MOTION_START_S = 3.0      # the stationary phase before the grating moves
COMMON_HZ = 30.0
ROLLING = 7               # Fig1-S1.ipynb, rolling medians of angular velocity and acceleration
ACCEL_RANGE = (10.0, 1000.0)  # Fig1-S1.ipynb keeps absolute values in this range, deg/s^2

# Stimulus codes and names: pandastim's protocol order mapped to codes by Fig1-S1.ipynb.
_PROTOCOL_NAMES = ["medial_right", "right", "forward_backward", "x_backward", "converging",
                   "lateral_right", "x_forward", "backward", "forward_x", "backward_right",
                   "forward_left", "lateral_left", "backward_x", "diverging", "forward_right",
                   "medial_left", "backward_left", "left", "backward_forward", "forward", "blank"]
_CODE_ORDER = [10, 3, 16, 19, 12, 11, 15, 1, 14, 4, 6, 9, 18, 8, 5, 13, 7, 2, 17, 0, 20]
STIMULUS_NAMES = dict(zip(_CODE_ORDER, _PROTOCOL_NAMES))
STIMULUS_NAMES[20] = "static"    # the protocol's "blank": 4 h without motion after the trials
LATERAL_FROM_FIGURE_CODE = {9: "lateral_right", 11: "lateral_left"}

WHOLE_FIELD = [20, 0, 5, 3, 4, 1, 7, 2, 6]     # Fig1-S1.ipynb's order for Figure 1D, G and H
RIGHTWARD, LEFTWARD = [3, 5, 4], [2, 6, 7]


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    value = value[()]
    return value.decode() if isinstance(value, bytes) else str(value)


def load_session(path: str, url: str) -> dict:
    """One fish: its metadata, and the frames that belong to a trial.

    Frames outside a trial (no stim_index) are dropped, and the static block (code 20, hours
    long) is cut to its first 60 s. Before that, the file's mean frame interval over tracked
    frames is kept as `code_dt`, which Fig1-S1.ipynb uses for its angular acceleration.
    """
    with h5py.File(remfile.File(url), "r") as f:
        subject = f["general/subject"]
        series = f["processing/behavior/BehavioralTimeSeries"]
        t = series["f0_x/timestamps"][:]
        data = {k: series[f"{k}/data"][:] for k in
                ("f0_x", "f0_y", "f0_theta", "f0_vtheta", "f0_vx", "f0_vy", "stimulus", "stim_index")}
        has_dist = "dist" in series
        if has_dist:
            data["dist"] = series["dist/data"][:]
        session = {
            "path": path,
            "subject_id": _text(subject["subject_id"]),
            "species": _text(subject["species"]),
            "age": _text(subject["age"]),
            "session_start": _text(f["session_start_time"]),
            "units": {k: series[f"{k}/data"].attrs.get("unit") for k in series},
            "descriptions": {k: series[k].attrs.get("description") for k in series},
            "same_timestamps": all(np.array_equal(series[f"{k}/timestamps"][:], t) for k in series),
            "has_dist": has_dist,
        }
    tracked = ~np.isnan(data["f0_x"])
    session["n_frames"] = len(t)
    session["n_tracked"] = int(tracked.sum())
    session["frame_hz"] = float(1 / np.median(np.diff(t)))
    session["code_dt"] = float(np.mean(np.diff(t[tracked])))
    session["x_range"] = (float(np.nanmin(data["f0_x"])), float(np.nanmax(data["f0_x"])))
    session["y_range"] = (float(np.nanmin(data["f0_y"])), float(np.nanmax(data["f0_y"])))
    in_trial = ~np.isnan(data["stim_index"])
    static = in_trial & (data["stimulus"] == 20)
    if static.any():
        start = t[static][0]
        in_trial &= ~(static & (t > start + 60))
    session["t"] = t[in_trial]
    for k, v in data.items():
        session[k] = v[in_trial]
    return session


def load_all(workers: int = 8) -> list[dict]:
    """Every fish in the dandiset, loaded in parallel."""
    urls = asset_urls()
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(lambda pu: load_session(*pu), urls))


def fish_key(session: dict) -> str:
    """Subject ids are reused across species, so a fish is named by species and subject."""
    return f"{'ZF' if session['species'] == 'Danio rerio' else 'DC'}-sub-{session['subject_id']}"


def trials(session: dict):
    """(trial number, stimulus code, indices of its tracked frames), in recorded order."""
    tracked = ~np.isnan(session["f0_x"])
    index = session["stim_index"]
    for number in np.unique(index):
        rows = np.flatnonzero((index == number) & tracked)
        if len(rows):
            yield int(number), int(session["stimulus"][rows[0]]), rows


def _path_length(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.hypot(np.diff(x), np.diff(y)).sum())


def _resample(t: np.ndarray, values: list[np.ndarray], hz: float = COMMON_HZ):
    grid = np.arange(t[0], t[-1], 1 / hz)
    return grid, [np.interp(grid, t, v) for v in values]


def trial_measures(session: dict) -> pd.DataFrame:
    """One row per trial: whether it passes the code's criteria, and its measures.

    speed_mm_s: path length of the smoothed positions from 3 to 35 s over that time (Fig1-S1).
    speed30_mm_s: the same from raw positions resampled to 30 Hz (variant).
    angvel_deg_s: summed heading change from 3 to 35 s over that time (Fig1-S1).
    steadiness: median over mean of the 30 Hz instantaneous speed, 3 to 35 s.
    """
    rows = []
    for number, code, idx in trials(session):
        t = session["t"][idx]
        x, y, vth = session["f0_x"][idx], session["f0_y"][idx], session["f0_vtheta"][idx]
        row = {"fish": fish_key(session), "species": fish_key(session)[:2], "path": session["path"],
               "trial": number, "code": code, "n_frames": len(idx), "passes": False}
        rows.append(row)
        if len(idx) < SAVGOL_WINDOW:
            row["reason"] = "too short"
            continue
        xs = savgol_filter(x, SAVGOL_WINDOW, SAVGOL_ORDER, mode="nearest")
        ys = savgol_filter(y, SAVGOL_WINDOW, SAVGOL_ORDER, mode="nearest")
        if session["has_dist"]:      # DC files carry `dist`, which the code uses in its check
            step = session["dist"][idx].copy()
            step[0] = 0
        else:
            step = np.concatenate([[0], np.hypot(np.diff(xs), np.diff(ys))])
        w35 = t < t[0] + TRIAL_LIMIT_S
        w10 = t < t[0] + 10
        cum10 = abs(np.sum(vth[w10]) * 180 / np.pi)
        cum35 = abs(np.sum(vth[w35]) * 180 / np.pi)
        span = t[w35][-1] - t[0]
        speed_check = (np.nansum(step[w35]) / PX_PER_MM) / span if span > 0 else np.inf
        if cum10 > MAX_CUM_ANGLE_10S or cum35 > MAX_CUM_ANGLE_35S or speed_check > MAX_SPEED_MM_S:
            row["reason"] = "criteria"
            continue
        keep = w35 & (t > 0)
        t, xs, ys, vth, xr, yr = t[keep], xs[keep], ys[keep], vth[keep], x[keep], y[keep]
        if len(t) < 2:
            row["reason"] = "empty"
            continue
        motion = (t > t[0] + MOTION_START_S) & (t < t[0] + TRIAL_LIMIT_S)
        if motion.sum() < 2:
            row["reason"] = "no motion phase"
            continue
        tm = t[motion]
        duration = tm[-1] - tm[0]
        row.update(passes=True, reason="", duration_s=duration,
                   speed_mm_s=_path_length(xs[motion], ys[motion]) / duration / PX_PER_MM,
                   angvel_deg_s=np.sum(vth[motion]) / duration * 180 / np.pi)
        if duration > 2 / COMMON_HZ:
            _, (gx, gy) = _resample(tm, [xr[motion], yr[motion]])
            inst = np.hypot(np.diff(gx), np.diff(gy)) * COMMON_HZ / PX_PER_MM
            row["speed30_mm_s"] = float(inst.mean()) if len(inst) else np.nan
            row["steadiness"] = float(np.median(inst) / inst.mean()) if len(inst) and inst.mean() > 0 else np.nan
    return pd.DataFrame(rows)


def _rolling_median(values: np.ndarray, window: int = ROLLING) -> np.ndarray:
    return pd.Series(values).rolling(window, min_periods=1).median().to_numpy()


def angular_acceleration(t: np.ndarray, vtheta: np.ndarray) -> np.ndarray:
    """Absolute angular acceleration (deg/s^2) as the Methods define it, at 30 Hz.

    Heading is the cumulative sum of the per-frame change, resampled to 30 Hz; angular velocity
    and acceleration are its first and second differences over time, each smoothed with the
    code's 7-sample rolling median.
    """
    if len(t) < 3 or t[-1] - t[0] < 3 / COMMON_HZ:
        return np.array([])
    _, (heading,) = _resample(t, [np.cumsum(vtheta)])
    omega = _rolling_median(np.diff(heading) * COMMON_HZ)
    alpha = _rolling_median(np.diff(omega) * COMMON_HZ)
    return np.abs(alpha) * 180 / np.pi


def code_angular_acceleration(vtheta: np.ndarray, code_dt: float) -> np.ndarray:
    """What Fig1-S1.ipynb computes as angular acceleration (deg/s^2 in its labels).

    Rolling median of the per-frame heading change, divided by the file's mean frame interval,
    rolling median again. This is an angular velocity, and the mean interval includes the gaps
    between trials in files that hold only trial frames.
    """
    return np.abs(_rolling_median(_rolling_median(vtheta) / code_dt)) * 180 / np.pi


def acceleration_frames(session: dict, passing: set) -> pd.DataFrame:
    """Per-frame absolute angular acceleration, 0 to 35 s into each passing trial, both ways."""
    out = []
    for number, code, idx in trials(session):
        if (session["path"], number) not in passing:
            continue
        t, vth = session["t"][idx], session["f0_vtheta"][idx]
        keep = (t < t[0] + TRIAL_LIMIT_S) & (t > 0)
        t, vth = t[keep], vth[keep]
        if len(t) < 3:
            continue
        window = (t > t[0]) & (t < t[0] + TRIAL_LIMIT_S)
        methods = angular_acceleration(t[window], vth[window])
        coded = code_angular_acceleration(vth, session["code_dt"])[window]
        for kind, values in (("methods", methods), ("code", coded)):
            values = values[(values > ACCEL_RANGE[0]) & (values < ACCEL_RANGE[1])]
            out.append(pd.DataFrame({"fish": fish_key(session), "species": fish_key(session)[:2],
                                     "code": code, "kind": kind, "accel": values.astype(np.float32)}))
    return pd.concat(out, ignore_index=True) if out else pd.DataFrame()


def fish_medians(measures: pd.DataFrame, column: str) -> pd.DataFrame:
    """Per fish and stimulus code, the median over passing trials (failing trials are NaN)."""
    m = measures.copy()
    m.loc[~m["passes"], column] = np.nan
    out = m.groupby(["species", "fish", "code"])[column].median().reset_index()
    return out.dropna(subset=[column])
