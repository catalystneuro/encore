"""Loading and measures for dandiset 000114 (Carcea et al. 2021, Nature 596:553).

The dandiset holds three kinds of file:

- ``sub-V*_ecephys.nwb``: 12 to 16 h recordings from a 16-wire bundle in the PVN of virgin
  mice co-housed with a dam and litter (30 kHz raw voltage), some with a ``units`` table of
  sorted spike times and a ``behavioral_events`` table of video annotations;
- ``sub-ROV*_ophys.nwb``: fibre photometry of non-co-housed virgins during observation of dam
  retrievals ("obs") and their own retrieval tests ("retrieval"), with "Pup out" and
  "retrieval" events.

Files are streamed from the DANDI Archive with remfile and h5py at the pinned version; the
raw voltage is never read. Groups are walked by name, as h5py's ``visititems`` stalls on the
large ecephys files.

Parameters of the unit analysis, and where they come from:

- ``NEST_CAP_S = 40``: nest entry episodes are cut at 40 s (Methods, Spike train analysis).
  The paper's code has the cap commented out.
- ``GAP_S = 0.5``: the equal-duration baseline ends 0.5 s before the episode
  (``adj=0.5`` in calc_spike_freq_behavior_significance.m; the Methods do not give it).
- ``PRE_S = 10``: baseline for shepherding and dam retrieval is the 10 s before the start
  (Methods). The code uses the equal-duration baseline for every behaviour.
- ``N_SHIFTS = 1000`` and ``SHIFT_RANGE_S = 500``: the null shifts every episode of a session
  together by one integer number of seconds in [-500, 500] (Methods and code).
- ``Q = 0.05``: Benjamini-Hochberg false discovery rate (Methods).
- Labels: "Mom agressing" is shepherding, "Virgin in rest" nest entry and "Mom retrieval" dam
  retrieval, from ``behStrings`` in shepNestPup_xCorr_ForNature.m (GitHub
  ic283/Carcea-et-al.-2021, commit 2db2a75). The files do not name them.
- ``EXCEL_ROWS = 1048500``: the code's cross-correlation script drops units with more spikes
  than this (the spreadsheet row limit); used here only as a variant.
"""

from __future__ import annotations

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "000114"
DANDISET_VERSION = "0.230602.1643"

NEST_CAP_S = 40.0
GAP_S = 0.5
PRE_S = 10.0
N_SHIFTS = 1000
SHIFT_RANGE_S = 500
Q = 0.05
EXCEL_ROWS = 1048500

SHEPHERDING = ("Mom agressing", "Mom aggressing")
NEST_ENTRY = ("Virgin in rest",)
DAM_RETRIEVAL = ("Mom retrieval",)
VIRGIN_LABELS = ("Virgin in rest", "Virgin in nest", "Virgin Agressing")


def assets():
    """Path and download URL of every asset of the pinned version, sorted by path."""
    dandiset = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    out = [(a.path, a.size, a.get_content_url(follow_redirects=1, strip_query=True))
           for a in dandiset.get_assets()]
    return sorted(out)


def _open(url):
    return h5py.File(remfile.File(url), "r")


def _text(value):
    return value.decode() if isinstance(value, bytes) else str(value)


def _events(f):
    if "behavior" not in f["processing"] or "behavioral_events" not in f["processing/behavior"]:
        return pd.DataFrame(columns=["label", "start", "stop"])
    be = f["processing/behavior/behavioral_events"]
    return pd.DataFrame({"label": [_text(x) for x in be["behavior"][:]],
                         "start": be["start_time"][:], "stop": be["stop_time"][:]})


def _subject(f):
    return {k: _text(f["general/subject"][k][()]) for k in f["general/subject"]}


def load_ecephys(path, url):
    """Metadata, unit spike times and events of one ecephys file (no raw voltage)."""
    f = _open(url)
    series = {}
    for name in f["acquisition"]:
        es = f["acquisition"][name]
        rate = float(es["starting_time"].attrs["rate"])
        series[name] = {"shape": es["data"].shape, "rate": rate, "unit": _text(es["data"].attrs["unit"]),
                        "conversion": float(es["data"].attrs["conversion"]),
                        "duration_s": es["data"].shape[0] / rate}
    units, unit_names = [], []
    if "units" in f:
        st = f["units/spike_times"][:]
        idx = f["units/spike_times_index"][:]
        units = np.split(st, idx[:-1])
        unit_names = [_text(x) for x in f["units/unit_name"][:]]
    el = f["general/extracellular_ephys/electrodes"]
    s = {
        "path": path,
        "session": path.split("/")[1].replace("_ecephys.nwb", ""),
        "subject": _subject(f),
        "session_id": _text(f["general/session_id"][()]),
        "session_start_time": _text(f["session_start_time"][()]),
        "series": series,
        "channels": [_text(x) for x in el["channel_name"][:]],
        "electrode_locations": sorted({_text(x) for x in el["location"][:]}),
        "units": units,
        "unit_names": unit_names,
        "units_columns": [_text(x) for x in f["units"].attrs["colnames"]] if "units" in f else [],
        "events": _events(f),
    }
    f.close()
    return s


def load_ophys(path, url):
    """Photometry trace, the second series, timestamps, events and metadata of one ophys file."""
    f = _open(url)
    rr = f["acquisition/RoiResponseSeries"]
    s = {
        "path": path,
        "session": path.split("/")[1].replace("_ophys.nwb", ""),
        "subject": _subject(f),
        "session_id": _text(f["general/session_id"][()]),
        "session_start_time": _text(f["session_start_time"][()]),
        "t": rr["timestamps"][:],
        "f": rr["data"][:].astype(float),
        "unit": _text(rr["data"].attrs["unit"]),
        "commanded_voltage": (f["acquisition/commanded_voltage/data"][:].astype(float)
                              if "commanded_voltage" in f["acquisition"] else None),
        "fiber_location": _text(f["general/fiber_photometry/fibers/location"][0]),
        "fluorophore": _text(f["general/fiber_photometry/fluorophores/label"][0]),
        "events": _events(f),
    }
    f.close()
    return s


def session_length_s(s):
    """The longer of the recording and the last annotation, in seconds."""
    rec = max([v["duration_s"] for v in s["series"].values()] or [0.0])
    last = float(s["events"]["stop"].max()) if len(s["events"]) else 0.0
    return max(rec, last)


def episodes(events, labels, cap=None):
    """Start and stop of the episodes with one of ``labels``, sorted, stop capped at start + cap."""
    e = events[events.label.isin(labels)].sort_values("start")
    start, stop = e.start.to_numpy(float), e.stop.to_numpy(float)
    if cap is not None:
        stop = np.minimum(stop, start + cap)
    return start, stop


def baseline_windows(start, stop, baseline):
    """Baseline window per episode: 'equal' (episode's duration, ending GAP_S before start, as the
    code) or 'pre10' (the PRE_S seconds before start, as the Methods for shepherding and retrieval)."""
    if baseline == "equal":
        b1 = start - GAP_S
        return b1 - (stop - start), b1
    if baseline == "pre10":
        return start - PRE_S, start
    raise ValueError(baseline)


def _counts(spikes, a, b):
    return np.searchsorted(spikes, b, side="right") - np.searchsorted(spikes, a, side="left")


def modulation(spikes, start, stop, baseline, shift=0.0, empty_as_zero=False):
    """Mean over episodes of (behaviour - baseline) x 100 / (behaviour + baseline) firing rates.

    ``shift`` may be an array (one value per shuffle); then the result has one value per shift.
    Episodes with no spike in either window give 0/0; they are left out (``empty_as_zero`` False,
    as the code does for the real episodes) or counted as 0 (as the code does for shuffles).
    """
    shift = np.atleast_1d(np.asarray(shift, float))[:, None]
    s, e = start[None, :] + shift, stop[None, :] + shift
    b0, b1 = baseline_windows(s, e, baseline)
    rb = _counts(spikes, s, e) / (e - s)
    r0 = _counts(spikes, b0, b1) / (b1 - b0)
    with np.errstate(invalid="ignore", divide="ignore"):
        mi = (rb - r0) * 100.0 / (rb + r0)
    if empty_as_zero:
        mi = np.where(np.isnan(mi), 0.0, mi)
        out = mi.mean(1)
    else:
        n = np.sum(~np.isnan(mi), 1)
        out = np.where(n > 0, np.nansum(mi, 1) / np.maximum(n, 1), np.nan)
    return out


def shuffle_test(spikes, start, stop, baseline, shifts):
    """Real modulation, the shuffled values and the code's p-value for one unit."""
    real = modulation(spikes, start, stop, baseline)[0]
    null = modulation(spikes, start, stop, baseline, shift=shifts, empty_as_zero=True)
    if np.isnan(real):
        return real, null, np.nan
    p = np.mean(null > real) if real >= 0 else np.mean(null < real)
    return real, null, p


def bh(p, q=Q):
    """Benjamini-Hochberg: which p-values pass at false discovery rate q (NaN never passes)."""
    p = np.asarray(p, float)
    ok = ~np.isnan(p)
    out = np.zeros(len(p), bool)
    if ok.sum() == 0:
        return out
    pv = p[ok]
    order = np.argsort(pv)
    m = len(pv)
    passed = pv[order] <= q * np.arange(1, m + 1) / m
    if passed.any():
        k = np.max(np.nonzero(passed)[0])
        sig = np.zeros(m, bool)
        sig[order[:k + 1]] = True
        out[np.nonzero(ok)[0]] = sig
    return out


def draw_shifts(rng, n=N_SHIFTS):
    """Integer shifts in seconds, uniform on [-SHIFT_RANGE_S, SHIFT_RANGE_S], as MATLAB randi."""
    return rng.integers(-SHIFT_RANGE_S, SHIFT_RANGE_S + 1, size=n).astype(float)


def unit_table(sessions, labels, baseline, cap, rng, keep=None):
    """Shuffle test for every unit of every session with at least one episode of ``labels``.

    One set of shifts per session, as the code applies the same shifts to all units. Returns a
    DataFrame with one row per unit: session, mouse, unit, spikes, episodes, mi, p, activated
    (positive and BH-significant over the session's units), suppressed.
    """
    rows = []
    for s in sessions:
        if not s["units"]:
            continue
        start, stop = episodes(s["events"], labels, cap)
        if len(start) == 0:
            continue
        shifts = draw_shifts(rng)
        idx = [i for i in range(len(s["units"])) if keep is None or keep(s, i)]
        res = [shuffle_test(s["units"][i], start, stop, baseline, shifts) for i in idx]
        p = np.array([r[2] for r in res])
        sig = bh(p)
        for j, i in enumerate(idx):
            mi = res[j][0]
            rows.append({"session": s["session"], "mouse": s["subject"]["subject_id"], "unit": i,
                         "spikes": len(s["units"][i]), "episodes": len(start), "mi": mi, "p": p[j],
                         "activated": bool(sig[j] and mi > 0), "suppressed": bool(sig[j] and mi < 0)})
    return pd.DataFrame(rows)


def fisher_vs_zero(k, n):
    """The Methods' one-sided Fisher's exact test of k activated of n against 0 of n."""
    return stats.fisher_exact([[k, n - k], [0, n]], alternative="greater")[1]


def isi_violation(spikes, limit=0.002):
    """Fraction of inter-spike intervals shorter than ``limit`` seconds."""
    d = np.diff(spikes)
    return float(np.mean(d < limit)) if len(d) else np.nan


def coincident_fraction(units, tol=1e-4):
    """Fraction of a session's spikes that lie within ``tol`` s of a spike of another unit."""
    lab = np.concatenate([np.full(len(u), i) for i, u in enumerate(units)])
    t = np.concatenate(units)
    o = np.argsort(t, kind="stable")
    t, lab = t[o], lab[o]
    close = (np.diff(t) <= tol) & (lab[1:] != lab[:-1])
    hit = np.zeros(len(t), bool)
    hit[1:] |= close
    hit[:-1] |= close
    return float(hit.mean())


def onset_contrast(units, start, shifts, win=5.0):
    """Mean over units of |t| of the firing change (win s after minus win s before an onset),
    for each shift of the onsets. A shared clock predicts the largest value near shift 0 when
    the units respond to the onsets."""
    out = []
    for sh in shifts:
        on = start + sh
        tv = []
        for u in units:
            d = (_counts(u, on, on + win) - _counts(u, on - win, on)) / win
            sd = d.std(ddof=1)
            tv.append(abs(d.mean()) / (sd / np.sqrt(len(d))) if sd > 0 else 0.0)
        out.append(np.mean(tv))
    return np.array(out)


def triggered_change(t, f, times, pre=(-5.0, 0.0), post=(0.0, 5.0)):
    """Percent change of the mean signal in ``post`` against ``pre`` around each time."""
    out = []
    for e in times:
        a = f[(t >= e + pre[0]) & (t < e + pre[1])].mean()
        b = f[(t >= e + post[0]) & (t < e + post[1])].mean()
        out.append((b - a) / a * 100.0)
    return np.array(out)
