"""Loading and spiking measures for the tFUS recordings of dandiset 001199.

Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23) e2218242025,
doi:10.1523/jneurosci.2218-24.2025.

Each NWB file holds sorted units (spike times only; no waveforms) and a trial table whose
`start_time` is taken as the sonication onset (the notebook checks this). The condition of a file
is written in its `identifier` and `general/notes`, in two formats:

- files of rats BH590, BH594, BH596 and BH615 (recorded 2024): identifier
  `<rat>[_tag]_<PRF>_<PD>_<UD>_<voltage>[_tags]` or `<rat>_BASELINE`, notes
  `Recording:S1; stim at:S1|POM`, and in BH596 and BH615 a `celltype_label` column that holds the
  area (S1 or POm) of each unit;
- files of rats BH608 and BH646 to BH658 (recorded 2025): identifier `<PRF>_<PD>_<UD>` or
  `no tFUS`, notes `recording:<area>;stimulation:<target>`, one file per probe.

Files are streamed from the archive at the pinned version; nothing is written to disk. Spike
times are sorted per unit on reading, as 64 units in 16 files hold a few out of order.

Where the parameters come from:

- `MIN_SPIKES = 2000`: "Only neurons that fire >2,000 spikes for each session were considered"
  (Methods, Neuronal type classification); claims file, header U.
- `PRESTIM = (-0.067, 0)`: "normalized to 67 ms before each stimulation" (Methods, same
  paragraph; Statistical analysis); claims file, header R.
- `WINDOWS`: during sonication 0 to 67 ms and postsonication 201 to 268 ms (Results, tFUS
  parameters, paragraph 1; claims file, header W), with the consecutive 67 ms windows between.
- `normalized_rates`: readings R1 (per unit, trial-averaged window rate over trial-averaged
  prestimulus rate) and R2 (per trial ratio, then the mean over trials with a prestimulus spike),
  as the claims file, header R, names them.
- `vs_baseline`: one-tailed two-sample Wilcoxon (rank-sum) test, readings T1 (window rates
  against prestimulus rates, spikes/s) and T2 (normalized values against 100%), claims file,
  header T. The Bonferroni factor is applied by the caller (readings B1 and B2 of header T).
- `SHIFT_S = 1.25` s for the clock check: half the 2.5 s intersonication interval (Methods,
  Transcranial focused ultrasound stimulation), a standard choice that puts the shifted onsets
  between sonications.
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

DANDISET_ID = "001199"
DANDISET_VERSION = "0.250829.1250"
API = "https://api.dandiarchive.org/api"

MIN_SPIKES = 2000
PRESTIM = (-0.067, 0.0)
WINDOWS = {
    "0-67": (0.0, 0.067),
    "67-134": (0.067, 0.134),
    "134-201": (0.134, 0.201),
    "201-268": (0.201, 0.268),
}
PRFS = (30, 300, 1500, 3000, 4500)
SHIFT_S = 1.25


def list_assets(version: str = DANDISET_VERSION) -> pd.DataFrame:
    """Every asset of a version: path, asset id, blob id and size."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += [{k: a[k] for k in ("path", "asset_id", "blob", "size")} for a in page["results"]]
        url = page["next"]
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def version_metadata(version: str = DANDISET_VERSION) -> dict:
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/", timeout=60).json()


def _url(asset_id: str) -> str:
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def _str(x):
    v = x[()]
    if isinstance(v, np.ndarray):   # some files store a scalar as a one-element array
        v = v.ravel()[0]
    return v.decode() if isinstance(v, bytes) else str(v)


def read_file(asset_id: str, spikes: bool = True) -> dict:
    """Read one file's metadata, trial table and (optionally) spike trains."""
    f = h5py.File(remfile.File(_url(asset_id)), "r")
    g = f["general"]
    out = {
        "identifier": _str(f["identifier"]),
        "session_start": _str(f["session_start_time"]),
        "data_collection": _str(g["data_collection"]) if "data_collection" in g else "",
        "notes": _str(g["notes"]) if "notes" in g else "",
        "subject_id": _str(g["subject/subject_id"]),
        "age": _str(g["subject/age"]),
        "sex": _str(g["subject/sex"]),
        "device": dict(g["devices/array"].attrs).get("description", "") if "devices/array" in g else "",
        "n_electrodes": g["extracellular_ephys/electrodes/id"].shape[0],
        "electrode_locations": sorted({v.decode() for v in g["extracellular_ephys/electrodes/location"][:]}),
        "units_columns": sorted(k for k in f["units"].keys()),
        "units_descriptions": {k: f["units"][k].attrs.get("description", "") for k in f["units"].keys()},
        "trial_start": f["intervals/trials/start_time"][:],
        "trial_stop": f["intervals/trials/stop_time"][:],
        "n_units": f["units/id"].shape[0],
    }
    if "celltype_label" in f["units"]:
        out["celltype_label"] = [v.decode() if isinstance(v, bytes) else str(v) for v in f["units/celltype_label"][:]]
    else:
        out["celltype_label"] = None
    if spikes:
        st = f["units/spike_times"][:]
        idx = f["units/spike_times_index"][:]
        units = np.split(st, idx[:-1])
        # Some units hold spike times out of order (a few per unit); they are sorted here, as the
        # window counts need, and the number of such units is kept for the data check.
        out["n_unsorted"] = int(sum(np.any(np.diff(u) < 0) for u in units))
        out["spikes"] = [np.sort(u) for u in units]
    f.close()
    return out


def read_many(asset_ids, spikes: bool = True, workers: int = 16) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda a: read_file(a, spikes), asset_ids))


def parse_condition(identifier: str, notes: str) -> dict:
    """PRF (Hz), PD (us), voltage (V, when written), recording area and target of a file."""
    out = {"prf": None, "pd": None, "volt": None, "sham": False, "rec": None, "target": None, "tags": ""}
    if "BASELINE" in identifier or "no tFUS" in identifier:
        out["sham"] = True
    m = re.search(r"(?:^|_)(30|300|1500|3000|4500)_(200)(?:_(67))?(?:_(5|10|15))?(?:_|$)", identifier)
    if m:
        out["prf"], out["pd"] = int(m.group(1)), int(m.group(2))
        if m.group(4):
            out["volt"] = int(m.group(4))
    m = re.search(r"recording:\s*(\w+)", notes, re.I)
    out["rec"] = m.group(1) if m else None
    m = re.search(r"(?:stimulation|stim at):\s*([^;]+)", notes, re.I)
    tgt = m.group(1).strip() if m else None
    out["target"] = "none" if out["sham"] or tgt == "no tFUS" else tgt
    tags = [t for t in ("nocoating", "coating", "NZ", "C", "P", "pom", "POm", "S1", "2mm", "break", "bad",
                         "x0y35z165", "2") if re.search(rf"_{t}(?:_|$)", identifier)]
    out["tags"] = ",".join(tags)
    return out


def unit_counts(spikes, onsets, windows: dict, prestim=PRESTIM) -> dict:
    """Spike counts per trial for each window, and for the prestimulus window.

    Returns {name: array (units, trials)} with key 'pre' for the prestimulus window."""
    onsets = np.asarray(onsets)
    allw = {"pre": prestim, **windows}
    out = {k: np.zeros((len(spikes), len(onsets))) for k in allw}
    for i, s in enumerate(spikes):
        for k, (a, b) in allw.items():
            lo = np.searchsorted(s, onsets + a, side="left")
            hi = np.searchsorted(s, onsets + b, side="left")
            out[k][i] = hi - lo
    return out


def normalized_rates(counts: dict, windows: dict, prestim=PRESTIM) -> pd.DataFrame:
    """Per unit: prestimulus and window rates (spikes/s), and normalized rates (%) under R1 and R2.

    R1: trial-averaged window rate / trial-averaged prestimulus rate x 100.
    R2: per-trial ratio x 100, averaged over trials with a prestimulus spike.
    Units with no prestimulus spike in any trial get NaN under both."""
    pre = counts["pre"] / (prestim[1] - prestim[0])
    rows = {"pre_rate": pre.mean(1)}
    has_pre = pre.sum(1) > 0
    for k, (a, b) in windows.items():
        r = counts[k] / (b - a)
        rows[f"rate_{k}"] = r.mean(1)
        with np.errstate(divide="ignore", invalid="ignore"):
            r1 = r.mean(1) / pre.mean(1) * 100
            ratio = np.where(pre > 0, r / np.where(pre > 0, pre, 1) * 100, np.nan)
            r2 = np.nanmean(ratio, axis=1)
        rows[f"R1_{k}"] = np.where(has_pre, r1, np.nan)
        rows[f"R2_{k}"] = np.where(has_pre, r2, np.nan)
    return pd.DataFrame(rows)


def vs_baseline(df: pd.DataFrame, window: str, reading: str, t: str, alternative: str = "greater") -> float:
    """One-tailed rank-sum test of a window against baseline over units (uncorrected p).

    t='T1': window rates against prestimulus rates (spikes/s).
    t='T2': normalized window values (reading R1 or R2) against 100% for every unit."""
    d = df.dropna(subset=[f"{reading}_{window}"])
    if len(d) < 2:
        return np.nan
    if t == "T1":
        x, y = d[f"rate_{window}"].values, d["pre_rate"].values
    else:
        x, y = d[f"{reading}_{window}"].values, np.full(len(d), 100.0)
    return float(stats.mannwhitneyu(x, y, alternative=alternative).pvalue)


def kruskal(groups) -> tuple[float, float]:
    groups = [np.asarray(g)[~np.isnan(g)] for g in groups]
    groups = [g for g in groups if len(g) > 0]
    if len(groups) < 2:
        return np.nan, np.nan
    h, p = stats.kruskal(*groups)
    return float(h), float(p)


def modulation_fraction(spikes, onsets, window=(0.0, 0.4), alpha=0.01) -> float:
    """Fraction of units whose count in `window` after onset differs from the count in the same
    length before onset (paired Wilcoxon over trials, two-sided)."""
    pre = (-(window[1] - window[0]), 0.0)
    c = unit_counts(spikes, onsets, {"w": window}, prestim=pre)
    sig = []
    for a, b in zip(c["w"], c["pre"]):
        if np.all(a == b):
            sig.append(False)
            continue
        sig.append(stats.wilcoxon(a, b).pvalue < alpha)
    return float(np.mean(sig)) if sig else np.nan
