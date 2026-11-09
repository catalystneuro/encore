"""Loading and measures for the ALM recordings of dandiset 000006.

Economo, Viswanathan, Tasic et al. (2018), Nature, doi:10.1038/s41586-018-0642-9.

Each NWB file (NWB 2.0.2) holds one session of one mouse in a delayed response task: a trial
table (`start_time` in seconds on the session clock; `pole_in_time`, `pole_out_time` and
`cue_start_time` in seconds from the trial start; `type` lick left or lick right; `response`
correct, incorrect, early lick or no response; `is_good`; `stim_present`), the times of left and
right licks, and a units table with spike times. Tagged pyramidal tract units have ids above 1000
and `cell_type` PTupper or PTlower; the other units are `unidentified`. Files are streamed from
the archive at the pinned version; nothing is written to disk.

Where the parameters come from. The claims file (claims/000006/10.1038-s41586-018-0642-9.yaml)
fixes every method; its opening comment and criteria cite the Methods, the figure legends and the
paper's MATLAB code, Ephys.zip of the Figshare record doi:10.25378/janelia.7007846 (version 1).

- `EPOCHS`, in seconds from the go cue: the code's epochs (defineDataset.m), as the claims file
  gives them. Epoch means take bins with centres in (start, end] (getData); coding direction
  windows take [start, end) (DirectionVector). On the 5 ms grid used here no bin centre falls on
  a boundary, so both give the same bins.
- `GOOD_QUALITY`, `MIN_CORRECT`, `MIN_SPIKES_PER_TRIAL`, `MIN_PERFORMANCE` and `EDGE_TRIALS`: the
  code's per-unit inclusion rule and trial range (loadAndProcessData.m), reading (a) of the
  claims file's unit inclusion and of the trial range, which the claims file settles as the ones
  the claims use. `session_rule` is reading (b), the Methods' session rule, a variant.
- `DT` and `SMOOTH`: 5 ms bins and a causal 50 ms boxcar (Methods; MySmooth with sm = 19 keeps
  the current bin and the nine before). `TIME` is the bin grid of the paper's processed data
  files, which the code reads (bin centres from -3.3975 to 2.9975 s around the go cue); it is a
  standard choice of grid, and only its 5 ms step comes from the paper.
- `CD_WINDOWS`, `N_BOOT` and `BOOT_TRIALS`: the coding directions and the hierarchical bootstrap
  (Methods; Projections.m), as the claims file gives them.
- `SELECTIVITY_P`: the two-sided Mann-Whitney test at p < 0.01 (Results; simplePlots.m).
- `BURST_ISI` and `BURST_FRACTION`: Extended Data Fig. 5c legend (showISIHists).

Two things are built from the files because the files do not store them. Trials are taken on
the file's clock: a trial's spikes are the spikes from 3.4 s before its go cue to 3.0 s after
(the grid), and its licks are the licks after its go cue and before the next trial's pole comes
in. The data check shows where this differs from the paper's processed data.
"""

from __future__ import annotations

import io
import zipfile
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
import scipy.io as sio
import scipy.sparse as sp
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "000006"
DANDISET_VERSION = "0.220126.1855"

EPOCHS = {                      # seconds from the go cue, defineDataset.m
    "baseline": (-3.1, -2.7),
    "sample": (-2.5, -2.1),
    "delay": (-1.3, 0.0),
    "late delay": (-0.4, 0.0),
    "response": (0.0, 0.4),
}
GOOD_QUALITY = {"Excellent", "Good", "single"}
MIN_CORRECT = 50                # more than this many correct trials of each direction
MIN_SPIKES_PER_TRIAL = 3.2
MIN_PERFORMANCE = 0.65          # fraction correct, each direction
EDGE_TRIALS = 10                # trials dropped at each end of a unit's range
SELECTIVITY_P = 0.01
TYPES = ("PTupper", "PTlower")
PROJECTION = {"PTupper": "thalamus-projecting", "PTlower": "medulla-projecting"}

DT = 0.005
TIME = np.round(-3.3975 + DT * np.arange(1280), 4)
SMOOTH = 10
CD_WINDOWS = {"early": (-2.5, -2.1), "late": (-0.4, 0.0), "go": (0.0, 0.4)}
N_BOOT = 1000
BOOT_TRIALS = 50
BURST_ISI = 0.005
BURST_FRACTION = 0.1
# defineDataset.m: group 1 ("MP", medulla-projecting) holds these animals, group 2 ("TP") the rest
MP_ANIMALS = ("anm369962", "anm369963", "anm369964", "anm372794")


# ----------------------------------------------------------------------------------------------
# Loading

def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def dandiset_metadata() -> dict:
    with DandiAPIClient() as client:
        return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_raw_metadata()


def _text(value) -> str:
    if isinstance(value, bytes):
        return value.decode()
    if isinstance(value, np.ndarray):
        return _text(value[()]) if value.shape == () else str(value)
    return str(value)


def load_session(path: str, url: str) -> dict:
    """Read one file: trials, licks and every unit with its spike times."""
    with h5py.File(remfile.File(url), "r") as f:
        tr = f["intervals/trials"]
        trials = pd.DataFrame({
            "start": tr["start_time"][()], "stop": tr["stop_time"][()],
            "pole_in": tr["pole_in_time"][()], "pole_out": tr["pole_out_time"][()],
            "cue": tr["cue_start_time"][()],
            "type": [_text(v) for v in tr["type"][()]],
            "response": [_text(v) for v in tr["response"][()]],
            "is_good": tr["is_good"][()].astype(bool),
            "stim": tr["stim_present"][()].astype(bool),
        })
        trials["cue_abs"] = trials.start + trials.cue
        u = f["units"]
        ids = u["id"][()]
        index = u["spike_times_index"][()]
        spikes = u["spike_times"][()]
        bounds = np.r_[0, index]
        groups = [k for k in f["general/extracellular_ephys"] if k != "electrodes"]
        location = _text(f["general/extracellular_ephys"][groups[0]].attrs["location"])
        units = pd.DataFrame({
            "id": ids,
            "cell_type": [_text(v) for v in u["cell_type"][()]],
            "quality": [_text(v) for v in u["quality"][()]],
            "depth": u["depth"][()],
        })
        units["spikes"] = [spikes[bounds[i]:bounds[i + 1]] for i in range(len(ids))]
        licks = {side: f[f"acquisition/lick_times/lick_{side}_times/timestamps"][()]
                 for side in ("left", "right")}
        lick_units = {side: _text(f[f"acquisition/lick_times/lick_{side}_times/timestamps"]
                                  .attrs.get("unit", "")) for side in ("left", "right")}
        subject = _text(f["general/subject/subject_id"][()])
        meta = {
            "nwb_version": _text(f.attrs["nwb_version"]),
            "session_start": _text(f["session_start_time"][()]),
            "genotype": _text(f["general/subject/genotype"][()]),
            "sex": _text(f["general/subject/sex"][()]),
            "species": _text(f["general/subject/species"][()]),
            "related_publications": _text(f["general/related_publications"][()]),
            "spike_unit_attr": _text(u["spike_times"].attrs.get("description", "")),
            "lick_units": lick_units,
            "electrode_groups": groups,
            "electrodes_xyz_zero": all(not np.any(f["general/extracellular_ephys/electrodes"][k][()])
                                       for k in ("x", "y", "z")),
            "units_columns": sorted(k for k in u.keys()),
            "acquisition": sorted(f["acquisition"].keys()),
            "has_video": any("video" in k.lower() or "image" in k.lower() for k in f["acquisition"].keys()),
            "cell_type_description": _text(u["cell_type"].attrs.get("description", "")),
        }
    hemisphere = location.split("hemisphere:")[1].split(";")[0].strip()
    return {"path": path, "subject": subject, "session": path.split("_ses-")[1][:8],
            "trials": trials, "units": units, "licks": licks, "hemisphere": hemisphere,
            "location": location, "meta": meta}


def load_all(max_workers: int = 8) -> list[dict]:
    urls = asset_urls()
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        return list(pool.map(lambda pu: load_session(*pu), urls))


def animal_numbers(session: dict) -> str:
    """The code's animal number, reading (b) of what a mouse is in the bootstrap: the right
    hemisphere recordings of WR29 (anm369962) and WR30 (anm369963) are separate animals 29.5 and
    30.5 in defineDataset.m."""
    if session["subject"] in ("anm369962", "anm369963") and session["hemisphere"] == "right":
        return session["subject"] + " right"
    return session["subject"]


# ----------------------------------------------------------------------------------------------
# Trials, the inclusion rules and per-trial spike counts

def trial_of_spikes(spikes: np.ndarray, trials: pd.DataFrame) -> np.ndarray:
    """Index of the trial each spike falls in (from one trial start to the next), -1 before
    the first trial."""
    return np.searchsorted(trials.start.to_numpy(), spikes, side="right") - 1


def scored(trials: pd.DataFrame) -> np.ndarray:
    """Trials without early licks or photostimulation (the code's '~lickearly&~stim')."""
    return ((trials.response != "early lick") & ~trials.stim).to_numpy()


def correct_trials(trials: pd.DataFrame) -> np.ndarray:
    """Correct trials without early licks or photostimulation (the code's 'hit&~lickearly&~stim')."""
    return ((trials.response == "correct") & ~trials.stim).to_numpy()


def session_rule(session: dict) -> dict:
    """Reading (b) of the claims file's unit inclusion, the Methods' session rule: the session's
    performance is above 65% for both trial types and it has at least 50 correct trials of each
    type (scored trials only)."""
    t = session["trials"]
    ok, out = True, {}
    for side, label in (("L", "lick left"), ("R", "lick right")):
        of_side = scored(t) & (t.type == label).to_numpy()
        hits = of_side & correct_trials(t)
        out[f"n_correct_{side}"] = int(hits.sum())
        out[f"performance_{side}"] = hits.sum() / of_side.sum() if of_side.sum() else np.nan
        ok &= hits.sum() >= MIN_CORRECT and out[f"performance_{side}"] > MIN_PERFORMANCE
    out["session_ok"] = bool(ok)
    return out


LICK_FIRST_WITHIN = 2.0         # s after the go cue; rebuilding trials from the files (see last_licks)
LICK_BOUT_GAP = 1.0             # s


def last_licks(session: dict) -> np.ndarray:
    """Time of each trial's last lick (either side) after its go cue, on the session clock.

    getLickInfo takes the last of each trial's licks after its go cue. The files do not assign
    licks to trials: like the spikes, each side's lick times are stored trial by trial (trial
    start + the lick's time in the trial), so the stored order runs backwards where one trial's
    licks overlap the next trial's on the file's clock. Here, per side, the first lick within
    `LICK_FIRST_WITHIN` s after the go cue starts the bout, and the bout runs on in stored order
    while the times increase (no new trial) and the gaps stay under `LICK_BOUT_GAP` s; the later
    of the two sides' last licks is the trial's. These two values are standard choices made to
    rebuild the trials, not the paper's; the data check compares the result with the processed
    data's per-trial licks. NaN when there is none."""
    t = session["trials"]
    cue = t.cue_abs.to_numpy()
    out = np.full(len(t), -np.inf)
    for side in ("left", "right"):
        x = np.asarray(session["licks"][side])
        if len(x) == 0:
            continue
        seg = np.r_[0, np.cumsum(np.diff(x) < 0)]
        for i, c in enumerate(cue):
            hit = np.flatnonzero((x > c) & (x < c + LICK_FIRST_WITHIN))
            if len(hit) == 0:
                continue
            m = hit[0]
            while m + 1 < len(x) and seg[m + 1] == seg[m] and x[m + 1] - x[m] < LICK_BOUT_GAP:
                m += 1
            out[i] = max(out[i], x[m])
    out[~np.isfinite(out)] = np.nan
    return out


def binned_counts(spikes_sorted: np.ndarray, cue: np.ndarray, align: np.ndarray | None = None) -> sp.csr_matrix:
    """Spike counts per trial in the bins of `TIME`. The trial's spikes are those within the
    grid around its go cue (`cue`, session clock); with `align`, they are binned relative to that
    time (the last lick) in place of the go cue."""
    lo_edge = TIME[0] - DT / 2
    span = DT * len(TIME)
    lo = np.searchsorted(spikes_sorted, cue + lo_edge, "left")
    hi = np.searchsorted(spikes_sorted, cue + lo_edge + span, "left")
    ref = cue if align is None else align
    rows, cols = [], []
    for i in range(len(cue)):
        if hi[i] <= lo[i] or not np.isfinite(ref[i]):
            continue
        b = np.floor((spikes_sorted[lo[i]:hi[i]] - ref[i] - lo_edge) / DT).astype(int)
        b = b[(b >= 0) & (b < len(TIME))]
        rows.append(np.full(len(b), i))
        cols.append(b)
    rows = np.concatenate(rows) if rows else np.zeros(0, int)
    cols = np.concatenate(cols) if cols else np.zeros(0, int)
    m = sp.csr_matrix((np.ones(len(rows), np.float32), (rows, cols)), shape=(len(cue), len(TIME)))
    m.sum_duplicates()
    return m


def overlap_flags(raw: np.ndarray) -> np.ndarray:
    """Spikes stored before a spike that is earlier in time.

    Spike times are stored trial by trial. Where a trial's spikes reach past the start of the
    next trial's spikes on the file's clock, the stored order runs backwards in time; the
    spikes flagged here belong to an earlier trial than a later-stored spike at a smaller
    time, so they lie inside a later trial's span."""
    if len(raw) == 0:
        return np.zeros(0, bool)
    later_min = np.minimum.accumulate(raw[::-1])[::-1]
    later_min = np.r_[later_min[1:], np.inf]
    return raw > later_min


def build_unit(session: dict, unit: pd.Series, rule: dict, lick: np.ndarray | None) -> dict:
    """One unit: the code's inclusion rule (reading (a)), the session rule (reading (b)), and
    the binned spike counts of its scored correct trials, go-cue aligned and, when `lick` is
    given, aligned to each trial's last lick. `in_range` marks the trials of the code's range,
    from ten trials after the unit's first trial with a spike to ten before the earlier of its
    last trial with a spike and the session's last correct trial (ObjToLickPSTH)."""
    trials = session["trials"]
    raw = np.asarray(unit.spikes)
    spikes = np.sort(raw)
    rec = {"subject": session["subject"], "session": session["session"], "path": session["path"],
           "hemisphere": session["hemisphere"], "animal": animal_numbers(session),
           "cohort": "PTlower cohort" if session["subject"] in MP_ANIMALS else "PTupper cohort",
           "id": int(unit.id), "cell_type": unit.cell_type, "quality": unit.quality,
           "depth": float(unit.depth), "n_spikes": len(spikes), "session_ok": rule["session_ok"],
           "raw_spikes": raw}
    spk_trial = trial_of_spikes(spikes, trials)
    in_trial = spk_trial[spk_trial >= 0]
    idx = np.arange(len(trials))
    correct = correct_trials(trials)
    if len(in_trial):
        first, last = int(in_trial.min()), int(in_trial.max())
        last_hit = int(np.flatnonzero(trials.response.to_numpy() == "correct").max())
        lo, hi = first + EDGE_TRIALS, min(last, last_hit) - EDGE_TRIALS
        in_range = (idx >= lo) & (idx <= hi)
        # The code divides by range(eventTrials), the last trial with a spike minus the first.
        rec["spikes_per_trial"] = len(in_trial) / max(last - first, 1)
    else:
        in_range = np.zeros(len(trials), bool)
        rec["spikes_per_trial"] = 0.0
    sc = in_range & scored(trials)
    for side, label in (("L", "lick left"), ("R", "lick right")):
        of_side = sc & (trials.type == label).to_numpy()
        hits = of_side & correct
        rec[f"n_correct_{side}"] = int(hits.sum())
        rec[f"performance_{side}"] = hits.sum() / of_side.sum() if of_side.sum() else np.nan
    reasons = []
    if unit.quality not in GOOD_QUALITY:
        reasons.append("quality")
    if rec["n_correct_L"] <= MIN_CORRECT or rec["n_correct_R"] <= MIN_CORRECT:
        reasons.append("too few correct trials")
    if rec["spikes_per_trial"] <= MIN_SPIKES_PER_TRIAL:
        reasons.append("low rate")
    if not (rec["performance_L"] > MIN_PERFORMANCE and rec["performance_R"] > MIN_PERFORMANCE):
        reasons.append("performance")
    rec["included"] = not reasons
    rec["reason"] = ", ".join(reasons)
    use = correct & (trials.type.isin(["lick left", "lick right"])).to_numpy()
    cue = trials.cue_abs.to_numpy()[use]
    rec["trial_index"] = idx[use]
    rec["is_right"] = trials.type.to_numpy()[use] == "lick right"
    rec["in_range"] = in_range[use]
    rec["go"] = binned_counts(spikes, cue)
    if lick is not None:
        rec["lick"] = binned_counts(spikes, cue, lick[use])
        rec["last_lick_rel"] = lick[use] - cue
    return rec


def build_units(sessions: list[dict], unidentified: bool = True) -> list[dict]:
    """Every tagged unit, and every unidentified unit of good quality (the code loads only
    units of quality Excellent, Good or single; getData), of every session."""
    out = []
    for s in sessions:
        rule = session_rule(s)
        lick = last_licks(s)
        for _, unit in s["units"].iterrows():
            tagged = unit.cell_type in TYPES
            if not tagged and not (unidentified and unit.quality in GOOD_QUALITY):
                continue
            out.append(build_unit(s, unit, rule, lick if tagged else None))
    return out


def selected(units: list[dict], cell_type: str, selection: str, cohort: str | None = None,
             left_only: bool = False) -> list[dict]:
    """The units of a population under a reading of the unit inclusion: 'code' (reading (a),
    the per-unit rule) or 'methods' (reading (b), the session rule; unidentified units also keep
    the code's quality filter, as the code loads only those). `cell_type` 'unidentified' takes
    the untagged units of `cohort` (the code's groups 3 and 4)."""
    out = []
    for u in units:
        if u["cell_type"] != cell_type or (cohort and u["cohort"] != cohort):
            continue
        if left_only and u["hemisphere"] != "left":
            continue
        keep = u["included"] if selection == "code" else u["session_ok"]
        if keep:
            out.append(u)
    return out


def trial_rows(u: dict, trial_range: str) -> tuple[np.ndarray, np.ndarray]:
    """Rows of a unit's left and right trials under a reading of the trial range: 'unit' (a),
    the code's range of the unit; 'all' (b), all its scored correct trials."""
    keep = u["in_range"] if trial_range == "unit" else np.ones(len(u["is_right"]), bool)
    return np.flatnonzero(keep & ~u["is_right"]), np.flatnonzero(keep & u["is_right"])


# ----------------------------------------------------------------------------------------------
# Rates

def smooth(x: np.ndarray, n: int = SMOOTH) -> np.ndarray:
    """Causal boxcar along the last axis: the mean of the current bin and the n - 1 before, with
    zeros before the first bin (MySmooth, conv 'same' with a half-zeroed kernel)."""
    c = np.cumsum(x, axis=-1, dtype=float)
    out = c.copy()
    out[..., n:] = c[..., n:] - c[..., :-n]
    return out / n


def bins(window: tuple[float, float], kind: str = "epoch") -> np.ndarray:
    """Bins of a window: 'epoch' centres in (start, end] (getData); 'cd' in [start, end)."""
    a, b = window
    return (TIME > a) & (TIME <= b) if kind == "epoch" else (TIME >= a) & (TIME < b)


def window_weights(window: tuple[float, float], kind: str = "epoch", n: int = SMOOTH) -> np.ndarray:
    """Weights w such that counts @ w / DT is the mean over the window's bins of the smoothed rate."""
    ind = bins(window, kind).astype(float)
    c = np.r_[np.cumsum(ind[::-1])[::-1], 0.0]
    s = np.arange(len(TIME))
    w = c[s] - c[np.minimum(s + n, len(TIME))]
    return w / (n * ind.sum())


def trial_means(counts: sp.csr_matrix, rows: np.ndarray, window: tuple[float, float], kind: str = "epoch") -> np.ndarray:
    """Per-trial mean of the smoothed rate (spikes/s) over a window."""
    return np.asarray(counts[rows] @ window_weights(window, kind)).ravel() / DT


def average_rate(counts: sp.csr_matrix, rows: np.ndarray, n: int = SMOOTH) -> np.ndarray:
    """Trial-averaged smoothed rate (spikes/s) over `rows`."""
    if len(rows) == 0:
        return np.zeros(len(TIME))
    return smooth(np.asarray(counts[rows].mean(axis=0)).ravel(), n) / DT


def ranksum_p(x: np.ndarray, y: np.ndarray) -> float:
    """Two-sided Wilcoxon rank-sum p, with tie and continuity corrections (as MATLAB ranksum's
    approximate method, which it uses at these trial counts); 1 when all values are equal."""
    if np.ptp(np.r_[x, y]) == 0:
        return 1.0
    return float(stats.mannwhitneyu(x, y, alternative="two-sided", method="asymptotic").pvalue)


def dprime(x_left: np.ndarray, x_right: np.ndarray) -> float:
    """(mean right - mean left) / sqrt(var left + var right), 0 when undefined (equation 1)."""
    den = np.sqrt(np.var(x_left, ddof=1) + np.var(x_right, ddof=1))
    return float((x_right.mean() - x_left.mean()) / den) if den > 0 else 0.0


def roc(x_left: np.ndarray, x_right: np.ndarray) -> tuple[float, float]:
    """Single-unit decoding (doROC.m, decodingAccuracy.m): every observed value is a threshold,
    the polarity is set by the side of the ROC area, and the accuracy is the best fraction of
    trials classified correctly. Returns the accuracy and the d' at the first threshold that
    reaches it (norminv(TP) - norminv(FP), as acc.dprime)."""
    dat = np.r_[x_left, x_right]
    lab = np.r_[np.zeros(len(x_left), bool), np.ones(len(x_right), bool)]
    thr = np.unique(dat)
    above = dat[None, :] >= thr[:, None]

    def curve(pol):
        pos = lab if pol else ~lab
        tp = (above & pos).sum(axis=1) / pos.sum()
        fp = (above & ~pos).sum(axis=1) / (~pos).sum()
        acc = ((above & pos).sum(axis=1) + (~above & ~pos).sum(axis=1)) / len(dat)
        return tp, fp, acc

    tp, fp, acc = curve(True)
    if abs(np.trapezoid(tp, fp)) < 0.5:
        tp, fp, acc = curve(False)
    i = int(np.argmax(acc))
    with np.errstate(divide="ignore"):
        d = stats.norm.ppf(tp[i]) - stats.norm.ppf(fp[i])
    return float(acc[i]), float(d)


# ----------------------------------------------------------------------------------------------
# The hierarchical bootstrap (Methods; Projections.m getBootix, DirectionVector, projectOntoVector)

def seeded(key: str) -> np.random.Generator:
    """A generator of its own for each analysis, seeded from its name (a standard choice)."""
    return np.random.default_rng(zlib.crc32(key.encode()))


def _draw_counts(rng: np.random.Generator, n: int, k: int, n_iter: int) -> np.ndarray:
    """(n_iter, n) counts of k draws with replacement from n items, per iteration."""
    idx = rng.integers(0, n, size=(n_iter, k))
    flat = (np.arange(n_iter)[:, None] * n + idx).ravel()
    return np.bincount(flat, minlength=n_iter * n).reshape(n_iter, n).astype(float)


def unit_draws(animals: list[str], rng: np.random.Generator, n_iter: int) -> np.ndarray:
    """(n_iter, n_units) times each unit is drawn: M animals with replacement from the cohort,
    then n units with replacement from the pooled units of the drawn animals (an animal drawn
    twice is pooled once), as getBootix."""
    animals = np.asarray(animals)
    uniq = np.unique(animals)
    out = np.zeros((n_iter, len(animals)))
    for k in range(n_iter):
        drawn = rng.choice(uniq, size=len(uniq), replace=True)
        pool = np.flatnonzero(np.isin(animals, drawn))
        out[k] = np.bincount(rng.choice(pool, size=len(animals), replace=True), minlength=len(animals))
    return out


def _boot_dprime(xl, xr, cl, cr):
    """d' per iteration from resampled trials (counts cl, cr over the unit's trials), with the
    code's zero weight where the rank-sum p of the resampled trials is 1 (DirectionVector,
    cv.*(pval<1)); p is 1 when the rank sum is within 0.5 of its mean, or every value is tied."""
    kl, kr = cl[0].sum(), cr[0].sum()
    mul, mur = cl @ xl / kl, cr @ xr / kr
    vl = np.maximum(cl @ xl ** 2 - kl * mul ** 2, 0) / (kl - 1)
    vr = np.maximum(cr @ xr ** 2 - kr * mur ** 2, 0) / (kr - 1)
    den = np.sqrt(vl + vr)
    with np.errstate(divide="ignore", invalid="ignore"):
        d = np.where(den > 0, (mur - mul) / den, 0.0)
    kmat = (xl[:, None] > xr[None, :]) + 0.5 * (xl[:, None] == xr[None, :])
    u_stat = ((cl @ kmat) * cr).sum(axis=1)
    tied = (vl == 0) & (vr == 0) & np.isclose(mul, mur)
    d[(np.abs(u_stat - kl * kr / 2) <= 0.5) | tied] = 0.0
    return d


def full_dprime(xl, xr):
    """d' over all trials, with the zero weight where the rank-sum p is 1 (bootrep 0)."""
    return 0.0 if ranksum_p(xl, xr) >= 1 else dprime(xl, xr)


def coding_direction(units: list[dict], trial_range: str, window: tuple[float, float]) -> np.ndarray:
    """The coding direction over all trials (bootrep 0): d' per unit, normalised by the L1 norm."""
    v = np.array([full_dprime(*(trial_means(u["go"], r, window, "cd") for r in trial_rows(u, trial_range)))
                  for u in units])
    return v / np.abs(v).sum()


def bootstrap(units: list[dict], animal_key: str, trial_range: str, rng: np.random.Generator,
              n_iter: int = N_BOOT, n_trials: int = BOOT_TRIALS, lick: bool = False,
              resample_projection: bool = True, scales: np.ndarray | None = None) -> dict:
    """Selectivity along CDearly, CDlate and CDgo (orthogonalised to CDlate) for one population.

    Per iteration: units drawn hierarchically (`unit_draws`, with `animal_key` 'subject' for
    the 4 and 8 mice of the Methods or 'animal' for the code's animal numbers), and for every
    unit `n_trials` trials of each type with replacement. The coding directions use the
    resampled trials; each unit's weight is multiplied by the times it was drawn and the vector
    is normalised by its L1 norm. Selectivity is the right projection minus the left. Reading
    (a) of the projection ('proj a') projects the trial-averaged rates of all the unit's trials,
    as the code; reading (b) ('proj b') projects the averages of the resampled trials. Go-cue
    aligned selectivity has its mean in the baseline epoch subtracted (plotProjectionSelectivity);
    lick-aligned selectivity does not.

    `scales`, one per unit, multiplies each unit's rates before they are projected (the z-scored
    variant of Extended Data Fig. 8; the coding directions do not change, as d' does not depend
    on a unit's scale).

    Returns {'go': {reading: {cd: (n_iter, T)}}, 'lick': ..., 'weights': {cd: (n_iter, n)}}."""
    n = len(units)
    draws = unit_draws([u[animal_key] for u in units], rng, n_iter)
    rows = [trial_rows(u, trial_range) for u in units]
    counts = [(_draw_counts(rng, len(rl), min(len(rl), n_trials), n_iter),
               _draw_counts(rng, len(rr), min(len(rr), n_trials), n_iter)) for rl, rr in rows]
    weights = {}
    for name, window in CD_WINDOWS.items():
        w = np.zeros((n_iter, n))
        for i, u in enumerate(units):
            xl, xr = (trial_means(u["go"], r, window, "cd") for r in rows[i])
            w[:, i] = _boot_dprime(xl, xr, *counts[i])
        w *= draws
        with np.errstate(invalid="ignore"):
            weights[name] = w / np.abs(w).sum(axis=1, keepdims=True)
    late = weights["late"]
    go = weights["go"]
    weights["go"] = go - ((go * late).sum(axis=1) / (late * late).sum(axis=1))[:, None] * late
    out = {"weights": weights}
    base = bins(EPOCHS["baseline"])
    scales = np.ones(n) if scales is None else np.asarray(scales, float)
    for align in ("go", "lick") if lick else ("go",):
        cds = ("early", "late", "go") if align == "go" else ("late", "go")
        diff_a = np.stack([(average_rate(u[align], rr) - average_rate(u[align], rl)) * scales[i]
                           for i, (u, (rl, rr)) in enumerate(zip(units, rows))], axis=1)   # (T, n)
        res = {"proj a": {c: (diff_a @ weights[c].T).T for c in cds}}
        if resample_projection:
            acc = {c: np.zeros((n_iter, len(TIME))) for c in cds}
            for i, u in enumerate(units):
                (rl, rr), (cl, cr) = rows[i], counts[i]
                ml = smooth((u[align][rl].T @ cl.T).T / cl[0].sum()) / DT
                mr = smooth((u[align][rr].T @ cr.T).T / cr[0].sum()) / DT
                d = (mr - ml) * scales[i]
                for c in cds:
                    acc[c] += d * weights[c][:, i][:, None]
            res["proj b"] = acc
        if align == "go":
            for reading in res.values():
                for c in reading:
                    reading[c] = reading[c] - reading[c][:, base].mean(axis=1, keepdims=True)
        out[align] = res
    return out


SUMMARY_WINDOWS = {"CDearly window": (-2.5, -2.1), "sample epoch": (-2.5, -1.5), "late delay": (-0.4, 0.0),
                   "response": (0.0, 0.4)}


def summarise(boot: dict) -> dict:
    """Per alignment, projection reading and coding direction: the 5th, 50th and 95th
    percentiles of the bootstrap selectivity at each bin, and per iteration its mean over the
    windows of `SUMMARY_WINDOWS` (bins with centres in [start, end))."""
    out = {}
    for align in ("go", "lick"):
        for reading, cds in boot.get(align, {}).items():
            for cd, sel in cds.items():
                q5, q50, q95 = np.nanpercentile(sel, [5, 50, 95], axis=0)
                out[(align, reading, cd)] = {
                    "q5": q5, "q50": q50, "q95": q95,
                    "means": {w: sel[:, bins(win, "cd")].mean(axis=1) for w, win in SUMMARY_WINDOWS.items()}}
    return out


def binned_cd_correlation(units: list[dict], animal_key: str, trial_range: str, rng: np.random.Generator,
                          time_range: tuple[float, float], n_iter: int = N_BOOT, n_trials: int = BOOT_TRIALS,
                          reference: str = "late") -> np.ndarray:
    """(n_iter, bins) inner product of the unit-normalised coding direction at each bin in
    `time_range` with a reference direction (Methods, the correlation matrices; Extended Data
    Fig. 7e). The per-bin direction is the d' of each unit's smoothed rate in that bin over
    resampled trials, weighted by the times the unit was drawn, normalised to unit length.
    `reference` 'late' is CDlate of the same iteration (d' over the window -0.4 to 0 s, the same
    weighting, unit length); 'delay' is the code's variant (CDCorrelation.m), the mean over
    the bins of the delay epoch of the inner products with each bin's direction."""
    sel = (TIME >= time_range[0]) & (TIME <= time_range[1])
    draws = unit_draws([u[animal_key] for u in units], rng, n_iter)
    rows = [trial_rows(u, trial_range) for u in units]
    counts = [(_draw_counts(rng, len(rl), min(len(rl), n_trials), n_iter),
               _draw_counts(rng, len(rr), min(len(rr), n_trials), n_iter)) for rl, rr in rows]

    def binned(i):
        out = []
        for r, c in zip(rows[i], counts[i]):
            k = c[0].sum()
            s = smooth(units[i]["go"][r].toarray()) / DT
            m1 = c @ s / k
            m2 = c @ s ** 2 / k
            out.append((m1, np.maximum(m2 - m1 ** 2, 0) * k / (k - 1)))
        (ml, vl), (mr, vr) = out
        den = np.sqrt(vl + vr)
        with np.errstate(divide="ignore", invalid="ignore"):
            return np.where(den > 0, (mr - ml) / den, 0.0)

    if reference == "late":
        ref = np.zeros((n_iter, len(units)))
        for i, u in enumerate(units):
            xl, xr = (trial_means(u["go"], r, CD_WINDOWS["late"], "cd") for r in rows[i])
            ref[:, i] = _boot_dprime(xl, xr, *counts[i])
        ref *= draws
        ref /= np.linalg.norm(ref, axis=1, keepdims=True)
        dot = np.zeros((n_iter, sel.sum()))
        norm2 = np.zeros((n_iter, sel.sum()))
        for i in range(len(units)):
            d = binned(i) * draws[:, i][:, None]
            dot += d[:, sel] * ref[:, i][:, None]
            norm2 += d[:, sel] ** 2
        return dot / np.sqrt(norm2)
    delay = bins(EPOCHS["delay"])
    vecs = np.zeros((n_iter, len(TIME), len(units)), np.float32)
    for i in range(len(units)):
        vecs[:, :, i] = binned(i) * draws[:, i][:, None]
    vecs /= np.linalg.norm(vecs, axis=2, keepdims=True) + 1e-30
    mean_delay = vecs[:, delay, :].mean(axis=1)
    return np.einsum("ktu,ku->kt", vecs[:, sel, :], mean_delay)


def epoch_similarity(units: list[dict], animal_key: str, trial_range: str, rng: np.random.Generator,
                     n_iter: int = 100, max_trials: int = 500) -> np.ndarray:
    """The code's sample to late delay similarity (CDCorrelation.m, compareEpochs): per
    iteration, d' per unit in the sample and late delay epochs over resampled trials (all of
    the unit's trials up to 500, with replacement), weighted by the times the unit was drawn,
    normalised to unit length; the inner product of the two."""
    draws = unit_draws([u[animal_key] for u in units], rng, n_iter)
    rows = [trial_rows(u, trial_range) for u in units]
    counts = [(_draw_counts(rng, len(rl), min(len(rl), max_trials), n_iter),
               _draw_counts(rng, len(rr), min(len(rr), max_trials), n_iter)) for rl, rr in rows]
    vec = {}
    for epoch in ("sample", "late delay"):
        v = np.zeros((n_iter, len(units)))
        for i, u in enumerate(units):
            xl, xr = (trial_means(u["go"], r, EPOCHS[epoch]) for r in rows[i])
            (cl, cr) = counts[i]
            kl, kr = cl[0].sum(), cr[0].sum()
            mul, mur = cl @ xl / kl, cr @ xr / kr
            vl = np.maximum(cl @ xl ** 2 - kl * mul ** 2, 0) / (kl - 1)
            vr = np.maximum(cr @ xr ** 2 - kr * mur ** 2, 0) / (kr - 1)
            den = np.sqrt(vl + vr)
            with np.errstate(divide="ignore", invalid="ignore"):
                v[:, i] = np.where(den > 0, (mur - mul) / den, 0.0)
        v *= draws
        vec[epoch] = v / np.linalg.norm(v, axis=1, keepdims=True)
    return (vec["sample"] * vec["late delay"]).sum(axis=1)


def onset(lower5: np.ndarray, stamp: str = "centre", sustained: int = 1) -> float:
    """First time after the go cue at which the 5th percentile is above zero, in seconds;
    `stamp` dates a bin by its centre, end or start; `sustained` asks for that many consecutive
    significant bins. NaN when there is none."""
    t = TIME + {"centre": 0.0, "end": DT / 2, "start": -DT / 2}[stamp]
    sig = lower5 > 0
    after = np.flatnonzero(t > 0)
    for i in after:
        if i + sustained <= len(sig) and sig[i:i + sustained].all():
            return float(t[i])
    return float("nan")


def first_run_end(lower5: np.ndarray, stamp: str = "centre") -> float:
    """Last time of the first run of significant bins after the go cue (NaN when there is none)."""
    t = TIME + {"centre": 0.0, "end": DT / 2, "start": -DT / 2}[stamp]
    sig = (lower5 > 0) & (t > 0)
    idx = np.flatnonzero(sig)
    if len(idx) == 0:
        return float("nan")
    i = idx[0]
    while i + 1 < len(sig) and sig[i + 1]:
        i += 1
    return float(t[i])


# ----------------------------------------------------------------------------------------------
# Variance explained (Extended Data Fig. 6)

def variance_explained(x: np.ndarray, n_comp: int = 6) -> np.ndarray:
    """Cumulative fraction of variance explained by 1..n_comp principal components of x
    (observations by neurons)."""
    x = x - x.mean(axis=0)
    s = np.linalg.svd(x, compute_uv=False) ** 2
    return np.cumsum(s)[:n_comp] / s.sum()


def concatenated(units: list[dict], trial_range: str, n: int = SMOOTH) -> np.ndarray:
    """Trial-averaged lick-left and lick-right rates of each unit, concatenated in time and
    z-scored per unit (Methods); (2T, n_units). Units without spikes give zeros."""
    cols = []
    for u in units:
        rl, rr = trial_rows(u, trial_range)
        x = np.r_[average_rate(u["go"], rl, n), average_rate(u["go"], rr, n)]
        sd = x.std()
        cols.append((x - x.mean()) / sd if sd > 0 else np.zeros_like(x))
    return np.column_stack(cols)


def code_variance_explained(units: list[dict], trial_range: str, rng: np.random.Generator,
                            n_iter: int = N_BOOT, n_comp: int = 6, pool: list[dict] | None = None,
                            size: int | None = None) -> np.ndarray:
    """The code's variant (VarianceExplained.m, calcVarExp): 100 ms smoothing (sm = 39, 20 bins),
    per iteration `size` units drawn without replacement from `pool` (or all of `units`) and 50
    trials of each type resampled for each, trial-averaged rates of the first 1000 bins of each
    type concatenated, the baseline epoch mean subtracted and divided by the s.d.; variance
    explained by k components taken per unit and averaged over units. (n_iter, n_comp)."""
    pool = units if pool is None else pool
    size = len(pool) if size is None else size
    base = bins(EPOCHS["baseline"])
    out = np.zeros((n_iter, n_comp))
    for k in range(n_iter):
        pick = rng.choice(len(pool), size=size, replace=False)
        cols = []
        for j in pick:
            u = pool[j]
            series = []
            for r in trial_rows(u, trial_range):
                c = _draw_counts(rng, len(r), min(len(r), BOOT_TRIALS), 1)[0]
                series.append(smooth(np.asarray(u["go"][r].T @ c).ravel() / c.sum(), 20) / DT)
            b = np.mean([s[base].mean() for s in series])
            x = np.r_[series[0][:1000], series[1][:1000]] - b
            sd = x.std(ddof=1)
            cols.append(x / sd if sd > 0 else np.zeros_like(x))
        ts = np.column_stack(cols)
        ts = ts - ts.mean(axis=0)
        uu, s, vt = np.linalg.svd(ts, full_matrices=False)
        tot = ts.var(axis=0, ddof=1)
        for c in range(n_comp):
            rec = (uu[:, :c + 1] * s[:c + 1]) @ vt[:c + 1]
            with np.errstate(invalid="ignore", divide="ignore"):
                ve = 1 - (ts - rec).var(axis=0, ddof=1) / tot
            out[k, c] = np.nanmean(np.where(np.isfinite(ve), ve, np.nan))
    return out


# ----------------------------------------------------------------------------------------------
# The paper's processed data, Ephys.zip of doi:10.25378/janelia.7007846 (version 1), file
# 13292708. One file per animal and recording period (two for anm369962 and anm369963), each
# holding several sessions. Read in the data check, to show how the files' spike times were built
# and which of the paper's units the dandiset holds, and in variants that rerun tests on the
# paper's units. No outcome rests on them.
FIGSHARE_EPHYS_ZIP = "https://ndownloader.figshare.com/files/13292708"
FIGSHARE_SEQ_ZIP = "https://ndownloader.figshare.com/files/13308305"
FIGSHARE_AXONS_ZIP = "https://ndownloader.figshare.com/files/13308434"
FIGSHARE_ANATOMY_ZIP = "https://ndownloader.figshare.com/files/13314290"


class _Seekable(io.RawIOBase):
    def __init__(self, f):
        self.f = f

    def seekable(self):
        return True

    def readable(self):
        return True

    def seek(self, *args):
        return self.f.seek(*args)

    def tell(self):
        return self.f.tell()

    def read(self, n=-1):
        return self.f.read(n)


def figshare_zip(url: str) -> zipfile.ZipFile:
    """A zip file of the Figshare record, read by range requests, in memory."""
    real = requests.head(url, allow_redirects=True, timeout=60).url
    return zipfile.ZipFile(_Seekable(remfile.File(real)))


def processed_members() -> list[str]:
    """Names of the processed data files in Ephys.zip."""
    return sorted(n for n in figshare_zip(FIGSHARE_EPHYS_ZIP).namelist() if n.endswith("_psth.mat"))


def _processed_unit(mat_obj, meta, tt, psth, j, member, time_ok):
    """One tagged unit of a processed session in the same form as `build_unit`, from the
    processed go-cue aligned rates (the code's psth, NaN outside the trial range)."""
    subject = member.split("data_structure_")[1].split("_")[0]
    session = str(meta.filename).split("_")[-1].split(".")[0].replace("-", "")
    hit, left, right = (np.asarray(getattr(tt, k), bool) for k in ("hit", "L", "R"))
    sc = ~np.asarray(tt.lickearly, bool) & ~np.asarray(tt.stim, bool)
    trial_no = np.arange(1, len(hit) + 1)
    last_hit = trial_no[hit].max()
    unit = np.atleast_1d(mat_obj.eventSeriesHash.value)[j]
    times = np.atleast_1d(unit.eventTimes).astype(float)
    trials = np.atleast_1d(unit.eventTrials).astype(int)
    first, last = max(trials.min(), 1), trials.max()
    in_range = (trial_no >= first + EDGE_TRIALS) & (trial_no <= min(last, last_hit) - EDGE_TRIALS)
    number = int(np.atleast_1d(meta.unitNum)[j])
    rec = {"subject": subject, "session": session, "id": number,
           "cell_type": "PTlower" if subject in MP_ANIMALS else "PTupper",
           "quality": str(np.atleast_1d(meta.unitQuality)[j]), "depth": float(np.atleast_1d(meta.depth)[j]),
           "manipulator_depth": float(meta.manipulatorDepth), "animal": str(meta.animal),
           "spikes_per_trial": len(times) / max(np.ptp(trials), 1)}
    for side, of_side in (("L", left), ("R", right)):
        hits = in_range & sc & of_side & hit
        misses = in_range & sc & of_side & ~hit
        rec[f"n_correct_{side}"] = int(hits.sum())
        rec[f"performance_{side}"] = hits.sum() / (hits.sum() + misses.sum()) if hits.sum() + misses.sum() else np.nan
    reasons = []
    if rec["quality"] not in GOOD_QUALITY:
        reasons.append("quality")
    if rec["n_correct_L"] <= MIN_CORRECT or rec["n_correct_R"] <= MIN_CORRECT:
        reasons.append("too few correct trials")
    if rec["spikes_per_trial"] <= MIN_SPIKES_PER_TRIAL:
        reasons.append("low rate")
    if not (rec["performance_L"] > MIN_PERFORMANCE and rec["performance_R"] > MIN_PERFORMANCE):
        reasons.append("performance")
    rec["included"] = not reasons
    rec["reason"] = ", ".join(reasons)
    rates = psth[:, j, :]                                   # (time, trials), spikes/s
    has = ~np.all(np.isnan(rates), axis=0)
    use = sc & hit & (left | right) & has
    rec["is_right"] = right[use]
    rec["in_range"] = np.ones(use.sum(), bool)
    vals = np.nan_to_num(rates[:, use].T) * DT
    rec["go"] = sp.csr_matrix(vals[:, time_ok].astype(np.float32))
    rec["isi_times"], rec["isi_trials"] = times, trials
    # last-lick aligned counts from the processed spike times and per-trial licks (ObjToLickPSTH)
    props = mat_obj.trialPropertiesHash.value
    last = np.full(len(hit) + 1, np.nan)
    for k in range(len(hit)):
        ll = np.concatenate([np.atleast_1d(props[c][k]).astype(float) for c in (5, 6)]) - float(np.atleast_1d(props[2])[k])
        ll = ll[ll > 0]
        if len(ll):
            last[k + 1] = ll.max()
    row_of = np.full(len(hit) + 1, -1)
    row_of[1:][use] = np.arange(use.sum())
    rows = row_of[trials]
    b = np.floor((times - last[trials] - (TIME[0] - DT / 2)) / DT)
    ok = (rows >= 0) & np.isfinite(b) & (b >= 0) & (b < len(TIME))
    m = sp.csr_matrix((np.ones(ok.sum(), np.float32), (rows[ok], b[ok].astype(int))), shape=(use.sum(), len(TIME)))
    m.sum_duplicates()
    rec["lick"] = m
    return rec


def compare_with_processed(session: dict, mat: dict, index: int = 0) -> tuple[pd.DataFrame, pd.DataFrame]:
    """For session `index` of a processed file: per unit, whether the file's spike times equal
    trial start + go cue + the processed cue-relative spike time, in stored order; and per
    trial, the span of the processed spike times (pooled over units) relative to the go cue,
    and the last lick after the go cue in the processed trial properties."""
    t = session["trials"]
    cue_abs = t.cue_abs.to_numpy()
    obj, meta = np.atleast_1d(mat["obj"])[index], np.atleast_1d(mat["meta"])[index]
    rows = []
    lo = np.full(len(t), np.inf)
    hi = np.full(len(t), -np.inf)
    for j, number in enumerate(np.atleast_1d(meta.unitNum)):
        unit = np.atleast_1d(obj.eventSeriesHash.value)[j]
        rel = np.atleast_1d(unit.eventTimes).astype(float)
        trial = np.atleast_1d(unit.eventTrials).astype(int) - 1
        stored = session["units"].set_index("id").spikes.get(int(number))
        same = stored is not None and len(stored) == len(rel) and np.allclose(stored, cue_abs[trial] + rel, atol=2e-5)
        rows.append({"unit": int(number), "spikes": len(rel), "in_file": stored is not None,
                     "equal_in_stored_order": bool(same)})
        np.minimum.at(lo, trial, rel)
        np.maximum.at(hi, trial, rel)
    props = obj.trialPropertiesHash.value
    last = []
    for j in range(len(t)):
        cue_j = np.atleast_1d(props[2])[j]
        ll = [np.atleast_1d(props[k][j]).astype(float) - cue_j for k in (5, 6)]
        ll = np.concatenate(ll)
        ll = ll[ll > 0]
        last.append(ll.max() if len(ll) else np.nan)
    spans = pd.DataFrame({"first": lo, "last": hi, "pole_in": (t.pole_in - t.cue).to_numpy(),
                          "start_spacing": np.r_[np.diff(t.start.to_numpy()), np.nan],
                          "processed last lick": last})
    return pd.DataFrame(rows), spans


def read_processed(sessions: list[dict]) -> tuple[list[dict], pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, dict]:
    """Read every processed file. Returns the tagged units of every processed session (as
    `build_unit`, go-cue aligned only); per unit of every session also in the dandiset, whether
    the file's spike times equal trial start + go cue + the processed time in stored order; per
    such session, the start of the processed spike windows relative to the pole coming in, for
    the first ten trials and for the others; per such session, the last lick after the go cue
    from the files (`last_licks`) against the processed trial properties; and the count of
    unidentified good-quality units per processed session; and, per session also in the
    dandiset, for every trial whether the last lick rebuilt from the files equals the processed
    one within 5 ms (False where either is missing)."""
    by_key = {(s["subject"], s["session"]): s for s in sessions}
    records, storage, shifts, licks, unidentified = [], [], [], [], []
    lick_agree = {}
    for member in processed_members():
        # a fresh signed URL for each file, as the archive's links expire
        data = figshare_zip(FIGSHARE_EPHYS_ZIP).read(member)
        mat = sio.loadmat(io.BytesIO(data), squeeze_me=True, struct_as_record=False)
        del data
        time_ok = np.isin(np.round(np.asarray(mat["time"], float), 4), TIME)
        subject = member.split("data_structure_")[1].split("_")[0]
        metas, objs, tts, psths = (np.atleast_1d(mat[k]) for k in ("meta", "obj", "tt", "psth"))
        for i in range(len(metas)):
            meta = metas[i]
            session = str(meta.filename).split("_")[-1].split(".")[0].replace("-", "")
            numbers = np.atleast_1d(meta.unitNum)
            quality = np.atleast_1d(meta.unitQuality)
            s = by_key.get((subject, session))
            unidentified.append({"subject": subject, "session": session, "in_dandiset": s is not None,
                                 "cohort": "PTlower cohort" if subject in MP_ANIMALS else "PTupper cohort",
                                 "unidentified good": int(sum((n < 1000) and (str(q) in GOOD_QUALITY)
                                                             for n, q in zip(numbers, quality)))})
            psth = psths[i] if psths[i].ndim == 3 else psths[i][:, None, :]   # one unit: squeezed
            for j, number in enumerate(numbers):
                if 1000 < number < 2000:
                    r = _processed_unit(objs[i], meta, tts[i], psth, j, member, time_ok)
                    r["in_dandiset"] = s is not None
                    records.append(r)
            if s is None:
                continue
            per_unit, spans = compare_with_processed(s, mat, i)
            storage.append(per_unit.assign(subject=subject, session=session))
            offset = (spans["first"] - spans["pole_in"]).replace([np.inf, -np.inf], np.nan)
            shifts.append({"subject": subject, "session": session, "trials": len(spans),
                           "first 10: first - pole_in": offset.iloc[:EDGE_TRIALS].median(),
                           "others: first - pole_in": offset.iloc[EDGE_TRIALS:].median()})
            mine = last_licks(s) - s["trials"].cue_abs.to_numpy()
            corr = correct_trials(s["trials"])
            lick_agree[(subject, session)] = np.abs(mine - spans["processed last lick"].to_numpy()) < 5e-3
            diff = (mine - spans["processed last lick"].to_numpy())[corr]
            licks.append({"subject": subject, "session": session, "correct trials": int(corr.sum()),
                          "equal (within 5 ms)": int(np.sum(np.abs(diff) < 5e-3)),
                          "missing in files": int(np.sum(np.isnan(mine[corr]))),
                          "max |difference| (s)": float(np.nanmax(np.abs(diff))) if np.isfinite(diff).any() else np.nan})
        del mat
    return (records, pd.concat(storage, ignore_index=True), pd.DataFrame(shifts), pd.DataFrame(licks),
            pd.DataFrame(unidentified), lick_agree)


def isi_burst_fraction(times: np.ndarray, boundary: np.ndarray) -> float:
    """Fraction of a unit's spikes whose interval to the next spike is under 5 ms, intervals
    across a trial boundary counted as long (showISIHists: the denominator is every spike)."""
    if len(times) == 0:
        return np.nan
    isi = np.diff(np.r_[times, np.inf])
    isi[np.r_[boundary, True]] = np.inf
    return float(np.sum(isi < BURST_ISI) / len(isi))


# ----------------------------------------------------------------------------------------------
# Sequencing and axon data on the same Figshare record (claims with data elsewhere)

def read_seq() -> dict:
    """Seq.zip: the single-cell annotation (SingleCellAnnotation.txt), the single-cell expression
    of the PT cells (SingleCellExpression.txt), the bulk RNA-seq counts (bulk_data.txt) and the
    sample key (sample.key), read in memory."""
    z = figshare_zip(FIGSHARE_SEQ_ZIP)
    anno = pd.read_csv(io.BytesIO(z.read("Seq/Data/SingleCellAnnotation.txt")), low_memory=False)
    sc = pd.read_csv(io.BytesIO(z.read("Seq/Data/SingleCellExpression.txt")), index_col=0)
    bulk = pd.read_csv(io.BytesIO(z.read("Seq/Data/bulk_data.txt")), index_col=0)
    key = pd.read_csv(io.BytesIO(z.read("Seq/Data/sample.key")), sep="\t", header=None, names=["sample", "label"])
    meta = pd.read_csv(io.BytesIO(z.read("Seq/Data/cluster_metadata.csv")), index_col=0)
    return {"anno": anno, "sc": sc, "bulk": bulk, "key": key, "cluster_metadata": meta}


def bulk_vs_sc(seq: dict, bulk_scale: str = "cpm", n_genes: int = 100) -> dict:
    """bulkVsSC.m: fold change (mean log2(1 + x), PTupper minus PTlower) of the genes in both
    data sets, in single cells (Npsr1 and Hpgd clusters against Slco2a1, by the annotation's
    primary cluster label) and in bulk samples (columns 1, 6, 8, 9, 11, 13 thalamus and 2, 4, 7,
    10, 12, 14 medulla, as the code); genes ranked by how well detection (> 0) in single cells
    classifies the two groups, the `n_genes` at each end kept; Pearson's r of the fold changes
    over those genes. `bulk_scale` 'cpm' scales each bulk sample to counts per million, as the
    Extended Data Fig. 4i legend says and the claims file's criterion follows; 'counts' uses the
    bulk values as stored, as the code (a variant). The single-cell values are stored as CPM."""
    anno, sc, bulk = seq["anno"], seq["sc"], seq["bulk"]
    lab = anno.set_index("sample_id").primary_cluster_label.astype(str)
    lab = lab.reindex(sc.columns)
    thal = lab.str.contains("Hpgd") | lab.str.contains("Npsr1")
    med = lab.str.contains("Slco2a1")
    # gene names repeat in the tables; MATLAB's ismember takes the first row of each name
    sc = sc[~sc.index.duplicated()]
    b = bulk.astype(float)
    if bulk_scale == "cpm":
        b = b / b.sum(axis=0) * 1e6         # over all of the sample's counts
    b = b[~b.index.duplicated()]
    thal_cols = [1, 6, 8, 9, 11, 13]
    med_cols = [2, 4, 7, 10, 12, 14]
    genes = sc.index.intersection(b.index)
    # MATLAB intersect sorts the genes; the order matters only for ties in the ranking
    genes = genes.sort_values()
    s = sc.loc[genes]
    bb = b.loc[genes]
    sc_fc = np.log2(1 + s.loc[:, thal.to_numpy()]).mean(axis=1) - np.log2(1 + s.loc[:, med.to_numpy()]).mean(axis=1)
    bulk_fc = (np.log2(1 + bb.iloc[:, [c - 1 for c in thal_cols]]).mean(axis=1)
               - np.log2(1 + bb.iloc[:, [c - 1 for c in med_cols]]).mean(axis=1))
    above = s.to_numpy() > 0
    t_med = med.to_numpy()
    t_thal = thal.to_numpy()
    acc = (above[:, t_med].sum(axis=1) + (~above[:, t_thal]).sum(axis=1)) / (t_med.sum() + t_thal.sum())
    vals = 1 - acc
    order = np.argsort(-vals, kind="stable")
    keep = np.zeros(len(genes), bool)
    keep[order[:n_genes]] = True
    keep[order[-n_genes:]] = True
    r = stats.pearsonr(sc_fc.to_numpy()[keep], bulk_fc.to_numpy()[keep])
    return {"r": float(r[0]), "p": float(r[1]), "genes": int(len(genes)), "kept": int(keep.sum()),
            "cells thal": int(t_thal.sum()), "cells med": int(t_med.sum()),
            "r all genes": float(stats.pearsonr(sc_fc, bulk_fc)[0])}


def read_axons() -> list:
    """Axons.zip: the MouseLight reconstructions (PTcells-MDhighlighted.mat), one object per
    axon ('-A') or dendrite ('-D'), each node with its structure in the Allen Common Coordinate
    Framework."""
    z = figshare_zip(FIGSHARE_AXONS_ZIP)
    m = sio.loadmat(io.BytesIO(z.read("Axons/PTcells-MDhighlighted.mat")), squeeze_me=True, struct_as_record=False)
    return list(np.atleast_1d(m["Session"].Neurons))


# AxonReconstructions.m: the 12 fully reconstructed neurons and their groups (1 medulla, 2 thalamus),
# the same as Supplementary data table 1 as the claims file gives it
AXON_GROUPS = {"AA0180": "medulla", "AA0179": "medulla", "AA0133": "medulla", "AA0012": "medulla",
               "AA0181": "thalamus", "AA0182": "thalamus", "AA0245": "thalamus", "AA0011": "thalamus",
               "AA0261": "thalamus", "AA0122": "thalamus", "AA0115": "thalamus", "AA0114": "thalamus"}


# Supplementary data table 1, as the claims file gives it (pt-types-account-for-all-pt): the six
# partially reconstructed PT neurons that, with the 12 above, make the paper's 18
AXON_PARTIAL = {"AA0132": "thalamus", "AA0135": "thalamus", "AA0250": "thalamus",
                "AA0131": "medulla", "AA0134": "medulla", "AA0169": "medulla"}


def axon_targets(neurons: list, structures: list[str]) -> pd.DataFrame:
    """Per axon reconstruction, the number of axon termini (nodes without children, as
    quantifyStructures) and the axon length (mm) in each named structure and its subdivisions."""
    names = {}
    for n in neurons:
        for a in np.atleast_1d(n.Anatomy):
            if isinstance(a.structureIdPath, str) and a.structureIdPath:
                names[a.safeName] = int(a.structureId)
    rows = []
    for n in neurons:
        if not n.Name.endswith("-A"):
            continue
        nodes = n.Nodes
        an = np.atleast_1d(n.Anatomy)
        ids = nodes[:, 4].astype(int)
        parents = nodes[:, 3].astype(int)
        ends = ~np.isin(ids, parents)
        where = {k: i for i, k in enumerate(ids)}
        par = np.array([where.get(p, -1) for p in parents])
        seg = np.where(par >= 0, np.linalg.norm(nodes[:, :3] - nodes[np.maximum(par, 0), :3], axis=1), 0.0) / 1000
        paths = [set(int(x) for x in a.structureIdPath.strip("/").split("/"))
                 if isinstance(a.structureIdPath, str) and a.structureIdPath else set() for a in an]
        row = {"neuron": n.Name[:-2], "soma": n.Location, "group": AXON_GROUPS.get(n.Name[:-2], "")}
        for s in structures:
            sid = names.get(s)
            inside = np.array([sid in p for p in paths]) if sid is not None else np.zeros(len(paths), bool)
            row[f"{s} termini"] = int((inside & ends).sum())
            row[f"{s} length"] = float(seg[inside].sum())
        rows.append(row)
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------------------------
# Per-unit measures, and the clock check of the data check

def unit_measures(u: dict, trial_range: str) -> dict:
    """One unit's measures under a reading of the trial range, all from the smoothed rates of
    its correct trials: the baseline rate (the mean over the two trial types of each type's mean
    rate in the baseline epoch) and the peak rate (the maximum of either type's trial-averaged
    rate; plotFiringRates); the two-sided rank-sum p between trial types in each epoch, and in the
    full sample epoch (-2.5 to -1.5 s); the d' in the CDearly window; the single-unit decoding
    accuracy and its d' in the sample epoch (decodingAccuracy.m), and the accuracy with rates
    rectified at the baseline (signConstraint 1)."""
    rl, rr = trial_rows(u, trial_range)
    out = {"n_left": len(rl), "n_right": len(rr)}
    al, ar = average_rate(u["go"], rl), average_rate(u["go"], rr)
    bl, br = (trial_means(u["go"], r, EPOCHS["baseline"]) for r in (rl, rr))
    base = (bl.mean() + br.mean()) / 2
    out["baseline rate"] = base
    out["peak rate"] = float(max(al.max(), ar.max()))
    for name, window in {**EPOCHS, "full sample": (-2.5, -1.5)}.items():
        out[f"p {name}"] = ranksum_p(trial_means(u["go"], rl, window), trial_means(u["go"], rr, window))
    xl, xr = (trial_means(u["go"], r, CD_WINDOWS["early"], "cd") for r in (rl, rr))
    out["early d'"] = dprime(xl, xr)
    sl, sr = (trial_means(u["go"], r, EPOCHS["sample"]) for r in (rl, rr))
    out["accuracy"], out["roc d'"] = roc(sl, sr)
    out["rectified accuracy"], _ = roc(np.maximum(sl - base, 0), np.maximum(sr - base, 0))
    return out


def epoch_rates(spikes: np.ndarray, cue_abs: np.ndarray, window: tuple[float, float]) -> np.ndarray:
    """Spikes per second in `window` (seconds from the go cue) for each trial (raw counts)."""
    a, b = window
    lo = np.searchsorted(spikes, cue_abs + a, side="left")
    hi = np.searchsorted(spikes, cue_abs + b, side="left")
    return (hi - lo) / (b - a)


def decode_direction(session: dict, window: tuple[float, float], shift: int = 0) -> tuple[float, int]:
    """Leave-one-out nearest-centroid accuracy of lick direction on correct trials, from the
    rates of every unit of the session in `window` (seconds from the go cue), z-scored with the
    training trials. `shift` takes each trial's label from the trial `shift` rows later. Trials
    from the eleventh onward. A check of the clock, not a method of the paper."""
    t = session["trials"]
    labels = np.roll(t.type.to_numpy() == "lick right", -shift)
    keep = correct_trials(t) & (np.arange(len(t)) >= EDGE_TRIALS)
    if shift:
        keep &= np.arange(len(t)) < len(t) - shift
    cue = t.cue_abs.to_numpy()[keep]
    y = labels[keep]
    raw = np.column_stack([epoch_rates(np.sort(sp_), cue, window) for sp_ in session["units"].spikes])
    correct = 0
    for i in range(len(y)):
        others = np.ones(len(y), bool)
        others[i] = False
        mu, sd = raw[others].mean(axis=0), raw[others].std(axis=0)
        x = (raw - mu) / np.where(sd > 0, sd, 1)
        c1 = x[others & y].mean(axis=0)
        c0 = x[others & ~y].mean(axis=0)
        guess = np.sum((x[i] - c1) ** 2) < np.sum((x[i] - c0) ** 2)
        correct += guess == y[i]
    return correct / len(y), len(y)
