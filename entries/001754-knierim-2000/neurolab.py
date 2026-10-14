"""Loading and spatial measures for the Neurolab (STS-90) place cell data of dandiset 001754.

Knierim, McNaughton & Poe (2000), Nature Neuroscience 3:209-210, doi:10.1038/72910.

Each NWB file holds one rat on one day (preflight, flight day 4 or flight day 9): sorted units
(spike times in seconds, tetrode and Xclust cluster id), task epochs (BL baseline, ES Escher
staircase, MC Magic Carpet), and a table of 64 x 64 rate and occupancy maps from the original
analysis (.RMA files). The flight files also hold the video position in pixels (0 to 255), but
only at spike times: the conversion took it from the position column of the spike files. Files
are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from. The paper's Methods were not available (it is not open access),
so every parameter below is a common choice, fixed in the claims file before the analysis:

- `PX_PER_RMA_BIN = 4`: the rate maps are 64 x 64 over the 256-pixel video range; spike-count
  maps binned this way match them best (shown in the notebook's data check).
- `MERGE = 2`: spatial information and stability use 32 x 32 bins (2 x 2 rate-map bins).
- `MISSING_XY = (0, 255)`: the tracker's value for a lost position; it falls in rate-map bin
  `SENTINEL_BIN = (63, 0)`, which is left out of every occupancy.
- `UNVISITED = -999`: the rate maps' value for bins without occupancy.
- `MIN_OCC = 5` occupancy counts per bin, `MIN_SPIKES = 50` spikes at a known position per unit.
- Shuffles shift spikes circularly by at least `MIN_SHIFT_S = 20` s and take the position of the
  nearest position sample within `MAX_LOOKUP_S = 0.25` s.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter

DANDISET_ID = "001754"
DANDISET_VERSION = "0.260728.1352"

PX_PER_RMA_BIN = 4
MERGE = 2
MISSING_XY = (0.0, 255.0)
SENTINEL_BIN = (63, 0)
UNVISITED = -999.0
MIN_OCC = 5
MIN_SPIKES = 50
MIN_SHIFT_S = 20.0
MAX_LOOKUP_S = 0.25
N_SHUFFLES = 500


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    return value.decode() if isinstance(value, bytes) else str(value)


def _column(group, name):
    return [_text(v) for v in group[name][:]]


def h5_tree(path_url: tuple[str, str]) -> list[str]:
    """Every dataset in a file, with its shape, type and description or unit."""
    lines = []
    with h5py.File(remfile.File(path_url[1]), "r") as f:
        def visit(name, obj):
            if isinstance(obj, h5py.Dataset) and not name.startswith("specifications"):
                note = obj.attrs.get("description", obj.attrs.get("unit", ""))
                lines.append(f"{name}  {obj.shape}  {obj.dtype}  {_text(note)[:70]}")
        f.visititems(visit)
    return lines


def load_session(path_url: tuple[str, str]) -> dict:
    """Read one file: metadata, epochs, units, position and rate maps."""
    path, url = path_url
    with h5py.File(remfile.File(url), "r") as f:
        s = {"path": path,
             "subject": _text(f["general/subject/subject_id"][()]),
             "description": _text(f["session_description"][()]),
             "start": _text(f["session_start_time"][()])}
        s["day"] = ("preflight" if "Preflight" in s["description"]
                    else "FD4" if "Flight Day 4" in s["description"] else "FD9")
        ep = f["intervals/epochs"]
        s["epochs"] = pd.DataFrame({"start": ep["start_time"][:], "stop": ep["stop_time"][:],
                                    "type": _column(ep, "session_type")})
        u = f["units"]
        index = u["spike_times_index"][:]
        times = u["spike_times"][:]
        starts = np.concatenate([[0], index[:-1]])
        s["units"] = pd.DataFrame({"tetrode": _column(u, "tetrode"),
                                   "cluster": u["cluster_id"][:],
                                   "spikes": [times[a:b] for a, b in zip(starts, index)]})
        if "processing/behavior" in f:
            ss = f["processing/behavior/position/spatial_series"]
            s["t"] = ss["timestamps"][:]
            s["xy"] = ss["data"][:]
            s["xy_unit"] = _text(ss["data"].attrs["unit"])
            s["xy_description"] = _text(ss.attrs.get("description", ""))
        rm = f["processing/ecephys/rate_maps"]
        s["maps"] = pd.DataFrame({"tetrode": _column(rm, "tetrode"),
                                  "source_file": _column(rm, "source_file"),
                                  "type": _column(rm, "session_type"),
                                  "cell_number": rm["cell_number"][:]})
        s["rate_maps"] = rm["rate_map"][:].astype(float)
        s["occupancy_maps"] = rm["occupancy_map"][:].astype(float)
    if "xy" in s:
        s["valid"] = ~((s["xy"][:, 0] == MISSING_XY[0]) & (s["xy"][:, 1] == MISSING_XY[1]))
    return s


def load_all() -> list[dict]:
    with ThreadPoolExecutor(8) as pool:
        return list(pool.map(load_session, asset_urls()))


def label(s: dict) -> str:
    return f"{s['subject']} {s['day']}"


# ---------------------------------------------------------------- rate maps of the dandiset

def map_occupancy_groups(s: dict) -> list[tuple[str, np.ndarray, np.ndarray]]:
    """Distinct occupancy maps of a file: (session type, occupancy, row indices using it)."""
    groups = {}
    for i, (typ, occ) in enumerate(zip(s["maps"]["type"], s["occupancy_maps"])):
        groups.setdefault((typ, occ.tobytes()), (typ, occ, []))[2].append(i)
    return [(typ, occ, np.array(rows)) for typ, occ, rows in groups.values()]


def clean_occupancy(occ: np.ndarray) -> np.ndarray:
    occ = occ.astype(float).copy()
    occ[SENTINEL_BIN] = 0.0
    return occ


def skaggs_info(rate: np.ndarray, occ: np.ndarray) -> float:
    """Skaggs et al. (1993) spatial information in bits per spike, over bins with occ > 0."""
    keep = occ > 0
    p = occ[keep] / occ[keep].sum()
    r = rate[keep]
    mean = (p * r).sum()
    if mean <= 0:
        return np.nan
    nz = r > 0
    return float((p[nz] * (r[nz] / mean) * np.log2(r[nz] / mean)).sum())


def rma_info(rate_map: np.ndarray, occ_map: np.ndarray) -> tuple[float, float, float]:
    """(bits per spike, mean rate, peak rate) of one of the dandiset's rate maps."""
    occ = clean_occupancy(occ_map)
    occ[rate_map == UNVISITED] = 0
    rate = np.where(occ > 0, rate_map, 0.0)
    keep = occ > 0
    mean = float((rate[keep] * occ[keep]).sum() / occ[keep].sum())
    return skaggs_info(rate, occ), mean, float(rate[keep].max())


def rma_table(sessions: list[dict]) -> pd.DataFrame:
    """Spatial information of every distinct rate map; identical maps in a file count once."""
    rows = []
    for s in sessions:
        seen = set()
        for i, m in s["maps"].iterrows():
            key = s["rate_maps"][i].tobytes()
            duplicate = key in seen
            seen.add(key)
            info, mean, peak = rma_info(s["rate_maps"][i], s["occupancy_maps"][i])
            rows.append({"rat": s["subject"], "day": s["day"], "type": m["type"],
                         "tetrode": m["tetrode"], "source_file": m["source_file"],
                         "cel_name": "CEL" in m["source_file"].upper(),
                         "duplicate": duplicate, "info": info, "mean_rate": mean,
                         "peak_rate": peak})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- spikes and positions

def bin_xy(xy: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """(row, column) of each position on the 64 x 64 rate-map grid: row from y, column from x."""
    col = np.clip((xy[:, 0] // PX_PER_RMA_BIN).astype(int), 0, 63)
    row = np.clip((xy[:, 1] // PX_PER_RMA_BIN).astype(int), 0, 63)
    return row, col


def merge_bins(a: np.ndarray, k: int = MERGE) -> np.ndarray:
    n = a.shape[0] // k
    return a.reshape(n, k, n, k).sum(axis=(1, 3))


class PositionLookup:
    """Positions of the pooled trace (valid samples only) at arbitrary times."""

    def __init__(self, s: dict):
        keep = s["valid"]
        self.t = s["t"][keep]
        self.row, self.col = bin_xy(s["xy"][keep])

    def __call__(self, times: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """(found, row, column): found marks times with a sample within MAX_LOOKUP_S."""
        i = np.clip(np.searchsorted(self.t, times), 1, len(self.t) - 1)
        left_closer = np.abs(self.t[i - 1] - times) <= np.abs(self.t[i] - times)
        j = np.where(left_closer, i - 1, i)
        found = np.abs(self.t[j] - times) <= MAX_LOOKUP_S
        return found, self.row[j[found]], self.col[j[found]]


def count_map(rows: np.ndarray, cols: np.ndarray) -> np.ndarray:
    counts = np.zeros((64, 64))
    np.add.at(counts, (rows, cols), 1)
    return counts


def epoch_occupancy(s: dict, start: float, stop: float, typ: str) -> tuple[np.ndarray, list]:
    """The rate-map occupancy map that belongs to an epoch, and the match scores of all
    candidates of the same type: the correlation of each binary occupancy map with the binary
    histogram of the epoch's position samples."""
    m = (s["t"] >= start) & (s["t"] <= stop) & s["valid"]
    hist = count_map(*bin_xy(s["xy"][m])) > 0
    scores = []
    for t, occ, rows in map_occupancy_groups(s):
        if t == typ:
            r = np.corrcoef((clean_occupancy(occ) > 0).ravel(), hist.ravel())[0, 1]
            scores.append((float(r), int(occ.sum()), occ))
    scores.sort(key=lambda x: -x[0])
    return scores[0][2], [(r, n) for r, n, _ in scores]


def spatial_info_spikes(rows: np.ndarray, cols: np.ndarray, occ32: np.ndarray) -> float:
    counts = merge_bins(count_map(rows, cols))
    keep = occ32 >= MIN_OCC
    rate = np.where(keep, counts / np.where(keep, occ32, 1), 0.0)
    return skaggs_info(rate, np.where(keep, occ32, 0))


def epoch_units(s: dict, start: float, stop: float, typ: str, rng: np.random.Generator,
                n_shuffles: int = N_SHUFFLES) -> pd.DataFrame:
    """Spatial information of every unit in one epoch with its shuffle distribution."""
    occ, _ = epoch_occupancy(s, start, stop, typ)
    occ32 = merge_bins(clean_occupancy(occ))
    lookup = PositionLookup(s)
    duration = stop - start
    out = []
    for _, u in s["units"].iterrows():
        sp = u["spikes"][(u["spikes"] >= start) & (u["spikes"] <= stop)]
        found, r, c = lookup(sp)
        keep = occ32[r // MERGE, c // MERGE] >= MIN_OCC
        n = int(keep.sum())
        row = {"rat": s["subject"], "day": s["day"], "epoch_start": start, "tetrode": u["tetrode"],
               "cluster": int(u["cluster"]), "spikes_in_epoch": len(sp), "spikes_used": n}
        if n < MIN_SPIKES:
            out.append(row | {"info": np.nan, "p": np.nan, "null95": np.nan})
            continue
        info = spatial_info_spikes(r[keep], c[keep], occ32)
        null = np.empty(n_shuffles)
        shifts = rng.uniform(MIN_SHIFT_S, duration - MIN_SHIFT_S, n_shuffles)
        for k, shift in enumerate(shifts):
            shifted = start + (sp - start + shift) % duration
            f2, r2, c2 = lookup(shifted)
            k2 = occ32[r2 // MERGE, c2 // MERGE] >= MIN_OCC
            null[k] = spatial_info_spikes(r2[k2], c2[k2], occ32)
        out.append(row | {"info": info, "p": float((null >= info).mean()),
                          "null95": float(np.percentile(null, 95))})
    return pd.DataFrame(out)


def smoothed_rate_map(rows, cols, occ64: np.ndarray, sigma: float = 1.0) -> tuple[np.ndarray, np.ndarray]:
    """32 x 32 rate map with spike counts and occupancy each smoothed by a Gaussian (in bins);
    returns (rate, smoothed occupancy)."""
    occ32 = merge_bins(clean_occupancy(occ64))
    counts = merge_bins(count_map(rows, cols))
    sc = gaussian_filter(counts, sigma)
    so = gaussian_filter(occ32, sigma)
    rate = np.where(occ32 >= MIN_OCC, sc / np.maximum(so, 1e-9), np.nan)
    return rate, occ32
