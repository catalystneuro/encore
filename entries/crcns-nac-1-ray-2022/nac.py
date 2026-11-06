"""Loading and measures for CRCNS data set nac-1 (Ray, Moaddab & McDannald 2022, J Neurosci 42:817).

The data set is one zip file, `nac-1/live/data.zip`, in the public bucket crcnsarchive. It is
opened in place over HTTP range requests (fsspec and zipfile) and nothing is written to disk. It
holds one MATLAB file per single unit (`data/matFiles/*.mat`): spike times (`spike`, s), the mean
waveform (`wave`, 32 points), and the event channels of the session (`EVTnn`, s). The data
description does not say what the channels hold; the map below is the one written in the
authors' script `data/cubeScriptPR25.m`, which is part of the data set:

- EVT01 foot shock, EVT02 pellet (feeder advance), EVT13 nose poke;
- the three cue channels depend on the behavior program, the 16th character of the file name
  (`programType = filename(16)`), and are assigned there to danger (shock p = 1), uncertainty
  (p = 0.25) and safety (p = 0) for programs a to f;
- uncertainty trials with a shock within 30 s of cue onset are shock trials, the others omission
  trials (same script).

The file name is `acRRMMDDYYepr25P` (rat RR, date MM/DD/YY, program P), and the unit name is
`SPKnnx`. The authors' analysis script `data/NAccAnalysis/mainAnalysis.m` is also in the data
set; the paper links no code, so these scripts are the paper's code read here.

Where the parameters come from (claim ids in brackets):

- Trials are ordered as the data description orders the rows of its cube: 4 danger, 2
  uncertainty shock, 6 uncertainty omission, 4 safety, each in time order.
- Spike and poke counts use half-open windows (t0, t1], as `cubeScriptPR25.m` does.
- Suppression ratio per trial, 20-s baseline and 10-s cue poke rates, from the Methods
  (Calculating suppression ratios). A trial with no pokes in either window gives 0/0; the claims
  file names two readings (left out, or 0) and the authors' script sets it to 1 (variant).
- The cue-responsive screen, normalization (`norm_methods`), cue windows, the ANOVA bins and the
  bootstrap follow the claims file's opening comment, which cites the Methods.
- `norm_code` is the normalization of `cubeScriptPR25.m` (per trial, minus the trial's 2-s
  pre-cue rate, z-scored over all trials and bins of the unit, with rates floored to integers);
  it is a variant only.
- The bootstrap is studentized with the analytic standard error of the mean in each resample;
  MATLAB `bootci` estimates that standard error by an inner bootstrap. This is a standard choice
  that cannot move a bound by more than resampling noise.
- `HD_BOUNDARY` (0.3875 ms) is from `data/NAccAnalysis/halfDuration.m`; the dashed line of
  Figure 3C, read from the PDF, sits at about 0.39 ms. The waveform measure `peak_valley`
  follows `mainAnalysis.m` without its final division by 2 (see its docstring), so that its
  values span the 0.15 to 0.6 ms of Figure 3C (fig3c-waveform-bimodal).
- The ITI windows for reward and nose poke cessation events are the two readings of the claims
  file (fig9a-reward-firing); `iti_events_code` is the script's window (18 to 2 s before cue
  onset, and 14 to 28 s after it), shown as a variant.
"""

from __future__ import annotations

import io
import zipfile

import fsspec
import numpy as np
import scipy.io as sio
from scipy import stats

DATASET_ID = "nac-1"
DATASET_VERSION = "unversioned"  # CRCNS data sets are not versioned; data.zip is pinned by its MD5
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/nac-1/live/data.zip"
DATA_MD5 = "ab13407080360d7d683ef818ae66f33a"  # checksums.md5 of the data set, for data.zip

# cubeScriptPR25.m: cue channels per program (danger, uncertainty, safety)
PROGRAM_CHANNELS = {
    "a": ("EVT09", "EVT12", "EVT11"),
    "b": ("EVT11", "EVT09", "EVT12"),
    "c": ("EVT12", "EVT11", "EVT09"),
    "d": ("EVT09", "EVT12", "EVT10"),
    "e": ("EVT10", "EVT09", "EVT12"),
    "f": ("EVT12", "EVT10", "EVT09"),
}
TRIAL_TYPES = np.array([0] * 4 + [1] * 2 + [2] * 6 + [3] * 4)  # danger, unc shock, unc omission, safety
CUE_OF_TRIAL = np.array([0] * 4 + [1] * 8 + [2] * 4)  # danger, uncertainty, safety

BIN = 0.25
EDGES = np.arange(-20, 30 + BIN / 2, BIN)  # 200 bins of 250 ms, 20 s before onset to 20 s after offset
ONSET_BIN = 80  # first bin after cue onset
ANOVA_BINS = slice(ONSET_BIN - 8, ONSET_BIN + 40)  # 2 s before onset to offset, 48 bins
ONSET = slice(ONSET_BIN, ONSET_BIN + 4)  # first 1 s of the cue
LATE = slice(ONSET_BIN + 20, ONSET_BIN + 40)  # last 5 s
WHOLE_CUE = slice(ONSET_BIN, ONSET_BIN + 40)
BASE10 = slice(ONSET_BIN - 40, ONSET_BIN)  # 10 s before onset
HD_BOUNDARY = (0.375 + 0.4) / 2  # halfDuration.m

POPULATIONS = ["Threat Excited", "Threat Inhibited", "Danger Excited", "Bidirectional Valence",
               "Non-Selective"]
MAIN3 = ["Threat Inhibited", "Danger Excited", "Bidirectional Valence"]


def open_zip():
    f = fsspec.open(URL, block_size=2**22).open()
    return zipfile.ZipFile(f)


def load_units():
    """Read every unit file; return a list of dicts, one per unit, in file-name order."""
    z = open_zip()
    names = sorted(n for n in z.namelist() if n.startswith("data/matFiles/") and n.endswith(".mat"))
    units = []
    for n in names:
        m = sio.loadmat(io.BytesIO(z.read(n)), squeeze_me=True)
        fname = str(m["filename"])
        prog = fname[15]
        chans = PROGRAM_CHANNELS[prog]
        ev = {k: np.atleast_1d(np.asarray(m[k], float)) for k in m if k.startswith("EVT")}
        danger, unc, safety = (np.sort(ev[c]) for c in chans)
        shock = np.sort(ev["EVT01"])
        unc_shock = np.array([t for t in unc if np.any((shock > t) & (shock <= t + 30))])
        unc_omit = np.array([t for t in unc if not np.any((shock > t) & (shock <= t + 30))])
        onsets = np.concatenate([danger, unc_shock, unc_omit, safety])
        units.append(dict(
            file=n.split("/")[-1], filename=fname, neuron=str(m["neuron"]),
            rat=fname[:4], date=fname[4:10], program=prog, session=fname[:10],
            spikes=np.sort(np.atleast_1d(np.asarray(m["spike"], float))),
            wave=np.asarray(m["wave"], float), onsets=onsets,
            n_type=(len(danger), len(unc_shock), len(unc_omit), len(safety)),
            shock=shock, pellet=np.sort(ev["EVT02"]), poke=np.sort(ev["EVT13"]),
            channels=sorted(ev),
        ))
    return units


def load_cube():
    """The authors' precomputed cube (data/cubeFile/cube.mat), used only to check the loading."""
    z = open_zip()
    m = sio.loadmat(io.BytesIO(z.read("data/cubeFile/cube.mat")), struct_as_record=False)
    return m["cube"][0, 0]


def count_in(times, t0, t1):
    """Counts of `times` in (t0, t1], vectorized over t0 and t1."""
    return np.searchsorted(times, t1, side="right") - np.searchsorted(times, t0, side="right")


def binned_rates(times, onsets, edges=EDGES):
    """Rate (Hz) per trial and bin, bins (onset + edges[i], onset + edges[i+1]]."""
    t = onsets[:, None] + edges[None, :]
    c = np.searchsorted(times, t, side="right")
    return np.diff(c, axis=1) / np.diff(edges)[None, :]


def window_rate(times, onsets, a, b):
    return count_in(times, onsets + a, onsets + b) / (b - a)


# ---------------------------------------------------------------- behavior

def suppression(u, nan_reading="drop"):
    """Per-trial suppression ratio; nan_reading 'drop' (NaN kept), 'zero' or 'one' (script)."""
    base = count_in(u["poke"], u["onsets"] - 20, u["onsets"]) * 3.0  # pokes/min
    cue = count_in(u["poke"], u["onsets"], u["onsets"] + 10) * 6.0
    with np.errstate(invalid="ignore", divide="ignore"):
        sr = (base - cue) / (base + cue)
    if nan_reading == "zero":
        sr = np.where(np.isnan(sr), 0.0, sr)
    elif nan_reading == "one":
        sr = np.where(np.isnan(sr), 1.0, sr)
    return sr, base


# ---------------------------------------------------------------- screen

def screen(u, unc="pooled", floor=False):
    """Paired two-tailed t-tests of the 10-s baseline against the first 1 s and the last 5 s of
    each cue. unc 'pooled' tests the eight uncertainty trials as one cue; 'split' tests shock
    and omission trials as two cues. floor=True floors the rates as cubeScriptPR25.m does.
    Returns (responsive, list of (cue, window, p))."""
    on = u["onsets"]
    base = window_rate(u["spikes"], on, -10, 0)
    first = window_rate(u["spikes"], on, 0, 1)
    last = window_rate(u["spikes"], on, 5, 10)
    if floor:
        base, first, last = np.floor(base), np.floor(first), np.floor(last)
    groups = ([("danger", TRIAL_TYPES == 0), ("uncertainty", (TRIAL_TYPES == 1) | (TRIAL_TYPES == 2)),
               ("safety", TRIAL_TYPES == 3)] if unc == "pooled" else
              [("danger", TRIAL_TYPES == 0), ("unc shock", TRIAL_TYPES == 1),
               ("unc omission", TRIAL_TYPES == 2), ("safety", TRIAL_TYPES == 3)])
    res = []
    for name, sel in groups:
        for wname, w in (("onset", first), ("late", last)):
            d = w[sel] - base[sel]
            if np.all(d == d[0]):
                p = np.nan  # zero variance: MATLAB ttest gives NaN, the script counts it as not significant
            else:
                p = stats.ttest_rel(w[sel], base[sel]).pvalue
            res.append((name, wname, p))
    responsive = any(p < 0.05 for _, _, p in res if np.isfinite(p))
    return responsive, res


# ---------------------------------------------------------------- normalization

def norm_methods(u, types=4, collapse="trials", bin_s=BIN):
    """Normalized firing per cue (danger, uncertainty, safety) x 200 bins of 250 ms.

    Methods (Z-score normalization): per trial type, mean rate per bin over trials, minus the
    type's mean over the 10 s before onset, then z-scored over all types and bins of the unit.
    types 4 (danger, unc shock, unc omission, safety) or 3 (uncertainty as one type);
    collapse 'trials' (mean over the eight uncertainty trials) or 'types' (mean of the shock and
    omission traces). bin_s other than 0.25 s gives the same normalization in other bins (used
    for the 1-s reading of fig6). Returns (traces 3 x bins, sd used, mean used)."""
    edges = np.arange(-20, 30 + bin_s / 2, bin_s)
    r = binned_rates(u["spikes"], u["onsets"], edges)
    base = (edges[:-1] >= -10 - 1e-9) & (edges[:-1] < 0 - 1e-9)
    if types == 4:
        groups = [TRIAL_TYPES == k for k in range(4)]
    else:
        groups = [CUE_OF_TRIAL == k for k in range(3)]
    tr = np.array([r[g].mean(0) for g in groups])
    tr = tr - tr[:, base].mean(1, keepdims=True)
    mu, sd = tr.mean(), tr.std(ddof=1)
    z = (tr - mu) / sd
    if types == 4:
        if collapse == "trials":
            # mean over the eight trials = (2 * shock trace + 6 * omission trace) / 8
            unc = (2 * z[1] + 6 * z[2]) / 8
        else:
            unc = (z[1] + z[2]) / 2
        out = np.array([z[0], unc, z[3]])
    else:
        out = z
        if collapse == "types":
            # three-type z-score with the uncertainty trace as the mean of the two type traces
            r4 = np.array([r[TRIAL_TYPES == k].mean(0) for k in range(4)])
            r4 = r4 - r4[:, base].mean(1, keepdims=True)
            unc = (r4[1] + r4[2]) / 2
            tr3 = np.array([r4[0], unc, r4[3]])
            mu, sd = tr3.mean(), tr3.std(ddof=1)
            out = (tr3 - mu) / sd
    return out, sd, mu


def trial_code(u, bin_s=1.0):
    """The authors' per-trial normalization (cubeScriptPR25.m) in bins of bin_s: floored rates
    minus the floored 2-s pre-cue rate, z-scored over all 16 trials and bins."""
    edges = np.arange(-20, 30 + bin_s / 2, bin_s)
    r = np.floor(binned_rates(u["spikes"], u["onsets"], edges))
    b2 = np.floor(window_rate(u["spikes"], u["onsets"], -2, 0))
    d = r - b2[:, None]
    s = d.std(ddof=1)
    return (d - d.mean()) / (s if s > 0 else np.nan)


def norm_code(u):
    """The authors' script: per trial, floored rates minus the floored 2-s pre-cue rate,
    z-scored over all 16 trials x 200 bins; then the mean per cue."""
    r = np.floor(binned_rates(u["spikes"], u["onsets"]))
    b2 = np.floor(window_rate(u["spikes"], u["onsets"], -2, 0))
    d = r - b2[:, None]
    z = (d - d.mean()) / d.std(ddof=1)
    return np.array([z[CUE_OF_TRIAL == k].mean(0) for k in range(3)]), z


NORM_READINGS = {
    "N1 4 types, unc = mean of 8 trials": dict(types=4, collapse="trials"),
    "N2 4 types, unc = mean of 2 type traces": dict(types=4, collapse="types"),
    "N3 3 types, unc = mean of 8 trials": dict(types=3, collapse="trials"),
    "N4 3 types, unc = mean of 2 type traces": dict(types=3, collapse="types"),
}


def epochs(tr):
    """Six clustering epochs: onset (first 1 s) and late (last 5 s) firing, danger, unc, safety."""
    return np.concatenate([tr[:, ONSET].mean(1), tr[:, LATE].mean(1)])


# ---------------------------------------------------------------- per-trial normalization

def trial_norm(u, reading, sd, bin_s=1.0, nan_sr="drop"):
    """Per-trial normalized firing, trials x bins of `bin_s` from 20 s before onset to 30 s after.

    (a) each trial's rate minus that trial's 10-s pre-cue mean, divided by the unit's SD from
        the Methods normalization; (b) the same with the trial-type 10-s baseline subtracted;
    (c) each trial's binned rate z-scored over all trials and bins of the unit."""
    edges = np.arange(-20, 30 + bin_s / 2, bin_s)
    r = binned_rates(u["spikes"], u["onsets"], edges)
    b = window_rate(u["spikes"], u["onsets"], -10, 0)
    if reading == "a":
        return (r - b[:, None]) / sd, edges
    if reading == "b":
        tb = np.array([b[TRIAL_TYPES == TRIAL_TYPES[i]].mean() for i in range(16)])
        return (r - tb[:, None]) / sd, edges
    if reading == "c":
        s = r.std(ddof=1)
        return (r - r.mean()) / (s if s > 0 else np.nan), edges
    raise ValueError(reading)


def ols_betas(y, X):
    """Betas of y (n x k) on X (n x p) with a constant; NaN when X is rank deficient."""
    Xc = np.column_stack([np.ones(len(X)), X])
    if np.linalg.matrix_rank(Xc) < Xc.shape[1]:
        return np.full((Xc.shape[1] - 1,) + y.shape[1:], np.nan)
    b, *_ = np.linalg.lstsq(Xc, y, rcond=None)
    return b[1:]


def pattern(u_value):
    return np.where(CUE_OF_TRIAL == 0, 1.0, np.where(CUE_OF_TRIAL == 2, 0.0, u_value))


# ---------------------------------------------------------------- events in the ITI

def iti_events(times, u, reading):
    """Events whose [-2, +2] s window lies in the ITI.
    (a) outside every [onset - 20, onset + 30] s; (b) not overlapping any cue [onset, onset + 10]
    or shock [shock, shock + 0.5]."""
    on = u["onsets"]
    keep = []
    for t in times:
        lo, hi = t - 2, t + 2
        if reading == "a":
            bad = np.any((hi > on - 20) & (lo < on + 30))
        else:
            bad = np.any((hi > on) & (lo < on + 10)) or np.any((hi > u["shock"]) & (lo < u["shock"] + 0.5))
        if not bad:
            keep.append(t)
    return np.array(keep)


def iti_events_code(times, u):
    on = u["onsets"]
    sel = [t for t in times if np.any(((t >= on - 18) & (t <= on - 2)) | ((t >= on + 14) & (t <= on + 28)))]
    return np.array(sorted(sel))


def cessations(u, reading):
    """Nose pokes followed by at least 2 s without a poke, in the ITI (reading as iti_events)."""
    p = u["poke"]
    gap = np.diff(p)
    cand = p[:-1][gap >= 2]
    if reading == "code":
        on = u["onsets"]
        out = []
        for i in range(len(on)):
            a = p[(p >= on[i] - 18) & (p <= on[i] - 2)]
            if len(a) > 1:
                out.extend(a[:-1][np.diff(a) > 2])
        return np.array(sorted(out))
    return iti_events(cand, u, reading)


def event_trace(u, events, norm, sd=None):
    """Firing in 16 bins of 250 ms from 2 s before to 2 s after each event, averaged over events,
    minus the mean of the 1 s before. norm 'sd' divides by the unit's cue-normalization SD
    (reading i); 'z16' z-scores the 16-bin mean trace (reading ii); 'code' follows the script
    (floored rates, per event minus its 1-s pre mean, z-scored over all events and bins, then
    averaged). Returns NaN when there is no event."""
    if len(events) == 0:
        return np.full(16, np.nan)
    edges = np.arange(-2, 2 + BIN / 2, BIN)
    r = binned_rates(u["spikes"], events, edges)
    if norm == "code":
        r = np.floor(r)
        d = r - r[:, :4].mean(1, keepdims=True)
        s = d.std(ddof=1) if d.size > 1 else np.nan
        return ((d - d.mean()) / s).mean(0) if s > 0 else np.full(16, np.nan)
    m = r.mean(0)
    m = m - m[:4].mean()
    if norm == "sd":
        return m / sd
    s = m.std(ddof=1)
    return (m - m.mean()) / s if s > 0 else np.full(16, np.nan)


# ---------------------------------------------------------------- statistics

def boot_ci(x, rng, n_boot=1000, level=0.95, mirrored=False):
    """Studentized bootstrap CI of the mean (bootci 'student', analytic SE per resample)."""
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    n = len(x)
    if n < 3:
        return np.nan, np.nan, np.nan
    m, se = x.mean(), x.std(ddof=1) / np.sqrt(n)
    idx = rng.integers(0, n, size=(n_boot, n))
    xb = x[idx]
    mb = xb.mean(1)
    seb = xb.std(1, ddof=1) / np.sqrt(n)
    with np.errstate(divide="ignore", invalid="ignore"):
        t = (mb - m) / seb
    t = t[np.isfinite(t)]
    a = (1 - level) / 2
    q_lo, q_hi = np.quantile(t, a), np.quantile(t, 1 - a)
    if mirrored:
        # the quantiles of t added without reflection; this form matches the paper's printed
        # bounds (see the notebook, fig1g-discrimination), it is a variant only
        return m, m + q_lo * se, m + q_hi * se
    return m, m - q_hi * se, m - q_lo * se


def rm_anova2(Y):
    """Two-way repeated-measures ANOVA, Y subjects x A x B. Returns dict of (F, df1, df2, p)
    for A, B and AxB (uncorrected, as MATLAB ranova reports by default)."""
    n, a, b = Y.shape
    G = Y.mean()
    mS = Y.mean((1, 2))
    mA = Y.mean((0, 2))
    mB = Y.mean((0, 1))
    mAS = Y.mean(2)
    mBS = Y.mean(1)
    mAB = Y.mean(0)
    ss_A = n * b * ((mA - G) ** 2).sum()
    ss_B = n * a * ((mB - G) ** 2).sum()
    ss_AB = n * ((mAB - mA[:, None] - mB[None, :] + G) ** 2).sum()
    ss_AS = b * ((mAS - mA[None, :] - mS[:, None] + G) ** 2).sum()
    ss_BS = a * ((mBS - mB[None, :] - mS[:, None] + G) ** 2).sum()
    res = Y - mAB[None] - mAS[:, :, None] - mBS[:, None, :] + mA[None, :, None] + mB[None, None, :] + mS[:, None, None] - G
    ss_ABS = (res ** 2).sum()
    out = {}
    for k, ss, df, sse, dfe in (("A", ss_A, a - 1, ss_AS, (a - 1) * (n - 1)),
                                ("B", ss_B, b - 1, ss_BS, (b - 1) * (n - 1)),
                                ("AxB", ss_AB, (a - 1) * (b - 1), ss_ABS, (a - 1) * (b - 1) * (n - 1))):
        F = (ss / df) / (sse / dfe)
        out[k] = (F, df, dfe, stats.f.sf(F, df, dfe))
    return out


def rm_anova1(Y):
    """One-way repeated-measures ANOVA, Y subjects x levels."""
    n, a = Y.shape
    G = Y.mean()
    ss_A = n * ((Y.mean(0) - G) ** 2).sum()
    ss_S = a * ((Y.mean(1) - G) ** 2).sum()
    ss_E = ((Y - G) ** 2).sum() - ss_A - ss_S
    df, dfe = a - 1, (a - 1) * (n - 1)
    F = (ss_A / df) / (ss_E / dfe)
    return F, df, dfe, stats.f.sf(F, df, dfe)


def mixed_anova(groups):
    """Split-plot ANOVA: a list of arrays (subjects x levels), one per group. Returns dict of
    (F, df1, df2, p) for group, level, and group x level."""
    Y = np.concatenate(groups)
    g = np.concatenate([[i] * len(x) for i, x in enumerate(groups)]).astype(int)
    N, b = Y.shape
    k = len(groups)
    G = Y.mean()
    mS = Y.mean(1)
    mB = Y.mean(0)
    mG = np.array([x.mean() for x in groups])
    mGB = np.array([x.mean(0) for x in groups])
    ss_G = sum(len(x) * b * (mG[i] - G) ** 2 for i, x in enumerate(groups))
    ss_SG = b * ((mS - mG[g]) ** 2).sum()
    ss_B = N * ((mB - G) ** 2).sum()
    ss_GB = sum(len(x) * ((mGB[i] - mG[i] - mB + G) ** 2).sum() for i, x in enumerate(groups))
    ss_BSG = ((Y - mGB[g] - mS[:, None] + mG[g][:, None]) ** 2).sum()
    df_G, df_SG = k - 1, N - k
    df_B, df_GB, df_BSG = b - 1, (k - 1) * (b - 1), (b - 1) * (N - k)
    out = {}
    for name, ss, df, sse, dfe in (("group", ss_G, df_G, ss_SG, df_SG), ("level", ss_B, df_B, ss_BSG, df_BSG),
                                   ("group x level", ss_GB, df_GB, ss_BSG, df_BSG)):
        F = (ss / df) / (sse / dfe)
        out[name] = (F, df, dfe, stats.f.sf(F, df, dfe))
    return out


def pitman_morgan(x, y):
    """Pitman-Morgan test of equal variances of paired x and y: the correlation of x + y with
    x - y, tested with n - 2 degrees of freedom. Returns (variance ratio var(x)/var(y), r, p)."""
    r, p = stats.pearsonr(x + y, x - y)
    return np.var(x, ddof=1) / np.var(y, ddof=1), r, p


def fisher_independent(r1, n1, r2, n2):
    z = (np.arctanh(r1) - np.arctanh(r2)) / np.sqrt(1 / (n1 - 3) + 1 / (n2 - 3))
    return z, 2 * stats.norm.sf(abs(z))


def steiger_dependent(r12, r13, r23, n):
    """Steiger (1980) Z for two correlations sharing variable 1."""
    rm = (r12 + r13) / 2
    c = (r23 * (1 - 2 * rm**2) - 0.5 * rm**2 * (1 - 2 * rm**2 - r23**2)) / (1 - rm**2) ** 2
    z = (np.arctanh(r12) - np.arctanh(r13)) * np.sqrt(n - 3) / np.sqrt(2 - 2 * c)
    return z, 2 * stats.norm.sf(abs(z))


def dip_test(x, rng, n_sim=1000):
    """Hartigan's dip with a p-value from n_sim uniform samples of the same size, as the
    authors' HartigansDipSignifTest(x, 1000) does."""
    import diptest
    x = np.sort(np.asarray(x, float))
    d = diptest.dipstat(x)
    sims = np.array([diptest.dipstat(np.sort(rng.uniform(size=len(x)))) for _ in range(n_sim)])
    return d, float((sims >= d).mean())


def peak_valley(wave):
    """Peak-valley duration on the scale of Figure 3C: the after-hyperpolarization peak index
    minus the valley index, counted as mainAnalysis.m counts it (its MATLAB index within
    wave(valley:end), which adds one sample), divided by 40 (samples per ms at 32 points over
    0.8 ms). mainAnalysis.m divides this by a further 2 ("HD", half duration), which gives values
    of 0.075 to 0.3, half the 0.15 to 0.6 of Figure 3C; the boundary 0.3875 of halfDuration.m
    falls between the two modes only on the scale used here."""
    v = int(np.argmin(wave))
    post = int(np.argmax(wave[v:])) + 1  # MATLAB index within wave(v:end)
    return post / 40


def peak_valley_ms(wave):
    """Valley to after-hyperpolarization peak in ms at 40 kHz (32 points over 0.8 ms)."""
    v = int(np.argmin(wave))
    return int(np.argmax(wave[v:])) / 40.0


# ---------------------------------------------------------------- clustering

def kmeans_runs(X, k, n_starts, seed):
    """n_starts single k-means++ runs (sklearn, Lloyd). Returns list of (labels, inertia)."""
    from sklearn.cluster import KMeans
    out = []
    for i in range(n_starts):
        km = KMeans(n_clusters=k, n_init=1, init="k-means++", random_state=seed + i).fit(X)
        out.append((km.labels_, km.inertia_))
    return out


def canonical(labels):
    """Relabel a partition by order of first appearance, to compare partitions."""
    mp = {}
    return tuple(mp.setdefault(l, len(mp)) for l in labels)


TEMPLATES = {
    # (danger, uncertainty, safety) at onset, then in the late cue, from the Results' descriptions
    # (NAcc neurons show heterogeneous cue firing, paragraph 2, and Figures 4 and 5)
    "Threat Excited": (1, 1, 0, 0, 0, 0),
    "Threat Inhibited": (-1, -1, 0, -1, -1, 0),
    "Danger Excited": (1, 0.5, 0, 1, 0, 0),
    "Bidirectional Valence": (-1, 0, 0.5, -1, 0, 0),
    "Non-Selective": (1, 1, 1, 0.5, 0.5, 0.5),
}


def name_clusters(X, labels):
    """Name five clusters from their centroids (d_on, u_on, s_on, d_late, u_late, s_late) by the
    Results' descriptions: each centroid is matched one to one to the pattern templates above by
    the largest summed cosine similarity (Hungarian assignment). The templates code the
    descriptions; the assignment is a standard choice. Returns (dict cluster -> name, cosine
    similarity of each cluster to its template)."""
    from scipy.optimize import linear_sum_assignment
    cl = list(np.unique(labels))
    cents = np.array([X[labels == c].mean(0) for c in cl])
    T = np.array([TEMPLATES[p] for p in POPULATIONS], float)
    cos = (cents / np.linalg.norm(cents, axis=1, keepdims=True)) @ (T / np.linalg.norm(T, axis=1, keepdims=True)).T
    r, c = linear_sum_assignment(-cos)
    return {cl[i]: POPULATIONS[j] for i, j in zip(r, c)}, {POPULATIONS[j]: cos[i, j] for i, j in zip(r, c)}
