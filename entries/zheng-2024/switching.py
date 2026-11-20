"""Loading and measures for Zheng et al. (2024), "Perpetual step-like restructuring of
hippocampal circuit dynamics", on dandiset 000552.

Where each parameter comes from is said beside it:
- "criterion": the claim's criterion in claims/zheng-2024.yaml (which cites the paper or its code);
- "Methods, <section>": the paper's STAR Methods (author, step 1.6);
- "code, <file>": the paper's code, github.com/samdeoxys1/within-session-representationl-drift,
  tag v0.0, commit 93d6e33d813291e0a5a0dcce39a335fc2d8ce13c (Zenodo doi:10.5281/zenodo.13247193);
- "assumption": a choice the paper leaves open, stated in the attempt record;
- "standard": a detail that cannot change a result.
"""
import json
import zlib
from functools import lru_cache

import h5py
import numpy as np
import pandas as pd
import pynwb
import remfile
import requests
from scipy.ndimage import gaussian_filter1d

DANDISET = "000552"
VERSION = "0.261113.1035"
PAPER = "zheng-2024"
API = "https://api.dandiarchive.org/api"

# Sessions of the paper, from the claims file's opening comment (the code's stored outputs).
FAMILIAR_SESSIONS = {
    "e13_16f1": ["210302", "210312", "210314", "210317", "210319", "210322", "210328", "210331"],
    "e13_26m1": ["210913", "211019", "211116", "211119", "211124"],
    "e14_2m2": ["201017", "201019"],
    "e14_2m3": ["201118", "201121", "201125", "201129", "201206", "201208"],
    "e15_10m1": ["200727", "200803", "200809", "200812"],
    "e15_13f1": ["220117", "220118", "220119", "220120"],
    "e15_9f1": ["200715", "200720", "200723", "200729", "200802"],
    "e16_1f1": ["200918", "200919", "200920", "200923", "201004"],
    "e16_2m1": ["201121"],
    "e16_3m1": ["210119", "210201", "210203"],
    "e16_3m2": ["211210", "211212", "211213"],
}
NOVEL_SESSIONS = ["e13_26m1_211019", "e13_26m1_211116", "e13_26m1_211119", "e15_13f1_220118",
                  "e15_13f1_220119", "e15_13f1_220120", "e16_3m2_211212", "e16_3m2_211213"]
NOVEL_ANIMALS = ["e13_26m1", "e15_13f1", "e16_3m2"]
FAMILIAR_ENVS = ("figure-8 maze", "tmaze_familiar")

BIN_CM = 2.2            # Methods, Ratemap calculation
SMOOTH_BINS = 2.5       # Methods, Ratemap calculation
SPEED_SMOOTH = 10       # Methods, Behavior segmentation (gaussian std 10 position samples)
SPEED_THRESH = 1.0      # Methods, Behavior segmentation (immobility < 1 cm/s)
N_SHUFFLE_FIELD = 1000  # Methods, Place field detection
FIELD_PCT = 0.95        # Methods, Place field detection
FIELD_WIDTH = (4, 30)   # Methods; code place_field_analysis.py measures end - start
FIELD_MIN_PEAK = 1.0    # Methods, Place field detection (Hz)
N_SHUFFLE_SWITCH = 1000  # Methods, Detection of discrete switching
STEP_FRAC = 0.4         # Methods, Detection of discrete switching
CENTRAL_ARM_CM = (15, 74)  # code behavior_and_switching.py and plot_helper.py section bounds
SEGMENT_CUTS = np.array([0, 15, 74, 111, 185, 202, 222])  # code behavior_and_switching.py
SEGMENT_NAMES = ["delay", "central", "choice", "return_side", "pre_delay", "delay"]


def seed(claim, extra=0):
    """The claim's seed (protocol, author step 3)."""
    return zlib.crc32(f"{PAPER}/{claim}".encode()) + extra


@lru_cache(maxsize=1)
def assets():
    out, url = [], f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return {a["path"]: a for a in out}


def session_path(session):
    animal = session.rsplit("_", 1)[0]
    p = f"sub-{animal.replace('_', '-')}/sub-{animal.replace('_', '-')}_ses-{session.replace('_', '-')}_behavior+ecephys.nwb"
    return p if p in assets() else None


def open_nwb(path):
    a = assets()[path]
    url = requests.head(f"{API}/assets/{a['asset_id']}/download/", allow_redirects=True, timeout=60).url
    h = h5py.File(remfile.File(url), "r")
    io = pynwb.NWBHDF5IO(file=h, load_namespaces=True)
    return io.read(), io


def load_session(session):
    """Read what the analyses need from one session, reduced as it loads.

    Returns a dict with the units table (no spikes), spike times of every unit, NREM intervals and
    one entry per maze task with timestamps, linearised position, x and y, and the trials.
    """
    nwb, io = open_nwb(session_path(session))
    u = nwb.units
    cols = ["unit_name", "shank_id", "max_electrode", "putative_cell_type", "firing_rate",
            "light_responsive"]
    units = pd.DataFrame({c: np.asarray(u[c].data[:]).reshape(len(u), -1)[:, 0] for c in cols})
    units["putative_cell_type"] = [x.decode() if isinstance(x, bytes) else str(x) for x in units.putative_cell_type]
    idx = u["spike_times"].data[:]  # the ragged index
    st_all = u["spike_times"].target.data[:]
    spikes = np.split(st_all, idx[:-1])
    ss = nwb.processing["behavior"]["SleepStates"].to_dataframe()
    nrem = ss.loc[ss.label.isin(["NREM", "Non-REM"]), ["start_time", "stop_time"]].values
    ep = nwb.epochs.to_dataframe()
    tr = nwb.trials.to_dataframe()
    lin_d = nwb.processing["behavior"]["LinearizedPosition"].spatial_series
    xy_d = nwb.processing["behavior"]["SubjectPosition"].spatial_series
    tasks = []
    for _, e in ep[ep.task.isin(["alternation", "linearMaze"])].iterrows():
        key = [k for k in lin_d if k.endswith(e.environment) or (len(lin_d) == 1)]
        lin = lin_d[key[0]]
        t = lin.timestamps[:]
        x = lin.data[:].astype(float)
        xk = [k for k in xy_d if k.endswith(e.environment) or len(xy_d) == 1]
        xy = xy_d[xk[0]].data[:].astype(float) if xk else None
        xy_unit = xy_d[xk[0]].unit if xk else None
        trials = tr[(tr.start_time >= e.start_time) & (tr.start_time < e.stop_time)].copy()
        tasks.append(dict(env=e.environment, kind=e.task, start=e.start_time, stop=e.stop_time,
                          familiar=e.environment in FAMILIAR_ENVS, t=t, lin=x, xy=xy,
                          xy_unit=xy_unit, trials=trials.reset_index(drop=True)))
    io.close()
    return dict(session=session, units=units, spikes=spikes, nrem=nrem, tasks=tasks)


# ---------------------------------------------------------------- behaviour

def lin_velocity(t, lin):
    """Velocity of the linearised position, smoothed with a gaussian of 10 samples (Methods,
    Behavior segmentation, applied to the linearised position as the code's directed speed 'v'
    does; the x and y of the novel figure-8 maze have no scale). Jumps of the loop's wrap
    (more than 20 cm in one sample) are removed before smoothing (standard)."""
    dt = np.median(np.diff(t))
    d = np.diff(lin, prepend=lin[0])
    d[np.abs(d) > 20] = 0.0
    v = gaussian_filter1d(d, SPEED_SMOOTH) / dt
    return v, dt


def xy_speed(t, xy):
    """Speed from x and y, velocity smoothed with a gaussian of 10 samples (Methods, Behavior
    segmentation)."""
    dt = np.median(np.diff(t))
    vx = gaussian_filter1d(np.gradient(xy[:, 0]) / dt, SPEED_SMOOTH)
    vy = gaussian_filter1d(np.gradient(xy[:, 1]) / dt, SPEED_SMOOTH)
    return np.sqrt(vx ** 2 + vy ** 2)


def prepare_task(task):
    """Assign frames to trials and trial types, and mark forward locomotion.

    Trial type: the visited arm on the figure-8 maze, the running direction on the linear maze
    (Methods, Place field detection, paragraph 2; code data_prep_pyn.group_into_trialtype). The
    direction of a linear-maze trial is the sign of the net change of linearised position over
    the trial (the files' visited_arm is checked against it). Forward locomotion: directed
    speed above 1 cm/s in the trial's running direction (Methods, Behavior segmentation; code
    speed_key 'v' with speed_thresh 1)."""
    t, lin = task["t"], task["lin"]
    trials = task["trials"]
    frame_trial = np.full(len(t), -1)
    for i, r in trials.iterrows():
        a, b = np.searchsorted(t, [r.start_time, r.stop_time])
        frame_trial[a:b] = i
    v, dt = lin_velocity(t, lin)
    if task["kind"] == "linearMaze":
        dirn = []
        for i in range(len(trials)):
            m = frame_trial == i
            dirn.append("pos" if m.sum() and lin[m][-1] > lin[m][0] else "neg")
        trials["trial_type"] = dirn
        sign = np.where(np.array(dirn)[np.clip(frame_trial, 0, None)] == "pos", 1.0, -1.0)
    else:
        trials["trial_type"] = trials["visited_arm"].values
        sign = np.ones(len(t))
    forward = (frame_trial >= 0) & (v * sign > SPEED_THRESH) & np.isfinite(lin)
    lo, hi = np.nanmin(lin), np.nanmax(lin)
    nbins = int(np.floor((hi - lo) / BIN_CM))  # code data_prep_pyn.add_lin_binned
    edges = np.linspace(lo, hi, nbins + 1)
    pbin = np.clip(np.searchsorted(edges, lin, side="right") - 1, 0, nbins - 1)
    task.update(frame_trial=frame_trial, v=v, dt=dt, forward=forward, nbins=nbins, edges=edges,
                pbin=pbin, speed_sign=sign)
    return task


def spike_frames(t, st):
    """Frame index of each spike (the sample at or before it)."""
    f = np.searchsorted(t, st, side="right") - 1
    return f[(f >= 0) & (f < len(t))]


# ---------------------------------------------------------------- rate maps and fields

def trial_maps(task, spk_frames_list, trial_idx):
    """Per-trial rate maps (cells x trials x bins): counts and occupancy of forward frames per
    trial, each smoothed with a gaussian of 2.5 bins, then divided (Methods, Ratemap
    calculation; code place_cell_analysis.get_fr_map_trial_onegroup, order smooth, divide)."""
    nb, ft, fw, pb, dt = task["nbins"], task["frame_trial"], task["forward"], task["pbin"], task["dt"]
    pos = {tr: k for k, tr in enumerate(trial_idx)}
    ntr = len(trial_idx)
    sel = fw & np.isin(ft, trial_idx)
    tmap = np.array([pos.get(x, 0) for x in ft[sel]])
    occ = np.zeros((ntr, nb))
    np.add.at(occ, (tmap, pb[sel]), 1)
    cnt = np.zeros((len(spk_frames_list), ntr, nb))
    selidx = np.full(len(ft), -1)
    selidx[np.nonzero(sel)[0]] = np.arange(sel.sum())
    for c, f in enumerate(spk_frames_list):
        k = selidx[f]
        k = k[k >= 0]
        np.add.at(cnt[c], (tmap[k], pb[sel][k]), 1)
    occ_s = gaussian_filter1d(occ, SMOOTH_BINS, axis=1)
    cnt_s = gaussian_filter1d(cnt, SMOOTH_BINS, axis=2)
    with np.errstate(invalid="ignore", divide="ignore"):
        fr = np.where(occ_s[None] > 0, cnt_s / (occ_s[None] * dt), 0.0)
    return fr, occ


def pooled_map_and_null(task, f, trial_idx, rng, nshuf=N_SHUFFLE_FIELD):
    """Trial-type map pooled over trials (smoothed summed counts over smoothed summed
    occupancy) and its null from circular shifts of the spike train against position over the
    trial type's frames, shift drawn from 50 to N - 50 (Methods, Place field detection; code
    place_field_analysis.get_fr_map_shuffle and ratemap_from_spk_beh_df_onetrialtype, which
    pool counts over trials for the average map)."""
    nb, ft, fw, pb, dt = task["nbins"], task["frame_trial"], task["forward"], task["pbin"], task["dt"]
    frames = np.nonzero(np.isin(ft, trial_idx))[0]
    N = len(frames)
    loc = np.full(len(ft), -1)
    loc[frames] = np.arange(N)
    k = loc[f]
    k = k[k >= 0]
    fwd = fw[frames]
    pbf = pb[frames]
    occ = np.bincount(pbf[fwd], minlength=nb).astype(float)
    occ_s = gaussian_filter1d(occ, SMOOTH_BINS)
    shifts = np.concatenate([[0], rng.integers(50, N - 50, size=nshuf)])
    kk = (k[None, :] + shifts[:, None]) % N
    ok = fwd[kk]
    rows = np.broadcast_to(np.arange(nshuf + 1)[:, None], kk.shape)[ok]
    cnt = np.zeros((nshuf + 1, nb))
    np.add.at(cnt, (rows, pbf[kk[ok]]), 1)
    cnt_s = gaussian_filter1d(cnt, SMOOTH_BINS, axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        fr = np.where(occ_s[None] > 0, cnt_s / (occ_s[None] * dt), 0.0)
    return fr[0], fr[1:]


def detect_fields(avg, null):
    """Contiguous bins above the 95th percentile of the null, end - start from 4 to 30 bins,
    peak of the average map above 1 Hz (Methods, Place field detection; code
    detect_significant_segments)."""
    thr = np.quantile(null, FIELD_PCT, axis=0)
    sig = avg > thr
    d = np.diff(np.concatenate([[0], sig.astype(int), [0]]))
    starts, ends = np.nonzero(d == 1)[0], np.nonzero(d == -1)[0] - 1
    out = []
    for s, e in zip(starts, ends):
        w = e - s
        if FIELD_WIDTH[0] <= w <= FIELD_WIDTH[1] and avg[s:e + 1].max() > FIELD_MIN_PEAK:
            out.append((s, e, s + int(np.argmax(avg[s:e + 1]))))
    return out, thr


# ---------------------------------------------------------------- change points

def segment_costs(x):
    """x: (P, n). Returns C (P, n+1, n+1): l2 cost of segment [i, j), inf when j - i < 2."""
    P, n = x.shape
    s1 = np.concatenate([np.zeros((P, 1)), np.cumsum(x, 1)], 1)
    s2 = np.concatenate([np.zeros((P, 1)), np.cumsum(x * x, 1)], 1)
    i = np.arange(n + 1)
    L = (i[None, :] - i[:, None]).astype(float)
    with np.errstate(invalid="ignore", divide="ignore"):
        C = (s2[:, None, :] - s2[:, :, None]) - (s1[:, None, :] - s1[:, :, None]) ** 2 / L[None]
    C[:, L < 2] = np.inf
    return C


def optimal_partition(x, kmax, backtrack=False):
    """Optimal partitioning with an l2 cost and minimum segment length 2, as ruptures Dynp
    (Methods, Detection of discrete switching). x: (P, n). Returns costs (P, kmax) for K = 1 ..
    kmax change points and, when backtrack, the change points of row 0 for each K (indices of
    the first trial of each new segment)."""
    C = segment_costs(x)
    P, n1, _ = C.shape
    F = C[:, 0, :].copy()  # cost of one segment ending at j
    costs = np.zeros((P, kmax))
    for k in range(1, kmax + 1):
        F = np.min(F[:, :, None] + C, axis=1)
        costs[:, k - 1] = F[:, n1 - 1]
    cps = None
    if backtrack:
        cps, Fk, Al = {}, C[0, 0, :].copy(), []
        for k in range(1, kmax + 1):
            tot = Fk[:, None] + C[0]
            a = np.argmin(tot, axis=0)
            Fk = tot[a, np.arange(n1)]
            Al.append(a)
        for K in range(1, kmax + 1):
            j, pts = n1 - 1, []
            for k in range(K, 0, -1):
                j = int(Al[k - 1][j])
                pts.append(j)
            cps[K] = sorted(pts)
    return costs, cps


def step_fit(x, cps):
    """Piecewise-constant fit for change points cps (first trial of each new segment)."""
    b = [0] + list(cps) + [len(x)]
    y = np.empty(len(x))
    for a, c in zip(b[:-1], b[1:]):
        y[a:c] = x[a:c].mean()
    return y


def detect_switch(x, rng, nshuf=N_SHUFFLE_SWITCH):
    """Switch detection of one field's per-trial peak rates (Methods, Detection of discrete
    switching): trial order permuted 1000 times, K = 1 .. min(5, floor(n/4)); p for each K the
    fraction of shuffles with a lower cost than the data; significant when the smallest p is
    below 0.05 / number of K (Bonferroni); best K the lowest percentile (ties to the smaller K,
    standard). Switches: steps of the fitted step function divided by its maximum, ON above
    +0.4, OFF below -0.4 (code change_point_analysis.detect_switch_pwc); the variant divides by
    the maximum of the raw per-trial rates."""
    x = np.asarray(x, float)
    n = len(x)
    kmax = min(5, n // 4)
    res = dict(n=n, kmax=kmax, sig=False, K=0, cps=[], on=[], off=[], on_raw=[], off_raw=[])
    if kmax < 1 or np.all(x == x[0]):
        return res
    perms = np.array([rng.permutation(x) for _ in range(nshuf)])
    X = np.vstack([x[None], perms])
    costs, cps = optimal_partition(X, kmax, backtrack=True)
    p = (costs[1:] < costs[0][None]).mean(0)
    res["p"] = p
    res["costs"] = costs[0]
    if p.min() < 0.05 / kmax:
        K = int(np.argmin(p)) + 1
        fit = step_fit(x, cps[K])
        res.update(sig=True, K=K, cps=cps[K], fit=fit)
        for norm, (kon, koff) in ((fit.max(), ("on", "off")), (x.max(), ("on_raw", "off_raw"))):
            if norm <= 0:
                continue
            for c in cps[K]:
                d = (fit[c] - fit[c - 1]) / norm
                if d > STEP_FRAC:
                    res[kon].append(c)
                elif d < -STEP_FRAC:
                    res[koff].append(c)
    return res


def r2_step(x, K):
    """Explained variance ratio of the K-change-point model (code step_vs_gradual_analysis
    fit_cpd_get_r2)."""
    x = np.asarray(x, float)
    costs, cps = optimal_partition(x[None], K, backtrack=True)
    tot = ((x - x.mean()) ** 2).sum()
    return 1 - costs[0, K - 1] / tot if tot > 0 else np.nan


def r2_poly(x, K):
    """Explained variance ratio of an order-K polynomial in trial number, ordinary least
    squares (Methods, Continuous model; statsmodels rsquared equals this)."""
    x = np.asarray(x, float)
    t = np.arange(len(x), dtype=float)
    t = (t - t.mean()) / (t.std() if t.std() > 0 else 1)
    A = np.vander(t, K + 1)
    coef, *_ = np.linalg.lstsq(A, x, rcond=None)
    tot = ((x - x.mean()) ** 2).sum()
    return 1 - ((x - A @ coef) ** 2).sum() / tot if tot > 0 else np.nan


# ---------------------------------------------------------------- one task

def analyse_task(sess, task, rng_field, rng_switch, pyr_mask):
    """Rate maps, place fields and switches for one maze task of one session.

    Returns a dict: per trial type the trial indices, per-trial maps of place cells, and a
    fields table with per-trial peak rate and location of each field and its switches."""
    prepare_task(task)
    t = task["t"]
    units = sess["units"]
    pyr = np.nonzero(pyr_mask)[0]
    sf = [spike_frames(t, sess["spikes"][i]) for i in pyr]
    trials = task["trials"]
    out = dict(trial_types={}, maps={}, fields=[])
    for tt, g in trials.groupby("trial_type"):
        tidx = g.index.values
        fr, occ = trial_maps(task, sf, tidx)
        out["trial_types"][tt] = tidx
        out["maps"][tt] = fr.astype(np.float32)
        for c, i in enumerate(pyr):
            avg, null = pooled_map_and_null(task, sf[c], tidx, rng_field)
            flds, thr = detect_fields(avg, null)
            for (s, e, pk) in flds:
                sub = fr[c][:, s:e + 1]
                out["fields"].append(dict(unit=int(i), cell=c, trial_type=tt, start=s, end=e,
                                          peak_bin=pk, avg_peak=float(avg[pk]),
                                          trials=tidx, rate=sub.max(1),
                                          loc=s + sub.argmax(1).astype(float),
                                          mean_rate=sub.mean(1), thr=thr[s:e + 1].copy(),
                                          avg_map=avg.copy()))
    out["fields"] = merge_central(task, out["fields"])
    return out


def merge_central(task, fields):
    """Turn-common central-arm fields: peaks of the two turns less than 5 bins apart, both on
    the central arm, per-trial peak rates not different by an independent t-test; merged into
    one field over all trials (Methods, Place field detection, paragraph 2). Other central-arm
    fields are splitter fields (flag 'splitter'). On the linear maze nothing is merged."""
    from scipy.stats import ttest_ind
    for f in fields:
        f["merged"] = False
        f["splitter"] = False
    if task["kind"] != "alternation":
        return fields
    edges = task["edges"]
    cbin = np.searchsorted(edges, CENTRAL_ARM_CM) - 1
    on_c = lambda f: cbin[0] <= f["peak_bin"] <= cbin[1]
    types = sorted({f["trial_type"] for f in fields})
    if len(types) != 2:
        return fields
    A = [f for f in fields if f["trial_type"] == types[0] and on_c(f)]
    B = [f for f in fields if f["trial_type"] == types[1] and on_c(f)]
    used_b, merged, drop = set(), [], set()
    for a in A:
        best = None
        for j, b in enumerate(B):
            if b["unit"] != a["unit"] or j in used_b:
                continue
            if abs(a["peak_bin"] - b["peak_bin"]) < 5:
                best = j if best is None or abs(B[best]["peak_bin"] - a["peak_bin"]) > abs(b["peak_bin"] - a["peak_bin"]) else best
        if best is None:
            a["splitter"] = True
            continue
        b = B[best]
        p = ttest_ind(a["rate"], b["rate"]).pvalue
        if p >= 0.05:
            used_b.add(best)
            drop.add(id(a)); drop.add(id(b))
            tr = np.concatenate([a["trials"], b["trials"]])
            o = np.argsort(tr)
            m = dict(unit=a["unit"], cell=a["cell"], trial_type="both", start=min(a["start"], b["start"]),
                     end=max(a["end"], b["end"]), peak_bin=a["peak_bin"],
                     avg_peak=max(a["avg_peak"], b["avg_peak"]), trials=tr[o],
                     rate=np.concatenate([a["rate"], b["rate"]])[o],
                     loc=np.concatenate([a["loc"], b["loc"]])[o],
                     mean_rate=np.concatenate([a["mean_rate"], b["mean_rate"]])[o],
                     thr=a["thr"], avg_map=a["avg_map"], parts=(a, b),
                     merged=True, splitter=False)
            merged.append(m)
        else:
            a["splitter"] = True
    for j, b in enumerate(B):
        if j not in used_b:
            b["splitter"] = True
    return [f for f in fields if id(f) not in drop] + merged


# ---------------------------------------------------------------- whole session

def spatial_information(avg, occ):
    """Skaggs spatial information in bits per spike (standard)."""
    p = occ / occ.sum() if occ.sum() > 0 else occ
    r = (p * avg).sum()
    if r <= 0:
        return 0.0
    with np.errstate(divide="ignore", invalid="ignore"):
        v = np.where(avg > 0, p * avg / r * np.log2(avg / r), 0.0)
    return float(np.nansum(v))


def nrem_rates(sess, idx):
    """Firing rate of each unit during the lab's NREM intervals (SleepStates)."""
    iv = sess["nrem"]
    dur = (iv[:, 1] - iv[:, 0]).sum()
    out = []
    for i in idx:
        st = sess["spikes"][i]
        a = np.searchsorted(st, iv[:, 0])
        b = np.searchsorted(st, iv[:, 1])
        out.append((b - a).sum() / dur if dur > 0 else np.nan)
    return np.array(out)


def trial_segment_behaviour(task):
    """Per trial: mean speed over the trial's forward frames, and per maze segment the mean and
    CV of speed (figure-8 only; segments of code behavior_and_switching.py). Speed is the
    absolute smoothed velocity of the linearised position (see lin_velocity)."""
    ft, v, lin = task["frame_trial"], np.abs(task["v"]), task["lin"]
    rows = []
    seg = np.clip(np.searchsorted(SEGMENT_CUTS, lin, side="right") - 1, 0, len(SEGMENT_NAMES) - 1)
    segname = np.array(SEGMENT_NAMES)[seg]
    for i in range(len(task["trials"])):
        m = ft == i
        mf = m & task["forward"]
        d = dict(trial=i, speed=float(v[mf].mean()) if mf.any() else np.nan,
                 speed_all=float(v[m].mean()) if m.any() else np.nan)
        if task["kind"] == "alternation":
            for s in dict.fromkeys(SEGMENT_NAMES):
                ms = m & (segname == s)
                d[f"speed_{s}"] = float(v[ms].mean()) if ms.any() else np.nan
                d[f"cv_{s}"] = float(v[ms].std() / v[ms].mean()) if ms.any() and v[ms].mean() > 0 else np.nan
        rows.append(d)
    return pd.DataFrame(rows)


def clock_check(sess, task, pyr, shifts=(0.0, 1.0, 5.0, 30.0)):
    """Mean spatial information of the pyramidal cells in the first trial type with the spike
    times as they are and shifted by 1, 5 and 30 s against position: if spikes and position
    share a clock, the unshifted value is the largest (protocol, author step 2)."""
    tt = sorted(task["trials"].trial_type.unique())[0]
    tidx = task["trials"].index[task["trials"].trial_type == tt].values
    sel = np.isin(task["frame_trial"], tidx) & task["forward"]
    occb = np.bincount(task["pbin"][sel], minlength=task["nbins"]).astype(float)
    occ_s = gaussian_filter1d(occb, SMOOTH_BINS)
    out = {}
    for sh in shifts:
        vals = []
        for i in np.nonzero(pyr)[0]:
            f = spike_frames(task["t"], sess["spikes"][i] + sh)
            f = f[sel[f]]
            c = gaussian_filter1d(np.bincount(task["pbin"][f], minlength=task["nbins"]).astype(float), SMOOTH_BINS)
            avg = np.where(occ_s > 0, c / (occ_s * task["dt"]), 0.0)
            vals.append(spatial_information(avg, occb))
        out[sh] = float(np.mean(vals))
    return out


def run_session(session, claim_seed=None):
    """Load one session and run the place-field and switch pipeline on each maze task.

    Seeds: the field shuffles and the switch permutations use the seed of the claim
    fig2d-switch-fractions (the claim that defines fields and switches for all the others),
    plus a per-session offset from the session name so that sessions are independent (the
    seed of a later session does not depend on how many draws an earlier one made)."""
    base = seed("fig2d-switch-fractions") if claim_seed is None else claim_seed
    off = zlib.crc32(session.encode())
    sess = load_session(session)
    units = sess["units"]
    pyr = (units.putative_cell_type == "Pyramidal Cell").values
    res = dict(session=session, animal=session.rsplit("_", 1)[0], units=units,
               nrem_rate=nrem_rates(sess, range(len(units))), tasks=[])
    for ti, task in enumerate(sess["tasks"]):
        rf = np.random.default_rng([base, off, ti, 0])
        rs = np.random.default_rng([base, off, ti, 1])
        o = analyse_task(sess, task, rf, rs, pyr)
        for f in o["fields"]:
            f["sw"] = detect_switch(f["rate"], rs)
        o.update(env=task["env"], kind=task["kind"], familiar=task["familiar"],
                 trials=task["trials"], nbins=task["nbins"], edges=task["edges"],
                 beh=trial_segment_behaviour(task), pyr_units=np.nonzero(pyr)[0])
        # spatial information per pyramidal cell and trial type (pooled map)
        si = {}
        for tt, tidx in o["trial_types"].items():
            fr = o["maps"][tt]
            occ = np.isin(task["frame_trial"], tidx) & task["forward"]
            occb = np.bincount(task["pbin"][occ], minlength=task["nbins"]).astype(float)
            si[tt] = np.array([spatial_information(fr[c].mean(0), occb) for c in range(fr.shape[0])])
        o["si"] = si
        o["task_index"] = ti
        o["clock_check"] = clock_check(sess, task, pyr)
        res["tasks"].append(o)
        if task["xy"] is not None and task["familiar"]:
            o["xy"] = task["xy"].astype(np.float32)
            o["t"] = task["t"]
            o["lin"] = task["lin"].astype(np.float32)
            o["frame_trial"] = task["frame_trial"]
    return res


def all_sessions():
    """The paper's familiar sessions that the dandiset holds, and the novel ones."""
    fam = [f"{a}_{d}" for a, l in FAMILIAR_SESSIONS.items() for d in l]
    return [s for s in fam if session_path(s)], [s for s in fam if not session_path(s)]


def run_all(sessions, workers=4, claim_seed=None):
    """Run run_session over sessions in a pool of processes."""
    from functools import partial
    from multiprocessing import get_context
    with get_context("spawn").Pool(workers) as p:
        return p.map(partial(run_session, claim_seed=claim_seed), sessions)


# ---------------------------------------------------------------- tables over sessions

def iter_tasks(res, novel_sessions=NOVEL_SESSIONS):
    """Yield (record, task) for the paper's familiar tasks and its eight novel tasks."""
    for r in res:
        for o in r["tasks"]:
            if o["familiar"] or r["session"] in novel_sessions:
                yield r, o


def split_parts(fields):
    """Turn-specific series: merged fields are split back into their two turn parts."""
    out = []
    for f in fields:
        out += list(f["parts"]) if f.get("merged") else [f]
    return out


def has_switch(f, raw=False):
    s = f["sw"]
    return bool(s["on_raw"] or s["off_raw"]) if raw else bool(s["on"] or s["off"])


def switch_trials(f, kind="on", raw=False):
    """Session trial indices of a field's switches of one kind ('on' or 'off')."""
    key = kind + ("_raw" if raw else "")
    return [int(f["trials"][c]) for c in f["sw"][key]]


def place_cells(o, tt):
    """Cells (index into the pyramidal list) with a field in trial type tt or a merged field."""
    return sorted({f["cell"] for f in o["fields"] if f["trial_type"] in (tt, "both")})


def pv_corr(maps, cells):
    """Pearson correlation between trial population vectors (concatenated rate maps of the
    cells) for every pair of trials; returns lags and correlations of pairs i < j."""
    X = maps[cells].transpose(1, 0, 2).reshape(maps.shape[1], -1).astype(float)
    C = np.corrcoef(X)
    i, j = np.triu_indices(len(X), 1)
    return j - i, C[i, j]


def lag_slope(lags, vals, lo, hi, min_lags=5):
    """Slope of a linear regression of vals on lag over all pairs with lag in [lo, hi]; None
    when fewer than min_lags distinct lags are present (code pv_corr_analysis.py)."""
    m = (lags >= lo) & (lags <= hi) & np.isfinite(vals)
    if len(np.unique(lags[m])) < min_lags:
        return None
    return float(np.polyfit(lags[m], vals[m], 1)[0])


def cohen_d(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    s = np.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))
    return float((a.mean() - b.mean()) / s)


def vector_cpm_r2(Y, K):
    """Explained variance ratio of a change-point model with K change points shared across the
    columns of Y (trials x features), cost summed over features, minimum segment 2 (Methods,
    Model comparison applied to the population vectors)."""
    n, d = Y.shape
    s1 = np.vstack([np.zeros(d), np.cumsum(Y, 0)])
    s2 = np.concatenate([[0], np.cumsum((Y ** 2).sum(1))])
    i = np.arange(n + 1)
    L = (i[None, :] - i[:, None]).astype(float)
    with np.errstate(invalid="ignore", divide="ignore"):
        S1 = s1[None, :, :] - s1[:, None, :]
        C = (s2[None, :] - s2[:, None]) - (S1 ** 2).sum(2) / L
    C[L < 2] = np.inf
    F = C[0].copy()
    for _ in range(K):
        F = np.min(F[:, None] + C, axis=0)
    tot = ((Y - Y.mean(0)) ** 2).sum()
    return 1 - F[n] / tot


def vector_poly_r2(Y, K):
    t = np.arange(len(Y), dtype=float)
    t = (t - t.mean()) / t.std()
    A = np.vander(t, K + 1)
    coef, *_ = np.linalg.lstsq(A, Y, rcond=None)
    tot = ((Y - Y.mean(0)) ** 2).sum()
    return 1 - ((Y - A @ coef) ** 2).sum() / tot


def passage_times(f):
    """First passage times of each switch of a field (Methods, Switch duration quantification):
    for ON, post: trials from the change point to the first trial above the post-switch
    prediction; pre: trials back from the trial before it to the first trial below the
    pre-switch prediction; mirrored for OFF. None where no crossing exists in the segment."""
    x, fit = np.asarray(f["rate"], float), f["sw"].get("fit")
    out = []
    for kind in ("on", "off"):
        for c in f["sw"][kind]:
            post_thr, pre_thr = fit[c], fit[c - 1]
            nxt = [cc for cc in f["sw"]["cps"] if cc > c] + [len(x)]
            prv = [cc for cc in f["sw"]["cps"] if cc < c]
            lo = prv[-1] if prv else 0
            post = pre = None
            for t in range(c, nxt[0]):
                if (x[t] > post_thr) if kind == "on" else (x[t] < post_thr):
                    post = t - c
                    break
            for t in range(c - 1, lo - 1, -1):
                if (x[t] < pre_thr) if kind == "on" else (x[t] > pre_thr):
                    pre = (c - 1) - t
                    break
            out.append(dict(kind=kind, post=post, pre=pre))
    return out


def trial_rowmap(o):
    """Session trial index -> (trial type, row within the trial type's maps)."""
    d = {}
    for tt, tidx in o["trial_types"].items():
        for k, t in enumerate(tidx):
            d[int(t)] = (tt, k)
    return d


def head_scans(t, xy, lin, frame_trial, frame_turn):
    """Head scans (Methods, Behavior segmentation): track samples from times with speed above
    10 cm/s mapped from linearised to x, y by linear interpolation at 200 evenly spaced
    linearised positions, one track per turn as both turns share the linearised coordinate
    (code data_prep_pyn.find_tmaze_turns samples the turns apart); distance of the head to the
    nearest sample of its trial's track; events where it exceeds 3 cm, extended both ways
    until it is below 1 cm; kept when at least 0.4 s long and the start and end lie within 20
    position bins; merged when less than 0.4 s apart. Returns a list of [start, end] frames."""
    ok = np.all(np.isfinite(xy), 1) & np.isfinite(lin)
    sp = xy_speed(t, np.where(ok[:, None], xy, 0))
    dist = np.full(len(t), np.nan)
    for turn in np.unique(frame_turn[frame_trial >= 0]):
        sel = ok & (frame_turn == turn) & (frame_trial >= 0)
        m = sel & (sp > 10)
        if m.sum() < 50:
            continue
        L, X, Y = lin[m], xy[m, 0], xy[m, 1]
        bins = np.linspace(L.min(), L.max(), 201)
        idx = np.clip(np.searchsorted(bins, L) - 1, 0, 199)
        cnt = np.bincount(idx, minlength=200)
        good = cnt > 0
        mx = np.bincount(idx, X, 200)[good] / cnt[good]
        my = np.bincount(idx, Y, 200)[good] / cnt[good]
        mid = ((bins[:-1] + bins[1:]) / 2)[good]
        q = np.linspace(L.min(), L.max(), 200)
        track = np.stack([np.interp(q, mid, mx), np.interp(q, mid, my)], 1)
        dist[sel] = np.min(np.linalg.norm(xy[sel][:, None, :] - track[None], axis=2), axis=1)
    far = np.nan_to_num(dist) > 3
    on = np.nan_to_num(dist, nan=99) < 1
    events = []
    i, n = 0, len(t)
    while i < n:
        if far[i]:
            a = i
            while a > 0 and not on[a - 1] and frame_trial[a - 1] == frame_trial[i]:
                a -= 1
            b = i
            while b < n - 1 and not on[b + 1] and frame_trial[b + 1] == frame_trial[i]:
                b += 1
            events.append([a, b])
            i = b + 1
        else:
            i += 1
    kept = [e for e in events if (t[e[1]] - t[e[0]]) >= 0.4 and abs(lin[e[1]] - lin[e[0]]) <= BIN_CM * 20]
    merged = []
    for e in kept:
        if merged and t[e[0]] - t[merged[-1][1]] < 0.4:
            merged[-1][1] = e[1]
        else:
            merged.append(list(e))
    return merged
