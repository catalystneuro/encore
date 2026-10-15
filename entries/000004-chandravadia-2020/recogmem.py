"""Loading and measures for dandiset 000004 (Chandravadia et al. 2020, Scientific Data 7, 78).

Human single neurons from the amygdala and hippocampus during a new/old recognition memory task,
one NWB file per session. Files are streamed from the archive at a pinned version with h5py over
remfile; the stimulus images (most of each file's size) are not read, only their shape and
timestamps.

Where the parameters come from:

- Analysis windows. The Methods use a 1 s window starting 200 ms after stimulus onset
  (``WINDOW_METHODS``). The paper's code (rutishauserlab/recogmem-release-NWB, commit 1d95162,
  NWB_singleCellAnalysis_release.m and single_neuron.py) uses 200 ms to 1700 ms
  (``WINDOW_CODE``).
- Visual selectivity: one-way ANOVA of the window rate across the 5 categories of the
  recognition trials (Methods; code's anovan and f_oneway).
- Memory selectivity: two-sided bootstrap test of equal means, Efron and Tibshirani algorithm
  16.2, as in the code's bootstrapMeanEqualTest.m (B = 1000, Methods and code).
- Behaviour: the cumulative ROC over the six confidence levels, the adjustment of rates of 0
  and 1 (Macmillan and Creelman, p. 8), the AUC by the trapezoid rule and the z-ROC slope follow
  the code's calcEmpiricalROC.m, calcCumulativeD.m, adjustHF.m, calcROC_AUC.m and
  calcZROCSlope.m. The fixed high/low confidence split follows NO_behavior_evaluateSessionStatus.m
  and the dynamic split NO_dynamic_lowHighSplit.m / helper.dynamic_split.
- Labels. ``OLD`` is 1, as in the code (its comments say "1 is old, 0 is new"); the paper's text
  and the files' column description say the reverse. The notebook tests which is right.
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "000004"
DANDISET_VERSION = "0.220126.1852"

WINDOW_METHODS = (0.2, 1.2)   # s after stimulus onset; Methods
WINDOW_CODE = (0.2, 1.7)      # s after stimulus onset; the paper's code
OLD, NEW = 1, 0               # label coding of new_old_labels_recog, as the code reads it

# Online-only Table 1 of the paper (CC BY 4.0): subject, session ids, task variants, age, sex,
# diagnosis. Copied from the article as text; used only to compare with the files' metadata.
ONLINE_TABLE_1 = """\
H09|5, 6|1, 2|55|M|Right Mesial Temporal
H10|7|1|37|M|Left Frontal
H11|9|1|16|M|Right Lateral Frontal
H14|17,18|2, 1|31|M|Bilateral Independent Temporal
H15|20, 21|1, 2|45|M|Right Mesial Temporal
H16|23, 24|2, 1|34|F|Right Frontal
H17|32|1|19|M|Left Inferior Frontal
H18|26|1|40|M|Right Mesial Temporal
H19|27, 28|2, 1|34|M|Left Frontal
H21|38, 39, 41|2,1,3|20|M|Not Localized
H23|43, 44, 47|3, 2, 1|40|M|Left Mesial Temporal
H27|58|2|40|M|Bilateral Independent Temporal
H28|48|3|22|M|Right Mesial Temporal
H29|49|3|17|F|Left Deep Insula
H31|50|2|30|M|Right Mesial Temporal
H33|52|1|29|M|Left Mesial Temporal
H42|54, 55|1, 1|29|M|Not Localized
H43|56|1|27|F|Left Mesial Temporal
H44|68|1|57|F|Right Mesial Temporal
H47|92, 97|1, 3|20|M|Right Mesial Temporal
H48|99|1|54|M|Left Mesial Temporal
H51|104, 105|3, 1|24|M|Bilateral Frontal and Temporal
C24|59, 60|1, 2|47|F|Not Localized
C25|61, 63|1, 2|36|F|Bilateral Independent Mesial Temporal
C26|64, 66|1, 2|56|F|Left Mesial Temporal
C27|67|1|44|M|Left Mesial Temporal
C29|69, 70|1, 2|19|M|Left Neocortical Temporal
C31|73|3|32|M|Left Neocortical Temporal
C32|74|2|19|M|Not Localized (Generalized)
C33|76, 77, 78|3, 2, 1|44|F|Right Mesial Temporal
C34|85|3|70|M|Bilateral Mesial Temporal
C37|96|3|33|F|Right Mesial Temporal
C38|102|3|63|F|Right Mesial Temporal
C39|93, 100|1, 3|26|M|Right Insula
C40|101|3|25|M|Right Motor Cortex
C42|111, 112|1, 2|25|F|Not Localized
C43|113|3|42|F|Left Mesial Temporal
C44|114|3|53|F|Right Mesial Temporal
C47|115|3|32|M|Right Mesial Temporal
C48|116|3|32|F|Left Mesial Temporal
C49|117, 118|3, 1|24|F|Left Mesial Temporal
C51|119, 120|3, 1|17|M|Not Localized (No Seizures)
C53|122, 123|3, 1|60|M|Bilateral Independent Mesial Temporal Lobe
C54|124, 125, 126|3, 1, 2|59|F|Right Mesial Temporal
C55|127|1|43|F|Right Mesial Temporal
C56|128|2|48|M|Multifocal, Bitemporal + Orbitofrontal
C57|130, 131|3, 2|46|M|Left Neocortical Parietal
C58|132, 133|3, 1|32|F|Right Frontal Neocortical
C60|134|1|67|M|Left Mesial Temporal
C61|135|1|52|F|Left Mesial Temporal
C62|136|1|25|F|Right Mesial Temporal
T88|2001, 2002|2, 3|26|M|Right Mesial Temporal
T89|2004|1|45|F|Right Frontal
T90|2003|3|20|M|Occipital Cortex
T98|2005|1|46|F|Left Neocortical Temporal
T100|2008|1|19|F|Right Insula
T101|2011|1|25|F|Left Neocortical Temporal
T103|2009|1|49|M|Right Mesial Temporal
T107|2007|1|64|F|Left Mesial Temporal
"""


# Table 1 of Faraut et al. 2018, Scientific Data 5, 180010 (doi:10.1038/sdata.2018.10, CC BY 4.0),
# the paper describing the earlier release of this task's data: subject, session ids, task
# variants, age, sex, diagnosis. Copied from the article as text; used only to mark which sessions
# of the dandiset were in the earlier release. Its abstract gives 1576 neurons in 65 sessions of
# 42 patients.
FARAUT_2018_TABLE_1 = """\
H09|5, 6|1, 2|55|M|Right Mesial Temporal
H10|7|1|37|M|Left Frontal
H11|9|1|16|M|Right Lateral Frontal
H14|17, 18|2, 1|31|M|Bilateral Indep. Temporal
H15|20, 21|1, 2|45|M|Right Mesial Temporal
H16|23, 24|2, 1|34|F|Right Frontal
H17|32|1|19|M|Left Inferior Frontal
H18|26|1|40|M|Right Mesial Temporal
H19|27, 28|2, 1|34|M|Left Frontal
H21|38, 39, 41|2, 1, 3|20|M|Not Localized
H23|43, 44, 47|3, 2, 1|40|M|Left Mesial Temporal
H27|58|2|40|M|Bilateral Indep. Temporal
H28|48|3|22|M|Right Mesial Temporal
H29|49|3|17|F|Left Deep Insula
H31|50|2|30|M|Right Mesial Temporal
H33|52|1|29|M|Left Mesial Temporal
H42|54, 55|1, 1|29|M|Not Localized
H43|56|1|27|F|Left Mesial Temporal
H44|68|1|57|F|Right Mesial Temporal
H47|92, 97|1, 3|20|M|Right Mesial Temporal
H48|98, 99|2, 1|54|M|Left Mesial Temporal
H51|104, 105|3, 1|24|M|Bilateral Frontal and Temporal
C24|59, 60|1, 2|47|F|Not localized
C25|61, 63|1, 2|36|F|Bilateral Indep. Mesial Temporal
C26|64, 66|1, 2|56|F|Left Mesial Temporal
C27|67|1|44|M|Left Mesial Temporal
C29|69, 70|1, 2|19|M|Left Neocortical Temporal
C31|73|3|32|M|Left Neocortical Temporal
C32|74|2|19|M|Not Localized (Generalized)
C33|76, 77, 78|3, 2, 1|44|F|Right Mesial Temporal
C34|85|3|70|M|Bilateral Mesial Temporal
C37|96|3|33|F|Right Mesial Temporal
C38|102|3|63|F|Right Mesial Temporal
C39|93, 100|1, 3|26|M|Right Insula
C40|101|3|25|M|Right Motor Cortex
C42|111, 112|1, 2|25|F|Not Localized
C43|113|3|42|F|Left Mesial Temporal
C44|114|3|53|F|Right Mesial Temporal
C47|115|3|32|M|Right Mesial Temporal
C48|116|3|32|F|Left Mesial Temporal
C49|117, 118|3, 1|24|F|Left Mesial Temporal
C51|119, 120|3, 1|17|M|Not Localized (No Seizures)
"""


def _parse_table(text: str) -> pd.DataFrame:
    rows = []
    for line in text.strip().splitlines():
        sid, sessions, variants, age, sex, diagnosis = line.split("|")
        for s, v in zip(re.findall(r"\d+", sessions), re.findall(r"\d+", variants)):
            rows.append({"table_subject": sid, "session": int(s), "variant": int(v), "age": int(age),
                         "sex": sex, "diagnosis": diagnosis})
    return pd.DataFrame(rows)


def online_table_1() -> pd.DataFrame:
    """Online-only Table 1 as one row per session."""
    return _parse_table(ONLINE_TABLE_1)


def faraut_2018_table_1() -> pd.DataFrame:
    """Table 1 of Faraut et al. 2018 (the earlier release) as one row per session."""
    return _parse_table(FARAUT_2018_TABLE_1)


# --- loading ------------------------------------------------------------------

def _text(x):
    return x.decode() if isinstance(x, bytes) else x


def _column(group, name):
    d = group[name][()]
    if d.dtype == object:
        d = np.array([_text(x) for x in d])
    return d


def asset_urls() -> list[tuple[str, str]]:
    """(path, S3 URL) of every asset of the pinned version, sorted by path."""
    dandiset = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return [(a.path, a.get_content_url(follow_redirects=1, strip_query=True))
            for a in sorted(dandiset.get_assets(), key=lambda a: a.path)]


def load_session(path: str, url: str) -> dict:
    """Everything the analysis uses from one file, without the stimulus images."""
    with h5py.File(remfile.File(url), "r") as f:
        s = {"path": path}
        for key, name in [("identifier", "identifier"), ("session_start_time", "session_start_time"),
                          ("subject_id", "general/subject/subject_id"), ("age", "general/subject/age"),
                          ("sex", "general/subject/sex"), ("diagnosis", "general/subject/description"),
                          ("species", "general/subject/species"), ("institution", "general/institution"),
                          ("data_collection", "general/data_collection")]:
            s[key] = _text(f[name][()])
        s["devices"] = list(f["general/devices"].keys())
        g = f["intervals/trials"]
        s["trials"] = pd.DataFrame({k: _column(g, k) for k in g})
        s["trial_descriptions"] = {k: _text(g[k].attrs.get("description", "")) for k in g}
        s["events"] = np.array([float(_text(x)) for x in f["acquisition/events/data"][()]])
        s["events_t"] = f["acquisition/events/timestamps"][()]
        s["events_description"] = _text(f["acquisition/events"].attrs["description"])
        s["experiment_ids"] = f["acquisition/experiment_ids/data"][()]
        s["experiment_ids_t"] = f["acquisition/experiment_ids/timestamps"][()]
        u = f["units"]
        s["unit_columns"] = sorted(u.keys())
        times, index = u["spike_times"][()], u["spike_times_index"][()]
        s["spikes"] = np.split(times, index[:-1])
        s["unit_electrode"] = u["electrodes"][()]
        s["unit_electrode_index"] = u["electrodes_index"][()]
        s["cluster_id"] = u["origClusterID"][()]
        s["snr"] = u["SNR"][()]
        s["isolation_distance"] = u["IsolationDist"][()]
        s["waveform_rate"] = u["waveform_mean_sampling_rate"][()].ravel()
        s["waveform_shape"] = u["waveform_mean_encoding"].shape
        e = f["general/extracellular_ephys/electrodes"]
        s["electrodes"] = pd.DataFrame({k: _column(e, k) for k in e if k != "group"})
        p = f["stimulus/presentation"]
        s["stimulus"] = {k: (p[k]["data"].shape, p[k]["timestamps"][()]) for k in p}
    s["session"] = int(s["identifier"].split("_")[1])
    s["label"] = s["identifier"].split("_")[0]
    s["site"] = "TWH" if s["label"].startswith("T") else "CS"
    return s


def load_all(workers: int = 8) -> list[dict]:
    """All sessions of the pinned version, streamed in parallel, sorted by session id."""
    urls = asset_urls()
    with ThreadPoolExecutor(workers) as pool:
        sessions = list(pool.map(lambda pu: load_session(*pu), urls))
    return sorted(sessions, key=lambda s: s["session"])


def recognition(s: dict) -> pd.DataFrame:
    """Recognition trials with integer label, confidence response (1-6) and category."""
    r = s["trials"][s["trials"].stim_phase == "recog"].copy()
    r["label"] = r.new_old_labels_recog.astype(int)
    r["response"] = (r.response_value - 30).astype(int)
    r["category"] = r.stimCategory.astype(int)
    return r.reset_index(drop=True)


# --- spikes -------------------------------------------------------------------

def window_rates(spikes: np.ndarray, onsets: np.ndarray, window: tuple[float, float]) -> np.ndarray:
    """Spikes per second in (onset + start, onset + stop] for each onset; spikes need not be sorted."""
    sp = np.sort(spikes)
    lo = np.searchsorted(sp, onsets + window[0], side="right")
    hi = np.searchsorted(sp, onsets + window[1], side="right")
    return (hi - lo) / (window[1] - window[0])


def anova_p(rates: np.ndarray, groups: np.ndarray) -> float:
    """One-way ANOVA p across groups; 1.0 when the rates do not vary."""
    parts = [rates[groups == g] for g in np.unique(groups)]
    if np.all(rates == rates[0]):
        return 1.0
    return float(stats.f_oneway(*parts).pvalue)


def bootstrap_p(z: np.ndarray, y: np.ndarray, rng: np.random.Generator, B: int = 1000) -> float:
    """Two-sided bootstrap test of equal means (Efron and Tibshirani 16.2; bootstrapMeanEqualTest.m)."""
    xm = np.mean(np.concatenate([z, y]))
    zt, yt = z - z.mean() + xm, y - y.mean() + xm
    zs = zt[rng.integers(0, len(z), size=(B, len(z)))].mean(axis=1)
    ys = yt[rng.integers(0, len(y), size=(B, len(y)))].mean(axis=1)
    return float(np.mean(np.abs(zs - ys) >= abs(z.mean() - y.mean())))


def isi_fraction(spikes: np.ndarray, limit: float = 0.003, sort: bool = True) -> float:
    """Fraction of interspike intervals shorter than ``limit`` seconds."""
    sp = np.sort(spikes) if sort else spikes
    isi = np.diff(sp)
    return float(np.mean(isi < limit)) if len(isi) else np.nan


# --- behaviour ----------------------------------------------------------------

def type_counters(labels: np.ndarray, responses: np.ndarray) -> np.ndarray:
    """Hits and false alarms per confidence level, from "old, confident" (6) down to 1."""
    levels = range(6, 0, -1)
    hits = [np.sum((responses == k) & (labels == OLD)) for k in levels]
    fas = [np.sum((responses == k) & (labels == NEW)) for k in levels]
    return np.array([hits, fas])


def _adjust(rate: float, n: int) -> float:
    if rate == 1:
        return 1 - 1 / (2 * n)
    if rate == 0:
        return 1 / (2 * n)
    return rate


def cumulative_rates(labels: np.ndarray, responses: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Cumulative hit and false alarm rates over the six criteria, adjusted for 0 and 1."""
    c = type_counters(labels, responses)
    n_old, n_new = c[0].sum(), c[1].sum()
    h = [_adjust(c[0, :i + 1].sum() / n_old, n_old) for i in range(6)]
    f = [_adjust(c[1, :i + 1].sum() / n_new, n_new) for i in range(6)]
    return np.array(h), np.array(f)


def auc(labels: np.ndarray, responses: np.ndarray) -> float:
    """Area under the cumulative ROC (trapezoid rule, with (0,0) and (1,1) added; calcROC_AUC.m)."""
    h, f = cumulative_rates(labels, responses)
    if f[0] != 0 or h[0] != 1:      # the code's condition, which always adds (0,0) here
        h, f = np.r_[0, h], np.r_[0, f]
    if f[-1] != 1 or h[-1] != 1:
        h, f = np.r_[h, 1], np.r_[f, 1]
    area = 0.0
    for i in range(1, len(h)):
        if f[i - 1] < f[i]:
            area += (f[i] - f[i - 1]) * h[i - 1] + 0.5 * (h[i] - h[i - 1]) * (f[i] - f[i - 1])
    return area


def zroc_slope(labels: np.ndarray, responses: np.ndarray) -> float:
    """Slope of z(hit) on z(false alarm) over the five interior points (calcZROCSlope.m)."""
    h, f = cumulative_rates(labels, responses)
    zh, zf = stats.norm.ppf(h[:-1]), stats.norm.ppf(f[:-1])
    return float(np.polyfit(zf, zh, 1)[0])


def confidence_accuracy(labels: np.ndarray, responses: np.ndarray, split: str = "fixed") -> tuple[float, float]:
    """Percent correct among high and among low confidence responses.

    ``fixed``: high is 1 or 6, low is 2 to 5 (NO_behavior_evaluateSessionStatus.m).
    ``dynamic``: high is 1 and 6, or 1, 2, 5 and 6, whichever split balances the counts better
    (NO_dynamic_lowHighSplit.m). NaN when a group has no responses.
    """
    correct = ((responses >= 4) & (labels == OLD)) | ((responses <= 3) & (labels == NEW))
    if split == "fixed":
        high = (responses == 1) | (responses == 6)
    else:
        n = [np.sum(responses == k) for k in range(1, 7)]
        c1, c2, c3 = n[0] + n[5], n[1] + n[4], n[2] + n[3]
        mode = 1 if abs(c1 - (c2 + c3)) <= abs((c1 + c2) - c3) else 2
        if n[0] == 0 or n[5] == 0:
            mode = 2
        if n[1] == 0 or n[4] == 0:
            mode = 1
        high = np.isin(responses, [1, 6]) if mode == 1 else np.isin(responses, [1, 2, 5, 6])
    low = ~high
    acc = lambda m: 100 * correct[m].mean() if m.any() else np.nan
    return acc(high), acc(low)
