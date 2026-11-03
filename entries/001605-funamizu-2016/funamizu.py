"""Loading and measures for dandiset 001605 (Funamizu, Kuhn & Doya 2016, Nat Neurosci 19:1682).

The dandiset holds one NWB file per imaging session: the green/red ratio R and dR/R of every
ROI, the virtual position, locomotion speed, lick frequency and rewards, all on one 30.9 Hz
clock, and a trial table (start, condition, start-to-goal distance). Files are streamed from
the archive with remfile and h5py; nothing is written to disk.

Where each parameter comes from:
- Moving averages of 500 ms (15 frames, the nearest odd count to 15.45) for time-aligned and
  8.37 cm (20 bins of 0.42 cm) for distance-aligned activity, the threshold P < 1e-10 of a
  one-sided one-sample t-test, and the 16 frames before the goal used for k-means: claims file,
  opening comment (Online Methods, "Task-relevant neurons").
- Windows of the aligned traces: claims file, O2 (start -1 to 6 s, goal time -3 to 3 s, goal
  distance 67 to 0 cm then 0 to 3 s, first lick -2 to 3 s, start distance 0 to 67 or 0 to 33 cm).
- Baselines of the t-test: claims file, O1, (a) zero and (b) the neuron's mean dR/R over the
  inter-trial intervals. The inter-trial interval is taken as the last 7 s of each trial record
  ("The inter-trial interval (ITI) was 7 s", Online Methods, Behavioral training); the records
  run from one start tone to the next and last 7.9 to 8.0 s past the reward.
- Trials: the 150 trials of each file; trials over 20 s to reward and trials without reward are
  excluded (Online Methods, Behavioral analysis). The first lick is the first lick more than
  33 cm from the start (same passage).
- Distance-aligned activity: dR/R is linearly interpolated at 0.42 cm bin centres from the
  frames between the start and the goal, using the running maximum of the position so that it
  is monotonic. This is a standard choice: the paper bins every 0.42 cm, and at 15 to 25 cm/s
  most 0.42 cm bins hold no frame of their own.
- Licks: the files hold a lick frequency (1/inter-lick interval, capped at 10 Hz, held between
  licks), not lick times. A lick count over a stretch is the integral of this frequency over
  time; a lick onset is a frame where the frequency changes to a non-zero value or stays at
  the 10 Hz cap. These are standard choices forced by the data's form.
- Decoder: claims file, opening comment (Online Methods, "Probabilistic decoding of goal
  distance"): 3-frame moving average, 4.2 cm bins of continuous trials, Gaussian smoothing of
  s.d. 4.2 cm, resampling every 0.84 cm, flat prior, leave-one-trial-out for continuous trials.
  The positive shift is O7 (minimum 0.01 or 0.1). The decoded range is 67.2 to 0 cm (O8; 16
  bins of 4.2 cm).
- Single-basis regressions (Supplementary Fig. 6): equation (3) with the centre at the value of
  maximal averaged activity (Online Methods, Regression analysis); the free width is profiled
  over a grid of 25 values and refined by a bounded optimizer between the neighbouring grid
  values (an assumption standing in for four optimizer starts); sound intensity
  100 dB SPL at 25 cm, 6 dB lower per doubling (Online Methods, Behavioral training); readings of
  frames (O6) and of the intensity below 25 cm from the claims file.
"""
from __future__ import annotations

import numpy as np
import h5py
import remfile
import requests
from scipy import optimize, sparse, stats
from scipy.ndimage import uniform_filter1d, gaussian_filter1d

DANDISET = "001605"
VERSION = "0.251007.0553"
API = "https://api.dandiarchive.org/api"
FS = 30.9                       # frames per second (imaging and behaviour share it)
PX_CM = 36 / 430                # cm per virtual position unit (trial table description)
ITI_S = 7.0                     # inter-trial interval, Online Methods
MAX_REWARD_S = 20.0             # trials slower than this are excluded, Online Methods
LICK_START_CM = 33.0            # first lick counts only beyond 33 cm from the start
SMOOTH_T = 15                   # 500 ms in frames
DBIN = 0.42                     # cm
SMOOTH_D = 20                   # 8.37 cm in 0.42 cm bins
NDB = 160                       # 0.42 cm bins over 67.2 to 0 cm
DCENT = DBIN * (np.arange(NDB) + 0.5)          # bin centres, cm from the goal (or start)
ZONES = [(58.6, 41.9), (41.9, 25.1), (25.1, 8.4), (8.4, 0.0)]
P_TASK = 1e-10
WIN = {  # frames relative to the anchor
    "start": np.arange(int(-1 * FS), int(6 * FS) + 1),
    "goal": np.arange(int(-3 * FS), int(3 * FS) + 1),
    "lick": np.arange(int(-2 * FS), int(3 * FS) + 1),
}
AFTER = np.arange(0, int(3 * FS) + 1)          # 0 to 3 s after the goal, for the joined trace


# ---------------------------------------------------------------- archive

def assets():
    """Paths and asset ids of the pinned version, sorted by path."""
    out, url = [], f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    while url:
        d = requests.get(url, timeout=60).json()
        out += [(a["path"], a["asset_id"], a["size"]) for a in d["results"]]
        url = d["next"]
    return sorted(out)


def open_asset(asset_id):
    url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(url), "r")


def sound_zone(gdist, sdist, state):
    """True where sound plays, from the condition and the distances (Online Methods): zones of
    17 cm (borders 8.4, 25.1, 41.9, 58.6 cm ... from the goal); in intermittent 1 a no-sound zone
    is centred on the goal, in intermittent 2 a sound zone; the first 33 cm always have sound."""
    k = np.floor((gdist + 8.375) / 16.75).astype(int)   # zone index, 0 is centred on the goal
    if np.ndim(state) == 0:
        state = np.full(np.shape(gdist), state)
    on = np.ones(np.shape(gdist), bool)
    on[state == 1] = (k[state == 1] % 2) == 1
    on[state == 2] = (k[state == 2] % 2) == 0
    on |= sdist < 33.0
    return on


# ---------------------------------------------------------------- loading

def load_session(path, asset_id, dff=True):
    """Read one session. Returns a dict with metadata, per-frame behaviour, the trial table with
    derived events, and optionally dR/R (frames x ROIs, float32)."""
    f = open_asset(asset_id)
    ip = f["general/optophysiology/ImagingPlane"]
    area, layer = ip["description"][()].decode().split(", Layer ")
    b = f["processing/behavior"]
    pos = b["VirtualMovement/move_scan/data"][:, 0] * PX_CM
    lick = b["Licking/lick_rate/data"][:]
    conv = b["Speed/speed_x/data"].attrs["conversion"]
    speed = b["Speed/speed_x/data"][:] * conv * 100.0            # cm/s
    sound = b["Sound/sound_on_off/data"][:]
    rew_t = b["Reward/reward_times/timestamps"][:]
    tr = f["intervals/trials"]
    nfr = tr["frames"][:].astype(int)
    t0 = tr["start_time"][:]
    s0 = np.r_[0, np.cumsum(nfr)[:-1]]
    gd = tr["goal_distance_cm"][:]
    state = tr["state"][:].astype(int)
    T = len(pos)
    trial_of = np.repeat(np.arange(len(nfr)), nfr)
    gdist = gd[trial_of] - pos
    # events per trial
    goal_f = np.full(len(nfr), -1)
    rew_f = np.full(len(nfr), -1)
    lick_f = np.full(len(nfr), -1)
    onset = (lick > 0) & ((np.r_[0, np.diff(lick)] != 0) | (lick >= 10))
    for k in range(len(nfr)):
        a, e = s0[k], s0[k] + nfr[k]
        g = np.flatnonzero(pos[a:e] >= gd[k])
        if len(g):
            goal_f[k] = a + g[0]
        r = rew_t[(rew_t >= t0[k]) & (rew_t < t0[k] + nfr[k] / FS)]
        if len(r):
            rew_f[k] = a + int(round((r[0] - t0[k]) * FS))
        lk = np.flatnonzero(onset[a:e] & (pos[a:e] > LICK_START_CM))
        if len(lk):
            lick_f[k] = a + lk[0]
    reward_s = np.where(rew_f >= 0, (rew_f - s0) / FS, np.nan)
    valid = (goal_f >= 0) & (rew_f >= 0) & (reward_s <= MAX_REWARD_S)
    out = dict(
        path=path, subject=f["general/subject/subject_id"][()].decode(), area=area, layer=int(layer),
        date=f["session_start_time"][()].decode()[:10], n_rois=f["processing/ophys/DfOverF/dF_over_F/data"].shape[1],
        T=T, pos=pos, gdist=gdist, lick=lick, speed=speed, sound=sound, trial_of=trial_of,
        trials=dict(s0=s0, nfr=nfr, gd=gd, state=state, goal_f=goal_f, rew_f=rew_f, lick_f=lick_f,
                    reward_s=reward_s, valid=valid, t0=t0),
        n_speaker_rows=len(f["intervals/speaker_presentations/start_time"]),
        checks=_file_checks(f, t0, nfr, T, rew_t),
    )
    if dff:
        out["dff"] = f["processing/ophys/DfOverF/dF_over_F/data"][:].astype(np.float32)
    f.close()
    return out


def _file_checks(f, t0, nfr, T, rew_t):
    """Checks of the file against its description (verifier round 1): where the rows of
    speaker_presentations fall relative to the trial starts and how long they last, whether
    the trial table's frames sum to the series length, and the sampling rate of each series."""
    sp = f["intervals/speaker_presentations"]
    st, et = sp["start_time"][:], sp["stop_time"][:]
    near = np.abs(st[:, None] - t0[None, :]).min(1)
    per_trial = np.bincount(np.searchsorted(t0, st + 1e-9) - 1, minlength=len(t0))
    b = f["processing/behavior"]
    rates = {k: float(b[k]["starting_time"].attrs["rate"]) for k in
             ("VirtualMovement/move_scan", "Licking/lick_rate", "Sound/sound_on_off", "Speed/speed_x")}
    ophys = f["processing/ophys/DfOverF/dF_over_F"]
    rates["dF_over_F"] = float(ophys["starting_time"].attrs["rate"]) if "starting_time" in ophys else float("nan")
    spk = f["stimulus/presentation/speaker_on_matrix/data"][:] != 0         # frames x speakers (verifier round 2)
    spk_on = np.flatnonzero(spk.any(1))
    return dict(speaker_matrix_shape=tuple(int(v) for v in spk.shape), speaker_matrix_on_frames=int(len(spk_on)),
                speaker_matrix_on_at_trial_start=int(np.isin(spk_on, np.r_[0, np.cumsum(nfr)[:-1]]).sum()),speaker_start_to_trial_start_max_s=float(near.max()),
                speaker_durations_s=sorted(set(np.round(et - st, 5).tolist())),
                speaker_unique_starts=int(len(np.unique(st))),
                speaker_rows_per_trial=(int(per_trial.min()), int(per_trial.max())),
                speaker_ids=sorted(set(sp["speaker_id"][:].tolist())),
                frames_sum_equals_T=bool(int(nfr.sum()) == T),
                trial_start_vs_frames_max_s=float(np.abs(np.diff(t0) - nfr[:-1] / FS).max()),
                rates=rates, n_reward_timestamps=int(len(rew_t)))


# ---------------------------------------------------------------- behaviour

def lick_bins(s, edges):
    """Licks per trial in goal-distance bins (edges descending, cm from the goal): the integral
    of the lick frequency over the frames between the start and the goal falling in each bin."""
    tr = s["trials"]
    out = np.full((len(tr["gd"]), len(edges) - 1), np.nan)
    for k in np.flatnonzero(tr["valid"]):
        a, g = tr["s0"][k], tr["goal_f"][k]
        gdist = s["gdist"][a:g + 1]
        lk = s["lick"][a:g + 1] / FS
        idx = np.digitize(gdist, edges[::-1])      # ascending edges
        cnt = np.bincount(idx, weights=lk, minlength=len(edges) + 1)[1:len(edges)][::-1]
        out[k] = cnt
        out[k, edges[:-1] > tr["gd"][k]] = np.nan  # bins the trial never covered
    return out


def zone_times(s):
    """Time spent per no-sound zone, per trial, under the two readings of behaviour-timing:
    (a) complete no-sound zones after the first 33 cm and before the goal; (b) every no-sound
    zone entered, including the one around the goal (intermittent 1) up to the reward."""
    tr = s["trials"]
    ra, rb = [], []
    for k in np.flatnonzero(tr["valid"] & (tr["state"] > 0)):
        a, g, r = tr["s0"][k], tr["goal_f"][k], tr["rew_f"][k]
        gdist = s["gdist"][a:r + 1]
        sdist = s["pos"][a:r + 1]
        kz = np.floor((gdist + 8.375) / 16.75).astype(int)
        silent = ~sound_zone(gdist, sdist, tr["state"][k])
        st = tr["state"][k]
        for z in np.unique(kz[silent]):
            on = silent & (kz == z)
            t = on.sum() / FS
            lo, hi = z * 16.75 - 8.375, z * 16.75 + 8.375   # zone extent, cm from the goal
            complete = (lo >= 0) and (tr["gd"][k] - hi >= 33.0)
            if complete:
                ra.append(t)
            rb.append(t)
    return np.array(ra), np.array(rb)


# ---------------------------------------------------------------- neurons

def _ttest_logp(x, base, axis=0):
    """One-sided one-sample t-test of x > base along axis (NaNs ignored); log10 P."""
    n = np.sum(~np.isnan(x), axis=axis)
    m = np.nanmean(x, axis=axis)
    sd = np.nanstd(x, axis=axis, ddof=1)
    t = (m - base) / (sd / np.sqrt(n))
    return stats.t.logsf(t, n - 1) / np.log(10), m


def _gather(dff, anchors, offs):
    idx = anchors[:, None] + offs[None, :]
    ok = (idx >= 0) & (idx < len(dff))
    x = dff[np.clip(idx, 0, len(dff) - 1)]          # trials x points x neurons
    x[~ok] = np.nan
    return x


def _dist_traces(s, trials, frm="goal", nb=NDB):
    """Per trial dR/R interpolated at 0.42 cm bins of goal distance (67.2 to 0) or of distance
    from the start (0 to nb*0.42), frames from the start to the goal. trials x bins x neurons."""
    tr, dff = s["trials"], s["dff"]
    out = np.full((len(trials), nb, dff.shape[1]), np.nan, np.float32)
    for j, k in enumerate(trials):
        a, g = tr["s0"][k], tr["goal_f"][k]
        p = np.maximum.accumulate(s["pos"][a:g + 1])
        p[-1] = max(p[-1], tr["gd"][k])
        x = tr["gd"][k] - DCENT[:nb] if frm == "goal" else DCENT[:nb]   # start-distance of centres
        good = (x >= p[0]) & (x <= p[-1])
        # keep one frame per position value so the interpolation is defined
        pu, iu = np.unique(p, return_index=True)
        fi = np.interp(x[good], pu, iu.astype(float))
        lo = np.floor(fi).astype(int)
        w = (fi - lo)[:, None]
        hi = np.minimum(lo + 1, g - a)
        out[j, good] = dff[a + lo] * (1 - w) + dff[a + hi] * w
    return out


def neuron_stats(s):
    """Per-neuron statistics for the classification (claims file, opening comment, O1 to O4).
    Returns a dict of arrays over neurons, and per-neuron condition traces."""
    tr, dff = s["trials"], s["dff"]
    N = dff.shape[1]
    v = np.flatnonzero(tr["valid"])
    # baseline (b): mean dR/R over the last 7 s of each trial record (inter-trial interval)
    iti = np.concatenate([np.arange(tr["s0"][k] + tr["nfr"][k] - int(ITI_S * FS), tr["s0"][k] + tr["nfr"][k])
                          for k in range(len(tr["gd"]))])
    base = {"a": np.zeros(N), "b": dff[iti].mean(0)}
    res = dict(base_b=base["b"])
    # time-aligned
    traces = {}
    for name, anch in (("start", tr["s0"][v]), ("goal", tr["goal_f"][v]),
                       ("lick", tr["lick_f"][v][tr["lick_f"][v] >= 0])):
        x = uniform_filter1d(_gather(dff, anch, WIN[name]), SMOOTH_T, axis=1, mode="nearest")
        for bk, bv in base.items():
            lp, m = _ttest_logp(x, bv[None, :])
            res[f"lp_{name}_{bk}"] = np.nanmin(lp, axis=0)
            if name == "start":     # start neurons: significant within 2 s of the start
                tw = (WIN["start"] >= 0) & (WIN["start"] <= 2 * FS)
                res[f"lp_start2s_{bk}"] = np.nanmin(lp[tw], axis=0)
        traces[name] = m
    # distance-aligned
    xd = _dist_traces(s, v, "goal")
    xs = _dist_traces(s, v, "start")
    sm = lambda a: uniform_filter1d(a, SMOOTH_D, axis=1, mode="nearest")
    xds, xss = sm(np.nan_to_num(xd, nan=0)), sm(np.nan_to_num(xs, nan=0))
    # smoothing must not invent values where a trial has no data: restore NaN there
    xds[np.isnan(xd)] = np.nan
    xss[np.isnan(xs)] = np.nan
    for bk, bv in base.items():
        lp, m = _ttest_logp(xds, bv[None, :])
        res[f"lp_dist_{bk}"] = np.nanmin(lp, axis=0)
        lp2, _ = _ttest_logp(xss, bv[None, :])
        res[f"lp_sdist67_{bk}"] = np.nanmin(lp2, axis=0)
        n33 = int(round(33 / DBIN))
        res[f"lp_sdist33_{bk}"] = np.nanmin(lp2[:n33], axis=0)
    dist_mean = np.nanmean(xds, axis=0)                        # bins x neurons, 67.2 -> 0 reversed below
    dist_mean = dist_mean[::-1]                                # index 0 = 67.0 cm, last = 0.2 cm
    gi = np.searchsorted(WIN["goal"], 0)
    after = traces["goal"][gi + AFTER]                         # 0 to 3 s after the goal
    joined = np.vstack([dist_mean, after])
    pk = np.nanargmax(joined, axis=0)
    res["peak_after"] = pk >= NDB
    res["dist_pref"] = DCENT[::-1][np.nanargmax(dist_mean, axis=0)]
    g = traces["goal"]
    gn = (g - np.nanmin(g, 0)) / (np.nanmax(g, 0) - np.nanmin(g, 0))
    res["pre16"] = gn[gi - 16:gi].T                            # neurons x 16, normalized 0..1
    res["joined"] = joined.T.astype(np.float32)
    # per-condition trial-averaged traces, 0.42 cm bins (raw interpolation), goal distance ascending
    cond = np.full((N, 3, NDB), np.nan, np.float32)
    for c in range(3):
        sel = tr["state"][v] == c
        if sel.sum():
            cond[:, c] = np.nanmean(xd[sel], axis=0).T
    res["cond"] = cond
    # per-condition distance preference (smoothed), for supp9
    cs = uniform_filter1d(np.nan_to_num(cond), SMOOTH_D, axis=2, mode="nearest")
    cs[np.isnan(cond)] = np.nan
    res["cond_pref"] = np.where(np.all(np.isnan(cs), axis=2), np.nan,
                                DCENT[np.nanargmax(np.nan_to_num(cs, nan=-np.inf), axis=2)])
    return res


def decoder_inputs(s, neurons):
    """Frames used by the decoder: valid trials, from the start to the goal, goal distance 0 to
    67.2 cm. Activity is dR/R after a 3-frame moving average (Online Methods)."""
    tr = s["trials"]
    v = np.flatnonzero(tr["valid"])
    sm = uniform_filter1d(s["dff"][:, neurons], 3, axis=0, mode="nearest")
    fr = np.concatenate([np.arange(tr["s0"][k], tr["goal_f"][k] + 1) for k in v])
    fr = fr[(s["gdist"][fr] >= 0) & (s["gdist"][fr] < NDB * DBIN)]
    t = s["trial_of"][fr]
    return dict(n=sm[fr].astype(np.float32), x=s["gdist"][fr], trial=t, state=tr["state"][t],
                time=(fr - tr["s0"][t]) / FS, speed=s["speed"][fr], neurons=np.asarray(neurons),
                min_all=s["dff"][:, neurons].min(0) if len(neurons) else np.zeros(0),
                sdist=s["pos"][fr])


# ---------------------------------------------------------------- decoder

XB = 4.2
NXB = 16
GRID = 0.84 * np.arange(81)                      # 0 to 67.2 cm every 0.84 cm


def _interp_matrix():
    """Linear interpolation from the 16 bin centres to the 0.84 cm grid, as a matrix."""
    xc = XB * (np.arange(NXB) + 0.5)
    return np.array([np.interp(GRID, xc, np.eye(NXB)[j]) for j in range(NXB)]).T   # grid x bins


_IM = None


def _tuning(cnt, s1, s2, eps=1e-6):
    """Per-bin mean and s.d. (maximum likelihood) from counts and sums, smoothed with a
    Gaussian of s.d. one bin (4.2 cm) and resampled every 0.84 cm."""
    global _IM
    if _IM is None:
        _IM = _interp_matrix()
    c = np.maximum(cnt, 1)[:, None]
    mu = s1 / c
    var = np.maximum(s2 / c - mu ** 2, eps)
    mu = gaussian_filter1d(mu, 1.0, axis=0, mode="nearest")
    sd = gaussian_filter1d(np.sqrt(var), 1.0, axis=0, mode="nearest")
    return _IM @ mu, _IM @ sd                      # grid x neurons


def _posterior(y, mu, sd):
    """Log-likelihood of Gaussian y (frames x neurons) under each grid point; flat prior."""
    iv = 1.0 / sd ** 2                                   # grid x neurons
    ll = -0.5 * ((y ** 2) @ iv.T - 2 * y @ (mu * iv).T + (mu ** 2 * iv).sum(1)[None]) - np.log(sd).sum(1)[None]
    ll -= ll.max(1, keepdims=True)
    p = np.exp(ll)
    return p / p.sum(1, keepdims=True)


def _outputs(p, x):
    rmse = np.sqrt((p * (GRID[None] - x[:, None]) ** 2).sum(1))
    mp = GRID[np.argmax(p, 1)]
    unc = np.sqrt((p * (GRID[None] - mp[:, None]) ** 2).sum(1))
    return rmse, mp, unc


def decode(d, shift=0.01, likelihood="lognormal", permute=None, rng=None):
    """Decode goal distance for every frame of d. Continuous trials by leave-one-trial-out,
    intermittent trials by a decoder trained on all continuous trials. Returns RMSE, MAP and
    uncertainty per frame. permute: train with the distance traces of the training trials
    permuted across trials (matched by fraction of the trial's frames), a chance reading."""
    n = d["n"]
    if likelihood == "lognormal":
        y = np.log(n - d["min_all"][None, :] + shift)
    else:
        y = n.astype(float)
    x = d["x"].copy()
    trials = d["trial"]
    cont = d["state"] == 0
    if permute:
        ut = np.unique(trials[cont])
        perm = rng.permutation(ut)
        for a, b in zip(ut, perm):
            ia, ib = np.flatnonzero(trials == a), np.flatnonzero(trials == b)
            x[ia] = np.interp(np.linspace(0, 1, len(ia)), np.linspace(0, 1, len(ib)), d["x"][ib])
    xb = np.clip((x / XB).astype(int), 0, NXB - 1)
    ut = np.unique(trials[cont])
    # per-trial sufficient statistics of continuous trials
    tix = {t: i for i, t in enumerate(ut)}
    m = cont
    key = np.array([tix[t] for t in trials[m]]) * NXB + xb[m]
    M = sparse.csr_matrix((np.ones(m.sum()), (key, np.arange(m.sum()))), shape=(len(ut) * NXB, m.sum()))
    C = np.asarray(M.sum(1)).reshape(len(ut), NXB)
    S1 = (M @ y[m]).reshape(len(ut), NXB, -1)
    S2 = (M @ (y[m] ** 2)).reshape(len(ut), NXB, -1)
    Ct, S1t, S2t = C.sum(0), S1.sum(0), S2.sum(0)
    rmse = np.full(len(x), np.nan); mp = rmse.copy(); unc = rmse.copy()
    for t in ut:
        i = tix[t]
        mu, sd = _tuning(Ct - C[i], S1t - S1[i], S2t - S2[i])
        m = trials == t
        p = _posterior(y[m], mu, sd)
        rmse[m], mp[m], unc[m] = _outputs(p, d["x"][m])
    mu, sd = _tuning(Ct, S1t, S2t)
    m = ~cont
    if m.any():
        p = _posterior(y[m], mu, sd)
        rmse[m], mp[m], unc[m] = _outputs(p, d["x"][m])
    return rmse, mp, unc


def flat_rmse(x):
    """RMSE of the flat prior over the decoded grid, at the actual distance x."""
    return np.sqrt(((GRID[None] - x[:, None]) ** 2).mean(1))


# ---------------------------------------------------------------- statistics helpers

def zone_slope(dist, y):
    """Slope of y against approach (y = b0 - b1 distance), so a positive b1 means y rises (or,
    for MAP and uncertainty, falls when the sign is flipped by the caller) toward the goal."""
    ok = ~np.isnan(y)
    if ok.sum() < 3 or np.ptp(dist[ok]) == 0:
        return np.nan
    return -np.polyfit(dist[ok], y[ok], 1)[0]


def wilcoxon_z(x, y=None, alternative="two-sided"):
    """Wilcoxon signed-rank P and normal-approximation z, dropping NaNs."""
    d = np.asarray(x, float) if y is None else np.asarray(x, float) - np.asarray(y, float)
    d = d[~np.isnan(d)]
    d = d[d != 0]
    if len(d) < 1:
        return np.nan, np.nan, 0
    r = stats.wilcoxon(d, alternative=alternative, method="approx")
    n = len(d)
    rk = stats.rankdata(np.abs(d))
    wp = rk[d > 0].sum()
    z = (wp - n * (n + 1) / 4) / np.sqrt(n * (n + 1) * (2 * n + 1) / 24)
    return r.pvalue, z, n


def mwu(a, b, alternative="two-sided"):
    """Mann-Whitney U P and z (positive when a tends to exceed b), dropping NaNs."""
    a = np.asarray(a, float); b = np.asarray(b, float)
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    if len(a) < 1 or len(b) < 1:
        return np.nan, np.nan
    r = stats.mannwhitneyu(a, b, alternative=alternative, method="asymptotic")
    n1, n2 = len(a), len(b)
    z = (r.statistic - n1 * n2 / 2) / np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
    return r.pvalue, z


# ---------------------------------------------------------------- one pass per session

LICK_EDGES = XB * np.arange(32, -1, -1)          # 134.4 to 0 cm, 4.2 cm bins (Fig. 1c)


def lick_zone_slopes(s):
    """Per trial, for each zone of ZONES that is silent in its condition, the slope of lick
    frequency on time (Lick(t) = b0 + b1 t, Supplementary Fig. 1) and the mean speed there."""
    tr = s["trials"]
    nt = len(tr["gd"])
    slope = np.full((nt, len(ZONES)), np.nan)
    spd = np.full((nt, len(ZONES)), np.nan)
    for k in np.flatnonzero(tr["valid"] & (tr["state"] > 0)):
        a, g = tr["s0"][k], tr["goal_f"][k]
        gdist = s["gdist"][a:g + 1]
        silent = ~sound_zone(gdist, s["pos"][a:g + 1], tr["state"][k])
        for z, (hi, lo) in enumerate(ZONES):
            m = (gdist <= hi) & (gdist > lo) & silent
            if m.sum() >= 3:
                t = np.flatnonzero(m) / FS
                slope[k, z] = np.polyfit(t, s["lick"][a:g + 1][m], 1)[0]
                spd[k, z] = s["speed"][a:g + 1][m].mean()
    return slope, spd


def summarize(s):
    """Everything the notebook needs from one session, without the full activity matrix."""
    tr = s["trials"]
    nt = len(tr["gd"])
    trial_speed = np.array([s["speed"][tr["s0"][k]:tr["goal_f"][k] + 1].mean() if tr["goal_f"][k] >= 0 else np.nan
                            for k in range(nt)])
    lick_to_reward = np.array([s["lick"][tr["s0"][k]:tr["rew_f"][k] + 1].sum() / FS if tr["rew_f"][k] >= 0 else np.nan
                               for k in range(nt)])
    ls, lsp = lick_zone_slopes(s)
    za, zb = zone_times(s)
    out = dict(meta={k: s[k] for k in ("path", "subject", "area", "layer", "date", "n_rois", "T", "n_speaker_rows")},
               trials=tr, trial_speed=trial_speed, lick_bins=lick_bins(s, LICK_EDGES),
               lick_slope=ls, lick_slope_speed=lsp, zone_a=za, zone_b=zb,
               first_lick_cm=np.where(tr["lick_f"] >= 0, s["pos"][np.maximum(tr["lick_f"], 0)], np.nan),
               first_lick_any_cm=first_lick_any(s),
               first_lick_bout_cm=first_lick_bout(s),
               lick_form=lick_form(s),
               checks=s["checks"],
               sound_frames=int((s["sound"] > 0).sum()),
               sound_at_start=int((s["sound"][tr["s0"]] > 0).sum()),
               ranges=dict(pos=(float(s["pos"].min()), float(s["pos"].max())),
                           speed=(float(np.percentile(s["speed"], 1)), float(np.percentile(s["speed"], 99))),
                           lick=(float(s["lick"].min()), float(s["lick"].max()))))
    if "dff" in s:
        ns = neuron_stats(s)
        cand = np.flatnonzero((np.minimum(ns["lp_goal_a"], ns["lp_dist_a"]) < np.log10(P_TASK)) |
                              (np.minimum(ns["lp_goal_b"], ns["lp_dist_b"]) < np.log10(P_TASK)))
        out["neurons"] = ns
        out["dec"] = decoder_inputs(s, cand)
        out["reg"] = regressions(s, cand) if len(cand) else {}
        out["ranges"]["dff"] = (float(np.percentile(s["dff"], 0.1)), float(np.percentile(s["dff"], 99.9)))
        out["ranges"]["dff_session_mean_absmax"] = float(np.abs(s["dff"].mean(0)).max())
    return out


def process(path, asset_id):
    for attempt in range(3):
        try:
            return summarize(load_session(path, asset_id))
        except OSError:
            if attempt == 2:
                raise


def first_lick_any(s):
    """Variant lick onset: the first frame beyond 33 cm from the start with a non-zero lick
    frequency, whether or not it changed (start-to-lick distance, cm)."""
    tr = s["trials"]
    out = np.full(len(tr["gd"]), np.nan)
    for k in range(len(tr["gd"])):
        a, e = tr["s0"][k], tr["s0"][k] + tr["nfr"][k]
        i = np.flatnonzero((s["lick"][a:e] > 0) & (s["pos"][a:e] > LICK_START_CM))
        if len(i):
            out[k] = s["pos"][a + i[0]]
    return out


def first_lick_bout(s):
    """Variant lick onset: the first frame beyond 33 cm from the start where the lick frequency
    turns from 0 to a non-zero value, the start of a bout (start-to-lick distance, cm)."""
    tr = s["trials"]
    rise = (s["lick"] > 0) & (np.r_[0.0, s["lick"][:-1]] == 0)
    out = np.full(len(tr["gd"]), np.nan)
    for k in range(len(tr["gd"])):
        a, e = tr["s0"][k], tr["s0"][k] + tr["nfr"][k]
        i = np.flatnonzero(rise[a:e] & (s["pos"][a:e] > LICK_START_CM))
        if len(i):
            out[k] = s["pos"][a + i[0]]
    return out


def lick_form(s):
    """The form of the lick frequency (verifier round 1): the fraction of frames at 0 Hz, over
    the session and from the start to 33 cm in valid trials; the fraction of valid trials whose
    frequency is non-zero at the frame where the mouse passes 33 cm; the lengths of runs of one
    held non-zero value; and a sample trace around the first lick onset of the first valid trial."""
    tr, lk = s["trials"], s["lick"]
    v = np.flatnonzero(tr["valid"])
    pre = np.concatenate([np.arange(tr["s0"][k], tr["s0"][k] + tr["nfr"][k])[s["pos"][tr["s0"][k]:tr["s0"][k] + tr["nfr"][k]] <= LICK_START_CM]
                          for k in v])
    at33 = []
    for k in v:
        a, e = tr["s0"][k], tr["s0"][k] + tr["nfr"][k]
        j = np.flatnonzero(s["pos"][a:e] > LICK_START_CM)
        if len(j):
            at33.append(lk[a + j[0]] > 0)
    ch = np.flatnonzero(np.diff(lk) != 0) + 1
    runs = np.diff(np.r_[0, ch, len(lk)])
    vals = lk[np.r_[0, ch]]
    held = runs[(vals > 0) & (vals < 10)]
    k = v[0]
    f0 = tr["lick_f"][k] if tr["lick_f"][k] >= 0 else tr["s0"][k]
    w = np.arange(max(f0 - 20, 0), min(f0 + 40, len(lk)))
    return dict(zero_frac=float((lk == 0).mean()), zero_frac_before33=float((lk[pre] == 0).mean()),
                nonzero_at33_frac=float(np.mean(at33)) if at33 else np.nan,
                held_run_frames=np.percentile(held, [5, 50, 95]).tolist() if len(held) else [np.nan] * 3,
                sample=dict(frame=(w - f0).tolist(), pos=np.round(s["pos"][w], 2).tolist(), lick=np.round(lk[w], 2).tolist()))


# ---------------------------------------------------------------- single-basis regression (Supplementary Fig. 6)

WIDTHS = np.geomspace(0.5, 200.0, 25)          # profile grid for the free width s


def sound_db(gdist, silent, cap):
    """Sound intensity (Online Methods, Behavioral training): 100 dB SPL at 25 cm, 6 dB lower per
    doubling of distance. Zero in no-sound zones. Below 25 cm, readings of supp6: the formula with
    distance floored at 0.42 cm (cap=False) or capped at 100 dB (cap=True)."""
    d = np.maximum(gdist, DBIN)
    db = 100.0 - 6.0 * np.log2(d / 25.0)
    if cap:
        db = np.minimum(db, 100.0)
    return np.where(silent, 0.0, db)


def step_distance(s, frames):
    """Goal distance held at its value on entering each no-sound zone (supp6, Step)."""
    tr = s["trials"]
    out = s["gdist"][frames].copy()
    t = s["trial_of"][frames]
    sil = ~sound_zone(s["gdist"][frames], s["pos"][frames], tr["state"][t])
    kz = np.floor((s["gdist"][frames] + 8.375) / 16.75).astype(int)
    held = np.nan
    for j in range(len(frames)):
        if sil[j]:
            if j == 0 or not sil[j - 1] or kz[j] != kz[j - 1] or t[j] != t[j - 1]:
                held = out[j]
            out[j] = held
    return out, sil


def fit_single(y, v, binw, smooth):
    """y = b0 + b1 phi(v), phi Gaussian with centre at the value of maximal averaged activity
    (equation 3) and width profiled over WIDTHS by least squares (a grid in place of four
    initial values of an optimizer), then refined by a bounded scalar optimizer of log width
    between the neighbours of the best grid value, so the widths are not quantized to the grid.
    Returns RMSE, width and b1 per neuron."""
    nb = int(np.ceil((v.max() - v.min()) / binw)) + 1
    b = ((v - v.min()) / binw).astype(int)
    cnt = np.bincount(b, minlength=nb)
    mean = np.stack([np.bincount(b, weights=y[:, i], minlength=nb) for i in range(y.shape[1])], 1) / np.maximum(cnt, 1)[:, None]
    mean[cnt == 0] = np.nan
    ms = uniform_filter1d(np.nan_to_num(mean, nan=np.nanmin(mean)), smooth, axis=0, mode="nearest")
    mu = v.min() + binw * (np.argmax(ms, axis=0) + 0.5)
    yc = y - y.mean(0)
    syy = (yc ** 2).sum(0)
    rmse = np.zeros(y.shape[1]); wid = np.zeros(y.shape[1]); beta = np.zeros(y.shape[1])
    for i in range(y.shape[1]):
        d2 = (v - mu[i]) ** 2
        phi = np.exp(-d2[:, None] / (2 * WIDTHS[None, :] ** 2))
        phc = phi - phi.mean(0)
        spp = (phc ** 2).sum(0); spy = phc.T @ yc[:, i]
        sse = syy[i] - np.where(spp > 1e-12, spy ** 2 / np.maximum(spp, 1e-12), 0)
        k = int(np.argmin(sse))
        lo, hi = np.log(WIDTHS[max(k - 1, 0)]), np.log(WIDTHS[min(k + 1, len(WIDTHS) - 1)])
        res = optimize.minimize_scalar(lambda lw: _sse_at(np.exp(lw), d2, yc[:, i], syy[i])[0], bounds=(lo, hi),
                                       method="bounded", options=dict(xatol=1e-3))
        w = float(np.exp(res.x)) if res.fun < sse[k] else WIDTHS[k]
        e, b1 = _sse_at(w, d2, yc[:, i], syy[i])
        rmse[i] = np.sqrt(max(e, 0) / len(v)); wid[i] = w; beta[i] = b1
    return rmse, wid, beta


def _sse_at(w, d2, yc, syy):
    """Sum of squared errors and b1 of y = b0 + b1 phi at width w (centred y)."""
    phi = np.exp(-d2 / (2 * w ** 2))
    phc = phi - phi.mean()
    spp = float(phc @ phc); spy = float(phc @ yc)
    if spp <= 1e-12:
        return syy, 0.0
    return syy - spy ** 2 / spp, spy / spp


def regressions(s, neurons):
    """Single-basis fits of unfiltered dR/R for the given neurons on Distance, Step and Sound
    (two readings), over the frames of O6: (a) start to goal, (b) start to 3 s after the goal."""
    tr = s["trials"]
    v = np.flatnonzero(tr["valid"])
    out = {}
    for fr_reading in "ab":
        ext = 0 if fr_reading == "a" else int(3 * FS)
        fr = np.concatenate([np.arange(tr["s0"][k], min(tr["goal_f"][k] + ext, tr["s0"][k] + tr["nfr"][k] - 1) + 1) for k in v])
        y = s["dff"][fr][:, neurons].astype(np.float64)
        gdist = s["gdist"][fr]
        step, sil = step_distance(s, fr)
        for name, var, bw, sm in (("distance", gdist, DBIN, SMOOTH_D), ("step", step, DBIN, SMOOTH_D),
                                  ("sound_a", sound_db(gdist, sil, False), 1.0, 3), ("sound_b", sound_db(gdist, sil, True), 1.0, 3)):
            out[(name, fr_reading)] = fit_single(y, var, bw, sm)
    return out
