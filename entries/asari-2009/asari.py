"""Loading and measures for Asari and Zador (2009) on CRCNS ac-1.

The data are streamed from the public S3 bucket of CRCNS (crcnsarchive, ac-1/), opening each
zip in place with fsspec and zipfile. Nothing is written to disk.

Where each parameter comes from:

- The 10-ms median filter that clips spikes, the Kruskal-Wallis test at each 0.1-ms point with
  P < 0.01 held for 5 ms, the 1000 shuffles of the noise floor, Eqs. 17 to 20 and 43, the
  [0, 2t] running mean of the denominator, the 100-ms PSTH bins with k = 0 to 60 and the SD over
  contexts (Eq. 42): the claims file's criteria, which cite the paper's Methods (Analysis).
- How contexts, probes and repeats are formed (each probe needs at least two different
  contexts; the first fragment of a sequence has "silence" as its context; trials of a context
  are pooled over its occurrences and cut to the smallest count over contexts; the first
  "Effective repeats" presentations of each sequence are used; a 2.5-s silence probe after each
  sequence), the use of ordinal ranks in the Kruskal-Wallis test, the run rule (a run counts
  when its last point is at least 50 samples after its first), the removal of each trial's mean
  over the probe before the power measures, and the spike detector (the FIR high-pass filter of
  GetSpikes.m, a threshold of two thirds of the largest filtered value, spike times at the peaks
  of suprathreshold segments, downward spikes removed): the analysis code shipped in the data
  set (asari/Tools/CxtDep.m, ViewResp.m, GetEvoked.m, GetSpikes.m), which its header calls the
  "basic analysis script for Asari and Zador". The paper does not link it; it is used where the
  paper is silent, and each use is recorded as a deviation.
- The median filter length is 101 samples (an odd window for the 10-ms filter of the paper; the
  code's MATLAB medfilt1 uses 100), a standard choice that cannot change a result.
- The noise floor is computed by shuffling trials across contexts, as the Methods say; the
  number of shuffles is a parameter (1000 in the paper).
"""
from __future__ import annotations

import io
import re
import zipfile
from dataclasses import dataclass, field

import fsspec
import numpy as np
import scipy.io as sio
import scipy.ndimage as nd
from scipy import signal, stats
from scipy.optimize import curve_fit

DATASET = "crcns:ac-1/unversioned"  # CRCNS does not version data sets; MD5 sums in the notebook
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/"
ZIPS = {
    "main": "crcns-ac1.zip",
    1: "crcns-ac1-asari-results-1.zip",
    2: "crcns-ac1-asari-results-2.zip",
}
SF = 10000  # Hz, response.sf in every file (checked in the notebook)

# FIR high-pass filter of GetSpikes.m (ExtractSpikes), applied forward and backward
SPIKE_FIR = np.array([-2.9419, -7.7633, -16.2976, -28.7498, -44.7001, -62.8034, -80.9099,
                      -96.4457, -106.9520, 889.3317, -106.9520, -96.4457, -80.9099, -62.8034,
                      -44.7001, -28.7498, -16.2976, -7.7633, -2.9419]) / 1000


# ----------------------------------------------------------------------------------------------
# Reading
# ----------------------------------------------------------------------------------------------
_ZCACHE: dict = {}


def zips():
    """Open the three zip files of ac-1 in place (range requests)."""
    if not _ZCACHE:
        for k, f in ZIPS.items():
            _ZCACHE[k] = zipfile.ZipFile(fsspec.open(BASE + f, block_size=2 ** 20).open())
    return _ZCACHE


def read_member(path: str) -> bytes:
    """Read a file of asari/Results (path as Summary.mat gives it, 'Results/<dir>/<file>')."""
    name = path.split("/", 1)[1]
    for k in (1, 2):
        z = zips()[k]
        n = f"asari-results-{k}/{name}"
        try:
            return z.read(n)
        except KeyError:
            continue
    raise KeyError(path)


def _s(x):
    if isinstance(x, str):
        return x.strip()
    if isinstance(x, np.ndarray):
        return " ".join(_s(y) for y in x.ravel())
    return str(x)


def summary():
    """Rows of asari/Summary.mat: experiment index, its description, cell index, file, file
    description."""
    m = sio.loadmat(io.BytesIO(zips()["main"].read("asari/Summary.mat")), squeeze_me=True,
                    struct_as_record=False)
    rows = []
    for ei, ex in enumerate(np.atleast_1d(m["experiment"])):
        for ci, c in enumerate(np.atleast_1d(ex.cell)):
            fs = [c.file] if isinstance(c.file, str) else list(c.file)
            ds = [c.description] if isinstance(c.description, str) else list(c.description)
            for f, d in zip(fs, ds):
                rows.append(dict(exp=ei, exp_desc=_s(ex.description), cell=ci, file=f,
                                 desc=_s(d), cell_dir=f.split("/")[1]))
    return rows


@dataclass
class Recording:
    file: str
    rec_type: str
    trace: np.ndarray            # mV, offset-corrected as GetEvoked.m does, float32
    sf: float
    unit: str
    triggers: list               # (type, onset sample, duration ms, description)
    stim: list                   # dicts with name, description, file, param
    notes: list
    rep: int | None
    seqs: list                   # list of lists of fragment numbers (1-based)
    animal: dict
    recording: dict
    meta: dict = field(default_factory=dict)


def load(path: str) -> Recording:
    d = sio.loadmat(io.BytesIO(read_member(path)), squeeze_me=True, struct_as_record=False)
    r, p = d["response"], d["param"]
    tr = np.asarray(r.trace).astype(np.float32) * np.float32(r.scale)
    off = _s(getattr(p.recording, "offset", "")) if hasattr(p, "recording") else ""
    if off:
        try:
            tr -= np.float32(float(off))
        except ValueError:
            pass
    trig = []
    for x in np.atleast_1d(d["triggers"]):
        pa = x.param
        dur = float(getattr(pa, "duration", np.nan)) if hasattr(pa, "_fieldnames") else np.nan
        desc = _s(getattr(pa, "description", "")) if hasattr(pa, "_fieldnames") else ""
        trig.append((_s(x.type), float(x.time), dur, desc))
    stim = []
    if hasattr(p, "stimulus"):
        for x in np.atleast_1d(p.stimulus):
            pa = {}
            if hasattr(x, "param") and hasattr(x.param, "_fieldnames"):
                pa = {k: getattr(x.param, k) for k in x.param._fieldnames}
            stim.append(dict(name=_s(getattr(x, "name", "")),
                             description=_s(getattr(x, "description", "")),
                             file=_s(getattr(x, "file", "")), param=pa))
    notes = [_s(l) for l in np.atleast_1d(getattr(p, "notes", []))]
    rep, seqs = None, []
    for l in notes:
        if "Effective repeats:" in l:
            rep = int(l.split("Effective repeats:")[1].split()[0])
        mm = re.match(r"Seq\.\s*\d+:(.*)", l)
        if mm:
            seqs.append([int(v) for v in mm.group(1).split()])
    return Recording(file=path, rec_type=_s(p.recording.type), trace=tr, sf=float(r.sf),
                     unit=_s(r.unit), triggers=trig, stim=stim, notes=notes, rep=rep, seqs=seqs,
                     animal={k: _s(getattr(p.animal, k)) for k in p.animal._fieldnames},
                     recording={k: _s(getattr(p.recording, k)) for k in p.recording._fieldnames})


def median_clip(trace: np.ndarray, sf: float = SF, ms: float = 10.0) -> np.ndarray:
    """10-ms median filter that clips spikes (Methods, Analysis; window of 101 samples)."""
    n = int(round(ms / 1000 * sf)) | 1
    return nd.median_filter(trace, size=n, mode="nearest")


# ----------------------------------------------------------------------------------------------
# Periods: evoked (sound) and spontaneous (silence), as GetEvoked.m
# ----------------------------------------------------------------------------------------------
def periods(rec: Recording):
    """Evoked periods [start, stop) of every non-pulse trigger and the silent periods between
    them, in samples. Pulse triggers are left out of both, as GetEvoked.m does."""
    ev = []
    for typ, t0, dur, desc in rec.triggers:
        if "pulse" in typ:
            continue
        a = int(round(t0)) - 1
        b = min(a + int(round(dur * rec.sf / 1000)), len(rec.trace))
        ev.append((a, b, typ, desc))
    sp = []
    prev = 0
    for a, b, _, _ in ev:
        if a > prev:
            sp.append((prev, a))
        prev = b
    if prev < len(rec.trace):
        sp.append((prev, len(rec.trace)))
    return ev, sp


def pulse_windows(rec: Recording):
    out = []
    for typ, t0, dur, desc in rec.triggers:
        if "pulse" in typ:
            a = int(round(t0)) - 1
            out.append((a, a + int(round(dur * rec.sf / 1000))))
    return out


# ----------------------------------------------------------------------------------------------
# Context-probe structure, as CxtDep.m
# ----------------------------------------------------------------------------------------------
SILENCE = 0  # context label of the intersequence silence


def frag_samples(rec: Recording):
    return [int(round(s["param"]["duration"] / 1000 * rec.sf)) for s in rec.stim]


def presentations(rec: Recording):
    """For each sequence (1-based number as in the notes), the onsets (samples) of its first
    `rep` presentations, matching each natural or synthetic trigger by its description."""
    ev, sp = periods(rec)
    out = {i + 1: [] for i in range(len(rec.seqs))}
    for a, b, typ, desc in ev:
        mm = re.match(r"Sequence\s*(\d+)", desc)
        if mm:
            k = int(mm.group(1))
        else:
            continue
        if k in out:
            out[k].append((a, b))
    if rec.rep:
        out = {k: v[: rec.rep] for k, v in out.items()}
    return out


def context_probe_sets(rec: Recording, trace: np.ndarray, include_silence=True,
                       blank_probe=2.5, context_ok=None, probe_ok=None, context_map=None):
    """Probes of a recording, CxtDep.m style.

    Returns a list of dicts: probe (fragment number, or 'blank' for the silence after a
    sequence), contexts (fragment numbers, 0 for silence), X (n_ctx, rep, T) float32 responses
    over the probe, dur (s).
    `context_ok(c)` and `probe_ok(p)` restrict which fragments may serve as context or probe.
    """
    fs = frag_samples(rec)
    pres = presentations(rec)
    occ = {}  # (probe, context) -> list of onset samples of the probe
    seq_ends = []
    for si, seq in enumerate(rec.seqs, start=1):
        for (a, b) in pres.get(si, []):
            pos = a
            prev = SILENCE
            for f in seq:
                occ.setdefault((f, prev), []).append(pos)
                pos += fs[f - 1]
                prev = f
            seq_ends.append((pos, prev, b))
    if context_map is not None:
        # pool the occurrences of fragments that share a class of the varied property
        occ2 = {}
        for (p, c), v in occ.items():
            lab = context_map(c)
            if lab is None:
                continue
            occ2.setdefault((p, lab), []).extend(v)
        occ = {k: sorted(v) for k, v in occ2.items()}
    out = []
    probes = sorted({p for p, c in occ})
    for p in probes:
        if probe_ok is not None and not probe_ok(p):
            continue
        ctxs = sorted(c for (pp, c) in occ if pp == p)
        if not include_silence:
            ctxs = [c for c in ctxs if c != SILENCE]
        if context_ok is not None:
            ctxs = [c for c in ctxs if context_ok(c)]
        if len(ctxs) < 2:
            continue
        T = fs[p - 1]
        reps = min(len(occ[(p, c)]) for c in ctxs)
        if reps < 1:
            continue
        X = np.empty((len(ctxs), reps, T), np.float32)
        ok = True
        for i, c in enumerate(ctxs):
            for j, s0 in enumerate(occ[(p, c)][:reps]):
                seg = trace[s0:s0 + T]
                if len(seg) < T:
                    ok = False
                    break
                X[i, j] = seg
        if ok:
            out.append(dict(probe=p, contexts=ctxs, X=X, dur=T / rec.sf))
    if blank_probe:
        # silence after each sequence as a probe; context is the sequence's last fragment
        nb = int(round(blank_probe * rec.sf))
        by_ctx = {}
        for pos, last, b in seq_ends:
            if pos + nb <= len(trace):
                by_ctx.setdefault(last, []).append(pos)
        ctxs = sorted(by_ctx)
        if context_ok is not None:
            ctxs = [c for c in ctxs if context_ok(c)]
        if len(ctxs) >= 2:
            reps = min(len(by_ctx[c]) for c in ctxs)
            X = np.empty((len(ctxs), reps, nb), np.float32)
            for i, c in enumerate(ctxs):
                for j, s0 in enumerate(by_ctx[c][:reps]):
                    X[i, j] = trace[s0:s0 + nb]
            out.append(dict(probe="blank", contexts=ctxs, X=X, dur=blank_probe))
    return out


# ----------------------------------------------------------------------------------------------
# Significance measure (Kruskal-Wallis at each time point) and its noise floor
# ----------------------------------------------------------------------------------------------
def _ranks(X):
    """Ordinal ranks (1..N) over all trials at each time point; X (n, rep, T)."""
    n, rep, T = X.shape
    Y = X.reshape(n * rep, T)
    r = np.empty_like(Y, dtype=np.float32)
    order = np.argsort(Y, axis=0, kind="stable")
    np.put_along_axis(r, order, np.arange(1, n * rep + 1, dtype=np.float32)[:, None]
                      .repeat(T, axis=1), axis=0)
    return r


def _runs(mask, min_len):
    """Keep runs of True whose last point is at least `min_len` samples after the first."""
    L = min_len + 1
    h = L // 2
    m = mask.view(np.uint8) if mask.dtype == bool else mask.astype(np.uint8)
    # a binary opening with a line of L samples: erosion (all of [i, i+L-1] true), then dilation
    e = nd.minimum_filter1d(m, L, axis=-1, origin=-h, mode="constant", cval=0)
    d = nd.maximum_filter1d(e, L, axis=-1, origin=h if L % 2 else h - 1, mode="constant",
                            cval=0)
    return d.astype(bool)


def kw_significance(X, alpha=0.01, run_ms=5.0, sf=SF, n_shuffle=1000, rng=None,
                    chunk=100):
    """Kruskal-Wallis across contexts at each time point (Eq. 10 with ordinal ranks).

    Returns (signif bool (T,), noise float (T,) or None). The noise floor is the fraction of
    shuffles (trials shuffled across contexts) significant at each point.
    """
    n, rep, T = X.shape
    N = n * rep
    R = _ranks(X)
    crit = stats.chi2.isf(alpha, n - 1)
    run = int(round(run_ms / 1000 * sf))
    g = np.repeat(np.arange(n), rep)

    def kw_from_groups(Gsum):  # Gsum (..., n, T) rank sums per group
        rbar = Gsum / rep
        return 12.0 * ((rbar - (N + 1) / 2.0) ** 2).sum(axis=-2) / (n * (N + 1))

    Gs = np.zeros((n, T), np.float64)
    np.add.at(Gs, g, R)
    kw = kw_from_groups(Gs)
    signif = _runs(kw > crit, run)
    noise = None
    if n_shuffle and rng is not None:
        cnt = np.zeros(T, np.float64)
        done = 0
        while done < n_shuffle:
            S = min(chunk, n_shuffle - done)
            M = np.zeros((S * n, N), np.float32)
            for s in range(S):
                perm = rng.permutation(N)
                M[s * n + g[perm], np.arange(N)] = 1.0
            Gsh = (M @ R).reshape(S, n, T).astype(np.float64)
            sig = _runs(kw_from_groups(Gsh) > crit, run)
            cnt += sig.sum(axis=0)
            done += S
        noise = cnt / n_shuffle
    return signif, noise


# ----------------------------------------------------------------------------------------------
# Fractional power measure (Eqs. 17 to 19), per probe
# ----------------------------------------------------------------------------------------------
def power_terms(X, center="trial"):
    """Per-probe stimulus-related power (Eq. 17), context-independent power (Eq. 18) and the
    context-dependent power (Eq. 19), as FracPow in CxtDep.m.

    center='trial' removes each trial's mean over the probe (CxtDep.m); 'none' leaves the
    traces as they are (the Methods' zero-mean traces over the recording only shift each probe
    by a constant)."""
    X = X.astype(np.float64)
    if center == "trial":
        X = X - X.mean(axis=2, keepdims=True)
    n, rep, T = X.shape
    m = X.mean(axis=1)                      # (n, T) mean per context
    p2 = (X ** 2).mean(axis=1)              # (n, T)
    pred = ((rep * m ** 2 - p2) / (rep - 1)).mean(axis=0)
    inv = (n * m.mean(axis=0) ** 2 - (m ** 2).mean(axis=0)) / (n - 1)
    return pred, inv, pred - inv


def bin_mean(x, k=10):
    """Average consecutive blocks of k samples (0.1 ms -> 1 ms for k = 10)."""
    T = (len(x) // k) * k
    return x[:T].reshape(-1, k).mean(axis=1)


def running_02t(y, dt):
    """Running mean of y over [0, 2t] at each time t (Methods, Eq. 20), y sampled every dt."""
    c = np.concatenate([[0.0], np.cumsum(y)])
    n = len(y)
    i = np.arange(n)
    hi = np.minimum(2 * i + 1, n)
    out = (c[hi] - c[0]) / hi
    return out


def population_curve(arrs, length, running=True):
    """Average of per-probe arrays over probes at each time point. running=True averages over
    the probes still running at t; False counts probes that ended as zero (all probes)."""
    S = np.zeros(length)
    C = np.zeros(length)
    for a in arrs:
        L = min(len(a), length)
        S[:L] += a[:L]
        C[:L] += 1
    if running:
        with np.errstate(invalid="ignore"):
            return S / C, C
    return S / len(arrs), C


# ----------------------------------------------------------------------------------------------
# Exponential fits (Eq. 44)
# ----------------------------------------------------------------------------------------------
def _expsum(t, *p, kappa=0.0, k=1):
    y = np.full_like(t, kappa, dtype=float)
    for i in range(k):
        y = y + p[2 * i] * np.exp(-t / p[2 * i + 1])
    return y


def fit_exp(t, y, k=1, kappa=None, starts=None, positive=False):
    """Least-squares fit of Eq. 44 with k exponentials. kappa=None fits the constant; a number
    fixes it. A grid of start values is tried and the best fit kept (a standard choice; the paper
    gives none). Returns dict(alpha=[...], tau=[...], kappa=, sse=)."""
    t = np.asarray(t, float)
    y = np.asarray(y, float)
    ok = np.isfinite(y)
    t, y = t[ok], y[ok]
    taus = [0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 4.0]
    amp0 = y[: max(1, len(y) // 50)].mean() - (kappa if kappa is not None else y[-len(y) // 10:].mean())
    best = None
    import itertools
    for combo in itertools.combinations(taus, k):
        p0 = []
        for tau in combo:
            p0 += [amp0 / k, tau]
        lo = [0.0 if positive else -np.inf, 1e-3] * k
        if positive:
            p0 = [abs(v) if i % 2 == 0 else v for i, v in enumerate(p0)]
        hi = [np.inf, 100.0] * k
        if kappa is None:
            f = lambda tt, *p: _expsum(tt, *p[:-1], kappa=p[-1], k=k)
            p0 = p0 + [y[-len(y) // 10:].mean()]
            lo, hi = lo + [-np.inf], hi + [np.inf]
        else:
            f = lambda tt, *p: _expsum(tt, *p, kappa=kappa, k=k)
        try:
            p, _ = curve_fit(f, t, y, p0=p0, bounds=(lo, hi), maxfev=20000)
        except Exception:
            continue
        sse = float(((f(t, *p) - y) ** 2).sum())
        if best is None or sse < best[0]:
            best = (sse, p)
    if best is None:
        return None
    sse, p = best
    al = [float(p[2 * i]) for i in range(k)]
    ta = [float(p[2 * i + 1]) for i in range(k)]
    order = np.argsort(ta)
    return dict(alpha=[al[i] for i in order], tau=[ta[i] for i in order],
                kappa=float(p[-1]) if kappa is None else float(kappa), sse=sse)


def fit_select(t, y, kappa=None, kmax=3, positive=False):
    """Fits with 1..kmax exponentials and keeps the largest number for which every size is at
    least a tenth of the total (Methods, Exponential curve fit). Returns (chosen, all fits)."""
    fits = {}
    chosen = None
    for k in range(1, kmax + 1):
        f = fit_exp(t, y, k=k, kappa=kappa, positive=positive)
        fits[k] = f
        if f is None:
            continue
        a = np.abs(f["alpha"])
        if np.all(a >= a.sum() / 10):
            chosen = k
    return chosen, fits


# ----------------------------------------------------------------------------------------------
# Spikes
# ----------------------------------------------------------------------------------------------
def spike_filter(trace):
    return signal.filtfilt(SPIKE_FIR, [1.0], trace.astype(np.float64))


def detect_spikes(filtered, threshold, remove_downward=True, half=10):
    """Spike times (samples) at the peak of each segment above threshold (ExtractSpikes in
    GetSpikes.m); with remove_downward, a peak is dropped when the filtered trace within 10
    samples goes below minus its height."""
    above = filtered > threshold
    if not above.any():
        return np.array([], int)
    lab, nlab = nd.label(above)
    idx = nd.maximum_position(filtered, lab, index=np.arange(1, nlab + 1))
    pk = np.array([i[0] for i in idx], int)
    if remove_downward and len(pk):
        mins = nd.minimum_filter1d(filtered, 2 * half + 1, mode="nearest")[pk]
        pk = pk[~(mins < -filtered[pk])]
    return pk


def auto_threshold(filtered):
    """Two thirds of the largest absolute filtered value (ExtractSpikes, automatic mode)."""
    a = np.abs(filtered)
    i = int(np.argmax(a))
    th = 2 / 3 * a[i]
    if th > 100:
        b = a.copy()
        b[max(0, i - 30):i + 31] = 0
        th = 2 / 3 * b.max()
    return th


def mad_threshold(filtered, k=5.0):
    """k robust SDs (median absolute deviation / 0.6745) of the filtered trace, a standard
    choice used as a variant."""
    return k * np.median(np.abs(filtered)) / 0.6745


# ----------------------------------------------------------------------------------------------
# Small helpers
# ----------------------------------------------------------------------------------------------
def trial_correlation(X):
    """Reliability of a probe: (a) mean Pearson r over pairs of trials within a context, and (b)
    mean r of each trial with the mean of the other trials, each averaged over contexts."""
    n, rep, T = X.shape
    a_vals, b_vals = [], []
    for i in range(n):
        Y = X[i].astype(np.float64)
        if rep < 2:
            continue
        C = np.corrcoef(Y)
        iu = np.triu_indices(rep, 1)
        a_vals.append(np.nanmean(C[iu]))
        s = Y.sum(axis=0)
        bb = []
        for j in range(rep):
            o = (s - Y[j]) / (rep - 1)
            bb.append(np.corrcoef(Y[j], o)[0, 1])
        b_vals.append(np.nanmean(bb))
    return float(np.nanmean(a_vals)), float(np.nanmean(b_vals))


def autocorr(x, maxlag):
    """Autocorrelation of a mean-removed series normalized by its variance (Eq. 45), lags
    0..maxlag-1 samples."""
    x = np.asarray(x, float)
    x = x - x.mean()
    n = len(x)
    nf = 1 << int(np.ceil(np.log2(2 * n)))
    F = np.fft.rfft(x, nf)
    ac = np.fft.irfft(F * np.conj(F), nf)[:maxlag]
    return ac / ac[0]


def first_below(t, y, level):
    i = np.where(y < level)[0]
    return float(t[i[0]]) if len(i) else np.nan


# ----------------------------------------------------------------------------------------------
# Per-probe analysis and per-file drivers
# ----------------------------------------------------------------------------------------------
def analyse_probe(X, rng=None, n_shuffle=1000, acf=False, maxlag_ms=1000):
    """Everything the claims use from one probe: significance and noise floor at 0.1 ms; the
    power terms (Eqs. 17 to 19) at 1 ms, with each trial's mean removed (CxtDep.m) and without;
    reliability; and, with acf=True, the mean noise autocorrelation (Eq. 45) at 1 ms."""
    sig, noise = kw_significance(X, rng=rng, n_shuffle=n_shuffle)
    out = dict(sig=sig, noise=None if noise is None else bin_mean(noise).astype(np.float32))
    for c in ("trial", "none"):
        pred, inv, cd = power_terms(X, center=c)
        out[f"pred_{c}"] = bin_mean(pred).astype(np.float32)
        out[f"inv_{c}"] = bin_mean(inv).astype(np.float32)
    out["rel_pairs"], out["rel_loo"] = trial_correlation(X)
    if acf:
        res = X - X.mean(axis=1, keepdims=True)          # Eq. 14
        n, rep, T = X.shape
        acs = []
        for i in range(n):
            for j in range(rep):
                r = bin_mean(res[i, j].astype(np.float64))
                if len(r) > maxlag_ms:
                    acs.append(autocorr(r, maxlag_ms))
        out["acf"] = np.mean(acs, axis=0) if acs else None
    return out


def spont_acf(rec, trace, min_s=2.0, skip_s=0.0, maxlag_ms=1000):
    """Mean autocorrelation (Eq. 45) of the median-filtered trace over the intersequence
    silences of a recording, at 1 ms, leaving out the first `skip_s` seconds of each."""
    ev, sp = periods(rec)
    acs = []
    for a, b in sp[1:]:  # the period before the first sound is not an intersequence silence
        a2 = a + int(skip_s * rec.sf)
        if (b - a2) / rec.sf < min_s:
            continue
        r = bin_mean(trace[a2:b].astype(np.float64))
        acs.append(autocorr(r, maxlag_ms))
    return np.mean(acs, axis=0) if acs else None


NAT = re.compile(r"Track")


def is_natural(stim):
    return bool(NAT.search(stim["description"])) and "pink" not in stim["name"].lower()


def property_groups(rec):
    """Groups of conditioning fragments that differ in one sound property only (Methods,
    Stimulus design, paragraph 2; Table 1 columns), from the file's stimulus descriptions,
    parameters and notes. Returns a list of (property, set of fragment numbers)."""
    typ = rec.triggers[0][0] if rec.triggers else ""
    types = {t[0] for t in rec.triggers}
    st = rec.stim
    groups = []
    note_groups = []
    for l in rec.notes:
        mm = re.match(r"^([\d,\-\s]+):\s*(.*variants)", l)
        if mm:
            nums = set()
            for part in mm.group(1).split(","):
                part = part.strip()
                if "-" in part:
                    a, b = part.split("-")
                    nums |= set(range(int(a), int(b) + 1))
                elif part:
                    nums.add(int(part))
            name = mm.group(2).lower()
            prop = ("AM" if "amplitude-modulation" in name else
                    "FM" if "frequency-modulation" in name else
                    "amplitude" if "amplitude" in name else
                    "frequency" if "frequency" in name else None)
            if prop:
                note_groups.append((prop, nums))
    if note_groups:
        return note_groups
    if "synthetic" in types:
        mht = [i + 1 for i, s in enumerate(st) if "Harmonic" in s["description"]]
        if len(mht) >= 2:
            keys = ["f0", "AMmean", "AMstd", "AMrange", "FMrange", "FMstd"]
            vary = set()
            for k in keys:
                vals = {str(np.asarray(st[i - 1]["param"].get(k)).tolist()) for i in mht}
                if len(vals) > 1:
                    vary.add(k)
            if vary == {"AMmean"}:
                groups.append(("amplitude", set(mht)))
            elif vary == {"f0"}:
                groups.append(("frequency", set(mht)))
            elif vary and vary <= {"AMrange", "AMstd", "AMmean"}:
                groups.append(("AM", set(mht)))
            elif vary and vary <= {"FMrange", "FMstd"}:
                groups.append(("FM", set(mht)))
            else:
                groups.append(("mixed:" + ",".join(sorted(vary)), set(mht)))
        return groups
    if types & {"torc", "dmr"}:
        syn = [i + 1 for i, s in enumerate(st) if not is_natural(s)]
        d = " ".join(st[i - 1]["description"] for i in syn).lower()
        if "amplitude" in d:
            groups.append(("amplitude", set(syn)))
        elif "bandwidth" in d or "frequency" in d:
            groups.append(("frequency", set(syn)))
        return groups
    if "pinknoise" in types:
        nat = {}
        for i, s in enumerate(st):
            mm = re.match(r"natural sound fragment\s*(\d+)", s["name"])
            if mm:
                nat[int(mm.group(1))] = i + 1
        pn = {}
        for i, s in enumerate(st):
            mm = re.match(r"pink noise fragment\s*(\d+)", s["name"])
            if mm:
                pn.setdefault(int(mm.group(1)), set()).add(i + 1)
        for k, f in sorted(nat.items()):
            if k in pn:
                groups.append(("higher-order", {f} | pn[k]))
        return groups
    return groups


def _num(v):
    try:
        return str(np.round(np.asarray(v, float), 6).tolist())
    except Exception:
        return str(v)


def property_tests(rec):
    """Tests of one sound property for a file of the synthetic experiments: a list of
    (property, context_map), where context_map gives each conditioning fragment the class of
    the varied property (None for fragments not used). When a file varies two properties on a
    grid (AM rate by FM rate, or level by playing direction) or holds several natural sounds each
    with its colored noise, the fragments that share the value of the tested property are pooled
    into one context, so that each probe is tested once per property."""
    types = {t[0] for t in rec.triggers}
    st = rec.stim
    tests = []
    groups = property_groups(rec)
    for prop, G in groups:
        if prop.startswith("mixed"):
            keys = prop.split(":")[1].split(",")
            for k in keys:
                p2 = "AM" if k.startswith("AM") else "FM" if k.startswith("FM") else k
                vals = {i: _num(st[i - 1]["param"].get(k)) for i in G}
                tests.append((p2, lambda c, vals=vals: vals.get(c)))
        else:
            tests.append((prop, lambda c, G=G: c if c in G else None))
    if "pinknoise" in types and groups:
        allf = set().union(*[G for _, G in groups])
        tests = [("higher-order",
                  lambda c, allf=allf: (("PN" if "pink" in st[c - 1]["name"].lower() else "NS")
                                        if c in allf else None))]
    if not groups and "naturalistic" in types:
        att = {i + 1: _num(s["param"].get("attenuation", 1)) for i, s in enumerate(st)}
        names = {i + 1: s["description"].lower() for i, s in enumerate(st)}
        dfs = {i + 1: _num(s["param"]["df"]) for i, s in enumerate(st) if "df" in s["param"]}
        if len(set(att.values())) > 2 and all("variant" not in n for n in names.values()):
            tests.append(("amplitude", lambda c, att=att: att.get(c)))
        elif len(set(dfs.values())) > 2 and all("variant" not in n for n in names.values()):
            # natural sounds shifted in frequency (parameter df), forward or backward
            tests.append(("frequency", lambda c, dfs=dfs: dfs.get(c)))
        else:
            orig = [i for i, n in names.items() if "variant" not in n and "reversed" not in n
                    and "randomized" not in n]
            amp = [i for i, n in names.items() if "amplitude variant" in n]
            frq = [i for i, n in names.items() if "frequency variant" in n]
            if orig and amp:
                G = set(orig[:1] + amp)
                tests.append(("amplitude", lambda c, G=G: c if c in G else None))
            if orig and frq:
                G = set(orig[:1] + frq)
                tests.append(("frequency", lambda c, G=G: c if c in G else None))
    return tests


# ----------------------------------------------------------------------------------------------
# One pass over the data set
# ----------------------------------------------------------------------------------------------
def spike_counts(rec, spikes):
    """Spikes and seconds in sound periods (evoked) and in silent periods, two readings of the
    silent periods: (a) every silent period, (b) the 1 s before each sound onset."""
    ev, sp = periods(rec)
    s = np.sort(spikes)
    cnt = lambda a, b: int(np.searchsorted(s, b) - np.searchsorted(s, a))
    out = dict(ev_n=0, ev_t=0.0, sp_n=0, sp_t=0.0, pre_n=0, pre_t=0.0)
    for a, b, _, _ in ev:
        out["ev_n"] += cnt(a, b)
        out["ev_t"] += (b - a) / rec.sf
    for a, b in sp:
        out["sp_n"] += cnt(a, b)
        out["sp_t"] += (b - a) / rec.sf
    for a, b, _, _ in ev:
        a0 = max(0, a - int(rec.sf))
        out["pre_n"] += cnt(a0, a)
        out["pre_t"] += (a - a0) / rec.sf
    return out


def a1_spikes(rec):
    """A1 whole-cell spikes, two standard detectors (the paper gives none for A1): (a) upward
    crossings of -20 mV by the raw membrane potential, at least 2 ms apart; (b) peaks of the
    GetSpikes.m high-pass filtered trace above 2 mV (no removal of downward spikes, as in the
    code's manual mode for whole-cell recordings)."""
    v = rec.trace
    up = np.where((v[1:] > -20) & (v[:-1] <= -20))[0] + 1
    if len(up):
        keep = np.concatenate([[True], np.diff(up) > 0.002 * rec.sf])
        up = up[keep]
    f = spike_filter(v)
    pk = detect_spikes(f, 2.0, remove_downward=False)
    return dict(raw=up, filt=pk)


def mgb_spikes(rec):
    """MGB cell-attached spikes: GetSpikes.m automatic mode (FIR high-pass, threshold two
    thirds of the largest filtered value, peaks, downward spikes removed); variant with half that
    threshold."""
    f = spike_filter(rec.trace)
    th = auto_threshold(f)
    return dict(auto=detect_spikes(f, th, True), half=detect_spikes(f, th / 2, True),
                threshold=th)


def psth_sd(rec, spikes, include_silence=True, dt=0.1, kmax=60):
    """PSTHs in 100-ms bins [k dt, (k+1) dt) for k = 0..60 per context, and their SD over
    contexts with the n - 1 denominator (Eq. 42), for every probe with at least two contexts.
    Bins past the end of the probe are NaN."""
    fs = frag_samples(rec)
    pres = presentations(rec)
    s = np.sort(spikes)
    occ = {}
    for si, seq in enumerate(rec.seqs, start=1):
        for (a, b) in pres.get(si, []):
            pos, prev = a, SILENCE
            for f in seq:
                occ.setdefault((f, prev), []).append(pos)
                pos += fs[f - 1]
                prev = f
    out = []
    for p in sorted({p for p, c in occ}):
        ctxs = sorted(c for (pp, c) in occ if pp == p)
        if not include_silence:
            ctxs = [c for c in ctxs if c != SILENCE]
        if len(ctxs) < 2:
            continue
        reps = min(len(occ[(p, c)]) for c in ctxs)
        T = fs[p - 1] / rec.sf
        edges = np.arange(kmax + 2) * dt
        H = np.zeros((len(ctxs), kmax + 1))
        for i, c in enumerate(ctxs):
            for s0 in occ[(p, c)][:reps]:
                rel = (s[(s >= s0) & (s < s0 + fs[p - 1])] - s0) / rec.sf
                H[i] += np.histogram(rel, edges)[0]
        H = H / reps / dt
        sd = H.std(axis=0, ddof=1)
        sd[edges[1:] > T + 1e-9] = np.nan
        out.append(dict(probe=p, contexts=ctxs, reps=reps, dur=T, psth=H, sd=sd))
    return out


def run_pass(rows, rng_nat, rng_syn, rng_blank, n_shuffle=1000, log=print, limit=None):
    """Read every file once and compute what the claims use. Returns a dict of lists."""
    import time
    R = dict(nat=[], blank=[], syn=[], mgb=[], rates=[], spont_acf=[], files=[])
    t0 = time.time()
    todo = rows if limit is None else rows[:limit]
    for k, r in enumerate(todo):
        rec = load(r["file"])
        info = dict(file=r["file"], exp=r["exp"], cell=r["cell_dir"], desc=r["desc"],
                    type=rec.rec_type, sf=rec.sf, unit=rec.unit, n=len(rec.trace), rep=rec.rep,
                    nseq=len(rec.seqs), nstim=len(rec.stim),
                    trig_types=sorted({t[0] for t in rec.triggers}),
                    vmin=float(rec.trace.min()), vmax=float(rec.trace.max()),
                    age=rec.animal.get("age", ""), Rs=rec.recording.get("Rs", ""))
        R["files"].append(info)
        if r["exp"] == 1:
            sp = mgb_spikes(rec)
            for key in ("auto", "half"):
                R["rates"].append(dict(area="MGB", cell=r["cell_dir"], file=r["file"],
                                       detector=key, desc=r["desc"],
                                       **spike_counts(rec, sp[key])))
            if rec.seqs:
                for inc in (True, False):
                    for q in psth_sd(rec, sp["auto"], include_silence=inc):
                        R["mgb"].append(dict(cell=r["cell_dir"], file=r["file"], desc=r["desc"],
                                             silence=inc, detector="auto", **q))
                for q in psth_sd(rec, sp["half"], include_silence=True):
                    R["mgb"].append(dict(cell=r["cell_dir"], file=r["file"], desc=r["desc"],
                                         silence=True, detector="half", **q))
        else:
            sp = a1_spikes(rec)
            for key in ("raw", "filt"):
                R["rates"].append(dict(area="A1", cell=r["cell_dir"], file=r["file"],
                                       detector=key, desc=r["desc"],
                                       **spike_counts(rec, sp[key])))
        if r["exp"] == 0 and rec.seqs:
            tr = median_clip(rec.trace)
            for skip in (0.0, 1.0):
                a = spont_acf(rec, tr, skip_s=skip)
                if a is not None:
                    R["spont_acf"].append(dict(cell=r["cell_dir"], file=r["file"], skip=skip,
                                               acf=a))
            for p in context_probe_sets(rec, tr, include_silence=True):
                n, rep, T = p["X"].shape
                base = dict(cell=r["cell_dir"], file=r["file"], probe=p["probe"],
                            contexts=p["contexts"], n=n, rep=rep, dur=p["dur"])
                if p["probe"] == "blank":
                    res = analyse_probe(p["X"], rng=rng_blank, n_shuffle=n_shuffle)
                    R["blank"].append(dict(**base, **res))
                    continue
                res = analyse_probe(p["X"], rng=rng_nat, n_shuffle=n_shuffle, acf=True)
                res2 = {}
                if 0 in p["contexts"] and n - 1 >= 2:
                    X2 = p["X"][[i for i, c in enumerate(p["contexts"]) if c != 0]]
                    s2, n2 = kw_significance(X2, rng=rng_nat, n_shuffle=n_shuffle)
                    pr2, iv2, _ = power_terms(X2)
                    res2 = dict(sig_nosil=s2, noise_nosil=bin_mean(n2).astype(np.float32),
                                pred_nosil=bin_mean(pr2).astype(np.float32),
                                inv_nosil=bin_mean(iv2).astype(np.float32))
                elif 0 not in p["contexts"]:
                    res2 = dict(sig_nosil=res["sig"], noise_nosil=res["noise"],
                                pred_nosil=res["pred_trial"], inv_nosil=res["inv_trial"])
                X1 = np.stack([[bin_mean(x) for x in xc] for xc in p["X"]]).astype(np.float32)
                R["nat"].append(dict(**base, **res, **res2, X1=X1))
        if r["exp"] == 2 and rec.seqs:
            tr = median_clip(rec.trace)
            for prop, cm in property_tests(rec):
                for p in context_probe_sets(rec, tr, include_silence=False, blank_probe=0,
                                            context_map=cm):
                    n, rep, T = p["X"].shape
                    res = analyse_probe(p["X"], rng=rng_syn, n_shuffle=n_shuffle)
                    res["X1"] = np.stack([[bin_mean(x) for x in xc] for xc in p["X"]]).astype(
                        np.float32)
                    R["syn"].append(dict(cell=r["cell_dir"], file=r["file"], prop=prop,
                                         probe=p["probe"], natural=is_natural(
                                             rec.stim[p["probe"] - 1]),
                                         kind=rec.triggers[0][0], contexts=p["contexts"], n=n,
                                         rep=rep, dur=p["dur"], **res))
        del rec
        if log and (k % 20 == 0 or k == len(todo) - 1):
            log(f"{k + 1}/{len(todo)} files, {time.time() - t0:.0f} s")
    return R


def power_from_x1(X1, center="trial"):
    """Eqs. 17 and 18 from the 1-ms binned trials of a probe. center='trial' removes each
    trial's mean over the probe (CxtDep.m); 'probe' removes one mean over all trials, contexts and
    times of the probe (a stand-in for the Methods' zero-mean traces)."""
    X = X1.astype(np.float64)
    if center == "trial":
        X = X - X.mean(axis=2, keepdims=True)
    elif center == "probe":
        X = X - X.mean()
    n, rep, T = X.shape
    m = X.mean(axis=1)
    p2 = (X ** 2).mean(axis=1)
    pred = ((rep * m ** 2 - p2) / (rep - 1)).mean(axis=0)
    inv = (n * m.mean(axis=0) ** 2 - (m ** 2).mean(axis=0)) / (n - 1)
    return pred, inv


def q_curve(recs, length, center="trial", running=True, key_pred=None, key_inv=None,
            from_x1=False):
    """Population Q(t) (Eq. 20) and the predictability ratio (Eq. 43) at 1 ms, with the
    denominator smoothed over [0, 2t]; also the unsmoothed ratio. Returns dict of arrays."""
    if from_x1:
        terms = [power_from_x1(p["X1"], center) for p in recs]
        P = [a for a, b in terms]
        I = [b for a, b in terms]
    else:
        P = [p[key_pred or f"pred_{center}"] for p in recs]
        I = [p[key_inv or f"inv_{center}"] for p in recs]
    pr, C = population_curve(P, length, running)
    iv, _ = population_curve(I, length, running)
    sm = running_02t(np.nan_to_num(pr), 1e-3)
    with np.errstate(invalid="ignore", divide="ignore"):
        return dict(t=np.arange(length) * 1e-3 + 5e-4, pred=pr, inv=iv, cd=pr - iv, smooth=sm,
                    Q=(pr - iv) / sm, U=iv / sm, U_raw=iv / pr, count=C)
