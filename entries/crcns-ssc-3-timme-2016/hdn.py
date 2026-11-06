"""Loading and measures for CRCNS ssc-3, as used by Timme et al. (2016).

Timme NM, Ito S, Myroshnychenko M, Nigam S, Shimono M, Yeh F-C, Hottowy P, Litke AM, Beggs JM
(2016). High-degree neurons feed cortical computations. PLoS Comput Biol 12(5): e1004858,
doi:10.1371/journal.pcbi.1004858. Data: CRCNS ssc-3, doi:10.6080/K07D2S2F.

The data set is one archive, `ssc-3/live/data.tar.gz` in the public CRCNS bucket, holding 25
MATLAB files (`data/DataSet<n>.mat`), each with a structure `data`: spike times per neuron in
ms (`spikes`), `nNeurons`, `recordinglength` (ms), neuron positions `x` and `y` (um) and a
`recordingID`. CRCNS data sets are not versioned; the MD5 sum of the archive from the data set's
`checksums.md5` is `DATA_MD5`, and `load_all` checks the bytes it streamed against it. The archive
is streamed and decompressed in memory; nothing is written to disk.

Where each parameter comes from. "Paper" is the version of record (PMC4861348); its displayed
equations, lost from the flattened text under paper/, were read from the version of record's
JATS XML (Europe PMC). "[44]" is Timme et al. (2014), PLoS One 9: e115764 (PMC4275261), whose TE
networks the paper says it reused ("The complete procedure for the TE analysis is described in
[44]", Methods, Effective Connectivity Detection, paragraph 1; "we used these same TE networks",
paragraph 4).

- `TIME_SCALES`: bins of 1.6 and 3.5 ms with interaction delays of 1.6 to 6.4 and 3.5 to 14 ms
  (paper, Effective Connectivity Detection, paragraph 4; [44], Table 1, time scales 2 and 3:
  bin 1.6 ms, d = 1, delay window 1 to 4 bins, jitter window 11.2 ms; bin 3.5 ms, d = 1, delay
  window 1 to 4 bins, jitter window 24.5 ms).
- TE states ([44], Transfer Entropy Analysis, paragraph 3): binary spike trains; the past state
  of both the sender and the receiver is the OR of two adjacent bins ("a spike in either or both
  time bins yielded an overall state of 1"). Which two bins: [44]'s text writes i_{t-d} and
  i_{t-d-1}, which for d = 1 gives bins t-1 and t-2 and delays of 0 to 2 bins; its Table 1 and
  the paper give a delay window of 1 to 4 bins (1.6 to 6.4 ms), which bins t-2 and t-3 give
  (a spike in bin t-3 and one in bin t are 2 to 4 bins apart, in t-2 and t 1 to 3 bins).
  `PAST_BINS = (2, 3)` follows the stated delay window, the version both papers give in numbers
  (an assumption, recorded in the attempt). The future state is one bin, t.
- Normalized TE is TE over the entropy of the receiver's future state (paper, Eq 4).
- Significance (paper, paragraph 5, and [44], paragraph 6 of Transfer Entropy Analysis): the
  sender's spikes are jittered uniformly over a window of seven bins centred on each spike
  (`JITTER_HALF_BINS = 3`); 5000 surrogates; significant when fewer than 5 surrogates give a TE
  greater than the real one. [44] states that the jitter preserved the number of past states
  equal to 1; `n(s'=1)` is held at its real value in each surrogate, as that sentence says. The
  test stops early once 5 surrogates exceed the real TE, which cannot change the decision.
  For pairs whose jitter moves more than `exact_max` (50 in the notebook) relevant sender spikes,
  the surrogate counts are drawn from a normal distribution with their exact moments in place of
  jittering every spike: a deviation, made for the time limit, whose agreement with the full
  jitter the notebook shows on two recordings.
- Sub-networks ([44], Topology Analysis - Sub-Networks, paragraph 2; paper, paragraph 5): 50
  neurons drawn at random; neurons without a connection inside the group are replaced from the
  pool until all have one; then only the k*N/2 = 75 strongest connections by normalized TE are
  kept. `SUBNET_N`, `SUBNET_K`, `N_SUBNETS`.
- PID ("Williams and Beer"; paper, Eqs 5 to 10): redundancy is I_min conditioned on I_P in the
  form of Eq 8 (specific information of R together with I_P minus that of I_P alone, minimum over
  the two sources, weighted by p(i_F)); unique terms are the bivariate TE minus the redundancy;
  synergy is the TE of the pair minus the other three. Normalized by H(I_F) (paper, last
  sentence of the paragraph after Eq 10). The past states of the two senders are the same
  binned, OR'ed states as for the TE ("The binning and delay methods for the PID multivariate TE
  were identical to the bivariate TE analysis").
- Information gain (paper, Eq 12): TE of n senders jointly minus the TE of n - 1 of them,
  averaged over the n choices of the sender left out; all combinations of n inputs or 100
  sampled ones, whichever is fewer; n up to 6 (paper, Methods, paragraph after Eq 11).
- Random seeds are standard choices; they cannot change a result beyond sampling noise.
"""

from __future__ import annotations

import hashlib
import itertools
import io
import math
import re
import tarfile

import fsspec
import numba as nb
import numpy as np
import scipy.io

DATASET = "ssc-3"
DATASET_DOI = "10.6080/K07D2S2F"
DATASET_VERSION = "unversioned"
DATA_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-3/live/data.tar.gz"
DATA_MD5 = "1a5bd3d304c5442290a7c9c1f1b5def6"   # ssc-3/live/checksums.md5

TIME_SCALES = {"1.6-6.4 ms": 1.6, "3.5-14 ms": 3.5}   # bin size in ms ([44], Table 1)
PAST_BINS = (2, 3)
JITTER_HALF_BINS = 3
N_SURROGATES = 5000
MAX_EXCEED = 5            # significant when fewer than 5 of 5000 surrogates exceed (p < 0.001)
SUBNET_N, SUBNET_K, N_SUBNETS = 50, 3, 500


# ---------------------------------------------------------------- loading

def load_all():
    """Stream data.tar.gz and return one dict per recording, in data set order (1 to 25)."""
    md5 = hashlib.md5()

    class Hashing(io.RawIOBase):
        def __init__(self, f):
            self.f = f

        def readable(self):
            return True

        def readinto(self, b):
            chunk = self.f.read(len(b))
            md5.update(chunk)
            b[:len(chunk)] = chunk
            return len(chunk)

    raw = {}
    with fsspec.open(DATA_URL, block_size=2**22).open() as f:
        stream = io.BufferedReader(Hashing(f), buffer_size=2**22)
        with tarfile.open(fileobj=stream, mode="r|gz") as tf:
            for m in tf:
                if m.isfile() and m.name.endswith(".mat"):
                    raw[m.name] = tf.extractfile(m).read()
        while stream.read(2**22):
            pass
    recs = []
    for name in sorted(raw, key=lambda s: int(re.search(r"DataSet(\d+)", s).group(1))):
        d = scipy.io.loadmat(io.BytesIO(raw[name]), squeeze_me=True, struct_as_record=False)["data"]
        recs.append({
            "name": re.search(r"(DataSet\d+)", name).group(1),
            "recording_id": str(d.recordingID),
            "n_neurons_field": int(d.nNeurons),
            "length_ms": float(d.recordinglength),
            "timescale": str(d.timescale),
            "sampling": str(d.samplingfrequency),
            "spikes": [np.atleast_1d(np.asarray(s, dtype=float)) for s in d.spikes],
            "x": np.asarray(d.x, float), "y": np.asarray(d.y, float),
        })
    return recs, md5.hexdigest()


def bin_trains(spikes, bin_ms, length_ms):
    """Binary spike trains as sorted unique bin indices, and the number of bins."""
    T = int(math.ceil(length_ms / bin_ms))
    out = nb.typed.List()
    for s in spikes:
        b = np.unique(np.floor(s / bin_ms).astype(np.int64))
        out.append(b[(b >= 0) & (b < T)])
    return out, T


# ---------------------------------------------------------------- TE network

@nb.njit(cache=True)
def _xlogy(n, num, den, N):
    if n <= 0:
        return 0.0
    return n / N * math.log2(num / den)


@nb.njit(cache=True)
def te_from_counts(N, R1, P1, RP, S1, a, b, c):
    """TE (bits) from the counts of the 2x2x2 table of receiver future r, receiver past r' and
    sender past s'. R1 = n(r), P1 = n(r'), RP = n(r, r'), S1 = n(s'), a = n(r, s'),
    b = n(r', s'), c = n(r, r', s')."""
    te = 0.0
    for rp in range(2):
        for sp in range(2):
            # n(r', s') and n(r=1, r', s')
            if rp == 1 and sp == 1:
                n_ps, n1 = b, c
            elif rp == 1 and sp == 0:
                n_ps, n1 = P1 - b, RP - c
            elif rp == 0 and sp == 1:
                n_ps, n1 = S1 - b, a - c
            else:
                n_ps, n1 = N - P1 - S1 + b, (R1 - RP) - (a - c)
            n_p = P1 if rp == 1 else N - P1
            n_p1 = RP if rp == 1 else R1 - RP
            n0 = n_ps - n1
            if n1 > 0:
                te += n1 / N * math.log2((n1 / n_ps) / (n_p1 / n_p))
            if n0 > 0:
                te += n0 / N * math.log2((n0 / n_ps) / ((n_p - n_p1) / n_p))
    return te


@nb.njit(cache=True)
def _rng(state):
    # xorshift64*; state is a one-element uint64 array; returns 64 random bits
    x = state[0]
    x ^= x >> np.uint64(12)
    x ^= x << np.uint64(25)
    x ^= x >> np.uint64(27)
    state[0] = x
    return x * np.uint64(2685821657736338717)


@nb.njit(cache=True)
def _u7(bits32):
    # uniform integer 0..6 from 32 random bits (multiply-shift; bias below 2e-9)
    return np.int64((bits32 * np.uint64(7)) >> np.uint64(32))


@nb.njit(parallel=True, cache=True)
def te_network(trains, T, n_surr, max_exceed, seed, exact_max):
    """TE from every sender (row) to every receiver (column), its normalized value, the number of
    surrogates run and the number that exceeded the real TE.

    In a surrogate each sender spike moves by u, uniform on -3..3 bins. A spike can change the
    counts a, b, c only if the receiver's future or past state is 1 somewhere in the bins it can
    cover; only those spikes are jittered explicitly. A spike more than 7 bins from any other such
    spike covers bins no other spike can reach, so its contribution for each u is tabulated once;
    spikes closer together are jittered together and their covered bins merged (the OR of the
    past state)."""
    n = len(trains)
    p0, p1 = 2, 3                      # PAST_BINS
    J = 3                              # JITTER_HALF_BINS
    W = 2 * J + 1
    t0 = 3                             # first bin with a full past
    N = T - t0
    te = np.zeros((n, n))
    nte = np.zeros((n, n))
    ran = np.zeros((n, n), np.int32)
    exceed = np.zeros((n, n), np.int32)
    S1 = np.zeros(n, np.int64)
    for s in range(n):
        tr = trains[s]
        last = -10
        cnt = 0
        for k in range(len(tr)):
            for d in (p0, p1):
                t = tr[k] + d
                if t >= t0 and t < T and t > last:
                    cnt += 1
                    last = t
        S1[s] = cnt
    for r in nb.prange(n):
        rF = np.zeros(T + 16, np.uint8)
        rP = np.zeros(T + 16, np.uint8)
        rel = np.zeros(T + 16, np.uint8)
        stamp = np.zeros(T + 16, np.int32)
        tr = trains[r]
        for k in range(len(tr)):
            rF[tr[k]] = 1
            for d in (p0, p1):
                if tr[k] + d < T:
                    rP[tr[k] + d] = 1
        R1 = 0
        P1 = 0
        RP = 0
        for t in range(t0, T):
            R1 += rF[t]
            P1 += rP[t]
            RP += rF[t] & rP[t]
        HF = 0.0
        q = R1 / N
        if 0 < q < 1:
            HF = -(q * math.log2(q) + (1 - q) * math.log2(1 - q))
        for t in range(t0, T):
            if rF[t] or rP[t]:
                lo = max(t - (p1 + J), 0)
                hi = min(t - (p0 - J), T - 1)
                for p in range(lo, hi + 1):
                    rel[p] = 1
        st = 0
        for s in range(n):
            if s == r:
                continue
            ts = trains[s]
            relp = np.empty(len(ts), np.int64)
            m = 0
            for k in range(len(ts)):
                if rel[ts[k]]:
                    relp[m] = ts[k]
                    m += 1
            # real counts
            st += 1
            a = 0
            b = 0
            c = 0
            for k in range(m):
                for d in (p0, p1):
                    t = relp[k] + d
                    if t >= t0 and t < T and stamp[t] != st:
                        stamp[t] = st
                        a += rF[t]
                        b += rP[t]
                        c += rF[t] & rP[t]
            real = te_from_counts(N, R1, P1, RP, S1[s], a, b, c)
            te[s, r] = real
            nte[s, r] = real / HF if HF > 0 else 0.0
            # isolated spikes: table of packed (a, b, c) per u; others: explicit groups
            tab = np.empty((m, W), np.int64)
            n_iso = 0
            base = np.int64(0)
            grp = np.empty(m + 1, np.int64)
            gp = np.empty(m, np.int64)
            n_g = 0
            n_gp = 0
            k = 0
            while k < m:
                e = k
                while e + 1 < m and relp[e + 1] - relp[e] <= 2 * J + 1:
                    e += 1
                if e == k:
                    p = relp[k]
                    same = True
                    for ui in range(W):
                        v = np.int64(0)
                        for d in (p0, p1):
                            t = p + ui - J + d
                            if t >= t0 and t < T:
                                v += np.int64(rF[t]) + (np.int64(rP[t]) << 20) + (np.int64(rF[t] & rP[t]) << 40)
                        tab[n_iso, ui] = v
                        if v != tab[n_iso, 0]:
                            same = False
                    if same:
                        base += tab[n_iso, 0]
                    else:
                        n_iso += 1
                else:
                    grp[n_g] = n_gp
                    n_g += 1
                    for kk in range(k, e + 1):
                        gp[n_gp] = relp[kk]
                        n_gp += 1
                k = e + 1
            grp[n_g] = n_gp
            state = np.empty(1, np.uint64)
            state[0] = np.uint64(seed) * np.uint64(1000003) + np.uint64(s * 100003 + r + 1) * np.uint64(7919)
            for _ in range(10):
                _rng(state)
            mask = np.uint64(0xFFFFFFFF)
            nex = 0
            k_run = 0
            if n_iso + n_gp > exact_max:
                # Gaussian null: the jittered counts are a sum of many independent spike
                # contributions; take their exact mean and covariance (isolated spikes) plus
                # those of the merged groups from 50 joint draws, and draw (a, b, c) from the
                # normal with these moments.
                mu = np.zeros(3)
                cov = np.zeros((3, 3))
                mu[0] = base & 0xFFFFF
                mu[1] = (base >> 20) & 0xFFFFF
                mu[2] = base >> 40
                v = np.zeros(3)
                for i in range(n_iso):
                    m1 = np.zeros(3)
                    m2 = np.zeros((3, 3))
                    for ui in range(W):
                        x0 = tab[i, ui]
                        v[0] = x0 & 0xFFFFF
                        v[1] = (x0 >> 20) & 0xFFFFF
                        v[2] = x0 >> 40
                        for p_ in range(3):
                            m1[p_] += v[p_] / W
                            for q_ in range(3):
                                m2[p_, q_] += v[p_] * v[q_] / W
                    for p_ in range(3):
                        mu[p_] += m1[p_]
                        for q_ in range(3):
                            cov[p_, q_] += m2[p_, q_] - m1[p_] * m1[q_]
                if n_g > 0:
                    K = 50
                    g1 = np.zeros(3)
                    g2 = np.zeros((3, 3))
                    for it in range(K):
                        v[:] = 0.0
                        for g in range(n_g):
                            st += 1
                            for kk in range(grp[g], grp[g + 1]):
                                u = _u7(_rng(state) & mask) - J
                                for d in (p0, p1):
                                    t = gp[kk] + u + d
                                    if t >= t0 and t < T and stamp[t] != st:
                                        stamp[t] = st
                                        v[0] += rF[t]
                                        v[1] += rP[t]
                                        v[2] += rF[t] & rP[t]
                        for p_ in range(3):
                            g1[p_] += v[p_] / K
                            for q_ in range(3):
                                g2[p_, q_] += v[p_] * v[q_] / K
                    for p_ in range(3):
                        mu[p_] += g1[p_]
                        for q_ in range(3):
                            cov[p_, q_] += (g2[p_, q_] - g1[p_] * g1[q_]) * K / (K - 1)
                # matrix square root through the eigendecomposition (cov may be singular)
                w, V = np.linalg.eigh(cov)
                L = np.zeros((3, 3))
                for p_ in range(3):
                    sw = math.sqrt(w[p_]) if w[p_] > 0 else 0.0
                    for q_ in range(3):
                        L[q_, p_] = V[q_, p_] * sw
                z = np.zeros(3)
                for it in range(n_surr):
                    for p_ in range(3):
                        u1 = ((_rng(state) >> np.uint64(11)) + np.uint64(1)) * (1.0 / 9007199254740993.0)
                        u2 = (_rng(state) >> np.uint64(11)) * (1.0 / 9007199254740992.0)
                        z[p_] = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
                    av = mu[0] + L[0, 0] * z[0] + L[0, 1] * z[1] + L[0, 2] * z[2]
                    bv = mu[1] + L[1, 0] * z[0] + L[1, 1] * z[1] + L[1, 2] * z[2]
                    cv = mu[2] + L[2, 0] * z[0] + L[2, 1] * z[1] + L[2, 2] * z[2]
                    a = max(np.int64(round(av)), 0)
                    b = max(np.int64(round(bv)), 0)
                    c = min(max(np.int64(round(cv)), 0), a, b, RP)
                    a = min(a, R1)
                    b = min(b, P1, S1[s])
                    a = min(a, S1[s])
                    c = min(c, a, b)
                    k_run += 1
                    if te_from_counts(N, R1, P1, RP, S1[s], a, b, c) > real:
                        nex += 1
                        if nex >= max_exceed:
                            break
                ran[s, r] = k_run
                exceed[s, r] = nex
                continue
            for it in range(n_surr):
                tot = base
                for i in range(0, n_iso - 1, 2):
                    x = _rng(state)
                    tot += tab[i, _u7(x & mask)] + tab[i + 1, _u7(x >> np.uint64(32))]
                if n_iso % 2 == 1:
                    tot += tab[n_iso - 1, _u7(_rng(state) & mask)]
                a = tot & 0xFFFFF
                b = (tot >> 20) & 0xFFFFF
                c = tot >> 40
                for g in range(n_g):
                    st += 1
                    for kk in range(grp[g], grp[g + 1]):
                        u = _u7(_rng(state) & mask) - J
                        for d in (p0, p1):
                            t = gp[kk] + u + d
                            if t >= t0 and t < T and stamp[t] != st:
                                stamp[t] = st
                                a += rF[t]
                                b += rP[t]
                                c += rF[t] & rP[t]
                k_run += 1
                if te_from_counts(N, R1, P1, RP, S1[s], a, b, c) > real:
                    nex += 1
                    if nex >= max_exceed:
                        break
            ran[s, r] = k_run
            exceed[s, r] = nex
    return te, nte, ran, exceed


def significant(exceed):
    """Significant connections: fewer than MAX_EXCEED surrogates above the real TE."""
    sig = exceed < MAX_EXCEED
    np.fill_diagonal(sig, False)
    return sig


# ---------------------------------------------------------------- sub-networks

def subnetworks(sig, nte, rng, n_sub=N_SUBNETS, size=SUBNET_N, k=SUBNET_K, max_tries=10**5):
    """Sub-networks as in [44] (Topology Analysis - Sub-Networks): `size` neurons at random;
    a neuron with no significant connection (either direction) to the others is replaced by a
    random neuron from the pool until all have one; then the k*size/2 strongest connections by
    normalized TE are kept. Returns a list of (neurons, senders, receivers) in recording indices,
    and the number of restarts."""
    n = sig.shape[0]
    und = sig | sig.T
    out = []
    restarts = 0
    n_keep = k * size // 2
    while len(out) < n_sub:
        if restarts > max_tries:
            break
        perm = rng.permutation(n)
        group, pool = list(perm[:size]), list(perm[size:])
        ok = False
        for _ in range(10 * size):
            g = np.array(group)
            deg = und[np.ix_(g, g)].sum(1)
            lone = np.flatnonzero(deg == 0)
            if len(lone) == 0:
                ok = True
                break
            # replace one unconnected neuron by a pool neuron connected to the group, if any
            cand = [p for p in pool if und[p, g].any()]
            if not cand:
                break
            new = cand[rng.integers(len(cand))]
            old = lone[rng.integers(len(lone))]
            pool.remove(new)
            pool.append(group[old])
            group[old] = new
        if not ok:
            restarts += 1
            continue
        g = np.array(group)
        s_idx, r_idx = np.nonzero(sig[np.ix_(g, g)])
        w = nte[g[s_idx], g[r_idx]]
        order = np.argsort(-w, kind="stable")[:n_keep]
        out.append((g, g[s_idx[order]], g[r_idx[order]]))
    return out, restarts


# ---------------------------------------------------------------- PID and multivariate TE

def past_sets(trains, T):
    """For each neuron the sorted bins t (t0 <= t < T) whose past state is 1."""
    out = nb.typed.List()
    for tr in trains:
        s = np.unique(np.concatenate([tr + d for d in PAST_BINS]))
        out.append(s[(s >= 3) & (s < T)])
    return out


@nb.njit(cache=True)
def _receiver_arrays(tr, T):
    rF = np.zeros(T + 8, np.uint8)
    rP = np.zeros(T + 8, np.uint8)
    for k in range(len(tr)):
        rF[tr[k]] = 1
        for d in (2, 3):
            if tr[k] + d < T:
                rP[tr[k] + d] = 1
    base = np.zeros((2, 2), np.int64)
    for t in range(3, T):
        base[rF[t], rP[t]] += 1
    return rF, rP, base


@nb.njit(cache=True)
def _te_table(n):
    """TE (bits) and H(I_F) from counts n[iF, iP, x]."""
    nf = n.shape[2]
    N = n.sum()
    te = 0.0
    nP = np.zeros(2)
    nFP = np.zeros((2, 2))
    for f in range(2):
        for p in range(2):
            for x in range(nf):
                nP[p] += n[f, p, x]
                nFP[f, p] += n[f, p, x]
    for p in range(2):
        for x in range(nf):
            nPX = n[0, p, x] + n[1, p, x]
            for f in range(2):
                v = n[f, p, x]
                if v > 0:
                    te += v / N * math.log2(v * nP[p] / (nPX * nFP[f, p]))
    q = (nFP[1, 0] + nFP[1, 1]) / N
    H = 0.0
    if 0 < q < 1:
        H = -(q * math.log2(q) + (1 - q) * math.log2(1 - q))
    return te, H


@nb.njit(cache=True)
def _joint_counts(rF, rP, base, sets, idx, code, touched):
    """Counts n[iF, iP, x] with x the joint past state of the senders sets[idx[i]] (bit i)."""
    m = len(idx)
    n = np.zeros((2, 2, 1 << m))
    nt = 0
    for i in range(m):
        s = sets[idx[i]]
        for k in range(len(s)):
            t = s[k]
            if code[t] == 0:
                touched[nt] = t
                nt += 1
            code[t] |= 1 << i
    for f in range(2):
        for p in range(2):
            n[f, p, 0] = base[f, p]
    for k in range(nt):
        t = touched[k]
        f = rF[t]
        p = rP[t]
        n[f, p, code[t]] += 1
        n[f, p, 0] -= 1
        code[t] = 0
    return n


@nb.njit(cache=True)
def pid_from_table(n):
    """Williams-Beer PID of the multivariate TE {J, K} -> I from counts n[iF, iP, x], x = j + 2k
    (paper, Eqs 5 to 10). Returns synergy, redundancy, unique J, unique K, TE(J), TE(K),
    TE({J,K}), H(I_F), all in bits."""
    N = n.sum()
    p = n / N
    pJ = np.zeros((2, 2, 2))
    pK = np.zeros((2, 2, 2))
    for f in range(2):
        for q in range(2):
            for x in range(4):
                pJ[f, q, x & 1] += p[f, q, x]
                pK[f, q, x >> 1] += p[f, q, x]
    teJK, H = _te_table(n)
    teJ, _ = _te_table(pJ * N)
    teK, _ = _te_table(pK * N)
    pF = np.zeros(2)
    pFP = np.zeros((2, 2))
    pPp = np.zeros(2)
    for f in range(2):
        for q in range(2):
            for x in range(4):
                pF[f] += p[f, q, x]
                pFP[f, q] += p[f, q, x]
                pPp[q] += p[f, q, x]
    red = 0.0
    for f in range(2):
        if pF[f] <= 0:
            continue
        # I_spec(I_F = f; I_P)
        isp = 0.0
        for q in range(2):
            if pFP[f, q] > 0:
                isp += pFP[f, q] / pF[f] * math.log2(pFP[f, q] / (pPp[q] * pF[f]))
        best = 1e300
        for src in range(2):
            pr = pJ if src == 0 else pK
            v = 0.0
            for q in range(2):
                for x in range(2):
                    pj = pr[f, q, x]
                    if pj > 0:
                        v += pj / pF[f] * math.log2(pj / ((pr[0, q, x] + pr[1, q, x]) * pF[f]))
            v -= isp
            if v < best:
                best = v
        red += pF[f] * best
    uJ = teJ - red
    uK = teK - red
    syn = teJK - red - uJ - uK
    return syn, red, uJ, uK, teJ, teK, teJK, H


@nb.njit(parallel=True, cache=True)
def pid_triples(trains, sets, T, recv, js, ks):
    """PID of every triple (js[i], ks[i]) -> recv[i]; triples must be sorted by receiver.
    Returns an array (n, 8) of pid_from_table's outputs."""
    n = len(recv)
    out = np.zeros((n, 8))
    starts = [0]
    for i in range(1, n):
        if recv[i] != recv[i - 1]:
            starts.append(i)
    starts.append(n)
    ng = len(starts) - 1
    st = np.array(starts)
    for g in nb.prange(ng):
        r = recv[st[g]]
        rF, rP, base = _receiver_arrays(trains[r], T)
        code = np.zeros(T + 8, np.int64)
        touched = np.empty(T + 8, np.int64)
        idx = np.empty(2, np.int64)
        for i in range(st[g], st[g + 1]):
            idx[0] = js[i]
            idx[1] = ks[i]
            tab = _joint_counts(rF, rP, base, sets, idx, code, touched)
            res = pid_from_table(tab)
            for k in range(8):
                out[i, k] = res[k]
    return out


@nb.njit(cache=True)
def _te_drop(n, m, drop):
    """TE of all senders but `drop` from the joint table n over m senders."""
    nn = np.zeros((2, 2, 1 << (m - 1)))
    for x in range(1 << m):
        lo = x & ((1 << drop) - 1)
        hi = x >> (drop + 1)
        y = lo | (hi << drop)
        for f in range(2):
            for q in range(2):
                nn[f, q, y] += n[f, q, x]
    te, _ = _te_table(nn)
    return te


@nb.njit(parallel=True, cache=True)
def info_gain(trains, sets, T, recv, combos, n_in):
    """Information gain (paper, Eq 12) for each combination of senders: TE of all n_in senders
    minus the TE without one of them, averaged over the n_in senders left out; in bits and
    normalized by H(I_F). `combos` is (k, n_in), rows sorted by `recv`."""
    k = combos.shape[0]
    out = np.zeros((k, 2))
    starts = [0]
    for i in range(1, k):
        if recv[i] != recv[i - 1]:
            starts.append(i)
    starts.append(k)
    st = np.array(starts)
    for g in nb.prange(len(st) - 1):
        r = recv[st[g]]
        rF, rP, base = _receiver_arrays(trains[r], T)
        code = np.zeros(T + 8, np.int64)
        touched = np.empty(T + 8, np.int64)
        for i in range(st[g], st[g + 1]):
            tab = _joint_counts(rF, rP, base, sets, combos[i], code, touched)
            te_all, H = _te_table(tab)
            v = 0.0
            if n_in == 1:
                v = te_all
            else:
                for d in range(n_in):
                    v += (te_all - _te_drop(tab, n_in, d)) / n_in
            out[i, 0] = v
            out[i, 1] = v / H if H > 0 else 0.0
    return out


# ---------------------------------------------------------------- per-recording analysis

N_FULL_TRIPLES = 3000      # reading (f): triples sampled per recording and time scale (time limit)
N_GAIN_RECEIVERS = 30      # Fig 6: receivers sampled per recording and time scale (time limit)
N_GAIN_COMBOS = 20         # Fig 6: combinations per receiver and n (paper: 100; time limit)
MAX_INPUTS = 6             # Fig 6: up to six inputs (paper)


def _triples_from_edges(senders, receivers):
    """All (receiver, sender j, sender k) with j < k both sending to the receiver."""
    out = []
    by_r = {}
    for s, r in zip(senders, receivers):
        by_r.setdefault(int(r), []).append(int(s))
    for r, ins in by_r.items():
        ins = sorted(ins)
        for a in range(len(ins)):
            for b in range(a + 1, len(ins)):
                out.append((r, ins[a], ins[b]))
    return out


def analyse_recording(trains, T, sig, nte, seed):
    """Sub-networks, synergy of every triple (readings s and f) and information gains."""
    rng = np.random.default_rng(seed)
    sets = past_sets(trains, T)
    subs, restarts = subnetworks(sig, nte, rng)
    # reading (s): triples inside each sub-network, degrees counted inside it
    rows = []
    for si, (g, s_e, r_e) in enumerate(subs):
        indeg = {}
        outdeg = {}
        for s, r in zip(s_e, r_e):
            indeg[int(r)] = indeg.get(int(r), 0) + 1
            outdeg[int(s)] = outdeg.get(int(s), 0) + 1
        for r, j, k in _triples_from_edges(s_e, r_e):
            rows.append((si, r, j, k, indeg[r], outdeg[j], outdeg[k]))
    sub_tr = np.array(rows, dtype=np.int64).reshape(-1, 7)
    # reading (f): triples of the full network, sampled
    s_all, r_all = np.nonzero(sig)
    indeg_f = sig.sum(0)
    outdeg_f = sig.sum(1)
    w = np.array([indeg_f[r] * (indeg_f[r] - 1) / 2 for r in range(sig.shape[0])], float)
    n_full_total = int(w.sum())
    full = set()
    if n_full_total <= N_FULL_TRIPLES:
        full = set(_triples_from_edges(s_all, r_all))
    else:
        while len(full) < N_FULL_TRIPLES:
            r = int(rng.choice(len(w), p=w / w.sum()))
            ins = np.flatnonzero(sig[:, r])
            j, k = sorted(rng.choice(ins, 2, replace=False))
            full.add((r, int(j), int(k)))
    full_tr = np.array(sorted(full), dtype=np.int64).reshape(-1, 3)
    # PID of every distinct triple
    keys = set(map(tuple, sub_tr[:, 1:4].tolist())) | set(map(tuple, full_tr.tolist()))
    keys = np.array(sorted(keys), dtype=np.int64).reshape(-1, 3)
    pid = pid_triples(trains, sets, T, keys[:, 0], keys[:, 1], keys[:, 2]) if len(keys) else np.zeros((0, 8))
    syn = {tuple(k): (p[0] / p[7] if p[7] > 0 else 0.0) for k, p in zip(keys.tolist(), pid)}
    # information gain, reading (f)
    cand = np.flatnonzero(indeg_f >= 1)
    pick = np.sort(rng.choice(cand, min(N_GAIN_RECEIVERS, len(cand)), replace=False)) if len(cand) else cand
    gains = {}
    for n_in in range(1, MAX_INPUTS + 1):
        recv, combos = [], []
        for r in pick:
            ins = np.flatnonzero(sig[:, r])
            if len(ins) < n_in:
                continue
            if math.comb(len(ins), n_in) <= N_GAIN_COMBOS:
                import itertools
                cs = [list(c) for c in itertools.combinations(ins, n_in)]
            else:
                cs = [sorted(rng.choice(ins, n_in, replace=False)) for _ in range(N_GAIN_COMBOS)]
            recv += [r] * len(cs)
            combos += cs
        if not recv:
            continue
        g = info_gain(trains, sets, T, np.array(recv, np.int64), np.array(combos, np.int64), n_in)
        recv = np.array(recv)
        gains[n_in] = {int(r): (g[recv == r, 0].mean(), g[recv == r, 1].mean()) for r in np.unique(recv)}
    return {"subs": subs, "restarts": restarts, "sub_triples": sub_tr, "full_triples": full_tr,
            "n_full_total": n_full_total, "syn": syn, "pid": (keys, pid), "gains": gains,
            "indeg_f": indeg_f, "outdeg_f": outdeg_f}


# ---------------------------------------------------------------- feedforward model (Fig 7, S1 Fig)
# Paper, Methods, Feedforward Network Model, and Eqs 13 to 24 (version of record). Each run is
# independent: b(t) is 0 or 1 with equal probability; input neuron i fires with the probability of
# Eqs 16-17; output neuron o receives the current of Eqs 18-19 plus I_con for each active
# connected input; firing follows Eq 13. Rewiring: 500 runs, score S(i, o) (Eq 20), the connected
# pair with the lowest score is disconnected and the unconnected pair with the highest score is
# connected; repeated N_connections times. 100 models per type.

I_CON = 10.0
MODEL_RUNS = 500
N_MODELS = 100
RULES = {   # (a1 DegIn(o), a2 DegOut(i), a3 FR(o), a4 FR(i)); paper Eqs 22 to 24
    20: {"random": None, "hebbian": (0, 0, 0, 0), "degree": (0.05, -1.75, 0, 0), "firing_rate": (0, 0, 0.35, 3.1)},
    40: {"random": None, "hebbian": (0, 0, 0, 0), "degree": (0.16, -0.3, 0, 0), "firing_rate": (0, 0, 0.35, 3.1)},
}


def sigmoid_params(n_neurons):
    """alpha and beta from Eq 14 (p(0) = 0.01) and Eq 15 (p(I_con N) = 0.5)."""
    beta = math.log(99.0)
    return beta / (I_CON * n_neurons), beta


def _current(p, alpha, beta):
    # the current that gives firing probability p under Eq 13
    return (beta + np.log(p / (1 - p))) / alpha


def simulate(conn, n_runs, rng, alpha, beta):
    """conn (M, N_in, N_out) bool. Returns b (M, R), input states (M, R, N), output states (M, R, N)."""
    M, N, _ = conn.shape
    frac = np.arange(N) / (N - 1)
    I_in = np.stack([_current(0.5 - 0.4 * frac, alpha, beta), _current(0.5 + 0.4 * frac, alpha, beta)])
    I_out = np.stack([_current(0.5 - 0.2 * frac, alpha, beta), _current(0.5 + 0.2 * frac, alpha, beta)])
    b = rng.integers(0, 2, (M, n_runs))
    p_in = 1 / (1 + np.exp(-alpha * I_in[b] + beta))
    x = rng.random((M, n_runs, N)) < p_in
    cur = I_out[b] + I_CON * np.matmul(x.astype(np.float32), conn.astype(np.float32))
    y = rng.random((M, n_runs, N)) < 1 / (1 + np.exp(-alpha * cur + beta))
    return b, x, y


def build_models(n_neurons, rule, rng, alpha, beta, n_models=N_MODELS):
    """Connectivity of n_models models of one type, after rewiring (none for 'random')."""
    N = n_neurons
    n_conn = int(round(0.2 * N * N))
    conn = np.zeros((n_models, N, N), bool)
    for m in range(n_models):
        conn[m].flat[rng.choice(N * N, n_conn, replace=False)] = True
    a = RULES[N][rule]
    if a is None:
        return conn
    for _ in range(n_conn):
        b, x, y = simulate(conn, MODEL_RUNS, rng, alpha, beta)
        xf, yf = x.astype(np.float32), y.astype(np.float32)
        xt = np.swapaxes(xf, 1, 2)
        agree = (np.matmul(xt, yf) + np.matmul(1 - xt, 1 - yf)) / MODEL_RUNS
        deg_in = conn.sum(1)[:, None, :]
        deg_out = conn.sum(2)[:, :, None]
        fr_out = yf.mean(1)[:, None, :]
        fr_in = xf.mean(1)[:, :, None]
        score = agree + a[0] * deg_in + a[1] * deg_out + a[2] * fr_out + a[3] * fr_in
        for m in range(n_models):
            s = score[m]
            on = np.flatnonzero(conn[m].ravel())
            off = np.flatnonzero(~conn[m].ravel())
            lo = on[np.argmin(s.ravel()[on])]
            hi = off[np.argmax(s.ravel()[off])]
            conn[m].flat[lo] = False
            conn[m].flat[hi] = True
    return conn


def model_correlations(conn, rng, alpha, beta, n_runs):
    """Per model: Pearson and Spearman correlations of synergy (PID of two input states about
    the output state in the same run, normalized by H(output)) with the output's in-degree and
    with each input's out-degree; mean MI between connected neurons, unconditioned and
    conditioned on b."""
    from scipy import stats
    b, x, y = simulate(conn, n_runs, rng, alpha, beta)
    out = []
    for m in range(conn.shape[0]):
        c = conn[m]
        xi, yi = x[m].astype(np.int64), y[m].astype(np.int64)
        deg_in, deg_out = c.sum(0), c.sum(1)
        syn, din, dj, dk = [], [], [], []
        for o in range(c.shape[1]):
            ins = np.flatnonzero(c[:, o])
            for j, k in itertools.combinations(ins, 2):
                code = xi[:, j] + 2 * xi[:, k] + 4 * yi[:, o]
                tab = np.zeros((2, 2, 4))
                tab[:, 0, :] = np.bincount(code, minlength=8).reshape(2, 4)
                r = pid_from_table(tab)
                syn.append(r[0] / r[7] if r[7] > 0 else 0.0)
                din.append(deg_in[o]); dj.append(deg_out[j]); dk.append(deg_out[k])
        syn = np.array(syn)
        res = {}
        for name, f in [("p", stats.pearsonr), ("r", stats.spearmanr)]:
            res["in_" + name] = f(din, syn)[0] if len(syn) > 2 and np.ptp(din) > 0 else np.nan
            xo, so = np.r_[dj, dk], np.r_[syn, syn]
            res["out_" + name] = f(xo, so)[0] if len(so) > 2 and np.ptp(xo) > 0 else np.nan
        mi_u, mi_c = [], []
        for i, o in zip(*np.nonzero(c)):
            mi_u.append(_mi2(x[m, :, i], y[m, :, o]))
            mi_c.append(sum((b[m] == v).mean() * _mi2(x[m, b[m] == v, i], y[m, b[m] == v, o]) for v in (0, 1)))
        res["mi"] = np.mean(mi_u)
        res["mi_given_b"] = np.mean(mi_c)
        res["upper_half_fraction"] = c[c.shape[0] // 2:].sum() / c.sum()
        out.append(res)
    return out


def _mi2(u, v):
    p = np.bincount(u.astype(np.int64) * 2 + v.astype(np.int64), minlength=4).reshape(2, 2) / len(u)
    pu, pv = p.sum(1, keepdims=True), p.sum(0, keepdims=True)
    k = p > 0
    return float((p[k] * np.log2(p[k] / (pu @ pv)[k])).sum())
