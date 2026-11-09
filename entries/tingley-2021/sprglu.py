"""Loading and measures for dandiset 000233 (Tingley et al. 2021, Nature 597, 82-86).

The dandiset holds, per rat, NWB files of continuous recordings with the CA1 LFP
(1,250 Hz), tables of detected SPW-Rs, the iPro2 glucose sensor current (nA, one
reading every 5 min), a head accelerometer and, for some rats, sleep states.

Where each parameter comes from:

- Time base. The glucose readings are 5 min apart in the files (checked in the
  notebook). The SPW-R rate is the count of SPW-Rs in the 5-min interval that ends
  at each reading, per minute, and the glucose change ("delta current", Fig. 2a
  legend) is the difference between that reading and the one before, so that both
  describe the same interval. The claims file fixes 5-min bins aligned to the
  readings (opening comment, "Time base"); pairing the count and the change of the
  same interval is an assumption (the paper does not say), and the notebook shows
  the alignments one reading earlier and later, which move every lag by 5 min.
- An interval counts only when the LFP files cover at least 99% of it (a standard
  choice: an interval without recording has no SPW-R count).
- Cross-correlogram: correlation of SPW-R rate with delta current at offsets of
  -100 to +100 min in 5-min steps, positive offsets meaning glucose after SPW-Rs,
  pairs taken only within a continuous run of readings (claims file, opening
  comment). Pearson and Spearman are both computed (claims file, OPEN).
- Circular shuffle: SPW-R rate rotated by a random number of bins within each
  continuous run (claims file, opening comment; buzcode bz_shuffleCircular).
- SPW-R table. The CA1 SPW-R table of each file is `Ripples` or `Ca1Ripples`
  (`Dorsalripples` in the dorsal and ventral rats); its `start_time` is on the
  session clock and its `peak` is relative to the file's start (checked in the
  notebook), so the event time used is the LFP starting time plus `peak`.
"""
from __future__ import annotations

import json
import re
import urllib.request
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timedelta

import h5py
import numpy as np
import pandas as pd
import remfile

DANDISET = "000233"
VERSION = "0.250624.0414"
API = "https://api.dandiarchive.org/api"
LFP_RATE = 1250.0
STEP = 300.0  # s between glucose readings (checked in the notebook)
LAGS = np.arange(-20, 21)  # in 5-min steps, -100 to +100 min
CA1_TABLES = ("Ripples", "Ca1Ripples", "Dorsalripples")
MIN_PEAK_SD = 5.0  # Methods, SPW-R detection: "The peak power threshold was set to five s.d."
RIPPLE_COLUMNS = ("start_time", "stop_time", "peak", "duration", "peak_normed_power",
                  "peak_frequency", "peak_amplitude")


def _get(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.load(r)


def list_assets():
    """All assets of the pinned version, as a DataFrame (path, size, asset_id)."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        page = _get(url)
        out += page["results"]
        url = page["next"]
    df = pd.DataFrame([{"path": a["path"], "size": a["size"], "asset_id": a["asset_id"]} for a in out])
    df["subject"] = df.path.str.split("/").str[0].str.replace("sub-", "", regex=False)
    return df.sort_values("path").reset_index(drop=True)


def version_metadata():
    return _get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/")


def asset_url(asset_id):
    return f"{API}/assets/{asset_id}/download/"


def open_h5(asset_id):
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def read_file(asset):
    """Read what the analysis uses from one NWB file, without the signal arrays.

    Returns a dict with the session reference time, the LFP start and duration on
    the session clock, every SPW-R table (1-D columns only), the sleep states and
    which acquisition series are present.
    """
    path, aid = asset["path"], asset["asset_id"]
    for attempt in range(3):
        try:
            with open_h5(aid) as h:
                d = {"path": path, "subject": asset["subject"], "size": asset["size"],
                     "reference": _s(h["session_start_time"][()]),
                     "session_id": _s(h["general/session_id"][()]) if "general/session_id" in h else None,
                     "experiment": _s(h["general/experiment_description"][()])
                     if "general/experiment_description" in h else None,
                     "acquisition": sorted(h["acquisition"].keys()),
                     "units": "units" in h,
                     "session_description": _s(h["session_description"][()]),
                     "subject_description": _s(h["general/subject/description"][()])
                     if "general/subject/description" in h else None}
                # groups that could hold condition data: their member names, two levels down
                groups = []
                for top in ("intervals", "stimulus", "analysis", "processing", "general"):
                    if top not in h:
                        continue
                    for k, o in h[top].items():
                        groups.append(f"/{top}/{k}")
                        if isinstance(o, h5py.Group) and k not in ("extracellular_ephys",):
                            groups += [f"/{top}/{k}/{c}" for c in o.keys()]
                d["groups"] = groups
                el = h["general/extracellular_ephys/electrodes"]
                d["electrode_columns"] = sorted(el.keys())
                d["electrode_groups"] = sorted({_s(x) for x in el["group_name"][:]}) if "group_name" in el else []
                d["electrode_locations"] = sorted({_s(x) for x in el["location"][:]}) if "location" in el else []
                d["channel_names"] = [_s(x) for x in el["channel_name"][:]] if "channel_name" in el else []
                lfp = h["processing/ecephys/LFP/ElectricalSeriesLFP"]
                d["lfp_t0"] = float(lfp["starting_time"][()])
                d["lfp_rate"] = float(lfp["starting_time"].attrs["rate"])
                d["lfp_n"], d["lfp_channels"] = lfp["data"].shape
                tables, attrs = {}, {}
                for k in h["processing/ecephys"].keys():
                    if k == "LFP":
                        continue
                    g = h["processing/ecephys"][k]
                    tables[k] = pd.DataFrame({c: g[c][:] for c in RIPPLE_COLUMNS if c in g})
                    # every attribute of the table, to look for stored detection parameters
                    attrs[k] = {a: _s(v) for a, v in g.attrs.items() if a not in ("namespace", "object_id")}
                d["tables"] = tables
                d["table_attrs"] = attrs
                ss = None
                if "processing/behavior/sleep_states" in h:
                    g = h["processing/behavior/sleep_states"]
                    ss = pd.DataFrame({"start": g["start_time"][:], "stop": g["stop_time"][:],
                                       "label": [_s(x) for x in g["label"][:]]})
                d["sleep"] = ss
                acc = h["acquisition"].get("Accelerometer")
                d["acc_shape"] = acc["data"].shape if acc is not None else None
                return d
        except OSError:
            if attempt == 2:
                raise


def read_glucose(asset):
    """The glucose series of one file: timestamps (s, session clock) and current (nA)."""
    with open_h5(asset["asset_id"]) as h:
        g = h["acquisition/GlucoseLevel"]
        return {"t": g["timestamps"][:], "nA": g["data"][:], "unit": _s(g["data"].attrs["unit"]),
                "description": _s(g.attrs.get("description", ""))}


def read_all(assets, processes=16):
    """read_file on every asset, in separate processes (h5py serialises threads)."""
    with ProcessPoolExecutor(processes) as ex:
        return list(ex.map(read_file, [r for _, r in assets.iterrows()]))


def read_all_glucose(assets, processes=16):
    with ProcessPoolExecutor(processes) as ex:
        return list(ex.map(read_glucose, [r for _, r in assets.iterrows()]))


def file_start_from_name(path):
    """The date and time in a file name (yymmdd hhmmss), as written by the lab's acquisition."""
    m = re.search(r"(\d{6})[-_](\d{6})_ecephys", path)
    return datetime.strptime(m.group(1) + m.group(2), "%y%m%d%H%M%S") if m else None


def reference_time(ref):
    """The session reference time without its time zone; the notebook shows it is wall-clock time."""
    return datetime.fromisoformat(ref).replace(tzinfo=None)


def find_duplicates(files):
    """Files of one subject with the same LFP start and sample count are one recording."""
    key = [(f["subject"], round(f["lfp_t0"], 3), f["lfp_n"]) for f in files]
    groups = {}
    for i, k in enumerate(key):
        groups.setdefault(k, []).append(i)
    return [g for g in groups.values() if len(g) > 1]


def ca1_table(f):
    for name in CA1_TABLES:
        if name in f["tables"]:
            return name
    return None


def ripple_events(f, table=None):
    """SPW-R events of one file on the session clock (time = LFP start + peak)."""
    table = table or ca1_table(f)
    if table is None:
        return None
    df = f["tables"][table].copy()
    df["t"] = f["lfp_t0"] + df["peak"]
    return df


def glucose_runs(t, nA, max_gap=1.5 * STEP):
    """Sort the readings in time and number the runs of consecutive 5-min readings."""
    o = np.argsort(t, kind="stable")
    t, nA = t[o], nA[o]
    run = np.concatenate([[0], np.cumsum(np.diff(t) > max_gap)])
    return pd.DataFrame({"t": t, "nA": nA, "run": run})


def coverage(intervals, starts, stops):
    """Fraction of each interval [starts, stops) covered by the union of `intervals`."""
    iv = sorted(intervals)
    merged = []
    for a, b in iv:
        if merged and a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    if not merged:
        return np.zeros(len(starts))
    m = np.array(merged)
    cov = np.zeros(len(starts))
    for a, b in m:
        cov += np.clip(np.minimum(stops, b) - np.maximum(starts, a), 0, None)
    return cov / (stops - starts)


def binned(glu, events, file_intervals, min_cover=0.99):
    """One row per glucose reading: SPW-R count and rate over the 5 min ending at it, delta current.

    `events` is a DataFrame with a column `t`; rows whose interval is not covered by
    recording, or that start a run, have NaN rate or delta.
    """
    b = glu.copy()
    prev_t = b.t.shift(1)
    same = b.run.eq(b.run.shift(1))
    b["delta"] = np.where(same, b.nA - b.nA.shift(1), np.nan)
    starts = np.where(same, prev_t, b.t - STEP)
    b["cover"] = coverage(file_intervals, starts, b.t.values)
    et = np.sort(events.t.values) if events is not None and len(events) else np.array([])
    b["count"] = np.searchsorted(et, b.t.values, side="right") - np.searchsorted(et, starts, side="right")
    b["rate"] = np.where(b.cover >= min_cover, b["count"] / (STEP / 60), np.nan)
    return b


def lagged_pairs(b, lag, x="rate", y="delta"):
    """Pairs (x_i, y_{i+lag}) within the same run, both defined."""
    xs, ys = [], []
    for _, g in b.groupby("run"):
        xv, yv = g[x].values, g[y].values
        n = len(g)
        if abs(lag) >= n:
            continue
        if lag >= 0:
            a, c = xv[: n - lag], yv[lag:]
        else:
            a, c = xv[-lag:], yv[: n + lag]
        ok = np.isfinite(a) & np.isfinite(c)
        xs.append(a[ok])
        ys.append(c[ok])
    if not xs:
        return np.array([]), np.array([])
    return np.concatenate(xs), np.concatenate(ys)


def _corr(a, c, method):
    if len(a) < 10 or np.std(a) == 0 or np.std(c) == 0:
        return np.nan
    if method == "spearman":
        a = pd.Series(a).rank().values
        c = pd.Series(c).rank().values
    return float(np.corrcoef(a, c)[0, 1])


def xcorr(b, lags=LAGS, method="pearson", x="rate", y="delta"):
    return np.array([_corr(*lagged_pairs(b, int(k), x, y), method) for k in lags])


def circular_shuffle(b, rng, x="rate"):
    """Rotate x within each run by a random number of bins (buzcode bz_shuffleCircular)."""
    s = b.copy()
    vals = s[x].values.copy()
    for _, idx in s.groupby("run").indices.items():
        if len(idx) > 1:
            vals[idx] = np.roll(vals[idx], rng.integers(1, len(idx)))
    s[x] = vals
    return s


def clock(reference, t):
    """Wall-clock datetime of session-clock times t (s)."""
    return pd.to_datetime(reference_time(reference)) + pd.to_timedelta(np.asarray(t), unit="s")


def swap_day_month(reference, t):
    """Session-clock times with the day and month of their wall-clock date swapped when the day is 12 or less.

    Used to repair glucose timestamps whose dates were read with day and month swapped
    (shown in the notebook): a reading stored on 2021-04-03 belongs to 2021-03-04.
    """
    ref = pd.Timestamp(reference_time(reference))
    w = clock(reference, t)
    out = np.empty(len(w))
    for i, x in enumerate(w):
        if x.day <= 12:
            try:
                x = x.replace(month=x.day, day=x.month)
            except ValueError:
                pass
        out[i] = (x - ref).total_seconds()
    return out


def breaks(t, step=STEP):
    """Number of steps between time-sorted readings that are not one reading interval."""
    return int((np.abs(np.diff(np.sort(t)) - step) > 10).sum())


def repaired_glucose(reference, glu):
    """Glucose readings with dates repaired when swapping day and month leaves fewer breaks.

    Returns (DataFrame of runs, whether the swap was applied, breaks as stored, breaks swapped).
    """
    t2 = swap_day_month(reference, glu["t"])
    b1, b2 = breaks(glu["t"]), breaks(t2)
    use = b2 < b1
    return glucose_runs(t2 if use else glu["t"], glu["nA"]), use, b1, b2


def subject_files(files, subject, drop=()):
    return [f for i, f in enumerate(files) if f["subject"] == subject and i not in drop]


def clock_offset(f, reference):
    """Seconds to add to times of file f to put them on the clock of `reference`.

    Files of one subject do not all share a session reference time (shown in the notebook)."""
    return (reference_time(f["reference"]) - reference_time(reference)).total_seconds()


def subject_events(fs, tables=CA1_TABLES, min_peak_sd=MIN_PEAK_SD, reference=None):
    """SPW-R events of a subject's files (one table per file, the first of `tables` present,
    events with peak normed power of at least min_peak_sd), with the recording intervals of the
    files that have such a table, on the clock of `reference` (default: the first file's)."""
    reference = reference or fs[0]["reference"]
    ev, iv = [], []
    for f in fs:
        name = next((n for n in tables if n in f["tables"]), None)
        if name is None:
            continue
        off = clock_offset(f, reference)
        e = ripple_events(f, name)
        e = e[e.peak_normed_power >= min_peak_sd].copy()
        e["t"] += off
        e["file"] = f["path"]
        ev.append(e)
        iv.append((f["lfp_t0"] + off, f["lfp_t0"] + off + f["lfp_n"] / f["lfp_rate"]))
    if not ev:
        return None, []
    return pd.concat(ev).sort_values("t").reset_index(drop=True), iv


def time_read(asset_id, seconds=1800):
    """Seconds taken to read the first `seconds` of LFP (all channels) and of accelerometer of one file.

    Used only to estimate the cost of predictors computed from these signals."""
    import time
    with open_h5(asset_id) as h:
        t0 = time.time()
        h["processing/ecephys/LFP/ElectricalSeriesLFP/data"][: int(LFP_RATE * seconds), :]
        t1 = time.time()
        acc = h["acquisition/Accelerometer"]
        acc["data"][: int(acc["starting_time"].attrs["rate"] * seconds), :]
        return t1 - t0, time.time() - t1
