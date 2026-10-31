"""Loading for dandiset 000941 (FALCON Benchmark M1-A), read against Rouse & Schieber (2015).

Rouse AG, Schieber MH (2015). Spatiotemporal distribution of location and object effects in
reach-to-grasp kinematics. J Neurophysiol 114:3268-3282, doi:10.1152/jn.00686.2015.

The dandiset holds monkey L only. Each NWB file holds a trial table (`gocue_time`,
`move_onset_time`, `contact_time`, `reward_time`, `result`, `number`, `tgt_loc`, `tgt_obj`,
`obj_id`, `condition_id`), 16 channels of preprocessed EMG at 50 Hz (`preprocessed_emg`), an
`eval_mask`, and multiunit spike times from 64 channels (`units`). It holds no marker positions
and no joint angles. Files are streamed from the archive at the pinned version; nothing is
written to disk.

Where the parameters come from:

- `PAPER_SESSION` is the session of monkey L in the paper's Table 2 (L20120928).
- `APPARATUS_ORDER` is the fixed order of the objects on the apparatus, from the Fig. 1 legend
  of the paper: "positioned in a fixed clockwise order: a perpendicular cylinder ..., a coaxial
  cylinder ..., a button ..., and a sphere", with 157.5 degrees the leftmost location and 0
  degrees the right horizontal one, so that going clockwise the location angle decreases.
  `infer_object_names` uses it to name the codes of `obj_id`, which the files do not name.
- `SAMPLE_HZ` (200 frames/s) is the paper's video frame rate (Methods, Temporal Normalization),
  used to turn a median movement time into the number of normalized samples from M to C.
- The windows and the classifier of `decode_object` (100 ms windows of mean activity, linear
  discriminant analysis, 5-fold stratified cross-validation, seed 0) belong to the clock check
  of the data, not to any claim; they are standard choices that cannot change a claim's result.
"""

from __future__ import annotations

from functools import lru_cache

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000941"
DANDISET_VERSION = "0.241029.1405"
PAPER_SESSION = "20120928"
SAMPLE_HZ = 200.0

APPARATUS_ORDER = ["perpendicular cylinder", "coaxial cylinder", "button", "sphere"]  # clockwise

TRIAL_COLUMNS = ["start_time", "stop_time", "gocue_time", "move_onset_time", "contact_time",
                 "reward_time", "result", "number", "tgt_loc", "tgt_obj", "obj_id", "condition_id"]


@lru_cache(maxsize=1)
def assets() -> pd.DataFrame:
    """Every asset of the pinned version: path, size, split, session and S3 URL."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = []
        for a in ds.get_assets():
            name = a.path.split("/")[-1]
            rows.append({"path": a.path, "size": a.size,
                         "split": a.path.split("/")[0].replace("sub-MonkeyL-", ""),
                         "session": name.split("_ses-")[1].split("_")[0],
                         "url": a.get_content_url(follow_redirects=1, strip_query=True)})
    return pd.DataFrame(rows).sort_values(["split", "session"]).reset_index(drop=True)


def open_file(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def _text(x):
    return x.decode() if isinstance(x, bytes) else x


def read_trials(f: h5py.File) -> pd.DataFrame:
    g = f["intervals/trials"]
    t = pd.DataFrame({c: g[c][:] for c in TRIAL_COLUMNS})
    for c in ("result", "tgt_obj"):
        t[c] = t[c].map(_text)
    return t


def read_emg(f: h5py.File) -> tuple[np.ndarray, np.ndarray, list[str]]:
    """Timestamps (s), data (samples x muscles, in the file's unit) and muscle names."""
    g = f["acquisition/preprocessed_emg"]
    names = sorted(g.keys())
    ts = g[names[0]]["timestamps"][:]
    for n in names[1:]:
        assert np.array_equal(g[n]["timestamps"][:], ts)
    data = np.column_stack([g[n]["data"][:] for n in names])
    return ts, data, names


def read_spike_times(f: h5py.File) -> list[np.ndarray]:
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    return np.split(st, idx[:-1])


def file_summary(f: h5py.File) -> dict:
    s = f["general/subject"]
    return {"identifier": _text(f["identifier"][()]),
            "session_start": _text(f["session_start_time"][()]),
            "subject_id": _text(s["subject_id"][()]),
            "acquisition": sorted(f["acquisition"].keys()),
            "processing": sorted(f["processing"].keys()),
            "analysis": sorted(f["analysis"].keys()),
            "stimulus": sorted(f["stimulus/presentation"].keys()),
            "n_units": len(f["units/id"]),
            "n_emg_samples": f["acquisition/eval_mask/timestamps"].shape[0]}


def infer_object_names(trials: pd.DataFrame) -> tuple[dict, pd.DataFrame]:
    """Name the `obj_id` codes from the apparatus order of the paper's Fig. 1 legend.

    Within a block of trials at one apparatus orientation each object sits at a fixed location,
    and the objects are 45 degrees apart. The location minus the object's offset on the apparatus
    must then be constant within a block. The offsets are found from the trials (for each pair of
    codes, the most frequent difference of location between successive trials), ordered from the
    largest angle (leftmost) to the smallest, and named in the clockwise order of the legend.
    """
    t = trials.reset_index(drop=True)
    codes = sorted(t.obj_id.unique())
    diffs = {}
    for a, b in zip(t.index[:-1], t.index[1:]):
        oa, ob = t.obj_id[a], t.obj_id[b]
        if oa != ob:
            diffs.setdefault((oa, ob), []).append(t.tgt_loc[b] - t.tgt_loc[a])
    ref = codes[0]
    offset = {ref: 0.0}
    for c in codes[1:]:
        vals = pd.Series(diffs.get((ref, c), [np.nan]))
        offset[c] = vals.mode().iloc[0]
    order = sorted(codes, key=lambda c: -offset[c])           # leftmost first = clockwise order
    names = {c: APPARATUS_ORDER[i] for i, c in enumerate(order)}
    table = pd.DataFrame({"obj_id": order, "offset_deg": [offset[c] for c in order],
                          "name": [names[c] for c in order]})
    return names, table


def window_means(ts: np.ndarray, data: np.ndarray, times: np.ndarray, start: float, stop: float) -> np.ndarray:
    """Mean of each channel over [time + start, time + stop) for each event time."""
    out = np.empty((len(times), data.shape[1]))
    for i, t0 in enumerate(times):
        sel = (ts >= t0 + start) & (ts < t0 + stop)
        out[i] = data[sel].mean(axis=0) if sel.any() else np.nan
    return out


def decode_object(X: np.ndarray, y: np.ndarray, seed: int = 0) -> float:
    """5-fold stratified cross-validated accuracy of LDA (standard choices for a data check)."""
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.model_selection import StratifiedKFold, cross_val_score
    ok = np.isfinite(X).all(axis=1)
    cv = StratifiedKFold(5, shuffle=True, random_state=seed)
    return float(cross_val_score(LinearDiscriminantAnalysis(), X[ok], y[ok], cv=cv).mean())


def spike_counts(spikes: list[np.ndarray], times: np.ndarray, start: float, stop: float) -> np.ndarray:
    out = np.empty((len(times), len(spikes)))
    for j, s in enumerate(spikes):
        out[:, j] = np.searchsorted(s, times + stop) - np.searchsorted(s, times + start)
    return out
