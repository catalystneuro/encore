"""Loading and measures for CRCNS data set rrf-1 (Moaddab & McDannald 2021, Curr Biol 31:2099).

The data set (doi:10.6080/K04B2ZJ5) is one zip, `rrf-1/live/data.zip`, in the public S3 bucket
crcnsarchive. It holds the authors' derived file `data/cubeFile/cube.mat` (all 743 units, binned
firing, nose pokes and suppression ratios), `data/matFiles.tar` (one MATLAB file per unit with
spike times, event times and mean waveform), and the authors' MATLAB code: `cubeScriptPR25.m`,
which builds the cube from the unit files, and `rrfAnalysis.m`, which makes the paper's analyses
from the cube. Everything is streamed with fsspec and read in memory; nothing is written to disk.

Where the parameters come from. The claims file (claims/crcns-rrf-1/) fixes the claims and their
criteria; its header (checks, last item) says that an author who finds the paper's code in the
data set should follow it where it settles an open reading. The code is cited below by file
and line (as in data.zip, MD5 bf5cb2951c928394084d7b67c6b4663b):

- Trial order in every unit: rows 1-4 danger, 5-6 uncertainty shock, 7-12 uncertainty
  omission, 13-16 safety (data descriptor, "RRF cube data structure"; cubeScriptPR25.m 128-140).
- Binned firing: spikes in (t, t + w] from 20 s before cue onset, counts / w, floored to an
  integer (cubeScriptPR25.m, "Align firing to cue onset for multiple bin sizes"). Differential
  firing subtracts the trial's own 2-s pre-cue rate, floored to an integer Hz (lines 265-272
  and 460-463). The z-score is taken over all 16 trials x all bins of one unit
  (`zscore(...,0,'all')`, lines 469-472), and normalized firing for a trial type is the mean of
  the trial z-scores (rrfAnalysis.m 466-488). `z_methods` gives the Methods' wording
  ("Z-score normalization": average per trial type, subtract that type's 2-s baseline, z-score
  across trial types), with three (z-b) or four (z-a) trial types, as variants.
- Cue-responsive screen: paired t tests of the floored 10-s baseline rate against the floored
  rate in the first 1 s and in the last 5 s of each cue, p < 0.05, a NaN test counted as not
  significant (rrfAnalysis.m 5-60).
- K-means matrix: 1-s normalized firing, cue bins 21-30 (0 to 10 s after cue onset) for
  danger, uncertainty (8 trials) and safety, and bins 34-39 (13 to 19 s after cue onset) for
  danger, uncertainty shock, uncertainty omission and safety (rrfAnalysis.m, "K means
  clustering", `aa = [...]`); one k-means run per k after `rng(1)`, MATLAB defaults
  (k-means++, squared Euclidean). The code maps its cluster numbers to k1..k8 by hand
  (`idx == 5` is k1, and so on), which cannot be repeated outside MATLAB's generator.
- Periods (250-ms bins, 1-based as in the code): onset 81-84 (first 1 s of cue), late cue
  101-120 (last 5 s), delay 121-128 (2 s after cue offset); cue ANOVA bins 73-128; outcome
  bins 131-200, the 17.5 s after shock offset (rrfAnalysis.m, "Find individual firing in
  specified periods" and "Make SPSS data for ms250 firing"). Figure 3 intervals: k1 onset;
  k5 101-128; k7 121-128; the others 81-128 (rrfAnalysis.m, figure 4 summary section).
- Regression: per unit and 1-s bin 19-32 (2 s before cue onset to the end of the delay),
  trial z-scored firing on [1, threat probability, trial suppression ratio] (rrfAnalysis.m,
  "Single-unit regression"). Tuning curve bins (columns of the 14): k1 3; k5 8-12; k7 13-14;
  k3, k4, k6, k8 3-14; k4, k6 and k8 multiplied by -1 (rrfAnalysis.m, "Plot regression tuning
  curve for each cluster"). For the peak regression the whole beta row (both regressors) of
  k4, k6, k8 is multiplied by -1 (rrfAnalysis.m, "k4, peak prob7" and the following lines).
  The Figure 5F scatter averages columns 3-14 of each regressor (rrfAnalysis.m, "Make a
  scatter plot for peak probability vs fear output").
- Waveform half duration and amplitude ratio (rrfAnalysis.m, after "Find mean and SEM firing
  for cue-responsive units"); the code's sample rate, 40 points per ms, matches the data
  descriptor (32 points over 0.8 ms). Bregma level per rat (rrfAnalysis.m, "bregma for each id").
- Bootstrap: studentized 95% CI of the mean, 1,000 resamples (STAR Methods; `bootci(1000,
  {@mean, x}, 'type', 'student')` in the code, e.g. rrfAnalysis.m 1744). Called this way, with no
  'StdErr', bootci estimates each standard error from 'NBootStd' = 100 nested bootstrap samples
  (MATLAB documentation of bootci). The main reading uses s / sqrt(n) for every standard error,
  a deterministic choice; `boot_ci(..., n_boot_std=100)` gives the nested version as a variant.
"""

from __future__ import annotations

import io
import tarfile
import zipfile

import fsspec
import numpy as np
import scipy.io as sio
from scipy import stats

DATASET_ID = "rrf-1"
DATASET_VERSION = "unversioned"      # CRCNS data sets are not versioned; the MD5 below pins the file
DATASET_DOI = "10.6080/K04B2ZJ5"
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/rrf-1/live"
ZIP_URL = f"{BUCKET}/data.zip"
ZIP_MD5 = "bf5cb2951c928394084d7b67c6b4663b"   # checksums.md5 of the data set, = S3 ETag

# Trial rows (0-based) of every unit
DANGER = np.arange(0, 4)
UNC_SHOCK = np.arange(4, 6)
UNC_OMIT = np.arange(6, 12)
UNC = np.arange(4, 12)
SAFETY = np.arange(12, 16)
TRIAL_TYPE = np.array([1] * 4 + [2] * 2 + [3] * 6 + [4] * 4)   # code's tags

# Bregma level of each rat (rrfAnalysis.m, "bregma for each id")
BREGMA = {1: -7.08, 3: -6.84, 4: -6.72, 6: -6.72, 7: -6.60, 9: -6.36, 10: -6.72, 11: -6.84,
          12: -6.72, 13: -6.48, 14: -6.72}


def b250(first, last):
    """1-based inclusive 250-ms bin range of the code, as a 0-based slice."""
    return slice(first - 1, last)


ONSET = b250(81, 84)
LATE = b250(101, 120)
DELAY = b250(121, 128)
CUE_ANOVA = b250(73, 128)
OUTCOME = b250(131, 200)
OUTCOME_0_8 = b250(131, 162)        # 0 to 8 s after shock offset (claims file, Figure 6 boxes)
FIG3_INTERVAL = {"k1": ONSET, "k2": b250(81, 128), "k3": b250(81, 128), "k4": b250(81, 128),
                 "k5": b250(101, 128), "k6": b250(81, 128), "k7": DELAY, "k8": b250(81, 128)}
FIG6_WINDOW = {"k1": OUTCOME_0_8, "k2": OUTCOME, "k3": OUTCOME_0_8, "k4": OUTCOME,
               "k5": OUTCOME_0_8, "k6": OUTCOME_0_8, "k7": OUTCOME, "k8": OUTCOME}
# Regression columns (0-based of the 14 regression bins) for the tuning curves
TUNE_COLS = {"k1": slice(2, 3), "k3": slice(2, 14), "k4": slice(2, 14), "k5": slice(7, 12),
             "k6": slice(2, 14), "k7": slice(12, 14), "k8": slice(2, 14)}
INVERTED = ("k4", "k6", "k8")
ASSIGNMENTS = np.arange(9) * 0.125
PAPER_PEAK = {"k1": 0.375, "k3": 0.375, "k4": 0.875, "k5": 0.375, "k6": 0.625, "k7": 0.5,
              "k8": 0.25}


def open_zip():
    f = fsspec.open(ZIP_URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def code_lines(z, member, first, last):
    """Lines first..last (1-based, inclusive) of one of the code files in data.zip, numbered."""
    text = z.read(member).decode("latin-1").splitlines()
    return "\n".join(f"{i:5d}  {text[i - 1]}" for i in range(first, last + 1))


def _walk(o, prefix, out):
    if hasattr(o, "_fieldnames"):
        for k in o._fieldnames:
            _walk(getattr(o, k), f"{prefix}.{k}" if prefix else k, out)
    else:
        out[prefix] = o


def load_cube(z=None):
    """The authors' cube.mat as a flat dict of arrays, units on the last axis."""
    z = z or open_zip()
    raw = sio.loadmat(io.BytesIO(z.read("data/cubeFile/cube.mat")), squeeze_me=True,
                      struct_as_record=False)["cube"]
    out = {}
    _walk(raw, "", out)
    # name is 1 x 22 x 743 chars; scipy gives 22 strings of 743 characters each
    cols = [str(s) for s in np.atleast_1d(out["name"])]
    out["name"] = np.array(["".join(s[i] for s in cols) for i in range(len(cols[0]))])
    return out


def load_units(z=None):
    """Every unit file in matFiles.tar: spike times, events, waveform, name. Read in memory."""
    z = z or open_zip()
    units = []
    with tarfile.open(fileobj=z.open("data/matFiles.tar")) as t:
        for m in t:
            if not m.isfile():
                continue
            d = sio.loadmat(io.BytesIO(t.extractfile(m).read()), squeeze_me=True)
            u = {k: np.atleast_1d(np.asarray(v, float)) for k, v in d.items()
                 if k.startswith("EVT") or k in ("spike", "wave")}
            u["filename"] = str(d["filename"])
            u["neuron"] = str(d["neuron"])
            u["member"] = m.name
            units.append(u)
    return units


# Cue channels by program letter (cubeScriptPR25.m 52-88)
PROGRAM_CHANNELS = {"a": ("EVT09", "EVT12", "EVT11"), "b": ("EVT11", "EVT09", "EVT12"),
                    "c": ("EVT12", "EVT11", "EVT09"), "d": ("EVT09", "EVT12", "EVT10"),
                    "e": ("EVT10", "EVT09", "EVT12"), "f": ("EVT12", "EVT10", "EVT09")}


def trial_onsets(u):
    """Cue onsets in the cube's row order and their tags, as cubeScriptPR25.m builds them."""
    d, p, s = PROGRAM_CHANNELS[u["filename"][15]]
    shock = u.get("EVT01", np.array([]))
    pr = u[p]
    has = np.array([np.any((shock > t) & (shock <= t + 30)) for t in pr])
    onsets = np.concatenate([u[d], pr[has], pr[~has], u[s]])
    tags = np.concatenate([np.full(len(u[d]), 1), np.full(has.sum(), 2),
                           np.full((~has).sum(), 3), np.full(len(u[s]), 4)])
    return onsets, tags


def binned_rates(spikes, onsets, width, n_bins, start=-20.0, floor=True):
    """Rate in (t, t + width] bins from `start` s around each onset; floored as in the code."""
    edges = onsets[:, None] + start + width * np.arange(n_bins + 1)[None, :]
    counts = np.diff(np.searchsorted(spikes, edges, side="right"), axis=1)
    rate = counts / width
    return np.floor(rate) if floor else rate


# ---------------------------------------------------------------- normalization

def z_code(raw, base2):
    """Code normalization: trial z-scores over all trials x bins of a unit (16, bins, units)."""
    diff = raw - base2[:, None, :]
    mu = diff.mean(axis=(0, 1), keepdims=True)
    sd = diff.std(axis=(0, 1), ddof=1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        return (diff - mu) / sd


def type_means(trial_z):
    """Per unit means of trial values by type: danger, unc shock, unc omission, safety, unc."""
    return {"D": trial_z[DANGER].mean(0), "US": trial_z[UNC_SHOCK].mean(0),
            "UO": trial_z[UNC_OMIT].mean(0), "S": trial_z[SAFETY].mean(0),
            "U": trial_z[UNC].mean(0)}


def z_methods(raw, n_types=3, base_bins=slice(72, 80)):
    """Methods' normalization: per type mean rate, minus that type's mean in the 2 s before cue
    onset (250-ms bins 73-80), z-scored over the bins of all types (three types with
    uncertainty pooled, z-b, or four, z-a). Returns per-unit type means (bins, units)."""
    m = type_means(raw)
    keys = ("D", "U", "S") if n_types == 3 else ("D", "US", "UO", "S")
    diffs = {k: m[k] - m[k][base_bins].mean(0, keepdims=True) for k in ("D", "US", "UO", "S", "U")}
    stack = np.concatenate([diffs[k] for k in keys], axis=0)
    mu, sd = stack.mean(0), stack.std(0, ddof=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return {k: (diffs[k] - mu) / sd for k in diffs}


# ---------------------------------------------------------------- statistics

def _nested_se(xb, rng, n_boot_std):
    """Standard error of the mean of each row of xb from n_boot_std bootstrap samples of it."""
    n = xb.shape[1]
    out = np.empty(len(xb))
    for i, row in enumerate(xb):
        out[i] = row[rng.integers(0, n, size=(n_boot_std, n))].mean(1).std(ddof=1)
    return out


def boot_ci(x, rng, n_boot=1000, alpha=0.05, n_boot_std=0):
    """Studentized bootstrap CI of the mean (bootci 'student'). Standard errors are s / sqrt(n),
    or with n_boot_std > 0 from that many nested bootstrap samples, as bootci does by default.
    Returns mean, low, high."""
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    n = len(x)
    m, se = x.mean(), x.std(ddof=1) / np.sqrt(n)
    if n_boot_std:
        se = _nested_se(x[None], rng, n_boot_std)[0]
    idx = rng.integers(0, n, size=(n_boot, n))
    xb = x[idx]
    mb = xb.mean(1)
    seb = _nested_se(xb, rng, n_boot_std) if n_boot_std else xb.std(1, ddof=1) / np.sqrt(n)
    with np.errstate(invalid="ignore", divide="ignore"):
        t = (mb - m) / seb
    t = t[np.isfinite(t)]
    lo_t, hi_t = np.quantile(t, [1 - alpha / 2, alpha / 2])
    return m, m - lo_t * se, m - hi_t * se


def excludes_zero(ci):
    return ci[1] > 0 or ci[2] < 0


def ci_sign(ci):
    """+1 above zero, -1 below, 0 includes zero."""
    return 1 if ci[1] > 0 else (-1 if ci[2] < 0 else 0)


def mixed_anova(y, groups=None, type3=True):
    """ANOVA with subjects on axis 0, one or two within factors on the next axes, and an
    optional between factor (`groups`, one label per subject). Sums of squares from the
    per-subject centred data; within effects are tested against effect x subject (within
    group); with groups of unequal size, the within main effect uses the unweighted mean of the
    group means and the harmonic mean group size (type III, as SPSS reports it). Uncorrected
    degrees of freedom; the Greenhouse-Geisser epsilon and p are added as a variant.
    type3=False gives the weighted within main effect (grand mean over all subjects).
    Returns {effect: (F, df1, df2, p, partial eta2, GG epsilon, GG p)}."""
    y = np.asarray(y, float)
    n = y.shape[0]
    wshape = y.shape[1:]
    nw = int(np.prod(wshape))
    g = np.zeros(n, int) if groups is None else np.unique(np.asarray(groups), return_inverse=True)[1]
    ng = g.max() + 1
    out = {}

    def add(name, ss, df1, sse, df2, eps=1.0):
        F = (ss / df1) / (sse / df2)
        out[name] = (F, df1, df2, stats.f.sf(F, df1, df2), ss / (ss + sse),
                     eps, stats.f.sf(F, df1 * eps, df2 * eps))

    subj = y.reshape(n, -1).mean(1)
    if ng > 1:
        gm = np.array([subj[g == k].mean() for k in range(ng)])
        ss_g = nw * sum((g == k).sum() * (gm[k] - subj.mean()) ** 2 for k in range(ng))
        ss_sg = nw * sum(((subj[g == k] - gm[k]) ** 2).sum() for k in range(ng))
        add("group", ss_g, ng - 1, ss_sg, n - ng)

    def effect(r, reps, name, df1):
        # r: per subject residual table for this effect (n, levels...), reps = cells averaged
        eps = gg_epsilon(r.reshape(n, -1), g, r.shape[1:])
        rm = r.mean(0)
        ss = reps * n * (rm ** 2).sum()
        if ng > 1 and type3:
            # SPSS (type III): the within main effect uses the unweighted mean of the group
            # means and the harmonic mean group size
            gmeans = np.array([r[g == k].mean(0) for k in range(ng)])
            n_h = ng / np.sum(1.0 / np.bincount(g))
            ss = reps * ng * n_h * (gmeans.mean(0) ** 2).sum()
        sse = 0.0
        ss_gx = 0.0
        for k in range(ng):
            rk = r[g == k]
            mk = rk.mean(0)
            sse += reps * ((rk - mk) ** 2).sum()
            ss_gx += reps * len(rk) * ((mk - rm) ** 2).sum()
        add(name, ss, df1, sse, (n - ng) * df1, eps)
        if ng > 1:
            add(f"{name} x group", ss_gx, df1 * (ng - 1), sse, (n - ng) * df1, eps)

    if len(wshape) == 1:
        r = y - subj[:, None]
        effect(r, 1, "w1", wshape[0] - 1)
    else:
        a, b = wshape
        ma = y.mean(2) - subj[:, None]
        mb = y.mean(1) - subj[:, None]
        effect(ma, b, "w1", a - 1)
        effect(mb, a, "w2", b - 1)
        inter = y - y.mean(2, keepdims=True) - y.mean(1, keepdims=True) + subj[:, None, None]
        effect(inter, 1, "w1 x w2", (a - 1) * (b - 1))
    return out


def _helmert(k):
    """Orthonormal contrasts (k - 1, k)."""
    c = np.zeros((k - 1, k))
    for i in range(1, k):
        c[i - 1, :i] = 1.0 / i
        c[i - 1, i] = -1.0
        c[i - 1] /= np.linalg.norm(c[i - 1])
    return c


def gg_epsilon(r, g, shape):
    """Greenhouse-Geisser epsilon of a within effect, from its orthonormal contrasts
    (a variant: the claims file names it; the paper does not say whether it was used)."""
    if len(shape) == 1:
        C = _helmert(shape[0])
    else:
        C = np.kron(_helmert(shape[0]), _helmert(shape[1]))
    yc = r @ C.T
    for k in np.unique(g):
        yc[g == k] -= yc[g == k].mean(0)
    S = yc.T @ yc / max(len(r) - len(np.unique(g)), 1)
    k = C.shape[0]
    return float(np.trace(S) ** 2 / (k * np.trace(S @ S)))


def meng_z(r1, r2, rx, n):
    """Meng, Rosenthal & Rubin (1992) Z for two correlations sharing one variable."""
    z1, z2 = np.arctanh(r1), np.arctanh(r2)
    r2bar = (r1 ** 2 + r2 ** 2) / 2
    f = min((1 - rx) / (2 * (1 - r2bar)), 1.0)
    h = (1 - f * r2bar) / (1 - r2bar)
    z = (z1 - z2) * np.sqrt((n - 3) / (2 * (1 - rx) * h))
    return z, 2 * stats.norm.sf(abs(z))


def regress_betas(y, X):
    """MATLAB regress: least squares with QR and column pivoting; on rank deficiency the
    coefficients of dependent columns are 0 (a basic solution). y (16, bins), X (16, p)."""
    from scipy.linalg import qr
    Q, R, piv = qr(X, mode="economic", pivoting=True)
    d = np.abs(np.diag(R))
    tol = max(X.shape) * np.finfo(float).eps * (d[0] if d.size else 0)
    rank = int((d > tol).sum())
    b = np.zeros((X.shape[1], y.shape[1]))
    if rank:
        sol = np.linalg.solve(R[:rank, :rank], Q[:, :rank].T @ y)
        b[piv[:rank]] = sol
    return b, rank


def waveform_measures(wave):
    """Half duration (ms) and amplitude ratio as rrfAnalysis.m computes them (1-based indices
    kept: the code adds the valley index to a 1-based post-valley index)."""
    v = int(np.argmin(wave))                     # 0-based valley
    pre = wave[: v + 1].max()
    post_loc = int(np.argmax(wave[v:])) + 1      # 1-based within wave(v:end)
    post_abs = post_loc + (v + 1)                # code: maxPostValleyLocation + valleyLocation
    half = ((post_abs - (v + 1)) / 2) / 40
    p = pre - wave[0]
    n = wave[0] - wave[v]
    return half, (n - p) / (n + p)


# ---------------------------------------------------------------- cluster patterns

CLUSTERS = ("k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8")
WHOLE = b250(81, 128)          # 10-s cue and 2-s delay
CUE10 = b250(81, 120)


def cluster_profile(means, sel):
    """Mean normalized firing (D, U, S) of the units in `sel` in each period used by the
    patterns. `means` holds per-unit 250-ms type means (bins, units)."""
    per = {"onset": ONSET, "late": LATE, "delay": DELAY, "whole": WHOLE, "cue10": CUE10,
           "late+delay": b250(101, 128)}
    return {p: np.array([np.nanmean(means[t][s][:, sel]) for t in "DUS"]) for p, s in per.items()}


def pattern_checks(pr):
    """The patterns of Results, 'Diverse cue firing patterns', paragraph 3 (and Figure 3), as
    sign tests on a cluster's mean D, U, S firing in the cluster's Figure 3 interval. The
    tests are this attempt's reading of the paper's words; they are listed here so that they
    can be checked. Returns {paper cluster: [(test, passed)]}."""
    on, wh, ld, dl, cue = pr["onset"], pr["whole"], pr["late+delay"], pr["delay"], pr["cue10"]
    D, U, S = 0, 1, 2
    return {
        "k1": [("onset D > 0", on[D] > 0), ("onset D > U and D > S", on[D] > max(on[U], on[S])),
               ("onset U and S similar: |U - S| < D - U", abs(on[U] - on[S]) < on[D] - on[U]),
               ("phasic: onset D > delay D", on[D] > dl[D])],
        "k2": [("U < 0", wh[U] < 0), ("U below D and S", wh[U] < min(wh[D], wh[S])),
               ("D not inhibited as strongly: |D| < |U|", abs(wh[D]) < abs(wh[U]))],
        "k3": [("D > U > S", wh[D] > wh[U] > wh[S]), ("D > 0", wh[D] > 0),
               ("sustained: onset and delay D > 0", on[D] > 0 and dl[D] > 0),
               ("sustained: delay D at least half of onset D", dl[D] >= 0.5 * on[D])],
        "k4": [("D < 0 and U < 0", wh[D] < 0 and wh[U] < 0),
               ("D and U similar: |D - U| < U-S distance", abs(wh[D] - wh[U]) < abs(wh[S] - wh[U])),
               ("S above U", wh[S] > wh[U])],
        "k5": [("D > U > S", ld[D] > ld[U] > ld[S]), ("D > 0", ld[D] > 0),
               ("ramping: late+delay D > onset D", ld[D] > on[D]),
               ("ramping: late+delay U > onset U", ld[U] > on[U])],
        "k6": [("D < U < S", wh[D] < wh[U] < wh[S]), ("D < 0", wh[D] < 0), ("S > 0", wh[S] > 0)],
        "k7": [("delay D > U > S", dl[D] > dl[U] > dl[S]), ("delay D > 0", dl[D] > 0),
               ("minimal cue: |cue D| < delay D", abs(cue[D]) < dl[D])],
        "k8": [("D < 0", wh[D] < 0), ("D below U and S", wh[D] < min(wh[U], wh[S])),
               ("U and S similar: |U - S| < U - D", abs(wh[U] - wh[S]) < wh[U] - wh[D])],
    }


def match_clusters(means, labels):
    """Match found clusters to k1..k8: Hungarian assignment maximizing the fraction of each
    paper cluster's pattern tests passed. Returns {paper cluster: found label}, the score table."""
    from scipy.optimize import linear_sum_assignment
    found = np.unique(labels)
    score = np.zeros((len(found), 8))
    for i, f in enumerate(found):
        chk = pattern_checks(cluster_profile(means, labels == f))
        for j, k in enumerate(CLUSTERS):
            score[i, j] = np.mean([bool(v) for _, v in chk[k]])
    r, cidx = linear_sum_assignment(-score)
    return {CLUSTERS[j]: found[i] for i, j in zip(r, cidx)}, score


# ---------------------------------------------------------------- MATLAB k-means

# rrfAnalysis.m maps its k-means cluster numbers to the paper's names: idx == 5 is k1, 6 k2,
# 7 k3, 1 k4, 4 k5, 8 k6, 3 k7, 2 k8 ("Separate cue-responsive units into clusters").
CODE_IDX = {"k1": 5, "k2": 6, "k3": 7, "k4": 1, "k5": 4, "k6": 8, "k7": 3, "k8": 2}


def matlab_kmeans(X, k, seed=1, max_iter=100, replicates=1, all_runs=False):
    """MATLAB `rng(seed); kmeans(X, k)` with its defaults: k-means++ seeding (the first centre
    drawn uniformly, the others by distance-weighted sampling with one uniform draw each, as
    datasample does), then batch Lloyd updates until no assignment changes (OnlinePhase off).
    MATLAB's default generator is the Mersenne Twister, whose doubles from seed s equal
    numpy's RandomState(s).random_sample(). Returns 1-based labels, as MATLAB's idx, and the
    summed squared distances of each cluster (sumd). With `replicates`, the runs continue one
    stream and the run of least total sumd is returned (an assumption about how
    'Replicates' draws, which the code never uses); `all_runs` returns every run."""
    rs = np.random.RandomState(seed)
    runs = [_kmeans_once(X, k, rs, max_iter) for _ in range(replicates)]
    if all_runs:
        return runs
    return min(runs, key=lambda r: r[1].sum())


def _kmeans_once(X, k, rs, max_iter):
    n = len(X)
    centres = [X[int(np.floor(rs.random_sample() * n))]]
    md = np.full(n, np.inf)
    for _ in range(1, k):
        md = np.minimum(md, ((X - centres[-1]) ** 2).sum(1))
        edges = np.minimum(np.concatenate([[0.0], np.cumsum(md / md.sum())]), 1.0)
        edges[-1] = 1.0
        centres.append(X[np.searchsorted(edges, rs.random_sample(), side="right") - 1])
    C = np.array(centres)
    lab = None
    for _ in range(max_iter):
        new = ((X[:, None, :] - C[None]) ** 2).sum(2).argmin(1)
        if lab is not None and (new == lab).all():
            break
        lab = new
        C = np.array([X[lab == j].mean(0) if (lab == j).any() else C[j] for j in range(k)])
    sumd = np.bincount(lab, weights=((X - C[lab]) ** 2).sum(1), minlength=k)
    return lab + 1, sumd
