"""Loading and measures for dandiset 000232 (Chang, Finkel, Xu & O'Connor, cross-modal selection task).

Chang Y-T, Finkel EA, Xu D, O'Connor DH. Rule-based modulation of a sensorimotor transformation
across cortical areas. bioRxiv doi:10.1101/2023.08.21.554194 (version 2, March 2024).

The dandiset holds three kinds of NWB file, all streamed here from the archive at the pinned
version; nothing is written to disk:

- 49 silicon-probe sessions (`*_behavior+ecephys.nwb`) of the cross-modal selection task, one
  cortical area per session (S1, S2, MM, ALM, AMM; named in `experiment_description` and in the
  electrode group's `location`). Each holds a trials table and a Units table of spike times.
- 112 optogenetic sessions of the cross-modal task and 29 of a tactile detection task
  (`*_behavior.nwb`), with a trials table that includes laser onsets and offsets.

Trial coding (checked against the data in the notebook): `blockType` "Whisker" is the
respond-to-touch block, "Visual" the respond-to-light block and "Change" the cue trial (water on
the 9th trial of a block), which the paper's code leaves out of every analysis. `response` is 1
for a right lick, 2 for a left lick and 0 for no lick (3 appears only on trials without a
stimulus). A tactile trial has `somOnset_times`, a visual trial `visOnset_times`. In the
behaviour files `start_time` equals the stimulus onset; lick times are absolute and cover the
inter-trial interval before it.

Where the parameters come from:

- Methods of the paper (preprint v2): 10 ms bins smoothed with a 50 ms Gaussian kernel for
  stimulus-evoked activity, 100 ms bins without smoothing for pre-stimulus activity; soft
  normalization (x - mean) / (range + 5) for population analyses; the analysis windows of
  each figure; Bonferroni-corrected bootstrap confidence intervals on AUC; LDA with ten-fold
  cross-validation; top three principal components; hierarchical bootstrap over mice,
  sessions and trials for the optogenetic results.
- The paper's analysis code, https://github.com/YitingChang/cross_modal_task at commit
  227631ee133709df979b9914c9031cfa992c3736, where the Methods leave a choice open: the
  smoothing kernel is MATLAB `smoothdata(..., 'gaussian', 5)` on 10 ms bins (`GAUSS_WINDOW`;
  MATLAB sets the kernel's standard deviation to a fifth of the window); 1000 bootstrap
  resamples of each class for AUC, with the Bonferroni interval read off the sorted
  resamples at ceil(a * n) and ceil((1 - a) * n), a = 0.05 / (2 * number of neurons in the
  area); a unit is tHit-tCR selective when 3 consecutive 10 ms bins are significant; LDA is
  MATLAB `fitcdiscr(..., 'diaglinear')` (`DiagLDA`); the laser timing that marks pre- and
  post-stimulus inhibition, and the lick windows of the optogenetic analysis (`opto_licks`).
"""

from __future__ import annotations

import math
import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000232"
DANDISET_VERSION = "0.240510.2038"

AREAS = ["S1", "S2", "MM", "ALM"]
GAUSS_WINDOW = 5            # bins; code: smoothdata(..., 'gaussian', 5) on 10 ms bins
SOFT_NORM_OFFSET = 5.0      # Methods: (x - mean) / (range + 5)

# Trial categories of the paper's code: block (1 touch, 2 light), stimulus (1 tactile, 2 visual),
# decision (1 right, 2 left, 3 no lick).
CATEGORIES = {(b, s, d): f"{'TV'[b - 1]}{'TV'[s - 1]}{'TVN'[d - 1]}"
              for b in (1, 2) for s in (1, 2) for d in (1, 2, 3)}
T_HIT, T_CR, V_HIT, V_CR = (1, 1, 1), (2, 1, 3), (2, 2, 2), (1, 2, 3)


# --- loading -----------------------------------------------------------------------------------

def asset_urls() -> pd.DataFrame:
    """Path, size and streaming URL of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = [{"path": a.path, "size": a.size,
                 "url": a.get_content_url(follow_redirects=1, strip_query=True)}
                for a in dandiset.get_assets() if a.path.endswith(".nwb")]
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def _text(value) -> str:
    value = value[()] if hasattr(value, "shape") else value
    if isinstance(value, bytes):
        return value.decode()
    if isinstance(value, np.ndarray):
        return ",".join(_text(v) for v in value)
    return str(value)


def _ragged(group, name: str, n: int) -> list[np.ndarray]:
    if name not in group:
        return [np.array([])] * n
    data, index = group[name][:], group[name + "_index"][:]
    return np.split(data, index[:-1].astype(int))


def _column(group, name: str, n: int) -> np.ndarray:
    return group[name][:] if name in group else np.full(n, np.nan)


def load_file(path: str, url: str, spikes: bool = True) -> dict:
    """Read one file: session metadata, the trials table and, for ephys files, spike times."""
    with h5py.File(remfile.File(url), "r") as f:
        description = _text(f["general/experiment_description"])
        subject = f["general/subject"]
        out = {
            "path": path,
            "description": description,
            "session": _text(f["session_description"]),
            "session_start": _text(f["session_start_time"]),
            "subject": _text(subject["subject_id"]),
            "genotype": _text(subject["genotype"]) if "genotype" in subject else "",
            "sex": _text(subject["sex"]) if "sex" in subject else "",
            "date_of_birth": _text(subject["date_of_birth"]) if "date_of_birth" in subject else "",
        }
        t = f["intervals/trials"]
        n = len(t["id"])
        trials = pd.DataFrame({
            "start": t["start_time"][:], "stop": t["stop_time"][:],
            "block_type": [_text(v) for v in t["blockType"][:]],
            "trial_type": [_text(v) for v in t["trialType"][:]],
            "response": t["response"][:],
            "som_on": _column(t, "somOnset_times", n), "vis_on": _column(t, "visOnset_times", n),
            "stim_on": t["stimOnset_times"][:], "first_lick": _column(t, "firstLick_times", n),
            "opto_on": _column(t, "optoOnset_times", n), "opto_off": _column(t, "optoOffset_times", n),
            "vis_stim_type": [_text(v) for v in t["visStimType"][:]],
            "som_stim_type": [_text(v) for v in t["somStimType"][:]],
        })
        trials["r_licks"] = _ragged(t, "rLickOnset_times", n)
        trials["l_licks"] = _ragged(t, "lLickOnset_times", n)
        out["trial_columns"] = list(t.attrs["colnames"])
        out["trials"] = trials
        out["kind"] = "ephys" if "units" in f else "opto"
        if out["kind"] == "ephys":
            out["area"] = re.search(r"recording of (\S+) during", description).group(1)
            out["group_location"] = _text(
                f["general/extracellular_ephys/electrode_group"].attrs["location"])
            out["electrode_locations"] = sorted({_text(v) for v in
                                                 f["general/extracellular_ephys/electrodes/location"][:]})
            e = f["general/extracellular_ephys/electrodes"]
            out["electrode_xyz_all_nan"] = bool(np.isnan(np.r_[e["x"][:], e["y"][:], e["z"][:]]).all())
            out["unit_ids_head"] = f["units/id"][:5].tolist()
            out["unit_columns"] = list(f["units"].attrs["colnames"])
            out["n_units"] = len(f["units/id"])
            if spikes:
                out["spikes"] = _ragged(f["units"], "spike_times", out["n_units"])
                obs = f["units/obs_intervals"][:]
                obs_index = f["units/obs_intervals_index"][:].astype(int)
                out["obs_intervals"] = np.split(obs, obs_index[:-1])
            out["has_lfp"] = "processing/ecephys/LFP" in f
        else:
            m = re.search(r"inhibition of (\S+) during", description)
            out["condition"] = m.group(1) if m else "sham"
            out["task"] = "detection" if "tactile detection" in description else "cross-modal"
    return out


def load_all(assets: pd.DataFrame, spikes: bool = True, workers: int = 16) -> list[dict]:
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(lambda r: load_file(r.path, r.url, spikes), assets.itertuples()))


# --- trial coding ------------------------------------------------------------------------------

def code_trials(trials: pd.DataFrame) -> pd.DataFrame:
    """Add block (b), stimulus (s) and decision (d) codes; cue ("Change") trials get b = 0."""
    t = trials.copy()
    t["b"] = t.block_type.map({"Whisker": 1, "Visual": 2}).fillna(0).astype(int)
    t["s"] = np.where(t.som_on.notna(), 1, np.where(t.vis_on.notna(), 2, 0))
    t["d"] = t.response.map({1.0: 1, 2.0: 2, 0.0: 3}).fillna(0).astype(int)
    t["category"] = [CATEGORIES.get((b, s, d), "") if b and s and d else ""
                     for b, s, d in zip(t.b, t.s, t.d)]
    return t


def estimated_trial_numbers(trials: pd.DataFrame) -> np.ndarray:
    """Estimated position of each row in the session's full trial sequence, counting from 0.

    The ephys files lack the trials the paper removed, and have no trial numbers. Kept trials abut
    (one's stop is the next one's start), so a gap of more than 10 ms between rows marks removed
    trials; their number is estimated as the gap over the median trial duration, rounded, and at
    least 1. Trials removed after the last row cannot be seen.
    """
    start, stop = trials.start.to_numpy(), trials.stop.to_numpy()
    gaps = start[1:] - stop[:-1]
    dur = np.median(stop - start)
    removed = np.where(gaps > 0.01, np.maximum(1, np.round(gaps / dur)), 0)
    return np.arange(len(trials)) + np.r_[0, np.cumsum(removed)].astype(int)


def is_category(t: pd.DataFrame, cat: tuple) -> np.ndarray:
    return ((t.b == cat[0]) & (t.s == cat[1]) & (t.d == cat[2])).to_numpy()


def licks_in(t: pd.DataFrame, lo: float, hi: float, side: str = "both", ref: str = "stim_on") -> np.ndarray:
    """Whether a lick onset falls in (lo, hi) seconds from each trial's reference time."""
    out = np.zeros(len(t), bool)
    for i, (r, l, t0) in enumerate(zip(t.r_licks, t.l_licks, t[ref])):
        licks = r if side == "right" else l if side == "left" else np.concatenate([r, l])
        out[i] = np.any((licks - t0 > lo) & (licks - t0 < hi))
    return out


# --- firing rates ------------------------------------------------------------------------------

def binned_rates(spikes: list[np.ndarray], onsets: np.ndarray, t0: float, t1: float,
                 width: float) -> np.ndarray:
    """Spike rates (Hz), shape (trials, units, bins), in bins of `width` from t0 to t1 s of each onset."""
    nb = int(round((t1 - t0) / width))
    edges = onsets[:, None] + t0 + width * np.arange(nb + 1)[None, :]
    out = np.empty((len(onsets), len(spikes), nb))
    for u, st in enumerate(spikes):
        idx = np.searchsorted(st, edges.ravel(), side="left").reshape(edges.shape)
        out[:, u, :] = np.diff(idx, axis=1)
    return out / width


def gauss_smooth(x: np.ndarray, window: int = GAUSS_WINDOW) -> np.ndarray:
    """Gaussian moving average along the last axis, as MATLAB smoothdata(x, 'gaussian', window).

    The kernel spans `window` bins with standard deviation window / 5; at the ends the kernel is
    truncated and renormalized.
    """
    half = (window - 1) / 2
    offsets = np.arange(-math.floor(half), math.ceil(half) + 1)
    w = np.exp(-0.5 * (offsets / (window / 5)) ** 2)
    num = np.zeros_like(x, dtype=float)
    den = np.zeros(x.shape[-1])
    n = x.shape[-1]
    for k, wk in zip(offsets, w):
        lo, hi = max(0, -k), min(n, n - k)
        num[..., lo:hi] += wk * x[..., lo + k:hi + k]
        den[lo:hi] += wk
    return num / den


def soft_normalize(x: np.ndarray, reference: np.ndarray, offset: float = SOFT_NORM_OFFSET,
                   axis_units: int = 0) -> np.ndarray:
    """(x - mean) / (range + offset) per unit, with mean and range taken from `reference`.

    `reference` has units on its first axis; any other axes are pooled.
    """
    ref = reference.reshape(reference.shape[0], -1)
    mean, rng_ = np.nanmean(ref, axis=1), np.nanmax(ref, axis=1) - np.nanmin(ref, axis=1)
    shape = [1] * x.ndim
    shape[axis_units] = -1
    return (x - mean.reshape(shape)) / (rng_.reshape(shape) + offset)


# --- ideal observer ----------------------------------------------------------------------------

def bootstrap_auc(pos: np.ndarray, neg: np.ndarray, n_boot: int, rng: np.random.Generator,
                  chunk: int = 64) -> np.ndarray:
    """Bootstrap distribution of the AUC (pos against neg), shape (n_boot, features).

    pos (n1, features) and neg (n2, features). Each resample draws n1 positive and n2 negative
    trials with replacement, as the code's `bootstrp`; the same resampled trials serve every
    feature (unit and bin) of a session. AUC counts ties as one half (MATLAB perfcurve).
    """
    n1, n2 = len(pos), len(neg)
    w1 = rng.multinomial(n1, np.full(n1, 1 / n1), size=n_boot).astype(float)
    w2 = rng.multinomial(n2, np.full(n2, 1 / n2), size=n_boot).astype(float)
    out = np.empty((n_boot, pos.shape[1]))
    for k0 in range(0, pos.shape[1], chunk):
        p, q = pos[:, k0:k0 + chunk], neg[:, k0:k0 + chunk]
        c = (p[:, None, :] > q[None, :, :]) + 0.5 * (p[:, None, :] == q[None, :, :])  # n1, n2, K
        tmp = np.einsum("bi,ijk->bjk", w1, c)
        out[:, k0:k0 + chunk] = np.einsum("bjk,bj->bk", tmp, w2) / (n1 * n2)
    return out


def bonferroni_significant(boot: np.ndarray, n_tests: int, alpha: float = 0.05) -> np.ndarray:
    """Whether the Bonferroni-corrected bootstrap interval excludes 0.5, as the code reads it."""
    n = boot.shape[0]
    a = alpha / n_tests / 2
    srt = np.sort(boot, axis=0)
    lo = srt[max(math.ceil(a * n), 1) - 1]
    hi = srt[max(math.ceil((1 - a) * n), 1) - 1]
    return (0.5 - lo) * (0.5 - hi) > 0


def consecutive(sig: np.ndarray, k: int = 3) -> np.ndarray:
    """Whether each row of a boolean (units, bins) array has k consecutive True values."""
    run = np.zeros(sig.shape[0], int)
    best = np.zeros(sig.shape[0], int)
    for j in range(sig.shape[1]):
        run = np.where(sig[:, j], run + 1, 0)
        best = np.maximum(best, run)
    return best >= k


# --- decoding ----------------------------------------------------------------------------------

class DiagLDA:
    """Linear discriminant with a diagonal pooled covariance (MATLAB fitcdiscr 'diaglinear').

    Priors are the class frequencies of the training set; the pooled variance divides the
    within-class sum of squares by n - (number of classes). Neurons with zero variance in the
    training set are left out of the fit.
    """

    def fit(self, x: np.ndarray, y: np.ndarray) -> "DiagLDA":
        self.classes = np.unique(y)
        self.means = np.array([x[y == c].mean(axis=0) for c in self.classes])
        resid = x - self.means[np.searchsorted(self.classes, y)]
        dof = max(len(y) - len(self.classes), 1)
        self.var = (resid ** 2).sum(axis=0) / dof
        self.use = self.var > 0          # a neuron silent in every training trial carries no information
        self.logprior = np.log(np.array([(y == c).mean() for c in self.classes]))
        return self

    def log_posterior(self, x: np.ndarray) -> np.ndarray:
        u = self.use
        ll = -0.5 * (((x[:, None, u] - self.means[None][:, :, u]) ** 2) / self.var[u]).sum(axis=2)
        lp = ll + self.logprior
        return lp - np.logaddexp.reduce(lp, axis=1, keepdims=True)

    def predict(self, x: np.ndarray) -> np.ndarray:
        return self.classes[np.argmax(self.log_posterior(x), axis=1)]


def stratified_folds(y: np.ndarray, k: int, rng: np.random.Generator) -> np.ndarray:
    """Fold index per observation, balanced within each class (as MATLAB cvpartition)."""
    folds = np.empty(len(y), int)
    for c in np.unique(y):
        idx = np.flatnonzero(y == c)
        folds[rng.permutation(idx)] = np.arange(len(idx)) % k
    return folds


def usable_features(x: np.ndarray) -> np.ndarray:
    """Features with non-zero variance (the code rounds the variance to 6 decimals)."""
    return np.round(x.var(axis=0, ddof=1), 6) > 0


def cv_accuracy(x: np.ndarray, y: np.ndarray, rng: np.random.Generator, k: int = 10,
                make_model=DiagLDA) -> float:
    """Ten-fold cross-validated accuracy (correct predictions over all observations)."""
    x = x[:, usable_features(x)]
    folds = stratified_folds(y, k, rng)
    correct = 0
    for f in range(k):
        test = folds == f
        if not test.any():
            continue
        model = make_model().fit(x[~test], y[~test])
        correct += (model.predict(x[test]) == y[test]).sum()
    return correct / len(y)


# --- block transitions -------------------------------------------------------------------------

def transition_info(t: pd.DataFrame) -> pd.DataFrame:
    """Port of the code's GetTransitionInfo and GetFirstHitInfo on the trials of one session.

    Cue trials take the block of the trial before them. A transition runs from the first trial of
    a block (not the session's first block) to its first hit; it is split at the first rule
    error (a lick to the previous block's port for the previous block's stimulus: TVV in a
    touch block, VTT in a light block): `early` up to and including it, `late` after it and
    before the first hit. When the first hit comes before any rule error, `early` runs up to and
    including the first hit, and there is no `late`. `not_trans` marks trials from the first hit
    to the end of the block. Returns per-trial flags and, per block, the row of its first hit.
    """
    cat = t.category.to_numpy()
    in_t = np.isin(cat, [CATEGORIES[(1, s, d)] for s in (1, 2) for d in (1, 2, 3)]).astype(int)
    in_v = np.isin(cat, [CATEGORIES[(2, s, d)] for s in (1, 2) for d in (1, 2, 3)]).astype(int)
    change = (t.block_type == "Change").to_numpy()
    for i in range(1, len(t)):
        if change[i] and in_t[i - 1]:
            in_t[i] = 1
        elif change[i] and in_v[i - 1]:
            in_v[i] = 1
    n = len(t)
    early, late, not_trans = (np.zeros(n, bool) for _ in range(3))
    blocks = []
    for flag, hit, error, name in ((in_t, "TTT", "TVV", "touch"), (in_v, "VVV", "VTT", "light")):
        starts = np.flatnonzero(np.diff(np.r_[0, flag]) == 1)
        ends = np.flatnonzero(np.diff(np.r_[flag, 0]) == -1)
        for s0, e0 in zip(starts, ends):
            seg = np.arange(s0, e0 + 1)
            hits = seg[cat[seg] == hit]
            errs = seg[cat[seg] == error]
            cues = seg[change[seg]]
            first_hit = hits[0] if len(hits) else None
            if first_hit is not None:
                not_trans[first_hit:e0 + 1] = True
            if s0 > 0 and first_hit is not None and len(errs):
                if errs[0] < first_hit:
                    early[s0:errs[0] + 1] = True
                    late[errs[0] + 1:first_hit] = True
                else:
                    early[s0:first_hit + 1] = True
            blocks.append({"block": name, "start": s0, "end": e0, "first_block": s0 == 0,
                           "first_hit": first_hit, "cue": cues[0] if len(cues) else None})
    flags = pd.DataFrame({"early": early, "late": late, "not_trans": not_trans}, index=t.index)
    return flags, pd.DataFrame(blocks)


# --- optogenetic sessions ----------------------------------------------------------------------

def opto_licks(t: pd.DataFrame, task: str) -> dict:
    """Lick outcomes per condition of one optogenetic session, as the code's GetBehavInfo.

    Keys (b, s, l, o) for the cross-modal task: block b (1 touch, 2 light); stimulus s (1
    tactile, 2 visual, 3 short laser-only, 4 long laser-only); lick l (1 right, 2 left); laser o
    (1 none, 2 before the stimulus, 3 from its onset; for laser-only trials o = 1 is the
    inter-trial window and o = 2 or 3 the response window). Each value is a boolean array over the
    trials of that condition. For the detection task, keys (s, o) with s = 1 tactile and s = 2 no
    tactile stimulus, lick = any right lick 0 to 2 s after the reference time, and s = 4, 5 the
    short and long laser-only trials.

    Times are relative to `stimOnset_times`, which for laser-only trials is the laser offset
    (short, 0.8 s) or onset (long, 2 s). Laser before the stimulus: onset at -0.8 s; from the
    stimulus: onset at 0 (rounded to 0.1 s, as the code). Trials with a lick in the censor
    (-0.2 to 0 s) or grace (0 to 0.1 s) period are left out.
    """
    rel = np.round((t.opto_on - t.stim_on).to_numpy(), 1)
    is_opto = ~np.isnan(rel)
    pre, post = is_opto & (rel < 0), is_opto & (rel == 0)
    out = {}
    if task == "cross-modal":
        tstim, vstim = t.som_on.notna().to_numpy(), t.vis_on.notna().to_numpy()
        catch = is_opto & ~(tstim | vstim)
        stims = {1: tstim, 2: vstim, 3: catch & pre, 4: catch & post}
        blocks = {1: (t.block_type == "Whisker").to_numpy(), 2: (t.block_type == "Visual").to_numpy()}
        resp = t.response.to_numpy()
        lick = {1: resp == 1, 2: resp == 2}
        rw = {1: licks_in(t, 0, 2, "right"), 2: licks_in(t, 0, 2, "left")}
        iti_short = {1: licks_in(t, -2.8, -0.8, "right"), 2: licks_in(t, -2.8, -0.8, "left")}
        iti_long = {1: licks_in(t, -2, 0, "right"), 2: licks_in(t, -2, 0, "left")}
        ok = ~licks_in(t, -0.2, 0) & ~licks_in(t, 0, 0.1)
        optos = {1: ~is_opto, 2: pre, 3: post}
        for b, blk in blocks.items():
            for l in (1, 2):
                for s in (1, 2):
                    for o, op in optos.items():
                        out[(b, s, l, o)] = lick[l][blk & stims[s] & op & ok]
                out[(b, 3, l, 1)] = iti_short[l][blk & stims[3] & ok]
                out[(b, 3, l, 2)] = rw[l][blk & stims[3] & ok]
                out[(b, 4, l, 1)] = iti_long[l][blk & stims[4] & ok]
                out[(b, 4, l, 3)] = rw[l][blk & stims[4] & ok]
    else:
        tstim = t.som_on.notna().to_numpy()
        catch = is_opto & ~tstim
        rw = licks_in(t, 0, 2, "right")
        ok = ~licks_in(t, -0.2, 0, "right") & ~licks_in(t, 0, 0.1, "right")
        ok_short = ~licks_in(t, -1, -0.8, "right") & ~licks_in(t, -0.8, -0.7, "right")
        for s, st in ((1, tstim), (2, ~tstim)):
            for o, op in ((1, ~is_opto), (2, pre), (3, post)):
                out[(s, o)] = rw[st & op & ok]
        out[(4, 1)] = licks_in(t, -2.8, -0.8, "right")[catch & pre & ok_short]
        out[(4, 3)] = licks_in(t, -0.8, 1.2, "right")[catch & pre & ok_short]
        out[(5, 1)] = licks_in(t, -2, 0, "right")[catch & post & ok]
        out[(5, 3)] = rw[catch & post & ok]
    return out


def cross_modal_passed(d: dict) -> bool:
    """The code's PerfControl: baseline hit rates, block and overall performance, laser-only licks."""
    m = lambda k: round(float(np.mean(d[k])), 2) if len(d[k]) else np.nan
    t_hit, v_hit = m((1, 1, 1, 1)), m((2, 2, 2, 1))
    t_perf = round(float(np.mean(np.r_[d[(1, 1, 1, 1)], ~d[(1, 2, 1, 1)] & ~d[(1, 2, 2, 1)]])), 2)
    v_perf = round(float(np.mean(np.r_[d[(2, 2, 2, 1)], ~d[(2, 1, 1, 1)] & ~d[(2, 1, 2, 1)]])), 2)
    overall = round(float(np.mean(np.r_[d[(1, 1, 1, 1)], ~d[(1, 2, 1, 1)] & ~d[(1, 2, 2, 1)],
                                        d[(2, 2, 2, 1)], ~d[(2, 1, 1, 1)] & ~d[(2, 1, 2, 1)]])), 2)
    catch = [(m((1, 3, 1, 2)), t_hit), (m((1, 4, 1, 3)), t_hit), (m((2, 3, 2, 2)), v_hit), (m((2, 4, 2, 3)), v_hit)]
    return bool(t_hit >= 0.35 and v_hit >= 0.35 and t_perf >= 0.55 and v_perf >= 0.55 and overall >= 0.60
                and all(c < h and c <= 0.75 for c, h in catch))


def hierarchical_bootstrap(mouse: np.ndarray, counts: dict, formula, n_boot: int,
                           rng: np.random.Generator, resample: set | None = None) -> np.ndarray:
    """Mice, then sessions within each mouse, then trials, all with replacement (the code's scheme).

    `mouse`: the mouse of each session. `counts`: for each named trial group, a pair of arrays
    over sessions (number of trials, number with a lick). `formula(p)` combines a dict of lick
    probabilities (arrays of any shape) into the session's value, e.g. a change in sensitivity.
    Groups named in `resample` (default all) get a bootstrap draw of their trials, which for a
    lick indicator is a binomial draw; the others keep their observed probability. The value of
    one resample is the mean over the resampled mice of the mean over each mouse's resampled
    sessions. Returns the n_boot values.
    """
    resample = set(counts) if resample is None else resample
    mice = np.unique(mouse)
    members = [np.flatnonzero(mouse == m) for m in mice]
    smax = max(len(m) for m in members)
    table = np.zeros((len(mice), smax), int)
    for i, m in enumerate(members):
        table[i, :len(m)] = m
    n_of = np.array([len(m) for m in members])
    picks = rng.integers(len(mice), size=(n_boot, len(mice)))
    ns = n_of[picks]
    slot = (rng.random((n_boot, len(mice), smax)) * ns[..., None]).astype(int)
    sess = table[picks[..., None], slot]
    valid = np.arange(smax)[None, None, :] < ns[..., None]
    p = {}
    for name, (n, k) in counts.items():
        nn, kk = n[sess], k[sess]
        with np.errstate(invalid="ignore", divide="ignore"):
            if name in resample:
                p[name] = np.where(nn > 0, rng.binomial(nn, np.where(nn > 0, kk / np.maximum(nn, 1), 0)) / nn, np.nan)
            else:
                p[name] = np.where(nn > 0, kk / nn, np.nan)
    val = np.where(valid, formula(p), np.nan)
    with np.errstate(invalid="ignore"):
        return np.nanmean(np.nanmean(val, axis=2), axis=1)


def point_estimate(mouse: np.ndarray, counts: dict, formula) -> float:
    """Mean over mice of the mean over sessions, without resampling."""
    with np.errstate(invalid="ignore", divide="ignore"):
        p = {name: np.where(n > 0, k / np.maximum(n, 1), np.nan) for name, (n, k) in counts.items()}
    val = pd.Series(formula(p)).groupby(mouse).mean()
    return float(val.mean())


# --- per-session arrays for the ephys analyses -------------------------------------------------

def ephys_session(d: dict) -> dict:
    """Coded trials and the rates the analyses use, for one ephys session.

    `r100`: rates (Hz) in the 100 ms bins before and after the stimulus, (trials, units, 2).
    `r10`: rates in 10 ms bins from -100 to 150 ms, smoothed as the code (Gaussian over the
    -1 to 2.5 s grid; only two bins either side matter), (trials, units, 25); bin k covers
    -0.1 + 0.01 k to -0.09 + 0.01 k s.
    """
    t = code_trials(d["trials"])
    on = t.stim_on.to_numpy()
    r100 = binned_rates(d["spikes"], on, -0.1, 0.1, 0.1)
    r10 = gauss_smooth(binned_rates(d["spikes"], on, -0.2, 0.25, 0.01))[:, :, 10:35]
    return {"path": d["path"], "subject": d["subject"], "area": d["area"], "trials": t,
            "r100": r100, "r10": r10, "n_units": d["n_units"]}


def correct_trials(t: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Mask of correct trials and, for them, block (1 touch, 2 light) and stimulus (1 tactile, 2 visual)."""
    masks = [is_category(t, c) for c in (T_HIT, V_CR, T_CR, V_HIT)]
    sel = np.any(masks, axis=0)
    return sel, np.select(masks, [1, 1, 2, 2])[sel], np.select(masks, [1, 2, 1, 2])[sel]


def bootstrap_decoding(sessions: list[dict], target: str, bin_index: int, n_boot: int,
                       rng: np.random.Generator, k: int = 10) -> np.ndarray:
    """The code's multilevel bootstrap of decoding accuracy, shape (n_boot, 2): true, shuffled.

    Per resample: sessions with replacement; in each, neurons with replacement; per trial type
    (tactile hit, visual CR, tactile CR, visual hit) each trial gets a random fold of k (redrawn
    up to 50 times until no fold is empty), and the training and test trials of each fold are
    resampled with replacement. Diagonal LDA is trained on the training set and scored on the
    test set; for the shuffled value the labels are permuted within each set. The value is the
    mean accuracy over folds and sessions. `target` is "block" or "stimulus".
    """
    prepared = []
    for s in sessions:
        t = s["trials"]
        types = [is_category(t, c) for c in (T_HIT, V_CR, T_CR, V_HIT)]
        label = [1, 1, 2, 2] if target == "block" else [1, 2, 1, 2]
        prepared.append([(s["r100"][m][:, :, bin_index], lab) for m, lab in zip(types, label)])
    out = np.empty((n_boot, 2))
    for b in range(n_boot):
        acc = np.zeros((len(sessions), 2))
        for si, j in enumerate(rng.integers(len(sessions), size=len(sessions))):
            groups = prepared[j]
            n_units = groups[0][0].shape[1]
            neurons = rng.integers(n_units, size=n_units)
            folds = []
            for x, _ in groups:
                for _attempt in range(50):
                    f = rng.integers(k, size=len(x))
                    if len(np.unique(f)) == k:
                        break
                folds.append(f)
            fold_acc = np.zeros((k, 2))
            for f in range(k):
                xtr, ytr, xte, yte = [], [], [], []
                for (x, lab), fo in zip(groups, folds):
                    tr, te = np.flatnonzero(fo != f), np.flatnonzero(fo == f)
                    if len(tr):
                        tr = tr[rng.integers(len(tr), size=len(tr))]
                    if len(te):
                        te = te[rng.integers(len(te), size=len(te))]
                    xtr.append(x[tr][:, neurons]); xte.append(x[te][:, neurons])
                    ytr.append(np.full(len(tr), lab)); yte.append(np.full(len(te), lab))
                xtr, xte = np.concatenate(xtr), np.concatenate(xte)
                ytr, yte = np.concatenate(ytr), np.concatenate(yte)
                for shuffled in (0, 1):
                    a, c = (ytr, yte) if not shuffled else (rng.permutation(ytr), rng.permutation(yte))
                    if len(np.unique(a)) < 2 or len(c) == 0:
                        fold_acc[f, shuffled] = np.nan
                        continue
                    fold_acc[f, shuffled] = (DiagLDA().fit(xtr, a).predict(xte) == c).mean()
            acc[si] = np.nanmean(fold_acc, axis=0)
        out[b] = acc.mean(axis=0)
    return out


def condition_means(s: dict, window: slice = slice(None)) -> tuple[np.ndarray, dict]:
    """Trial-averaged smoothed rates per category, (units, categories, bins), and the trial counts.

    Categories in the order of `CATEGORIES`; a category without trials is NaN.
    """
    t, r = s["trials"], s["r10"][:, :, window]
    keys = list(CATEGORIES)
    out = np.full((r.shape[1], len(keys), r.shape[2]), np.nan)
    counts = {}
    for i, key in enumerate(keys):
        m = is_category(t, key)
        counts[key] = int(m.sum())
        if m.any():
            out[:, i, :] = r[m].mean(axis=0)
    return out, counts


def trajectory_distance(s: dict, offset: float = SOFT_NORM_OFFSET, n_pc: int = 3) -> np.ndarray:
    """Mean distance between tactile hit and correct rejection trials in the top PCs, per 10 ms bin.

    Window -100 to 150 ms (the 25 bins of `r10`). Normalization: (x - mean) / (range + offset)
    with mean and range over the trial averages of all categories, as the code. PCA: uncentred
    SVD of the concatenated normalized hit and correct-rejection averages; single trials are
    projected on the top `n_pc` left singular vectors; distances are averaged over all pairs.
    """
    keys = list(CATEGORIES)
    x, _ = condition_means(s)
    ref = x.reshape(x.shape[0], -1)
    mean = np.nanmean(ref, axis=1)[:, None]
    scale = (np.nanmax(ref, axis=1) - np.nanmin(ref, axis=1) + offset)[:, None]
    z = (x - mean[:, :, None]) / scale[:, :, None]
    zz = np.concatenate([z[:, keys.index(T_HIT)], z[:, keys.index(T_CR)]], axis=1)
    w = np.linalg.svd(zz, full_matrices=False)[0][:, :n_pc]
    t = s["trials"]
    proj = {}
    for key in (T_HIT, T_CR):
        tr = (s["r10"][is_category(t, key)] - mean[None]) / scale[None]       # trials, units, bins
        proj[key] = np.einsum("tub,uk->tbk", tr, w)
    d = np.linalg.norm(proj[T_HIT][:, None] - proj[T_CR][None], axis=-1)      # hits, CRs, bins
    return d.mean(axis=(0, 1))


def subspace_overlaps(s: dict, rng: np.random.Generator, n_splits: int = 100, n_pc: int = 3,
                      ref_offset: float = SOFT_NORM_OFFSET, cmp_offset: float = SOFT_NORM_OFFSET,
                      per_neuron_split: bool = False) -> dict:
    """Subspace overlaps of control tactile hits and of tactile CRs with reference tactile hits.

    Tactile hit trials are split into equal reference and control halves (`n_splits` times, the
    overlaps averaged; with `per_neuron_split` each neuron gets its own split, as the code). PCA
    (uncentred SVD) of the normalized reference average over 0 to 150 ms. The overlap of a
    normalized average F is the squared norm of its projection on the reference's top `n_pc`
    components over that on its own top `n_pc`. Normalization: (x - mean) / (range + offset),
    mean and range over all category averages from -100 to 150 ms; the code uses offset 5 for
    the reference and 0.01 for the compared averages. Returns post-stimulus overlaps of control
    hits and CRs and the pre-stimulus (-100 to 0 ms) overlap of CRs.
    """
    keys = list(CATEGORIES)
    x, _ = condition_means(s)
    ref = x.reshape(x.shape[0], -1)
    mean = np.nanmean(ref, axis=1)[:, None]
    rng_ = (np.nanmax(ref, axis=1) - np.nanmin(ref, axis=1))[:, None]
    post, pre = slice(10, 25), slice(0, 10)
    t = s["trials"]
    hits = s["r10"][is_category(t, T_HIT)][:, :, post]                      # trials, units, bins
    cr = x[:, keys.index(T_CR)]

    def overlap(f, w):
        own = np.linalg.svd(f, full_matrices=False)[0][:, :n_pc]
        return (np.sum((f.T @ w) ** 2)) / np.sum((f.T @ own) ** 2)

    vals = []
    n = len(hits)
    for _ in range(n_splits):
        if per_neuron_split:
            comp = np.stack([rng.permutation(n) < round(n / 2) for _ in range(hits.shape[1])], axis=1)
            x_comp = np.stack([hits[comp[:, u], u].mean(0) for u in range(hits.shape[1])])
            x_ref = np.stack([hits[~comp[:, u], u].mean(0) for u in range(hits.shape[1])])
        else:
            comp = rng.permutation(n) < round(n / 2)
            x_comp, x_ref = hits[comp].mean(0), hits[~comp].mean(0)
        w = np.linalg.svd((x_ref - mean) / (rng_ + ref_offset), full_matrices=False)[0][:, :n_pc]
        norm = lambda a: (a - mean) / (rng_ + cmp_offset)
        vals.append((overlap(norm(x_comp), w), overlap(norm(cr[:, post]), w), overlap(norm(cr[:, pre]), w)))
    v = np.mean(vals, axis=0)
    return {"control_post": v[0], "cr_post": v[1], "cr_pre": v[2]}


def _unit(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)


def coding_dimension_dots(x: np.ndarray) -> dict:
    """Magnitudes of dot products between the two blocks' coding dimensions, from condition means.

    x: normalized condition means (units, categories in `CATEGORIES` order, 25 bins from -100 ms).
    CDs average 0 to 150 ms. Stimulus CD: tactile minus visual, each the mean of lick (right in
    touch blocks, left in light blocks) and no-lick averages. Choice CD: lick minus no lick, each
    the mean over tactile and visual. Right-left choice CD: right minus left lick, each the mean
    over the tactile and visual averages that exist (the code's nanmean).
    """
    keys = list(CATEGORIES)
    c = lambda b, s, d: x[:, keys.index((b, s, d)), 10:25].mean(axis=1)
    cds = {}
    for b, lick in ((1, 1), (2, 2)):
        cds[("stim", b)] = _unit((c(b, 1, lick) + c(b, 1, 3)) / 2 - (c(b, 2, lick) + c(b, 2, 3)) / 2)
        cds[("choice", b)] = _unit((c(b, 1, lick) + c(b, 2, lick)) / 2 - (c(b, 1, 3) + c(b, 2, 3)) / 2)
        right = np.nanmean([c(b, 1, 1), c(b, 2, 1)], axis=0)
        left = np.nanmean([c(b, 1, 2), c(b, 2, 2)], axis=0)
        cds[("rl", b)] = _unit(right - left)
    return {k: abs(float(cds[(k, 1)] @ cds[(k, 2)])) for k in ("stim", "choice", "rl")}


def bootstrap_coding_dimensions(sessions: list[dict], n_boot: int, rng: np.random.Generator,
                                min_trials: int = 2, offset: float = 0.01,
                                rl_rule: str = "pooled") -> pd.DataFrame:
    """The code's bootstrap of coding-dimension alignment (CM_coding_dimension_bootstrapping.m).

    Per resample: sessions with replacement; in each, neurons with replacement and, for every
    neuron and category, its trials with replacement (Multi_bootstrp); the shuffled version
    permutes each neuron's resampled trials across categories, keeping the counts
    (getShuffledData). Condition means are normalized by (x - mean) / (range + offset) over all
    categories and bins. Returns per resample the mean over sessions of each dot product, true
    and shuffled. The right-left value of a session is NaN when, in either block, the right-lick
    or the left-lick trials (pooled over stimuli, `rl_rule` "pooled") number fewer than
    `min_trials`; with `rl_rule` "each", when any of the four left- or right-lick categories
    that are rare (touch block left licks, light block right licks) does. The stimulus and
    choice CDs use categories every session has.
    """
    keys = list(CATEGORIES)

    def rl_ok(counts):
        if rl_rule == "each":
            return min(counts[keys.index(k)] for k in ((1, 1, 2), (1, 2, 2), (2, 1, 1), (2, 2, 1))) >= min_trials
        pooled = [counts[keys.index((b, 1, d))] + counts[keys.index((b, 2, d))] for b in (1, 2) for d in (1, 2)]
        return min(pooled) >= min_trials

    prepared = []
    for s in sessions:
        t = s["trials"]
        prepared.append([s["r10"][is_category(t, key)] for key in CATEGORIES])
    rows = []
    for b in range(n_boot):
        vals = {(k, sh): [] for k in ("stim", "choice", "rl") for sh in (0, 1)}
        for j in rng.integers(len(sessions), size=len(sessions)):
            groups = prepared[j]
            n_units = groups[0].shape[1]
            neurons = rng.integers(n_units, size=n_units)
            resampled = []
            for g in groups:
                k = len(g)
                if k == 0:
                    resampled.append(np.zeros((n_units, 0, g.shape[2])))
                    continue
                idx = rng.integers(k, size=(n_units, k))
                resampled.append(g[idx, neurons[:, None], :])                 # units, k, bins
            counts = [r.shape[1] for r in resampled]
            for shuffled in (0, 1):
                if shuffled:
                    allt = np.concatenate(resampled, axis=1)
                    order = np.argsort(rng.random(allt.shape[:2]), axis=1)
                    allt = np.take_along_axis(allt, order[:, :, None], axis=1)
                    parts = np.split(allt, np.cumsum(counts)[:-1], axis=1)
                else:
                    parts = resampled
                x = np.stack([p.mean(axis=1) if p.shape[1] else np.full((n_units, p.shape[2]), np.nan)
                              for p in parts], axis=1)
                ref = x.reshape(n_units, -1)
                mean = np.nanmean(ref, axis=1)[:, None, None]
                scale = (np.nanmax(ref, axis=1) - np.nanmin(ref, axis=1))[:, None, None] + offset
                dots = coding_dimension_dots((x - mean) / scale)
                if not rl_ok(counts):
                    dots["rl"] = np.nan
                for k, v in dots.items():
                    vals[(k, shuffled)].append(v)
        rows.append({f"{k}_{'shuffled' if sh else 'true'}": np.nanmean(v) if np.isfinite(v).any() else np.nan
                     for (k, sh), v in vals.items()})
    return pd.DataFrame(rows)


def transition_taus(s: dict, rng: np.random.Generator, k: int = 10, bootstrap: bool = False,
                    make_model=None) -> dict:
    """Kendall's tau of the touch-block probability over a rule transition, for one session.

    The classifier (default: LDA with Ledoit-Wolf shrinkage) is trained on correct trials from
    each block's first hit on (`not_trans`), on z-scored spike counts of the 100 ms before the
    stimulus (std + 0.01, as the code). Pre and post: mean posterior of the touch block on held-out
    correct trials of the old and new block types (the mean over the two trial types of each
    block). Early and late: mean posterior on the transition trials of the new block.

    Without `bootstrap`, held-out values come from k stratified folds and transition trials get
    the mean posterior of the k fold models. With `bootstrap` (one resample of the code's
    scheme), neurons are resampled, one random 1/k of each trial type is held out, training,
    test and transition trials are each resampled with replacement, and one model is fitted.
    Returns tau for light-to-touch (`to_touch`, x = pre light, early, late, post touch) and
    touch-to-light (`to_light`) transitions; NaN periods are dropped, as the code.
    """
    from scipy.stats import kendalltau
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    if make_model is None:
        make_model = lambda: LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
    t = s["trials"]
    flags, _ = transition_info(t)
    usable = (t.category != "").to_numpy()
    x = s["r100"][:, :, 0]
    if bootstrap:
        x = x[:, rng.integers(x.shape[1], size=x.shape[1])]
    ref = x[usable]
    z = (x - ref.mean(0)) / (ref.std(0, ddof=1) + 0.01)
    types = {key: is_category(t, key) & flags.not_trans.to_numpy() for key in (T_HIT, V_CR, T_CR, V_HIT)}
    label = {T_HIT: 1, V_CR: 1, T_CR: 2, V_HIT: 2}
    trans = {(period, b): np.flatnonzero(flags[period].to_numpy() & (t.b == b).to_numpy() & usable)
             for period in ("early", "late") for b in (1, 2)}
    prob = {}
    if not bootstrap:
        idx = np.flatnonzero(np.any(list(types.values()), axis=0))
        y = np.select([types[key][idx] for key in types], [label[key] for key in types])
        folds = stratified_folds(y * 10 + np.select([types[key][idx] for key in types], [1, 2, 3, 4]), k, rng)
        held = np.full(len(idx), np.nan)
        trans_p = {key: [] for key in trans}
        for f in range(k):
            tr, te = folds != f, folds == f
            model = make_model().fit(z[idx[tr]], y[tr])
            held[te] = model.predict_proba(z[idx[te]])[:, 0]
            for key, rows in trans.items():
                if len(rows):
                    trans_p[key].append(model.predict_proba(z[rows])[:, 0])
        for key in types:
            prob[key] = held[types[key][idx]].mean()
        for key, ps in trans_p.items():
            prob[key] = np.mean(ps, axis=0).mean() if ps else np.nan
    else:
        xtr, ytr, tests = [], [], {}
        for key, m in types.items():
            rows = rng.permutation(np.flatnonzero(m))
            n_test = int(round(len(rows) / k))
            te, tr = rows[:n_test], rows[n_test:]
            tr = tr[rng.integers(len(tr), size=len(tr))] if len(tr) else tr
            te = te[rng.integers(len(te), size=len(te))] if len(te) else te
            xtr.append(z[tr]); ytr.append(np.full(len(tr), label[key])); tests[key] = te
        model = make_model().fit(np.concatenate(xtr), np.concatenate(ytr))
        for key, te in tests.items():
            prob[key] = model.predict_proba(z[te])[:, 0].mean() if len(te) else np.nan
        for key, rows in trans.items():
            if len(rows):
                rows = rows[rng.integers(len(rows), size=len(rows))]
                prob[key] = model.predict_proba(z[rows])[:, 0].mean()
            else:
                prob[key] = np.nan
    touch = np.nanmean([prob[T_HIT], prob[V_CR]])
    light = np.nanmean([prob[T_CR], prob[V_HIT]])
    out = {"pre_touch": touch, "pre_light": light}
    for name, b, first, last in (("to_touch", 1, light, touch), ("to_light", 2, touch, light)):
        yv = np.array([first, prob[("early", b)], prob[("late", b)], last])
        xv = np.arange(1, 5)
        ok = ~np.isnan(yv)
        out[name] = kendalltau(xv[ok], yv[ok]).statistic if ok.sum() >= 2 else np.nan
        out[name + "_values"] = yv
    return out
