"""Loading and measures for the behavior of Kauvar, Richman, Liu et al. 2025 (Science 388, eadt3971)
deposited in dandiset 001347, version 0.250528.0702.

The dandiset holds three kinds of behavioral file used here:

- `sub-mouse/sub-mouse_ses-<id>_behavior.nwb`: one eye closure trace per behavior-rig experiment
  (`acquisition/eye_closure`, 200 Hz), with no condition label. Trials are 16200 frames (81 s), the
  first puff of a trial 6 s after its start, eight puffs 3 s apart (mouse_eyepuff code below). The
  experiment ids per condition come from the paper's code, Zenodo doi:10.5281/zenodo.14920570
  (`EXPERIMENTS` below, with the file and line of each list).
- `sub-m<mouse>-<rec>/..._ses-puff_behavior.nwb`: eye closure of the Neuropixels-recorded mice
  (100 Hz), with the onset of each puff series (`events-on`, frames), `ket_trial`,
  `trial_range_preket`, `trial_range_ket` and per-trial and per-puff cut-outs.
- `sub-h0xx/sub-h0xx_ses-P50_behavior.nwb`: per-trial eye closure (800 samples) of the four
  non-implanted human participants, `pre_trials_data` and `post_trials_data`, 40 trials each, and
  the time axis `time_reference/tt`.

Where each parameter comes from (Zenodo code paths are relative to kauvar-richman-liu-2025_zenodo/):

- Session lists per condition (`EXPERIMENTS`): mouse_eyepuff/scripts/fig1_drugs.py:23-30 (saline,
  ket50, pcp20, kx, dzp, bup), fig1_dose.py (ket35, ket25, ket13, ket6, pcp10, pcp5, pcp1),
  fig1_psi.py (8, 18, 28 PSI), fig1_muscimol.py (intact, sal, vpm_musc). Within a list the
  position is the mouse (the code pairs conditions by position, e.g. fig1_drugs_first_puff.py
  `ttest_rel(saline, ket)` grouped by `id`); this is the code's assumption, kept here.
- Trial counts and selections: drug and dose experiments 40 trials, Pre trials 5 to 19 and infusion
  trials 22 to 36 (0-based, 15 each; fig1_drugs.py:61-70, fig1_dose.py); PSI and muscimol 20 trials,
  trials 2 to 16 for every condition (fig1_psi.py, fig1_muscimol.py).
- Baseline: each trial minus the mean of its first 400 frames (2 s), ketmouse/eye_trace_utils.py
  `prox_norm` (lines 35-56) as called by `get_mean_traces` with do_prox=True (lines 853-907); the
  further subtraction of trial `baseline_trial` and the scale 1/(1 - baseline) are then 0 and 1.
- Windows: early (reflexive) 0.1 to 0.2 s, late (affective) 0.3 to 0.8 s after a puff (Fig. 1
  legend; fig1_drugs.py:66-67); frame indices fps*(6 + t_puff + w), cast to int (fig1_drugs.py:198-201,
  340-343). Puff k (0-based) is at t_puff = 3k s.
- Normalized late closure: per trial late divided by the mean over trials of early, then the mean
  over trials per mouse (`mean_ref=True`, eye_trace_utils.py `get_data_by_trial` lines 746-812 and
  `plot_drug_comparison_bar_from_df` lines 1315-1433; PSI: `plot_puff_comparison_bar_trials`
  lines 1536-1617).
- Tests: paired t-tests with Benjamini-Hochberg correction (eye_trace_utils.py
  `annotate_pvals_pre_vs_post` lines 75-106; fig1_psi.py; fig1_muscimol.py).
- Persistence (Kaplan-Meier): mouse_eyepuff/scripts/fig1_persistence.py: raw trace, baseline the
  mean of the first 5 s of the trial, closed while above 1.2 times baseline, scanned from
  fps*(6 + 8*3 + 0.3) (30.3 s into the trial, 3.3 s after the eighth puff onset), event at the first
  frame not above, censored at 50 s if never. The KM product-limit estimator and its median (first
  time the survival function is at or below 0.5, as lifelines' median_survival_time_) are written
  out here, a standard choice that does not change the estimate.
- Recorded mice: analysis.py (Zenodo doi:10.5281/zenodo.14876694) `make_puffseries_behavior_plot`
  lines 38-90: puff 1 of a series at `events-on` + 5 s, puffs 3 s apart, each puff cut from 1 s
  before to 2 s after (5 s more after puff 8), the trial minus the mean of the 1 s before puff 1,
  Pre series 1 to 20, Ketamine series 23 to 32, each condition's mean trace divided by its maximum.
- Link to dandiset 001326: the recorded sessions are named in
  mouse_eyepuff/scripts/convert_npx_mouse_airpuff_to_nwb.py:15-24 as `<date>_m<mouse>_<rec>`; the
  date and mouse give the 001326 session (`NPX_SESSIONS`). The video clock is mapped onto the 001326
  clock by a linear fit of the series onsets (assumption: a linear clock relation; the residuals are
  printed).
- Tones: onsets from the 001326 stimulus table, mapped onto the video by that fit. Pre is the first
  10 tone series before ketamine onset (30 s after the last puff of series 20, analysis.py
  `get_windowed_tone_psth`), Ketamine the first 5 after it (table S3, fig. S34 C), 10 as a variant
  (code). Baseline the 1 s before the first tone.
- Human: human_ieeg/scripts/analyze_airpuff_p50.py: trials 2 to 39 (the first two skipped), samples
  with 0.3 < tt < 0.8 and 0.1 < tt < 0.2, per-participant late / mean(early), `pre_trials` taken as
  saline and `post_trials` as ketamine (the script labels them 'saline' and 'highdose').
- Model: analysis.py theoretical model (inputs, segments, `model_system`, lines 2757-2790),
  `filter_reflex` (line 2803), `theoretical_behavior` (line 2861) and `compare_models` bounds and
  starting values (line 2867). The behavioral data fed to it are not in the code: assumed here to
  be the across-mouse mean of the infusion-trial mean traces (trials 22 to 36), 1 s before to 43 s
  after the first puff, averaged to 100 Hz (Methods, "Model fitting, behavioral data").

Cite Kauvar, Richman, Liu et al., Science (2025) for the methods reimplemented here.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import scipy.stats
from scipy.optimize import curve_fit
from statsmodels.stats.multitest import multipletests

DANDISET = "001347"
VERSION = "0.250528.0702"            # dandi:001347/0.250528.0702, the only published version
DANDISET_NPX = "001326"
VERSION_NPX = "0.250528.1957"
CODE_DOI = "10.5281/zenodo.14920570"  # paper's behavior code, source of the session-to-condition lists

FPS = 200                  # behavior rig, file unit "Eye closure, sampled at 200.0Hz"
FRAMES_PER_TRIAL = 16200   # eye_trace_utils.py load_files_nwb
T_FIRST = 6.0              # s from trial start to puff 1 (get_mean_traces: t = frame/fps - 6)
BASELINE_FRAMES = 400      # prox_norm
LATE = (0.3, 0.8)          # s, Fig. 1 legend
EARLY = (0.1, 0.2)         # s, Fig. 1 legend

# mouse_eyepuff/scripts: fig1_drugs.py:23-30, fig1_dose.py, fig1_psi.py, fig1_muscimol.py
EXPERIMENTS = {
    "sal": [282, 283, 284, 285, 286],
    "ket50": [275, 276, 277, 280, 281],
    "pcp20": [287, 288, 289, 290, 291],
    "kx": [316, 338, 339, 343, 344],
    "dzp": [325, 326, 327, 333, 334],
    "bup": [340, 341, 342, 347, 348],
    "ket35": [1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027],
    "ket25": [355, 356, 357, 362, 363],
    "ket13": [401, 400, 399, 398, 397],
    "ket6": [403, 405, 404, 406, 426],
    "pcp10": [358, 359, 360, 361, 364],
    "pcp5": [370, 368, 366, 365, 434],
    "pcp1": [430, 432, 431, 435, 436],
    "18 PSI": [1004, 1001, 1002, 1003, 1030, 1031, 1029, 1028],
    "8 PSI": [1034, 1033, 1032, 1035, 1008, 1005, 1007, 1006],
    "28 PSI": [1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027],
    "intact": [975, 971, 972, 973, 974],
    "musc_sal": [984, 985, 980, 981, 982],
    "vpm_musc": [989, 990, 986, 987, 988],
}
# code lists of panels no claim here uses (convert_mouse_airpuff_to_nwb.py:11-64; fig1_days.py,
# fig1_sex.py, fig1_skippuff.py, fig1_psi.py '5 PSI'); listed only to account for every file
EXPERIMENTS_OTHER = {
    # written in short pieces: tools/entry.py's literal scan backtracks without end on long integer lists
    "days": [668, 669, 670, 671, 674, 672, 673] + [677, 678, 679, 675, 676, 682, 683] + [684, 680, 681, 687, 688, 689]
            + [685, 686, 690, 691, 692],
    "male": [700, 701, 702, 708, 709],
    "skip": [411, 412, 413, 420, 421],
    "5 PSI": [1014, 1016, 1019, 1017, 1011, 1012, 1013, 1009],
}
NTRIALS = {k:(20 if ("PSI" in k or k in ("intact", "musc_sal", "vpm_musc")) else 40) for k in EXPERIMENTS}
WHICH_PRE = {k: (np.arange(2, 17) if NTRIALS[k] == 20 else np.arange(5, 20)) for k in EXPERIMENTS}
WHICH_POST = {k: (np.arange(2, 17) if NTRIALS[k] == 20 else np.arange(22, 37)) for k in EXPERIMENTS}

# convert_npx_mouse_airpuff_to_nwb.py:15-24 (<date>_m<mouse>_<rec>) -> 001326 session
NPX_SESSIONS = {
    "m94-549": "sub-8_ses-20220228",
    "m304-876": "sub-7_ses-20220831",
    "m11208-959": "sub-1_ses-20230218",
    "m11208-962": "sub-1_ses-20230226",
    "m11210-960": "sub-3_ses-20230218",
    "m11219-1108": "sub-6_ses-20230823",
    "m11221-1119": "sub-0_ses-20230901",
    "m11223-1125": "sub-2_ses-20230902",
    "m11225-1131": "sub-4_ses-20230907",
    "m11227-1132": "sub-9_ses-20230908",
}
NPX_DATES = {k: v.split("ses-")[1] for k, v in NPX_SESSIONS.items()}


# ---------------------------------------------------------------- archive access

def asset_urls(dandiset=DANDISET, version=VERSION):
    """{path: S3 url} of every file in the pinned version."""
    from dandi.dandiapi import DandiAPIClient
    client = DandiAPIClient()
    assets = list(client.get_dandiset(dandiset, version).get_assets())
    urls = _pmap(lambda a: a.get_content_url(follow_redirects=1, strip_query=True), assets)
    return {a.path: u for a, u in zip(assets, urls)}


def _open(url):
    return h5py.File(remfile.File(url), "r")


def _pmap(fn, items, workers=16):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(fn, items))


# ---------------------------------------------------------------- behavior-rig mice

def load_mouse(ids, urls, max_frames=None):
    """Stream the eye closure trace of each behavior-rig experiment id; returns {id: (trace, meta)}."""
    def one(i):
        f = _open(urls[f"sub-mouse/sub-mouse_ses-{i}_behavior.nwb"])
        ts = f["acquisition/eye_closure"]
        d = ts["data"]
        x = d[:max_frames] if max_frames else d[:]
        meta = {"n_frames": d.shape[0], "rate": float(ts["starting_time"].attrs["rate"]),
                "unit": ts["data"].attrs["unit"], "subject_id": f["general/subject/subject_id"][()].decode(),
                "description": f["general/subject/description"][()].decode()}
        f.close()
        return i, (np.asarray(x, float), meta)
    return dict(_pmap(one, sorted(set(ids))))


def by_trial(trace, ntrials, prox=True):
    """Reshape to (ntrials, frames) as load_files_nwb + get_mean_traces; subtract each trial's first 2 s."""
    m = trace[:FRAMES_PER_TRIAL * ntrials].reshape(ntrials, -1)
    if prox:
        m = m - m[:, :BASELINE_FRAMES].mean(1, keepdims=True)
    return m


def win(tpuff, w, fps=FPS, t_first=T_FIRST):
    """Frame indices of window w after the puff at tpuff s (fig1_drugs.py:198-201)."""
    a = (fps * (t_first + np.array([tpuff + w[0], tpuff + w[1]]))).astype(int)
    return a[0], a[1]


def puff_measures(trials, puff):
    """Per-trial late and early closure for puff `puff` (0-based) and the per-mouse summaries."""
    la, lb = win(3 * puff, LATE)
    ea, eb = win(3 * puff, EARLY)
    late = np.nanmean(trials[:, la:lb], axis=1)
    early = np.nanmean(trials[:, ea:eb], axis=1)
    return {"late": late.mean(), "early": early.mean(), "norm": np.mean(late / early.mean())}


def condition_table(data, conds, puff):
    """Per-mouse pre and infusion values of late, early and normalized late closure at one puff."""
    rows = []
    for c in conds:
        for pos, i in enumerate(EXPERIMENTS[c]):
            m = by_trial(data[i][0], NTRIALS[c])
            for phase, sel in (("pre", WHICH_PRE[c]), ("post", WHICH_POST[c])):
                r = puff_measures(m[sel], puff)
                rows.append({"cond": c, "mouse": pos, "id": i, "phase": phase, **r})
    return pd.DataFrame(rows)


def paired(df, cond_a, phase_a, cond_b, phase_b, metric):
    """Paired t-test across mouse positions of metric (a against b); returns (t, p, a, b)."""
    a = df[(df.cond == cond_a) & (df.phase == phase_a)].sort_values("mouse")[metric].to_numpy()
    b = df[(df.cond == cond_b) & (df.phase == phase_b)].sort_values("mouse")[metric].to_numpy()
    t, p = scipy.stats.ttest_rel(a, b)
    return t, p, a, b


def fdr(p):
    return multipletests(np.asarray(p, float), method="fdr_bh")[1]


def mean_sem(x):
    x = np.asarray(x, float)
    return x.mean(), scipy.stats.sem(x)


# ---------------------------------------------------------------- persistence (fig. S2E)

def survival_times(trace, ntrials, trials, fps=FPS):
    """fig1_persistence.py: time from 30.3 s into the trial to the first frame not above 1.2 x baseline."""
    m = trace[:FRAMES_PER_TRIAL * ntrials].reshape(ntrials, -1)[trials]
    last = int(fps * (6 + 8 * 3 + LATE[0]))
    base = m[:, :fps * 5].mean(1)
    b = m > 1.2 * base[:, None]
    first = b[:, last:].argmin(1)
    never = np.where(b[:, last:].min(1) == 1)[0]
    first[never] = fps * 50
    ev = np.ones_like(first)
    ev[never] = 0
    return first / fps, ev


def km_median(times, events):
    """Kaplan-Meier product-limit survival and its median (first t with S(t) <= 0.5)."""
    times = np.asarray(times, float)
    events = np.asarray(events, int)
    s = 1.0
    for t in np.unique(times):
        at_risk = np.sum(times >= t)
        d = np.sum((times == t) & (events == 1))
        if at_risk:
            s *= 1 - d / at_risk
        if s <= 0.5:
            return float(t)
    return np.inf


# ---------------------------------------------------------------- recorded mice

def load_npx(urls):
    """Stream the recorded mice's eye closure files; {mouse_rec: dict}."""
    keys = ["fps", "ket_trial", "ket_puff", "w_pre", "w_post", "led_delay", "npuffs_per_trial"]

    def one(name):
        f = _open(urls[f"sub-{name}/sub-{name}_ses-puff_behavior.nwb"])
        A = f["acquisition"]
        d = {k: int(A[k]["data"][0]) for k in keys}
        d.update({
            "eyeclosure": A["eyeclosure/data"][:],
            "rate": float(A["eyeclosure/starting_time"].attrs["rate"]),
            "events_on": A["events-on/data"][:],
            "events_off": A["events-off/data"][:],
            "trial_range_preket": A["trial_range_preket/data"][:],
            "trial_range_ket": A["trial_range_ket/data"][:],
            "by_trial_shape": A["eyeclosure_by_trial/data"].shape,
            "by_puff_shape": A["eyeclosure_by_puff/data"].shape,
            "t_trial": A["t_trial_eyeclosure/data"][[0, -1]],
            "subject_id": f["general/subject/subject_id"][()].decode(),
            "description": f["general/subject/description"][()].decode(),
        })
        f.close()
        return name, d
    return dict(_pmap(one, list(NPX_SESSIONS)))


def npx_series(d, first_only=False):
    """analysis.py make_puffseries_behavior_plot: (n_series, samples) cut-outs, baseline the 1 s before puff 1."""
    fps = d["fps"]
    x = d["eyeclosure"]
    out = []
    for e in d["events_on"] + 5 * fps:
        parts = []
        for k in range(8):
            p = int(e + k * 3 * fps)
            extra = int(5 * fps) if k == 7 else 0
            if first_only and k > 0:
                continue
            seg = x[p - fps: p + 2 * fps + extra]
            parts.append(seg)
        if sum(len(s) for s in parts) != (3 * fps if first_only else 8 * 3 * fps + 5 * fps):
            break  # series running past the end of the video
        tr = np.concatenate(parts)
        out.append(tr - np.nanmean(parts[0][:fps]))
    return np.stack(out)


def npx_late(series, k, fps=100):
    """Late closure (0.3 to 0.8 s) after puff k in the concatenated cut-out (each puff 3 s, 1 s before)."""
    a = int(fps * (3 * k + 1 + LATE[0]))
    b = int(fps * (3 * k + 1 + LATE[1]))
    return np.nanmean(series[..., a:b], axis=-1)


def stim_001326(sessions):
    """Puff and tone onsets and infusion time from the 001326 stimulus tables (only these datasets read)."""
    urls = asset_urls(DANDISET_NPX, VERSION_NPX)
    by_name = {p.split("/")[-1].replace("_ecephys.nwb", ""): u for p, u in urls.items()}

    def one(s):
        f = _open(by_name[s])
        g = f["intervals/Stimulus presentations"]
        st = g["start_time"][:]
        kind = np.array([x.decode() if isinstance(x, bytes) else str(x) for x in g["stimulus"][:]])
        out = {k: np.sort(st[kind == k]) for k in np.unique(kind)}
        out["ket_infusion"] = float(f["acquisition/Ketamine infusion start/timestamps"][0])
        f.close()
        return s, out
    return dict(_pmap(one, sessions, workers=13))


def series_starts(t, gap=10.0):
    br = np.where(np.diff(t) > gap)[0] + 1
    return np.array([s[0] for s in np.split(t, br)]), np.split(t, br)


def link_clock(d, stim):
    """Fit 001326 series onset = a * video event time + b over the first n series; returns fit and residuals."""
    ev = d["events_on"] / d["fps"]
    ser, _ = series_starts(stim["puff"])
    n = min(len(ev), len(ser))
    a, b = np.polyfit(ev[:n], ser[:n], 1)
    res = ser[:n] - (a * ev[:n] + b)
    return {"a": a, "b": b, "n_video": len(ev), "n_001326": len(ser), "n_matched": n,
            "max_abs_resid_s": float(np.max(np.abs(res)))}


def tone_series(d, stim, fit, fps=100):
    """Tone series cut-outs on the video clock: 1 s before the first tone to 2 s after the last."""
    x = d["eyeclosure"]
    starts, groups = series_starts(stim["tone"])
    out, t0 = [], []
    for g in groups:
        if len(g) != 8:
            continue
        fr = ((g - fit["b"]) / fit["a"] * fps).astype(int)
        if fr[0] - fps < 0 or fr[-1] + 3 * fps > len(x):
            continue
        parts = [x[f - fps: f + 2 * fps] for f in fr]
        tr = np.concatenate(parts)
        out.append(tr - np.nanmean(parts[0][:fps]))
        t0.append(g[0])
    return np.array(t0), (np.stack(out) if out else np.zeros((0, 8 * 3 * fps)))


# ---------------------------------------------------------------- humans

def load_p50(urls):
    """{participant: (pre (40, 800), post (40, 800), tt)} from the P50 files."""
    names = sorted(p for p in urls if p.endswith("_ses-P50_behavior.nwb"))

    def one(p):
        f = _open(urls[p])
        A = f["acquisition"]
        tt = A["time_reference/tt/data"][:]
        pre = np.stack([A[f"pre_trials_data/pre_trial_{i + 1}/data"][:] for i in range(len(A["pre_trials_data"]))])
        post = np.stack([A[f"post_trials_data/post_trial_{i + 1}/data"][:] for i in range(len(A["post_trials_data"]))])
        sid = f["general/subject/subject_id"][()].decode()
        f.close()
        return sid, (pre, post, tt)
    return dict(_pmap(one, names))


def human_measures(trials, tt, trial_range=np.arange(2, 40)):
    late_i = (tt > LATE[0]) & (tt < LATE[1])
    early_i = (tt > EARLY[0]) & (tt < EARLY[1])
    late = np.nanmean(trials[trial_range][:, late_i], axis=1)
    early = np.nanmean(trials[trial_range][:, early_i], axis=1)
    return {"late": late.mean(), "early": early.mean(), "norm": np.mean(late / early.mean()),
            "early_sum": np.nansum(trials[trial_range][:, early_i], axis=1).mean(), "n_early_samples": int(early_i.sum())}


# ---------------------------------------------------------------- model (analysis.py 2757-2880)

BIN_T = 0.01
_inputs = np.hstack([np.concatenate([np.zeros(100), np.ones(25), np.zeros(175)]) for _ in range(8)])
_inputs = np.hstack([_inputs, np.zeros(int(47 / BIN_T))])
_segments = np.hstack([np.hstack([(i * 300), (i * 300) + 100, (i * 300) + 100, (i * 300) + 125,
                                  (i * 300) + 125, (i * 300) + 300]) for i in range(8)])
_segments = np.hstack([_segments, [300 * 8, 300 * 8 + int(47 / BIN_T)]]).reshape((-1, 2))


def model_system(S, tB, tP):
    Sin = S * _inputs
    out = np.zeros_like(Sin)
    x0 = Sin[0]
    for a, b in _segments:
        t = np.arange(0, b - a) * BIN_T
        if Sin[a] != 0:
            xt = (Sin[a] - x0) * (1 - np.exp(-t / tB)) + x0
        else:
            xt = x0 * np.exp(-t / tP)
        out[a:b] = xt
        x0 = xt[-1]
    return out


def filter_reflex(trace):
    """analysis.py:2803, drop the 750 ms after each puff."""
    parts = [trace[:100]]
    for i in range(8):
        parts.append(trace[100 + i * 300 + 75:100 + i * 300 + 300])
    parts.append(trace[100 + 7 * 300 + 300:])
    return np.hstack(parts)


def theoretical_behavior(x, S, tB, tP, *c):
    return np.hstack([filter_reflex(model_system(S, tB, tP * ci)[:3 * 8 * 100 + 20 * 100]) for ci in c])


def fit_behavior_model(data, conditions):
    """analysis.py compare_models bounds and starts; variance explained 1 - MSE_model / MSE_null."""
    p0 = [1, 1, 1] + [1] * conditions
    bounds = ([0, 0, 0] + [0] * conditions, [100, 100, 100] + [1] * conditions)
    bounds_null = ([0, 0, 0] + [0.99999] * conditions, [100, 100, 100] + [1] * conditions)
    x = np.arange(len(data))
    pm, _ = curve_fit(theoretical_behavior, x, data, p0=p0, maxfev=5000, bounds=bounds)
    pn, _ = curve_fit(theoretical_behavior, x, data, p0=p0, maxfev=5000, bounds=bounds_null)
    e_m = np.mean((data - theoretical_behavior(x, *pm)) ** 2)
    e_n = np.mean((data - theoretical_behavior(x, *pn)) ** 2)
    return {"varexp": 1 - e_m / e_n, "S": pm[0], "tauB": pm[1], "tauP": pm[2] * pm[3:], "factors": pm[3:],
            "null_tauP": pn[2] * pn[3:]}


def model_trace(data, cond, which=None):
    """Across-mouse mean of the infusion-trial mean trace, -1 to 43 s from puff 1, averaged to 100 Hz."""
    which = WHICH_POST[cond] if which is None else which
    per = []
    for i in EXPERIMENTS[cond]:
        m = by_trial(data[i][0], NTRIALS[cond])[which].mean(0)
        seg = m[int(FPS * (T_FIRST - 1)): int(FPS * (T_FIRST - 1)) + 2 * 4400]
        per.append(seg.reshape(-1, 2).mean(1))
    return np.mean(per, axis=0)
