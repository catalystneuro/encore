"""Linear (STRF) and linear-nonlinear encoding models on M. Wehr's A1 recordings in CRCNS ac-1
(the wehr/ folder of crcns-ac1.zip), for fig4-strf-performance-low of Asari and Zador (2009).

Where each parameter comes from:

- Spectrogram (Eq. 47) in dB, 3 bins per octave from 0.40 kHz (17 bins), time bins of 2^k ms for
  k = 2..10 with 45 bins split [45, 0, ...], [9, 36, 0, ...], ..., [9, 8, ..., 1] (windows 180 to
  4052 ms, 765 parameters), ridge regression (Eq. 50) with 10-fold cross-validation choosing the
  ridge parameter on the validation folds, the static nonlinearity by robust lowess (5% span, 5
  iterations) on the training set, and the performance of Eq. 53 on training (upper) and
  validation (lower) data: the claim's criterion, citing the Methods (Neural encoding models,
  Model performance).
- The window h(t) of Eq. 47 (Hann, 10 ms main, 20 ms variant), the response sampling (4-ms bins,
  the finest time bin), the ridge grid (log-spaced, wide enough that the chosen value is
  interior) and the folds (contiguous blocks main, whole stimuli variant): readings named by the
  criterion.
- The 10-ms median filter and the removal of each trial's mean: the paper's preprocessing of
  membrane potential (Methods, Analysis) and STRFanalysis.m in the data set.
- Cells: those with at least two trials of a natural sound, which Eq. 52 needs (an assumption:
  the paper names 20 cells of Machens et al. 2004 without saying which).
"""
from __future__ import annotations

import io
import re
import zipfile

import fsspec
import numpy as np
import scipy.io as sio
import scipy.ndimage as nd
from scipy import signal

DATASET = "crcns:ac-1/unversioned"  # CRCNS does not version data sets; MD5 sums in the notebook
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip"
DT = 0.004                      # s, finest time bin (2^2 ms)
F0, NF, BPO = 400.0, 17, 3      # lowest frequency, number of bins, bins per octave
CONFIGS = [[45], [9, 36], [9, 8, 28], [9, 8, 7, 21], [9, 8, 7, 6, 15], [9, 8, 7, 6, 5, 10],
           [9, 8, 7, 6, 5, 4, 6], [9, 8, 7, 6, 5, 4, 3, 3], [9, 8, 7, 6, 5, 4, 3, 2, 1]]

_Z = {}


def zf():
    if "z" not in _Z:
        _Z["z"] = zipfile.ZipFile(fsspec.open(BASE, block_size=2 ** 20).open())
    return _Z["z"]


def window_ms(cfg):
    return sum(c * 2 ** (k + 2) for k, c in enumerate(cfg))


def cells():
    """Cells of wehr/Summary.mat with, for each natural-sound stimulus, the files of its trials."""
    m = sio.loadmat(io.BytesIO(zf().read("wehr/Summary.mat")), squeeze_me=True,
                    struct_as_record=False)
    out = []
    for e in np.atleast_1d(m["experiment"]):
        for c in np.atleast_1d(e.cell):
            fs, ds = list(c.file), list(c.description)
            stims = {}
            for f, d in zip(fs, ds):
                stem = re.sub(r":\s*Trial No\.\s*\d+", "", d).strip()
                if any(x in stem.lower() for x in ("tuning", "silence", "white")):
                    continue
                stims.setdefault(stem, []).append(f)
            out.append(dict(cell=fs[0].split("/")[1], experiment=str(e.description).strip(),
                            stimuli=stims))
    return out


def load_trial(path):
    d = sio.loadmat(io.BytesIO(zf().read("wehr/" + path)), squeeze_me=True,
                    struct_as_record=False)
    r, t = d["response"], d["triggers"]
    tr = np.asarray(r.trace).astype(np.float64) * float(r.scale)
    return tr, float(r.sf), int(round(float(t.time))) - 1, float(t.param.duration), str(t.file)


def load_stimulus(path):
    d = sio.loadmat(io.BytesIO(zf().read("wehr/Stimuli/" + path)), squeeze_me=True,
                    struct_as_record=False)
    s = d["stimulus"]
    return np.asarray(s.samples, float).ravel(), float(s.param.sf)


def spectrogram(x, sf, win_ms=10.0):
    """Eq. 47: |STFT| with a Hann window of win_ms, every 4 ms, power summed in 1/3-octave bands
    centred at 0.4 kHz * 2^(k/3), k = 0..16, in dB."""
    nper = int(round(win_ms / 1000 * sf))
    hop = int(round(DT * sf))
    f, t, Z = signal.stft(x, fs=sf, window="hann", nperseg=nper, noverlap=nper - hop,
                          boundary=None, padded=False)
    P = np.abs(Z) ** 2
    cent = F0 * 2 ** (np.arange(NF) / BPO)
    S = np.empty((NF, P.shape[1]))
    for i, c in enumerate(cent):
        lo, hi = c * 2 ** (-0.5 / BPO), c * 2 ** (0.5 / BPO)
        m = (f >= lo) & (f < hi)
        if not m.any():
            m = [np.argmin(np.abs(f - c))]
        S[i] = P[m].sum(axis=0)
    # STFT frame j is centred at (j * hop + nper / 2) / sf; shift so that column j covers
    # [j * DT, (j + 1) * DT) as closely as the hop allows
    S = 10 * np.log10(S + 1e-12)
    return S


def responses(paths, win_ms=None):
    """Median-filtered (10 ms), trial-mean-removed responses of one stimulus in 4-ms bins,
    (trials, T), and its stimulus file."""
    R, stimfile = [], None
    for p in paths:
        tr, sf, t0, dur, sfile = load_trial(p)
        stimfile = sfile
        v = nd.median_filter(tr, size=int(round(0.01 * sf)) | 1, mode="nearest")
        seg = v[t0:t0 + int(round(dur / 1000 * sf))]
        k = int(round(DT * sf))
        n = len(seg) // k
        R.append(seg[:n * k].reshape(n, k).mean(axis=1))
    n = min(len(r) for r in R)
    R = np.array([r[:n] for r in R])
    R = R - R.mean(axis=1, keepdims=True)
    return R, stimfile


def features(S, cfg):
    """History features: for each time bin t, the mean spectrogram over consecutive past bins of
    2^k ms (closest first), counts per level from cfg. Returns (T, NF * 45)."""
    nf, T = S.shape
    c = np.concatenate([np.zeros((nf, 1)), np.cumsum(S, axis=1)], axis=1)
    cols = []
    lag = 0  # in 4-ms units, start of the current history bin (0 = the current bin)
    for k, cnt in enumerate(cfg):
        w = 2 ** k
        for _ in range(cnt):
            # bin covers time steps [t - lag - w + 1, t - lag]
            hi = np.arange(T) - lag + 1
            lo = hi - w
            hi_c = np.clip(hi, 0, T)
            lo_c = np.clip(lo, 0, T)
            val = (c[:, hi_c] - c[:, lo_c]) / w
            cols.append(val)
            lag += w
    X = np.concatenate(cols, axis=0).T
    return X


def performance(Rtr, rhat, idx):
    """Eq. 53 over the time samples idx: (total - error) / predictable power, Rtr (trials, T)
    padded with NaN where a stimulus had fewer trials."""
    Rr = Rtr[:, idx]
    m = np.sum(np.isfinite(Rr), axis=0)
    tot = np.nanmean(Rr ** 2, axis=0)
    mean = np.nanmean(Rr, axis=0)
    pred = (m * mean ** 2 - tot) / (m - 1)
    err = np.nanmean((Rr - rhat[idx]) ** 2, axis=0)
    return (np.mean(tot) - np.mean(err)) / np.mean(pred)


def performance_many(Rtr, RH, idx):
    """Eq. 53 for several response estimates at once (columns of RH)."""
    Rr = Rtr[:, idx]
    m = np.sum(np.isfinite(Rr), axis=0)
    tot = np.nanmean(Rr ** 2, axis=0)
    mean = np.nanmean(Rr, axis=0)
    pred = (m * mean ** 2 - tot) / (m - 1)
    # mean over trials of (r_j - rh)^2 = tot - 2 mean rh + rh^2
    err = tot[:, None] - 2 * mean[:, None] * RH[idx] + RH[idx] ** 2
    return (np.mean(tot) - err.mean(axis=0)) / np.mean(pred)


def lowess_fit(x, y, frac=0.05, it=5):
    import statsmodels.api as sm
    rng = np.ptp(x)
    out = sm.nonparametric.lowess(y, x, frac=frac, it=it, delta=0.01 * rng, return_sorted=True)
    xs, ys = out[:, 0], out[:, 1]
    xs, ui = np.unique(xs, return_index=True)
    ys = ys[ui]
    return lambda z: np.interp(z, xs, ys)


def fit_cell(stims, win_ms=10.0, folds="contiguous", ridges=None, configs=CONFIGS,
             with_ln=True):
    """Fits every window configuration for one cell. stims: list of (R trials x T, S spectrogram).
    Returns list of dicts per window: chosen ridge, mean training/validation performance of the
    STRF and LN models."""
    if ridges is None:
        ridges = np.logspace(0, 11, 23)
    Ts = [min(R.shape[1], S.shape[1]) for R, S in stims]
    mmax = max(R.shape[0] for R, S in stims)
    Rall = np.full((mmax, sum(Ts)), np.nan)
    pos = 0
    stim_id = np.zeros(sum(Ts), int)
    for i, ((R, S), T) in enumerate(zip(stims, Ts)):
        Rall[:R.shape[0], pos:pos + T] = R[:, :T]
        stim_id[pos:pos + T] = i
        pos += T
    r = np.nanmean(Rall, axis=0)
    N = len(r)
    if folds == "contiguous":
        edges = np.linspace(0, N, 11).astype(int)
        fold_of = np.searchsorted(edges, np.arange(N), side="right") - 1
    else:
        fold_of = stim_id % 10
    out = []
    for cfg in configs:
        X = np.concatenate([features(S[:, :T], cfg) for (R, S), T in zip(stims, Ts)], axis=0)
        X = X - X.mean(axis=0)
        G = X.T @ X
        b = X.T @ r
        perf_tr = np.zeros((len(ridges), 10))
        perf_va = np.zeros((len(ridges), 10))
        wts = {}
        for k in range(10):
            va = np.where(fold_of == k)[0]
            tr = np.where(fold_of != k)[0]
            if len(va) == 0:
                perf_tr[:, k] = perf_va[:, k] = np.nan
                continue
            Gt = G - X[va].T @ X[va]
            bt = b - X[va].T @ r[va]
            ev, V = np.linalg.eigh(Gt)
            Vb = V.T @ bt
            Wl = V @ (Vb[:, None] / (ev[:, None] + ridges[None, :]))
            RH = X @ Wl
            perf_tr[:, k] = performance_many(Rall, RH, tr)
            perf_va[:, k] = performance_many(Rall, RH, va)
            for j in range(len(ridges)):
                wts[(j, k)] = Wl[:, j]
        jbest = int(np.nanargmax(np.nanmean(perf_va, axis=1)))
        res = dict(window_ms=window_ms(cfg), ridge=float(ridges[jbest]),
                   ridge_interior=0 < jbest < len(ridges) - 1,
                   strf_train=float(np.nanmean(perf_tr[jbest])),
                   strf_valid=float(np.nanmean(perf_va[jbest])))
        if with_ln:
            ln_tr, ln_va = [], []
            for k in range(10):
                va = np.where(fold_of == k)[0]
                tr = np.where(fold_of != k)[0]
                if len(va) == 0:
                    continue
                rh = X @ wts[(jbest, k)]
                g = lowess_fit(rh[tr], r[tr])
                rn = g(rh)
                ln_tr.append(performance(Rall, rn, tr))
                ln_va.append(performance(Rall, rn, va))
            res.update(ln_train=float(np.mean(ln_tr)), ln_valid=float(np.mean(ln_va)))
        out.append(res)
    return out
