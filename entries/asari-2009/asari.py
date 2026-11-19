"""Loading and context-dependence measures for CRCNS ac-1 (Asari & Zador 2009).

The data set is read in place from the public S3 bucket ``crcnsarchive``
(docs/archives.md, "CRCNS"): each zip is opened over range requests with
fsspec and ``zipfile``, and each MATLAB file is read into memory, reduced to
what the analysis needs, and dropped.

Where a parameter comes from:

- Paper, Methods, Analysis: the 10-ms median filter that clips spikes; the
  Kruskal-Wallis test at each 0.1-ms point, P < 0.01 held for 5 ms (50
  points); the shuffle noise floor (1000 shuffles of trials across contexts
  per probe); the power estimates of Eqs. 17 to 19 and the running mean over
  [0, 2t] of the denominator of Eqs. 20 and 43; Eq. 44 for the exponential
  fits and its rule that each exponential carry at least a tenth of the total;
  the 100-ms PSTH bins and Eq. 42 for the thalamus; Eq. 45 for the noise
  autocorrelation. MGB spikes by a high-pass filter and a threshold, with the
  spike at the peak (Methods, Analysis, paragraph 3).
- The authors' own analysis code, shipped with the data set
  (``asari/Tools/CxtDep.m``, ``GetEvoked.m``, ``ViewResp.m``, ``GetSpikes.m``
  in ``crcns-ac1.zip``; the paper does not link it). It settles details the
  Methods leave open, and is cited where used: how a recording is cut into
  context-probe pairs (the ``Seq.`` table and "Effective repeats" in the
  file's notes, the first ``rep`` presentations of each sequence, fragment
  lengths rounded to samples); that "silence" (the intersequence interval) is
  a context of the first fragment of each sequence; that each context keeps
  as many trials as the context with the fewest; ordinal ranks without a tie
  correction in the Kruskal-Wallis statistic; a significant run needs its last
  and first points 50 samples apart; the fractional power traces are each
  centred over the probe (``FracPow``) while the test uses the filtered
  traces; the MGB spike detector (``ExtractSpikes``: its high-pass FIR filter
  applied forwards and backwards, a threshold at two thirds of the largest
  filtered value, downward artefacts removed); PSTH bins starting at the
  probe onset.
- Standard choices that cannot change a result: the median filter's exact
  alignment for an even window (scipy's ``median_filter``), fitting the
  population curves at 1-ms resolution (means of ten 0.1-ms points), the
  start grid of the least-squares fits.
- Assumptions, each also stated in the notebook and the record: the A1 spike
  detector (the code extracts whole-cell spikes by hand), see ``a1_spikes``.
"""
from __future__ import annotations

import functools
import io
import re
import zipfile

import fsspec
import numpy as np
import scipy.io as sio
from scipy import optimize, signal, stats
from scipy.ndimage import median_filter

DATASET = "ac-1"
VERSION = "unversioned"  # CRCNS data sets are not versioned; the MD5 sums below pin the files
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/"
ZIPS = {
    "main": "crcns-ac1.zip",
    "r1": "crcns-ac1-asari-results-1.zip",
    "r2": "crcns-ac1-asari-results-2.zip",
}
# From the data set's checksums.md5 (read in the notebook's header).
MD5 = {
    "crcns-ac1.zip": "2300ee76d93383ab8c808ddf16761a23",
    "crcns-ac1-asari-results-1.zip": "18537da81d98e311c0274f62aea04daa",
    "crcns-ac1-asari-results-2.zip": "2f7ab955cc778fc6839ce59ed51bce89",
}
SF = 10000  # Hz, every file (checked in the notebook)


# --------------------------------------------------------------------------
# reading
# --------------------------------------------------------------------------
@functools.lru_cache(maxsize=None)
def open_zip(name: str) -> zipfile.ZipFile:
    return zipfile.ZipFile(fsspec.open(BUCKET + name, block_size=2**22).open())


@functools.lru_cache(maxsize=None)
def member_index() -> dict:
    """Map 'Results/<cell>/<file>.mat' to (zip name, member name)."""
    out = {}
    for key in ("r1", "r2"):
        z = open_zip(ZIPS[key])
        for i in z.infolist():
            if i.filename.endswith(".mat"):
                rel = "Results/" + i.filename.split("/", 1)[1]
                out[rel] = (ZIPS[key], i.filename)
    return out


def read_text(member: str) -> str:
    return open_zip(ZIPS["main"]).read(member).decode("latin-1")


def _lst(x):
    return list(np.atleast_1d(x))


def _s(x) -> str:
    if isinstance(x, np.ndarray):
        return " ".join(str(v).strip() for v in x.ravel())
    return str(x).strip()


def summary() -> list[dict]:
    """asari/Summary.mat: one row per (experiment, cell, file)."""
    m = sio.loadmat(io.BytesIO(open_zip(ZIPS["main"]).read("asari/Summary.mat")),
                    squeeze_me=True, struct_as_record=False)
    rows = []
    for ei, e in enumerate(_lst(m["experiment"])):
        for ci, c in enumerate(_lst(e.cell)):
            files = [str(f) for f in _lst(c.file)]
            descs = [_s(d) for d in (c.description if isinstance(c.description, np.ndarray)
                                     and c.description.dtype == object else [c.description])]
            if len(descs) != len(files):
                descs = [_s(d) for d in _lst(c.description)]
            for f, d in zip(files, descs):
                rows.append(dict(experiment=ei, experiment_description=_s(e.description),
                                 cell=f.split("/")[1], file=f, description=d))
    return rows


def parse_notes(notes) -> tuple[list[list[int]], int | None]:
    seqs, rep = [], None
    for line in notes:
        line = str(line)
        if "Effective repeats:" in line:
            rep = int(line.split(":")[1])
        if line.startswith("Seq."):
            seqs.append([int(x) for x in line.split(":", 1)[1].split()])
    return seqs, rep


def load(path: str, trace: bool = True) -> dict:
    """Read one recording file. ``path`` is 'Results/<cell>/<file>.mat'.

    The trace is returned in mV (int16 times ``response.scale``), as float32.
    """
    zname, member = member_index()[path]
    b = open_zip(zname).read(member)
    names = ["triggers", "param"] + (["response"] if trace else [])
    m = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False,
                    variable_names=names)
    del b
    p = m["param"]
    notes = [str(s) for s in _lst(p.notes)] if "notes" in p._fieldnames else []
    seqs, rep = parse_notes(notes)
    stim = []
    if "stimulus" in p._fieldnames:
        for s in _lst(p.stimulus):
            stim.append(dict(name=_s(s.name), description=_s(s.description),
                             file=_s(getattr(s, "file", "")),
                             param={k: getattr(s.param, k) for k in s.param._fieldnames}))
    trig = []
    for t in _lst(m.get("triggers", [])):
        trig.append(dict(type=str(t.type), time=int(t.time),
                         param={k: getattr(t.param, k) for k in t.param._fieldnames}))
    d = dict(path=path, cell=path.split("/")[1], rtype=str(p.recording.type),
             description=_s(p.ID.description), animal=f"{p.ID.date}-{p.ID.animal}",
             age=_s(getattr(p.animal, "age", "")), notes=notes, seqs=seqs, rep=rep,
             stim=stim, triggers=trig, offset=_s(getattr(p.recording, "offset", "")),
             Rs=_s(getattr(p.recording, "Rs", "")))
    if trace:
        r = m["response"]
        d["sf"] = int(r.sf)
        d["unit"] = str(r.unit)
        d["trace"] = (r.trace.astype(np.float32) * np.float32(r.scale))
    return d


def median_clip(trace: np.ndarray, ms: float = 10.0, sf: int = SF) -> np.ndarray:
    """10-ms median filter that clips spikes (Methods, Analysis, paragraph 1)."""
    return median_filter(trace, size=int(round(ms * sf / 1000)), mode="nearest")


# --------------------------------------------------------------------------
# cutting a recording into context-probe pairs (CxtDep.m)
# --------------------------------------------------------------------------
def fragment_samples(d: dict) -> np.ndarray:
    """Length of each stimulus fragment in samples, as CxtDep.m rounds it."""
    return np.array([int(round(float(s["param"]["duration"]) / 1000 * d["sf"]))
                     for s in d["stim"]])


def presentations(d: dict) -> list[dict]:
    """Sequence presentations in time order, with the sequence index (0-based)
    taken from the trigger's description "Sequence k: ..."."""
    out = []
    for t in d["triggers"]:
        if "pulse" in t["type"]:
            continue
        desc = _s(t["param"].get("description", ""))
        mm = re.match(r"Sequence\s+(\d+)\s*:(.*)", desc)
        if not mm:
            continue
        content = [int(v) for v in mm.group(2).split()]
        # the sequence whose content the trigger names; in two files the
        # trigger numbers (2, 4, 6, 8) are not the notes' (1 to 4)
        k = int(mm.group(1)) - 1
        if not (k < len(d["seqs"]) and d["seqs"][k] == content):
            k = next((i for i, q in enumerate(d["seqs"]) if q == content), None)
            if k is None:
                continue
        out.append(dict(seq=k, onset=t["time"] - 1,
                        duration=float(t["param"]["duration"])))
    return out


def pairs(d: dict, contexts=None, silence: bool = True) -> dict:
    """For each probe fragment (1-based index), the list of (context, onset of
    the probe in samples) over the first ``rep`` presentations of each
    sequence (CxtDep.m). Context 0 is "silence" (the intersequence interval
    before a sequence). ``contexts``: optional set of fragment indices allowed
    as contexts (Methods, Stimulus design, paragraph 2, for Figs. 7 and 8)."""
    lens = fragment_samples(d)
    seen = {}
    out: dict[int, list] = {}
    for pr in presentations(d):
        k = pr["seq"]
        seen[k] = seen.get(k, 0) + 1
        if d["rep"] is not None and seen[k] > d["rep"]:
            continue
        seq = d["seqs"][k]
        start = pr["onset"]
        for pos, frag in enumerate(seq):
            ctx = seq[pos - 1] if pos > 0 else 0
            use = silence if ctx == 0 else (contexts is None or ctx in contexts)
            if use:
                out.setdefault(frag, []).append((ctx, start, seen[k]))
            start += lens[frag - 1]
    return out


def probe_trials(d: dict, trace: np.ndarray, probe: int, plist: list,
                 min_ctx: int = 2, pre: int = 0, post: int = 0):
    """Stack the responses to one probe as (n contexts, m trials, T samples),
    with m the smallest trial count over contexts (GetResp in CxtDep.m) and T
    the probe length. ``pre``/``post`` extend the window before/after the probe.
    Returns None when fewer than ``min_ctx`` contexts."""
    T = fragment_samples(d)[probe - 1]
    by = {}
    for ctx, on, _ in plist:
        by.setdefault(ctx, []).append(on)
    ctxs = sorted(by)
    if len(ctxs) < min_ctx:
        return None
    m = min(len(v) for v in by.values())
    X = np.empty((len(ctxs), m, pre + T + post), np.float32)
    for i, c in enumerate(ctxs):
        for j, on in enumerate(by[c][:m]):
            seg = trace[on - pre: on + T + post]
            if len(seg) < pre + T + post:  # recording ends early
                return None
            X[i, j] = seg
    return dict(probe=probe, contexts=ctxs, m=m, X=X)


# --------------------------------------------------------------------------
# significance measure (Eq. 10; KWtest in CxtDep.m)
# --------------------------------------------------------------------------
def runs(mask: np.ndarray, min_gap: int = 50) -> np.ndarray:
    """Keep runs of True whose last and first index differ by >= min_gap
    (CxtDep.m: 5 ms at 10 kHz). Works on 1-D or on rows of a 2-D array."""
    mask = np.atleast_2d(mask)
    R, T = mask.shape
    pad = np.zeros((R, 1), bool)
    dm = np.diff(np.concatenate([pad, mask, pad], axis=1).astype(np.int8), axis=1)
    st = np.flatnonzero(dm.ravel() == 1)  # flat index into (R, T + 1)
    en = np.flatnonzero(dm.ravel() == -1)  # one past the run's end
    keep = (en - st - 1) >= min_gap
    mark = np.zeros(R * (T + 1) + 1, np.int32)
    np.add.at(mark, st[keep], 1)
    np.add.at(mark, en[keep], -1)
    out = np.cumsum(mark[:-1]).reshape(R, T + 1)[:, :T] > 0
    return out


def kw_significance(X: np.ndarray, alpha: float = 0.01, min_gap: int = 50,
                    nshuffle: int = 0, rng=None, batch: int = 50):
    """Pointwise Kruskal-Wallis across contexts. X: (n, m, T).

    Returns (KW statistic, significant mask, noise floor). Ranks are ordinal
    (ties broken by order, as CxtDep.m's double sort); no tie correction. The
    noise floor is the fraction of ``nshuffle`` shuffles of whole trials
    across contexts that are significant at each point."""
    n, m, T = X.shape
    N = n * m
    flat = X.reshape(N, T)
    r = np.empty((N, T), np.float32)
    order = np.argsort(flat, axis=0, kind="stable")
    np.put_along_axis(r, order, np.arange(1, N + 1, dtype=np.float32)[:, None], axis=0)
    crit = stats.chi2.ppf(1 - alpha, n - 1)
    c = (N + 1) / 2

    def kw_of(R):  # R: (..., N, T) -> (..., T)
        Rb = R.reshape(R.shape[:-2] + (n, m, T)).mean(axis=-2)
        return 12 * ((Rb - c) ** 2).sum(axis=-2) / (n * (N + 1))

    kw = kw_of(r)
    sig = runs(kw > crit, min_gap)[0]
    noise = None
    if nshuffle:
        noise = np.zeros(T, np.float64)
        done = 0
        G = np.zeros((n, N), np.float32)
        for i in range(n):
            G[i, i * m:(i + 1) * m] = 1.0 / m
        while done < nshuffle:
            b = min(batch, nshuffle - done)
            perms = np.stack([rng.permutation(N) for _ in range(b)])
            # group means of shuffled trials: G[:, perm^-1] @ r
            Gp = np.stack([G[:, np.argsort(p)] for p in perms])  # (b, n, N)
            Rb = Gp.reshape(b * n, N) @ r  # (b*n, T)
            K = 12 * ((Rb.reshape(b, n, T) - c) ** 2).sum(axis=1) / (n * (N + 1))
            noise += runs(K > crit, min_gap).sum(axis=0)
            done += b
        noise /= nshuffle
    return kw, sig, noise


# --------------------------------------------------------------------------
# fractional power measure (Eqs. 12 to 19; FracPow in CxtDep.m)
# --------------------------------------------------------------------------
def frac_power(X: np.ndarray):
    """X: (n, m, T). Each trace is centred over the probe (FracPow).
    Returns (stimulus-related power, Eq. 17 before the population average;
    context-independent power, Eq. 18; total power)."""
    n, m, T = X.shape
    Y = X.astype(np.float64)
    Y = Y - Y.mean(axis=2, keepdims=True)
    mu = Y.mean(axis=1)  # (n, T)
    pred = ((m * mu ** 2 - (Y ** 2).mean(axis=1)) / (m - 1)).mean(axis=0)
    inv = (n * mu.mean(axis=0) ** 2 - (mu ** 2).mean(axis=0)) / (n - 1)
    total = (Y ** 2).mean(axis=(0, 1))
    return pred, inv, total


def bin_mean(y: np.ndarray, k: int = 10) -> np.ndarray:
    """Mean over consecutive blocks of k samples (0.1 ms -> 1 ms)."""
    L = len(y) // k
    return y[: L * k].reshape(L, k).mean(axis=1)


def pop_average(curves: list[np.ndarray], length: int | None = None):
    """Average curves of different lengths. Returns (mean over the curves still
    running at each point, mean over all curves with zero past their end,
    number running)."""
    L = length or max(len(c) for c in curves)
    s = np.zeros(L)
    cnt = np.zeros(L)
    for c in curves:
        k = min(len(c), L)
        s[:k] += c[:k]
        cnt[:k] += 1
    with np.errstate(invalid="ignore", divide="ignore"):
        running = s / cnt
    return running, s / len(curves), cnt


def smooth_0_2t(y: np.ndarray) -> np.ndarray:
    """Running mean over [0, 2t] at each t (Methods, Eq. 20); where 2t passes
    the end of the curve, the mean over [0, end]."""
    cs = np.cumsum(y)
    idx = np.minimum(2 * np.arange(len(y)), len(y) - 1)
    return cs[idx] / (idx + 1)


# --------------------------------------------------------------------------
# exponential fits (Eq. 44)
# --------------------------------------------------------------------------
def _model(p, t, k, kappa):
    y = np.zeros_like(t)
    for i in range(k):
        y = y + p[2 * i] * np.exp(-t / p[2 * i + 1])
    return y + (p[2 * k] if kappa is None else kappa)


def fit_exp(t, y, k: int, kappa=None):
    """Least-squares fit of sum_k alpha_k exp(-t/tau_k) + kappa (free when
    ``kappa`` is None). A grid of start values; the best fit is kept (a
    standard choice: the paper gives none). tau bounded to (1 ms, 100 s)."""
    t = np.asarray(t, float)
    y = np.asarray(y, float)
    ok = np.isfinite(y)
    t, y = t[ok], y[ok]
    amp = y[0] - (kappa if kappa is not None else y[-1])
    taus = [0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
    starts = []
    if k == 1:
        for ta in taus:
            starts.append([amp, ta])
    else:
        for i, ta in enumerate(taus):
            for tb in taus[i + 1:]:
                for f in (0.3, 0.6, 0.8):
                    starts.append([amp * f, ta, amp * (1 - f), tb])
    best = None
    lo, hi = [], []
    for _ in range(k):
        lo += [-np.inf, 1e-3]
        hi += [np.inf, 100.0]
    if kappa is None:
        lo.append(-np.inf)
        hi.append(np.inf)
    for s in starts:
        s = list(s) + ([y[-1]] if kappa is None else [])
        try:
            res = optimize.least_squares(lambda p: _model(p, t, k, kappa) - y, s,
                                         bounds=(lo, hi), method="trf", max_nfev=4000)
        except Exception:
            continue
        if best is None or res.cost < best.cost:
            best = res
    p = best.x
    comps = sorted([(p[2 * i], p[2 * i + 1]) for i in range(k)], key=lambda a: a[1])
    out = dict(k=k, alpha=[a for a, _ in comps], tau=[b for _, b in comps],
               kappa=(p[2 * k] if kappa is None else kappa), sse=2 * best.cost)
    return out


def fit_select(t, y, kappa=None, kmax: int = 2):
    """Eq. 44 with the paper's rule for the number of exponentials: each
    |alpha_k| at least a tenth of the total. Tries kmax, then fewer."""
    fits = {}
    for k in range(kmax, 0, -1):
        f = fit_exp(t, y, k, kappa)
        fits[k] = f
        a = np.abs(f["alpha"])
        if np.all(a >= a.sum() / 10):
            return f, fits
    return fits[1], fits


# --------------------------------------------------------------------------
# spikes
# --------------------------------------------------------------------------
# High-pass FIR of ExtractSpikes in asari/Tools/GetSpikes.m.
HP_NUM = np.array([-2.9419, -7.7633, -16.2976, -28.7498, -44.7001, -62.8034, -80.9099,
                   -96.4457, -106.9520, 889.3317, -106.9520, -96.4457, -80.9099,
                   -62.8034, -44.7001, -28.7498, -16.2976, -7.7633, -2.9419]) / 1000


def extract_spikes(trace: np.ndarray, threshold: float | None = None,
                   remove_downward: bool = True, chunk: int = 5_000_000) -> np.ndarray:
    """Automatic spike detection of GetSpikes.m (``ExtractSpikes``), used by
    the authors' code for cell-attached recordings: the FIR high-pass applied
    with filtfilt, a threshold at 2/3 of the largest |filtered| value (with the
    code's guard against one spurious value above 100), the spike at the peak
    of each suprathreshold run, and runs whose 21-point neighbourhood dips below
    minus the peak removed. Returns spike sample indices."""
    x = trace.astype(np.float64)
    f = np.empty_like(x)
    for a in range(0, len(x), chunk):  # code filters 5e6-sample blocks
        b = min(len(x), a + chunk)
        if len(x) - b < chunk // 2:  # last short block joins the previous one
            b = len(x)
        f[a:b] = signal.filtfilt(HP_NUM, [1.0], x[a:b])
        if b == len(x):
            break
    if threshold is None:
        i = int(np.argmax(np.abs(f)))
        threshold = 2 / 3 * abs(f[i])
        if threshold > 100:
            g = np.abs(f).copy()
            g[max(0, i - 30): i + 30] = 0
            threshold = 2 / 3 * g.max()
    above = f > threshold
    pad = np.concatenate([[False], above, [False]]).astype(np.int8)
    st = np.flatnonzero(np.diff(pad) == 1)
    en = np.flatnonzero(np.diff(pad) == -1)
    peaks = np.array([a + int(np.argmax(f[a:b])) for a, b in zip(st, en)], int)
    if remove_downward and len(peaks):
        keep = []
        for pk in peaks:
            lo = f[max(0, pk - 10): pk + 11].min()
            keep.append(lo >= -f[pk])
        peaks = peaks[np.array(keep, bool)]
    return peaks


def a1_spikes(trace: np.ndarray, height: float = 15.0, sf: int = SF) -> np.ndarray:
    """A1 whole-cell spikes (an assumption: the authors' code extracts these
    by hand, GetSpikes.m with auto = 0, and the paper gives no detector).
    A spike is a peak of the raw trace minus its 10-ms median (the clipped
    trace of Methods, Analysis) that rises more than ``height`` mV, with peaks at
    least 2 ms apart. Readings of 10 and 20 mV are run in the notebook."""
    resid = trace - median_clip(trace)
    pk, _ = signal.find_peaks(resid, height=height, distance=int(0.002 * sf))
    return pk


def silences(d: dict, n: int) -> list[tuple[int, int]]:
    """Intersequence silences: sample ranges between the end of one sequence
    presentation (or the recording start) and the next (GetEvoked.m),
    excluding pulse triggers. ``n`` is the trace length."""
    pres = presentations(d)
    out = []
    t1 = 0
    for p in pres:
        out.append((t1, p["onset"]))
        t1 = p["onset"] + int(round(p["duration"] / 1000 * SF))
    out.append((t1, n))
    return [(a, b) for a, b in out if b > a]


def sounds(d: dict) -> list[tuple[int, int]]:
    return [(p["onset"], p["onset"] + int(round(p["duration"] / 1000 * SF)))
            for p in presentations(d)]


def psth_sd(spk_by_ctx: dict, T: float, dt: float = 0.1, m: int | None = None):
    """PSTH in bins [k dt, (k+1) dt) from probe onset for each context (rate in
    spike/s over ``m`` trials, the fewest of any context, as CxtDep.m's psth)
    and the SD over contexts with n - 1 (Eq. 42). Only whole bins inside the
    probe are kept. spk_by_ctx: context -> list of arrays of spike times (s)."""
    nb = int(np.floor(T / dt + 1e-9))
    m = m or min(len(v) for v in spk_by_ctx.values())
    P = []
    for c in sorted(spk_by_ctx):
        tr = spk_by_ctx[c][:m]
        allsp = np.concatenate(tr) if len(tr) else np.array([])
        h, _ = np.histogram(allsp, bins=np.arange(nb + 1) * dt)
        P.append(h / m / dt)
    P = np.array(P)
    return P, P.std(axis=0, ddof=1)


# --------------------------------------------------------------------------
# synthetic ensembles: which conditioning stimuli vary one property (Fig. 8)
# --------------------------------------------------------------------------
PROPERTIES = ("amplitude", "frequency", "AM", "FM", "higher-order")
_NUISANCE = {"iniphase", "envphase", "sinphase", "sf", "ramp", "duration", "iter",
             "torc_order", "tempmod", "specmod", "torc_parameters"}
# Parameters of SoundTrans.m / MHTones.m whose change defines each property
# (Methods, Synthetic sounds; Table 1 legend: amplitude, frequency, AM and FM
# rate and depth). For MHTs, a change of AMmean alone is a level change
# (amplitude); AMmean with AMstd, or AMrange, is AM depth or rate.
_KEYS = {"amplitude": {"attenuation"}, "frequency": {"f0", "df", "ff"},
         "AM": {"AMrange", "AMstd"}, "FM": {"FMrange", "FMstd"}}


def _norm(v):
    if hasattr(v, "_fieldnames"):
        return tuple((k, _norm(getattr(v, k))) for k in v._fieldnames)
    if isinstance(v, np.ndarray):
        if v.dtype == object:
            return tuple(_norm(x) for x in v.ravel())
        if v.dtype.kind in "US":
            return tuple(str(x) for x in v.ravel())
        return tuple(np.round(v.astype(float).ravel(), 6))
    if isinstance(v, float):
        return round(v, 6)
    return v


def is_natural(s: dict) -> bool:
    """A natural sound fragment or a transform of one (level, frequency shift,
    reversal): anything that is not a TORC, DMR, MHT or modulated coloured
    noise, nor silence."""
    desc = s["description"]
    return bool(desc) and desc != "[]" and not any(
        k in desc for k in ("TORC", "DMR", "Modulated Harmonic", "pink noise"))


def property_classes(d: dict) -> dict:
    """Sets of fragments (1-based) that differ from each other in one property
    only. TORC and DMR ensembles are labelled in their descriptions ("amplitude
    variants", "bandwidth variants", "frequency variants"); MHT and
    natural-sound variants are told apart by their parameters; a natural sound
    and the modulated coloured noise made from it (same stimulus file) form a
    higher-order class (Table 1 legend)."""
    st = d["stim"]
    out = {p: [] for p in PROPERTIES}
    typ = d["triggers"][0]["type"] if d["triggers"] else ""
    syl = lambda s: _norm(s["param"].get("syllables"))
    if typ in ("torc", "dmr"):
        groups = {}
        for i, s in enumerate(st, 1):
            desc = s["description"].lower()
            if is_natural(s):
                continue
            if "amplitude" in desc:
                p = "amplitude"
            elif "bandwidth" in desc or "frequency" in desc:
                p = "frequency"
            else:
                continue
            groups.setdefault((p, syl(s)), set()).add(i)
        for (p, _), g in groups.items():
            if len(g) >= 2:
                out[p].append(g)
        return out
    if typ == "pinknoise":
        groups = {}
        for i, s in enumerate(st, 1):
            groups.setdefault(s["file"], set()).add(i)
        for g in groups.values():
            kinds = {is_natural(st[i - 1]) for i in g}
            if len(g) >= 2 and kinds == {True, False}:
                out["higher-order"].append(g)
        return out
    if typ not in ("synthetic", "naturalistic"):
        return out
    params = []
    for s in st:
        p = {k: _norm(v) for k, v in s["param"].items() if k not in _NUISANCE}
        p["_src"] = s["file"] if typ == "naturalistic" else s["description"][:9]
        params.append(p)
    for prop in ("amplitude", "frequency", "AM", "FM"):
        keys = set(_KEYS[prop])
        if typ == "synthetic" and prop == "amplitude":
            keys = {"AMmean"}
        groups = {}
        for i, p in enumerate(params, 1):
            if st[i - 1]["description"] in ("", "[]"):
                continue
            if typ == "synthetic" and "Modulated Harmonic" not in st[i - 1]["description"]:
                continue
            sig = tuple(sorted((k, v) for k, v in p.items() if k not in keys
                               and not (prop == "AM" and k == "AMmean")))
            groups.setdefault(sig, []).append(i)
        for sig, g in groups.items():
            if len(g) < 2:
                continue
            vals = [tuple(params[i - 1].get(k) for k in sorted(keys)) for i in g]
            if len(set(vals)) < 2:
                continue
            out[prop].append(set(g))
    return out


def synthetic_tests(d: dict) -> list[dict]:
    """Each (property, probe, class) whose class gives the probe at least two
    conditioning stimuli; silence is left out (Methods, Stimulus design,
    paragraph 2: only the variants of the property are conditioning stimuli)."""
    P = pairs(d, silence=False)
    out = []
    for prop, classes in property_classes(d).items():
        for ci, cls in enumerate(classes):
            for probe in sorted(P):
                pl = [x for x in P[probe] if x[0] in cls]
                if len({x[0] for x in pl}) >= 2:
                    out.append(dict(prop=prop, probe=probe, cls=sorted(cls), ci=ci,
                                    natural=is_natural(d["stim"][probe - 1]), plist=pl))
    return out


# --------------------------------------------------------------------------
# per-file reductions (what the notebook keeps of each file)
# --------------------------------------------------------------------------
def _intervals(mask: np.ndarray) -> list[tuple[int, int]]:
    pad = np.concatenate([[0], mask.astype(np.int8), [0]])
    st = np.flatnonzero(np.diff(pad) == 1)
    en = np.flatnonzero(np.diff(pad) == -1)
    return list(zip(st.tolist(), en.tolist()))


def _acf(Y: np.ndarray, maxlag: int) -> np.ndarray:
    """Mean autocorrelation of the rows of Y (each centred), each normalised by
    its value at lag 0 (Eq. 45), for lags 0..maxlag-1."""
    Y = Y - Y.mean(axis=-1, keepdims=True)
    L = Y.shape[-1]
    nfft = 1 << int(np.ceil(np.log2(2 * L)))
    F = np.fft.rfft(Y, nfft, axis=-1)
    ac = np.fft.irfft(F * np.conj(F), nfft, axis=-1)[..., :maxlag]
    ac = ac / ac[..., :1]
    return ac.reshape(-1, maxlag).mean(axis=0)


def _corrs(X: np.ndarray):
    """Trial-to-trial correlation within each context. Returns, over contexts,
    (mean over pairs of trials, correlation of each trial with the mean of
    the others, all pairwise values)."""
    pair_all, loo = [], []
    for Xi in X:
        m = Xi.shape[0]
        C = np.corrcoef(Xi.astype(np.float64))
        iu = np.triu_indices(m, 1)
        pair_all.extend(C[iu].tolist())
        for j in range(m):
            others = np.delete(Xi, j, axis=0).mean(axis=0)
            loo.append(np.corrcoef(Xi[j], others)[0, 1])
    return float(np.mean(pair_all)), float(np.mean(loo)), pair_all


def _seed(seed: int, *keys) -> np.random.Generator:
    """Generator for one probe, derived from the claim's seed and the probe's
    fixed position (file, probe, class), so that runs in parallel draw the
    same numbers."""
    return np.random.default_rng(np.random.SeedSequence([seed, *keys]))


def reduce_wholecell(path: str, kind: str, seeds: list[int], fidx: int,
                     nshuffle: int = 1000, blank_s: float = 2.5) -> dict:
    """Everything the notebook needs from one current-clamp file.

    kind 'natural': probes over all fragments with silence as a context
    (CxtDep.m), and the variant without silence; the silence probes
    (Supplemental Fig. S1 in Methods, Stimulus design); trial correlations;
    noise and spontaneous autocorrelations. kind 'synthetic': the tests of
    ``synthetic_tests``. Both: spike counts in silences and sounds for the
    A1 rates. ``seeds``: the claim seed and its four offsets for the shuffles
    of the main reading (the first is also used for the variants)."""
    d = load(path)
    raw = d.pop("trace")
    x = median_clip(raw)
    n = len(x)
    out = dict(path=path, cell=d["cell"], animal=d["animal"], rep=d["rep"],
               description=d["description"], nsamples=n, sf=d["sf"], unit=d["unit"],
               age=d["age"], vrange=(float(np.percentile(x, 1)), float(np.percentile(x, 99))))
    # spikes for the firing-rate claim
    sil = silences(d, n)
    snd = sounds(d)
    out["silence_s"] = sum(b - a for a, b in sil) / SF
    out["sound_s"] = sum(b - a for a, b in snd) / SF
    sil_late = [(a + SF, b) for a, b in sil if b - a > SF]
    out["silence_late_s"] = sum(b - a for a, b in sil_late) / SF
    resid = raw - x
    for h in (10.0, 15.0, 20.0):
        pk, _ = signal.find_peaks(resid, height=h, distance=int(0.002 * SF))
        def cnt(iv):
            return int(sum(((pk >= a) & (pk < b)).sum() for a, b in iv))
        out[f"spk{int(h)}"] = dict(silence=cnt(sil), sound=cnt(snd), silence_late=cnt(sil_late))
    del resid, raw
    lens = fragment_samples(d)
    out["frag_s"] = (lens / SF).tolist()
    out["stim"] = [s["description"] for s in d["stim"]]
    out["seqs"] = d["seqs"]
    tests = []
    if kind == "natural":
        P = pairs(d, silence=True)
        for probe in sorted(P):
            pt = probe_trials(d, x, probe, P[probe])
            if pt is None:
                continue
            X = pt["X"]
            rec = dict(probe=probe, contexts=pt["contexts"], m=pt["m"], T=X.shape[2])
            noises = []
            for si, s in enumerate(seeds):
                kw, sig, noise = kw_significance(X, nshuffle=nshuffle,
                                                 rng=_seed(s, fidx, probe))
                noises.append(bin_mean(noise).astype(np.float32))
            rec["sig"] = _intervals(sig)
            rec["noise"] = noises
            pred, inv, tot = frac_power(X)
            rec["pred"], rec["inv"], rec["tot"] = bin_mean(pred), bin_mean(inv), bin_mean(tot)
            # power per probe for Fig. 2E style checks (context-dependent)
            rec["corr_pair"], rec["corr_loo"], pa = _corrs(X)
            rec["corr_pair_sd"] = float(np.std(pa))
            # noise autocorrelation (Eqs. 14, 45), lags to 1 s
            eps = X - X.mean(axis=1, keepdims=True)
            rec["acf_noise"] = bin_mean(_acf(eps.reshape(-1, X.shape[2]).astype(np.float64),
                                             SF), 1)[: SF : 10].astype(np.float32)
            # variant: silence not a context
            ctx_ns = [c for c in pt["contexts"] if c != 0]
            if len(ctx_ns) >= 2:
                keep = [i for i, c in enumerate(pt["contexts"]) if c != 0]
                Xn = X[keep]
                kw, sig, noise = kw_significance(Xn, nshuffle=nshuffle,
                                                 rng=_seed(seeds[0], fidx, probe, 1))
                pn, iv, _ = frac_power(Xn)
                rec["ns"] = dict(sig=_intervals(sig), noise=bin_mean(noise).astype(np.float32),
                                 pred=bin_mean(pn), inv=bin_mean(iv), n=len(keep))
            tests.append(rec)
        # silence probes: the first blank_s of the interval after each sequence,
        # its context the sequence's last fragment (CxtDep.m, blank probe)
        pres = presentations(d)
        seen, segs = {}, []
        for i, pr in enumerate(pres):
            k = pr["seq"]
            seen[k] = seen.get(k, 0) + 1
            if d["rep"] is not None and seen[k] > d["rep"]:
                continue
            end = pr["onset"] + int(sum(lens[f - 1] for f in d["seqs"][k]))
            nxt = pres[i + 1]["onset"] if i + 1 < len(pres) else n
            segs.append((d["seqs"][k][-1], end, nxt - end))
        L = int(min(blank_s * SF, min(g for _, _, g in segs))) if segs else 0
        by = {}
        for c, e, _ in segs:
            by.setdefault(c, []).append(e)
        out["blank"] = None
        if len(by) >= 2 and L > 0:
            m = min(len(v) for v in by.values())
            X = np.stack([np.stack([x[e:e + L] for e in by[c][:m]]) for c in sorted(by)])
            kw, sig, _ = kw_significance(X)
            pred, inv, tot = frac_power(X)
            out["blank"] = dict(contexts=sorted(by), m=m, T=L, sig=_intervals(sig),
                                pred=bin_mean(pred), inv=bin_mean(inv))
        # spontaneous autocorrelation over the intersequence intervals
        acs, acs_late = [], []
        for a, b in sil:
            if b - a >= 2 * SF:
                acs.append(_acf(x[a:b][None].astype(np.float64), SF)[::10])
            if b - a >= 3 * SF:
                acs_late.append(_acf(x[a + SF:b][None].astype(np.float64), SF)[::10])
        out["acf_spont"] = np.mean(acs, axis=0).astype(np.float32) if acs else None
        out["acf_spont_late"] = np.mean(acs_late, axis=0).astype(np.float32) if acs_late else None
    else:
        for ti, t in enumerate(synthetic_tests(d)):
            pt = probe_trials(d, x, t["probe"], t["plist"])
            if pt is None:
                continue
            X = pt["X"]
            rec = dict(prop=t["prop"], probe=t["probe"], cls=t["cls"], natural=t["natural"],
                       contexts=pt["contexts"], m=pt["m"], T=X.shape[2])
            noises = []
            for s in seeds:
                kw, sig, noise = kw_significance(X, nshuffle=nshuffle,
                                                 rng=_seed(s, fidx, t["probe"], ti))
                noises.append(bin_mean(noise).astype(np.float32))
            rec["sig"] = _intervals(sig)
            rec["noise"] = noises
            pred, inv, tot = frac_power(X)
            rec["pred"], rec["inv"] = bin_mean(pred), bin_mean(inv)
            tests.append(rec)
    out["tests"] = tests
    return out


def reduce_mgb(path: str) -> dict:
    """Spikes and PSTHs of one cell-attached (MGB) file. Spikes by the
    authors' automatic detector (``extract_spikes``) and, as a variant, by the
    same detector with half its threshold (a third of the largest filtered
    value), to show how much the threshold matters."""
    d = load(path)
    raw = d.pop("trace")
    n = len(raw)
    out = dict(path=path, cell=d["cell"], animal=d["animal"], rep=d["rep"],
               description=d["description"], nsamples=n, seqs=d["seqs"],
               frag_s=(fragment_samples(d) / SF).tolist())
    xf = signal.filtfilt(HP_NUM, [1.0], raw.astype(np.float64))
    i = int(np.argmax(np.abs(xf)))
    thr = 2 / 3 * abs(xf[i])
    del xf
    spk = {"code": extract_spikes(raw),
           "half": extract_spikes(raw, threshold=thr / 2)}
    out["thr_code"] = float(thr)
    sil, snd = silences(d, n), sounds(d)
    out["silence_s"] = sum(b - a for a, b in sil) / SF
    out["sound_s"] = sum(b - a for a, b in snd) / SF
    sil_late = [(a + SF, b) for a, b in sil if b - a > SF]
    out["silence_late_s"] = sum(b - a for a, b in sil_late) / SF
    lens = fragment_samples(d)
    P = pairs(d, silence=True)
    for key, pk in spk.items():
        def cnt(iv):
            return int(sum(((pk >= a) & (pk < b)).sum() for a, b in iv))
        out[f"spk_{key}"] = dict(silence=cnt(sil), sound=cnt(snd), silence_late=cnt(sil_late),
                                 n=len(pk))
        probes = []
        for probe in sorted(P):
            by = {}
            for ctx, on, _ in P[probe]:
                by.setdefault(ctx, []).append(on)
            if len(by) < 2:
                continue
            T = lens[probe - 1]
            m = min(len(v) for v in by.values())
            sp = {c: [(pk[(pk > on) & (pk <= on + T)] - on) / SF for on in by[c][:m]]
                  for c in by}
            Pm, sd = psth_sd(sp, T / SF, 0.1, m)
            probes.append(dict(probe=probe, contexts=sorted(by), m=m, T=T / SF,
                               psth=Pm, sd=sd))
        out[f"probes_{key}"] = probes
    return out


def file_lists() -> dict:
    """Files of each experiment in asari/Summary.mat, left out the tuning
    curves: 'natural' (A1, natural sound ensembles), 'mgb', 'synthetic'
    (A1, synthetic ensembles); experiment 4 (a variety of stimuli, not in the
    context design) is not used. Files listed but absent from the zips are
    returned under 'absent'."""
    idx = member_index()
    out = {"natural": [], "mgb": [], "synthetic": [], "absent": [], "other": []}
    names = {0: "natural", 1: "mgb", 2: "synthetic"}
    for r in summary():
        if r["file"] not in idx:
            out["absent"].append(r["file"])
            continue
        if r["description"].startswith("tuning"):
            continue
        out[names.get(r["experiment"], "other")].append(r["file"])
    return out


def run_many(fn, args: list[tuple], workers: int = 4) -> list:
    """Run ``fn(*a)`` for each a in a pool of processes, results in order."""
    import multiprocessing as mp
    from concurrent.futures import ProcessPoolExecutor
    # spawn, not fork: fsspec's event-loop thread does not survive a fork
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        futs = [ex.submit(fn, *a) for a in args]
        return [f.result() for f in futs]


# --------------------------------------------------------------------------
# population curves from the per-file reductions
# --------------------------------------------------------------------------
def sig_curve(tests: list[dict], noise_index: int = 0, sub: str | None = None):
    """Proportion of probes significant at each 1-ms bin after probe onset and
    the noise floor, both under two readings of the denominator: the probes
    still running at t ('running') and all probes ('all'). ``sub``: take the
    record under this key (the no-silence variant 'ns')."""
    L = max(t["T"] for t in tests) // 10
    S, C, Nf = np.zeros(L), np.zeros(L), np.zeros(L)
    for t in tests:
        r = t[sub] if sub else t
        T = t["T"] // 10
        m = np.zeros(T)
        for a, b in r["sig"]:
            m[a // 10:(b + 9) // 10] = 1
        S[:T] += m
        C[:T] += 1
        nz = r["noise"] if sub else r["noise"][noise_index]
        Nf[:min(T, len(nz))] += nz[:T]
    with np.errstate(invalid="ignore", divide="ignore"):
        return dict(running=S / C, all=S / len(tests), noise_running=Nf / C,
                    noise_all=Nf / len(tests), n=C)


def late_fraction(p: np.ndarray, noise: np.ndarray, t1: float = 1.0, tmax: float = 6.0):
    """Figure 3A legend: cumulative probability of the proportion curve less
    the noise floor, normalised at its peak; returns (1 - value at t1, peak
    time). Curves on a 1-ms grid."""
    k = int(tmax * 1000)
    cum = np.nancumsum((p - noise)[:k]) / 1000
    pk = int(np.nanargmax(cum))
    return float(1 - cum[int(t1 * 1000)] / cum[pk]), pk / 1000


def power_curves(tests: list[dict], sub: str | None = None):
    """Population Q(t) (Eq. 20) and the predictability ratio (Eq. 43) with
    the denominator smoothed over [0, 2t], and Eq. 43 unsmoothed, under the
    'running' reading (probes still running at t) and the 'all' reading."""
    get = (lambda t: t[sub]) if sub else (lambda t: t)
    pr, pa, n = pop_average([get(t)["pred"] for t in tests])
    ir, ia, _ = pop_average([get(t)["inv"] for t in tests])
    out = {}
    for name, p, i in (("running", pr, ir), ("all", pa, ia)):
        den = smooth_0_2t(p)
        out[name] = dict(pred=p, inv=i, den=den, Q=(p - i) / den, U=i / den, U_raw=i / p)
    out["n"] = n
    return out


def alignment_check(path: str, kind: str, seed: int, jitter=(0.5, 1.5)) -> dict:
    """Clock check: the trial tables' onsets against the trace. For each
    probe and context, the mean trial-to-trial correlation over the first
    second of the probe (current clamp), or the spike count in the first
    100 ms against the next 900 ms (cell-attached), at the true onsets and
    with each trial's onset moved by an independent random 0.5 to 1.5 s."""
    rng = np.random.default_rng(seed)
    d = load(path)
    raw = d.pop("trace")
    x = median_clip(raw) if kind == "cc" else raw
    pk = extract_spikes(raw) if kind == "ca" else None
    P = pairs(d, silence=True)
    res = {"true": [], "jitter": []}
    for probe, pl in sorted(P.items()):
        by = {}
        for c, on, _ in pl:
            by.setdefault(c, []).append(on)
        for c, ons in by.items():
            ons = np.array(ons)
            for key, o in (("true", ons),
                           ("jitter", ons + (rng.uniform(*jitter, len(ons)) * SF).astype(int))):
                if kind == "cc":
                    if len(o) < 2:
                        continue
                    Y = np.stack([x[a:a + SF] for a in o]).astype(np.float64)
                    C = np.corrcoef(Y)
                    res[key].append(C[np.triu_indices(len(o), 1)].mean())
                else:
                    first = sum(((pk > a) & (pk <= a + SF // 10)).sum() for a in o)
                    rest = sum(((pk > a + SF // 10) & (pk <= a + SF)).sum() for a in o)
                    res[key].append((first / 0.1 - rest / 0.9) / len(o))
    return {k: float(np.mean(v)) for k, v in res.items()} | {"n": len(res["true"])}
