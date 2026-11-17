"""Loading and measures for Gabriel et al. (2025), dandiset 001887 and its Zenodo record.

Dandiset 001887 holds, per mouse and day, the trial table (tone and shock times from the
experiment's MATLAB timestamp file), the behaviour video as an external file and, for two
sessions only (F1 and F2, day 1), the BehaviorDEPOT arrays. It holds no calcium imaging. The
paper's "Analyzed datasets" (Zenodo doi:10.5281/zenodo.13381210, named in the paper's STAR
Methods, "Data and Software Availability") hold for every imaged session the Minian traces
(`*_minian_processed.mat`), the BehaviorDEPOT output (`Behavior.mat`), the trial results
(`pma_results.mat`) and the camera and miniscope timestamps. Both are streamed: the dandiset
with remfile and h5py, the Zenodo zip files by HTTP range requests on the members needed.

Where each parameter comes from:
- Behaviour trial measures: the paper's code, batch_PMA_postanalysis_script_BDv15.m
  (Zenodo doi:10.5281/zenodo.13351302), as the claims file's opening comment gives them. The
  code's frame rate of 25 frames/s is used in the `paper` tone reading; see `tone_windows`.
- Tone windows: two readings (author, step 1.6, and data check). `paper`, the
  BehaviorDEPOT tone bouts (Behavior.Temporal.Tone.Bouts) taken as camera frames, which is
  what the paper's code does. `clock`, the same bout onsets read as seconds at the 25 frames/s
  the cue conversion used (calcCueFramesCG.m converts seconds to frames with a given fps),
  placed on the camera clock through timeStamps.csv. The data check shows the camera ran at
  about 30 frames/s, so the `paper` windows drift from the true tones.
- Calcium frame times: the miniscope timestamps (timeStamps_V4.csv), every second frame, as
  Minian downsampled by 2 in time (STAR Methods, Miniscope data processing). Behaviour labels
  are carried to calcium frames by nearest camera timestamp; the paper's alignment code
  (caAnalyze) is not public, so this is an assumption, the standard use of the Miniscope DAQ
  timestamps, which share one clock.
- ROC: STAR Methods, ROC analysis (auROC of DeltaF/F against a binary event vector, 1000
  circular shuffles, excited above 97.5%, suppressed below 2.5%; tone onset and offset the
  first and last 5 s of the tone; platform entries and exits from 1 s before to 4 s after).
  Feature list and category rule: genFeatCellResponses.m (claims file, opening comment).
- Mean activity around events: compile_pooled_avg_heatmaps.m and trialAvg.m, as the claim
  fig1p-platform-exit-excited-day2 gives them.
- Rescorla-Wagner model: "RW_q-weighted model_Feb 2024.py" (claims file, opening comment),
  update U1; the STAR Methods' formula (R_t, the outcome of the same trial) is the variant U2.
- Decoding bins: 3 calcium frames, with bin times at the code's 15 frames/s; the frames run
  at 14.9 frames/s, so a bin's time is off by about 0.2 s at 28 s and 0.4 s at 50 s, a
  standard choice that moves epoch edges by one or two bins.
- Random seeds: a standard choice. The seed of the ROC shuffles moves cells near the 2.5% and
  97.5% bounds; the notebook shows its effect where a result is near p = 0.05.
"""

import io
import json
import struct
import time
import zlib
import zipfile
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
import scipy.io as sio

DANDISET = "001887"
VERSION = "0.260902.1724"
ZENODO_RECORD = "13381210"
ZENODO_URL = "https://zenodo.org/api/records/13381210/files/{}/content"
API = "https://api.dandiarchive.org/api"

CA_FPS = 15.0      # Minian output, 30 Hz downsampled by 2 (STAR Methods)
CODE_FPS = 25      # fps in batch_PMA_postanalysis_script_BDv15.m and in On Plat.mat (vid_fps)
TONE_S = 30.0      # 30 s tones (STAR Methods, Platform-mediated avoidance)


# ---------------------------------------------------------------- dandiset

def dandi_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        out += d["results"]
        url = d["next"]
    return out


def dandi_metadata():
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60)
    r.raise_for_status()
    return r.json()


def open_nwb(asset_id):
    url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True,
                        timeout=60).url
    return h5py.File(remfile.File(url), "r")


def read_nwb_session(asset):
    """Trial table, shock intervals and the list of series of one dandiset NWB file."""
    f = open_nwb(asset["asset_id"])
    rec = {"path": asset["path"], "size": asset["size"],
           "subject": f["general/subject/subject_id"][()].decode(),
           "sex": f["general/subject/sex"][()].decode(),
           "session": f["general/session_id"][()].decode(),
           "notes": json.loads(f["general/notes"][()].decode()),
           "start_time": f["session_start_time"][()].decode()}
    rec["has_video"] = "behavior_video" in f["acquisition"]
    rec["video_frames"] = (int(f["acquisition/behavior_video/num_samples"][()])
                           if rec["has_video"] else None)
    rec["processing"] = {}
    if "behavior_from_matlab" in f["processing"]:
        g = f["processing/behavior_from_matlab"]
        rec["processing"] = {k: g[k]["data"].shape for k in g}
    tr = f["intervals/trials"] if "intervals/trials" in f else None
    if tr is not None:
        rec["trials"] = {k: tr[k][:] for k in tr if k != "id"}
        rec["trials"]["stimulus_type"] = [x.decode() for x in rec["trials"]["stimulus_type"]]
    else:
        rec["trials"] = None
    rec["shocks"] = (np.c_[f["intervals/shock_intervals/start_time"][:],
                           f["intervals/shock_intervals/stop_time"][:]]
                     if "intervals/shock_intervals" in f else None)
    rec["imaging"] = any(k in f["processing"] for k in ("ophys",)) or any(
        "TwoPhoton" in k or "OnePhoton" in k for k in f["acquisition"])
    if rec["processing"]:
        g = f["processing/behavior_from_matlab"]
        rec["beh"] = {k: g[k]["data"][:] for k in
                      ("Behavior_Platform_Vector", "Behavior_Freezing_Vector",
                       "Behavior_Temporal_Tone_Bouts")}
    return rec


# ---------------------------------------------------------------- Zenodo

_zips = {}


class _Seekable(remfile.File):
    def seekable(self):
        return True


def _zip(day):
    if day not in _zips:
        url = requests.head(ZENODO_URL.format(f"Day%20{day}.zip"), allow_redirects=True,
                            timeout=60).url
        z = zipfile.ZipFile(_Seekable(url))
        _zips[day] = (url, {i.filename: i for i in z.infolist()})
    return _zips[day]


def zenodo_listing(day):
    return _zip(day)[1]


def _range(url, a, b):
    status = None
    for k in range(8):
        try:
            r = requests.get(url, headers={"Range": f"bytes={a}-{b}"}, timeout=180)
            status = r.status_code
            r.raise_for_status()
            if len(r.content) == b - a + 1:
                return r.content
        except requests.RequestException:
            pass
        time.sleep(min(60, 2 ** k))      # Zenodo rate limits bursts of requests
    raise IOError(f"range {a}-{b} of {url} failed, last status {status}")


def read_member(day, name, chunk=24_000_000, workers=16):
    """One file of the Zenodo zip, fetched in parallel ranges and checked against its CRC."""
    url, info = _zip(day)
    i = info[name]
    h = _range(url, i.header_offset, i.header_offset + 29)
    n, e = struct.unpack("<HH", h[26:30])
    s = i.header_offset + 30 + n + e
    end = s + i.compress_size
    ranges = [(a, min(a + chunk, end) - 1) for a in range(s, end, chunk)]
    with ThreadPoolExecutor(workers) as ex:
        raw = b"".join(ex.map(lambda r: _range(url, *r), ranges))
    out = raw if i.compress_type == 0 else zlib.decompress(raw, -15)
    if zlib.crc32(out) != i.CRC:
        raise IOError(f"CRC mismatch for {name}")
    return out


def load_parallel(fn, sessions, n=4):
    """fn(day, folder) for each (day, group, mouse, folder), n sessions at a time. Zenodo
    serves each connection at under 1 MB/s and allows 133 requests a minute, so many
    connections with large ranges are used."""
    with ThreadPoolExecutor(n) as ex:
        return dict(zip(sessions, ex.map(lambda s: fn(s[0], s[3]), sessions)))


def loadmat(b, **kw):
    return sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False, **kw)


def zenodo_sessions():
    """(day, group, mouse, folder) for every session folder of the Zenodo record."""
    out = []
    for day in (1, 2):
        for name in zenodo_listing(day):
            p = name.rstrip("/").split("/")
            if name.endswith("/") and len(p) == 3:
                out.append((day, p[1], p[2].split("_")[0], name))
    return sorted(out)


def _find(day, folder, pred):
    hits = [n for n in zenodo_listing(day) if n.startswith(folder) and pred(n[len(folder):])]
    if len(hits) != 1:
        raise KeyError(f"{folder}: {hits}")
    return hits[0]


def _is_cam_ts(s):
    # camera timestamps are named timeStamps.csv, webcam_timeStamps.csv or
    # timeStamps_behavCAM.csv; the miniscope's carry "V4"
    s = s.lower()
    return s.endswith(".csv") and "timestamps" in s and "v4" not in s and "/" not in s


def _is_v4_ts(s):
    s = s.lower()
    return s.endswith(".csv") and "timestamps" in s and "v4" in s and "/" not in s


def load_behaviour(day, folder):
    """BehaviorDEPOT labels, the camera timestamps and the trial results of one session."""
    B = loadmat(read_member(day, _find(day, folder, lambda s: s == "Behavior.mat")))["Behavior"]
    tone = B.Temporal.Tone if hasattr(B.Temporal, "Tone") else B.Temporal
    pm = loadmat(read_member(day, _find(day, folder, lambda s: s == "pma_results.mat")))
    ts = np.loadtxt(io.BytesIO(read_member(day, _find(day, folder, _is_cam_ts))),
                    delimiter=",", skiprows=1)
    return {"platform": np.asarray(B.Platform.Vector, bool),
            "freezing": np.asarray(B.Freezing.Vector, bool),
            "tone_bouts": np.atleast_2d(np.asarray(tone.Bouts, float)),
            "cam_t": ts[:, 1] / 1000.0,
            "pma": {k: np.atleast_1d(v) for k, v in pm.items() if not k.startswith("__")},
            "fields": struct_fields(B)}


def struct_fields(x, prefix="", depth=3):
    """The field names of a MATLAB struct and of its sub-structs, as dotted paths."""
    out = []
    for k in getattr(x, "_fieldnames", []) or []:
        v = getattr(x, k)
        out.append(prefix + k)
        if depth > 1 and hasattr(v, "_fieldnames"):
            out += struct_fields(v, prefix + k + ".", depth - 1)
    return out


def load_calcium(day, folder):
    """ta_dff (the traces the paper's code uses, genFeatCellResponses.m), frame times, and the
    names and shapes of every variable in the minian file."""
    raw = read_member(day, _find(day, folder, lambda s: s.endswith("minian_processed.mat")))
    names = [(n, shape) for n, shape, _ in sio.whosmat(io.BytesIO(raw))]
    m = loadmat(raw, variable_names=["ta_dff"])
    del raw
    dff = np.asarray(m["ta_dff"], np.float32)
    v4 = np.loadtxt(io.BytesIO(read_member(day, _find(day, folder, _is_v4_ts))),
                    delimiter=",", skiprows=1)
    return {"dff": np.atleast_2d(dff), "v4_t": v4[:, 1] / 1000.0, "variables": names}


# ---------------------------------------------------------------- tones and trials

def tone_windows(beh, reading):
    """Tone onset and offset, in seconds on the camera clock, one row per tone of the session
    (a tone BehaviorDEPOT left out, NaN in its bouts, stays as a NaN row so that tones keep
    their numbers).

    `paper`: the BehaviorDEPOT tone bouts as camera frames (the paper's code).
    `clock`: the bout onsets divided by the 25 frames/s the cue conversion used, which gives
    seconds from the start of the video, with 30 s tones.
    """
    b = beh["tone_bouts"]
    ok = ~np.isnan(b[:, 0])
    t = beh["cam_t"]
    out = np.full((len(b), 2), np.nan)
    if reading == "paper":
        i0 = np.clip(b[ok, 0].astype(int) - 1, 0, len(t) - 1)
        i1 = np.clip(b[ok, 1].astype(int) - 1, 0, len(t) - 1)
        out[ok] = np.c_[t[i0], t[i1]]
    elif reading == "clock":
        on = b[ok, 0] / CODE_FPS + t[0]
        out[ok] = np.c_[on, on + TONE_S]
    else:
        raise ValueError(reading)
    return out


def bouts(v):
    """Start and stop indices (inclusive) of runs of True."""
    d = np.diff(np.r_[0, v.astype(np.int8), 0])
    return np.c_[np.flatnonzero(d == 1), np.flatnonzero(d == -1) - 1]


def trial_measures_code(beh):
    """batch_PMA_postanalysis_script_BDv15.m on the paper's tone bouts, frames at 25 fps."""
    fps = CODE_FPS
    b = beh["tone_bouts"]
    plat, frz = beh["platform"], beh["freezing"]
    pb = bouts(plat)
    out = {k: [] for k in ("platform", "freezing", "latency", "avoid")}
    for s, e in b:
        if np.isnan(s):
            for k in out:
                out[k].append(np.nan)
            continue
        s, e = int(s) - 1, int(e) - 1                     # MATLAB to 0-based
        idx = np.arange(s, e + 1)
        out["platform"].append(plat[idx].mean())
        out["freezing"].append(frz[idx].mean())
        ent = pb[(pb[:, 0] > s) & (pb[:, 0] <= e), 0]
        out["latency"].append((ent[0] - s) / fps if len(ent) else (0.0 if plat[s] else 30.0))
        sh0 = e - 2 * fps                                 # shock bouts, last 2 s of the tone
        out["avoid"].append(float(plat[sh0:e - fps + 1].sum() >= 0.75 * fps))
    return {k: np.array(v) for k, v in out.items()}


def trial_measures_clock(beh):
    """The same measures on the `clock` tone windows, in seconds on the camera clock."""
    t = beh["cam_t"]
    plat, frz = beh["platform"], beh["freezing"]
    n = min(len(t), len(plat))
    t, plat, frz = t[:n], plat[:n], frz[:n]
    pb = bouts(plat)
    out = {k: [] for k in ("platform", "freezing", "latency", "avoid")}
    for on, off in tone_windows(beh, "clock"):
        if np.isnan(on):
            for k in out:
                out[k].append(np.nan)
            continue
        m = (t >= on) & (t < off)
        out["platform"].append(plat[m].mean())
        out["freezing"].append(frz[m].mean())
        ent_t = t[pb[:, 0]]
        ent = ent_t[(ent_t > on) & (ent_t < off)]
        i_on = min(np.searchsorted(t, on), n - 1)
        out["latency"].append(ent[0] - on if len(ent) else (0.0 if plat[i_on] else 30.0))
        sh = (t >= off - 2.0) & (t < off - 1.0)           # first second of the 2 s shock
        out["avoid"].append(float(plat[sh].mean() >= 0.75))
    return {k: np.array(v) for k, v in out.items()}


def epoch_fraction(beh, reading, t0, t1, which):
    """Per trial, the fraction of frames from t0 to t1 s after tone onset with the label."""
    t = beh["cam_t"]
    v = beh[which][:len(t)]
    t = t[:len(v)]
    return np.array([v[(t >= on + t0) & (t < on + t1)].mean() if on == on else np.nan
                     for on, _ in tone_windows(beh, reading)])


# ---------------------------------------------------------------- calcium and features

def read_nwb_all(assets, workers=8):
    """read_nwb_session for every NWB asset, keyed by (subject, session)."""
    nwbs = [a for a in assets if a["path"].endswith(".nwb")]
    with ThreadPoolExecutor(workers) as ex:
        recs = list(ex.map(read_nwb_session, nwbs))
    return {(r["subject"], r["session"]): r for r in recs}


def nwb_key(session):
    day, group, mouse, _ = session
    return (mouse, f"TD{day}{'Shock' if group == 'Shock' else 'NoShock'}")


def trial_table(sessions, beh, reading):
    """Per trial: fraction of the tone on the platform and freezing, latency, and success.

    Success is the hand-scored outcome (pma_results `avoids`) when the session has one, else
    the code's rule (batch_PMA_postanalysis_script_BDv15.m uses a hand-scored outcome file
    when one exists); `success_rule` is the rule alone.
    """
    import pandas as pd
    rows = []
    for s in sessions:
        b = beh[s]
        m = trial_measures_code(b) if reading == "paper" else trial_measures_clock(b)
        ok = ~np.isnan(m["avoid"])
        succ = m["avoid"].copy()
        man = b["pma"].get("avoids")
        if man is not None:
            if len(man) != ok.sum():
                raise ValueError(f"{s}: {len(man)} hand-scored outcomes for {ok.sum()} tones")
            succ[ok] = man
        for i in range(len(succ)):
            rows.append(dict(day=s[0], group=s[1], mouse=s[2], trial=i + 1, block=i // 3 + 1,
                             platform=m["platform"][i], freezing=m["freezing"][i],
                             latency=m["latency"][i], success=succ[i],
                             success_rule=m["avoid"][i], hand_scored=man is not None))
    return pd.DataFrame(rows)


def ca_times(ca):
    """Time of each calcium frame: every second miniscope timestamp (2x temporal downsampling)."""
    n = ca["dff"].shape[1]
    t = ca["v4_t"][::2]
    if len(t) < n:
        raise ValueError("fewer timestamps than calcium frames")
    return t[:n]


def to_ca(beh, ca_t, which):
    """A behaviour label carried to calcium frames by nearest camera timestamp."""
    t = beh["cam_t"]
    v = beh[which][:len(t)]
    t = t[:len(v)]
    i = np.clip(np.searchsorted(t, ca_t), 1, len(t) - 1)
    i = np.where(np.abs(t[i - 1] - ca_t) < np.abs(t[i] - ca_t), i - 1, i)
    return v[i]


def window_vector(ca_t, times, a, b):
    """Binary vector of calcium frames from `a` to `b` seconds around each event time."""
    v = np.zeros(len(ca_t), bool)
    for x in times:
        v |= (ca_t >= x + a) & (ca_t < x + b)
    return v


def features(beh, ca_t, reading):
    """The seven feature vectors of genFeatCellResponses.m on calcium frames (STAR Methods
    windows), plus the tone and ITI splits of platform entries and exits (Figure 2) and the
    exits split by a shock within 2 s (STAR Methods, ROC analysis)."""
    tw_all = tone_windows(beh, reading)
    tw = tw_all[~np.isnan(tw_all[:, 0])]
    plat = to_ca(beh, ca_t, "platform")
    frz = to_ca(beh, ca_t, "freezing")
    pb = bouts(plat)
    ent, ext = ca_t[pb[:, 0]], ca_t[pb[:, 1]]
    tone_ent = np.array([x for x in ent if any((x >= on) & (x < off) for on, off in tw)])
    tone_ext = np.array([x for x in ext if any((x >= on) & (x < off) for on, off in tw)])
    iti_ent = np.array([x for x in ent if not any((x >= on) & (x < off) for on, off in tw)])
    iti_ext = np.array([x for x in ext if not any((x >= on) & (x < off) for on, off in tw)])
    shocks = tw[:, 1] - 2.0
    shk_ext = np.array([x for x in ext if any((s >= x) & (s < x + 2.0) for s in shocks)])
    noshk_ext = np.array([x for x in ext if not any((s >= x) & (s < x + 2.0) for s in shocks)])
    F = {"tonesVector": window_vector(ca_t, tw[:, 0], 0, TONE_S),
         "toneonVector": window_vector(ca_t, tw[:, 0], 0, 5),
         "toneoffVector": window_vector(ca_t, tw[:, 0], TONE_S - 5, TONE_S),
         "platformVector": plat,
         "platentVector": window_vector(ca_t, ent, -1, 4),
         "platextVector": window_vector(ca_t, ext, -1, 4),
         "freezingVector": frz,
         "tonePlatentVector": window_vector(ca_t, tone_ent, -1, 4),
         "itiPlatentVector": window_vector(ca_t, iti_ent, -1, 4),
         "tonePlatextVector": window_vector(ca_t, tone_ext, -1, 4),
         "itiPlatextVector": window_vector(ca_t, iti_ext, -1, 4)}
    events = {"tone_on": tw[:, 0], "tone_off": tw[:, 1], "plat_ent": ent, "plat_ext": ext,
              "frz_on": ca_t[bouts(frz)[:, 0]], "frz_off": ca_t[bouts(frz)[:, 1]],
              "plat_ext_noshock": noshk_ext, "plat_ext_shock": shk_ext}
    return F, events, tw_all


CORE = ["tonesVector", "toneonVector", "toneoffVector", "platformVector", "platentVector",
        "platextVector", "freezingVector"]


def period_mask(ca_t, tw, tones, frames):
    """Calcium frames of a period of tones (1-based) under frame reading F1 or F2."""
    first, last = tones[0] - 1, tones[-1] - 1
    if frames == "F1":
        a = tw[first, 0]
        b = tw[last + 1, 0] if last + 1 < len(tw) else np.inf
    elif frames == "F2":
        a = tw[first - 1, 1] if first > 0 else -np.inf
        b = tw[last, 1]
    else:
        raise ValueError(frames)
    return (ca_t >= a) & (ca_t < b)


def _ranks(x):
    """Average ranks along the last axis (ties share their mean rank)."""
    from scipy.stats import rankdata
    return rankdata(x, axis=-1)


def roc_prepare(dff):
    """The FFT along time of each cell's ranks, which roc_calls correlates with the vector."""
    return np.fft.rfft(_ranks(dff), axis=1)


def roc_calls(dff, vec, rng, n_shuffle=1000, ranks=None):
    """auROC of each cell's trace for a binary vector, and its call against circular shuffles.

    Returns (auc, call) with call +1 excited (above 97.5% of the null), -1 suppressed (below
    2.5%), 0 otherwise; NaN auc and call 0 when the vector has no positive or no negative frame.
    The auROC is the Mann-Whitney statistic; for all circular shifts at once it is computed
    from the circular cross-correlation of the ranks with the vector (FFT). `ranks`, the
    output of roc_prepare(dff), may be passed when several vectors are tested on one trace;
    it gives the same result.
    """
    n = dff.shape[1]
    n1 = int(vec.sum())
    n0 = n - n1
    if n1 == 0 or n0 == 0:
        return np.full(len(dff), np.nan), np.zeros(len(dff), int)
    fr = roc_prepare(dff) if ranks is None else ranks
    shifts = rng.integers(1, n, n_shuffle)
    # S[c, s] = sum_t R[c, t] * vec[(t - s) mod n]
    fv = np.fft.rfft(vec.astype(float))
    S = np.fft.irfft(fr * np.conj(fv), n=n, axis=1)  # circular cross-correlation
    # S[:, s] for s = 0 is the true statistic; numerical rounding is removed by rounding.
    S = np.round(S * 2) / 2
    auc_all = (S - n1 * (n1 + 1) / 2) / (n1 * n0)
    auc = auc_all[:, 0]
    null = auc_all[:, shifts]
    hi = np.percentile(null, 97.5, axis=1)
    lo = np.percentile(null, 2.5, axis=1)
    call = np.where(auc > hi, 1, np.where(auc < lo, -1, 0))
    return auc, call


def categories(calls):
    """Tone, platform and freezing calls from the seven core calls (genFeatCellResponses.m):
    a category's calls are summed and the sign kept, so opposite calls cancel."""
    t = np.sign(calls[:, 0:3].sum(1))
    p = np.sign(calls[:, 3:6].sum(1))
    f = calls[:, 6]
    return np.c_[t, p, f]


def event_area(dff, ca_t, times, half_s, fps=CA_FPS):
    """compile_pooled_avg_heatmaps.m and trialAvg.m: per cell, DeltaF/F averaged over the
    events in a window of `half_s` s on each side (events whose window leaves the recording
    are dropped), z-scored by the mean and SD of the pre-event half, and the trapezoid area of
    the post-event half at 15 frames/s. Returns (area per cell, number of events used)."""
    h = int(round(half_s * fps))
    idx = [int(np.searchsorted(ca_t, x)) for x in times]
    idx = [i for i in idx if i - h >= 0 and i + h < dff.shape[1]]
    if not idx:
        return np.full(len(dff), np.nan), 0
    seg = np.mean([dff[:, i - h:i + h + 1] for i in idx], axis=0)
    pre, post = seg[:, :h], seg[:, h:]
    sd = pre.std(axis=1, ddof=1)
    z = (post - pre.mean(1, keepdims=True)) / np.where(sd > 0, sd, np.nan)[:, None]
    return np.trapezoid(z, dx=1 / fps, axis=1), len(idx)


# ---------------------------------------------------------------- Rescorla-Wagner

def rw_predict(alpha, q, data, success, v0, form="U1"):
    """Predicted platform value per trial. U1, the claims file's update (from the deposited
    script): v(t+1) = v(t) + rate * (R(t+1) - v(t)), so the prediction for trial t+1 uses
    that trial's own outcome. U2, the STAR Methods' formula (Rescorla-Wagner modeling,
    "Delta v_t = alpha * (R_t - v_t)", R_t the outcome at trial t): v(t+1) = v(t) + rate *
    (R(t) - v(t)), which predicts each trial from the earlier ones only. The rate is alpha*q
    after a success and alpha*(1-q) after a failure in both."""
    v = np.full(len(data), v0, float)
    for t in range(len(data) - 1):
        delta = (data[t + 1] if form == "U1" else data[t]) - v[t]
        if success[t] == 1:
            v[t + 1] = v[t] + alpha * q * delta
        elif success[t] == 0:
            v[t + 1] = v[t] + alpha * (1 - q) * delta
        else:
            v[t + 1] = v[t]
    return v


def rw_fit(data, success, v0, model, form="U1", starts=((1, 1),)):
    """Fit by mean squared error (the code's loss), bounds [0, 1], start [1, 1] (code).
    `hybrid` frees alpha and q; `shock` fixes q = 0 and `avoid` fixes q = 1 (claims file).
    With several `starts` the fit with the lowest loss is kept (a variant: the code uses one)."""
    from scipy.optimize import minimize
    loss = lambda a, q: np.mean((rw_predict(a, q, data, success, v0, form) - data) ** 2)
    best = None
    for st in starts:
        if model == "hybrid":
            r = minimize(lambda p: loss(p[0], p[1]), list(st), bounds=[(0, 1), (0, 1)])
            a, q = r.x
        else:
            q = 0.0 if model == "shock" else 1.0
            r = minimize(lambda p: loss(p[0], q), [st[0]], bounds=[(0, 1)])
            a = r.x[0]
        if best is None or r.fun < best[2]:
            best = (a, q, r.fun)
    a, q, _ = best
    return a, q, rw_predict(a, q, data, success, v0, form)


# ---------------------------------------------------------------- statistics

def sidak(p, m):
    return 1 - (1 - np.asarray(p, float)) ** m


def chi2_yates(a, n_a, b, n_b):
    """Two-sided chi-square with Yates' correction on a 2x2 table (count, total) per group."""
    from scipy.stats import chi2_contingency
    t = np.array([[a, n_a - a], [b, n_b - b]])
    if (t.sum(0) == 0).any():
        return np.nan, np.nan
    c, p, _, _ = chi2_contingency(t, correction=True)
    return c, p


# ---------------------------------------------------------------- decoding (Figure 3)

DEC_PRE, DEC_POST, DEC_BIN = 300, 750, 3   # a_SVM_permousev3ASF.m: 20 s before, 50 s after, 200 ms
GRID = range(-10, 11)                      # C and gamma 2^-10 to 2^10 (code)


def decode_inputs(dff, ca_t, onsets):
    """Per trial, each cell's DeltaF/F from 300 frames before to 750 after the tone onset
    (the onset's calcium frame by nearest timestamp), averaged in bins of 3 frames (code).
    Returns (trials, bins, cells) and the bin start times in s."""
    nb = (DEC_PRE + DEC_POST + 1) // DEC_BIN
    X = []
    for on in onsets:
        i = int(np.argmin(np.abs(ca_t - on)))
        seg = dff[:, i - DEC_PRE:i + DEC_POST + 1]
        X.append(seg[:, :nb * DEC_BIN].reshape(len(dff), nb, DEC_BIN).mean(2).T)
    return np.array(X), -20 + 0.2 * np.arange(nb)


def _svm():
    import ctypes
    from libsvm import svm, svmutil
    return svm, svmutil, ctypes.CDLL(None)


def decode_mouse(X, labels, seed):
    """LIBSVM RBF decoder per bin (a_SVM_permousev3ASF.m): C and gamma chosen by 5-fold
    cross-validated accuracy over the grid on all trials (the first maximum in MATLAB's
    column order, C varying fastest), then leave-one-trial-out predictions with them.
    labels: 1 success, 0 failure. Returns the predictions per bin (bins, trials), with the
    code's coding (2 success, 1 failure). LIBSVM's fold shuffling uses C rand(), seeded per
    bin, a standard choice that cannot change more than the folds."""
    svm, su, libc = _svm()
    y = np.where(np.asarray(labels) == 1, 2.0, 1.0)
    n = len(y)
    preds = np.zeros((X.shape[1], n))
    for b in range(X.shape[1]):
        xs = X[:, b, :].tolist()
        prob = su.svm_problem(y.tolist(), xs)
        best, arg = -1, None
        for g in GRID:                       # MATLAB max(:) over matrix (hc, hg): hc fastest
            for c in GRID:
                libc.srand(seed + b)
                p = su.svm_parameter(f"-s 0 -t 2 -c {2.0 ** c} -g {2.0 ** g} -q")
                target = (svm.c_double * n)()
                svm.libsvm.svm_cross_validation(prob, p, 5, target)
                acc = np.mean(np.array(target[:n]) == y)
                if acc > best:
                    best, arg = acc, (c, g)
        c, g = arg
        for i in range(n):
            keep = [k for k in range(n) if k != i]
            m = su.svm_train(su.svm_problem(y[keep].tolist(), [xs[k] for k in keep]),
                             f"-s 0 -t 2 -c {2.0 ** c} -g {2.0 ** g} -q")
            preds[b, i] = su.svm_predict([y[i]], [xs[i]], m, "-q")[0][0]
    return preds


def f1_scores(preds, labels, positive):
    """F1 per bin, undefined counted as 0 (code). positive: 'success' (C1) or 'failure' (C2)."""
    y = np.where(np.asarray(labels) == 1, 2.0, 1.0)
    pos = 2.0 if positive == "success" else 1.0
    tp = ((preds == pos) & (y == pos)).sum(1)
    fp = ((preds == pos) & (y != pos)).sum(1)
    fn = ((preds != pos) & (y == pos)).sum(1)
    with np.errstate(invalid="ignore", divide="ignore"):
        f1 = 2 * tp / (2 * tp + fp + fn)
    return np.nan_to_num(f1, nan=0.0)


def normalise(f1, how):
    if how == "N1":
        r = f1.max() - f1.min()
        return (f1 - f1.min()) / r if r > 0 else np.zeros_like(f1)
    sd = f1.std()
    return (f1 - f1.mean()) / sd if sd > 0 else np.zeros_like(f1)


def decode_job(args):
    X, labels, seed = args
    return decode_mouse(X, labels, seed)

