"""Belief state TD model of Starkweather, Gershman & Uchida (2018), ported to Python.

A line-by-line port of the paper's MATLAB code,
https://github.com/cstarkweather/Starkweather2018 at commit
d667730bd5e118ceb29abd5458bb4a7dfa0baed8 (trainOdor*.m, SimulateOdor*.m,
TDlearning.m, blur_matrices_inputWeberFraction.m, blur_vector.m,
Organize_for_Plotting.m and the slope fits of allSimulations_Saline_SalB.m).
MATLAB cannot be run here, so the port stands in for it; MATLAB's random
streams are replaced by numpy's, so single simulations differ from the
authors' while their distribution is the same.

Where each parameter comes from:

- Weber fraction 0.05, cue jitter 2 sub-states, gamma 0.93, learning rate 0.1,
  500 training sessions of 50 trials (10 for odors B and C, as in the code),
  awgn noise at SNR 12 dB, 50 simulations: claim fig7cd-model-intact (Methods,
  Training the belief state TD model; Figure 7 legend), and the code.
- awgn(x, 12) with its default signal power of 0 dBW adds Gaussian noise of
  variance 10^(-12/10) (MATLAB's documented default).
- The belief impairment, O(30,30,1) = 1 and O(30,30,2) = 1e-7, in the task 2
  simulations (A with omissions, B and C) only: claim
  fig7fgh-model-belief-impaired (Methods, Impairing the belief state), as
  in the code.
- Timing impairment, a Weber fraction drawn as 0.5 + rand (0.5 to 1.5) per
  simulation, or 0.56 for all: claim fig7ijk-model-timing-impaired (Methods,
  Impairing timing; Figure S7D).
- Odor names: "A100" is odor A in task 1, "A90" odor A in task 2 (10%
  omissions), "B" and "C" the task 2 odors with ISIs of 1.2 and 2.8 s.
"""

import numpy as np
from scipy.stats import norm

ITI_HAZARD = 1 / 65
GAMMA = 0.93
S = 30
ISI_GRID = np.round(np.arange(1.2, 2.81, 0.2), 1)
N_TRIALS = {"train": {"A90": 50, "A100": 50, "B": 10, "C": 10},
            "sim": {"A90": 100, "A100": 100, "B": 10, "C": 10}}


def mround(x):
    """MATLAB round: halves away from zero."""
    return np.sign(x) * np.floor(np.abs(x) + 0.5)


def isi_pdf(odor):
    if odor in ("A90", "A100"):
        p = norm.pdf(ISI_GRID, 2, 0.5)
        return p / p.sum()
    return np.eye(9)[0 if odor == "B" else 8]


def blur_vector(dist, jitter):
    pos = np.arange(1, 30)
    out = np.zeros(29)
    for i in range(len(dist)):
        k = norm.pdf(pos, i + 1, jitter)
        out += k * dist[i] / k.sum()
    return out


def blur_matrix(T, weber):
    """blur_matrices_inputWeberFraction.m: scalar timing blur of rows 1 to 29."""
    T_blur = T.copy()
    ep = 0.2 * np.arange(1, 30)
    ea, ej = ep[:, None], ep[None, :]
    with np.errstate(divide="ignore", invalid="ignore", over="ignore", under="ignore"):
        K = 1 / (ea * weber * np.sqrt(2 * np.pi)) * np.exp(-((ej - ea) ** 2) / (2 * weber**2 * ea**2))
        for i in range(29):
            p = T[i, :29]
            ts = K @ p
            T_blur[i, :29] = ts / ts.sum() * p.sum()
    return T_blur


def matrices(odor, weber, jitter, phase, impaired=0):
    """Transition matrix T_blur and observation array O, as each .m file builds them."""
    full = np.r_[np.zeros(5), isi_pdf(odor), np.zeros(15)]
    blurred = blur_vector(full, jitter)
    if not (phase == "train" and odor == "A90"):
        blurred[blurred < 0] = 0
    cdf = np.cumsum(blurred)
    with np.errstate(divide="ignore", invalid="ignore"):
        hazard = np.r_[blurred[0], blurred[1:] / (1 - cdf[:-1])]
    hazard[hazard > 1] = 1
    hazard[hazard < 0] = 0
    T = np.zeros((S, S))
    last = np.flatnonzero(hazard != 0)[-1]
    for i in range(last + 1):
        T[i, i + 1] = 1 - hazard[i]
        T[i, S - 1] = hazard[i]
    T_blur = blur_matrix(T, weber)
    T_blur[np.isnan(T_blur)] = 0
    h = ITI_HAZARD
    omissions = odor != "A100"
    T_blur[S - 1, S - 1] = (1 - h) + h * 0.1 if omissions else 1 - h
    T_blur[S - 1, 0] = h * 0.9 if omissions else h
    O = np.zeros((S, S, 3))
    O[S - 1, 0, :] = [0, 1, 0]
    if odor == "A100":
        O[S - 1, S - 1, 1] = 0
        O[S - 1, S - 1, 0] = 1
    elif phase == "train":
        O[S - 1, S - 1, 1] = h * 0.1
        O[S - 1, S - 1, 0] = 1 - h * 0.1
    else:
        O[S - 1, S - 1, 1] = h * 0.1 * (1 - impaired) + 1e-7 * impaired
        O[S - 1, S - 1, 0] = (1 - h * 0.1) * (1 - impaired) + 1 * impaired
    for i in range(S - 1):
        nz = np.flatnonzero(T_blur[i, 1:S - 1] > 1e-4)
        O[i, nz + 1, 0] = 1
    rows = S - 1 if (phase == "sim" and odor in ("A90", "A100")) else S
    O[np.flatnonzero(T_blur[:rows, S - 1] > 1e-4), S - 1, 2] = 1
    return T_blur, O


def observations(odor, jitter, phase, rng):
    """Trial sequence and observation series x (1 null, 2 odor, 3 reward)."""
    n = N_TRIALS[phase][odor]
    full = np.r_[np.zeros(5), isi_pdf(odor), np.zeros(15)]
    isis = np.flatnonzero(mround(full * n) > 0) + 1
    frac = 1.0 if odor == "A100" else 0.9
    dist = mround(full * n * frac).astype(int)
    trialtype = np.concatenate([np.full(dist[i - 1], i) for i in isis])
    n_omit = 0 if odor == "A100" else int(mround(n * 0.1))
    temp = np.r_[trialtype, np.zeros(n_omit, int)]
    isi_matrix = temp[rng.permutation(len(temp))]
    blurred = np.zeros(len(isi_matrix), int)
    x = []
    for i, isi in enumerate(isi_matrix):
        if isi > 0:
            blurred[i] = int(mround(rng.normal(isi, jitter)))
            iti = rng.geometric(ITI_HAZARD) - 1 + 10
            x += [2] + [1] * max(blurred[i] - 1, 0) + [3] + [1] * iti
        else:
            iti = rng.geometric(ITI_HAZARD) - 1 + 20
            x += [2] + [1] * 10 + [1] * iti
    x += [1] * 30
    return np.array(x), isi_matrix, blurred


def td_learning(x, T, O, w, alpha):
    """TDlearning.m. Returns the RPE series and the last stored weights (w0 of the last step)."""
    M = [T * O[:, :, k] for k in range(3)]
    b = np.ones(S) / S
    w = np.array(w, dtype=float)
    rpe = np.empty(len(x))
    w0 = w
    for t, obs in enumerate(x):
        b0 = b
        b = b0 @ M[obs - 1]
        b = b / b.sum()
        w0 = w
        d = float(obs == 3) + w @ (GAMMA * b - b0)
        w = w + alpha * d * b0
        rpe[t] = d
    return rpe, w0


def train(odor, rng, weber=0.05, jitter=2, n_sessions=500, alpha=0.1):
    """500 training sessions from zero weights (allSimulations_Saline_SalB.m, Training)."""
    T, O = matrices(odor, weber, jitter, "train")
    w = np.zeros(S)
    for _ in range(n_sessions):
        x, _, _ = observations(odor, jitter, "train", rng)
        _, w = td_learning(x, T, O, w, alpha)
    return w


def simulate(odor, w, rng, weber=0.05, jitter=2, impaired=0, alpha=0.1, snr=12):
    """One simulation (SimulateOdor*.m) and its summary (Organize_for_Plotting.m).

    Returns phasic (9 or 1 ISIs x [pre-reward, reward, reward+1]), tonic (30)
    and omission (30, cue - 5 to cue + 24 sub-states, or None).
    """
    T, O = matrices(odor, weber, jitter, "sim", impaired)
    x, isi_m, blurred = observations(odor, jitter, "sim", rng)
    rpe, _ = td_learning(x, T, O, w, alpha)
    # Organize_for_Plotting.m, in 1-based positions kept as in MATLAB
    x = np.r_[np.ones(6, int), x]
    rpe = np.r_[np.zeros(6), rpe]
    rpe = rpe + rng.standard_normal(len(rpe)) * np.sqrt(10 ** (-snr / 10))
    R = lambda a, b: rpe[a - 1:b]          # MATLAB rpe(a:b)
    cue = np.flatnonzero(x == 2) + 1        # 1-based cue positions
    omit_idx = np.flatnonzero(isi_m == 0)
    omission = None
    if len(omit_idx):
        omission = np.mean([R(cue[i] - 5, cue[i] + 24) for i in omit_idx], axis=0)
    ub = np.unique(blurred[blurred > 0])
    mn, mx = ub.min(), ub.max()
    tonic = np.zeros(30)
    bridge_mat = np.zeros((len(ub), 30))
    for k, u in enumerate(ub):
        idx = np.flatnonzero(blurred == u)
        bridge = np.zeros(30)
        for j in idx:
            c = cue[j]
            tonic[:mn + 5] += R(c - 5, c + mn - 1)
            tonic[mx + 5:] += R(c + mx + 1, c + 25)
            tb = R(c + mn, c + u - 1)
            bridge[:len(tb)] += tb
        bridge_mat[k] = bridge / len(idx)
    with np.errstate(invalid="ignore"):
        final_bridge = bridge_mat.sum(0) / (bridge_mat != 0).sum(0)
    final_bridge = final_bridge[~np.isnan(final_bridge)]
    n_rew = np.count_nonzero(blurred)
    tonic[:mn + 5] /= n_rew
    tonic[mn + 5:mx + 5] = final_bridge
    tonic[mx + 5:] /= n_rew
    phasic = []
    for u in np.unique(isi_m[isi_m > 0]):
        idx = np.flatnonzero(isi_m == u)
        ro = cue[idx] + blurred[idx]
        phasic.append([tonic[u + 4], rpe[ro - 1].mean(), rpe[ro].mean()])
    return np.array(phasic), tonic, omission


def run(weights, rng, n_sim=50, weber=lambda rng: 0.05, impaired=None):
    """n_sim simulations of every odor; impaired is a 0/1 array over simulations (task 2 only)."""
    if impaired is None:
        impaired = np.zeros(n_sim, int)
    out = {k: [] for k in ("A100", "A90", "B", "C")}
    for s in range(n_sim):
        wf = weber(rng)
        out["A100"].append(simulate("A100", weights["A100"], rng, weber=wf, impaired=impaired[s]))
        out["A90"].append(simulate("A90", weights["A90"], rng, weber=wf, impaired=impaired[s]))
        out["C"].append(simulate("C", weights["C"], rng, weber=wf, impaired=impaired[s]))
        out["B"].append(simulate("B", weights["B"], rng, weber=wf, impaired=impaired[s]))
    return out


def summarize(out):
    """Slopes and omission traces as allSimulations_Saline_SalB.m plots them."""
    ph = {k: np.array([o[0] for o in v]) for k, v in out.items()}   # sims x ISIs x 3
    fit = lambda y: np.polyfit(ISI_GRID, y, 1)[0]
    res = dict(
        post_slope_avg_t1=fit(ph["A100"][:, :, 1].mean(0)),
        post_slope_avg_t2=fit(ph["A90"][:, :, 1].mean(0)),
        pre_slope_avg_t1=fit(ph["A100"][:, :, 0].mean(0)),
        pre_slope_avg_t2=fit(ph["A90"][:, :, 0].mean(0)),
        sim_slopes_t1=np.array([fit(p[:, 1]) for p in ph["A100"]]),
        sim_slopes_t2=np.array([fit(p[:, 1]) for p in ph["A90"]]),
        post_avg_t1=ph["A100"][:, :, 1].mean(0), post_avg_t2=ph["A90"][:, :, 1].mean(0),
        pre_avg_t1=ph["A100"][:, :, 0].mean(0), pre_avg_t2=ph["A90"][:, :, 0].mean(0),
        omission_B=np.mean([o[2] for o in out["B"]], axis=0),
        omission_C=np.mean([o[2] for o in out["C"]], axis=0),
    )
    return res


def omission_window(trace, isi_substates):
    """Mean of an omission trace over the 5 sub-states (1 s) from the usual reward time.

    The trace starts at cue - 5, so the usual reward time (cue + ISI) is at
    0-based position ISI + 5. The 1 s span follows the Methods' omission window,
    0-1000 ms after the usual reward time.
    """
    i = isi_substates + 5
    return trace[i:i + 5].mean(), trace[i:i + 5].min()
