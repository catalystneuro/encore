"""Loading and measures for CRCNS data set pag-1 (Wright and McDannald 2019, eLife 8:e45013).

The data set is one zip, ``pag-1/live/data.zip``, in the public bucket crcnsarchive. It is
opened in place over HTTP range requests (fsspec and zipfile); nothing is written to disk.
Each of its 245 ``data/mFiles/*.mat`` files holds one unit: the spike times (``spike``, s),
the Plexon event channels of its session (``EVT01`` foot shock, ``EVT02`` pellet, ``EVT09``,
``EVT11`` and ``EVT12`` the three cues, ``EVT13`` nose poke, as listed in the data set's
``cubeScript.m``), the mean waveform (``wave``, 32 points over 0.8 ms), and the session name
(``filename``: rat, date mmddyy, behaviour program ``epr38a/b/c``) and unit name (``neuron``).
The program letter fixes which channel is danger, uncertainty and safety (cubeScript.m).

Where the parameters come from:

- Trial types, cue length (10 s), shock 2 s after cue offset (12 s after onset), 0.5 s long,
  the 32 trials per session: the paper, Materials and methods, Fear discrimination.
- Uncertainty shock and omission trials are told apart by a shock within 30 s of the cue onset,
  as in cubeScript.m (the data set's own script).
- Firing: counts in half-open bins (t0, t1], as cubeScript.m counts them. Raw rate in spikes/s.
- Interval Z firing (Methods, Z-score normalization, paragraph 2): per trial, firing in the
  interval minus the baseline, Z-scored over the 32 trials of the session. The baseline is the
  trial's own 2 s before onset (reading a of detail 4 of the claims file) or the trial type's
  mean 2 s baseline (reading b).
- 100 ms population firing (Methods, Z-score normalization, paragraph 1): per trial type, mean
  rate in 100 ms bins from 10 s before onset to 12 s after offset (320 bins), minus the trial
  type's mean 2 s baseline, Z-scored over all trial types and bins of the neuron.
- Suppression ratio (Methods, Calculating suppression ratios): (baseline rate - cue rate) /
  (baseline rate + cue rate), per trial. The baseline windows are open (detail 1 of the claims
  file, as amended after this attempt's question): interval fear and total fear have separate
  windows ending at cue onset, readings (a) 2 s and 10 s, (b) 2 s and 20 s, (c) 10 s and 20 s.
  Reading b reproduces the Methods regression table, and 20 s is the window of the data set's
  cubeScript.m. A 0/0 ratio is open (detail 2): 0, left out (NaN), or 1 as the table and
  cubeScript.m set it.
"""

from __future__ import annotations

import io
import zipfile

import fsspec
import numpy as np
import scipy.io as sio

DATASET = "pag-1"            # CRCNS data set, doi:10.6080/K0R49P0V
VERSION = "unversioned"      # CRCNS data sets are not versioned (docs/archives.md); MD5 in checksums.md5
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-1/live/data.zip"
CHECKSUMS_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-1/live/checksums.md5"

# cubeScript.m: event channel of each cue for behaviour programs a, b and c
CUE_CHANNELS = {
    "a": {"danger": "EVT09", "uncertainty": "EVT12", "safety": "EVT11"},
    "b": {"danger": "EVT11", "uncertainty": "EVT09", "safety": "EVT12"},
    "c": {"danger": "EVT12", "uncertainty": "EVT11", "safety": "EVT09"},
}
# trial types in the data description's row order: danger, uncertainty shock, uncertainty
# omission, safety (rows 1-6, 7-12, 13-22, 23-32)
TYPES = ("D", "US", "UO", "S")
PROB = {"D": 1.0, "US": 0.375, "UO": 0.375, "S": 0.0}
CUE_S = 10.0
SHOCK_ONSET_S = 12.0   # 2 s after cue offset
SHOCK_LEN_S = 0.5


def open_zip():
    f = fsspec.open(URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def checksums() -> dict:
    with fsspec.open(CHECKSUMS_URL, "rt") as f:
        return {line.split()[1]: line.split()[0] for line in f if line.strip()}


def _arr(m, key):
    return np.asarray(m[key], dtype=float).ravel() if key in m else np.zeros(0)


def load_units() -> list[dict]:
    """Every unit of the data set: spikes, the session's events and trials, and the waveform."""
    z = open_zip()
    names = sorted(n for n in z.namelist() if n.startswith("data/mFiles/") and n.endswith(".mat"))
    units = []
    for n in names:
        m = sio.loadmat(io.BytesIO(z.read(n)))
        session = str(m["filename"][0])
        program = session[15]
        ch = CUE_CHANNELS[program]
        shock = _arr(m, "EVT01")
        onsets, types = [], []
        for cue, chan in ch.items():
            for t in _arr(m, chan):
                if cue == "danger":
                    ty = "D"
                elif cue == "safety":
                    ty = "S"
                else:
                    ty = "US" if np.any((shock > t) & (shock <= t + 30)) else "UO"
                onsets.append(t)
                types.append(ty)
        onsets, types = np.array(onsets), np.array(types)
        # order trials by type (data description order), chronological within type
        key = np.array([TYPES.index(t) for t in types]) * 1e7 + onsets
        o = np.argsort(key)
        units.append(dict(
            file=n.split("/")[-1], session=session, rat=session[:4], program=program,
            unit=str(m["neuron"][0]), spikes=np.sort(_arr(m, "spike")),
            spikes_sorted=bool(np.all(np.diff(_arr(m, "spike")) >= 0)),
            onsets=onsets[o], types=types[o], shock=shock, pokes=_arr(m, "EVT13"),
            pellets=_arr(m, "EVT02"), wave=_arr(m, "wave"),
            channels=sorted(k for k in m if k.startswith("EVT")),
        ))
    return units


def counts(times: np.ndarray, onsets: np.ndarray, start: float, stop: float, width: float):
    """Counts in half-open bins (t0, t1] from onset+start to onset+stop, trials x bins."""
    nb = int(round((stop - start) / width))
    edges = start + width * np.arange(nb + 1)
    out = np.empty((len(onsets), nb))
    for i, t in enumerate(onsets):
        idx = np.searchsorted(times, t + edges, side="right")
        out[i] = np.diff(idx)
    return out


def interval_rate(u: dict, a: float, b: float, times_key: str = "spikes") -> np.ndarray:
    """Rate (events/s) in (onset+a, onset+b] for each of the 32 trials."""
    return counts(u[times_key], u["onsets"], a, b, b - a)[:, 0] / (b - a)


def zscore(x: np.ndarray) -> np.ndarray:
    """Z-score with the sample SD (MATLAB zscore); a constant vector gives zeros."""
    sd = np.std(x, ddof=1)
    return (x - np.mean(x)) / sd if sd > 0 else np.zeros_like(x)


def interval_z(u: dict, a: float, b: float, baseline: str = "trial") -> np.ndarray:
    """Interval Z firing over the 32 trials (Methods, Z-score normalization, paragraph 2).

    baseline "trial": the trial's own 2 s pre-cue rate (reading a of detail 4);
    "type": the trial type's mean 2 s pre-cue rate (reading b)."""
    r = interval_rate(u, a, b)
    base = interval_rate(u, -2.0, 0.0)
    if baseline == "type":
        base = np.array([base[u["types"] == t].mean() for t in u["types"]])
    return zscore(r - base)


def population_z100(u: dict, start: float = -10.0, stop: float = 22.0, split_uncertainty=False):
    """Z-scored 100 ms firing (Methods, Z-score normalization, paragraph 1).

    Returns dict trial type -> 320 bins. Cue analyses collapse uncertainty (D, U, S); post-cue
    analyses split it (D, US, UO, S)."""
    c = counts(u["spikes"], u["onsets"], start, stop, 0.1) * 10.0
    base = interval_rate(u, -2.0, 0.0)
    groups = {"D": ["D"], "U": ["US", "UO"], "S": ["S"]} if not split_uncertainty else \
        {t: [t] for t in TYPES}
    out = {}
    for g, ts in groups.items():
        m = np.isin(u["types"], ts)
        out[g] = c[m].mean(0) - base[m].mean()
    allv = np.concatenate(list(out.values()))
    mu, sd = allv.mean(), allv.std(ddof=1)
    return {g: (v - mu) / sd if sd > 0 else v * 0 for g, v in out.items()}


def suppression(base_rate: np.ndarray, cue_rate: np.ndarray, zero: str = "one") -> np.ndarray:
    """(baseline - cue) / (baseline + cue); 0/0 set to 1 ("one"), 0 ("zero") or NaN ("nan")."""
    num, den = base_rate - cue_rate, base_rate + cue_rate
    with np.errstate(invalid="ignore", divide="ignore"):
        r = num / den
    fill = {"one": 1.0, "zero": 0.0, "nan": np.nan}[zero]
    return np.where(den == 0, fill, r)


def poke_baseline(u: dict, window: float) -> np.ndarray:
    return interval_rate(u, -window, 0.0, "pokes")


def total_sr(u: dict, window: float, zero: str = "one") -> np.ndarray:
    """Suppression ratio over the whole 10 s cue, per trial."""
    return suppression(poke_baseline(u, window), interval_rate(u, 0.0, CUE_S, "pokes"), zero)


def interval_sr(u: dict, a: float, b: float, window: float, zero: str = "one") -> np.ndarray:
    """Suppression ratio of the interval (onset+a, onset+b], per trial."""
    return suppression(poke_baseline(u, window), interval_rate(u, a, b, "pokes"), zero)


def waveform_features(wave: np.ndarray, fs: float = 32 / 0.0008):
    """Half duration (ms) and amplitude ratio (n - p) / (n + p) of a mean waveform.

    Methods, K-means clustering: duration is the time from peak depolarization to the trough of
    the after-hyperpolarization, halved; p is the initial hyperpolarization and n the maximal
    depolarization. Read here as: n the largest absolute deflection of the main phase, p the
    absolute value of the extreme of opposite sign before it, and the after-hyperpolarization
    the extreme of opposite sign after it. The waveform's polarity is taken from the sign of its
    largest deflection (Plexon waveforms are usually negative-going)."""
    w = np.asarray(wave, float)
    i = int(np.argmax(np.abs(w)))
    s = np.sign(w[i]) if w[i] != 0 else 1.0
    v = w * s
    n = v[i]
    p = -v[:i].min() if i > 0 else 0.0
    p = max(p, 0.0)
    j = i + int(np.argmin(v[i:]))
    half = (j - i) / fs * 1000 / 2
    amp = (n - p) / (n + p) if (n + p) != 0 else np.nan
    return half, amp


# ---------------------------------------------------------------------------------------------
# Populations (Methods, Identifying cue-responsive vlPAG neurons; K-means clustering)

CUE_GROUPS = {"D": ["D"], "U": ["US", "UO"], "S": ["S"]}   # uncertainty collapsed in the cue
SCREEN_P = 0.017   # Methods: p < 0.017, Bonferroni for three cues
# the part of each trial every unit's spike train holds, s from onset (data check of the notebook)
STORED_S = (-20.0, 30.0)


def screen_p(u: dict, a: float, b: float, floor_baseline: bool = False) -> dict:
    """The screen's paired two-tailed t-test per cue, {cue: (t, p)}, over the cue's trials of the
    raw rate (spikes/s) in the 2 s before onset against the interval (a, b] (Methods, Identifying
    cue-responsive vlPAG neurons). floor_baseline rounds the baseline rate down, as the data set's
    cubeScript.m does (variant). A cue whose differences are all zero has no test: (nan, nan)."""
    from scipy import stats
    base = interval_rate(u, -2.0, 0.0)
    if floor_baseline:
        base = np.floor(base)
    r = interval_rate(u, a, b)
    out = {}
    for c, ts in CUE_GROUPS.items():
        m = np.isin(u["types"], ts)
        if np.all(r[m] == base[m]):
            out[c] = (np.nan, np.nan)
            continue
        t, p = stats.ttest_rel(r[m], base[m])
        out[c] = (float(t), float(p))
    return out


def screen(u: dict, a: float, b: float, floor_baseline: bool = False) -> bool:
    """True when any cue of screen_p gives p < 0.017 with the cue higher than baseline."""
    return any(p < SCREEN_P and t > 0 for t, p in screen_p(u, a, b, floor_baseline).values())


def cluster_features(units, baseline: str = "pre-cue"):
    """Baseline rate (spikes/s), half duration (ms) and amplitude ratio for every unit.

    baseline "pre-cue": mean rate in the 2 s before onset over the 32 trials (reading a of
    detail 5); "session": the mean rate over the recorded part of the session (reading b). The
    files hold spikes only from 20 s before each onset to 31 to 34 s after it (data check), so
    the session rate is taken over the 32 windows STORED_S around the onsets, the part of the
    session every unit holds."""
    if baseline == "pre-cue":
        b = np.array([interval_rate(u, -2.0, 0.0).mean() for u in units])
    else:
        b = np.array([interval_rate(u, *STORED_S).mean() for u in units])
    w = np.array([waveform_features(u["wave"]) for u in units])
    return np.c_[b, w]


def kmeans2(X: np.ndarray, scale: bool, seed: int = 0, replicates: int = 20):
    """k-means, k = 2, Lloyd's algorithm with k-means++ starts, best of `replicates` (a standard
    choice; the Methods name no initialisation). Returns True for the low-rate (LFR) cluster,
    the one whose centroid baseline rate (column 0) is lower."""
    from scipy.cluster.vq import kmeans2 as _km
    Z = (X - X.mean(0)) / X.std(0, ddof=1) if scale else X.copy()
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(replicates):
        cent, lab = _km(Z, 2, minit="++", seed=rng)
        inertia = sum(((Z[lab == k] - cent[k]) ** 2).sum() for k in range(2))
        if best is None or inertia < best[0] - 1e-9:
            best = (inertia, lab)
    lab = best[1]
    low = 0 if X[lab == 0, 0].mean() < X[lab == 1, 0].mean() else 1
    return lab == low


# ---------------------------------------------------------------------------------------------
# Statistics

def rm_anova(Y: np.ndarray, names: tuple | None = None) -> dict:
    """Repeated-measures ANOVA over any number of within factors, without sphericity correction
    (the integer degrees of freedom the paper prints). Y is subjects x factor1 x factor2 ...
    Each effect is tested against its interaction with subjects. Returns
    {effect: (F, df1, df2, p)}, effects named by `names` joined with "x" (default A, B, C)."""
    from itertools import combinations
    from scipy import stats
    Y = np.asarray(Y, float)
    k = Y.ndim - 1
    names = names or tuple("ABCDE"[:k])
    axes = tuple(range(Y.ndim))

    def term(T):
        # interaction term of the axes in T, by inclusion-exclusion of marginal means
        t = 0.0
        for r in range(len(T) + 1):
            for R in combinations(T, r):
                rest = tuple(ax for ax in axes if ax not in R)
                t = t + (-1) ** (len(T) - r) * Y.mean(axis=rest, keepdims=True)
        return np.broadcast_to(t, Y.shape)

    out = {}
    for r in range(1, k + 1):
        for S in combinations(range(1, k + 1), r):
            ss = (term(S) ** 2).sum()
            sse = (term((0,) + S) ** 2).sum()
            d1 = int(np.prod([Y.shape[ax] - 1 for ax in S]))
            d2 = d1 * (Y.shape[0] - 1)
            F = (ss / d1) / (sse / d2)
            out["x".join(names[ax - 1] for ax in S)] = (F, d1, d2, stats.f.sf(F, d1, d2))
    return out


def mixed_anova(groups: list) -> dict:
    """Split-plot ANOVA: one between factor G (the list of arrays) and two within factors A, B.
    Each array is subjects x A x B. Sums of squares with weighted means (equal to the usual
    formulas when groups are equal). Returns {effect: (F, df1, df2, p)}."""
    from scipy import stats
    Y = np.concatenate(groups)
    g = np.concatenate([np.full(len(x), i) for i, x in enumerate(groups)])
    N, a, b = Y.shape
    k = len(groups)
    m = Y.mean()
    ma, mb, mab = Y.mean((0, 2)), Y.mean((0, 1)), Y.mean(0)
    mg = np.array([x.mean() for x in groups])
    mga = np.array([x.mean((0, 2)) for x in groups])
    mgb = np.array([x.mean((0, 1)) for x in groups])
    mgab = np.array([x.mean(0) for x in groups])
    ng = np.array([len(x) for x in groups])
    ms, msa, msb = Y.mean((1, 2)), Y.mean(2), Y.mean(1)
    ssg = a * b * (ng * (mg - m) ** 2).sum()
    sssg = a * b * ((ms - mg[g]) ** 2).sum()
    ssa = N * b * ((ma - m) ** 2).sum()
    ssag = b * (ng[:, None] * (mga - mg[:, None] - ma[None] + m) ** 2).sum()
    ssasg = b * ((msa - ms[:, None] - mga[g] + mg[g][:, None]) ** 2).sum()
    ssb = N * a * ((mb - m) ** 2).sum()
    ssbg = a * (ng[:, None] * (mgb - mg[:, None] - mb[None] + m) ** 2).sum()
    ssbsg = a * ((msb - ms[:, None] - mgb[g] + mg[g][:, None]) ** 2).sum()
    ssab = N * ((mab - ma[:, None] - mb[None] + m) ** 2).sum()
    ssabg = (ng[:, None, None] * (mgab - mga[:, :, None] - mgb[:, None, :] + mg[:, None, None]
                                  - mab[None] + ma[None, :, None] + mb[None, None, :] - m) ** 2).sum()
    ssabsg = ((Y - msa[:, :, None] - msb[:, None, :] + ms[:, None, None] - mgab[g]
               + mga[g][:, :, None] + mgb[g][:, None, :] - mg[g][:, None, None]) ** 2).sum()
    dS, dA, dB = N - k, a - 1, b - 1
    rows = [("G", ssg, k - 1, sssg, dS), ("A", ssa, dA, ssasg, dA * dS),
            ("AxG", ssag, dA * (k - 1), ssasg, dA * dS), ("B", ssb, dB, ssbsg, dB * dS),
            ("BxG", ssbg, dB * (k - 1), ssbsg, dB * dS), ("AxB", ssab, dA * dB, ssabsg, dA * dB * dS),
            ("AxBxG", ssabg, dA * dB * (k - 1), ssabsg, dA * dB * dS)]
    out = {}
    for name, ss, d1, sse, d2 in rows:
        F = (ss / d1) / (sse / d2)
        out[name] = (F, d1, d2, stats.f.sf(F, d1, d2))
    return out


def sign_test(x: np.ndarray, y: np.ndarray | None = None) -> tuple[int, int, float]:
    """Two-sided sign test of x - y (or x) against zero; ties dropped. (n positive, n, p)."""
    from scipy import stats
    d = np.asarray(x, float) - (0 if y is None else np.asarray(y, float))
    d = d[~np.isnan(d) & (d != 0)]
    k = int((d > 0).sum())
    return k, len(d), stats.binomtest(k, len(d), 0.5).pvalue if len(d) else np.nan


def ols(y: np.ndarray, X: np.ndarray):
    """OLS with a constant (MATLAB regress with a column of ones). X is trials x regressors.
    Rows with a NaN are dropped. Returns (betas without the constant, their two-sided p)."""
    from scipy import stats
    X = np.asarray(X, float)
    if X.ndim == 1:
        X = X[:, None]
    ok = ~np.isnan(y) & ~np.isnan(X).any(1)
    y, X = y[ok], X[ok]
    A = np.c_[np.ones(len(y)), X]
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    dof = len(y) - A.shape[1]
    resid = y - A @ beta
    s2 = resid @ resid / dof if dof > 0 else np.nan
    cov = s2 * np.linalg.pinv(A.T @ A)
    se = np.sqrt(np.diag(cov))
    with np.errstate(invalid="ignore", divide="ignore"):
        p = 2 * stats.t.sf(np.abs(beta / se), dof)
    return beta[1:], p[1:]
