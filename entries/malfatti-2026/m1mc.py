"""Loading and measures for dandiset 002056 (Malfatti, Velica et al. 2026, eLife 14:RP109286).

The dandiset holds three groups of mice on the single pellet prehension task, each file one
session of one mouse, with DeepLabCut (DLC) positions and likelihoods of ten body parts at 50
frames/s:

- `BehaviourL5GqMC`: the behaviour-only learning group (CLZ before every session), 13 mice,
  sessions 1 to 10 as deposited.
- `L5PCMSMCGq`: the miniscope group, 7 mice, sessions 1, 2, 5 and 6. The NWB files hold the DLC
  tracking and a OnePhotonSeries that points to the raw miniscope AVI files; no extracted traces.
- `LFPM1GqMC`: the LFP group, 11 mice, sessions 8 to 13, one LFP channel at 30 kHz.

Files are streamed from the archive at the pinned version with remfile and h5py; nothing is
written to disk.

Where the parameters come from:

- Prehension detection follows the paper's code (https://gitlab.com/malfatti/M1MartinottiOnMovement,
  commit 86efdf1; MS_PRT_Reaches.py, BehavOnly.py and LFP_PRT_Reaches.py share it), as the claims
  file's opening comment fixes: frames where the likelihood of LPaw and LFinger1 (columns 5 and 6
  of the network's body parts, Core.LHCutOff 0.7) exceed 0.7, single-frame gaps filled,
  single-frame blocks dropped, rising edges by sciscripts Analysis.QuantifyTTLs with its default
  threshold (mean + 2.5 SD of the binary trace), and the first onset in each rounded second.
  `detect_prehensions(..., parts=LEFT_ALL)` is the Methods' variant (paw and its three fingers).
  `edge="any"` takes every onset, the reading of the Methods' "blocks", without the code's
  2.5 SD threshold.
- Accuracy follows Core.ReachClassify of the same commit (claims file, opening comment), with the
  sciscripts functions it calls (EucDist, QuantifyTTLs, PolygonArea, RMS) as they were at
  sciscripts commit ef25f53 (2024-04-25), the last before the code's commit. The video size is
  the camera's 1920 x 1080 px (Methods, "Pellet prehension task", the code's default when no
  video is found). Every class but 'Success' is failed (BehavOnly.py, LFP_PRT_Reaches.py).
- Session 5 of the behaviour-only group is split at 300 s into session 5 (spoon) and session 6
  (plate), and later sessions are renumbered +1 (Methods, "Pellet prehension task": "After five
  minutes in the fifth session, the pellet was instead placed on a fixed position on the plate";
  BehavOnly.py does the split from a per-mouse table, Session5Split.dict, not in the repository,
  and renumbers the sessions after 5 by +1, line 330). The per-mouse split times are not public;
  300 s is the Methods' "five minutes".
- Counts per session normalised to 10 min of session time, as BehavOnly.py does (the halves of
  session 5 keep the full session's time there, and here).
- LFP: decimated from 30 kHz to 1 kHz before filtering (a standard choice that cannot change
  power below 100 Hz), second-order Butterworth band-pass applied forward and backward
  (sciscripts FilterSignal, order 2 as LFP_PRT_EPhys.py calls it), then a spectrogram (Hann
  windows; 1 s with 50% overlap, and 0.5 s as a variant: the claims file's reading d), power
  normalised by the mean (per frequency bin over the recording, or over all bins: reading c; and
  the running mean of each bin up to that time, a literal reading of the Methods' "cumulative
  mean", added under step 1.6), and
  averaged over the bins inside the band (Methods, "LFP electrophysiology analysis").
- Statistics follow the paper's Statistical analysis section and sciscripts Stats.Full 'auto':
  Shapiro's test in every cell, Holm-adjusted, normal when the smallest adjusted p exceeds 0.05;
  then a mixed-model ANOVA, or else the ANOVA-type statistic (Brunner, Domhof and Langer 2002, as
  R nparLD computes it, with infinite denominator degrees of freedom).
"""

from __future__ import annotations

import itertools
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import signal, stats

DANDISET_ID = "002056"
DANDISET_VERSION = "0.261113.1541"
API = "https://api.dandiarchive.org/api"

# Body parts in the order of the network's config.yaml (Mice-Fingers_Forepaws_Nose_Pellet-PRT-Front).
BODY_PARTS = ["Nose", "RPaw", "RFinger1", "RFinger2", "RFinger3",
              "LPaw", "LFinger1", "LFinger2", "LFinger3", "Pellet1"]
READ_XY = (5, 9)                # the analysis uses positions of LPaw and Pellet1 only
READ_LH = (5, 6, 7, 8, 9)       # and likelihoods of the left paw, its fingers and the pellet
LH_CUTOFF = 0.7                 # Core.LHCutOff; Methods "70%"
LEFT_CODE = (5, 6)              # BehavOnly.py etc.: range(5, 7), LPaw and LFinger1
LEFT_ALL = (5, 6, 7, 8)         # Methods: the left paw and its three fingers
FPS = 50                        # Methods, 50 FPS; the files' rate
FRAME_W, FRAME_H = 1920, 1080   # Methods, 1920x1080 px
SESSION5_SPLIT_S = 300.0        # Methods: "After five minutes in the fifth session"
SESSION_MINUTES = 10.0          # BehavOnly.py: counts / ((TotalTime/60)/10)

BANDS = {  # Methods, "LFP electrophysiology analysis"; beta is a standard choice (claims file)
    "full": (1, 100), "theta": (4, 12), "gamma": (30, 90), "low_theta": (4, 7),
    "high_theta": (8, 12), "low_gamma": (30, 40), "high_gamma": (60, 90), "beta": (13, 30),
}
LFP_RATE_OUT = 1000


# ---------------------------------------------------------------------------- archive

def list_assets():
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += page["results"]
        url = page["next"]
    return out


def asset_url(asset):
    return f"{API}/assets/{asset['asset_id']}/download/"


def nwb_table(assets):
    """One row per NWB file: group, subject, session (as deposited) and the asset."""
    rows = []
    for a in assets:
        p = a["path"]
        if not p.endswith(".nwb"):
            continue
        name = p.split("/")[1]
        ses = int(name.split("_ses-Session")[1].split("Trial")[0])
        trial = int(name.split("Trial")[1].split("_")[0])
        rows.append(dict(path=p, subject=p.split("/")[0][4:], session=ses, trial=trial,
                         kind=name.split("_")[-1][:-4], size_mb=a["size"] / 1e6, asset=a))
    return pd.DataFrame(rows)


def _s(h, k):
    v = h[k][()]
    return v.decode() if isinstance(v, bytes) else v


def open_h5(asset):
    return h5py.File(remfile.File(asset_url(asset)), "r")


def load_dlc(asset, lfp=False):
    """DLC arrays X, Y, Lh (frames x 10 body parts), with the file's metadata.

    With lfp=True the LFP channel is read too, decimated to 1 kHz (LFP_RATE_OUT)."""
    with open_h5(asset) as h:
        b = h["processing/behavior"]
        lh = b["LPawLikelihood"]
        n = lh["data"].shape[0]
        X, Y, L = [np.full(n, np.nan) for _ in BODY_PARTS], [np.full(n, np.nan) for _ in BODY_PARTS], \
            [np.full(n, np.nan) for _ in BODY_PARTS]
        for i, bp in enumerate(BODY_PARTS):
            if i in READ_XY:
                xy = b[f"Position/{bp}Position/data"][:]
                X[i], Y[i] = xy[:, 0], xy[:, 1]
            if i in READ_LH:
                L[i] = b[f"{bp}Likelihood/data"][:]
        d = dict(X=np.array(X).T, Y=np.array(Y).T, Lh=np.array(L).T,
                 rate=float(lh["starting_time"].attrs["rate"]), t0=float(lh["starting_time"][()]),
                 start_time=_s(h, "session_start_time"),
                 subject=_s(h, "general/subject/subject_id"), genotype=_s(h, "general/subject/genotype"),
                 sex=_s(h, "general/subject/sex"), session_id=_s(h, "general/session_id"),
                 units_xy=b["Position/LPawPosition/data"].attrs["unit"],
                 trial_start=h["intervals/trials/start_time"][:], trial_stop=h["intervals/trials/stop_time"][:])
        if "acquisition/OnePhotonSeries" in h:
            o = h["acquisition/OnePhotonSeries"]
            d["ms_timestamps"] = o["timestamps"][:]
            d["ms_files"] = [x.decode() for x in o["external_file"][:]]
        if lfp and "acquisition/ElectricalSeries" in h:
            e = h["acquisition/ElectricalSeries"]
            rate = float(e["starting_time"].attrs["rate"])
            d["lfp_rate_in"] = rate
            d["lfp_t0"] = float(e["starting_time"][()])
            d["lfp_unit"] = e["data"].attrs["unit"]
            d["lfp_n_in"] = e["data"].shape[0]
            d["lfp_channels"] = [x.decode() if isinstance(x, bytes) else str(x)
                                 for x in h["general/extracellular_ephys/electrodes/channelName"][:]]
            q = int(round(rate / LFP_RATE_OUT))
            raw = e["data"][:].astype(np.float64)
            d["lfp_raw_range"] = (float(raw.min()), float(raw.max()), float(raw.std()))
            # two stages of 5 and 6 (30 kHz to 1 kHz), FIR anti-alias filters, zero phase
            x = signal.decimate(raw, 5, ftype="fir", zero_phase=True)
            x = signal.decimate(x, q // 5, ftype="fir", zero_phase=True)
            d["lfp"] = x
            d["lfp_rate"] = rate / q
            del raw
    return d


def load_many(assets, lfp=False, workers=8):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda a: load_dlc(a, lfp), assets))


# ---------------------------------------------------------------------------- sciscripts (ef25f53)

def quantify_ttls(data, std_no=2.5, edge="rise"):
    """sciscripts Analysis.QuantifyTTLs: edges crossing mean + std_no * SD."""
    thr = data.mean() + std_no * data.std()
    rise = (data[:-1] < thr) * (data[1:] > thr)
    fall = (data[:-1] > thr) * (data[1:] < thr)
    return np.where(rise if edge == "rise" else fall)[0]


def euc_dist(a, b):
    return (np.diff(a) ** 2 + np.diff(b) ** 2) ** 0.5, np.arctan2(np.diff(b), np.diff(a))


def polygon_area(x, y):
    nan = np.isnan(x) + np.isnan(y)
    x, y = x[~nan], y[~nan]
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def rms(x):
    return np.mean(x ** 2) ** 0.5


# ---------------------------------------------------------------------------- prehensions

def reach_trace(Lh, parts=LEFT_CODE, cutoff=LH_CUTOFF):
    good = np.ones(Lh.shape[0], dtype=bool)
    for b in parts:
        good *= Lh[:, b] > cutoff
    r = good.astype(float)
    gap = np.where((r[:-2] == 1) * (r[1:-1] == 0) * (r[2:] == 1))[0] + 1
    r[gap] = 1
    single = np.where((r[:-2] == 0) * (r[1:-1] == 1) * (r[2:] == 0))[0] + 1
    r[single] = 0
    return r


def detect_prehensions(Lh, rate=FPS, parts=LEFT_CODE, edge="code"):
    """Onset frames of prehensions, as the code finds them (one per rounded second).

    edge='code' uses QuantifyTTLs' default threshold (mean + 2.5 SD of the binary trace),
    edge='any' every 0 to 1 transition."""
    r = reach_trace(Lh, parts)
    time = np.arange(r.shape[0]) / rate
    if edge == "code":
        ttls = quantify_ttls(r)
    else:
        ttls = np.where((r[:-1] < 0.5) * (r[1:] > 0.5))[0]
    ttls_sec = ttls[np.unique(np.round(time[ttls]).astype(int), return_index=True)[1]] if len(ttls) else ttls
    return r, time, ttls, ttls_sec


def reach_classify(reaches, time, ttls_sec, X, Y, Lh, fps=FPS):
    """Core.ReachClassify of the paper's code, line for line. Returns classes and invalid indices."""
    lpaw = euc_dist(X[:, 5], Y[:, 5])[0]
    lpaw[~reaches[1:].astype(bool)] = 0
    pel, pel_ang = euc_dist(X[:, -1], Y[:, -1])
    pel = pel.copy(); pel_ang = pel_ang.copy()
    pel[~reaches[1:].astype(bool)] = 0
    pel_ang[~reaches[1:].astype(bool)] = 0
    full_area = FRAME_W * FRAME_H
    w = fps // 2
    result, invalid = [], []
    with np.errstate(all="ignore"):
        for T, ttl in enumerate(ttls_sec):
            tw = [ttl - w, ttl + w]
            if min(tw) < 0 or max(tw) > time.shape[0]:
                invalid.append(T)
                continue
            seg = reaches[tw[0]:tw[1]]
            ends = quantify_ttls(seg, LH_CUTOFF, "fall")
            t_end = ends[0] + 1 if len(ends) else seg.shape[0]
            t_r = reaches.copy()
            t_r[tw[0]:tw[1]][t_end:] = 0
            reach_range = np.where(t_r[tw[0]:tw[1]])[0]
            t_bl = time[tw[0]:tw[1]] < time[ttl]
            tp, tlh = pel[tw[0]:tw[1]], Lh[tw[0]:tw[1], -1]
            tpa = pel_ang[tw[0]:tw[1]]
            m = tpa[reach_range].mean() if len(reach_range) else np.nan
            tpa_up = np.pi / 2 - 0.5 < m < np.pi / 2 + 0.5
            pa = polygon_area(X[tw[0]:tw[1], -1][~t_bl], Y[tw[0]:tw[1], -1][~t_bl]) / full_area
            pa = pa < 5e-4
            tp_mean = tp[reach_range].mean() if len(reach_range) else np.nan
            tp_mean_m = 0.01 < tp_mean < 0.5
            tlh_m = tlh.mean() > LH_CUTOFF
            tlh_bl = tlh[t_bl].mean() > LH_CUTOFF
            tlh_rs = tlh[~t_bl].mean() > LH_CUTOFF
            ppd = euc_dist(X[tw[0]:tw[1]][:, [5, -1]].ravel(), Y[tw[0]:tw[1]][:, [5, -1]].ravel())[0][::2]
            ppd_bl, ppd_rs = ppd[t_bl].mean(), ppd[~t_bl].mean()
            mx = rms(np.diff(X[tw[0]:tw[1], -1][~t_bl]))
            my = rms(np.diff(Y[tw[0]:tw[1], -1][~t_bl]))
            if tlh_m and pa and tp_mean_m:
                result.append("HitMiss")
            elif pa and tlh_bl == tlh_rs:
                result.append("Miss")
            elif tlh_bl and not tlh_rs and not tpa_up and mx > my and ppd_rs > ppd_bl:
                result.append("HitDrop")
            elif not tlh_bl:
                result.append("NoPellet")
            else:
                result.append("Success")
    return np.array(result), np.array(invalid, dtype=int)


def prehensions(d, parts=LEFT_CODE, edge="code"):
    """Table of valid prehensions of one file: onset time (s, file clock), class, accuracy."""
    r, time, ttls, ttls_sec = detect_prehensions(d["Lh"], d["rate"], parts, edge)
    cls, inv = reach_classify(r, time, ttls_sec, d["X"], d["Y"], d["Lh"], int(round(d["rate"])))
    keep = np.setdiff1d(np.arange(len(ttls_sec)), inv)
    on = ttls_sec[keep]
    df = pd.DataFrame(dict(frame=on, t=time[on] + d["t0"], cls=cls))
    df["success"] = df.cls == "Success"
    df.attrs.update(n_onsets=len(ttls), n_per_second=len(ttls_sec), n_invalid=len(inv),
                    frac_frames_on=float(r.mean()), duration_s=float(time[-1]))
    return df


# ---------------------------------------------------------------------------- statistics

def holm(p):
    p = np.asarray(p, float)
    o = np.argsort(p)
    m = len(p)
    adj = np.empty(m)
    run = 0
    for k, i in enumerate(o):
        run = max(run, (m - k) * p[i])
        adj[i] = min(1, run)
    return adj


def is_normal(df, value, factors):
    """sciscripts IsNormal: Shapiro per cell, Holm, normal when min adjusted p > 0.05."""
    ps = []
    for _, g in df.groupby(list(factors)):
        v = g[value].dropna().values
        if len(v) >= 3 and np.ptp(v) > 0:
            ps.append(stats.shapiro(v).pvalue)
        elif len(v) >= 3:
            ps.append(0.0)
    if not ps:
        return True, np.nan
    adj = holm(ps)
    return bool(adj.min() > 0.05), float(adj.min())


def _cube(df, value, subject, between, within):
    """Array subjects x within cells (balanced), with group labels; drops incomplete subjects."""
    levels = [sorted(df[w].unique(), key=lambda x: (str(type(x)), x)) for w in within]
    cells = list(itertools.product(*levels))
    piv = df.pivot_table(index=subject, columns=list(within), values=value, aggfunc="mean")
    if len(within) == 1:
        piv = piv.reindex(columns=[c[0] for c in cells])
    else:
        piv = piv.reindex(columns=pd.MultiIndex.from_tuples(cells))
    piv = piv.dropna()
    grp = df.groupby(subject)[between].first().reindex(piv.index) if between else None
    return piv.values, grp, levels


def _P(k):
    return np.eye(k) - np.ones((k, k)) / k


def _J(k):
    return np.ones((k, k)) / k


def mixed_anova(df, value, subject, between, within):
    """Split-plot ANOVA with one between factor (or none) and any number of within factors.

    Sums of squares from orthogonal projections of the subject x cell array (equal to the
    classical split-plot ANOVA; with unequal group sizes the between-group terms weight
    subjects equally). Returns a table of F, df and p for every effect."""
    Ymat, grp, levels = _cube(df, value, subject, between, within)
    nsub, ncell = Ymat.shape
    wl = [len(l) for l in levels]
    groups = sorted(grp.unique()) if between else ["all"]
    gidx = [np.where(grp.values == g)[0] for g in groups] if between else [np.arange(nsub)]
    out = []
    wnames = list(within)
    for r in range(0, len(within) + 1):
        for comb in itertools.combinations(range(len(within)), r):
            # within contrast matrix
            mats = [_P(wl[i]) if i in comb else _J(wl[i]) for i in range(len(within))]
            C = mats[0]
            for M in mats[1:]:
                C = np.kron(C, M)
            if r == 0:
                C = np.ones((ncell, ncell)) / ncell
            Z = Ymat @ C  # projected data per subject
            # error: subjects within groups
            ss_err = sum(((Z[ix] - Z[ix].mean(0)) ** 2).sum() for ix in gidx)
            df_err = (nsub - len(gidx)) * (np.trace(C).round().astype(int) if r else 1)
            names = [wnames[i] for i in comb]
            # effect of within combination (pooled over groups)
            if r > 0:
                ss = nsub * (Z.mean(0) ** 2).sum()
                dfe = int(round(np.trace(C)))
                out.append(dict(effect=":".join(names), F=(ss / dfe) / (ss_err / df_err), df1=dfe, df2=df_err))
            if between and len(groups) > 1:
                gm = np.array([Z[ix].mean(0) for ix in gidx])
                ss = sum(len(ix) * ((gm[k] - Z.mean(0)) ** 2).sum() for k, ix in enumerate(gidx))
                dfe = (len(groups) - 1) * (int(round(np.trace(C))) if r else 1)
                out.append(dict(effect=":".join([between] + names), F=(ss / dfe) / (ss_err / df_err), df1=dfe, df2=df_err))
    t = pd.DataFrame(out)
    t["p"] = stats.f.sf(t.F, t.df1, t.df2)
    t.attrs["n_subjects"] = nsub
    return t


def ats(df, value, subject, between, within):
    """ANOVA-type statistic for split-plot designs (nparLD's f1.ld.f1, f1.ld.f2, ld.f1 ...).

    Ranks over all observations, relative effects per cell, covariance of the subjects' rank
    vectors within each group; F = p'Tp / tr(T S), df1 = tr(TS)^2 / tr(TSTS), df2 = inf."""
    Ymat, grp, levels = _cube(df, value, subject, between, within)
    nsub, ncell = Ymat.shape
    wl = [len(l) for l in levels]
    groups = sorted(grp.unique()) if between else ["all"]
    gidx = [np.where(grp.values == g)[0] for g in groups] if between else [np.arange(nsub)]
    a = len(groups)
    N = Ymat.size
    R = stats.rankdata(Ymat.ravel()).reshape(Ymat.shape)
    RTP = (R - 0.5) / N
    p = np.concatenate([RTP[ix].mean(0) for ix in gidx])
    S = np.zeros((a * ncell, a * ncell))
    for k, ix in enumerate(gidx):
        V = np.cov(RTP[ix].T, ddof=1) if len(ix) > 1 else np.zeros((ncell, ncell))
        S[k * ncell:(k + 1) * ncell, k * ncell:(k + 1) * ncell] = np.atleast_2d(V) / len(ix)
    out = []
    for r in range(0, len(within) + 1):
        for comb in itertools.combinations(range(len(within)), r):
            mats = [_P(wl[i]) if i in comb else _J(wl[i]) for i in range(len(within))]
            names = [within[i] for i in comb]
            for withgrp in ([False, True] if (between and a > 1) else [False]):
                if r == 0 and not withgrp:
                    continue
                M = _P(a) if withgrp else _J(a)
                T = M
                for m in mats:
                    T = np.kron(T, m)
                tr = np.trace(T @ S)
                F = float(p @ T @ p / tr) if tr > 0 else np.nan
                df1 = tr ** 2 / np.trace(T @ S @ T @ S) if tr > 0 else np.nan
                out.append(dict(effect=":".join(([between] if withgrp else []) + names), F=F, df1=df1, df2=np.inf))
    t = pd.DataFrame(out)
    t["p"] = stats.chi2.sf(t.F * t.df1, t.df1)
    t.attrs["n_subjects"] = nsub
    return t


def auto_anova(df, value, subject, between, within):
    """Stats.Full 'auto': mixed ANOVA when normal by Shapiro (Holm), else the ATS."""
    factors = ([between] if between else []) + list(within)
    normal, pmin = is_normal(df, value, factors)
    t = mixed_anova(df, value, subject, between, within) if normal else ats(df, value, subject, between, within)
    t.attrs.update(test="mixed ANOVA" if normal else "ANOVA-type statistic", shapiro_min_padj=pmin,
                   n_subjects=t.attrs["n_subjects"])
    return t


def fmt(t):
    s = t.copy()
    s["F"] = s.F.round(3); s["df1"] = s.df1.round(2); s["p"] = s.p.map(lambda x: f"{x:.3g}")
    return s.to_string(index=False)


# ---------------------------------------------------------------------------- LFP

def band_power(x, rate, band, win_s=1.0, norm="bin"):
    """Band-filtered LFP -> spectrogram -> normalised -> mean over bins in the band.

    Returns (times in s from the start of x, power per time bin)."""
    sos = signal.butter(2, [band[0] / (rate / 2), band[1] / (rate / 2)], "bandpass", output="sos")
    y = signal.sosfiltfilt(sos, x)
    nper = int(win_s * rate)
    f, t, S = signal.spectrogram(y, rate, window="hann", nperseg=nper, noverlap=nper // 2)
    if norm == "bin":
        S = S / S.mean(axis=1, keepdims=True)
    elif norm == "cum":
        S = S / (np.cumsum(S, axis=1) / np.arange(1, S.shape[1] + 1))
    else:
        S = S / S.mean()
    sel = (f >= band[0]) & (f <= band[1])
    return t, S[sel].mean(0)


def window_means(t, pw, onsets, pre=(-1.0, 0.0), post=(0.0, 1.0)):
    """Mean power over the time bins whose centres fall in each prehension's before/after window."""
    b, a = [], []
    for o in onsets:
        mb = (t >= o + pre[0]) & (t < o + pre[1])
        ma = (t >= o + post[0]) & (t < o + post[1])
        b.append(pw[mb].mean() if mb.any() else np.nan)
        a.append(pw[ma].mean() if ma.any() else np.nan)
    return np.array(b), np.array(a)


def locked_lag(d, lo=-60.0, hi=60.0, band=(1, 30)):
    """Lag (s) at which the prehension-locked LFP potential is strongest, for the clock check.

    The 1-30 Hz LFP (z-scored) is averaged at the prehension onsets shifted by every lag; the score
    at a lag is the RMS of that average over +/- 0.5 s around it. Returns lags, scores."""
    fs = int(round(d["lfp_rate"]))
    sos = signal.butter(2, [band[0] / (fs / 2), band[1] / (fs / 2)], "bandpass", output="sos")
    y = signal.sosfiltfilt(sos, d["lfp"])
    y = (y - y.mean()) / y.std()
    p = prehensions(d)
    on = np.round((p.t.values - d["lfp_t0"]) * fs).astype(int)
    on = on[(on > 0) & (on < len(y))]
    imp = np.zeros(len(y))
    np.add.at(imp, on, 1)
    cc = signal.fftconvolve(y, imp[::-1], mode="full") / max(len(on), 1)
    lags = np.arange(-len(y) + 1, len(y)) / fs
    m = (lags >= lo) & (lags <= hi)
    sc = np.sqrt(np.convolve(cc[m] ** 2, np.ones(fs) / fs, mode="same"))
    return lags[m], sc, len(on)


def outside_mean(t, pw, onsets, half=1.0):
    m = np.ones(t.shape[0], dtype=bool)
    for o in onsets:
        m &= ~((t >= o - half) & (t <= o + half))
    return pw[m].mean() if m.any() else np.nan


# ---------------------------------------------------------------------------- per-claim tables

def learning_table(files, datas, parts=LEFT_CODE, keep_copy=False):
    """Per mouse and session counts of the behaviour-only group.

    The deposited session 5 holds the spoon (first 300 s) and plate halves (Methods); they become
    sessions 5 and 6. Deposited sessions after 5 are renumbered +1, as BehavOnly.py (line 330)
    does, so deposited sessions 7 to 10 are sessions 8 to 11. The deposited session 6 (session 7
    after renumbering) is the same recording as session 5 (identical traces, shown in the data
    check) and is dropped, unless keep_copy, which counts it as session 7. That variant has no
    meaning of its own: it only gives the paper's eleven sessions and degrees of freedom. Genotype
    is taken per subject from its files that state one."""
    gen = {}
    for d in datas:
        if d["genotype"] != "unknown":
            gen.setdefault(d["subject"], d["genotype"])
    rows = []
    for (_, r), d in zip(files.iterrows(), datas):
        p = prehensions(d, parts)
        if r.session == 6 and not keep_copy:
            continue
        if r.session == 5:
            parts_ = [(5, p[p.t < SESSION5_SPLIT_S]), (6, p[p.t >= SESSION5_SPLIT_S])]
        elif r.session > 5:
            parts_ = [(r.session + 1, p)]
        else:
            parts_ = [(r.session, p)]
        for s, q in parts_:
            rows.append(dict(mouse=r.subject, gen=gen[r.subject], session=s, total_raw=len(q),
                             success_raw=int(q.success.sum()), duration_s=p.attrs["duration_s"]))
    df = pd.DataFrame(rows)
    f = (df.duration_s / 60) / SESSION_MINUTES
    df["total"] = df.total_raw / f
    df["success"] = df.success_raw / f
    df["ratio"] = np.where(df.total_raw > 0, df.success_raw / df.total_raw.clip(lower=1), 0.0)
    return df


def overlap_flags(t, within=2.0):
    """For onsets t (s, sorted): next prehension within `within` s after (a), previous within before (b)."""
    nxt = np.r_[np.diff(t), np.inf]
    prv = np.r_[np.inf, np.diff(t)]
    return nxt <= within, prv <= within


def pooled_lag(datas, lo=-60.0, hi=60.0):
    """Per mouse: the mean over its sessions of the locked_lag score curves, its best lag, and the
    score at lag 0 and at the best lag relative to the curve's spread (z)."""
    curves = {}
    for d in datas:
        L, sc, n = locked_lag(d, lo, hi)
        curves.setdefault(d["subject"], []).append(sc)
    out = {}
    for m, cs in curves.items():
        n = min(len(c) for c in cs)
        c = np.mean([x[:n] for x in cs], axis=0)
        Lm = L[:n]
        i = int(np.argmax(c))
        far = np.abs(Lm) > 5
        z = lambda v: (v - c[far].mean()) / c[far].std()
        out[m] = dict(best_lag=float(Lm[i]), z_best=float(z(c[i])), z_at_0=float(z(c[np.argmin(np.abs(Lm))])))
    return out
