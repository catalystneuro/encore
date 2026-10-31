"""Loading and measures for dandiset 000579 (Tseng et al. 2022, Neuron).

The files are streamed from the DANDI Archive at a pinned version with remfile and
h5py; nothing is written to disk. Each session is reduced as it loads to what the
analyses need (trial table, neuron labels, position-binned velocities per trial,
the velocity-LSTM outputs with their trial and position, and optionally the mean
z-scored deconvolved activity of each neuron per epoch).

Where parameters come from:
- Session fraction correct excludes visually guided trials: Methods, Behavioral
  training ("we excluded them from all analyses unless mentioned otherwise").
- Session inclusion thresholds 0.5 and 0.65: Methods, Task performance analysis.
- Maze geometry (stem 2.0 m, arm 0.5 m) and epoch lengths: read from each file's
  TaskParam metadata.
- The velocity LSTM outputs (dynamic choice, cue-biased running) are stored at 6 Hz on
  the third frame of each imaging volume; this is the files' own description.
- Position bins for running trajectories (20 or 11 equal bins of the maze): the
  readings named in the claims file (fig2c-running-variability-after-switch).
- Hierarchical bootstrap: Methods, Statistical procedures (mice, then the lower
  level; two-tailed p as twice the smaller tail).
- Sigmoid fit of block performance: Methods, Task performance analysis; the
  parameter constraints are a standard choice named in the claims file.
"""
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy.optimize import minimize

DANDISET = "000579"
VERSION = "0.230728.1727"
API = "https://api.dandiarchive.org/api"
AREAS = ["V1", "PM", "AM", "MM", "RSC", "A"]


# ---------------------------------------------------------------- archive access
def list_assets():
    """All assets of the pinned version, with fields parsed from the path."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        js = r.json()
        rows += js["results"]
        url = js["next"]
    out = []
    for a in rows:
        p = a["path"]
        m = re.search(r"session-date-([\d-]+)-area-(\w+)-(L\w+)-(single|multi)-plane", p)
        out.append(dict(path=p, asset_id=a["asset_id"], size=a["size"],
                        subject=p.split("/")[0].replace("sub-", ""),
                        kind="session" if m else "widefield",
                        date=m.group(1) if m else None,
                        fov_area=(m.group(2) if m else None),
                        layer=(m.group(3) if m else None),
                        imaging=(m.group(4) if m else None)))
    return pd.DataFrame(out)


def s3_url(asset_id):
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def open_h5(asset_id, retries=3):
    for k in range(retries):
        try:
            return h5py.File(remfile.File(s3_url(asset_id)), "r")
        except Exception:
            if k == retries - 1:
                raise
            time.sleep(2 + 3 * k)


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


# ---------------------------------------------------------------- one session
def load_session(asset_id, nbins=(20, 11), activity=False):
    """Reduce one behavior+ophys file.

    Returns a dict with:
    - 'trials': the trial table (association_mat split into P(R|W), P(L|W), P(R|B), P(L|B)),
      plus 'maze_dur' (maze epoch duration, s) and 'trial_dur' (start to stop, s).
    - 'task': TaskParam metadata; 'imaging': Imaging metadata.
    - 'neurons': one row per neuron (plane, area, depth, ml, ap).
    - 'velbin': {n: array (trials, 3, n)} mean pitch, roll, yaw velocity in n equal
      position bins of the maze (0 to stem + arm), from frames with a position.
    - 'stem_vel': (trials, 3) mean velocities over the first 25% of the stem.
    - 'rnn': DataFrame of the velocity-LSTM samples (6 Hz): trial, posF, tfc, t,
      dyn_choice (P left), cue_run (P black).
    - 'act' (if activity): per-neuron mean z-scored deconvolved activity in the stem,
      arm and feedback/ITI epochs.
    """
    f = open_h5(asset_id)
    try:
        tr = f["intervals/trials"]
        d = {}
        for k in tr.keys():
            if k in ("trial_onset_plane_frame_idx", "trial_offset_plane_frame_idx"):
                continue
            v = tr[k][:]
            if k == "association_mat":
                for j, nm in enumerate(["P_R_W", "P_L_W", "P_R_B", "P_L_B"]):
                    d[nm] = v[:, j]
            else:
                d[k] = v
        trials = pd.DataFrame(d).set_index("id")
        ep = f["intervals/epochs"]
        et = np.array([_s(x) for x in ep["epoch_type"][:]])
        eid = ep["trial_id"][:]
        dur = ep["stop_time"][:] - ep["start_time"][:]
        mz = et == "maze"
        maze_dur = pd.Series(dur[mz], index=eid[mz])
        trials["maze_dur"] = maze_dur.reindex(trials.index).values
        trials["trial_dur"] = trials["stop_time"] - trials["start_time"]

        md = f["general/harvey_lab_swac_metadata_session"]
        task = {k: (v.tolist() if isinstance(v, np.ndarray) else _s(v))
                for k, v in md["TaskParam"].attrs.items()}
        imaging = {k: (v.item() if hasattr(v, "item") else _s(v))
                   for k, v in md["Imaging"].attrs.items()}
        reg = {k: (v.tolist() if isinstance(v, np.ndarray) else _s(v))
               for k, v in md["Registration"].attrs.items()}

        seg = f["processing/ophys/ImageSegmentation"]
        nrows = []
        for pname in sorted(seg.keys()):
            ps = seg[pname]
            pi = int(pname.split("_")[-1])
            nrows.append(pd.DataFrame(dict(
                plane=pi,
                area=[_s(x) for x in ps["area"][:]],
                depth=ps["depth"][:], ml=ps["ml"][:], ap=ps["ap"][:])))
        neurons = pd.concat(nrows, ignore_index=True)

        b = f["processing/behavior"]
        ts = b["frame_aligned_position/frame_aligned_forward_and_lateral_position/timestamps"][:]
        posF = b["frame_aligned_position/frame_aligned_forward_and_lateral_position/data"][:, 0]
        tn = b["frame_aligned_trial_number/data"][:]
        tfc = b["frame_aligned_time_from_choice_point/data"][:]
        vel = b["frame_aligned_velocity/frame_aligned_pitch_roll_yaw_velocity/data"][:]
        rg = "velocity_RNN_prediction_for_choice_and_cue/velocity_RNN_prediction_for_choice_and_cue"
        rts = b[rg + "/timestamps"][:]
        rd = b[rg + "/data"][:]

        mpu = task["meter_per_virmen_unit"]
        stem = task["maze_stem_length"] * mpu
        maze_len = (task["maze_stem_length"] + task["maze_arm_length"]) * mpu
        ntr = len(trials)
        tid = trials.index.values
        ok = ~np.isnan(tn) & ~np.isnan(posF) & (posF >= 0) & (posF <= maze_len)
        ti = np.searchsorted(tid, tn[ok].astype(int))
        velbin = {}
        for n in nbins:
            bi = np.clip((posF[ok] / maze_len * n).astype(int), 0, n - 1)
            key = ti * n + bi
            cnt = np.bincount(key, minlength=ntr * n)
            out = np.full((ntr, 3, n), np.nan)
            for c in range(3):
                s = np.bincount(key, weights=vel[ok, c], minlength=ntr * n)
                with np.errstate(invalid="ignore", divide="ignore"):
                    out[:, c, :] = (s / cnt).reshape(ntr, n)
            velbin[n] = out
        e = ok & (posF < 0.25 * stem)
        tie = np.searchsorted(tid, tn[e].astype(int))
        cnt = np.bincount(tie, minlength=ntr)
        stem_vel = np.full((ntr, 3), np.nan)
        for c in range(3):
            s = np.bincount(tie, weights=vel[e, c], minlength=ntr)
            with np.errstate(invalid="ignore", divide="ignore"):
                stem_vel[:, c] = s / cnt

        idx = np.searchsorted(ts, rts)
        idx = np.clip(idx, 0, len(ts) - 1)
        rnn = pd.DataFrame(dict(t=rts, trial=tn[idx], posF=posF[idx], tfc=tfc[idx],
                                dyn_choice=rd[:, 0], cue_run=rd[:, 2],
                                ts_match=np.abs(ts[idx] - rts) < 1e-6))
        out = dict(trials=trials, task=task, imaging=imaging, registration=reg,
                   neurons=neurons, velbin=velbin, stem_vel=stem_vel, rnn=rnn,
                   n_frames=len(ts), stem=stem, maze_len=maze_len)
        if activity:
            out["act"] = _epoch_activity(f, ts, posF, tn, tfc, stem, maze_len, task)
        return out
    finally:
        f.close()


def _epoch_activity(f, ts, posF, tn, tfc, stem, maze_len, task):
    """Per-neuron mean of deconvolved activity z-scored over the session, in the stem,
    arm and feedback/ITI epochs (epoch definitions from the files' frame-aligned
    position and time from choice point; z-scoring over the whole session is the
    standard reading named in the claims file, fig4h-activity-by-epoch)."""
    o = f["processing/ophys"]
    res = []
    planes = sorted(k for k in o.keys() if k.startswith("deconvolved_activity_plane_"))
    for pn in planes:
        g = o[pn]
        pts = g["timestamps"][:]
        idx = np.clip(np.searchsorted(ts, pts), 0, len(ts) - 1)
        p, t, c = posF[idx], tn[idx], tfc[idx]
        X = g["data"][:].astype(np.float32)
        mu = X.mean(0)
        sd = X.std(0)
        sd[sd == 0] = np.nan
        Z = (X - mu) / sd
        intr = ~np.isnan(t)
        st = intr & (p >= 0) & (p < stem)
        arm = intr & (p >= stem) & (p <= maze_len)
        fb = intr & np.isnan(p) & (c >= 0)
        pi = int(pn.split("_")[-1])
        res.append(pd.DataFrame(dict(plane=pi, stem=Z[st].mean(0), arm=Z[arm].mean(0),
                                     fb_iti=Z[fb].mean(0),
                                     n_stem=st.sum(), n_arm=arm.sum(), n_fb=fb.sum())))
    return pd.concat(res, ignore_index=True)


def _load_one(args):
    import warnings
    a, act = args
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # empty epochs give NaN means, counted later
            return a, load_session(a, activity=act)
    except Exception as e:  # recorded and reported by the caller
        return a, e


def load_many(asset_ids, activity_ids=(), workers=12):
    """Load sessions in parallel processes (h5py serialises reads within a process);
    the mean epoch activity is read only for the sessions in activity_ids. Returns
    {asset_id: dict or Exception}."""
    import warnings
    from concurrent.futures import ProcessPoolExecutor
    act = set(activity_ids)
    jobs = [(a, a in act) for a in asset_ids]
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with ProcessPoolExecutor(workers) as ex:
            return dict(ex.map(_load_one, jobs))


# ---------------------------------------------------------------- statistics
def hboot(groups, nboot=10000, rng=None, stat=np.mean):
    """Hierarchical bootstrap of the mean: groups is a list (one per mouse) of 1-D
    arrays of lower-level values. Resample mice with replacement, then values within
    each resampled mouse; the bootstrap value is the mean over all resampled values
    (pooled, as the Methods describe resampling 'first of the mice and then of the
    sessions'). Returns the array of bootstrap means."""
    rng = rng or np.random.default_rng(0)
    groups = [np.asarray(g, float) for g in groups if len(g)]
    m = len(groups)
    out = np.empty(nboot)
    for i in range(nboot):
        pick = rng.integers(0, m, m)
        vals = [groups[j][rng.integers(0, len(groups[j]), len(groups[j]))] for j in pick]
        out[i] = stat(np.concatenate(vals))
    return out


def hboot_multi(groups, nboot=10000, rng=None):
    """Like hboot, for 2-D values (n, k): returns (nboot, k) bootstrap means, the same
    resampled units for every column (paired comparisons)."""
    rng = rng or np.random.default_rng(0)
    groups = [np.asarray(g, float) for g in groups if len(g)]
    m = len(groups)
    out = np.empty((nboot, groups[0].shape[1]))
    for i in range(nboot):
        pick = rng.integers(0, m, m)
        vals = np.concatenate([groups[j][rng.integers(0, len(groups[j]), len(groups[j]))]
                               for j in pick])
        out[i] = np.nanmean(vals, 0)
    return out


def p_two(boot):
    """Two-tailed p of a bootstrap distribution of a difference against zero: twice the
    smaller tail (Methods, Statistical procedures)."""
    boot = np.asarray(boot)
    return min(1.0, 2 * min((boot <= 0).mean(), (boot >= 0).mean()))


def p_unpaired(b1, b2):
    """Two non-paired bootstrap samples: twice the smaller of P(b1 > b2), P(b1 < b2)."""
    b1, b2 = np.asarray(b1, float), np.sort(np.asarray(b2, float))
    gt = np.searchsorted(b2, b1, side="left").sum() / (len(b1) * len(b2))
    lt = (len(b2) - np.searchsorted(b2, b1, side="right")).sum() / (len(b1) * len(b2))
    return min(1.0, 2 * min(gt, lt))


def bh(p, alpha=0.05):
    """Benjamini-Hochberg: returns adjusted p values."""
    p = np.asarray(p, float)
    n = len(p)
    o = np.argsort(p)
    adj = np.empty(n)
    run = 1.0
    for r in range(n - 1, -1, -1):
        run = min(run, p[o[r]] * n / (r + 1))
        adj[o[r]] = run
    return adj


# ---------------------------------------------------------------- behaviour measures
def fit_block_sigmoid(y, free_t0=False):
    """Fit r(t) = L / (1 + exp(-(t - t0)/k)) + b to a block's outcomes (1 correct, 0
    incorrect, visually guided trials removed) by minimising cross-entropy (Methods, Task
    performance analysis: "t0 is the first trial of the fitted block. L, b, and k are the
    constrained parameters"). With free_t0=False t0 is the block's first trial, as the
    Methods state; free_t0=True lets the midpoint move (a variant). Constraints (a
    standard choice named in the claims file): the rate stays in (0, 1) over the block
    and k > 0, imposed by fitting the rates at the first and last trial through a
    logistic transform. Returns the fitted values at the first and last trial."""
    y = np.asarray(y, float)
    n = len(y)
    t = np.arange(n, dtype=float)
    eps = 1e-6
    sig = lambda z: 1 / (1 + np.exp(-z))

    def curve(th):
        k = np.exp(th[2])
        t0 = th[3] if free_t0 else 0.0
        g = sig((t - t0) / k)                   # rises from g[0] to g[-1]
        a, z = sig(th[0]), sig(th[1])           # fitted rates at first and last trial
        if abs(g[-1] - g[0]) < 1e-9:
            return np.full(n, a)
        L = (z - a) / (g[-1] - g[0])
        b = a - L * g[0]
        return np.clip(L * g + b, eps, 1 - eps)

    def loss(th):
        p = curve(th)
        return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))

    best = None
    np.seterr(over="ignore")
    starts = [[0, 1.5, np.log(10), 10], [-1, 2, np.log(5), 20], [1, 1, np.log(30), 40],
              [-0.5, 1, np.log(2), 5]]
    for th0 in starts:
        r = minimize(loss, np.array(th0, float), method="Nelder-Mead",
                     options=dict(maxiter=4000, xatol=1e-6, fatol=1e-10))
        if best is None or r.fun < best.fun:
            best = r
    p = curve(best.x)
    return p[0], p[-1]


# ---------------------------------------------------------------- reinforcement learning model 4
# Methods, Reinforcement learning model; Figure S1G legend: model 4 is model 2 (single
# learning rule with choice bias and lapse, plus choice-history perseverance) with separate
# learning rates for rewarded and unrewarded trials. Q0 = 0 (Methods). Parameters:
# a_rew, a_unrew, delta (decay toward Q0), beta (inverse temperature), b0 (bias),
# phi and tau (perseverance strength and timescale, Katahira 2018), lam (lapse).
# The lapse is the standard mixture (1 - lam) P + lam / 2 (the claims file's reading, as
# the printed formula is garbled). The bias enters inside the inverse temperature, as the
# Methods print it. Visually guided trials update Q and the choice trace but are left out
# of the likelihood, as for the LSTM (Methods, LSTM model).
RL_BOUNDS = [(0, 1), (0, 1), (0, 1), (0, 50), (-5, 5), (-5, 5), (0, 1), (0, 1)]

try:
    from numba import njit
except ImportError:  # pragma: no cover
    def njit(f=None, **kw):
        return f if f is not None else (lambda g: g)


@njit(cache=False)
def rl_loglik(th, cue, cho, rew, vis, start):
    """Per-trial log2 likelihood of the actual choice (NaN on visually guided trials).
    cue: 1 black / 0 white; cho: 1 left / 0 right; rew: 1/0; start: 1 on a session's first
    trial, which resets Q and the choice trace."""
    a_r, a_u, dlt, beta, b0, phi, tau, lam = th
    n = cue.shape[0]
    out = np.empty(n)
    Q = np.zeros((2, 2))      # [cue, choice], choice 1 = left
    C = np.zeros(2)
    for t in range(n):
        if start[t]:
            Q[:, :] = 0.0
            C[:] = 0.0
        c = cue[t]
        z = beta * ((Q[c, 1] - Q[c, 0]) + phi * (C[1] - C[0]) + b0)
        if z > 30:
            z = 30.0
        if z < -30:
            z = -30.0
        pl = 1.0 / (1.0 + np.exp(-z))
        pl = (1 - lam) * pl + lam / 2
        p = pl if cho[t] == 1 else 1 - pl
        if p < 1e-12:
            p = 1e-12
        out[t] = np.nan if vis[t] else np.log2(p)
        a = a_r if rew[t] == 1 else a_u
        for cc in range(2):
            for aa in range(2):
                if cc == c and aa == cho[t]:
                    Q[cc, aa] = Q[cc, aa] + a * (rew[t] - Q[cc, aa])
                else:
                    Q[cc, aa] = dlt * Q[cc, aa]
        C[0] = (1 - tau) * C[0] + tau * (1.0 if cho[t] == 0 else 0.0)
        C[1] = (1 - tau) * C[1] + tau * (1.0 if cho[t] == 1 else 0.0)
    return out


def rl_arrays(trials_list):
    """Concatenate trial tables of several sessions into the arrays rl_loglik takes."""
    cue = np.concatenate([t.is_cueB.values.astype(np.int64) for t in trials_list])
    cho = np.concatenate([t.is_choL.values.astype(np.int64) for t in trials_list])
    rew = np.concatenate([t.is_correct.values.astype(np.float64) for t in trials_list])
    vis = np.concatenate([t.is_vis.values.astype(np.bool_) for t in trials_list])
    start = np.concatenate([np.r_[1, np.zeros(len(t) - 1)].astype(np.bool_) for t in trials_list])
    return cue, cho, rew, vis, start


def rl_fit(arrs, x0s=None):
    """Minimise the negative log likelihood over the training sessions (L-BFGS-B in place of
    Matlab's fminunc, with the bounds above). Starting points are a standard choice."""
    def nll(th):
        ll = rl_loglik(np.asarray(th, np.float64), *arrs)
        return -np.nansum(ll)
    x0s = x0s or [[0.1, 0.1, 0.9, 2, 0, 0, 0.5, 0.2], [0.3, 0.3, 0.95, 3, 0, 0.3, 0.3, 0.1],
                  [0.2, 0.05, 0.99, 1.5, 0, 0.5, 0.3, 0.05]]
    best = None
    for x0 in x0s:
        r = minimize(nll, np.array(x0, float), method="L-BFGS-B", bounds=RL_BOUNDS)
        if best is None or r.fun < best.fun:
            best = r
    return best.x
