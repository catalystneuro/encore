"""Loading and measures for dandiset 000016 (Najafi et al. 2020, Neuron 105, 165-179).

Each NWB file is one imaging session of one mouse. It holds a trial table whose times are
relative to the start of each trial, the ROI table (status good or bad; neuron type excitatory,
inhibitory or unknown), and, for the good ROIs, trial-segmented traces aligned to trial events
(groups `dFoF_<event>Al`, one dataset per trial, frames x ROIs, NaN when the trial lacks the
event). The groups are named dFoF but hold the inferred spiking activity (sparse, non-negative,
at most 1); the data check in the first notebook shows this. Files are streamed from the archive
at the pinned version with fsspec over HTTP; nothing is written to disk.

Where the parameters come from (the claims file is claims/000016/10.1016-j.neuron.2019.09.045.yaml,
whose opening comment gives the methods common to all claims):

- Bins of 3 frames (97 ms) counted from the event frame, so that bin -1 is the 3 frames before
  the event (claims file, opening comment, from the paper's code). `BIN_FRAMES`.
- Trials with a correct or incorrect choice; change-of-mind trials have no choice-aligned
  traces in the files (they are in a separate `_COM` group) and so drop out (claims file).
  The files do not mark helped trials or the first trials of a session, so these are kept.
- The choice is coded as high-rate choice or not, from the trial type and outcome. The files do
  not say which side is high; ROC selectivity, decoding accuracy and same or opposite preference
  do not depend on the side.
- ROC: AUC between the two choices on correct trials without 16 Hz trials, 50 label shuffles,
  selective when normpdf(AUC)/normpdf(mean) <= 0.05 of a normal fitted to the shuffled AUCs, at
  least 10 trials of each choice (claims file, from the paper's code). `N_SHUFFLES`,
  `MIN_TRIALS`. The empirical shuffle p is a variant named in fig2bc-fraction-selective-similar.
- Decoders: linear SVM with L2 penalty and squared hinge loss, the objective of sklearn's
  LinearSVC with its default intercept (a constant feature of 1 that is penalised like the
  weights). It is solved exactly here, by a Newton method with line search, warm-started along
  the C path; on random problems it matches LinearSVC run to tight tolerance (the notebook shows
  a check on real data). Each neuron z-scored per bin over the decoder's trials with 5e-4 added
  to the SD; left and right trials matched by random subsampling; 50 repetitions of a random
  90/10 split; C from 10^(-6 to 6 in steps of 0.2) divided by the number of trials, the one with
  the smallest mean test error; shuffled control scores the same predictions against permuted
  test labels (claims file). `N_REPS`, `C_GRID`, `TEST_FRACTION`, `SD_PAD`. The number of test
  trials is round(10% of the balanced trials), a standard choice.
- Noise correlations: the choice mean subtracted within each choice, Pearson r per pair, each
  neuron's r averaged over its partners (claims file, fig6a and fig6bc).
"""

from __future__ import annotations

import os
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
from scipy import stats

DANDISET_ID = "000016"
DANDISET_VERSION = "0.260915.2309"

GROUPS = {
    "choice": "dFoF_firstSideTryAl",
    "choice_com": "dFoF_firstSideTryAl_COM",
    "stim": "dFoF_stimAl_noEarlyDec",
    "stim_all": "dFoF_stimAl_allTrs",
    "stimoff": "dFoF_stimOffAl",
    "go": "dFoF_goToneAl",
    "reward": "dFoF_rewardAl",
    "incorr": "dFoF_commitIncorrAl",
    "init": "dFoF_initToneAl",
}
MICE = {"mouse1_fni16": 1, "mouse2_fni17": 2, "mouse3_fni18": 3, "mouse4_fni19": 4}

BIN_FRAMES = 3
N_SHUFFLES = 50
MIN_TRIALS = 10
Z_SELECTIVE = np.sqrt(2 * np.log(20))   # normpdf(z)/normpdf(0) <= 0.05
N_REPS = 50
N_EXC_SAMPLES = 50
C_GRID = 10.0 ** np.arange(-6, 6.0001, 0.2)
TEST_FRACTION = 0.1
SD_PAD = 5e-4
SEED = 16


# --- archive --------------------------------------------------------------------------------

def asset_urls() -> pd.DataFrame:
    """Path, streaming URL, mouse and recording date of every NWB file at the pinned version."""
    from dandi.dandiapi import DandiAPIClient
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = [(a.path, a.get_content_url(follow_redirects=1, strip_query=True), a.size)
                for a in ds.get_assets() if a.path.endswith(".nwb")]
    df = pd.DataFrame(rows, columns=["path", "url", "size"])
    df["subject"] = df.path.str.split("/").str[0].str.replace("sub-", "").str.replace("-", "_")
    df["mouse"] = df.subject.map(MICE)
    return df.sort_values("path").reset_index(drop=True)


def open_nwb(url: str) -> h5py.File:
    import fsspec
    fo = fsspec.filesystem("http").open(url, "rb", block_size=2 ** 22, cache_type="blockcache")
    return h5py.File(fo, "r")


def _text(x):
    x = x[()]
    return x.decode() if isinstance(x, bytes) else str(x)


def read_trials(f) -> pd.DataFrame:
    T = f["intervals/trials"]
    df = pd.DataFrame({c: (T[c][:].astype(str) if T[c].dtype == object else T[c][:])
                       for c in T.attrs["colnames"]})
    df["decided"] = df.trial_response.isin(["correct", "incorrect"])
    high = df.trial_type.eq("High-rate")
    corr = df.trial_response.eq("correct")
    df["choice_high"] = np.where(df.decided, (high == corr).astype(float), np.nan)
    df["stim_high"] = high.astype(float)
    df["is16"] = df.trial_pulse_rate.eq(16.0)
    return df


def read_group(f, name: str, rois_only=True):
    """Traces of one alignment: (trials, frames, ROIs) float32, the event frame and frame period."""
    G = f["processing/Ophys"][name]
    names = sorted(G.keys(), key=lambda s: int(s.split("_")[1]))
    first = G[names[0]]
    period = float(first["starting_time"].attrs["rate"])     # the file stores the period here
    start = float(first["starting_time"][()])
    event = int(round(-start / period))
    data = np.stack([G[n]["data"][:] for n in names]).astype(np.float32)
    return dict(x=data, event=event, period=period, start=start, n_trials=len(names))


def load_session(path: str, url: str, groups=("choice",), behaviour=False) -> dict:
    """One session: trials, ROI types of the traced ROIs, and the requested aligned traces."""
    with open_nwb(url) as f:
        trials = read_trials(f)
        P = f["processing/Ophys/ImageSegmentation/PlaneSegmentation"]
        status = P["roi_status"][:].astype(str)
        ntype = P["neuron_type"][:].astype(str)
        G0 = f["processing/Ophys"][GROUPS["choice"]]
        first = sorted(G0.keys())[0]
        rois = G0[first]["rois"][:]
        out = dict(path=path, subject=_text(f["general/subject/subject_id"]),
                   date=_text(f["session_start_time"])[:10], description=_text(f["session_description"]),
                   imaging_rate=float(f["general/optophysiology/ImagingPlane/imaging_rate"][()]),
                   trials=trials, roi_status=status, roi_type_all=ntype, rois=rois,
                   types=ntype[rois], roi_status_traced=status[rois], groups={},
                   available=[k for k in f["processing/Ophys"].keys()])
        for g in groups:
            if GROUPS[g] in f["processing/Ophys"]:
                out["groups"][g] = read_group(f, GROUPS[g])
        if behaviour:
            B = f["processing/Behavior/Epoched_behavioral_series"]
            out["lick"] = dict(t=B["firstSideTryAl_lick/timestamps"][:], x=B["firstSideTryAl_lick/data"][:])
            out["wheel"] = dict(t=B["firstSideTryAl_wheelRev/timestamps"][:],
                                x=B["firstSideTryAl_wheelRev/data"][:])
    out["mouse"] = MICE[out["subject"]]
    return out


def map_sessions(fn, items, workers=4):
    """Run fn on each item in fresh worker processes with one BLAS thread each (many small
    solves run slower with threads competing); results in input order."""
    import multiprocessing as mp
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[k] = "1"
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return list(ex.map(fn, items))


# --- bins and trials ---------------------------------------------------------------------------

def bin_traces(x: np.ndarray, event: int, period: float):
    """Average non-overlapping 3-frame bins counted from the event frame.

    Returns (trials, bins, neurons), the index of bin -1 (the 3 frames before the event) and the
    start time of each bin in ms relative to the event."""
    n_before = event // BIN_FRAMES
    n_after = (x.shape[1] - event) // BIN_FRAMES
    lo = event - n_before * BIN_FRAMES
    hi = event + n_after * BIN_FRAMES
    xb = x[:, lo:hi].reshape(x.shape[0], n_before + n_after, BIN_FRAMES, x.shape[2]).mean(2)
    t = (np.arange(-n_before, n_after) * BIN_FRAMES) * period * 1000
    return xb, n_before - 1, t


def frame_window(x: np.ndarray, event: int, period: float, t0_ms: float, t1_ms: float):
    """Mean over the frames whose time from the event lies in [t0, t1) ms."""
    t = (np.arange(x.shape[1]) - event) * period * 1000
    sel = (t >= t0_ms) & (t < t1_ms)
    return x[:, sel].mean(1), np.where(sel)[0] - event


def valid_trials(x: np.ndarray) -> np.ndarray:
    return np.isfinite(x).all(axis=(1, 2))


# --- ROC ---------------------------------------------------------------------------------------

def auc(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """AUC of each column of x (trials, ...) for y == 1 against y == 0 (ties counted half)."""
    y = np.asarray(y).astype(bool)
    r = stats.rankdata(x, axis=0)
    n1, n0 = y.sum(), (~y).sum()
    return (r[y].sum(0) - n1 * (n1 + 1) / 2) / (n1 * n0)


def roc_selectivity(x: np.ndarray, y: np.ndarray, rng, n_shuffles=N_SHUFFLES) -> dict:
    """AUC, selectivity 2|AUC-0.5|, shuffled AUCs and significance (normal fit, and empirical p)."""
    a = auc(x, y)
    sh = np.stack([auc(x, rng.permutation(y)) for _ in range(n_shuffles)])
    mu, sd = sh.mean(0), sh.std(0, ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        z = (a - mu) / sd
    sig = np.abs(z) >= Z_SELECTIVE
    sig = np.where(sd > 0, sig, False)
    p_emp = (np.abs(sh - 0.5) >= np.abs(a - 0.5)).mean(0)
    return dict(auc=a, sel=2 * np.abs(a - 0.5), sig=sig, sig_emp=p_emp < 0.05,
                sel_shuffled=2 * np.abs(sh - 0.5).mean(0))


# --- correlations -----------------------------------------------------------------------------

def noise_corr(x: np.ndarray, y=None) -> np.ndarray:
    """Pearson r between neurons over trials, after subtracting each choice's mean when y given."""
    x = x.astype(float).copy()
    if y is not None:
        for v in np.unique(y):
            x[y == v] -= x[y == v].mean(0)
    with np.errstate(invalid="ignore", divide="ignore"):
        r = np.corrcoef(x.T)
    np.fill_diagonal(r, np.nan)
    return r


def mean_partner_r(r: np.ndarray, rows: np.ndarray, cols: np.ndarray) -> np.ndarray:
    """Each row neuron's mean r over the column neurons (itself excluded), NaN-aware."""
    sub = r[np.ix_(rows, cols)]
    with np.errstate(invalid="ignore"):
        return np.nanmean(sub, 1) if sub.shape[1] else np.full(len(rows), np.nan)


def max_bin_match(med_e: np.ndarray, med_i: np.ndarray, n_bins=50):
    """Neurons in the bin of median activity that holds most inhibitory neurons (Methods, S10D)."""
    allv = np.r_[med_e, med_i]
    edges = np.linspace(allv.min(), allv.max(), n_bins + 1)
    bi = np.clip(np.digitize(med_i, edges) - 1, 0, n_bins - 1)
    be = np.clip(np.digitize(med_e, edges) - 1, 0, n_bins - 1)
    best = np.bincount(bi, minlength=n_bins).argmax()
    return be == best, bi == best


# --- SVM ---------------------------------------------------------------------------------------

def _obj_primal(w, X, y, C):
    r = np.maximum(0, 1 - y * np.einsum("bnd,bd->bn", X, w))
    return 0.5 * (w * w).sum(1) + C * (r * r).sum(1)


def _newton_primal(X, y, C, w, max_iter=200, tol=1e-12):
    B, n, d = X.shape
    eye = np.eye(d)
    Xt = np.swapaxes(X, 1, 2)
    f = _obj_primal(w, X, y, C)
    act = np.arange(B)
    for _ in range(max_iter):
        if len(act) == 0:
            break
        Xa, ya, Ca, wa, fa = X[act], y[act], C[act], w[act], f[act]
        m = (ya * np.einsum("bnd,bd->bn", Xa, wa)) < 1
        Xm = Xt[act] * m[:, None, :]
        A = eye + 2 * Ca[:, None, None] * (Xm @ Xa)
        rhs = 2 * Ca[:, None] * np.einsum("bdn,bn->bd", Xm, ya)
        step = np.linalg.solve(A, rhs[..., None])[..., 0] - wa
        t = np.ones(len(act))
        fn = _obj_primal(wa + step, Xa, ya, Ca)
        for _ in range(50):
            bad = fn > fa
            if not bad.any():
                break
            t[bad] *= 0.5
            fn[bad] = _obj_primal(wa[bad] + t[bad, None] * step[bad], Xa[bad], ya[bad], Ca[bad])
        better = fn < fa
        w[act] = np.where(better[:, None], wa + t[:, None] * step, wa)
        f[act] = np.minimum(fn, fa)
        act = act[(fa - np.minimum(fn, fa)) > tol * np.maximum(1, fa)]
    return w


def _obj_kernel(b, K, y, C):
    o = np.einsum("bij,bj->bi", K, b)
    r = np.maximum(0, 1 - y * o)
    return 0.5 * (b * o).sum(1) + C * (r * r).sum(1)


def _newton_kernel(K, y, C, b, max_iter=200, tol=1e-12):
    B, n, _ = K.shape
    eye = np.eye(n)
    f = _obj_kernel(b, K, y, C)
    act = np.arange(B)
    for _ in range(max_iter):
        if len(act) == 0:
            break
        Ka, ya, Ca, ba, fa = K[act], y[act], C[act], b[act], f[act]
        m = (ya * np.einsum("bij,bj->bi", Ka, ba)) < 1
        mf = m.astype(float)
        A = (Ka + eye / (2 * Ca[:, None, None])) * mf[:, :, None] * mf[:, None, :] + eye * (1 - mf)[:, :, None]
        step = np.linalg.solve(A, (ya * mf)[..., None])[..., 0] - ba
        t = np.ones(len(act))
        fn = _obj_kernel(ba + step, Ka, ya, Ca)
        for _ in range(50):
            bad = fn > fa
            if not bad.any():
                break
            t[bad] *= 0.5
            fn[bad] = _obj_kernel(ba[bad] + t[bad, None] * step[bad], Ka[bad], ya[bad], Ca[bad])
        better = fn < fa
        b[act] = np.where(better[:, None], ba + t[:, None] * step, ba)
        f[act] = np.minimum(fn, fa)
        act = act[(fa - np.minimum(fn, fa)) > tol * np.maximum(1, fa)]
    return b


def svm_path(X: np.ndarray, y: np.ndarray, Cs: np.ndarray) -> np.ndarray:
    """Exact L2 squared-hinge SVMs (LinearSVC's objective, penalised intercept) for each C.

    X (R, n, d) training sets, y (R, n) in {-1, 1}; returns weights (R, len(Cs), d + 1), the last
    element the intercept. Solved in the primal when d + 1 <= n, else in the span of the trials."""
    R, n, d = X.shape
    Xb = np.concatenate([X, np.ones((R, n, 1))], 2)
    W = np.zeros((R, len(Cs), d + 1))
    if d + 1 <= n:
        w = np.zeros((R, d + 1))
        for j, C in enumerate(Cs):
            w = _newton_primal(Xb, y, np.full(R, C), w.copy())
            W[:, j] = w
    else:
        K = Xb @ np.swapaxes(Xb, 1, 2)
        b = np.zeros((R, n))
        for j, C in enumerate(Cs):
            b = _newton_kernel(K, y, np.full(R, C), b.copy())
            W[:, j] = np.einsum("rn,rnd->rd", b, Xb)
    return W


def zscore(x: np.ndarray, axis=0):
    mu = x.mean(axis, keepdims=True)
    sd = x.std(axis, keepdims=True) + SD_PAD
    return (x - mu) / sd, mu, sd


def splits(y: np.ndarray, rng, n_reps=N_REPS, balance_groups=None):
    """Balanced random subsamples split 90/10: lists of (train index, test index).

    The two classes of y are matched by random subsampling; with balance_groups, each class is
    matched within each group (e.g. equal left and right choices in each stimulus category)."""
    out = []
    y = np.asarray(y)
    for _ in range(n_reps):
        if balance_groups is None:
            i1, i0 = np.where(y == 1)[0], np.where(y == 0)[0]
            k = min(len(i1), len(i0))
            idx = np.r_[rng.choice(i1, k, replace=False), rng.choice(i0, k, replace=False)]
        else:
            idx = []
            g = np.asarray(balance_groups)
            k = min(((y == c) & (g == v)).sum() for c in (0, 1) for v in np.unique(g))
            for c in (0, 1):
                for v in np.unique(g):
                    idx.append(rng.choice(np.where((y == c) & (g == v))[0], k, replace=False))
            idx = np.concatenate(idx)
        idx = rng.permutation(idx)
        n_test = int(round(TEST_FRACTION * len(idx)))
        out.append((idx[n_test:], idx[:n_test]))
    return out


def decode(X: np.ndarray, y: np.ndarray, rng, n_reps=N_REPS, Cs=None, C_fixed=None,
           test_sets=None, balance_groups=None, sp=None) -> dict:
    """Cross-validated choice decoder on one population at one bin.

    X (trials, neurons) is z-scored here over the given trials. test_sets maps a name to
    (X_other, kind): kind "same_trials" gives (trials, bins, neurons) already z-scored per bin,
    on which each repetition's decoder is tested on its own held-out trials (stability); kind
    "other_trials" gives (trials, neurons) already normalised, on which every repetition is
    tested whole (e.g. incorrect trials). Returns accuracies in percent."""
    y = np.asarray(y).astype(int)
    Xz, mu, sd = zscore(X)
    if sp is None:
        sp = splits(y, rng, n_reps, balance_groups)
    n_reps = len(sp)
    Cs = (C_GRID / len(y)) if Cs is None else Cs
    if C_fixed is not None:
        Cs = np.array([C_fixed])
    tr = np.stack([Xz[a] for a, _ in sp])
    ytr = np.stack([2 * y[a] - 1 for a, _ in sp])
    W = svm_path(tr, ytr.astype(float), Cs)                       # (R, nC, d+1)
    te = np.stack([Xz[b] for _, b in sp])
    yte = np.stack([y[b] for _, b in sp])
    pred = (np.einsum("rnd,rcd->rcn", te, W[:, :, :-1]) + W[:, :, None, -1]) > 0
    acc = (pred == yte[:, None, :].astype(bool)).mean(2)          # (R, nC)
    best = int(np.argmin((1 - acc).mean(0)))
    perm = np.stack([rng.permutation(v) for v in yte])
    shfl = (pred[:, best] == perm.astype(bool)).mean(1)
    out = dict(acc=100 * acc[:, best].mean(), acc_reps=100 * acc[:, best], shfl=100 * shfl.mean(),
               shfl_reps=100 * shfl, C=Cs[best], C_index=best, w=W[:, best, :-1].mean(0),
               w_reps=W[:, best, :-1], n_trials=len(y), n_train=tr.shape[1], n_test=te.shape[1],
               mu=mu, sd=sd)
    for name, (Xo, kind) in (test_sets or {}).items():
        wb = W[:, best]
        if kind == "same_trials":
            res = np.stack([((Xo[b] @ wb[r, :-1] + wb[r, -1]) > 0) == y[b][:, None].astype(bool)
                            for r, (_, b) in enumerate(sp)]).mean(1)          # (R, bins)
            out[name] = 100 * res
        else:
            Xo_, yo = Xo
            pr = ((Xo_ @ wb[:, :-1].T) + wb[:, -1]) > 0                       # (trials, R)
            out[name] = 100 * (pr == yo[:, None].astype(bool)).mean(0)        # (R,)
            yp = np.stack([rng.permutation(yo) for _ in range(n_reps)], 1).astype(bool)
            out[name + "_shfl"] = 100 * (pr == yp).mean(0)
    return out


def pseudo_population(X: np.ndarray, y: np.ndarray, rng) -> np.ndarray:
    """Shuffle trial order independently for each neuron within each choice (Methods, Figure 7)."""
    Xp = X.copy()
    for v in np.unique(y):
        idx = np.where(y == v)[0]
        for j in range(X.shape[1]):
            Xp[idx, j] = X[rng.permutation(idx), j]
    return Xp


def ttest(a, b):
    """Unpaired two-tailed t-test, NaNs dropped; returns (t, p, n_a, n_b)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    if len(a) < 2 or len(b) < 2:
        return np.nan, np.nan, len(a), len(b)
    t, p = stats.ttest_ind(a, b)
    return float(t), float(p), len(a), len(b)


def angle(u, v):
    """Angle in degrees between two weight vectors."""
    c = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return float(np.degrees(np.arccos(np.clip(c, -1, 1))))


def early_late(dates, performance) -> dict:
    """Early and late training days of one mouse (Methods, "Learning analysis"; claims file,
    fig8de-learning-parallel): performance below the 20th or above the 80th percentile of all
    its days. Reading "a": every such day (code, perc_thb = [20, 80]); reading "b": only the run
    of such days at the start (early) or at the end (late) of training. Returns boolean masks in
    the order of the inputs."""
    dates = np.asarray(dates)
    perf = np.asarray(performance, float)
    order = np.argsort(dates)
    lo, hi = np.nanpercentile(perf, 20), np.nanpercentile(perf, 80)
    early_a, late_a = perf < lo, perf > hi
    early_b = np.zeros(len(perf), bool)
    late_b = np.zeros(len(perf), bool)
    for k in order:
        if not early_a[k]:
            break
        early_b[k] = True
    for k in order[::-1]:
        if not late_a[k]:
            break
        late_b[k] = True
    return {"a": (early_a, late_a), "b": (early_b, late_b), "thresholds": (lo, hi)}


def align_bins(arrays, i1s, axis=0):
    """Stack per-session arrays on the bins all sessions share, counted from the event: offset -1
    is the bin before the event. Returns the stack (sessions first) and the offsets."""
    lo = min(i1 + 1 for i1 in i1s)
    hi = min(a.shape[axis] - (i1 + 1) for a, i1 in zip(arrays, i1s))
    out = np.stack([np.take(a, np.arange(i1 + 1 - lo, i1 + 1 + hi), axis=axis) for a, i1 in zip(arrays, i1s)])
    return out, np.arange(-lo, hi)

