"""Loading and measures for dandiset 001262, single auditory nerve fibres of gerbils.

Heeringa (2024), Scientific Data 11, 411, doi:10.1038/s41597-024-03259-3.

Each NWB file holds one single unit (fibre) of one gerbil. A file holds, per trial, the spike
times (`units`, one row per trial, tagged `<TYPE>_<condition>_rep<n>`), the trial's stimulus
(`intracellular_recordings/stimuli`: recording type, frequency, level, delay, duration), the raw
voltage trace (`acquisition`, not read here), and a small analysis table with one row per
recording type (`results_bf`, `results_sr`, `results_threshold`). Animal metadata are in
`general/subject` (age, sex, weight), `general/surgery` (oxygen) and `general/notes` (ABR).
Files are streamed from the archive at the pinned version; nothing is written to disk. The
voltage traces are not read: no claim tested here needs them.

Where the parameters come from:

- Age groups: young adult <= 365 days, middle aged > 365 and <= 1095, old > 1095; months are
  days / (365/12). Claims file, from check_dataset_metadata.m and check_dataset_units.m
  (Zenodo 10.5281/zenodo.10370064).
- Best estimate of spontaneous rate: the SR recording, else PH, else RLF, else BF (claims file,
  from check_dataset_units.m; Methods, "Calculating spike rate": "For units without data in the
  'SR' field, the author advises choosing ... the PH recording ..., followed by the RLF
  recording"). Low-SR is SR < 18 spikes/s (Fig. 6d legend).
- `vector_strength_by_level` follows PHextract_func.m and TytoView_calcVS.m (Zenodo record
  above), which the Methods name ("The analysis procedures were carried out by the function
  PHextract_func.m"): spikes between stimulus onset and offset (strict inequalities), pooled
  over the repetitions of a level; vs = |mean(exp(i 2 pi f t))|; p = exp(-N vs^2); p is NaN
  when N <= 50 (the code's `ntot > 50`; the Methods say "When N < 50, the p-value is NaN").
  Significant when p < 0.001 (Methods). The silent trials are left out (the code also computes
  a value for them; it is not a tone level).
- `cf_from_cf_recording` follows CFextract_func.m, getSpikeCounts.m and getQ10dB.m, which the
  Methods name: rates in the stimulus window per trial, mean over repetitions per frequency and
  level; response criterion T = mean + 1.2 x SD (population SD, `std(y,1,2)`) of the rates of
  the silent trials, and also above 15 spikes/s; a frequency's threshold is the lower level of
  the first pair of adjacent suprathreshold levels, or the only suprathreshold level; CF is the
  mean of the frequencies at the lowest threshold. The code then asks the experimenter to accept
  T and the CF or type new ones ("T could be manually adjusted when needed", Methods); those
  manual choices are not in the dataset, so this is the automatic first pass only.
- `click_latency_2bins` follows Clickextract_func.m and getFSL2bins.m, named by the Methods:
  only recordings with more than 75 spikes are analysed; the PSTH of all spikes has
  round(trial duration / 0.05 ms) bins spanning the first to the last spike (MATLAB `hist`);
  the reference is the largest bin before the click, leaving out the first 10 bins; the
  latency is the centre of the first of two consecutive bins after the click that exceed it,
  minus the click delay. The click delay is not in the files (the trial table gives NaN), so it
  is a parameter: `CLICK_DELAY_S` is an assumption, the 7.75 ms delay that every tone recording
  in the dataset uses, and the notebook shows another value.
- Inter-spike intervals: within a trial, between successive spike times, as checkAN.m computes
  them (`diff(spT)` per trial); the 0.6 ms limit is the Technical Validation's.
"""

from __future__ import annotations

import re
import time
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "001262"
DANDISET_VERSION = "0.241205.0959"
API = "https://api.dandiarchive.org/api"

YOUNG_MAX_DAYS = 365
MIDDLE_MAX_DAYS = 3 * 365
DAYS_PER_MONTH = 365 / 12
LOW_SR_CUTOFF = 18.0          # spikes/s, Fig. 6d legend
VS_P_SIGNIFICANT = 0.001      # Methods
VS_MIN_SPIKES = 50            # TytoView_calcVS.m: p only when N > 50
CF_SD_FACTOR = 1.2            # Methods and CFextract_func.m
CF_MIN_RATE = 15.0            # CFextract_func.m (m > 15)
CLICK_MIN_SPIKES = 75         # Clickextract_func.m
CLICK_BIN_S = 0.00005         # 0.05 ms, Methods
CLICK_DELAY_S = 0.00775       # assumption, see the module docstring
SHORT_ISI_S = 0.0006          # Technical Validation
SPONT = -99999.0              # frequency and level of silent trials


def age_group(days):
    if days <= YOUNG_MAX_DAYS:
        return "young"
    if days <= MIDDLE_MAX_DAYS:
        return "middle"
    return "old"


def list_assets(version=DANDISET_VERSION):
    """Assets of the pinned version: path, asset id, blob id and size."""
    out, url = [], f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000"
    while url:
        page = requests.get(url, timeout=60).json()
        out += page["results"]
        url = page["next"]
    return pd.DataFrame([{"path": a["path"], "asset_id": a["asset_id"], "blob": a.get("blob"),
                          "size": a["size"]} for a in out])


def blob_url(blob):
    return f"https://dandiarchive.s3.amazonaws.com/blobs/{blob[:3]}/{blob[3:6]}/{blob}"


def _s(v):
    if isinstance(v, np.ndarray) and v.shape == ():
        v = v[()]
    if isinstance(v, bytes):
        return v.decode("utf-8", "surrogateescape")
    return v


def read_unit(asset):
    """Read one file's metadata, analysis table, trial table and spike times (no traces)."""
    with h5py.File(remfile.File(blob_url(asset["blob"])), "r") as f:
        g = f["general"]
        d = {"path": asset["path"], "blob": asset["blob"], "size": asset["size"]}
        for key, name in [("subject_id", "subject/subject_id"), ("age", "subject/age"),
                          ("sex", "subject/sex"), ("weight", "subject/weight"),
                          ("species", "subject/species"), ("notes", "notes"),
                          ("surgery", "surgery"), ("session_id", "session_id")]:
            d[key] = _s(g[name][()]) if name in g else None
        d["identifier"] = _s(f["identifier"][()])
        d["session_start"] = _s(f["session_start_time"][0])
        d["stimulus_description"] = _s(f["stimulus/presentation/stimulus"].attrs.get("description"))
        at = f["analysis/analysis_table"]
        d["analysis"] = pd.DataFrame({
            "experiment": [_s(v) for v in at["experiment"][:]],
            "bf": at["results_bf"][:], "sr": at["results_sr"][:],
            "threshold": at["results_threshold"][:]})
        st = f["general/intracellular_ephys/intracellular_recordings/stimuli"]
        lv, lvi = st["level_dBSPL"][:], st["level_dBSPL_index"][:]
        lv_start = np.r_[0, lvi[:-1]]
        first_level = np.array([lv[a] if b > a else np.nan for a, b in zip(lv_start, lvi)])
        n_levels = lvi - lv_start
        tags = [_s(v) for v in f["units/tag"][:]]
        trials = pd.DataFrame({
            "tag": tags,
            "experiment": [_s(v) for v in st["experiment_name"][:]],
            "frequency": st["frequency"][:], "level": first_level, "n_levels": n_levels,
            "delay": st["delay"][:], "duration": st["duration"][:],
            "click_polarity": [_s(v) for v in st["click_polarity"][:]],
        })
        d["sequential_types"] = [_s(v) for v in
                                 f["general/intracellular_ephys/sequential_recordings/stimulus_type"][:]]
        sp = f["units/spike_times"][:]
        idx = f["units/spike_times_index"][:]
        starts = np.r_[0, idx[:-1]]
        spikes = [sp[a:b] for a, b in zip(starts, idx)]
        d["n_nan_spikes"] = int(sum(np.isnan(s).sum() for s in spikes))
        d["spikes"] = [s[~np.isnan(s)] for s in spikes]
        trials["n_spikes"] = [len(s) for s in d["spikes"]]
        # trial length per recording type, from the shape of its first voltage trace
        acq = f["acquisition"]
        trial_s = {}
        for exp in trials.experiment.unique():
            tag = trials.tag[trials.experiment == exp].iloc[0]
            if tag in acq:
                ser = acq[tag]
                rate = ser["starting_time"].attrs["rate"]
                trial_s[exp] = ser["data"].shape[0] / rate
        trials["trial_s"] = trials.experiment.map(trial_s)
        d["acq_rate"] = float(acq[tags[0]]["starting_time"].attrs["rate"]) if tags[0] in acq else np.nan
        d["acq_unit"] = _s(acq[tags[0]]["data"].attrs.get("unit")) if tags[0] in acq else None
        d["trials"] = trials
    return d


def _read_with_retries(asset, retries=4):
    for attempt in range(retries):
        try:
            return read_unit(asset)
        except Exception as err:  # network errors: retry
            last = err
            time.sleep(3 * (attempt + 1))
    raise last


def load_all(assets, workers=24):
    """Read every file in `assets` (a DataFrame from list_assets) with a process pool.

    h5py holds a global lock, so threads do not read files in parallel; processes do.
    """
    rows = [dict(r) for _, r in assets.iterrows()]
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_read_with_retries, rows, chunksize=1))


# --- metadata parsing --------------------------------------------------------------------

def age_days(age):
    m = re.fullmatch(r"P(\d+(?:\.\d+)?)D", age or "")
    return float(m.group(1)) if m else np.nan


def weight_g(weight):
    m = re.fullmatch(r"\s*([0-9.eE+-]+)\s*g\s*", weight or "")
    return float(m.group(1)) if m else np.nan


def oxygen(surgery):
    m = re.search(r"oxygen:\s*(\w+)", surgery or "")
    return m.group(1) if m else None


def speaker(stimulus_description):
    m = re.search(r"speaker:\s*(.+)$", stimulus_description or "")
    return m.group(1).strip() if m else None


def abr_field(notes):
    """The text after 'threshold (db SPL): ' in the notes."""
    m = re.search(r"threshold \(db SPL\): (.*)$", notes or "", flags=re.S)
    return m.group(1) if m else None


def abr_decoded(field):
    """The ABR field holds one character whose code point is the threshold (see notebook).

    Returns the code point of a single character, NaN for 'NaN' or an empty field.
    """
    if field is None or field == "" or field == "NaN":
        return np.nan
    if len(field) == 1:
        return float(ord(field))
    try:
        return float(field)
    except ValueError:
        return np.nan


# --- measures from spike times ------------------------------------------------------------

def trials_of(unit, experiment):
    t = unit["trials"]
    idx = np.flatnonzero(t.experiment.values == experiment)
    return t.iloc[idx], [unit["spikes"][i] for i in idx]


def vs_calc(spike_times_s, freq):
    """TytoView_calcVS.m: vector strength and p (NaN when N <= 50)."""
    n = len(spike_times_s)
    if n == 0:
        return np.nan, np.nan, 0
    ph = 2 * np.pi * freq * spike_times_s
    vs = float(np.hypot(np.cos(ph).mean(), np.sin(ph).mean()))
    p = float(np.exp(-n * vs * vs)) if n > VS_MIN_SPIKES else np.nan
    return vs, p, n


def vector_strength_by_level(unit):
    """PHextract_func.m: vector strength and p per tone level of the PH recording."""
    t, sp = trials_of(unit, "PH")
    if len(t) == 0:
        return None
    tone = t.frequency.values != SPONT
    freqs = np.unique(t.frequency.values[tone])
    rows = []
    for lvl in np.unique(t.level.values[tone]):
        sel = np.flatnonzero(tone & (t.level.values == lvl))
        start, dur = t.delay.values[sel[0]], t.duration.values[sel[0]]
        s = np.concatenate([sp[i] for i in sel]) if len(sel) else np.array([])
        s = s[(s > start) & (s < start + dur)]
        vs, p, n = vs_calc(s, freqs[0])
        rows.append({"level": lvl, "frequency": freqs[0], "n_freqs": len(freqs), "vs": vs, "p": p,
                     "n_spikes": n})
    return pd.DataFrame(rows)


def max_significant_vs(unit):
    """check_dataset_units.m: largest vs over levels with p not NaN and < 0.001."""
    v = vector_strength_by_level(unit)
    if v is None:
        return np.nan
    ok = v.p.notna() & (v.p < VS_P_SIGNIFICANT)
    return float(v.vs[ok].max()) if ok.any() else np.nan


def _rates(t, sp):
    start, dur = t.delay.values, t.duration.values
    return np.array([np.sum((s > a) & (s < a + d)) / d for s, a, d in zip(sp, start, dur)])


def cf_from_cf_recording(unit, level_from="tag"):
    """CFextract_func.m, automatic first pass: (CF in Hz, threshold, tuning curve)."""
    t, sp = trials_of(unit, "CF")
    if len(t) == 0:
        return np.nan, np.nan, None
    t = t.copy()
    t["rate"] = _rates(t, sp)
    if level_from == "tag":
        # nominal attenuator level (ABI) from the tag, as the code's depvars use
        abi = t.tag.str.extract(r"ABI(-?\d+(?:\.\d+)?)")[0].astype(float)
        if abi.notna().sum() == (t.frequency != SPONT).sum():
            t["lv"] = abi.where(t.frequency != SPONT, SPONT)
        else:
            t["lv"] = t.level
    else:
        t["lv"] = t.level
    spont = t[t.frequency == SPONT]
    if len(spont) == 0:
        return np.nan, np.nan, None
    resp = spont.rate.mean() + CF_SD_FACTOR * spont.rate.std(ddof=0)
    m = t[t.frequency != SPONT].groupby(["frequency", "lv"]).rate.mean().unstack("lv").sort_index()
    m = m.reindex(columns=sorted(m.columns))
    levels = np.array(m.columns, dtype=float)
    tc = np.full(len(m), np.nan)
    for i, row in enumerate(m.values):
        xi = np.flatnonzero((row > resp) & (row > CF_MIN_RATE))
        if len(xi) > 1:
            xn = np.flatnonzero(np.diff(xi) == 1)
            tc[i] = levels[xi[xn[0]]] if len(xn) else np.nan
        elif len(xi) == 1:
            tc[i] = levels[xi[0]]
    if np.all(np.isnan(tc)):
        return np.nan, np.nan, pd.Series(tc, index=m.index)
    thr = np.nanmin(tc)
    cf = float(np.mean(np.array(m.index)[tc == thr]))
    return cf, float(thr), pd.Series(tc, index=m.index)


def _matlab_hist(x, nbin):
    """MATLAB hist(x, nbin): nbin equal bins from min(x) to max(x); returns counts, centres."""
    lo, hi = float(np.min(x)), float(np.max(x))
    if hi == lo:
        lo, hi = lo - 0.5, hi + 0.5
    edges = np.linspace(lo, hi, nbin + 1)
    counts, _ = np.histogram(x, edges)
    return counts, (edges[:-1] + edges[1:]) / 2


def click_latency_2bins(unit, delay=CLICK_DELAY_S):
    """Clickextract_func.m and getFSL2bins.m on the unit's CLICK trials (seconds)."""
    t, sp = trials_of(unit, "CLICK")
    if len(t) == 0:
        return np.nan
    n_sp = sum(len(s) for s in sp)
    if n_sp <= CLICK_MIN_SPIKES:
        return np.nan
    dur = float(t.trial_s.iloc[0])
    nbin = int(round(dur / CLICK_BIN_S))
    allsp = np.concatenate(sp)
    counts, cent = _matlab_hist(allsp, nbin)
    rate = counts / len(t) / CLICK_BIN_S
    sfr = cent < delay
    sfr[:10] = False
    efr = np.flatnonzero(cent > delay)
    thr = rate[sfr].max() if sfr.any() else 1.0
    high = efr[rate[efr] > thr]
    consec = np.flatnonzero(np.diff(high) == 1)
    if len(consec) == 0:
        return np.nan
    return float(cent[high[consec[0]]] - delay)


def short_isis(unit, limit=SHORT_ISI_S):
    """Per recording type: number of within-trial ISIs below `limit`, and of all ISIs."""
    out = {}
    t = unit["trials"]
    for exp in t.experiment.unique():
        idx = np.flatnonzero(t.experiment.values == exp)
        isis = [np.diff(np.sort(unit["spikes"][i])) for i in idx]
        isis = np.concatenate(isis) if isis else np.array([])
        out[exp] = (int(np.sum(isis < limit)), len(isis))
    return out


def rlf_rates(unit):
    """Mean and SD of the rate per level of the RLF recording (stimulus window), spont apart."""
    t, sp = trials_of(unit, "RLF")
    if len(t) == 0:
        return None
    t = t.copy()
    t["rate"] = _rates(t, sp)
    return t[t.frequency != SPONT].groupby("level").rate.agg(["mean", "std", "size"])
