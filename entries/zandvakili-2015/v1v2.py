"""Loading and measures for CRCNS v1v2-1 (Zandvakili and Kohn 2015, Neuron 87, 827-839).

The data set is one zip, ``v1v2-1/live/v1-v2_gratings.zip`` in the public S3 bucket
``crcnsarchive``. It is opened in place with fsspec and zipfile, and each session's .mat member
is read into memory; nothing is written to disk.

Where each parameter comes from:

- Analysis of driven trials only, the 1.28 s grating presentations (paper, Experimental
  Procedures, Visual Stimuli; data descriptor, spikeRasters).
- Units with a mean driven rate below 0.5 sp/s are removed (Experimental Procedures, Physiology,
  "we removed units with firing rates less than 0.5 spikes/s ... averaged across all stimuli").
  The SNR >= 2 selection cannot be applied: the data set has no waveforms or SNR.
- CCG (Equation 1): coincidences summed over trials, divided by the overlap Q(tau) = T - |tau|
  and the V1 rate, computed per stimulus and combined (Pairwise V1-V2 Analysis). Combining
  is done by summing the coincidences of the eight stimuli and dividing by the summed
  normaliser, which weights each stimulus by its V1 spike count; a standard choice that keeps
  the unit of Equation 1 (coincidences per V1 spike per bin).
- Bin of 1 ms: the files hold spike times at 1 ms resolution, where the paper used 0.1 ms
  (deviation forced by the data).
- Shuffle correction: the all-trial shift predictor (cross-correlation of the PSTHs divided by
  the number of trials), per stimulus (Pairwise V1-V2 Analysis, "shuffle-corrected for
  stimulus-locked correlations").
- Jitter correction: subtract the expected CCG of jittered data (Smith and Kohn 2008, cited in
  Pairwise V1-V2 Analysis). Jitter as in the claims file's shared divergence method: each spike
  is redrawn from the spikes the neuron fired in the same window on trials of the same
  stimulus, keeping the count per window and trial. Its expectation is the trial's count in the
  window spread over the window in proportion to the PSTH; both neurons are jittered
  independently, so the expected CCG is the CCG of these expected trains. Windows tile the trial
  from 0 ms. The window is 10 ms (claims file, reading j-a, from the Figure 4C legend).
- Smoothing of the jitter-corrected CCG with a Gaussian of SD 1.5 ms; significance when the
  peak within 10 ms of zero lag exceeds 5 SD of the smoothed CCG over the flanks, 75 to 125 ms
  on both sides (Pairwise V1-V2 Analysis). Lags of +-125 ms.
- Divergence (Divergence Analysis; Results, V2 Spiking Is Preceded by Stronger V1
  Coordination): V1 state is the number of V1 units active in a 1 ms bin, divided by the
  number of V1 units; V2 spikes and V1 epochs from 50 ms after stimulus onset to the end of the
  stimulus; jitter windows tile the trial from 50 ms; Jensen-Shannon divergence in bits
  (Equations 2 and 3). The jitter draws from all trials of the stratum including the spike's
  own trial, a standard choice (one trial in 400 changes the pool little).
- Epochs at 1 ms resolution: a V1 bin at offset d holds V1 spikes d ms before the V2 spike's
  bin (d > 0 before, d < 0 after); bins d = 2 and 3, centred 2 and 3 ms before, make the
  1.5 to 3.5 ms epoch (claims file, reading e-a).
"""

import io
import zipfile

import fsspec
import numpy as np
import scipy.io as sio

DATASET = "v1v2-1"
VERSION = "unversioned"   # CRCNS data sets are not versioned (docs/archives.md); pinned by MD5
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/v1v2-1/live/v1-v2_gratings.zip"
MEMBER = "v1-v2_gratings/mat_neural_data/{}.mat"
SESSIONS = ["105l001p16", "106r001p26", "106r002p70", "107l002p67", "107l003p143"]
T_MS = 1280            # driven trial length (data descriptor; SET_CONSTS.m)
ONSET_MS = 50          # response onset for the divergence analysis (Divergence Analysis)
MIN_RATE = 0.5         # sp/s (Physiology)
MAXLAG = 125           # ms, the outer edge of the CCG flanks
JITTER_WINDOWS = [5, 10, 20, 40, 80, 1280]   # ms (Figure 6)


def open_zip():
    f = fsspec.open(URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def load_session(z, name):
    """Driven trials of one session as spike events.

    Returns a dict with, per area ('V1', 'V2'): unit codes (electrode, sort), and spike events
    as arrays (unit, trial, t) with t the ms bin 0..1279; per-trial stimulus codes 1..8; the
    blank trials' events (for the clock check); the raw rate of every unit; and rfInfo.
    """
    nd = sio.loadmat(io.BytesIO(z.read(MEMBER.format(name))))["neuralData"][0, 0]
    sr = nd["spikeRasters"]
    stim = nd["stim"].ravel().astype(int)
    driven = np.where(stim > 0)[0]
    out = {"name": name, "stim": stim[driven], "trial_id": nd["trialId"].ravel()[driven],
           "n_rows": len(stim), "row_stim": stim}
    for a, area in enumerate(["V1", "V2"]):
        ev = {"driven": [], "blank": []}
        for kind, rows in [("driven", driven), ("blank", np.where(stim == 0)[0])]:
            us, ts, trs = [], [], []
            for k, r in enumerate(rows):
                m = sr[r, a].tocoo()
                us.append(m.row); ts.append(m.col); trs.append(np.full(m.nnz, k))
                assert np.all(m.data == 1)
            ev[kind] = (np.concatenate(us).astype(np.int32), np.concatenate(trs).astype(np.int32),
                        np.concatenate(ts).astype(np.int32))
        n_units = sr[0, a].shape[0]
        rf = nd["rfInfo"][0, a]
        if rf.ndim == 2:
            rf = rf[:, :, None]
        counts = np.bincount(ev["driven"][0], minlength=n_units)
        out[area] = {"codes": nd["unitCodes"][0, a].astype(int), "events": ev["driven"],
                     "blank_events": ev["blank"], "n_units": n_units,
                     "rate": counts / (len(driven) * T_MS / 1000.0), "rf": rf}
    return out


def keep_units(sess, area):
    """Indices of units passing the 0.5 sp/s rate criterion (Physiology)."""
    return np.where(sess[area]["rate"] >= MIN_RATE)[0]


def dense(events, units, trials, n_t=T_MS):
    """Binary array (len(units), len(trials), n_t) of the given units and trials."""
    u, tr, t = events
    umap = np.full(u.max() + 1, -1)
    umap[units] = np.arange(len(units))
    tmap = np.full(tr.max() + 1, -1)
    tmap[trials] = np.arange(len(trials))
    sel = (umap[u] >= 0) & (tmap[tr] >= 0)
    x = np.zeros((len(units), len(trials), n_t), np.float32)
    x[umap[u[sel]], tmap[tr[sel]], t[sel]] = 1
    return x


def _jitter_expectation(x, window, start=0):
    """Expected trains under the jitter of the module docstring, for x (units, trials, time)."""
    n_t = x.shape[2]
    win = np.full(n_t, -1)
    win[start:] = (np.arange(n_t - start)) // window
    nw = win.max() + 1
    valid = win >= 0
    psth = x.sum(1)                                            # units, time
    wsum = np.zeros((x.shape[0], nw), np.float64)
    np.add.at(wsum.T, win[valid], psth[:, valid].T)
    p = np.zeros_like(psth, dtype=np.float64)
    denom = wsum[:, win[valid]]
    p[:, valid] = np.divide(psth[:, valid], denom, out=np.zeros_like(denom), where=denom > 0)
    cnt = np.zeros((x.shape[0], x.shape[1], nw), np.float32)
    np.add.at(cnt.transpose(2, 0, 1), win[valid], x[:, :, valid].transpose(2, 0, 1))
    xj = np.zeros_like(x)
    xj[:, :, valid] = cnt[:, :, win[valid]] * p[:, None, valid].astype(np.float32)
    return xj


def _xcorr_sum(x, nfft, chunk=100):
    """Sum over trials of the cross-correlations of all unit pairs, lags -MAXLAG..MAXLAG.

    r[i, j, tau] = sum_trials sum_t x_i(t) x_j(t + tau).
    """
    n = x.shape[0]
    nf = nfft // 2 + 1
    s = np.zeros((nf, n, n), np.complex128)
    for c in range(0, x.shape[1], chunk):
        xf = np.fft.rfft(x[:, c:c + chunk], n=nfft, axis=2).astype(np.complex64)
        xf = np.ascontiguousarray(xf.transpose(2, 0, 1))      # f, units, trials
        s += np.matmul(xf.conj(), xf.transpose(0, 2, 1))
    r = np.fft.irfft(s, n=nfft, axis=0)                        # lag, i, j
    lags = np.arange(-MAXLAG, MAXLAG + 1)
    return r[lags % nfft].transpose(1, 2, 0)


def session_ccgs(sess, jitter_windows=(10, 25)):
    """CCGs of all pairs of kept units (V1 then V2), summed over the eight stimuli.

    Returns a dict: 'units' (area label and index of each unit), 'raw', 'shuffle', 'jitter'
    (coincidence sums, units x units x lags; entry [i, j, tau] counts spikes of j at tau after
    spikes of i; 'jitter' is a dict by jitter window), 'n_spikes' per unit, 'n_trials'. The
    10 ms window is the claims file's reading j-a; 25 ms is run as a variant of reading j-b, a
    choice of this attempt (the paper gives no other window).
    """
    k1, k2 = keep_units(sess, "V1"), keep_units(sess, "V2")
    nfft = 1536                                               # >= 1280 + 125, so no wrap
    n = len(k1) + len(k2)
    L = 2 * MAXLAG + 1
    raw = np.zeros((n, n, L)); shuf = np.zeros((n, n, L))
    jit = {w: np.zeros((n, n, L)) for w in jitter_windows}
    nsp = np.zeros(n)
    for s in range(1, 9):
        trials = np.where(sess["stim"] == s)[0]
        x = np.concatenate([dense(sess["V1"]["events"], k1, trials),
                            dense(sess["V2"]["events"], k2, trials)])
        nsp += x.sum((1, 2))
        raw += _xcorr_sum(x, nfft)
        for w in jitter_windows:
            jit[w] += _xcorr_sum(_jitter_expectation(x, w), nfft)
        shuf += _xcorr_sum(x.sum(1, keepdims=True), nfft) / len(trials)
        del x
    units = [("V1", i) for i in k1] + [("V2", i) for i in k2]
    return {"units": units, "raw": raw, "shuffle": shuf, "jitter": jit, "n_spikes": nsp,
            "n_trials": len(sess["stim"])}


def normalise(c, n_spikes_first):
    """Equation 1: divide by Q(tau) = T - |tau| (as a fraction of T) and the first unit's
    spike count, giving coincidences per spike of the first unit per 1 ms bin."""
    lags = np.arange(-MAXLAG, MAXLAG + 1)
    q = (T_MS - np.abs(lags)) / T_MS
    return c / (q * n_spikes_first[..., None])


def gauss_smooth(c, sd=1.5):
    """Gaussian kernel of SD 1.5 ms along the last axis (Pairwise V1-V2 Analysis)."""
    k = np.arange(-6, 7)
    w = np.exp(-0.5 * (k / sd) ** 2)
    w /= w.sum()
    out = np.zeros_like(c)
    L = c.shape[-1]
    for kk, ww in zip(k, w):
        src = np.clip(np.arange(L) + kk, 0, L - 1)
        out += ww * c[..., src]
    return out


def significance(jc_smoothed):
    """Peak within 10 ms of zero against 5 SD of the flanks (75 to 125 ms, both sides).

    Returns (significant, peak value, peak lag in ms, flank SD)."""
    lags = np.arange(-MAXLAG, MAXLAG + 1)
    centre = np.abs(lags) <= 10
    flank = (np.abs(lags) >= 75) & (np.abs(lags) <= 125)
    seg = jc_smoothed[..., centre]
    i = np.argmax(seg, axis=-1)
    peak = np.take_along_axis(seg, i[..., None], -1)[..., 0]
    sd = jc_smoothed[..., flank].std(-1)
    return peak > 5 * sd, peak, lags[centre][i], sd


def half_width(c, lag_index):
    """Full width at half the peak height around a given peak (linear interpolation), in ms."""
    c = np.asarray(c, float)
    h = c[lag_index] / 2
    j = lag_index
    while j > 0 and c[j] > h:
        j -= 1
    left = j + (h - c[j]) / (c[j + 1] - c[j]) if c[j] <= h else float(j)
    j = lag_index
    while j < len(c) - 1 and c[j] > h:
        j += 1
    right = j - (h - c[j]) / (c[j - 1] - c[j]) if c[j] <= h else float(j)
    return right - left


# ---------------------------------------------------------------- divergence

def pop_counts(events, units, n_trials, n_t=T_MS):
    """Number of the given units active in each 1 ms bin of each trial (trials x time).

    A unit with two spikes in one bin counts once (jittered data can put two there)."""
    u, tr, t = events
    K = np.zeros(n_trials * n_t, np.int16)
    order = np.argsort(u, kind="stable")
    us = u[order]
    cells = tr[order].astype(np.int64) * n_t + t[order]
    bounds = np.searchsorted(us, units), np.searchsorted(us, units, side="right")
    seen = np.zeros(n_trials * n_t, bool)
    for a, b in zip(*bounds):
        seen[:] = False
        seen[cells[a:b]] = True
        K += seen
    return K.reshape(n_trials, n_t)


def jitter_events(events, units, stim, window, by_stim, rng, start=ONSET_MS, n_t=T_MS):
    """Jittered V1 events: windows tile [start, n_t); each spike in a window is replaced by one
    drawn with replacement from the spikes the same unit fired in that window on trials of the
    stratum (same stimulus if by_stim, else all trials). Spikes before start are kept."""
    u, tr, t = events
    sel = np.isin(u, units)
    u, tr, t = u[sel], tr[sel], t[sel]
    late = t >= start
    w = (t[late] - start) // window
    strat = stim[tr[late]] if by_stim else np.zeros(late.sum(), int)
    g = (u[late].astype(np.int64) * 9 + strat) * 1000 + w
    order = np.argsort(g, kind="stable")
    gs = g[order]
    ts = t[late][order]
    first = np.r_[0, np.flatnonzero(np.diff(gs)) + 1]
    sizes = np.diff(np.r_[first, len(gs)])
    pick = np.repeat(first, sizes) + (rng.random(len(gs)) * np.repeat(sizes, sizes)).astype(np.int64)
    new_t = np.empty_like(ts)
    new_t[:] = ts[pick]
    t_out = t.copy()
    idx_late = np.where(late)[0][order]
    t_out[idx_late] = new_t
    return (u, tr, t_out)


def shuffle_events(events, units, stim, by_stim, rng):
    """Trial shuffle: each unit's trials permuted independently (within stimulus if by_stim)."""
    u, tr, t = events
    sel = np.isin(u, units)
    u, tr, t = u[sel], tr[sel], t[sel]
    n_tr = len(stim)
    newtr = tr.copy()
    for unit in units:
        perm = np.arange(n_tr)
        if by_stim:
            for s in np.unique(stim):
                idx = np.where(stim == s)[0]
                perm[idx] = rng.permutation(idx)
        else:
            perm = rng.permutation(n_tr)
        m = u == unit
        newtr[m] = perm[tr[m]]
    return (u, newtr, t)


def control_trials(stim, trials, by_stim, rng):
    """For each V2 spike's trial, another trial (same stimulus if by_stim)."""
    n = len(stim)
    out = np.empty(len(trials), int)
    if by_stim:
        groups = {s: np.where(stim == s)[0] for s in np.unique(stim)}
        for s, idx in groups.items():
            m = stim[trials] == s
            pos = np.searchsorted(idx, trials[m])
            r = rng.integers(0, len(idx) - 1, m.sum())
            r = r + (r >= pos)
            out[m] = idx[r]
    else:
        r = rng.integers(0, n - 1, len(trials))
        out = r + (r >= trials)
    return out


def state_hist(K, trials, times, offsets, unit_idx, n_units_v2, n_v1):
    """Histogram, per V2 unit, of V1 counts K[trial, time - d] pooled over offsets d.

    Epochs falling outside [ONSET_MS, T_MS) are dropped. Returns (n_units_v2, n_v1 + 1)."""
    h = np.zeros((n_units_v2, n_v1 + 1), np.int64)
    for d in offsets:
        tt = times - d
        ok = (tt >= ONSET_MS) & (tt < K.shape[1])
        k = K[trials[ok], tt[ok]]
        h += np.bincount(unit_idx[ok] * (n_v1 + 1) + k,
                         minlength=n_units_v2 * (n_v1 + 1)).reshape(n_units_v2, n_v1 + 1)
    return h


def js_bits(p, q):
    """Jensen-Shannon divergence in bits between distributions along the last axis
    (Equations 2 and 3); inputs are normalised here."""
    p = p / p.sum(-1, keepdims=True)
    q = q / q.sum(-1, keepdims=True)
    m = 0.5 * (p + q)
    with np.errstate(divide="ignore", invalid="ignore"):
        a = np.where(p > 0, p * np.log2(p / m), 0.0).sum(-1)
        b = np.where(q > 0, q * np.log2(q / m), 0.0).sum(-1)
    return 0.5 * a + 0.5 * b


def to_global(hists, n_v1s):
    """Map per-session histograms over counts 0..N1 onto one support of proportions k/N1.

    hists: list of (n_neurons, N1 + 1) arrays; returns (sum of n_neurons, n_support)."""
    from fractions import Fraction
    keys = sorted({Fraction(k, n) for n in set(n_v1s) for k in range(n + 1)})
    pos = {f: i for i, f in enumerate(keys)}
    out = []
    for h, n in zip(hists, n_v1s):
        g = np.zeros((h.shape[0], len(keys)))
        idx = np.array([pos[Fraction(k, n)] for k in range(n + 1)])
        np.add.at(g.T, idx, h.T)
        out.append(g)
    return np.concatenate(out)


def divergence(h_raw, h_jit, weights=None, per_neuron=False):
    """Divergence of a group: h_raw, h_jit (neurons x support). weights (draws x neurons) are
    bootstrap counts. Pooled distributions (reading d-a) or mean of per-neuron normalised
    distributions (d-b)."""
    if per_neuron:
        h_raw = h_raw / np.maximum(h_raw.sum(1, keepdims=True), 1)
        h_jit = h_jit / np.maximum(h_jit.sum(1, keepdims=True), 1)
    if weights is None:
        return js_bits(h_raw.sum(0), h_jit.sum(0))
    return js_bits(weights @ h_raw, weights @ h_jit)


def boot_weights(n, n_boot, rng):
    """Bootstrap counts (n_boot x n) of neurons resampled with replacement."""
    idx = rng.integers(0, n, (n_boot, n))
    w = np.zeros((n_boot, n))
    np.add.at(w, (np.repeat(np.arange(n_boot), n), idx.ravel()), 1)
    return w


def boot_p_paired(spk, ctl):
    """Reading p-a: two-sided p from paired draws (same neurons for both)."""
    a = np.mean(ctl >= spk)
    b = np.mean(ctl <= spk)
    return min(1.0, 2 * min(a, b))


def boot_p_indep(spk, ctl):
    """Reading p-b: two-sided p treating the two bootstrap distributions as independent."""
    s = np.sort(spk)
    ge = np.searchsorted(s, ctl, side="right").mean() / len(s)      # P(spk <= ctl)
    le = 1 - np.searchsorted(s, ctl, side="left").mean() / len(s)   # P(spk >= ctl)
    return min(1.0, 2 * min(ge, le))


def session_divergence(sess, seed, n_extra_realizations=2, offsets=range(-16, 17)):
    """Histograms of V1 states around the spikes of every kept V2 unit of one session.

    Readings (claims file header): s-a jitter pool and control trials from the same stimulus
    (main) or s-b from all trials; r-a one jitter realization (main) or r-b the sum of
    1 + n_extra_realizations (the mean distribution); shuffled data with trial permutation
    within stimulus (a) or across all trials (b), at spike epochs (c) and control epochs (d).
    Returns a dict of integer histograms over counts 0..N1 of active V1 units:
      raw[o, e, n, k]          offsets o, e = 0 spike epochs / 1 control epochs (s-a)
      jit[w, o, e, n, k]       the same on jittered V1 data, per jitter window w (s-a, r-a)
      raw_sb[o4, e, ...], jit_sb[w, o4, e, ...]   s-b, offsets (-3, -2, 2, 3)
      jit_rb[w, o4, e, ...]    r-b, extra realizations summed (add jit for the mean)
      shuf[r, x, e, ...], shuf_jit[r, w5, x, e, ...]  r = within stimulus / all trials,
                               x = 0 raw shuffled, epochs d = 2, 3 summed
    """
    rng = np.random.default_rng(seed)
    k1, k2 = keep_units(sess, "V1"), keep_units(sess, "V2")
    n1, n2 = len(k1), len(k2)
    stim = sess["stim"]
    n_tr = len(stim)
    ev1 = sess["V1"]["events"]
    u2, tr2, t2 = sess["V2"]["events"]
    m = np.isin(u2, k2) & (t2 >= ONSET_MS)
    umap = np.full(u2.max() + 1, -1)
    umap[k2] = np.arange(n2)
    vu, vtr, vt = umap[u2[m]], tr2[m], t2[m]
    ctl_a = control_trials(stim, vtr, True, rng)
    ctl_b = control_trials(stim, vtr, False, rng)
    offsets = list(offsets)
    o4 = [-3, -2, 2, 3]
    nw = len(JITTER_WINDOWS)

    def hists(K, offs, ctl):
        out = np.zeros((len(offs), 2, n2, n1 + 1), np.int64)
        for i, d in enumerate(offs):
            out[i, 0] = state_hist(K, vtr, vt, [d], vu, n2, n1)
            out[i, 1] = state_hist(K, ctl, vt, [d], vu, n2, n1)
        return out

    K = pop_counts(ev1, k1, n_tr)
    res = {"n_v1": n1, "n_v2": n2, "v2_units": k2, "n_spikes": np.bincount(vu, minlength=n2),
           "offsets": offsets, "o4": o4}
    res["raw"] = hists(K, offsets, ctl_a)
    res["raw_sb"] = hists(K, o4, ctl_b)
    res["jit"] = np.zeros((nw,) + res["raw"].shape, np.int64)
    res["jit_sb"] = np.zeros((nw,) + res["raw_sb"].shape, np.int64)
    res["jit_rb"] = np.zeros((nw,) + res["raw_sb"].shape, np.int64)
    for w, win in enumerate(JITTER_WINDOWS):
        Kj = pop_counts(jitter_events(ev1, k1, stim, win, True, rng), k1, n_tr)
        res["jit"][w] = hists(Kj, offsets, ctl_a)
        Kj = pop_counts(jitter_events(ev1, k1, stim, win, False, rng), k1, n_tr)
        res["jit_sb"][w] = hists(Kj, o4, ctl_b)
        for _ in range(n_extra_realizations):
            Kj = pop_counts(jitter_events(ev1, k1, stim, win, True, rng), k1, n_tr)
            res["jit_rb"][w] += hists(Kj, o4, ctl_a)
    w5 = [w for w in JITTER_WINDOWS if w <= 80]
    res["shuf"] = np.zeros((2, 2, n2, n1 + 1), np.int64)
    res["shuf_jit"] = np.zeros((2, len(w5), 2, n2, n1 + 1), np.int64)
    for r, by_stim in enumerate([True, False]):
        ev_s = shuffle_events(ev1, k1, stim, by_stim, rng)
        ctl = ctl_a if by_stim else ctl_b
        Ks = pop_counts(ev_s, k1, n_tr)
        res["shuf"][r] = hists(Ks, [2, 3], ctl).sum(0)
        for w, win in enumerate(w5):
            Kj = pop_counts(jitter_events(ev_s, k1, stim, win, by_stim, rng), k1, n_tr)
            res["shuf_jit"][r, w] = hists(Kj, [2, 3], ctl).sum(0)
    return res
