"""Loading and measures for dandiset 000718 (Zaki et al., Nature 2024, doi:10.1038/s41586-024-08168-4).

The dandiset holds two mice of the paper's calcium imaging and EEG/EMG experiment (Figure 5):
Ca_EEG2-1 (1.5 mA, high shock) and Ca_EEG3-4 (0.25 mA, low shock). Each session file holds the
Minian output of one Miniscope recording (deconvolved activity `S`, 15 Hz after the 2x temporal
downsampling of the Methods, and ROI centroids), and, by session type, ezTrack freezing intervals
and motion (behaviour sessions), shock times (FC), telemetry signals at 500 Hz and 6 s sleep-state
intervals (offline sessions). The `Week` file of Ca_EEG2-1 holds a week of telemetry, an epoch table
of all sessions, and the CellReg tables that map each offline-day-2 recording's ROIs to the encoding
and recall sessions (-9999 for no match). Files are streamed from the archive at the pinned version;
nothing is written to disk.

Where the parameters come from (the analysis code the paper names,
github.com/denisecailab/RetrospectiveMemoryLinkingAnalysis_2024, is not public):

- Burst detection, participation and co-participation follow the Methods ("Burst participation
  analysis", "Ensemble co-participation analysis"): each cell z-scored over time; the mean over
  cells z-scored again; frames above `BURST_Z` = 2 form burst events (maximal runs of such frames,
  a common reading of "time periods when the mean population activity reached above a threshold");
  a cell or ensemble participates when its z-scored activity exceeds 2 at any frame of the event.
- Ensembles of an offline cell follow the Methods ("Ensemble reactivation analysis"): matched by
  CellReg to neutral encoding only (neutral), FC only (aversive), both (overlap), or neither
  (remaining). A match to Recall1 alone does not count, as recall comes after the offline period.
- Surrogates circularly shift each cell's trace by an independent random offset, as in Extended
  Data Figure 3l; `N_SHUFFLES` = 1000 as there.
- Freezing is the share of the 30 Hz ezTrack motion frames inside the deposited freezing intervals
  (the intervals' own parameters are in their description).
- Movement in offline recordings is the magnitude of the telemetry ActivitySignal averaged in
  `MOVE_BIN_S` bins (a choice made here; the paper used a webcam the dandiset does not hold).
"""

from __future__ import annotations

from functools import lru_cache

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "000718"
DANDISET_VERSION = "0.260825.1902"

MICE = ["Ca_EEG2-1", "Ca_EEG3-4"]
BURST_Z = 2.0
N_SHUFFLES = 1000
MOVE_BIN_S = 0.1
REGISTRATION_TABLE = "OfflineDay2Session1vsConditioningSessions"


@lru_cache(maxsize=None)
def asset_urls() -> dict[str, str]:
    """Path -> streaming URL of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)
                for a in dandiset.get_assets() if a.path.endswith(".nwb")}


def session_path(mouse: str, session: str) -> str:
    sub = "sub-" + mouse.replace("_", "-")
    kind = "_ophys" if session.startswith("Offline") else ("" if session == "Week" else "_image+ophys")
    return f"{sub}/{sub}_ses-{session}{kind}.nwb"


def open_nwb(path: str) -> h5py.File:
    return h5py.File(remfile.File(asset_urls()[path]), "r")


def _text(x) -> str:
    x = x[()] if hasattr(x, "shape") else x
    return x.decode() if isinstance(x, bytes) else str(x)


def load_session(path: str) -> dict:
    """Everything a session file holds that the analyses use, reduced as it loads."""
    f = open_nwb(path)
    out = {"path": path, "session_id": _text(f["general/session_id"]),
           "subject_id": _text(f["general/subject/subject_id"]),
           "species": _text(f["general/subject/species"]), "sex": _text(f["general/subject/sex"]),
           "age": _text(f["general/subject/age"]), "strain": _text(f["general/subject/strain"]),
           "start": _text(f["session_start_time"]), "description": _text(f["session_description"])}
    dec = f["processing/ophys/Fluorescence/Deconvolved"]
    out["S"] = dec["data"][:].astype(np.float32)
    out["t"] = dec["timestamps"][:]
    out["S_unit"] = _text(dec["data"].attrs["unit"])
    out["centroids"] = f["processing/ophys/ImageSegmentation/PlaneSegmentation/ROICentroids"][:].astype(float)
    out["roi_ids"] = f["processing/ophys/ImageSegmentation/PlaneSegmentation/id"][:]
    ops = f["acquisition/OnePhotonSeries/timestamps"][:]
    out["ops_n"], out["ops_last"], out["ops_dt"] = len(ops), float(ops[-1]), float(np.median(np.diff(ops)))
    out["max_proj"] = f["processing/ophys/SegmentationImages/maximum_projection"][:]
    if "processing/behavior" in f:
        m = f["processing/behavior/MotionSeries"]
        motion = m["data"][:]
        out["motion"] = motion
        out["motion_t"] = m["starting_time"][()] + np.arange(len(motion)) / m["starting_time"].attrs["rate"]
        g = f["processing/behavior/FreezingIntervals"]
        out["freeze"] = np.column_stack([g["start_time"][:], g["stop_time"][:]])
        out["freeze_description"] = _text(g.attrs["description"]).strip()
    if "stimulus/presentation/ShockStimuli" in f:
        g = f["stimulus/presentation/ShockStimuli"]
        out["shocks"] = np.column_stack([g["start_time"][:], g["stop_time"][:]])
        out["shock_amplitude"] = g["shock_amplitude"][:]
    if "processing/sleep/SleepIntervals" in f:
        g = f["processing/sleep/SleepIntervals"]
        out["sleep"] = (g["start_time"][:], g["stop_time"][:],
                        np.array([_text(s) for s in g["sleep_state"][:]]))
    if "acquisition/ActivitySignal" in f:
        a = f["acquisition/ActivitySignal"]
        out["activity"] = a["data"][:]
        out["activity_t0"] = float(a["starting_time"][()])
        out["activity_rate"] = float(a["starting_time"].attrs["rate"])
        out["eeg_head"] = f["acquisition/EEGSignal/data"][:5000]
    return out


def load_week(mouse: str = "Ca_EEG2-1") -> dict:
    """Epoch table and the registration table of offline-day-2 session 1."""
    f = open_nwb(session_path(mouse, "Week"))
    e = f["intervals/epochs"]
    epochs = {_text(s): (a, b) for s, a, b in zip(e["session_ids"][:], e["start_time"][:], e["stop_time"][:])}
    t = f[f"processing/cell_registration/{REGISTRATION_TABLE}"]
    reg = {_text(k).replace(mouse + "_", ""): t[_text(k)][:] for k in t.attrs["colnames"]}
    tables = sorted(f["processing/cell_registration"].keys())
    return {"epochs": epochs, "registration": reg, "tables": tables, "start": _text(f["session_start_time"]),
            "eeg_rate": float(f["acquisition/EEGSignal/starting_time"].attrs["rate"]),
            "eeg_n": f["acquisition/EEGSignal/data"].shape[0]}


def week_signal(t0: float, t1: float, channel: str = "EEGSignal", mouse: str = "Ca_EEG2-1") -> np.ndarray:
    """A window of a week-long telemetry channel, in seconds of the Week file's clock."""
    f = open_nwb(session_path(mouse, "Week"))
    d = f[f"acquisition/{channel}"]
    rate = d["starting_time"].attrs["rate"]
    return d["data"][int(t0 * rate):int(t1 * rate)]


# --- behaviour ------------------------------------------------------------------------------

def in_intervals(t: np.ndarray, intervals: np.ndarray) -> np.ndarray:
    inside = np.zeros(len(t), bool)
    for a, b in intervals:
        inside |= (t >= a) & (t <= b)
    return inside


def freezing_percent(s: dict) -> tuple[float, float]:
    """(a) % of motion frames inside a freezing interval, (b) summed interval time / motion span."""
    a = 100 * in_intervals(s["motion_t"], s["freeze"]).mean()
    span = s["motion_t"][-1] - s["motion_t"][0]
    b = 100 * np.sum(s["freeze"][:, 1] - s["freeze"][:, 0]) / span
    return a, b


def binned_freezing(s: dict, bin_s: float = 30.0) -> np.ndarray:
    inside = in_intervals(s["motion_t"], s["freeze"])
    edges = np.arange(0, s["motion_t"][-1] + 1e-9, bin_s)
    return np.array([100 * inside[(s["motion_t"] >= a) & (s["motion_t"] < a + bin_s)].mean()
                     for a in edges if (s["motion_t"] >= a + bin_s - 1).any()])


# --- calcium --------------------------------------------------------------------------------

def zscore_cells(S: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Each cell z-scored over time; cells with no activity are left out (mask returned)."""
    sd = S.std(0)
    keep = sd > 0
    Z = (S[:, keep] - S[:, keep].mean(0)) / sd[keep]
    return Z.astype(np.float32), keep


def zscore(x: np.ndarray) -> np.ndarray:
    return (x - x.mean()) / x.std()


def burst_events(trace: np.ndarray, thr: float = BURST_Z, merge: int = 0) -> np.ndarray:
    """(start, stop) frame indices, stop exclusive, of maximal runs of frames above thr.

    With merge > 0, runs separated by fewer than `merge` frames are joined (a variant).
    """
    above = np.concatenate([[False], trace > thr, [False]])
    d = np.diff(above.astype(int))
    ev = np.column_stack([np.where(d == 1)[0], np.where(d == -1)[0]])
    if merge and len(ev) > 1:
        keep = [list(ev[0])]
        for a, b in ev[1:]:
            if a - keep[-1][1] < merge:
                keep[-1][1] = b
            else:
                keep.append([a, b])
        ev = np.array(keep)
    return ev


def event_peaks(trace: np.ndarray, events: np.ndarray) -> np.ndarray:
    return np.array([a + int(np.argmax(trace[a:b])) for a, b in events], dtype=int)


def participates(Zsub: np.ndarray, events: np.ndarray, thr: float = BURST_Z) -> np.ndarray:
    """Boolean (events x columns): column above thr at any frame of the event."""
    return np.array([(Zsub[a:b] > thr).any(0) for a, b in events]).reshape(len(events), -1)


def population(Z: np.ndarray) -> np.ndarray:
    return zscore(Z.mean(1))


def shuffle_surrogates(Z: np.ndarray, n: int, rng: np.random.Generator, duration_min: float,
                       thr: float = BURST_Z, fixed: float | None = None, merge: int = 0) -> tuple[np.ndarray, np.ndarray]:
    """Burst frequency (per min) and skew of the population trace for n circular-shift surrogates.

    Each surrogate trace is z-scored and thresholded at thr, as the data; with `fixed`, the
    unscaled surrogate mean is thresholded at that value instead (a variant).

    Uses that deconvolved activity is mostly zero: a z-scored cell equals its floor value c_j
    except at its active frames, so the shifted mean is a constant plus a bincount of those frames.
    """
    T, N = Z.shape
    floor = Z.min(0)
    rows, cols = np.nonzero(Z > floor + 1e-6)
    vals = (Z[rows, cols] - floor[cols]).astype(np.float64)
    base = floor.sum()
    freq, skew = np.empty(n), np.empty(n)
    for i in range(n):
        k = rng.integers(0, T, N)
        m = (base + np.bincount((rows + k[cols]) % T, weights=vals, minlength=T)) / N
        p = zscore(m)
        freq[i] = len(burst_events(p if fixed is None else m, thr if fixed is None else fixed, merge)) / duration_min
        skew[i] = stats.skew(p)
    return freq, skew


def ensembles(reg: dict, offline_col: str, n_offline: int) -> np.ndarray:
    """Label of each offline ROI: neutral, aversive, overlap or remaining."""
    labels = np.full(n_offline, "remaining", dtype=object)
    off = reg[offline_col]
    for row in np.where(off >= 0)[0]:
        ne, fc = reg["NeutralExposure"][row] >= 0, reg["FC"][row] >= 0
        labels[off[row]] = "overlap" if ne and fc else "neutral" if ne else "aversive" if fc else "remaining"
    return labels


def state_of_frames(t: np.ndarray, sleep: tuple) -> np.ndarray:
    """Sleep state of each calcium frame from the 6 s intervals ('none' outside every interval)."""
    st, sp, lab = sleep
    out = np.full(len(t), "none", dtype=object)
    for a, b, s in zip(st, sp, lab):
        out[(t >= a) & (t < b + 0.1)] = s
    return out


def movement(s: dict, bin_s: float = MOVE_BIN_S) -> tuple[np.ndarray, np.ndarray]:
    """|ActivitySignal| averaged in bins; returns (bin centre times, values)."""
    a = np.abs(s["activity"])
    k = int(round(bin_s * s["activity_rate"]))
    n = len(a) // k
    v = a[:n * k].reshape(n, k).mean(1)
    return s["activity_t0"] + (np.arange(n) + 0.5) * bin_s, v


def window_mean(t: np.ndarray, v: np.ndarray, centres: np.ndarray, lo: float, hi: float) -> np.ndarray:
    """Mean of v in [c+lo, c+hi) for each centre; NaN when the window leaves the recording."""
    out = np.full(len(centres), np.nan)
    for i, c in enumerate(centres):
        if c + lo >= t[0] and c + hi <= t[-1]:
            out[i] = v[(t >= c + lo) & (t < c + hi)].mean()
    return out


def bin_matrix(S: np.ndarray, t: np.ndarray, edges: np.ndarray) -> np.ndarray:
    idx = np.searchsorted(edges, t, side="right") - 1
    ok = (idx >= 0) & (idx < len(edges) - 1)
    X = np.zeros((len(edges) - 1, S.shape[1]))
    np.add.at(X, idx[ok], S[ok])
    counts = np.bincount(idx[ok], minlength=len(edges) - 1)[:, None]
    return X / np.maximum(counts, 1)


def shift_decoding(S: np.ndarray, t: np.ndarray, y: np.ndarray, ty: np.ndarray, shifts_s, bin_s: float = 1.0,
                   folds: int = 5, alpha: float = 1e3) -> dict:
    """Cross-validated ridge decoding of y from binned activity, with y shifted in time.

    Returns the correlation of predicted and true y for each shift (s). Contiguous folds.
    """
    edges = np.arange(max(t[0], ty[0]), min(t[-1], ty[-1]), bin_s)
    X = bin_matrix(S, t, edges)
    Y = bin_matrix(y[:, None], ty, edges)[:, 0]
    X = (X - X.mean(0)) / (X.std(0) + 1e-9)
    n = len(Y)
    parts = np.array_split(np.arange(n), folds)
    out = {}
    for sh in shifts_s:
        Ys = np.roll(Y, int(round(sh / bin_s)))
        pred = np.zeros(n)
        for test in parts:
            train = np.setdiff1d(np.arange(n), test)
            Xt, yt = X[train], Ys[train] - Ys[train].mean()
            w = np.linalg.solve(Xt.T @ Xt + alpha * np.eye(X.shape[1]), Xt.T @ yt)
            pred[test] = X[test] @ w + Ys[train].mean()
        out[sh] = float(np.corrcoef(pred, Ys)[0, 1])
    return out
