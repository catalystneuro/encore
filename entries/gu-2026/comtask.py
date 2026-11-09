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
  Leaving the well (``poke_out``, for figs7b-no-swr) is the last beam release at the final well
  before a poke at any other well.
- Sessions with fewer than ``MIN_TRIALS`` trials are left out where a claim says so (claims file,
  opening comment, point 2, behavior.determine_if_include_session).
- Linearized position: the 500 Hz Spyglass linearization (Methods, Change of mind time detection,
  "We operated on smoothed and upsampled 1D position tracking data"). Each outer arm is one track
  segment; the segment of each well is read from the segment the head is on at that well's pokes.
- COM detection (Methods, Change-of-mind trial detection and Change of mind time detection; claims
  file, fig1e-trial-counts): in a trial, every entry into an outer arm other than the final one
  whose depth exceeds the threshold (``THETA_CM`` = 10 cm, or ``THETA_PROP`` = 0.1 of the arm's
  length, the two readings of the claims file; the arm length is the 96 cm of the Methods,
  Behavioral apparatus, so 9.6 cm), and in which the head moves in the negative direction along the
  arm for more than ``REVERSAL_MS`` after binary closing, is a COM event, provided the second before
  the reversal holds at least ``MIN_POS_S`` s of position samples (claims file, findProportion). The
  COM time is the start of the first such reversal that ends after the head has passed the
  threshold: the Methods define it as "the moment the rat stops advancing forward in a choice arm",
  so a short backward wiggle near the arm's entrance, before the rat advances further, is not it.
  Each event also keeps the times the head entered and left the arm's segment. The Methods name scipy's ``binary_closing`` without parameters;
  its default structure (three neighbouring samples in one dimension) is used.
- Side transitions: arms 1-2 and 3-4 are on the same side (claims file, point 5).
- Nearby control trial: drawn at random from trials t-3 to t+3 of the same session that are not
  COM trials (Methods, Identification of nearby trials; claims file, point 6).
"""

from __future__ import annotations

import json
import urllib.request
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

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
ARM_LEN_CM = 96.0          # outer arm length (Methods, Behavioral apparatus)
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


def _falling(ts, data):
    data = np.asarray(data)
    ts = np.asarray(ts)
    prev = np.concatenate([[0], data[:-1]])
    return ts[(data == 0) & (prev > 0)]


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
            if kind == "poke":
                ev[(w, "poke_off")] = _falling(g["timestamps"][:], g["data"][:])
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
        # leaving the well: the last beam release at this well before a poke at any other well
        other = np.concatenate([ev[(w, "poke")] for w in WELLS if w != f"Arm{well}"])
        nxt_other = other[other > t1].min() if np.any(other > t1) else stop
        off = ev[(f"Arm{well}", "poke_off")]
        off = off[(off > t1) & (off <= min(nxt_other, stop))]
        poke_out = off[-1] if len(off) else np.nan
        rows.append({"start": t0, "end": t1, "final": well, "rewarded": rew, "poke_out": poke_out})
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


def detect_com(trials, lin, seg_of_arm, arm_start, theta="cm", past_threshold=True):
    """COM events per trial. Returns trials with com columns and a list of events.

    ``past_threshold=False`` is the earlier rule, under which the first reversal of the visit counts
    even when it ends before the head passes the threshold; it is kept to show what the rule changes."""
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
                thr = THETA_CM if theta == "cm" else THETA_PROP * ARM_LEN_CM
                if np.nanmax(depth) <= thr:
                    continue
                i_thr = int(np.flatnonzero(depth > thr)[0])
                neg = np.diff(depth) < 0
                neg = ndimage.binary_closing(neg)
                lab, nlab = ndimage.label(neg)
                if nlab == 0:
                    continue
                sizes = ndimage.sum(neg, lab, range(1, nlab + 1))
                # a reversal counts once the head has passed the threshold: the COM time is where
                # the rat stops advancing in the arm (Methods, Change of mind time detection)
                last = ndimage.maximum(np.arange(len(neg)), lab, range(1, nlab + 1))
                ok = np.flatnonzero((sizes > rev_n) & ((np.asarray(last) >= i_thr) | (not past_threshold)))
                if len(ok) == 0:
                    continue
                first = np.flatnonzero(lab == ok[0] + 1)[0]
                t_rev = ts[a + first]
                w = (t >= t_rev - 1) & (t < t_rev)
                if np.sum(np.isfinite(lp[w])) * dt < MIN_POS_S:
                    continue
                visits.append((arm, t_rev, float(np.nanmax(depth)), ts[a], ts[b - 1]))
                if arm not in arms_entered:
                    arms_entered.append(arm)
        for arm, t_rev, depth, t_enter, t_exit in visits:
            events.append({"trial_start": tr.start, "arm": arm, "t_rev": t_rev, "depth": depth,
                           "t_enter": t_enter, "t_exit": t_exit})
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
    trials_all, events_all, trials_p, events_p, events_old = [], [], [], [], []
    for tag, (e, lin) in loaded.items():
        tr = build_trials(info["events"], e.start, e.stop)
        if len(tr) == 0:
            checks.append({"epoch": tag, "lin_files": 1, "trials": 0})
            continue
        trp, evp = detect_com(tr, lin, seg_of_arm, starts, theta="prop")
        tr0, ev0 = detect_com(tr, lin, seg_of_arm, starts, theta="cm", past_threshold=False)
        tr, evs = detect_com(tr, lin, seg_of_arm, starts, theta="cm")
        tr["com_earlier_rule"] = tr0.com.values
        ev0["epoch"] = tag
        events_old.append(ev0)
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
            "events_earlier_rule": cat(events_old),
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


def processes(fn, items, workers=12):
    """Map over items in separate processes (h5py serializes reads across threads)."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(fn, items))


def load_all(assets, workers=12):
    """load_day for every rat-day; adds rat and day columns and the day index per rat."""
    days = sorted(assets.day.unique())
    res = dict(zip(days, processes(load_day, [assets[assets.day == d] for d in days], workers=workers)))
    for d, r in res.items():
        rat = d.split("-")[0]
        for k in ("trials", "events", "trials_prop", "events_prop", "events_earlier_rule", "checks"):
            if len(r[k]):
                r[k]["rat"] = RATS[rat]
                r[k]["day"] = d
    return res


# ---------------------------------------------------------------------------------------------
# Sharp-wave ripples (figs7b-no-swr)
#
# Where the parameters come from. Ripple band 150 to 250 Hz, with 140 and 260 Hz stop edges
# (Methods, Electrophysiology, "band-pass filters to produce SWR LFP (150-250Hz pass, 140-260Hz
# stop)"); the paper uses ghostipy's FIR design, here an equiripple FIR of the same edges
# (scipy.signal.remez, a standard choice), applied with zero phase. Envelope by the Hilbert transform.
# Consensus trace: squared envelopes summed over tetrodes, smoothed by a 4 ms Gaussian; an event is
# a run of the consensus trace above 2 SD of its session baseline for at least 15 ms in which more
# than one tetrode's envelope exceeds 3 SD of its own baseline; baselines are taken where the
# head speed is above 4 cm/s and events are kept only below 4 cm/s (Methods, SWR detection). The
# "session" of the baseline is a run epoch; the baseline is estimated from BASE_N windows of
# BASE_S seconds spread evenly over the epoch, not the whole epoch, to keep the streaming small
# (an assumption, stated in the notebook). One channel per tetrode, the first good one (Methods,
# Electrophysiology, "the first functioning channel from each tetrode").
# The electrode table gives no locations, so the tetrodes are those of the LFP file with more than
# one channel in it (an assumption). The reference: the Methods subtract an ipsilateral corpus
# callosum channel; the electrode table names each channel's reference (`ref_elect_id`), which is
# in the LFP file for some rats and days only. Two readings: the LFP as deposited, and the LFP
# minus its `ref_elect_id` channel where that channel is in the file.
# Speed: the Spyglass head velocity at the camera rate (`scratch/BehavioralTimeSeries/
# head_velocity`, third column, in cm/s by its conversion of 0.01 to m/s).
# ---------------------------------------------------------------------------------------------

from scipy import signal  # noqa: E402

SWR_BAND = (150.0, 250.0)
SWR_STOP = (140.0, 260.0)
SWR_TAPS = 401
SWR_SMOOTH_MS = 4.0
SWR_CONS_SD = 2.0
SWR_IND_SD = 3.0
SWR_MIN_MS = 15.0
SWR_MIN_CH = 2
SPEED_CM_S = 4.0
BASE_N = 20
BASE_S = 4.0
PAD_S = 0.5
LFP_FS = 1000.0


def _ripple_fir(fs=LFP_FS):
    return signal.remez(SWR_TAPS, [0, SWR_STOP[0], SWR_BAND[0], SWR_BAND[1], SWR_STOP[1], fs / 2],
                        [0, 1, 0], fs=fs)


def lfp_layout(f):
    """Detection channel (column) per tetrode and the column of its reference, or -1."""
    e = f["general/extracellular_ephys/electrodes"]
    tab = pd.DataFrame({"id": e["id"][:], "nt": e["ntrode_id"][:], "ref": e["ref_elect_id"][:],
                        "bad": e["bad_channel"][:], "pe": e["probe_electrode"][:]}).set_index("id")
    ids = f["scratch/filtered data/electrodes"][:]
    col = {int(i): k for k, i in enumerate(ids)}
    sub = tab.loc[ids].assign(col=range(len(ids)))
    nper = sub.nt.value_counts()
    det = []
    for nt, g in sub[sub.nt.isin(nper.index[nper > 1])].groupby("nt"):
        g = g[~g.bad].sort_values("pe")
        if len(g) == 0:
            continue
        r = g.iloc[0]
        ref_col = col.get(int(r.ref), -1)
        if ref_col == int(r.col):
            ref_col = -1
        det.append({"ntrode": int(nt), "col": int(r.col), "ref_col": ref_col})
    det = pd.DataFrame(det)
    # a tetrode whose reference channel is the tetrode's own (the reference electrode) is left out
    ref_nts = set(sub.loc[[i for i in set(sub.ref) if i in col], "nt"])
    det = det[~det.ntrode.isin(ref_nts)]
    return det, ids


def _find_index(ts, t, n):
    """Index of the first sample at or after t in a timestamps dataset, by interpolation search."""
    lo, hi = 0, n - 1
    tlo, thi = float(ts[lo]), float(ts[hi])
    if t <= tlo:
        return 0
    for _ in range(60):
        if hi - lo <= 1:
            return hi
        g = int(lo + (t - tlo) / (thi - tlo) * (hi - lo))
        g = min(max(g, lo + 1), hi - 1)
        tg = float(ts[g])
        if tg < t:
            lo, tlo = g, tg
            # close enough: finish with a local block
            if t - tg < 2.0:
                blk = ts[g:min(g + 4000, n)]
                return g + int(np.searchsorted(blk, t))
        else:
            hi, thi = g, tg
    return hi


class LFP:
    """Streams windows of one day's LFP file."""

    def __init__(self, url):
        self.f = open_nwb(url)
        self.es = self.f["scratch/filtered data"]
        self.ts = self.es["timestamps"]
        self.n = self.ts.shape[0]
        self.det, self.ids = lfp_layout(self.f)
        self.fir = _ripple_fir()

    def read(self, t0, t1):
        i0 = _find_index(self.ts, t0, self.n)
        i1 = min(i0 + int((t1 - t0) * LFP_FS * 1.01) + 2, self.n)
        tt = self.ts[i0:i1]
        k = int(np.searchsorted(tt, t1))
        x = self.es["data"][i0:i0 + k, :]
        return tt[:k], x

    def envelopes(self, x):
        """Ripple envelopes per detection tetrode, as deposited (r0) and minus the reference (r1)."""
        x = x.astype(float)
        out = {}
        for name in ("r0", "r1"):
            sig = x[:, self.det.col.values].copy()
            if name == "r1":
                has = self.det.ref_col.values >= 0
                sig[:, has] -= x[:, self.det.ref_col.values[has]]
            filt = signal.oaconvolve(sig, self.fir[:, None], mode="same", axes=0)
            env = np.abs(signal.hilbert(filt, axis=0))
            sd = SWR_SMOOTH_MS / 1000 * LFP_FS
            out[name] = ndimage.gaussian_filter1d(env, sd, axis=0)
        return out


def _speed_at(speed, t):
    return np.interp(t, speed[0], speed[1], left=np.nan, right=np.nan)


def load_speed(url):
    g = open_nwb(url)["scratch/BehavioralTimeSeries/head_velocity"]
    return g["timestamps"][:], g["data"][:, 2]


def swr_baseline(lfp, speed, start, stop):
    """Mean and SD of the consensus trace and of each tetrode's envelope at speed > 4 cm/s."""
    stats = {"r0": ([], []), "r1": ([], [])}
    edges = np.linspace(start + PAD_S, stop - BASE_S - PAD_S, BASE_N)
    kept = []
    for a in edges:
        tt, x = lfp.read(a - PAD_S, a + BASE_S + PAD_S)
        if len(tt) < BASE_S * LFP_FS:
            continue
        env = lfp.envelopes(x)
        kept.append((a, tt, env))
        keep = (tt >= a) & (tt < a + BASE_S) & (_speed_at(speed, tt) > SPEED_CM_S)
        for name, e in env.items():
            stats[name][0].append(e[keep])
            stats[name][1].append((e[keep] ** 2).sum(1))
    out = {}
    for name, (envs, cons) in stats.items():
        envs = np.concatenate(envs) if envs else np.empty((0, len(lfp.det)))
        cons = np.concatenate(cons) if cons else np.empty(0)
        out[name] = {"env_mu": envs.mean(0), "env_sd": envs.std(0), "cons_mu": cons.mean(),
                     "cons_sd": cons.std(), "n": len(cons)}
    # a check: SWRs per second of immobility in the same windows
    for name in out:
        n_ev, imm = 0, 0.0
        for a, tt, env in kept:
            on = detect_swr(tt, env[name], out[name], speed)
            n_ev += int(((on >= a) & (on < a + BASE_S)).sum())
            inside = (tt >= a) & (tt < a + BASE_S)
            imm += float(np.sum(_speed_at(speed, tt[inside]) < SPEED_CM_S)) / LFP_FS
        out[name]["imm_events"], out[name]["imm_s"] = n_ev, imm
    return out


def detect_swr(tt, env, base, speed):
    """Onset times of SWRs in one window (see the section comment)."""
    cons = (env ** 2).sum(1)
    cz = (cons - base["cons_mu"]) / base["cons_sd"]
    iz = (env - base["env_mu"]) / base["env_sd"]
    above = cz > SWR_CONS_SD
    lab, nlab = ndimage.label(above)
    onsets = []
    min_n = SWR_MIN_MS / 1000 * LFP_FS
    sp = _speed_at(speed, tt)
    for k, sl in enumerate(ndimage.find_objects(lab), start=1):
        s = sl[0]
        if s.stop - s.start < min_n:
            continue
        nch = int(((iz[s] > SWR_IND_SD).any(0)).sum())
        if nch < SWR_MIN_CH:
            continue
        if not (sp[s.start] < SPEED_CM_S):
            continue
        onsets.append(tt[s.start])
    return np.array(onsets)


def swr_day(lfp_url, speed_by_epoch, epochs, windows):
    """Ripple counts in each window of one day.

    ``windows``: rows with ``epoch``, ``read0``, ``read1`` (the span to stream) and any number of
    ``w0_<x>``/``w1_<x>`` pairs (the windows to count in). Returns the windows with ``n_<x>_<r>``
    counts for the two reference readings, and the baselines per epoch.
    """
    lfp = LFP(lfp_url)
    base = {}
    for e in epochs.itertuples():
        if e.tag in speed_by_epoch and (windows.epoch == e.tag).any():
            base[e.tag] = swr_baseline(lfp, speed_by_epoch[e.tag], e.start, e.stop)
    names = sorted({c[3:] for c in windows.columns if c.startswith("w0_")})
    rows = []
    for w in windows.itertuples(index=False):
        row = w._asdict()
        b = base.get(w.epoch)
        if b is None:
            rows.append(row)
            continue
        tt, x = lfp.read(w.read0 - PAD_S, w.read1 + PAD_S)
        if len(tt) < 10:
            rows.append(row)
            continue
        env = lfp.envelopes(x)
        for r, e in env.items():
            on = detect_swr(tt, e, b[r], speed_by_epoch[w.epoch])
            for nm in names:
                a0, a1 = row[f"w0_{nm}"], row[f"w1_{nm}"]
                row[f"n_{nm}_{r}"] = int(((on >= a0) & (on < a1)).sum()) if np.isfinite(a0) and np.isfinite(a1) else np.nan
        rows.append(row)
    bt = pd.DataFrame([{"epoch": k, "ref": r, "n_base": v[r]["n"], "cons_mu": v[r]["cons_mu"],
                        "cons_sd": v[r]["cons_sd"], "imm_events": v[r]["imm_events"], "imm_s": v[r]["imm_s"]}
                       for k, v in base.items() for r in v])
    return pd.DataFrame(rows), bt, lfp.det.assign(n_ref=int((lfp.det.ref_col >= 0).sum()))


def speed_by_epoch(assets_day, epochs):
    """Head speed (cm/s) of each run epoch, from the camera-rate Spyglass position file."""
    objs = assets_day[assets_day.kind == "obj_behavior"]
    pr = pd.DataFrame(parallel(probe_obj, list(objs.url), workers=8), index=objs.index)
    objs = objs.join(pr)
    objs = objs[(objs.obj_kind == "position") & (objs.rate <= LIN_RATE_MIN)]
    out = {}
    for e in epochs[epochs.tag.str.contains("Session")].itertuples():
        cand = objs[(objs.t0 >= e.start - 1) & (objs.t1 <= e.stop + 1)]
        if len(cand):
            out[e.tag] = load_speed(cand.iloc[0].url)
    return out


def triggered_rows(url):
    """Trigger time, window and trial info of each row of a `scratch/triggered` table."""
    g = open_nwb(url)["scratch/triggered"]
    ta = g["time_abs"][:]
    tr = g["time_triggered"][:]
    info = g["triggered_trial_info"][:]
    if ta.ndim == 2:            # one row per trigger, fixed length
        ta, tr = ta.ravel(), tr.ravel()
        idx = np.arange(1, info.shape[0] + 1) * (len(ta) // info.shape[0])
        layout = "fixed"
    else:                       # ragged rows with an index
        idx = g["time_abs_index"][:].astype(int)
        layout = "ragged"
    rows = []
    for k, (a, b) in enumerate(zip(np.concatenate([[0], idx[:-1]]), idx)):
        if b <= a:
            continue
        off = ta[a:b] - tr[a:b]
        rows.append({"row": k, "t_trig": float(np.median(off)), "off_spread": float(np.ptp(off)),
                     "rel_min": float(tr[a:b].min()), "rel_max": float(tr[a:b].max()), "n": int(b - a),
                     "info0": int(info[k, 0]), "info1": int(info[k, 1]), "layout": layout})
    return pd.DataFrame(rows)


def triggered_day(assets_day):
    objs = assets_day[assets_day.kind == "obj"]
    pr = pd.DataFrame(parallel(probe_obj, list(objs.url), workers=8), index=objs.index)
    objs = objs.join(pr)
    objs = objs[objs.obj_kind == "triggered"]
    out = parallel(lambda u: triggered_rows(u), list(objs.url), workers=8)
    for o, p in zip(out, objs.path):
        o["file"] = p
    return pd.concat(out, ignore_index=True) if out else pd.DataFrame()


def swr_job(args):
    """swr_day for one day, with its speed; for ``processes``."""
    lfp_url, assets_day, epochs, windows = args
    sp = speed_by_epoch(assets_day, epochs)
    return swr_day(lfp_url, sp, epochs, windows)


# ---------------------------------------------------------------------------------------------
# Triggered decode tables (Figure 3)
#
# The `scratch/triggered` tables are written by the paper's code
# (Gu2026 at commit 0f0c9a7, changeOfMind_triggered_position.save_triggered_position_decode_day and
# changeOfMind_triggered.find_triggered_session): per row, a window of the 500 Hz linearized head
# position and the decoded position, as `triggered_positions` (position minus the position at the
# trigger, or absolute when the window is not restricted to the arm), `triggered_positions_baseoff`
# (indexed by absolute time), `triggered_decodes_baseoff` (decode minus the arm's base) and
# `triggered_decodes_abs`; `triggered_trial_info` is (trial, arm). The decode is the MAP when the
# table was made with max_flag (turnaround_triggered_decode); restricted to the arm, moments with
# 0.2 or less of the causal posterior in the arm are NaN. Which parameter set made a file is kept in
# the lab's database, not in the file; here each file is identified by aligning its trigger times
# with this entry's COM times and outer pokes, and by its window.
# Arm regions on the linearization: the base and outer end of the home arm and the four outer arms,
# as the code gives them (changeOfMind_remote_interval.loc1d_to_baseoff); checked against the
# deposited linearization in the notebook.
# ---------------------------------------------------------------------------------------------

ARM_REGIONS = np.array([[0.0, 57.63896252], [165.66041604, 252.64353221], [331.10211383, 418.29227956],
                        [496.49241045, 583.18763812], [657.72023142, 743.03215907]])
FIG3_MAX_CM = 80.0     # head within the first 80 cm of the arm (figure4c.maze_distance)
TRIG_TOL_S = 0.02


def loc_baseoff(x):
    """(arm, distance from the arm's base toward its outer end) of linear positions; NaN off arms
    (changeOfMind_remote_interval.loc1d_to_baseoff; the home arm, 0, is measured from its end)."""
    x = np.asarray(x, dtype=float)
    arm = np.full(x.shape, np.nan)
    d = np.full(x.shape, np.nan)
    for k, (a, b) in enumerate(ARM_REGIONS):
        m = (x >= a) & (x < b)
        arm[m] = k
        d[m] = (b - x[m]) if k == 0 else (x[m] - a)
    return arm, d


def maze_distance_max(pos, dec):
    """Largest maze distance between head and decode, through the centre when on different arms
    (figure4c.maze_distance_max)."""
    if len(pos) == 0:
        return np.nan
    ap, dp = loc_baseoff(pos)
    ad, dd = loc_baseoff(dec)
    dist = np.where(ap == ad, np.abs(dp - dd), dp + dd)
    return np.nanmax(dist) if np.any(np.isfinite(dist)) else np.nan


def read_triggered(url):
    g = open_nwb(url)["scratch/triggered"]
    cols = ["time_abs", "time_triggered", "triggered_positions", "triggered_positions_baseoff",
            "triggered_decodes_baseoff", "triggered_decodes_abs"]
    info = g["triggered_trial_info"][:]
    rows = [{} for _ in range(info.shape[0])]
    for c in cols:
        data = g[c][:]
        if f"{c}_index" in g:       # ragged rows, each column with its own index
            idx = g[f"{c}_index"][:].astype(int)
            b0 = np.concatenate([[0], idx[:-1]])
            for k, (a, b) in enumerate(zip(b0, idx)):
                rows[k][c] = data[a:b]
        elif data.ndim == 2:        # one row per trigger, fixed length
            for k in range(len(rows)):
                rows[k][c] = data[k]
        else:                       # one value per row
            for k in range(len(rows)):
                rows[k][c] = np.atleast_1d(data[k])
    for k, r in enumerate(rows):
        r["trial"], r["arm"] = int(info[k, 0]), int(info[k, 1])
        n = len(r["time_abs"])
        for c in cols:              # a decode the code could not align is stored empty: NaN here
            if len(r[c]) != n:
                r[c] = np.full(n, np.nan)
    return rows


def _nearest(v, x):
    v = np.sort(np.asarray(v))
    if len(v) == 0:
        return np.full(len(x), np.inf)
    j = np.clip(np.searchsorted(v, x), 1, max(len(v) - 1, 1))
    return np.minimum(np.abs(x - v[j - 1]), np.abs(x - v[np.minimum(j, len(v) - 1)]))


def classify_triggered(rows, com_times, poke_times):
    """What a file holds: trigger (COM time, outer poke, other), window and whether restricted to the arm."""
    rows = [r for r in rows if len(r["time_abs"])]
    trig = np.array([np.median(r["time_abs"] - r["time_triggered"]) for r in rows])
    rel_min = np.array([np.nanmin(r["time_triggered"]) for r in rows])
    rel_max = np.array([np.nanmax(r["time_triggered"]) for r in rows])
    d_com = _nearest(com_times, trig)
    d_poke = _nearest(poke_times, trig)
    trigger = ("com" if np.mean(d_com < TRIG_TOL_S) > 0.5 else
               "poke" if np.mean(d_poke < TRIG_TOL_S) > 0.5 else "other")
    window = ("pre" if np.all(rel_max <= 0.01) else "post" if np.all(rel_min >= -0.01) else "both")
    # restricted to the arm: positions are relative to the trigger position (0 at the trigger)
    at0 = [r["triggered_positions"][np.argmin(np.abs(r["time_triggered"]))] for r in rows]
    segment = bool(np.nanmax(np.abs(at0)) < 1e-6)
    return {"trigger": trigger, "window": window, "segment": segment, "rows": len(rows),
            "frac_com": float(np.mean(d_com < TRIG_TOL_S)), "frac_poke": float(np.mean(d_poke < TRIG_TOL_S)),
            "median_d_com": float(np.median(d_com)), "median_d_poke": float(np.median(d_poke)),
            "rel_min": float(np.median(rel_min)), "rel_max": float(np.median(rel_max)),
            "nan_decode": float(np.mean(np.concatenate([np.isnan(r["triggered_decodes_abs"]) for r in rows])))}


def _speed_rows(rows, speeds):
    """Head speed at each sample of each row, from the run epoch whose speed covers it."""
    out = []
    for r in rows:
        t = r["time_abs"]
        s = np.full(len(t), np.nan)
        for ts, sp in speeds.values():
            if len(ts) and t[0] >= ts[0] - 1 and t[-1] <= ts[-1] + 1:
                s = np.interp(t, ts, sp)
                break
        out.append(s)
    return out


def segment_metrics(rows, speeds):
    """Per row, at head speed of 4 cm/s or more: the max |head - decode| within the arm (both from the
    arm base), the range of head positions and the number of samples (figure4c.return_distance_max and
    make_distance_plot)."""
    sp = _speed_rows(rows, speeds)
    out = []
    for r, s in zip(rows, sp):
        pos = np.array(r["triggered_positions_baseoff"], dtype=float)
        dec = np.array(r["triggered_decodes_baseoff"], dtype=float)
        slow = ~(s >= SPEED_CM_S)
        pos[slow] = np.nan
        dec[slow] = np.nan
        out.append({"trial": r["trial"], "arm": r["arm"], "t_trig": float(np.median(r["time_abs"] - r["time_triggered"])),
                    "pos": pos, "dec": dec, "n": len(pos),
                    "pos_min": np.nanmin(pos) if np.any(np.isfinite(pos)) else np.nan,
                    "pos_max": np.nanmax(pos) if np.any(np.isfinite(pos)) else np.nan,
                    "speed_known": float(np.mean(np.isfinite(s)))})
    return out


def max_dist(pos, dec, fix_range=None):
    if fix_range is not None:
        m = (pos >= fix_range[0]) & (pos <= fix_range[1])
        if not np.any(m):
            return np.nan
        pos, dec = pos[m], dec[m]
    d = np.abs(pos - dec)
    return np.nanmax(d) if np.any(np.isfinite(d)) else np.nan


def prepost_maze(rows, speeds):
    """Per row of a whole-track table around COM time: max maze distance before and after stopping,
    head within the first 80 cm of the arm and at 4 cm/s or more (figure4c.maze_distance)."""
    sp = _speed_rows(rows, speeds)
    out = []
    for r, s in zip(rows, sp):
        base = ARM_REGIONS[r["arm"]][0]
        pos = np.asarray(r["triggered_positions_baseoff"], dtype=float)
        dec = np.asarray(r["triggered_decodes_baseoff"], dtype=float) + base
        rel = np.asarray(r["time_triggered"])
        inarm = (pos - base >= 0) & (pos - base <= FIG3_MAX_CM)
        fast = s >= SPEED_CM_S
        row = {"trial": r["trial"], "arm": r["arm"], "t_trig": float(np.median(r["time_abs"] - rel))}
        if not np.any(inarm):
            continue
        t0 = np.argmin(np.abs(rel[inarm]))
        p, d_, f = pos[inarm], dec[inarm], fast[inarm]
        pre, post = np.arange(len(p)) < t0, np.arange(len(p)) >= t0
        if not pre.any() or not post.any() or not (pre & f).any() or not (post & f).any():
            continue
        row["d_pre"] = maze_distance_max(p[pre & f], d_[pre & f])
        row["d_post"] = maze_distance_max(p[post & f], d_[post & f])
        row["post_min"] = float(np.min(p[post & f] - base))
        row["post_max"] = float(np.max(p[post & f] - base))
        out.append(row)
    return out


def segment_maze_post(rows, speeds, fix_ranges, rng):
    """Max maze distance on an arm-restricted table (decode NaN off the arm), at 4 cm/s or more,
    over a head range drawn from ``fix_ranges`` (figure4c.maze_distance_max with fix_range)."""
    sp = _speed_rows(rows, speeds)
    out = []
    for r, s in zip(rows, sp):
        base = ARM_REGIONS[r["arm"]][0]
        pos = np.asarray(r["triggered_positions_baseoff"], dtype=float) + base
        dec = np.asarray(r["triggered_decodes_baseoff"], dtype=float) + base
        m = (s >= SPEED_CM_S) & (pos >= base) & (pos <= ARM_REGIONS[r["arm"]][1])
        fr = fix_ranges[rng.integers(len(fix_ranges))] if len(fix_ranges) else None
        if fr is not None:
            m &= (pos - base >= fr[0]) & (pos - base <= fr[1])
        out.append({"trial": r["trial"], "arm": r["arm"], "d_post": maze_distance_max(pos[m], dec[m]) if m.any() else np.nan})
    return out


N_DRAWS = 20   # further draws of the control arm ranges, each with its own seed (a standard choice)


def _row_trig(r):
    return float(np.median(r["time_abs"] - r["time_triggered"]))


def pair_agreement(rows_by_file, tol_s=1e-3):
    """For every two tables of a day that share trigger times: at the samples both hold, how often
    their decodes agree to within 1 cm (both finite), overall and where both lie on the row's arm.
    The decodes lie on the decoder's 2 cm grid, so two decodes either agree or differ by 2 cm or more;
    the 1 cm tolerance is a standard choice that cannot change a result."""
    keys = {f: {int(round(_row_trig(r) / tol_s)): r for r in rows} for f, rows in rows_by_file.items()}
    files = sorted(keys)
    out = []
    for i, fa in enumerate(files):
        for fb in files[i + 1:]:
            shared = sorted(set(keys[fa]) & set(keys[fb]))
            if not shared:
                continue
            n, eq, n_arm, eq_arm = 0, 0, 0, 0
            for k in shared:
                ra, rb = keys[fa][k], keys[fb][k]
                ta = np.round(np.asarray(ra["time_abs"]) * 1e4).astype(np.int64)
                tb = np.round(np.asarray(rb["time_abs"]) * 1e4).astype(np.int64)
                _, ia, ib = np.intersect1d(ta, tb, return_indices=True)
                da = np.asarray(ra["triggered_decodes_abs"], dtype=float)[ia]
                db = np.asarray(rb["triggered_decodes_abs"], dtype=float)[ib]
                ok = np.isfinite(da) & np.isfinite(db)
                n += int(ok.sum())
                eq += int((np.abs(da - db)[ok] < 1.0).sum())
                lo, hi = ARM_REGIONS[ra["arm"]]
                inarm = ok & (da >= lo) & (da < hi) & (db >= lo) & (db < hi)
                n_arm += int(inarm.sum())
                eq_arm += int((np.abs(da - db)[inarm] < 1.0).sum())
            out.append({"file_a": fa, "file_b": fb, "shared_rows": len(shared), "samples": n,
                        "frac_equal": eq / n if n else np.nan, "samples_on_arm": n_arm,
                        "frac_equal_on_arm": eq_arm / n_arm if n_arm else np.nan})
    return pd.DataFrame(out)


def segment_post_com(rows, speeds):
    """Per row of an arm-restricted table around COM time: the largest maze distance after the
    trigger, head within the first 80 cm of the arm and at 4 cm/s or more, decode within the arm
    (the measure of the inbound rows, segment_maze_post, without the drawn range)."""
    sp = _speed_rows(rows, speeds)
    out = []
    for r, s in zip(rows, sp):
        base = ARM_REGIONS[r["arm"]][0]
        pos = np.asarray(r["triggered_positions_baseoff"], dtype=float) + base
        dec = np.asarray(r["triggered_decodes_baseoff"], dtype=float) + base
        rel = np.asarray(r["time_triggered"])
        m = (s >= SPEED_CM_S) & (pos >= base) & (pos - base <= FIG3_MAX_CM) & (rel >= 0)
        out.append({"trial": r["trial"], "arm": r["arm"], "t_trig": _row_trig(r),
                    "d_post": maze_distance_max(pos[m], dec[m]) if m.any() else np.nan})
    return out


def fig3_day(args):
    """All triggered tables of one day: what each holds, and the Figure 3 measures."""
    assets_day, epochs, com_times, poke_times, seed = args
    rng = np.random.default_rng(seed)
    speeds = speed_by_epoch(assets_day, epochs)
    objs = assets_day[assets_day.kind == "obj"]
    pr = pd.DataFrame([probe_obj(u) for u in objs.url], index=objs.index)
    objs = objs.join(pr)
    objs = objs[objs.obj_kind == "triggered"]
    files, rows_by_file = [], {}
    for p, u in zip(objs.path, objs.url):
        try:
            rows = [r for r in read_triggered(u) if len(r["time_abs"])]
        except Exception as e:      # reported in the notebook
            files.append({"file": p, "trigger": "unreadable", "window": "", "segment": False, "rows": 0, "error": repr(e)})
            continue
        if not rows:
            continue
        c = classify_triggered(rows, com_times, poke_times)
        c["file"] = p
        files.append(c)
        rows_by_file[p] = rows
    files = pd.DataFrame(files)
    res = {"files": files, "com_pre": [], "poke_pre": [], "com_both": {}, "poke_post": [], "other_rows": [],
           "com_both_other": {}, "com_seg_post": [], "other_pre": [], "pairs": pd.DataFrame()}
    if len(files) == 0:
        return res
    res["pairs"] = pair_agreement(rows_by_file)
    # Which decoder made each whole-track table: its agreement, on the arm, with the arm-restricted
    # tables that share its triggers (all of these come from one decoder; see the notebook)
    seg = set(files[files.segment].file)
    agree = {}
    for x in res["pairs"].itertuples():
        for a, b in ((x.file_a, x.file_b), (x.file_b, x.file_a)):
            if b in seg and a not in seg and x.samples_on_arm >= 100:
                agree[a] = max(agree.get(a, 0.0), x.frac_equal_on_arm)
    files["arm_table_agreement"] = files.file.map(agree)
    # The rows of the tables that match neither trigger: their trigger times, and how far each is from
    # this entry's COM times and outer pokes
    for f in files[files.trigger == "other"].file:
        c = files[files.file == f].iloc[0]
        for r in rows_by_file[f]:
            t = np.array([_row_trig(r)])
            res["other_rows"].append({"file": f, "window": c.window, "segment": bool(c.segment), "trial": r["trial"],
                                      "arm": r["arm"], "t_trig": float(t[0]), "d_com": float(_nearest(com_times, t)[0]),
                                      "d_poke": float(_nearest(poke_times, t)[0])})
    sel = lambda trig, win, seg: files[(files.trigger == trig) & (files.window == win) & (files.segment == seg)].file
    for f in sel("com", "pre", True):
        res["com_pre"] += [dict(m, file=f) for m in segment_metrics(rows_by_file[f], speeds)]
    for f in sel("poke", "pre", True):
        res["poke_pre"] += [dict(m, file=f) for m in segment_metrics(rows_by_file[f], speeds)]
    for f in sel("com", "both", False):
        res["com_both"][f] = prepost_maze(rows_by_file[f], speeds)
    post_ranges = [(r["post_min"], r["post_max"]) for v in res["com_both"].values() for r in v]
    for f in sel("poke", "post", True):
        res["poke_post"] += [dict(m, file=f) for m in segment_maze_post(rows_by_file[f], speeds, post_ranges, rng)]
    # fig3b control: each control row's distance over a head range drawn from the day's COM ranges
    ranges = [(m["pos_min"], m["pos_max"]) for m in res["com_pre"] if np.isfinite(m["pos_min"])]
    for m in res["poke_pre"]:
        fr = ranges[rng.integers(len(ranges))] if ranges else None
        m["d_matched"] = max_dist(m["pos"], m["dec"], fr) if fr else np.nan
        m["d_all"] = max_dist(m["pos"], m["dec"])
    # Variants asked for by the verifier (round 2). Each further draw has its own generator, so the
    # draws above are unchanged.
    for k in range(1, N_DRAWS + 1):
        g = np.random.default_rng([seed, k])
        for m in res["poke_pre"]:
            fr = ranges[g.integers(len(ranges))] if ranges else None
            m[f"d_matched_{k}"] = max_dist(m["pos"], m["dec"], fr) if fr else np.nan
        g = np.random.default_rng([seed, 100 + k])
        j = 0
        for f in sel("poke", "post", True):
            for m in segment_maze_post(rows_by_file[f], speeds, post_ranges, g):
                res["poke_post"][j][f"d_post_{k}"] = m["d_post"]
                j += 1
    # every row of the "other" whole-track tables around a trigger, flagged by whether its trigger
    # is within TRIG_TOL_S of a COM time of this entry
    for f in sel("other", "both", False):
        res["com_both_other"][f] = [dict(m, aligned=bool(_nearest(com_times, np.array([m["t_trig"]]))[0] < TRIG_TOL_S))
                                    for m in prepost_maze(rows_by_file[f], speeds)]
    # COM rows of the arm-restricted tables around COM time, measured as the inbound rows are
    for f in sel("com", "both", True):
        res["com_seg_post"] += [dict(m, file=f) for m in segment_post_com(rows_by_file[f], speeds)]
    # rows of the arm-restricted tables before stopping that match neither trigger
    for f in sel("other", "pre", True):
        res["other_pre"] += [dict(m, file=f) for m in segment_metrics(rows_by_file[f], speeds)]
    for m in res["com_pre"] + res["other_pre"]:
        m["d_all"] = max_dist(m["pos"], m["dec"])
        m["speed"] = ((m["pos_max"] - m["pos_min"]) / (m["n"] * 0.002)) if m["n"] >= 250 else np.nan
    for m in res["poke_pre"]:
        m["speed"] = ((m["pos_max"] - m["pos_min"]) / (m["n"] * 0.002)) if m["n"] >= 250 else np.nan
    for k in ("com_pre", "poke_pre", "other_pre"):
        for m in res[k]:
            m.pop("pos"), m.pop("dec")
    return res


def theta_speed_check(args):
    """Clock check of the LFP against the head speed: correlation of theta (6-10 Hz) amplitude on the
    first detection tetrode with speed, over 300 s of a run epoch, at shifts of the speed trace."""
    lfp_url, speed, start, shifts = args
    lfp = LFP(lfp_url)
    tt, x = lfp.read(start + 60, start + 360)
    sos = signal.butter(4, [6, 10], btype="band", fs=LFP_FS, output="sos")
    th = np.abs(signal.hilbert(signal.sosfiltfilt(sos, x[:, lfp.det.col.values[0]].astype(float))))
    th = ndimage.uniform_filter1d(th, int(LFP_FS))[::100]
    t = tt[::100]
    out = {}
    for sh in shifts:
        s = np.interp(t + sh, speed[0], speed[1])
        ok = np.isfinite(s)
        out[sh] = stats_spearman(th[ok], s[ok])
    return out


def stats_spearman(a, b):
    from scipy.stats import spearmanr
    return float(spearmanr(a, b)[0])
