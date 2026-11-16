"""Loading and measures for CRCNS data set v4-2 (Henry & Kohn 2022, Current Biology 32, 5126-5137,
doi:10.1016/j.cub.2022.10.049; data doi:10.6080/K0736P4H).

The data set has one zip, data.zip, with two MATLAB files. Each holds `v1population` and
`v4population`, one entry per population (a session and one of its two orientation ranges), with
`spikecounts` (neurons x stimulus epochs, the count 0 to 0.25 s after onset), `parameters` (one row
per label in `parameter_labels`), `session`, `animal` and `session_orientation_range`. The zip is
read in place from the public S3 bucket over range requests; nothing is written to disk.

CRCNS data sets are not versioned (docs/archives.md). The version is recorded as `unversioned`,
and `DATA_MD5` is the MD5 the data set's checksums.md5 gives for data.zip; `load` checks the zip
it reads against it.

Where the parameters come from (claim ids are those of claims/henry-2022.yaml):

- Spacings 1.32, 1.64, 2.04 and 2.56 degrees are the data's values; the paper prints them as 1.3,
  1.6, 2.1 and 2.6.
- Single-neuron discriminability (fig2*): AUC between the counts to the two most extreme target
  orientations, "We assumed the orientation closer to 0 would evoke stronger responses" (Results,
  "Distractors limit target discriminability", paragraph 1): the AUC is P(count to the extreme
  closer to 0 degrees, as an axial orientation, exceeds the count to the other). When both are
  equally close (reference 0, extremes -9 and +9) the lower one is taken (a standard choice).
  Regression slope by OLS with intercept and bootstrap over neurons (STAR Methods, paragraph 2 of
  Quantification); 1000 bootstrap samples is a standard choice.
- Decoding (fig2de onwards): L1 logistic regression, penalty "set to the largest value that
  yielded maximal cross-validated performance on held out trials from the training set", "an
  average over cross-validation folds" (STAR Methods, paragraph 3 of Quantification). Folds (10
  outer, 10 inner, 5 as a variant) are the claims file's standard choice. The penalty grid
  (`CS`, 13 values of C from 0.01 to 100) and z-scoring of each neuron's counts on the training
  trials are standard choices the paper does not state; the fold assignment is stratified and
  seeded.
- Threshold elevation: cumulative normal adjusted for chance, P(x) = Phi(x / sigma) for x >= 0,
  crowded prediction Phi(Phi^-1(p_alone) / k), binomial likelihood, k by maximum likelihood on a
  grid (`K_GRID`, 0.2 to 20, log spaced; a standard choice; `K_GRID_WIDE`, 0.2 to 1000, shows
  which estimates the upper bound censors), STAR Methods paragraph 4 and the
  Figure S2 legend, as the claims file reads them.
- Noise correlations: trials with both responses within 3 SD of their means, per stimulus, then
  averaged (STAR Methods, paragraph 5).
- Modulation index and its permutation test: STAR Methods paragraph 6 and Results ("geometric mean
  of the indices computed for each target orientation separately").
- Tuning model rTD = m*rT + a*mean(rT), rectified at 0, Poisson likelihood (STAR Methods,
  paragraph 7). The rectification floor `EPS` (1e-3 spikes) keeps the log-likelihood finite, a
  standard choice. Single-form models of Figure S5: c*rT and rT + c*mean(rT).
"""

from __future__ import annotations

import hashlib
import io
import zipfile

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy import optimize, stats

BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/v4-2/live"
DATASET = "CRCNS v4-2 (doi:10.6080/K0736P4H), version unversioned, file live/data.zip"
DATA_URL = f"{BASE}/data.zip"
DATA_MD5 = "bdd60f999b997523151b9ae24a42b837"
FILES = {"separation": "data/HenryKohn2022_distractorseparation.mat",
         "orientation": "data/HenryKohn2022_distractororientation.mat"}
SPACINGS = (1.32, 1.64, 2.04, 2.56)
CS = np.logspace(-2, 2, 13)
K_GRID = np.exp(np.linspace(np.log(0.2), np.log(20), 1201))
K_GRID_WIDE = np.exp(np.linspace(np.log(0.2), np.log(1000), 2201))
EPS = 1e-3


# --- loading --------------------------------------------------------------------------------------

def _md5_of_url(url):
    h = hashlib.md5()
    with fsspec.open(url, "rb", block_size=2**20) as f:
        for chunk in iter(lambda: f.read(2**20), b""):
            h.update(chunk)
    return h.hexdigest()


def load():
    """Both experiments, as {'separation': [pop, ...], 'orientation': [pop, ...]}.

    Each pop is a dict: area ('V1' or 'V4'), session, animal, orange (orientation range 1 or 2),
    counts (neurons x epochs, int), and the epoch table `p` (a DataFrame). In `p`: kind is 'blank'
    (no target, no distractors), 'dist' (distractors only), 'alone' (target only) or 'crowd'
    (target with distractors); sep the spacing (NaN without distractors); rel the target
    orientation relative to the reference (the orientation of the blank epochs); oi the index of
    the target orientation (0 for the lowest); config, for the orientation experiment, 0 or 1 by
    distractor1's orientation relative to the reference (-10 or +10)."""
    md5 = _md5_of_url(DATA_URL)
    z = zipfile.ZipFile(fsspec.open(DATA_URL, "rb", block_size=2**20).open())
    out = {"md5": md5}
    for key, member in FILES.items():
        m = sio.loadmat(io.BytesIO(z.read(member)), squeeze_me=True, struct_as_record=False)
        pops = []
        for var, area in (("v1population", "V1"), ("v4population", "V4")):
            for s in np.atleast_1d(m[var]):
                labels = [str(x).replace(" ", "_") for x in s.parameter_labels]
                p = pd.DataFrame(np.asarray(s.parameters, float).T, columns=labels)
                tc, dc = p.target_contrast > 0, p.distractor_contrast > 0
                p["kind"] = np.select([~tc & ~dc, ~tc & dc, tc & ~dc, tc & dc],
                                      ["blank", "dist", "alone", "crowd"], default="")
                ref = p.loc[p.kind == "blank", "target_ori"].iloc[0]
                p["rel"] = p.target_ori - ref
                oris = np.sort(p.loc[tc, "target_ori"].unique())
                p["oi"] = np.where(tc, np.searchsorted(oris, p.target_ori), -1)
                if "distractorseparation" in p:
                    p["sep"] = p.distractorseparation.round(2)
                else:
                    p["sep"] = np.where(dc, 0.0, np.nan)
                p["config"] = np.where(dc, (p.distractor1_ori - ref > 0).astype(int), -1)
                pops.append(dict(area=area, session=int(s.session), animal=str(s.animal),
                                 orange=int(s.session_orientation_range),
                                 counts=np.asarray(s.spikecounts).astype(int), p=p,
                                 oris=oris, ref=ref))
        out[key] = pops
    return out


def stim_mask(pop, kind, sep=None, oi=None, config=None):
    p = pop["p"]
    m = p.kind.values == kind
    if sep is not None:
        m &= np.isclose(p.sep.values, sep)
    if oi is not None:
        m &= p.oi.values == oi
    if config is not None:
        m &= p.config.values == config
    return m


def responses(pop, kind, sep=None, config=None):
    """List over target orientation index of (neurons x trials) count arrays."""
    n_or = len(pop["oris"])
    return [pop["counts"][:, stim_mask(pop, kind, sep, oi, config)] for oi in range(n_or)]


def tuning(pop, kind, sep=None, config=None):
    """Mean count per target orientation, neurons x orientations."""
    return np.stack([r.mean(1) for r in responses(pop, kind, sep, config)], 1)


# --- single-neuron discriminability --------------------------------------------------------------

def auc(a, b):
    """P(a > b) + 0.5 P(a = b), over all pairs of samples."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    return (np.mean(a[:, None] > b[None, :]) + 0.5 * np.mean(a[:, None] == b[None, :]))


def axial_distance_to_zero(ori):
    o = np.mod(ori, 180.0)
    return np.minimum(o, 180 - o)


def extreme_order(pop):
    """(index of the extreme closer to 0 degrees, the other); the lower when tied."""
    lo, hi = 0, len(pop["oris"]) - 1
    dlo, dhi = axial_distance_to_zero(pop["oris"][[lo, hi]])
    return (hi, lo) if dhi < dlo else (lo, hi)


def neuron_aucs(pop, kind, sep=None, order="paper"):
    first, second = extreme_order(pop) if order == "paper" else (0, len(pop["oris"]) - 1)
    r = responses(pop, kind, sep)
    return np.array([auc(r[first][i], r[second][i]) for i in range(pop["counts"].shape[0])])


def ols_slope(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    xc = x - x.mean()
    return float(np.sum(xc * (y - y.mean())) / np.sum(xc ** 2))


def origin_slope(x, y, c=0.5):
    """Slope of a fit through (c, c)."""
    x, y = np.asarray(x, float) - c, np.asarray(y, float) - c
    return float(np.sum(x * y) / np.sum(x ** 2))


def slope_ci(x, y, rng, n_boot=1000, fit=ols_slope):
    x, y = np.asarray(x, float), np.asarray(y, float)
    n = len(x)
    idx = rng.integers(0, n, size=(n_boot, n))
    boots = np.array([fit(x[i], y[i]) for i in idx])
    return fit(x, y), np.percentile(boots, 2.5), np.percentile(boots, 97.5)


# --- population decoding --------------------------------------------------------------------------

def _zscore(train, test):
    mu, sd = train.mean(0), train.std(0)
    sd[sd == 0] = 1.0
    return (train - mu) / sd, (test - mu) / sd


def _folds(y, k, rng):
    """Stratified fold labels 0..k-1."""
    f = np.empty(len(y), int)
    for c in np.unique(y):
        idx = np.flatnonzero(y == c)
        idx = idx[rng.permutation(len(idx))]
        f[idx] = (np.arange(len(idx)) + rng.integers(k)) % k
    return f


def _fit(X, y, C):
    """L1-penalised logistic regression by liblinear (as sklearn's LogisticRegression with
    solver="liblinear" and an L1 penalty), called directly to save the per-fit overhead; liblinear's
    own random state is fixed at 0."""
    from sklearn.svm._base import _fit_liblinear
    coef, b, _ = _fit_liblinear(X, y, C, True, 1.0, None, "l1", False, 0, 1000, 1e-4, 0,
                                loss="logistic_regression")
    return coef[0], float(np.ravel(b)[0])


def _predict(model, X):
    coef, b = model
    return (X @ coef + b > 0).astype(int)


def choose_C(X, y, inner, rng):
    """Smallest C (largest penalty) that reaches the maximal inner cross-validated accuracy."""
    f = _folds(y, inner, rng)
    acc = np.zeros(len(CS))
    for j in range(inner):
        tr, te = f != j, f == j
        Xtr, Xte = _zscore(X[tr], X[te])
        for ci, C in enumerate(CS):
            acc[ci] += np.sum(_predict(_fit(Xtr, y[tr], C), Xte) == y[te])
    return CS[int(np.flatnonzero(acc == acc.max())[0])]


def fit_nonzero(X, y, C):
    """The decoder at C, or, if it has no nonzero coefficient, at the smallest larger C of `CS`
    that has one (a variant that never keeps an all-zero decoder; the last C is kept if none has)."""
    model = _fit(X, y, C)
    for c in CS[CS > C]:
        if np.any(model[0] != 0):
            break
        model = _fit(X, y, c)
    return model


def decode(X, y, rng, outer=10, inner=10, diag=None):
    """Mean over outer folds of the held-out fraction correct of an L1 logistic decoder. If `diag`
    is a list, (chosen C, number of nonzero coefficients, held-out accuracy of `fit_nonzero` at the
    chosen C) of each outer fold is appended to it; the variant uses no random numbers, so the
    folds and the main result are the same with and without it."""
    f = _folds(y, outer, rng)
    accs = []
    for j in range(outer):
        tr, te = f != j, f == j
        C = choose_C(X[tr], y[tr], inner, rng)
        Xtr, Xte = _zscore(X[tr], X[te])
        model = _fit(Xtr, y[tr], C)
        accs.append(np.mean(_predict(model, Xte) == y[te]))
        if diag is not None:
            nz = int(np.sum(model[0] != 0))
            alt = accs[-1] if nz else np.mean(_predict(fit_nonzero(Xtr, y[tr], C), Xte) == y[te])
            diag.append((C, nz, float(alt)))
    return float(np.mean(accs))


def shuffle_within(X, y, rng):
    """Each neuron's counts permuted independently across trials of the same stimulus."""
    X = X.copy()
    for c in np.unique(y):
        idx = np.flatnonzero(y == c)
        for i in range(X.shape[1]):
            X[idx, i] = X[rng.permutation(idx), i]
    return X


def decode_shuffled_train(X, y, rng, outer=10, inner=10):
    """As `decode`, with the training trials of each fold shuffled and the test trials intact."""
    f = _folds(y, outer, rng)
    accs = []
    for j in range(outer):
        tr, te = f != j, f == j
        Xtr0 = shuffle_within(X[tr], y[tr], rng)
        C = choose_C(Xtr0, y[tr], inner, rng)
        Xtr, Xte = _zscore(Xtr0, X[te])
        accs.append(np.mean(_predict(_fit(Xtr, y[tr], C), Xte) == y[te]))
    return float(np.mean(accs))


def pair_trials(pop, kind, sep, a, b):
    ma, mb = stim_mask(pop, kind, sep, a), stim_mask(pop, kind, sep, b)
    X = np.concatenate([pop["counts"][:, ma], pop["counts"][:, mb]], 1).T.astype(float)
    y = np.r_[np.zeros(ma.sum(), int), np.ones(mb.sum(), int)]
    return X, y


# --- threshold elevation ---------------------------------------------------------------------------

def k_loglik(pa, pc, n, grid=K_GRID):
    """Log-likelihood over `grid` of crowded performances pc given target-alone pa, n trials."""
    za = stats.norm.ppf(pa)
    pred = stats.norm.cdf(za[None, :] / grid[:, None])
    pred = np.clip(pred, 1e-9, 1 - 1e-9)
    s = pc * n
    return np.sum(s[None, :] * np.log(pred) + (n - s)[None, :] * np.log(1 - pred), 1)


def usable(pa):
    return (pa > 0.5) & (pa < 1)


def fit_k(pa, pc, n, grid=K_GRID):
    pa, pc, n = map(lambda v: np.asarray(v, float), (pa, pc, n))
    ok = usable(pa)
    if ok.sum() == 0:
        return np.nan
    return float(grid[np.argmax(k_loglik(pa[ok], pc[ok], n[ok], grid))])


def boot_k(pa, pc, n, rng, n_boot=1000):
    pa, pc, n = map(lambda v: np.asarray(v, float), (pa, pc, n))
    ok = np.flatnonzero(usable(pa))
    out = np.empty(n_boot)
    for b in range(n_boot):
        i = ok[rng.integers(0, len(ok), len(ok))]
        out[b] = K_GRID[np.argmax(k_loglik(pa[i], pc[i], n[i]))]
    return out


def perm_k(pa, pc, n, rng, n_perm=1000):
    """Null estimates with the alone and crowded labels swapped at random within each point."""
    pa, pc, n = map(lambda v: np.asarray(v, float), (pa, pc, n))
    out = np.empty(n_perm)
    for b in range(n_perm):
        sw = rng.random(len(pa)) < 0.5
        a, c = np.where(sw, pc, pa), np.where(sw, pa, pc)
        out[b] = fit_k(a, c, n)
    return out


# --- variability -------------------------------------------------------------------------------------

def noise_corr(counts):
    """Pairwise rSC for one stimulus (neurons x trials), trials with both within 3 SD of their
    means; NaN where a neuron has no variance."""
    n = counts.shape[0]
    z = (counts - counts.mean(1, keepdims=True)) / np.where(counts.std(1, keepdims=True) > 0,
                                                            counts.std(1, keepdims=True), np.nan)
    ok = np.abs(z) <= 3
    r = np.full((n, n), np.nan)
    for i in range(n):
        for j in range(i + 1, n):
            t = ok[i] & ok[j]
            a, b = counts[i, t], counts[j, t]
            if t.sum() > 2 and a.std() > 0 and b.std() > 0:
                r[i, j] = np.corrcoef(a, b)[0, 1]
    return r


def pair_rsc(pop, kind, sep=None, epochs=None):
    """rSC per pair averaged over target orientations; `epochs` an optional boolean mask."""
    rs = []
    for oi in range(len(pop["oris"])):
        m = stim_mask(pop, kind, sep, oi)
        if epochs is not None:
            m &= epochs
        rs.append(noise_corr(pop["counts"][:, m]))
    r = np.nanmean(np.stack(rs), 0)
    iu = np.triu_indices(pop["counts"].shape[0], 1)
    return r[iu]


def fano(pop, kind, sep=None):
    """Per neuron, the geometric mean over stimulus conditions of var/mean; conditions with zero
    mean or zero variance are left out (a standard choice)."""
    ff = []
    for r in responses(pop, kind, sep):
        mu, var = r.mean(1), r.var(1, ddof=1)
        ff.append(np.where((mu > 0) & (var > 0), var / np.where(mu > 0, mu, 1), np.nan))
    ff = np.stack(ff, 1)
    return np.exp(np.nanmean(np.log(ff), 1))


# --- modulation ---------------------------------------------------------------------------------------

def modulation(pop, sep):
    """Per neuron, the geometric mean over target orientations of mean(crowded)/mean(alone);
    NaN where a target-alone or crowded mean is zero."""
    ta, tc = tuning(pop, "alone"), tuning(pop, "crowd", sep)
    with np.errstate(divide="ignore", invalid="ignore"):
        lr = np.log(tc) - np.log(ta)
    lr[~np.isfinite(lr)] = np.nan
    return np.exp(np.mean(lr, 1))


def modulation_null(pop, sep, rng, n_perm=1000, pool="orientation"):
    """Null modulation indices (neurons x n_perm): responses to targets alone and with distractors
    combined, resampled with replacement in the experimental numbers. pool='orientation' combines
    within each target orientation, 'all' over all orientations."""
    ra, rc = responses(pop, "alone"), responses(pop, "crowd", sep)
    nN = pop["counts"].shape[0]
    logs = np.zeros((nN, n_perm))
    if pool == "all":
        allc = np.concatenate(ra + rc, 1)
    for o in range(len(ra)):
        na, nc = ra[o].shape[1], rc[o].shape[1]
        comb = np.concatenate([ra[o], rc[o]], 1) if pool == "orientation" else allc
        K = comb.shape[1]
        ia = rng.integers(0, K, size=(n_perm, na))
        ic = rng.integers(0, K, size=(n_perm, nc))
        ma = comb[:, ia].mean(2)
        mc = comb[:, ic].mean(2)
        with np.errstate(divide="ignore", invalid="ignore"):
            logs += np.log(mc) - np.log(ma)
    logs /= len(ra)
    logs[~np.isfinite(logs)] = np.nan
    return np.exp(logs)


# --- tuning models ------------------------------------------------------------------------------------

def _poisson_ll(pred, counts_by_ori, single_trial=True):
    """Poisson log-likelihood (up to the log r! term when using means)."""
    pred = np.maximum(pred, EPS)
    if single_trial:
        return float(sum(np.sum(c * np.log(p) - p - _lgam(c)) for p, c in zip(pred, counts_by_ori)))
    means = np.array([c.mean() for c in counts_by_ori])
    return float(np.sum(means * np.log(pred) - pred))


def _lgam(c):
    from scipy.special import gammaln
    return gammaln(np.asarray(c, float) + 1)


def fit_affine(rT, counts_by_ori, single_trial=True):
    """m, a for rTD = max(m*rT + a*mean(rT), 0) by maximum Poisson likelihood, Nelder-Mead from
    several starts (a standard choice)."""
    mu = rT.mean()

    def nll(th):
        return -_poisson_ll(th[0] * rT + th[1] * mu, counts_by_ori, single_trial)

    best = None
    for start in ((1, 0), (0.5, 0.5), (0, 1), (-0.5, 1.5), (1.5, -0.5)):
        r = optimize.minimize(nll, np.array(start, float), method="Nelder-Mead",
                              options=dict(xatol=1e-6, fatol=1e-8, maxiter=4000))
        if best is None or r.fun < best.fun:
            best = r
    return best.x[0], best.x[1], -best.fun


def fit_single(rT, counts_by_ori, form, single_trial=True):
    """One-parameter models of Figure S5: 'mult' c*rT, 'add' rT + c*mean(rT)."""
    mu = rT.mean()
    f = (lambda c: c * rT) if form == "mult" else (lambda c: rT + c * mu)

    def nll(c):
        return -_poisson_ll(f(c), counts_by_ori, single_trial)

    lo, hi = (0.0, 20.0) if form == "mult" else (-1.0, 20.0)
    r = optimize.minimize_scalar(nll, bounds=(lo, hi), method="bounded", options=dict(xatol=1e-6))
    return float(r.x), -float(r.fun)


def even_odd_reliability(pop, kind="alone", sep=None, config=None):
    """Correlation between the tuning from even and from odd presentations of each target
    orientation, in the order the epochs are stored."""
    ev, od = [], []
    for r in responses(pop, kind, sep, config):
        ev.append(r[:, 0::2].mean(1))
        od.append(r[:, 1::2].mean(1))
    ev, od = np.stack(ev, 1), np.stack(od, 1)
    return rowcorr(ev, od)


def random_split_reliability(pop, rng, n_split=20):
    """As `even_odd_reliability`, with the presentations of each target orientation split into two
    random halves instead of even and odd ones, averaged over `n_split` splits (does not depend on
    the stored order; 20 splits is a standard choice)."""
    rs = []
    for _ in range(n_split):
        ev, od = [], []
        for r in responses(pop, "alone"):
            perm = rng.permutation(r.shape[1])
            h = r.shape[1] // 2
            ev.append(r[:, perm[:h]].mean(1))
            od.append(r[:, perm[h:]].mean(1))
        rs.append(rowcorr(np.stack(ev, 1), np.stack(od, 1)))
    return np.nanmean(np.stack(rs), 0)


def rowcorr(a, b):
    a = a - a.mean(1, keepdims=True)
    b = b - b.mean(1, keepdims=True)
    den = np.sqrt((a ** 2).sum(1) * (b ** 2).sum(1))
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(den > 0, (a * b).sum(1) / den, np.nan)


def dprime(x1, x2):
    return (x1.mean() - x2.mean()) / np.sqrt(0.5 * (x1.var(ddof=1) + x2.var(ddof=1)))
