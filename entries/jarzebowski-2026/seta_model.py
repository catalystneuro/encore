"""Two-compartment LIF model of an L2/3 neuron, from the Methods of Jarzebowski & Bendor (2026).

Every parameter is from the Methods ("Computational model of L2/3 neuron", "Synaptic connectivity
and kinetics", "Scaling of L2/3 inputs"):

- soma C = 0.281 nF, g_leak = 9.4 nS; AIS C = 0.0145 nF, g_leak = 1.25 nS; E_rest = -70 mV;
  axial g_a = 18 nS; spike when V_ais reaches -50 mV, both compartments reset to -70 mV and held
  for a 2 ms refractory period;
- noise n(t) = sigma / sqrt(tau_noise) * xi(t), sigma = 3 mV, tau_noise = 10 ms, independent in each
  compartment, xi white noise as in Brian 2 (so each step adds sigma * sqrt(dt / tau_noise) * N(0, 1));
- alpha conductances g(t) = g_max (t / tau) exp(1 - t / tau): L4 tau 4 ms, E 0 mV; L5 IT tau 8 ms,
  E 0 mV; basket tau 6 ms, E -75 mV, g = 1.2 x L4 by default, onset 2.5 ms after L4; ChC on the AIS,
  tau 4 ms, E -58 mV, 25 nS by default, onset 1.5 ms after L5 IT.

The paper ran the model in Brian 2. This module integrates the same equations with the
Euler-Maruyama method, the method Brian 2 uses for equations with noise, at dt = 0.1 ms, Brian 2's
default (the claims file names 0.1 ms as the standard step). The 50 ms before the inputs, with the
neuron at rest, let the noise settle; this and the 100 ms counting window are standard choices that
should not change a result (the inputs end well within it).
"""
import numpy as np

C_S, GL_S = 281.0, 9.4      # pF, nS
C_A, GL_A = 14.5, 1.25      # pF, nS
E_REST, V_TH, V_RESET, T_REF = -70.0, -50.0, -70.0, 2.0
G_AX = 18.0
SIGMA, TAU_NOISE = 3.0, 10.0
TAU = {"l4": 4.0, "l5": 8.0, "bc": 6.0, "chc": 4.0}
E = {"l4": 0.0, "l5": 0.0, "bc": -75.0, "chc": -58.0}
BC_DELAY, CHC_DELAY = 2.5, 1.5
DEFAULTS = dict(l4=60.0, l5=12.0, chc=25.0, bc_scale=1.2, e_chc=-58.0)


def alpha(t, gmax, tau):
    t = np.asarray(t, float)
    with np.errstate(over="ignore"):
        return np.where(t >= 0, gmax * (t / tau) * np.exp(1 - t / tau), 0.0)


def simulate(l4, l5, chc, bc_scale=1.2, e_chc=-58.0, sens_delay=0.0, pred_delay=0.0, gain=1.0,
             runs=80, rng=None, dt=0.1, pre=50.0, window=100.0):
    """Spike times (ms from the input onset) of `runs` noisy runs for each condition.

    l4, l5, chc, bc_scale, e_chc, sens_delay, pred_delay, gain may be arrays of one shape (the
    conditions). L4 and basket start at sens_delay, L5 IT and ChC at pred_delay (ms); all four
    conductances are multiplied by gain. Returns a list (one per condition) of lists (one per run)
    of spike times, measured from time 0 (the earlier of the two onsets when delays differ)."""
    b = np.broadcast_arrays(*[np.atleast_1d(np.asarray(x, float)) for x in
                              (l4, l5, chc, bc_scale, e_chc, sens_delay, pred_delay, gain)])
    l4, l5, chc, bcs, ech, sd, pdl, gn = [x.reshape(-1, 1) for x in b]
    K = l4.shape[0]
    n = int(round((pre + window) / dt))
    vs = np.full((K, runs), E_REST)
    va = np.full((K, runs), E_REST)
    ref = np.zeros((K, runs))
    spikes = [[[] for _ in range(runs)] for _ in range(K)]
    noise_k = SIGMA * np.sqrt(dt / TAU_NOISE)
    for step in range(n):
        t = step * dt - pre
        g4 = alpha(t - sd, gn * l4, TAU["l4"])
        gb = alpha(t - sd - BC_DELAY, gn * l4 * bcs, TAU["bc"])
        g5 = alpha(t - pdl, gn * l5, TAU["l5"])
        gc = alpha(t - pdl - CHC_DELAY, gn * chc, TAU["chc"])
        i_s = GL_S * (E_REST - vs) + g4 * (E["l4"] - vs) + g5 * (E["l5"] - vs) + gb * (E["bc"] - vs) \
            + G_AX * (va - vs)
        i_a = GL_A * (E_REST - va) + gc * (ech - va) + G_AX * (vs - va)
        dvs = dt * i_s / C_S + noise_k * rng.standard_normal((K, runs))
        dva = dt * i_a / C_A + noise_k * rng.standard_normal((K, runs))
        active = ref <= 0
        vs = np.where(active, vs + dvs, V_RESET)
        va = np.where(active, va + dva, V_RESET)
        ref -= dt
        fired = active & (va >= V_TH)
        if fired.any():
            for k, r in zip(*np.nonzero(fired)):
                if t >= 0:
                    spikes[k][r].append(round(t, 4))
            vs[fired] = V_RESET
            va[fired] = V_RESET
            ref[fired] = T_REF
    return spikes


def summarise(spk):
    """Per condition: expected spike count, fraction of runs with >= 1 and >= 2 spikes, and the
    first-spike latencies of runs that spike."""
    out = []
    for runs in spk:
        c = np.array([len(s) for s in runs])
        lat = np.array([s[0] for s in runs if s])
        out.append(dict(count=c.mean(), p1=(c >= 1).mean(), p2=(c >= 2).mean(), n_spiking=int((c >= 1).sum()),
                        lat_median=float(np.median(lat)) if len(lat) else np.nan,
                        lat_mean=float(lat.mean()) if len(lat) else np.nan,
                        single=float((c[c >= 1] == 1).mean()) if (c >= 1).any() else np.nan))
    return out


def trace(l4, l5, chc, bc_scale=1.2, e_chc=-58.0, gain=1.0, sigma=0.0, rng=None, dt=0.1, pre=50.0,
          window=100.0):
    """One run of one condition with the voltages and conductances at every step, for inspection.

    sigma = 0 gives the noise-free run. Returns a dict of arrays over time (ms from the input onset):
    t, v_soma, v_ais, g_l4, g_bc, g_l5, g_chc, and the spike times."""
    n = int(round((pre + window) / dt))
    vs = va = E_REST
    ref = 0.0
    noise_k = sigma * np.sqrt(dt / TAU_NOISE)
    rec = {k: np.zeros(n) for k in ["t", "v_soma", "v_ais", "g_l4", "g_bc", "g_l5", "g_chc"]}
    spikes = []
    for step in range(n):
        t = step * dt - pre
        g4 = float(alpha(t, gain * l4, TAU["l4"]))
        gb = float(alpha(t - BC_DELAY, gain * l4 * bc_scale, TAU["bc"]))
        g5 = float(alpha(t, gain * l5, TAU["l5"]))
        gc = float(alpha(t - CHC_DELAY, gain * chc, TAU["chc"]))
        i_s = GL_S * (E_REST - vs) + g4 * (E["l4"] - vs) + g5 * (E["l5"] - vs) + gb * (E["bc"] - vs) \
            + G_AX * (va - vs)
        i_a = GL_A * (E_REST - va) + gc * (e_chc - va) + G_AX * (vs - va)
        dvs = dt * i_s / C_S + (noise_k * rng.standard_normal() if sigma else 0.0)
        dva = dt * i_a / C_A + (noise_k * rng.standard_normal() if sigma else 0.0)
        if ref <= 0:
            vs, va = vs + dvs, va + dva
        else:
            vs = va = V_RESET
        ref -= dt
        if ref <= 0 and va >= V_TH:
            if t >= 0:
                spikes.append(round(t, 4))
            vs = va = V_RESET
            ref = T_REF
        for k, v in zip(rec, [t, vs, va, g4, gb, g5, gc]):
            rec[k][step] = v
    rec["spikes"] = spikes
    return rec
