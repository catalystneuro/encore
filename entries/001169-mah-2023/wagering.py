"""Loading and measures for the temporal wagering task of dandiset 001169.

Mah, Schiereck, Bossio & Constantinople (2023), Nature Communications 14:7573,
doi:10.1038/s41467-023-43250-x.

Each NWB file holds one session of one rat. The analysis uses the table
`intervals/processed_trials`, which the conversion
(https://github.com/catalystneuro/constantinople-lab-to-nwb, commit bf2bf76) filled from the
paper's processed per-rat structs (`A_Structs_Final` in Zenodo 10.5281/zenodo.10031483), the
catch probability from the raw trials table (`intervals/trials/catch_percentage`), and the
task argument `center_port_cue` of the pre-initiation cue sessions. Each file is about 1 MB
and is read whole into memory from the archive at the pinned version, in parallel; nothing is
written to disk.

Where the parameters come from. The paper's analysis code is
https://github.com/constantinoplelab/published/tree/main/rat_behavior at commit
b7b68ca8c107d8ce4a061e16da214307f175c3e5; the function it follows is named in each docstring.

- Rewards of 4, 8, 16, 32 and 64 uL (some female rats) are treated as 5, 10, 20, 40 and
  80 uL (Methods; `convertreward.m`).
- Trial initiation times above the 99th percentile of the rat's pooled distribution are
  removed (Methods; `iticurves.m` and others).
- `wait_time` is the conversion's copy of the processed wait time, already thresholded at the
  rat's mean + 1 SD (Methods, Statistical analyses).
- Blocks: 1 mixed, 2 high, 3 low, as in the paper's structs.
- Block transitions in the first 40 trials of a session are ignored (`blockhmat_withvios.m`).
- Model constants (H0 = 1/40, delay time constant 2.5 s, log-normal noise of variance 8 s,
  reward and block probabilities) are from the Methods and the generative model code
  (`GenerateSynthData_Bayes.m`, `GenerateSynthData_AlphaPHModel.m`).
"""

from __future__ import annotations

import io
import threading
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import optimize, stats

DANDISET_ID = "001169"
DANDISET_VERSION = "0.260825.1909"

BLOCK_CODE = {"Mixed": 1, "High": 2, "Low": 3}
STANDARD_VOLUMES = np.array([5, 10, 20, 40, 80])
VOLUME_TO_STANDARD = {4: 5, 5: 5, 8: 10, 10: 10, 16: 20, 20: 20, 32: 40, 40: 40, 64: 80, 80: 80}

TRIAL_COLUMNS = ["block_type", "reward_volume_ul", "is_catch", "is_rewarded", "is_violation",
                 "is_opt_out", "wait_time", "wait_time_unthresholded", "wait_time_threshold",
                 "inter_trial_interval", "wait_for_center_poke", "training_stage", "start_time"]


# ----------------------------------------------------------------------------------------
# Loading
# ----------------------------------------------------------------------------------------

def blob_url(blob_id: str) -> str:
    return f"https://dandiarchive.s3.amazonaws.com/blobs/{blob_id[:3]}/{blob_id[3:6]}/{blob_id}"


def asset_list() -> pd.DataFrame:
    """Path, size and content URL of every asset at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = [{"path": a.path, "size": a.size, "blob": a.blob} for a in dandiset.get_assets()]
    assets = pd.DataFrame(rows).sort_values("path").reset_index(drop=True)
    assets["url"] = assets.blob.map(blob_url)
    return assets


def _text(value) -> str:
    return value.decode() if isinstance(value, bytes) else str(value)


def read_session(content: bytes) -> tuple[dict, pd.DataFrame]:
    """Session metadata and the processed trials of one NWB file held in memory."""
    with h5py.File(io.BytesIO(content), "r") as f:
        g = f["intervals/processed_trials"]
        trials = pd.DataFrame({c: g[c][:] for c in TRIAL_COLUMNS})
        raw = f["intervals/trials"]
        trials["catch_percentage"] = raw["catch_percentage"][:]
        args = f["general/task/task_arguments"]
        arguments = {_text(n): _text(e) for n, e in zip(args["argument_name"][:], args["expression"][:])}
        subject = f["general/subject"]
        meta = {
            "subject_id": _text(subject["subject_id"][()]),
            "sex": _text(subject["sex"][()]),
            "species": _text(subject["species"][()]),
            "session_id": _text(f["general/session_id"][()]),
            "session_start": _text(f["session_start_time"][()]),
            "protocol": _text(f["general/protocol"][()]),
            "n_raw_trials": len(raw["start_time"]),
            "center_port_cue": arguments.get("center_port_cue", "absent"),
            "has_age": "age" in subject,
            "processed_columns": tuple(sorted(g.keys())),
        }
    trials["block_type"] = [BLOCK_CODE[_text(b)] for b in trials["block_type"]]
    return meta, trials


_local = threading.local()


def _fetch(url: str) -> bytes:
    if not hasattr(_local, "session"):
        _local.session = requests.Session()
    for attempt in range(5):
        response = _local.session.get(url, timeout=120)
        if response.ok:
            return response.content
    response.raise_for_status()


def _load_one(row) -> tuple[dict, pd.DataFrame]:
    meta, trials = read_session(_fetch(row.url))
    meta["path"] = row.path
    return meta, trials


def load_all(assets: pd.DataFrame, max_workers: int = 48) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Sessions and trials of every asset. Trials are in session order (by start time) and
    in trial order within a session; `session` indexes the sessions table."""
    with ThreadPoolExecutor(max_workers) as pool:
        results = list(pool.map(_load_one, assets.itertuples()))
    sessions = pd.DataFrame([m for m, _ in results])
    sessions["n_trials"] = [len(t) for _, t in results]
    sessions["start"] = pd.to_datetime(sessions.session_start, utc=True)
    order = sessions.sort_values(["subject_id", "start", "session_id"]).index.to_numpy()
    sessions = sessions.loc[order].reset_index().rename(columns={"index": "file_index"})
    parts = []
    for k, i in enumerate(order):
        t = results[i][1]
        t.insert(0, "session", np.int32(k))
        t.insert(1, "trial", np.arange(len(t), dtype=np.int32))
        parts.append(t)
    trials = pd.concat(parts, ignore_index=True)
    trials["rat"] = sessions.subject_id.to_numpy()[trials.session]
    trials["reward"] = trials.reward_volume_ul.map(VOLUME_TO_STANDARD).astype(np.int16)
    for c in ["wait_time", "wait_time_unthresholded", "wait_time_threshold", "inter_trial_interval",
              "wait_for_center_poke", "start_time", "catch_percentage"]:
        trials[c] = trials[c].astype(np.float32 if c != "start_time" else np.float64)
    trials["block_type"] = trials.block_type.astype(np.int8)
    trials["rat"] = trials.rat.astype("category")
    return sessions, trials


def drop_duplicate_sessions(sessions: pd.DataFrame, trials: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Remove sessions that repeat an earlier session of the same rat trial for trial (same trial
    count, rewards, blocks and trial initiation times). Returns the kept sessions, their
    trials (sessions renumbered) and the removed sessions."""
    g = trials.groupby("session", sort=True)
    fingerprint = pd.DataFrame({
        "n": g.size(),
        "rewards": g.reward_volume_ul.apply(lambda s: hash(s.to_numpy().tobytes())),
        "blocks": g.block_type.apply(lambda s: hash(s.to_numpy().tobytes())),
        "iti": g.inter_trial_interval.apply(lambda s: hash(np.nan_to_num(s.to_numpy(), nan=-1).tobytes())),
    })
    fingerprint["subject_id"] = sessions.subject_id.to_numpy()
    duplicated = fingerprint.duplicated(keep="first").to_numpy()
    removed = sessions[duplicated]
    keep = np.flatnonzero(~duplicated)
    new_index = np.full(len(sessions), -1)
    new_index[keep] = np.arange(len(keep))
    trials = trials[~duplicated[trials.session.to_numpy()]].copy()
    trials["session"] = new_index[trials.session.to_numpy()].astype(np.int32)
    return sessions.iloc[keep].reset_index(drop=True), trials.reset_index(drop=True), removed


# ----------------------------------------------------------------------------------------
# Per-rat arrays
# ----------------------------------------------------------------------------------------

def rat_arrays(trials: pd.DataFrame, sessions: pd.DataFrame) -> dict[str, dict]:
    """For each rat, its trials in order as numpy arrays (the fields of the paper's A struct)."""
    cue = sessions.center_port_cue.eq("True").to_numpy()
    out = {}
    for rat, t in trials.groupby("rat", observed=True, sort=True):
        session = t.session.to_numpy()
        _, sess_local = np.unique(session, return_inverse=True)
        out[rat] = {
            "session": sess_local,
            "trial": t.trial.to_numpy(),
            "reward": t.reward.to_numpy().astype(float),            # 5 to 80 uL
            "volume": t.reward_volume_ul.to_numpy().astype(float),  # as offered (4 to 80 uL)
            "block": t.block_type.to_numpy().astype(int),
            "catch": t.is_catch.to_numpy(),
            "vios": t.is_violation.to_numpy(),
            "hits": t.is_rewarded.to_numpy(),
            "optout": t.is_opt_out.to_numpy(),
            "wait_time": t.wait_time.to_numpy().astype(float),
            "iti": t.inter_trial_interval.to_numpy().astype(float),
            "prob_catch": np.round(t.catch_percentage.to_numpy().astype(float), 3),
            "cue": cue[session],
        }
    return out


def subset(A: dict, mask: np.ndarray) -> dict:
    """The trials of a rat selected by a boolean mask, sessions renumbered."""
    B = {k: v[mask] for k, v in A.items()}
    _, B["session"] = np.unique(B["session"], return_inverse=True)
    return B


def clean_iti(iti: np.ndarray) -> np.ndarray:
    """Trial initiation times with values above the 99th percentile set to NaN (Methods)."""
    out = iti.copy()
    out[out > np.nanpercentile(out, 99)] = np.nan
    return out


def zscore(x: np.ndarray) -> np.ndarray:
    return (x - np.nanmean(x)) / np.nanstd(x, ddof=1)


def ranksum(x, y, alternative="two-sided") -> float:
    x, y = np.asarray(x, float), np.asarray(y, float)
    x, y = x[~np.isnan(x)], y[~np.isnan(y)]
    if len(x) == 0 or len(y) == 0:
        return np.nan
    return stats.mannwhitneyu(x, y, alternative=alternative).pvalue


def signrank(x, y=None) -> float:
    x = np.asarray(x, float)
    d = x if y is None else x - np.asarray(y, float)
    d = d[~np.isnan(d)]
    return stats.wilcoxon(d).pvalue


def matlab_smooth(y: np.ndarray, span: int = 5) -> np.ndarray:
    """Moving average as MATLAB's smooth(y, span): an even span is reduced by one and the
    window shrinks symmetrically at the ends. NaNs are left out of each window's mean."""
    y = np.asarray(y, float)
    if span % 2 == 0:
        span -= 1
    half = span // 2
    n = len(y)
    out = np.full(n, np.nan)
    for i in range(n):
        h = min(half, i, n - 1 - i)
        w = y[i - h:i + h + 1]
        if np.any(~np.isnan(w)):
            out[i] = np.nanmean(w)
    return out


# ----------------------------------------------------------------------------------------
# Figure 1: block sensitivity
# ----------------------------------------------------------------------------------------

def wait_curves(A: dict) -> dict:
    """Mean wait time per block and reward on catch trials the rat opted out of (wtcurves.m),
    the same on wait times z-scored over all catch trials (Methods), and the one-tailed
    rank-sum p of 20 uL high < low."""
    use = A["optout"] & A["catch"]
    z = np.full(len(use), np.nan)
    z[A["catch"]] = zscore(A["wait_time"][A["catch"]])
    out = {}
    for b in (1, 2, 3):
        for r in STANDARD_VOLUMES:
            sel = use & (A["block"] == b) & (A["reward"] == r)
            out[(b, r)] = np.nanmean(A["wait_time"][sel]) if sel.any() else np.nan
            out[("z", b, r)] = np.nanmean(z[sel]) if sel.any() else np.nan
    wt = A["wait_time"]
    out["p"] = ranksum(wt[use & (A["block"] == 2) & (A["reward"] == 20)],
                       wt[use & (A["block"] == 3) & (A["reward"] == 20)], "less")
    return out


def initiation_by_block(A: dict) -> dict:
    """Mean trial initiation time per block, raw and z-scored, over all trials (iticurves.m),
    and the one-tailed rank-sum p of high < low."""
    L = clean_iti(A["iti"])
    z = zscore(L)
    out = {}
    for b in (1, 2, 3):
        out[b] = np.nanmean(L[A["block"] == b])
        out[("z", b)] = np.nanmean(z[A["block"] == b])
    out["p"] = ranksum(L[A["block"] == 2], L[A["block"] == 3], "less")
    return out


def initiation_by_previous_outcome(A: dict) -> dict:
    """FigureS2.m: z-scored initiation time in low and high blocks after rewarded and after
    unrewarded trials (the previous trial in the rat's sequence)."""
    L = clean_iti(A["iti"])
    z = zscore(L)
    prev_hit = np.r_[False, A["hits"][:-1]]
    prev_unrew = np.r_[False, ~A["hits"][:-1]]
    out = {}
    for name, m in (("rewarded", prev_hit), ("unrewarded", prev_unrew)):
        sel = m & ~np.isnan(L)
        out[name] = (np.nanmean(z[sel & (A["block"] == 3)]), np.nanmean(z[sel & (A["block"] == 2)]))
    return out


# ----------------------------------------------------------------------------------------
# Figure 2: previous-offer sensitivity, transitions, regressions
# ----------------------------------------------------------------------------------------

def wait_by_previous_offer(A: dict) -> tuple[float, float, float]:
    """waittime_20ul_by_previous_vol.m: z-scored wait times on 20 uL catch trials in mixed
    blocks (opted out), after offers below and above 20 uL, and the two-tailed rank-sum p."""
    idx = np.flatnonzero((A["reward"] == 20) & (A["block"] == 1) & A["optout"] & A["catch"])
    idx = idx[idx > 0]
    wt = A["wait_time"]
    z = (wt - np.nanmean(wt[idx])) / np.nanstd(wt[idx], ddof=1)
    prev = A["reward"][idx - 1]
    lo, hi = z[idx[prev < 20]], z[idx[prev > 20]]
    return np.nanmean(lo), np.nanmean(hi), ranksum(lo, hi)


def initiation_by_previous_offer(A: dict, only_20ul: bool = True) -> tuple[float, float, float]:
    """latency_post20ul_by_previous_vol.m: z-scored initiation times in mixed blocks after
    offers below and above 20 uL, and the two-tailed rank-sum p. With only_20ul, trials
    offering 20 uL only (Methods); without, all mixed-block trials (the code)."""
    L = clean_iti(A["iti"])
    z = zscore(L)
    prev = np.r_[np.nan, A["reward"][:-1]]
    base = A["block"] == 1
    if only_20ul:
        base = base & (A["reward"] == 20)
    lo, hi = z[base & (prev < 20)], z[base & (prev > 20)]
    return np.nanmean(lo), np.nanmean(hi), ranksum(lo, hi)


def _transitions(A: dict) -> dict[int, np.ndarray]:
    """Global indices of the first trial of each new block, by kind (blockhmat_withvios.m):
    +1 mixed to high, +2 mixed to low, -1 high to mixed, -2 low to mixed. Transitions in the
    first 40 trials of a session are ignored, as in the code."""
    block, session, trial = A["block"], A["session"], A["trial"]
    d = np.r_[0, np.diff(block)]
    d[np.r_[True, session[1:] != session[:-1]]] = 0
    within = np.zeros(len(block), int)
    starts = np.flatnonzero(np.r_[True, session[1:] != session[:-1]])
    for s, e in zip(starts, np.r_[starts[1:], len(block)]):
        within[s:e] = np.arange(e - s)
    d[within < 40] = 0
    return {k: np.flatnonzero(d == k) for k in (1, 2, -1, -2)}


def wait_dynamics(A: dict, twin: int = 20, smoothfactor: int = 10) -> dict[int, np.ndarray]:
    """block_dynamics_wt.m: change in z-scored wait time on catch trials around transitions,
    relative to the mean for each reward; windows on the rat's pooled trial sequence."""
    wt = A["wait_time"].copy()
    c = A["catch"]
    wt[c] = zscore(wt[c])
    good = c & ~A["vios"]
    for r in STANDARD_VOLUMES:
        m = good & (A["reward"] == r)
        if m.sum() > 1:
            wt[m] = zscore(wt[m])
    n = len(wt)
    out = {}
    for kind, idx in _transitions(A).items():
        rows = np.full((max(len(idx), 1), 2 * twin + 1), np.nan)
        for j, t in enumerate(idx):
            these = np.arange(t - twin, t + twin + 1)
            ok = (these >= 0) & (these < n)
            ok[ok] &= good[these[ok]]
            rows[j, ok] = wt[these[ok]]
        mean = np.nanmean(rows, axis=0) if len(idx) else np.full(2 * twin + 1, np.nan)
        mean[twin] = mean[twin - 2]
        out[kind] = matlab_smooth(mean, smoothfactor)
    return out


def initiation_dynamics(A: dict, twin: int = 20, smoothfactor: int = 10, detrend: bool = True) -> dict[int, np.ndarray]:
    """block_dynamics_latency.m: z-scored initiation time around transitions, within sessions,
    after subtracting a linear fit on trial number pooled over sessions (satiety detrend)."""
    l = A["iti"].copy()
    session, trial = A["session"], A["trial"]
    l[np.r_[True, session[1:] != session[:-1]]] = np.nan
    l[l > np.nanpercentile(l, 99)] = np.nan
    z = zscore(l)
    n_sess = session.max() + 1
    lengths = np.bincount(session, minlength=n_sess)
    width = lengths.max()
    mat = np.full((n_sess, width), np.nan)
    within = np.zeros(len(l), int)
    starts = np.r_[0, np.cumsum(lengths)[:-1]]
    within = np.arange(len(l)) - starts[session]
    mat[session, within] = z
    x = np.tile(np.arange(1, width + 1), n_sess)
    s = mat.ravel()
    ok = ~np.isnan(s)
    if detrend:
        b = np.polyfit(x[ok], s[ok], 1)
        regline = b[0] * np.arange(1, width + 1) + b[1]
    else:
        regline = np.zeros(width)
    out = {}
    for kind, idx in _transitions(A).items():
        rows = []
        for t in idx:
            ss, w = session[t], within[t]
            these = np.arange(w - twin, w + twin + 1)
            ok = (these >= 0) & (these < width)
            row = np.full(2 * twin + 1, np.nan)
            row[ok] = mat[ss, these[ok]] - regline[these[ok]]
            rows.append(row)
        mean = np.nanmean(rows, axis=0) if rows else np.full(2 * twin + 1, np.nan)
        if kind == 2:
            mean[twin] = mean[twin - 2]
        else:
            mean[twin] = mean[twin - 1]
        mean[twin - 1] = np.nan
        out[kind] = matlab_smooth(mean, smoothfactor)
    return out


def ols(y: np.ndarray, X: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Least squares as MATLAB's regress: rows with any NaN dropped; coefficients and their
    95% confidence intervals."""
    ok = ~np.isnan(y) & ~np.isnan(X).any(axis=1)
    y, X = y[ok], X[ok]
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    dof = len(y) - X.shape[1]
    resid = y - X @ b
    s2 = resid @ resid / dof
    cov = s2 * np.linalg.pinv(X.T @ X)
    half = stats.t.ppf(0.975, dof) * np.sqrt(np.diag(cov))
    return b, np.c_[b - half, b + half]


def fit_exp_decay(x, y, lower=(-50, -50), upper=(50, 50)) -> np.ndarray:
    """y = a exp(-x / tau) by least squares within bounds, as fit_exp_decay.m. The code uses
    fmincon from 10 random starts; here tau is searched on a grid of 5000 values within its
    bounds with a solved in closed form (and clipped to its bounds) at each, which finds the
    global minimum without random starts. Returns (a, tau)."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = ~np.isnan(y)
    x, y = x[ok], y[ok]
    taus = np.linspace(max(lower[1], 0.01), upper[1], 5000)
    E = np.exp(-x[None, :] / taus[:, None])
    a = np.clip((E @ y) / np.sum(E ** 2, axis=1), lower[0], upper[0])
    mse = np.mean((y[None, :] - a[:, None] * E) ** 2, axis=1)
    k = int(np.nanargmin(np.where(np.isfinite(mse), mse, np.inf)))
    return np.array([a[k], taus[k]])


def regress_wait_on_rewards(A: dict, nback: int, zero: bool = True) -> tuple[np.ndarray, float]:
    """regress_wt_vs_rew.m: z-scored wait times on mixed-block catch trials (opted out)
    regressed on the current and nback-1 previous log2 offers (rewards outside mixed blocks
    NaN, the first trials padded with 0, as the code), with a constant. Coefficients from the
    first one whose 95% CI contains 0 are set to 0 (unless zero is False); tau from an
    exponential fit, set to 0 when every coefficient from 2 back on is 0 (the code's b(2:end-1),
    which for initiation times leaves out the coefficient 1 back)."""
    use = A["optout"] & A["catch"] & (A["block"] == 1)
    WT = np.full(len(use), np.nan)
    WT[use] = zscore(A["wait_time"][use])
    R = np.log2(A["volume"])
    R[A["block"] != 1] = np.nan
    X = np.full((len(R), nback + 1), np.nan)
    for j in range(nback):
        X[:, j] = np.r_[np.zeros(j), R[:len(R) - j]]
    X[:, -1] = 1.0
    b, ci = ols(WT[use], X[use])
    nonsig = np.flatnonzero((ci[:, 0] < 0) & (ci[:, 1] > 0))
    if len(nonsig) and zero:
        b[nonsig[0]:-1] = 0
    fit = fit_exp_decay(np.arange(1, nback + 1), 10 * b[:nback], (-10, 0), (10, 10))
    tau = 0.0 if np.all(b[1:-1] == 0) else fit[1]
    return b, tau


def regress_initiation_on_rewards(A: dict, nback: int, zero: bool = True) -> tuple[np.ndarray, float]:
    """regress_latency_vs_rew.m: z-scored initiation times in mixed blocks regressed on the
    nback previous log2 rewards received (0 after unrewarded trials; NaN outside mixed blocks
    and before the first trial), with a constant; zeroing and tau as for wait times."""
    use = A["block"] == 1
    L = A["iti"][use].copy()
    L[L > np.nanpercentile(L, 99)] = np.nan
    L = zscore(L)
    R = np.log2(A["volume"]) * A["hits"]
    R[A["block"] != 1] = np.nan
    X = np.full((len(R), nback + 1), np.nan)
    for j in range(1, nback + 1):
        X[:, j - 1] = np.r_[np.full(j, np.nan), R[:len(R) - j]]
    X[:, -1] = 1.0
    b, ci = ols(L, X[use])
    nonsig = np.flatnonzero((ci[:, 0] < 0) & (ci[:, 1] > 0))
    if len(nonsig) and zero:
        b[nonsig[0]:-1] = 0
    fit = fit_exp_decay(np.arange(1, nback + 1), b[:nback], (-10, 0), (0, 10))
    tau = 0.0 if np.all(b[1:-1] == 0) else fit[1]
    return b, tau


def tau_shuffle_test(first: np.ndarray, last: np.ndarray, betas: np.ndarray, n_shuffle: int, rng,
                     consistent: bool = False, amp_upper: float = 1) -> tuple[float, float]:
    """myTauShuffleTest.m: tau of an exponential fit to the mean coefficients (without the
    constant) of the two groups, against random halves of the same rats; p as the code
    computes it, the count of |shuffled difference| > |observed| over 2 * n_shuffle. The code
    fits the shuffled groups to 10 x coefficients with bounds (-3, 0) to (1, 50) and the
    observed groups to the coefficients with bounds (-10, 0) to (1, 10); with consistent=True
    the observed groups are fit as the shuffled ones. amp_upper replaces the code's upper bound
    of 1 on the amplitude in every fit."""
    B = betas[first | last][:, :-1]
    x = np.arange(1, B.shape[1] + 1)
    n = len(B)
    shuffled = np.empty(n_shuffle)
    for i in range(n_shuffle):
        perm = rng.permutation(n)
        g1, g2 = perm[: n // 2], perm[n // 2:]
        t1 = fit_exp_decay(x, 10 * B[g1].mean(0), (-3, 0), (amp_upper, 50))[1]
        t2 = fit_exp_decay(x, 10 * B[g2].mean(0), (-3, 0), (amp_upper, 50))[1]
        shuffled[i] = t1 - t2
    if consistent:
        t1 = fit_exp_decay(x, 10 * betas[first][:, :-1].mean(0), (-3, 0), (amp_upper, 50))[1]
        t2 = fit_exp_decay(x, 10 * betas[last][:, :-1].mean(0), (-3, 0), (amp_upper, 50))[1]
    else:
        t1 = fit_exp_decay(x, betas[first][:, :-1].mean(0), (-10, 0), (amp_upper, 10))[1]
        t2 = fit_exp_decay(x, betas[last][:, :-1].mean(0), (-10, 0), (amp_upper, 10))[1]
    observed = t1 - t2
    return observed, np.sum(np.abs(shuffled) > abs(observed)) / (2 * n_shuffle)


# ----------------------------------------------------------------------------------------
# Figure 3: wait time models
# ----------------------------------------------------------------------------------------

H0 = 1 / 40
DELAY_TAU = 2.5
NOISE_VARIANCE = 8.0
P_REWARD = np.array([[1 / 5] * 5, [0, 0, 1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3, 0, 0]])
P_BLOCK = np.array([[1 - H0, H0, H0], [H0 / 2, 1 - H0, 0], [H0 / 2, 0, 1 - H0]])
REWARD_INDEX = {5: 0, 10: 1, 20: 2, 40: 3, 80: 4}


def model_inputs(A: dict) -> dict:
    """What the wait time models use: the non-violation trials in order (beliefs and the
    running average are updated over these), the session starts among them, the offered
    volumes, and the catch trials the rat opted out of with a wait time (fitted)."""
    good = ~A["vios"]
    session = A["session"][good]
    starts = np.r_[True, session[1:] != session[:-1]]
    volume = A["volume"][good]
    fitted = (A["catch"] & A["optout"] & ~np.isnan(A["wait_time"]))[good]
    return {
        "good": good,
        "rew_idx": np.array([REWARD_INDEX[r] for r in A["reward"][good].astype(int)]),
        "R": np.log2(volume),
        "starts": starts,
        "fitted": fitted,
        "wt": A["wait_time"][good],
        "C": np.max(1 - A["prob_catch"]),
        "min_R": np.log2(volume.min()),
        "n_trials": len(A["reward"]),
    }


def beliefs(M: dict, lam: np.ndarray | None = None) -> np.ndarray:
    """Posterior over (mixed, high, low) on each trial. With lam None, the optimal model of
    GenerateSynthData_Bayes.m (belief reset to [1/2, 1/4, 1/4] at a session start); with a
    vector of lambdas, the suboptimal-prior model of
    GenerateSynthData_Bayes_subopt_onlylambda_flat.m for each (reset to [1/3, 1/3, 1/3]);
    returns (n_lambda, n_trials, 3) then."""
    lik = P_REWARD[:, M["rew_idx"]].T
    n = len(lik)
    if lam is None:
        out = np.empty((n, 3))
        b = np.array([0.5, 0.25, 0.25])
        for t in range(n):
            if M["starts"][t]:
                b = np.array([0.5, 0.25, 0.25])
            else:
                b = lik[t] * (P_BLOCK @ b)
                b = b / b.sum()
            out[t] = b
        return out
    lam = np.asarray(lam, float)[:, None]
    out = np.empty((len(lam), n, 3))
    flat = np.full(3, 1 / 3)
    b = np.tile(flat, (len(lam), 1))
    for t in range(n):
        if M["starts"][t]:
            b = np.tile(flat, (len(lam), 1))
        else:
            prior = lam * (b @ P_BLOCK.T) + (1 - lam) * flat
            b = lik[t] * prior
            b = b / b.sum(axis=1, keepdims=True)
        out[:, t] = b
    return out


def lognormal_nll(wt_obs: np.ndarray, wt_pred: np.ndarray) -> float:
    """Negative log likelihood of observed wait times under log-normal noise with mean wt_pred
    and variance NOISE_VARIANCE (generate_wts.m)."""
    pred = np.clip(wt_pred, 1e-3, None)
    s2 = np.log(NOISE_VARIANCE / pred ** 2 + 1)
    mu = np.log(pred) - s2 / 2
    x = wt_obs
    ll = -np.log(x) - 0.5 * np.log(2 * np.pi * s2) - (np.log(x) - mu) ** 2 / (2 * s2)
    return -np.sum(ll)


def _wait_from_kappa(R, kappa, C, D):
    with np.errstate(divide="ignore", invalid="ignore"):
        arg = (R - kappa * DELAY_TAU) / (kappa * DELAY_TAU) * C / (1 - C)
        wt = D * DELAY_TAU * np.log(arg)
    return np.where(np.isfinite(wt), wt, 1e-3)


def inferential_nll(params, M, inferred) -> float:
    """GenerateSynthData_Bayes.m: kappa of the most probable block; params in [0, 1] are
    (kappa mixed, kappa high, kappa low, D/10)."""
    f = M["fitted"]
    scale = M["C"] * M["min_R"] / DELAY_TAU
    kappa = np.asarray(params[:3])[inferred[f]] * scale
    wt = _wait_from_kappa(M["R"][f], kappa, M["C"], 10 * params[3])
    return lognormal_nll(M["wt"][f], wt)


def fit_inferential(M: dict, inferred: np.ndarray, rng, starts: int = 20, x0=None) -> tuple[np.ndarray, float]:
    bounds = [(1e-4, 1)] * 4
    best, best_val = None, np.inf
    inits = [np.asarray(x0)] if x0 is not None else []
    inits += [rng.random(4) for _ in range(starts)]
    for p0 in inits:
        res = optimize.minimize(inferential_nll, np.clip(p0, 1e-4, 1), args=(M, inferred),
                                method="L-BFGS-B", bounds=bounds)
        if res.fun < best_val:
            best, best_val = res.x, res.fun
    return best, best_val


K0_CODE = np.mean(np.log([5, 10, 20, 40, 80]))    # natural log, as the code; the offers are in log2


def retrospective_kappa(M: dict, alphas: np.ndarray, belief_mixed: np.ndarray, k0: float = K0_CODE) -> np.ndarray:
    """GenerateSynthData_AlphaPHModel.m: running average of log2 offers with the learning rate
    alpha0 / (1 - |change in P(mixed)|), capped at 1, reset at session starts to k0; then scaled
    as the code does. The code's k0 is the mean of the natural logs of 5 to 80 uL (3.0) while the
    offers are log2 (mean 4.32). Returns (n_alpha, n_trials)."""
    alphas = np.asarray(alphas, float)
    R = M["R"]
    n = len(R)
    kappa = np.empty((len(alphas), n))
    kappa[:, 0] = k0
    k = np.full(len(alphas), k0)
    for t in range(n - 1):
        if M["starts"][t]:
            k = np.full(len(alphas), k0)
            a = alphas
        else:
            a = np.minimum(alphas / (1 - abs(belief_mixed[t] - belief_mixed[t - 1])), 1)
        kappa[:, t] = k
        k = k + a * (R[t] - k)
    kappa[:, n - 1] = k
    kappa = kappa / kappa.max(axis=1, keepdims=True) * (R.min() * M["C"] / DELAY_TAU)
    kappa[kappa < 0] = np.finfo(float).eps
    return kappa


def fit_retrospective(M: dict, belief_mixed: np.ndarray, alphas: np.ndarray, k0: float = K0_CODE) -> tuple[np.ndarray, float]:
    """Grid over the baseline learning rate; D/15 in [0, 1] fit at each by bounded search."""
    f = M["fitted"]
    kappas = retrospective_kappa(M, alphas, belief_mixed, k0)[:, f]
    R, wt_obs = M["R"][f], M["wt"][f]
    best, best_val = None, np.inf
    for a, kap in zip(alphas, kappas):
        def nll(d):
            wt = _wait_from_kappa(R, kap, M["C"], 15 * d)
            return lognormal_nll(wt_obs, np.where(wt < 0, np.finfo(float).eps, wt))
        res = optimize.minimize_scalar(nll, bounds=(1e-4, 1), method="bounded")
        if res.fun < best_val:
            best, best_val = np.array([a, res.x]), res.fun
    return best, best_val


def sigmoid(x, p):
    return p[3] + (p[0] - p[3]) / (1 + np.exp(np.clip(-p[1] * (x - p[2]), -500, 500)))


def _sigmoid_sse(p, x, y):
    s = 1 / (1 + np.exp(np.clip(-p[1] * (x - p[2]), -500, 500)))
    r = y - (p[3] + (p[0] - p[3]) * s)
    ds = s * (1 - s)
    grad = -2 * np.array([r @ s, r @ ((p[0] - p[3]) * ds * (x - p[2])), r @ (-(p[0] - p[3]) * ds * p[1]), r @ (1 - s)])
    return r @ r, grad


def fit_sigmoid(x, y, rng, iters: int = 10) -> np.ndarray:
    """my_fit_sigmoid.m: (right asymptote, slope, midpoint, left asymptote) by least squares
    from random starts within bounds (-5, 0, 0, -5) to (5, 5, 30, 5)."""
    lb, ub = np.array([-5, 0, 0, -5.0]), np.array([5, 5, 30, 5.0])
    best, best_val = None, np.inf
    for _ in range(iters):
        p0 = rng.random(4) * (ub - lb) + lb
        res = optimize.minimize(_sigmoid_sse, p0, args=(x, y), jac=True, method="L-BFGS-B", bounds=list(zip(lb, ub)))
        if res.fun < best_val:
            best, best_val = res.x, res.fun
    return best


def lambda_shuffle_test(lo: np.ndarray, hi: np.ndarray, n_perm: int, twin: int, rng) -> tuple[np.ndarray, np.ndarray]:
    """myLambdaShuffleTest.m: sigmoid parameters of the two groups' mean curves (central
    2 * (twin - 10) + 1 trials) against random halves; returns the observed difference (high
    minus low lambda) and the code's p per parameter."""
    xs = np.arange(-(twin - 10), twin - 10 + 1)
    allr = np.vstack([lo, hi])[:, 10:-10]
    n = len(allr)
    diffs = np.empty((n_perm, 4))
    for i in range(n_perm):
        perm = rng.permutation(n)
        g1 = np.nanmean(allr[perm[: n // 2]], axis=0)
        g2 = np.nanmean(allr[perm[n // 2:]], axis=0)
        diffs[i] = fit_sigmoid(xs, g1, rng) - fit_sigmoid(xs, g2, rng)
    true = fit_sigmoid(xs, np.nanmean(hi[:, 10:-10], axis=0), rng) - fit_sigmoid(xs, np.nanmean(lo[:, 10:-10], axis=0), rng)
    p = np.sum(np.abs(diffs) > np.abs(true), axis=0) / (2 * n_perm)
    return true, p


# ----------------------------------------------------------------------------------------
# The paper's processed data on Zenodo (outside input)
# ----------------------------------------------------------------------------------------

ZENODO_URL = "https://zenodo.org/records/10031483/files/published.zip?download=1"
STRUCT_FIELDS = ["reward", "block", "catch", "vios", "hits", "optout", "wait_time", "ITI", "trainingstage",
                 "prob_catch", "ntrials", "wait_thresh"]


def _get_range(url: str, first: int, last: int) -> bytes:
    """Bytes first to last (inclusive) of a URL, retrying when the server asks to slow down."""
    import time
    for attempt in range(8):
        r = requests.get(url, headers={"Range": f"bytes={first}-{last}"}, timeout=600)
        if r.status_code == 206:
            return r.content
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(float(r.headers.get("Retry-After", 10 * (attempt + 1))))
            continue
        r.raise_for_status()
        raise IOError(f"range request answered with status {r.status_code}")
    raise IOError(f"range request failed after retries: {url}")


def load_zenodo_structs(folder: str) -> dict[str, dict]:
    """The per-rat structs in `published/<folder>/` of Zenodo 10.5281/zenodo.10031483. The zip's
    directory is read first; the members of the folder, which lie together in the archive,
    are then read with one range request and decompressed in memory."""
    import struct
    import zlib

    import scipy.io as sio

    head = requests.head(ZENODO_URL, allow_redirects=True, timeout=60)
    size = int(head.headers["Content-Length"])
    tail = _get_range(ZENODO_URL, size - 65536, size - 1)
    eocd = tail.rfind(b"PK\x05\x06")
    cd_size, cd_offset = struct.unpack("<II", tail[eocd + 12:eocd + 20])
    if cd_offset == 0xFFFFFFFF:          # zip64: read the zip64 end record through its locator
        loc = tail.rfind(b"PK\x06\x07")
        z64 = struct.unpack("<Q", tail[loc + 8:loc + 16])[0]
        rec = _get_range(ZENODO_URL, z64, z64 + 55)
        cd_size, cd_offset = struct.unpack("<QQ", rec[40:56])
    directory = _get_range(ZENODO_URL, cd_offset, cd_offset + cd_size - 1)
    members = []
    pos = 0
    while pos < len(directory) and directory[pos:pos + 4] == b"PK\x01\x02":
        (method, csize, usize, nlen, xlen, clen, offset) = (
            struct.unpack("<H", directory[pos + 10:pos + 12])[0],
            *struct.unpack("<II", directory[pos + 20:pos + 28]),
            *struct.unpack("<HHH", directory[pos + 28:pos + 34]),
            struct.unpack("<I", directory[pos + 42:pos + 46])[0])
        name = directory[pos + 46:pos + 46 + nlen].decode()
        extra = directory[pos + 46 + nlen:pos + 46 + nlen + xlen]
        if 0xFFFFFFFF in (csize, usize, offset):   # zip64 sizes and offset in the extra field
            i = 0
            while i < len(extra):
                tag, ln = struct.unpack("<HH", extra[i:i + 4])
                if tag == 1:
                    vals = list(struct.unpack("<" + "Q" * (ln // 8), extra[i + 4:i + 4 + ln]))
                    if usize == 0xFFFFFFFF:
                        usize = vals.pop(0)
                    if csize == 0xFFFFFFFF:
                        csize = vals.pop(0)
                    if offset == 0xFFFFFFFF:
                        offset = vals.pop(0)
                i += 4 + ln
        if name.startswith(f"published/{folder}/ratTrial_") and name.endswith(".mat"):
            members.append((name, method, csize, offset))
        pos += 46 + nlen + xlen + clen
    first = min(m[3] for m in members)
    last = max(m[3] + m[2] for m in members) + 1024
    blob = _get_range(ZENODO_URL, first, min(last, size - 1))
    out = {}
    for name, method, csize, offset in sorted(members):
        h = offset - first
        nlen, xlen = struct.unpack("<HH", blob[h + 26:h + 30])
        data = blob[h + 30 + nlen + xlen:h + 30 + nlen + xlen + csize]
        raw = zlib.decompress(data, -15) if method == 8 else data
        A = sio.loadmat(io.BytesIO(raw), simplify_cells=True)["A"]
        out[name.split("ratTrial_")[1][:-4]] = {k: np.asarray(A[k]) for k in STRUCT_FIELDS if k in A}
    return out


# ----------------------------------------------------------------------------------------
# Figure 4: training (A_Structs_all from Zenodo)
# ----------------------------------------------------------------------------------------

def _ordinal(volume: np.ndarray) -> np.ndarray:
    """convertreward.m: offered volume to its rank 1 to 5."""
    rank = {4: 1, 5: 1, 8: 2, 10: 2, 16: 3, 20: 3, 32: 4, 40: 4, 64: 5, 80: 5}
    return np.array([rank.get(int(v), np.nan) if np.isfinite(v) else np.nan for v in volume], float)


def regress_trials_blocks(Z: dict, idx: np.ndarray) -> dict:
    """regress_trials_blocksv2.m (tback = 1) on the non-violation trials among idx of a struct
    (with wait times above the threshold and initiation times above the 99th percentile
    already removed): wait time ratio 20 uL high/low, initiation time ratio high/low, the wait
    time coefficients of reward and block (blocks coded low 1, mixed 2, high 3; no constant)
    and the initiation time coefficient of the previous reward (no constant)."""
    keep = idx[~Z["vios"][idx].astype(bool)]
    block = Z["block"][keep].astype(float)
    block = np.select([block == 3, block == 2, block == 1], [1.0, 3.0, 2.0], default=np.nan)
    wt = Z["wait_time"][keep].astype(float).copy()
    wt[Z["optout"][keep] == 0] = np.nan
    rew = _ordinal(Z["reward"][keep])
    iti = Z["ITI"][keep].astype(float)
    prev = np.r_[0, rew[:-1]]
    Y, Y2 = zscore(wt), zscore(iti)
    out = {}
    ok = ~np.isnan(Y) & ~np.isnan(rew) & ~np.isnan(block)
    out["b_reward"], out["b_block"] = (np.linalg.lstsq(np.c_[rew, block][ok], Y[ok], rcond=None)[0]
                                       if ok.sum() > 2 else (np.nan, np.nan))
    ok2 = ~np.isnan(Y2) & ~np.isnan(prev)
    out["b_iti_prev"] = np.linalg.lstsq(prev[ok2, None], Y2[ok2], rcond=None)[0][0] if ok2.sum() > 2 else np.nan
    with np.errstate(invalid="ignore", divide="ignore"):
        out["wt_ratio"] = np.nanmean(wt[(block == 3) & (rew == 3)]) / np.nanmean(wt[(block == 1) & (rew == 3)])
        out["iti_ratio"] = np.nanmean(iti[block == 3]) / np.nanmean(iti[block == 1])
    return out


def training_pairs(Z: dict, nsess: int = 50, grp: int = 2, final_stage_only: bool = False) -> tuple[pd.DataFrame, pd.DataFrame]:
    """macro_regress_overtraining_V2.m: the measures of regress_trials_blocks for the first and
    the last nsess sessions in groups of grp, one row per group (NaN where the rat has too few
    sessions). The code takes every session of the struct; with final_stage_only, only the
    sessions whose first trial is in the final stage (as Figure4.m selects for Figure 4d)."""
    Z = dict(Z)
    if final_stage_only:
        keep = final_stage_sessions(Z)
        nt = np.atleast_1d(Z["ntrials"]).astype(int)
        starts = np.r_[0, np.cumsum(nt)]
        idx = np.concatenate([np.arange(starts[s], starts[s + 1]) for s in keep]) if len(keep) else np.array([], int)
        Z = {k: (v[idx] if np.ndim(v) and len(v) == starts[-1] else v) for k, v in Z.items()}
        Z["ntrials"] = nt[keep]
    Z["wait_time"] = Z["wait_time"].astype(float).copy()
    Z["wait_time"][Z["wait_time"] > float(Z["wait_thresh"])] = np.nan
    Z["ITI"] = Z["ITI"].astype(float).copy()
    Z["ITI"][Z["ITI"] > np.nanpercentile(Z["ITI"], 99)] = np.nan
    nt = np.atleast_1d(Z["ntrials"]).astype(int)
    starts = np.r_[0, np.cumsum(nt)]
    n = len(nt)
    first, last = [], []
    for k in range(0, nsess, grp):
        for rows, sess in ((first, np.arange(k, k + grp)), (last, np.arange(n - nsess + k, n - nsess + k + grp))):
            if sess.max() >= n or sess.min() < 0:
                rows.append({})
            else:
                idx = np.arange(starts[sess.min()], starts[sess.max() + 1])
                rows.append(regress_trials_blocks(Z, idx))
    cols = ["wt_ratio", "iti_ratio", "b_reward", "b_block", "b_iti_prev"]
    return pd.DataFrame(first, columns=cols), pd.DataFrame(last, columns=cols)


def final_stage_sessions(Z: dict) -> np.ndarray:
    """Figure4.m: the sessions of a struct whose first trial is in the final stage (coded 9)."""
    nt = np.atleast_1d(Z["ntrials"]).astype(int)
    starts = np.r_[0, np.cumsum(nt)[:-1]]
    return np.flatnonzero(Z["trainingstage"][starts] == 9)


def struct_arrays(Z: dict, sessions: np.ndarray) -> dict:
    """The trials of the given sessions of a Zenodo struct as the per-rat arrays that
    initiation_dynamics and wait_dynamics use (sessions renumbered from 0)."""
    nt = np.atleast_1d(Z["ntrials"]).astype(int)
    starts = np.r_[0, np.cumsum(nt)]
    idx = np.concatenate([np.arange(starts[s], starts[s + 1]) for s in sessions])
    return {
        "session": np.repeat(np.arange(len(sessions)), nt[sessions]),
        "trial": np.concatenate([np.arange(nt[s]) for s in sessions]),
        "block": Z["block"][idx].astype(int),
        "iti": Z["ITI"][idx].astype(float),
    }


def overshoot(curve: np.ndarray, twin: int = 20) -> float:
    """Figure4.m: the maximum of a high-to-mixed initiation time curve from the switch on, minus
    its value twin trials after the switch."""
    return np.nanmax(curve[twin:]) - curve[-1]


def remove_outliers(x: np.ndarray, window: int = 5) -> np.ndarray:
    """MATLAB's isoutlier(x, 'movmedian', 5) set to NaN: points more than three scaled median
    absolute deviations from the median of their moving window."""
    x = np.asarray(x, float).copy()
    half = window // 2
    out = x.copy()
    for i in range(len(x)):
        w_ = x[max(0, i - half):i + half + 1]
        w_ = w_[~np.isnan(w_)]
        if len(w_) == 0 or np.isnan(x[i]):
            continue
        med = np.median(w_)
        mad = 1.4826 * np.median(np.abs(w_ - med))
        if abs(x[i] - med) > 3 * mad:
            out[i] = np.nan
    return out
