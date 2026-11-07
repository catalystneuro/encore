"""Loading and measures for CRCNS data set alm-3 (Li, Daie, Svoboda & Druckmann 2016, Nature 532,
459-464, doi:10.1038/nature17643).

The data set holds one MATLAB file per recording session (`data/data_structure_files/`), each a
structure `obj` with the trial table, the photostimulus type of each trial, the lick and laser
traces, and the spike times of the sorted single units. Files are streamed from the public S3
bucket `crcnsarchive` into memory and reduced as they load; nothing is written to disk. CRCNS data
sets are not versioned; the files read are those under `alm-3/live/` with the MD5 sums of the data
set's `checksums.md5`.

Where the parameters come from. "Code" is the authors' MATLAB analysis scripts deposited in the
data set (`alm-3/live/analyses_scripts/`), which the data set's description says reproduce the
paper's figures; the claims file did not read them. They are cited by file name.

- Trials (`trial_mask`): correct and error trials grouped by instructed movement (HitR or ErrR is
  lick right, HitL or ErrL lick left), lick-early trials and trials marked GoodTrials = 0 dropped,
  and only trials between the unit's first and last trial with a spike (the unit's stable
  trials). Code, analysis_compile_all_data_unilateral.m, "index the behavioral trials" and "index
  stable trials"; the Methods, Electrophysiology data analysis, say selectivity under
  photoinhibition uses "all trials, correct and incorrect, grouped by instructed movement".
- Epochs: sample from PoleInTime to PoleOutTime, delay from PoleOutTime to CueTime, response the
  1.3 s after CueTime (code, same file, "significant selectivity").
- Mouse line: the gene modification in the session's meta data file (`load_meta`).
- Cell type: the `cellType` label of each unit ("pyramidal", "FS" or empty), which the data
  description says comes from the spike-width bounds of the Methods. The trough-to-peak width of
  the mean waveform is also computed, to check the label.
- PSTH (`psth`): mean spike rate in a 200 ms boxcar centred on each time point, as
  func_getPSTH.m of the code (1 ms bins convolved with a 200 ms window); it is evaluated here
  every 5 ms, a sampling step that cannot change a recovery time by more than 5 ms (a standard
  choice).
- Rate test (`rate_pvalues`): two-tailed t-test of spike counts in 400 ms windows centred every
  50 ms from 3 s before to 2 s after the cue, control against photoinhibition trials, lick right
  and lick left pooled (Methods, Electrophysiology data analysis; code, "t-test on firing rate").
- Licks: the first lick after the go cue is the first upward crossing of the lick trace (a
  photodiode signal) over a threshold set per session halfway between the trace's median and its
  99.9th percentile; a standard choice, as neither the paper nor the code defines it.
"""
import hashlib
import io
import re
import time
import xml.etree.ElementTree as ET

import fsspec
import numpy as np
import requests
import scipy.io as sio

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com"
PREFIX = "alm-3/live/"
DATASET_ID = "alm-3"
DATASET_VERSION = "unversioned"  # CRCNS data sets have no versions (docs/archives.md)
DATASET_DOI = "10.6080/K0RB72JW"

STIM_LABELS = {
    0: "control",
    1: "ipsi 1 spot sample (0.5 s)",
    2: "ipsi 1 spot early delay (0.5 s)",
    3: "ipsi 1 spot middle delay (0.5 s)",
    -1: "no ramp sample (do not analyse)",
    -2: "no ramp early delay (do not analyse)",
    -3: "no ramp middle delay (do not analyse)",
    4: "ipsi 1 spot (0.8 s)",
    5: "contra 1 spot (0.8 s)",
    6: "bilateral 4 spots (0.8 s)",
    7: "bilateral 1 spot (0.8 s)",
    8: "ipsi 4 spots (0.8 s)",
    9: "contra 4 spots (0.8 s)",
    10: "CCX ipsi 1 spot (0.8 s)",
    11: "CCX contra 1 spot (0.8 s)",
    12: "CCX bilateral 4 spots (0.8 s)",
}

SAMPLE_RATE_WAVEFORM = 19531.25  # Hz, data description ("Each snippets is 29 samples long")


def list_files():
    """List the data set's files under alm-3/ with their sizes, from the bucket's listing."""
    r = requests.get(f"{BUCKET}/?list-type=2&prefix=alm-3/", timeout=60)
    r.raise_for_status()
    ns = {"s": "http://s3.amazonaws.com/doc/2006-03-01/"}
    root = ET.fromstring(r.content)
    if root.find("s:IsTruncated", ns).text != "false":
        raise RuntimeError("bucket listing truncated")
    out = {}
    for c in root.findall("s:Contents", ns):
        out[c.find("s:Key", ns).text] = int(c.find("s:Size", ns).text)
    return out


def checksums():
    """MD5 sums from the data set's checksums.md5, keyed by path under alm-3/live/."""
    r = requests.get(f"{BUCKET}/{PREFIX}checksums.md5", timeout=60)
    r.raise_for_status()
    out = {}
    for line in r.text.splitlines():
        parts = line.split()
        if len(parts) == 2:
            out[parts[1]] = parts[0]
    return out


def session_names():
    """The sessions: one per data_structure_<ANM>_<date>.mat file."""
    keys = list_files()
    names = []
    for k in keys:
        m = re.match(r"alm-3/live/data/data_structure_files/data_structure_(ANM\d+_\d+)\.mat$", k)
        if m:
            names.append(m.group(1))
    return sorted(names)


def _first_crossings(x, thr):
    above = x > thr
    return np.flatnonzero(above[1:] & ~above[:-1]) + 1


def _reduce(obj, name):
    tp = obj.trialPropertiesHash
    keys = list(tp.keyNames)
    val = {k: np.asarray(tp.value[i], dtype=float) for i, k in enumerate(keys)}
    types = {str(s): np.asarray(obj.trialTypeMat[i], dtype=bool) for i, s in enumerate(obj.trialTypeStr)}
    trial_ids = np.asarray(obj.trialIds, dtype=int)
    t0 = np.asarray(obj.trialStartTimes, dtype=float)
    n = len(trial_ids)
    s = {
        "name": name,
        "mouse": name.split("_")[0],
        "date": name.split("_")[1],
        "trial_ids": trial_ids,
        "trial_start": t0,
        "pole_in": val["PoleInTime"],
        "pole_out": val["PoleOutTime"],
        "cue": val["CueTime"],
        "good": val["GoodTrials"] == 1,
        "stim_type": val["PhotostimulationType"],
        "trial_types": types,
        "trial_type_names": [str(x) for x in obj.trialTypeStr],
        "trial_property_names": keys,
        "time_unit": int(obj.trialTimeUnit),
    }
    # Lick and laser traces, reduced per trial.
    ts = obj.timeSeriesArrayHash.value
    s["ts_channels"] = [str(x) for x in ts.idStr]
    vm = ts.valueMatrix
    tt = np.asarray(ts.trial, dtype=int)
    tm = np.asarray(ts.time, dtype=float)
    lick = vm[:, list(ts.idStr).index("lick_trace")]
    laser_col = list(ts.idStr).index("laser_power") if "laser_power" in list(ts.idStr) else None
    aom_col = list(ts.idStr).index("aom_input_trace") if "aom_input_trace" in list(ts.idStr) else None
    finite = np.isfinite(lick)
    med = np.median(lick[finite])
    hi = np.percentile(lick[finite], 99.9)
    s["lick_median"], s["lick_p999"] = float(med), float(hi)
    thr = med + 0.5 * (hi - med)
    s["dt_trace"] = float(np.median(np.diff(tm[:1000])))
    order = np.argsort(tt, kind="stable")
    tt_sorted = tt[order]
    bounds = np.searchsorted(tt_sorted, trial_ids, side="left"), np.searchsorted(tt_sorted, trial_ids, side="right")
    first_lick = np.full(n, np.nan)
    first_lick_any = np.full(n, np.nan)
    laser_on = np.full(n, np.nan)
    laser_off = np.full(n, np.nan)
    laser_max = np.full(n, np.nan)
    aom_on = np.full(n, np.nan)
    aom_off = np.full(n, np.nan)
    trace_end = np.full(n, np.nan)
    for i in range(n):
        idx = order[bounds[0][i]:bounds[1][i]]
        if len(idx) == 0:
            continue
        t = tm[idx] - t0[i]
        trace_end[i] = t[-1]
        lk = lick[idx]
        cr = _first_crossings(lk, thr)
        if len(cr):
            first_lick_any[i] = t[cr[0]]
            if np.isfinite(s["cue"][i]):
                after = t[cr][t[cr] > s["cue"][i]]
                if len(after):
                    first_lick[i] = after[0]
        if laser_col is not None:
            L = vm[idx, laser_col]
            L = np.where(np.isfinite(L), L, 0.0)
            if L.max() > 0:
                laser_max[i] = L.max()
                on = t[L > 0.05 * L.max()]
                laser_on[i], laser_off[i] = on[0], on[-1]
        if aom_col is not None:
            A = vm[idx, aom_col]
            A = np.where(np.isfinite(A), A, 0.0)
            if A.max() > 0.05:
                on = t[A > 0.05 * A.max()]
                aom_on[i], aom_off[i] = on[0], on[-1]
    s.update(first_lick=first_lick, first_lick_any=first_lick_any, laser_on=laser_on, laser_off=laser_off,
             laser_max=laser_max, aom_on=aom_on, aom_off=aom_off, trace_end=trace_end, lick_threshold=thr)
    # Units.
    es = obj.eventSeriesHash
    vals = es.value if isinstance(es.value, np.ndarray) else [es.value]
    units = []
    id_to_index = {int(tid): i for i, tid in enumerate(trial_ids)}
    for k, u in enumerate(vals):
        et = np.atleast_1d(np.asarray(u.eventTimes, dtype=float))
        etr = np.atleast_1d(np.asarray(u.eventTrials, dtype=int))
        wf = np.atleast_2d(np.asarray(u.waveforms, dtype=float))
        mw = wf.mean(axis=0) if wf.size else np.full(29, np.nan)
        trough = int(np.argmin(mw))
        peak = trough + int(np.argmax(mw[trough:]))
        ct = u.cellType
        if isinstance(ct, np.ndarray):
            ct = [str(x) for x in ct.ravel()]
        else:
            ct = [str(ct)] if str(ct) else []
        ti = np.array([id_to_index.get(int(x), -1) for x in etr])
        ok = ti >= 0
        rel = et[ok] - t0[ti[ok]]
        units.append({
            "key": str(np.atleast_1d(es.keyNames)[k]),
            "descr": str(np.atleast_1d(es.descr)[k]),
            "fields": list(u._fieldnames),
            "cell_type": ct,
            "spike_width_ms": (peak - trough) / SAMPLE_RATE_WAVEFORM * 1e3,
            "mean_waveform": mw.astype(np.float32),
            "channel": float(np.median(np.atleast_1d(u.channel))),
            "n_spikes": len(et),
            "n_spikes_outside_trials": int((~ok).sum()),
            "spike_trial_index": ti[ok].astype(np.int32),
            "spike_time": rel.astype(np.float64),
            "first_trial": int(etr.min()) if len(etr) else -1,
            "last_trial": int(etr.max()) if len(etr) else -1,
            "time_unit": int(u.timeUnit),
            "spikes_sorted": bool(np.all(np.diff(et) >= 0)),
        })
    s["units"] = units
    return s


def load_session(name, retries=3):
    """Stream one session file into memory, compute its MD5 sum and reduce it."""
    url = f"{BUCKET}/{PREFIX}data/data_structure_files/data_structure_{name}.mat"
    for attempt in range(retries):
        try:
            with fsspec.open(url, "rb", block_size=2**24) as f:
                raw = f.read()
            break
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(5)
    digest = hashlib.md5(raw).hexdigest()
    obj = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)["obj"]
    del raw
    s = _reduce(obj, name)
    s["md5"] = digest  # computed from the bytes read
    return s


def load_all(names=None, workers=3):
    """Load the sessions, a few at a time in separate processes, in name order."""
    from concurrent.futures import ProcessPoolExecutor
    names = session_names() if names is None else names
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(load_session, names))


# ---------------------------------------------------------------- experiments and trials

def experiment(s):
    """The experiment a session belongs to, from the photostimulus types it holds.

    unilateral: types 1 to 3 (or -1 to -3); exp2: types 4, 5, 6 (ipsilateral 1 spot,
    contralateral 1 spot, bilateral 4 spots, Experiment 2 of the Methods); exp2b: types 4, 5, 7;
    exp3: types 7, 8, 9 (Experiment 3); ccx: types 10 to 12 (callosotomy).
    """
    st = set(np.unique(s["stim_type"][s["good"] & np.isfinite(s["stim_type"])]).astype(int).tolist())
    if st & {10, 11, 12} or s["mouse"] in CCX_MICE:
        return "ccx"
    if st & {1, 2, 3, -1, -2, -3}:
        return "unilateral"
    if st & {8, 9}:
        return "exp3"
    if 6 in st:
        return "exp2"
    if 7 in st:
        return "exp2b"
    return "none"


# The seven callosotomy mice, named in analysis_compile_all_data_bilateralCCX.m (code); their
# sessions are also the only ones with photostimulus types 10 to 12.
CCX_MICE = {"ANM278733", "ANM270340", "ANM298738", "ANM298740", "ANM291063", "ANM291064", "ANM297634"}

def load_meta():
    """Per session, the fields of meta_data_<session>.mat (in data/meta_data_files.zip, read in
    place) that the analysis uses: the mouse's gene modification, sex, and the recording
    coordinates."""
    import zipfile
    url = f"{BUCKET}/{PREFIX}data/meta_data_files.zip"
    out = {}
    with fsspec.open(url, "rb", block_size=2**20) as f:
        z = zipfile.ZipFile(f)
        for name in z.namelist():
            m = re.search(r"meta_data_(ANM\d+_\d+)\.mat$", name)
            if not m:
                continue
            md = sio.loadmat(io.BytesIO(z.read(name)), squeeze_me=True, struct_as_record=False)["meta_data"]
            gm = md.animalGeneModification
            gm = " x ".join(str(x) for x in np.atleast_1d(gm))
            out[m.group(1)] = {"gene_modification": gm, "sex": str(md.sex),
                               "recording_coordinates": np.atleast_1d(md.extracellular.recordingCoordinates).astype(float).tolist(),
                               "photostim_wavelength": " ".join(str(x) for x in np.atleast_1d(md.photostim.photostimWavelength))}
    return out


def mouse_line(gene_modification):
    """VGAT-ChR2 or PV x ReaChR, from the meta data's gene modification."""
    if "VGAT" in gene_modification:
        return "VGAT-ChR2"
    if "PV" in gene_modification and "ReaChR" in gene_modification:
        return "PV x ReaChR"
    return gene_modification


def side(s):
    """+1 for instructed lick right (HitR, ErrR, NoLickR), -1 for lick left, 0 otherwise."""
    tt = s["trial_types"]
    r = tt["HitR"] | tt["ErrR"] | tt.get("NoLickR", False)
    l = tt["HitL"] | tt["ErrL"] | tt.get("NoLickL", False)
    return np.where(r, 1, np.where(l, -1, 0))


def base_trials(s, include_lick_early=False):
    """Trials usable for analysis: performing (GoodTrials), with epoch times, a response
    (correct or error), and, unless asked otherwise, not lick-early (code; FAQ of the data set)."""
    tt = s["trial_types"]
    ok = s["good"] & np.isfinite(s["cue"]) & np.isfinite(s["pole_in"]) & np.isfinite(s["pole_out"])
    ok &= tt["HitR"] | tt["ErrR"] | tt["HitL"] | tt["ErrL"]
    if not include_lick_early:
        ok &= ~tt["LickEarly"]
    return ok


def stable_trials(s, u):
    """The unit's stable trials: from its first to its last trial with a spike (code)."""
    ids = s["trial_ids"]
    return (ids >= u["first_trial"]) & (ids <= u["last_trial"])


# ---------------------------------------------------------------- spike counts

T0, T1 = -3.6, 2.3  # s from the go cue; 1 ms bins
NB = int(round((T1 - T0) * 1000))


def cum_counts(s, u, trials):
    """Cumulative 1 ms spike counts, cue aligned, for the given trial indices: (n, NB + 1)."""
    trials = np.asarray(trials, dtype=int)
    row = np.full(len(s["trial_ids"]), -1)
    row[trials] = np.arange(len(trials))
    ti = u["spike_trial_index"]
    r = row[ti]
    keep = r >= 0
    t = u["spike_time"][keep] - s["cue"][ti[keep]]
    r = r[keep]
    b = np.floor((t - T0) * 1000).astype(int)
    ok = (b >= 0) & (b < NB)
    M = np.zeros((len(trials), NB), dtype=np.int32)
    np.add.at(M, (r[ok], b[ok]), 1)
    C = np.zeros((len(trials), NB + 1), dtype=np.int32)
    np.cumsum(M, axis=1, out=C[:, 1:])
    return C


def window_counts(C, start, stop):
    """Spike counts in [start, stop) s from the cue, per trial; start and stop may be arrays."""
    a = np.clip(np.round((np.asarray(start) - T0) * 1000).astype(int), 0, NB)
    b = np.clip(np.round((np.asarray(stop) - T0) * 1000).astype(int), 0, NB)
    if a.ndim == 0:
        return C[:, b] - C[:, a]
    return C[np.arange(len(C)), b] - C[np.arange(len(C)), a]


PSTH_T = np.round(np.arange(-3.4, 2.0 + 1e-9, 0.005), 3)


def psth(C, width=0.2, times=PSTH_T):
    """Mean rate (spikes/s) in a boxcar of `width` s centred on each time, over the trials of C."""
    if len(C) == 0:
        return np.full(len(times), np.nan)
    a = np.round((times - width / 2 - T0) * 1000).astype(int)
    b = np.round((times + width / 2 - T0) * 1000).astype(int)
    return (C[:, b] - C[:, a]).mean(axis=0) / width


RATE_T = np.round(np.arange(-3.0, 2.0 + 1e-9, 0.05), 3)


def rate_pvalues(C_ctrl, C_stim, times=RATE_T, width=0.4):
    """Two-tailed t-test p-value per window (counts in `width` s centred on each time)."""
    from scipy import stats
    a = np.round((times - width / 2 - T0) * 1000).astype(int)
    b = np.round((times + width / 2 - T0) * 1000).astype(int)
    x = C_ctrl[:, b] - C_ctrl[:, a]
    y = C_stim[:, b] - C_stim[:, a]
    with np.errstate(invalid="ignore", divide="ignore"):
        p = stats.ttest_ind(x, y, axis=0).pvalue
    return p


def epoch_rates(s, C, trials):
    """Rates (spikes/s) in the sample, delay and response epochs for each trial of C.

    Response epoch: the 1.3 s after the cue (code). Epoch bounds per trial from the trial table.
    """
    cue = s["cue"][trials]
    pin = s["pole_in"][trials] - cue
    pout = s["pole_out"][trials] - cue
    sample = window_counts(C, pin, pout) / (pout - pin)
    delay = window_counts(C, pout, np.zeros_like(pout)) / (-pout)
    resp = window_counts(C, 0.0, 1.3) / 1.3
    return np.vstack([sample, delay, resp]).T


def recovery_time(sel_ctrl, sel_stim, times, t_off, t_end, rng, n_boot=1000, frac=0.2):
    """Bootstrap recovery time of selectivity (code, Fig. 1g and 2e sections).

    sel_ctrl, sel_stim: neurons x time selectivity (preferred minus non-preferred) on control
    and photoinhibition trials. For each bootstrap resample of neurons, the first time after
    photoinhibition offset `t_off` (and before `t_end`) at which the mean of (control minus
    photoinhibition) over the mean control selectivity is below `frac` (i.e. 80% recovered).
    Returns (mean, std over the resamples that recover, fraction of resamples that recover, mean
    with resamples that do not recover counted at `t_end`), times from offset. The last is how
    the code's MATLAB arrays behave: a resample that does not recover leaves a zero (the cue
    time) in T_recovery when a later resample recovers.
    """
    n = len(sel_ctrl)
    win = (times > t_off) & (times < t_end)
    sel_ctrl, sel_stim, tw = sel_ctrl[:, win], sel_stim[:, win], times[win]
    out = []
    for _ in range(n_boot):
        i = rng.integers(0, n, n)
        r = (sel_ctrl[i] - sel_stim[i]).mean(0) / sel_ctrl[i].mean(0)
        hit = np.flatnonzero(r < frac)
        out.append(tw[hit[0]] - t_off if len(hit) else np.nan)
    out = np.array(out)
    ok = np.isfinite(out)
    censored = float(np.where(ok, out, t_end - t_off).mean())
    if not ok.any():
        return np.nan, np.nan, 0.0, censored
    sd = float(out[ok].std(ddof=1)) if ok.sum() > 1 else np.nan
    return float(out[ok].mean()), sd, float(ok.mean()), censored


# ---------------------------------------------------------------- per-session tables

BIN = 0.01  # s; counts are kept in 10 ms bins from T0 to T1 (cue aligned)
NB10 = int(round((T1 - T0) / BIN))
BIN_T = np.round(T0 + BIN * np.arange(NB10 + 1), 3)  # bin edges


def trial_table(s):
    """One row per trial with its side, outcome, photostimulus type and epoch times."""
    import pandas as pd
    tt = s["trial_types"]
    return pd.DataFrame({
        "session": s["name"], "mouse": s["mouse"], "trial": np.arange(len(s["trial_ids"])),
        "side": side(s), "hit": tt["HitR"] | tt["HitL"], "err": tt["ErrR"] | tt["ErrL"],
        "nolick": tt.get("NoLickR", np.zeros(len(side(s)), bool)) | tt.get("NoLickL", np.zeros(len(side(s)), bool)),
        "lick_early": tt["LickEarly"], "good": s["good"], "stim": s["stim_type"],
        "pole_in": s["pole_in"], "pole_out": s["pole_out"], "cue": s["cue"],
        "laser_on": s["laser_on"], "laser_off": s["laser_off"], "laser_max": s["laser_max"],
        "first_lick": s["first_lick"],
    })


def reduce_units(s):
    """Per unit: 10 ms binned counts and epoch rates on the session's usable trials.

    The trials kept are base_trials(s, include_lick_early=True), so that lick-early trials can be
    shown as a reading; `lick_early` marks them. `stable` marks the unit's stable trials.
    """
    trials = np.flatnonzero(base_trials(s, include_lick_early=True))
    out = []
    for k, u in enumerate(s["units"]):
        C = cum_counts(s, u, trials)
        edges = np.round((BIN_T - T0) * 1000).astype(int)
        binned = np.diff(C[:, edges], axis=1)
        assert binned.size == 0 or binned.max() < 256
        binned = binned.astype(np.uint8)
        out.append({
            "session": s["name"], "mouse": s["mouse"], "unit": k, "experiment": experiment(s),
            "cell_type": "pyramidal" if u["cell_type"] == ["pyramidal"] else ("FS" if u["cell_type"] == ["FS"] else ("none" if not u["cell_type"] else "/".join(u["cell_type"]))),
            "spike_width_ms": u["spike_width_ms"], "n_spikes": u["n_spikes"], "channel": u["channel"],
            "trials": trials, "stable": stable_trials(s, u)[trials], "binned": binned,
            "epoch_rates": epoch_rates(s, C, trials),
            "response_rate_1p5": window_counts(C, 0.0, 1.5) / 1.5,
        })
    return out


# ---------------------------------------------------------------- per-unit measures from 10 ms bins

GRID_T = np.round(np.arange(-3.5, 2.2 + 1e-9, 0.01), 3)  # time points for rates and PSTHs


def binned_window(binned, times, width):
    """Counts in windows of `width` s centred on `times` (multiples of 10 ms), per trial; windows
    are cut at the ends of the binned range (3.6 s before to 2.3 s after the cue)."""
    cs = np.zeros((binned.shape[0], binned.shape[1] + 1), dtype=np.int32)
    np.cumsum(binned, axis=1, out=cs[:, 1:])
    a = np.clip(np.round((np.asarray(times) - width / 2 - T0) / BIN).astype(int), 0, NB10)
    b = np.clip(np.round((np.asarray(times) + width / 2 - T0) / BIN).astype(int), 0, NB10)
    return cs[:, b] - cs[:, a]


def unit_measures(u, s, n_screen, conditions, seed, width_psth=0.2, screen="per_type"):
    """Measures of one unit used by the selectivity and rate analyses (code; see module doc).

    n_screen: control trials drawn at random to set the preferred trial type (5 per side in the
    unilateral code, 10 per side in the bilateral and callosotomy code; the Methods say "a subset
    of 10 trials"). screen = "per_type" draws n_screen trials of each type (M4 reading a);
    screen = "total" draws n_screen control trials in all, whatever their type (M4 reading b).
    Preference from the spike count from sample onset to 1.3 s after the cue (code, first column
    of spk_count_*_screen; M4 reading a), and, as `pref_best`, from the epoch (sample, delay or
    response) where the screening trials differ most between types, by the difference of means
    over the pooled standard deviation (M4 reading b; the measure of "most selective" is a
    standard choice). Selectivity traces on the remaining control trials.
    """
    from scipy import stats
    tr = u["trials"]
    sd = side(s)[tr]
    st = s["stim_type"][tr]
    le = s["trial_types"]["LickEarly"][tr]
    hit = (s["trial_types"]["HitR"] | s["trial_types"]["HitL"])[tr]
    ok = u["stable"] & ~le
    b = u["binned"]
    ctrl = ok & (st == 0)
    iR, iL = np.flatnonzero(ctrl & (sd == 1)), np.flatnonzero(ctrl & (sd == -1))
    out = {"nR": len(iR), "nL": len(iL)}
    rate = binned_window(b, GRID_T, width_psth) / width_psth
    out["fr_mean"] = float(binned_window(b[np.r_[iR, iL]], [-0.5], 5.0).mean() / 5.0) if len(iR) + len(iL) else np.nan
    rng = np.random.default_rng(seed)
    if screen == "per_type":
        enough = len(iR) > n_screen and len(iL) > n_screen
        if enough:
            pR, pL = rng.permutation(iR), rng.permutation(iL)
            sR, sL, tR, tL = pR[:n_screen], pL[:n_screen], pR[n_screen:], pL[n_screen:]
    else:
        pick = rng.permutation(np.r_[iR, iL])[:n_screen]
        sR, sL = np.intersect1d(pick, iR), np.intersect1d(pick, iL)
        tR, tL = np.setdiff1d(iR, pick), np.setdiff1d(iL, pick)
        # a preference needs screening trials of both types, and the trace test trials of both
        enough = len(iR) + len(iL) > n_screen and min(len(sR), len(sL), len(tR), len(tL)) > 0
    if enough:
        er = u["epoch_rates"]
        cue = s["cue"][tr]
        whole = (s["pole_in"][tr] - cue)
        # spike count from sample onset to 1.3 s after the cue: the rates times epoch lengths
        dur = np.vstack([s["pole_out"][tr] - s["pole_in"][tr], cue - s["pole_out"][tr], np.full(len(tr), 1.3)]).T
        counts = er * dur
        whole_count = counts.sum(1)
        out["pref_counts"] = np.r_[whole_count[sR].mean() - whole_count[sL].mean(), (counts[sR].mean(0) - counts[sL].mean(0))]
        diff = er[sR].mean(0) - er[sL].mean(0)
        spread = np.sqrt((er[sR].var(0) + er[sL].var(0)) / 2) + 1e-9
        best = int(np.argmax(np.abs(diff) / spread))
        out["pref_best"] = (best, 1 if diff[best] >= 0 else -1)
        out["psth_ctrl"] = {1: rate[tR].mean(0), -1: rate[tL].mean(0)}
        out["n_test"] = (len(tR), len(tL))
    else:
        out["pref_counts"] = None
        out["pref_best"] = None
    out["psth_ctrl_all"] = {1: rate[iR].mean(0) if len(iR) else None, -1: rate[iL].mean(0) if len(iL) else None}
    out["cond"] = {}
    for c in conditions:
        m = ok & (st == c)
        cR, cL = np.flatnonzero(m & (sd == 1)), np.flatnonzero(m & (sd == -1))
        d = {"nR": len(cR), "nL": len(cL),
             "psth": {1: rate[cR].mean(0) if len(cR) else None, -1: rate[cL].mean(0) if len(cL) else None}}
        if len(cR) > 3 and len(cL) > 3 and len(iR) + len(iL) > 1:
            x = binned_window(b[np.r_[iR, iL]], RATE_T, 0.4)
            y = binned_window(b[np.r_[cR, cL]], RATE_T, 0.4)
            with np.errstate(invalid="ignore", divide="ignore"):
                d["p_rate"] = stats.ttest_ind(x, y, axis=0).pvalue
        else:
            d["p_rate"] = None
        out["cond"][c] = d
    # selectivity tests (Methods; code): epoch rates, lick right against lick left
    er = u["epoch_rates"]
    with np.errstate(invalid="ignore", divide="ignore"):
        for name, trials_ok in (("all", ctrl), ("correct", ctrl & hit), ("all_le", u["stable"] & (st == 0))):
            r_, l_ = np.flatnonzero(trials_ok & (sd == 1)), np.flatnonzero(trials_ok & (sd == -1))
            if len(r_) > 1 and len(l_) > 1:
                p = stats.ttest_ind(er[r_], er[l_], axis=0).pvalue
                p15 = stats.ttest_ind(u["response_rate_1p5"][r_], u["response_rate_1p5"][l_]).pvalue
                # response epoch read as the first 400 ms after the cue
                b4 = binned_window(b, [0.2], 0.4)[:, 0] / 0.4
                p04 = stats.ttest_ind(b4[r_], b4[l_]).pvalue
                out[f"p_sel_{name}"] = np.r_[p, p04, p15]
            else:
                out[f"p_sel_{name}"] = np.full(5, np.nan)
    return out


# ---------------------------------------------------------------- population analyses

POP_T = np.round(np.arange(-3.5, 1.0 + 1e-9, 0.01), 3)  # window starts; windows [t, t + 0.4]


def population_session(s, sess_units, conds, cell_types=("pyramidal",), seed=0, split="code", min_group=5):
    """Trials x neurons x windows rates for one session, with the code's trial selection.

    Neurons: units of `cell_types` whose stable trials include trial 50 and the 50th from the end
    (code, analysis_compile_all_data_bilateral_activityModes.m). Trials: performing, not
    lick-early, stable for every neuron, correct and error grouped by instructed movement.
    Rates: spike counts in 400 ms windows starting every 10 ms from 3.5 s before to 1 s after the
    cue, over 0.4 s (Methods; code). Control trials are split into a training set (for cd, the
    decision boundary and the offset) and a test set: split = "code", as many test trials of each
    type as the mean number of photoinhibition trials per type and condition (code); split =
    "half", one random half of each type (M6 reading a); split = "loo", every control trial is both
    a training and a test trial, and the analysis leaves the test trial out of the training set
    (M6 reading b).
    Returns None when the session has 5 or fewer neurons or fewer than `min_group` trials in a
    group. The code keeps groups of 5 trials (min_group = 5), which gives the paper's 16 sessions;
    the Methods' "> 5 trials per condition" (M6) is min_group = 6, shown as a reading.
    """
    n_tr = len(s["trial_ids"])
    keep = []
    for u in sess_units:
        su = s["units"][u["unit"]]
        if u["cell_type"] not in cell_types:
            continue
        ids = s["trial_ids"]
        if not (su["first_trial"] <= 50 <= su["last_trial"] and su["first_trial"] <= ids[-1] - 50 <= su["last_trial"]):
            continue
        keep.append(u)
    if not keep:
        return None
    trials = keep[0]["trials"]
    stable = np.all([u["stable"] for u in keep], axis=0)
    sd = side(s)[trials]
    st = s["stim_type"][trials]
    le = s["trial_types"]["LickEarly"][trials]
    hit = (s["trial_types"]["HitR"] | s["trial_types"]["HitL"])[trials]
    ok = stable & ~le & (sd != 0)
    groups = {(c, d): np.flatnonzero(ok & (st == c) & (sd == d)) for c in [0] + list(conds) for d in (1, -1)}
    rng = np.random.default_rng(seed)
    n_test = int(round(np.mean([len(groups[(c, d)]) for c in conds for d in (1, -1)])))
    train, test = {}, {}
    for d in (1, -1):
        g = rng.permutation(groups[(0, d)])
        if split == "loo":
            test[d], train[d] = g, g
            continue
        n_t = n_test if split == "code" else len(g) // 2
        test[d], train[d] = g[len(g) - n_t:], g[:len(g) - n_t]
    counts = [len(train[1]), len(train[-1]), len(test[1]), len(test[-1])] + [len(groups[(c, d)]) for c in conds for d in (1, -1)]
    if len(keep) <= 5 or min(counts) < min_group:
        return None
    X = np.stack([binned_window(u["binned"], POP_T + 0.2, 0.4) / 0.4 for u in keep], axis=1)  # trials x neurons x windows
    return {"session": s["name"], "mouse": s["mouse"], "X": X, "split": split, "side": sd, "hit": hit, "stim": st,
            "train": train, "test": test, "groups": groups, "n_neurons": len(keep), "counts": counts,
            "trials": trials}


def lda_direction(XR, XL):
    """Fisher discriminant direction (code, func_discriminant.m), sign so that R projects higher."""
    x = np.vstack([XL, XR])
    xm = x.mean(0)
    xc = x - xm
    T = xc.T @ xc
    W = np.zeros_like(T)
    for g in (XL, XR):
        z = g - g.mean(0)
        W += z.T @ z
    B = T - W
    _, _, vt = np.linalg.svd(np.linalg.pinv(W) @ B)
    v = vt[0]
    if (XR @ v).mean() < (XL @ v).mean():
        v = -v
    return v


def boundary(pR, pL):
    """Decision boundary: inverse-variance weighted mean of the two class means (Methods; code)."""
    vR, vL = np.var(pR, ddof=1), np.var(pL, ddof=1)
    return (pR.mean() / vR + pL.mean() / vL) / (1 / vR + 1 / vL)


def auc(a, b):
    """Area under the ROC curve for separating a (positive) from b."""
    from scipy.stats import mannwhitneyu
    if len(a) == 0 or len(b) == 0:
        return np.nan
    return mannwhitneyu(a, b).statistic / (len(a) * len(b))
