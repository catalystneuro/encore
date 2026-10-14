"""Loading and measures for dandiset 001616 (SUMMER), human MTL single units during the film
"500 Days of Summer".

Gerken, Darcher et al., eLife reviewed preprint 106758 v1, doi:10.7554/eLife.106758.1.

Each NWB file holds one patient: spike times of every unit (milliseconds, recording clock, with
0 at the movie start), the unit's brain region, the movie annotations (53 labels, per frame and as
segments in movie time), and the watchlogs that map each presented frame (presentation time
stamp, seconds) to the recording clock (milliseconds). Files are streamed from the archive at the
pinned version; nothing is written to disk.

Where the parameters come from:

- The Methods of the paper: 80 ms bins (two frames), a window of 800 ms before and after each
  sample, labels of a bin taken from its first frame, camera cut labels extended to frames within
  520 ms of the cut, a gap of 32 s between training, validation and test samples, logistic
  regression with an L1 penalty (liblinear), z-scored with training statistics, Cohen's kappa,
  1000 test-label shuffles for chance. The responsive-unit test (baseline -1000 to 0 ms,
  19 overlapping 100 ms bins from 0 to 1000 ms, Wilcoxon signed-rank, Simes correction, spikes in
  at least a third of the pseudo-trials) and the cluster permutation test (p < 0.005 per bin,
  1000 permutations).
- The dataset's code (https://github.com/mormannlab/SUMMER at commit
  59fc2424615150481494edf3e31d707729d395ea): the bin edges and frames of `movie_binning_info`,
  the fold layout of ML_framework/dataloader.py (`BUFFER_NUMBER_REPEATED_PARTS`, five folds per
  part, test fold f, validation fold f+1), the grouping of hippocampal subregions
  (`REGION_ALTERNATIVE_NAMES`), the onset rule of calc_responsive_units.py, and the ZETA test it
  uses for responsive units (shown as a variant).
- Common choices where neither says: class weights balanced in the logistic regression (the paper
  oversamples the minority class for its LSTM), the grid of C values, the threshold search for
  single units, and dropping spikes that fall in playback pauses.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "001616"
DANDISET_VERSION = "0.260702.0824"

BIN_MS = 80                 # Methods: 80 ms bins, two frames of 40 ms
WINDOW_BINS = 10            # Methods: 800 ms before and 800 ms after a sample
CUT_SPREAD_S = 0.52         # Methods: cut labels cover frames within 520 ms of the cut onset
GAP_S = 32                  # Methods: 32 s between training, validation and test samples
# dataset code, ML_framework/dataloader.py: number of repeated parts for each gap size
PARTS_FOR_GAP = {4: 59, 8: 36, 12: 26, 16: 21, 20: 17, 24: 14, 28: 12, 32: 11, 36: 10, 40: 9, 44: 8}
C_GRID = (0.001, 0.003, 0.01, 0.03)   # common choice; chosen per split on the validation kappa
N_PERMUTATIONS = 1000       # Methods
ALPHAS = (0.001, 0.01)      # Results and Figure 2 give 0.001, the Methods 0.01
CLUSTER_ALPHA = 0.005       # Methods

# Paper label name -> (dandiset label, value that marks the feature)
LABELS = {
    "Summer": ("summer", 1), "Tom": ("tom", 1), "McKenzie": ("mckenzie", 1),
    "Persons": ("persons", 1), "Summer Faces": ("summer-faces", 1), "Tom Faces": ("tom-faces", 1),
    "Summer Presence": ("summer-presence", 1), "Camera Cuts": ("camera-cuts", 1),
    "Scene Cuts": ("scenes", 1), "Indoor": ("indoor-setting", 1), "Outdoor": ("indoor-setting", 0),
}
CUT_LABELS = ("camera-cuts", "scenes")
# dataset code, visualization/plot_code/nwb_io.py
REGIONS = {"A": ["A"], "H": ["H", "AH", "MH", "PH"], "EC": ["EC"], "PHC": ["PHC", "APH", "PPH", "MPH"],
           "PIC": ["PIC"]}


def _text(value):
    return value.decode() if isinstance(value, bytes) else value


def _ragged(group, name):
    data, index = group[name][:], group[name + "_index"][:]
    starts = np.r_[0, index[:-1]]
    return [data[a:b] for a, b in zip(starts, index)]


def asset_urls(version: str = DANDISET_VERSION) -> list[tuple[str, str, str]]:
    """(path, blob id, streaming URL) of every NWB file at a version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, version)
        return sorted((a.path, a.blob, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def load_session(path: str, url: str) -> dict:
    """Everything the analysis uses from one file, without the waveforms."""
    f = h5py.File(remfile.File(url), "r")
    u = f["units"]
    units = pd.DataFrame({k: [_text(x) for x in u[k][:]] for k in
                          ("unit_id", "csc_nr", "brain_region", "hemisphere", "is_single_unit")})
    s = {"path": path,
         "subject_id": _text(f["general/subject/subject_id"][()]),
         "sex": _text(f["general/subject/sex"][()]),
         "age": _text(f["general/subject/age"][()]),
         "units": units,
         "units_description": _text(u.attrs["description"]),
         "spikes_ms": _ragged(u, "spike_times")}
    e = f["general/extracellular_ephys/electrodes"]
    s["electrodes"] = pd.DataFrame({k: [_text(x) for x in e[k][:]] for k in ("csc_nr", "group_name", "brain_region")})
    for name in ("cleaned_watchlogs", "raw_watchlogs"):
        g = f["stimulus/presentation/" + name]
        s[name] = pd.DataFrame({"pts": g["pts"][:], "rec_ms": g["neural_recording_time"][:]})
    for name in ("annotations_base", "annotations_patient_aligned"):
        g = f["stimulus/presentation/" + name]
        s[name] = pd.DataFrame({"start": g["start_time"][:], "stop": g["stop_time"][:],
                                "label": [_text(x) for x in g["label_name"][:]], "value": g["value"][:]})
        s[name + "_unit"] = _text(g["start_time"].attrs["description"])
    g = f["processing/machine_learning/movie_annotations_indicator_functions"]
    s["indicator"] = dict(zip([_text(x) for x in g["label_name"][:]], _ragged(g, "indicator_function")))
    g = f["processing/machine_learning/movie_binning_info"]
    lengths = list(g["bin_length"][:])
    i = lengths.index(BIN_MS)
    s["edges_s"] = _ragged(g, "edges")[i]
    s["bin_frames"] = np.array([int(_text(x).split("_")[1].split(".")[0]) for x in _ragged(g, "frames")[i]])
    s["frame_times_base"] = f["stimulus/presentation/movie_frame_times_base/data"][:]
    s["frame_times_analysis"] = f["stimulus/presentation/movie_frame_times_analysis/data"][:]
    f.close()
    return s


def load_all(version: str = DANDISET_VERSION, workers: int = 8) -> list[dict]:
    assets = asset_urls(version)
    with ThreadPoolExecutor(workers) as pool:
        sessions = list(pool.map(lambda a: load_session(a[0], a[2]), assets))
    for s, a in zip(sessions, assets):
        s["blob"] = a[1]
    return sorted(sessions, key=lambda s: int(s["subject_id"]))


# --- time base ------------------------------------------------------------------------------

def pauses(watchlog: pd.DataFrame) -> np.ndarray:
    """(start, stop) on the recording clock (ms) of each playback pause: consecutive entries with
    the same presentation time stamp."""
    pts, rec = watchlog.pts.to_numpy(), watchlog.rec_ms.to_numpy()
    i = np.where(np.diff(pts) == 0)[0]
    return np.c_[rec[i], rec[i + 1]]


def movie_time(spikes_ms: np.ndarray, watchlog: pd.DataFrame) -> np.ndarray:
    """Spike times in movie seconds, through the cleaned watchlog. Spikes in pauses and outside
    the logged playback are dropped."""
    pts, rec = watchlog.pts.to_numpy(), watchlog.rec_ms.to_numpy()
    keep = (spikes_ms >= rec[0]) & (spikes_ms <= rec[-1])
    for a, b in pauses(watchlog):
        keep &= ~((spikes_ms > a) & (spikes_ms < b))
    return np.interp(spikes_ms[keep], rec, pts)


def movie_to_rec(t_s: np.ndarray, watchlog: pd.DataFrame) -> np.ndarray:
    """Movie seconds to recording milliseconds (first presentation of each time stamp)."""
    pts, rec = watchlog.pts.to_numpy(), watchlog.rec_ms.to_numpy()
    first = np.r_[True, np.diff(pts) != 0]
    return np.interp(t_s, pts[first], rec[first])


def unit_table(sessions: list[dict]) -> pd.DataFrame:
    rows = []
    for s in sessions:
        for k, r in s["units"].iterrows():
            region = next((name for name, members in REGIONS.items() if r.brain_region in members), "other")
            rows.append({"patient": int(s["subject_id"]), "index": k, "unit_id": r.unit_id,
                         "brain_region": r.brain_region, "region": region,
                         "single": bool(r.is_single_unit), "n_spikes": len(s["spikes_ms"][k])})
    return pd.DataFrame(rows)


def movie_spikes(sessions: list[dict]) -> list[np.ndarray]:
    """Spike times in movie seconds, one array per unit, in the order of `unit_table`."""
    return [movie_time(sp, s["cleaned_watchlogs"]) for s in sessions for sp in s["spikes_ms"]]


def binned_counts(spikes_s: list[np.ndarray], edges_s: np.ndarray) -> np.ndarray:
    """Units x bins spike counts on the 80 ms bin edges."""
    return np.array([np.histogram(t, edges_s)[0] for t in spikes_s], dtype=np.int16)


def window_sums(counts: np.ndarray, half: int = WINDOW_BINS) -> np.ndarray:
    """Samples x units: spikes from `half` bins before to `half` bins after each bin (the bin
    itself included in the after part), truncated at the ends."""
    n = counts.shape[1]
    c = np.cumsum(np.pad(counts.astype(np.int32), ((0, 0), (1, 0))), axis=1)
    k = np.arange(n)
    return (c[:, np.clip(k + half, 0, n)] - c[:, np.clip(k - half, 0, n)]).T.astype(np.float32)


# --- labels -----------------------------------------------------------------------------------

def frame_labels(session: dict, label: str) -> np.ndarray:
    """Per-frame label (frames 1..125743, index = frame - 1). Cut labels are extended to the
    frames within 520 ms after each cut onset."""
    v = session["indicator"][label].copy()
    if label in CUT_LABELS:
        onsets = np.where(v == 1)[0]
        spread = int(round(CUT_SPREAD_S / 0.04))
        out = np.zeros_like(v)
        for i in onsets:
            out[i:i + spread] = 1
        v = out
    return v


def bin_labels(session: dict, label: str) -> np.ndarray:
    """Label of each 80 ms bin, from its first frame (`movie_binning_info` gives one frame per
    bin); values other than 0 and 1 (99, excluded) are kept as they are."""
    return frame_labels(session, label)[session["bin_frames"] - 1]


def onsets(annotations: pd.DataFrame, label: str, value: int, min_absence: float = 1.0,
           min_presence: float | None = 1.0) -> np.ndarray:
    """Onsets of a feature preceded by at least `min_absence` (s) without it and, if
    `min_presence` is given, lasting at least that long. Times as in `annotations`."""
    a = annotations[(annotations.label == label) & (annotations.value == value)].sort_values("start")
    start, stop = a.start.to_numpy(), a.stop.to_numpy()
    keep = np.r_[False, start[1:] - min_absence > stop[:-1]]
    if min_presence is not None:
        keep &= (stop - start) >= min_presence
    return start[keep]


# --- responsive units (Methods) ----------------------------------------------------------------

def _counts_in(t: np.ndarray, starts: np.ndarray, width: float) -> np.ndarray:
    return np.searchsorted(t, starts + width, side="left") - np.searchsorted(t, starts, side="left")


def wilcoxon_simes(spikes_s: np.ndarray, events_s: np.ndarray) -> tuple[float, float]:
    """Simes-combined p of 19 overlapping 100 ms bins (0 to 1000 ms) against the baseline rate
    (-1000 to 0 ms, per 100 ms), two-sided Wilcoxon signed-rank across pseudo-trials, and the
    fraction of pseudo-trials with a spike from -1000 to 1000 ms. p = 1 below a third."""
    t = np.sort(spikes_s)
    base = _counts_in(t, events_s - 1.0, 1.0) / 10.0
    active = np.mean(_counts_in(t, events_s - 1.0, 2.0) > 0) if len(events_s) else 0.0
    if active < 1 / 3 or len(events_s) < 2:
        return 1.0, active
    starts = events_s[:, None] + 0.05 * np.arange(19)[None, :]
    bins = _counts_in(t, starts.ravel(), 0.1).reshape(starts.shape)
    diff = bins - base[:, None]
    p = np.ones(19)
    for j in range(19):
        if np.any(diff[:, j] != 0):
            p[j] = stats.wilcoxon(diff[:, j]).pvalue
    ps = np.sort(p)
    return float(min(1.0, np.min(19 * ps / np.arange(1, 20)))), active


def responsive_table(spikes_s: list[np.ndarray], t_range: tuple[float, float],
                     events: dict[str, np.ndarray]) -> pd.DataFrame:
    """For one patient's units: the Wilcoxon-Simes p, the fraction of active pseudo-trials, the
    number of pseudo-trials and the trial-averaged PSTH (Methods z-scoring, and the code's
    per-trial z-scoring) for each label. Events whose window leaves the patient's logged
    playback are left out."""
    rows = []
    for name, ev in events.items():
        ev = ev[(ev - 1.0 >= t_range[0]) & (ev + 1.0 <= t_range[1])]
        for i, t in enumerate(spikes_s):
            p, active = wilcoxon_simes(t, ev)
            rows.append({"unit": i, "label": name, "p": p, "active": active, "trials": len(ev),
                         "psth": mean_psth(t, ev), "psth_trial_z": mean_psth(t, ev, per_trial_z=True)})
    return pd.DataFrame(rows)


def mean_psth(spikes_s: np.ndarray, events_s: np.ndarray, per_trial_z: bool = False) -> np.ndarray:
    """Trial-averaged spike counts in 20 bins of 100 ms from -1000 to 1000 ms, z-scored over the
    20 bins (Methods). With `per_trial_z`, each trial is z-scored first and then averaged, as in
    the dataset's code; trials without spikes stay at 0."""
    t = np.sort(spikes_s)
    starts = events_s[:, None] - 1.0 + 0.1 * np.arange(20)[None, :]
    m = _counts_in(t, starts.ravel(), 0.1).reshape(starts.shape).astype(float)
    if per_trial_z:
        sd = m.std(1, keepdims=True)
        z = np.where(sd > 0, (m - m.mean(1, keepdims=True)) / np.where(sd > 0, sd, 1), 0.0)
        return z.mean(0)
    v = m.mean(0)
    return (v - v.mean()) / v.std() if v.std() > 0 else np.zeros_like(v)


def _clusters(t: np.ndarray, p: np.ndarray) -> list[float]:
    sums, current = [], 0.0
    for tv, pv in zip(t, p):
        if pv < CLUSTER_ALPHA:
            current += abs(tv)
        elif current:
            sums.append(current)
            current = 0.0
    if current:
        sums.append(current)
    return sums


def cluster_test(psth: np.ndarray, responsive: np.ndarray, rng: np.random.Generator,
                 n_perm: int = N_PERMUTATIONS) -> tuple[float, float]:
    """Largest cluster sum of |t| between responsive and non-responsive units, and its
    permutation p (fraction of label permutations whose largest cluster sum is at least it)."""
    if responsive.sum() < 2 or (~responsive).sum() < 2:
        return 0.0, 1.0

    def largest(mask):
        t, p = stats.ttest_ind(psth[mask], psth[~mask], axis=0)
        c = _clusters(np.nan_to_num(t), np.nan_to_num(p, nan=1.0))
        return max(c) if c else 0.0

    observed = largest(responsive)
    if observed == 0:
        return 0.0, 1.0
    null = np.array([largest(rng.permutation(responsive)) for _ in range(n_perm)])
    return observed, float(np.mean(null >= observed))


# --- splits and decoding -------------------------------------------------------------------------

def fold_blocks(n: int, gap_s: int = GAP_S, window_s: float = 2 * WINDOW_BINS * BIN_MS / 1000):
    """Per repeated part, the five folds and the gaps after them (sample indices), as in the
    dataset's code with sequence = the 1.6 s window."""
    parts = PARTS_FOR_GAP[gap_s]
    base = int(n / parts)
    gap = int(np.ceil((gap_s + window_s) * 1000 / BIN_MS))
    length = int((base - 5 * gap) / 5)
    blocks = []
    for p in range(parts):
        i = p * base
        folds = [np.arange(i + j * (length + gap), i + j * (length + gap) + length) for j in range(5)]
        gaps = [np.arange(i + j * (length + gap) + length, i + (j + 1) * (length + gap)) for j in range(5)]
        blocks.append((folds, gaps))
    return blocks


def split(n: int, test_fold: int, val_fold: int | None = None, gap_s: int = GAP_S):
    """Train, validation and test indices. Test is fold `test_fold` (0-4), validation fold
    `val_fold` (default the next one); training is the other three folds with the gaps between
    adjacent training folds (the gap after fold 5 leads to fold 1 of the next part), as in the
    dataset's code."""
    val_fold = (test_fold + 1) % 5 if val_fold is None else val_fold
    train_folds = [j for j in range(5) if j not in (test_fold, val_fold)]
    tr, va, te = [], [], []
    for folds, gaps in fold_blocks(n, gap_s):
        te.append(folds[test_fold])
        va.append(folds[val_fold])
        for j in train_folds:
            tr.append(folds[j])
            if (j + 1) % 5 in train_folds:
                tr.append(gaps[j])
    return np.concatenate(tr), np.concatenate(va), np.concatenate(te)


def random_split(n: int, sizes: tuple[int, int, int], rng: np.random.Generator):
    order = rng.permutation(n)
    a, b, c = sizes
    return np.sort(order[:a]), np.sort(order[a:a + b]), np.sort(order[a + b:a + b + c])


def kappa(y: np.ndarray, p: np.ndarray) -> float:
    """Cohen's kappa for binary labels."""
    y, p = np.asarray(y, bool), np.asarray(p, bool)
    po = np.mean(y == p)
    pe = y.mean() * p.mean() + (1 - y.mean()) * (1 - p.mean())
    return float((po - pe) / (1 - pe)) if pe < 1 else 0.0


def shuffled_kappas(y: np.ndarray, p: np.ndarray, rng: np.random.Generator, n: int = N_PERMUTATIONS):
    """Kappa of the fixed predictions against shuffled test labels (Methods, test-set shuffle)."""
    y = np.asarray(y, bool)
    p = np.asarray(p, bool)
    ys = np.array([rng.permutation(y) for _ in range(n)])
    po = np.mean(ys == p[None, :], axis=1)
    pe = y.mean() * p.mean() + (1 - y.mean()) * (1 - p.mean())
    return (po - pe) / (1 - pe) if pe < 1 else np.zeros(n)


def fit_logreg(S: np.ndarray, y: np.ndarray, tr: np.ndarray, va: np.ndarray, te: np.ndarray,
               columns=None, c_grid=C_GRID) -> dict:
    """L1 logistic regression on window sums, z-scored with training statistics; C chosen on the
    validation kappa. Samples whose label is not 0 or 1 are left out."""
    from sklearn.linear_model import LogisticRegression
    ok = (y == 0) | (y == 1)
    tr, va, te = tr[ok[tr]], va[ok[va]], te[ok[te]]
    X = S if columns is None else S[:, columns]
    mu = X[tr].mean(0)
    sd = X[tr].std(0)
    sd[sd == 0] = 1
    Ztr, Zva, Zte = ((X[i] - mu) / sd for i in (tr, va, te))
    best, test_by_c = None, {}
    for c in c_grid:
        model = LogisticRegression(l1_ratio=1.0, solver="liblinear", C=c, class_weight="balanced", random_state=0)
        model.fit(Ztr, y[tr])
        k = kappa(y[va], model.predict(Zva))
        test_by_c[c] = kappa(y[te], model.predict(Zte))
        if best is None or k > best[0]:
            best = (k, c, model)
    k_val, c, model = best
    pred = model.predict(Zte)
    return {"kappa": kappa(y[te], pred), "kappa_val": k_val, "C": c, "coef": model.coef_.ravel(),
            "y_test": y[te], "pred": pred, "n": (len(tr), len(va), len(te)), "kappa_by_C": test_by_c}


def fit_folds(S: np.ndarray, columns, labels: dict, splits: list) -> dict:
    """`fit_logreg` for each label and split on one subset of units, sliced once."""
    X = np.ascontiguousarray(S[:, columns])
    return {(name, f): fit_logreg(X, y, *sp) for name, y in labels.items() for f, sp in enumerate(splits)}


def run_jobs(jobs, n_jobs: int = -1):
    """Run (function, args) pairs in parallel processes."""
    from joblib import Parallel, delayed
    return Parallel(n_jobs=n_jobs)(delayed(f)(*a) for f, a in jobs)


def kappa_rows(y: np.ndarray, P: np.ndarray) -> np.ndarray:
    """Cohen's kappa of each row of a boolean prediction matrix against labels y."""
    y = np.asarray(y, bool)
    P = np.asarray(P, bool)
    po = (P == y[None, :]).mean(1)
    q = P.mean(1)
    pe = y.mean() * q + (1 - y.mean()) * (1 - q)
    with np.errstate(invalid="ignore", divide="ignore"):
        k = (po - pe) / (1 - pe)
    return np.where(pe < 1, k, 0.0)


def threshold_unit(x: np.ndarray, y: np.ndarray, va: np.ndarray, te: np.ndarray, n_q: int = 50) -> float:
    """Single-unit decoding (Methods, Figure 3b): the threshold and direction with the best
    validation kappa, among up to `n_q` quantiles of the unit's window counts, applied to the
    test set."""
    t = np.unique(np.quantile(x[va], np.linspace(0, 1, n_q)))
    above = x[va][None, :] > t[:, None]
    k = np.r_[kappa_rows(y[va], above), kappa_rows(y[va], ~above)]
    best = int(np.argmax(k))
    threshold, sign = t[best % len(t)], (1 if best < len(t) else -1)
    pred = x[te] > threshold if sign == 1 else ~(x[te] > threshold)
    return kappa(y[te], pred)


def unit_summary(url: str) -> dict:
    """Units, spike counts and the sorted spike times of a file, to compare deposits."""
    f = h5py.File(remfile.File(url), "r")
    u = f["units"]
    out = {"subject_id": _text(f["general/subject/subject_id"][()]),
           "regions": [_text(x) for x in u["brain_region"][:]],
           "spikes_ms": np.sort(u["spike_times"][:]),
           "n_units": len(u["spike_times_index"])}
    f.close()
    return out


def ranking(coefs: list[np.ndarray], rng: np.random.Generator) -> np.ndarray:
    """Methods: units grouped by the number of models with a non-zero coefficient (most first),
    then by mean absolute coefficient; ties (all zero) in a random order."""
    C = np.abs(np.array(coefs))
    nonzero = (C > 0).sum(0)
    mean_abs = C.mean(0)
    tiebreak = rng.permutation(C.shape[1])
    return np.lexsort((tiebreak, -mean_abs, -nonzero))
