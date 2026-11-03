"""Loading and per-trial summaries for dandiset 001535 (Natraj et al. 2025, Cell).

Natraj, Seko, Abiri, Miao, Yan, Graham, Tu-Chan, Chang & Ganguly (2025), Cell 188, 1208-1225,
doi:10.1016/j.cell.2025.02.001.

The dandiset holds one NWB file, sub-BRAVO1/sub-BRAVO1.nwb, for participant B1. Each of its 9737
trials is a TimeSeries `acquisition/trial_<n>` of shape (time, 256) with timestamps from 0 s in
steps of 0.01 s (100 Hz), and the trial table `intervals/trials` gives per trial `target_id`,
`is_virtual` and `is_robot`; its `start_time` and `stop_time` are marked "DUMMY". The dandiset
description says the 256 features are high-gamma amplitude (70 to 150 Hz) and low-frequency
signals (below 25 Hz) at 100 Hz on the 128 channels; it does not say which columns are which.
The Methods (Spatiotemporal feature extraction for RNNs) say each of the two feature matrices
"was transformed to have an L 2 norm of 1 and concatenated together", which the data check tests.

The file is streamed from the archive at the pinned version with remfile and h5py; nothing is
written to disk. Opening it with pynwb reads the metadata of all 9737 TimeSeries over the network
before any data, so the file is read with h5py, by the same paths pynwb uses. Reading each trial's
object header is the slow part (about 0.3 s per trial), so trials are read in parallel processes,
each with its own handle on the file. `WORKERS` is a standard choice that cannot change a result.

Per trial only summaries are kept: the length, the timestamp step, the L2 norm of each block of
128 columns, the mean of each column over time, the largest absolute value, and a hash of the
data, used to find trials deposited more than once. Also kept are the first and last `EDGE`
samples of the channel-averaged high gamma (columns 0 to 127, which the data check finds
non-negative), multiplied by sqrt(samples x 128) to undo the per-trial L2 scaling, so that the
time course at a trial's start and end can be compared across trials of different lengths. For
the trials asked for in `keep_binned`, the high gamma is kept in 200 ms bins per channel
(`BIN_SAMPLES`, from the Methods, Spatial feature extraction, as the claims file's figs3 criterion
gives it).

`pool_2x2` forms the 2x2 pooling of Figure S3. The file has no electrodes table, so the place of
each channel on B1's 8x16 grid is an assumption, passed in as `layout`.
"""

from __future__ import annotations

import hashlib
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "001535"
DANDISET_VERSION = "0.260608.0617"
ASSET_PATH = "sub-BRAVO1/sub-BRAVO1.nwb"
SAMPLING_HZ = 100.0     # dandiset description: down-sampled to 100 Hz; checked against timestamps
N_CHANNELS = 128        # Methods, ECoG array and implantation: B1 has a 128-channel 8x16 grid
WORKERS = 16            # parallel readers; I/O bound, a standard choice
EDGE = 100              # samples (1 s) kept at each end of a trial for the time course; a plotting choice
BIN_SAMPLES = 20        # 200 ms bins at 100 Hz (figs3 criterion, Methods: Spatial feature extraction)
SMOOTH_BINS = 5         # 1 s running average of 200 ms bins (same source)
GRID = (8, 16)          # Methods, ECoG array and implantation


def asset_url() -> str:
    """S3 URL of the file at the pinned version."""
    with DandiAPIClient() as client:
        asset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_asset_by_path(ASSET_PATH)
        return asset.get_content_url(follow_redirects=1, strip_query=True)


def open_file(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def file_metadata(url: str) -> dict:
    """Subject, session and trial table fields of the file."""
    f = open_file(url)
    dec = lambda v: v.decode() if isinstance(v, bytes) else v
    sub = f["general/subject"]
    meta = {
        "identifier": dec(f["identifier"][()]),
        "session_description": dec(f["session_description"][()]),
        "session_start_time": dec(f["session_start_time"][()]),
        "related_publications": [dec(v) for v in f["general/related_publications"][()]],
        "subject": {k: dec(sub[k][()]) for k in sub.keys()},
        "top_level": list(f.keys()),
        "processing": list(f["processing"].keys()),
        "analysis": list(f["analysis"].keys()),
        "electrodes": "extracellular_ephys/electrodes" in f["general"],
    }
    tr = f["intervals/trials"]
    meta["trial_columns"] = {c: dec(tr[c].attrs.get("description", "")) for c in tr.attrs["colnames"]}
    meta["trial_series_attrs"] = {k: dec(v) for k, v in f["acquisition/trial_1"].attrs.items()
                                  if k != "object_id"}
    meta["trial_series_unit"] = dec(f["acquisition/trial_1/data"].attrs["unit"])
    table = pd.DataFrame({c: tr[c][:] for c in ["id", "start_time", "stop_time", "target_id",
                                                 "is_virtual", "is_robot"]})
    # Listing the acquisition group takes minutes over the network; the trial series are named
    # trial_<id>, so the count is checked by the series after the last id being absent.
    meta["series_after_last_id"] = f"acquisition/trial_{int(table.id.max()) + 1}" in f
    return meta, table


def acquisition_names(url: str) -> list:
    """Names of every object in the acquisition group (slow: minutes over the network)."""
    return list(open_file(url)["acquisition"].keys())


def _summarise(args):
    url, ids, keep = args
    f = open_file(url)
    rows = []
    for i in ids:
        g = f[f"acquisition/trial_{i}"]
        x = g["data"][:]
        ts = g["timestamps"][:]
        dt = np.diff(ts)
        hg = x[:, :N_CHANNELS].mean(axis=1) * np.sqrt(x.shape[0] * N_CHANNELS)
        rows.append({
            "id": i,
            "n_samples": x.shape[0],
            "n_features": x.shape[1],
            "t_first": float(ts[0]),
            "t_last": float(ts[-1]),
            "dt_min": float(dt.min()) if len(dt) else np.nan,
            "dt_max": float(dt.max()) if len(dt) else np.nan,
            "norm_a": float(np.linalg.norm(x[:, :N_CHANNELS])),
            "norm_b": float(np.linalg.norm(x[:, N_CHANNELS:])),
            "min_a": float(x[:, :N_CHANNELS].min()),
            "min_b": float(x[:, N_CHANNELS:].min()),
            "abs_max": float(np.abs(x).max()),
            "n_nan": int(np.isnan(x).sum()),
            "hash": hashlib.sha1(np.ascontiguousarray(x).tobytes()).hexdigest(),
            "mean": x.mean(axis=0).astype(np.float32),
            "hg_start": hg[:EDGE].astype(np.float32),
            "hg_end": hg[-EDGE:].astype(np.float32),
            "binned": _bin(x[:, :N_CHANNELS]) if i in keep else None,
        })
    return rows


def _bin(x: np.ndarray) -> np.ndarray:
    """Mean of each channel in consecutive 200 ms bins; a last partial bin is dropped."""
    n = x.shape[0] // BIN_SAMPLES
    return x[:n * BIN_SAMPLES].reshape(n, BIN_SAMPLES, -1).mean(axis=1).astype(np.float32)


def running_mean(b: np.ndarray, k: int = SMOOTH_BINS) -> np.ndarray:
    """Running average over k bins within a trial, valid part only."""
    c = np.cumsum(np.vstack([np.zeros((1, b.shape[1])), b]), axis=0)
    return (c[k:] - c[:-k]) / k


def pool_2x2(b: np.ndarray, layout: np.ndarray) -> np.ndarray:
    """2x2 pooling with stride 2 of binned channels (time, 128) placed on the 8x16 grid.

    layout[r, c] is the column of the channel at grid row r, column c (an assumption: the file
    gives no electrode positions). Returns (time, 32)."""
    g = b[:, layout]                                   # (time, 8, 16)
    t = g.shape[0]
    return g.reshape(t, GRID[0] // 2, 2, GRID[1] // 2, 2).mean(axis=(2, 4)).reshape(t, -1)


def trial_summaries(url: str, ids, workers: int = WORKERS, keep_binned=()) -> pd.DataFrame:
    """Per-trial summaries for the given trial ids, read in parallel; binned high gamma is kept
    for the ids in keep_binned."""
    ids = list(ids)
    keep = set(int(i) for i in keep_binned)
    parts = [(url, ids[k::workers], keep) for k in range(workers)]
    with ProcessPoolExecutor(workers) as pool:
        rows = [r for part in pool.map(_summarise, parts) for r in part]
    return pd.DataFrame(rows).sort_values("id").reset_index(drop=True)


def read_trials(url: str, ids) -> dict:
    """Full data of a few trials, keyed by trial id."""
    f = open_file(url)
    return {i: f[f"acquisition/trial_{i}/data"][:] for i in ids}
