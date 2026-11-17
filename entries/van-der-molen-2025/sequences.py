"""Loading and measures for van der Molen, Spaeth, Chini et al. (2025) on DANDI:001603.

Every recording is read from the dandiset's sorted files at the pinned version, by streaming
(remfile and h5py), from the 1 ms spike matrix ``processing/curated_binning/t_spk_mat`` that each
sorted file holds. That matrix is the input of the paper's own code (the claims file, opening
comment: "Spike matrix at 1 ms resolution"). It marks a bin as 1 when it holds at least one spike.

Where each parameter comes from is said beside it:
- "claims" means the claims file's opening comment or the claim's criterion, which cite the paper's
  Methods or its code (github.com/braingeneers/Protosequences at e9a79c4);
- "paper" means a passage of the paper taken by the author (protocol, author step 1.6), cited;
- "standard choice" means a detail that cannot change an outcome beyond noise.
"""
import json
import urllib.request

import h5py
import numba
import numpy as np
import remfile
from scipy import ndimage, signal, stats

DANDISET = "001603"
VERSION = "0.260923.0623"
API = "https://api.dandiarchive.org/api"

# Recording length kept, in seconds (claims, opening comment, reading (a): the code's
# KEEP_DURATION, 180 s for HO1 to HO4, MS and Pr and 600 s for HO5 to HO8 and MO).
KEEP_S = {"HO_sharf": 180, "HO_alam": 600, "MO": 600, "MS": 180, "PR": 180}

# Burst detection (claims, opening comment, from the Methods "Population rate calculations").
BURST_PARAMS = {
    "default": dict(square_ms=20, gauss_ms=100, rms_mult=4.0, edge_frac=0.10),
    "PR": dict(square_ms=20, gauss_ms=50, rms_mult=3.0, edge_frac=0.20),
}
MIN_PEAK_DIST_MS = 700  # Methods; 800 ms is the code's value, a variant
EDGE_DROP_START_MS = 450  # claims (code): bursts within 450 ms of the start are dropped
EDGE_DROP_END_MS = 1000  # claims (code): and within 1000 ms of the end

# Backbone thresholds: fraction of bursts with at least two spikes (claims, opening comment).
BACKBONE_FRAC = {"HO": 1.0, "PR": 1.0, "MO": 0.8, "MS": 0.9}
MS_BACKBONE_VARIANT = 0.7  # Fig. 6B legend, the second slice reading

RATE_SMOOTH_MS = 50  # Methods, "Single-unit firing rate": a 50 ms Gaussian on the inverse ISI
MIN_SPIKES = 30  # Methods: units with at least 30 spikes
WIN_PRE, WIN_POST = 250, 500  # Methods: -250 to 500 ms around the burst peak
B2B_MAXLAG = 10  # Methods, burst-to-burst correlation: xcorr maxlag 10 ms
PAIR_MAXLAG = 350  # Methods, pairwise correlations: xcorr maxlag 350 ms


def model_type(name):
    """Model type of a recording name: HO, MO, MS or PR."""
    if name.startswith("HO"):
        return "HO"
    if name.startswith("MO"):
        return "MO"
    if name.startswith("PR") or name.startswith("Pr"):
        return "PR"
    return "MS"


def keep_seconds(name):
    t = model_type(name)
    if t == "HO":
        return KEEP_S["HO_sharf"] if name[:3] in ("HO1", "HO2", "HO3", "HO4") else KEEP_S["HO_alam"]
    return KEEP_S[t]


# ---------------------------------------------------------------- archive


def list_assets():
    """All assets of the pinned version: path, asset id and size."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=500"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += [dict(path=a["path"], asset_id=a["asset_id"], size=a["size"]) for a in page["results"]]
        url = page["next"]
    return out


def asset_url(asset_id):
    return f"{API}/assets/{asset_id}/download/"


def open_nwb(asset_id):
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def sorted_file_info(asset):
    """Identifier, subject, age and shapes of one sorted file (metadata only)."""
    with open_nwb(asset["asset_id"]) as f:
        d = f["processing/curated_binning/t_spk_mat/data"]
        return dict(
            path=asset["path"],
            identifier=f["identifier"][()].decode(),
            subject=f["general/subject/subject_id"][()].decode(),
            age=f["general/subject/age"][()].decode(),
            species=f["general/subject/species"][()].decode(),
            frames=d.shape[0],
            n_units=d.shape[1],
            has_units_table="units" in f,
        )


def load_matrix(asset_id, keep_s=None):
    """The 1 ms spike matrix as booleans, units by frames, cut to the first keep_s seconds."""
    with open_nwb(asset_id) as f:
        d = f["processing/curated_binning/t_spk_mat/data"]
        n = d.shape[0] if keep_s is None else min(d.shape[0], int(keep_s * 1000))
        m = d[:n, :]
    return np.ascontiguousarray(m.T.astype(bool))


def load_units_table(asset_id):
    """Spike times per unit from the units table, where the file has one (NaN entries removed)."""
    with open_nwb(asset_id) as f:
        if "units" not in f:
            return None
        st = f["units/spike_times"][:]
        idx = f["units/spike_times_index"][:]
    out, a = [], 0
    for b in idx:
        x = st[a:b]
        out.append(x[~np.isnan(x)])
        a = b
    return out


# ---------------------------------------------------------------- smoothing


def movmean(x, w):
    """Centered moving mean of width w frames (MATLAB smoothdata 'movmean')."""
    return ndimage.uniform_filter1d(np.asarray(x, float), size=w, axis=-1, mode="nearest")


def gauss(x, w):
    """Gaussian smoothing over a window of w frames, as MATLAB smoothdata 'gaussian': standard
    deviation w/5 and the kernel cut at the window (a standard choice for the kernel width)."""
    x = np.asarray(x)
    if x.dtype not in (np.float32, np.float64):
        x = x.astype(float)
    return ndimage.gaussian_filter1d(x, sigma=w / 5.0, axis=-1, mode="nearest",
                                     truncate=2.5)


# ---------------------------------------------------------------- bursts


def detect_bursts(M, mtype, min_dist_ms=MIN_PEAK_DIST_MS):
    """Population bursts (claims, opening comment; Methods "Population rate calculations").

    Returns a dict with arrays start, end and peak (frames) and the coarse population rate."""
    p = BURST_PARAMS["PR"] if mtype == "PR" else BURST_PARAMS["default"]
    pop = M.sum(0).astype(float)
    coarse = gauss(movmean(pop, p["square_ms"]), p["gauss_ms"])
    fine = gauss(movmean(pop, 5), 5)
    rms = np.sqrt(np.mean(coarse ** 2))
    pk, _ = signal.find_peaks(coarse, height=p["rms_mult"] * rms, distance=min_dist_ms)
    T = len(coarse)
    starts, ends, peaks = [], [], []
    for k in pk:
        thr = p["edge_frac"] * coarse[k]
        below = np.nonzero(coarse[:k] < thr)[0]
        s = below[-1] if len(below) else 0
        above = np.nonzero(coarse[k:] < thr)[0]
        e = k + above[0] if len(above) else T - 1
        pt = s + int(np.argmax(fine[s:e + 1]))
        starts.append(s)
        ends.append(e)
        peaks.append(pt)
    starts, ends, peaks = (np.array(x, dtype=int) for x in (starts, ends, peaks))
    keep = (peaks >= EDGE_DROP_START_MS) & (peaks <= T - EDGE_DROP_END_MS)
    return dict(start=starts[keep], end=ends[keep], peak=peaks[keep], coarse=coarse,
                rms=rms, n_raw=len(pk))


def spikes_in_bursts(M, bursts):
    """Spike counts per unit and burst between burst start and end (units by bursts)."""
    c = np.cumsum(np.concatenate([np.zeros((M.shape[0], 1), np.int32), M.astype(np.int32)], 1), 1)
    return c[:, bursts["end"] + 1] - c[:, bursts["start"]]


def backbone_mask(counts, frac):
    """Backbone units: at least two spikes in at least frac of the bursts (claims)."""
    return (counts >= 2).mean(1) >= frac - 1e-12


# ---------------------------------------------------------------- rates


def isi_rates(M, bursts=None, smooth=True):
    """Inverse-ISI rates of all units in Hz (units by frames, float32): the inverse ISI held between
    consecutive spikes, zero before the first and after the last spike, then the 50 ms Gaussian
    (Methods, "Single-unit firing rate"; the code's compute_rate_isi).

    With bursts given, the paper's "burst-only" rates: spikes outside the burst windows (start to
    end) are removed first. The inverse ISI is then held only between spikes of the same burst
    window; the code also holds it across the gap between two bursts (below 1 Hz for gaps over a
    second). This deviation keeps the rate zero between bursts, so that cross-correlations can be
    computed on the burst windows alone."""
    U, T = M.shape
    R = np.zeros((U, T), np.float32)
    if bursts is None:
        wins = [(0, T - 1)]
    else:
        wins = list(zip(bursts["start"], bursts["end"]))
    for u in range(U):
        f_all = np.nonzero(M[u])[0]
        for s0, e0 in wins:
            f = f_all[(f_all >= s0) & (f_all <= e0)]
            if len(f) < 2:
                continue
            isi = np.diff(f)
            R[u, f[0]:f[-1]] = np.repeat(1000.0 / isi, isi)
    if smooth:
        R = gauss(R, RATE_SMOOTH_MS).astype(np.float32)
    return R


def burst_mask(bursts, T):
    m = np.zeros(T, bool)
    for s, e in zip(bursts["start"], bursts["end"]):
        m[s:e + 1] = True
    return m


def burst_segments(R, peaks, pre=WIN_PRE, post=WIN_POST):
    """Rates from -pre to +post ms around each peak: units by bursts by frames."""
    idx = peaks[:, None] + np.arange(-pre, post + 1)[None, :]
    idx = np.clip(idx, 0, R.shape[1] - 1)
    return R[:, idx]


# ---------------------------------------------------------------- correlations


def xcorr_coeff_max(X, maxlag):
    """For a units-by-bursts-by-frames array, MATLAB xcorr(x, y, maxlag, 'coeff') between every pair
    of bursts of each unit; returns the maximum over lags, units by bursts by bursts."""
    U, B, T = X.shape
    X = X.astype(np.float64)
    norm = np.sqrt((X ** 2).sum(2))
    best = np.full((U, B, B), -np.inf)
    for lag in range(-maxlag, maxlag + 1):
        if lag >= 0:
            a, b = X[:, :, lag:], X[:, :, :T - lag]
        else:
            a, b = X[:, :, :T + lag], X[:, :, -lag:]
        c = np.einsum("ubt,uct->ubc", a, b)
        best = np.maximum(best, c)
    den = norm[:, :, None] * norm[:, None, :]
    with np.errstate(invalid="ignore", divide="ignore"):
        return best / den


def burst_to_burst(M, bursts, min_frac=0.3, min_spikes=MIN_SPIKES, R=None):
    """Burst-to-burst correlation per unit (claims, fig2e-b2b-correlation; Methods).

    Burst-only rates; per pair of bursts in which the unit has at least two spikes in the -250 to
    500 ms window, the maximum xcorr coefficient within 10 ms; the mean over those pairs. Units kept
    with at least two spikes in at least min_frac of the bursts and at least min_spikes spikes.
    Returns an array with NaN for units not kept."""
    U, T = M.shape
    if R is None:
        R = isi_rates(M, bursts)
    peaks = bursts["peak"]
    win = peaks[:, None] + np.arange(-WIN_PRE, WIN_POST + 1)[None, :]
    win = np.clip(win, 0, T - 1)
    cnt_win = M[:, win].sum(2)  # units by bursts
    active = cnt_win >= 2
    keep = (active.mean(1) >= min_frac) & (M.sum(1) >= min_spikes)
    out = np.full(U, np.nan)
    idx = np.nonzero(keep)[0]
    if len(idx) == 0:
        return out
    X = R[idx][:, win]
    C = xcorr_coeff_max(X, B2B_MAXLAG)
    B = len(peaks)
    tri = np.triu(np.ones((B, B), bool), 1)
    for j, u in enumerate(idx):
        a = active[u]
        pm = tri & a[:, None] & a[None, :]
        v = C[j][pm]
        v = v[np.isfinite(v)]
        out[u] = v.mean() if len(v) else np.nan
    return out


def compress_zeros(R, keep_gap=PAIR_MAXLAG + 1):
    """Shorten every run of frames where all rates are zero to keep_gap frames. Lags up to
    keep_gap - 1 of a zero-padded cross-correlation are unchanged by this (exact)."""
    nz = (R != 0).any(0)
    keep = nz.copy()
    run = 0
    for i in range(len(nz)):
        if nz[i]:
            run = 0
        else:
            run += 1
            if run <= keep_gap:
                keep[i] = True
    return R[:, keep]


def pairwise_xcorr(R, maxlag=PAIR_MAXLAG):
    """MATLAB xcorr(x, y, maxlag, 'coeff') for every pair of rows of R: the maximum coefficient and
    its lag (ms, positive when the second unit lags), each as a units-by-units array (upper triangle
    filled). Computed by FFT in single precision."""
    from scipy import fft as sfft
    R = np.asarray(R, np.float32)
    U, T = R.shape
    L = sfft.next_fast_len(T + maxlag + 1, real=True)
    F = sfft.rfft(R, n=L, axis=1, workers=-1)
    norm = np.sqrt((R.astype(np.float64) ** 2).sum(1))
    C = np.full((U, U), np.nan)
    LAG = np.full((U, U), np.nan)
    lags = np.r_[np.arange(0, maxlag + 1), np.arange(-maxlag, 0)]
    for i in range(U - 1):
        cc = sfft.irfft(F[i][None, :] * np.conj(F[i + 1:]), n=L, axis=1, workers=-1)
        cc = np.concatenate([cc[:, :maxlag + 1], cc[:, L - maxlag:]], axis=1)
        k = np.argmax(cc, axis=1)
        den = norm[i] * norm[i + 1:]
        with np.errstate(invalid="ignore", divide="ignore"):
            C[i, i + 1:] = cc[np.arange(len(k)), k] / den
        LAG[i, i + 1:] = -lags[k]
    return C, LAG


# ---------------------------------------------------------------- shuffles


@numba.njit(cache=True)
def _swap_loop(M, u, t, n_swaps, seed):
    np.random.seed(seed)
    n = len(u)
    done = 0
    tries = 0
    max_tries = 4 * (n_swaps + n)
    while done < n_swaps and tries < max_tries:
        tries += 1
        a = np.random.randint(n)
        b = np.random.randint(n)
        ua, ta, ub, tb = u[a], t[a], u[b], t[b]
        if ua == ub or ta == tb or M[ua, tb] or M[ub, ta]:
            continue
        M[ua, ta] = False
        M[ub, tb] = False
        M[ua, tb] = True
        M[ub, ta] = True
        t[a] = tb
        t[b] = ta
        done += 1
    return done


def okun_shuffle(M, seed, swaps_per_spike=5):
    """Okun et al. swap randomization (Methods, "Randomized recording"; the code's
    shuffle_spike_mats.py): draw two spikes (unit a at frame 1, unit b at frame 2); when a does not
    fire at frame 2 and b does not fire at frame 1, move them, which keeps every unit's count and
    every frame's count. Done 5 times as many times as there are spikes. Returns the shuffled matrix
    and the number of swaps made."""
    M = M.copy()
    u, t = np.nonzero(M)
    u = u.astype(np.int64)
    t = t.astype(np.int64)
    done = _swap_loop(M, u, t, swaps_per_spike * len(u), seed)
    return M, done


def normalize(a, b):
    """(A - B) / (A + B) (Methods)."""
    with np.errstate(invalid="ignore", divide="ignore"):
        return (a - b) / (a + b)


# ---------------------------------------------------------------- peaks and sequences


def peak_times(R, bursts, counts):
    """Per unit and burst, the time of the unit's maximum rate between burst start and end, relative
    to the burst peak (ms), NaN where the unit has fewer than two spikes in the burst (Methods)."""
    U = R.shape[0]
    B = len(bursts["peak"])
    P = np.full((U, B), np.nan)
    for k, (s, e, p) in enumerate(zip(bursts["start"], bursts["end"], bursts["peak"])):
        seg = R[:, s:e + 1]
        P[:, k] = np.argmax(seg, 1) + s - p
    P[counts < 2] = np.nan
    return P


def backbone_window(P, bb):
    """Backbone period: from the earliest to the latest median peak time of backbone units."""
    med = np.nanmedian(P[bb], 1)
    return int(np.floor(np.nanmin(med))), int(np.ceil(np.nanmax(med)))


def cv2(spike_frames):
    """CV2 of Holt et al.: the mean over consecutive interval pairs of 2|I2 - I1| / (I2 + I1)."""
    isi = np.diff(np.asarray(spike_frames, float))
    if len(isi) < 2:
        return np.nan
    return np.mean(2 * np.abs(isi[1:] - isi[:-1]) / (isi[1:] + isi[:-1]))


def _fit_r2(f, x, y, p0):
    from scipy.optimize import curve_fit
    try:
        popt, _ = curve_fit(f, x, y, p0=p0, maxfev=20000)
    except Exception:
        return np.nan
    yh = f(x, *popt)
    return 1 - np.sum((y - yh) ** 2) / np.sum((y - y.mean()) ** 2)


def lognormal_r2(rates, variant=False):
    """Reading (a) of ed1c (Methods; plot_multi_rec_figs_backbone.m): the probability histogram of
    mean rates in 20 bins from 0 to 10 Hz, up to the last non-empty bin, fitted by nonlinear least
    squares with a lognormal density (parameters sigma and mu, start values 1 and 0.25 as the code);
    ordinary R^2. variant=True uses the code's exponent, divided by (2 sigma)^2."""
    edges = np.linspace(0, 10, 21)
    h, _ = np.histogram(rates, bins=edges)
    y = h / max(len(rates), 1)  # MATLAB 'probability' divides by all values, also those beyond 10 Hz
    x = edges[1:] - 0.5 * np.diff(edges)
    last = np.nonzero(y > 0)[0].max()
    x, y = x[:last + 1], y[:last + 1]

    def f(x, sg, mu):
        d = (2 * sg) ** 2 if variant else 2 * sg ** 2
        return 1 / (x * sg * np.sqrt(2 * np.pi)) * np.exp(-(np.log(x) - mu) ** 2 / d)

    return _fit_r2(f, x, y, [1.0, 0.25])


def lognormal_r2_legend(rates):
    """Reading (b) of ed1c (Extended Data Fig. 1C legend; the code's second fit): a normal density
    (sigma and mu, start values 1 and 0.25) fitted to the probability histogram of natural-log rates
    in ceil(n^0.4) bins, placed at the bins' left edges as the code does."""
    lr = np.log(rates[rates > 0])
    nb = int(np.ceil(len(lr) ** 0.4))
    h, edges = np.histogram(lr, bins=nb)
    y = h / h.sum()
    x = edges[1:] - np.diff(edges)
    last = np.nonzero(y > 0)[0].max()
    x, y = x[:last + 1], y[:last + 1]

    def f(x, sg, mu):
        return 1 / (sg * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sg) ** 2)

    return _fit_r2(f, x, y, [1.0, 0.25])


# ---------------------------------------------------------------- compressed burst segments


def burst_segments_compressed(M, bursts, margin=60, gap=PAIR_MAXLAG + 1):
    """Cut the recording to the burst neighbourhoods, each from min(start, peak - 250) - margin to
    max(end, peak + 500) + margin, joined by gap frames of silence. Burst-only rates are zero
    outside the burst windows (apart from the 50 ms Gaussian's tail, under margin), so their
    cross-correlations up to 350 ms lag and their sums are the same on the cut recording (exact).
    Returns the cut matrix and the bursts in its frames."""
    U, T = M.shape
    s0 = np.minimum(bursts["start"], bursts["peak"] - WIN_PRE) - margin
    e0 = np.maximum(bursts["end"], bursts["peak"] + WIN_POST) + margin
    s0 = np.clip(s0, 0, T - 1)
    e0 = np.clip(e0, 0, T - 1)
    cover = np.zeros(T + 2, np.int8)
    for a, b in zip(s0, e0):
        cover[a + 1:b + 2] = 1
    edges = np.diff(cover)
    segs = list(zip(np.nonzero(edges == 1)[0], np.nonzero(edges == -1)[0] - 1))
    total = sum(b - a + 1 for a, b in segs) + gap * (len(segs) + 1)
    out = np.zeros((U, total), bool)
    pos = gap
    shift = np.zeros(T, np.int64)
    for a, b in segs:
        out[:, pos:pos + b - a + 1] = M[:, a:b + 1]
        shift[a:b + 1] = pos - a
        pos += b - a + 1 + gap
    nb = {k: bursts[k] + shift[bursts[k]] for k in ("start", "end", "peak")}
    return out, nb


def pca_cumvar(R, idx, T_full):
    """PCA as compute_manifolds in the code: each unit's rate centred and scaled to unit standard
    deviation over the whole recording (T_full frames; frames outside R are zero), eigenvalues of
    the covariance. Returns the fraction of variance per component, largest first."""
    X = np.asarray(R[idx], np.float64)
    n = T_full
    s1 = X.sum(1)
    S = X @ X.T
    mu = s1 / n
    cov = S / n - np.outer(mu, mu)
    sd = np.sqrt(np.clip(np.diag(cov), 0, None))
    ok = sd > 0
    cov = cov[np.ix_(ok, ok)] / np.outer(sd[ok], sd[ok])
    ev = np.sort(np.linalg.eigvalsh(cov))[::-1]
    ev = np.clip(ev, 0, None)
    return ev / ev.sum()


def pca_ratio(v_all, v_bb, v_nr, k=3):
    """Variance of the first three PCs over that of the first X, X the smallest number of PCs among
    the three selections (Methods, "PCA manifold analysis")."""
    X = min(len(v_all), len(v_bb), len(v_nr))
    return [v[:k].sum() / v[:X].sum() for v in (v_all, v_bb, v_nr)]


def rank_order_corr(P_bb):
    """Spearman correlation of backbone peak-time ranks for every pair of bursts (Supplementary
    Methods, "Firing rate peak rank order correlations"). P_bb is backbone units by bursts; units
    without a peak in a burst are left out of that pair. Returns the upper-triangle values."""
    B = P_bb.shape[1]
    if np.isfinite(P_bb).all():
        rk = stats.rankdata(P_bb, axis=0)
        with np.errstate(invalid="ignore", divide="ignore"):
            C = np.corrcoef(rk.T)
        return C[np.triu_indices(B, 1)]
    out = []
    for i in range(B):
        for j in range(i + 1, B):
            a, b = P_bb[:, i], P_bb[:, j]
            ok = np.isfinite(a) & np.isfinite(b)
            if ok.sum() >= 3:
                out.append(stats.spearmanr(a[ok], b[ok])[0])
            else:
                out.append(np.nan)
    return np.array(out)


def burst_similarity(Z, peaks, frames):
    """Cosine similarity between the unit rate vectors of every pair of bursts at each frame relative
    to the peak (Methods, "Burst similarity score"; comp_burst_sim). Z is units by frames, already
    z-scored over the recording. Returns frames by pairs (upper triangle)."""
    B = len(peaks)
    iu = np.triu_indices(B, 1)
    out = np.full((len(frames), len(iu[0])), np.nan)
    for k, f in enumerate(frames):
        idx = np.clip(peaks + f, 0, Z.shape[1] - 1)
        V = Z[:, idx].T.astype(np.float64)
        nrm = np.linalg.norm(V, axis=1)
        with np.errstate(invalid="ignore", divide="ignore"):
            C = (V @ V.T) / np.outer(nrm, nrm)
        out[k] = C[iu]
    return out


def zscore_rows(R):
    """z-score of each row; a constant row gives zeros, as MATLAB's zscore."""
    mu = R.mean(1, keepdims=True, dtype=np.float64)
    sd = R.std(1, keepdims=True, dtype=np.float64)
    sd[sd == 0] = 1.0
    return ((R - mu) / sd).astype(np.float32)


# ---------------------------------------------------------------- one recording

SIM_FRAMES = np.arange(-450, 1001)  # the code's FRAME_RANGE for burst similarity


def analyse(name, M, seed, n_shuf=0, n_shuf_pair=0, similarity=False, min_dist_ms=MIN_PEAK_DIST_MS,
            light=False):
    """Every measure of one recording that does not need an HMM. M is units by 1 ms frames.
    light=True keeps only bursts, backbone units, peak times and rank-order correlations (with
    their shuffles), for the drug recordings."""
    rng_seeds = np.random.default_rng(seed).integers(0, 2 ** 31 - 1, size=max(n_shuf, 1))
    mt = model_type(name)
    U, T = M.shape
    n_spk = M.sum(1)
    res = dict(name=name, mtype=mt, U=U, T=T, n_spk=n_spk, rate=n_spk / (T / 1000.0))
    b = detect_bursts(M, mt, min_dist_ms)
    res["bursts"] = {k: b[k] for k in ("start", "end", "peak")}
    res["n_bursts"] = len(b["peak"])
    res["n_bursts_800"] = len(detect_bursts(M, mt, 800)["peak"])
    res["cv2"] = np.array([cv2(np.nonzero(m)[0]) for m in M])
    if res["n_bursts"] < 2:
        return res
    counts = spikes_in_bursts(M, b)
    res["counts"] = counts
    res["frac2"] = (counts >= 2).mean(1)
    thr = BACKBONE_FRAC[mt]
    res["bb"] = res["frac2"] >= thr - 1e-12
    if mt == "MS":
        res["bb_70"] = res["frac2"] >= MS_BACKBONE_VARIANT - 1e-12
    res["duration"] = b["end"] - b["start"]
    # full rates: peak times, unit sequence, burst similarity
    R = isi_rates(M)
    res["P"] = peak_times(R, b, counts)
    if similarity:
        Z = zscore_rows(R)
        bbm = res["bb"]
        res["sim_all"] = burst_similarity(Z, b["peak"], SIM_FRAMES)
        res["sim_bb"] = burst_similarity(Z[bbm], b["peak"], SIM_FRAMES) if bbm.sum() else None
        res["sim_nr"] = burst_similarity(Z[~bbm], b["peak"], SIM_FRAMES)
        del Z
    del R
    Mc, bc = burst_segments_compressed(M, b)
    if light:
        res["rank"] = rank_order_corr(res["P"][res["bb"]]) if res["bb"].sum() >= 3 else None
        sh = dict(rank=[])
        for k in range(n_shuf if res["rank"] is not None else 0):
            Ms, _ = okun_shuffle(M, int(rng_seeds[k]))
            Msc, _ = burst_segments_compressed(Ms, b)
            Ps = peak_times(isi_rates(Msc), bc, spikes_in_bursts(Msc, bc))
            sh["rank"].append(rank_order_corr(Ps[res["bb"]]))
        res["shuf"] = sh
        return res
    # burst-only measures on the cut recording
    Rb = isi_rates(Mc, bc)
    res["b2b30"] = burst_to_burst(Mc, bc, 0.3, R=Rb)
    res["b2b70"] = burst_to_burst(Mc, bc, 0.7, R=Rb)
    keep30 = n_spk >= MIN_SPIKES
    res["idx30"] = np.nonzero(keep30)[0]
    C, L = pairwise_xcorr(Rb[keep30])
    res["pw_corr"], res["pw_lag"] = C, L
    sel = {"all": np.arange(U), "bb": np.nonzero(res["bb"])[0], "nr": np.nonzero(~res["bb"])[0]}
    res["pca"] = {k: (pca_cumvar(Rb, v, T) if len(v) >= 3 else None) for k, v in sel.items()}
    # burst segments (-250 to 500 ms) of burst-only rates, for burst clustering
    res["segments"] = burst_segments(Rb, bc["peak"]).astype(np.float32)
    res["rank"] = rank_order_corr(res["P"][res["bb"]]) if res["bb"].sum() >= 3 else None
    del Rb
    # shuffles
    sh = dict(b2b30=[], cv2=[], pca=[], rank=[], pw_corr=[], pw_lag=[], sim_all=[])
    for k in range(n_shuf):
        Ms, _ = okun_shuffle(M, int(rng_seeds[k]))
        sh["cv2"].append(np.array([cv2(np.nonzero(m)[0]) for m in Ms]))
        Msc, _ = burst_segments_compressed(Ms, b)
        Rbs = isi_rates(Msc, bc)
        sh["b2b30"].append(burst_to_burst(Msc, bc, 0.3, R=Rbs))
        pv = {kk: (pca_cumvar(Rbs, v, T) if len(v) >= 3 else None) for kk, v in sel.items()}
        sh["pca"].append(pv)
        if res["rank"] is not None:
            Rfs = isi_rates(Msc)
            Ps = peak_times(Rfs, bc, spikes_in_bursts(Msc, bc))
            sh["rank"].append(rank_order_corr(Ps[res["bb"]]))
            del Rfs
        if k < n_shuf_pair:
            Cs, Ls = pairwise_xcorr(Rbs[keep30])
            sh["pw_corr"].append(Cs)
            sh["pw_lag"].append(np.abs(Ls))
        if similarity and k < n_shuf_pair:
            # the code compares with burst-only rates of the shuffles, z-scored over the recording
            Zs = zscore_rows(isi_rates(Ms, b))
            sh["sim_all"].append(burst_similarity(Zs, b["peak"], SIM_FRAMES).astype(np.float32))
            del Zs
        del Rbs
    if sh["sim_all"]:
        sh["sim_all"] = np.mean(sh["sim_all"], 0)
    res["shuf"] = sh
    return res


# ---------------------------------------------------------------- recordings of the dandiset

MAIN = ([f"HO{i}" for i in range(1, 9)] + [f"MO{i}" for i in range(1, 10)]
        + ["M1S1", "M1S2", "M2S1", "M2S2", "M3S1", "M3S2"] + [f"Pr{i}" for i in range(1, 9)])
DRUG = {f"MO{i}": ["BASE", "GABAZINE", "NBQXCPP"] for i in range(10, 15)}
LONGITUDINAL = {"HO2": ["6M", "7M", "8M", "8M_4H"], "HO3": ["6M", "7M", "8M", "8M_4H"]}


def recording_table(assets, infos):
    """One row per sorted file: identifier (the source .mat name), path and asset id."""
    import pandas as pd
    ids = {a["path"]: a["asset_id"] for a in assets}
    df = pd.DataFrame(infos)
    df["asset_id"] = df["path"].map(ids)
    df["recording"] = df["identifier"].str.replace("_sorted.mat", "", regex=False)
    return df.sort_values("path").reset_index(drop=True)


# ---------------------------------------------------------------- statistics


class RandomInterceptFit:
    """Result of lmm: fixed effects, their covariance, Wald z and two-sided p."""

    def __init__(self, names, beta, cov, lam, sigma2, n_groups, n_obs):
        import pandas as pd
        self.fe_params = pd.Series(beta, index=names)
        self.params = self.fe_params
        self._cov = pd.DataFrame(cov, index=names, columns=names)
        se = np.sqrt(np.diag(cov))
        self.bse = pd.Series(se, index=names)
        self.tvalues = self.fe_params / self.bse
        self.pvalues = pd.Series(2 * stats.norm.sf(np.abs(self.tvalues.values)), index=names)
        self.group_var = lam * sigma2
        self.resid_var = sigma2
        self.n_groups, self.nobs = n_groups, n_obs

    def cov_params(self):
        return self._cov


def lmm(df, formula, group):
    """Linear mixed-effects model with a random intercept per group, fitted by REML, the model of
    lme4's lmer(y ~ x + (1 | group)) that the paper uses (Methods, "Statistical analyses for model
    comparisons"). The variance ratio is found by maximising the profile REML likelihood over one
    parameter; fixed effects are tested with Wald z tests, where lmerTest uses Satterthwaite t tests
    (a deviation that matters only with few groups)."""
    import patsy
    from scipy.optimize import minimize_scalar
    df = df.replace([np.inf, -np.inf], np.nan).reset_index(drop=True)
    y, X = patsy.dmatrices(formula, df, return_type="dataframe")
    names = list(X.columns)
    g = df.loc[y.index, group].values
    yv, Xv = y.values[:, 0], X.values
    _, gi = np.unique(g, return_inverse=True)
    G = gi.max() + 1
    n_g = np.bincount(gi, minlength=G).astype(float)
    N, p = Xv.shape

    def transform(lam):
        theta = 1 - np.sqrt(1 / (1 + n_g * lam))
        ym = np.bincount(gi, yv, G) / n_g
        Xm = np.vstack([np.bincount(gi, Xv[:, j], G) for j in range(p)]).T / n_g[:, None]
        return yv - theta[gi] * ym[gi], Xv - theta[gi][:, None] * Xm[gi]

    def fit(lam):
        ys, Xs = transform(lam)
        XtX = Xs.T @ Xs
        beta = np.linalg.lstsq(Xs, ys, rcond=None)[0]
        rss = float(((ys - Xs @ beta) ** 2).sum())
        s2 = rss / (N - p)
        sign, logdet = np.linalg.slogdet(XtX)
        ll = -0.5 * ((N - p) * np.log(s2) + np.log(1 + n_g * lam).sum() + logdet)
        return ll, beta, s2, XtX

    res = minimize_scalar(lambda t: -fit(np.exp(t))[0], bounds=(-15, 8), method="bounded")
    lam = np.exp(res.x)
    if fit(0.0)[0] > fit(lam)[0]:
        lam = 0.0
    ll, beta, s2, XtX = fit(lam)
    cov = s2 * np.linalg.pinv(XtX)
    return RandomInterceptFit(names, beta, cov, lam, s2, G, N)


def contrast(fit, weights):
    """Estimate, z and two-sided p of a linear combination of fixed effects (dict name -> weight)."""
    names = fit.fe_params.index
    w = np.array([weights.get(n, 0.0) for n in names])
    est = float(w @ fit.fe_params.values)
    cov = fit.cov_params().loc[names, names].values
    se = float(np.sqrt(w @ cov @ w))
    z = est / se if se > 0 else np.nan
    return dict(estimate=est, se=se, z=z, p=2 * stats.norm.sf(abs(z)))


def cell_means_contrast(fit, a, b):
    """Contrast between two cells of a model fitted with the cell-means formula "0 + C(cell)":
    a minus b, by their names in the fit."""
    return contrast(fit, {f"C(cell)[{a}]": 1.0, f"C(cell)[{b}]": -1.0})
