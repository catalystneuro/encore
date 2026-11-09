"""Loading and measures for CRCNS data set apl-1 (Bruno & Frost 2017).

Bruno, Frost & Humphries (2017), "A spiral attractor network drives rhythmic locomotion",
eLife 6:e27342, doi:10.7554/elife.27342. The data set (doi:10.6080/K0SN074B) holds the spike
times of 30 voltage-sensitive dye recordings (10 preparations, 3 evoked bouts each), the P10
nerve spikes of 9 of them, and neuron coordinates on the photodiode array. Files are streamed
from the public S3 bucket ``crcnsarchive`` and read in memory; nothing is written to disk.

Where the parameters come from. "Methods" is the paper's Materials and methods; "code" is the
paper's analysis code, https://github.com/mdhumphries/AplysiaAttractorAnalysis at commit
e5f28e986eb3165df1441a49eee4e07c25ee01fe, as cited by the claims file.

- Stimulation onset 30 s, offset 32.5 s: Methods (Imaging) and the data description.
- Spike-density functions: 10 ms grid, Gaussian kernel to +/-5 SD with unit area (Methods,
  Spike-train analysis; code DataSet_Properties.m). The SD is open (claim fig2b-dimensions):
  ``sd_mode`` 'sqrt12' (median ISI / sqrt(12)), 'twelve' (median ISI / 12, as the extracted
  text prints), 'own' (median ISI of the recording, the code's choice of width) and 'pooled'
  (the code's running median over the recordings of the same bout number read so far). The
  median ISI uses the ISIs of every neuron after stimulation onset (code).
- PCA on the covariance of the post-onset spike-density functions, mean-centred (Methods,
  Recurrence analysis; code princomp). Number of PCs: ``count`` 'min80' (smallest number
  reaching 80%, Methods) or 'le80' (number whose cumulative variance is at most 80%, code
  Analyse_by_Recurrence_Points.m).
- Recurrence: theta at the 2nd, 5th and 10th percentiles of all distances between post-onset
  points; points checked from 35 s to 10 s before the end; the first contiguous run within theta
  after the point is dropped; histogram of delays in 1 s bins on 0..50 s; peaks are runs of
  non-empty bins at 5 s or more with at least 100 points; 5 s windows stepped by 1 s (Methods,
  Recurrence analysis; code Analyse_by_Recurrence_Points.m for the bins, the 100-point rule
  and the windows).
- Local linear models: the contiguous run of points within 2.5 theta around each point of the
  dominant orbit, least squares of the first difference on the points, points with at least 100
  neighbours averaged (Methods, Statistical estimation of the attractor's parameters; code
  LocalLinearDynamics.m). The "maximum eigenvalue" is the one of largest modulus, as MATLAB's
  max orders complex numbers (code); ties between a conjugate pair go to the one with positive
  imaginary part, as MATLAB breaks ties by phase angle.
- Multitaper spectra: a port of Chronux mtspectrumpt with its default tapers [3 5], 1 ms
  sampling, fpass 0..1 Hz (Methods, Spike-train analysis; code DataSet_Properties.m).
"""

from __future__ import annotations

import hashlib
import io

import fsspec
import numpy as np
import scipy.io as sio
from scipy.signal.windows import dpss
from scipy.spatial.distance import directed_hausdorff, pdist

DATASET = "apl-1"            # CRCNS data set, doi:10.6080/K0SN074B
VERSION = "unversioned"      # CRCNS data sets are not versioned (docs/archives.md); MD5 sums are checked
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/live/"
FILES = ["FileTable.mat", "SpikeData.mat", "ExtracellularData.mat", "Coordinates.mat",
         "diode_template.mat"]
STIM_ON, STIM_OFF = 30.0, 32.5
DT = 0.01
THETA_PRCT = (2, 5, 10)
T0 = 35.0           # start checking recurrence (code pars.T0; Methods "5 s after stimulation")
MAX_WINDOW = 10.0   # stop 10 s before the end
TMIN = 5.0          # minimum delay for a peak
NMIN = 100          # minimum points in a peak (code pars.Nmin)
WIN_L, WIN_STEP = 5.0, 1.0
NEIGHBOUR_D = 2.5
MIN_NEIGHBOURS = 100


def _read(name):
    with fsspec.open(BUCKET + name, "rb", block_size=2**20) as f:
        return f.read()


def load():
    """Stream the data set's MATLAB files. Returns a dict with the raw bytes' MD5 sums,
    the archive's checksums.md5, and the parsed contents."""
    raw = {n: _read(n) for n in FILES}
    md5 = {n: hashlib.md5(b).hexdigest() for n, b in raw.items()}
    listed = {}
    for line in _read("checksums.md5").decode().splitlines():
        if line.strip():
            h, n = line.split()
            listed[n] = h
    mats = {n: sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
            for n, b in raw.items()}
    ft = mats["FileTable.mat"]["FileTable"]
    preps = []
    for i, row in enumerate(ft[1:]):
        p10 = row[3]
        preps.append({"prep": i + 1, "file": str(row[0]), "name": str(row[0]).replace("da01.mat", ""),
                      "side": str(row[1]), "n_neurons_table": int(row[2]),
                      "p10_bouts": [] if isinstance(p10, str) else [int(x) for x in np.atleast_1d(p10)]})
    recs = []
    for s in mats["SpikeData.mat"]["SpikeData"]:
        fn = str(s.filename)
        name = fn[:-8]
        bout = int(fn[-5])
        prep = next(p["prep"] for p in preps if p["name"] == name)
        spks = np.asarray(s.spks, float)
        recs.append({"file": fn, "prep": prep, "bout": bout, "Bout_field": s.Bout,
                     "ids": spks[:, 0].astype(int), "t": spks[:, 1]})
    p10 = []
    for s in mats["ExtracellularData.mat"]["ExtracellularData"]:
        fn = str(s.filename)
        spks = np.atleast_2d(np.asarray(s.spks, float))
        # The P10 file names lack the "B" of prep Jun0414B; the code matches on the first 7
        # characters (DecodeP10_statespace.m), as here.
        prep = next(p["prep"] for p in preps if p["name"][:7] == fn[:7])
        p10.append({"file": fn, "prep": prep, "bout": int(s.Bout), "ids": spks[:, 0],
                    "t": np.sort(spks[:, 1]), "sorted": bool(np.all(np.diff(spks[:, 1]) >= 0))})
    coords = []
    for s in mats["Coordinates.mat"]["Coordinates"]:
        coords.append({"file": str(s.filename), "ganglion": str(s.ganglion),
                       "x": np.asarray(s.x, float), "y": np.asarray(s.y, float)})
    return {"md5": md5, "listed_md5": listed, "preps": preps, "recs": recs, "p10": p10,
            "coords": coords, "template": mats["diode_template.mat"]["diode_template"]}


def neuron_trains(rec):
    """Spike times per neuron id 1..N (ids as stored)."""
    n = int(rec["ids"].max())
    return [np.sort(rec["t"][rec["ids"] == i]) for i in range(1, n + 1)]


def post_onset_isis(rec):
    out = []
    for tr in neuron_trains(rec):
        tr = tr[tr >= STIM_ON]
        if tr.size > 1:
            out.append(np.diff(tr))
    return np.concatenate(out)


def gaussian_sds(recs):
    """Kernel SD (s) per recording under each reading of the Methods and the code."""
    own = np.array([np.median(post_onset_isis(r)) for r in recs])
    pooled = np.zeros(len(recs))
    for bout in (1, 2, 3):
        acc = []
        for i in sorted([i for i, r in enumerate(recs) if r["bout"] == bout],
                        key=lambda i: recs[i]["file"]):
            acc.append(post_onset_isis(recs[i]))
            pooled[i] = np.median(np.concatenate(acc))
    return {"sqrt12": own / np.sqrt(12), "twelve": own / 12, "own": own, "pooled": pooled}


def kernel(sd):
    sig = sd / DT
    x = np.arange(-5 * sig, 5 * sig + 1e-9, 1.0)
    h = np.exp(-x**2 / (2 * sig**2))
    return h / h.sum()


def sdf_matrix(trains, sd, t_end):
    """Spike-density functions (spikes/s) on the grid 0, 0.01, ..., t_end; one column per train."""
    nb = int(np.floor(t_end / DT + 1e-9)) + 1
    h = kernel(sd)
    half = (h.size - 1) / 2
    out = np.zeros((nb, len(trains)))
    for j, tr in enumerate(trains):
        k = np.round(tr / DT).astype(int)
        k = k[(k >= 0) & (k < nb)]
        c = np.bincount(k, minlength=nb).astype(float)
        y = np.convolve(c, h)
        s = int(np.floor(half))
        out[:, j] = y[s:s + nb]
    return out / DT


def pca(x):
    """Mean-centred PCA. Returns coeffs (columns), centred projections, eigenvalues (descending)."""
    xc = x - x.mean(0)
    cov = xc.T @ xc / (x.shape[0] - 1)
    ev, vec = np.linalg.eigh(cov)
    o = np.argsort(ev)[::-1]
    ev, vec = np.clip(ev[o], 0, None), vec[:, o]
    return vec, xc @ vec, ev


def n_pcs(ev, frac=0.8, rule="min80"):
    cum = np.cumsum(ev) / ev.sum()
    if rule == "min80":
        return int(np.argmax(cum >= frac - 1e-12) + 1)
    return int(np.sum(cum <= frac))


class Program:
    """One recording: spike-density functions, PCA, and the recurrence analysis."""

    def __init__(self, rec, sd, rule="min80"):
        self.rec, self.sd, self.rule = rec, sd, rule
        self.trains = neuron_trains(rec)
        self.t_end = rec["t"].max()
        self.sdf = sdf_matrix(self.trains, sd, self.t_end)
        self.bins = np.arange(self.sdf.shape[0]) * DT
        self.ix_stim = np.flatnonzero(self.bins >= STIM_ON - 1e-9)
        self.stimbins = self.bins[self.ix_stim]
        self.coeffs, self.proj, self.ev = pca(self.sdf[self.ix_stim])
        self.d = max(n_pcs(self.ev, 0.8, rule), 1)
        self.pcs = self.proj[:, :self.d]

    # ---------------- recurrence ----------------
    def recurrence(self, prct=THETA_PRCT):
        X = self.pcs
        n = X.shape[0]
        # all pairwise distances, for the percentiles of theta
        sq = (X**2).sum(1)
        dists = pdist(X)
        self.theta = np.percentile(dists, prct)
        del dists
        ix0 = int(np.argmin(np.abs(self.stimbins - T0)))
        ix_end = int(np.argmin(np.abs(self.stimbins - (self.stimbins[-1] - MAX_WINDOW))))
        self.ix0, self.ix_end = ix0, ix_end
        pts = np.arange(ix0 + 1, ix_end + 1)       # code: points ix0+1 .. ixEnd
        delay = np.full((pts.size, len(prct)), np.nan)
        for a in range(0, pts.size, 500):
            p = pts[a:a + 500]
            g = sq[p, None] + sq[None, :] - 2 * X[p] @ X.T
            g = np.sqrt(np.maximum(g, 0))
            for r, i in enumerate(p):
                row = g[r, i + 1:]
                for k, th in enumerate(self.theta):
                    idx = np.flatnonzero(row <= th)
                    if idx.size == 0:
                        continue
                    gaps = np.flatnonzero(np.diff(idx) > 1)
                    if gaps.size == 0:
                        continue
                    delay[a + r, k] = (idx[gaps[0] + 1] + 1) * DT
        self.delay = delay
        self.pt_index = pts           # index into stimbins of each checked point
        self.pt_time = self.stimbins[pts]
        return delay

    def peaks(self, k=-1):
        """Peaks of the delay histogram at threshold k. Returns list of dicts (index arrays)."""
        dl = self.delay[:, k]
        edges = np.arange(0, 51)
        h = np.zeros(51)
        v = dl[~np.isnan(dl)]
        v = v[(v >= 0) & (v <= 50)]
        bi = np.minimum(np.floor(v + 1e-9).astype(int), 50)
        np.add.at(h, bi, 1)
        filled = np.flatnonzero(h[5:] > 0) + 5
        out = []
        if filled.size == 0:
            return out
        runs = np.split(filled, np.flatnonzero(np.diff(filled) > 1) + 1)
        for run in runs:
            lo, hi = edges[run[0]], edges[run[-1]] + 1
            ids = np.flatnonzero((dl >= lo) & (dl <= hi))
            if ids.size >= NMIN:
                out.append({"ids": ids, "mean": float(np.mean(dl[ids])),
                            "median": float(np.median(dl[ids])), "n": int(ids.size),
                            "lo": float(lo), "hi": float(hi)})
        return out

    def dominant(self, k=-1):
        pk = self.peaks(k)
        if not pk:
            return None, pk
        return max(pk, key=lambda p: p["n"]), pk

    def windows(self, k=-1):
        """5 s windows stepped by 1 s: start index (stimbins), mid time, density of recurrent
        points, mean and SD of delays (code AllRecurrentPoint)."""
        win = int(round(WIN_L / DT))
        step = int(round(WIN_STEP / DT))
        starts = np.arange(self.ix0, self.ix_end - win + 1, step)
        dl = self.delay[:, k]
        rel = self.pt_index - self.ix0     # 1..nTs
        dens, md, sdd, mids = [], [], [], []
        for s in starts:
            m = (rel > s - self.ix0) & (rel <= s + win - self.ix0)
            v = dl[m]
            ok = ~np.isnan(v)
            dens.append(ok.sum() / win)
            md.append(np.mean(v[ok]) if ok.any() else np.nan)
            sdd.append(np.std(v[ok], ddof=1) if ok.sum() > 1 else np.nan)
            mids.append(self.stimbins[int(round(s + win / 2))])
        return {"start": starts, "start_t": self.stimbins[starts], "mid_t": np.array(mids),
                "dens": np.array(dens), "mdelay": np.array(md), "sddelay": np.array(sdd)}

    # ---------------- local linear dynamics ----------------
    def local_linear(self, ids, k=-1):
        """Local linear models around the checked points ``ids`` (rows of self.delay)."""
        X = self.pcs
        th = self.theta[k] * NEIGHBOUR_D
        out_eigs = np.full((len(ids), self.d), np.nan, complex)
        npts = np.zeros(len(ids), int)
        sq = (X**2).sum(1)
        for a in range(0, len(ids), 500):
            chunk = ids[a:a + 500]
            p = self.pt_index[chunk]
            g = sq[p, None] + sq[None, :] - 2 * X[p] @ X.T
            within = g <= th**2
            for r, i in enumerate(p):
                w = within[r]
                # contiguous run of within-neighbourhood points containing the point
                before = np.flatnonzero(~w[:i])
                after = np.flatnonzero(~w[i + 1:])
                lo = before[-1] + 1 if before.size else 0
                hi = i + after[0] if after.size else len(w) - 1
                seg = X[lo:hi + 1]
                npts[a + r] = seg.shape[0]
                if seg.shape[0] < 3:
                    continue
                A, *_ = np.linalg.lstsq(seg[:-1], np.diff(seg, axis=0), rcond=None)
                e = np.linalg.eigvals(A)
                # MATLAB sort(...,'descend') on complex: by modulus, then phase angle
                o = np.lexsort((-np.angle(e), -np.abs(e)))
                out_eigs[a + r] = e[o]
        return out_eigs, npts


def emax_stats(eigs, npts):
    """Mean real and imaginary part of the maximum eigenvalue over points with enough
    neighbours (code recurrence_point_results_Viz.m)."""
    use = npts >= MIN_NEIGHBOURS
    em = eigs[use, 0]
    with np.errstate(divide="ignore"):
        rot = 2 * np.pi / np.imag(em) * DT
    rot[~np.isfinite(rot)] = 0       # code: inf (no rotation) set to 0
    return {"a": float(np.mean(em.real)), "b": float(np.mean(em.imag)),
            "sd_a": float(np.std(em.real, ddof=1)), "sd_b": float(np.std(em.imag, ddof=1)),
            "n_used": int(use.sum()), "n_all": int(len(npts)), "mrot": float(np.mean(rot)),
            "eigs": eigs[use]}


# ---------------- multitaper spectrum (Chronux mtspectrumpt port) ----------------
def mtspectrumpt(trains, fs=1000.0, fpass=(0.0, 1.0), tapers=(3, 5)):
    """Port of Chronux mtspectrumpt with trialave=1: point-process multitaper spectrum,
    averaged over the trains. Time grid from the earliest to the latest spike, minus and plus
    one sample, as Chronux's minmaxsptimes."""
    allt = np.concatenate([t for t in trains if t.size])
    dt = 1 / fs
    t = np.arange(allt.min() - dt, allt.max() + dt + dt / 2, dt)
    N = t.size
    nfft = max(int(2 ** np.ceil(np.log2(N))), N)
    f = np.arange(nfft) * fs / nfft
    findx = (f >= fpass[0]) & (f <= fpass[1])
    f = f[findx]
    tp = dpss(N, tapers[0], tapers[1]).T * np.sqrt(fs)    # N x K
    w = 2 * np.pi * f
    H = np.fft.fft(tp, nfft, axis=0)[findx]                # fft of tapers, retained frequencies
    S = np.zeros(f.size)
    for tr in trains:
        d = tr[(tr >= t.min()) & (tr <= t.max())]
        msp = d.size / N
        if d.size == 0:
            continue
        proj = np.column_stack([np.interp(d, t, tp[:, k]) for k in range(tp.shape[1])])
        ex = np.exp(-1j * np.outer(w, d - t[0]))
        J = ex @ proj - H * msp
        S += np.mean(np.abs(J) ** 2, axis=1)
    return f, S / len(trains)


def peak_frequency(f, S):
    """Code DataSet_Properties.m: power-weighted mean frequency of the region more than 2 SD
    above the spectrum's mean."""
    hi = S > S.mean() + 2 * S.std(ddof=1)
    return float(np.sum(f[hi] * S[hi]) / S[hi].sum())


def analyse_program(args):
    """Recurrence analysis of one recording under one reading; with ``lld`` also the local
    linear models of the dominant orbit at the 10% threshold. Returns plain arrays."""
    rec, sd, rule, lld = args
    P = Program(rec, sd, rule)
    P.recurrence()
    out = {"file": rec["file"], "prep": rec["prep"], "bout": rec["bout"], "sd": sd, "rule": rule,
           "d": P.d, "ev": P.ev, "theta": P.theta, "delay": P.delay, "pt_index": P.pt_index,
           "pt_time": P.pt_time, "ix0": P.ix0, "ix_end": P.ix_end, "t_end": P.t_end,
           "n_neurons": len(P.trains)}
    out["peaks"] = [P.peaks(k) for k in range(len(THETA_PRCT))]
    out["windows"] = [P.windows(k) for k in range(len(THETA_PRCT))]
    if lld:
        dom, _ = P.dominant(-1)
        if dom is not None:
            out["eigs"], out["npts"] = P.local_linear(dom["ids"])
    return out


def run_all(recs, sds, rule, lld=True, workers=3):
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    jobs = [(r, float(s), rule, lld) for r, s in zip(recs, sds)]
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
        return list(ex.map(analyse_program, jobs))


# ---------------- summaries of the recurrence analysis ----------------
def summarise(o, k=-1):
    """Dominant orbit, density and coalescence of one analysed program at threshold k."""
    pk = o["peaks"][k]
    dl = o["delay"][:, k]
    rec = ~np.isnan(dl)
    hist_n = int(np.sum(rec & (dl >= TMIN) & (dl <= 50)))
    s = {"file": o["file"], "prep": o["prep"], "bout": o["bout"], "d": o["d"],
         "n_peaks": len(pk), "prop_recurrent": float(rec.mean()), "n_points": int(dl.size)}
    if pk:
        dom = max(pk, key=lambda p: p["n"])
        s.update(period_mean=dom["mean"], period_median=dom["median"], dom_n=dom["n"],
                 prop_dom_hist=dom["n"] / hist_n, prop_dom_all=dom["n"] / int(rec.sum()))
    else:
        s.update(period_mean=np.nan, period_median=np.nan, dom_n=0, prop_dom_hist=np.nan,
                 prop_dom_all=np.nan)
    w = o["windows"][k]
    hi = np.flatnonzero(w["dens"] >= 0.9)   # Methods: "at least 90%"
    s["coalesce_t"] = float(w["mid_t"][hi[0]]) if hi.size else np.nan
    if hi.size:
        after = np.flatnonzero(o["pt_time"] >= w["mid_t"][hi[0]])
        s["prop_recurrent_after"] = float(rec[after].mean()) if after.size else np.nan
    else:
        s["prop_recurrent_after"] = np.nan
    return s


def divergences(o, period, k=-1, cycles=2.0):
    """Divergent periods after coalescence (Methods, Testing return to the same manifold):
    runs of 5 s windows with recurrence density below 90% that fall below 50% at least once.
    Returns one dict per period with the divergent point (window of lowest density), whether
    density returns above 90%, whether it lies within ``cycles`` periods of the end, and the
    proportions for the same-manifold test."""
    w = o["windows"][k]
    dens = w["dens"]
    hi = np.flatnonzero(dens >= 0.9)
    if not hi.size:
        return []
    first = hi[0]
    low = dens < 0.9
    low[:first + 1] = False
    out = []
    idx = np.flatnonzero(low)
    if not idx.size:
        return out
    runs = np.split(idx, np.flatnonzero(np.diff(idx) > 1) + 1)
    t_end = o["t_end"]
    dl = o["delay"][:, k]
    win = int(round(WIN_L / DT))
    rel = o["pt_index"] - o["ix0"]
    for run in runs:
        if dens[run].min() >= 0.5:
            continue
        ip = run[np.argmin(dens[run])]
        returned = run[-1] + 1 < dens.size        # a later window is above 90%
        t_point = float(w["mid_t"][ip])
        near_end = (t_end - t_point) < cycles * period
        d = {"start_win": int(run[0]), "end_win": int(run[-1]), "point_win": int(ip),
             "t_point": t_point, "min_dens": float(dens[ip]), "returned": bool(returned),
             "near_end": bool(near_end)}
        if returned:
            before = run[0] - 1                    # final window before the divergent period
            s = w["start"][before]
            m = (rel > s - o["ix0"]) & (rel <= s + win - o["ix0"])
            nxt = o["pt_time"][m] + dl[m]
            nxt = nxt[~np.isnan(nxt)]
            t_return = float(w["start_t"][run[-1] + 1])   # start of the first window back above 90%
            d.update(t_return=t_return, n_before=int(nxt.size),
                     p_after_end=float(np.mean(nxt > t_return)) if nxt.size else np.nan,
                     p_after_point=float(np.mean(nxt > t_point)) if nxt.size else np.nan)
        out.append(d)
    return out


def weighted_r(x, y, w):
    sw = w.sum()
    mx, my = (w * x).sum() / sw, (w * y).sum() / sw
    cxx = (w * (x - mx) ** 2).sum() / sw
    cyy = (w * (y - my) ** 2).sum() / sw
    cxy = (w * (x - mx) * (y - my)).sum() / sw
    return cxy / np.sqrt(cxx * cyy)


def _ranks(v):
    r = np.empty(v.size)
    r[np.argsort(v, kind="stable")] = np.arange(1, v.size + 1)
    return r


def weighted_spearman(x, y, w, n_perm=10000, rng=None, pooled=False):
    """Weighted Spearman correlation (Methods, Tracking changes in periodicity; code
    WeightedCorrelation.m, which ranks without averaging ties) with a permutation p-value.
    ``pooled=False``: y is permuted against x, two-sided (the Methods give only "a permutation
    test with 10000 permutations"). ``pooled=True``: the code's test, which permutes the pooled
    x and y values and is one-sided in the direction of rho."""
    ok = ~(np.isnan(x) | np.isnan(y))
    x, y, w = x[ok], y[ok], w[ok]
    rx, ry = _ranks(x), _ranks(y)
    r = weighted_r(rx, ry, w)
    rng = rng or np.random.default_rng(0)
    perm = np.empty(n_perm)
    n = x.size
    pool = np.concatenate([x, y])
    for i in range(n_perm):
        if pooled:
            p = rng.permutation(2 * n)
            perm[i] = weighted_r(_ranks(pool[p[:n]]), _ranks(pool[p[n:]]), w)
        else:
            perm[i] = weighted_r(rx, ry[rng.permutation(n)], w)
    if pooled:
        p = np.mean(perm > r) if r > 0 else np.mean(perm < r)
    else:
        p = (np.sum(np.abs(perm) >= abs(r)) + 1) / (n_perm + 1)
    return float(r), float(p), int(n)


# ---------------- comparisons between the programs of a preparation ----------------
PAIRS = [(0, 1), (0, 2), (1, 2)]


def point_sets(o, k=-1):
    """Two readings of the points compared between programs, as indices into the post-onset
    grid: 'recurrent', every checked point that recurs (Methods, Testing convergence to the
    same manifold); 'code', every point of the 5 s windows with at least 90% recurrent points
    (code Are_sequential_attractors_the_same.m, ixAdPts)."""
    dl = o["delay"][:, k]
    rec = o["pt_index"][~np.isnan(dl)]
    w = o["windows"][k]
    win = int(round(WIN_L / DT))
    ok = np.flatnonzero(w["dens"] >= 0.9)
    code = np.unique(np.concatenate([np.arange(w["start"][i], w["start"][i] + win + 1) for i in ok])) \
        if ok.size else np.array([], int)
    return {"recurrent": rec, "code": code}


def _hausdorff_with_control(XA, XB, ia, ib, coeffs, sdfA, sdfB, rng, n_shuffle):
    """Hausdorff distance between point sets ia (of A) and ib (of B), and its control: the
    same with the target program's neurons shuffled before projection (Methods; code)."""
    PA, PB = XA[ia], XB[ib]
    dAB = directed_hausdorff(PA, PB)[0]
    dBA = directed_hausdorff(PB, PA)[0]
    ctrl = np.empty(n_shuffle)
    for s in range(n_shuffle):
        cB = (sdfB[:, rng.permutation(sdfB.shape[1])] @ coeffs)[ib]
        cA = (sdfA[:, rng.permutation(sdfA.shape[1])] @ coeffs)[ia]
        ctrl[s] = max(directed_hausdorff(PA, cB)[0], directed_hausdorff(PB, cA)[0])
    return float(max(dAB, dBA)), ctrl


def manifold_prep(args):
    """For the three programs of one preparation: Hausdorff distances with controls on the
    axes of program 1 and on common axes, under both point sets; the distances of Figure 3D;
    the similarity-matrix correlations of Figure 3F."""
    recs, sds, outs, seed, n_shuffle = args
    rng = np.random.default_rng(seed)
    progs = [Program(r, s, "min80") for r, s in zip(recs, sds)]
    sdfs = [p.sdf[p.ix_stim] for p in progs]
    res = {"prep": recs[0]["prep"]}
    # axes of program 1, smallest number of its PCs reaching 80% (code nPCsVAF80)
    k1 = n_pcs(progs[0].ev, 0.8, "min80")
    C1 = progs[0].coeffs[:, :k1]
    # common axes: PCA of the concatenated post-onset functions, PCs at most 80% (code CommonAxes)
    cat = np.vstack(sdfs)
    Cc, _, evc = pca(cat)
    kc = max(n_pcs(evc, 0.8, "le80"), 1)
    Cc = Cc[:, :kc]
    res["k_prog1"], res["k_common"] = k1, kc
    sets = [point_sets(o) for o in outs]
    for axes, C in (("prog1", C1), ("common", Cc)):
        X = [s @ C for s in sdfs]
        for ps in ("recurrent", "code"):
            for (i, j) in PAIRS:
                ia, ib = sets[i][ps], sets[j][ps]
                if ps == "code" and ia.size and ib.size:
                    start = max(ia.min(), ib.min())     # from the later program's first point
                    ia, ib = ia[ia >= start], ib[ib >= start]
                if ia.size == 0 or ib.size == 0:
                    res[(axes, ps, i, j)] = (np.nan, np.full(n_shuffle, np.nan))
                    continue
                res[(axes, ps, i, j)] = _hausdorff_with_control(X[i], X[j], ia, ib, C, sdfs[i],
                                                                sdfs[j], rng, n_shuffle)
    # Figure 3D (code Initial_Conditions.m), common axes
    X = [s @ Cc for s in sdfs]
    for (i, j) in PAIRS:
        ci = summarise(outs[i])["coalesce_t"] - STIM_ON
        cj = summarise(outs[j])["coalesce_t"] - STIM_ON
        A = X[i][:int(round(ci / DT))]
        B = X[j][:int(round(cj / DT))]
        onset = float(np.linalg.norm(X[i][0] - X[j][0]))
        trans = float(np.sqrt(((A[:, None, :] - B[None, ::5, :]) ** 2).sum(-1)).max()) if A.size and B.size else np.nan
        res[("ic", i, j)] = (onset, trans)
    # Figure 3F: similarity matrices
    S, E = [], []
    for s in sdfs:
        c = np.corrcoef(s.T)
        c[c < 0] = 0
        np.fill_diagonal(c, 0)
        S.append(c)
        tot = c.sum(0)
        E.append(np.outer(c.sum(1), tot) / tot.sum())
    res["sim"] = (S, E)
    return res


def run_manifold(recs, sds, outs, n_shuffle=100, seed=1, workers=4):
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    jobs = []
    for prep in sorted({r["prep"] for r in recs}):
        ix = sorted([i for i, r in enumerate(recs) if r["prep"] == prep], key=lambda i: recs[i]["bout"])
        jobs.append(([recs[i] for i in ix], [float(sds[i]) for i in ix], [outs[i] for i in ix],
                     seed * 1000 + prep, n_shuffle))
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
        return list(ex.map(manifold_prep, jobs))


# ---------------- eigenvalues of the local models ----------------
def eig_dimensions(eigs):
    """Code Check_All_Real_Eigenvalues.m: per point, the real part of each unique eigenvalue
    dimension (a conjugate pair counted once), in the order of the sorted eigenvalues; the
    proportion of points with a complex eigenvalue among the top one or two."""
    is_real = np.abs(eigs.imag) < np.finfo(float).eps * np.abs(eigs.real)
    n, d = eigs.shape
    max_dom = int(np.max((~is_real).sum(1)) / 2 + d % 2)
    U = np.zeros((n, max_dom))
    for p in range(n):
        c = 0
        for k in range(max_dom):
            if c >= d:
                U[p, k] = np.nan
                continue
            U[p, k] = eigs[p, c].real
            c += 1 if is_real[p, c] else 2
    return {"mean_unique": np.nanmean(U, 0), "p_complex1": float(np.mean(~is_real[:, 0])),
            "p_complex12": float(np.mean(~is_real[:, 0] | (~is_real[:, 1] if d > 1 else False)))}


# ---------------- participation ----------------
def participation(coeffs, ev, d):
    """Methods, Single neuron participation: sum over the d principal axes of the absolute
    eigenvalue-weighted weights, and the same normalised to the program's maximum."""
    raw = np.abs(coeffs[:, :d] * ev[:d][None, :]).sum(1)
    return raw, raw / raw.max()


def iterate_outliers(x):
    """Code iterateoutliers.m: fit a Gaussian, drop the point furthest from the mean (all ties),
    refit, and stop when the log likelihood falls; returns (mu, sd) of the last fit before the
    fall. MATLAB fitdist uses the unbiased SD."""
    from scipy.stats import norm
    keep = np.ones(x.size, bool)
    mu, sd = x.mean(), x.std(ddof=1)
    ll = norm.logpdf(x, mu, sd).sum()
    while keep.sum() > 3:
        dist = np.abs(x - mu)
        dist[~keep] = -1
        keep2 = keep & (dist < dist.max())
        y = x[keep2]
        mu2, sd2 = y.mean(), y.std(ddof=1)
        ll2 = norm.logpdf(y, mu2, sd2).sum()
        if ll2 < ll:
            break
        keep, mu, sd, ll = keep2, mu2, sd2, ll2
    return float(mu), float(sd), int((~keep).sum())


def hellinger(p, q, bins=np.arange(0, 1.0001, 0.05)):
    """Hellinger distance between histograms of normalised participation on MATLAB hist
    centres 0:0.05:1 (code RobustnessOfAttractor_to_single_neuron_variability.m)."""
    edges = np.concatenate([[-np.inf], (bins[:-1] + bins[1:]) / 2, [np.inf]])
    a = np.histogram(p, edges)[0].astype(float)
    b = np.histogram(q, edges)[0].astype(float)
    a, b = a / a.sum(), b / b.sum()
    return float(np.sqrt(np.sum((np.sqrt(a) - np.sqrt(b)) ** 2)) / np.sqrt(2))


# ---------------- P10 nerve ----------------
def p10_locking(neuron, p10, start=33.0, delays=np.arange(0, 0.0255, 0.001), jitter=0.002):
    """Code P10_ID_motorneurons.m: the proportion of a neuron's spikes after ``start`` followed
    by a P10 spike at each delay, within +/- jitter; returns the maximum over delays."""
    ts = neuron[neuron > start]
    if ts.size == 0:
        return np.nan, 0
    best = 0.0
    for d in delays:
        lo = np.searchsorted(p10, ts + d - jitter - 1e-12, "left")
        hi = np.searchsorted(p10, ts + d + jitter + 1e-12, "right")
        best = max(best, float(np.mean(hi > lo)))
    return best, int(ts.size)


def poisson_glm(X, y, iters=25, tol=1e-6, beta=None):
    """Poisson GLM with log link by iteratively reweighted least squares (as MATLAB glmfit);
    X includes the intercept column. y may be non-integer, as the code fits a rate. Stops when
    the deviance changes by less than ``tol`` relatively, or after ``iters`` iterations (a
    standard choice; the forecasts agree to three decimals with 100 iterations)."""
    if beta is None:
        beta = np.zeros(X.shape[1])
        beta[0] = np.log(max(y.mean(), 1e-6))
    else:
        beta = beta.copy()
    dev_old = np.inf
    for _ in range(iters):
        eta = np.clip(X @ beta, -30, 30)
        mu = np.exp(eta)
        z = eta + (y - mu) / mu
        W = mu
        XtW = X.T * W
        try:
            beta_new = np.linalg.solve(XtW @ X + 1e-10 * np.eye(X.shape[1]), XtW @ z)
        except np.linalg.LinAlgError:
            break
        beta = beta_new
        mu = np.exp(np.clip(X @ beta, -30, 30))
        with np.errstate(divide="ignore", invalid="ignore"):
            dev = 2 * np.sum(np.where(y > 0, y * np.log(y / mu), 0) - (y - mu))
        if abs(dev_old - dev) < tol * (abs(dev) + 0.1):
            break
        dev_old = dev
    return beta


def lagged(pcs, rows, n_hist):
    """Design matrix: intercept and the PCs at lags 1..n_hist time steps before each row."""
    cols = [np.ones(rows.size)]
    for h in range(1, n_hist + 1):
        cols.append(pcs[rows - h])
    return np.column_stack([cols[0]] + [c for c in cols[1:]]) if n_hist else cols[0][:, None]


def decode_p10(pcs, p10_rate, stimbins, hist_steps, train_s=40.0, test_s=10.0, step_s=1.0,
               start=33.0, train_frac=None):
    """Fit the P10 rate from the lagged PCs in a training window and forecast the next
    ``test_s`` s, windows stepped by ``step_s`` from ``start`` (Methods, Decoding motor output).
    With ``train_frac`` the training window is that fraction of the series after ``start``
    (the code's reading). Returns per-window forecast R, MAE, training R and MAE."""
    t_last = stimbins[-1]
    if train_frac is not None:
        train_s = round((t_last - start) * train_frac)
    out = []
    s0 = start
    n_test = int(round(test_s / DT))
    b = None
    while True:
        i0 = int(np.searchsorted(stimbins, s0 - 1e-9))
        i1 = int(np.searchsorted(stimbins, s0 + train_s - 1e-9))
        if i1 + n_test > stimbins.size:
            break
        rows = np.arange(max(i0, hist_steps), i1)
        X = lagged(pcs, rows, hist_steps)
        y = p10_rate[rows]
        b = poisson_glm(X, y, beta=b)     # warm start from the previous window
        fit = np.exp(np.clip(X @ b, -30, 30))
        rf = np.arange(i1, i1 + n_test)
        Xf = lagged(pcs, rf, hist_steps)
        fc = np.exp(np.clip(Xf @ b, -30, 30))
        yf = p10_rate[rf]
        with np.errstate(invalid="ignore"):
            out.append({"t": s0, "R": np.corrcoef(yf, fc)[0, 1], "MAE": np.median(np.abs(yf - fc)),
                        "R_train": np.corrcoef(y, fit)[0, 1], "MAE_train": np.median(np.abs(y - fit)),
                        "fc_max": float(fc.max())})
        s0 += step_s
    return out


HISTORIES_METHODS = list(range(5, 21))      # 50..200 ms in 10 ms steps (Methods)
HISTORIES_CODE = [5, 10, 15, 20, 25]         # 50..250 ms (code DecodeP10_statespace.m)


def decode_program(args):
    """Decoding of one P10 program under one windowing and dimension count (``frac`` of the
    variance, under count ``rule``, as claim fig2b-dimensions); the history with
    the smallest mean forecast MAE is kept (Methods: "the smallest median absolute error";
    code Best_P10_StateSpace_GLMmodels.m takes the mean over windows of the per-window
    median absolute error)."""
    rec, p10_t, sd, frac, windowing, hists, rule = args
    P = Program(rec, sd, "min80")
    d = n_pcs(P.ev, frac, rule)
    pcs = P.proj[:, :d]
    rate = sdf_matrix([p10_t], sd, P.t_end)[P.ix_stim, 0]
    res = {}
    for h in hists:
        if windowing == "methods":
            o = decode_p10(pcs, rate, P.stimbins, h)
        else:
            o = decode_p10(pcs, rate, P.stimbins, h, step_s=0.2, train_frac=0.5)
        res[h] = o
    best = min(res, key=lambda h: np.nanmean([w["MAE"] for w in res[h]]))
    # fc_max_by_history: the largest forecast of each window, to count forecasts that diverge
    # (reported, not judged; the clip of the linear predictor at 30 caps them at about 1e13).
    return {"file": rec["file"], "prep": rec["prep"], "bout": rec["bout"], "d": d, "best": best,
            "rate_max": float(rate.max()),
            "fc_max_by_history": {h: np.array([w["fc_max"] for w in v]) for h, v in res.items()},
            "windows": res[best], "by_history": {h: (np.array([w["R"] for w in v]),
                                                      np.array([w["MAE"] for w in v]))
                                                  for h, v in res.items()}}


def run_decoding(jobs, workers=4):
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
        return list(ex.map(decode_program, jobs))


# ---------------- ensembles and their types (claim fig7s2-no-invariant-core) ----------------
# A port of the code's ensemble pipeline: Analysis/Ensembles/StaticEnsembles.m (clustering from
# stimulation onset to the end), Functions/consensus_cluster_spike_data_binless.m (Gaussian
# functions, rectified correlation), Functions/allevsplitConTransitive.m (consensus community
# detection), Analysis/Ensembles/Analyse_Spike_Train_Properties.m (autocorrelogram of each
# ensemble's pooled spikes against 100 interval shuffles, Functions/shuffle_intervals.m and
# spike_xcorr.m) and Types_of_Ensemble_Across_Dataset.m (the four types). Parameters are the
# code's: quantisation 0.01 s (Data.GaussQt), the recording's median ISI as SD (Data.GaussSD),
# 50 k-means runs per number of groups, autocorrelogram bins of 1 s to 20 s, 100 shuffles,
# troughs of 2 SD and peaks of 3 SD over at least two consecutive bins. MATLAB's kmeans is
# replaced by Lloyd's algorithm from the code's own k-means++ start (at most 100 iterations, an
# empty cluster restarted at the farthest point, as MATLAB's 'singleton' default).

def _kmeans(X, k, rng, start=None, iters=100):
    n = X.shape[0]
    if start is None:                         # code kmeansplus
        C = np.empty((k, X.shape[1]))
        C[0] = X[int(np.ceil(n * rng.random())) - 1]
        v = np.full(n, np.inf)
        for i in range(1, k):
            v = np.minimum(v, np.sqrt(((X - C[i - 1]) ** 2).sum(1)))
            p = np.cumsum(v / v.sum())
            C[i] = X[min(int(np.searchsorted(p, rng.random(), "right")), n - 1)]
    else:
        C = np.array(start, float).reshape(k, -1)
    lab = None
    for _ in range(iters):
        D = ((X[:, None, :] - C[None]) ** 2).sum(-1)
        new = D.argmin(1)
        for j in range(k):
            if not np.any(new == j):
                far = int(D[np.arange(n), new].argmax())
                new[far] = j
        if lab is not None and np.array_equal(new, lab):
            break
        lab = new
        C = np.array([X[lab == j].mean(0) for j in range(k)])
    return lab


def _modularity(B, lab, m):
    S = (lab[:, None] == np.unique(lab)[None, :]).astype(float)
    return float(np.trace(S.T @ B @ S) / (2 * m))


def _dosplit(A, rng, nreps=50):
    Abar = (A + A.T) / 2
    m = A.sum() / 2
    k_in, k_out = A.sum(0), A.sum(1)
    P = np.outer(k_out, k_in) / k_in.sum()
    B = Abar - (P + P.T) / 2
    eg, V = np.linalg.eigh(B)
    Vpos = V[:, eg > 1e-3]
    ndivs = Vpos.shape[1]
    Q = np.zeros((nreps, ndivs))
    G = np.zeros((A.shape[0], nreps * ndivs), int)
    qmax = []
    for j in range(ndivs):
        for r in range(nreps):
            lab = _kmeans(Vpos, j + 2, rng)
            G[:, j * nreps + r] = lab
            Q[r, j] = _modularity(B, lab, m)
        qmax.append(Q[:, j].max())
        if j > 1 and qmax[j] <= 0 and qmax[j - 1] <= 0:
            break
    return G, Q


def consensus_communities(A, rng, nreps=50, max_iter=50):
    """Functions/allevsplitConTransitive.m: k-means on the positive eigenvectors of the
    modularity matrix, consensus over the clusterings with Q > 0, repeated on the consensus
    matrix until thresholding it at the lower edge of its upper mode gives transitive groups.
    Returns group labels 1..k (zeros when nothing can be grouped)."""
    n = A.shape[0]
    Aorig = A
    for it in range(max_iter):
        G, Q = _dosplit(A, rng, nreps)
        if it == 0 and (G.size == 0 or np.all(Q <= 0)):
            return np.zeros(n, int)
        allowed = Q.T.ravel() > 0
        Gs = G[:, allowed]
        A = (Gs[:, None, :] == Gs[None, :, :]).mean(2)
        np.fill_diagonal(A, 0)
        w = A[np.triu_indices(n, 1)]
        w = w[w > 0]
        if np.all(w == 1):
            theta = -np.inf
        else:
            s = np.percentile(w, [5, 95], method="hazen")     # MATLAB prctile
            idx = _kmeans(w[:, None], 2, rng, start=s)
            hi = 0 if w[idx == 0].mean() > w[idx == 1].mean() else 1
            theta = w[idx == hi].min()
        Au = np.where(A < theta, 0, A)
        lab = np.zeros(n, int)
        g, trans = 1, True
        for i in range(n):
            if lab[i]:
                continue
            members = np.concatenate([[i], np.flatnonzero(Au[i] > 0)])
            if np.any(lab[members[1:]] > 0):
                trans = False
                break
            lab[members] = g
            g += 1
        if trans:
            return lab
    # not converged in 50 iterations: the code groups by any link of the consensus matrix
    lab = np.zeros(n, int)
    g = 1
    for i in range(n):
        if not lab[i]:
            lab[np.concatenate([[i], np.flatnonzero(A[i] > 0)])] = g
            g += 1
    return lab


def ensembles(rec, sd, rng, qt=0.01, t0=STIM_ON):
    """StaticEnsembles.m: consensus clustering of the spike trains from ``t0`` to the end.
    Returns the ids (1-based) of the neurons with spikes and their group labels."""
    trains = neuron_trains(rec)
    t_end = rec["t"].max()
    nb = int(np.floor((t_end - t0) / qt + 1e-9)) + 1
    sig = int(round(sd / qt))
    x = np.arange(-5 * sig, 5 * sig + 1)
    h = np.exp(-x ** 2 / (2 * sig ** 2))
    h /= h.sum()
    ids, F = [], []
    for i, tr in enumerate(trains):
        tr = tr[(tr >= t0) & (tr <= t_end)]
        if tr.size == 0:
            continue
        c = np.bincount(np.round((tr - t0) / qt).astype(int), minlength=nb)[:nb].astype(float)
        F.append(np.convolve(c, h, "same"))
        ids.append(i + 1)
    F = np.array(F)
    S = np.corrcoef(F)
    S[S < 0] = 0
    np.fill_diagonal(S, 0)
    n = len(ids)
    if n < 6 or (S != 0).sum() <= np.log(n):
        return np.array(ids), np.zeros(n, int)
    return np.array(ids), consensus_communities(S, rng)


def _acorr(ts, maxlag=20, binsize=1.0):
    """Functions/spike_xcorr.m: histogram of all spike-time differences within maxlag, on MATLAB
    hist centres -maxlag:binsize:maxlag."""
    centres = np.arange(-maxlag, maxlag + binsize / 2, binsize)
    if ts.size < 2:
        return np.zeros(centres.size)
    edges = np.concatenate([[-maxlag], (centres[:-1] + centres[1:]) / 2, [maxlag]])
    q = np.searchsorted(ts, (ts[:, None] + edges[None, :]).ravel(), "left").reshape(ts.size, -1)
    q[:, -1] = np.searchsorted(ts, ts + maxlag, "right")
    return (q[:, 1:] - q[:, :-1]).sum(0).astype(float)


def _shuffle_intervals(ts, T, dt, rng):
    """Functions/shuffle_intervals.m for one train: intervals permuted, start drawn at random in
    the free time and quantised to dt; raises after 20 failed attempts, as the code."""
    iei = np.diff(ts)
    free = (ts[0] - T[0]) + (T[1] - ts[-1])
    for _ in range(21):
        start = T[0] + np.ceil(rng.random() * free / dt) * dt
        out = np.concatenate([[start], start + np.cumsum(iei[rng.permutation(iei.size)])])
        if out.max() <= T[1]:
            return out
    raise RuntimeError("cannot shuffle")


def acorr_type(ts, T, rng, n_perm=100, qt=0.001, n_thresh=2, p_thresh=3):
    """Analyse_Spike_Train_Properties.m and Types_of_Ensemble_Across_Dataset.m: type of an
    ensemble from its pooled spikes, 1 tonic (no peak, no trough), 2 oscillator (both),
    3 burster (peak only), 4 pauser (trough only)."""
    ts = np.sort(ts)
    A = _acorr(ts)
    try:
        perm = np.array([_acorr(np.sort(_shuffle_intervals(ts, T, qt, rng))) for _ in range(n_perm)])
        with np.errstate(divide="ignore", invalid="ignore"):
            Z = (A - perm.mean(0)) / perm.std(0, ddof=1)
    except RuntimeError:
        Z = np.full(A.size, np.nan)
    Z[(Z.size + 1) // 2 - 1] = 0
    neg = np.any(np.diff(np.flatnonzero(Z < -n_thresh)) == 1)
    pos = np.any(np.diff(np.flatnonzero(Z > p_thresh)) == 1)
    return {(False, False): 1, (True, True): 2, (True, False): 3, (False, True): 4}[(bool(pos), bool(neg))]


def type_neurons(args):
    """Ensembles and the type of every neuron of one recording (0 for neurons without spikes
    after onset). The pooled spikes of an ensemble are its neurons' spikes from onset, each
    neuron's last spike left out, as the code pools ts(1:end-1)."""
    rec, sd, seed = args
    rng = np.random.default_rng(seed)
    ids, lab = ensembles(rec, sd, rng)
    trains = neuron_trains(rec)
    T = (STIM_ON, float(rec["t"].max()))
    types = np.zeros(len(trains), int)
    groups = []
    for g in np.unique(lab[lab > 0]):
        members = ids[lab == g]
        pooled = np.concatenate([trains[i - 1][trains[i - 1] >= STIM_ON][:-1] for i in members])
        ty = acorr_type(pooled, T, rng)
        types[members - 1] = ty
        groups.append({"size": int(members.size), "type": ty, "spikes": int(pooled.size)})
    return {"file": rec["file"], "prep": rec["prep"], "bout": rec["bout"], "types": types,
            "groups": groups, "n_clustered": int(ids.size), "ungrouped": bool(np.all(lab == 0))}


def run_types(recs, sds, seed=7, workers=4):
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    jobs = [(r, float(s), seed * 1000 + i) for i, (r, s) in enumerate(zip(recs, sds))]
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
        return list(ex.map(type_neurons, jobs))
