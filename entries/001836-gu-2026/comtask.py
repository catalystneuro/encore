"""Loading and behavioral measures for dandiset 001836 (Gu et al. 2026, spatial sequence task).

Gu, Liu, Gillespie, Nevers, Denovellis, Coulter, Kay & Frank (2026), "Naturalistic behavior and
self-generated neural activity predictive of self-correction", bioRxiv,
doi:10.64898/2026.05.26.727951.

The dandiset holds, per rat and day, a raw file (``*_behavior+ecephys+image.nwb``: 30 kHz voltage,
headstage inertial sensors, raw LED tracking, the well pokes, lights and pumps as digital events,
the Statescript logs and the epochs), a 1 kHz ``*_ecephys.nwb`` LFP file, and Spyglass analysis
files named only by an object id (``obj-*``): head position, velocity and orientation
(``*_behavior.nwb``), linearized position (``scratch/pandas_table``), and decodes triggered on
events (``scratch/triggered``). None of the analysis files says what it is; they are identified here
by their content and matched to epochs by their time range. Files are streamed from the archive at
the pinned version; nothing is written to disk.

Where the parameters come from:

- Trials (Methods, Behavioral analysis, "Trial start and end time marked by the subject poking at
  home well and outer choice wells, along with reward deliveries"): a trial starts at a home reward
  (the home pump turning on after a home poke; Methods, Behavioral training, "each self-paced trial
  is initiated by a nose trigger at the home well and receipt of a reward") and ends at the first
  outer-well poke after it. The trial is rewarded when that well's pump turns on within
  ``REWARD_WINDOW_S`` of the poke (claims file, opening comment, point 4: rewardNum == 2). The
  window is a standard choice: pumps turn on within milliseconds of the poke or not at all.
- Sessions with fewer than ``MIN_TRIALS`` trials are left out where a claim says so (claims file,
  opening comment, point 2, behavior.determine_if_include_session).
- Linearized position: the 500 Hz Spyglass linearization (Methods, Change of mind time detection,
  "We operated on smoothed and upsampled 1D position tracking data"). Each outer arm is one track
  segment; the segment of each well is read from the segment the head is on at that well's pokes.
- COM detection (Methods, Change-of-mind trial detection and Change of mind time detection; claims
  file, fig1e-trial-counts): in a trial, every entry into an outer arm other than the final one
  whose depth exceeds the threshold (``THETA_CM`` = 10 cm, or ``THETA_PROP`` = 0.1 of the arm's
  length, the two readings of the claims file), and in which the head moves in the negative
  direction along the arm for more than ``REVERSAL_MS`` after binary closing, is a COM event,
  provided the second before the reversal holds at least ``MIN_POS_S`` s of position samples
  (claims file, findProportion). The Methods name scipy's ``binary_closing`` without parameters;
  its default structure (three neighbouring samples in one dimension) is used.
- Side transitions: arms 1-2 and 3-4 are on the same side (claims file, point 5).
- Nearby control trial: drawn at random from trials t-3 to t+3 of the same session that are not
  COM trials (Methods, Identification of nearby trials; claims file, point 6).
"""

from __future__ import annotations

import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import ndimage

DANDISET_ID = "001836"
DANDISET_VERSION = "0.261030.0428"
API = "https://api.dandiarchive.org/api"

RATS = {"molly": "M", "eliot": "E", "julio": "J", "klein": "K", "lewis": "L"}
REWARD_WINDOW_S = 2.0
MIN_TRIALS = 20
THETA_CM = 10.0
THETA_PROP = 0.1
REVERSAL_MS = 100.0
MIN_POS_S = 0.8
LIN_RATE_MIN = 100.0       # the 500 Hz linearization, as against the 23 Hz one
SAME_SIDE = {frozenset((1, 2)), frozenset((3, 4))}
WELLS = ["Home", "Arm1", "Arm2", "Arm3", "Arm4"]


def _get(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.load(r)


def list_assets():
    """All assets of the pinned version: path, size, blob id, S3 URL, rat, day."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        page = _get(url)
        for a in page["results"]:
            b = a["blob"]
            path = a["path"]
            rows.append({"path": path, "size": a["size"], "blob": b,
                         "url": f"https://dandiarchive.s3.amazonaws.com/blobs/{b[:3]}/{b[3:6]}/{b}",
                         "rat": path.split("/")[0].replace("sub-", ""),
                         "day": path.split("_ses-")[1].split("_")[0],
                         "kind": ("raw" if path.endswith("behavior+ecephys+image.nwb") else
                                  "lfp" if path.endswith("_ecephys.nwb") else
                                  "obj_behavior" if path.endswith("_behavior.nwb") else "obj")})
        url = page["next"]
    return pd.DataFrame(rows)


def open_nwb(url):
    return h5py.File(remfile.File(url), "r")


def _rising(ts, data):
    data = np.asarray(data)
    ts = np.asarray(ts)
    prev = np.concatenate([[0], data[:-1]])
    return ts[(data > 0) & (prev == 0)]


def load_raw_events(url):
    """Epochs and digital events of a day's raw file (no voltage is read)."""
    f = open_nwb(url)
    ep = f["intervals/epochs"]
    tags = [t.decode() if isinstance(t, bytes) else str(t) for t in ep["tags"][:]]
    epochs = pd.DataFrame({"start": ep["start_time"][:], "stop": ep["stop_time"][:], "tag": tags})
    be = f["processing/behavior/behavioral_events"]
    ev = {}
    for w in WELLS:
        for kind in ("poke", "milk_pump"):
            g = be[f"{w}_{kind}"]
            ev[(w, kind)] = _rising(g["timestamps"][:], g["data"][:])
    scripts = {}
    af = f["processing/associated_files"]
    for k in af:
        scripts[k] = af[k].attrs.get("content", "")
    subj = f["general/subject/subject_id"][()]
    return {"epochs": epochs, "events": ev, "statescript": scripts,
            "subject_id": subj.decode() if isinstance(subj, bytes) else str(subj)}


def probe_obj(url):
    """What an analysis file holds: its kind, sample count, time range and rate."""
    f = open_nwb(url)
    if "scratch/pandas_table" in f:
        t = f["scratch/pandas_table/time"]
        n = t.shape[0]
        a, b = float(t[0]), float(t[-1])
        return {"obj_kind": "linearization", "n": n, "t0": a, "t1": b, "rate": (n - 1) / (b - a)}
    if "scratch/triggered" in f:
        return {"obj_kind": "triggered", "n": f["scratch/triggered/id"].shape[0]}
    if "scratch/Position" in f:
        t = f["scratch/Position/head_position/timestamps"]
        n = t.shape[0]
        a, b = float(t[0]), float(t[-1])
        return {"obj_kind": "position", "n": n, "t0": a, "t1": b, "rate": (n - 1) / (b - a)}
    return {"obj_kind": "other"}


def load_linearization(url):
    g = open_nwb(url)["scratch/pandas_table"]
    return pd.DataFrame({"time": g["time"][:], "lin": g["linear_position"][:],
                         "seg": g["track_segment_id"][:].astype(int)})


def build_trials(ev, start, stop):
    """Trials of one run epoch from the digital events (see module docstring)."""
    home_rew = ev[("Home", "milk_pump")]
    home_rew = home_rew[(home_rew >= start) & (home_rew <= stop)]
    outer = []
    for i in range(1, 5):
        p = ev[(f"Arm{i}", "poke")]
        outer += [(t, i) for t in p[(p >= start) & (p <= stop)]]
    outer.sort()
    ot = np.array([o[0] for o in outer])
    rows = []
    for k, t0 in enumerate(home_rew):
        nxt = home_rew[k + 1] if k + 1 < len(home_rew) else stop
        j = np.searchsorted(ot, t0)
        if j >= len(ot) or ot[j] > nxt:
            continue
        t1, well = outer[j]
        pump = ev[(f"Arm{well}", "milk_pump")]
        rew = bool(np.any((pump >= t1) & (pump <= t1 + REWARD_WINDOW_S)))
        rows.append({"start": t0, "end": t1, "final": well, "rewarded": rew})
    return pd.DataFrame(rows)


def arm_segments(lin, ev, start, stop):
    """Segment id of each outer well, from the head's segment at that well's pokes."""
    out = {}
    for i in range(1, 5):
        p = ev[(f"Arm{i}", "poke")]
        p = p[(p >= start) & (p <= stop)]
        if len(p) == 0:
            continue
        idx = np.clip(np.searchsorted(lin.time.values, p), 0, len(lin) - 1)
        segs = lin.seg.values[idx]
        vals, cnt = np.unique(segs, return_counts=True)
        out[i] = {"seg": int(vals[np.argmax(cnt)]), "frac": cnt.max() / cnt.sum(), "n": len(p)}
    return out


def detect_com(trials, lin, seg_of_arm, arm_start, arm_len, theta="cm"):
    """COM events per trial. Returns trials with com columns and a list of events."""
    t = lin.time.values
    lp = lin.lin.values
    sg = lin.seg.values
    dt = np.median(np.diff(t))
    rev_n = int(round(REVERSAL_MS / 1000 / dt))
    arm_of_seg = {v: k for k, v in seg_of_arm.items()}
    events = []
    n_arm, n_time, first_arm, first_time = [], [], [], []
    for tr in trials.itertuples():
        i0, i1 = np.searchsorted(t, [tr.start, tr.end])
        s = sg[i0:i1]
        d = lp[i0:i1]
        ts = t[i0:i1]
        arms_entered, visits = [], []
        if len(s):
            # contiguous runs of the same segment
            change = np.flatnonzero(np.diff(s) != 0) + 1
            bounds = np.concatenate([[0], change, [len(s)]])
            for a, b in zip(bounds[:-1], bounds[1:]):
                arm = arm_of_seg.get(int(s[a]))
                if arm is None or arm == tr.final:
                    continue
                depth = d[a:b] - arm_start[arm]
                thr = THETA_CM if theta == "cm" else THETA_PROP * arm_len[arm]
                if np.nanmax(depth) <= thr:
                    continue
                neg = np.diff(depth) < 0
                neg = ndimage.binary_closing(neg)
                lab, nlab = ndimage.label(neg)
                if nlab == 0:
                    continue
                sizes = ndimage.sum(neg, lab, range(1, nlab + 1))
                ok = np.flatnonzero(sizes > rev_n)
                if len(ok) == 0:
                    continue
                first = np.flatnonzero(lab == ok[0] + 1)[0]
                t_rev = ts[a + first]
                w = (t >= t_rev - 1) & (t < t_rev)
                if np.sum(np.isfinite(lp[w])) * dt < MIN_POS_S:
                    continue
                visits.append((arm, t_rev, float(np.nanmax(depth))))
                if arm not in arms_entered:
                    arms_entered.append(arm)
        for arm, t_rev, depth in visits:
            events.append({"trial_start": tr.start, "arm": arm, "t_rev": t_rev, "depth": depth})
        n_arm.append(len(arms_entered))
        n_time.append(len(visits))
        first_arm.append(visits[0][0] if visits else np.nan)
    out = trials.copy()
    out["n_com_arm"] = n_arm
    out["n_com_time"] = n_time
    out["n_com"] = np.maximum(n_arm, n_time)
    out["com"] = out.n_com > 0
    out["initial"] = first_arm
    return out, pd.DataFrame(events)


def infer_sequence(trials):
    """The rewarded cycle: for each rewarded arm, the arm most often rewarded next."""
    r = trials[trials.rewarded]
    nxt = {}
    for a, b in zip(r.final.values[:-1], r.final.values[1:]):
        nxt.setdefault(int(a), []).append(int(b))
    cyc = {a: max(set(v), key=v.count) for a, v in nxt.items()}
    support = {a: v.count(cyc[a]) / len(v) for a, v in nxt.items()}
    return cyc, support


def is_switch(a, b):
    return frozenset((int(a), int(b))) not in SAME_SIDE


def nearby_control(trials_sess, rng):
    """For each COM trial, a random non-COM trial among t-3..t+3 of the same session (or -1)."""
    com = trials_sess.com.values
    idx = []
    for i in np.flatnonzero(com):
        cand = [j for j in range(i - 3, i + 4) if 0 <= j < len(com) and j != i and not com[j]]
        idx.append(rng.choice(cand) if cand else -1)
    return np.array(idx, dtype=int)


def parallel(fn, items, workers=16):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(fn, items))


def load_day(assets_day):
    """Trials and COM events of one rat-day, with the checks the notebook prints."""
    raw = assets_day[assets_day.kind == "raw"].iloc[0]
    info = load_raw_events(raw.url)
    objs = assets_day[(assets_day.kind == "obj")]
    probes = parallel(lambda u: probe_obj(u), list(objs.url), workers=8)
    objs = objs.assign(**pd.DataFrame(probes, index=objs.index))
    lins = objs[(objs.obj_kind == "linearization") & (objs.rate > LIN_RATE_MIN)]
    epochs = info["epochs"]
    run = epochs[epochs.tag.str.contains("Session")]
    per_epoch, checks, dups = [], [], []
    loaded = {}
    for e in run.itertuples():
        cand = lins[(lins.t0 >= e.start - 1) & (lins.t1 <= e.stop + 1)]
        if len(cand) == 0:
            checks.append({"epoch": e.tag, "lin_files": 0})
            continue
        lin = load_linearization(cand.iloc[0].url)
        if len(cand) > 1:
            for k in range(1, len(cand)):
                other = load_linearization(cand.iloc[k].url)
                same = (len(other) == len(lin)) and np.allclose(other.lin.values, lin.lin.values, equal_nan=True)
                dups.append({"epoch": e.tag, "file_a": cand.iloc[0].path, "file_b": cand.iloc[k].path, "identical": same})
        loaded[e.tag] = (e, lin)
    # arm geometry over the day
    segmap, starts, lens = {}, {}, {}
    for tag, (e, lin) in loaded.items():
        segmap[tag] = arm_segments(lin, info["events"], e.start, e.stop)
    allseg = {}
    for tag in segmap:
        for arm, v in segmap[tag].items():
            allseg.setdefault(arm, []).append(v["seg"])
    seg_of_arm = {arm: max(set(v), key=v.count) for arm, v in allseg.items()}
    lin_all = pd.concat([lin for _, lin in loaded.values()])
    for arm, s in seg_of_arm.items():
        x = lin_all.lin.values[lin_all.seg.values == s]
        starts[arm], lens[arm] = float(np.nanmin(x)), float(np.nanmax(x) - np.nanmin(x))
    trials_all, events_all, trials_p, events_p = [], [], [], []
    for tag, (e, lin) in loaded.items():
        tr = build_trials(info["events"], e.start, e.stop)
        if len(tr) == 0:
            checks.append({"epoch": tag, "lin_files": 1, "trials": 0})
            continue
        trp, evp = detect_com(tr, lin, seg_of_arm, starts, lens, theta="prop")
        tr, evs = detect_com(tr, lin, seg_of_arm, starts, lens, theta="cm")
        for x in (tr, trp):
            x["epoch"] = tag
            x["trial"] = np.arange(len(x))
        evs["epoch"] = tag
        evp["epoch"] = tag
        trials_p.append(trp)
        events_p.append(evp)
        # clock check: linear position at outer pokes relative to the arm end
        idx = np.clip(np.searchsorted(lin.time.values, tr.end.values), 0, len(lin) - 1)
        on_arm = np.array([lin.seg.values[i] == seg_of_arm.get(w, -9) for i, w in zip(idx, tr.final)])
        shifted = {}
        for sh in (-10.0, 10.0):
            j = np.clip(np.searchsorted(lin.time.values, tr.end.values + sh), 0, len(lin) - 1)
            shifted[sh] = np.mean([lin.seg.values[i] == seg_of_arm.get(w, -9) for i, w in zip(j, tr.final)])
        depth_end = np.array([lin.lin.values[i] - starts.get(w, np.nan) for i, w in zip(idx, tr.final)])
        ss = info["statescript"].get("statescript " + tag.split("_", 1)[1], "")
        checks.append({"epoch": tag, "lin_files": 1, "trials": len(tr),
                       "rewarded": int(tr.rewarded.sum()), **statescript_counts(ss),
                       "end_on_final_arm": float(np.mean(on_arm)),
                       "on_final_arm_10s_before": float(shifted[-10.0]),
                       "on_final_arm_10s_after": float(shifted[10.0]),
                       "median_depth_at_poke": float(np.nanmedian(depth_end)),
                       "lin_nan_frac": float(np.mean(~np.isfinite(lin.lin.values)))})
        trials_all.append(tr)
        events_all.append(evs)
    trials = pd.concat(trials_all, ignore_index=True) if trials_all else pd.DataFrame()
    events = pd.concat(events_all, ignore_index=True) if events_all else pd.DataFrame()
    cat = lambda xs: pd.concat(xs, ignore_index=True) if xs else pd.DataFrame()
    return {"trials": trials, "events": events, "trials_prop": cat(trials_p), "events_prop": cat(events_p),
            "checks": pd.DataFrame(checks), "dups": dups,
            "seg_of_arm": seg_of_arm, "arm_start": starts, "arm_len": lens,
            "segmap": segmap, "epochs": epochs, "subject_id": info["subject_id"],
            "obj_counts": objs.obj_kind.value_counts().to_dict(),
            "n_lin_500": int(len(lins)), "n_lin_23": int(((objs.obj_kind == "linearization") & (objs.rate <= LIN_RATE_MIN)).sum()),
            "statescript_names": list(info["statescript"].keys())}


def statescript_counts(content):
    """Home and outer rewards the Statescript log reports, and its last outerCount."""
    lines = [ln for ln in content.splitlines() if ln and not ln.startswith("#")]
    home = sum(ln.endswith(" home reward") for ln in lines)
    outer = sum(ln.endswith(" outer reward") for ln in lines)
    oc = [int(ln.split("=")[1]) for ln in lines if " outerCount = " in ln]
    gc = [int(ln.split("=")[1]) for ln in lines if " goalCount = " in ln]
    return {"ss_home_rewards": home, "ss_outer_rewards": outer,
            "ss_outerCount": max(oc) if oc else 0, "ss_goalCount": max(gc) if gc else 0}


def load_all(assets, workers=5):
    """load_day for every rat-day; adds rat and day columns and the day index per rat."""
    days = sorted(assets.day.unique())
    res = dict(zip(days, parallel(lambda d: load_day(assets[assets.day == d]), days, workers=workers)))
    for d, r in res.items():
        rat = d.split("-")[0]
        for k in ("trials", "events", "trials_prop", "events_prop", "checks"):
            if len(r[k]):
                r[k]["rat"] = RATS[rat]
                r[k]["day"] = d
    return res
