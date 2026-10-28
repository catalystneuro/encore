"""Loading and measures for dandiset 000139 (MC_Maze_Medium), used to test
Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400.

Where each parameter comes from:

- Version: the only published version of the dandiset (``VERSION``).
- Trials kept: delays above 400 ms (claims file, opening comment, from Methods,
  Task design and behavior). Trials whose horizontal and vertical velocity
  profiles correlate with a reference proto-trial at r > 0.9 (Supplemental
  Experimental Procedures, Task design and behavioral control). The
  proto-trial and how the two profiles are combined are open; the claims file
  names the readings, implemented in ``proto_keep``. The window over which the
  profiles are correlated is not given; 150 ms before to 800 ms after movement
  onset (the maze-task peri-movement window of Methods, PCA-based spaces) is
  used, an assumption.
- Movement onset: reading (a) the dataset's ``move_onset_time``; reading (b)
  the first time after the go cue at which hand speed exceeds 10% of the
  trial's peak speed (the threshold is a standard choice; the paper does not
  give one).
- Rates: spike trains smoothed with a Gaussian of 20 ms standard deviation
  (Supplemental Experimental Procedures, Computing the mean firing rate),
  computed on a 1 ms grid; the T-matrices sample them every 10 ms (a standard
  choice that cannot change an outcome).
- Preparatory rate: mean from 200 ms before to 100 ms after the go cue;
  peri-movement rate: mean from 100 ms before to 350 ms after movement onset
  (Methods, Correlations between preparatory and peri-movement tuning).
- Tuning strength: readings (a) range across conditions, (b) standard
  deviation across conditions (claims file, opening comment). Array threshold
  5 spikes/s of preparatory tuning (Methods, Neural recordings and datasets);
  peri-movement tuning at least 1.5 times preparatory tuning (Methods,
  Correlations).
- PD model and leave-one-condition-out performance: Methods, Using a PD and
  PD performance. Whether a PCA-based S is recomputed in each fold is open;
  both readings are implemented (``recompute``).
- Peri-movement T-matrix: 150 ms before to 800 ms after movement onset, all
  units except the one being fitted, not normalized (Methods, PCA-based
  spaces). Kinematic T-matrix: hand position, velocity and acceleration from
  150 ms before onset, each signal scaled to unit range (same passage).
- Reach end, used for endpoints and the trajectory-based task spaces: the
  first time after peak speed at which the condition-mean speed falls below
  10% of its peak (a standard choice; the paper does not define it).
"""

import numpy as np
import pandas as pd
import requests
import h5py
import remfile
import pynwb
from scipy.ndimage import gaussian_filter1d

DANDISET = "000139"
VERSION = "0.220113.0408"
TRAIN_PATH = "sub-Jenkins/sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb"
TEST_PATH = "sub-Jenkins/sub-Jenkins_ses-medium_desc-test_ecephys.nwb"
API = "https://api.dandiarchive.org/api"

# Windows in ms, relative to the event (go cue or movement onset).
GO_WIN = (-600, 500)      # stored go-locked bins
MOVE_WIN = (-600, 1000)   # stored move-locked bins
PREP = (-200, 100)        # relative to go cue
PERI = (-100, 350)        # relative to movement onset
TMAT = (-150, 800)        # peri-movement T-matrix, maze task
SIGMA_MS = 20
STEP_MS = 10


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return out


def asset_url(path):
    a = [x for x in list_assets() if x["path"] == path][0]
    meta = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{a['asset_id']}/",
                        timeout=60).json()
    return [u for u in meta["contentUrl"] if "s3" in u][0]


def open_nwb(path):
    f = h5py.File(remfile.File(asset_url(path)), "r")
    io = pynwb.NWBHDF5IO(file=f, load_namespaces=True)
    return io.read(), f


def load(path=TRAIN_PATH):
    """Trials, units (with the array read from the unit id) and hand kinematics."""
    nwb, f = open_nwb(path)
    trials = nwb.trials.to_dataframe()
    g = f["units"]
    ids = g["id"][:]
    st_idx = g["spike_times_index"][:]
    st_all = g["spike_times"][:]
    spikes = np.split(st_all, st_idx[:-1])
    el_rows = g["electrodes"][:]
    eg = f["general/extracellular_ephys/electrodes"]
    el_group = np.array([x.decode() for x in eg["group_name"][:]])
    units = pd.DataFrame({
        "id": ids,
        "heldout": g["heldout"][:].astype(bool),
        "electrode_row": el_rows,
        "electrode_group_in_file": el_group[el_rows],
        # The unit id is array * 1000 + channel * 10 + sort (checked in the notebook).
        "id_array": ids // 1000,
        "id_channel": (ids % 1000) // 10,
    })
    out = dict(nwb=nwb, file=f, trials=trials, units=units, spikes=spikes,
               electrodes=pd.DataFrame({k: eg[k][:] for k in ["x", "y", "z", "imp"]} |
                                       {"group_name": el_group}))
    if "behavior" in nwb.processing:
        b = f["processing/behavior"]
        out["t_beh"] = b["hand_pos/timestamps"][:]
        out["hand_pos"] = b["hand_pos/data"][:]   # mm (description), conversion 0.001 to m
        out["hand_vel"] = b["hand_vel/data"][:]   # mm/s
    return out


def bin_spikes(spikes, events, win):
    """1 ms spike counts, (trials, units, bins), for windows [win) around events (s)."""
    nb = win[1] - win[0]
    out = np.zeros((len(events), len(spikes), nb), dtype=np.uint8)
    for u, s in enumerate(spikes):
        for i, e in enumerate(events):
            t0 = e + win[0] / 1000.0
            lo, hi = np.searchsorted(s, [t0, t0 + nb / 1000.0])
            if hi > lo:
                b = np.floor((s[lo:hi] - t0) * 1000.0).astype(int)
                b = b[(b >= 0) & (b < nb)]
                np.add.at(out[i, u], b, 1)
    return out


def kin_traces(t, x, events, win):
    """Behaviour samples at 1 ms around events, (trials, bins, 2), nearest sample."""
    nb = win[1] - win[0]
    rel = np.arange(win[0], win[1]) / 1000.0
    out = np.empty((len(events), nb, x.shape[1]))
    for i, e in enumerate(events):
        idx = np.searchsorted(t, e + rel)
        idx = np.clip(idx, 1, len(t) - 1)
        left = np.where(np.abs(t[idx - 1] - (e + rel)) < np.abs(t[idx] - (e + rel)), idx - 1, idx)
        out[i] = x[left]
    return out


def onset_from_speed(t, vel, go_times, frac=0.10, search=(0.0, 1.0)):
    """Movement onset reading (b): first time after the go cue at which hand speed
    exceeds `frac` of the trial's peak speed in the search window (s after go)."""
    on = np.empty(len(go_times))
    for i, g in enumerate(go_times):
        lo, hi = np.searchsorted(t, [g + search[0], g + search[1]])
        sp = np.hypot(vel[lo:hi, 0], vel[lo:hi, 1])
        j = np.argmax(sp > frac * sp.max())
        on[i] = t[lo + j]
    return on


def smooth_rate(counts_mean, sigma_ms=SIGMA_MS):
    """Condition-mean 1 ms counts -> rate in spikes/s, smoothed along the last axis."""
    return gaussian_filter1d(counts_mean.astype(float) * 1000.0, sigma_ms, axis=-1, mode="nearest")


def cond_mean(arr, cond_codes, conds):
    """Mean over trials of each condition: arr (trials, ...) -> (conds, ...)."""
    return np.stack([arr[cond_codes == c].mean(0) for c in conds])


def window_mean(rate, win, ref):
    """Mean of rate (..., bins) over [win) ms, where bin 0 is at `ref` ms."""
    return rate[..., win[0] - ref: win[1] - ref].mean(-1)


def tuning_strength(x, how):
    """x (conds, units). Reading (a) 'range' or (b) 'sd' across conditions."""
    if how == "range":
        return x.max(0) - x.min(0)
    return x.std(0, ddof=0)


def proto_keep(vel, cond_codes, proto="mean", combine="separate", r_min=0.9):
    """Proto-trial selection. vel (trials, bins, 2) velocity profiles.
    proto: 'mean' (condition-mean profile) or 'medoid' (the condition's trial with the
    highest mean correlation to the others). combine: 'separate' (x and y each r > r_min)
    or 'concat' (the two profiles concatenated, r > r_min)."""
    keep = np.zeros(len(vel), dtype=bool)
    for c in np.unique(cond_codes):
        idx = np.where(cond_codes == c)[0]
        v = vel[idx]
        if proto == "mean":
            p = v.mean(0)
        else:
            cat = v.transpose(0, 2, 1).reshape(len(idx), -1)
            cc = np.corrcoef(cat)
            p = v[np.argmax((cc.sum(1) - 1) / max(len(idx) - 1, 1))]
        for j, i in enumerate(idx):
            if combine == "separate":
                rx = np.corrcoef(v[j, :, 0], p[:, 0])[0, 1]
                ry = np.corrcoef(v[j, :, 1], p[:, 1])[0, 1]
                keep[i] = (rx > r_min) and (ry > r_min)
            else:
                r = np.corrcoef(v[j].T.ravel(), p.T.ravel())[0, 1]
                keep[i] = r > r_min
    return keep


# ---------------------------------------------------------------- PD model

def _centered_parts(G, train, l):
    """From an uncentered Gram matrix G (c x c), the centered Gram of the training rows
    and the centered cross products of row l with them (training mean removed)."""
    Gtt = G[np.ix_(train, train)]
    rm = Gtt.mean(1)
    gm = Gtt.mean()
    Gc = Gtt - rm[:, None] - rm[None, :] + gm
    gl = G[l, train]
    cross = gl - gl.mean() - rm + gm
    return Gc, cross


def pca_scores(G, kmax):
    """PCA scores of all rows from the uncentered Gram matrix (c x c)."""
    c = G.shape[0]
    H = np.eye(c) - 1.0 / c
    Gc = H @ G @ H
    w, U = np.linalg.eigh(Gc)
    o = np.argsort(w)[::-1][:kmax]
    w, U = np.clip(w[o], 1e-12, None), U[:, o]
    return U * np.sqrt(w)


def explained(G):
    c = G.shape[0]
    H = np.eye(c) - 1.0 / c
    w = np.sort(np.linalg.eigvalsh(H @ G @ H))[::-1]
    w = np.clip(w, 0, None)
    return w / w.sum()


def _fit_predict(S_train, x_train, s_l):
    A = np.column_stack([np.ones(len(S_train)), S_train])
    coef, *_ = np.linalg.lstsq(A, x_train, rcond=None)
    return coef[0] + s_l @ coef[1:]


def pd_performance_pca(x, G, ks, recompute):
    """Leave-one-condition-out PD performance for one neuron in a PCA-based space.
    x (c,) preparatory rates; G (c x c) uncentered Gram matrix of the T-matrix (without
    the neuron). recompute: False = S from all conditions, only the regression leaves the
    condition out (reading a); True = PCA redone on the remaining conditions and the
    left-out condition projected onto its components (reading b). Returns perf per k."""
    c = len(x)
    kmax = max(ks)
    pred = np.zeros((len(ks), c))
    if not recompute:
        S = pca_scores(G, kmax)
    for l in range(c):
        train = np.delete(np.arange(c), l)
        if recompute:
            Gc, cross = _centered_parts(G, train, l)
            w, U = np.linalg.eigh(Gc)
            o = np.argsort(w)[::-1][:kmax]
            w, U = np.clip(w[o], 1e-12, None), U[:, o]
            S_train = U * np.sqrt(w)
            s_l = (cross @ U) / np.sqrt(w)
        else:
            S_train, s_l = S[train], S[l]
        for i, k in enumerate(ks):
            pred[i, l] = _fit_predict(S_train[:, :k], x[train], s_l[:k])
    v = x.var()
    return 1.0 - ((pred - x[None, :]) ** 2).mean(1) / v


def pd_performance_fixed(x, S):
    """Leave-one-condition-out PD performance in a fixed (task) space S (c x k)."""
    c = len(x)
    pred = np.array([_fit_predict(np.delete(S, l, 0), np.delete(x, l), S[l]) for l in range(c)])
    return 1.0 - ((pred - x) ** 2).mean() / x.var()


def pd_unit(x, S):
    A = np.column_stack([np.ones(len(S)), S])
    coef, *_ = np.linalg.lstsq(A, x, rcond=None)
    b = coef[1:]
    return b / np.linalg.norm(b)


def pd_consistency(x, S, rng, n_draws=100, n_cond=25):
    """Results, Stability of the PD: 25 conditions drawn with replacement, PD fitted,
    another 25 drawn, PD refitted; consistency is the dot product of the two unit PDs."""
    c = len(x)
    d = np.empty(n_draws)
    for i in range(n_draws):
        a = rng.integers(0, c, n_cond)
        b = rng.integers(0, c, n_cond)
        d[i] = pd_unit(x[a], S[a]) @ pd_unit(x[b], S[b])
    return d.mean()


# ---------------------------------------------------------------- task spaces

def condition_kinematics(pos, vel, rel0):
    """Per-condition kinematic features from condition-mean traces.
    pos, vel: (conds, bins, 2), bin 0 at rel0 ms from movement onset."""
    out = []
    for p, v in zip(pos, vel):
        sp = np.hypot(v[:, 0], v[:, 1])
        on = -rel0
        ipk = on + np.argmax(sp[on:])
        after = np.where(sp[ipk:] < 0.1 * sp[ipk])[0]
        iend = ipk + (after[0] if len(after) else len(sp) - 1 - ipk)
        traj = p[on:iend + 1]
        start, end = traj[0], traj[-1]
        d = end - start
        L = np.linalg.norm(d)
        rel = traj - start
        signed = (d[0] * rel[:, 1] - d[1] * rel[:, 0]) / L   # left of the reach is positive
        imax = np.argmax(np.abs(signed))
        seg = np.linalg.norm(np.diff(traj, axis=0), axis=1)
        cum = np.concatenate([[0], np.cumsum(seg)])
        half = traj[np.searchsorted(cum, cum[-1] / 2)]
        n = len(traj) - 1
        pts_t = traj[[0, n // 3, 2 * n // 3, n]]
        pts_l = traj[[0, np.searchsorted(cum, cum[-1] / 3), np.searchsorted(cum, 2 * cum[-1] / 3), n]]
        vpk = v[ipk]
        out.append(dict(
            end_x=end[0], end_y=end[1], peak_speed=sp[ipk],
            vx_peak_speed=vpk[0], vy_peak_speed=vpk[1],
            vx_extreme=v[on:iend + 1, 0][np.argmax(np.abs(v[on:iend + 1, 0]))],
            vy_extreme=v[on:iend + 1, 1][np.argmax(np.abs(v[on:iend + 1, 1]))],
            init_vx=v[on:on + 150, 0].mean(), init_vy=v[on:on + 150, 1].mean(),
            excursion=signed[imax], exc_x=traj[imax, 0], exc_y=traj[imax, 1],
            half_x=half[0], half_y=half[1],
            **{f"segt{i}{a}": (pts_t[i + 1] - pts_t[i])[j] for i in range(3) for j, a in enumerate("xy")},
            **{f"segl{i}{a}": (pts_l[i + 1] - pts_l[i])[j] for i in range(3) for j, a in enumerate("xy")},
            reach_end_ms=iend - on,
        ))
    return pd.DataFrame(out)


def task_spaces(k, barriers, distractors):
    """The maze-task spaces of Methods, Task spaces. Variants for the open details:
    segments equal in time (t) or in path length (l); peak velocity read as the velocity
    at peak speed (pk) or each component's extreme (ex)."""
    sp = {}
    sp["endpoints + max speed"] = k[["end_x", "end_y", "peak_speed"]].values
    sp["initial velocity"] = k[["init_vx", "init_vy"]].values
    sp["endpoints + orth. excursion"] = k[["end_x", "end_y", "excursion"]].values
    sp["endpoints + viapoint"] = k[["end_x", "end_y", "exc_x", "exc_y"]].values
    sp["endpoints + max velocity (pk)"] = k[["end_x", "end_y", "vx_peak_speed", "vy_peak_speed"]].values
    sp["endpoints + max velocity (ex)"] = k[["end_x", "end_y", "vx_extreme", "vy_extreme"]].values
    sp["endpoints + halfpoint"] = k[["end_x", "end_y", "half_x", "half_y"]].values
    for s in "tl":
        segs = k[[f"seg{s}{i}{a}" for i in range(3) for a in "xy"]].values
        sp[f"segment dirs ({s})"] = segs
        sp[f"kitchen sink ({s})"] = np.column_stack(
            [segs, k[["excursion", "exc_x", "exc_y"]].values, barriers, distractors])
    return sp


# ---------------------------------------------------------------- spaces from the data

def grams_per_unit(rate, rel0, win=TMAT, step=STEP_MS):
    """Per-unit Gram matrices of the peri-movement T-matrix.
    rate (conds, units, bins) smoothed condition means, bin 0 at rel0 ms.
    Returns (units, conds, conds); the T-matrix without unit n has Gram G.sum(0) - G[n]."""
    T = rate[:, :, win[0] - rel0: win[1] - rel0: step]
    return np.einsum("aut,but->uab", T, T)


def kinematic_gram(pos, vel, rel0, n_blocks, end_ms=TMAT[1], start_ms=TMAT[0], replicate=True):
    """Gram matrix of the kinematic T-matrix (Methods, PCA-based spaces).
    pos, vel: condition means (conds, bins, 2), bin 0 at rel0 ms. Acceleration is the time
    derivative of velocity after the 20 ms Gaussian (a standard choice). Each of the six
    signals is scaled to unit range across times and conditions. replicate: reading (a)
    the six signals repeated in turn to `n_blocks` blocks; reading (b) the six once."""
    v_s = gaussian_filter1d(vel, SIGMA_MS, axis=1, mode="nearest")
    acc = np.gradient(v_s, axis=1) * 1000.0
    sl = slice(start_ms - rel0, end_ms - rel0, STEP_MS)
    sigs = [pos[:, sl, 0], pos[:, sl, 1], vel[:, sl, 0], vel[:, sl, 1], acc[:, sl, 0], acc[:, sl, 1]]
    sigs = [s / (s.max() - s.min()) for s in sigs]
    if replicate:
        counts = [n_blocks // 6 + (1 if i < n_blocks % 6 else 0) for i in range(6)]
    else:
        counts = [1] * 6
    return sum(c * (s @ s.T) for c, s in zip(counts, sigs))


def perf_curves_pca(X, G_total, G_units, fit_idx, ks, recompute):
    """PD performance (neurons x ks) for the neurons in fit_idx. X (conds, units) preparatory
    rates. If G_units is None, the space is the same for every neuron (G_total)."""
    out = np.empty((len(fit_idx), len(ks)))
    for j, n in enumerate(fit_idx):
        G = G_total if G_units is None else G_total - G_units[n]
        out[j] = pd_performance_pca(X[:, n], G, ks, recompute)
    return out


def prep_grams(X):
    """Per-unit Gram matrices of the c x n preparatory matrix (upper limit, Supplemental
    Experimental Procedures, Estimating the upper limit of PD performance)."""
    return np.einsum("au,bu->uab", X, X)
