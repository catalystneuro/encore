"""Loading and measures for DANDI:000130 (Sohn, Narain, Meirhaeghe & Jazayeri 2019, Neuron).

The dandiset holds one session of monkey H (Haydn, 2016-12-11) of the Ready-Set-Go task with
two priors of the sample interval ts, split for the Neural Latents Benchmark into a train file
(trials with behaviour, 54 units) and a test file (unlabelled 1.7 s segments, 40 units).

Where each parameter comes from:

- Trials: completed (Set and Go present, no failure time, tp > 0) and not flagged by
  `is_outlier`, the file's flag from the paper's mixture model. Claims file, header.
- Units: mean rate over the file of at least 1 spike/s and at least 5 trials in every one of the
  40 conditions. Claims file, header; Methods, "Analysis of single- and multi-unit activity".
- Rates: 20 ms bins averaged over trials, in spikes/s, then smoothed with a Gaussian of SD 40 ms.
  Claims file, header (Methods, "Principal component analysis": "bin size: 20 ms, Gaussian
  smoothing kernel width: 40 ms"). The kernel is truncated at the ends of a window and
  renormalised there: a standard choice for edges, which the paper does not describe.
- Attrition: in the estimation epoch, the bin ending at t averages the trials whose nominal ts
  is at least t. Claims file, header; Methods ("firing rate at time t was computed from spikes in
  all trials in which Set occurred after t"). The nominal ts is used, as Set - Ready differs from
  it by at most 23.5 ms in the file (a standard choice; it keeps the five attrition groups).
- PCA: per dataset (effector and direction) and epoch, on the trajectories of both priors
  concatenated, keeping the fewest components that reach 75% of the variance. Claims file,
  header; Methods, "Principal component analysis".
- Encoding axis: mean of X(ts_max - d) - X(ts_min + d), d = 0, 20, ... while
  ts_min + d < ts_max - d, normalised. Claims file, header; Methods, "Analysis of neural
  projection".
- Bayesian observer: continuous uniform prior, measurement SD wm*ts, posterior-mean estimate,
  production SD wp*te, offset b per prior; fit by maximum likelihood. Claims file, header;
  Methods, "Analysis of behavior with a Bayesian model". Integration grids (241 points for tm,
  201 for the prior) are a standard numerical choice.
- GLM: Poisson, counts in the 80 ms before 480 ... 800 ms after Ready, BIC comparison. Claims
  file, glm-prior-ts; Methods, "Generalized linear model". The ts model of the Long prior uses
  the 80 ms before 800 ... 1200 ms, "that prior's 5 time indicators" (claims file), as the
  Methods use "two distinct GLMs" because "values of ts were different between the priors".
"""

import numpy as np
import pandas as pd

DANDISET_ID = "000130"
VERSION = "0.241017.1448"
TRAIN_PATH = "sub-Haydn/sub-Haydn_desc-train_ecephys.nwb"
TEST_PATH = "sub-Haydn/sub-Haydn_desc-test_ecephys.nwb"

BIN_MS = 20
SMOOTH_SD_MS = 40
DATASETS = ["Eye Left", "Eye Right", "Hand Left", "Hand Right"]
PRIORS = ["Short", "Long"]
TS = {"Short": [480, 560, 640, 720, 800], "Long": [800, 900, 1000, 1100, 1200]}


# ---------------------------------------------------------------- loading

def asset_url(path):
    """S3 URL of an asset of the pinned version."""
    from dandi.dandiapi import DandiAPIClient

    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, VERSION)
        return ds.get_asset_by_path(path).get_content_url(follow_redirects=1, strip_query=True)


def open_nwb(path):
    """Stream an NWB file of the pinned version; returns (nwbfile, io)."""
    import h5py
    import pynwb
    import remfile

    f = remfile.File(asset_url(path))
    io = pynwb.NWBHDF5IO(file=h5py.File(f, "r"), load_namespaces=True)
    return io.read(), io


def load_session():
    """Trials table and spike times of the train file.

    Returns a dict with `trials` (DataFrame with added columns), `spikes` (list of arrays, s),
    `unit_ids`, `heldout`, `obs_intervals` and `duration` (s observed)."""
    nwb, io = open_nwb(TRAIN_PATH)
    tr = nwb.trials.to_dataframe()
    u = nwb.units
    spikes = [np.asarray(u["spike_times"][i]) for i in range(len(u))]
    obs = [np.asarray(u["obs_intervals"][i]) for i in range(len(u))]
    unit_ids = np.asarray(u.id[:])
    heldout = np.asarray(u["heldout"][:])
    tr["prior"] = np.where(tr.is_short, "Short", "Long")
    tr["effector"] = np.where(tr.is_eye, "Eye", "Hand")
    tr["direction"] = np.where(tr.theta == 180, "Left", "Right")
    tr["dataset"] = tr.effector + " " + tr.direction
    tr["completed"] = (tr.set_time.notna() & tr.go_time.notna() & tr.bad_time.isna()
                       & (tr.tp > 0))
    tr["valid"] = tr.completed & ~tr.is_outlier
    tr["ts"] = tr.ts.round().astype(int)
    meta = dict(session_start=str(nwb.session_start_time), subject=nwb.subject.subject_id,
                species=nwb.subject.species, description=nwb.session_description)
    io.close()
    duration = np.sum(obs[0][:, 1] - obs[0][:, 0])
    return dict(trials=tr, spikes=spikes, unit_ids=unit_ids, heldout=heldout,
                obs_intervals=obs, duration=duration, meta=meta)


def select_units(sess, min_rate=1.0, min_trials=5):
    """Units with mean rate >= 1 spike/s over the file and >= 5 valid trials in each of the 40
    conditions (all units are observed over the whole session, so the trial rule applies to the
    session as a whole). Returns a boolean mask and the per-unit rates."""
    rates = np.array([len(s) for s in sess["spikes"]]) / sess["duration"]
    v = sess["trials"][sess["trials"].valid]
    counts = v.groupby(["prior", "ts", "effector", "direction"]).size()
    enough = (len(counts) == 40) and (counts.min() >= min_trials)
    return (rates >= min_rate) & enough, rates


# ---------------------------------------------------------------- binning and rates

def bin_counts(spikes, align, edges_ms):
    """Spike counts, array (trials, units, bins), for windows align + edges (align in s)."""
    edges = np.asarray(align)[:, None] + np.asarray(edges_ms)[None, :] / 1000.0
    out = np.empty((edges.shape[0], len(spikes), edges.shape[1] - 1))
    for j, s in enumerate(spikes):
        idx = np.searchsorted(s, edges)
        out[:, j, :] = np.diff(idx, axis=1)
    return out


def smooth(x, sd_ms=SMOOTH_SD_MS, bin_ms=BIN_MS, axis=0):
    """Gaussian smoothing along `axis`, kernel truncated at the edges and renormalised."""
    x = np.moveaxis(np.asarray(x, float), axis, 0)
    n = x.shape[0]
    sd = sd_ms / bin_ms
    t = np.arange(n)
    k = np.exp(-0.5 * ((t[:, None] - t[None, :]) / sd) ** 2)
    k /= k.sum(axis=1, keepdims=True)
    y = np.tensordot(k, x, axes=(1, 0))
    return np.moveaxis(y, 0, axis)


def estimation_rates(spikes, trials, ts_max, attrition=True):
    """Trial-averaged rates (bins x units, spikes/s) aligned to Ready, bins ending at
    20, 40, ..., ts_max ms; with attrition the bin ending at t uses trials with ts >= t.
    Returns (rates, n_trials_per_bin, bin_end_times_ms)."""
    edges = np.arange(0, ts_max + BIN_MS, BIN_MS)
    c = bin_counts(spikes, trials.ready_time.values, edges)
    ends = edges[1:]
    if attrition:
        use = trials.ts.values[:, None] >= ends[None, :]
    else:
        use = np.ones((len(trials), len(ends)), bool)
    n = use.sum(0)
    tot = np.einsum("tub,tb->bu", c, use.astype(float))
    r = tot / np.maximum(n, 1)[:, None] / (BIN_MS / 1000.0)
    return smooth(r), n, ends


def aligned_rates(spikes, align_s, start_ms, stop_ms):
    """Trial-averaged smoothed rates (bins x units) for align + [start, stop) in 20 ms bins."""
    edges = np.arange(start_ms, stop_ms + 1e-9, BIN_MS)
    c = bin_counts(spikes, align_s, edges)
    r = c.mean(0).T / (BIN_MS / 1000.0)
    return smooth(r), edges[1:]


def production_rates(spikes, trials):
    """Per prior and ts: rates from Set to the shortest tp of that condition (whole 20 ms bins),
    as a dict (prior, ts) -> (rates, bin_end_times_ms, n_trials, shortest_tp). The two priors'
    ts = 800 trials are kept apart, as the Methods' 16 matrices are per prior ("Principal
    component analysis")."""
    out = {}
    for (prior, ts), g in trials.groupby(["prior", "ts"]):
        tmin = g.tp.min()
        stop = int(np.floor(tmin / BIN_MS) * BIN_MS)
        r, ends = aligned_rates(spikes, g.set_time.values, 0, stop)
        out[(prior, ts)] = (r, ends, len(g), tmin)
    return out


# ---------------------------------------------------------------- PCA and geometry

def pca(blocks, frac=0.75):
    """PCA on concatenated (time x units) blocks. Returns dict with mean, components (k x units),
    explained ratio (all), and k, the fewest components reaching `frac`."""
    X = np.vstack(blocks)
    mu = X.mean(0)
    U, S, Vt = np.linalg.svd(X - mu, full_matrices=False)
    ev = S ** 2 / np.sum(S ** 2)
    k = int(np.searchsorted(np.cumsum(ev), frac) + 1)
    return dict(mean=mu, components=Vt, explained=ev, k=k)


def project(p, R, k=None):
    k = p["k"] if k is None else k
    return (R - p["mean"]) @ p["components"][:k].T


def encoding_axis(X, times, t_min, t_max):
    """Mean of X(t_max - d) - X(t_min + d) for d = 0, 20, ... while t_min + d < t_max - d,
    normalised. X rows are states at `times` (ms)."""
    times = list(times)
    vecs = []
    d = 0
    while t_min + d < t_max - d:
        vecs.append(X[times.index(t_max - d)] - X[times.index(t_min + d)])
        d += BIN_MS
    u = np.mean(vecs, 0)
    return u / np.linalg.norm(u), len(vecs)


def mean_step(X):
    """Mean Euclidean distance between successive states (rows)."""
    return float(np.mean(np.linalg.norm(np.diff(X, axis=0), axis=1)))


# ---------------------------------------------------------------- statistics

def wls(x, y, w):
    """Weighted least squares y = a + b x. Returns dict a, b, se_b, r2 (weighted), rmse
    (unweighted residuals), wrmse (weighted), resid."""
    x, y, w = (np.asarray(v, float) for v in (x, y, w))
    W = w / w.sum()
    xm, ym = np.sum(W * x), np.sum(W * y)
    b = np.sum(W * (x - xm) * (y - ym)) / np.sum(W * (x - xm) ** 2)
    a = ym - b * xm
    res = y - (a + b * x)
    r2 = 1 - np.sum(W * res ** 2) / np.sum(W * (y - ym) ** 2)
    return dict(a=a, b=b, r2=r2, rmse=float(np.sqrt(np.mean(res ** 2))),
                wrmse=float(np.sqrt(np.sum(W * res ** 2))), resid=res)


def increments(means):
    """Extreme (mean of first and last) and middle (mean of second and third) increments of a
    5-point profile."""
    d = np.diff(np.asarray(means, float))
    return (d[0] + d[3]) / 2, (d[1] + d[2]) / 2


# ---------------------------------------------------------------- Bayesian observer

def _grids(ts, wm, lo, hi, n_tm=241, n_prior=201):
    """tm grid and Gaussian weights for one ts; te(tm) for a uniform prior on [lo, hi]."""
    sd = wm * ts
    tm = np.linspace(max(ts - 5 * sd, 1.0), ts + 5 * sd, n_tm)
    w = np.exp(-0.5 * ((tm - ts) / sd) ** 2)
    w /= w.sum()
    sp = np.linspace(lo, hi, n_prior)
    lik = np.exp(-0.5 * ((tm[:, None] - sp[None, :]) / (wm * sp[None, :])) ** 2) / (wm * sp[None, :])
    te = (lik * sp[None, :]).sum(1) / lik.sum(1)
    return tm, w, te


def bls_predict(ts, wm, wp, b, lo, hi):
    """Mean estimate te(ts), predicted mean tp and SD of tp for a scalar ts."""
    _, w, te = _grids(ts, wm, lo, hi)
    m_te = np.sum(w * te)
    m = m_te + b
    v = np.sum(w * ((wp * te) ** 2 + (te + b) ** 2)) - m ** 2
    return m_te, m, np.sqrt(v)


def bls_nll(params, data):
    """Negative log-likelihood; params = (log wm, log wp, bShort/100, bLong/100) (offsets in
    units of 100 ms, so that the simplex moves them); data = list of (prior, ts, tp array)."""
    wm, wp = np.exp(params[0]), np.exp(params[1])
    bs = {"Short": 100 * params[2], "Long": 100 * params[3]}
    nll = 0.0
    for prior, ts, tp in data:
        lo, hi = TS[prior][0], TS[prior][-1]
        _, w, te = _grids(ts, wm, lo, hi)
        mu = te + bs[prior]
        sd = wp * te
        p = (w[None, :] * np.exp(-0.5 * ((tp[:, None] - mu[None, :]) / sd[None, :]) ** 2)
             / (np.sqrt(2 * np.pi) * sd[None, :])).sum(1)
        nll -= np.sum(np.log(np.maximum(p, 1e-300)))
    return nll


def fit_bls(trials):
    """Maximum-likelihood fit of (wm, wp, bShort, bLong) to the valid trials of one dataset,
    by Nelder-Mead from 8 starting points (wm 0.05 or 0.15, wp 0.05 or 0.1, offsets 10 or
    -10 ms); the best of the 8 is kept. The starting points are a standard numerical choice."""
    from scipy.optimize import minimize

    data = [(p, ts, g.tp.values) for (p, ts), g in trials.groupby(["prior", "ts"])]
    best = None
    for wm0 in (0.05, 0.15):
        for wp0 in (0.05, 0.1):
            for b0 in (0.1, -0.1):
                r = minimize(bls_nll, [np.log(wm0), np.log(wp0), b0, b0], args=(data,),
                             method="Nelder-Mead",
                             options=dict(maxiter=4000, xatol=1e-5, fatol=1e-4))
                if best is None or r.fun < best.fun:
                    best = r
    wm, wp = np.exp(best.x[:2])
    return dict(wm=wm, wp=wp, bShort=100 * best.x[2], bLong=100 * best.x[3], nll=best.fun,
                success=bool(best.success))


# ---------------------------------------------------------------- GLM

def glm_bic(y, X):
    """BIC = k log n - 2 logL of a Poisson GLM (statsmodels); None if the fit fails."""
    import statsmodels.api as sm

    try:
        r = sm.GLM(y, X, family=sm.families.Poisson()).fit()
    except Exception:
        return None
    if not np.isfinite(r.llf):
        return None
    return X.shape[1] * np.log(len(y)) - 2 * r.llf
