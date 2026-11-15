"""Loading and measures for the human MTL recognition memory data of dandiset 000004.

Chandravadia, Liang, Schjetnan et al. (2020), Scientific Data 7, 78, doi:10.1038/s41597-020-0415-9.

Each NWB file holds one session: a trials table (100 encoding and 100 recognition trials),
the TTL event markers and the experiment id of each marker, the electrodes table, the units
table (spike times, mean waveforms, quality metrics) and the stimulus images. Files are
streamed from the archive at the pinned version; nothing is written to disk, and the
stimulus images are not read (only their shape).

Where the parameters come from:

- Recognition trials are the rows with stim_phase "recog"; the confidence response is
  response_value minus 30 (claims file, opening comment). The paper's code reads it from the
  events (events of the recognition experiment id between 30 and 36, minus 30;
  helper.extract_recog_responses in rutishauserlab/recogmem-release-NWB at commit 1d95162);
  `check_responses_against_events` compares the two.
- "Old" is new_old_labels_recog == 1, as in the paper's code (claims file; tested in claim
  new-old-label-coding).
- Firing rate: spikes strictly inside (onset + start, onset + end) divided by the window
  length, as `Trial.win_spike_rate` in single_neuron.py of the paper's code. The Methods'
  window is 0.2 to 1.2 s after stimulus onset (Technical Validation, "a 1 s long window
  starting 200 ms after stimulus onset"); the code's is 0.2 to 1.7 s (single_neuron.py,
  vs_test and ms_test). Stimulus onset is the trial's start_time, as in the code
  (extract_neuron_data_from_nwb).
- VS cells: one-way ANOVA (scipy f_oneway) of the recognition-trial rates across the
  stimCategory values, P < 0.05 (Technical Validation; single_neuron.py vs_test).
- MS cells: the bootstrap test of the paper's code (single_neuron.py ms_test, the same as
  bootstrapMeanEqualTest.m mode 1 without variance correction, Efron and Tibshirani
  algorithm 16.2): both groups shifted to the pooled mean, each resampled with replacement
  within itself, 1000 runs, p = fraction of runs with |mean difference| >= the observed one.
  The seed is a standard choice (it cannot change a result beyond the resampling noise).
- Behaviour: cumulative ROC over the six confidence levels from "old, confident" down,
  hit and false alarm rates adjusted for 0 and 1 (adjustHF), AUC by the trapezoid rule with
  (0,0) and (1,1) added (helper.cal_cumulative_d, cal_auc; calcROC_AUC.m), z-ROC slope by
  regressing z(H) on z(F) over the five interior points (calcZROCSlope.m). High/low
  confidence accuracy by the fixed split of NO_behavior_evaluateSessionStatus.m (high = 1
  or 6, low = 2 to 5) and the dynamic split of helper.dynamic_split (claims file).
"""

from __future__ import annotations

import re
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "000004"
DANDISET_VERSION = "0.220126.1852"

METHODS_WINDOW = (0.2, 1.2)   # s after stimulus onset; Technical Validation
CODE_WINDOW = (0.2, 1.7)      # s; single_neuron.py vs_test / ms_test
N_BOOT = 1000                 # Technical Validation, "bootstrap comparison of means with 1,000 runs"
ALPHA = 0.05

# The paper's patient tables, read from Europe PMC's copy of the open access full texts.
PAPER_PMC = "PMC7055261"      # this paper, doi:10.1038/s41597-020-0415-9, Online-only Table 1
FARAUT_PMC = "PMC5810422"     # Faraut et al. 2018, doi:10.1038/sdata.2018.10, Table 1


def _s(x):
    if isinstance(x, bytes):
        return x.decode()
    if isinstance(x, np.ndarray) and x.shape == ():
        return _s(x[()])
    return x


def list_assets():
    """Paths and S3 URLs of the dandiset's NWB files at the pinned version."""
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    out = []
    for a in ds.get_assets():
        if a.path.endswith(".nwb"):
            out.append((a.path, a.get_content_url(follow_redirects=1, strip_query=True), a.size))
    return sorted(out)


def dandiset_metadata():
    client = DandiAPIClient()
    return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_raw_metadata()


def _table(g, skip=()):
    cols = {}
    for k in g:
        if k in skip or k == "id" or k.endswith("_index"):
            continue
        d = g[k]
        if not isinstance(d, h5py.Dataset) or d.ndim != 1:
            continue
        v = d[:]
        if v.dtype.kind in "OS":
            v = np.array([_s(x) for x in v], dtype=object)
        cols[k] = v
    df = pd.DataFrame(cols)
    df.index = g["id"][:]
    return df


def load_session(path, url):
    """Read one file: everything the analyses use, without the stimulus images."""
    with h5py.File(remfile.File(url), "r") as f:
        s = {"path": path}
        for k in ["identifier", "session_description", "session_start_time"]:
            s[k] = _s(f[k][()])
        for k in ["data_collection", "experiment_description", "institution", "lab"]:
            s[k] = _s(f["general"][k][()]) if k in f["general"] else None
        subj = f["general/subject"]
        s["subject"] = {k: _s(subj[k][()]) for k in subj}
        s["nwb_version"] = _s(f.attrs.get("nwb_version"))
        ev = f["acquisition/events"]
        s["events"] = np.array([float(_s(x)) for x in ev["data"][:]])
        s["events_t"] = ev["timestamps"][:]
        s["events_description"] = _s(ev.attrs.get("description"))
        ex = f["acquisition/experiment_ids"]
        s["expids"] = ex["data"][:]
        s["expids_t"] = ex["timestamps"][:]
        s["expids_description"] = _s(ex.attrs.get("description"))
        s["trials"] = _table(f["intervals/trials"])
        s["trials_columns"] = [_s(c) for c in f["intervals/trials"].attrs["colnames"]]
        s["label_description"] = " ".join(_s(f["intervals/trials/new_old_labels_recog"].attrs.get("description", "")).split())
        el = f["general/extracellular_ephys/electrodes"]
        s["electrodes"] = _table(el, skip=("group",))
        s["electrodes_columns"] = [_s(c) for c in el.attrs["colnames"]]
        s["imp_dtype"] = str(el["imp"].dtype) if "imp" in el else None
        u = f["units"]
        s["units_columns"] = [_s(c) for c in u.attrs["colnames"]]
        s["units_datasets"] = sorted(u.keys())
        s["unit_ids"] = u["id"][:]
        st = u["spike_times"][:]
        idx = u["spike_times_index"][:]
        s["spikes"] = np.split(st, idx[:-1])
        eidx = u["electrodes_index"][:]
        s["unit_electrodes"] = np.split(u["electrodes"][:], eidx[:-1])
        for k in ["origClusterID", "SNR", "IsolationDist", "IsolDist"]:
            if k in u:
                s[k] = u[k][:]
        s["waveform_rate"] = u["waveform_mean_sampling_rate"][:].ravel() if "waveform_mean_sampling_rate" in u else None
        for k in ["waveform_mean_encoding", "waveform_mean_recognition"]:
            s[k + "_shape"] = u[k].shape if k in u else None
        pres = f["stimulus/presentation"] if "stimulus/presentation" in f else {}
        s["stimulus_series"] = {k: (pres[k]["data"].shape if "data" in pres[k] else None) for k in pres}
    m = re.match(r"([A-Z]+)(\d+)_(\d+)$", s["identifier"])
    s["label"] = m.group(1) + m.group(2)
    s["session_id"] = int(m.group(3))
    m2 = re.search(r"ID:\s*(\d+)", s["session_description"] or "")
    s["session_id_description"] = int(m2.group(1)) if m2 else None
    return s


def retry(fn, *args, tries=4, wait=10, **kwargs):
    """Call fn, again after a pause when it raises (the archive and OSF sometimes answer 500 or
    time out); the last failure is raised."""
    for k in range(tries):
        try:
            return fn(*args, **kwargs)
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(wait * (k + 1))


def load_all(assets, workers=6):
    with ThreadPoolExecutor(workers) as ex:
        sessions = list(ex.map(lambda a: retry(load_session, a[0], a[1]), assets))
    return sorted(sessions, key=lambda s: s["session_id"])


def site(label):
    """CS (labels H or C) or TWH (labels T), as the Figure 5 legend defines."""
    return "TWH" if label.startswith("T") else "CS"


# --- the paper's patient tables ------------------------------------------------------------

def pmc_table(pmc, label):
    """Rows of the table with this label in Europe PMC's full-text XML of an article."""
    r = retry(requests.get, f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/fullTextXML", timeout=60)
    r.raise_for_status()
    root = ET.fromstring(r.content)
    for tw in root.iter("table-wrap"):
        lab = tw.find("label")
        if lab is not None and lab.text and lab.text.strip() == label:
            return [["".join(td.itertext()).strip() for td in tr] for tr in tw.iter("tr")]
    raise ValueError(f"{label} not found in {pmc}")


def patient_table(pmc, label):
    """Subject rows of a patient table: one row per (subject, session) with variant, age, sex, diagnosis."""
    rows = []
    for r in pmc_table(pmc, label):
        if len(r) < 7 or not re.match(r"^[HCT]\d+$", r[0]):
            continue
        sids = [int(x) for x in re.findall(r"\d+", r[2])]
        vars_ = [int(x) for x in re.findall(r"\d+", r[3])]
        for i, sid in enumerate(sids):
            rows.append({"label": r[0], "n_sessions": int(r[1]), "session_id": sid,
                         "variant": vars_[i] if i < len(vars_) else None,
                         "age": int(r[4]), "sex": r[5], "diagnosis": r[6]})
    return pd.DataFrame(rows)


def table_label(label):
    """File labels are P9HMH, P24CS, TWH088; the tables write H09, C24, T88."""
    m = re.match(r"P(\d+)(HMH|CS)$", label)
    if m:
        return ("H" if m.group(2) == "HMH" else "C") + f"{int(m.group(1)):02d}"
    m = re.match(r"TWH(\d+)$", label)
    if m:
        return f"T{int(m.group(1))}"
    return label


# --- trials and behaviour ------------------------------------------------------------------

def recog_trials(s):
    t = s["trials"]
    r = t[t["stim_phase"] == "recog"].copy()
    r["conf"] = r["response_value"] - 30
    r["label"] = pd.to_numeric(r["new_old_labels_recog"], errors="coerce")
    return r


def version_assets(version):
    """(path, blob id, size) of every asset of a version of the dandiset, from the archive's API."""
    url = f"https://api.dandiarchive.org/api/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        r = retry(requests.get, url, timeout=60)
        r.raise_for_status()
        d = r.json()
        out += [(a["path"], a["blob"], a["size"]) for a in d["results"]]
        url = d["next"]
    return sorted(out)


def check_responses_against_events(s):
    """The responses the paper's code reads from the events (recognition experiment id, codes 30 to 36).
    The recognition id is taken as the larger of the file's two experiment ids; the notebook checks
    that the learning trials carry the smaller id in every file (experiment-ids)."""
    ids = np.unique(s["expids"])
    recog_id = ids[1] if len(ids) > 1 else np.nan
    ev = s["events"][(s["expids"] == recog_id) & (s["events"] >= 30) & (s["events"] <= 36)] - 30
    return ev


def typecounters(label, conf):
    """Counts of old (label 1) and new (label 0) trials at each confidence, from 6 ('old, confident') down."""
    old = np.array([np.sum((conf == c) & (label == 1)) for c in range(6, 0, -1)])
    new = np.array([np.sum((conf == c) & (label == 0)) for c in range(6, 0, -1)])
    return old, new


def adjust_hf(h, f, n_old, n_new):
    """adjustHF.m: rates of 0 or 1 moved by half a trial."""
    h = np.where(h == 1, 1 - 1 / (2 * n_old), h)
    f = np.where(f == 1, 1 - 1 / (2 * n_new), f)
    h = np.where(h == 0, 1 / (2 * n_old), h)
    f = np.where(f == 0, 1 / (2 * n_new), f)
    return h, f


def cumulative_roc(label, conf):
    """Hit and false alarm rates at the six cumulative criteria (helper.cal_cumulative_d)."""
    old, new = typecounters(label, conf)
    n_old, n_new = old.sum(), new.sum()
    h = np.cumsum(old) / n_old
    f = np.cumsum(new) / n_new
    return adjust_hf(h, f, n_old, n_new)


def auc(h, f):
    """helper.cal_auc / calcROC_AUC.m: trapezoid rule with (0,0) and (1,1) added."""
    tp, fp = list(h), list(f)
    if tp[0] != 0 or fp[0] != 0:
        tp, fp = [0.0] + tp, [0.0] + fp
    if tp[-1] != 1 or fp[-1] != 1:
        tp, fp = tp + [1.0], fp + [1.0]
    a = 0.0
    for i in range(1, len(tp)):
        a += (fp[i] - fp[i - 1]) * tp[i - 1] + 0.5 * (tp[i] - tp[i - 1]) * (fp[i] - fp[i - 1])
    return a


def zroc_slope(h, f):
    """calcZROCSlope.m: regression of z(H) on z(F) over the first five cumulative points."""
    zh, zf = stats.norm.ppf(h[:5]), stats.norm.ppf(f[:5])
    if np.unique(zf).size < 2:
        return np.nan
    return stats.linregress(zf, zh).slope


def accuracy_fixed_split(label, conf):
    """NO_behavior_evaluateSessionStatus.m (useDynamicSplitMode=0): high = 1 or 6, low = 2 to 5.
    Returns percent correct among high and among low confidence responses (nan when none)."""
    correct = ((conf <= 3) & (label == 0)) | ((conf >= 4) & (label == 1))
    hi = (conf == 1) | (conf == 6)
    lo = (conf >= 2) & (conf <= 5)
    f = lambda m: 100 * correct[m].mean() if m.sum() else np.nan
    return f(hi), f(lo)


def accuracy_dynamic_split(label, conf, matlab=False):
    """helper.dynamic_split and its use in behavior_all.py, as the Python code has it.
    Mode 1 is high = 1 or 6, low = 2, 3 or 4: the Python code's low "old" responses are 4 only,
    so response 5 is in neither group. With matlab=True, mode 1's low "old" responses are 4 or 5,
    as in NO_dynamic_lowHighSplit.m. Mode 2 is high = 1, 2, 5, 6, low = 3 or 4 in both."""
    counts = np.array([np.sum(conf == k) for k in range(1, 7)])
    c1, c2, c3 = counts[0] + counts[5], counts[1] + counts[4], counts[2] + counts[3]
    split = np.array([c1 - (c2 + c3), (c1 + c2) - c3])
    mode = int(np.where(np.abs(split) == np.min(np.abs(split)))[0][0]) + 1
    if counts[0] == 0 or counts[5] == 0:
        mode = 2
    if counts[1] == 0 or counts[4] == 0:
        mode = 1
    old, new = label == 1, label == 0
    if mode == 1:
        hi_old, lo_old = conf >= 6, (conf == 4) | ((conf == 5) & matlab)
        hi_new, lo_new = conf <= 1, (conf == 2) | (conf == 3)
    else:
        hi_old, lo_old = conf >= 5, conf == 4
        hi_new, lo_new = conf <= 2, conf == 3
    tp_hi, tp_lo = (old & hi_old).sum(), (old & lo_old).sum()
    tn_hi, tn_lo = (new & hi_new).sum(), (new & lo_new).sum()
    n_hi = ((old | new) & (hi_old | hi_new)).sum()
    n_lo = ((old | new) & (lo_old | lo_new)).sum()
    hi = 100 * (tp_hi + tn_hi) / n_hi if n_hi else np.nan
    lo = 100 * (tp_lo + tn_lo) / n_lo if n_lo else np.nan
    return hi, lo, mode


# --- single neurons ------------------------------------------------------------------------

def window_rates(spikes, onsets, window):
    """Spike counts strictly inside (onset + start, onset + end), divided by the window length."""
    sp = np.sort(spikes)
    lo = np.searchsorted(sp, onsets + window[0], side="right")
    hi = np.searchsorted(sp, onsets + window[1], side="left")
    return (hi - lo) / (window[1] - window[0])


def vs_p(rates, categories):
    """One-way ANOVA p across categories. When every group is constant the F statistic is
    undefined: p is nan when all groups have the same value (no spikes, for example) and 0
    when their values differ (zero variance within groups, a difference between them)."""
    groups = [rates[categories == c] for c in np.unique(categories)]
    groups = [g for g in groups if len(g)]
    if len(groups) < 2:
        return np.nan
    if all(np.all(g == g[0]) for g in groups):
        return np.nan if len({g[0] for g in groups}) == 1 else 0.0
    return stats.f_oneway(*groups).pvalue


def bootstrap_p(a, b, rng, n_boot=N_BOOT):
    """Two-tailed bootstrap test of equal means (single_neuron.py ms_test; bootstrapMeanEqualTest.m)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    if len(a) == 0 or len(b) == 0:
        return np.nan
    m = np.mean(np.concatenate([a, b]))
    at, bt = a - a.mean() + m, b - b.mean() + m
    ia = rng.integers(0, len(a), size=(n_boot, len(a)))
    ib = rng.integers(0, len(b), size=(n_boot, len(b)))
    t = np.abs(at[ia].mean(1) - bt[ib].mean(1))
    return np.mean(t >= abs(a.mean() - b.mean()))


def isi_violation_fraction(spikes, sort=True, limit=0.003):
    sp = np.sort(spikes) if sort else np.asarray(spikes)
    if len(sp) < 2:
        return np.nan
    return np.mean(np.diff(sp) < limit)


# --- checks of the files -------------------------------------------------------------------

def variant_from_images(s):
    """Task variant from the image directory of the trials (newolddelay, newolddelay2, newolddelay3),
    the directories of Table 2 of Faraut et al. 2018."""
    dirs = {re.split(r"[\\/]", p)[0].lower() for p in s["trials"]["external_image_file"]}
    out = {"newolddelay": 1, "newolddelay2": 2, "newolddelay3": 3}
    v = {out.get(d) for d in dirs}
    return v.pop() if len(v) == 1 else None


def trial_event_order(s, learn_codes=(20, 21), recog_codes=tuple(range(31, 37))):
    """For each stimulus onset (1) in the events, whether the next four codes are offset (2),
    question (3), a response of the phase's kind and end of trial (6). Returns (n onsets, n bad).
    The learning block is taken as the smaller experiment id (checked in the notebook, experiment-ids)."""
    ids = np.unique(s["expids"])
    n, bad = 0, 0
    for k, eid in enumerate(ids):
        ev = s["events"][s["expids"] == eid]
        resp = learn_codes if k == 0 else recog_codes
        for i in np.where(ev == 1)[0]:
            n += 1
            nxt = ev[i + 1:i + 5]
            ok = len(nxt) == 4 and nxt[0] == 2 and nxt[1] == 3 and nxt[2] in resp and nxt[3] == 6
            bad += not ok
    return n, bad


def duplicated_trains(sessions):
    """Units whose spike trains are identical to a unit of an earlier file (by session id).
    Returns a set of (session_id, unit index) to drop when each train is counted once, and the
    pairs of sessions that share trains with their counts."""
    seen, drop, pairs = {}, set(), {}
    for s in sessions:
        for i, sp in enumerate(s["spikes"]):
            key = (len(sp), np.asarray(sp).tobytes())
            if key in seen:
                drop.add((s["session_id"], i))
                p = (seen[key][0], s["session_id"])
                pairs[p] = pairs.get(p, 0) + 1
            else:
                seen[key] = (s["session_id"], i)
    return drop, pairs
