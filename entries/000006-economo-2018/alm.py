"""Loading and measures for the ALM recordings of dandiset 000006.

Economo, Viswanathan, Tasic et al. (2018), Nature, doi:10.1038/s41586-018-0642-9.

Each NWB file (NWB 2.0.2) holds one session of one mouse in a delayed response task: a trial
table (`start_time` in seconds on the session clock; `pole_in_time`, `pole_out_time` and
`cue_start_time` in seconds from the trial start; `type` lick left or lick right; `response`
correct, incorrect, early lick or no response; `is_good`; `stim_present`), the times of left and
right licks, and a units table with spike times. Tagged pyramidal tract units have ids above 1000
and `cell_type` PTupper or PTlower; the other units are `unidentified`. Files are streamed from
the archive at the pinned version; nothing is written to disk.

Where the parameters come from. The paper's Methods were not available (the paper is not open
access). Every choice below follows the analysis code the paper links to, the MATLAB scripts in
Ephys.zip of the Figshare record doi:10.25378/janelia.7007846 (version 1):

- `EPOCHS`, in seconds from the go cue: defineDataset.m.
- `GOOD_QUALITY`, `MIN_CORRECT`, `MIN_SPIKES_PER_TRIAL`, `MIN_PERFORMANCE` and `EDGE_TRIALS`:
  loadAndProcessData.m (unit inclusion, and the trial range of each unit in ObjToLickPSTH).
  The code counts spikes per trial over the range of trials in which the unit fired.
- `SELECTIVITY_P`: simplePlots.m (sigCellsByType), a rank-sum test of trial rates between
  correct lick-left and lick-right trials.
- `dprime`: the coding direction weights of Projections.m and CDCorrelation.m, mean right minus
  mean left over the root of the summed variances.
- The code averages a causally smoothed PSTH (5 ms bins, a 50 ms box) over each epoch; here the
  epoch rate is the spike count in the epoch divided by its length, which differs only by that
  smoothing.
"""

from __future__ import annotations

import io
import zipfile
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
import scipy.io as sio
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
        }
    hemisphere = location.split("hemisphere:")[1].split(";")[0].strip()
    return {"path": path, "subject": subject, "session": path.split("_ses-")[1][:8],
            "trials": trials, "units": units, "licks": licks, "hemisphere": hemisphere,
            "location": location, "meta": meta}


def load_all(max_workers: int = 8) -> list[dict]:
    urls = asset_urls()
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        return list(pool.map(lambda pu: load_session(*pu), urls))


def trial_of_spikes(spikes: np.ndarray, trials: pd.DataFrame) -> np.ndarray:
    """Index of the trial each spike falls in (from one trial start to the next), -1 before
    the first trial."""
    return np.searchsorted(trials.start.to_numpy(), spikes, side="right") - 1


def epoch_rates(spikes: np.ndarray, cue_abs: np.ndarray, window: tuple[float, float]) -> np.ndarray:
    """Spikes per second in `window` (seconds from the go cue) for each trial."""
    a, b = window
    lo = np.searchsorted(spikes, cue_abs + a, side="left")
    hi = np.searchsorted(spikes, cue_abs + b, side="left")
    return (hi - lo) / (b - a)


def correct_trials(trials: pd.DataFrame, exclude_bad: bool = False) -> pd.Series:
    """Correct trials without early licks or photostimulation (the code's
    'hit&~lickearly&~stim'); `exclude_bad` also drops trials with is_good False."""
    keep = (trials.response == "correct") & ~trials.stim
    if exclude_bad:
        keep &= trials.is_good
    return keep


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


def unit_record(session: dict, unit: pd.Series, exclude_bad: bool = False,
                drop_overlap: bool = False) -> dict:
    """Apply the code's inclusion rule to one unit and collect its trial rates per epoch.
    `drop_overlap` leaves out the spikes `overlap_flags` marks."""
    trials = session["trials"]
    raw = np.asarray(unit.spikes)
    spikes = np.sort(raw[~overlap_flags(raw)] if drop_overlap else raw)
    spk_trial = trial_of_spikes(spikes, trials)
    in_trial = spk_trial[spk_trial >= 0]
    rec = {"subject": session["subject"], "session": session["session"], "path": session["path"],
           "hemisphere": session["hemisphere"], "id": int(unit.id), "cell_type": unit.cell_type,
           "quality": unit.quality, "depth": float(unit.depth), "n_spikes": len(spikes)}
    if len(in_trial) == 0:
        rec.update(included=False, reason="no spikes in trials")
        return rec
    first, last = int(in_trial.min()), int(in_trial.max())
    correct = correct_trials(trials, exclude_bad)
    last_hit = int(np.flatnonzero(trials.response.to_numpy() == "correct").max())
    lo, hi = first + EDGE_TRIALS, min(last, last_hit) - EDGE_TRIALS
    idx = np.arange(len(trials))
    in_range = (idx >= lo) & (idx <= hi)
    # The code divides by range(eventTrials), the last trial with a spike minus the first.
    rec["spikes_per_trial"] = len(in_trial) / max(last - first, 1)
    scored = in_range & (trials.response != "early lick").to_numpy() & ~trials.stim.to_numpy()
    if exclude_bad:
        scored &= trials.is_good.to_numpy()
    for side, label in (("L", "lick left"), ("R", "lick right")):
        of_side = scored & (trials.type == label).to_numpy()
        hits = of_side & correct.to_numpy()
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
    use = in_range & correct.to_numpy()
    cue = trials.cue_abs.to_numpy()[use]
    rec["is_right"] = (trials.type.to_numpy()[use] == "lick right")
    rec["rates"] = {name: epoch_rates(spikes, cue, w) for name, w in EPOCHS.items()}
    rec["cue"] = cue
    rec["spike_times"] = spikes
    return rec


def tagged_units(sessions: list[dict], exclude_bad: bool = False,
                 drop_overlap: bool = False) -> list[dict]:
    """The record of every tagged unit (cell_type PTupper or PTlower) in every session."""
    out = []
    for s in sessions:
        for _, unit in s["units"].iterrows():
            if unit.cell_type in TYPES:
                out.append(unit_record(s, unit, exclude_bad, drop_overlap))
    return out


def label_shuffles(n_trials: int, n: int, rng: np.random.Generator) -> np.ndarray:
    """`n` random orders of `n_trials` trials, one per row."""
    return np.argsort(rng.random((n, n_trials)), axis=1)


def shuffled_dprime(rates: np.ndarray, is_right: np.ndarray, perms: np.ndarray) -> np.ndarray:
    """`dprime` for each row of `perms`."""
    labels = is_right[perms]
    n_r = labels.sum(axis=1)
    n_l = labels.shape[1] - n_r
    r = rates[None, :]
    mu_r = np.where(labels, r, 0).sum(axis=1) / n_r
    mu_l = np.where(~labels, r, 0).sum(axis=1) / n_l
    var_r = (np.where(labels, r, 0) ** 2).sum(axis=1) / n_r - mu_r ** 2
    var_l = (np.where(~labels, r, 0) ** 2).sum(axis=1) / n_l - mu_l ** 2
    var_r *= n_r / (n_r - 1)
    var_l *= n_l / (n_l - 1)
    den = np.sqrt(np.maximum(var_r + var_l, 0))
    return np.where(den > 0, (mu_r - mu_l) / np.where(den > 0, den, 1), 0.0)


def decode_direction(session: dict, window: tuple[float, float], shift: int = 0) -> tuple[float, int]:
    """Leave-one-out nearest-centroid accuracy of lick direction on correct trials, from the
    rates of every unit of the session in `window` (seconds from the go cue). `shift` takes each
    trial's label from the trial `shift` rows later. Trials from the eleventh onward."""
    t = session["trials"]
    labels = np.roll(t.type.to_numpy() == "lick right", -shift)
    keep = correct_trials(t).to_numpy() & (np.arange(len(t)) >= EDGE_TRIALS)
    if shift:
        keep &= np.arange(len(t)) < len(t) - shift
    cue = t.cue_abs.to_numpy()[keep]
    y = labels[keep]
    raw = np.column_stack([epoch_rates(np.sort(sp), cue, window) for sp in session["units"].spikes])
    correct = 0
    for i in range(len(y)):
        others = np.ones(len(y), bool)
        others[i] = False
        # z-score with the mean and spread of the training trials only
        mu, sd = raw[others].mean(axis=0), raw[others].std(axis=0)
        x = (raw - mu) / np.where(sd > 0, sd, 1)
        c1 = x[others & y].mean(axis=0)
        c0 = x[others & ~y].mean(axis=0)
        guess = np.sum((x[i] - c1) ** 2) < np.sum((x[i] - c0) ** 2)
        correct += guess == y[i]
    return correct / len(y), len(y)


def ranksum_p(rates: np.ndarray, is_right: np.ndarray) -> float:
    """Two-sided Wilcoxon rank-sum p, with tie and continuity corrections (as MATLAB ranksum's
    approximate method, which it uses at these trial counts)."""
    x, y = rates[~is_right], rates[is_right]
    if np.ptp(rates) == 0:
        return 1.0
    return float(stats.mannwhitneyu(x, y, alternative="two-sided", method="asymptotic").pvalue)


def shuffled_ranksum_p(rates: np.ndarray, is_right: np.ndarray, perms: np.ndarray) -> np.ndarray:
    """Rank-sum p for each row of `perms`, a (n_shuffles, n_trials) array of trial orders that
    shuffle the labels."""
    labels = is_right[perms]
    if np.ptp(rates) == 0:
        return np.ones(len(perms))
    r = stats.rankdata(rates)
    n1 = (~is_right).sum()
    n2 = is_right.sum()
    # U of the left trials under each shuffle, and the normal approximation with ties
    rank_left = np.where(~labels, r[None, :], 0.0).sum(axis=1)
    u = rank_left - n1 * (n1 + 1) / 2
    _, counts = np.unique(rates, return_counts=True)
    n = n1 + n2
    tie = (counts ** 3 - counts).sum() / (n * (n - 1))
    sd = np.sqrt(n1 * n2 / 12 * ((n + 1) - tie))
    z = (np.abs(u - n1 * n2 / 2) - 0.5) / sd
    return 2 * stats.norm.sf(np.maximum(z, 0))


def dprime(rates: np.ndarray, is_right: np.ndarray) -> float:
    """(mean right - mean left) / sqrt(var left + var right), 0 when undefined (the code)."""
    x, y = rates[~is_right], rates[is_right]
    den = np.sqrt(x.var(ddof=1) + y.var(ddof=1))
    return float((y.mean() - x.mean()) / den) if den > 0 else 0.0


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    return float(a @ b / (na * nb)) if na > 0 and nb > 0 else np.nan


def null_p(observed: float, null: np.ndarray) -> float:
    """One-sided p of `observed` against a null sample: (1 + #null >= observed) / (1 + n)."""
    return float((1 + np.sum(null >= observed)) / (1 + len(null)))


def mcnemar_one_sided(first_only: int, second_only: int) -> float:
    """Exact one-sided McNemar p that the second condition is more often positive."""
    n = first_only + second_only
    return float(stats.binomtest(second_only, n, 0.5, alternative="greater").pvalue) if n else 1.0


def roc_accuracy(rates: np.ndarray, is_right: np.ndarray) -> float:
    """Single-unit decoding accuracy of trial type, as doROC.m and decodingAccuracy.m
    (Extended Data Fig. 9): the best fraction of trials classified correctly by one threshold
    on the trial rates, with the polarity chosen by the area under the ROC curve."""
    thresholds = np.unique(rates)
    above = rates[None, :] >= thresholds[:, None]
    n_r, n_l = is_right.sum(), (~is_right).sum()
    tp = (above & is_right).sum(axis=1) / n_r
    fp = (above & ~is_right).sum(axis=1) / n_l
    auc = abs(np.trapezoid(tp, fp))
    right_high = ((above & is_right).sum(axis=1) + (~above & ~is_right).sum(axis=1)) / len(rates)
    right_low = ((above & ~is_right).sum(axis=1) + (~above & is_right).sum(axis=1)) / len(rates)
    return float((right_high if auc >= 0.5 else right_low).max())


# The paper's processed data, Ephys.zip of doi:10.25378/janelia.7007846 (version 1), file
# 13292708. One file per animal and recording period (two for anm369962 and anm369963), each
# holding several sessions. Read in the data check to show how the files' spike times were
# built and which of the paper's units the dandiset holds, and in variants that rerun the
# tests on the paper's units.
FIGSHARE_EPHYS_ZIP = "https://ndownloader.figshare.com/files/13292708"
FIGSHARE_CHECK_FILE = "Code/ProcessedData/data_structure_anm372906_WR40_psth.mat"
# defineDataset.m: group 1 ("MP", medulla-projecting) holds these animals, group 2 ("TP") the rest
MP_ANIMALS = ("anm369962", "anm369963", "anm369964", "anm372794")


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


def read_figshare_processed(member: str = FIGSHARE_CHECK_FILE) -> dict:
    """Read one processed .mat file from the paper's Ephys.zip by range requests, in memory."""
    url = requests.head(FIGSHARE_EPHYS_ZIP, allow_redirects=True, timeout=60).url
    with zipfile.ZipFile(_Seekable(remfile.File(url))) as z:
        data = z.read(member)
    return sio.loadmat(io.BytesIO(data), squeeze_me=True, struct_as_record=False)


def compare_with_processed(session: dict, mat: dict, index: int = 0) -> tuple[pd.DataFrame, pd.DataFrame]:
    """For session `index` of a processed file: per unit, whether the file's spike times equal
    trial start + go cue + the processed cue-relative spike time, in stored order; and per
    trial, the span of the processed spike times (pooled over units) relative to the go cue."""
    t = session["trials"]
    cue_abs = t.cue_abs.to_numpy()
    obj, meta = mat["obj"][index], mat["meta"][index]
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
    spans = pd.DataFrame({"first": lo, "last": hi, "pole_in": (t.pole_in - t.cue).to_numpy(),
                          "start_spacing": np.r_[np.diff(t.start.to_numpy()), np.nan]})
    return pd.DataFrame(rows), spans


def processed_members() -> list[str]:
    """Names of the processed data files in Ephys.zip."""
    url = requests.head(FIGSHARE_EPHYS_ZIP, allow_redirects=True, timeout=60).url
    with zipfile.ZipFile(_Seekable(remfile.File(url))) as z:
        return sorted(n for n in z.namelist() if n.endswith("_psth.mat"))


def processed_session_units(mat: dict, index: int, member: str) -> list[dict]:
    """The code's inclusion rule (loadAndProcessData.m, ObjToLickPSTH) applied to the tagged
    units of session `index` of a processed file, with each unit's epoch rates on its correct
    trials. Spike times in the processed data are seconds from the go cue, with the trial of
    each spike (1-based)."""
    obj, meta, tt = (np.atleast_1d(mat[k])[index] for k in ("obj", "meta", "tt"))
    subject = member.split("data_structure_")[1].split("_")[0]
    session = str(meta.filename).split("_")[-1].split(".")[0].replace("-", "")
    hit, left, right = (np.asarray(getattr(tt, k), bool) for k in ("hit", "L", "R"))
    scored = ~np.asarray(tt.lickearly, bool) & ~np.asarray(tt.stim, bool)
    trial_no = np.arange(1, len(hit) + 1)
    last_hit = trial_no[hit].max()
    numbers = np.atleast_1d(meta.unitNum)
    quality = np.atleast_1d(meta.unitQuality)
    depth = np.atleast_1d(meta.depth)
    out = []
    for j, number in enumerate(numbers):
        if not 1000 < number < 2000:
            continue
        unit = np.atleast_1d(obj.eventSeriesHash.value)[j]
        times = np.atleast_1d(unit.eventTimes).astype(float)
        trials = np.atleast_1d(unit.eventTrials).astype(int)
        first, last = max(trials.min(), 1), trials.max()
        in_range = (trial_no >= first + EDGE_TRIALS) & (trial_no <= min(last, last_hit) - EDGE_TRIALS)
        rec = {"subject": subject, "session": session, "id": int(number),
               "cell_type": "PTlower" if subject in MP_ANIMALS else "PTupper",
               "quality": str(quality[j]), "depth": float(depth[j]),
               "spikes_per_trial": len(times) / max(np.ptp(trials), 1)}
        for side, of_side in (("L", left), ("R", right)):
            hits = in_range & scored & of_side & hit
            misses = in_range & scored & of_side & ~hit
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
        use = in_range & scored & hit & (left | right)
        rec["is_right"] = right[use]
        rec["rates"] = {}
        for name, (a, b) in EPOCHS.items():
            inside = (times >= a) & (times < b)
            counts = np.bincount(trials[inside], minlength=len(hit) + 1)[1:]
            rec["rates"][name] = counts[use] / (b - a)
        out.append(rec)
    return out


def read_processed(sessions: list[dict]) -> tuple[list[dict], pd.DataFrame, pd.DataFrame]:
    """Read every processed file. Returns the tagged unit records of every processed session
    (`processed_session_units`); per unit of every session also in the dandiset, whether the
    file's spike times equal trial start + go cue + the processed time in stored order; and per
    such session, the start of the processed spike windows relative to the pole coming in, for
    the first ten trials and for the others."""
    by_key = {(s["subject"], s["session"]): s for s in sessions}
    records, storage, shifts = [], [], []
    for member in processed_members():
        mat = read_figshare_processed(member)
        for i in range(len(np.atleast_1d(mat["meta"]))):
            recs = processed_session_units(mat, i, member)
            meta = np.atleast_1d(mat["meta"])[i]
            subject = member.split("data_structure_")[1].split("_")[0]
            session = str(meta.filename).split("_")[-1].split(".")[0].replace("-", "")
            s = by_key.get((subject, session))
            for r in recs:
                r["in_dandiset"] = s is not None
            records.extend(recs)
            if s is None:
                continue
            per_unit, spans = compare_with_processed(s, mat, i)
            storage.append(per_unit.assign(subject=subject, session=session))
            offset = (spans["first"] - spans["pole_in"]).replace([np.inf, -np.inf], np.nan)
            shifts.append({"subject": subject, "session": session, "trials": len(spans),
                           "first 10: first - pole_in": offset.iloc[:EDGE_TRIALS].median(),
                           "others: first - pole_in": offset.iloc[EDGE_TRIALS:].median()})
        del mat
    return records, pd.concat(storage, ignore_index=True), pd.DataFrame(shifts)
