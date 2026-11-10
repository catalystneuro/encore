"""Loading and checks for DANDI:001182 (Kennedy, Kunwar, Li et al. 2020, Nature 586, 730-734).

The dandiset holds one NWB file per mouse and imaging day (sub-M<k>-session<d>), each with a
cells-by-time trace matrix (processing/ophys/NeuralTrace) and one behavioural annotation channel
("Ch1: baseline", an IntervalSeries). Files are streamed from the archive with remfile and h5py;
nothing is written to disk.

Parameters and where they come from:

- DANDISET_VERSION: the only published version (see the notebook header for why it is pinned).
- STEP_Z = 15 and the robust SD of the frame-to-frame differences in `step_counts`: a standard
  choice for a descriptive check that marks discontinuities (steps far above a cell's own
  frame-to-frame noise); it decides no outcome.
- The cells-per-day measure in `cells_per_day` counts the columns of each file's trace matrix,
  which the file describes as CNMF-E output (Methods, "Microendoscopic imaging data acquisition
  and processing": traces "extracted ... using CNMF-E" and "manually screened"). The two ways of
  reading 187.3 (per mouse and day, as the claims file's unit has it, and summed over the five
  mice per day) are both computed.
"""

import re

import h5py
import numpy as np
import remfile
import requests

DANDISET_ID = "001182"
DANDISET_VERSION = "0.240827.1656"
API = "https://api.dandiarchive.org/api"

STEP_Z = 15.0


def list_assets(version=DANDISET_VERSION):
    """Every asset of a version: path, asset id, blob id and size, sorted by path."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        page = requests.get(url, timeout=60).json()
        out += page["results"]
        url = page.get("next")
    return sorted(
        [{"path": a["path"], "asset_id": a["asset_id"], "blob": a["blob"], "size": a["size"]} for a in out],
        key=lambda a: a["path"],
    )


def version_metadata(version=DANDISET_VERSION):
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/", timeout=60).json()


def _s3_url(asset_id):
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def _str(v):
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray):
        return [_str(x) for x in v.tolist()]
    return v


def _walk(f):
    """Every group and dataset in the file, with shape and attributes, outside the specifications."""
    rows = []

    def visit(name, obj):
        if name.startswith("specifications"):
            return
        attrs = {k: _str(v) for k, v in obj.attrs.items() if k not in ("object_id", "namespace")}
        if isinstance(obj, h5py.Dataset):
            rows.append({"name": name, "kind": "dataset", "shape": obj.shape, "dtype": str(obj.dtype), "attrs": attrs})
        else:
            rows.append({"name": name + "/", "kind": "group", "shape": None, "dtype": None, "attrs": attrs})

    f.visititems(visit)
    return rows


def load_file(asset):
    """Stream one file and return its traces, annotation and metadata."""
    f = h5py.File(remfile.File(_s3_url(asset["asset_id"])), "r")
    m = re.match(r"sub-(M\d+)-session(\d+)/", asset["path"])
    trace = f["processing/ophys/NeuralTrace"]
    epochs = f["processing/behavior/BehavioralEpochs"]
    s = {
        "path": asset["path"],
        "mouse": m.group(1),
        "day": int(m.group(2)),
        "traces": trace["data"][:],  # frames x cells
        "rate": float(trace["starting_time"].attrs["rate"]),
        "starting_time": float(trace["starting_time"][()]),
        "trace_unit": _str(trace["data"].attrs["unit"]),
        "trace_comments": _str(trace.attrs["comments"]),
        "trace_description": _str(trace.attrs["description"]),
        "ophys_description": _str(f["processing/ophys"].attrs["description"]),
        "behavior_description": _str(f["processing/behavior"].attrs["description"]),
        "epochs": {k: (epochs[k]["data"][:], epochs[k]["timestamps"][:]) for k in epochs},
        "acquisition": list(f["acquisition"].keys()),
        "analysis": list(f["analysis"].keys()),
        "stimulus": list(f["stimulus/presentation"].keys()) + list(f["stimulus/templates"].keys()),
        "intervals": list(f["intervals"].keys()) if "intervals" in f else [],
        "processing": {k: list(f["processing"][k].keys()) for k in f["processing"]},
        "has_imaging_planes": "general/optophysiology" in f,
        "contents": _walk(f),
    }
    for key, p in [("subject_id", "general/subject/subject_id"), ("age", "general/subject/age"),
                   ("sex", "general/subject/sex"), ("species", "general/subject/species"),
                   ("session_start", "session_start_time"), ("session_description", "session_description"),
                   ("experiment_description", "general/experiment_description"),
                   ("device", "general/devices/inscopix-miniscope")]:
        if p not in f:
            s[key] = None
        elif isinstance(f[p], h5py.Group):
            s[key] = {k: _str(v) for k, v in f[p].attrs.items() if k != "object_id"}
        else:
            s[key] = _str(f[p][()])
    f.close()
    return s


def load_all(version=DANDISET_VERSION):
    return [load_file(a) for a in list_assets(version)]


def step_counts(X, z=STEP_Z):
    """Per frame transition, the number of cells whose change from the previous frame exceeds z
    robust SDs (1.4826 MAD) of that cell's frame-to-frame changes. Standard choice, descriptive."""
    D = np.diff(X, axis=0)
    sd = 1.4826 * np.median(np.abs(D - np.median(D, axis=0)), axis=0) + 1e-12
    return (np.abs(D) / sd > z).sum(axis=1)


def mean_step(X):
    """Per frame transition, the mean over cells of |change| divided by the cell's robust SD of changes."""
    D = np.diff(X, axis=0)
    sd = 1.4826 * np.median(np.abs(D - np.median(D, axis=0)), axis=0) + 1e-12
    return (np.abs(D) / sd).mean(axis=1)


def max_cross_file_correlation(Xa, Xb, n_frames=None):
    """Largest absolute Pearson correlation between any column of Xa and any column of Xb, over
    their common first frames: a duplicate check (identical traces give 1)."""
    n = min(len(Xa), len(Xb)) if n_frames is None else n_frames
    A = Xa[:n] - Xa[:n].mean(0)
    B = Xb[:n] - Xb[:n].mean(0)
    A /= np.linalg.norm(A, axis=0) + 1e-12
    B /= np.linalg.norm(B, axis=0) + 1e-12
    return float(np.abs(A.T @ B).max())


def cell_features(X):
    """Per cell: SD, 99th percentile and skewness of its trace. Used to ask whether column order is
    shared across days (descriptive)."""
    from scipy import stats

    return np.column_stack([X.std(0), np.percentile(X, 99, axis=0), stats.skew(X, axis=0)])


def cells_per_day(sessions):
    """Cell counts by mouse and day, and the two readings of 'cells imaged per day'."""
    import pandas as pd

    df = pd.DataFrame([{"mouse": s["mouse"], "day": s["day"], "cells": s["traces"].shape[1]} for s in sessions])
    table = df.pivot(index="mouse", columns="day", values="cells")
    per_mouse_day = df.cells.to_numpy()
    totals = table.sum(axis=0).to_numpy()
    return {
        "table": table,
        "per_mouse_day_mean": per_mouse_day.mean(),
        "per_mouse_day_sem": per_mouse_day.std(ddof=1) / np.sqrt(len(per_mouse_day)),
        "per_day_totals": totals,
        "per_day_total_mean": totals.mean(),
        "per_day_total_sem": totals.std(ddof=1) / np.sqrt(len(totals)),
        "per_day_total_sd": totals.std(ddof=1),
    }
