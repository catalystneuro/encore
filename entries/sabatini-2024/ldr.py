"""Loading and measures for testing Sabatini & Kaufman (2024) on DANDI:000070.

Where each parameter comes from is said beside it:
- "claims": the claim's criterion in claims/sabatini-2024.yaml (which cites the paper or its code);
- "Methods, <section>": a passage of the paper taken by the author (protocol, author step 1.6);
- "assumption": a choice the paper leaves open, recorded as a deviation in the attempt;
- "standard": a choice that cannot change a result (a padding margin, a plotting detail).

The dandiset is read by streaming (remfile + h5py); nothing is written to disk.
"""

from __future__ import annotations

import numpy as np
import h5py
import remfile
import requests
from scipy.ndimage import gaussian_filter1d

DANDISET = "000070"
VERSION = "0.260528.0919"
# The two files the paper's Data availability statement names.
ASSETS = {
    "J": "sub-Jenkins/sub-Jenkins_ses-20090918_behavior+ecephys.nwb",
    "N": "sub-Nitschke/sub-Nitschke_ses-20100923_behavior+ecephys.nwb",
}
API = "https://api.dandiarchive.org/api"

# Time base (claims, shared method): -350 to +850 ms around movement onset, every 10 ms (121 bins).
GRID_MS = np.arange(-350, 851, 10)
# Dynamics are fitted from -150 ms on (Methods, Fitting dynamics to single conditions); index 20.
FIT0 = 20
# 1 ms counts are taken over a wider window so that the 20 ms Gaussian has data at the edges
# (standard; the code pads symmetrically).
PAD_MS = 150
WIN0_MS, WIN1_MS = -350 - PAD_MS, 850 + PAD_MS + 1
SMOOTH_SD_MS = 20  # Methods, Subjects, behavior and data pre-processing
WARP_MS = 600  # Methods, Control for stereotyped time course of behavior


def asset_url(path, version=VERSION):
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{version}/assets/",
                     params={"path": path}, timeout=60)
    r.raise_for_status()
    hits = [a for a in r.json()["results"] if a["path"] == path]
    assert len(hits) == 1, path
    aid = hits[0]["asset_id"]
    return requests.head(f"{API}/assets/{aid}/download/", allow_redirects=True, timeout=60).url, aid


def open_nwb(monkey):
    url, aid = asset_url(ASSETS[monkey])
    return h5py.File(remfile.File(url), "r"), aid


def _segments(t):
    """Index ranges [a, b) of runs in which times do not go backwards."""
    cuts = np.where(np.diff(t) < 0)[0] + 1
    edges = np.r_[0, cuts, len(t)]
    return [(edges[i], edges[i + 1]) for i in range(len(edges) - 1)]


def assign_trial_segments(start, hand_seg_bounds):
    """Segment of each trial, walking through trials in file order: the segment advances when a
    trial starts before the previous one, or after the end of the current hand segment."""
    seg = np.zeros(len(start), int)
    s = 0
    for k in range(len(start)):
        if k > 0 and (start[k] < start[k - 1] or start[k] > hand_seg_bounds[s][1]):
            s += 1
        seg[k] = s
    return seg


def load_trials(f):
    T = f["intervals/trials"]
    cols = ["maze_condition", "task_success", "discard_trial", "correct_reach", "maze_num_targets",
            "maze_num_barriers", "novel_maze", "start_time", "stop_time", "go_cue_time",
            "move_begins_time", "move_ends_time", "target_presentation_time", "trial_version"]
    d = {c: T[c][:] for c in cols}
    tp = T["target_positions"][:]
    ti = T["target_positions_index"][:]
    first = np.r_[0, ti[:-1]]
    d["target_x"] = tp[first, 0].astype(float)
    d["target_y"] = tp[first, 1].astype(float)
    d["delay"] = d["go_cue_time"] - d["target_presentation_time"]
    bi = T["barrier_info_index"][:]
    d["n_barrier_rows"] = np.diff(np.r_[0, bi])
    return d


def select_trials(d, reading="b"):
    """Trials of the 72 conditions (claims, shared method).

    Conditions: maze_condition not a multiple of 3, which is also the set of 1-target mazes
    (reading (a) and (b) of the claims give the same set here; shown in the notebook).
    Trials: reading (a) all successful trials; reading (b) successful trials with delay > 400 ms.
    """
    mc = d["maze_condition"]
    keep = (mc % 3 != 0) & (d["task_success"] == 1)
    if reading == "b":
        keep &= d["delay"] > 0.4
    return keep


def load_session(monkey, shuffle_seeds=(), progress=False):
    """Stream one session; return single-trial smoothed rates and hand position.

    For every successful trial of the 72 conditions (reading (a); reading (b) is a subset), returns
    1 ms spike counts reduced as the analyses need them:
      R   (trials, units, 121) smoothed rates (Gaussian s.d. 20 ms on 1 ms counts, spikes/s),
          sampled at GRID_MS around movement onset;
      C10 (trials, units, 121) spike counts summed in 10 ms bins [t, t+10), times 100 (spikes/s);
      RS  {seed: array} as R, with the 1 ms bins of each trial permuted in time before
          smoothing (tbf-shuffle-control), one array per seed;
      RW  as R, time-warped so that the reach lasts 600 ms, post-reach truncated at 850 ms;
      RW2 as R, warped to 600 ms with the post-reach part warped to last 250 ms.
    Hand position (trials, 1201, 2) at 1 ms over -350..+850 ms.
    """
    f, aid = open_nwb(monkey)
    d = load_trials(f)
    keep = select_trials(d, "a")
    # hand, by segment
    ht = f["processing/behavior/Position/Hand/timestamps"][:]
    hd = f["processing/behavior/Position/Hand/data"][:]
    hsegs = _segments(ht)
    hb = [(ht[a], ht[b - 1]) for a, b in hsegs]
    tseg = assign_trial_segments(d["start_time"], hb)
    d["segment"] = tseg
    idx = np.where(keep)[0]
    onset = d["move_begins_time"][idx]
    ntr = len(idx)
    win = np.arange(WIN0_MS, WIN1_MS)  # ms offsets
    nwin = len(win)
    # window must lie within the trial (spikes are stored only within trials)
    ok_win = (onset + WIN0_MS / 1000 >= d["start_time"][idx]) & (onset + WIN1_MS / 1000 <= d["stop_time"][idx])
    # hand position at 1 ms over -350..+850, per segment
    hand = np.full((ntr, 1201, 2), np.nan)
    hgrid = np.arange(-350, 851) / 1000
    for i, k in enumerate(idx):
        a, b = hsegs[tseg[k]]
        tt = ht[a:b]
        q = onset[i] + hgrid
        if q[0] < tt[0] or q[-1] > tt[-1]:
            continue
        j = np.searchsorted(tt, q)
        j = np.clip(j, 1, len(tt) - 1)
        w = (q - tt[j - 1]) / (tt[j] - tt[j - 1])
        hand[i] = hd[a:b][j - 1] * (1 - w)[:, None] + hd[a:b][j] * w[:, None]
    # spikes
    u = f["units"]
    sidx = u["spike_times_index"][:]
    nunits = len(sidx)
    loc = f["general/extracellular_ephys/electrodes/location"][:]
    el = u["electrodes"][:]
    area = np.array(["PMd" if b"Pre-Motor" in loc[e] else "M1" for e in el])
    counts = np.zeros((ntr, nunits, nwin), np.uint8)
    unit_jumps = np.zeros(nunits, int)
    a0 = 0
    for un in range(nunits):
        s = u["spike_times"][a0:sidx[un]]
        a0 = sidx[un]
        segs = _segments(s)
        unit_jumps[un] = len(segs) - 1
        if len(segs) != tseg.max() + 1 and tseg.max() == 0:
            # one recording segment but a spike train that restarts (one unit in J): the runs are
            # merged and sorted, as an electrode's multi-unit activity (assumption, notebook).
            s = np.sort(s)
            segs = [(0, len(s))]
        for sg in range(tseg.max() + 1):
            m = tseg[idx] == sg
            if not m.any():
                continue
            if len(segs) != tseg.max() + 1:
                raise RuntimeError(f"unit {un}: {len(segs)} spike runs, {tseg.max() + 1} segments")
            a, b = segs[sg]
            ss = s[a:b]
            ii = np.where(m)[0]
            t0 = onset[ii] + WIN0_MS / 1000
            lo = np.searchsorted(ss, t0)
            hi = np.searchsorted(ss, onset[ii] + WIN1_MS / 1000)
            for q, i in enumerate(ii):
                if hi[q] > lo[q]:
                    b_ = np.floor((ss[lo[q]:hi[q]] - t0[q]) * 1000).astype(int)
                    b_ = b_[(b_ >= 0) & (b_ < nwin)]
                    np.add.at(counts[i, un], b_, 1)
        if progress and un % 48 == 0:
            print("unit", un, flush=True)
    f.close()
    # reductions
    gi = GRID_MS - WIN0_MS  # indices of the grid in the 1 ms window
    R = np.zeros((ntr, nunits, len(GRID_MS)), np.float32)
    RS = {sd: np.zeros_like(R) for sd in shuffle_seeds}
    rngs = {sd: np.random.default_rng(sd) for sd in shuffle_seeds}
    RW = np.zeros_like(R)
    RW2 = np.zeros_like(R)
    C10 = np.zeros_like(R)
    dur = reach_duration(hand)
    for i in range(ntr):
        c = counts[i].astype(np.float32)
        sm = gaussian_filter1d(c, SMOOTH_SD_MS, axis=1, mode="reflect") * 1000
        R[i] = sm[:, gi]
        for sd in shuffle_seeds:
            # the trial's 1 ms bins permuted in time, the same permutation for every unit so that
            # spike correlations between units are kept (Methods, Control for data smoothing); over
            # the window read (assumption; claims, tbf-shuffle-control, code scrambleTrials.m)
            cs = c[:, rngs[sd].permutation(nwin)]
            RS[sd][i] = gaussian_filter1d(cs, SMOOTH_SD_MS, axis=1, mode="reflect")[:, gi] * 1000
        cc = c[:, gi[0]:gi[0] + 1210].reshape(nunits, 121, 10).sum(2)
        C10[i] = cc * 100
        if np.isfinite(dur[i]):
            for arr, mode in ((RW, "truncate"), (RW2, "warp250")):
                tq = warp_map(GRID_MS, dur[i], mode) - WIN0_MS
                j = np.clip(np.floor(tq).astype(int), 0, nwin - 2)
                w = (tq - j)[None, :]
                arr[i] = sm[:, j] * (1 - w) + sm[:, j + 1] * w
        else:
            RW[i] = np.nan
            RW2[i] = np.nan
    info = dict(asset_id=aid, n_all_trials=len(d["start_time"]), unit_jumps=unit_jumps,
                n_hand_segments=len(hsegs), hand_segment_bounds=hb, ok_window=ok_win,
                spikes_per_unit=np.diff(np.r_[0, sidx]))
    tr = {k: v[idx] for k, v in d.items()}
    tr["duration_ms"] = dur
    return dict(trials=tr, all_trials=d, R=R, RS=RS, RW=RW, RW2=RW2, C10=C10, hand=hand,
                area=area, info=info)


def reach_duration(hand):
    """Per trial, ms from movement onset to the last 1 ms sample at which hand speed is at least a
    tenth of its peak (claims, fig3i, from code warpTrials.m). Speed over 0..+850 ms."""
    v = np.gradient(hand, axis=1)  # per ms
    sp = np.hypot(v[..., 0], v[..., 1])[:, 350:]
    out = np.full(len(hand), np.nan)
    for i in range(len(hand)):
        if np.isfinite(sp[i]).all():
            pk = sp[i].max()
            out[i] = np.where(sp[i] >= 0.1 * pk)[0].max()
    return out


def warp_map(grid_ms, dur, mode):
    """Original time (ms) sampled at each warped grid time (Methods, Control for stereotyped time
    course of behavior): before onset unchanged; 0..dur mapped linearly to 0..600 ms; after the
    reach either unwarped and truncated at 850 ms ('truncate'), or the post-reach activity up to
    850 ms after onset warped to last 250 ms ('warp250')."""
    g = np.asarray(grid_ms, float)
    out = g.copy()
    m = (g >= 0) & (g <= WARP_MS)
    out[m] = g[m] * dur / WARP_MS
    post = g > WARP_MS
    if mode == "truncate":
        out[post] = dur + (g[post] - WARP_MS)
    else:
        out[post] = dur + (g[post] - WARP_MS) * (850 - dur) / 250
    return out


# ---------------------------------------------------------------- condition structure

def condition_table(tr):
    """The 72 conditions in maze-condition order, with straight/curved and the target angle."""
    mc = np.unique(tr["maze_condition"])
    straight = np.array([(tr["maze_num_barriers"][tr["maze_condition"] == m] == 0).all() for m in mc])
    tx = np.array([np.median(tr["target_x"][tr["maze_condition"] == m]) for m in mc])
    ty = np.array([np.median(tr["target_y"][tr["maze_condition"] == m]) for m in mc])
    cond = np.searchsorted(mc, tr["maze_condition"])
    return dict(maze=mc, straight=straight, tx=tx, ty=ty, angle=np.arctan2(ty, tx), cond=cond)


def cond_average(X, cond, nc, mask=None):
    """Mean over trials per condition; X (trials, ...) -> (conditions, ...)."""
    if mask is None:
        mask = np.ones(len(cond), bool)
    W = np.zeros((nc, len(cond)))
    W[cond[mask], np.where(mask)[0]] = 1
    W /= W.sum(1, keepdims=True)
    return (W[:, mask] @ X[mask].reshape(int(mask.sum()), -1)).reshape((nc,) + X.shape[1:])


def split_half(cond, nc, rng, mask=None):
    """Random assignment of each condition's trials to two partitions of equal size (+-1)."""
    if mask is None:
        mask = np.ones(len(cond), bool)
    a = np.zeros(len(cond), bool)
    for c in range(nc):
        ii = np.where(mask & (cond == c))[0]
        p = rng.permutation(ii)
        a[p[: len(p) // 2]] = True
    b = mask & ~a
    return a & mask, b


# ---------------------------------------------------------------- variance measures

def pop_ve(X, Xh):
    """Population variance explained (claims, shared method; code getVarExplained.m):
    1 - summed variance over neurons of the residual / summed variance of the data, floored at 0.
    X, Xh: (neurons, time)."""
    num = np.var(X - Xh, axis=-1).sum(-1)
    den = np.var(X, axis=-1).sum(-1)
    return np.maximum(0.0, 1 - num / den)


# ---------------------------------------------------------------- temporal basis factorization

def tbf(Xc, k):
    """Temporal basis factorization (Methods, Factorizing neural activity using temporal basis
    functions). Xc (conditions, neurons, time). SVD of the (neurons x conditions)-by-time matrix;
    returns basis B (k, time) and loadings L (conditions, neurons, k), X(c) ~ L(c) B."""
    C, N, T = Xc.shape
    A = Xc.reshape(C * N, T)
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    B = Vt[:k]
    L = (U[:, :k] * S[:k]).reshape(C, N, k)
    return B, L


def loadings(Xc, B):
    """Loadings of each condition on a fixed basis by least squares (Methods, Measuring the
    across-condition alignment of rotations: 'used linear regression to identify the loading
    matrix')."""
    return Xc @ np.linalg.pinv(B)


def cv_tbf_k(Rtr, cond, nc, rng, kmax=20, folds=100, mask=None, t0=FIT0):
    """Held-out variance explained for k = 1..kmax (Methods, Cross-validating the number of
    temporal basis functions): TBF on one half of the trials, compared with the other half."""
    ve = np.zeros((folds, kmax))
    for f_ in range(folds):
        a, b = split_half(cond, nc, rng, mask)
        XA = cond_average(Rtr, cond, nc, a)[..., t0:]
        XB = cond_average(Rtr, cond, nc, b)[..., t0:]
        C, N, T = XA.shape
        U, S, Vt = np.linalg.svd(XA.reshape(C * N, T), full_matrices=False)
        for k in range(1, kmax + 1):
            Xh = ((U[:, :k] * S[:k]) @ Vt[:k]).reshape(C, N, T)
            ve[f_, k - 1] = pop_ve(XB, Xh).mean()
    return ve


def fit_lds_ls(Z):
    """Least-squares LDS z(t+1) = M z(t) on rows of Z (dims, time)."""
    return Z[:, 1:] @ np.linalg.pinv(Z[:, :-1])


def demix(B, L):
    """De-mix the basis (Methods, De-mixing temporal basis functions): fit an LDS to the basis
    functions and project onto its eigenvectors, in real form (a conjugate pair becomes the real
    and imaginary parts of its eigenvector, spanning the same plane). Returns basis, loadings,
    eigenvalues (one per basis row, the pair's eigenvalue with positive angle on both rows),
    and a group label per row (rotation index; -1 for real modes), rotations sorted by frequency."""
    M = fit_lds_ls(B)
    lam, V = np.linalg.eig(M)
    cols, lams, kinds = [], [], []
    used = np.zeros(len(lam), bool)
    for i in np.argsort(np.abs(np.angle(lam))):
        if used[i]:
            continue
        if abs(lam[i].imag) < 1e-10:
            cols.append(V[:, i].real)
            lams.append(lam[i].real)
            kinds.append(("real", lam[i].real))
            used[i] = True
        else:
            j = np.argmin(np.abs(lam - np.conj(lam[i])) + used * 1e9 + (np.arange(len(lam)) == i) * 1e9)
            used[i] = used[j] = True
            l = lam[i] if lam[i].imag > 0 else lam[j]
            v = V[:, i] if lam[i].imag > 0 else V[:, j]
            cols += [v.real, v.imag]
            lams += [l, l]
            kinds += [("pair", l), ("pair", l)]
    P = np.array(cols).T
    Bd = np.linalg.solve(P, B)
    Ld = L @ P
    lams = np.array(lams, complex)
    freq = np.abs(np.angle(lams)) / (2 * np.pi) * 100
    group = np.full(len(lams), -1)
    pf = sorted({round(fr, 9) for fr, (kd, _) in zip(freq, kinds) if kd == "pair"})
    for r, fr in enumerate(pf):
        group[np.isclose(freq, fr) & np.array([kd == "pair" for kd, _ in kinds])] = r
    # normalise each basis row to unit norm, scaling loadings inversely (standard)
    nrm = np.linalg.norm(Bd, axis=1)
    return Bd / nrm[:, None], Ld * nrm, lams, group, freq


# ---------------------------------------------------------------- alignment and angles

def orth(A):
    """Orthonormal basis of the column span of A (neurons, d)."""
    U, S, _ = np.linalg.svd(A, full_matrices=False)
    return U[:, S > S[0] * 1e-10]


def alignment_index(L1, B1, L2):
    """Fraction of the variance of activity L1 @ B1 (neurons x time) captured by projection onto
    span(L2) (claims, shared method; code getAlignmentIndex.m)."""
    Y = L1 @ B1
    Y = Y - Y.mean(1, keepdims=True)
    Q = orth(L2)
    return np.sum((Q.T @ Y) ** 2) / np.sum(Y ** 2)


def sea(planes, ndim=25, seeds=None):
    """Subspace excursion angles (Methods, Subspace excursion angles). planes: list of
    (neurons, d) orthonormal bases. From a seed, repeatedly add the vector of any other subspace
    that forms the greatest angle with the span so far. Every seed is tried and the sequence with
    the largest summed angles is kept (the Methods optimise over sequences; assumption that
    greedy steps from the best seed implement it). Returns angles in degrees."""
    best, bestsum = None, -1
    if seeds is None:
        seeds = range(len(planes))
    P = np.stack(planes)  # (c, N, d)
    for s0 in seeds:
        S = planes[s0].copy()
        angs = []
        while len(angs) < ndim and S.shape[1] < P.shape[1]:
            R = P - np.einsum("nk,cmd,mk->cnd", S, P, S)  # residuals (c, N, d)
            G = np.einsum("cnd,cne->cde", R, R)
            w, v = np.linalg.eigh(G)
            c = int(np.argmax(w[:, -1]))
            sv = np.sqrt(max(w[c, -1], 0.0))
            angs.append(np.degrees(np.arcsin(min(1.0, sv))))
            vec = R[c] @ v[c, :, -1]
            vec = vec / np.linalg.norm(vec)
            vec = vec - S @ (S.T @ vec)
            S = np.column_stack([S, vec / np.linalg.norm(vec)])
        if sum(angs) > bestsum:
            bestsum, best = sum(angs), np.array(angs)
    return best


def pmap(func, args, processes=4):
    """Run func over args in forked worker processes (standard; speeds up independent fits)."""
    import multiprocessing as mp
    with mp.get_context("fork").Pool(processes) as pool:
        return pool.map(func, args)


def participation_ratio(ev):
    ev = np.asarray(ev)
    return ev.sum() ** 2 / np.sum(ev ** 2)


# ---------------------------------------------------------------- single-condition LDS

def rrr_lds(X, k, max_half_life_s=10.0, dt_s=0.01):
    """Reduced-rank LDS for one condition (Methods, Fitting dynamics to single conditions).
    X (neurons, time). x(t+1) = x(t) M with rank(M) = k, by reduced-rank regression; eigenvalues
    with half-life > 10 s are shrunk to a 10 s half-life; the system is simulated forward from the
    first state. Returns the simulated activity and the k eigenvalues of the reduced system."""
    Xp, Xf = X[:, :-1].T, X[:, 1:].T
    Mols = np.linalg.pinv(Xp) @ Xf
    Yh = Xp @ Mols
    _, _, Vt = np.linalg.svd(Yh, full_matrices=False)
    V = Vt[:k].T  # (N, k)
    A = V.T @ Mols @ V  # z(t+1) = z(t) A, with z = x V
    lam, W = np.linalg.eig(A)
    rmax = 0.5 ** (dt_s / max_half_life_s)
    mag = np.abs(lam)
    lam2 = np.where(mag > rmax, lam / mag * rmax, lam)
    A2 = (W @ np.diag(lam2) @ np.linalg.inv(W)).real
    T = X.shape[1]
    out = np.zeros((T, X.shape[0]))
    x0 = X[:, 0]
    out[0] = x0
    z = (x0 @ Mols) @ V
    out[1] = z @ V.T
    for t in range(2, T):
        z = z @ A2
        out[t] = z @ V.T
    return out.T, lam2


def cv_condition_dim(Rtr, cond, nc, rng, ks, folds=100, mask=None, t0=FIT0, frac=0.5):
    """Per condition, PCA dimensionality by cross-validation over trial partitions (Methods,
    Fitting dynamics to single conditions): singular vectors from X, projection of X onto the
    top k, variance explained in Y. Returns (folds, conditions, len(ks))."""
    out = np.zeros((folds, nc, len(ks)))
    for f_ in range(folds):
        a = np.zeros(len(cond), bool)
        m = np.ones(len(cond), bool) if mask is None else mask
        for c in range(nc):
            ii = rng.permutation(np.where(m & (cond == c))[0])
            a[ii[: int(round(len(ii) * frac))]] = True
        b = m & ~a
        XA = cond_average(Rtr, cond, nc, a)[..., t0:]
        XB = cond_average(Rtr, cond, nc, b)[..., t0:]
        for c in range(nc):
            U, S, Vt = np.linalg.svd(XA[c], full_matrices=False)
            for j, k in enumerate(ks):
                Xh = U[:, :k] @ (U[:, :k].T @ XA[c])
                out[f_, c, j] = pop_ve(XB[c], Xh)
    return out


def sort_eigs(lam):
    """Eigenvalues sorted by angle (frequency), conjugates with negative angle dropped."""
    lam = np.asarray(lam)
    lam = lam[lam.imag >= -1e-12]
    return lam[np.lexsort((-lam.real, np.abs(np.angle(lam))))]


# ---------------------------------------------------------------- jPCA

def soft_norm(Xc, const=5.0):
    """Soft normalisation (Methods, Explaining variability in jPCA-identified rotations):
    each neuron divided by its range over conditions and times plus 5."""
    rng_ = Xc.max(axis=(0, 2)) - Xc.min(axis=(0, 2))
    return Xc / (rng_ + const)[None, :, None], rng_ + const


def jpca(Xc, t_idx, npc=6):
    """jPCA (Churchland et al. 2012, as the Methods apply it). Xc (conditions, neurons, time),
    already soft-normalised and mean-subtracted across conditions. Fitted on time indices t_idx.
    Returns dict with PCs, Mskew, Mbest, the jPC planes (in PC space, sorted by eigenvalue
    magnitude), and the R2 of the skew-symmetric and unconstrained fits in the first plane."""
    C, N, T = Xc.shape
    D = Xc[:, :, t_idx].transpose(0, 2, 1).reshape(-1, N)
    mu = D.mean(0)
    U, S, Vt = np.linalg.svd(D - mu, full_matrices=False)
    PC = Vt[:npc].T  # (N, npc)
    Z = (Xc[:, :, t_idx].transpose(0, 2, 1) @ PC)  # (C, T', npc)
    pre = Z[:, :-1].reshape(-1, npc)
    dZ = np.diff(Z, axis=1).reshape(-1, npc)
    Mbest = np.linalg.lstsq(pre, dZ, rcond=None)[0]
    Mskew = fit_skew(pre, dZ)
    ev, evec = np.linalg.eig(Mskew)
    order = np.argsort(-np.abs(ev.imag))
    planes = []
    used = set()
    for i in order:
        if i in used or ev[i].imag <= 0:
            continue
        v = evec[:, i]
        p1, p2 = (v + np.conj(v)).real, ((v - np.conj(v)) * 1j).real
        P = np.linalg.qr(np.column_stack([p1, p2]))[0]
        planes.append(P)
        used.add(i)
    out = dict(PC=PC, Mskew=Mskew, Mbest=Mbest, planes=planes, mu=mu)
    out["R2_skew_2D"], out["R2_best_2D"] = r2_plane(pre, dZ, Mskew, planes[0])
    return out


def r2_plane(pre, dZ, Mskew, P):
    pre2, d2 = pre @ P, dZ @ P
    Ms2 = P.T @ Mskew @ P
    ss = np.sum((d2 - d2.mean(0)) ** 2)
    r2s = 1 - np.sum((d2 - pre2 @ Ms2) ** 2) / ss
    Mb2 = np.linalg.lstsq(pre2, d2, rcond=None)[0]
    r2b = 1 - np.sum((d2 - pre2 @ Mb2) ** 2) / ss
    return r2s, r2b


def fit_skew(X, dX):
    """Least-squares skew-symmetric M with dX ~ X M (jPCA)."""
    n = X.shape[1]
    idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
    H = np.zeros((n * n, len(idx)))
    for q, (i, j) in enumerate(idx):
        Mq = np.zeros((n, n))
        Mq[i, j], Mq[j, i] = 1, -1
        H[:, q] = Mq.reshape(-1)
    A = np.kron(X, np.eye(n))  # vec(X M) row-major = (X kron I) vec(M) row-major
    k = np.linalg.lstsq(A @ H, dX.reshape(-1), rcond=None)[0]
    return (H @ k).reshape(n, n)


# ---------------------------------------------------------------- kinematics

def kin_basis(vel_list):
    """Kinematic basis functions (Methods, Extracting kinematic basis functions, raw-SVD reading):
    SVD of x and y hand velocity of all conditions of all datasets; the top two right singular
    vectors over time; integrated over time to position basis functions. vel_list: arrays
    (conditions, time, 2)."""
    rows = np.concatenate([v.transpose(0, 2, 1).reshape(-1, v.shape[1]) for v in vel_list])
    U, S, Vt = np.linalg.svd(rows, full_matrices=False)
    Bv = Vt[:2]
    for i in range(2):  # sign: positive peak first basis (standard)
        if Bv[i][np.argmax(np.abs(Bv[i]))] < 0:
            Bv[i] = -Bv[i]
    Bp = np.cumsum(Bv, axis=1)
    return Bv, Bp, S


def skewnorm_basis(t, Bv):
    """Second reading of the kinematic basis: least-squares fits of a skew-normal curve and of the
    derivative of a skew-normal curve to the two velocity basis functions (Methods)."""
    from scipy.optimize import least_squares
    from scipy.stats import skewnorm

    def f1(p):
        a, loc, sc, amp = p
        return amp * skewnorm.pdf(t, a, loc, abs(sc) + 1e-6)

    def f2(p):
        a, loc, sc, amp = p
        y = skewnorm.pdf(t, a, loc, abs(sc) + 1e-6)
        return amp * np.gradient(y, t)

    p1 = least_squares(lambda p: f1(p) - Bv[0], [1.0, 200.0, 150.0, Bv[0].max() * 150]).x
    best = None
    for s in (+1, -1):
        r = least_squares(lambda p: f2(p) - Bv[1], [1.0, 200.0, 150.0, s * 1e4])
        if best is None or r.cost < best.cost:
            best = r
    v = np.array([f1(p1), f2(best.x)])
    return v, np.cumsum(v, axis=1)


def reach_params(pos, Bp):
    """Four reach parameters per condition or trial: least-squares coefficients of x and y hand
    position (relative to the position at -350 ms) on the two position basis functions, ordered
    (x1, y1, x2, y2) so that the third and fourth describe curvature (Methods, LDR encoding;
    'Quantifying the trial-to-trial fidelity')."""
    P = pos - pos[:, :1, :]
    G = np.linalg.pinv(Bp)  # (T, 2)
    cx = P[..., 0] @ G
    cy = P[..., 1] @ G
    return np.column_stack([cx[:, 0], cy[:, 0], cx[:, 1], cy[:, 1]])


def params_to_pos(p, Bp):
    x = p[:, [0, 2]] @ Bp
    y = p[:, [1, 3]] @ Bp
    return np.stack([x, y], -1)


def kin_ve(true, pred):
    """Variance explained in position over time (code getVarExplainedKinematics.m), x and y
    pooled, negatives set to 0. true, pred (time, 2) relative positions."""
    num = np.sum((true - pred) ** 2)
    den = np.sum((true - true.mean(0)) ** 2)
    return max(0.0, 1 - num / den)


# ---------------------------------------------------------------- regression

def ridge_fit(X, Y, lam):
    """Ridge with an unpenalised intercept."""
    mx, my = X.mean(0), Y.mean(0)
    Xc = X - mx
    W = np.linalg.solve(Xc.T @ Xc + lam * np.eye(X.shape[1]), Xc.T @ (Y - my))
    return lambda Z: (Z - mx) @ W + my


def kernel_fit(X, Y, kernel, ell, lam):
    """Kernel ridge regression with an intercept (the training mean). kernel 'ou'
    (exp(-|x-y|/ell)) or 'gauss' (exp(-|x-y|^2/(2 ell^2)))."""
    my = Y.mean(0)

    def K(A, Bm):
        d = np.sqrt(np.maximum(0, (A ** 2).sum(1)[:, None] + (Bm ** 2).sum(1)[None] - 2 * A @ Bm.T))
        return np.exp(-d / ell) if kernel == "ou" else np.exp(-d ** 2 / (2 * ell ** 2))

    Kx = K(X, X)
    alpha = np.linalg.solve(Kx + max(lam, 1e-8) * np.eye(len(X)), Y - my)
    return lambda Z: K(Z, X) @ alpha + my


def folds_of(n, k, rng):
    p = rng.permutation(n)
    return [np.sort(p[i::k]) for i in range(k)]


def auc(pos, neg):
    """ROC-AUC that pos > neg, folded to at least 0.5 (claims, shared method)."""
    from scipy.stats import mannwhitneyu
    u = mannwhitneyu(pos, neg).statistic
    a = u / (len(pos) * len(neg))
    return 0.5 + abs(a - 0.5), a


def circ_corr(a, b):
    """Circular correlation coefficient (Jammalamadaka) with a permutation-free large-sample p."""
    from scipy.stats import norm
    sa, sb = np.sin(a - np.angle(np.exp(1j * a).mean())), np.sin(b - np.angle(np.exp(1j * b).mean()))
    r = np.sum(sa * sb) / np.sqrt(np.sum(sa ** 2) * np.sum(sb ** 2))
    n = len(a)
    l20, l02, l22 = np.mean(sa ** 2), np.mean(sb ** 2), np.mean(sa ** 2 * sb ** 2)
    z = np.sqrt(n * l20 * l02 / l22) * r
    return r, 2 * (1 - norm.cdf(abs(z)))
