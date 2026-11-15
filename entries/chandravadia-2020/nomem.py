"""Loading and measures for the new/old recognition memory data of dandiset 000004.

Chandravadia, Liang, Schjetnan et al. (2020), Scientific Data 7, 78, doi:10.1038/s41597-020-0415-9.

Each NWB file holds one session: the TTL events and experiment ids (acquisition), the trials table
(100 encoding and 100 recognition trials), the 200 stimulus images (stimulus/presentation), the
electrodes table and the units table with spike times. Files are streamed from the archive at the
pinned version; nothing is written to disk. The stimulus images are reduced to one hash per frame
as they load.

Where the parameters come from:

- Recognition trials are the rows with stim_phase "recog"; the confidence response is
  response_value minus 30 (1 = new, confident; 6 = old, confident); "old" is label 1 of
  new_old_labels_recog. All three are fixed by the claims file (its opening comment), which
  takes them from the paper's code (github.com/rutishauserlab/recogmem-release-NWB at commit
  1d95162d2672e71dd234a31e4b8d70017a289ee3: NWBloadDataOfBlock_release.m subtracts 30 from
  the event codes; NWB_singleCellAnalysis_release.m says "1 is old, 0 is new").
- The ROC follows the paper's code as the claims file prescribes: the cumulative hit and false
  alarm rates over the six confidence levels from "old, confident" down (calcEmpiricalROC.m,
  calcCumulativeD.m), each adjusted for 0 and 1 as in adjustHF.m, the AUC by the trapezoid rule
  with (0,0) and (1,1) added (calcROC_AUC.m), and the z-ROC slope as the least-squares
  regression of z(H) on z(F) over the five interior points (calcZROCSlope.m).
- Accuracy in high and low confidence trials: the fixed split (high 1 or 6, low 2 to 5) of
  NO_behavior_evaluateSessionStatus.m, and the dynamic split of helper.dynamic_split in the
  Python code, both named by the claims file (fig5d-confidence-accuracy). The Python split is
  reproduced as written, including its count of low-confidence hits as response 4 only in split
  mode 1 (MATLAB's NO_dynamic_lowHighSplit.m counts 4 and 5 there).
- Firing rates are spike counts in a window after stimulus onset divided by its length (claims
  file). The windows are 0.2 to 1.2 s (Methods, "a 1 s long window starting 200 ms after
  stimulus onset") and 0.2 to 1.7 s (the code's, single_neuron.py and
  NWB_singleCellAnalysis_release.m). Stimulus onset is the trial's start_time, which the paper
  defines as "the time of stimulus onset of each trial" (Data Records, interval group).
- The bootstrap test of equal means is Efron and Tibshirani's algorithm 16.2 as in
  bootstrapMeanEqualTest.m (both samples shifted to the pooled mean, resampled with
  replacement, two-sided on the absolute difference of means), with B = 1000 (Methods). The seed
  is a standard choice and is passed in by the caller.
"""

from __future__ import annotations

import hashlib
import re
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "000004"
DANDISET_VERSION = "0.220126.1852"

WINDOW_METHODS = (0.2, 1.2)   # s after stimulus onset; Methods, Technical Validation
WINDOW_CODE = (0.2, 1.7)      # s; single_neuron.py and NWB_singleCellAnalysis_release.m
N_BOOT = 1000                 # Methods: "two-tailed bootstrap comparison of means with 1,000 runs"
ALPHA = 0.05

# Full texts in Europe PMC (version of record, CC BY): this paper, and Faraut et al. 2018,
# Sci Data 5, 180010 (doi:10.1038/sdata.2018.10), the earlier release of the task's data.
PAPER_PMC = "PMC7055261"
FARAUT_PMC = "PMC5810422"
EUROPE_PMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/{}/fullTextXML"


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    if isinstance(value, bytes):
        return value.decode()
    if isinstance(value, np.ndarray):
        return "; ".join(_text(v) for v in value.ravel())
    return str(value)


def _strings(dataset) -> np.ndarray:
    return np.array([_text(v) for v in dataset[:]], dtype=object)


def load_session(path: str, url: str, images: bool = True) -> dict:
    """Everything the analyses use from one file, as plain arrays."""
    with h5py.File(remfile.File(url), "r") as f:
        s = {"path": path, "identifier": _text(f["identifier"][()]),
             "session_description": _text(f["session_description"][()]),
             "session_start_time": _text(f["session_start_time"][()]),
             "institution": _text(f["general/institution"][()]) if "general/institution" in f else "",
             "data_collection": _text(f["general/data_collection"][()]) if "general/data_collection" in f else "",
             "devices": sorted(f["general/devices"].keys())}
        s["subject"] = {k: _text(v[()]) for k, v in f["general/subject"].items()}
        ev, ex = f["acquisition/events"], f["acquisition/experiment_ids"]
        s["events"] = np.array([float(_text(v)) for v in ev["data"][:]])
        s["events_t"] = ev["timestamps"][:]
        s["expids"] = ex["data"][:].astype(float)
        s["expids_t"] = ex["timestamps"][:]
        s["events_description"] = _text(ev.attrs.get("description", ""))
        s["expids_description"] = _text(ex.attrs.get("description", ""))

        tr = f["intervals/trials"]
        cols = [_text(c) for c in tr.attrs["colnames"]]
        table = {}
        for c in cols:
            d = tr[c]
            table[c] = _strings(d) if d.dtype.kind in "OSU" else d[:]
        s["trials"] = pd.DataFrame(table)
        s["trial_columns"] = cols
        s["label_description"] = _text(tr["new_old_labels_recog"].attrs.get("description", ""))

        el = f["general/extracellular_ephys/electrodes"]
        ecols = [_text(c) for c in el.attrs["colnames"]]
        etab = {"id": el["id"][:]}
        for c in ecols:
            if c == "group":
                continue
            d = el[c]
            etab[c] = _strings(d) if d.dtype.kind in "OSU" else d[:]
        s["electrodes"] = pd.DataFrame(etab)
        s["electrode_columns"] = ecols
        s["imp_dtype"] = str(el["imp"].dtype) if "imp" in el else ""

        u = f["units"]
        ucols = [_text(c) for c in u.attrs["colnames"]]
        s["unit_columns"] = ucols
        s["unit_descriptions"] = {c: _text(u[c].attrs.get("description", "")) for c in ucols if c in u}
        s["spike_times_attrs"] = {k: _text(v) for k, v in u["spike_times"].attrs.items()
                                  if k in ("description", "unit", "resolution")}
        s["event_time_unit"] = _text(ev["timestamps"].attrs.get("unit", ""))
        n = len(u["id"])
        idx = u["spike_times_index"][:]
        st = u["spike_times"][:]
        starts = np.concatenate([[0], idx[:-1]])
        s["spikes"] = [st[a:b] for a, b in zip(starts, idx)]
        eidx = u["electrodes_index"][:]
        e = u["electrodes"][:]
        estarts = np.concatenate([[0], eidx[:-1]])
        s["unit_electrodes"] = [e[a:b] for a, b in zip(estarts, eidx)]
        units = {"id": u["id"][:]}
        for c in ("origClusterID", "SNR", "IsolationDist", "IsolDist"):
            if c in u:
                units[c] = u[c][:]
        if "waveform_mean_sampling_rate" in u:
            units["waveform_rate"] = u["waveform_mean_sampling_rate"][:].reshape(n, -1)[:, 0]
        for c in ("waveform_mean_encoding", "waveform_mean_recognition"):
            if c in u:
                w = u[c][:]
                units[c + "_samples"] = np.full(n, w.shape[1])
                units[c + "_finite"] = np.isfinite(w).all(axis=1)
        s["units"] = pd.DataFrame(units)

        if images:
            data = f["stimulus/presentation/StimulusPresentation/data"]
            s["image_shape"] = data.shape
            frames = data[:]
            s["image_hash"] = [hashlib.md5(frames[i].tobytes()).hexdigest() for i in range(frames.shape[0])]
            s["image_t"] = f["stimulus/presentation/StimulusPresentation/timestamps"][:]
            del frames
    return s


def load_all(images: bool = True, workers: int = 6) -> list[dict]:
    urls = asset_urls()
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(lambda pu: load_session(*pu, images=images), urls))


def session_key(s: dict) -> tuple[str, int]:
    """(subject label, session id) from the identifier, e.g. 'H09_5' -> ('H09', 5)."""
    label, sid = s["identifier"].rsplit("_", 1)
    return label, int(sid)


def site(label: str) -> str:
    """CS for subjects labelled H or C, TWH for T (Figure 5 legend)."""
    return "TWH" if label.startswith("T") else "CS"


# --- the paper's tables, read from the full text --------------------------------------------

def _tables(pmc: str) -> dict[str, list[list[str]]]:
    with urllib.request.urlopen(EUROPE_PMC.format(pmc), timeout=60) as r:
        root = ET.fromstring(r.read())
    out = {}
    for tw in root.iter("table-wrap"):
        label = tw.find("label")
        name = "".join(label.itertext()).strip() if label is not None else tw.get("id")
        rows = [["".join(c.itertext()).strip() for c in tr] for tr in tw.iter("tr")]
        out.setdefault(name, rows)
    return out


def _subject_rows(rows: list[list[str]]) -> pd.DataFrame:
    out = []
    for r in rows:
        if len(r) < 7 or not re.fullmatch(r"[HCT]\d+", r[0]):
            continue
        sessions = [int(x) for x in re.findall(r"\d+", r[2])]
        variants = [int(x) for x in re.findall(r"\d+", r[3])]
        out.append({"label": r[0], "n_sessions": int(r[1]), "sessions": sessions, "variants": variants,
                    "age": int(r[4]), "sex": r[5], "diagnosis": r[6]})
    return pd.DataFrame(out)


def paper_table1() -> tuple[pd.DataFrame, list[str]]:
    """Online-only Table 1 of the paper, one row per subject, and its totals row."""
    rows = _tables(PAPER_PMC)["Online-only Table 1"]
    totals = [c for c in rows[-1] if c]
    return _subject_rows(rows), totals


def faraut_table1() -> tuple[pd.DataFrame, list[str], dict[str, list[list[str]]]]:
    """Table 1 of Faraut et al. 2018 (the earlier release), its totals, and all its tables."""
    tables = _tables(FARAUT_PMC)
    rows = tables["Table 1"]
    totals = [c for c in rows[-1] if c]
    return _subject_rows(rows), totals, tables


def sessions_of(table: pd.DataFrame) -> pd.DataFrame:
    """One row per (subject, session) of a subject table, with the session's variant."""
    rows = []
    for _, r in table.iterrows():
        for i, sid in enumerate(r.sessions):
            rows.append({"label": r.label, "session": sid,
                         "variant": r.variants[i] if i < len(r.variants) else np.nan})
    return pd.DataFrame(rows)


# --- behaviour --------------------------------------------------------------------------------

def recog(s: dict) -> pd.DataFrame:
    """Recognition trials: label (1 = old, as the paper's code), confidence 1..6 and onset."""
    t = s["trials"]
    r = t[t.stim_phase == "recog"].reset_index(drop=True)
    out = pd.DataFrame({"onset": r.start_time.to_numpy(float),
                        "label": r.new_old_labels_recog.astype(int).to_numpy(),
                        "confidence": (r.response_value.to_numpy(float) - 30).astype(int),
                        "category": r.stimCategory.to_numpy(int),
                        "category_name": r.category_name.to_numpy()})
    return out


def adjust_hf(h: float, f: float, n_old: int, n_new: int) -> tuple[float, float]:
    """adjustHF.m: rates of 0 and 1 moved to 1/(2n) and 1 - 1/(2n)."""
    if h == 1:
        h = 1 - 1 / (2 * n_old)
    if f == 1:
        f = 1 - 1 / (2 * n_new)
    if h == 0:
        h = 1 / (2 * n_old)
    if f == 0:
        f = 1 / (2 * n_new)
    return h, f


def roc(confidence: np.ndarray, is_old: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Cumulative hit and false alarm rates for criteria 6, >=5, ..., >=1 (calcCumulativeD.m)."""
    n_old, n_new = int(is_old.sum()), int((~is_old).sum())
    hs, fs = [], []
    for k in range(6, 0, -1):
        said_old = confidence >= k
        h = (said_old & is_old).sum() / n_old
        f = (said_old & ~is_old).sum() / n_new
        h, f = adjust_hf(h, f, n_old, n_new)
        hs.append(h)
        fs.append(f)
    return np.array(hs), np.array(fs)


def auc(h: np.ndarray, f: np.ndarray) -> float:
    """calcROC_AUC.m / helper.cal_auc: trapezoid rule with (0,0) and (1,1) added.

    calcROC_AUC.m adds (0,0) when FP(1) ~= 0 or TP(1) ~= 1, this function when either is not 0.
    The two differ only when the first point is (0,0) or (0, h < 1), which cannot occur after
    adjust_hf (F is at least 1/(2n)), so both add (0,0) to every ROC here and give the same AUC.
    """
    tp, fp = list(h), list(f)
    if fp[0] != 0 or tp[0] != 0:
        tp, fp = [0.0] + tp, [0.0] + fp
    if fp[-1] != 1 or tp[-1] != 1:
        tp, fp = tp + [1.0], fp + [1.0]
    area = 0.0
    for i in range(1, len(tp)):
        if fp[i - 1] < fp[i]:
            area += (fp[i] - fp[i - 1]) * tp[i - 1] + 0.5 * (tp[i] - tp[i - 1]) * (fp[i] - fp[i - 1])
    return area


def zroc_slope(h: np.ndarray, f: np.ndarray) -> float:
    """calcZROCSlope.m: regression of z(H) on z(F) over the first five points.

    The sixth point, criterion >= 1, is (1,1) before adjust_hf and (1 - 1/(2n), 1 - 1/(2n)) after
    it; calcZROCSlope.m drops it ("is always in right upper corner").
    """
    zh, zf = stats.norm.ppf(h[:5]), stats.norm.ppf(f[:5])
    return float(np.polyfit(zf, zh, 1)[0])


def zroc_slope_regress(h: np.ndarray, f: np.ndarray) -> float:
    """The slope MATLAB's regress returns in calcZROCSlope.m, also when z(F) is constant.

    regress solves by QR with column pivoting and, when the design [1, z(F)] is rank deficient,
    sets the coefficient of the dropped column to 0 (a basic solution). Equal to zroc_slope when
    z(F) takes at least two values.
    """
    from scipy import linalg
    zh, zf = stats.norm.ppf(h[:5]), stats.norm.ppf(f[:5])
    x = np.column_stack([np.ones(5), zf])
    q, r, perm = linalg.qr(x, mode="economic", pivoting=True)
    rank = int((np.abs(np.diag(r)) > max(x.shape) * np.spacing(abs(r[0, 0]))).sum())
    b = np.zeros(2)
    b[perm[:rank]] = linalg.solve_triangular(r[:rank, :rank], q[:, :rank].T @ zh)
    return float(b[1])


def accuracy_fixed(conf: np.ndarray, is_old: np.ndarray) -> tuple[float, float]:
    """NO_behavior_evaluateSessionStatus.m: high is response 1 or 6, low is 2 to 5."""
    correct = (is_old & (conf >= 4)) | (~is_old & (conf <= 3))
    high = (conf == 1) | (conf == 6)
    low = (conf >= 2) & (conf <= 5)
    acc_h = correct[high].mean() if high.any() else np.nan
    acc_l = correct[low].mean() if low.any() else np.nan
    return acc_h, acc_l


def accuracy_dynamic(conf: np.ndarray, is_old: np.ndarray) -> tuple[float, float, int]:
    """helper.dynamic_split and plotFigure5.ipynb, as written. Returns (high, low, split mode)."""
    counts = np.array([(conf == k).sum() for k in range(1, 7)])
    c1, c2, c3 = counts[0] + counts[5], counts[1] + counts[4], counts[2] + counts[3]
    split = np.array([c1 - (c2 + c3), (c1 + c2) - c3])
    mode = int(np.where(np.abs(split) == np.abs(split).min())[0][0]) + 1
    if counts[0] == 0 or counts[5] == 0:
        mode = 2
    if counts[1] == 0 or counts[4] == 0:
        mode = 1
    old, new = is_old, ~is_old
    if mode == 1:
        tp_h, tp_l = old & (conf >= 6), old & (conf == 4)
        fp_h, fp_l = new & (conf >= 6), new & (conf == 4)
        tn_h, tn_l = new & (conf <= 1), new & ((conf == 3) | (conf == 2))
        fn_h, fn_l = old & (conf <= 1), old & ((conf == 3) | (conf == 2))
    else:
        tp_h, tp_l = old & (conf >= 5), old & (conf == 4)
        fp_h, fp_l = new & (conf >= 5), new & (conf == 4)
        tn_h, tn_l = new & (conf <= 2), new & (conf == 3)
        fn_h, fn_l = old & (conf <= 2), old & (conf == 3)
    n_h = tn_h.sum() + tp_h.sum() + fn_h.sum() + fp_h.sum()
    n_l = tn_l.sum() + tp_l.sum() + fn_l.sum() + fp_l.sum()
    acc_h = (tn_h.sum() + tp_h.sum()) / n_h if n_h else np.nan
    acc_l = (tn_l.sum() + tp_l.sum()) / n_l if n_l else np.nan
    return acc_h, acc_l, mode


def included(conf: np.ndarray, auc_value: float) -> bool:
    """helper.check_inclusion, applied by plotFigure5.ipynb before the accuracy panel."""
    counts = np.array([(conf == k).sum() for k in range(1, 7)])
    return not (auc_value < 0.6 or (counts[:3] == 0).sum() > 1 or (counts[3:] == 0).sum() > 1)


# --- single units -----------------------------------------------------------------------------

def window_rates(spikes: np.ndarray, onsets: np.ndarray, window: tuple[float, float]) -> np.ndarray:
    """Spike count in (onset + start, onset + stop] divided by the window length, per trial."""
    sp = np.sort(spikes)
    lo = np.searchsorted(sp, onsets + window[0], side="right")
    hi = np.searchsorted(sp, onsets + window[1], side="right")
    return (hi - lo) / (window[1] - window[0])


def anova_p(rates: np.ndarray, groups: np.ndarray) -> float:
    """One-way ANOVA across the groups (the 5 categories); nan when every rate is equal."""
    samples = [rates[groups == g] for g in np.unique(groups)]
    if np.all(rates == rates[0]):
        return np.nan
    return float(stats.f_oneway(*samples).pvalue)


def bootstrap_p(a: np.ndarray, b: np.ndarray, rng: np.random.Generator, n_boot: int = N_BOOT) -> float:
    """bootstrapMeanEqualTest.m (Efron and Tibshirani, algorithm 16.2), two-sided."""
    pooled = np.concatenate([a, b]).mean()
    at, bt = a - a.mean() + pooled, b - b.mean() + pooled
    ia = rng.integers(0, len(a), size=(n_boot, len(a)))
    ib = rng.integers(0, len(b), size=(n_boot, len(b)))
    t = np.abs(at[ia].mean(axis=1) - bt[ib].mean(axis=1))
    return float(np.mean(t >= abs(a.mean() - b.mean())))


def isi_violation_fraction(spikes: np.ndarray, sort: bool = True, limit: float = 0.003) -> float:
    """Fraction of interspike intervals shorter than `limit` seconds (Methods: 3 ms)."""
    sp = np.sort(spikes) if sort else spikes
    if len(sp) < 2:
        return np.nan
    return float(np.mean(np.diff(sp) < limit))
