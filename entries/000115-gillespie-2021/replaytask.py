"""Loading and behavioural measures for dandiset 000115 (Gillespie et al. 2021, Neuron).

Gillespie, Astudillo Maya, Denovellis, Liu, Kastner, Coulter, Roumis, Eden & Frank (2021),
Neuron 109, 3149-3163, doi:10.1016/j.neuron.2021.07.029.

Each NWB file holds one recording day of one rat: raw 30 kHz broadband from 128 channels
(`acquisition/e-series`, no spikes, LFP or ripple times), port beam breaks, lights and pumps
(`processing/behavior/behavioral_events`), head LED position per epoch
(`processing/behavior/position/series_*`), and the StateScript log of each epoch as text
(`processing/associated_files/statescript_<epoch>`, attribute `content`). Run epochs are tagged
`NN_rK` in `intervals/epochs`. Files are streamed from the archive at the pinned version; nothing
is written to disk.

Trials are rebuilt from the StateScript log, which prints every port entry (`UP n`), each
reward at an outer port (`outer reward`), the goal arm before each outer visit
(`CURRENTGOAL IS [n]`, printed when the centre-port wait ends) and each timeout
(`WHITENOISE`). Ports 1 to 8 are the outer arms, 10 the home port and 11 and 12 the centre
ports (the log's own `define wells`).

Where the parameters come from:

- A trial is a completed home, centre and outer sequence; timeout (lockout) trials are dropped,
  as the claims file's opening comment gives the paper's code (dfa_ripcontent.m, `nonlocktrials`).
- Task phase follows the claims file's opening comment, which reads label_trial_interval.m of
  the paper's code (LorenFrankLab/Gillespie_Neuron_2021 at 1be6a6a): 0 or -0.2 for search trials
  before the goal is found (-0.2 when the arm was already visited in this search), an integer n
  for the n-th reward of the block, n + 0.5 for an error at an arm next to the goal (arm number
  differs by 1), n + 0.3 for an error at the previous goal, n + 0.8 for other errors, and
  n + 0.9 for the final unrewarded visit to the old goal after the goal changes.
- The trial that closes a block: the claims file's opening comment (after a reader's answer)
  gives the first valid trial after each goal change to the old block, whatever arm it visits,
  as label_trial_interval.m (goalbounds) and dfa_ripcontent.m ("[1 ctemp(1:end-1)]") do. This
  is `FINAL_TRIAL` = "first_after_switch". The other value of `FINAL_TRIAL_READINGS`,
  "old_goal_visit" (only a visit to the old goal closes the block), was the second reading run
  before the answer; it is kept to show what the answer changed and decides nothing.
- A block counts for Figure 1D to 1F when it has a trial of task phase >= 4 (claims file,
  fig1d-sessions-blocks, from dfs_ripcontent.m part 2, `any(ctphase>=4)`).
- The error subtypes n + 0.3, 0.5 and 0.8 are not used by any test here (only integer phases,
  phase <= 1 against > 1 and the reward flags are); the claims file does not say which arms
  count as next to the goal, and arms 1 and 8 are not treated as neighbours.
- A log shows forage assist when a `CURRENTGOAL IS [...]` line lists more than one arm: with
  forageNum above 1 the observer's goalWell holds several arms until one is found (the
  observer code in the log headers); `n_multi_goal_lines` counts such lines.
- The visit traces of fig6b-visits-decay follow its criterion (as fig6a-pg-replay-persists, for
  visits, unsmoothed): per block 1 to 8, the goal arm's visits from 40 trials before to 40
  after the block's last rewarded trial, NaN beyond the session, against the same window for
  every arm never a goal in the session.
- The reward-rate curves (fig1ef-reward-rate) take trials 1 to 15 and the binomial S.E.M.
  sqrt(p(1-p)/n), as the claim's criterion gives them.
"""

from __future__ import annotations

import hashlib
import re
import time
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000115"
DANDISET_VERSION = "0.210914.1732"

SUBJECTS = ["jaq", "roquefort", "despereaux", "montague"]  # subjects 1 to 4 of the legends
OUTER_ARMS = list(range(1, 9))
HOME_PORT, CENTER_PORTS = 10, (11, 12)
FINAL_TRIAL_READINGS = ("first_after_switch", "old_goal_visit")
FINAL_TRIAL = "first_after_switch"   # claims file, opening comment
FULL_BLOCK_PHASE = 4          # any(ctphase>=4), dfs_ripcontent.m part 2
CURVE_TRIALS = np.arange(1, 16)
CHANCE = 1 / 8


# --------------------------------------------------------------------------- archive access

def list_assets():
    """Assets of the pinned version: path, asset id, size and S3 URL."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = [{"path": a.path, "asset_id": a.identifier, "size": a.size,
                 "url": a.get_content_url(follow_redirects=1, strip_query=True)}
                for a in ds.get_assets()]
    df = pd.DataFrame(rows).sort_values("path").reset_index(drop=True)
    df["subject"] = df.path.str.extract(r"sub-([a-z]+)/")[0]
    df["day"] = df.path.str.extract(r"ses-[a-z]+-(\d+)_")[0].astype(int)
    return df


def open_nwb(url):
    return h5py.File(remfile.File(url), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


# --------------------------------------------------------------------------- StateScript

def parse_statescript(content):
    """Event lines of a StateScript log as a list of (time in ms, message)."""
    events = []
    for line in content.split("\n"):
        if not line or line[0] in "#~":
            continue
        head, _, msg = line.partition(" ")
        if head.isdigit() and msg:
            events.append((int(head), msg.strip()))
    return events


def header_parameters(content):
    """Task parameters set in the embedded Python observer (uncommented lines only)."""
    hdr = [l[1:] for l in content.split("\n") if l.startswith("#") and not l.startswith("##")]
    get = lambda pat: next((m.group(1).strip() for l in hdr for m in [re.match(pat, l)] if m), None)
    return {"programs": re.findall(r"#<([^>]+)>", content),
            "forageNum": get(r"forageNum = (.+)"), "numgoals": get(r"numgoals = (.+)"),
            "outerReps_setting": get(r"outerReps = (.+)")}


def trials_from_events(events):
    """One row per trial that reached an outer visit or a timeout after the centre-port wait.

    A trial opens when the log prints the goal (`CURRENTGOAL IS [n]`, end of the centre wait)
    and closes at the next outer-port entry (a valid trial) or at a timeout (`WHITENOISE`,
    a lockout trial). Rewarded means an `outer reward` line within 100 ms of the entry.
    """
    rows, goal, pending, t_goal = [], None, False, None
    for i, (t, msg) in enumerate(events):
        if msg.startswith("CURRENTGOAL"):
            goal = int(re.findall(r"\d+", msg)[0])
            if not pending:
                t_goal = t
            pending = True
        elif msg == "WHITENOISE":
            if pending:
                rows.append({"t_ms": t, "t_goal_ms": t_goal, "outer": -1, "goal": goal,
                             "rewarded": False, "lockout": True})
            pending = False
        elif msg.startswith("UP "):
            port = int(msg[3:])
            if pending and port in OUTER_ARMS:
                rew = any(m == "outer reward" for tt, m in events[i + 1:i + 20] if tt - t < 100)
                rows.append({"t_ms": t, "t_goal_ms": t_goal, "outer": port, "goal": goal,
                             "rewarded": rew, "lockout": False})
                pending = False
    return pd.DataFrame(rows, columns=["t_ms", "t_goal_ms", "outer", "goal", "rewarded", "lockout"])


def label_task_phase(trials, final=FINAL_TRIAL):
    """Block number and task phase for the valid (non-lockout) trials of one session.

    Returns a copy of the valid trials with columns block (1, 2, ...), block_goal, prev_goal,
    phase and final (True for the trial that closes a block after the goal switched).
    """
    v = trials[~trials.lockout].reset_index(drop=True).copy()
    n = len(v)
    block = np.zeros(n, int)
    is_final = np.zeros(n, bool)
    goals_seen = []
    b = 0
    for i in range(n):
        if i == 0:
            b = 1
            goals_seen.append(v.goal[0])
        elif v.goal[i] != v.goal[i - 1] and not is_final[i - 1]:
            old = v.goal[i - 1]
            closes = (final == "first_after_switch") or (v.outer[i] == old and not v.rewarded[i])
            if closes:
                is_final[i] = True          # stays in the old block
            else:
                b += 1
                goals_seen.append(v.goal[i])
        elif i > 0 and is_final[i - 1]:
            b += 1
            goals_seen.append(v.goal[i])
        block[i] = b
    v["block"] = block
    v["final"] = is_final
    v["block_goal"] = [goals_seen[k - 1] for k in block]
    v["prev_goal"] = [goals_seen[k - 2] if k > 1 else 0 for k in block]
    phase = np.zeros(n)
    for k in np.unique(block):
        idx = np.where(block == k)[0]
        g = goals_seen[k - 1]
        pg = goals_seen[k - 2] if k > 1 else None
        nrew, searched = 0, set()
        for i in idx:
            o = v.outer[i]
            if v.rewarded[i] and not is_final[i]:
                nrew += 1
                phase[i] = nrew
            elif nrew == 0:
                phase[i] = -0.2 if o in searched else 0.0
                searched.add(o)
            elif is_final[i] and o == g:
                phase[i] = nrew + 0.9
            elif abs(o - g) == 1:
                phase[i] = nrew + 0.5
            elif pg is not None and o == pg:
                phase[i] = nrew + 0.3
            else:
                phase[i] = nrew + 0.8
    v["phase"] = phase
    return v


def full_blocks(labelled):
    """Blocks with a trial of task phase >= 4."""
    g = labelled.groupby("block").phase.max()
    return g.index[g >= FULL_BLOCK_PHASE].tolist()


def reward_curves(labelled):
    """Per full block, rewards on trials 1-15 from the block start and after the first reward.

    The block's closing unrewarded trial is dropped (fig1ef-reward-rate). A trial scores 1
    when it is a reward (integer task phase >= 1).
    """
    search, repeat = [], []
    for k in full_blocks(labelled):
        bt = labelled[(labelled.block == k) & ~labelled.final]
        rew = (bt.rewarded & (bt.phase >= 1)).to_numpy().astype(float)
        s = np.full(len(CURVE_TRIALS), np.nan)
        m = min(len(rew), len(CURVE_TRIALS))
        s[:m] = rew[:m]
        search.append(s)
        first = int(np.where(bt.phase.to_numpy() == 1)[0][0])
        after = rew[first + 1:]
        r = np.full(len(CURVE_TRIALS), np.nan)
        m = min(len(after), len(CURVE_TRIALS))
        r[:m] = after[:m]
        repeat.append(r)
    return np.array(search).reshape(-1, len(CURVE_TRIALS)), np.array(repeat).reshape(-1, len(CURVE_TRIALS))


VISIT_WINDOW = 40   # fig6b-visits-decay, as fig6a-pg-replay-persists: 40 trials either side
VISIT_BLOCKS = 8    # blocks 1 to 8


def visit_traces(labelled, completed_only=False):
    """Goal and non-goal visit traces around the last rewarded trial of each block.

    Returns (goal, nongoal): arrays of shape (n, 81) for trials -40 to +40, 1 when the arm was
    visited on that trial, 0 when not, NaN beyond the session. Blocks 1 to 8 with at least one
    reward; with `completed_only`, only blocks closed by a goal change. Non-goal arms are the
    arms never a goal in the session, one trace per arm and block.
    """
    v = labelled.reset_index(drop=True)
    outer, block = v.outer.to_numpy(), v.block.to_numpy()
    rewarded, final = v.rewarded.to_numpy(), v.final.to_numpy()
    n = len(v)
    never = [a for a in OUTER_ARMS if a not in set(v.block_goal)]
    offs = np.arange(-VISIT_WINDOW, VISIT_WINDOW + 1)
    goal, nongoal = [], []
    for k in range(1, VISIT_BLOCKS + 1):
        rows = np.where(block == k)[0]
        rew = rows[rewarded[rows] & ~final[rows]]
        if len(rew) == 0 or (completed_only and not final[rows].any()):
            continue
        idx = rew[-1] + offs
        inside = (idx >= 0) & (idx < n)
        seen = np.full(len(offs), -1)
        seen[inside] = outer[idx[inside]]
        for arm, out in [(v.block_goal[rows[0]], goal)] + [(a, nongoal) for a in never]:
            out.append(np.where(inside, (seen == arm).astype(float), np.nan))
    w = len(offs)
    return np.array(goal).reshape(-1, w), np.array(nongoal).reshape(-1, w)


def binomial_curve(mat):
    """Mean, binomial S.E.M. sqrt(p(1-p)/n) and n per column, ignoring NaN."""
    n = np.sum(~np.isnan(mat), axis=0)
    p = np.nanmean(mat, axis=0)
    se = np.sqrt(p * (1 - p) / n)
    return p, se, n


# --------------------------------------------------------------------------- per-file loading

def _events_on(group, start, stop):
    d, ts = group["data"][:], group["timestamps"][:]
    keep = (ts >= start) & (ts <= stop)
    return d[keep], ts[keep]


def load_day(asset):
    """Everything the behavioural analysis needs from one file, read as it streams.

    Returns a dict with the file's metadata and one entry per run epoch: the StateScript
    trials, task parameters, a hash of the log, and the DIO and position checks.
    """
    t0 = time.time()
    f = open_nwb(asset["url"])
    ep = f["intervals/epochs"]
    tags = [_s(t) for t in ep["tags"][:]]
    starts, stops = ep["start_time"][:], ep["stop_time"][:]
    el = f["general/extracellular_ephys/electrodes"]
    es = f["acquisition/e-series"]
    day = {"path": asset["path"], "subject": _s(f["general/subject/subject_id"][()]),
           "session_id": _s(f["general/session_id"][()]), "day": int(asset["day"]),
           "session_start": _s(f["session_start_time"][()]),
           "tags": tags, "n_epochs": len(tags), "epoch_seconds": float(np.sum(stops - starts)),
           "tasks": {k: (_s(f["processing/tasks"][k]["task_name"][0]),
                         _s(f["processing/tasks"][k]["task_description"][0]),
                         f["processing/tasks"][k]["task_epochs"][:].ravel().tolist())
                     for k in f["processing/tasks"]},
           "electrode_locations": sorted({_s(x) for x in el["location"][:]}),
           "n_channels": int(es["data"].shape[1]), "n_samples": int(es["data"].shape[0]),
           "ephys_chunks": es["data"].chunks, "ephys_conversion": float(es["data"].attrs["conversion"]),
           "ephys_t0": float(es["timestamps"][0]), "ephys_t1": float(es["timestamps"][-1]),
           "bytes": int(asset["size"]), "runs": []}
    be = f["processing/behavior/behavioral_events"]
    pos = f["processing/behavior/position"]
    pos_series = {}
    for k in pos:
        ts = pos[k]["timestamps"][:]
        pos_series[k] = (ts, pos[k]["data"], float(pos[k]["data"].attrs["conversion"]))
    for key in f["processing/associated_files"]:
        a = f["processing/associated_files"][key].attrs
        if not re.match(r"statescript_r\d+$", key):
            continue
        content = _s(a["content"])
        ep_index = int(re.findall(r"\d+", _s(a["task_epochs"]))[0]) - 1
        start, stop = float(starts[ep_index]), float(stops[ep_index])
        events = parse_statescript(content)
        trials = trials_from_events(events)
        params = header_parameters(content)
        run = {"key": key, "epoch_tag": tags[ep_index], "epoch_index": ep_index + 1,
               "start": start, "stop": stop, "duration_min": (stop - start) / 60,
               "sc_hash": hashlib.md5(content.encode()).hexdigest()[:12],
               "n_events": len(events),
               "n_outer_reward_lines": sum(m == "outer reward" for _, m in events),
               "n_multi_goal_lines": sum(len(re.findall(r"\d+", m)) > 1 for _, m in events
                                         if m.startswith("CURRENTGOAL")),
               "outerreps_printed": sorted({int(x) for x in re.findall(r"outerreps = (\d+)",
                                                                       "\n".join(m for _, m in events))}),
               "trials": trials, **params}
        # DIO: reward pumps and beam breaks per arm inside this epoch
        pumps, beams = [], []
        for arm in OUTER_ARMS:
            d, ts = _events_on(be[f"arm{arm}pump"], start, stop)
            pumps += [(t, arm) for t in ts[d == 1]]
            d, ts = _events_on(be[f"arm{arm}beam"], start, stop)
            beams += [(t, arm) for t in ts[d == 1]]
        pumps.sort()
        beams.sort()
        run["dio_pump_arms"] = np.array([a for _, a in pumps], int)
        run["dio_pump_t"] = np.array([t for t, _ in pumps])
        run["dio_beam_arms"] = np.array([a for _, a in beams], int)
        run["dio_beam_t"] = np.array([t for t, _ in beams])
        # position series covering this epoch
        best = None
        for k, (ts, data, conv) in pos_series.items():
            overlap = np.mean((ts >= start) & (ts <= stop))
            if overlap > 0.9:
                best = k
        if best is not None:
            ts, data, conv = pos_series[best]
            xy = data[:, :2].astype(float) * conv
            finite = np.isfinite(ts)
            tf = ts[finite]
            run.update(pos_key=best, pos_t=tf, pos_xy=xy[finite], pos_conv=conv, pos_n=len(ts),
                       pos_nan_t=int((~finite).sum()), pos_nonincreasing=int(np.sum(np.diff(tf) <= 0)),
                       pos_fs=1 / np.median(np.diff(tf)), pos_unit=_s(data.attrs.get("unit", "")),
                       pos_offset_start=float(tf[0] - start), pos_offset_stop=float(stop - tf[-1]))
        day["runs"].append(run)
    day["load_s"] = time.time() - t0
    f.close()
    return day


def load_all(assets, workers=12):
    with ThreadPoolExecutor(workers) as ex:
        days = list(ex.map(load_day, [r for _, r in assets.iterrows()]))
    return days


# --------------------------------------------------------------------------- clock checks

def statescript_to_nwb_clock(run):
    """Fit NWB time = a * StateScript time + b on rewarded entries matched to pump onsets.

    When the pump list has extra events, the run of pumps whose arms equal the logged
    rewarded arms is used. Returns (a, b, median and max abs residual in ms, n matched,
    unmatched pumps) or None when no such run exists.
    """
    tr = run["trials"]
    rew = tr[tr.rewarded & ~tr.lockout]
    rt, rarms = rew.t_ms.to_numpy() / 1000.0, rew.outer.to_numpy()
    pt, parms = run["dio_pump_t"], run["dio_pump_arms"]
    n, m = len(rt), len(pt)
    if n < 3 or m < n:
        return None
    for off in range(m - n + 1):
        if np.array_equal(parms[off:off + n], rarms):
            p = pt[off:off + n]
            a, b = np.polyfit(rt, p, 1)
            res = np.abs(p - (a * rt + b)) * 1000
            return a, b, float(np.median(res)), float(res.max()), n, m - n
    return None


def arm_from_position(run, shift_s=0.0):
    """Leave-one-out nearest-centroid decoding of the poked arm from the position at each
    outer-port entry (DIO beam breaks), with the position taken `shift_s` later.

    Returns the fraction decoded correctly and the number of entries; chance is about 1/8.
    """
    if "pos_t" not in run or len(run["dio_beam_t"]) < 16:
        return np.nan, 0
    t = run["dio_beam_t"] + shift_s
    order = np.argsort(run["pos_t"], kind="stable")
    pt = run["pos_t"][order]
    keep = (t >= pt[0]) & (t <= pt[-1])
    t, arms = t[keep], run["dio_beam_arms"][keep]
    idx = order[np.clip(np.searchsorted(pt, t), 0, len(pt) - 1)]
    xy = run["pos_xy"][idx]
    ok = np.all(np.isfinite(xy), axis=1) & np.any(xy != 0, axis=1)
    xy, arms = xy[ok], arms[ok]
    correct = 0
    for i in range(len(arms)):
        mask = np.ones(len(arms), bool)
        mask[i] = False
        cents = {a: xy[mask & (arms == a)].mean(axis=0) for a in np.unique(arms[mask])}
        guess = min(cents, key=lambda a: np.sum((xy[i] - cents[a]) ** 2))
        correct += guess == arms[i]
    return correct / max(len(arms), 1), len(arms)


def compare_with_draft(path, event="homebeam", series="series_1"):
    """Compare one file's DIO and position timestamps between the pinned version and the draft."""
    with DandiAPIClient() as client:
        urls = {v: client.get_dandiset(DANDISET_ID, v).get_asset_by_path(path)
                .get_content_url(follow_redirects=1, strip_query=True)
                for v in (DANDISET_VERSION, "draft")}
    out = {}
    files = {v: open_nwb(u) for v, u in urls.items()}
    for v, f in files.items():
        out[v] = {"nwb_version": _s(f.attrs["nwb_version"]),
                  "file_create_date": _s(f["file_create_date"][0]),
                  "dio_t": f[f"processing/behavior/behavioral_events/{event}/timestamps"][:],
                  "pos_t": f[f"processing/behavior/position/{series}/timestamps"][:]}
    a, b = (files[DANDISET_VERSION][f"processing/behavior/position/{series}/data"],
            files["draft"][f"processing/behavior/position/{series}/data"])
    out["pos_data_equal"] = bool(np.array_equal(a[:], b[:]))
    for f in files.values():
        f.close()
    return out


def time_raw_read(url, n_samples=300_000, start=10_000_000):
    """Seconds to stream n_samples x 128 channels of the raw broadband, and the bytes read."""
    f = open_nwb(url)
    d = f["acquisition/e-series/data"]
    t0 = time.time()
    x = d[start:start + n_samples, :]
    dt = time.time() - t0
    f.close()
    return dt, x.nbytes
