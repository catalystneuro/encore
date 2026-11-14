"""STRF and LN models of Wehr's recordings (Machens et al. 2004) in CRCNS ac-1, as Asari & Zador
(2009) fit them for Figure 4 (Methods, Neural encoding models; Model performance).

Where the parameters come from (paper = Methods of Asari & Zador 2009; criterion = the claim
fig4-strf-performance-low; code = wehr/Tools/STRFanalysis.m in crcns-ac1.zip):

- Spectrogram (Eq. 47): short-time Fourier transform with a Hann window h(t) of 10 ms (main) or
  20 ms (criterion readings), in dB, 3 bins per octave from 0.40 kHz (paper: 17 frequency bins;
  the band edges are 400 * 2^(k/3) Hz, k = 0..17, up to 20.3 kHz). Power is floored 100 dB below
  the cell's largest value before the logarithm, and each frequency channel is centred over the
  cell's stimuli (STRFanalysis.m centres it per stimulus; a standard choice). The sound before
  stimulus onset is silence.
- Time bins of 4 ms, the finest bin of the model (criterion reading); responses are the membrane
  potential with spikes clipped by a 10-ms median filter (ViewResponse.m default), averaged in
  4-ms bins and centred per trial.
- Windows: 45 bins of 2^k ms, k = 2..10, split as [45, 0, ...], [9, 36, 0, ...], ...,
  [9, 8, ..., 1] (paper), so windows of 180 to 4052 ms and 765 parameters.
- Ridge regression (Eq. 50) with 10-fold cross-validation; the ridge parameter is the one with
  the best mean validation performance over folds (STRFanalysis.m), from a grid of 17 values
  spanning 10^-7 to 10 times the largest eigenvalue of S'S (a standard choice, checked to be
  interior). Folds are contiguous blocks of the concatenated data (main) or whole stimuli
  (criterion reading).
- Static nonlinearity (Eq. 51): robust lowess of the mean response on the linear estimate over
  the training set, 5% span, five robustness iterations (paper), evaluated on 60 points of the
  estimate and interpolated (a standard approximation), then applied to the validation set.
- Performance (Eq. 53) with the predictable power of Eq. 52 over the time points of each set,
  each time point with its own number of trials; stimuli with fewer than two trials are left out,
  as Eq. 52 cannot use them.
"""

from __future__ import annotations

import io
import re
from concurrent.futures import ThreadPoolExecutor

import numpy as np

import asari

DATASET = "crcns:ac-1/unversioned"   # CRCNS does not version data sets
DT_MS = 4
SF_RESP = 4000
F_EDGES = 400.0 * 2 ** (np.arange(18) / 3)
BIN_MS = 2 ** np.arange(2, 11)
WINDOWS = [[9, 8, 7, 6, 5, 4, 3, 2, 1][:j] + [45 - sum([9, 8, 7, 6, 5, 4, 3, 2, 1][:j])] + [0] * (8 - j) for j in range(9)]
WINDOW_MS = [int(np.dot(w, BIN_MS)) for w in WINDOWS]
PAD_S = 4.2
N_FOLD = 10


def summary():
    z = asari.open_zip(asari.MAIN_ZIP)
    m = asari.loadmat(io.BytesIO(z.read("wehr/Summary.mat")))
    rows = []
    for gi, ex in enumerate(np.atleast_1d(m["experiment"])):
        for c in np.atleast_1d(ex.cell):
            files = [str(f) for f in np.atleast_1d(c.file)]
            descs = [" ".join(str(d).split()) for d in np.atleast_1d(c.description)]
            for f, d in zip(files, descs):
                rows.append({"group": gi, "cell": f.split("/")[1], "file": f, "description": d,
                             "stimulus": re.sub(r":\s*Trial No.*", "", d)})
    return rows


def is_natural(desc):
    d = desc.lower()
    return not any(k in d for k in ("tuning curve", "silence", "white noise"))


def load_trial(path):
    """One trial file: the response over the stimulus, spikes clipped, in 4-ms bins, centred."""
    z = asari.open_zip(asari.MAIN_ZIP)
    m = asari.loadmat(io.BytesIO(z.read("wehr/" + path)))
    r, t = m["response"], m["triggers"]
    sf = int(r.sf)
    x = r.trace.astype(np.float64) * float(r.scale)
    a = int(t.time) - 1
    n = int(round(float(t.param.duration) / 1000 * sf))
    x = asari.median_clip(x, 10, sf=sf)[a:a + n]
    k = int(DT_MS * sf / 1000)
    y = x[:len(x) // k * k].reshape(-1, k).mean(1)
    return {"stim_file": str(t.file), "sf": sf, "y": y - y.mean()}


def load_stimulus(name):
    z = asari.open_zip(asari.MAIN_ZIP)
    m = asari.loadmat(io.BytesIO(z.read("wehr/Stimuli/" + name)))
    return np.asarray(m["stimulus"].samples, float), int(m["stimulus"].param.sf)


def band_power(s, sf, n_frames, win_ms):
    """Power in the 17 third-octave bands at frames every 4 ms (frame i centred at (i + 0.5) * 4 ms
    after onset), with PAD_S of silence before onset (frames counted from the start of the pad)."""
    pad = int(round(PAD_S * sf))
    s = np.concatenate([np.zeros(pad), s, np.zeros(int(sf))])
    w = int(round(win_ms / 1000 * sf))
    h = np.hanning(w)
    nfft = 1 << int(np.ceil(np.log2(w)))
    n_pad = int(round(PAD_S * 1000 / DT_MS))
    total = n_pad + n_frames
    centres = np.round((np.arange(total) + 0.5) * DT_MS / 1000 * sf).astype(int)
    idx = centres[:, None] - w // 2 + np.arange(w)[None, :]
    idx = np.clip(idx, 0, len(s) - 1)
    out = np.zeros((total, 17))
    f = np.fft.rfftfreq(nfft, 1 / sf)
    band = np.searchsorted(F_EDGES, f, side="right") - 1
    ok = (band >= 0) & (band < 17)
    for i0 in range(0, total, 2000):
        seg = s[idx[i0:i0 + 2000]] * h
        P = np.abs(np.fft.rfft(seg, nfft, axis=1)) ** 2
        out[i0:i0 + 2000] = np.stack([P[:, ok & (band == b)].sum(1) for b in range(17)], 1)
    return out, n_pad


def load_cell(rows, threads=6):
    """Trials of the natural sounds of one cell, grouped by stimulus; stimuli with >= 2 trials."""
    paths = [r["file"] for r in rows if is_natural(r["description"])]
    with ThreadPoolExecutor(threads) as ex:
        trials = list(ex.map(load_trial, paths))
    by = {}
    for t in trials:
        by.setdefault(t["stim_file"], []).append(t["y"])
    out = {}
    for k, ys in by.items():
        if len(ys) >= 2:
            n = min(len(y) for y in ys)
            out[k] = np.stack([y[:n] for y in ys])
    return out, {k: len(v) for k, v in by.items()}


def design(spec, n_pad, window):
    """Lagged spectrogram features for one stimulus: frames x 765 (bin means, nearest bin first)."""
    C = np.concatenate([np.zeros((1, spec.shape[1])), np.cumsum(spec, 0)])
    T = spec.shape[0] - n_pad
    t = n_pad + np.arange(T)
    cols, a = [], 0
    for n_k, size_ms in zip(window, BIN_MS):
        s = int(size_ms // DT_MS)
        for _ in range(n_k):
            lo = np.maximum(t - a - s + 1, 0)
            cols.append((C[t - a + 1] - C[lo]) / s)
            a += s
    return np.concatenate(cols, 1).astype(np.float32)


def perf_terms(R):
    """Per time point: sum of trials, sum of squares, number of trials (Eqs. 52 and 53)."""
    return R.sum(0), (R ** 2).sum(0), np.full(R.shape[1], R.shape[0], float)


def performance(rhat, S1, S2, m):
    tot = np.mean(S2 / m)
    err = np.mean(S2 / m - 2 * rhat * S1 / m + rhat ** 2)
    pred = np.mean((S1 ** 2 / m - S2 / m) / (m - 1))
    return (tot - err) / pred


def lowess_fit(x, y, frac=0.05, it=5, n_grid=60):
    """Robust lowess (tricube, local linear, bisquare robustness), evaluated on n_grid quantiles of x."""
    o = np.argsort(x)
    xs, ys = x[o], y[o]
    N = len(xs)
    k = max(int(np.ceil(frac * N)), 10)
    grid = np.quantile(xs, np.linspace(0, 1, n_grid))
    rw = np.ones(N)
    for _ in range(it + 1):
        g = np.empty(n_grid)
        for j, x0 in enumerate(grid):
            i = int(np.searchsorted(xs, x0))
            lo = int(np.clip(i - k // 2, 0, N - k))
            xx, yy, ww = xs[lo:lo + k], ys[lo:lo + k], rw[lo:lo + k]
            d = np.abs(xx - x0)
            dm = d.max() if d.max() > 0 else 1.0
            w = (1 - (d / dm) ** 3) ** 3 * ww
            sw = w.sum()
            if sw <= 0:
                g[j] = yy.mean()
                continue
            mx, my = (w * xx).sum() / sw, (w * yy).sum() / sw
            vx = (w * (xx - mx) ** 2).sum()
            b = (w * (xx - mx) * (yy - my)).sum() / vx if vx > 0 else 0.0
            g[j] = my + b * (x0 - mx)
        res = ys - np.interp(xs, grid, g)
        s = np.median(np.abs(res))
        u = res / (6 * s) if s > 0 else np.zeros_like(res)
        rw = np.where(np.abs(u) < 1, (1 - u ** 2) ** 2, 0.0)
    return grid, g


def fit_cell(stims, specs, n_pads, schemes=("contiguous", "stimulus")):
    """Per fold scheme and window: ridge path over the folds; best ridge by mean validation
    performance; lower and upper performance of the STRF and the LN model, and whether the best
    ridge is interior. The STRF performances come from S'S and S'r of each set (Eq. 53 needs only
    the means of rhat^2 and rhat*rbar over time), so the folds share one pass over the data."""
    names = sorted(stims)
    ybar = [stims[k].mean(0) for k in names]
    terms = [perf_terms(stims[k]) for k in names]
    lens = [len(v) for v in ybar]
    N = sum(lens)
    edges = np.linspace(0, N, N_FOLD + 1).astype(int)
    fold_c = np.searchsorted(edges, np.arange(N), side="right") - 1
    stim_of = np.concatenate([np.full(L, i) for i, L in enumerate(lens)])
    fold_s = stim_of % min(N_FOLD, len(names))
    seg = stim_of * N_FOLD + fold_c
    useg = np.unique(seg)
    y = np.concatenate(ybar)
    S1 = np.concatenate([t[0] for t in terms]); S2 = np.concatenate([t[1] for t in terms]); M = np.concatenate([t[2] for t in terms])
    pp = (S1 ** 2 / M - S2 / M) / (M - 1)
    out = []
    for w_ms, window in zip(WINDOW_MS, WINDOWS):
        X = np.concatenate([design(specs[k], n_pads[k], window)[:L] for k, L in zip(names, lens)])
        G = {}
        for sg in useg:
            Xs = X[seg == sg].astype(np.float64)
            G[sg] = (Xs.T @ Xs, Xs.T @ y[seg == sg], int((seg == sg).sum()), pp[seg == sg].sum())
        A = sum(g[0] for g in G.values()); b = sum(g[1] for g in G.values())
        lams = np.linalg.eigvalsh(A)[-1] * 10.0 ** np.linspace(-7, 1, 17)
        for scheme in schemes:
            fold_of = fold_c if scheme == "contiguous" else fold_s
            nf = int(fold_of.max()) + 1
            seg_fold = {sg: int(fold_of[seg == sg][0]) for sg in useg}
            pv = np.zeros((nf, len(lams))); pt = np.zeros((nf, len(lams))); betas = []
            for f in range(nf):
                parts = [G[sg] for sg in useg if seg_fold[sg] == f]
                Av = sum(p[0] for p in parts); bv = sum(p[1] for p in parts)
                nv = sum(p[2] for p in parts); qv = sum(p[3] for p in parts)
                At, bt, nt, qt = A - Av, b - bv, N - nv, pp.sum() - qv
                e, V = np.linalg.eigh(At)
                B = V @ ((V.T @ bt)[:, None] / (e[:, None] + lams[None, :]))
                betas.append(B)
                for j in range(len(lams)):
                    be = B[:, j]
                    pv[f, j] = (2 * be @ bv - be @ Av @ be) / qv
                    pt[f, j] = (2 * be @ bt - be @ At @ be) / qt
            jb = int(np.argmax(pv.mean(0)))
            ln_v, ln_t = [], []
            for f in range(nf):
                va, tr = fold_of == f, fold_of != f
                rh = X @ betas[f][:, jb].astype(np.float32)
                grid, g = lowess_fit(rh[tr].astype(float), y[tr])
                ln_t.append(performance(np.interp(rh[tr], grid, g), S1[tr], S2[tr], M[tr]))
                ln_v.append(performance(np.interp(rh[va], grid, g), S1[va], S2[va], M[va]))
            out.append({"folds": scheme, "window_ms": w_ms, "strf_lower": pv[:, jb].mean(), "strf_upper": pt[:, jb].mean(),
                        "ln_lower": float(np.mean(ln_v)), "ln_upper": float(np.mean(ln_t)),
                        "ridge_index": jb, "ridge_interior": 0 < jb < len(lams) - 1, "n_points": N, "n_folds": nf})
        del X
    return out


_POWER = {}


def cell_specs(stims, win_ms):
    """dB spectrograms of a cell's stimuli (power floored 100 dB below the cell's largest value),
    each channel centred over the cell's in-stimulus frames."""
    raw, n_pads = {}, {}
    for k, R in stims.items():
        key = (k, win_ms)
        if key not in _POWER:
            s, sf = load_stimulus(k)
            n_frames = int(np.ceil(len(s) / sf * 1000 / DT_MS))
            _POWER[key] = band_power(s, sf, n_frames, win_ms)
        P, n_pad = _POWER[key]
        raw[k], n_pads[k] = P[:n_pad + R.shape[1]], n_pad
    top = max(P.max() for P in raw.values())
    db = {k: 10 * np.log10(P + top * 1e-10) for k, P in raw.items()}
    mu = np.concatenate([db[k][n_pads[k]:] for k in db]).mean(0)
    return {k: v - mu for k, v in db.items()}, n_pads
