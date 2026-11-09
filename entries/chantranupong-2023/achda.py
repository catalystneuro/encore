"""Loading and measures for the striatal photometry of dandiset 001767.

Chantranupong, Beron, Zimmer, Wen, Wang & Sabatini (2023), Nature 621, 577-585,
doi:10.1038/s41586-023-06492-9.

Each NWB file holds one session of the two-armed bandit task: up to four demodulated photometry
channels at 54 ms per sample (`raw_photometry_<chan>`, arbitrary units), their rolling z-score
(`detrended_photometry_<chan>`, 60-s window), a stored `baseline_f0_<chan>`, binary port, lick,
LED and laser channels on the same 54-ms samples, and a trials table whose
`photometry_*_index` columns are 1-based sample indices (MATLAB). The channel names follow the
LabJack inputs: greenR = channel 1, redR = 2, greenL = 5, redL = 6. Sensor, virus code, region
and hemisphere of each channel are in the file's `notes` JSON. Files are streamed from the
archive at the pinned version; nothing is written to disk.

Cohort labels (figure, genotype) are not in the files. They come from `manuscript_sessions.csv`
of the dandiset's export code, https://github.com/bernardosabatinilab/Chantranupong-2023-NWB at
commit f9a4ca95370e8d7451f2a29d81e184dd67a735ca, which the dandiset's metadata links
(`relatedResource`, HasMetadata).

Where the parameters come from:

- `WIN` = 17 samples (0.918 s) and the readings W1 and W2 of where the window starts: the claims
  file's header (Supplementary Methods, Quantitative analyses of signals). `CODE_WIN` (0 to 18)
  is the code's window (aa_processStats_final_Fig1_AllDA.m), a variant.
- Per-trial mean of z-scored DA and max minus min of z-scored Ach, the two-sample t-test with
  pooled variance per mouse (T1) and the paired t-test of mouse means (T2): claims file header,
  from processStats_SIMPLE.m.
- LDA: claims file header (70/30 split, classes balanced to the smaller count). `N_LDA_RUNS` = 10
  is nModels in the paper's scripts (aa_processStats_Fig1_DA_Ach_LED.m). MATLAB's fitcdiscr with
  hyperparameter optimisation is replaced by scikit-learn's LDA with Ledoit-Wolf shrinkage, an
  assumption (the optimised hyperparameters are the regularisation amount and delta).
- Cross-correlation: 40 samples before and 100 after centre entry (claims file header,
  Supplementary Methods, Cross-variance analyses), MATLAB xcorr "normalized" (divides by the
  root of the product of the energies, no mean removal). Positive lag = DA leads Ach.
- dF/F0 readings: (a) F0 = session median of the raw trace, (b) F0 = rolling mean over 1111
  samples (60 s, the `signalDetrendWindow` of the files' processing parameters): claims file,
  fig3d-telc-abolishes-ach.
- Behaviour: switch, block position and the RFLR as in the behaviour code
  (AchDA_manuscript_behavior at 20c0edb0d64466e2376f8a1f84ab97f055b13b44, bandit_models.py
  `single_state_model_sessions`). The fit there uses stochastic gradient descent from a module
  the repository does not hold; here the same likelihood is maximised with Nelder-Mead from two starting
  points (a standard choice: any optimiser that reaches the maximum gives the same estimate). Decision time = side entry minus centre entry and ITI =
  start_time minus the previous trial's stop_time, from the trials table; the notebook shows this
  ITI equals centre entry minus the previous side exit taken from the photometry sample indices. The code reads them from the
  box's 'Trial Duration (s)' and 'Since last trial (s)' columns, which the files do not hold (an
  assumption about what those columns measured).
"""

from __future__ import annotations

import io
import json
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import stats
from scipy.optimize import minimize
from scipy.special import expit

DANDISET_ID = "001767"
DANDISET_VERSION = "0.260318.1448"
EXPORT_REPO_COMMIT = "f9a4ca95370e8d7451f2a29d81e184dd67a735ca"
SESSIONS_CSV_URL = ("https://raw.githubusercontent.com/bernardosabatinilab/Chantranupong-2023-NWB/"
                    f"{EXPORT_REPO_COMMIT}/manuscript_sessions.csv")

DT = 0.054                 # s per demodulated sample (files' finalTimeStep)
WIN = 17                   # samples, 0.918 s (Supplementary Methods)
WIN_ITI = 14               # samples, 0.756 s (Supplementary Methods, ITI comparisons)
ITI_SEP = 15               # samples, 0.81 s, isolation of ITI port entries (Supplementary Methods)
XC_PRE, XC_POST = 40, 100  # samples about centre entry (Supplementary Methods)
F0_ROLL = 1111             # samples, 60 s
N_LDA_RUNS = 10
CHANNELS = ["greenL", "greenR", "redL", "redR"]
EVENTS = ["center_port", "left_port", "right_port", "left_lick", "right_lick", "center_LED",
          "side_LED", "laser_or_unused"]

DA_SENSORS = {"dlight1.1", "rDAh"}
ACH_SENSORS = {"Ach3.0"}


# ----------------------------------------------------------------------------- loading

def list_assets():
    """Asset paths and ids at the pinned version, from the DANDI REST API."""
    url = (f"https://api.dandiarchive.org/api/dandisets/{DANDISET_ID}/versions/"
           f"{DANDISET_VERSION}/assets/?page_size=1000")
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += page["results"]
        url = page["next"]
    return out


def dandiset_metadata():
    url = f"https://api.dandiarchive.org/api/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/"
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def manuscript_sessions():
    """The export repository's table of sessions by figure and genotype (one row per use)."""
    with urllib.request.urlopen(SESSIONS_CSV_URL) as r:
        c = pd.read_csv(io.BytesIO(r.read()), dtype=str)
    s = c.Session.str.zfill(8)
    c["date"] = s.str[4:] + s.str[:4]          # MMDDYYYY -> YYYYMMDD
    return c


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def _s3_url(asset_id):
    """The S3 address the archive's download endpoint redirects to."""
    opener = urllib.request.build_opener(_NoRedirect)
    try:
        opener.open(f"https://api.dandiarchive.org/api/assets/{asset_id}/download/")
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307):
            return e.headers["Location"]
        raise
    raise RuntimeError(f"no redirect for asset {asset_id}")


def load_session(asset):
    """Read one file: traces (float32), event onsets, trials and channel metadata."""
    for attempt in range(4):
        try:
            f = h5py.File(remfile.File(_s3_url(asset["asset_id"])), "r")
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2)
    path = asset["path"]
    mouse = path.split("/")[0][4:]
    date = path.split("_ses-")[1].split("_")[0]
    notes = json.loads(f["general/notes"][()].decode())
    meta = notes["channelMetadata"]
    subj = {k: (v.decode() if isinstance(v, bytes) else str(v))
            for k, v in ((k, f[f"general/subject/{k}"][()]) for k in f["general/subject"].keys())}
    s = {"path": path, "mouse": mouse, "date": date, "meta": meta, "subject": subj,
         "params": notes["processingParams"], "z": {}, "raw": {}, "f0": {}}
    s["streams"] = {}
    for ch in CHANNELS:
        if ch not in meta:
            continue
        have = {k: p in f for k, p in [("raw", f"acquisition/raw_photometry_{ch}"),
                                       ("z", f"processing/ophys/detrended_photometry_{ch}"),
                                       ("f0", f"processing/ophys/baseline_f0_{ch}")]}
        s["streams"][ch] = have
        if meta[ch]["sensor"] == "unknown":
            continue
        if have["z"]:
            s["z"][ch] = f[f"processing/ophys/detrended_photometry_{ch}/data"][:].astype(np.float32)
            s["rate"] = float(f[f"processing/ophys/detrended_photometry_{ch}/starting_time"].attrs["rate"])
        if have["raw"]:
            s["raw"][ch] = f[f"acquisition/raw_photometry_{ch}/data"][:].astype(np.float32)
        if have["f0"]:
            s["f0"][ch] = f[f"processing/ophys/baseline_f0_{ch}/data"][:].astype(np.float32)
    s["events"] = {e: np.flatnonzero(f[f"processing/behavior/event_onsets/{e}_event_onsets/data"][:])
                   for e in EVENTS}
    s["exits"] = {}
    for e in ["center_port", "left_port", "right_port", "left_lick", "right_lick", "center_LED", "side_LED"]:
        occ = f[f"processing/behavior/occupancy/{e}_occupancy/data"][:].astype(np.int8)
        s["exits"][e] = np.flatnonzero(np.diff(occ) == -1) + 1   # first sample after the port is left
    s["n_samples"] = f["processing/behavior/event_onsets/center_port_event_onsets/data"].shape[0]
    T = f["intervals/trials"]
    t = pd.DataFrame({c: T[c][:] for c in T.keys() if c != "id"})
    for c in ["chose_left", "chose_right", "was_rewarded", "is_photometry_trial",
              "has_all_photometry_data", "center_laser", "side_laser"]:
        t[c] = t[c].astype(bool)
    for c in [c for c in t.columns if c.startswith("photometry_") and c.endswith("_index")]:
        t[c] = t[c].astype(int) - 1            # to 0-based; -1 = no photometry
    t["trial"] = np.arange(len(t))
    s["trials"] = t
    f.close()
    return s


def load_all(assets, workers=16):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_session, assets))


def channel_of(s, sensors, prefer=None):
    """Channels of a session whose sensor is in `sensors`, preferred channel first."""
    chans = [c for c in CHANNELS if c in s["z"] and s["meta"][c]["sensor"] in sensors]
    if prefer in chans:
        chans.remove(prefer)
        chans.insert(0, prefer)
    return chans


# ----------------------------------------------------------------------------- trials

def add_history(t):
    """Previous-trial columns within a session; stay/switch and the paper's words (Fig. 1g,h)."""
    t = t.copy()
    t["choice"] = np.where(t.chose_left, 1, 0)
    t["prev_choice"] = t.choice.shift(1)
    t["prev_rew"] = t.was_rewarded.shift(1)
    t["switch"] = np.where(t.prev_choice.isna(), np.nan, (t.choice != t.prev_choice).astype(float))
    # words, previous trial first: upper case = rewarded, A = previous port, B = other port
    w = []
    for pr, sw, r in zip(t.prev_rew, t.switch, t.was_rewarded):
        if pd.isna(pr) or pd.isna(sw):
            w.append(None)
            continue
        a = "A" if pr else "a"
        b = ("B" if r else "b") if sw else ("A" if r else "a")
        w.append(a + b)
    t["word"] = w
    return t


def photometry_trials(s):
    t = add_history(s["trials"])
    ok = t.has_all_photometry_data & (t.photometry_side_in_index >= 0)
    return t[ok].copy()


def window_idx(side_idx, which, reading, n=WIN):
    """Sample indices of the pre or post window about side entry for one window reading.

    W1: post = +1..+n, pre = -n..-1; W2: post = 0..+n-1, pre = -(n-1)..0;
    CODE: post = 0..+18, pre = -18..0 (aa_processStats_final_Fig1_AllDA.m), a variant."""
    if reading == "W1":
        off = np.arange(1, n + 1) if which == "post" else np.arange(-n, 0)
    elif reading == "W2":
        off = np.arange(0, n) if which == "post" else np.arange(-(n - 1), 1)
    elif reading == "CODE":
        off = np.arange(0, 19) if which == "post" else np.arange(-18, 1)
    else:
        raise ValueError(reading)
    return np.asarray(side_idx)[:, None] + off[None, :]


def segments(trace, idx):
    """trace[idx] with rows that run off the trace dropped (returns values and a keep mask)."""
    keep = (idx.min(axis=1) >= 0) & (idx.max(axis=1) < len(trace))
    return trace[idx[keep]], keep


def measure(seg, kind):
    if kind == "mean":
        return seg.mean(axis=1)
    if kind == "range":
        return seg.max(axis=1) - seg.min(axis=1)
    if kind == "min":
        return seg.min(axis=1)
    if kind == "max":
        return seg.max(axis=1)
    raise ValueError(kind)


def t1(a, b):
    """Two-sample two-sided t-test with pooled variance (MATLAB ttest2), effect = mean(a)-mean(b)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    if len(a) < 2 or len(b) < 2:
        return np.nan, np.nan
    return float(a.mean() - b.mean()), float(stats.ttest_ind(a, b, equal_var=True).pvalue)


def lda_accuracy(Xa, Xb, rng, runs=N_LDA_RUNS, test_fraction=0.3):
    """Mean test accuracy of LDA separating two sets of trial windows, classes balanced."""
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    accs = []
    n = min(len(Xa), len(Xb))
    if n < 10:
        return np.nan
    for _ in range(runs):
        ia = rng.choice(len(Xa), n, replace=False)
        ib = rng.choice(len(Xb), n, replace=False)
        X = np.vstack([Xa[ia], Xb[ib]])
        y = np.r_[np.zeros(n), np.ones(n)]
        perm = rng.permutation(2 * n)
        ntest = int(round(test_fraction * 2 * n))
        te, tr = perm[:ntest], perm[ntest:]
        clf = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto").fit(X[tr], y[tr])
        accs.append((clf.predict(X[te]) == y[te]).mean())
    return float(np.mean(accs))


# ----------------------------------------------------------------------------- cross-correlation

def xcorr_norm(da, ach, maxlag):
    """MATLAB xcorr(ach, da, maxlag, 'normalized'): r(m) = sum ach[n+m] da[n] / sqrt(Eda Each).

    Positive m: Ach follows DA (DA leads)."""
    da = np.asarray(da, float)
    ach = np.asarray(ach, float)
    n = len(da)
    norm = np.sqrt((da ** 2).sum() * (ach ** 2).sum())
    lags = np.arange(-maxlag, maxlag + 1)
    r = np.empty(len(lags))
    for i, m in enumerate(lags):
        if m >= 0:
            r[i] = (ach[m:] * da[:n - m]).sum()
        else:
            r[i] = (ach[:n + m] * da[-m:]).sum()
    return lags, r / norm


def trial_matrix(trace, centers, pre=XC_PRE, post=XC_POST):
    idx = np.asarray(centers)[:, None] + np.arange(-pre, post + 1)[None, :]
    seg, keep = segments(trace, idx)
    return seg, keep


# ----------------------------------------------------------------------------- dF/F0

def dff(raw, reading):
    raw = np.asarray(raw, float)
    if reading == "median":
        f0 = np.median(raw)
    elif reading == "rolling":
        f0 = pd.Series(raw).rolling(F0_ROLL, center=True, min_periods=1).mean().values
    else:
        raise ValueError(reading)
    return (raw - f0) / f0


# ----------------------------------------------------------------------------- behaviour

def behaviour_table(s):
    """All trials of a session with choice, reward, high port, block position and timing."""
    t = add_history(s["trials"])
    t["high_left"] = t.left_reward_prob > t.right_reward_prob
    t["high"] = (t.chose_left == t.high_left)
    blk = (t.high_left != t.high_left.shift(1)).cumsum()
    t["block"] = blk
    t["block_pos"] = t.groupby("block").cumcount()
    t["first_block"] = blk == 1
    t["decision_time"] = t.side_in_time - t.center_in_time
    t["iti"] = t.start_time - t.stop_time.shift(1)
    t["session"] = s["mouse"] + "_" + s["date"]
    t["mouse"] = s["mouse"]
    return t


def block_position_curves(tab, before=10, after=30):
    """P(switch) and P(high port) by position relative to block transitions (transition = 0).

    Positions before the transition count back from the end of the previous block. The first
    block of a session has no transition and is used only for negative positions of block 2."""
    rows = []
    for sess, t in tab.groupby("session"):
        t = t.reset_index(drop=True)
        starts = t.index[(t.block_pos == 0) & ~t.first_block]
        for st in starts:
            for k in range(-before, after + 1):
                i = st + k
                if 0 <= i < len(t):
                    if k >= 0 and t.block[i] != t.block[st]:
                        continue
                    if k < 0 and t.block[i] != t.block[st] - 1:
                        continue
                    rows.append((sess, k, float(t.high[i]), t.switch[i]))
    # P(high port) is the choice of the high port of the block the trial is in, as in the code's plots:
    # high before the transition, dropping at it and recovering after it
    return pd.DataFrame(rows, columns=["session", "block_pos", "phigh", "pswitch"])


def tau_highport(curve):
    """Time constant of the recovery of P(high port) after a transition (block_transition_stats.ipynb).

    a*exp(k*x) + baseline fitted over block positions 0 to 30, baseline = mean P(high port) over the
    10 trials before the transition; returned as -1/k (the code's tau_and_error), positive for a
    recovering curve."""
    from scipy.optimize import curve_fit
    base = curve.loc[(curve.block_pos >= -10) & (curve.block_pos < 0), "phigh"].mean()
    c = curve[(curve.block_pos >= 0) & (curve.block_pos <= 30)]
    f = lambda x, a, k: a * np.exp(x * k) + base  # noqa: E731
    try:
        popt, _ = curve_fit(f, c.block_pos.values, c.phigh.values, p0=[0, -0.5], maxfev=20000)
    except RuntimeError:
        return np.nan
    return -1 / popt[1]


def rflr_probs(params, choices, rewards):
    """P(choose left) per trial for one session (bandit_models.single_state_model_sessions)."""
    alpha, beta, tau = params
    gamma = np.exp(-1 / tau)
    cbar = 2 * choices - 1
    p = np.empty(len(choices))
    p[0] = 0.5
    phi = beta * rewards[0] * cbar[0]
    for t in range(1, len(choices)):
        p[t] = expit(phi + alpha * cbar[t - 1])
        phi = gamma * phi + beta * rewards[t] * cbar[t]
    return p


def rflr_nll(params, sessions):
    if params[2] <= 0.05:
        return 1e12
    nll = 0.0
    for c, r in sessions:
        p = np.clip(rflr_probs(params, c, r)[1:], 1e-9, 1 - 1e-9)
        y = c[1:]
        nll -= (y * np.log(p) + (1 - y) * np.log(1 - p)).sum()
    return nll


def fit_rflr(sessions):
    """Maximum-likelihood alpha, beta, tau over a list of (choices, rewards) arrays."""
    best = None
    for x0 in ([0.5, 2.0, 1.5], [0.0, 1.0, 3.0]):
        res = minimize(rflr_nll, x0, args=(sessions,), method="Nelder-Mead",
                       options={"maxiter": 4000, "xatol": 1e-4, "fatol": 1e-4})
        if best is None or res.fun < best.fun:
            best = res
    return best.x, best.fun


def session_arrays(tab):
    return [(t.choice.values.astype(int), t.was_rewarded.values.astype(int))
            for _, t in tab.groupby("session")]


# ----------------------------------------------------------------------------- GLM (Methods, GLM)

GLM_T = 20                 # time shifts forward and backward, 54 ms each (Methods, GLM)


def glm_events(s, predictor_set="P1", history=False):
    """Binary event predictors (sample indices) for one session.

    P1: centre entry, centre exit, side entry, side exit, lick onset and reward (the side entry of
    rewarded trials, when the reward is delivered); P2 adds lick offset and LED onset and offset.
    history=True replaces side entry by eight side-entry predictors, one per two-trial word."""
    e = s["events"]
    ev = {"centre_entry": e["center_port"], "centre_exit": s["exits"]["center_port"],
          "side_entry": np.r_[e["left_port"], e["right_port"]],
          "side_exit": np.r_[s["exits"]["left_port"], s["exits"]["right_port"]],
          "lick": np.r_[e["left_lick"], e["right_lick"]]}
    t = add_history(s["trials"])
    ok = t.photometry_side_in_index >= 0
    ev["reward"] = t.photometry_side_in_index[ok & t.was_rewarded].values
    if predictor_set == "P2":
        ev["lick_offset"] = np.r_[s["exits"]["left_lick"], s["exits"]["right_lick"]]
        ev["led_onset"] = np.r_[e["center_LED"], e["side_LED"]]
        ev["led_offset"] = np.r_[s["exits"]["center_LED"], s["exits"]["side_LED"]]
    if history:
        del ev["side_entry"]
        for w in ["AA", "Aa", "aA", "aa", "AB", "Ab", "aB", "ab"]:
            ev[f"side_entry_{w}"] = t.photometry_side_in_index[ok & (t.word == w)].values
    return ev


def glm_session(s, ch_y, events, continuous=None, T=GLM_T):
    """Design rows of one session: trial segments from T samples before centre entry to T after side exit.

    Returns a sparse design (intercept first, then 2T+1 shifted copies of each predictor; a
    column for shift k at row n holds predictor[n - k]), the response, the trial of each row and
    the column names. Segments of neighbouring trials that overlap are both kept (Methods)."""
    from scipy import sparse
    n = s["n_samples"]
    t = s["trials"]
    ok = (t.photometry_center_in_index >= 0) & (t.photometry_side_out_index >= 0)
    rows, trial_of = [], []
    for i, c0, c1 in zip(t.trial[ok], t.photometry_center_in_index[ok], t.photometry_side_out_index[ok]):
        lo, hi = max(c0 - T, 0), min(c1 + T, n - 1)
        rows.append(np.arange(lo, hi + 1))
        trial_of.append(np.full(hi - lo + 1, i))
    rows, trial_of = np.concatenate(rows), np.concatenate(trial_of)
    shifts = np.arange(-T, T + 1)
    blocks, names = [sparse.csr_matrix(np.ones((len(rows), 1)))], ["intercept"]
    for name, idx in events.items():
        idx = np.unique(np.asarray(idx, int))
        ind = np.zeros(n, bool)
        ind[idx[(idx >= 0) & (idx < n)]] = True
        src = rows[:, None] - shifts[None, :]
        valid = (src >= 0) & (src < n)
        m = np.zeros(src.shape, bool)
        m[valid] = ind[src[valid]]
        blocks.append(sparse.csr_matrix(m.astype(np.float64)))
        names += [f"{name}:{k}" for k in shifts]
    for name, x in (continuous or {}).items():
        src = rows[:, None] - shifts[None, :]
        valid = (src >= 0) & (src < n)
        m = np.zeros(src.shape)
        m[valid] = x[src[valid]]
        blocks.append(sparse.csr_matrix(m))
        names += [f"{name}:{k}" for k in shifts]
    X = sparse.hstack(blocks).tocsr()
    return X, s["z"][ch_y][rows].astype(np.float64), trial_of, names


def suff_stats(X, y, mask):
    Xm = X[mask]
    ym = y[mask]
    return {"XtX": (Xm.T @ Xm).toarray(), "Xty": np.asarray(Xm.T @ ym).ravel(), "yty": float(ym @ ym),
            "ysum": float(ym.sum()), "n": int(mask.sum())}


def add_stats(a, b, sign=1):
    return {k: a[k] + sign * b[k] for k in a}


def fit_ols(st, cols=None):
    XtX, Xty = st["XtX"], st["Xty"]
    if cols is not None:
        XtX, Xty = XtX[np.ix_(cols, cols)], Xty[cols]
    try:
        return np.linalg.solve(XtX, Xty)
    except np.linalg.LinAlgError:          # a predictor with no events: minimum-norm solution
        return np.linalg.lstsq(XtX, Xty, rcond=None)[0]


def sse(st, b, cols=None):
    XtX, Xty = st["XtX"], st["Xty"]
    if cols is not None:
        XtX, Xty = XtX[np.ix_(cols, cols)], Xty[cols]
    return st["yty"] - 2 * b @ Xty + b @ XtX @ b


def r2(st, b, cols=None):
    sst = st["yty"] - st["ysum"] ** 2 / st["n"]
    return 1 - sse(st, b, cols) / sst
