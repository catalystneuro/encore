"""Linear (STRF) and linear-nonlinear encoding models on Wehr's recordings in CRCNS ac-1.

Paper: Asari and Zador (2009), Methods, "Neural encoding models" and "Model performance"
(Eqs. 46 to 53), and the claim fig4-strf-performance-low in claims/asari-2009.yaml.

Where each parameter comes from:

- Stimulus sampling rate: `param.sf` of each stimulus file (wehr/Stimuli), 97656 Hz where absent.
- Spectrogram (Eq. 47): log-frequency bins at 3 per octave from 0.40 kHz (17 bins, to 20.3
  kHz; the paper says 0.40 to 22 kHz, 17 bins), dB of the power; each frequency centred over
  time, as in the authors' STRFanalysis.m (wehr/Tools in crcns-ac1.zip). The window h(t) is open:
  Hann windows of 10 and 20 ms are the readings the claim names.
- Time bins of 2^k ms for k = 2 to 10, 45 bins per model split as [45], [9, 36], [9, 8, 28], ...,
  [9, 8, ..., 1], giving windows of 180 to 4052 ms and 765 parameters (Methods).
- Response: the membrane potential, median filtered over 10 ms to clip spikes (Methods,
  Analysis, as for the A1 data), averaged in 4-ms bins (the finest time bin; a reading the claim
  names), each trial centred over time.
- Ridge regression (Eq. 50) with 10-fold cross-validation, the ridge parameter chosen as the one
  with the best mean validation performance over folds (Methods; STRFanalysis.m). The grid of
  ridge values (17 values, 1e-4 to 1e4 times the mean eigenvalue of S'S) is a standard choice;
  the chosen value is reported with its position in the grid, and the grid was widened from
  1e2 after the first round found the top value chosen in 36 of 208 fits. Folds are
  contiguous blocks of the concatenated data (reading A) or whole stimuli (reading B).
- Static nonlinearity (Eq. 51): robust lowess with a 5% span and 5 iterations on the training set,
  applied to the validation set by linear interpolation (Methods).
- Performance (Eq. 53): (total power - error power) / predictable power (Eq. 52), with the
  predictable power estimated from the trials of each stimulus, on the training set (upper) and
  the validation set (lower).
"""
from __future__ import annotations

import numpy as np
from scipy import ndimage
from statsmodels.nonparametric.smoothers_lowess import lowess

import ctxdep as cd

DT = 0.004                     # s, finest time bin (2^2 ms)
F_LO, NB_OCT, NF = 400.0, 3, 17
COUNTS = [[45], [9, 36], [9, 8, 28], [9, 8, 7, 21], [9, 8, 7, 6, 15], [9, 8, 7, 6, 5, 10],
          [9, 8, 7, 6, 5, 4, 6], [9, 8, 7, 6, 5, 4, 3, 3], [9, 8, 7, 6, 5, 4, 3, 2, 1]]
WIDTHS = [2 ** k for k in range(0, 9)]       # in 4-ms units: 4, 8, ..., 1024 ms
RIDGE_SCALE = np.logspace(-4, 4, 17)


def window_ms(counts) -> int:
    return int(sum(c * w * 4 for c, w in zip(counts, WIDTHS)))


def lag_bins(counts):
    """(start lag, width) in 4-ms units for each of the 45 bins, from near to distant past."""
    out, a = [], 0
    for c, w in zip(counts, WIDTHS):
        for _ in range(c):
            out.append((a, w))
            a += w
    return out


def spectrogram(x: np.ndarray, sf: float, win_ms: float) -> np.ndarray:
    """dB power in 17 log-frequency bins, one frame every 4 ms (frame centred on the bin)."""
    L = int(round(win_ms / 1000 * sf))
    nfft = int(2 ** np.ceil(np.log2(L)))
    w = np.hanning(L)
    n = int(len(x) / sf / DT)
    xp = np.concatenate([np.zeros(L), x, np.zeros(L)])
    centres = (np.arange(n) * DT + DT / 2) * sf + L
    idx = (centres[:, None] - L // 2 + np.arange(L)[None, :]).astype(int)
    P = np.abs(np.fft.rfft(xp[idx] * w, nfft, axis=1)) ** 2
    f = np.fft.rfftfreq(nfft, 1 / sf)
    edges = F_LO * 2 ** (np.arange(NF + 1) / NB_OCT)
    S = np.stack([P[:, (f >= edges[i]) & (f < edges[i + 1])].sum(axis=1) for i in range(NF)], axis=1)
    S = 10 * np.log10(S + S.max() * 1e-8)
    return S - S.mean(axis=0, keepdims=True)


def response_bins(trace: np.ndarray, sf: float, n: int) -> np.ndarray:
    """10-ms median filter, mean in 4-ms bins, centred."""
    v = ndimage.median_filter(trace.astype(float), size=int(round(0.010 * sf)))
    k = int(round(DT * sf))
    v = v[: n * k].reshape(-1, k).mean(axis=1)
    return v - v.mean()


def design(S: np.ndarray, counts) -> np.ndarray:
    """Lagged features: mean of the spectrogram over each lag bin before (and including) t."""
    n = S.shape[0]
    bins = lag_bins(counts)
    maxlag = max(a + w for a, w in bins)
    Sp = np.concatenate([np.zeros((maxlag, S.shape[1])), S])
    C = np.concatenate([np.zeros((1, S.shape[1])), np.cumsum(Sp, axis=0)])
    t = np.arange(n) + maxlag + 1             # index after time t in C
    X = np.empty((n, len(bins) * S.shape[1]), np.float32)
    for j, (a, w) in enumerate(bins):
        X[:, j * S.shape[1]:(j + 1) * S.shape[1]] = (C[t - a] - C[t - a - w]) / w
    return X


def performance(R_list, rhat, idx_list):
    """Eq. 53 over the time points idx of each stimulus; R_list holds (trials, T) arrays."""
    tot = err = pred = 0.0
    n = 0
    for R, rh, idx in zip(R_list, rhat, idx_list):
        if len(idx) == 0:
            continue
        Rs = R[:, idx]
        m = Rs.shape[0]
        tot += (Rs ** 2).mean(axis=0).sum()
        err += ((Rs - rh[idx]) ** 2).mean(axis=0).sum()
        pred += ((m * Rs.mean(axis=0) ** 2 - (Rs ** 2).mean(axis=0)) / (m - 1)).sum()
        n += len(idx)
    return (tot - err) / pred, pred / n


def fit_cell(stims, counts, folds: str = "blocks", nfold: int = 10, ln: bool = True):
    """stims: list of (S spectrogram (T, 17), R trials (m, T)). Returns performances."""
    Xs = [design(S, counts) for S, _ in stims]
    ys = [R.mean(axis=0) for _, R in stims]
    lens = [len(y) for y in ys]
    off = np.concatenate([[0], np.cumsum(lens)])
    X = np.concatenate(Xs).astype(np.float64)
    y = np.concatenate(ys)
    N = len(y)
    if folds == "blocks":
        edges = np.linspace(0, N, nfold + 1).astype(int)
        fold_of = np.searchsorted(edges, np.arange(N), side="right") - 1
    else:
        order = np.arange(len(stims)) % nfold
        fold_of = np.concatenate([np.full(L, order[i]) for i, L in enumerate(lens)])
    XtX = X.T @ X
    Xty = X.T @ y
    lam0 = np.trace(XtX) / X.shape[1]
    res = {s: dict(tr=[], va=[]) for s in RIDGE_SCALE}
    W_all = {}
    for k in range(nfold):
        v = fold_of == k
        if not v.any():
            continue
        A = XtX - X[v].T @ X[v]
        b = Xty - X[v].T @ y[v]
        ev, U = np.linalg.eigh(A)
        Ub = U.T @ b
        for s in RIDGE_SCALE:
            w = U @ (Ub / (ev + s * lam0))
            W_all[(k, s)] = w
            rh = X @ w
            rh_list = [rh[off[i]:off[i + 1]] for i in range(len(stims))]
            va_idx = [np.where(v[off[i]:off[i + 1]])[0] for i in range(len(stims))]
            tr_idx = [np.where(~v[off[i]:off[i + 1]])[0] for i in range(len(stims))]
            res[s]["va"].append(performance([R for _, R in stims], rh_list, va_idx)[0])
            res[s]["tr"].append(performance([R for _, R in stims], rh_list, tr_idx)[0])
    best = max(RIDGE_SCALE, key=lambda s: np.mean(res[s]["va"]))
    out = dict(window_ms=window_ms(counts), ridge_scale=best, ridge_pos=int(np.where(RIDGE_SCALE == best)[0][0]),
               lin_va=float(np.mean(res[best]["va"])), lin_tr=float(np.mean(res[best]["tr"])))
    if ln:
        va_l, tr_l = [], []
        for k in range(nfold):
            v = fold_of == k
            if not v.any():
                continue
            rh = X @ W_all[(k, best)]
            fit = lowess(y[~v], rh[~v], frac=0.05, it=5, delta=0.005 * np.ptp(rh[~v]), return_sorted=True)
            xs, ix = np.unique(fit[:, 0], return_index=True)
            g = np.interp(rh, xs, fit[ix, 1])
            g_list = [g[off[i]:off[i + 1]] for i in range(len(stims))]
            va_idx = [np.where(v[off[i]:off[i + 1]])[0] for i in range(len(stims))]
            tr_idx = [np.where(~v[off[i]:off[i + 1]])[0] for i in range(len(stims))]
            va_l.append(performance([R for _, R in stims], g_list, va_idx)[0])
            tr_l.append(performance([R for _, R in stims], g_list, tr_idx)[0])
        out.update(ln_va=float(np.mean(va_l)), ln_tr=float(np.mean(tr_l)))
    return out


def load_cell(cell: dict, stim_cache: dict, win_ms: float, min_trials: int = 2):
    """Natural sound trials of one Wehr cell, grouped by stimulus; stimuli with >= min_trials."""
    groups = {}
    for f, d in zip(cell["files"], cell["descriptions"]):
        if not d.startswith("natural sound"):
            continue
        groups.setdefault(d.split(": Trial")[0], []).append(f)
    stims = []
    for desc, files in groups.items():
        if len(files) < min_trials:
            continue
        key = (desc, win_ms)
        if key not in stim_cache:
            stim_cache[key] = None
        trials, sf, sdesc = [], None, None
        for f in files:
            m = cd.loadmat_member("crcns-ac1.zip", "wehr/" + f)
            tr = np.atleast_1d(m["triggers"])[0]
            sf = float(m["response"].sf)
            x = m["response"].trace.astype(float) * float(getattr(m["response"], "scale", 1.0))
            on = int(tr.time) - 1
            dur = float(tr.param.duration) / 1000
            sdesc = str(tr.param.description)
            trials.append((x[on:], dur))
        if stim_cache[key] is None:
            stim_cache[key] = spectrogram(STIMULI[sdesc], STIM_SF.get(sdesc, 97656.0), win_ms)
        S = stim_cache[key]
        n = min([S.shape[0]] + [int(len(x) / sf / DT) for x, _ in trials])
        R = np.array([response_bins(x, sf, n) for x, _ in trials])
        stims.append((S[:n], R))
    return stims


STIMULI: dict = {}


def load_stimuli():
    """All Wehr stimulus waveforms, by description."""
    z = cd.open_zip("crcns-ac1.zip")
    for n in z.namelist():
        if n.startswith("wehr/Stimuli/") and n.endswith(".mat"):
            s = cd.loadmat_member("crcns-ac1.zip", n)["stimulus"]
            STIMULI[str(s.param.description)] = np.asarray(s.samples, float)
            if getattr(s.param, "sf", None) is not None:
                STIM_SF[str(s.param.description)] = float(s.param.sf)
    return STIMULI


STIM_SF: dict = {}
