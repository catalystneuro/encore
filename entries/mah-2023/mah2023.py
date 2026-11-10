"""Loading and measures for Mah, Schiereck, Bossio and Constantinople (2023) on DANDI:001169.

Data access. Each NWB file holds one session of one rat. The analysis uses the table
``intervals/processed_trials`` (the lab's per-rat "A struct", one row per trial, written by
parse_data_from_mysql.m in github.com/constantinoplelab/published, rat_behavior) and, from the
raw Bpod table ``intervals/trials``, only the catch probability of each session. Each file is
streamed from the archive's S3 bucket into memory (one HTTP GET per file, never written to disk)
and opened with h5py; only the columns below are kept.

Where parameters come from is said beside each one: "claim" (the claim's criterion, which cites
the paper or its code), "paper" (a passage of the paper taken by the author, protocol step 1.6),
"assumption", or "standard" (a choice that cannot change a result).
"""
from __future__ import annotations

import hashlib
import io
import time
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests

DANDISET = "001169"
VERSION = "0.260825.1909"  # the only published version (see the notebook header)
API = "https://api.dandiarchive.org/api"

# Male volumes; female volumes 4, 8, 16, 32, 64 are treated as 5, 10, 20, 40, 80
# (Methods, Training for male and female rats; utils/convertreward.m). "claim"
VOLUME_MAP = {4: 5, 5: 5, 8: 10, 10: 10, 16: 20, 20: 20, 32: 40, 40: 40, 64: 80, 80: 80}
VOLUMES = [5, 10, 20, 40, 80]
BLOCK_CODE = {b"Mixed": 1, b"High": 2, b"Low": 3}  # the code's coding: 1 mixed, 2 high, 3 low

TRIAL_COLUMNS = [
    "block_type", "reward_volume_ul", "is_catch", "is_opt_out", "is_rewarded", "is_violation",
    "wait_time", "wait_time_unthresholded", "inter_trial_interval", "training_stage",
    "reward_delay", "wait_time_threshold", "start_time",
]


def list_assets(version: str = VERSION) -> list[dict]:
    """All assets of the pinned version, from the DANDI REST API."""
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        js = r.json()
        out += js["results"]
        url = js["next"]
    return out


def s3_url(asset: dict) -> str:
    b = asset["blob"]
    return f"https://dandiarchive.s3.amazonaws.com/blobs/{b[:3]}/{b[3:6]}/{b}"


def _get(url: str, tries: int = 5) -> bytes:
    for k in range(tries):
        try:
            r = requests.get(url, timeout=120)
            r.raise_for_status()
            return r.content
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(2 ** k)


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def _attr(f, key):
    return _s(f[key][()]) if key in f else ""


def read_session(asset: dict) -> tuple[dict, pd.DataFrame]:
    """Read one session: its metadata and its processed trial table."""
    raw = _get(s3_url(asset))
    with h5py.File(io.BytesIO(raw), "r") as f:
        pt = f["intervals/processed_trials"]
        cols = {c: pt[c][:] for c in TRIAL_COLUMNS if c in pt}
        tr = f["intervals/trials"]
        catchp = tr["catch_percentage"][:] if "catch_percentage" in tr else np.full(len(tr["id"]), np.nan)
        raw_vol = tr["reward_volume_ul"][:]
        raw_catch = tr["is_catch"][:].astype(bool)
        raw_start = tr["start_time"][:]
        stage_raw = tr["training_stage"][:] if "training_stage" in tr else np.array([np.nan])
        meta = dict(
            path=asset["path"],
            subject=_attr(f, "general/subject/subject_id"),
            sex=_attr(f, "general/subject/sex"),
            age=_attr(f, "general/subject/age"),
            subject_description=_attr(f, "general/subject/description"),
            genotype=_attr(f, "general/subject/genotype"),
            session_id=_attr(f, "general/session_id"),
            protocol=_attr(f, "general/protocol"),
            session_start_time=_attr(f, "session_start_time"),
            n_raw_trials=len(tr["id"]),
            n_trials=len(pt["id"]),
            catch_percentage=float(pd.Series(catchp).mode().iloc[0]) if len(catchp) else np.nan,
            catch_percentage_values=",".join(sorted({f"{v:g}" for v in np.unique(catchp)})),
            raw_stage_values=",".join(sorted({f"{v:g}" for v in np.unique(stage_raw)})),
            missing_columns=",".join(c for c in TRIAL_COLUMNS if c not in pt),
            has_prob_catch_column="prob_catch" in pt or "catch_percentage" in pt,
        )
    # The processed table has no catch probability; it is taken from the raw table, row by row.
    # The two tables are checked to be the same trials (equal length, reward, catch flag, start).
    same_len = len(raw_vol) == meta["n_trials"]
    meta["raw_rows_match"] = bool(same_len)
    meta["raw_volume_mismatch"] = int((raw_vol != cols["reward_volume_ul"]).sum()) if same_len else -1
    meta["raw_catch_mismatch"] = int((raw_catch != cols["is_catch"].astype(bool)).sum()) if same_len else -1
    meta["raw_start_maxdiff"] = float(np.max(np.abs(raw_start - cols["start_time"]))) if same_len and len(raw_start) else np.nan
    n = meta["n_trials"]
    df = pd.DataFrame({
        "block": np.array([BLOCK_CODE.get(b, 0) for b in cols["block_type"]], dtype=np.int8),
        "volume_raw": cols["reward_volume_ul"].astype(np.int16),
        "catch": cols["is_catch"].astype(bool),
        "optout": cols["is_opt_out"].astype(bool),
        "hit": cols["is_rewarded"].astype(bool),
        "vio": cols["is_violation"].astype(bool),
        "wt": cols["wait_time"].astype(np.float32),
        "wt_unthr": cols["wait_time_unthresholded"].astype(np.float32),
        "iti": cols["inter_trial_interval"].astype(np.float32),
        "stage": cols["training_stage"].astype(np.int8),
        "reward_delay": cols["reward_delay"].astype(np.float32),
        "wt_thresh": cols["wait_time_threshold"].astype(np.float32),
        "t_start": cols["start_time"].astype(np.float64),
        "catch_p": (catchp if same_len else np.full(n, np.nan)).astype(np.float32),
    })
    df["trial"] = np.arange(n, dtype=np.int32)
    h = hashlib.sha1()
    for c in ("volume_raw", "wt_unthr", "iti"):
        h.update(np.ascontiguousarray(df[c].values).tobytes())
    meta["fingerprint"] = h.hexdigest()
    return meta, df


def load_all(assets: list[dict], workers: int = 24, progress: int = 2000):
    """Read every session; returns (sessions, trials). Trials carry a session index."""
    metas, frames = [], []
    t0 = time.time()
    with ThreadPoolExecutor(workers) as ex:
        for i, (m, df) in enumerate(ex.map(read_session, assets)):
            m["sidx"] = i
            df["sidx"] = np.int32(i)
            metas.append(m)
            frames.append(df)
            if progress and (i + 1) % progress == 0:
                print(f"{i + 1} of {len(assets)} sessions read, {time.time() - t0:.0f} s", flush=True)
    sessions = pd.DataFrame(metas)
    trials = pd.concat(frames, ignore_index=True)
    return sessions, trials



# ---------------------------------------------------------------------------------------------
# Preparing the trials of each rat
# ---------------------------------------------------------------------------------------------

def prepare(sessions: pd.DataFrame, trials: pd.DataFrame):
    """Order sessions by start time within each rat (the lab's A struct is in date order), drop
    recordings deposited twice (same rat, identical trial data), and add the male-equivalent
    volume. Returns (sessions kept, trials kept, duplicates dropped)."""
    s = sessions.copy()
    s["start"] = pd.to_datetime(s["session_start_time"], utc=True, format="ISO8601")
    s = s.sort_values(["subject", "start", "path"])
    dup = s[s.duplicated(["subject", "fingerprint"], keep="first")]
    s = s.drop(dup.index)
    s["order"] = s.groupby("subject").cumcount()
    t = trials[trials["sidx"].isin(s["sidx"])]
    t = t.merge(s[["sidx", "subject", "order"]], on="sidx", how="left")
    t = t.sort_values(["subject", "order", "trial"], kind="stable").reset_index(drop=True)
    t["vol"] = t["volume_raw"].map(VOLUME_MAP).astype(np.int16)
    return s.reset_index(drop=True), t, dup


def rat_arrays(t: pd.DataFrame) -> dict:
    """Per-rat dict of numpy arrays, trials concatenated over sessions in date order."""
    out = {}
    for rat, g in t.groupby("subject", sort=True):
        d = {c: g[c].to_numpy() for c in ["block", "vol", "catch", "optout", "hit", "vio", "wt",
                                           "wt_unthr", "iti", "order", "trial", "catch_p",
                                           "volume_raw"]}
        d["vol_raw"] = d.pop("volume_raw")
        for c in ("wt", "wt_unthr", "iti", "catch_p"):
            d[c] = d[c].astype(float)
        d["first"] = d["trial"] == 0
        d["prev_vol"] = np.r_[np.nan, d["vol"][:-1].astype(float)]
        out[rat] = d
    return out


def nanz(x):
    x = np.asarray(x, float)
    return (x - np.nanmean(x)) / np.nanstd(x, ddof=1)


def clip99(x):
    """Values above the 99th percentile of the rat's pooled distribution set to NaN (Methods,
    Criteria for including behavioral data; iticurves.m). "claim" """
    x = np.array(x, float)
    x[x > np.nanpercentile(x, 99)] = np.nan
    return x


def matlab_smooth(y, span):
    """Moving average as MATLAB's smooth(y, span): an even span is reduced by one and the window
    shrinks symmetrically at the ends. NaNs are ignored (standard choice)."""
    y = np.asarray(y, float)
    span = int(span)
    if span % 2 == 0:
        span -= 1
    h = span // 2
    n = len(y)
    out = np.full(n, np.nan)
    for i in range(n):
        k = min(h, i, n - 1 - i)
        w = y[i - k:i + k + 1]
        if np.isfinite(w).any():
            out[i] = np.nanmean(w)
    return out


# ---------------------------------------------------------------------------------------------
# Block effects (Fig. 1, Supplementary Figs 2, 3, 12, 14)
# ---------------------------------------------------------------------------------------------

def wt_curves(d, wt=None, mask=None):
    """Mean wait time on opt-out catch trials by block and offer (wtcurves.m). Rows mixed, high,
    low; columns 5 to 80 uL."""
    wt = d["wt"] if wt is None else wt
    use = d["optout"] & d["catch"]
    if mask is not None:
        use = use & mask
    out = np.full((3, 5), np.nan)
    for i, b in enumerate([1, 2, 3]):
        for j, v in enumerate(VOLUMES):
            x = wt[use & (d["block"] == b) & (d["vol"] == v)]
            if np.isfinite(x).any():
                out[i, j] = np.nanmean(x)
    return out


def _m(x):
    return np.nanmean(x) if np.isfinite(x).any() else np.nan


def block_effects(d):
    """Per-rat numbers for Fig. 1e,f,i and Supplementary Figs 2, 3, 12 and 14."""
    from scipy.stats import mannwhitneyu
    r = {}
    cur = wt_curves(d)
    r["wt_curve"] = cur
    r["wt_curve_unthr"] = wt_curves(d, wt=d["wt_unthr"])
    co = d["optout"] & d["catch"]
    wt = d["wt"]
    hi20 = co & (d["vol"] == 20) & (d["block"] == 2)
    lo20 = co & (d["vol"] == 20) & (d["block"] == 3)
    r["wt20_hi"], r["wt20_lo"] = _m(wt[hi20]), _m(wt[lo20])
    # reading (a): z-scored over all the rat's catch trials (Methods, Statistical analyses)
    z = np.full(len(wt), np.nan)
    z[co] = nanz(wt[co])
    r["wt20z_hi"], r["wt20z_lo"] = _m(z[hi20]), _m(z[lo20])
    a, b = wt[hi20], wt[lo20]
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    r["p_wt_rank_left"] = mannwhitneyu(a, b, alternative="less").pvalue if len(a) and len(b) else np.nan
    # trial initiation times, all trials (iticurves.m)
    L = clip99(d["iti"])
    Lz = nanz(L)
    for name, blk in (("hi", 2), ("lo", 3), ("mix", 1)):
        r[f"iti_{name}"] = _m(L[d["block"] == blk])
        r[f"itiz_{name}"] = _m(Lz[d["block"] == blk])
    a, b = L[d["block"] == 2], L[d["block"] == 3]
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    r["p_iti_rank_left"] = mannwhitneyu(a, b, alternative="less").pvalue
    # Supplementary Fig. 2 (FigureS2.m): previous trial rewarded or not; the first trial of the
    # rat's concatenated data is in neither set, as in the code
    prev_hit = np.r_[False, d["hit"][:-1]]
    prev_unhit = np.r_[False, ~d["hit"][:-1]]
    for name, msk in (("postrew", prev_hit), ("postunrew", prev_unhit)):
        r[f"itiz_{name}_hi"] = _m(Lz[msk & (d["block"] == 2)])
        r[f"itiz_{name}_lo"] = _m(Lz[msk & (d["block"] == 3)])
    # Supplementary Fig. 3 (FigureS3.m): wait time ratio after rewarded and unrewarded trials
    for name, msk in (("postrew", prev_hit), ("postunrew", prev_unhit)):
        r[f"wt20_{name}_hi"] = _m(wt[hi20 & msk])
        r[f"wt20_{name}_lo"] = _m(wt[lo20 & msk])
    return r


# ---------------------------------------------------------------------------------------------
# Block transitions (Fig. 2a,b; Supplementary Figs 4 to 6)
# ---------------------------------------------------------------------------------------------

TRANSITIONS = {"ltom": -2, "htom": -1, "mtol": 2, "mtoh": 1}


def transition_codes(d):
    """Block change at each trial within its session, 0 for the first 40 trials of each session
    (blockhmat_withvios.m): -2 low to mixed, -1 high to mixed, 2 mixed to low, 1 mixed to high."""
    blk = d["block"].astype(int)
    diff = np.r_[0, np.diff(blk)]
    diff[d["first"]] = 0
    diff[d["trial"] < 40] = 0
    return diff


def wt_dynamics(d, twin=20, smooth=10, mask=None):
    """Delta z-scored wait time around block transitions (block_dynamics_wt.m): z-scored over
    catch trials, then within each offer over non-violation catch trials; windows of +-twin trials
    over the concatenated trials; mean over transitions, then smoothed."""
    w = d["wt"].copy()
    c = d["catch"]
    w[c] = nanz(w[c])
    for v in VOLUMES:
        m = (d["vol"] == v) & c & ~d["vio"]
        if m.sum() > 1:
            w[m] = nanz(w[m])
    if mask is not None:
        w[~mask] = np.nan
    ctch = c & ~d["vio"]
    w = np.where(ctch, w, np.nan)
    codes = transition_codes(d)
    n = len(w)
    off = np.arange(-twin, twin + 1)
    out = {}
    for name, code in TRANSITIONS.items():
        pos = np.flatnonzero(codes == code)
        if len(pos) == 0:
            out[name] = np.full(2 * twin + 1, np.nan)
            continue
        idx = pos[:, None] + off[None, :]
        ok = (idx >= 0) & (idx < n)
        mat = np.full(idx.shape, np.nan)
        mat[ok] = w[idx[ok]]
        with np.errstate(all="ignore"):
            cur = np.nanmean(mat, axis=0)
        cur[twin] = cur[twin - 2]
        out[name] = matlab_smooth(cur, smooth)
    return out


def lat_dynamics(d, twin=20, smooth=10, detrend="pooled", mask=None, iti=None):
    """z-scored trial initiation time around block transitions (block_dynamics_latency.m).
    detrend: "pooled" (the code: one line of z-scored time against trial number over all
    sessions), "session" (the Methods: per session, against z-scored trial number), or None.
    Windows stay within the session."""
    l = (d["iti"] if iti is None else iti).copy()
    l[d["first"]] = np.nan
    l = clip99(l)
    z = nanz(l)
    if mask is not None:
        z[~mask] = np.nan
    tn = d["trial"].astype(float) + 1
    if detrend == "pooled":
        ok = np.isfinite(z)
        b = np.polyfit(tn[ok], z[ok], 1)
        z = z - (b[0] * tn + b[1])
    elif detrend == "session":
        z = z.copy()
        for o in np.unique(d["order"]):
            m = d["order"] == o
            ok = m & np.isfinite(z)
            if ok.sum() > 2:
                x = tn[m]
                xz = (x - x.mean()) / x.std(ddof=1)
                ok2 = np.isfinite(z[m])
                b = np.polyfit(xz[ok2], z[m][ok2], 1)
                z[m] = z[m] - (b[0] * xz + b[1])
    codes = transition_codes(d)
    sess = d["order"]
    n = len(z)
    off = np.arange(-twin, twin + 1)
    out = {}
    for name, code in TRANSITIONS.items():
        pos = np.flatnonzero(codes == code)
        if len(pos) == 0:
            out[name] = np.full(2 * twin + 1, np.nan)
            continue
        idx = pos[:, None] + off[None, :]
        ok = (idx >= 0) & (idx < n)
        ok[ok] = sess[idx[ok]] == np.repeat(sess[pos], ok.sum(1))
        mat = np.full(idx.shape, np.nan)
        mat[ok] = z[idx[ok]]
        with np.errstate(all="ignore"):
            cur = np.nanmean(mat, axis=0)
        cur[twin] = cur[twin - 2] if name == "mtol" else cur[twin - 1]
        cur[twin - 1] = np.nan
        out[name] = matlab_smooth(cur, smooth)
    return out


def mixed_by_previous_block(d, within_session=False):
    """Mean z-scored initiation time over mixed blocks after high and after low blocks
    (FigureS4.m: transitions found on the concatenated trials, the last one dropped). With
    within_session, transitions at a session's first trial are dropped and a mixed block ends at
    the end of its session."""
    L = nanz(clip99(d["iti"]))
    blk = d["block"].astype(int)
    bt = np.r_[np.nan, np.diff(blk)].astype(float)
    if within_session:
        bt[d["first"]] = np.nan
    tr = np.flatnonzero(bt < 0)
    hi, lo = [], []
    for a, b in zip(tr[:-1], tr[1:]):
        seg = np.arange(a, b)
        if within_session:
            seg = seg[d["order"][seg] == d["order"][a]]
        seg = seg[blk[seg] == 1]
        (hi if bt[a] == -1 else lo).append(L[seg])
    h = np.concatenate(hi) if hi else np.array([np.nan])
    lw = np.concatenate(lo) if lo else np.array([np.nan])
    return _m(h), _m(lw)


# ---------------------------------------------------------------------------------------------
# Trial history regressions (Fig. 2c-h)
# ---------------------------------------------------------------------------------------------

def ols(y, X):
    """Least squares with a 95% interval per coefficient, rows with NaN dropped (MATLAB regress)."""
    from scipy.stats import t as tdist
    ok = np.isfinite(y) & np.isfinite(X).all(1)
    y, X = y[ok], X[ok]
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ b
    dof = len(y) - X.shape[1]
    s2 = res @ res / dof
    cov = s2 * np.linalg.pinv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    q = tdist.ppf(0.975, dof)
    return b, np.c_[b - q * se, b + q * se], int(ok.sum())


def fit_exp_decay(x, y, lb, ub, iters=10, rng=None):
    """y = D exp(-x/tau) fitted by least squares within the bounds (fit_exp_decay.m: fmincon from 10
    random starts). Here the fit is found without random starts: D is linear given tau, so for
    each tau on a fine grid the best D in its bounds is exact, and the best tau is then refined
    with a bounded scalar search. This finds the least-squares optimum that the random starts
    look for (a standard choice; a gradient search from random starts can stall at D = 0, where
    the error does not depend on tau). `iters` and `rng` are kept for the signature. Returns
    (D, tau)."""
    from scipy.optimize import minimize_scalar
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ok = np.isfinite(y)
    x, y = x[ok], y[ok]
    if len(y) == 0:
        return np.array([np.nan, np.nan])
    (dlo, tlo), (dhi, thi) = lb, ub
    tlo = max(tlo, 1e-6)

    def best_d(tau):
        e = np.exp(-x / tau)
        ee = e @ e
        dd = (e @ y) / ee if ee > 0 else 0.0
        dd = min(max(dd, dlo), dhi)
        return dd, np.mean((y - dd * e) ** 2)

    grid = np.geomspace(tlo, thi, 400)
    E = np.exp(-x[None, :] / grid[:, None])
    ee = (E * E).sum(1)
    D = np.clip(np.where(ee > 0, (E @ y) / np.where(ee > 0, ee, 1), 0.0), dlo, dhi)
    errs = ((y[None, :] - D[:, None] * E) ** 2).mean(1)
    k = int(np.argmin(errs))
    a, b = grid[max(k - 1, 0)], grid[min(k + 1, len(grid) - 1)]
    if b > a:
        r = minimize_scalar(lambda t: best_d(t)[1], bounds=(a, b), method="bounded",
                            options={"xatol": 1e-6})
        tau = r.x if r.fun <= errs[k] else grid[k]
    else:
        tau = grid[k]
    return np.array([best_d(tau)[0], tau])


def regress_wt(d, nback=10):
    """Wait time on catch trials in mixed blocks regressed on the current and previous log2
    offers (regress_wt_vs_rew.m): z-scored over those trials; offers outside mixed blocks NaN;
    column j is the offer j-1 trials back, zero-padded at the start; constant last."""
    use = d["optout"] & d["catch"] & (d["block"] == 1)
    WT = np.full(len(use), np.nan)
    WT[use] = nanz(d["wt"][use])
    R = np.log2(d["vol_raw"].astype(float))  # the code uses log2(A.reward), the raw volumes
    R[d["block"] != 1] = np.nan
    n = len(R)
    X = np.empty((n, nback + 1))
    for j in range(nback):
        X[:, j] = np.r_[np.zeros(j), R[:n - j]]
    X[:, -1] = 1
    b, ci, _ = ols(WT[use], X[use])
    return b, ci


def regress_iti(d, nback=10):
    """Initiation time in mixed blocks regressed on previous log2 rewards, unrewarded trials 0
    (regress_latency_vs_rew.m: reward times hits); column j is the reward j trials back, NaN-padded;
    constant last. 99th percentile and z-score over mixed-block trials, as in the code."""
    use = d["block"] == 1
    L = np.full(len(use), np.nan)
    L[use] = nanz(clip99(d["iti"][use]))
    R = np.log2(d["vol_raw"].astype(float)) * d["hit"]  # raw volumes, as the code
    R[d["block"] != 1] = np.nan
    n = len(R)
    X = np.empty((n, nback + 1))
    for j in range(1, nback + 1):
        X[:, j - 1] = np.r_[np.full(j, np.nan), R[:n - j]]
    X[:, -1] = 1
    b, ci, _ = ols(L[use], X[use])
    return b, ci


def zero_after_first_ns(b, ci, start=0, stop=None):
    """Set the first coefficient (from `start`) whose 95% interval contains 0, and all after it up
    to `stop` (exclusive), to 0 (Methods, Trial history effects; the code's b(i:end-1) = 0)."""
    b = b.copy()
    stop = len(b) - 1 if stop is None else stop
    ns = np.flatnonzero((ci[start:, 0] < 0) & (ci[start:, 1] > 0))
    if len(ns):
        i = start + ns[0]
        b[i:stop] = 0
    return b


def taus(d, rng):
    """Per-rat regression coefficients and time constants under the code's and the Methods'
    readings (claims fig2c-d and fig2e)."""
    out = {}
    bw, ciw = regress_wt(d, 10)
    bl, cil = regress_iti(d, 10)
    bl9, cil9 = regress_iti(d, 9)
    out["b_wt_raw"], out["b_iti_raw"], out["b_iti9_raw"] = bw, bl, bl9
    # code (regress_wt_vs_rew.m): zero from the current offer on (the search includes the
    # constant), fit 10*b over coefficients 1 to 10, D in [-10, 10], tau in [0, 10]
    bwc = zero_after_first_ns(bw, ciw, 0)
    p = fit_exp_decay(np.arange(1, 11), 10 * bwc[:10], [-10, 0], [10, 10], 10, rng)
    out["b_wt"] = bwc
    out["tau_wt_code"] = 0.0 if np.all(bwc[1:10] == 0) else p[1]
    # Methods: the 9 previous offers only (columns 2 to 10), zero from the first previous one
    bwm = bw.copy()
    bwm[1:10] = zero_after_first_ns(np.r_[bw[1:10], 0], np.r_[ciw[1:10], [[1, 1]]], 0)[:9]
    out["b_wt_methods"] = bwm
    if np.all(bwm[1:10] == 0):
        out["tau_wt_methods"] = 0.0
    else:
        out["tau_wt_methods"] = fit_exp_decay(np.arange(1, 10), 10 * bwm[1:10], [-10, 0], [10, 10], 10, rng)[1]
    # initiation times, code: nback 10, fit b over lags 1 to 10, D in [-10, 0], tau in [0, 10];
    # tau 0 when lags 2 to 10 are all 0
    blc = zero_after_first_ns(bl, cil, 0)
    out["b_iti"] = blc
    p = fit_exp_decay(np.arange(1, 11), blc[:10], [-10, 0], [0, 10], 10, rng)
    out["tau_iti_code"] = 0.0 if np.all(blc[1:10] == 0) else p[1]
    # Methods: nback 9, fit the 9 previous coefficients; tau 0 when all are 0
    blm = zero_after_first_ns(bl9, cil9, 0)
    out["b_iti9"] = blm
    if np.all(blm[:9] == 0):
        out["tau_iti_methods"] = 0.0
    else:
        out["tau_iti_methods"] = fit_exp_decay(np.arange(1, 10), blm[:9], [-10, 0], [0, 10], 10, rng)[1]
    out["ci_wt"], out["ci_iti"] = ciw, cil
    return out


def tau_shuffle_test(first_q, last_q, betas, nshuffle, rng):
    """myTauShuffleTest.m: labels of the two groups shuffled; the mean coefficients of each half
    refitted (10*b, D in [-3, 1], tau in [0, 50]); the observed fits use b, D in [-10, 1], tau in
    [0, 10]; p = share of |shuffled difference| > |observed| over 2*nshuffle."""
    B = betas[first_q | last_q][:, :10]
    n = len(B)
    x = np.arange(1, 11)
    sh = np.empty((nshuffle, 2))
    for i in range(nshuffle):
        perm = rng.permutation(n)
        g1, g2 = perm[: n // 2], perm[n // 2:]
        sh[i, 0] = fit_exp_decay(x, 10 * np.nanmean(B[g1], 0), [-3, 0], [1, 50], 10, rng)[1]
        sh[i, 1] = fit_exp_decay(x, 10 * np.nanmean(B[g2], 0), [-3, 0], [1, 50], 10, rng)[1]
    o1 = fit_exp_decay(x, np.nanmean(betas[first_q][:, :10], 0), [-10, 0], [1, 10], 10, rng)[1]
    o2 = fit_exp_decay(x, np.nanmean(betas[last_q][:, :10], 0), [-10, 0], [1, 10], 10, rng)[1]
    obs = o1 - o2
    shd = sh[:, 0] - sh[:, 1]
    return float(np.sum(np.abs(shd) > abs(obs)) / (2 * nshuffle)), obs, o1, o2


# ---------------------------------------------------------------------------------------------
# Previous offer (Fig. 2j-l)
# ---------------------------------------------------------------------------------------------

def wt_by_previous(d):
    """waittime_20ul_by_previous_vol.m: 20 uL opt-out catch trials in mixed blocks (not the first
    trial), z-scored over these trials, split by previous offer below or above 20 uL; two-tailed
    rank-sum. Returns (mean below, mean above, p)."""
    from scipy.stats import mannwhitneyu
    f = (d["vol"] == 20) & (d["block"] == 1) & d["optout"] & d["catch"]
    f[0] = False
    w = np.full(len(f), np.nan)
    w[f] = nanz(d["wt"][f])
    a = w[f & (d["prev_vol"] < 20)]
    b = w[f & (d["prev_vol"] > 20)]
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    p = mannwhitneyu(a, b).pvalue if len(a) and len(b) else np.nan
    return _m(a), _m(b), p


def iti_by_previous(d, reading="code"):
    """Initiation time in mixed blocks by previous offer below or above 20 uL, z-scored over all
    the rat's trials after the 99th percentile cut (latency_post20ul_by_previous_vol.m). reading
    "code": all mixed-block trials; "methods": 20 uL trials only (Methods, Trial history effects).
    Two-tailed rank-sum. Returns (mean below, mean above, p)."""
    from scipy.stats import mannwhitneyu
    z = nanz(clip99(d["iti"]))
    m = d["block"] == 1
    if reading == "methods":
        m = m & (d["vol"] == 20)
    a = z[m & (d["prev_vol"] < 20)]
    b = z[m & (d["prev_vol"] > 20)]
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    p = mannwhitneyu(a, b).pvalue if len(a) and len(b) else np.nan
    return _m(a), _m(b), p


# ---------------------------------------------------------------------------------------------
# Catch probability (Fig. 3c)
# ---------------------------------------------------------------------------------------------

PCATCH = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35]


def wt_by_pcatch(d):
    """wtByPCatch.m: mean wait time on catch trials in mixed blocks by offer, per catch
    probability, leaving out the rat's first 1000 trials. Returns {p: 5 means}."""
    keep = np.arange(len(d["vol"])) >= 1000
    out = {}
    for p in PCATCH:
        use = (d["block"] == 1) & np.isclose(d["catch_p"], p) & d["catch"] & keep
        out[p] = np.array([_m(d["wt"][use & (d["vol"] == v)]) for v in VOLUMES])
    return out


# ---------------------------------------------------------------------------------------------
# Block inference (GenerateSynthData_Bayes.m), Bayes observer and retrospective model
# ---------------------------------------------------------------------------------------------

P_REW = np.array([[1 / 5] * 5, [0, 0, 1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3, 0, 0]])  # mixed, high, low
VOL_IDX = {5: 0, 10: 1, 20: 2, 40: 3, 80: 4}


def transition_matrix(h0=1 / 40, reading="code"):
    """Column-stochastic block transitions, order mixed, high, low. "code": the model scripts
    (mixed to high or to low with H0/2 each); "methods": Equation 6 (H0 each, 1 - 2 H0 to stay)."""
    if reading == "code":
        return np.array([[1 - h0, h0, h0], [h0 / 2, 1 - h0, 0], [h0 / 2, 0, 1 - h0]])
    return np.array([[1 - 2 * h0, h0, h0], [h0, 1 - h0, 0], [h0, 0, 1 - h0]])


def infer_blocks(vols, new_session, P):
    """Belief and prior over blocks on each trial (GenerateSynthData_Bayes.m): the belief is reset
    to [1/2, 1/4, 1/4] on a session's first trial, where there is no prior. Order mixed, high,
    low."""
    n = len(vols)
    belief = np.empty((n, 3))
    prior = np.full((n, 3), np.nan)
    idx = [VOL_IDX[int(v)] for v in vols]
    L = P_REW.T.tolist()
    (p00, p01, p02), (p10, p11, p12), (p20, p21, p22) = P.tolist()
    b0 = b1 = b2 = 0.0
    news = np.asarray(new_session).tolist()
    for t in range(n):
        if news[t]:
            b0, b1, b2 = 0.5, 0.25, 0.25
        else:
            q0 = p00 * b0 + p01 * b1 + p02 * b2
            q1 = p10 * b0 + p11 * b1 + p12 * b2
            q2 = p20 * b0 + p21 * b1 + p22 * b2
            prior[t] = (q0, q1, q2)
            l0, l1, l2 = L[idx[t]]
            b0, b1, b2 = l0 * q0, l1 * q1, l2 * q2
            s = b0 + b1 + b2
            b0, b1, b2 = b0 / s, b1 / s, b2 / s
        belief[t] = (b0, b1, b2)
    return belief, prior


def model_trials(d):
    """Trials the model scripts use: those with a wait time (isgood = ~isnan(wait_time))."""
    good = np.isfinite(d["wt"])
    order = d["order"][good]
    new = np.r_[True, order[1:] != order[:-1]]
    return good, d["vol"][good], new


def retrospective_kappa(vols_log2, new_session, belief_mixed, alpha0, model="alphaPH"):
    """Kappa under Equation 9 with the gain of Equation 10 ("alphaPH",
    GenerateLatencyData_AlphaPHModel.m), G = 1 ("vanilla", _VanillaAlpha.m) or G = |delta|
    ("rpe", _RPEAlpha.m), with each script's initial kappa and reset at session starts."""
    n = len(vols_log2)
    kappa = np.full(n, np.nan)
    k0 = {"alphaPH": np.mean(np.log([5, 10, 20, 40, 80])), "vanilla": 20.0, "rpe": 0.5}[model]
    kappa[0] = k0
    for t in range(n - 1):
        if new_session[t]:
            kappa[t] = k0
            a = alpha0
        else:
            if model == "alphaPH":
                a = alpha0 / (1 - abs(belief_mixed[t] - belief_mixed[t - 1]))
                a = min(a, 1.0)
            elif model == "vanilla":
                a = alpha0
        rpe = vols_log2[t] - kappa[t]
        if model == "rpe":
            a = min(abs(rpe) * alpha0, 1.0)
        kappa[t + 1] = kappa[t] + a * rpe
    if model == "alphaPH":
        kappa[kappa < 0] = np.finfo(float).eps
    return kappa


def lognormal_noise(mean, var, rng, nsims=1):
    """generate_wts.m, 'logn': log-normal draws with the given mean and variance, averaged over
    nsims."""
    v = np.log(var / mean ** 2 + 1)
    mu = np.log(mean) - v / 2
    draws = rng.lognormal(mu[None, :], np.sqrt(v)[None, :], size=(nsims, len(mean)))
    return draws.mean(0)


# ---------------------------------------------------------------------------------------------
# Checks of the trial table against the raw Bpod events
# ---------------------------------------------------------------------------------------------

def iti_from_events(asset: dict) -> pd.DataFrame:
    """For one session, the first center poke of each trial measured from the trial start, from
    the raw events table, beside the processed inter_trial_interval. getITI.m defines the time to
    initiate as CenterIn (relative to trial start), minus the last exit from the rewarded port
    when the previous trial was rewarded."""
    raw = _get(s3_url(asset))
    with h5py.File(io.BytesIO(raw), "r") as f:
        ev = f["acquisition/task_recording/events"]
        names = [_s(x) for x in f["general/task/event_types/event_name"][:]]
        et = ev["event_type"][:]
        ts = ev["timestamp"][:]
        val = np.array([_s(x) for x in ev["value"][:]])
        start = f["intervals/trials/start_time"][:]
        stop = f["intervals/trials/stop_time"][:]
        pt = f["intervals/processed_trials"]
        iti = pt["inter_trial_interval"][:]
        hit = pt["is_rewarded"][:].astype(bool)
    center = names.index("center_port_poke")
    cin = np.sort(ts[(et == center) & (val == "In")])
    first_in = np.full(len(start), np.nan)
    for i, (a, b) in enumerate(zip(start, stop)):
        k = np.searchsorted(cin, a)
        if k < len(cin) and cin[k] <= b:
            first_in[i] = cin[k] - a
    prev_hit = np.r_[False, hit[:-1]]
    return pd.DataFrame({"iti": iti, "center_in": first_in, "prev_hit": prev_hit})


# ---------------------------------------------------------------------------------------------
# Pre-initiation cue task (Fig. 5)
# ---------------------------------------------------------------------------------------------

# The 16 rats and their switch dates as Figure5.m lists them (ratListAll, startDates); the code
# indexes startDates(rr) for rat rr, so the first 16 of its 20 dates are paired with the rats in
# order. M045 to M048 (secondGroup) were trained only on the pre-cue task. Outside labels, from
# github.com/constantinoplelab/published at b7b68ca8c107, rat_behavior/Figures/Figure5.m.
PRECUE_RATS = ["M041", "M042", "M043", "M044", "M045", "M046", "M047", "M048", "G070", "E005",
               "E008", "G078", "G076", "G069", "S042", "S050"]
PRECUE_START = ["2022-10-04", "2022-10-04", "2022-10-04", "2022-10-04", "2022-12-13", "2022-12-13",
                "2022-12-13", "2022-12-13", "2022-10-24", "2022-10-24", "2022-10-24", "2022-11-07",
                "2022-11-14", "2022-11-14", "2022-12-21", "2022-12-22"]
PRECUE_ONLY = ["M045", "M046", "M047", "M048"]


def subset_rat(d, keep):
    """The rat's arrays restricted to the trials in `keep` (whole sessions), with the previous
    offer recomputed within the subset."""
    out = {k: v[keep] for k, v in d.items() if isinstance(v, np.ndarray) and len(v) == len(keep)}
    out["prev_vol"] = np.r_[np.nan, out["vol"][:-1].astype(float)]
    return out


def iti_by_reward(d):
    """iti_by_reward.m: z-scored initiation time by current offer in mixed blocks, leaving out each
    session's first trial and trials after violations; 99th percentile cut over the subset;
    one-way ANOVA over offers. Returns (5 means, p, slope over log2 offer)."""
    from scipy.stats import f_oneway
    L = d["iti"].copy()
    L[d["first"]] = np.nan
    L = clip99(L)
    post_vio = np.r_[False, d["vio"][:-1]]
    use = ~post_vio & (d["block"] == 1)
    z = np.full(len(L), np.nan)
    z[use] = nanz(L[use])
    groups = [z[use & (d["vol"] == v)] for v in VOLUMES]
    groups = [g[np.isfinite(g)] for g in groups]
    means = np.array([_m(g) for g in groups])
    p = f_oneway(*groups).pvalue if all(len(g) > 1 for g in groups) else np.nan
    ok = use & np.isfinite(z)
    slope = np.polyfit(np.log2(d["vol"][ok].astype(float)), z[ok], 1)[0] if ok.sum() > 10 else np.nan
    return means, p, slope
