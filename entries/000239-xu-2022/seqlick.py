"""Loading and measures for dandiset 000239 (Xu et al. 2022, sequence licking).

The files were converted by catalystneuro/oconnor-lab-to-nwb (commit 8d3e9e9). Each file holds a
trial table; the `_behavior.nwb` files add per-trial time series (tongue tracking from the bottom-view
video at about 400 Hz, lick port and force sensor voltages at 1 kHz) and, for recording sessions, a
units table with spike times only. The recorded area and the kind of session are given only by the
session description (the name of the lab's data folder, e.g. "Data ephys ALM").

Where parameters come from:
- 32 um per pixel for the bottom-view video, the 0.84 Lmax point that defines theta_shoot, licks
  shorter than 10 ms dropped, theta used only when L > 1 mm: the paper's Methods ("High-speed
  videography", "Behavioral quantifications").
- Spike rates in 2.5 ms bins smoothed with a 15 ms SD Gaussian, soft normalisation by max(rate, 5 Hz),
  elastic net with alpha 0.1 and the largest lambda within one SE of the minimum 10-fold CV error,
  12 PCs and a linear SVM with balanced class weights: the Methods ("PCA", "Linear regression and
  decoding", "SVM classification").
- Trial selection (feature vectors of lick, touch and port-moving touch histograms in 10 ms bins,
  smoothed with a 20 ms SD Gaussian, the third of trials with the lowest mean pairwise distance, at
  least 10, initiation time under 1 s): the Methods ("Trial selection for standard and backtracking
  sequences").
- Single versus multi-unit: refractory period 2.5 ms, 1% violation threshold, 15% contamination
  threshold by the method of Hill et al. (2011), with the mean rate taken over 1 s bins of at least
  0.5 spikes/s: the Methods ("Electrophysiology"); the 1 s bin and a censored period of 0 are
  choices made here, as the Methods do not give them.
"""

from __future__ import annotations

import os
import re
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
import requests

DANDISET_ID = "000239"
VERSION = "0.230607.1752"
API = "https://api.dandiarchive.org/api"

MM_PER_PX = 0.032          # Methods: 32 um/pixel
REFRACTORY = 0.0025        # Methods: 2.5 ms refractory period
RPV_MAX = 0.01             # Methods: 1% of ISIs
CONTAM_MAX = 0.15          # Methods: 15% contamination
BIN = 0.0025               # Methods: 2.5 ms bins (400 samples/s)
SMOOTH_SD = 0.015          # Methods: 15 ms SD Gaussian

STANDARD = {"[1 2 3 4 5 6]": "LR", "[5 4 3 2 1 0]": "RL"}
BACKTRACK = {"[1 2 3 1 4 5 6]": "LR", "[5 4 3 5 2 1 0]": "RL"}
ZIGZAG = {"[1 2 3 4 3 2 1 0 1 2 3 4]": "A", "[3 2 1 0 1 2 3 4 3 2 1 0]": "B"}


# --- the archive ---------------------------------------------------------------

def list_assets():
    """Every asset of the pinned version, with its path, size, S3 URL and session description."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{VERSION}/assets/"
    params = {"page_size": 500, "metadata": "true"}
    out = []
    while url:
        r = requests.get(url, params=params, timeout=120)
        r.raise_for_status()
        page = r.json()
        for a in page["results"]:
            m = a["metadata"]
            s3 = [u for u in m["contentUrl"] if "s3" in u][0]
            desc = [g.get("description", "") for g in m.get("wasGeneratedBy", [])
                    if g.get("schemaKey") == "Session"][0]
            out.append(dict(path=a["path"], size=a["size"], url=s3, description=desc,
                            subject=m["wasAttributedTo"][0]["identifier"],
                            group=desc.split(" - ")[0], session_start=[
                                g.get("startDate") for g in m["wasGeneratedBy"]
                                if g.get("schemaKey") == "Session"][0]))
        url, params = page["next"], None
    return out


def open_file(url):
    return h5py.File(remfile.File(url), "r")


def _ragged(t, name):
    data = t[name][:]
    idx = t[name + "_index"][:].astype(int)
    starts = np.concatenate([[0], idx[:-1]])
    return [data[a:b] for a, b in zip(starts, idx)]


def read_trials(f):
    """The trial table as a dict of arrays and lists (one entry per trial)."""
    t = f["intervals/trials"]
    cols = [c for c in t.attrs["colnames"]]
    out = {}
    for c in cols:
        if c + "_index" in t:
            out[c] = _ragged(t, c)
        else:
            v = t[c][:]
            if v.dtype.kind in "OS":
                v = np.array([x.decode() if isinstance(x, bytes) else str(x) for x in v])
            out[c] = v
    out["n"] = len(t["id"])
    return out


def read_units(f):
    if "units" not in f:
        return []
    u = f["units"]
    idx = u["spike_times_index"][:].astype(int)
    st = u["spike_times"][:]
    starts = np.concatenate([[0], idx[:-1]])
    return [st[a:b] for a, b in zip(starts, idx)]


VIDEO = ["is_tongue_out", "tongue_bottom_lm_tipX", "tongue_bottom_lm_tipY",
         "tongue_bottom_lm_baseX", "tongue_bottom_lm_baseY"]


def read_video(f):
    """Per trial: start time, rate, tongue-out flag, L (mm) and theta (degrees).

    theta is the angle of the base-to-tip vector from the image's vertical axis (the tongue points
    to lower image y). Its sign follows image x, and the files do not say which side of the image is
    the animal's left; no result here depends on the sign.
    """
    b = f["processing/behavior"]
    g = b["BehavioralTimeSeries_is_tongue_out"]
    n = len(g.keys())
    out = []
    for i in range(n):
        ts = g[f"is_tongue_out_{i}"]
        start = float(ts["starting_time"][()])
        rate = float(ts["starting_time"].attrs["rate"])
        arr = {k: b["BehavioralTimeSeries_" + k][f"{k}_{i}"]["data"][:] for k in VIDEO}
        dx = arr["tongue_bottom_lm_tipX"] - arr["tongue_bottom_lm_baseX"]
        dy = arr["tongue_bottom_lm_baseY"] - arr["tongue_bottom_lm_tipY"]
        out_flag = arr["is_tongue_out"].astype(bool)
        L = np.hypot(dx, dy) * MM_PER_PX
        theta = np.degrees(np.arctan2(dx, dy))
        L[~out_flag] = np.nan
        theta[~out_flag] = np.nan
        out.append(dict(start=start, rate=rate, out=out_flag, L=L.astype(np.float32),
                        theta=theta.astype(np.float32)))
    return out


# --- unit quality --------------------------------------------------------------

def unit_quality(spikes, t0, t1):
    """Refractory period violation rate and contamination (Hill et al. 2011) of one unit."""
    n = len(spikes)
    if n < 2:
        return np.nan, np.nan
    isi = np.diff(spikes)
    viol = int(np.sum(isi < REFRACTORY))
    rpv = viol / len(isi)
    edges = np.arange(t0, t1 + 1, 1.0)
    counts = np.histogram(spikes, edges)[0]
    active = counts >= 0.5
    rate = counts[active].mean() if active.any() else n / (t1 - t0)
    T = n / rate   # duration the unit was active, so that n / T is the rate over active periods
    x = viol * T / (2 * REFRACTORY * n ** 2)
    contam = 1.0 if x >= 0.25 else 0.5 * (1 - np.sqrt(1 - 4 * x))
    return rpv, contam


# --- licks from the video -------------------------------------------------------

def licks_in_trial(v, min_dur=0.010):
    """Tongue-out bouts of one trial: onset, offset, mid time, Lmax and theta_shoot."""
    o = v["out"].astype(int)
    d = np.diff(np.concatenate([[0], o, [0]]))
    on, off = np.where(d == 1)[0], np.where(d == -1)[0]
    rows = []
    for a, b in zip(on, off):
        if (b - a) / v["rate"] < min_dur:
            continue
        L = v["L"][a:b]
        th = v["theta"][a:b]
        if np.all(np.isnan(L)):
            continue
        lmax = np.nanmax(L)
        k = int(np.nanargmax(L >= 0.84 * lmax))
        ok = (L > 1.0) & ~np.isnan(th)
        shoot = th[k] if ok[k] else (th[ok][0] if ok.any() else np.nan)
        rows.append((v["start"] + a / v["rate"], v["start"] + b / v["rate"],
                     v["start"] + (a + b - 1) / 2 / v["rate"], lmax, shoot))
    return np.array(rows).reshape(-1, 5)


# --- sessions -----------------------------------------------------------------

def load_session(asset, video=True, spikes=True):
    """Everything an analysis here needs from one file, reduced as it loads."""
    f = open_file(asset["url"])
    s = dict(asset)
    s["trials"] = read_trials(f)
    s["has_electrodes"] = "general/extracellular_ephys" in f or "electrodes" in f.get("general", {})
    s["unit_columns"] = list(f["units"].attrs["colnames"]) if "units" in f else []
    if video and "processing/behavior" in f:
        vids = read_video(f)
        s["video"] = vids
        s["licks"] = [licks_in_trial(v) for v in vids]
    raw = read_units(f)
    s["duplicate_spikes"] = int(sum(len(u) - len(np.unique(u)) for u in raw))
    bounds = np.sort(np.concatenate([s["trials"]["start_time"], s["trials"]["stop_time"]]))
    dup_t = np.concatenate([u[1:][np.diff(u) == 0] for u in raw]) if raw else np.array([])
    k = np.clip(np.searchsorted(bounds, dup_t), 1, len(bounds) - 1) if len(bounds) > 1 else None
    s["duplicate_boundary_distance"] = (np.minimum(np.abs(dup_t - bounds[k - 1]), np.abs(dup_t - bounds[k]))
                                        if k is not None else np.array([]))
    units = [np.unique(u) for u in raw]   # Methods: duplicated spike times were kept only once
    t0 = float(s["trials"]["start_time"][0]) if s["trials"]["n"] else 0.0
    t1 = float(s["trials"]["stop_time"][-1]) if s["trials"]["n"] else 1.0
    s["n_units"] = len(units)
    s["unit_quality"] = np.array([unit_quality(u, t0, t1) for u in units]).reshape(-1, 2)
    s["n_spikes"] = np.array([len(u) for u in units])
    s["unsorted"] = int(sum(np.any(np.diff(u) < 0) for u in raw))
    if spikes:
        s["spikes"] = units
    f.close()
    return s


def load_many(assets, workers=12, **kw):
    """Load several files in parallel processes (h5py serialises reads within one process)."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_load_kw, [(a, kw) for a in assets]))


def _load_kw(args):
    a, kw = args
    return load_session(a, **kw)


# --- trial events -----------------------------------------------------------------

def trial_events(s, i):
    """Cue, port-moving touches, all touches, water, and the next trial's cue for trial i."""
    t = s["trials"]
    return dict(cue=float(t["cue_times"][i]), pos=np.asarray(t["posIndex_times"][i], float),
                touch=np.asarray(t["lickOn_times"][i], float),
                water=float(t["water_times"][i]) if "water_times" in t else np.nan,
                kind=str(t["posIndex"][i]))


def trial_type(kind):
    if kind in STANDARD:
        return "standard", STANDARD[kind]
    if kind in BACKTRACK:
        return "backtrack", BACKTRACK[kind]
    if kind in ZIGZAG:
        return "zigzag", ZIGZAG[kind]
    return "other", None


def mid_touch(ev):
    """The touch at the middle position: the fourth port-moving touch of a 7-position sequence."""
    return ev["pos"][3] if len(ev["pos"]) >= 4 else np.nan


# --- trial selection ----------------------------------------------------------------

def _gauss_smooth(x, sd_bins, axis=-1):
    from scipy.ndimage import gaussian_filter1d
    return gaussian_filter1d(x.astype(float), sd_bins, axis=axis, mode="constant")


def select_trials(s, trials, align, window, frac=1 / 3, n_min=10):
    """The trials with the most similar lick and touch pattern in `window` around `align`.

    align: one alignment time per trial. Feature vector: histograms (10 ms bins) of lick onsets
    from the video, of all touch onsets, and of port-moving touches, each smoothed by a 20 ms SD
    Gaussian, concatenated. Returns the chosen subset of `trials`.
    """
    trials = list(trials)
    if len(trials) <= n_min:
        return trials
    edges = np.arange(window[0], window[1] + 1e-9, 0.010)
    feats = []
    for i, t0 in zip(trials, align):
        ev = trial_events(s, i)
        lk = s["licks"][i][:, 0] if "licks" in s else np.array([])
        h = [np.histogram(x - t0, edges)[0] for x in (lk, ev["touch"], ev["pos"])]
        feats.append(np.concatenate([_gauss_smooth(np.asarray(x), 2.0) for x in h]))
    X = np.array(feats)
    from scipy.spatial.distance import pdist, squareform
    D = squareform(pdist(X))
    n = max(n_min, int(round(len(trials) * frac)))
    # Greedy: start from the trial closest to all others and add the trial that keeps the mean
    # pairwise distance lowest. The Methods do not say how the subset was searched.
    chosen = [int(np.argmin(D.sum(1)))]
    rest = set(range(len(trials))) - set(chosen)
    while len(chosen) < n:
        r = np.array(sorted(rest))
        k = int(r[np.argmin(D[np.ix_(r, chosen)].sum(1))])
        chosen.append(k)
        rest.remove(k)
    return [trials[k] for k in sorted(chosen)]


# --- spike rates ------------------------------------------------------------------

def rates(spikes, t_grid):
    """Smoothed spike rates (spikes/s) of every unit on a regular grid of BIN steps."""
    edges = np.concatenate([t_grid - BIN / 2, [t_grid[-1] + BIN / 2]])
    R = np.empty((len(spikes), len(t_grid)), np.float32)
    for k, u in enumerate(spikes):
        a, b = np.searchsorted(u, [edges[0] - 0.1, edges[-1] + 0.1])
        R[k] = _gauss_smooth(np.histogram(u[a:b], edges)[0], SMOOTH_SD / BIN) / BIN
    return R


def trial_rates(s, aligns, window, pad=0.1):
    """Rates on a BIN grid in `window` around each alignment time: array trials x units x time."""
    rel = np.arange(window[0], window[1] + BIN / 2, BIN)
    out = []
    for t0 in aligns:
        grid = np.arange(window[0] - pad, window[1] + pad + BIN / 2, BIN) + t0
        R = rates(s["spikes"], grid)
        k = int(round(pad / BIN))
        out.append(R[:, k:k + len(rel)])
    return rel, np.array(out)


def soft_normalise(X):
    """Divide each unit's rate by max(its maximum rate, 5 Hz). X: samples x units."""
    return X / np.maximum(X.max(0), 5.0)


def video_on_grid(v, t):
    """Tongue-out flag, L and theta of one trial sampled at times t (nearest frame)."""
    k = np.round((t - v["start"]) * v["rate"]).astype(int)
    ok = (k >= 0) & (k < len(v["out"]))
    kk = np.clip(k, 0, len(v["out"]) - 1)
    out = np.where(ok, v["out"][kk], False)
    L = np.where(ok, v["L"][kk], np.nan)
    th = np.where(ok, v["theta"][kk], np.nan)
    return out, L, th


# --- models ----------------------------------------------------------------------

def enet_cv_r2(X, y, folds, seed, groups=None, n_alphas=30):
    """10-fold CV elastic net (l1_ratio 0.1) with the one-SE rule; returns (cv R2, weights, intercept).

    folds: number of folds. When `groups` is given the folds keep groups (trials) together;
    otherwise samples are assigned to folds at random, as MATLAB's lasso does by default.
    Predictors are standardised, as MATLAB's lasso does by default; the weights returned are in
    the units of the unstandardised predictors.
    """
    from sklearn.linear_model import enet_path
    from sklearn.model_selection import GroupKFold, KFold
    mu, sd = X.mean(0), X.std(0)
    sd[sd == 0] = 1
    Z = (X - mu) / sd
    yc = y - y.mean()
    amax = np.max(np.abs(Z.T @ yc)) / (len(y) * 0.1)
    alphas = np.logspace(np.log10(amax), np.log10(amax * 1e-4), n_alphas)
    if groups is None:
        splits = KFold(folds, shuffle=True, random_state=seed).split(Z)
    else:
        splits = GroupKFold(folds).split(Z, y, groups)
    mse = []
    for tr, te in splits:
        zm, ym = Z[tr].mean(0), y[tr].mean()
        _, coefs, _ = enet_path(Z[tr] - zm, y[tr] - ym, l1_ratio=0.1, alphas=alphas)
        pred = (Z[te] - zm) @ coefs + ym
        mse.append(((pred - y[te][:, None]) ** 2).mean(0))
    mse = np.array(mse)
    m, se = mse.mean(0), mse.std(0, ddof=1) / np.sqrt(len(mse))
    j = int(np.argmin(m))
    ok = np.where(m <= m[j] + se[j])[0]
    jj = int(ok.min())   # alphas are in decreasing order: the smallest index is the largest lambda
    r2 = 1 - m[jj] / y.var()
    _, coefs, _ = enet_path(Z - Z.mean(0), y - y.mean(), l1_ratio=0.1, alphas=alphas[[jj]])
    w = coefs[:, 0] / sd
    c = y.mean() - X.mean(0) @ w
    return float(r2), w, float(c)


def svm_accuracy(X, y, seed, folds=10):
    """10-fold CV accuracy of a linear SVM with balanced class weights; X trials x features."""
    from sklearn.model_selection import StratifiedKFold, cross_val_predict
    from sklearn.svm import LinearSVC
    clf = LinearSVC(class_weight="balanced", dual="auto", max_iter=5000)
    k = min(folds, np.bincount(y).min())
    pred = cross_val_predict(clf, X, y, cv=StratifiedKFold(k, shuffle=True, random_state=seed))
    w = np.where(y == 1, 0.5 / np.mean(y == 1), 0.5 / np.mean(y == 0))
    return float(np.sum(w * (pred == y)) / np.sum(w))


def canonical_correlations(X, Y):
    """Canonical correlations between the columns of X and Y (samples x dims)."""
    Qx, _ = np.linalg.qr(X - X.mean(0))
    Qy, _ = np.linalg.qr(Y - Y.mean(0))
    return np.clip(np.linalg.svd(Qx.T @ Qy, compute_uv=False), 0, 1)


def group_label(description):
    m = re.match(r"Data (ephys|opto VGAT-CRE Ai32|behav|learning)\s*(.*?) - ", description)
    return m.groups() if m else (None, None)


def cpu_workers():
    return max(4, min(16, 4 * (os.cpu_count() or 1)))


# --- trial sets ------------------------------------------------------------------

def first_touch(ev):
    t = ev["touch"][ev["touch"] >= ev["cue"]]
    return t[0] if len(t) else np.nan


def trials_of(s, ttype, direction, video_window=(-0.5, 0.8), max_init=1.0, need_video=True):
    """Trials of one type and direction, with initiation under `max_init` s and video around the
    middle touch over `video_window`; returns (trials, middle touch times). The video of a trial
    starts at the cue."""
    tr, al = [], []
    for i in range(s["trials"]["n"]):
        ev = trial_events(s, i)
        ty, d = trial_type(ev["kind"])
        if ty != ttype or d != direction:
            continue
        m = mid_touch(ev)
        if np.isnan(m) or not first_touch(ev) - ev["cue"] < max_init:
            continue
        if need_video:
            if i >= len(s.get("video", [])):
                continue
            v = s["video"][i]
            if (m + video_window[0] < v["start"]
                    or m + video_window[1] > v["start"] + len(v["out"]) / v["rate"]):
                continue
        tr.append(i)
        al.append(m)
    return tr, al


def selected(s, ttype, direction, window=(-1.0, 1.0), video_window=(-0.5, 0.8)):
    """Trials chosen by the Methods' selection on `window` around the middle touch."""
    tr, al = trials_of(s, ttype, direction, video_window)
    if not tr:
        return [], []
    ch = select_trials(s, tr, al, window)
    return ch, [al[tr.index(i)] for i in ch]


# --- Figure 3: regression, coding axes, PCA and CCA ---------------------------------

VARS = ["L", "Ldot", "theta", "I", "tau"]


def behaviour_samples(s, trials, aligns, direction, rel):
    """L (0 when the tongue is in), L' and theta (NaN when not observed), I and tau on rel + align."""
    rows = []
    for i, t0 in zip(trials, aligns):
        out, L, th = video_on_grid(s["video"][i], rel + t0)
        Lnan = np.where(out, L, np.nan)
        Ld = np.gradient(Lnan, BIN)
        rows.append(np.c_[np.where(out & ~np.isnan(L), L, 0.0), Ld,
                          np.where(Lnan > 1.0, th, np.nan),
                          np.full(len(rel), 2.0 if direction == "LR" else 1.0), rel,
                          np.full(len(rel), i)])
    return np.concatenate(rows)


def fig3_session(s, seed=0, fit_window=(-0.5, 0.5), window=(-0.5, 0.8), shifts=()):
    """Everything Figure 3 and Extended Data Fig. 5 need from one session."""
    rel = np.arange(window[0], window[1] + BIN / 2, BIN)
    sel = {d: selected(s, "standard", d) for d in ("LR", "RL")}
    out = dict(path=s["path"], area=s["area"], subject=s["subject"], n_units=len(s["spikes"]),
               n_trials={d: len(sel[d][0]) for d in sel},
               n_bt={d: len(selected(s, "backtrack", d)[0]) for d in ("LR", "RL")})
    Xs, Ys = [], []
    for d in ("LR", "RL"):
        tr, al = sel[d]
        if not tr:
            continue
        _, R = trial_rates(s, al, window)
        Xs.append(np.concatenate([r.T for r in R]))
        Ys.append(behaviour_samples(s, tr, al, d, rel))
    X, Y = np.concatenate(Xs), np.concatenate(Ys)
    scale = np.maximum(X.max(0), 5.0)
    Xn = X / scale
    fit = (Y[:, 4] >= fit_window[0]) & (Y[:, 4] <= fit_window[1])
    r2, r2g, W, C = {}, {}, {}, {}
    for j, v in enumerate(VARS):
        ok = fit & ~np.isnan(Y[:, j])
        r2[v], W[v], C[v] = enet_cv_r2(Xn[ok], Y[ok, j], 10, seed)
        r2g[v] = enet_cv_r2(Xn[ok], Y[ok, j], 10, seed, groups=Y[ok, 5])[0]
    out.update(r2=r2, r2_trialfolds=r2g, weights=W)
    # Pairwise correlation of the behavioural variables over the fitting samples.
    corr = {}
    for a in range(5):
        for b in range(a + 1, 5):
            ok = fit & ~np.isnan(Y[:, a]) & ~np.isnan(Y[:, b])
            corr[(VARS[a], VARS[b])] = abs(np.corrcoef(Y[ok, a], Y[ok, b])[0, 1])
    out["corr"] = corr
    # Variance explained by coding axes and by PCs, over the whole window.
    Xc = Xn - Xn.mean(0)
    total = Xc.var(0).sum()
    ve_axes = {}
    for v in VARS:
        w = W[v]
        ve_axes[v] = 0.0 if not np.any(w) else float((Xc @ (w / np.linalg.norm(w))).var() / total)
    _, sv, Vt = np.linalg.svd(Xc, full_matrices=False)
    ve_pc = sv ** 2 / np.sum(sv ** 2)
    out.update(ve_axes=ve_axes, ve_pc5=float(ve_pc[:5].sum()))
    units = [W[v] / np.linalg.norm(W[v]) if np.any(W[v]) else None for v in VARS]
    cos = {}
    for a in range(5):
        for b in range(a + 1, 5):
            if units[a] is not None and units[b] is not None:
                cos[(VARS[a], VARS[b])] = abs(float(units[a] @ units[b]))
    rng = np.random.default_rng(seed)
    rnd = rng.standard_normal((200, Xn.shape[1]))
    rnd /= np.linalg.norm(rnd, axis=1, keepdims=True)
    out.update(cos=cos, cos_random=float(np.abs(np.sum(rnd[::2] * rnd[1::2], 1)).mean()))
    # Trial averages per direction of decoded variables and of PC projections (CCA).
    dec = np.column_stack([Xn @ W[v] + C[v] for v in VARS])
    pcs = Xc @ Vt[:5].T
    avg_dec, avg_pc = [], []
    for code in (2.0, 1.0):
        m = Y[:, 3] == code
        if not m.any():
            continue
        k = np.round((Y[m, 4] - window[0]) / BIN).astype(int)
        cnt = np.bincount(k, minlength=len(rel))[:, None]
        avg_dec.append(np.array([np.bincount(k, dec[m, j], len(rel)) for j in range(5)]).T / cnt)
        avg_pc.append(np.array([np.bincount(k, pcs[m, j], len(rel)) for j in range(5)]).T / cnt)
    A, P = np.concatenate(avg_dec), np.concatenate(avg_pc)
    A = A - A.mean(0)
    out["cca"] = {1: canonical_correlations(A[:, [0, 1, 2]], P[:, :3]).mean(),
                  2: canonical_correlations(A[:, [2, 3, 4]], P[:, :3]).mean(),
                  3: canonical_correlations(A, P[:, :5]).mean()}
    out["mean_traj"] = {"rel": rel, "decoded": A, "dirs": len(avg_dec)}
    # Spike-time shift check (Extended Data Fig. 5a): R2 of L with spikes shifted by each lag.
    if len(shifts):
        okL = fit
        res = {}
        for lag in shifts:
            Xl = []
            for d in ("LR", "RL"):
                tr, al = sel[d]
                if tr:
                    _, R = trial_rates(s, np.asarray(al) + lag, window)
                    Xl.append(np.concatenate([r.T for r in R]))
            Xl = np.concatenate(Xl) / scale
            res[lag] = enet_cv_r2(Xl[okL], Y[okL, 0], 5, seed, groups=Y[okL, 5], n_alphas=10)[0]
        out["shift_r2"] = res
    return out


def run_parallel(fn, items, workers=None):
    with ProcessPoolExecutor(workers or min(4, os.cpu_count() or 1)) as ex:
        return list(ex.map(fn, items))


# --- SVM classification over time ----------------------------------------------------

def _pcs(R, n=12):
    """R: trials x units x time (rates). Soft-normalised rates projected on the first n PCs,
    fitted over all samples: trials x n x time."""
    X = np.concatenate([r.T for r in R])
    scale = np.maximum(X.max(0), 5.0)
    X = X / scale
    mu = X.mean(0)
    _, _, Vt = np.linalg.svd(X - mu, full_matrices=False)
    k = min(n, Vt.shape[0])
    return np.array([(r.T / scale - mu) @ Vt[:k].T for r in R]).transpose(0, 2, 1)


def _bin(P, step):
    """Average consecutive samples: trials x dims x time -> trials x dims x time/step."""
    n = P.shape[2] // step
    return P[:, :, :n * step].reshape(P.shape[0], P.shape[1], n, step).mean(3)


def svm_over_time(P, y, seed, null_bins, n_shuffles=20):
    """Accuracy per time bin, and for each shuffle the accuracy in `null_bins`."""
    rng = np.random.default_rng(seed)
    acc = np.array([svm_accuracy(P[:, :, b], y, seed) for b in range(P.shape[2])])
    null = np.array([[svm_accuracy(P[:, :, b], yy, seed) for b in null_bins]
                     for yy in [rng.permutation(y) for _ in range(n_shuffles)]])
    return acc, null


def backtrack_session(s, seed=0, window=(-0.15, 0.4), n_shuffles=20):
    """Figure 3f: standard against backtracking trials from population activity, per 15 ms bin."""
    rng = np.random.default_rng(seed)
    groups = {}
    for ty in ("standard", "backtrack"):
        for d in ("LR", "RL"):
            tr, al = trials_of(s, ty, d, need_video=False)
            ch = select_trials(s, tr, al, (-1.0, 1.0)) if tr else []
            groups[(ty, d)] = [(i, al[tr.index(i)]) for i in ch]
    trials, labels = [], []
    for code, ty in enumerate(("standard", "backtrack")):
        n = min(len(groups[(ty, "LR")]), len(groups[(ty, "RL")]))
        for d in ("LR", "RL"):
            g = groups[(ty, d)]
            pick = rng.choice(len(g), n, replace=False)
            trials += [g[k] for k in sorted(pick)]
            labels += [code] * n
    y = np.array(labels)
    rel, R = trial_rates(s, [a for _, a in trials], window)
    P = _bin(_pcs(R), 6)                                 # 400 Hz to 66.7 Hz
    t = _bin(rel[None, None, :], 6)[0, 0]
    null_bins = np.where((t >= 0.2) & (t <= 0.4))[0]
    acc, null = svm_over_time(P, y, seed, null_bins, n_shuffles)
    return dict(path=s["path"], area=s["area"], subject=s["subject"], t=t, acc=acc,
                null=null, null_bins=null_bins, n=dict(standard=int((y == 0).sum()),
                                                       backtrack=int((y == 1).sum())))


def zigzag_touches(s, i):
    """The 13 touches of a zigzag trial (12 port-moving touches and the touch at the last
    position), or None when the trial is not executed perfectly (a lick without a touch, or an
    extra touch, between the first and last touch)."""
    ev = trial_events(s, i)
    if len(ev["pos"]) != 12:
        return None
    after = ev["touch"][ev["touch"] > ev["pos"][-1] + 0.05]
    if not len(after):
        return None
    t = np.concatenate([ev["pos"], after[:1]])
    span = (ev["touch"] >= t[0] - 1e-6) & (ev["touch"] <= t[-1] + 1e-6)
    if span.sum() != 13 or i >= len(s.get("licks", [])):
        return None
    v = s["video"][i]
    if t[-1] > v["start"] + len(v["out"]) / v["rate"]:
        return None
    lk = s["licks"][i]
    inside = (lk[:, 0] >= t[0] - 0.1) & (lk[:, 0] <= t[-1] + 0.01)
    if inside.sum() != 13:
        return None
    return t


ZZ_COMPARISONS = [("B", 6, "A", 2), ("B", 6, "A", 10), ("A", 6, "B", 2), ("A", 6, "B", 10)]


def zigzag_session(s, seed=0, half=0.25, n_shuffles=20, null_every=5):
    """Figure 4f,g: sequence identity during matched subsequences, per 5 ms bin."""
    touches = {"A": [], "B": []}
    for i in range(s["trials"]["n"]):
        ty, d = trial_type(trial_events(s, i)["kind"])
        if ty == "zigzag":
            t = zigzag_touches(s, i)
            if t is not None:
                touches[d].append(t)
    out = dict(path=s["path"], subject=s["subject"], n={k: len(v) for k, v in touches.items()}, comps=[])
    for fix, kf, shift, ks in ZZ_COMPARISONS:
        al = [t[kf] for t in touches[fix]] + [t[ks] for t in touches[shift]]
        y = np.array([0] * len(touches[fix]) + [1] * len(touches[shift]))
        rel, R = trial_rates(s, al, (-half, half))
        P = _bin(_pcs(R), 2)                             # 400 Hz to 200 Hz
        t = _bin(rel[None, None, :], 2)[0, 0]
        null_bins = np.arange(0, P.shape[2], null_every)
        acc, null = svm_over_time(P, y, seed, null_bins, n_shuffles)
        out["comps"].append(dict(label=f"fix {fix}{kf}, shift {shift}{ks}", t=t, acc=acc, null=null,
                                 null_bins=null_bins))
    return out


# --- the inter-trial interval ---------------------------------------------------------

def iti_session(s, seed=0, window=(-1.0, 0.0)):
    """Extended Data Fig. 7: upcoming direction (TP) and time to the cue, decoded from the second
    before the cue of every standard trial."""
    trials, al, tp = [], [], []
    for i in range(1, s["trials"]["n"]):
        ev = trial_events(s, i)
        ty, d = trial_type(ev["kind"])
        if ty != "standard":
            continue
        trials.append(i)
        al.append(ev["cue"])
        tp.append(2.0 if d == "LR" else 1.0)
    rel, R = trial_rates(s, al, window)
    X = np.concatenate([r.T for r in R])
    X = X / np.maximum(X.max(0), 5.0)
    y_tp = np.repeat(tp, len(rel))
    y_t = np.tile(rel, len(trials))
    g = np.repeat(trials, len(rel))
    res = dict(path=s["path"], area=s["area"], subject=s["subject"], n_trials=len(trials))
    for name, y in (("TP", y_tp), ("time", y_t)):
        res[name] = enet_cv_r2(X, y, 10, seed)[0]
        res[name + "_trialfolds"] = enet_cv_r2(X, y, 10, seed, groups=g)[0]
    return res


# --- PETHs --------------------------------------------------------------------------

def last_consummatory_touch(s, ev, ili_max):
    """The last touch of the bout that starts with the first touch at or after water delivery."""
    t = ev["touch"][ev["touch"] >= ev["water"]] if not np.isnan(ev["water"]) else []
    if not len(t):
        return np.nan
    k = 0
    while k + 1 < len(t) and t[k + 1] - t[k] < ili_max:
        k += 1
    return t[k]


def session_ili_max(s):
    iti = np.concatenate([np.diff(np.asarray(x)) for x in s["trials"]["lickOn_times"] if len(x) > 1])
    return 1.5 * np.median(iti)


PETH_WINDOWS = {"init": (0.0, 0.5), "mid": (-1.0, 1.0), "term": (-0.5, 0.7)}


def peth_session(s, seed=0):
    """Six PETHs per unit (three periods, two directions), the reward comparison and unit quality."""
    ili_max = session_ili_max(s)
    peth, ntr = {}, {}
    for d in ("LR", "RL"):
        tr, mids = trials_of(s, "standard", d, need_video=False)
        evs = {i: trial_events(s, i) for i in tr}
        aligns = {"init": [evs[i]["cue"] for i in tr], "mid": mids,
                  "term": [last_consummatory_touch(s, evs[i], ili_max) for i in tr]}
        for per, win in PETH_WINDOWS.items():
            ok = [k for k, a in enumerate(aligns[per]) if not np.isnan(a)]
            trs = [tr[k] for k in ok]
            als = [aligns[per][k] for k in ok]
            ch = select_trials(s, trs, als, win) if trs else []
            a2 = [als[trs.index(i)] for i in ch]
            rel, R = trial_rates(s, a2, win)
            peth[(per, d)] = (rel, R.mean(0))
            ntr[(per, d)] = len(ch)
    # Reward: rate before and after the first touch at or after water, all standard trials.
    pre, post = [], []
    for i in range(s["trials"]["n"]):
        ev = trial_events(s, i)
        if trial_type(ev["kind"])[0] != "standard" or np.isnan(ev["water"]):
            continue
        t = ev["touch"][ev["touch"] >= ev["water"]]
        if not len(t):
            continue
        w = t[0]
        pre.append([np.sum((u >= w - 0.5) & (u < w)) for u in s["spikes"]])
        post.append([np.sum((u >= w) & (u < w + 0.5)) for u in s["spikes"]])
    return dict(path=s["path"], area=s["area"], subject=s["subject"], peth=peth, n_trials=ntr,
                quality=s["unit_quality"], reward_pre=np.array(pre) / 0.5, reward_post=np.array(post) / 0.5)


def rhythmicity(rel, peth, freq=6.5):
    """Correlation of a PETH with its best fitting sinusoid of fixed frequency."""
    A = np.c_[np.sin(2 * np.pi * freq * rel), np.cos(2 * np.pi * freq * rel), np.ones_like(rel)]
    coef, *_ = np.linalg.lstsq(A, peth, rcond=None)
    fit = A @ coef
    if np.std(peth) == 0 or np.std(fit) == 0:
        return np.nan
    return float(np.corrcoef(peth, fit)[0, 1])
