"""Loading and measures for dandiset 000971 (Seiler et al. 2022, Current Biology).

Seiler, Cosme, Sherathiya, Schaid, Bianco, Bridgemohan & Lerner (2022), "Dopamine signaling in the
dorsomedial striatum promotes compulsive behavior", doi:10.1016/j.cub.2022.01.055.

The dandiset holds one NWB file per operant session (MedPC events: nosepokes, rewards, port
entries, footshocks), dual-site fiber photometry for some RI60 and RR20 sessions, optogenetic
stimulus series, and western blot images. Files are streamed from the archive at the pinned version;
nothing is written to disk.

Where the parameters come from:

- Phenotype rule (STAR Methods, Behavioral Analysis): DPR when the late probe count rises by more
  than 85% over the early one; otherwise PR when the early count exceeds 13; otherwise PS.
- Early probe after 1 to 2 days of RI60, late probe after 13 to 14 days (Results). The early probe
  is the first probe day if fewer than 8 training sessions precede it; the late probe is the later
  probe day, after at least 8 training sessions, whose count of preceding sessions is closest to
  13.5 (choices here, as some mice have one or three probe days).
- Sessions last 60 min or until 50 rewards (Methods); omission completion time is the time to 50
  rewards (Methods), and 60 min when fewer were earned (a choice here).
- Photometry processing follows the authors' MATLAB code (IndividualPhotometryAnalysis.m, GitHub
  jillianseiler/Seiler-et-al.-2022-MATLAB-code at commit 56f1529): the first second dropped; a
  100-sample moving average applied with filtfilt; a least-squares fit of the 405 nm channel to the
  465 nm one; dF/F = (465 - fit) / fit; a z-score over the session; unrewarded nosepokes less those
  within 2 s of the previous one. The 0 to 1.5 s window for the maximum and minimum is from the
  Methods.
- Some recordings hold brief dropouts where a raw channel falls near zero; dF/F there reaches
  hundreds of standard deviations and dominates the session's z-score. Samples below half the
  channel median, and 1 s around them, are left out (a choice here; the Methods say only that
  recordings with excessive artifacts were excluded). The code's processing without this step is
  available with mask_dropouts=False.
- Rewarded port entry, extra nosepokes and the wait after reward (Figure 2K and 2L) are defined
  from the Results' wording; the code for them is not published.
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy.signal import filtfilt

DANDISET_ID = "000971"
DANDISET_VERSION = "0.261013.1707"
API = "https://api.dandiarchive.org/api"

PR_EARLY_THRESHOLD = 13      # shocks on the early probe (Methods: "more than 13")
DPR_CHANGE_THRESHOLD = 85.0  # percent rise from early to late probe (Methods: "greater than 85%")
LATE_PROBE_DAY = 13.5        # Results: late probe after 13 to 14 days of RI60
EARLY_LATE_SPLIT = 8         # a choice here: a probe after fewer training days is early, else late
SESSION_S = 3600.0           # Methods: one hour or 50 rewards
MAX_REWARDS = 50
SMOOTH_N = 100               # authors' code, filtfilt(ones(1,100)/100, 1, x)
DROP_FIRST_S = 1.0           # authors' code, "cut off 1st second"
BURST_S = 2.0                # authors' code, unrewarded nosepokes closer than 2 s dropped
PEAK_WINDOW_S = 1.5          # Methods, max and min in the 1.5 s after the event
PSTH_PRE_S, PSTH_POST_S = 2.0, 10.0  # window here (the code uses 10 s and 20 s)
PROLONGED_WINDOW = (2.0, 10.0)  # Results: DLS prolonged component, AUC 2 to 10 s after the nosepoke
DROPOUT_FRACTION = 0.5       # a choice here: raw samples below half the channel median are dropouts
DROPOUT_PAD_S = 1.0          # a choice here: and 1 s on each side of them is left out

STAGES = [("Footshock Probe", "shock"), ("Omission Probe", "omission"), ("RI60 Training", "RI60"),
          ("RI30 Training", "RI30"), ("RR20 Training", "RR20"), ("FR1 Habit", "FR1habit"),
          ("FR1 Training", "FR1"), ("Probe Test", "probetest"), ("RR5", "RR5"), ("Unknown", "unknown")]


def stage_of(description: str) -> str:
    for prefix, stage in STAGES:
        if description.startswith(prefix):
            return stage
    return "other"


def list_sessions() -> pd.DataFrame:
    """All assets of the pinned version with the session metadata the archive holds for them."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?metadata=true&page_size=1000"
    rows = []
    while url:
        page = requests.get(url, timeout=120).json()
        for a in page["results"]:
            m = a["metadata"]
            ses = [w for w in m.get("wasGeneratedBy", []) if w.get("schemaKey") == "Session"][0]
            part = m["wasAttributedTo"][0]
            rows.append({"path": a["path"], "asset_id": a["asset_id"], "size": a["size"],
                         "subject": part["identifier"], "sex": part.get("sex", {}).get("name", "")[:1],
                         "description": ses.get("description", ""), "start": ses.get("startDate", "")})
        url = page["next"]
    df = pd.DataFrame(rows)
    ses = df.path.str.split("_ses-").str[1]
    df["group"] = ses.str.extract(r"^(.*?)-\d{4}-\d\d-\d\dT")[0].fillna("western_blot")
    df["experiment"] = df.group.str.extract(r"^(FP|Opto-DLS-Excitatory|Opto-DMS-Excitatory|Opto-DMS-Inhibitory)")[0]
    df["arm"] = df.group.str.split("-").str[-1]
    df["stage"] = df.description.map(stage_of)
    side = df.description.str.extract(r"delivered on (left|right) nose pokes")[0]
    df["side"] = side
    df["date"] = df.start.str[:10]
    df["start_ts"] = pd.to_datetime(df.start.str[:19])
    return df


def _url(asset_id: str) -> str:
    return f"{API}/assets/{asset_id}/download/"


def _open(asset_id: str):
    return h5py.File(remfile.File(requests.head(_url(asset_id), allow_redirects=True, timeout=120).url), "r")


def _text(x) -> str:
    v = x[()]
    return v.decode() if isinstance(v, bytes) else str(v)


def read_events(asset_id: str) -> dict:
    """MedPC events and notes of one file. Port entries are taken from either form the file uses."""
    for attempt in range(4):
        try:
            with _open(asset_id) as f:
                out = {"asset_id": asset_id, "notes": _text(f["general/notes"]) if "general/notes" in f else ""}
                ev = {}
                if "processing/behavior" in f:
                    b = f["processing/behavior"]
                    out["module_description"] = str(b.attrs.get("description", ""))
                    for k in b:
                        if "timestamps" in b[k]:
                            ev[k] = b[k]["timestamps"][:]
                    if "behavioral_epochs/reward_port_intervals" in b:
                        g = b["behavioral_epochs/reward_port_intervals"]
                        ev["reward_port_entry_times"] = g["timestamps"][:][g["data"][:] == 1]
                out["events"] = ev
                out["has_photometry"] = "acquisition/fiber_photometry_response_series" in f
                return out
        except OSError:
            if attempt == 3:
                raise
    raise RuntimeError(asset_id)


def read_all_events(asset_ids, threads: int = 32) -> dict:
    with ThreadPoolExecutor(threads) as ex:
        return dict(zip(asset_ids, ex.map(read_events, asset_ids)))


def note_field(notes: str, field: str):
    m = re.search(field + r": (.*)", notes or "")
    return m.group(1).strip() if m else None


def rewards(ev: dict) -> np.ndarray:
    parts = [ev[k] for k in ("left_reward_times", "right_reward_times") if k in ev]
    return np.sort(np.concatenate(parts)) if parts else np.array([])


def active_pokes(ev: dict, side: str) -> np.ndarray:
    return np.sort(ev.get(f"{side}_nose_poke_times", np.array([])))


def session_length(ev: dict) -> float:
    r = rewards(ev)
    return float(r[MAX_REWARDS - 1]) if len(r) >= MAX_REWARDS else SESSION_S


def omission_time_min(ev: dict) -> float:
    """Time to the 50th reward, or 60 min when fewer were earned."""
    r = rewards(ev)
    return (float(r[MAX_REWARDS - 1]) if len(r) >= MAX_REWARDS else SESSION_S) / 60.0


def reward_measures(ev: dict, side: str) -> dict:
    """Wait after the rewarded port entry, extra nosepokes before it, and inter-reward intervals."""
    r, pokes = rewards(ev), active_pokes(ev, side)
    ports = np.sort(ev.get("reward_port_entry_times", np.array([])))
    waits, extras = [], []
    for i, t in enumerate(r):
        nxt = r[i + 1] if i + 1 < len(r) else np.inf
        pe = ports[(ports > t) & (ports < nxt)]
        if len(pe) == 0:
            continue
        extras.append(int(((pokes > t) & (pokes < pe[0])).sum()))
        after = pokes[pokes > pe[0]]
        if len(after):
            waits.append(float(after[0] - pe[0]))
    return {"wait": np.mean(waits) if waits else np.nan, "extra": np.mean(extras) if extras else np.nan,
            "n_waits": len(waits), "iri": np.diff(r), "has_ports": len(ports) > 0}


def classify(early: float, late: float) -> str:
    """Methods rule: DPR when the rise exceeds 85%, otherwise PR when early > 13, otherwise PS."""
    if early > 0 and 100.0 * (late - early) / early > DPR_CHANGE_THRESHOLD:
        return "DPR"
    if early == 0 and late > 0:
        return "DPR"
    return "PR" if early > PR_EARLY_THRESHOLD else "PS"


def probe_table(sessions: pd.DataFrame, events: dict, training_stages=("RI60", "RR20")) -> pd.DataFrame:
    """One row per mouse and probe day: shock count (last file of the day with footshock_times, and
    the sum over the day's files), the number of training sessions before it, and early/late."""
    rows = []
    for subj, s in sessions.sort_values("start_ts").groupby("subject"):
        train_dates = s[s.stage.isin(training_stages)].date.tolist()
        for date, d in s[s.stage == "shock"].groupby("date"):
            counts = [len(events[a]["events"]["footshock_times"]) for a in d.asset_id
                      if "footshock_times" in events[a]["events"]]
            rows.append({"subject": subj, "date": date, "n_files": len(d), "n_with_shocks": len(counts),
                         "shocks": counts[-1] if counts else np.nan, "shocks_sum": sum(counts) if counts else np.nan,
                         "train_days_before": sum(t < date for t in train_dates)})
    p = pd.DataFrame(rows)
    p = p[p.n_with_shocks > 0].copy()
    p["probe"] = ""
    for subj, d in p.groupby("subject"):
        d = d.sort_values("date")
        if d.train_days_before.iloc[0] < EARLY_LATE_SPLIT:
            p.loc[d.index[0], "probe"] = "early"
            d = d.iloc[1:]
        later = d[d.train_days_before >= EARLY_LATE_SPLIT]
        if len(later):
            p.loc[(later.train_days_before - LATE_PROBE_DAY).abs().idxmin(), "probe"] = "late"
    return p


def early_late(probes: pd.DataFrame, value: str = "shocks") -> pd.DataFrame:
    w = probes[probes.probe != ""].pivot(index="subject", columns="probe", values=value)
    return w.reindex(columns=["early", "late"])


# ---------------------------------------------------------------- photometry

def load_photometry(asset_id: str) -> dict:
    """The four photometry columns (DMS 465, DMS 405, DLS 465, DLS 405), the rate, and events."""
    for attempt in range(4):
        try:
            with _open(asset_id) as f:
                s = f["acquisition/fiber_photometry_response_series"]
                data = s["data"][:]
                fs = float(s["starting_time"].attrs["rate"])
                t0 = float(s["starting_time"][()])
                b = f["processing/behavior"]
                ev = {k: b[k]["timestamps"][:] for k in b if "timestamps" in b[k]}
                table = f["general/fiber_photometry/fiber_photometry_table"]
                locations = [x.decode() for x in table["location"][:]]
                sources = [f[r].name.split("/")[-1] for r in table["excitation_source"][:]]
                freqs = {k: float(f[f"acquisition/{k}/frequency"][()]) for k in f["acquisition"]
                         if k.startswith("commanded_voltage_series") and "frequency" in f[f"acquisition/{k}"]}
                return {"data": data, "fs": fs, "t0": t0, "events": ev, "locations": locations,
                        "sources": sources, "coordinates": table["coordinates"][:], "modulation_hz": freqs}
        except OSError:
            if attempt == 3:
                raise
    raise RuntimeError(asset_id)


def dropout_mask(signal: np.ndarray, control: np.ndarray, fs: float) -> np.ndarray:
    """Samples near a dropout: either channel below DROPOUT_FRACTION of its median, widened by
    DROPOUT_PAD_S on each side. A choice here; the authors' code has no such step."""
    bad = (signal < DROPOUT_FRACTION * np.median(signal)) | (control < DROPOUT_FRACTION * np.median(control))
    if not bad.any():
        return bad
    pad = int(round(DROPOUT_PAD_S * fs))
    return np.convolve(bad.astype(float), np.ones(2 * pad + 1), mode="same") > 0


def zscored_dff(signal: np.ndarray, control: np.ndarray, fs: float, mask_dropouts: bool = True) -> np.ndarray:
    """As IndividualPhotometryAnalysis.m: smooth, fit control to signal, dF/F, z-score.
    The first second is set to NaN (the code removes it). With mask_dropouts, samples near a dropout
    are left out of the fit and the z-score and set to NaN."""
    k = np.ones(SMOOTH_N) / SMOOTH_N
    n0 = int(np.ceil(DROP_FIRST_S * fs))
    raw_s, raw_c = signal[n0:].astype(float), control[n0:].astype(float)
    sig = filtfilt(k, 1, raw_s)
    ctl = filtfilt(k, 1, raw_c)
    bad = dropout_mask(raw_s, raw_c, fs) if mask_dropouts else np.zeros(len(sig), bool)
    a, b = np.polyfit(ctl[~bad], sig[~bad], 1)
    fit = a * ctl + b
    dff = 100.0 * (sig - fit) / fit
    dff[bad] = np.nan
    z = (dff - np.nanmean(dff)) / np.nanstd(dff, ddof=1)
    return np.concatenate([np.full(n0, np.nan), z])


def psth(z: np.ndarray, fs: float, times: np.ndarray, t0: float = 0.0,
         pre: float = PSTH_PRE_S, post: float = PSTH_POST_S) -> tuple[np.ndarray, np.ndarray]:
    """Mean trace around events; events whose window leaves the recording are dropped."""
    win = np.arange(-int(round(pre * fs)), int(round(post * fs)) + 1)
    idx = np.round((np.asarray(times) - t0) * fs).astype(int)
    idx = idx[(idx + win[0] >= 0) & (idx + win[-1] < len(z))]
    if len(idx) == 0:
        return win / fs, np.full(len(win), np.nan)
    return win / fs, np.nanmean(z[idx[:, None] + win], axis=0)


def drop_bursts(times: np.ndarray, gap: float = BURST_S) -> np.ndarray:
    """As the authors' code: drop an event within `gap` s of the previous one (first and last kept)."""
    times = np.sort(times)
    keep = np.ones(len(times), bool)
    for i in range(1, len(times) - 1):
        if times[i] - times[i - 1] < gap:
            keep[i] = False
    return times[keep]


def split_nosepokes(ev: dict, side: str) -> tuple[np.ndarray, np.ndarray]:
    """Rewarded and unrewarded active nosepokes (unrewarded after dropping bursts)."""
    pokes = active_pokes(ev, side)
    rew = rewards(ev)
    rewarded = pokes[np.isin(np.round(pokes, 3), np.round(rew, 3))]
    unrewarded = pokes[~np.isin(np.round(pokes, 3), np.round(rew, 3))]
    return rewarded, drop_bursts(unrewarded)


def peak_score(z: np.ndarray, fs: float, rewarded: np.ndarray, unrewarded: np.ndarray, t0: float = 0.0,
               window: float = PEAK_WINDOW_S) -> dict:
    t, pr = psth(z, fs, rewarded, t0)
    _, pu = psth(z, fs, unrewarded, t0)
    m = (t >= 0) & (t <= window)
    late = (t >= PROLONGED_WINDOW[0]) & (t <= PROLONGED_WINDOW[1])
    auc = np.trapezoid(pr[late], t[late]) if np.isfinite(pr[late]).all() else np.nan
    return {"score": np.nanmax(pr[m]) - np.nanmin(pu[m]), "rew_max": np.nanmax(pr[m]), "unrew_min": np.nanmin(pu[m]),
            "auc_2_10": auc, "t": t, "psth_rew": pr, "psth_unrew": pu}
