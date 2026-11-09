"""Loading and measures for CRCNS pfc-2 (Fujisawa, Amarasingham, Harrison and Buzsaki 2008).

Data. The data set is read from the public S3 bucket crcnsarchive, streamed and never
written to disk:

- `pfc-2/live/data/behaviors.zip`: one `<session>_Behavior_PFC.mat` per working memory session
  (12 sessions; EE.188 is not in it). Each holds the spikes of the session's PFC cells
  (`spiket`, 20 kHz samples; `spikeind`, cell number), the normalised position of every spike
  (`spikeX`, -1 outside trials), the trial of every spike within its condition (`spikeLtr`,
  `spikeRtr`), the cells' shank and type (`CellsInfo`), the correct trials (`SessionNP`, in
  seconds: nose-poke start, trial start, trial end, 1 right 2 left) and the position file
  (`whlrld`, 39.0625 Hz: x1, y1, x2, y2, side, trial, linearised position d in [1, 2], one more).
- `pfc-2/live/data/EE0708/EE188_Behavior.mat`: `SessionNP` and `whlrl` of session EE.188.
- `EE188_example.mat`, a member of `pfc-2/live/data/EE0708/EE.188.tar.gz`, the file the data
  description names as the session of the paper's Figures 2a and 3d: 117 cells (the paper's
  117), their types, and the paper's connected pairs (`pairs_all`). The tar is gzip, so it is
  read as a stream (about 2 GB of the 2.4 GB file before the member); the stream also gives
  the list of the tar's members and the nose-poke sensor channels of the session's `.eeg` file.

Parameters and where they come from.

- Kernel: Gaussian, bandwidth 0.05 normalised length (Methods, "Identifying conditional
  differences in firing rates"). Positions are binned at 0.005 before smoothing and the
  statistic is evaluated at the 200 bin centres: a standard discretisation, finer than the
  kernel, that cannot change a result.
- Permutation and global bands: the Methods' stepping procedure, implemented on ranks
  (`global_test`): the global band at level alpha is the smallest pointwise band that holds the
  original and all resampled statistics but a fraction alpha. Number of permutations 1,000
  (the claims file's standard choice).
- Jitter: every spike of each neuron uniform on [-5, +5] ms, 1,000 surrogates, CCG over
  [-5, +5] ms, pointwise and global bands at 99 %, global band from the maximum and minimum of
  each surrogate; connection when the counts break the global band in [1, 4] ms (Methods,
  "Identifying monosynaptic interactions"). The Methods define a band's global acceptance level
  as "the proportion of the original and the resampled data sets i that lie completely within
  the pointwise bands", and the global band at level a as "the minimal pointwise band with global
  acceptance level a", found by "a stepping procedure" ("Multiple hypothesis testing and global
  bands"). So the band is stepped inwards, excluding the k largest maxima and the k smallest
  minima of the surrogates, for as long as at least 99 % of the surrogates lie entirely within
  both sides (G-b, the reading used). The 99th percentile of the maxima and the 1st percentile of
  the minima (1 % on each side, G-a) is run as a variant. Bin width 1 ms (B-a) or 0.5 ms (B-b),
  lag rounded to the nearest bin centre (claims file, shared method).
- Coincidences: 1 <= tdiff <= 4 ms, placed at the presynaptic spike's position, smoothed with
  the same kernel, divided by the number of trials; one-sided bands for excess (Methods,
  "Identifying position dependence"). The position of a jittered event is that of the original
  presynaptic spike: the jitter moves it by at most 5 ms, under 0.005 of the maze at running
  speed, a standard choice that cannot change a result.
"""
import io
import tarfile
import zipfile

import fsspec
import numpy as np
import scipy.io as sio
from numba import njit

DATASET = "crcns:pfc-2/unversioned"  # CRCNS data sets are not versioned (docs/archives.md)
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-2/live/data/"
FS = 20000.0
WHL_RATE = 39.0625
NGRID = 200
GRID = (np.arange(NGRID) + 0.5) / NGRID
SIGMA = 0.05

# Rat to layer, from Supplementary Figure 1 (rats E and G layer 2/3, rat F layer 5; rat H, layer
# 2/3, is not in the data set). The data set's rats EE, FF and GG are taken to be the paper's E, F
# and G: an assumption, stated in the notebook.
LAYER = {"EE": "L2/3", "FF": "L5", "GG": "L2/3"}


def _mat(b):
    return {k: v for k, v in sio.loadmat(io.BytesIO(b)).items() if not k.startswith("__")}


def read_raw():
    """Stream the files the analysis uses; returns {name: bytes}."""
    raw = {}
    with fsspec.open(BASE + "behaviors.zip", block_size=2**20) as f:
        z = zipfile.ZipFile(f)
        for info in z.infolist():
            if info.filename.endswith("_Behavior_PFC.mat"):
                raw[info.filename.split("/")[-1]] = z.read(info.filename)
    for name in ["EE0708/EE188_Behavior.mat", "EE0708/EE188_Behavior_PFC.mat"]:
        with fsspec.open(BASE + name, block_size=2**22) as f:
            raw[name.split("/")[-1]] = f.read()
    # Every member of the session's tar is listed (name, size), to show what the session holds.
    # From the 1,250 Hz .eeg file only channels 97 and 98 are kept: the optic sensors of the
    # nose-poke, right and left trials, of the 104 channels of rat EE (data description, page 1).
    members = []
    with fsspec.open(BASE + "EE0708/EE.188.tar.gz", block_size=2**24) as f:
        t = tarfile.open(fileobj=f, mode="r|gz")
        for m in t:
            members.append((m.name, m.size))
            if m.name.endswith("EE188_example.mat"):
                raw["EE188_example.mat"] = t.extractfile(m).read()
            elif m.name.endswith(".eeg"):
                fe, parts = t.extractfile(m), []
                while b := fe.read(208 * 100000):
                    parts.append(np.frombuffer(b, np.int16).reshape(-1, 104)[:, 96:98].copy())
                raw["EE188 nose-poke sensors"] = np.concatenate(parts)
    return raw, members


def poke_intervals(v, rate=1250.0, thr=-15000):
    """Intervals (s) when a nose-poke sensor channel is low (the sensor's beam broken). The
    channels sit near 0 and drop to about -30,000 during a poke; the threshold halfway is a
    standard choice (the trial table's nose-poke times are matched to within a sample)."""
    on = v < thr
    d = np.diff(on.astype(int), prepend=0, append=0)
    return np.c_[np.flatnonzero(d == 1), np.flatnonzero(d == -1)] / rate


class Session:
    """One working memory session: PFC cells, spikes, trials and position."""

    def __init__(self, name, m, beh=None):
        self.name = name
        self.rat = name[:2]
        self.layer = LAYER[self.rat]
        beh = m if beh is None else beh
        self.NP = np.asarray(beh["SessionNP"], float)
        self.whl = np.asarray(beh["whlrld"] if "whlrld" in beh else beh["whlrl"], float)
        ci = np.asarray(m["CellsInfo"], int)
        self.cells = ci[:, 0]
        self.shank = ci[:, 1]
        self.celltype_file = ci[:, 2]
        idx = {c: i for i, c in enumerate(self.cells)}
        si = np.asarray(m["spikeind"], int).ravel()
        keep = np.isin(si, self.cells)
        self.n_spikes_not_in_cells = int((~keep).sum())
        self.t = np.asarray(m["spiket"], float).ravel()[keep] / FS
        self.u = np.array([idx[c] for c in si[keep]])
        self.x = np.asarray(m["spikeX"], float).ravel()[keep]
        ltr = np.asarray(m["spikeLtr"], int).ravel()[keep]
        rtr = np.asarray(m["spikeRtr"], int).ravel()[keep]
        side = self.NP[:, 3].astype(int)
        self.left = side == 2
        # trial index (row of SessionNP) of every spike; -1 outside trials
        lrows = np.flatnonzero(side == 2)
        rrows = np.flatnonzero(side == 1)
        tr = np.full(len(self.t), -1)
        tr[ltr > 0] = lrows[ltr[ltr > 0] - 1]
        tr[rtr > 0] = rrows[rtr[rtr > 0] - 1]
        self.trial = tr
        self.max_ltr, self.max_rtr = int(ltr.max()), int(rtr.max())
        o = np.argsort(self.t, kind="stable")
        for a in ("t", "u", "x", "trial"):
            setattr(self, a, getattr(self, a)[o])
        # The spikes' trial labels and positions run from the first nose-poke of a trial; the
        # trial proper runs from the end of the nose-poke ("trial start time" in the paper) to the
        # start of reward consumption (data description, page 2, SessionNP). Only spikes within
        # the trial proper are placed on the maze.
        k = np.maximum(self.trial, 0)
        self.intrial = (self.trial >= 0) & (self.t >= self.NP[k, 1]) & (self.t <= self.NP[k, 2])
        self.n = len(self.cells)
        self.ntrials = len(self.NP)
        self.duration = self.whl.shape[0] / WHL_RATE

    def spikes_of(self, i):
        return self.t[self.u == i]

    def trial_hist(self, i, mask=None):
        """Per-trial histogram (trials x NGRID) of cell i's spike positions."""
        s = (self.u == i) & self.intrial
        if mask is not None:
            s &= mask
        b = np.minimum((self.x[s] * NGRID).astype(int), NGRID - 1)
        h = np.zeros((self.ntrials, NGRID))
        np.add.at(h, (self.trial[s], b), 1.0)
        return h


def load_sessions(raw):
    out = {}
    for k in sorted(raw):
        if k.endswith("_Behavior_PFC.mat") and k != "EE188_Behavior_PFC.mat":
            name = k.split("_")[0]
            out[name] = Session(name, _mat(raw[k]))
    out["EE188"] = Session("EE188", _mat(raw["EE188_example.mat"]), _mat(raw["EE188_Behavior.mat"]))
    return dict(sorted(out.items()))


# ---------------------------------------------------------------- smoothing and resampling tests

def _kernel():
    k = np.arange(-60, 61) / NGRID
    g = np.exp(-0.5 * (k / SIGMA) ** 2)
    return g / g.sum() * NGRID  # density per unit normalised length


KERNEL = _kernel()


def smooth(h):
    """Gaussian smoothing along the last axis (sum of kernels at the spike positions)."""
    from scipy.ndimage import convolve1d
    return convolve1d(h, KERNEL, axis=-1, mode="constant")


def global_test(D, alpha, sided="two"):
    """Pointwise and global significance of D[0] against D[1:] (Methods, stepping procedure).

    Returns (pointwise boolean array, global boolean array, global p). The pointwise P-values are
    the Methods' P+, P- and P+- = min(1, 2P+, 2P-), counted over j = 0..M. The global band is the
    smallest pointwise band (a band is indexed by the extremeness rank it admits) containing a
    fraction 1 - alpha of the M + 1 statistics; D[0] breaks it where its rank exceeds that band.
    """
    M1 = D.shape[0]
    # rank of each D_j(x) among the M+1 values: ge = #(D_k >= D_j), le = #(D_k <= D_j)
    srt = np.sort(D, axis=0)
    le = np.empty_like(D, dtype=np.int64)
    ge = np.empty_like(D, dtype=np.int64)
    for x in range(D.shape[1]):
        le[:, x] = np.searchsorted(srt[:, x], D[:, x], side="right")
        ge[:, x] = M1 - np.searchsorted(srt[:, x], D[:, x], side="left")
    if sided == "two":
        p = np.minimum(1.0, 2.0 * np.minimum(ge, le) / M1)
    else:  # one-sided, excess
        p = ge / M1
    point = p[0] <= alpha
    pmin = p.min(axis=1)  # the most extreme point of each statistic
    # Ties at the smallest attainable pointwise P (1/(M+1)) are broken by the standardised
    # excess at that point, as the bands' values beyond the last order statistic would be: a
    # standard way to resolve the discreteness of the ranks, which the Methods do not discuss.
    sd = D[1:].std(axis=0)
    sd[sd == 0] = np.inf
    z = (D - D[1:].mean(axis=0)) / sd
    if sided == "two":
        z = np.abs(z)
    zmax = np.where(p == pmin[:, None], z, -np.inf).max(axis=1)
    # global p of the original: fraction of statistics at least as extreme as the original
    worse = (pmin < pmin[0]) | ((pmin == pmin[0]) & (zmax >= zmax[0]))
    gp = np.mean(worse)
    # global band: D[0] breaks it at the points more extreme than the (1 - alpha) quantile of
    # the other statistics' extremes
    glob = np.zeros(D.shape[1], bool)
    if gp <= alpha:
        order = np.lexsort((-zmax, pmin))  # most extreme first
        k = max(int(np.floor(alpha * M1)) - 1, 0)
        cp, cz = pmin[order[k]], zmax[order[k]]
        glob = (p[0] < cp) | ((p[0] == cp) & (z[0] >= cz))
    return point, glob, gp


def segments(point, glob):
    """Contiguous pointwise-significant runs that contain a global break: list of (i0, i1)."""
    segs = []
    i = 0
    n = len(point)
    while i < n:
        if point[i]:
            j = i
            while j + 1 < n and point[j + 1]:
                j += 1
            if glob[i:j + 1].any():
                segs.append((i, j))
            i = j + 1
        else:
            i += 1
    return segs


def lr_test(H, labels, rng, M=1000, alpha=0.05):
    """Permutation test of the left minus right PSTH difference (Methods).

    H: smoothed per-trial PSTHs (trials x NGRID); labels: True for LEFT.
    Returns D0, pointwise, global, global p.
    """
    labels = np.asarray(labels, bool)
    nl = labels.sum()
    nr = len(labels) - nl
    P = np.empty((M + 1, len(labels)), bool)
    P[0] = labels
    for j in range(1, M + 1):
        P[j] = rng.permutation(labels)
    W = P / nl - (~P) / nr
    D = W @ H
    point, glob, gp = global_test(D, alpha, "two")
    return D[0], point, glob, gp


# ---------------------------------------------------------------- cross-correlograms with jitter

@njit(cache=True)
def _ccg_all(t, u, n, maxlag, bw, K):
    """Counts[i, j, k]: spikes of j at lag (k - K) * bw (nearest bin) after spikes of i."""
    c = np.zeros((n, n, 2 * K + 1), np.uint16)
    N = len(t)
    for a in range(N):
        b = a + 1
        while b < N and t[b] - t[a] <= maxlag:
            d = t[b] - t[a]
            k = int(np.floor(d / bw + 0.5))
            if k <= K:
                c[u[a], u[b], K + k] += 1
                c[u[b], u[a], K - k] += 1
            b += 1
    return c


def ccg_jitter(t, u, n, rng, bw, nsur=1000, maxlag=0.005, jit=0.005):
    """Observed CCG counts (n x n x bins) and jitter surrogates (nsur x n x n x bins, uint16)."""
    K = int(round(maxlag / bw))
    lim = (K + 0.5) * bw
    obs = _ccg_all(t, u, n, lim, bw, K)
    sur = np.empty((nsur,) + obs.shape, np.uint16)
    for j in range(nsur):
        tj = t + rng.uniform(-jit, jit, len(t))
        o = np.argsort(tj, kind="stable")
        sur[j] = _ccg_all(tj[o], u[o], n, lim, bw, K)
    return obs, sur


def detect_connections(obs, sur, bw, level=0.01, gside="step"):
    """Excitatory and inhibitory connections from the jitter bands.

    Returns dict of boolean n x n arrays (ref i -> target j): exc, inh (global band broken in
    [1, 4] ms), and the width in ms of the run of bins around the largest [1, 4] ms excess that
    break the pointwise 99 % band (for the 2 ms width reading W-b). gside: "step" for
    the Methods' stepping procedure (G-b): the band excludes the k largest surrogate maxima and
    the k smallest minima, with k the largest for which a fraction 1 - level of the surrogates lie
    entirely within both sides; or a number, the fraction of surrogate maxima (minima) above
    (below) the band on each side (0.01 for G-a). Also returns `joint`, the fraction of
    surrogates lying entirely within both global bands.
    """
    n = obs.shape[0]
    nb = obs.shape[2]
    K = nb // 2
    lags = (np.arange(nb) - K) * bw * 1000
    win = (lags >= 1 - 1e-9) & (lags <= 4 + 1e-9)
    gmax = sur.max(axis=3)
    gmin = sur.min(axis=3)
    if gside == "step":
        M = sur.shape[0]
        smax = np.sort(gmax, axis=0)
        smin = np.sort(gmin, axis=0)
        gup, gdn = smax[-1], smin[0]
        for k in range(1, int(level * M) + 1):
            up_k, dn_k = smax[M - 1 - k], smin[k]
            ok = ((gmax <= up_k) & (gmin >= dn_k)).mean(axis=0) >= 1 - level
            gup = np.where(ok, up_k, gup)
            gdn = np.where(ok, dn_k, gdn)
    else:
        gup = np.quantile(gmax, 1 - gside, axis=0)
        gdn = np.quantile(gmin, gside, axis=0)
    pup = np.quantile(sur, 1 - level / 2, axis=0)
    pdn = np.quantile(sur, level / 2, axis=0)
    o = obs.astype(float)
    exc = (o[:, :, win] > gup[:, :, None]).any(axis=2)
    inh = (o[:, :, win] < gdn[:, :, None]).any(axis=2)
    np.fill_diagonal(exc, False)
    np.fill_diagonal(inh, False)
    # width of the pointwise excess (peak) or deficit (trough) run that contains the extreme bin
    width = np.full((n, n), np.nan)
    wi = np.flatnonzero(win)
    for i, j in zip(*np.nonzero(exc | inh)):
        if exc[i, j]:
            above = o[i, j] > pup[i, j]
            k = wi[np.argmax(o[i, j, wi] - pup[i, j, wi])]
        else:
            above = o[i, j] < pdn[i, j]
            k = wi[np.argmax(pdn[i, j, wi] - o[i, j, wi])]
        a = b = k
        while a - 1 >= 0 and above[a - 1]:
            a -= 1
        while b + 1 < nb and above[b + 1]:
            b += 1
        width[i, j] = (b - a + 1) * bw * 1000 if above[k] else 0.0
    mean = sur.mean(axis=0)
    sd = sur.std(axis=0)
    joint = ((gmax <= gup[None]) & (gmin >= gdn[None])).mean(axis=0)
    return {"exc": exc, "inh": inh, "width": width, "mean": mean, "sd": sd, "lags": lags, "win": win,
            "joint": joint}


# ---------------------------------------------------------------- coincidences along the maze

@njit(cache=True)
def _coinc(tpre, tpost, lo, hi):
    """Index of every presynaptic spike for each coincident event lo <= tpost - tpre <= hi."""
    out = []
    j0 = 0
    for a in range(len(tpre)):
        while j0 < len(tpost) and tpost[j0] < tpre[a] + lo:
            j0 += 1
        j = j0
        while j < len(tpost) and tpost[j] <= tpre[a] + hi:
            out.append(a)
            j += 1
    return np.array(out, np.int64)


def pair_spikes(s, i, j, trials_mask=None):
    """Spikes of pre i and post j near the chosen trials, for the coincidence test."""
    if trials_mask is None:
        trials_mask = np.ones(s.ntrials, bool)
    # spikes of the two cells within the chosen trials, widened by 20 ms for the jitter
    win = s.NP[trials_mask][:, 1:3]

    def near(t):
        k = np.searchsorted(win[:, 0] - 0.02, t, side="right") - 1
        return (k >= 0) & (t <= win[np.maximum(k, 0), 1] + 0.02)
    mi = s.u == i
    tpre, xpre, trpre = s.t[mi], s.x[mi], s.trial[mi]
    ok = near(tpre)
    tpre, xpre, trpre = tpre[ok], xpre[ok], trpre[ok]
    inpre = s.intrial[mi][ok].copy()
    inpre[inpre] = trials_mask[trpre[inpre]]
    mj = s.u == j
    tpost = s.t[mj]
    okj = near(tpost)
    return {"tpre": tpre, "xpre": xpre, "inpre": inpre, "tpost": tpost[okj], "xpost": s.x[mj][okj],
            "inpost": s.intrial[mj][okj] & trials_mask[np.maximum(s.trial[mj][okj], 0)],
            "N": int(trials_mask.sum())}


def coincidence_test(s, i, j, rng, nsur=1000, alpha=0.01, trials_mask=None, jitter_post=True, ps=None):
    """Position of excess coincidences between pre i and post j (Methods).

    trials_mask: boolean over trials, which trials enter (left, right or all). ps: spikes from
    pair_spikes (possibly thinned). Returns S0 (coincidence rate on GRID), mean surrogate rate,
    pointwise, global, global p.
    """
    if ps is None:
        ps = pair_spikes(s, i, j, trials_mask)
    tpre, xpre, inpre, tpost = ps["tpre"], ps["xpre"], ps["inpre"], ps["tpost"]
    lo, hi = 0.001, 0.004
    D = np.empty((nsur + 1, NGRID))
    for k in range(nsur + 1):
        if k == 0:
            a, b = tpre, tpost
            order = np.arange(len(a))
        else:
            a = tpre + rng.uniform(-0.005, 0.005, len(tpre))
            b = tpost + rng.uniform(-0.005, 0.005, len(tpost)) if jitter_post else tpost
            order = np.argsort(a, kind="stable")
            a = a[order]
            b = np.sort(b)
        ev = order[_coinc(a, b, lo, hi)]
        ev = ev[inpre[ev]]
        h = np.bincount(np.minimum((xpre[ev] * NGRID).astype(int), NGRID - 1), minlength=NGRID)
        D[k] = h
    D = smooth(D) / ps["N"]
    point, glob, gp = global_test(D, alpha, "one")
    return D[0], D[1:].mean(axis=0), point, glob, gp


def thin(t, x, keep_mask, lo, hi, rng):
    """Thinning (Methods, "Controlling for power"): spikes in the trials are removed one at a time,
    chosen at random within [-s, +s] of the PSTH maximum in the region [lo, hi], until the PSTH
    minimum in the region is within 10% of its maximum. The loop also stops when no spike is left
    within [-s, +s] of the maximum, before the target is met. Returns the kept spikes (boolean)
    and the ratio of the PSTH minimum to its maximum in the region at the end (0.9 or more when
    the target was met)."""
    keep = keep_mask.copy()
    reg = (GRID >= lo) & (GRID <= hi)
    b = np.minimum((x * NGRID).astype(int), NGRID - 1)
    h = np.bincount(b[keep], minlength=NGRID).astype(float)
    P = smooth(h[None])[0]
    kern = smooth(np.eye(NGRID))  # row k: kernel centred at bin k
    while True:
        pr = P[reg]
        if pr.max() <= 0 or pr.min() >= 0.9 * pr.max():
            break
        xm = GRID[reg][pr.argmax()]
        cand = np.flatnonzero(keep & (np.abs(x - xm) <= SIGMA))
        if len(cand) == 0:
            break
        k = rng.choice(cand)
        keep[k] = False
        P -= kern[b[k]]
    pr = np.clip(P[reg], 0, None)  # the running subtraction can leave rounding errors below 0
    return keep, (pr.min() / pr.max() if pr.max() > 0 else np.nan)


# ---------------------------------------------------------------- spike transmission by spike order

def train_labels(t, silence=0.2, within=0.04, chained=True):
    """First spikes (preceded by at least 200 ms without spikes) and later spikes (within 40 ms of
    the previous spike) of a train (Results; Figure 6b legend). chained: a later spike must belong
    to a train begun by a first spike (reading x), otherwise any spike within 40 ms (reading y)."""
    isi = np.diff(t, prepend=-np.inf)
    first = isi >= silence
    later = isi <= within
    if chained:
        ok = np.zeros(len(t), bool)
        cur = False
        for k in range(len(t)):
            if first[k]:
                cur = True
            elif not later[k]:
                cur = False
            ok[k] = cur and later[k]
        later = ok
    return first, later


@njit(cache=True)
def _lag_counts(tpre, tpost, edges):
    """Counts of post spikes per lag bin (edges, seconds) after each pre spike."""
    nb = len(edges) - 1
    out = np.zeros((len(tpre), nb), np.uint8)
    j0 = 0
    for a in range(len(tpre)):
        while j0 < len(tpost) and tpost[j0] < tpre[a] + edges[0]:
            j0 += 1
        j = j0
        while j < len(tpost) and tpost[j] < tpre[a] + edges[nb]:
            k = 0
            while tpost[j] - tpre[a] >= edges[k + 1]:
                k += 1
            out[a, k] += 1
            j += 1
    return out


def order_effect(tpre, tpost, first, later, rng, how, nsur=200, nperm=1000):
    """Standardised peak height (h - jitter mean) / jitter s.d. (Supplementary Figure 9B) for first
    and later presynaptic spikes, their difference, and its two-sided permutation P (labels shuffled
    between the two groups; Figure 6c legend, Supplementary Figure 16). how: 'i' largest 1 ms bin in
    [1, 4] ms, 'ii' sum over [1, 4] ms. Surrogates jitter every spike of both cells on [-5, +5] ms.

    The standardised heights grow with the square root of the number of spikes, so with groups of
    different sizes the permutation distribution of the difference is not centred on 0. The P-value
    is therefore taken from the two tails of that distribution, as the Methods define a two-sided
    permutation P (P+- = min(1, 2P+, 2P-), counted over j = 0..M): the original difference above
    the permuted ones (P+ small) means the first spikes are more effective than under shuffled
    labels (depression), below them (P- small) facilitation. Returns z first, z later, difference,
    P, n first, n later, side (+1 when P+ < P-, else -1) and the mean permuted difference."""
    edges = np.array([0.0005, 0.0015, 0.0025, 0.0035, 0.0045])
    sel = first | later
    tp = tpre[sel]
    grp = first[sel]
    C = np.empty((nsur + 1, len(tp), 4), np.float32)
    C[0] = _lag_counts(tp, tpost, edges)
    for j in range(1, nsur + 1):
        a = tp + rng.uniform(-0.005, 0.005, len(tp))
        b = np.sort(tpost + rng.uniform(-0.005, 0.005, len(tpost)))
        o = np.argsort(a)
        c = np.empty((len(tp), 4), np.uint8)
        c[o] = _lag_counts(a[o], b, edges)
        C[j] = c
    nz = C.reshape(nsur + 1, len(tp), 4).sum(axis=(0, 2)) > 0
    Cn = C[:, nz].transpose(1, 0, 2).reshape(nz.sum(), -1)  # spikes x (sur*4)
    g = grp[nz]
    masks = np.empty((nperm + 1, nz.sum()), np.float32)
    masks[0] = g
    for p in range(1, nperm + 1):
        masks[p] = rng.permutation(g)
    tot = Cn.sum(axis=0)
    SF = (masks @ Cn).reshape(nperm + 1, nsur + 1, 4)
    SL = (tot[None] - masks @ Cn).reshape(nperm + 1, nsur + 1, 4)

    def z(Sx):
        h = Sx.max(axis=2) if how == "i" else Sx.sum(axis=2)
        mu, sd = h[:, 1:].mean(axis=1), h[:, 1:].std(axis=1)
        return (h[:, 0] - mu) / np.where(sd > 0, sd, np.nan)
    zf, zl = z(SF), z(SL)
    d = zf - zl
    if not np.isfinite(d[0]):
        return zf[0], zl[0], d[0], np.nan, int(grp.sum()), int((~grp).sum()), 0, np.nan
    dd = d[np.isfinite(d)]
    pp = np.mean(dd >= d[0] - 1e-12)
    pm = np.mean(dd <= d[0] + 1e-12)
    p = min(1.0, 2 * pp, 2 * pm)
    return (zf[0], zl[0], d[0], p, int(grp.sum()), int((~grp).sum()), (1 if pp < pm else -1),
            float(dd[1:].mean()))
