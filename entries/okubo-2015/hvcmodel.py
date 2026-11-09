"""Python port of the HVC network model of Okubo, Mackevicius, Payne, Lynch & Fee 2015 (Nature 528,
352-357, doi:10.1038/nature15741), from the MATLAB Supplementary Information code
(`paper/10.1038-nature15741.code.m`, "HVCModelCode") and the Methods section "Neural model of chain
formation and splitting" (`paper/10.1038-nature15741.txt`).

Line numbers "code L.." refer to the MATLAB file. "Methods" quotes refer to the paper text.

Random numbers. MATLAB's `rng(seed)` Mersenne Twister stream cannot be reproduced here, so every
run uses `numpy.random.default_rng(seed)` with the same seed numbers (9038, 1009). The order in which
random numbers are drawn follows the MATLAB code (including re-seeding before the initial weights,
code L73 and L97, and column-major filling of matrices), but the numbers themselves differ, so no
run is bit-identical to the published figures.

Index conventions. Neuron indices in the returned arrays are 0-based (MATLAB neuron 1 is row 0).
Time indices of syllable onsets (`tind`) and candidate latencies (`cand_lat`) are kept 1-based exactly
as in the MATLAB code, so that `find_latency` reproduces code L592-594 literally; the conversion to
0-based array positions happens only inside `find_latency`.
"""
from __future__ import annotations

import numpy as np

# ---------------------------------------------------------------- fixed network constants
N = 100            # code L28 / L286, "A network of 100 binary neurons" (Methods)
TRAININT = 10      # code L29 / L287, time steps between seed inputs (T = 100 ms, Methods)
STEP_MS = 10       # Methods, "at each time step (10 ms)"
TAU = 4            # code L41 / L298, tau_adapt = 40 ms (Methods)
ALPHA = 30         # code L38 / L295, alpha = 30 (Methods)
PIN = 0.01         # code L33 / L290, "random inputs with probability pin = 0.01" (Methods)
HOW_CLAMPED = 10   # code L53 / L310, theta_i = 10 for seed neurons (Methods)
SIG_TAU = 200      # code L66 / L327 sigmf slope 1/200, "time constant tau_gamma = 200 iterations"
GAMMA_START = 0.01  # code L42 / L299, "gamma was increased from 0.01" (Methods)
WMAX_START = 1     # code L45 / L302, "wmax was increased from 1 to 2" (Methods)
WMAX_SPLIT = 2     # code L46 / L303


def sigmf(x, a, c):
    """MATLAB sigmf(x, [a c]) = 1 / (1 + exp(-a (x - c))) (used at code L66 and L327)."""
    return 1.0 / (1.0 + np.exp(-a * (np.asarray(x, float) - c)))


# ---------------------------------------------------------------- HVCIter (code L512-572)
def hvc_iter(w, inp, *, gamma, wmax, m, beta, eta, epsilon, alpha=ALPHA, tau=TAU):
    """One iteration of the network (code L512-572). `w[i, j]` is the weight from j to i;
    `inp` is the (n, nsteps) external input `bdyn`. Returns (new w, boolean activity xdyn).

    The arithmetic is that of the MATLAB code; it is only rearranged for speed: the excitatory
    input w*oldx is summed over active columns, and the row/column sums of w + dw_STDP needed by the
    heterosynaptic penalty are computed from w's sums plus the closed-form sums of the STDP term,
    and the (sparse) STDP term is then added only at the active rows/columns. The result equals
    the dense formula up to floating-point rounding order."""
    n, nsteps = inp.shape
    w = np.array(w, dtype=float, copy=True)
    Wmax = wmax * m                                  # code L521
    xdyn = np.zeros((n, nsteps), dtype=bool)
    oldx = np.zeros(n)
    oldy = np.zeros(n)
    diag = np.arange(n)
    learn = eta > 0                                  # code L560
    for t in range(nsteps):
        y = oldy + (1.0 / tau) * (-oldy + oldx)      # code L532
        act = np.flatnonzero(oldx)
        AE = w[:, act].sum(axis=1) if act.size else np.zeros(n)   # code L537, w*oldx
        Anet = AE - beta * act.size - alpha * y + inp[:, t]          # code L533-539
        Anet[Anet < 0] = 0                                           # code L540
        AIrec = gamma * Anet.sum()                                   # code L543
        x = (Anet - AIrec) > 0                                       # code L546
        if learn:
            xf = x.astype(float)
            sx, so = xf.sum(), act.size
            # sums of w + dw_STDP, dw_STDP = eta (x oldx' - oldx x')        code L549
            colsum = w.sum(axis=0) + eta * (sx * oldx - xf * so)    # sum(.,1), per presynaptic j
            rowsum = w.sum(axis=1) + eta * (xf * so - oldx * sx)    # sum(.,2), per postsynaptic i
            pre = eta * np.maximum(0.0, colsum - Wmax)               # code L552-553
            post = eta * np.maximum(0.0, rowsum - Wmax)              # code L555-556
            w -= epsilon * (pre[None, :] + post[:, None])            # code L561-562
            xi = np.flatnonzero(x)
            if xi.size and act.size:
                w[np.ix_(xi, act)] += eta
                w[np.ix_(act, xi)] -= eta
            np.clip(w, 0.0, wmax, out=w)                             # code L563-564
            w[diag, diag] = 0.0                                      # code L565
        oldx = xf if learn else x.astype(float)                      # code L568
        oldy = y                                                     # code L569
        xdyn[:, t] = x                                               # code L570
    return w, xdyn


def _rand(rng, rows, cols):
    """MATLAB rand(rows, cols): fills column-major, so draw in that order."""
    return rng.random(rows * cols).reshape((rows, cols), order="F")


# ---------------------------------------------------------------- alternating / motif
def _run_seeded_rhythm(seed, *, k, n_groups, m_start, m_split, beta, eta, epsilon,
                       gamma_split, t0, n_proto, n_split, snap_split, nsteps,
                       nsteps_subsong, how_on):
    """Subsong, protosyllable and splitting stages of code L23-141, with `k` seed neurons split into
    `n_groups` groups for splitting (2 groups: code L89-91)."""
    seeds = np.arange(k)
    Wmax = m_start * WMAX_START                                       # code L50
    gammas = np.r_[np.full(n_proto, GAMMA_START),
                   gamma_split * sigmf(np.arange(1, n_split + 1), 1 / SIG_TAU, t0)]  # code L65-66
    wmaxs = np.r_[np.full(n_proto, WMAX_START), np.full(n_split, WMAX_SPLIT)]  # code L67-68
    ms = np.r_[np.full(n_proto, m_start), np.full(n_split, m_split)]             # code L69-70
    proto = np.r_[np.ones(n_proto, bool), np.zeros(n_split, bool)]               # code L63

    # subsong inputs, code L73-80
    rng = np.random.default_rng(seed)
    is_onset = rng.random(nsteps_subsong) > 0.9
    sub_in = (_rand(rng, N, nsteps_subsong) >= (1 - PIN)).astype(float)
    sub_in[:k, :] = -HOW_CLAMPED
    sub_in[:k, is_onset] = how_on

    steps = np.arange(1, nsteps + 1)
    psyl_in = np.full((k, nsteps), -float(HOW_CLAMPED))              # code L83-85
    psyl_in[:, steps % TRAININT == 1] = how_on
    groups = np.array_split(seeds, n_groups)
    alt_in = np.full((k, nsteps), -float(HOW_CLAMPED))               # code L89-91
    for g, ids in enumerate(groups):
        alt_in[np.ix_(ids, np.flatnonzero(steps % (n_groups * TRAININT) == g * TRAININT + 1))] = how_on

    # initial weights after re-seeding, code L97-98
    rng = np.random.default_rng(seed)
    w0 = 2 * _rand(rng, N, N) * Wmax / N

    w_sub, x_sub = hvc_iter(w0, sub_in, gamma=gammas[0], wmax=wmaxs[0], m=ms[0], beta=beta,
                            eta=0.0, epsilon=0.0)                    # code L101-112
    snaps = {"subsong": dict(w=w_sub, xdyn=x_sub, input=sub_in, is_onset=is_onset,
                             types=[dict(nids=seeds, tind=np.flatnonzero(is_onset) + 1,
                                         cand_lat=np.arange(1, 2 * TRAININT + 1),
                                         thres=12)])}               # code L184-187
    proto_types = [dict(nids=seeds, tind=np.flatnonzero(steps % TRAININT == 1) + 1,
                        cand_lat=np.arange(1, TRAININT + 1), thres=4)  # code L199-211
                   for _ in range(max(2, n_groups))]
    split_types = [dict(nids=ids, tind=np.flatnonzero(steps % (n_groups * TRAININT)
                                                        == g * TRAININT + 1) + 1,
                        cand_lat=np.arange(1, TRAININT + 1), thres=2)  # code L225-238
                   for g, ids in enumerate(groups)]
    keep = {n_proto: proto_types}
    for s in snap_split:
        keep[n_proto + s] = split_types
    w = w_sub
    for t in range(n_proto + n_split):                               # code L116-141
        bdyn = (_rand(rng, N, nsteps) >= (1 - PIN)).astype(float)
        bdyn[:k, :] = psyl_in if proto[t] else alt_in
        w, xdyn = hvc_iter(w, bdyn, gamma=gammas[t], wmax=wmaxs[t], m=ms[t], beta=beta,
                           eta=eta, epsilon=epsilon)
        if t + 1 in keep:
            snaps[t + 1] = dict(w=w, xdyn=xdyn, input=bdyn, types=keep[t + 1],
                                gamma=gammas[t], wmax=wmaxs[t], m=ms[t])
    return dict(seed=seed, seeds=seeds, groups=groups, snapshots=snaps)


def run_alternating(seed=9038):
    """Alternating differentiation, code L23-141 (Fig. 5a-d). Snapshots: 'subsong' (end of the
    1,000-step subsong record), 500 (end of protosyllable stage), 992 and 2500 (code L131-139).
    Each snapshot holds the weights `w`, the activity `xdyn` of that iteration, its `input`, and the
    participation definitions `types` the code's plotting uses (code L184-238)."""
    return _run_seeded_rhythm(
        seed,
        k=10,                 # code L35, "Ten neurons were designated as seed neurons" (Methods)
        n_groups=2,           # code L89-91, "divided into two groups" (Methods)
        m_start=10,           # code L48, "m was decreased from 10 to 5" (Methods)
        m_split=10 * WMAX_START / WMAX_SPLIT,  # code L51, mSplit = Wmax/wmaxSplit = 5
        beta=0.115,           # code L37, beta = 0.115 (Methods)
        eta=0.025,            # code L39, eta = 0.025 (Methods)
        epsilon=0.2,          # code L40, epsilon = 0.2 (Methods)
        gamma_split=0.18,     # code L43, "increased from 0.01 to 0.18" (Methods)
        t0=500,               # code L66, "inflection point t0 = 500 iterations" (Methods)
        n_proto=500,          # code L57, "500 iterations of 10 pulses each" (Methods)
        n_split=2000,         # code L60, "The splitting stage consisted of 2,000 iterations"
        snap_split=(492, 2000),  # code L58, L60
        nsteps=100,           # code L30, "1 s total per iteration" (Methods)
        nsteps_subsong=1000,  # code L32
        how_on=10,            # code L54, "strong external input (Wmax)" (Methods), Wmax = 10
    )


def run_motif(seed=9038):
    """Motif strategy (Extended Data Fig. 10e-h), Methods: "similar manner as alternating
    differentiation, except that 9 seed neurons were used, and for the splitting stage, seed
    neurons were divided into 3 groups of 3 neurons, each driven on every third cycle".
    The Methods give no iteration counts, snapshot iterations, participation threshold or seed for
    this strategy; these follow the alternating run (500 + 2,000 iterations, snapshots 500, 992,
    2500, thresholds 4 and 2, seed 9038). Group g (0, 1, 2) is driven at steps with
    mod(step, 30) == 10 g + 1 within the 100-step iteration, so the groups get 4, 3 and 3 pulses."""
    return _run_seeded_rhythm(
        seed,
        k=9,                  # Methods, "9 seed neurons were used"
        n_groups=3,           # Methods, "divided into 3 groups of 3 neurons"
        m_start=9,            # Methods, "m was decreased from 9 to 3"
        m_split=3,            # Methods, "m was decreased from 9 to 3" (so Wmax 9 -> 6)
        beta=0.115,           # Methods, motif strategy, "beta = 0.115"
        eta=0.025,            # Methods, motif strategy, "eta = 0.025"
        epsilon=0.2,          # Methods, motif strategy, "epsilon = 0.2"
        gamma_split=0.18,     # Methods, "gamma was increased from 0.01 to 0.18"
        t0=500,               # Methods, "inflection point t0 = 500 iterations"
        n_proto=500,          # not in Methods; as alternating (code L57)
        n_split=2000,         # not in Methods; as alternating (code L60)
        snap_split=(492, 2000),  # not in Methods; as alternating (code L58, L60)
        nsteps=100,           # "similar manner as alternating" (code L30, 1 s per iteration)
        nsteps_subsong=1000,  # as alternating (code L32)
        how_on=10,            # as alternating code L54 (Methods' "Wmax" would be 9 here)
    )


MOTIF_GITHUB = "github.com/emackev/HVCModelCode, commit 05dc96b1263ee14c066eeda674b96b015f6c57d7"


def run_motif_github(seed=210):
    """Motif strategy as in `RunHVC_split_intoThree.m` of the GitHub code (MOTIF_GITHUB), reading
    (b) of model-ed10eh-motif. That script: seed 210 (its L45); 9 seed neurons (L55); wmax 1 and
    m 9 (L46-47), so Wmax = 9; beta 0.115, alpha 30, eta 0.025, epsilon 0.2, tau 4, gamma 0.01
    (L56-61); splitting with wmaxSplit 3 and m = Wmax / wmaxSplit = 3 (L63, L159-160), gamma rising
    as sigmf(1:2000, [1/200 500]) * 0.18 (L68); Niter = [1 499 690 2000] (L67): 500 protosyllable
    iterations, then 690 and 2,000 splitting iterations (snapshots there). Seeds 1-3, 4-6 and 7-9
    are driven at steps with mod(step, 30) == 1, 11 and 21 (L101-103), so in a 100-step iteration
    the groups get 4, 3 and 3 pulses, as in reading (a). Random numbers: rng(seed) once before the
    initial weights (L84-85), no subsong stage, then per iteration rand(n, nsteps) (L120 ...).
    The script's own classification is in `HVCtestRaster_intoThree.m` (see `raster_classes`)."""
    k, nsteps = 9, 100
    wmax0, m0, wmax_split = 1.0, 9.0, 3.0
    Wmax = wmax0 * m0
    gammas = sigmf(np.arange(1, 2001), 1 / SIG_TAU, 500) * 0.18
    steps = np.arange(1, nsteps + 1)
    psyl_in = np.full((k, nsteps), -float(HOW_CLAMPED))
    psyl_in[:, steps % TRAININT == 1] = 10.0
    alt_in = np.full((k, nsteps), -float(HOW_CLAMPED))
    groups = [np.arange(0, 3), np.arange(3, 6), np.arange(6, 9)]
    for g, ids in enumerate(groups):
        alt_in[np.ix_(ids, np.flatnonzero(steps % (3 * TRAININT) == g * TRAININT + 1))] = 10.0
    rng = np.random.default_rng(seed)
    w = 2 * _rand(rng, N, N) * Wmax / N
    snaps = {}
    proto_types = [dict(nids=np.arange(k), tind=np.flatnonzero(steps % TRAININT == 1) + 1,
                        cand_lat=np.arange(1, TRAININT + 1), thres=4) for _ in range(3)]  # as run_motif
    split_types = [dict(nids=ids, tind=np.flatnonzero(steps % (3 * TRAININT) == g * TRAININT + 1) + 1,
                        cand_lat=np.arange(1, TRAININT + 1), thres=2) for g, ids in enumerate(groups)]
    for t in range(500):
        bdyn = (_rand(rng, N, nsteps) >= (1 - PIN)).astype(float)
        bdyn[:k, :] = psyl_in
        w, xdyn = hvc_iter(w, bdyn, gamma=GAMMA_START, wmax=wmax0, m=m0, beta=0.115, eta=0.025, epsilon=0.2)
    snaps[500] = dict(w=w, xdyn=xdyn, input=bdyn, types=proto_types)
    for i in range(2000):
        bdyn = (_rand(rng, N, nsteps) >= (1 - PIN)).astype(float)
        bdyn[:k, :] = alt_in
        w, xdyn = hvc_iter(w, bdyn, gamma=gammas[i], wmax=wmax_split, m=Wmax / wmax_split, beta=0.115,
                           eta=0.025, epsilon=0.2)
        if i + 1 in (690, 2000):
            snaps[500 + i + 1] = dict(w=w, xdyn=xdyn, input=bdyn, types=split_types)
    return dict(seed=seed, seeds=np.arange(k), groups=groups, snapshots=snaps)


def raster_classes(xdyn, k=9):
    """The classification of `HVCtestRaster_intoThree.m` (MOTIF_GITHUB, L44-46): over the first 60
    steps of the iteration (two cycles of the three groups), a non-seed neuron firing more than 4
    times is shared by three groups, 3 or 4 times by two; the rest (at most 2 firings) are
    specific or silent. Returns counts (three, two, one or two firings, silent)."""
    c = np.asarray(xdyn[k:, :60], dtype=float).sum(axis=1)
    return dict(three=int((c > 4).sum()), two=int(((c > 2) & (c < 5)).sum()),
                specific=int(((c >= 1) & (c <= 2)).sum()), silent=int((c == 0).sum()))


# ---------------------------------------------------------------- bout-onset runs
def _bout_onset_core(seed, *, beta, eta, epsilon, gamma_split, how_on, how_on_psyl_start,
                     how_on_psyl_split):
    """Bout-onset section, code L281-408."""
    k = 10                       # code L292, "5 bout-onset seed neurons and 5 protosyllable" (Methods)
    nsteps = 500                 # code L288, "Each iteration of the simulation was 5 s long"
    m_start = 5                  # code L305, "m was decreased from 5 to 2.5" (Methods)
    Wmax = m_start * WMAX_START  # code L307
    m_split = Wmax / WMAX_SPLIT  # code L308, = 2.5
    n_early, n_proto, n_split1, n_split = 5, 100, 30, 500   # code L317-321
    t0 = 250                     # code L327, "inflection point t0 = 250 iterations" (Methods)
    cycles_per_bout = 5          # code L336
    b_on_offset = 3              # code L337, "Then, 30 ms later" (Methods)
    gammas = np.r_[np.full(n_proto, GAMMA_START),
                   gamma_split * sigmf(np.arange(1, n_split + 1), 1 / SIG_TAU, t0)]  # code L326-327
    wmaxs = np.r_[np.full(n_proto, WMAX_START), np.full(n_split, WMAX_SPLIT)]       # code L328-329
    ms = np.r_[np.full(n_proto, m_start), np.full(n_split, m_split)]                # code L330-331
    how_on_psyl = np.r_[np.full(n_proto, how_on_psyl_start),
                        np.full(n_split, how_on_psyl_split)]                         # code L332-333
    bo = np.arange(k // 2)          # bout-onset seeds, code L371
    ps = np.arange(k // 2, k)       # protosyllable seeds, code L372

    rng = np.random.default_rng(seed)                                # code L342
    w = 2 * _rand(rng, N, N) * Wmax / N                              # code L343
    rng.permutation(20)                                              # code L344 (value unused)
    snap_at = {n_early: "early", n_proto: "proto", n_proto + n_split1: "split1",
               n_proto + n_split: "split2"}
    snaps = {}
    for t in range(n_proto + n_split):                               # code L347
        inp = np.full((k, nsteps), -float(HOW_CLAMPED))              # code L354
        var = np.r_[1, rng.permutation(20) + 1]                      # code L355
        ind_psyl, ind_bstart, ind_off = [], [], []
        prev_end = 1
        for i in range(1, nsteps // cycles_per_bout // TRAININT + 1):    # code L358-368
            istart = (i - 1) * cycles_per_bout * TRAININT + 1 + var[i - 1] + b_on_offset
            ind_bstart.append(istart - b_on_offset)
            ind_psyl += [istart, istart + TRAININT, istart + 2 * TRAININT]
            ind_off += list(range(prev_end, istart - b_on_offset))
            prev_end = istart + 3 * TRAININT
        ind_psyl = np.array([v for v in ind_psyl if v <= nsteps])    # code L369
        ind_bstart = np.array([v for v in ind_bstart if v <= nsteps])  # code L370
        ind_off = np.array(ind_off, dtype=int)
        inp[np.ix_(bo, ind_bstart - 1)] = how_on                     # code L371
        inp[np.ix_(ps, ind_psyl - 1)] = how_on_psyl[t]               # code L372
        bdyn = (_rand(rng, N, nsteps) >= (1 - PIN)).astype(float)    # code L373
        bdyn[:k, :] = inp                                            # code L374
        if ind_off.size:
            bdyn[:, ind_off - 1] = -HOW_CLAMPED                      # code L375
        w, xdyn = hvc_iter(w, bdyn, gamma=gammas[t], wmax=wmaxs[t], m=ms[t], beta=beta,
                           eta=eta, epsilon=epsilon)                 # code L379
        if t + 1 in snap_at:                                         # code L382-407
            onset = ind_bstart + b_on_offset
            types = [dict(nids=bo, tind=onset,
                          cand_lat=np.arange(-b_on_offset + 1, TRAININT + 1), thres=4),
                     dict(nids=ps, tind=np.setdiff1d(ind_psyl, onset),
                          cand_lat=np.arange(1, TRAININT + 1), thres=6)]   # code L446-490
            snaps[t + 1] = dict(name=snap_at[t + 1], w=w, xdyn=xdyn, input=bdyn, types=types,
                                ind_psyl=ind_psyl, ind_bstart=ind_bstart, gamma=gammas[t],
                                wmax=wmaxs[t], m=ms[t])
    return dict(seed=seed, seeds=np.arange(k), bout_seeds=bo, psyl_seeds=ps, snapshots=snaps)


def run_bout_onset(seed=1009):
    """Bout-onset differentiation, code L281-408 (Extended Data Fig. 10a-d). Snapshots at
    iterations 5, 100, 130, 600 (code L317-321, L382-407), each with `w`, `xdyn`, `input`, the
    participation `types` of code L446-490, and the 1-based protosyllable / bout start times."""
    return _bout_onset_core(
        seed,
        beta=0.13,            # code L294, "beta = 0.13" (Methods)
        eta=0.05,             # code L296, "eta = 0.05" (Methods)
        epsilon=0.14,         # code L297, "epsilon = 0.14" (Methods)
        gamma_split=0.04,     # code L300, "from 0.01 to 0.04" (Methods)
        how_on=10,            # code L311
        how_on_psyl_start=10,  # code L312
        how_on_psyl_split=1,  # code L313, "decreased to Wmax/10" (Methods; Wmax/10 = 0.5 there)
    )


def run_new_chain(seed=1009):
    """Formation of a new syllable at bout onset (Extended Data Fig. 10i-k), Methods: "Input to
    seed neurons was set high (2.5* Wmax), and maintained at this high level throughout
    development", beta 0.13, eta 0.05, epsilon 0.15, m 5 to 2.5, gamma 0.01 to 0.05, t0 250.
    Everything the Methods leave open follows the bout-onset run (code L281-408): bout structure,
    iteration counts, snapshots 5, 100, 130, 600, seed 1009, theta = 10, random input size 1,
    participation thresholds 4 and 6. 2.5 Wmax = 12.5 is applied to both seed groups."""
    return _bout_onset_core(
        seed,
        beta=0.13,              # Methods, new-syllable case, "beta = 0.13"
        eta=0.05,               # Methods, new-syllable case, "eta = 0.05"
        epsilon=0.15,           # Methods, new-syllable case, "epsilon = 0.15"
        gamma_split=0.05,       # Methods, "gamma was increased from 0.01 to 0.05"
        how_on=2.5 * 5,         # Methods, "set high (2.5* Wmax)", Wmax = m wmax = 5
        how_on_psyl_start=2.5 * 5,  # Methods, "(2.5* Wmax)"
        how_on_psyl_split=2.5 * 5,  # Methods, "maintained at this high level throughout"
    )


# ---------------------------------------------------------------- measures
def find_latency(xdyn, types):
    """findLatency, code L575-608. For each syllable type returns `mode` (most common latency, a
    value of cand_lat; first maximum on ties, as MATLAB max), `fire_dur` (participation: firing count
    at that latency > thres) and `n_fired` (n x len(cand_lat))."""
    xdyn = np.asarray(xdyn, dtype=float)
    n, nsteps = xdyn.shape
    out = []
    for ty in types:
        cand = np.asarray(ty["cand_lat"])
        nf = np.zeros((n, cand.size))
        for li, lat in enumerate(cand):
            t_inds = np.zeros(nsteps)
            idx1 = np.minimum(nsteps, np.asarray(ty["tind"]) + lat) - 1   # 1-based, code L592-594
            t_inds[idx1 - 1] = 1
            nf[:, li] = xdyn @ t_inds                                      # code L595-596
        best = nf.argmax(axis=1)
        out.append(dict(mode=cand[best], fire_dur=nf.max(axis=1) > ty["thres"], n_fired=nf))
    return out


def participation(xdyn, types):
    """(n_types, n) boolean participation, FireDur of findLatency (code L604-605)."""
    return np.array([L["fire_dur"] for L in find_latency(xdyn, types)])


def shared_specific(lat, seeds):
    """Shared / specific classification of code L644-647 (and L1059-1062), generalised to any
    number of types: specific = participates in exactly one type, shared = in two or more.
    Counts are given for non-seed neurons and, with suffix `_all`, for all neurons.
    `shared_same_lat` = shared neurons whose most common latency is the same in every type they
    participate in (the condition of code L789)."""
    fd = np.array([L["fire_dur"] for L in lat])
    md = np.array([L["mode"] for L in lat])
    n = fd.shape[1]
    nonseed = np.ones(n, bool)
    nonseed[np.asarray(seeds)] = False
    npart = fd.sum(axis=0)
    same = np.array([np.unique(md[fd[:, i], i]).size == 1 if npart[i] >= 2 else False
                     for i in range(n)])
    res = {}
    for suffix, mask in (("", nonseed), ("_all", np.ones(n, bool))):
        part = (npart >= 1) & mask
        shared = (npart >= 2) & mask
        res["participating" + suffix] = int(part.sum())
        res["shared" + suffix] = int(shared.sum())
        res["shared_same_lat" + suffix] = int((shared & same).sum())
        res["specific" + suffix] = [int(((npart == 1) & fd[j] & mask).sum()) for j in range(len(lat))]
        res["shared_fraction" + suffix] = float(shared.sum() / part.sum()) if part.sum() else np.nan
    return res


def latencies(lat, seeds, types_idx=None):
    """Most common latencies (in steps, values of cand_lat) of participating non-seed neurons. A
    neuron contributes each distinct latency among the types it participates in (one value if the
    same in all). `types_idx` restricts the types used (e.g. [0] for the protosyllable stage, where
    the code defines two identical types)."""
    idx = range(len(lat)) if types_idx is None else types_idx
    fd = np.array([lat[j]["fire_dur"] for j in idx])
    md = np.array([lat[j]["mode"] for j in idx])
    nonseed = np.ones(fd.shape[1], bool)
    nonseed[np.asarray(seeds)] = False
    out = []
    for i in np.flatnonzero(nonseed & fd.any(axis=0)):
        out += list(np.unique(md[fd[:, i], i]))
    return np.array(out, dtype=float)


def subsong_decay(xdyn, is_onset, seeds, max_lag=20, window=TRAININT):
    """Model-fig5a measure. For lag 0..max_lag, mean number of active non-seed neurons at step
    t0 + lag over seed activations t0 (`is_onset`, the steps at which seed input is on; the input in
    column t acts at step t, code L536). `all`: every onset; `isolated`: onsets with no other onset
    within `window` steps before and `max_lag` steps after. `baseline`: mean over steps with no
    onset at that step or in the `window` steps before."""
    xdyn = np.asarray(xdyn, bool)
    nonseed = np.ones(xdyn.shape[0], bool)
    nonseed[np.asarray(seeds)] = False
    cnt = xdyn[nonseed].sum(axis=0).astype(float)
    T = cnt.size
    on = np.flatnonzero(is_onset)
    iso = [t for t in on if not is_onset[max(0, t - window):t].any()
           and not is_onset[t + 1:t + max_lag + 1].any()]

    def trace(ts):
        ts = [t for t in ts if t + max_lag < T]
        return np.array([cnt[np.array(ts) + l].mean() if ts else np.nan
                         for l in range(max_lag + 1)]), len(ts)

    base = np.array([not is_onset[max(0, t - window):t + 1].any() for t in range(T)])
    a, na = trace(on)
    b, nb = trace(iso)
    return dict(lags=np.arange(max_lag + 1), all=a, n_all=na, isolated=b, n_isolated=nb,
                baseline=float(cnt[base].mean()), n_baseline=int(base.sum()))


def period_autocorr(xdyn, lo_ms=80, hi_ms=1000):
    """Per neuron, the lag (ms) of the largest autocorrelation value of its binary activity at lags
    lo_ms..hi_ms (steps of 10 ms; lags beyond the record are dropped). Autocorrelation is the raw
    count sum_t x(t) x(t+L); ties go to the shortest lag; NaN if all values are 0."""
    x = np.asarray(xdyn, float)
    T = x.shape[1]
    lags = np.arange(lo_ms // STEP_MS, min(hi_ms // STEP_MS, T - 1) + 1)
    ac = np.array([(x[:, :T - L] * x[:, L:]).sum(axis=1) for L in lags]).T
    per = lags[ac.argmax(axis=1)] * STEP_MS
    return np.where(ac.max(axis=1) > 0, per, np.nan).astype(float)


def period_ibi(xdyn):
    """Per neuron, the most common inter-burst interval (ms; shortest on ties), NaN if fewer than
    two bursts."""
    out = np.full(xdyn.shape[0], np.nan)
    for i, row in enumerate(np.asarray(xdyn, bool)):
        d = np.diff(np.flatnonzero(row))
        if d.size:
            v, c = np.unique(d, return_counts=True)
            out[i] = v[c.argmax()] * STEP_MS
    return out


def seed_reliability(xdyn, times, nids):
    """Fraction of the given 1-based input times (e.g. `ind_psyl`) at which each listed seed neuron
    bursts (input in column t acts at step t, code L536-546)."""
    return np.asarray(xdyn, bool)[np.ix_(np.asarray(nids), np.asarray(times) - 1)].mean(axis=1)
