"""Loading and measures for dandiset 001084 (Vu et al. 2024, Neuron, multi-fiber arrays).

The files are streamed from the DANDI Archive at a pinned version. Each NWB file holds
fiber photometry traces (raw, baseline and DF/F, one column per fiber), a fiber table with
the localized tip coordinates (AP, ML, DV in mm from bregma) and an ``included`` flag, the
treadmill velocities, and a table of light, tone, reward and lick intervals.

Where the parameters come from:

- GLM for salient stimulus responses (``fit_cue_glm``): the paper's STAR Methods ("DA
  release to salient stimuli") and its code (Zenodo 10.5281/zenodo.10272874,
  ``Fig04/general_functions/run_sal_stim_glm.m``): window -1 to 2 s around onset, a cubic
  B-spline basis of 13 functions over the 1 s stimulus (knots every 3 frames at 30 Hz), lagged
  overall velocity and acceleration (most positive and most negative ITI cross-correlation
  with p < 0.05, lags within 500 ms). At 18 Hz the code keeps knots every 3 frames, which
  gives 9 functions (``SuppFig05/EFGH/analysis_code/run_sal_stim_glm_470_415.m``); the
  Methods' 13 can be had with ``knot_intervals=10``.
- Null distribution (``cue_glm_null``): the same model refitted with random onsets drawn from
  the sampleable frames and shuffled stimulus labels, 10000 times (Methods); significance is
  3 consecutive frames outside the 0.5 to 99.5 percentile band (Methods and code).
- Tone onsets are shifted by 11 frames at 30 Hz (6 at 18 Hz), the speaker delay stated in the
  paper's code (``salientStim_getTrialTimes.m`` README, ``sal_stim_glm.m``); the Methods do not
  mention it.
- Overall velocity: linear velocity plus the absolute angular velocity in m/s (ball diameter
  0.2032 m), low-pass filtered at 1.5 Hz and smoothed over 300 ms; acceleration is its
  difference, filtered and smoothed the same way (Methods). The paper uses MATLAB's
  ``lowpass`` (a zero-phase FIR); here a zero-phase 4th-order Butterworth filter is used, a
  common choice.
- Half-maximum latency (``half_max_latency``): Methods ("Latency"), with the code's rule for
  the baseline of the rise (the larger of 0 and the minimum before the peak).
- Optogenetic stimulation responses (``stim_response``): Methods ("DA release to optogenetic
  stimulation") and code (``Fig06/general functions``): stimulation epochs are where the
  stimulated fiber's DF/F exceeds 0.4, kept when at least 4 s apart; the response is the mean
  DF/F from one frame to 0.5 s after laser offset, tested against 10000 random onsets. The
  random onsets exclude frames with the laser trace above 0.5, the windows ending at each
  onset and the end of the recording, as ``getNullDist_stim.m`` does.
- Correlation within groups (``within_group_rank_corr``): a common choice, not from the paper,
  for testing a pooled correlation without letting differences between mice drive it.
"""

from __future__ import annotations

import functools

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import signal, stats
from scipy.interpolate import BSpline

DANDISET_ID = "001084"
DANDISET_VERSION = "0.241023.2011"
BALL_DIAMETER_M = 0.2032  # 8 inch ball (paper's ball2xy.m and the conversion code)

SALIENT_SESSIONS = {
    "DL18": "sub-DL18/sub-DL18_ses-211110_image+ophys.nwb",
    "DL20": "sub-DL20/sub-DL20_ses-220111_image+ophys.nwb",
    "DL21": "sub-DL21/sub-DL21_ses-220112_image+ophys.nwb",
    "DL23": "sub-DL23/sub-DL23_ses-220117_image+ophys.nwb",
    "DL27": "sub-DL27/sub-DL27_ses-220930_image+ophys.nwb",
    "DL29": "sub-DL29/sub-DL29_ses-220930_image+ophys.nwb",
    "DL30": "sub-DL30/sub-DL30_ses-220930_image+ophys.nwb",
}
ISOSBESTIC_SESSIONS = {
    "DL31": "sub-DL31/sub-DL31_ses-231020_ophys.nwb",
    "DL32": "sub-DL32/sub-DL32_ses-231020_ophys.nwb",
}


# --- access -------------------------------------------------------------------------------

@functools.lru_cache(maxsize=1)
def _dandiset():
    from dandi.dandiapi import DandiAPIClient
    return DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)


@functools.lru_cache(maxsize=1)
def _assets() -> dict:
    return {a.path: a for a in _dandiset().get_assets()}


@functools.lru_cache(maxsize=None)
def asset_url(path: str) -> str:
    return _assets()[path].get_content_url(follow_redirects=1, strip_query=True)


def list_nwb_paths() -> list[str]:
    return sorted(p for p in _assets() if p.endswith(".nwb"))


def open_nwb(path: str) -> h5py.File:
    return h5py.File(remfile.File(asset_url(path)), "r")


def _text(x):
    return x.decode() if isinstance(x, bytes) else x


# --- reading ------------------------------------------------------------------------------

def fiber_table(f: h5py.File, series: str) -> pd.DataFrame:
    """The fiber table rows of one acquisition series, in the series' column order."""
    t = f["general/FiberPhotometry/FiberPhotometryTable"]
    rows = f["acquisition"][series]["fiber_photometry_table_region"][:]
    coords = t["coordinates"][:][rows]
    allen = t["allen_atlas_coordinates"][:][rows]
    return pd.DataFrame({
        "row": rows,
        "location": [_text(x) for x in t["location"][:][rows]],
        "included": t["included"][:][rows].astype(bool),
        "AP": coords[:, 0], "ML": coords[:, 1], "DV": coords[:, 2],
        "allen_AP": allen[:, 0], "allen_ML": allen[:, 1], "allen_DV": allen[:, 2],
    })


def series_times(group: h5py.Group, n: int) -> np.ndarray:
    if "timestamps" in group:
        return group["timestamps"][:]
    st = group["starting_time"]
    return st[()] + np.arange(n) / st.attrs["rate"]


def read_dff(f: h5py.File, color: str = "Green", columns=None):
    """DF/F (frames x fibers) of one channel, its frame times and its fiber table."""
    g = f["processing/ophys"][f"DfOverFFiberPhotometryResponseSeries{color}"]
    data = g["data"][:]
    times = series_times(g, data.shape[0])
    table = fiber_table(f, f"FiberPhotometryResponseSeries{color}")
    if columns is not None:
        data, table = data[:, columns], table.iloc[columns].reset_index(drop=True)
    return data, times, table


def read_events(f: h5py.File) -> pd.DataFrame:
    if "processing/behavior/TimeIntervals" not in f:
        return pd.DataFrame(columns=["start_time", "stop_time", "event_type"])
    g = f["processing/behavior/TimeIntervals"]
    return pd.DataFrame({"start_time": g["start_time"][:], "stop_time": g["stop_time"][:],
                         "event_type": [_text(x) for x in g["event_type"][:]]})


def read_behavior(f: h5py.File) -> dict:
    g = f["processing/behavior"]
    vel = g["Velocity/data"][:]
    return {"t": g["AngularVelocity/timestamps"][:], "roll": vel[:, 0], "pitch": vel[:, 1],
            "angular": g["AngularVelocity/data"][:]}


def nearest_index(times: np.ndarray, t: np.ndarray) -> np.ndarray:
    idx = np.clip(np.searchsorted(times, t), 1, len(times) - 1)
    return np.where(np.abs(times[idx - 1] - t) <= np.abs(times[idx] - t), idx - 1, idx)


# --- locomotion -----------------------------------------------------------------------------

def _smooth(x, span):
    """Centred moving average over ``span`` samples, ignoring NaN, like MATLAB's smooth."""
    span = int(span) | 1
    k = np.ones(span)
    ok = np.isfinite(x)
    num = np.convolve(np.where(ok, x, 0.0), k, mode="same")
    den = np.convolve(ok.astype(float), k, mode="same")
    return num / np.maximum(den, 1)


def _lowpass(x, cutoff, fs):
    b, a = signal.butter(4, cutoff / (fs / 2))
    y = np.array(x, dtype=float)
    ok = np.isfinite(y)
    y[~ok] = np.interp(np.flatnonzero(~ok), np.flatnonzero(ok), y[ok]) if (~ok).any() else y[~ok]
    return signal.filtfilt(b, a, y)


def overall_velocity(beh: dict, fs: float, cutoff: float = 1.5, smooth_s: float = 0.3):
    """Overall velocity and acceleration (Methods, 'Velocity and acceleration')."""
    linear = np.hypot(beh["roll"], beh["pitch"])
    angular_ms = np.abs(beh["angular"]) * BALL_DIAMETER_M / 2
    vel = _smooth(_lowpass(linear + angular_ms, cutoff, fs), round(smooth_s * fs))
    acc = np.r_[np.nan, _smooth(_lowpass(np.diff(vel), cutoff, fs), round(smooth_s * fs))]
    return vel, acc


def iti_mask(n: int, onsets, offsets, extra: int) -> np.ndarray:
    """True outside stimulus presentations (from onset to offset plus ``extra`` frames)."""
    m = np.ones(n, bool)
    for a, b in zip(onsets, offsets):
        m[max(a, 0):min(b + extra + 1, n)] = False
    return m


def loco_lags(dff, vel, acc, iti, max_lag: int, code_indexing: bool = False):
    """Lag (frames) of the most positive and most negative ITI correlation of each fiber with
    velocity and acceleration, NaN when not significant (p >= 0.05) or of the wrong sign.

    Correlates DF/F at t with locomotion at t + lag. With ``code_indexing`` the negative lags
    are computed as the paper's code does (sal_stim_iti_acc_cc.m), where they reduce to a zero
    shift over a truncated range.
    """
    n, nfib = dff.shape
    lags = np.arange(-max_lag, max_lag + 1)
    out = {}
    for name, x in (("vel", vel), ("acc", acc)):
        x = np.where(iti, x, np.nan)
        rho = np.full((nfib, len(lags)), np.nan)
        p = np.full_like(rho, np.nan)
        for i, lag in enumerate(lags):
            if lag >= 0:
                xs, ys = x[lag:], dff[:n - lag]
            elif code_indexing:
                xs, ys = x[:n + lag], dff[:n + lag]
            else:
                xs, ys = x[:n + lag], dff[-lag:]
            ok = np.isfinite(xs)
            xv = xs[ok] - xs[ok].mean()
            yv = ys[ok] - ys[ok].mean(0)
            r = (xv @ yv) / np.sqrt((xv @ xv) * (yv * yv).sum(0))
            rho[:, i] = r
            df = ok.sum() - 2
            tt = r * np.sqrt(df / np.maximum(1 - r ** 2, 1e-12))
            p[:, i] = 2 * stats.t.sf(np.abs(tt), df)
        for which, fn in (("max", np.argmax), ("min", np.argmin)):
            j = fn(rho, axis=1)
            r = rho[np.arange(nfib), j]
            pj = p[np.arange(nfib), j]
            good = (pj < 0.05) & ((r > 0) if which == "max" else (r < 0))
            out[f"{name}_{which}"] = np.where(good, lags[j], np.nan)
    return out


# --- GLM ------------------------------------------------------------------------------------

def spline_basis(whole_window: int, step: int = 3, degree: int = 3, n_intervals: int | None = None) -> np.ndarray:
    """B-spline basis evaluated at frames 0..whole_window (as MATLAB spcol in the paper's code).

    Knots every ``step`` frames, or, with ``n_intervals``, that many equal intervals; there are
    ``n_intervals + degree`` functions."""
    if n_intervals is None:
        n_intervals = whole_window // step
    knots = np.linspace(0, whole_window, n_intervals + 1)
    t = np.r_[[knots[0]] * degree, knots, [knots[-1]] * degree]
    nb = len(t) - degree - 1
    x = np.arange(whole_window + 1, dtype=float)
    B = np.zeros((len(x), nb))
    for b in range(nb):
        c = np.zeros(nb)
        c[b] = 1
        B[:, b] = BSpline(t, c, degree, extrapolate=False)(x)
    B[-1, -1] = 1.0  # right end point belongs to the last basis function
    return np.nan_to_num(B)


class CueGLM:
    """The salient-stimulus GLM of one session, refit cheaply for many sets of onsets.

    The design holds an intercept, the spline regressors of each cue type and every candidate
    lagged locomotion column. Each fiber uses its own subset of locomotion columns; all fibers
    are solved together from the shared Gram matrix (normal equations), which gives the same
    estimates as fitting each fiber separately.
    """

    def __init__(self, dff, vel, acc, lags: dict, fs: float, knot_intervals: int | None = None):
        self.fs = fs
        self.whole = int(round(fs))  # the 1 s stimulus: 30 frames at 30 Hz, 18 at 18 Hz
        self.pre, self.post = self.whole, 2 * self.whole  # window -1 s to +2 s
        self.tau = np.arange(-self.pre, self.post + 1)
        self.B = spline_basis(self.whole, n_intervals=knot_intervals)
        self.nb = self.B.shape[1]
        self.max_lag = int(round(fs / 2))
        lag_list = np.arange(-self.max_lag, self.max_lag + 1)
        self.cand = [("vel", int(L)) for L in lag_list] + [("acc", int(L)) for L in lag_list]
        pad = self.max_lag + self.post + self.pre + 1
        self.pad = pad
        self.n = dff.shape[0]
        self.dff = np.vstack([np.full((pad, dff.shape[1]), np.nan), dff, np.full((pad, dff.shape[1]), np.nan)])
        self.loco = np.stack([np.r_[np.full(pad, np.nan), x, np.full(pad, np.nan)] for x in (vel, acc)])
        self.cand_var = np.array([0 if v == "vel" else 1 for v, _ in self.cand])
        self.cand_lag = np.array([L for _, L in self.cand])
        index = {c: i for i, c in enumerate(self.cand)}
        nbase = 1 + 2 * self.nb
        self.nbase = nbase
        ncol = nbase + len(self.cand)
        cols = np.empty((dff.shape[1], nbase + 4), int)
        self.n_loco = np.zeros(dff.shape[1], int)
        for r in range(dff.shape[1]):
            own = [nbase + index[(name, int(lags[f"{name}_{which}"][r]))]
                   for name in ("vel", "acc") for which in ("max", "min")
                   if np.isfinite(lags[f"{name}_{which}"][r])]
            self.n_loco[r] = len(own)
            cols[r] = list(range(nbase)) + own + list(range(ncol, ncol + 4 - len(own)))
        self.cols = cols
        self.ncol = ncol
        block = np.zeros((len(self.tau), self.nb))
        block[(self.tau >= 0) & (self.tau <= self.whole)] = self.B
        self.block = block

    def sampleable(self):
        """Onsets the null may draw from: full windows (eventTriggeredAverage.m)."""
        n, w = self.n, len(self.tau)
        idx = np.arange(self.pre, n - self.post)
        return idx[(idx > w) & (idx < n - self.post - self.pre - 1)]

    def _design(self, onsets, labels):
        onsets = np.asarray(onsets) + self.pad
        labels = np.asarray(labels)
        ntr, T = len(onsets), len(self.tau)
        rows = onsets[:, None] + self.tau[None, :]
        X = np.zeros((ntr, T, self.ncol))
        X[:, :, 0] = 1
        for c in (0, 1):
            X[labels == c, :, 1 + c * self.nb:1 + (c + 1) * self.nb] = self.block
        X[:, :, self.nbase:] = self.loco[self.cand_var[None, None, :],
                                         rows[:, :, None] + self.cand_lag[None, None, :]]
        Y = self.dff[rows]
        return X.reshape(ntr * T, -1), Y.reshape(ntr * T, -1)

    def fit(self, onsets, labels, keep_trials=False):
        """Spline ETA (B @ coefficients) per cue and fiber; optionally the trial activity with the
        fitted locomotion terms removed (the code's ``loco_regr``)."""
        X, Y = self._design(onsets, labels)
        ok = np.isfinite(X).all(1) & np.isfinite(Y).all(1)
        Xo, Yo = X[ok], Y[ok]
        G = np.zeros((self.ncol + 4, self.ncol + 4))
        G[:self.ncol, :self.ncol] = Xo.T @ Xo
        G[self.ncol:, self.ncol:] = np.eye(4)
        XtY = np.zeros((self.ncol + 4, Y.shape[1]))
        XtY[:self.ncol] = Xo.T @ Yo
        c = self.cols
        Gs = G[c[:, :, None], c[:, None, :]]
        rhs = XtY[c, np.arange(Y.shape[1])[:, None]]
        coef = np.linalg.solve(Gs, rhs[..., None])[..., 0]  # fibers x columns
        nb = self.nb
        mu = np.stack([self.B @ coef[:, 1 + k * nb:1 + (k + 1) * nb].T for k in (0, 1)])
        regr = None
        if keep_trials:
            Xn = np.nan_to_num(np.c_[X, np.zeros((len(X), 4))])
            loco = np.einsum("tfk,fk->tf", Xn[:, c[:, self.nbase:]], coef[:, self.nbase:])
            regr = (Y - loco).reshape(len(onsets), len(self.tau), -1)
        return mu, regr


def cue_glm_null(glm: CueGLM, labels, n_iter: int, rng: np.random.Generator):
    """Spline ETAs for random onsets (drawn without replacement) and permuted labels."""
    pool = glm.sampleable()
    out = np.empty((n_iter, 2, glm.B.shape[0], glm.dff.shape[1]))
    labels = np.asarray(labels)
    for it in range(n_iter):
        on = rng.choice(pool, size=len(labels), replace=False)
        lab = rng.permutation(labels)
        out[it], _ = glm.fit(on, lab)
    return out


def runs_of(mask: np.ndarray, n: int = 3) -> np.ndarray:
    """True for columns of ``mask`` (time x fibers) with at least n consecutive True values."""
    m = np.asarray(mask, bool)
    if m.ndim == 1:
        m = m[:, None]
    run = np.zeros(m.shape[1], int)
    best = np.zeros(m.shape[1], int)
    for row in m:
        run = np.where(row, run + 1, 0)
        best = np.maximum(best, run)
    return best >= n


def signed_peak(mu: np.ndarray, sig_up: np.ndarray, sig_down: np.ndarray):
    """Largest-magnitude value of the ETA per fiber, and its significance (sal_stim_bubbles_rb.m)."""
    mx, mn = mu.max(0), mu.min(0)
    use_min = np.abs(mn) > np.abs(mx)
    return np.where(use_min, mn, mx), np.where(use_min, sig_down, sig_up)


def half_max_latency(trace: np.ndarray, direction: int = 1):
    """Index of the half-maximum crossing before the peak (or trough for direction -1), from the
    rise rule of the paper's rise_dip_time.m; NaN if there is none. Index 0 is stimulus onset."""
    x = direction * np.asarray(trace, float)
    k = int(np.nanargmax(x))
    start = max(0.0, np.nanmin(x[:k + 1]))
    thr = 0.5 * (x[k] - start) + start
    below = np.flatnonzero(x[:k + 1] < thr)
    if len(below) == 0:
        return np.nan
    j0 = below[-1]
    above = np.flatnonzero(x[j0:k + 1] >= thr)
    return float(j0 + above[0]) if len(above) else np.nan


# --- optogenetic stimulation ------------------------------------------------------------------

def laser_epochs(trace: np.ndarray, fs: float, thresh: float = 0.4, min_sep_s: float = 4.0):
    """Onsets and offsets where the stimulated fiber's DF/F exceeds ``thresh``, keeping epochs at
    least ``min_sep_s`` from their neighbours (getStimTimes.m)."""
    above = trace > thresh
    d = np.diff(np.r_[0, above.astype(int)])
    on = np.flatnonzero(d == 1)
    off = np.flatnonzero(d == -1)
    if len(off) < len(on):
        on = on[:len(off)]
    sep = round(min_sep_s * fs)
    keep = np.ones(len(on), bool)
    for i in range(len(on)):
        if (i > 0 and on[i] - on[i - 1] < sep) or (i < len(on) - 1 and on[i + 1] - on[i] < sep):
            keep[i] = False
    return on[keep], off[keep]


def stim_response(dff: np.ndarray, on, off, fs: float, rng: np.random.Generator,
                  n_iter: int = 10000, window_s: float = 0.5, laser_trace=None):
    """Mean DF/F from one frame after laser offset to ``window_s``, per fiber, with the paper's
    bootstrap test: the trial-averaged trace exceeds the 0.5 to 99.5 percentile band of random
    onsets for 3 consecutive frames (getStimResp.m, getNullDist_stim.m)."""
    n = dff.shape[0]
    w = np.arange(1, round(window_s * fs) + 1)
    off = np.asarray(off)
    off = off[off + w[-1] < n]  # epochs whose window ends inside the recording
    trials = dff[off[:, None] + w[None, :]]  # trials x frames x fibers
    avg = trials.mean(0)
    resp = trials.mean(1)  # trial x fiber
    stim = laser_trace > 0.5 if laser_trace is not None else np.zeros(n, bool)
    excl = stim.copy()
    for a in on:
        excl[max(a - w[-1], 0):a + 1] = True
    excl[n - w[-1] - 1:] = True
    pool = np.flatnonzero(~excl)
    draws = pool[rng.integers(0, len(pool), size=(n_iter, len(off)))]
    null = np.empty((n_iter, len(w), dff.shape[1]))
    for i in range(n_iter):
        null[i] = dff[draws[i][:, None] + w[None, :]].mean(0)
    lo, hi = np.percentile(null, [0.5, 99.5], axis=0)
    sig_up = runs_of(avg > hi)
    sig_down = runs_of(avg < lo)
    return {"avg_trace": avg, "resp_trials": resp, "resp": resp.mean(0), "n_trials": len(off),
            "sig_up": sig_up, "sig_down": sig_down, "sig": runs_of((avg > hi) | (avg < lo))}


def stimulated_fiber(dff: np.ndarray, fs: float, thresh: float = 0.4):
    """The fiber carrying the laser artefact: among fibers with at least 3 laser epochs (DF/F
    above ``thresh``, epochs 4 s apart), the one with the largest DF/F. Also returns how many
    fibers have such epochs, which is more than one when the artefact spreads."""
    counts = np.array([len(laser_epochs(dff[:, j], fs, thresh)[0]) for j in range(dff.shape[1])])
    cand = np.flatnonzero(counts >= 3)
    if len(cand) == 0:
        return None, 0
    best = cand[np.argmax(dff[:, cand].max(0))]
    return int(best), int(len(cand))


def within_group_rank_corr(x, y, groups, n_perm: int, rng: np.random.Generator):
    """Correlation of x and y after ranking each within its group (as fractions of the group's
    size), pooled over groups, with a two-sided p-value from permuting y within each group."""
    df = pd.DataFrame({"x": np.asarray(x, float), "y": np.asarray(y, float), "g": np.asarray(groups)})
    df = df.dropna()
    gx = df.groupby("g").x.rank(pct=True).values
    gy = df.groupby("g").y.rank(pct=True).values
    idx = [np.flatnonzero(df.g.values == g) for g in df.g.unique()]
    r = np.corrcoef(gx, gy)[0, 1]
    null = np.empty(n_perm)
    for i in range(n_perm):
        yp = gy.copy()
        for k in idx:
            yp[k] = gy[rng.permutation(k)]
        null[i] = np.corrcoef(gx, yp)[0, 1]
    p = (1 + np.sum(np.abs(null) >= abs(r))) / (n_perm + 1)
    return r, p


def exp_fit(d: np.ndarray, y: np.ndarray):
    """Least-squares fit of y = a exp(b d) (MATLAB fit 'exp1'); returns (a, b)."""
    from scipy.optimize import curve_fit
    p0 = (float(np.nanmax(y)) if np.nanmax(y) > 0 else 0.01, -1.0)
    (a, b), _ = curve_fit(lambda x, a, b: a * np.exp(b * x), d, y, p0=p0, maxfev=20000)
    return a, b


# --- outside inputs ------------------------------------------------------------------------------

ZENODO_RECORD = "10272874"  # doi:10.5281/zenodo.10272874, the paper's data and code


class _RangeFile:
    """A read-only file over HTTP range requests, retrying when the server limits the rate."""

    def __init__(self, url):
        import requests
        self._get = requests.get
        self.url, self.pos = url, 0
        self.size = int(self._fetch(0, 0).headers["Content-Range"].split("/")[1])

    def _fetch(self, a, b):
        import time
        for k in range(10):
            r = self._get(self.url, headers={"Range": f"bytes={a}-{b}"}, timeout=120)
            if r.status_code == 206:
                return r
            time.sleep(min(60, 5 * 2 ** k))
        raise RuntimeError(f"range request to {self.url} failed with status {r.status_code}")

    def seekable(self):
        return True

    def readable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, offset, whence=0):
        self.pos = offset if whence == 0 else self.pos + offset if whence == 1 else self.size + offset
        return self.pos

    def read(self, n=-1):
        if n is None or n < 0:
            n = self.size - self.pos
        n = min(n, self.size - self.pos)
        if n <= 0:
            return b""
        data = self._fetch(self.pos, self.pos + n - 1).content
        self.pos += len(data)
        return data


def zenodo_member(zip_name: str, member: str) -> bytes:
    """One file from a zip archive of the paper's Zenodo record, read by range requests."""
    import zipfile
    url = f"https://zenodo.org/api/records/{ZENODO_RECORD}/files/{zip_name}/content"
    with zipfile.ZipFile(_RangeFile(url)) as z:
        return z.read(member)


def windows(x: np.ndarray, onsets, start: int, stop: int) -> np.ndarray:
    """Samples ``start``..``stop`` (inclusive) around each onset, NaN outside the recording
    (as eventTriggeredAverage.m pads); shape onsets x samples x columns."""
    x = np.asarray(x, float)
    if x.ndim == 1:
        x = x[:, None]
    idx = np.asarray(onsets)[:, None] + np.arange(start, stop + 1)[None, :]
    ok = (idx >= 0) & (idx < len(x))
    out = np.full(idx.shape + (x.shape[1],), np.nan)
    out[ok] = x[idx[ok]]
    return out
