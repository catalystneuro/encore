"""Loading and measures for dandiset 001692 (Bouabid, Vu et al. 2026, striatal DA and ACh).

The files hold, per session, the fluorescence of every fiber of a multi-fiber array in two
channels: green (GRAB-ACh3.0, or the mutant ACh4.3mut in control mice) and red (GRAB-rDA3m, or
tdTomato in control mice), with the wheel velocity and an event table (licks, rewards, light cues,
optogenetic stimulation). Fibers marked `included` in the fiber table are the paper's sites.

Where a parameter comes from:
- 18 Hz sampling: the paper's Methods and code (`sr = 18`); the files state 9 Hz (see the notebook).
- Lags of -18 to 18 samples for spontaneous cross-correlation, -9 to 9 for event-related
  correlation, windows and significance windows: the paper's code (HoweLab/BouabidVu2026, 833fa3d).
- Transient detection (3 consecutive samples beyond the 2.5th/97.5th percentile of a null of
  3-sample means), pairing within 1 s, the 6 s reward exclusion: the Methods and code.
- Triggered-average significance (3 consecutive samples beyond the bootstrap null percentiles):
  the Methods (2.5/97.5); the code uses 0.5/99.5, available through `alpha`.
- Hotspot procedure: the code's steps (interpolate, pad, smooth, local Moran's I, shuffle null,
  95th percentile, connected volume of 0.125 mm3) with simplifications chosen here to fit the time
  limit: linear in place of natural-neighbor interpolation, 100 um voxels in place of 50 um, the
  convex hull of the sites in place of the Allen striatum mask, and fewer shuffles.
- Velocity filter: 1.3 Hz low-pass and 0.3 s smoothing from the Methods; a zero-phase Butterworth
  stands in for MATLAB's `lowpass` (a common choice). Stillness threshold 0.0208 m/s and minimum
  stillness of 1 s from the code; minimum bout of 2.27 s from the Methods (the code uses 2.2 s).
"""

from __future__ import annotations

import os
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
from scipy import ndimage, signal, stats
from scipy.spatial import Delaunay

DANDISET_ID = "001692"
DANDISET_VERSION = "0.260303.1724"
SR = 18.0  # samples per second per channel (Methods; the code's `sr = 18`)

SERIES = {
    "hp_art": "DfOverFexpHpArtFiberPhotometryResponseSeries",  # code: Fc_exp_hp_art
    "hp": "DfOverFexpHpFiberPhotometryResponseSeries",  # code: Fc_exp_hp
    "raw": "DfOverFexpFiberPhotometryResponseSeries",  # code: Fc_exp
}


# ---------------------------------------------------------------- archive access

def list_assets():
    """Paths and download URLs of every asset in the pinned version."""
    from dandi.dandiapi import DandiAPIClient

    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        out = []
        for a in ds.get_assets():
            out.append({"path": a.path, "size": a.size,
                        "url": f"https://api.dandiarchive.org/api/assets/{a.identifier}/download/"})
    return sorted(out, key=lambda a: a["path"])


def _open(url):
    return h5py.File(remfile.File(url), "r")


def _events(f):
    b = f["processing/behavior"]
    if "TimeIntervals" not in b:
        return {}
    ti = b["TimeIntervals"]
    kinds = ti["event_type"][:].astype(str)
    start, stop = ti["start_time"][:], ti["stop_time"][:]
    return {k: (start[kinds == k], stop[kinds == k]) for k in np.unique(kinds)}


def read_events(asset):
    """Session metadata and event table only (no traces)."""
    f = _open(asset["url"])
    ft = f["general/FiberPhotometry/FiberPhotometryTable"]
    return {"path": asset["path"], "subject": f["general/subject/subject_id"][()].decode(),
            "session_id": f["general/session_id"][()].decode(),
            "indicators": sorted({f[r].name.split("/")[-1] for r in ft["indicator"][:]}),
            "series": sorted(k for k in f["processing/ophys"] if "Series" in k),
            "events": _events(f)}


def read_session(asset, series="hp_art"):
    """One session: included fibers of both channels, their coordinates, velocity and events.

    Returns ACh (green) and DA (red) as float32 arrays of samples x sites, paired by sample index
    as the paper's code pairs them, with the times of the green channel's samples."""
    f = _open(asset["url"])
    ft = f["general/FiberPhotometry/FiberPhotometryTable"]
    included = ft["included"][:]
    coords = ft["coordinates"][:]
    indicator = np.array([f[r].name.split("/")[-1] for r in ft["indicator"][:]])
    out = {"path": asset["path"], "subject": f["general/subject/subject_id"][()].decode(),
           "session_id": f["general/session_id"][()].decode(), "series": series}
    missing = [c for c in ("Green", "Red") if f"{SERIES[series]}{c}" not in f["processing/ophys"]]
    if missing:  # the code skips sessions whose series is empty
        out["missing"] = missing
        out["events"] = _events(f)
        return out
    for color, name in (("Green", "ACh"), ("Red", "DA")):
        reg = f[f"acquisition/FiberPhotometryResponseSeries{color}/fiber_photometry_table_region"][:]
        keep = included[reg]
        ts = f[f"processing/ophys/{SERIES[series]}{color}"]
        out[name] = ts["data"][:][:, keep].astype(np.float32)
        out[f"{name}_start"] = float(ts["starting_time"][()])
        out[f"{name}_stated_rate"] = float(ts["starting_time"].attrs["rate"])
        out[f"{name}_indicator"] = sorted(set(indicator[reg][keep]))
        out[f"{name}_coords"] = coords[reg][keep]
        out[f"{name}_n_fibers"] = len(reg)
    beh = f["processing/behavior"]
    out["t"] = beh["WheelVelocity/timestamps"][:]
    out["velocity"] = beh["WheelVelocity/data"][:].astype(np.float32)
    out["events"] = _events(f)
    out["coords"] = out["ACh_coords"]
    return out


def _call(args):
    func, asset, kwargs = args
    for attempt in range(3):
        try:
            return func(asset, **kwargs)
        except OSError:
            if attempt == 2:
                raise


def load_many(assets, func=read_session, workers=None, **kwargs):
    """Stream many files in parallel processes (h5py serialises threads)."""
    workers = workers or min(12, 2 * (os.cpu_count() or 2))
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_call, [(func, a, kwargs) for a in assets]))


def event_index(session, times):
    """Sample indices nearest to event times, on the session's shared clock."""
    t = session["t"]
    idx = np.searchsorted(t, times)
    idx = np.clip(idx, 1, len(t) - 1)
    idx = np.where(np.abs(t[idx - 1] - times) < np.abs(t[idx] - times), idx - 1, idx)
    return idx[(times >= t[0]) & (times <= t[-1])]


def first_licks(session):
    """Index of the first lick after each reward delivery, before the next (code: get_reward_info)."""
    ev = session["events"]
    if "Reward" not in ev:
        return np.array([], int), np.array([], int)
    rew = event_index(session, ev["Reward"][0])
    licks = event_index(session, ev["Lick"][0]) if "Lick" in ev else np.array([], int)
    nxt = np.append(rew[1:], len(session["t"]))
    out = []
    for r, n in zip(rew, nxt):
        later = licks[(licks > r) & (licks < n)]
        if len(later):
            out.append(later[0])
    return rew, np.array(out, int)


def time_since(n, idx):
    """Seconds since the most recent index in `idx` (inf before the first)."""
    out = np.full(n, np.inf)
    for i, j in enumerate(np.sort(idx)):
        end = np.sort(idx)[i + 1] if i + 1 < len(idx) else n
        out[j:end] = np.arange(end - j) / SR
    return out


def concat(sessions, keys=("DA", "ACh"), pad=int(5 * SR)):
    """Concatenate sessions with NaN padding; returns arrays and per-session offsets."""
    parts = {k: [] for k in keys}
    offsets = []
    pos = 0
    for s in sessions:
        for k in keys:
            x = s[k]
            fill = np.full((pad,) + x.shape[1:], np.nan, np.float32)
            parts[k] += [fill, x.astype(np.float32)]
        offsets.append(pos + pad)
        pos += pad + len(s[keys[0]])
    return {k: np.concatenate(v) for k, v in parts.items()}, np.array(offsets)


# ---------------------------------------------------------------- correlation

def lagged_corr(da, ach, maxlag=18):
    """Pearson r of DA(t) with ACh(t + k) for k = -maxlag..maxlag, per site, NaNs dropped.

    Positive k means ACh after DA, so DA leads (the paper's convention)."""
    lags = np.arange(-maxlag, maxlag + 1)
    n = len(da)
    r = np.full((da.shape[1], len(lags)), np.nan)
    for j, k in enumerate(lags):
        if k >= 0:
            x, y = da[: n - k], ach[k:]
        else:
            x, y = da[-k:], ach[: n + k]
        ok = ~np.isnan(x) & ~np.isnan(y)
        m = ok.sum(0)
        x0, y0 = np.where(ok, x, 0.0).astype(np.float64), np.where(ok, y, 0.0).astype(np.float64)
        mx, my = x0.sum(0) / m, y0.sum(0) / m
        cov = (x0 * y0).sum(0) / m - mx * my
        vx = (x0 ** 2).sum(0) / m - mx ** 2
        vy = (y0 ** 2).sum(0) / m - my ** 2
        r[:, j] = cov / np.sqrt(vx * vy)
    return lags, r


def dominant(r, lags):
    """The extreme (max or min) with the larger magnitude, and its lag, per row."""
    ok = ~np.isnan(r).all(1)
    j = np.nanargmax(np.where(np.isnan(r), -1, np.abs(r)), axis=1)
    return np.where(ok, r[np.arange(len(r)), j], np.nan), np.where(ok, lags[j], 0)


# ---------------------------------------------------------------- transients

def transients(x, rng, n_boot=10000, n_surpass=3, alpha=0.025):
    """Significant transients per site (Methods; code get_transients.m).

    Returns, for 'pos' and 'neg', lists per site of (onset, offset, peak index, magnitude)."""
    rows = np.flatnonzero(~np.isnan(x).any(1))
    draw = rows[rng.integers(0, len(rows), size=(n_boot, n_surpass))]
    null = x[draw].mean(1)  # n_boot x sites
    upper = np.percentile(null, 100 * (1 - alpha), axis=0)
    lower = np.percentile(null, 100 * alpha, axis=0)
    out = {"pos": [], "neg": []}
    for s in range(x.shape[1]):
        for sign, above in (("pos", x[:, s] > upper[s]), ("neg", x[:, s] < lower[s])):
            d = np.diff(np.concatenate([[0], above.astype(np.int8), [0]]))
            on, off = np.flatnonzero(d == 1), np.flatnonzero(d == -1) - 1
            keep = (off - on + 1) >= n_surpass
            on, off = on[keep], off[keep]
            pk = np.array([o + (np.argmax(x[o:e + 1, s]) if sign == "pos" else np.argmin(x[o:e + 1, s]))
                           for o, e in zip(on, off)], int)
            out[sign].append(np.column_stack([on, off, pk, x[pk, s] if len(pk) else []]) if len(pk)
                             else np.zeros((0, 4)))
    return out


def pair_transients(first, second, window=18):
    """Pairs (i, j): transient j of `second` starts and peaks within (0, window] samples after
    transient i of `first`. Each first transient takes its earliest such partner (Methods) and
    each second transient is used once."""
    pairs, used = [], set()
    for i in range(len(first)):
        d_on = second[:, 0] - first[i, 0]
        d_pk = second[:, 2] - first[i, 2]
        cand = np.flatnonzero((d_on > 0) & (d_on <= window) & (d_pk > 0) & (d_pk <= window))
        cand = [j for j in cand if j not in used]
        if cand:
            pairs.append((i, cand[0]))
            used.add(cand[0])
    return np.array(pairs, int).reshape(-1, 2)


def boot_corr(a, b, rng, n_pairs=100, n_rep=1000):
    """Mean Pearson r over repeated draws of n_pairs pairs, and the 2.5/97.5 percentiles (Methods)."""
    if len(a) < n_pairs:
        return np.nan, np.nan, np.nan
    idx = np.argsort(rng.random((n_rep, len(a))), axis=1)[:, :n_pairs]
    xa, xb = a[idx], b[idx]
    xa = xa - xa.mean(1, keepdims=True)
    xb = xb - xb.mean(1, keepdims=True)
    r = (xa * xb).sum(1) / np.sqrt((xa ** 2).sum(1) * (xb ** 2).sum(1))
    return r.mean(), np.percentile(r, 2.5), np.percentile(r, 97.5)


# ---------------------------------------------------------------- triggered averages

def raster(x, events, w0, w1):
    """samples x sites x events, from w0 to w1 samples around each event (NaN outside the data)."""
    lags = np.arange(w0, w1 + 1)
    idx = events[None, :] + lags[:, None]
    ok = (idx >= 0) & (idx < len(x))
    out = x[np.clip(idx, 0, len(x) - 1)].transpose(0, 2, 1).astype(np.float32)  # lags x sites x events
    out[~np.broadcast_to(ok[:, None, :], out.shape)] = np.nan
    return out


def bootstrap_means(x, sampleable, n_events, w0, w1, rng, n_boot=1000, chunk=50):
    """Null distribution of the triggered average of n_events random times (Methods)."""
    lags = np.arange(w0, w1 + 1)
    out = np.empty((n_boot, len(lags), x.shape[1]), np.float32)
    for b0 in range(0, n_boot, chunk):
        nb = min(chunk, n_boot - b0)
        ev = sampleable[rng.integers(0, len(sampleable), size=(nb, n_events))]
        idx = ev[:, :, None] + lags[None, None, :]
        vals = x[idx]  # nb x n_events x lags x sites
        out[b0:b0 + nb] = np.nanmean(vals, axis=1)
    return out


def significant(mean, null, window, alpha=(2.5, 97.5), n_min=3):
    """Per site, whether the mean trace is above (peak) or below (dip) the null percentiles for
    n_min consecutive samples within the window (row indices)."""
    lo = np.percentile(null, alpha[0], axis=0)
    hi = np.percentile(null, alpha[1], axis=0)
    rows = slice(window[0], window[1] + 1)

    def run(b):
        b = b[rows]
        out = np.zeros(b.shape[1], bool)
        for s in range(b.shape[1]):
            c = np.convolve(b[:, s].astype(int), np.ones(n_min, int), "valid")
            out[s] = (c == n_min).any()
        return out

    return run(mean > hi), run(mean < lo)


def sampleable_times(n, w0, w1, exclude=None, valid=None):
    """Indices usable as random event times: the window fits and the time is not excluded."""
    ok = np.zeros(n, bool)
    ok[max(0, -w0): n - max(0, w1)] = True
    if exclude is not None:
        ok &= ~exclude
    if valid is not None:
        ok &= valid
    return np.flatnonzero(ok)


def event_correlation(ref, other, polarity, input_idx, ref_idx, corr_idx=np.arange(-9, 10),
                      window=9, min_trials=11):
    """Port of raster_transient_correlation.m (center_trial_transient = 1).

    ref and other are samples x sites x trials. For each site, the trial-averaged extreme of `ref`
    within ref_idx anchors a +/- window search; on each trial the local extreme nearest to it is
    the trial's magnitude; `other` is taken at corr_idx samples from that trial's extreme; Pearson
    r across trials at each lag. Returns r (lags x sites), dominant r, its lag, and the mean of
    `other` at the dominant lag."""
    input_idx = np.asarray(input_idx)
    L, S, T = ref.shape
    in_ref = np.isin(input_idx, ref_idx)
    mean_ref = np.nanmean(np.where(in_ref[:, None, None], ref, np.nan), axis=2)
    anchor = (np.nanargmax(mean_ref, 0) if polarity == 1 else np.nanargmin(mean_ref, 0))
    mag = np.full((S, T), np.nan)
    pk_row = np.full((S, T), -1)
    for s in range(S):
        lo, hi = anchor[s] - window, anchor[s] + window
        for t in range(T):
            seg = ref[max(lo, 0): min(hi, L - 1) + 1, s, t]
            off0 = max(lo, 0)
            if np.isnan(seg).all():
                continue
            v = polarity * np.nan_to_num(seg, nan=-np.inf)
            pk, _ = signal.find_peaks(v, distance=3)
            pk = pk[polarity * seg[pk] > 0]
            if not len(pk):
                continue
            rows = pk + off0
            dist = np.abs(rows - anchor[s])
            best = pk[np.lexsort((-polarity * seg[pk], dist))[0]]
            mag[s, t] = seg[best]
            pk_row[s, t] = best + off0
    lags = np.asarray(corr_idx)
    r = np.full((len(lags), S), np.nan)
    vals = np.full((len(lags), S, T), np.nan)
    for s in range(S):
        for t in range(T):
            if pk_row[s, t] < 0:
                continue
            rows = pk_row[s, t] + lags
            ok = (rows >= 0) & (rows < L)
            vals[ok, s, t] = other[rows[ok], s, t]
        for j in range(len(lags)):
            ok = ~np.isnan(mag[s]) & ~np.isnan(vals[j, s])
            if ok.sum() >= min_trials:
                r[j, s] = stats.pearsonr(mag[s, ok], vals[j, s, ok])[0]
    has = ~np.isnan(r).all(0)
    dom = np.full(S, np.nan)
    lag = np.full(S, np.nan)
    at = np.full(S, np.nan)
    j = np.nanargmax(np.abs(np.where(np.isnan(r), 0, r)), axis=0)
    dom[has] = r[j[has], np.flatnonzero(has)]
    lag[has] = lags[j[has]]
    mu = np.nanmean(vals, axis=2)
    at[has] = mu[j[has], np.flatnonzero(has)]
    return {"r": r, "dominant": dom, "lag": lag, "other_at_lag": at, "magnitude": mag, "lags": lags}


# ---------------------------------------------------------------- locomotion

def smooth_velocity(v, lp_hz=1.3, span=5):
    """Low-pass at 1.3 Hz (zero-phase Butterworth) and a 5-sample moving average (0.3 s)."""
    b, a = signal.butter(4, lp_hz / (SR / 2))
    vf = signal.filtfilt(b, a, v.astype(np.float64))
    return ndimage.uniform_filter1d(vf, span, mode="nearest")


def acceleration(vs, lp_hz=1.3, span=5):
    b, a = signal.butter(4, lp_hz / (SR / 2))
    acc = signal.filtfilt(b, a, np.diff(vs))
    return np.append(ndimage.uniform_filter1d(acc, span, mode="nearest"), np.nan)


def initiations(vel, still=0.0208, still_s=1.0, bout_s=2.27):
    """Clean initiations (code get_init_invig_events): >= still_s below threshold, then movement;
    kept when the bout (until velocity falls below threshold) lasts >= bout_s without NaNs."""
    moving = vel > still
    nan = np.isnan(vel)
    n_still = int(round(still_s * SR))
    inits, terms = [], []
    run = 0
    for i in range(len(vel)):
        if nan[i]:
            run = 0
            continue
        if not moving[i]:
            run += 1
            continue
        if run >= n_still:
            j = i
            while j < len(vel) and moving[j] and not nan[j]:
                j += 1
            if j < len(vel) and not nan[j]:
                inits.append(i)
                terms.append(j)
        run = 0
    inits, terms = np.array(inits, int), np.array(terms, int)
    keep = (terms - inits) >= bout_s * SR
    return inits[keep], terms[keep], inits, terms


def invigorations(acc, inits, terms):
    """First local maximum of acceleration after each initiation, before its termination."""
    out = np.full(len(inits), -1)
    for k, (i, j) in enumerate(zip(inits, terms)):
        seg = acc[i - 1: j + 2]
        pk = signal.argrelmax(np.nan_to_num(seg, nan=-np.inf))[0]
        if len(pk):
            out[k] = i - 1 + pk[0]
    return out


def invigoration_glm(y, vel, acc, init_ev, invig_all, fir=np.arange(-9, 19), fit_window=(-18, 36)):
    """Linear model of one site's signal around initiations (code fit_invig_GLM_get_resid).

    Returns the invigoration FIR coefficients, their p values, and the residual with the
    invigoration terms set to zero (NaN outside the fitted samples)."""
    n = len(y)
    rows = np.unique((init_ev[:, None] + np.arange(fit_window[0], fit_window[1] + 1)[None]).ravel())
    rows = rows[(rows >= 0) & (rows < n)]
    rows = rows[~np.isnan(y[rows]) & ~np.isnan(vel[rows]) & ~np.isnan(acc[rows])]

    def fir_cols(ev):
        cols = np.zeros((len(rows), len(fir)))
        pos = {r: k for k, r in enumerate(rows)}
        for c, lag in enumerate(fir):
            for e in ev + lag:
                k = pos.get(e)
                if k is not None:
                    cols[k, c] = 1
        return cols

    X = np.column_stack([np.ones(len(rows)), vel[rows], acc[rows], fir_cols(init_ev), fir_cols(invig_all)])
    beta, *_ = np.linalg.lstsq(X, y[rows], rcond=None)
    resid = y[rows] - X @ beta
    dof = len(rows) - np.linalg.matrix_rank(X)
    sigma2 = resid @ resid / dof
    cov = sigma2 * np.linalg.pinv(X.T @ X)
    se = np.sqrt(np.clip(np.diag(cov), 0, None))
    with np.errstate(divide="ignore", invalid="ignore"):
        p = 2 * stats.t.sf(np.abs(beta / se), dof)
    k0 = 3 + len(fir)
    b_noinv = beta.copy()
    b_noinv[k0:] = 0
    out = np.full(n, np.nan)
    out[rows] = y[rows] - X @ b_noinv
    return beta[k0:], p[k0:], out


# ---------------------------------------------------------------- hotspots

class Grid:
    """A 100 um grid over striatal coordinates (ML, DV, AP in mm) shared by all cohorts."""

    def __init__(self, coords, step=0.1, pad=0.5):
        lo = np.floor((coords.min(0) - pad) / step) * step
        hi = np.ceil((coords.max(0) + pad) / step) * step
        self.axes = [np.round(np.arange(lo[d], hi[d] + step / 2, step), 3) for d in range(3)]  # AP, ML, DV
        self.shape = tuple(len(a) for a in self.axes)
        self.step = step
        mesh = np.meshgrid(*self.axes, indexing="ij")
        self.points = np.column_stack([m.ravel() for m in mesh])

    def voxel(self, coords):
        idx = [np.clip(np.round((coords[:, d] - self.axes[d][0]) / self.step).astype(int), 0, self.shape[d] - 1)
               for d in range(3)]
        return np.ravel_multi_index(idx, self.shape)


class Interpolator:
    """Linear interpolation of site values onto the grid, with the code's padding and smoothing."""

    def __init__(self, grid, coords, sigma=1.0, n_pad=5):
        self.grid = grid
        tri = Delaunay(coords)
        simplex = tri.find_simplex(grid.points)
        inside = simplex >= 0
        T = tri.transform[simplex[inside]]
        bary = np.einsum("nij,nj->ni", T[:, :3], grid.points[inside] - T[:, 3])
        self.weights = np.column_stack([bary, 1 - bary.sum(1)])
        self.vertices = tri.simplices[simplex[inside]]
        self.inside = inside.reshape(grid.shape)
        self.sigma, self.n_pad = sigma, n_pad

    def volume(self, values):
        vol = np.full(self.grid.shape, np.nan)
        vol[self.inside] = (self.weights * values[self.vertices]).sum(1)
        valid = ~np.isnan(vol)
        k = np.ones((3, 3, 3))
        for _ in range(self.n_pad):
            s = ndimage.convolve(np.where(valid, vol, 0), k, mode="constant")
            c = ndimage.convolve(valid.astype(float), k, mode="constant")
            grow = ~valid & (c > 0)
            vol[grow] = s[grow] / c[grow]
            valid = ~np.isnan(vol)
        num = ndimage.gaussian_filter(np.where(valid, vol, 0), self.sigma, mode="constant")
        den = ndimage.gaussian_filter(valid.astype(float), self.sigma, mode="constant")
        sm = num / np.where(den > 0, den, np.nan)
        sm[~self.inside] = np.nan  # convex hull of the sites stands in for the striatum mask
        return sm


def local_moran(vol, half=5):
    """Local Moran's I as in local_morans_I.m, neighborhood of (2*half+1)^3 voxels."""
    z = vol - np.nanmean(vol)
    valid = ~np.isnan(z)
    z0 = np.where(valid, z, 0)
    size = 2 * half + 1
    box = lambda a: ndimage.uniform_filter(a, size, mode="constant") * size ** 3
    n = box(valid.astype(float)) - valid
    sz = box(z0) - z0
    sz2 = box(z0 ** 2) - z0 ** 2
    with np.errstate(divide="ignore", invalid="ignore"):
        m = z * (sz / n) / (sz2 / (n - 1))
    m[~valid] = np.nan
    return m


def hotspot(interp, values, rng, how="dominant", n_null=200, min_vox=125, pct=95, null=None):
    """The hotspot procedure: smoothed map, local Moran's I against a shuffle null, and the
    connected significant volume of at least min_vox voxels with the most extreme mean."""
    sm = interp.volume(values)
    mi = local_moran(sm)
    if null is None:
        null = np.stack([local_moran(interp.volume(values[rng.permutation(len(values))]))
                         for _ in range(n_null)])
    thr = np.nanpercentile(null, pct, axis=0)
    sig = (mi > thr) & interp.inside & ~np.isnan(sm)
    lab, n = ndimage.label(sig, structure=np.ones((3, 3, 3)))
    comps = []
    for c in range(1, n + 1):
        vox = np.flatnonzero(lab.ravel() == c)
        if len(vox) >= min_vox:
            comps.append((vox, np.nanmean(sm.ravel()[vox])))
    out = {"smooth": sm, "moran": mi, "n_components": len(comps), "voxels": None, "mean": np.nan,
           "striatal_mean": np.nanmean(sm), "null": null, "centroid": np.full(3, np.nan)}
    if comps:
        key = {"dominant": lambda c: -abs(c[1]), "max": lambda c: -c[1], "min": lambda c: c[1]}[how]
        vox, mean = sorted(comps, key=key)[0]
        out.update(voxels=vox, mean=mean)
        pts = interp.grid.points[vox]
        out["centroid"] = pts.mean(0)  # AP, ML, DV
    return out


def inside(grid, hs, coords):
    if hs["voxels"] is None:
        return np.zeros(len(coords), bool)
    return np.isin(grid.voxel(coords), hs["voxels"])


def random_volume(mask_flat, shape, size, rng):
    """A random connected volume grown inside the mask (code rand_volume.m, 6-neighbor growth)."""
    allowed = np.flatnonzero(mask_flat)
    cur = np.zeros(mask_flat.size, bool)
    cur[allowed[rng.integers(len(allowed))]] = True
    strides = np.array([shape[1] * shape[2], shape[2], 1])
    while cur.sum() < size:
        sel = np.flatnonzero(cur)
        sub = np.array(np.unravel_index(sel, shape)).T
        nb = []
        for d in range(3):
            for s in (-1, 1):
                q = sub.copy()
                q[:, d] += s
                ok = (q[:, d] >= 0) & (q[:, d] < shape[d])
                nb.append(q[ok] @ strides)
        cand = np.unique(np.concatenate(nb))
        cand = cand[mask_flat[cand] & ~cur[cand]]
        if not len(cand):
            break
        k = min(size - cur.sum(), rng.integers(1, max(2, len(cand) // 2 + 1)))
        cur[rng.choice(cand, k, replace=False)] = True
    return np.flatnonzero(cur)


def overlap_test(hs_a, mask_a, hs_b, mask_b, shape, rng, n=200):
    """Volume overlap test (code hotspot_comparison.m): the fraction of random pairs of connected
    volumes of the same sizes whose overlap is at least the observed one."""
    if hs_a["voxels"] is None or hs_b["voxels"] is None:
        return {"overlap": np.nan, "p": np.nan, "n_a": 0, "n_b": 0}
    obs = len(np.intersect1d(hs_a["voxels"], hs_b["voxels"]))
    ma, mb = mask_a.ravel(), mask_b.ravel()
    null = [len(np.intersect1d(random_volume(ma, shape, len(hs_a["voxels"]), rng),
                               random_volume(mb, shape, len(hs_b["voxels"]), rng))) for _ in range(n)]
    return {"overlap": obs, "p": float(np.mean(np.array(null) >= obs)), "n_a": len(hs_a["voxels"]),
            "n_b": len(hs_b["voxels"]), "null_median": float(np.median(null))}


def in_out(values, is_in):
    """Two-sided rank-sum inside against outside; medians and counts."""
    a, b = values[is_in & ~np.isnan(values)], values[~is_in & ~np.isnan(values)]
    p = stats.ranksums(a, b).pvalue if len(a) and len(b) else np.nan
    return {"n_in": len(a), "n_out": len(b), "median_in": np.median(a) if len(a) else np.nan,
            "median_out": np.median(b) if len(b) else np.nan, "p": p}


# ---------------------------------------------------------------- per-figure pipelines

def by_mouse(sessions):
    out = {}
    for s in sessions:
        out.setdefault(s["subject"], []).append(s)
    return {m: sorted(v, key=lambda s: s["session_id"]) for m, v in sorted(out.items())}


def site_table(sessions):
    """Mouse and coordinates of every site, in the order the pipelines return values."""
    mice, coords = [], []
    for m, ss in by_mouse(sessions).items():
        mice += [m] * len(ss[0]["coords"])
        coords.append(ss[0]["coords"])
    return np.array(mice), np.concatenate(coords)


def spontaneous_xcorr(sessions, maxlag=18, mask=None, concatenate=False):
    """Dominant cross-correlation per site. By default r is computed per session and averaged
    over sessions (the code's get_cross_corr_results); `mask(session)` returns samples to drop."""
    lags = np.arange(-maxlag, maxlag + 1)
    rs = []
    for m, ss in by_mouse(sessions).items():
        prepared = []
        for s in ss:
            da, ach = s["DA"].copy(), s["ACh"].copy()
            if mask is not None:
                bad = mask(s)
                da[bad], ach[bad] = np.nan, np.nan
            prepared.append({"DA": da, "ACh": ach})
        if concatenate:
            cat, _ = concat(prepared)
            rs.append(lagged_corr(cat["DA"], cat["ACh"], maxlag)[1])
        else:
            with np.errstate(invalid="ignore"):
                per = np.array([lagged_corr(p["DA"], p["ACh"], maxlag)[1] for p in prepared])
            with np.errstate(all="ignore"):
                import warnings
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", RuntimeWarning)
                    rs.append(np.nanmean(per, 0))
    r = np.concatenate(rs)
    dom, lag = dominant(r, lags)
    return {"r": r, "lags": lags, "dominant": dom, "lag": lag}


def reward_mask(session, seconds=6.0):
    """Samples within `seconds` after a reward delivery or first lick (the code's 6 s)."""
    n = len(session["DA"])
    rew, lick = first_licks(session)
    return (time_since(n, rew) < seconds) | (time_since(n, lick) < seconds)


PAIR_TYPES = [("ACh", "neg", "DA", "pos"), ("ACh", "pos", "DA", "neg"),
              ("ACh", "pos", "DA", "pos"), ("ACh", "neg", "DA", "neg")]


def pair_name(tp):
    names = {"pos": "peak", "neg": "trough"}
    return f"ACh {names[tp[1]]} / DA {names[tp[3]]}"


def transient_pairs(sessions, rng, n_rep=1000, exclude_s=6.0):
    """Transient detection, pairing, directionality, occurrence and magnitude correlation per site
    (Methods and code fig2_paired_transients.m)."""
    per_site = []
    rates = []
    for m, ss in by_mouse(sessions).items():
        nsite = ss[0]["DA"].shape[1]
        acc = {tp: [dict(A=0, B=0, pa=0, pd=0, ta=0, td=0, ma=[], md=[], ra=[], rd=[]) for _ in range(nsite)]
               for tp in PAIR_TYPES}
        cnt = {k: np.zeros(nsite) for k in ("DA_pos", "DA_neg", "ACh_pos", "ACh_neg")}
        dur = 0.0
        for s in ss:
            tr = {ch: transients(s[ch], rng) for ch in ("DA", "ACh")}
            n = len(s["DA"])
            dur += n / SR
            rew, lick = first_licks(s)
            since = np.minimum(time_since(n, rew), time_since(n, lick))
            for si in range(nsite):
                filt = {}
                for ch in ("DA", "ACh"):
                    for sg in ("pos", "neg"):
                        x = tr[ch][sg][si]
                        keep = since[x[:, 0].astype(int)] > exclude_s if len(x) else np.zeros(0, bool)
                        filt[(ch, sg)] = x[keep]
                        cnt[f"{ch}_{sg}"][si] += keep.sum()
                for tp in PAIR_TYPES:
                    a, d = filt[(tp[0], tp[1])], filt[(tp[2], tp[3])]
                    pa, pdd = pair_transients(a, d), pair_transients(d, a)
                    st = acc[tp][si]
                    st["A"] += len(pa)
                    st["B"] += len(pdd)
                    st["pa"] += len(set(pa[:, 0]) | set(pdd[:, 1]))
                    st["pd"] += len(set(pa[:, 1]) | set(pdd[:, 0]))
                    st["ta"] += len(a)
                    st["td"] += len(d)
                    st["ma"] += list(a[pa[:, 0], 3])
                    st["md"] += list(d[pa[:, 1], 3])
                    st["ra"] += list(a[pdd[:, 1], 3])
                    st["rd"] += list(d[pdd[:, 0], 3])
        for si in range(nsite):
            row = {"mouse": m, "site": si}
            for k in cnt:
                row[f"rate_{k}"] = cnt[k][si] / dur
            for tp in PAIR_TYPES:
                st = acc[tp][si]
                key = pair_name(tp)
                tot = st["A"] + st["B"]
                row[f"di|{key}"] = (st["A"] - st["B"]) / tot if tot else np.nan
                row[f"occ|{key}"] = (st["pa"] + st["pd"]) / (st["ta"] + st["td"]) if st["ta"] + st["td"] else np.nan
                ach = np.array(st["ma"] + st["ra"])  # ACh-first pairs then DA-first pairs
                da = np.array(st["md"] + st["rd"])
                mean, lo, hi = boot_corr(ach, da, rng, n_rep=n_rep)
                row[f"mag|{key}"], row[f"lo|{key}"], row[f"hi|{key}"] = mean, lo, hi
                row[f"npairs|{key}"] = len(ach)
                # the code's version: Pearson over the pairs of the leading order given by the index
                if st["A"] + st["B"] >= 3:
                    use_a = st["A"] >= st["B"]
                    xa = np.array(st["ma"] if use_a else st["ra"])
                    xd = np.array(st["md"] if use_a else st["rd"])
                    if len(xa) >= 3 and np.std(xa) > 0 and np.std(xd) > 0:
                        r, p = stats.pearsonr(xa, xd)
                        row[f"code_r|{key}"], row[f"code_p|{key}"] = r, p
            per_site.append(row)
    return per_site


def event_rasters(sessions, events_of, w0, w1, exclude_of=None, keys=("DA", "ACh")):
    """Per mouse: concatenated data, rasters at events and random-time candidates for the null."""
    out = {}
    for m, ss in by_mouse(sessions).items():
        cat, off = concat(ss, keys=keys)
        n = len(cat[keys[0]])
        ev, excl = [], np.zeros(n, bool)
        for s, o in zip(ss, off):
            e = events_of(s)
            ev += list(e + o)
            if exclude_of is not None:
                for a, b in exclude_of(s):
                    excl[o + a: o + b] = True
            excl[o + e] = True
        ev = np.array(ev, int)
        valid = ~np.isnan(cat[keys[0]]).any(1)
        samp = sampleable_times(n, w0, w1, exclude=excl, valid=valid)
        out[m] = {"cat": cat, "events": ev, "sampleable": samp,
                  "rasters": {k: raster(cat[k], ev, w0, w1) for k in keys}}
    return out


def triggered_significance(er, w0, w1, window, rng, n_boot=1000, keys=("DA", "ACh")):
    """Mean traces and significance per site, for the Methods' and the code's percentiles."""
    out = {}
    for m, d in er.items():
        res = {}
        for k in keys:
            mean = np.nanmean(d["rasters"][k], 2)
            null = bootstrap_means(d["cat"][k], d["sampleable"], len(d["events"]), w0, w1, rng, n_boot)
            res[k] = {"mean": mean,
                      "methods": significant(mean, null, window, (2.5, 97.5)),
                      "code": significant(mean, null, window, (0.5, 99.5))}
        out[m] = res
    return out


def stack(per_mouse, f):
    return np.concatenate([f(v) for _, v in sorted(per_mouse.items())])


def locomotion_events(sessions, bout_s=2.27):
    """Velocity, acceleration and events per mouse over concatenated spontaneous sessions."""
    out = {}
    for m, ss in by_mouse(sessions).items():
        prepared = []
        for s in ss:
            vs = smooth_velocity(s["velocity"])
            prepared.append({"DA": s["DA"], "ACh": s["ACh"], "vel": vs[:, None], "acc": acceleration(vs)[:, None]})
        cat, _ = concat(prepared, keys=("DA", "ACh", "vel", "acc"))
        vel, acc = cat["vel"][:, 0], cat["acc"][:, 0]
        init, term, init_all, term_all = initiations(vel, bout_s=bout_s)
        out[m] = {"cat": cat, "vel": vel, "acc": acc, "init": init, "term": term, "init_all": init_all,
                  "invig": invigorations(acc, init, term)}
    return out


def invigoration_analysis(loco):
    """GLM residuals and invigoration-triggered rasters per mouse (code get_invig_trg_avg)."""
    out = {}
    for m, d in loco.items():
        acc = d["acc"]
        a = np.nan_to_num(acc, nan=-np.inf)
        is_max = np.zeros(len(acc), bool)
        is_max[1:-1] = (a[1:-1] > a[:-2]) & (a[1:-1] >= a[2:])
        all_inv = np.flatnonzero(is_max & (acc > 0))
        resid, sig, beta = {}, [], []
        for ch in ("DA", "ACh"):
            cols = []
            for si in range(d["cat"][ch].shape[1]):
                b, p, rr = invigoration_glm(d["cat"][ch][:, si].astype(float), d["vel"], acc, d["init_all"], all_inv)
                cols.append(rr)
                if ch == "DA":
                    ok = ((p < 0.05) & (b > 0)).astype(int)
                    sig.append(len(ok) >= 3 and np.convolve(ok, np.ones(3, int), "valid").max() == 3)
                    beta.append(b)
            resid[ch] = np.array(cols).T
        inv = d["invig"][d["invig"] >= 0]
        out[m] = {"sig_da_peak": np.array(sig), "beta_da": np.array(beta), "n_invig": len(inv),
                  "rasters": {ch: raster(resid[ch], inv, -18, 36) for ch in ("DA", "ACh")}}
    return out


def read_descriptions(asset):
    """Device descriptions and the session description of one file."""
    f = _open(asset["url"])
    dev = f["general/devices"]
    out = {k: dev[k].attrs.get("description", "") for k in dev}
    out["session_description"] = f["session_description"][()].decode(errors="replace")
    out["pharmacology"] = f["general/pharmacology"][()].decode(errors="replace")
    return out
