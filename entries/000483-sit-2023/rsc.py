"""Loading and measures for dandiset 000483 (Sit & Goard 2023, Nat Commun 14:1992).

Each NWB file is one two-photon recording of retrosplenial cortex (somata) or of axon
terminals in it, made in a floating chamber (Neurotar). Each file holds the raw two-photon
video (not read here), the raw fluorescence of each ROI (`raw-fluorescence`, frames x ROIs, at
10 Hz), the ROI masks, and the chamber heading (degrees) and position (mm), one sample per
imaging frame. No neuropil trace, dF/F or inferred spikes are stored. The kind of experiment is
given only by the file's `identifier` (for example `..._DualCue_3rpm_SKKS088-DualCue-001`).
Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from ("claims" is claims/000483/10.1038-s41467-023-37704-5.yaml; "code"
is github.com/ucsb-goard-lab/Neurotar-HD-Experiments at commit c6344f5):

- dF/F = (F - F0)/F0 with F0 the mode of the fluorescence density (Methods, eq. 2). The Methods
  subtract a neuropil trace first (eq. 1); the dataset holds none, so F is used as it is
  (deviation). The mode is the peak of a Gaussian kernel density with
  Silverman's bandwidth, computed on a 1024-bin histogram (a standard choice).
- Inferred spikes: OASIS with an AR(1) kernel on dF/F (Methods, Analysis of calcium data), with
  its parameters estimated from the trace, as the call left in Cue.m
  (deconvolveCa(dff, 'ar1', 'foopsi', 'optimize_pars')) does (claims, opening comment). The
  Python port of OASIS (package oasis-deconv, `deconvolve`, penalty 1, g and noise optimised) is
  used in place of the MATLAB one.
- Heading clean-up and trials: code ControlledRotation.getTrialResponses (claims, opening
  comment): steps of 20 to 350 degrees replaced by the previous value (up to 10 passes); breaks
  at the wraps of heading and at rests (more than 20 consecutive frames with a change under 0.5
  degree); segments under 50 frames dropped, and segments whose 25th or 75th heading percentile
  lies more than 50 degrees from +-90 dropped. Wraps are found as the code finds them: peaks of
  the distance from the first heading within 10 degrees of its maximum (scipy's find_peaks in
  place of MATLAB's findpeaks).
- Tuning curves: 60 bins of 6 degrees over -180 to 180 (code Cue.binData), mean activity per bin,
  then a 15 degree moving average (Methods), here a circular 3-bin mean (18 degrees; the code's
  movmean of 15/6 bins has no integer width, a standard choice).
- Light and dark segments: code Separator.m with RSCSomaDualExperiment and AxonExperiment
  (claims, opening comment): 1950-frame recordings, one repeat of 950-frame segments; 7550-frame
  recordings, three repeats; 15050-frame recordings, six repeats, of 1250-frame segments; each
  repeat a light segment then a dark one.
- Heading-selection test: code ControlledRotation.calculateHeadDirection with 1000 iterations
  (claims, opening comment; Methods): split-half correlations of real and circularly shifted
  trials (same split), two-sample KS p < 0.1 and Cohen's d > 0.8; the real trial-mean curve,
  min-max rescaled, fitted with a Gaussian (one or two terms) with the code's start points and
  bounds must have r2 above the 90th percentile of the r2 of the 1000 shuffled trial means, and
  amplitude a1 > 0. The fit is a bounded Levenberg-Marquardt in numpy in place of MATLAB's
  `fit`. The code fits the curve as it is, without centring its peak (`center_flag` false);
  `center=True` gives the variant in which the peak is first shifted to bin 15, as the code's
  'fit' preferred direction and its older fits do.
- Cross-validated alignment: for each trial, the peak of the mean of the other trials sets the
  circular shift that puts that peak at bin 15 (claims, opening comment; Methods).
- Flip score: code Cue.calculateFlipScore (Methods, eq. 5): circular autocorrelation of the
  tuning curve smoothed with MATLAB's smoothdata default (a moving mean whose width is a quarter
  of the curve's length, here 15 bins), CC at 180 minus the mean of CC at 90 and 270 degrees.
- V-test: circ_vtest of the Circular Statistics Toolbox (Methods, Statistical information).
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats
from scipy.signal import find_peaks

DANDISET_ID = "000483"
DANDISET_VERSION = "0.230421.2321"

N_BINS = 60
BIN_WIDTH = 6
N_ITER = 1000
X = np.linspace(0, 2 * np.pi, N_BINS)
SHIFT_POINT = 14          # bin 15 in MATLAB's 1-based index
FLUOR = "processing/ophys/Fluorescence/raw-fluorescence/data"
HEADING = "processing/neurotar-data/floating cage orientation/heading-spatial-series/data"
POSITION = "processing/neurotar-data/location in floating cage/position-spatial-series/data"


# ----------------------------------------------------------------------------------- loading
def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in ds.get_assets() if a.path.endswith(".nwb"))


def _text(v):
    v = v[()]
    return v.decode() if isinstance(v, bytes) else str(v)


def _retry(fn, *args, tries=4):
    for k in range(tries):
        try:
            return fn(*args)
        except Exception:
            if k == tries - 1:
                raise


def _header(item):
    path, url = item
    with h5py.File(remfile.File(url), "r") as f:
        if not FULL_HEADER:
            return dict(path=path, url=url, identifier=_text(f["identifier"]),
                        subject=_text(f["general/subject/subject_id"]),
                        n_frames=f[FLUOR].shape[0], n_rois=f[FLUOR].shape[1])
        return dict(path=path, url=url, identifier=_text(f["identifier"]),
                    subject=_text(f["general/subject/subject_id"]),
                    genotype=_text(f["general/subject/genotype"]),
                    sex=_text(f["general/subject/sex"]),
                    start=_text(f["session_start_time"]),
                    n_frames=f[FLUOR].shape[0], n_rois=f[FLUOR].shape[1],
                    n_heading=f[HEADING].shape[0],
                    fluor_rate=float(f["processing/ophys/Fluorescence/raw-fluorescence/starting_time"].attrs["rate"]),
                    heading_rate=float(f["processing/neurotar-data/floating cage orientation/heading-spatial-series/starting_time"].attrs["rate"]),
                    heading_unit=f[HEADING].attrs.get("unit"),
                    heading_ref=_text(f["processing/neurotar-data/floating cage orientation/heading-spatial-series/reference_frame"]),
                    imaging_desc=_text(f["general/optophysiology/imgplane/description"]))


def classify(identifier: str) -> str:
    """Experiment of a file, from its identifier (the only place the files name it)."""
    s = identifier
    if "SingleCue" in s:
        return "single_rotation"
    if "ADNaxons" in s or "ADNAxons" in s:
        return "adn_axons"
    if "VISaxons" in s or "VISAxons" in s:
        return "vis_axons"
    if "DualCue" in s or "RSCSoma" in s:
        return "soma_dual"
    if "HeadRotation-" in s:
        return "head_rotation"
    if "PlatformRotation-" in s:
        return "chamber_rotation"
    if "Remapping" in s:
        return "remapping"
    if "Suspended" in s:
        return "visual_only"
    if "FR_CW_CCW" in s:
        tail = s.split("-")[-2]
        return {"FR": "animal_controlled", "FM": "animal_controlled", "CW": "motor_cw",
                "CCW": "motor_ccw", "DualRotation": "motor_both", "DualDir": "motor_both"}.get(tail, "other")
    return "other"


FULL_HEADER = True


def catalog(n_threads: int = 24, full: bool = True) -> pd.DataFrame:
    """One row per file: identifier, subject, sizes, and the experiment it belongs to.

    With full=False only the identifier, subject and array shapes are read (faster)."""
    global FULL_HEADER
    FULL_HEADER = full
    items = asset_urls()
    with ThreadPoolExecutor(n_threads) as ex:
        rows = list(ex.map(lambda it: _retry(_header, it), items))
    df = pd.DataFrame(rows)
    df["experiment"] = df["identifier"].map(classify)
    df["date"] = df["identifier"].str[:6]
    df = df.sort_values(["experiment", "subject", "identifier"]).reset_index(drop=True)
    return df


def _load(url):
    with h5py.File(remfile.File(url), "r") as f:
        F = f[FLUOR][:].astype(np.float64)
        h = f[HEADING][:].astype(np.float64).ravel()
        xy = f[POSITION][:]
    return dict(F=F, heading=h, xy=xy)


def load_many(urls, n_threads: int = 12) -> list[dict]:
    with ThreadPoolExecutor(n_threads) as ex:
        return list(ex.map(lambda u: _retry(_load, u), urls))


# ----------------------------------------------------------------------------------- activity
def dff(F: np.ndarray) -> np.ndarray:
    """(F - F0)/F0 per ROI (columns), F0 the mode of a Gaussian KDE of F."""
    from scipy.ndimage import gaussian_filter1d
    out = np.zeros_like(F)
    for i in range(F.shape[1]):
        y = F[:, i]
        y = y[np.isfinite(y)]
        if y.size < 10 or np.ptp(y) == 0:
            continue
        bw = 1.06 * y.std() * y.size ** (-1 / 5)
        hist, edges = np.histogram(y, bins=1024, range=(y.min(), y.max()))
        dens = gaussian_filter1d(hist.astype(float), bw / (edges[1] - edges[0]), mode="constant")
        f0 = (edges[:-1] + edges[1:])[np.argmax(dens)] / 2
        if f0 <= 0:
            f0 = np.median(y[y > 0]) if np.any(y > 0) else 1.0
        out[:, i] = (F[:, i] - f0) / f0
    return out


def _deconv_one(y):
    from oasis.functions import deconvolve
    y = np.nan_to_num(np.asarray(y, dtype=float))
    if np.ptp(y) == 0:
        return np.zeros_like(y)
    try:
        _, s, _, _, _ = deconvolve(y, penalty=1, optimize_g=5)
    except Exception:
        return np.zeros_like(y)
    return s


def spikes(D: np.ndarray, pool=None) -> np.ndarray:
    """Inferred spikes (frames x ROIs) from dF/F by OASIS AR(1)."""
    cols = [D[:, i] for i in range(D.shape[1])]
    res = pool.map(_deconv_one, cols, chunksize=16) if pool is not None else map(_deconv_one, cols)
    return np.stack(list(res), axis=1)


# ----------------------------------------------------------------------------------- heading and trials
def clean_heading(h: np.ndarray) -> np.ndarray:
    """The code's clean-up: NaN to 0, then steps of 20 to 350 degrees set to the previous value."""
    h = np.nan_to_num(np.asarray(h, dtype=float).copy())
    for _ in range(9):
        jump = np.abs(np.diff(h))
        is_jump = (jump > 20) & (jump < 350)
        if not is_jump.any():
            break
        idx = np.flatnonzero(is_jump)
        h[idx] = h[np.maximum(idx - 1, 0)]
    return h


def trial_segments(h: np.ndarray) -> list[np.ndarray]:
    """Full rotations of the chamber (code ControlledRotation.getTrialResponses)."""
    h = clean_heading(h)
    d = np.diff(h)
    dist = np.abs(h - h[0])
    pk, _ = find_peaks(dist - dist.max())
    wraps = pk[np.abs(dist[pk] - dist.max()) <= 10]
    slow = np.flatnonzero(np.abs(d) < 0.5)
    stops = []
    if slow.size:
        x = np.diff(slow) == 1
        f = np.flatnonzero(np.r_[False, x] != np.r_[x, False])
        starts, ends = f[0::2], f[1::2]
        for s0, e0 in zip(starts, ends):
            if e0 - s0 > 20:
                stops.extend(slow[s0:e0 + 1].tolist())
    breaks = np.sort(np.r_[wraps, np.array(stops, dtype=int)])
    segs = [np.arange(breaks[i] + 1, breaks[i + 1] + 1) for i in range(len(breaks) - 1)]
    segs = [s for s in segs if len(s) >= 50]
    keep = []
    for s in segs:
        if len(s) == 0:
            continue
        p = np.percentile(h[s], [25, 75])
        if not np.any(90 - np.abs(p) > 50):
            keep.append(s)
    return keep


def light_dark_frames(n_frames: int) -> tuple[list[np.ndarray], list[np.ndarray]]:
    """Light and dark segments of a dual-cue recording (code Separator.m and the experiment classes)."""
    if n_frames == 1950:
        seg, rep = 950, 1
    elif n_frames == 7550:
        seg, rep = 1250, 3
    elif n_frames == 15050:
        seg, rep = 1250, 6
    else:
        raise ValueError(n_frames)
    n_trials = n_frames // (seg * rep)
    light, dark = [], []
    for r in range(rep):
        base = r * seg * n_trials
        light.append(np.arange(base, base + seg))
        dark.append(np.arange(base + seg, base + 2 * seg))
    return light, dark


def bin_tuning(act: np.ndarray, h: np.ndarray) -> np.ndarray:
    """Tuning curves (ROIs x 60) of activity (frames x ROIs) over heading h, smoothed."""
    g = np.clip(np.floor((h + 180) / BIN_WIDTH).astype(int), 0, N_BINS - 1)
    sums = np.zeros((N_BINS, act.shape[1]))
    np.add.at(sums, g, act)
    cnt = np.bincount(g, minlength=N_BINS).astype(float)
    with np.errstate(invalid="ignore", divide="ignore"):
        tc = (sums / cnt[:, None]).T
    tc = np.nan_to_num(tc)
    return (np.roll(tc, 1, 1) + tc + np.roll(tc, -1, 1)) / 3


def trial_tuning(act: np.ndarray, h: np.ndarray, segments=None) -> np.ndarray:
    """Per-trial tuning curves, ROIs x 60 x trials, over the given frames (all frames by default)."""
    hc = clean_heading(h)
    if segments is None:
        segs = trial_segments(hc)
    else:
        segs = segments
    if not segs:
        return np.zeros((act.shape[1], N_BINS, 0))
    return np.stack([bin_tuning(act[s], hc[s]) for s in segs], axis=2)


def segments_within(h: np.ndarray, frame_blocks: list[np.ndarray]) -> list[np.ndarray]:
    """Trials found separately within each block of frames (as the code does per light or dark DataStructure)."""
    hc = clean_heading(h)
    out = []
    for blk in frame_blocks:
        blk = blk[blk < len(hc)]
        for s in trial_segments(hc[blk]):
            out.append(blk[s])
    return out


# ----------------------------------------------------------------------------------- Gaussian fits
def _model(p, cue):
    if cue == "single":
        a0, a1, b1, c1 = p.T
        e1 = np.exp(-((X[None] - b1[:, None]) / c1[:, None]) ** 2)
        f = a0[:, None] + a1[:, None] * e1
        J = np.stack([np.ones_like(f), e1,
                      a1[:, None] * e1 * 2 * (X[None] - b1[:, None]) / c1[:, None] ** 2,
                      a1[:, None] * e1 * 2 * (X[None] - b1[:, None]) ** 2 / c1[:, None] ** 3], axis=2)
        return f, J
    a0, a1, a2, b1, b2, c1, c2 = p.T
    e1 = np.exp(-((X[None] - b1[:, None]) / c1[:, None]) ** 2)
    e2 = np.exp(-((X[None] - b2[:, None]) / c2[:, None]) ** 2)
    f = a0[:, None] + a1[:, None] * e1 + a2[:, None] * e2
    J = np.stack([np.ones_like(f), e1, e2,
                  a1[:, None] * e1 * 2 * (X[None] - b1[:, None]) / c1[:, None] ** 2,
                  a2[:, None] * e2 * 2 * (X[None] - b2[:, None]) / c2[:, None] ** 2,
                  a1[:, None] * e1 * 2 * (X[None] - b1[:, None]) ** 2 / c1[:, None] ** 3,
                  a2[:, None] * e2 * 2 * (X[None] - b2[:, None]) ** 2 / c2[:, None] ** 3], axis=2)
    return f, J


def _bounds(cue):
    if cue == "single":
        w = np.pi / 6
        return (np.array([0, 0, np.pi / 2 - w, 1e-3]), np.array([1, 1, np.pi / 2 + w, np.pi / 2]))
    w = np.pi / 24
    return (np.array([0, 0, 0, np.pi / 2 - w, 3 * np.pi / 2 - w, 1e-3, 1e-3]),
            np.array([0.2, 1, 1, np.pi / 2 + w, 3 * np.pi / 2 + w, 2 * np.pi, 2 * np.pi]))


def rescale(Y: np.ndarray) -> np.ndarray:
    lo = Y.min(1, keepdims=True)
    rng = np.ptp(Y, axis=1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        out = np.where(rng > 0, (Y - lo) / rng, 0.0)
    return out


def center(Y: np.ndarray) -> np.ndarray:
    """Shift each curve so that its smoothed peak sits at bin 15 (the code's center_flag)."""
    sm = np.stack([np.convolve(np.r_[y[-7:], y, y[:7]], np.ones(15) / 15, "valid") for y in Y]) if len(Y) else Y
    pk = sm.argmax(1)
    idx = (np.arange(N_BINS)[None] + (pk - SHIFT_POINT)[:, None]) % N_BINS
    return np.take_along_axis(Y, idx, 1)


def fit_gauss(Y: np.ndarray, cue: str, n_iter: int = 40, do_rescale=True):
    """Bounded least-squares fit of the code's Gaussian to each row of Y (curves x 60).

    Returns parameters (curves x k) and r2 = 1 - SSE/SST. Start points and bounds are the code's
    (Cue.fitGaussians).
    """
    Y = rescale(Y) if do_rescale else np.asarray(Y, float)
    n = Y.shape[0]
    lo, hi = _bounds(cue)
    if cue == "single":
        p = np.tile([0, 0.5, np.pi / 2, np.pi / 6], (n, 1)).astype(float)
    else:
        p = np.column_stack([Y.min(1), Y[:, 12:17].mean(1), Y[:, 42:47].mean(1),
                             np.full(n, np.pi / 2), np.full(n, 3 * np.pi / 2),
                             np.full(n, np.pi / 6), np.full(n, np.pi / 6)])
    p = np.clip(p, lo, hi)
    f, J = _model(p, cue)
    sse = ((Y - f) ** 2).sum(1)
    lam = np.full(n, 1e-2)
    k = p.shape[1]
    eye = np.eye(k)[None]
    for _ in range(n_iter):
        r = Y - f
        Jt = J.transpose(0, 2, 1)
        A = Jt @ J
        g = (Jt @ r[..., None])[..., 0]
        D = A * eye
        try:
            step = np.linalg.solve(A + lam[:, None, None] * (D + 1e-9 * eye), g[..., None])[..., 0]
        except np.linalg.LinAlgError:
            step = np.zeros_like(p)
        pn = np.clip(p + np.nan_to_num(step), lo, hi)
        fn, Jn = _model(pn, cue)
        ssen = ((Y - fn) ** 2).sum(1)
        better = ssen < sse
        p[better] = pn[better]
        f[better] = fn[better]
        J[better] = Jn[better]
        sse[better] = ssen[better]
        lam = np.where(better, lam / 3, lam * 4)
        if np.all(lam > 1e6):
            break
    sst = ((Y - Y.mean(1, keepdims=True)) ** 2).sum(1)
    with np.errstate(invalid="ignore", divide="ignore"):
        r2 = np.where(sst > 0, 1 - sse / sst, np.nan)
    return p, r2


# ----------------------------------------------------------------------------------- selection test
def cohen_d(x1, x2):
    n1, n2 = len(x1), len(x2)
    s = np.sqrt(((n1 - 1) * np.var(x1, ddof=1) + (n2 - 1) * np.var(x2, ddof=1)) / (n1 + n2 - 2))
    return (np.mean(x1) - np.mean(x2)) / s if s > 0 else 0.0


def _rowcorr(a, b):
    a = a - a.mean(1, keepdims=True)
    b = b - b.mean(1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        return (a * b).sum(1) / np.sqrt((a * a).sum(1) * (b * b).sum(1))


def selection_test(trials: np.ndarray, cue: str, rng: np.random.Generator, n_iter: int = N_ITER,
                   centre: bool = False, pre_shuffle: bool = False) -> pd.DataFrame:
    """The code's heading-selection test for every ROI of one recording.

    trials: ROIs x 60 x n_trials. With pre_shuffle="each" (the commented
    calculateHeadDirection_shuff of Cue.m), the "real" trials are themselves circularly shifted
    by independent random amounts afresh in each iteration; with pre_shuffle="once" (a variant),
    they are shifted once before the test.
    """
    n_cells, _, n_tr = trials.shape
    cols = ["ks_p", "cohen_d", "r2", "r2_p90", "a1", "reliable", "shape_ok", "is_hd"]
    if n_tr < 2:
        return pd.DataFrame({c: [np.nan] * n_cells if c not in ("reliable", "shape_ok", "is_hd") else [False] * n_cells for c in cols})
    half = int(np.floor(n_tr / 2 + 0.5))
    rows = []
    for c in range(n_cells):
        A = trials[c].T                       # trials x 60
        if pre_shuffle == "once":
            sh0 = rng.integers(1, N_BINS + 1, n_tr)
            A = np.stack([np.roll(A[t], sh0[t]) for t in range(n_tr)])
        shifts = rng.integers(1, N_BINS + 1, (n_iter, n_tr))
        perm = np.argsort(rng.random((n_iter, n_tr)), axis=1)
        M = np.zeros((n_iter, n_tr))
        np.put_along_axis(M, perm[:, :half], 1.0, axis=1)
        idx = (np.arange(N_BINS)[None, None] - shifts[:, :, None]) % N_BINS
        R = A[np.arange(n_tr)[None, :, None], idx]          # iter x trials x 60
        if pre_shuffle in (True, "each"):
            # code: the "data" are trials shifted afresh in every iteration, and the real fit
            # uses the shifted trials of the last iteration
            sh2 = rng.integers(1, N_BINS + 1, (n_iter, n_tr))
            idx2 = (np.arange(N_BINS)[None, None] - sh2[:, :, None]) % N_BINS
            Ad = A[np.arange(n_tr)[None, :, None], idx2]
            m1 = np.einsum("it,itb->ib", M, Ad) / half
            m2 = np.einsum("it,itb->ib", 1 - M, Ad) / (n_tr - half)
            A = Ad[-1]
        else:
            m1 = (M @ A) / half
            m2 = ((1 - M) @ A) / (n_tr - half)
        cc_data = _rowcorr(m1, m2)
        r1 = np.einsum("it,itb->ib", M, R) / half
        r2_ = np.einsum("it,itb->ib", 1 - M, R) / (n_tr - half)
        cc_rand = _rowcorr(r1, r2_)
        a = cc_data[np.isfinite(cc_data)]
        b = cc_rand[np.isfinite(cc_rand)]
        if len(a) > 1 and len(b) > 1:
            ks_p = stats.ks_2samp(a, b).pvalue
            d = cohen_d(a, b)
        else:
            ks_p, d = 1.0, 0.0
        reliable = (ks_p < 0.1) and (d > 0.8)
        real_mean = A.mean(0)[None]
        # The shape test can change the outcome only for reliable cells; for the others only
        # the real curve is fitted (is_hd is the same, r2_p90 is left empty).
        Y = np.vstack([real_mean, R.mean(1)]) if reliable else real_mean
        if centre:
            Y = center(Y)
        p, r2 = fit_gauss(Y, cue)
        r2_real = r2[0]
        p90 = np.nanpercentile(r2[1:], 90) if np.isfinite(r2[1:]).any() else np.nan
        shape_ok = bool(np.isfinite(r2_real) and r2_real > p90)
        rows.append(dict(ks_p=ks_p, cohen_d=d, r2=r2_real, r2_p90=p90, a1=p[0, 1],
                         reliable=reliable, shape_ok=shape_ok,
                         is_hd=bool(reliable and shape_ok and p[0, 1] > 0)))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------------- alignment, preference, flip
def cv_shifts(trials: np.ndarray) -> np.ndarray:
    """Per ROI and trial, the shift that puts the peak of the other trials' mean at bin 15."""
    n_cells, _, n_tr = trials.shape
    tot = trials.sum(2)
    sh = np.zeros((n_cells, n_tr), dtype=int)
    for t in range(n_tr):
        other = (tot - trials[:, :, t]) / max(n_tr - 1, 1)
        sh[:, t] = SHIFT_POINT - other.argmax(1)
    return sh


def apply_shifts(trials: np.ndarray, sh: np.ndarray) -> np.ndarray:
    """Circularly shift each ROI's trials by the given shifts (ROIs x trials)."""
    n_cells, nb, n_tr = trials.shape
    out = np.empty_like(trials)
    for t in range(n_tr):
        k = sh[:, min(t, sh.shape[1] - 1)] if sh.shape[1] else np.zeros(n_cells, int)
        idx = (np.arange(nb)[None] - k[:, None]) % nb
        out[:, :, t] = np.take_along_axis(trials[:, :, t], idx, 1)
    return out


def cv_preferred(trials: np.ndarray) -> np.ndarray:
    """Cross-validated preferred heading (degrees, bin centre on -180..180) per ROI.

    The circular mean over held-out trials of the peak bin of the mean of the other trials.
    """
    n_cells, _, n_tr = trials.shape
    tot = trials.sum(2)
    centres = np.deg2rad(-180 + BIN_WIDTH / 2 + BIN_WIDTH * np.arange(N_BINS))
    z = np.zeros(n_cells, complex)
    for t in range(n_tr):
        other = tot - trials[:, :, t]
        z += np.exp(1j * centres[other.argmax(1)])
    return np.rad2deg(np.angle(z))


def peak_heading(tc: np.ndarray) -> np.ndarray:
    """Heading (degrees, bin centre) of the peak of each tuning curve (ROIs x 60)."""
    return -180 + BIN_WIDTH / 2 + BIN_WIDTH * tc.argmax(1)


def fit_preferred(tc: np.ndarray, cue: str = "single") -> np.ndarray:
    """The code's 'fit' preferred direction (Cue.calculatePreferredDirection), degrees on -180..180."""
    pk = np.stack([np.convolve(np.r_[y[-7:], y, y[:7]], np.ones(15) / 15, "valid") for y in tc]).argmax(1)
    Yc = center(tc)
    p, _ = fit_gauss(Yc, cue)
    xg = np.linspace(0, 2 * np.pi, N_BINS + 1)
    if cue == "single":
        b = p[:, 2]
    else:
        b = np.where(p[:, 1] >= p[:, 2], p[:, 3], p[:, 4])
    ang = np.mod(b + xg[(pk - SHIFT_POINT) % N_BINS], 2 * np.pi)
    # x = 0 is the first bin (-180 degrees)
    return np.rad2deg(np.angle(np.exp(1j * (ang - np.pi))))


def _smoothdata(y):
    n = len(y)
    w = max(int(round(n / 4)), 1)
    k = np.ones(w)
    # MATLAB smoothdata 'movmean', window n/4, shrinking at the ends (not circular)
    num = np.convolve(y, k, "same")
    den = np.convolve(np.ones(n), k, "same")
    return num / den


def flip_score(tc: np.ndarray) -> np.ndarray:
    """Flip score of each tuning curve (code Cue.calculateFlipScore)."""
    out = np.full(tc.shape[0], np.nan)
    q = tc.shape[1] // 4
    for i, y in enumerate(tc):
        b = _smoothdata(np.asarray(y, float))
        cc = {}
        for t in (q, 2 * q, 3 * q):
            s = np.roll(b, t)
            with np.errstate(invalid="ignore", divide="ignore"):
                cc[t] = np.corrcoef(b, s)[0, 1]
        out[i] = cc[2 * q] - (cc[q] + cc[3 * q]) / 2
    return out


def vtest(alpha_deg: np.ndarray, mu_deg: float = 0.0):
    """circ_vtest: V statistic and p-value for nonuniformity with a mean direction mu."""
    a = np.deg2rad(np.asarray(alpha_deg, float))
    a = a[np.isfinite(a)]
    n = len(a)
    r = np.abs(np.mean(np.exp(1j * a)))
    mean = np.angle(np.mean(np.exp(1j * a)))
    V = n * r * np.cos(mean - np.deg2rad(mu_deg))
    u = V * np.sqrt(2 / n)
    p = 1 - stats.norm.cdf(u)
    return V, p, n


def wrap180(a):
    return (np.asarray(a) + 180) % 360 - 180


def _sel_job(args):
    trials, cue, seed, centre, pre_shuffle = args
    return selection_test(trials, cue, np.random.default_rng(seed), centre=centre, pre_shuffle=pre_shuffle)


def selection_many(trial_list, cue, seed, pool=None, centre=False, pre_shuffle=False, chunk=8):
    """selection_test over several recordings, split into chunks of ROIs for a process pool.

    Each chunk gets its own generator from one SeedSequence, so results do not depend on the
    number of processes.
    """
    jobs, owners = [], []
    for i, tr in enumerate(trial_list):
        for s in range(0, tr.shape[0], chunk):
            jobs.append(tr[s:s + chunk])
            owners.append(i)
    seeds = np.random.SeedSequence(seed).spawn(len(jobs))
    args = [(j, cue, sd, centre, pre_shuffle) for j, sd in zip(jobs, seeds)]
    res = pool.map(_sel_job, args) if pool is not None else list(map(_sel_job, args))
    out = []
    for i in range(len(trial_list)):
        parts = [r for r, o in zip(res, owners) if o == i]
        out.append(pd.concat(parts, ignore_index=True) if parts else pd.DataFrame())
    return out
