"""Data access and analysis helpers for dandiset 000127 (Chowdhury, Glaser & Miller 2020).

The dandiset holds one session of the paper's active/passive experiment
(monkey H, "Han", 2017-12-07), packaged for the Neural Latents Benchmark.
`load_session` streams it from the DANDI Archive and returns one row per
trial: the trial type, the average kinematics and the spike count of every
neuron in the 120 ms after movement onset, which is the paper's analysis
window.

The model fitting follows the paper's methods: Poisson generalised linear
models, repeated 5-fold cross-validation, a deviance-based pseudo-R2 and the
corrected resampled t-test.
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import PoissonRegressor
from sklearn.preprocessing import StandardScaler

DANDISET = "000127"
VERSION = "0.220113.0359"
ASSET = "sub-Han/sub-Han_desc-train_behavior+ecephys.nwb"

WINDOW = 0.120      # s after movement onset, as in the paper
FOLDS, REPEATS = 5, 20
SPEED_TIMES = np.arange(-0.1, 0.3, 0.001)   # s around movement onset, for plotting
MIN_RATE = 1.0      # Hz; neurons firing less than this in the window are not modelled
RIDGE = 0.01        # small penalty on the model weights, see fit_predict

# Counts kept while fitting, so a notebook can report them.
FIT_LOG = {"fits": 0, "not_converged": 0, "no_training_spikes": 0}

JOINTS = ["shoulder_adduction", "shoulder_rotation", "shoulder_flexion", "elbow_flexion",
          "radial_pronation", "wrist_flexion", "wrist_abduction"]
HAND = ["hand_pos_x", "hand_pos_y", "hand_vel_x", "hand_vel_y"]
JOINT_KINEMATICS = [f"{j}_angle" for j in JOINTS] + [f"{j}_velocity" for j in JOINTS]


@dataclass
class Session:
    trials: pd.DataFrame     # one row per analysed trial: type, direction, kinematics
    counts: np.ndarray       # spikes in the window, shape (trials, neurons)
    speed: np.ndarray        # hand speed around onset, m/s, shape (trials, len(SPEED_TIMES))
    sanity: dict             # ranges and counts read from the file, for checking


# --- loading ------------------------------------------------------------------

def load_session(version: str = VERSION) -> Session:
    """Stream the session and reduce it to the analysis window of each trial."""
    import h5py
    import remfile
    from dandi.dandiapi import DandiAPIClient
    from pynwb import NWBHDF5IO

    with DandiAPIClient() as client:
        asset = client.get_dandiset(DANDISET, version).get_asset_by_path(ASSET)
        url = asset.get_content_url(follow_redirects=1, strip_query=True)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        io = NWBHDF5IO(file=h5py.File(remfile.File(url), "r"), mode="r", load_namespaces=True)
        nwb = io.read()
        behavior = nwb.processing["behavior"]
        series = {name: behavior[name] for name in ("hand_pos", "hand_vel", "joint_ang", "joint_vel")}
        rate = series["hand_pos"].rate
        start = series["hand_pos"].starting_time
        # Stored values times `conversion` are in the series' stated unit.
        data = {name: s.data[:] * s.conversion for name, s in series.items()}
        all_trials = nwb.intervals["trials"].to_dataframe()
        units = nwb.units.to_dataframe()
        joint_columns = str(series["joint_ang"].comments)

    # Successful trials only. A trial with a bump during the centre hold is
    # passive, and its movement onset is the onset of the bump; a trial without
    # one is active, and its onset is the start of the reach.
    ok = all_trials[(all_trials.result == "R") & all_trials.move_onset_time.notna()].copy()
    ok["passive"] = ok.ctr_hold_bump.astype(bool)
    ok["direction"] = np.where(ok.passive, ok.bump_dir, ok.target_dir)

    rows, keep, traces = [], [], []
    width = int(round(WINDOW * rate))
    before = int(round(-SPEED_TIMES[0] * rate))
    for trial in ok.itertuples():
        first = int(round((trial.move_onset_time - start) * rate))
        window = slice(first, first + width)
        values = np.concatenate([data[name][window].mean(axis=0)
                                 for name in ("hand_pos", "hand_vel", "joint_ang", "joint_vel")])
        around = slice(first - before, first - before + len(SPEED_TIMES))
        if around.start < 0 or around.stop > len(data["hand_pos"]) or np.isnan(values).any():
            continue
        speed = np.hypot(*data["hand_vel"][window].T)
        traces.append(np.hypot(*data["hand_vel"][around].T))
        rows.append(dict(zip(HAND + JOINT_KINEMATICS, values), passive=trial.passive,
                         direction=float(trial.direction), onset=trial.move_onset_time,
                         mean_speed=float(speed.mean())))
        keep.append(trial.move_onset_time)
    trials = pd.DataFrame(rows)

    onsets = np.array(keep)
    counts = np.column_stack([
        np.searchsorted(np.asarray(spikes), onsets + WINDOW) - np.searchsorted(np.asarray(spikes), onsets)
        for spikes in units.spike_times
    ])

    sanity = {
        "sampling rate (Hz)": rate,
        "recording length (s)": round(len(data["hand_pos"]) / rate, 1),
        "trials in file": len(all_trials),
        "successful trials with a movement onset": len(ok),
        "trials analysed": len(trials),
        "neurons": counts.shape[1],
        "hand position range (m)": [round(float(v), 3) for v in
                                    (np.nanmin(data["hand_pos"]), np.nanmax(data["hand_pos"]))],
        "hand speed, 99th percentile (m/s)": round(float(np.nanpercentile(
            np.hypot(*data["hand_vel"].T), 99)), 3),
        "joint angle range (deg)": [round(float(v)) for v in
                                    (np.nanmin(data["joint_ang"]), np.nanmax(data["joint_ang"]))],
        "joint columns in file": joint_columns,
        "movement directions (deg)": sorted(trials.direction.unique().tolist()),
        "onset minus bump time (s): min, median, max": [round(float(v), 3) for v in (
            (ok[ok.passive].move_onset_time - ok[ok.passive].bump_time)
            .agg(["min", "median", "max"]))],
        "trials by result and bump": {f"{r}/{'bump' if b else 'no bump'}": int(n) for (r, b), n in
                                      all_trials.groupby(["result", "ctr_hold_bump"]).size().items()},
        "series share a timebase": len({(s.rate, s.starting_time, len(s.data))
                                        for s in series.values()}) == 1,
    }
    return Session(trials=trials, counts=counts, speed=np.array(traces), sanity=sanity)


# --- cross-validation ---------------------------------------------------------

def folds(n: int, rng: np.random.Generator):
    """Train and test indices for repeated k-fold cross-validation."""
    for _ in range(REPEATS):
        order = rng.permutation(n)
        for k in range(FOLDS):
            test = np.sort(order[k::FOLDS])
            yield np.setdiff1d(order, test), test


def corrected_t_test(differences: np.ndarray) -> float:
    """Two-sided p-value of the corrected resampled t-test (Nadeau & Bengio 2003).

    `differences` holds one value per cross-validation fold. Test folds
    overlap between repeats, so the plain standard error is too small; the
    correction adds 1/(K-1) to 1/n under the square root.
    """
    d = np.asarray(differences, dtype=float)
    d = d[np.isfinite(d)]
    n = len(d)
    variance = d.var(ddof=1)
    if n < 2 or variance == 0:
        return np.nan
    t = d.mean() / np.sqrt((1 / n + 1 / (FOLDS - 1)) * variance)
    return float(2 * stats.t.sf(abs(t), n - 1))


# --- models -------------------------------------------------------------------

def fit_predict(x_train, y_train, x_test) -> np.ndarray:
    """Fit a Poisson GLM for each neuron and predict the test trials' counts.

    The paper fits by maximum likelihood. With 120 ms windows many counts are
    zero, and for some neurons and folds the unpenalised fit diverges and
    predicts absurd rates on held-out trials. A small ridge penalty (RIDGE)
    on standardised covariates prevents that; it is a deviation from the
    paper's method.
    """
    scaler = StandardScaler().fit(x_train)
    a, b = scaler.transform(x_train), scaler.transform(x_test)
    predicted = np.empty((len(x_test), y_train.shape[1]))
    for i in range(y_train.shape[1]):
        FIT_LOG["fits"] += 1
        if y_train[:, i].sum() == 0:
            # Nothing to fit: predict silence. Held-out spikes then score badly.
            FIT_LOG["no_training_spikes"] += 1
            predicted[:, i] = 0.0
            continue
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always", ConvergenceWarning)
            model = PoissonRegressor(alpha=RIDGE, max_iter=300).fit(a, y_train[:, i])
        FIT_LOG["not_converged"] += any(issubclass(w.category, ConvergenceWarning) for w in caught)
        predicted[:, i] = model.predict(b)
    return predicted


def pseudo_r2(observed: np.ndarray, predicted: np.ndarray) -> np.ndarray:
    """Deviance-based pseudo-R2 for each neuron (the paper's equation 4c).

    1 is a perfect fit, 0 is no better than predicting the mean count of the
    evaluated trials, and negative is worse than that.
    """
    def deviance(f, fhat):
        fhat = np.maximum(fhat, 1e-9)
        with np.errstate(divide="ignore", invalid="ignore"):
            log_term = np.where(f > 0, f * np.log(f / fhat), 0.0)
        return 2 * np.sum(log_term - (f - fhat), axis=0)

    null = deviance(observed, np.broadcast_to(observed.mean(axis=0), observed.shape))
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(null > 0, 1 - deviance(observed, predicted) / null, np.nan)


def separability(features: np.ndarray, passive: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Cross-validated accuracy of a linear discriminant telling passive from active.

    Returns one value per cross-validation fold.
    """
    features = np.asarray(features, dtype=float).reshape(len(passive), -1)
    scores = []
    for train, test in folds(len(passive), rng):
        if features[train].std(axis=0).min() == 0:
            scores.append(max(passive[test].mean(), 1 - passive[test].mean()))
            continue
        model = LinearDiscriminantAnalysis().fit(features[train], passive[train])
        scores.append(model.score(features[test], passive[test]))
    return np.array(scores)


def cross_validate(models: dict[str, np.ndarray], counts: np.ndarray, passive: np.ndarray,
                   within: str, rng: np.random.Generator) -> dict:
    """Fit every model on the same folds and score the held-out predictions.

    `models` maps a model name to its covariates, one row per trial. All
    models are trained on both trial types. The model named `within` is also
    trained on each trial type separately.

    Returns pseudo-R2 arrays with one column per neuron:

    - "fold": {model: (folds, neurons)}, scored on each test fold, for
      comparing models with the corrected t-test.
    - "both": {(model, type): (repeats, neurons)}, the model trained on both
      trial types, scored on the held-out trials of one type.
    - "within": {type: (repeats, neurons)}, the `within` model trained and
      scored on one trial type.

    The per-type scores pool the held-out predictions of a whole repeat, so
    every trial of that type is predicted once by a model that did not see it.
    Scoring single folds of one trial type leaves about 35 trials, too few for
    a stable pseudo-R2 at these spike counts.
    """
    n = len(passive)
    types = {"active": ~passive, "passive": passive}
    fold_scores = {name: [] for name in models}
    both = {(name, t): [] for name in models for t in types}
    within_scores = {t: [] for t in types}
    all_folds = list(folds(n, rng))
    for repeat in range(REPEATS):
        pooled = {name: np.full(counts.shape, np.nan) for name in models}
        pooled_within = np.full(counts.shape, np.nan)
        for train, test in all_folds[repeat * FOLDS:(repeat + 1) * FOLDS]:
            for name, x in models.items():
                predicted = fit_predict(x[train], counts[train], x[test])
                pooled[name][test] = predicted
                fold_scores[name].append(pseudo_r2(counts[test], predicted))
            for mask in types.values():
                tr, te = train[mask[train]], test[mask[test]]
                pooled_within[te] = fit_predict(models[within][tr], counts[tr], models[within][te])
        for t, mask in types.items():
            for name in models:
                both[(name, t)].append(pseudo_r2(counts[mask], pooled[name][mask]))
            within_scores[t].append(pseudo_r2(counts[mask], pooled_within[mask]))
    return {"fold": {k: np.array(v) for k, v in fold_scores.items()},
            "both": {k: np.array(v) for k, v in both.items()},
            "within": {k: np.array(v) for k, v in within_scores.items()}}
