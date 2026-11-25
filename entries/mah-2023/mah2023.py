"""Loading and shared measures for the reproduction of Mah et al. (2023) on DANDI:001169.

Every NWB file of the pinned version is fetched over HTTPS into memory (no file is written to
disk) and read with h5py. The files are about 1 MB each, so one request per file is much faster
than range requests; the 23,033 files are read in parallel threads. Only the processed trials
table, the subject, the session start time and the task argument `center_port_cue` are kept.

Where each parameter comes from:
- Volumes: female volumes 4, 8, 16, 32, 64 uL are treated as 5, 10, 20, 40, 80 uL (claims file
  header; Methods, "Training for male and female rats").
- Wait times: the dandiset's `wait_time` column, which already removes wait times above the
  rat's pooled catch-trial mean + 1 SD (`wait_time_threshold`; Methods, "Statistical analyses",
  paragraph 1). Only opt-out catch trials have a wait time (claims file header).
- Trial initiation time: the dandiset's `inter_trial_interval` ("the time between the end of the
  consummatory period and the time to initiate the next trial"), which is the paper's definition
  (Results, paragraph 1: "the time from opting out or consuming reward to initiating a new
  trial"). Values above the rat's pooled 99th percentile are removed (Methods, "Criteria for
  including behavioral data"; claims file header).
- z-scoring is within rat over the trials each analysis names (claims file header).
"""
import io
import json
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd

DANDISET = "001169"
VERSION = "0.261120.1450"
API = "https://api.dandiarchive.org/api"

VOL_MAP = {4: 5, 8: 10, 16: 20, 32: 40, 64: 80, 5: 5, 10: 10, 20: 20, 40: 40, 80: 80}
BLOCK_CODE = {b"Mixed": 1, b"High": 2, b"Low": 3}  # the code's coding: 1 mixed, 2 high, 3 low

COLS = ["start_time", "training_stage", "is_catch", "catch_percentage", "reward_volume_ul",
        "reward_delay", "block_type", "is_rewarded", "is_violation", "is_opt_out", "wait_time",
        "wait_time_unthresholded", "wait_time_threshold", "wait_for_center_poke",
        "inter_trial_interval"]


def _get(url, tries=5):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return r.read()
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))


def list_assets():
    """All assets of the pinned version, from the DANDI REST API."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = json.loads(_get(url))
        out += r["results"]
        url = r["next"]
    return out


def version_info():
    return json.loads(_get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/info/"))


def _read_session(asset):
    b = _get(f"{API}/assets/{asset['asset_id']}/download/")
    with h5py.File(io.BytesIO(b), "r") as f:
        g = f["intervals/processed_trials"]
        d = {k: g[k][:] for k in COLS}
        n_raw = f["intervals/trials/id"].shape[0]
        tis = f["intervals/trials/trials_in_stage"]
        tis_first, tis_last = int(tis[0]), int(tis[-1])
        ta = f["general/task/task_arguments"]
        args = {n.decode(): e.decode() for n, e in zip(ta["argument_name"][:], ta["expression"][:])}
        meta = dict(
            path=asset["path"],
            subject=f["general/subject/subject_id"][()].decode(),
            sex=f["general/subject/sex"][()].decode(),
            start=f["session_start_time"][()].decode(),
            protocol=f["general/protocol"][()].decode(),
            center_port_cue=args.get("center_port_cue", "absent"),
            n_trials=len(d["start_time"]),
            n_raw_trials=n_raw,
            trials_in_stage_first=tis_first,
            trials_in_stage_last=tis_last,
        )
    return meta, d


def load_all(assets, workers=24):
    """Read every session. Returns (sessions, trials) DataFrames; trials hold a `sess` index."""
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(_read_session, assets))
    sessions = pd.DataFrame([m for m, _ in res])
    sessions["start"] = pd.to_datetime(sessions["start"], utc=True)
    # order sessions within each rat by start time
    order = sessions.sort_values(["subject", "start"]).index.to_numpy()
    sessions = sessions.loc[order].reset_index(drop=True)
    parts = []
    for new_i, old_i in enumerate(order):
        d = res[old_i][1]
        df = pd.DataFrame({k: d[k] for k in COLS if k != "block_type"})
        df["block"] = np.array([BLOCK_CODE.get(x, 0) for x in d["block_type"]], dtype=np.int8)
        df["sess"] = new_i
        df["trial"] = np.arange(len(df), dtype=np.int32)
        parts.append(df)
    trials = pd.concat(parts, ignore_index=True)
    trials["subject"] = sessions["subject"].to_numpy()[trials["sess"].to_numpy()]
    trials["vol"] = trials["reward_volume_ul"].map(VOL_MAP).astype("Int64")
    sessions["sess_in_rat"] = sessions.groupby("subject").cumcount()
    return sessions, trials


def add_measures(trials):
    """Per-rat measures shared by the claims (see the module docstring for their sources).

    wt: wait time on opt-out catch trials (thresholded, as deposited); NaN elsewhere.
    iti: trial initiation time with values above the rat's pooled 99th percentile removed.
    z_wt: wt z-scored within rat over all its catch trials with a wait time.
    z_iti: iti z-scored within rat over all its trials.
    """
    t = trials
    catch_oo = t["is_catch"].to_numpy() & t["is_opt_out"].to_numpy()
    t["wt"] = np.where(catch_oo, t["wait_time"].to_numpy(), np.nan)
    t["wt_raw"] = np.where(catch_oo, t["wait_time_unthresholded"].to_numpy(), np.nan)
    # the first trial of a session has no previous trial to initiate from; block_dynamics_latency.m
    # sets it to NaN
    raw = t["inter_trial_interval"].where(t["trial"] > 0)
    p99 = raw.groupby(t["subject"]).transform(lambda x: np.nanpercentile(x, 99))
    t["iti"] = raw.where(raw <= p99)
    for c in ["wt", "iti"]:
        g = t.groupby("subject")[c]
        t["z_" + c] = (t[c] - g.transform("mean")) / g.transform("std")
    # previous trial within the session
    sess = t["sess"].to_numpy()
    same = np.r_[False, sess[1:] == sess[:-1]]
    for c in ["vol", "is_rewarded", "block"]:
        prev = t[c].shift(1)
        t["prev_" + c] = prev.where(same)
    return t


def wilcoxon_p(x, y=None, alternative="two-sided"):
    from scipy.stats import wilcoxon
    return wilcoxon(x, y, alternative=alternative).pvalue


# ---------------------------------------------------------------------------------------------
# Shared measures
# ---------------------------------------------------------------------------------------------

def per_rat_mean(t, value, mask, by=None):
    """Mean of `value` over trials in `mask`, per rat (and per `by` when given)."""
    keys = ["subject"] + ([by] if by else [])
    return t.loc[mask].groupby(keys)[value].mean()


def ranksum_p(x, y, alternative="two-sided"):
    from scipy.stats import mannwhitneyu
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    x, y = x[~np.isnan(x)], y[~np.isnan(y)]
    if len(x) == 0 or len(y) == 0:
        return np.nan
    return mannwhitneyu(x, y, alternative=alternative, method="asymptotic").pvalue


def zscore_within(t, value, mask, keys=("subject",)):
    """z-score `value` within groups `keys`, over the trials in `mask`; NaN outside the mask."""
    v = t[value].where(mask)
    g = v.groupby([t[k] for k in keys])
    return (v - g.transform("mean")) / g.transform("std")


def detrend_iti(t, z, per_session=True):
    """Remove the trend of z-scored initiation time against trial number.

    per_session=True: each session's z-scored ITI regressed on z-scored trial number, fit
    subtracted (Methods, Block transition dynamics). per_session=False: one line per rat on raw
    trial number over pooled sessions (block_dynamics_latency.m), fit subtracted.
    """
    out = np.full(len(t), np.nan)
    zz = z.to_numpy()
    tr = t["trial"].to_numpy().astype(float)
    key = t["sess"].to_numpy() if per_session else t["subject"].astype("category").cat.codes.to_numpy()
    order = np.argsort(key, kind="stable")
    bounds = np.flatnonzero(np.diff(key[order])) + 1
    for idx in np.split(order, bounds):
        y = zz[idx]
        x = tr[idx]
        if per_session:
            x = (x - x.mean()) / (x.std() if x.std() > 0 else 1)
        ok = ~np.isnan(y)
        if ok.sum() < 3:
            continue
        b = np.polyfit(x[ok], y[ok], 1)
        out[idx] = y - np.polyval(b, x)
    return pd.Series(out, index=t.index)


def transitions(t):
    """Block transitions within sessions: global row index of the first trial of the new block,
    with the previous and next block codes (1 mixed, 2 high, 3 low)."""
    b = t["block"].to_numpy()
    s = t["sess"].to_numpy()
    i = np.flatnonzero((b[1:] != b[:-1]) & (s[1:] == s[:-1])) + 1
    return pd.DataFrame({"idx": i, "prev": b[i - 1], "next": b[i], "subject": t["subject"].to_numpy()[i]})


def transition_curves(t, values, trans, twin=20, smooth=10, rats=None):
    """Per-rat mean curve of `values` at offsets -twin..twin around each transition type, within
    the session; each rat's curve smoothed with a `smooth`-point moving average (Methods, Block
    transition dynamics). Returns {(prev, next): DataFrame rats x offsets}."""
    v = np.asarray(values, float)
    s = t["sess"].to_numpy()
    offs = np.arange(-twin, twin + 1)
    out = {}
    for (p, n), g in trans.groupby(["prev", "next"]):
        idx = g["idx"].to_numpy()[:, None] + offs[None, :]
        ok = (idx >= 0) & (idx < len(v))
        idx2 = np.where(ok, idx, 0)
        ok &= s[idx2] == s[g["idx"].to_numpy()][:, None]
        m = np.where(ok, v[idx2], np.nan)
        df = pd.DataFrame(m, columns=offs)
        df["subject"] = g["subject"].to_numpy()
        with np.errstate(all="ignore"):
            cur = df.groupby("subject").mean()
        if smooth:
            cur = cur.T.rolling(smooth, center=True, min_periods=1).mean().T
        if rats is not None:
            cur = cur.reindex(rats)
        out[(p, n)] = cur
    return out


def fit_exp_decay(x, Y, lb, ub, ngrid=4000):
    """Least-squares fit of y = D exp(-x / tau) with bounds lb=(D_lo, tau_lo), ub=(D_hi, tau_hi),
    for each row of Y. fit_exp_decay.m uses fmincon from 10 random starts; here the search is a
    dense grid over tau with the bounded optimal D in closed form for each tau, which finds the
    least-squares optimum without random starts (a standard choice that cannot change a result
    beyond fit noise). Returns arrays (D, tau)."""
    x = np.asarray(x, float)
    Y = np.atleast_2d(np.asarray(Y, float))
    lo = max(lb[1], 0.01)  # below 0.01 trials the curve is 0 at every lag
    taus = np.unique(np.r_[np.linspace(lo, ub[1], ngrid), np.geomspace(lo, ub[1], ngrid)])
    E = np.exp(-x[None, :] / taus[:, None])  # (G, n)
    YE = Y @ E.T  # (R, G)
    EE = (E * E).sum(1)
    D = np.clip(YE / EE, lb[0], ub[0])
    sse = (Y * Y).sum(1)[:, None] - 2 * D * YE + D * D * EE
    sse = np.where(np.isfinite(sse), sse, np.inf)
    k = np.argmin(sse, axis=1)
    r = np.arange(len(Y))
    return D[r, k], taus[k]


def ols_ci(X, y):
    """OLS with 95% intervals, rows with any NaN dropped (Matlab regress)."""
    from scipy.stats import t as tdist
    ok = ~np.isnan(X).any(1) & ~np.isnan(y)
    X, y = X[ok], y[ok]
    n, k = X.shape
    if n <= k + 1:
        return np.full(k, np.nan), np.full((k, 2), np.nan), n
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ b
    s2 = r @ r / (n - k)
    cov = s2 * np.linalg.pinv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    q = tdist.ppf(0.975, n - k)
    return b, np.c_[b - q * se, b + q * se], n


def lagged(x, sess, nback, valid=None):
    """Columns x[t-1] .. x[t-nback] within the session (NaN across sessions or where not valid)."""
    n = len(x)
    out = np.full((n, nback), np.nan)
    for j in range(1, nback + 1):
        col = np.full(n, np.nan)
        col[j:] = x[:-j]
        same = np.zeros(n, bool)
        same[j:] = sess[j:] == sess[:-j]
        col[~same] = np.nan
        out[:, j - 1] = col
    return out


# ---------------------------------------------------------------------------------------------
# Inferential model (Methods, Equations 3 to 6; GenerateSynthData_Bayes.m)
# ---------------------------------------------------------------------------------------------

P_REW = np.array([[1 / 5] * 5, [0, 0, 1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3, 0, 0]])  # mixed, high, low


def transition_matrix(h0=1 / 40):
    """P(B_t | B_t-1), columns the previous block (mixed, high, low), as GenerateSynthData_Bayes.m:
    from mixed, H0/2 to each of high and low; from high or low, H0 to mixed."""
    return np.array([[1 - h0, h0, h0], [h0 / 2, 1 - h0, 0], [h0 / 2, 0, 1 - h0]])


def infer_blocks(vol_idx, new_sess, h0=1 / 40, lam=1.0):
    """Prior and posterior over (mixed, high, low) per trial. vol_idx: offer index 0..4 per trial
    (the model's trials, non-violation trials in GenerateSynthData_Bayes.m); new_sess: True at the
    first such trial of each session, where the belief is reset to (1/2, 1/4, 1/4) and no prior is
    defined. lam < 1 gives the sub-optimal prior of Equation 8."""
    pb = transition_matrix(h0)
    n = len(vol_idx)
    post = np.full((n, 3), np.nan)
    prior = np.full((n, 3), np.nan)
    b = None
    for i in range(n):
        if new_sess[i]:
            b = np.array([0.5, 0.25, 0.25])
        else:
            pr = pb @ b
            if lam != 1.0:
                pr = lam * pr + (1 - lam) / 3
            prior[i] = pr
            b = P_REW[:, vol_idx[i]] * pr
            b = b / b.sum()
        post[i] = b
    return prior, post


# ---------------------------------------------------------------------------------------------
# The paper's Zenodo deposit (doi:10.5281/zenodo.10031483, published.zip): A_Structs_all holds
# every session that ended in the final stage, the data of Figure 4 (its README.txt).
# ---------------------------------------------------------------------------------------------

ZENODO_URL = "https://zenodo.org/api/records/10031483/files/published.zip/content"


def zenodo_zip():
    """The deposit's zip, opened over HTTP range requests (its directory is read once)."""
    import fsspec
    import zipfile
    return zipfile.ZipFile(fsspec.open(ZENODO_URL, block_size=2 ** 20).open())


def zenodo_rat_list(z):
    import scipy.io as sio
    m = sio.loadmat(io.BytesIO(z.read("published/ratList.mat")), squeeze_me=True)
    return [str(x) for x in m["ratList"]], [str(x) for x in m["sexList"]]


def _range(url, start, end, tries=6):
    req = urllib.request.Request(url, headers={"Range": f"bytes={start}-{end}"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read()
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(15 * (i + 1))  # Zenodo answers 429 when asked too often


def _parse_astruct(rat, raw):
    import scipy.io as sio
    A = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)["A"]
    nt = np.atleast_1d(A.ntrials).astype(int)
    d = {k: np.atleast_1d(getattr(A, k)).astype(float) for k in
         ["trainingstage", "catch", "prob_catch", "reward", "block", "hits", "vios", "optout",
          "wait_time", "ITI", "wait_time_unthresholded"]}
    df = pd.DataFrame(d)
    df["sess_in_rat"] = np.repeat(np.arange(len(nt)), nt)
    df["subject"] = rat
    df["wait_thresh"] = float(A.wait_thresh)
    return df


def load_zenodo_astructs(z, rats, folder="A_Structs_all", chunk=64 * 2 ** 20):
    """Per-trial table of the deposit's A structs for `rats` (sessions in file order). The
    members are read from the zip by a few large range requests (Zenodo limits the request
    rate) and inflated in memory."""
    import struct
    import zlib as _zl
    infos = {i.filename: i for i in z.infolist()}
    want = [infos[f"published/{folder}/ratTrial_{r}.mat"] for r in rats]
    lo = min(i.header_offset for i in want)
    hi = max(i.header_offset + 30 + len(i.filename) + 1024 + i.compress_size for i in want)
    buf = bytearray()
    for s in range(lo, hi, chunk):
        buf += _range(ZENODO_URL, s, min(s + chunk, hi) - 1)
    parts = []
    for r, i in zip(rats, want):
        o = i.header_offset - lo
        n, m = struct.unpack("<HH", buf[o + 26:o + 30])
        start = o + 30 + n + m
        data = bytes(buf[start:start + i.compress_size])
        raw = _zl.decompressobj(-15).decompress(data) if i.compress_type == 8 else data
        parts.append(_parse_astruct(r, raw))
    return pd.concat(parts, ignore_index=True)


# ---------------------------------------------------------------------------------------------
# Wait time models (Methods, Behavioral models; the generative code in BehavioralModel/ of the
# paper's repository at b7b68ca8c107: GenerateSynthData_Bayes.m, _Bayes_BeliefState.m,
# _AlphaPHModel.m, _Bayes_subopt_onlylambda_flat.m; GenerateLatencyData_*.m). The fitting code
# is not public; what it would fix (bounds, starts, folds) is stated where it is chosen.
# ---------------------------------------------------------------------------------------------

from numba import njit

TAU_DELAY = 2.5  # tau of the exponential delay distribution (Methods, Equation 1)
NOISE_WT = 8.0  # variance of the log-normal noise of the wait time model (Methods)


@njit
def belief_filter(vidx, newsess, lam, reset):
    """Posterior and prior over (mixed, high, low) with H0 = 1/40, as in the generative code:
    at the first model trial of each session the belief is set to `reset` (prior NaN); otherwise
    prior = lam * P(B_t | B_t-1) belief + (1 - lam) / 3, posterior = likelihood * prior."""
    h0 = 1.0 / 40
    pb = np.array([[1 - h0, h0, h0], [h0 / 2, 1 - h0, 0.0], [h0 / 2, 0.0, 1 - h0]])
    prew = np.array([[0.2, 0.2, 0.2, 0.2, 0.2], [0.0, 0.0, 1 / 3, 1 / 3, 1 / 3],
                     [1 / 3, 1 / 3, 1 / 3, 0.0, 0.0]])
    n = len(vidx)
    post = np.empty((n, 3))
    prior = np.full((n, 3), np.nan)
    b = reset.copy()
    for i in range(n):
        if newsess[i]:
            b = reset.copy()
        else:
            pr = pb @ b
            pr = lam * pr + (1 - lam) / 3.0
            for k in range(3):
                prior[i, k] = pr[k]
            b = prew[:, vidx[i]] * pr
            b = b / b.sum()
        for k in range(3):
            post[i, k] = b[k]
    return post, prior


@njit
def retro_kappa(r, newsess, gain, alpha0, mode, k0):
    """kappa_{t+1} = kappa_t + alpha_t (r_t - kappa_t) (Equation 9), reset to k0 at each session.
    mode 0: alpha_t = min(alpha0 * gain_t, 1) (Equation 10; alpha0 at the session's first trial);
    mode 1: alpha_t = alpha0 (G = 1); mode 2: alpha_t = min(alpha0 |delta_t|, 1) (G = |delta|)."""
    n = len(r)
    kap = np.empty(n)
    k = k0
    for i in range(n):
        if newsess[i]:
            k = k0
        kap[i] = k
        d = r[i] - k
        if mode == 0:
            a = alpha0 if newsess[i] else min(alpha0 * gain[i], 1.0)
        elif mode == 1:
            a = alpha0
        else:
            a = min(alpha0 * abs(d), 1.0)
        k = k + a * d
    return kap


def lognormal_nll(wt, m, var=NOISE_WT):
    """-sum log density of wt under a log-normal with mean m and variance var (generate_wts.m)."""
    m = np.maximum(m, 1e-12)
    s2 = np.log(var / m ** 2 + 1)
    mu = np.log(m) - s2 / 2
    lw = np.log(np.maximum(wt, 1e-6))
    return float(np.sum(lw + 0.5 * np.log(2 * np.pi * s2) + (lw - mu) ** 2 / (2 * s2)))


class RatModel:
    """One rat's model trials: the trials with a wait time (hits and opt-outs; isgood in the
    generative code), in session order."""

    def __init__(self, g):
        good = g["wait_time"].notna().to_numpy()
        h = g.loc[good]
        self.vidx = h["vol"].map({5: 0, 10: 1, 20: 2, 40: 3, 80: 4}).to_numpy().astype(np.int64)
        self.rlog = np.log2(h["reward_volume_ul"].to_numpy().astype(float))
        s = h["sess"].to_numpy()
        self.sess = s
        self.newsess = np.r_[True, s[1:] != s[:-1]]
        self.C = float((1 - g["catch_percentage"]).max())
        self.minr = float(np.log2(g["reward_volume_ul"].min()))
        self.fit = (h["is_catch"] & h["is_opt_out"]).to_numpy()
        self.wt = h["wait_time"].to_numpy()
        self.block = h["block"].to_numpy()
        self.vol = h["vol"].to_numpy()
        self.index = h.index.to_numpy()
        self.post, self.prior = belief_filter(self.vidx, self.newsess, 1.0, np.array([0.5, 0.25, 0.25]))
        self.blk_inf = np.argmax(self.post, 1)  # 0 mixed, 1 high, 2 low
        dm = np.abs(np.diff(self.post[:, 0], prepend=np.nan))
        self.gain = np.where(self.newsess, 1.0, 1.0 / (1 - np.nan_to_num(dm)))

    def wt_opt(self, model, p, only_fit=True):
        """Optimal wait time (Equation 1) on the fitted trials (or all model trials)."""
        C, tau = self.C, TAU_DELAY
        sel = self.fit if only_fit else np.ones(len(self.fit), bool)
        R = self.rlog[sel]
        if model in ("inferential", "belief", "lambda"):
            kv = np.array(p[:3]) * C * self.minr / tau  # (mixed, high, low)
            D = 10 * p[3]
            if model == "inferential":
                kap = kv[self.blk_inf[sel]]
            elif model == "belief":
                kap = self.post[sel] @ kv
            else:
                post, _ = belief_filter(self.vidx, self.newsess, p[4], np.array([1 / 3, 1 / 3, 1 / 3]))
                kap = kv[np.argmax(post, 1)[sel]]
        else:  # retrospective (GenerateSynthData_AlphaPHModel.m)
            D = 15 * p[1]
            kap = retro_kappa(self.rlog, self.newsess, self.gain, p[0], 0, np.mean(np.log([5, 10, 20, 40, 80])))
            kap = (kap / kap.max() * (self.minr * C / tau))[sel]
            kap = np.where(kap < 0, 1e-16, kap)
        with np.errstate(all="ignore"):
            arg = (R - kap * tau) / (kap * tau) * C / (1 - C)
            w = D * tau * np.log(arg)
        return np.where(np.isfinite(w) & (w > 0), w, 1e-12)

    def nll(self, model, p, mask):
        """mask: over the fitted trials"""
        w = self.wt_opt(model, p)
        return lognormal_nll(self.wt[self.fit][mask], w[mask])


MODELS = {  # free parameters and their bounds (bounds are this attempt's choice; see the notebook)
    "inferential": ["k_mixed", "k_high", "k_low", "D"],
    "belief": ["k_mixed", "k_high", "k_low", "D"],
    "retrospective": ["alpha0", "D"],
    "lambda": ["k_mixed", "k_high", "k_low", "D", "lambda"],
}


def bounds_for(model, C):
    kb = (0.01, min(0.999 / C, 5.0))
    return {"inferential": [kb, kb, kb, (0.01, 10)], "belief": [kb, kb, kb, (0.01, 10)],
            "retrospective": [(0.001, 1.0), (0.01, 10)],
            "lambda": [kb, kb, kb, (0.01, 10), (0.0, 1.0)]}[model]


def fit_model(rm, model, mask, rng, nstarts):
    from scipy.optimize import minimize
    bnds = bounds_for(model, rm.C)
    best = None
    for _ in range(nstarts):
        p0 = np.array([rng.uniform(lo, hi) for lo, hi in bnds])
        r = minimize(lambda p: rm.nll(model, p, mask), p0, method="L-BFGS-B", bounds=bnds)
        if best is None or r.fun < best.fun:
            best = r
    return best.x, best.fun


def cv_fit(rm, model, rng, nstarts=3, nfold=5):
    """5-fold cross-validation over sessions (folds drawn at random from rng). For each fold the
    model is fitted on the other four and evaluated on it; the parameters of the fold with the
    lowest test nLL are kept (Zenodo README, BestFit final_params) and evaluated on all data.
    Returns dict with params, nll_all, cv_nll (summed test nLL over folds), best_fold_test_nll,
    k and n (trials fitted)."""
    us = np.unique(rm.sess)
    fold_of = dict(zip(us, rng.permutation(len(us)) % nfold))
    f = np.array([fold_of[s] for s in rm.sess[rm.fit]])
    tests, params = [], []
    for k in range(nfold):
        p, _ = fit_model(rm, model, f != k, rng, nstarts)
        params.append(p)
        tests.append(rm.nll(model, p, f == k))
    kbest = int(np.argmin(tests))
    p = params[kbest]
    all_ = rm.nll(model, p, np.ones(len(f), bool))
    return dict(params=p, nll_all=all_, cv_nll=float(np.sum(tests)), best_fold_test_nll=tests[kbest],
                k=len(p), n=int(rm.fit.sum()))


_T = None  # trials table shared with forked workers


def _fit_rat(args):
    rat, models, seed, nstarts, cv = args
    rm = RatModel(_T[rat])
    out = {}
    for j, m in enumerate(models):
        rng = np.random.default_rng(seed + j)
        if cv:
            out[m] = cv_fit(rm, m, rng, nstarts=nstarts)
        else:
            p, f = fit_model(rm, m, np.ones(int(rm.fit.sum()), bool), rng, nstarts)
            out[m] = dict(params=p, nll_all=f, k=len(p), n=int(rm.fit.sum()))
    return rat, out


def fit_all(trials, rats, models, seed, nstarts=3, procs=4, cv=True):
    """Fit `models` to every rat in parallel processes (fork). The generator of each rat and model
    is seeded from `seed` (the claim's seed) plus the rat's position times 10 and the model's."""
    import multiprocessing as mp
    global _T
    cols = ["subject", "sess", "wait_time", "vol", "reward_volume_ul", "catch_percentage",
            "is_catch", "is_opt_out", "block"]
    _T = {r: g for r, g in trials[cols].groupby("subject") if r in set(rats)}
    # compile the numba functions once, before the workers are forked
    belief_filter(np.zeros(2, np.int64), np.array([True, False]), 1.0, np.array([0.5, 0.25, 0.25]))
    retro_kappa(np.zeros(2), np.array([True, False]), np.ones(2), 0.1, 0, 1.0)
    args = [(r, models, seed + 10 * i, nstarts, cv) for i, r in enumerate(rats)]
    with mp.get_context("fork").Pool(procs) as pool:
        res = dict(pool.map(_fit_rat, args, chunksize=4))
    return res


def simulate_iti(g, model, alpha0, dscale, noise_var, rng, nsims=50, gain=None):
    """Simulated trial initiation times on a rat's offers (GenerateLatencyData_*.m).
    model 'eq10' (AlphaPHModel: trials with a wait time, kappa0 = mean(ln[5..80]), D = 25 p,
    alpha from Equation 10), 'static' (VanillaAlpha: trials with an initiation time, kappa0 = 20,
    D = 10 p, G = 1) or 'rpe' (RPEAlpha: trials with an initiation time, kappa0 = 0.5, D = 15 p,
    G = |delta|). TI = D / kappa (Equation 2), kappa < 0 set to eps. Noise: log-normal with mean
    TI and variance `noise_var`; the mean of `nsims` simulations is drawn from its normal
    approximation (mean TI, variance noise_var / nsims), a standard shortcut that only changes
    the noise. Returns a Series over g.index (NaN off the model's trials)."""
    if model == "eq10":
        good = g["wait_time"].notna().to_numpy()
        k0, D, mode = float(np.mean(np.log([5, 10, 20, 40, 80]))), 25 * dscale, 0
    elif model == "static":
        good = g["inter_trial_interval"].notna().to_numpy()
        k0, D, mode = 20.0, 10 * dscale, 1
    else:
        good = g["inter_trial_interval"].notna().to_numpy()
        k0, D, mode = 0.5, 15 * dscale, 2
    h = g.loc[good]
    r = np.log2(h["reward_volume_ul"].to_numpy().astype(float))
    s = h["sess"].to_numpy()
    new = np.r_[True, s[1:] != s[:-1]]
    if mode == 0:
        vidx = h["vol"].map({5: 0, 10: 1, 20: 2, 40: 3, 80: 4}).to_numpy().astype(np.int64)
        post, _ = belief_filter(vidx, new, 1.0, np.array([0.5, 0.25, 0.25]))
        dm = np.abs(np.diff(post[:, 0], prepend=np.nan))
        gain = np.where(new, 1.0, 1.0 / (1 - np.nan_to_num(dm)))
    else:
        gain = np.ones(len(r))
    kap = retro_kappa(r, new, gain, alpha0, mode, k0)
    kap = np.where(kap < 0, 1e-16, kap)
    ti = D / kap
    sim = ti + rng.normal(0, np.sqrt(noise_var / nsims), len(ti)) if nsims > 1 else \
        np.exp(rng.normal(np.log(ti) - np.log(noise_var / ti ** 2 + 1) / 2, np.sqrt(np.log(noise_var / ti ** 2 + 1))))
    out = pd.Series(np.nan, index=g.index)
    out.loc[h.index] = sim
    return out


def logistic4(x, A, D, C, x0):
    return A + (D - A) / (1 + np.exp(-C * (x - x0)))


def fit_logistic(x, Y, ngrid_c=161, ngrid_x0=81):
    """4-parameter logistic of Equation 11 (A lower asymptote, D upper, C inverse temperature, x0
    midpoint) fitted by least squares to each row of Y: a grid over C in [-8, 8] and x0 in
    [-20, 20], with A and D solved exactly for each grid point (the model is linear in them).
    my_fit_sigmoid.m uses fmincon from 10 random starts; the grid is a deterministic search for
    the same optimum (a standard choice). Returns an array (rows, 4) of (A, D, C, x0)."""
    x = np.asarray(x, float)
    Y = np.atleast_2d(np.asarray(Y, float))
    Cs = np.linspace(-8, 8, ngrid_c)
    Cs = Cs[Cs != 0]
    X0 = np.linspace(-20, 20, ngrid_x0)
    cc, xx = np.meshgrid(Cs, X0, indexing="ij")
    cc, xx = cc.ravel(), xx.ravel()
    with np.errstate(over="ignore"):
        S = 1 / (1 + np.exp(-cc[:, None] * (x[None, :] - xx[:, None])))  # (G, n)
    U = 1 - S
    suu, sus, sss = (U * U).sum(1), (U * S).sum(1), (S * S).sum(1)
    det = suu * sss - sus ** 2
    yu, ys = Y @ U.T, Y @ S.T  # (R, G)
    with np.errstate(all="ignore"):
        A = (yu * sss - ys * sus) / det
        D = (ys * suu - yu * sus) / det
        sse = (Y * Y).sum(1)[:, None] - 2 * (A * yu + D * ys) + A * A * suu + 2 * A * D * sus + D * D * sss
    sse = np.where(np.isfinite(sse), sse, np.inf)
    k = np.argmin(sse, 1)
    r = np.arange(len(Y))
    return np.c_[A[r, k], D[r, k], cc[k], xx[k]]
