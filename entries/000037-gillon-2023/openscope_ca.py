"""Loading and measures for dandiset 000037 (OpenScope Credit Assignment).

Gillon, Lecoq et al. (2023), Scientific Data 10, 287, doi:10.1038/s41597-023-02214-y.

Each session is deposited three times: a basic file (`behavior+ophys`), one with the stimulus
frame images (`behavior+image+ophys`) and one with the motion corrected stack
(`obj-raw_behavior+image+ophys`). Only the basic files are opened here; the other two are only
listed (their sizes). Each basic file is streamed from the archive at the pinned version into
memory with parallel HTTP range requests (`stream_file`) and read with `h5py`; nothing is
written to disk.

Where the parameters come from:

- SNR and signal (`calculate_snr`): the Technical Validation and the paper's code,
  `math_util.calculate_snr` of https://github.com/colleenjg/util (commit
  2b05f954a4aa871dbfdd83d1546ebe8e7f3069c6), as the claims file's criterion
  fig7a-snr-above-1 gives it. Ported line for line.
- Smoothing (`rolling_mean`): a 4-point moving average with scipy.ndimage.convolve, mode
  mirror, as `math_util.rolling_mean` (criteria fig7c-correlations-similar and
  fig5-example-responses).
- Robust scaling ((x - median) / (95th - 5th percentile) over the session, per ROI): criteria
  fig5-example-responses and fig9-onset-offset-transients, from the paper's code.
- Windows: -0.9 to 0.6 s around D or U onset (Gabor), -2 to 2 s around inconsistent flow onset
  and around grey screen transitions: the criteria fig5-example-responses and
  fig9-onset-offset-transients (from the code's paper_organization.py).
- The selection rules of `select_gabor_rois` and `select_flow_rois` are those of the criterion
  fig5-example-responses (seq_analys.identify_gabor_roi_ns and identify_visflow_roi_ns of
  https://github.com/colleenjg/OpenScope_CA_Analysis at commit
  046e7fef5f452cdc0775fe54040b0f13aeae1e57).
- Standard choices that cannot change a result: a window of n seconds is taken as
  round(n * frame rate) two-photon frames from the reference frame given by the trial table's
  `start_frame_twop`; dF/F is held as float32 after loading; correlations are computed in
  float32.

Outside inputs, all pinned (fetched from GitHub at fixed commits):

- Supplementary Table 1 of the paper, as metadata.csv of
  https://github.com/jeromelecoq/allen_openscope_metadata (commit
  0e9c7aca3d67cbab7c493ab824b7287fb9508f47): Tables 1 and 2 with local session numbers and QC.
- The paper's repository (commit above): roi_tracking/nway-matched-dfs (union counts of the
  Fig. 8 examples) and paper_figures/dataset_paper/Fig7/data_files/panel_A.json (per-ROI SNRs).
"""

from __future__ import annotations

import io
import json
import threading
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests
import scipy.ndimage
import scipy.stats

DANDISET_ID = "000037"
DANDISET_VERSION = "0.230426.0054"
LATEST_VERSION = "0.240209.1623"
API = "https://api.dandiarchive.org/api"

OSCA_REPO = "colleenjg/OpenScope_CA_Analysis"
OSCA_COMMIT = "046e7fef5f452cdc0775fe54040b0f13aeae1e57"
META_REPO = "jeromelecoq/allen_openscope_metadata"
META_COMMIT = "0e9c7aca3d67cbab7c493ab824b7287fb9508f47"

SMOOTH_WIN = 4                       # 4-point moving average (criteria fig5, fig7c)
GABOR_PRE, GABOR_POST = 0.9, 0.6     # s around D or U onset (criterion fig5-example-responses)
FLOW_PRE, FLOW_POST = 2.0, 2.0       # s around inconsistent flow onset (same criterion)
TRANS_PRE, TRANS_POST = 2.0, 2.0     # s around grey screen transitions (fig9 criterion)

CONTENT = {"behavior+ophys": "B", "behavior+image+ophys": "I", "obj-raw_behavior+image+ophys": "S"}


# --- archive ------------------------------------------------------------------

def version_assets(version: str = DANDISET_VERSION) -> pd.DataFrame:
    """Every asset of a version: path, size, blob, subject, session and file version (B, I, S)."""
    rows, url = [], f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000"
    while url:
        page = requests.get(url, timeout=60).json()
        rows += page["results"]
        url = page["next"]
    df = pd.DataFrame(rows)[["asset_id", "path", "size", "blob"]]
    name = df.path.str.split("/").str[-1]
    parts = name.str.extract(r"sub-(\d+)_ses-(\d+)_(.+)\.nwb")
    df["subject"], df["session"], df["content"] = parts[0], parts[1], parts[2]
    df["kind"] = df.content.map(CONTENT)
    return df.sort_values("path").reset_index(drop=True)


def s3_url(asset_id: str, version: str = DANDISET_VERSION) -> str:
    """The S3 address of an asset, from its metadata."""
    meta = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/{asset_id}/",
                        timeout=60).json()
    return next(u for u in meta["contentUrl"] if "s3" in u)


def github_raw(repo: str, commit: str, path: str) -> bytes:
    r = requests.get(f"https://raw.githubusercontent.com/{repo}/{commit}/{path}", timeout=120)
    r.raise_for_status()
    return r.content


def supplementary_table() -> pd.DataFrame:
    """Supplementary Table 1 (metadata.csv at the pinned commit)."""
    raw = github_raw(META_REPO, META_COMMIT, "projects/credit_assignement/metadata.csv")
    return pd.read_csv(io.BytesIO(raw), dtype={"imaging_UTC_date_time": str, "imaging_date": str,
                                               "subject_date_of_birth": str})


def nway_example(subject: str, session: str) -> dict:
    path = f"roi_tracking/nway-matched-dfs/mouse_{subject}__session_{session}__nway_matched_rois.json"
    return json.loads(github_raw(OSCA_REPO, OSCA_COMMIT, path))


def fig7a_source() -> pd.DataFrame:
    raw = json.loads(github_raw(OSCA_REPO, OSCA_COMMIT,
                                "paper_figures/dataset_paper/Fig7/data_files/panel_A.json"))
    return pd.DataFrame({k: pd.Series(v) for k, v in raw["snr_df"].items()})


# --- one session --------------------------------------------------------------

def _text(value) -> str:
    value = value[()]
    return value.decode() if isinstance(value, bytes) else str(value)


TRIAL_COLUMNS = ["start_time", "stop_time", "stimulus_type", "stimulus_template_name", "unexpected",
                 "gabor_frame", "gabor_kappa", "gabor_mean_orientation", "gabor_number",
                 "main_flow_direction", "square_size", "square_number", "square_proportion_flipped",
                 "start_frame_twop", "stop_frame_twop", "start_frame_stim", "stop_frame_stim"]


def text_fields(f: h5py.File, max_size: int = 64) -> dict:
    """Every small dataset and attribute under `general`, and the file's top-level datasets and
    attributes (start time, creation date, reference time, descriptions), as text."""
    out = {}

    def as_text(v):
        v = v.decode() if isinstance(v, bytes) else v
        if isinstance(v, np.ndarray):
            v = [x.decode() if isinstance(x, bytes) else x for x in v.ravel()]
        return str(v)

    def add(path, obj):
        for k, v in obj.attrs.items():
            if k not in ("namespace", "neurodata_type", "object_id"):
                out[f"{path}@{k}"] = as_text(v)
        if isinstance(obj, h5py.Dataset) and obj.size <= max_size:
            out[path] = as_text(obj[()])

    for k in f.keys():
        if isinstance(f[k], h5py.Dataset):
            add(k, f[k])
    add("/", f)
    f["general"].visititems(lambda name, obj: add(f"general/{name}", obj))
    return out


def load_session(f: h5py.File, masks: bool = False) -> dict:
    """Metadata, trial table, tracking, running and pupil of one basic file (no dF/F).

    With `masks`, the centroid (row, column) of every tracked ROI's mask is read too.
    """
    g = f["general"]
    ps = f["processing/ophys/ImageSegmentation/PlaneSegmentation"]
    rrs = f["processing/ophys/DfOverF/RoiResponseSeries"]
    beh = f["processing/behavior"]
    trials = f["intervals/trials"]
    s = {
        "session_id": _text(g["session_id"]),
        "identifier": _text(f["identifier"]),
        "session_start_time": _text(f["session_start_time"]),
        "subject_id": _text(g["subject/subject_id"]),
        "sex": _text(g["subject/sex"]),
        "age": _text(g["subject/age"]),
        "genotype": _text(g["subject/genotype"]),
        "species": _text(g["subject/species"]),
        "subject_fields": sorted(g["subject"].keys()),
        "location": _text(g["optophysiology/ImagingPlane/location"]),
        "imaging_rate": float(g["optophysiology/ImagingPlane/imaging_rate"][()]),
        "indicator": _text(g["optophysiology/ImagingPlane/indicator"]),
        "excitation_lambda": float(g["optophysiology/ImagingPlane/excitation_lambda"][()]),
        "dff_shape": rrs["data"].shape,
        "dff_unit": rrs["data"].attrs.get("unit"),
        "dff_storage": (rrs["data"].chunks, rrs["data"].compression),
        "mask_shape": ps["image_mask"].shape,
        "max_projection_shape": f["processing/ophys/PlaneImages/max_projection"].shape,
        "tracking_id": ps["tracking_id"][:] if "tracking_id" in ps else np.full(ps["id"].shape, np.nan),
        "dff_t": rrs["timestamps"][:],
        "run_v": beh["BehavioralTimeSeries/running_velocity/data"][:],
        "run_t": beh["BehavioralTimeSeries/running_velocity/timestamps"][:],
        "run_unit": beh["BehavioralTimeSeries/running_velocity/data"].attrs.get("unit"),
        "pupil_d": beh["PupilTracking/pupil_diameter/data"][:],
        "pupil_t": beh["PupilTracking/pupil_diameter/timestamps"][:],
        "pupil_unit": beh["PupilTracking/pupil_diameter/data"].attrs.get("unit"),
        "pupil_x": beh["PupilTracking/pupil_position_x/data"][:],
        "pupil_y": beh["PupilTracking/pupil_position_y/data"][:],
        "pupil_x_unit": beh["PupilTracking/pupil_position_x/data"].attrs.get("unit"),
        "trial_columns": sorted(trials.keys()),
        "text_fields": text_fields(f),
    }
    t = {}
    for c in TRIAL_COLUMNS:
        v = trials[c][:]
        t[c] = np.array([x.decode() if isinstance(x, bytes) else x for x in v]) if v.dtype == object else v
    s["trials"] = pd.DataFrame(t)
    # Gabor patches per image, from the per-patch orientation index.
    idx = trials["gabor_orientations_index"][:]
    s["trials"]["n_patches"] = np.diff(np.concatenate([[0], idx]))
    # Square positions of the first consistent and first inconsistent flow trials.
    sq_idx = trials["square_locations_x_index"][:]
    tt = s["trials"]
    first = {}
    for name, sel in (("consistent", (tt.stimulus_type == "visflow") & (tt.unexpected == 0)),
                      ("inconsistent", (tt.stimulus_type == "visflow") & (tt.unexpected == 1))):
        i = int(np.flatnonzero(sel.values)[0])
        lo = int(sq_idx[i - 1]) if i > 0 else 0
        first[name] = (trials["square_locations_x"][lo:int(sq_idx[i])],
                       trials["square_locations_y"][lo:int(sq_idx[i])],
                       tt.main_flow_direction.iloc[i])
    s["squares"] = first
    if masks:
        tracked = np.flatnonzero(np.isfinite(s["tracking_id"]))
        cents = mask_centroids(f, tracked)
        cents.index = s["tracking_id"][tracked].astype(int)
        s["tracked_centroids"] = cents.sort_index()
    return s


# --- measures -----------------------------------------------------------------

def calculate_snr(data):
    """Port of util math_util.calculate_snr: (snr, noise_thr, signal_mean, noise_std)."""
    data = np.asarray(data, dtype=float).reshape(-1)
    data_median = np.median(data)
    lower = data[data <= data_median]
    noise = np.concatenate([lower, 2 * data_median - lower])
    noise_mean, noise_std = np.mean(noise), np.std(noise)
    noise_thr = scipy.stats.norm.ppf(0.95, noise_mean, noise_std)
    signal_mean = np.mean(data[data > noise_thr])
    return signal_mean / noise_std, noise_thr, signal_mean, noise_std


def rolling_mean(vals, win=SMOOTH_WIN):
    """Port of util math_util.rolling_mean: moving average over the last axis, mode mirror."""
    weights = (np.repeat(1.0, win) / win).reshape(tuple([1] * (vals.ndim - 1) + [win]))
    return scipy.ndimage.convolve(vals, weights.astype(vals.dtype), mode="mirror")


def robust_scale(x):
    """(x - median) / (95th - 5th percentile), per row (ROI), over the session."""
    med = np.median(x, axis=1, keepdims=True)
    p5, p95 = np.percentile(x, [5, 95], axis=1, keepdims=True)
    return (x - med) / (p95 - p5)


def windows(x, refs, pre_n, post_n):
    """ROIs x events x frames, for frames ref - pre_n to ref + post_n (excluded); events whose
    window leaves the recording are dropped."""
    refs = np.asarray(refs, dtype=int)
    keep = (refs - pre_n >= 0) & (refs + post_n <= x.shape[1])
    idx = refs[keep][:, None] + np.arange(-pre_n, post_n)[None, :]
    return x[:, idx], int((~keep).sum())


def median_pairwise_corr(tr):
    """Per ROI, the median correlation between its individual (event) traces; tr: ROIs x events x frames."""
    n = tr.shape[1]
    iu = np.triu_indices(n, k=1)
    out = np.empty(tr.shape[0])
    for i, roi in enumerate(tr):
        out[i] = np.median(np.corrcoef(roi)[iu])
    return out


def select_gabor_rois(tr, snr_above, thresholds=None):
    """Criterion fig5-example-responses (Gabor): among ROIs with SNR above the session median,
    those whose median pairwise sequence correlation (smoothed sequences), and the standard
    deviation and skew of their mean response, all exceed the 75th percentile of those ROIs.
    A dict passed as `thresholds` receives the candidate count and the three percentiles."""
    cand = np.flatnonzero(snr_above)
    sub = tr[cand]
    mean_tr = sub.mean(axis=1)
    stds, skews = mean_tr.std(axis=1), scipy.stats.skew(mean_tr, axis=1)
    corrs = median_pairwise_corr(rolling_mean(sub))
    ok = ((stds > np.percentile(stds, 75)) & (skews > np.percentile(skews, 75))
          & (corrs > np.percentile(corrs, 75)))
    if thresholds is not None:
        thresholds.update(candidates=len(cand), std_p75=np.percentile(stds, 75),
                          skew_p75=np.percentile(skews, 75), corr_p75=np.percentile(corrs, 75))
    return cand[ok]


def select_flow_rois(tr, pre_n, snr_above, thresholds=None):
    """Criterion fig5-example-responses (flow): among ROIs above the median SNR, those whose median
    pairwise correlation of post-onset responses and mean post-minus-pre difference both exceed
    the 75th percentile. A dict passed as `thresholds` receives the candidate count and the two
    percentiles."""
    cand = np.flatnonzero(snr_above)
    sub = tr[cand]
    diffs = (sub[..., pre_n:].mean(axis=2) - sub[..., :pre_n].mean(axis=2)).mean(axis=1)
    corrs = median_pairwise_corr(rolling_mean(sub)[..., pre_n:])
    ok = (diffs > np.percentile(diffs, 75)) & (corrs > np.percentile(corrs, 75))
    if thresholds is not None:
        thresholds.update(candidates=len(cand), diff_p75=np.percentile(diffs, 75),
                          corr_p75=np.percentile(corrs, 75))
    return cand[ok]


RANGE_STEP = 32 * 2**20


def _get_range(url: str, start: int, stop: int) -> bytes:
    """Bytes start to stop (excluded) of a file, by an HTTP range request."""
    for attempt in range(5):
        try:
            r = requests.get(url, headers={"Range": f"bytes={start}-{stop - 1}"}, timeout=300)
            r.raise_for_status()
            if len(r.content) == stop - start:
                return r.content
        except requests.RequestException:
            if attempt == 4:
                raise
    raise IOError(f"short read of {url} at {start}")


class MemoryFile(io.RawIOBase):
    """A read-only file object over a byte buffer held in memory, for h5py."""

    def __init__(self, buf: np.ndarray):
        self.buf, self.pos = buf, 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        self.pos = offset if whence == 0 else self.pos + offset if whence == 1 else len(self.buf) + offset
        return self.pos

    def tell(self):
        return self.pos

    def readinto(self, b):
        n = max(0, min(len(b), len(self.buf) - self.pos))
        memoryview(b).cast("B")[:n] = self.buf[self.pos:self.pos + n]
        self.pos += n
        return n


def stream_file(url: str, threads: int = 16) -> h5py.File:
    """Stream a whole NWB file into memory with parallel HTTP range requests, and open it.

    Nothing is written to disk. The dF/F of the dendritic files is stored gzip-chunked, and
    reading it through remfile and h5py is slow (the chunk index is spread through the file);
    one streamed copy in memory is read in seconds, and holds everything else used here too.
    """
    size = int(requests.head(url, timeout=60).headers["Content-Length"])
    buf = np.empty(size, dtype=np.uint8)

    def fill(start):
        stop = min(start + RANGE_STEP, size)
        buf[start:stop] = np.frombuffer(_get_range(url, start, stop), dtype=np.uint8)

    with ThreadPoolExecutor(threads) as ex:
        list(ex.map(fill, range(0, size, RANGE_STEP)))
    return h5py.File(MemoryFile(buf), "r")


def read_dff(f: h5py.File, block: int = 16384) -> np.ndarray:
    """dF/F as ROIs x frames, float32."""
    d = f["processing/ophys/DfOverF/RoiResponseSeries/data"]
    out = np.empty(d.shape[::-1], dtype=np.float32)
    for i in range(0, d.shape[0], block):
        out[:, i:i + block] = d[i:i + block].T
    return out


def mask_centroids(f: h5py.File, rois) -> pd.DataFrame:
    """Weighted centroid (row, column) of the masks of the given ROIs."""
    rows = []
    for i in rois:
        m = f["processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask"][int(i)]
        r, c = np.nonzero(m)
        w = m[r, c].astype(float)
        rows.append((np.sum(r * w) / w.sum(), np.sum(c * w) / w.sum()))
    return pd.DataFrame(rows, columns=["row", "col"], index=[int(i) for i in rois])


def grey_transitions(trials: pd.DataFrame) -> pd.DataFrame:
    """Onsets (ends of every grey period but the last) and offsets (starts of every grey period
    but the first), as in basic_analys.get_stim_on_off_data, with the stimulus on the other side."""
    t = trials.reset_index(drop=True)
    grey = t.index[t.stimulus_type == "grayscreen"].to_numpy()
    rows = []
    for g in grey[:-1]:
        rows.append({"kind": "onset", "frame": int(t.stop_frame_twop[g]),
                     "time": float(t.stop_time[g]), "stimulus": t.stimulus_template_name[g + 1]})
    for g in grey[1:]:
        rows.append({"kind": "offset", "frame": int(t.start_frame_twop[g]),
                     "time": float(t.start_time[g]), "stimulus": t.stimulus_template_name[g - 1]})
    return pd.DataFrame(rows)


def flow_onsets(trials: pd.DataFrame, direction: str) -> np.ndarray:
    """Two-photon frames of inconsistent flow onsets (first reversed trial of each run) for one
    direction ("right" or "left")."""
    t = trials[(trials.stimulus_type == "visflow")
               & trials.main_flow_direction.str.startswith(direction)].reset_index(drop=True)
    u = t.unexpected.to_numpy() == 1
    start = u & ~np.concatenate([[False], u[:-1]])
    return t.start_frame_twop.to_numpy()[start]


def process_session(s: dict, f: h5py.File, corr: bool = False, fig5: bool = False) -> dict:
    """Read one session's dF/F and reduce it to what the claims use.

    Always: per-ROI mean, median, min, max, SNR and signal (unscaled dF/F); the population mean
    of the robust-scaled traces (for the clock check); per-ROI traces around each grey screen
    transition, robust-scaled and unscaled. With `corr`: the upper triangle of the ROI x ROI
    Pearson correlations of the smoothed full traces. With `fig5`: per-ROI mean traces around D
    and U onsets and inconsistent flow onsets, and the ROIs each selection keeps.
    """
    x = read_dff(f)
    fps = 1.0 / np.median(np.diff(s["dff_t"]))
    out = {"session_id": s["session_id"], "fps": fps, "n_rois": x.shape[0]}
    snr = np.array([calculate_snr(r) for r in x])
    out["roi"] = pd.DataFrame({
        "mean": x.mean(axis=1, dtype=np.float64), "median": np.median(x, axis=1),
        "min": x.min(axis=1), "max": x.max(axis=1),
        "snr": snr[:, 0], "noise_thr": snr[:, 1], "signal": snr[:, 2],
        "tracking_id": s["tracking_id"]})
    xs = robust_scale(x)
    out["popmean_scaled"] = xs.mean(axis=0)
    tr = grey_transitions(s["trials"])
    pre, post = int(round(TRANS_PRE * fps)), int(round(TRANS_POST * fps))
    out["transitions"] = tr
    out["trans_scaled"], dropped = windows(xs, tr.frame, pre, post)  # ROIs x transitions x frames
    out["trans_unscaled"], _ = windows(x, tr.frame, pre, post)
    # Rows of `transitions` index the windows, so no transition may be dropped.
    assert dropped == 0, f"{s['session_id']}: {dropped} grey screen transitions leave the recording"
    out["trans_t"] = np.arange(-pre, post) / fps

    if fig5:
        trials = s["trials"]
        snr_above = snr[:, 0] > np.median(snr[:, 0])
        f5 = {"snr_above": snr_above}
        g_pre, g_post = int(round(GABOR_PRE * fps)), int(round(GABOR_POST * fps))
        f5["gabor_t"] = np.arange(-g_pre, g_post) / fps
        refs = {"D": trials.start_frame_twop[(trials.gabor_frame == "D") & (trials.unexpected == 0)],
                "U": trials.start_frame_twop[trials.gabor_frame == "U"]}
        for scaled, data in (("scaled", xs), ("unscaled", x)):
            for k, r in refs.items():
                w, dropped = windows(data, r, g_pre, g_post)
                f5[f"gabor_{k}_{scaled}_mean"] = w.mean(axis=1)
                f5[f"gabor_{k}_n"] = w.shape[1]
                f5[f"gabor_{k}_dropped"] = dropped
                f5[f"gabor_{k}_{scaled}_thr"] = {}
                f5[f"gabor_{k}_{scaled}_sel"] = select_gabor_rois(w, snr_above, f5[f"gabor_{k}_{scaled}_thr"])
        fl_pre, fl_post = int(round(FLOW_PRE * fps)), int(round(FLOW_POST * fps))
        f5["flow_t"] = np.arange(-fl_pre, fl_post) / fps
        for direction in ("right", "left"):
            r = flow_onsets(trials, direction)
            for scaled, data in (("scaled", xs), ("unscaled", x)):
                w, dropped = windows(data, r, fl_pre, fl_post)
                f5[f"flow_{direction}_{scaled}_mean"] = w.mean(axis=1)
                f5[f"flow_{direction}_n"] = w.shape[1]
                f5[f"flow_{direction}_dropped"] = dropped
                f5[f"flow_{direction}_{scaled}_thr"] = {}
                f5[f"flow_{direction}_{scaled}_sel"] = select_flow_rois(w, fl_pre, snr_above,
                                                                         f5[f"flow_{direction}_{scaled}_thr"])
        out["fig5"] = f5
    del xs
    if corr:
        sm = rolling_mean(x)
        del x
        sm -= sm.mean(axis=1, keepdims=True)
        sm /= np.linalg.norm(sm, axis=1, keepdims=True)
        c = sm @ sm.T
        out["corr"] = c[np.triu_indices(c.shape[0], k=1)].astype(np.float32)
    return out


def analyse(url: str, masks: bool = False, corr: bool = False, fig5: bool = False):
    """Stream one basic file into memory once; return (load_session, process_session) for it."""
    with stream_file(url) as f:
        s = load_session(f, masks=masks)
        return s, process_session(s, f, corr=corr, fig5=fig5)


def run_parallel(fn, items, weights=None, workers=4, budget=None):
    """fn over items in threads. With `weights` and `budget`, items run only while the sum of
    the weights in flight stays within the budget (one item always runs), to bound memory."""
    if weights is None or budget is None:
        with ThreadPoolExecutor(workers) as ex:
            return list(ex.map(fn, items))
    cond, state = threading.Condition(), {"used": 0, "running": 0}

    def guarded(pair):
        item, w = pair
        with cond:
            cond.wait_for(lambda: state["running"] == 0 or state["used"] + w <= budget)
            state["used"] += w
            state["running"] += 1
        try:
            return fn(item)
        finally:
            with cond:
                state["used"] -= w
                state["running"] -= 1
                cond.notify_all()

    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(guarded, zip(items, weights)))


def github_listing(repo: str, commit: str, path: str) -> list[str]:
    """File names in a directory of a repository at a commit (GitHub contents API)."""
    r = requests.get(f"https://api.github.com/repos/{repo}/contents/{path}?ref={commit}", timeout=60)
    r.raise_for_status()
    return sorted(x["name"] for x in r.json())
