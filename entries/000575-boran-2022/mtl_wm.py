"""Loading and per-neuron measures for dandiset 000575 (human MTL neurons, visual working memory).

Boran, Hilfiker, Stieglitz, Sarnthein & Klaver (2022), NeuroImage 254, 119123,
doi:10.1016/j.neuroimage.2022.119123.

Each NWB file holds one session: a trial table (start and stop, set size, the correct answer), the
participant's answer per trial (`processing/behavior/BehavioralEvents.response`), the task epochs,
and a Units table of sorted units with spike times, the electrode (microwire label) of each unit,
and the mean and standard deviation of its waveform. Files are streamed from the archive at the
pinned version with remfile and h5py; nothing is written to disk. The LFP is not read.

Where the parameters come from:

- Periods, relative to trial start (the onset of the 900 ms fixation period): fixation 0 to 0.9 s,
  encoding 0.9 to 1.7 s, maintenance 1.7 to 2.6 s, test 2.6 to 4.6 s. These are the durations of
  the claims file's opening comment (Methods 2.2 and 2.3); the notebook checks them against the
  epochs table of every file.
- Region of a unit: the claims file (neurons-recorded) names two readings. `region_of` gives
  reading (b), the electrode name of the unit's microwire bundle, AH and PH hippocampus, EC
  entorhinal cortex, A amygdala (Table 1 legend). Reading (a), the anatomical location of the
  microwire tips (Figure 1d legend), is built in the notebook's data check from the atlas label of
  each bundle's tip contact. The `location` column is not used; see the notebook's data check.
- Response time: the files' response timestamps are the conversion's `Response time` plus the
  trial start plus 1.7 s (usz-neuro-conversion, convert_Human_MTL_units_visual_WM.ipynb,
  `write_behavior` and `_get_time_offset`, commit c31dad914fd3f63476750dffff30f119386f60ec).
  `RT_OFFSET_S` recovers the stored `Response time`, read here as the time from test array onset
  (an assumption, checked in the notebook; the Figure 1c legend measures RT from test onset).
- Permutation tests: `perm_ttest` is the two-sided permutation t-test of EEGLAB statcond that
  Methods 2.6 names, paired (sign flips of the per-trial differences) or unpaired (shuffling the
  pooled values between the two groups). The number of permutations (1000) is the claims file's
  standard choice.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "000575"
DANDISET_VERSION = "0.231010.1811"
API = "https://api.dandiarchive.org/api"

PERIODS = {"fixation": (0.0, 0.9), "encoding": (0.9, 1.7), "maintenance": (1.7, 2.6), "test": (2.6, 4.6)}
TRIAL_S = 4.6
RT_OFFSET_S = 1.7
REGION_OF_BUNDLE = {"AH": "Hipp", "PH": "Hipp", "EC": "Ent", "A": "Amg"}
REGIONS = ["Hipp", "Ent", "Amg"]


def list_assets(version: str = DANDISET_VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    return requests.get(url, timeout=60).json()["results"]


def _s3_url(asset_id: str) -> str:
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url


def _text(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def bundle_of(label: str) -> str:
    """'AHL3' -> 'AHL' (the microwire bundle); the trailing number is the wire."""
    return label.rstrip("0123456789")


def region_of(label: str) -> str:
    b = bundle_of(label)
    site = b[:-1] if b[-1:] in ("L", "R") else b
    return REGION_OF_BUNDLE.get(site, "other:" + b)


def load_file(asset: dict) -> dict:
    """Read one file: trials, answers, epochs and units. Spike times stay in seconds."""
    f = h5py.File(remfile.File(_s3_url(asset["asset_id"])), "r")
    tr = f["intervals/trials"]
    trials = pd.DataFrame({
        "trial_id": tr["id"][:], "start": tr["start_time"][:], "stop": tr["stop_time"][:],
        "set_size": tr["set_size"][:], "solution_same": tr["solution"][:].astype(bool)})
    resp = f["processing/behavior/BehavioralEvents.response/response"]
    trials["answer_same"] = resp["data"][:].astype(bool)
    trials["response_ts"] = resp["timestamps"][:]
    trials["correct"] = trials.answer_same == trials.solution_same
    trials["rt"] = trials.response_ts - trials.start - RT_OFFSET_S
    ep = f["intervals/epochs"]
    tags_index = ep["tags_index"][:]
    tags = [_text(t) for t in ep["tags"][:]]
    epochs = pd.DataFrame({"start": ep["start_time"][:], "stop": ep["stop_time"][:],
                           "tag": [tags[i - 1] for i in tags_index]})
    el = f["general/extracellular_ephys/electrodes"]
    labels = np.array([_text(x) for x in el["label"][:]])
    locations = np.array([_text(x) for x in el["location"][:]])
    el_ids = el["id"][:]
    u = f["units"]
    spikes = u["spike_times"][:]
    bounds = np.concatenate([[0], u["spike_times_index"][:]])
    unit_el = u["electrodes"][:]
    row = np.array([int(np.where(el_ids == e)[0][0]) for e in unit_el])
    units = pd.DataFrame({"unit_id": u["id"][:], "label": labels[row], "location": locations[row]})
    units["bundle"] = units.label.map(bundle_of)
    units["region"] = units.label.map(region_of)
    units["n_spikes"] = np.diff(bounds)
    subj = f["general/subject"]
    out = {
        "path": asset["path"], "asset_id": asset["asset_id"], "size": asset["size"],
        "identifier": _text(f["identifier"][()]),
        "subject": _text(subj["subject_id"][()]),
        "subject_description": _text(subj["description"][()]),
        "session_start": _text(f["session_start_time"][()]),
        "trials": trials, "epochs": epochs, "units": units,
        "spike_times": [spikes[bounds[i]:bounds[i + 1]] for i in range(len(units))],
        "waveform_mean": u["waveform_mean"][:], "waveform_sd": u["waveform_sd"][:],
        "waveform_unit": _text(u["waveform_mean"].attrs.get("unit", "")),
        "waveform_rate": float(u["waveform_mean"].attrs.get("sampling_rate", np.nan)),
        "n_obs_intervals": int(u["obs_intervals"].shape[0]),
        "obs_first": u["obs_intervals"][:3],
        "has_lfp": "ecephys" in f["processing"],
    }
    out["session"] = int(out["identifier"].split("session")[-1])
    f.close()
    return out


def fingerprint(s: dict) -> tuple:
    """What two copies of one recording share: trial starts, spike counts and the first spikes."""
    first = tuple(np.round(np.concatenate([t[:3] for t in s["spike_times"]]), 6))
    return (len(s["trials"]), tuple(np.round(s["trials"].start.values, 6)), tuple(s["units"].n_spikes), first)


def load_all(version: str = DANDISET_VERSION, workers: int = 8) -> tuple[list[dict], list[tuple[str, str]]]:
    """Every file of the version, and the list of files that duplicate another (kept once)."""
    assets = sorted(list_assets(version), key=lambda a: a["path"])
    with ThreadPoolExecutor(workers) as ex:
        files = list(ex.map(load_file, assets))
    kept, seen, duplicates = [], {}, []
    for s in files:
        key = fingerprint(s)
        if key in seen:
            duplicates.append((s["path"], seen[key]))
            continue
        seen[key] = s["path"]
        kept.append(s)
    for s in kept:
        s["key"] = f"P{int(s['subject']):02d}S{s['session']}"
    return files, duplicates, sorted(kept, key=lambda s: s["key"])


def period_counts(s: dict, periods: dict = PERIODS) -> dict[str, np.ndarray]:
    """Spike counts per unit, trial and period: {period: array (units, trials)}."""
    starts = s["trials"].start.values
    out = {}
    for name, (a, b) in periods.items():
        lo, hi = starts + a, starts + b
        out[name] = np.array([np.searchsorted(t, hi, "left") - np.searchsorted(t, lo, "left")
                              for t in s["spike_times"]])
    return out


def window_counts(s: dict, offsets: np.ndarray, width: float) -> np.ndarray:
    """Spike counts per unit, trial and window starting at trial start + offset: (units, trials, windows)."""
    starts = s["trials"].start.values
    lo = starts[:, None] + offsets[None, :]
    hi = lo + width
    return np.stack([np.searchsorted(t, hi, "left") - np.searchsorted(t, lo, "left") for t in s["spike_times"]])


def make_perms(n: int, n_perm: int, paired: bool, rng: np.random.Generator) -> np.ndarray:
    """Paired: sign flips (n_perm, n). Unpaired: (n_perm, n) permutations of the pooled indices."""
    if paired:
        return rng.choice([-1.0, 1.0], size=(n_perm, n))
    return np.array([rng.permutation(n) for _ in range(n_perm)])


def paired_t(d: np.ndarray, signs: np.ndarray | None = None) -> np.ndarray:
    """t of the mean of d (trials, units); with signs (perms, trials) one t per permutation and unit."""
    n = d.shape[0]
    ss = (d ** 2).sum(0)
    m = d.mean(0) if signs is None else signs @ d / n
    var = (ss - n * m ** 2) / (n - 1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return m / np.sqrt(var / n)


def welch_t(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Unpaired t of x (trials, units) against y (trials, units), unequal variances as in statcond."""
    nx, ny = x.shape[0], y.shape[0]
    with np.errstate(divide="ignore", invalid="ignore"):
        return (x.mean(0) - y.mean(0)) / np.sqrt(x.var(0, ddof=1) / nx + y.var(0, ddof=1) / ny)


def unpaired_null(x: np.ndarray, y: np.ndarray, perms: np.ndarray) -> np.ndarray:
    """t for each permutation of the pooled values: (perms, units)."""
    pooled = np.concatenate([x, y], 0)
    nx = x.shape[0]
    n = pooled.shape[0]
    onehot = np.zeros((perms.shape[0], n))
    onehot[np.arange(perms.shape[0])[:, None], perms[:, :nx]] = 1.0
    s1, q1 = onehot @ pooled, onehot @ pooled ** 2
    tot, totq = pooled.sum(0), (pooled ** 2).sum(0)
    ny = n - nx
    m1, m2 = s1 / nx, (tot - s1) / ny
    v1 = (q1 - nx * m1 ** 2) / (nx - 1)
    v2 = (totq - q1 - ny * m2 ** 2) / (ny - 1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return (m1 - m2) / np.sqrt(v1 / nx + v2 / ny)


def perm_ttest(x: np.ndarray, y: np.ndarray, paired: bool, n_perm: int, rng: np.random.Generator):
    """Two-sided permutation t-test per unit (statcond). x, y: (trials, units). Returns t, p.

    A unit with no variance in either condition gets t = 0 and p = 1."""
    if paired:
        d = x - y
        t = paired_t(d)
        null = paired_t(d, make_perms(d.shape[0], n_perm, True, rng))
    else:
        t = welch_t(x, y)
        null = unpaired_null(x, y, make_perms(x.shape[0] + y.shape[0], n_perm, False, rng))
    t = np.nan_to_num(t)
    null = np.nan_to_num(null)
    p = ((np.abs(null) >= np.abs(t) - 1e-12).sum(0) + 1) / (n_perm + 1)
    return t, p


# ---------------------------------------------------------------------------------------------
# Population decoding (Methods 2.5): pseudo-populations, cross-validated linear SVM.
#
# From the paper: spike counts in 1000 ms windows, windows centred every 100 ms, an SVM as in the
# NDT toolbox (Meyers 2013), 20 cross-validation splits, resampling runs, accuracy as the median
# over runs, a null from runs with scrambled labels. The NDT defaults taken where the paper is
# silent (claims file, fig4d-decode-workload-all): a linear kernel with C = 1 (libsvm's default)
# and features z-scored with the training split's mean and standard deviation (reading e) or raw
# (reading f). How pseudo-trials are drawn is open; `draw_pseudo` implements reading (c), the
# largest equal number per label available in every session, drawn without replacement, and
# reading (d), each session's own trials, split into folds first and resampled with replacement
# within each fold to the largest session's fold size, so that no trial is in both training and
# test data.
# ---------------------------------------------------------------------------------------------

def draw_pseudo(groups: list[list[np.ndarray]], n_folds: int, reading: str, rng: np.random.Generator):
    """Trial indices for one resampling run.

    groups[g][label] holds the trial indices of session g with that label. Returns, per session,
    an array (labels, n_folds, per_fold) of trial indices; the same index positions across
    sessions form one pseudo-trial."""
    n_labels = len(groups[0])
    if reading == "c":
        k = min(len(ix) for g in groups for ix in g)
        per_fold = k // n_folds
        return [np.stack([rng.permutation(ix)[:per_fold * n_folds].reshape(n_folds, per_fold) for ix in g])
                for g in groups], per_fold
    per_fold = int(np.ceil(max(len(ix) for g in groups for ix in g) / n_folds))
    out = []
    for g in groups:
        lab = []
        for ix in g:
            p = rng.permutation(ix)
            folds = [p[f::n_folds] for f in range(n_folds)]
            lab.append(np.stack([rng.choice(fo, per_fold, replace=True) for fo in folds]))
        out.append(np.stack(lab))
    return out, per_fold


def decode_run(feats: list[np.ndarray], groups: list[list[np.ndarray]], n_folds: int, reading: str,
               zscore: bool, rng: np.random.Generator) -> np.ndarray:
    """One resampling run. feats[g]: (trials, units, windows) counts of session g.
    Returns the accuracy per window, averaged over the cross-validation splits."""
    from sklearn.svm import SVC
    idx, per_fold = draw_pseudo(groups, n_folds, reading, rng)
    n_labels = len(groups[0])
    # X: (labels, folds, per_fold, units, windows)
    X = np.concatenate([f[i] for f, i in zip(feats, idx)], axis=3).astype(float)
    n_win = X.shape[-1]
    y_fold = np.repeat(np.arange(n_labels), per_fold)
    acc = np.zeros(n_win)
    for f in range(n_folds):
        train = np.ones(n_folds, bool)
        train[f] = False
        Xtr = X[:, train].reshape(-1, X.shape[3], n_win)
        ytr = np.repeat(np.arange(n_labels), train.sum() * per_fold)
        Xte = X[:, f].reshape(-1, X.shape[3], n_win)
        for w in range(n_win):
            a, b = Xtr[:, :, w], Xte[:, :, w]
            if zscore:
                mu, sd = a.mean(0), a.std(0)
                sd[sd == 0] = 1.0
                a, b = (a - mu) / sd, (b - mu) / sd
            clf = SVC(kernel="precomputed", C=1.0).fit(a @ a.T, ytr)
            acc[w] += (clf.predict(b @ a.T) == y_fold).mean()
    return acc / n_folds


def decode(feats, groups, n_runs: int, n_null: int, n_folds: int, reading: str, zscore: bool,
           seed: int, n_jobs: int = -1):
    """Accuracy per run and window (n_runs, windows) and the same with labels scrambled within
    each session before each run (n_null, windows)."""
    from joblib import Parallel, delayed

    def shuffled(g, rng):
        allix = np.concatenate(g)
        p = rng.permutation(allix)
        cuts = np.cumsum([len(ix) for ix in g])[:-1]
        return np.split(p, cuts)

    def one(i, null):
        rng = np.random.default_rng([seed, i, int(null)])
        gr = [shuffled(g, rng) for g in groups] if null else groups
        return decode_run(feats, gr, n_folds, reading, zscore, rng)

    res = np.array(Parallel(n_jobs=n_jobs)(delayed(one)(i, False) for i in range(n_runs)))
    nul = np.array(Parallel(n_jobs=n_jobs)(delayed(one)(i, True) for i in range(n_null)))
    return res, nul.reshape(n_null, res.shape[1])


def realign(s: dict, k: int) -> dict:
    """A copy of session s in which the spikes stored in trial window i are moved to trial i + k.

    Used only for the exploratory alignment check of the notebook (the data check finds the set-size
    information of the spikes peaks when they are paired with the label of a later trial). Trials
    that receive no window are dropped."""
    st = s["trials"].start.values
    n = len(st)
    out = []
    for t in s["spike_times"]:
        i = np.searchsorted(st, t, "right") - 1
        keep = (i >= 0) & (i + k >= 0) & (i + k < n)
        out.append(np.sort(t[keep] - st[i[keep]] + st[i[keep] + k]))
    s2 = dict(s)
    s2["spike_times"] = out
    lo, hi = max(0, k), min(n, n + k)
    s2["trials"] = s["trials"].iloc[lo:hi].reset_index(drop=True)
    return s2


def null_t(x: np.ndarray, y: np.ndarray, paired: bool, n_perm: int, rng: np.random.Generator,
           perms: np.ndarray | None = None) -> np.ndarray:
    """The permutation distribution of t, (n_perm, units), for x and y (trials, units).

    Shuffling period labels within trials (paired) or condition labels across trials (unpaired)
    leaves this distribution unchanged, so it is computed once per neuron and reused for every
    label-scrambled repetition of a count. `perms` (from make_perms) may be passed to reuse one
    set of permutations for samples of the same size."""
    if paired:
        d = x - y
        return np.nan_to_num(paired_t(d, make_perms(d.shape[0], n_perm, True, rng) if perms is None else perms))
    n = x.shape[0] + y.shape[0]
    return np.nan_to_num(unpaired_null(x, y, make_perms(n, n_perm, False, rng) if perms is None else perms))


def obs_t(x: np.ndarray, y: np.ndarray, paired: bool) -> np.ndarray:
    return np.nan_to_num(paired_t(x - y) if paired else welch_t(x, y))


def p_from_null(t: np.ndarray, null: np.ndarray) -> np.ndarray:
    return ((np.abs(null) >= np.abs(t) - 1e-12).sum(0) + 1) / (null.shape[0] + 1)


def swap_within_trials(x: np.ndarray, y: np.ndarray, rng: np.random.Generator):
    """Scramble two period labels within each trial (the same swap for every unit of a session)."""
    flip = rng.random(x.shape[0]) < 0.5
    return np.where(flip[:, None], y, x), np.where(flip[:, None], x, y)


def cluster_masses(t: np.ndarray, thr: float) -> list[tuple[int, int, float]]:
    """Clusters of consecutive time points with |t| > thr and one sign: (start, stop, sum of t)."""
    out, i, n = [], 0, len(t)
    while i < n:
        if abs(t[i]) > thr:
            j = i
            while j + 1 < n and abs(t[j + 1]) > thr and np.sign(t[j + 1]) == np.sign(t[i]):
                j += 1
            out.append((i, j + 1, float(t[i:j + 1].sum())))
            i = j + 1
        else:
            i += 1
    return out
