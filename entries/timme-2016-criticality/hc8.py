"""Loading and measures for CRCNS hc-8, the culture recordings of Timme et al. (2016).

Timme, Marshall, Bennett, Ripp, Lautzenhiser & Beggs (2016), "Criticality Maximizes Complexity in
Neural Tissue", Front. Physiol. 7:425, doi:10.3389/fphys.2016.00425. Data set doi:10.6080/K0PC308P.

The data set is one zip, hc-8/live/Data.zip, of 435 MATLAB files CultureXDIVY.mat, each with a
struct `data` whose `spikes` is a cell array of spike times per neuron in 0.05 ms bins. The zip is
read in place from the public S3 bucket over range requests; nothing is written to disk.

The measures port the NCC MATLAB toolbox that the paper cites (Marshall et al., 2016; "NCC Toolbox
Version 1", June 14th, 2016, from the Software page of nicholastimme.com, zip sha256
b7c912f8154f70fc82b13ab1725ed191935ed2877256cadd7e39f66737be294b, the version the claims file
read). Each function names the toolbox function it ports. Where the parameters come from:

- First 59 min of each recording, rebinning to the mean network-wide ISI, avalanches as runs of
  active bins: Methods 2.2 and 2.3 (claims file, common method). The ISI is rounded to a whole
  number of 0.05 ms bins, as `rebin.m` requires (claims file, common detail 1, a standard choice).
- Cuts before power-law fits (values >= 4 seen at least 20 times), MLE on tau in [1, 5] to 0.001,
  500 surrogates and p >= 0.2, the support search largest range first: Methods 2.7, `plparams.m`,
  `plmle.m`, `pvcalc.m`.
- Size given duration by weighted least squares over the fitted duration range, weights the number
  of avalanches per duration: Methods 2.7, `sizegivdurwls.m`.
- Shape collapse of mean profiles of durations >= 4 seen >= 20 times, exponent in [0, 4] refined
  to 0.001, 1000 interpolation points, curvature 2 x the quadratic coefficient: Methods 2.8,
  `avgshapes.m`, `avshapecollapse.m`. The claims file takes the absolute value (common detail 6).
- Complexity with the sub-sampling correction (randomized data subtracted, cut at the first peak):
  Methods 2.9, `complexity.m`. The number of random subsets per subset size is a parameter;
  Methods 2.9 give 100.
- Randomizations jitter (SD in rebinned bins), wrap, Poisson, swap and shuffling: Methods 2.5,
  `randomizeasdf2.m` (shuffling is its `swap2`, which is what Methods 2.5 describe). Jitter moves
  one spike at a time, as `randomizeasdf2.m` does.
- Branching ratio B_new with delays 1 to 8 and 0 <= A(t) <= 10: Methods 2.11, `brestimate.m`.
- Susceptibility: Eq. 14 and the claims file's common detail 5.
- Sub-sampling: 30 random sub-samples from 40% to 100% of the neurons, weighted least squares on
  1/N with weight N, the intercept kept: Methods 2.10.
"""

from __future__ import annotations

import hashlib
import io
import re
import zipfile
from functools import lru_cache

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy import optimize, signal, sparse

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-8/live"
ZIP_URL = f"{BUCKET}/Data.zip"
DATASET_ID = "hc-8"
DATASET_VERSION = "unversioned"  # CRCNS data sets carry no versions (docs/archives.md); the MD5 pins the zip
ZIP_MD5 = "bd4e2a8685df3e55e1a3c04fbe09d9ce"  # hc-8/live/checksums.md5
BIN_MS = 0.05            # data description: spike times in 0.05 ms bins
ANALYSIS_MIN = 59.0      # Methods 2.2: first 59 min of each recording
ANALYSIS_BINS = int(round(ANALYSIS_MIN * 60e3 / BIN_MS))

MIN_VALUE = 4            # Methods 2.7: sizes or durations less than 4 removed
MIN_COUNT = 20           # Methods 2.7: values seen fewer than 20 times removed
N_SURROGATES = 500       # Methods 2.7
P_CRIT = 0.2             # Methods 2.7
BR_DELAYS = np.arange(1, 9)      # Methods 2.11: 1 <= k <= 8
BR_ACT_MAX_CULTURE = 10          # Methods 2.11: 0 <= A(t) <= 10 for the culture data
BR_ACT_MAX_MODEL = 5             # Methods 2.11: 0 <= A(t) <= 5 for the cortical branching model


# ----------------------------------------------------------------------------------------------
# Loading

@lru_cache(maxsize=1)
def _zip():
    f = fsspec.open(ZIP_URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def recording_names() -> list[str]:
    """Members CultureXDIVY.mat of Data.zip, sorted by culture then DIV."""
    names = [i.filename for i in _zip().infolist() if i.filename.endswith(".mat")]
    return sorted(names, key=lambda n: culture_div(n))


def culture_div(name: str) -> tuple[int, int]:
    m = re.search(r"Culture(\d+)DIV(\d+)\.mat$", name)
    return int(m.group(1)), int(m.group(2))


def load(name: str, zf: zipfile.ZipFile | None = None) -> dict:
    """One recording: spike times per neuron (0.05 ms bins, int64) and the struct's metadata."""
    zf = zf or _zip()
    m = sio.loadmat(io.BytesIO(zf.read(name)), squeeze_me=True, struct_as_record=False)
    d = m["data"]
    spikes = [np.atleast_1d(np.asarray(s, dtype=np.int64)) for s in np.atleast_1d(d.spikes)]
    return dict(name=name, spikes=spikes, nNeurons=int(d.nNeurons), binsize=float(d.binsize),
                nbins=int(d.nbins), recordingID=str(d.recordingID), datatype=str(d.datatype),
                expsys=str(d.expsys), channel=np.atleast_1d(d.channel),
                wave_clus=d.wave_ClusParams)


def open_zip() -> zipfile.ZipFile:
    """A fresh handle on the zip, for use in another thread or process."""
    return zipfile.ZipFile(fsspec.open(ZIP_URL, block_size=2**20).open())


# ----------------------------------------------------------------------------------------------
# Rebinning and avalanches

def first_window(spikes: list[np.ndarray], nbins: int = ANALYSIS_BINS) -> list[np.ndarray]:
    """Spikes in the first 59 min (bins 1..nbins in the 1-based convention of the files)."""
    return [s[(s >= 1) & (s <= nbins)] for s in spikes]


def network_isi_bins(spikes: list[np.ndarray]) -> float:
    """Mean interval between consecutive spikes of all neurons pooled, in 0.05 ms bins (Methods 2.3).

    Spikes of different neurons in the same 0.05 ms bin give intervals of 0, which are kept."""
    t = np.sort(np.concatenate(spikes))
    return float(np.mean(np.diff(t))) if t.size > 1 else np.nan


def rebin(spikes: list[np.ndarray], factor: int, nbins: int = ANALYSIS_BINS):
    """`rebin.m`: new time ceil(t / factor), duplicates within a neuron merged."""
    new = [np.unique(np.ceil(s / factor).astype(np.int64)) for s in spikes]
    return new, int(np.ceil(nbins / factor))


def activity(raster: list[np.ndarray], nbins: int) -> np.ndarray:
    """A(t), the number of active neurons per bin, for bins 1..nbins (index 0 is bin 1)."""
    a = np.zeros(nbins + 1, dtype=np.int32)
    for s in raster:
        np.add.at(a, s, 1)
    return a[1:]


def avalanches(act: np.ndarray):
    """`avprops.m` on the activity series: runs of consecutive active bins.

    Returns sizes, durations, start indices (0-based bin index) of each avalanche."""
    on = act > 0
    d = np.diff(np.concatenate([[0], on.astype(np.int8), [0]]))
    starts = np.flatnonzero(d == 1)
    ends = np.flatnonzero(d == -1)
    dur = ends - starts
    cs = np.concatenate([[0], np.cumsum(act, dtype=np.int64)])
    size = cs[ends] - cs[starts]
    return size, dur, starts


# ----------------------------------------------------------------------------------------------
# Power-law fitting (plmle.m, pvcalc.m, plparams.m)

def apply_cuts(x: np.ndarray) -> np.ndarray:
    """demoempdata.m: keep values >= 4 that occur at least 20 times (Methods 2.7)."""
    u, c = np.unique(x, return_counts=True)
    keep = u[(c >= MIN_COUNT) & (u >= MIN_VALUE)]
    return x[np.isin(x, keep)]


class _PLData:
    """Histogram of integer data with prefix sums of x^-tau on the 0.001 tau grid of plmle.m."""

    TAUS = np.round(np.arange(1000, 5001) / 1000.0, 3)

    def __init__(self, x: np.ndarray):
        x = np.asarray(x, dtype=np.int64)
        self.x = x
        self.xmax_all = int(x.max())
        self.counts = np.bincount(x, minlength=self.xmax_all + 1).astype(np.float64)
        self.cum_n = np.concatenate([[0], np.cumsum(self.counts)])          # cum_n[v+1] = #x <= v
        logv = np.log(np.maximum(np.arange(self.xmax_all + 1), 1))
        self.cum_log = np.concatenate([[0], np.cumsum(self.counts * logv)])
        self.logv = logv
        self._W = None

    def W(self):
        if self._W is None:
            v = np.arange(1, self.xmax_all + 1, dtype=np.float64)
            # cumulative sums over v of v^-tau, rows tau; column j is sum over 1..j
            w = np.exp(-np.outer(self.TAUS, np.log(v)))
            self._W = np.concatenate([np.zeros((len(self.TAUS), 1)), np.cumsum(w, axis=1)], axis=1)
        return self._W

    def mle(self, xmin: np.ndarray, xmax: np.ndarray) -> np.ndarray:
        """plmle.m for integer data, vectorized over candidate supports: coarse-to-fine to 0.001."""
        xmin = np.atleast_1d(xmin).astype(np.int64)
        xmax = np.atleast_1d(xmax).astype(np.int64)
        W = self.W()
        n = self.cum_n[xmax + 1] - self.cum_n[xmin]
        slog = self.cum_log[xmax + 1] - self.cum_log[xmin]
        mlog = slog / n

        def L(idx):  # idx: (ncand, m) tau indices
            Z = W[idx, xmax[:, None]] - W[idx, xmin[:, None] - 1]
            return -np.log(Z) - self.TAUS[idx] * mlog[:, None]

        lo = np.zeros(len(xmin), dtype=np.int64)
        hi = np.full(len(xmin), 4000, dtype=np.int64)
        best = None
        for step in (100, 10, 1):
            m = (hi - lo) // step + 1
            mmax = int(m.max())
            idx = lo[:, None] + step * np.arange(mmax)[None, :]
            valid = np.arange(mmax)[None, :] < m[:, None]
            idx = np.where(valid, idx, lo[:, None])
            Lv = np.where(valid, L(idx), -np.inf)
            j = np.argmax(Lv, axis=1)
            best = idx[np.arange(len(j)), j]
            # the next level spans the neighbours of the best value (plmle.m edge rules)
            jl = np.where(j == 0, 0, j - 1)
            jh = np.where(j == m - 1, m - 1, j + 1)
            lo = lo + step * jl
            hi = lo + step * (jh - jl)
        return self.TAUS[best]

    def cdf_pair(self, xmin: int, xmax: int, tau: float):
        v = np.arange(xmin, xmax + 1)
        pdf_x = self.counts[xmin:xmax + 1]
        n = pdf_x.sum()
        pdf_fit = v.astype(float) ** (-tau)
        pdf_fit /= pdf_fit.sum()
        return pdf_x, int(n), pdf_fit

    def ks(self, xmin: int, xmax: int, tau: float) -> float:
        pdf_x, n, pdf_fit = self.cdf_pair(xmin, xmax, tau)
        return float(np.max(np.abs(np.cumsum(pdf_x / n) - np.cumsum(pdf_fit))))


def pvcalc(pl: _PLData, xmin: int, xmax: int, tau: float, rng: np.random.Generator,
           n_samples: int = N_SURROGATES):
    """pvcalc.m for integer data: surrogates drawn from the fitted truncated power law with the
    data's number of events, KS of each against the fit; p is the fraction at least as large as
    the data's KS. All surrogates are drawn (pvcalc.m stops early only when the decision is
    already certain, which does not change whether p >= 0.2)."""
    pdf_x, n, pdf_fit = pl.cdf_pair(xmin, xmax, tau)
    emp = np.max(np.abs(np.cumsum(pdf_x / n) - np.cumsum(pdf_fit)))
    samp = rng.multinomial(n, pdf_fit, size=n_samples)
    ks = np.max(np.abs(np.cumsum(samp, axis=1) / n - np.cumsum(pdf_fit)[None, :]), axis=1)
    return float(np.mean(emp <= ks)), float(emp)


def support_order(x: np.ndarray) -> np.ndarray:
    """plparams.m: all pairs of unique values, without the pair of each value with the next one,
    ranked by (log(xmax/xmin) / log(max ratio))^2, largest first (stable order for ties)."""
    u = np.unique(x)
    i, j = np.triu_indices(len(u), k=2)       # drops adjacent pairs (k = 1) and identical values
    pairs = np.column_stack([u[i], u[j]])
    r = np.log(pairs[:, 1] / pairs[:, 0])
    r = r / r.max()
    order = np.argsort(-(r ** 2), kind="stable")
    return pairs[order]


def plparams(x: np.ndarray, rng: np.random.Generator, screen: float = 1.2, chunk: int = 2000):
    """plparams.m: the largest support (in the ranking above) whose truncated power-law fit gives
    p >= 0.2.

    Screening, to keep the search fast: a support whose data KS exceeds screen / sqrt(n) is
    rejected without surrogates. For sqrt(n) KS above 1.2 the asymptotic Kolmogorov probability
    is 0.11 < 0.2, and the KS of discrete surrogates against a fixed distribution is smaller
    still, so these supports would be rejected by pvcalc as well (a numerical shortcut, not a
    change of method).

    Returns dict with tau, xmin, xmax, p, n_tried (supports evaluated), n (events in range)."""
    x = np.asarray(x, dtype=np.int64)
    out = dict(tau=np.nan, xmin=np.nan, xmax=np.nan, p=np.nan, ks=np.nan, n=0, n_tried=0)
    if np.unique(x).size < 3:
        return out
    pl = _PLData(x)
    pairs = support_order(x)
    tried = 0
    for c0 in range(0, len(pairs), chunk):
        pc = pairs[c0:c0 + chunk]
        taus = pl.mle(pc[:, 0], pc[:, 1])
        for (xmin, xmax), tau in zip(pc, taus):
            tried += 1
            pdf_x, n, pdf_fit = pl.cdf_pair(int(xmin), int(xmax), float(tau))
            emp = np.max(np.abs(np.cumsum(pdf_x / n) - np.cumsum(pdf_fit)))
            if emp * np.sqrt(n) > screen:
                continue
            p, _ = pvcalc(pl, int(xmin), int(xmax), float(tau), rng)
            if p >= P_CRIT:
                return dict(tau=float(tau), xmin=int(xmin), xmax=int(xmax), p=p, ks=float(emp),
                            n=int(n), n_tried=tried)
    out["n_tried"] = tried
    return out


def plmle_full(x: np.ndarray) -> float:
    """plmle.m over all of x (no range search), as Methods 2.10 use for sub-samples."""
    x = np.asarray(x, dtype=np.int64)
    if np.unique(x).size < 2:
        return np.nan
    pl = _PLData(x)
    return float(pl.mle(np.array([x.min()]), np.array([x.max()]))[0])


def sizegivdur(size: np.ndarray, dur: np.ndarray, durmin, durmax) -> float:
    """sizegivdurwls.m: slope of log10 mean size on log10 duration, weighted by the number of
    avalanches per duration, over the unique durations from durmin to durmax."""
    if not np.isfinite(durmin) or not np.isfinite(durmax):
        return np.nan
    u, inv, c = np.unique(dur, return_inverse=True, return_counts=True)
    ms = np.bincount(inv, weights=size) / c
    sel = (u >= durmin) & (u <= durmax)
    if sel.sum() < 2:
        return np.nan
    X = np.column_stack([np.log10(u[sel]), np.ones(sel.sum())])
    y = np.log10(ms[sel])
    w = np.sqrt(c[sel].astype(float))
    beta, *_ = np.linalg.lstsq(X * w[:, None], y * w, rcond=None)
    return float(beta[0])


# ----------------------------------------------------------------------------------------------
# Shape collapse (avgshapes.m, avshapecollapse.m)

def mean_profiles(act: np.ndarray, size, dur, starts, min_dur: int = 4, min_count: int = 20):
    """avgshapes.m with 'cutoffs', 4, 20: the mean profile of each duration >= 4 seen >= 20 times."""
    u, c = np.unique(dur, return_counts=True)
    keep = u[(u >= min_dur) & (c >= min_count)]
    prof = []
    for T in keep:
        st = starts[dur == T]
        idx = st[:, None] + np.arange(T)[None, :]
        prof.append(act[idx].mean(axis=0))
    return prof


def shape_collapse(profiles: list[np.ndarray], n_interp: int = 1000):
    """avshapecollapse.m: the exponent 1/sigma nu z in [0, 4] (refined to 0.001) minimizing the
    mean over scaled time of the variance across scaled profiles over the squared range, and the
    curvature, 2 x the leading coefficient of a quadratic fit of the mean collapsed profile."""
    if len(profiles) < 2:
        return np.nan, np.nan
    T = np.array([len(p) for p in profiles], dtype=float)
    grid = np.linspace(0, 1, n_interp)
    interp = np.array([np.interp(grid, np.linspace(0, 1, len(p)), p) for p in profiles])
    logT = np.log(T)

    def errors(xs):
        scale = np.exp(np.outer(1 - xs, logT))            # (nx, nprof)
        S = scale[:, :, None] * interp[None, :, :]        # (nx, nprof, ninterp)
        var = S.var(axis=1, ddof=1).mean(axis=1)
        rng_ = S.max(axis=(1, 2)) - S.min(axis=(1, 2))
        return var / rng_ ** 2

    lo, hi = 0.0, 4.0
    best = None
    for it in range(1, 4):
        xs = np.round(np.arange(lo, hi + 1e-9, 10.0 ** (-it)), 6)
        e = errors(xs)
        best = xs[int(np.argmin(e))]
        lo, hi = best - 10.0 ** (1 - it), best + 10.0 ** (1 - it)
    S = np.exp((1 - best) * logT)[:, None] * interp
    coeffs = np.polyfit(grid, S.mean(axis=0), 2)
    return float(best), float(2 * coeffs[0])


# ----------------------------------------------------------------------------------------------
# Complexity (complexity.m)

def _states(raster_bins: list[np.ndarray], bins: np.ndarray):
    """Unique network states over the given bins: a sparse (n_unique x n_neurons) matrix and the
    count of each state."""
    n = len(raster_bins)
    pos = {}
    index = np.full(bins.max() + 2 if bins.size else 1, -1, dtype=np.int64)
    index[bins] = np.arange(bins.size)
    rows, cols = [], []
    for j, s in enumerate(raster_bins):
        r = index[s[s < index.size]]
        r = r[r >= 0]
        rows.append(r)
        cols.append(np.full(r.size, j))
    rows = np.concatenate(rows) if rows else np.array([], dtype=np.int64)
    cols = np.concatenate(cols) if cols else np.array([], dtype=np.int64)
    X = sparse.csr_matrix((np.ones(rows.size, dtype=np.int64), (rows, cols)), shape=(bins.size, n))
    return X


def _unique_rows(X: sparse.csr_matrix, rng: np.random.Generator):
    """Unique rows of a 0/1 sparse matrix with their counts (hash on random 62-bit weights)."""
    w = rng.integers(1, 2**62, size=X.shape[1], dtype=np.int64)
    h = X @ w
    _, first, cnt = np.unique(h, return_index=True, return_counts=True)
    return X[first], cnt


def _integration_curve(U: sparse.csr_matrix, cnt: np.ndarray, nT: int, n_subsets: int,
                       rng: np.random.Generator) -> np.ndarray:
    """Mean integration of random k-subsets for k = 1..N (k = 1 is 0), as complexity.m."""
    N = U.shape[1]
    nsp = np.asarray(U.multiply(cnt[:, None]).sum(axis=0)).ravel().astype(float)
    p1 = nsp / nT
    with np.errstate(divide="ignore", invalid="ignore"):
        ent = -(p1 * np.log2(p1)) - ((1 - p1) * np.log2(1 - p1))
    ent = np.nan_to_num(ent)
    curve = np.zeros(N)
    w_all = rng.integers(1, 2**62, size=N, dtype=np.int64)
    Ur = U.tocsr()
    from math import comb
    for k in range(2, N + 1):
        if comb(N, k) <= n_subsets:
            from itertools import combinations
            subsets = [np.array(c) for c in combinations(range(N), k)]
        else:
            subsets = [rng.permutation(N)[:k] for _ in range(n_subsets)]
        W = np.zeros((N, len(subsets)), dtype=np.int64)
        for i, sub in enumerate(subsets):
            W[sub, i] = w_all[sub]
        H = np.ascontiguousarray((Ur @ W).T)   # hash of each unique state restricted to each subset
        vals = np.empty(len(subsets))
        for i, sub in enumerate(subsets):
            inv, _ = pd.factorize(H[i])
            p = np.bincount(inv, weights=cnt) / nT
            vals[i] = ent[sub].sum() + np.sum(p * np.log2(p))
        curve[k - 1] = vals.mean()
    return curve


def complexity(X: sparse.csr_matrix, n_subsets: int, rng: np.random.Generator,
               subsamp_correct: bool = True, return_variants: bool = False):
    """complexity.m on a (time bins x neurons) 0/1 matrix.

    With the correction, the integration curve of the data with each neuron's bins permuted
    independently is subtracted, and the curve is cut after the first peak of I(k)/(k-1)
    (findpeaks with a minimum peak distance of max(3, round(0.1 N))). Returns (Cn, curve), or
    with return_variants a dict: 'cut' (complexity.m), 'uncut' (the corrected curve without the
    cut), 'raw' (no correction), 'k_kept' (subset sizes kept by the cut) and 'N'."""
    nT, N = X.shape
    U, cnt = _unique_rows(X, rng)
    curve = _integration_curve(U, cnt, nT, n_subsets, rng)
    Cn = np.sum(np.linspace(0, curve[-1], N) - curve) / N
    if not subsamp_correct:
        return float(Cn), curve
    Xc = X.tocsc()
    rows, cols = [], []
    for j in range(N):
        r = Xc.indices[Xc.indptr[j]:Xc.indptr[j + 1]]
        perm = rng.permutation(nT)
        rows.append(perm[r])
        cols.append(np.full(r.size, j))
    Xr = sparse.csr_matrix((np.ones(sum(r.size for r in rows), dtype=np.int64),
                            (np.concatenate(rows), np.concatenate(cols))), shape=(nT, N))
    Ur, cntr = _unique_rows(Xr, rng)
    curve_r = _integration_curve(Ur, cntr, nT, n_subsets, rng)
    corr = curve - curve_r
    m = corr[1:] / np.arange(1, N)
    mpd = max(3, int(np.floor(0.1 * N + 0.5)))
    cut = N + 1
    if len(m) >= 3:
        locs, _ = signal.find_peaks(m, distance=mpd)
        if len(locs):
            cut = locs[0] + 1 + 2          # 1-based Cut of complexity.m
    kept = corr[:cut - 1]
    Cn = np.sum(np.linspace(0, kept[-1], len(kept)) - kept) / len(kept)
    if return_variants:
        uncut = np.sum(np.linspace(0, corr[-1], N) - corr) / N
        raw = np.sum(np.linspace(0, curve[-1], N) - curve) / N
        return dict(cut=float(Cn), uncut=float(uncut), raw=float(raw), k_kept=len(kept), N=N)
    return float(Cn), corr


def raster_matrix(raster: list[np.ndarray], bins: np.ndarray) -> sparse.csr_matrix:
    """(len(bins) x neurons) 0/1 matrix of the raster restricted to the given 1-based bins."""
    return _states(raster, bins)


# ----------------------------------------------------------------------------------------------
# Randomizations (randomizeasdf2.m), on rebinned rasters with bins 1..nbins

def rand_jitter(raster, nbins, sd_bins, rng, counts=None):
    """Jitter as randomizeasdf2.m 'jitter': the spikes of a neuron are moved one at a time, in a
    random order, each by round(sd * N(0,1)) bins from its original time, and a move is undone
    when it would leave the recording (before bin 1 or after nbins) or land on a bin the neuron's
    train occupies at that moment (spikes already moved included, bins they left free). This
    keeps the spike count, as Methods 2.5 require. counts, if a list, receives (spikes, spikes
    drawn a move of 0 bins, moves undone)."""
    out = []
    n_all = n_zero = n_undone = 0
    for s in raster:
        n = s.size
        if n == 0:
            out.append(s)
            continue
        order = rng.permutation(n)
        step = np.round(sd_bins * rng.standard_normal(n)).astype(np.int64)
        res = s.tolist()
        new_all = (s + step).tolist()
        occ = set(res)
        for k in order.tolist():
            new = new_all[k]
            old = res[k]
            if new == old:
                continue
            if new < 1 or new > nbins or new in occ:
                n_undone += 1
                continue
            occ.discard(old)
            occ.add(new)
            res[k] = new
        n_all += n
        n_zero += int(np.sum(step == 0))
        out.append(np.sort(np.array(res, dtype=np.int64)))
    if counts is not None:
        counts.append((n_all, n_zero, n_undone))
    return out


def rand_wrap(raster, nbins, rng):
    """Wrap: each train cut at a random point and the two parts exchanged."""
    out = []
    for s in raster:
        cut = rng.integers(1, nbins + 1)
        out.append(np.sort(np.where(s > cut, s - cut, s + (nbins - cut))))
    return out


def rand_poisson(raster, nbins, rng):
    """Poisson: each neuron's spikes placed at distinct uniformly random bins."""
    return [np.sort(rng.choice(nbins, size=s.size, replace=False) + 1) for s in raster]


def rand_swap(raster, nbins, rng):
    """Swap: neuron labels of all spikes permuted (each neuron keeps its count, each bin its
    activity), then every spike that landed on a neuron already spiking in that bin is traded
    with a random other spike when the trade is valid, as randomizeasdf2.m 'swap'."""
    lab = np.concatenate([np.full(s.size, j) for j, s in enumerate(raster)])
    t = np.concatenate(raster)
    lab = lab[rng.permutation(lab.size)]
    N = len(raster)
    for _ in range(1000):
        key = t * N + lab
        order = np.argsort(key, kind="stable")
        dup = np.flatnonzero(np.diff(key[order]) == 0)
        if dup.size == 0:
            break
        keys_set = set(key.tolist())
        bad = order[dup + 1]
        for i in bad:
            for _try in range(200):
                j = rng.integers(lab.size)
                if lab[j] == lab[i] or t[j] == t[i]:
                    continue
                k1 = t[i] * N + lab[j]
                k2 = t[j] * N + lab[i]
                if k1 in keys_set or k2 in keys_set:
                    continue
                keys_set.discard(t[j] * N + lab[j])
                keys_set.add(k1)
                keys_set.add(k2)
                lab[i], lab[j] = lab[j], lab[i]
                break
    return [np.sort(t[lab == j]) for j in range(N)]


def rand_shuffle(raster, nbins, rng):
    """Neuron shuffling (randomizeasdf2.m 'swap2', Methods 2.5): in each bin the active count is
    kept and the active neurons drawn uniformly without replacement from all neurons."""
    N = len(raster)
    act = activity(raster, nbins)
    bins = np.flatnonzero(act) + 1
    a = act[bins - 1]
    # random keys per (bin, neuron); the a smallest keys in each bin are the active neurons
    out_t, out_n = [], []
    for start in range(0, bins.size, 20000):
        b = bins[start:start + 20000]
        aa = a[start:start + 20000]
        keys = rng.random((b.size, N))
        ranks = np.argsort(keys, axis=1)
        mask = np.arange(N)[None, :] < aa[:, None]
        rr, cc = np.nonzero(mask)
        out_t.append(b[rr])
        out_n.append(ranks[rr, cc])
    t = np.concatenate(out_t)
    n = np.concatenate(out_n)
    return [np.sort(t[n == j]) for j in range(N)]


# ----------------------------------------------------------------------------------------------
# Branching ratio and susceptibility

def branching_new(act: np.ndarray, act_max: int, delays=BR_DELAYS):
    """brestimate.m: slopes r_k of A(t+k) on A(t) over bins with 0 <= A(t) <= act_max, fitted with
    r_k = b B^k by non-linear least squares from (1, 1). Returns (B_new, B_simple, slopes)."""
    act = act.astype(float)
    slopes = []
    for k in delays:
        a0, ak = act[:-k], act[k:]
        sel = a0 <= act_max
        slopes.append(np.polyfit(a0[sel], ak[sel], 1)[0])
    slopes = np.array(slopes)
    a0, a1 = act[:-1], act[1:]
    sel = a0 <= act_max
    br_simple = np.polyfit(a0[sel], a1[sel], 1)[0]
    try:
        (B, b), _ = optimize.curve_fit(lambda k, B, b: b * B ** k, delays.astype(float), slopes,
                                       p0=[1.0, 1.0], maxfev=20000)
    except RuntimeError:
        B = np.nan
    return float(B), float(br_simple), slopes


def branching_basic(act: np.ndarray) -> float:
    """Eq. 11, the time average of A(t+1)/A(t) over bins with A(t) > 0."""
    a0, a1 = act[:-1].astype(float), act[1:].astype(float)
    sel = a0 > 0
    return float(np.mean(a1[sel] / a0[sel]))


def susceptibility(act: np.ndarray, n_neurons: int):
    """Eq. 14 as printed, var(A/N), and the Williams-Garcia et al. (2014) form N var(A/N), over all
    bins (claims file, common detail 5)."""
    rho = act.astype(float) / n_neurons
    v = float(np.var(rho))
    return v, n_neurons * v


# ----------------------------------------------------------------------------------------------
# Sub-sampling (Methods 2.10)

def subsample_sizes(n: int, n_samples: int = 30, layout: str = "even", rng=None):
    """Sizes of the sub-samples: 'even', 30 sizes evenly spaced from 40% of n to n (reading a of
    the claims file); 'all', every integer size from 40% of n to n (reading b, 30 at each)."""
    lo = int(np.ceil(0.4 * n))
    if layout == "even":
        return np.unique(np.round(np.linspace(lo, n, n_samples)).astype(int)).tolist() if False \
            else np.round(np.linspace(lo, n, n_samples)).astype(int).tolist()
    return [m for m in range(lo, n + 1) for _ in range(n_samples)]


def wls_intercept(n_neurons, values):
    """Weighted least squares of values on 1/N with weight N; the intercept (1/N = 0)."""
    n = np.asarray(n_neurons, dtype=float)
    v = np.asarray(values, dtype=float)
    ok = np.isfinite(v)
    if ok.sum() < 2:
        return np.nan
    X = np.column_stack([1 / n[ok], np.ones(ok.sum())])
    w = np.sqrt(n[ok])
    beta, *_ = np.linalg.lstsq(X * w[:, None], v[ok] * w, rcond=None)
    return float(beta[1])


# ----------------------------------------------------------------------------------------------
# Statistics

def fdr(p, method: str = "bh"):
    """Benjamini-Hochberg ('bh') or Benjamini-Yekutieli ('by') adjusted p-values."""
    p = np.asarray(p, dtype=float)
    m = p.size
    order = np.argsort(p)
    c = np.sum(1.0 / np.arange(1, m + 1)) if method == "by" else 1.0
    adj = p[order] * m * c / np.arange(1, m + 1)
    adj = np.minimum.accumulate(adj[::-1])[::-1]
    out = np.empty(m)
    out[order] = np.minimum(adj, 1.0)
    return out


def terrell_scott_mode(x):
    """Mode of a histogram with the Terrell-Scott (1985) number of bins, (2n)^(1/3)."""
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    k = int(np.ceil((2 * x.size) ** (1 / 3)))
    h, e = np.histogram(x, bins=k)
    i = int(np.argmax(h))
    return float((e[i] + e[i + 1]) / 2), k


# ----------------------------------------------------------------------------------------------
# Per-recording pipeline

RANDOMIZATIONS = ["jitter1", "jitter10", "jitter100", "wrap", "poisson", "swap", "shuffle"]
JITTER_SD = {"jitter1": 1, "jitter10": 10, "jitter100": 100}   # Methods 2.5, in rebinned bins


def prepare(d: dict) -> dict:
    """First 59 min, network ISI, rebinning, activity and avalanches of one recording.

    Neurons with no spike in the first 59 min are dropped (complexity.m would give NaN for them);
    the number dropped is returned."""
    sp = first_window(d["spikes"])
    n_all = len(sp)
    counts_all = np.array([s.size for s in sp])
    sp = [s for s in sp if s.size > 0]
    isi = network_isi_bins(sp)
    factor = max(1, int(round(isi)))
    r, nb = rebin(sp, factor)
    act = activity(r, nb)
    return dict(name=d["name"], spikes=sp, counts_all=counts_all, n_all=n_all,
                n_silent=int(n_all - len(sp)), isi_bins=isi, factor=factor, raster=r, nbins=nb,
                act=act)


def randomize(kind: str, raster, nbins, rng, counts=None):
    if kind in JITTER_SD:
        return rand_jitter(raster, nbins, JITTER_SD[kind], rng, counts)
    return {"wrap": rand_wrap, "poisson": rand_poisson, "swap": rand_swap,
            "shuffle": rand_shuffle}[kind](raster, nbins, rng)


def criticality(act: np.ndarray, n_neurons: int, rng: np.random.Generator) -> dict:
    """Avalanche counts, the size and duration fits with range search, size given duration,
    shape collapse and susceptibility of one activity series."""
    size, dur, starts = avalanches(act)
    cs, cd = apply_cuts(size), apply_cuts(dur)
    fs = plparams(cs, rng) if cs.size else plparams(np.array([1]), rng)
    fd = plparams(cd, rng) if cd.size else plparams(np.array([1]), rng)
    prof = mean_profiles(act, size, dur, starts)
    sc_exp, curv = shape_collapse(prof)
    chi_a, chi_b = susceptibility(act, n_neurons)
    return dict(n_av=int(size.size), n_size_cut_values=int(np.unique(cs).size),
                n_dur_cut_values=int(np.unique(cd).size), n_profiles=len(prof),
                tau=fs["tau"], s_xmin=fs["xmin"], s_xmax=fs["xmax"], s_p=fs["p"],
                s_tried=fs["n_tried"],
                alpha=fd["tau"], d_xmin=fd["xmin"], d_xmax=fd["xmax"], d_p=fd["p"],
                d_tried=fd["n_tried"],
                s_range=np.log10(fs["xmax"] / fs["xmin"]) if np.isfinite(fs["tau"]) else np.nan,
                d_range=np.log10(fd["xmax"] / fd["xmin"]) if np.isfinite(fd["tau"]) else np.nan,
                sgd=sizegivdur(size, dur, fd["xmin"], fd["xmax"]),
                sc_exp=sc_exp, curv=curv, abs_curv=abs(curv) if np.isfinite(curv) else np.nan,
                chi_a=chi_a, chi_b=chi_b)


def avalanche_ratio(act: np.ndarray) -> float:
    """avprops.m 'ratio': per avalanche sum of s(t+1)/s(t) over its bins divided by its duration;
    the mean over avalanches."""
    size, dur, starts = avalanches(act)
    a = act.astype(float)
    nxt = np.concatenate([a[1:], [0]])
    within = (a > 0) & (nxt > 0)
    ratio = np.where(within, nxt / np.where(a > 0, a, 1), 0.0)
    cs = np.concatenate([[0], np.cumsum(ratio)])
    per = (cs[starts + dur] - cs[starts]) / dur
    return float(per.mean())


def subsample_exponents(spikes: list[np.ndarray], rng: np.random.Generator, own_isi: bool,
                        factor_full: int, sizes: list[int], return_values: bool = False) -> dict:
    """Methods 2.10 for the culture exponents: for each sub-sample of neurons, tau and alpha by the
    MLE over all avalanches that survive the cuts (no range search), 1/sigma nu z from size given
    duration over the cut duration range and from the shape collapse, then the weighted least
    squares intercept on 1/N. own_isi: each sub-sample rebinned to its own network ISI (the
    analysis of the whole system, Methods 2.3, repeated, as Methods 2.10 say the analyses were
    identical); otherwise the full system's bin."""
    N = len(spikes)
    lab = np.concatenate([np.full(s.size, j) for j, s in enumerate(spikes)])
    t = np.concatenate(spikes)
    o = np.argsort(t, kind="stable")
    t, lab = t[o], lab[o]
    vals = {k: [] for k in ("tau", "alpha", "sgd", "sc_exp")}
    for m in sizes:
        keep = np.zeros(N, dtype=bool)
        keep[rng.permutation(N)[:m]] = True
        sel = keep[lab]
        tt, ll = t[sel], lab[sel]
        f = max(1, int(round((tt[-1] - tt[0]) / (tt.size - 1)))) if own_isi else factor_full
        b = np.ceil(tt / f).astype(np.int64)
        key = np.unique(b * N + ll)
        nb = int(np.ceil(ANALYSIS_BINS / f))
        act = np.bincount(key // N, minlength=nb + 1)[1:nb + 1].astype(np.int32)
        size, dur, starts = avalanches(act)
        cs, cd = apply_cuts(size), apply_cuts(dur)
        vals["tau"].append(plmle_full(cs) if cs.size else np.nan)
        vals["alpha"].append(plmle_full(cd) if cd.size else np.nan)
        vals["sgd"].append(sizegivdur(size, dur, cd.min(), cd.max()) if cd.size else np.nan)
        prof = mean_profiles(act, size, dur, starts)
        vals["sc_exp"].append(shape_collapse(prof)[0])
    if return_values:
        return vals
    return {k: wls_intercept(sizes, v) for k, v in vals.items()}


def subsample_chunk(args) -> dict:
    """Sub-sample values (own-ISI rebinning) of one recording for a chunk of sizes, for running
    layout reading b in parallel. args = (name, sizes, seed list)."""
    name, sizes, seed = args
    p = prepare(load(name, _worker_zip()))
    vals = subsample_exponents(p["spikes"], np.random.default_rng(seed), True, p["factor"], sizes,
                               return_values=True)
    vals["n"] = list(sizes)
    return vals


_ZF = None


def _worker_zip():
    global _ZF
    if _ZF is None:
        _ZF = open_zip()
    return _ZF


def culture_record(args) -> dict:
    """Notebook 1, one recording: counts, ISI, real-data criticality measures, branching ratios,
    sub-sampled exponents (both rebinning readings) and the criticality measures of each
    randomization. args = (index, name, seed)."""
    i, name, seed = args
    d = load(name, _worker_zip())
    p = prepare(d)
    N = len(p["raster"])
    allt = np.concatenate(d["spikes"])
    out = dict(name=name, culture=culture_div(name)[0], div=culture_div(name)[1],
               n_neurons=d["nNeurons"], n_trains=len(d["spikes"]), binsize=d["binsize"],
               recordingID=d["recordingID"], datatype=d["datatype"], expsys=d["expsys"],
               n_channel=len(d["channel"]), n_spikes=int(allt.size),
               n_beyond_nbins=int(np.sum(allt > d["nbins"])),
               n_dup_spikes=int(sum(np.sum(np.diff(s) == 0) for s in d["spikes"])),
               all_sorted=bool(all(np.all(np.diff(s) >= 0) for s in d["spikes"])),
               train_hash=hashlib.md5(b"".join(s.tobytes() for s in d["spikes"])).hexdigest(),
               n_silent=p["n_silent"], nbins_file=d["nbins"],
               isi_ms=p["isi_bins"] * BIN_MS, factor=p["factor"],
               rates=p["counts_all"] / (ANALYSIS_MIN * 60.0),
               t_max_ms=float(max(s.max() for s in d["spikes"] if s.size) * BIN_MS),
               min_isi_ms=float(min(np.diff(s).min() for s in d["spikes"] if s.size > 1) * BIN_MS),
               min_pos_isi_ms=float(min(np.diff(s)[np.diff(s) > 0].min() for s in d["spikes"]
                                        if np.sum(np.diff(s) > 0) > 0) * BIN_MS),
               wave_clus_ref=float(getattr(d["wave_clus"], "ref", np.nan)),
               wave_clus_sr=float(getattr(d["wave_clus"], "sr", np.nan)))
    act = p["act"]
    res = {"real": criticality(act, N, np.random.default_rng([seed, i, 1]))}
    out["B_new"], out["B_simple"], out["slopes"] = branching_new(act, BR_ACT_MAX_CULTURE)
    out["B_basic"] = branching_basic(act)
    out["B_avalanche"] = avalanche_ratio(act)
    sizes = subsample_sizes(N)
    for own, tag in ((True, "own"), (False, "fixed")):
        ss = subsample_exponents(p["spikes"], np.random.default_rng([seed, i, 2 + own]), own,
                                 p["factor"], sizes)
        for k, v in ss.items():
            out[f"ss_{tag}_{k}"] = v
    for j, kind in enumerate(RANDOMIZATIONS):
        jc = []
        rr = randomize(kind, p["raster"], p["nbins"], np.random.default_rng([seed, i, 10 + j]), jc)
        if jc:
            out[f"{kind}_spikes"], out[f"{kind}_zero_moves"], out[f"{kind}_undone"] = jc[0]
        rng = np.random.default_rng([seed, i, 20 + j])
        a2 = activity(rr, p["nbins"])
        if kind in ("swap", "shuffle"):
            out[f"{kind}_act_identical"] = bool(np.array_equal(a2, act))
            out[f"{kind}_counts_kept"] = bool(all(a.size == b.size for a, b in zip(rr, p["raster"])))
            res[kind] = dict(res["real"])   # A(t) is unchanged, so every avalanche measure is
            continue
        out[f"{kind}_counts_kept"] = bool(all(a.size == b.size for a, b in zip(rr, p["raster"])))
        res[kind] = criticality(a2, N, rng)
    out["measures"] = res
    return out


def complexity_record(args) -> dict:
    """Notebook 2, one recording: complexity (sub-sampling correction on, n_subsets random subsets
    per size) on the avalanche bins of the real data and of each randomization, with the real
    data's susceptibility and fit ranges. args = (index, name, seed, n_subsets)."""
    i, name, seed, n_subsets = args
    d = load(name, _worker_zip())
    p = prepare(d)
    N = len(p["raster"])
    act = p["act"]
    crit = criticality(act, N, np.random.default_rng([seed, i, 1]))
    out = dict(name=name, culture=culture_div(name)[0], div=culture_div(name)[1], n_neurons=N,
               chi_a=crit["chi_a"], chi_b=crit["chi_b"], abs_curv=crit["abs_curv"],
               s_range=crit["s_range"],
               d_range=crit["d_range"], n_av=crit["n_av"], n_profiles=crit["n_profiles"],
               n_size_cut_values=crit["n_size_cut_values"],
               n_dur_cut_values=crit["n_dur_cut_values"])
    for j, kind in enumerate(["real"] + RANDOMIZATIONS):
        rng = np.random.default_rng([seed, i, 100 + j])
        # the same randomized data as culture_record (same generator for the randomization)
        rr = p["raster"] if kind == "real" else randomize(
            kind, p["raster"], p["nbins"], np.random.default_rng([seed, i, 10 + j - 1]))
        a2 = act if kind == "real" else activity(rr, p["nbins"])
        if kind != "real":
            size, dur, starts = avalanches(a2)
            out[f"chi_a_{kind}"], out[f"chi_b_{kind}"] = susceptibility(a2, N)
            out[f"abs_curv_{kind}"] = abs(shape_collapse(mean_profiles(a2, size, dur, starts))[1])
        bins = np.flatnonzero(a2) + 1
        X = raster_matrix(rr, bins)
        # a neuron that the shuffle left without a spike has no entropy; drop it
        keep = np.asarray(X.sum(axis=0)).ravel() > 0
        X = X[:, keep] if not keep.all() else X
        cv = complexity(X, n_subsets, rng, return_variants=True)
        out[f"C_{kind}"] = cv["cut"]
        out[f"Cuncut_{kind}"] = cv["uncut"]
        out[f"Craw_{kind}"] = cv["raw"]
        out[f"kkept_{kind}"] = cv["k_kept"]
        out[f"N_{kind}"] = cv["N"]
        out[f"nbins_{kind}"] = int(bins.size)
    return out


def complexity_swap_record(args) -> dict:
    """complexity_swap.ipynb, one recording: complexity_record restricted to the real data and spike
    swapping, with the same generators, so a recording in both notebooks gets the same values.
    Also the counts of the exclusion rule (reading a). args = (index, name, seed, n_subsets)."""
    i, name, seed, n_subsets = args
    p = prepare(load(name, _worker_zip()))
    N = len(p["raster"])
    act = p["act"]
    size, dur, starts = avalanches(act)
    out = dict(name=name, culture=culture_div(name)[0], div=culture_div(name)[1], n_neurons=N,
               n_size_cut_values=int(np.unique(apply_cuts(size)).size),
               n_dur_cut_values=int(np.unique(apply_cuts(dur)).size),
               n_profiles=len(mean_profiles(act, size, dur, starts)))
    j_swap = 1 + RANDOMIZATIONS.index("swap")
    for j, kind in ((0, "real"), (j_swap, "swap")):
        rng = np.random.default_rng([seed, i, 100 + j])
        rr = p["raster"] if kind == "real" else randomize(
            kind, p["raster"], p["nbins"], np.random.default_rng([seed, i, 10 + j - 1]))
        a2 = act if kind == "real" else activity(rr, p["nbins"])
        if kind == "swap":
            out["swap_act_identical"] = bool(np.array_equal(a2, act))
        X = raster_matrix(rr, np.flatnonzero(a2) + 1)
        keep = np.asarray(X.sum(axis=0)).ravel() > 0
        X = X[:, keep] if not keep.all() else X
        cv = complexity(X, n_subsets, rng, return_variants=True)
        out[f"C_{kind}"] = cv["cut"]
        out[f"Cuncut_{kind}"] = cv["uncut"]
        out[f"Craw_{kind}"] = cv["raw"]
        out[f"kkept_{kind}"] = cv["k_kept"]
        out[f"N_{kind}"] = cv["N"]
    return out


def complexity_seeds(args) -> list[dict]:
    """Notebook 2, one recording: the complexity of the real data repeated with several generators
    for the random subsets and the time permutation of the correction, at each number of subsets
    per size, to show the estimator's spread. args = (index, name, seed, n_subsets_list, n_seeds)."""
    i, name, seed, n_subsets_list, n_seeds = args
    p = prepare(load(name, _worker_zip()))
    X = raster_matrix(p["raster"], np.flatnonzero(p["act"]) + 1)
    X = X[:, np.asarray(X.sum(axis=0)).ravel() > 0]
    out = []
    for ns in n_subsets_list:
        for s in range(n_seeds):
            cv = complexity(X, ns, np.random.default_rng([seed, i, 500, ns, s]), return_variants=True)
            out.append(dict(name=name, n_subsets=ns, rep=s, C=cv["cut"], Cuncut=cv["uncut"],
                            Craw=cv["raw"], k_kept=cv["k_kept"], N=cv["N"]))
    return out
