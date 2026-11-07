"""Loading and measures for CRCNS data set alm-1 (Li, Chen, Guo, Gerfen & Svoboda 2015, Nature
519, 51-56, doi:10.1038/nature14178).

The data set (doi:10.6080/K0RF5RZT) is unversioned; the files are read from the public S3 bucket
`crcnsarchive` under `alm-1/live/`. Each animal's sessions are MATLAB files inside one
`data_structure_<animal>.tar.gz`; the tar is streamed and decompressed in memory, one session at
a time, and reduced to what the analyses need. Nothing is written to disk.

Each session is reduced to:

- a trial table: trial id, start time, pole in, pole out and cue times (seconds from trial
  start), `GoodTrials`, `PhotostimulationType`, the eight trial type flags, the reaction time
  read from the lick trace, and a summary of the photostimulation waveform;
- per unit: its cell type labels, its median channel, its mean waveform, and its spike times
  (seconds from the start of their trial) with the index of their trial;
- per tagging trial: the onset times of the light pulses, read from the AOM input trace.

Where the parameters come from:

- Epochs. Sample from `PoleInTime` to `PoleOutTime`, delay from `PoleOutTime` to `CueTime`
  (the data set's trial properties; Methods, Behaviour). The response epoch is `RESPONSE_S` =
  1.3 s after the cue, the claims file's reading (a), which is also what the data set's own
  script `matlab_scripts/analyses_scripts/analysis_compile_all_data.m` uses; 1.5 s is reading (b).
- Trials for the neural analyses. Correct trials (Methods, Electrophysiology data analyses),
  `GoodTrials` = 1 (the data description: trials with 0 "should be discarded"), no axonal
  photostimulation (`PhotostimulationType` = 0; the claims file's shared methods), and lick
  early trials dropped or kept (claims file readings a and b). Only trials within each unit's
  recorded span (from its first to its last trial with a spike) count for it: an assumption
  taken from `analysis_compile_all_data.m` ("index stable trials"); the paper does not say.
- Spike width is the trough-to-peak interval of the mean waveform (Methods), at the sampling
  rate of 19531.25 Hz (Methods; the data description). The thresholds 0.35 and 0.45 ms are the
  Methods'.
- Selectivity test: two-tailed t-test with pooled variance on spike rates of lick right against
  lick left trials, P < 0.05 (Methods; claims file). Welch is the claims file's variant.
- Time courses: 200 ms windows (Fig. 2c and ED Fig. 2a legends), stepped by `STEP_S` = 10 ms,
  a standard choice for a detail that cannot change a result beyond the window.
- Reaction time: first movement of the lick (mouth movement) trace after the cue (Methods,
  Behaviour). The paper gives no detection rule, and the trace's level, scale and sign differ
  between sessions. Two rules are run, both assumptions. The noise rule (`rtn_<k>_<floor>`): the
  first sample after the cue from which the trace stays, for `LICK_HOLD_S` = 5 ms, further from
  its pre-cue baseline (median of the 0.2 s before the cue) than `k` times the baseline noise
  (1.4826 times the median absolute deviation) and at least `floor` volts; `k` in
  `LICK_NOISE_K` and `floor` in `LICK_FLOOR` are readings. The peak rule (`rt_<r>`): the first
  sample at which the trace has moved from the baseline by a fraction `r` (`LICK_RISE`) of its
  largest excursion in the 1 s after the cue; trials whose excursion is under five times the
  baseline noise (or 0.02 V) have none. A few correct trials per session keep the trace from
  0.1 s before to 0.3 s after the cue (`lick_examples`), to show the onsets on the traces. As a
  control for the noise rule, `rtfa_<k>_<floor>` is 1 when the same rule, with its baseline
  from 0.3 to 0.1 s before the cue, fires in the last 0.1 s before the cue.
- Light pulses: onsets where the AOM input trace (`aom_input_trace`, 10 kHz) crosses half its
  trial maximum, in trials whose maximum exceeds `AOM_MIN` volts (a standard choice).
"""

from __future__ import annotations

import io
import tarfile
from concurrent.futures import ProcessPoolExecutor

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy import stats

DATASET = "crcns:alm-1"
DATASET_DOI = "10.6080/K0RF5RZT"
VERSION = "unversioned"
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/"
ANIMALS = ["ANM210861", "ANM210862", "ANM210863", "ANM214427", "ANM214429", "ANM214430",
           "ANM218453", "ANM218457", "ANM218693", "ANM219030", "ANM219031", "ANM219033",
           "ANM219036", "ANM219037", "ANM219038", "ANM219247", "ANM219248", "ANM219253",
           "ANM221977"]

FS_WAVEFORM = 19531.25        # Hz, Methods and data description
FS_MAX_MS, PYR_MIN_MS = 0.35, 0.45   # Methods
RESPONSE_S = 1.3              # response epoch, reading (a); 1.5 s is reading (b)
STEP_S = 0.01                 # time-course step, standard choice
WIN_S = 0.2                   # averaging window, Fig. 2c legend
LICK_RISE = (0.05, 0.1, 0.25, 0.5)   # fractions of the trial's peak excursion, readings
LICK_NOISE_K = (3, 5, 10)     # multiples of the pre-cue noise, readings
LICK_FLOOR = (0.002, 0.005)   # volts, smallest departure counted, readings
LICK_HOLD_S = 0.005           # the departure must last this long, an assumption
N_LICK_EXAMPLES = 6           # correct trials per session whose lick trace is kept
AOM_MIN = 1.0                 # volts, a trial with a light pulse
TRIAL_TYPES = ["HitR", "HitL", "ErrR", "ErrL", "NoLickR", "NoLickL", "LickEarly", "StimTrials"]


def _as_list(x):
    if isinstance(x, str):
        return [x]
    return [str(v) for v in np.atleast_1d(x)]


def _reduce(o, animal, session):
    """Reduce one session object (`obj` of a data structure file) to what the analyses use."""
    ids = np.atleast_1d(o.trialIds).astype(int)
    start = np.atleast_1d(o.trialStartTimes).astype(float)
    props = dict(zip(_as_list(o.trialPropertiesHash.keyNames), o.trialPropertiesHash.value))
    tts = _as_list(o.trialTypeStr)
    mat = np.atleast_2d(o.trialTypeMat)
    trials = pd.DataFrame({"trial_id": ids, "start": start,
                           "pole_in": props["PoleInTime"].astype(float),
                           "pole_out": props["PoleOutTime"].astype(float),
                           "cue": props["CueTime"].astype(float),
                           "good": props["GoodTrials"].astype(float),
                           "ptype": props["PhotostimulationType"].astype(float)})
    for name in TRIAL_TYPES:
        trials[name] = mat[tts.index(name)].astype(bool) if name in tts else False
    trials.insert(0, "session", session)
    trials.insert(0, "animal", animal)

    # time series: lick trace, AOM input, laser power, 10 kHz, only within trials
    ts = o.timeSeriesArrayHash.value
    names = _as_list(ts.idStr)
    t = np.asarray(ts.time, float)
    tr = np.asarray(ts.trial).astype(int)
    vm = np.asarray(ts.valueMatrix)
    lick, aom, power = (vm[:, names.index(n)] for n in ("lick_trace", "aom_input_trace", "laser_power"))
    bounds = np.flatnonzero(np.diff(tr)) + 1
    seg_start = np.r_[0, bounds]
    seg_end = np.r_[bounds, len(tr)]
    pos = {tid: k for k, tid in enumerate(ids)}
    extra = {k: np.full(len(ids), np.nan) for k in
             ["ts_offset", "ts_len", "aom_max", "power_max", "stim_on", "stim_off", "n_pulses",
              "pulse_ms", "lick_base", "lick_peak", "lick_noise", "n_lick_pre"] + [f"rt_{r}" for r in LICK_RISE]
             + [f"rtn_{k}_{f}" for k in LICK_NOISE_K for f in LICK_FLOOR]
             + [f"rtfa_{k}_{f}" for k in LICK_NOISE_K for f in LICK_FLOOR]}
    pulses = {}
    examples = {}
    hold = int(round(LICK_HOLD_S * 1e4))   # samples at 10 kHz
    for a, b in zip(seg_start, seg_end):
        tid = tr[a]
        if tid not in pos:
            continue
        k = pos[tid]
        tt = t[a:b] - start[k]
        extra["ts_offset"][k] = tt[0]
        extra["ts_len"][k] = tt[-1] - tt[0]
        am = aom[a:b]
        extra["aom_max"][k] = am.max()
        extra["power_max"][k] = power[a:b].max()
        if am.max() > AOM_MIN:
            hi = am > am.max() / 2
            on = np.flatnonzero(hi[1:] & ~hi[:-1]) + 1
            off = np.flatnonzero(~hi[1:] & hi[:-1]) + 1
            if len(on):
                extra["stim_on"][k] = tt[on[0]]
                extra["stim_off"][k] = tt[off[-1]] if len(off) else tt[-1]
                extra["n_pulses"][k] = len(on)
                if len(off) >= len(on):
                    extra["pulse_ms"][k] = np.median(tt[off[:len(on)]] - tt[on]) * 1e3
                pulses[k] = tt[on]
        cue = trials.cue.iat[k]
        if np.isfinite(cue):
            lk = lick[a:b]
            pre = (tt > cue - 0.2) & (tt <= cue)
            post = tt > cue
            post = (tt > cue) & (tt <= cue + 1.0)
            if pre.sum() > 100 and post.sum() > 100:
                base = np.median(lk[pre])
                noise = 1.4826 * np.median(np.abs(lk[pre] - base))
                exc = lk[post] - base
                peak = exc[np.argmax(np.abs(exc))]
                extra["lick_base"][k] = base
                extra["lick_peak"][k] = peak
                extra["lick_noise"][k] = noise
                for r in LICK_RISE:
                    if abs(peak) <= max(5 * noise, 0.02):
                        continue
                    above = np.flatnonzero(exc * np.sign(peak) > r * abs(peak))
                    extra[f"rt_{r}"][k] = tt[post][above[0]] - cue
                dev = np.abs(exc)
                # control for the noise rule: the same rule before the cue, baseline from 0.3 to
                # 0.1 s before it, detection in the last 0.1 s before it
                cpre = (tt > cue - 0.3) & (tt <= cue - 0.1)
                cwin = (tt > cue - 0.1) & (tt <= cue)
                cbase = np.median(lk[cpre])
                cnoise = 1.4826 * np.median(np.abs(lk[cpre] - cbase))
                cdev = np.abs(lk[cwin] - cbase)
                for kk in LICK_NOISE_K:
                    for f in LICK_FLOOR:
                        out = (dev > max(kk * noise, f)).astype(int)
                        run = np.convolve(out, np.ones(hold, int), "valid")
                        first = np.flatnonzero(run == hold)
                        if len(first):
                            extra[f"rtn_{kk}_{f}"][k] = tt[post][first[0]] - cue
                        cout = (cdev > max(kk * cnoise, f)).astype(int)
                        extra[f"rtfa_{kk}_{f}"][k] = float(np.any(np.convolve(cout, np.ones(hold, int), "valid") == hold))
                ok = (trials.good.iat[k] == 1 and trials.ptype.iat[k] == 0 and not trials.LickEarly.iat[k]
                      and (trials.HitR.iat[k] or trials.HitL.iat[k]))
                if ok and len(examples) < N_LICK_EXAMPLES:
                    w = (tt > cue - 0.1) & (tt <= cue + 0.3)
                    examples[k] = ((tt[w] - cue).astype(np.float32), lk[w].astype(np.float32))
            samp = (tt > trials.pole_in.iat[k]) & (tt < cue)
            hi = lk > 1.0
            extra["n_lick_pre"][k] = int(np.sum(samp[1:] & hi[1:] & ~hi[:-1]))
    for key, v in extra.items():
        trials[key] = v

    units = []
    for i, u in enumerate(np.atleast_1d(o.eventSeriesHash.value)):
        et = np.atleast_1d(u.eventTimes).astype(float)
        etr = np.atleast_1d(u.eventTrials).astype(int)
        k = np.searchsorted(ids, etr)
        ok = (k < len(ids)) & (ids[np.minimum(k, len(ids) - 1)] == etr)
        wf = np.atleast_2d(u.waveforms)
        units.append({"animal": animal, "session": session, "unit": i + 1,
                      "cell_types": tuple(_as_list(u.cellType)) if np.size(u.cellType) else (),
                      "channel": float(np.median(u.channel)),
                      "waveform": wf.mean(axis=0),
                      "waveform_shape": wf.shape,
                      "n_spikes": len(et),
                      "spike_t": et[ok] - start[k[ok]],
                      "spike_k": k[ok].astype(np.int32),
                      "spike_t_session": et[ok]})
    return {"animal": animal, "session": session, "trials": trials, "units": units,
            "pulses": pulses, "lick_examples": examples}


def load_animal(animal):
    """Stream one animal's tar.gz and reduce each session in it."""
    url = f"{BASE}datafiles/data_structure_files/data_structure_{animal}.tar.gz"
    out = []
    with fsspec.open(url, block_size=2**23).open() as fh:
        with tarfile.open(fileobj=fh, mode="r|gz") as tf:
            for m in tf:
                if not m.isfile() or not m.name.endswith(".mat"):
                    continue
                raw = tf.extractfile(m).read()
                o = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)["obj"]
                del raw
                session = m.name.split("/")[-1].replace("data_structure_", "").replace(".mat", "")
                out.append(_reduce(o, animal, session))
                del o
    return out


def load_meta():
    """Per-session metadata from meta_data_files.tar.gz."""
    rows = []
    with fsspec.open(BASE + "datafiles/meta_data_files.tar.gz").open() as fh:
        with tarfile.open(fileobj=fh, mode="r|gz") as tf:
            for m in tf:
                if not m.isfile():
                    continue
                md = sio.loadmat(io.BytesIO(tf.extractfile(m).read()), squeeze_me=True,
                                 struct_as_record=False)["meta_data"]
                ph = getattr(md, "photostim", None)
                rows.append({"session": m.name.split("/")[-1].replace("meta_data_", "").replace(".mat", ""),
                             "animal_id": "/".join(_as_list(md.animalID)),
                             "strain": "/".join(_as_list(md.animalStrain)),
                             "gene": "/".join(_as_list(md.animalGeneModification)),
                             "date_of_birth": str(md.dateOfBirth),
                             "penetration": int(md.extracellular.penetrationN),
                             "probe": str(md.extracellular.probeType),
                             "photostim_location": "/".join(_as_list(ph.photostimLocation)) if ph is not None and hasattr(ph, "photostimLocation") else ""})
    return pd.DataFrame(rows)


def load_all(workers=3):
    """Stream every animal (largest files first, `workers` at a time) and return the sessions."""
    with ProcessPoolExecutor(workers) as ex:
        parts = list(ex.map(load_animal, ANIMALS))
    return [s for p in parts for s in p]


def spike_width_ms(waveform):
    """Trough-to-peak interval of a mean waveform (Methods): from the trough to the following
    maximum."""
    w = np.asarray(waveform, float)
    i = int(np.argmin(w))
    j = i + int(np.argmax(w[i:]))
    return (j - i) / FS_WAVEFORM * 1e3


def trial_mask(trials, unit, lick_early="drop", outcome="hit"):
    """Trials a unit's analysis uses. `outcome` is 'hit' or 'err'."""
    span = np.zeros(len(trials), bool)
    if len(unit["spike_k"]):
        span[unit["spike_k"].min():unit["spike_k"].max() + 1] = True
    m = span & (trials.good.values == 1) & (trials.ptype.values == 0) & np.isfinite(trials.cue.values)
    if lick_early == "drop":
        m &= ~trials.LickEarly.values
    right = trials["HitR" if outcome == "hit" else "ErrR"].values
    left = trials["HitL" if outcome == "hit" else "ErrL"].values
    return m & right, m & left


def counts_in(unit, trials, sel, t0, t1):
    """Spike counts of a unit in trials `sel` between t0 and t1 (arrays, seconds from trial start)."""
    idx = np.flatnonzero(sel)
    out = np.zeros(len(idx))
    if not len(idx):
        return out
    k, t = unit["spike_k"], unit["spike_t"]
    m = np.isin(k, idx)
    k, t = k[m], t[m]
    loc = np.searchsorted(idx, k)
    a, b = t0[k], t1[k]
    inside = (t > a) & (t < b)
    np.add.at(out, loc[inside], 1)
    return out


def epoch_bounds(trials, response_s=RESPONSE_S):
    """Start and end (s from trial start) of sample, delay and response epochs, and the whole
    trial (sample start to response end), per trial."""
    pi, po, cu = trials.pole_in.values, trials.pole_out.values, trials.cue.values
    return {"sample": (pi, po), "delay": (po, cu), "response": (cu, cu + response_s),
            "trial": (pi, cu + response_s), "pre": (pi - 0.5, pi), "pre_all": (np.zeros_like(pi), pi)}


def unit_epoch_rates(unit, trials, lick_early="drop", response_s=RESPONSE_S, outcome="hit"):
    """Per epoch, the spike rates (spikes/s) on lick right and lick left trials, and under
    `<epoch>_count` the spike counts."""
    r, l = trial_mask(trials, unit, lick_early, outcome)
    out = {"n_right": int(r.sum()), "n_left": int(l.sum())}
    for name, (a, b) in epoch_bounds(trials, response_s).items():
        dur = b - a
        cr, cl = counts_in(unit, trials, r, a, b), counts_in(unit, trials, l, a, b)
        out[name] = (cr / dur[r], cl / dur[l])
        out[name + "_count"] = (cr, cl)
    return out


def ttest_p(x, y, welch=False):
    if len(x) < 2 or len(y) < 2:
        return np.nan
    if np.var(x) == 0 and np.var(y) == 0:
        return 1.0 if np.mean(x) == np.mean(y) else 0.0
    return stats.ttest_ind(x, y, equal_var=not welch).pvalue


def cue_aligned_counts(unit, trials, sel, centers, win=WIN_S):
    """Spike counts per trial in windows of `win` s centred on `centers` (s from the cue)."""
    idx = np.flatnonzero(sel)
    out = np.zeros((len(idx), len(centers)))
    if not len(idx):
        return out
    k, t = unit["spike_k"], unit["spike_t"]
    m = np.isin(k, idx)
    rel = t[m] - trials.cue.values[k[m]]
    loc = np.searchsorted(idx, k[m])
    edges_lo = centers - win / 2
    for j, lo in enumerate(edges_lo):
        inside = (rel > lo) & (rel < lo + win)
        out[:, j] = np.bincount(loc[inside], minlength=len(idx))
    return out


def unit_table(sessions, lick_early="drop", response_s=RESPONSE_S):
    """One row per unit: labels, spike width, trial counts, per-epoch rates on lick right (R)
    and lick left (L) correct trials and on error trials (labelled by the instructed side), the
    selectivity t-test P values (pooled and Welch on rates, as the data set's
    analysis_compile_all_data.m tests them; pooled on spike counts, the Methods' wording, as
    `pc_`), and baseline rates."""
    rows = []
    for s in sessions:
        tr = s["trials"]
        for u in s["units"]:
            ct = u["cell_types"]
            row = {"animal": s["animal"], "session": s["session"], "unit": u["unit"],
                   "label": "FS" if "FS" in ct else "pyramidal" if "pyramidal" in ct else "unclassified",
                   "tag": "PT" if "PT" in ct else "IT" if "IT" in ct else "",
                   "width_ms": spike_width_ms(u["waveform"]), "n_spikes": u["n_spikes"]}
            rates = unit_epoch_rates(u, tr, lick_early, response_s)
            err = unit_epoch_rates(u, tr, lick_early, response_s, outcome="err")
            row["n_R"], row["n_L"] = rates["n_right"], rates["n_left"]
            row["n_errR"], row["n_errL"] = err["n_right"], err["n_left"]
            for ep in ("sample", "delay", "response", "trial", "pre", "pre_all"):
                r, l = rates[ep]
                row[f"{ep}_R"] = r.mean() if len(r) else np.nan
                row[f"{ep}_L"] = l.mean() if len(l) else np.nan
                er, el = err[ep]
                row[f"{ep}_errR"] = er.mean() if len(er) else np.nan
                row[f"{ep}_errL"] = el.mean() if len(el) else np.nan
                if ep in ("sample", "delay", "response", "trial"):
                    row[f"p_{ep}"] = ttest_p(r, l)
                    row[f"pw_{ep}"] = ttest_p(r, l, welch=True)
                    row[f"pc_{ep}"] = ttest_p(*rates[ep + "_count"])
            rows.append(row)
    df = pd.DataFrame(rows)
    for kind, col in (("p", "selective"), ("pw", "selective_welch"), ("pc", "selective_count")):
        sig = df[[f"{kind}_sample", f"{kind}_delay", f"{kind}_response"]].fillna(1) < 0.05
        df[col] = sig.any(axis=1)
        df[col + "_prep"] = sig.iloc[:, 0] | sig.iloc[:, 1]
        df[col + "_peri"] = sig.iloc[:, 2]
    df["contra"] = df.trial_R > df.trial_L
    return df


def categories(df, sel_col="selective"):
    """Preparatory only, both, peri-movement only, among the rows where `sel_col` holds."""
    d = df[df[sel_col]]
    prep, peri = d[sel_col + "_prep"], d[sel_col + "_peri"]
    return {"prep_only": int((prep & ~peri).sum()), "both": int((prep & peri).sum()),
            "peri_only": int((~prep & peri).sum()), "n": len(d)}


def bootstrap_more_ipsi(contra, n_boot=10_000, rng=None):
    """Methods (Fig. 3f, j): neurons resampled with replacement; P is the fraction of resamples
    with more ipsi-preferring than contra-preferring neurons (one-tailed)."""
    contra = np.asarray(contra, bool)
    n = len(contra)
    if n == 0:
        return np.nan
    k = rng.binomial(n, contra.mean(), size=n_boot)   # resampling n neurons with replacement
    return float(np.mean(n - k > k))


def antidromic_latencies(session, unit, ptypes, order=0, max_ms=10.0):
    """Latency (ms) of the first spike after each light pulse in tagging trials of the given
    photostimulation types. `order` 0 is the first pulse of each pair, 1 the second. Pulses are
    paired when the next onset follows within 15 ms. Returns one latency per pulse (NaN when no
    spike within `max_ms`), so the response probability is the fraction that is finite. The
    default window, 10 ms, ends before the second pulse of a pair (onsets 11 ms apart in the
    AOM trace), so a response to the second pulse is not taken for one to the first."""
    tr = session["trials"]
    out = []
    k, t = unit["spike_k"], unit["spike_t"]
    span = (k.min(), k.max()) if len(k) else (0, -1)
    for ti, on in session["pulses"].items():
        if not np.isfinite(tr.ptype.iat[ti]) or tr.ptype.iat[ti] not in ptypes:
            continue
        if not (span[0] <= ti <= span[1]):
            continue
        first = np.r_[True, np.diff(on) > 0.015]
        idx = np.flatnonzero(first)
        if order == 1:
            idx = idx[(idx + 1 < len(on))]
            idx = idx[np.diff(on)[idx] <= 0.015] + 1
        st = np.sort(t[k == ti])
        for p in on[idx]:
            j = np.searchsorted(st, p, side="right")
            lat = (st[j] - p) * 1e3 if j < len(st) else np.inf
            out.append(lat if lat <= max_ms else np.nan)
    return np.array(out)


def latency_background(lat, mode, half_width_ms, max_ms=10.0, guard_ms=2.0):
    """Spikes expected by chance within `half_width_ms` of the modal latency: the density of
    first-spike latencies more than `guard_ms` from the mode (in 0 to `max_ms`), taken as the
    spontaneous background, times the window's width. Returns the expected number and the number
    observed in the window."""
    lat = lat[np.isfinite(lat)]
    far = np.abs(lat - mode) > guard_ms
    span = max_ms - (min(mode + guard_ms, max_ms) - max(mode - guard_ms, 0.0))
    density = far.sum() / span if span > 0 else np.nan
    return density * 2 * half_width_ms, int(np.sum(np.abs(lat - mode) <= half_width_ms))


def latency_mode(lat, bin_ms=0.2):
    """Modal latency (centre of the fullest `bin_ms` bin)."""
    lat = lat[np.isfinite(lat)]
    h, e = np.histogram(lat, bins=np.arange(0, lat.max() + bin_ms, bin_ms))
    return e[np.argmax(h)] + bin_ms / 2


def latency_mode_stats(lat, half_width_ms=1.0, bin_ms=0.2):
    """Mean latency and jitter (s.d.) of the spikes within `half_width_ms` of the modal latency
    (bins of `bin_ms`), with the response probability and the number of responses. The paper
    gives no window; 1 ms is an assumption, chosen because the spikes between 0.5 and 1 ms from
    the mode far exceed the spontaneous background (`latency_background`); 0.5 ms is a variant."""
    lat = lat[np.isfinite(lat)]
    if len(lat) < 3:
        return np.nan, np.nan, 0.0, len(lat)
    h, e = np.histogram(lat, bins=np.arange(0, lat.max() + bin_ms, bin_ms))
    mode = e[np.argmax(h)] + bin_ms / 2
    near = lat[np.abs(lat - mode) <= half_width_ms]
    return near.mean(), near.std(ddof=1) if len(near) > 1 else np.nan, len(near), len(lat)


BIN_S = 0.01
CUE_EDGES = np.round(np.arange(-3.6, 2.1 + 1e-9, BIN_S), 3)   # 10 ms bins around the cue


def cue_binned(unit, trials, sel):
    """Spike counts in 10 ms bins from 3.6 s before to 2.1 s after the cue, one row per trial
    in `sel`."""
    idx = np.flatnonzero(sel)
    out = np.zeros((len(idx), len(CUE_EDGES) - 1))
    if not len(idx):
        return out
    k, t = unit["spike_k"], unit["spike_t"]
    m = np.isin(k, idx)
    rel = t[m] - trials.cue.values[k[m]]
    loc = np.searchsorted(idx, k[m])
    b = np.floor((rel - CUE_EDGES[0]) / BIN_S).astype(int)
    ok = (b >= 0) & (b < out.shape[1])
    np.add.at(out, (loc[ok], b[ok]), 1)
    return out


def window_sums(binned, win=WIN_S):
    """Sliding sums over `win` s of 10 ms bins; returns the sums and the window centres (s from
    the cue)."""
    n = int(round(win / BIN_S))
    c = np.cumsum(np.pad(binned, ((0, 0), (1, 0))), axis=1)
    sums = c[:, n:] - c[:, :-n]
    centers = CUE_EDGES[:len(CUE_EDGES) - n] + win / 2
    return sums, np.round(centers, 3)
