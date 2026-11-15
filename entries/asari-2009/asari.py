"""Loading and measures for CRCNS ac-1 (Asari & Zador 2009, J Neurophysiol 102:2638).

The data set holds the authors' MATLAB analysis code (asari/Tools in crcns-ac1.zip):
CxtDep.m (context-dependence analysis), GetEvoked.m (splitting a trace into stimulus and
silent periods, median filter), ViewResp.m and GetSpikes.m (spike extraction). The paper
does not link it; it is the authors' own code shipped with their data, and is followed here
where the Methods leave a detail open (protocol, reader step 2: the Methods come first, then
the paper's analysis code). Where a parameter comes from is said beside it:

- "Methods" with a section name: the paper's Methods (the claims file's criterion cites the
  same passages).
- "CxtDep.m", "GetEvoked.m", "GetSpikes.m": the authors' code in the data set.
- "standard choice": a detail that cannot change a result (a binning for storage or fits).
- "assumption": a choice neither the paper nor the code fixes; the notebook shows the other
  readings.

Files are streamed from the public bucket crcnsarchive over HTTP range requests; nothing is
written to disk.
"""
import io
import multiprocessing as mp
import re
import zipfile
import zlib
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import fsspec
import numpy as np
import scipy.io as sio
from scipy import ndimage, signal, stats
from scipy.optimize import least_squares

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/"
ZIPS = ["crcns-ac1.zip", "crcns-ac1-asari-results-1.zip", "crcns-ac1-asari-results-2.zip"]
SF = 10000  # Hz; checked against response.sf of every file in the notebook

_zips = {}
_members = None


def open_zip(name):
    if name not in _zips:
        _zips[name] = zipfile.ZipFile(fsspec.open(BUCKET + name, block_size=2**22).open())
    return _zips[name]


def members():
    """Map 'Results/<rec>/<file>.mat' (the paths in Summary.mat) to (zip, member)."""
    global _members
    if _members is None:
        _members = {}
        for z in ZIPS[1:]:
            for info in open_zip(z).infolist():
                if info.filename.endswith(".mat"):
                    _members["Results/" + info.filename.split("/", 1)[1]] = (z, info.filename, info.file_size)
    return _members


def cell_id(path):
    """Recording folder, date-animal-penetration (one cell per folder in Summary.mat)."""
    return path.split("/")[1]


def animal_id(path):
    return "-".join(cell_id(path).split("-")[:2])


def seed_of(path):
    """A fixed seed per file, so that each file's shuffles do not depend on the others."""
    return zlib.crc32(path.encode())


def run_parallel(func, items, workers=4):
    """Map func over items in worker processes started fresh ('spawn': forked workers would
    share the parent's open HTTP connections)."""
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return list(ex.map(func, items))


def run_threads(func, items, workers=6):
    members()
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(func, items))


def survey_file(path):
    """Metadata of one result file: recording type, units, sampling rate, length, triggers."""
    z, mem, size = members()[path]
    m = loadmat_bytes(read_member(z, mem))
    r, p = m["response"], m["param"]
    rec = getattr(p, "recording", None)
    trig = np.atleast_1d(m["triggers"])
    types = {}
    for t in trig:
        types[str(t.type)] = types.get(str(t.type), 0) + 1
    return dict(path=path, size=size, rectype=str(getattr(rec, "type", "")), unit=str(r.unit),
                sf=int(r.sf), n=int(np.size(r.trace)), datatype=str(r.datatype),
                trigger_types=types, description=" ".join(_str(getattr(p.ID, "description", "")).split()),
                age=str(getattr(getattr(p, "animal", None), "age", "")),
                site=str(getattr(rec, "site", "")))


def loadmat_bytes(b):
    return sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)


def read_member(zipname, member):
    return open_zip(zipname).read(member)


def summary():
    """Rows (experiment index, description, cell index, file path, file description) of asari/Summary.mat."""
    m = loadmat_bytes(read_member("crcns-ac1.zip", "asari/Summary.mat"))
    rows = []
    for ei, e in enumerate(np.atleast_1d(m["experiment"])):
        for ci, c in enumerate(np.atleast_1d(e.cell)):
            files = np.atleast_1d(c.file)
            descs = np.atleast_1d(c.description)
            for f, d in zip(files, descs):
                d = " ".join(np.atleast_1d(d).astype(str)) if not isinstance(d, str) else d
                rows.append(dict(experiment=ei, exp_description=str(e.description), cell=ci,
                                 file=str(f), description=" ".join(d.split())))
    return rows


def _str(x):
    if isinstance(x, str):
        return x
    return "\n".join(np.atleast_1d(x).astype(str))


class Recording:
    """One data file: the trace in mV, the stimulus triggers and the stimulus table."""

    def __init__(self, path, raw=None):
        z, mem, _ = members()[path]
        m = loadmat_bytes(read_member(z, mem) if raw is None else raw)
        r, p = m["response"], m["param"]
        self.path = path
        self.sf = int(r.sf)
        self.unit = str(r.unit)
        self.scale = float(r.scale)
        trace = np.asarray(r.trace, dtype=np.float64) * self.scale
        rec = getattr(p, "recording", None)
        self.rectype = str(getattr(rec, "type", ""))
        off = str(getattr(rec, "offset", "")).strip()
        # GetEvoked.m subtracts param.recording.offset from the trace
        self.offset = float(off) if off not in ("", "[]") else 0.0
        self.trace = trace - self.offset
        self.description = " ".join(_str(getattr(p.ID, "description", "")).split())
        self.notes = _str(getattr(p, "notes", ""))
        self.triggers = []
        for t in np.atleast_1d(m["triggers"]):
            self.triggers.append(dict(type=str(t.type), time=int(t.time),
                                      description=str(getattr(t.param, "description", "")),
                                      duration=float(getattr(t.param, "duration", np.nan))))
        self.stimuli = []
        if hasattr(p, "stimulus"):
            for s in np.atleast_1d(p.stimulus):
                self.stimuli.append(dict(name=str(getattr(s, "name", "")),
                                         description=" ".join(_str(getattr(s, "description", "")).split()),
                                         file=str(getattr(s, "file", "")),
                                         duration=float(s.param.duration),
                                         param=s.param))
        # stimulus table and effective repeats, parsed from param.notes as CxtDep.m does
        self.table, self.rep = [], None
        for line in self.notes.split("\n"):
            if "Effective repeats:" in line:
                self.rep = int(line.split("Effective repeats:")[1].split()[0])
            if line.strip().startswith("Seq."):
                self.table.append([int(v) for v in line.split(":", 1)[1].split()])


def median_clip(trace, smooth_ms=10, sf=SF):
    """GetEvoked.m: subtract the mean, median filter (window smooth_ms; Methods, Analysis:
    10-ms window to clip spikes), add the mean back. MATLAB medfilt1 with an even window n
    takes x(k-n/2 : k+n/2-1), as ndimage with its default origin; zero padding at the ends."""
    mu = trace.mean()
    y = ndimage.median_filter((trace - mu).astype(np.float32), size=int(round(smooth_ms / 1000 * sf)),
                              mode="constant", cval=0.0)
    return y + mu


def split_periods(rec):
    """GetEvoked.m: stimulus periods start at each non-pulse trigger and last its duration;
    silent periods lie between them. Returns lists of (start, stop) sample indices."""
    trig = [t for t in rec.triggers if "pulse" not in t["type"]]
    n = len(rec.trace)
    evoked, spont = [], []
    t1 = 0
    for t in trig:
        t0 = t1
        t1 = t["time"] - 1
        spont.append((t0, t1))
        stop = min(t1 + int(round(t["duration"] * rec.sf / 1000)), n)
        evoked.append((t1, stop))
        t1 = stop
    if t1 < n:
        spont.append((t1, n))
    return trig, evoked, spont


# ---------------------------------------------------------------------------------------
# Spikes

# GetSpikes.m, ExtractSpikes: equiripple high-pass FIR applied with filtfilt
HP_NUM = np.array([-2.9419, -7.7633, -16.2976, -28.7498, -44.7001, -62.8034, -80.9099, -96.4457,
                   -106.9520, 889.3317, -106.9520, -96.4457, -80.9099, -62.8034, -44.7001,
                   -28.7498, -16.2976, -7.7633, -2.9419]) / 1000


def extract_spikes(trace, threshold=None, remove_downward=True):
    """GetSpikes.m, ExtractSpikes: high-pass filter, threshold, one spike at the peak of each
    suprathreshold segment (Methods, Analysis: 'high-pass filter and thresholding ... peaks of
    suprathreshold segments'). threshold None is the code's automatic rule (2/3 of the largest
    absolute filtered value). remove_downward drops peaks with a deeper trough within +-10
    samples, as the code does in automatic mode. Returns sample indices and the threshold."""
    f = signal.filtfilt(HP_NUM, [1.0], trace)
    if threshold is None:
        a = np.abs(f)
        i = int(np.argmax(a))
        threshold = 2 / 3 * a[i]
        if threshold > 100:
            mask = np.ones(len(f), bool)
            mask[max(0, i - 30):i + 31] = False
            threshold = 2 / 3 * a[mask].max()
    above = f > threshold
    if not above.any():
        return np.array([], int), threshold
    d = np.diff(above.astype(np.int8))
    starts = list(np.where(d == 1)[0] + 1)
    stops = list(np.where(d == -1)[0] + 1)
    if above[0]:
        starts = [0] + starts
    if above[-1]:
        stops = stops + [len(f)]
    peaks = np.array([s + int(np.argmax(f[s:e])) for s, e in zip(starts, stops)])
    if remove_downward and len(peaks):
        keep = []
        for p in peaks:
            lo, hi = max(0, p - 10), min(len(f), p + 11)
            keep.append(f[lo:hi].min() >= -f[p])
        peaks = peaks[np.array(keep)]
    return peaks, threshold


# ---------------------------------------------------------------------------------------
# Context-probe sequences (CxtDep.m)

SILENCE = 0  # index used here for the "silence" context (intersequence interval)


def probe_sets(rec, x, spikes=None, rep_min=None, blank_probe=False, blank_probe_s=2.5,
               blank_context_s=4.0):
    """Collect the responses to each probe in each context, as CxtDep.m does.

    x is the (filtered) trace. Sequences follow rec.table; the first rec.rep presentations of
    each sequence are used (CxtDep.m: resp(:,1:rep)). A probe is a fragment; its context is the
    fragment before it in the sequence, or silence (index 0) when it opens the sequence. With
    blank_probe, the first blank_probe_s seconds after each sequence (2.5 s, CxtDep.m default,
    shortened to the shortest silence) form an extra probe, index -1, whose contexts are the
    last fragments. Trials of a context are pooled over its occurrences and cut to the smallest
    count over contexts (CxtDep.m, GetResp). Returns a list of dicts: probe, contexts (sorted),
    trials (n_contexts, m, T) array, spikes (n_contexts lists of m arrays of probe-relative
    times in s), seconds of context available per trial set (ctx_len)."""
    trig, evoked, spont = split_periods(rec)
    rep = rec.rep
    M = len(rec.table)
    dur = {i + 1: int(round(s["duration"] / 1000 * rec.sf)) for i, s in enumerate(rec.stimuli)}
    # presentations of each sequence, in order of the triggers
    # a trigger belongs to the table row whose fragment list its description carries (the
    # numbers in "Sequence k:" do not always match the table rows, as in 20051107-ha1-001)
    seq_of = []
    for t in trig:
        frags = [int(v) for v in t["description"].split(":", 1)[-1].split()] if ":" in t["description"] else []
        seq_of.append(rec.table.index(frags) + 1 if frags in rec.table else None)
    pres = {s: [k for k, q in enumerate(seq_of) if q == s] for s in range(1, M + 1)}
    if any(len(pres[s]) < rep for s in pres):
        rep = min(len(pres[s]) for s in pres)
    blank_len = None
    if blank_probe:
        lens = []
        for s in pres:
            for k in pres[s][:rep]:
                lens.append(spont[k + 1][1] - spont[k + 1][0] if k + 1 < len(spont) else 0)
        blank_len = int(min(blank_probe_s * rec.sf, min(lens)))
    occ = {}  # probe -> context -> list of (start sample of probe, length)
    for s in range(1, M + 1):
        seq = rec.table[s - 1]
        for k in pres[s][:rep]:
            t0 = evoked[k][0]
            pos = t0
            prev = SILENCE
            for frag in seq:
                occ.setdefault(frag, {}).setdefault(prev, []).append((pos, dur[frag]))
                pos += dur[frag]
                prev = frag
            if blank_probe:
                occ.setdefault(-1, {}).setdefault(prev, []).append((pos, blank_len))
    out = []
    for probe in sorted(occ):
        ctx = occ[probe]
        if len(ctx) < 2:  # CxtDep.m: each probe should have at least 2 contexts
            continue
        T = min(L for c in ctx for (_, L) in ctx[c])
        m = min(len(v) for v in ctx.values())
        if rep_min is not None and m < rep_min:
            pass  # counted by the caller; returned with its trial count
        contexts = sorted(ctx)
        tr = np.empty((len(contexts), m, T), np.float32)
        spk = []
        for i, c in enumerate(contexts):
            row = []
            for j, (st, _) in enumerate(ctx[c][:m]):
                tr[i, j] = x[st:st + T]
                if spikes is not None:
                    sel = spikes[(spikes >= st) & (spikes < st + T)]
                    row.append((sel - st) / rec.sf)
            spk.append(row)
        out.append(dict(probe=probe, contexts=contexts, trials=tr, spikes=spk, m=m, T=T,
                        n_occ={c: len(ctx[c]) for c in contexts}))
    return out


def drop_context(ps, context=SILENCE):
    """The same probe set without one context (for the reading that silence is not a
    conditioning stimulus); None when fewer than two contexts remain."""
    keep = [i for i, c in enumerate(ps["contexts"]) if c != context]
    if len(keep) < 2:
        return None
    q = dict(ps)
    q["contexts"] = [ps["contexts"][i] for i in keep]
    q["trials"] = ps["trials"][keep]
    q["spikes"] = [ps["spikes"][i] for i in keep] if ps["spikes"] else ps["spikes"]
    return q


# ---------------------------------------------------------------------------------------
# Significance measure (Methods, Significance measure; CxtDep.m, KWtest)

ALPHA = 0.01        # Methods: P < 0.01
RUN = 50            # Methods: for >= 5 ms, i.e. >= 50 consecutive time points at 10 kHz


def runs_at_least(b, L=RUN):
    """Mark the points of b (..., T) that lie in runs of True of length >= L."""
    b = b.astype(np.int32)
    c = np.cumsum(b, axis=-1)
    c = np.concatenate([np.zeros(b.shape[:-1] + (1,), np.int32), c], axis=-1)
    w = (c[..., L:] - c[..., :-L]) == L  # window of L starting at s is all True
    # point t is covered if some window start s in [t-L+1, t] qualifies
    wc = np.cumsum(w.astype(np.int32), axis=-1)
    wc = np.concatenate([np.zeros(w.shape[:-1] + (1,), np.int32), wc], axis=-1)
    T = b.shape[-1]
    t = np.arange(T)
    hi = np.minimum(t, w.shape[-1] - 1) + 1
    lo = np.clip(t - L + 1, 0, w.shape[-1])
    cov = (wc[..., hi] - wc[..., lo]) > 0
    cov &= (t <= T - 1)
    return cov


def kw_significance(trials, n_shuffle=1000, rng=None, chunk=50):
    """Kruskal-Wallis test across contexts at each time point (Methods, Eq. 10), on ranks of
    the trials at each time point; significant where P < 0.01 for >= 50 consecutive points.
    Ties take average ranks (the standard test; CxtDep.m breaks ties by order, which on
    int16-quantised data would favour the first contexts). Noise floor: the trials are shuffled
    across contexts n_shuffle times (Methods: 1,000 per probe) and the fraction of shuffles
    significant at each point is returned. Returns (p, signif, noise)."""
    n, m, T = trials.shape
    N = n * m
    R = stats.rankdata(trials.reshape(N, T), axis=0).astype(np.float32)
    crit = stats.chi2.ppf(1 - ALPHA, n - 1)

    def kw(rbar):
        return 12 * ((rbar - (N + 1) / 2) ** 2).sum(axis=-2) / (n * (N + 1))

    rbar = R.reshape(n, m, T).mean(axis=1)
    H = kw(rbar)
    p = stats.chi2.sf(H, n - 1)
    signif = runs_at_least(H > crit)
    noise = np.zeros(T, np.float64)
    if n_shuffle:
        rng = np.random.default_rng(rng)
        G0 = np.kron(np.eye(n, dtype=np.float32), np.ones((1, m), np.float32)) / m  # (n, N)
        done = 0
        while done < n_shuffle:
            k = min(chunk, n_shuffle - done)
            G = np.concatenate([G0[:, rng.permutation(N)] for _ in range(k)], axis=0)  # (k n, N)
            rb = (G @ R).reshape(k, n, T)
            Hs = kw(rb)
            noise += runs_at_least(Hs > crit).sum(axis=0)
            done += k
        noise /= n_shuffle
    return p, signif, noise


# ---------------------------------------------------------------------------------------
# Fractional power measure (Methods, Eqs. 11 to 19; CxtDep.m, FracPow)

def frac_power(trials, center=True):
    """Per-probe terms of Eqs. 17 and 18 at each time point. Each trial is centred over the
    probe period (CxtDep.m, FracPow; Methods: responses centred to zero mean). Returns
    (total, predictable, invariant): predictable is Eq. 17 before the population average,
    invariant Eq. 18; context-dependent is predictable - invariant (Eq. 19)."""
    n, m, T = trials.shape
    r = trials.astype(np.float64)
    if center:
        r = r - r.mean(axis=2, keepdims=True)
    tot = r ** 2
    mu = r.mean(axis=1)  # (n, T) context means
    pred = ((m * mu ** 2 - tot.mean(axis=1)) / (m - 1)).mean(axis=0)
    inv = (n * mu.mean(axis=0) ** 2 - (mu ** 2).mean(axis=0)) / (n - 1)
    return tot.mean(axis=(0, 1)), pred, inv


def running_mean_0_2t(y, dt):
    """Methods (Eqs. 20 and 43): the denominator is smoothed by the running average over
    [0, 2t] at time t; at t = 0 the value itself. y sampled every dt from t = 0."""
    c = np.concatenate([[0.0], np.cumsum(y)])
    i = np.arange(len(y))
    hi = np.minimum(2 * i, len(y) - 1)
    return (c[hi + 1] - c[0]) / (hi + 1)


def bin_mean(y, k):
    """Mean over blocks of k samples (storage and fitting at 1 ms; standard choice)."""
    L = (len(y) // k) * k
    return y[:L].reshape(-1, k).mean(axis=1)


# ---------------------------------------------------------------------------------------
# Exponential fits (Methods, Exponential curve fit, Eq. 44)

def fit_exp(t, y, n_exp, kappa=None, starts=None, nonneg=False):
    """Least squares fit of sum_k a_k exp(-t/tau_k) + kappa (Eq. 44; the paper used MATLAB
    lsqcurvefit, a least-squares solver). kappa fixed when given, free when None. Start values
    and bounds are not given in the paper: a grid of start values is used and the best fit
    kept (standard choice), with tau in [1 ms, 100 s]. nonneg bounds the sizes at zero or
    above (a reading: the paper calls them decay sizes and reports positive values). Returns
    dict(a, tau, kappa, cost)."""
    free_k = kappa is None
    if starts is None:
        taus = [0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
        if n_exp == 1:
            starts = [[t1] for t1 in taus]
        else:
            starts = [[t1, t2] for t1 in taus for t2 in taus if t2 > t1]
    amp0 = (y[: max(1, len(y) // 50)].mean() - (y[-len(y) // 5:].mean() if free_k else kappa))
    best = None
    for s in starts:
        x0 = []
        for tau in s:
            x0 += [abs(amp0) / n_exp if nonneg else amp0 / n_exp, tau]
        if free_k:
            x0 += [y[-len(y) // 5:].mean()]
        lb = []
        ub = []
        for _ in s:
            lb += [0.0 if nonneg else -np.inf, 1e-3]
            ub += [np.inf, 100.0]
        if free_k:
            lb += [-np.inf]
            ub += [np.inf]

        def res(v):
            f = np.zeros_like(t)
            for k in range(n_exp):
                f = f + v[2 * k] * np.exp(-t / v[2 * k + 1])
            return f + (v[-1] if free_k else kappa) - y

        try:
            r = least_squares(res, x0, bounds=(lb, ub), max_nfev=2000)
        except Exception:
            continue
        if best is None or r.cost < best.cost:
            best = r
    v = best.x
    order = np.argsort([v[2 * k + 1] for k in range(n_exp)])
    a = np.array([v[2 * k] for k in order])
    tau = np.array([v[2 * k + 1] for k in order])
    return dict(a=a, tau=tau, kappa=(v[-1] if free_k else kappa), cost=best.cost)


def fit_exp_select(t, y, kappa=None, max_exp=2, nonneg=False):
    """Methods: fit sums of exponentials and keep the largest number for which every size is
    at least a tenth of the total, |a_k| >= sum|a| / 10."""
    fits = {}
    chosen = 1
    for k in range(1, max_exp + 1):
        f = fit_exp(t, y, k, kappa, nonneg=nonneg)
        fits[k] = f
        if np.all(np.abs(f["a"]) >= np.abs(f["a"]).sum() / 10):
            chosen = k
    return chosen, fits


# ---------------------------------------------------------------------------------------
# Per-file analyses, run in worker processes by the notebook

def spikes_whole_cell(trace, clipped, threshold):
    """Spikes in a whole-cell trace: upward crossings of the raw trace above the 10-ms
    median-clipped trace by more than threshold mV (assumption: the paper does not say how A1
    spikes were found, and GetSpikes.m's whole-cell mode is manual; the code's high-pass
    filter, designed for 4 kHz, attenuates spikes at 10 kHz). One spike per crossing, at
    the peak of the excursion."""
    d = trace - clipped
    a = d > threshold
    on = np.where(np.diff(a.astype(np.int8)) == 1)[0] + 1
    off = np.where(np.diff(a.astype(np.int8)) == -1)[0] + 1
    if a[0]:
        on = np.r_[0, on]
    if a[-1]:
        off = np.r_[off, len(a)]
    return np.array([s + int(np.argmax(d[s:e])) for s, e in zip(on, off)], dtype=np.int64)


def period_rates(rec, spikes, baseline_s=1.0):
    """Spike counts and durations (s) in: all silent periods ('silence'), the last
    baseline_s before each stimulus ('baseline'), and all stimulus periods ('sound')."""
    trig, evoked, spont = split_periods(rec)
    sp = np.sort(spikes)

    def count(a, b):
        return int(np.searchsorted(sp, b) - np.searchsorted(sp, a))

    out = dict(silence=[0, 0.0], baseline=[0, 0.0], sound=[0, 0.0])
    for a, b in spont:
        out["silence"][0] += count(a, b)
        out["silence"][1] += (b - a) / rec.sf
    for a, b in evoked:
        out["sound"][0] += count(a, b)
        out["sound"][1] += (b - a) / rec.sf
        a0 = max(0, a - int(baseline_s * rec.sf))
        if a - a0 > 0:
            out["baseline"][0] += count(a0, a)
            out["baseline"][1] += (a - a0) / rec.sf
    return out


def trial_correlation(trials):
    """Correlation of response traces across trials within each context, over the probe:
    (a) mean over pairs of trials, (b) mean correlation of each trial with the mean of the
    others. Averaged over contexts. Returns (a, b)."""
    n, m, T = trials.shape
    pa, pb = [], []
    for i in range(n):
        X = trials[i].astype(np.float64)
        C = np.corrcoef(X)
        iu = np.triu_indices(m, 1)
        pa.append(np.nanmean(C[iu]))
        s = X.sum(axis=0)
        pb.append(np.nanmean([np.corrcoef(X[j], (s - X[j]) / (m - 1))[0, 1] for j in range(m)]))
    return float(np.mean(pa)), float(np.mean(pb))


def autocorr(x, max_lag):
    """Mean normalised autocorrelation of the rows of x (Eq. 45: the autocorrelation divided
    by the variance), lags 0..max_lag samples, via FFT."""
    x = x - x.mean(axis=1, keepdims=True)
    T = x.shape[1]
    nfft = 1 << int(np.ceil(np.log2(2 * T)))
    F = np.fft.rfft(x, nfft, axis=1)
    ac = np.fft.irfft(F * np.conj(F), nfft, axis=1)[:, : max_lag + 1]
    ac = ac / ac[:, :1]
    return ac.mean(axis=0)


def _sig_runs(s):
    d = np.diff(np.r_[0, s.astype(np.int8), 0])
    return np.c_[np.where(d == 1)[0], np.where(d == -1)[0]]


def analyse_probe(trials, n_shuffle, seed, bin_k=10):
    """Significance (with noise floor) and fractional power for one probe set; series are
    stored as means over bin_k samples (1 ms; standard choice)."""
    p, s, noise = kw_significance(trials, n_shuffle=n_shuffle, rng=seed)
    tot, pred, inv = frac_power(trials)
    return dict(runs=_sig_runs(s), noise=bin_mean(noise, bin_k).astype(np.float32),
                total=bin_mean(tot, bin_k).astype(np.float32),
                pred=bin_mean(pred, bin_k).astype(np.float32),
                inv=bin_mean(inv, bin_k).astype(np.float32),
                pmin=float(p.min()))


def analyse_a1_file(path, n_shuffle=1000, seed=None, spike_thresholds=(5.0, 10.0, 20.0),
                    context_analysis=True, keep_probe_mean=False):
    """Everything the notebook needs from one A1 current-clamp file: spike counts by period
    for each spike threshold, and for each probe (CxtDep.m sets, blank probe included) its
    trial counts, significance and power with all contexts and without silence, trial
    correlations, and the noise autocorrelation."""
    rec = Recording(path)
    x = median_clip(rec.trace)
    out = dict(path=path, rep=rec.rep, n_frag=len(rec.stimuli), rectype=rec.rectype,
               unit=rec.unit, sf=rec.sf, n_samples=len(rec.trace), description=rec.description,
               vrange=(float(np.percentile(x, 1)), float(np.percentile(x, 99))), rates={})
    for th in spike_thresholds:
        out["rates"][th] = period_rates(rec, spikes_whole_cell(rec.trace, x, th))
    out["probes"] = []
    if not context_analysis or not rec.table or rec.rep is None:
        return out
    sets = probe_sets(rec, x, blank_probe=True)
    rng = np.random.default_rng(seed_of(path) if seed is None else seed)
    for q in sets:
        tr = q["trials"]
        r = dict(probe=q["probe"], contexts=q["contexts"], m=q["m"], T=q["T"], n_occ=q["n_occ"],
                 stim=(rec.stimuli[q["probe"] - 1]["description"] if q["probe"] > 0 else "silence"))
        if q["m"] >= 2:
            r["all"] = analyse_probe(tr, n_shuffle, int(rng.integers(2**31)))
            q0 = drop_context(q, SILENCE)
            r["nosil"] = analyse_probe(q0["trials"], n_shuffle, int(rng.integers(2**31))) if q0 else None
            r["ncx_nosil"] = len(q0["contexts"]) if q0 else 0
            r["corr"] = trial_correlation(tr)
            if q["probe"] > 0:
                eps = (tr - tr.mean(axis=1, keepdims=True)).reshape(-1, q["T"])
                r["noise_ac"] = bin_mean(autocorr(eps, 10000), 10).astype(np.float32)
            if keep_probe_mean:
                r["mean"] = np.stack([bin_mean(tr[i].mean(axis=0), 10) for i in range(len(tr))])
        out["probes"].append(r)
    # clock check: correlation across repeats of the response to the first sequence, aligned
    # on its triggers, and with repeat j shifted by j x 0.7 s (circularly within the sequence)
    trig, evoked, spont = split_periods(rec)
    seq1 = [k for k, t in enumerate(trig) if ":" in t["description"] and
            [int(v) for v in t["description"].split(":", 1)[1].split()] == rec.table[0]][: rec.rep]
    L = min(evoked[k][1] - evoked[k][0] for k in seq1)
    X = np.stack([x[evoked[k][0]:evoked[k][0] + L] for k in seq1])
    Xs = np.stack([np.roll(X[j], int(j * 0.7 * rec.sf)) for j in range(len(X))])
    iu = np.triu_indices(len(X), 1)
    out["clock"] = (float(np.corrcoef(X)[iu].mean()), float(np.corrcoef(Xs)[iu].mean()))
    # autocorrelation of spontaneous activity: the intersequence silences (whole, and
    # without their first 1 s), each cut to its first 5 s
    segs = [(a, b) for a, b in spont[1:] if b - a > 2 * rec.sf]
    for key, skip in (("spont_ac", 0), ("spont_ac_skip1s", rec.sf)):
        rows = [x[a + skip:a + skip + min(5 * rec.sf, b - a - skip)] for a, b in segs]
        L = min(len(r_) for r_ in rows) if rows else 0
        out[key] = (bin_mean(autocorr(np.stack([r_[:L] for r_ in rows]), 10000), 10).astype(np.float32)
                    if L > 10000 else None)
    return out


MGB_THRESHOLDS = ("auto", 20, 40)


def analyse_mgb_file(path):
    """MGB cell-attached file: spikes found on the high-pass filtered trace of GetSpikes.m (no
    median filter, as ViewResp.m does for non-whole-cell data) at three thresholds, since the
    paper gives none: 'auto' is GetSpikes.m's automatic rule (2/3 of the largest value, with
    its downward-spike rule); 20 and 40 are multiples of the robust SD of the filtered trace
    (median absolute value / 0.6745), assumption, with the code's manual-mode setting of no
    downward-spike rule. Counts by period, and per probe the PSTHs in 100-ms bins (Methods,
    Context dependence at suprathreshold level; CxtDep.m, psth)."""
    rec = Recording(path)
    out = dict(path=path, rep=rec.rep, rectype=rec.rectype, n_frag=len(rec.stimuli),
               description=rec.description, n_samples=len(rec.trace), sf=rec.sf, unit=rec.unit)
    f = signal.filtfilt(HP_NUM, [1.0], rec.trace)
    sd = np.median(np.abs(f)) / 0.6745
    spk = {}
    for key in MGB_THRESHOLDS:
        if key == "auto":
            spk[key], thr = extract_spikes(rec.trace, None, remove_downward=True)
        else:
            spk[key], thr = extract_spikes(rec.trace, key * sd, remove_downward=False)
        out.setdefault("threshold", {})[key] = float(thr)
    out["rates"] = {k: period_rates(rec, v) for k, v in spk.items()}
    # clock check: spikes (20 x SD threshold) in the 100 ms after and before each stimulus onset
    trig, evoked, spont = split_periods(rec)
    on = np.array([a for a, b in evoked])
    sp = np.sort(spk[20])
    w = int(0.1 * rec.sf)
    out["clock"] = (int(sum(np.searchsorted(sp, a + w) - np.searchsorted(sp, a) for a in on)),
                    int(sum(np.searchsorted(sp, a) - np.searchsorted(sp, a - w) for a in on)), len(on))
    out["probes"] = []
    if not rec.table or rec.rep is None:
        return out
    for key in MGB_THRESHOLDS:
        for q in probe_sets(rec, rec.trace, spikes=spk[key], blank_probe=False):
            r = [p for p in out["probes"] if p["probe"] == q["probe"]]
            if not r:
                out["probes"].append(dict(probe=q["probe"], contexts=q["contexts"], m=q["m"], T=q["T"],
                                          stim=rec.stimuli[q["probe"] - 1]["description"]))
                r = out["probes"][-1]
            else:
                r = r[0]
            r["psth_%s" % key] = psth(q["spikes"], q["T"] / rec.sf)
    return out


def psth(spikes, Tend, dt=0.1):
    """CxtDep.m, psth: PSTH per context in bins [k dt, (k+1) dt) from 0 to Tend, over the
    first m trials of each context (m the smallest count). Returns (n_contexts, n_bins)."""
    m = min(len(s) for s in spikes)
    edges = np.arange(0, Tend + dt, dt)
    out = []
    for s in spikes:
        allspk = np.concatenate([np.asarray(v) for v in s[:m]]) if m else np.array([])
        allspk = allspk[(allspk > 0) & (allspk <= Tend)]
        out.append(np.histogram(allspk, edges)[0] / m / dt)
    return np.array(out)
