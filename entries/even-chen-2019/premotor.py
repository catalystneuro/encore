"""Loading and measures for the delayed center-out reaching data of dandiset 000121.

Even-Chen, Sheffer, Vyas, Ryu & Shenoy (2019), PLOS Computational Biology,
doi:10.1371/journal.pcbi.1006808.

Each NWB file holds one session of one monkey (J, "JenkinsC", or R, "Reggie"): a trials table,
hand, cursor and eye positions sampled at 1 kHz within trials, and 192 units, one per electrode of
two 96-channel Utah arrays, holding the threshold crossings at 1 ms resolution (the conversion,
github.com/catalystneuro/shenoy-lab-to-nwb at commit 319acb4, builds them from the rig's
`spikeRaster` and `spikeRaster2`). Files are streamed from the archive at the pinned version and
reduced as they load; nothing is written to disk.

Where the parameters come from:

- From the paper's Methods: the 200 ms window before the go cue; subtraction of each channel's
  average rate for the day; removal of trials without a delay; PCA on condition averages with 6
  (J) and 5 (R) components kept; the regressions to target x and y, with y fit in the null space
  of x, and to maximum speed on the full activity, fit after x and y are projected out; the
  on-axis and off-axis split of deviations; RBF SVMs, one-vs-one, 10-fold cross-validation.
- Common choices here, as the Methods leave them open: the PMd array is units 96 to 191 (see
  `PMD_UNITS`); the day's average rate is the session's spike count over its recorded time (the
  time of the hand samples, about the summed trial time; spikes, like hand samples, exist only
  within trials, see `units.in_trials`); a
  delayed trial has a delay of at least `MIN_DELAY_S`; hand positions are smoothed with a
  Gaussian of SD `HAND_SMOOTH_MS` before the speed is taken; maximum speed is searched from the
  go cue to `SPEED_WINDOW_S` after it; movement onset is the last time before the peak that speed
  is below `ONSET_FRACTION` of the peak (`onset_after_go`, the same searched only from the go
  cue, is a variant); the SVM uses sklearn's default C and gamma on z-scored
  features (the paper tuned them on held-out trials and does not report them).
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter1d
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

DANDISET_ID = "000121"
DANDISET_VERSION = "0.220124.2156"

PMD_UNITS = slice(96, 192)   # units whose `electrodes` point to the rows of group "2" (PMd)
FILE_PMD_UNITS = slice(0, 96)  # units whose `electrode_group` says PMd (variant)
DELAY_WINDOW_S = 0.2         # Methods: 200 ms before the go cue
MIN_DELAY_S = 0.25           # delayed trials; the shortest stated delay is 300 ms
BIN_S = 0.02                 # time course aligned on target onset
TC_START_S, TC_STOP_S = -0.2, 0.7
HAND_SMOOTH_MS = 20.0
SPEED_WINDOW_S = 1.0
ONSET_FRACTION = 0.1
HAND_LIMIT_MM = 250.0        # samples beyond this are tracking glitches (positions reach 1258)
N_PCS = {"J": 6, "R": 5}     # Methods

CONFIGS = ("ring", "horizontal", "vertical", "3-rings")
# Methods, Experimental design: configuration of each session by date
METHODS_CONFIG = {
    "J": {"2015-10-09": "ring", "2015-10-15": "ring", "2015-10-26": "ring", "2015-10-27": "ring",
          "2015-09-24": "horizontal", "2015-09-25": "horizontal", "2015-09-29": "horizontal",
          "2015-09-30": "horizontal", "2015-10-01": "vertical", "2015-10-02": "vertical",
          "2015-10-07": "vertical", "2015-10-08": "vertical", "2016-01-27": "3-rings",
          "2016-01-28": "3-rings", "2016-01-29": "3-rings", "2016-02-02": "3-rings"},
    "R": {"2017-01-24": "ring", "2017-01-25": "ring", "2017-01-17": "horizontal",
          "2017-01-18": "horizontal", "2017-01-15": "vertical", "2017-01-16": "vertical",
          "2017-01-19": "3-rings"},
}


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    value = value[()]
    if isinstance(value, np.ndarray):
        value = value[0]
    return value.decode() if isinstance(value, bytes) else str(value)


def _ragged(group, name) -> list[np.ndarray]:
    data, index = group[name][:], group[f"{name}_index"][:].astype(np.int64)
    return np.split(data, index[:-1])


def infer_config(tx: np.ndarray, ty: np.ndarray) -> tuple[str, np.ndarray]:
    """The session's configuration from its center-out targets, and which trials fit it.

    horizontal: targets on the x axis; vertical: on the y axis; 3-rings: radii 40, 80 and 120 mm;
    ring: one radius. The layout of the majority of trials wins; trials to other targets are
    flagged False.
    """
    tx, ty = np.round(tx, 1), np.round(ty, 1)
    radius = np.round(np.hypot(tx, ty))
    candidates = {
        "horizontal": ty == 0,
        "vertical": tx == 0,
        "3-rings": np.isin(radius, [40, 80, 120]) & (len(np.unique(radius)) >= 3),
        "ring": radius == pd.Series(radius).mode()[0],
    }
    best = max(candidates, key=lambda k: candidates[k].sum())
    return best, candidates[best]


def _first_after(values: list[np.ndarray], times: np.ndarray) -> np.ndarray:
    out = np.full(len(times), np.nan)
    for i, (v, t) in enumerate(zip(values, times)):
        later = v[v >= t] if np.isfinite(t) else []
        if len(later):
            out[i] = later.min()
    return out


def _kinematics(ht: np.ndarray, hxy: np.ndarray, go: np.ndarray, start: np.ndarray,
                stop: np.ndarray) -> pd.DataFrame:
    """Per trial: maximum hand speed after the go cue, where it happened, and movement onset.

    Only the trial's own samples are used (samples exist only within trials, 1 ms apart).
    """
    rows = []
    for g, a, b in zip(go, start, stop):
        i0, i1 = np.searchsorted(ht, a), np.searchsorted(ht, b, side="right")
        t, xy = ht[i0:i1], hxy[i0:i1]
        row = {"max_speed": np.nan, "x_at_max": np.nan, "y_at_max": np.nan, "onset": np.nan,
               "onset_05": np.nan, "onset_20": np.nan, "onset_after_go": np.nan,
               "glitch": bool(np.any(np.abs(xy) > HAND_LIMIT_MM))}
        rows.append(row)
        if row["glitch"] or len(t) < 100 or not np.any(t >= g):
            continue
        smooth = gaussian_filter1d(xy, HAND_SMOOTH_MS, axis=0)  # samples are 1 ms apart
        speed = np.hypot(*np.gradient(smooth, t, axis=0).T)       # mm/s
        window = np.flatnonzero((t >= g) & (t <= g + SPEED_WINDOW_S))
        peak = window[np.argmax(speed[window])]
        row.update(max_speed=speed[peak], x_at_max=smooth[peak, 0], y_at_max=smooth[peak, 1])
        for key, fraction in (("onset", ONSET_FRACTION), ("onset_05", 0.05), ("onset_20", 0.2)):
            below = np.flatnonzero(speed[:peak] < fraction * speed[peak])
            row[key] = t[below[-1]] if len(below) else np.nan
        # variant: onset searched only from the go cue to the peak
        below = np.flatnonzero(speed[window[0]:peak] < ONSET_FRACTION * speed[peak])
        row["onset_after_go"] = t[window[0] + below[-1]] if len(below) else np.nan
    return pd.DataFrame(rows)


def _counts(units: list[np.ndarray], start: np.ndarray, stop: np.ndarray) -> np.ndarray:
    """Spike counts, trials by units, in [start, stop)."""
    return np.stack([np.searchsorted(u, stop) - np.searchsorted(u, start) for u in units], axis=1)


def load_session(path: str, url: str) -> dict:
    """One session: its trials, unit summaries, and for analysed trials the reduced activity.

    Analysed trials (`trials.analysed`) are successful center-out trials with a delay of at least
    MIN_DELAY_S. For them: counts of every unit in the 200 ms before the go cue (`delay_counts`,
    trials x 192), in 200 to 400 ms after it (`move_counts`), and PMd counts in 20 ms bins from 200
    ms before to 700 ms after target onset (`tc_counts`, trials x 96 x 45, uint8). Kinematics are
    computed for every successful center-out trial.
    """
    with h5py.File(remfile.File(url), "r") as f:
        subject = _text(f["general/subject/subject_id"])
        start_time = _text(f["session_start_time"])
        tr = f["intervals/trials"]
        cols = ["start_time", "stop_time", "is_successful", "task_id", "version_id",
                "go_cue_time", "target_shown_time", "target_held_time"]
        trials = pd.DataFrame({c: tr[c][:] for c in cols})
        pos = _ragged(tr, "target_pos")
        trials["tx"] = [p[0] for p in pos]
        trials["ty"] = [p[1] for p in pos]
        trials["first_acquire"] = _first_after(_ragged(tr, "target_acquire_time"),
                                               trials.go_cue_time.values)
        hand = f["processing/behavior/Position/Hand"]
        ht = hand["timestamps"][:]
        hxy = hand["data"][:, :2]
        meta = {
            "hand_unit": hand["data"].attrs["unit"],
            "hand_conversion": float(hand["data"].attrs["conversion"]),
            "cursor_minus_hand_mm": np.quantile(np.abs(
                f["processing/behavior/Position/Cursor/data"][:] - hxy).max(axis=1), [0.5, 0.99, 1]),
            "electrode_group_names": [f[r].name.rsplit("/", 1)[1]
                                      for r in f["units/electrode_group"][:]],
            "unit_electrodes": f["units/electrodes"][:],
            "electrode_rows_group": [g.decode() for g in
                                     f["general/extracellular_ephys/electrodes/group_name"][:]],
            "lfp_electrodes": {k: (int(v["electrodes"][0]), int(v["electrodes"][-1]))
                               for k, v in f["processing/ecephys/LFP"].items()},
        }
        index = f["units/spike_times_index"][:].astype(np.int64)
        spikes = f["units/spike_times"][:]
    units = np.split(spikes, index[:-1])
    del spikes
    decreases = [int(np.sum(np.diff(u) < 0)) for u in units]
    units = [np.sort(u) if d else u for u, d in zip(units, decreases)]  # counting needs order

    monkey = "J" if subject.startswith("Jenkins") else "R"
    date = start_time[:10]
    dt = np.diff(ht)
    recorded_s = float(len(ht) * np.median(dt))  # samples exist only within trials
    unit_info = pd.DataFrame({
        "n_spikes": [len(u) for u in units],
        "first": [u[0] if len(u) else np.nan for u in units],
        "last": [u[-1] if len(u) else np.nan for u in units],
        "time_decreases": decreases,
        "group_label": meta["electrode_group_names"],
        "electrode": meta["unit_electrodes"],
    })
    unit_info["electrode_group"] = [meta["electrode_rows_group"][e] for e in unit_info.electrode]
    unit_info["rate"] = unit_info.n_spikes / recorded_s
    # spikes inside trial intervals: spikes, like hand samples, should exist only within trials
    order = np.argsort(trials.start_time.values)
    t0, t1 = trials.start_time.values[order], trials.stop_time.values[order]
    unit_info["in_trials"] = [int(np.sum(np.searchsorted(u, t1) - np.searchsorted(u, t0))) for u in units]
    trial_s = float(np.sum(t1 - t0))

    trials["delay"] = trials.go_cue_time - trials.target_shown_time
    trials["center_out"] = (np.round(trials.tx, 1) != 0) | (np.round(trials.ty, 1) != 0)
    co = trials.center_out.values
    config, fits = infer_config(trials.tx.values[co], trials.ty.values[co])
    trials["in_layout"] = False
    trials.loc[co, "in_layout"] = fits
    trials["successful"] = trials.is_successful == 1
    trials["analysed"] = (trials.successful & trials.center_out & trials.in_layout
                          & (trials.delay >= MIN_DELAY_S))

    kin_rows = trials.successful & trials.center_out
    k = trials[kin_rows]
    kin = _kinematics(ht, hxy, k.go_cue_time.values, k.start_time.values, k.stop_time.values)
    for c in kin:
        trials[c] = np.nan if c != "glitch" else False
        trials.loc[kin_rows, c] = kin[c].values
    trials["reaction_time"] = trials.onset - trials.go_cue_time
    del ht, hxy

    a = trials[trials.analysed]
    go, shown = a.go_cue_time.values, a.target_shown_time.values
    delay_counts = _counts(units, go - DELAY_WINDOW_S, go).astype(np.int16)
    move_counts = _counts(units, go + 0.2, go + 0.4).astype(np.int16)
    edges = shown[:, None] + np.arange(TC_START_S, TC_STOP_S + BIN_S / 2, BIN_S)[None, :]
    pmd = units[PMD_UNITS]
    tc = np.stack([np.diff(np.searchsorted(u, edges.ravel()).reshape(edges.shape), axis=1)
                   for u in pmd], axis=1).astype(np.uint8)
    return {
        "path": path, "monkey": monkey, "date": date, "config": config,
        "methods_config": METHODS_CONFIG[monkey].get(date), "recorded_s": recorded_s,
        "trial_s": trial_s, "span_s": float(max(t1.max(), np.nanmax(unit_info["last"]))),
        "n_hand_samples": len(dt) + 1, "hand_dt_median": float(np.median(dt)),
        "trials": trials, "units": unit_info, "meta": meta,
        "delay_counts": delay_counts, "move_counts": move_counts, "tc_counts": tc,
    }


def load_all(workers: int = 4) -> list[dict]:
    """Every session, loaded in parallel, ordered by monkey and date."""
    urls = asset_urls()
    with ThreadPoolExecutor(workers) as pool:
        sessions = list(pool.map(lambda pu: load_session(*pu), urls))
    return sorted(sessions, key=lambda s: (s["monkey"], s["date"]))


def delay_rates(session: dict, units: slice = PMD_UNITS, day_mean: str = "session") -> np.ndarray:
    """Delay activity of analysed trials (spikes/s) minus each channel's mean rate for the day.

    day_mean "session": the channel's rate over the whole recorded session (main);
    "trials": its mean over the analysed trials' delay windows (variant).
    """
    rates = session["delay_counts"][:, units] / DELAY_WINDOW_S
    if day_mean == "session":
        return rates - session["units"].rate.values[units][None, :]
    return rates - rates.mean(axis=0, keepdims=True)


def monkey_table(sessions: list[dict], monkey: str, units: slice = PMD_UNITS,
                 day_mean: str = "session") -> tuple[pd.DataFrame, np.ndarray]:
    """All analysed trials of a monkey (one row each) and their delay activity."""
    rows, X = [], []
    for s in sessions:
        if s["monkey"] != monkey:
            continue
        a = s["trials"][s["trials"].analysed].copy()
        a["date"], a["config"], a["methods_config"] = s["date"], s["config"], s["methods_config"]
        rows.append(a)
        X.append(delay_rates(s, units, day_mean))
    t = pd.concat(rows, ignore_index=True)
    t["condition"] = t.config + ":" + t.tx.round(1).astype(str) + "," + t.ty.round(1).astype(str)
    t["distance"] = np.hypot(t.tx, t.ty)
    return t, np.concatenate(X)


def fit_plane(t: pd.DataFrame, X: np.ndarray, n_pcs: int) -> dict:
    """PCA on mean-centred condition averages, then x and y regressed from the PC scores.

    Returns the condition means, their mean `mu`, the loadings `A` (n_pcs x channels), the
    explained variance ratios of all components, and the plane: `wx`, `wy` (directions in channel
    space, orthogonal) with intercepts, so that x = (X - mu) @ wx + ix, in mm.
    """
    cond = pd.DataFrame(X).groupby(t.condition.values).mean()
    mu = cond.values.mean(axis=0)
    _, sv, vt = np.linalg.svd(cond.values - mu, full_matrices=False)
    A = vt[:n_pcs]
    S = (X - mu) @ A.T
    ones = np.ones((len(S), 1))
    bx = np.linalg.lstsq(np.hstack([ones, S]), t.tx.values, rcond=None)[0]
    null = np.eye(n_pcs) - np.outer(bx[1:], bx[1:]) / (bx[1:] @ bx[1:])
    by = np.linalg.lstsq(np.hstack([ones, S @ null]), t.ty.values, rcond=None)[0]
    return {"conditions": cond, "mu": mu, "A": A, "explained": sv ** 2 / (sv ** 2).sum(),
            "wx": A.T @ bx[1:], "wy": A.T @ (null @ by[1:]), "ix": bx[0], "iy": by[0]}


def plane_coords(plane: dict, X: np.ndarray) -> np.ndarray:
    """Trials (or time points) by 2: position in the spatial plane, in mm."""
    Xc = X - plane["mu"]
    return np.stack([Xc @ plane["wx"] + plane["ix"], Xc @ plane["wy"] + plane["iy"]], axis=-1)


def plane_basis(plane: dict) -> np.ndarray:
    """Orthonormal basis (channels x 2) of the spatial plane."""
    q, _ = np.linalg.qr(np.stack([plane["wx"], plane["wy"]], axis=1))
    return q


def on_off(dev: np.ndarray, tx: np.ndarray, ty: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Split 2D deviations into the component along the target direction and the normal one."""
    r = np.hypot(tx, ty)
    ux, uy = tx / r, ty / r
    return dev[:, 0] * ux + dev[:, 1] * uy, -dev[:, 0] * uy + dev[:, 1] * ux


def deviations(values: np.ndarray, groups: np.ndarray) -> np.ndarray:
    """Each row minus the mean of its group."""
    df = pd.DataFrame(values)
    return (df - df.groupby(groups).transform("mean")).values


def svm_cv(X: np.ndarray, y: np.ndarray, seed: int, folds: int = 10) -> tuple[np.ndarray, np.ndarray]:
    """Out-of-fold predictions and per-fold accuracies of an RBF SVM (one-vs-one)."""
    pred = np.empty_like(y)
    acc = []
    for train, test in StratifiedKFold(folds, shuffle=True, random_state=seed).split(X, y):
        model = make_pipeline(StandardScaler(), SVC(kernel="rbf"))
        model.fit(X[train], y[train])
        pred[test] = model.predict(X[test])
        acc.append(np.mean(pred[test] == y[test]))
    return pred, np.array(acc)
