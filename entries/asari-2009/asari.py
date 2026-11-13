"""Loading and context-dependence measures for CRCNS ac-1 (Asari's recordings).

Asari & Zador (2009), J Neurophysiol 102:2638-2656, doi:10.1152/jn.00577.2009.

The data set is three zip files in the public CRCNS bucket. `crcns-ac1.zip` holds the
documentation, the stimuli, the analysis code of the paper (asari/Tools) and Wehr's data;
`crcns-ac1-asari-results-1.zip` and `-2.zip` hold Asari's recordings, one MATLAB file per
recording, with the membrane potential (whole cell) or the raw cell-attached voltage at 10 kHz
(`response`), the stimulus triggers (`triggers`) and the metadata, with the stimulus sequences and
the "Effective repeats" in `param.notes`. The zips are stored without compression; members are
read in place over range requests and nothing is written to disk.

Where the parameters come from (paper = Methods of Asari & Zador 2009; code = the paper's
analysis script asari/Tools/CxtDep.m in crcns-ac1.zip, "Basic analysis script for Asari and
Zador", with GetEvoked.m, ViewResp.m and GetSpikes.m):

- Spike clipping by a 10-ms median filter and centring (paper, Analysis, paragraph 2). The
  filter is applied as GetEvoked.m does it (mean removed, MATLAB medfilt1 window of 100 samples,
  the recording offset in `param.recording.offset` subtracted first).
- The probe responses: each sequence presentation is cut at its trigger for the stimulus
  duration; a fragment's position in the sequence is the sum of the rounded durations of the
  fragments before it; the first `Effective repeats` presentations of each sequence are used;
  "silence" is a context (the last 4 s before a sequence) and a probe (the first 2.5 s after a
  sequence), and a probe enters when it has at least two different contexts; each context
  is cut to the smallest number of trials over the contexts (all from CxtDep.m).
- Significance measure: Kruskal-Wallis across contexts at every 0.1-ms point, P < 0.01 for
  at least 5 ms, noise floor from 1000 shuffles of trials across contexts (paper, Significance
  measure). The ranks are ordinal ranks with ties broken by trial order, the statistic has no
  tie correction, a run counts when its last and first significant points are at least 50
  samples apart, and a shuffle permutes whole trials (the same permutation at every time
  point), as KWtest in CxtDep.m does. `kw_significance(..., ties="average")` is a variant with
  average ranks.
- Fractional power: Eqs. 17 and 18 as FracPow in CxtDep.m computes them, each trial first
  centred on its mean over the probe period.
- MGB spikes: the high-pass filter and threshold of ExtractSpikes in GetSpikes.m, in its
  automatic mode (threshold two thirds of the largest filtered value, downward spikes removed),
  which ViewResp.m uses for cell-attached recordings (paper: "a high-pass filter and
  thresholding ... spike times were then assigned to the peaks"). PSTHs in 100-ms bins (paper,
  Context dependence at suprathreshold level; psth in CxtDep.m).
- Exponential fits (Eq. 44) by least squares, with the paper's rule for the number of
  exponentials. Start values: a grid, the best fit kept (a standard choice). Curves are averaged
  in 1-ms bins before fitting (a standard choice that does not change the fit).
"""

from __future__ import annotations

import io
import re
from functools import lru_cache

import fsspec
import numpy as np
import scipy.io as sio
from scipy import ndimage, optimize, signal, stats

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/"
DOI = "10.6080/K0KW5CXR"
MAIN_ZIP = "crcns-ac1.zip"
RESULT_ZIPS = ("crcns-ac1-asari-results-1.zip", "crcns-ac1-asari-results-2.zip")

SF = 10000            # Hz, every recording (checked in the notebook)
SMOOTH_MS = 10        # paper, Analysis: 10-ms median filter
ALPHA = 0.01          # paper: P < 0.01
ALPHA_SAMPLES = 50    # paper: for at least 5 ms; CxtDep.m: last - first >= 50 samples
N_SHUFFLE = 1000      # paper: 1000 shuffles per probe
BLANK_PROBE_S = 2.5   # CxtDep.m: silence as a probe, 2.5 s
BLANK_CONTEXT_S = 4.0  # CxtDep.m: silence as a context, 4 s
PSTH_BIN_S = 0.1      # paper: 100-ms bins
BLANK = "silence"

# ExtractSpikes in GetSpikes.m: equiripple high-pass FIR, applied forwards and backwards.
HP_FIR = np.array([-2.9419, -7.7633, -16.2976, -28.7498, -44.7001, -62.8034, -80.9099, -96.4457,
                   -106.9520, 889.3317, -106.9520, -96.4457, -80.9099, -62.8034, -44.7001,
                   -28.7498, -16.2976, -7.7633, -2.9419]) / 1000


# ----------------------------------------------------------------------------- reading
def open_zip(name):
    import zipfile
    return zipfile.ZipFile(fsspec.open(BUCKET + name, block_size=2**20).open())


def read_text(name):
    with fsspec.open(BUCKET + name, "rb") as f:
        return f.read().decode("latin1")


def checksums():
    """MD5 sums the data set publishes in checksums.md5."""
    out = {}
    for line in read_text("checksums.md5").splitlines():
        if line.strip():
            md5, fname = line.split()
            out[fname] = md5
    return out


def loadmat(fh, **kw):
    return sio.loadmat(fh, squeeze_me=True, struct_as_record=False, **kw)


@lru_cache(maxsize=None)
def member_index():
    """Map 'Results/<cell>/<file>.mat' (the paths in Summary.mat) to (zip, member)."""
    idx = {}
    for zname in RESULT_ZIPS:
        for info in open_zip(zname).infolist():
            if info.filename.endswith(".mat"):
                parts = info.filename.split("/")
                idx["Results/" + "/".join(parts[1:])] = (zname, info.filename, info.file_size)
    return idx


def summary():
    """asari/Summary.mat: the experiment groups, with each cell's files and descriptions."""
    z = open_zip(MAIN_ZIP)
    m = loadmat(io.BytesIO(z.read("asari/Summary.mat")))
    rows = []
    for gi, ex in enumerate(np.atleast_1d(m["experiment"])):
        for c in np.atleast_1d(ex.cell):
            files = [str(f) for f in np.atleast_1d(c.file)]
            descs = [" ".join(np.atleast_1d(d).astype(str)).strip() if not isinstance(d, str) else d
                     for d in np.atleast_1d(c.description)]
            cell = files[0].split("/")[1]
            for f, d in zip(files, descs):
                rows.append({"group": gi, "group_description": str(ex.description).strip(),
                             "reference": str(ex.reference).strip(), "cell": cell, "file": f,
                             "description": " ".join(d.split())})
    return rows


def load_recording(path, variables=None):
    """Stream one recording ('Results/...'); returns the MATLAB structures."""
    zname, member, _ = member_index()[path]
    z = open_zip(zname)
    with z.open(member) as fh:
        return loadmat(fh, variable_names=variables)


def notes_text(param):
    return "\n".join(str(s).rstrip() for s in np.atleast_1d(getattr(param, "notes", [])))


def parse_notes(param):
    """Sequences (lists of 1-based fragment indices) and effective repeats, from param.notes."""
    text = notes_text(param)
    rep = re.search(r"Effective repeats:\s*(\d+)", text)
    seqs = [list(map(int, s.split())) for s in re.findall(r"Seq\.\s*\d+:([\d\s]+)", text)]
    return seqs, (int(rep.group(1)) if rep else None)


def sequence_triggers(triggers):
    """Non-pulse triggers (GetEvoked.m leaves pulses out), with their sequence number."""
    out = []
    for t in np.atleast_1d(triggers):
        if "pulse" in str(t.type):
            continue
        d = str(getattr(t.param, "description", ""))
        m = re.match(r"\s*Sequence\s*(\d+)\s*:(.*)", d)
        out.append({"type": str(t.type), "time": int(t.time), "duration_ms": float(t.param.duration),
                    "seq": int(m.group(1)) if m else None,
                    "frags": list(map(int, m.group(2).split())) if m else None})
    return out


def trace_mv(response, offset=None):
    x = response.trace.astype(np.float64)
    if hasattr(response, "scale"):
        x = x * float(response.scale)
    if offset not in (None, ""):
        try:
            x = x - float(offset)
        except ValueError:
            pass
    return x


def median_clip(x, smooth_ms=SMOOTH_MS, sf=SF):
    """GetEvoked.m: mean removed, 2*smooth zero samples padded, medfilt1 of smooth_ms, mean added."""
    r = x.mean()
    pad = int(round(smooth_ms * 2))
    y = np.concatenate([np.zeros(pad), x - r, np.zeros(pad)])
    n = int(round(smooth_ms / 1000 * sf))
    y = ndimage.median_filter(y, size=n, mode="constant", cval=0.0)
    return y[pad:-pad] + r


def extract_spikes(x, threshold=None, remove_downward=True):
    """ExtractSpikes of GetSpikes.m (automatic mode when threshold is None). Returns sample indices."""
    f = signal.filtfilt(HP_FIR, [1.0], x)
    if threshold is None:
        a = np.abs(f)
        i = int(np.argmax(a))
        threshold = 2 / 3 * a[i]
        if threshold > 100:
            keep = np.ones(len(f), bool)
            keep[max(0, i - 30):i + 30] = False
            threshold = a[keep].max() * 2 / 3
    hi = f > threshold
    if not hi.any():
        return np.array([], int), threshold
    d = np.diff(np.concatenate([[0], hi.astype(np.int8), [0]]))
    starts, ends = np.where(d == 1)[0], np.where(d == -1)[0]
    peaks = np.array([s + int(np.argmax(f[s:e])) for s, e in zip(starts, ends)])
    if remove_downward:
        ok = []
        for p in peaks:
            w = f[max(0, p - 10):p + 11]
            ok.append(w.min() >= -f[p])
        peaks = peaks[np.array(ok, bool)]
    return peaks, threshold


# ----------------------------------------------------------------------------- probes
def fragment_samples(param, sf=SF):
    """Rounded fragment durations in samples (CxtDep.m: round(duration/1000*sf))."""
    return [int(round(float(s.param.duration) / 1000 * sf)) for s in np.atleast_1d(param.stimulus)]


def split_periods(x, trigs, sf=SF):
    """Evoked periods (from each trigger for the sequence duration) and the silences between."""
    ev, sp = [], []
    t1 = 0
    for t in trigs:
        t0 = t["time"] - 1  # MATLAB 1-based sample index
        sp.append((t1, t0))
        t1 = min(t0 + int(round(t["duration_ms"] * sf / 1000)), len(x))
        ev.append((t0, t1))
    sp.append((t1, len(x)))
    return ev, sp


def probe_trials(x, param, trigs, spikes=None, sf=SF, include_blank=True, blank_as_context=True,
                 min_contexts=2):
    """Per probe, the trials of each context, as CxtDep.m forms them.

    Returns a list of dicts: probe (1-based fragment index, or BLANK), contexts (sorted list
    of context labels; BLANK for silence), data (n_ctx x rep x T array of the probe period,
    for continuous x), spikes (per context, per trial, spike times in s from probe onset),
    rep, T, and occurrences.
    """
    seqs, rep = parse_notes(param)
    dur = fragment_samples(param, sf)
    nfr = len(dur)
    ev, sp = split_periods(x, trigs, sf)
    # presentations per sequence, in order, first `rep` of each
    pres = {}
    for k, t in enumerate(trigs):
        if t["seq"] is None:
            continue
        pres.setdefault(t["seq"], []).append(k)
    blank_probe = int(round(BLANK_PROBE_S * sf))
    # CxtDep.m shortens the blank probe to the shortest silence after a used presentation
    used = [k for s in pres for k in pres[s][:rep]]
    after = [sp[k + 1][1] - sp[k + 1][0] for k in used]
    blank_probe = min([blank_probe] + after)
    seq_frags = {}
    for t in trigs:
        if t["seq"] is not None:
            seq_frags[t["seq"]] = t["frags"]
    occ = {}  # probe -> list of (context, seq, onset offset in samples)
    for s, frags in seq_frags.items():
        ext = ([BLANK] if blank_as_context else [None]) + frags + ([BLANK] if include_blank else [])
        offs = np.concatenate([[0], np.cumsum([dur[f - 1] for f in frags])])
        for pos in range(1, len(ext)):
            probe, ctx = ext[pos], ext[pos - 1]
            if probe is None or ctx is None:
                continue
            occ.setdefault(probe, []).append((ctx, s, int(offs[pos - 1])))
    out = []
    keys = [p for p in range(1, nfr + 1) if p in occ] + ([BLANK] if include_blank and BLANK in occ else [])
    for p in keys:
        ctxs = sorted({c for c, _, _ in occ[p]}, key=lambda c: (c == BLANK, c if c != BLANK else 0))
        if len(ctxs) < min_contexts:
            continue
        T = blank_probe if p == BLANK else dur[p - 1]
        per = {c: [] for c in ctxs}
        per_spk = {c: [] for c in ctxs}
        for c, s, off in sorted(occ[p], key=lambda o: (o[1], o[2])):
            for k in pres.get(s, [])[:rep]:
                a = ev[k][0] + off
                if p == BLANK:
                    a = sp[k + 1][0]
                b = a + T
                if b > len(x):
                    continue
                per[c].append(x[a:b])
                if spikes is not None:
                    sel = spikes[(spikes > a) & (spikes <= b)]
                    per_spk[c].append((sel - a) / sf)
        m = min(len(v) for v in per.values())
        if m == 0:
            continue
        data = np.stack([np.stack(per[c][:m]) for c in ctxs]).astype(np.float32)
        out.append({"probe": p, "contexts": ctxs, "data": data, "rep": m, "T": T,
                    "spikes": [per_spk[c][:m] for c in ctxs] if spikes is not None else None,
                    "n_occurrences": {str(c): sum(1 for o in occ[p] if o[0] == c) for c in ctxs}})
    return out


# ----------------------------------------------------------------------------- measures
def _ranks(flat, ties):
    if ties == "ordinal":
        # MATLAB [~,r]=sort(x); [~,r]=sort(r): stable ordinal ranks
        return np.argsort(np.argsort(flat, axis=0, kind="stable"), axis=0, kind="stable") + 1.0
    return stats.rankdata(flat, axis=0)


def long_runs(b, min_gap=ALPHA_SAMPLES):
    """Keep runs of True whose last and first points are at least min_gap samples apart."""
    L = min_gap + 1
    b = np.asarray(b, bool)
    if b.shape[-1] < L:
        return np.zeros_like(b)
    c = np.cumsum(np.concatenate([np.zeros(b.shape[:-1] + (1,), np.int32), b.astype(np.int32)], -1), -1)
    full = (c[..., L:] - c[..., :-L]) == L          # window [t, t+L) all True
    starts = np.concatenate([full, np.zeros(b.shape[:-1] + (L - 1,), bool)], -1)
    cs = np.cumsum(np.concatenate([np.zeros(b.shape[:-1] + (1,), np.int32), starts.astype(np.int32)], -1), -1)
    lo = np.maximum(np.arange(b.shape[-1]) - L + 1, 0)
    covered = (cs[..., np.arange(b.shape[-1]) + 1] - cs[..., lo]) > 0
    return covered


def kw_significance(data, n_shuffle=N_SHUFFLE, rng=None, ties="ordinal", batch=50, return_p=False):
    """Significance measure for one probe. data: n_ctx x rep x T.

    Returns (signif bool T, noise float T: fraction of shuffles significant at each t).
    """
    M, rep, T = data.shape
    N = M * rep
    flat = data.reshape(N, T)
    r = _ranks(flat, ties).astype(np.float32)
    crit = stats.chi2.ppf(1 - ALPHA, M - 1)
    scale = 12.0 / (M * (N + 1))
    mid = (N + 1) / 2

    def kw_of(G):  # G: (S*M) x N group-mean operators
        rbar = (G @ r).reshape(-1, M, T)
        return scale * ((rbar - mid) ** 2).sum(1)

    G0 = np.kron(np.eye(M), np.ones((1, rep)) / rep).astype(np.float32)
    kw = kw_of(G0)[0]
    signif = long_runs(kw > crit)
    noise = np.zeros(T)
    if n_shuffle:
        rng = rng if rng is not None else np.random.default_rng(0)
        done = 0
        while done < n_shuffle:
            s = min(batch, n_shuffle - done)
            G = np.concatenate([G0[:, rng.permutation(N)] for _ in range(s)])
            noise += long_runs(kw_of(G) > crit).sum(0)
            done += s
        noise /= n_shuffle
    if return_p:
        return signif, noise, stats.chi2.sf(kw, M - 1)
    return signif, noise


def frac_power(data):
    """FracPow of CxtDep.m: per-time predictable (Eq. 17) and context-independent (Eq. 18) power."""
    n, rep, T = data.shape
    d = data.astype(np.float64)
    d = d - d.mean(axis=2, keepdims=True)       # each trial centred over the probe period
    total = d ** 2
    mt = d.mean(1)                               # n x T, context means
    pred = ((rep * mt ** 2 - total.mean(1)) / (rep - 1)).mean(0)
    inv = (n * mt.mean(0) ** 2 - (mt ** 2).mean(0)) / (n - 1)
    return pred, inv


def psth_sd(spk, T_s, rep=None, dt=PSTH_BIN_S):
    """psth in CxtDep.m: PSTH per context (bins from 0 by dt, histc), SD over contexts (n-1)."""
    edges = np.arange(0, T_s + 1e-12, dt)
    reps = min(len(s) for s in spk) if rep is None else rep
    ps = []
    for trials in spk:
        allsp = np.concatenate([np.asarray(t) for t in trials[:reps]]) if reps else np.array([])
        allsp = allsp[(allsp > 0) & (allsp <= T_s)]
        # histc: bin k counts edges[k] <= s < edges[k+1]; the last counts s == edges[-1]
        h = np.histogram(allsp, bins=np.append(edges, edges[-1] + dt))[0].astype(float)
        ps.append(h / reps / dt)
    ps = np.array(ps)
    return ps, ps.std(0, ddof=1)


def running_mean_0_2t(y):
    """Running average over [0, 2t] at each t (paper, Eq. 20), truncated at the curve's end."""
    c = np.concatenate([[0], np.cumsum(y)])
    t = np.arange(len(y))
    hi = np.minimum(2 * t, len(y) - 1)
    return c[hi + 1] / (hi + 1)


def bin_mean(y, k):
    n = len(y) // k
    return np.asarray(y[:n * k]).reshape(n, k).mean(1)


# ----------------------------------------------------------------------------- fits
def _model(t, p, n, kappa):
    y = np.zeros_like(t)
    for i in range(n):
        y = y + p[2 * i] * np.exp(-t / p[2 * i + 1])
    return y + (p[2 * n] if kappa is None else kappa)


def fit_exp(t, y, n, kappa=None, nonneg=False):
    """Least-squares fit of Eq. 44 with n exponentials; kappa fixed when given, free otherwise.
    nonneg bounds the sizes at zero (for decays of a proportion)."""
    ok = np.isfinite(y)
    t, y = np.asarray(t)[ok], np.asarray(y)[ok]
    best = None
    taus = [0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
    a0 = (y[0] - (kappa if kappa is not None else y[-1]))
    import itertools
    for combo in itertools.combinations(taus, n):
        p0 = []
        for tau in combo:
            p0 += [abs(a0) / n if nonneg else a0 / n, tau]
        lo = [0.0 if nonneg else -np.inf, 1e-4] * n
        hi = [np.inf, 100.0] * n
        if kappa is None:
            p0.append(y[-1]); lo.append(-np.inf); hi.append(np.inf)
        try:
            res = optimize.least_squares(lambda p: _model(t, p, n, kappa) - y, p0, bounds=(lo, hi))
        except Exception:
            continue
        if best is None or res.cost < best.cost:
            best = res
    p = best.x
    comps = sorted([(p[2 * i], p[2 * i + 1]) for i in range(n)], key=lambda c: c[1])
    out = {"n": n, "alpha": [c[0] for c in comps], "tau": [c[1] for c in comps],
           "kappa": float(p[2 * n]) if kappa is None else kappa, "sse": 2 * best.cost}
    return out


def fit_paper_rule(t, y, kappa=None, max_n=3, nonneg=False):
    """Fits with 1..max_n exponentials; keeps the largest n whose every |alpha_k| is at least a
    tenth of sum |alpha| (paper, Exponential curve fit)."""
    fits = [fit_exp(t, y, n, kappa, nonneg) for n in range(1, max_n + 1)]
    chosen = fits[0]
    for f in fits[1:]:
        a = np.abs(f["alpha"])
        if np.all(a >= a.sum() / 10):
            chosen = f
    return chosen, fits


# ----------------------------------------------------------------------------- per-file passes
AC_MAX_LAG = 10000    # 1 s of lags for the autocorrelations
AC_STEP = 10          # kept every 1 ms


def autocorr(x, max_lag=AC_MAX_LAG):
    """Autocorrelation of the mean-removed traces (rows), summed over rows, unnormalized."""
    x = np.atleast_2d(x).astype(np.float64)
    x = x - x.mean(1, keepdims=True)
    n = x.shape[1]
    nfft = 1 << int(np.ceil(np.log2(2 * n)))
    f = np.fft.rfft(x, nfft, axis=1)
    ac = np.fft.irfft(np.abs(f) ** 2, nfft, axis=1)[:, :max_lag + 1]
    return ac.sum(0)


def a1_spikes(x, method):
    """A1 spike detection, which the paper does not describe (two readings).

    'code': ExtractSpikes of GetSpikes.m with the starting values of its manual mode, the one
    ViewResp.m uses for whole-cell data (threshold 1 on the high-passed trace, downward spikes
    kept); the manual adjustment of the threshold cannot be repeated.
    'dvdt': upward crossings of 10 mV/ms in the raw membrane potential with a 2-ms dead time
    (a standard choice).
    """
    if method == "code":
        return extract_spikes(x, threshold=1.0, remove_downward=False)[0]
    dv = np.diff(x) * (SF / 1000)
    up = np.where((dv[1:] >= 10) & (dv[:-1] < 10))[0] + 1
    if len(up):
        up = up[np.concatenate([[True], np.diff(up) > 20])]
    return up


def mgb_spikes(x):
    """MGB spikes: ExtractSpikes in its automatic mode, as ViewResp.m uses it for cell-attached data."""
    return extract_spikes(x)[0]


def period_rates(spikes, ev, sp, sf=SF):
    """Spike counts and durations (s) in the stimulus periods and the silences (GetEvoked.m split)."""
    def count(periods):
        n = sum(int(np.sum((spikes >= a) & (spikes < b))) for a, b in periods)
        return n, sum(b - a for a, b in periods) / sf
    return count(ev), count(sp)


def onset_contrast(x, trigs, win_s=0.2, shift_s=3.0):
    """Clock check: mean of x in the window after each sequence trigger less the window before it,
    at the trigger times and at times shifted shift_s earlier (inside the preceding silence)."""
    w = int(win_s * SF)
    out = {}
    for name, sh in (("trigger", 0), ("shifted", int(shift_s * SF))):
        d = []
        for t in trigs:
            a = t["time"] - 1 - sh
            if a - w >= 0 and a + w <= len(x):
                d.append(x[a:a + w].mean() - x[a - w:a].mean())
        out[name] = np.array(d)
    return out


def count_probes(param):
    """Probes with at least two different contexts, with silence counted as a context or not."""
    seqs, rep = parse_notes(param)
    out = {}
    for with_blank in (True, False):
        occ = {}
        for s in seqs:
            ext = ([BLANK] if with_blank else [None]) + s
            for i in range(1, len(ext)):
                if ext[i - 1] is not None:
                    occ.setdefault(ext[i], set()).add(ext[i - 1])
        out["with_silence" if with_blank else "without_silence"] = sum(len(v) >= 2 for v in occ.values())
    return out


def file_info(m):
    p = m["param"]
    r = m["response"]
    trigs = sequence_triggers(m["triggers"])
    seqs, rep = parse_notes(p)
    import hashlib
    return {"trace_md5": hashlib.md5(np.ascontiguousarray(r.trace).tobytes()).hexdigest(),
            "recording_type": str(p.recording.type), "unit": str(getattr(r, "unit", "")),
            "sf": float(r.sf), "n_samples": int(np.size(r.trace)), "rep": rep, "n_seq": len(seqs),
            "n_trig": len(trigs), "trigger_types": sorted({t["type"] for t in trigs}),
            "description": " ".join(" ".join(np.atleast_1d(p.ID.description).astype(str)).split()),
            "animal": f'{p.ID.date}-{p.ID.animal}', "age": str(getattr(p.animal, "age", "")),
            "n_stimuli": len(np.atleast_1d(getattr(p, "stimulus", []))),
            "n_probes": count_probes(p) if seqs else {"with_silence": 0, "without_silence": 0}}


def a1_file_pass(m, do_context, rng=None, n_shuffle=N_SHUFFLE):
    """One whole-cell recording: firing rates, and when do_context, the per-probe measures."""
    p = m["param"]
    x_raw = trace_mv(m["response"], getattr(p.recording, "offset", None))
    trigs = sequence_triggers(m["triggers"])
    ev, sp = split_periods(x_raw, trigs)
    out = {"info": file_info(m), "rates": {}}
    out["info"]["vm_percentiles_mv"] = [float(v) for v in np.percentile(x_raw[::10], [1, 50, 99])]
    out["onset"] = onset_contrast(x_raw, trigs)
    for method in ("code", "dvdt"):
        out["rates"][method] = period_rates(a1_spikes(x_raw, method), ev, sp)
    if not do_context:
        return out
    x = median_clip(x_raw)
    # spontaneous autocorrelation over the intersequence silences (>= 2 s)
    sil = [(a, b) for a, b in sp if b - a >= 2 * SF]
    out["spont_ac"] = {"whole": sum(autocorr(x[a:b])[::AC_STEP] for a, b in sil) if sil else None,
                       "after_1s": sum(autocorr(x[a + SF:b])[::AC_STEP] for a, b in sil) if sil else None,
                       "n_silences": len(sil), "silence_s": [round((b - a) / SF, 2) for a, b in sil]}
    probes = []
    for pr in probe_trials(x, p, trigs):
        d = pr["data"]
        sig, noise = kw_significance(d, n_shuffle=n_shuffle, rng=rng)
        sig_avg, _ = kw_significance(d, n_shuffle=0, ties="average")
        pred, inv = frac_power(d)
        # trial-to-trial reliability within each context
        pairs, loo = [], []
        for c in range(d.shape[0]):
            tr = d[c].astype(np.float64)
            cc = np.corrcoef(tr)
            iu = np.triu_indices(len(tr), 1)
            pairs.append(np.nanmean(cc[iu]))
            loo.append(np.nanmean([np.corrcoef(tr[j], np.delete(tr, j, 0).mean(0))[0, 1] for j in range(len(tr))]))
        resid = d - d.mean(1, keepdims=True)
        ac = autocorr(resid.reshape(-1, d.shape[2]))[::AC_STEP]
        # variant: silence left out of the contexts (with 200 shuffles for its noise floor)
        keep = [i for i, c in enumerate(pr["contexts"]) if c != BLANK]
        nosil = None
        if len(keep) >= 2 and len(keep) < len(pr["contexts"]):
            s2, n2 = kw_significance(d[keep], n_shuffle=200, rng=rng)
            p2, i2 = frac_power(d[keep])
            nosil = {"signif": s2, "noise": n2.astype(np.float32), "pred": p2.astype(np.float32),
                     "inv": i2.astype(np.float32)}
        elif len(keep) == len(pr["contexts"]):
            nosil = "same"
        probes.append({"probe": pr["probe"], "contexts": pr["contexts"], "rep": pr["rep"], "T": pr["T"],
                       "nosil": nosil, "n_occurrences": pr["n_occurrences"],
                       "signif": sig, "noise": noise.astype(np.float32), "signif_avg_ties": sig_avg,
                       "pred": pred.astype(np.float32), "inv": inv.astype(np.float32),
                       "rel_pairs": float(np.mean(pairs)), "rel_loo": float(np.mean(loo)),
                       "rel_pairs_ctx": [float(v) for v in pairs], "noise_ac": ac})
    out["probes"] = probes
    return out


def mgb_file_pass(m, do_context, min_rep=10):
    """One cell-attached recording: firing rates, and PSTH SDs over contexts per probe."""
    p = m["param"]
    x = trace_mv(m["response"], getattr(p.recording, "offset", None))
    trigs = sequence_triggers(m["triggers"])
    ev, sp = split_periods(x, trigs)
    out = {"info": file_info(m), "rates": {}, "probes": []}
    spk = mgb_spikes(x)
    out["rates"]["code"] = period_rates(spk, ev, sp)
    out["onset"] = onset_contrast(np.bincount(spk, minlength=len(x)).astype(float) * SF, trigs)
    if not do_context or (out["info"]["rep"] or 0) < min_rep:
        return out
    for pr in probe_trials(x, p, trigs, spikes=spk):
        if pr["probe"] == BLANK:
            continue
        ps, sd = psth_sd(pr["spikes"], pr["T"] / SF)
        out["probes"].append({"probe": pr["probe"], "contexts": pr["contexts"],
                              "rep": pr["rep"], "T": pr["T"], "psth": ps, "sd": sd})
    return out


def pop_curve(arrays, mode, length):
    """Population average at each time of curves of different lengths.

    'running': over the probes still running at t; 'all': over all probes, a probe that has
    ended counting as zero. Returns (curve, number of probes running at t)."""
    s = np.zeros(length)
    c = np.zeros(length)
    for a in arrays:
        n = min(len(a), length)
        s[:n] += a[:n]
        c[:n] += 1
    if mode == "running":
        return s / np.maximum(c, 1), c
    return s / len(arrays), c


def runs(b, sf=SF):
    """(start, end) times in s of the runs of True in b."""
    d = np.diff(np.concatenate([[0], np.asarray(b, np.int8), [0]]))
    return [(a / sf, e / sf) for a, e in zip(np.where(d == 1)[0], np.where(d == -1)[0])]


# ----------------------------------------------------------------------------- synthetic sounds (Figure 8)
PROPERTIES = ("amplitude", "frequency", "AM", "FM", "higher-order")


def _num(v):
    a = np.atleast_1d(v).astype(float)
    return tuple(np.round(a, 6)) if a.size else ()


def property_families(param, ttype):
    """Sets of conditioning stimuli (1-based) that differ in one sound property only.

    The paper gives the principle (Methods, Stimulus design, paragraph 2: "only those frequency
    variants ... as conditioning stimuli for each probe fragment") and Table 1 the properties per
    ensemble; the sets for each recording are rebuilt here from the stimulus metadata, an
    assumption stated in the notebook:
    - TORC and DMR ensembles: the stimuli described as amplitude (or attenuation) variants form an
      amplitude set, bandwidth or frequency variants a frequency set; forward and time-reversed
      ("backward") variants are separate sets.
    - SoundTrans variants of a natural sound ('naturalistic'): the natural sound with its
      attenuated copies (amplitude), or with its frequency-shifted copies (frequency).
    - Modulated harmonic tones: the sets listed in the recording's notes when it lists them;
      otherwise stimuli that share every parameter but one: AMmean (amplitude), f0 (frequency),
      AMrange and AMstd (AM), FMrange and FMstd (FM).
    - Pink noise (MCN): each natural sound with the modulated colored noise made from it
      (higher-order).
    """
    st = list(np.atleast_1d(getattr(param, "stimulus", [])))
    names = [str(s.name).lower() for s in st]
    descs = [str(s.description).lower() for s in st]
    fam = {k: [] for k in PROPERTIES}
    idx = list(range(1, len(st) + 1))
    if ttype in ("torc", "dmr") or (ttype == "naturalistic" and len(st) > 6):
        for direction in ("forward", "backward", None):
            sel = [i for i in idx if "track" not in descs[i - 1] or ttype == "naturalistic"]
            if direction:
                sel = [i for i in sel if direction in names[i - 1]]
            elif any(("forward" in n or "backward" in n) for n in names):
                continue
            amp = [i for i in sel if "amplitude" in descs[i - 1] or hasattr(st[i - 1].param, "attenuation")]
            frq = [i for i in sel if ("bandwidth" in descs[i - 1] or "frequency" in descs[i - 1]) and i not in amp]
            if len(amp) >= 2:
                fam["amplitude"].append(amp)
            if len(frq) >= 2:
                fam["frequency"].append(frq)
    elif ttype == "naturalistic":
        nat = [i for i in idx if "track" in descs[i - 1]]
        amp = nat + [i for i in idx if "amplitude variant" in descs[i - 1]]
        frq = nat + [i for i in idx if "frequency variant" in descs[i - 1]]
        if len(amp) >= 2:
            fam["amplitude"].append(amp)
        if len(frq) >= 2:
            fam["frequency"].append(frq)
    elif ttype == "synthetic":
        text = notes_text(param)
        listed = re.findall(r"^\s*([\d,\-\s]+):\s*(amplitude|frequency|amplitude-modulation|frequency-modulation) variants",
                            text, flags=re.M)
        if listed:
            key = {"amplitude": "amplitude", "frequency": "frequency", "amplitude-modulation": "AM",
                   "frequency-modulation": "FM"}
            for spec, prop in listed:
                members = []
                for part in spec.split(","):
                    part = part.strip()
                    if "-" in part:
                        a, b = part.split("-")
                        members += list(range(int(a), int(b) + 1))
                    elif part:
                        members.append(int(part))
                fam[key[prop]].append(sorted(set(members)))
        else:
            mht = [i for i in idx if "modulated harmonic" in descs[i - 1]]
            def par(i, f):
                return _num(getattr(st[i - 1].param, f, []))
            groups = {"amplitude": ("AMmean",), "frequency": ("f0",), "AM": ("AMrange", "AMstd"), "FM": ("FMrange", "FMstd")}
            allf = sum(groups.values(), ())
            for prop, own in groups.items():
                others = [f for f in allf if f not in own]
                bucket = {}
                for i in mht:
                    bucket.setdefault(tuple(par(i, f) for f in others), []).append(i)
                for members in bucket.values():
                    if len({tuple(par(i, f) for f in own) for i in members}) >= 2:
                        fam[prop].append(members)
    elif ttype == "pinknoise":
        nat = {}
        for i in idx:
            m = re.search(r"natural sound fragment\s*(\d+)", names[i - 1])
            if m:
                nat.setdefault(int(m.group(1)), []).append(i)
        for i in idx:
            m = re.search(r"corresponding to natural sound\s*(\d+)", descs[i - 1])
            if m and int(m.group(1)) in nat:
                nat[int(m.group(1))].append(i)
        fam["higher-order"] = [v for v in nat.values() if len(v) >= 2]
    return fam


def synthetic_file_pass(m, rng=None, n_shuffle=N_SHUFFLE):
    """Significance and fractional power per probe and property, with only the conditioning
    stimuli of one property set as contexts (the largest set the probe was tested with)."""
    p = m["param"]
    trigs = sequence_triggers(m["triggers"])
    ttype = trigs[0]["type"] if trigs else ""
    fam = property_families(p, ttype)
    descs = [str(s.description).lower() for s in np.atleast_1d(getattr(p, "stimulus", []))]
    x = median_clip(trace_mv(m["response"], getattr(p.recording, "offset", None)))
    out = []
    for pr in probe_trials(x, p, trigs):
        if pr["probe"] == BLANK:
            continue
        for prop in PROPERTIES:
            best = []
            for members in fam[prop]:
                keep = [k for k, c in enumerate(pr["contexts"]) if c in members]
                if len(keep) > len(best):
                    best = keep
            if len(best) < 2:
                continue
            d = pr["data"][best]
            sig, noise = kw_significance(d, n_shuffle=n_shuffle, rng=rng)
            pred, inv = frac_power(d)
            out.append({"probe": pr["probe"], "property": prop, "ensemble": ttype,
                        "probe_type": "natural" if "track" in descs[pr["probe"] - 1] else "synthetic",
                        "contexts": [pr["contexts"][k] for k in best], "rep": pr["rep"], "T": pr["T"],
                        "signif": sig, "noise": noise.astype(np.float32), "pred": pred.astype(np.float32),
                        "inv": inv.astype(np.float32)})
    return out
