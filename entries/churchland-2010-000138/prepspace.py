"""Loading and measures for dandiset 000138 (MC_Maze_Large), for Churchland, Cunningham, Kaufman,
Ryu & Shenoy (2010), Neuron 68:387-400, doi:10.1016/j.neuron.2010.09.015.

The dandiset holds one session of monkey J (Jenkins, 2009-10-06) on the maze task: 500 successful
trials over 27 conditions (9 mazes, `trial_type`, each in 3 versions, `trial_version`), 162 sorted
units from two 96-electrode arrays, and hand position and velocity at 1 kHz. Files are streamed
from the archive at the pinned version; nothing is written to disk.

Where the parameters come from. "Claims file" means the shared methods at the top of
claims/000138/10.1016-j.neuron.2010.09.015.yaml, which cite the paper; "paper" means a passage
taken here (protocol, author, step 1.6); "assumption" and "standard choice" are said as such.

- `MIN_DELAY_MS` = 400: only trials with delays over 400 ms (claims file; Methods, Task design).
- `PROTO_R` = 0.9: maze trials kept when their horizontal and vertical velocity profiles
  correlate with a reference proto-trial at r > 0.9 (claims file; Supplemental Experimental
  Procedures, Task design). The proto-trial is the condition's mean profile (reading a) or its
  elementwise median profile (reading b). The window of the profile is not given; the window of
  the peri-movement T-matrix (`T_WINDOW`) is used (assumption: it is the window the paper
  analyses). Whether horizontal and vertical are each required to pass (`each`) or are
  correlated as one concatenated profile (`concat`) is not said; both are run.
- `SMOOTH_SD_MS` = 20: spike trains smoothed with a 20 ms Gaussian before averaging (claims
  file; Supplemental Experimental Procedures, Computing the mean firing rate versus time). SD
  20 ms is the claims file's standard choice.
- `PREP_WINDOW` = go cue -200 to +100 ms; `PERI_WINDOW` = movement onset -100 to +350 ms
  (claims file; Methods, Correlations between preparatory and peri-movement tuning).
- `T_WINDOW` = movement onset -150 to +800 ms, the maze task's peri-movement T-matrix (claims
  file; Methods, PCA-based spaces). Time step 1 ms (standard choice, as the claims file says).
- `ARRAY_MIN_TUNING` = 5 spikes/s, the array inclusion criterion (claims file; Methods, Neural
  recordings). Tuning is the range (reading a) or the SD (reading b) of the condition means.
- `PERI_RATIO` = 1.5, the extra Figure 4 criterion (claims file; Methods, Correlations).
- Movement onset: the trial table's `move_onset_time` (reading a), or a hand speed threshold
  crossing (reading b), at `ONSET_FRACTION` = 10% of the trial's peak speed, the last crossing
  before the peak (standard choice; the claims file leaves the threshold open).
- Reach end, for task spaces and reading b of the kinematic window: the first time after peak
  speed that speed falls below `END_FRACTION` = 10% of the peak (standard choice), or, as the
  claims file's other reading, a fixed time, here the end of `T_WINDOW` (+800 ms).
- Task spaces follow the Methods, Task spaces, as listed in the claims file. They are measured
  on the condition's mean hand trajectory (standard choice: the paper measures "average
  endpoint and peak velocity for each condition", Results, Testing preparatory tuning).
- Kinematic T-matrix: horizontal and vertical position, velocity and acceleration from 150 ms
  before movement onset, each variable scaled to unity range across times and conditions
  (claims file; Methods, PCA-based spaces). Acceleration is the time derivative of the
  condition-mean velocity (standard choice). Replicating the six variables equally to the number
  of neurons gives the same PC scores up to a scale and so the same PD fits, so they are used
  once.
- PD performance: leave-one-condition-out, 1 - MSE / variance (claims file; Methods, PD
  performance). The space is computed once from all conditions (`fold="once"`, reading a) or
  recomputed without the left-out condition (`fold="refit"`, reading b). Variance is the
  population variance (ddof 0) of the neuron's condition means.
"""

from __future__ import annotations

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter1d
from scipy.stats import rankdata

DANDISET_ID = "000138"
DANDISET_VERSION = "0.220113.0407"
TRAIN_PATH = "sub-Jenkins/sub-Jenkins_ses-large_desc-train_behavior+ecephys.nwb"
TEST_PATH = "sub-Jenkins/sub-Jenkins_ses-large_desc-test_ecephys.nwb"

MIN_DELAY_MS = 400
PROTO_R = 0.9
SMOOTH_SD_MS = 20
PREP_WINDOW = (-200, 100)      # ms from the go cue
PERI_WINDOW = (-100, 350)      # ms from movement onset
T_WINDOW = (-150, 800)         # ms from movement onset
MOVE_TRACE = (-600, 850)       # ms from movement onset, the traces kept per trial
ARRAY_MIN_TUNING = 5.0
PERI_RATIO = 1.5
ONSET_FRACTION = 0.10
END_FRACTION = 0.10

TASK_SPACES = ["initial velocity", "endpoints + max speed", "endpoints + orthogonal excursion",
               "endpoints + viapoint", "endpoints + max velocity", "endpoints + halfpoint",
               "segment directions", "kitchen sink"]


# ----------------------------------------------------------------------------------------------
# Loading

def asset_url(path):
    dandiset = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return dandiset.get_asset_by_path(path).get_content_url(follow_redirects=1, strip_query=True)


def open_h5(path):
    return h5py.File(remfile.File(asset_url(path)), "r")


def _ragged(f, name):
    data, index = f[name][:], f[name + "_index"][:]
    return np.split(data, index[:-1])


def load_train():
    """Trials, units and hand data of the training file, read with h5py from the stream."""
    f = open_h5(TRAIN_PATH)
    tr = f["intervals/trials"]
    trials = pd.DataFrame({k: tr[k][:] for k in [
        "start_time", "stop_time", "trial_type", "trial_version", "maze_id", "success",
        "target_on_time", "go_cue_time", "move_onset_time", "rt", "delay", "num_targets",
        "num_barriers", "active_target"]})
    trials["split"] = [s.decode() for s in tr["split"][:]]
    trials["target_pos"] = _ragged(tr, "target_pos")
    trials["barrier_pos"] = _ragged(tr, "barrier_pos")
    trials["condition"] = list(zip(trials.trial_type, trials.trial_version))
    conds = sorted(trials.condition.unique())
    trials["cond_idx"] = [conds.index(c) for c in trials.condition]
    u = f["units"]
    ids = u["id"][:]
    units = pd.DataFrame({
        "id": ids, "heldout": u["heldout"][:],
        "electrode": [e[0] for e in _ragged(u, "electrodes")],
        "id_array": ids // 1000, "id_channel": (ids % 1000) // 10})
    spikes = _ragged(u, "spike_times")
    el = f["general/extracellular_ephys/electrodes"]
    electrodes = pd.DataFrame({
        "id": el["id"][:], "location": [s.decode() for s in el["location"][:]],
        "group_name": [s.decode() for s in el["group_name"][:]],
        "x": el["x"][:], "y": el["y"][:], "z": el["z"][:]})
    units["electrode_location"] = electrodes.location.values[units.electrode.values]
    beh = f["processing/behavior"]
    hand = {"t": beh["hand_pos/timestamps"][:]}
    for name in ["hand_pos", "hand_vel", "cursor_pos", "eye_pos"]:
        hand[name] = beh[name + "/data"][:]
        hand[name + "_unit"] = beh[name + "/data"].attrs["unit"]
        hand[name + "_conversion"] = beh[name + "/data"].attrs["conversion"]
        hand[name + "_description"] = beh[name].attrs["description"]
    meta = {"session_start": f["session_start_time"][()].decode(),
            "subject": f["general/subject/subject_id"][()].decode(),
            "species": f["general/subject/species"][()].decode(),
            "session_description": f["session_description"][()].decode()}
    return {"trials": trials, "units": units, "spikes": spikes, "hand": hand,
            "electrodes": electrodes, "meta": meta}


def load_test_summary():
    f = open_h5(TEST_PATH)
    tr = f["intervals/trials"]
    u = f["units"]
    return {"trial_columns": list(tr.keys()), "n_trials": len(tr["start_time"][:]),
            "unit_ids": u["id"][:], "spikes": _ragged(u, "spike_times"),
            "starts": tr["start_time"][:], "stops": tr["stop_time"][:]}


# ----------------------------------------------------------------------------------------------
# Movement onset, trial selection

def speed_onset(hand, go_s, fraction=ONSET_FRACTION, search_ms=1200):
    """Movement onset by hand speed: last crossing of `fraction` of peak speed before the peak,
    searched from the go cue to `search_ms` after it."""
    i0 = int(np.searchsorted(hand["t"], go_s - 0.0005))
    i1 = i0 + int(np.searchsorted(np.diff(hand["t"][i0:i0 + search_ms]), 0.0015))
    v = hand["hand_vel"][i0:i1]
    sp = np.hypot(v[:, 0], v[:, 1])
    ipk = int(np.argmax(sp))
    below = np.nonzero(sp[:ipk] < fraction * sp[ipk])[0]
    j = below[-1] + 1 if len(below) else 0
    return hand["t"][i0 + j]


def onset_times(data, reading):
    t = data["trials"]
    if reading == "a":
        return t.move_onset_time.values.copy()
    return np.array([speed_onset(data["hand"], g) for g in t.go_cue_time.values])


def _segment(hand, key, centre_s, window_ms):
    """Samples of hand[key] from window_ms[0] to window_ms[1] ms around centre_s. Hand samples
    exist only within trials, at 1 ms, so the window is found by timestamp; it must lie within
    the trial."""
    i = int(np.searchsorted(hand["t"], centre_s - 0.0005))
    seg = hand[key][i + window_ms[0]: i + window_ms[1]]
    tt = hand["t"][i + window_ms[0]: i + window_ms[1]]
    assert np.allclose(np.diff(tt), 0.001, atol=1e-6), "window crosses a trial boundary"
    return seg


def select_trials(data, onset, proto="a", combine="each"):
    """Trials with delay > 400 ms whose velocity profiles in T_WINDOW correlate with the
    condition's proto-trial at r > 0.9. Returns a boolean mask over all trials and the r values."""
    t = data["trials"]
    keep = (t.delay.values > MIN_DELAY_MS)
    r_all = np.full((len(t), 2), np.nan)
    passed = np.zeros(len(t), bool)
    for cond, idx in t.groupby("condition").indices.items():
        idx = idx[keep[idx]]
        prof = np.stack([_segment(data["hand"], "hand_vel", onset[i], T_WINDOW) for i in idx])   # trials x time x 2
        ref = prof.mean(0) if proto == "a" else np.median(prof, 0)
        for j, i in enumerate(idx):
            if combine == "each":
                r = [np.corrcoef(prof[j, :, d], ref[:, d])[0, 1] for d in (0, 1)]
                r_all[i] = r
                passed[i] = min(r) > PROTO_R
            else:
                r = np.corrcoef(prof[j].T.ravel(), ref.T.ravel())[0, 1]
                r_all[i] = [r, r]
                passed[i] = r > PROTO_R
    return keep & passed, r_all


# ----------------------------------------------------------------------------------------------
# Firing rates

def smoothed_rate(spike_times, n_ms, sd_ms=SMOOTH_SD_MS):
    counts = np.bincount(np.floor(spike_times * 1000).astype(int), minlength=n_ms)[:n_ms]
    return gaussian_filter1d(counts.astype(float), sd_ms) * 1000.0


def trial_rates(data, onsets_by_reading):
    """Per unit and trial: mean rate in the preparatory epoch, and the movement-locked trace
    (MOVE_TRACE) for each movement-onset reading. Also the go-locked trace -200..+500 ms."""
    t = data["trials"]
    n_ms = int(np.ceil(t.stop_time.max() * 1000)) + 2000
    go = np.round(t.go_cue_time.values * 1000).astype(int)
    nu, nt = len(data["spikes"]), len(t)
    prep = np.zeros((nu, nt))
    go_trace = np.zeros((nu, nt, 700), np.float32)
    move = {r: np.zeros((nu, nt, MOVE_TRACE[1] - MOVE_TRACE[0]), np.float32)
            for r in onsets_by_reading}
    go_idx = go[:, None] + np.arange(-200, 500)[None, :]
    mv_idx = {r: np.round(o * 1000).astype(int)[:, None] + np.arange(*MOVE_TRACE)[None, :]
              for r, o in onsets_by_reading.items()}
    for u, st in enumerate(data["spikes"]):
        rate = smoothed_rate(st, n_ms)
        go_trace[u] = rate[go_idx]
        prep[u] = go_trace[u][:, 200 + PREP_WINDOW[0]: 200 + PREP_WINDOW[1]].mean(1)
        for r in move:
            move[r][u] = rate[mv_idx[r]]
    return {"prep": prep, "go_trace": go_trace, "move": move}


def condition_means(values, trials, mask):
    """Average over the selected trials of each condition, along axis 1 (trials)."""
    ci = trials.cond_idx.values
    return np.stack([values[:, (ci == c) & mask].mean(1) for c in range(ci.max() + 1)], 1)


def tuning(prep_means, reading):
    """Tuning strength in spikes/s across conditions: range (a) or SD (b)."""
    if reading == "a":
        return prep_means.max(1) - prep_means.min(1)
    return prep_means.std(1)


def epoch_mean(trace_means, window, origin=MOVE_TRACE[0]):
    return trace_means[..., window[0] - origin: window[1] - origin].mean(-1)


# ----------------------------------------------------------------------------------------------
# Hand kinematics per condition

def hand_condition_means(data, onset, mask, window=(-200, 900)):
    """Condition-mean hand position and velocity, movement-locked, ms from onset in `window`."""
    t = data["trials"]
    pos, vel = [], []
    for c in range(t.cond_idx.max() + 1):
        idx = np.nonzero((t.cond_idx.values == c) & mask)[0]
        pos.append(np.mean([_segment(data["hand"], "hand_pos", onset[i], window) for i in idx], 0))
        vel.append(np.mean([_segment(data["hand"], "hand_vel", onset[i], window) for i in idx], 0))
    return np.stack(pos), np.stack(vel), np.arange(*window)


def reach_end_index(vel, times, fraction=END_FRACTION):
    """Per condition, index of the first sample after peak speed (after onset) below `fraction`
    of the peak."""
    out = []
    for v in vel:
        sp = np.hypot(v[:, 0], v[:, 1])
        sp = np.where(times >= 0, sp, 0)
        ipk = int(np.argmax(sp))
        after = np.nonzero(sp[ipk:] < fraction * sp[ipk])[0]
        out.append(ipk + (after[0] if len(after) else len(sp) - 1 - ipk))
    return np.array(out)


def _split_points(path, n, by):
    """Indices that cut a path (time x 2) into n parts, by path length or by time."""
    if by == "time":
        return [int(round((len(path) - 1) * j / n)) for j in range(n + 1)]
    seg = np.r_[0, np.cumsum(np.hypot(*np.diff(path, axis=0).T))]
    return [min(int(np.searchsorted(seg, seg[-1] * j / n)), len(path) - 1) for j in range(n + 1)]


def task_spaces(pos, vel, times, trials, end="speed", split="length"):
    """The maze task spaces of the Methods, one c x k matrix each."""
    i0 = int(np.nonzero(times == 0)[0][0])
    ends = reach_end_index(vel, times) if end == "speed" else \
        np.full(len(pos), int(np.nonzero(times == T_WINDOW[1] - 1)[0][0]))
    feats = {k: [] for k in TASK_SPACES}
    for c, (p, v, ie) in enumerate(zip(pos, vel, ends)):
        path, pv = p[i0:ie + 1], v[i0:ie + 1]
        start, stop = path[0], path[-1]
        d = stop - start
        perp = (d[0] * (path[:, 1] - start[1]) - d[1] * (path[:, 0] - start[0])) / np.hypot(*d)
        imax = int(np.argmax(np.abs(perp)))
        sp = np.hypot(pv[:, 0], pv[:, 1])
        ipk = int(np.argmax(sp))
        ivx, ivy = int(np.argmax(np.abs(pv[:, 0]))), int(np.argmax(np.abs(pv[:, 1])))
        cuts3 = _split_points(path, 3, split)
        cuts2 = _split_points(path, 2, split)
        segs = np.concatenate([path[cuts3[j + 1]] - path[cuts3[j]] for j in range(3)])
        tri = trials[trials.cond_idx.values == c].iloc[0]
        feats["initial velocity"].append(v[i0:i0 + 150].mean(0))
        feats["endpoints + max speed"].append([*stop, sp[ipk]])
        feats["endpoints + orthogonal excursion"].append([*stop, perp[imax]])
        feats["endpoints + viapoint"].append([*stop, *path[imax]])
        feats["endpoints + max velocity"].append([*stop, pv[ivx, 0], pv[ivy, 1]])
        feats["endpoints + halfpoint"].append([*stop, *path[cuts2[1]]])
        feats["segment directions"].append(segs)
        feats["kitchen sink"].append([*segs, perp[imax], *path[imax],
                                      float(tri.num_barriers > 0), float(tri.num_targets > 1)])
    return {k: np.asarray(v, float) for k, v in feats.items()}, ends


def kinematic_matrix(pos, vel, times, end_ms):
    """c x 6t kinematic T-matrix from -150 ms to end_ms, each variable scaled to unity range."""
    sel = (times >= T_WINDOW[0]) & (times < end_ms)
    acc = np.gradient(vel, axis=1) * 1000.0
    blocks = []
    for arr in (pos, vel, acc):
        for d in (0, 1):
            x = arr[:, sel, d]
            blocks.append(x / (x.max() - x.min()))
    return np.concatenate(blocks, 1)


# ----------------------------------------------------------------------------------------------
# PD performance

def _scores_from_gram(Gc, kmax):
    """Leading kmax PC scores (c x kmax) from a centred Gram matrix."""
    w, V = np.linalg.eigh(Gc)
    order = np.argsort(w)[::-1][:kmax]
    w, V = np.clip(w[order], 1e-12, None), V[:, order]
    return V * np.sqrt(w), V, w


def centre_gram(G):
    c = len(G)
    H = np.eye(c) - 1.0 / c
    return H @ G @ H


def loo_errors_fixed(S, X):
    """Leave-one-condition-out prediction errors of OLS with offset, for a fixed c x k space S
    and responses X (n x c). Uses the exact leave-one-out identity e_i / (1 - h_ii)."""
    c = S.shape[0]
    D = np.column_stack([np.ones(c), S])
    H = D @ np.linalg.pinv(D)
    resid = X - X @ H.T
    return resid / (1.0 - np.diag(H))[None, :]


def loo_errors_refit_gram(G, x, kmax):
    """Leave-one-condition-out errors when the PCA space is recomputed without the left-out
    condition. G is the uncentred c x c Gram matrix of the T-matrix rows; x the c responses.
    Returns kmax x c errors."""
    c = len(x)
    err = np.zeros((kmax, c))
    for i in range(c):
        tr = np.r_[0:i, i + 1:c]
        B = G[np.ix_(tr, tr)]
        A = G[i, tr]
        Gc = centre_gram(B)
        scores, V, w = _scores_from_gram(Gc, kmax)
        cross = A - A.mean() - B.mean(0) + B.mean()
        test = cross @ V / np.sqrt(w)
        for k in range(1, kmax + 1):
            D = np.column_stack([np.ones(c - 1), scores[:, :k]])
            beta = np.linalg.lstsq(D, x[tr], rcond=None)[0]
            err[k - 1, i] = x[i] - (beta[0] + test[:k] @ beta[1:])
    return err


def performance(err, X, pooled=False):
    """1 - MSE / variance per neuron (reading a), or pooled over neurons (reading b).
    err and X are n x c."""
    var = X.var(1)
    if pooled:
        return 1.0 - (err ** 2).sum() / (X.shape[1] * var.sum())
    return 1.0 - (err ** 2).mean(1) / var


def neuron_grams(M):
    """Per-neuron c x c Gram contributions of a neuron x condition x time array."""
    return np.einsum("nct,ndt->ncd", M, M, optimize=True)


def loo_pca_space(G_total, G_parts, X, kmax, fold):
    """Errors (n x kmax x c) for each neuron's responses X[n] in the PCA space of the T-matrix
    with that neuron's part removed (G_total - G_parts[n]). G_parts may be None (space shared by
    all neurons, as for the kinematic space)."""
    n, c = X.shape
    err = np.zeros((n, kmax, c))
    for j in range(n):
        G = G_total if G_parts is None else G_total - G_parts[j]
        if fold == "once":
            S = _scores_from_gram(centre_gram(G), kmax)[0]
            for k in range(1, kmax + 1):
                err[j, k - 1] = loo_errors_fixed(S[:, :k], X[j:j + 1])[0]
        else:
            err[j] = loo_errors_refit_gram(G, X[j], kmax)
    return err


def pd_fit(S, x):
    """PD fit with offset; returns the unit-length PD (or None if b is zero)."""
    D = np.column_stack([np.ones(len(x)), S])
    b = np.linalg.lstsq(D, x, rcond=None)[0][1:]
    nb = np.linalg.norm(b)
    return b / nb if nb > 0 else None


def corr_pearson_spearman(a, b):
    """Row-wise Pearson and Spearman correlations between two n x c arrays."""
    def rowcorr(x, y):
        x = x - x.mean(1, keepdims=True)
        y = y - y.mean(1, keepdims=True)
        return (x * y).sum(1) / np.sqrt((x ** 2).sum(1) * (y ** 2).sum(1))
    ra, rb = rankdata(a, axis=1), rankdata(b, axis=1)
    return rowcorr(a, b), rowcorr(ra, rb)


# ----------------------------------------------------------------------------------------------
# Figure 8 oscillator

def oscillator(rng, n_cond=25, hold=100, release=360, init="uniform"):
    """Unit activities (cond x time x 2) for x(t+1) = W x(t), W = [1 -a; a 1], a = 2 pi / 360,
    held at the initial state for `hold` steps, then released for `release` steps."""
    a = 2 * np.pi / 360
    W = np.array([[1, -a], [a, 1]])
    x0 = rng.uniform(-1, 1, (n_cond, 2)) if init == "uniform" else rng.standard_normal((n_cond, 2))
    out = np.zeros((n_cond, hold + release, 2))
    out[:, :hold] = x0[:, None, :]
    x = x0.copy()
    for s in range(release):
        x = x @ W.T
        out[:, hold + s] = x
    return out, x0


# ----------------------------------------------------------------------------------------------
# Readings and the grid of PD performance

READINGS = {
    "proto": ["a", "b"],          # proto-trial: mean (a) or elementwise median (b) profile
    "combine": ["concat", "each"],  # r > 0.9 for the concatenated profile, or for each axis
    "onset": ["a", "b"],          # movement onset: trial table (a) or speed threshold (b)
    "tuning": ["a", "b"],         # tuning: range (a) or SD (b) of condition means
    "t_units": ["all", "included"],  # neurons entering the peri-movement T-matrix
    "fold": ["once", "refit"],    # PCA space computed once, or recomputed per left-out condition
    "norm": ["neuron", "pooled"],  # performance per neuron then mean (a), or pooled ratio (b)
    "kin_end": ["fixed", "speed"],  # kinematic window ends at +800 ms (a) or at the reach end (b)
    "task_end": ["speed", "fixed"],  # reach end for task spaces: speed threshold or +800 ms
    "split": ["length", "time"],  # halfpoint and segments by path length or by time
    "kmax": [14, 12],             # range of dimensionalities
}
MAIN = {k: v[0] for k, v in READINGS.items()}


def prepare(data, R, onsets, proto, combine, onset):
    """Condition means under one trial-selection reading."""
    t = data["trials"]
    mask, r = select_trials(data, onsets[onset], proto, combine)
    pos, vel, times = hand_condition_means(data, onsets[onset], mask)
    return {"mask": mask, "r": r, "prep": condition_means(R["prep"], t, mask),
            "move": condition_means(R["move"][onset], t, mask), "pos": pos, "vel": vel,
            "times": times, "trials": t}


def t_matrix(move, start=T_WINDOW[0], stop=T_WINDOW[1]):
    return move[:, :, start - MOVE_TRACE[0]: stop - MOVE_TRACE[0]].astype(float)


def peri_errors(ctx, inc, t_units, fold, kmax=14, start=T_WINDOW[0], move=None):
    """Errors (n_inc x kmax x c) of the PD in the peri-movement space built from every neuron in
    the T-matrix except the one being fit (Methods, PCA-based spaces)."""
    move = ctx["move"] if move is None else move
    Gp = neuron_grams(t_matrix(move, start))
    in_t = np.ones(len(inc), bool) if t_units == "all" else inc
    G = Gp[in_t].sum(0)
    parts = Gp[inc] * in_t[inc][:, None, None]
    return loo_pca_space(G, parts, ctx["prep"][inc], kmax, fold)


def kinematic_end_ms(ctx, kin_end):
    if kin_end == "fixed":
        return T_WINDOW[1]
    return int(ctx["times"][reach_end_index(ctx["vel"], ctx["times"])].max()) + 1


def kinematic_errors(ctx, inc, fold, kin_end, kmax=14):
    KT = kinematic_matrix(ctx["pos"], ctx["vel"], ctx["times"], kinematic_end_ms(ctx, kin_end))
    return loo_pca_space(KT @ KT.T, None, ctx["prep"][inc], kmax, fold)


def task_errors(ctx, inc, task_end, split):
    spaces, _ = task_spaces(ctx["pos"], ctx["vel"], ctx["times"], ctx["trials"], task_end, split)
    X = ctx["prep"][inc]
    return {name: loo_errors_fixed(S, X) for name, S in spaces.items()}, \
        {name: S.shape[1] for name, S in spaces.items()}


def perf_both(err, X):
    return {"neuron": float(np.mean(performance(err, X))),
            "pooled": float(performance(err, X, pooled=True))}
