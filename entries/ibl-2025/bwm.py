"""Loading and measures for the IBL brain-wide map, dandiset 000409.

International Brain Laboratory et al. (2025), A brain-wide map of neural activity during complex
behaviour, Nature 645, 177-191, doi:10.1038/s41586-025-09235-0.

Each session has one processed NWB file (`desc-processed_behavior+ecephys.nwb`) with the trials
table, the spike-sorted units of all its probes, the electrode localisation in the Allen CCF (with
the Beryl and Cosmos groupings), the wheel, licks and, for most sessions, video pose estimates.
Files are streamed from the archive at the pinned version with remfile; nothing is written to disk.
h5py serialises its calls within a process, so files are read in parallel processes.

Where the parameters come from. "Methods" is the paper's Methods section; "code" is the paper's
repository https://github.com/int-brain-lab/paper-brain-wide-map at commit
118fc36cb3602934466ad2c6087c2b3b441f9f1f.

- Unit inclusion: a well-isolated unit passes all three IBL metrics (Methods; code `label == 1`,
  here `ibl_quality_score == 1`). A unit's region is the Beryl region of its peak channel (code,
  `atlas_id` of the cluster mapped to Beryl). Regions `void` and `root` are dropped; a region-session
  needs at least 5 units, a region at least 2 such sessions and 20 units (Methods; code
  `meta/inclusion_info.py`).
- Trial inclusion: trials with a missing stimulus onset, choice, block probability, feedback type
  or time, or first movement time are dropped, as are trials whose first movement time minus
  stimulus onset is outside 0.08 to 2 s (Methods). A session whose performance on 100% contrast
  trials is not above 90% is first truncated from the end until it is, keeping at least 400 trials
  (code `load_trials_and_mask`, `truncate_to_pass`).
- Windows: stimulus 0 to 0.1 s after stimulus onset, choice 0.1 s before the first movement, feedback
  0 to 0.2 s after feedback (Methods; code decoding settings).
- Decoding: L1 logistic regression (liblinear, tol 0.001, up to 20000 iterations, balanced class
  weights), nested 5 x 5 cross-validation with interleaved random folds, C from
  1e-5 to 10, balanced accuracy of the pooled test predictions (Methods). The paper repeats the
  cross-validation 10 times and uses 200 null sessions; here `N_RUNS` and `N_NULL` are smaller to fit
  the time limit, and each null session reuses the C chosen in each outer fold for the real labels
  (`decode`); `decode_nested_null` runs the full nested search for a null session, for comparison.
- Null sessions: stimulus side from pseudo-sessions drawn from the task's generative process
  (Methods: 90 unbiased trials with a fixed contrast set, then alternating 0.2/0.8 blocks whose
  lengths follow an exponential of scale 60 truncated to 20 to 100 trials, contrasts 1, 0.25, 0.125,
  0.0625 and 0 in the ratio 2:2:2:2:1). Choice and feedback from synthetic sessions: an
  action-kernel model fitted to each session (Methods give the prior update; the choice policy here
  is a logistic function of the signed contrast and the prior, a common choice, as the companion
  paper's model package is not used) simulated on pseudo-session stimuli.
- Single-cell tests: condition-combined Mann-Whitney test with 3000 permutations within individual
  blocks, combined with a simple Mann-Whitney test; a unit is selective when p < 0.001 (simple) and
  p < 0.05 (combined) (Methods; code `single_cell_stats`). Strata are the biased blocks crossed with
  choice (stimulus test) or with stimulus side (choice test); zero-contrast and unbiased-block trials
  are left out (code).
- Population trajectories: 12.5 ms bins with a 2 ms stride over 0 to 0.15 s after stimulus onset,
  trial-averaged per cell for left and right stimuli, distance sqrt(sum over cells of squared
  differences / number of cells) minus its minimum, null from 1000 permutations of stimulus side
  within trials of the same block and choice, latency the first time above 70% of the maximum that
  is also significant point-wise at 0.05, on the code's time axis linspace(0, 0.15, 72) (Methods and
  code `manifold/state_space_bwm.py`). The Methods permute within each block; the code merges the
  unbiased block with the 0.2 blocks (`traj_labels`). Regions are significant after
  Benjamini-Hochberg at q = 0.01 over regions (Methods); the code applies Benjamini-Yekutieli at
  0.05 (`by`).
"""

from __future__ import annotations

import os
import warnings
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import stats
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression

DANDISET_ID = "000409"
DANDISET_VERSION = "0.260309.1324"
API = "https://api.dandiarchive.org/api"

N_WORKERS = 8                  # processes streaming files at once
CHUNK_CACHE = 64 * 1024 ** 2   # the spike arrays are stored in 10 MB chunks

MIN_RT, MAX_RT = 0.08, 2.0
MIN_UNITS_SESSION, MIN_SESSIONS, MIN_UNITS_REGION = 5, 2, 20
WINDOWS = {  # event column, start, stop (s)
    "stim": ("stim_on", 0.0, 0.1),
    "choice": ("first_move", -0.1, 0.0),
    "feedback": ("feedback_time", 0.0, 0.2),
}
CLOCK_OFFSETS = np.round(np.arange(-1.0, 0.41, 0.2), 2)   # 0.2 s windows around feedback
C_GRID = np.array([1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0])
N_FOLDS = 5
N_RUNS = 1
N_NULL = 100
TRAJ_BIN, TRAJ_STRIDE, TRAJ_POST = 0.0125, 0.002, 0.15
TRAJ_SHIFTS = int(TRAJ_BIN // TRAJ_STRIDE)                 # 6, as in the code
TRAJ_NBINS = int(round(TRAJ_POST / TRAJ_BIN))              # 12
TRAJ_TIMES = np.linspace(0, TRAJ_POST, TRAJ_SHIFTS * TRAJ_NBINS)   # the code's time axis
TRAJ_POST_LONG = 0.2                                       # variant window, 0 to 0.2 s
TRAJ_TIMES_LONG = np.linspace(0, TRAJ_POST_LONG, TRAJ_SHIFTS * int(round(TRAJ_POST_LONG / TRAJ_BIN)))
N_PERM_TRAJ = 1000
Q_TRAJ = 0.01                  # Benjamini-Hochberg level over regions (Methods)
N_SHUF_CELL = 3000
ALPHA_MW, ALPHA_CCMW = 0.001, 0.05
PSTH_BIN, PSTH_POST = 0.005, 1.0


# --- assets and streaming -------------------------------------------------------------------

def list_assets() -> pd.DataFrame:
    """Every asset of the pinned version: path, asset id, size, subject, session and kind."""
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    rows = []
    for a in ds.get_assets():
        name = a.path.split("/")[-1]
        rows.append({"path": a.path, "asset_id": a.identifier, "size": a.size,
                     "subject": a.path.split("/")[0][4:],
                     "eid": name.split("_ses-")[1][:36] if "_ses-" in name else None,
                     "kind": ("processed" if "desc-processed" in name else "raw" if "desc-raw" in name
                              else name.rsplit("_", 1)[-1].replace(".mp4", ""))})
    return pd.DataFrame(rows)


def open_nwb(asset_id: str) -> h5py.File:
    url = f"{API}/assets/{asset_id}/download/"
    for _ in range(3):
        try:
            url = requests.head(url, allow_redirects=True, timeout=60).url.split("?")[0]
            break
        except requests.RequestException:
            continue
    return h5py.File(remfile.File(url), "r", rdcc_nbytes=CHUNK_CACHE, rdcc_nslots=10007)


def _str(x):
    v = x[()] if hasattr(x, "shape") else x
    return v.decode() if isinstance(v, bytes) else v


def _col(group, name):
    v = group[name][:]
    if v.dtype.kind in "OS":
        v = np.array([x.decode() if isinstance(x, bytes) else x for x in v])
    return v


def run_parallel(fn, items, workers=N_WORKERS):
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(fn, items))


def run_parallel_iter(fn, items, workers=N_WORKERS):
    """As run_parallel, but yields each result as it comes, so large results need not all be held."""
    with ProcessPoolExecutor(workers) as ex:
        yield from ex.map(fn, items)


# --- session metadata -----------------------------------------------------------------------

def scan_session(asset_id: str) -> dict:
    """Everything but the spikes: subject, trials, units with regions, probes and small streams."""
    with open_nwb(asset_id) as f:
        subj = f["general/subject"]
        info = {k: _str(subj[k]) for k in ("subject_id", "sex", "date_of_birth", "weight", "species")}
        info.update({k: _str(f[f"general/{k}"]) for k in ("lab", "institution", "protocol", "session_id")})
        info["session_start"] = _str(f["session_start_time"])
        info["revision"] = _str(f["general/ibl_metadata/revision"])
        info["units_description"] = _str(f["units"].attrs.get("description", ""))
        info["processing"] = sorted(f["processing"].keys())
        info_stim = [f"{g}/{k}" for g in ("presentation", "templates") for k in f[f"stimulus/{g}"].keys()]
        tr = f["intervals/trials"]
        trials = pd.DataFrame({k: _col(tr, k) for k in tr if k != "id"})
        u = f["units"]
        units = pd.DataFrame({k: _col(u, k) for k in (
            "ibl_quality_score", "max_electrode", "probe_name", "spike_count", "firing_rate",
            "median_spike_amplitude_uV", "noise_cutoff", "sliding_rp_violation")})
        idx = u["spike_times_index"][:]
        units["n_spikes_index"] = np.diff(np.r_[0, idx])
        loc = f["general/localization/ElectrodesIBLBregma"]
        entity = loc["localized_entity"][:]
        beryl = np.empty(len(entity), dtype=object)
        beryl[entity] = _col(loc, "beryl_location")
        loc_probe = np.empty(len(entity), dtype=object)
        loc_probe[entity] = _col(loc, "probe_name")
        units["region"] = beryl[units.max_electrode.values]
        units["region_probe"] = loc_probe[units.max_electrode.values]
        probes = {k: f["general/devices"][k].attrs.get("description", "") for k in f["general/devices"]}
        epochs = (pd.DataFrame({k: _col(f["intervals/epochs"], k) for k in ("start_time", "stop_time", "protocol_type")})
                  if "epochs" in f["intervals"] else pd.DataFrame({"protocol_type": ["none"]}))
        passive = None
        if "passive_protocol" in f["processing"]:
            pi = f["processing/passive_protocol/passive_intervals"]
            passive = list(_col(pi, "protocol_name"))
        licks = (f["processing/lick_times/EventsLickTimes/timestamps"][:]
                 if "lick_times" in f["processing"] else np.array([]))
        wheel_moves = (f["processing/wheel/WheelMovementIntervals/start_time"][:]
                       if "WheelMovementIntervals" in f["processing/wheel"] else np.array([]))
    return {"asset_id": asset_id, "info": info, "stimulus": ",".join(info_stim) or "empty",
            "trials": trials, "units": units, "probes": probes,
            "epochs": epochs, "passive": passive, "licks": licks, "wheel_moves": wheel_moves}


def task_table(trials: pd.DataFrame) -> pd.DataFrame:
    """The trials table in the paper's terms.

    side: +1 stimulus on the right, -1 on the left. choice: +1 for the response that is rewarded when
    the stimulus is on the right (counter-clockwise, which the table says moves the stimulus left,
    towards the centre), -1 for clockwise, 0 for no response. contrast as a fraction.
    """
    t = pd.DataFrame({
        "stim_on": trials.gabor_stimulus_onset_time.values,
        "go_cue": trials.auditory_cue_time.values,
        "first_move": trials.wheel_movement_onset_time.values,
        "feedback_time": trials.feedback_time.values,
        "contrast": trials.gabor_stimulus_contrast.values / 100.0,
        "side": np.where(trials.gabor_stimulus_side.values == "right", 1, -1),
        "choice": trials.mouse_wheel_choice.map({"counter_clockwise": 1, "clockwise": -1, "none": 0}).values,
        "correct": trials.is_mouse_rewarded.values.astype(bool),
        "p_left": trials.probability_left.values,
        "block": trials.block_index.values,
        "reward_ul": trials.reward_volume_uL.values,
    })
    t["signed_contrast"] = t.side * t.contrast
    t["rt"] = t.first_move - t.stim_on
    return t


def perf_easy(t: pd.DataFrame) -> float:
    easy = t.contrast >= 0.5
    return float(t.correct[easy].mean()) if easy.any() else np.nan


def analysis_mask(t: pd.DataFrame) -> tuple[np.ndarray, int]:
    """Trials the paper analyses, and the number of trials kept after truncation.

    A session that does not pass even at 400 trials is excluded (no trial kept), as the code's
    `load_trials_and_mask` raises an error for it.
    """
    n = len(t)
    good = lambda k: k >= 400 and perf_easy(t.iloc[:k]) > 0.9
    while not good(n) and n > 400:
        n -= 1
    keep = np.zeros(len(t), bool)
    keep[:n] = good(n)
    ok = (keep & t.stim_on.notna() & t.first_move.notna() & t.feedback_time.notna()
          & t.p_left.notna() & (t.choice != 0) & (t.rt >= MIN_RT) & (t.rt <= MAX_RT))
    return ok.values, n


def canonical_units(scans: list[dict]) -> pd.DataFrame:
    """Well-isolated units in the canonical regions, with the counts at each inclusion step."""
    rows = []
    for s in scans:
        u = s["units"]
        rows.append(pd.DataFrame({"eid": s["info"]["session_id"], "asset_id": s["asset_id"],
                                  "unit": np.arange(len(u)), "region": u.region.values,
                                  "good": u.ibl_quality_score.values == 1}))
    allu = pd.concat(rows, ignore_index=True)
    steps = [("all units", allu)]
    g = allu[allu.good]
    steps.append(("well-isolated", g))
    g = g[~g.region.isin(["void", "root"])]
    steps.append(("grey matter", g))
    n = g.groupby(["region", "eid"]).unit.transform("size")
    g = g[n >= MIN_UNITS_SESSION]
    steps.append((f">= {MIN_UNITS_SESSION} per session", g))
    ns = g.groupby("region").eid.transform("nunique")
    g = g[ns >= MIN_SESSIONS]
    steps.append((f">= {MIN_SESSIONS} sessions", g))
    nr = g.groupby("region").unit.transform("size")
    g = g[nr >= MIN_UNITS_REGION]
    steps.append((f">= {MIN_UNITS_REGION} per region", g))
    table = pd.DataFrame([{"step": k, "sessions": v.eid.nunique(), "units": len(v),
                           "regions": v.region.nunique()} for k, v in steps])
    return g.reset_index(drop=True), table


# --- spikes -----------------------------------------------------------------------------------

def window_counts(st: np.ndarray, starts: np.ndarray, width: float) -> np.ndarray:
    """Spikes of a sorted spike train in [start, start + width) for each start (any shape)."""
    s = np.asarray(starts, float)
    out = np.searchsorted(st, s + width) - np.searchsorted(st, s)
    out[~np.isfinite(s)] = 0
    return out


def traj_starts(events: np.ndarray, n_points: int = TRAJ_TIMES.size) -> np.ndarray:
    """Start of each overlapping trajectory bin, in the code's order (trials x 72 for 0 to 0.15 s).

    The first 72 of the 96 points of the 0 to 0.2 s window are the 72 points of the 0 to 0.15 s window.
    """
    j = np.arange(n_points)
    return events[:, None] + (j // TRAJ_SHIFTS) * TRAJ_BIN + (j % TRAJ_SHIFTS) * TRAJ_STRIDE


def extract_session(job: tuple) -> dict:
    """Stream the spikes of the requested units of one session and reduce them to counts.

    job = (asset_id, unit indices, which of them need trajectory bins, which need feedback PSTHs).
    Returns the trials table with the analysis mask, counts in the analysis windows (trials x units),
    trajectory bins over 0 to 0.2 s (trials x units x 96, uint8; the first 72 points are the 0 to
    0.15 s window), and per unit the mean feedback PSTH on correct and
    incorrect analysed trials (units x 2 x bins, spikes/s).
    """
    asset_id, units, traj_units, psth_units = job
    with open_nwb(asset_id) as f:
        t = task_table(pd.DataFrame({k: _col(f["intervals/trials"], k)
                                     for k in f["intervals/trials"] if k != "id"}))
        mask, n_kept = analysis_mask(t)
        t["analysed"] = mask
        u = f["units"]
        idx = u["spike_times_index"][:]
        start = np.r_[0, idx[:-1]]
        st_all = u["spike_times"]
        order = np.argsort(start[units])
        trains, unsorted = {}, 0
        for i in np.asarray(units)[order]:
            st = st_all[start[i]:idx[i]]
            if np.any(np.diff(st) < 0):
                unsorted += 1
                st = np.sort(st)
            trains[i] = st
    counts = {}
    for var, (col, a, b) in WINDOWS.items():
        ev = t[col].values
        counts[var] = np.stack([window_counts(trains[i], ev + a, b - a) for i in units], axis=1)
    fb = t.feedback_time.values
    traj = None
    if len(traj_units):
        s = traj_starts(t.stim_on.values, TRAJ_TIMES_LONG.size)
        traj = np.stack([window_counts(trains[i], s, TRAJ_BIN) for i in traj_units], axis=1).astype(np.uint8)
    psth = None
    if len(psth_units):
        edges = fb[:, None] + np.arange(0, PSTH_POST, PSTH_BIN)[None, :]
        sel = {True: mask & t.correct.values, False: mask & ~t.correct.values}
        psth = np.stack([np.stack([window_counts(trains[i], edges[sel[c]], PSTH_BIN).mean(0) / PSTH_BIN
                                   for c in (True, False)]) for i in psth_units])
    return {"asset_id": asset_id, "trials": t, "n_kept": n_kept, "units": np.asarray(units),
            "counts": counts, "traj_units": np.asarray(traj_units), "traj": traj,
            "psth_units": np.asarray(psth_units), "psth": psth, "unsorted_units": unsorted,
            "n_spikes": int(sum(len(v) for v in trains.values()))}


# --- null sessions -----------------------------------------------------------------------------

CONTRASTS = np.array([1.0, 0.25, 0.125, 0.0625, 0.0])
CONTRAST_P = np.array([2, 2, 2, 2, 1]) / 9


def block_length(rng) -> int:
    while True:
        x = int(rng.exponential(60))
        if 20 <= x <= 100:
            return x


def pseudo_session(n: int, rng) -> pd.DataFrame:
    """Stimuli of one session drawn from the task's generative process (Methods)."""
    first = np.r_[np.repeat(CONTRASTS[:4], 10), -np.repeat(CONTRASTS[:4], 10), np.zeros(10)]
    first = rng.permutation(first)
    side = np.sign(first)
    side[side == 0] = rng.choice([-1, 1], size=(side == 0).sum())
    contrast = np.abs(first)
    p_left = np.full(90, 0.5)
    pl = rng.choice([0.2, 0.8])
    while len(p_left) < n:
        p_left = np.r_[p_left, np.full(block_length(rng), pl)]
        pl = 1 - pl
    p_left = p_left[:n]
    k = n - 90
    if k > 0:
        s2 = np.where(rng.random(k) < p_left[90:], -1, 1)
        c2 = rng.choice(CONTRASTS, size=k, p=CONTRAST_P)
        side = np.r_[side, s2]
        contrast = np.r_[contrast, c2]
    side, contrast = side[:n].astype(int), contrast[:n]
    return pd.DataFrame({"side": side, "contrast": contrast, "signed_contrast": side * contrast,
                         "p_left": p_left})


def _contrast_term(signed_contrast):
    return np.tanh(5 * signed_contrast) / np.tanh(5)


def _prior(actions, alpha):
    """Action-kernel prior that the next stimulus is on the right (Methods' update rule)."""
    pi = np.empty(len(actions))
    p = 0.5
    for i, a in enumerate(actions):
        pi[i] = p
        if a != 0:
            p = (1 - alpha) * p + alpha * (a > 0)
    return pi


def fit_action_kernel(t: pd.DataFrame) -> dict:
    """Learning rate and choice policy of the action-kernel model, by maximum likelihood."""
    best = None
    resp = t.choice.values != 0
    for alpha in (0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.7):
        pi = _prior(t.choice.values, alpha)
        X = np.c_[_contrast_term(t.signed_contrast.values), pi - 0.5][resp]
        y = (t.choice.values[resp] > 0).astype(int)
        m = LogisticRegression(C=1e4, max_iter=1000).fit(X, y)
        p = np.clip(m.predict_proba(X)[:, 1], 1e-9, 1 - 1e-9)
        ll = np.sum(y * np.log(p) + (1 - y) * np.log(1 - p))
        if best is None or ll > best["ll"]:
            best = {"alpha": alpha, "b0": m.intercept_[0], "b": m.coef_[0].copy(), "ll": ll}
    return best


def synthetic_session(model: dict, n: int, rng) -> pd.DataFrame:
    """Pseudo-session stimuli with choices simulated from the fitted action-kernel model."""
    ps = pseudo_session(n, rng)
    p, choice = 0.5, np.empty(n, int)
    x = _contrast_term(ps.signed_contrast.values)
    for i in range(n):
        z = model["b0"] + model["b"][0] * x[i] + model["b"][1] * (p - 0.5)
        a = 1 if rng.random() < 1 / (1 + np.exp(-z)) else -1
        choice[i] = a
        p = (1 - model["alpha"]) * p + model["alpha"] * (a > 0)
    ps["choice"] = choice
    ps["correct"] = choice == ps.side.values
    return ps


# --- decoding -------------------------------------------------------------------------------

def _logreg(C):
    return LogisticRegression(C=C, l1_ratio=1.0, solver="liblinear", tol=1e-3, max_iter=20000,
                              class_weight="balanced", random_state=0)


def balanced_accuracy(y, p) -> float:
    return 0.5 * (np.mean(p[y == 1] == 1) + np.mean(p[y == 0] == 0))


def _folds(n, rng, y=None, k=N_FOLDS):
    """Interleaved random folds; redrawn until every training set holds both classes."""
    for _ in range(100):
        f = rng.permutation(np.arange(n) % k)
        if y is None or all(len(np.unique(y[f != i])) == 2 for i in range(k)):
            return f
    raise RuntimeError("could not draw folds with both classes in training")


FITS = {"fits": 0, "not_converged": 0}   # per process; reset and reported by each job


def _fit_predict(Xtr, ytr, Xte, C):
    if len(np.unique(ytr)) < 2:
        return np.full(len(Xte), ytr[0])
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", ConvergenceWarning)
        m = _logreg(C).fit(Xtr, ytr)
    FITS["fits"] += 1
    FITS["not_converged"] += any(issubclass(w.category, ConvergenceWarning) for w in caught)
    return m.predict(Xte)


def _choose_C(X, y, rng):
    inner = _folds(len(y), rng, y)
    score = np.zeros(len(C_GRID))
    for i in range(N_FOLDS):
        tr, va = inner != i, inner == i
        for k, C in enumerate(C_GRID):
            score[k] += balanced_accuracy(y[va], _fit_predict(X[tr], y[tr], X[va], C))
    return C_GRID[int(np.argmax(score))]


def decode(X: np.ndarray, y: np.ndarray, null_ys: list, seed: int) -> dict:
    """Nested cross-validated decoding of y, and of each null target with the outer folds' C."""
    rng = np.random.default_rng(seed)
    X = np.asarray(X, float)
    scores, null = [], np.zeros((N_RUNS, len(null_ys)))
    for run in range(N_RUNS):
        outer = _folds(len(y), rng, y)
        pred = np.zeros(len(y))
        chosen = []
        for i in range(N_FOLDS):
            tr, te = outer != i, outer == i
            C = _choose_C(X[tr], y[tr], rng)
            chosen.append(C)
            pred[te] = _fit_predict(X[tr], y[tr], X[te], C)
        scores.append(balanced_accuracy(y, pred))
        for j, yn in enumerate(null_ys):
            outer_n = _folds(len(yn), rng, yn)
            pn = np.zeros(len(yn))
            for i in range(N_FOLDS):
                tr, te = outer_n != i, outer_n == i
                pn[te] = _fit_predict(X[tr], yn[tr], X[te], chosen[i])
            null[run, j] = balanced_accuracy(yn, pn)
    score, null = float(np.mean(scores)), null.mean(0)
    return {"score": score, "null": null, "p": (1 + np.sum(null >= score)) / (1 + len(null)),
            "corrected": score - float(np.median(null)) if len(null) else np.nan}


def decode_nested_null(X, y, seed) -> float:
    """Balanced accuracy with the full nested search, for one target (a null target, say)."""
    rng = np.random.default_rng(seed)
    X = np.asarray(X, float)
    outer = _folds(len(y), rng, y)
    pred = np.zeros(len(y))
    for i in range(N_FOLDS):
        tr, te = outer != i, outer == i
        pred[te] = _fit_predict(X[tr], y[tr], X[te], _choose_C(X[tr], y[tr], rng))
    return balanced_accuracy(y, pred)


def decoding_targets(t: pd.DataFrame, var: str, sessions: list | None = None):
    """Analysed-trial rows used, the binary target, and the same target in each null session."""
    m = t.analysed.values
    if var == "stim":
        rows = m & (t.contrast.values > 0)
        y = (t.side.values[rows] > 0).astype(int)
        nulls = [(s.side.values[rows] > 0).astype(int) for s in sessions or []]
    elif var == "choice":
        rows = m
        y = (t.choice.values[rows] > 0).astype(int)
        nulls = [(s.choice.values[rows] > 0).astype(int) for s in sessions or []]
    else:
        rows = m
        y = t.correct.values[rows].astype(int)
        nulls = [s.correct.values[rows].astype(int) for s in sessions or []]
    return rows, y, nulls


def decode_job(job: tuple) -> dict:
    """One region-session: decode stimulus, choice and feedback against their null sessions."""
    key, t, counts, seed = job
    FITS.update(fits=0, not_converged=0)
    rng = np.random.default_rng(seed)
    n = len(t)
    model = fit_action_kernel(t[t.analysed])
    pseudo = [pseudo_session(n, rng) for _ in range(N_NULL)]
    synth = [synthetic_session(model, n, rng) for _ in range(N_NULL)]
    out = {"key": key, "alpha": model["alpha"]}
    for k, var in enumerate(("stim", "choice", "feedback")):
        rows, y, nulls = decoding_targets(t, var, pseudo if var == "stim" else synth)
        nulls = [yn for yn in nulls if len(np.unique(yn)) == 2 and min(np.bincount(yn)) >= N_FOLDS]
        res = decode(counts[var][rows], y, nulls, seed + k + 1)
        out[var] = {"n_trials": int(rows.sum()), "n_minor": int(min(np.bincount(y, minlength=2))),
                    "n_null": len(nulls), **res}
    out["fits"], out["not_converged"] = FITS["fits"], FITS["not_converged"]
    return out


def nested_null_job(job: tuple) -> dict:
    """For one region-session, null scores with the full nested search and with the reused C."""
    key, t, counts, seed, n_null = job
    rng = np.random.default_rng(seed)
    model = fit_action_kernel(t[t.analysed])
    pseudo = [pseudo_session(len(t), rng) for _ in range(n_null)]
    synth = [synthetic_session(model, len(t), rng) for _ in range(n_null)]
    out = {"key": key}
    for k, var in enumerate(("stim", "choice", "feedback")):
        rows, y, nulls = decoding_targets(t, var, pseudo if var == "stim" else synth)
        nulls = [yn for yn in nulls if len(np.unique(yn)) == 2 and min(np.bincount(yn)) >= N_FOLDS]
        X = counts[var][rows]
        out[var] = {"nested": np.array([decode_nested_null(X, yn, seed + 10 * k + j) for j, yn in enumerate(nulls)]),
                    "reused": decode(X, y, nulls, seed + k)["null"]}
    return out


def nested_p_job(job: tuple) -> dict:
    """Stimulus nulls of one region-session decoded with the full nested search of C.

    job = (key, trials, counts, seed, score, n_null), with the seed of `decode_job`, so that the
    null sessions are the first n_null of the pseudo-sessions `decode_job` used; score is the real
    labels' score there.
    """
    key, t, counts, seed, score, n_null = job
    rng = np.random.default_rng(seed)
    pseudo = [pseudo_session(len(t), rng) for _ in range(N_NULL)]
    rows, y, nulls = decoding_targets(t, "stim", pseudo)
    nulls = [yn for yn in nulls if len(np.unique(yn)) == 2 and min(np.bincount(yn)) >= N_FOLDS][:n_null]
    X = counts["stim"][rows]
    null = np.array([decode_nested_null(X, yn, seed + 100 + j) for j, yn in enumerate(nulls)])
    return {"key": key, "null": null, "p": (1 + np.sum(null >= score)) / (1 + len(null))}


def clock_job(job: tuple) -> dict:
    """Feedback decoded from 0.2 s windows at offsets around feedback, and with labels one trial off."""
    key, t, clock, seed = job
    rng = np.random.default_rng(seed)
    m = t.analysed.values
    y = t.correct.values[m].astype(int)
    X = clock[m].astype(float)
    if min(np.bincount(y, minlength=2)) < N_FOLDS or X.shape[1] == 0:
        return {"key": key, "acc": np.full(len(CLOCK_OFFSETS), np.nan), "shifted": np.nan}

    def cv(Xk, yk):
        f = _folds(len(yk), rng, yk)
        pred = np.zeros(len(yk))
        for i in range(N_FOLDS):
            pred[f == i] = _fit_predict(Xk[f != i], yk[f != i], Xk[f == i], 1.0)
        return balanced_accuracy(yk, pred)

    acc = np.array([cv(X[:, :, j], y) for j in range(len(CLOCK_OFFSETS))])
    j0 = int(np.where(CLOCK_OFFSETS == 0)[0][0])
    shifted = cv(X[1:, :, j0], y[:-1])
    return {"key": key, "acc": acc, "shifted": shifted}


def fisher_p(p) -> float:
    p = np.asarray(p, float)
    return float(stats.chi2.sf(-2 * np.sum(np.log(p)), 2 * len(p)))


def bh(p, q) -> np.ndarray:
    """Benjamini-Hochberg: which p-values are significant at false discovery rate q."""
    p = np.asarray(p, float)
    order = np.argsort(p)
    thresh = q * np.arange(1, len(p) + 1) / len(p)
    passed = p[order] <= thresh
    k = np.max(np.where(passed)[0]) + 1 if passed.any() else 0
    sig = np.zeros(len(p), bool)
    sig[order[:k]] = True
    return sig


def by(p, q) -> np.ndarray:
    """Benjamini-Yekutieli, the correction of the code's trajectory analysis (`fdr_by`)."""
    m = len(p)
    return bh(p, q / np.sum(1.0 / np.arange(1, m + 1)))


# --- single cells -----------------------------------------------------------------------------

def ccmw_p(counts: np.ndarray, label: np.ndarray, strata: np.ndarray, blocks: np.ndarray,
           n_shuf: int, rng) -> np.ndarray:
    """Condition-combined Mann-Whitney p-value per unit, permuting within individual blocks.

    counts: trials x units; label: 1 (x), 0 (y) or -1 (left out); strata: condition per trial.
    Follows Time_TwoNmannWhitneyUshuf and the stimulus, choice and feedback scripts of the code.
    """
    n_units = counts.shape[1]
    num = np.zeros((n_shuf + 1, n_units))
    den = 0.0
    for s in np.unique(strata[label >= 0]):
        idx = np.where((strata == s) & (label >= 0))[0]
        lab = label[idx]
        nx, ny = int((lab == 1).sum()), int((lab == 0).sum())
        if nx == 0 or ny == 0:
            continue
        ranks = stats.rankdata(counts[idx], axis=0)
        b = blocks[idx]
        shared = np.intersect1d(b[lab == 1], b[lab == 0])
        sx = np.empty((n_shuf + 1, len(idx)))
        sy = np.empty((n_shuf + 1, len(idx)))
        sx[0] = sy[0] = lab
        for tgt in (sx, sy):
            tgt[1:] = lab
            for blk in shared:
                j = np.where(b == blk)[0]
                tgt[1:, j] = rng.permuted(np.tile(lab[j], (n_shuf, 1)), axis=1)
        ux = sx @ ranks - nx * (nx + 1) / 2
        uy = (1 - sy) @ ranks - ny * (ny + 1) / 2
        num += np.minimum(ux, uy)
        den += nx * ny
    if den == 0:
        return np.full(n_units, np.nan)
    cp = num / den
    return np.array([stats.rankdata(cp[:, k])[0] / (1 + n_shuf) for k in range(n_units)])


def simple_mw_p(counts, label) -> np.ndarray:
    x, y = counts[label == 1], counts[label == 0]
    out = np.ones(counts.shape[1])
    for k in range(counts.shape[1]):
        if np.ptp(np.r_[x[:, k], y[:, k]]) > 0:
            out[k] = stats.mannwhitneyu(x[:, k], y[:, k], alternative="two-sided").pvalue
    return out


def single_cell_design(t: pd.DataFrame, var: str, side=None, choice=None, p_left=None):
    """Label, strata and blocks of the code's test for stimulus side or choice.

    Analysed trials of the biased blocks with a visible stimulus. Stimulus: label is left stimulus,
    strata are block x choice. Choice: label is the code's choice 1 (here -1, clockwise), strata are
    block x stimulus side. Other side, choice or p_left (a null session) can be passed in.
    """
    side = t.side.values if side is None else side
    choice = t.choice.values if choice is None else choice
    p_left = t.p_left.values if p_left is None else p_left
    use = t.analysed.values & (t.contrast.values > 0) & (p_left != 0.5)
    if var == "stim":
        label = np.where(use, (side < 0).astype(int), -1)
        strata = np.where(p_left == 0.8, 0, 2) + (choice > 0)
    else:
        label = np.where(use, (choice < 0).astype(int), -1)
        strata = np.where(p_left == 0.8, 0, 2) + (side > 0)
    blocks = np.r_[0, np.cumsum(np.abs(np.diff(p_left)) > 0)]
    return label, strata, blocks


def single_cell_job(job: tuple) -> dict:
    """Selectivity of each unit of one region-session to stimulus side and choice, with two null runs.

    `null`: a pseudo-session (stimulus) or synthetic session (choice); `shuf`: the real label
    permuted over the tested trials. The shuffle run has its own generator, so the real and null
    runs give what they gave without it.
    """
    key, t, counts, seed = job
    rng = np.random.default_rng(seed)
    rng_shuf = np.random.default_rng([seed, 1])
    model = fit_action_kernel(t[t.analysed])
    ps = pseudo_session(len(t), rng)
    syn = synthetic_session(model, len(t), rng)
    out = {"key": key}
    use = t.analysed.values & (t.contrast.values > 0) & (t.p_left.values != 0.5)
    for var in ("stim", "choice"):
        c = counts[var]
        col = "side" if var == "stim" else "choice"
        shuffled = t[col].values.copy()
        shuffled[use] = rng_shuf.permutation(shuffled[use])
        for name, kw, g in (("real", {}, rng),
                            ("null", {"side": ps.side.values, "p_left": ps.p_left.values} if var == "stim"
                             else {"choice": syn.choice.values}, rng),
                            ("shuf", {col: shuffled}, rng_shuf)):
            label, strata, blocks = single_cell_design(t, var, **kw)
            p_cc = ccmw_p(c, label, strata, blocks, N_SHUF_CELL, g)
            p_mw = simple_mw_p(c[label >= 0], label[label >= 0])
            out[f"{var}_{name}"] = (p_mw < ALPHA_MW) & (p_cc < ALPHA_CCMW)
            out[f"{var}_{name}_mw"] = p_mw < ALPHA_MW
            out[f"{var}_{name}_cc"] = p_cc < ALPHA_CCMW
    return out


# --- population trajectories ------------------------------------------------------------------

def traj_labels(side, block, choice, n_perm: int, rng) -> np.ndarray:
    """Left-stimulus indicator of the trials (row 0) and n_perm permutations of it within block x choice.

    block: p_left, so that each of the 0.2, 0.5 and 0.8 blocks is a class (Methods), or p_left == 0.8,
    which merges the unbiased block with the 0.2 blocks as the code's `get_d_vars` does.
    """
    n = len(side)
    labels = np.empty((n_perm + 1, n), np.float32)
    labels[0] = side < 0
    groups = [np.where((block == b) & (choice == c))[0] for b in np.unique(block) for c in (-1, 1)]
    for k in range(1, n_perm + 1):
        lab = labels[0].copy()
        for g in groups:
            lab[g] = lab[rng.permutation(g)]
        labels[k] = lab
    return labels


def traj_sq(bins: np.ndarray, labels: np.ndarray) -> np.ndarray:
    """Sum over the cells of one session of the squared left minus right mean rate, per label row and time."""
    n, u, nt = bins.shape
    X = bins.reshape(n, u * nt).astype(np.float32) / TRAJ_BIN
    nl = labels.sum(1, keepdims=True)
    mean_l = (labels / nl) @ X
    mean_r = ((1 - labels) / (n - nl)) @ X
    d = (mean_l - mean_r).reshape(len(labels), u, nt)
    return np.sum(d.astype(np.float64) ** 2, axis=1)


def traj_stats(sq: np.ndarray, n_cells: int, times: np.ndarray = TRAJ_TIMES) -> dict:
    """Distance, amplitude, permutation p and latencies from the summed squares of a region."""
    dist = np.sqrt(sq / n_cells)
    M = dist - dist.min(1, keepdims=True)
    amp = M.max(1) - M.min(1)
    ps = np.mean(M >= M[0], axis=0)
    ups = np.where(M[0] > 0.7 * M[0].max())[0]
    sig_ups = ups[ps[ups] < 0.05]
    # The code's canonical window: the first 48 points of the curve with the full window's baseline
    # subtracted, on the axis linspace(0, 0.1, 48) (code `d_var_stacked`).
    Mc = M[:, :48]
    psc = np.mean(Mc >= Mc[0], axis=0)
    upc = np.where(Mc[0] > 0.7 * Mc[0].max())[0]
    sig_c = upc[psc[upc] < 0.05]
    return {"n_cells": n_cells, "d": M[0], "amp": float(amp[0]), "p": float(np.mean(amp >= amp[0])),
            "latency": float(times[sig_ups[0]]) if len(sig_ups) else np.nan,
            "latency_70": float(times[ups[0]]),
            "latency_70_bin_start": float(traj_starts(np.zeros(1), len(times))[0, ups[0]]),
            "latency_canonical": float(np.linspace(0, 0.1, 48)[sig_c[0]]) if len(sig_c) else np.nan}


def trajectory(sessions: list, n_perm: int, rng, times: np.ndarray = TRAJ_TIMES) -> dict:
    """Stimulus trajectory distance of one region pooled over sessions, with its permutation null.

    sessions: list of (traj bins trials x units x len(times), side, p_left, choice) over analysed trials.
    """
    sq = np.zeros((n_perm + 1, times.size))
    n_cells = 0
    for bins, side, p_left, choice in sessions:
        sq += traj_sq(bins, traj_labels(side, p_left, choice, n_perm, rng))
        n_cells += bins.shape[1]
    return traj_stats(sq, n_cells, times)


def region_traj_job(job: tuple) -> dict:
    """Stimulus trajectory sums of every canonical region of one session, and the clock check.

    job = (asset_id, unit indices, their regions, seed). One set of permutations per session is
    shared by its regions. Returns per region the summed squares (permutations + 1 x 72, float32)
    with the Methods' permutation classes (`sq`) and with the code's (`sq_code`), the number of
    cells, and the feedback decoding of `clock_job` on all the units given.
    """
    asset_id, units, regions, seed = job
    rng = np.random.default_rng(seed)
    with open_nwb(asset_id) as f:
        t = task_table(pd.DataFrame({k: _col(f["intervals/trials"], k)
                                     for k in f["intervals/trials"] if k != "id"}))
        t["analysed"] = analysis_mask(t)[0]
        u = f["units"]
        idx = u["spike_times_index"][:]
        start = np.r_[0, idx[:-1]]
        st_all = u["spike_times"]
        trains = {}
        for i in np.asarray(units)[np.argsort(start[units])]:
            trains[i] = np.sort(st_all[start[i]:idx[i]])
    a = t.analysed.values
    out = {"asset_id": asset_id, "n_analysed": int(a.sum()), "sq": {}, "sq_code": {}, "n": {}}
    fb = t.feedback_time.values
    clock = np.stack([window_counts(trains[i], fb[:, None] + CLOCK_OFFSETS[None, :], 0.2) for i in units], axis=1)
    out["clock"] = clock_job((asset_id, t, clock, seed))
    if not a.any():
        return out
    s = traj_starts(t.stim_on.values[a])
    labels = traj_labels(t.side.values[a], t.p_left.values[a], t.choice.values[a], N_PERM_TRAJ, rng)
    labels_code = traj_labels(t.side.values[a], t.p_left.values[a] == 0.8, t.choice.values[a], N_PERM_TRAJ, rng)
    regions = np.asarray(regions)
    for r in np.unique(regions):
        sel = np.asarray(units)[regions == r]
        bins = np.stack([window_counts(trains[i], s, TRAJ_BIN) for i in sel], axis=1)
        out["sq"][r] = traj_sq(bins, labels).astype(np.float32)
        out["sq_code"][r] = traj_sq(bins, labels_code).astype(np.float32)
        out["n"][r] = len(sel)
    return out


# --- behaviour --------------------------------------------------------------------------------

def spectrum_peak(x: np.ndarray, dt: float, fmin=4.0, fmax=20.0, pad=4096):
    """Peak frequency and power of a detrended, Hann-windowed signal within [fmin, fmax]."""
    x = np.asarray(x, float)
    x = x - np.polyval(np.polyfit(np.arange(len(x)), x, 1), np.arange(len(x)))
    p = np.abs(np.fft.rfft(x * np.hanning(len(x)), n=pad)) ** 2
    f = np.fft.rfftfreq(pad, dt)
    band = (f >= fmin) & (f <= fmax)
    k = np.argmax(p[band])
    return float(f[band][k]), p, f


def thread_limits():
    """One linear-algebra thread per process: many small fits run in parallel processes."""
    for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[v] = "1"
