"""Loading and measures for dandiset 001847 (Bech, Dard et al., eLife, doi:10.7554/eLife.109717).

Data are streamed from the DANDI archive at the pinned version VERSION; nothing is written to disk.

Where parameters come from:
- Session groups (expert, opto, control, Context Off, muscimol, Ringer, widefield lines) are the
  lists of the paper's processing code, github.com/LSENS-BMI-EPFL/Bech_Dard_process_NWB at commit
  CODE_COMMIT (configs/session_groups), as the claims file cites them. The dandiset records no
  mouse line (every subject's genotype is "WT" or "Ai148"), so the lists are the only source of it.
- Early-lick trials (perf 6, early_lick 1) are dropped for behaviour (claims file, opening comment,
  citing cicada behavior_analysis_utils.py:37), except where a criterion says otherwise.
- The opto map (opto_map) follows the claims file's opening comment (process
  main_analysis/figure2_analysis.py:44-145, plot utils/figure2CDE.py, misc/stats.py:8-12).
  The code builds the null on the full trial table, early licks kept; this is followed.
- Widefield d' follows plot misc/stats.py:97 as the claims file gives it (ddof 0, signed).
- Window lengths for trial-aligned widefield traces (-0.3 to +0.3 s) are a standard choice that
  cannot change a result: every measure uses a sub-window of it.
"""
import io
import json
import re
import signal
from multiprocessing import Pool

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
import yaml

DANDISET = "001847"
VERSION = "0.260610.1400"
API = "https://api.dandiarchive.org/api"
CODE_COMMIT = "212a63103528cdeafb6ebcf90a50235cd2290082"
CODE_RAW = f"https://raw.githubusercontent.com/LSENS-BMI-EPFL/Bech_Dard_process_NWB/{CODE_COMMIT}/configs/session_groups"

# Grid sites (AP, ML) in mm, from the claims file's opening comment (plot utils/figure4C_G.py, figure3H.py).
SITES = {"wS1": (-1.5, 3.5), "wS2": (-1.5, 4.5), "wM1": (1.5, 1.5), "wM2": (2.5, 1.5),
         "ALM": (2.5, 2.5), "tjS1": (0.5, 4.5), "tjM1": (1.5, 3.5), "A1": (-2.5, 5.5),
         "RSC": (-1.5, 0.5), "RSC_2": (-0.5, 0.5)}


# ---------------------------------------------------------------- archive
def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    a = pd.DataFrame(out)[["asset_id", "path", "size"]]
    a["subject"] = a.path.str.extract(r"sub-([^/]+)/")[0]
    a["session_id"] = a.path.str.extract(r"ses-([A-Z]+\d+)-(\d{8})-(\d{6})").agg("_".join, axis=1)
    a["kind"] = a.path.str.extract(r"_([a-z+]+)\.nwb$")[0]
    return a


def asset_url(asset_id):
    return f"{API}/assets/{asset_id}/download/"


def code_list(name):
    """Session identifiers of a session list of the paper's code (configs/session_groups/<name>.yaml)."""
    txt = requests.get(f"{CODE_RAW}/{name}.yaml", timeout=60).text
    return [s["identifier"] for s in yaml.safe_load(io.StringIO(txt))["sessions"]]


def _open(asset_id):
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def _str(x):
    x = x[()]
    return x.decode() if isinstance(x, bytes) else str(x)


def _timeout(*_):
    raise TimeoutError


def _pmap(fn, items, n=16):
    with Pool(n) as p:
        return p.map(fn, items, chunksize=2)


# ---------------------------------------------------------------- trial tables
def _trials_one(row):
    asset_id, session_id = row
    signal.signal(signal.SIGALRM, _timeout)
    for attempt in range(3):
        signal.alarm(120)
        try:
            f = _open(asset_id)
            t = f["intervals/trials"]
            d = {k: (t[k][:].astype(str) if t[k].dtype == object else t[k][:]) for k in t if k != "id"}
            T = pd.DataFrame(d)
            T["session_id"] = session_id
            ep = f["processing/behavior/BehavioralEpochs"]
            E = []
            for k in ep:
                ts, v = ep[k]["timestamps"][:], ep[k]["data"][:]
                st, sp = ts[v == 1], ts[v == -1]
                for a, b in zip(st, sp):
                    E.append((session_id, k, a, b))
            meta = {"session_id": session_id,
                    "experiment_description": _str(f["general/experiment_description"]),
                    "session_description": _str(f["session_description"]),
                    "genotype": _str(f["general/subject/genotype"]),
                    "n_epoch_start": int(sum((ep[k]["data"][:] == 1).sum() for k in ep)),
                    "n_epoch_stop": int(sum((ep[k]["data"][:] == -1).sum() for k in ep))}
            signal.alarm(0)
            return T, pd.DataFrame(E, columns=["session_id", "epoch", "start", "stop"]), meta
        except Exception as e:  # network hiccup; retried
            signal.alarm(0)
            err = repr(e)
    return None, None, {"session_id": session_id, "error": err}


def load_trials(assets):
    """Trial tables, context epochs and file metadata of the given assets (rows of list_assets())."""
    res = _pmap(_trials_one, list(zip(assets.asset_id, assets.session_id)))
    T = pd.concat([r[0] for r in res if r[0] is not None], ignore_index=True)
    E = pd.concat([r[1] for r in res if r[1] is not None], ignore_index=True)
    M = pd.DataFrame([r[2] for r in res])
    T["mouse_id"] = T.session_id.str.split("_").str[0]
    E["mouse_id"] = E.session_id.str.split("_").str[0]
    M["mouse_id"] = M.session_id.str.split("_").str[0]
    M["session_type"] = M.experiment_description.str.extract(r"'session_type': '([^']*)'")[0]
    T["stim_time"] = np.where(T.trial_type == "whisker_trial", T.whisker_stim_time,
                              np.where(T.trial_type == "auditory_trial", T.auditory_stim_time, T.no_stim_time))
    # block index within session: runs of the same context in trial order
    T = T.sort_values(["session_id", "start_time"]).reset_index(drop=True)
    T["block"] = T.groupby("session_id").context.transform(lambda c: (c != c.shift()).cumsum() - 1)
    return T, E, M


# ---------------------------------------------------------------- behaviour measures
def mouse_avg(df, value, by):
    """Mean over trials per session, then over sessions per mouse (Methods, Figures 1C-E)."""
    s = df.groupby(["mouse_id", "session_id"] + by)[value].mean().reset_index()
    return s.groupby(["mouse_id"] + by)[value].mean().reset_index()


def block_contrast(T, blocks="epochs", E=None):
    """Per session, the block contrasts of the Methods (Behavioral task and training curriculum).

    For each block but the first and last, the mean of the absolute differences in whisker hit rate
    between the block and its two neighbours. Early-lick trials dropped. blocks='epochs' uses the
    context runs of the trial table (the context epochs); blocks='20' cuts consecutive blocks of 20
    non-early-lick trials, the code's variant (figure1_supp_analysis.py:72-85)."""
    out = {}
    for sid, g in T[T.early_lick == 0].groupby("session_id"):
        g = g.sort_values("start_time")
        if blocks == "epochs":
            b = g.block.values
        else:
            b = np.arange(len(g)) // 20
        w = g.trial_type.values == "whisker_trial"
        hr = pd.Series(g.lick_flag.values[w]).groupby(b[w]).mean()
        hr = hr.reindex(np.unique(b)).values
        c = [np.nanmean([abs(hr[i] - hr[i - 1]), abs(hr[i] - hr[i + 1])]) for i in range(1, len(hr) - 1)]
        out[sid] = np.array([x for x in c if np.isfinite(x)])
    return out


def is_expert(contrasts, threshold=0.375, seed=0):
    """Lower bound of the 95% bootstrap interval of the mean contrast above threshold
    (scipy.stats.bootstrap, 10,000 resamples; process main_analysis/figure1_supp_analysis.py:53-187)."""
    from scipy.stats import bootstrap
    rng = np.random.default_rng(seed)
    res = {}
    for sid, c in contrasts.items():
        if len(c) < 2:
            res[sid] = (np.nan, False)
            continue
        if np.all(c == c[0]):
            lo = c[0]
        else:
            lo = bootstrap((c,), np.mean, n_resamples=10000, random_state=rng).confidence_interval.low
        res[sid] = (lo, bool(lo > threshold))
    return res


def transition_table(T, before=3, after=4):
    """Whisker trials around each context transition (cicada behavior_analysis_utils.py:214-274).

    Non-early-lick whisker trials; position -1 is the last whisker trial of a block, +1 the first of
    the next. Returns rows (session, mouse, direction, position, lick)."""
    rows = []
    for sid, g in T[(T.early_lick == 0) & (T.trial_type == "whisker_trial")].groupby("session_id"):
        g = g.sort_values("start_time")
        for b in range(1, g.block.max() + 1):
            pre, post = g[g.block == b - 1], g[g.block == b]
            if len(pre) == 0 or len(post) == 0:
                continue
            direction = "W-toW+" if post.context.iloc[0] == 1 else "W+toW-"
            for k in range(1, before + 1):
                if len(pre) >= k:
                    rows.append((sid, g.mouse_id.iloc[0], direction, -k, pre.lick_flag.iloc[-k]))
            for k in range(1, after + 1):
                if len(post) >= k:
                    rows.append((sid, g.mouse_id.iloc[0], direction, k, post.lick_flag.iloc[k - 1]))
    return pd.DataFrame(rows, columns=["session_id", "mouse_id", "direction", "position", "lick"])


# ---------------------------------------------------------------- statistics
def cohen_d(x, y):
    """Pooled-SD Cohen's d, ddof 1 (plot misc/stats.py:8-12)."""
    nx, ny = len(x), len(y)
    return (np.mean(x) - np.mean(y)) / np.sqrt(((nx - 1) * np.var(x, ddof=1) + (ny - 1) * np.var(y, ddof=1)) / (nx + ny - 2))


def dprime(a, b, axis=0):
    """Signed d' across mice, (mean a - mean b) / sqrt((var a + var b) / 2), ddof 0 (plot misc/stats.py:97)."""
    return (np.mean(a, axis) - np.mean(b, axis)) / np.sqrt((np.var(a, axis) + np.var(b, axis)) / 2)


# ---------------------------------------------------------------- opto map
def opto_map(T, mice, null="trials", n_shuffle=10000, seed=0):
    """Per mouse, context, trial type and site, dP(Lick) = lick probability with the laser at the
    site minus that on control trials (opto_stim 0), all the mouse's sessions pooled, and its null.

    null='trials': lick outcomes permuted across all trials of that trial type and context within
    each session (Figure 2 legend; figure2_analysis.py:70-82). null='blocks': the context labels
    of whole blocks permuted within each session (Methods, Figures 2C-E). Returns a table of observed
    dP per mouse and the pooled null per (context, trial_type, site), and the d' of figure2CDE.py:29
    (absolute Cohen's d between the null pooled over mice and the per-mouse dP values)."""
    rng = np.random.default_rng(seed)
    obs, nulls = [], {}
    D = T[T.mouse_id.isin(mice)].copy()
    D = D[~(D.opto_grid_ap == 3.5)]  # the code drops the AP 3.5 row (figure2_analysis.py:150)
    D["site"] = list(zip(D.opto_grid_ap.round(2), D.opto_grid_ml.round(2)))
    D.loc[D.opto_stim == 0, "site"] = "control"
    for mouse, M in D.groupby("mouse_id"):
        for ttype, G in M.groupby("trial_type"):
            sites = sorted(set(G.site) - {"control"})
            sidx = {s: i for i, s in enumerate(sites)}
            S = np.zeros((len(G), len(sites)))
            for i, s in enumerate(G.site.values):
                if s != "control":
                    S[i, sidx[s]] = 1
            C = (G.site.values == "control").astype(float)
            L = G.lick_flag.values.astype(float)
            ctx = G.context.values
            sess = G.session_id.values
            for c in (0, 1):
                m = ctx == c
                dp = (L * m) @ S / np.maximum(m @ S, 1) - (L * m) @ C / max((m * C).sum(), 1)
                cnt = m @ S
                for s, v, n in zip(sites, dp, cnt):
                    if n > 0:
                        obs.append((mouse, c, ttype, s, v, n))
            # null
            if null == "trials":
                for c in (0, 1):
                    m = ctx == c
                    idx = np.where(m)[0]
                    P = np.empty((n_shuffle, len(idx)))
                    for sid in np.unique(sess[idx]):
                        j = np.where(sess[idx] == sid)[0]
                        P[:, j] = rng.permuted(np.broadcast_to(L[idx][j], (n_shuffle, len(j))), axis=1)
                    Si, Ci = S[idx], C[idx]
                    nd = P @ Si / np.maximum(Si.sum(0), 1) - (P @ Ci / max(Ci.sum(), 1))[:, None]
                    for k, s in enumerate(sites):
                        if Si[:, k].sum() > 0:
                            nulls.setdefault((c, ttype, s), []).append(nd[:, k])
            else:
                # block labels permuted within each session; trials take their block's new label
                blk = G.block.values
                Mk = np.zeros((n_shuffle, len(G)), dtype=bool)
                for sid in np.unique(sess):
                    j = np.where(sess == sid)[0]
                    Ts = T[T.session_id == sid]
                    labels = Ts.groupby("block").context.first()
                    perm = np.array([rng.permutation(labels.values) for _ in range(n_shuffle)])
                    bpos = np.searchsorted(labels.index.values, blk[j])
                    Mk[:, j] = perm[:, bpos] == 1
                for c in (0, 1):
                    m = (Mk if c == 1 else ~Mk).astype(float)
                    num = (m * L) @ S
                    den = m @ S
                    nd = num / np.where(den > 0, den, np.nan) - (((m * L) @ C) / np.maximum(m @ C, 1))[:, None]
                    for k, s in enumerate(sites):
                        v = nd[:, k]
                        v = v[np.isfinite(v)]
                        if len(v):
                            nulls.setdefault((c, ttype, s), []).append(v)
    obs = pd.DataFrame(obs, columns=["mouse_id", "context", "trial_type", "site", "dP", "n_trials"])
    rows = []
    for (c, ttype, s), g in obs.groupby(["context", "trial_type", "site"]):
        nl = np.concatenate(nulls[(c, ttype, s)])
        rows.append((c, ttype, s, g.dP.mean(), len(g), abs(cohen_d(nl, g.dP.values)), nl.mean(), nl.std()))
    summ = pd.DataFrame(rows, columns=["context", "trial_type", "site", "dP_mean", "n_mice", "dprime", "null_mean", "null_sd"])
    return obs, summ


# ---------------------------------------------------------------- widefield grid traces
def _grid_one(args):
    asset_id, session_id, pre, post = args
    signal.signal(signal.SIGALRM, _timeout)
    for attempt in range(3):
        signal.alarm(900)
        try:
            f = _open(asset_id)
            g = f["processing/ophys/brain_grid_fluorescence/dff0_grid_traces"]
            names = [n.decode() if isinstance(n, bytes) else n for n in g["control_description"][:]]
            ts = g["timestamps"][:]
            X = g["data"][:].astype(np.float32)
            t = f["intervals/trials"]
            tt = t["trial_type"][:].astype(str)
            st = np.where(tt == "whisker_trial", t["whisker_stim_time"][:],
                          np.where(tt == "auditory_trial", t["auditory_stim_time"][:], t["no_stim_time"][:]))
            dt = np.median(np.diff(ts))
            offs = np.arange(int(round(-pre / dt)), int(round(post / dt)) + 1)
            i0 = np.searchsorted(ts, st)
            ok = (i0 + offs[0] >= 0) & (i0 + offs[-1] < len(ts))
            W = np.full((len(st), len(offs), X.shape[1]), np.nan, np.float32)
            W[ok] = X[(i0[ok, None] + offs[None, :])]
            lag = np.where(ok, ts[np.clip(i0, 0, len(ts) - 1)] - st, np.nan)
            signal.alarm(0)
            return session_id, names, offs * dt, W, lag
        except Exception as e:
            signal.alarm(0)
            err = repr(e)
    return session_id, None, None, None, err


def load_grid(assets, pre=0.3, post=0.3, n=8):
    """Trial-aligned grid ROI dF/F0 (the 42 grid circles of brain_grid_fluorescence/dff0_grid_traces),
    from pre s before to post s after each trial's stimulus time; the first frame at or after the
    stimulus is time 0. Returns {session_id: (site_names, times, array trials x time x site, lag)}."""
    res = _pmap(_grid_one, [(a, s, pre, post) for a, s in zip(assets.asset_id, assets.session_id)], n=n)
    return {r[0]: r[1:] for r in res}


def site_index(names):
    """Map (AP, ML) tuples to column indices of the grid traces, whose names are '(AP, ML)'."""
    out = {}
    for i, n in enumerate(names):
        m = re.match(r"\(\s*([-\d.]+),\s*([-\d.]+)\)", n)
        if m:
            out[(float(m.group(1)), float(m.group(2)))] = i
    return out


# ---------------------------------------------------------------- hierarchical bootstrap
def hier_boot(groups, n_iter=100000, seed=42):
    """Two-level bootstrap of the difference of differences (process main_analysis/figure2_supp_stats.py).

    groups: dict with keys ('m', 1), ('m', 2), ('r', 1), ('r', 2) (drug, session number), each a list
    of per-mouse binary outcome arrays. Mice are drawn with replacement, then trials within a mouse;
    the mean of n trials drawn with replacement from a binary array is Binomial(n, p)/n, which is
    used to draw the trial level exactly. Each group is resampled independently. Returns the
    observed statistic, the bootstrap draws and the two-sided p (twice the smaller tail)."""
    rng = np.random.default_rng(seed)

    def draw(arrs):
        n = np.array([len(a) for a in arrs])
        k = np.array([a.sum() for a in arrs])
        pick = rng.integers(0, len(arrs), size=(n_iter, len(arrs)))
        nn = n[pick]
        kk = rng.binomial(nn, (k / n)[pick])
        return kk.sum(1) / nn.sum(1)

    def obs(arrs):
        return np.concatenate(arrs).mean()
    o = (obs(groups[("m", 2)]) - obs(groups[("m", 1)])) - (obs(groups[("r", 2)]) - obs(groups[("r", 1)]))
    bs = (draw(groups[("m", 2)]) - draw(groups[("m", 1)])) - (draw(groups[("r", 2)]) - draw(groups[("r", 1)]))
    p = 2 * min((bs <= 0).mean(), (bs >= 0).mean())
    return o, bs, min(p, 1.0)


# ---------------------------------------------------------------- orofacial tracking (DeepLabCut)
SIDE_PX_PER_MM = 28.0  # Methods (Behavior videography): side camera 28 pixels/mm, top camera 24
TOP_PX_PER_MM = 24.0
LIK = {"whisker": 0.8, "jaw": 0.6, "pupil": 0.5}  # Methods, Figures 1I-J
KEEP_FRACTION = 0.7  # a body part kept for a session when at least 70% of its points pass (Methods, Figures 1I-J)


def _dlc_one(args):
    asset_id, session_id = args
    signal.signal(signal.SIGALRM, _timeout)
    for attempt in range(3):
        signal.alarm(1200)
        try:
            f = _open(asset_id)
            b = f["processing/behavior/BehavioralTimeSeries"]
            r = lambda k: b[k]["data"][:]
            ts = b["jaw_y/timestamps"][:]
            tsw = b["whisker_base_x/timestamps"][:]
            # some sessions have timestamps and data of different lengths; both are cut to the shorter
            n_j = min(len(ts), b["jaw_y"]["data"].shape[0]); n_w = min(len(tsw), b["whisker_base_x"]["data"].shape[0])
            ts, tsw = ts[:n_j], tsw[:n_w]
            rj = lambda k: b[k]["data"][:n_j]
            rw = lambda k: b[k]["data"][:n_w]
            fr = 1 / np.median(np.diff(ts))
            # jaw opening (Methods, Behavioral kinematics): vertical distance from the 5th percentile
            # of the jaw trace after a 50% likelihood filter; analysis filter 60% (Figures 1I-J).
            jy, jl = rj("jaw_y"), rj("jaw_likelihood")
            ref = np.nanpercentile(jy[jl >= 0.5], 5)
            jaw = (jy - ref) / SIDE_PX_PER_MM
            jaw_ok = jl >= LIK["jaw"]
            # pupil area: polygon of top, right, bottom, left, all four above 50% likelihood
            P = {k: (rj(f"pupil_{k}_x"), rj(f"pupil_{k}_y"), rj(f"pupil_{k}_likelihood")) for k in ["top", "right", "bottom", "left"]}
            xs = np.stack([P[k][0] for k in ["top", "right", "bottom", "left"]]); ys = np.stack([P[k][1] for k in ["top", "right", "bottom", "left"]])
            area_px = 0.5 * np.abs(np.sum(xs * np.roll(ys, -1, 0) - np.roll(xs, -1, 0) * ys, 0))
            pupil = area_px / SIDE_PX_PER_MM ** 2
            pupil_ok = np.all(np.stack([P[k][2] for k in P]) > LIK["pupil"], 0)
            stored_pupil = rj("pupil_area")
            # whisker angle (Methods, Behavioral kinematics): angle between particle - whisker base
            # and the nose midline (median nose tip - median nose base), rotated so that a whisker
            # parallel to the body is 180 degrees and a perpendicular one 90.
            v1 = np.stack([rw("top_particle_x") - rw("whisker_base_x"), rw("top_particle_y") - rw("whisker_base_y")])
            v2 = np.array([np.nanmedian(rw("top_nose_tip_x")) - np.nanmedian(rw("top_nose_base_x")),
                           np.nanmedian(rw("top_nose_tip_y")) - np.nanmedian(rw("top_nose_base_y"))])
            cosang = (v1[0] * v2[0] + v1[1] * v2[1]) / (np.hypot(v1[0], v1[1]) * np.hypot(*v2))
            wang = 180 - np.degrees(np.arccos(np.clip(cosang, -1, 1)))
            stored_wang = rw("whisker_angle")
            w_ok = (rw("whisker_base_likelihood") >= LIK["whisker"]) & (rw("top_particle_likelihood") >= LIK["whisker"])
            frw = 1 / np.median(np.diff(tsw))
            frac = {"jaw": jaw_ok.mean(), "pupil": pupil_ok.mean(), "whisker": w_ok.mean()}
            jaw_f = np.where(jaw_ok, jaw, np.nan); pupil_f = np.where(pupil_ok, pupil, np.nan); w_f = np.where(w_ok, wang, np.nan)
            jaw_speed = np.abs(np.diff(jaw_f, prepend=np.nan)) * fr
            w_speed = np.abs(np.diff(w_f, prepend=np.nan)) * frw
            sw_f = np.where(w_ok, stored_wang, np.nan)
            sw_speed = np.abs(np.diff(sw_f, prepend=np.nan)) * frw
            jaw_speed200 = np.abs(np.diff(jaw_f, prepend=np.nan)) * 200
            t = f["intervals/trials"]
            tt = t["trial_type"][:].astype(str)
            st = np.where(tt == "whisker_trial", t["whisker_stim_time"][:],
                          np.where(tt == "auditory_trial", t["auditory_stim_time"][:], t["no_stim_time"][:]))
            rows = []
            for i, s in enumerate(st):
                a0, a1 = np.searchsorted(ts, [s - 2.0, s])
                b0, b1 = np.searchsorted(tsw, [s - 2.0, s])
                with np.errstate(all="ignore"):
                    rows.append((i, np.nanmean(pupil_f[a0:a1]), np.nanmean(jaw_f[a0:a1]), np.nanmean(w_f[b0:b1]),
                                 np.nanmean(jaw_speed[a0:a1]), np.nanmean(w_speed[b0:b1]), np.nanmean(jaw_speed200[a0:a1]),
                                 np.nanmean(stored_pupil[a0:a1]), np.nanmean(sw_f[b0:b1]), np.nanmean(sw_speed[b0:b1])))
            pre = pd.DataFrame(rows, columns=["trial", "pupil", "jaw", "whisker_angle", "jaw_speed", "whisker_speed",
                                              "jaw_speed_x200", "stored_pupil_area", "stored_whisker_angle", "stored_whisker_speed"])
            # jaw traces around the stimulus for Figure 3B-C, 60% likelihood filter
            offs = np.arange(int(round(-0.25 * fr)), int(round(0.3 * fr)) + 1)
            i0 = np.searchsorted(ts, st)
            ok = (i0 + offs[0] >= 0) & (i0 + offs[-1] < len(ts))
            J = np.full((len(st), len(offs)), np.nan, np.float32)
            J[ok] = jaw_f[i0[ok, None] + offs[None, :]]
            signal.alarm(0)
            return session_id, dict(frac=frac, rate=fr, rate_whisker=frw, pre=pre, jaw_t=offs / fr, jaw_traces=J)
        except Exception as e:
            signal.alarm(0)
            err = repr(e)
    return session_id, {"error": err}


def load_dlc(assets, n=8):
    """Per trial pre-stimulus (2 s before the stimulus, the imposed quiet window; Methods, Figures 1I-J)
    means of pupil area (mm2), jaw opening (mm), whisker angle (degrees), jaw and whisker speed, with the
    likelihood filters of the Methods, and stimulus-aligned jaw opening traces (-0.25 to 0.3 s)."""
    res = _pmap(_dlc_one, list(zip(assets.asset_id, assets.session_id)), n=n)
    return dict(res)
