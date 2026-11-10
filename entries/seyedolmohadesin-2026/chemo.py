"""Loading and measures for the whole-brain chemosensory recordings of dandiset 000981.

Seyedolmohadesin et al. (2026), "Whole-brain chemosensory responses of both C. elegans sexes",
Current Biology, doi:10.1016/j.cub.2026.08.040.

Each NWB file holds one animal: a table of calcium traces (`ActivityTraces`, one row per
identified head neuron, 4979 frames at 2.66 volumes/s), the neuron's NeuroPAL label, the
stimulus annotations (`StimulusInfo`, stimulus name and frame number) and the subject, whose sex
is given only in its description ("Adult hermaphrodite." or "Adult male."). Files are streamed
from the archive at the pinned version; nothing is written to disk.

Where the parameters come from. "Claims file" is claims/seyedolmohadesin-2026.yaml, whose
opening comment names the common methods (RESPONSE, EXCLUSION, CLASSES, DIMORPHISM, RESPONSIVE,
CORRELATION); "code" is https://github.com/venkatachalamlab/whole-brain-chemosensory-responses
at commit b0dbdbf50c579d056d7991b7612fcff30091ffbd, which the claims file cites.

- ON_STIM, WINDOW (40 frames) and BASELINE (10 frames): claims file, RESPONSE (Methods,
  "Calculating stimulus onset and offset responses"; code config.py and
  compile_all_traces.ipynb, `normalized_odor_response`). The code takes the onset frames from
  config.py, not from the per-recording annotations; the annotations lie 1 to 3 frames after
  them (checked in the notebook).
- A baseline of exactly 0 is replaced by 0.001, as the code does (`normalized_odor_response`);
  a detail that cannot change a result beyond the outlier rule, which removes such responses.
- IQR_FACTOR = 5 and the three 15 s windows: claims file, EXCLUSION (Methods, same section).
  The code's further filters (range of each window by the same rule; more than 7 missing
  frames of 120) are reading (b). The dandiset carries no identification confidence, so the
  code's `conf == 1` filter cannot be applied; the ignored time ranges appear already as
  missing values in the traces.
- Subclasses: claims file, CLASSES (code `separate_neuron_name`: strip a final L or R, except
  AQR and RIR). ASEL and ASER stay separate, as the claims file says. AVL is a single neuron and
  keeps its name (assumption: the code reads classes from neuron_classes.json, not in the
  repository, and AVL would otherwise become "AV"; it is the standard name of a single cell).
- COLLAPSED: code Fig5.ipynb, `collapsed`.
- LAYER: an assumption, as the claims file asks (CLASSES, OPEN). The code's neuron_classes.json
  is not public. The assignment here gives the paper's totals, 24 sensory, 36 inter, 15 motor
  and 14 pharyngeal classes: IL1 and URA are counted as motor (they are sensory-motor neurons
  with neuromuscular synapses), RMG, SAA, SAB, SIA and SIB as interneurons. Other assignments
  with the same totals are possible; the notebook lists this one.
- Band-pass filter (BP_SHORT 10, BP_LONG 240 frames, windows including the current frame),
  z-scoring, the first 96 frames blanked and frames 98 to 4978 correlated, the stimulus series
  set to 1 from 2 frames before each onset frame for 40 frames: claims file, CORRELATION (code
  compile_all_traces.ipynb `correct`, Fig4_prepare_data.ipynb).
"""

from __future__ import annotations

import re
import warnings
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "000981"
DANDISET_VERSION = "0.260910.1747"

ON_STIM = np.array("""181 340 500 660 820 980 1140 1300 1460 1620
                     1780 1940 2100 2259 2419 2579 2739 2899 3059 3219
                     3379 3539 3699 3859 4019 4179 4338 4498 4658 4818""".split(), dtype=int)
WINDOW = 40        # frames, 15 s
BASELINE = 10      # frames, 3.75 s
IQR_FACTOR = 5.0
N_FRAMES = 4979

STIMULI = ["OP50", "1uM ascr#3", "800mM Sorbitol", "10mM CuSO4", "e-6 IAA", "e-2 IAA",
           "100mM NaCl", "450mM NaCl", "Control", "Fluorescein"]
CUES = STIMULI[:8]
CUE_NAMES = {"OP50": "food", "1uM ascr#3": "pheromone", "800mM Sorbitol": "osmotic",
             "10mM CuSO4": "toxic", "e-6 IAA": "low odor", "e-2 IAA": "high odor",
             "100mM NaCl": "low salt", "450mM NaCl": "high salt", "Control": "buffer",
             "Fluorescein": "fluorescein"}
MALE_SPECIFIC = {"CEMD", "CEMV", "MCM"}

COLLAPSED = {
    "CEP": ["CEPD", "CEPV"], "IL1": ["IL1", "IL1D", "IL1V"], "IL2": ["IL2", "IL2D", "IL2V"],
    "OLQ": ["OLQD", "OLQV"], "URY": ["URYD", "URYV"], "SAA": ["SAAD", "SAAV"],
    "SAB": ["SABD", "SABV"], "SIA": ["SIAD", "SIAV"], "SIB": ["SIBD", "SIBV"],
    "RMD": ["RMD", "RMDD", "RMDV"], "RME": ["RME", "RMED", "RMEV"], "SMB": ["SMBD", "SMBV"],
    "SMD": ["SMDD", "SMDV"], "URA": ["URAD", "URAV"],
    "AS": [f"AS{i}" for i in range(1, 12)], "DA": [f"DA{i}" for i in range(1, 10)],
    "DB": [f"DB{i}" for i in range(1, 8)], "DD": [f"DD{i}" for i in range(1, 7)],
    "VA": [f"VA{i}" for i in range(1, 13)], "VB": [f"VB{i}" for i in range(1, 12)],
    "VD": [f"VD{i}" for i in range(1, 14)],
}
TO_CANONICAL = {sub: canon for canon, subs in COLLAPSED.items() for sub in subs}

LAYER_CLASSES = {
    "sensory": ["ADF", "ADL", "AFD", "ASEL", "ASER", "ASG", "ASH", "ASI", "ASJ", "ASK", "AWA",
                "AWB", "AWC", "ADE", "AQR", "BAG", "FLP", "URB", "URX", "URY", "CEP", "IL2",
                "OLL", "OLQ"],
    "inter": ["ADA", "AIA", "AIB", "AIM", "AIN", "AIY", "AIZ", "ALA", "AUA", "AVF", "AVG", "AVH",
              "AVJ", "AVK", "AVL", "RIA", "RIB", "RIC", "RID", "RIF", "RIG", "RIH", "RIM", "RIP",
              "RIR", "RIS", "RIV", "AVA", "AVB", "AVD", "AVE", "RMG", "SAA", "SAB", "SIA", "SIB"],
    "motor": ["IL1", "URA", "RMD", "RME", "RMF", "RMH", "SMB", "SMD", "AS", "DA", "DB", "DD",
              "VA", "VB", "VD"],
    "pharyngeal": ["I1", "I2", "I3", "I4", "I5", "I6", "M1", "M2", "M3", "M4", "M5", "MC", "MI",
                   "NSM"],
}
LAYER = {c: layer for layer, cs in LAYER_CLASSES.items() for c in cs}


# ---------------------------------------------------------------- loading

def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _s(x) -> str:
    return x.decode() if isinstance(x, bytes) else str(x)


def load_recording(path: str, url: str) -> dict:
    """One file: traces, labels, stimulus annotations and subject (no image data are read)."""
    with h5py.File(remfile.File(url), "r") as f:
        tab = f["processing/CalciumActivity/ActivityTraces"]
        info = f["processing/CalciumActivity/StimulusInfo"]
        subj = f["general/subject"]
        rec = {
            "path": path,
            "subject": path.split("/")[0].removeprefix("sub-"),
            "neuron": [_s(x) for x in tab["neuron"][:]],
            "group": [_s(x) for x in tab["neuron_group"][:]],
            "activity": tab["activity"][:].astype(np.float64),
            "stim_names": [_s(x) for x in info["data"][:]],
            "stim_frames": info["timestamps"][:],
            "stim_unit": _s(info["timestamps"].attrs.get("unit", "")),
            "sex_field": _s(subj["sex"][()]),
            "description": _s(subj["description"][()]),
            "strain": _s(subj["strain"][()]),
            "neuropal_ids": [_s(x) for x in
                             f["processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/ID_labels"][:]],
            "rate": float(f["acquisition/CalciumImageSeries/starting_time"].attrs["rate"]),
            "n_volumes": f["acquisition/CalciumImageSeries/data"].shape[0],
        }
    d = rec["description"].lower()
    rec["sex"] = "hermaphrodite" if "hermaphrodite" in d else ("male" if "male" in d else "?")
    cues = [n for n in rec["stim_names"] if n != "CTX"]
    rec["order"] = cues[:10]
    rec["cue_frames"] = np.array([t for n, t in zip(rec["stim_names"], rec["stim_frames"])
                                  if n != "CTX"])
    return rec


def load_all(workers: int = 6) -> list[dict]:
    """Every recording at the pinned version, streamed in parallel (about 90 s, 0.6 GB)."""
    urls = asset_urls()
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda pu: load_recording(*pu), urls))


# ---------------------------------------------------------------- classes

def subclass(neuron: str) -> str:
    """Code `separate_neuron_name`, with ASEL, ASER and AVL kept whole (see module docstring)."""
    if neuron in ("AQR", "RIR", "ASEL", "ASER", "AVL"):
        return neuron
    if neuron.endswith("L") or neuron.endswith("R"):
        return neuron[:-1]
    return neuron


def canonical(sub: str) -> str:
    """Canonical class of a subclass (code Fig5.ipynb `collapsed`)."""
    return TO_CANONICAL.get(sub, sub)


# ---------------------------------------------------------------- responses

def responses(rec: dict, rows: slice | None = None) -> pd.DataFrame:
    """Per neuron and presentation, the measures of code `normalized_odor_response`.

    avg_before, avg_during, avg_after: mean dF/F0 over the 40 frames before onset, during
    delivery and after offset, F0 the mean of the 10 frames before onset. avg_off: mean dF/F0 over
    the 40 frames after offset with F0 the 10 frames before offset. range_*: max - min in each
    window; n_nan: missing frames in the 120.
    """
    A = rec["activity"] if rows is None else rec["activity"][rows]
    names = rec["neuron"] if rows is None else rec["neuron"][rows]
    order = rec["order"]
    out = []
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        for j, on in enumerate(ON_STIM):
            seg = A[:, on - WINDOW: on + 2 * WINDOW]
            bl = np.nanmean(seg[:, WINDOW - BASELINE: WINDOW], 1)
            bl[bl == 0] = 0.001
            tr = (seg - bl[:, None]) / bl[:, None]
            blo = np.nanmean(seg[:, 2 * WINDOW - BASELINE: 2 * WINDOW], 1)
            blo[blo == 0] = 0.001
            off = (seg[:, 2 * WINDOW:] - blo[:, None]) / blo[:, None]
            w = [tr[:, :WINDOW], tr[:, WINDOW:2 * WINDOW], tr[:, 2 * WINDOW:]]
            df = pd.DataFrame({
                "subject": rec["subject"], "sex": rec["sex"], "neuron": names,
                "stimulus": order[j % 10], "position": j % 10 + 1, "cycle": j // 10 + 1,
                "avg_before": np.nanmean(w[0], 1), "avg_during": np.nanmean(w[1], 1),
                "avg_after": np.nanmean(w[2], 1), "avg_off": np.nanmean(off, 1),
                "range_before": np.nanmax(w[0], 1) - np.nanmin(w[0], 1),
                "range_during": np.nanmax(w[1], 1) - np.nanmin(w[1], 1),
                "range_after": np.nanmax(w[2], 1) - np.nanmin(w[2], 1),
                "n_nan": np.isnan(seg).sum(1),
            })
            out.append(df)
    df = pd.concat(out, ignore_index=True)
    df = df[df.n_nan < 3 * WINDOW].copy()          # all-missing presentations (code: None)
    df["subclass"] = df.neuron.map(subclass)
    df["canonical"] = df.subclass.map(canonical)
    df["side"] = [n[-1] if s != n else "" for n, s in zip(df.neuron, df.subclass)]
    return df


def _iqr_flags(g: pd.DataFrame, cols: list[str]) -> pd.Series:
    q1, q3 = g[cols].quantile(0.25), g[cols].quantile(0.75)
    lo, hi = q1 - IQR_FACTOR * (q3 - q1), q3 + IQR_FACTOR * (q3 - q1)
    return ((g[cols] < lo) | (g[cols] > hi)).any(axis=1)


def exclude(df: pd.DataFrame, reading: str) -> pd.DataFrame:
    """Claims file EXCLUSION. Reading "a": the Methods' 5 IQR rule on the three window means,
    per subclass, sex and stimulus. Reading "b": also the code's filters, as far as the dandiset
    allows (more than 7 missing frames of 120, and the same rule on the window ranges)."""
    d = df
    if reading == "b":
        d = d[d.n_nan <= 7]
    keep = np.ones(len(d), bool)
    mean_cols = ["avg_before", "avg_during", "avg_after"]
    range_cols = ["range_before", "range_during", "range_after"]
    for _, g in d.groupby(["subclass", "sex", "stimulus"]):
        bad = _iqr_flags(g, mean_cols)
        if reading == "b":
            bad = bad | _iqr_flags(g, range_cols)
        keep[d.index.get_indexer(g.index[bad.values])] = False
    return d[keep]


WINDOW_COL = {"onset": "avg_during", "offset": "avg_off"}


def ttest(x, y) -> float:
    """Two-sample t-test, equal variances (scipy default, as the code)."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    x = x[np.isfinite(x)]; y = y[np.isfinite(y)]
    if len(x) < 2 or len(y) < 2:
        return np.nan
    return float(stats.ttest_ind(x, y).pvalue)


def responsive_table(df: pd.DataFrame, level: str = "subclass") -> pd.DataFrame:
    """Claims file RESPONSIVE: per class, sex, cue and window, pooled responses against the
    pooled responses of the same class and sex to the buffer-to-buffer control."""
    rows = []
    for (cl, sex), g in df.groupby([level, "sex"]):
        ctrl = g[g.stimulus == "Control"]
        for cue in CUES:
            c = g[g.stimulus == cue]
            for win, col in WINDOW_COL.items():
                rows.append({level: cl, "sex": sex, "cue": cue, "window": win,
                             "n_cue": int(c[col].notna().sum()), "n_ctrl": int(ctrl[col].notna().sum()),
                             "mean_cue": c[col].mean(), "mean_ctrl": ctrl[col].mean(),
                             "p": ttest(c[col], ctrl[col])})
    return pd.DataFrame(rows)


def per_animal(df: pd.DataFrame, level: str = "subclass") -> pd.DataFrame:
    """Representation 3: each animal's responses averaged over cycles and sides."""
    return (df.groupby(["subject", "sex", level, "stimulus"], as_index=False)
              [["avg_during", "avg_off"]].mean())


def dimorphism_table(df: pd.DataFrame, rep: int = 1, level: str = "subclass",
                     stimuli=CUES) -> pd.DataFrame:
    """Claims file DIMORPHISM: per class, stimulus and window, hermaphrodite against male
    responses, two-sample t-test. rep 1: every cycle and side; rep 2: cycle 1 only; rep 3: per
    animal means over cycles and sides (Methods, "Identifying sexually dimorphic responses")."""
    d = df
    if rep == 2:
        d = d[d.cycle == 1]
    if rep == 3:
        d = per_animal(d, level)
    rows = []
    for (cl, cue), g in d[d.stimulus.isin(stimuli)].groupby([level, "stimulus"]):
        h, m = g[g.sex == "hermaphrodite"], g[g.sex == "male"]
        for win, col in WINDOW_COL.items():
            mh, mm = h[col].mean(), m[col].mean()
            rows.append({level: cl, "cue": cue, "window": win,
                         "n_herm": int(h[col].notna().sum()), "n_male": int(m[col].notna().sum()),
                         "mean_herm": mh, "mean_male": mm,
                         "norm_diff": abs(mm - mh) / (abs(mh) + abs(mm) + 0.1),
                         "p": ttest(h[col], m[col])})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- correlations

def ma_past(x: np.ndarray, k: int) -> np.ndarray:
    """Code `ma_past`: mean of the current and past k frames (k + 1 values; fewer at the start),
    missing values counted as 0 in the sums and the result kept missing where the input is."""
    w = k + 1
    cs = np.nancumsum(x, axis=-1)
    out = np.empty_like(cs)
    out[..., :w] = cs[..., :w] / (1 + np.arange(w))
    out[..., w:] = (cs[..., w:] - cs[..., :-w]) / w
    out[np.isnan(x)] = np.nan
    return out


def band_pass(A: np.ndarray) -> np.ndarray:
    """Code `correct`: z-score each trace, then mean of past 10 minus mean of past 240 frames,
    computed from frame 96 on (the code blanks frames 0 to 95)."""
    A = A.copy()
    A[:, :96] = np.nan
    X = A[:, 96:]
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        Z = (X - np.nanmean(X, 1, keepdims=True)) / np.nanstd(X, 1, keepdims=True)
    B = ma_past(Z, 10) - ma_past(Z, 240)
    out = np.full_like(A, np.nan)
    out[:, 96:] = B
    return out


def stimulus_series(rec: dict) -> dict[str, np.ndarray]:
    """Code Fig4_prepare_data: 1 from 2 frames before each onset frame, for 40 frames."""
    out = {}
    for i, cue in enumerate(rec["order"]):
        s = np.zeros(N_FRAMES)
        for on in ON_STIM[[i, i + 10, i + 20]]:
            s[on - 2: on - 2 + WINDOW] = 1.0
        out[cue] = s
    return out


def correlation_frame(rec: dict, filtered: bool = True, rows: slice | None = None) -> pd.DataFrame:
    """Pearson r between every pair of neurons and stimuli of one animal over frames 98 to 4978,
    pairwise complete (pandas `corr`, as the code)."""
    A = rec["activity"] if rows is None else rec["activity"][rows]
    names = rec["neuron"] if rows is None else rec["neuron"][rows]
    X = band_pass(A) if filtered else A
    S = stimulus_series(rec)
    cols = {**{c: S[c] for c in CUES}, **dict(zip(names, X))}
    df = pd.DataFrame(cols).iloc[98:]
    return df.corr()


# ---------------------------------------------------------------- connectomes (outside inputs)

COOK_SI3 = ("https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-019-1352-7/MediaObjects/"
            "41586_2019_1352_MOESM6_ESM.xlsx")   # Cook et al. 2019, SI 3, synapse counts
COOK_SI5 = ("https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-019-1352-7/MediaObjects/"
            "41586_2019_1352_MOESM9_ESM.xlsx")   # Cook et al. 2019, SI 5, EM serial sections
WITVLIET_ST4 = ("https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03778-8/MediaObjects/"
                "41586_2021_3778_MOESM4_ESM.xlsx")   # Witvliet et al. 2021, synapse count matrices
COOK_SHEETS = {COOK_SI3: ("herm chem synapse adjacency", "male chem synapse adjacency"),
               COOK_SI5: ("hermaphrodite chemical", "male chemical")}


def _sheet(content: bytes, sheet: str, pre_in_rows: bool) -> pd.DataFrame:
    import io
    x = pd.read_excel(io.BytesIO(content), sheet_name=sheet, header=None)
    m = x.iloc[3:, 3:]
    m.index, m.columns = x.iloc[3:, 2].tolist(), x.iloc[2, 3:].tolist()
    m = m.loc[[r for r in m.index if isinstance(r, str)], [c for c in m.columns if isinstance(c, str)]]
    m = m.apply(pd.to_numeric, errors="coerce").fillna(0.0)
    return m if pre_in_rows else m.T


def load_connectomes(cook_url: str) -> dict[str, pd.DataFrame]:
    """Chemical connectomes as pre x post matrices, read into memory from the journals' supplements:
    White et al. 1986 as annotated by Cook et al. 2019 ("white") and the male of Cook et al. 2019
    ("male"), from SI 3 (synapse counts) or SI 5 (EM serial sections), and Witvliet et al. 2021
    datasets 7 and 8 (synapse counts; its matrices have the presynaptic cell in columns)."""
    import requests
    cook = requests.get(cook_url, timeout=120).content
    wit = requests.get(WITVLIET_ST4, timeout=120).content
    herm_sheet, male_sheet = COOK_SHEETS[cook_url]
    return {"white": _sheet(cook, herm_sheet, True), "male": _sheet(cook, male_sheet, True),
            "witvliet7": _sheet(wit, "Dataset7", False), "witvliet8": _sheet(wit, "Dataset8", False)}
