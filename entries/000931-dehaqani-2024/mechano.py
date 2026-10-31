"""Loading and checks for dandiset 000931 (Dehaqani, Michelon et al. 2024, Cell Reports 43, 114013).

doi:10.1016/j.celrep.2024.114013. The dandiset holds one NWB file, ``sub-001/sub-001.nwb``: a
Units table of spike-sorted units from one mouse, and no other data. The file is streamed from
the archive at the pinned version with ``remfile`` and read with ``h5py``; nothing is written to
disk.

Where the parameters come from:

- ``MIN_RATE_HZ`` = 0.5 Hz, the inclusion threshold for awake mice (STAR Methods, Spike sorting and
  inclusion criteria: "Single units with a firing rate of less than 0.5 Hz were excluded").
- ``ISI_THRESHOLD_S`` = 1.5 ms and the ISI violation rate of Hill et al. (2011), as in the Allen
  Institute's ``isi_violations`` metric: the Methods report an "inter-spike-interval (ISI)
  violation rate (threshold: <0.5; median: 0.01, Q1: 0, Q3: 0.04)" without giving the refractory
  period or the formula. This is a standard choice used only to compare the file with the
  reported range; it decides no claim.
- ``COINCIDENCE_S`` = 0.2 ms and ``NEAR_CHANNELS`` = 4, for the check of units deposited twice
  (protocol, Author, step 1.2). Standard choices for a check; they decide no claim.
- ``BIN_S`` = 10 ms and Welch segments of 2048 bins, for the spectrum of the population rate, a
  check that the activity carries a respiratory rhythm, as the Methods say the probe was placed
  where activity was "breathing-coupled" (Stereotaxic probe insertion). A standard choice; it
  decides no claim.
- ``CLAIM_NEEDS``: for each claim of ``claims/000931/10.1016-j.celrep.2024.114013.yaml``, the data
  its criterion uses, read from the criterion and from the STAR Methods sections it cites.
"""

from __future__ import annotations

import hashlib

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import signal

DANDISET_ID = "000931"
DANDISET_VERSION = "0.261011.1559"
API = "https://api.dandiarchive.org/api"

MIN_RATE_HZ = 0.5
ISI_THRESHOLD_S = 0.0015
COINCIDENCE_S = 0.0002
NEAR_CHANNELS = 4
BIN_S = 0.01

# What each kind of data is, and how its presence in an NWB file is tested (see `streams_present`).
STREAMS = {
    "spikes": "sorted spike times of single units",
    "breathing": "nasal airflow signal from the flow sensor, or inhalation onset, peak and offset "
                 "times (STAR Methods, Experimental signals; Analysis of the breathing signal)",
    "odor_trials": "odor onset times with the odor and concentration of each trial (Experimental "
                   "signals, the odor-trial TTL; Odor delivery)",
    "airflow_pulses": "times and flow rates of the artificial suction pulses in tracheostomized mice "
                      "(Artificial mechanical stimulation)",
    "waveforms": "mean spike waveform of each unit, for trough-to-peak latency and asymmetry "
                 "(Spike sorting and inclusion criteria)",
    "regions": "brain area of each unit (PCx layers 2 and 3, motor cortex, or the olfactory areas of "
               "fig3_C), from the probe reconstruction (Histology)",
    "other_groups": "recordings of the other experimental groups or mice the claim pools",
}

CLAIM_NEEDS = {
    "inhalation-sorting": ["breathing", "other_groups"],
    "figs1a-phase-decoding": ["spikes", "breathing", "regions", "other_groups"],
    "figs1b-speed-decoding-single-mice": ["spikes", "breathing", "odor_trials", "regions"],
    "fig1-odor-responsive-fraction": ["spikes", "odor_trials", "regions", "other_groups"],
    "fig1hi-sniff-changes-responses": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig1h-direction-of-change": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "figs1c-early-70ms": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "figs1d-rs-fs-similar": ["spikes", "breathing", "odor_trials", "waveforms", "regions", "other_groups"],
    "fig1j-sniff-change-larger-than-concentration": ["spikes", "breathing", "odor_trials", "regions",
                                                     "other_groups"],
    "fig1l-cdi-mixed-lower": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig2-glm-variance": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig2c-interaction-small": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig2d-mixed-sensitivities": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "figs2ab-rs-fs-heterogeneous": ["spikes", "breathing", "odor_trials", "waveforms", "regions",
                                    "other_groups"],
    "figs2c-waveform-no-prediction": ["spikes", "breathing", "odor_trials", "waveforms", "regions",
                                      "other_groups"],
    "figs2d-70ms-similar": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig3c-airflow-tuning-anesthetized": ["spikes", "airflow_pulses", "regions", "other_groups"],
    "fig3b-latency-shortens": ["spikes", "airflow_pulses", "regions", "other_groups"],
    "fig3f-airflow-tuning-awake": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "figs3-aen-neurectomy": ["spikes", "breathing", "regions", "other_groups"],
    "figs4-bulbectomy-no-odor-no-phase": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig4-sniff-preferring-fraction": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig4e-sniff-response-smaller": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig4f-sniff-response-more-variable": ["spikes", "breathing", "odor_trials", "regions",
                                           "other_groups"],
    "fig4g-sniff-decoding-reduced": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig4d-pre-sniff-rise": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "figs4-motor-cortex-sniff": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig5b-pc1-speed-pc23-concentration": ["spikes", "breathing", "odor_trials", "regions",
                                           "other_groups"],
    "fig5c-encoding-angles": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig5d-sniff-invariant-decoding": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "figs5gh-other-windows-and-codes": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig5ef-correlated-subpopulations": ["spikes", "breathing", "odor_trials", "regions",
                                         "other_groups"],
    "fig5gh-mechanosensitive-as-good": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig5i-time-course-similar": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "figs5i-coefficients-similar": ["spikes", "breathing", "odor_trials", "regions", "other_groups"],
    "fig6-simulation-mechanosensory-rescues": ["spikes", "breathing", "odor_trials", "regions",
                                               "other_groups"],
    "figs6h-waveforms-homogeneous": ["waveforms", "other_groups"],
}


# Archive ------------------------------------------------------------------------------------------

def versions() -> pd.DataFrame:
    """Every version of the dandiset, with its assets (path, size, SHA-256) and related papers."""
    rows = []
    listing = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/", timeout=60).json()["results"]
    for v in listing:
        name = v["version"]
        meta = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{name}/", timeout=60).json()
        assets = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{name}/assets/",
                              params={"page_size": 1000}, timeout=60).json()["results"]
        for a in assets:
            info = requests.get(f"{API}/assets/{a['asset_id']}/", timeout=60).json()
            rows.append({"version": name, "status": v["status"], "path": a["path"], "size": a["size"],
                         "asset_id": a["asset_id"],
                         "sha256": info.get("digest", {}).get("dandi:sha2-256", "")[:16],
                         "related_papers": ", ".join(r.get("identifier", r.get("url", ""))
                                                     for r in meta.get("relatedResource", [])),
                         "variables": ", ".join(meta.get("assetsSummary", {}).get("variableMeasured", [])),
                         "subjects": meta.get("assetsSummary", {}).get("numberOfSubjects")})
    return pd.DataFrame(rows)


def asset_url(path: str = "sub-001/sub-001.nwb") -> str:
    """The S3 URL of an asset of the pinned version."""
    assets = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/",
                          params={"path": path}, timeout=60).json()["results"]
    (asset,) = [a for a in assets if a["path"] == path]
    r = requests.get(f"{API}/assets/{asset['asset_id']}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


def open_file(path: str = "sub-001/sub-001.nwb") -> h5py.File:
    return h5py.File(remfile.File(asset_url(path)), "r")


# Contents -----------------------------------------------------------------------------------------

def contents(f: h5py.File) -> pd.DataFrame:
    """Every group and dataset of the file outside /specifications, with shape, type and description."""
    rows = []

    def visit(name, obj):
        if name.startswith("specifications"):
            return
        desc = obj.attrs.get("description", "")
        rows.append({"path": "/" + name,
                     "kind": "dataset" if isinstance(obj, h5py.Dataset) else "group",
                     "neurodata_type": obj.attrs.get("neurodata_type", ""),
                     "shape": obj.shape if isinstance(obj, h5py.Dataset) else "",
                     "dtype": str(obj.dtype) if isinstance(obj, h5py.Dataset) else "",
                     "description": desc if isinstance(desc, str) else str(desc)})
    f.visititems(visit)
    return pd.DataFrame(rows)


def general(f: h5py.File) -> dict:
    """The file's general metadata, decoded."""
    out = {}
    for key in ["session_description", "session_start_time", "identifier"]:
        out[key] = _text(f[key][()])
    for key, obj in f["general"].items():
        if isinstance(obj, h5py.Dataset):
            out[key] = _text(obj[()])
    for key, obj in f["general/subject"].items():
        out["subject/" + key] = _text(obj[()])
    return out


def _text(value):
    if isinstance(value, bytes):
        return value.decode()
    if isinstance(value, np.ndarray):
        return [_text(v) for v in value]
    return value


def streams_present(f: h5py.File, n_subjects: int) -> dict:
    """For each kind of data in STREAMS, whether the file holds it, and what was looked for.

    `n_subjects` is the number of subjects the archive lists for the dandiset; other groups of
    mice are present only if it is more than one."""
    def children(group):
        return list(f[group].keys()) if group in f else []

    timeseries = [g for g in ("acquisition", "processing", "stimulus/presentation", "stimulus/templates")
                  if children(g)]
    intervals = children("intervals")
    unit_cols = set(_text(f["units"].attrs["colnames"]))
    electrodes = "general/extracellular_ephys/electrodes" in f
    has_location = electrodes and "location" in f["general/extracellular_ephys/electrodes"]
    return {
        "spikes": ("spike_times" in unit_cols, "units/spike_times"),
        "breathing": (bool(timeseries), "any series in acquisition, processing or stimulus"),
        "odor_trials": (bool(intervals) or bool(children("stimulus/presentation")),
                        "any table under intervals, or a stimulus series"),
        "airflow_pulses": (bool(intervals) or bool(children("stimulus/presentation")),
                           "any table under intervals, or a stimulus series"),
        "waveforms": (bool({"waveform_mean", "waveforms"} & unit_cols), "units/waveform_mean or waveforms"),
        "regions": (has_location or "location" in unit_cols or "brain_area" in unit_cols,
                    "electrodes table with location, or a location column in units"),
        "other_groups": (n_subjects > 1, f"subjects in the dandiset: {n_subjects}"),
    }


# Units --------------------------------------------------------------------------------------------

COLUMNS = ["unit_name", "KSLabel", "quality", "sh", "ch", "depth", "Amplitude", "amp", "ContamPct",
           "fr", "n_spikes", "original_cluster_id"]


def load_units(f: h5py.File) -> tuple[pd.DataFrame, list[np.ndarray]]:
    """The Units table, every column, and each unit's spike train (seconds)."""
    u = f["units"]
    table = pd.DataFrame({c: (pd.Series(u[c][:]).map(_text) if u[c].dtype == object else u[c][:])
                          for c in COLUMNS})
    table.index = u["id"][:]
    spikes = u["spike_times"][:]
    ends = u["spike_times_index"][:].astype(int)
    starts = np.r_[0, ends[:-1]]
    trains = [spikes[a:b] for a, b in zip(starts, ends)]
    table["count"] = ends - starts
    table["first_spike"] = [t[0] if len(t) else np.nan for t in trains]
    table["last_spike"] = [t[-1] if len(t) else np.nan for t in trains]
    table["sorted"] = [bool(np.all(np.diff(t) >= 0)) for t in trains]
    return table, trains


def isi_violation_rate(train: np.ndarray, duration: float, threshold: float = ISI_THRESHOLD_S) -> float:
    """Hill et al. (2011) false-positive rate estimate, as in the Allen Institute's isi_violations."""
    n = len(train)
    if n < 2:
        return np.nan
    violations = int(np.sum(np.diff(train) < threshold))
    return violations * duration / (2 * threshold * n * n)


def presence_ratio(train: np.ndarray, duration: float, n_bins: int = 100) -> float:
    """Fraction of 100 equal blocks of the recording that hold at least one spike."""
    counts, _ = np.histogram(train, np.linspace(0, duration, n_bins + 1))
    return float(np.mean(counts > 0))


def duplicates(table: pd.DataFrame, trains: list[np.ndarray]) -> tuple[int, pd.DataFrame]:
    """Identical spike trains, and for pairs of units within NEAR_CHANNELS channels, the fraction of
    the smaller unit's spikes that have a spike of the other unit within COINCIDENCE_S."""
    digests = [hashlib.sha256(t.tobytes()).hexdigest() for t in trains]
    identical = len(digests) - len(set(digests))
    ch = table["ch"].to_numpy()
    rows = []
    for i in range(len(trains)):
        for j in range(i + 1, len(trains)):
            if abs(ch[i] - ch[j]) > NEAR_CHANNELS:
                continue
            a, b = (trains[i], trains[j]) if len(trains[i]) <= len(trains[j]) else (trains[j], trains[i])
            if len(a) == 0 or len(b) < 2:
                continue
            k = np.clip(np.searchsorted(b, a), 1, len(b) - 1)
            gap = np.minimum(np.abs(b[k] - a), np.abs(b[k - 1] - a))
            rows.append({"unit_a": table.index[i], "unit_b": table.index[j], "ch_a": ch[i], "ch_b": ch[j],
                         "spikes_smaller": len(a), "coincident": float(np.mean(gap <= COINCIDENCE_S))})
    return identical, pd.DataFrame(rows)


def rate_spectrum(trains: list[np.ndarray], duration: float) -> tuple[np.ndarray, np.ndarray]:
    """Welch spectrum of the summed spike count in BIN_S bins."""
    edges = np.arange(0, duration + BIN_S, BIN_S)
    counts, _ = np.histogram(np.concatenate(trains), edges)
    freq, power = signal.welch(counts - counts.mean(), fs=1 / BIN_S, nperseg=2048)
    return freq, power
