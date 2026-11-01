"""Loading and measures for the closed-loop microstimulation gaze data of dandiset 000959.

Fan, Dal Monte, Nair, Fagan & Chang (2024), Neuron 112, 2631-2644,
doi:10.1016/j.neuron.2024.05.004. The claims file is claims/000959/10.1016-j.neuron.2024.05.004.yaml.

Each NWB file holds one 300-s run (a "session" in the paper) of one day: M1's gaze (pixels,
1 kHz), in social runs M2's gaze, pupil size, the stimulation and sham times
(`stimulation_events`), the ROIs of the day (`roi_definitions`), and fixation events as
interval tables (`m1_all`, `m1_eye`, `m1_wholeface`, ..., `m2_*`, `mutual_*`). The
`session_description` names the date, run, subject, stimulated region, triggering ROI (Eyes or
Mouth) and condition (Social, or Dot for the non-social RDM control). Files are read over HTTP
into memory at the pinned version; nothing is written to disk.

Where the parameters come from:

- Trial selection (the claims file's opening comment, from the paper's code): a trial is kept
  when its time lies within the valid run (non-NaN `t`) and more than 5 s before the run's last
  valid sample; the first trial of each run is dropped. Trials are grouped by their own label.
- Post-gaze epoch: fixations whose start lies in [0, 1.5) s after the trial (claims file,
  opening comment; STAR Methods, Fixation density map, "within 1.5 sec after the onset").
- A fixation's position is the mean of its own gaze samples between its start and end indices
  (claims file, opening comment). Indices in the files are 1-based (MATLAB); this module
  checks that `t[start_index - 1]` equals the stored start time.
- Which events enter a distance: the Methods reading (M1-only events, `m1_all`, plus the M1
  side of mutual whole Face events, `mutual_wholeface`) and the code's (M1-only events only);
  claims file, opening comment. Mutual events are only defined within the face, and
  `mutual_wholeface` holds every mutual event (`mutual_eye` and `mutual_face` are subsets of
  it; shown in the notebook).
- Hemifield: the side of the fixation's mean x relative to the centre of `roi_m2_face`; for
  monkey L left is ipsilateral, for monkey T right (claims file, opening comment). The files'
  own `laterality_label` is compared with it in the notebook.
- Pixels to degrees: screen height 27 cm at 50 cm over 768 pixels (claims file, opening
  comment, from the paper's code); rank tests do not depend on it.
- Pupil: 700 ms after the trial in 10-ms bins, trials where M1's gaze stays within the whole
  Face ROI throughout (STAR Methods, Control analyses, "throughout at least 700-msec").
"""

from __future__ import annotations

import io
import re
import warnings
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests

DANDISET_ID = "000959"
DANDISET_VERSION = "0.261020.0242"
API = "https://api.dandiarchive.org/api"

POST_GAZE_S = 1.5
LATENCY_WINDOW_S = 5.0          # STAR Methods, Gaze latency analyses, "within 5 sec"
END_MARGIN_S = 5.0              # trials more than 5 s before the run's last sample
HALF_SAMPLE_S = 0.0005          # "after" the trial: later than the trial's own sample
PUPIL_MS = 700
PUPIL_BIN_MS = 10
DEG_PER_PX = np.degrees(2 * np.arctan(13.5 / 50.0)) / 768.0
IPSI_SIDE = {"L": "left", "T": "right"}   # chamber side (claims file, opening comment)


def list_assets(version: str = DANDISET_VERSION) -> pd.DataFrame:
    """Every asset of the pinned version, with its path, size and id."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000"
    rows = []
    while url:
        r = requests.get(url, timeout=60).json()
        rows += r["results"]
        url = r["next"]
    return pd.DataFrame([{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]}
                         for a in rows])


def _dec(x):
    return x.decode() if isinstance(x, bytes) else x


def _table(f, name):
    it = f["intervals"][name]
    return pd.DataFrame({c: [_dec(v) for v in it[c][:]] for c in it if c != "id"})


def _centre(r):
    return np.array([(r[0] + r[2]) / 2, (r[1] + r[3]) / 2])


def _in_rect(xy, r):
    x1, x2 = sorted(r[[0, 2]])
    y1, y2 = sorted(r[[1, 3]])
    return (xy[..., 0] >= x1) & (xy[..., 0] <= x2) & (xy[..., 1] >= y1) & (xy[..., 1] <= y2)


def read_run(asset_id: str, session: requests.Session | None = None) -> dict:
    """Read one run into small tables: metadata, trials, ROIs, fixation events, pupil."""
    s = session or requests
    for attempt in range(4):
        try:
            content = s.get(f"{API}/assets/{asset_id}/download/", timeout=300).content
            f = h5py.File(io.BytesIO(content), "r")
            break
        except Exception:  # retry network errors
            if attempt == 3:
                raise
    desc = _dec(f["session_description"][()])
    m = re.match(r"data_(\d{8}) run_(\d+) \| subject=(\w) \| region=(\w+) \| roi=(\w+) \| "
                 r"condition=(\w+)", desc)
    date, run, subj, region, roi, cond = m.groups()
    meta = dict(asset_id=asset_id, desc=desc, date=date, run=int(run), subject=subj,
                region=region, roi=roi, cond=cond,
                region_scratch=_dec(f["scratch/stimulated_region"][0]),
                roi_scratch=_dec(f["scratch/stimulation_roi"][0]),
                cond_scratch=_dec(f["scratch/stimulation_condition"][0]),
                identifier=_dec(f["identifier"][()]),
                gaze_unit=_dec(f["acquisition/EyeTracking_m1/spatialseries/data"].attrs["unit"]),
                rate=float(f["acquisition/t/starting_time"].attrs["rate"]))
    t = f["acquisition/t/data"][:]
    valid = np.flatnonzero(~np.isnan(t))
    i0, i1 = valid[0], valid[-1]
    meta.update(n_samples=len(t), t_first=t[i0], t_last=t[i1], n_valid=len(valid),
                dt_median=float(np.median(np.diff(t[i0:i1 + 1]))),
                dt_max=float(np.max(np.diff(t[i0:i1 + 1]))))
    g1 = f["acquisition/EyeTracking_m1/spatialseries/data"][:]
    g2 = (f["acquisition/EyeTracking_m2/spatialseries/data"][:]
          if "EyeTracking_m2" in f["acquisition"] else None)
    p1 = f["acquisition/pupil_m1/data"][:]
    meta.update(gaze_x_range=(np.nanmin(g1[:, 0]), np.nanmax(g1[:, 0])),
                gaze_y_range=(np.nanmin(g1[:, 1]), np.nanmax(g1[:, 1])),
                gaze_nan=float(np.isnan(g1[i0:i1 + 1, 0]).mean()),
                pupil_range=(np.nanmin(p1), np.nanmax(p1)))
    rt = f["acquisition/roi_definitions"]
    rois = {_dec(n): np.array([rt[c][i] for c in ["x1", "y1", "x2", "y2"]])
            for i, n in enumerate(rt["roi_name"][:])}

    # trials
    se = f["acquisition/stimulation_events"]
    tt = se["timestamps"][:]
    lab = np.array([_dec(v) for v in se["data"][:]])
    order = np.argsort(tt, kind="stable")
    tt, lab = tt[order], lab[order]
    trials = pd.DataFrame({"time": tt, "type": lab})
    trials["first"] = np.arange(len(trials)) == 0
    trials["in_run"] = (tt >= t[i0]) & (tt < t[i1] - END_MARGIN_S)
    trials["kept"] = trials.in_run & ~trials["first"]
    tidx = np.clip(np.searchsorted(t[i0:i1 + 1], tt) + i0, 0, len(t) - 1)
    trials["sample"] = tidx
    # pupil and gaze in the whole Face during the 700 ms after each trial
    nb = PUPIL_MS // PUPIL_BIN_MS
    pup = np.full((len(trials), nb), np.nan)
    inface = np.zeros(len(trials), bool)
    for k, i in enumerate(tidx):
        if i + PUPIL_MS <= len(t):
            pup[k] = p1[i:i + PUPIL_MS].reshape(nb, PUPIL_BIN_MS).mean(1)
            if "roi_m1_face" in rois:
                inface[k] = _in_rect(g1[i:i + PUPIL_MS], rois["roi_m1_face"]).all()
    trials["in_face_700"] = inface

    # fixation events: one row per monkey per event (mutual events give one row each)
    ev = []
    idx_check = []
    for name in f["intervals"]:
        tab = _table(f, name)
        if not len(tab):
            continue
        kind, roi_name = name.split("_", 1)
        whos = ["m1", "m2"] if kind == "mutual" else [kind]
        for who in whos:
            s0 = tab[f"{who}_start_index"].to_numpy().astype(int) - 1
            e0 = tab[f"{who}_end_index"].to_numpy().astype(int)
            g = g1 if who == "m1" else g2
            with warnings.catch_warnings():  # an event whose samples are all NaN has no position
                warnings.simplefilter("ignore", RuntimeWarning)
                pos = np.array([np.nanmean(g[a:b], 0) if b > a else [np.nan, np.nan]
                                for a, b in zip(s0, e0)])
            idx_check.append(np.nanmax(np.abs(t[s0] - tab[f"{who}_start_time_sec"].to_numpy())))
            ev.append(pd.DataFrame({
                "table": name, "who": who, "target": roi_name, "mutual": kind == "mutual",
                "start": tab[f"{who}_start_time_sec"].to_numpy(),
                "stop": tab[f"{who}_end_time_sec"].to_numpy(),
                "x": pos[:, 0], "y": pos[:, 1],
                "laterality_label": tab["laterality_label"].to_numpy()}))
    events = pd.concat(ev, ignore_index=True)
    meta["index_time_max_err"] = float(np.max(idx_check))
    f.close()
    return dict(meta=meta, trials=trials, rois=rois, events=events, pupil=pup)


def load_all(assets: pd.DataFrame, workers: int = 16) -> list[dict]:
    """Read every asset in parallel (each file into memory, reduced, then released)."""
    sess = requests.Session()
    adapter = requests.adapters.HTTPAdapter(pool_connections=workers, pool_maxsize=workers)
    sess.mount("https://", adapter)
    with ThreadPoolExecutor(workers) as ex:
        runs = list(ex.map(lambda a: read_run(a, sess), assets.asset_id))
    for r, p in zip(runs, assets.path):
        r["meta"]["path"] = p
    return runs


def tables(runs: list[dict]):
    """Concatenate runs into `meta`, `trials` and `events` tables keyed by `run_id`."""
    meta = pd.DataFrame([r["meta"] for r in runs])
    meta["run_id"] = np.arange(len(meta))
    tr, ev = [], []
    for k, r in enumerate(runs):
        a = r["trials"].copy()
        a["run_id"] = k
        a["row"] = np.arange(len(a))
        tr.append(a)
        b = r["events"].copy()
        b["run_id"] = k
        ev.append(b)
    keys = ["run_id", "date", "subject", "region", "roi", "cond"]
    trials = pd.concat(tr, ignore_index=True).merge(meta[keys], on="run_id")
    events = pd.concat(ev, ignore_index=True).merge(meta[keys], on="run_id")
    return meta, trials, events


def day_rois(runs: list[dict]) -> dict:
    """ROIs of each day, from its social runs (the Dot runs hold M1's ROIs only)."""
    out = {}
    for r in runs:
        if r["meta"]["cond"] == "Social":
            out.setdefault(r["meta"]["date"], r["rois"])
    return out


def add_hemifield(events: pd.DataFrame, droi: dict) -> pd.DataFrame:
    """Hemifield by the event's mean x against the centre of the day's `roi_m2_face`."""
    cx = events.date.map(lambda d: _centre(droi[d]["roi_m2_face"])[0])
    right = events.x > cx
    ipsi = np.where(events.subject == "T", right, ~right)
    events = events.copy()
    events["hemi"] = np.where(events.x.isna(), None, np.where(ipsi, "ipsi", "contra"))
    return events


def window_pairs(trials: pd.DataFrame, events: pd.DataFrame, t0: float, t1: float) -> pd.DataFrame:
    """All (trial, event) pairs of the same run with event start in [trial + t0, trial + t1).

    Returns the event rows with `trial` (the trial's index in `trials`) and `lag` (start minus
    trial time, s)."""
    ev = events.sort_values(["run_id", "start"], kind="stable").reset_index(drop=True)
    er = ev.run_id.to_numpy()
    est = ev.start.to_numpy()
    # events sorted by (run, start): offset the start by run so one searchsorted serves all runs
    span = 1e6
    key = er * span + est
    tk = trials.run_id.to_numpy() * span + trials.time.to_numpy()
    lo = np.searchsorted(key, tk + t0, side="left")
    hi = np.searchsorted(key, tk + t1, side="left")
    n = hi - lo
    ti = np.repeat(np.arange(len(trials)), n)
    ei = np.concatenate([np.arange(a, b) for a, b in zip(lo, hi)]) if n.sum() else np.array([], int)
    out = ev.iloc[ei].reset_index(drop=True)
    out["trial"] = trials.index.to_numpy()[ti]
    out["lag"] = est[ei] - trials.time.to_numpy()[ti]
    return out


def roi_centre(droi: dict, date: str, name: str) -> np.ndarray:
    return _centre(droi[date][name])


def day_means(trial_values: pd.DataFrame, value: str, by=("date",)) -> pd.DataFrame:
    """Mean over trials of each type per day (NaN ignored), as columns `stim` and `sham`."""
    keys = list(by) + ["subject", "region"]
    d = trial_values.groupby(keys + ["type"])[value].mean().unstack("type")
    return d.reset_index()


def in_rect(xy, r):
    return _in_rect(xy, r)


def run_centres(runs: list[dict]) -> pd.DataFrame:
    """Per run, the ROI centres (pixels) the measures use, from the run's own ROIs.

    `eyes` and `mouth` are the partner's Eyes and Mouth in M1's coordinates (`roi_m1_eyes`,
    `roi_m1_mouth`; in Dot runs the RDM stimulus, "same location and size as Eyes ROI", STAR
    Methods); `m2_eyes` is M1's Eyes in M2's coordinates (`roi_m2_eyes`, social runs only);
    `m2face_x` is the x of the centre of the day's `roi_m2_face`, the hemifield reference (taken
    from the day's social runs for Dot runs, which do not hold it)."""
    droi = day_rois(runs)
    rows = []
    for k, r in enumerate(runs):
        ro = r["rois"]
        e, m = _centre(ro["roi_m1_eyes"]), _centre(ro["roi_m1_mouth"])
        e2 = _centre(ro["roi_m2_eyes"]) if "roi_m2_eyes" in ro else (np.nan, np.nan)
        rows.append(dict(run_id=k, eyes_x=e[0], eyes_y=e[1], mouth_x=m[0], mouth_y=m[1],
                         m2_eyes_x=e2[0], m2_eyes_y=e2[1],
                         m2face_x=_centre(droi[r["meta"]["date"]]["roi_m2_face"])[0]))
    return pd.DataFrame(rows)


def prepare(runs: list[dict]):
    """Tables for the analyses: run metadata, every trial, every event with its hemifield
    and the run's ROI centres."""
    meta, trials, events = tables(runs)
    cen = run_centres(runs)
    events = events.merge(cen, on="run_id")
    right = events.x > events.m2face_x
    ipsi = np.where(events.subject == "T", right, ~right)
    events["hemi"] = np.where(events.x.isna(), None, np.where(ipsi, "ipsi", "contra"))
    trials = trials.merge(cen, on="run_id")
    return meta, trials, events


def m1_fixations(events: pd.DataFrame, reading: str = "methods") -> pd.DataFrame:
    """M1's fixations: `methods`, M1-only events and the M1 side of mutual whole Face events;
    `code`, M1-only events (`m1_all`)."""
    sel = events.table == "m1_all"
    if reading == "methods":
        sel |= (events.table == "mutual_wholeface") & (events.who == "m1")
    return events[sel]


def m2_fixations(events: pd.DataFrame, reading: str = "methods") -> pd.DataFrame:
    """M2's fixations, as `m1_fixations` for the partner."""
    sel = events.table == "m2_all"
    if reading == "methods":
        sel |= (events.table == "mutual_wholeface") & (events.who == "m2")
    return events[sel]


def trial_distance(trials, fix, centre=("eyes_x", "eyes_y"), t1=POST_GAZE_S, hemi=None):
    """Per trial, the mean Euclidean distance (pixels) of the fixations starting in [0, t1) s
    after it from the given centre; NaN for a trial with none (STAR Methods, Gaze distance
    analyses: "first averaged across all fixations after each trial")."""
    if hemi is not None:
        fix = fix[fix.hemi == hemi]
    pairs = window_pairs(trials, fix.dropna(subset=["x"]), 0.0, t1)
    cx = pairs[centre[0]].to_numpy()
    cy = pairs[centre[1]].to_numpy()
    pairs["dist"] = np.hypot(pairs.x - cx, pairs.y - cy)
    d = pairs.groupby("trial").dist.mean()
    return trials.index.map(d).astype(float)


def first_latency(trials, ev, t1=LATENCY_WINDOW_S):
    """Per trial, the time from the trial to the start of the first event that starts after it
    (strictly, so an event starting at the trial sample, the triggering fixation, is not a look
    back; claims file, fig3b-ofc-inter-looking-interval, "starts after it") and within t1;
    NaN when there is none."""
    pairs = window_pairs(trials, ev, HALF_SAMPLE_S, t1)
    lat = pairs.groupby("trial").lag.min()
    return trials.index.map(lat).astype(float)


def reciprocation(trials, m1_ev, m2_ev, t1=LATENCY_WINDOW_S, first="m2"):
    """Per trial, the mean over sequences of the latency from the first event of a run of
    consecutive `first` events to the next event of the other monkey, over the whole Face
    events of both monkeys that start in [0, t1) after the trial (S1_Gaze_ITI_Combined.m, as
    the claims file gives it). Mutual events enter both lists. NaN when there is no
    sequence."""
    a = window_pairs(trials, m1_ev, 0.0, t1).assign(w="m1")
    b = window_pairs(trials, m2_ev, 0.0, t1).assign(w="m2")
    allp = pd.concat([a, b], ignore_index=True).sort_values(["trial", "start"], kind="stable")
    out = {}
    for tr, g in allp.groupby("trial", sort=False):
        w = g.w.to_numpy()
        st = g.start.to_numpy()
        lats, run_start = [], None
        for k in range(len(w)):
            if w[k] == first:
                if run_start is None:
                    run_start = st[k]
            elif run_start is not None:
                lats.append(st[k] - run_start)
                run_start = None
        if lats:
            out[tr] = np.mean(lats)
    return trials.index.map(out).astype(float)
