"""Loading and measures for the widefield and behaviour session of dandiset 001712.

Davatolhagh et al. (2025), bioRxiv, doi:10.1101/2025.09.12.675910.

The dandiset holds one session of one mouse (sub-FD-28): a processed NWB file (trials, wheel,
pose, pupil, ROI motion energy, licks, and the widefield SVD components), a raw NWB file
(the widefield frames and sync events) and three camera videos. Files are streamed from the
archive; nothing is written to disk.

The dandiset has no published version, so the draft is read. `DRAFT_ASSETS` gives the asset
ids and sizes this entry was written against, and `check_assets` reports any difference.

Where the parameters come from:

- Reaction time is the wheel movement onset minus the stimulus onset, the paper's "time to
  first movement" (Figure 1E). A rightward choice is a counter-clockwise turn (the trial
  table's description: it moves the stimulus leftward, which centres a right stimulus).
- The psychometric function is the lapse-and-erf form used by the IBL (IBL et al. 2021, the
  paper's reference 10): P(right) = gL + (1 - gL - gR) * Phi((c - bias) / sigma).
- The subjective prior is an action-kernel model (the paper's Methods cite the ActionKernel
  model of reference 10 and 20 without parameters): the prior moves toward each choice by a
  learning rate fitted to this session's choices by maximum likelihood, with a logistic
  choice rule on contrast and prior. This is a common form; the paper's code is not public.
- The encoding model follows the lab's code the paper links (github.com/churchlandlab/chiCa,
  commit d98b3c6, encoding_model_full_version.py and encoding_utils.py): a time-varying
  intercept, task variables multiplied into it, analog movement variables per frame, analog
  columns z-scored on the training data, 10 folds stratified by trial time point, ridge with a
  penalty per target chosen on the training data (here by generalized cross-validation), and
  shuffles that permute each shuffled column over rows. The trial windows (`STIM_WINDOW`,
  `FEEDBACK_WINDOW`) are a choice here: the paper aligns to stimulus onset and feedback.
- Video components: the top `N_VIDEO_COMPONENTS` (200, the paper's number) of a camera's
  video and of its motion energy, from frames reduced to 1280 pixels by area averaging (blocks
  of 16 x 16 pixels for the body and right cameras, 32 x 32 for the left camera, which records
  at twice their resolution; a choice here, for speed and memory). The main notebook uses the
  body camera; the left and right cameras take about 15 minutes more to stream and decode and
  are used in a second notebook.
"""

from __future__ import annotations

import time

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import optimize, stats

DANDISET_ID = "001712"
DANDISET_VERSION = "draft"
SESSION = "sub-FD-28/sub-FD-28_ses-81f90b18-e61c-4d32-bbce-3e0c5f33f06c"
PROCESSED = f"{SESSION}_desc-processed_behavior+ophys.nwb"
RAW = f"{SESSION}_desc-raw_behavior+ophys.nwb"
VIDEOS = {cam: f"{SESSION}_ecephys+image/sub-FD-28_ses-81f90b18-e61c-4d32-bbce-3e0c5f33f06c_Video{cam}Camera.mp4"
          for cam in ("Body", "Left", "Right")}
POSE_SERIES = {"Body": "PoseEstimationSeriesTailStart", "Left": "PoseEstimationSeriesNoseTip",
               "Right": "PoseEstimationSeriesNoseTip"}
# The draft's assets when this entry was written (draft modified 2026-05-28T10:04:28Z).
DRAFT_ASSETS = {
    PROCESSED: ("3102badd-5260-498a-aaaf-acec7d7960e7", 1048736052),
    RAW: ("d99e80d1-1b9e-4a83-836c-dec4a46e4cce", 33347222662),
    VIDEOS["Body"]: ("07e84de1-50e0-443d-9ca0-caa5d7a2636d", 609146151),
    VIDEOS["Left"]: ("8ee6d630-f8d1-4400-aa82-782341c16309", 3496105008),
    VIDEOS["Right"]: ("18493935-8c8c-4f8b-b04f-802e8a7cdef5", 1100744490),
}

STIM_WINDOW = (-16, 16)       # frames around stimulus onset (about -0.5 to +0.5 s at 31.2 Hz)
FEEDBACK_WINDOW = (-6, 32)    # frames around feedback (about -0.2 to +1.0 s)
N_FOLDS = 10                  # Methods: 10-fold cross-validation
N_VIDEO_COMPONENTS = 200      # Results: the top 200 dimensions of the video SVD
VIDEO_BIN = {"Body": 16, "Left": 32, "Right": 16}   # 1280 pixels per camera after binning
ALPHAS = np.logspace(-1, 6, 29)


# --- archive --------------------------------------------------------------------------------

def draft_info() -> dict:
    """The draft's modification time and its assets (path, asset id, size)."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        assets = {a.path: (a.identifier, a.size) for a in ds.get_assets()}
        return {"modified": str(ds.version.modified), "assets": assets}


def check_assets(info: dict) -> list[str]:
    """Differences between the draft now and `DRAFT_ASSETS`."""
    out = []
    for path, (aid, size) in DRAFT_ASSETS.items():
        now = info["assets"].get(path)
        if now != (aid, size):
            out.append(f"{path}: expected {(aid, size)}, found {now}")
    return out


def url(path: str) -> str:
    aid = DRAFT_ASSETS[path][0]
    with DandiAPIClient() as client:
        asset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_asset(aid)
        return asset.get_content_url(follow_redirects=1, strip_query=True)


def open_nwb(path: str) -> h5py.File:
    return h5py.File(remfile.File(url(path)), "r")


def _text(v):
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray) and v.dtype == object:
        return [_text(x) for x in v]
    return v


def text(f: h5py.File, path: str):
    return _text(f[path][()])


# --- trials ---------------------------------------------------------------------------------

def load_trials(f: h5py.File) -> pd.DataFrame:
    """The trial table, with signed contrast (%; right positive), rightward choice (1/0, NaN for
    no response), correctness, and reaction time (s)."""
    t = f["intervals/trials"]
    df = pd.DataFrame({c: _text(t[c][:]) for c in t if c != "id"})
    df["signed_contrast"] = np.where(df.gabor_stimulus_side == "right", 1, -1) * df.gabor_stimulus_contrast
    df["choice_right"] = df.mouse_wheel_choice.map({"counter_clockwise": 1.0, "clockwise": 0.0, "none": np.nan})
    df["rt"] = df.wheel_movement_onset_time - df.gabor_stimulus_onset_time
    return df


def psychometric(c, bias, sigma, gl, gr):
    return gl + (1 - gl - gr) * stats.norm.cdf((np.asarray(c) - bias) / sigma)


def fit_psychometric(contrast: np.ndarray, right: np.ndarray) -> dict:
    """Maximum-likelihood lapse-and-erf fit; contrast in %."""
    def nll(p):
        pr = np.clip(psychometric(contrast, *p), 1e-6, 1 - 1e-6)
        return -np.sum(right * np.log(pr) + (1 - right) * np.log(1 - pr))
    best = None
    for b0 in (-20, 0, 20):
        for s0 in (5, 20, 50):
            r = optimize.minimize(nll, [b0, s0, 0.05, 0.05], method="L-BFGS-B",
                                  bounds=[(-100, 100), (0.5, 200), (0, 0.5), (0, 0.5)])
            if best is None or r.fun < best.fun:
                best = r
    return dict(zip(["bias", "sigma", "lapse_left", "lapse_right"], best.x), nll=best.fun, n=len(right))


def action_kernel_prior(choices: np.ndarray, rate: float) -> np.ndarray:
    """Prior of a rightward stimulus before each trial: starts at 0.5 and moves toward each
    choice (1 right, 0 left; trials without a choice leave it unchanged)."""
    out = np.empty(len(choices))
    p = 0.5
    for i, c in enumerate(choices):
        out[i] = p
        if np.isfinite(c):
            p = p + rate * (c - p)
    return out


def fit_action_kernel(trials: pd.DataFrame) -> dict:
    """Learning rate of the action kernel, by maximum likelihood of the choices under a
    logistic rule on contrast (as a fraction) and prior."""
    ch = trials.choice_right.to_numpy()
    ok = np.isfinite(ch)
    c = trials.signed_contrast.to_numpy() / 100

    def nll_for(rate):
        prior = action_kernel_prior(ch, rate)
        X = np.column_stack([np.ones(len(c)), c, np.sign(c) * np.sqrt(np.abs(c)), prior - 0.5])[ok]
        y = ch[ok]

        def nll(w):
            z = X @ w
            return np.sum(np.logaddexp(0, z) - y * z)
        r = optimize.minimize(nll, np.zeros(X.shape[1]), method="BFGS")
        return r.fun, r.x
    grid = np.linspace(0.01, 0.99, 99)
    vals = [nll_for(r)[0] for r in grid]
    rate = float(grid[int(np.argmin(vals))])
    fun, w = nll_for(rate)
    return {"rate": rate, "nll": fun, "weights": w, "grid": grid, "nll_grid": np.array(vals),
            "prior": action_kernel_prior(ch, rate)}


# --- imaging and movement -------------------------------------------------------------------

def load_svd(f: h5py.File) -> dict:
    """Haemodynamically corrected temporal components (frames x 200), their timestamps, and the
    spatial components (200 x height x width)."""
    o = "processing/ophys/"
    return {
        "svt": f[o + "SVDTemporalComponents/HaemoCorrectedSVDTemporalComponentsCalcium/data"][:].astype(np.float64),
        "t": f[o + "SVDTemporalComponents/HaemoCorrectedSVDTemporalComponentsCalcium/timestamps"][:],
        "u": f[o + "SVDSpatialComponents/SVDTemporalComponentsCalcium/image_mask"][:],
        "mean_image": f[o + "Images/MeanImage"][:],
    }


def bin_to_frames(t_src: np.ndarray, values: np.ndarray, frame_t: np.ndarray) -> np.ndarray:
    """Mean of a series over each imaging frame's interval (midpoints between frame times);
    frames with no sample take the nearest sample."""
    values = np.asarray(values, dtype=np.float64)
    if values.ndim == 1:
        values = values[:, None]
    edges = np.concatenate([[frame_t[0] - (frame_t[1] - frame_t[0]) / 2],
                            (frame_t[1:] + frame_t[:-1]) / 2,
                            [frame_t[-1] + (frame_t[-1] - frame_t[-2]) / 2]])
    idx = np.searchsorted(t_src, edges)
    good = np.isfinite(values)
    csum = np.vstack([np.zeros((1, values.shape[1])), np.cumsum(np.where(good, values, 0), axis=0)])
    ccount = np.vstack([np.zeros((1, values.shape[1])), np.cumsum(good, axis=0)])
    s = csum[idx[1:]] - csum[idx[:-1]]
    n = ccount[idx[1:]] - ccount[idx[:-1]]
    out = np.where(n > 0, s / np.maximum(n, 1), np.nan)
    near = np.clip(np.searchsorted(t_src, frame_t), 0, len(t_src) - 1)
    out = np.where(np.isnan(out), values[near], out)
    return out


def load_movement(f: h5py.File, frame_t: np.ndarray) -> pd.DataFrame:
    """Movement variables per imaging frame: wheel velocity (rad/s), the speed of each paw in the
    left and right cameras (pixels/s; frames with likelihood below 0.9 left out), and the three
    ROI motion energies (a.u.)."""
    cols = {}
    w = f["processing/wheel/WheelVelocitySmoothed"]
    rate = w["starting_time"].attrs["rate"]
    wv = w["data"][:]
    tw = w["starting_time"][()] + np.arange(len(wv)) / rate
    cols["wheel_velocity"] = bin_to_frames(tw, wv, frame_t)[:, 0]
    for cam in ("Left", "Right"):
        base = f"processing/pose_estimation/{cam}Camera/"
        t = f[base + "PoseEstimationSeriesNoseTip/timestamps"][:]
        for paw in ("LeftPaw", "RightPaw"):
            xy = f[base + f"PoseEstimationSeries{paw}/data"][:]
            conf = f[base + f"PoseEstimationSeries{paw}/confidence"][:]
            xy[conf < 0.9] = np.nan
            speed = np.hypot(*np.diff(xy, axis=0).T) / np.diff(t)
            cols[f"paw_{paw[:-3].lower()}_{cam.lower()}cam"] = bin_to_frames(t[1:], speed, frame_t)[:, 0]
    for cam in ("Left", "Right", "Body"):
        me = f[f"processing/motion_energy/{cam}CameraMotionEnergy"]
        cols[f"motion_energy_{cam.lower()}"] = bin_to_frames(me["timestamps"][:], me["data"][:], frame_t)[:, 0]
    df = pd.DataFrame(cols)
    return df.interpolate(limit_direction="both")


def video_components(f: h5py.File, frame_t: np.ndarray, camera: str = "Body", n: int = N_VIDEO_COMPONENTS) -> dict:
    """Top `n` temporal components of one camera's video and of its motion energy (absolute
    difference of consecutive frames), from frames reduced by area averaging over blocks of
    `VIDEO_BIN[camera]` pixels in each direction, binned to imaging frames. The video is streamed
    and decoded once; reduced frames are kept as uint8.
    The camera's frame times are those of its pose estimation series."""
    import av
    started = time.time()
    path = VIDEOS[camera]
    cam_t = f[f"processing/pose_estimation/{camera}Camera/{POSE_SERIES[camera]}/timestamps"][:]
    container = av.open(remfile.File(url(path), verbose=False))
    stream = container.streams.video[0]
    stream.thread_type = "AUTO"
    frames = []
    k = VIDEO_BIN[camera]
    for fr in container.decode(stream):
        b = fr.reformat(width=fr.width // k, height=fr.height // k, format="gray", interpolation="AREA")
        frames.append(b.to_ndarray().ravel())
    container.close()
    video = np.asarray(frames)
    del frames
    n_frames = len(video)
    m = min(n_frames, len(cam_t))
    video, cam_t_used = video[:m], cam_t[:m]
    out = {"n_video_frames": n_frames, "n_timestamps": len(cam_t), "decode_s": time.time() - started,
           "pixels": video.shape[1]}
    chunk = 20000

    def blocks(kind):
        for i in range(0, m, chunk):
            x = video[max(i - 1, 0):i + chunk].astype(np.float64)
            if kind == "motion":
                x = np.abs(np.diff(x, axis=0)) if i > 0 else np.abs(np.diff(x, axis=0, prepend=x[:1]))
            yield x
    for kind in ("video", "motion"):
        mean = sum(b.sum(0) for b in blocks(kind)) / m
        cov = sum((b - mean).T @ (b - mean) for b in blocks(kind))
        evals, evecs = np.linalg.eigh(cov)
        order = np.argsort(evals)[::-1][:n]
        comps = np.vstack([(b - mean) @ evecs[:, order] for b in blocks(kind)])
        out[f"{kind}_explained"] = float(evals[order].sum() / evals.sum())
        out[kind] = bin_to_frames(cam_t_used, comps, frame_t)
    return out


# --- trial alignment and evoked responses ----------------------------------------------------

def frame_index(frame_t: np.ndarray, times: np.ndarray) -> np.ndarray:
    """Index of the imaging frame nearest each time."""
    i = np.clip(np.searchsorted(frame_t, times), 1, len(frame_t) - 1)
    return np.where(np.abs(frame_t[i - 1] - times) < np.abs(frame_t[i] - times), i - 1, i)


def segment_frames(trials: pd.DataFrame, frame_t: np.ndarray, valid: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Rows of the trialized design: for each valid trial, the frames of `STIM_WINDOW` around
    stimulus onset and of `FEEDBACK_WINDOW` around feedback. Returns frame indices, the trial
    time point (0 .. points-1) and the trial index of each row."""
    s0 = frame_index(frame_t, trials.gabor_stimulus_onset_time.to_numpy())
    f0 = frame_index(frame_t, trials.feedback_time.to_numpy())
    offs_s = np.arange(*STIM_WINDOW)
    offs_f = np.arange(*FEEDBACK_WINDOW)
    points = len(offs_s) + len(offs_f)
    rows, tp, tr = [], [], []
    for i in np.flatnonzero(valid):
        fr = np.concatenate([s0[i] + offs_s, f0[i] + offs_f])
        rows.append(fr)
        tp.append(np.arange(points))
        tr.append(np.full(points, i))
    return np.concatenate(rows), np.concatenate(tp), np.concatenate(tr)


def evoked(svt: np.ndarray, onset_frames: np.ndarray, post=(3, 13), pre=(-9, 0)) -> np.ndarray:
    """Per trial, the mean of the components over `post` frames after onset minus the mean over
    `pre` frames (defaults: 0.1 to 0.4 s and -0.3 to 0 s at 31.2 Hz). Trials x components."""
    a = np.stack([svt[o + post[0]:o + post[1]].mean(0) - svt[o + pre[0]:o + pre[1]].mean(0) for o in onset_frames])
    return a


# --- encoding model --------------------------------------------------------------------------

def build_design(trials: pd.DataFrame, rows_trial: np.ndarray, rows_tp: np.ndarray, points: int,
                 subjective_prior: np.ndarray, movement: np.ndarray, rows_frame: np.ndarray) -> tuple[np.ndarray, dict, list]:
    """The design matrix and the column indices of each regressor and group. Task variables are
    coded per trial and multiplied into the time-point block (chiCa): choice (+1 right, -1 left),
    left and right stimulus contrast (fractions), outcome (+1 rewarded, -1 not), true prior
    (0.5 - probability_left, positive when right is likely) and subjective prior (minus 0.5)."""
    tr = trials.iloc[rows_trial]
    block = np.zeros((len(rows_tp), points))
    block[np.arange(len(rows_tp)), rows_tp] = 1
    task_values = {
        "choice": np.where(tr.choice_right == 1, 1.0, -1.0),
        "stim_left": np.where(tr.gabor_stimulus_side == "left", tr.gabor_stimulus_contrast / 100, 0.0),
        "stim_right": np.where(tr.gabor_stimulus_side == "right", tr.gabor_stimulus_contrast / 100, 0.0),
        "outcome": np.where(tr.is_mouse_rewarded, 1.0, -1.0),
        "true_prior": 0.5 - tr.probability_left.to_numpy(),
        "subjective_prior": subjective_prior[rows_trial] - 0.5,
    }
    parts = [block]
    index = {"intercept": np.arange(points)}
    col = points
    for name, v in task_values.items():
        parts.append(block * v[:, None])
        index[name] = np.arange(col, col + points)
        col += points
    mov = movement[rows_frame]
    parts.append(mov)
    index["movement_columns"] = np.arange(col, col + mov.shape[1])
    X = np.hstack(parts)
    analog = list(index["movement_columns"])
    return X, index, analog


def _ridge_fold(Xtr, Ytr, Xte):
    """Ridge with a penalty per target chosen by generalized cross-validation on the training
    rows; returns test predictions and the chosen penalties."""
    xm = Xtr.mean(0)
    ym = Ytr.mean(0)
    Xc, Yc = Xtr - xm, Ytr - ym
    G = Xc.T @ Xc
    lam, V = np.linalg.eigh(G)
    lam = np.clip(lam, 0, None)
    B = V.T @ (Xc.T @ Yc)                   # p x targets
    keep = lam > lam.max() * 1e-12
    uty = np.zeros_like(B)
    uty[keep] = B[keep] / np.sqrt(lam[keep])[:, None]
    yy = (Yc ** 2).sum(0)
    proj = (uty ** 2).sum(0)
    n = Xtr.shape[0]
    best_gcv = np.full(Ytr.shape[1], np.inf)
    best_alpha = np.zeros(Ytr.shape[1])
    for a in ALPHAS:
        shrink = (a / (lam + a)) ** 2
        rss = yy - proj + (shrink[keep, None] * uty[keep] ** 2).sum(0)
        df = (lam[keep] / (lam[keep] + a)).sum()
        gcv = n * rss / (n - df) ** 2
        better = gcv < best_gcv
        best_gcv[better] = gcv[better]
        best_alpha[better] = a
    pred = np.empty((Xte.shape[0], Ytr.shape[1]))
    Xtc = Xte - xm
    for a in np.unique(best_alpha):
        t = best_alpha == a
        beta = V @ (B[:, t] / (lam + a)[:, None])
        pred[:, t] = Xtc @ beta + ym[t]
    return pred, best_alpha


def folds(timepoints: np.ndarray, rng: np.random.Generator) -> list[np.ndarray]:
    """Test rows of `N_FOLDS` folds stratified by trial time point (as StratifiedKFold with
    shuffling): within each time point the rows are shuffled and dealt to folds in turn."""
    assign = np.empty(len(timepoints), dtype=int)
    for t in np.unique(timepoints):
        idx = np.flatnonzero(timepoints == t)
        perm = rng.permutation(idx)
        assign[perm] = (np.arange(len(perm)) + rng.integers(N_FOLDS)) % N_FOLDS
    return [np.flatnonzero(assign == k) for k in range(N_FOLDS)]


def trial_folds(trial_of_row: np.ndarray, rng: np.random.Generator) -> list[np.ndarray]:
    """Test rows of `N_FOLDS` folds that keep each trial's rows together: trials are shuffled
    and dealt to folds in turn. A variant of `folds`, which splits rows at random within each
    time point (chiCa) and so puts frames of one trial in both training and test rows."""
    trials_ = rng.permutation(np.unique(trial_of_row))
    fold_of = dict(zip(trials_, np.arange(len(trials_)) % N_FOLDS))
    assign = np.array([fold_of[t] for t in trial_of_row])
    return [np.flatnonzero(assign == k) for k in range(N_FOLDS)]


def fit_model(X, Y, analog, test_folds, shuffle_cols, rng, u_flat=None) -> dict:
    """Cross-validated fit. Shuffled columns are permuted over rows, each independently (chiCa).
    Returns, averaged over folds: (a) pooled pixel-space R2, (b) mean over pixels of per-pixel R2
    (when `u_flat`, pixels x components, is given; also the per-pixel map), (c) mean over
    components of per-component R2; and the penalty chosen for each target in each fold."""
    Xs = np.array(X, dtype=np.float64)
    for k in shuffle_cols:
        Xs[:, k] = Xs[rng.permutation(Xs.shape[0]), k]
    n = len(Xs)
    res = {"pooled": [], "pixel_mean": [], "component_mean": [], "alpha_median": []}
    all_alphas = []
    pixel_maps = []
    for te in test_folds:
        tr = np.setdiff1d(np.arange(n), te)
        Xtr, Xte = Xs[tr].copy(), Xs[te].copy()
        if analog:
            m, s = Xtr[:, analog].mean(0), Xtr[:, analog].std(0)
            s[s == 0] = 1
            Xtr[:, analog] = (Xtr[:, analog] - m) / s
            Xte[:, analog] = (Xte[:, analog] - m) / s
        pred, alphas = _ridge_fold(Xtr, Y[tr], Xte)
        yte = Y[te]
        resid = yte - pred
        cen = yte - yte.mean(0)
        ss_res = (resid ** 2).sum(0)
        ss_tot = (cen ** 2).sum(0)
        res["pooled"].append(1 - ss_res.sum() / ss_tot.sum())
        res["component_mean"].append(np.mean(1 - ss_res / ss_tot))
        res["alpha_median"].append(np.median(alphas))
        all_alphas.append(alphas)
        if u_flat is not None:
            R = resid.T @ resid
            S = cen.T @ cen
            num = ((u_flat @ R) * u_flat).sum(1)
            den = ((u_flat @ S) * u_flat).sum(1)
            r2 = 1 - num / den
            pixel_maps.append(r2)
            res["pixel_mean"].append(np.mean(r2))
    out = {k: float(np.mean(v)) for k, v in res.items() if v}
    out["folds"] = {k: np.array(v) for k, v in res.items() if v}
    out["alphas"] = np.array(all_alphas)          # folds x targets
    if pixel_maps:
        out["pixel_map"] = np.mean(pixel_maps, axis=0)
    return out
