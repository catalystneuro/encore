"""Loading and jPCA measures for Churchland et al. (2012) on dandiset 000070.

Sources of the parameters (paper = doi:10.1038/nature11129, text under paper/;
claims = claims/churchland-2012.yaml; codepack = the jPCA code the claims file
cites, bantin/jPCA at commit 3f8be9f, a port of the authors' MATLAB codepack):

- Trial selection: successful trials (`task_success`), consistent reaches
  (`correct_reach`), delay above 400 ms, conditions 1 to 108 (claims, header;
  Methods, "Only trials with delays >400 ms were analyzed"). Trials flagged
  `discard_trial` are also left out, as the file's own description of that
  column says to do (standard choice; no trial of the two main sessions is
  flagged).
- Rates: condition averages of the trials' spikes, aligned on movement onset,
  smoothed with a Gaussian of 20 ms SD (claims, header; Methods, "filtering
  with a Gaussian (20 or 24 ms depending on the dataset)"). The movement onset
  column is open: `offline_move_onset_time` ("calculated offline using a
  robust algorithm") is the main reading and `move_begins_time` the other.
- Soft normalisation by range + 5 spikes/s, cross-condition mean subtracted,
  PCA and jPCA on -50 to +150 ms every 10 ms, 6 PCs, derivative as the
  difference of adjacent samples, R2 as one minus residual over total sum of
  squares (claims, header; Methods, "Projections that capture rotational
  structure"). The window over which the range is taken is open: the codepack
  takes it over all the times it is given; here the main reading takes it over
  the analysed window and the other over -1000 to +700 ms.
- Plane orientation: jPC1 along the largest spread of the states at the first
  analysed time, and jPC2 so that the plane's fitted rotation is
  counter-clockwise (Methods: "selected jPC1 and jPC2 so that any net rotation
  was counter-clockwise ... and so that the spread of preparatory states was
  strongest along jPC1").
- Shuffles: supplementary figure 2 legend (dividing point 50 ms after the go
  cue; inversion around the dividing point per neuron; reassignment of
  peri-movement activity, the same for all neurons, appended to the final
  preparatory rate).
- Simulated populations: Methods, "Simulated neural data". How far the rates
  lead the hand, the time course of the preparatory term and the relative
  weights of the factors are not given; they are assumptions, stated in
  `simulate_population`.
- Spikes are binned at 1 ms (a standard choice that cannot change a result at
  the 10 ms sampling used).
"""
import numpy as np
import h5py
import remfile
import requests
import pandas as pd

DANDISET = "000070"
VERSION = "0.261122.2046"
API = "https://api.dandiarchive.org/api"

SESSIONS = {
    "J-array": "sub-Jenkins/sub-Jenkins_ses-20090918_behavior+ecephys.nwb",
    "N-array": "sub-Nitschke/sub-Nitschke_ses-20100923_behavior+ecephys.nwb",
    "N-9-10-2010": "sub-Nitschke/sub-Nitschke_ses-20100910_behavior+ecephys.nwb",
}

# Rates are kept from T0 to T1 ms around movement onset, at 1 ms.
T0, T1 = -1000, 700
PAD = 100            # ms of spikes kept on each side for smoothing
SMOOTH_SD = 20.0     # ms (claims, header)
ANALYSIS = (-50, 150, 10)   # ms: start, stop (inclusive), step (claims, header)
SOFT_NORM = 5.0      # spikes/s (claims, header)


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    return sorted(out, key=lambda a: a["path"])


def version_metadata():
    return requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60).json()


def open_asset(path):
    """Stream one NWB file of the pinned version (no download to disk)."""
    assets = {a["path"]: a for a in list_assets()}
    aid = assets[path]["asset_id"]
    s3 = requests.head(f"{API}/assets/{aid}/download/", allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(s3), "r")


TRIAL_COLS = ["start_time", "stop_time", "target_presentation_time", "go_cue_time",
              "move_begins_time", "offline_move_onset_time", "move_ends_time",
              "task_success", "correct_reach", "discard_trial", "maze_condition",
              "trial_version", "maze_num_targets", "maze_num_barriers"]


def load_trials(f):
    tr = f["intervals/trials"]
    d = pd.DataFrame({c: tr[c][:] for c in TRIAL_COLS if c in tr})
    d["hit_x"], d["hit_y"] = tr["hit_target_position"][:].T
    d["cursor_dx"], d["cursor_dy"] = tr["cursor_offset"][:].T
    d["delay"] = d.go_cue_time - d.target_presentation_time
    return d


def select_trials(d):
    """The Methods' selection (see module docstring)."""
    return ((d.task_success == 1) & (d.correct_reach == 1) & (d.discard_trial == 0)
            & (d.delay > 0.4) & (d.maze_condition >= 1) & (d.maze_condition <= 108))


def unit_groups(f):
    """Electrode group name of each unit ('1' PMd, '2' M1 in these files)."""
    return np.array([f[r].name.split("/")[-1] for r in f["units/electrode_group"][:]])


def load_rates(f, trials, onset_cols=("offline_move_onset_time", "move_begins_time"),
               target_bins=(-500, 500, 50), move_bins=(-1000, 700, 50), n_blocks=6):
    """Condition-mean spike counts at 1 ms, aligned on each movement onset column.

    Returns a dict with, per onset column, `sum` (units x conditions x ms) of
    spike counts summed over trials, `n` trials per condition, and per-trial
    counts in 50 ms bins aligned on target onset and on movement onset (for
    the clock check), and `block_sum`: counts aligned on the first onset column
    summed over the trials of each of `n_blocks` consecutive blocks of the
    session (units x blocks x ms), to look for a drift between arrays. Spikes
    are read one unit at a time.
    """
    si = f["units/spike_times_index"][:]
    st = f["units/spike_times"]
    nu = len(si)
    conds = trials.maze_condition.values.astype(int)
    cidx = conds - 1
    ncond = 108
    nbin = (T1 - T0) + 2 * PAD
    out = {"units_unsorted": 0, "outside_trial": {}}
    for col in onset_cols:
        out[col] = {"sum": np.zeros((nu, ncond, nbin), np.float32),
                    "n": np.bincount(cidx, minlength=ncond)}
    tb = np.arange(*target_bins) / 1000.0
    mb = np.arange(*move_bins) / 1000.0
    tgt = trials.target_presentation_time.values
    mov = trials.offline_move_onset_time.values
    block = np.minimum((np.arange(len(trials)) * n_blocks) // len(trials), n_blocks - 1)
    out["block"] = block
    out["block_sum"] = np.zeros((nu, n_blocks, nbin), np.float32)
    out["target_counts"] = np.zeros((len(trials), nu, len(tb)), np.uint16)
    out["move_counts"] = np.zeros((len(trials), nu, len(mb)), np.uint16)
    for col in onset_cols:
        a = trials[col].values
        lo = a + (T0 - PAD) / 1000.0
        hi = a + (T1 + PAD) / 1000.0
        out["outside_trial"][col] = int(np.sum((lo < trials.start_time.values) | (hi > trials.stop_time.values)))
    start = 0
    for u in range(nu):
        s = st[start:si[u]]
        start = si[u]
        if np.any(np.diff(s) < 0):
            out["units_unsorted"] += 1
            s = np.sort(s)
        for col in onset_cols:
            a = trials[col].values
            lo = np.searchsorted(s, a + (T0 - PAD) / 1000.0)
            hi = np.searchsorted(s, a + (T1 + PAD) / 1000.0)
            cnt = hi - lo
            if cnt.sum() == 0:
                continue
            tri = np.repeat(np.arange(len(a)), cnt)
            idx = np.concatenate([np.arange(l, h) for l, h in zip(lo, hi)])
            b = np.floor((s[idx] - a[tri]) * 1000.0 - (T0 - PAD)).astype(int)
            b = np.clip(b, 0, nbin - 1)
            np.add.at(out[col]["sum"][u], (cidx[tri], b), 1)
            if col == onset_cols[0]:
                np.add.at(out["block_sum"][u], (block[tri], b), 1)
        for key, ref, edges in (("target_counts", tgt, tb), ("move_counts", mov, mb)):
            w = edges[1] - edges[0]
            l = np.searchsorted(s, ref + edges[0])
            h = np.searchsorted(s, ref + edges[-1] + w)
            cnt = h - l
            tri = np.repeat(np.arange(len(ref)), cnt)
            idx = np.concatenate([np.arange(x, y) for x, y in zip(l, h)]) if cnt.sum() else np.array([], int)
            b = np.floor((s[idx] - ref[tri] - edges[0]) / w + 1e-9).astype(int)
            ok = (b >= 0) & (b < len(edges))
            np.add.at(out[key][:, u, :], (tri[ok], b[ok]), 1)
    out["target_edges"] = tb
    out["move_edges"] = mb
    return out


def smooth_rates(sum_counts, n, sd=SMOOTH_SD):
    """Gaussian-smoothed condition-mean rates (spikes/s) from T0 to T1 at 1 ms."""
    from scipy.ndimage import gaussian_filter1d
    mean = sum_counts / np.maximum(n, 1)[None, :, None] * 1000.0
    sm = gaussian_filter1d(mean, sd, axis=2, mode="nearest")
    return sm[:, :, PAD:PAD + (T1 - T0)]


def ms_index(t_ms):
    return np.asarray(t_ms) - T0


def load_hand(f, trials, col="offline_move_onset_time", t0=-200, t1=700):
    """Hand position (mm) from t0 to t1 ms around movement onset, per trial, at 1 ms."""
    ts = f["processing/behavior/Position/Hand/timestamps"][:]
    a = trials[col].values
    lo = np.searchsorted(ts, a + t0 / 1000.0 - 0.005)
    hi = np.searchsorted(ts, a + t1 / 1000.0 + 0.005)
    grid = np.arange(t0, t1) / 1000.0
    out = np.full((len(a), len(grid), 2), np.nan)
    hd = f["processing/behavior/Position/Hand/data"]
    for i in range(len(a)):
        if hi[i] - lo[i] < 10:
            continue
        x = hd[lo[i]:hi[i]]
        tt = ts[lo[i]:hi[i]] - a[i]
        for k in range(2):
            out[i, :, k] = np.interp(grid, tt, x[:, k], left=np.nan, right=np.nan)
    return out, np.arange(t0, t1)


# ----------------------------------------------------------------------------
# jPCA

def analysis_times():
    s, e, d = ANALYSIS
    return np.arange(s, e + 1, d)


def preprocess(rates, norm_window=None, times=None):
    """Soft-normalise, subtract the cross-condition mean, cut the analysed times.

    rates: units x conditions x ms (T0..T1). norm_window: (start, stop) in ms for
    the firing-rate range; None for the analysed window. Returns units x
    conditions x analysed times.
    """
    times = analysis_times() if times is None else times
    if norm_window is None:
        rng_src = rates[:, :, ms_index(times)]
    else:
        rng_src = rates[:, :, ms_index(norm_window[0]):ms_index(norm_window[1])]
    rng = rng_src.max(axis=(1, 2)) - rng_src.min(axis=(1, 2))
    r = rates / (rng + SOFT_NORM)[:, None, None]
    r = r - r.mean(axis=1, keepdims=True)
    return r[:, :, ms_index(times)]


def pca(X, k):
    """X: units x conditions x times. Returns scores (k x c x t), loadings, total variance."""
    n, c, t = X.shape
    A = X.reshape(n, c * t).T
    A = A - A.mean(axis=0)
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    var = S ** 2 / (A.shape[0] - 1)
    total = var.sum()
    scores = (A @ Vt[:k].T).T.reshape(k, c, t)
    return scores, Vt[:k], var, total


def state_and_derivative(Z):
    """Z: k x c x t. Returns states (k x N) without each condition's last time, and differences."""
    k = Z.shape[0]
    Xs = Z[:, :, :-1].reshape(k, -1)
    dX = np.diff(Z, axis=2).reshape(k, -1)
    return Xs, dX


def fit_M(X, dX):
    M, *_ = np.linalg.lstsq(X.T, dX.T, rcond=None)
    return M.T


def fit_Mskew(X, dX):
    k = X.shape[0]
    pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
    N = X.shape[1]
    H = np.zeros((k * N, len(pairs)))
    for p, (i, j) in enumerate(pairs):
        # M[i, j] = +m, M[j, i] = -m ; dX[i] += m X[j], dX[j] -= m X[i]
        H[i * N:(i + 1) * N, p] = X[j]
        H[j * N:(j + 1) * N, p] = -X[i]
    m, *_ = np.linalg.lstsq(H, dX.reshape(-1), rcond=None)
    M = np.zeros((k, k))
    for p, (i, j) in enumerate(pairs):
        M[i, j] = m[p]
        M[j, i] = -m[p]
    return M


def r2(M, X, dX):
    res = dX - M @ X
    tot = dX - dX.mean(axis=1, keepdims=True)
    return 1.0 - np.sum(res ** 2) / np.sum(tot ** 2)


def jpca(X, k=6, n_planes=1):
    """jPCA as in the Methods. X: units x conditions x analysed times (preprocessed).

    Returns a dict: planes (list of 2 x c x t projections), the planes' basis in
    PC space, the variance each plane captures (fraction of total), the PCs'
    variance fractions, M, M_skew, R2 values, and eigenvalues of M_skew.
    """
    scores, load, var, total = pca(X, k)
    Xs, dX = state_and_derivative(scores)
    M = fit_M(Xs, dX)
    Mk = fit_Mskew(Xs, dX)
    ev, V = np.linalg.eig(Mk)
    order = np.argsort(-np.abs(ev.imag) - 1e-9 * ev.imag)   # +i w before -i w
    planes, bases, pvar, freqs = [], [], [], []
    used = []
    for idx in order:
        if len(planes) >= n_planes:
            break
        if any(np.isclose(ev[idx], np.conj(ev[u])) or np.isclose(ev[idx], ev[u]) for u in used):
            continue
        used.append(idx)
        v1 = V[:, idx]
        v2 = np.conj(v1)
        if np.sign(v1.real.sum()) != np.sign(v2.real.sum()):
            v2 = -v2
        j1 = (v1 + v2).real
        j2 = (1j * (v1 - v2)).real
        j1 /= np.linalg.norm(j1)
        j2 -= j1 * (j1 @ j2)
        j2 /= np.linalg.norm(j2)
        P = np.stack([j1, j2])                      # 2 x k
        Z = np.tensordot(P, scores, axes=(1, 0))    # 2 x c x t
        # jPC1 along the largest spread of the first-time states
        z0 = Z[:, :, 0] - Z[:, :, 0].mean(axis=1, keepdims=True)
        w, U = np.linalg.eigh(z0 @ z0.T)
        u = U[:, np.argmax(w)]
        th = np.arctan2(u[1], u[0])
        R = np.array([[np.cos(th), np.sin(th)], [-np.sin(th), np.cos(th)]])
        P = R @ P
        # counter-clockwise: the plane's skew dynamics dx2/dt = +w x1
        if (P @ Mk @ P.T)[1, 0] < 0:
            P[1] = -P[1]
        Z = np.tensordot(P, scores, axes=(1, 0))
        planes.append(Z)
        bases.append(P)
        pvar.append(np.sum(np.var(Z.reshape(2, -1), axis=1, ddof=1)) / total)
        freqs.append(abs(ev[idx].imag))
    out = {"planes": planes, "bases": bases, "plane_var": np.array(pvar),
           "pc_var": var[:k] / total, "pc_var_all": var / total, "M": M, "Mskew": Mk,
           "R2_M": r2(M, Xs, dX), "R2_skew": r2(Mk, Xs, dX), "eig": ev, "scores": scores,
           "plane_eig": np.array(freqs)}
    # fits within the first plane
    Z = planes[0]
    Xp, dXp = state_and_derivative(Z)
    out["R2_M_plane"] = r2(fit_M(Xp, dXp), Xp, dXp)
    out["R2_skew_plane"] = r2(fit_Mskew(Xp, dXp), Xp, dXp)
    return out


def freq_hz(eig_mag, step_ms=ANALYSIS[2]):
    """Eigenvalue magnitude per sample to rad/s and Hz."""
    rad_s = eig_mag * 1000.0 / step_ms
    return rad_s, rad_s / (2 * np.pi)


def net_rotation(Z):
    """Net change of polar angle (rad) of each condition's state across the window."""
    ang = np.unwrap(np.arctan2(Z[1], Z[0]), axis=1)
    return ang[:, -1] - ang[:, 0]


def state_derivative_angles(Z):
    X, dX = state_and_derivative(Z)
    return np.arctan2(X[0] * dX[1] - X[1] * dX[0], X[0] * dX[0] + X[1] * dX[1])


def angle_peak(angles, bins=36):
    h, e = np.histogram(angles, bins=bins, range=(-np.pi, np.pi))
    c = (e[:-1] + e[1:]) / 2
    return c[np.argmax(h)], h, e


# ----------------------------------------------------------------------------
# Shuffle controls (supplementary figure 2 legend)

def shuffle_invert(rates, div_ms, conds_mask):
    """Invert the peri-movement pattern around the dividing point.

    rates: units x conditions x ms; conds_mask: units x conditions boolean, the
    (unit, condition) pairs to invert (per neuron for shuffle 1, all for 2).
    """
    i = ms_index(div_ms)
    r = rates.copy()
    ref = r[:, :, i:i + 1]
    inv = 2 * ref - r[:, :, i:]
    r[:, :, i:] = np.where(conds_mask[:, :, None], inv, r[:, :, i:])
    return r


def shuffle_reassign(rates, div_ms, perm):
    """Give condition c the peri-movement activity of condition perm[c], appended
    to c's final preparatory rate; the same for all neurons."""
    i = ms_index(div_ms)
    r = rates.copy()
    mov = rates[:, perm, i:] - rates[:, perm, i:i + 1]
    r[:, :, i:] = rates[:, :, i:i + 1] + mov
    return r


# ----------------------------------------------------------------------------
# Simulated populations (Methods, "Simulated neural data")

def kinematics(hand_mean, t_ms, sd=20.0):
    """Position (m), velocity, acceleration and jerk of condition-mean hand paths.

    hand_mean: conditions x ms x 2 in mm. The path is smoothed with a Gaussian of
    20 ms SD before differentiating (standard choice).
    """
    from scipy.ndimage import gaussian_filter1d
    p = gaussian_filter1d(hand_mean / 1000.0, sd, axis=1, mode="nearest")
    p = p - p[:, :1, :]
    v = np.gradient(p, axis=1) * 1000.0
    a = np.gradient(v, axis=1) * 1000.0
    j = np.gradient(a, axis=1) * 1000.0
    return p, v, a, j


def simulate_population(model, kin, t_kin, rates, n_trials, rng, lag_ms=100,
                        prep="switch"):
    """Simulated spikes for a velocity or complex kinematic population.

    Assumptions (the Methods do not give them): the movement term leads the
    hand by `lag_ms` (100 ms; 0 is the other reading), the preparatory term
    holds before movement and falls linearly to zero from -50 to +50 ms around
    movement onset (`prep="switch"`; `"persist"`, the other reading, keeps it
    throughout), and the movement term is added to it; before movement the hand
    kinematics are those at its start. Preferred directions are drawn
    uniformly for the preparatory and the movement terms (Methods). Velocity
    model: movement term = velocity along the PD + speed, each factor scaled to
    unit SD over conditions and times and weighted by a uniform draw on 0 to 1;
    preparatory term = endpoint along the preparatory PD + peak speed, likewise.
    Complex kinematic model: the Methods' sensitivities (25, 10, 1, 0.05
    spikes/s per m, m/s, m/s^2, m/s^3) on position, velocity, acceleration and
    jerk along the PD; preparatory term 25 spikes/s per m of endpoint along the
    preparatory PD. Each unit's noiseless rate is then scaled to the recorded
    unit's mean and range over T0..T1 (Methods: "matched the overall firing
    rates ... of each simulated unit to those of the respective recorded
    neuron"), rectified, and spikes are drawn from a gamma-interval process of
    order 2 (Methods) for the recorded number of trials of each condition.

    kin: (p, v, a, j), each conditions x len(t_kin) x 2, t_kin in ms.
    rates: recorded units x conditions x ms (T0..T1). Returns summed spike counts
    (units x conditions x ms, padded as load_rates) for smooth_rates.
    """
    p, v, a, j = kin
    nu, nc, _ = rates.shape
    t = np.arange(T0 - PAD, T1 + PAD)
    # kinematics at time t + lag, held at the ends
    tk = np.clip(t + lag_ms, t_kin[0], t_kin[-1]) - t_kin[0]
    P, Vv, A, J = (x[:, tk, :] for x in (p, v, a, j))
    endpoint = p[:, -1, :]
    speed = np.linalg.norm(Vv, axis=2)
    peak_speed = np.linalg.norm(v, axis=2).max(axis=1)
    if prep == "switch":
        w_prep = np.clip(0.5 - t / 100.0, 0, 1)
    elif prep == "persist":
        w_prep = np.ones(len(t))
    else:
        raise ValueError(prep)
    th_m = rng.uniform(0, 2 * np.pi, nu)
    th_p = rng.uniform(0, 2 * np.pi, nu)
    um = np.stack([np.cos(th_m), np.sin(th_m)], 1)
    up = np.stack([np.cos(th_p), np.sin(th_p)], 1)
    rec_mean = rates.mean(axis=(1, 2))
    rec_rng = rates.max(axis=(1, 2)) - rates.min(axis=(1, 2))
    if model == "velocity":
        wv, ws, we, wps = rng.uniform(0, 1, (4, nu))
        sv = Vv.std()
        ss = speed.std()
        se = endpoint.std()
        sps = peak_speed.std()
    out = np.zeros((nu, nc, len(t)), np.float32)
    for u in range(nu):
        if model == "velocity":
            mov = wv[u] * (Vv @ um[u]) / sv + ws[u] * speed / ss
            pr = we[u] * (endpoint @ up[u]) / se + wps[u] * peak_speed / sps
        elif model == "complex":
            mov = 25 * (P @ um[u]) + 10 * (Vv @ um[u]) + 1 * (A @ um[u]) + 0.05 * (J @ um[u])
            pr = 25 * (endpoint @ up[u])
        else:
            raise ValueError(model)
        r = mov + pr[:, None] * w_prep[None, :]
        core = r[:, PAD:PAD + (T1 - T0)]
        rr = core.max() - core.min()
        r = (r - core.mean()) / (rr if rr > 0 else 1) * rec_rng[u] + rec_mean[u]
        r = np.clip(r, 0, None)
        out[u] = gamma_spikes(r, n_trials, rng)
    return out


def gamma_spikes(r, n_trials, rng, order=2):
    """Summed spike counts (conditions x ms) of a gamma-interval process.

    r: conditions x ms (spikes/s); n_trials: trials per condition. Spikes are
    drawn by time rescaling: intervals Gamma(order, 1/order) in units of the
    integrated rate, with a random phase at the start.
    """
    nc, nt = r.shape
    lam = np.cumsum(r, axis=1) / 1000.0
    out = np.zeros((nc, nt), np.float32)
    for c in range(nc):
        n = int(n_trials[c])
        if n == 0:
            continue
        L = lam[c, -1]
        m = int(L + 6 * np.sqrt(L + 1) + 10)
        isi = rng.gamma(order, 1.0 / order, size=(n, m))
        isi[:, 0] *= rng.uniform(0, 1, n)
        cs = np.cumsum(isi, axis=1)
        cs = cs[cs < L]
        b = np.searchsorted(lam[c], cs)
        out[c] = np.bincount(b, minlength=nt)[:nt]
    return out


# ----------------------------------------------------------------------------
# Checks of the data

def reach_direction_class(trials, n=8):
    """Sector (of n) of the direction of the hit target from the screen centre."""
    ang = np.arctan2(trials.hit_y.values, trials.hit_x.values)
    return np.floor((ang + np.pi) / (2 * np.pi / n)).astype(int) % n


def decode_accuracy(counts, labels, rng, folds=5):
    """Cross-validated nearest-centroid decoding (standard choice).

    counts: trials x features. Features are z-scored on the training trials.
    """
    n = len(labels)
    order = rng.permutation(n)
    fold = np.empty(n, int)
    fold[order] = np.arange(n) % folds
    correct = 0
    classes = np.unique(labels)
    for k in range(folds):
        tr, te = fold != k, fold == k
        mu = counts[tr].mean(0)
        sd = counts[tr].std(0) + 1e-6
        Xtr = (counts[tr] - mu) / sd
        Xte = (counts[te] - mu) / sd
        cen = np.stack([Xtr[labels[tr] == c].mean(0) for c in classes])
        d = ((Xte[:, None, :] - cen[None]) ** 2).sum(-1)
        correct += np.sum(classes[np.argmin(d, 1)] == labels[te])
    return correct / n
