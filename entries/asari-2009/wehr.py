"""Wehr's A1 recordings in CRCNS ac-1: loading and the STRF / LN encoding models
of Asari & Zador (2009), Methods, "Neural encoding models" and "Model
performance" (Eqs. 46 to 53, Fig. 4).

The data are read in place from the public bucket: ``crcns-ac1.zip`` is opened
over HTTP range requests (fsspec + zipfile) and each member is read into
memory, reduced, and dropped. Nothing is written to disk.

Where each parameter comes from
-------------------------------
Paper (Methods, Neural encoding models; Model performance) and the claim's
criterion:

- spectrogram ``S(t, x) = 20 log10 |STFT|`` (Eq. 47); 3 bins per octave from
  0.40 kHz (17 bins, so 765 = 45 x 17 parameters);
- time bins of 2^k ms, k = 2..10, 45 bins in total, split as
  [45,0,...], [9,36,0,...], ..., [9,8,...,1] from near to distant past, giving
  windows of 180 ... 4052 ms (``BIN_SPLITS``);
- ridge regression, Eq. 50, via the eigendecomposition of S'S (identical
  to the SVD form of Eq. 50); 10-fold cross-validation; the ridge value chosen
  by the best performance on the validation folds;
- static nonlinearity by robust lowess with 5% span and five iterations, fitted
  on the training set and applied to the validation set (Eq. 51);
- performance by Eq. 53 with the predictable power of Eq. 52, on training
  (upper) and validation (lower) data.

Authors' code shipped in the zip (``wehr/Tools``; not linked from the paper):

- ``STRFanalysis.m``: per-trial responses are mean-subtracted for each
  stimulus, the model is fitted to the trial-averaged response, the
  spectrogram is mean-subtracted per frequency within each stimulus, the
  stimuli are concatenated and cut into 10 contiguous folds of equal length,
  one ridge value is chosen for all folds as the one with the best mean
  validation performance of the linear model, the LN model uses that same
  filter, and Eq. 53 is computed for each fold as
  (mean P_total - mean P_error) / mean P_pred over the fold's time bins, with
  P_pred(t) = (m rbar(t)^2 - P_total(t)) / (m - 1) (``LNperformance``);
- ``ViewResponse.m`` / ``GetEvoked.m``: the trace is median-filtered with a
  10-ms window (QX-314 blocks most spikes; the filter removes what is left),
  the evoked response is the trigger's duration from the trigger time, natural
  sounds are every stimulus other than "tuning curve", "silence" and
  "white noise"; the stimulus gets a Hann ramp of ``param.ramp`` ms at both
  ends (``MakeRamp.m``);
- ``logspectrogram.m``: frequencies 400 * 2^(k/3) Hz, the DFT evaluated at
  each centre frequency (no band integration).

Assumptions (each also stated in the notebook):

- cells: the paper's 20 cells cannot be identified from the files; we use every
  Wehr cell with at least two trials of the same natural sound, since Eq. 52
  needs m >= 2 (``select_cells``), and only those stimuli;
- 17 frequencies 400 * 2^(k/3) Hz, k = 0..16 (0.40 to 16.1 kHz): the code's
  rule with fmax = 22.1 kHz gives 18; the paper says 17 bins;
- response sampled in 4-ms bins (the finest time bin; mean of 16 samples of the
  4-kHz trace), the spectrogram computed every 4 ms with the window centred on
  the bin, the coarser history bins the mean of the 4-ms frames they cover;
- history before stimulus onset is set to the stimulus mean (zero after
  centring), so every window is scored on the same time bins ("all"); a second
  scoring keeps only bins at least 4052 ms after onset ("late"); folds by
  stimulus are a reading of the criterion;
- spectrogram window: Hann, 10 or 20 ms (the criterion's readings);
  ``logspectrogram.m`` uses a Hamming window of twice the time bin;
- ridge grid: 33 values, lambda = 10^(-6 ... 2) times the mean eigenvalue of
  the training S'S (a log grid wide enough that the choice is interior; edge
  hits are printed);
- lowess: local linear fit with tricube weights, one initial fit then five
  robustness iterations with bisquare weights (6 x median |residual|), as in
  Cleveland (1979); the fit is evaluated at 100 quantiles of the training
  predictions and linearly interpolated (Cleveland's ``delta`` device, a
  standard choice that cannot change a result), held constant outside the
  training range;
- a diagnostic only (not a reading): the same lowess without the robustness
  iterations, for the contiguous-fold, all-bins scheme only;
- (authors' code, not an assumption) per-fold performance averaged over folds
  as ``ViewSTRF.m`` does (``mean(strf.performance.linear, 2)``);
- the paper's numbers are means over cells.

No result depends on random draws (folds are contiguous blocks, or stimuli
assigned in order), so no generator is used.
"""
from __future__ import annotations

import functools
import io
import threading
import zipfile
from concurrent.futures import ThreadPoolExecutor

import fsspec
import numpy as np
import scipy.io as sio
from scipy.ndimage import median_filter

URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip"
DT = 0.004                      # s, finest time bin (2^2 ms); response bin (assumption)
FREQS = 400.0 * 2.0 ** (np.arange(17) / 3.0)   # Hz (logspectrogram.m rule, 17 bins)
BIN_SIZES = 2 ** np.arange(2, 11)              # ms, k = 2..10
BIN_SPLITS = [[45, 0, 0, 0, 0, 0, 0, 0, 0]] + [
    list(range(9, 9 - i, -1)) + [45 - sum(range(9, 9 - i, -1))] + [0] * (8 - i)
    for i in range(1, 9)]
WINDOWS_MS = [int(np.dot(s, BIN_SIZES)) for s in BIN_SPLITS]
MEDFILT_MS = 10                 # ViewResponse.m default ``smooth``
NONNATURAL = ("tuning curve", "silence", "white noise")   # ViewResponse.m
RIDGE_REL = 10.0 ** np.linspace(-6, 2, 33)
LOWESS_SPAN, LOWESS_ITER, LOWESS_GRID = 0.05, 5, 100

_local = threading.local()


def zf() -> zipfile.ZipFile:
    """One ZipFile per thread over HTTP range requests."""
    if not hasattr(_local, "z"):
        _local.z = zipfile.ZipFile(fsspec.open(URL, block_size=2**22).open())
    return _local.z


def _l(x):
    return list(np.atleast_1d(x))


@functools.lru_cache(maxsize=None)
def summary() -> list[dict]:
    """wehr/Summary.mat: one row per recording file."""
    m = sio.loadmat(io.BytesIO(zf().read("wehr/Summary.mat")), squeeze_me=True,
                    struct_as_record=False)
    rows = []
    for ei, e in enumerate(_l(m["experiment"])):
        for c in _l(e.cell):
            for f, d in zip(_l(c.file), _l(c.description)):
                f, d = str(f), str(d)
                rows.append(dict(experiment=ei, exp_description=str(e.description),
                                 reference=str(e.reference), cell=f.split("/")[1],
                                 file=f, stim=d.split(": Trial")[0].strip()))
    return rows


def select_cells(min_trials: int = 2) -> dict:
    """Cells with >= ``min_trials`` trials of some natural sound.

    Returns {cell: {stimulus description: [files]}} keeping only natural-sound
    stimuli with at least ``min_trials`` trials (Eq. 52 needs m >= 2).
    """
    out = {}
    for r in summary():
        if r["stim"].lower() in NONNATURAL:
            continue
        out.setdefault(r["cell"], {}).setdefault(r["stim"], []).append(r["file"])
    sel = {}
    for c, st in out.items():
        keep = {s: f for s, f in st.items() if len(f) >= min_trials}
        if keep:
            sel[c] = keep
    return sel


def read_trial(file: str) -> dict:
    """One recording file: the natural-sound trigger and the evoked trace.

    The trace (int16 * scale, mV) is median filtered (10 ms, GetEvoked.m),
    cut to the trigger's duration and averaged in 4-ms bins.
    """
    b = zf().read("wehr/" + file)
    m = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
    del b
    r = m["response"]
    sf = float(r.sf)
    tr = [t for t in _l(m["triggers"]) if "file" in t._fieldnames]
    assert len(tr) == 1, file
    t = tr[0]
    x = r.trace.astype(np.float64) * float(r.scale)
    raw_range = (float(x.min()), float(x.max()))
    w = int(round(MEDFILT_MS / 1000 * sf))
    x = median_filter(x - x.mean(), size=w, mode="constant") + x.mean()
    t0 = int(round(float(t.time) - 1))          # GetEvoked.m: samples, 1-based
    dur = float(t.param.duration) / 1000        # s
    nb = int(np.floor(dur / DT))
    spb = int(round(DT * sf))
    seg = x[t0:t0 + nb * spb]
    nb = len(seg) // spb
    resp = seg[:nb * spb].reshape(nb, spb).mean(1)
    return dict(file=file, stimfile=str(t.file), ramp=float(t.param.ramp),
                stim_sf=float(t.param.sf), duration=dur, sf=sf, unit=str(r.unit),
                n_samples=len(r.trace), raw_range=raw_range, resp=resp)


def spectrogram(y: np.ndarray, sf: float, n_bins: int, win_ms: float) -> np.ndarray:
    """Eq. 47 at 17 frequencies (FREQS), one frame per 4-ms bin.

    Hann window of ``win_ms`` (a reading), centred on each bin's centre, DFT
    evaluated at each centre frequency (logspectrogram.m), 20 log10 |.| in dB,
    then centred per frequency (STRFanalysis.m). Returns (n_bins, 17).
    """
    L = int(round(win_ms / 1000 * sf))
    n = np.arange(L)
    h = np.hanning(L + 2)[1:-1]
    ker = h[:, None] * np.exp(-2j * np.pi * FREQS[None, :] * n[:, None] / sf)
    c = np.round((np.arange(n_bins) + 0.5) * DT * sf).astype(int) - L // 2
    pad = np.concatenate([np.zeros(L), y, np.zeros(L + int(DT * sf) * 2)])
    out = np.empty((n_bins, len(FREQS)))
    for i0 in range(0, n_bins, 500):
        idx = c[i0:i0 + 500, None] + L + n[None, :]
        out[i0:i0 + 500] = np.abs(pad[idx] @ ker)
    S = 20 * np.log10(out + np.finfo(float).eps)
    return S - S.mean(0)


def read_stimulus(stimfile: str, ramp_ms: float, n_bins: int, wins_ms) -> dict:
    """Stimulus waveform with MakeRamp's Hann ramp; spectrograms for each window."""
    b = zf().read("wehr/Stimuli/" + stimfile)
    s = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)["stimulus"]
    del b
    y = np.asarray(s.samples, dtype=np.float64).ravel()
    sf = float(s.param.sf)
    a = int(round(ramp_ms * sf / 1000))
    if a >= 1:
        w = np.hanning(2 * a + 2)[1:-1]
        y[:a] *= w[:a]
        y[-a:] *= w[a:]
    out = dict(file=stimfile, sf=sf, n=len(y), dur=len(y) / sf, peak=float(np.abs(y).max()))
    for wm in wins_ms:
        out[wm] = spectrogram(y, sf, n_bins, wm)
    return out


def load_cells(sel: dict, wins_ms=(10, 20), threads: int = 4) -> tuple[dict, dict]:
    """Read every selected trial and stimulus (I/O in threads, one process).

    Returns (cells, stimuli). cells[c] = list of dict(stim, stimfile,
    R=(m, n_bins) mean-subtracted 4-ms responses); stimuli[file] = spectrograms.
    """
    files = [f for st in sel.values() for fl in st.values() for f in fl]
    with ThreadPoolExecutor(threads) as ex:
        trials = dict(zip(files, ex.map(read_trial, files)))
    cells, need = {}, {}
    for c, st in sel.items():
        cells[c] = []
        for name, fl in st.items():
            tr = [trials[f] for f in fl]
            sfiles = {t["stimfile"] for t in tr}
            assert len(sfiles) == 1, (c, name, sfiles)
            nb = min(len(t["resp"]) for t in tr)
            R = np.array([t["resp"][:nb] for t in tr])
            R = R - R.mean(1, keepdims=True)          # STRFanalysis.m, per trial
            sfile = tr[0]["stimfile"]
            need[sfile] = (max(need.get(sfile, (0, 0))[0], nb), tr[0]["ramp"])
            cells[c].append(dict(stim=name, stimfile=sfile, R=R, sf=tr[0]["sf"],
                                 unit=tr[0]["unit"], duration=tr[0]["duration"],
                                 raw_range=(min(t["raw_range"][0] for t in tr),
                                            max(t["raw_range"][1] for t in tr)),
                                 n_samples=[t["n_samples"] for t in tr]))
    del trials

    def _rs(item):
        f, (nb, ramp) = item
        return f, read_stimulus(f, ramp, nb, wins_ms)
    with ThreadPoolExecutor(min(threads, 2)) as ex:
        stimuli = dict(ex.map(_rs, need.items()))
    return cells, stimuli


# --------------------------------------------------------------------------
# design matrix and models
# --------------------------------------------------------------------------
def _edges(split):
    """Lag edges (in 4-ms frames) of the 45 history bins, near to far."""
    e = [0]
    for k, nk in zip(BIN_SIZES, split):
        for _ in range(nk):
            e.append(e[-1] + k // 4)
    return np.array(e)


def design(Sc: np.ndarray, split, rows: np.ndarray) -> np.ndarray:
    """Rows of the stimulus matrix (Eq. 48) for time bins ``rows``.

    Sc: cumulative sum of the zero-padded spectrogram (pad P frames of zeros
    before onset). Bin b covers lags [e_b, e_{b+1}) frames before and
    including the current frame; its value is the mean spectrogram there.
    """
    e = _edges(split)
    out = np.empty((len(rows), 45, Sc.shape[1]))
    for b in range(45):
        hi = rows + 1 - e[b]          # exclusive end index in padded frames (+1 for cumsum)
        lo = rows + 1 - e[b + 1]
        out[:, b] = (Sc[hi] - Sc[lo]) / (e[b + 1] - e[b])
    return out.reshape(len(rows), -1)


PAD = 1013  # frames of 4 ms in the longest window (4052 ms)


def prepare(cell: list, stimuli: dict, win_ms: float):
    """Concatenate a cell's stimuli: cumsum spectrograms, rbar, P_pred, stim id."""
    Scs, rbar, ppred, sid, rows = [], [], [], [], []
    off = 0
    for i, s in enumerate(cell):
        R = s["R"]
        m, nb = R.shape
        S = stimuli[s["stimfile"]][win_ms][:nb]
        Sp = np.vstack([np.zeros((PAD, S.shape[1])), S])
        Sc = np.vstack([np.zeros((1, S.shape[1])), np.cumsum(Sp, 0)])
        Scs.append(Sc)
        rb = R.mean(0)
        pt = (R ** 2).mean(0)
        rbar.append(rb)
        ppred.append((m * rb ** 2 - pt) / (m - 1))   # Eq. 52 / LNperformance
        sid.append(np.full(nb, i))
        rows.append(np.arange(nb) + PAD + off)
        off += Sc.shape[0]
    Sc = np.vstack(Scs)
    return Sc, np.concatenate(rbar), np.concatenate(ppred), np.concatenate(sid), np.concatenate(rows)


def folds_contiguous(n: int, k: int = 10) -> np.ndarray:
    """STRFanalysis.m: k blocks of round(n/k) bins, the last takes the rest."""
    f = np.empty(n, int)
    sz = int(round(n / k))
    for i in range(k):
        f[i * sz:(i + 1) * sz if i < k - 1 else n] = i
    return f


def folds_by_stimulus(sid: np.ndarray, k: int = 10) -> np.ndarray:
    """Stimulus i goes to fold i mod k (fewer folds if fewer stimuli)."""
    return sid % min(k, sid.max() + 1)


def perf(rbar, rhat, ppred):
    """Eq. 53 over a set of bins: (P_total - P_error) / P_pred, means over bins.

    P_total - P_error = <2 r_j rhat - rhat^2>_j = 2 rbar rhat - rhat^2.
    """
    return np.sum(2 * rbar * rhat - rhat ** 2, 0) / np.sum(ppred)


def lowess_fit(x, y, span=LOWESS_SPAN, iters=LOWESS_ITER, ngrid=LOWESS_GRID):
    """Robust lowess (Cleveland 1979) of y on x; returns (grid, fitted values)."""
    o = np.argsort(x)
    xs, ys = x[o], y[o]
    n = len(xs)
    k = max(int(np.ceil(span * n)), 3)
    g = np.unique(np.quantile(xs, np.linspace(0, 1, ngrid)))
    # nearest-k window [l, l+k) for each grid point: the smallest l with
    # xs[l] + xs[l+k-1] >= 2 g, or the one before it (vectorized bisection)
    lo = np.zeros(len(g), int)
    hi = np.full(len(g), n - k)
    while np.any(lo < hi):
        mid = (lo + hi) // 2
        right = xs[mid] + xs[mid + k - 1] < 2 * g
        lo = np.where(right & (lo < hi), mid + 1, lo)
        hi = np.where(~right & (lo < hi), mid, hi)
    prev = np.maximum(lo - 1, 0)
    c_lo = np.maximum(g - xs[lo], xs[lo + k - 1] - g)
    c_pr = np.maximum(g - xs[prev], xs[prev + k - 1] - g)
    L = np.where(c_pr < c_lo, prev, lo)
    idx = L[:, None] + np.arange(k)[None, :]
    X = xs[idx]
    Y = ys[idx]
    d = np.abs(X - g[:, None])
    dmax = d.max(1, keepdims=True)
    dmax[dmax == 0] = 1
    wt = (1 - np.clip(d / dmax, 0, 1) ** 3) ** 3
    rob = np.ones(n)
    for it in range(iters + 1):
        w = wt * rob[idx]
        sw = w.sum(1)
        mx = (w * X).sum(1) / sw
        my = (w * Y).sum(1) / sw
        vx = (w * (X - mx[:, None]) ** 2).sum(1)
        cxy = (w * (X - mx[:, None]) * (Y - my[:, None])).sum(1)
        beta = np.where(vx > 1e-12 * np.maximum(1, mx ** 2), cxy / np.where(vx > 0, vx, 1), 0)
        fit = my + beta * (g - mx)
        if it == iters:
            break
        res = ys - np.interp(xs, g, fit)
        s = np.median(np.abs(res))
        if s == 0:
            break
        u = res / (6 * s)
        rob = np.where(np.abs(u) < 1, (1 - u ** 2) ** 2, 0)
    return g, fit


def fit_window(X, rbar, ppred, schemes, ridge_rel=RIDGE_REL, nonrobust=("contig/all",)):
    """Ridge STRF (Eq. 50) and LN (Eq. 51) for one window under several fold schemes.

    X: (n, 765) stimulus matrix (Eq. 48); schemes: {name: fold id per bin, -1 =
    bin not used}. Grams are computed once per atom (bins sharing all fold ids)
    and summed. For each scheme returns per-fold performance (columns: training
    = upper, validation = lower) of STRF and LN at the one ridge value with the
    best mean validation performance (STRFanalysis.m), and that value.
    """
    names = list(schemes)
    F = np.stack([schemes[k] for k in names], 1)
    atoms, inv = np.unique(F, axis=0, return_inverse=True)
    inv = inv.ravel()
    p = X.shape[1]
    Ga = np.zeros((len(atoms), p, p))
    Ba = np.zeros((len(atoms), p))
    for a in range(len(atoms)):
        ii = np.flatnonzero(inv == a)
        if atoms[a].max() < 0:
            continue
        Xa = X[ii]
        Ga[a] = Xa.T @ Xa
        Ba[a] = Xa.T @ rbar[ii]
    out = {}
    for si, name in enumerate(names):
        fold = schemes[name]
        K = fold.max() + 1
        use = atoms[:, si] >= 0
        Gt, Bt = Ga[use].sum(0), Ba[use].sum(0)
        Wf = np.empty((K, p, len(ridge_rel)))
        lam = np.empty((K, len(ridge_rel)))
        vperf = np.empty((K, len(ridge_rel)))
        for f in range(K):
            m = atoms[:, si] == f
            ev, V = np.linalg.eigh(Gt - Ga[m].sum(0))
            ev = np.clip(ev, 0, None)
            lam[f] = ridge_rel * ev.mean()
            z = V.T @ (Bt - Ba[m].sum(0))
            Wf[f] = V @ (z[:, None] / (ev[:, None] + lam[f][None, :]))
            v = np.flatnonzero(fold == f)
            vperf[f] = perf(rbar[v, None], X[v] @ Wf[f], ppred[v])
        best = int(np.argmax(vperf.mean(0)))     # one value for all folds
        r = dict(best=best, ridge_rel=float(ridge_rel[best]), nfold=int(K))
        lin, ln, ln0 = (np.empty((K, 2)) for _ in range(3))
        P = X @ Wf[:, :, best].T                  # (n, K): every fold's filter on all bins
        for f in range(K):
            t = np.flatnonzero((fold >= 0) & (fold != f))
            v = np.flatnonzero(fold == f)
            pt, pv = P[t, f], P[v, f]
            lin[f] = perf(rbar[t], pt, ppred[t]), perf(rbar[v], pv, ppred[v])
            for arr, it in ((ln, LOWESS_ITER), (ln0, 0)):
                if it == 0 and name not in nonrobust:
                    arr[f] = np.nan
                    continue
                g, fit = lowess_fit(pt, rbar[t], iters=it)
                arr[f] = (perf(rbar[t], np.interp(pt, g, fit), ppred[t]),
                          perf(rbar[v], np.interp(pv, g, fit), ppred[v]))
        r["strf"], r["ln"], r["ln_nonrobust"] = lin, ln, ln0
        out[name] = r
    return out


_DATA = {}


def run_cell(args):
    """All windows and fold schemes for one cell and one spectrogram window.

    Schemes: folds as 10 contiguous blocks or by stimulus, scoring every bin
    from stimulus onset ("all"); and contiguous folds over only the bins at
    least 4052 ms after onset ("late", so no window reaches before onset). Uses ``_DATA`` (set before
    forking) to avoid pickling the data.
    """
    cell, win_ms = args
    Sc, rbar, ppred, sid, rows = prepare(_DATA["cells"][cell], _DATA["stim"], win_ms)
    late = np.concatenate([np.arange(s["R"].shape[1]) >= PAD for s in _DATA["cells"][cell]])
    schemes = {}
    schemes["contig/all"] = folds_contiguous(len(rows))
    schemes["stim/all"] = folds_by_stimulus(sid)
    fl = np.full(len(rows), -1)
    fl[late] = folds_contiguous(int(late.sum()))
    schemes["contig/late"] = fl
    res = []
    for sp in BIN_SPLITS:
        X = design(Sc, sp, rows)
        res.append(fit_window(X, rbar, ppred, schemes))
        del X
    snr = float(ppred.sum() / (rbar ** 2).sum())
    return cell, win_ms, res, snr, int(late.sum()), len(rows)
