"""Loading and measures for Fujisawa, Amarasingham, Harrison & Buzsaki (2008), Nat Neurosci 11:823.

Data come from two archives, both streamed (nothing is written to disk):

- DANDI:000067, pinned at DANDI_VERSION. Spike times, shank and cluster of every unit, the raw
  wideband signal (for the channel map check) and the head LED positions are read from the NWB
  files with remfile and h5py.
- CRCNS pfc-2 (doi:10.6080/K01V5BWK, unversioned; MD5 sums in CRCNS_MD5). The lab's summary
  files: SessionNP (correct trials: first poke start, last poke end = trial start, reward start =
  trial end, side R=1 L=2), the extended whl file (linearised position d in 1..2 at 39.0625 Hz),
  spikeph (unit -> shank, cluster), CellsInfo (the units of each session and the lab's cell
  type), and EE188_example.mat (the 117 cells of the paper's Figure 2a / 3 session and the lab's
  list of connections, pairs_all). The example file is read from inside EE.188.tar.gz by
  streaming the archive (about 80 s).

Where each parameter comes from is said where it is defined:
  [claims]   the claim's criterion or the claims file's shared method, which cite the paper;
  [paper]    a passage of the paper, cited (author step 1.6);
  [assumed]  an assumption, with the reason;
  [standard] a standard choice for a detail that cannot change a result.
"""
import io
import tarfile
import warnings
import zipfile

import h5py
import numpy as np
import remfile
import requests
import fsspec
import scipy.io as sio
from numba import njit

DANDI_ID = "000067"
DANDI_VERSION = "0.261106.2004"
CRCNS = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-2/live/"
CRCNS_MD5 = {
    "data/behaviors.zip": "3a510fe0ef8a24ed4248d37bed3fd624",
    "data/EE0708/EE188_Behavior.mat": "b7407ba84d282c33cf937f090f2ebb0c",
    "data/EE0708/EE188_Behavior_PFC.mat": "a3ca6359c45e2a8deeada4b8eb1d61c6",
    "data/EE0711/EE210_Behavior.mat": "5cb9abf19e143fd60d1f506a84e1989b",
    "data/EE0711/EE210_Behavior_PFC.mat": "38b6450c96410d38348cb7c4b66591b2",
    "data/EE0708/EE.188.tar.gz": "115236aeb0b9890b4dd0a26fbabe0ed3",
}
# Working memory sessions (CRCNS description, table of sessions). GG.063 is the spontaneous
# alternation task and is left out.
SESSIONS = ["EE049", "EE088", "EE152", "EE165", "EE188", "EE196", "EE210",
            "FF103", "FF130", "FF167", "GG069", "GG097", "GG149"]
FS = 20000.0          # spike time stamps, 20 kHz (CRCNS description)
WHL_RATE = 39.0625    # whl frames per second (CRCNS description, 20 kHz / 512)
LENGTH_CM = 230.0     # [paper] Results, "total length, 230 cm"
SIGMA = 0.05          # [paper] Methods, gaussian kernels of bandwidth 0.05 normalised length
GRID = np.linspace(0, 1, 101)  # [standard] evaluation points of D0(x), as the claims file says

_assets = None


def dandi_assets():
    global _assets
    if _assets is None:
        url = f"https://api.dandiarchive.org/api/dandisets/{DANDI_ID}/versions/{DANDI_VERSION}/assets/?page_size=200"
        _assets = {a["path"]: a for a in requests.get(url, timeout=60).json()["results"]}
    return _assets


def nwb_path(session):
    rat, num = session[:2], session[2:]
    for p in dandi_assets():
        if p.startswith(f"sub-{rat}/sub-{rat}_ses-{rat}-{num}_"):
            return p
    raise KeyError(session)


def open_nwb(session):
    a = dandi_assets()[nwb_path(session)]
    url = f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
    s3 = requests.head(url, allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(s3), "r")


def read_nwb_units(f):
    """Every unit of an NWB file: spike times (s), shank, cluster, region, cell type, lab number."""
    U = f["units"]
    idx = U["spike_times_index"][:]
    st = U["spike_times"][:]
    starts = np.r_[0, idx[:-1]]
    dec = lambda d: np.array([x.decode() if isinstance(x, bytes) else x for x in d[:]])
    return dict(times=[st[a:b] for a, b in zip(starts, idx)], shank=U["shank"][:],
                cluster=U["cluster_id"][:], region=dec(U["region"]), cell_type=dec(U["cell_type"]),
                lab=U["lab_cell_number"][:])


def read_nwb_trials(f):
    if "intervals/trials" not in f:
        return None
    T = f["intervals/trials"]
    side = np.array([x.decode() for x in T["side"][:]])
    return dict(start=T["start_time"][:], stop=T["stop_time"][:], poke=T["nose_poke_start_time"][:],
                side=side)


def read_nwb_leds(f):
    P = f["processing/behavior/Position"]
    return [P[k]["data"][:] for k in sorted(P.keys())]


def load_crcns():
    """The lab's summary .mat files of every working memory session, in memory."""
    out = {}
    with fsspec.open(CRCNS + "data/behaviors.zip", block_size=2**20).open() as fh:
        z = zipfile.ZipFile(fh)
        for n in z.namelist():
            if n.endswith("_Behavior_PFC.mat"):
                out[n.split("/")[-1][:5]] = sio.loadmat(io.BytesIO(z.read(n)))
    # EE188 is not in behaviors.zip; its files are in its folder (SessionNP and whl in
    # EE188_Behavior.mat, the PFC cells in EE188_Behavior_PFC.mat).
    b = sio.loadmat(io.BytesIO(fsspec.open(CRCNS + "data/EE0708/EE188_Behavior.mat").open().read()))
    p = sio.loadmat(io.BytesIO(fsspec.open(CRCNS + "data/EE0708/EE188_Behavior_PFC.mat").open().read()))
    p["SessionNP"] = b["SessionNP"]
    w = b["whlrl"]
    p["whlrld"] = np.c_[w, np.zeros(len(w))]
    p["spikeph_all"] = b["spikeph"]
    out["EE188"] = p
    # EE210 is both in behaviors.zip and in its folder; the folder copy is compared in the notebook.
    out["_EE210_folder"] = sio.loadmat(io.BytesIO(fsspec.open(CRCNS + "data/EE0711/EE210_Behavior_PFC.mat").open().read()))
    return out


def load_example():
    """EE188_example.mat, read from inside EE.188.tar.gz by streaming the archive."""
    with fsspec.open(CRCNS + "data/EE0708/EE.188.tar.gz", block_size=2**23).open() as fh:
        tf = tarfile.open(fileobj=fh, mode="r|gz")
        for m in tf:
            if m.name.endswith("EE188_example.mat"):
                return sio.loadmat(io.BytesIO(tf.extractfile(m).read()))
    raise FileNotFoundError("EE188_example.mat")


class Session:
    """One working memory session: units (CRCNS cell numbers) with NWB spike times, trials, positions."""

    def __init__(self, name, mat, nwb_units, leds, example=None):
        self.name, self.rat = name, name[:2]
        sp = mat.get("spikeph_all", mat["spikeph"])
        if example is not None:
            cells = example["CellsInfo"]          # the 117 cells of the paper's Figure 2a session
        else:
            cells = mat["CellsInfo"]
        self.cells = cells[:, 0].astype(int)
        self.lab_type = cells[:, 2].astype(int)   # lab's CellsInfo code: 1 pyr, 2 int, 3 unknown
        key = {(int(s), int(c)): i for i, (s, c) in enumerate(zip(nwb_units["shank"], nwb_units["cluster"]))}
        self.shank, self.times, self.nwb_index = [], [], []
        si = mat["spikeind"].ravel()
        st = mat["spiket"].ravel() / FS
        self.n_identical = 0
        for c in self.cells:
            r = sp[sp[:, 0] == c][0]
            i = key[(int(r[1]), int(r[2]))]
            t = np.asarray(nwb_units["times"][i], float)
            self.times.append(t)
            self.shank.append(int(r[1]))
            self.nwb_index.append(i)
            if example is None or c in set(mat["CellsInfo"][:, 0]):
                ref = st[si == c]
                self.n_identical += int(len(ref) == len(t) and np.allclose(ref, t, atol=1e-4))
        self.shank = np.array(self.shank)
        npk = mat["SessionNP"]
        self.poke_start, self.start, self.stop = npk[:, 0], npk[:, 1], npk[:, 2]
        self.side = np.where(npk[:, 3] == 2, "L", "R")   # R = 1, L = 2 (CRCNS description)
        w = mat["whlrld"]
        self.whl = w
        self.whl_t = np.arange(len(w)) / WHL_RATE
        self.d = w[:, 6]
        self.leds = leds
        self.duration = max(t.max() if len(t) else 0 for t in self.times)

    @property
    def n_trials(self):
        return len(self.start)

    def trial_of(self, t):
        """Index of the trial holding each time (start <= t <= stop), -1 outside trials."""
        k = np.searchsorted(self.start, t, side="right") - 1
        ok = (k >= 0) & (t <= self.stop[np.clip(k, 0, None)])
        return np.where(ok, k, -1)

    def position(self, t):
        """Normalised position (d - 1) at times t, interpolated from the whl file; NaN outside trials."""
        # interpolate over tracked frames only (d > 0); frames with d = 0 inside a trial are
        # untracked moments [standard]
        v = self.d > 0
        x = np.interp(t, self.whl_t[v], self.d[v]) - 1.0
        k = self.trial_of(t)
        x[(k < 0)] = np.nan
        return np.clip(x, 0, 1)

    def spikes_in_trials(self, u):
        t = self.times[u]
        k = self.trial_of(t)
        m = k >= 0
        return t[m], k[m], self.position(t[m])


# ---------------------------------------------------------------- PSTH and permutation bands

def kernel_matrix(x, grid=GRID, sigma=SIGMA):
    """Gaussian kernel density contributions of points x at the grid (rows: points)."""
    x = np.asarray(x)[:, None]
    return np.exp(-0.5 * ((grid[None, :] - x) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))


def trial_psth(sess, u):
    """Per trial PSTH (spikes per unit normalised length), trials x grid [paper, Methods]."""
    return trial_psth_times(sess, sess.times[u])


def trial_psth_times(sess, t):
    """trial_psth for any spike train t (s) of the session, such as an NWB unit the lab's list leaves out."""
    t = np.asarray(t, float)
    k = sess.trial_of(t)
    m = k >= 0
    t, k = t[m], k[m]
    P = np.zeros((sess.n_trials, len(GRID)))
    if len(t):
        np.add.at(P, k, kernel_matrix(sess.position(t)))
    return P


def max_trial_rate(P, O, side):
    """Largest occupancy-normalised rate (Hz) over the grid, of the left or the right trials,
    whichever is higher (P trial PSTHs, O occupancy, side 'L'/'R' per trial)."""
    out = 0.0
    for m in (side == "L", side == "R"):
        o = O[m].sum(0)
        with np.errstate(invalid="ignore", divide="ignore"):
            r = np.where(o > 0, P[m].sum(0) / o, 0.0)
        out = max(out, float(r.max()))
    return out


def occupancy(sess):
    """Seconds per unit normalised length per trial (trials x grid), from whl frames in trials."""
    k = sess.trial_of(sess.whl_t)
    m = (k >= 0) & (sess.d > 0)
    x = np.clip(sess.d[m] - 1, 0, 1)
    O = np.zeros((sess.n_trials, len(GRID)))
    np.add.at(O, k[m], kernel_matrix(x) / WHL_RATE)
    return O


def perm_bands(P, labels, M=1000, alpha=0.05, rng=None, two_sided=True):
    """The Methods' permutation test of D0 = mean(P[L]) - mean(P[R]) with pointwise and global bands.

    labels: boolean array, True for the first condition (LEFT). M permutations [claims: M not given,
    1,000 a standard choice]. Returns D0, a boolean array of pointwise breaks (sign +1/-1/0), the
    significant segments (runs of pointwise breaks holding a global break, Figure 1c legend) and the
    global flag."""
    rng = rng or np.random.default_rng(0)
    labels = np.asarray(labels, bool)
    nL, n = labels.sum(), len(labels)
    W = np.empty((M + 1, n))
    W[0] = np.where(labels, 1 / nL, -1 / (n - nL))
    for j in range(1, M + 1):
        lj = rng.permutation(labels)
        W[j] = np.where(lj, 1 / nL, -1 / (n - nL))
    D = W @ P
    return bands_from_curves(D, alpha, two_sided)


def bands_from_curves(D, alpha, two_sided=True):
    """D: (M+1) x grid, row 0 the data. Pointwise and global (stepping) bands as in the Methods."""
    S = np.sort(D, axis=0)
    Mp1 = D.shape[0]
    le = np.empty_like(D, dtype=np.int64)
    ge = np.empty_like(D, dtype=np.int64)
    for x in range(D.shape[1]):
        le[:, x] = np.searchsorted(S[:, x], D[:, x], side="right")    # count(S <= D)
        ge[:, x] = Mp1 - np.searchsorted(S[:, x], D[:, x], side="left")  # count(S >= D)
    if two_sided:
        edge = np.minimum(le, ge)
        pw_thr = alpha / 2 * Mp1
    else:
        edge = ge
        pw_thr = alpha * Mp1
    e = edge.min(axis=1)                      # each curve: its most extreme rank over positions
    ks = np.arange(0, Mp1)
    # acceptance of band k: fraction of curves with e > k; the narrowest band with acceptance >= 1-alpha
    acc = 1 - np.searchsorted(np.sort(e), ks, side="right") / Mp1
    ok = np.nonzero(acc >= 1 - alpha)[0]
    kstar = ok.max() if len(ok) else 0
    glob = edge[0] <= kstar
    sign = np.zeros(D.shape[1], int)
    if two_sided:
        sign[ge[0] <= pw_thr] = 1
        sign[le[0] <= pw_thr] = -1
    else:
        sign[ge[0] <= pw_thr] = 1
    segs = []
    x = 0
    while x < len(sign):
        if sign[x] != 0:
            y = x
            while y + 1 < len(sign) and sign[y + 1] == sign[x]:
                y += 1
            if glob[x:y + 1].any():
                segs.append((GRID[x], GRID[y], int(sign[x])))
            x = y + 1
        else:
            x += 1
    return dict(D0=D[0], sign=sign, glob=glob, segments=segs, significant=bool(glob.any()), kstar=int(kstar))


def seg_length(segs):
    return sum(b - a + (GRID[1] - GRID[0]) for a, b, s in segs)


def seg_in(segs, lo, hi):
    return any(b >= lo and a <= hi for a, b, s in segs)


# ---------------------------------------------------------------- jitter cross-correlograms

@njit(cache=True)
def _near_pairs(ta, tb, win):
    """All (i, j, tb[j]-ta[i]) with |difference| < win; ta, tb sorted."""
    out_i, out_j, out_d = [], [], []
    j0 = 0
    nb = len(tb)
    for i in range(len(ta)):
        while j0 < nb and tb[j0] < ta[i] - win:
            j0 += 1
        j = j0
        while j < nb and tb[j] < ta[i] + win:
            out_i.append(i)
            out_j.append(j)
            out_d.append(tb[j] - ta[i])
            j += 1
    return np.array(out_i, np.int64), np.array(out_j, np.int64), np.array(out_d)


@njit(cache=True)
def _jitter_ccg(ii, jj, dd, na, nb, M, half_jit, edges, seed, jitter_b):
    """CCG counts of real data (row 0) and M jitter surrogates over bins `edges` (seconds).

    Each spike of a (and of b when jitter_b) is moved uniformly on [-half_jit, +half_jit]; a spike
    keeps one jitter value within a surrogate for all its pairs."""
    np.random.seed(seed)
    nbins = len(edges) - 1
    out = np.zeros((M + 1, nbins), np.int64)
    lo, hi = edges[0], edges[-1]
    w = edges[1] - edges[0]
    for k in range(len(dd)):
        d = dd[k]
        if d >= lo and d < hi:
            out[0, int((d - lo) / w)] += 1
    ja = np.zeros(na)
    jb = np.zeros(nb)
    for m in range(1, M + 1):
        for k in range(na):
            ja[k] = (np.random.random() * 2 - 1) * half_jit
        if jitter_b:
            for k in range(nb):
                jb[k] = (np.random.random() * 2 - 1) * half_jit
        for k in range(len(dd)):
            d = dd[k] + jb[jj[k]] - ja[ii[k]]
            if d >= lo and d < hi:
                out[m, int((d - lo) / w)] += 1
    return out


def jitter_pair(ta, tb, M=1000, binw=0.001, seed=0, half_jit=0.005, window=0.005, jitter_b=True):
    """Real and jittered CCG of b relative to a over [-window, +window] [paper, Methods]. Every spike
    of both cells is jittered; jitter_b=False moves the spikes of a only (Supplementary Fig. 9A, a
    variant named in the claims file header)."""
    edges = np.round(np.arange(-window, window + binw / 2, binw), 6)
    ii, jj, dd = _near_pairs(ta, tb, window + 2 * half_jit + 1e-4)
    if len(dd) == 0:
        return edges, np.zeros((M + 1, len(edges) - 1), np.int64)
    ua, ia = np.unique(ii, return_inverse=True)
    ub, ib = np.unique(jj, return_inverse=True)
    C = _jitter_ccg(ia.astype(np.int64), ib.astype(np.int64), dd, len(ua), len(ub), M, half_jit,
                    edges, seed, jitter_b)
    return edges, C


def classify_ccg(edges, C, level=0.99, lag=(0.001, 0.004), width="W-a"):
    """Excitatory / inhibitory a->b (positive lags) and b->a (negative lags) by the global band.

    Global band from the maximum and minimum of each surrogate over the whole window, at 99%
    [paper, Methods]; significant when the counts break it anywhere in [1, 4] ms. Width reading
    W-b also asks the run of bins above the pointwise 99% band around the peak to span <= 2 ms
    [claims, header]."""
    real, sur = C[0], C[1:]
    gmax = np.quantile(sur.max(axis=1), level)
    gmin = np.quantile(sur.min(axis=1), 1 - level)
    pw_hi = np.quantile(sur, 1 - (1 - level) / 2, axis=0)
    centers = (edges[:-1] + edges[1:]) / 2
    res = {}
    for direction, sgn in (("ab", 1), ("ba", -1)):
        inlag = (sgn * centers > lag[0]) & (sgn * centers < lag[1])
        exc = bool((real[inlag] > gmax).any())
        inh = bool((real[inlag] < gmin).any())
        if exc and width == "W-b":
            above = real > pw_hi
            peak = np.nonzero(inlag & (real > gmax))[0]
            ok = False
            binw = edges[1] - edges[0]
            for p in peak:
                a = b = p
                while a - 1 >= 0 and above[a - 1]:
                    a -= 1
                while b + 1 < len(above) and above[b + 1]:
                    b += 1
                if (b - a + 1) * binw <= 0.002 + 1e-9:
                    ok = True
            exc = ok
        res[direction] = (exc, inh)
    return res


# ---------------------------------------------------------------- position of excess coincidences

@njit(cache=True)
def _coinc_jitter(ii, jj, dd, na, nb, M, half_jit, lo, hi, seed, jitter_b, q, KT):
    """Coincidence rate curves (M+1 x grid): row 0 real, rows 1..M jittered. A pair k counts when
    lo <= t_b - t_a <= hi; the kernel row KT[q[k]] of its position is added (positions on a 1e-4
    grid, so that memory does not grow with the number of pairs). Each spike keeps one jitter value
    within a surrogate for all its pairs."""
    np.random.seed(seed)
    G = KT.shape[1]
    out = np.zeros((M + 1, G))
    for k in range(len(dd)):
        if dd[k] >= lo and dd[k] <= hi:
            for g in range(G):
                out[0, g] += KT[q[k], g]
    ja = np.zeros(na)
    jb = np.zeros(nb)
    for m in range(1, M + 1):
        for k in range(na):
            ja[k] = (np.random.random() * 2 - 1) * half_jit
        if jitter_b:
            for k in range(nb):
                jb[k] = (np.random.random() * 2 - 1) * half_jit
        for k in range(len(dd)):
            d = dd[k] + jb[jj[k]] - ja[ii[k]]
            if d >= lo and d <= hi:
                for g in range(G):
                    out[m, g] += KT[q[k], g]
    return out


_KT = None


def _kernel_table():
    """Kernel rows for positions 0, 1e-4, ..., 1 [standard: a 1e-4 step is 1/500 of the bandwidth]."""
    global _KT
    if _KT is None:
        _KT = kernel_matrix(np.linspace(0, 1, 10001))
    return _KT


def coincidence_position_test(sess, a, b, trials_mask, M=1000, alpha=0.01, seed=0, jitter_b=True):
    """Methods, 'Identifying position dependence of monosynaptic interactions'.

    Coincident events: spike pairs with 1 <= t_b - t_a <= 4 ms [paper], placed at the presynaptic
    spike's position [claims, standard], smoothed with the 0.05 kernel, divided by the number of
    trials; jitter of both cells on [-5, +5] ms [paper; jitter_b=False is Supplementary Fig. 12B's
    presynaptic jitter]; one-sided pointwise and global bands at alpha = 0.01 [paper, Fig. 4]."""
    ta = sess.times[a]
    tb = sess.times[b]
    ii, jj, dd = _near_pairs(ta, tb, 0.004 + 2 * 0.005 + 1e-4)
    ntr = int(trials_mask.sum())
    if len(dd) == 0 or ntr == 0:
        return None
    k = sess.trial_of(ta[ii])
    keep = k >= 0
    keep[keep] = trials_mask[k[keep]]
    ii, jj, dd = ii[keep], jj[keep], dd[keep]
    if len(dd) == 0:
        return None
    x = sess.position(ta[ii])
    ua, ia = np.unique(ii, return_inverse=True)
    ub, ib = np.unique(jj, return_inverse=True)
    q = np.rint(x * 10000).astype(np.int64)
    S = _coinc_jitter(ia.astype(np.int64), ib.astype(np.int64), dd, len(ua), len(ub), M, 0.005,
                      0.001, 0.004, seed, jitter_b, q, _kernel_table()) / ntr
    r = bands_from_curves(S, alpha, two_sided=False)
    r["expected"] = S[1:].mean(axis=0)
    r["n_events"] = int(np.sum((dd >= 0.001) & (dd <= 0.004)))
    return r


# ---------------------------------------------------------------- first and later spikes (Figure 6)

def spike_labels(t, reading="x"):
    """First spikes (preceded by > 200 ms without spikes) and later spikes (< 40 ms after the previous
    spike) [paper, Results; Figure 6b legend]. Reading x: a later spike must belong to a train begun by
    a first spike, with every interval since < 40 ms; reading y: any spike < 40 ms after the previous."""
    isi = np.diff(t, prepend=-np.inf)
    first = isi > 0.2
    later = isi < 0.04
    if reading == "x":
        intrain = np.zeros(len(t), bool)
        on = False
        for i in range(len(t)):
            if first[i]:
                on = True
            elif isi[i] >= 0.04:
                on = False
            intrain[i] = on and not first[i]
        later = later & intrain
    return first, later


@njit(cache=True)
def _per_spike_jitter_counts(ta, tb, M, half_jit, lo, hi, seed):
    """For each spike of a: count of b spikes at lag [lo, hi) real (col 0) and under M jitters of a."""
    np.random.seed(seed)
    n = len(ta)
    H = np.zeros((n, M + 1), np.float32)
    nb = len(tb)
    j0 = 0
    for i in range(n):
        while j0 < nb and tb[j0] < ta[i] - half_jit + lo - 1e-9:
            j0 += 1
        for m in range(M + 1):
            s = ta[i] if m == 0 else ta[i] + (np.random.random() * 2 - 1) * half_jit
            c = 0
            j = j0
            while j < nb and tb[j] < s + hi:
                if tb[j] >= s + lo:
                    c += 1
                j += 1
            H[i, m] = c
    return H


@njit(cache=True)
def _per_spike_jitter_counts_both(ii, jj, dd, na, nb, M, half_jit, lo, binw, nbins, seed):
    """Per spike of a (rows, compact index ii) and lag bin: count of b spikes at lag
    [lo + k binw, lo + (k+1) binw), real (col 0) and under M surrogates jittering every spike of a
    and of b (each spike keeps one jitter value within a surrogate for all its pairs)."""
    np.random.seed(seed)
    H = np.zeros((nbins, na, M + 1), np.float32)
    hi = lo + nbins * binw
    for k in range(len(dd)):
        d = dd[k]
        if d >= lo and d < hi:
            H[int((d - lo) / binw), ii[k], 0] += 1
    ja = np.zeros(na)
    jb = np.zeros(nb)
    for m in range(1, M + 1):
        for k in range(na):
            ja[k] = (np.random.random() * 2 - 1) * half_jit
        for k in range(nb):
            jb[k] = (np.random.random() * 2 - 1) * half_jit
        for k in range(len(dd)):
            d = dd[k] + jb[jj[k]] - ja[ii[k]]
            if d >= lo and d < hi:
                H[int((d - lo) / binw), ii[k], m] += 1
    return H


def standardized_height_test(ta, tb, first, later, M_jit=1000, R=1000, seed=0, lag=(0.001, 0.004), jitter="both"):
    """Standardized peak height h_hat = (h - mu_jitter) / sd_jitter [paper, Supplementary Fig. 9B] for
    first and later presynaptic spikes, and the two-sided permutation test of their difference
    shuffling the labels [paper, Supplementary Fig. 16]. The jitter is the shared method's [claims,
    header]: every spike of both cells on [-5, +5] ms, M_jit = 1,000 surrogates; jitter="pre" moves
    the presynaptic spikes only (Supplementary Fig. 9A, a variant). Peak readings: 'sum' over
    [1, 4] ms, 'max' the largest 1 ms bin (its standardized height). R = 1,000 permutations [claims,
    standard]. The side of a significant pair is the tail of the permutation distribution the
    observed difference falls in (Figure 6c legend, "one side corresponds 'facilitation', the other
    to 'depression'"): 'dep' when it is above the permutation median (first spikes relatively
    stronger), 'fac' when below. The sign of the raw difference is not used, as the standardized
    height grows with the number of spikes and first spikes usually outnumber later ones.
    Returns a dict per peak reading."""
    rng = np.random.default_rng(seed)
    idx = np.nonzero(first | later)[0]
    if first.sum() < 5 or later.sum() < 5:
        return None
    nbin = int(round((lag[1] - lag[0]) / 0.001))
    if jitter == "pre":
        Hb = [_per_spike_jitter_counts(ta[idx], tb, M_jit, 0.005, lo, lo + 0.001, seed)
              for lo in np.arange(lag[0], lag[1] - 1e-9, 0.001)]
        nz = np.nonzero(np.any([H.any(axis=1) for H in Hb], axis=0))[0]
        Hb = [H[nz] for H in Hb]
    else:
        ii, jj, dd = _near_pairs(ta[idx], tb, lag[1] + 2 * 0.005 + 1e-4)
        if len(dd) == 0:
            return None
        nz, ia = np.unique(ii, return_inverse=True)
        ub, ib = np.unique(jj, return_inverse=True)
        H3 = _per_spike_jitter_counts_both(ia.astype(np.int64), ib.astype(np.int64), dd, len(nz), len(ub),
                                           M_jit, 0.005, lag[0], 0.001, nbin, seed)
        Hb = [H3[k] for k in range(nbin)]
    lab = first[idx]
    labs = np.empty((R + 1, len(idx)), bool)
    labs[0] = lab
    for r in range(1, R + 1):
        labs[r] = rng.permutation(lab)
    Lf = labs[:, nz].astype(np.float32)
    Ll = (1.0 - Lf).astype(np.float32)

    def z(S):
        S = S.astype(np.float64)
        mu, sd = S[:, 1:].mean(1), S[:, 1:].std(1)
        with np.errstate(invalid="ignore", divide="ignore"):
            return (S[:, 0] - mu) / np.where(sd > 0, sd, np.nan)
    PF = [Lf @ H for H in Hb]
    PL = [Ll @ H for H in Hb]
    out = {}
    for peak in ("sum", "max"):
        with np.errstate(invalid="ignore"), warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            if peak == "sum":
                zf, zl = z(sum(PF)), z(sum(PL))
            else:
                zf = np.nanmax(np.vstack([z(P) for P in PF]), axis=0)
                zl = np.nanmax(np.vstack([z(P) for P in PL]), axis=0)
        diff = zf - zl
        d0 = diff[0]
        null = diff[1:][np.isfinite(diff[1:])]
        if not np.isfinite(d0) or len(null) == 0:
            out[peak] = None
            continue
        p_up = (np.sum(null >= d0) + 1) / (len(null) + 1)
        p_lo = (np.sum(null <= d0) + 1) / (len(null) + 1)
        p = min(1.0, 2 * min(p_up, p_lo))
        side = "dep" if d0 > np.median(null) else "fac"
        out[peak] = dict(z_first=zf[0], z_later=zl[0], diff=d0, null_mean=float(null.mean()),
                         null_median=float(np.median(null)), p=p, side=side)
    out["n_first"], out["n_later"] = int(first.sum()), int(later.sum())
    return out
