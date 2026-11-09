"""Loading, commands, conditions and shared measures for dandiset 000404 (Monkey 2D cursor BMI).

Athalye, Khanna, Gowda, Orsborn, Costa & Carmena (2023), Current Biology 33, 2962-2976,
doi:10.1016/j.cub.2023.06.027. The claims file is claims/000404/10.1016-j.cub.2023.06.027.yaml;
"shared method" below means its header section of that name. "Code" means the paper's repository
https://github.com/pkhanna104/bmi_dynamics_code at commit CODE_COMMIT.

Each NWB file holds one session: per task frame (60 Hz for Monkey G, 200 Hz for Monkey J) the
spike counts of the decoder's units, the decoder state (position, velocity, offset), the cursor,
target and obstacle series, the task entry number, a flag for frames where the decoder updated,
and a trials table from the go cue to the reward. Files are streamed at the pinned version; nothing
is written to disk.

Where the parameters come from:

- Bins (shared method, citing prelim_analysis.bin_spks and ppf_pa._bin_spike_counts). Monkey G:
  one bin per decoder update frame i with go + 5 <= i <= reward, holding the counts of frames
  i-5 to i. Monkey J: 100 ms bins of 20 frames from the go frame, the last bin running past the
  reward to complete 20 frames.
- The decoder. The files hold no decoder matrices (the code that wrote them comments them out,
  nwb_utils.py 290-303). The paper defines the command as the velocity rows of the steady-state
  Kalman gain applied to the binned counts (Methods, "Command definition -- Monkey G"), and for
  Monkey J as a time-invariant matrix that approximates the PPF update (Methods, "Command
  definition -- Monkey J"). Both are estimated here by least squares from the files: the velocity
  after each update regressed on the state before it (position, velocity, offset) and the counts
  of the update. When the fit is exact (variance accounted for near 1) the count coefficients are
  the gain; `fit_decoder` reports the fit. This estimation is an assumption forced by the
  missing matrices; for Monkey J it is the paper's own construction.
- Monkey J commands are summed over the 20 frames of a bin (Methods, "Command definition --
  Monkey J") and multiplied by 100 (m to cm, as ppf_pa._bin_neural_push does).
- Conditions (Methods, "Neuroprosthetic tasks"; shared method). Task from the obstacle series;
  target from the cursor position at reward (the cursor must be inside the target then), as the
  target series of the files do not give it (see the notebook). Clockwise or counterclockwise by
  the code's rule (util_fcns.CW_CCW_obs). For Monkey J obstacle trials the start and end targets
  are matched to the code's target list (resim_ppf/jeev_obs_positions_from_amy.mat and
  file_key.trialList) to recover the code's trial type; types 0 and 1 are dropped
  (analysis_config.min_targix, Methods "only trials that included partial or full obstruction"),
  and the code's fixed cw/ccw labels are used for types 3, 4, 5, 8, 9
  (analysis_config.jeev_cw_ccw_dict) with the rule for the others.
- Command bins (Methods, "Discretizing commands"; util_fcns.commands2bins): 8 angle bins centred
  on multiples of 45 degrees and 4 magnitude bins with edges at the 23.75, 47.5, 71.25 and 95th
  percentiles of the session's command magnitudes; bin 4 (above the 95th) is not analysed.
- Distribution matching (shared method; plot_fr_diffs.distribution_match_global_mov).
- Ridge grid (shared method; generate_models.py 56-65).
"""

from __future__ import annotations

import io
import math
import urllib.request

import h5py
import numpy as np
import remfile
import scipy.io as sio
import scipy.linalg
import scipy.stats
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000404"
DANDISET_VERSION = "0.230605.2024"
CODE_COMMIT = "416187366f84f2b7367ac54205aa321480e1acd1"
CODE_RAW = f"https://raw.githubusercontent.com/pkhanna104/bmi_dynamics_code/{CODE_COMMIT}/"

MIN_OBS = 15                      # Methods: a command used at least 15 times in a condition
MAG_PERCENTILES = [23.75, 47.5, 71.25, 95.0]
J_CENTER = np.array([0.0377292, 0.1383867])   # resim_ppf/file_key.centerPos (m)
J_CW_FIXED = {1: 1, 2: 1, 3: 0, 4: 0, 5: 1, 8: 0, 9: 1}  # analysis_config.jeev_cw_ccw_dict (1 = ccw)
J_TRIAL_LIST = np.array([[5, 2, 11], [11, 2, 5], [3, 13, 11], [11, 13, 3], [5, 16, 9],
                         [9, 16, 5], [3, 21, 9], [9, 21, 3], [23, 20, 24], [24, 20, 23]])  # file_key.trialList - 63
RIDGE_GRID = np.unique(np.hstack([np.array([0.25, 0.5, 0.75, 1.0])[:, None] * 10.0 ** np.array(
    [i for i in range(-4, 7) if i != 4])[None, :]]).ravel().tolist() + list(range(2000, 10001, 1000)))


def session_list():
    """(monkey, session number, asset path) for every NWB file of the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        out = []
        for a in ds.get_assets():
            m = "G" if "monk-g" in a.path else "J"
            s = int(a.path.split("session")[-1].split(".")[0])
            out.append((m, s, a.path, a.identifier, a.size))
    return sorted(out)


def _s3_url(path):
    with DandiAPIClient() as client:
        return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_asset_by_path(path).get_content_url(
            follow_redirects=1, strip_query=True)


def load_raw(path):
    """Every series of the behavior module, the trials table and the file metadata."""
    f = h5py.File(remfile.File(_s3_url(path)), "r")
    b = f["processing/behavior"]
    d = {k: b[k]["data"][()] for k in b}
    d["meta"] = {k: b[k]["data"].attrs["unit"] for k in b}
    d["descr"] = {k: b[k].attrs["description"] for k in b}
    d["rate"] = float(b["cursor/starting_time"].attrs["rate"])
    d["start"] = f["intervals/trials/start_time"][()]
    d["stop"] = f["intervals/trials/stop_time"][()]
    d["session_id"] = f["general/session_id"][()].decode()
    d["subject"] = f["general/subject/subject_id"][()].decode()
    d["identifier"] = f["identifier"][()].decode()
    d["experiment_description"] = f["general/experiment_description"][()].decode()
    d["te_num"] = np.array([x.decode() if isinstance(x, bytes) else str(int(x)) for x in d["te_num"]])
    if d["obs_details"].dtype == object:
        d["obs_details"] = np.array([x.decode() for x in d["obs_details"]])
    f.close()
    return d


def fit_decoder(d, monkey):
    """Least-squares decoder: velocity after an update on [state before, counts of the update].

    Returns K (2 x N, counts to velocity), F (2 x 5, state before to velocity), and the variance
    accounted for of the velocity (`vaf_velocity`) and of the neural update alone
    (`vaf_command`: velocity minus F times the state before, explained by K times the counts).
    Fit on all frames of the session, separately for each task entry as a check.
    """
    S = d["decoder_state"]
    Y = d["spike_counts"].astype(float)
    if monkey == "G":
        up = np.where(d["update_bmi"] == 1)[0]
        up = up[up >= 6]
        cs = np.vstack([np.zeros((1, Y.shape[1])), np.cumsum(Y, 0)])
        ybin = cs[up + 1] - cs[up - 5]
        prev = S[up - 1]
        tgt = S[up][:, 2:4]
        te = d["te_num"][up]
    else:
        up = np.arange(1, len(S))
        ybin = Y[up]
        prev = S[up - 1]
        tgt = S[up][:, 2:4]
        te = d["te_num"][up]
    X = np.hstack([prev, ybin])
    keep = np.ones(len(up), bool)
    beta, *_ = np.linalg.lstsq(X, tgt, rcond=None)
    if monkey == "G":
        # The Kalman filter is linear in steady state, so the exact gain fits most updates to
        # rounding; updates where the filter had not converged (the first of each block) or did
        # not follow it are left out by refitting on the updates the fit explains (trimmed least
        # squares). Monkey J's PPF is not linear, so its matrix is the plain least-squares fit.
        for _ in range(5):
            r = np.abs(tgt - X @ beta).max(1)
            keep = r < max(1e-3 * np.abs(tgt).max(), 20 * np.median(r))
            beta, *_ = np.linalg.lstsq(X[keep], tgt[keep], rcond=None)
    F, K = beta[:5].T, beta[5:].T
    res = tgt - X @ beta
    upd = tgt - prev @ beta[:5]
    vaf_vel = 1 - (res ** 2).sum() / ((tgt - tgt.mean(0)) ** 2).sum()
    vaf_cmd = 1 - (res ** 2).sum() / ((upd - upd.mean(0)) ** 2).sum()
    vaf_cmd_kept = 1 - (res[keep] ** 2).sum() / ((upd[keep] - upd[keep].mean(0)) ** 2).sum()
    # per task entry: the variance of the update the session's matrix accounts for, and for Monkey G
    # the fraction of the entry's updates it fits to rounding (one decoder for both tasks)
    per_te = {}
    tol = 1e-3 * np.abs(tgt).max()
    for t in np.unique(te):
        ix = te == t
        u2 = upd[ix]
        per_te[t] = dict(n=int(ix.sum()),
                         vaf_command=1 - (res[ix] ** 2).sum() / ((u2 - u2.mean(0)) ** 2).sum(),
                         frac_fit=float((np.abs(res[ix]).max(1) < tol).mean()))
    return dict(K=K, F=F, vaf_velocity=vaf_vel, vaf_command=vaf_cmd, vaf_command_kept=vaf_cmd_kept,
                frac_kept=float(keep.mean()), per_te=per_te,
                n_updates=len(up), max_abs_residual=float(np.abs(res).max()))


def j_command_fit_variants(d):
    """Monkey J: readings of the linear map from 5 ms counts to the velocity update, for
    monkey-j-linear-command. The criterion fits the PPF's update over rewarded trials with no
    intercept; the files hold neither the update nor the PPF's parameters, so the update is
    estimated. Frames: every frame of the session, or frames from go to reward of the trials table.
    Cursor dynamics F: fitted jointly with the map on the state before (position, velocity, with or
    without the offset column, which acts as an intercept), or the identity on velocity (update =
    velocity minus the velocity before). Variance accounted for as in the criterion: 1 minus the
    summed squared residual of x and y over the summed squares of the demeaned update."""
    S = d["decoder_state"]
    Y = d["spike_counts"].astype(float)
    up = np.arange(1, len(S))
    go = np.round(d["start"] * d["rate"]).astype(int)
    rw = np.round(d["stop"] * d["rate"]).astype(int)
    intr = np.zeros(len(S), bool)
    for g, r in zip(go, rw):
        intr[g + 1:r + 1] = True
    out = []
    for frames in ["all", "rewarded trials"]:
        u = up if frames == "all" else up[intr[up]]
        tgt, prev, yb = S[u][:, 2:4], S[u - 1], Y[u]
        for fname, cols in [("fitted, with offset", [0, 1, 2, 3, 4]), ("fitted, no offset", [0, 1, 2, 3]),
                            ("identity on velocity", None)]:
            if cols is None:
                upd = tgt - prev[:, 2:4]
                K, *_ = np.linalg.lstsq(yb, upd, rcond=None)
                res = upd - yb @ K
            else:
                X = np.hstack([prev[:, cols], yb])
                beta, *_ = np.linalg.lstsq(X, tgt, rcond=None)
                upd = tgt - prev[:, cols] @ beta[:len(cols)]
                res = tgt - X @ beta
            out.append(dict(frames=frames, dynamics=fname, n=len(u),
                            vaf=1 - (res ** 2).sum() / ((upd - upd.mean(0)) ** 2).sum()))
    return out


def cw_ccw(center, target, traj):
    """util_fcns.CW_CCW_obs: 0 for clockwise, 1 for counterclockwise. traj is T x 2."""
    tc = target - center
    ang = np.arctan2(tc[1], tc[0])
    R = np.array([[np.cos(-ang), -np.sin(-ang)], [np.sin(-ang), np.cos(-ang)]])
    rot = R @ (traj - center).T
    dx = np.hstack([[0], np.diff(rot[0])])
    s = float(np.dot(dx, rot[1]))
    return (0 if s > 0 else 1), s


def j_targets_m(amy):
    """Monkey J obstacle-task target centres in metres, in the decoder's frame (util_fcns.add_targ_locs)."""
    return (amy["targPos"] - np.array([0.0, 2.5])) / 100.0 + J_CENTER


def load_amy():
    raw = urllib.request.urlopen(CODE_RAW + "resim_ppf/jeev_obs_positions_from_amy.mat").read()
    return sio.loadmat(io.BytesIO(raw))


def bin_session(d, monkey, K, amy=None):
    """Bins of rewarded trials, commands and condition labels.

    Returns a dict of arrays over bins: spk (counts per 100 ms), cmd (2), pos (2, cursor at the bin's
    end), vel (decoder velocity at the bin's end), trl, bin_num, rev_bin_num, task (0 co, 1 obstacle),
    target, cw (0 cw, 1 ccw, -1 center-out), cond (string), plus a per-trial table `trials`.
    """
    rate = d["rate"]
    S = d["decoder_state"]
    Y = d["spike_counts"].astype(float)
    nfr = len(S)
    go = np.round(d["start"] * rate).astype(int)
    rw = np.round(d["stop"] * rate).astype(int)
    if monkey == "G":
        up = np.zeros(nfr, bool)
        up[d["update_bmi"] == 1] = True
    out = {k: [] for k in ["spk", "cmd", "pos", "vel", "trl", "bin_num", "rev_bin_num"]}
    trials = []
    for it, (g, r) in enumerate(zip(go, rw)):
        if monkey == "G":
            ends = np.array([i for i in range(g, min(r, nfr - 1) + 1) if up[i] and i >= g + 5])
            if len(ends) < 1:
                continue
            spk = np.vstack([Y[i - 5:i + 1].sum(0) for i in ends])
            cmd = spk @ K.T
            pos = S[ends][:, :2]
            vel = S[ends][:, 2:4]
            obs = d["obs_details"][g:r + 1]
            task = 0 if np.all(obs == "na") else 1
            endpos = d["cursor"][r]
            tgt = int(np.round(np.degrees(np.arctan2(endpos[1], endpos[0])) / 45.0)) % 8
            if task == 1:
                tpos = 10.0 * np.array([np.cos(np.radians(45 * tgt)), np.sin(np.radians(45 * tgt))])
                cw, _ = cw_ccw(np.zeros(2), tpos, pos)
            else:
                cw = -1
            ttype = tgt
        else:
            edges = np.arange(g, r + 20, 20)
            edges = edges[edges + 20 <= nfr]
            if len(edges) < 2:
                continue
            spk = np.vstack([Y[e:e + 20].sum(0) for e in edges[:-1]])
            cmd = 100.0 * (spk @ K.T)
            pos = S[edges[1:] - 1][:, :2]
            vel = S[edges[1:] - 1][:, 2:4]
            startpos, endpos = d["cursor"][g], d["cursor"][r]
            te = d["te_num"][g]
            # task from the block: obstacle blocks have obstacle values (the code fills them per block)
            if not _j_is_obs_block(d, te):
                task = 0
                ang = np.degrees(np.arctan2(*(endpos - J_CENTER)[::-1]))
                tgt = int(np.round(ang / 45.0)) % 8
                ttype, cw = tgt, -1
            else:
                task = 1
                tm = j_targets_m(amy)
                ds = np.linalg.norm(tm - startpos, axis=1)
                de = np.linalg.norm(tm - endpos, axis=1)
                s_num, e_num = int(np.nanargmin(ds)) + 1, int(np.nanargmin(de)) + 1
                hit = np.where((J_TRIAL_LIST[:, 0] == s_num) & (J_TRIAL_LIST[:, 2] == e_num))[0]
                ttype = int(hit[0]) if len(hit) else -1
                tgt = ttype
                if ttype in J_CW_FIXED and ttype not in (2,):
                    cw = J_CW_FIXED[ttype]
                elif ttype >= 0:
                    cw, _ = cw_ccw(tm[s_num - 1] * 20, tm[e_num - 1] * 20, pos * 20)
                else:
                    cw = -1
        if monkey == "J" and task == 1 and ttype < 2:
            # analysis_config.min_targix['jeev'] = [0, 2]: obstacle trial types 0 and 1 not analysed
            # (Methods: only partial or full obstruction); -1 is a pair not in the code's list
            trials.append(dict(trl=it, task=task, target=tgt, ttype=ttype, cw=cw, cond="dropped",
                               nbins=0, te=d["te_num"][g], go=g, reward=r))
            continue
        cond = ("co" if task == 0 else ("cw" if cw == 0 else "ccw")) + f"{tgt}"
        n = len(spk)
        out["spk"].append(spk)
        out["cmd"].append(cmd)
        out["pos"].append(pos)
        out["vel"].append(vel)
        out["trl"].append(np.full(n, it))
        out["bin_num"].append(np.arange(n))
        out["rev_bin_num"].append(np.arange(n)[::-1])
        trials.append(dict(trl=it, task=task, target=tgt, ttype=ttype, cw=cw, cond=cond, nbins=n,
                           te=d["te_num"][g], go=g, reward=r))
    B = {k: np.concatenate(v) for k, v in out.items()}
    import pandas as pd
    T = pd.DataFrame(trials)
    lab = T[T.cond != "dropped"].set_index("trl")
    for k in ["task", "target", "ttype", "cw", "cond"]:
        B[k] = lab.loc[B["trl"], k].values
    B["trials"] = T
    return B


def _j_is_obs_block(d, te):
    ix = d["te_num"] == te
    return bool(np.isfinite(d["obs_details"][ix]).any())


def mag_boundaries(cmd):
    return np.percentile(np.linalg.norm(cmd, axis=1), MAG_PERCENTILES)


def command_bins(cmd, mags):
    """(magnitude bin 0-4, angle bin 0-7) per command (util_fcns.commands2bins)."""
    mag = np.linalg.norm(cmd, axis=1)
    ang = np.arctan2(cmd[:, 1], cmd[:, 0])
    ang[ang < 0] += 2 * np.pi
    rads = np.linspace(0.0, 2 * np.pi, 9) + np.pi / 8
    mb = np.digitize(mag, mags)
    ab = np.digitize(ang, rads)
    ab[ab == 8] = 0
    return mb, ab


def match_pool(cmd_cond, cmd_pool, ix_mov, psig=0.05, perc_drop=0.05):
    """plot_fr_diffs.distribution_match_global_mov with keep_mov_indices_in_pool=True.

    cmd_cond: the condition's commands; cmd_pool: the commands of the pool (all conditions);
    ix_mov: positions of the condition's commands within the pool. Returns kept pool positions or
    an empty array when the pool is no larger than the condition.
    """
    n = len(cmd_cond)
    idx = np.arange(len(cmd_pool))
    mean_m = cmd_cond.mean(0)
    sd_m = cmd_cond.std(0)
    keep = np.zeros(len(cmd_pool), bool)
    keep[ix_mov] = True
    while True:
        p = [scipy.stats.ttest_ind(cmd_cond[:, v], cmd_pool[idx, v]).pvalue for v in range(2)]
        if np.all(np.array(p) > psig):
            return idx
        if len(idx) <= n:
            return np.array([], int)
        cost = (((cmd_pool[idx] - mean_m) / sd_m) ** 2).sum(1)
        cost[keep[idx]] = 0.0
        nd = int(np.floor(perc_drop * len(cost)))
        if nd == 0:
            return np.array([], int)
        order = np.argsort(cost, kind="stable")
        idx = np.delete(idx, order[-nd:])


def match_pairwise(c1, c2, psig=0.05, perc_drop=0.05):
    """plot_fr_diffs.distribution_match_mov_pairwise: while a t-test on either command dimension
    gives p <= psig, drop the perc_drop share of the larger set farthest (variance-scaled squared
    distance) from the smaller set's mean. Returns kept positions in c1 and c2."""
    i1, i2 = np.arange(len(c1)), np.arange(len(c2))
    m1, m2, s1, s2 = c1.mean(0), c2.mean(0), c1.std(0), c2.std(0)
    while True:
        p = [scipy.stats.ttest_ind(c1[i1, v], c2[i2, v]).pvalue for v in range(c1.shape[1])]
        if np.all(np.array(p) > psig):
            return i1, i2
        if len(i1) == 0 or len(i2) == 0:
            return np.array([], int), np.array([], int)
        if len(i1) >= len(i2):
            cost = (((c1[i1] - m2) / s2) ** 2).sum(1)
            nd = int(np.floor(perc_drop * len(cost)))
            if nd == 0:
                return np.array([], int), np.array([], int)
            i1 = np.delete(i1, np.argsort(cost)[-nd:])
        else:
            cost = (((c2[i2] - m1) / s1) ** 2).sum(1)
            nd = int(np.floor(perc_drop * len(cost)))
            if nd == 0:
                return np.array([], int), np.array([], int)
            i2 = np.delete(i2, np.argsort(cost)[-nd:])


def tuples(B, mags, min_obs=MIN_OBS, min_conds=1, edge_bins=0):
    """(command, condition) tuples with at least min_obs occurrences, for commands with at least
    min_conds such conditions. Returns a list of dicts with the bins of the condition (ix), the
    command's bins over all conditions (ix_com), and the matched pool (ix_pool, empty if dropped).
    edge_bins drops bins within that many bins of a trial's start or end (as return_command_indices)."""
    mb, ab = command_bins(B["cmd"], mags)
    valid = (B["bin_num"] >= edge_bins) & (B["rev_bin_num"] >= edge_bins)
    out = []
    for m in range(4):
        for a in range(8):
            ix_com = np.where((mb == m) & (ab == a) & valid)[0]
            conds, counts = np.unique(B["cond"][ix_com], return_counts=True)
            ok = conds[counts >= min_obs]
            if len(ok) < min_conds or len(ok) == 0:
                continue
            for c in ok:
                ix = ix_com[B["cond"][ix_com] == c]
                pos = np.searchsorted(ix_com, ix)
                kept = match_pool(B["cmd"][ix], B["cmd"][ix_com], pos)
                out.append(dict(mag=m, ang=a, cond=c, ix=ix, ix_com=ix_com,
                                ix_pool=ix_com[kept] if len(kept) and len(kept) > len(ix) else np.array([], int),
                                n_conds=len(ok)))
    return out


def null_basis(K):
    """Orthonormal basis of the decoder-null space (scipy.linalg.null_space), N x (N-2)."""
    return scipy.linalg.null_space(K)


def r2_pooled(y, yhat):
    """generalization_plots.r2: 1 - summed squared error / summed squares about each column's mean."""
    return 1 - ((y - yhat) ** 2).sum() / ((y - y.mean(0)) ** 2).sum()


def pairs_in_trials(B):
    """Indices t with t-1 in the same trial (pairs of consecutive bins)."""
    t = np.where(B["bin_num"] >= 1)[0]
    return t - 1, t


def ridge_fit(X, Y, alpha):
    """sklearn Ridge(alpha, fit_intercept=True) in closed form. Returns (W, b): Y ~ X W + b."""
    mx, my = X.mean(0), Y.mean(0)
    Xc, Yc = X - mx, Y - my
    W = np.linalg.solve(Xc.T @ Xc + alpha * np.eye(X.shape[1]), Xc.T @ Yc)
    return W, my - mx @ W


def folds(n, task, k=5, seed=0):
    """5 folds over bins, stratified by task (shared method; random with a fixed seed)."""
    rng = np.random.default_rng(seed)
    f = np.zeros(n, int)
    for t in np.unique(task):
        ix = np.where(task == t)[0]
        ix = rng.permutation(ix)
        f[ix] = np.arange(len(ix)) % k
    return f


def choose_alpha(X, Y, fold, grid=RIDGE_GRID):
    """Ridge parameter with the best 5-fold pooled R2 over the grid (Methods; generate_models.py)."""
    best, best_r2 = None, -np.inf
    for a in grid:
        pred = np.zeros_like(Y)
        for k in np.unique(fold):
            tr, te = fold != k, fold == k
            W, b = ridge_fit(X[tr], Y[tr], a)
            pred[te] = X[te] @ W + b
        r2 = r2_pooled(Y, pred)
        if r2 > best_r2:
            best, best_r2 = a, r2
    return best, best_r2


def behavior_shuffle(B, mags, rng):
    """Behavior-preserving shuffle: permute activity among bins that share a command bin (Methods).
    Returns the permutation index (bin i takes the activity of bin perm[i])."""
    mb, ab = command_bins(B["cmd"], mags)
    lab = mb * 8 + ab
    perm = np.arange(len(lab))
    for l in np.unique(lab):
        ix = np.where(lab == l)[0]
        perm[ix] = ix[rng.permutation(len(ix))]
    return perm


def condition_on_command(pred, Sigma, K, cmd, b_cmd=None):
    """E[x | c = K x] for x ~ N(pred, Sigma): Gaussian conditioning (Methods, generate_models.py 2294-2298)."""
    KS = K @ Sigma
    G = KS.T @ np.linalg.inv(KS @ K.T)
    return pred + (cmd - pred @ K.T) @ G.T


def math_angle(a, b):
    """Signed angle in degrees from vector a to b (rows), sign from the cross product."""
    cross = a[:, 0] * b[:, 1] - a[:, 1] * b[:, 0]
    dot = (a * b).sum(1)
    return np.degrees(np.arctan2(cross, dot))


def prepare(B, dec, monkey):
    """Adds the command matrix (counts to command; Monkey J in cm, ppf_pa._bin_neural_push), its
    decoder-null basis and the session's magnitude boundaries to B."""
    B["Kc"] = dec["K"] * (100.0 if monkey == "J" else 1.0)
    B["Nb"] = null_basis(B["Kc"])
    B["mags"] = mag_boundaries(B["cmd"])
    return B
