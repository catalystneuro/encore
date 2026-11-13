"""Loading and cNE measures for CRCNS ac-3 (See, Atencio & Schreiner), used by See et al. (2018).

See JZ, Atencio CA, Sohal VS, Schreiner CE (2018). Coordinated neuronal ensembles in primary
auditory cortical columns. eLife 7:e35587, doi:10.7554/eLife.35587.

The data set CRCNS ac-3 (doi:10.6080/K09021X1) is not versioned; it is read as `unversioned`
from the public bucket crcnsarchive, under ac-3/live/, by opening the zip files in place over
range requests. Nothing is written to disk. Data.zip holds one MATLAB file per recording
(`site<k>-<stim>.mat`, 16 files): `spk`, one struct per unit (spike times in ms, `position` as
[lateral offset, depth below the surface] in um, `probechan`, `meanwaveform`), and `trigger`,
the stimulus triggers in samples at 20 kHz. Stimulus.zip holds the stimulus envelopes
(`stim_mat`, 64 carriers by 0.5-ms columns, 667 columns per trigger) for rn1 (the DMR) and rn16
(the RN, the sum of 16 DMRs).

Where the parameters come from:

- cNE detection (`detect`) follows the claims file's opening comment, from Materials and
  methods, Detection of coordinated neuronal ensembles: 10-ms bins, z-scored rows, eigenvalues
  of the correlation matrix above the Marcenko-Pastur bound (1 + sqrt(n/T))^2 (the claims file's
  reading, Lopes-dos-Santos et al. 2013), fastICA on the significant PCs, membership at the mean
  plus or minus 1.5 SD of the IC weights from 100 circular shuffles (ICA on the N largest PCs of
  each), activity threshold at the 99.9th percentile of the real ICs projected on the shuffles.
  fastICA is the symmetric algorithm with the logcosh contrast (`fastica`, as in sklearn and the
  FastICA package). Its settings (at most 1000 iterations and tolerance 1e-6 on the data; at most
  200 iterations and tolerance 1e-4, sklearn's defaults, on the shuffles, which hold no
  independent sources) and the random seeds are standard choices that the paper does not fix.
- IC scale and sign, and the activity projection, have the two readings each of the claims file
  (`SIGN_READINGS`, `PROJECTIONS`).
- The analysis window of each recording is the stimulus: from the first trigger to one stimulus
  period (667 columns) after the last. Spikes outside it are left out. Spike times are put on the
  stimulus clock (`to_stim_ms`), interpolating between triggers, so that every binned train is
  aligned with the stimulus columns; this clock runs 0.05% slower than the recording clock.
- PWCs (`pwc`) are histograms of spike-time differences of the spikes inside the stimulus period,
  on the stimulus clock, with the lag bins and ranges of the claims file (1 ms over +-50 or +-100
  ms). The paper does not say whether a baseline was removed; `pair_table` also gives sharpness
  after subtracting one of two baselines (variants, not readings of the claims file). Sharpness is the median of
  the absolute lag from the peak, weighted by the counts (Figure 6G to I legend); peak delay is
  the absolute lag of the maximum, the first maximum on ties.
- STRFs are spike- or event-triggered averages of the stimulus envelope. The window and
  resolution are not given by the paper. The data set's own STRF code (Codes.zip,
  calc_and_plot_STRFs.m, written by the first author) uses 0.5-ms columns and 100 lags (50 ms);
  its segment code notes that "for AI cells, and 5 ms bins, nlags = 20 is sufficient". Here the
  stimulus is averaged to `STRF_BIN_MS` = 5-ms bins with `STRF_LAGS` = 20 lags (100 ms), the
  first author's stated choice, an assumption stated in the notebook. The temporal profiles of
  Figure 6B, E use a 1-ms version (`strf_1ms`), 50 lags, as in the sample code's 50 ms.
- STRF mutual information (`strf_mi`) follows Materials and methods, STRF mutual information:
  projections z = s . STRF, P(z) from all stimulus segments, P(z|event) from the segments before
  events, both normalised by the mean and SD of P(z), MI extrapolated from 20 random subsamples at
  90, 95, 97.5, 99 and 100% of the events against the inverse fraction. The projection bins,
  `MI_BINS` = 25 equal bins over -5 to 5 SD with the tails pooled into the end bins, are a
  standard choice.
"""

from __future__ import annotations

import io
import re
import zipfile

import fsspec
import numpy as np
import scipy.io as sio
from scipy import stats

DATASET = "ac-3"
VERSION = "unversioned"
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live"
FS = 20000.0              # trigger sampling rate, data descriptor
NT = 667                  # stimulus columns per trigger, rnX-param.mat
COL_MS = 0.5              # stimulus column width on the stimulus clock, taxis in rnX-param.mat
BIN_MS = 10               # cNE detection bin, Materials and methods
N_SHUFFLES = 100          # Materials and methods
MEMBER_SD = 1.5           # Materials and methods
SHUFFLE_ICA_ITER = 200    # standard choice (sklearn's default); fastICA does not converge on shuffles
ACTIVITY_PCT = 99.9       # Materials and methods
STRF_BIN_MS = 5           # assumption, the first author's sample code (see docstring)
STRF_LAGS = 20
MI_BINS = np.linspace(-5, 5, 26)
MI_FRACTIONS = (0.90, 0.95, 0.975, 0.99, 1.0)   # Materials and methods
MI_ITER = 20
SIGN_READINGS = ("a", "b")      # (a) largest |weight| positive; (b) as fastICA returns it
PROJECTIONS = ("quadratic", "linear")


# --- loading ---------------------------------------------------------------------------------

def _zip(name: str) -> zipfile.ZipFile:
    return zipfile.ZipFile(fsspec.open(f"{BASE}/{name}", block_size=2**22).open())


def load_sites() -> list[dict]:
    """All 16 recordings of Data.zip, in site order, reduced to what the analysis uses."""
    z = _zip("Data.zip")
    sites = []
    for name in z.namelist():
        m = re.search(r"site(\d+)-(rn\d+)\.mat$", name)
        if not m:
            continue
        mat = sio.loadmat(io.BytesIO(z.read(name)), squeeze_me=True, struct_as_record=False)
        spk = np.atleast_1d(mat["spk"])
        trig = np.asarray(mat["trigger"], dtype=float).ravel()
        units = []
        for s in spk:
            pos = np.asarray(s.position, dtype=float).ravel()
            units.append({"spikes_ms": np.asarray(s.spiketimes, dtype=float).ravel(),
                          "x": pos[0], "depth": pos[1], "probechan": int(s.probechan),
                          "chan": int(s.chan), "tip_depth": float(s.depth), "stim": str(s.stim),
                          "fs": float(s.fs),
                          "waveform": np.asarray(s.meanwaveform, dtype=float)})
        sites.append({"site": int(m.group(1)), "stim": m.group(2), "file": name.split("/")[-1],
                      "trigger": trig, "units": units})
    return sorted(sites, key=lambda s: s["site"])


def load_stimulus(name: str) -> np.ndarray:
    """The stimulus envelope `stim_mat` of rn1 or rn16 (64 carriers by 0.5-ms columns), float32."""
    z = _zip("Stimulus.zip")
    raw = z.read(f"Stimulus/{name}-matrix.mat")
    stim = sio.loadmat(io.BytesIO(raw))["stim_mat"]
    del raw
    return np.asarray(stim, dtype=np.float32)


def load_params(name: str) -> dict:
    z = _zip("Stimulus.zip")
    m = sio.loadmat(io.BytesIO(z.read(f"Stimulus/{name}-param.mat")), squeeze_me=True)
    return {k: v for k, v in m.items() if not k.startswith("__")}


def downsample(stim: np.ndarray, bin_ms: float) -> np.ndarray:
    """Average 0.5-ms columns into bins of `bin_ms` on the stimulus clock; a partial last bin is dropped."""
    k = int(round(bin_ms / COL_MS))
    n = stim.shape[1] // k
    return stim[:, :n * k].reshape(stim.shape[0], n, k).mean(axis=2)


# --- clocks and binning ------------------------------------------------------------------------

def to_stim_ms(site: dict, spikes_ms: np.ndarray) -> np.ndarray:
    """Spike times (recording ms) to the stimulus clock: ms since the first trigger, measured in
    0.5-ms stimulus columns, interpolated between triggers. Times outside the stimulus are NaN."""
    trig_ms = site["trigger"] / FS * 1000.0
    period = np.median(np.diff(trig_ms))
    knots = np.append(trig_ms, trig_ms[-1] + period)
    cols = np.interp(spikes_ms, knots, np.arange(len(knots)) * NT, left=np.nan, right=np.nan)
    return cols * COL_MS


def stim_duration_ms(site: dict) -> float:
    return len(site["trigger"]) * NT * COL_MS


def binned(site: dict, bin_ms: float, units=None, t_range=None) -> np.ndarray:
    """Spike counts (units by bins) on the stimulus clock."""
    dur = stim_duration_ms(site)
    lo, hi = t_range if t_range is not None else (0.0, dur)
    n = int(np.floor((hi - lo) / bin_ms))
    edges = lo + np.arange(n + 1) * bin_ms
    us = site["units"] if units is None else [site["units"][i] for i in units]
    out = np.zeros((len(us), n), dtype=np.float32)
    for i, u in enumerate(us):
        t = u["stim_ms"]
        out[i] = np.histogram(t[np.isfinite(t)], edges)[0]
    return out


def prepare(site: dict) -> None:
    """Add stimulus-clock spike times to every unit."""
    for u in site["units"]:
        u["stim_ms"] = to_stim_ms(site, u["spikes_ms"])


# --- cNE detection -----------------------------------------------------------------------------

def zscore(counts: np.ndarray) -> np.ndarray:
    m = counts.mean(axis=1, keepdims=True)
    s = counts.std(axis=1, keepdims=True)
    s[s == 0] = 1.0
    return ((counts - m) / s).astype(np.float32)


def mp_bound(n: int, t: int) -> float:
    return (1.0 + np.sqrt(n / t)) ** 2


def fastica(x: np.ndarray, seed: int, max_iter: int, tol: float, info: dict | None = None) -> np.ndarray:
    """Symmetric fastICA with the logcosh contrast (Hyvarinen and Oja 1997; the algorithm of
    sklearn's FastICA) on whitened data x (N by T). Returns the unmixing matrix W (N by N); the
    number of iterations run is put in `info` when given."""
    rng = np.random.default_rng(seed)
    n, t = x.shape
    w = _sym_decorrelate(rng.standard_normal((n, n)))
    it = 0
    for it in range(1, max_iter + 1):
        g = np.tanh(w.astype(np.float32) @ x)
        w1 = (g @ x.T) / t - (1.0 - g ** 2).mean(axis=1)[:, None] * w
        w1 = _sym_decorrelate(w1.astype(np.float64))
        lim = np.max(np.abs(np.abs(np.einsum("ij,ij->i", w1, w)) - 1.0))
        w = w1
        if lim < tol:
            break
    if info is not None:
        info["iter"] = it
    return w


def _sym_decorrelate(w: np.ndarray) -> np.ndarray:
    s, u = np.linalg.eigh(w @ w.T)
    s = np.clip(s, np.finfo(w.dtype).tiny, None)
    return (u * (1.0 / np.sqrt(s))) @ u.T @ w


def _ica_weights(z: np.ndarray, vals: np.ndarray, vecs: np.ndarray, seed: int,
                 max_iter: int = 1000, tol: float = 1e-6, info: dict | None = None) -> np.ndarray:
    """fastICA on the projection of z onto the PCs `vecs` (n by N) with eigenvalues `vals`, which
    are already uncorrelated, so whitening divides each by the square root of its eigenvalue.
    Returns the IC weights in unit space (n by N), each of unit length."""
    if vecs.shape[1] == 1:
        if info is not None:
            info["iter"] = 0
        return vecs / np.linalg.norm(vecs, axis=0, keepdims=True)
    scale = 1.0 / np.sqrt(vals)
    x = (vecs.T.astype(np.float32) @ z) * scale[:, None].astype(np.float32)
    w = fastica(x, seed, max_iter, tol, info)
    weights = vecs @ (w * scale[None, :]).T
    return weights / np.linalg.norm(weights, axis=0, keepdims=True)


def orient(w: np.ndarray, reading: str) -> np.ndarray:
    """Reading (a): sign set so that the largest absolute weight is positive. Reading (b): unchanged."""
    if reading == "b":
        return w
    s = np.sign(w[np.abs(w).argmax(axis=0), np.arange(w.shape[1])])
    s[s == 0] = 1
    return w * s


def pcs(z: np.ndarray):
    c = (z @ z.T) / z.shape[1]
    vals, vecs = np.linalg.eigh(c)
    order = np.argsort(vals)[::-1]
    return vals[order], vecs[:, order]


def n_cnes(counts: np.ndarray) -> int:
    """Number of eigenvalues above the Marcenko-Pastur bound (the number of cNEs)."""
    keep = counts.std(axis=1) > 0
    z = zscore(counts[keep])
    vals, _ = pcs(z)
    return int((vals > mp_bound(z.shape[0], z.shape[1])).sum())


def circular_shuffle(counts: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    t = counts.shape[1]
    shifts = rng.integers(1, t, size=counts.shape[0])
    idx = (np.arange(t)[None, :] - shifts[:, None]) % t
    return np.take_along_axis(counts, idx, axis=1)


def activity(z: np.ndarray, w: np.ndarray, projection: str) -> np.ndarray:
    """cNE activity (N by T). Quadratic: z' P z with P = w w' and its diagonal set to zero
    (Lopes-dos-Santos et al. 2013). Linear: w . z."""
    lin = w.T @ z
    if projection == "linear":
        return lin
    return lin ** 2 - (w ** 2).T @ (z ** 2)


def detect(counts: np.ndarray, seed: int, n_shuffles: int = N_SHUFFLES, null: bool = True,
           activity_null: bool = True) -> dict:
    """cNE detection of the claims file's opening comment on a units-by-bins count matrix.

    Returns the number of cNEs, the raw IC weights (reading b), and, with `null`, per sign reading
    the membership thresholds and the members, and the shuffled IC weights (for the
    interleaved-halves null); with `activity_null`, the 99.9th percentile activity thresholds per
    projection reading. Units without spikes are left out and reported in `kept`."""
    rng = np.random.default_rng(seed)
    keep = np.flatnonzero(counts.std(axis=1) > 0)
    z = zscore(counts[keep])
    n, t = z.shape
    vals, vecs = pcs(z)
    k = int((vals > mp_bound(n, t)).sum())
    out = {"n": k, "kept": keep, "n_units": counts.shape[0], "eigenvalues": vals,
           "bound": mp_bound(n, t)}
    if k == 0:
        out["w"] = np.zeros((n, 0))
        return out
    info = {}
    w = _ica_weights(z, vals[:k], vecs[:, :k], seed, info=info)
    out["w"] = w
    out["ica_iter"] = info["iter"]
    if not null:
        return out
    shuf_w, shuf_iter = [], []
    act = {p: [] for p in PROJECTIONS}
    oriented = {r: orient(w, r) for r in SIGN_READINGS}
    for i in range(n_shuffles):
        zs = circular_shuffle(z, rng)
        sl, sv = pcs(zs)
        si = {}
        shuf_w.append(_ica_weights(zs, sl[:k], sv[:, :k], seed + 1 + i, SHUFFLE_ICA_ITER, 1e-4, si))
        shuf_iter.append(si["iter"])
        if activity_null:
            for p in PROJECTIONS:
                act[p].append(activity(zs, oriented["a"], p))
    out["shuffled_w"] = shuf_w
    out["shuffle_ica_iter"] = np.array(shuf_iter)
    out["members"], out["thresholds"] = {}, {}
    for r in SIGN_READINGS:
        null_w = np.concatenate([orient(sw, r).ravel() for sw in shuf_w])
        lo = null_w.mean() - MEMBER_SD * null_w.std()
        hi = null_w.mean() + MEMBER_SD * null_w.std()
        wr = oriented[r]
        out["thresholds"][r] = (lo, hi)
        out["members"][r] = [{"pos": keep[wr[:, j] > hi], "neg": keep[wr[:, j] < lo]} for j in range(k)]
    if activity_null:
        out["act_threshold"] = {p: np.percentile(np.concatenate(act[p], axis=1), ACTIVITY_PCT, axis=1)
                                for p in PROJECTIONS}
    return out


def member_sets(det: dict, reading: str = "a") -> list[np.ndarray]:
    """Members (positive and negative) of each cNE, as unit indices of the recording."""
    return [np.union1d(m["pos"], m["neg"]) for m in det["members"][reading]]


def events_from_activity(act: np.ndarray, threshold: float, reading: str) -> np.ndarray:
    """Indices of events. Reading (a): every sample above threshold. Reading (b): one per run of
    samples above threshold, at its peak."""
    above = act > threshold
    if reading == "a":
        return np.flatnonzero(above)
    d = np.diff(np.r_[0, above.astype(int), 0])
    starts, ends = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
    return np.array([s + np.argmax(act[s:e]) for s, e in zip(starts, ends)], dtype=int)


def interp_activity(act: np.ndarray, bin_ms: float, n_ms: int) -> np.ndarray:
    """Activity on bins of `bin_ms` linearly interpolated to 1 ms (Materials and methods, STRF MI),
    each value placed at its bin centre."""
    centres = (np.arange(len(act)) + 0.5) * bin_ms
    return np.interp(np.arange(n_ms) + 0.5, centres, act)


# --- pairwise correlation functions ------------------------------------------------------------

def pwc(a: np.ndarray, b: np.ndarray, max_lag: float, bin_ms: float = 1.0) -> np.ndarray:
    """Histogram of b - a spike-time differences in bins of `bin_ms` centred on 0, over +-max_lag."""
    edges = np.arange(-max_lag - bin_ms / 2, max_lag + bin_ms, bin_ms)
    b = np.sort(b)
    idx = np.searchsorted(b, a[:, None] + edges[None, :])
    return np.diff(idx, axis=1).sum(axis=0)


def pwc_measures(counts: np.ndarray, bin_ms: float = 1.0) -> tuple[float, float]:
    """(sharpness, absolute peak delay) in ms: the PWC folded at its peak, sharpness the lag from the
    peak at the median of the folded count distribution (Figure 6G to I)."""
    lags = (np.arange(len(counts)) - (len(counts) - 1) / 2) * bin_ms
    if counts.sum() == 0:
        return np.nan, np.nan
    peak = lags[np.argmax(counts)]
    dist = np.abs(lags - peak)
    order = np.argsort(dist, kind="stable")
    cum = np.cumsum(counts[order])
    sharp = dist[order][np.searchsorted(cum, cum[-1] / 2.0)]
    return float(sharp), float(abs(peak))


# --- STRFs and mutual information --------------------------------------------------------------

def segment_index(times_ms: np.ndarray, bin_ms: float, n_bins: int, lags: int) -> np.ndarray:
    """Stimulus bin indices of the last bin before each time, kept when a full window precedes it."""
    idx = np.floor(times_ms / bin_ms).astype(int) - 1
    return idx[(idx >= lags - 1) & (idx < n_bins)]


def sta(stim: np.ndarray, idx: np.ndarray, lags: int) -> np.ndarray:
    """Spike- or event-triggered average (carriers by lags, last lag nearest the event)."""
    if len(idx) == 0:
        return np.zeros((stim.shape[0], lags), dtype=np.float32)
    out = np.zeros((stim.shape[0], lags), dtype=np.float64)
    for j in range(lags):
        out[:, j] = stim[:, idx - (lags - 1 - j)].sum(axis=1)
    return (out / len(idx)).astype(np.float32)


def projections(stim: np.ndarray, strf: np.ndarray) -> np.ndarray:
    """z(t) = s(t) . STRF for every stimulus segment ending at bin t (valid for t >= lags - 1; the
    first lags - 1 values are partial sums)."""
    nf, lags = strf.shape
    m = strf.T @ stim
    z = np.zeros(stim.shape[1], dtype=np.float64)
    for j in range(lags):
        shift = lags - 1 - j
        z[shift:] += m[j, :stim.shape[1] - shift]
    return z


def _hist(x: np.ndarray) -> np.ndarray:
    idx = np.clip(np.searchsorted(MI_BINS, x, side="right") - 1, 0, len(MI_BINS) - 2)
    h = np.bincount(idx, minlength=len(MI_BINS) - 1).astype(float)
    return h / h.sum()


def mi_bits(p: np.ndarray, x_ev: np.ndarray) -> float:
    """MI (bits) from the prior P(x) (histogram `p`) and the projections before events."""
    q = _hist(x_ev)
    ok = (q > 0) & (p > 0)
    return float((q[ok] * np.log2(q[ok] / p[ok])).sum())


def strf_mi(z_all: np.ndarray, z_ev: np.ndarray, rng: np.random.Generator) -> float:
    """MI between STRF projections and events, extrapolated to infinite data (Materials and methods).
    Projections are binned in `MI_BINS` after normalising by the mean and SD of P(z); values beyond
    the outer edges fall in the end bins."""
    mu, sd = z_all.mean(), z_all.std()
    p = _hist((z_all - mu) / sd)
    x_ev = (z_ev - mu) / sd
    means = []
    for f in MI_FRACTIONS:
        m = max(int(round(f * len(x_ev))), 1)
        vals = [mi_bits(p, x_ev if f == 1.0 else rng.choice(x_ev, m, replace=False))
                for _ in range(MI_ITER if f < 1.0 else 1)]
        means.append(np.mean(vals))
    slope, intercept = np.polyfit(1.0 / np.array(MI_FRACTIONS), means, 1)
    return float(intercept)


def strf_mi_heldout(stim: np.ndarray, idx: np.ndarray, lags: int, rng: np.random.Generator) -> float:
    """STRF MI with the STRF estimated on the events of one half of the stimulus and the MI computed
    (as in `strf_mi`) on the events of the other half, averaged over the two directions. Splitting
    by time keeps neighbouring events, which share stimulus segments, on one side. A check of the
    bias of estimating the STRF and the MI on the same events, which the paper does not describe."""
    first = idx < stim.shape[1] // 2
    halves = (idx[first], idx[~first])
    out = []
    for fit, test in (halves, halves[::-1]):
        if len(fit) == 0 or len(test) < 2:
            return np.nan
        zall = projections(stim, sta(stim, fit, lags))
        out.append(strf_mi(zall[lags - 1:], zall[test], rng))
    return float(np.mean(out))


# --- dichotomized Gaussian ---------------------------------------------------------------------

_GL_X, _GL_W = np.polynomial.legendre.leggauss(40)


def bvn_cdf(h: np.ndarray, k: np.ndarray, r: np.ndarray) -> np.ndarray:
    """P(X < h, Y < k) for standard bivariate normals with correlation r (|r| < 1), by Gauss-Legendre
    quadrature of Plackett's identity d/dr Phi2 = phi2(h, k; r)."""
    h, k, r = np.broadcast_arrays(np.asarray(h, float), np.asarray(k, float), np.asarray(r, float))
    s = 0.5 * r[..., None] * (_GL_X + 1.0)
    dens = np.exp(-(h[..., None] ** 2 - 2 * h[..., None] * k[..., None] * s + k[..., None] ** 2)
                  / (2 * (1 - s ** 2))) / (2 * np.pi * np.sqrt(1 - s ** 2))
    return stats.norm.cdf(h) * stats.norm.cdf(k) + 0.5 * r * (dens * _GL_W).sum(axis=-1)


def fit_dg(binary: np.ndarray, info: dict | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Dichotomized Gaussian fit to binary trains (units by bins): thresholds gamma and latent
    correlation matrix, matching each unit's mean and each pair's covariance (Macke et al. 2009, as
    findLatentGaussian01 of CorBinian does), by bisection on each pair's latent correlation. The
    latent matrix is made positive definite by clipping its eigenvalues at 1e-4 and rescaling to a
    unit diagonal, as the fit may not be. With `info`, the smallest eigenvalue before clipping and
    the largest change the clipping makes to a latent correlation are put in it."""
    p = binary.mean(axis=1).clip(1e-6, 1 - 1e-6)
    gamma = stats.norm.ppf(p)
    joint = (binary @ binary.T) / binary.shape[1]
    n = len(p)
    iu = np.triu_indices(n, 1)
    target = joint[iu]
    lo, hi = np.full(len(target), -0.999), np.full(len(target), 0.999)
    for _ in range(40):
        mid = (lo + hi) / 2
        val = bvn_cdf(gamma[iu[0]], gamma[iu[1]], mid)
        up = val < target
        lo = np.where(up, mid, lo)
        hi = np.where(up, hi, mid)
    lam = np.eye(n)
    lam[iu] = (lo + hi) / 2
    lam[(iu[1], iu[0])] = (lo + hi) / 2
    vals, vecs = np.linalg.eigh(lam)
    fitted = lam
    lam = (vecs * np.maximum(vals, 1e-4)) @ vecs.T
    d = np.sqrt(np.diag(lam))
    lam = lam / np.outer(d, d)
    if info is not None:
        info["min_eigenvalue"] = float(vals.min())
        info["max_change"] = float(np.abs(lam - fitted).max())
    return gamma, lam


def sample_dg(gamma: np.ndarray, lam: np.ndarray, n_bins: int, rng: np.random.Generator) -> np.ndarray:
    chol = np.linalg.cholesky(lam)
    x = (rng.standard_normal((n_bins, len(gamma)), dtype=np.float32) @ chol.T.astype(np.float32))
    return (x > -gamma[None, :].astype(np.float32)).T.astype(np.float32)


# --- per-recording analyses, run in worker processes ------------------------------------------
# The notebook sets SITES (and STIM, the 5-ms and 1-ms stimuli by name) before forking workers.

SITES: list[dict] = []
STIM: dict = {}
BIN_SIZES = (2, 5, 8, 10, 15, 20, 35, 50)   # Materials and methods, STRF mutual information
N_EVENTS_5A = 5000                          # Materials and methods
PR_BINS = 15                                # Materials and methods, Simulated spike trains


def run_main(i: int, seed: int) -> dict:
    """cNE detection at 10 ms with membership and activity thresholds."""
    det = detect(binned(SITES[i], BIN_MS), seed)
    det.pop("eigenvalues")
    return det


def run_halves(i: int, seed: int) -> dict:
    """Detection on two interleaved halves (10 equal parts; odd parts A, even parts B)."""
    c = binned(SITES[i], BIN_MS)
    parts = np.array_split(np.arange(c.shape[1]), 10)
    a = np.concatenate(parts[0::2])
    b = np.concatenate(parts[1::2])
    out = {}
    for name, idx in (("A", a), ("B", b)):
        d = detect(c[:, idx], seed + (0 if name == "A" else 5000), activity_null=False)
        out[name] = {"w": d["w"], "shuffled_w": d.get("shuffled_w", []), "kept": d["kept"], "n": d["n"]}
    return out


def run_traintest(i: int, seed: int) -> dict:
    """Detection on the first (training) and second (test) halves; both IC sets projected onto the
    z-scored test half; correlations of training with test activities, per projection reading."""
    c = binned(SITES[i], BIN_MS)
    half = c.shape[1] // 2
    tr, te = c[:, :half], c[:, half:]
    keep = np.flatnonzero((tr.std(axis=1) > 0) & (te.std(axis=1) > 0))
    dtr = detect(tr[keep], seed, null=False)
    dte = detect(te[keep], seed + 1, null=False)
    zte = zscore(te[keep])
    out = {"n_train": dtr["n"], "n_test": dte["n"]}
    for p in PROJECTIONS:
        if dtr["n"] == 0 or dte["n"] == 0:
            out[p] = np.zeros((dtr["n"], dte["n"]))
            continue
        a = activity(zte, orient(dtr["w"], "a"), p)
        b = activity(zte, orient(dte["w"], "a"), p)
        out[p] = np.corrcoef(a, b)[:dtr["n"], dtr["n"]:]
    return out


def unit_strfs(site: dict, stim: np.ndarray, bin_ms: float, lags: int) -> list[np.ndarray]:
    return [sta(stim, segment_index(u["stim_ms"][np.isfinite(u["stim_ms"])], bin_ms, stim.shape[1], lags), lags)
            for u in site["units"]]


def run_binsizes(i: int, seed: int) -> dict:
    """Detection at each bin size (number, sizes) and, per cNE, the STRF MI of Figure 5A: activity
    interpolated to 1 ms, the 5000 largest samples (event reading a) or the 5000 largest local
    peaks (event reading b) as events, STRF by event-triggered average. Also, per cNE, the number
    of distinct detection bins the events fall in, and the MI with the STRF from held-out events
    (`strf_mi_heldout`)."""
    site = SITES[i]
    stim = STIM[(site["stim"], STRF_BIN_MS)]
    rng = np.random.default_rng(seed)
    rng_ho = np.random.default_rng(seed + 100000)
    n_ms = int(stim_duration_ms(site))
    out = {}
    for b in BIN_SIZES:
        c = binned(site, b)
        d = detect(c, seed + b, activity_null=False)
        res = {"n": d["n"], "sizes_a": [len(m) for m in member_sets(d, "a")] if d["n"] else [],
               "sizes_b": [len(m) for m in member_sets(d, "b")] if d["n"] else [], "mi": {},
               "mi_heldout": {}, "distinct_bins": {}}
        if d["n"]:
            z = zscore(c[d["kept"]])
            w = orient(d["w"], "a")
            for p in PROJECTIONS:
                act = activity(z, w, p)
                for er in ("a", "b"):
                    mis, mis_ho, nd = [], [], []
                    for j in range(d["n"]):
                        a1 = interp_activity(act[j], b, n_ms)
                        if er == "a":
                            ev = np.argsort(a1)[-N_EVENTS_5A:]
                        else:
                            peaks = np.flatnonzero((a1[1:-1] > a1[:-2]) & (a1[1:-1] >= a1[2:])) + 1
                            ev = peaks[np.argsort(a1[peaks])[-N_EVENTS_5A:]]
                        nd.append(len(np.unique(ev // b)))
                        idx = segment_index(ev + 0.5, STRF_BIN_MS, stim.shape[1], STRF_LAGS)
                        strf = sta(stim, idx, STRF_LAGS)
                        zall = projections(stim, strf)
                        mis.append(strf_mi(zall[STRF_LAGS - 1:], zall[idx], rng))
                        mis_ho.append(strf_mi_heldout(stim, idx, STRF_LAGS, rng_ho))
                    res["mi"][(p, er)] = mis
                    res["mi_heldout"][(p, er)] = mis_ho
                    res["distinct_bins"][(p, er)] = nd
        out[b] = res
    return out


def pair_table(i: int, det: dict, reading: str = "a") -> list[dict]:
    """All unit pairs of a recording with PWC measures (both lag readings), correlation coefficient
    at 10 ms, distances, and whether they share a cNE. PWCs use the spikes inside the stimulus
    period, on the stimulus clock, as the correlation coefficient does. Also, as variants the
    claims file does not name, sharpness with a baseline subtracted and over +-10 and +-20 ms."""
    site = SITES[i]
    units = site["units"]
    c = binned(site, BIN_MS)
    r = np.corrcoef(c)
    sets = member_sets(det, reading) if det["n"] else []
    spikes = [u["stim_ms"][np.isfinite(u["stim_ms"])] for u in units]
    dur = stim_duration_ms(site)
    rows = []
    for a in range(len(units)):
        ta = spikes[a]
        for b in range(a + 1, len(units)):
            tb = spikes[b]
            h = pwc(ta, tb, 100.0)
            s100, d100 = pwc_measures(h)
            s50, d50 = pwc_measures(h[50:151])
            # baseline readings: the count per 1-ms bin expected from the two rates, or the mean of
            # the outer +-50 to 100 ms of the histogram, subtracted and the rest clipped at zero
            ind = len(ta) * len(tb) / dur
            flank = np.r_[h[:50], h[151:]].mean()
            extra = {f"sharp_{lag}_{name}": pwc_measures(np.clip(h[100 - lag:101 + lag] - base, 0, None))[0]
                     for lag in (50, 100) for name, base in (("ind", ind), ("flank", flank))}
            extra.update({f"sharp_{lag}": pwc_measures(h[100 - lag:101 + lag])[0] for lag in (10, 20)})
            shared = sum(1 for m in sets if a in m and b in m)
            in_any = (any(a in m for m in sets), any(b in m for m in sets))
            rows.append({"site": site["site"], "a": a, "b": b, "r": r[a, b],
                         "sharp_50": s50, "delay_50": d50, "sharp_100": s100, "delay_100": d100,
                         "count_50": int(h[50:151].sum()),
                         "depth_diff": abs(units[a]["depth"] - units[b]["depth"]),
                         "euclid": float(np.hypot(units[a]["x"] - units[b]["x"],
                                                  units[a]["depth"] - units[b]["depth"])),
                         "n_shared": shared, "both_members": all(in_any), **extra})
    return rows


def run_pairs(i: int, det: dict) -> list[dict]:
    return pair_table(i, det)


def run_strf_profiles(i: int) -> list[np.ndarray]:
    """1-ms STRFs (50 lags), for the temporal profiles of Figure 6B, E."""
    site = SITES[i]
    stim = STIM[(site["stim"], 1)]
    return unit_strfs(site, stim, 1, 50)


def cne_events_10ms(det: dict, z: np.ndarray, projection: str, reading: str) -> list[np.ndarray]:
    """Event times (ms, stimulus clock, the centre of the 10-ms bin) of each cNE: activity above the
    99.9th percentile threshold; reading (a) every bin, (b) the peak bin of each run."""
    act = activity(z, orient(det["w"], "a"), projection)
    thr = det["act_threshold"][projection]
    return [(events_from_activity(act[j], thr[j], reading) + 0.5) * BIN_MS for j in range(det["n"])]


def _strf_measures(times: np.ndarray, stim: np.ndarray, rng) -> tuple[float, float, int]:
    idx = segment_index(times, STRF_BIN_MS, stim.shape[1], STRF_LAGS)
    strf = sta(stim, idx, STRF_LAGS)
    zall = projections(stim, strf)
    return float(strf.max() - strf.min()), strf_mi(zall[STRF_LAGS - 1:], zall[idx], rng), len(idx)


def run_cne_vs_members(i: int, det: dict, seed: int, heldout: bool = True) -> list[dict]:
    """Figure 10B, C: STRF PTD and MI of each cNE and each of its members, after subsampling the
    larger of the event and spike trains to equal counts. Also the MI with the STRF from held-out
    events (`strf_mi_heldout`), on the same subsampled trains."""
    site = SITES[i]
    stim = STIM[(site["stim"], STRF_BIN_MS)]
    rng = np.random.default_rng(seed)
    rng_ho = np.random.default_rng(seed + 100000)
    if det["n"] == 0:
        return []
    z = zscore(binned(site, BIN_MS)[det["kept"]])
    rows = []
    sets = member_sets(det, "a")
    for p in PROJECTIONS:
        for er in ("a", "b"):
            evs = cne_events_10ms(det, z, p, er)
            for j, members in enumerate(sets):
                for m in members:
                    sp = site["units"][m]["stim_ms"]
                    sp = sp[np.isfinite(sp)]
                    ev = evs[j]
                    k = min(len(sp), len(ev))
                    if k < 2:
                        continue
                    ev_s = np.sort(rng.choice(ev, k, replace=False))
                    sp_s = np.sort(rng.choice(sp, k, replace=False))
                    ptd_c, mi_c, _ = _strf_measures(ev_s, stim, rng)
                    ptd_n, mi_n, _ = _strf_measures(sp_s, stim, rng)
                    ho = [strf_mi_heldout(stim, segment_index(t, STRF_BIN_MS, stim.shape[1], STRF_LAGS),
                                          STRF_LAGS, rng_ho) if heldout else np.nan for t in (ev_s, sp_s)]
                    rows.append({"site": site["site"], "cne": j, "unit": m, "projection": p,
                                 "events": er, "count": k, "ptd_cne": ptd_c, "ptd_unit": ptd_n,
                                 "mi_cne": mi_c, "mi_unit": mi_n, "mi_cne_heldout": ho[0],
                                 "mi_unit_heldout": ho[1]})
    return rows


def random_groups(members: np.ndarray, others: list[np.ndarray], n_units: int, n_groups: int,
                  rng: np.random.Generator, max_draws: int = 20000) -> tuple[list[tuple], int]:
    """Random groups of the cNE's size (Materials and methods, MI comparisons): `level` members of the
    cNE and the rest from non-members, with at most `level` units from any other cNE; the level is
    raised until `n_groups` unique groups are found within `max_draws` draws (a standard choice).
    When no level reaches `n_groups` (a 2-unit cNE has too few possible groups), the largest set
    found is used, at the lowest level that gave it (a standard choice; the Methods do not say)."""
    size = len(members)
    non = np.setdiff1d(np.arange(n_units), members)
    best, best_level = [], 1
    for level in range(1, size + 1):
        if size - level > len(non):
            continue
        found = set()
        for _ in range(max_draws):
            g = tuple(sorted(np.r_[rng.choice(members, level, replace=False),
                                   rng.choice(non, size - level, replace=False)].tolist()))
            if g == tuple(sorted(members.tolist())):
                continue
            if any(len(np.intersect1d(g, o)) > level for o in others):
                continue
            found.add(g)
            if len(found) >= n_groups:
                return sorted(found), level
        if len(found) > len(best):
            best, best_level = sorted(found), level
    return best, best_level


def run_random_groups(i: int, det: dict, seed: int, n_groups: int = 500) -> list[dict]:
    """Figure 10-figure supplement 1: PTD and STRF MI of the summed spikes of each cNE's members and
    of random groups, all subsampled to the fewest spikes; sets under 200 spikes left out."""
    site = SITES[i]
    stim = STIM[(site["stim"], STRF_BIN_MS)]
    rng = np.random.default_rng(seed)
    if det["n"] == 0:
        return []
    sets = member_sets(det, "a")
    spikes = [u["stim_ms"][np.isfinite(u["stim_ms"])] for u in site["units"]]
    rows = []
    for j, members in enumerate(sets):
        if len(members) < 2:
            continue
        others = [s for k, s in enumerate(sets) if k != j]
        groups, level = random_groups(members, others, len(spikes), n_groups, rng)
        trains = [np.concatenate([spikes[m] for m in members])] + \
                 [np.concatenate([spikes[m] for m in g]) for g in groups]
        k = min(len(t) for t in trains)
        if k < 200:
            rows.append({"site": site["site"], "cne": j, "size": len(members), "n_groups": len(groups),
                         "level": level, "count": k, "excluded": True})
            continue
        ptd, mi = [], []
        for t in trains:
            p_, m_, _ = _strf_measures(np.sort(rng.choice(t, k, replace=False)), stim, rng)
            ptd.append(p_)
            mi.append(m_)
        ptd, mi = np.array(ptd), np.array(mi)
        rows.append({"site": site["site"], "cne": j, "size": len(members), "n_groups": len(groups),
                     "level": level, "count": k, "excluded": False,
                     "ptd_cne": ptd[0], "ptd_rand_median": float(np.median(ptd[1:])),
                     "ui_ptd": float((ptd >= ptd[0]).mean()),
                     "mi_cne": mi[0], "mi_rand_median": float(np.median(mi[1:])),
                     "ui_mi": float((mi >= mi[0]).mean())})
    return rows


# --- models (Figure 11C, D and its supplement 3) ---------------------------------------------

def pr_setup(site: dict, model_bin: float) -> list[dict]:
    """Per unit, for the PR model on bins of `model_bin` ms: the STRF projection class (one of 15
    equal bins over the full range of projection values) of the stimulus segment before each bin,
    and the unit's spike count in each class. Units without spikes in the stimulus get no model."""
    stim = STIM[(site["stim"], STRF_BIN_MS)]
    n_bins = int(stim_duration_ms(site) // BIN_MS) * int(BIN_MS // model_bin)
    starts = np.arange(n_bins) * model_bin
    seg = np.floor(starts / STRF_BIN_MS).astype(int) - 1     # last stimulus bin before the model bin
    ok = seg >= STRF_LAGS - 1
    out = []
    for u in site["units"]:
        t = u["stim_ms"][np.isfinite(u["stim_ms"])]
        strf = sta(stim, segment_index(t, STRF_BIN_MS, stim.shape[1], STRF_LAGS), STRF_LAGS)
        z = projections(stim, strf)[np.clip(seg, 0, None)]
        z[~ok] = np.nan
        edges = np.linspace(np.nanmin(z), np.nanmax(z), PR_BINS + 1)
        cls = np.clip(np.digitize(z, edges[1:-1]), 0, PR_BINS - 1)
        cls[~ok] = -1
        counts = np.histogram(t, np.r_[starts, starts[-1] + model_bin])[0]
        members = [np.flatnonzero(cls == k) for k in range(PR_BINS)]
        spikes = [int(counts[m].sum()) for m in members]
        out.append({"members": members, "spikes": spikes, "n_bins": n_bins,
                    "strf": strf, "dropped": int(counts[~ok].sum())})
    return out


def pr_sample(setup: list[dict], rng: np.random.Generator, units=None) -> np.ndarray:
    """PR trains: each spike assigned to a random time bin of its projection class."""
    units = range(len(setup)) if units is None else units
    out = np.zeros((len(units), setup[0]["n_bins"]), dtype=np.float32)
    for r, u in enumerate(units):
        s = setup[u]
        for m, k in zip(s["members"], s["spikes"]):
            if k and len(m):
                np.add.at(out[r], m[rng.integers(0, len(m), k)], 1)
    return out


def rebin(c: np.ndarray, k: int) -> np.ndarray:
    n = c.shape[1] // k
    return c[:, :n * k].reshape(c.shape[0], n, k).sum(axis=2)


def model_trains(name: str, ctx: dict, rng: np.random.Generator) -> np.ndarray:
    """One model matrix at 10 ms: 'shuffled', 'pr10', 'pr5' or 'dg'."""
    if name == "shuffled":
        return circular_shuffle(ctx["real"], rng)
    if name == "pr10":
        return pr_sample(ctx["pr10"], rng)
    if name == "pr5":
        return rebin(pr_sample(ctx["pr5"], rng), 2)
    if name == "dg":
        return rebin(sample_dg(ctx["gamma"], ctx["lam"], ctx["n5"], rng), 2)
    raise ValueError(name)


MODELS = ("shuffled", "pr10", "pr5", "dg")


def model_context(site: dict) -> dict:
    real = binned(site, BIN_MS)
    b5 = np.minimum(binned(site, 5), 1)
    gamma, lam = fit_dg(b5)
    return {"real": real, "pr10": pr_setup(site, 10), "pr5": pr_setup(site, 5),
            "gamma": gamma, "lam": lam, "n5": b5.shape[1]}


def run_dg_check(i: int, seed: int) -> dict:
    """How well the DG fit reproduces the real 5-ms binary trains: the clipping of `fit_dg`, and the
    rates and pairwise covariances of one sampled run against the real ones."""
    site = SITES[i]
    b5 = np.minimum(binned(site, 5), 1)
    info = {}
    gamma, lam = fit_dg(b5, info)
    sim = sample_dg(gamma, lam, b5.shape[1], np.random.default_rng(seed))
    iu = np.triu_indices(len(gamma), 1)
    cov_r, cov_s = np.cov(b5)[iu], np.cov(sim)[iu]
    return {"site": site["site"], "min_eigenvalue": info["min_eigenvalue"], "max_change": info["max_change"],
            "rate_max_abs_diff": float(np.abs(sim.mean(axis=1) - b5.mean(axis=1)).max()),
            "rate_real_mean": float(b5.mean()),
            "cov_r": float(np.corrcoef(cov_r, cov_s)[0, 1]),
            "cov_slope": float(np.polyfit(cov_r, cov_s, 1)[0]),
            "cov_median_abs_diff": float(np.median(np.abs(cov_s - cov_r))),
            "cov_real_median_abs": float(np.median(np.abs(cov_r))),
            "pr_dropped_spikes_10": sum(u["dropped"] for u in pr_setup(site, 10)),
            "pr_dropped_spikes_5": sum(u["dropped"] for u in pr_setup(site, 5)),
            "spikes": int(sum(np.isfinite(u["stim_ms"]).sum() for u in site["units"]))}


def run_models(i: int, det: dict, seed: int, n_iter: int) -> dict:
    """Number and mean size of cNEs in `n_iter` runs of each model. Membership uses the recording's
    own thresholds (sign reading a) from the shuffles of the real data."""
    site = SITES[i]
    ctx = model_context(site)
    lo, hi = det["thresholds"]["a"]
    out = {}
    for mi_, name in enumerate(MODELS):
        rng = np.random.default_rng(seed + 1000 * mi_)
        ns, sizes = [], []
        for it in range(n_iter):
            c = model_trains(name, ctx, rng)
            keep = np.flatnonzero(c.std(axis=1) > 0)
            z = zscore(c[keep])
            vals, vecs = pcs(z)
            k = int((vals > mp_bound(*z.shape)).sum())
            ns.append(k)
            if k:
                w = orient(_ica_weights(z, vals[:k], vecs[:, :k], seed + it), "a")
                sizes.append(float(np.mean(((w > hi) | (w < lo)).sum(axis=0))))
            else:
                sizes.append(np.nan)
        out[name] = {"n": np.array(ns), "size": np.array(sizes)}
    return out


def run_strf_similarity(i: int, seed: int, n_iter: int) -> dict:
    """Correlation of each unit's model STRF with its real STRF, both from trains binned as the
    model is (10 ms; 5 ms for pr5), spikes placed at bin centres."""
    site = SITES[i]
    stim = STIM[(site["stim"], STRF_BIN_MS)]
    ctx = model_context(site)
    rng = np.random.default_rng(seed)
    out = {}

    def strfs(c, bin_ms):
        res = []
        for row in c:
            nz = np.flatnonzero(row)
            t = np.repeat((nz + 0.5) * bin_ms, row[nz].astype(int))
            res.append(sta(stim, segment_index(t, STRF_BIN_MS, stim.shape[1], STRF_LAGS), STRF_LAGS).ravel())
        return res

    real10 = strfs(ctx["real"], 10)
    real5 = strfs(binned(site, 5), 5)
    for name in MODELS:
        vals = []
        for it in range(n_iter):
            if name == "pr5":
                c, ref, bm = pr_sample(ctx["pr5"], rng), real5, 5
            elif name == "dg":
                c, ref, bm = sample_dg(ctx["gamma"], ctx["lam"], ctx["n5"], rng), real5, 5
            else:
                c, ref, bm = model_trains(name, ctx, rng), real10, 10
            for a, b in zip(strfs(c, bm), ref):
                if a.std() > 0 and b.std() > 0:
                    vals.append(float(np.corrcoef(a, b)[0, 1]))
        out[name] = np.array(vals)
    return out


def coincidence_ratio(binary: np.ndarray) -> float:
    """Bins where all units spike over bins where the unit with the lowest rate spikes."""
    low = binary[np.argmin(binary.sum(axis=1))]
    return float(np.all(binary, axis=0).sum() / low.sum()) if low.sum() else np.nan


def run_cr(i: int, groups: list[tuple], seed: int, n_iter: int) -> list[dict]:
    """Real and model CRs (median over `n_iter` runs) for groups of units of this recording."""
    site = SITES[i]
    ctx = model_context(site)
    rng = np.random.default_rng(seed)
    real = ctx["real"] > 0
    units = sorted({u for g in groups for u in g})
    pos = {u: k for k, u in enumerate(units)}
    idx = [[pos[u] for u in g] for g in groups]
    sub_gamma = ctx["gamma"][units]
    sub_lam = ctx["lam"][np.ix_(units, units)]
    t = ctx["real"].shape[1]
    crs = {m: np.full((n_iter, len(groups)), np.nan) for m in MODELS}
    for it in range(n_iter):
        shifts = rng.integers(1, t, size=len(units))
        sims = {"shuffled": np.stack([np.roll(real[u], s) for u, s in zip(units, shifts)]),
                "pr10": pr_sample(ctx["pr10"], rng, units) > 0,
                "pr5": rebin(pr_sample(ctx["pr5"], rng, units), 2) > 0,
                "dg": rebin(sample_dg(sub_gamma, sub_lam, ctx["n5"], rng), 2) > 0}
        for m in MODELS:
            crs[m][it] = [coincidence_ratio(sims[m][ix]) for ix in idx]
    rows = []
    for k, g in enumerate(groups):
        row = {"site": site["site"], "group": g, "size": len(g), "real": coincidence_ratio(real[list(g)])}
        for m in MODELS:
            row[m] = float(np.nanmedian(crs[m][:, k]))
        rows.append(row)
    return rows
