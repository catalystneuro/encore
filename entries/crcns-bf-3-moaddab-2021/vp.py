"""Loading and measures for the ventral pallidum recordings of CRCNS data set bf-3.

Moaddab, Ray & McDannald (2021), Communications Biology 4:43, doi:10.1038/s42003-020-01554-4.

The data set is one zip file, `bf-3/live/data_and_scripts.zip`, in the public CRCNS bucket. It
holds one MATLAB file per single unit (`matFiles/`, 435 files) with the unit's spike times
(`spike`, s), its mean waveform (`wave`, 32 points over 0.8 ms), the session's file name and the
Med Associates event channels as recorded by Plexon (`EVTnn`, s), a precomputed cube of all
units (`cubeFile/cube.mat`), and the authors' MATLAB scripts (`cubeScriptPR25.m`, which builds the
cube from the unit files, and `vpAnalysis.m`, which analyses it). The zip is read into memory
over HTTP, its MD5 is checked against the data set's `checksums.md5`, and its members are read
from memory; nothing is written to disk.

Every measure here is computed from the spike and event times. The cube is used only to check
that the trial tables built here are the authors'.

Where the parameters come from (the claims file is `claims/crcns-bf-3/10.1038-s42003-020-01554-4.yaml`;
"Methods" is the paper's Methods section; "the authors' code" is the two scripts in the zip,
which the paper does not link, see the notebook header):

- Event channels. The data descriptor does not say which channel is which. The authors' code,
  `cubeScriptPR25.m`, lists them: EVT01 foot shock, EVT02 pellet, EVT13 nose poke, and the cue
  channels by program letter (character 16 of the file name): program a, danger EVT09,
  uncertainty EVT12, safety EVT11; b, danger EVT11, uncertainty EVT09, safety EVT12; c, danger
  EVT12, uncertainty EVT11, safety EVT09 (`CUE_CHANNELS`). An uncertainty trial is a shock trial
  when a shock follows its onset within 30 s (same script). The notebook checks this mapping
  against the shocks.
- Trial structure (Methods, Fear discrimination; Results, paragraph 1): 20 s baseline, 10 s
  cue, shock 2 s after cue offset. Firing in 250 ms bins from 20 s before cue onset to 20 s after
  cue offset, 200 bins (Methods, Z-score normalization). Bins are left-open, (a, b], as in the
  authors' code; a standard choice that cannot change a result.
- Baseline firing = mean rate over the 10 s before cue onset (Methods, Identifying cue-responsive
  neurons; Firing and waveform characteristics).
- Cue screen (claim cue-responsive-screen): paired two-tailed t-tests, per cue (uncertainty
  pooled) and window (first 1 s, last 5 s), of the window rate against the 10 s baseline rate,
  p < 0.05, uncorrected (Methods). The authors' code floors each trial's rate to an integer
  (`floor`); `screen(..., floor_rates=True)` shows that as a variant. A test whose trial
  differences are all equal follows Matlab's ttest: significant when they are not zero.
- Suppression ratio per trial = (baseline pokes/min - cue pokes/min)/(sum), baseline the 20 s
  before cue onset, cue the 10 s cue (Methods, Calculating suppression ratios). A trial with no
  pokes in either is 0/0: claims file reading O3 (a) drop it, (b) set 0; the authors' code sets
  it to 1 (variant).
- Normalized cue firing (Methods, Z-score normalization): per neuron and trial type, the
  trial-averaged 250 ms rates minus that type's mean 10 s baseline, Z-scored over all bins of all
  types. Claims file reading O1: the pool is (a) three cues, uncertainty trials pooled, or (b)
  four trial types; under (b) the uncertainty curve is the trial-weighted mean of the shock and
  omission curves. The authors' code instead Z-scores single trials after subtracting each
  trial's own 2 s baseline, floored (variant `code`).
- Periods (Methods, Population and single-unit firing analyses): onset 0-1 s, late cue 5-10 s,
  delay 10-12 s; ANOVA intervals are the 56 bins of 250 ms from 2 s before cue onset to 2 s
  after offset.
- Firing characteristics (Methods): CV = SD/mean and skewness = 3(mean - median)/SD of
  inter-spike intervals; over which spikes is reading (a) whole session or (b) the 10 s
  baselines (claims file); the authors' code uses the 20 s before each cue (variant `base20`).
  Half duration and amplitude ratio follow the Methods' definitions as the authors' code
  computes them (`vpAnalysis.m`, lines 1035-1049): valley = minimum, P = maximum before the
  valley minus the first sample, N = first sample minus the valley, ratio (N - P)/(N + P);
  D = samples from the valley to the maximum after it, half duration D/2 in ms at 40 samples per
  ms. The code's one-sample offset in D is not copied (a constant, it cannot change the
  clusters).
- K-means (Methods): Matlab kmeans, k = 3, on the five characteristics. Claims file reading O7:
  (a) raw features, (b) Z-scored features. The authors' code uses raw features and Matlab
  defaults after rng(1) (`vpAnalysis.m`, lines 1485-1487), one k-means++ start. `kmeans3` runs
  scikit-learn's k-means++ with 100 restarts and a fixed seed (the claims file's standard
  choice); `matlab_kmeans` repeats the authors' single Matlab run, and `code_features` the
  features as their code computes them.
- Single-unit regression (Methods, Single-unit linear regression): per neuron, the 16 trials, 1 s
  bins from 2 s before cue onset to 2 s after offset (14 bins), firing regressed on a constant,
  relative threat (danger 1, safety 0, uncertainty the assignment) and the trial's suppression
  ratio (fear output). Claims file reading O2 for the per-trial firing: (a) trial rate minus its
  own 10 s baseline, centred and scaled with the mean and SD of the neuron's cue normalization;
  (b) trial rate minus the trial type's mean baseline, same scaling; (c) trial rate minus its
  own baseline, Z-scored over all trials and 1 s bins of the epoch (the authors' code does (c)
  with a 2 s floored baseline).
- Recorded time. Spikes, pokes and pellets exist only from 20 s before each cue onset to the
  pause event (EVT14) 31.5 s after it (`recorded_windows`); the rest of each inter-trial interval
  was not recorded. Event-locked windows (reward, pauses) must lie within recorded time.
- Reward firing (Methods, Z-score normalization): pellet deliveries (EVT02) outside cues, 16 bins
  of 250 ms from 2 s before to 2 s after, minus the mean of the 1 s before delivery. Claims file
  reading O4: the 4 s window (a) outside the cue and 2 s delay, (b) outside the whole trial
  window, so in the recorded 19.5 s after the delay;
  scaling (i) Z over the 16 bins of the neuron's mean, (ii) the SD of the neuron's cue
  normalization. The authors' code takes the pellets 18 to 2 s before and 14 to 28 s after each
  cue onset, subtracts the mean of the first 1 s of the window and Z-scores single events
  (variant `code`).
- Nose-poke pauses (claims supp6, supp9): a poke followed by no poke for (a) 10 s or (b) 5 s,
  the window from 2 s before to the end of the gap outside every trial and within recorded time (claims file readings,
  assumptions of the claims file). The authors' code takes gaps longer than 2 s between pokes
  18 to 2 s before each cue (variant `code`). Normalization as for reward.
- Bootstrap: studentized 95% interval of the mean, 1000 resamples (Methods, 95% bootstrap
  confidence interval); the standard error of each resample is the analytic SD/sqrt(n), a
  standard choice in place of Matlab's nested bootstrap of the SE.
- Repeated measures ANOVA: univariate, sphericity assumed (the paper reports uncorrected degrees
  of freedom). Between-subject factors and covariates enter as a linear model on each within
  contrast (`rm_anova`).
"""

from __future__ import annotations

import hashlib
import io
import itertools
import zipfile

import numpy as np
import requests
import scipy.io as sio
from scipy import stats

BASE_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/bf-3/live/"
ZIP_NAME = "data_and_scripts.zip"
ZIP_MD5 = "43a2887fac54e7bd12db345257a29864"   # bf-3/live/checksums.md5
DATASET_ID = "bf-3"
DATASET_VERSION = "unversioned"       # CRCNS data sets are not versioned; the MD5 pins the file
DATASET_DOI = "10.6080/K0HH6H8V"

CUE_CHANNELS = {  # program letter -> danger, uncertainty, safety (cubeScriptPR25.m)
    "a": ("EVT09", "EVT12", "EVT11"),
    "b": ("EVT11", "EVT09", "EVT12"),
    "c": ("EVT12", "EVT11", "EVT09"),
}
DANGER, UNC_SHOCK, UNC_OMIT, SAFETY = 1, 2, 3, 4
TYPE_NAMES = {DANGER: "danger", UNC_SHOCK: "uncertainty shock", UNC_OMIT: "uncertainty omission",
              SAFETY: "safety"}

BIN = 0.25
EPOCH = (-20.0, 30.0)                 # s from cue onset, 200 bins of 250 ms
N_BINS = 200
ANOVA_BINS = np.arange(72, 128)       # -2 s to +12 s, 56 bins
ONSET = np.arange(80, 84)             # 0-1 s
LATE = np.arange(100, 120)            # 5-10 s
DELAY = np.arange(120, 128)           # 10-12 s
REG_BINS = np.arange(18, 32)          # 1 s bins from -2 s to +12 s, on the 50-bin 1 s epoch
ASSIGNMENTS = (0.0, 0.25, 0.5, 0.75, 1.0)


# ----------------------------------------------------------------------------- loading

def read_zip() -> tuple[zipfile.ZipFile, str]:
    """The data set's zip, read into memory, and its MD5."""
    r = requests.get(BASE_URL + ZIP_NAME, timeout=300)
    r.raise_for_status()
    return zipfile.ZipFile(io.BytesIO(r.content)), hashlib.md5(r.content).hexdigest()


def load_units(zf: zipfile.ZipFile) -> list[dict]:
    """One dict per unit file: names, spike times, events, waveform, trial table."""
    units = []
    names = sorted(n for n in zf.namelist() if n.startswith("data_and_scipts/matFiles/") and n.endswith(".mat"))
    for n in names:
        m = sio.loadmat(io.BytesIO(zf.read(n)), squeeze_me=True)
        session = str(m["filename"])
        u = {
            "file": n.split("/")[-1],
            "session": session,
            "rat": session[:4],
            "date": session[4:10],
            "program": session[15],
            "neuron": str(m["neuron"]),
            "spikes": np.sort(np.atleast_1d(m["spike"]).astype(float)),
            "spikes_sorted_in_file": bool(np.all(np.diff(np.atleast_1d(m["spike"])) >= 0)),
            "wave": np.atleast_1d(m["wave"]).astype(float),
            "events": {k: np.sort(np.atleast_1d(v).astype(float)) for k, v in m.items() if k.startswith("EVT")},
        }
        u["name"] = u["session"] + u["neuron"]
        u["onsets"], u["types"] = trial_table(u)
        units.append(u)
    return units


def load_cube(zf: zipfile.ZipFile):
    """The authors' precomputed cube (used only for checks)."""
    return sio.loadmat(io.BytesIO(zf.read("data_and_scipts/cubeFile/cube.mat")),
                       squeeze_me=True, struct_as_record=False)["cube"]


def trial_table(u: dict) -> tuple[np.ndarray, np.ndarray]:
    """Cue onsets and trial types, ordered by time."""
    ev = u["events"]
    d, unc, s = (ev.get(c, np.array([])) for c in CUE_CHANNELS[u["program"]])
    shock = ev.get("EVT01", np.array([]))
    unc_type = [UNC_SHOCK if np.any((shock > t) & (shock <= t + 30)) else UNC_OMIT for t in unc]
    onsets = np.concatenate([d, unc, s])
    types = np.concatenate([np.full(len(d), DANGER), np.array(unc_type, dtype=int), np.full(len(s), SAFETY)])
    order = np.argsort(onsets)
    return onsets[order], types[order].astype(int)


# ----------------------------------------------------------------------------- binning

def counts(times: np.ndarray, starts: np.ndarray, stops: np.ndarray) -> np.ndarray:
    """Number of times in (start, stop] for each window."""
    return np.searchsorted(times, stops, side="right") - np.searchsorted(times, starts, side="right")


def binned(times: np.ndarray, align: np.ndarray, t0: float, t1: float, width: float) -> np.ndarray:
    """Rates (per s) in bins of `width` from t0 to t1 around each alignment time, (n_align, n_bins)."""
    edges = np.arange(t0, t1 + width / 2, width)
    c = np.searchsorted(times, align[:, None] + edges[None, :], side="right")
    return np.diff(c, axis=1) / width


def unit_measures(u: dict) -> None:
    """Adds the per-trial measures every claim uses."""
    sp, on = u["spikes"], u["onsets"]
    u["rate250"] = binned(sp, on, *EPOCH, BIN)                 # (16, 200)
    u["rate1s"] = binned(sp, on, *EPOCH, 1.0)                  # (16, 50)
    u["base10"] = counts(sp, on - 10, on) / 10.0
    u["onset1"] = counts(sp, on, on + 1) / 1.0
    u["last5"] = counts(sp, on + 5, on + 10) / 5.0
    u["base2_floor"] = np.floor(counts(sp, on - 2, on) / 2.0)
    pk = u["events"].get("EVT13", np.array([]))
    base = counts(pk, on - 20, on) * 3.0                       # pokes/min
    cue = counts(pk, on, on + 10) * 6.0
    with np.errstate(invalid="ignore", divide="ignore"):
        u["sr"] = (base - cue) / (base + cue)                  # NaN where 0/0
    u["poke_base"], u["poke_cue"] = base, cue


# ----------------------------------------------------------------------------- screen

def screen(u: dict, floor_rates: bool = False) -> np.ndarray:
    """p-values of the six screen tests: (danger, uncertainty, safety) x (onset 1 s, last 5 s)."""
    f = np.floor if floor_rates else (lambda x: x)
    base, on1, l5 = f(u["base10"]), f(u["onset1"]), f(u["last5"])
    p = []
    for win in (on1, l5):
        for sel in (u["types"] == DANGER, np.isin(u["types"], [UNC_SHOCK, UNC_OMIT]), u["types"] == SAFETY):
            a, b = base[sel], win[sel]
            d = b - a
            if np.all(d == d[0]):
                # no variance: Matlab's ttest gives t = +-Inf, p = 0, for a nonzero difference
                # and NaN (not significant, vpAnalysis.m line 55) for none
                p.append(0.0 if d[0] != 0 else np.nan)
            else:
                p.append(stats.ttest_rel(b, a).pvalue)
    return np.array(p)


# ----------------------------------------------------------------------------- normalization

def type_masks(types: np.ndarray, pool: str) -> dict:
    if pool == "3":
        return {"D": types == DANGER, "U": np.isin(types, [UNC_SHOCK, UNC_OMIT]), "S": types == SAFETY}
    return {"D": types == DANGER, "US": types == UNC_SHOCK, "UO": types == UNC_OMIT, "S": types == SAFETY}


def normalize_cue(u: dict, pool: str = "3") -> dict:
    """Normalized cue firing per cue (D, U, S), each (200,), and the mean and SD used (Methods)."""
    if pool == "code":
        d = u["rate250"] - u["base2_floor"][:, None]
        mu, sd = d.mean(), d.std(ddof=1)
        z = (d - mu) / sd
        m3 = type_masks(u["types"], "3")
        return {k: z[v].mean(0) for k, v in m3.items()} | {"mu": mu, "sd": sd}
    masks = type_masks(u["types"], pool)
    diff = {k: u["rate250"][v].mean(0) - u["base10"][v].mean() for k, v in masks.items()}
    allv = np.concatenate(list(diff.values()))
    mu, sd = allv.mean(), allv.std(ddof=1)
    z = {k: (v - mu) / sd for k, v in diff.items()}
    if pool == "4":
        n_s, n_o = masks["US"].sum(), masks["UO"].sum()
        z["U"] = (n_s * z.pop("US") + n_o * z.pop("UO")) / (n_s + n_o)
    return z | {"mu": mu, "sd": sd}


def stack(norms: list[dict], key: str) -> np.ndarray:
    return np.array([n[key] for n in norms])


# ----------------------------------------------------------------------------- characteristics

def isi_stats(u: dict, spikes_from: str) -> tuple[float, float]:
    """CV and coefficient of skewness of inter-spike intervals (Methods)."""
    sp, on = u["spikes"], u["onsets"]
    if spikes_from == "session":
        isi = np.diff(sp)
    else:
        w = {"base10": 10.0, "base20": 20.0}[spikes_from]
        isi = np.concatenate([np.diff(sp[(sp > t - w) & (sp <= t)]) for t in on])
    if len(isi) < 2:
        return np.nan, np.nan
    sd = isi.std(ddof=1)
    return sd / isi.mean(), 3 * (isi.mean() - np.median(isi)) / sd


def waveform_features(wave: np.ndarray) -> tuple[float, float]:
    """Half duration (ms) and amplitude ratio (Methods, as computed in vpAnalysis.m)."""
    v = int(np.argmin(wave))
    pre_max = wave[: v + 1].max()
    post = int(np.argmax(wave[v:]))           # samples from the valley to the maximum after it
    half = post / 2 / 40.0
    p = pre_max - wave[0]
    n = wave[0] - wave[v]
    return half, (n - p) / (n + p)


def kmeans3(X: np.ndarray, scale: bool, seed: int = 0) -> np.ndarray:
    """k-means labels, k = 3, renamed 0 = Low, 1 = Intermediate, 2 = High by mean of column 0."""
    from sklearn.cluster import KMeans
    Xf = (X - X.mean(0)) / X.std(0, ddof=1) if scale else X
    lab = KMeans(n_clusters=3, n_init=100, random_state=seed).fit_predict(Xf)
    order = np.argsort([X[lab == k, 0].mean() for k in range(3)])
    return np.argsort(order)[lab]


def code_features(u: dict) -> list[float]:
    """The five characteristics as vpAnalysis.m computes them: mean of the floored 10 s baseline
    rates, CV and skewness over the 20 s baselines, half duration with the code's one-sample
    offset, amplitude ratio. Order: baseline, CV, skewness, half duration, amplitude ratio."""
    v = int(np.argmin(u["wave"]))
    post = int(np.argmax(u["wave"][v:]))
    _, ratio = waveform_features(u["wave"])
    return [np.floor(u["base10"]).mean(), *isi_stats(u, "base20"), (post + 1) / 80.0, ratio]


def matlab_kmeans(X: np.ndarray, seed: int = 1, k: int = 3) -> tuple[np.ndarray, float]:
    """One run of Matlab's kmeans (k-means++ start, batch updates) after rng(seed).

    Matlab's rng(seed) twister and numpy's RandomState(seed) give the same uniform stream; the
    first centre is row ceil(u * n), the others are drawn with probability proportional to the
    squared distance to the nearest centre (Matlab kmeans 'plus' start, one replicate, the
    default). Returns labels renamed by mean of column 0 (0 = Low) and the within-cluster sum
    of squares.
    """
    rs = np.random.RandomState(seed)
    n = len(X)
    C = [X[int(np.ceil(rs.random_sample() * n)) - 1]]
    md = np.full(n, np.inf)
    for _ in range(1, k):
        md = np.minimum(md, ((X - C[-1]) ** 2).sum(1))
        c = np.cumsum(md / md.sum())
        C.append(X[int((c <= rs.random_sample()).sum())])
    return _lloyd(X, np.array(C))


def _lloyd(X: np.ndarray, C: np.ndarray) -> tuple[np.ndarray, float]:
    for _ in range(100):
        lab = ((X[:, None, :] - C[None]) ** 2).sum(2).argmin(1)
        Cn = np.array([X[lab == j].mean(0) for j in range(len(C))])
        if np.allclose(Cn, C):
            break
        C = Cn
    sse = sum(((X[lab == j] - X[lab == j].mean(0)) ** 2).sum() for j in range(len(C)))
    order = np.argsort([X[lab == j, 0].mean() for j in range(len(C))])
    return np.argsort(order)[lab], sse


def kmeans_sse(X: np.ndarray, lab: np.ndarray) -> float:
    return sum(((X[lab == j] - X[lab == j].mean(0)) ** 2).sum() for j in np.unique(lab))


# ----------------------------------------------------------------------------- regression

def trial_firing(u: dict, reading: str, norm: dict | None = None) -> np.ndarray:
    """Per-trial normalized firing in the 14 regression bins (16, 14), claims file reading O2."""
    r = u["rate1s"]
    if reading == "a":
        return ((r - u["base10"][:, None]) - norm["mu"])[:, REG_BINS] / norm["sd"]
    if reading == "b":
        tb = np.array([u["base10"][u["types"] == t].mean() for t in u["types"]])
        return ((r - tb[:, None]) - norm["mu"])[:, REG_BINS] / norm["sd"]
    if reading == "c":
        d = r - u["base10"][:, None]
        return ((d - d.mean()) / d.std(ddof=1))[:, REG_BINS]
    if reading == "code":
        d = r - u["base2_floor"][:, None]
        return ((d - d.mean()) / d.std(ddof=1))[:, REG_BINS]
    raise ValueError(reading)


def fear_output(u: dict, sr_nan: str) -> np.ndarray:
    """Per-trial suppression ratio with 0/0 trials as NaN (drop), 0 or 1."""
    sr = u["sr"].copy()
    if sr_nan == "zero":
        sr[np.isnan(sr)] = 0.0
    elif sr_nan == "one":
        sr[np.isnan(sr)] = 1.0
    return sr


def threat(types: np.ndarray, assignment: float) -> np.ndarray:
    return np.select([types == DANGER, np.isin(types, [UNC_SHOCK, UNC_OMIT])], [1.0, assignment], 0.0)


def regress(y: np.ndarray, cols: list[np.ndarray]) -> np.ndarray:
    """Betas (without the constant) of y (trials, bins) on a constant and cols; NaN rows dropped."""
    X = np.column_stack([np.ones(len(y))] + cols)
    ok = np.all(np.isfinite(X), 1)
    b = np.linalg.lstsq(X[ok], y[ok], rcond=None)[0]
    return b[1:]                                   # (n_cols, bins)


# ----------------------------------------------------------------------------- event-locked firing

def recorded_windows(u: dict) -> np.ndarray:
    """Spans with recorded data: from 20 s before each cue onset to the next EVT14 (pause
    recording, cubeScriptPR25.m), 31.5 s after onset. Spikes, pokes and pellets exist only there."""
    p = u["events"].get("EVT14", np.array([]))
    ends = np.array([p[p > t].min() if np.any(p > t) else t + 31.5 for t in u["onsets"]])
    return np.column_stack([u["onsets"] - 20, ends])


def inside(t: np.ndarray, win: np.ndarray, before: float, after: float) -> np.ndarray:
    """True where [t - before, t + after] lies within one window."""
    return np.any((t[:, None] - before >= win[None, :, 0]) & (t[:, None] + after <= win[None, :, 1]), axis=1)


def trial_windows(u: dict, kind: str) -> np.ndarray:
    on = u["onsets"]
    if kind == "a":
        return np.column_stack([on, on + 12])
    return np.column_stack([on - 20, on + 12])


def outside(t: np.ndarray, win: np.ndarray, before: float = 0.0, after: float = 0.0) -> np.ndarray:
    """True where [t - before, t + after] overlaps no window."""
    lo, hi = t - before, t + after
    return ~np.any((lo[:, None] < win[None, :, 1]) & (hi[:, None] > win[None, :, 0]), axis=1)


def reward_events(u: dict, reading: str) -> np.ndarray:
    p = u["events"].get("EVT02", np.array([]))
    if reading == "code":
        on = u["onsets"]
        keep = [p[(p >= t - 18) & (p <= t - 2)] for t in on] + [p[(p >= t + 14) & (p <= t + 28)] for t in on]
        return np.sort(np.concatenate(keep)) if keep else p[:0]
    keep = outside(p, trial_windows(u, reading), 2.0, 2.0) & inside(p, recorded_windows(u), 2.0, 2.0)
    return p[keep]


def pause_events(u: dict, reading: str) -> np.ndarray:
    pk = u["events"].get("EVT13", np.array([]))
    if reading == "code":
        out = []
        for t in u["onsets"]:
            a = pk[(pk >= t - 18) & (pk <= t - 2)]
            out.append(a[:-1][np.diff(a) > 2])
        return np.sort(np.concatenate(out)) if out else pk[:0]
    gap = {"10s": 10.0, "5s": 5.0}[reading]
    nxt = np.append(pk[1:], np.inf)
    cand = pk[(nxt - pk) >= gap]
    keep = outside(cand, trial_windows(u, "b"), 2.0, gap) & inside(cand, recorded_windows(u), 2.0, gap)
    return cand[keep]


def event_firing(u: dict, events: np.ndarray, scale: str, cue_sd: float | None = None) -> np.ndarray | None:
    """Normalized firing in 16 bins of 250 ms from 2 s before to 2 s after the events (Methods)."""
    if len(events) == 0:
        return None
    r = binned(u["spikes"], events, -2.0, 2.0, BIN)       # (n_events, 16)
    if scale == "code":
        d = r - r[:, 0:4].mean(1, keepdims=True)
        sd = d.std(ddof=1)
        return (d - d.mean()).mean(0) / sd if sd > 0 else None
    d = r.mean(0) - r.mean(0)[4:8].mean()
    if scale == "i":
        sd = d.std(ddof=1)
        return (d - d.mean()) / sd if sd > 0 else None
    return d / cue_sd                                     # "ii"


# ----------------------------------------------------------------------------- statistics

def boot_ci(x: np.ndarray, rng: np.random.Generator, n_boot: int = 1000, level: float = 0.95):
    """Mean and studentized bootstrap interval of the mean."""
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    n = len(x)
    m, se = x.mean(), x.std(ddof=1) / np.sqrt(n)
    idx = rng.integers(0, n, size=(n_boot, n))
    xb = x[idx]
    mb, seb = xb.mean(1), xb.std(1, ddof=1) / np.sqrt(n)
    ok = seb > 0
    t = (mb[ok] - m) / seb[ok]
    a = (1 - level) / 2
    return m, m - np.quantile(t, 1 - a) * se, m - np.quantile(t, a) * se


def _contrasts(k: int) -> np.ndarray:
    """Orthonormal contrasts (k, k-1) orthogonal to the constant."""
    h = np.zeros((k, k - 1))
    for j in range(1, k):
        h[:j, j - 1] = 1.0
        h[j, j - 1] = -j
    return h / np.linalg.norm(h, axis=0)


def rm_anova(Y: np.ndarray, within: list[str], between: np.ndarray | None = None,
             covariate: np.ndarray | None = None, between_name: str = "group") -> dict:
    """Univariate repeated measures ANOVA (sphericity assumed).

    Y is (subjects, levels of within[0], levels of within[1], ...). `between` is a group label per
    subject (effect coded, unweighted means) and `covariate` a value per subject (centred). Returns
    {effect: (F, df1, df2, p, partial eta squared)} for every within effect and its interactions
    with the between factor or the covariate.
    """
    n = Y.shape[0]
    levels = Y.shape[1:]
    Yf = Y.reshape(n, -1)
    X = [np.ones(n)]
    terms = {}
    if between is not None:
        g = np.unique(between)
        cols = [(between == gi).astype(float) - (between == g[-1]).astype(float) for gi in g[:-1]]
        terms[between_name] = list(range(len(X), len(X) + len(cols)))
        X += cols
    if covariate is not None:
        terms["cov"] = [len(X)]
        X.append(covariate - covariate.mean())
    X = np.column_stack(X)
    rank = np.linalg.matrix_rank(X)
    XtXi = np.linalg.pinv(X.T @ X)
    out = {}
    for r in range(1, len(within) + 1):
        for S in itertools.combinations(range(len(within)), r):
            C = np.ones((1, 1))
            for f, k in enumerate(levels):
                C = np.kron(C, _contrasts(k) if f in S else np.ones((k, 1)) / np.sqrt(k))
            Z = Yf @ C
            B = XtXi @ X.T @ Z
            R = Z - X @ B
            ss_err = (R ** 2).sum()
            df_e = C.shape[1]
            df_err = df_e * (n - rank)
            name = " x ".join(within[f] for f in S)
            for tname, rows in [("", [0])] + [(t, idx) for t, idx in terms.items()]:
                L = np.zeros((len(rows), X.shape[1]))
                for i, j in enumerate(rows):
                    L[i, j] = 1
                LB = L @ B
                M = np.linalg.inv(L @ XtXi @ L.T)
                ss = np.trace(LB.T @ M @ LB)
                df1 = df_e * len(rows)
                F = (ss / df1) / (ss_err / df_err)
                key = name if not tname else f"{tname} x {name}"
                out[key] = (F, df1, df_err, stats.f.sf(F, df1, df_err), ss / (ss + ss_err))
    return out


def fmt_anova(res: dict, keys: list[str] | None = None) -> str:
    keys = keys or list(res)
    return "\n".join(f"  {k}: F({res[k][1]},{res[k][2]}) = {res[k][0]:.2f}, p = {res[k][3]:.3g}, "
                     f"partial eta2 = {res[k][4]:.3f}" for k in keys)


def fisher_z(r1: float, r2: float, n1: int, n2: int) -> tuple[float, float]:
    """Independent-samples Fisher r-to-z comparison."""
    z = (np.arctanh(r1) - np.arctanh(r2)) / np.sqrt(1 / (n1 - 3) + 1 / (n2 - 3))
    return z, 2 * stats.norm.sf(abs(z))


def steiger_z(r12: float, r13: float, r23: float, n: int) -> tuple[float, float]:
    """Steiger (1980) Z for two dependent correlations sharing variable 1."""
    z12, z13 = np.arctanh(r12), np.arctanh(r13)
    rm2 = (r12 ** 2 + r13 ** 2) / 2
    f = min((1 - r23) / (2 * (1 - rm2)), 1.0)
    h = (1 - f * rm2) / (1 - rm2)
    z = (z12 - z13) * np.sqrt(n - 3) / np.sqrt(2 * (1 - r23) * h)
    return z, 2 * stats.norm.sf(abs(z))
