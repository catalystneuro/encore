"""Loading and measures for dandiset 000447 (Tang, Shin & Jadhav 2023, Cell Reports 42, 112246).

Each NWB file holds one rat and one day: three W-track epochs (N, F, N' in order, the dandiset's
description), a trials table (one row per trajectory, with start and end well and whether it was
correct), 2D position with a speed column, and sorted units with spike times. Files are streamed
from the archive at the pinned version; nothing is written to disk.

Where the parameters come from (claims file claims/000447/10.1016-j.celrep.2023.112246.yaml,
"criterion" of each claim, and the paper's STAR Methods, quoted as "Methods"):

- Trajectory types follow the paper's code (cal_UMAP.m, GitHub JadhavLab/GeometricTransformation
  at commit 5e55e69): track 1 = well 1 to 2 (OUT_L), 2 = 2 to 1 (IN_L), 3 = 1 to 3 (OUT_R),
  4 = 3 to 1 (IN_R); well 1 is the center (the trials table says so). Linear position is the
  distance from the center well, as in the code.
- Linearization. The Methods project 2D positions "onto pre-defined idealized paths along the
  track"; the paths are not in the dandiset. Assumption: the idealized path of a trajectory type
  in an epoch is the pointwise median of its correct passes, each resampled to equal arc length
  (TEMPLATE_POINTS points) over the samples where the rat moves (speed > MIN_SPEED).
- Run periods: speed > 5 cm/s (Methods, "locomotor periods (> 5 cm/s"); occupancy above 20 ms
  (Methods), which every visited bin passes at 30 frames per second. SWR times cannot be
  excluded: the dandiset holds no ripple times (deviation).
- Bins of 2 cm (Methods). The 1D Gaussian width is garbled in the paper's text ("s = σ cm");
  SMOOTH_CM = 8 is reading (a) of the claims file (fig2d-pv-similarity); 4 and 2 cm are its
  variants. Counts and occupancy are smoothed separately and divided, a standard choice.
- Cell inclusion: more than 100 spikes in the epoch (Methods), CA1 mean rate below 7 Hz
  (poolcells_acrossep.m in the paper's code). The code's per-animal interneuron lists name
  (tetrode, cell) pairs; the files have no cell numbers, so they cannot be applied (see the
  notebook).
- Region of a unit: units/electrodes holds the tetrode number (see the notebook's data check),
  and the region is the `location` of the electrode row whose label is that tetrode.
- Decoding (decode_session): Methods, "Bayesian decoding" (200-ms windows moving with 50 ms
  overlap, run periods, 15 cm from the wells excluded, uniform prior, Poisson); the error along
  the four trajectories laid end to end and the bin rule follow the claims file (the code,
  decoding_position_*_novelfamiliar_cross.m). RATE_FLOOR is a standard choice.
- Manifolds: 201 normalized bins and fewer than 5 active cells dropped (cal_UMAP.m); single-trial
  maps at 1-cm bins (Methods); clusters at 20-30% and 70-80% (cal_all_dichotomies.m); CCGP
  decoders and their permutation test (CCGP_*.m, decoding_CCGP_linearSVM_simple.m); dichotomies
  with 4-fold cross-validation (decoding_dichotomy_linearSVM.m). Filling empty bins of
  single-trial maps is an assumption (single_trial_matrix).
- Statistics: the tests named in the claims file; Dunn's test with Bonferroni adjustment and
  Tukey's test after a repeated-measures ANOVA on its error term, as GraphPad Prism (the paper's
  statistics software) runs them, are standard choices.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "000447"
DANDISET_VERSION = "0.250724.2224"
ANIMALS = ["AM2", "JS17", "JS21", "ZT2", "JS34"]   # order of the paper's code
EPOCHS = ["N", "F", "N'"]
TRACKS = {1: "OUT_L", 2: "IN_L", 3: "OUT_R", 4: "IN_R"}
WELLS_TO_TRACK = {(1, 2): 1, (2, 1): 2, (1, 3): 3, (3, 1): 4}

MIN_SPEED = 5.0        # cm/s, Methods
BIN_CM = 2.0           # Methods
SMOOTH_CM = 8.0        # claims file, fig2d-pv-similarity reading (a)
MIN_SPIKES = 100       # Methods, "at least 100 spikes"; the code uses > 100
CA1_MAX_RATE = 7.0     # Hz, poolcells_acrossep.m
PEAK_HZ = 3.0          # Methods, spatially tuned cell
TEMPLATE_POINTS = 400  # assumption, resolution of the idealized paths (0.5 cm on a 2 m path)
N_NORM_BINS = 101      # cal_PVsimilarity.m, (0:0.01:1)


def _str(v):
    return v.decode() if isinstance(v, bytes) else str(v)


def asset_urls():
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    out = {}
    for a in ds.get_assets():
        name = a.path.split("/")[0].replace("sub-JDS-NFN-", "")
        out[name] = (a.path, a.get_content_url(follow_redirects=1, strip_query=True))
    return out


def load_animal(name, url):
    """Read what the analysis uses from one file: units, position, trials, epochs."""
    f = h5py.File(remfile.File(url), "r")
    d = {"animal": name}
    d["epochs"] = np.c_[f["intervals/epoch intervals/start_time"][:],
                        f["intervals/epoch intervals/stop_time"][:]]
    tr = pd.DataFrame({k: f["intervals/trials/" + k][:] for k in
                       ["start_time", "stop_time", "correct", "trajectory_type", "start_well", "end_well"]})
    tr["epoch"] = [int(np.searchsorted(d["epochs"][:, 0], t, side="right") - 1) for t in tr.start_time]
    tr["track"] = [WELLS_TO_TRACK.get((int(a), int(b)), 0) for a, b in zip(tr.start_well, tr.end_well)]
    d["trials"] = tr
    pos = f["processing/behavior/Position/SpatialSeries/data"][:]
    d["t"] = f["processing/behavior/Position/SpatialSeries/timestamps"][:]
    d["x"], d["y"], d["speed"] = pos[:, 0], pos[:, 1], pos[:, 2]
    d["pos_comments"] = _str(f["processing/behavior/Position/SpatialSeries"].attrs.get("comments", ""))
    d["pos_unit"] = _str(f["processing/behavior/Position/SpatialSeries/data"].attrs.get("unit", ""))
    d["reference_frame"] = _str(f["processing/behavior/Position/SpatialSeries/reference_frame"][()])
    d["session_start"] = _str(f["session_start_time"][()])
    e = f["general/extracellular_ephys/electrodes"]
    labels = [_str(v) for v in e["label"][:]]
    locs = [_str(v) for v in e["location"][:]]
    d["electrode_labels"], d["electrode_locations"] = labels, locs
    ue = f["units/electrodes"][:]
    idx = f["units/spike_times_index"][:]
    st = f["units/spike_times"][:]
    starts = np.r_[0, idx[:-1]]
    d["spikes"] = [st[a:b] for a, b in zip(starts, idx)]
    d["unit_electrode_value"] = ue
    lab2loc = {lab: loc for lab, loc in zip(labels, locs)}
    d["unit_region"] = np.array([lab2loc.get(f"tetrode{v}", "?") for v in ue])
    d["unit_region_rowreading"] = np.array([locs[v] if v < len(locs) else "?" for v in ue])
    d["n_units"] = len(ue)
    return d


def load_all(max_workers=5):
    urls = asset_urls()
    with ThreadPoolExecutor(max_workers) as ex:
        out = list(ex.map(lambda n: load_animal(n, urls[n][1]), ANIMALS))
    return out


# ---------- linearization ----------

def _resample_path(xy, n):
    seg = np.r_[0, np.cumsum(np.hypot(*np.diff(xy, axis=0).T))]
    if seg[-1] <= 0:
        return None
    s = np.linspace(0, seg[-1], n)
    return np.c_[np.interp(s, seg, xy[:, 0]), np.interp(s, seg, xy[:, 1])]


def well_positions(d, ep):
    """Median position of the rat at the end of the trajectories ending at each well."""
    tr = d["trials"]
    out = {}
    for w in (1, 2, 3):
        rows = tr[(tr.epoch == ep) & (tr.end_well == w)]
        j = np.clip(np.searchsorted(d["t"], rows.stop_time.values) - 1, 0, len(d["t"]) - 1)
        out[w] = np.array([np.nanmedian(d["x"][j]), np.nanmedian(d["y"][j])])
    return out


def build_skeleton(d):
    """Idealized W paths per (epoch, track), from the well positions (assumption).

    The three wells lie at the ends of three parallel arms joined by a cross bar. The arm
    direction is perpendicular to the line from the left to the right well, pointing to where the
    rat runs. Each arm lies at the median lateral position of the run samples along the middle of
    the arm (25% to 75% of its length, within 15 cm of the well), and the bar at the median
    position, along the arms, of the run samples beyond 85% of the 99th percentile. Each track
    runs center well, top of center arm, top of side arm, side well, and is oriented from the
    center well for all four tracks (linear position = distance from the center well)."""
    tmpl = {}
    for ep in range(3):
        w = well_positions(d, ep)
        C, Lw, Rw = w[1], w[2], w[3]
        lr = Rw - Lw
        v = lr / np.hypot(*lr)
        u = np.array([-v[1], v[0]])
        m = (d["epoch_of_sample"] == ep) & (d["speed"] > MIN_SPEED)
        xy = np.c_[d["x"][m], d["y"][m]] - C
        pu, pv = xy @ u, xy @ v
        if np.nanmean(pu) < 0:
            u, pu = -u, -pu
        h99 = np.nanpercentile(pu, 99)
        h = np.nanmedian(pu[pu > 0.85 * h99])
        w2 = {}
        for k, P in w.items():
            c_v, c_u = (P - C) @ v, (P - C) @ u
            sel = (pu > 0.25 * h) & (pu < 0.75 * h) & (np.abs(pv - c_v) < 15)
            if sel.sum() > 20:
                c_v = np.nanmedian(pv[sel])
            w2[k] = C + c_v * v + c_u * u
        w = w2
        J = {k: P + (h - (P - C) @ u) * u for k, P in w.items()}
        C = w[1]
        side = {1: 2, 2: 2, 3: 3, 4: 3}
        for track in TRACKS:
            s = side[track]
            tmpl[(ep, track)] = np.array([C, J[1], J[s], w[s]])
        d.setdefault("wells", {})[ep] = w
    return tmpl


def build_templates(d):
    """Idealized path per (epoch, track): pointwise median of the correct passes (variant)."""
    tmpl = {}
    tr = d["trials"]
    for ep in range(3):
        for track in TRACKS:
            rows = tr[(tr.epoch == ep) & (tr.track == track) & (tr.correct == 1)]
            if len(rows) < 2:
                rows = tr[(tr.epoch == ep) & (tr.track == track)]
            paths = []
            for _, r in rows.iterrows():
                m = (d["t"] >= r.start_time) & (d["t"] <= r.stop_time) & (d["speed"] > MIN_SPEED)
                if m.sum() < 10:
                    continue
                p = _resample_path(np.c_[d["x"][m], d["y"][m]], TEMPLATE_POINTS)
                if p is not None:
                    paths.append(p)
            if not paths:
                continue
            med = np.median(np.stack(paths), axis=0)
            # re-sample the median path to equal arc length, oriented from the center well
            med = _resample_path(med, TEMPLATE_POINTS)
            if track in (2, 4):  # inbound: from side well to center; orient from center
                med = med[::-1]
            tmpl[(ep, track)] = med
    return tmpl


def project(xy, path):
    """Arc length along `path` (from its first point) of the nearest point to each of `xy`."""
    seg = np.diff(path, axis=0)
    seglen2 = (seg ** 2).sum(1)
    cum = np.r_[0, np.cumsum(np.sqrt(seglen2))]
    best_d = np.full(len(xy), np.inf)
    best_s = np.zeros(len(xy))
    for i in range(len(seg)):
        v = xy - path[i]
        u = np.clip((v @ seg[i]) / seglen2[i], 0, 1) if seglen2[i] > 0 else np.zeros(len(xy))
        proj = path[i] + u[:, None] * seg[i]
        dist = np.hypot(*(xy - proj).T)
        better = dist < best_d
        best_d[better] = dist[better]
        best_s[better] = cum[i] + u[better] * np.sqrt(seglen2[i])
    return best_s, best_d


def linearize(d, method="skeleton"):
    """Per position sample: epoch, track (0 outside the four types), linear position from the
    center well (cm), distance to the idealized path (cm), and the trial row index."""
    n = len(d["t"])
    epoch = np.full(n, -1)
    for ep, (a, b) in enumerate(d["epochs"]):
        epoch[(d["t"] >= a) & (d["t"] <= b)] = ep
    d["epoch_of_sample"] = epoch
    d["templates"] = build_skeleton(d) if method == "skeleton" else build_templates(d)
    lin = np.full(n, np.nan)
    off = np.full(n, np.nan)
    track = np.zeros(n, int)
    trial = np.full(n, -1)
    for i, r in d["trials"].iterrows():
        m = np.where((d["t"] >= r.start_time) & (d["t"] < r.stop_time))[0]
        trial[m] = i
        if r.track == 0 or (r.epoch, r.track) not in d["templates"]:
            continue
        s, dist = project(np.c_[d["x"][m], d["y"][m]], d["templates"][(r.epoch, r.track)])
        lin[m], off[m], track[m] = s, dist, r.track
    d["lin"], d["lin_offset"], d["track"], d["trial_of_sample"], d["epoch_of_sample"] = lin, off, track, trial, epoch
    d["track_length"] = {k: float(np.sum(np.hypot(*np.diff(v, axis=0).T))) for k, v in d["templates"].items()}
    return d


# ---------- cells ----------

def epoch_counts(d):
    """Spikes and mean rate (spikes over epoch duration) of every unit in every epoch."""
    n = np.zeros((d["n_units"], 3), int)
    for u, s in enumerate(d["spikes"]):
        for ep, (a, b) in enumerate(d["epochs"]):
            n[u, ep] = np.sum((s >= a) & (s <= b))
    dur = d["epochs"][:, 1] - d["epochs"][:, 0]
    return n, n / dur


def included(d, region, ep, min_spikes=MIN_SPIKES, strict=True):
    """Units of `region` that pass the inclusion rules in epoch `ep` (strict: > 100 spikes, as the
    code; otherwise >= 100, as the Methods)."""
    n, rate = epoch_counts(d)
    ok = (n[:, ep] > min_spikes) if strict else (n[:, ep] >= min_spikes)
    ok &= d["unit_region"] == region
    if region == "CA1":
        ok &= rate[:, ep] < CA1_MAX_RATE
    return np.where(ok)[0]


# ---------- rate maps ----------

def _run_mask(d, ep, track=None, trial=None):
    m = (d["epoch_of_sample"] == ep) & (d["speed"] > MIN_SPEED) & np.isfinite(d["lin"])
    if track is not None:
        m &= d["track"] == track
    if trial is not None:
        m &= d["trial_of_sample"] == trial
    return m


def _sample_dt(d):
    dt = np.diff(d["t"], append=d["t"][-1])
    med = np.median(dt)
    return np.clip(dt, 0, 2 * med)


def rate_maps(d, ep, units, smooth_cm=SMOOTH_CM, trial=None, track_only=None, bin_cm=BIN_CM):
    """Occupancy-normalized linearized rate maps on the four tracks for `units` in epoch `ep`.

    Returns {track: (bin_centers_cm, rates[n_units, n_bins])}; NaN where occupancy is zero."""
    dt = _sample_dt(d)
    out = {}
    tracks = [track_only] if track_only else list(TRACKS)
    for track in tracks:
        if (ep, track) not in d["track_length"]:
            continue
        L = d["track_length"][(ep, track)]
        edges = np.arange(0, L + bin_cm, bin_cm)
        centers = edges[:-1] + bin_cm / 2
        m = _run_mask(d, ep, track, trial)
        occ = np.histogram(d["lin"][m], edges, weights=dt[m])[0]
        idx = np.where(m)[0]
        rates = np.full((len(units), len(centers)), np.nan)
        if len(idx) == 0:
            out[track] = (centers, rates)
            continue
        tt = d["t"]
        # each spike takes the sample nearest in time; it counts when that sample is in the mask
        for k, u in enumerate(units):
            s = d["spikes"][u]
            s = s[(s >= tt[idx[0]]) & (s <= tt[idx[-1]] + 0.05)]
            j = np.clip(np.searchsorted(tt, s), 1, len(tt) - 1)
            j -= (s - tt[j - 1]) < (tt[j] - s)
            keep = m[j] & (np.abs(tt[j] - s) < 0.1)
            cnt = np.histogram(d["lin"][j[keep]], edges)[0].astype(float)
            if smooth_cm > 0:
                sig = smooth_cm / bin_cm
                cs = gaussian_filter1d(cnt, sig, mode="constant")
                os_ = gaussian_filter1d(occ, sig, mode="constant")
                with np.errstate(invalid="ignore", divide="ignore"):
                    r = cs / os_
            else:
                with np.errstate(invalid="ignore", divide="ignore"):
                    r = cnt / occ
            r[occ <= 0.02] = np.nan
            rates[k] = r
        out[track] = (centers, rates)
    return out


def normalized(maps, n=N_NORM_BINS, fill_nan=True):
    """Each track's map on `n` bins of normalized length (nearest bin, as cal_PVsimilarity.m),
    interior NaN runs filled linearly; tracks concatenated in the order 1 to 4."""
    pos = np.linspace(0, 1, n)
    cols = []
    for track in TRACKS:
        centers, r = maps[track]
        r = r.copy()
        if fill_nan:
            for k in range(len(r)):
                v = r[k]
                good = np.isfinite(v)
                if good.sum() >= 2:
                    first, last = np.argmax(good), len(v) - 1 - np.argmax(good[::-1])
                    inner = np.arange(first, last + 1)
                    v[inner] = np.interp(inner, np.where(good)[0], v[good])
        p = centers / centers.max()
        j = np.abs(p[None, :] - pos[:, None]).argmin(1)
        cols.append(r[:, j])
    return np.concatenate(cols, axis=1)


def peak_rate(maps):
    return np.nanmax(np.concatenate([maps[t][1] for t in TRACKS], axis=1), axis=1)


# ---------- behaviour: state-space estimate of proportion correct ----------

def state_space_correct(correct, background=1 / 3, n_iter=200, tol=1e-6):
    """Smoothed probability of a correct trial (Smith et al. 2004, J Neurosci 24, 447, ref 84 of
    the paper): a random-walk state x_k with p_k = logistic(mu + x_k), mu set by the background
    probability, the noise variance and initial state fitted by EM. `background` is 1/3 for
    inbound and outbound trials together (cal_behavperform.m in the paper's code)."""
    n = np.asarray(correct, float)
    K = len(n)
    mu = np.log(background / (1 - background))
    sig2, x0 = 0.005, 0.0
    for _ in range(n_iter):
        xp, vp = np.zeros(K), np.zeros(K)
        xf, vf = np.zeros(K), np.zeros(K)
        xprev, vprev = x0, sig2
        for k in range(K):
            xp[k], vp[k] = xprev, vprev + sig2
            x = xp[k]
            for _ in range(50):  # Newton for the posterior mode
                p = 1 / (1 + np.exp(-(mu + x)))
                g = x - xp[k] - vp[k] * (n[k] - p)
                h = 1 + vp[k] * p * (1 - p)
                step = g / h
                x -= step
                if abs(step) < 1e-10:
                    break
            p = 1 / (1 + np.exp(-(mu + x)))
            xf[k], vf[k] = x, 1 / (1 / vp[k] + p * (1 - p))
            xprev, vprev = xf[k], vf[k]
        xs, vs = xf.copy(), vf.copy()
        A = np.zeros(K)
        for k in range(K - 2, -1, -1):
            A[k] = vf[k] / vp[k + 1]
            xs[k] = xf[k] + A[k] * (xs[k + 1] - xp[k + 1])
            vs[k] = vf[k] + A[k] ** 2 * (vs[k + 1] - vp[k + 1])
        cov = np.zeros(K)
        cov[1:] = A[:-1] * vs[1:]
        # initial state: x_0 before the first trial
        A0 = sig2 / (sig2 + sig2) if K else 0
        x0_s = x0 + A0 * (xs[0] - xp[0])
        v0_s = sig2 + A0 ** 2 * (vs[0] - vp[0])
        cov0 = A0 * vs[0]
        terms = vs[1:] + vs[:-1] - 2 * cov[1:] + (xs[1:] - xs[:-1]) ** 2
        t0 = vs[0] + v0_s - 2 * cov0 + (xs[0] - x0_s) ** 2
        new_sig2 = (terms.sum() + t0) / K
        new_x0 = x0_s
        done = abs(new_sig2 - sig2) < tol
        sig2, x0 = new_sig2, new_x0
        if done:
            break
    return 1 / (1 + np.exp(-(mu + xs)))


# ---------- statistics ----------

def rm_anova_tukey(values, names):
    """Repeated-measures one-way ANOVA (rows subjects, columns conditions) with Tukey's test on
    the error term of the ANOVA, as GraphPad Prism runs it after a repeated-measures ANOVA."""
    from scipy import stats
    Y = np.asarray(values, float)
    n, k = Y.shape
    gm = Y.mean()
    ss_cond = n * ((Y.mean(0) - gm) ** 2).sum()
    ss_subj = k * ((Y.mean(1) - gm) ** 2).sum()
    ss_tot = ((Y - gm) ** 2).sum()
    ss_err = ss_tot - ss_cond - ss_subj
    df_c, df_e = k - 1, (k - 1) * (n - 1)
    F = (ss_cond / df_c) / (ss_err / df_e)
    p = stats.f.sf(F, df_c, df_e)
    mse = ss_err / df_e
    rows = []
    for i in range(k):
        for j in range(i + 1, k):
            diff = Y[:, j].mean() - Y[:, i].mean()
            q = abs(diff) / np.sqrt(mse / n)
            pt = stats.studentized_range.sf(q, k, df_e)
            rows.append({"A": names[i], "B": names[j], "mean_B_minus_A": diff, "q": q, "p_tukey": pt})
    return {"F": F, "df": (df_c, df_e), "p": p}, pd.DataFrame(rows)


def anova_tukey(groups, names):
    """One-way ANOVA with Tukey's HSD."""
    from scipy import stats
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    gs = [np.asarray(g, float)[np.isfinite(g)] for g in groups]
    F, p = stats.f_oneway(*gs)
    vals = np.concatenate(gs)
    labs = np.concatenate([[nm] * len(g) for nm, g in zip(names, gs)])
    t = pairwise_tukeyhsd(vals, labs)
    df = pd.DataFrame(t._results_table.data[1:], columns=t._results_table.data[0])
    return {"F": F, "p": p, "n": [len(g) for g in gs]}, df


def kruskal_dunn(groups, names):
    """Kruskal-Wallis with Dunn's test, Bonferroni-adjusted over all pairs (GraphPad's Dunn)."""
    from scipy import stats
    import scikit_posthocs as sp
    gs = [np.asarray(g, float)[np.isfinite(g)] for g in groups]
    H, p = stats.kruskal(*gs)
    dunn = sp.posthoc_dunn(gs, p_adjust="bonferroni")
    dunn.index = names
    dunn.columns = names
    return {"H": H, "p": p, "n": [len(g) for g in gs]}, dunn


def grubbs(x):
    """Two-sided Grubbs' test for one outlier: statistic, p-value (Bonferroni bound on the
    largest studentized deviation, the usual form) and index of the most extreme value."""
    from scipy import stats
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    n = len(x)
    sd = x.std(ddof=1)
    i = int(np.argmax(np.abs(x - x.mean())))
    G = abs(x[i] - x.mean()) / sd
    t2 = n * (n - 2) * G ** 2 / max((n - 1) ** 2 - n * G ** 2, 1e-12)
    p = min(1.0, 2 * n * stats.t.sf(np.sqrt(t2), n - 2))
    return G, p, i


def fisher_z_compare(r1, n1, r2, n2):
    from scipy import stats
    z = (np.arctanh(r1) - np.arctanh(r2)) / np.sqrt(1 / (n1 - 3) + 1 / (n2 - 3))
    return z, 2 * stats.norm.sf(abs(z))


# ---------- selectivity, path equivalence, ramping ----------

def _nearest_interp(src_x, src_y, dst_x):
    j = np.abs(src_x[None, :] - dst_x[:, None]).argmin(1)
    return src_y[j]


def selectivity(maps, k, peak_rule=">="):
    """SI(IN) and SI(OUT) of row k, as cal_SI.m: right map interpolated (nearest) to the left
    map's bins, means over bins valid on both; NaN unless the peak rate passes 3 Hz on the IN
    pair and on the OUT pair (Methods "≥ 3"; cal_SI.m "> 3" when peak_rule is ">")."""
    out = []
    for left, right in ((2, 4), (1, 3)):
        cl, rl = maps[left]
        cr, rr = maps[right]
        a = rl[k]
        b = _nearest_interp(cr / cr.max(), rr[k], cl / cl.max())
        ok = np.isfinite(a) & np.isfinite(b)
        if ok.sum() == 0:
            return np.nan, np.nan
        m1, m2 = a[ok].mean(), b[ok].mean()
        pk = max(a[ok].max(), b[ok].max())
        good = pk >= PEAK_HZ if peak_rule == ">=" else pk > PEAK_HZ
        if not good:
            return np.nan, np.nan
        out.append((m1 - m2) / (m1 + m2) if (m1 + m2) > 0 else np.nan)
    return out[0], out[1]


def path_equivalence(maps, k):
    """Median over the 6 track pairs of the Pearson r of maps aligned from start to end
    (cal_path_equivalence.m: inbound maps reversed, interpolated to the first track's bins,
    NaN bins dropped)."""
    c1 = maps[1][0]
    pm = c1 / c1.max()
    cols = []
    for track in TRACKS:
        c, r = maps[track]
        p = c / c.max()
        v = r[k]
        if track in (2, 4):
            p = 1 - p
        good = np.isfinite(v)
        if good.sum() < 2:
            return np.nan
        order = np.argsort(p[good])
        cols.append(np.interp(pm, p[good][order], v[good][order], left=np.nan, right=np.nan))
    M = np.array(cols).T
    ok = np.isfinite(M).all(1)
    rs = []
    for i in range(4):
        for j in range(i + 1, 4):
            a, b = M[ok, i], M[ok, j]
            rs.append(np.corrcoef(a, b)[0, 1] if a.std() > 0 and b.std() > 0 else np.nan)
    return np.nanmedian(rs)


def ramping(maps, k, track):
    """Ramping toward reward (Methods): Pearson r > 0.5 and p < 0.05 of rate against traversed
    position, peak rate >= 3 Hz, peak within 20 cm of the reward (the trajectory's end)."""
    from scipy import stats
    c, r = maps[track]
    v = r[k]
    traversed = c if track in (1, 3) else c.max() + BIN_CM / 2 - c
    good = np.isfinite(v)
    if good.sum() < 3 or np.nanmax(v) < PEAK_HZ or v[good].std() == 0:
        return False, np.nan, np.nan, bool(good.sum() >= 3)
    rr, p = stats.pearsonr(traversed[good], v[good])
    end = traversed.max()
    peak_at = traversed[good][np.argmax(v[good])]
    ok = (rr > 0.5) and (p < 0.05) and (end - peak_at <= 20)
    return ok, rr, p, True


# ---------- Bayesian decoding ----------

RATE_FLOOR = 1e-4  # Hz, standard choice so that log rates are finite where a template is 0


def decode_session(d, ep, units, template_maps, window=0.2, step=0.15, min_speed=MIN_SPEED,
                   well_cm=15.0, restrict_track=False, min_active=1, n_shuffles=100, rng=None):
    """Memoryless Bayesian decoder (Methods, "Bayesian decoding"): Poisson spiking, uniform prior
    over position and trajectory type, templates = `template_maps` (N' maps). Time bins of
    `window` s every `step` s in epoch `ep`; a bin is decoded when all its position samples lie
    on one trajectory type, the mean speed exceeds `min_speed`, the position is more than
    `well_cm` from a well, and at least `min_active` cells fire. The error is the distance along
    the four trajectories laid end to end (a decode onto the wrong trajectory is far), in the
    N' coordinates (the session's position scaled by the ratio of trajectory lengths); with
    `restrict_track` the decode is restricted to the current trajectory (the code's variant).
    Returns a DataFrame of bins with the error, and the errors under cell-ID shuffles of the
    templates (one shuffle, and the median over `n_shuffles`)."""
    rng = rng or np.random.default_rng(0)
    tracks = list(TRACKS)
    Ls = [template_maps[t][0].max() + BIN_CM / 2 for t in tracks]
    offsets = np.r_[0, np.cumsum(Ls)[:-1]]
    F = np.concatenate([np.nan_to_num(template_maps[t][1], nan=0.0) for t in tracks], axis=1)
    F = np.maximum(F, RATE_FLOOR)
    pos_track = np.concatenate([[t] * template_maps[t][1].shape[1] for t in tracks])
    pos_x = np.concatenate([template_maps[t][0] for t in tracks])
    pos_cat = np.concatenate([template_maps[t][0] + o for t, o in zip(tracks, offsets)])
    a, b = d["epochs"][ep]
    centers = np.arange(a + window / 2, b - window / 2, step)
    tt = d["t"]
    i0 = np.searchsorted(tt, centers - window / 2)
    i1 = np.searchsorted(tt, centers + window / 2)
    rows = []
    keep = []
    for k, (u, v) in enumerate(zip(i0, i1)):
        if v <= u:
            continue
        trk = d["track"][u:v]
        if trk[0] == 0 or not np.all(trk == trk[0]):
            continue
        if np.nanmean(d["speed"][u:v]) <= min_speed:
            continue
        lin = np.nanmean(d["lin"][u:v])
        L_ep = d["track_length"][(ep, int(trk[0]))]
        if not np.isfinite(lin) or lin < well_cm or lin > L_ep - well_cm:
            continue
        keep.append(k)
        rows.append((centers[k], int(trk[0]), lin, lin / L_ep, int(d["trial_of_sample"][u])))
    if not rows:
        return pd.DataFrame(), None
    df = pd.DataFrame(rows, columns=["t", "track", "lin", "frac", "trial"])
    edges_lo, edges_hi = df.t.values - window / 2, df.t.values + window / 2
    N = np.zeros((len(df), len(units)))
    for j, uidx in enumerate(units):
        s = d["spikes"][uidx]
        N[:, j] = np.searchsorted(s, edges_hi) - np.searchsorted(s, edges_lo)
    active = (N > 0).sum(1)
    ok = active >= min_active
    df, N = df[ok].reset_index(drop=True), N[ok]
    tri = np.array([tracks.index(t) for t in df.track])
    x_act = df.frac.values * np.array(Ls)[tri]
    act_cat = offsets[tri] + x_act

    def errors(Fm):
        ll = N @ np.log(Fm) - window * Fm.sum(0)[None, :]
        if restrict_track:
            ll = np.where(pos_track[None, :] == df.track.values[:, None], ll, -np.inf)
            j = ll.argmax(1)
            return np.abs(pos_x[j] - x_act)
        j = ll.argmax(1)
        return np.abs(pos_cat[j] - act_cat)

    df["error"] = errors(F)
    shuf = np.empty((len(df), n_shuffles))
    for s_ in range(n_shuffles):
        shuf[:, s_] = errors(F[rng.permutation(F.shape[0])])
    df["error_shuffle1"] = shuf[:, 0]
    df["error_shuffle_median"] = np.median(shuf, axis=1)
    return df, shuf


# ---------- single-trial maps and the pseudo-population ----------

def single_trial_matrix(d, ep, units, trials_by_track, n_bins=201, smooth_cm=SMOOTH_CM, bin_cm=1.0,
                        fill_gaps=True):
    """Single-trial linearized rate maps (bins of `bin_cm`, 1 cm in the Methods) of `units`,
    interpolated (nearest) to `n_bins` bins of normalized length, as cal_UMAP.m does (NaN set to
    0). In one pass many 1-cm bins hold no position sample at 30 frames per second; with
    `fill_gaps` (an assumption) the empty bins inside the visited stretch are filled linearly,
    as cal_PVsimilarity.m fills session maps, so that no animal's block of cells is set to 0 at
    a bin the rat ran through. Returns rows of states (track, trial number, bin) by cells, and
    their labels."""
    pos = np.linspace(0, 1, n_bins)
    X, lab = [], []
    for track, rows in trials_by_track.items():
        for tj, ti in enumerate(rows):
            m = rate_maps(d, ep, units, smooth_cm=smooth_cm, trial=ti, track_only=track, bin_cm=bin_cm)
            c, r = m[track]
            if fill_gaps:
                r = r.copy()
                good = np.isfinite(r[0]) if len(r) else np.array([])
                if good.sum() >= 2:
                    first, last = np.argmax(good), len(good) - 1 - np.argmax(good[::-1])
                    inner = np.arange(first, last + 1)
                    for k in range(len(r)):
                        r[k, inner] = np.interp(inner, np.where(good)[0], r[k, good])
            r = np.nan_to_num(r, nan=0.0)
            j = np.abs((c / c.max())[None, :] - pos[:, None]).argmin(1)
            X.append(r[:, j].T)
            lab.append(np.c_[np.full(n_bins, track), np.full(n_bins, tj), np.arange(n_bins)])
    return np.vstack(X), np.vstack(lab)


def trials_of_track(d, ep):
    tr = d["trials"]
    return {t: list(tr[(tr.epoch == ep) & (tr.track == t)].index) for t in TRACKS}


# ---------- CCGP and dichotomies ----------

EARLY_BINS = np.arange(40, 60)    # 20% to 30% of the normalized position (cal_all_dichotomies.m, id1 = 41:60)
LATE_BINS = np.arange(140, 160)   # 70% to 80% (id2 = 141:160)


def clusters(E, lab):
    """The 8 clusters: states of each track at 20-30% ('a') and 70-80% ('b') of the normalized
    position from the center well (cal_all_dichotomies.m)."""
    out = {}
    for t in TRACKS:
        for seg, bins in (("a", EARLY_BINS), ("b", LATE_BINS)):
            out[(t, seg)] = E[(lab[:, 0] == t) & np.isin(lab[:, 2], bins)]
    return out


def _phase_class(t, seg):
    # outbound: 'a' is early (1), 'b' late (2); inbound runs toward the center, so the reverse
    if t in (1, 3):
        return 1 if seg == "a" else 2
    return 2 if seg == "a" else 1


SEQ_ROWS = [(1, 3, "a"), (4, 2, "a"), (1, 3, "b"), (4, 2, "b")]   # CCGP_taskSeq.m testing_sets


def _other(seg):
    return "b" if seg == "a" else "a"


def ccgp_sets(CN, CF=None, seq_same_phase=False):
    """Training and test sets of the 16 CCGP decoders (CCGP_trajPhase.m, CCGP_taskSeq.m,
    CCGP_environment.m). With `seq_same_phase` the two clusters of a task-sequence row are taken
    at the same segment (a variant)."""
    from itertools import combinations
    sets = []

    def stack(C, items):
        X = np.vstack([C[k] for k, _ in items])
        y = np.concatenate([[c] * len(C[k]) for k, c in items])
        return X, y

    phase_train = []
    for tr in combinations(TRACKS, 3):
        test = [t for t in TRACKS if t not in tr][0]
        items = [((t, s), _phase_class(t, s)) for t in tr for s in "ab"]
        titems = [((test, s), _phase_class(test, s)) for s in "ab"]
        sets.append(("phase", f"test {TRACKS[test]}", stack(CN, items), stack(CN, titems)))
        phase_train.append((tr, items))

    def seq_items(row):
        p, q, seg = row
        return [((p, seg), 1), ((q, seg if seq_same_phase else _other(seg)), 2)]

    seq_train = []
    for i, row in enumerate(SEQ_ROWS):
        trows = [SEQ_ROWS[j] for j in ((1, 3) if i in (0, 2) else (0, 2))]
        items = sum([seq_items(r) for r in trows], [])
        sets.append(("sequence", f"test {TRACKS[row[0]]}/{TRACKS[row[1]]} {row[2]}", stack(CN, items), stack(CN, seq_items(row))))
        seq_train.append((row, items))
    if CF is not None:
        for tr, items in phase_train:
            sets.append(("environment", "phase, train " + "+".join(TRACKS[t] for t in tr), stack(CN, items), stack(CF, items)))
        for row, items in seq_train:
            sets.append(("environment", f"sequence, held out {TRACKS[row[0]]}/{TRACKS[row[1]]} {row[2]}", stack(CN, items), stack(CF, items)))
    return sets


def balanced_accuracy(y, p):
    return 0.5 * (np.mean(p[y == 1] == 1) + np.mean(p[y == 2] == 2))


def svm_ccgp(train, test, n_perm=1000, rng=None):
    """Linear C-SVM (libsvm through scikit-learn, C = 1, as `-s 0 -t 0`), balanced accuracy on
    the test set, and the trial-label permutation test of decoding_CCGP_linearSVM_simple.m
    (train and test labels shuffled; p = fraction of shuffles above the real value)."""
    from sklearn.svm import SVC
    rng = rng or np.random.default_rng(0)
    (Xtr, ytr), (Xte, yte) = train, test
    acc = balanced_accuracy(yte, SVC(kernel="linear", C=1.0).fit(Xtr, ytr).predict(Xte))
    null = np.empty(n_perm)
    for i in range(n_perm):
        m = SVC(kernel="linear", C=1.0).fit(Xtr, rng.permutation(ytr))
        null[i] = balanced_accuracy(rng.permutation(yte), m.predict(Xte))
    return acc, null, float(np.mean(null > acc))


def run_ccgp(CN, CF, n_perm=1000, seed=0, n_jobs=4, **kw):
    """All 16 decoders of one region with their permutation tests (one generator per decoder)."""
    from joblib import Parallel, delayed
    sets = ccgp_sets(CN, CF, **kw)
    res = Parallel(n_jobs=n_jobs)(delayed(svm_ccgp)(tr, te, n_perm, np.random.default_rng([seed, i]))
                                  for i, (_, _, tr, te) in enumerate(sets))
    return pd.DataFrame([{"variable": k, "decoder": nm, "ccgp": a, "null_95": np.percentile(nl, 95),
                          "null_median": np.median(nl), "p": p, "p_ge": float(np.mean(nl >= a))}
                         for (k, nm, _, _), (a, nl, p) in zip(sets, res)])


def ccgp_values(CN, CF):
    """CCGP of the 16 decoders without permutations (for the geometric null)."""
    from sklearn.svm import SVC
    out = []
    for kind, nm, (Xtr, ytr), (Xte, yte) in ccgp_sets(CN, CF):
        out.append((kind, balanced_accuracy(yte, SVC(kernel="linear", C=1.0).fit(Xtr, ytr).predict(Xte))))
    return pd.DataFrame(out, columns=["variable", "ccgp"])


def permute_noise(C, rng):
    """Geometric random model (Methods): each cluster's noise cloud (its points about the
    centroid) has the axes of its space permuted, separately for each cluster."""
    out = {}
    for k, X in C.items():
        c = X.mean(0)
        out[k] = c + (X - c)[:, rng.permutation(X.shape[1])]
    return out


def dichotomies():
    """The 35 balanced dichotomies of the 8 clusters (each split counted once)."""
    from itertools import combinations
    keys = [(t, s) for t in TRACKS for s in "ab"]
    out = []
    for comb in combinations(range(8), 4):
        if 0 in comb:
            out.append(([keys[i] for i in comb], [keys[i] for i in range(8) if i not in comb]))
    return out


def _cv_acc(X, y, rng):
    from sklearn.model_selection import StratifiedKFold, cross_val_predict
    from sklearn.svm import SVC
    order = rng.permutation(len(y))
    X, y = X[order], y[order]
    pred = cross_val_predict(SVC(kernel="linear", C=1.0), X, y, cv=StratifiedKFold(4))
    return float(np.mean(pred == y))


def decode_dichotomy(C, groups, n_perm, seed):
    """4-fold cross-validated linear C-SVM accuracy (libsvm `-v 4` reports the fraction of
    correct predictions) and the trial-label permutation test (decoding_dichotomy_linearSVM.m)."""
    rng = np.random.default_rng(seed)
    g1, g2 = groups
    X = np.vstack([C[k] for k in g1 + g2])
    y = np.concatenate([[1] * len(C[k]) for k in g1] + [[2] * len(C[k]) for k in g2])
    acc = _cv_acc(X, y, rng)
    null = np.array([_cv_acc(X, rng.permutation(y), rng) for _ in range(n_perm)])
    return acc, float(np.mean(null > acc)), null
