"""Loading and measures for the maze-task array data of dandiset 000140 (MC_Maze_Small).

Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68:387-400,
doi:10.1016/j.neuron.2010.09.015. Claims: claims/000140/10.1016-j.neuron.2010.09.015.yaml.

The train file holds 100 trials of monkey J (Jenkins) on 2009-09-28, 27 maze conditions
(`maze_id` x `trial_version`), 142 units from two 96-electrode arrays, and hand position and
velocity at 1 kHz. The test file holds 100 segments of 0.7 s with no condition, go cue or
behaviour, so only the train file is used. Files are streamed; nothing is written to disk.

Where the parameters come from (C = the claim's criterion or the claims file header, which
cite the paper; P = a passage of the paper taken by the author, step 1.6; A = an assumption;
S = a standard choice for a detail that cannot change a result):

- Delay > 400 ms (C; Methods, Task design and behavior).
- Spike trains smoothed with a 20 ms Gaussian before averaging (C; Supplemental Experimental
  Procedures, Computing the mean firing rate versus time). The width is taken as the SD (S).
- Preparatory epoch -200 to +100 ms around the go cue; peri-movement epoch -100 to +350 ms
  around movement onset (C; Methods, Correlations).
- Inclusion > 5 spikes/s of preparatory tuning; peri-movement tuning >= 1.5 times it (C;
  Methods). Tuning is the range (reading O1a) or SD (O1b) across conditions (C, header O1).
- Movement onset: the dataset's `move_onset_time` (O3a) or the first time after the go cue
  that hand speed reaches `ONSET_FRACTION` of the trial's peak (O3b) (C, header O3). The
  fraction 0.15 is a common choice (A, shown with O3a).
- Trial filter: velocity profiles correlated with a proto-trial at r > 0.9 (C; Supplemental
  Experimental Procedures). Proto-trial readings O4a, O4b, O4c (C). The window of the profiles,
  150 ms before to 800 ms after movement onset, is the peri-movement window (P; Methods,
  PCA-based spaces) (S).
- Peri-movement T matrix: condition means 150 ms before to 800 ms after movement onset
  (maze task), all units but the fitted one, not normalised, columns mean-centred (C; Methods,
  PCA-based spaces; Supplemental Text). Samples every 10 ms (C, header O5).
- PD performance: leave-one-condition-out linear regression with offset; one minus the mean
  squared prediction error over the variance across conditions (C; Methods, PD performance).
  The variance is taken with ddof 0 (S).
- Kinematic T matrix: horizontal and vertical position, velocity and acceleration from 150 ms
  before movement onset to the end of the reach (600 or 800 ms, C), each variable scaled to
  unity range across times and conditions (C; Methods). Acceleration is the time derivative of
  the dataset's hand velocity after a 20 ms Gaussian (S).
- Task spaces as the Methods list them (Task spaces). The reach ends at the last time within
  800 ms of onset at which speed is at least `REACH_END_FRACTION` of its peak (A); the
  maximum velocity component is the signed value of largest magnitude (A); segments are of
  equal path length, with equal duration as a variant (A).
- Upper limit of PD performance: PCA space of the c x n preparatory matrix (C; Supplemental
  Experimental Procedures, Estimating the upper limit), here without the fitted unit, as for the
  peri-movement space (A).
- Array of a unit: the first digit of its id (1 or 2). The file's `units/electrodes` points every
  unit to the PMd electrode group, and the electrodes table has no positions; unit ids
  1xxx map to electrode index xx-1 of that table, which is the PMd group, so prefix 1 is read
  as PMd and prefix 2 as M1 (A).
"""

from __future__ import annotations

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "000140"
DANDISET_VERSION = "0.220113.0408"
TRAIN_PATH = "sub-Jenkins/sub-Jenkins_ses-small_desc-train_behavior+ecephys.nwb"
TEST_PATH = "sub-Jenkins/sub-Jenkins_ses-small_desc-test_ecephys.nwb"

MIN_DELAY_MS = 400
SMOOTH_SD_MS = 20
PREP_WIN = (-200, 100)        # ms re go cue
PERI_WIN = (-100, 350)        # ms re movement onset
T_WIN = (-150, 800)           # ms re movement onset, maze task
STEP_MS = 10
GO_SPAN = (-300, 200)         # stored go-locked span, ms
MV_SPAN = (-400, 900)         # stored movement-locked span, ms
PREP_TUNING_MIN = 5.0         # spikes/s, array data
PERI_RATIO_MIN = 1.5
ONSET_FRACTION = 0.15
REACH_END_FRACTION = 0.10
PROTO_R_MIN = 0.9


def asset_urls() -> dict:
    """Streaming URL of each NWB file at the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)
                for a in ds.get_assets()}


def _txt(v):
    return v.decode() if isinstance(v, bytes) else str(v)


def load_train(url: str) -> dict:
    """Trials, units, spikes and hand kinematics of the train file."""
    with h5py.File(remfile.File(url), "r") as f:
        T = f["intervals/trials"]
        cols = ["start_time", "stop_time", "trial_type", "trial_version", "maze_id", "success",
                "target_on_time", "go_cue_time", "move_onset_time", "rt", "delay",
                "num_targets", "num_barriers", "active_target"]
        trials = pd.DataFrame({c: T[c][()] for c in cols})
        trials["split"] = [_txt(s) for s in T["split"][()]]
        tp, tpi = T["target_pos"][()], T["target_pos_index"][()]
        starts = np.r_[0, tpi[:-1]]
        trials["target_x"] = [tp[s + a, 0] for s, a in zip(starts, trials.active_target)]
        trials["target_y"] = [tp[s + a, 1] for s, a in zip(starts, trials.active_target)]
        U = f["units"]
        ids = U["id"][()]
        st, sti = U["spike_times"][()], U["spike_times_index"][()]
        spikes = np.split(st, sti[:-1])
        E = f["general/extracellular_ephys/electrodes"]
        units = pd.DataFrame({
            "id": ids,
            "electrode": U["electrodes"][()],
            "heldout": U["heldout"][()],
        })
        units["electrode_group"] = [_txt(E["group_name"][()][e]) for e in units.electrode]
        units["array_prefix"] = ids // 1000
        units["channel"] = (ids // 10) % 100
        units["array"] = np.where(units.array_prefix == 1, "PMd", "M1")
        B = f["processing/behavior"]
        beh = {"t": B["hand_pos/timestamps"][()], "pos": B["hand_pos/data"][()],
               "vel": B["hand_vel/data"][()]}
        meta = {
            "electrode_xyz_all_nan": bool(np.all(np.isnan(np.c_[E["x"][()], E["y"][()], E["z"][()]]))),
            "electrode_groups": pd.Series([_txt(g) for g in E["group_name"][()]]).value_counts().to_dict(),
            "pos_unit": B["hand_pos/data"].attrs["unit"], "pos_conversion": float(B["hand_pos/data"].attrs["conversion"]),
            "vel_unit": B["hand_vel/data"].attrs["unit"], "vel_conversion": float(B["hand_vel/data"].attrs["conversion"]),
            "pos_description": _txt(B["hand_pos"].attrs["description"]),
            "vel_description": _txt(B["hand_vel"].attrs["description"]),
            "session_start": _txt(f["session_start_time"][()]),
            "subject": _txt(f["general/subject/subject_id"][()]),
            "obs_intervals": U["obs_intervals"][()],
        }
    conds = trials[["maze_id", "trial_version"]].drop_duplicates().sort_values(["maze_id", "trial_version"])
    cmap = {tuple(r): i for i, r in enumerate(conds.values)}
    trials["cond"] = [cmap[(m, v)] for m, v in zip(trials.maze_id, trials.trial_version)]
    return {"trials": trials, "units": units, "spikes": spikes, "beh": beh, "meta": meta,
            "conditions": conds.reset_index(drop=True)}


def load_test(url: str) -> dict:
    """The test file: segment table, units and spikes (no conditions or behaviour)."""
    with h5py.File(remfile.File(url), "r") as f:
        T = f["intervals/trials"]
        trials = pd.DataFrame({c: T[c][()] for c in ["start_time", "stop_time", "move_onset_time"]})
        U = f["units"]
        st, sti = U["spike_times"][()], U["spike_times_index"][()]
        return {"trials": trials, "ids": U["id"][()], "spikes": np.split(st, sti[:-1]),
                "heldout": U["heldout"][()], "colnames": [_txt(c) for c in T.attrs["colnames"]],
                "has_behavior": "processing/behavior" in f}


# ---------------------------------------------------------------- kinematics per trial

def _trial_slice(beh, t0, t1):
    i0, i1 = np.searchsorted(beh["t"], [t0 - 1e-6, t1 + 1e-6])
    return beh["t"][i0:i1], beh["pos"][i0:i1], beh["vel"][i0:i1]


def speed_onset(beh, trial, fraction=ONSET_FRACTION) -> float:
    """O3b: first time after the go cue that hand speed reaches `fraction` of its trial peak."""
    t, _, v = _trial_slice(beh, trial.go_cue_time, trial.stop_time)
    sp = np.hypot(v[:, 0], v[:, 1])
    return float(t[np.argmax(sp >= fraction * sp.max())])


def trial_kinematics(beh, onset: float, span=MV_SPAN) -> dict:
    """Movement-locked position, velocity and acceleration at 1 ms (mm, mm/s, mm/s^2)."""
    lags = np.arange(span[0], span[1] + 1) / 1000.0
    t, p, v = _trial_slice(beh, onset + span[0] / 1000 - 0.05, onset + span[1] / 1000 + 0.05)
    pos = np.c_[np.interp(onset + lags, t, p[:, 0]), np.interp(onset + lags, t, p[:, 1])]
    vel = np.c_[np.interp(onset + lags, t, v[:, 0]), np.interp(onset + lags, t, v[:, 1])]
    acc = np.gradient(gaussian_filter1d(vel, SMOOTH_SD_MS, axis=0), axis=0) * 1000.0
    return {"lags_ms": np.arange(span[0], span[1] + 1), "pos": pos, "vel": vel, "acc": acc}


# ---------------------------------------------------------------- rates per trial

def trial_rates(data: dict, onsets: np.ndarray, trial_idx) -> tuple[np.ndarray, np.ndarray]:
    """Smoothed rates (spikes/s, float32) of every unit, go-locked over GO_SPAN and
    movement-locked over MV_SPAN, for the given trials. Spikes are binned at 1 ms over the
    whole trial and smoothed with a Gaussian of SD 20 ms before the windows are cut."""
    tr = data["trials"]
    n_units = len(data["spikes"])
    go_lags = np.arange(GO_SPAN[0], GO_SPAN[1] + 1)
    mv_lags = np.arange(MV_SPAN[0], MV_SPAN[1] + 1)
    R_go = np.zeros((len(trial_idx), n_units, len(go_lags)), np.float32)
    R_mv = np.zeros((len(trial_idx), n_units, len(mv_lags)), np.float32)
    for j, i in enumerate(trial_idx):
        t0, t1 = tr.start_time.iat[i], tr.stop_time.iat[i]
        nb = int(round((t1 - t0) * 1000))
        counts = np.zeros((n_units, nb), np.float32)
        for u, s in enumerate(data["spikes"]):
            s = s[(s >= t0) & (s < t1)]
            b = np.minimum(((s - t0) * 1000).astype(int), nb - 1)
            np.add.at(counts[u], b, 1.0)
        rate = gaussian_filter1d(counts, SMOOTH_SD_MS, axis=1, mode="reflect") * 1000.0
        g = int(round((tr.go_cue_time.iat[i] - t0) * 1000))
        m = int(round((onsets[i] - t0) * 1000))
        R_go[j] = rate[:, g + go_lags]
        R_mv[j] = rate[:, m + mv_lags]
    return R_go, R_mv


# ---------------------------------------------------------------- trial filter (O4)

def proto_filter(vel_profiles: np.ndarray, conds: np.ndarray, reading: str) -> np.ndarray:
    """Keep trials whose horizontal and vertical velocity profiles both correlate with the
    condition's proto-trial at r > 0.9. reading 'a': the proto-trial is the trial best
    correlated with the condition mean; 'b': the condition mean itself; 'c': no filter.
    vel_profiles: trials x time x 2."""
    keep = np.ones(len(conds), bool)
    if reading == "c":
        return keep
    for c in np.unique(conds):
        idx = np.flatnonzero(conds == c)
        if len(idx) < 2:
            continue
        V = vel_profiles[idx]
        mean = V.mean(0)
        r_mean = np.array([[np.corrcoef(v[:, d], mean[:, d])[0, 1] for d in (0, 1)] for v in V])
        if reading == "b":
            ok = np.all(r_mean > PROTO_R_MIN, axis=1)
        else:
            proto = V[np.argmax(r_mean.mean(1))]
            r = np.array([[np.corrcoef(v[:, d], proto[:, d])[0, 1] for d in (0, 1)] for v in V])
            ok = np.all(r > PROTO_R_MIN, axis=1)
        keep[idx] = ok
    return keep


def condition_means(X: np.ndarray, conds: np.ndarray, n_cond: int) -> np.ndarray:
    """Mean over trials of each condition, first axis trials."""
    return np.stack([X[conds == c].mean(0) for c in range(n_cond)])


# ---------------------------------------------------------------- tuning and correlations

def epoch_mean(CM, lags, win):
    sel = (lags >= win[0]) & (lags <= win[1])
    return CM[..., sel].mean(-1)


def tuning(V: np.ndarray, measure: str) -> np.ndarray:
    """Across-condition tuning strength of each column of V (conditions first):
    'range' (O1a) or 'sd' (O1b, ddof 0)."""
    return np.ptp(V, axis=0) if measure == "range" else V.std(axis=0)


def peri_tuning(CM_mv, mv_lags, peri_rates, measure: str, reading: str) -> np.ndarray:
    """O2: (i) tuning of the peri-movement epoch means, (ii) the largest across-condition
    tuning at any time from 100 ms before to 350 ms after movement onset."""
    if reading == "i":
        return tuning(peri_rates, measure)
    sel = (mv_lags >= PERI_WIN[0]) & (mv_lags <= PERI_WIN[1])
    X = CM_mv[:, :, sel]
    t = np.ptp(X, axis=0) if measure == "range" else X.std(axis=0)
    return t.max(-1)


def rowwise_corr(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Pearson r between matching columns of A and B (conditions x units)."""
    a = A - A.mean(0)
    b = B - B.mean(0)
    return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))


# ---------------------------------------------------------------- PD performance

def loo_performance(x: np.ndarray, S: np.ndarray) -> float:
    """Leave-one-condition-out performance of x ~ b0 + S b: one minus the mean squared
    prediction error over the variance of x across conditions (Methods, PD performance).
    Uses the closed form of the leave-one-out residual, e_i / (1 - h_ii)."""
    X = np.c_[np.ones(len(x)), S]
    H = X @ np.linalg.pinv(X)
    h = np.diag(H)
    if np.any(h > 1 - 1e-8):
        return np.nan
    press = (x - H @ x) / (1 - h)
    return 1.0 - np.mean(press ** 2) / np.var(x)


def loo_performance_curve(x, scores, kmax):
    return np.array([loo_performance(x, scores[:, :k]) for k in range(1, kmax + 1)])


def gram_scores(G: np.ndarray, kmax: int) -> np.ndarray:
    """PC scores (c x kmax) of a column-centred matrix from its c x c Gram matrix."""
    w, V = np.linalg.eigh(G)
    order = np.argsort(w)[::-1][:kmax]
    return V[:, order] * np.sqrt(np.clip(w[order], 0, None))


def leave_one_out_scores(blocks: np.ndarray, kmax: int, members=None) -> list[np.ndarray]:
    """For each unit j, the PC scores of the matrix of all other units' blocks.
    blocks: conditions x units x features (each unit's columns of the T matrix).
    members: optional boolean mask of units allowed in the space (others are left out)."""
    c, n, _ = blocks.shape
    Bc = blocks - blocks.mean(0, keepdims=True)
    per_unit = np.einsum("aif,bif->iab", Bc, Bc)         # n x c x c
    if members is None:
        members = np.ones(n, bool)
    G = per_unit[members].sum(0)
    out = []
    for j in range(n):
        Gj = G - per_unit[j] if members[j] else G
        out.append(gram_scores(Gj, kmax))
    return out


def pca_scores(M: np.ndarray, kmax: int) -> np.ndarray:
    Mc = M - M.mean(0)
    return gram_scores(Mc @ Mc.T, kmax)


def n_components_for(M: np.ndarray, frac=0.9) -> tuple[int, np.ndarray]:
    Mc = M - M.mean(0)
    s = np.linalg.svd(Mc, compute_uv=False)
    ev = s ** 2 / np.sum(s ** 2)
    return int(np.searchsorted(np.cumsum(ev), frac) + 1), ev


# ---------------------------------------------------------------- kinematic and task spaces

def kinematic_matrix(KIN: dict, end_ms: int) -> np.ndarray:
    """c x (6 t) matrix of condition-mean x and y position, velocity and acceleration from
    150 ms before onset to `end_ms`, every 10 ms, each variable scaled to unity range."""
    lags = KIN["lags_ms"]
    sel = (lags >= T_WIN[0]) & (lags <= end_ms) & ((lags - T_WIN[0]) % STEP_MS == 0)
    cols = []
    for key in ("pos", "vel", "acc"):
        for d in (0, 1):
            v = KIN[key][:, sel, d]
            cols.append(v / np.ptp(v))
    return np.concatenate(cols, axis=1)


def _resample_path(p, n_pts):
    seg = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]
    targets = np.linspace(0, seg[-1], n_pts)
    return np.c_[np.interp(targets, seg, p[:, 0]), np.interp(targets, seg, p[:, 1])], seg


def task_features(kin: dict, segments: str = "length") -> dict:
    """Task-space features of one trial (Methods, Task spaces)."""
    lags, pos, vel = kin["lags_ms"], kin["pos"], kin["vel"]
    sp = np.hypot(vel[:, 0], vel[:, 1])
    after = (lags >= 0) & (lags <= 800)
    i0 = np.flatnonzero(lags == 0)[0]
    peak = sp[after].max()
    above = np.flatnonzero(after & (sp >= REACH_END_FRACTION * peak))
    i_end = above[-1]
    path = pos[i0:i_end + 1]
    start, end = path[0], path[-1]
    d = end - start
    L = np.hypot(*d)
    cross = (d[0] * (path[:, 1] - start[1]) - d[1] * (path[:, 0] - start[0])) / max(L, 1e-9)
    i_exc = np.argmax(np.abs(cross))
    i_ccw = np.argmax(cross)
    first150 = (lags >= 0) & (lags < 150)
    v_r = vel[i0:i_end + 1]
    vmax = np.array([v_r[np.argmax(np.abs(v_r[:, k])), k] for k in (0, 1)])
    half, _ = _resample_path(path, 3)
    if segments == "length":
        pts, _ = _resample_path(path, 4)
    else:
        idx = np.linspace(0, len(path) - 1, 4).round().astype(int)
        pts = path[idx]
    segs = np.diff(pts, axis=0).ravel()
    return {
        "initial_velocity": vel[first150].mean(0),
        "endpoint": end,
        "max_speed": np.array([peak]),
        "orth_excursion": np.array([cross[i_exc]]),
        "viapoint": path[i_exc],
        "max_velocity": vmax,
        "halfpoint": half[1],
        "segments": segs,
        "max_ccw_excursion": np.array([cross[i_ccw]]),
        "ccw_location": path[i_ccw],
        "reach_end_ms": np.array([lags[i_end]]),
    }


TASK_SPACES = {
    "initial vel.": ["initial_velocity"],
    "endpoints + max. spd.": ["endpoint", "max_speed"],
    "endpoints + orth. exc.": ["endpoint", "orth_excursion"],
    "endpoints + viapoint": ["endpoint", "viapoint"],
    "endpoints + max. vel.": ["endpoint", "max_velocity"],
    "endpoints + halfpoint": ["endpoint", "halfpoint"],
    "segment dirs.": ["segments"],
    "kitchen sink": ["segments", "max_ccw_excursion", "ccw_location", "barriers", "distractors"],
}


def task_space_matrices(feats: list[dict], trials: pd.DataFrame, conds: np.ndarray, n_cond: int) -> dict:
    """Condition means of each task space (c x dim)."""
    F = {}
    keys = feats[0].keys()
    for k in keys:
        F[k] = condition_means(np.stack([f[k] for f in feats]), conds, n_cond)
    F["barriers"] = condition_means((trials.num_barriers.values > 0).astype(float)[:, None], conds, n_cond)
    F["distractors"] = condition_means((trials.num_targets.values > 1).astype(float)[:, None], conds, n_cond)
    return {name: np.concatenate([F[p] for p in parts], axis=1) for name, parts in TASK_SPACES.items()}


# ---------------------------------------------------------------- PD consistency

def pd_consistency(x, S, rng, n_draw=25, n_rep=100, standardize=False) -> float:
    """Mean dot product of two unit-length PDs, each fitted on n_draw conditions drawn with
    replacement (Results, Stability of the PD). Draws where a PD is zero (the unit's rate is
    the same in every drawn condition) are dropped. Axes are z-scored across conditions
    when `standardize` (an open reading: the paper does not give the axes' scale)."""
    if standardize:
        S = (S - S.mean(0)) / S.std(0)
    c = len(x)
    dots = []
    for _ in range(n_rep):
        bs = []
        for _ in range(2):
            idx = rng.integers(0, c, n_draw)
            X = np.c_[np.ones(n_draw), S[idx]]
            b = np.linalg.lstsq(X, x[idx], rcond=None)[0][1:]
            nb = np.linalg.norm(b)
            bs.append(b / nb if nb > 0 else None)
        if bs[0] is not None and bs[1] is not None:
            dots.append(bs[0] @ bs[1])
    return float(np.mean(dots)) if dots else np.nan


# ---------------------------------------------------------------- Figure 8 simulation

def simulate_rotation(rng, n_cond=25, hold=100, n_steps=360, init="disk"):
    """x(t+1) = W x(t), W = [[1, -2pi/360], [2pi/360, 1]] (Figure 8 legend), after holding the
    initial state for `hold` steps. Returns initial states (c x 2) and released trajectories
    (c x n_steps x 2)."""
    if init == "disk":
        r = np.sqrt(rng.uniform(0, 1, n_cond))
        th = rng.uniform(0, 2 * np.pi, n_cond)
        x0 = np.c_[r * np.cos(th), r * np.sin(th)]
    else:
        x0 = rng.uniform(-1, 1, (n_cond, 2))
    a = 2 * np.pi / 360
    W = np.array([[1, -a], [a, 1]])
    traj = np.zeros((n_cond, n_steps, 2))
    x = x0.copy()
    for t in range(n_steps):
        x = x @ W.T
        traj[:, t] = x
    return x0, traj
