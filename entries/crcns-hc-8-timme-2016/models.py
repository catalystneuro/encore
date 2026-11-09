"""The three models of Timme et al. (2016), Methods 2.4, ported from the NCC MATLAB toolbox.

These are simulations: they use no recorded data. Parameters:

- Chain model (Methods 2.4, last paragraph): 12 neurons, the first active or inactive in
  alternate runs (so p = 0.5 each), p(a_i+1 = a_i) = 0.5 (1 + c). Methods 2.9 say the model's
  joint distribution was defined exactly, so the complexity uses the exact distribution and every
  subset of each size (Eq. 10; "the lesser of all possible permutations or 100").
- Bethe lattice (Methods 2.4, `bethelattice.m`): each neuron sends two connections to the next
  layer, p_trans = 0.5, one active neuron in layer 1 per run, activity stopped at layer 10^4.
  The number of runs, 10^4, is the claims file's standard choice. Small avalanches are runs whose
  last active layer is 8 or less ("stopped on or before the 8th layer", Results 3.1); in the
  raster, runs follow each other with one silent bin between them, as `bethelattice.m` places
  them, over the 255 neurons of layers 1 to 8.
- Cortical branching model (Methods 2.4, `cbmodel.m` with method 'spont'): 100 neurons on a
  10 x 10 torus, four nearest neighbours, p_spont = 10^-4, 3 x 10^5 steps. A neuron with j
  active neighbours fires with the probability `cbmodel.m` builds, P_0 = p_spont,
  P_j+1 = P_j + p_trans - P_j p_trans.
"""

from __future__ import annotations

from itertools import combinations

import numpy as np


# ----------------------------------------------------------------------------------------------
# Chain model

def chain_joint(c: float, n: int = 12):
    """All 2^n states and their exact probabilities."""
    states = ((np.arange(2 ** n)[:, None] >> np.arange(n)[None, :]) & 1).astype(np.int8)
    same = states[:, 1:] == states[:, :-1]
    p = 0.5 * np.prod(np.where(same, 0.5 * (1 + c), 0.5 * (1 - c)), axis=1)
    return states, p


def _entropy(p):
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


def chain_integration_curve(c: float, n: int = 12):
    """Mean integration over all subsets of each size k = 1..n (Eq. 9), from the exact joint."""
    states, p = chain_joint(c, n)
    weights = 1 << np.arange(n)
    h1 = np.array([_entropy(np.bincount(states[:, i], weights=p, minlength=2)) for i in range(n)])
    curve = np.zeros(n)
    for k in range(2, n + 1):
        vals = []
        for sub in combinations(range(n), k):
            sub = list(sub)
            code = states[:, sub] @ weights[:k]
            hj = _entropy(np.bincount(code, weights=p, minlength=2 ** k))
            vals.append(h1[sub].sum() - hj)
        curve[k - 1] = np.mean(vals)
    return curve


def complexity_from_curve(curve):
    """Eq. 10: (1/N) sum over k of [(k-1)/(N-1) I(X) - <I(X_j^k)>]."""
    N = len(curve)
    return float(np.sum(np.linspace(0, curve[-1], N) - curve) / N)


# ----------------------------------------------------------------------------------------------
# Bethe lattice

def bethe_full_sizes(n_runs: int, rng, p: float = 0.5, stop_layer: int = 10 ** 4):
    """Sizes, durations and profiles of the full model (counts per layer only):
    n_l+1 ~ Binomial(2 n_l, p), stopped at layer 10^4."""
    sizes = np.zeros(n_runs, dtype=np.int64)
    durs = np.zeros(n_runs, dtype=np.int64)
    profiles = []
    for r in range(n_runs):
        n, layer, prof = 1, 1, [1]
        while n > 0 and layer < stop_layer:
            n = rng.binomial(2 * n, p)
            layer += 1
            if n > 0:
                prof.append(n)
        sizes[r], durs[r] = sum(prof), len(prof)
        profiles.append(np.array(prof))
    return sizes, durs, profiles


def bethe_small_raster(n_runs: int, rng, p: float = 0.5, max_layer: int = 8):
    """Runs of the Bethe lattice, keeping those whose last active layer is <= max_layer.

    Neuron j of layer l (1-based j) has index 2^(l-1) - 1 + (j - 1); a neuron's children in the
    next layer are 2(j-1)+1 and 2(j-1)+2, as `bethelattice.m`. Returns the raster as a list of
    1-based spike bins per neuron, the number of bins, and the small avalanches' sizes."""
    n_neurons = 2 ** max_layer - 1
    spikes_t, spikes_n, sizes = [], [], []
    t0 = 1
    for r in range(n_runs):
        active = np.array([0])          # 0-based position within the layer
        rec = [(1, active)]
        layer = 1
        while active.size and layer <= max_layer:
            hits = rng.random(2 * active.size) < p
            idx = np.flatnonzero(hits)
            active = 2 * active[idx // 2] + (idx % 2)
            layer += 1
            if active.size:
                rec.append((layer, active))
        if active.size:                 # still active beyond max_layer: not a small avalanche
            continue
        dur = len(rec)
        for l, a in rec:
            spikes_t.append(np.full(a.size, t0 + l - 1))
            spikes_n.append(2 ** (l - 1) - 1 + a)
        sizes.append(sum(a.size for _, a in rec))
        t0 += dur + 1                   # one silent bin between runs
    t = np.concatenate(spikes_t)
    nn = np.concatenate(spikes_n)
    raster = [np.sort(t[nn == j]) for j in range(n_neurons)]
    return raster, int(t0 - 1), np.array(sizes)


# ----------------------------------------------------------------------------------------------
# Cortical branching model

def cb_simulate(p_trans: float, n_models: int, rng, t_steps: int = 3 * 10 ** 5,
                side: int = 10, p_spont: float = 1e-4):
    """n_models independent cortical branching models run together; returns packed states
    (t_steps x n_models x ceil(side^2 / 8) uint8). The first step is silent, as cbmodel.m."""
    n = side * side
    probconv = np.zeros(5)
    probconv[0] = p_spont
    for j in range(4):
        probconv[j + 1] = probconv[j] + p_trans - probconv[j] * p_trans
    packed = np.zeros((t_steps, n_models, (n + 7) // 8), dtype=np.uint8)
    state = np.zeros((n_models, side, side), dtype=bool)
    for it in range(1, t_steps):
        s = state.view(np.int8)
        cnt = (np.roll(s, 1, 1) + np.roll(s, -1, 1) + np.roll(s, 1, 2) + np.roll(s, -1, 2))
        state = rng.random((n_models, side, side)) < probconv[cnt]
        packed[it] = np.packbits(state.reshape(n_models, n), axis=1)
    return packed


def cb_raster(packed: np.ndarray, model: int, n: int = 100) -> np.ndarray:
    """(t_steps x n) bool states of one model."""
    return np.unpackbits(packed[:, model, :], axis=1, count=n).astype(bool)


# ----------------------------------------------------------------------------------------------
# Analyses of the cortical branching model

def _quad_coef(x):
    """Quadratic coefficient of log10 P(x) on log10 x over the values kept by the cuts of
    Methods 2.7 (P over all avalanches); the claims file's reading of "curved"."""
    import hc8
    u, c = np.unique(x, return_counts=True)
    keep = (u >= hc8.MIN_VALUE) & (c >= hc8.MIN_COUNT)
    if keep.sum() < 3:
        return np.nan
    return float(np.polyfit(np.log10(u[keep]), np.log10(c[keep] / x.size), 2)[0])


def cb_point(args) -> list[dict]:
    """One p_trans: simulate n_models models and, for each, the curvature of the size and duration
    distributions, the shape collapse curvature of the full model and extrapolated by sub-sampling
    (30 sub-samples from 40 to 100 neurons, sizes evenly spaced, Methods 2.10), the susceptibility
    (both readings) extrapolated the same way, and B_new (delays 1 to 8, A(t) <= 5, no
    sub-sampling, Methods 2.11). For comparison with 4 p_trans, the mean avalanche size, B_basic
    (Eq. 11) and the one-step ratio sum A(t+1) / sum A(t) over bins with A(t) > 0.
    args = (p_trans, n_models, t_steps, seed)."""
    import hc8
    p_trans, n_models, t_steps, seed = args
    rng = np.random.default_rng(seed)
    packed = cb_simulate(p_trans, n_models, rng, t_steps=t_steps)
    sizes = hc8.subsample_sizes(100)
    out = []
    for m in range(n_models):
        R = cb_raster(packed, m)
        A = R.sum(axis=1).astype(np.int32)
        s, d, st = hc8.avalanches(A)
        rec = dict(p_trans=p_trans, model=m, n_av=int(s.size), active_frac=float((A > 0).mean()),
                   quad_size=_quad_coef(s), quad_dur=_quad_coef(d), mean_size=float(s.mean()),
                   br_basic=hc8.branching_basic(A))
        on = A[:-1] > 0
        rec["one_step"] = float(A[1:][on].sum() / A[:-1][on].sum())
        _, curv = hc8.shape_collapse(hc8.mean_profiles(A, s, d, st))
        rec["curv_full"] = abs(curv) if np.isfinite(curv) else np.nan
        chi_full = hc8.susceptibility(A, 100)
        rec["chi_a_full"], rec["chi_b_full"] = chi_full
        cv, ca, cb = [], [], []
        for n in sizes:
            sub = np.sort(rng.permutation(100)[:n])
            a = R[:, sub].sum(axis=1).astype(np.int32)
            s2, d2, st2 = hc8.avalanches(a)
            c2 = hc8.shape_collapse(hc8.mean_profiles(a, s2, d2, st2))[1]
            cv.append(abs(c2) if np.isfinite(c2) else np.nan)
            x = hc8.susceptibility(a, n)
            ca.append(x[0]); cb.append(x[1])
        rec["curv_ss"] = hc8.wls_intercept(sizes, cv)
        rec["chi_a_ss"] = hc8.wls_intercept(sizes, ca)
        rec["chi_b_ss"] = hc8.wls_intercept(sizes, cb)
        rec["B_new"] = hc8.branching_new(A, hc8.BR_ACT_MAX_MODEL)[0]
        out.append(rec)
    return out


def tau_sd(xmin: int, xmax: int, tau: float, n: int, rng, n_samples: int = 500) -> float:
    """pvcalc.m with threshold 1: the SD of the MLE refitted on surrogates of the fitted law."""
    import hc8
    v = np.arange(xmin, xmax + 1, dtype=float)
    pdf = v ** (-tau)
    pdf /= pdf.sum()
    samp = rng.multinomial(n, pdf, size=n_samples)
    mlog = samp @ np.log(v) / n
    taus = hc8._PLData.TAUS
    logZ = np.log(np.exp(-np.outer(taus, np.log(v))).sum(axis=1))
    L = -logZ[None, :] - mlog[:, None] * taus[None, :]
    return float(np.std(taus[np.argmax(L, axis=1)], ddof=1))
