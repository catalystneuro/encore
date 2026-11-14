"""Loading and measures for the Ready-Set-Go recording of dandiset 000130.

Sohn, Narain, Meirhaeghe & Jazayeri (2019), Neuron, doi:10.1016/j.neuron.2019.06.012.

The dandiset holds one session (2016-12-11) of monkey H ("Haydn"), prepared for the Neural
Latents Benchmark. The train file holds the trial table (event times, prior, effector, target
direction, ts, tp, the outlier flag of the paper's mixture model) and the spike times of all 54
units over the whole session; the test file holds 1.7 s segments of 283 further trials, for 40
units, with no task variables, and is not used for the analysis. Files are streamed from the
archive at the pinned version; nothing is written to disk.

Where the parameters come from (claims/sohn-2019.yaml is cited as "claims header" for the
method choices its opening comment fixes):

- Trials: completed trials (tp > 0) not flagged by `is_outlier` (claims header).
- Units: mean rate over the recording of at least 1 spike/s and at least 5 trials in each of
  the 40 conditions (claims header; STAR Methods, "Analysis of single- and multi-unit
  activity").
- `BIN_MS` = 20 ms bins and `SMOOTH_SD_MS` = 40 ms Gaussian smoothing of trial-averaged rates
  (claims header; STAR Methods, "Principal component analysis": "bin size: 20 ms, Gaussian
  smoothing kernel width: 40 ms"). Edges of a smoothed trajectory use the nearest value, a
  standard choice.
- Estimation epoch: from Ready to the longest ts of the prior; bin k (ending at 20(k+1) ms after
  Ready) averages the trials with ts >= 20(k+1) ms, so that Set comes after the end of the bin
  (attrition; claims header and STAR Methods, "Principal component analysis"). The state "at
  time t" is the bin ending at t.
- Production epoch: from Set to the shortest Set-to-Go time of the trials of that ts (claims
  header; STAR Methods). Spikes are aligned to the file's event times (`ready_time`,
  `set_time`, `go_time`); behaviour uses the `ts` and `tp` columns (claims header).
- PCA keeps the fewest components reaching `VAR_THRESHOLD` = 75% of the variance (claims
  header; STAR Methods).
- Encoding axis: the mean of X(ts_max - d) - X(ts_min + d) for d = 0, 20, 40 ... while
  ts_min + d < ts_max - d, normalised (claims header; STAR Methods, "Analysis of neural
  projection").
- Bayesian observer: continuous uniform prior over each range, measurement noise SD wm*ts,
  posterior mean as te, production noise SD wp*te, offset b per prior, fit by maximum
  likelihood per dataset (claims header; STAR Methods, "Analysis of behavior with a Bayesian
  model"). The integration grids (`TM_GRID_N`, `TS_GRID_N`) are a standard numerical choice.
"""

from __future__ import annotations

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import optimize
from scipy.ndimage import gaussian_filter1d
from sklearn.decomposition import PCA

DANDISET_ID = "000130"
DANDISET_VERSION = "0.241017.1448"
TRAIN_PATH = "sub-Haydn/sub-Haydn_desc-train_ecephys.nwb"
TEST_PATH = "sub-Haydn/sub-Haydn_desc-test_ecephys.nwb"

BIN_MS = 20
SMOOTH_SD_MS = 40
VAR_THRESHOLD = 0.75
MIN_RATE = 1.0
MIN_TRIALS = 5
SHORT_TS = (480, 560, 640, 720, 800)
LONG_TS = (800, 900, 1000, 1100, 1200)
PRIOR_TS = {"Short": SHORT_TS, "Long": LONG_TS}
TM_GRID_N = 600
TS_GRID_N = 400

# The four "datasets" of the paper (effector x target direction); theta 0 is right, 180 left.
DATASETS = {"Eye Right": (True, 0.0), "Eye Left": (True, 180.0),
            "Hand Right": (False, 0.0), "Hand Left": (False, 180.0)}


def asset_urls() -> dict[str, str]:
    """Streaming URL of every NWB file at the pinned version, by path."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)
                for a in dandiset.get_assets() if a.path.endswith(".nwb")}


def _text(value):
    return value.decode() if isinstance(value, bytes) else value


def _read_table(group) -> pd.DataFrame:
    """A DynamicTable without ragged columns, read with h5py."""
    cols = {}
    for name in _text(group.attrs["colnames"]):
        name = _text(name)
        data = group[name][()]
        if data.dtype.kind in "SO":
            data = np.array([_text(x) for x in data])
        cols[name] = data
    return pd.DataFrame(cols, index=group["id"][()])


def _ragged(group, name):
    data, index = group[name][()], group[name + "_index"][()]
    return np.split(data, index[:-1])


def load_file(url: str) -> dict:
    """Trial table, unit table and spike times of one NWB file, with the column descriptions."""
    with h5py.File(remfile.File(url), "r") as f:
        trials = _read_table(f["intervals/trials"])
        tr_desc = {c: _text(f["intervals/trials"][c].attrs.get("description", ""))
                   for c in trials.columns}
        units = f["units"]
        spikes = _ragged(units, "spike_times")
        obs = [x.reshape(-1, 2) for x in _ragged(units, "obs_intervals")]
        unit_table = pd.DataFrame({"heldout": units["heldout"][()].astype(bool),
                                   "n_spikes": [len(s) for s in spikes]},
                                  index=units["id"][()])
        el = f["general/extracellular_ephys/electrodes"]
        electrodes = {"n": len(el["id"]),
                      "groups": sorted({_text(x) for x in el["group_name"][()]}),
                      "locations": sorted({_text(x) for x in el["location"][()]}),
                      "positions_all_nan": bool(np.all(np.isnan(el["x"][()]))
                                                and np.all(np.isnan(el["y"][()]))
                                                and np.all(np.isnan(el["z"][()]))),
                      "unit_columns": sorted(k for k in units.keys() if not k.endswith("_index"))}
        meta = {"session_description": _text(f["session_description"][()]),
                "session_start_time": _text(f["session_start_time"][()]),
                "subject_id": _text(f["general/subject/subject_id"][()]),
                "species": _text(f["general/subject/species"][()])}
    return {"trials": trials, "trial_descriptions": tr_desc, "units": unit_table,
            "spikes": spikes, "obs_intervals": obs, "meta": meta, "electrodes": electrodes}


def good_trials(trials: pd.DataFrame) -> pd.DataFrame:
    """Completed trials not flagged as outliers, with prior and dataset labels."""
    t = trials[(trials.tp > 0) & ~trials.is_outlier.astype(bool)].copy()
    t["prior"] = np.where(t.is_short.astype(bool), "Short", "Long")
    names = {v: k for k, v in DATASETS.items()}
    t["dataset"] = [names[(bool(e), float(th))] for e, th in zip(t.is_eye, t.theta)]
    t["ts"] = t.ts.round().astype(int)
    return t


def select_units(data: dict, trials: pd.DataFrame) -> tuple[np.ndarray, pd.DataFrame]:
    """Indices of the units kept, and the table of rates and minimum trial counts."""
    rows = []
    for i, (s, obs) in enumerate(zip(data["spikes"], data["obs_intervals"])):
        dur = float(np.sum(obs[:, 1] - obs[:, 0]))
        # trials of each condition inside the unit's observation intervals
        inside = np.zeros(len(trials), bool)
        for a, b in obs:
            inside |= (trials.start_time.values >= a) & (trials.stop_time.values <= b)
        counts = trials[inside].groupby(["prior", "ts", "dataset"]).size()
        n_cond = len(counts)
        rows.append({"unit": data["units"].index[i], "rate": len(s) / dur,
                     "min_trials": int(counts.min()) if n_cond else 0, "conditions": n_cond})
    table = pd.DataFrame(rows)
    keep = (table.rate >= MIN_RATE) & (table.min_trials >= MIN_TRIALS) & (table.conditions == 40)
    table["kept"] = keep
    return np.flatnonzero(keep.values), table


def bin_counts(spikes: list[np.ndarray], align_s: np.ndarray, start_ms: float, stop_ms: float,
               bin_ms: float = BIN_MS) -> np.ndarray:
    """Spike counts, trials x bins x units, in bins from start_ms to stop_ms after each event."""
    edges = np.arange(start_ms, stop_ms + bin_ms / 2, bin_ms) / 1000.0
    grid = align_s[:, None] + edges[None, :]
    out = np.empty((len(align_s), len(edges) - 1, len(spikes)))
    for j, s in enumerate(spikes):
        idx = np.searchsorted(s, grid.ravel()).reshape(grid.shape)
        out[:, :, j] = np.diff(idx, axis=1)
    return out


def smooth(rates: np.ndarray, sd_ms: float = SMOOTH_SD_MS, bin_ms: float = BIN_MS) -> np.ndarray:
    """Gaussian smoothing along the time axis (axis 0)."""
    return gaussian_filter1d(rates, sd_ms / bin_ms, axis=0, mode="nearest")


def estimation_rates(spikes, t: pd.DataFrame, ts_max: int, smoothed: bool = True):
    """Trial-averaged rates (spikes/s) from Ready to ts_max with attrition, and trials per bin."""
    c = bin_counts(spikes, t.ready_time.values, 0, ts_max)
    ends = np.arange(1, c.shape[1] + 1) * BIN_MS
    incl = t.ts.values[:, None] >= ends[None, :]          # Set at or after the end of the bin
    n = incl.sum(0)
    rates = (c * incl[:, :, None]).sum(0) / np.maximum(n, 1)[:, None] * (1000 / BIN_MS)
    return (smooth(rates) if smoothed else rates), n


def production_rates(spikes, t: pd.DataFrame, length_ms: float | None = None, smoothed=True):
    """Trial-averaged rates from Set; by default up to the shortest Set-to-Go time of the trials."""
    if length_ms is None:
        length_ms = np.min((t.go_time - t.set_time).values) * 1000
    nb = int(length_ms // BIN_MS)
    c = bin_counts(spikes, t.set_time.values, 0, nb * BIN_MS)
    rates = c.mean(0) * (1000 / BIN_MS)
    return smooth(rates) if smoothed else rates


def go_rates(spikes, t: pd.DataFrame, before_ms: float = 800, smoothed=True):
    """Trial-averaged rates from Go - before_ms to Go."""
    c = bin_counts(spikes, t.go_time.values, -before_ms, 0)
    rates = c.mean(0) * (1000 / BIN_MS)
    return smooth(rates) if smoothed else rates


def n_components(pca: PCA, threshold: float = VAR_THRESHOLD) -> int:
    """Fewest components whose cumulative explained variance reaches the threshold."""
    return int(np.searchsorted(np.cumsum(pca.explained_variance_ratio_), threshold - 1e-12) + 1)


def fit_pca(blocks: list[np.ndarray], threshold: float = VAR_THRESHOLD):
    """PCA on the concatenated [time x units] blocks; returns the fit and the number kept."""
    pca = PCA().fit(np.vstack(blocks))
    return pca, n_components(pca, threshold)


def encoding_axis(X: np.ndarray, ts_min: int, ts_max: int) -> np.ndarray:
    """Unit vector u: mean of X(ts_max - d) - X(ts_min + d), d = 0, 20, ... while the first is
    earlier than the second. X is indexed by bin, the state at time t being row t/20 - 1."""
    diffs, d = [], 0
    while ts_min + d < ts_max - d:
        diffs.append(X[(ts_max - d) // BIN_MS - 1] - X[(ts_min + d) // BIN_MS - 1])
        d += BIN_MS
    v = np.mean(diffs, axis=0)
    return v / np.linalg.norm(v)


def wls(y, x, w):
    """Weighted least squares y = a + b x; returns (a, b), weighted R2, fitted values."""
    y, x, w = map(np.asarray, (y, x, w))
    A = np.column_stack([np.ones_like(x), x]) * np.sqrt(w)[:, None]
    coef, *_ = np.linalg.lstsq(A, y * np.sqrt(w), rcond=None)
    fit = coef[0] + coef[1] * x
    ybar = np.sum(w * y) / np.sum(w)
    r2 = 1 - np.sum(w * (y - fit) ** 2) / np.sum(w * (y - ybar) ** 2)
    return coef, r2, fit


# ----------------------------------------------------------------------------------------------
# Bayesian observer (BLS) model

def _tm_grid(lo, hi):
    return np.linspace(0.2 * lo, 2.2 * hi, TM_GRID_N)


def bls_estimate(tm: np.ndarray, lo: float, hi: float, wm: float) -> np.ndarray:
    """Posterior mean of ts given tm, uniform prior on [lo, hi], noise SD wm*ts."""
    s = np.linspace(lo, hi, TS_GRID_N)
    loglik = -0.5 * ((tm[:, None] - s[None, :]) / (wm * s[None, :])) ** 2 - np.log(s[None, :])
    lik = np.exp(loglik - loglik.max(1, keepdims=True))
    return (lik * s).sum(1) / lik.sum(1)


def _tm_weights(ts, lo, hi, wm):
    tm = _tm_grid(lo, hi)
    w = np.exp(-0.5 * ((tm[None, :] - ts[:, None]) / (wm * ts[:, None])) ** 2)
    return tm, w / w.sum(1, keepdims=True)


def bls_negloglik(params, data: dict[str, tuple[np.ndarray, np.ndarray]]):
    wm, wp, b_short, b_long = params
    if wm <= 0.01 or wp <= 0.01 or wm > 1 or wp > 1:
        return np.inf
    nll = 0.0
    for prior, (ts, tp) in data.items():
        lo, hi = min(PRIOR_TS[prior]), max(PRIOR_TS[prior])
        b = b_short if prior == "Short" else b_long
        tm, w = _tm_weights(ts.astype(float), lo, hi, wm)
        te = bls_estimate(tm, lo, hi, wm)
        sd = wp * te
        dens = np.exp(-0.5 * ((tp[:, None] - te[None, :] - b) / sd[None, :]) ** 2) / (
            np.sqrt(2 * np.pi) * sd[None, :])
        p = (w * dens).sum(1)
        nll -= np.sum(np.log(np.maximum(p, 1e-300)))
    return nll


def fit_bls(t: pd.DataFrame) -> dict:
    """Maximum-likelihood fit of wm, wp, bShort, bLong to the trials of one dataset."""
    data = {p: (g.ts.values.astype(float), g.tp.values.astype(float))
            for p, g in t.groupby("prior")}
    best = None
    for x0 in ([0.1, 0.1, 0, 0], [0.15, 0.08, 20, -20], [0.07, 0.12, -20, 20]):
        r = optimize.minimize(bls_negloglik, x0, args=(data,), method="Nelder-Mead",
                              options={"xatol": 1e-5, "fatol": 1e-4, "maxiter": 4000})
        if best is None or r.fun < best.fun:
            best = r
    if not best.success:
        raise RuntimeError(f"BLS fit failed: {best.message}")
    wm, wp, bs, bl = best.x
    return {"wm": wm, "wp": wp, "b_Short": bs, "b_Long": bl, "nll": best.fun}


def bls_predict(fit: dict, prior: str, ts) -> pd.DataFrame:
    """Model mean te (no offset), mean tp and SD of tp at each ts."""
    lo, hi = min(PRIOR_TS[prior]), max(PRIOR_TS[prior])
    ts = np.atleast_1d(np.asarray(ts, float))
    tm, w = _tm_weights(ts, lo, hi, fit["wm"])
    te = bls_estimate(tm, lo, hi, fit["wm"])
    b = fit[f"b_{prior}"]
    mean_te = (w * te).sum(1)
    mean_tp = mean_te + b
    second = (w * ((te + b) ** 2 + (fit["wp"] * te) ** 2)).sum(1)
    return pd.DataFrame({"ts": ts, "te": mean_te, "tp_mean": mean_tp,
                         "tp_sd": np.sqrt(second - mean_tp ** 2)})
