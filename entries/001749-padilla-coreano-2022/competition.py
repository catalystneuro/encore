"""Loading and behavioural measures for dandiset 001749 (Padilla-Coreano et al. 2022, Nature 603, 667-671).

Each NWB file holds one implanted mouse in one reward competition with a cagemate: the wireless
logger recording (32 channels at 20 kHz), Klusta clusters (`units`), the tone onsets
(`cs_onsets`) and reward deliveries (`us_deliveries`), and, for the mPFC-LH ("chrimson") and
mPFC-BLA ("BLA") cohorts, AlphaTracker poses of two mice, the subject's port entries
(`port_entries`) and the hand-scored labels (`manual_behavior_labels`, 20 Hz, -2 to +12 s from
each tone onset). Files are streamed from the archive at the pinned version; nothing is written
to disk.

Where the parameters come from:

- Label codes are the files' own (`LABELS`); 4 and 5 are "self in port", 6 and 7 "other in port",
  1 push, 2 resist, 3 displaced. Labels of a file are from the point of view of its subject.
- Winner of a trial (`trial_outcomes`), from the Methods, "Reward competition behavioral
  analysis": "If the port was occupied during reward delivery, winning was assigned based on who
  was at the reward port for seconds 1.5-3 post tone onset. If there was complete switch of who
  was at the reward port during the period of reward delivery the trial was considered
  complicated and not assigned as a win nor lose. If the port was unoccupied during the reward
  delivery winning and losing was assigned based on latency to enter port post-delivery of
  reward." Reward delivery is taken at 2 s after tone onset, from the Methods ("A 10uL reward of
  vanilla Ensure was delivered 2 seconds after tone onset"); the files give 0.49 s, a variant
  (`delivery_s`). How "who was at the port for 1.5-3 s" is read when the label changes inside the
  window is not given: the occupant is the mouse with more "in port" bins in the window (an
  assumption), and a "complete switch" is a window whose first and last occupied bins belong to
  different mice (an assumption). Bins labelled push, resist or displaced say nothing about who
  holds the port and are not counted as occupancy (a standard choice).
- Pushing success, from the same Methods passage: "percent of pushing that resulted in displacing
  competitor". A push is a run of bins labelled 1 in the pusher's view; it succeeded when the
  competitor's view labels any of its bins 3 (displaced), and failed when it labels them 2
  (resist). In one file the subject's displaced (3) and resist (2) bins are the competitor's
  pushes, so a file gives the competitor's success directly; the subject's own success needs the
  competitor's file (`push_success`).
- Latency to pick up the reward (ED Fig. 5d): first bin at or after tone onset in which the
  winner is in the port; read from tone onset (Methods 5 and ED Fig. 1a count latency from tone
  onset) and from delivery (a constant 2 s less).
- Spike times: the stored `spike_times` are two thirds of the time of the same spikes in the
  `ElectricalSeries` (shown in the notebook), so `SPIKE_TIME_SCALE` = 1.5 converts them.
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.signal import butter, correlate, sosfiltfilt

DANDISET_ID = "001749"
DANDISET_VERSION = "0.260311.1727"

LABELS = {1: "push", 2: "resist", 3: "displaced", 4: "self in port, other close",
          5: "self in port, other far", 6: "other in port, self close", 7: "other in port, self far",
          8: "close to other, far from port", 9: "alone and far from port"}
SELF_IN = (4, 5)
OTHER_IN = (6, 7)
MIRROR_POSITION = {4: 6, 5: 7, 6: 4, 7: 5, 8: 8, 9: 9}  # position codes in the competitor's view (see notebook)
LABEL_HZ = 20.0
LABEL_START_S = -2.0
WIN_WINDOW_S = (1.5, 3.0)      # Methods, Reward competition behavioral analysis
DELIVERY_S = 2.0               # Methods 5: reward 2 s after tone onset
TONE_S = 10.0                  # Methods 5: 10 s tone
SPIKE_TIME_SCALE = 1.5         # shown in the notebook from the raw recording
FS = 20000.0


def assets() -> list[dict]:
    """NWB assets of the pinned version: path, asset id, S3 URL and size."""
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    out = []
    for a in ds.get_assets():
        if a.path.endswith(".nwb"):
            out.append({"path": a.path, "asset_id": a.identifier, "url": a.get_content_url(follow_redirects=1, strip_query=True),
                        "size": a.size})
    return sorted(out, key=lambda a: a["path"])


def open_nwb(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


NAME = re.compile(r"sub-(\d{8})-([A-Za-z]+)(\d)-(\d)-(\d)v(\d)")


def parse_name(path: str) -> dict:
    """Date, cohort, cage, animal and the pair from a file name such as sub-20200121-BLA2-2-1v2."""
    m = NAME.match(path.split("/")[0])
    date, cohort, cage, animal, a, b = m.groups()
    other = b if animal == a else a
    return {"date": date, "cohort": {"ephys": "mPFC", "chrimson": "mPFC-LH", "BLA": "mPFC-BLA"}[cohort],
            "cage": f"{cohort}{cage}", "animal": int(animal), "other_animal": int(other), "pair": f"{a}v{b}",
            "mouse": f"{cohort}{cage}-{animal}", "competitor": f"{cohort}{cage}-{other}"}


RANK = re.compile(r"Mouse\s*(\d)\s*\(social rank (\d)")
OTHER_RANK = re.compile(r"cagemate mouse\s*(\d)\s*\(social rank (\d)")


def load_file(a: dict) -> dict:
    """Everything the behavioural analysis uses from one file, and the shapes of the rest."""
    f = open_nwb(a["url"])
    meta = parse_name(a["path"])
    desc = f["general/subject/description"][()].decode()
    m1, m2 = RANK.search(desc), OTHER_RANK.search(desc)
    r = dict(meta, path=a["path"], subject_id=f["general/subject/subject_id"][()].decode(), description=desc,
             session_start=f["session_start_time"][()].decode(),
             pair_in_dataset=f["general/lab_meta_data/session_pairing/pair_in_dataset"][()].decode(),
             rank=int(m1.group(2)), desc_animal=int(m1.group(1)), other_rank=int(m2.group(2)), desc_other=int(m2.group(1)),
             video=f["acquisition/BehaviorVideo"].attrs["description"])
    es = f["acquisition/ElectricalSeries"]
    r["es_shape"] = es["data"].shape
    r["es_rate"] = float(es["starting_time"].attrs["rate"])
    r["es_unit"] = es["data"].attrs["unit"]
    r["cs"] = f["intervals/cs_onsets/start_time"][:]
    r["cs_stop"] = f["intervals/cs_onsets/stop_time"][:]
    r["us"] = f["intervals/us_deliveries/start_time"][:]
    if "port_entries" in f["intervals"]:
        r["pe_start"] = f["intervals/port_entries/start_time"][:]
        r["pe_stop"] = f["intervals/port_entries/stop_time"][:]
    else:
        r["pe_start"] = r["pe_stop"] = None
    if "behavior" in f["processing"]:
        ts = f["processing/behavior/BehavioralLabels/manual_behavior_labels"]
        r["labels"] = ts["data"][:].T.astype(int)          # trials x bins
        r["label_rate"] = float(ts["starting_time"].attrs["rate"])
    else:
        r["labels"] = None
    r["pose_modules"] = sorted(k for k in f["processing"] if k.startswith("behavior_"))
    idx = f["units/spike_times_index"][:]
    r["n_units"] = len(idx)
    r["quality"] = sorted(set(f["units/quality"][:].astype(str)))
    r["spike_counts"] = np.diff(np.r_[0, idx])
    st = f["units/spike_times"]
    r["last_spike"] = float(np.max(st[np.unique(idx[idx > 0]) - 1])) if np.any(idx > 0) else np.nan
    return r


def load_all(threads: int = 12) -> list[dict]:
    al = assets()
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(load_file, al))


def session_key(r: dict) -> tuple:
    """A competition session: the date in the file name, the cage and the pair."""
    return (r["date"], r["cage"], r["pair"])


# ---------------------------------------------------------------- trial outcomes from the labels

def _occupant(row: np.ndarray, i0: int, i1: int) -> tuple[int, int, int | None, int | None]:
    seg = row[i0:i1]
    s = np.isin(seg, SELF_IN)
    o = np.isin(seg, OTHER_IN)
    occ = np.where(s, 1, np.where(o, -1, 0))
    nz = occ[occ != 0]
    first = int(nz[0]) if len(nz) else None
    last = int(nz[-1]) if len(nz) else None
    return int(s.sum()), int(o.sum()), first, last


def trial_outcomes(labels: np.ndarray, delivery_s: float = DELIVERY_S, switch_rule: str = "first_last") -> np.ndarray:
    """Per trial, 'win', 'lose' or 'excluded' for the file's subject (see module docstring).

    switch_rule 'first_last': a trial is a switch when the first and last occupied bins of the
    1.5-3 s window belong to different mice; 'any': when both mice are in the port in the window.
    """
    b = lambda t: int(round((t - LABEL_START_S) * LABEL_HZ))
    i0, i1 = b(WIN_WINDOW_S[0]), b(WIN_WINDOW_S[1])
    idel = b(delivery_s)
    out = []
    for row in labels:
        at_delivery = row[idel]
        occupied = at_delivery in SELF_IN or at_delivery in OTHER_IN
        if occupied:
            ns, no, first, last = _occupant(row, i0, i1)
            switch = (first is not None and last is not None and first != last) if switch_rule == "first_last" else (ns > 0 and no > 0)
            if switch:
                out.append("excluded")
            elif ns > no:
                out.append("win")
            elif no > ns:
                out.append("lose")
            else:
                out.append("excluded")
        else:
            after = row[idel:]
            s = np.flatnonzero(np.isin(after, SELF_IN))
            o = np.flatnonzero(np.isin(after, OTHER_IN))
            if len(s) == 0 and len(o) == 0:
                out.append("excluded")
            elif len(o) == 0 or (len(s) and s[0] < o[0]):
                out.append("win")
            elif len(s) == 0 or o[0] < s[0]:
                out.append("lose")
            else:
                out.append("excluded")
    return np.array(out)


def latency_to_port(labels: np.ndarray, who: str = "self") -> np.ndarray:
    """Seconds from tone onset to the first bin at or after onset with `who` in the port (NaN if never)."""
    codes = SELF_IN if who == "self" else OTHER_IN
    i_on = int(round(-LABEL_START_S * LABEL_HZ))
    out = []
    for row in labels:
        k = np.flatnonzero(np.isin(row[i_on:], codes))
        out.append(k[0] / LABEL_HZ if len(k) else np.nan)
    return np.array(out)


def runs(mask: np.ndarray) -> list[tuple[int, int]]:
    """Start and stop (exclusive) of each run of True."""
    m = np.r_[False, mask, False].astype(int)
    d = np.diff(m)
    return list(zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1)))


def push_success(pusher: np.ndarray, target: np.ndarray, bins: slice = slice(None)) -> tuple[int, int]:
    """Pushes by the mouse whose view is `pusher` and how many displaced the competitor.

    `pusher` and `target` are trials x bins label arrays of the two views of one session. A push
    (run of 1 in the pusher's view) succeeded when the target's view has a 3 in it.
    """
    n = s = 0
    for rp, rt in zip(pusher[:, bins], target[:, bins]):
        for a0, a1 in runs(rp == 1):
            n += 1
            s += bool(np.any(rt[a0:a1] == 3))
    return n, s


def competitor_push_success(labels: np.ndarray, bins: slice = slice(None)) -> tuple[int, int]:
    """Pushes by the competitor, seen in the subject's own file: runs of 2 or 3; success = runs with a 3."""
    n = s = 0
    for row in labels[:, bins]:
        for a0, a1 in runs(np.isin(row, (2, 3))):
            n += 1
            s += bool(np.any(row[a0:a1] == 3))
    return n, s


# ---------------------------------------------------------------- clocks

BAND = butter(3, [600, 6000], btype="band", fs=FS, output="sos")


def raw_crossings(f: h5py.File, t0: float, dur: float, n_sd: float = 4.0) -> np.ndarray:
    """Times (s, in the recording's clock) of negative threshold crossings on any channel.

    Band 600 to 6,000 Hz and common average reference as in Methods 11 (recording); threshold at
    4 SD (median-based) as for the multi-unit rates of Methods 17.
    """
    x = f["acquisition/ElectricalSeries/data"][int(t0 * FS):int((t0 + dur) * FS), :].astype(np.float32)
    x = sosfiltfilt(BAND, x, axis=0)
    x -= np.median(x, axis=1, keepdims=True)
    sd = np.median(np.abs(x), axis=0) / 0.6745
    cr = (x[1:] < -n_sd * sd) & (x[:-1] >= -n_sd * sd)
    return np.flatnonzero(cr.any(axis=1)) / FS + t0


def spike_raw_xcorr(f: h5py.File, scale: float, t0: float, dur: float = 20.0, max_lag: float = 60.0, bw: float = 0.001):
    """Peak of the cross-correlation of all units' spikes (times x scale) with raw crossings.

    Returns the lag (s) of the peak and its height in SD of the correlation over lags (-60 to
    +60 s). A positive lag means a spike at time t (scaled) is seen in the recording at t - lag.
    """
    rt = raw_crossings(f, t0, dur)
    st = f["units/spike_times"][:] * scale
    R = np.histogram(rt, np.arange(t0, t0 + dur, bw))[0].astype(float)
    R -= R.mean()
    S = np.histogram(st, np.arange(t0 - max_lag, t0 + dur + max_lag, bw))[0].astype(float)
    cc = correlate(S - S.mean(), R, mode="valid", method="fft")
    lags = np.arange(len(cc)) * bw - max_lag
    j = int(np.argmax(cc))
    return float(lags[j]), float((cc[j] - cc.mean()) / cc.std())


def spike_units(f: h5py.File, scale: float = SPIKE_TIME_SCALE) -> list[np.ndarray]:
    st = f["units/spike_times"][:] * scale
    idx = f["units/spike_times_index"][:]
    return np.split(st, idx[:-1])


def event_lag_scan(units: list[np.ndarray], events: np.ndarray, lags: np.ndarray, bw: float = 0.05, w: int = 20,
                   min_spikes: int = 200, max_spikes: int = 200000) -> np.ndarray:
    """For each lag, the mean over units of t^2 of (spikes 0 to 1 s after) minus (1 to 0 s before) an event.

    Events are placed at events + lag in the spike clock. A lag at which units respond to the
    events gives a peak; elsewhere the value is near its null of about 1.
    """
    units = [u for u in units if min_spikes < len(u) < max_spikes]
    lo = min(0.0, float(events.min() + lags.min())) - 5
    hi = max(max(u.max() for u in units), float(events.max() + lags.max())) + 5
    edges = np.arange(lo, hi, bw)
    H = np.array([np.histogram(u, edges)[0] for u in units], dtype=np.float32)
    C = np.cumsum(np.c_[np.zeros(len(units), dtype=np.float32), H], axis=1)
    out = np.zeros(len(lags))
    for j, lag in enumerate(lags):
        i0 = ((events + lag - lo) / bw).astype(int)
        i0 = i0[(i0 - w >= 0) & (i0 + w < C.shape[1])]
        if len(i0) < 10:
            continue
        d = (C[:, i0 + w] - C[:, i0]) - (C[:, i0] - C[:, i0 - w])
        t = d.mean(1) / (d.std(1) / np.sqrt(d.shape[1]) + 1e-9)
        out[j] = np.mean(t ** 2)
    return out


def port_occupancy_on_label_grid(r: dict, lag: float = 0.0) -> np.ndarray:
    """1 where the file's port entries say the subject is in the port, on the label bins of each trial."""
    tb = np.arange(r["labels"].shape[1]) / LABEL_HZ + LABEL_START_S
    s, e = r["pe_start"], r["pe_stop"]
    occ = np.zeros(r["labels"].shape)
    for j in range(min(len(r["cs"]), r["labels"].shape[0])):
        t = r["cs"][j] + lag + tb
        i = np.searchsorted(s, t, side="right") - 1
        occ[j] = (i >= 0) & (t < e[np.clip(i, 0, None)])
    return occ


def clock_checks(a: dict, raw_t0: float = 300.0, lags: np.ndarray | None = None) -> dict:
    """Clock checks of one file: spikes against the raw recording, and spikes against port entries.

    - Spikes against the raw recording: the cross-correlation peak of the stored spike times, and
      of the spike times times 1.5, with threshold crossings of 20 s of the ElectricalSeries.
    - Spikes against the trial tables: `event_lag_scan` of the port entries over offsets of -300
      to +300 s (0.1 s steps), with spike times times 1.5. The 99th percentile over offsets is
      the reference for the peak.
    """
    if lags is None:
        lags = np.arange(-300, 300, 0.1)
    f = open_nwb(a["url"])
    out = {"path": a["path"]}
    for scale in (1.0, SPIKE_TIME_SCALE):
        lag, z = spike_raw_xcorr(f, scale, raw_t0)
        out[f"raw_lag_{scale}"], out[f"raw_peak_sd_{scale}"] = lag, z
    if "port_entries" in f["intervals"]:
        ev = f["intervals/port_entries/start_time"][:]
        units = spike_units(f)
        sc = event_lag_scan(units, ev, lags)
        j = int(np.argmax(sc))
        out.update(pe_lag=float(lags[j]), pe_peak=float(sc[j]), pe_p99=float(np.percentile(sc, 99)),
                   pe_median=float(np.median(sc)), pe_at_zero=float(sc[np.argmin(np.abs(lags))]), n_entries=len(ev))
        cs = f["intervals/cs_onsets/start_time"][:]
        sc2 = event_lag_scan(units, cs, lags, w=40)
        out.update(cs_at_pe_lag=float(sc2[j]), cs_p99=float(np.percentile(sc2, 99)))
    return out


def pose_summary(a: dict) -> dict:
    """Fraction of frames without a position, per pose module, and the frame times."""
    f = open_nwb(a["url"])
    out = {"path": a["path"]}
    for m in sorted(k for k in f["processing"] if k.startswith("behavior_Mouse")):
        name = m.split("_")[1]
        g = f[f"processing/{m}/PoseEstimation_{name}"]
        parts = sorted(g.keys())
        d = g[parts[0]]["data"]
        ts = g[parts[0]]["timestamps"]
        x = d[:, 0]
        out[f"{name}_frames"] = len(x)
        out[f"{name}_nan"] = float(np.isnan(x).mean())
        out[f"{name}_t0"], out[f"{name}_t1"] = float(ts[0]), float(ts[-1])
        out["parts"] = ",".join(p.split("_", 1)[1] for p in parts)
    return out
