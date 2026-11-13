"""Loading and measures for CRCNS cb-1 (ten Brinke et al. 2017, eLife 6:e28132).

The data set is CRCNS cb-1, which CRCNS does not version (recorded as `unversioned`, with
the data set DOI 10.6080/K0B85697). It is one MATLAB 7.3 (HDF5) file, `eLife_dataset.mat`,
in the public S3 bucket `crcnsarchive` under `cb-1/live/`. It is streamed into memory (not
written to disk) and its MD5 is checked against the data set's `checksums.md5`.

Where each parameter comes from is said at the parameter. "Claims file" means
claims/brinke-2017.yaml (its opening comment or the claim's criterion), which cites the
paper. "Methods" means the paper's Materials and methods. "Standard choice" marks a detail
the paper does not fix and that was chosen here; "assumption" marks a choice the paper leaves
open that could change a result (each is run under its alternatives in the notebook).
"""
import hashlib
import io

import fsspec
import h5py
import numpy as np
from scipy import stats

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/cb-1/live/"
DATASET = "cb-1"
VERSION = "unversioned"
DOI = "10.6080/K0B85697"
FILE = "eLife_dataset.mat"

# The 1 ms time axis of every trace, in ms from CS onset (data.timeIndex, -0.5 to 1.5 s).
N_SET1 = 270  # cells 1-270 are the first dataset (data description, SET 1)


def checksums():
    """The data set's published MD5 sums, as {file: md5}."""
    with fsspec.open(BUCKET + "checksums.md5", "rt") as f:
        return {line.split()[1]: line.split()[0] for line in f if line.strip()}


def load():
    """Stream eLife_dataset.mat into memory and return a dict of per-cell arrays.

    Keys: t (ms, int), eyelid, sdf (lists of trials x 2001 arrays), spikes (list of lists of
    spike-time arrays in ms), fac, cramp (lists of per-trial vectors, the data set's own
    `facilitation` and `crAmplitude`), day, mouse, us (US onset, ms), dset (1 or 2), md5.
    """
    with fsspec.open(BUCKET + FILE, "rb", block_size=2**24) as f:
        raw = f.read()
    md5 = hashlib.md5(raw).hexdigest()
    h = h5py.File(io.BytesIO(raw), "r")
    d = h["data"]

    def cells(key):
        return [np.array(h[r][()]) for r in d[key][()].ravel()]

    out = {
        "t": np.round(d["timeIndex"][()].ravel() * 1000).astype(int),
        "eyelid": cells("eyelid"),
        "sdf": cells("ephys"),
        "fac": [v.ravel() for v in cells("facilitation")],
        "cramp": [v.ravel() for v in cells("crAmplitude")],
        "day": d["day"][()].ravel(),
        "mouse": d["mouseID"][()].ravel().astype(int),
        "us": np.round(d["usOnset"][()].ravel() * 1000).astype(int),
        "eyelid_mean": d["eyelidMean"][()],
        "sdf_mean": d["ephysMean"][()],
        "md5": md5,
    }
    out["spikes"] = [[row[~np.isnan(row)] * 1000 for row in st] for st in cells("spikeTimes")]
    out["dset"] = np.where(np.arange(len(out["sdf"])) < N_SET1, 1, 2)
    h.close()
    del raw
    return out


# The paper's Source data 1 (eLife, doi:10.7554/eLife.28132, Additional files), read only for the
# recording depth, which the data set lacks (claims file, opening comment). It is the file of the
# version of record (v2) on the eLife CDN, pinned by its MD5.
SOURCE_DATA1 = "https://cdn.elifesciences.org/articles/28132/elife-28132-data1-v2.mat"
SOURCE_DATA1_MD5 = "3ca8f91c5371e88c12f5eb32b3b209c6"


def load_source_data1():
    """Stream Source data 1 into memory; return ({variable name: list of 372 per-trial arrays}, md5).

    The file is a structure 'ipn' of 51 variables, each with a 'name' and a 'values' cell array of
    one vector of per-trial values per cell, cells in the data set's order (paper, Additional files,
    Source data 1)."""
    from scipy.io import loadmat
    with fsspec.open(SOURCE_DATA1, "rb") as f:
        raw = f.read()
    md5 = hashlib.md5(raw).hexdigest()
    s = loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)["ipn"]
    return {v.name: [np.atleast_1d(np.asarray(x, float)) for x in v.values] for v in s}, md5


def idx(t, a, b):
    """Boolean mask of the samples with a <= t < b (ms)."""
    return (t >= a) & (t < b)


# ----------------------------------------------------------------------------- statistics

def grubbs_keep(x, alpha=0.05):
    """Iterative two-sided Grubbs test (alpha 0.05, Methods, Statistics); mask of points kept."""
    x = np.asarray(x, float)
    keep = np.ones(len(x), bool)
    while keep.sum() > 2:
        v = x[keep]
        sd = v.std(ddof=1)
        if sd == 0:
            break
        g = np.abs(v - v.mean()) / sd
        n = len(v)
        tc = stats.t.ppf(1 - alpha / (2 * n), n - 2)
        gcrit = (n - 1) / np.sqrt(n) * np.sqrt(tc**2 / (n - 2 + tc**2))
        if g.max() > gcrit:
            keep[np.flatnonzero(keep)[np.argmax(g)]] = False
        else:
            break
    return keep


def is_normal(x):
    """Normality after Grubbs outlier removal. The paper does not name the test; Lilliefors
    (MATLAB's lillietest, alpha 0.05) is the assumption here."""
    from statsmodels.stats.diagnostic import lilliefors
    v = np.asarray(x, float)[grubbs_keep(x)]
    if len(v) < 5 or np.std(v) == 0:
        return False
    return lilliefors(v, dist="norm")[1] >= 0.05


def corr_kind(x, y):
    """Methods, Statistics: Pearson if at least 30 points and both variables normal after a
    Grubbs test, otherwise Spearman. Returns 'pearson' or 'spearman'."""
    if len(x) >= 30 and is_normal(x) and is_normal(y):
        return "pearson"
    return "spearman"


def corr(x, y, kind=None):
    """(r, p, kind) with the Statistics rule unless kind is given. Correlation on all points
    (the Grubbs test only decides the test, a standard choice: the paper does not say that
    outliers were dropped from the correlation itself)."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    kind = kind or corr_kind(x, y)
    if np.std(x) == 0 or np.std(y) == 0:
        return np.nan, np.nan, kind
    r, p = (stats.pearsonr(x, y) if kind == "pearson" else stats.spearmanr(x, y))
    return float(r), float(p), kind


def _r_to_p(r, n):
    """Two-sided p of a correlation coefficient by the t approximation (as scipy's spearmanr)."""
    r = np.clip(r, -0.9999999, 0.9999999)
    tt = r * np.sqrt((n - 2) / (1 - r**2))
    return 2 * stats.t.sf(np.abs(tt), n - 2)


def bootstrap_count(pairs, kinds, observed, sign, rng, reps=500, reading="shuffle", alpha=0.05):
    """Bootstrap test of how many cells are significant (Methods, Statistics: 500 random
    datasets with similar numbers of cells and trials). How the random datasets are made is
    open (claims file, opening comment): reading 'shuffle' permutes the trial pairing within
    each cell; reading 'random' draws independent normal values with each cell's trial count.
    `sign` is +1 or -1, the direction counted. Returns (p, null counts); p is the fraction of
    random datasets with at least the observed count."""
    counts = np.zeros(reps, int)
    prepared = []
    for (x, y), kind in zip(pairs, kinds):
        x, y = np.asarray(x, float), np.asarray(y, float)
        if reading == "random":
            kind = "pearson" if len(x) >= 30 else "spearman"
        if kind == "spearman":
            x, y = stats.rankdata(x), stats.rankdata(y)
        prepared.append((x, y, kind))
    for k in range(reps):
        c = 0
        for x, y, kind in prepared:
            n = len(x)
            if reading == "shuffle":
                xa, ya = x, rng.permutation(y)
            else:
                xa, ya = rng.standard_normal(n), rng.standard_normal(n)
                if kind == "spearman":
                    xa, ya = stats.rankdata(xa), stats.rankdata(ya)
            r = np.corrcoef(xa, ya)[0, 1]
            if np.sign(r) == sign and _r_to_p(r, n) < alpha:
                c += 1
        counts[k] = c
    return float(np.mean(counts >= observed)), counts


def mixedlm(y, x, groups, slopes=True):
    """Linear mixed model y ~ x with random intercepts (and slopes when `slopes`) per cell
    (Methods, Statistics; Supplementary file 1 says which terms each model has), by statsmodels
    MixedLM (REML), Wald test. Returns a dict: slope, se, p of the fixed effect of x; `ok`, False
    when the fit did not converge, its standard error is not finite or statsmodels warned of a
    singular random-effects covariance, a Hessian that is not positive definite or an estimate on
    the boundary of the parameter space;
    and `warnings`, the distinct warning messages of this fit, shortened."""
    import warnings
    import pandas as pd
    import statsmodels.formula.api as smf
    df = pd.DataFrame({"y": y, "x": x, "g": groups})
    model = smf.mixedlm("y ~ x", df, groups=df["g"], re_formula="~x" if slopes else "1")
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        fit = model.fit(reml=True, method=["lbfgs", "powell"])
    msgs = sorted({str(w.message).split(".")[0][:60] for w in caught
                   if not issubclass(w.category, (DeprecationWarning, FutureWarning))})
    se = float(fit.bse["x"])
    # the first optimizer failing and the second being tried is reported but is not a failure of the fit
    serious = [m for m in msgs if not m.startswith(("Maximum Likelihood optimization failed", "Retrying"))]
    ok = bool(fit.converged) and np.isfinite(se) and not serious
    return {"slope": float(fit.params["x"]), "se": se, "p": float(fit.pvalues["x"]), "ok": ok,
            "warnings": "; ".join(msgs)}


# ----------------------------------------------------------------------------- cell measures

def baseline_window(dset):
    """Baseline before the CS: 500 ms (Methods, Spike modulation) in the first dataset; the
    second dataset's trials start 200 ms before the CS (data description), so its baseline is
    the whole pre-CS period available (claims file, opening comment)."""
    return (-500, 0) if dset == 1 else (-200, 0)


def last200_windows(us, dset):
    """The last 200 ms of the CS-US interval. First dataset 50-250 ms. Second dataset: 12-212
    ms under the description's 212 ms interval, or 0-200 ms under the paper's 200 ms
    (claims file, opening comment); 0-212 ms is the window the data set's own `facilitation`
    variable uses in the second dataset (found in the data check), shown as a variant that is
    not a reading of the claims file."""
    if dset == 1:
        return {"50-250": (us - 200, us)}
    return {"12-212": (us - 200, us), "0-200": (0, 200), "0-212": (0, us)}


def modulation(m, t, base, win):
    """CS-US facilitation and suppression of an average (or single-trial) trace `m`
    (Methods, Spike modulation). Baseline mean mu over `base`; window mean over `win`.
    Reading (a): window mean minus mu, minus the mean above-baseline (or below-baseline)
    part of the baseline trace (mean over all baseline bins of max(b - mu, 0)).
    Reading (b): the same positive (negative) parts taken in both the window and the baseline.
    Reading (a+): as (a), with the above-baseline part averaged over the above-baseline bins
    only (the Methods' "mean above-baseline activity within the baseline itself" allows it).
    Reading (b), applied to single trials over the whole 0-212 ms CS-US interval, gives the data
    set's own per-trial `facilitation` exactly in the second dataset; in the first dataset that
    variable follows no window tried here exactly (data check). On the average trace, reading (b)
    gives the per-cell 'Mean Facil Hz' of the paper's Source data 1 (Source data 1 comparison).
    Reading (a+) is this attempt's own, not one the claims file names; it is shown as a variant.
    Returns dict with fac_a, sup_a, fac_ap, sup_ap, fac_b, sup_b; suppression as a positive
    depth."""
    b = m[..., idx(t, *base)]
    w = m[..., idx(t, *win)]
    mu = np.nanmean(b, -1, keepdims=True)
    pos_b = np.nanmean(np.clip(b - mu, 0, None), -1)
    neg_b = np.nanmean(np.clip(mu - b, 0, None), -1)
    d = b - mu
    pos_only = np.nanmean(np.where(d > 0, d, np.nan), -1)
    neg_only = np.nanmean(np.where(d < 0, -d, np.nan), -1)
    return {
        "fac_ap": np.nanmean(w, -1) - mu[..., 0] - pos_only,
        "sup_ap": mu[..., 0] - np.nanmean(w, -1) - neg_only,
        "fac_a": np.nanmean(w, -1) - mu[..., 0] - pos_b,
        "sup_a": mu[..., 0] - np.nanmean(w, -1) - neg_b,
        "fac_b": np.nanmean(np.clip(w - mu, 0, None), -1) - pos_b,
        "sup_b": np.nanmean(np.clip(mu - w, 0, None), -1) - neg_b,
    }


def classify(fac, sup, rule):
    """Class of a cell from facilitation and suppression (>= 5 Hz each, Methods). A cell
    meeting both thresholds is open (claims file): rule 'larger' takes the larger change,
    rule 'fac_first' takes facilitation."""
    f, s = fac >= 5, sup >= 5
    if f and s:
        if rule == "fac_first":
            return "fac"
        return "fac" if fac >= sup else "sup"
    return "fac" if f else ("sup" if s else "none")


def runs(mask):
    """List of (start, length) of runs of True."""
    out, start = [], None
    for i, v in enumerate(mask):
        if v and start is None:
            start = i
        if not v and start is not None:
            out.append((start, i - start))
            start = None
    if start is not None:
        out.append((start, len(mask) - start))
    return out


def duration_onset_peak(m, t, mu, sd, us, sign):
    """Duration: number of 1 ms bins beyond 3 baseline SDs in the last 200 ms of the CS-US
    interval, counted only when the trace exceeds the threshold for at least 10 consecutive
    ms in the CS-US interval (Methods, Spike modulation). Onset: first bin of the first such
    10 ms run in the CS-US interval; peak time: time of the extreme in the CS-US interval
    (claims file, suppression-same-timing-as-facilitation). Returns (duration, onset, peak)."""
    csus = idx(t, 0, us)
    dev = sign * (m - mu)
    beyond = dev > 3 * sd
    r = [(s, n) for s, n in runs(beyond[csus]) if n >= 10]
    tc = t[csus]
    peak = float(tc[np.nanargmax(dev[csus])])
    if not r:
        return 0.0, np.nan, peak
    dur = float(np.sum(beyond[idx(t, us - 200, us)]))
    return dur, float(tc[r[0][0]]), peak


def cs_transients(z, t, end=125, rebound_span=None):
    """CS pause and CS peak in the baseline-standardized average trace `z`, between 50 and
    `end` ms after the CS (Methods, CS-responses: 50-125 ms; Results overview: 50-130 ms).
    A drop exceeding 4.5 SDs followed by a peak of at least 2 SDs is a pause; an upstroke of
    4.5 SDs followed by a drop of at least 2 SDs is a peak. Open (claims file): whether 4.5
    SDs is from the baseline mean ('mean') or the size of the drop from the highest point
    before the trough within the window ('drop'), and whether the 2 SD rebound is from the
    trough ('trough') or from the baseline mean ('mean'). The rebound is looked for after the
    trough within the same window (standard choice); with `rebound_span` it is looked for up to
    that many ms after the trough, past the window's end (variant). Returns {reading: (pause,
    latency, peak, latency)} for the four readings."""
    w = idx(t, 50, end + 1)
    zw, tw = z[w], t[w]
    out = {}
    for depth in ("mean", "drop"):
        for reb in ("trough", "mean"):
            res = []
            for sgn in (1, -1):  # 1: pause (trough), -1: peak (upstroke)
                v = -sgn * zw  # transient direction positive
                k = int(np.argmax(v))
                ext = v[k]
                if depth == "mean":
                    big = ext > 4.5
                else:
                    big = (ext - np.min(v[: k + 1])) > 4.5
                after = v[k + 1:]
                if rebound_span is not None:
                    k0 = int(np.flatnonzero(t == tw[k])[0])
                    after = -sgn * z[k0 + 1:k0 + 1 + rebound_span]
                if len(after) == 0:
                    ok = False
                elif reb == "trough":
                    ok = (ext - np.min(after)) >= 2
                else:
                    ok = np.min(after) <= -2
                res += [bool(big and ok), float(tw[k])]
            out[f"{depth}/{reb}"] = tuple(res)
    return out


def us_responses(z, m, t, us, mu, turn_span=30):
    """US responses of the standardized average trace `z` (Methods, US-responses). Windows
    1-30 ms (first peak), 16-45 ms (pause) and 31-60 ms (second peak) after the US, inclusive.
    L is the mean z of the last 50 ms of the CS-US interval. First peak: max - L > 5, or
    max - L > 2 and max > 5. Pause: (L - min > 5 and min < -2) or (L - min > 2 and min < -5).
    Second peak: max - L >= 2 and max >= 5. For the pause and second peak the trace must turn
    back at least 2 SDs within `turn_span` ms after the extreme (the span is a standard
    choice). Amplitudes in Hz from the baseline mean (`*_base`) and from the last 50 ms
    (`*_l50`); times in ms after the US."""
    L = np.nanmean(z[idx(t, us - 50, us)])
    l50 = np.nanmean(m[idx(t, us - 50, us)])
    res = {"L": L}

    def win(a, b):
        return idx(t, us + a, us + b + 1)

    w = win(1, 30)
    k = np.flatnonzero(w)[np.nanargmax(z[w])]
    P = z[k]
    res["peak1"] = bool((P - L > 5) or (P - L > 2 and P > 5))
    res["peak1_t"], res["peak1_base"], res["peak1_l50"] = float(t[k] - us), m[k] - mu, m[k] - l50
    res["peak1_max_base"] = np.nanmax(m[w]) - mu

    w = win(16, 45)
    k = np.flatnonzero(w)[np.nanargmin(z[w])]
    Q = z[k]
    turn = np.nanmax(z[k + 1:k + 1 + turn_span]) - Q >= 2
    res["pause"] = bool(((L - Q > 5 and Q < -2) or (L - Q > 2 and Q < -5)) and turn)
    res["pause_t"], res["pause_base"], res["pause_l50"] = float(t[k] - us), m[k] - mu, m[k] - l50

    w = win(31, 60)
    k = np.flatnonzero(w)[np.nanargmax(z[w])]
    R = z[k]
    turn = R - np.nanmin(z[k + 1:k + 1 + turn_span]) >= 2
    res["peak2_any"] = bool(R - L >= 2 and R >= 5 and turn)
    res["peak2_t"], res["peak2_base"], res["peak2_l50"] = float(t[k] - us), m[k] - mu, m[k] - l50
    res["peak2_max_base"], res["peak2_max_l50"] = np.nanmax(m[w]) - mu, np.nanmax(m[w]) - l50
    res["peak2_vel"] = np.nanmax(np.diff(m[idx(t, us + 30, us + 61)]))
    return res


def trial_extreme(sdf, t, centre, kind="max"):
    """Per-trial maximum (minimum for pauses) absolute rate in a 30 ms window centred on the
    cell's average peak (pause) time `centre` in ms (Methods, US-responses)."""
    w = idx(t, centre - 15, centre + 15)
    return np.nanmax(sdf[:, w], 1) if kind == "max" else np.nanmin(sdf[:, w], 1)


def eyelid_trials(e, t, us):
    """Per-trial eyelid measures. Baseline: the mean of all pre-CS samples, which is the 500 ms
    before the CS in the first dataset and the 200 ms recorded in the second (both readings of
    the claims file coincide). CR: closure above 5% of the full blink range over the baseline
    mean anywhere in the CS-US interval (Methods, Eyeblink conditioning). Amplitude at US onset
    (the Results' CR amplitude) and the maximum in the CS-US interval (the Methods'), in %."""
    bl = np.nanmean(e[:, idx(t, -500, 0)], 1)
    csus = e[:, idx(t, 0, us)] - bl[:, None]
    at_us = (e[:, t == us][:, 0] - bl) * 100
    mx = np.nanmax(csus, 1) * 100
    ext = np.take_along_axis(csus, np.nanargmax(np.abs(csus), 1)[:, None], 1)[:, 0] * 100
    return {"bl": bl, "cr": mx > 5, "amp_us": at_us, "amp_max": mx, "amp_ext": ext}


def cr_latency(e, t, us, cr):
    """CR latency (Figure 4G legend: when the CR passes 5% eyelid closure). Reading a: on the
    cell's average eyelid trace; reading b: mean of the trial values over CR trials; reading
    c: the Methods' CR onset, the start of the continuous positive eyelid velocity leading up
    to the 5% crossing, on the average trace. NaN when there is no crossing."""
    bl = np.nanmean(e[:, idx(t, -500, 0)], 1, keepdims=True)
    x = e - bl
    w = idx(t, 0, us + 1)
    tw = t[w]

    def cross(tr):
        k = np.flatnonzero(tr[w] > 0.05)
        return float(tw[k[0]]) if len(k) else np.nan

    avg = np.nanmean(x, 0)
    a = cross(avg)
    vals = [cross(tr) for tr in x[cr]]
    b = float(np.nanmean(vals)) if len(vals) and not np.all(np.isnan(vals)) else np.nan
    c = np.nan
    if not np.isnan(a):
        k = int(np.flatnonzero(t == a)[0])
        v = np.diff(avg)
        j = k
        while j > np.flatnonzero(w)[0] and v[j - 1] > 0:
            j -= 1
        c = float(t[j])
    return a, b, c


def isi_cv(spikes, a, b):
    """Coefficient of variation of interspike intervals within [a, b) ms, pooled over trials."""
    isis = np.concatenate([np.diff(s[(s >= a) & (s < b)]) for s in spikes] + [np.array([])])
    return float(np.std(isis) / np.mean(isis)) if len(isis) > 2 else np.nan


def xcorr_lag(spk, eye, t, seg, maxlag=100, sign=1, estimator="xcov"):
    """Lag (ms) of the maximum (sign +1) or minimum (sign -1) cross-correlation between the average
    spike trace and the average eyelid trace over the segment `seg`; positive lags mean spikes lead
    the eyelid. Segment and lag range are open (claims file, fig2d-facilitation-leads-eyelid-ds1).
    The estimator is not given in the paper ("temporal cross-correlations between average spike and
    eyelid traces", Results); it is an assumption, run two ways:
    'xcov' (adopted): both traces cut to the segment and mean-subtracted, sum of s(t) e(t + lag) over
    the overlapping samples divided by the product of the two norms, as MATLAB's
    xcov(s, e, maxlag, 'coeff'), the field's standard cross-correlation of two traces;
    'recut': Pearson r of the spike segment with the eyelid trace re-cut at segment + lag. Its r is
    normalized afresh at each lag, so on ramp-shaped traces it is nearly flat across lags and its
    maximum often falls at the edge of the lag range (verifier, round 1).
    Returns (lag, r by lag from -maxlag to +maxlag)."""
    lags = np.arange(-maxlag, maxlag + 1)
    s = spk[idx(t, *seg)]
    r = np.full(len(lags), np.nan)
    if estimator == "xcov":
        e = eye[idx(t, *seg)]
        s, e = s - s.mean(), e - e.mean()
        n, norm = len(s), np.sqrt(np.dot(s, s) * np.dot(e, e))
        for i, L in enumerate(lags):
            r[i] = (np.dot(s[:n - L], e[L:]) if L >= 0 else np.dot(s[-L:], e[:n + L])) / norm
    else:
        for i, L in enumerate(lags):
            e = eye[idx(t, seg[0] + L, seg[1] + L)]
            if len(e) == len(s) and not np.isnan(e).any() and np.std(e) > 0 and np.std(s) > 0:
                r[i] = np.corrcoef(s, e)[0, 1]
    k = np.nanargmax(sign * r)
    return int(lags[k]), r


def corr_matrix(sdf, eyelid, t, start, stop, width=20, step=20, velocity=False):
    """Trial-by-trial spike-eyelid correlation matrix (Methods, Statistics; ten Brinke et al.
    2015): mean rate and mean eyelid position (or velocity, the mean of the 1 ms derivative)
    in windows of `width` ms at `step` ms, correlated across trials (Pearson, standard
    choice). Returns (centres, R) with R[i, j] = r(spikes in window i, eyelid in window j)."""
    starts = np.arange(start, stop - width + 1, step)
    ey = np.diff(eyelid, axis=1, prepend=np.nan) if velocity else eyelid
    S = np.stack([np.nanmean(sdf[:, idx(t, a, a + width)], 1) for a in starts], 1)
    E = np.stack([np.nanmean(ey[:, idx(t, a, a + width)], 1) for a in starts], 1)
    Sz = (S - S.mean(0)) / S.std(0)
    Ez = (E - E.mean(0)) / E.std(0)
    R = Sz.T @ Ez / S.shape[0]
    return starts + width / 2, R


def optimal_offset(mats, centres, us, sign, maxoff=100):
    """Average the cells' matrices after setting r of the sign opposite to `sign` to zero
    (Methods, Statistics), then for each diagonal offset (eyelid time minus spike time)
    average the r values whose eyelid window lies in the last 200 ms of the CS-US interval
    (Figure 2-figure supplement 1 legend). Returns (best offset, offsets, mean r by offset)."""
    M = np.nanmean([np.where(sign * R > 0, R, 0) for R in mats], 0)
    step = centres[1] - centres[0]
    offs = np.arange(-maxoff, maxoff + 1, step)
    vals = []
    for d in offs:
        v = []
        for j, ce in enumerate(centres):
            if us - 200 <= ce - 10 and ce + 10 <= us + 1e-9:
                i = np.flatnonzero(np.isclose(centres, ce - d))
                if len(i):
                    v.append(M[i[0], j])
        vals.append(np.mean(v) if v else np.nan)
    vals = np.array(vals)
    return float(offs[np.nanargmax(sign * vals)]), offs, vals


# CS transient windows: end of the window (Methods 125 ms, Results overview 130 ms) and where the
# rebound is looked for (None: within the window, a standard choice; 50: up to 50 ms after the
# trough). Both are open in the paper and both could change counts, so all four are run.
CS_WINDOWS = {"125": (125, None), "130": (130, None), "125+50": (125, 50), "130+50": (130, 50)}


def cell_table(D):
    """One row per recording with every per-cell measure the claims use (see the functions
    above for where each comes from). Class columns are named cls_<baseline reading>_<tie
    rule>_<window>."""
    import pandas as pd
    t = D["t"]
    rows = []
    for i in range(len(D["sdf"])):
        ds, us = int(D["dset"][i]), int(D["us"][i])
        sdf, eye = D["sdf"][i], D["eyelid"][i]
        base = baseline_window(ds)
        m = np.nanmean(sdf, 0)
        b = m[idx(t, *base)]
        mu, sd = float(np.mean(b)), float(np.std(b, ddof=1))
        z = (m - mu) / sd
        r = {"cell": i + 1, "dset": ds, "day": float(D["day"][i]), "mouse": int(D["mouse"][i]),
             "us": us, "n_trials": sdf.shape[0], "mu": mu, "sd": sd}
        # firing frequency: (a) baseline mean of the average trace, (b) spikes over the whole trial
        lo, hi = (-500, 1500) if ds == 1 else (-200, 800)
        r["rate_base"] = mu
        r["rate_trial"] = float(np.mean([len(s) for s in D["spikes"][i]]) / ((hi - lo) / 1000))
        for wname, win in last200_windows(us, ds).items():
            mod = modulation(m, t, base, win)
            for k, v in mod.items():
                r[f"{k}_{wname}"] = float(v)
            for rd in ("a", "ap", "b"):
                for rule in ("larger", "fac_first"):
                    r[f"cls_{rd}_{rule}_{wname}"] = classify(mod[f"fac_{rd}"], mod[f"sup_{rd}"], rule)
        for sgn, nm in ((1, "fac"), (-1, "sup")):
            dur, on, pk = duration_onset_peak(m, t, mu, sd, us, sgn)
            r[f"dur_{nm}"], r[f"onset_{nm}"], r[f"peaktime_{nm}"] = dur, on, pk
        w200 = idx(t, us - 200, us)
        r["zpeak_fac"] = float(np.nanmax(z[w200]))
        r["zpeak_sup"] = float(-np.nanmin(z[w200]))
        r["zmean_fac"] = float(np.nanmean(z[w200]))
        r["zmean_sup"] = float(-np.nanmean(z[w200]))
        csus = idx(t, 0, us)
        r["max_csus"] = float(np.nanmax(m[csus]) - mu)
        r["min_csus"] = float(np.nanmin(m[csus]) - mu)
        dm = np.diff(m)
        r["vel_max"] = float(np.nanmax(dm[csus[1:]]))
        r["vel_min"] = float(np.nanmin(dm[csus[1:]]))
        r["cv_base"] = isi_cv(D["spikes"][i], base[0], base[1])
        r["cv_trial"] = isi_cv(D["spikes"][i], lo, hi)
        for key, (end, span) in CS_WINDOWS.items():
            for rd, (pa, pat, pk, pkt) in cs_transients(z, t, end, span).items():
                r[f"cspause_{rd}_{key}"], r[f"cspause_t_{rd}_{key}"] = pa, pat
                r[f"cspeak_{rd}_{key}"], r[f"cspeak_t_{rd}_{key}"] = pk, pkt
        r.update(us_responses(z, m, t, us, mu))
        ey = eyelid_trials(eye, t, us)
        r["cr_pct"] = float(ey["cr"].mean() * 100)
        r["amp_us"] = float(np.mean(ey["amp_us"]))
        r["amp_max"] = float(np.mean(ey["amp_max"]))
        r["amp_us_data"] = float(np.mean(D["cramp"][i]))
        r["crlat_a"], r["crlat_b"], r["crlat_c"] = cr_latency(eye, t, us, ey["cr"])
        rows.append(r)
    df = pd.DataFrame(rows)
    df["behav"] = df["cr_pct"] >= 20
    return df


def trial_rates(D, i, win_name=None):
    """Per-trial firing-rate measures in the last 200 ms of the CS-US interval (claims file,
    opening comment, trial-by-trial facilitation): (a) window mean minus the trial's own
    baseline mean, (b) minus the cell's mean baseline, (c) the data set's `facilitation`."""
    t, ds, us = D["t"], int(D["dset"][i]), int(D["us"][i])
    sdf = D["sdf"][i]
    base = baseline_window(ds)
    win = list(last200_windows(us, ds).values())[0] if win_name is None else last200_windows(us, ds)[win_name]
    w = np.nanmean(sdf[:, idx(t, *win)], 1)
    bt = np.nanmean(sdf[:, idx(t, *base)], 1)
    return {"a": w - bt, "b": w - bt.mean(), "c": D["fac"][i]}


def trial_corrs(pairs, kind=None):
    """Per-cell trial-by-trial correlations of (x, y) pairs, by the Statistics rule unless
    `kind` is given. Returns arrays r, p and the list of kinds."""
    out = [corr(x, y, kind) for x, y in pairs]
    return np.array([o[0] for o in out]), np.array([o[1] for o in out]), [o[2] for o in out]


def mwu(a, b):
    """Two-sided Mann-Whitney U test (Methods, Statistics), p-value."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    if len(a) == 0 or len(b) == 0:
        return np.nan
    return float(stats.mannwhitneyu(a, b, alternative="two-sided").pvalue)
