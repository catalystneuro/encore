"""STRF and LN models of the Wehr whole-cell data in CRCNS ac-1 (crcns-ac1.zip, wehr/), for
fig4-strf-performance-low, following Asari & Zador (2009), Methods, "Neural encoding models" and
"Model performance" (Eqs. 46 to 53), and Wehr's tools in the data set (wehr/Tools: ViewResponse.m,
GetEvoked.m, STRFanalysis.m, ridgesvd1.m, logspectrogram.m) where the Methods leave a detail open.

Where a parameter comes from is said beside it, as in asari.py. Choices the paper and the code do
not fix (assumptions):
- the response is the 10-ms median-filtered membrane potential averaged in 4-ms bins (the finest
  time bin of the Methods; STRFanalysis.m resamples instead);
- the spectrogram has 17 frequencies, the first 17 of the 18 that logspectrogram.m gives for
  0.4 to 22.1 kHz at 3 per octave (the Methods give 17 bins and 765 parameters);
- lags before the sound onset see a zero (centred) spectrogram, so that every window length is fitted
  on the same response bins (STRFanalysis.m drops the first window of each stimulus);
- the ridge value is chosen per fold as the one with the smallest error on the validation fold,
  from 1e-10 to 1e2 times the largest eigenvalue of the training X'X (a grid wide enough that the
  best value is interior, standard choice; the choice on the validation fold is the Methods');
- folds are 10 contiguous blocks of the concatenated data, sized as in STRFanalysis.m;
- the static nonlinearity is a robust local-linear lowess (5% span, five robust iterations,
  Methods) fitted on the training folds and interpolated onto the validation fold.

Streams everything from the public bucket via asari.open_zip; nothing is written to disk.
"""
import functools

import numpy as np
from scipy import ndimage

import asari as A

DT = 0.004                    # s, time bin (Methods: finest lag bin, 2^2 ms)
FMIN, FMAX, DF = 400.0, 22100.0, 1 / 3   # Methods: 3 bins/octave, 0.40 to 22 kHz
EXCLUDE = ("tuning curve", "silence", "white noise")   # as ViewResponse.m
SMOOTH_MS = 10.0              # median filter window, ViewResponse.m default
# Methods: lag bins of 2^k ms, k = 2..10, 45 in all, split as [45, 0, ...], [9, 36, ...], ...,
# [9, 8, ..., 1]; the splits below give the stated windows of 180, 324, 548, 884, 1364, 2004, 2772,
# 3540 and 4052 ms (the notebook prints them)
WIDTHS_MS = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
MODELS = [[45], [9, 36], [9, 8, 28], [9, 8, 7, 21], [9, 8, 7, 6, 15], [9, 8, 7, 6, 5, 10],
          [9, 8, 7, 6, 5, 4, 6], [9, 8, 7, 6, 5, 4, 3, 3], [9, 8, 7, 6, 5, 4, 3, 2, 1]]


def _z():
    return A.open_zip("crcns-ac1.zip")


@functools.lru_cache(None)
def summary():
    """List of dicts, one per cell: exp (0/1), cell id, files, descriptions."""
    m = A.loadmat_bytes(_z().read("wehr/Summary.mat"))
    out = []
    for ei, ex in enumerate(m["experiment"]):
        for c in ex.cell:
            files = list(np.atleast_1d(c.file))
            out.append(dict(exp=ei, exp_description=ex.description, cell=files[0].split("/")[1],
                            files=files, descriptions=list(np.atleast_1d(c.description))))
    return out


def load_trial(path):
    """One result file -> (trace in mV at 4 kHz, sf, triggers struct, notes str)."""
    d = A.loadmat_bytes(_z().read("wehr/" + path))
    r = d["response"]
    x = r.trace.astype(float) * r.scale
    notes = " | ".join(s.strip() for s in np.atleast_1d(d["param"].notes) if s.strip())
    return x, int(r.sf), d["triggers"], notes


def frequencies():
    """logspectrogram.m grid for fmin=400, fmax=22100, df=1/3: 18 values, 400 Hz..20.3 kHz."""
    x = np.arange(0, np.fix(np.log2(FMAX / FMIN) / DF) * DF + 1e-9, DF)
    return FMIN * 2 ** x


def spectrogram(samples, sf, nbins, win_ms=10.0, nfreq=17):
    """Eq. 47: 20 log10 |STFT| with a Hann window of win_ms, evaluated at the logspectrogram.m
    frequencies (first nfreq of the 18), one column per 4-ms bin, column k centred on the
    centre of response bin k ((k + 0.5) * 4 ms). Samples outside the sound are zero.
    Returns (nfreq, nbins) array in dB."""
    f = frequencies()[:nfreq]
    N = int(round(win_ms / 1000 * sf))
    w = np.hanning(N + 2)[1:-1]   # MATLAB hann(N) is symmetric with nonzero ends
    centres = np.round((np.arange(nbins) + 0.5) * DT * sf).astype(int)
    starts = centres - N // 2
    pad = np.concatenate([np.zeros(N), samples, np.zeros(N + int(DT * sf) * 2 + N)])
    idx = starts[:, None] + N + np.arange(N)[None, :]
    E = np.exp(-2j * np.pi * np.outer(np.arange(N), f) / sf) * w[:, None]
    S = np.empty((nbins, len(f)), complex)
    for a in range(0, nbins, 2000):
        S[a:a + 2000] = pad[idx[a:a + 2000]] @ E
    return 20 * np.log10(np.abs(S).T + np.finfo(float).eps)


@functools.lru_cache(None)
def stimulus_samples(stim_file):
    """wehr/Stimuli/<stim_file> -> (samples float64, sf=97656)."""
    s = A.loadmat_bytes(_z().read("wehr/Stimuli/" + stim_file))["stimulus"]
    return np.asarray(s.samples, float).ravel(), int(s.param.sf)


def ramp(x, ramp_ms, sf):
    """MakeRamp.m: Hann on- and off-ramps of ramp_ms."""
    a = int(round(ramp_ms * sf / 1000))
    if a < 1:
        return x
    w = np.hanning(2 * a + 2)[1:-1]
    x = x.copy()
    x[:a] *= w[:a]
    x[-a:] *= w[a:]
    return x


def evoked(trace, sf, trig, smooth_ms=SMOOTH_MS):
    """GetEvoked.m: mean-removed 10-ms median filter (zero padded at the ends), then the
    segment from trigger time (1-based sample) for param.duration ms."""
    if smooth_ms > 0:
        mu = trace.mean()
        trace = ndimage.median_filter(trace - mu, size=int(round(smooth_ms / 1000 * sf)),
                                      mode="constant") + mu
    t0 = int(round(trig.time))           # 1-based start sample
    n = int(round(trig.param.duration * sf / 1000))
    return trace[t0 - 1:t0 - 1 + n]


def cell_data(cell, win_ms=10.0, nfreq=17, min_trials=2, smooth_ms=SMOOTH_MS):
    """For one cell (e.g. '20020508-mw-003') return a list of dicts, one per natural-sound
    stimulus with >= min_trials included trials (files noted 'Not included in the published
    results' are dropped), in order of first presentation:
      stim_file, description, S (nfreq x T dB spectrogram, 4-ms columns),
      R (trials x T membrane potential in mV, 10-ms median filtered, mean of each 4-ms bin).
    """
    info = next(c for c in summary() if c["cell"] == cell)
    groups = {}
    for f, d in zip(info["files"], info["descriptions"]):
        stim = d.split(": Trial No.")[0]
        if stim.lower() in EXCLUDE:
            continue
        x, sf, trig, notes = load_trial(f)
        if "Not included" in notes:
            continue
        ev = evoked(x, sf, trig, smooth_ms)
        nb = len(ev) // int(round(DT * sf))
        rb = ev[:nb * int(round(DT * sf))].reshape(nb, -1).mean(1)
        g = groups.setdefault(trig.file, dict(stim_file=trig.file, description=stim, trials=[],
                                              ramp=trig.param.ramp))
        g["trials"].append(rb)
    out = []
    for g in groups.values():
        if len(g["trials"]) < min_trials:
            continue
        T = min(len(t) for t in g["trials"])
        R = np.array([t[:T] for t in g["trials"]])
        smp, ssf = stimulus_samples(g["stim_file"])
        S = spectrogram(ramp(smp, g["ramp"], ssf), ssf, T, win_ms, nfreq)
        out.append(dict(stim_file=g["stim_file"], description=g["description"], S=S, R=R))
    return out


def lag_edges(counts):
    """Lag bin edges in 4-ms columns: list of (start, stop) column lags, lag 0 = current bin."""
    edges, a = [], 0
    for w, c in zip(WIDTHS_MS, counts):
        k = w // 4
        for _ in range(c):
            edges.append((a, a + k))
            a += k
    return edges


def design(S, counts):
    """Lagged design (T x nfreq*45, float32) for one centred spectrogram S (nfreq x T): each lag
    bin is the mean of the columns t-stop+1 .. t-start; columns before the sound are zero."""
    nf, T = S.shape
    edges = lag_edges(counts)
    L = edges[-1][1]
    C = np.zeros((T + L + 1, nf))
    C[L + 1:] = np.cumsum(S.T, 0)
    t = np.arange(T) + L + 1          # index of C after column t
    X = np.empty((T, len(edges), nf), np.float32)
    for j, (a, b) in enumerate(edges):
        X[:, j] = (C[t - a] - C[t - b]) / (b - a)
    return X.reshape(T, -1)


def lowess_fit(x, y, frac=0.05, iters=5, ngrid=200):
    """Robust local-linear lowess (tricube weights, bisquare robustness, `iters` robust
    iterations), evaluated on ngrid quantiles of x; returns (grid, fitted values)."""
    o = np.argsort(x)
    x, y = x[o], y[o]
    n = len(x)
    k = max(int(np.ceil(frac * n)), 3)
    grid = np.unique(np.quantile(x, np.linspace(0, 1, ngrid)))
    rw = np.ones(n)
    for it in range(iters + 1):
        fit = np.empty(len(grid))
        for i, g in enumerate(grid):
            c = np.searchsorted(x, g)
            lo, hi = max(0, c - k), min(n, c + k)
            xx, yy, ww = x[lo:hi], y[lo:hi], rw[lo:hi]
            d = np.abs(xx - g)
            h = np.partition(d, min(k, len(d)) - 1)[min(k, len(d)) - 1] + 1e-12
            w = np.clip(1 - (d / h) ** 3, 0, None) ** 3 * ww
            sw = w.sum()
            mx, my = (w * xx).sum() / sw, (w * yy).sum() / sw
            vx = (w * (xx - mx) ** 2).sum()
            beta = (w * (xx - mx) * (yy - my)).sum() / vx if vx > 1e-12 else 0.0
            fit[i] = my + beta * (g - mx)
        if it == iters:
            break
        res = y - np.interp(x, grid, fit)
        s = np.median(np.abs(res))
        rw = np.clip(1 - (res / (6 * s + 1e-12)) ** 2, 0, None) ** 2
    return grid, fit


def performance(rhat, ptot, rbar, ppred, idx):
    """Eq. 53 on bins idx, using per-bin P_total, trial mean, P_pred (Eq. 52):
    P_error per bin = P_total - 2 rhat <r_j> + rhat^2."""
    num, den = perf_terms(rhat, ptot, rbar, ppred, idx)
    return num / den


def perf_terms(rhat, ptot, rbar, ppred, idx):
    """Numerator (P_total - P_error) and denominator P_pred of Eq. 53 on bins idx."""
    perr = ptot[idx] - 2 * rhat[idx] * rbar[idx] + rhat[idx] ** 2
    return ptot[idx].mean() - perr.mean(), ppred[idx].mean()


def prepare(stims):
    """Centre spectrograms (per frequency, per stimulus) and responses (per trial, per stimulus);
    return centred S list and per-bin arrays (P_total, trial mean, P_pred) concatenated."""
    Sc, ptot, rbar, ppred = [], [], [], []
    for s in stims:
        Sc.append(s["S"] - s["S"].mean(1, keepdims=True))
        R = s["R"] - s["R"].mean(1, keepdims=True)
        m = R.shape[0]
        pt = (R ** 2).mean(0)
        rb = R.mean(0)
        ptot.append(pt)
        rbar.append(rb)
        ppred.append((m * rb ** 2 - pt) / (m - 1))
    return Sc, np.concatenate(ptot), np.concatenate(rbar), np.concatenate(ppred)


def strf_cv(stims, counts, nfold=10, ridge_rel=np.logspace(-10, 2, 37), ln=True):
    """Ridge STRF (Eq. 50) with nfold contiguous-block cross-validation for one lag model.
    The ridge value is chosen per fold as the one minimising the error power on that validation
    fold (same as maximising Eq. 53 there when P_pred > 0; grid: ridge_rel times the largest
    eigenvalue of the training X'X).
    Returns dict with per-fold arrays: strf_train, strf_valid, ln_train, ln_valid, ridge_index,
    filters (nfold x p, lag-major: index = lag_bin*nfreq + freq), and the means over folds
    (strf_upper/strf_lower/ln_upper/ln_lower), pooled versions (*_pooled: mean over folds of the
    numerator divided by mean over folds of P_pred), ridge_low_edge / ridge_high_edge counts,
    nbins, nparams."""
    Sc, ptot, rbar, ppred = prepare(stims)
    X = np.concatenate([design(S, counts) for S in Sc])
    y = rbar
    n, p = X.shape
    b = np.r_[np.round(np.full(nfold, n / nfold)).astype(int)]
    b[-1] += n - b.sum()
    bnd = np.r_[0, np.cumsum(b)]
    G = np.zeros((nfold, p, p))
    B = np.zeros((nfold, p))
    for k in range(nfold):
        Xk = X[bnd[k]:bnd[k + 1]].astype(float)
        G[k] = Xk.T @ Xk
        B[k] = Xk.T @ y[bnd[k]:bnd[k + 1]]
    Gs, Bs = G.sum(0), B.sum(0)
    res = {key: [] for key in ("strf_train", "strf_valid", "ln_train", "ln_valid", "ridge_index", "ridge", "filters",
                                "t_strf_train", "t_strf_valid", "t_ln_train", "t_ln_valid")}
    allidx = np.arange(n)
    for k in range(nfold):
        va = allidx[bnd[k]:bnd[k + 1]]
        tr = np.setdiff1d(allidx, va)
        # SVD ridge: X = U s V'  =>  w = V diag(s/(s^2+lam)) U'y = V diag(1/(s^2+lam)) V' X'y;
        # the eigendecomposition of X'X gives V and s^2 without forming U.
        s2, V = np.linalg.eigh(Gs - G[k])
        s2 = np.clip(s2, 0, None)
        Vb = V.T @ (Bs - B[k])
        lams = ridge_rel * s2.max()
        W = V @ (Vb[:, None] / (s2[:, None] + lams[None, :]))     # p x nlam
        Yv = X[va] @ W.astype(np.float32)
        verr = ((Yv.astype(float) - y[va, None]) ** 2).mean(0)
        i = int(np.argmin(verr))
        w = W[:, i]
        rhat = (X @ w.astype(np.float32)).astype(float)
        res["ridge_index"].append(i)
        res["ridge"].append(lams[i])
        res["filters"].append(w)
        models = [("strf", rhat)]
        if ln:
            g, fv = lowess_fit(rhat[tr], y[tr])
            models.append(("ln", np.interp(rhat, g, fv)))
        for name, rh in models:
            for part, idx in (("train", tr), ("valid", va)):
                t = perf_terms(rh, ptot, rbar, ppred, idx)
                res["t_%s_%s" % (name, part)].append(t)
                res["%s_%s" % (name, part)].append(t[0] / t[1])
    out = {k: np.array(v) for k, v in res.items()}
    for a in ("strf", "ln"):
        if len(out[a + "_train"]):
            out[a + "_upper"] = out[a + "_train"].mean()
            out[a + "_lower"] = out[a + "_valid"].mean()
            for part, lab in (("train", "upper"), ("valid", "lower")):
                t = out["t_%s_%s" % (a, part)]
                out["%s_%s_pooled" % (a, lab)] = t[:, 0].mean() / t[:, 1].mean()
    out["ridge_low_edge"] = int(np.sum(out["ridge_index"] == 0))
    out["ridge_high_edge"] = int(np.sum(out["ridge_index"] == len(ridge_rel) - 1))
    out["nbins"], out["nparams"] = n, p
    return out


def usable_cells(min_trials=2):
    """Cells with >= 1 natural-sound stimulus having >= min_trials included trials (from Summary.mat
    descriptions; 'Not included' notes are only known after loading, see cell_data)."""
    out = []
    for c in summary():
        cnt = {}
        for d in c["descriptions"]:
            s = d.split(": Trial No.")[0]
            if s.lower() not in EXCLUDE:
                cnt[s] = cnt.get(s, 0) + 1
        if any(v >= min_trials for v in cnt.values()):
            out.append(c["cell"])
    return out


def run_cell(args):
    """All nine window models for one cell and one spectrogram window: rows of the lower and
    upper performance of STRF and LN, averaged over folds (Methods) and pooled over folds."""
    cell, win_ms = args
    st = cell_data(cell, win_ms=win_ms)
    stimulus_samples.cache_clear()
    rows = []
    if not st:
        return rows
    ntr = [s["R"].shape[0] for s in st]
    for mi, cnt in enumerate(MODELS):
        r = strf_cv(st, cnt)
        F = r["filters"].mean(0).reshape(45, -1)
        rows.append(dict(cell=cell, win_ms=win_ms, model=mi + 1,
                         window_ms=sum(w * k for w, k in zip(WIDTHS_MS, cnt)), n_stimuli=len(st),
                         trials_min=min(ntr), trials_max=max(ntr), bins=r["nbins"], params=r["nparams"],
                         strf_upper=r["strf_upper"], strf_lower=r["strf_lower"],
                         ln_upper=r["ln_upper"], ln_lower=r["ln_lower"],
                         strf_upper_pooled=r["strf_upper_pooled"], strf_lower_pooled=r["strf_lower_pooled"],
                         ln_upper_pooled=r["ln_upper_pooled"], ln_lower_pooled=r["ln_lower_pooled"],
                         folds_ridge_at_low_edge=r["ridge_low_edge"], folds_ridge_at_high_edge=r["ridge_high_edge"],
                         fold_valid_min=float(r["strf_valid"].min()), fold_valid_max=float(r["strf_valid"].max()),
                         peak_lag_ms=4 * lag_edges(cnt)[int(np.argmax(np.abs(F).max(1)))][0]))
    return rows
