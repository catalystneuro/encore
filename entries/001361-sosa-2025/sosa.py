"""Loading and measures for dandiset 001361 (Sosa, Plitt & Giocomo 2025, Nature Neuroscience).

Each NWB file holds one imaging session of one mouse: Suite2p fluorescence (F), neuropil (Fneu),
deconvolved activity, ROI masks and an `iscell` column, and behaviour resampled to the imaging
frames (position, speed, licks, reward, trial number, trial start and teleport flags). The file's
`identifier` ends with the scene name (for example `Env1_LocationB_to_A`), which names the
environment and the reward zone before and after the switch.

Where each parameter comes from is given next to it:
- "Methods, <section>": the paper's Methods, taken for a detail the claims file does not give
  (protocol, author step 1.6).
- "claims": the criterion of a claim in claims/001361/.
- "code": the paper's code, github.com/GiocomoLab/Sosa_et_al_2024 at commit adf0f9e, as the claims
  file or the Methods point to it.
- "assumption": a choice the paper does not make, said why.
- "standard": a choice that cannot change a result.
"""
import json
import urllib.request

import h5py
import numpy as np
import remfile
import requests
import scipy.ndimage as ndi
import scipy.sparse as sps

DANDISET = "001361"
VERSION = "0.251124.0550"     # see the notebook header for why this version and not 0.250406.0045
CITED_VERSION = "0.250406.0045"
API = "https://api.dandiarchive.org/api"

TRACK = 450.0                 # cm, Methods, Hidden reward zone task
NBINS = 45                    # 10 cm bins, Methods, Place cell identification
ZONE_START = {"A": 80.0, "B": 200.0, "C": 320.0}   # Methods, Hidden reward zone task
ZONE_LEN = 50.0
SWITCH_DAYS = [3, 5, 7, 8, 10, 12, 14]             # Methods, Hidden reward zone task
STAY_DAYS = [1, 2, 4, 6, 9, 11, 13]
N_PRE = 30                    # "Each switch occurred after 30 trials", Methods
SPEED_THR = 2.0               # cm/s, Methods, Place cell identification
FS = 15.5                     # imaging rate per plane, Methods, 2P imaging
RAD50 = 2 * np.pi * 50 / TRACK   # 0.698 rad, Methods, Quantification of RR remapping


# ---------------------------------------------------------------- archive access
def list_assets(version=VERSION):
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=500"
    out = []
    import time
    while url:
        for k in range(5):
            try:
                with urllib.request.urlopen(url, timeout=60) as r:
                    d = json.load(r)
                break
            except OSError:
                if k == 4:
                    raise
                time.sleep(10 * (k + 1))
        out += d["results"]
        url = d.get("next")
    return {a["path"]: a for a in out}


def session_table(version=VERSION):
    """One row per file: mouse, day, asset id, size."""
    rows = []
    for path, a in list_assets(version).items():
        sub = path.split("/")[0].replace("sub-", "")
        day = int(path.split("_ses-")[1].split("_")[0])
        rows.append(dict(path=path, mouse=sub, day=day, asset_id=a["asset_id"], size=a["size"]))
    return sorted(rows, key=lambda r: (int(r["mouse"][1:]), r["day"]))


def open_asset(asset_id, tries=5):
    """Open a file for streaming; a dropped connection is retried (standard)."""
    import time
    url = f"{API}/assets/{asset_id}/download/"
    for k in range(tries):
        try:
            s3 = requests.head(url, allow_redirects=True, timeout=60).url
            return h5py.File(remfile.File(s3), "r")
        except (requests.exceptions.RequestException, OSError):
            if k == tries - 1:
                raise
            time.sleep(10 * (k + 1))


B = "processing/behavior/BehavioralTimeSeries/"
O = "processing/ophys/"


def scene_of(f):
    return f["identifier"][()].decode().rstrip("/").split("/")[-1]


def parse_scene(scene):
    """'Env1_LocationB_to_A' -> (['Env1','Env1'], ['B','A']); 'Env1_B_to_Env2_C' -> (['Env1','Env2'], ['B','C'])."""
    parts = scene.split("_")
    if "to" not in parts:
        env, loc = parts[0], parts[1].replace("Location", "")
        return [env, env], [loc, loc]
    i = parts.index("to")
    pre, post = parts[:i], parts[i + 1:]
    env0 = pre[0]
    z0 = pre[1].replace("Location", "")
    if len(post) == 1:
        return [env0, env0], [z0, post[0]]
    return [env0, post[0]], [z0, post[1].replace("Location", "")]


def load_behavior(f):
    keys = ["position", "speed", "lick", "trial number", "trial_start", "teleport", "reward_zone",
            "environment", "autoreward", "scanning"]
    d = {k: f[B + k + "/data"][:] for k in keys}
    d["t"] = f[B + "position/timestamps"][:]
    d["reward_t"] = f[B + "Reward/timestamps"][:]
    return d


def trial_bounds(beh, n):
    """Trials as the paper's code takes them: from each trial start to the next teleport (code,
    spatial.py place cell calc, 'each trial is from start to teleport'); only complete trials, and
    frames beyond the n imaging frames are dropped."""
    starts = np.where(beh["trial_start"][:n] > 0)[0]
    tele = np.where(beh["teleport"][:n] > 0)[0]
    out = []
    for s in starts:
        e = tele[tele > s]
        if len(e):
            out.append((s, e[0]))
    # drop a start whose teleport belongs to a later start
    out2 = []
    for i, (s, e) in enumerate(out):
        if i + 1 < len(out) and out[i + 1][0] < e:
            continue
        out2.append((s, e))
    return np.array(out2, dtype=int)


# ---------------------------------------------------------------- dF/F
def dff_trials(F, Fneu, bounds, neu_coef=0.7, win=300, sig_base=15, sig_out=2):
    """dF/F as the Methods give it (Calcium data processing): baseline within each trial by a
    maximin over a 20 s window, (F - baseline)/|baseline|, smoothed by a 2-sample Gaussian.
    Neuropil subtraction with coefficient 0.7 and the neuropil mean of the trial added back, a
    15-sample Gaussian before the maximin and a 300-sample window are the code's
    (preprocessing.py dff, utilities.default_dff_method), which the Methods do not state.
    F and Fneu are frames x cells. Frames outside trials are NaN."""
    out = np.full(F.shape, np.nan, dtype=np.float32)
    for s, e in bounds:
        f = F[s:e].astype(np.float64) - neu_coef * Fneu[s:e]
        f = f + neu_coef * Fneu[s:e].mean(0, keepdims=True)
        w = min(win, e - s)
        base = ndi.gaussian_filter1d(f, sig_base, axis=0, mode="nearest")
        base = ndi.minimum_filter1d(base, w, axis=0, mode="nearest")
        base = ndi.maximum_filter1d(base, w, axis=0, mode="nearest")
        d = (f - base) / np.abs(base)
        out[s:e] = ndi.gaussian_filter1d(d, sig_out, axis=0, mode="nearest")
    return out


# ---------------------------------------------------------------- deconvolution
from numba import njit, prange


@njit(cache=True)
def _oasis_trace(F, v, w, t, l, s, tau, fs):
    NT = F.shape[0]
    g = -1. / (tau * fs)
    it = 0
    ip = 0
    while it < NT:
        v[ip], w[ip], t[ip], l[ip] = F[it], 1, it, 1
        while ip > 0:
            if v[ip - 1] * np.exp(g * l[ip - 1]) > v[ip]:
                f1 = np.exp(g * l[ip - 1])
                f2 = np.exp(2 * g * l[ip - 1])
                wnew = w[ip - 1] + w[ip] * f2
                v[ip - 1] = (v[ip - 1] * w[ip - 1] + v[ip] * w[ip] * f1) / wnew
                w[ip - 1] = wnew
                l[ip - 1] = l[ip - 1] + l[ip]
                ip -= 1
            else:
                break
        it += 1
        ip += 1
    s[t[1:ip]] = v[1:ip] - v[:ip - 1] * np.exp(g * l[:ip - 1])


@njit(parallel=True, cache=True)
def _oasis_matrix(F, tau, fs):
    NN, NT = F.shape
    S = np.zeros((NN, NT), dtype=np.float32)
    for n in prange(NN):
        v = np.zeros(NT)
        w = np.zeros(NT)
        t = np.zeros(NT, dtype=np.int64)
        l = np.zeros(NT)
        s = np.zeros(NT)
        _oasis_trace(F[n], v, w, t, l, s, tau, fs)
        S[n] = s
    return S


def events_from_dff(dff, bounds, tau=0.7, fs=FS):
    """Deconvolved activity as the Methods give it (Calcium data processing): OASIS on dF/F with
    a canonical calcium kernel, as in Suite2p, trial by trial as the code does
    (preprocessing.dff, deconvolve=True, tau 0.7 its default; the frame rate per plane, 15.5 Hz).
    This is Suite2p's OASIS (suite2p.extraction.dcnv.oasis), written out here. The dataset's own
    'Deconvolved' series is not this signal (see the notebook's data check)."""
    E = np.full(dff.shape, np.nan, dtype=np.float32)
    for s, e in bounds:
        E[s:e] = _oasis_matrix(np.ascontiguousarray(dff[s:e].T.astype(np.float64)), tau, fs).T
    return E


# ---------------------------------------------------------------- binning
def bin_index(pos, nb=NBINS, lo=0.0, hi=TRACK):
    b = np.floor((pos - lo) / (hi - lo) * nb).astype(int)
    b[(pos < lo) | (pos > hi)] = -1
    return np.clip(b, -1, nb - 1)


def circ_bin_index(pos, nbins_circ=45, code_bins=False):
    """Position in cm to circular bins over -pi..pi (0 cm -> -pi, 450 cm -> pi), Methods,
    Quantification of RR remapping. Methods bin size 2pi/45; with code_bins the code's
    np.linspace(-pi, pi, 45) step of 2pi/44, with bin edges from -pi (dayData.py:954-967). With
    that step the track fills 44 bins, so the 45th code-bin centre (beyond pi) stays empty; this
    touches only the code-bin variants."""
    th = 2 * np.pi * pos / TRACK - np.pi
    if code_bins:
        bs = 2 * np.pi / 44
        b = np.floor((th + np.pi) / bs).astype(int)
        b = np.clip(b, 0, 44)
        centers = -np.pi + bs / 2 + bs * np.arange(45)
    else:
        bs = 2 * np.pi / 45
        b = np.clip(np.floor((th + np.pi) / bs).astype(int), 0, 44)
        centers = -np.pi + bs / 2 + bs * np.arange(45)
    b[(pos < 0) | (pos > TRACK)] = -1
    return b, centers


def trial_matrix(X, bidx, bounds, speed, nb=NBINS, speed_thr=SPEED_THR):
    """Mean activity per trial and bin (trials x bins x cells), frames at speed < 2 cm/s
    excluded (Methods, Place cell identification). Also returns occupancy in frames."""
    nt = len(bounds)
    rows, cols = [], []
    for t, (s, e) in enumerate(bounds):
        fr = np.arange(s, e)
        ok = (bidx[fr] >= 0) & (speed[fr] >= speed_thr)
        fr = fr[ok]
        rows.append(t * nb + bidx[fr])
        cols.append(fr)
    rows = np.concatenate(rows)
    cols = np.concatenate(cols)
    occ = np.bincount(rows, minlength=nt * nb).astype(float)
    M = sps.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(nt * nb, X.shape[0]))
    S = M @ np.nan_to_num(X)
    with np.errstate(invalid="ignore", divide="ignore"):
        tm = S / occ[:, None]
    tm[occ == 0] = np.nan
    return tm.reshape(nt, nb, -1), occ.reshape(nt, nb)


# ---------------------------------------------------------------- spatial information
def _si(fmap, p):
    """SI = sum_i p_i (f_i/f) log2(f_i/f), f = sum_i f_i p_i (Methods, Place cell identification).
    fmap bins x cells."""
    fmap = np.where(np.isnan(fmap), 0, fmap)
    fbar = (fmap * p[:, None]).sum(0)
    with np.errstate(divide="ignore", invalid="ignore"):
        r = fmap / fbar
        v = np.where(r > 0, r * np.log2(r), 0.0)
    si = (p[:, None] * v).sum(0)
    si[~np.isfinite(si)] = 0
    return si


def spatial_info_shuffle(X, pos, speed, bounds, rng, nperm=100, min_shift=15, nb=NBINS):
    """A variant since round 1 of verification; the main procedure is spatial_info_shuffle_code.
    SI and its shuffle for one trial set (Methods, Place cell identification): occupancy p_i
    from the per-trial occupancy fractions summed over trials; f_i the trial-averaged activity
    per bin; the shuffle circularly shifts activity against position within each trial by a
    random amount between ~1 s (15 samples) and the trial length, 100 times. Returns the real
    SI (cells) and the shuffled SI (nperm x cells)."""
    bidx = bin_index(pos, nb)
    nt = len(bounds)
    # weights: per trial, frames at speed >= thr in bin b get 1/(occ[t,b] * ntrials_visiting[b])
    occ = np.zeros((nt, nb))
    fr_all, b_all, t_all = [], [], []
    for t, (s, e) in enumerate(bounds):
        fr = np.arange(s, e)
        ok = (bidx[fr] >= 0) & (speed[fr] >= SPEED_THR)
        fr = fr[ok]
        b = bidx[fr]
        occ[t] = np.bincount(b, minlength=nb)
        fr_all.append(fr); b_all.append(b); t_all.append(np.full(len(fr), t))
    fr_all = np.concatenate(fr_all); b_all = np.concatenate(b_all); t_all = np.concatenate(t_all)
    nvis = (occ > 0).sum(0)
    w = 1.0 / (occ[t_all, b_all] * nvis[b_all])
    tot = occ.sum(1, keepdims=True)
    p = (occ / np.where(tot > 0, tot, 1)).sum(0)
    p = p / p.sum()
    Xn = np.nan_to_num(X)
    M = sps.csr_matrix((w, (b_all, fr_all)), shape=(nb, X.shape[0]))
    si = _si(M @ Xn, p)
    # shuffles: roll activity within each trial (start..teleport); the frames used and the
    # weights stay, the activity they read is shifted
    shuf = np.zeros((nperm, X.shape[1]))
    lens = bounds[:, 1] - bounds[:, 0]
    for k in range(nperm):
        src = np.empty(len(fr_all), dtype=int)
        shifts = np.array([rng.integers(min(min_shift, L - 1), L) if L > 1 else 0 for L in lens])
        s0 = bounds[t_all, 0]
        L = lens[t_all]
        src = s0 + (fr_all - s0 + shifts[t_all]) % L
        Mk = sps.csr_matrix((w, (b_all, src)), shape=(nb, X.shape[0]))
        shuf[k] = _si(Mk @ Xn, p)
    return si, shuf


def _si_code(fmap, occ):
    """SI as TwoPUtils computes it (spatial_analyses.spatial_info, called by the paper's
    spatial.py:1260-1289): the rate map minus its minimum over all bins and cells, plus 0.001,
    then the Methods' formula. fmap bins x cells, occ the occupancy probabilities."""
    P = fmap - np.nanmin(fmap) + 0.001
    mr = (P * occ[:, None]).sum(0, keepdims=True)
    Pn = P / mr
    return np.nansum(Pn * occ[:, None] * np.log2(Pn), 0)


def spatial_info_shuffle_code(X, pos, speed, bounds, rng, nperm=100, nb=NBINS, min_shift=15):
    """SI and its shuffle as the paper's code runs them (TwoPUtils spatial_analyses.place_cells_calc
    and trial_matrix with perm=True, github.com/GiocomoLab/TwoPUtils at commit 3714d32, which the
    paper's spatial.py:1260-1289 calls; the claims criterion cites those lines). Frames at speed
    < 2 cm/s have their activity set to NaN and their position to -1000; in each shuffle the
    position of each trial (start to teleport) is rolled by np.random.randint(15, trial length),
    one offset per trial shared by all cells, so the speed mask on position moves with it while
    the mask on activity stays. f_i is the mean over trials of the per-trial bin means; occupancy
    is the per-trial occupancy fractions summed over trials, plus 0.001, normalized; SI is
    `_si_code`. Returns the real SI (cells) and the shuffled SI (nperm x cells)."""
    bidx = bin_index(pos, nb)
    Xn = np.nan_to_num(X)
    act_ok = speed >= SPEED_THR
    src_ok = (bidx >= 0) & act_ok
    nt = len(bounds)

    def one(shifts):
        fr_all, b_all, t_all = [], [], []
        cnt = np.zeros((nt, nb))
        for t, (s, e) in enumerate(bounds):
            L = e - s
            src = s + (np.arange(L) - shifts[t]) % L      # np.roll(pos_t, shift)
            ok = act_ok[s:e] & src_ok[src]
            fr = np.arange(s, e)[ok]
            b = bidx[src][ok]
            cnt[t] = np.bincount(b, minlength=nb)
            fr_all.append(fr); b_all.append(b); t_all.append(np.full(len(fr), t))
        fr_all = np.concatenate(fr_all); b_all = np.concatenate(b_all); t_all = np.concatenate(t_all)
        nvis = (cnt > 0).sum(0)
        w = 1.0 / (cnt[t_all, b_all] * nvis[b_all])
        fmap = sps.csr_matrix((w, (b_all, fr_all)), shape=(nb, X.shape[0])) @ Xn
        fmap[nvis == 0] = np.nan
        occ = (cnt / (cnt.sum(1, keepdims=True) + 1e-3)).sum(0) + 1e-3
        return _si_code(fmap, occ / occ.sum())

    si = one(np.zeros(nt, dtype=int))
    lens = bounds[:, 1] - bounds[:, 0]
    shuf = np.array([one(np.array([rng.integers(min(min_shift, L - 1), L) if L > 1 else 0
                                   for L in lens])) for _ in range(nperm)])
    return si, shuf


def pop_shuffle_p(si, shuf):
    """p = fraction of all shuffled SI values (all cells pooled) at or above the cell's SI
    (code, spatial.p_from_pop_shuffle; Methods 'pooled across cells')."""
    allv = np.sort(shuf.ravel())
    return 1 - np.searchsorted(allv, si, side="left") / len(allv)


# ---------------------------------------------------------------- circular helpers
def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def cm_to_rad(x):
    return 2 * np.pi * x / TRACK - np.pi


def circmean(a, axis=None):
    return np.arctan2(np.nanmean(np.sin(a), axis=axis), np.nanmean(np.cos(a), axis=axis))


def circvar(a):
    """astropy circvar: 1 - R."""
    a = np.asarray(a)
    a = a[np.isfinite(a)]
    if len(a) == 0:
        return np.nan
    return 1 - np.hypot(np.mean(np.sin(a)), np.mean(np.cos(a)))


def corr_cc(a, b):
    """Circular-circular correlation of Kempter et al. 2012 (the paper's ref. 64, CINPLA
    phase-precession corr_cc)."""
    a = np.asarray(a); b = np.asarray(b)
    ma = np.arctan2(np.sum(np.sin(a)), np.sum(np.cos(a)))
    mb = np.arctan2(np.sum(np.sin(b)), np.sum(np.cos(b)))
    sa = np.sin(a - ma); sb = np.sin(b - mb)
    den = np.sqrt(np.sum(sa ** 2) * np.sum(sb ** 2))
    return np.sum(sa * sb) / den if den > 0 else np.nan


def circ_mtest_ci(a, alpha=0.05):
    """pycircstat mtest: the circular mean and its 1-alpha confidence interval
    (Zar, Biostatistical Analysis, eq. 26.24-26.25), as pycircstat.tests.mtest computes it."""
    from scipy.stats import chi2
    a = np.asarray(a)
    n = len(a)
    C = np.sum(np.cos(a)); S = np.sum(np.sin(a))
    R = np.hypot(C, S)
    r = R / n
    mu = np.arctan2(S, C)
    c2 = chi2.ppf(1 - alpha, 1)
    if r < 0.9 and r > np.sqrt(c2 / 2 / n):
        t = np.sqrt((2 * n * (2 * R ** 2 - n * c2)) / (4 * n - c2))
    elif r >= 0.9:
        t = np.sqrt(n ** 2 - (n ** 2 - R ** 2) * np.exp(c2 / n))
    else:
        return mu, np.nan, np.nan
    d = np.arccos(t / R)
    return mu, mu - d, mu + d


def xcorr_same(a, b):
    """scipy.signal.correlate(zscore(a), zscore(b), 'same') / (len - 1) along the last axis,
    with lags -22..22 for 45 bins (code, dayData.calc_field_xcorr)."""
    n = a.shape[-1]
    za = (a - np.nanmean(a, -1, keepdims=True)) / np.nanstd(a, -1, keepdims=True)
    zb = (b - np.nanmean(b, -1, keepdims=True)) / np.nanstd(b, -1, keepdims=True)
    za = np.nan_to_num(za); zb = np.nan_to_num(zb)
    lags = np.arange(-(n // 2), n - n // 2)
    out = np.zeros(np.broadcast(za, zb).shape[:-1] + (n,))
    for i, k in enumerate(lags):
        # correlate: c[k] = sum_m a[m + k] * b[m]
        if k >= 0:
            out[..., i] = (za[..., k:] * zb[..., :n - k]).sum(-1)
        else:
            out[..., i] = (za[..., :n + k] * zb[..., -k:]).sum(-1)
    return out / (n - 1), lags


# ---------------------------------------------------------------- clock checks
def clock_check_laser(F, beh, bounds, n, lags=range(-60, 61)):
    """In sessions where the laser was lowered during the teleport (Methods, 2P imaging), the
    population fluorescence drops in the teleport. Returns the fraction of frames that are dark,
    and the lag (imaging frame = behaviour frame + lag) at which dark frames best agree with
    teleport frames, with the agreement at that lag and at lag 0."""
    m = F[:, :min(F.shape[1], 200)].mean(1)
    dark = m < 0.6 * np.median(m)
    tele = np.zeros(n, bool)
    for t in range(len(bounds) - 1):
        tele[bounds[t, 1]:bounds[t + 1, 0]] = True
    out = dict(dark_frac=float(dark.mean()))
    if dark.mean() < 0.02:
        return out
    sc = {}
    for L in lags:
        i = np.arange(max(0, -L), min(n, n - L))
        sc[L] = np.mean(dark[i + L] == tele[i])
    best = max(sc, key=sc.get)
    out.update(best_lag=int(best), agree_best=float(sc[best]), agree0=float(sc[0]),
               agree_far=float(np.mean([sc[L] for L in (-60, 60)])))
    return out


def clock_check_maps(X, pos, spd, bounds, lags=(-300, -50, -10, 0, 10, 50, 300)):
    """Median over cells of the correlation between odd- and even-trial maps when the activity
    is shifted against the behaviour by `lag` frames (positive: activity later)."""
    out = {}
    nt = len(bounds)
    for L in lags:
        Xs = np.roll(X, -L, axis=0)
        tm, _ = trial_matrix(Xs, bin_index(pos), bounds, spd)
        a = np.nanmean(tm[0::2], 0); b = np.nanmean(tm[1::2], 0)
        a = a - np.nanmean(a, 0); b = b - np.nanmean(b, 0)
        r = np.nansum(a * b, 0) / np.sqrt(np.nansum(a * a, 0) * np.nansum(b * b, 0))
        out[L] = float(np.nanmedian(r))
    return out


# ---------------------------------------------------------------- one session
def read_ophys(f, n):
    """F, Fneu and deconvolved activity of the ROIs Suite2p marks as cells (iscell), planes
    pooled (Methods, Calcium data processing: 'planes were pooled for all analyses except those
    in Extended Data Fig. 7'), first n frames. Also ROI centroids, plane, and pixel lists."""
    ps = f[O + "ImageSegmentation/PlaneSegmentation/"]
    iscell = ps["iscell"][:, 0] > 0
    plane_idx = ps["planeIdx"][:]
    # single-plane files hold pixel masks, two-plane files (m17, m18) voxel masks with z
    key = "pixel_mask" if "pixel_mask" in ps else "voxel_mask"
    pm = ps[key][:]
    pmi = ps[key + "_index"][:].astype(np.int64)
    starts = np.r_[0, pmi[:-1]]
    planes = sorted(f[O + "Fluorescence"].keys())
    F, N, D, rois = [], [], [], []
    for p in planes:
        r = f[O + "Fluorescence/" + p + "/rois"][:]
        sel = iscell[r]
        F.append(f[O + "Fluorescence/" + p + "/data"][:n][:, sel])
        N.append(f[O + "Neuropil/" + p + "/data"][:n][:, sel])
        D.append(f[O + "Deconvolved/" + p + "/data"][:n][:, sel])
        rois.append(r[sel])
    rois = np.concatenate(rois)
    pix, cx, cy = [], [], []
    H, W = f[O + "Backgrounds_0/meanImg"].shape
    for i in rois:
        m = pm[starts[i]:pmi[i]]
        z = m["z"].astype(np.int64) if key == "voxel_mask" else 0
        # the masks' "x" indexes image rows (0..511) and "y" columns (0..795), as their ranges show
        pix.append((z * H * W + m["x"].astype(np.int64) * W + m["y"]).astype(np.int32))
        cx.append(m["x"].mean()); cy.append(m["y"].mean())
    mean_imgs = [f[O + f"Backgrounds_{k}/meanImg"][:] for k in range(len(planes))]
    return dict(F=np.concatenate(F, 1), Fneu=np.concatenate(N, 1), D=np.concatenate(D, 1),
                roi=rois, plane=plane_idx[rois], cx=np.array(cx), cy=np.array(cy), pix=pix,
                n_rois_total=len(iscell), n_iscell=int(iscell.sum()), mean_imgs=mean_imgs)


def trial_zone_from_flags(beh, bounds):
    """Zone of each rewarded trial read from the data: the position where the reward_zone flag
    first goes up in the trial, assigned to the nearest zone start. NaN when the flag never rises
    (omission trials, where no reward is given)."""
    out = []
    for s, e in bounds:
        fr = np.arange(s, e)
        z = fr[beh["reward_zone"][fr] > 0]
        if len(z) == 0:
            out.append("")
            continue
        p = beh["position"][z[0]]
        out.append(min(ZONE_START, key=lambda k: abs(ZONE_START[k] - p)) if p >= 60 else "")
    return np.array(out)


def behavior_per_trial(beh, bounds, zone_starts, n):
    """Per trial: licks and occupancy in 10 cm bins, speed in 2 cm bins, rewarded, sensor error,
    distance run in the teleport after the trial, lick positions."""
    pos = beh["position"]; spd = beh["speed"]; lick = beh["lick"]
    dt = np.median(np.diff(beh["t"]))
    nt = len(bounds)
    lick_cnt = np.zeros((nt, NBINS)); occ_t = np.zeros((nt, NBINS))
    spd2 = np.full((nt, 225), np.nan)
    rewarded = np.zeros(nt, bool); err = np.zeros(nt, bool)
    tele_dist = np.full(nt, np.nan)
    lick_pos = []
    for t, (s, e) in enumerate(bounds):
        fr = np.arange(s, e)
        b = bin_index(pos[fr])
        ok = b >= 0
        # sensor error: >30% of frames with a cumulative lick count > 2 (Methods, Quantification
        # of licking behavior)
        err[t] = np.mean(lick[fr] > 2) > 0.3
        lb = (lick[fr] > 0).astype(float)   # 'converted to a binary vector', Methods
        lick_cnt[t] = np.bincount(b[ok], weights=lb[ok], minlength=NBINS)
        occ_t[t] = np.bincount(b[ok], minlength=NBINS) * dt
        b2 = np.clip(np.floor(pos[fr] / 2).astype(int), -1, 224)
        ok2 = (pos[fr] >= 0) & (pos[fr] <= TRACK)
        sm = np.bincount(b2[ok2], weights=spd[fr][ok2], minlength=225)
        sc = np.bincount(b2[ok2], minlength=225)
        with np.errstate(invalid="ignore", divide="ignore"):
            spd2[t] = np.where(sc > 0, sm / sc, np.nan)
        t0, t1 = beh["t"][s], beh["t"][e]
        rewarded[t] = np.any((beh["reward_t"] >= t0) & (beh["reward_t"] <= t1))
        # teleport distance: speed integrated from the first teleport frame to the last frame
        # before the next trial start (Methods, Relationship between distance run ...)
        nxt = bounds[t + 1, 0] if t + 1 < nt else None
        if nxt is not None:
            tf = np.arange(e, nxt)
            tele_dist[t] = np.sum(spd[tf]) * dt
        lp = pos[fr][(lick[fr] > 0) & ok]
        lick_pos.append(lp)
    return dict(lick_cnt=lick_cnt, occ_t=occ_t, speed2=spd2, rewarded=rewarded, sensor_err=err,
                tele_dist=tele_dist, lick_pos=lick_pos)


def peaks_from_map(m, axis=0):
    """Bin of the maximum of a (bins x cells) map; NaN columns give -1."""
    allnan = np.all(np.isnan(m), axis=axis)
    p = np.nanargmax(np.where(np.isnan(m), -np.inf, m), axis=axis)
    p[allnan] = -1
    return p


def rr_xcorr(c0, c1, shift, rng, nperm=500, shift_hi=45):
    """RR cross-correlation criterion (Methods, Criteria to define RR cells; code,
    dayData.calc_field_xcorr). c0 trials x bins x cells (before), c1 (after), circular maps in
    track coordinates; c1 is rolled by `shift` bins so that the zone starts align. Each
    post-switch trial is circularly shifted by a random 1..shift_hi-1 bins (shift_hi=46 gives the
    Methods' 1 to 45; the code's np.random.randint(1, 45) gives 1 to 44), 500 times. Returns the
    lag of the highest cross-correlation that exceeds the shuffle's 97.5th percentile (NaN if
    none)."""
    c1 = np.roll(c1, shift, axis=1)
    m0 = np.nanmean(c0, 0).T            # cells x bins
    m1 = np.nanmean(c1, 0).T
    xc, lags = xcorr_same(m0, m1)       # cells x lags
    ncell = m0.shape[0]
    nt, nb = c1.shape[0], c1.shape[1]
    out = np.full(ncell, np.nan)
    if ncell == 0:
        return out, xc
    shifts = rng.integers(1, shift_hi, size=(nperm, nt))
    idx = (np.arange(nb)[None, None, :] - shifts[:, :, None]) % nb    # perm x trial x bins
    tix = np.arange(nt)[None, :, None]
    chunk = max(1, int(2e7 // (nperm * nt * nb)))
    for c0i in range(0, ncell, chunk):
        sl = slice(c0i, min(ncell, c0i + chunk))
        sub = np.moveaxis(c1[:, :, sl], 2, 0)          # cells x trials x bins
        sh = sub[:, tix, idx]                           # cells x perm x trials x bins
        with np.errstate(invalid="ignore"):
            msh = np.nanmean(sh, 2)                     # cells x perm x bins
        xs, _ = xcorr_same(m0[sl][:, None, :], msh)     # cells x perm x lags
        hi = np.nanpercentile(xs, 97.5, axis=1)
        for j, ci in enumerate(range(sl.start, sl.stop)):
            above = xc[ci] > hi[j]
            if np.any(above):
                out[ci] = lags[above][np.argmax(xc[ci][above])]
    return out, xc


def process_session(row, seed, nperm_si=100, with_rr=True, with_xcorr=True):
    """Everything the notebook needs from one session, reduced as it loads."""
    rng = np.random.default_rng(seed)
    f = open_asset(row["asset_id"])
    scene = scene_of(f)
    envs, zones = parse_scene(scene)
    beh = load_behavior(f)
    n_img = f[O + "Deconvolved/plane0/data"].shape[0]
    n = min(n_img, len(beh["position"]))
    bounds = trial_bounds(beh, n)
    nt = len(bounds)
    is_switch = zones[0] != zones[1] or envs[0] != envs[1]
    if is_switch:
        sets = [np.arange(min(N_PRE, nt)), np.arange(N_PRE, nt)]
    else:  # first and second halves on days without a switch (Methods, Place cell identification)
        h = nt // 2
        sets = [np.arange(h), np.arange(h, nt)]
    zs = [ZONE_START[z] for z in zones]
    flag_zone = trial_zone_from_flags(beh, bounds)
    res = dict(mouse=row["mouse"], day=row["day"], scene=scene, envs=envs, zones=zones,
               zone_starts=zs, n_img=n_img, n_beh=len(beh["position"]), n_trials=nt,
               sets=sets, flag_zone=flag_zone, is_switch=is_switch,
               beh=behavior_per_trial(beh, bounds, zs, n))
    if not with_rr:
        return res
    op = read_ophys(f, n)
    f.close()
    pos = beh["position"][:n]; spd = beh["speed"][:n]
    clock = clock_check_laser(op["F"], beh, bounds, n)
    dff = dff_trials(op["F"], op["Fneu"], bounds)
    D_ds = op["D"].astype(np.float32)          # the dataset's deconvolved series (variant)
    D = events_from_dff(dff, bounds)           # the Methods' deconvolved activity (main)
    del op["F"], op["Fneu"]
    ncell = D.shape[1]
    # putative interneurons: Pearson r > 0.5 between dF/F and running speed (Methods)
    inn = np.isfinite(dff[:, 0])
    z = (dff[inn] - dff[inn].mean(0)) / dff[inn].std(0)
    sz = (spd[inn] - spd[inn].mean()) / spd[inn].std()
    r_speed = (z * sz[:, None]).mean(0)
    is_int = r_speed > 0.5
    clock["split_half"] = clock_check_maps(D, pos, spd, bounds)
    # spatial information on the deconvolved activity, per trial set, as the paper's code runs it
    si, sig, shuf_q95 = [], [], []
    for s in sets:
        v, sh = spatial_info_shuffle_code(D, pos, spd, bounds[s], rng, nperm=nperm_si)
        p = pop_shuffle_p(v, sh)
        si.append(v); sig.append(p < 0.05); shuf_q95.append(np.percentile(sh, 95))
    # variants, from a generator of their own so that they do not change the main result:
    # (1) the procedure of the first round (activity rolled against fixed frames, the Methods'
    # SI without the code's offset); (2) the main procedure on the dataset's own deconvolved
    # series; (3) the main procedure on OASIS events with tau = 1.0 s. Switch days only, where
    # the notebook uses them
    rng_v = np.random.default_rng(seed + 10 ** 6)
    sig_meth, sig_ds, sig_tau1 = [], [], []
    if is_switch:
        for s in sets:
            v, sh = spatial_info_shuffle(D, pos, spd, bounds[s], rng_v, nperm=nperm_si)
            sig_meth.append(pop_shuffle_p(v, sh) < 0.05)
            v, sh = spatial_info_shuffle_code(D_ds, pos, spd, bounds[s], rng_v, nperm=nperm_si)
            sig_ds.append(pop_shuffle_p(v, sh) < 0.05)
        D1 = events_from_dff(dff, bounds, tau=1.0)
        for s in sets:
            v, sh = spatial_info_shuffle_code(D1, pos, spd, bounds[s], rng_v, nperm=nperm_si)
            sig_tau1.append(pop_shuffle_p(v, sh) < 0.05)
        del D1
    # linear trial matrices
    lb = bin_index(pos)
    tm_dff, occ = trial_matrix(dff, lb, bounds, spd)
    tm_dec, _ = trial_matrix(D, lb, bounds, spd)
    lin_centers = 5 + 10 * np.arange(NBINS)
    mean_dff = [np.nanmean(tm_dff[s], 0) for s in sets]
    peak_lin = [lin_centers[peaks_from_map(m)] for m in mean_dff]
    # per-trial mean dF/F (mean over bins), for appearing / disappearing
    trial_mean = [np.nanmean(tm_dff[s], 1) for s in sets]      # trials x cells
    # circular maps, Methods bins (2pi/45) and code bins (2pi/44)
    circ = {}
    for key, cb in [("m", False), ("c", True)]:
        bidx, centers = circ_bin_index(pos, code_bins=cb)
        tmc, _ = trial_matrix(dff, bidx, bounds, spd)
        bs = centers[1] - centers[0]
        pk = [peaks_from_map(np.nanmean(tmc[s], 0)) for s in sets]
        rz = [cm_to_rad(z) for z in zs]
        # shift aligning the zone starts (code, calc_field_xcorr)
        if zs[0] > zs[1]:
            shift = int(np.round((rz[0] - rz[1]) / bs))
        elif zs[1] > zs[0]:
            shift = -int(np.round((rz[1] - rz[0]) / bs))
        else:
            shift = 0
        rel = [wrap(centers[pk[k]] - rz[k]) for k in range(2)]
        pc_or = (sig[0] | sig[1]) & ~is_int
        cand = pc_or & (np.abs(wrap(rel[1] - rel[0])) <= RAD50 + 1e-9)
        lag_m = np.full(ncell, np.nan); lag_c = np.full(ncell, np.nan)
        ci = np.where(cand)[0]
        if len(ci) and with_xcorr:
            lag_m[ci], _ = rr_xcorr(tmc[sets[0]][:, :, ci], tmc[sets[1]][:, :, ci], shift, rng,
                                    shift_hi=46)
            lag_c[ci], _ = rr_xcorr(tmc[sets[0]][:, :, ci], tmc[sets[1]][:, :, ci], shift, rng,
                                    shift_hi=45)
        m0 = np.nanmean(tmc[sets[0]], 0); m1 = np.nanmean(tmc[sets[1]], 0)
        # reward-aligned and track-coordinate correlations of the trial-averaged maps
        m1r = np.roll(m1, shift, axis=0)
        def pear(a, b):
            ok = np.isfinite(a) & np.isfinite(b)
            a = np.where(ok, a, np.nan); b = np.where(ok, b, np.nan)
            a = a - np.nanmean(a, 0); b = b - np.nanmean(b, 0)
            return np.nansum(a * b, 0) / np.sqrt(np.nansum(a * a, 0) * np.nansum(b * b, 0))
        odd = sets[0][0::2]     # trials 1, 3, 5 ... counted from 1
        even = sets[0][1::2]
        circ[key] = dict(
            centers=centers, shift=shift, peak0=pk[0], peak1=pk[1], rel0=rel[0], rel1=rel[1],
            cand=cand, lag_meth=lag_m, lag_code=lag_c,
            r_rew=pear(m0, m1r), r_track=pear(m0, m1),
            peak_odd=peaks_from_map(np.nanmean(tmc[odd], 0)),
            peak_even=peaks_from_map(np.nanmean(tmc[even], 0)),
            # per-trial peaks (trials x cells), for the teleport-distance analysis
            trial_peak=np.where(np.all(np.isnan(tmc), 1), -1,
                                np.nanargmax(np.where(np.isnan(tmc), -np.inf, tmc), 1)).astype(np.int16),
            map0=m0.astype(np.float32), map1=m1.astype(np.float32),
        )
    res.update(dict(
        n_cells=ncell, n_rois_total=op["n_rois_total"], is_int=is_int, r_speed=r_speed,
        si=si, sig=sig, sig_ds=sig_ds, sig_meth=sig_meth, sig_tau1=sig_tau1, shuf_q95=shuf_q95, clock=clock, peak_lin=peak_lin, trial_mean=trial_mean,
        mean_dff=mean_dff, mean_dec=[np.nanmean(tm_dec[s], 0) for s in sets],
        circ=circ, roi=op["roi"], plane=op["plane"], cx=op["cx"], cy=op["cy"], pix=op["pix"],
        mean_imgs=op["mean_imgs"],
        # per-trial deconvolved maps of place cells, for the field analyses (float16)
        pc_idx=np.where((sig[0] | sig[1]) & ~is_int)[0],
        tm_dec_pc=(tm_dec[:, :, (sig[0] | sig[1]) & ~is_int].astype(np.float16) if is_switch
                   else None),
        # individual place fields from the raw activity (place_fields_raw), switch days
        fields_raw=(place_fields_raw(D, pos, spd, bounds, sets, np.where((sig[0] | sig[1]) & ~is_int)[0])
                    if is_switch else None),
        dec_mean=np.nanmean(D, 0),
        dff_range=(float(np.nanpercentile(dff, 1)), float(np.nanpercentile(dff, 99))),
        dec_range=(float(np.nanmin(D)), float(np.nanpercentile(D, 99))),
        ds_dec_range=(float(np.nanmin(D_ds)), float(np.nanpercentile(D_ds, 99))),
        r_events_vs_ds=float(np.nanmedian([np.corrcoef(D[inn, i], D_ds[inn, i])[0, 1]
                                           for i in range(0, ncell, max(1, ncell // 50))])),
    ))
    return res


def nansmooth(a, sig, axis=-1):
    """Gaussian smoothing that does not spread NaNs, as the paper's utilities.nansmooth."""
    nan = np.isnan(a)
    one = np.where(nan, 0.001, 1.0)
    return (ndi.gaussian_filter1d(np.where(nan, 0, a), sig, axis=axis)
            / ndi.gaussian_filter1d(one, sig, axis=axis))


def _com(w, x):
    """utilities.center_of_mass: sum |w| x / sum |w|, NaNs ignored."""
    w = np.abs(w)
    s = np.nansum(w)
    return np.nansum(w * x) / s if s > 0 else np.nan


def place_fields_raw(D, pos, spd, bounds, sets, cells, n_std=1, n_trials_thr=8, field_thr=0.2):
    """Place fields as the Methods give them (Place field definition and inclusion criteria;
    Formation lap identification and backwards shifting), following the paper's code
    (Ext3_FieldQuant.md, find_sig_active_fields, n_std 1, n_trials_thr 8, field_thr 0.2, sigma 1
    bin; spatial.field_from_thresh). Per cell and set (the 30 trials before, the last 30 after):
    the trial-averaged binned activity (speed >= 2 cm/s), smoothed by 1 bin (10 cm); fields are
    runs of >= 2 bins above min + 0.2 (max - min); a field is kept when on >= 8 trials the raw,
    unbinned activity exceeds the mean + 1 s.d. of the raw activity of the set (frames at speed
    >= 2 cm/s from the set's first trial start to its last teleport) at a position strictly
    between the field's first and last bin centres. Positions are resolved to 5 cm, which places
    each frame exactly against the bin centres. The formation lap is the first trial, in the
    first 5-trial window with >= 3 such trials, on which the smoothed binned activity exceeds
    its mean + 1 s.d. over all post-switch trials within the field +/- 10 cm; the shift is the
    field's centre of mass in the smoothed mean of the last 30 trials minus the centre of mass of
    the raw activity within the field +/- 10 cm on the formation lap. Returns per cell: number of
    fields before and after, the offset between the two field centres (rad) when there are two,
    the primary field's (the one with the highest mean) formation lap (from 1) and shift (cm)."""
    nb = NBINS
    cen = 5.0 + 10 * np.arange(nb)
    X = D[:, cells].astype(np.float64)
    Xs = np.where((spd >= SPEED_THR)[:, None], X, np.nan)
    bidx = bin_index(pos)
    tm, _ = trial_matrix(X, bidx, bounds, spd)            # trials x bins x cells
    tms = nansmooth(tm, 1, axis=1)
    half = np.clip(np.floor(pos / 5).astype(int), -1, 2 * nb - 1)
    half[(pos < 0) | (pos > TRACK)] = -1
    ncell = len(cells)
    out = dict(n0=np.zeros(ncell, int), n1=np.zeros(ncell, int), off0=np.full(ncell, np.nan),
               off1=np.full(ncell, np.nan), form_lap=np.full(ncell, np.nan),
               shift_cm=np.full(ncell, np.nan))
    s0 = np.asarray(sets[0])[:30]
    s1 = np.asarray(sets[1])
    s1l = s1[-30:]
    kept = {}
    for key, st in (("0", s0), ("1", s1l)):
        if len(st) == 0:
            continue
        a, b = bounds[st[0], 0], bounds[st[-1], 1]
        thr = np.nanmean(Xs[a:b], 0) + n_std * np.nanstd(Xs[a:b], 0)
        act = np.zeros((len(st), 2 * nb, ncell), bool)       # any raw frame above thr, 5 cm bins
        for i, t in enumerate(st):
            fr = np.arange(bounds[t, 0], bounds[t, 1])
            ok = half[fr] >= 0
            sig = Xs[fr[ok]] > thr[None, :]
            np.logical_or.at(act[i], half[fr[ok]], sig)
        mean = nansmooth(np.nanmean(tm[st], 0), 1, axis=0)  # bins x cells
        for c in range(ncell):
            m = mean[:, c]
            if not np.any(np.isfinite(m)):
                kept[(key, c)] = []
                continue
            th = field_thr * (np.nanmax(m) - np.nanmin(m)) + np.nanmin(m)
            above = m > th
            runs, i = [], 0
            while i < nb:
                if above[i]:
                    j = i
                    while j + 1 < nb and above[j + 1]:
                        j += 1
                    if j - i + 1 >= 2:
                        runs.append((i, j))
                    i = j + 1
                else:
                    i += 1
            fl = []
            for i, j in runs:
                # strictly between the first and last bin centres: half-bins 2i+1 .. 2j
                if act[:, 2 * i + 1:2 * j + 1, c].any(1).sum() >= n_trials_thr:
                    fl.append((i, j, _com(m[i:j + 1], cen[i:j + 1]), np.nanmax(m[i:j + 1])))
            kept[(key, c)] = fl
    post_thr = np.nanmean(tms[s1], axis=(0, 1)) + np.nanstd(tms[s1], axis=(0, 1))
    for c in range(ncell):
        f0 = kept.get(("0", c), []); f1 = kept.get(("1", c), [])
        out["n0"][c] = len(f0); out["n1"][c] = len(f1)
        if len(f0) == 2 and len(f1) == 2:
            out["off0"][c] = (f0[1][2] - f0[0][2]) * 2 * np.pi / TRACK
            out["off1"][c] = (f1[1][2] - f1[0][2]) * 2 * np.pi / TRACK
        if not f1:
            continue
        i, j, com_mean, _ = max(f1, key=lambda f: f[3])
        lo, hi = cen[i] - 10, cen[j] + 10
        inb = (cen >= lo) & (cen <= hi)
        on = (tms[s1][:, inb, c] > post_thr[c]).any(1)
        form = None
        for k in range(len(on)):
            if on[k] and on[k:k + 5].sum() >= 3:
                form = k
                break
        if form is None:
            continue
        t = s1[form]
        fr = np.arange(bounds[t, 0], bounds[t, 1])
        p = pos[fr]
        w = (p >= lo) & (p <= hi)
        out["form_lap"][c] = form + 1
        out["shift_cm"][c] = com_mean - _com(Xs[fr[w], c], p[w])
    return out


def session_seed(row):
    """A fixed seed per session, so that each session's shuffles do not depend on the others."""
    return int(row["mouse"][1:]) * 100 + int(row["day"])


def run_all(rows, workers=4):
    """Process sessions in parallel worker processes; switch days with the RR cross-correlation,
    other days without it."""
    from concurrent.futures import ProcessPoolExecutor
    import warnings
    out = {}
    with ProcessPoolExecutor(workers) as ex:
        futs = {}
        for r in rows:
            sw = r["day"] in SWITCH_DAYS
            futs[(r["mouse"], r["day"])] = ex.submit(_run_one, r, sw)
        for k, fu in futs.items():
            out[k] = fu.result()
    return out


def _run_one(r, sw):
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return process_session(r, session_seed(r), with_xcorr=sw)


@njit(cache=True)
def seed_numba(seed):
    """Seed the random generator of numba-compiled code (affinewarp's warp search draws from it;
    np.random.seed called from Python does not reach it)."""
    np.random.seed(seed)
