"""Loading and measures for dandiset 001454 (Patel, Kim et al. 2026, Nature Neuroscience,
doi:10.1038/s41593-026-02413-x).

The dandiset holds three kinds of NWB file, all streamed from the archive at the pinned
version; nothing is written to disk.

- `*_icephys.nwb`: one BLA neuron per file, whole-cell current clamp at 10 kHz, one 2-s sweep
  per current step. The electrode description says whether the cell was a BLA-mPFC projector
  ("targeting BLA to mPFC projections") or a nonspecific neighbour ("targeting
  Non-specific_BLA"); the session description gives the housing; the subject description gives
  the rank where there is one.
- `*_behavior+image+ophys.nwb` (cohorts 9, 10, 13b and 16): cued two-bottle choice sessions,
  CNMF-E traces at 10 Hz (`RoiResponseSeries`, every ROI, not the paper's curated neurons), lick
  onset and offset times of the two bottles, and the cue times with the trial type (1 forced
  water, 2 forced alcohol or sucrose, 3 choice without light, 4 choice with light).
- `*_image+ophys.nwb` (sub-M1-1 to sub-M2-3): resident-juvenile intruder sessions, CNMF-E traces
  only.

Where the parameters come from (claim criteria cite the paper; the claims file's shared methods
are named M1 to M8):

- Steps of 500 ms from -120 to +500 pA in 20-pA increments (Methods, Ex vivo whole-cell
  patch-clamp electrophysiology); the step onset and offset are read from the stimulus trace.
  Excitability uses the 26 steps 0 to +500 pA (M6). Spikes are upward crossings of 0 mV or of
  -20 mV within the step (M6 readings), with a 1 mV re-arm and a 1 ms dead time against
  noise at the threshold (standard choices; see `count_spikes`). Input resistance is from the -120 pA step, steady state
  over the last 100 ms or 50 ms of the step (claim supt1 readings), against the mean over the
  50 ms before the step (a standard choice). Firing threshold is the smallest step eliciting a
  spike (Methods).
- Lick bouts (M1): two or more consecutive licks with inter-lick intervals of 1 s or less,
  onset at the first lick. For calcium analyses only bouts whose onset is 3 s or more after the
  last lick of the preceding bout (M2); as the 3-s baseline must be free of drinking, the
  preceding bout is that of either bottle (a standard choice: the baseline then holds no bout;
  single licks outside bouts are not counted, so a baseline can hold an isolated lick).
- Z-score (M3): baseline the 3 s before onset (30 frames), z = (F - mean) / s.d. of the
  baseline; the trace F is the CNMF-E trace in the file. A neuron's response is its mean z from
  onset to 3 s. Bouts are matched across the conditions compared, per neuron, by cutting every
  condition to the smallest count, taking the bouts at random (reading a) or the first ones
  (reading b).
- Responsive (M4): response >= +1.98 (excited) or <= -1.98 (inhibited); the Wilcoxon reading
  compares, over bouts, the mean z from 0 to 3 s against 0 (p < 0.05).
- Decoding (M5): see `decode`.
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "001454"
DANDISET_VERSION = "0.260911.2319"
API = "https://api.dandiarchive.org/api"

FS_EPHYS = 10_000.0
FS_IMAGING = 10.0
STEP_CURRENTS = np.arange(-120, 501, 20)       # pA, Methods
EXCITABILITY_CURRENTS = np.arange(0, 501, 20)  # the 26 levels of the F(25, df) tests (M6)
SPIKE_THRESHOLDS_MV = (0.0, -20.0)             # M6 readings (a) and (b)
RIN_WINDOWS_MS = (100.0, 50.0)                 # supt1 readings, last 100 ms or 50 ms of the step

BOUT_ILI_S = 1.0          # M1
BOUT_GAP_S = 3.0          # M2
BASELINE_S = 3.0          # M3, drinking
RESPONSE_WINDOW_S = 3.0   # M3 and M4, onset to 3 s
Z_THRESHOLD = 1.98        # M4
MIN_ALCOHOL_LICKS = 50    # Methods, 2BC drinking: mice under 50 alcohol licks are excluded


# --------------------------------------------------------------------------------------------
# Archive

def assets() -> pd.DataFrame:
    """Path, asset id and size of every asset at the pinned version."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += [(a["path"], a["asset_id"], a["size"]) for a in page["results"]]
        url = page.get("next")
    return pd.DataFrame(rows, columns=["path", "asset_id", "size"]).sort_values("path",
                                                                              ignore_index=True)


def open_asset(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/"), "r")


def _text(ds) -> str:
    v = ds[()]
    return v.decode() if isinstance(v, bytes) else str(v)


def parallel(fn, items, workers=16):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(fn, items))


# --------------------------------------------------------------------------------------------
# Patch clamp

def load_cell(asset_id: str) -> dict:
    """One neuron: metadata, the step current of each sweep, and the voltage sweeps (mV)."""
    f = open_asset(asset_id)
    acq = [k for k in f["acquisition"] if "Clamp" in k][0]
    stim = [k for k in f["stimulus/presentation"]][0]
    v = f["acquisition"][acq]["data"]
    i = f["stimulus/presentation"][stim]["data"]
    vv = v[:] * v.attrs["conversion"] * 1e3
    ii = i[:] * i.attrs["conversion"] * 1e12
    n = 20000
    ns = len(vv) // n
    V, I = vv[: ns * n].reshape(ns, n), ii[: ns * n].reshape(ns, n)
    d = np.abs(np.diff(I[-1]))
    edges = np.nonzero(d > d.max() / 2)[0]
    on, off = edges[0] + 1, edges[-1] + 1
    step = np.median(I[:, on + 50: off - 50], axis=1) - np.median(I[:, : on - 50], axis=1)
    el = f["general/intracellular_ephys"]
    ename = [k for k in el if k.startswith("IntracellularElectrode")][0]
    desc = _text(el[ename]["description"])
    subj_desc = _text(f["general/subject/description"])
    rank = re.search(r"Rank (\d)", subj_desc)
    out = dict(
        asset_id=asset_id,
        subject=_text(f["general/subject/subject_id"]),
        sex=_text(f["general/subject/sex"]),
        housing=_text(f["session_description"]),
        target="BLA-mPFC" if "mPFC projections" in desc else "nonspecific",
        rank=int(rank.group(1)) if rank else np.nan,
        cell_id=_text(el[ename]["cell_id"]),
        location=_text(el[ename]["location"]),
        series_description=f["acquisition"][acq].attrs.get("description"),
        acquisition=sorted(f["acquisition"]), stimulus=sorted(f["stimulus/presentation"]),
        series_shape=tuple(v.shape),
        histology_shapes=[tuple(x.shape) for x in f["acquisition"]["histology_images"].values()]
        if "histology_images" in f["acquisition"] else [],
        n_sweeps=ns, step_on=int(on), step_off=int(off),
        step_pA=step, V=V.astype(np.float32),
    )
    f.close()
    return out


REARM_MV = 1.0       # a new crossing counts after V fell 1 mV below the threshold (noise guard)
DEAD_TIME_MS = 1.0   # a crossing within 1 ms of the last counted one is noise, not a new spike
SPIKE_RULES = {"": None, "r0": 0.0, "r5": 5.0}  # re-arm of each variant column (see cell_table)


def count_spikes(V: np.ndarray, on: int, off: int, threshold_mv: float,
                 rearm_mv: float | None = None, dead_ms: float | None = None) -> np.ndarray:
    """Upward crossings of `threshold_mv` within the step, per sweep (M6: "upward crossings of
    0 mV" or "of -20 mV"). Two guards against counting noise on a single crossing:
    `dead_ms`, crossings within that time of the last counted one are not counted (default
    `DEAD_TIME_MS` = 1 ms, about one spike's width: the recorded traces hold crossings 0.2 to
    0.3 ms apart that are noise at the threshold); `rearm_mv`, a crossing counts only after the
    voltage fell that far below the threshold since the last counted one (default `REARM_MV` =
    1 mV, about 8 times the median sample-to-sample noise s.d. of the recordings, 0.12 mV,
    printed in the notebook). Both are standard choices against noise on a plateau near the
    threshold (depolarisation block), where every crossing counted literally gives up to 98
    "spikes" per step. Variants shown in the notebook: no re-arm (dead time only, the literal
    reading), and the 5 mV re-arm of the first version of this attempt, which misses spikes
    whose troughs stay within 5 mV of the threshold."""
    rearm = REARM_MV if rearm_mv is None else rearm_mv
    dead = int(round((DEAD_TIME_MS if dead_ms is None else dead_ms) * FS_EPHYS / 1000))
    out = np.zeros(len(V), int)
    for s, seg in enumerate(V[:, on:off]):
        hi = seg >= threshold_mv
        rising = np.nonzero(hi & ~np.r_[False, hi[:-1]])[0]
        if len(rising) == 0:
            continue
        lo = seg < threshold_mv - rearm if rearm > 0 else ~hi
        clo = np.cumsum(lo)
        n, last = 1, rising[0]
        for r in rising[1:]:
            if r - last >= dead and clo[r] - clo[last] > 0:
                n += 1
                last = r
        out[s] = n
    return out


def nominal_steps(cell: dict) -> np.ndarray:
    """Nominal current of each sweep: sweep k is -120 + 20 k pA (Methods). The measured steps
    are within a few percent of these in every recorded cell (checked in the notebook)."""
    return STEP_CURRENTS[0] + 20.0 * np.arange(cell["n_sweeps"])


def recorded(cell: dict) -> bool:
    """False for files whose sweeps hold no response: no step in the stimulus trace (largest
    step under 100 pA) or a voltage range under 20 mV."""
    return bool(np.nanmax(np.abs(cell["step_pA"])) > 100 and np.ptp(cell["V"]) > 20)


def excitability(cell: dict, threshold_mv: float, rearm_mv: float | None = None) -> np.ndarray | None:
    """Spike counts at 0, 20, ..., 500 pA (M6), or None when the cell lacks those steps."""
    nominal = nominal_steps(cell)
    counts = count_spikes(cell["V"], cell["step_on"], cell["step_off"], threshold_mv, rearm_mv=rearm_mv)
    out = []
    for c in EXCITABILITY_CURRENTS:
        idx = np.nonzero(nominal == c)[0]
        if len(idx) == 0:
            return None
        out.append(counts[idx[0]])
    return np.array(out, dtype=float)


def input_resistance(cell: dict, window_ms: float) -> float:
    """MOhm, from the -120 pA step: steady state over the last `window_ms` of the step against
    the 50 ms before it (Methods; the window is a claim reading)."""
    nominal = nominal_steps(cell)
    idx = np.nonzero(nominal == -120)[0]
    if len(idx) == 0:
        return np.nan
    k = idx[0]
    on, off = cell["step_on"], cell["step_off"]
    w = int(window_ms * FS_EPHYS / 1000)
    base = cell["V"][k, on - 500: on].mean()
    ss = cell["V"][k, off - w: off].mean()
    di = cell["step_pA"][k]
    return (ss - base) / di * 1e3  # mV / pA = GOhm; x1e3 = MOhm


def rheobase(cell: dict, threshold_mv: float) -> float:
    """Smallest step (pA) eliciting at least one spike (Methods)."""
    nominal = nominal_steps(cell)
    counts = count_spikes(cell["V"], cell["step_on"], cell["step_off"], threshold_mv)
    hit = [c for c, n in sorted(zip(nominal, counts)) if n > 0 and c >= 0]
    return float(hit[0]) if hit else np.nan


# --------------------------------------------------------------------------------------------
# Split-plot ANOVA (between factors, one repeated factor), sphericity assumed

def split_plot_anova(Y: np.ndarray, between: pd.DataFrame) -> pd.DataFrame:
    """Univariate repeated-measures ANOVA for `Y` (subjects x levels) with the between-subject
    factors in `between` (one column per factor). Type III sums of squares with sum-to-zero
    coding. Within-subject effects (the repeated factor and its interactions) are computed from
    orthonormal contrasts of the levels, each tested against the subject-by-level error; the
    between effects use the subject means. This is the classical sphericity-assumed analysis,
    as GraphPad Prism reports it for two-way and three-way repeated measures ANOVA."""
    import statsmodels.formula.api as smf
    from scipy import stats
    from statsmodels.stats.anova import anova_lm

    n, k = Y.shape
    facs = list(between.columns)
    rhs = " * ".join(f"C({c}, Sum)" for c in facs)
    # orthonormal contrasts of the k levels
    H = np.linalg.qr(np.column_stack([np.ones(k), np.eye(k)[:, : k - 1]]))[0][:, 1:]
    D = Y @ H
    within = {}
    for j in range(k - 1):
        df = between.copy()
        df["y"] = D[:, j]
        t = anova_lm(smf.ols(f"y ~ {rhs}", df).fit(), typ=3)
        for term, row in t.iterrows():
            within.setdefault(term, [0.0, 0.0])
            within[term][0] += row["sum_sq"]
            within[term][1] += row["df"]
    df = between.copy()
    df["y"] = Y.mean(axis=1) * np.sqrt(k)
    tb = anova_lm(smf.ols(f"y ~ {rhs}", df).fit(), typ=3)
    rows = []
    err_b = tb.loc["Residual"]
    for term, row in tb.iterrows():
        if term in ("Intercept", "Residual"):
            continue
        F = (row["sum_sq"] / row["df"]) / (err_b["sum_sq"] / err_b["df"])
        rows.append((_name(term), row["df"], err_b["df"], F, stats.f.sf(F, row["df"], err_b["df"])))
    ss_e, df_e = within["Residual"]
    for term, (ss, dfe) in within.items():
        if term == "Residual":
            continue
        name = "level" if term == "Intercept" else "level:" + _name(term)
        F = (ss / dfe) / (ss_e / df_e)
        rows.append((name, dfe, df_e, F, stats.f.sf(F, dfe, df_e)))
    return pd.DataFrame(rows, columns=["effect", "df1", "df2", "F", "p"]).set_index("effect")


def _name(term: str) -> str:
    return ":".join(re.findall(r"C\((\w+), Sum\)", term))


def sidak(p, m):
    return 1 - (1 - np.asarray(p, float)) ** m


# --------------------------------------------------------------------------------------------
# Cued-2BC imaging sessions

def load_session(asset_id: str, traces: bool = True) -> dict:
    """One imaging session: metadata, licks (s), cues (s and type), CNMF-E traces (frames x
    ROIs, 10 Hz, starting at 0 s)."""
    f = open_asset(asset_id)
    out = dict(asset_id=asset_id, subject=_text(f["general/subject/subject_id"]),
               description=_text(f["session_description"]),
               start=_text(f["session_start_time"]),
               location=_text(f["general/optophysiology/ImagingPlane/location"]))
    rr = f["processing/ophys/Fluorescence/RoiResponseSeries"]
    out["rate"] = float(rr["starting_time"].attrs["rate"])
    out["t0"] = float(rr["starting_time"][()])
    out["n_frames"], out["n_rois"] = rr["data"].shape
    if traces:
        out["F"] = rr["data"][:].astype(np.float32)
    if "acquisition/LickTimes" in f:
        lt = f["acquisition/LickTimes"]
        out["licks"] = {
            "reward": lt["Etoh lick start timestamps/data"][:],
            "reward_end": lt["Etoh lick end timestamps/data"][:],
            "water": lt["Water lick start timestamps/data"][:],
            "water_end": lt["Water lick end timestamps/data"][:],
        }
    if "stimulus/presentation/CS timestamps and type" in f:
        cs = f["stimulus/presentation/CS timestamps and type"]
        out["cue_t"] = cs["timestamps"][:]
        out["cue_type"] = cs["data"][:].astype(int)
    f.close()
    return out


def bouts(licks: np.ndarray, ili: float = BOUT_ILI_S) -> pd.DataFrame:
    """Bouts of two or more licks with inter-lick intervals <= `ili` (M1)."""
    licks = np.sort(np.asarray(licks, float))
    if len(licks) < 2:
        return pd.DataFrame({"onset": np.zeros(0), "offset": np.zeros(0),
                             "n_licks": np.zeros(0, int)})
    brk = np.nonzero(np.diff(licks) > ili)[0]
    starts = np.r_[0, brk + 1]
    ends = np.r_[brk, len(licks) - 1]
    keep = ends > starts
    return pd.DataFrame({"onset": licks[starts[keep]], "offset": licks[ends[keep]],
                         "n_licks": (ends - starts + 1)[keep]})


def session_bouts(s: dict, gap: float = BOUT_GAP_S, gap_from: str = "last_lick") -> pd.DataFrame:
    """Bouts of both bottles, labelled, with whether each is isolated by `gap` s from the
    preceding bout of either bottle (M2). `gap_from` is "last_lick" (the M2 reading) or
    "onset" (the onset-to-onset variant). Each bout is labelled with the trial it falls in and
    whether light was delivered on that trial (types 4)."""
    b = []
    for liquid in ("reward", "water"):
        x = bouts(s["licks"][liquid])
        x["liquid"] = liquid
        b.append(x)
    b = pd.concat(b, ignore_index=True).sort_values("onset", ignore_index=True)
    prev_end = np.r_[-np.inf, b["offset"].values[:-1]]
    prev_on = np.r_[-np.inf, b["onset"].values[:-1]]
    ref = prev_end if gap_from == "last_lick" else prev_on
    b["isolated"] = (b["onset"].values - ref) >= gap
    b["next_gap"] = np.r_[b["onset"].values[1:], np.inf] - b["offset"].values
    b["prev_gap"] = b["onset"].values - prev_end
    if "cue_t" in s:
        idx = np.searchsorted(s["cue_t"], b["onset"].values, side="right") - 1
        b["trial"] = idx
        b["trial_type"] = np.where(idx >= 0, s["cue_type"][np.clip(idx, 0, None)], 0)
        b["since_cue"] = b["onset"].values - np.where(idx >= 0, s["cue_t"][np.clip(idx, 0, None)], np.nan)
    return b


SD_FLOOR = 0.05  # a bout's z is undefined when its baseline s.d. is under 5% of the session s.d.
Z_MODE = "baseline"  # "baseline" (M3) or "session" (variant: divide by the session s.d.)


def event_z(F: np.ndarray, onsets_s: np.ndarray, pre_s: float = BASELINE_S, post_s: float = 5.0,
            rate: float = FS_IMAGING, t0: float = 0.0, sd_floor: float = SD_FLOOR,
            sd_mode: str | None = None) -> np.ndarray:
    """z-scored traces around each onset (M3): events x neurons x frames, from -pre_s to
    +post_s; z against the mean and s.d. of the pre_s baseline. Events whose window leaves the
    recording are dropped. Where a neuron's baseline s.d. is under `sd_floor` times its s.d.
    over the session (flat baselines), the z of that bout is set to NaN: the Methods' z-score
    is undefined or unbounded there. This is a choice of this attempt (the paper does not say
    how such baselines were treated); the notebook reports how many bout-neuron pairs it
    removes. On nonnegative traces that are smooth between transients, as in cohort 9, the
    rule keeps mostly baselines
    that hold the decay of a transient, which biases z downward; the notebook therefore
    leaves cohort 9 out of the baseline z (an assumption, see the notebook). `sd_mode`
    "session" (default `Z_MODE`) is the variant that divides by the neuron's s.d. over the
    session instead, defined for every trace but on another scale than the Methods' z. The
    onsets are in seconds on the trace clock, whose start `t0` is 0 in every file (printed in
    the notebook)."""
    mode = Z_MODE if sd_mode is None else sd_mode
    pre, post = int(round(pre_s * rate)), int(round(post_s * rate))
    ssd = F.std(axis=0)
    floor = sd_floor * ssd
    fr = np.round((np.asarray(onsets_s) - t0) * rate).astype(int)
    fr = fr[(fr - pre >= 0) & (fr + post <= F.shape[0])]
    out = np.empty((len(fr), F.shape[1], pre + post), np.float32)
    for j, c in enumerate(fr):
        seg = F[c - pre: c + post]
        base = seg[:pre]
        if mode == "session":
            sd = ssd.copy()
            sd[sd == 0] = np.nan
        else:
            sd = base.std(axis=0)
            sd[(sd == 0) | (sd < floor)] = np.nan
        out[j] = ((seg - base.mean(axis=0)) / sd).T
    return out


def matched_mean(z_by_cond: dict, rng: np.random.Generator | None, how: str = "random") -> dict:
    """Mean z trace per neuron for each condition, every condition cut to the smallest bout
    count (M3). `how` is "random" (reading a, bouts drawn with `rng`) or "first" (reading b)."""
    m = min(len(z) for z in z_by_cond.values())
    out = {}
    for c, z in z_by_cond.items():
        if m == 0:
            out[c] = np.full(z.shape[1:], np.nan, np.float32)
            continue
        idx = np.sort(rng.choice(len(z), m, replace=False)) if how == "random" else np.arange(m)
        out[c] = np.nanmean(z[idx], axis=0)
    return out


def window_mean(trace: np.ndarray, pre_s: float = BASELINE_S, start_s: float = 0.0,
                stop_s: float = RESPONSE_WINDOW_S, rate: float = FS_IMAGING) -> np.ndarray:
    """Mean over the last axis between start_s and stop_s after onset."""
    a, b = int(round((pre_s + start_s) * rate)), int(round((pre_s + stop_s) * rate))
    return np.nanmean(trace[..., a:b], axis=-1)


# --------------------------------------------------------------------------------------------
# Decoding (M5)

def decoding_bouts(s: dict) -> pd.DataFrame:
    """Bouts longer than 1 s and separated from other bouts by at least 2 s (Methods,
    Pseudo-simultaneous population generation and decoding)."""
    b = session_bouts(s)
    dur = b["offset"] - b["onset"]
    return b[(dur > 1.0) & (b["prev_gap"] >= 2.0) & (b["next_gap"] >= 2.0)].reset_index(drop=True)


def bout_frames(F: np.ndarray, onset: float, offset: float, span: str, rate=FS_IMAGING) -> np.ndarray:
    """Frames of a bout: "bout" from onset to the last lick, "3s" from onset to 3 s."""
    a = int(round(onset * rate))
    b = int(round(offset * rate)) + 1 if span == "bout" else a + int(RESPONSE_WINDOW_S * rate)
    return F[a:min(b, F.shape[0])]


def decode(animals: list[dict], rng: np.random.Generator, k: int = 5, T: int = 10_000,
           shuffle: str | None = None, C: float = 1.0) -> np.ndarray:
    """k-fold pseudo-simultaneous decoding with a linear SVM; returns one accuracy per fold.

    `animals` is a list of dicts with "X" (list of frames x neurons arrays, one per bout) and
    "y" (bout labels 0/1). Bouts of each animal are split into k folds stratified by label, so
    that each fold holds at least one bout per class (Methods); each animal needs k bouts of
    each class. For each fold, training and test pseudo-populations of T samples are built: a
    label is drawn, and from every animal one frame of a bout of that label (in its training or
    its test bouts) is drawn; the animals' vectors are concatenated. The majority class of the
    training set is subsampled. Features are standardised on the training set (a standard
    choice for SVMs; the Methods do not say). `shuffle`: None; "train" (training labels
    permuted after sampling, chance reading 1); "bouts" (bout labels permuted within each
    animal before sampling, chance reading 2). C = 1, the library default (a standard choice)."""
    from sklearn.svm import LinearSVC

    folds = []
    for a in animals:
        y = np.asarray(a["y"])
        if shuffle == "bouts":
            y = rng.permutation(y)
        f = np.empty(len(y), int)
        for c in (0, 1):
            idx = rng.permutation(np.nonzero(y == c)[0])
            f[idx] = np.arange(len(idx)) % k
        folds.append((y, f))

    def sample(split_mask_fn, labels):
        cols = []
        for a, (y, f) in zip(animals, folds):
            pools = {}
            for c in (0, 1):
                bi = np.nonzero((y == c) & split_mask_fn(f))[0]
                pools[c] = np.concatenate([a["X"][i] for i in bi], axis=0)
            col = np.empty((len(labels), pools[0].shape[1]), np.float32)
            for c in (0, 1):
                m = labels == c
                col[m] = pools[c][rng.integers(0, len(pools[c]), m.sum())]
            cols.append(col)
        return np.concatenate(cols, axis=1)

    acc = []
    for fold in range(k):
        ytr = rng.integers(0, 2, T)
        yte = rng.integers(0, 2, T)
        Xtr = sample(lambda f: f != fold, ytr)
        Xte = sample(lambda f: f == fold, yte)
        # balance the training set by subsampling the majority class
        n0, n1 = (ytr == 0).sum(), (ytr == 1).sum()
        maj = 0 if n0 > n1 else 1
        keep = np.r_[np.nonzero(ytr != maj)[0],
                     rng.choice(np.nonzero(ytr == maj)[0], min(n0, n1), replace=False)]
        Xtr, ytr_b = Xtr[keep], ytr[keep]
        if shuffle == "train":
            ytr_b = rng.permutation(ytr_b)
        mu, sd = Xtr.mean(0), Xtr.std(0)
        sd[sd == 0] = 1
        clf = LinearSVC(C=C, dual=False, max_iter=5000)
        clf.fit((Xtr - mu) / sd, ytr_b)
        acc.append(float((clf.predict((Xte - mu) / sd) == yte).mean()))
    return np.array(acc)


def cell_table(cells: list[dict]) -> pd.DataFrame:
    """One row per neuron with the measures of every reading: spike counts at 0 to 500 pA
    (`e0` for the 0 mV threshold, `e-20` for -20 mV; suffix `r0` for the variant without a
    re-arm, `r5` for a 5 mV re-arm), rheobase, input resistance (`rin100`,
    `rin50`), resting potential before the first sweep."""
    rows = []
    for c in cells:
        ok = recorded(c)
        r = dict(path=c.get("path"), subject=c["subject"], sex=c["sex"],
                 housing="GH" if c["housing"].startswith("Group") else "SI",
                 target=c["target"], rank=c["rank"], n_sweeps=c["n_sweeps"],
                 cohort=c["subject"][-10:-6], recorded=ok)
        for thr in SPIKE_THRESHOLDS_MV:
            r[f"e{int(thr)}"] = excitability(c, thr) if ok else None
            for tag, ra in SPIKE_RULES.items():
                if tag:
                    r[f"e{int(thr)}{tag}"] = excitability(c, thr, rearm_mv=ra) if ok else None
            r[f"rheo{int(thr)}"] = rheobase(c, thr) if ok else np.nan
        for w in RIN_WINDOWS_MS:
            r[f"rin{int(w)}"] = input_resistance(c, w) if ok else np.nan
        r["vrest"] = float(np.median(c["V"][0, : c["step_on"] - 50]))
        rows.append(r)
    return pd.DataFrame(rows)


def curves(d: pd.DataFrame, thr) -> np.ndarray:
    """Neurons x 26 spike counts for the cells of `d` that have all 26 steps. `thr` is 0 or
    -20, or "0r0", "-20r5" and so on for the spike-rule variants."""
    v = [x for x in d[f"e{thr}"] if x is not None]
    return np.stack(v) if v else np.zeros((0, len(EXCITABILITY_CURRENTS)))


def posthoc_two(A: np.ndarray, B: np.ndarray) -> pd.DataFrame:
    """Sidak-adjusted comparisons of two groups at each of the 26 steps, under two readings of
    Prism's post hoc (the paper does not say which error term): (a) an unpaired t-test at each
    step; (b) a t-test using the error pooled over all steps and groups, as Prism does for
    two-way ANOVA. Both are adjusted for 26 comparisons."""
    from scipy import stats
    k = A.shape[1]
    with np.errstate(invalid="ignore", divide="ignore"):
        pa = np.array([stats.ttest_ind(A[:, j], B[:, j]).pvalue for j in range(k)])
    pa = np.nan_to_num(pa, nan=1.0)
    res = np.r_[A - A.mean(0), B - B.mean(0)]
    df = res.size - 2 * k
    mse = (res ** 2).sum() / df
    t = (B.mean(0) - A.mean(0)) / np.sqrt(mse * (1 / len(A) + 1 / len(B)))
    pb = 2 * stats.t.sf(np.abs(t), df)
    return pd.DataFrame({"current_pA": EXCITABILITY_CURRENTS, "mean_a": A.mean(0),
                         "mean_b": B.mean(0), "diff": B.mean(0) - A.mean(0),
                         "p_sidak_step": sidak(pa, k), "p_sidak_pooled": sidak(pb, k)})


def tukey_pooled(Ys: list[np.ndarray]) -> np.ndarray:
    """Tukey comparisons of each group against the first at every step, with the error pooled
    over all steps and groups (the pooled-error reading of the post hoc, as in `posthoc_two`;
    the per-step reading is scipy's `tukey_hsd` at each step). Returns p (steps x groups); the
    column of the first group is 1."""
    from scipy import stats
    g = len(Ys)
    k = Ys[0].shape[1]
    res = np.concatenate([Y - Y.mean(0) for Y in Ys])
    df = res.size - g * k
    mse = (res ** 2).sum() / df
    p = np.ones((k, g))
    for r in range(1, g):
        se = np.sqrt(mse / 2 * (1 / len(Ys[0]) + 1 / len(Ys[r])))
        q = np.abs(Ys[r].mean(0) - Ys[0].mean(0)) / se
        p[:, r] = stats.studentized_range.sf(q, g, df)
    return p


# --------------------------------------------------------------------------------------------
# Neuron responses per condition

def condition_traces(s: dict, b: pd.DataFrame, conds: dict, rng, how: str = "random",
                     pre_s: float = BASELINE_S, post_s: float = 5.0) -> tuple[dict, int, dict]:
    """Mean z trace per neuron (neurons x frames) for each condition of a session (M3).

    `b` are the session's bouts (`session_bouts`), `conds` maps a condition name to a boolean
    mask over `b`; only bouts isolated by the M2 gap enter. The conditions are cut to the
    smallest bout count (M3, "a matched number of bouts per condition per neuron"), at random
    with `rng` (reading a) or the first bouts (reading b). Returns the traces, the matched
    count, and the z of every bout of each condition (events x neurons x frames)."""
    z = {c: event_z(s["F"], b.onset.values[m & b.isolated.values], pre_s=pre_s, post_s=post_s)
         for c, m in conds.items()}
    m = min(len(v) for v in z.values())
    return matched_mean(z, rng, how), m, z


def wilcoxon_responsive(zb: np.ndarray, pre_s: float = BASELINE_S) -> np.ndarray:
    """M4, Wilcoxon reading: +1 / -1 / 0 per neuron from a signed-rank test of the per-bout mean
    z from onset to 3 s against 0, p < 0.05 (sign from the median)."""
    from scipy import stats
    r = window_mean(zb, pre_s)  # bouts x neurons
    out = np.zeros(r.shape[1], int)
    for j in range(r.shape[1]):
        x = r[:, j][np.isfinite(r[:, j])]
        if len(x) < 5 or np.all(x == 0):
            continue
        if stats.wilcoxon(x).pvalue < 0.05:
            out[j] = 1 if np.median(x) > 0 else -1
    return out
