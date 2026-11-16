"""Loading and measures for CRCNS ssc-4 (McGuire, Telian, Laboy-Juarez et al. 2016, PLoS Biol 14 e1002549).

The data set is one MATLAB file, AllRats.mat, streamed from the public CRCNS bucket
(crcns:ssc-4/unversioned, doi:10.6080/K06D5QXN). Nothing is written to disk.

Where each parameter comes from:
- Trials. Neural analyses use completed trials (Complete == 1). The data set's own regression inputs
  (StimReg(...).Yval) equal the spike counts summed over exactly these trials (checked in the
  notebook), and the data descriptor says the paper used trials with nose poke > 250 ms, which all
  completed trials meet. This is a detail taken from the data and its descriptor (author, step 1.6).
- Layers from depth: L2/3 200-650, L4 650-975, L5a 975-1285, L5b 1285-1575, L6 1575-2200 um (Methods,
  Neural Recordings).
- Baseline 25 ms before stimulus onset (Results, S1 Recordings, paragraph 2; claim baseline-rates).
- Impulse windows: evoked 5-35 ms after impulse onset, impulse baseline 0-10 ms before it, peak in a
  40-ms window after onset of the 10-ms boxcar smoothed 1-ms PSTH (Methods, Stimulus-evoked responses).
  The Methods do not place the boxcar; it is centred (Matlab's smooth), a standard choice, with
  trailing, forward and no smoothing as variants (smooth_window).
- Temporal modulation: 10-ms bins, 10,000 permutations, p < 0.05 (Methods, Temporal response
  modulation). Spikes permuted uniformly within the window on each trial (claim's standard choice);
  pooled over trials this makes the null PSTH multinomial with equal bin probabilities, which is
  how it is drawn here. The variance of the PSTH across bins and the sum of squared deviations from
  the mean permuted PSTH differ only by a constant under this null, so the two statistics the
  claim names give the same p-value. A second null, shuffling each trial's 10-ms bins
  (perm_pval_shuffle), is a variant.
- Temporally modulated units used by the claims that depend on temporal-modulation-count: the data
  set's TempSig.TemporalPval < 0.05, which the data descriptor names as the units of the paper's
  analyses ("For many analyses in the paper, we only analyzed units whose firing rate was
  significantly temporally modulated ... These units can be identified by
  AllRats(expt).TempSig.TemporalPval(unit) < 0.05"). The set recomputed with the Methods' test is a
  variant (an assumption, stated in the notebook).
- Regression: 5-ms bins 0-180 ms, regressor the integrated panel speed over 5-180 ms windows ending at
  the bin start (Methods, Stimulus regression). The regressor values are the data set's own (Xval in
  StimReg), the stimulus record the claim allows.
- Decoders: logistic regression per unit, 10-ms bins or one bin 0-150 ms, 70% of trials to fit,
  outputs normalised per unit, summed, 300 repeats (Methods, Neural Decoders). L2 penalty with C = 1
  (scikit-learn's default, claim reading a) is fit here by Newton's method batched over units, which
  gives the same optimum as scikit-learn's lbfgs (checked in the notebook). The 70% split is
  stratified by class, and 100 pseudo-trials per class per repeat are drawn: standard choices.
"""

from __future__ import annotations

import collections
import hashlib
import io

import fsspec
import numpy as np
import pandas as pd
import scipy.io
from scipy import stats

URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/AllRats.mat"
DATASET = "crcns:ssc-4/unversioned"
DOI = "10.6080/K06D5QXN"
MD5 = "a929b803ca0feab5270e807f571d13eb"  # AllRats.mat, from ssc-4/live/checksums.md5
S1_DATA = "https://journals.plos.org/plosbiology/article/file?type=supplementary&id=10.1371/journal.pbio.1002549.s001"
S2_DATA = "https://journals.plos.org/plosbiology/article/file?type=supplementary&id=10.1371/journal.pbio.1002549.s002"
S1_TABLE = "https://journals.plos.org/plosbiology/article/file?type=supplementary&id=10.1371/journal.pbio.1002549.s010"

RAT_NAMES = {"18FB": "18FB", "18RI": "18Ri", "18R": "18Ro", "62B": "62BS", "107ST": "107St"}
STIMS = ["FMS", "SMF", "FFF", "SSS"]          # StimNumber 1..4 (data descriptor)
MEAN_SPEED = {"FFF": 65.7, "FMS": 54.4, "SMF": 54.7, "SSS": 44.6}   # Table 1, mm/s
LAYERS = [("L2/3", 200, 650), ("L4", 650, 975), ("L5a", 975, 1285), ("L5b", 1285, 1575), ("L6", 1575, 2200)]
T0, T1 = -100, 400                            # 1-ms spike matrix span, ms from first impulse onset


def layer_of(depth):
    for name, lo, hi in LAYERS:
        if lo <= depth < hi:
            return name
    return "none"


def load_mat():
    f = fsspec.open(URL, block_size=2**22).open()
    return scipy.io.loadmat(f, squeeze_me=True, struct_as_record=False)["AllRats"]


def fetch_xlsx(url):
    with fsspec.open(url, block_size=2**20).open() as f:
        return pd.read_excel(io.BytesIO(f.read()), sheet_name=None, header=None)


def fetch_docx_table(url):
    """Rows of the tables of a DOCX file (cell texts), read from its XML."""
    import re
    import zipfile
    with fsspec.open(url, block_size=2**20).open() as f:
        raw = f.read()
    x = zipfile.ZipFile(io.BytesIO(raw)).read("word/document.xml").decode()
    rows = [[''.join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", c)) for c in re.findall(r"<w:tc>.*?</w:tc>", r, re.S)]
            for r in re.findall(r"<w:tr[ >].*?</w:tr>", x, re.S)]
    return rows, hashlib.md5(raw).hexdigest()


class Data:
    """Sessions, trials, units and a 1-ms spike matrix per session (trials x units x ms)."""

    def __init__(self, A):
        self.A = A
        trials, units, self.spk, self.tw = [], [], [], []
        for si, e in enumerate(A):
            n = len(np.atleast_1d(e.StimNumber))
            t = pd.DataFrame(dict(
                session=si, rat=RAT_NAMES[e.RatName], date=pd.to_datetime(e.RecTime).date(),
                stim=[STIMS[k - 1] for k in np.atleast_1d(e.StimNumber)],
                stim_name=np.atleast_1d(e.StimName), chosen=np.atleast_1d(e.ChosenDP).astype(int),
                target=np.atleast_1d(e.TargetDP).astype(int), complete=np.atleast_1d(e.Complete).astype(bool),
                withdrew=np.atleast_1d(e.Withdrew).astype(bool), timeout=np.atleast_1d(e.Timeout).astype(bool),
                correct=np.atleast_1d(e.Correct).astype(bool), np_dur=np.atleast_1d(e.NPDuration).astype(float),
                np_req=np.atleast_1d(e.NPTimeReq), delay=np.atleast_1d(e.StimOnsetDelay).astype(float),
                start_min=np.atleast_1d(e.StartTime)))
            t["trial"] = np.arange(n)
            t["withdraw_t"] = t.np_dur - t.delay   # nose poke withdrawal, ms after stimulus onset
            trials.append(t)
            info = e.TrialCellInfo
            el = np.atleast_1d(info.Elect).astype(int)
            depth = np.atleast_1d(e.HistDepth).astype(float)
            ct = np.atleast_1d(info.CellTypeKJL)
            pv = np.atleast_1d(e.TempSig.TemporalPval)
            lab = np.atleast_1d(e.LongShortInfo.DFLabel)
            bb = np.atleast_1d(e.BestBin)
            nu = len(el)
            for u in range(nu):
                units.append(dict(session=si, rat=RAT_NAMES[e.RatName], unit=u, elect=el[u],
                                  depth=depth[el[u] - 1], layer=layer_of(depth[el[u] - 1]), type=ct[u],
                                  dep_temp_p=float(pv[u]), dep_label=lab[u], dep_peakbin=bb[u].PeakBin))
            tc = np.asarray(e.TrialCells).reshape(n, nu)
            M = np.zeros((n, nu, T1 - T0), np.uint8)
            for i in range(n):
                for u in range(nu):
                    s = np.atleast_1d(tc[i, u]).astype(float)
                    s = s[(s >= T0) & (s < T1)]
                    np.add.at(M[i, u], np.floor(s - T0).astype(int), 1)
            self.spk.append(M)
            # counts in the 100 ms before nose poke withdrawal (Results, Neural Decoding, paragraph 4)
            w = t.withdraw_t.values
            C = np.zeros((n, nu))
            for i in range(n):
                for u in range(nu):
                    s = np.atleast_1d(tc[i, u]).astype(float)
                    C[i, u] = np.sum((s >= w[i] - 100) & (s < w[i]))
            self.tw.append(C)
        self.trials = pd.concat(trials, ignore_index=True)
        self.units = pd.DataFrame(units)
        self.units["uid"] = np.arange(len(self.units))
        self.stimtimes = [[np.atleast_2d(e.StimTimes[k]).astype(float) for k in range(4)] for e in A]

    def onsets(self, si, stim):
        """Impulse onsets (ms, floored as in the descriptor's example code) for a session and sequence."""
        return np.floor(self.stimtimes[si][STIMS.index(stim)][:, 0]).astype(int)

    def unit_trials(self, uid, sel=None):
        """Spike matrix (trials x ms) and trial table of one unit, completed trials only by default."""
        r = self.units.iloc[uid]
        t = self.trials[self.trials.session == r.session]
        m = t.complete.values if sel is None else sel(t)
        return self.spk[r.session][m, r.unit, :].astype(float), t[m].reset_index(drop=True), \
            self.tw[r.session][m, r.unit]


def rate(M, a, b):
    """Mean rate (Hz) per trial in [a, b) ms from stimulus onset; M is trials x ms from T0."""
    return M[:, a - T0:b - T0].sum(1) * 1000.0 / (b - a)


# ---------- temporal modulation ----------

def perm_pval(counts, rng, nperm=10000):
    """Permutation p-value of the variance of a pooled PSTH against uniformly redistributed spikes."""
    counts = np.asarray(counts, float)
    N, k = int(counts.sum()), len(counts)
    if N == 0:
        return 1.0
    obs = counts.var()
    null = rng.multinomial(N, np.full(k, 1.0 / k), size=nperm).var(1)
    return (np.sum(null >= obs - 1e-12) + 1) / (nperm + 1)


def perm_pval_shuffle(bins, rng, nperm=1000, chunk=100):
    """Permutation p-value of the variance of a pooled PSTH against the PSTHs obtained by shuffling
    the 10-ms bins of each trial independently (a second null, asked for by the verifier: it keeps
    each trial's bin counts, so bursts stay together)."""
    bins = np.asarray(bins, float)
    if bins.sum() == 0:
        return 1.0
    obs = bins.sum(0).var()
    null = []
    for _ in range(nperm // chunk):
        keys = rng.random((chunk,) + bins.shape).argsort(2)
        null.append(np.take_along_axis(np.broadcast_to(bins, keys.shape), keys, 2).sum(1).var(1))
    null = np.concatenate(null)
    return (np.sum(null >= obs - 1e-12) + 1) / (nperm + 1)


def temporal_bins(D, uid, reading):
    """10-ms counts per completed trial (trials x bins). reading 'np': 0-180 ms after nose poke
    entry; 'stim': 0-180 ms after stimulus onset; 'deposit': -50 to 300 ms after onset
    (TempSig.Params of the data set)."""
    M, t, _ = D.unit_trials(uid)
    if reading == "stim":
        return M[:, -T0:180 - T0].reshape(len(M), 18, 10).sum(2)
    if reading == "deposit":
        return M[:, -50 - T0:300 - T0].reshape(len(M), 35, 10).sum(2)
    out = np.zeros((len(M), 18))
    for i, d in enumerate(t.delay.values.astype(int)):   # NP entry is `delay` ms before onset
        out[i] = M[i, -d - T0:-d + 180 - T0].reshape(18, 10).sum(1)
    return out


def temporal_counts(D, uid, reading):
    """Pooled 10-ms counts over completed trials (see temporal_bins)."""
    return temporal_bins(D, uid, reading).sum(0)


# ---------- impulse-locked measures ----------

SMOOTH = {"centred": (-5, 5), "trailing": (-9, 1), "forward": (0, 10)}


def smooth_window(psth, how="centred"):
    """10-ms boxcar of a segment's 1-ms PSTH (index 0 = -10 ms) at 0..39 ms after impulse onset.
    'centred' averages t-5..t+4 ms, 'trailing' t-9..t, 'forward' t..t+9 (Methods: "10 ms
    smoothing", placement not given; centred is Matlab's smooth, a standard choice, and the other
    two are shown as variants); 'none' is the unsmoothed PSTH."""
    if how == "none":
        return psth[10:50]
    a, b = SMOOTH[how]
    return np.array([psth[10 + t + a:10 + t + b].mean() for t in range(40)])


def impulse_segments(D, uid, stims=None, pulses=(0, 1, 2), kinds=None, trials_sel=None):
    """Per impulse instance (sequence, pulse) the trial x ms spike matrix aligned to impulse onset,
    from -10 to +50 ms (the 10 ms after the 40-ms peak window are there so that the smoothing
    needs no padding). Returns a list of dicts."""
    M, t, _ = D.unit_trials(uid, trials_sel)
    si = int(D.units.iloc[uid].session)
    segs = []
    for s in (stims or STIMS):
        m = (t.stim == s).values
        if m.sum() == 0:
            continue
        on = D.onsets(si, s)
        for p in pulses:
            k = s[p]
            if kinds and k not in kinds:
                continue
            a = on[p] - 10 - T0
            segs.append(dict(stim=s, pulse=p, kind=k, X=M[m, a:a + 60], trials=t[m]))
    return segs


def evoked_peak(segs, pooled=True, smooth="centred"):
    """Peak modulation (signed extreme of larger |deviation| from the 0-10 ms pre-impulse baseline,
    in the 10-ms smoothed PSTH over 0-40 ms after onset), the 5-35 ms mean minus baseline, and the
    latency of the maximum (the mean of the times that share the maximum, so that a plateau is not
    read at its first sample). pooled: one PSTH over all impulses (reading i); else per impulse,
    averaged (reading ii). smooth: see smooth_window."""
    def one(X):
        psth = X.mean(0) * 1000.0
        base = psth[0:10].mean()
        sm = smooth_window(psth, smooth) - base
        imax, imin = sm.argmax(), sm.argmin()
        peak = sm[imax] if abs(sm[imax]) >= abs(sm[imin]) else sm[imin]
        lat = float(np.flatnonzero(np.isclose(sm, sm[imax])).mean())
        return peak, psth[15:45].mean() - base, lat
    if pooled:
        X = np.concatenate([g["X"] for g in segs])
        return one(X)
    v = np.array([one(g["X"]) for g in segs])
    return tuple(v.mean(0))


def impulse_ttest(segs):
    """Per trial, mean rate 5-35 ms after impulse onset against 0-10 ms before, averaged over the
    trial's impulses; paired t test across trials. Returns (t, p two-sided, p one-sided greater)."""
    post, pre = [], []
    for g in segs:
        post.append(g["X"][:, 15:45].mean(1) * 1000)
        pre.append(g["X"][:, 0:10].mean(1) * 1000)
    # group by trial within each sequence: impulses of the same trial are averaged
    d = collections.defaultdict(list)
    for g, a, b in zip(segs, post, pre):
        for i, (x, y) in enumerate(zip(a, b)):
            d[(g["stim"], i)].append(x - y)
    diff = np.array([np.mean(v) for v in d.values()])
    if diff.std() == 0:
        return 0.0, 1.0, 1.0
    r = stats.ttest_1samp(diff, 0)
    return r.statistic, r.pvalue, (r.pvalue / 2 if r.statistic > 0 else 1 - r.pvalue / 2)


# ---------- regression ----------

def regression(D, uid, use_rate=False):
    """36 OLS regressions of 5-ms counts (0-180 ms, 4 sequences) on the data set's integrated speed.
    Returns arrays R2, p, slope over windows 5..180 ms."""
    r = D.units.iloc[uid]
    e = D.A[r.session]
    M, t, _ = D.unit_trials(uid)
    Y = np.zeros((4, 36))
    for k, s in enumerate(STIMS):
        m = (t.stim == s).values
        Y[k] = M[m, -T0:180 - T0].reshape(m.sum(), 36, 5).sum((0, 2))
        if use_rate:
            Y[k] = Y[k] / max(m.sum(), 1) / 0.005
    y = Y.ravel()
    sr = np.atleast_2d(e.StimReg)[r.unit]
    R2, P, B = np.zeros(36), np.ones(36), np.zeros(36)
    for w in range(36):
        x = np.asarray(sr[w].Xval)[:, 1]
        res = stats.linregress(x, y)
        R2[w], P[w], B[w] = res.rvalue**2, res.pvalue, res.slope
    return R2, P, B


def classify(best_ms, slope, sig, which="all", medium55=False):
    """Fast 5-20 ms, Medium 25-50 (or 25-55), Slow above; Slow split by slope sign (Results)."""
    if which == "sig" and not sig:
        return "none"
    if best_ms <= 20:
        return "Fast"
    if best_ms <= (55 if medium55 else 50):
        return "Medium"
    return "SlowPos" if slope > 0 else "SlowNeg"


# ---------- logistic decoders ----------

def fit_logistic(X, y, w, C=1.0, iters=25):
    """L2-penalised logistic regression (scikit-learn's objective: 0.5|b|^2 + C sum w*logloss, intercept
    unpenalised), batched: X (P, n, d), y and w (P, n). Newton's method. Returns (P, d+1)."""
    P, n, d = X.shape
    Xa = np.concatenate([X, np.ones((P, n, 1))], 2)
    beta = np.zeros((P, d + 1))
    reg = np.ones(d + 1) / C
    reg[-1] = 1e-8
    for _ in range(iters):
        z = np.einsum("pnd,pd->pn", Xa, beta)
        mu = 1 / (1 + np.exp(-z))
        g = np.einsum("pnd,pn->pd", Xa, w * (mu - y)) + reg * beta
        Wt = w * mu * (1 - mu)
        H = np.einsum("pnd,pn,pne->pde", Xa, Wt, Xa) + np.eye(d + 1) * reg
        step = np.linalg.solve(H, g[..., None])[..., 0]
        beta -= step
        if np.abs(step).max() < 1e-8:
            break
    return beta


def predict_logistic(beta, X):
    Xa = np.concatenate([X, np.ones(X.shape[:-1] + (1,))], -1)
    return 1 / (1 + np.exp(-(Xa @ beta)))


def unit_features(D, uid, kind):
    """Completed-trial features of one unit: '10ms' (15 counts, 0-150 ms), '1bin' (count 0-150 ms),
    'pre100' (count in the 100 ms before withdrawal). Returns X, trial table."""
    M, t, tw = D.unit_trials(uid)
    if kind == "10ms":
        X = M[:, -T0:150 - T0].reshape(len(M), 15, 10).sum(2)
    elif kind == "1bin":
        X = M[:, -T0:150 - T0].sum(1, keepdims=True)
    else:
        X = tw[:, None]
    return X.astype(float), t


def transform(X, how, rng):
    if how == "norm":   # each trial's count vector divided by its Euclidean norm (Methods)
        n = np.linalg.norm(X, axis=1, keepdims=True)
        return np.divide(X, n, out=np.zeros_like(X), where=n > 0)
    if how == "scramble":   # spikes redistributed uniformly over the 0-150 ms window of each trial
        return np.array([rng.multinomial(int(c), np.full(X.shape[1], 1 / X.shape[1])) for c in X.sum(1)], float)
    return X


def _split(y, rng, frac=0.7):
    tr = np.zeros(len(y), bool)
    for c in np.unique(y):
        idx = np.where(y == c)[0]
        rng.shuffle(idx)
        tr[idx[:int(round(frac * len(idx)))]] = True
    return tr


def _cv_C(Xs, ys, rng, Cs, folds=5, balanced=False):
    """Per problem, the C of the grid with the best mean held-out accuracy over stratified folds
    (balanced accuracy when the fit is class-balanced)."""
    P = len(Xs)
    acc = np.zeros((P, len(Cs)))
    fold_of = []
    for y in ys:
        f = np.zeros(len(y), int)
        for c in np.unique(y):
            idx = np.where(y == c)[0]
            rng.shuffle(idx)
            f[idx] = np.arange(len(idx)) % folds
        fold_of.append(f)
    for k in range(folds):
        Xtr = [x[f != k] for x, f in zip(Xs, fold_of)]
        ytr = [y[f != k] for y, f in zip(ys, fold_of)]
        for j, C in enumerate(Cs):
            beta = _fit_bucketed(Xtr, ytr, C, balanced)
            for p in range(P):
                te = fold_of[p] == k
                if te.sum():
                    hit = (predict_logistic(beta[p], Xs[p][te]) > 0.5) == (ys[p][te] > 0.5)
                    if balanced:
                        acc[p, j] += np.mean([hit[ys[p][te] == c].mean() for c in (0, 1) if np.any(ys[p][te] == c)]) / folds
                    else:
                        acc[p, j] += hit.mean() / folds
    return np.array(Cs)[acc.argmax(1)]


def _pad(Xs, ys, balanced=False):
    n = max(len(x) for x in Xs)
    d = Xs[0].shape[1]
    X = np.zeros((len(Xs), n, d))
    y = np.zeros((len(Xs), n))
    w = np.zeros((len(Xs), n))
    for i, (a, b) in enumerate(zip(Xs, ys)):
        X[i, :len(a)] = a
        y[i, :len(b)] = b
        w[i, :len(b)] = 1
        if balanced:   # each class weighted to half the total, as scikit-learn's class_weight="balanced"
            for c in (0, 1):
                m = b == c
                if m.any():
                    w[i, :len(b)][m] = len(b) / (2 * m.sum())
    return X, y, w


def _fit_bucketed(Xs, ys, C=1.0, balanced=False):
    """Fit many problems, grouped by trial count so that little padding is fitted."""
    order = np.argsort([len(y) for y in ys])
    beta = np.zeros((len(ys), Xs[0].shape[1] + 1))
    for chunk in np.array_split(order, max(1, len(ys) // 64)):
        Xb, yb, wb = _pad([Xs[i] for i in chunk], [ys[i] for i in chunk], balanced)
        beta[chunk] = fit_logistic(Xb, yb, wb, C=C)
    return beta


def _fit(Xs, ys, rng, cv, balanced=False):
    if not cv:
        return _fit_bucketed(Xs, ys, 1.0, balanced)
    Cs = _cv_C(Xs, ys, rng, [1e-3, 1e-2, 1e-1, 1, 10, 100], balanced=balanced)
    beta = np.zeros((len(ys), Xs[0].shape[1] + 1))
    for C in np.unique(Cs):
        idx = np.where(Cs == C)[0]
        beta[idx] = _fit_bucketed([Xs[i] for i in idx], [ys[i] for i in idx], C, balanced)
    return beta


def stim_decoder(D, uids, kind="10ms", how=None, repeats=300, seed=0, cv=False, npseudo=100):
    """Population one-vs-all stimulus decoder (Methods, Neural Decoders). Returns the mean confusion
    matrix (rows true FFF, FMS, SMF, SSS; rows sum to 1), per-repeat accuracy and per-unit accuracy."""
    rng = np.random.default_rng(seed)
    order = ["FFF", "FMS", "SMF", "SSS"]
    feats = []
    for u in uids:
        X, t = unit_features(D, u, kind)
        X = transform(X, how, rng)
        feats.append((X, np.array([order.index(s) for s in t.stim])))
    U = len(feats)
    conf = np.zeros((4, 4))
    accs, unit_acc = [], np.zeros(U)
    for r in range(repeats):
        Xs, ys, tests = [], [], []
        for X, y in feats:
            tr = _split(y, rng)
            tests.append((X[~tr], y[~tr]))
            for c in range(4):
                Xs.append(X[tr])
                ys.append((y[tr] == c).astype(float))
        beta = _fit(Xs, ys, rng, cv).reshape(U, 4, -1)
        probs = []
        for i, (Xt, yt) in enumerate(tests):
            p = np.stack([predict_logistic(beta[i, c], Xt) for c in range(4)], 1)
            p = p / p.sum(1, keepdims=True)
            probs.append((p, yt))
            unit_acc[i] += np.mean(p.argmax(1) == yt) / repeats
        cm = np.zeros((4, 4))
        for c in range(4):
            tot = np.zeros((npseudo, 4))
            for p, yt in probs:
                idx = np.where(yt == c)[0]
                if len(idx):
                    tot += p[rng.choice(idx, npseudo)]
            pred = tot.argmax(1)
            cm[c] = np.bincount(pred, minlength=4) / npseudo
        conf += cm / repeats
        accs.append(np.trace(cm) / 4)
    return conf, np.array(accs), unit_acc


def choice_decoder(D, uids, kind="1bin", repeats=300, seed=0, cv=False, npseudo=100, balanced=True):
    """Population choice decoder (Methods): one logistic function per unit fit on trials of all four
    sequences, tested within each sequence. Returns, per sequence, accuracy with equal numbers of
    right and left pseudo-trials (reading i) and with the data's proportions (reading ii), averaged
    over repeats, and each unit's balanced accuracy on its own test trials. balanced: training trials
    weighted so that right and left count equally (an assumption: the paper gives chance as 50%)."""
    rng = np.random.default_rng(seed)
    feats = []
    for u in uids:
        X, t = unit_features(D, u, kind)
        feats.append((X, (t.chosen.values == 1).astype(float), t.stim.values))
    allt = pd.concat([unit_features(D, u, kind)[1] for u in uids])
    pright = allt.groupby("stim").chosen.mean().to_dict()
    U = len(feats)
    res = {s: np.zeros(2) for s in STIMS}
    unit_acc = np.zeros(U)
    for r in range(repeats):
        Xs, ys, tests = [], [], []
        for X, y, st in feats:
            tr = _split(y + 2 * np.array([STIMS.index(s) for s in st]), rng)   # stratify by stim and choice
            Xs.append(X[tr])
            ys.append(y[tr])
            tests.append((X[~tr], y[~tr], st[~tr]))
        beta = _fit(Xs, ys, rng, cv, balanced)
        P = [(predict_logistic(beta[i], Xt), yt, st) for i, (Xt, yt, st) in enumerate(tests)]
        for i, (p, yt, st) in enumerate(P):
            unit_acc[i] += np.mean([np.mean((p[yt == c] > 0.5) == c) for c in (0, 1) if np.any(yt == c)]) / repeats
        for s in STIMS:
            acc_c = {}
            for c in (0, 1):
                tot = np.zeros(npseudo)
                cnt = np.zeros(npseudo)
                for p, yt, st in P:
                    idx = np.where((st == s) & (yt == c))[0]
                    if len(idx):
                        tot += p[rng.choice(idx, npseudo)]
                        cnt += 1
                acc_c[c] = np.mean((tot > cnt / 2) == c)
            res[s] += np.array([(acc_c[0] + acc_c[1]) / 2,
                                pright[s] * acc_c[1] + (1 - pright[s]) * acc_c[0]]) / repeats
    return res, unit_acc


# ---------- unit selection pipeline shared by the notebooks ----------

def temporal_pvals(D, reading, seed):
    rng = np.random.default_rng(seed)
    return np.array([perm_pval(temporal_counts(D, u, reading), rng) for u in D.units.uid])


def regress_all(D, use_rate=False):
    """R2, p and slope (units x 36 windows) for every unit."""
    out = [regression(D, u, use_rate) for u in D.units.uid]
    return tuple(np.array([o[k] for o in out]) for k in range(3))


def unit_classes(R2, P, B, mod, which="all", medium55=False):
    """Class of each unit from its regression: temporally modulated units only ('none' otherwise).
    which='all': every modulated unit by its highest-R2 window (reading a); 'sig': only units with
    a window at p < 0.05/36 (reading b). Best window in ms, slope of that window."""
    best = (R2.argmax(1) + 1) * 5
    slope = B[np.arange(len(B)), R2.argmax(1)]
    sig = (P < 0.05 / 36).any(1)
    lab = np.array([classify(b, s, g, which, medium55) if m else "none"
                    for b, s, g, m in zip(best, slope, sig, mod)])
    return lab, best, slope, sig


def deposited_classes(D):
    """The data set's own labels mapped to the paper's classes: FastPos/FastNeg split at the 20-ms
    boundary into Fast and Medium by PeakBin (ms), SlowPos, SlowNeg; NoTempMod and others 'none'."""
    out = []
    for lab, pb in zip(D.units.dep_label, D.units.dep_peakbin):
        if lab in ("FastPos", "FastNeg"):
            out.append("Fast" if pb <= 20 else "Medium")
        elif lab in ("SlowPos", "SlowNeg"):
            out.append(lab)
        else:
            out.append("none")
    return np.array(out)
