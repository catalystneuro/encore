"""Data access and analysis helpers for dandiset 000147 (Guan, Aflalo et al. 2022).

The dandiset holds the main task of the paper ("finger flexion grid") for its
ten sessions of participant NS (subject P1 in the files): sorted units, and a
trials table with the cued finger, the finger the online decoder chose, the
cue's grid position and the run. The calibration task and the no-movement
control task are not included.

`load_session` streams one file from the DANDI Archive and reduces it as it
loads to spike counts per trial and unit: in the paper's analysis window, and
in short bins around the cue for the alignment check.

Where parameters come from:

- WINDOW, 0.5 to 1.5 s after the cue (the trial start time): the paper's
  methods, the window of the online decoder and of the offline analyses.
- Cross-validated Mahalanobis (crossnobis) distance with five stratified,
  unshuffled folds and a shrinkage (OAS) noise covariance from the residuals
  of each fold: the paper's methods, and the authors' code (calc_rdm.py in
  github.com/AndersenLab-Caltech/fingers_rsa at the commit archived with the
  paper). The paper names Ledoit-Wolf shrinkage; the code uses OAS.
- Diagonal LDA for classification: the paper's methods.
- WUC similarity: rsatoolbox's "cosine_cov" method, which the authors' code
  uses.
- MIN_RATE_TUNING, 0.1 Hz: the paper's methods for the tuning analysis.
- The layout of the cue grid (grid_coordinates): three rows and four columns
  from the paper's Figure 1a legend; the order of the index on it is not in the
  files or the paper, so two orders are offered.
- BIN, 50 ms bins from -1 to 3 s, and the 200 ms decoding window of the
  alignment check: a common choice, not from the paper.

The fMRI model RDMs (able-bodied PC-IP, able-bodied MC) are not in the
dandiset. They are read from the authors' code repository at the commit the
paper archived (MODEL_COMMIT).
"""

from __future__ import annotations

import io
import urllib.parse
import urllib.request
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.covariance import OAS
from sklearn.model_selection import GroupKFold, StratifiedKFold

DANDISET = "000147"
VERSION = "0.221122.2256"

FINGERS = ["T", "I", "M", "R", "P"]          # the paper's condition order; X is No-Go
CONDITIONS = FINGERS + ["X"]
PAIRS = [(a, b) for i, a in enumerate(FINGERS) for b in FINGERS[i + 1:]]   # rsatoolbox's vector order
PAIR_NAMES = [a + b for a, b in PAIRS]

WINDOW = (0.5, 1.5)                 # s after the cue
BIN = 0.05                          # s, for the alignment check
BIN_EDGES = np.round(np.arange(-1.0, 3.0 + BIN / 2, BIN), 3)
MIN_RATE_TUNING = 0.1               # Hz
N_FOLDS_RDM = 5

MODEL_COMMIT = "6915bf863ad1339e6fc8c6886032cd0f70fd8b10"
MODEL_URL = ("https://raw.githubusercontent.com/AndersenLab-Caltech/fingers_rsa/"
             f"{MODEL_COMMIT}/models/{{}}.hdf5")


@dataclass
class Session:
    name: str                 # e.g. "2018-09-17a"
    trials: pd.DataFrame      # one row per trial: run, trial_number, screen, finger, finger_pred, cue_location, ...
    counts: np.ndarray        # spikes in WINDOW, shape (trials, units)
    binned: np.ndarray        # spikes in BIN_EDGES bins around the cue, shape (trials, units, bins)
    info: dict                # values read from the file, for the data check


# --- loading ------------------------------------------------------------------

def asset_urls(version: str = VERSION) -> dict[str, str]:
    """Session name -> S3 URL of its NWB file, for the pinned version."""
    from dandi.dandiapi import DandiAPIClient

    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET, version)
        urls = {}
        for asset in dandiset.get_assets():
            session = asset.path.split("_ses-")[1].split("_")[0]
            urls[session] = asset.get_content_url(follow_redirects=1, strip_query=True)
    return dict(sorted(urls.items()))


def _text(values) -> list[str]:
    return [v.decode() if isinstance(v, bytes) else str(v) for v in values]


def load_session(name: str, url: str) -> Session:
    """Stream one session and reduce it to spike counts per trial and unit."""
    import h5py
    import remfile

    with h5py.File(remfile.File(url), "r") as f:
        tr = f["intervals/trials"]
        trials = pd.DataFrame({
            "run": tr["Run"][:].astype(int),
            "trial_number": tr["TrialNumber"][:].astype(int),
            "start_time": tr["start_time"][:],
            "stop_time": tr["stop_time"][:],
            "finger": _text(tr["finger"][:]),
            "finger_pred": _text(tr["finger_pred"][:]),
            "cue_location": tr["cue_location"][:].astype(int),
        })
        units = f["units"]
        index = units["spike_times_index"][:]
        spikes = units["spike_times"][:]
        obs = units["obs_intervals"][:]
        obs_index = units["obs_intervals_index"][:]
        unit_electrodes = units["electrodes"][:]
        epochs = pd.DataFrame({"start_time": f["intervals/epochs/start_time"][:],
                               "stop_time": f["intervals/epochs/stop_time"][:],
                               "run": f["intervals/epochs/Run"][:].astype(int)})
        info = {
            "trial_column_descriptions": {k: tr[k].attrs.get("description", "") for k in _text(tr.attrs["colnames"])},
            "units_columns": _text(units.attrs["colnames"]),
            "session_description": f["session_description"][()].decode(),
            "session_id": f["general/session_id"][()].decode(),
            "subject_id": f["general/subject/subject_id"][()].decode(),
        }

    # The paper's methods: each screen shows the 12 grid positions, and each is cued once
    # (12 trials) before the next screen. Screen and position within it are counted per run.
    trials["screen"] = (trials.trial_number - 1) // 12
    trials["position_in_screen"] = (trials.trial_number - 1) % 12
    starts = trials.start_time.to_numpy()
    n_units = len(index)
    counts = np.zeros((len(trials), n_units), dtype=np.int32)
    binned = np.zeros((len(trials), n_units, len(BIN_EDGES) - 1), dtype=np.int16)
    window_edges = starts[:, None] + np.array(WINDOW)[None, :]
    bin_edges = starts[:, None] + BIN_EDGES[None, :]
    spike_ranges, unsorted, backward_jumps, touched = [], 0, 0, np.zeros(len(trials), dtype=bool)
    analysis_lo, analysis_hi = starts + BIN_EDGES[0], starts + BIN_EDGES[-1]
    lo = 0
    for u, hi in enumerate(index):
        s = spikes[lo:hi]
        jumps = np.flatnonzero(np.diff(s) < 0)
        if len(jumps):
            # Spike times are not in ascending order. Each backward jump leaves a span of
            # time [s[i+1], s[i]] covered twice; note any trial whose analysed range meets one.
            unsorted += 1
            backward_jumps += len(jumps)
            for i in jumps:
                touched |= (analysis_hi >= s[i + 1]) & (analysis_lo <= s[i])
            s = np.sort(s)
        counts[:, u] = np.diff(np.searchsorted(s, window_edges), axis=1)[:, 0]
        binned[:, u, :] = np.diff(np.searchsorted(s, bin_edges), axis=1)
        if len(s):
            spike_ranges.append((s[0], s[-1]))
        lo = hi

    # Observation intervals: the same for every unit? Do all trial windows fall inside them?
    obs_sets = np.split(obs, obs_index[:-1])
    same_obs = all(np.array_equal(o, obs_sets[0]) for o in obs_sets)
    first = obs_sets[0]
    inside = np.zeros(len(trials), dtype=bool)
    for a, b in first:
        inside |= (starts + BIN_EDGES[0] >= a) & (starts + BIN_EDGES[-1] <= b)
    run_bounds = trials.groupby("run").agg(first=("start_time", "min"), last=("stop_time", "max"))
    run_in_epoch = [
        bool(((epochs.run == r) & (epochs.start_time <= row["first"] + 1e-6)
              & (epochs.stop_time >= row["last"] - 1e-6)).any())
        for r, row in run_bounds.iterrows()]
    window_rate = counts.sum(axis=0) / (len(trials) * (WINDOW[1] - WINDOW[0]))
    recorded = float((first[:, 1] - first[:, 0]).sum())
    info.update({
        "n_units": n_units,
        "n_spikes": int(len(spikes)),
        "units_with_unsorted_spike_times": unsorted,
        "backward_jumps_in_spike_times": backward_jumps,
        "trials_whose_range_meets_an_unsorted_span": int(touched.sum()),
        "units_without_spikes": int(n_units - len(spike_ranges)),
        "spike_time_range_s": (round(float(min(r[0] for r in spike_ranges)), 2),
                               round(float(max(r[1] for r in spike_ranges)), 2)),
        "trial_time_range_s": (round(float(starts.min()), 2), round(float(trials.stop_time.max()), 2)),
        "trial_durations_s": sorted(set(np.round(trials.stop_time - trials.start_time, 3))),
        "n_electrodes_with_units": int(len(np.unique(unit_electrodes))),
        "obs_intervals_same_for_all_units": same_obs,
        "n_obs_intervals": int(len(first)),
        "trials_inside_obs_intervals": int(inside.sum()),
        "runs_inside_epochs": f"{sum(run_in_epoch)} of {len(run_in_epoch)}",
        "window_rate_hz_median": round(float(np.median(window_rate)), 2),
        "window_rate_hz_range": (round(float(window_rate.min()), 3), round(float(window_rate.max()), 1)),
        "session_rate_hz": np.diff(index, prepend=0) / recorded,   # all spikes over the observation intervals
    })
    return Session(name=name, trials=trials, counts=counts, binned=binned, info=info)


def load_all(version: str = VERSION) -> list[Session]:
    from concurrent.futures import ThreadPoolExecutor

    urls = asset_urls(version)
    with ThreadPoolExecutor(max_workers=5) as pool:
        return list(pool.map(lambda kv: load_session(*kv), urls.items()))


def load_model_rdm(name: str) -> tuple[np.ndarray, list[str]]:
    """A model RDM from the authors' repository, as a vector in PAIRS order, and the
    condition order stored in the file (which must be FINGERS)."""
    import h5py

    url = MODEL_URL.format(urllib.parse.quote(name))
    with urllib.request.urlopen(url, timeout=60) as response:
        data = response.read()
    with h5py.File(io.BytesIO(data), "r") as f:
        vector = f["dissimilarities"][0]
        key = next(k for k in ["condition", "finger"] if f"pattern_descriptors/{k}" in f)
        order = _text(f[f"pattern_descriptors/{key}"][:])
    assert order == FINGERS, f"model {name} has conditions {order}"
    return np.asarray(vector, dtype=float), order


def grid_coordinates(cue_location: np.ndarray, layout: str) -> np.ndarray:
    """Column and row (x, y) of a cue location index 1 to 12 on the grid of three rows and
    four columns (the paper's Figure 1a legend). The files do not say how the index maps
    onto the grid, so the layout is an assumption: "row-major" numbers along the rows,
    "column-major" down the columns. A flip of either axis does not change a linear fit."""
    i = np.asarray(cue_location) - 1
    if layout == "row-major":
        return np.column_stack([i % 4, i // 4]).astype(float)
    if layout == "column-major":
        return np.column_stack([i // 3, i % 3]).astype(float)
    raise ValueError(layout)


# --- classification -------------------------------------------------------------

def diag_lda_fit(X: np.ndarray, y: np.ndarray, classes):
    means = np.stack([X[y == c].mean(axis=0) for c in classes])
    resid = X - means[np.searchsorted(classes, y)]
    var = (resid ** 2).sum(axis=0) / max(len(y) - len(classes), 1)
    return means, var


def diag_lda_predict(X: np.ndarray, means: np.ndarray, var: np.ndarray, classes):
    keep = var > 0
    if not keep.any():
        return np.full(len(X), classes[0])
    d = ((X[:, None, keep] - means[None, :, keep]) ** 2 / var[keep]).sum(axis=2)
    return np.asarray(classes)[np.argmin(d, axis=1)]


def diag_lda_cv(X: np.ndarray, y: np.ndarray, folds: int | None = None, rng=None,
                groups: np.ndarray | None = None) -> np.ndarray:
    """Cross-validated diagonal LDA predictions. folds=None is leave-one-out.

    With `groups`, the folds are GroupKFold folds, so that no group (for example a
    screen of the grid task) is split between training and test sets.
    Equal class priors; the classes here are balanced. Features with zero
    within-class variance in the training set are ignored.
    """
    classes = np.unique(y)
    pred = np.empty(len(y), dtype=y.dtype)
    if groups is not None:
        splits = GroupKFold(folds).split(X, y, groups)
    elif folds is None:
        splits = [(np.delete(np.arange(len(y)), i), np.array([i])) for i in range(len(y))]
    else:
        seed = None if rng is None else int(rng.integers(2**31))
        splits = StratifiedKFold(folds, shuffle=rng is not None, random_state=seed).split(X, y)
    for train, test in splits:
        means, var = diag_lda_fit(X[train], y[train], classes)
        pred[test] = diag_lda_predict(X[test], means, var, classes)
    return pred


def weighted_sd(values, weights) -> float:
    """SD across sessions weighted by trials, as statsmodels DescrStatsW(ddof=1), which the authors' code uses."""
    values, weights = np.asarray(values, float), np.asarray(weights, float)
    mean = np.average(values, weights=weights)
    return float(np.sqrt((weights * (values - mean) ** 2).sum() / (weights.sum() - 1)))


# --- representational dissimilarity -----------------------------------------------

def fold_ids(y: np.ndarray, n_folds: int = N_FOLDS_RDM) -> np.ndarray:
    """Stratified, unshuffled folds, so each fold is a block of time (as the authors' code)."""
    ids = -np.ones(len(y), dtype=int)
    for k, (_, test) in enumerate(StratifiedKFold(n_folds, shuffle=False).split(np.zeros(len(y)), y)):
        ids[test] = k
    return ids


def crossnobis_rdm(X: np.ndarray, y: np.ndarray, conditions=FINGERS, n_folds: int = N_FOLDS_RDM,
                   noise_cov: np.ndarray | None = None) -> np.ndarray:
    """Cross-validated squared Mahalanobis distance between conditions, per neuron.

    For each pair of folds (A, B), d_jk = (b_j - b_k)_A ((S_A + S_B)/2)^-1 (b_j - b_k)_B' / N,
    averaged over all pairs of folds, as in the paper's methods. S is the OAS
    shrinkage covariance of the fold's residuals from its condition means, or
    `noise_cov` for every fold when it is given.
    """
    mask = np.isin(y, conditions)
    X, y = X[mask].astype(float), y[mask]
    folds = fold_ids(y, n_folds)
    means, covs = [], []
    for k in range(n_folds):
        Xk, yk = X[folds == k], y[folds == k]
        m = np.stack([Xk[yk == c].mean(axis=0) for c in conditions])
        resid = Xk - m[[conditions.index(c) for c in yk]]
        covs.append(OAS(assume_centered=True).fit(resid).covariance_)
        means.append(m)
    j = np.array([conditions.index(a) for a, _ in PAIRS])
    k_ = np.array([conditions.index(b) for _, b in PAIRS])
    total, n = np.zeros(len(PAIRS)), 0
    for a in range(n_folds):
        for b in range(a + 1, n_folds):
            precision = np.linalg.pinv(noise_cov if noise_cov is not None else (covs[a] + covs[b]) / 2)
            da = means[a][j] - means[a][k_]
            db = means[b][j] - means[b][k_]
            total += np.einsum("pi,ij,pj->p", da, precision, db)
            n += 1
    return total / n / X.shape[1]


def square(vector: np.ndarray) -> pd.DataFrame:
    m = np.zeros((len(FINGERS), len(FINGERS)))
    iu = np.triu_indices(len(FINGERS), 1)
    m[iu] = vector
    m = m + m.T
    return pd.DataFrame(m, index=FINGERS, columns=FINGERS)


def wuc(model: np.ndarray, data: np.ndarray) -> np.ndarray:
    """Whitened unbiased cosine similarity of a model with each data RDM (rows), via rsatoolbox."""
    import rsatoolbox

    m = rsatoolbox.rdm.RDMs(np.atleast_2d(model), dissimilarity_measure="crossnobis")
    d = rsatoolbox.rdm.RDMs(np.atleast_2d(data), dissimilarity_measure="crossnobis")
    return rsatoolbox.rdm.compare(m, d, method="cosine_cov")[0]


def run_rdms(session: Session, session_noise: bool = False) -> pd.DataFrame:
    """One crossnobis RDM per run of a session, in long form (run, pair, distance).

    A run has eight trials of each finger, so each of the five folds holds one or two
    trials per finger, and the noise covariance of a fold is estimated from few
    residuals. With session_noise=True, the noise covariance is instead estimated once
    from all trials of the session, after removing each run's condition means.
    """
    rows = []
    y = session.trials.finger.to_numpy()
    runs = session.trials.run.to_numpy()
    noise = None
    if session_noise:
        keep = np.isin(y, FINGERS)
        resid = session.counts.astype(float).copy()
        for r in np.unique(runs):
            for c in FINGERS:
                m = (runs == r) & (y == c)
                resid[m] -= resid[m].mean(axis=0)
        noise = OAS(assume_centered=True).fit(resid[keep]).covariance_
    for run in sorted(np.unique(runs)):
        m = runs == run
        for pair, d in zip(PAIR_NAMES, crossnobis_rdm(session.counts[m], y[m], noise_cov=noise)):
            rows.append({"run": int(run), "pair": pair, "distance": d})
    return pd.DataFrame(rows)


# --- other measures ----------------------------------------------------------------

def authors_classifier():
    """The classifier in the authors' crossval_classify config: units with a mean count
    of at least 0.5 in the window, z-scored, then LDA with identity covariance (shrinkage 1)."""
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.feature_selection import SelectFromModel
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    return make_pipeline(
        SelectFromModel(StandardScaler(), importance_getter="mean_", threshold=0.5),
        StandardScaler(),
        LinearDiscriminantAnalysis(solver="lsqr", shrinkage=1),
    )


def decoding_curve(session: Session, centers: np.ndarray, width: float = 0.2, folds: int = 8) -> np.ndarray:
    """Cross-validated 6-class diagonal LDA accuracy for the cued finger, from spike counts in
    windows of `width` s centred on `centers` (s from the trial start)."""
    y = session.trials.finger.to_numpy()
    accuracy = []
    for c in centers:
        a = np.searchsorted(BIN_EDGES, c - width / 2 + 1e-9)
        b = np.searchsorted(BIN_EDGES, c + width / 2 - 1e-9)
        X = session.binned[:, :, a:b].sum(axis=2).astype(float)
        accuracy.append((diag_lda_cv(X, y, folds) == y).mean())
    return np.array(accuracy)


def tuning_pvalues(session: Session, min_rate: float = MIN_RATE_TUNING) -> tuple[np.ndarray, np.ndarray]:
    """Two-tailed t-test of each finger's rate in WINDOW against No-Go, per unit.

    Returns the p-values (units kept, 5 fingers) and the indices of the units kept
    (mean rate in the window at least `min_rate`).
    """
    from scipy import stats

    y = session.trials.finger.to_numpy()
    rates = session.counts / (WINDOW[1] - WINDOW[0])
    keep = np.flatnonzero(rates.mean(axis=0) >= min_rate)
    p = np.array([[stats.ttest_ind(rates[y == f, u], rates[y == "X", u]).pvalue for f in FINGERS]
                  for u in keep])
    return p, keep


def shuffle_within(labels: np.ndarray, groups: np.ndarray, rng) -> np.ndarray:
    """Permute labels among trials of the same group."""
    out = labels.copy()
    for g in np.unique(groups):
        m = groups == g
        out[m] = rng.permutation(out[m])
    return out
