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
data, used to find trials deposited more than once.
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


def _summarise(args):
    url, ids = args
    f = open_file(url)
    rows = []
    for i in ids:
        g = f[f"acquisition/trial_{i}"]
        x = g["data"][:]
        ts = g["timestamps"][:]
        dt = np.diff(ts)
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
        })
    return rows


def trial_summaries(url: str, ids, workers: int = WORKERS) -> pd.DataFrame:
    """Per-trial summaries for the given trial ids, read in parallel."""
    ids = list(ids)
    parts = [(url, ids[k::workers]) for k in range(workers)]
    with ProcessPoolExecutor(workers) as pool:
        rows = [r for part in pool.map(_summarise, parts) for r in part]
    return pd.DataFrame(rows).sort_values("id").reset_index(drop=True)


def read_trials(url: str, ids) -> dict:
    """Full data of a few trials, keyed by trial id."""
    f = open_file(url)
    return {i: f[f"acquisition/trial_{i}/data"][:] for i in ids}
