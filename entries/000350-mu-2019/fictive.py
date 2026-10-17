"""Loading and behavioural measures for the light-sheet fictive-swimming sessions of dandiset 000350.

Mu, Bennett, Rubinov et al. (2019), Cell 178, 27-43, doi:10.1016/j.cell.2019.05.050.

Each NWB file holds one paralysed larval zebrafish swimming fictively in a one-dimensional virtual
reality while its brain is imaged with a light-sheet microscope. Every file holds the raw signals
of the rig at 5989.6 Hz (two swim channels, the stimulus gain, the grating's baseline velocity,
the stimulus type and parameters, and the camera trigger), the swim bouts (`SwimIntervals`) and
a table of behavioural states (`ActivityStates`). Eight files also hold segmented cell traces
(`processing/ophys/DfOverF`), of neurons, of radial astrocytes ("glia"), or of both. Files are
streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Passive and active epochs follow the STAR Methods ("Futility-induced passivity behavioral
  analysis"): a passive epoch is a pause of `PASSIVE_GAP_S` (5 s) or more; an active epoch is a
  chain of bouts separated by pauses under 5 s whose first start and last end are more than 5 s
  apart. The pause is measured from the end of one bout to the start of the next, a choice made
  here (the Methods say "did not swim for at least 5 s").
- Open loop is gain 0 (Methods: "In open loop, the gain was zero"); closed loop is gain above 0.
  Both require the grating to move (baseline velocity above 0); `GAIN_EPS` and the 10 Hz grid of
  the condition signals (`COND_HZ`) are common choices made here.
- The windows of the onset analyses (baseline 10 to 5 s before onset, response 1 to 4 s after)
  are those of the Methods ("Analysis of component and cell activity around passivity onset").
- The whole-brain signal is the mean of the DfOverF series over an evenly spaced subset of ROI
  blocks (`N_ROI_BLOCKS` blocks of the file's chunk width); reading every ROI of every file
  would take far longer than the notebook's time limit. This is a choice made here.
"""

from __future__ import annotations

import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "000350"
DANDISET_VERSION = "0.240822.1759"
API = "https://api.dandiarchive.org/api"

COND_HZ = 10.0          # grid for the condition signals (gain, grating velocity)
GAIN_EPS = 1e-4         # gain at or below this is taken as 0 (open loop)
PASSIVE_GAP_S = 5.0     # Methods: passive if the fish did not swim for 5 s or more
MIN_SEGMENT_S = 10.0    # shorter condition periods are left out
N_ROI_BLOCKS = 8        # ROI blocks read per imaging series for the whole-brain signal
BASELINE = (-10.0, -5.0)  # Methods: baseline 10 to 5 s before passivity onset
RESPONSE = (1.0, 4.0)     # Methods: reliability from 1 to 4 s after onset


def assets(version: str = DANDISET_VERSION) -> list[dict]:
    """Every asset of the dandiset at a version, sorted by path."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=100"
    out = []
    while url:
        page = requests.get(url, timeout=60)
        page.raise_for_status()
        page = page.json()
        out += page["results"]
        url = page["next"]
    return sorted(out, key=lambda a: a["path"])


def open_asset(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/"), "r")


def _text(value) -> str:
    value = value[()] if hasattr(value, "shape") else value
    return value.decode() if isinstance(value, bytes) else str(value)


def _decimate(dataset, step: int, column: int | None = None) -> np.ndarray:
    data = dataset[:] if column is None else dataset[:, column]
    return data[::step]


def load_session(asset: dict) -> dict:
    """Metadata, behaviour, conditions and imaging layout of one file (no cell traces)."""
    f = open_asset(asset["asset_id"])
    g = f["general"]
    s = {"path": asset["path"], "asset_id": asset["asset_id"], "fish": asset["path"].split("/")[0][4:]}
    s["subject"] = {k: _text(v) for k, v in g["subject"].items()}
    s["session_start"] = _text(f["session_start_time"])
    s["session_description"] = _text(f["session_description"])
    s["planes"] = {}
    for name, grp in g["optophysiology"].items():
        plane = {k: _text(v) for k, v in grp.items() if isinstance(v, h5py.Dataset)}
        for c in grp:
            if isinstance(grp[c], h5py.Group) and "emission_lambda" in grp[c]:
                plane["emission_lambda"] = _text(grp[c]["emission_lambda"])
                plane["filter"] = _text(grp[c]["description"])
        s["planes"][name] = plane
    acq = f["acquisition"]
    rate = float(acq["SwimSignals/starting_time"].attrs["rate"])
    s["rate"] = rate
    s["n_samples"] = acq["SwimSignals/data"].shape[0]
    s["duration_s"] = s["n_samples"] / rate
    s["raw_series"] = {k: {"shape": acq[k]["data"].shape, "neurodata_type": _text(acq[k].attrs["neurodata_type"]),
                           "t": acq[k]["timestamps"][:]}
                       for k in acq if "Series" in k}
    step = int(round(rate / COND_HZ))
    s["cond_t"] = np.arange(0, s["n_samples"], step) / rate
    s["gain"] = _decimate(acq["StimulusGainSignal/data"], step)
    s["velocity"] = _decimate(acq["BaselineStimulusVelocitySignal/data"], step)
    s["protocol_code"] = _decimate(acq["StimulusParameterSignals/data"], step, 0)
    ttl = acq["FrameCaptureTTLSignal/data"][:]
    s["ttl_volume_starts"] = np.flatnonzero((ttl[1:] > 3.8) & (ttl[:-1] <= 3.8)) / rate
    s["ttl_range"] = (float(ttl.min()), float(ttl.max()))
    b = f["processing/behavior"]
    s["swims"] = pd.DataFrame({k: b["SwimIntervals"][k][:] for k in ["start_time", "stop_time", "power", "width"]})
    s["states"] = pd.DataFrame({"start": b["ActivityStates/start_time"][:], "stop": b["ActivityStates/stop_time"][:],
                                "type": [_text(x) for x in b["ActivityStates/state_type"][:]]})
    s["n_burst_events"] = b["BurstEvents/event_times"].shape[0]
    s["behavior_units"] = {"SwimSignals": _text(acq["SwimSignals/data"].attrs["unit"]),
                           "StimulusGainSignal": _text(acq["StimulusGainSignal/data"].attrs["unit"])}
    s["imaging"] = {}
    if "ophys" in f["processing"]:
        for name, series in f["processing/ophys/DfOverF"].items():
            d = series["data"]
            s["imaging"][name] = {"shape": d.shape, "chunks": d.chunks, "t": series["timestamps"][:],
                                  "unit": _text(d.attrs["unit"]), "description": _text(series.attrs["description"])}
    f.close()
    return s


def load_all(version: str = DANDISET_VERSION) -> list[dict]:
    with ThreadPoolExecutor(6) as ex:
        return list(ex.map(load_session, [a for a in assets(version) if a["path"].endswith(".nwb")]))


# --- conditions and epochs -----------------------------------------------------------------

def condition_masks(s: dict) -> dict[str, np.ndarray]:
    """Boolean masks on `cond_t`: closed loop, open loop (both with the grating moving), and
    any time with gain above 0."""
    moving = s["velocity"] > 0
    gain_on = s["gain"] > GAIN_EPS
    return {"closed": gain_on & moving, "open": ~gain_on & moving, "gain_on": gain_on}


def segments(t: np.ndarray, mask: np.ndarray, min_len: float = MIN_SEGMENT_S) -> list[tuple[float, float]]:
    """Contiguous periods where `mask` holds, as (start, stop) in seconds."""
    edges = np.flatnonzero(np.diff(np.r_[0, mask.astype(int), 0]))
    dt = t[1] - t[0]
    out = [(t[a], t[b - 1] + dt) for a, b in zip(edges[::2], edges[1::2])]
    return [(a, b) for a, b in out if b - a >= min_len]


def epochs_in_segment(swims: pd.DataFrame, seg: tuple[float, float], gap: float = PASSIVE_GAP_S) -> dict:
    """Passive and active epochs inside one condition period, by the Methods' rule.

    Passive epochs are pauses of `gap` or more between two bouts inside the period. Active epochs
    are chains of bouts separated by pauses under `gap`, longer than `gap` from first start to last
    end, and bounded on both sides by a pause of `gap` or more (a period edge counts as a pause
    only if the time to it is `gap` or more). Returns the epochs and every pause of `gap` or more,
    including those cut by the period's edges (for fractions of time).
    """
    a, b = seg
    w = swims[(swims.start_time >= a) & (swims.stop_time <= b)].sort_values("start_time")
    st, sp, pw = w.start_time.to_numpy(), w.stop_time.to_numpy(), w.power.to_numpy()
    if len(st) == 0:
        return {"passive": [], "active": [], "pauses": [(a, b)], "seg": seg}
    gaps = st[1:] - sp[:-1]
    passive = [(sp[i], st[i + 1]) for i in np.flatnonzero(gaps >= gap)]
    pauses = list(passive)
    if st[0] - a >= gap:
        pauses.append((a, st[0]))
    if b - sp[-1] >= gap:
        pauses.append((sp[-1], b))
    breaks = np.flatnonzero(gaps >= gap)
    starts = np.r_[0, breaks + 1]
    stops = np.r_[breaks, len(st) - 1]
    active = []
    for i0, i1 in zip(starts, stops):
        before = st[i0] - (sp[i0 - 1] if i0 > 0 else a)
        after = (st[i1 + 1] if i1 + 1 < len(st) else b) - sp[i1]
        if sp[i1] - st[i0] > gap and before >= gap and after >= gap:
            active.append({"start": st[i0], "stop": sp[i1], "n_bouts": i1 - i0 + 1,
                           "bout_starts": st[i0:i1 + 1], "bout_powers": pw[i0:i1 + 1],
                           "followed_by_passive": i1 + 1 < len(st)})
    return {"passive": passive, "active": active, "pauses": pauses, "seg": seg}


def session_epochs(s: dict, condition: str) -> list[dict]:
    m = condition_masks(s)[condition]
    return [epochs_in_segment(s["swims"], seg) for seg in segments(s["cond_t"], m)]


def passivity_onsets(s: dict) -> np.ndarray:
    """End of the last bout of each open-loop active epoch followed by a passive epoch."""
    return np.array(sorted(e["stop"] for seg in session_epochs(s, "open") for e in seg["active"]
                           if e["followed_by_passive"]))


def closed_loop_pause_onsets(s: dict) -> np.ndarray:
    """Starts of pauses of 5 s or more that begin while the gain is above 0 (closed loop with the
    grating moving or stationary), between two bouts."""
    sw = s["swims"].sort_values("start_time")
    st, sp = sw.start_time.to_numpy(), sw.stop_time.to_numpy()
    on = sp[:-1][(st[1:] - sp[:-1]) >= PASSIVE_GAP_S]
    gain_on = condition_masks(s)["gain_on"]
    idx = np.clip(np.searchsorted(s["cond_t"], on), 0, len(gain_on) - 1)
    # the gain must stay above 0 over the response window as well
    idx_end = np.clip(np.searchsorted(s["cond_t"], on + RESPONSE[1]), 0, len(gain_on) - 1)
    return on[gain_on[idx] & gain_on[idx_end]]


# --- imaging -------------------------------------------------------------------------------

def roi_blocks(n_rois: int, width: int, n_blocks: int = N_ROI_BLOCKS, offset: float = 0.0) -> list[tuple[int, int]]:
    """Evenly spaced blocks of `width` ROIs (the file's chunk width), `offset` in units of the
    spacing (0 for the main subset; 0.5 gives a disjoint subset)."""
    total = int(np.ceil(n_rois / width))
    spacing = total / n_blocks
    idx = sorted({int((i + offset) * spacing) for i in range(n_blocks)})
    return [(i * width, min((i + 1) * width, n_rois)) for i in idx]


def _block_sum(args):
    asset_id, name, lo, hi = args
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    with open_asset(asset_id) as f:
        d = f[f"processing/ophys/DfOverF/{name}/data"][:, lo:hi]
    return asset_id, name, d.sum(1), hi - lo


def whole_brain_means(jobs: list[tuple[dict, str, float]], workers: int = 4) -> dict:
    """Mean DfOverF over the ROI subset, per (fish, series, offset). Each block is read in its own
    process, as h5py reads one chunk at a time."""
    tasks, keys = [], []
    for s, name, offset in jobs:
        info = s["imaging"][name]
        for lo, hi in roi_blocks(info["shape"][1], info["chunks"][1], offset=offset):
            tasks.append((s["asset_id"], name, lo, hi))
            keys.append((s["fish"], name, offset))
    sums, counts = {}, {}
    with ProcessPoolExecutor(workers) as ex:
        for key, (_, _, total, n) in zip(keys, ex.map(_block_sum, tasks)):
            sums[key] = sums.get(key, 0) + total
            counts[key] = counts.get(key, 0) + n
    return {k: (sums[k] / counts[k], counts[k]) for k in sums}


def event_windows(t: np.ndarray, y: np.ndarray, onsets: np.ndarray, lags: np.ndarray) -> np.ndarray:
    """y interpolated at onset + lag, one row per onset (NaN outside the recording)."""
    grid = onsets[:, None] + lags[None, :]
    out = np.interp(grid, t, y)
    out[(grid < t[0]) | (grid > t[-1])] = np.nan
    return out


def window_mean(t: np.ndarray, y: np.ndarray, onsets: np.ndarray, window: tuple[float, float]) -> np.ndarray:
    """Mean of y over [onset + window[0], onset + window[1]] for each onset (NaN if empty)."""
    out = np.full(len(onsets), np.nan)
    for i, o in enumerate(onsets):
        sel = (t >= o + window[0]) & (t <= o + window[1])
        if sel.any():
            out[i] = y[sel].mean()
    return out


def mean_in_intervals(t: np.ndarray, y: np.ndarray, intervals) -> float:
    sel = np.zeros(len(t), bool)
    for a, b in intervals:
        sel |= (t >= a) & (t < b)
    return float(y[sel].mean()) if sel.any() else np.nan


def swim_rate(s: dict, t: np.ndarray) -> np.ndarray:
    """Number of bout starts in each imaging frame interval of `t`."""
    edges = np.r_[t, t[-1] + np.median(np.diff(t))]
    return np.histogram(s["swims"].start_time.to_numpy(), bins=edges)[0].astype(float)


def condition_labels(s: dict) -> np.ndarray:
    """Per `cond_t` sample: 1 closed loop, 2 open loop, 0 other (stationary grating)."""
    m = condition_masks(s)
    return np.where(m["closed"], 1, np.where(m["open"], 2, 0))


def seconds_since_switch(s: dict, t: np.ndarray) -> np.ndarray:
    """For times `t`, the time since the last switch between closed and open loop (periods of
    stationary grating carry the label of the condition before them)."""
    lab = pd.Series(condition_labels(s)).replace(0, np.nan).ffill().fillna(0).to_numpy()
    changes = s["cond_t"][1:][np.diff(lab) != 0]
    changes = np.r_[s["cond_t"][0], changes]
    last = changes[np.clip(np.searchsorted(changes, t, side="right") - 1, 0, None)]
    return t - last


def label_at(s: dict, t: np.ndarray) -> np.ndarray:
    idx = np.clip(np.searchsorted(s["cond_t"], t), 0, len(s["cond_t"]) - 1)
    return condition_labels(s)[idx]


def censored(y: np.ndarray) -> np.ndarray:
    """Frames at the start or end of a trace that repeat its first or last value exactly; the
    segmentation code (z6_components.py, `censor_tau`) sets such frames to a constant."""
    out = np.zeros(len(y), bool)
    i = 0
    while i < len(y) - 1 and y[i + 1] == y[0]:
        i += 1
    if i > 0:
        out[:i + 1] = True
    j = len(y) - 1
    while j > 0 and y[j - 1] == y[-1]:
        j -= 1
    if j < len(y) - 1:
        out[j:] = True
    return out


def plane_summary(version: str) -> pd.DataFrame:
    """Imaging plane names and indicators, and raw series names, of every file at a version."""
    def one(a):
        with open_asset(a["asset_id"]) as f:
            planes = f["general/optophysiology"]
            return {"fish": a["path"].split("/")[0][4:], "version": version,
                    "planes": ", ".join(f"{n} ({_text(planes[n]['indicator'])}, {_text(planes[n]['excitation_lambda'])} nm)"
                                        for n in planes),
                    "raw_series": ", ".join(k for k in f["acquisition"] if "Series" in k),
                    "swim_bouts": f["processing/behavior/SwimIntervals/start_time"].shape[0],
                    "sum_swim_starts": float(f["processing/behavior/SwimIntervals/start_time"][:].sum()),
                    "dfof_series": ", ".join(f"{k} {f['processing/ophys/DfOverF'][k]['data'].shape}"
                                             for k in (f["processing/ophys/DfOverF"] if "ophys" in f["processing"] else []))}
    with ThreadPoolExecutor(6) as ex:
        return pd.DataFrame(list(ex.map(one, [a for a in assets(version) if a["path"].endswith(".nwb")])))


def dfof_sample(asset_id: str, name: str, n_rois: int = 200) -> dict:
    """The first `n_rois` columns of a DfOverF series and of the matching Fluorescence series."""
    with open_asset(asset_id) as f:
        d = f[f"processing/ophys/DfOverF/{name}/data"]
        fl = f[f"processing/ophys/Fluorescence/{name.replace('DfOverF', 'Fluorescence')}/data"]
        return {"dfof": d[:, :n_rois].astype(float), "fluorescence": fl[:, :n_rois].astype(float),
                "dtype": str(d.dtype), "unit": _text(d.attrs["unit"])}
