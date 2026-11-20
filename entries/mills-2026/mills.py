"""Loading and measures for DANDI:001203 (Mills et al. 2026, amygdalostriatal transition zone).

Every file is streamed from the archive at the pinned version with remfile and h5py; nothing is
written to disk. Where a parameter comes from is said beside it:

- "paper" with the passage: taken from the paper (author, step 1.6) or the claims file.
- "assumption": a choice the paper leaves open, stated in the attempt record.
- "standard choice": a detail that cannot change a result.
"""
import json
import warnings
import urllib.request
from functools import lru_cache

import h5py
import numpy as np
import remfile

DANDISET = "001203"
VERSION = "0.261103.1719"
API = "https://api.dandiarchive.org/api"


# ---------------------------------------------------------------- archive access
@lru_cache(maxsize=1)
def assets():
    """All assets of the pinned version, as a list of dicts with path, asset_id and size."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += page["results"]
        url = page["next"]
    return out


def nwb_assets():
    return sorted([a for a in assets() if a["path"].endswith(".nwb")], key=lambda a: a["path"])


def open_nwb(path):
    """Open one NWB asset (by its full path in the dandiset) as a streamed h5py file."""
    a = next(a for a in assets() if a["path"] == path)
    url = f"{API}/assets/{a['asset_id']}/download/"
    return h5py.File(remfile.File(url), "r")


def _s(x):
    x = x[()]
    return x.decode() if isinstance(x, bytes) else x


def series_times(g, n):
    """Timestamps of a TimeSeries group: its timestamps, or starting_time and rate."""
    if "timestamps" in g:
        return g["timestamps"][:]
    st = g["starting_time"]
    return st[()] + np.arange(n) / float(st.attrs["rate"])


def _strs(ds):
    return np.array([v.decode() if isinstance(v, bytes) else v for v in ds[:]])


# ---------------------------------------------------------------- file inventory
def describe_ecephys(f):
    """Metadata of an ecephys file: subject, group description, electrode locations, tables present."""
    sub = f["general/subject"]
    loc = _strs(f["general/extracellular_ephys/electrodes/location"])
    r = {
        "subject_id": _s(sub["subject_id"]),
        "subject_description": _s(sub["description"]) if "description" in sub else "",
        "session_start": _s(f["session_start_time"]),
        "locations": sorted(set(loc)),
        "n_units": f["units/id"].shape[0],
        "has_trials": "intervals/trials" in f,
        "has_pose": "processing/behavior" in f,
        "units_description": str(f["units"].attrs.get("description", "")),
    }
    if "firing_rate" in f["units"]:
        r["n_units_below_50Hz"] = int((f["units/firing_rate"][:] < 50).sum())
    return r


# ---------------------------------------------------------------- Open Ephys sessions
def spike_trains(f, table="units"):
    st = f[f"{table}/spike_times"][:]
    idx = f[f"{table}/spike_times_index"][:]
    starts = np.concatenate([[0], idx[:-1]])
    return [st[a:b] for a, b in zip(starts, idx)]


def trials_by_type(f):
    """{trial_type: (start_times, stop_times)} from intervals/trials."""
    t = f["intervals/trials"]
    tt = _strs(t["trial_type"])
    st, sp = t["start_time"][:], t["stop_time"][:]
    return {k: (st[tt == k], sp[tt == k]) for k in np.unique(tt)}


def load_oe(path, pose=True):
    """One Open Ephys session: curated unit spike trains, cue onsets, port entries and pose.

    CS onsets are the start times of the 'shock_stimulus_presentation' and
    'reward_stimulus_presentation' trials. The CS-reward stop time is when the tone ended; the
    paper says collecting the reward ends the tone (STAR Methods, Two-tone discrimination tasks).
    """
    f = open_nwb(path)
    tr = trials_by_type(f)
    d = {
        "path": path,
        "subject_id": _s(f["general/subject/subject_id"]),
        "location": sorted(set(_strs(f["general/extracellular_ephys/electrodes/location"]))),
        "spikes": spike_trains(f, "units"),
        "unit_names": _strs(f["units/unit_name"]) if "unit_name" in f["units"] else None,
        "shock_on": tr["shock_stimulus_presentation"][0],
        "shock_off": tr["shock_stimulus_presentation"][1],
        "reward_on": tr["reward_stimulus_presentation"][0],
        "reward_off": tr["reward_stimulus_presentation"][1],
        "port_on": tr["port_entry"][0] if "port_entry" in tr else np.array([]),
        "port_off": tr["port_entry"][1] if "port_entry" in tr else np.array([]),
        "reward_delivery": tr["reward_delivery"][0] if "reward_delivery" in tr else np.array([]),
        "shock_relay": tr["shock_relay"][0] if "shock_relay" in tr else np.array([]),
        "duration": f["acquisition/ElectricalSeries/data"].shape[0] / 30000.0,
    }
    if pose:
        d["pose_t"], d["pose"] = load_pose(f)
    return d


# ---------------------------------------------------------------- pose and behaviour
NODES = ["Nose", "LeftEarTip", "LeftEarBase", "RightEarBase", "RightEarTip", "SkullBase", "Shoulders",
         "Haunch", "TailBase", "TailSeg", "LeftArm", "RightArm", "RightLeg", "LeftLeg"]


def load_pose(f):
    """SLEAP pose: timestamps (s) and an array frames x 14 nodes x 2 (pixels)."""
    P = f["processing/behavior/PoseEstimationTrack0"]
    xy = np.stack([P[f"PoseEstimationSeries{n}/data"][:].astype(np.float32) for n in NODES], axis=1)
    t = series_times(P["PoseEstimationSeriesNose"], xy.shape[0])
    return t, xy


ARENA_CM = (40.0, 30.0)  # paper: operant chambers 30 x 40 cm (STAR Methods, Behavioral analysis)


def pixels_per_cm(xy):
    """Pixel scale from the extent of the body points against the 40 x 30 cm floor.

    Assumption: the 0.5th to 99.5th percentile of all body-point positions spans the chamber floor
    along each axis; the scale is the mean of the two axes' estimates. The files give positions in
    pixels with no scale.
    """
    x = xy[..., 0].ravel()
    y = xy[..., 1].ravel()
    ex = np.nanpercentile(x, 99.5) - np.nanpercentile(x, 0.5)
    ey = np.nanpercentile(y, 99.5) - np.nanpercentile(y, 0.5)
    long_, short = max(ex, ey), min(ex, ey)
    return float(np.mean([long_ / ARENA_CM[0], short / ARENA_CM[1]]))


def behaviour_frames(xy, ppc, freeze_cm=0.08, dart_cms=45.0, fps=30.0, freeze_rule="max"):
    """Per-frame freezing and darting.

    Paper (STAR Methods, Behavioral analysis of two-tone discrimination task): freezing when "the
    total displacement of ALL mouse body points was less than 0.08 cm per frame"; darting when "the
    center point of the mouse rear body reached a velocity of 45 cm/s". The rear body centre is
    taken as the Haunch node (assumption; the skeleton has no node of that name). "Total
    displacement of all body points" has two readings: freeze_rule "max", every point moved less
    than 0.08 cm; "sum", the summed displacement of the points is below 0.08 cm. Frames with a
    missing point count as not freezing under either rule. Darting speed is taken over one frame.
    """
    disp = np.linalg.norm(np.diff(xy, axis=0), axis=2) / ppc  # cm per frame, frames-1 x nodes
    if freeze_rule == "max":
        frz = np.nanmax(np.where(np.isnan(disp), np.inf, disp), axis=1) < freeze_cm
    else:
        frz = np.where(np.isnan(disp).any(axis=1), np.inf, np.nansum(disp, axis=1)) < freeze_cm
    sp = disp[:, NODES.index("Haunch")] * fps
    dart = np.nan_to_num(sp, nan=0.0) >= dart_cms
    frz = np.concatenate([[False], frz])
    dart = np.concatenate([[False], dart])
    return frz, dart


def window_fraction(t, flag, onsets, dur):
    """Fraction of frames with flag set in [onset, onset+dur) for each onset."""
    out = []
    for o in onsets:
        a, b = np.searchsorted(t, [o, o + dur])
        out.append(flag[a:b].mean() if b > a else np.nan)
    return np.array(out)


# ---------------------------------------------------------------- spike measures
def binned(spikes, onsets, t0, t1, width):
    """Spike counts, trials x bins, in bins of `width` s from t0 to t1 around each onset."""
    edges = np.arange(t0, t1 + width / 2, width)
    out = np.empty((len(onsets), len(edges) - 1))
    for i, o in enumerate(onsets):
        out[i] = np.histogram(spikes - o, edges)[0]
    return out, edges[:-1] + width / 2


def cue_z(spikes, onsets, width, t0=-20.0, t1=20.0):
    """Trial-averaged firing rate z-scored by the mean and SD of the 20 s before cue onset.

    Paper (STAR Methods, Analysis of neural responses to cue delivery). Returns z trace and bin
    centres. A neuron with no baseline variance gets NaN.
    """
    c, centres = binned(spikes, onsets, t0, t1, width)
    m = c.mean(axis=0) / width
    base = m[centres < 0]
    sd = base.std(ddof=1)
    z = (m - base.mean()) / sd if sd > 0 else np.full_like(m, np.nan)
    return z, centres


PHASIC = (0.0, 0.1)      # paper: 0-100 ms after cue onset
SUSTAINED = (0.1, 19.0)  # paper: 0.1-19 s after cue onset


def window_mean(z, centres, win):
    sel = (centres > win[0]) & (centres < win[1])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return np.nanmean(z[..., sel], axis=-1)


# ---------------------------------------------------------------- calcium imaging
def load_ophys(path, pose=True):
    """One imaging session: traces (frames x ROIs), timestamps, CS onsets of imaged trials.

    F is processing/ophys/Fluorescence/RoiResponseSeries (raw CNMF-E fluorescence) and D the
    Deconvolved series. CS onsets are stimulus_events start times that fall inside an imaged
    trial of intervals/trials, with the type of the event.
    """
    f = open_nwb(path)
    g = f["processing/ophys/Fluorescence/RoiResponseSeries"]
    F = g["data"][:]
    t = series_times(g, F.shape[0])
    D = f["processing/ophys/Fluorescence/Deconvolved/data"][:]
    d = {"path": path, "F": F, "D": D, "t": t,
         "subject_id": _s(f["general/subject/subject_id"]),
         "genotype": _s(f["general/subject/genotype"]),
         "session_description": _s(f["session_description"])}
    if "processing/behavior/stimulus_events" in f:
        ev = f["processing/behavior/stimulus_events"]
        on, typ = ev["start_time"][:], _strs(ev["trial_type"])
        tr = f["intervals/trials"]
        ts, te = tr["start_time"][:], tr["stop_time"][:]
        imaged = np.array([((ts <= o) & (te >= o + 10)).any() for o in on])
        d["cs_on"], d["cs_type"], d["cs_imaged"] = on, typ, imaged
        pe = f["processing/behavior/port_entries"]
        d["port_on"] = pe["start_time"][:]
    if pose and "processing/behavior/PoseEstimationTrack0" in f:
        d["pose_t"], d["pose"] = load_pose(f)
    return d


def ca_cue_z(F, t, onsets, pre=10.0, post=10.0):
    """Calcium cue response per ROI: trial-averaged fluorescence z-scored by the 10 s baseline.

    Paper (STAR Methods, Statistical analysis of calcium recordings): mean fluorescence over trials
    of a CS type, z-scored by the mean and SD of the 10 s before cue onset. Traces are put on a
    grid with the file's median frame interval by nearest frame (standard choice). Imaged clips
    start about 9.6 s before the cue, so the first baseline bins hold no frame; the baseline mean
    and SD are taken over the bins that do. Returns ROIs x bins and the grid.
    """
    dt = float(np.median(np.diff(t)))
    grid = np.arange(-pre, post, dt) + dt / 2
    stack = []
    for o in onsets:
        i = np.searchsorted(t, o + grid)
        i = np.clip(i, 1, len(t) - 1)
        i = np.where(np.abs(t[i - 1] - (o + grid)) < np.abs(t[i] - (o + grid)), i - 1, i)
        ok = np.abs(t[i] - (o + grid)) < dt
        tr = F[i].astype(float)
        tr[~ok] = np.nan
        stack.append(tr)
    with np.errstate(invalid="ignore"), warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        m = np.nanmean(np.stack(stack), axis=0).T  # ROIs x bins
        base = m[:, grid < 0]
        mu = np.nanmean(base, axis=1, keepdims=True)
        sd = np.nanstd(base, axis=1, ddof=1, keepdims=True)
        z = (m - mu) / sd
    return z, grid


SHORT = (0.0, 1.0)  # paper: short window 0-1 s
LONG = (1.0, 10.0)  # paper: long window 1-10 s
