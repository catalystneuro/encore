"""Loading and measures for the electrophysiology claims of McKenzie et al. (2025) on dandiset 000552.

McKenzie, Sommer, Donaldson, Pimentel, Kakani, Choi, Newman & English (2025), eLife 14:RP105183,
doi:10.7554/elife.105183. The paper reanalyses Huszar et al. (2022) at DANDI:000552 version
0.230630.2304 (Methods, Electrophysiology subjects), the version pinned here (`VERSION`). Files are
streamed from the archive; nothing is written to disk.

The pinned version has no cell type labels and no names for its epochs. A later version,
`LABEL_VERSION` (0.261113.1035), of the same dandiset holds the same spike times (checked unit by
unit in `cell_types`) with CellExplorer's putative cell types; `cell_types` reads only that column
from it. Claims file E3 asks for the dataset's own labels; this is the only source of them.

Where the parameters come from:

- `BIN = 0.1` s population vectors, z-scored over the first `ZWIN = 1000` s after transfer
  (Methods, ACG slope analysis; claims file E4).
- Transfer (time 0 of a run) is the start of the maze epoch (claims file E2). Tracking starts 15 to
  63 s later; time 0 at the first tracked frame is shown as a variant.
- Nearest neighbours: `K_NN = 3` most correlated vectors in the same location bin, location bins with
  at least `MIN_OCC = 1` s of occupancy, smoothed with a Gaussian of `SMOOTH_SD = 1` s (Methods, Reset
  analysis). Whether "1-s Gaussian kernel" is the standard deviation or the width is not said; the
  standard deviation is a standard choice, and the windows averaged are 60 s long.
- Location bins are 1 cm (Methods, Place field detection). They are taken on the linearized
  position, in cm, because the (x, y) position of 5 of the 9 novel runs is not in cm (0 to 1),
  though the file says cm; an assumption recorded in the attempt.
- Speed threshold `SPEED_MIN = 5` cm/s and field threshold `FIELD_HZ = 5` Hz (Methods, Place field
  detection).
- Speed is the path length along the linearized position per second. A step over `JUMP_CM` (the
  wrap of the figure-eight linearization from its end to its start) adds no length; a standard
  choice. Readings of claims file E8: (a) a second-order (constant acceleration) Kalman smoother,
  as the photometry Methods use, with process noise `KALMAN_Q` and measurement noise `KALMAN_R`
  (standard choices, the paper gives none); (b) finite differences smoothed with a 1 s Gaussian.
- Ripples are detected as the Methods say (Ripple detection; claims file E9) from the 1250 Hz LFP of
  each session's raw file, which can be read one channel at a time, on the channel with the largest
  ripple-band power before the familiar run. The Chebyshev type and the smoothing of the squared
  signal are not given: type II with 20 dB stopband attenuation, zero phase, and an 11-sample
  (8.8 ms) moving average are standard choices. The
  events deposited in the files (processing/ecephys/Ripples, Huszar et al. 2022) are a variant.
- Reactivation (Methods, Reactivation analysis): each ripple's vector is spike count over duration;
  `N_SHUF = 1000` shuffles that move each unit's value on a ripple to a random other ripple (an
  independent permutation of each unit across the pooled ripples); a ripple reactivates a moment
  when its Pearson R exceeds 99.9% of its shuffles (`ALPHA = 0.001`).
"""

from __future__ import annotations

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import curve_fit

DANDISET_ID = "000552"
VERSION = "0.230630.2304"
LABEL_VERSION = "0.261113.1035"

# Sessions of the three mice the Methods name (e13_26m1, e15_13f1, e16_3m2).
SESSIONS = [
    "e13-26m1-211019", "e13-26m1-211116", "e13-26m1-211119", "e13-26m1-211124",
    "e15-13f1-220117", "e15-13f1-220118", "e15-13f1-220119", "e15-13f1-220120",
    "e16-3m2-211210", "e16-3m2-211211", "e16-3m2-211212", "e16-3m2-211213",
]

BIN = 0.1
ZWIN = 1000.0
K_NN = 3
MIN_OCC = 1.0
SMOOTH_SD = 1.0
LOC_CM = 1.0
SPEED_MIN = 5.0
FIELD_HZ = 5.0
JUMP_CM = 20.0
KALMAN_Q = 50.0     # cm^2/s^5, white-noise jerk
KALMAN_R = 1.0      # cm^2, measurement noise
N_SHUF = 1000
ALPHA = 0.001
GAP_S = 60.0        # a gap in tracking longer than this separates two runs

_client = None


def _dandiset(version=VERSION):
    global _client
    if _client is None:
        _client = DandiAPIClient()
    return _client.get_dandiset(DANDISET_ID, version)


def asset_path(sid):
    sub = sid.rsplit("-", 1)[0]
    return f"sub-{sub}/sub-{sub}_ses-{sid}_behavior+ecephys.nwb"


def open_file(sid, version=VERSION):
    asset = _dandiset(version).get_asset_by_path(asset_path(sid))
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    return h5py.File(remfile.File(url), "r")


def _str(a):
    return [x.decode() if isinstance(x, bytes) else str(x) for x in a]


def load_session(sid):
    """Everything the analyses use from one pinned file, as numpy arrays."""
    f = open_file(sid)
    s = {"sid": sid, "subject": sid.rsplit("-", 1)[0]}
    idx = f["units/spike_times_index"][:]
    st = f["units/spike_times"][:]
    s["spikes"] = np.split(st, idx[:-1])
    s["unit_name"] = _str(f["units/unit_name"][:])
    s["spike_index"] = idx
    s["spike_times"] = st
    if "epochs" in f["intervals"]:
        s["epochs"] = np.c_[f["intervals/epochs/start_time"][:], f["intervals/epochs/stop_time"][:]]
    else:
        s["epochs"] = None
    g = f["processing/behavior"]
    s["pos_t"] = g["SubjectPosition/SpatialSeries/timestamps"][:]
    s["xy"] = g["SubjectPosition/SpatialSeries/data"][:]
    s["xy_unit"] = g["SubjectPosition/SpatialSeries/data"].attrs["unit"]
    s["lin"] = g["LinearizedPosition/LinearizedSpatialSeries/data"][:]
    s["behavior_description"] = g.attrs.get("description")
    tr = f["intervals/trials"]
    s["trials"] = {k: tr[k][:] for k in ("start_time", "stop_time", "is_familiar_maze", "recordings")}
    r = f["processing/ecephys/Ripples"]
    s["rip"] = np.c_[r["start_time"][:], r["stop_time"][:]]
    s["rip_dur"] = r["ripple_durations"][:]
    ss = g["SleepStates"]
    s["sleep"] = (np.c_[ss["start_time"][:], ss["stop_time"][:]], _str(ss["label"][:]))
    f.close()
    s["runs"] = find_runs(s)
    return s


def cell_types(sid, spike_index, spike_times=None):
    """CellExplorer putative cell types from LABEL_VERSION, after checking that its spike index and,
    when given, its spike times are identical to the pinned version's."""
    f = open_file(sid, LABEL_VERSION)
    if not np.array_equal(f["units/spike_times_index"][:], spike_index):
        raise ValueError(f"{sid}: units differ between versions")
    if spike_times is not None and not np.array_equal(f["units/spike_times"][:], spike_times):
        raise ValueError(f"{sid}: spike times differ between versions")
    ct = np.array(_str(f["units/putative_cell_type"][:]))
    env = None
    if "environment" in f["intervals/epochs"]:
        env = list(zip(f["intervals/epochs/start_time"][:], f["intervals/epochs/stop_time"][:],
                       _str(f["intervals/epochs/environment"][:])))
    f.close()
    return ct, env


def find_runs(s):
    """Maze runs: stretches of tracking separated by more than GAP_S, each with its epoch.

    Returns a list of dicts with the tracking indices, the transfer time t0 (start of the epoch that
    holds the run; the first tracked frame when the file has no epochs) and the epoch end.
    """
    t = s["pos_t"]
    cut = np.where(np.diff(t) > GAP_S)[0] + 1
    runs = []
    for seg in np.split(np.arange(len(t)), cut):
        a, b = t[seg[0]], t[seg[-1]]
        if s["epochs"] is not None:
            k = np.where((s["epochs"][:, 0] <= a) & (s["epochs"][:, 1] >= b))[0]
            t0, t1 = s["epochs"][k[0]] if len(k) else (a, b)
            ep = int(k[0]) if len(k) else None
        else:
            t0, t1, ep = a, b, None
        tm = s["trials"]
        intr = (tm["start_time"] >= t0) & (tm["start_time"] < t1)
        fam = tm["is_familiar_maze"][intr]
        runs.append(dict(idx=seg, t0=float(t0), t1=float(t1), epoch=ep, first_track=float(a),
                         last_track=float(b), n_trials=int(intr.sum()),
                         familiar=bool(fam.all()) if len(fam) else None))
    return runs


def moved_run(s, run, t0, t1):
    """The session with one run's tracking moved onto the epoch (t0, t1), and that run.

    For e16-3m2-211211, whose linear-track tracking is filed in the open-field epoch (settling.ipynb,
    finding-tracking-misfiled): moved by the difference of the epoch starts, it is tuned at zero shift.
    """
    off = t0 - run["t0"]
    s2 = dict(s)
    s2["pos_t"] = s["pos_t"].copy()
    s2["pos_t"][run["idx"]] += off
    r2 = dict(run, t0=float(t0), t1=float(t1), first_track=run["first_track"] + off,
              last_track=run["last_track"] + off)
    s2["runs"] = [r2 if r is run else r for r in s["runs"]]
    return s2, r2, off


# ---------------------------------------------------------------- behaviour

def path_length(lin):
    d = np.diff(lin)
    d[~np.isfinite(d) | (np.abs(d) > JUMP_CM)] = 0.0
    return np.r_[0.0, np.cumsum(np.abs(d))]


def kalman_va(t, p, q=KALMAN_Q, r=KALMAN_R):
    """Speed and acceleration from a constant-acceleration Kalman filter with RTS smoothing."""
    n = len(p)
    dt = np.median(np.diff(t))
    F = np.array([[1, dt, dt * dt / 2], [0, 1, dt], [0, 0, 1]])
    G = np.array([[dt ** 3 / 6], [dt ** 2 / 2], [dt]])
    Q = q * G @ G.T
    H = np.array([[1.0, 0, 0]])
    x = np.array([p[0], 0, 0.0]); P = np.eye(3) * 10
    xs = np.zeros((n, 3)); Ps = np.zeros((n, 3, 3)); xp = np.zeros((n, 3)); Pp = np.zeros((n, 3, 3))
    for i in range(n):
        if i:
            x = F @ x; P = F @ P @ F.T + Q
        xp[i] = x; Pp[i] = P
        S = (H @ P @ H.T)[0, 0] + r
        K = (P @ H.T)[:, 0] / S
        x = x + K * (p[i] - x[0]); P = P - np.outer(K, H @ P)
        xs[i] = x; Ps[i] = P
    for i in range(n - 2, -1, -1):
        C = Ps[i] @ F.T @ np.linalg.inv(Pp[i + 1])
        xs[i] = xs[i] + C @ (xs[i + 1] - xp[i + 1])
        Ps[i] = Ps[i] + C @ (Ps[i + 1] - Pp[i + 1]) @ C.T
    return xs[:, 1], xs[:, 2]


def diff_va(t, p, sd_s=1.0):
    dt = np.median(np.diff(t))
    v = np.gradient(p, t)
    v = gaussian_filter1d(v, sd_s / dt)
    a = np.gradient(v, t)
    return v, a


def run_behaviour(s, run, edges):
    """Linearized position, speed and acceleration (both readings) at the centres of the bins."""
    i = run["idx"]
    t = s["pos_t"][i]; lin = s["lin"][i]
    pl = path_length(lin)
    vk, ak = kalman_va(t, pl)
    vd, ad = diff_va(t, pl)
    c = (edges[:-1] + edges[1:]) / 2
    j = np.searchsorted(t, c)
    j = np.clip(j, 1, len(t) - 1)
    j = np.where(np.abs(t[j - 1] - c) < np.abs(t[j] - c), j - 1, j)
    ok = np.abs(t[j] - c) <= BIN
    out = {}
    for k, v in dict(lin=lin, vel_k=vk, acc_k=ak, vel_d=vd, acc_d=ad).items():
        x = v[j].astype(float)
        x[~ok] = np.nan
        out[k] = x
    out["loc"] = np.where(np.isfinite(out["lin"]), np.floor(out["lin"] / LOC_CM), np.nan)
    return out


# ---------------------------------------------------------------- spikes

def bin_counts(spikes, units, edges):
    return np.stack([np.histogram(spikes[u], edges)[0] for u in units], 1).astype(np.float32)


def run_vectors(s, run, units):
    """100 ms counts over the run epoch from transfer, and their z-score over the first ZWIN s.

    Units with no spike in the z-scoring window are dropped (their z-score is undefined).
    """
    edges = np.arange(run["t0"], run["t1"] + 1e-9, BIN)
    cnt = bin_counts(s["spikes"], units, edges)
    tb = edges[:-1] - run["t0"]
    w = tb < ZWIN
    mu = cnt[w].mean(0); sd = cnt[w].std(0)
    keep = sd > 0
    z = (cnt[:, keep] - mu[keep]) / sd[keep]
    return dict(edges=edges, t=tb, counts=cnt[:, keep], z=z.astype(np.float32),
                units=np.asarray(units)[keep], dropped=int((~keep).sum()))


def row_normalize(z):
    zc = z - z.mean(1, keepdims=True)
    n = np.linalg.norm(zc, axis=1, keepdims=True)
    n[n == 0] = np.nan
    return zc / n


# ---------------------------------------------------------------- decorrelation (Figure S6)

def expo(lag, beta, tau, c):
    return beta * np.exp(-lag / tau) + c


def decorrelation_curve(zn, t, start, length, max_lag=10.0):
    """Mean Pearson R between vectors separated by each lag (0.1 to 10 s), both inside the window."""
    m = (t >= start) & (t < start + length)
    v = zn[m]
    lags = np.arange(1, int(round(max_lag / BIN)) + 1)
    r = np.array([np.nanmean(np.sum(v[:-k] * v[k:], 1)) if k < len(v) else np.nan for k in lags])
    return lags * BIN, r


def decay_rate(lag, r):
    ok = np.isfinite(r)
    try:
        p, _ = curve_fit(expo, lag[ok], r[ok], p0=[r[ok][0] - r[ok][-1], 1.0, r[ok][-1]],
                         bounds=([-np.inf, 1e-3, -1], [np.inf, 1e3, 1]), maxfev=20000)
        return 1.0 / p[1], p
    except RuntimeError:
        return np.nan, None


# ---------------------------------------------------------------- nearest neighbours (Figure 7)

def nn_conditioned(zn, loc, valid, t, k=K_NN, exclude_visit=False):
    """For each bin, the mean R of its k most correlated bins in the same location bin.

    `valid` marks bins that take part (located, and above the speed threshold under reading b).
    Location bins with less than MIN_OCC s of valid bins are left out. Returns the mean R and the
    indices of the neighbours (-1 where missing).
    """
    n = len(zn)
    out = np.full(n, np.nan); nbr = np.full((n, k), -1)
    ok = valid & np.isfinite(loc) & np.isfinite(zn[:, 0])
    min_n = int(round(MIN_OCC / BIN))
    locs = loc[ok]
    for L in np.unique(locs):
        ii = np.where(ok & (loc == L))[0]
        if len(ii) < min_n or len(ii) <= k:
            continue
        c = zn[ii] @ zn[ii].T
        np.fill_diagonal(c, -np.inf)
        if exclude_visit:
            visit = np.cumsum(np.r_[1, np.diff(ii) > 1])
            c[visit[:, None] == visit[None, :]] = -np.inf
        top = np.argpartition(-c, k - 1, axis=1)[:, :k]
        vals = np.take_along_axis(c, top, 1)
        good = np.isfinite(vals).all(1)
        out[ii[good]] = vals[good].mean(1)
        nbr[ii[good]] = ii[top[good]]
    return out, nbr


def nn_unconditioned(zn, valid, k=K_NN, chunk=2000):
    """(a) mean R of the k most correlated bins anywhere in the run; (b) mean R with all others."""
    n = len(zn)
    ok = valid & np.isfinite(zn[:, 0])
    ii = np.where(ok)[0]
    v = zn[ii]
    topk = np.full(n, np.nan); allm = np.full(n, np.nan)
    tot = v.sum(0)
    for s0 in range(0, len(ii), chunk):
        c = v[s0:s0 + chunk] @ v.T
        rows = np.arange(c.shape[0])
        c[rows, s0 + rows] = -np.inf
        top = np.partition(c, c.shape[1] - k, axis=1)[:, -k:]
        topk[ii[s0:s0 + chunk]] = top.mean(1)
        selfdot = np.sum(v[s0:s0 + chunk] ** 2, 1)
        allm[ii[s0:s0 + chunk]] = (v[s0:s0 + chunk] @ tot - selfdot) / (len(ii) - 1)
    return topk, allm


def nan_smooth(x, sd_s=SMOOTH_SD):
    ok = np.isfinite(x)
    num = gaussian_filter1d(np.where(ok, x, 0.0), sd_s / BIN)
    den = gaussian_filter1d(ok.astype(float), sd_s / BIN)
    y = num / np.where(den > 0, den, np.nan)
    y[den < 0.05] = np.nan
    return y


def window_mean(x, t, start, length=60.0):
    m = (t >= start) & (t < start + length)
    return float(np.nanmean(x[m])) if np.isfinite(x[m]).any() else np.nan


# ---------------------------------------------------------------- ripple detection (claims file E9)

RIP_BAND = (130.0, 200.0)
RIP_PEAK_SD = 5.0
RIP_EDGE_SD = 2.0
RIP_DUR = (0.020, 0.200)
RIP_SMOOTH = 11          # samples of the moving average of the squared signal (8.8 ms at 1250 Hz)


def raw_lfp(sid):
    """The 1250 Hz LFP of a session: from the pinned version's raw file (processing/ecephys/LFP, chunked
    by channel) or, for the one session whose raw file the pinned version lacks (e13-26m1-211119), from
    the LABEL_VERSION file of the session, which holds it (processing/ecephys/LFP/LFP).
    Returns the open file, the data, the rate, the start time and the source."""
    sub = sid.rsplit("-", 1)[0]
    path = f"sub-{sub}/sub-{sub}_ses-{sid}-raw_ecephys.nwb"
    if any(a.path == path for a in _dandiset().get_assets_with_path_prefix(path)):
        asset = _dandiset().get_asset_by_path(path)
        f = h5py.File(remfile.File(asset.get_content_url(follow_redirects=1, strip_query=True)), "r")
        g = f["processing/ecephys/LFP/ElectricalSeriesLFP"]
        source = f"{VERSION} {path.split('/')[1]}"
    else:
        f = open_file(sid, LABEL_VERSION)
        g = f["processing/ecephys/LFP/LFP"]
        source = f"{LABEL_VERSION} {asset_path(sid).split('/')[1]}"
    rate = float(g["starting_time"].attrs["rate"])
    return f, g["data"], rate, float(g["starting_time"][()]), source


def _ripple_filter(x, rate):
    from scipy.signal import cheby2, filtfilt
    b, a = cheby2(4, 20, RIP_BAND, btype="band", fs=rate)
    return filtfilt(b, a, x.astype(np.float64), axis=0)


def ripple_channel(data, rate, t0, t1):
    """The channel with the largest ripple-band power over (t0, t1) s: the pyramidal layer, where
    ripples are largest (a standard choice; the Methods name no channel)."""
    x = data[int(t0 * rate):int(t1 * rate), :]
    pw = (_ripple_filter(x, rate) ** 2).mean(0)
    return int(np.argmax(pw)), pw


def detect_ripples(x, rate, start=0.0):
    """Methods, Ripple detection: 130 to 200 Hz fourth-order Chebyshev (type II, 20 dB, zero phase),
    the squared signal (moving average of RIP_SMOOTH samples) normalized to z, peaks above 5 SD,
    edges at 2 SD, durations 20 to 200 ms. Returns start, stop and peak times (s)."""
    sq = np.convolve(_ripple_filter(x, rate) ** 2, np.ones(RIP_SMOOTH) / RIP_SMOOTH, "same")
    z = (sq - sq.mean()) / sq.std()
    above = np.r_[False, z > RIP_EDGE_SD, False]
    d = np.diff(above.astype(np.int8))
    on, off = np.where(d == 1)[0], np.where(d == -1)[0]
    out = []
    for a, b in zip(on, off):
        if z[a:b].max() > RIP_PEAK_SD and RIP_DUR[0] <= (b - a) / rate <= RIP_DUR[1]:
            out.append((start + a / rate, start + b / rate, start + (a + np.argmax(z[a:b])) / rate))
    return np.array(out).reshape(-1, 3)


# ---------------------------------------------------------------- reactivation (Figure 8)

def ripple_vectors(s, units, windows, rip=None):
    """Rate vectors (spikes / duration) of the ripples (start, stop; default the deposited ones)
    starting inside any of the windows."""
    r = s["rip"] if rip is None else rip
    m = np.zeros(len(r), bool)
    for a, b in windows:
        m |= (r[:, 0] >= a) & (r[:, 0] < b)
    rr = r[m]
    dur = rr[:, 1] - rr[:, 0]
    vec = np.zeros((len(rr), len(units)), np.float32)
    for j, u in enumerate(units):
        sp = s["spikes"][u]
        vec[:, j] = (np.searchsorted(sp, rr[:, 1]) - np.searchsorted(sp, rr[:, 0])) / dur
    return vec


def reactivation(rip_vec, groups, moments, rng, n_shuf=N_SHUF, alpha=ALPHA):
    """Fraction of ripples of each group that significantly reactivate each moment.

    rip_vec: ripples x units (the pool shuffled together); groups: dict name -> boolean mask of the
    pool; moments: moments x units. Each shuffle permutes every unit independently across the pool.
    Returns dict name -> per-moment fraction (0 to 1) and the number of ripples in the group.
    """
    mn = row_normalize(moments.astype(np.float32)).T            # units x moments
    obs_n = row_normalize(rip_vec)
    obs = obs_n @ mn                                            # ripples x moments
    exceed = np.zeros(obs.shape, np.int32)
    for _ in range(n_shuf):
        shn = row_normalize(rng.permuted(rip_vec, axis=0))
        exceed += (np.nan_to_num(shn @ mn, nan=-2) >= obs)
    # significant when the observed R is above every shuffle, i.e. above their 99.9th percentile
    sig = (exceed < max(1, round(alpha * n_shuf))) & np.isfinite(obs)
    return {g: (sig[m].mean(0) if m.sum() else np.full(mn.shape[1], np.nan), int(m.sum()))
            for g, m in groups.items()}


B_SID = "e16-3m2-211211b"


def reactivation_sessions():
    """The eight tested sessions of settling.ipynb (claims file E1: a familiar run and a novel run of at
    least 660 s), each with its cell types and the ripples detected on its LFP (`rip_det`, start and
    stop; `rip_info` describes the detection), and e16-3m2-211211 under E1 reading (b) as B_SID: its
    linear-track epoch, with the tracking moved onto it (`moved_run`)."""
    out = {}
    for sid in SESSIONS:
        s = load_session(sid)
        if len(s["runs"]) < 2 or s["runs"][1]["t1"] - s["runs"][1]["t0"] < 660:
            continue
        s["cell_type"], labels = cell_types(sid, s["spike_index"])
        f, data, rate, start, source = raw_lfp(sid)
        t0 = s["runs"][0]["t0"]                     # 165 s of home cage before the familiar run
        ch, pw = ripple_channel(data, rate, t0 - 170, t0 - 5)
        ev = detect_ripples(data[:, ch], rate, start)
        f.close()
        s["rip_det"] = ev[:, :2]
        s["rip_info"] = dict(source=source, channel=ch, channels=len(pw), power_vs_median=float(pw[ch] / np.median(pw)), peaks=ev[:, 2])
        out[sid] = s
        if sid == "e16-3m2-211211":
            lin_ep = [(a, b) for a, b, e in labels if e == "linear_manu"][0]
            s2, _, _ = moved_run(s, s["runs"][1], *lin_ep)
            out[B_SID] = s2
    return out


def reactivation_windows(s, run):
    """Pre and post windows of claims file E10: pre (a) the 30 min before the run, pre (b) the first
    30 min of the recording, post the 30 min after the run."""
    rec0 = 0.0 if s["epochs"] is None else float(s["epochs"][0, 0])
    return dict(preA=(run["t0"] - 1800, run["t0"]), preB=(rec0, rec0 + 1800), post=(run["t1"], run["t1"] + 1800))


def run_moments(s, run, units, off=0.0):
    """The 100 ms moments of minute 1 and of minutes 10 to 11 (Figure 8B), counted from `off` s after
    the epoch start (0, claims file E2; the first tracked frame as a variant)."""
    V = run_vectors(s, run, units)
    t = V["t"]
    sel = np.r_[np.where((t >= off) & (t < off + 60))[0], np.where((t >= off + 600) & (t < off + 660))[0]]
    return dict(units=V["units"], z=V["z"][sel], raw=V["counts"][sel], early=t[sel] < off + 60)


def run_reactivation(s, rip, win, mo, rng, pre="preA", vec="z", pool="a", sets=("pre", "post")):
    """Percentage of the pre and post ripples that reactivate each moment, under one reading of E10.

    pre: 'preA' or 'preB'; vec: 'z' (z-scored track vectors) or 'raw' (counts); pool: 'a' (the shuffle
    moves activity within the ripple's own set) or 'b' (within pre and post together).
    """
    rv = {k: ripple_vectors(s, mo["units"], [win[pre if k == "pre" else "post"]], rip) for k in sets}
    out = {}
    if pool == "a":
        for k in sets:
            out[k] = reactivation(rv[k], {k: np.ones(len(rv[k]), bool)}, mo[vec], rng)[k]
    else:
        allv = np.concatenate([rv[k] for k in sets])
        lab = np.concatenate([[k] * len(rv[k]) for k in sets])
        out.update(reactivation(allv, {k: lab == k for k in sets}, mo[vec], rng))
    rows = []
    for k, (frac, n) in out.items():
        rows.append(dict(pre=pre, vec=vec, pool=pool, set=k, n_ripples=n,
                         early_pct=100 * np.nanmean(frac[mo["early"]]), late_pct=100 * np.nanmean(frac[~mo["early"]]),
                         all_pct=100 * np.nanmean(frac)))
    return rows


# ---------------------------------------------------------------- one run, every measure

WINDOWS = {"min1": 0.0, "min10": 600.0, "min10_alt": 540.0}   # claims file E6


def run_measures(s, run, units, kalman=True):
    """Every per-bin measure of one run that the claims use.

    Returns the bin times from transfer, the normalized vectors, behaviour, and the nearest-neighbour
    series under the speed readings of claims file E5 (all bins; bins above SPEED_MIN), with the
    neighbours' movement differences for both readings of E8.
    """
    V = run_vectors(s, run, units)
    B = run_behaviour(s, run, V["edges"])
    zn = row_normalize(V["z"])
    out = dict(t=V["t"], zn=zn, beh=B, n_units=zn.shape[1], dropped=V["dropped"], z=V["z"],
               counts=V["counts"], units=V["units"])
    located = np.isfinite(B["loc"])
    for name, valid in (("all", located), ("fast", located & (B["vel_k"] > SPEED_MIN))):
        nn, nb = nn_conditioned(zn, B["loc"], valid, V["t"])
        nnx, _ = nn_conditioned(zn, B["loc"], valid, V["t"], exclude_visit=True)
        res = dict(nn=nn, nn_s=nan_smooth(nn), nnx_s=nan_smooth(nnx), nbr=nb, valid=valid)
        for e in ("k", "d"):
            vel, acc = B[f"vel_{e}"], B[f"acc_{e}"]
            has = nb >= 0
            dv = np.where(has, np.abs(vel[:, None] - vel[np.clip(nb, 0, None)]), np.nan)
            da = np.where(has, np.abs(acc[:, None] - acc[np.clip(nb, 0, None)]), np.nan)
            with np.errstate(all="ignore"):
                res[f"dvel3_{e}"] = np.nanmean(dv, 1)
                res[f"dacc3_{e}"] = np.nanmean(da, 1)
            res[f"dvel1_{e}"] = _first_nn_diff(zn, nb, vel)
            res[f"dacc1_{e}"] = _first_nn_diff(zn, nb, acc)
        out[name] = res
    a, b = nn_unconditioned(zn, np.isfinite(zn[:, 0]))
    out["uncond_top3_s"] = nan_smooth(a)
    out["uncond_all_s"] = nan_smooth(b)
    return out


def _first_nn_diff(zn, nb, x):
    """|x(t) - x(nn)| for the single most correlated of the k neighbours."""
    n = len(zn)
    out = np.full(n, np.nan)
    has = (nb >= 0).all(1)
    i = np.where(has)[0]
    if len(i) == 0:
        return out
    r = np.einsum("ij,ikj->ik", zn[i], zn[nb[i]])
    best = nb[i, np.argmax(r, 1)]
    out[i] = np.abs(x[i] - x[best])
    return out


# ---------------------------------------------------------------- checks

def spatial_info_by_shift(counts, lin, shifts_s=(-120, -30, -5, 0, 5, 30, 120), bin_cm=4.0):
    """Mean Skaggs spatial information (bits/spike) over units, with position shifted in time.

    A check that position and spikes share a clock: information should peak at zero shift. The 4 cm
    bins are a standard choice for this check only.
    """
    ok = np.isfinite(lin)
    out = {}
    for sh in shifts_s:
        k = int(round(sh / BIN))
        l2 = np.roll(lin, k)
        m = ok & np.isfinite(l2)
        if k > 0:
            m[:k] = False
        elif k < 0:
            m[k:] = False
        loc = np.floor(l2[m] / bin_cm).astype(int)
        c = counts[m]
        occ = np.bincount(loc).astype(float)
        good = occ > 0
        p = occ[good] / occ.sum()
        info = []
        for j in range(c.shape[1]):
            r = np.bincount(loc, weights=c[:, j], minlength=len(occ))[good] / occ[good]
            lam = (p * r).sum()
            if lam <= 0:
                continue
            q = r / lam
            info.append(np.nansum(p * q * np.log2(np.where(q > 0, q, 1))))
        out[sh] = float(np.mean(info))
    return out


# ---------------------------------------------------------------- place fields (Figure S7A, B)

def field_deviations(M, speed_for_dev=False):
    """Per-bin mean deviation of z-scored rates from the place map, in field and out of field.

    Maps (Methods, Place field detection): 1 cm linearized bins, bins above SPEED_MIN, location bins
    with more than MIN_OCC s; the map is the mean z-scored rate, the field the bins whose mean
    unnormalized rate exceeds FIELD_HZ. Units with no field bin are left out. Deviations are taken
    at every located bin (reading a) or only above SPEED_MIN (reading b, `speed_for_dev`).
    """
    B = M["beh"]
    loc = B["loc"]; fast = B["vel_k"] > SPEED_MIN
    z = M["z"]; hz = M["counts"] / BIN
    ok = np.isfinite(loc) & fast
    L = loc[ok].astype(int)
    nL = int(np.nanmax(loc)) + 1
    occ = np.bincount(L, minlength=nL) * BIN
    zmap = np.stack([np.bincount(L, weights=z[ok, j], minlength=nL) for j in range(z.shape[1])], 1)
    hmap = np.stack([np.bincount(L, weights=hz[ok, j], minlength=nL) for j in range(z.shape[1])], 1)
    n = np.maximum(np.bincount(L, minlength=nL), 1)[:, None]
    zmap /= n; hmap /= n
    good = occ > MIN_OCC
    field = (hmap > FIELD_HZ) & good[:, None]
    has_field = field.any(0)
    use = np.isfinite(loc) & (fast if speed_for_dev else True)
    use &= np.isfinite(loc) & good[np.nan_to_num(loc, nan=0).astype(int).clip(0, nL - 1)]
    idx = np.where(use)[0]
    li = loc[idx].astype(int)
    dev = z[idx][:, has_field] - zmap[li][:, has_field]
    inf = field[li][:, has_field]
    with np.errstate(invalid="ignore"):
        d_in = np.where(inf.sum(1) > 0, (dev * inf).sum(1) / inf.sum(1), np.nan)
        d_out = np.where((~inf).sum(1) > 0, (dev * ~inf).sum(1) / (~inf).sum(1), np.nan)
    t = M["t"][idx]
    return t, d_in, d_out, int(has_field.sum())


def minute_slope(t, x, minutes=10):
    m = np.array([np.nanmean(x[(t >= 60 * k) & (t < 60 * (k + 1))]) for k in range(minutes)])
    ok = np.isfinite(m)
    return (np.polyfit(np.arange(minutes)[ok], m[ok], 1)[0] if ok.sum() > 2 else np.nan), m


# ---------------------------------------------------------------- model of NN similarity (Figure S7E, F)

def _design(t, dv, da, terms, p):
    """Prediction of the model with the given terms; p holds every parameter."""
    b0, b1, r1, b2, r2, bv, ba = p
    y = np.zeros_like(t)
    if "intercept" in terms:
        y = y + b0
    if "time" in terms:
        y = y + b1 * np.exp(-r1 * t) - b2 * np.exp(-r2 * t)
    if "vel" in terms:
        y = y + bv * dv
    if "acc" in terms:
        y = y + ba * da
    return y


def fit_nn_model(t, dv, da, y, terms, form):
    """Fit one model; form 'exp' or 'exp_pos' (photometry Methods form, rates bounded as there) or 'linear'."""
    from scipy.optimize import least_squares
    if form == "linear":
        cols = []
        names = []
        if "intercept" in terms:
            cols.append(np.ones_like(t)); names.append("b0")
        if "time" in terms:
            cols.append(t); names.append("bt")
        if "vel" in terms:
            cols.append(dv); names.append("bv")
        if "acc" in terms:
            cols.append(da); names.append("ba")
        X = np.stack(cols, 1)
        beta = np.linalg.lstsq(X, y, rcond=None)[0]
        return ("linear", terms, beta)
    # every beta bounded at +-10 (photometry Methods, "All beta values were bound at +-10 s.t.d."), so the
    # fast term can describe a rise as well as a fall; form 'exp_pos' keeps both betas >= 0, the signs
    # the Methods give the two terms ("a positive term ... and a negative term")
    lo = np.array([-10, -10, 0.001, -10, 0.0001, -10, -10.0])
    hi = np.array([10, 10, 0.1, 10, 0.001, 10, 10.0])
    if form == "exp_pos":
        lo[[1, 3]] = 0
    p0 = np.array([np.mean(y), 0.1, 0.01, 0.01, 0.0005, 0, 0])
    res = least_squares(lambda p: _design(t, dv, da, terms, p) - y, p0, bounds=(lo, hi))
    return (form, terms, res.x)


def predict_nn_model(model, t, dv, da):
    form, terms, p = model
    if form != "linear":
        return _design(t, dv, da, terms, p)
    cols = []
    if "intercept" in terms:
        cols.append(np.ones_like(t))
    if "time" in terms:
        cols.append(t)
    if "vel" in terms:
        cols.append(dv)
    if "acc" in terms:
        cols.append(da)
    return np.stack(cols, 1) @ p


FULL = ("intercept", "time", "vel", "acc")


def cv_percent_change(data, form):
    """Leave-one-session-out CVMSE of the full model and of each reduced one (Methods, Reset analysis).

    data: list of (t, dv, da, y) per session. Returns dict dropped term -> per-session percent change
    in CVMSE relative to the full model.
    """
    out = {k: [] for k in FULL}
    for i in range(len(data)):
        tr = [d for j, d in enumerate(data) if j != i]
        T, DV, DA, Y = (np.concatenate([d[k] for d in tr]) for k in range(4))
        t, dv, da, y = data[i]
        full = fit_nn_model(T, DV, DA, Y, FULL, form)
        mse_full = np.mean((predict_nn_model(full, t, dv, da) - y) ** 2)
        for drop in FULL:
            terms = tuple(x for x in FULL if x != drop)
            m = fit_nn_model(T, DV, DA, Y, terms, form)
            mse = np.mean((predict_nn_model(m, t, dv, da) - y) ** 2)
            out[drop].append(100 * (mse - mse_full) / mse_full)
    return {k: np.array(v) for k, v in out.items()}


def location_2d(s, run, t):
    """1 x 1 cm (x, y) location bins at the bin times t (from transfer), for runs whose x, y are in cm.

    The Methods' bins (Place field detection) are 1 x 1 cm of the mouse's location; this is that reading,
    usable only where the file's x, y are in cm (`None` otherwise).
    """
    i = run["idx"]
    ts = s["pos_t"][i]; xy = s["xy"][i]
    if np.nanmax(xy) <= 1.5:
        return None
    c = t + BIN / 2 + run["t0"]
    j = np.clip(np.searchsorted(ts, c), 1, len(ts) - 1)
    j = np.where(np.abs(ts[j - 1] - c) < np.abs(ts[j] - c), j - 1, j)
    ok = np.abs(ts[j] - c) <= BIN
    return np.where(ok, np.floor(xy[j, 0] / LOC_CM) * 10000 + np.floor(xy[j, 1] / LOC_CM), np.nan)
