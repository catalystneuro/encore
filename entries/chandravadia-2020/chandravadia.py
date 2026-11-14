"""Loading and measures for dandiset 000004 (Chandravadia et al. 2020, Scientific Data 7, 78).

The dandiset holds one NWB file per session of the new/old recognition memory task: the
trials table, the TTL events and experiment ids, the electrodes table, the units table with
spike times and mean waveforms, and the 200 stimulus images. Files are streamed from the
archive with remfile and h5py; the images are never read, as nothing here needs their pixels.

Where each parameter comes from:

- Recognition trials are the rows with stim_phase "recog"; the confidence response is
  response_value minus 30 (1 = new, confident; 6 = old, confident); "old" is label 1. These
  are the claims file's method choices (its opening comment). The notebook checks the
  response against the TTL codes 31 to 36 of the events stream, which is what the paper's
  code reads (helper.extract_recog_responses).
- Firing rates are spike counts in a window divided by its length (claims file). The main
  window is 200 to 1200 ms after stimulus onset, from the paper ("a 1 s long window starting
  200 ms after stimulus onset", Technical Validation, proportion of selective cells,
  paragraph 2). The code's window, 200 to 1700 ms (single_neuron.py, vs_test and ms_test;
  NWB_singleCellAnalysis_release.m, countStimulus_long), is a variant. Spikes are counted in
  the half-open interval (start, end], as extractPeriodCountsSimple.m does; this is a
  standard choice that cannot change a result at the precision of the spike times.
- The ROC follows the paper's code (helper.cal_cumulative_d, cal_typecounter, adjustHF and
  cal_auc in recogmem-release-NWB at commit 1d95162): cumulative hit and false alarm rates
  from confidence 6 down to 1, rates of 0 or 1 adjusted to 1/(2n) or 1 - 1/(2n), AUC by the
  trapezoid rule with (0,0) and (1,1) added (claims file).
- The z-ROC slope is the regression of z(H) on z(F) over the five interior points
  (calcZROCSlope.m; claims file).
- The fixed confidence split is that of NO_behavior_evaluateSessionStatus.m (high = 1 or
  6, low = 2 to 5); the dynamic split is helper.dynamic_split of the Python code, and the
  MATLAB NO_dynamic_lowHighSplit.m, which differs from it in split mode 1, is a variant.
- The bootstrap test of equal means is bootstrapMeanEqualTest.m (Efron and Tibshirani,
  algorithm 16.2), two-sided, 1000 resamples, with the generator the notebook passes in
  (a fixed seed is a standard choice that cannot change a result beyond resampling noise).
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import stats

DANDISET = "000004"
VERSION = "0.220126.1852"
API = "https://api.dandiarchive.org/api"
EUROPEPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/{}/fullTextXML"
PAPER_PMC = "PMC7055261"       # this paper, doi:10.1038/s41597-020-0415-9
FARAUT_PMC = "PMC5810422"      # Faraut et al. 2018, doi:10.1038/sdata.2018.10

WINDOW_METHODS = (0.2, 1.2)    # paper, Technical Validation, proportion of selective cells
WINDOW_CODE = (0.2, 1.7)       # paper's code, single_neuron.py and NWB_singleCellAnalysis_release.m


def list_assets(version: str = VERSION) -> pd.DataFrame:
    """Every asset of a version (the pinned one by default), with its path, size and identifier."""
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += [dict(path=a["path"], size=a["size"], asset_id=a["asset_id"]) for a in page["results"]]
        url = page.get("next")
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def version_metadata() -> dict:
    return requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60).json()


def asset_url(asset_id: str) -> str:
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url


def _str(x):
    return x.decode() if isinstance(x, bytes) else x


def _strs(a):
    return np.array([_str(x) for x in a], dtype=object)


def read_session(asset_id: str) -> dict:
    """Read everything the analysis uses from one file: metadata, trials, events, electrodes, units.

    The stimulus images are not read; only their array shape is recorded."""
    f = h5py.File(remfile.File(asset_url(asset_id)), "r")
    out = {"asset_id": asset_id}
    for k in ["identifier", "session_description", "session_start_time", "timestamps_reference_time"]:
        out[k] = _str(f[k][()])
    for k in ["data_collection", "experiment_description", "institution", "lab"]:
        out[k] = _str(f["general/" + k][()]) if "general/" + k in f else None
    out["subject"] = {k: _str(f["general/subject/" + k][()]) for k in f["general/subject"]}
    out["devices"] = list(f["general/devices"].keys())

    t = f["intervals/trials"]
    out["trial_columns"] = [_str(c) for c in t.attrs["colnames"]]
    cols = {}
    for k in t:
        if k == "id":
            continue
        v = t[k][()]
        cols[k] = _strs(v) if v.dtype.kind in "OS" else v
    out["trials"] = pd.DataFrame(cols)
    out["trial_descriptions"] = {k: _str(t[k].attrs.get("description", "")) for k in t if k != "id"}

    ev = f["acquisition/events"]
    out["events"] = np.array([float(_str(x)) for x in ev["data"][()]])
    out["events_t"] = ev["timestamps"][()]
    out["events_description"] = _str(ev.attrs.get("description", ""))
    ex = f["acquisition/experiment_ids"]
    out["expids"] = ex["data"][()]
    out["expids_t"] = ex["timestamps"][()]
    out["expids_description"] = _str(ex.attrs.get("description", ""))

    e = f["general/extracellular_ephys/electrodes"]
    out["electrode_columns"] = [_str(c) for c in e.attrs["colnames"]]
    ecols = {}
    for k in e:
        if k == "group":
            continue
        v = e[k][()]
        ecols[k] = _strs(v) if v.dtype.kind in "OS" else v
    out["electrodes"] = pd.DataFrame(ecols)

    u = f["units"]
    out["unit_columns"] = [_str(c) for c in u.attrs["colnames"]]
    out["unit_datasets"] = sorted(u.keys())
    st, si = u["spike_times"][()], u["spike_times_index"][()]
    starts = np.r_[0, si[:-1]]
    out["spikes"] = [st[a:b] for a, b in zip(starts, si)]
    units = pd.DataFrame({"id": u["id"][()]})
    for k in ["origClusterID", "IsolationDist", "IsolDist", "SNR"]:
        if k in u:
            units[k] = u[k][()]
    if "waveform_mean_sampling_rate" in u:
        sr = u["waveform_mean_sampling_rate"][()]
        units["waveform_sampling_rate"] = sr.reshape(len(sr), -1)[:, 0]
    for k in ["waveform_mean_encoding", "waveform_mean_recognition"]:
        if k in u:
            w = u[k][()]
            units[k + "_samples"] = w.shape[1] if w.ndim > 1 else 0
            units[k + "_finite"] = np.isfinite(w).all(axis=1) if w.ndim > 1 else False
    eidx, el = u["electrodes_index"][()], u["electrodes"][()]
    estarts = np.r_[0, eidx[:-1]]
    units["n_electrodes"] = eidx - estarts
    units["electrode_row"] = [el[a] if b - a >= 1 else -1 for a, b in zip(estarts, eidx)]
    units["n_spikes"] = [len(s) for s in out["spikes"]]
    out["units"] = units
    p = "stimulus/presentation"
    out["stimulus_series"] = {k: f[p][k]["data"].shape for k in f[p] if "data" in f[p][k]}
    f.close()
    return out


def read_all(asset_ids, workers: int = 6) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(read_session, asset_ids))


def parse_identifier(identifier: str) -> tuple[str, int]:
    """'H09_5' -> ('H09', 5): the subject label and the session id (NOID)."""
    label, sid = identifier.rsplit("_", 1)
    return label, int(sid)


def ident_label(label: str) -> str:
    """The identifier's subject label in the paper's notation: CS24 -> C24 (H09 and T88 are unchanged)."""
    return re.sub(r"^CS", "C", label)


def table_label(subject_id: str) -> str:
    """The dandiset's subject_id in the paper's notation: P9HMH -> H09, P24CS -> C24, TWH088 -> T88."""
    m = re.fullmatch(r"P(\d+)(HMH|CS)", subject_id)
    if m:
        return ("H" if m[2] == "HMH" else "C") + f"{int(m[1]):02d}"
    m = re.fullmatch(r"TWH(\d+)", subject_id)
    if m:
        return f"T{int(m[1])}"
    return subject_id


def variant_of(paths) -> set:
    """Task variant from the image folder of external_image_file (newolddelay, newolddelay2, newolddelay3)."""
    out = set()
    for p in paths:
        folder = re.split(r"[\\/]", str(p))[0].lower()
        m = re.fullmatch(r"newolddelay(\d?)", folder)
        out.add(int(m[1]) if m and m[1] else (1 if m else folder))
    return out


# --- tables from the papers (Europe PMC full text) ------------------------------------------

def europepmc_tables(pmc: str) -> dict:
    """The tables of an open access article, by label, as lists of rows of cell texts."""
    import xml.etree.ElementTree as ET
    root = ET.fromstring(requests.get(EUROPEPMC.format(pmc), timeout=120).content)
    out = {}
    for tw in root.iter("table-wrap"):
        lab = tw.find("label")
        rows = [["".join(td.itertext()).strip() for td in tr] for tr in tw.iter("tr")]
        if lab is not None and lab.text not in out:
            out[lab.text.strip()] = rows
    return out


def session_table(rows) -> pd.DataFrame:
    """One row per (subject, session) from a patients table: ID, session IDs, variants, age, sex, diagnosis."""
    recs = []
    for r in rows:
        if len(r) < 7 or not re.fullmatch(r"[HCT]\d+", r[0]):
            continue
        sids = [int(s) for s in re.findall(r"\d+", r[2])]
        vars_ = [int(s) for s in re.findall(r"\d+", r[3])]
        for k, s in enumerate(sids):
            recs.append(dict(label=r[0], session=s, variant=vars_[k] if k < len(vars_) else np.nan,
                             n_sessions=int(r[1]), age=int(r[4]), sex=r[5], diagnosis=r[6]))
    return pd.DataFrame(recs)


# --- behaviour --------------------------------------------------------------------------------

def recog(trials: pd.DataFrame) -> pd.DataFrame:
    """Recognition trials with the confidence response (1-6) and the label (1 = old under the code's reading)."""
    r = trials[trials.stim_phase == "recog"].copy()
    r["conf"] = r.response_value - 30
    r["label"] = pd.to_numeric(r.new_old_labels_recog, errors="coerce")
    return r


def adjust_hf(H, F, n_old, n_new):
    if H == 1:
        H = 1 - 1 / (2 * n_old)
    if F == 1:
        F = 1 - 1 / (2 * n_new)
    if H == 0:
        H = 1 / (2 * n_old)
    if F == 0:
        F = 1 / (2 * n_new)
    return H, F


def cumulative_roc(conf, is_old):
    """Hit and false alarm rates cumulated from confidence 6 down to 1 (helper.cal_cumulative_d)."""
    conf, is_old = np.asarray(conf), np.asarray(is_old, bool)
    n_old, n_new = is_old.sum(), (~is_old).sum()
    H, F = [], []
    for c in range(6, 0, -1):
        sel = conf >= c
        h, f = adjust_hf((sel & is_old).sum() / n_old, (sel & ~is_old).sum() / n_new, n_old, n_new)
        H.append(h)
        F.append(f)
    return np.array(H), np.array(F)


def auc(H, F):
    """Trapezoid AUC with (0,0) and (1,1) added (helper.cal_auc)."""
    TP, FP = list(H), list(F)
    if TP[0] != 0 or FP[0] != 0:
        TP, FP = [0] + TP, [0] + FP
    if TP[-1] != 1 or FP[-1] != 1:
        TP, FP = TP + [1], FP + [1]
    a = 0.0
    for i in range(1, len(TP)):
        a += (FP[i] - FP[i - 1]) * TP[i - 1] + 0.5 * (TP[i] - TP[i - 1]) * (FP[i] - FP[i - 1])
    return a


def zroc_slope(H, F):
    """Slope of z(H) on z(F) over the five interior points (calcZROCSlope.m).

    NaN when the five false alarm rates are all equal, as the regression then has no slope."""
    x, y = stats.norm.ppf(F[:5]), stats.norm.ppf(H[:5])
    if np.ptp(x) < 1e-12:
        return np.nan
    return stats.linregress(x, y).slope


def accuracy_fixed(conf, is_old):
    """High = 1 or 6, low = 2 to 5 (NO_behavior_evaluateSessionStatus.m, fixed threshold)."""
    conf, is_old = np.asarray(conf), np.asarray(is_old, bool)
    high, low = (conf == 1) | (conf == 6), (conf >= 2) & (conf <= 5)
    correct = ((conf <= 3) & ~is_old) | ((conf >= 4) & is_old)
    ah = (correct & high).sum() / high.sum() if high.sum() else np.nan
    al = (correct & low).sum() / low.sum() if low.sum() else np.nan
    return ah, al, int(high.sum()), int(low.sum())


def accuracy_dynamic(conf, is_old, flavour="python"):
    """Dynamic split: helper.dynamic_split (python) or NO_dynamic_lowHighSplit.m (matlab).

    Mode 1 is 1 | 2,3 | 4,5 | 6 and mode 2 is 1,2 | 3 | 4 | 5,6. In mode 1 the Python code
    counts only response 4 (not 4 and 5) among the low old responses; the MATLAB code counts both."""
    conf, is_old = np.asarray(conf), np.asarray(is_old, bool)
    rc = np.array([(conf == k).sum() for k in range(1, 7)])
    s1 = rc[0] + rc[5] - (rc[1] + rc[4] + rc[2] + rc[3])
    s2 = rc[0] + rc[5] + rc[1] + rc[4] - (rc[2] + rc[3])
    mode = int(np.argmin(np.abs([s1, s2]))) + 1
    if rc[0] == 0 or rc[5] == 0:
        mode = 2
    if rc[1] == 0 or rc[4] == 0:
        mode = 1
    if mode == 1:
        high = (conf == 1) | (conf == 6)
        low_old = (conf == 4) if flavour == "python" else ((conf == 4) | (conf == 5))
        low = ((conf == 2) | (conf == 3)) | low_old
    else:
        high = (conf <= 2) | (conf >= 5)
        low = (conf == 3) | (conf == 4)
    correct = ((conf <= 3) & ~is_old) | ((conf >= 4) & is_old)
    ah = (correct & high).sum() / high.sum() if high.sum() else np.nan
    al = (correct & low).sum() / low.sum() if low.sum() else np.nan
    return ah, al, mode, int(high.sum()), int(low.sum())


def code_inclusion(conf, a):
    """The Python code's inclusion rule for the accuracy analysis (helper.check_inclusion):
    AUC at least 0.6, and at most one of the three new and one of the three old levels unused."""
    rc = np.array([(np.asarray(conf) == k).sum() for k in range(1, 7)])
    return bool(a >= 0.6 and (rc[:3] == 0).sum() <= 1 and (rc[3:] == 0).sum() <= 1)


# --- single neurons ---------------------------------------------------------------------------

def window_rates(spikes, onsets, window):
    """Spike counts in (onset + a, onset + b], divided by b - a (Hz), one per onset."""
    a, b = window
    s = np.sort(spikes)
    lo = np.searchsorted(s, onsets + a, side="right")
    hi = np.searchsorted(s, onsets + b, side="right")
    return (hi - lo) / (b - a)


def anova_p(rates, groups):
    """One-way ANOVA across groups; NaN when every rate is equal (no variance)."""
    gs = [rates[groups == g] for g in np.unique(groups)]
    if np.allclose(rates, rates[0]):
        return np.nan
    return stats.f_oneway(*gs).pvalue


def bootstrap_mean_equal(z, y, B, rng):
    """Two-sided bootstrap test of equal means (bootstrapMeanEqualTest.m, mode 1, no variance correction)."""
    z, y = np.asarray(z, float), np.asarray(y, float)
    n, m = len(z), len(y)
    xm = np.r_[z, y].mean()
    zt, yt = z - z.mean() + xm, y - y.mean() + xm
    zs = zt[rng.integers(0, n, size=(B, n))].mean(axis=1)
    ys = yt[rng.integers(0, m, size=(B, m))].mean(axis=1)
    t = np.abs(zs - ys)
    tob = z.mean() - y.mean()
    return np.mean(t >= abs(tob))


def isi_fraction(spikes, limit=0.003, sort=True):
    s = np.sort(spikes) if sort else np.asarray(spikes)
    if len(s) < 2:
        return np.nan
    return np.mean(np.diff(s) < limit)
