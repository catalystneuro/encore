"""Loading and measures for the mouse olfactory bulb imaging of dandiset 001170, and for the
locust recordings the paper deposited on Figshare.

Ling, Moss, Smith, Deng, Kroeger, Reimer, Raman & Arenkiel, "Conserved neural dynamics and
computations across species in olfaction", bioRxiv doi:10.1101/2023.04.24.538157 (v2, 2024).

Each NWB file holds one imaging session: raw fluorescence of glomerular ROIs in three fields of
view (`processing/ophys/fluorescence/fluorescence_FOV{1,2,3}_channel1`, unit "n.a.", not dF/F),
their timestamps on the odor clock, and a trials table whose rows are 1-s odor valve openings
(`odorant`, `concentration`). Files are streamed from the archive at the pinned version; nothing
is written to disk. Only the fluorescence and the trials table are read.

Where the parameters come from:

- The protocol (5 s odor pulses, 55 s inter-trial interval, blocks of 10 trials, 15 min between
  blocks; sequential pairs with 1 s between the two odors; random order with 1 s pulses and 19 s
  intervals) is in the paper's Methods, "Odor delivery to mice". Presentations are rebuilt from
  the trials table by joining consecutive 1-s rows of one odor.
- The windows (2 s before onset, 5 s ON, 5 s OFF after offset, 50 s ITI, 15 min IBI in 1-min
  bins, 17 s after offset in the random-order sessions) are in the Methods. The paper's code
  (Figshare doi:10.6084/m9.figshare.31435543.v2, Script_Fig2.m to Script_Fig6.m) counts frames
  at a nominal 16 frames per second; here the windows are placed in seconds, on a 16 Hz grid
  interpolated from each session's own frame times (13.7 to 17.8 Hz).
- dF/F: the Methods say traces were "converted to dF/F" without a baseline. For responses to an
  odor (ON, OFF, sequential), F0 is the mean of the 2 s before onset of that trial and ROI (a
  common choice). For the ITI and IBI analyses, where a pre-trial baseline would subtract the
  activity being measured, F0 is the median of the ROI's F over the session (a common choice).
  The arrays the paper deposited on Figshare are close to a z-score of F within each trial
  window; `zscore_trials` gives that as a variant.
- Population vectors follow the paper's code: trial-averaged traces, minus the median across
  glomeruli at each frame (`medRsp` in Script_Fig2.m and Script_Fig3.m), and angles between
  vectors centred over the analysed frames (the code takes angles between PCA scores, which are
  the centred vectors in a rotated basis).
- k-nearest-neighbour classifiers: k, the distance and leave-one-trial-out follow the Methods
  (k = 10 with correlation distance for the time-bin classifiers; k = 20 with angular distance
  for the ITI averages, from the Figure 7H legend; k = 50 for the IBI). Ties in the vote go to
  the lowest label, as MATLAB's `mode` does in the code.
"""

from __future__ import annotations

import hashlib
import io
import time
import urllib.error
import urllib.request

import h5py
import numpy as np
import pandas as pd
import remfile
import scipy.io as sio
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "001170"
DANDISET_VERSION = "0.260528.1016"

GRID_HZ = 16.0            # the paper's nominal frame rate (metaData.mat, fps = 16)
PRE_S, ON_S, OFF_S = 2.0, 5.0, 5.0
ITI_S = 50.0              # Methods: the 50 s after offset
SEQ_GAP_S = 1.0           # Methods: 1 s between the two odors of a sequential pair
RANDOM_ITI_S = 17.0       # Methods: the 17 s after offset in the random-order sessions
IBI_BIN_S, IBI_BINS = 60.0, 15
EMPTY = "Empty"

ABBREV = {"methyl salicylate": "msc", "acetophenone": "ace", "allyl sulfide": "als", "eugenol": "eug",
          "1,4-cineole": "cin", "2-methypyrazine": "mpz", "2-ethylphenol": "2ep", "isoeugenol": "ieg",
          "trans-cinnamaldehyde": "tcm", "anisole": "ani", "anisaldehyde": "asa"}
BLOCK_ODORS = ["msc", "ace", "als", "eug"]

# Figshare record of the paper's code and data (version 2), with the md5 the record gives.
FIGSHARE_DOI = "10.6084/m9.figshare.31435543.v2"
FIGSHARE_FILES = {
    "data1_mouse_glom198.mat": (62248975, "6fddcfa31f91eeb1a1d91637acccef99"),
    "data2_locust_PN66.mat": (62248987, "efcc53df471247b37984d12b9532bdd0"),
    "data4_locust_PN85.mat": (62249047, "666126aba6373dc74219b990f339b019"),
    "data5_locust_PN85.mat": (62249038, "f4005011e14874cefe66a93fa693ad61"),
}


# --- the archive ---------------------------------------------------------------------------

def asset_urls(version: str = DANDISET_VERSION) -> dict[str, str]:
    """Path -> streaming URL of every NWB file at a version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, version)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)
                for a in dandiset.get_assets() if a.path.endswith(".nwb")}


def asset_table(version: str) -> pd.DataFrame:
    """Path, asset id, blob and size of every asset at a version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, version)
        rows = []
        for a in dandiset.get_assets():
            raw = a.get_raw_metadata()
            rows.append({"path": a.path, "asset_id": a.identifier, "size": a.size,
                         "digest": raw.get("digest", {}).get("dandi:dandi-etag")})
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def _text(value) -> str:
    value = value[()]
    return value.decode() if isinstance(value, bytes) else str(value)


def presentations(trials: pd.DataFrame) -> pd.DataFrame:
    """Odor presentations: consecutive 1-s rows of one odorant, less than 1.05 s apart.

    Columns: odor (abbreviation), odorant (as in the file), onset, offset, rows, concentration,
    and, for the block protocol, block (index of runs separated by more than 300 s), kind
    ('solitary', 'seq_first' or 'seq_second') and trial (index within its block and kind).
    """
    t, names = trials.start_time.to_numpy(), trials.odorant.to_numpy()
    out, i = [], 0
    while i < len(t):
        j = i
        while j + 1 < len(t) and names[j + 1] == names[i] and t[j + 1] - t[j] < 1.05:
            j += 1
        if names[i] != EMPTY:
            out.append({"odorant": names[i], "odor": ABBREV.get(names[i].lower(), names[i]),
                        "onset": t[i], "offset": trials.stop_time.iloc[j], "rows": j - i + 1,
                        "concentration": trials.concentration.iloc[i]})
        i = j + 1
    p = pd.DataFrame(out)
    gap_next = np.append(np.diff(p.onset), np.inf)
    gap_prev = np.insert(np.diff(p.onset), 0, np.inf)
    p["kind"] = np.where(gap_next < 7, "seq_first", np.where(gap_prev < 7, "seq_second", "solitary"))
    p["block"] = np.cumsum(np.insert(np.diff(p.onset) > 300, 0, True)) - 1
    p["trial"] = p.groupby(["block", "kind"]).cumcount()
    return p


def protocol_of(p: pd.DataFrame) -> str:
    """'block' for 5-s pulses in blocks, 'random' for 1-s pulses every 20 s."""
    if (p.rows >= 4).all():
        return "block"
    if (p.rows == 1).all():
        return "random"
    return "other"


def open_session(path: str, url: str) -> dict:
    """Metadata, trials and the raw fluorescence of all ROIs (FOV1, FOV2, FOV3 in that order)."""
    with h5py.File(remfile.File(url), "r") as f:
        fl = f["processing/ophys/fluorescence"]
        names = sorted(fl.keys())
        t = fl[names[0]]["timestamps"][:]
        same_t = all(np.array_equal(fl[n]["timestamps"][:], t) for n in names)
        F = np.concatenate([fl[n]["data"][:] for n in names], axis=1)
        tr = f["intervals/trials"]
        trials = pd.DataFrame({
            "start_time": tr["start_time"][:], "stop_time": tr["stop_time"][:],
            "odorant": [x.decode() for x in tr["odorant"][:]],
            "concentration": tr["concentration"][:]})
        acq = f["acquisition"]
        tps = {k: (acq[k]["data"].shape[0], float(np.median(np.diff(acq[k]["timestamps"][:2000]))))
               for k in acq if k.startswith("two_photon")}
        g = f["general"]
        s = {
            "path": path, "subject": _text(g["subject/subject_id"]), "session": _text(g["session_id"]),
            "sex": _text(g["subject/sex"]), "dob": _text(g["subject/date_of_birth"])[:10],
            "subject_description": _text(g["subject/description"]),
            "start": _text(f["session_start_time"]),
            "indicator": _text(g["optophysiology/imaging_plane_channel1/indicator"]),
            "location": _text(g["optophysiology/imaging_plane_channel1/location"]),
            "unit": fl[names[0]]["data"].attrs["unit"],
            "rois_per_fov": [fl[n]["data"].shape[1] for n in names],
            "same_timestamps": same_t, "two_photon": tps,
            "behavior": [k for k in acq if not k.startswith("two_photon")],
        }
    s.update(F=F.astype(np.float32), t=t, trials=trials, n_rois=F.shape[1], n_frames=len(t),
             frame_hz=float(1 / np.median(np.diff(t))), F_median=np.median(F, axis=0))
    s["pres"] = presentations(trials)
    s["protocol"] = protocol_of(s["pres"])
    return s


def windows(s: dict, onsets: np.ndarray, start: float, stop: float) -> np.ndarray:
    """F on a 16 Hz grid from onset+start to onset+stop: trials x frames x ROIs."""
    grid = np.arange(int(round((stop - start) * GRID_HZ))) / GRID_HZ + start
    idx = np.searchsorted(s["t"], onsets[:, None] + grid[None, :])
    idx = np.clip(idx, 1, len(s["t"]) - 1)
    t0, t1 = s["t"][idx - 1], s["t"][idx]
    w = ((onsets[:, None] + grid[None, :]) - t0) / (t1 - t0)
    F = s["F"]
    return (F[idx - 1] * (1 - w[..., None]) + F[idx] * w[..., None]).astype(np.float32)


def frame_windows(s: dict, onsets: np.ndarray, pre_frames: int, n_frames: int) -> np.ndarray:
    """Consecutive frames, as the paper's code takes them: the frame at or after each onset
    less `pre_frames`, then `n_frames` frames."""
    first = np.searchsorted(s["t"], onsets) - pre_frames
    return np.stack([s["F"][i:i + n_frames] for i in first])


def dff_pre(win: np.ndarray, pre_s: float = PRE_S) -> np.ndarray:
    """(F - F0) / F0 with F0 the mean of the first `pre_s` seconds of each trial and ROI."""
    n = int(pre_s * GRID_HZ)
    f0 = win[:, :n].mean(axis=1, keepdims=True)
    return (win - f0) / f0


def dff_session(win: np.ndarray, s: dict) -> np.ndarray:
    """(F - F0) / F0 with F0 the ROI's median F over the session."""
    return (win - s["F_median"]) / s["F_median"]


def zscore_trials(win: np.ndarray) -> np.ndarray:
    """Variant: each trial and ROI z-scored over its window, close to the deposited arrays."""
    return (win - win.mean(axis=1, keepdims=True)) / win.std(axis=1, keepdims=True)


SOL_WINDOW = (-PRE_S, ON_S + 55.0)         # a solitary trial, 2 s before onset to the next trial
SEQ_WINDOW = (-PRE_S, ON_S + 55.0)         # a sequential pair, to the next pair
RANDOM_WINDOW = (-PRE_S, 1.0 + RANDOM_ITI_S + 1.0)
RANDOM_TRIALS = 10                         # Methods: the first 10 trials of each odor


def reduce_session(path: str, url: str) -> dict:
    """One session, reduced as it loads to what the analyses use.

    Block protocol: `sol` (solitary trials, 2 s before onset to 60 s after, 16 Hz grid),
    `sol_frames` (the same trials as 912 consecutive frames from 32 frames before onset, as the
    code takes them), `seq` (sequential pairs, from 2 s before the first onset to 60 s after),
    `ibi` (per solitary block, up to 15 one-minute means of F from the end of its last ITI, only
    minutes before the next presentation and the end of imaging), `pre_block` (per solitary
    block, mean F over the 15 min before its first onset, or as much as there is), and `pseudo`
    (per solitary block, the 5 to 55 s windows of up to ten pseudo-trials that continue the
    block's 60.4 s rhythm into the following inter-block interval, where no odor is given).
    Random order: `rnd` (the first 10 presentations of each odor, 2 s before onset to 19 s after).
    Raw F is kept in these arrays; dF/F is computed by the analyses.
    """
    s = open_session(path, url)
    p = s["pres"]
    out = {k: v for k, v in s.items() if k not in ("F", "t")}
    out["clock"] = {"t_first": float(s["t"][0]), "t_last": float(s["t"][-1])}
    if s["protocol"] == "block":
        sol = p[p.kind == "solitary"].reset_index(drop=True)
        out["sol_pres"] = sol
        out["sol"] = windows(s, sol.onset.to_numpy(), *SOL_WINDOW)
        out["sol_frames"] = frame_windows(s, sol.onset.to_numpy(), 32, 912)
        first = p[p.kind == "seq_first"].reset_index(drop=True)
        out["seq_pres"] = first
        out["seq"] = windows(s, first.onset.to_numpy(), *SEQ_WINDOW)
        ibi, pre_block = {}, {}
        for b, blk in sol.groupby("block"):
            start = blk.onset.max() + 60.0
            later = p.onset[p.onset > blk.onset.max()]
            stop = min(start + IBI_BINS * IBI_BIN_S, later.min() if len(later) else np.inf, s["t"][-1])
            n = int((stop - start) // IBI_BIN_S)
            ibi[blk.odor.iloc[0]] = np.stack([
                s["F"][(s["t"] >= start + i * IBI_BIN_S) & (s["t"] < start + (i + 1) * IBI_BIN_S)].mean(0)
                for i in range(n)]) if n else np.zeros((0, s["n_rois"]), np.float32)
            onset = blk.onset.min()
            earlier = p.offset[p.offset < onset]
            lo = max(onset - 900.0, earlier.max() + 60.0 if len(earlier) else -np.inf, s["t"][0])
            sel = (s["t"] >= lo) & (s["t"] < onset)
            pre_block[blk.odor.iloc[0]] = (s["F"][sel].mean(0), float(onset - lo))
        pseudo = {}
        for b, blk in sol.groupby("block"):
            last = blk.onset.max()
            later = p.onset[p.onset > last]
            limit = min(later.min() if len(later) else np.inf, s["t"][-1])
            ons = np.array([last + 60.4 * j for j in range(1, 11) if last + 60.4 * j + 55.0 < limit])
            pseudo[blk.odor.iloc[0]] = (windows(s, ons, ON_S, ON_S + ITI_S) if len(ons)
                                        else np.zeros((0, int(ITI_S * GRID_HZ), s["n_rois"]), np.float32))
        out["ibi"], out["pre_block"], out["pseudo"] = ibi, pre_block, pseudo
    elif s["protocol"] == "random":
        q = p[p.odorant != EMPTY].copy()
        q["previous"] = p.odor.shift(1).reindex(q.index)
        q = q.groupby("odor", sort=False).head(RANDOM_TRIALS).sort_values("onset").reset_index(drop=True)
        out["rnd_pres"] = q
        out["rnd"] = windows(s, q.onset.to_numpy(), *RANDOM_WINDOW)
    return out


# --- population measures -------------------------------------------------------------------

def median_subtracted(x: np.ndarray) -> np.ndarray:
    """frames x ROIs, minus the median across ROIs at each frame (the code's `medRsp`)."""
    return x - np.median(x, axis=1, keepdims=True)


def angles(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Angles in degrees between every row of a and every row of b."""
    an = a / np.linalg.norm(a, axis=1, keepdims=True)
    bn = b / np.linalg.norm(b, axis=1, keepdims=True)
    return np.degrees(np.arccos(np.clip(an @ bn.T, -1, 1)))


def onoff_angles(on: np.ndarray, off: np.ndarray, center: bool = True) -> dict:
    """Median angles ON-OFF, ON-ON and OFF-OFF between frame vectors (frames x ROIs).

    With `center`, vectors are centred over the ON and OFF frames together, as PCA scores are in
    the code; without it, they are taken as they are.
    """
    x = np.vstack([on, off])
    if center:
        x = x - x.mean(axis=0)
    a, b = x[:len(on)], x[len(on):]
    iu_a, iu_b = np.triu_indices(len(a), 1), np.triu_indices(len(b), 1)
    return {"on_off": float(np.median(angles(a, b))),
            "on_on": float(np.median(angles(a, a)[iu_a])),
            "off_off": float(np.median(angles(b, b)[iu_b]))}


def corr(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.corrcoef(a, b)[0, 1])


# --- classifiers ---------------------------------------------------------------------------

def _vote(neighbour_labels: np.ndarray) -> np.ndarray:
    """Most common label in each row; ties go to the lowest label (MATLAB `mode`)."""
    labels = np.unique(neighbour_labels)
    counts = np.stack([(neighbour_labels == lab).sum(axis=1) for lab in labels], axis=1)
    return labels[np.argmax(counts, axis=1)]


def knn_neighbours(x: np.ndarray, groups: np.ndarray, k: int, metric: str,
                   chunk: int = 1000) -> np.ndarray:
    """Indices of the k nearest rows of x for every row, never from the same group.

    metric 'correlation' is 1 - Pearson r between rows; 'cosine' is the angle between rows
    (ranked as 1 - cosine). Pass each row's own index as `groups` for leave-one-out.
    """
    x = np.asarray(x, dtype=np.float64)
    if metric == "correlation":
        x = x - x.mean(axis=1, keepdims=True)
    elif metric != "cosine":
        raise ValueError(metric)
    x = x / np.linalg.norm(x, axis=1, keepdims=True)
    out = np.empty((len(x), k), dtype=np.int64)
    for i in range(0, len(x), chunk):
        d = 1 - x[i:i + chunk] @ x.T
        d[groups[i:i + chunk, None] == groups[None, :]] = np.inf
        part = np.argpartition(d, k, axis=1)[:, :k]
        order = np.argsort(np.take_along_axis(d, part, axis=1), axis=1, kind="stable")
        out[i:i + chunk] = np.take_along_axis(part, order, axis=1)
    return out


def knn_predict(neighbours: np.ndarray, labels: np.ndarray) -> np.ndarray:
    return _vote(labels[neighbours])


def permuted_accuracy(neighbours: np.ndarray, labels: np.ndarray, trial_of_row: np.ndarray,
                      rng: np.random.Generator, n: int, by_bin: np.ndarray | None = None):
    """Null accuracies with the labels of whole trials permuted, neighbours kept.

    Returns an n-vector of overall accuracy, or n x bins when `by_bin` gives each row's bin.
    """
    trials = np.unique(trial_of_row)
    trial_label = np.array([labels[trial_of_row == tr][0] for tr in trials])
    pos = np.searchsorted(trials, trial_of_row)
    res = []
    for _ in range(n):
        perm = rng.permutation(trial_label)[pos]
        hit = knn_predict(neighbours, perm) == perm
        if by_bin is None:
            res.append(hit.mean())
        else:
            res.append([hit[by_bin == b].mean() for b in np.unique(by_bin)])
    return np.array(res)


# --- Figshare ------------------------------------------------------------------------------

def figshare_mat(name: str) -> dict:
    """A .mat file of the paper's Figshare record, read in memory and checked against its md5."""
    file_id, md5 = FIGSHARE_FILES[name]
    req = urllib.request.Request(f"https://ndownloader.figshare.com/files/{file_id}",
                                 headers={"User-Agent": "reproduction-registry"})
    for attempt in range(6):     # Figshare answers rapid requests with HTTP 500 or 429 for a while
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                raw = r.read()
            break
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503) or attempt == 5:
                raise
            time.sleep(10 * (attempt + 1))
    if hashlib.md5(raw).hexdigest() != md5:
        raise RuntimeError(f"{name}: md5 does not match the Figshare record")
    return sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)
