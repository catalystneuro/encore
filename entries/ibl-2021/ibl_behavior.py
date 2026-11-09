"""Loading and measures for the IBL behavioural dandiset (DANDI:000045).

Used by reproduce_ibl_2021.ipynb, which tests the claims of The International
Brain Laboratory (2021), eLife 10:e63711, against the claims file
claims/000045/10.7554-elife.63711.yaml. Other notebooks on this dandiset can
import the loader.

Every NWB file holds one session: a trials table, the session's metadata
(protocol, lab, project, start time) and the rig's settings as JSON. The files
are streamed from the archive with remfile and read with h5py; only the trial
columns and metadata the analysis uses are read.

Where parameters come from:
- Trial coding, psychometric fit, proficiency criteria, session windows, lab
  tests and the lab classifier follow the shared definitions in the claims
  file's header (which cite the paper's Methods, Appendix 1 and the code
  github.com/int-brain-lab/paper-behavior at commit edc4531).
- The number of parallel downloads, retries and the order of reading are
  standard choices that cannot change a result.
"""

from __future__ import annotations

import json
import time
import urllib.request
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import optimize, special

DANDISET_ID = "000045"
DANDISET_VERSION = "0.211209.1413"
API = "https://api.dandiarchive.org/api"

# Claims file header: project and cutoff date of the paper's selection
# (code query_subjects, CUTOFF_DATE) and the one session the code excludes.
PROJECT = "ibl_neuropixel_brainwide_01"
CUTOFF_DATE = "2020-03-23"
EXCLUDED_SESSION = "a9fb578a-9d7d-42b4-8dbc-3b419ce9f424"

# Claims file header: the code's lab numbers, by institution.
LAB_NUMBER = {
    "University College London": "Lab 1",
    "Champalimaud Centre for the Unknown": "Lab 2",
    "Cold Spring Harbor Laboratory": "Lab 3",
    "New York University": "Lab 4",
    "Princeton University": "Lab 5",
    "Sainsbury-Wellcome Centre": "Lab 6",
    "University of California, Berkeley": "Lab 7",
}
# Claims file header: the code's time zones (hours) by lab, for the positive control.
TIME_ZONE = {"Lab 1": 0, "Lab 2": 0, "Lab 3": -5, "Lab 4": -5, "Lab 5": -5,
             "Lab 6": 0, "Lab 7": -7}

TRIAL_COLUMNS = ["choice", "contrastLeft", "contrastRight", "feedbackType",
                 "probabilityLeft", "stimOn_times", "response_times",
                 "feedback_times", "goCue_times", "start_time", "stop_time",
                 "included", "rewardVolume"]


def list_assets(version: str = DANDISET_VERSION) -> pd.DataFrame:
    """All assets of the pinned version, from the DANDI REST API."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000"
    rows = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        rows += page["results"]
        url = page["next"]
    df = pd.DataFrame(rows)
    df["subject_dir"] = df.path.str.split("/").str[0].str.replace("sub-", "", regex=False)
    df["session_id"] = df.path.str.extract(r"_ses-([0-9a-f-]{36})")[0]
    df["suffix"] = df.path.str.extract(r"ses-[0-9a-f-]{36}_?([^/]*)\.nwb$")[0]
    return df


def version_metadata(version: str = DANDISET_VERSION) -> dict:
    with urllib.request.urlopen(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/") as r:
        return json.load(r)


def _str(v):
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray):
        return [_str(x) for x in v]
    return v


def read_session(asset_id: str, retries: int = 4) -> dict:
    """Stream one file and return its session metadata and trial columns."""
    url = f"{API}/assets/{asset_id}/download/"
    for attempt in range(retries):
        try:
            with h5py.File(remfile.File(url), "r") as f:
                g = f["general"]
                sub = g["subject"]
                isd = g["Ibl_session_data"]
                settings = json.loads(_str(isd["json"][()]) or "{}") or {}
                out = {
                    "asset_id": asset_id,
                    "session_id": _str(g["session_id"][()]),
                    "subject_id": _str(sub["subject_id"][()]),
                    "nickname": _str(sub["nickname"][()]),
                    "sex": _str(sub["sex"][()]),
                    "institution": _str(g["institution"][()]),
                    "lab": _str(g["lab"][()]),
                    "subject_projects": _str(sub["projects"][()]) if "projects" in sub else None,
                    "project": _str(isd["project"][()]),
                    "protocol": _str(g["protocol"][()]),
                    "start": _str(f["session_start_time"][()]),
                    "end": _str(isd["end_time"][()]),
                    "number": int(isd["number"][()]),
                    "date_of_birth": _str(sub["date_of_birth"][()]),
                    "disengaged": settings.get("SUBJECT_DISENGAGED_TRIGGERED"),
                    "disengaged_trial": settings.get("SUBJECT_DISENGAGED_TRIALNUM"),
                    "auto_stop": settings.get("USE_AUTOMATIC_STOPPING_CRITERIONS"),
                    "settings_protocol": settings.get("_PROTOCOL") or settings.get("PYBPOD_PROTOCOL"),
                }
                wpath = "processing/behavior/BehavioralTimeSeries/position"
                if wpath in f:
                    out["wheel_n"] = f[wpath]["data"].shape[0]
                    out["wheel_ts_n"] = f[wpath]["timestamps"].shape[0]
                else:
                    out["wheel_n"] = out["wheel_ts_n"] = None
                t = f["intervals"]["trials"] if "trials" in f.get("intervals", {}) else None
                for c in TRIAL_COLUMNS:
                    out[c] = t[c][:] if (t is not None and c in t) else None
                return out
        except Exception as e:  # network errors: retry, then report
            err = repr(e)
            time.sleep(2 * (attempt + 1))
    return {"asset_id": asset_id, "error": err}


def read_all(asset_ids, workers: int = 32) -> list[dict]:
    """Read many files in parallel. Processes, not threads: h5py holds a
    global lock, so threads read one file at a time."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(read_session, asset_ids, chunksize=4))


def trials_frame(sessions: list[dict]) -> pd.DataFrame:
    """One row per trial, with the session id."""
    parts = []
    for s in sessions:
        if s.get("choice") is None:
            continue
        d = pd.DataFrame({c: s[c] for c in TRIAL_COLUMNS if s.get(c) is not None})
        d["session_id"] = s["session_id"]
        parts.append(d)
    t = pd.concat(parts, ignore_index=True)
    # Trial coding (claims file header, code dj2pandas): signed contrast in %,
    # right minus left; a no-response trial (choice 0) is incorrect and is left
    # out of the fraction of rightward choices.
    cl = t.contrastLeft.fillna(0)
    cr = t.contrastRight.fillna(0)
    t["signed_contrast"] = np.round((cr - cl) * 100, 2)
    t["abs_contrast"] = t.signed_contrast.abs()
    t["correct"] = (t.feedbackType == 1).astype(float)
    # choice: -1 CCW, +1 CW. In the IBL convention CCW (-1) moves the stimulus
    # to the right, i.e. a rightward choice is choice == -1 (code dj2pandas:
    # choice_right = trial_response_choice == 'CCW'); checked against feedback
    # in the notebook.
    t["choice_right"] = np.where(t.choice == 0, np.nan, (t.choice == -1).astype(float))
    t["rt"] = np.where(t.choice == 0, np.nan, t.response_times - t.stimOn_times)
    return t




# ---------------------------------------------------------------------------
# Session table and training days

# The dataset's institution strings, mapped to the code's lab numbers (claims
# file header). The notebook checks that these are the seven labs.
INSTITUTION_LAB = {
    "University College London": "Lab 1",
    "Champalimaud Centre for the Unknown": "Lab 2",
    "Cold Spring Harbor Laboratory": "Lab 3",
    "New York University / Center for Neural Science": "Lab 4",
    "Princeton": "Lab 5",
    "Sainsbury Wellcome Centre": "Lab 6",
    "University of California Berkeley": "Lab 7",
}
LABS = [f"Lab {i}" for i in range(1, 8)]


def task_of(protocol: str) -> str:
    """'training' (basic task), 'biased' (full task), 'ephys' (full task on the
    recording rig) or 'other' (opto and reward-manipulation variants)."""
    p = protocol or ""
    if "trainingChoiceWorld" in p:
        return "training"
    if "ephysChoiceWorld" in p:
        return "ephys"
    if "biasedChoiceWorld" in p and "RPE" not in p:
        return "biased"
    return "other"


def session_table(sessions: list[dict]) -> pd.DataFrame:
    rows = []
    for s in sessions:
        r = {k: v for k, v in s.items() if k not in TRIAL_COLUMNS}
        r["n_trials"] = 0 if s.get("choice") is None else len(s["choice"])
        rows.append(r)
    S = pd.DataFrame(rows)
    S["date"] = S.start.str[:10]
    S["task"] = S.protocol.map(task_of)
    S["lab_number"] = S.institution.map(INSTITUTION_LAB)
    end = pd.to_datetime(S.end.where(S.end.str.match(r"\d{4}-", na=False)).str[:19], format="%Y-%m-%dT%H:%M:%S")
    S["duration_min"] = (end - pd.to_datetime(S.start.str[:19], format="%Y-%m-%dT%H:%M:%S")).dt.total_seconds() / 60
    return S


def project_mice(S: pd.DataFrame) -> pd.Index:
    """Mice of the paper's project (claims file header): the subject's projects
    include it; for a subject with no projects field, its sessions' project."""
    def has(l):
        return isinstance(l, list) and PROJECT in l
    by_sub = S.groupby("subject_id").subject_projects.agg(lambda x: any(has(l) for l in x))
    no_field = S.groupby("subject_id").subject_projects.agg(lambda x: all(not isinstance(l, list) for l in x))
    by_ses = S.groupby("subject_id").project.agg(lambda x: (x == PROJECT).any())
    keep = by_sub | (no_field & by_ses)
    return keep[keep].index


def daily(T: pd.DataFrame, S: pd.DataFrame, tasks=None) -> pd.DataFrame:
    """One row per mouse and training day (date), from the trials of sessions
    of the given tasks (all sessions with trials when None).

    Columns: n_trials, perf_easy (% correct, contrast >= 50%), perf_100,
    contrasts (set of absolute contrasts), n_signed (number of signed
    contrasts), tasks, basic_only (every session of the day is a basic-task
    session; probabilityLeft cannot mark 50:50 days, as it varies from trial
    to trial in basic-task sessions), tday0 (0-based day index over all days the
    mouse has a session with trials, so that indices are comparable across
    task selections)."""
    ses = S[S.n_trials > 0]
    allday = ses.groupby(["subject_id", "date"]).size().reset_index()[["subject_id", "date"]]
    allday = allday.sort_values(["subject_id", "date"])
    allday["tday0"] = allday.groupby("subject_id").cumcount()
    sel = ses if tasks is None else ses[ses.task.isin(tasks)]
    t = T.merge(sel[["session_id", "subject_id", "date", "task"]], on="session_id")
    g = t.groupby(["subject_id", "date"])
    D = pd.DataFrame({
        "n_trials": g.size(),
        "perf_easy": g.apply(lambda d: perf_easy(d), include_groups=False),
        "perf_100": g.apply(lambda d: 100 * d.correct[d.abs_contrast == 100].mean()
                            if (d.abs_contrast == 100).any() else np.nan, include_groups=False),
        "contrasts": g.abs_contrast.agg(lambda x: frozenset(x.unique())),
        "n_signed": g.signed_contrast.nunique(),
        "tasks": g.task.agg(lambda x: frozenset(x.unique())),
    }).reset_index()
    D["basic_only"] = D.tasks.apply(lambda x: x == frozenset(["training"]))
    D = D.merge(allday, on=["subject_id", "date"])
    return D.sort_values(["subject_id", "tday0"]).reset_index(drop=True)


def perf_easy(df: pd.DataFrame) -> float:
    """% correct on trials with contrast of 50% or more (claims file header;
    no-response trials count as incorrect)."""
    e = df[df.abs_contrast >= 50]
    return 100 * e.correct.mean() if len(e) else np.nan


# ---------------------------------------------------------------------------
# Psychometric fit (claims file header; code fit_psychfunc with psychofit)

def fit_psychfunc(contrast, choice_right, seed: int = 0) -> dict:
    """Fit of P = gamma + (1 - gamma - lambda) (erf((c - mu)/sigma) + 1)/2 by
    maximum likelihood with psychofit.mle_fit_psycho (the paper's fitting
    routine; 'erf_psycho_2gammas', its default number of fits).

    Start [0, 20, 0.05, 0.05]; bounds mu in [min, max] signed contrast, sigma
    in [5, 40], lapses in [0, 1]; NaN with fewer than four signed contrasts
    (claims file header). psychofit draws its random restarts from numpy's
    global generator; it is seeded before every fit so that each fit is
    reproducible on its own (the seed is a standard choice)."""
    import psychofit
    c = np.asarray(contrast, float)
    y = np.asarray(choice_right, float)
    ok = ~np.isnan(y)
    c, y = c[ok], y[ok]
    levels = np.unique(c)
    nan = dict(bias=np.nan, threshold=np.nan, lapselow=np.nan, lapsehigh=np.nan)
    if len(levels) < 4:
        return nan
    n = np.array([np.sum(c == x) for x in levels], float)
    p = np.array([y[c == x].mean() for x in levels])
    np.random.seed(seed)
    pars, _ = psychofit.mle_fit_psycho(
        np.vstack([levels, n, p]), P_model="erf_psycho_2gammas",
        parstart=np.array([0.0, 20.0, 0.05, 0.05]),
        parmin=np.array([levels.min(), 5.0, 0.0, 0.0]),
        parmax=np.array([levels.max(), 40.0, 1.0, 1.0]))
    return dict(bias=pars[0], threshold=pars[1], lapselow=pars[2], lapsehigh=pars[3])


def _fit_one(args):
    return fit_psychfunc(*args)


_POOLS: dict = {}


def fit_many(pairs, workers: int = 4) -> list[dict]:
    """Fit many (contrast, choice_right) pairs in parallel processes. The
    pool is kept between calls, as starting one costs more than many fits."""
    if workers not in _POOLS:
        _POOLS[workers] = ProcessPoolExecutor(workers)
    return list(_POOLS[workers].map(_fit_one, pairs, chunksize=16))


def psychometric_value(pars: dict, c: float) -> float:
    """Fitted probability of a rightward choice at signed contrast c."""
    return float(gamma_curve(pars, c))


def gamma_curve(pars, c):
    return pars["lapselow"] + (1 - pars["lapselow"] - pars["lapsehigh"]) * (
        special.erf((c - pars["bias"]) / pars["threshold"]) + 1) / 2


# ---------------------------------------------------------------------------
# Proficiency (Appendix 1, table 1d, as the claims file cites it)

# Table 1d, 'Trained 1a/1b': each of the last three sessions > 200/400 trials
# and > 80/90% correct, all contrasts introduced; the three combined: |bias|
# < 16/10, threshold < 19/20, lapse rates < 0.2/0.1; 1b only: median reaction
# time at 0% contrast < 2 s. Claims file header, P1 (answers of 2026-10-22):
# the status is recomputed as the pipeline's SessionTrainingStatus computes it,
# at each session from that session and the two before it (any protocol);
# trials completed are all trials; percent correct is over contrasts of 50% or
# more (compute_performance_easy). The table's 100% contrast is run as a
# sensitivity (perf="100").
CRIT_1A = dict(n=200, perf=80, bias=16, thr=19, lapse=0.2, rt=None)
CRIT_1B = dict(n=400, perf=90, bias=10, thr=20, lapse=0.1, rt=2.0)
# Claims file header, P1: the 1b implementation date in the code
# (text_trained1a_to_1b_sessions.py, DATE_IMPL), used by the variant in which
# 1b replaces 1a from that day.
DATE_1B = "2019-09-12"
# "All contrasts introduced" (claims file header, P1): main reading 'each',
# each of the three sessions presents the final set of Appendix 1, table 1c
# (100, 25, 12.5, 6.25, 0); variant 'last', the pipeline's check, the current
# session presents 0% and a contrast between 0.1 and 6.5%.
ALL_CONTRASTS = frozenset([0.0, 6.25, 12.5, 25.0, 100.0])


def _contrasts_ok(sets, contrasts):
    if contrasts == "each":
        return all(ALL_CONTRASTS <= c for c in sets)
    last = sets[-1]
    return 0.0 in last and any(0.1 < c < 6.5 for c in last)


def _windows(D):
    """For each mouse, consecutive triples of rows of D (training days)."""
    for sid, d in D.groupby("subject_id", sort=False):
        d = d.sort_values("tday0")
        idx = d.index.to_numpy()
        for j in range(2, len(idx)):
            yield sid, idx[j - 2: j + 1]


_WINDOW_FITS: dict = {}


def session_summary(T: pd.DataFrame, S: pd.DataFrame) -> pd.DataFrame:
    """One row per session with trials, in order of start time per mouse:
    n_trials (all trials), perf_easy, perf_100, the set of absolute contrasts,
    and the median reaction time at 0% contrast."""
    ses = S[S.n_trials > 0][["session_id", "subject_id", "date", "start", "task"]]
    t = T[T.session_id.isin(ses.session_id)]
    g = t.groupby("session_id")
    e = t[t.abs_contrast >= 50].groupby("session_id").correct.mean() * 100
    h = t[t.abs_contrast == 100].groupby("session_id").correct.mean() * 100
    z = t[t.signed_contrast == 0].groupby("session_id").rt.median()
    out = ses.set_index("session_id").assign(
        n_trials=g.size(), perf_easy=e, perf_100=h,
        contrasts=g.abs_contrast.agg(lambda x: frozenset(x.unique())), rt0=z)
    return out.reset_index().sort_values(["subject_id", "start"]).reset_index(drop=True)


def training_status(SS: pd.DataFrame, T: pd.DataFrame, contrasts: str = "each",
                    replace_from: str | None = None, perf: str = "easy",
                    nan_rt_passes: bool = False) -> pd.DataFrame:
    """Per mouse, the first session of trained_1a or trained_1b status (P1) and
    the first session meeting the 1b criteria, recomputed from the trials.

    SS: session_summary(). At each session the window is that session and the
    two before it (any protocol); the 1b criteria are tested and then the 1a
    criteria, at any date (main reading). replace_from: a date from which only
    the 1b criteria apply, and before which only the 1a criteria (variant).
    contrasts: 'each' or 'last' (see ALL_CONTRASTS). The fits of the windows
    that pass the per-session criteria are run in parallel and kept across
    calls. nan_rt_passes: a window whose median reaction time at 0% contrast
    is undefined (no 0% trial with both a stimulus onset time and a response)
    passes the 1b reaction-time criterion; a sensitivity, as the table gives no
    rule for it. Columns: p1_session, p1_date, p1_status, b1_session, b1_date,
    and n_rt_nan_1b, the windows evaluated that meet every 1b criterion but the
    reaction time, which is undefined; attrs["rt_nan_windows"] is their total
    over all mice, with or without P1."""
    pcol = "perf_easy" if perf == "easy" else "perf_100"
    cand = []   # (subject, window session ids, criteria names, last date)
    for sid, d in SS.groupby("subject_id", sort=False):
        n = d.n_trials.to_numpy()
        p = d[pcol].to_numpy()
        cs = d.contrasts.to_list()
        ids = d.session_id.to_list()
        dates = d.date.to_list()
        for j in range(2, len(d)):
            w = slice(j - 2, j + 1)
            if not _contrasts_ok(cs[w], contrasts):
                continue
            names = []
            for name, crit in (("1b", CRIT_1B), ("1a", CRIT_1A)):
                if replace_from is not None and (name == "1b") != (dates[j] >= replace_from):
                    continue
                if (n[w] > crit["n"]).all() and (np.nan_to_num(p[w]) > crit["perf"]).all():
                    names.append(name)
            if names:
                cand.append((sid, tuple(ids[w]), names, dates[j], j))
    by_mouse: dict = {}
    for c in cand:
        by_mouse.setdefault(c[0], []).append(c)
    by_ses = {k: v for k, v in T[T.session_id.isin({x for c in cand for x in c[1]})]
              .groupby("session_id")[["signed_contrast", "choice_right", "rt"]]}

    def fit_windows(ws):
        ws = [w for w in dict.fromkeys(ws) if w not in _WINDOW_FITS]
        tts = [pd.concat([by_ses[x] for x in w]) for w in ws]
        for w, tt, f in zip(ws, tts, fit_many([(tt.signed_contrast.to_numpy(), tt.choice_right.to_numpy())
                                               for tt in tts])):
            f["rt0"] = float(np.nanmedian(tt.rt[tt.signed_contrast == 0])) \
                if (tt.signed_contrast == 0).any() else np.nan
            _WINDOW_FITS[w] = f

    # Windows are evaluated in order, a few per mouse at a time, until the mouse
    # has both its first 1a-or-1b session and its first 1b session; later
    # windows cannot change either and are not fitted.
    out = {sid: {"n_rt_nan_1b": 0} for sid in by_mouse}
    pos = dict.fromkeys(by_mouse, 0)
    chunk = 15
    while True:
        live = [s for s in by_mouse if pos[s] < len(by_mouse[s]) and "b1_session" not in out[s]]
        if not live:
            break
        fit_windows([c[1] for s in live for c in by_mouse[s][pos[s]: pos[s] + chunk]])
        for s in live:
            r = out[s]
            for sid, w, names, date, j in by_mouse[s][pos[s]: pos[s] + chunk]:
                if "b1_session" in r:
                    break
                f = _WINDOW_FITS[w]
                for name in names:
                    crit = CRIT_1B if name == "1b" else CRIT_1A
                    ok = (abs(f["bias"]) < crit["bias"] and f["threshold"] < crit["thr"]
                          and f["lapselow"] < crit["lapse"] and f["lapsehigh"] < crit["lapse"])
                    if crit["rt"] is not None:
                        if ok and np.isnan(f["rt0"]):
                            r["n_rt_nan_1b"] += 1
                        ok = ok and (f["rt0"] < crit["rt"] or (nan_rt_passes and np.isnan(f["rt0"])))
                    if not ok:
                        continue
                    if "p1_session" not in r:
                        r.update(p1_session=w[-1], p1_date=date, p1_status=name,
                                 **{f"p1_{k}": v for k, v in f.items()})
                    if name == "1b":
                        r.update(b1_session=w[-1], b1_date=date)
                    break
            pos[s] += chunk
    n_nan = sum(v["n_rt_nan_1b"] for v in out.values())
    out = {k: v for k, v in out.items() if "p1_session" in v}
    df = pd.DataFrame.from_dict(out, orient="index")
    df.attrs["rt_nan_windows"] = n_nan
    return df


def full_proficiency(Dfull: pd.DataFrame, T: pd.DataFrame, S: pd.DataFrame,
                     nan_rt_passes: bool = False) -> pd.DataFrame:
    """P2 per mouse (Appendix 1, table 1d, 'Full task proficiency'): each of
    three consecutive full-task days > 400 trials and > 90% correct on 100%
    contrast; the three combined: all four lapse rates (left and right, 20:80
    and 80:20 blocks) < 0.1, bias[80:20] - bias[20:80] > 5, median reaction
    time at 0% contrast < 2 s. Dfull is daily() over biased-protocol sessions.
    nan_rt_passes: as in training_status. attrs["rt_nan_windows"] counts the
    windows evaluated (up to each mouse's P2) that meet every criterion but
    the reaction time, which is undefined."""
    ses = S[S.task == "biased"][["session_id", "subject_id", "date"]]
    t = T.merge(ses, on="session_id")
    tg = {k: v for k, v in t.groupby(["subject_id", "date"])}
    cand, pairs = [], []
    for sid, w in _windows(Dfull):
        d = Dfull.loc[w]
        if not ((d.n_trials > 400).all() and (d.perf_100 > 90).all()):
            continue
        tt = pd.concat([tg[(sid, x)] for x in d.date])
        cand.append((sid, d, tt))
        for pl in (0.2, 0.8):
            b = tt[np.isclose(tt.probabilityLeft, pl)]
            pairs.append((b.signed_contrast.to_numpy(), b.choice_right.to_numpy()))
    fits = fit_many(pairs)
    out, n_nan = {}, 0
    for k, (sid, d, tt) in enumerate(cand):
        if sid in out:
            continue
        f2080, f8020 = fits[2 * k], fits[2 * k + 1]
        lapses = [f[l] for f in (f2080, f8020) for l in ("lapselow", "lapsehigh")]
        ok = np.all(np.array(lapses) < 0.1) and f8020["bias"] - f2080["bias"] > 5
        rt0 = tt.rt[tt.signed_contrast == 0]
        rt0 = float(np.nanmedian(rt0)) if rt0.notna().any() else np.nan
        if ok and np.isnan(rt0):
            n_nan += 1
        ok = ok and (rt0 < 2.0 or (nan_rt_passes and np.isnan(rt0)))
        if ok:
            out[sid] = dict(p2_date=d.date.iloc[-1], p2_tday0=int(d.tday0.iloc[-1]))
    df = pd.DataFrame.from_dict(out, orient="index")
    df.attrs["rt_nan_windows"] = n_nan
    return df


# ---------------------------------------------------------------------------
# Lab tests (claims file header, 'Lab test')

def lab_test(values: pd.Series, labs: pd.Series, test: str = "kruskal") -> float:
    """p of a test across labs: 'kruskal', 'anova' (one-way), 'levene'
    (scipy default, median-centred) or 'code' (normaltest over all mice,
    Kruskal-Wallis when p < 0.05, one-way ANOVA otherwise)."""
    from scipy import stats
    ok = values.notna()
    groups = [values[ok & (labs == l)].to_numpy() for l in sorted(labs[ok].unique())]
    if test == "code":
        test = "kruskal" if stats.normaltest(values[ok]).pvalue < 0.05 else "anova"
    if test == "kruskal":
        return stats.kruskal(*groups).pvalue
    if test == "anova":
        return stats.f_oneway(*groups).pvalue
    if test == "levene":
        return stats.levene(*groups).pvalue
    raise ValueError(test)


def fdr(p):
    """Benjamini-Hochberg corrected p values."""
    from statsmodels.stats.multitest import multipletests
    return multipletests(np.asarray(p, float), method="fdr_bh")[1]


# ---------------------------------------------------------------------------
# Lab classifier (claims file header, 'Lab classifier'; Methods)

def loo_gaussian_nb(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Leave-one-out predictions of scikit-learn's GaussianNB with default
    settings (var_smoothing 1e-9 of the largest feature variance of the
    training set; priors from class frequencies; variances with ddof 0),
    computed directly for every fold at once so that 2000 subsamples run in
    seconds. The notebook checks it against scikit-learn."""
    X = np.asarray(X, float)
    n = len(y)
    classes = np.unique(y)
    keep = ~np.eye(n, dtype=bool)
    Xtr = np.stack([X[keep[i]] for i in range(n)])                      # (n, n-1, p)
    ytr = np.stack([y[keep[i]] for i in range(n)])
    eps = 1e-9 * Xtr.var(axis=1).max(axis=1)                            # (n,)
    ll = np.full((n, len(classes)), -np.inf)
    for k, c in enumerate(classes):
        m = (ytr == c)[..., None]                                       # (n, n-1, 1)
        cnt = m.sum(1)                                                  # (n, 1)
        ok = cnt[:, 0] > 0
        mu = (Xtr * m).sum(1) / np.maximum(cnt, 1)
        var = (((Xtr - mu[:, None]) ** 2) * m).sum(1) / np.maximum(cnt, 1) + eps[:, None]
        val = np.log(cnt[:, 0] / (n - 1)) - 0.5 * np.log(2 * np.pi * var).sum(1) \
            - 0.5 * ((X - mu) ** 2 / var).sum(1)
        ll[ok, k] = val[ok]
    return classes[np.argmax(ll, axis=1)]


def loo_ovr_logistic(X: np.ndarray, y: np.ndarray, C: float = 1.0, n_newton: int = 100) -> np.ndarray:
    """Leave-one-out predictions of LogisticRegression(solver='liblinear') with
    default settings, one-vs-rest over the classes, as scikit-learn did for
    several classes with this solver when the paper's code ran (from version
    1.5 the solver refuses more than two classes; OneVsRestClassifier gives the
    same model). liblinear's objective, 0.5 |w|^2 + C sum log(1 + exp(-y w.x))
    with x extended by a constant 1 (intercept_scaling 1, the intercept
    penalised), is strictly convex; it is minimised here by Newton's method
    for every fold and class at once, so that 2000 subsamples run in seconds.
    The notebook checks the predictions against scikit-learn."""
    n = len(y)
    classes = np.unique(y)
    Xa = np.hstack([np.asarray(X, float), np.ones((n, 1))])
    p = Xa.shape[1]
    keep = ~np.eye(n, dtype=bool)
    Xtr = np.stack([Xa[keep[i]] for i in range(n)])                     # (n, n-1, p)
    ytr = np.stack([y[keep[i]] for i in range(n)])                      # (n, n-1)
    K = len(classes)
    Xb = np.repeat(Xtr[:, None], K, axis=1).reshape(n * K, n - 1, p)
    yb = np.stack([np.where(ytr == c, 1.0, -1.0) for c in classes], 1).reshape(n * K, n - 1)
    w = np.zeros((n * K, p))
    eye = np.eye(p)
    for _ in range(n_newton):
        z = yb * np.einsum("bnp,bp->bn", Xb, w)
        s = special.expit(z)
        g = w + C * np.einsum("bnp,bn->bp", Xb, (s - 1) * yb)
        H = eye + C * np.einsum("bnp,bn,bnq->bpq", Xb, s * (1 - s), Xb)
        step = np.linalg.solve(H, g[..., None])[..., 0]
        w = w - step
        if np.abs(step).max() < 1e-10:
            break
    dec = np.einsum("ikp,ip->ik", w.reshape(n, K, p), Xa)
    return classes[np.argmax(dec, axis=1)]


def _loo_predict(kind, Xs, ys):
    if kind == "nb":
        return loo_gaussian_nb(Xs, ys)
    if kind == "lr":
        return loo_ovr_logistic(Xs, ys)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import LeaveOneOut, cross_val_predict
    m = RandomForestClassifier(n_estimators=100, random_state=424242)
    return cross_val_predict(m, Xs, ys, cv=LeaveOneOut())


def _loo_pair(args):
    kind, Xs, ys, ysh = args
    return _loo_predict(kind, Xs, ys), _loo_predict(kind, Xs, ysh)


def classify_labs(X: np.ndarray, labs: np.ndarray, kind: str = "nb", n_iter: int = 2000,
                  per_lab: int = 8, seed: int = 424242, return_confusion: bool = False,
                  workers: int = 1):
    """Accuracy over n_iter subsamples of per_lab mice per lab, leave-one-out,
    and the same with lab labels shuffled within each subsample (Methods;
    code seed 424242). kind: 'nb' GaussianNB, 'rf' RandomForest (100 trees,
    random_state 424242), 'lr' LogisticRegression (solver liblinear, one-vs-rest;
    loo_ovr_logistic). The subsamples and shuffles are drawn in the same order
    whatever the number of worker processes, so workers cannot change a result."""
    rng = np.random.default_rng(seed)
    labs = np.asarray(labs)
    names = np.array(sorted(set(labs)))
    acc, null = np.empty(n_iter), np.empty(n_iter)
    conf = np.zeros((len(names), len(names)))
    draws = []
    for k in range(n_iter):
        idx = np.concatenate([rng.choice(np.flatnonzero(labs == l), per_lab, replace=False)
                              for l in names])
        draws.append((kind, X[idx], labs[idx], rng.permutation(labs[idx])))
    if workers > 1:
        if workers not in _POOLS:
            _POOLS[workers] = ProcessPoolExecutor(workers)
        preds = _POOLS[workers].map(_loo_pair, draws)
    else:
        preds = map(_loo_pair, draws)
    for k, ((_, Xs, ys, ysh), (p, psh)) in enumerate(zip(draws, preds)):
        acc[k] = np.mean(p == ys)
        if return_confusion:
            for a, b in zip(ys, p):
                conf[np.searchsorted(names, a), np.searchsorted(names, b)] += 1
        null[k] = np.mean(psh == ysh)
    if return_confusion:
        return acc, null, names, conf / conf.sum(1, keepdims=True)
    return acc, null


# ---------------------------------------------------------------------------
# Choice consistency within labs (code suppfig_choicevariability_withinacrosslabs)

def within_lab_consistency(M: pd.DataFrame, labs: pd.Series) -> float:
    """M: mice x conditions of fraction rightward. Per lab, the variance
    across mice per condition, its mean over conditions and its inverse; the
    mean over labs."""
    cons = []
    for l in sorted(labs.unique()):
        v = M[labs.to_numpy() == l].var(axis=0, ddof=1).mean()
        cons.append(1 / v)
    return float(np.mean(cons))


def _consistency_many(M: np.ndarray, L: np.ndarray, K: int) -> np.ndarray:
    """within_lab_consistency for many labellings at once. M: mice x
    conditions (NaN where missing); L: labellings x mice, lab codes 0..K-1.
    Per lab and condition the variance across mice (ddof 1, NaN skipped, NaN
    with fewer than two mice), its mean over conditions, its inverse, and the
    mean over labs."""
    ok = ~np.isnan(M)
    M0 = np.where(ok, M, 0.0)
    out = np.empty(len(L))
    for a in range(0, len(L), 500):
        G = (L[a: a + 500, None, :] == np.arange(K)[None, :, None]).astype(float)   # (b, K, mice)
        cnt = G @ ok.astype(float)
        s1 = G @ M0
        s2 = G @ (M0 ** 2)
        with np.errstate(invalid="ignore", divide="ignore"):
            var = (s2 - s1 ** 2 / cnt) / (cnt - 1)
            var[cnt < 2] = np.nan
            out[a: a + 500] = np.mean(1 / np.nanmean(var, axis=2), axis=1)
    return out


def consistency_test(M: pd.DataFrame, labs: pd.Series, n_shuffle: int = 10000, seed: int = 0):
    """Observed within-lab consistency, its null over n_shuffle permutations
    of the lab labels, and the fraction of the null at or above the observed
    value."""
    rng = np.random.default_rng(seed)
    obs = within_lab_consistency(M, labs)
    names, codes = np.unique(labs.to_numpy(), return_inverse=True)
    L = np.stack([rng.permutation(codes) for _ in range(n_shuffle)])
    null = _consistency_many(M.to_numpy(float), L, len(names))
    return obs, null, float(np.mean(null >= obs))


# ---------------------------------------------------------------------------
# Trials with their mouse, day and task; session windows around a criterion

def trials_with_days(T: pd.DataFrame, S: pd.DataFrame, Dall: pd.DataFrame) -> pd.DataFrame:
    t = T.merge(S[["session_id", "subject_id", "date", "task", "lab_number", "start"]],
                on="session_id")
    t = t.merge(Dall[["subject_id", "date", "tday0"]], on=["subject_id", "date"])
    return t


def window(Tm: pd.DataFrame, crit_day: pd.Series, lo: int, hi: int, tasks) -> pd.DataFrame:
    """Trials of the given tasks on training days crit_day + lo to crit_day + hi
    (inclusive) of each mouse in crit_day (a Series of tday0 by subject)."""
    t = Tm[Tm.subject_id.isin(crit_day.index) & Tm.task.isin(tasks)]
    rel = t.tday0 - t.subject_id.map(crit_day)
    return t[(rel >= lo) & (rel <= hi)].assign(rel_day=rel)


def mouse_fits(t: pd.DataFrame, by=("subject_id",), workers: int = 4) -> pd.DataFrame:
    """Psychometric fit per group of trials (fit_psychfunc), in parallel."""
    keys, pairs = [], []
    for k, d in t.groupby(list(by)):
        keys.append(k)
        pairs.append((d.signed_contrast.to_numpy(), d.choice_right.to_numpy()))
    res = fit_many(pairs, workers)
    idx = pd.MultiIndex.from_tuples(keys, names=list(by)) if len(by) > 1 else \
        pd.Index([k[0] if isinstance(k, tuple) else k for k in keys], name=by[0])
    return pd.DataFrame(res, index=idx)


# ---------------------------------------------------------------------------
# Probabilistic choice model (Methods, equations 2-4; claims fig5cf)

GLM_CONTRASTS = (6.25, 12.5, 25.0, 50.0, 100.0)


def glm_design(t: pd.DataFrame, full: bool, drop50: bool) -> pd.DataFrame:
    """Predictors per trial: signed indicator per nonzero contrast (+1 right,
    -1 left), the previous choice split by its outcome (r: +1 right rewarded,
    -1 left rewarded, 0 unrewarded; u: the same for unrewarded), and in the
    full task the block (+1 20:80, -1 80:20, 0 50:50). The previous trial is
    the previous trial of the same session. No-response trials are left out
    after the history terms are formed; with drop50, 50% contrast trials too."""
    parts = []
    for _, d in t.sort_values(["session_id", "start_time"]).groupby("session_id", sort=False):
        d = d.copy()
        side = np.where(d.choice == -1, 1.0, np.where(d.choice == 1, -1.0, 0.0))  # +1 right choice
        rew = (d.feedbackType == 1).to_numpy()
        prev_side = np.r_[0.0, side[:-1]]
        prev_rew = np.r_[False, rew[:-1]]
        d["rewarded"] = np.where(prev_rew, prev_side, 0.0)
        d["unrewarded"] = np.where(~prev_rew, prev_side, 0.0)
        parts.append(d)
    d = pd.concat(parts)
    d = d[d.choice != 0]
    if drop50:
        d = d[d.abs_contrast != 50]
    for c in GLM_CONTRASTS:
        if drop50 and c == 50:
            continue
        name = "c" + str(c).replace(".", "_")
        d[name] = np.where(d.abs_contrast == c, np.sign(d.signed_contrast), 0.0)
    if full:
        d["block"] = np.where(np.isclose(d.probabilityLeft, 0.2), 1.0,
                              np.where(np.isclose(d.probabilityLeft, 0.8), -1.0, 0.0))
    return d


def glm_formula(full: bool, drop50: bool) -> str:
    names = ["c" + str(c).replace(".", "_") for c in GLM_CONTRASTS if not (drop50 and c == 50)]
    rhs = names + ["rewarded", "unrewarded"] + (["block"] if full else [])
    return "choice_right ~ " + " + ".join(rhs)


def fit_glm(d: pd.DataFrame, full: bool, drop50: bool, n_folds: int = 5, seed: int = 0) -> dict:
    """statsmodels Logit.fit_regularized with its defaults on the patsy design
    (Methods); weights, pseudo-R2, the condition number of the design matrix,
    and 5-fold cross-validated accuracy (folds shuffled; seed a standard
    choice) by two readings: (1) fraction of test trials where the predicted
    probability of the actual choice exceeds 0.5, (2) mean predicted
    probability of the actual choice."""
    import patsy
    import statsmodels.api as sm
    from sklearn.model_selection import KFold
    y, X = patsy.dmatrices(glm_formula(full, drop50), d, return_type="dataframe")
    y = y.iloc[:, 0].to_numpy()
    # A contrast the mouse was not shown (50% is dropped late in basic training
    # and absent from the full task) gives an all-zero column, whose weight
    # cannot be estimated; it is left out of that mouse's model.
    X = X.loc[:, (X != 0).any(axis=0) | (X.columns == "Intercept")]
    res = sm.Logit(y, X).fit_regularized(disp=False)
    out = {k: v for k, v in res.params.items()}
    out["pseudo_r2"] = 1 - res.llf / sm.Logit(y, np.ones((len(y), 1))).fit(disp=False).llf
    out["cond"] = np.linalg.cond(X.to_numpy())
    out["n_trials"] = len(y)
    acc1, acc2 = [], []
    for tr, te in KFold(n_folds, shuffle=True, random_state=seed).split(X):
        r = sm.Logit(y[tr], X.iloc[tr]).fit_regularized(disp=False)
        p = r.predict(X.iloc[te])
        pa = np.where(y[te] == 1, p, 1 - p)
        acc1.append(np.mean(pa > 0.5))
        acc2.append(np.mean(pa))
    out["acc_threshold"] = 100 * np.mean(acc1)
    out["acc_prob"] = 100 * np.mean(acc2)
    return out


def _glm_one(args):
    try:
        return fit_glm(*args)
    except Exception as e:  # reported as a failed fit
        return {"error": repr(e)}


def fit_glms(items, workers: int = 4):
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_glm_one, items))


# ---------------------------------------------------------------------------
# History-dependent choice updating (claims fig5s1b, c; code suppfig_history_strategy)

def history_columns(t: pd.DataFrame) -> pd.DataFrame:
    """Previous and next trial's choice (+1 right, -1 left, 0 none), outcome
    and absolute contrast, within each session."""
    parts = []
    for _, d in t.sort_values(["session_id", "start_time"]).groupby("session_id", sort=False):
        d = d.copy()
        side = np.where(d.choice == -1, 1.0, np.where(d.choice == 1, -1.0, 0.0))
        rew = (d.feedbackType == 1).astype(float).to_numpy()
        ac = d.abs_contrast.to_numpy()
        d["prev_choice"] = np.r_[np.nan, side[:-1]]
        d["prev_reward"] = np.r_[np.nan, rew[:-1]]
        d["prev_contrast"] = np.r_[np.nan, ac[:-1]]
        d["next_choice"] = np.r_[side[1:], np.nan]
        d["next_reward"] = np.r_[rew[1:], np.nan]
        d["next_contrast"] = np.r_[ac[1:], np.nan]
        parts.append(d)
    return pd.concat(parts)


# ---------------------------------------------------------------------------
# Session-end criteria (Figure 1, figure supplement 2 legend)

def end_criterion_trial(stim_on: np.ndarray, rt: np.ndarray, t0: float = 0.0):
    """First trial (1-based) at which one of the three legend criteria is met:
    fewer than 400 trials in 45 min; over 400 trials and 90 min; over 400
    trials and median reaction time over the last 20 trials above 5 times the
    session median. None when no criterion is met."""
    n = len(stim_on)
    el = (stim_on - t0) / 60.0
    for i in range(n):
        if not np.isfinite(el[i]):
            continue
        k = i + 1
        if k < 400 and el[i] >= 45:
            return k
        if k > 400 and el[i] >= 90:
            return k
        if k > 400:
            last = rt[max(0, i - 19): i + 1]
            if np.nanmedian(last) > 5 * np.nanmedian(rt[: i + 1]):
                return k
    return None


# ---------------------------------------------------------------------------
# Clock check: wheel against the trial table

def wheel_displacement(asset_id: str, shift: float = 0.0, retries: int = 4):
    """Wheel displacement between stimulus onset and response time for each
    trial, with the trial times shifted by `shift` seconds; and the choices.
    Returns (None, reason) when the wheel series cannot be used."""
    url = f"{API}/assets/{asset_id}/download/"
    for attempt in range(retries):
        try:
            with h5py.File(remfile.File(url), "r") as f:
                w = f["processing/behavior/BehavioralTimeSeries/position"]
                pos, ts = w["data"][:], w["timestamps"][:]
                t = f["intervals/trials"]
                on, resp, ch = t["stimOn_times"][:], t["response_times"][:], t["choice"][:]
        except Exception:
            time.sleep(2 * (attempt + 1))
            continue
        if len(pos) != len(ts):
            return None, f"wheel data {len(pos)} samples, timestamps {len(ts)}"
        if np.any(np.diff(ts) < 0):
            return None, "wheel timestamps not monotonic"
        try:
            out = {}
            for s in np.atleast_1d(shift):
                a = np.interp(on + s, ts, pos)
                b = np.interp(resp + s, ts, pos)
                out[float(s)] = b - a
            return out, ch
        except Exception as e:
            return None, repr(e)
    return None, "not read"


def _wheel_one(args):
    return wheel_displacement(*args)


def wheel_many(asset_ids, shifts, workers: int = 8):
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_wheel_one, [(a, shifts) for a in asset_ids]))
