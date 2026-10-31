"""Loading and measures for dandiset 000579 (Tseng et al. 2022, Neuron).

The files are streamed from the DANDI Archive at a pinned version with remfile and
h5py; nothing is written to disk. Each session is reduced as it loads to what the
analyses need (trial table, neuron labels, position-binned velocities per trial,
the velocity-LSTM outputs with their trial and position, and optionally the mean
z-scored deconvolved activity of each neuron per epoch).

Where parameters come from:
- Session fraction correct: two readings are computed in the notebook, with visually
  guided trials excluded (Methods, Behavioral training: "we excluded them from all
  analyses unless mentioned otherwise") and over all trials. The second is adopted as an
  assumption, as it is the one that gives the paper's neuron and session counts.
- Session inclusion thresholds 0.5 and 0.65: Methods, Task performance analysis.
- Maze geometry (stem 2.0 m, arm 0.5 m) and epoch lengths: read from each file's
  TaskParam metadata.
- The velocity LSTM outputs (dynamic choice, cue-biased running) are stored at 6 Hz on
  the third frame of each imaging volume; this is the files' own description.
- Position bins for running trajectories (20 or 11 equal bins of the maze): the
  readings named in the claims file (fig2c-running-variability-after-switch).
- Hierarchical bootstrap: Methods, Statistical procedures (mice, then the lower
  level; two-tailed p as twice the smaller tail).
- Population decoders: Methods, Trial phase-specific logistic decoders (groups of ~100
  neurons, PCA to 90% variance, elastic net 10% L1, 11 position bins, 5-fold CV); the
  readings of the penalty and the grouping are the claims file's; the fold partition
  (random frames, lassoglm's default, or whole trials) is run both ways; the penalty grid
  and solver tolerances are standard choices (see the block above decode_session).
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

        # Checks of the epoch and onset definitions: frames of the feedback delay (0 to
        # feedback_delay_sec after the choice point) that keep a maze position; frames before the
        # choice point beyond the maze end; and, per trial, the first frame with a position minus
        # the trial's start time.
        intr = ~np.isnan(tn)
        fd = intr & (tfc >= 0) & (tfc <= task["feedback_delay_sec"])
        pre = intr & (tfc < 0)
        diag = dict(fd_frames=int(fd.sum()), fd_with_pos=int((fd & ~np.isnan(posF)).sum()),
                    pre_frames=int(pre.sum()), pre_no_pos=int((pre & np.isnan(posF)).sum()),
                    pre_beyond_maze=int((pre & (posF > maze_len)).sum()),
                    max_pos=float(np.nanmax(posF)))
        hp = intr & ~np.isnan(posF)
        first = pd.Series(ts[hp]).groupby(tn[hp].astype(int)).min()
        trials["onset_lag"] = first.reindex(trials.index).values - trials["start_time"].values

        idx = np.searchsorted(ts, rts)
        idx = np.clip(idx, 0, len(ts) - 1)
        rnn = pd.DataFrame(dict(t=rts, trial=tn[idx], posF=posF[idx], tfc=tfc[idx],
                                dyn_choice=rd[:, 0], cue_run=rd[:, 2],
                                ts_match=np.abs(ts[idx] - rts) < 1e-6))
        out = dict(trials=trials, task=task, imaging=imaging, registration=reg,
                   neurons=neurons, velbin=velbin, stem_vel=stem_vel, rnn=rnn,
                   n_frames=len(ts), stem=stem, maze_len=maze_len, diag=diag)
        if activity:
            out["act"] = _epoch_activity(f, ts, posF, tn, tfc, stem, maze_len, task)
        return out
    finally:
        f.close()


def _epoch_activity(f, ts, posF, tn, tfc, stem, maze_len, task):
    """Per-neuron mean of deconvolved activity z-scored over the session, in the stem,
    arm and feedback/ITI epochs (epoch definitions from the files' frame-aligned
    position and time from choice point; z-scoring over the whole session is the
    standard reading named in the claims file, fig4h-activity-by-epoch). Stem: in-trial
    frames with position below the stem length; arm: in-trial frames with position at or
    beyond it (positions run a little past the maze end before the choice point registers);
    feedback/ITI: in-trial frames after the choice point, which have no position, so the 1 s
    feedback delay falls in this epoch (load_session's diag counts this)."""
    o = f["processing/ophys"]
    res = []
    planes = sorted(k for k in o.keys() if k.startswith("deconvolved_activity_plane_"))
    for pn in planes:
        g = o[pn]
        pts = g["timestamps"][:]
        ratio = float(np.median(pts[1:100] / ts[1:100])) if len(pts) == len(ts) else np.nan
        if len(pts) == len(ts) and ratio > 100:
            # Single-plane sessions: the plane's timestamps are labelled seconds but run about 2000
            # times the behaviour clock; the plane has one frame per behaviour frame, so frames are
            # matched by index (reported in the notebook as ts_ratio).
            idx = np.arange(len(ts))
        else:
            idx = np.clip(np.searchsorted(ts, pts), 0, len(ts) - 1)
        p, t, c = posF[idx], tn[idx], tfc[idx]
        X = g["data"][:].astype(np.float32)
        mu = X.mean(0)
        sd = X.std(0)
        sd[sd == 0] = np.nan
        Z = (X - mu) / sd
        intr = ~np.isnan(t)
        st = intr & (p >= 0) & (p < stem)
        arm = intr & (p >= stem)        # position is NaN from the choice point on (checked in diag)
        fb = intr & np.isnan(p) & (c >= 0)
        pi = int(pn.split("_")[-1])
        res.append(pd.DataFrame(dict(plane=pi, stem=Z[st].mean(0), arm=Z[arm].mean(0),
                                     fb_iti=Z[fb].mean(0),
                                     n_stem=st.sum(), n_arm=arm.sum(), n_fb=fb.sum(), ts_ratio=ratio)))
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


def rl_fit(arrs, x0s=None, return_runs=False):
    """Minimise the negative log likelihood over the training sessions (L-BFGS-B in place of
    Matlab's fminunc, with the bounds above). Starting points are a standard choice.
    With return_runs, also the negative log likelihood, success flag and iterations of every start."""
    def nll(th):
        ll = rl_loglik(np.asarray(th, np.float64), *arrs)
        return -np.nansum(ll)
    x0s = x0s or [[0.1, 0.1, 0.9, 2, 0, 0, 0.5, 0.2], [0.3, 0.3, 0.95, 3, 0, 0.3, 0.3, 0.1],
                  [0.2, 0.05, 0.99, 1.5, 0, 0.5, 0.3, 0.05]]
    best, runs = None, []
    for x0 in x0s:
        r = minimize(nll, np.array(x0, float), method="L-BFGS-B", bounds=RL_BOUNDS)
        runs.append(dict(nll=float(r.fun), success=bool(r.success), nit=int(r.nit)))
        if best is None or r.fun < best.fun:
            best = r
    if return_runs:
        return best.x, runs
    return best.x


# ---------------------------------------------------------------- population decoders
# Methods, Trial phase-specific logistic decoders: simultaneously imaged layer 2/3 neurons split
# into spatially adjacent, non-overlapping subpopulations of ~100 neurons (all neurons, no GLM
# selection); PCA to the fewest components explaining > 90% of variance; logistic regression
# (binomial, elastic net 10% L1 and 90% L2, Matlab lassoglm) on single imaging frames, one model
# per each of 11 equal position bins of the maze; 5-fold cross-validation gives a held-out
# prediction at every frame; performance as log likelihood (binary variables) or Spearman
# correlation. The penalty-strength readings (minimum CV deviance, one-SE) and the grouping
# readings (k-means on position, equal-count tiles) are the claims file's (fig3q-cue-decoding).
DEC_ALPHA = 0.1          # Methods: 10% L1, 90% L2
DEC_NBINS = 11           # Methods: 11 equally spaced position bins
DEC_NLAM = 10            # standard choice: 10 log-spaced penalties from lambda_max down to
                         # 1e-4 lambda_max (lassoglm's default range, with fewer values)
DEC_ITERS = 150          # at most 150 FISTA iterations, stopping when no coefficient moves by
DEC_TOL = 1e-5           # more than 1e-5 (standard choices, checked against sklearn's saga)


def enet_logistic_path(Z, y, train_masks, nlam=DEC_NLAM, iters=DEC_ITERS):
    """Elastic-net logistic regression (alpha = DEC_ALPHA, unpenalised intercept) fit by FISTA for
    every fold and penalty at once. Minimises, per fold f and penalty lam,
        mean over training rows of -[y log s + (1 - y) log(1 - s)]
        + lam * ((1 - alpha) / 2 * |b|^2 + alpha * |b|_1),
    which is lassoglm's objective up to a factor 2 on the deviance. y may be fractional
    (binomial with a proportion, used for dynamic choice). Z: (n, p) standardised predictors;
    train_masks: (F, n) booleans. Returns the penalties (nlam,) and held-out predictions
    P (n, nlam) for the rows outside each fold's training mask (each row is held out once)."""
    n, p = Z.shape
    F = train_masks.shape[0]
    a = DEC_ALPHA
    Z1 = np.c_[np.ones(n), Z].astype(np.float32)
    W = train_masks.astype(float) / train_masks.sum(1, keepdims=True)    # (F, n) row weights
    lam_max = np.max(np.abs(Z.T @ (y - y.mean()))) / n / a
    lams = lam_max * np.logspace(0, -4, nlam)
    lam_c = np.tile(lams, F)                                              # column -> penalty
    f_c = np.repeat(np.arange(F), nlam)                                   # column -> fold
    Wc = W[f_c].T.astype(np.float32)                                      # (n, F*nlam)
    y32 = y.astype(np.float32)[:, None]
    Lip = 0.25 * np.linalg.norm(Z1, 2) ** 2 * W.max() + lam_c * (1 - a)
    step = 1.0 / Lip
    B = np.zeros((p + 1, F * nlam), np.float32)
    ybar = np.clip((W @ y), 1e-4, 1 - 1e-4)
    B[0] = np.log(ybar / (1 - ybar))[f_c]
    Yk, tk = B.copy(), 1.0
    pen = np.ones((p + 1, 1), np.float32); pen[0] = 0
    lam_l2 = (pen * (lam_c * (1 - a))).astype(np.float32)
    step = step.astype(np.float32)
    thr = (step * lam_c * a).astype(np.float32)
    for it in range(iters):
        s = 1 / (1 + np.exp(-np.clip(Z1 @ Yk, -30, 30)))
        g = Z1.T @ ((s - y32) * Wc) + lam_l2 * Yk
        Bn = Yk - step * g
        Bn[1:] = np.sign(Bn[1:]) * np.maximum(np.abs(Bn[1:]) - thr, 0)
        tn = (1 + np.sqrt(1 + 4 * tk * tk)) / 2
        Yk = Bn + np.float32((tk - 1) / tn) * (Bn - B)
        done = it > 20 and np.max(np.abs(Bn - B)) < DEC_TOL
        B, tk = Bn, tn
        if done:
            break
    enet_logistic_path.last_iters = it + 1
    S = 1 / (1 + np.exp(-np.clip(Z1 @ B, -30, 30)))                       # (n, F*nlam)
    P = np.full((n, nlam), np.nan)
    for f in range(F):
        te = ~train_masks[f]
        P[te] = S[te][:, f * nlam:(f + 1) * nlam]
    return lams, P, B.reshape(p + 1, F, nlam)


def _choose_lambda(y, P, folds):
    """Mean held-out binomial deviance per penalty and its standard error over folds; returns the
    index of the minimum (reading a) and the largest penalty within one SE of it (reading b)."""
    eps = 1e-6
    Pc = np.clip(P, eps, 1 - eps)
    dev = -2 * (y[:, None] * np.log(Pc) + (1 - y[:, None]) * np.log(1 - Pc))
    per = np.array([dev[folds == f].mean(0) for f in np.unique(folds)])  # (F, nlam)
    m, se = per.mean(0), per.std(0, ddof=1) / np.sqrt(len(per))
    i_min = int(np.argmin(m))
    i_1se = int(np.where(m <= m[i_min] + se[i_min])[0].min())           # lams are descending
    return i_min, i_1se


def make_groups(xy, how, rng_seed=0):
    """Split neurons into spatially adjacent, non-overlapping groups of ~100: 'kmeans' (k-means
    on (ml, ap), k = round(n / 100)) or 'tiles' (equal-count tiles: round(sqrt(k)) rows by ap,
    each row split by ml into equal-count columns). The two readings of the claims file."""
    n = len(xy)
    k = max(1, int(round(n / 100)))
    if how == "kmeans":
        from sklearn.cluster import KMeans
        return KMeans(k, n_init=10, random_state=rng_seed).fit_predict(xy)
    nr = max(1, int(round(np.sqrt(k))))
    per_row = np.full(nr, k // nr); per_row[: k % nr] += 1
    lab = np.empty(n, int)
    order = np.argsort(xy[:, 1], kind="stable")
    rows = np.array_split(order, np.cumsum(per_row)[:-1] * n // k)
    g = 0
    for r, nc in zip(rows, per_row):
        o = r[np.argsort(xy[r, 0], kind="stable")]
        for c in np.array_split(o, nc):
            lab[c] = g
            g += 1
    return lab


def decode_session(asset_id, groupings=("kmeans", "tiles"), fold_kinds=("frames", "trials"),
                   variant_pairs=None, cross=True, seed=0):
    """Population decoders of one multi-plane layer 2/3 session (see the block comment above).
    Frames are imaging volumes (6 Hz); behaviour is read at the frame of the velocity-LSTM output
    (the third plane's timestamp). Frames used: maze traversal (position 0 to the maze end) of
    non-visually guided trials. Targets: cue (black = 1), reported choice (left = 1), dynamic choice
    (stored velocity-LSTM P(left), fractional). Folds: 'frames' (random frames, lassoglm's default
    partition) or 'trials' (whole trials per fold). variant_pairs limits the (grouping, folds) pairs
    run. Cross-position tests (Figure 8C, 8D): the decoder trained on one bin at the minimum-CV
    penalty, applied to every bin of the held-out trials (trial folds).
    Returns a list of dicts, one per decoder and reading."""
    from sklearn.decomposition import PCA
    from scipy.stats import spearmanr, rankdata
    rng = np.random.default_rng(seed)
    f = open_h5(asset_id)
    try:
        tr = f["intervals/trials"]
        T = pd.DataFrame({k: tr[k][:] for k in ("id", "is_vis", "is_cueB", "is_choL")}).set_index("id")
        task = {k: (v.tolist() if isinstance(v, np.ndarray) else _s(v))
                for k, v in f["general/harvey_lab_swac_metadata_session/TaskParam"].attrs.items()}
        mpu = task["meter_per_virmen_unit"]
        stem = task["maze_stem_length"] * mpu
        maze_len = (task["maze_stem_length"] + task["maze_arm_length"]) * mpu
        cue_off = (task["maze_stem_length"] + task["maze_arm_length"] - task["cue_delay_length"]) \
            / (task["maze_stem_length"] + task["maze_arm_length"])
        seg = f["processing/ophys/ImageSegmentation"]
        o = f["processing/ophys"]
        planes = sorted(k for k in o.keys() if k.startswith("deconvolved_activity_plane_"))
        xs, nb = [], []
        for pn in planes:
            ps = seg["PlaneSegmentation_" + pn.split("_")[-1]] if ("PlaneSegmentation_" + pn.split("_")[-1]) in seg \
                else seg[sorted(seg.keys())[int(pn.split("_")[-1])]]
            nb.append(pd.DataFrame(dict(area=[_s(x) for x in ps["area"][:]], ml=ps["ml"][:], ap=ps["ap"][:])))
            xs.append(o[pn]["data"])
        nlen = min(x.shape[0] for x in xs)
        b = f["processing/behavior"]
        ts = b["frame_aligned_position/frame_aligned_forward_and_lateral_position/timestamps"][:]
        posF = b["frame_aligned_position/frame_aligned_forward_and_lateral_position/data"][:, 0]
        tn = b["frame_aligned_trial_number/data"][:]
        rg = "velocity_RNN_prediction_for_choice_and_cue/velocity_RNN_prediction_for_choice_and_cue"
        rts = b[rg + "/timestamps"][:]
        dyn = b[rg + "/data"][:, 0]
        nlen = min(nlen, len(rts))
        idx = np.clip(np.searchsorted(ts, rts[:nlen]), 0, len(ts) - 1)
        p, t = posF[idx], tn[idx]
        ok = ~np.isnan(t) & ~np.isnan(p) & (p >= 0) & (p <= maze_len) & ~np.isnan(dyn[:nlen])
        ti = np.where(ok, np.nan_to_num(t), -1).astype(int)
        ok &= np.isin(ti, T.index.values)
        ok[ok] &= ~T.is_vis.reindex(ti[ok]).values.astype(bool)
        sel = np.where(ok)[0]
        X = np.hstack([x[:nlen][sel] for x in xs]).astype(np.float64)
    finally:
        f.close()
    neu = pd.concat(nb, ignore_index=True)
    trial = ti[sel]
    pos = p[sel]
    bins = np.clip((pos / maze_len * DEC_NBINS).astype(int), 0, DEC_NBINS - 1)
    targets = dict(cue=T.is_cueB.reindex(trial).values.astype(float),
                   choice=T.is_choL.reindex(trial).values.astype(float),
                   dyn=dyn[:nlen][sel].astype(float))
    utr = np.unique(trial)
    trial_fold = dict(zip(utr, rng.permutation(len(utr)) % 5))
    tfold = np.array([trial_fold[x] for x in trial])
    ffold = rng.permutation(len(trial)) % 5
    xy = neu[["ml", "ap"]].values.astype(float)
    out = []
    pairs = variant_pairs or [(g, k) for g in groupings for k in fold_kinds]
    for gname in sorted({g for g, _ in pairs}):
        lab = make_groups(xy, gname)
        for gi in np.unique(lab):
            mem = np.where(lab == gi)[0]
            cen = xy[mem].mean(0)
            near = mem[np.argmin(((xy[mem] - cen) ** 2).sum(1))]
            Xg = X[:, mem]
            pca = PCA().fit(Xg)
            npc = int(np.searchsorted(np.cumsum(pca.explained_variance_ratio_), 0.9) + 1)
            Z = pca.transform(Xg)[:, :npc]
            sd = Z.std(0); sd[sd == 0] = 1
            Z = (Z - Z.mean(0)) / sd
            for fk in [k for g, k in pairs if g == gname]:
                folds = ffold if fk == "frames" else tfold
                rec = dict(asset_id=asset_id, grouping=gname, folds=fk, group=int(gi), n_neurons=len(mem),
                           npc=npc, ml=cen[0], ap=cen[1], area=neu.area.values[near],
                           area_major=neu.area.iloc[mem].mode().iloc[0], cue_off=cue_off,
                           n_frames=len(trial), n_trials=len(utr))
                pred = {v: np.full((len(trial), 2), np.nan) for v in targets}
                for bi in range(DEC_NBINS):
                    m = bins == bi
                    if m.sum() < 50:
                        continue
                    fb = folds[m]
                    masks = np.array([fb != k for k in range(5)])
                    for v, y in targets.items():
                        yb = y[m]
                        if v != "dyn" and (yb.min() == yb.max()):
                            continue
                        lams, P, _ = enet_logistic_path(Z[m], yb, masks)
                        i_min, i_1se = _choose_lambda(yb, P, fb)
                        pred[v][m, 0] = P[:, i_min]
                        pred[v][m, 1] = P[:, i_1se]
                for li, lname in enumerate(("min", "1se")):
                    r = dict(rec, lam=lname)
                    for v, y in targets.items():
                        pv = np.clip(pred[v][:, li], 1e-6, 1 - 1e-6)
                        ll = y * np.log2(pv) + (1 - y) * np.log2(1 - pv)
                        for bi in range(DEC_NBINS):
                            m = (bins == bi) & ~np.isnan(pred[v][:, li])
                            r[f"{v}_ll_{bi}"] = ll[m].mean() if m.any() else np.nan
                        st = (pos < stem) & ~np.isnan(pred[v][:, li])
                        r[f"{v}_ll_stem"] = ll[st].mean()
                        r[f"{v}_ll_all"] = ll[~np.isnan(pred[v][:, li])].mean()
                        r[f"{v}_rho_stem"] = spearmanr(pred[v][st, li], y[st])[0]
                    # partial Spearman of the reported-choice decoder's output (Figure 4D), stem frames
                    st = (pos < stem) & ~np.isnan(pred["choice"][:, li])
                    R = np.c_[rankdata(pred["choice"][st, li]), rankdata(targets["dyn"][st]),
                              rankdata(targets["choice"][st])]
                    C = np.corrcoef(R.T)
                    pc = lambda a, b, c: (C[a, b] - C[a, c] * C[b, c]) / np.sqrt((1 - C[a, c] ** 2) * (1 - C[b, c] ** 2))
                    r["pc_dyn"] = pc(0, 1, 2)
                    r["pc_rep"] = pc(0, 2, 1)
                    out.append(r)
                if cross and fk == "trials":
                    out.append(dict(rec, lam="cross", **_cross_position(Z, bins, targets, tfold, cue_off)))
    return out


def _cross_position(Z, bins, targets, tfold, cue_off):
    """Figure 8C, 8D: per training bin, the decoder at its minimum-CV penalty (trial folds), applied
    to every bin of the held-out trials. Cue is scored as log2 likelihood over bins with the cue
    present (bin centre before the cue offset), dynamic choice as Spearman correlation."""
    from scipy.stats import spearmanr
    res = {}
    cue_bins = [b for b in range(DEC_NBINS) if (b + 0.5) / DEC_NBINS < cue_off]
    masks = np.array([tfold != k for k in range(5)])
    for v in ("cue", "dyn"):
        y = targets[v]
        use = cue_bins if v == "cue" else list(range(DEC_NBINS))
        M = np.full((DEC_NBINS, DEC_NBINS), np.nan)
        for bi in use:
            m = bins == bi
            if m.sum() < 50 or (v == "cue" and y[m].min() == y[m].max()):
                continue
            lams, P, B = enet_logistic_path(Z[m], y[m], masks[:, m])
            i_min, _ = _choose_lambda(y[m], P, tfold[m])
            for bj in use:
                mj = bins == bj
                if mj.sum() < 50:
                    continue
                pj = np.empty(mj.sum())
                for k in range(5):
                    te = tfold[mj] == k
                    zz = np.c_[np.ones(te.sum()), Z[mj][te]] @ B[:, k, i_min]
                    pj[te] = 1 / (1 + np.exp(-np.clip(zz, -30, 30)))
                yj = y[mj]
                if v == "cue":
                    pc = np.clip(pj, 1e-6, 1 - 1e-6)
                    M[bi, bj] = np.mean(yj * np.log2(pc) + (1 - yj) * np.log2(1 - pc))
                else:
                    M[bi, bj] = spearmanr(pj, yj)[0]
        res[f"x_{v}"] = M
    return res


def _decode_one(args):
    import warnings
    a, pairs = args
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return a, decode_session(a, variant_pairs=pairs)
    except Exception as e:  # recorded and reported by the caller
        return a, e


def decode_many(asset_ids, pairs, workers=4):
    """decode_session for several sessions in parallel processes. Returns {asset_id: list or Exception}."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return dict(ex.map(_decode_one, [(a, pairs) for a in asset_ids]))


def _rl_job(args):
    train, test = args
    th, runs = rl_fit(train, return_runs=True)
    return th, runs, float(np.nanmean(rl_loglik(th, *test)))


def rl_loso_many(jobs, workers=4):
    """rl_fit on each job's training arrays and the mean held-out log2 likelihood on its test
    arrays, in parallel processes. jobs: list of (train_arrays, test_arrays)."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_rl_job, jobs))
