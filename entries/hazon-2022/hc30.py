"""Loading and measures for CRCNS hc-30 (Hazon et al. 2022, Nat Commun 13:4276).

Sources of each parameter are given as:
  [claims]  the claims file claims/hazon-2022.yaml (its "common method" header or a criterion),
            which cites the paper's Methods or its code (github.com/approbatory/ML-project at
            commit 2057af9facfd3035c573e1254bdc32ed4781ba60);
  [paper]   a passage of the paper taken by the author (protocol, author step 1.6);
  [code]    the paper's code at that commit, cited by file, where the paper is silent;
  [assumed] an assumption, with the reason;
  [standard] a standard choice for a detail that cannot change a result.
"""
import io
import time

import fsspec
import numpy as np
import scipy.io
import scipy.sparse
from scipy.signal import lfilter

DATASET = "hc-30"
VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md); the MD5 pins the file
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-30/live/event_traces.mat"
MD5 = "fe0f5dd2fca6d64dbf0cd3f35e31e1f0"  # from hc-30/live/checksums.md5

FS = 20.0  # Hz [paper] Methods, Analysis of behavioral data, "20 frames per second"
TRACK_CM = 118.0  # [claims] common method, code DecodeTensor.default_opt total_length
CUTOFF_P = 5  # percentile [claims] common method
V_THRESH = 4.0  # cm/s [claims] common method; Methods, Data preprocessing
LEEWAY = 1 / 20  # [claims] common method, code default_opt leeway_frac
N_BINS = 20  # [claims] common method
BIN_CM = TRACK_CM / N_BINS  # 5.9 cm, [claims] common method (code bin_width)


def load_sessions(url=URL):
    """Stream event_traces.mat from the bucket into memory and return a list of sessions.

    Each session is a dict with mouse, session_id, events (frames x neurons, CSC sparse, the
    event onsets with their amplitudes, as the data descriptor says) and position (pixels).
    """
    t0 = time.time()
    with fsspec.open(url, block_size=2**22) as f:
        raw = f.read()
    import hashlib
    md5 = hashlib.md5(raw).hexdigest()
    m = scipy.io.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)
    del raw
    out = []
    for e in m["event_traces"]:
        out.append(dict(mouse=str(e.mouse_name), session_id=str(e.session_ID),
                        events=scipy.sparse.csc_matrix(e.traces),
                        position=np.asarray(e.position, dtype=float)))
    return out, md5, time.time() - t0


def alpha_kernel():
    """alpha(t) = (t/tau) exp(1 - t/tau), tau = 0.2 s, sampled at 20 Hz from 0.05 to 1.5 s.

    [paper] Methods, Event detection algorithm, last two steps; [code] DecodeTensor.tensor_loader
    ('HD_gamma': linspace(0, 7.5, 31)(2:end) in units of tau, causal 'full' convolution).
    """
    t = np.arange(1, 31) * 0.05 / 0.2
    return t * np.exp(1 - t)


def event_trace(events):
    """Convolve the event onsets with the alpha kernel (causal) and divide each trace by its
    standard deviation. [paper] Methods, Event detection algorithm ("Finally, we divided each
    event trace by its own standard deviation"); [code] tensor_loader, X ./ (std(X) + eps)."""
    X = events.toarray()
    Y = lfilter(alpha_kernel(), [1.0], X, axis=0)
    sd = Y.std(axis=0, ddof=1)
    return Y / (sd + np.finfo(float).eps)


def select_trials(position, n_bins=N_BINS):
    """Trials as in [claims] common method (code DecodeTensor.new_sel).

    Returns dict with cpp (cm per pixel), vel (cm/s), starts and ends (inclusive frame indices,
    0-based, as MATLAB's find(diff(...)) gives them), direction (+1 rightward, -1 leftward),
    bins (0..n_bins-1 per frame, clamped), and the counts before the bin filter.
    """
    x = position
    lo, hi = np.percentile(x, CUTOFF_P), np.percentile(x, 100 - CUTOFF_P)
    rng = hi - lo
    cpp = TRACK_CM / rng
    vel = np.concatenate([[0.0], np.diff(x)]) * cpp * FS
    fast = (np.abs(vel) > V_THRESH).astype(int)
    d = np.diff(fast)
    starts = np.where(d == 1)[0]
    ends = np.where(d == -1)[0]
    starts = starts[:len(ends)]
    n_runs = len(starts)
    b = lo + rng * LEEWAY
    t = hi - rng * LEEWAY
    sc, ec = x[starts], x[ends]
    regular = ((sc < b) & (ec > t)) | ((ec < b) & (sc > t))
    starts, ends = starts[regular], ends[regular]
    direction = np.where(x[starts] < b, 1, -1)
    bins = np.ceil(n_bins * (x - lo) / rng).astype(int)
    bins = np.clip(bins, 1, n_bins) - 1
    keep = np.array([len(np.unique(bins[s:e + 1])) == n_bins for s, e in zip(starts, ends)],
                    dtype=bool)
    return dict(cpp=cpp, vel=vel, lo=lo, hi=hi, n_fast_runs=n_runs, n_regular=int(regular.sum()),
                starts=starts[keep], ends=ends[keep], direction=direction[keep], bins=bins)


def build_tensor(X, tr, n_bins=N_BINS):
    """Tensor (neurons, bins, trials) of the mean event trace over each trial's frames in each
    bin. [paper] Methods, Data preprocessing ("mean event trace value for neuron n, during trial
    t, from all the frames where the mouse was in spatial bin k"); [code] construct_tensor."""
    starts, ends, bins = tr["starts"], tr["ends"], tr["bins"]
    T = np.zeros((X.shape[1], n_bins, len(starts)))
    for i, (s, e) in enumerate(zip(starts, ends)):
        bb = bins[s:e + 1]
        seg = X[s:e + 1]
        cnt = np.bincount(bb, minlength=n_bins)
        sums = np.zeros((n_bins, X.shape[1]))
        np.add.at(sums, bb, seg)
        T[:, :, i] = (sums / cnt[:, None]).T
    return T


def session_tensor(sess, n_bins=N_BINS):
    tr = select_trials(sess["position"], n_bins)
    X = event_trace(sess["events"])
    return build_tensor(X, tr, n_bins), tr["direction"], tr


def shuffle_tensor(T, d, rng):
    """Permute each neuron's values across trials, independently within each bin and direction.
    [claims] common method (code shuffle_tensor)."""
    S = T.copy()
    for dirn in (1, -1):
        idx = np.where(d == dirn)[0]
        n = len(idx)
        if n == 0:
            continue
        S[:, :, idx] = rng.permuted(T[:, :, idx], axis=2)
    return S


def equalize_trials(d, rng, n_per_dir=None):
    """Random equal numbers of rightward and leftward trials (the smaller count); [claims]
    common method (code cut_tensor). Returns sorted trial indices."""
    r, l = np.where(d == 1)[0], np.where(d == -1)[0]
    n = min(len(r), len(l)) if n_per_dir is None else n_per_dir
    return np.sort(np.concatenate([rng.permutation(r)[:n], rng.permutation(l)[:n]]))


def half_split(d, rng):
    """Random half of each direction's trials (code holdout_half: randperm <= n/2)."""
    first = np.zeros(len(d), dtype=bool)
    for dirn in (1, -1):
        idx = np.where(d == dirn)[0]
        first[rng.permutation(idx)[:len(idx) // 2]] = True
    return first


def to_dataset(T, d):
    """Samples (bin x trial) by neurons with class labels 0..39; class 2*b for rightward and
    2*b+1 for leftward (code tensor2dataset: 2b - (dir == 1), 1-based); position = class // 2."""
    N, K, Tn = T.shape
    X = T.transpose(2, 1, 0).reshape(Tn * K, N)
    y = (2 * np.tile(np.arange(K), Tn) + np.repeat(d != 1, K).astype(int))
    return X, y


class OvOLinearSVM:
    """One-vs-one linear SVMs with voting over the 40 classes.

    [claims] common method: fitcecoc one-vs-one of linear SVMs (templateLinear, lasso, Lambda
    0, SpaRSA). [assumed] Implemented with libsvm (scikit-learn SVC, linear kernel on a
    precomputed Gram matrix), L2-regularized hinge loss with a large C (default 100) to
    approximate the code's unregularized fit, and majority voting (MATLAB's default is
    loss-weighted decoding). The MATLAB solver is not available here; the decoder's C is shown
    as a variant in the notebook.
    """

    def __init__(self, C=100.0):
        self.C = C

    def fit(self, X, y):
        from sklearn.svm import SVC
        self.Xtr = X
        self.m = SVC(kernel="precomputed", C=self.C, decision_function_shape="ovo",
                     cache_size=50, tol=1e-3)
        self.m.fit(X @ X.T, y)
        return self

    def predict(self, X):
        return self.m.predict(X @ self.Xtr.T)


def decode_once(T, d, rng, shuffled, C=100.0, return_pred=False):
    """Two-fold decoding of one random trial split ([claims] common method, code decode_all).

    Returns the two-fold MSE in cm^2 (bin error times 5.9 cm, squared, averaged over the two
    folds) and optionally the true and predicted classes of all test samples."""
    first = half_split(d, rng)
    halves = []
    for sel in (first, ~first):
        Th, dh = T[:, :, sel], d[sel]
        if shuffled:
            Th = shuffle_tensor(Th, dh, rng)
        halves.append(to_dataset(Th, dh))
    mses, ys, ps = [], [], []
    for a, b in ((0, 1), (1, 0)):
        Xa, ya = halves[a]
        Xb, yb = halves[b]
        p = OvOLinearSVM(C).fit(Xa, ya).predict(Xb)
        err = (yb // 2 - p // 2) * BIN_CM
        mses.append(np.mean(err ** 2))
        ys.append(yb)
        ps.append(p)
    if return_pred:
        return float(np.mean(mses)), np.concatenate(ys), np.concatenate(ps)
    return float(np.mean(mses))


# ---- signal and noise ----

def _unit(v):
    return v / (np.linalg.norm(v) + np.finfo(float).eps)


def adjacent_signal_noise(T, d, rng):
    """One random half split; per direction and adjacent bin pair (38), the signal and noise
    along the training half's signal direction measured on the test half, unshuffled and
    shuffled ([claims] common method; Methods, Analyzing signal and noise, paragraphs 2 and 3;
    code DecodeTensor.adjacent_metrics rows 'm', columns 'se', 'ce', 'ue').

    Returns arrays (38,) signal, noise, noise_shuffled ordered [dir -1 pairs 0..18, dir +1
    pairs 0..18]; pair k joins bin k and k+1 in track coordinates."""
    first = half_split(d, rng)
    T1, d1, T2, d2 = T[:, :, first], d[first], T[:, :, ~first], d[~first]
    T2s = shuffle_tensor(T2, d2, rng)
    K = T.shape[1]
    sig, noi, nois = [], [], []
    for dirn in (-1, 1):
        A1 = T1[:, :, d1 == dirn]
        A2 = T2[:, :, d2 == dirn]
        A2s = T2s[:, :, d2 == dirn]
        m1 = A1.mean(axis=2)
        m2 = A2.mean(axis=2)
        for k in range(K - 1):
            w = _unit(m1[:, k + 1] - m1[:, k])
            sig.append(np.dot(w, m2[:, k + 1] - m2[:, k]) ** 2)
            p0, p1 = w @ A2[:, k, :], w @ A2[:, k + 1, :]
            noi.append((p0.var(ddof=1) + p1.var(ddof=1)) / 2)
            q0, q1 = w @ A2s[:, k, :], w @ A2s[:, k + 1, :]
            nois.append((q0.var(ddof=1) + q1.var(ddof=1)) / 2)
    return np.array(sig), np.array(noi), np.array(nois)


def ensemble_sizes(n_total, step=10):
    """Sizes 1 (or 2), step, 2*step, ..., and all neurons (code decode_series)."""
    s = list(range(step, n_total + 1, step))
    if not s or s[-1] != n_total:
        s.append(n_total)
    return s


def fit_line(n, y, cutoff=100):
    """Unweighted least-squares line through (n, y) for n >= cutoff ([claims] common method,
    code Utils.fitaline). Returns slope, intercept, R squared."""
    n, y = np.asarray(n, float), np.asarray(y, float)
    s = n >= cutoff
    A = np.vstack([n[s], np.ones(s.sum())]).T
    coef, *_ = np.linalg.lstsq(A, y[s], rcond=None)
    pred = A @ coef
    ss = ((y[s] - y[s].mean()) ** 2).sum()
    r2 = 1 - ((y[s] - pred) ** 2).sum() / ss if ss > 0 else np.nan
    return coef[0], coef[1], r2


def fit_imse(n, imse):
    """IMSE(n) = I0 n / (1 + n/N), unweighted nonlinear least squares from I0 = 1, N = 100, no
    bounds ([claims] fig2ef criterion, code createFit_infoSaturation.m). Returns I0, N, and
    the 95% half-intervals from the Jacobian (nan when the fit fails)."""
    from scipy.optimize import curve_fit
    f = lambda x, I0, N: I0 * x / (1 + x / N)
    try:
        p, cov = curve_fit(f, np.asarray(n, float), np.asarray(imse, float), p0=[1.0, 100.0],
                           maxfev=20000)
        ci = 1.96 * np.sqrt(np.diag(cov))
        return p[0], p[1], ci[0], ci[1]
    except Exception:
        return np.nan, np.nan, np.nan, np.nan


def nsv(T, d):
    """Normalized signal variance per session: per direction and adjacent bin pair, the
    variance over neurons of the squared elements of the unit vector of the difference of the
    two bins' trial-mean responses; mean over the 38 pairs. [claims] fig5f criterion (Methods,
    Definition of the NSV; code load_definitions.m line 43)."""
    vals = []
    for dirn in (-1, 1):
        m = T[:, :, d == dirn].mean(axis=2)
        for k in range(T.shape[1] - 1):
            u = _unit(m[:, k + 1] - m[:, k])
            vals.append(np.var(u ** 2))
    return float(np.mean(vals))


# ---- per-session measures used by several claims ----

def signal_noise_series(T, d, seed, n_subsets=20, step=10):
    """Signal and noise against ensemble size for one session ([claims] common method: sizes 2,
    10, 20, ... all; 80 subsets in the paper, n_subsets here; each subset a new trial split;
    equal numbers of trials per direction, code cut_tensor).

    Returns sizes, and arrays (sizes, 38) of the subset-averaged per-pair signal, noise and
    shuffled noise, and arrays (sizes,) of the subset-averaged median over pairs (code
    res_lookup: median over pairs per subset, then mean over subsets)."""
    rng = np.random.default_rng(seed)
    N = T.shape[0]
    sizes = [2] + ensemble_sizes(N, step)
    P = np.zeros((3, len(sizes), 38))
    M = np.zeros((3, len(sizes)))
    for i, n in enumerate(sizes):
        for _ in range(n_subsets):
            idx = equalize_trials(d, rng)
            sub = rng.choice(N, n, replace=False)
            s, c, u = adjacent_signal_noise(T[sub][:, :, idx], d[idx], rng)
            for j, v in enumerate((s, c, u)):
                P[j, i] += v / n_subsets
                M[j, i] += np.median(v) / n_subsets
    return np.array(sizes), P, M


def slope_with_se(n, y, cutoff=100):
    """Slope of an unweighted line fit at n >= cutoff, with its standard error."""
    n, y = np.asarray(n, float), np.asarray(y, float)
    s = n >= cutoff
    x, yy = n[s], y[s]
    if len(x) < 3:
        return np.nan, np.nan
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, yy, rcond=None)
    resid = yy - A @ coef
    s2 = (resid ** 2).sum() / (len(x) - 2)
    se = np.sqrt(s2 / ((x - x.mean()) ** 2).sum())
    return coef[0], se


def noise_pairs_by_peak_distance(T, d, rng):
    """Mean noise correlation per place-field peak distance (bins 0..19) for one session, per
    direction, unshuffled and shuffled ([claims] fig1d criterion; code DecodeTensor.corr_values:
    residuals from the class mean over all trials of that direction, Pearson correlation per
    bin; averaged over the 20 bins). Returns dict direction -> (sum_u, sum_s, count) over
    distance (pairs i < j), and the pooled pair values for the pooled reading."""
    S = shuffle_tensor(T, d, rng)
    out = {}
    for dirn in (1, -1):
        A, B = T[:, :, d == dirn], S[:, :, d == dirn]
        N, K, _ = A.shape
        Cu = np.zeros((N, N))
        Cs = np.zeros((N, N))
        nb = np.zeros((N, N))
        for k in range(K):
            for X, C in ((A[:, k, :], Cu), (B[:, k, :], Cs)):
                with np.errstate(invalid="ignore", divide="ignore"):
                    c = np.corrcoef(X)
                C += np.nan_to_num(c)
            ok = (A[:, k, :].std(axis=1) > 0) & (B[:, k, :].std(axis=1) > 0)
            nb += np.outer(ok, ok)
        with np.errstate(invalid="ignore", divide="ignore"):
            Cu, Cs = Cu / nb, Cs / nb
        peak = A.mean(axis=2).argmax(axis=1)
        iu = np.triu_indices(N, 1)
        dist = np.abs(peak[:, None] - peak[None, :])[iu]
        cu, cs = Cu[iu], Cs[iu]
        good = np.isfinite(cu) & np.isfinite(cs)
        out[dirn] = (dist[good], cu[good], cs[good])
    return out


def jitter(position, tr):
    """Position measurement noise of one session ([claims] position-measurement-noise; code
    estimate_position_jitter.m): frames from the first in bin 7 to the last in bin 13 of each
    trial, in the run's direction; even frames (1-based) fit a line, residuals of odd frames;
    robust scale IQR / 1.349 of all residuals."""
    devs = []
    cpp, bins = tr["cpp"], tr["bins"] + 1  # 1-based bins
    for s, e, dirn in zip(tr["starts"], tr["ends"], tr["direction"]):
        b = bins[s:e + 1]
        pos = cpp * position[s:e + 1]
        first, last = (7, 13) if dirn == 1 else (13, 7)
        i0 = np.where(b == first)[0]
        i1 = np.where(b == last)[0]
        if len(i0) == 0 or len(i1) == 0 or i1[-1] < i0[0]:
            continue
        fr = np.arange(i0[0], i1[-1] + 1) + 1  # 1-based frame index within trial
        rp = pos[fr - 1]
        trn = fr % 2 == 0
        if trn.sum() < 4:
            continue
        a, c = np.polyfit(fr[trn], rp[trn], 1)
        devs.append((rp - (a * fr + c))[~trn])
    devs = np.concatenate(devs)
    q75, q25 = np.percentile(devs, [75, 25])
    return (q75 - q25) / (2 * np.sqrt(2) * 0.4769362762044699)  # erfinv(1/2)


def hwhm_bins(x):
    """Half-width at half maximum of a tuning curve in bins (code load_definitions.m
    one_hwhm)."""
    x = x - x.min()
    ix = int(np.argmax(x))
    h = x[ix] / 2
    pre, post = x[:ix + 1], x[ix:]
    lb = np.where(pre < h)[0]
    left = ix - lb[-1] if len(lb) else -np.inf
    rb = np.where(post < h)[0]
    right = rb[0] if len(rb) else -np.inf
    hw = max(left, right)
    if hw < 0:
        hw = round(len(x) / 2)
    return hw


def var_fwhm_cm(T, d):
    """Variance over neurons (both directions pooled) of the half-width at half maximum of each
    direction's mean tuning curve, times (2 x 5.9 cm)^2 ([claims] fig5f criterion; code
    load_definitions.m var_fwhm_cm, calc_var_hwhm)."""
    hw = []
    for dirn in (1, -1):
        mu = T[:, :, d == dirn].mean(axis=2)
        for row in mu:
            hw.append(np.nan if np.all(row == row[0]) else hwhm_bins(row))
    return np.nanvar(hw, ddof=1) * (2 * BIN_CM) ** 2


def class_clouds(T, d):
    """The 40 clouds (neurons x trials) in the code's order (Cloud.m: bins 1..20 of rightward
    trials, then 1..20 of leftward)."""
    out = []
    for dirn in (1, -1):
        A = T[:, :, d == dirn]
        for k in range(T.shape[1]):
            out.append(A[:, k, :])
    return out


def pca_dirs(X):
    """Principal directions (neurons x components) and eigenvalues of the covariance of the
    samples in the columns of X (MATLAB pca: centred, min(N, T-1) components)."""
    Xc = X - X.mean(axis=1, keepdims=True)
    U, s, _ = np.linalg.svd(Xc, full_matrices=False)
    k = min(X.shape[0], X.shape[1] - 1)
    return U[:, :k], (s[:k] ** 2) / (X.shape[1] - 1)


def overlap_measures(T, d, rng):
    """Per adjacent bin pair (38, code Cloud.m order): cos^2 of the unit signal direction with
    each noise eigenvector of the first bin's cloud, unshuffled and shuffled, for covariance and
    correlation (z-scored) clouds; and the per-pair quantities of Supplementary Table 2.
    [claims] fig4b criterion (code Cloud.m, load_definitions.m area_between)."""
    clouds = class_clouds(T, d)
    S = shuffle_tensor(T, d, rng)
    clouds_s = class_clouds(S, d)
    K = T.shape[1]
    rows = []
    for j in list(range(K - 1)) + list(range(K, 2 * K - 1)):
        mu0, mu1 = clouds[j].mean(axis=1), clouds[j + 1].mean(axis=1)
        dmu = mu1 - mu0
        u = _unit(dmu)
        r = {}
        for kind in ("cov", "corr"):
            for tag, C in (("u", clouds[j]), ("s", clouds_s[j])):
                X = C
                if kind == "corr":
                    sd = X.std(axis=1, ddof=1, keepdims=True)
                    X = (X - X.mean(axis=1, keepdims=True)) / np.where(sd > 0, sd, 1)
                V, lam = pca_dirs(X)
                c2 = (u @ V) ** 2
                r[f"{kind}_{tag}_cos2"] = c2
                r[f"{kind}_{tag}_lam"] = lam
        r["dmu2"] = dmu ** 2
        r["u2"] = u ** 2
        rows.append(r)
    return rows


# ---- decoding jobs ----

def decode_full(T, d, seed, reps, C=1.0):
    """All neurons, all equalised trials ([claims] fig2d criterion; code mean_rms_all_sess.mlx
    reads the 'max' neurons and 'max' trials rows): per repetition a new random trial split,
    unshuffled and shuffled two-fold decoding. Returns per-repetition MSE (cm^2) of each, the
    40 x 40 confusion counts of each over all test samples, and the sum and count of squared
    errors per true class."""
    rng = np.random.default_rng(seed)
    out = dict(mse_u=[], mse_s=[], conf_u=np.zeros((40, 40)), conf_s=np.zeros((40, 40)))
    for _ in range(reps):
        idx = equalize_trials(d, rng)
        for tag, sh in (("u", False), ("s", True)):
            mse, y, p = decode_once(T[:, :, idx], d[idx], rng, sh, C=C, return_pred=True)
            out[f"mse_{tag}"].append(mse)
            np.add.at(out[f"conf_{tag}"], (y, p), 1)
    return out


def decode_series(T, d, seed, sizes, reps, C=1.0):
    """IMSE against ensemble size ([claims] common method, code decode_series): for each size,
    `reps` random neuron subsets, each with new equalised trials and split; IMSE = 1/MSE per
    subset (MSE in cm^2), averaged over subsets. Returns arrays (sizes,) for unshuffled and
    shuffled."""
    rng = np.random.default_rng(seed)
    N = T.shape[0]
    iu, is_ = [], []
    for n in sizes:
        a, b = [], []
        for _ in range(reps):
            idx = equalize_trials(d, rng)
            sub = rng.choice(N, n, replace=False)
            Tc = T[sub][:, :, idx]
            a.append(1 / decode_once(Tc, d[idx], rng, False, C=C))
            b.append(1 / decode_once(Tc, d[idx], rng, True, C=C))
        iu.append(np.mean(a))
        is_.append(np.mean(b))
    return np.array(iu), np.array(is_)


def decode_bins(sess, n_bins, seed, reps, C=1.0):
    """Unshuffled decoding with all neurons and `n_bins` bins per direction; RMS error (cm)
    relative to the continuous position ([claims] suppl6 criterion): the true position of a
    sample is the mean position (cm, from the 5th percentile) over the trial's frames in the
    bin; the prediction is (a) the predicted bin's centre or (b) the mean true position of the
    training samples of the predicted class. Returns per-repetition RMS of (a) and (b), and the
    fraction of (trial, bin) samples with no frame.

    Trials are those of the 20-bin selection for every bin count, and a (trial, bin) sample with
    no frame is left out ([code] bin_integration_time_checker.m, which feeds Supplementary
    Figure 6: new_sel with the default 20 bins, then NaN samples dropped by tensor2dataset)."""
    tr = select_trials(sess["position"], N_BINS)
    rng_cm = tr["hi"] - tr["lo"]
    tr = dict(tr, bins=np.clip(np.ceil(n_bins * (sess["position"] - tr["lo"]) / rng_cm)
                               .astype(int), 1, n_bins) - 1)
    X = event_trace(sess["events"])
    with np.errstate(invalid="ignore", divide="ignore"):
        T = build_tensor(X, tr, n_bins)
        pos_cm = (sess["position"] - tr["lo"]) * tr["cpp"]
        Pt = build_tensor(pos_cm[:, None], tr, n_bins)[0]  # bins x trials
    d = tr["direction"]
    width = TRACK_CM / n_bins
    rng = np.random.default_rng(seed)
    ra, rb = [], []
    for _ in range(reps):
        idx = equalize_trials(d, rng)
        Tc, dc, Pc = T[:, :, idx], d[idx], Pt[:, idx]
        first = half_split(dc, rng)
        sq_a, sq_b = [], []
        for tr_sel, te_sel in ((first, ~first), (~first, first)):
            Xa, ya = to_dataset(Tc[:, :, tr_sel], dc[tr_sel])
            Xb, yb = to_dataset(Tc[:, :, te_sel], dc[te_sel])
            pa = Pc[:, tr_sel].T.reshape(-1)  # same order as to_dataset (trial-major)
            pb = Pc[:, te_sel].T.reshape(-1)
            ka, kb = np.isfinite(pa), np.isfinite(pb)
            Xa, ya, pa, Xb, yb, pb = Xa[ka], ya[ka], pa[ka], Xb[kb], yb[kb], pb[kb]
            p = OvOLinearSVM(C).fit(Xa, ya).predict(Xb)
            centre = (p // 2 + 0.5) * width
            cls_mean = np.array([pa[ya == c].mean() if (ya == c).any() else np.nan
                                 for c in range(2 * n_bins)])
            sq_a.append((centre - pb) ** 2)
            sq_b.append((cls_mean[p] - pb) ** 2)
        ra.append(np.sqrt(np.mean(np.concatenate(sq_a))))
        rb.append(np.sqrt(np.nanmean(np.concatenate(sq_b))))
    return np.array(ra), np.array(rb), float(np.mean(~np.isfinite(Pt)))


def performance(position, tr, cutoff_cm=5.9):
    """Task performance, correct over total runs ([claims] suppl8 criterion; code
    error_trial_counter.m): slow runs (speed below 4 cm/s) and turn-arounds between the two
    5.9 cm milestones count as errors; correct runs are the valid trials."""
    cpp, vel = tr["cpp"], tr["vel"]
    cm = (position - tr["lo"]) * cpp
    cm[cm < 0] = 0
    right_m = cutoff_cm
    left_m = (tr["hi"] - tr["lo"]) * cpp - cutoff_cm
    slow = np.abs(vel) < V_THRESH
    states = (cm > left_m) * 10 + (cm < right_m) * 1 + slow * 100
    n_slow = n_turn = 0
    state, was_slow = "none", False
    for s in states:
        if s == 101:
            if state == "leftward" and was_slow:
                n_slow += 1
            elif state == "rightward" and was_slow:
                n_turn += 1
            state, was_slow = "rightward", False
        elif s == 110:
            if state == "rightward" and was_slow:
                n_slow += 1
            elif state == "leftward" and was_slow:
                n_turn += 1
            state, was_slow = "leftward", False
        elif s == 100:
            was_slow = True
    n_correct = len(tr["starts"])
    return n_correct / (n_correct + n_slow + n_turn), n_slow, n_turn


def single_cell_snr(T, d):
    """Mean over neurons of the single-cell SNR ([claims] suppl11b criterion). Per neuron,
    per direction and adjacent bin pair: signal (difference of trial means)^2 and noise (mean of
    the two bins' trial variances). Main reading (Methods): median over pairs of signal over
    median over pairs of noise. Variants (code single_cell_d_primes2): mean, and median, of the
    per-pair ratio."""
    sig, noi = [], []
    for dirn in (-1, 1):
        A = T[:, :, d == dirn]
        sig.append(np.diff(A.mean(axis=2), axis=1) ** 2)
        v = A.var(axis=2, ddof=1)
        noi.append((v[:, :-1] + v[:, 1:]) / 2)
    sig, noi = np.concatenate(sig, axis=1), np.concatenate(noi, axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        main = np.median(sig, axis=1) / np.median(noi, axis=1)
        ratio = sig / noi
    return (np.nanmean(np.where(np.isfinite(main), main, np.nan)),
            np.nanmean(np.nanmean(np.where(np.isfinite(ratio), ratio, np.nan), axis=1)),
            np.nanmean(np.nanmedian(np.where(np.isfinite(ratio), ratio, np.nan), axis=1)))


def clock_check(sess, shift):
    """Mean absolute position error (cm) of a quick nearest-centroid decoder (class means of one
    random half of the trials, per direction; the bin of the nearest mean for each bin of each
    held-out trial), with the event trace shifted by `shift` frames (np.roll). A check that the
    event trace and the position share a clock (protocol, author step 2), not the paper's
    decoder."""
    tr = select_trials(sess["position"])
    X = event_trace(sess["events"])
    if shift:
        X = np.roll(X, shift, axis=0)
    T = build_tensor(X, tr)
    d = tr["direction"]
    first = half_split(d, np.random.default_rng(0))
    errs = []
    for dirn in (1, -1):
        A = T[:, :, first & (d == dirn)].mean(axis=2)
        B = T[:, :, ~first & (d == dirn)]
        for t in range(B.shape[2]):
            dist = ((B[:, :, t][:, :, None] - A[:, None, :]) ** 2).sum(axis=0)
            errs.append(np.abs(dist.argmin(axis=1) - np.arange(N_BINS)).mean())
    return float(np.mean(errs) * BIN_CM)
