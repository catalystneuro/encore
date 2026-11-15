"""Network model of Peron et al. (2020), Methods, "Network model", rebuilt in numpy.

The paper simulated its model in Brian2; the model outputs were not deposited, so they are
regenerated here (claims file, model claims, ``data: elsewhere``). Several networks are
simulated at once as one block-diagonal network, which shares the per-step overhead.

Where each parameter comes from:

- Leaky integrate-and-fire neurons, ``tau dV/dt = -(V - Vr) + R(Iexc + Iinh + Iext)``, reset
  to Vr and frozen for tref = 0.5 ms; kick-and-decay synaptic currents (Methods, equations
  1 and 2). R is folded into the weights, as the Methods do, so currents are in mV.
- 2,000 neurons: 200 subnetwork (S), 1,500 other excitatory (E), 300 inhibitory (I);
  tau 30 ms (excitatory) and 10 ms (inhibitory); Vth - Vr uniform within 35 mV +- 50%;
  tau_exc 2 ms, tau_inh 3 ms; delays uniform within 0.6 ms +- 50%; connection
  probabilities 0.2 among excitatory groups and 0.6 for every pair involving I; pSS =
  Pconn (Methods). Unitary PSPs of 1 mV, 1.6 mV within S at Pconn 0.4, and linear
  interpolation or extrapolation of both pSS and the PSP for other Pconn (Methods).
- Kick size for a PSP from equation 7 of the Methods (``psp_to_kick``).
- Inhibitory PSPs are -1 mV. Assumption: the Methods say "All connections had the same
  strength, which was chosen so that the resulting post-synaptic potential (PSP) is 1 mV";
  the sign of inhibitory synapses is taken as negative with the same size.
- Stimulus: a beta(3, 5) waveform stretched so that its peak is 10 ms after onset (50 ms
  for the slow, whisking-like input), applied to S alone (Methods). Its amplitude
  (``strength``, the peak current in mV) is set by the calibration of the claims file's
  readings. Presentations every 300 ms from 300 ms, 66 in 20 s (claims file opening comment;
  github.com/jwittenbach/ablation-sim at a8b5583, ``interval`` 300 ms).
- Background: Poisson excitatory input at 5,000 Hz to excitatory and 2,000 Hz to
  inhibitory neurons (Methods). Its unitary PSP is not given. Assumption: one PSP size per
  population, calibrated so that the tonic rates are 0.5 Hz (excitatory) and 10 Hz
  (inhibitory) at Pconn 0.2 without stimulus, as the Methods say the frequencies "were
  selected so that the tonic firing rate of these populations were approximately 0.5 Hz
  for excitatory neurons and 10 Hz for inhibitory neurons". Per step, the number of background
  events of each population is drawn from a Poisson distribution and each event is given
  to a neuron of the population drawn at random (by a xorshift64 generator), which gives each neuron an independent
  Poisson train at the stated rate.
- dt 0.1 ms; 20 s per run; forward Euler for V and exact decay for the currents (a
  standard choice; Brian2 integrates the same linear equations). The step loop is compiled
  with numba. During the refractory period V is held at Vr.
- Encoding score: spikes convolved with a Gaussian of 20 ms s.d., rate and stimulus taken
  at 0.5 ms, the peak of the normalized cross-correlation within +-10 ms lags (Methods).
  Here spikes are binned at 0.5 ms, the Gaussian is cut at +-3.5 s.d. (as ablation-sim's
  ``xc_score``), and the correlation is circular over the 20 s run, which differs from the
  zero-padded one only at the edges (a standard choice that cannot change a result).
- Ablation: the outgoing synapses of the ablated neurons set to 0 (Methods); the network
  and its background are otherwise the same realisation.
"""
from __future__ import annotations

import numba
import numpy as np
from scipy.stats import beta as _beta

DT = 0.1  # ms
NS, NE, NI = 200, 1500, 300
N = NS + NE + NI
NEXC = NS + NE
TAU_E, TAU_I = 30.0, 10.0
TAU_SE, TAU_SI = 2.0, 3.0
DV_MEAN = 35.0
TREF = 0.5
TD = 0.6
P_EXC, P_INH = 0.2, 0.6
F_BG_E, F_BG_I = 5000.0, 2000.0
INTERVAL = 300.0  # ms
DURATION = 20000.0  # ms
SIGMA = 20.0  # ms
LAG = 10.0  # ms
DS = 5  # samples of dt per 0.5 ms


def psp_to_kick(psp, tau_m, tau_s):
    """Methods, equation 7: Rw = Vmax (a - 1) / (a^(1/(1-a)) - a^(a/(1-a))), a = tau_m/tau_s."""
    a = tau_m / tau_s
    return psp * (a - 1) / (a ** (1 / (1 - a)) - a ** (a / (1 - a)))


def subnet_params(pconn):
    """pSS and the PSP within S, interpolated linearly between (0.2, 1 mV) and (0.4, 1.6 mV)."""
    return pconn, 1.0 + (pconn - 0.2) / 0.2 * 0.6


def stimulus(peak_ms=10.0, duration=DURATION, interval=INTERVAL, dt=DT):
    """Beta(3,5) waveform of peak 1, stretched so that its peak falls ``peak_ms`` after onset."""
    a, b = 3.0, 5.0
    length = peak_ms / ((a - 1) / (a + b - 2))
    n = int(round(length / dt))
    w = _beta.pdf(np.arange(n) / (n - 1), a, b)
    w = w / w.max()
    T = int(round(duration / dt))
    s = np.zeros(T, np.float32)
    k = 1  # first onset one interval after the start, leaving the initial transient out
    while k * interval / dt + n <= T:
        i0 = int(round(k * interval / dt))
        s[i0:i0 + n] += w
        k += 1
    return s, k - 1


class Batch:
    """K independent networks, simulated together."""

    def __init__(self, seeds, pconn, bg_psp=(1.0, 1.0)):
        self.K = len(seeds)
        self.seeds = list(seeds)
        self.pconn = pconn
        pss, psp_ss = subnet_params(pconn)
        groups = np.r_[np.zeros(NS, int), np.ones(NE, int), 2 * np.ones(NI, int)]
        tau_m = np.where(groups < 2, TAU_E, TAU_I)
        pre_l, post_l, w_l, d_l, net_th = [], [], [], [], []
        for k, sd in enumerate(seeds):
            rng = np.random.default_rng([sd, 1])
            prob = np.full((3, 3), P_EXC)
            prob[2, :] = P_INH
            prob[:, 2] = P_INH
            prob[0, 0] = pss
            psp = np.ones((3, 3))  # [pre group, post group]
            psp[0, 0] = psp_ss
            psp[2, :] = -1.0
            P = prob[groups[:, None], groups[None, :]]  # pre x post
            C = rng.random((N, N), dtype=np.float32) < P
            np.fill_diagonal(C, False)
            pre, post = np.nonzero(C)
            pg, qg = groups[pre], groups[post]
            tau_s = np.where(pg < 2, TAU_SE, TAU_SI)
            w = psp_to_kick(psp[pg, qg], tau_m[post], tau_s)
            d = TD * (1 + 0.5 * (2 * rng.random(len(pre)) - 1))
            pre_l.append(pre + k * N)
            post_l.append(post + k * N)
            w_l.append(w.astype(np.float32))
            d_l.append(np.clip(np.round(d / DT), 1, None).astype(np.int32))
            net_th.append(DV_MEAN * (1 + 0.5 * (2 * rng.random(N) - 1)))
        pre = np.concatenate(pre_l)
        order = np.argsort(pre, kind="stable")
        self.pre = pre[order]
        self.post = np.concatenate(post_l)[order].astype(np.int32)
        self.w = np.concatenate(w_l)[order]
        self.delay = np.concatenate(d_l)[order]
        self.exc = (np.tile(groups, self.K)[self.pre] < 2)
        self.ptr = np.searchsorted(self.pre, np.arange(self.K * N + 1))
        self.theta = np.concatenate(net_th).astype(np.float32)
        self.groups = np.tile(groups, self.K)
        self.tau_m = np.tile(tau_m, self.K).astype(np.float32)
        bg = np.where(groups < 2, bg_psp[0], bg_psp[1])
        self.bg_kick = np.tile(psp_to_kick(bg, tau_m, TAU_SE), self.K).astype(np.float32)
        self.bg_lam = np.tile(np.where(groups < 2, F_BG_E, F_BG_I) * DT / 1000.0, self.K)
        self.w_orig = self.w.copy()

    def ablate(self, ids_per_net):
        """Set the outgoing synapses of the given neurons (indices within each network) to 0."""
        self.w = self.w_orig.copy()
        for k, ids in enumerate(ids_per_net):
            for j in np.asarray(ids, int) + k * N:
                self.w[self.ptr[j]:self.ptr[j + 1]] = 0.0

    def run(self, stim, strength, seed, duration=DURATION, pulse=None):
        """Simulate; returns spike steps and neuron indices (global over the batch).

        ``stim`` is the waveform per step; ``strength`` its peak current in mV, given to S.
        ``pulse``: optional (per-step array, amplitude in mV) of current given to I.
        """
        T = int(round(duration / DT))
        Ntot = self.K * N
        lams = np.unique(self.bg_lam)
        members = np.full((len(lams), Ntot), -1, np.int64)
        n_mem = np.zeros(len(lams), np.int64)
        lam_tot = np.zeros(len(lams))
        for g, lam in enumerate(lams):
            m = np.nonzero(self.bg_lam == lam)[0]
            members[g, :len(m)] = m
            n_mem[g] = len(m)
            lam_tot[g] = lam * len(m)
        V0 = (0.5 * self.theta * np.random.default_rng(seed).random(Ntot)).astype(np.float64)
        pt = np.zeros(T) if pulse is None else np.asarray(pulse[0], float)[:T]
        pa = 0.0 if pulse is None else float(pulse[1])
        cap = 8_000_000
        st, si, ns = _simulate(T, self.ptr, self.post, self.w.astype(np.float64), self.delay,
                               self.theta.astype(np.float64), (DT / self.tau_m).astype(np.float64),
                               self.bg_kick.astype(np.float64), lam_tot, members, n_mem,
                               (self.groups == 0).astype(np.float64), (self.groups == 2).astype(np.float64),
                               self.groups == 2, np.asarray(stim, np.float64)[:T], float(strength), pt, pa,
                               int(seed) % (2 ** 31), V0, cap)
        if ns > cap:
            raise RuntimeError(f"{ns} spikes, more than the {cap} recorded")
        return st, si


@numba.njit(fastmath=True)
def _simulate(T, ptr, post, w, delay, theta, dtt, bgk, lam_tot, members, n_mem, gS, gI, inh,
              stim, strength, pt, pa, seed, V0, cap):
    np.random.seed(seed)
    x = np.uint64(seed) * np.uint64(2654435761) + np.uint64(88172645463325252)
    Ntot = len(theta)
    D = 0
    for d in delay:
        D = max(D, d)
    D += 1
    bufE = np.zeros(D * Ntot)
    bufI = np.zeros(D * Ntot)
    V = V0.copy()
    IE = np.zeros(Ntot)
    II = np.zeros(Ntot)
    refr = np.zeros(Ntot, np.int64)
    dE = np.exp(-DT / TAU_SE)
    dI = np.exp(-DT / TAU_SI)
    nref = int(round(TREF / DT))
    sp_t = np.empty(cap, np.int32)
    sp_i = np.empty(cap, np.int32)
    ns = 0
    for t in range(T):
        off = (t % D) * Ntot
        ext = strength * stim[t]
        pul = pa * pt[t]
        # background: a Poisson count of events for each population, each given to a
        # neuron of the population drawn at random (independent Poisson trains per neuron)
        for g in range(len(lam_tot)):
            nev = np.random.poisson(lam_tot[g])
            nm = np.uint64(n_mem[g])
            for e in range(nev):
                # xorshift64 for the neuron of each event (numpy's generator is too slow here)
                x ^= x << np.uint64(13)
                x ^= x >> np.uint64(7)
                x ^= x << np.uint64(17)
                j = members[g, ((x >> np.uint64(32)) * nm) >> np.uint64(32)]
                IE[j] += bgk[j]
        for i in range(Ntot):
            ie = IE[i] + bufE[off + i]
            ii = II[i] + bufI[off + i]
            bufE[off + i] = 0.0
            bufI[off + i] = 0.0
            v = V[i]
            if refr[i] > 0:
                refr[i] -= 1
                v = 0.0
            else:
                v += dtt[i] * (ie + ii + gS[i] * ext + gI[i] * pul - v)
            ie *= dE
            ii *= dI
            if -1e-12 < ie < 1e-12:  # keep decaying currents out of the slow denormal range
                ie = 0.0
            if -1e-12 < ii < 1e-12:
                ii = 0.0
            IE[i] = ie
            II[i] = ii
            V[i] = v
            if V[i] >= theta[i]:
                V[i] = 0.0
                refr[i] = nref
                if ns < cap:
                    sp_t[ns] = t
                    sp_i[ns] = i
                ns += 1
                if inh[i]:
                    for s in range(ptr[i], ptr[i + 1]):
                        bufI[((t + delay[s]) % D) * Ntot + post[s]] += w[s]
                else:
                    for s in range(ptr[i], ptr[i + 1]):
                        bufE[((t + delay[s]) % D) * Ntot + post[s]] += w[s]
    return sp_t[:min(ns, cap)].copy(), sp_i[:min(ns, cap)].copy(), ns


def gauss_kernel(dt_ms):
    t = np.arange(-3.5 * SIGMA, 3.5 * SIGMA + dt_ms / 2, dt_ms)
    g = np.exp(-0.5 * (t / SIGMA) ** 2)
    return (g / g.sum()).astype(np.float64)


def binned(steps, ids, n, T):
    """Spike counts per neuron in 0.5 ms bins, as a dense (n, T/5) array of float32."""
    nb = T // DS
    M = np.zeros((n, nb), np.float32)
    np.add.at(M, (ids, np.minimum(steps // DS, nb - 1)), 1)
    return M


def rates(M):
    """Gaussian-convolved rates (circular), rows of M binned at 0.5 ms."""
    g = gauss_kernel(DT * DS)
    nb = M.shape[1]
    G = np.zeros(nb)
    h = len(g) // 2
    G[:h + 1] = g[h:]
    G[-h:] = g[:h]
    FG = np.fft.rfft(G)
    return np.fft.irfft(np.fft.rfft(M, axis=1) * FG, n=nb, axis=1)


def scores(steps, ids, n, stim, chunk=500):
    """Encoding score of every neuron (Methods): peak normalized cross-correlation of the
    Gaussian-convolved rate with the stimulus at 0.5 ms, lags up to 10 ms."""
    T = len(stim)
    x = stim[::DS].astype(np.float64)
    x = x - x.mean()
    nb = len(x)
    L = int(round(LAG / (DT * DS)))
    out = np.zeros(n)
    Fx = np.conj(np.fft.rfft(x))
    for c0 in range(0, n, chunk):
        sel = (ids >= c0) & (ids < c0 + chunk)
        M = binned(steps[sel], ids[sel] - c0, min(chunk, n - c0), T)
        R = rates(M)
        R = R - R.mean(1, keepdims=True)
        cc = np.fft.irfft(np.fft.rfft(R, axis=1) * Fx[None, :], n=nb, axis=1)  # cc[k] = sum x[t] R[t+k]
        cc = np.concatenate([cc[:, -L:], cc[:, :L + 1]], axis=1)
        den = np.sqrt((x ** 2).sum() * (R ** 2).sum(1))
        with np.errstate(invalid="ignore", divide="ignore"):
            s = cc.max(1) / den
        out[c0:c0 + chunk] = np.nan_to_num(s)
    return out


def split(steps, ids, K):
    """Split batch spikes into per-network (steps, local ids)."""
    net = ids // N
    return [(steps[net == k], ids[net == k] - k * N) for k in range(K)]


def mean_rate(ids, n, duration=DURATION):
    return np.bincount(ids, minlength=n) / (duration / 1000.0)


BG_PSP = (0.39, 1.4)  # mV; calibrated in the notebook (background, see the module docstring)


def similarity(steps, ids, ablated, n=N, T=None, chunk=500):
    """Response similarity (Methods): Pearson correlation of each neuron's Gaussian-convolved
    rate with the mean convolved rate of the ablated neurons, in the pre-ablation run."""
    T = T or int(round(DURATION / DT))
    sel = np.isin(ids, ablated)
    ref = rates(binned(steps[sel], np.searchsorted(np.sort(ablated), ids[sel]), len(ablated), T)).mean(0)
    ref = ref - ref.mean()
    out = np.zeros(n)
    for c0 in range(0, n, chunk):
        s2 = (ids >= c0) & (ids < c0 + chunk)
        R = rates(binned(steps[s2], ids[s2] - c0, min(chunk, n - c0), T))
        R = R - R.mean(1, keepdims=True)
        with np.errstate(invalid="ignore", divide="ignore"):
            out[c0:c0 + chunk] = (R @ ref) / np.sqrt((R ** 2).sum(1) * (ref ** 2).sum())
    return out


def condition(seeds, pconn, strength, sizes=(20,), peak_ms=10.0, bg=BG_PSP, pulse=None,
              run_seed=0, with_similarity=False):
    """Pre-ablation run, then one post-ablation run per ablation size (the top excitatory
    encoders by pre-ablation score), for a batch of networks. The pre and post runs of a
    network share their background and initial state (``run_seed``), as Brian2's
    ``store``/``restore`` of the paper's procedure would; a standard choice.

    Returns one dict per network: pre scores, pre rates, and per size the ablated ids and
    the post scores (and, for the 20 ablated, the response similarity to the ablated neurons
    when asked)."""
    stim, _ = stimulus(peak_ms)
    b = Batch(seeds, pconn, bg_psp=bg)
    st, ii = b.run(stim, strength, seed=run_seed, pulse=pulse)
    pre = [scores(s, l, N, stim) for s, l in split(st, ii, b.K)]
    out = [{"seed": sd, "pconn": pconn, "strength": strength, "pre": pre[k],
            "rate_pre": mean_rate(split(st, ii, b.K)[k][1], N), "post": {}, "ablated": {}, "sim": {}}
           for k, sd in enumerate(seeds)]
    pre_spikes = split(st, ii, b.K)
    for n_abl in sizes:
        abl = [np.argsort(-p[:NEXC], kind="stable")[:n_abl] for p in pre]
        if n_abl == 0:  # nothing removed: the repeated run, with the same seed, is the pre run
            for k in range(b.K):
                out[k]["post"][0] = pre[k].copy()
                out[k]["ablated"][0] = abl[k]
            continue
        b.ablate(abl)
        st2, ii2 = b.run(stim, strength, seed=run_seed, pulse=pulse)
        for k, (s, l) in enumerate(split(st2, ii2, b.K)):
            out[k]["post"][n_abl] = scores(s, l, N, stim)
            out[k]["ablated"][n_abl] = abl[k]
            if with_similarity and n_abl == 20:
                out[k]["sim"][n_abl] = similarity(*pre_spikes[k], abl[k])
    return out


def pre_only(seeds, pconn, strength, peak_ms=10.0, bg=BG_PSP, run_seed=0, duration=DURATION):
    """Scores and rates of one run without ablation (calibration sweeps)."""
    stim, _ = stimulus(peak_ms, duration=duration)
    b = Batch(seeds, pconn, bg_psp=bg)
    st, ii = b.run(stim, strength, seed=run_seed, duration=duration)
    return [{"seed": sd, "pconn": pconn, "strength": strength, "peak": peak_ms,
             "pre": scores(s, l, N, stim), "rate_pre": mean_rate(l, N, duration)}
            for sd, (s, l) in zip(seeds, split(st, ii, b.K))]


def _job(kw):
    kind = kw.pop("kind")
    return (condition if kind == "condition" else pre_only)(**kw)


def run_jobs(jobs, workers=4):
    """Run a list of job dicts (``kind`` "condition" or "pre_only", then their arguments),
    one network per job, in ``workers`` processes; returns the per-network dicts in order."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return [r for out in ex.map(_job, [dict(j) for j in jobs]) for r in out]


def spared(d, size, thresh=0.1, pop="all"):
    """Neurons with score above ``thresh`` before or after ablation, ablated neurons left
    out (Methods); ``pop`` "all" or "exc" (excitatory only)."""
    pre, post = d["pre"], d["post"][size]
    m = (pre > thresh) | (post > thresh)
    m[d["ablated"][size]] = False
    if pop == "exc":
        m[NEXC:] = False
    return m


def effect(results, size, thresh=0.1, pop="all"):
    """Per network: median pre and post score of the spared neurons, their number, and the
    summed pre-ablation score of the ablated neurons."""
    rows = []
    for d in results:
        m = spared(d, size, thresh, pop)
        rows.append({"seed": d["seed"], "n": int(m.sum()),
                     "pre": float(np.median(d["pre"][m])) if m.any() else np.nan,
                     "post": float(np.median(d["post"][size][m])) if m.any() else np.nan,
                     "net_ablated": float(d["pre"][d["ablated"][size]].sum())})
    return rows
