"""Loading and context-dependence measures for CRCNS ac-1 (Asari & Zador 2009).

Asari H, Zador AM (2009) Long-lasting context dependence constrains neural encoding models in
rodent auditory cortex. J Neurophysiol 102:2638-2656, doi:10.1152/jn.00577.2009.

The data set (doi:10.6080/K0KW5CXR) is read in place from the public S3 bucket `crcnsarchive`
(three zip files, opened over range requests with fsspec and zipfile; nothing is written to
disk). CRCNS data sets are not versioned; the MD5 sums of the zip files read are in `MD5`.

Asari's MATLAB files hold one recording each: `response` (int16 trace, `scale` to mV, 10 kHz),
`triggers` (one per stimulus sequence: onset in samples, duration in ms and a description
"Sequence k: a b c d e" naming the fragments in order) and `param` (stimulus fragments with
their durations in ms, recording type, and `notes` with the sequence table and "Effective
repeats"). `asari/Summary.mat` groups the recordings into experiments (A1 natural sounds, MGB
natural sounds, A1 synthetic sounds, unpublished).

Where the parameters come from:

- The data set ships the authors' analysis code, `asari/Tools/CxtDep.m` ("Basic analysis
  script for Asari and Zador (2008)") with `ViewResp.m`, `GetEvoked.m` and `GetSpikes.m`.
  The paper links no code; this code is the authors' and settles details the Methods leave
  open. It is followed here, and each such detail cites it:
  * context-probe alignment: the probe window is the fragment's stated duration; a fragment at
    the start of a sequence has "silence" as context (CxtDep.m, `blank(2) = 4` s of the
    preceding intersequence interval, "include blank as context"); trials of one context that
    occur at several places are pooled, and every context is cut to the smallest number of
    trials (`GetResp`); a probe needs at least two different contexts;
  * the intersequence silence as a probe (`blank(1) = 2.5` s, "include blank as probe"), which
    the paper leaves out of Figure 3 (Methods, Stimulus design) and which is used only for
    claim figs1-silence-probe;
  * Kruskal-Wallis on ordinal ranks without a tie correction, significant runs of P < 0.01
    lasting at least 5 ms (`k(end) - k(start) >= 50` samples), and the noise floor from 1000
    permutations of the trials (`KWtest`);
  * the power measures (`FracPow`): each trial is centred on its mean over the probe window,
    total, predictable (Eq. 17) and context-invariant (Eq. 18) power per time point;
  * PSTHs in 0.1-s bins from `t = 0:0.1:Tend` with MATLAB `histc` edges, SD over contexts with
    n - 1 (`psth`);
  * spike detection for cell-attached data (`GetSpikes.m`, automatic mode: equiripple FIR
    high-pass applied forward and backward, threshold at 2/3 of the largest absolute filtered
    value, one spike per suprathreshold segment at its peak, downward-noise spikes removed).
- The 10-ms median filter that clips spikes (Methods, Analysis, paragraph 1; CxtDep.m default
  `param.smooth = 10`) is applied to the whole trace, as `GetEvoked.m` does.
- The inclusion rule (at least 4 trials per context in current clamp, at least 10 in MGB) is the
  Methods' (Context dependence at subthreshold voltage level; at suprathreshold level) and the
  claim methods-recording-counts.
- A1 spikes (claim a1-mgb-firing-rates) are not detected by the authors' code (manual
  extraction in whole-cell mode); a standard choice is used here: upward crossings of a
  threshold on the raw membrane potential (-20 mV, with -10 and -30 mV shown), with a 2-ms dead
  time. It is an assumption stated in the claim.
"""

from __future__ import annotations

import io
import re
import zipfile
from functools import lru_cache

import fsspec
import numpy as np
import scipy.io as sio
from scipy import ndimage, signal, stats

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/"
ZIPS = ["crcns-ac1.zip", "crcns-ac1-asari-results-1.zip", "crcns-ac1-asari-results-2.zip"]
MD5 = {"crcns-ac1-asari-results-1.zip": "18537da81d98e311c0274f62aea04daa",
       "crcns-ac1-asari-results-2.zip": "2f7ab955cc778fc6839ce59ed51bce89",
       "crcns-ac1.zip": "2300ee76d93383ab8c808ddf16761a23"}
DATASET_DOI = "10.6080/K0KW5CXR"
DATASET_ID = "ac-1"             # CRCNS data set
DATASET_VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md); see MD5

SF = 10000                  # Hz, response.sf in every file read (checked in the notebook)
MEDIAN_MS = 10              # Methods, Analysis; CxtDep.m param.smooth
ALPHA = 0.01                # Methods, significance measure; CxtDep.m KWtest
ALPHA_DT = 50               # samples (5 ms at 10 kHz); KWtest dt
N_SHUFFLE = 1000            # Methods; KWtest bootstrap
BLANK_CONTEXT_S = 4.0       # CxtDep.m blank(2)
BLANK_PROBE_S = 2.5         # CxtDep.m blank(1)
MIN_TRIALS_CC = 4           # Methods, at least four repeats
MIN_TRIALS_MGB = 10         # Methods, at least 10 repeats
PSTH_DT = 0.1               # s, Methods, suprathreshold level; CxtDep.m psth
A1_THRESHOLDS = (-20.0, -10.0, -30.0)   # mV, A1 spike detection (assumption; first is the main one)

# GetSpikes.m ExtractSpikes: high-pass FIR coefficients, applied with filtfilt
_HP = np.array([-2.9419, -7.7633, -16.2976, -28.7498, -44.7001, -62.8034, -80.9099, -96.4457,
                -106.9520, 889.3317, -106.9520, -96.4457, -80.9099, -62.8034, -44.7001,
                -28.7498, -16.2976, -7.7633, -2.9419]) / 1000


# ----------------------------------------------------------------------------------- reading
class Archive:
    """The three zip files of ac-1, each opened once over HTTP range requests."""

    def __init__(self):
        self._files, self._zips = {}, {}
        for name in ZIPS:
            fh = fsspec.open(BUCKET + name, block_size=2 ** 22).open()
            self._files[name] = fh
            self._zips[name] = zipfile.ZipFile(fh)
        self.members = {}
        for name, z in self._zips.items():
            for info in z.infolist():
                self.members[info.filename] = (name, info)

    def read(self, member: str) -> bytes:
        name, _ = self.members[member]
        return self._zips[name].read(member)

    def loadmat(self, member: str):
        return sio.loadmat(io.BytesIO(self.read(member)), squeeze_me=True, struct_as_record=False)

    def result_member(self, path: str) -> str:
        """Summary.mat path 'Results/<dir>/<file>.mat' to the member in a results zip."""
        rel = path.split("Results/", 1)[1]
        for prefix in ("asari-results-1/", "asari-results-2/"):
            if prefix + rel in self.members:
                return prefix + rel
        raise KeyError(path)


def summary(archive: Archive) -> list[dict]:
    """One row per (experiment, cell, file) of asari/Summary.mat."""
    m = archive.loadmat("asari/Summary.mat")
    rows = []
    for ei, e in enumerate(np.atleast_1d(m["experiment"])):
        for ci, c in enumerate(np.atleast_1d(e.cell)):
            files = np.atleast_1d(c.file)
            descs = np.atleast_1d(c.description)
            for k, (f, d) in enumerate(zip(files, descs)):
                rows.append(dict(experiment=ei, experiment_description=str(e.description).strip(),
                                 reference=str(e.reference).strip(), cell_index=ci,
                                 cell=str(f).split("/")[1], file=str(f), description=str(d).strip()))
    return rows


def _notes(param) -> list[str]:
    notes = np.atleast_1d(param.notes)
    return [str(x) for x in notes]


MAX_MISMATCH_MS = 5.0       # tolerance between summed fragment durations and a trigger's duration


def _stimuli(param) -> list[dict]:
    return [dict(name=str(getattr(s, "name", "")), description=str(getattr(s, "description", "")),
                 file=str(getattr(s, "file", "")), duration_ms=float(s.param.duration), param=s.param)
            for s in np.atleast_1d(param.stimulus)]


def _duration_mismatch(trig: list[dict], stims: list[dict]) -> float:
    """Largest |sum of fragment durations - trigger duration| over the sequence triggers (ms)."""
    out = 0.0
    for t in trig:
        if t["seq"] is None:
            continue
        if max(t["seq"]) > len(stims):
            return np.inf
        out = max(out, abs(sum(stims[f - 1]["duration_ms"] for f in t["seq"]) - t["duration_ms"]))
    return out


def effective_repeats(param) -> int | None:
    for line in _notes(param):
        j = line.find("Effective repeats:")
        if j >= 0:
            return int(line[j + 18:].split()[0])
    return None


def load_recording(archive: Archive, member: str, smooth: bool = True, keep_raw: bool = False) -> dict:
    """Trace in mV (median-filtered when `smooth`), the sequence triggers and the fragments."""
    m = archive.loadmat(member)
    resp, param = m["response"], m["param"]
    raw = resp.trace.astype(np.float64) * float(resp.scale)
    trace = raw
    if smooth:
        r = raw.mean()
        trace = ndimage.median_filter(raw - r, size=int(round(MEDIAN_MS / 1000 * resp.sf)),
                                      mode="constant", cval=0.0) + r
    trig = []
    for t in np.atleast_1d(m["triggers"]):
        desc = str(getattr(t.param, "description", ""))
        seq = None
        mm = re.search(r":(.*)$", desc)
        if mm and str(t.type) != "pulse":
            try:
                seq = [int(x) for x in mm.group(1).split()]
            except ValueError:
                seq = None
        trig.append(dict(type=str(t.type), time=int(t.time), duration_ms=float(t.param.duration),
                         description=desc, seq=seq))
    stims = _stimuli(param)
    mismatch = _duration_mismatch(trig, stims)
    source = member
    if mismatch > MAX_MISMATCH_MS:
        # The fragment list does not fit the trigger durations. In two cells the fragment lists
        # of two files are swapped (data check); take the list of a sibling file that fits. When
        # none fits, the stored list is kept, as CxtDep.m would use it, and the file is flagged.
        source = member + " (stored list kept; it does not fit the triggers)"
        folder = member.rsplit("/", 1)[0]
        for other in sorted(m for m in archive.members if m.startswith(folder + "/") and m.endswith(".mat")):
            if other == member:
                continue
            p2 = archive.loadmat(other)["param"]
            if not hasattr(p2, "stimulus"):
                continue
            st2 = _stimuli(p2)
            if _duration_mismatch(trig, st2) <= MAX_MISMATCH_MS:
                stims, source = st2, other
                break
    return dict(member=member, raw=raw if (keep_raw or not smooth) else None, trace=trace, sf=int(resp.sf),
                unit=str(resp.unit), scale=float(resp.scale), triggers=trig, stimuli=stims,
                param=param, rep=effective_repeats(param), duration_mismatch_ms=mismatch,
                stimulus_source=source,
                recording_type=str(param.recording.type), notes=_notes(param))


# ---------------------------------------------------------------------------- probe structure
def sequences(rec: dict) -> list[dict]:
    """Sequence triggers in recording order, each with its fragments and the gaps around it."""
    trig = [t for t in rec["triggers"] if "pulse" not in t["type"] and t["seq"] is not None]
    n = len(rec["trace"])
    out = []
    for k, t in enumerate(trig):
        start = t["time"]
        end = start + int(round(t["duration_ms"] / 1000 * rec["sf"]))
        prev_end = 0 if k == 0 else trig[k - 1]["time"] + int(round(trig[k - 1]["duration_ms"] / 1000 * rec["sf"]))
        next_start = n if k == len(trig) - 1 else trig[k + 1]["time"]
        out.append(dict(seq=tuple(t["seq"]), start=start, end=end, gap_before=(prev_end, start),
                        gap_after=(end, next_start)))
    return out


def probe_table(rec: dict, min_trials: int, contexts_allowed=None, include_silence=True):
    """Probes of a recording, as CxtDep.m forms them.

    Returns a list of dicts: probe fragment index (1-based), duration in samples, and for each
    context (fragment index, 0 for silence) the list of (sequence onset, probe onset) sample
    positions of its trials. Only the first `rep` presentations of each sequence are used
    (`Effective repeats` in the notes). `contexts_allowed`, when given, restricts the
    conditioning stimuli (fragment indices; 0 for silence).
    """
    sf = rec["sf"]
    dur = [int(round(s["duration_ms"] / 1000 * sf)) for s in rec["stimuli"]]
    seqs = sequences(rec)
    rep = rec["rep"]
    by_seq = {}
    for s in seqs:
        by_seq.setdefault(s["seq"], []).append(s)
    if rep is not None:
        by_seq = {k: v[:rep] for k, v in by_seq.items()}
    probes = []
    nfrag = len(dur)
    for p in range(1, nfrag + 1):
        ctx = {}
        for sq, pres in by_seq.items():
            offs = np.cumsum([0] + [dur[f - 1] for f in sq])
            for pos, f in enumerate(sq):
                if f != p:
                    continue
                c = 0 if pos == 0 else sq[pos - 1]
                if c == 0 and not include_silence:
                    continue
                if contexts_allowed is not None and c not in contexts_allowed:
                    continue
                for pr in pres:
                    onset = pr["start"] + offs[pos]
                    ctx.setdefault(c, []).append(dict(onset=onset, seq_start=pr["start"],
                                                      gap_before=pr["gap_before"]))
        if len(ctx) < 2:
            continue
        ntr = min(len(v) for v in ctx.values())
        probes.append(dict(probe=p, duration=dur[p - 1], contexts=sorted(ctx), trials=ctx,
                           n_trials=ntr, eligible=ntr >= min_trials))
    return probes


def probe_matrix(rec: dict, probe: dict) -> tuple[np.ndarray, np.ndarray]:
    """Responses to a probe, (contexts * rep, duration) in mV, each context cut to `rep` trials
    as GetResp does, and the context label of each row."""
    rep = probe["n_trials"]
    T = probe["duration"]
    rows, labels = [], []
    for c in probe["contexts"]:
        for tr in probe["trials"][c][:rep]:
            seg = rec["trace"][tr["onset"]:tr["onset"] + T]
            if len(seg) < T:
                seg = np.concatenate([seg, np.full(T - len(seg), np.nan)])
            rows.append(seg)
            labels.append(c)
    return np.vstack(rows), np.array(labels)


def silence_probe_matrix(rec: dict, min_trials: int):
    """The intersequence silence as a probe (CxtDep.m blank(1) = 2.5 s, cut to the shortest
    gap), with the last fragment of each sequence as its context."""
    sf = rec["sf"]
    seqs = sequences(rec)
    rep = rec["rep"]
    by_seq = {}
    for s in seqs:
        by_seq.setdefault(s["seq"], []).append(s)
    if rep is not None:
        by_seq = {k: v[:rep] for k, v in by_seq.items()}
    T = int(round(BLANK_PROBE_S * sf))
    for v in by_seq.values():
        for s in v:
            T = min(T, s["gap_after"][1] - s["gap_after"][0])
    ctx = {}
    for sq, pres in by_seq.items():
        for s in pres:
            ctx.setdefault(sq[-1], []).append(s["end"])
    if len(ctx) < 2:
        return None
    rep_n = min(len(v) for v in ctx.values())
    if rep_n < min_trials:
        return None
    rows, labels = [], []
    for c in sorted(ctx):
        for onset in ctx[c][:rep_n]:
            rows.append(rec["trace"][onset:onset + T])
            labels.append(c)
    return np.vstack(rows), np.array(labels)


# --------------------------------------------------------------------------------- measures
def _runs_mask(b: np.ndarray, min_len_diff: int = ALPHA_DT) -> np.ndarray:
    """Keep runs of True whose last index minus first index is at least `min_len_diff`
    (KWtest: k(a(2,:)) - k(a(1,:)) >= dt). Works along the last axis."""
    b = np.atleast_2d(b)
    n, T = b.shape
    pad = np.zeros((n, 1), dtype=np.int8)
    d = np.diff(np.concatenate([pad, b.astype(np.int8), pad], axis=1), axis=1)
    rs, cs = np.nonzero(d == 1)
    re_, ce = np.nonzero(d == -1)
    keep = (ce - 1 - cs) >= min_len_diff
    out = np.zeros((n, T + 1), dtype=np.int32)
    np.add.at(out, (rs[keep], cs[keep]), 1)
    np.add.at(out, (re_[keep], ce[keep]), -1)
    return np.cumsum(out[:, :T], axis=1) > 0


def kw_significance(X: np.ndarray, labels: np.ndarray, n_shuffle: int = N_SHUFFLE,
                    rng: np.random.Generator | None = None, chunk: int = 4000):
    """KWtest of CxtDep.m: p-values, significant mask, and the noise floor (fraction of
    permutations significant at each time point)."""
    groups = np.unique(labels)
    M = len(groups)
    N, T = X.shape
    rep = N // M
    r = np.argsort(np.argsort(X, axis=0, kind="stable"), axis=0, kind="stable").astype(np.float32) + 1
    G = (labels[None, :] == groups[:, None]).astype(np.float32) / rep  # M x N
    c = 12.0 / (M * (N + 1))
    rbar = G @ r
    kw = c * ((rbar - (N + 1) / 2) ** 2).sum(0)
    p = stats.chi2.sf(kw, M - 1)
    signif = _runs_mask(p < ALPHA)[0]
    noise = None
    if n_shuffle:
        rng = rng or np.random.default_rng(0)
        thr = stats.chi2.isf(ALPHA, M - 1)
        perms = np.stack([rng.permutation(N) for _ in range(n_shuffle)])
        # permuting the trials is the same as permuting the group labels
        P = np.zeros((n_shuffle * M, N), dtype=np.float32)
        for i in range(n_shuffle):
            P[i * M:(i + 1) * M] = G[:, perms[i]]
        b = np.zeros((n_shuffle, T), dtype=bool)
        for t0 in range(0, T, chunk):
            rb = (P @ r[:, t0:t0 + chunk]).reshape(n_shuffle, M, -1)
            b[:, t0:t0 + chunk] = c * ((rb - (N + 1) / 2) ** 2).sum(1) > thr
        noise = _runs_mask(b).mean(0)
    return dict(p=p, signif=signif, noise=noise, n_contexts=M, rep=rep)


def frac_power(X: np.ndarray, labels: np.ndarray):
    """FracPow of CxtDep.m: total, predictable (Eq. 17) and context-invariant (Eq. 18) power at
    each time point, each trial centred on its mean over the probe window."""
    groups = np.unique(labels)
    n = len(groups)
    N, T = X.shape
    rep = N // n
    Y = X - X.mean(1, keepdims=True)
    tot = Y ** 2
    mt = np.stack([Y[labels == g].mean(0) for g in groups])
    pred = np.stack([(rep * mt[k] ** 2 - tot[labels == g].mean(0)) / (rep - 1) for k, g in enumerate(groups)])
    total = tot.mean(0)
    predictable = pred.mean(0)
    invariant = (n * mt.mean(0) ** 2 - (mt ** 2).mean(0)) / (n - 1)
    return dict(total=total, predictable=predictable, invariant=invariant)


def trial_correlations(X: np.ndarray, labels: np.ndarray) -> dict:
    """Trial-to-trial reliability within each context: mean Pearson r over pairs of trials, and
    mean r of each trial with the mean of the others; averaged over contexts."""
    pairs, loo = [], []
    for g in np.unique(labels):
        Y = X[labels == g]
        C = np.corrcoef(Y)
        iu = np.triu_indices(len(Y), 1)
        pairs.append(np.nanmean(C[iu]))
        s = Y.sum(0)
        k = len(Y)
        loo.append(np.nanmean([np.corrcoef(Y[i], (s - Y[i]) / (k - 1))[0, 1] for i in range(k)]))
    return dict(pairs=float(np.mean(pairs)), loo=float(np.mean(loo)))


def running_mean_0_2t(x: np.ndarray) -> np.ndarray:
    """Running mean over [0, 2t] at each t (Methods, Eq. 20: "the running average over [0, 2t]
    at time t (>= 0), where the window is selected to be symmetric around the time of interest
    t, but always nonnegative"). Where 2t passes the end of the data the window is cut at the
    end (Figure 3B shows the smoothed curve to 6 s, so it is defined there); NaNs are skipped."""
    ok = np.isfinite(x)
    cs = np.concatenate([[0.0], np.cumsum(np.where(ok, x, 0.0))])
    cn = np.concatenate([[0], np.cumsum(ok)])
    T = len(x)
    hi = np.minimum(2 * np.arange(T) + 1, T)
    with np.errstate(invalid="ignore", divide="ignore"):
        return cs[hi] / cn[hi]


def noise_autocorr(X: np.ndarray, labels: np.ndarray, max_lag: int) -> np.ndarray:
    """Eq. 45: autocorrelation of the residuals from the context mean (Eq. 14), normalised by the
    noise variance, averaged over trials; lags 0..max_lag samples."""
    acs = []
    for g in np.unique(labels):
        Y = X[labels == g]
        E = Y - Y.mean(0)
        for e in E:
            acs.append(autocorr(e, max_lag))
    return np.mean(acs, axis=0)


def autocorr(x: np.ndarray, max_lag: int) -> np.ndarray:
    x = x - x.mean()
    n = len(x)
    f = np.fft.rfft(x, 2 * n)
    ac = np.fft.irfft(f * np.conj(f))[:max_lag + 1]
    return ac / ac[0]


# ------------------------------------------------------------------------------------ spikes
def detect_spikes_getspikes(raw: np.ndarray) -> np.ndarray:
    """GetSpikes.m automatic mode (ExtractSpikes with threshold [] and downward removal)."""
    filt = signal.filtfilt(_HP, [1.0], raw)
    amax_i = int(np.argmax(np.abs(filt)))
    thr = 2 / 3 * abs(filt[amax_i])
    if thr > 100:
        mask = np.ones(len(filt), bool)
        mask[max(0, amax_i - 30):amax_i + 30] = False
        thr = np.abs(filt[mask]).max() * 2 / 3
    return _peaks_above(filt, thr, remove_downward=True), thr


def detect_spikes_mad(raw: np.ndarray, k: float = 5.0):
    """Variant: same filter, threshold at k robust SDs (median absolute deviation / 0.6745)."""
    filt = signal.filtfilt(_HP, [1.0], raw)
    thr = k * np.median(np.abs(filt)) / 0.6745
    return _peaks_above(filt, thr, remove_downward=True), thr


def _peaks_above(filt: np.ndarray, thr: float, remove_downward: bool, half: int = 10) -> np.ndarray:
    above = filt > thr
    if not above.any():
        return np.zeros(0, dtype=np.int64)
    d = np.diff(np.concatenate([[0], above.astype(np.int8), [0]]))
    s, e = np.nonzero(d == 1)[0], np.nonzero(d == -1)[0]
    peaks = np.array([a + int(np.argmax(filt[a:b])) for a, b in zip(s, e)])
    if remove_downward:
        keep = []
        for pk in peaks:
            lo, hi = max(pk - half, 0), min(pk + half + 1, len(filt))
            keep.append(filt[lo:hi].min() >= -filt[pk])
        peaks = peaks[np.array(keep, bool)]
    return peaks


def detect_spikes_vm(raw: np.ndarray, thr_mv: float = -20.0, dead_ms: float = 2.0, sf: int = SF):
    """A1 whole-cell spikes: upward crossings of `thr_mv` on the raw membrane potential."""
    up = np.nonzero((raw[1:] >= thr_mv) & (raw[:-1] < thr_mv))[0] + 1
    if len(up) == 0:
        return up
    keep = [up[0]]
    for u in up[1:]:
        if u - keep[-1] > dead_ms / 1000 * sf:
            keep.append(u)
    return np.array(keep)


def psth_sd(spike_times_by_context: dict, Tend: float, dt: float = PSTH_DT):
    """CxtDep.m psth: per context PSTH (spikes/s) on edges 0:dt:Tend with histc, spikes in
    (0, Tend]; SD over contexts with n - 1. Every context is cut to the smallest trial count."""
    rep = min(len(v) for v in spike_times_by_context.values())
    edges = np.arange(0, Tend + 1e-12, dt)
    ps = []
    for c in sorted(spike_times_by_context):
        trials = spike_times_by_context[c][:rep]
        s = np.concatenate([np.asarray(t) for t in trials]) if trials else np.zeros(0)
        s = s[(s > 0) & (s <= Tend)]
        # histc: bin k counts edges[k] <= s < edges[k+1]; the last bin counts s == edges[-1]
        h = np.zeros(len(edges))
        idx = np.searchsorted(edges, s, side="right") - 1
        exact_last = s == edges[-1]
        np.add.at(h, idx[~exact_last & (idx < len(edges) - 1)], 1)
        h[-1] += exact_last.sum()
        ps.append(h / rep / dt)
    ps = np.array(ps)
    return edges, ps, ps.std(0, ddof=1)


# ----------------------------------------------------------------------------------- fitting
def exp_model(t, *p):
    """Eq. 44: sum_k alpha_k exp(-t / tau_k) + kappa; p = (a1, tau1, a2, tau2, ...)."""
    y = np.zeros_like(t, dtype=float)
    for k in range(0, len(p), 2):
        y = y + p[k] * np.exp(-t / p[k + 1])
    return y


def fit_exponentials(t, y, n_exp: int, kappa: float | None = None, sign: float = 1.0,
                     tau_grid=(0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 4.0), nonneg: bool = False):
    """Least squares fit of Eq. 44 (scipy least_squares, the analogue of lsqcurvefit) with a grid
    of start values (a standard choice; the paper gives none). `kappa` fixed when given, else
    free. Returns the best parameters sorted by tau, and the residual sum of squares."""
    from itertools import combinations
    from scipy.optimize import least_squares
    t = np.asarray(t, float)
    y = np.asarray(y, float)
    ok = np.isfinite(y)
    t, y = t[ok], y[ok]
    best = None
    a0 = (np.nanmax(np.abs(y)) if len(y) else 1.0) * sign
    for taus in combinations(tau_grid, n_exp):
        p0 = []
        for tau in taus:
            p0 += [abs(a0) / n_exp * (1 if sign > 0 else -1), tau]
        free_k = kappa is None
        if free_k:
            p0 = p0 + [float(np.median(y[-max(1, len(y) // 10):]))]

        def res(p):
            k = p[-1] if free_k else kappa
            pp = p[:-1] if free_k else p
            return exp_model(t, *pp) + k - y
        lb = []
        ub = []
        for _ in taus:
            lb += [0.0 if nonneg and sign > 0 else -np.inf, 1e-4]
            ub += [0.0 if nonneg and sign < 0 else np.inf, 100.0]
        if free_k:
            lb += [-np.inf]
            ub += [np.inf]
        try:
            r = least_squares(res, p0, bounds=(lb, ub), max_nfev=5000)
        except Exception:
            continue
        sse = float((r.fun ** 2).sum())
        if best is None or sse < best[1]:
            best = (r.x, sse)
    p, sse = best
    pp = p[:-1] if kappa is None else p
    k = p[-1] if kappa is None else kappa
    pairs = sorted([(pp[i], pp[i + 1]) for i in range(0, len(pp), 2)], key=lambda x: x[1])
    return dict(params=pairs, kappa=float(k), sse=sse, n=len(t))


def choose_n_exp(t, y, kappa=None, sign=1.0, max_exp=2, nonneg=False):
    """The paper's rule (Methods, Exponential curve fit): the largest number of exponentials for
    which each |alpha_k| is at least a tenth of sum |alpha_k|."""
    chosen = None
    fits = {}
    for n in range(1, max_exp + 1):
        f = fit_exponentials(t, y, n, kappa=kappa, sign=sign, nonneg=nonneg)
        fits[n] = f
        a = np.abs([x[0] for x in f["params"]])
        if np.all(a >= a.sum() / 10):
            chosen = n
    return chosen, fits


# ------------------------------------------------------------------------ per-cell analyses
BIN = 10                    # samples; stored population traces are 1-ms means (a standard
                            # choice for storage and plotting; the measures are computed at 0.1 ms)


def _bin(x: np.ndarray, b: int = BIN) -> np.ndarray:
    n = len(x) // b
    return x[:n * b].reshape(n, b).mean(1)


def runs(mask: np.ndarray, sf: int = SF) -> list[tuple[float, float]]:
    """(start, end) in seconds of each True run."""
    d = np.diff(np.concatenate([[0], mask.astype(np.int8), [0]]))
    s, e = np.nonzero(d == 1)[0], np.nonzero(d == -1)[0]
    return [(a / sf, b / sf) for a, b in zip(s, e)]


def analyze_probe(X, labels, rng, n_shuffle=N_SHUFFLE, extras=True):
    """Significance and power measures of one probe, the traces stored as 1-ms means."""
    ok = np.isfinite(X).all(0)
    T = int(ok.sum()) if not ok.all() else X.shape[1]
    X = X[:, :T]
    k = kw_significance(X, labels, n_shuffle=n_shuffle, rng=rng)
    fp = frac_power(X, labels)
    out = dict(T=T, n_contexts=k["n_contexts"], rep=k["rep"], contexts=list(np.unique(labels)),
               significant=bool(k["signif"].any()), runs=runs(k["signif"]),
               signif=_bin(k["signif"].astype(np.float32)).astype(np.float32),
               noise=_bin(k["noise"]).astype(np.float32) if k["noise"] is not None else None,
               p_min=float(k["p"].min()),
               **{name: _bin(v).astype(np.float32) for name, v in fp.items()})
    if extras:
        out["corr"] = trial_correlations(X, labels)
        out["noise_ac"] = noise_autocorr(X, labels, max_lag=5000)[::BIN].astype(np.float32)
    return out


def spont_segments(rec: dict) -> list[tuple[int, int]]:
    """Intersequence intervals (between the end of one sequence and the start of the next)."""
    seqs = sequences(rec)
    return [s["gap_before"] for s in seqs[1:]]


def analyze_cc_cell(archive: Archive, member: str, seed: int, include_silence=True,
                    n_shuffle=N_SHUFFLE, extras=True, silence_probe=False):
    """All eligible probes of one current-clamp recording."""
    rec = load_recording(archive, member, smooth=True, keep_raw=True)
    a1_rates = {thr: firing_rates(rec, detect_spikes_vm(rec["raw"], thr)) for thr in A1_THRESHOLDS}
    rec["raw"] = None
    rng = np.random.default_rng(seed)
    probes = probe_table(rec, MIN_TRIALS_CC, include_silence=include_silence) if rec["stimulus_source"] else []
    res = []
    for p in probes:
        X, lab = probe_matrix(rec, p)
        r = dict(member=member, probe=p["probe"], duration=p["duration"] / SF,
                 n_trials=p["n_trials"], eligible=p["eligible"], contexts_all=p["contexts"])
        if p["eligible"]:
            r.update(analyze_probe(X, lab, rng, n_shuffle=n_shuffle, extras=extras))
        res.append(r)
    cell = dict(member=member, rep=rec["rep"], n_fragments=len(rec["stimuli"]),
                n_sequences=len(sequences(rec)), recording_type=rec["recording_type"],
                stimuli=[(s["name"], s["description"], s["duration_ms"]) for s in rec["stimuli"]],
                trace_min=float(rec["trace"].min()), trace_max=float(rec["trace"].max()),
                n_samples=len(rec["trace"]), unit=rec["unit"], rates=a1_rates,
                checks=recording_checks(rec))
    if extras:
        segs = spont_segments(rec)
        acs = [autocorr(rec["trace"][a:b], 5000) for a, b in segs if b - a > 10000]
        cell["spont_ac"] = np.mean(acs, 0)[::BIN].astype(np.float32) if acs else None
        acs1 = [autocorr(rec["trace"][a + SF:b], 5000) for a, b in segs if b - a > 10000 + SF]
        cell["spont_ac_late"] = np.mean(acs1, 0)[::BIN].astype(np.float32) if acs1 else None
    if silence_probe and rec["stimulus_source"]:
        sp = silence_probe_matrix(rec, MIN_TRIALS_CC)
        if sp is not None:
            cell["silence_probe"] = analyze_probe(sp[0], sp[1], rng, n_shuffle=0, extras=False)
    return cell, res


# ----------------------------------------------------------------------- population curves
def stack(probes: list[dict], key: str) -> np.ndarray:
    """Probes x time (1-ms bins) of a stored trace, NaN after the end of each probe."""
    L = max(len(p[key]) for p in probes)
    out = np.full((len(probes), L), np.nan)
    for i, p in enumerate(probes):
        out[i, :len(p[key])] = p[key]
    return out


def population_mean(M: np.ndarray, reading: str) -> np.ndarray:
    """Average over probes at each time: 'running' over the probes still running at t, 'all'
    over every probe with ended probes counted as 0 (claim fig3a-proportion-significant)."""
    if reading == "running":
        with np.errstate(invalid="ignore"):
            return np.nanmean(M, 0)
    return np.nan_to_num(M).sum(0) / M.shape[0]


def late_fraction(prop: np.ndarray, noise: np.ndarray, t_split: float = 1.0, dt: float = 1e-3):
    """Figure 3A legend: cumulative probability corrected for the noise floor (running integral
    of proportion minus noise floor), normalised at its peak; returns 1 - cum(t_split), the time
    of the peak, and the curve."""
    c = np.nancumsum(prop - noise) * dt
    ipk = int(np.nanargmax(c))
    cum = c / c[ipk]
    return float(1 - cum[int(round(t_split / dt))]), ipk * dt, cum


def q_curves(probes: list[dict], reading: str, dt: float = 1e-3):
    """Eqs. 17-20 and 43 over a population: predictable power (Eq. 17), its running mean over
    [0, 2t], context-dependent power (Eq. 19), Q(t) (Eq. 20) and the predictability ratio
    (Eq. 43, smoothed and unsmoothed denominator)."""
    pred = population_mean(stack(probes, "predictable"), reading)
    inv = population_mean(stack(probes, "invariant"), reading)
    if reading == "all":
        # counting ended probes as zero power would bias the ratio only through the denominator
        # and numerator equally; it is shown as a reading of the criterion
        pass
    smooth = running_mean_0_2t(pred)
    dep = pred - inv
    return dict(t=np.arange(len(pred)) * dt, predictable=pred, smooth=smooth, dependent=dep,
                invariant=inv, Q=dep / smooth, ratio=inv / smooth, ratio_raw=inv / pred)


def firing_rates(rec: dict, spikes: np.ndarray) -> dict:
    """Spontaneous and evoked rates (Hz): spikes in the intersequence intervals and in the
    sequences; 'pre1s' is the last 1 s before each sequence (claim a1-mgb-firing-rates)."""
    sf = rec["sf"]
    seqs = sequences(rec)
    sp_n = sp_t = ev_n = ev_t = pre_n = pre_t = 0
    for k, s in enumerate(seqs):
        ev_n += np.count_nonzero((spikes >= s["start"]) & (spikes < s["end"]))
        ev_t += (s["end"] - s["start"]) / sf
        if k > 0:
            a, b = s["gap_before"]
            sp_n += np.count_nonzero((spikes >= a) & (spikes < b))
            sp_t += (b - a) / sf
            a1 = max(a, b - sf)
            pre_n += np.count_nonzero((spikes >= a1) & (spikes < b))
            pre_t += (b - a1) / sf
    return dict(spont=sp_n / sp_t if sp_t else np.nan, evoked=ev_n / ev_t if ev_t else np.nan,
                pre1s=pre_n / pre_t if pre_t else np.nan, spont_s=sp_t, evoked_s=ev_t)


def analyze_mgb_file(archive: Archive, member: str, detector: str = "getspikes"):
    """MGB probes (at least 10 trials per context, at least two contexts): spike times of each
    trial relative to probe onset, PSTH SD over contexts (Eq. 42), and the firing rates."""
    rec = load_recording(archive, member, smooth=False)
    if detector == "getspikes":
        spikes, thr = detect_spikes_getspikes(rec["trace"])
    else:
        spikes, thr = detect_spikes_mad(rec["trace"], k=float(detector.split(":")[1]))
    sf = rec["sf"]
    out = []
    for p in (probe_table(rec, MIN_TRIALS_MGB) if rec["stimulus_source"] else []):
        if not p["eligible"]:
            out.append(dict(member=member, probe=p["probe"], eligible=False, n_trials=p["n_trials"]))
            continue
        Tend = p["duration"] / sf
        by_ctx = {}
        for c in p["contexts"]:
            trials = []
            for tr in p["trials"][c][:p["n_trials"]]:
                s = spikes[(spikes > tr["onset"]) & (spikes <= tr["onset"] + p["duration"])]
                trials.append((s - tr["onset"]) / sf)
            by_ctx[c] = trials
        edges, ps, sd = psth_sd(by_ctx, Tend)
        out.append(dict(member=member, probe=p["probe"], eligible=True, n_trials=p["n_trials"],
                        n_contexts=len(p["contexts"]), contexts=p["contexts"], Tend=Tend,
                        edges=edges, psth=ps, sd=sd))
    info = dict(member=member, rep=rec["rep"], recording_type=rec["recording_type"],
                checks=recording_checks(rec, spikes), n_spikes=len(spikes), threshold=float(thr), rates=firing_rates(rec, spikes),
                duration_s=len(rec["trace"]) / sf, trace_min=float(rec["trace"].min()),
                trace_max=float(rec["trace"].max()), unit=rec["unit"])
    return info, out


# ------------------------------------------------------------- synthetic stimulus properties
# Which parameter of a conditioning stimulus carries which sound property (Methods, Stimuli,
# SYNTHETIC SOUNDS; Table 1 legend): amplitude (attenuation, or the mean envelope level AMmean
# of a modulated harmonic tone), frequency (f0, frequency shift df, band ff, or the TORC/DMR
# "bandwidth/frequency variants"), AM (AM rate AMrange or depth AMstd), FM (FMrange, FMstd), and
# higher-order (a natural sound against its modulated colored noise, marked by `iter`). The
# grouping of conditioning stimuli into ensembles is this attempt's reading of the parameters
# stored with each fragment (Methods, Stimulus design, paragraph 2: "the analysis should be
# conducted by using only those frequency variants ... as conditioning stimuli").
PROPERTY_KEYS = {"amplitude": {"attenuation", "AMmean"}, "frequency": {"f0", "df", "ff"},
                 "AM": {"AMrange", "AMstd", "AMmean"}, "FM": {"FMrange", "FMstd"},
                 "higher-order": {"iter"}}
PROPERTIES = list(PROPERTY_KEYS)
_IGNORED = {"envphase", "sinphase", "iniphase", "torc_parameters", "torc_order", "specmod",
            "tempmod", "duration", "ramp", "sf"}
_DEFAULTS = {"attenuation": 1.0, "df": 0.0}


def _val(v):
    a = np.asarray(v)
    if a.dtype.kind in "fiu":
        return tuple(np.round(a.astype(float).ravel(), 6))
    return str(v)


def fragment_kind(stim: dict, trigger_type: str) -> str:
    """'natural' (a CD fragment or a variant of one), 'MCN', or the synthetic family."""
    p = stim["param"]
    if hasattr(p, "iter") or "pink noise" in stim["description"]:
        return "MCN"
    if stim["file"] and stim["file"] != "[]" and "class" in stim["file"]:
        return "natural"
    return {"torc": "TORC", "dmr": "DMR", "synthetic": "MHT"}.get(trigger_type, trigger_type)


def fragment_params(stim: dict) -> dict:
    p = stim["param"]
    d = dict(_DEFAULTS)
    for k in p._fieldnames:
        if k not in _IGNORED:
            d[k] = _val(getattr(p, k))
    return d


def _family_property(descs: list[str]) -> str | None:
    s = " ".join(descs)
    if "bandwidth" in s or "frequency variants" in s:
        return "frequency"
    if "amplitude variants" in s:
        return "amplitude"
    return None


def property_classes(rec: dict, contexts: list[int], prop: str) -> list[list[int]]:
    """Classes of a probe's conditioning stimuli (fragment indices, silence excluded) that
    differ only in `prop`: the same kind and source, equal in every parameter outside the
    property. For AM, of variants that share AM rate and depth only the one at the most common
    mean level is kept (the others are amplitude variants)."""
    trig_type = next(t["type"] for t in rec["triggers"] if t["seq"] is not None)
    stims = rec["stimuli"]
    keys = PROPERTY_KEYS[prop]
    groups = {}
    for c in contexts:
        if c == 0:
            continue
        s = stims[c - 1]
        kind = fragment_kind(s, trig_type)
        par = fragment_params(s)
        src = s["file"] if kind in ("natural", "MCN") else kind
        if prop == "higher-order":
            kind = "NS/MCN"
        other = tuple(sorted((k, v) for k, v in par.items() if k not in keys))
        groups.setdefault((kind, src, other), []).append((c, par, s["description"]))
    out = []
    for (kind, src, other), mem in groups.items():
        if len(mem) < 2:
            continue
        vals = {tuple(sorted((k, m[1].get(k)) for k in keys)) for m in mem}
        if prop == "higher-order":
            kinds = {fragment_kind(stims[m[0] - 1], trig_type) for m in mem}
            if kinds != {"natural", "MCN"}:
                continue
        elif len(vals) < 2:
            if _family_property([m[2] for m in mem]) != prop:
                continue
        if prop == "AM":
            by = {}
            for m in mem:
                by.setdefault((m[1].get("AMrange"), m[1].get("AMstd")), []).append(m)
            if len(by) < 2:
                continue
            means = [m[1].get("AMmean") for m in mem]
            mode = max(set(means), key=means.count)
            mem = [sorted(v, key=lambda m: m[1].get("AMmean") != mode)[0] for v in by.values()]
        out.append(sorted(m[0] for m in mem))
    return out


def analyze_synthetic_file(archive: Archive, member: str, seed: int, n_shuffle=N_SHUFFLE):
    """Every probe x property ensemble of one synthetic recording: significance and power."""
    rec = load_recording(archive, member, smooth=True, keep_raw=True)
    a1_rates = {thr: firing_rates(rec, detect_spikes_vm(rec["raw"], thr)) for thr in A1_THRESHOLDS}
    rec["raw"] = None
    rng = np.random.default_rng(seed)
    trig_type = next(t["type"] for t in rec["triggers"] if t["seq"] is not None)
    base = probe_table(rec, 1) if rec["stimulus_source"] else []
    n_eligible_any = sum(p["eligible"] for p in probe_table(rec, MIN_TRIALS_CC)) if base else 0
    out = []
    for p in base:
        ptype = fragment_kind(rec["stimuli"][p["probe"] - 1], trig_type)
        for prop in PROPERTIES:
            for cls in property_classes(rec, p["contexts"], prop):
                q = probe_table(rec, MIN_TRIALS_CC, contexts_allowed=set(cls))
                q = [x for x in q if x["probe"] == p["probe"]]
                r = dict(member=member, probe=p["probe"], probe_type=ptype, property=prop,
                         contexts=cls, eligible=bool(q and q[0]["eligible"]),
                         n_trials=q[0]["n_trials"] if q else 0, duration=p["duration"] / SF)
                if r["eligible"]:
                    X, lab = probe_matrix(rec, q[0])
                    r.update(analyze_probe(X, lab, rng, n_shuffle=n_shuffle, extras=False))
                out.append(r)
    info = dict(member=member, rep=rec["rep"], trigger_type=trig_type, n_fragments=len(rec["stimuli"]),
                recording_type=rec["recording_type"], n_sequences=len(sequences(rec)),
                kinds=[fragment_kind(s, trig_type) for s in rec["stimuli"]], rates=a1_rates,
                n_eligible_any=n_eligible_any,
                bands=[fragment_params(s).get("ff") for s in rec["stimuli"]],
                descriptions=[s["description"] for s in rec["stimuli"]],
                checks=recording_checks(rec))
    return info, out


def recording_checks(rec: dict, spikes: np.ndarray | None = None) -> dict:
    """Metadata against data: sampling rate, sum of fragment durations against each sequence
    trigger's duration, gaps between sequences, presentations per sequence against the stated
    effective repeats, and a clock check: the mean response in the 0.3 s after each sequence
    onset against the 0.3 s before it, and the same with onsets shifted by 3 s into the silence
    (membrane potential in mV; for spikes, the rate in Hz)."""
    sf = rec["sf"]
    seqs = sequences(rec)
    dur = [s["duration_ms"] for s in rec["stimuli"]]
    trig_ms = {t["seq"] and tuple(t["seq"]): t["duration_ms"] for t in rec["triggers"] if t["seq"]}
    mismatch = max(abs(sum(dur[f - 1] for f in sq) - d) for sq, d in trig_ms.items())
    gaps = [(s["gap_before"][1] - s["gap_before"][0]) / sf for s in seqs[1:]]
    counts = {}
    for s in seqs:
        counts[s["seq"]] = counts.get(s["seq"], 0) + 1
    w = int(0.3 * sf)

    def contrast(shift):
        pre, post = [], []
        for s in seqs[1:]:
            o = s["start"] - shift
            if spikes is None:
                pre.append(rec["trace"][o - w:o].mean())
                post.append(rec["trace"][o:o + w].mean())
            else:
                pre.append(np.count_nonzero((spikes >= o - w) & (spikes < o)) / 0.3)
                post.append(np.count_nonzero((spikes >= o) & (spikes < o + w)) / 0.3)
        pre, post = np.array(pre), np.array(post)
        return float(np.mean(post - pre)), float(stats.wilcoxon(post, pre).pvalue) if np.any(post != pre) else 1.0
    return dict(sf=sf, duration_mismatch_ms=float(mismatch), stored_mismatch_ms=float(rec["duration_mismatch_ms"]),
                stimulus_source=rec["stimulus_source"], gap_min=float(np.min(gaps)) if gaps else np.nan,
                gap_median=float(np.median(gaps)) if gaps else np.nan, gap_max=float(np.max(gaps)) if gaps else np.nan,
                presentations_min=min(counts.values()), presentations_max=max(counts.values()),
                n_distinct_sequences=len(counts), onset_effect=contrast(0), shifted_effect=contrast(3 * sf))
