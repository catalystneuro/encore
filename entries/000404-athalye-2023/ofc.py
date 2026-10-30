"""Optimal feedback control simulations of Figure 6 (Methods, "Optimal feedback control model and
simulation"), on the dynamics fitted to each session of dandiset 000404.

Where the parameters come from:

- The model (Methods): neural activity x_{t+1} = A x_t + b + u_t + noise, input matrix the
  identity; cursor s_{t+1} = F s_t + K x_{t+1} with s = (position, velocity, offset); a finite-horizon
  LQR with cost on the final cursor position and velocity only and input cost R = I. The code's
  terminal weight Q_f = 100 (LQR/behavior_co_obs.py 2194-2220, cited by the claims file).
- Horizon 40 bins for center-out; for obstacle avoidance two segments of 20 bins through a
  waypoint 6 cm from the obstacle centre, rotated +-90 degrees from the centre-to-obstacle
  direction, with a desired velocity of 10 cm/s along that direction (Methods). Targets 10 cm from
  the centre at multiples of 45 degrees, obstacles halfway (Methods; "same target arrangement as
  Monkey G"). 20 trials for each of 24 conditions; initial activity the dynamics' fixed point.
- Noise: isotropic, variance the mean per-neuron variance over time and conditions of one
  noiseless No Dynamics trial per condition (Methods, "Noise").
- F and K: the decoder's cursor update estimated from the files at the 100 ms bin (bmi.py). For
  Monkey G this is the steady-state Kalman filter (exact). For Monkey J the paper builds a
  100 ms decoder from the PPF's parameters, which the files do not hold; here F and K are the
  least-squares update of the decoder state over each 100 ms bin from the state at the bin's
  start and the bin's counts (an assumption). Commands are in the decoder's units (cm/s for G;
  J's state is in m and is converted to cm).
- Activity is in spike counts per bin, the units the dynamics were fitted in.
"""

from __future__ import annotations

import numpy as np

import bmi

QF = 100.0
T_CO = 40
T_SEG = 20
WAYPOINT_CM = 6.0
WAYPOINT_SPEED = 10.0
N_TRIALS = 20
TARGET_CM = 10.0


def cursor_update(d, B, monkey):
    """F (5 x 5) and K (5 x N) of s_t = F s_{t-1} + K y_t at the 100 ms bin, by least squares over the
    bins of rewarded trials (positions and velocities in cm and cm/s)."""
    S = d["decoder_state"].astype(float)
    if monkey == "J":
        S = S.copy()
        S[:, :4] *= 100.0
        rate = 20
    else:
        rate = 6
    up = np.where(d["update_bmi"] == 1)[0] if monkey == "G" else None
    rows_prev, rows_now, rows_y = [], [], []
    Y = d["spike_counts"].astype(float)
    cs = np.vstack([np.zeros((1, Y.shape[1])), np.cumsum(Y, 0)])
    if monkey == "G":
        up = up[up >= 6]
        prev, now = S[up - 1], S[up]
        yb = cs[up + 1] - cs[up - 5]
    else:
        ends = []
        T = B["trials"]
        T = T[T.cond != "dropped"]
        for g, r in zip(T.go, T.reward):
            e = np.arange(g, r + 20, 20)
            e = e[e + 20 <= len(S)]
            ends.append(e)
        e = np.concatenate(ends)
        prev, now = S[e - 1], S[e + 19]
        yb = cs[e + 20] - cs[e]
    X = np.hstack([prev, yb])
    beta, *_ = np.linalg.lstsq(X, now[:, :4], rcond=None)
    if monkey == "G":
        for _ in range(5):
            r = np.abs(now[:, :4] - X @ beta).max(1)
            keep = r < max(1e-3 * np.abs(now[:, :4]).max(), 20 * np.median(r))
            beta, *_ = np.linalg.lstsq(X[keep], now[keep, :4], rcond=None)
    F = np.vstack([beta[:5].T, np.eye(5)[4]])
    K = np.vstack([beta[5:].T, np.zeros((1, Y.shape[1]))])
    res = now[:, :4] - X @ beta
    vaf = 1 - (res ** 2).sum(0) / ((now[:, :4] - now[:, :4].mean(0)) ** 2).sum(0)
    return F, K, vaf


def joint(A, b, F, K):
    """z = (x, s): x' = A x + b s[4] + u; s' = F s + K x'."""
    N = A.shape[0]
    M = np.zeros((N + 5, N + 5))
    M[:N, :N] = A
    M[:N, N + 4] = b
    M[N:, :N] = K @ A
    M[N:, N:] = F + np.outer(K @ b, np.eye(5)[4])
    Bu = np.vstack([np.eye(N), K])
    return M, Bu


def lqr_gains(M, Bu, target, T):
    """Finite-horizon LQR gains with terminal cost QF on the cursor position and velocity error and
    input cost I. The target enters through the offset component (error = P z - target * z_offset)."""
    n = M.shape[0]
    N = n - 5
    E = np.zeros((4, n))
    E[:, N:N + 4] = np.eye(4)
    E[:, N + 4] -= target
    V = QF * E.T @ E
    gains = []
    R = np.eye(Bu.shape[1])
    for _ in range(T):
        G = np.linalg.solve(R + Bu.T @ V @ Bu, Bu.T @ V @ M)
        V = M.T @ V @ (M - Bu @ G)
        V = 0.5 * (V + V.T)
        gains.append(G)
    return gains[::-1]


def conditions():
    """24 conditions: center-out, and obstacle avoidance clockwise and counterclockwise, 8 targets."""
    out = []
    for task in ["co", "cw", "ccw"]:
        for k in range(8):
            ang = np.radians(45 * k)
            tgt = TARGET_CM * np.array([np.cos(ang), np.sin(ang)])
            out.append((task, k, tgt))
    return out


def plan(M, Bu, task, tgt):
    """Segments of (gains, target state) for one condition."""
    if task == "co":
        return [(lqr_gains(M, Bu, np.r_[tgt, 0, 0], T_CO), np.r_[tgt, 0, 0])]
    obs = tgt / 2.0
    dvec = obs / np.linalg.norm(obs)
    rot = np.radians(-90 if task == "cw" else 90)
    Rm = np.array([[np.cos(rot), -np.sin(rot)], [np.sin(rot), np.cos(rot)]])
    wp = obs + WAYPOINT_CM * (Rm @ dvec)
    wstate = np.r_[wp, WAYPOINT_SPEED * dvec]
    return [(lqr_gains(M, Bu, wstate, T_SEG), wstate), (lqr_gains(M, Bu, np.r_[tgt, 0, 0], T_SEG), np.r_[tgt, 0, 0])]


def simulate(A, b, F, K, x0, sigma, rng, n_trials=N_TRIALS, plans=None):
    """Runs every condition. Returns per trial the input magnitude (Frobenius norm of the N x T
    inputs), and the activity, commands and labels of every bin, and the final cursor errors."""
    N = A.shape[0]
    M, Bu = joint(A, b, F, K)
    if plans is None:
        plans = [(task, k, plan(M, Bu, task, tgt)) for task, k, tgt in conditions()]
    mags, X, C, cond, binn, rev, err = [], [], [], [], [], [], []
    for task, k, segs in plans:
        for tr in range(n_trials):
            z = np.r_[x0, 0, 0, 0, 0, 1.0]
            U, xs, cs = [], [], []
            for gains, _ in segs:
                for G in gains:
                    u = -G @ z
                    xn = A @ z[:N] + b + u + (sigma * rng.standard_normal(N) if sigma > 0 else 0)
                    s = F @ z[N:] + K @ xn
                    z = np.r_[xn, s]
                    U.append(u)
                    xs.append(xn)
                    cs.append((K @ xn)[2:4])
            U = np.array(U)
            mags.append(dict(task=task, target=k, trial=tr, mag=np.linalg.norm(U)))
            X.append(np.array(xs))
            C.append(np.array(cs))
            nb = len(xs)
            cond += [f"{task}{k}"] * nb
            binn.append(np.arange(nb))
            rev.append(np.arange(nb)[::-1])
            err.append(np.linalg.norm(z[N:N + 2] - segs[-1][1][:2]))
    return dict(mags=mags, spk=np.vstack(X), cmd=np.vstack(C), cond=np.array(cond),
                bin_num=np.concatenate(binn), rev_bin_num=np.concatenate(rev), final_err=np.array(err),
                plans=plans)


def noise_sigma(A0b, F, K, x0):
    """Methods, "Noise": one noiseless No Dynamics trial per condition; sigma^2 the mean over neurons
    of each neuron's variance over time and conditions."""
    A0, b0 = A0b
    sim = simulate(A0, b0, F, K, x0, 0.0, np.random.default_rng(0), n_trials=1)
    return float(np.sqrt(sim["spk"].var(0).mean()))


def session_models(d, B, monkey):
    """The four models of Figure 6 for one session: Full Dynamics (A, b fit on all pairs with the
    session's cross-validated ridge parameter), No Dynamics (A = 0, same b), Decoder-null Dynamics
    (fit on activity projected into the decoder-null space, its own parameter) and its No Dynamics
    model (A = 0, the decoder-null offset). Each starts at its fixed point."""
    F, K, vaf = cursor_update(d, B, monkey)
    tm1, t = bmi.pairs_in_trials(B)
    fold = bmi.folds(len(t), B["task"][t], seed=0)
    X = B["spk"]
    alpha, _ = bmi.choose_alpha(X[tm1], X[t], fold)
    W, b = bmi.ridge_fit(X[tm1], X[t], alpha)
    A = W.T
    Nb = bmi.null_basis(K[2:4])
    P = Nb @ Nb.T
    Xn = X @ P
    alpha_n, _ = bmi.choose_alpha(Xn[tm1], Xn[t], fold)
    Wn, bn = bmi.ridge_fit(Xn[tm1], Xn[t], alpha_n)
    An = Wn.T
    N = A.shape[0]
    Z = np.zeros((N, N))
    models = {
        "Full Dynamics": (A, b, np.linalg.solve(np.eye(N) - A, b)),
        "No Dynamics": (Z, b, b),
        "Decoder-null Dynamics": (An, bn, np.linalg.solve(np.eye(N) - An, bn)),
        "No Dynamics (decoder-null offset)": (Z, bn, bn),
    }
    sig = noise_sigma((Z, b), F, K, b)
    sig_n = noise_sigma((Z, bn), F, K, bn)
    sigmas = {"Full Dynamics": sig, "No Dynamics": sig, "Decoder-null Dynamics": sig_n,
              "No Dynamics (decoder-null offset)": sig_n}
    return dict(F=F, K=K, vaf=vaf, Nb=Nb, alpha=alpha, alpha_null=alpha_n, models=models, sigmas=sigmas)


def run_session(d, B, monkey, seed, nshuff):
    """Simulates the four models (20 trials x 24 conditions) and, on each simulation, the distances
    of Figure 6G: tuples of 15 or more occurrences, decoder-null population distance between the
    condition's mean and the matched condition-pooled mean, and the mean of its null under the
    behavior-preserving shuffle and under subsampling of the matched pool."""
    import analyses as an
    S = session_models(d, B, monkey)
    out = dict(vaf=S["vaf"], alpha=S["alpha"], alpha_null=S["alpha_null"], sigmas=S["sigmas"], models={})
    for i, (name, (A, b, x0)) in enumerate(S["models"].items()):
        rng = np.random.default_rng([seed, 6, i])
        sim = simulate(A, b, S["F"], S["K"], x0, S["sigmas"][name], rng)
        Bs = dict(spk=sim["spk"], cmd=sim["cmd"], cond=sim["cond"], bin_num=sim["bin_num"],
                  rev_bin_num=sim["rev_bin_num"], Nb=S["Nb"])
        Bs["mags"] = bmi.mag_boundaries(Bs["cmd"])
        tups = [x for x in bmi.tuples(Bs, Bs["mags"]) if len(x["ix_pool"]) > 0]
        res = dict(mags=sim["mags"], final_err=sim["final_err"], n_tuples=len(tups))
        if tups:
            for null, sub in [("shuffle", 1), ("subsample", 2)]:
                f = an.fig3_distances(Bs, tups, S["Nb"], nshuff, np.random.default_rng([seed, 7, i, sub]), null)
                res["dist_" + null] = f["pop"]
                res["null_mean_" + null] = f["null_pop"].mean(0)
        out["models"][name] = res
    return out
