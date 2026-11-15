"""Loading and context-dependence measures for CRCNS ac-1 (Asari and Zador 2009).

The data set is read from the public S3 bucket of CRCNS by range requests into
its zip files (docs/archives.md, "CRCNS"); nothing is written to disk.

Where each parameter comes from:

- Probe and context construction, the "silence" context (last 4 s of the
  intersequence interval) and the "silence probe" (first 2.5 s after a
  sequence), the rule that a probe needs at least two distinct contexts, the
  truncation of every context to the smallest number of trials, the
  Kruskal-Wallis significance with P < 0.01 for at least 5 ms, the noise
  floor from 1000 trial shuffles, the fractional power estimates (Eqs. 17 to
  19, each trial centred over the probe period) and the PSTH of the MGB units
  (100-ms bins from probe onset, SD over contexts with n - 1) are ported from
  the authors' analysis code deposited in the data set
  (asari/Tools/CxtDep.m, GetEvoked.m, ViewResp.m in crcns-ac1.zip), and agree
  with the paper's Methods (Analysis; Eqs. 10, 17 to 19, 42).
- The 10-ms median filter that clips spikes: Methods, Analysis, paragraph 2,
  and CxtDep.m (param.smooth = 10).
- MGB spike extraction: the high-pass FIR filter, the automatic threshold
  (two thirds of the largest filtered deflection) and the removal of
  downward artefacts are ported from GetSpikes.m (automatic mode, which
  ViewResp.m uses for cell-attached recordings); the Methods (Analysis,
  paragraph 3) say only "high-pass filter and thresholding".
- Time resolution: the paper works at 0.1 ms. Here the median-filtered
  membrane potential is evaluated every 1 ms (the median over the 10-ms
  window centred on each 1-ms point) and a significant period needs at least
  5 consecutive 1-ms points (5 ms). This is a standard choice to keep the
  1000-shuffle noise floor within the time limit; after a 10-ms median filter
  the trace changes little within 1 ms. The notebook compares the two
  resolutions on a subset of probes.
- The sets of conditioning stimuli in which one property varies (Figure 8, Table 1) are named
  in the files only for six recordings; `property_sets` rebuilds them from the stimulus
  descriptions, names and parameters, an assumption stated in the notebook.
- Ranks for the Kruskal-Wallis test use average ranks for ties (the code uses
  ordinal ranks); a standard choice that cannot change a result beyond ties.
"""
from __future__ import annotations

import functools
import io
import re
import zipfile
from dataclasses import dataclass, field

import fsspec
import numpy as np
import scipy.io as sio
from scipy import ndimage, optimize, signal, stats

DATASET = "crcns:ac-1/unversioned"   # CRCNS data sets are not versioned (docs/archives.md)
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/"
ZIPS = ["crcns-ac1.zip", "crcns-ac1-asari-results-1.zip", "crcns-ac1-asari-results-2.zip"]
SF = 10000          # recording sampling rate (Hz), checked against every file
DEC = 10            # 10 kHz -> 1 kHz for the subthreshold analysis (see docstring)
FS = SF // DEC      # analysis rate (Hz)
MEDWIN = 100        # 10-ms median filter at 10 kHz (Methods; CxtDep.m)
BLANK_PROBE = 2.5   # s, silence probe (CxtDep.m)
BLANK_CONTEXT = 4.0 # s, silence context (CxtDep.m)
ALPHA = 0.01        # Methods, Significance measure
MIN_RUN = 5         # 1-ms points = 5 ms (Methods: P < 0.01 for >= 5 ms)
NSHUFFLE = 1000     # Methods: 1000 resamplings per probe

# High-pass FIR filter of GetSpikes.m (ExtractSpikes)
HP_NUM = np.array([-2.9419, -7.7633, -16.2976, -28.7498, -44.7001, -62.8034, -80.9099, -96.4457,
                   -106.9520, 889.3317, -106.9520, -96.4457, -80.9099, -62.8034, -44.7001, -28.7498,
                   -16.2976, -7.7633, -2.9419]) / 1000


# ----------------------------------------------------------------------------- archive access
@functools.lru_cache(maxsize=None)
def open_zip(name: str) -> zipfile.ZipFile:
    return zipfile.ZipFile(fsspec.open(BASE + name, block_size=2**22).open())


def checksums() -> dict:
    with fsspec.open(BASE + "checksums.md5", "rt") as f:
        return {ln.split()[1]: ln.split()[0] for ln in f if ln.strip()}


def bucket_listing() -> list:
    import urllib.request
    xml = urllib.request.urlopen(BASE.replace("ac-1/", "") + "?list-type=2&prefix=ac-1/").read().decode()
    return re.findall(r"<Key>(.*?)</Key>.*?<Size>(\d+)</Size>", xml)


@functools.lru_cache(maxsize=None)
def member_index() -> dict:
    """Map 'Results/<cell>/<file>.mat' (as Summary.mat names files) to (zip, member)."""
    idx = {}
    for zn in ZIPS[1:]:
        for n in open_zip(zn).namelist():
            if n.endswith(".mat"):
                idx["Results/" + n.split("/", 1)[1]] = (zn, n)
    return idx


def loadmat_member(zn: str, member: str) -> dict:
    return sio.loadmat(io.BytesIO(open_zip(zn).read(member)), squeeze_me=True, struct_as_record=False)


def _txt(x) -> str:
    if isinstance(x, str):
        return x.strip()
    return " ".join(str(s).strip() for s in np.atleast_1d(x))


def summary(who: str = "asari") -> list:
    """Experiment groups of <who>/Summary.mat: description and cells with their files."""
    m = loadmat_member("crcns-ac1.zip", f"{who}/Summary.mat")
    out = []
    for e in np.atleast_1d(m["experiment"]):
        cells = []
        for c in np.atleast_1d(e.cell):
            files = [str(f) for f in np.atleast_1d(c.file)]
            descs = [_txt(d) for d in np.atleast_1d(c.description)] if not isinstance(c.description, str) else [c.description]
            cells.append(dict(cell=files[0].split("/")[1], files=files, descriptions=descs))
        out.append(dict(description=_txt(e.description), reference=_txt(getattr(e, "reference", "")), cells=cells))
    return out


# ----------------------------------------------------------------------------- one recording
@dataclass
class Recording:
    path: str
    cell: str
    rec_type: str
    description: str
    sf: int
    unit: str
    n_samples: int
    triggers: list                      # (type, onset sample, duration samples, description)
    notes: list
    stimuli: list                       # stimulus structs (name, description, file, param)
    durations: np.ndarray               # fragment durations in samples (CxtDep: round(ms/1000*sf))
    rep: int | None                     # 'Effective repeats' in the notes
    vm: np.ndarray | None = None        # median filtered, 1 kHz (mV)
    raw: np.ndarray | None = None       # raw 10 kHz (mV), kept only when asked
    meta: dict = field(default_factory=dict)


def _medfilt_decimated(x: np.ndarray) -> np.ndarray:
    """Median over the 10-ms window centred on every 10th sample (1 kHz output)."""
    h = MEDWIN // 2
    xp = np.concatenate([np.full(h, x[0]), x, np.full(h, x[-1])])
    win = np.lib.stride_tricks.sliding_window_view(xp, MEDWIN)[::DEC]
    out = np.empty(win.shape[0], dtype=np.float32)
    for k in range(0, win.shape[0], 200_000):
        out[k:k + 200_000] = np.median(win[k:k + 200_000], axis=1)
    return out[: (len(x) + DEC - 1) // DEC]


def load_recording(path: str, keep_raw: bool = False, filtered: bool = True) -> Recording:
    zn, member = member_index()[path]
    m = loadmat_member(zn, member)
    r, p = m["response"], m["param"]
    x = r.trace.astype(np.float64) * float(r.scale)
    trig = []
    for t in np.atleast_1d(m["triggers"]):
        dur = getattr(t.param, "duration", 0)
        trig.append((str(t.type), int(t.time), int(round(float(dur) / 1000 * r.sf)) if np.size(dur) == 1 else 0,
                     _txt(getattr(t.param, "description", ""))))
    notes = [str(s).rstrip() for s in np.atleast_1d(getattr(p, "notes", []))]
    rep = None
    for ln in notes:
        if "Effective repeats:" in ln:
            rep = int(ln.split(":")[1])
    stim = list(np.atleast_1d(getattr(p, "stimulus", [])))
    durs = np.array([int(round(float(s.param.duration) / 1000 * r.sf)) for s in stim]) if stim else np.array([], int)
    rec = Recording(path=path, cell=path.split("/")[1], rec_type=str(p.recording.type), description=_txt(p.ID.description),
                    sf=int(r.sf), unit=str(r.unit), n_samples=len(x), triggers=trig, notes=notes, stimuli=stim,
                    durations=durs, rep=rep)
    rec.meta = dict(age=str(getattr(p.animal, "age", "")), animal=str(p.ID.animal), date=str(p.ID.date),
                    Rs=str(getattr(p.recording, "Rs", "")), depth=str(getattr(p.recording, "depth", "")),
                    vmin=float(x.min()), vmax=float(x.max()), vmedian=float(np.median(x[::100])))
    if filtered:
        rec.vm = _medfilt_decimated(x)
    if keep_raw:
        rec.raw = x
    return rec


def sequence_segments(rec: Recording):
    """Port of GetEvoked.m: evoked (non-pulse triggers) and the silences between them.

    Returns a list of presentations in time order: dict(seq=tuple of fragments, on, off,
    pre=(start, end) of the silence before, post=(start, end) of the silence after),
    all in 10-kHz samples.
    """
    ev = [t for t in rec.triggers if "pulse" not in t[0]]
    out = []
    prev_end = 0
    for k, (typ, on, dur, desc) in enumerate(ev):
        nxt = ev[k + 1][1] if k + 1 < len(ev) else rec.n_samples
        off = min(on + dur, rec.n_samples)
        seq = None
        if ":" in desc and desc.lower().startswith("sequence"):
            seq = tuple(int(v) for v in desc.split(":", 1)[1].split())
        out.append(dict(type=typ, desc=desc, seq=seq, on=on, off=off, pre=(prev_end, on), post=(off, nxt)))
        prev_end = off
    return out


@dataclass
class Probe:
    cell: str
    path: str
    probe: int            # fragment index (1-based), or 0 for the silence probe
    contexts: list        # context fragment per group (0 = silence)
    traces: list          # per context: (n_trials, T) arrays at 1 kHz (median filtered)
    n_trials: list        # trials available per context before truncation
    duration: float       # s
    spikes: list | None = None   # per context: list of spike-time arrays (s, from probe onset)
    kind: str = ""

    @property
    def rep(self) -> int:
        return min(self.n_trials)


def build_probes(rec: Recording, include_silence_context: bool = True, include_silence_probe: bool = False,
                 spikes: np.ndarray | None = None) -> list:
    """Port of CxtDep.m: all probes with at least two distinct contexts.

    Trials of a context are pooled over the sequences where the pair occurs, the first
    `Effective repeats` presentations of every sequence are used, and every context is
    cut to the smallest number of trials (GetResp in CxtDep.m).
    """
    segs = [s for s in sequence_segments(rec) if s["seq"] is not None]
    if not segs:
        return []
    by_seq = {}
    for s in segs:
        by_seq.setdefault(s["seq"], []).append(s)
    if rec.rep:
        by_seq = {k: v[: rec.rep] for k, v in by_seq.items()}
    durs = rec.durations
    nfrag = len(durs)
    # length of the silence windows: the shortest available (CxtDep.m)
    bctx = min([BLANK_CONTEXT] + [(s["pre"][1] - s["pre"][0]) / SF for v in by_seq.values() for s in v])
    bprb = min([BLANK_PROBE] + [(s["post"][1] - s["post"][0]) / SF for v in by_seq.values() for s in v])
    occ = {}   # probe -> context -> list of (presentation, start sample of probe, length)
    for seq, pres in by_seq.items():
        if any(f < 1 or f > nfrag for f in seq):
            continue
        starts = np.concatenate([[0], np.cumsum([durs[f - 1] for f in seq])])
        ext = [0] + list(seq)
        for k, f in enumerate(seq):
            ctx = ext[k]
            if ctx == 0 and not include_silence_context:
                continue
            for s in pres:
                occ.setdefault(f, {}).setdefault(ctx, []).append((s["on"] + starts[k], durs[f - 1]))
        if include_silence_probe:
            for s in pres:
                occ.setdefault(0, {}).setdefault(seq[-1], []).append((s["off"], int(round(bprb * SF))))
    probes = []
    for f, ctxs in sorted(occ.items()):
        if len(ctxs) < 2:
            continue
        cl = sorted(ctxs)
        length = min(L for c in cl for _, L in ctxs[c])
        T = length // DEC
        traces, ntr, spk = [], [], []
        for c in cl:
            arr = []
            sp = []
            for st, _ in ctxs[c]:
                i0 = st // DEC
                seg = rec.vm[i0:i0 + T] if rec.vm is not None else None
                if seg is not None and len(seg) == T:
                    arr.append(seg)
                if spikes is not None:
                    sp.append((spikes[(spikes >= st) & (spikes < st + length)] - st) / SF)
            traces.append(np.array(arr) if arr else np.zeros((len(ctxs[c]), 0)))
            ntr.append(len(ctxs[c]))
            spk.append(sp)
        probes.append(Probe(cell=rec.cell, path=rec.path, probe=f, contexts=cl, traces=traces, n_trials=ntr,
                            duration=length / SF, spikes=spk if spikes is not None else None,
                            kind="silence" if f == 0 else "fragment"))
    return probes


# ----------------------------------------------------------------------------- significance
def _runs_mask(b: np.ndarray, min_run: int = MIN_RUN) -> np.ndarray:
    """Keep only runs of True at least min_run long (along the last axis)."""
    st = np.ones((1,) * (b.ndim - 1) + (min_run,), bool)
    return ndimage.binary_opening(b, structure=st)


def kw_significance(p: Probe, contexts_subset=None, nshuffle: int = NSHUFFLE, rng=None, t_max: float | None = None):
    """Kruskal-Wallis across contexts at each 1-ms point; significant runs; noise floor.

    Returns dict(p=p-values, sig=bool mask, noise=fraction of shuffles significant per point).
    """
    idx = range(len(p.contexts)) if contexts_subset is None else [p.contexts.index(c) for c in contexts_subset]
    rep = min(p.traces[i].shape[0] for i in idx)
    X = np.concatenate([p.traces[i][:rep] for i in idx], axis=0).astype(np.float64)
    if t_max is not None:
        X = X[:, : int(round(t_max * FS))]
    M = len(idx)
    N = X.shape[0]
    R = stats.rankdata(X, axis=0).astype(np.float32)
    grp = np.repeat(np.arange(M), rep)

    def kw_from(Rm):
        rbar = Rm.reshape(M, rep, -1).mean(axis=1)
        return 12 * ((rbar - (N + 1) / 2) ** 2).sum(axis=0) / (M * (N + 1))

    kw = kw_from(R)
    pval = stats.chi2.sf(kw, M - 1)
    sig = _runs_mask(pval < ALPHA)
    noise = None
    if nshuffle:
        rng = rng or np.random.default_rng(0)
        crit = stats.chi2.isf(ALPHA, M - 1)
        noise = np.zeros(X.shape[1])
        B = 50
        for b0 in range(0, nshuffle, B):
            nb = min(B, nshuffle - b0)
            G = np.zeros((nb * M, N), np.float32)
            for j in range(nb):
                perm = rng.permutation(N)
                G[j * M + grp[perm], np.arange(N)] = 1.0 / rep
            rbar = (G @ R).reshape(nb, M, -1)
            kws = 12 * ((rbar - (N + 1) / 2) ** 2).sum(axis=1) / (M * (N + 1))
            noise += _runs_mask(kws > crit).sum(axis=0)
        noise /= nshuffle
    return dict(p=pval, sig=sig, noise=noise, rep=rep, n_ctx=M)


# ----------------------------------------------------------------------------- fractional power
def frac_power(p: Probe, contexts_subset=None, t_max: float | None = None):
    """Port of FracPow (CxtDep.m): Eqs. 17 (predictable), 18 (invariant) per time point."""
    idx = range(len(p.contexts)) if contexts_subset is None else [p.contexts.index(c) for c in contexts_subset]
    rep = min(p.traces[i].shape[0] for i in idx)
    X = np.stack([p.traces[i][:rep] for i in idx]).astype(np.float64)   # (n, rep, T)
    if t_max is not None:
        X = X[:, :, : int(round(t_max * FS))]
    X = X - X.mean(axis=2, keepdims=True)          # each trial centred over the probe period
    n = X.shape[0]
    mk = X.mean(axis=1)                              # (n, T)
    pred = ((rep * mk ** 2 - (X ** 2).mean(axis=1)) / (rep - 1)).mean(axis=0)
    inv = (n * mk.mean(axis=0) ** 2 - (mk ** 2).mean(axis=0)) / (n - 1)
    return dict(pred=pred, inv=inv, dep=pred - inv, total=(X ** 2).mean(axis=(0, 1)))


def stack_curves(curves: list, T: int, fill=np.nan) -> np.ndarray:
    out = np.full((len(curves), T), fill, dtype=float)
    for i, c in enumerate(curves):
        L = min(len(c), T)
        out[i, :L] = c[:L]
    return out


def running_mean_0_2t(x: np.ndarray) -> np.ndarray:
    """Mean of x over [0, 2t] at each t (Methods, Eq. 20), truncated at the end of x."""
    c = np.concatenate([[0], np.nancumsum(x)])
    cnt = np.concatenate([[0], np.cumsum(~np.isnan(x))])
    t = np.arange(len(x))
    hi = np.minimum(2 * t + 1, len(x))
    return (c[hi] - c[0]) / np.maximum(cnt[hi], 1)


# ----------------------------------------------------------------------------- curve fits
def fit_exp(t, y, n_exp: int, kappa=None, starts=None):
    """Least-squares fit of Eq. 44, sum_k a_k exp(-t/tau_k) + kappa, over a grid of starts.

    kappa fixed when a number is given, free when None. Taus bounded to [1 ms, 100 s].
    """
    t = np.asarray(t, float)
    y = np.asarray(y, float)
    ok = np.isfinite(y)
    t, y = t[ok], y[ok]
    free_k = kappa is None

    def model(th):
        a = th[0:2 * n_exp:2]
        tau = th[1:2 * n_exp:2]
        k = th[-1] if free_k else kappa
        return (a[:, None] * np.exp(-t[None, :] / tau[:, None])).sum(axis=0) + k

    taus = [0.03, 0.1, 0.3, 1.0, 3.0]
    best = None
    grid = starts or ([(a, b) for a in taus for b in taus if b > a] if n_exp == 2 else [(a,) for a in taus])
    for g in grid:
        th0 = []
        for tau in g:
            th0 += [float(y[0] - (np.nanmean(y[-10:]) if free_k else kappa)) / n_exp, tau]
        lo = [-np.inf, 1e-3] * n_exp
        hi = [np.inf, 100.0] * n_exp
        if free_k:
            th0.append(float(np.nanmean(y[-10:])))
            lo.append(-np.inf)
            hi.append(np.inf)
        try:
            res = optimize.least_squares(lambda th: model(th) - y, th0, bounds=(lo, hi))
        except Exception:
            continue
        if best is None or res.cost < best.cost:
            best = res
    th = best.x
    comps = sorted([(th[2 * k], th[2 * k + 1]) for k in range(n_exp)], key=lambda z: z[1])
    return dict(alpha=[c[0] for c in comps], tau=[c[1] for c in comps], kappa=th[-1] if free_k else kappa,
                sse=2 * best.cost, n=len(t))


def fit_with_rule(t, y, kappa=None):
    """Two exponentials if each size is at least a tenth of the total (Methods, Eq. 44), else one."""
    f2 = fit_exp(t, y, 2, kappa)
    tot = sum(abs(a) for a in f2["alpha"])
    if all(abs(a) >= tot / 10 for a in f2["alpha"]):
        f2["n_exp"] = 2
        return f2, fit_exp(t, y, 1, kappa)
    f1 = fit_exp(t, y, 1, kappa)
    f1["n_exp"] = 1
    return f1, f2


# ----------------------------------------------------------------------------- stimulus properties (Fig. 8)
TABLE1_KINDS = ("natural", "TORC", "DMR", "MHT", "MCN")   # probe rows of Table 1


def _par(s, key):
    v = getattr(getattr(s, "param", None), key, None)
    if v is None:
        return None
    v = np.atleast_1d(v)
    return tuple(float(x) for x in np.round(v.astype(float), 6)) if v.dtype != object else None


def stim_kind(s) -> str:
    """Probe type of one stimulus struct (the rows of Table 1), from its name and description."""
    name, desc = str(getattr(s, "name", "")), _txt(getattr(s, "description", ""))
    if name == "silence":
        return "silence"
    if "TORC" in desc:
        return "TORC"
    if "DMR" in desc:
        return "DMR"
    if "Modulated Harmonic Tone" in desc:
        return "MHT"
    if name.startswith("pink noise"):
        return "MCN"
    if name.startswith("naturalistic"):
        return "naturalistic"
    if name.startswith("natural sound"):
        return "natural"
    return "other"


def property_sets(rec: Recording) -> list:
    """Sets of conditioning stimuli in which one property varies (Fig. 8, Table 1).

    The files do not name the sets except in the notes of the six recordings of a natural
    probe after MHT variants; the sets are rebuilt from the stimulus descriptions, names and
    parameters (an assumption, stated in the notebook). Each set is dict(prop, label,
    members = 1-based stimulus indices, main = whether it enters the main reading):

    - TORC and DMR ensembles whose descriptions say "amplitude variants" or "bandwidth
      variants" (TORC), "DMR; amplitude variants" or "DMR1..4: bandwidth" (DMR): one set of
      all their stimuli, amplitude or frequency (Table 1 legend: TORCs and DMRs for
      amplitude and frequency). In designs with forward and time-reversed variants (names
      "(forward)" and "(backward)"), each direction is a set; the forward one is the main.
    - Natural sound at several attenuations ("attenuation" parameter) or band shifts ("df"
      with "FF"), forward and backward: amplitude or frequency sets as above.
    - Naturalistic sets (SoundTrans.m): the original and its "amplitude variant" (amplitude),
      the original and its "frequency variant" 1 and 2 (frequency).
    - MHT designs with a natural probe and the notes listing the sets: the sets of the notes.
    - MHT 4 by 4 designs of AM rate range by FM rate range: an AM set for each FM range and an
      FM set for each AM range; the main reading keeps the set through the first stimulus
      (both ranges empty), so that each probe enters a property once, as Table 1 counts.
    - MHT designs varying AM rate and depth only: one AM set.
    - Pink noise (MCN): for each natural fragment k, the fragment and its pink noises
      ("pink noise fragment k" or "k-j"): higher-order (Table 1 legend, "comparing natural
      sounds and corresponding modulated colored noise"). A probe can meet several of these
      sets; the notebook's main reading keeps the one that holds the probe itself.
    """
    st = rec.stimuli
    n = len(st)
    idx = range(1, n + 1)
    names = [str(getattr(s, "name", "")) for s in st]
    descs = [_txt(getattr(s, "description", "")) for s in st]
    kinds = [stim_kind(s) for s in st]
    out = []

    def add(prop, label, members, main=True):
        members = sorted(members)
        if len(members) >= 2:
            out.append(dict(prop=prop, label=label, members=members, main=main))

    # sets written in the notes ("2-5,8: amplitude variants")
    notes = "\n".join(rec.notes)
    noted = re.findall(r"^\s*([\d,\- ]+):\s*(amplitude|frequency|amplitude-modulation|frequency-modulation) variants", notes, re.M)
    if noted:
        names_p = {"amplitude": "amplitude", "frequency": "frequency", "amplitude-modulation": "AM", "frequency-modulation": "FM"}
        for spec, prop in noted:
            mem = set()
            for part in spec.replace(" ", "").split(","):
                a, _, b = part.partition("-")
                mem |= set(range(int(a), int(b or a) + 1))
            add(names_p[prop], "notes", mem)
        return out
    for kind in ("TORC", "DMR"):
        ii = [i for i in idx if kinds[i - 1] == kind]
        if not ii:
            continue
        d = " ".join(descs[i - 1] for i in ii)
        prop = "amplitude" if "amplitude variants" in d else "frequency" if ("bandwidth" in d or "frequency variants" in d) else None
        if prop is None:
            continue
        fw = [i for i in ii if "(backward)" not in names[i - 1]]
        bw = [i for i in ii if "(backward)" in names[i - 1]]
        add(prop, f"{kind} forward", fw)
        add(prop, f"{kind} backward", bw, main=False)
    # one natural sound at several attenuations or band shifts
    nat = [i for i in idx if kinds[i - 1] == "natural"]
    if len(nat) > 2 and len({descs[i - 1] for i in nat}) == 1:
        for direction in ("(forward)", "(backward)"):
            ii = [i for i in nat if direction in names[i - 1]]
            att = [i for i in ii if _par(st[i - 1], "attenuation") is not None]
            shift = [i for i in ii if _par(st[i - 1], "df") is not None and _par(st[i - 1], "FF") is not None]
            add("amplitude", f"natural {direction}", att, main=direction == "(forward)")
            add("frequency", f"natural {direction}", shift, main=direction == "(forward)")
    # naturalistic variants (SoundTrans.m)
    orig = [i for i in idx if names[i - 1] == "natural sound fragment"]
    if orig and any(kinds[i - 1] == "naturalistic" for i in idx):
        add("amplitude", "naturalistic", orig + [i for i in idx if descs[i - 1] == "amplitude variant"])
        add("frequency", "naturalistic", orig + [i for i in idx if descs[i - 1].startswith("frequency variant")])
    # MHT designs
    mht = [i for i in idx if kinds[i - 1] == "MHT"]
    if mht:
        am = {i: _par(st[i - 1], "AMrange") for i in mht}
        fm = {i: _par(st[i - 1], "FMrange") for i in mht}
        if all(v is not None for v in fm.values()) and len(set(fm.values())) > 1:
            first = mht[0]
            rng = lambda r: "-".join(f"{v:g}" for v in r) + " Hz" if r else "none"
            for f in sorted(set(fm.values())):
                add("AM", f"FM range {rng(f)}", [i for i in mht if fm[i] == f], main=f == fm[first])
            for a in sorted(set(am.values())):
                add("FM", f"AM range {rng(a)}", [i for i in mht if am[i] == a], main=a == am[first])
        else:
            add("AM", "AM rate and depth", mht)
    # natural sounds and their pink noises (MCN)
    for i in idx:
        m = re.match(r"natural sound fragment (\d+)$", names[i - 1])
        if m:
            k = m.group(1)
            pinks = [j for j in idx if re.match(rf"pink noise fragment {k}(-\d+)?$", names[j - 1])]
            add("higher-order", f"natural {k} and its pink noise", [i] + pinks)
    return out


# ----------------------------------------------------------------------------- spikes
def extract_spikes(raw: np.ndarray, threshold: float | None = None, remove_downward: bool = True,
                   info: dict | None = None) -> np.ndarray:
    """Port of ExtractSpikes in GetSpikes.m (automatic mode). Returns spike sample indices.

    The automatic threshold is computed once over the whole trace passed in: ViewResp.m calls
    GetSpikes(response, auto) with the whole recording, and GetSpikes.m (auto == 1) calls
    ExtractSpikes(response, threshold, remove_downward_spikes) on all of it; only the manual
    mode works in 10-s sweeps. When `info` is a dict, the threshold used and a robust SD of
    the filtered trace (median absolute value / 0.6745) are written into it, with the heights,
    in those SDs, of every local maximum above 10 SDs (at least 2 ms apart).
    """
    f = signal.filtfilt(HP_NUM, [1.0], raw)
    if info is not None:
        sd = float(np.median(np.abs(f)) / 0.6745)
        info["noise_sd"] = sd
        info["peak_sd"] = (signal.find_peaks(f, height=10 * sd, distance=20)[1]["peak_heights"] / sd).astype(np.float32)
    if threshold is None:
        i = int(np.argmax(np.abs(f)))
        threshold = 2 / 3 * abs(f[i])
        if threshold > 100:
            mask = np.ones(len(f), bool)
            mask[max(0, i - 30): i + 31] = False
            threshold = np.abs(f[mask]).max() * 2 / 3
    if info is not None:
        info["threshold"] = float(threshold)
    above = f > threshold
    if not above.any():
        return np.array([], int)
    lab, n = ndimage.label(above)
    peaks = np.array(ndimage.maximum_position(f, lab, np.arange(1, n + 1))).ravel().astype(int)
    if remove_downward and len(peaks):
        h = f[peaks]
        mins = np.array([f[max(0, k - 10): k + 11].min() for k in peaks])
        peaks = peaks[~(mins < -h)]
    return peaks


def psth_sd(p: Probe, dt: float = 0.1, nbins: int = 61):
    """Port of psth() in CxtDep.m: PSTH per context (bins from probe onset), SD over contexts."""
    rep = min(len(s) for s in p.spikes)
    edges = np.arange(nbins + 1) * dt
    T = int(np.floor(p.duration / dt + 1e-9)) + 1    # histc bins t = 0:dt:Tend
    H = []
    for sp in p.spikes:
        allsp = np.concatenate(sp[:rep]) if rep else np.array([])
        allsp = allsp[(allsp > 0) & (allsp <= p.duration)]
        h, _ = np.histogram(allsp, bins=edges)
        H.append(h / rep / dt)
    H = np.array(H)[:, :min(T, nbins)]
    return dict(psth=H, sd=H.std(axis=0, ddof=1), rep=rep)


# ----------------------------------------------------------------------------- A1 spikes, rates, checks
def a1_spikes(rec: Recording, height: float) -> np.ndarray:
    """Spikes of a whole-cell trace: peaks of the raw trace minus its 10-ms median filter.

    The paper detected A1 spikes by hand (GetSpikes.m, manual mode, which the code says
    is needed for intracellular data). Here a spike is a peak at least `height` mV above
    the median-filtered membrane potential, at least 2 ms after the previous one; the
    heights used (10, 15, 20 mV) are readings, an assumption stated in the notebook.
    """
    base = np.repeat(rec.vm, DEC)[: rec.n_samples]
    pk, _ = signal.find_peaks(rec.raw - base, height=height, distance=20)
    return pk


def window_rates(rec: Recording, spikes: np.ndarray, pre_baseline: float = 1.0, pulse_skip: float = 0.5) -> dict:
    """Spike counts and durations in the stimulus periods and in the silences.

    Stimulus periods are the non-pulse triggers (GetEvoked.m). Silences are the gaps
    between them, less `pulse_skip` s after each test pulse; the pre-stimulus baseline
    is the last `pre_baseline` s before each stimulus.
    """
    ev = [t for t in rec.triggers if "pulse" not in t[0]]
    pulses = [t[1] for t in rec.triggers if "pulse" in t[0]]
    mask_sp = np.zeros(rec.n_samples, bool)
    mask_ev = np.zeros(rec.n_samples, bool)
    mask_pre = np.zeros(rec.n_samples, bool)
    prev = 0
    for typ, on, dur, _ in ev:
        mask_sp[prev:on] = True
        mask_pre[max(prev, on - int(pre_baseline * SF)):on] = True
        mask_ev[on:on + dur] = True
        prev = on + dur
    mask_sp[prev:] = True
    for p in pulses:
        a, b = p, p + int(pulse_skip * SF)
        mask_sp[a:b] = False
        mask_pre[a:b] = False
    mask_sp &= ~mask_ev
    mask_pre &= ~mask_ev
    sp = np.zeros(rec.n_samples, bool)
    sp[spikes[spikes < rec.n_samples]] = True
    return dict(n_ev=int(sp[mask_ev].sum()), t_ev=mask_ev.sum() / SF, n_sp=int(sp[mask_sp].sum()), t_sp=mask_sp.sum() / SF,
                n_pre=int(sp[mask_pre].sum()), t_pre=mask_pre.sum() / SF)


def onset_contrast(rec: Recording, win: float = 1.0) -> dict:
    """Clock check: across-trial predictable power (Eq. 52) of the membrane potential in
    the `win` s after each sequence onset and in the `win` s before it, per sequence."""
    segs = [s for s in sequence_segments(rec) if s["seq"] is not None]
    by = {}
    for s in segs:
        by.setdefault(s["seq"], []).append(s["on"] // DEC)
    W = int(win * FS)
    post, pre = [], []
    for ons in by.values():
        ons = [o for o in ons if o - W >= 0 and o + W <= len(rec.vm)]
        if len(ons) < 2:
            continue
        for sign, out in ((1, post), (-1, pre)):
            X = np.array([rec.vm[o:o + W] if sign > 0 else rec.vm[o - W:o] for o in ons], float)
            X -= X.mean(axis=1, keepdims=True)
            m = len(ons)
            out.append(((m * X.mean(0) ** 2 - (X ** 2).mean(0)) / (m - 1)).mean())
    return dict(post=float(np.mean(post)) if post else np.nan, pre=float(np.mean(pre)) if pre else np.nan)


def spont_autocorr(rec: Recording, max_lag: float = 0.5, skip: float = 0.0) -> np.ndarray | None:
    """Mean normalized autocorrelation (Eq. 45) of the silences between sequences (1 kHz,
    median filtered, each segment centred), skipping `skip` s after each sequence end and
    0.5 s after each test pulse."""
    segs = [s for s in sequence_segments(rec) if s["seq"] is not None]
    pulses = np.array([t[1] for t in rec.triggers if "pulse" in t[0]])
    L = int(max_lag * FS)
    acs = []
    for s in segs:
        a, b = s["post"][0] + int(skip * SF), s["post"][1]
        if len(pulses):
            inside = pulses[(pulses >= a) & (pulses < b)]
            if len(inside):
                b = int(inside.min())          # stop at the first test pulse
        x = rec.vm[a // DEC: b // DEC].astype(float)
        if len(x) < 2 * L:
            continue
        x = x - x.mean()
        ac = signal.correlate(x, x, mode="full", method="fft")[len(x) - 1: len(x) - 1 + L + 1]
        ac = ac / np.arange(len(x), len(x) - L - 1, -1)
        acs.append(ac / ac[0])
    return np.mean(acs, axis=0) if acs else None


def noise_autocorr(p: Probe, max_lag: float = 0.5) -> np.ndarray:
    """Mean normalized autocorrelation of the trial residuals (Eqs. 14 and 45) of a probe."""
    L = int(max_lag * FS)
    acs = []
    for X in p.traces:
        if X.shape[0] < 2:
            continue
        E = X - X.mean(axis=0, keepdims=True)
        for e in E:
            e = e - e.mean()
            if len(e) < 2 * L or not np.any(e):
                continue
            ac = signal.correlate(e, e, mode="full", method="fft")[len(e) - 1: len(e) - 1 + L + 1]
            ac = ac / np.arange(len(e), len(e) - L - 1, -1)
            acs.append(ac / ac[0])
    return np.mean(acs, axis=0)


def trial_correlations(X: np.ndarray) -> tuple:
    """Trial-to-trial reliability of one context: (mean pairwise r, mean r of each trial with
    the mean of the others)."""
    C = np.corrcoef(X)
    iu = np.triu_indices(len(X), 1)
    loo = [np.corrcoef(X[i], np.delete(X, i, 0).mean(0))[0, 1] for i in range(len(X))]
    return float(np.nanmean(C[iu])), float(np.nanmean(loo))


def first_cross(t: np.ndarray, y: np.ndarray, level: float) -> float:
    i = np.where(y < level)[0]
    return float(t[i[0]]) if len(i) else np.nan


def stim_bands(s) -> list:
    """Frequency band edges (Hz) of a stimulus: its `ff` parameter and, for TORC sequences,
    the `ff` of each TORC in `torc_parameters`."""
    out = []
    ff = _par(s, "ff")
    if ff:
        out.append(ff)
    tp = getattr(getattr(s, "param", None), "torc_parameters", None)
    if tp is not None:
        for q in np.atleast_1d(tp):
            v = getattr(q, "ff", None)
            if v is not None:
                out.append(tuple(float(x) for x in np.atleast_1d(v)))
    return out
