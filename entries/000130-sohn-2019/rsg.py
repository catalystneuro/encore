"""Loading and measures for the Ready-Set-Go data of dandiset 000130.

Sohn, Narain, Meirhaeghe & Jazayeri (2019), Neuron, doi:10.1016/j.neuron.2019.06.012.

The dandiset is the DMFC_RSG set of the Neural Latents Benchmark: one session of monkey H
(Haydn, 2016-12-11). The train file holds the trial table with every task variable and the
spike times of 54 units; the test file holds 283 further trials without task variables and
only 40 of the units. Analyses use the train file. Files are streamed from the archive at the
pinned version; nothing is written to disk.

Where the parameters come from:

- From the paper's STAR Methods: units kept with a mean rate of at least 1 spike/s and at least
  5 trials per condition (`MIN_RATE`, `MIN_TRIALS`); 20 ms bins and a 40 ms Gaussian kernel for
  population rates (`BIN_MS`, `SMOOTH_MS`, read here as the kernel's SD); attrition in the
  estimation epoch; production rates up to the shortest tp of each ts; PCA keeping the
  components that explain 75% of the variance (`VAR_KEPT`); the encoding axis from difference
  vectors every 20 ms; the 80 ms GLM window before Set (`GLM_WINDOW_MS`) and BIC comparison;
  the Bayesian observer with scalar measurement and production noise, a uniform prior, the
  posterior mean, and an offset per prior; GPFA on single trials with cross-validation.
- Common choices made here where the Methods leave it open (see the claims file): kernel width
  read as SD; rates averaged per 20 ms bin and then smoothed; no normalisation of rates before
  PCA (soft normalisation and z-scoring, `unit_scale`, are variants); difference vectors for the encoding axis averaged up to the middle of the support;
  speed as the mean step between successive 20 ms states; the GPFA latent dimensionality chosen
  from `GPFA_DIMS` by 3-fold cross-validation, and `GPFA_EM_ITERS` EM iterations.
- The flag `is_outlier` in the trial table is the paper's mixture-model exclusion and is used as
  given; `outlier_mixture` refits that model as a check.
"""

from __future__ import annotations

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import optimize, stats
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "000130"
DANDISET_VERSION = "0.241017.1448"
TRAIN = "sub-Haydn/sub-Haydn_desc-train_ecephys.nwb"
TEST = "sub-Haydn/sub-Haydn_desc-test_ecephys.nwb"

MIN_RATE = 1.0         # spikes/s, Methods
MIN_TRIALS = 5         # per condition, Methods
BIN_MS = 20            # Methods
SMOOTH_MS = 40         # Methods, "Gaussian smoothing kernel width", read as SD
VAR_KEPT = 0.75        # Methods
GLM_WINDOW_MS = 80     # Methods
GPFA_DIMS = (4, 8)     # choice here; the Methods say only "with cross validation"
GPFA_EM_ITERS = 100    # choice here, to keep the run short

SHORT_TS = (480, 560, 640, 720, 800)
LONG_TS = (800, 900, 1000, 1100, 1200)
DATASETS = [(True, 0.0), (True, 180.0), (False, 0.0), (False, 180.0)]


def dataset_name(is_eye: bool, theta: float) -> str:
    return f"{'Eye' if is_eye else 'Hand'} {'Right' if theta == 0 else 'Left'}"


def prior_ts(is_short: bool) -> tuple:
    return SHORT_TS if is_short else LONG_TS


# --- loading -------------------------------------------------------------------------------

def _str(value):
    return value.decode() if isinstance(value, bytes) else value


def asset_urls() -> dict:
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)
                for a in dandiset.get_assets()}


def read_file(url: str) -> dict:
    """The trial table, units and descriptive metadata of one NWB file."""
    with h5py.File(remfile.File(url), "r") as f:
        t = f["intervals/trials"]
        cols = [_str(c) for c in t.attrs["colnames"]]
        trials = pd.DataFrame({c: (t[c][:].astype(str) if t[c].dtype == object else t[c][:]) for c in cols})
        descriptions = {c: _str(t[c].attrs.get("description", "")) for c in cols}
        u = f["units"]
        index = u["spike_times_index"][:]
        spikes = np.split(u["spike_times"][:], index[:-1])
        oi_index = u["obs_intervals_index"][:]
        obs = np.split(u["obs_intervals"][:], oi_index[:-1])
        unit_ids, heldout = u["id"][:], u["heldout"][:]
        electrodes = f["general/extracellular_ephys/electrodes"]
        meta = {
            "session_description": _str(f["session_description"][()]),
            "session_start_time": _str(f["session_start_time"][()]),
            "session_id": _str(f["general/session_id"][()]),
            "subject_id": _str(f["general/subject/subject_id"][()]),
            "species": _str(f["general/subject/species"][()]),
            "age": _str(f["general/subject/age"][()]),
            "related_publications": [_str(x) for x in f["general/related_publications"][:]],
            "electrode_location": sorted({_str(x) for x in electrodes["location"][:]}),
            "electrode_x_all_nan": bool(np.isnan(electrodes["x"][:]).all()),
            "n_electrodes": len(electrodes["id"][:]),
        }
    return {"trials": trials, "descriptions": descriptions, "spikes": spikes, "unit_ids": unit_ids,
            "heldout": heldout, "obs_intervals": obs, "meta": meta}


def load() -> dict:
    """Both files of the pinned version, as returned by `read_file`."""
    urls = asset_urls()
    return {"train": read_file(urls[TRAIN]), "test": read_file(urls[TEST]), "urls": urls}


def completed(trials: pd.DataFrame) -> pd.DataFrame:
    """Completed trials (with Set and Go) not flagged as outliers."""
    ok = trials.set_time.notna() & trials.go_time.notna() & ~trials.is_outlier.astype(bool)
    return trials[ok].copy()


def select_units(session: dict, trials: pd.DataFrame) -> tuple[np.ndarray, pd.DataFrame]:
    """Units kept by the Methods' rule, and a table of rates and trial counts."""
    t0 = min(iv[0, 0] for iv in session["obs_intervals"])
    t1 = max(iv[-1, 1] for iv in session["obs_intervals"])
    observed = np.array([np.sum(iv[:, 1] - iv[:, 0]) for iv in session["obs_intervals"]])
    rate = np.array([len(s) for s in session["spikes"]]) / observed
    counts = trials.groupby(["is_short", "ts", "is_eye", "theta"]).size()
    n_cond = len(counts)
    min_trials = int(counts.min())
    table = pd.DataFrame({"unit": session["unit_ids"], "heldout": session["heldout"], "rate": rate,
                          "observed_s": observed})
    keep = (rate >= MIN_RATE) & (min_trials >= MIN_TRIALS) & (n_cond == 40)
    table["kept"] = keep
    table.attrs.update(conditions=n_cond, min_trials=min_trials, span=(t0, t1))
    return np.flatnonzero(keep), table


# --- spike counts and rates ----------------------------------------------------------------

def counts(spikes: list, units, align: np.ndarray, start_ms: float, stop_ms: float,
           bin_ms: float = BIN_MS) -> np.ndarray:
    """Spike counts, trials x bins x units, in bins from start to stop relative to `align` (s)."""
    edges = np.arange(start_ms, stop_ms + 1e-9, bin_ms) / 1000.0
    out = np.empty((len(align), len(edges) - 1, len(units)))
    for j, u in enumerate(units):
        s = spikes[u]
        pos = np.searchsorted(s, align[:, None] + edges[None, :])
        out[:, :, j] = np.diff(pos, axis=1)
    return out


def smooth(rate: np.ndarray) -> np.ndarray:
    """Gaussian smoothing along time (axis 0) with SD `SMOOTH_MS`."""
    return gaussian_filter1d(rate, SMOOTH_MS / BIN_MS, axis=0, mode="nearest")


def estimation_rates(spikes, units, trials: pd.DataFrame, t_max: float):
    """Rates from Ready to `t_max` ms with attrition: each bin averages the trials whose Set
    comes after the end of the bin. Returns rates (bins x units, spikes/s), bin end times (ms
    after Ready) and the number of trials in each bin."""
    c = counts(spikes, units, trials.ready_time.to_numpy(), 0, t_max)
    elapsed = (trials.set_time - trials.ready_time).to_numpy() * 1000
    return attrition_rates(c, elapsed)


def attrition_rates(c: np.ndarray, elapsed: np.ndarray):
    """`estimation_rates` from counts already taken (trials x bins x units from Ready)."""
    ends = np.arange(1, c.shape[1] + 1) * BIN_MS
    use = elapsed[:, None] >= ends[None, :] - 1e-6
    n = use.sum(0)
    mean = np.einsum("tb,tbu->bu", use, c) / np.maximum(n, 1)[:, None]
    return smooth(mean * 1000 / BIN_MS), ends, n


def aligned_rates(spikes, units, align: np.ndarray, start_ms: float, stop_ms: float):
    """Trial-averaged smoothed rates (bins x units, spikes/s) aligned to `align`."""
    c = counts(spikes, units, align, start_ms, stop_ms)
    return smooth(c.mean(0) * 1000 / BIN_MS)


def production_rates(spikes, units, trials: pd.DataFrame, stop_ms: float | None = None):
    """Rates from Set to the shortest tp of these trials (or to `stop_ms`)."""
    if stop_ms is None:
        stop_ms = np.floor(trials.tp.min() / BIN_MS) * BIN_MS
    return aligned_rates(spikes, units, trials.set_time.to_numpy(), 0, stop_ms)


# --- population measures -------------------------------------------------------------------

class PCA:
    """PCA on stacked rate matrices, keeping the components that reach `kept` of the variance,
    and at least `min_n`."""

    def __init__(self, matrices: list, kept: float = VAR_KEPT, min_n: int = 1):
        data = np.vstack(matrices)
        self.mean = data.mean(0)
        _, s, vt = np.linalg.svd(data - self.mean, full_matrices=False)
        self.explained = s ** 2 / np.sum(s ** 2)
        self.n = max(int(np.searchsorted(np.cumsum(self.explained), kept - 1e-12) + 1), min_n)
        self.components = vt[: self.n]

    def __call__(self, x: np.ndarray) -> np.ndarray:
        return (x - self.mean) @ self.components.T


def unit_scale(matrices: list, how: str) -> np.ndarray:
    """Divisor per unit for normalised rates, from the stacked matrices (bins x units):
    `soft`, the range plus 5 spikes/s (soft normalisation, a common choice; the Methods do
    not say whether rates were normalised), or `z`, the SD."""
    data = np.vstack(matrices)
    if how == "soft":
        return np.ptp(data, axis=0) + 5.0
    return np.maximum(data.std(0), 1e-9)


def encoding_axis(states: np.ndarray, times: np.ndarray, t_min: float, t_max: float) -> np.ndarray:
    """Unit vector from the mean of X(t_max - d) - X(t_min + d), d = 0, 20, 40 ... ms, while
    t_min + d < t_max - d."""
    vectors = []
    d = 0.0
    while t_min + d < t_max - d:
        i, j = np.argmin(abs(times - (t_min + d))), np.argmin(abs(times - (t_max - d)))
        vectors.append(states[j] - states[i])
        d += BIN_MS
    u = np.mean(vectors, axis=0)
    return u / np.linalg.norm(u)


def step_speed(states: np.ndarray) -> float:
    """Mean Euclidean distance between successive states."""
    return float(np.mean(np.linalg.norm(np.diff(states, axis=0), axis=1)))


def weighted_fit(x, y, w):
    """Weighted least squares y = a + b x; returns a, b, weighted R2 and RMSE of the fit."""
    x, y, w = map(np.asarray, (x, y, w))
    design = np.column_stack([np.ones_like(x), x])
    sw = np.sqrt(w)
    coef, *_ = np.linalg.lstsq(design * sw[:, None], y * sw, rcond=None)
    pred = design @ coef
    ybar = np.sum(w * y) / np.sum(w)
    r2 = 1 - np.sum(w * (y - pred) ** 2) / np.sum(w * (y - ybar) ** 2)
    rmse = float(np.sqrt(np.mean((y - pred) ** 2)))
    return coef[0], coef[1], float(r2), rmse


def increments(means) -> tuple[float, float]:
    """Mean increment at the extremes (first and last) and in the middle (second and third)
    of five ordered values."""
    d = np.diff(np.asarray(means, float))
    return (d[0] + d[3]) / 2, (d[1] + d[2]) / 2


# --- behaviour -----------------------------------------------------------------------------

def weighted_slope(ts, tp):
    """Regression of tp on ts with each trial weighted by 1 / variance of tp at its ts. Returns
    slope, its standard error, and the 95% interval."""
    df = pd.DataFrame({"ts": ts, "tp": tp})
    var = df.groupby("ts").tp.transform("var")
    w = 1 / var
    x, y = df.ts.to_numpy(), df.tp.to_numpy()
    design = np.column_stack([np.ones_like(x), x])
    sw = np.sqrt(w.to_numpy())
    coef, *_ = np.linalg.lstsq(design * sw[:, None], y * sw, rcond=None)
    resid = (y - design @ coef) * sw
    dof = len(y) - 2
    sigma2 = np.sum(resid ** 2) / dof
    cov = sigma2 * np.linalg.inv((design * sw[:, None]).T @ (design * sw[:, None]))
    se = np.sqrt(cov[1, 1])
    q = stats.t.ppf(0.975, dof)
    return coef[1], se, (coef[1] - q * se, coef[1] + q * se)


def outlier_mixture(tp: np.ndarray, ts: float, iters: int = 200) -> np.ndarray:
    """Posterior probability of the lapse component for each trial, under a mixture of a
    Gaussian and a uniform distribution from 0 to 3 ts (Methods)."""
    tp = np.asarray(tp, float)
    mu, sd, p = np.median(tp), max(np.std(tp), 1.0), 0.05
    lapse = 1 / (3 * ts)
    for _ in range(iters):
        g = (1 - p) * stats.norm.pdf(tp, mu, sd)
        l = p * lapse * ((tp >= 0) & (tp <= 3 * ts))
        r = l / np.maximum(g + l, 1e-300)
        w = 1 - r
        mu = np.sum(w * tp) / np.sum(w)
        sd = max(np.sqrt(np.sum(w * (tp - mu) ** 2) / np.sum(w)), 1.0)
        p = np.clip(r.mean(), 1e-6, 0.5)
    return r


class BayesObserver:
    """Bayesian observer of the Methods: tm ~ N(ts, wm ts), te = posterior mean under a uniform
    prior on the range of ts, tp ~ N(te + b, wp te), with an offset b per prior."""

    GRID = 400

    def __init__(self, wm=0.1, wp=0.08, b_short=0.0, b_long=0.0):
        self.wm, self.wp, self.b = wm, wp, {True: b_short, False: b_long}

    @staticmethod
    def estimator(tm: np.ndarray, lo: float, hi: float, wm: float) -> np.ndarray:
        s = np.linspace(lo, hi, 201)
        like = np.exp(-0.5 * ((tm[:, None] - s[None, :]) / (wm * s[None, :])) ** 2) / s[None, :]
        return (like * s).sum(1) / np.maximum(like.sum(1), 1e-300)

    def _grid(self, is_short: bool):
        ts = prior_ts(is_short)
        lo, hi = min(ts), max(ts)
        tm = np.linspace(lo * (1 - 5 * self.wm), hi * (1 + 5 * self.wm), self.GRID)
        return tm, self.estimator(tm, lo, hi, self.wm)

    def _p_tm(self, tm, ts):
        p = stats.norm.pdf(tm[None, :], ts[:, None], self.wm * ts[:, None])
        return p / p.sum(1, keepdims=True)

    def loglik(self, ts, tp, is_short: bool) -> float:
        tm, te = self._grid(is_short)
        p_tm = self._p_tm(tm, np.asarray(ts, float))
        p_tp = stats.norm.pdf(np.asarray(tp, float)[:, None], te[None, :] + self.b[is_short],
                              self.wp * te[None, :])
        return float(np.sum(np.log(np.maximum((p_tm * p_tp).sum(1), 1e-300))))

    def moments(self, ts, is_short: bool):
        """Mean te, and mean and SD of tp, for each ts."""
        tm, te = self._grid(is_short)
        ts = np.asarray(ts, float)
        p_tm = self._p_tm(tm, ts)
        mean_te = p_tm @ te
        mean_tp = mean_te + self.b[is_short]
        second = p_tm @ (te ** 2 * (1 + self.wp ** 2))
        sd_tp = np.sqrt(second - mean_te ** 2)
        return mean_te, mean_tp, sd_tp

    @classmethod
    def fit(cls, trials: pd.DataFrame) -> "BayesObserver":
        """Maximum likelihood fit of wm, wp, b_short and b_long to one dataset's trials."""
        groups = {s: g for s, g in trials.groupby("is_short")}

        def nll(theta):
            m = cls(*theta)
            if not (0.01 < m.wm < 0.5 and 0.01 < m.wp < 0.5):
                return 1e12
            return -sum(m.loglik(g.ts.to_numpy(), g.tp.to_numpy(), bool(s)) for s, g in groups.items())

        # Nelder-Mead from three starting points, with an explicit first simplex (steps of 0.03
        # for wm and wp, 20 ms for the offsets); the best fit is kept.
        best = None
        for wm0 in (0.05, 0.1, 0.2):
            x0 = np.array([wm0, 0.08, 0.0, 0.0])
            simplex = np.vstack([x0, x0 + np.diag([0.03, 0.03, 20.0, 20.0])])
            res = optimize.minimize(nll, x0=x0, method="Nelder-Mead",
                                    options={"initial_simplex": simplex, "xatol": 1e-3, "fatol": 1e-3,
                                             "maxiter": 3000})
            if best is None or res.fun < best.fun:
                best = res
        model = cls(*best.x)
        model.converged, model.nll = bool(best.success), float(best.fun)
        return model


# --- GPFA ----------------------------------------------------------------------------------

def estimation_spiketrains(spikes, units, trials: pd.DataFrame):
    """Single-trial spike trains from Ready to Set, as neo objects for elephant's GPFA."""
    import neo
    import quantities as pq
    out = []
    for ready, set_ in zip(trials.ready_time.to_numpy(), trials.set_time.to_numpy()):
        dur = set_ - ready
        out.append([neo.SpikeTrain((s[(s >= ready) & (s < set_)] - ready) * pq.s,
                                   t_start=0 * pq.s, t_stop=dur * pq.s) for s in (spikes[u] for u in units)])
    return out


def _quiet_elephant():
    """elephant logs each spike it moves across a bin edge; keep the notebook readable."""
    import logging

    import elephant.utils
    logging.getLogger(elephant.utils.__file__).setLevel(logging.ERROR)


def gpfa_folds(n: int, rng: np.random.Generator) -> np.ndarray:
    """Fold (0, 1 or 2) of each of `n` trials for 3-fold cross-validation."""
    return rng.permutation(n) % 3


def gpfa_cv_score(spiketrains, folds: np.ndarray, dim: int) -> float:
    """Summed test log-likelihood of GPFA with `dim` latents over the folds."""
    import contextlib
    import io
    import warnings

    import quantities as pq
    from elephant.gpfa import GPFA

    _quiet_elephant()
    total = 0.0
    with warnings.catch_warnings(), contextlib.redirect_stdout(io.StringIO()):
        warnings.simplefilter("ignore")
        for k in range(3):
            train = [s for s, f in zip(spiketrains, folds) if f != k]
            test = [s for s, f in zip(spiketrains, folds) if f == k]
            m = GPFA(bin_size=BIN_MS * pq.ms, x_dim=dim, em_max_iters=GPFA_EM_ITERS)
            m.fit(train)
            total += m.score(test)
    return total


def gpfa_model(spiketrains, dim: int):
    """GPFA with `dim` latents fit on all trials. Its `fit_info["log_likelihoods"]` holds the
    training log-likelihood every fifth EM iteration (elephant's default)."""
    import contextlib
    import io
    import warnings

    import quantities as pq
    from elephant.gpfa import GPFA

    _quiet_elephant()
    with warnings.catch_warnings(), contextlib.redirect_stdout(io.StringIO()):
        warnings.simplefilter("ignore")
        model = GPFA(bin_size=BIN_MS * pq.ms, x_dim=dim, em_max_iters=GPFA_EM_ITERS)
        model.fit(spiketrains)
    return model


def fit_gpfa(spiketrains, rng: np.random.Generator):
    """GPFA with the latent dimensionality from `GPFA_DIMS` chosen by 3-fold cross-validated
    log-likelihood. Returns the model fit on all trials, the chosen dimensionality, the
    cross-validated scores and the folds."""
    folds = gpfa_folds(len(spiketrains), rng)
    scores = {dim: gpfa_cv_score(spiketrains, folds, dim) for dim in GPFA_DIMS}
    best = max(scores, key=scores.get)
    return gpfa_model(spiketrains, best), best, scores, folds


def gpfa_transform(model, spiketrains):
    """Orthonormalised latent trajectories (latents x bins) of each trial, quietly."""
    import warnings
    _quiet_elephant()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return model.transform(spiketrains)
