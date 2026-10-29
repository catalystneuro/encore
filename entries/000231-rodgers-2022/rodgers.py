"""Loading and per-session measures for dandiset 000231 (Rodgers 2022, Sci Data 9, 620).

The dandiset is streamed from the DANDI archive at the pinned version below. Each NWB file is read
with h5py over remfile, and reduced as it loads to the summaries the claims need (counts, maxima,
per-trial and per-unit values), so no whole session is kept in memory.

Where parameters come from:

- The 0.005 s frame (200 frames/s), the 133 ms blackout, the 4-frame interpolation limit, the 45 s
  spoil offset, the 3 ms ISI and 5% of mean rate thresholds: the claims file, which cites the paper.
- `GRID_TOL` (1e-6 s) and the 1 ms and 5 ms match tolerances: the claims file's criteria.
- `BLACKOUT_SEARCH` (0.2 s), the window around a trial start in which the blackout gap must begin:
  the criterion of claim sync-gap-and-interpolation.
- 60 s bins and one bin per trial for the firing-rate criterion: the two readings of the criterion
  of unit-quality-isi. A last, partial 60 s bin is left out (a standard choice, said to be one).
- `CONTACT_WINDOW` (5 to 25 ms after a contact onset, against 25 to 5 ms before) and the 1 s shift
  used in the clock check of the neural stream: a standard choice for a check of alignment, not a
  method of the paper; it decides no claim.
"""

from __future__ import annotations

import re
import time
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "000231"
VERSION = "0.220904.1554"   # the version the paper cites (doi:10.48324/dandi.000231/0.220904.1554)
API = "https://api.dandiarchive.org/api"

FRAME = 0.005               # s, 200 frames/s (Methods, Alignment of multiple data streams)
GRID_TOL = 1e-6             # s, claim video-timebase
BLACKOUT_SEARCH = 0.2       # s, claim sync-gap-and-interpolation
WHISKERS = ["C0", "C1", "C2", "C3"]
CONTACT_WINDOW = (0.005, 0.025)  # s, clock check only (standard choice)

TRIAL_COLUMNS = ["start_time", "stop_time", "direct_delivery", "stim_is_random", "optogenetic",
                 "outcome", "choice", "rewarded_side", "servo_position", "stimulus", "ignore_trial",
                 "choice_time", "response_window_open_time", "trial"]


def list_assets() -> list[dict]:
    """All assets of the pinned version, from the DANDI REST API."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        j = r.json()
        out += j["results"]
        url = j["next"]
    return out


def version_metadata() -> dict:
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/info/", timeout=60)
    r.raise_for_status()
    return r.json()


def retry(fn, *args, tries: int = 4, wait: float = 5.0):
    """Call fn, retrying on network errors (the archive and S3 sometimes reset connections)."""
    for k in range(tries):
        try:
            return fn(*args)
        except (OSError, requests.RequestException):
            if k == tries - 1:
                raise
            time.sleep(wait * (k + 1))


def s3_url(asset_id: str) -> str:
    def head():
        r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
        r.raise_for_status()
        return r.headers["Location"]
    return retry(head)


def open_nwb(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def _str(x):
    if isinstance(x, bytes):
        return x.decode()
    if isinstance(x, np.ndarray) and x.dtype == object:
        return [_str(v) for v in x]
    return x


def parse_name(path: str) -> dict:
    """Subject, session and data types from an NWB path sub-<m>/sub-<m>_ses-<s>_<types>.nwb."""
    m = re.match(r"^sub-([^/]+)/sub-([^_]+)_ses-([^_]+)_([^/]+)\.nwb$", path)
    if not m:
        return {"folder": None, "subject": None, "session": None, "types": None}
    return {"folder": m.group(1), "subject": m.group(2), "session": m.group(3), "types": m.group(4)}


def max_true_run(b: np.ndarray) -> int:
    """Length of the longest run of True in a boolean array."""
    if b.size == 0 or not b.any():
        return 0
    d = np.diff(np.concatenate([[0], b.astype(np.int8), [0]]))
    starts, stops = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
    return int((stops - starts).max())


def grid_offset(t: np.ndarray) -> float:
    """Largest distance of any time from the 0.005 s grid."""
    if t.size == 0:
        return float("nan")
    k = np.round(t / FRAME)
    return float(np.abs(t - k * FRAME).max())


def _trials(f) -> pd.DataFrame:
    g = f["intervals/trials"]
    d = {"id": g["id"][:]}
    for c in g.keys():
        if c == "id":
            continue
        v = g[c][:]
        d[c] = _str(v) if v.dtype == object else v
    return pd.DataFrame(d)


def _whisker(f, w: str, trials: pd.DataFrame) -> dict:
    """Processed position, pose and contacts of one whisker, reduced to what the claims need."""
    out = {"whisker": w}
    pp = f"processing/behavior/processed_position_whisker_{w}"
    if pp in f:
        g = f[pp]
        out["processed_series"] = sorted(g.keys())
        lens = {k: g[k]["data"].shape[0] for k in g.keys()}
        out["processed_lengths_equal"] = len(set(lens.values())) == 1
        ends = {k: (float(g[k]["timestamps"][0]), float(g[k]["timestamps"][-1])) for k in g.keys()}
        out["processed_ends_equal"] = len(set(ends.values())) == 1
        out["units"] = {k: _str(g[k]["data"].attrs.get("unit")) for k in g.keys()}
        t = g["angle/timestamps"][:]
        interp = g["interpolated/data"][:].astype(bool)
        bend = g["bend/data"][:]
        out["n_processed"] = int(t.size)
        out["t_first"], out["t_last"] = (float(t[0]), float(t[-1])) if t.size else (np.nan, np.nan)
        out["grid_offset"] = grid_offset(t)
        dt = np.diff(t)
        out["n_steps"] = int(dt.size)
        out["n_steps_frame"] = int((np.abs(dt - FRAME) < GRID_TOL).sum())
        out["n_steps_short"] = int((dt < FRAME - GRID_TOL).sum())
        out["n_gaps"] = int((dt > FRAME + GRID_TOL).sum())
        out["n_interpolated"] = int(interp.sum())
        out["max_interp_run"] = max_true_run(interp)
        bn = np.isnan(bend)
        out["bend_notnan_on_interp"] = int((~bn & interp).sum())
        out["bend_nan_on_noninterp"] = int((bn & ~interp).sum())
        # frames present and not interpolated, on the frame grid
        fr = np.round(t / FRAME).astype(np.int64)
        # blackout gap per trial: longest gap whose last frame before it lies within 0.2 s of start
        gap_idx = np.flatnonzero(dt > FRAME + GRID_TOL)
        gap_begin, gap_missing = t[gap_idx], dt[gap_idx] - FRAME
        out["gap_begin"], out["gap_missing"] = gap_begin, gap_missing
        gaps = np.full(len(trials), np.nan)
        for i, s in enumerate(trials["start_time"].to_numpy()):
            sel = np.abs(gap_begin - s) <= BLACKOUT_SEARCH
            if sel.any():
                gaps[i] = gap_missing[sel].max()
        out["trial_gap"] = gaps
        # labeled frames for contacts: present and not interpolated
        nfr = int(fr.max()) + 2 if fr.size else 1
        labeled = np.zeros(nfr, bool)
        labeled[fr[fr >= 0]] = ~interp[fr >= 0]
        cum = np.concatenate([[0], np.cumsum(labeled)])
    else:
        labeled = cum = None
    # pose
    pr = f"processing/behavior/raw_position_whisker_{w}"
    if pr in f:
        g = f[pr]
        markers = sorted(k for k in g.keys() if k.startswith("marker_"))
        out["pose_markers"] = markers
        out["pose_shapes"] = [tuple(g[m]["data"].shape) for m in markers]
        out["pose_conversion"] = sorted({float(g[m]["data"].attrs["conversion"]) for m in markers})
        out["pose_unit"] = sorted({_str(g[m]["data"].attrs["unit"]) for m in markers})
        tp = g[markers[0]]["timestamps"][:] if markers else np.array([])
        out["n_pose"] = int(tp.size)
        out["pose_grid_offset"] = grid_offset(tp)
        dtp = np.diff(tp)
        out["pose_n_steps"] = int(dtp.size)
        out["pose_n_steps_short"] = int((dtp < FRAME - GRID_TOL).sum())
        out["pose_n_steps_not_frame"] = int((np.abs(dtp - FRAME) >= GRID_TOL).sum())
        out["pose_t_first"] = float(tp[0]) if tp.size else np.nan
        out["pose_t_last"] = float(tp[-1]) if tp.size else np.nan
    # contacts
    pc = f"processing/behavior/contacts_by_whisker_{w}"
    if pc in f:
        g = f[pc]
        out["contact_columns"] = [_str(c) for c in g.attrs["colnames"]]
        st, sp = g["start_time"][:], g["stop_time"][:]
        out["contact_start"] = st
        out["n_contacts"] = int(st.size)
        out["contact_start_after_stop"] = int((st > sp).sum())
        out["contact_grid_offset"] = max(grid_offset(st), grid_offset(sp)) if st.size else np.nan
        if "frame_start" in g:
            fs = g["frame_start"][:]
            out["contact_frame_vs_time"] = float(np.abs(fs * FRAME - st).max()) if st.size else np.nan
        if cum is not None and st.size:
            a = np.round(st / FRAME).astype(np.int64)
            b = np.round(sp / FRAME).astype(np.int64)
            a_c, b_c = np.clip(a, 0, len(labeled) - 1), np.clip(b, 0, len(labeled) - 1)
            nlab = cum[b_c + 1] - cum[a_c]
            full = (b - a + 1)
            out["contact_missing"] = (nlab < full) | (a < 0) | (b >= len(labeled))
    return out


def _ecephys(f, trials: pd.DataFrame) -> dict:
    out = {}
    es = f["acquisition/extracellular array recording"]
    d = es["data"]
    out["n_samples"], out["n_channels"] = d.shape
    out["dtype"] = str(d.dtype)
    out["has_timestamps"] = "timestamps" in es
    if "starting_time" in es:
        out["starting_time"] = float(es["starting_time"][()])
        out["rate"] = float(es["starting_time"].attrs["rate"])
    if out["has_timestamps"]:
        ts = es["timestamps"]
        out["ts_first"], out["ts_last"] = float(ts[0]), float(ts[-1])
    else:
        out["ts_first"] = out["starting_time"]
        out["ts_last"] = out["starting_time"] + (out["n_samples"] - 1) / out["rate"]
    out["conversion"] = float(d.attrs["conversion"])
    out["electrodes_region"] = es["electrodes"][:]
    e = f["general/extracellular_ephys/electrodes"]
    out["el_id"] = e["id"][:]
    out["el_y"] = e["y"][:]
    out["el_location"] = _str(e["location"][:])
    out["el_group_name"] = _str(e["group_name"][:])
    groups = [k for k in f["general/extracellular_ephys"].keys() if k != "electrodes"]
    out["groups"] = {k: _str(f["general/extracellular_ephys"][k].attrs.get("location")) for k in groups}
    u = f["units"]
    out["unit_columns"] = sorted(u.keys())
    out["unit_id"] = u["id"][:]
    out["unit_depth"] = u["depth"][:]
    out["unit_layer"] = _str(u["layer"][:])
    out["unit_channel"] = u["neuron_channel"][:]
    out["unit_inhibitory"] = u["inhibitory"][:]
    oi, oidx = u["obs_intervals"][:], u["obs_intervals_index"][:]
    st, sidx = u["spike_times"][:], u["spike_times_index"][:]
    units = []
    o0 = 0
    s0 = 0
    for k in range(len(out["unit_id"])):
        ints = oi[o0:oidx[k]]
        o0 = oidx[k]
        sp = st[s0:sidx[k]]
        s0 = sidx[k]
        units.append({"intervals": ints, "spikes": sp})
    out["units"] = units
    return out


def summarize_session(asset: dict) -> dict:
    """Open one NWB file and reduce it to the per-session summary used by every claim."""
    s = {"path": asset["path"], "asset_id": asset["asset_id"], "size": asset["size"]}
    s.update(parse_name(asset["path"]))
    with open_nwb(asset["asset_id"]) as f:
        s["top"] = sorted(f.keys())
        s["acquisition"] = sorted(f["acquisition"].keys())
        s["processing"] = {k: sorted(f["processing"][k].keys()) for k in f["processing"].keys()}
        s["experiment_description"] = _str(f["general/experiment_description"][()])
        s["session_description"] = _str(f["session_description"][()])
        s["identifier"] = _str(f["identifier"][()])
        s["session_start_time"] = _str(f["session_start_time"][()])
        s["keywords"] = _str(f["general/keywords"][:]) if "general/keywords" in f else []
        sub = f["general/subject"]
        s["subject_meta"] = {k: _str(sub[k][()]) for k in sub.keys()}
        bv = f["acquisition"].get("behavioral video")
        if bv is not None:
            s["video_external_file"] = _str(bv["external_file"][:])
            s["video_starting_time"] = float(bv["starting_time"][()])
            s["video_rate"] = float(bv["starting_time"].attrs["rate"])
        trials = _trials(f)
        s["trials"] = trials
        ev = {}
        for kind in ("licks", "rewards"):
            p = f"processing/behavior/{kind}"
            ev[kind] = {k: f[p][k]["timestamps"][:] for k in f[p].keys()} if p in f else {}
        s["events"] = ev
        s["whiskers"] = {w: _whisker(f, w, trials) for w in WHISKERS}
        s["ecephys"] = _ecephys(f, trials) if "extracellular array recording" in f["acquisition"] else None
    return s


def summarize_session_retry(asset: dict) -> dict:
    return retry(summarize_session, asset)


def summarize_all(assets: list[dict], workers: int = 8) -> list[dict]:
    """Summaries of every NWB asset, streamed in parallel processes (h5py serializes threads)."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(summarize_session_retry, assets))


def video_header(asset: dict) -> dict:
    """Container and stream metadata of one mkv, read over HTTP without decoding frames."""
    import av
    out = {"path": asset["path"], "size": asset["size"]}
    with av.open(remfile.File(s3_url(asset["asset_id"]))) as c:
        v = c.streams.video[0]
        out["format"] = c.format.name
        out["codec"] = v.codec_context.name
        out["width"], out["height"] = v.codec_context.width, v.codec_context.height
        out["average_rate"] = float(v.average_rate) if v.average_rate else np.nan
        out["base_rate"] = float(v.base_rate) if v.base_rate else np.nan
        out["frames"] = int(v.frames)
        out["container_duration"] = c.duration / 1e6 if c.duration else np.nan
        out["stream_tags"] = dict(v.metadata)
        out["container_tags"] = dict(c.metadata)
    return out


def video_header_retry(asset: dict) -> dict:
    return retry(video_header, asset)


def video_headers(assets: list[dict], workers: int = 8) -> list[dict]:
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(video_header_retry, assets))


def tag_duration(tags: dict) -> float:
    """Seconds from an mkv DURATION tag of the form HH:MM:SS.fffffffff."""
    v = tags.get("DURATION") or tags.get("duration")
    if not v:
        return float("nan")
    h, m, sec = v.split(":")
    return int(h) * 3600 + int(m) * 60 + float(sec)


def openephys_samples(size: int) -> int:
    """Samples in an Open Ephys 0.4 .continuous file from its size: a 1024-byte header, then
    records of 1024 samples, each 2070 bytes (8 timestamp, 2 count, 2 recording number, 2048 data,
    10 marker), as the format defines it."""
    return int((size - 1024) // 2070 * 1024)


def isi_fraction(spikes: np.ndarray, thr: float = 0.003) -> float:
    """Fraction of inter-spike intervals below thr (3 ms, claim unit-quality-isi)."""
    d = np.diff(np.sort(spikes))
    return float((d < thr).mean()) if d.size else float("nan")


def low_rate_fraction_bins(spikes: np.ndarray, start: float, stop: float, width: float = 60.0) -> float:
    """Fraction of full bins of `width` s within [start, stop] whose rate is below 5% of the mean
    rate over [start, stop] (reading (a) of unit-quality-isi; a last partial bin is left out)."""
    n = int((stop - start) // width)
    if n < 1:
        return float("nan")
    mean = spikes.size / (stop - start)
    counts = np.histogram(spikes, bins=start + width * np.arange(n + 1))[0]
    return float((counts / width < 0.05 * mean).mean())


def low_rate_fraction_trials(spikes: np.ndarray, start: float, stop: float, trials: pd.DataFrame) -> float:
    """As above with one bin per trial (start_time to stop_time) wholly inside [start, stop]
    (reading (b) of unit-quality-isi)."""
    t = trials[(trials.start_time >= start) & (trials.stop_time <= stop)]
    if len(t) == 0:
        return float("nan")
    mean = spikes.size / (stop - start)
    sp = np.sort(spikes)
    c = np.searchsorted(sp, t.stop_time.to_numpy()) - np.searchsorted(sp, t.start_time.to_numpy())
    dur = (t.stop_time - t.start_time).to_numpy()
    return float((c / dur < 0.05 * mean).mean())


def task_from_metadata(s: dict) -> str | None:
    """The task the session metadata names (experiment description, then keywords)."""
    text = (s.get("experiment_description") or "").lower() + " " + " ".join(s.get("keywords") or []).lower()
    det, dis = "shape detection" in text, "shape discrimination" in text
    if det and not dis:
        return "detection"
    if dis and not det:
        return "discrimination"
    return None


def assign_trials(times: np.ndarray, trials: pd.DataFrame) -> np.ndarray:
    """Row index of the trial whose [start_time, stop_time) holds each time, or -1."""
    st = trials["start_time"].to_numpy()
    sp = trials["stop_time"].to_numpy()
    i = np.searchsorted(st, times, side="right") - 1
    ok = (i >= 0) & (times < sp[np.clip(i, 0, None)])
    return np.where(ok, i, -1)
