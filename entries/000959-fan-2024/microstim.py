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


def file_layout(asset_id: str) -> dict:
    """Names of the top-level groups of one file and of the groups under `intervals`,
    `processing` (if any), `acquisition` and `scratch`."""
    content = requests.get(f"{API}/assets/{asset_id}/download/", timeout=300).content
    with h5py.File(io.BytesIO(content), "r") as f:
        out = {"/": sorted(f.keys())}
        for g in ["intervals", "processing", "acquisition", "scratch", "analysis"]:
            out[g] = sorted(f[g].keys()) if g in f else None
    return out


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

    # saccades of M1 in social runs (Otero-Millan et al. 2014, as the paper's code calls it)
    sacc = None
    if cond == "Social":
        f0 = int(np.flatnonzero(~np.isnan(t))[0])
        sacc = detect_saccades(g1[f0:, 0] * DEG_PER_PX, g1[f0:, 1] * DEG_PER_PX)
        meta.update({f"sacc_{k}": v for k, v in sacc.attrs.items()})
        if len(sacc):
            sacc["start"] = sacc.start.astype(int) + f0
            sacc["end"] = sacc.end.astype(int) + f0
            sacc["start_time"] = t[sacc.start.to_numpy()]
            sacc["end_time"] = t[sacc.end.to_numpy()]
            for c in ["x0", "y0", "x1", "y1"]:
                sacc[c] = sacc[c].astype(float) / DEG_PER_PX   # back to pixels
            sacc = sacc.dropna(subset=["start_time", "end_time"]).reset_index(drop=True)
    f.close()
    return dict(meta=meta, trials=trials, rois=rois, events=events, pupil=pup, saccades=sacc)


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


# ---------------------------------------------------------------------------------------------
# Saccade detection: a Python port of the unsupervised clustering method of Otero-Millan et al.
# (2014, J Vis 14(2):18), from the authors' MATLAB code at
# github.com/ocular-motor-lab/otero-millan_et_al_microsaccade_detection, commit ce2c10dc
# (+ClusterDetection/SaccadeDetectorCluster.m, SaccadeDetector.m, EyeMovRecording.m), the
# software the paper's key resources table names. Defaults of that code are kept: 5 velocity
# peaks per second of valid data, 20 ms between peaks, saccade limits at 5 deg/s, a 6-point
# Bartlett differentiator, features log peak velocity and log peak acceleration before and
# after the peak, whitened, k-means with 2 to 4 clusters chosen by the mean silhouette
# (squared Euclidean, as MATLAB's default), and clusters with mean displacement above 0.2 deg
# taken as saccades. The call follows the paper's own code (changlabneuro/microstim-ofc-social-
# attention at cc0bf994, script/run_saccade_detection.m and script/detect_microsaccades.m): M1's
# gaze from the first non-NaN time sample, in degrees (bfw.px2deg, the same factor as
# DEG_PER_PX), passed as both eyes, at 1 kHz, with every NaN sample marked as a blink (no
# padding); the detector then crops the first 1 s and last 10 ms of the recording
# (EyeMovRecording.GetTrials).
# Differences from the MATLAB code: scipy's k-means (Lloyd iterations from the same starting
# centres; MATLAB's default also runs batch updates only) in place of MATLAB's kmeans.
# ---------------------------------------------------------------------------------------------

SAC_RATE_OF_PEAKS = 5
SAC_MIN_IPI_MS = 20
SAC_LIMIT_DEG_S = 5.0
SAC_MIN_DISPLACEMENT_DEG = 0.2


def _differentiate(x, rate):
    """EyeMovRecording.Differenciate: causal 6-point Bartlett filter, difference, shifted."""
    w = np.array([0.0, 0.4, 0.8, 0.8, 0.4, 0.0])
    w = w / w.sum()
    xf = np.zeros_like(x)
    for k in range(6):  # filter(w, 1, x), with NaN propagating as in MATLAB
        xf[k:] += w[k] * x[:len(x) - k] if k else w[k] * x
    dxf = np.diff(xf, axis=0) * rate
    v = np.zeros_like(x)
    v[:-3] = dxf[2:]
    return v


def _find_peaks(data, mindist, npeaks):
    """SaccadeDetectorCluster.myfindpeaks: greedy highest local maxima, each the highest point
    within +-mindist samples, other maxima within mindist of an accepted one discarded."""
    with np.errstate(invalid="ignore"):
        d = np.diff(data)
        cand = np.flatnonzero((d[:-1] >= 0) & (d[1:] <= 0)) + 1
    vals = data[cand]
    filled = np.where(np.isnan(data), -np.inf, data)
    from scipy.ndimage import maximum_filter1d
    wmax = maximum_filter1d(filled, size=2 * mindist + 1, mode="nearest")
    order = np.lexsort((cand, -vals))     # highest first, ties by position (MATLAB max)
    removed = np.zeros(len(cand), bool)
    out = []
    for j in order:
        if len(out) >= npeaks:
            break
        if removed[j]:
            continue
        c = cand[j]
        removed[j] = True
        lo, hi = max(0, c - mindist), min(len(data) - 1, c + mindist)
        if not (vals[j] < filled[lo:hi + 1]).any():
            out.append(c)
            a, b = np.searchsorted(cand, [c - mindist, c + mindist + 1])
            removed[a:b] = True
    return np.sort(np.array(out, int))


def _kmeans_silhouette_choice(X, vels, max_k=4):
    """SaccadeDetectorCluster.ClusterPeaks: k-means for 2..max_k clusters from velocity-ranked
    starting centres; clusters renumbered by mean peak velocity (0 = fastest); keep the k whose
    two-group (fastest cluster against the rest) mean silhouette is highest, stopping when it
    no longer grows by 1%."""
    from scipy.cluster.vq import kmeans2
    smax, best = 0.0, None
    rank = np.argsort(vels, kind="stable")
    D = ((X[:, None, :] - X[None, :, :]) ** 2).sum(-1)   # squared Euclidean (MATLAB default)
    for k in range(2, max_k + 1):
        size = len(vels) // k
        starts = np.array([X[rank[i * size:(i + 1) * size]].mean(0) for i in range(k)])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            _, lab = kmeans2(X, starts, minit="matrix", iter=100, missing="warn")
        means = np.array([vels[lab == i].mean() if (lab == i).any() else -np.inf for i in range(k)])
        new = np.empty(k, int)
        new[np.argsort(-means, kind="stable")] = np.arange(k)
        lab = new[lab]
        two = np.minimum(lab, 1)
        a = np.array([D[i, two == two[i]].sum() / max((two == two[i]).sum() - 1, 1) for i in range(len(X))])
        b = np.array([D[i, two != two[i]].mean() if (two != two[i]).any() else 0 for i in range(len(X))])
        s = np.where(np.maximum(a, b) > 0, (b - a) / np.maximum(a, b), 0).mean()
        if smax * 1.01 > s:
            break
        smax, best = s, lab
    return best if best is not None else lab


def detect_saccades(gx, gy, rate=1000.0):
    """Saccades of one recording (positions in degrees). Returns a DataFrame with start and end
    sample indices (0-based, inclusive), amplitude, displacement (deg), peak velocity (deg/s),
    and start and end positions."""
    n = len(gx)
    pos = np.column_stack([gx, gy])
    vxy = _differentiate(pos, rate)
    vel = np.hypot(vxy[:, 0], vxy[:, 1])
    axy = _differentiate(vxy, rate)
    acc = np.hypot(axy[:, 0], axy[:, 1])
    # valid samples: within the cropped recording, not NaN, in stretches longer than 0.1 s
    bad = np.isnan(gx) | np.isnan(gy)
    t0, t1 = int(1.0 * rate), n - 1 - int(0.01 * rate)
    valid = ~bad
    valid[:t0] = False
    valid[t1 + 1:] = False
    edges = np.diff(np.r_[0, valid.astype(int), 0])
    vs, ve = np.flatnonzero(edges == 1), np.flatnonzero(edges == -1)
    for a, b in zip(vs, ve):
        if (b - a) / rate <= 0.1:
            valid[a:b] = False
    npk = int(np.ceil(valid[t0:t1 + 1].sum() / rate * SAC_RATE_OF_PEAKS))
    empty = pd.DataFrame(columns=["start", "end", "amplitude", "displacement", "peak_velocity",
                                  "x0", "y0", "x1", "y1"])
    if npk == 0:
        return empty
    pk = _find_peaks(vel[t0:t1 + 1], int(round(SAC_MIN_IPI_MS * rate / 1000)), npk) + t0
    # saccade limits: last sample under 5 deg/s before the peak, first after it
    below = np.flatnonzero(vel < SAC_LIMIT_DEG_S)   # NaN compares False, as in MATLAB
    starts, ends = np.empty(len(pk), int), np.empty(len(pk), int)
    for i, p in enumerate(pk):
        k = np.searchsorted(below, p) - 1
        if k >= 0 and below[k] >= t0:
            starts[i] = min(below[k] + 1, p - 1)
        else:
            seg = vel[t0:p]
            starts[i] = t0 + int(np.nanargmin(seg)) + 1 if np.isfinite(seg).any() else t0
        k = np.searchsorted(below, p + 1)
        if k < len(below) and below[k] <= t1:
            ends[i] = max(below[k] - 1, p + 1)
        else:
            seg = vel[p + 1:t1 + 1]
            ends[i] = p + int(np.nanargmin(seg)) if np.isfinite(seg).any() else t1
    # merge overlapping saccades (CreateYesNo)
    u = np.zeros(ends.max() + 2)
    u[starts] += 1
    u[ends] -= 1
    u = np.cumsum(u)
    st2 = np.flatnonzero(np.diff(np.r_[0, u]) > 0)
    en2 = np.flatnonzero(np.diff(np.r_[u, 0]) < 0)
    merged_as_union = len(st2) != len(en2)
    if merged_as_union:   # the MATLAB code would stop here; merge overlapping intervals instead
        o = np.argsort(starts, kind="stable")
        st2, en2 = [starts[o[0]]], [ends[o[0]]]
        for a, b in zip(starts[o[1:]], ends[o[1:]]):
            if a <= en2[-1]:
                en2[-1] = max(en2[-1], b)
            else:
                st2.append(a)
                en2.append(b)
        st2, en2 = np.array(st2), np.array(en2)
    starts, ends = st2, en2
    cs = np.r_[0, np.cumsum(~valid)]
    ok = (cs[ends + 1] - cs[starts]) == 0          # FindValidSaccades
    starts, ends = starts[ok], ends[ok]
    if len(starts) < 10:
        return empty
    # properties (GetSaccadeProps) and features (GetFeatures)
    pv = np.empty(len(starts))
    pvi = np.empty(len(starts), int)
    acs = np.empty(len(starts))
    acb = np.empty(len(starts))
    amp = np.empty(len(starts))
    nanmax = lambda x: np.nanmax(x) if np.isfinite(x).any() else np.nan   # MATLAB max skips NaN
    for i, (a, b) in enumerate(zip(starts, ends)):
        seg = vel[a:b + 1]
        j = int(np.nanargmax(seg)) if np.isfinite(seg).any() else 0
        pv[i], pvi[i] = seg[j], j + 1                  # MATLAB 1-based index within the saccade
        acs[i] = nanmax(acc[a:min(a + pvi[i], len(acc) - 1) + 1])
        acb[i] = nanmax(acc[min(a + pvi[i], b):b + 1])
        amp[i] = np.hypot(np.ptp(gx[a:b + 1]), np.ptp(gy[a:b + 1]))
    disp = np.hypot(gx[ends] - gx[starts], gy[ends] - gy[starts])
    keep = np.isfinite(pv) & np.isfinite(acs) & np.isfinite(acb)   # NaN velocity next to a gap
    starts, ends, pv, acs, acb, amp, disp = (v[keep] for v in (starts, ends, pv, acs, acb, amp, disp))
    feats = []
    for f in [pv, acs, acb]:
        with np.errstate(divide="ignore"):
            lf = np.log(f)
        lf[lf == -np.inf] = lf[lf != -np.inf].min()
        feats.append((lf - lf.mean()) / lf.std(ddof=1))
    X = np.column_stack(feats)
    C = np.cov(X, rowvar=False)
    D, V = np.linalg.eigh(C)
    W = (X - X.mean(0)) @ (V * np.sqrt(1.0 / (D + 0.1)))
    X = W[:, D / D[-1] > 0.05]
    lab = _kmeans_silhouette_choice(X, pv)
    is_sac = np.zeros(len(starts), bool)
    for c in range(lab.max()):                          # every cluster but the slowest
        if disp[lab == c].mean() > SAC_MIN_DISPLACEMENT_DEG:
            is_sac[lab == c] = True
    s, e = starts[is_sac], ends[is_sac]
    out = pd.DataFrame({"start": s, "end": e, "amplitude": amp[is_sac], "displacement": disp[is_sac],
                        "peak_velocity": pv[is_sac], "x0": gx[s], "y0": gy[s], "x1": gx[e], "y1": gy[e]})
    out.attrs.update(n_peaks=len(pk), n_candidates=len(pv), n_clusters=int(lab.max() + 1),
                     merged_as_union=merged_as_union)
    return out
