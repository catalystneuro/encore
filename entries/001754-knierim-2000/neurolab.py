"""Loading and spatial measures for the Neurolab (STS-90) place cell data of dandiset 001754.

Knierim, McNaughton & Poe (2000), Nature Neuroscience 3(3):211-212, doi:10.1038/72910.

Each NWB file of the pinned version holds one rat on one day (preflight, flight day 4 or flight
day 9): sorted units (spike times in seconds, tetrode and Xclust cluster id), task epochs (BL
baseline, ES Escher staircase, MC Magic Carpet), and a table of 64 x 64 rate and occupancy maps
from the original analysis (one row per .RMA file, with its task type, tetrode, 8.3 short file
name and a `cell_number` read from that name). The flight files also hold the video position in
pixels (0 to 255), but only at the spike times of the file's units. Files are streamed from the
archive at the pinned version; nothing is written to disk.

Where the parameters come from.

- `ACTIVE_HZ = 0.05`: active cells have a mean firing rate above 0.05 Hz on the track (the
  paper's main text, as the claims file's criteria give it).
- `ALPHA = 0.05`, two-sided: the level of the Mann-Whitney tests, which the paper does not print;
  the claims file reads it as two-sided p < 0.05.
- Spatial information is Skaggs' information per spike, I = sum_i p_i (r_i / r) log2(r_i / r)
  (the claims file, after the paper's ref. 13), over every visited bin, off-track positions kept
  (the claims file, after the Fig. 1 legend).
- Reading M-a uses the deposited rate and occupancy maps; reading M-b recomputes rate maps from
  spikes and position on the grid of the deposited maps, without smoothing, every visited bin kept
  (the claims file's opening comment). The dandiset has no occupancy time, as position is given
  only at spike times, so M-b divides spike counts by the deposited occupancy map of the epoch.
  The claims file's opening comment now gives this (answer of 2026-10-20 in
  `questions/001754.yaml`).
- `FIELD_FRACTION = 0.2`: the field of reading (b) of the stability claim is the bins with at
  least 20% of the peak rate (the claims file, which calls it a common choice).
- `PX_PER_BIN = 4`: the maps are 64 x 64 over the 256-pixel video range, x to columns and y to
  rows; the data check shows the deposited occupancy maps match the position this way.
- `MISSING_XY = (0, 255)` is the tracker's lost position and `SENTINEL_BIN = (63, 0)` the bin in
  which the original occupancy counts it; it is not a position, so it is left out of every map.
  `UNVISITED = -999` is the rate maps' value for bins without occupancy. Both are read from the
  values in the data check.
- `LOOKUP_S = 0.001`: a spike takes the position of the sample at its own time, within 1 ms; the
  data check shows every spike of a task epoch has one. A standard tolerance that cannot change a
  result.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "001754"
DANDISET_VERSION = "0.260728.1352"

ACTIVE_HZ = 0.05
ALPHA = 0.05
FIELD_FRACTION = 0.2
PX_PER_BIN = 4
MISSING_XY = (0.0, 255.0)
SENTINEL_BIN = (63, 0)
UNVISITED = -999.0
LOOKUP_S = 0.001


def asset_urls(version: str = DANDISET_VERSION) -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at a version (default the pinned one)."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, version)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    return value.decode() if isinstance(value, bytes) else str(value)


def _column(group, name):
    return [_text(v) for v in group[name][:]]


def h5_tree(path_url: tuple[str, str]) -> list[str]:
    """Every group (with its neurodata type) and every dataset (with its shape, type and
    description or unit) in a file, outside the format specifications."""
    lines = []
    with h5py.File(remfile.File(path_url[1]), "r") as f:
        def visit(name, obj):
            if name.startswith("specifications"):
                return
            if isinstance(obj, h5py.Group):
                lines.append(f"{name}/  group  {_text(obj.attrs.get('neurodata_type', ''))}")
            else:
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
        epochs = pd.DataFrame({"start": ep["start_time"][:], "stop": ep["stop_time"][:],
                               "type": _column(ep, "session_type")}).sort_values("start")
        epochs["name"] = epochs["type"] + (epochs.groupby("type").cumcount() + 1).astype(str)
        s["epochs"] = epochs.reset_index(drop=True)
        u = f["units"]
        index = u["spike_times_index"][:]
        times = u["spike_times"][:]
        starts = np.concatenate([[0], index[:-1]])
        s["units"] = pd.DataFrame({"tetrode": _column(u, "tetrode"), "cluster": u["cluster_id"][:],
                                   "spikes": [times[a:b] for a, b in zip(starts, index)]})
        if "processing/behavior" in f:
            ss = f["processing/behavior/position/spatial_series"]
            s["t"] = ss["timestamps"][:]
            s["xy"] = ss["data"][:].astype(float)
            s["xy_unit"] = _text(ss["data"].attrs["unit"])
            s["xy_description"] = _text(ss.attrs.get("description", ""))
        rm = f["processing/ecephys/rate_maps"]
        s["maps"] = pd.DataFrame({"tetrode": _column(rm, "tetrode"), "source_file": _column(rm, "source_file"),
                                  "type": _column(rm, "session_type"), "cell_number": rm["cell_number"][:]})
        s["rate_maps"] = rm["rate_map"][:].astype(float)
        s["occupancy_maps"] = rm["occupancy_map"][:].astype(float)
    if "xy" in s:
        s["valid"] = ~((s["xy"][:, 0] == MISSING_XY[0]) & (s["xy"][:, 1] == MISSING_XY[1]))
    s["maps"]["epoch"] = assign_map_epochs(s)
    s["maps"]["duplicate"] = duplicate_rows(s["rate_maps"])
    return s


def load_all(version: str = DANDISET_VERSION) -> list[dict]:
    with ThreadPoolExecutor(8) as pool:
        return list(pool.map(load_session, asset_urls(version)))


def label(s: dict) -> str:
    return f"{s['subject']} {s['day']}"


# ---------------------------------------------------------------- maps and epochs

def clean_occupancy(occ: np.ndarray) -> np.ndarray:
    """The occupancy map without the lost position's bin."""
    occ = occ.astype(float).copy()
    occ[SENTINEL_BIN] = 0.0
    return occ


def bin_xy(xy: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """(row, column) of each position on the 64 x 64 grid: row from y, column from x."""
    col = np.clip((xy[:, 0] // PX_PER_BIN).astype(int), 0, 63)
    row = np.clip((xy[:, 1] // PX_PER_BIN).astype(int), 0, 63)
    return row, col


def count_map(rows: np.ndarray, cols: np.ndarray) -> np.ndarray:
    counts = np.zeros((64, 64))
    np.add.at(counts, (rows, cols), 1)
    return counts


def occupancy_groups(s: dict) -> list[tuple[str, bytes, np.ndarray]]:
    """Distinct occupancy maps of a file: (task type, key, row indices using it)."""
    groups = {}
    for i, (typ, occ) in enumerate(zip(s["maps"]["type"], s["occupancy_maps"])):
        groups.setdefault((typ, occ.tobytes()), []).append(i)
    return [(typ, key, np.array(rows)) for (typ, key), rows in groups.items()]


def occupancy_match(s: dict, occ: np.ndarray, start: float, stop: float) -> float:
    """Correlation of a binary occupancy map with the binary histogram of the valid position
    samples in [start, stop]."""
    m = (s["t"] >= start) & (s["t"] <= stop) & s["valid"]
    hist = count_map(*bin_xy(s["xy"][m])) > 0
    return float(np.corrcoef((clean_occupancy(occ) > 0).ravel(), hist.ravel())[0, 1])


def assign_map_epochs(s: dict) -> list[str]:
    """The epoch name (ES1, ES2, MC1, ...) of each map row. Where a file has one epoch of a type,
    its maps are that epoch's. Where it has more (Rat3 flight day 4 has two ES epochs), each
    distinct occupancy map goes to the epoch whose position samples it matches best."""
    names = [""] * len(s["maps"])
    for typ, key, rows in occupancy_groups(s):
        cands = s["epochs"][s["epochs"].type == typ]
        if len(cands) == 1:
            name = cands.name.iloc[0]
        else:
            occ = s["occupancy_maps"][rows[0]]
            scores = {n: occupancy_match(s, occ, a, b) for a, b, n in cands[["start", "stop", "name"]].itertuples(index=False)}
            name = max(scores, key=scores.get)
        for i in rows:
            names[i] = name
    return names


def duplicate_rows(rate_maps: np.ndarray) -> list[bool]:
    """True for a map identical to an earlier map of the same file (each is counted once)."""
    seen, out = set(), []
    for r in rate_maps:
        out.append(r.tobytes() in seen)
        seen.add(r.tobytes())
    return out


def skaggs_info(rate: np.ndarray, occ: np.ndarray) -> float:
    """Skaggs' spatial information in bits per spike, over bins with occ > 0."""
    keep = occ > 0
    p = occ[keep] / occ[keep].sum()
    r = rate[keep]
    mean = (p * r).sum()
    if mean <= 0:
        return np.nan
    nz = r > 0
    return float((p[nz] * (r[nz] / mean) * np.log2(r[nz] / mean)).sum())


def map_measures(rate_map: np.ndarray, occ_map: np.ndarray) -> tuple[float, float, float]:
    """(bits per spike, occupancy-weighted mean rate in Hz, peak rate) of a deposited map, over
    its visited bins."""
    occ = clean_occupancy(occ_map)
    occ[rate_map == UNVISITED] = 0
    rate = np.where(occ > 0, rate_map, 0.0)
    keep = occ > 0
    mean = float((rate[keep] * occ[keep]).sum() / occ[keep].sum())
    return skaggs_info(rate, occ), mean, float(rate[keep].max())


def epoch_occupancy(s: dict, epoch: str) -> np.ndarray:
    """The deposited occupancy map of an epoch (one distinct map per epoch, checked in the
    notebook's data check)."""
    rows = s["maps"].index[s["maps"].epoch == epoch]
    occs = {s["occupancy_maps"][i].tobytes(): s["occupancy_maps"][i] for i in rows}
    assert len(occs) == 1, (s["path"], epoch, len(occs))
    return next(iter(occs.values()))


def ma_table(sessions: list[dict]) -> pd.DataFrame:
    """Reading M-a: every deposited map, with its spatial information and mean rate. Identical
    copies within a file are marked and counted once."""
    rows = []
    for s in sessions:
        for i, m in s["maps"].iterrows():
            info, mean, peak = map_measures(s["rate_maps"][i], s["occupancy_maps"][i])
            rows.append({"rat": s["subject"], "day": s["day"], "type": m["type"], "epoch": m["epoch"],
                         "tetrode": m["tetrode"], "source_file": m["source_file"], "cell_number": int(m["cell_number"]),
                         "row": i, "duplicate": bool(m["duplicate"]), "info": info, "mean_rate": mean, "peak_rate": peak,
                         "active": (mean > ACTIVE_HZ) and not m["duplicate"]})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- spikes and position (M-b)

def spike_positions(s: dict, spikes: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """(has a valid position, row, column) for each spike: the sample at the spike's own time
    (within LOOKUP_S), dropped when there is none or it is the lost position."""
    t = s["t"]
    i = np.clip(np.searchsorted(t, spikes), 1, len(t) - 1)
    j = np.where(np.abs(t[i - 1] - spikes) <= np.abs(t[i] - spikes), i - 1, i)
    has = np.abs(t[j] - spikes) <= LOOKUP_S
    ok = has & s["valid"][j]
    row, col = bin_xy(s["xy"][j[ok]])
    return ok, row, col


def map_unit_matches(s: dict, epoch: str) -> pd.DataFrame:
    """For every distinct deposited map of a flight epoch and every unit of its tetrode with a
    spike at a position in the epoch, the correlation of the map's rate x occupancy with the
    unit's spike-count map (one row per pair; pairs with an undefined correlation are left out)."""
    a, b = s["epochs"].set_index("name").loc[epoch, ["start", "stop"]]
    maps = s["maps"][(s["maps"].epoch == epoch) & ~s["maps"].duplicate]
    rows = []
    for ui, u in s["units"].iterrows():
        ok, r, c = spike_positions(s, u.spikes[(u.spikes >= a) & (u.spikes <= b)])
        if ok.sum() == 0:
            continue
        counts = count_map(r, c).ravel()
        for i in maps.index[maps.tetrode == u.tetrode]:
            x = (np.clip(s["rate_maps"][i], 0, None) * clean_occupancy(s["occupancy_maps"][i])).ravel()
            v = np.corrcoef(x, counts)[0, 1]
            if np.isfinite(v):
                rows.append({"map_row": i, "map_name": s["maps"].source_file[i], "tetrode": u.tetrode,
                             "unit": ui, "cluster": int(u.cluster), "r": float(v)})
    return pd.DataFrame(rows)


def mb_maps(s: dict, epoch: str) -> pd.DataFrame:
    """Reading M-b for every unit of a flight file in one epoch: spike-count map over the
    deposited occupancy (unsmoothed), spatial information over every visited bin, and the unit's
    mean rate over the epoch."""
    a, b = s["epochs"].set_index("name").loc[epoch, ["start", "stop"]]
    occ = clean_occupancy(epoch_occupancy(s, epoch))
    out = []
    for ui, u in s["units"].iterrows():
        sp = u.spikes[(u.spikes >= a) & (u.spikes <= b)]
        ok, r, c = spike_positions(s, sp)
        counts = count_map(r, c)
        unvisited = int(counts[occ == 0].sum())
        rate = np.where(occ > 0, counts / np.where(occ > 0, occ, 1), 0.0)
        out.append({"rat": s["subject"], "day": s["day"], "epoch": epoch, "unit": ui, "tetrode": u.tetrode,
                    "cluster": int(u.cluster), "spikes": len(sp), "spikes_lost_position": int((~ok).sum()),
                    "spikes_unvisited_bin": unvisited, "mean_rate": len(sp) / (b - a),
                    "active": len(sp) / (b - a) > ACTIVE_HZ,
                    "info": skaggs_info(rate, occ) if counts[occ > 0].sum() > 0 else np.nan,
                    "rate_map": np.where(occ > 0, rate, np.nan)})
    return pd.DataFrame(out)


# ---------------------------------------------------------------- tests

def mean_sem(x) -> tuple[float, float]:
    x = np.asarray(x, float)
    return float(x.mean()), float(x.std(ddof=1) / np.sqrt(len(x)))


def compare(flight, pre) -> dict:
    """Means with standard errors, and the two-sided Mann-Whitney test of flight against
    preflight values."""
    flight, pre = np.asarray(flight, float), np.asarray(pre, float)
    m1, e1 = mean_sem(flight)
    m0, e0 = mean_sem(pre)
    u = stats.mannwhitneyu(flight, pre, alternative="two-sided")
    return {"n_flight": len(flight), "n_pre": len(pre), "mean_flight": round(m1, 3), "sem_flight": round(e1, 3),
            "mean_pre": round(m0, 3), "sem_pre": round(e0, 3), "difference": round(m1 - m0, 3),
            "U": float(u.statistic), "p": float(u.pvalue), "significant": bool(u.pvalue < ALPHA)}


def map_correlation(m1: np.ndarray, m2: np.ndarray, both: np.ndarray) -> float:
    """Pearson correlation of two rate maps over the bins visited in both sessions."""
    ok = both & np.isfinite(m1) & np.isfinite(m2)
    x, y = m1[ok], m2[ok]
    if x.std() == 0 or y.std() == 0:
        return np.nan
    return float(np.corrcoef(x, y)[0, 1])


def peak_in_field(m1: np.ndarray, m2: np.ndarray, both: np.ndarray, fraction: float = FIELD_FRACTION) -> bool:
    """Reading (b) of the stability claim: the peak bin of the session 3 map m2 lies in the field
    of the session 2 map m1, the bins with at least `fraction` of m1's peak rate, over bins
    visited in both sessions."""
    a = np.where(both & np.isfinite(m1), m1, -np.inf)
    b = np.where(both & np.isfinite(m2), m2, -np.inf)
    if a.max() <= 0 or b.max() <= 0:
        return False
    return bool(a[np.unravel_index(b.argmax(), b.shape)] >= fraction * a.max())
