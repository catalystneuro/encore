"""Loading and measures for testing Garud & Morris (2026) on DANDI:001552 and the Krausz et al.
(2023) hex-level table.

Floeder et al. (2025), DANDI:001552, version 0.250828.1728 (the version the paper's Data
Availability cites). Each session file holds the raw 470 nm and 405 nm photometry, two TTL
channels and the behaviour event log (``eventCode``: 15 sound 1 = cue onset, 10 fixed solenoid 3
= reward, 5 lick onset; the mapping is in the series description).

Clock. The photometry series state a rate of 120481.9 Hz, or timestamps of about 8.3 microseconds
per sample, in the 9 ``JF-FP`` mice, and 130 Hz in the ``JF-dLight-ramp2`` mice, and start at 0,
while the event log runs on another clock. ``photometry_ttl2`` steps up once per cue. The helper
finds its rising edges and fits event time = a * sample index + b by least squares against the
cue times of the event log (the data check prints a and the residuals); every photometry sample
is placed on the event clock through this fit. This is an inference from the data, not a stated
mapping.

Krausz et al. (2023), Mendeley Data doi:10.17632/m59zdjpm9h.1, file hexLevelDf.csv.zip, read in
memory (SHA-256 below). Column meanings are read from the values (the data check prints them).

Where each parameter comes from:
- cue, reward and lick codes: the eventCode description in the files.
- 470 corrected by regressing out 405 and ΔF/F: Methods, "Floeder (2025) dataset", paragraph 1.
  Two readings from the claim's criterion (fig4b-long-iti-dip-below-baseline): "fit" (405 fitted
  to 470 by least squares per session, (470 - fit) / fit) and "own" (each channel's ΔF/F against
  its session mean, then the 405 ΔF/F fitted to the 470 ΔF/F subtracted). No filtering (criterion).
  Samples that are exactly 0 in either channel (dropouts, at most 3 in a session) are treated as
  missing, a standard choice.
- Recordings deposited twice (identical 470 traces) are counted once, at the first day.
- ITI class, median inter-cue interval below 25 s short: Methods, same paragraph.
- 1 s bins locked to reward, trace cut 1 s before the next cue, bins with fewer than 20
  observations dropped, tonic measure from the ITI midpoint to 1 s before the next cue in trials
  with ITI of 30 s or more: Methods, same section, paragraph 2. Readings from the criterion: ITI
  from reward ("reward") or from cue ("cue"); an observation is a trial ("trials") or a sample
  ("samples").
- How the tonic measure is averaged within a session (mean over trials of each trial's mean over
  its kept bins in the window) is not given; it is a standard choice, stated as one.
- Anticipatory lick rate, lick onsets 5 to 8 s after cue onset over 3 s: Methods, same paragraph.
- Reward assigned to a cue: the first reward from the cue up to 10 s after it (rewards come 9 s
  after the cue, CS_t_fxd = 9000 ms in taskParameters); cues with none (omitted or session end)
  are left out of reward-locked measures. Standard choice from the task parameters.
- Krausz inclusion: rows at a port (``port`` not -100), with no distance to the chosen port
  (``hexesFromPort`` missing, the start hex of each trial), at distance 0, or missing velocity are
  dropped. This mapping of the Methods' four conditions to columns is the author's (the claim asks
  for it) and gives 264,042 rows.
- Moving 15 cm/s or more, stationary below 5 cm/s, destination reward 80 or more against 20 or
  less, quartile splits within rat: Methods, "Krausz (2023) dataset".
- Model forms and parameter counts: Methods, "Model Comparison". BIC = n ln(SSE/n) + k ln n:
  assumption named in the criteria (standard for least squares). The Methods' Nelder-Mead is
  unconstrained, so the exponential rate λ may be negative and σ is searched up to 10,000 hexes,
  where the Gaussian is flat over the maze. The Figure 3 profiles keep their scale positive (decaying
  with distance), as the paper reads A > 0 as a net increase toward the goal, which holds only for
  a decaying profile; their scale is searched from 1e-6 (and σ from 0.1) up to the same wide limits.
"""
import hashlib
import io
import zipfile

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import optimize, stats
from scipy.integrate import solve_ivp

DANDISET = "001552"
VERSION = "0.250828.1728"
API = "https://api.dandiarchive.org/api"

KRAUSZ_DOI = "10.17632/m59zdjpm9h.1"
HEX_URL = ("https://data.mendeley.com/public-files/datasets/m59zdjpm9h/files/"
           "b7e8dff7-42d9-4582-875e-fee4bf85e27a/file_downloaded")
HEX_SHA256 = "cad0056f9627dcb8561ae0a42b1b97c7153bb76522b5f75affc1e982ef90553e"

CUE, REWARD, LICK = 15, 10, 5
LICK_WINDOW = (5.0, 8.0)       # s after cue onset (Methods)
SHORT_LONG_SPLIT = 25.0        # s, median inter-cue interval (Methods)
MIN_ITI = 30.0                 # s, long-ITI trials used for the tonic measure (Methods)
MIN_OBS = 20                   # observations per bin (Methods)
CUT_BEFORE_CUE = 1.0           # s (Methods)
MOVING, STATIONARY = 15.0, 5.0  # cm/s (Methods)


# ---------------------------------------------------------------- DANDI


def _get_json(url):
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return r.json()


def list_assets(version=VERSION):
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        page = _get_json(url)
        out += page["results"]
        url = page["next"]
    return pd.DataFrame([{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]}
                         for a in out])


def s3_url(asset_id):
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    r.raise_for_status()
    return r.headers["Location"]


def session_table(assets):
    """One row per file: subject, day number and the file's group (FP, VR-FP, dLight-ramp2)."""
    t = assets.copy()
    t["subject"] = t.path.str.split("/").str[0].str.replace("sub-", "", regex=False)
    t["day"] = t.path.str.extract(r"Day(\d+)").astype(int)
    t["group"] = t.subject.str.extract(r"JF-(FP|VR-FP|dLight-ramp2)-")[0]
    return t.sort_values(["subject", "day"]).reset_index(drop=True)


def rising_edges(x):
    x = np.asarray(x, dtype=float)
    thr = (np.nanmax(x) + np.nanmin(x)) / 2
    return np.flatnonzero((x[1:] > thr) & (x[:-1] <= thr)) + 1


def fit_clock(edges, cue_times):
    """Fit event time = a * sample + b from TTL2 rising edges and cue times.

    When the counts differ by one or two, every way of leaving out the extra edges or cues is
    tried and the fit with the smallest largest residual is kept; pairs then more than 0.1 s off
    the line are left out and the line refitted. Returns a, b, the largest residual (s) of the
    pairs kept, and their number.
    """
    from itertools import combinations
    e, c = np.asarray(edges, float), np.asarray(cue_times, float)
    longer, shorter, edges_longer = (e, c, True) if len(e) >= len(c) else (c, e, False)
    extra = len(longer) - len(shorter)
    if extra > 2 or len(shorter) < 3:
        return np.nan, np.nan, np.inf, 0
    best = None
    for drop in combinations(range(len(longer)), extra):
        keep = np.delete(longer, list(drop))
        x, y = (keep, shorter) if edges_longer else (shorter, keep)
        a, b = np.polyfit(x, y, 1)
        res = np.abs(a * x + b - y).max()
        if best is None or res < best[2]:
            best = (a, b, res, len(x), x, y)
    a, b, res, n, x, y = best
    # one refit without pairs more than 0.1 s off (a TTL edge that is not a cue onset)
    ok = np.abs(a * x + b - y) <= 0.1
    if (~ok).any() and ok.sum() >= 3:
        a, b = np.polyfit(x[ok], y[ok], 1)
        res = np.abs(a * x[ok] + b - y[ok]).max()
    return a, b, res, int(ok.sum())


def load_session(asset_id, photometry=True):
    """Events, and the photometry placed on the event clock, for one session file."""
    with h5py.File(remfile.File(s3_url(asset_id)), "r") as h:
        acq = h["acquisition"]
        d = {"session_description": h["session_description"][()].decode()}
        if "eventCode" not in acq:
            d["has_events"] = False
            d["n_samples"] = acq["photometry_470"]["data"].shape[0]
            return d
        d["has_events"] = True
        code = acq["eventCode"]["data"][:]
        ts = acq["eventCode"]["timestamps"][:]
        d["cue"] = ts[code == CUE]
        d["reward"] = ts[code == REWARD]
        d["lick"] = ts[code == LICK]
        d["end"] = ts.max()
        p470 = acq["photometry_470"]
        d["stated_rate"] = (float(p470["starting_time"].attrs["rate"]) if "starting_time" in p470
                            else 1 / float(np.median(np.diff(p470["timestamps"][:1000]))))
        d["stated_start"] = (float(p470["starting_time"][()]) if "starting_time" in p470
                             else float(p470["timestamps"][0]))
        desc = acq["photometry_ttl2"].attrs.get("description", "")
        d["ttl2_description"] = desc.decode() if isinstance(desc, bytes) else str(desc)
        if photometry:
            ttl2 = acq["photometry_ttl2"]["data"][:]
            edges = rising_edges(ttl2)
            a, b, res, npair = fit_clock(edges, d["cue"])
            d.update(clock_a=a, clock_b=b, clock_resid=res, clock_pairs=npair,
                     n_edges=len(edges))
            s470 = p470["data"][:].astype(float)
            s405 = acq["photometry_405"]["data"][:].astype(float)
            d["t"] = a * np.arange(len(s470)) + b
            d["s470"], d["s405"] = s470, s405
            d["n_samples"] = len(s470)
    return d


# ---------------------------------------------------------------- Floeder measures


def dff(s470, s405, reading="fit"):
    """ΔF/F of the 470 nm signal corrected with the 405 nm signal (two readings, see module)."""
    # exact zeros (at most 3 samples in a session) are dropouts and are treated as missing
    ok = np.isfinite(s470) & np.isfinite(s405) & (s470 > 0) & (s405 > 0)
    out = np.full_like(s470, np.nan)
    x, y = s405[ok], s470[ok]
    if reading == "fit":
        k, c = np.polyfit(x, y, 1)
        fit = k * x + c
        out[ok] = (y - fit) / fit
    elif reading == "own":
        dy = (y - y.mean()) / y.mean()
        dx = (x - x.mean()) / x.mean()
        k, c = np.polyfit(dx, dy, 1)
        out[ok] = dy - (k * dx + c)
    else:
        raise ValueError(reading)
    return out


def trial_table(d):
    """One row per cue: cue time, its reward, next cue, ITIs from reward and from cue."""
    cue = d["cue"]
    rew = d["reward"]
    rows = []
    for i, c in enumerate(cue):
        r = rew[(rew >= c) & (rew <= c + 10)]
        nxt = cue[i + 1] if i + 1 < len(cue) else np.nan
        rows.append({"cue": c, "reward": r[0] if len(r) else np.nan, "next_cue": nxt})
    t = pd.DataFrame(rows)
    t["iti_reward"] = t.next_cue - t.reward
    t["iti_cue"] = t.next_cue - t.cue
    return t


def lick_rates(d):
    """Anticipatory lick rate per cue (lick onsets 5 to 8 s after cue / 3 s)."""
    lk = np.sort(d["lick"])
    lo = np.searchsorted(lk, d["cue"] + LICK_WINDOW[0], side="left")
    hi = np.searchsorted(lk, d["cue"] + LICK_WINDOW[1], side="left")
    return (hi - lo) / (LICK_WINDOW[1] - LICK_WINDOW[0])


def reward_bins(t, sig, trials, max_bins=200):
    """Trial x bin matrices of the mean signal and the sample count in 1 s reward-locked bins.

    Each trial's trace runs from reward to 1 s before the next cue (Methods).
    """
    n = len(trials)
    means = np.full((n, max_bins), np.nan)
    counts = np.zeros((n, max_bins), dtype=int)
    for i, (r, nc) in enumerate(zip(trials.reward.values, trials.next_cue.values)):
        if not (np.isfinite(r) and np.isfinite(nc)):
            continue
        end = nc - CUT_BEFORE_CUE
        i0, i1 = np.searchsorted(t, r), np.searchsorted(t, end)
        if i1 <= i0:
            continue
        k = ((t[i0:i1] - r) // 1.0).astype(int)
        v = sig[i0:i1]
        ok = np.isfinite(v) & (k < max_bins)
        cnt = np.bincount(k[ok], minlength=max_bins)[:max_bins]
        s = np.bincount(k[ok], weights=v[ok], minlength=max_bins)[:max_bins]
        counts[i] = cnt
        with np.errstate(invalid="ignore", divide="ignore"):
            means[i] = np.where(cnt > 0, s / cnt, np.nan)
    return means, counts


def kept_bins(means, counts, obs="trials"):
    """Apply the 20-observation rule; returns the trial x bin matrix with dropped bins as NaN."""
    m = means.copy()
    if obs == "trials":
        n_trials = np.isfinite(means).sum(0)
        m[:, n_trials < MIN_OBS] = np.nan
    elif obs == "samples":
        m[counts < MIN_OBS] = np.nan
    else:
        raise ValueError(obs)
    return m


def tonic_measure(trials, m, iti="reward"):
    """Mean ΔF/F from the ITI midpoint to 1 s before the next cue, trials with ITI >= 30 s.

    Returns the session value (mean over trials of the trial means) and the number of trials.
    Bin k covers [k, k+1) s after reward; a bin is in the window when it starts at or after the
    midpoint (the trace is already cut 1 s before the next cue).
    """
    if iti == "reward":
        dur = trials.iti_reward.values
        mid_after_reward = dur / 2
    elif iti == "cue":
        dur = trials.iti_cue.values
        mid_after_reward = dur / 2 - (trials.reward.values - trials.cue.values)
    else:
        raise ValueError(iti)
    vals = []
    starts = np.arange(m.shape[1])
    for i in range(len(trials)):
        if not (np.isfinite(dur[i]) and dur[i] >= MIN_ITI):
            continue
        sel = starts >= mid_after_reward[i]
        v = m[i, sel]
        v = v[np.isfinite(v)]
        if len(v):
            vals.append(v.mean())
    return (float(np.mean(vals)) if vals else np.nan), len(vals)


def last_bin_value(m, obs="trials"):
    """ΔF/F of the last kept bin before the next cue.

    Under the trial reading, the last bin of the session-average trace that has 20 trials; under
    the sample reading, each trial's last kept bin, averaged over trials.
    """
    if obs == "trials":
        tr = np.nanmean(m, 0)
        k = np.flatnonzero(np.isfinite(tr))
        return float(tr[k[-1]]) if len(k) else np.nan, (int(k[-1]) if len(k) else -1)
    last = []
    for row in m:
        k = np.flatnonzero(np.isfinite(row))
        if len(k):
            last.append(row[k[-1]])
    return float(np.mean(last)) if last else np.nan, -1


def mixed_slope(df, y, x, group="subject"):
    """Linear mixed model y ~ x with random intercepts and slopes per subject (Methods).

    The REML surface has several local optima for some readings, and which one L-BFGS reaches
    can change with rounding in the inputs; the model is fitted with L-BFGS, Powell and
    Nelder-Mead and the converged fit with the highest REML log-likelihood is kept.
    """
    import statsmodels.formula.api as smf
    import warnings
    d = df[[y, x, group]].dropna()
    model = smf.mixedlm(f"{y} ~ {x}", d, groups=d[group], re_formula=f"~{x}")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fits = [model.fit(method=m, reml=True, maxiter=5000) for m in ("lbfgs", "powell", "nm")]
    fit = max((f for f in fits if f.converged and np.isfinite(f.pvalues[x])), key=lambda f: f.llf)
    r_pooled = stats.pearsonr(d[x], d[y])
    dm = d.groupby(group)[[x, y]].transform(lambda s: s - s.mean())
    r_within = stats.pearsonr(dm[x], dm[y])
    return {"slope": fit.fe_params[x], "se": fit.bse_fe[x], "p": fit.pvalues[x],
            "converged": bool(fit.converged), "n": len(d), "subjects": d[group].nunique(),
            "r_pooled": r_pooled[0], "p_pooled": r_pooled[1],
            "r_within": r_within[0], "p_within": r_within[1]}


# ---------------------------------------------------------------- Krausz measures


def load_hex():
    """hexLevelDf from Mendeley Data, read in memory, checked against its SHA-256."""
    r = requests.get(HEX_URL, timeout=300)
    r.raise_for_status()
    b = r.content
    sha = hashlib.sha256(b).hexdigest()
    if sha != HEX_SHA256:
        raise ValueError(f"hexLevelDf.csv.zip has SHA-256 {sha}, expected {HEX_SHA256}")
    z = zipfile.ZipFile(io.BytesIO(b))
    df = pd.read_csv(z.open("hexLevelDf.csv"))
    # destination reward: nominal reward of the port the trial ends at
    end = df[df.port != -100][["session", "trial", "port"]].drop_duplicates(["session", "trial"])
    df = df.merge(end.rename(columns={"port": "dest_port"}), on=["session", "trial"], how="left")
    nom = df[["nom_rwd_a", "nom_rwd_b", "nom_rwd_c"]].to_numpy()
    dp = df.dest_port.fillna(-1).astype(int).to_numpy()
    df["dest_rwd"] = np.where(dp >= 0, nom[np.arange(len(df)), np.clip(dp, 0, 2)], np.nan)
    df["d"] = df.hexesFromPort
    return df


def included(df):
    """The Methods' approach-epoch selection, mapped to columns (see module docstring)."""
    return ((df.port == -100) & df.hexesFromPort.notna() & (df.hexesFromPort != 0)
            & df.vel.notna() & df.DA.notna())


def per_rat_r(df, x, y, by="rat"):
    out = {}
    for rat, g in df.groupby(by):
        g = g[[x, y]].dropna()
        out[rat] = stats.pearsonr(g[x], g[y])[0] if len(g) > 2 else np.nan
    return pd.Series(out)


def slope(x, y):
    return np.polyfit(x, y, 1)[0]


def recover_value(g, min_obs=1):
    """Recovered V along distance to goal for one rat (Methods, value function recovery).

    Gradient per (hex, distance) cell = (mean moving DA - mean stationary DA) / mean moving
    velocity, averaged per distance; integrated toward the goal (progress s = -d) with an
    explicit 5(4) Runge-Kutta solver (scipy RK45, Dormand-Prince, in place of Julia's Tsit5) on
    the linear interpolant. Returns distances (ascending) and V (up to a constant).
    """
    mov = g[g.vel >= MOVING].groupby(["hexlabel", "d"]).agg(da=("DA", "mean"), v=("vel", "mean"),
                                                           n=("DA", "size"))
    st = g[g.vel < STATIONARY].groupby(["hexlabel", "d"]).agg(da=("DA", "mean"), n=("DA", "size"))
    j = mov.join(st, lsuffix="_m", rsuffix="_s", how="inner")
    j = j[(j.n_m >= min_obs) & (j.n_s >= min_obs)]
    grad = ((j.da_m - j.da_s) / j.v).groupby(level="d").mean().sort_index()
    d = grad.index.to_numpy(float)
    gv = grad.to_numpy()
    if len(d) < 5:
        return d, np.full_like(d, np.nan)
    # dV/ds = grad, s = -d; integrate from the farthest distance toward the goal
    s = -d[::-1]
    gs = gv[::-1]
    sol = solve_ivp(lambda x, v: [np.interp(x, s, gs)], (s[0], s[-1]), [0.0], t_eval=s,
                    method="RK45", max_step=0.5)
    V = sol.y[0][::-1]
    return d, V


PROFILES = {
    "exponential": lambda d, A, p, c: A * np.exp(-p * d) + c,
    "hyperbolic": lambda d, A, p, c: A / (1 + p * d) + c,
    "power-law": lambda d, A, p, c: A * (d + 1) ** (-p) + c,
    "gaussian": lambda d, A, p, c: A * np.exp(-d ** 2 / (2 * p ** 2)) + c,
}
PROFILE_BOUNDS = {"exponential": (1e-6, 20), "hyperbolic": (1e-6, 1e3), "power-law": (1e-6, 20),
                  "gaussian": (0.1, 1e4)}
# the first round's narrower bounds, shown beside the wide ones
PROFILE_BOUNDS_NARROW = {"exponential": (1e-4, 5), "hyperbolic": (1e-4, 50), "power-law": (1e-4, 10),
                         "gaussian": (0.3, 60)}


def _linear_given_shape(basis, y):
    X = np.column_stack(basis + [np.ones_like(y)])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    sse = float(np.sum((y - X @ coef) ** 2))
    return coef, sse


def fit_profile(name, d, V, bounds=PROFILE_BOUNDS):
    """Best three-parameter fit of a profile; the shape parameter by bounded search over a grid
    then refinement, A and c by least squares given it (same optimum as a joint search)."""
    f = PROFILES[name]
    lo, hi = bounds[name]
    grid = np.geomspace(lo, hi, 200)

    def sse_of(p):
        return _linear_given_shape([f(d, 1.0, p, 0.0)], V)[1]

    vals = [sse_of(p) for p in grid]
    i = int(np.argmin(vals))
    a, b = grid[max(i - 1, 0)], grid[min(i + 1, len(grid) - 1)]
    res = optimize.minimize_scalar(sse_of, bounds=(a, b), method="bounded")
    p = res.x if res.fun <= vals[i] else grid[i]
    coef, sse = _linear_given_shape([f(d, 1.0, p, 0.0)], V)
    n = len(V)
    sst = float(np.sum((V - V.mean()) ** 2))
    return {"A": coef[0], "p": p, "c": coef[1], "sse": sse,
            "r2": 1 - sse / sst if sst > 0 else np.nan, "bic": bic(sse, n, 3),
            "at_bound": i in (0, len(grid) - 1)}


def bic(sse, n, k):
    return n * np.log(sse / n) + k * np.log(n)


# Six models of Methods, "Model Comparison". For the nonlinear spatial scale the SSE is profiled
# over the linear parameters (A, B, c by least squares), which finds the same optimum as a
# Nelder-Mead search over all parameters; nelder_mead_check runs that search from the optimum.
# λ may be negative (unconstrained, as Nelder-Mead is); σ is searched from 0.3 to 10,000 hexes.
LAMBDA_GRID = np.concatenate([-np.geomspace(1e-5, 5, 150)[::-1], [0.0], np.geomspace(1e-5, 5, 150)])
SIGMA_GRID = np.geomspace(0.3, 1e4, 200)
MODEL_K = {"CT TD exp": 4, "CT TD gauss": 4, "dV/dt exp": 3, "dV/dt gauss": 3, "Value": 3,
           "Velocity": 2}


def _bases(model, d, v, p):
    e = np.exp(-p * d)
    gss = np.exp(-d ** 2 / (2 * p ** 2))
    return {"CT TD exp": [e * v, e], "CT TD gauss": [gss * v, gss], "dV/dt exp": [e * v],
            "dV/dt gauss": [gss * v], "Value": [e]}[model]


def fit_model(model, d, v, y, grid=None):
    n = len(y)
    if model == "Velocity":
        _, sse = _linear_given_shape([v], y)
        return {"sse": sse, "p": np.nan, "bic": bic(sse, n, 2)}
    if grid is None:
        grid = SIGMA_GRID if "gauss" in model else LAMBDA_GRID

    def sse_of(p):
        return _linear_given_shape(_bases(model, d, v, p), y)[1]

    vals = np.array([sse_of(p) for p in grid])
    i = int(np.argmin(vals))
    a, b = grid[max(i - 1, 0)], grid[min(i + 1, len(grid) - 1)]
    res = optimize.minimize_scalar(sse_of, bounds=(a, b), method="bounded")
    p, sse = (res.x, res.fun) if res.fun <= vals[i] else (grid[i], vals[i])
    coef, _ = _linear_given_shape(_bases(model, d, v, p), y)
    return {"sse": float(sse), "p": float(p), "coef": coef, "bic": bic(sse, n, MODEL_K[model]),
            "at_bound": i in (0, len(grid) - 1)}


def nelder_mead_check(model, d, v, y, fit):
    """SSE after a Nelder-Mead search over all parameters started from the profiled optimum."""
    def sse(theta):
        b = _bases(model, d, v, theta[-1])
        pred = sum(c * x for c, x in zip(theta[:-2], b)) + theta[-2]
        return float(np.sum((y - pred) ** 2))
    res = optimize.minimize(sse, np.r_[fit["coef"], fit["p"]], method="Nelder-Mead",
                            options={"maxiter": 20000, "maxfev": 20000, "xatol": 1e-10,
                                     "fatol": 1e-10})
    return res.fun


def cue_locked(t, sig, cues, before=5, after=15):
    """Mean signal in 1 s bins from `before` s before to `after` s after each cue."""
    edges = np.arange(-before, after + 1)
    rows = []
    for c in cues:
        i0, i1 = np.searchsorted(t, [c - before, c + after])
        k = ((t[i0:i1] - c + before) // 1.0).astype(int)
        v = sig[i0:i1]
        ok = np.isfinite(v) & (k >= 0) & (k < len(edges) - 1)
        cnt = np.bincount(k[ok], minlength=len(edges) - 1)
        s = np.bincount(k[ok], weights=v[ok], minlength=len(edges) - 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            rows.append(np.where(cnt > 0, s / cnt, np.nan))
    return np.nanmean(rows, 0) if rows else np.full(len(edges) - 1, np.nan)


def file_contents(asset_id):
    """Acquisition series and processing groups of one file."""
    with h5py.File(remfile.File(s3_url(asset_id)), "r") as h:
        proc = []
        if "processing" in h:
            h["processing"].visit(proc.append)
        return {"acquisition": sorted(h["acquisition"].keys()), "processing": proc}


def clock_contrast(t, sig, times, shift=0.0):
    """Mean signal 0 to 2 s after each event minus 2 to 0 s before, events shifted by `shift` s."""
    out = []
    for e in np.asarray(times) + shift:
        i0, i1, i2 = np.searchsorted(t, [e - 2, e, e + 2])
        if i1 > i0 and i2 > i1:
            out.append(np.nanmean(sig[i1:i2]) - np.nanmean(sig[i0:i1]))
    return float(np.mean(out)) if out else np.nan


def session_summary(asset_id):
    """Everything the Figure 4 claims need from one session, under every reading."""
    d = load_session(asset_id)
    if not d["has_events"]:
        return {"has_events": False, "n_samples": d["n_samples"],
                "session_description": d["session_description"]}
    trials = trial_table(d)
    lr = lick_rates(d)
    s = {"has_events": True, "session_description": d["session_description"],
         "n_cues": len(d["cue"]), "n_rewards": len(d["reward"]), "n_licks": len(d["lick"]),
         "median_ici": float(np.median(np.diff(d["cue"]))) if len(d["cue"]) > 1 else np.nan,
         "stated_rate": d["stated_rate"], "stated_start": d["stated_start"],
         "ttl2_description": d["ttl2_description"], "clock_a": d["clock_a"], "clock_b": d["clock_b"],
         "clock_resid": d["clock_resid"], "n_edges": d["n_edges"],
         "clock_pairs": d["clock_pairs"],
         "n_samples": d["n_samples"], "n_nan470": int(np.isnan(d["s470"]).sum()),
         "n_low470": int((d["s470"] < 0.01).sum()),
         "phot_span": (d["t"][0], d["t"][-1]), "event_end": d["end"],
         "hash470": hashlib.md5(np.nan_to_num(d["s470"]).tobytes()).hexdigest(),
         "hash_cues": hashlib.md5(np.round(np.diff(d["cue"]), 3).tobytes()).hexdigest(),
         "cue_reward_lag": [float(x) for x in (trials.reward - trials.cue).dropna()],
         "range470": (float(np.nanmin(d["s470"])), float(np.nanmax(d["s470"]))),
         "range405": (float(np.nanmin(d["s405"])), float(np.nanmax(d["s405"]))),
         "lick_rate": float(np.mean(lr)), "lick_rates": lr, "n_trials": len(trials),
         "n_rewarded": int(trials.reward.notna().sum()),
         "median_iti_reward": float(trials.iti_reward.median()),
         "n_iti30_reward": int((trials.iti_reward >= MIN_ITI).sum()),
         "n_iti30_cue": int((trials.iti_cue >= MIN_ITI).sum())}
    for corr in ("fit", "own"):
        sig = dff(d["s470"], d["s405"], corr)
        if corr == "fit":
            s["contrast_true"] = clock_contrast(d["t"], sig, trials.reward.dropna())
            s["contrast_shift"] = [clock_contrast(d["t"], sig, trials.reward.dropna(), sh)
                                   for sh in (-6.0, -3.0, 3.0, 6.0)]
            s["dff_range"] = (float(np.nanmin(sig)), float(np.nanmax(sig)))
            s["dff_pct"] = tuple(float(x) for x in np.nanpercentile(sig, [0.1, 50, 99.9]))
            s["cue_trace"] = cue_locked(d["t"], sig, d["cue"])
        s[f"dff_mean_{corr}"] = float(np.nanmean(sig))
        means, counts = reward_bins(d["t"], sig, trials)
        for obs in ("trials", "samples"):
            m = kept_bins(means, counts, obs)
            for iti in ("reward", "cue"):
                s[f"tonic_{corr}_{iti}_{obs}"], s[f"ntonic_{corr}_{iti}_{obs}"] = \
                    tonic_measure(trials, m, iti)
            s[f"last_{corr}_{obs}"], s[f"lastbin_{corr}_{obs}"] = last_bin_value(m, obs)
        s[f"trace_{corr}"] = np.nanmean(kept_bins(means, counts, "trials")[:, :80], 0) \
            if np.isfinite(means).any() else np.full(80, np.nan)
    return s


def summarise_all(table, workers=4, retries=3):
    """session_summary for every row of a session table, streamed in parallel threads."""
    import time
    from concurrent.futures import ThreadPoolExecutor

    def one(aid):
        for k in range(retries):
            try:
                return session_summary(aid)
            except Exception as e:  # network hiccup: retry, then fail loudly
                err = e
                time.sleep(5)
        raise err

    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(one, table.asset_id))


def session_frame(table, summaries):
    """Scalar session measures with subject, day, ITI class and the two session numberings."""
    rows = []
    for (_, r), s in zip(table.iterrows(), summaries):
        d = {k: v for k, v in s.items() if np.isscalar(v)}
        d.update(subject=r.subject, day=r.day, group=r.group, path=r.path)
        rows.append(d)
    T = pd.DataFrame(rows)
    T["cls"] = np.where(T.median_ici < SHORT_LONG_SPLIT, "short", "long")
    T["sess_all"] = T.groupby("subject").day.rank().astype(int)
    T["sess_long"] = T[T.cls == "long"].groupby("subject").day.rank()
    return T
