"""STRF and LN model performance on Wehr's recordings in CRCNS ac-1 (claim fig4-strf-performance-low).

Asari H, Zador AM (2009), Methods, Neural encoding models and Model performance (Eqs. 46-53),
reanalysed "the recording data (20 cells) from the previous work (Machens et al. 2004)". The data
set holds those recordings under `wehr/` (25 cells, `wehr/Summary.mat`), one file per trial, with
the stimuli under `wehr/Stimuli/`, and the authors' `wehr/Tools/STRFanalysis.m`, `ridgesvd1.m`,
`logspectrogram.m`, `ViewResponse.m` and `GetEvoked.m`. The archive is read with `asari.Archive`.

Where the parameters come from:

- Time bins of 2^k ms for k = 2..10, 45 bins split as the Methods list ([45], [9, 36], ...,
  [9, 8, ..., 1]), giving windows of 180 to 4052 ms; 3 frequency bins per octave from 0.40 kHz,
  17 bins (Methods, Neural encoding models; claim criterion). The 17 centre frequencies are
  400 * 2^(k/3) Hz, k = 0..16 (to 16 kHz): the Methods give "0.40 to 22 kHz; 17 frequency bins"
  and `STRFanalysis.m` fmax = 22100 Hz, which at 3 bins per octave gives 17 or 18 bins depending on
  rounding; the first 17 are used (a standard choice).
- Spectrogram (Eq. 47): magnitude in dB of the short-time Fourier transform at those
  frequencies, Hann window of 10 ms (main) or 20 ms (claim criterion readings), one frame per
  4-ms response bin, centred on the bin, each frequency centred on its mean over the stimulus
  (`STRFanalysis.m`, S - mean(S, 2)). The 20-ms ramp of `MakeRamp.m` (hann, applied by
  `ViewResponse.m`) is applied to the stimulus.
- Response: membrane potential with the 10-ms median filter (`ViewResponse.m` default
  `smooth = 10`, `GetEvoked.m`), the stimulus period of each trial, averaged in 4-ms bins (the
  finest time bin; criterion reading), each trial centred on its mean (`STRFanalysis.m`).
- Ridge regression (Eq. 50) on the trial mean, on a log grid of ridge values scaled to the mean
  eigenvalue of S'S (1e-3 to 1e4; a standard choice, the grid edges are reported), the value chosen
  by the validation performance (Methods). 10-fold cross-validation with contiguous folds
  (`STRFanalysis.m`, ncol) or folds formed by stimulus (criterion reading).
- Model performance (Eq. 53): (total power - error power) / predictable power (Eq. 52), with
  the predictable power of a stimulus heard once taken as half its total power, as
  `STRFanalysis.m` does (`Ppred = 0.5 * Ptotal` when n = 1). Validation performance is pooled
  over the validation folds (Eq. 53 averages over time); the mean over folds of the per-fold
  ratios (`STRFanalysis.m`) is a variant.
- Static nonlinearity: robust lowess (Cleveland 1979) of the actual against the estimated
  response on the training set, 5% span, 5 robustness iterations (Methods, Static
  nonlinearities), evaluated on a grid of 200 points and interpolated (as the `delta` option of
  common lowess implementations does), applied to the validation set.
- Samples: every window is scored on the same response bins, those at least 4052 ms after
  stimulus onset (main), so that every lag has stimulus history; the variant drops only each
  window's own length (`STRFanalysis.m` drops the first `nbin` bins).
"""

from __future__ import annotations

import re

import numpy as np
from scipy import ndimage

DT = 0.004                                      # s, response bin and spectrogram hop
FREQS = 400.0 * 2 ** (np.arange(17) / 3)        # Hz
COUNTS = [[45], [9, 36], [9, 8, 28], [9, 8, 7, 21], [9, 8, 7, 6, 15], [9, 8, 7, 6, 5, 10],
          [9, 8, 7, 6, 5, 4, 6], [9, 8, 7, 6, 5, 4, 3, 3], [9, 8, 7, 6, 5, 4, 3, 2, 1]]
WIDTHS = [2 ** k for k in range(9)]             # bin widths in 4-ms frames (4 ms to 1024 ms)
WINDOWS_MS = [int(sum(c * w * 4 for c, w in zip(cs, WIDTHS))) for cs in COUNTS]
MAX_LAG = max(sum(c * w for c, w in zip(cs, WIDTHS)) for cs in COUNTS)   # 1013 frames
RIDGE_REL = 10.0 ** np.arange(-3, 4.01, 0.5)
MEDIAN_MS = 10
SKIP = {"tuning curve", "silence", "white noise"}   # ViewResponse.m: not natural sound stimuli


def wehr_cells(archive) -> list[dict]:
    """Cells of wehr/Summary.mat, each with its natural sound stimuli and their trial files."""
    m = archive.loadmat("wehr/Summary.mat")
    out = []
    for ei, e in enumerate(np.atleast_1d(m["experiment"])):
        for c in np.atleast_1d(e.cell):
            files = [str(f) for f in np.atleast_1d(c.file)]
            descs = [str(d) for d in np.atleast_1d(c.description)]
            stim = {}
            for f, d in zip(files, descs):
                name = re.sub(r": Trial No.*", "", d).strip()
                if name not in SKIP:
                    stim.setdefault(name, []).append("wehr/" + f)
            out.append(dict(cell=files[0].split("/")[1], experiment=ei,
                            experiment_description=str(e.description).strip(), stimuli=stim))
    return out


def _hann(n):
    return 0.5 - 0.5 * np.cos(2 * np.pi * np.arange(n) / n)


def spectrogram(samples: np.ndarray, sf: float, n_frames: int, win_s: float) -> np.ndarray:
    """Eq. 47 at FREQS: dB magnitude of the STFT, Hann window `win_s`, frame k centred at
    (k + 0.5) * DT; frequencies x frames, each frequency centred on its mean."""
    nw = int(round(win_s * sf))
    w = _hann(nw)
    centres = np.round((np.arange(n_frames) + 0.5) * DT * sf).astype(int)
    pad = np.concatenate([np.zeros(nw), samples, np.zeros(nw)])
    idx = centres[:, None] + nw - nw // 2 + np.arange(nw)[None, :]
    E = np.exp(-2j * np.pi * np.outer(np.arange(nw) / sf, FREQS)) * w[:, None]
    out = np.empty((len(FREQS), n_frames))
    for a in range(0, n_frames, 2000):
        seg = pad[idx[a:a + 2000]]
        out[:, a:a + 2000] = (20 * np.log10(np.abs(seg @ E) + 1e-12)).T
    return out - out.mean(1, keepdims=True)


def load_stimulus(archive, rel: str, ramp_ms: float):
    s = archive.loadmat("wehr/Stimuli/" + rel)["stimulus"]
    x = np.asarray(s.samples, float).ravel().copy()
    sf = float(s.param.sf)
    a = int(round(ramp_ms * sf / 1000))
    if a >= 1:                              # MakeRamp.m
        w = np.hanning(2 * a)               # MATLAB window(@hann, 2a)
        x[:a] *= w[:a]
        x[-a:] *= w[a:]
    return x, sf


def load_cell(archive, cell: dict, win_s=(0.010, 0.020)) -> list[dict]:
    """Per stimulus: trials x bins response (mV, 4-ms means, each trial centred) and the
    spectrogram for each window length."""
    out = []
    for name, files in cell["stimuli"].items():
        R, trig0, rtype = [], None, set()
        for f in files:
            d = archive.loadmat(f)
            rtype.add(str(d["param"].recording.type))
            r = d["response"]
            sf = int(r.sf)
            x = r.trace.astype(float) * float(r.scale)
            mu = x.mean()
            x = ndimage.median_filter(x - mu, size=int(round(MEDIAN_MS / 1000 * sf)), mode="constant") + mu
            t = [tt for tt in np.atleast_1d(d["triggers"]) if "pulse" not in str(tt.type)][0]
            trig0 = trig0 or t
            t0 = int(t.time)                # GetEvoked.m: evoked from sample `time`
            n = int(round(float(t.param.duration) / 1000 * sf))
            seg = x[t0 - 1:t0 - 1 + n]
            per = int(round(DT * sf))
            nb = len(seg) // per
            R.append(seg[:nb * per].reshape(nb, per).mean(1))
        nb = min(len(v) for v in R)
        R = np.array([v[:nb] for v in R])
        R = R - R.mean(1, keepdims=True)
        stim, ssf = load_stimulus(archive, str(trig0.file), float(getattr(trig0.param, "ramp", 0)))
        specs = {w: spectrogram(stim, ssf, nb, w) for w in win_s}
        out.append(dict(name=name, R=R, n_trials=len(R), specs=specs, stim_file=str(trig0.file),
                        recording_type=sorted(rtype), sf=sf, stim_sf=ssf))
    return out


def design(spec: np.ndarray, counts: list[int]) -> np.ndarray:
    """Pseudo-logarithmic lag bins: for each response bin, the mean spectrogram over each lag
    bin (bin j of width WIDTHS[j], repeated counts[j] times, from the present into the past);
    frames before stimulus onset are 0 (the centred mean). Returns bins x (17 * 45)."""
    F, T = spec.shape
    cs = np.concatenate([np.zeros((F, MAX_LAG + 1)), spec], axis=1).cumsum(1)
    cs = np.concatenate([np.zeros((F, 1)), cs], axis=1)
    t = np.arange(T) + MAX_LAG + 1          # index in the padded series (one past the frame)
    cols, lag = [], 0
    for c, w in zip(counts, WIDTHS):
        for _ in range(c):
            hi, lo = t - lag, t - lag - w   # frames [lo, hi) in padded indices
            cols.append((cs[:, hi] - cs[:, lo]) / w)
            lag += w
    return np.concatenate(cols, axis=0).T


def lowess(x, y, frac=0.05, it=5, n_grid=200):
    """Robust lowess (Cleveland 1979): local linear fits with tricube weights over the nearest
    `frac` of the points, `it` robustness iterations with bisquare weights; evaluated on a grid
    and interpolated. Returns (grid, fitted values)."""
    o = np.argsort(x)
    x, y = x[o], y[o]
    n = len(x)
    k = max(int(np.ceil(frac * n)), 3)
    grid = np.unique(np.quantile(x, np.linspace(0, 1, n_grid)))
    rw = np.ones(n)
    for i in range(it + 1):
        fit = np.empty(len(grid))
        for g, x0 in enumerate(grid):
            j = np.searchsorted(x, x0)
            lo, hi = max(0, j - k), min(n, j + k)
            d = np.abs(x[lo:hi] - x0)
            sel = np.argsort(d)[:k]
            xs, ys, ds = x[lo:hi][sel], y[lo:hi][sel], d[sel]
            h = ds.max() if ds.max() > 0 else 1.0
            w = (1 - (ds / h) ** 3) ** 3 * rw[lo:hi][sel]
            sw = w.sum()
            if sw <= 0:
                fit[g] = ys.mean()
                continue
            mx = (w * xs).sum() / sw
            my = (w * ys).sum() / sw
            vx = (w * (xs - mx) ** 2).sum()
            b = (w * (xs - mx) * (ys - my)).sum() / vx if vx > 0 else 0.0
            fit[g] = my + b * (x0 - mx)
        if i == it:
            break
        res = y - np.interp(x, grid, fit)
        s = np.median(np.abs(res))
        u = res / (6 * s) if s > 0 else np.zeros(n)
        rw = np.where(np.abs(u) < 1, (1 - u ** 2) ** 2, 0.0)
    return grid, fit


def bin_powers(R: np.ndarray):
    """Per response bin: total power and predictable power (Eq. 52, per bin as in
    STRFanalysis.m LNperformance; half the total power for a stimulus heard once)."""
    n = len(R)
    pt = (R ** 2).mean(0)
    pp = (n * R.mean(0) ** 2 - pt) / (n - 1) if n > 1 else 0.5 * pt
    return pt, pp


def performance(P, r, pp, mask):
    """Eq. 53 over the bins in `mask`: (total - error power) / predictable power. With the
    error power of bin t, mean_j (R_j - p)^2 = total - 2 p rbar + p^2, the numerator is
    sum(2 p rbar - p^2). `P` may hold one prediction per row."""
    P = np.atleast_2d(P)
    return ((2 * P[:, mask] * r[mask] - P[:, mask] ** 2).sum(1)) / pp[mask].sum()


def cell_performance(stims: list[dict], win_s: float, folds: str = "contiguous", samples: str = "common",
                     n_folds: int = 10, ln: bool = True) -> list[dict]:
    """STRF and LN performance of one cell for each of the nine windows: validation pooled over
    the validation folds (main) and the mean over folds of per-fold values (STRFanalysis.m),
    training as the mean over folds."""
    out = []
    for wi, counts in enumerate(COUNTS):
        start = MAX_LAG if samples == "common" else sum(c * w for c, w in zip(counts, WIDTHS))
        Xs, rs, pps, sid = [], [], [], []
        for k, s in enumerate(stims):
            Xs.append(design(s["specs"][win_s], counts)[start:])
            R = s["R"][:, start:]
            _, pp = bin_powers(R)
            rs.append(R.mean(0))
            pps.append(pp)
            sid.append(np.full(R.shape[1], k))
        X = np.concatenate(Xs)
        r = np.concatenate(rs)
        pp = np.concatenate(pps)
        stim_of = np.concatenate(sid)
        m = len(r)
        if folds == "contiguous":           # STRFanalysis.m: ncol = round(m / xval), contiguous
            size = int(round(m / n_folds))
            fold = np.minimum(np.arange(m) // size, n_folds - 1)
        else:                               # by stimulus, at most n_folds groups
            fold = stim_of % n_folds
        nf = int(fold.max()) + 1
        G = X.T @ X
        b = X.T @ r
        lam = RIDGE_REL * np.trace(G) / G.shape[0]
        pred = np.zeros((len(lam), m))      # cross-validated predictions
        train = np.zeros((len(lam), nf))
        fvalid = np.zeros((len(lam), nf))
        W_all = []
        for f in range(nf):
            v = fold == f
            e, V = np.linalg.eigh(G - X[v].T @ X[v])
            Vb = V.T @ (b - X[v].T @ r[v])
            W = V @ (Vb[:, None] / (e[:, None] + lam[None, :]))
            P = (X @ W).T
            pred[:, v] = P[:, v]
            W_all.append(W)
            train[:, f] = performance(P, r, pp, ~v)
            fvalid[:, f] = performance(P, r, pp, v)
        pooled = performance(pred, r, pp, np.ones(m, bool))
        best = int(np.argmax(pooled))
        bestf = int(np.argmax(fvalid.mean(1)))
        row = dict(window_ms=WINDOWS_MS[wi], ridge_index=best, ridge_at_edge=best in (0, len(lam) - 1),
                   strf_valid=float(pooled[best]), strf_train=float(train[best].mean()),
                   strf_valid_foldmean=float(fvalid[bestf].mean()), strf_train_foldmean=float(train[bestf].mean()),
                   n_bins=m, n_folds=nf)
        if ln:
            ln_pred = np.zeros(m)
            ln_train, ln_fvalid = [], []
            for f in range(nf):
                v = fold == f
                P = X @ W_all[f][:, best]
                gx, gy = lowess(P[~v], r[~v])
                yh = np.interp(P, gx, gy)
                ln_pred[v] = yh[v]
                ln_train.append(performance(yh, r, pp, ~v)[0])
                ln_fvalid.append(performance(yh, r, pp, v)[0])
            row.update(ln_valid=float(performance(ln_pred, r, pp, np.ones(m, bool))[0]),
                       ln_train=float(np.mean(ln_train)), ln_valid_foldmean=float(np.mean(ln_fvalid)))
        out.append(row)
    return out


CONFIGS = {"main": (0.010, "contiguous", "common"), "window 20 ms": (0.020, "contiguous", "common"),
           "folds by stimulus": (0.010, "stimulus", "common"), "own samples": (0.010, "contiguous", "own")}


def run_cell(cell: dict) -> dict:
    """One cell, for use in a process pool: loads it, then the performance under the main
    configuration for both cell readings ('repeated': only stimuli heard at least twice;
    'code': every stimulus, with STRFanalysis.m's rule for a single trial) and under the
    variants for the 'repeated' reading."""
    import os
    import asari
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    A = asari.Archive()
    stims = load_cell(A, cell)
    rep = [s for s in stims if s["n_trials"] >= 2]
    rows = []
    info = dict(cell=cell["cell"], n_stimuli=len(stims), n_repeated=len(rep),
                trials=[s["n_trials"] for s in stims],
                recording_types=sorted({t for s in stims for t in s["recording_type"]}),
                sf=sorted({s["sf"] for s in stims}), stim_sf=sorted({s["stim_sf"] for s in stims}), seconds=[s["R"].shape[1] * DT for s in stims],
                spec_range=(float(min(s["specs"][0.010].min() for s in stims)),
                            float(max(s["specs"][0.010].max() for s in stims))),
                resp_range=(float(min(s["R"].min() for s in stims)), float(max(s["R"].max() for s in stims))),
                reliability=float(sum(bin_powers(s["R"])[1].sum() for s in rep) /
                                  sum(bin_powers(s["R"])[0].sum() for s in rep)) if rep else np.nan)
    for name, (w, folds, samples) in CONFIGS.items():
        readings = ["repeated", "code"] if name == "main" else ["repeated"]
        for reading in readings:
            use = rep if reading == "repeated" else stims
            if not use or (reading == "code" and len(use) == len(rep) and rep):
                continue
            for r in cell_performance(use, w, folds=folds, samples=samples):
                rows.append(dict(cell=cell["cell"], config=name, reading=reading, **r))
    return dict(info=info, rows=rows)
