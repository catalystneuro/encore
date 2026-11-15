"""Loading and measures for dandiset 000130 (Sohn, Narain, Meirhaeghe & Jazayeri 2019, Neuron 103:934).

Dandiset 000130 holds one session (2016-12-11) of monkey H (Haydn) in the Ready-Set-Go task,
prepared for the Neural Latents Benchmark (NLB): a "train" file with the trial table and the
spikes of 54 units over the session, and a "test" file with 283 further trials whose task
variables are withheld and whose spikes are given for 40 of the units only. Every analysis here
uses the train file, streamed from the archive at the pinned version.

Where each parameter comes from (claims file claims/sohn-2019.yaml, its opening comment and the
criteria, unless said otherwise):

- Trials: completed trials (Set and Go present, tp > 0) not flagged `is_outlier`, the file's
  mixture-model flag (claims file, method choices). The neural analyses use the same trials (a
  standard choice: the Methods do not say whether the behavioural outliers are dropped from the
  neural averages).
- Units: mean rate over the file of at least 1 spike/s and at least 5 trials in each of the 40
  conditions (Methods, "Analysis of single- and multi-unit activity").
- Rates: spike counts in 20 ms bins, averaged over trials, in spikes/s, smoothed by a Gaussian of
  SD 40 ms (Methods, "Principal component analysis": "bin size: 20 ms, Gaussian smoothing kernel
  width: 40 ms"; the claims file reads the width as the SD). The kernel is renormalised over the
  bins of each trajectory, so that no bin outside the epoch enters (a standard choice).
- Estimation epoch: from Ready to the prior's longest ts, each bin averaging the trials whose Set
  comes at or after the end of the bin (attrition; Methods, "Principal component analysis").
  Production epoch: from Set to the shortest tp of that ts (same passage).
- PCA: per effector and direction ("dataset") and epoch, on the trajectories of both priors
  concatenated, mean-centred, not normalised; the fewest components reaching 75% of the variance.
- Encoding axis u: the mean of X(ts_max - d) - X(ts_min + d) for d = 0, 20, 40 ms ... while
  ts_min + d < ts_max - d, normalised (Methods, "Analysis of neural projection"). The state at
  time t is the bin that ends at t.
- Bayesian observer: continuous uniform prior on each range, measurement noise SD wm*ts, the
  posterior mean as te, production noise SD wp*te, an offset b per prior; wm, wp, bShort, bLong
  fit by maximum likelihood per dataset (Methods, "Analysis of behavior with a Bayesian model").
  Integrals are taken on grids of 301 points over +-5 SD of tm and over the prior range (a
  standard choice).
- GPFA: elephant's implementation of Yu et al. (2009), 20 ms bins, the latent dimensionality
  chosen from 4 and 8 by 3-fold cross-validated log-likelihood (claims file), orthonormalised
  latents. Seeds are fixed per claim.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import requests

DANDISET = "000130"
VERSION = "0.241017.1448"
TRAIN_PATH = "sub-Haydn/sub-Haydn_desc-train_ecephys.nwb"
TEST_PATH = "sub-Haydn/sub-Haydn_desc-test_ecephys.nwb"
API = "https://api.dandiarchive.org/api"

SHORT_TS = np.array([480, 560, 640, 720, 800])
LONG_TS = np.array([800, 900, 1000, 1100, 1200])
PRIOR_TS = {"Short": SHORT_TS, "Long": LONG_TS}
BIN = 20  # ms
SMOOTH_SD = 40  # ms
VAR_THRESHOLD = 0.75

# effector and direction: theta 0 is right and 180 is left (the file's description of `theta`)
DATASETS = [("Eye", "Left"), ("Eye", "Right"), ("Hand", "Left"), ("Hand", "Right")]


# ---------------------------------------------------------------- loading

def asset_url(path: str) -> str:
    """S3 URL of an asset of the pinned version."""
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/",
                     params={"path": path}, timeout=60)
    r.raise_for_status()
    hits = [a for a in r.json()["results"] if a["path"] == path]
    if len(hits) != 1:
        raise RuntimeError(f"{path} not found once in {DANDISET}/{VERSION}")
    meta = requests.get(f"{API}/assets/{hits[0]['asset_id']}/", timeout=60)
    meta.raise_for_status()
    s3 = [u for u in meta.json()["contentUrl"] if "s3" in u and "amazonaws" in u]
    if not s3:
        raise RuntimeError(f"no S3 URL for {path}")
    return s3[0]


def list_assets() -> pd.DataFrame:
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/",
                     params={"page_size": 100}, timeout=60)
    r.raise_for_status()
    return pd.DataFrame(r.json()["results"])[["path", "size", "asset_id"]]


def open_nwb(path: str):
    """Stream an NWB file of the pinned version; returns (nwbfile, io)."""
    import h5py
    import pynwb
    import remfile
    h5 = h5py.File(remfile.File(asset_url(path)), "r")
    io = pynwb.NWBHDF5IO(file=h5, load_namespaces=True)
    return io.read(), io


def load_session(path: str = TRAIN_PATH) -> dict:
    """Trial table, spike times (s) of every unit, and the unit table of one file."""
    nwb, io = open_nwb(path)
    trials = nwb.trials.to_dataframe().reset_index()
    u = nwb.units
    spikes = [np.asarray(u["spike_times"][i]) for i in range(len(u))]
    obs = [np.asarray(u["obs_intervals"][i]) for i in range(len(u))]
    units = pd.DataFrame({"id": u.id[:], "heldout": u["heldout"][:]})
    units["observed_s"] = [float(np.sum(o[:, 1] - o[:, 0])) for o in obs]
    units["n_spikes"] = [len(s) for s in spikes]
    units["rate"] = units.n_spikes / units.observed_s
    out = dict(nwb=nwb, io=io, trials=trials, spikes=spikes, units=units, obs=obs)
    return out


def label_trials(trials: pd.DataFrame) -> pd.DataFrame:
    t = trials.copy()
    t["prior"] = np.where(t.is_short, "Short", "Long")
    t["effector"] = np.where(t.is_eye, "Eye", "Hand")
    t["direction"] = t.theta.map({0.0: "Right", 180.0: "Left"})
    t["dataset"] = t.effector + " " + t.direction
    return t


def good_trials(trials: pd.DataFrame) -> pd.DataFrame:
    """Completed trials not flagged by the mixture model (claims file, method choices)."""
    t = label_trials(trials)
    ok = t.set_time.notna() & t.go_time.notna() & (t.tp > 0) & ~t.is_outlier
    return t[ok].reset_index(drop=True)


def select_units(sess: dict, good: pd.DataFrame, min_rate=1.0, min_trials=5) -> np.ndarray:
    """Indices of units with mean rate >= 1 spike/s and >= 5 trials in each of the 40 conditions.

    All units are observed over the whole file (their obs_intervals), so the trial count per
    condition is the same for every unit."""
    counts = good.groupby(["prior", "ts", "effector", "direction"]).size()
    enough = len(counts) == 40 and counts.min() >= min_trials
    keep = (sess["units"].rate.values >= min_rate) & enough
    return np.flatnonzero(keep)


# ---------------------------------------------------------------- binning and rates

def bin_counts(spikes: list, align: np.ndarray, start_ms: float, stop_ms: float,
               bin_ms: float = BIN) -> np.ndarray:
    """Spike counts, trials x bins x units, in bins [start, stop) relative to `align` (s)."""
    edges_rel = np.arange(start_ms, stop_ms + bin_ms / 2, bin_ms) / 1000.0
    nb = len(edges_rel) - 1
    out = np.zeros((len(align), nb, len(spikes)), dtype=np.float32)
    edges = align[:, None] + edges_rel[None, :]
    for k, s in enumerate(spikes):
        idx = np.searchsorted(s, edges)
        out[:, :, k] = np.diff(idx, axis=1)
    return out


def gauss_smooth(x: np.ndarray, sd_bins: float = SMOOTH_SD / BIN) -> np.ndarray:
    """Gaussian smoothing along axis 0, renormalised at the edges (no bins outside x)."""
    n = x.shape[0]
    t = np.arange(n)
    w = np.exp(-0.5 * ((t[:, None] - t[None, :]) / sd_bins) ** 2)
    w /= w.sum(axis=1, keepdims=True)
    return np.tensordot(w, x, axes=(1, 0))


def estimation_rates(spikes, good_sub: pd.DataFrame, ts_max: float, smooth=True):
    """Trial-averaged rates (spikes/s) from Ready to ts_max with attrition.

    Bin j covers [20j, 20j+20) ms after Ready and averages the trials with ts >= its end.
    Returns (rates bins x units, bin end times in ms, trials per bin)."""
    counts = bin_counts(spikes, good_sub.ready_time.values, 0, ts_max)
    ends = np.arange(BIN, ts_max + 1, BIN)
    valid = good_sub.ts.values[:, None] >= ends[None, :]
    n = valid.sum(axis=0)
    rates = (counts * valid[:, :, None]).sum(axis=0) / n[:, None] * (1000.0 / BIN)
    if smooth:
        rates = gauss_smooth(rates)
    return rates, ends, n


def aligned_rates(spikes, align_s: np.ndarray, start_ms: float, stop_ms: float, smooth=True):
    """Trial-averaged rates (spikes/s), bins x units, aligned to align_s, over [start, stop)."""
    counts = bin_counts(spikes, align_s, start_ms, stop_ms)
    rates = counts.mean(axis=0) * (1000.0 / BIN)
    return gauss_smooth(rates) if smooth else rates


def production_rates(spikes, good_sub: pd.DataFrame, prior: str, stop_ms=None, smooth=True):
    """Per ts of the prior: rates from Set to the shortest tp of that ts (or to stop_ms, using
    trials with tp >= stop_ms). Returns dict ts -> (bins x units)."""
    out = {}
    for ts in PRIOR_TS[prior]:
        sub = good_sub[(good_sub.prior == prior) & (good_sub.ts == ts)]
        if stop_ms is None:
            stop = np.floor(sub.tp.min() / BIN) * BIN
        else:
            stop = stop_ms
            sub = sub[sub.tp >= stop_ms]
        out[ts] = aligned_rates(spikes, sub.set_time.values, 0, stop, smooth=smooth)
    return out


# ---------------------------------------------------------------- PCA and geometry

def pca_fit(X: np.ndarray, threshold: float = VAR_THRESHOLD):
    """PCA of rows of X (mean-centred). Returns (mean, components k x units, k, explained ratio)."""
    mu = X.mean(axis=0)
    _, s, vt = np.linalg.svd(X - mu, full_matrices=False)
    ev = s ** 2 / np.sum(s ** 2)
    k = int(np.searchsorted(np.cumsum(ev), threshold - 1e-12) + 1)
    return mu, vt[:k], k, ev


def project(X, mu, comps):
    return (X - mu) @ comps.T


def encoding_axis(states: np.ndarray, ends: np.ndarray, ts_min: float, ts_max: float):
    """Unit vector u: mean of X(ts_max - d) - X(ts_min + d), d = 0, 20, ... while
    ts_min + d < ts_max - d (Methods, "Analysis of neural projection")."""
    pos = {int(round(e)): i for i, e in enumerate(ends)}
    diffs = []
    d = 0
    while ts_min + d < ts_max - d:
        diffs.append(states[pos[int(ts_max - d)]] - states[pos[int(ts_min + d)]])
        d += BIN
    v = np.mean(diffs, axis=0)
    return v / np.linalg.norm(v)


def step_speed(traj: np.ndarray) -> float:
    """Mean Euclidean distance between successive states."""
    return float(np.mean(np.linalg.norm(np.diff(traj, axis=0), axis=1)))


# ---------------------------------------------------------------- Bayesian observer

def _grid(lo, hi, n=301):
    return np.linspace(lo, hi, n)


def te_of_tm(tm: np.ndarray, prior: str, wm: float) -> np.ndarray:
    """Posterior mean of ts given tm, continuous uniform prior over the prior's range."""
    lo, hi = PRIOR_TS[prior][0], PRIOR_TS[prior][-1]
    s = _grid(lo, hi)
    sd = wm * s
    lik = np.exp(-0.5 * ((tm[..., None] - s) / sd) ** 2) / sd
    return (lik * s).sum(-1) / lik.sum(-1)


def _tm_nodes(ts, wm, n=301):
    z = np.linspace(-5, 5, n)
    w = np.exp(-0.5 * z ** 2)
    w /= w.sum()
    return ts + z * wm * ts, w


def bayes_loglik(params, df: pd.DataFrame) -> float:
    wm, wp, bS, bL = params
    if wm <= 0.01 or wp <= 0.01 or wm > 1 or wp > 1:
        return -np.inf
    ll = 0.0
    for (prior, ts), g in df.groupby(["prior", "ts"]):
        tm, w = _tm_nodes(ts, wm)
        te = te_of_tm(tm, prior, wm)
        b = bS if prior == "Short" else bL
        mu = te + b
        sd = wp * te
        tp = g.tp.values[:, None]
        dens = (np.exp(-0.5 * ((tp - mu) / sd) ** 2) / (np.sqrt(2 * np.pi) * sd) * w).sum(1)
        ll += np.sum(np.log(np.maximum(dens, 1e-300)))
    return ll


def fit_bayes(df: pd.DataFrame) -> dict:
    """ML fit of wm, wp, bShort, bLong on the trials of one dataset."""
    from scipy.optimize import minimize

    def unpack(z):  # log noise weights, offsets in units of 100 ms, so the simplex steps match
        return np.exp(z[0]), np.exp(z[1]), 100 * z[2], 100 * z[3]

    best = None
    for wm0 in (0.05, 0.1, 0.2):
        z0 = np.array([np.log(wm0), np.log(0.1), 0.2, 0.0])
        res = minimize(lambda z: -bayes_loglik(unpack(z), df), z0, method="Nelder-Mead",
                       options=dict(xatol=1e-5, fatol=1e-4, maxiter=6000, maxfev=6000))
        if best is None or res.fun < best.fun:
            best = res
    if not best.success or not np.isfinite(best.fun):
        raise RuntimeError(f"Bayesian model fit failed: {best.message}")
    wm, wp, bS, bL = unpack(best.x)
    return dict(wm=wm, wp=wp, bShort=bS, bLong=bL, loglik=-best.fun)


def bayes_predict(ts: float, prior: str, p: dict):
    """Model mean and SD of tp, and mean te, for one ts."""
    tm, w = _tm_nodes(ts, p["wm"])
    te = te_of_tm(tm, prior, p["wm"])
    b = p["bShort"] if prior == "Short" else p["bLong"]
    m = np.sum(w * (te + b))
    second = np.sum(w * ((p["wp"] * te) ** 2 + (te + b) ** 2))
    return m, np.sqrt(second - m ** 2), np.sum(w * te)


def te_mean(t: np.ndarray, prior: str, wm: float) -> np.ndarray:
    """Mean Bayesian estimate for ts = t (no offset), integrating over tm."""
    out = []
    for x in np.atleast_1d(t):
        tm, w = _tm_nodes(x, wm)
        out.append(np.sum(w * te_of_tm(tm, prior, wm)))
    return np.array(out)


# ---------------------------------------------------------------- regression helpers

def wls(y, x, w):
    """Weighted least squares y = a + b x. Returns a, b, fitted, weighted R2."""
    X = np.column_stack([np.ones_like(x), x])
    W = np.asarray(w, float)
    beta = np.linalg.solve(X.T @ (X * W[:, None]), X.T @ (W * y))
    fit = X @ beta
    ybar = np.sum(W * y) / np.sum(W)
    r2 = 1 - np.sum(W * (y - fit) ** 2) / np.sum(W * (y - ybar) ** 2)
    return beta[0], beta[1], fit, r2


# ---------------------------------------------------------------- GPFA

def gpfa_fit(spikes, good_sub: pd.DataFrame, x_dims=(4, 8), n_folds=3, seed=0):
    """GPFA on single trials from Ready to Set (20 ms bins), units given by `spikes`.

    The latent dimensionality is chosen from x_dims by n_folds-fold cross-validated
    log-likelihood (no cross-validation when x_dims holds one value). Spike times are given in
    ms so that ts / 20 ms is a whole number of bins. elephant fits on segments of 20 bins whose
    overlaps it draws from numpy's global generator, so each fit seeds it (from `seed`); the
    segment length is elephant's default, as in Yu et al.'s code. Returns (chosen dim, cv log-likelihoods, list of orthonormalised latent
    trajectories, each bins x dims, with bin j ending at 20(j+1) ms after Ready)."""
    import contextlib
    import io
    import logging
    import warnings
    import neo
    import quantities as pq
    from elephant import utils as elephant_utils
    from elephant.gpfa import GPFA

    def trains(sub):  # in ms, so that ts / 20 ms is an exact number of bins
        out = []
        for ready, ts in zip(sub.ready_time.values, sub.ts.values):
            t1 = ready + ts / 1000.0
            tr = []
            for s in spikes:
                i0, i1 = np.searchsorted(s, [ready, t1])
                rel = np.minimum((s[i0:i1] - ready) * 1000.0, ts - 1e-6)
                tr.append(neo.SpikeTrain(rel * pq.ms, t_start=0 * pq.ms, t_stop=float(ts) * pq.ms))
            out.append(tr)
        return out

    data = trains(good_sub)
    rng = np.random.default_rng(seed)
    folds = np.array_split(rng.permutation(len(data)), n_folds)
    cv = {}
    # elephant prints its progress and warns about bin rounding; both are silenced
    with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
        warnings.simplefilter("ignore")
        elephant_utils.logger.setLevel(logging.ERROR)
        for d in (x_dims if len(x_dims) > 1 else ()):
            ll = 0.0
            for k in range(n_folds):
                test = set(folds[k].tolist())
                train = [data[i] for i in range(len(data)) if i not in test]
                held = [data[i] for i in sorted(test)]
                g = GPFA(bin_size=BIN * pq.ms, x_dim=d, verbose=False)
                np.random.seed(seed + 1 + k)  # elephant draws the segment overlaps from np.random
                g.fit(train)
                ll += g.score(held)
            cv[d] = ll
        best = max(cv, key=cv.get) if cv else x_dims[0]
        g = GPFA(bin_size=BIN * pq.ms, x_dim=best, verbose=False)
        np.random.seed(seed)
        lat = g.fit_transform(data, returned_data=["latent_variable_orth"])
    return best, cv, [np.asarray(x).T for x in lat]


# ---------------------------------------------------------------- trial-averaged geometry

def dataset_geometry(spikes, d: pd.DataFrame, wm: float, smooth=True) -> dict:
    """Estimation and production trajectories, their PCA and the encoding-axis projections of
    one dataset (effector and direction). `wm` is the dataset's fitted measurement noise, used
    for te(t). Returns a dict with per-prior tables and the numbers of components."""
    est, out = {}, {"prior": {}}
    for prior in ("Short", "Long"):
        dp = d[d.prior == prior]
        est[prior] = estimation_rates(spikes, dp, PRIOR_TS[prior][-1], smooth=smooth)
    Xe = np.vstack([est[p][0] for p in est])
    mu, comps, k, ev = pca_fit(Xe)
    prod = {}
    for prior in ("Short", "Long"):
        prod[prior] = production_rates(spikes, d, prior, smooth=smooth)
    Xp = np.vstack([r for p in prod for r in prod[p].values()])
    mup, cp, kp, evp = pca_fit(Xp)
    out.update(k_est=k, k_prod=kp, ev_est=ev, ev_prod=evp, est_pca=(mu, comps),
               prod_pca=(mup, cp), est=est, prod=prod)
    for prior in ("Short", "Long"):
        R, ends, n = est[prior]
        X = project(R, mu, comps)
        tsv = PRIOR_TS[prior]
        u = encoding_axis(X, ends, tsv[0], tsv[-1])
        sel = (ends >= tsv[0]) & (ends <= tsv[-1])
        t = ends[sel].astype(float)
        xu = X[sel] @ u
        rows = []
        for ts in tsv:
            i = int(np.flatnonzero(ends == ts)[0])
            traj = project(prod[prior][ts], mup, cp)
            g = d[(d.prior == prior) & (d.ts == ts)]
            rows.append(dict(ts=ts, xu_set=float(X[i] @ u), speed=step_speed(traj),
                             duration_ms=len(traj) * BIN, mean_tp=g.tp.mean(), n_trials=len(g)))
        out["prior"][prior] = dict(X=X, ends=ends, n=n, u=u, t=t, xu=xu, w=n[sel],
                                   te=te_mean(t, prior, wm), per_ts=pd.DataFrame(rows))
    return out


def single_trial_speed(spikes, d: pd.DataFrame, prod_pca) -> np.ndarray:
    """Speed of each trial from Set to Go: smoothed single-trial rates (20 ms bins, SD 40 ms)
    projected into the dataset's production PC space, mean distance between successive bins."""
    mu, comps = prod_pca
    out = np.empty(len(d))
    for i, (st, tp) in enumerate(zip(d.set_time.values, d.tp.values)):
        stop = np.floor(tp / BIN) * BIN
        c = bin_counts(spikes, np.array([st]), 0, stop)[0] * (1000.0 / BIN)
        out[i] = step_speed(project(gauss_smooth(c), mu, comps))
    return out
