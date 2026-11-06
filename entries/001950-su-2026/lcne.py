"""Loading and measures for dandiset 001950, LC-NE activity during dynamic foraging.

Su et al., "Topographic structure and function of locus coeruleus noradrenaline neurons",
Nature (doi:10.1038/s41586-026-11026-0); preprint doi:10.64898/2026.04.10.717727 (the text the
claims file was read from; Methods sections are cited by their titles there).

The dandiset holds one NWB file per session: a trial table for every session, lick and reward
times, spike-sorted units with opto-tagging metrics (and CCF coordinates for some Neuropixels
sessions), pupil diameter for some sessions, and fiber photometry for others. Files are streamed
from the archive at the pinned version with remfile and h5py; nothing is written to disk.

Where the parameters come from:

- Trials. A trial is a go cue; no-go cues (`trial_type` CSminus, present only in tetrode and
  photometry sessions) are part of the inter-trial interval (Methods, Data analysis: "no-go
  cues (when presented) were treated as part of the inter-trial interval"). A response is
  `animal_response` 0 (left) or 1 (right); 2 is no response. Rewarded is `rewarded_historyL` or
  `rewarded_historyR`. Switch is a responded trial whose choice differs from the previous
  responded trial (`SWITCH_PREV_RESPONDED`, as the paper's code makeSessionDF builds it from
  the responded trials only); the variant compares with the previous trial and leaves the
  trial out when that trial was not responded.
- Unit selection (`select_units`) follows the criteria file metrics/beh_all.json of the
  paper's code (github.com/AllenNeuralDynamics/aind-beh-ephys-analysis at 971c1ca), cited by
  the claims file: maximum increase of p(response | laser) 0.55 to 1, latency at that maximum
  2 to 20 ms, waveform Euclidean distance at most 0.35 and correlation at least 0.95 to the
  light-evoked waveform, default QC, peak -1000 to 500 uV, 4.5 to 6 passing pulses, location
  along the probe 0 to 2000 um for Neuropixels, 100 to 2000 trials, ISI violation ratio at most
  0.1, slow drift ratio `sd` at most 0.3. The file allows 0.2 for cortex-projecting units
  (`tier_1`), which the dandiset does not mark, so 0.1 is applied to all (a deviation).
  Tetrode units have no ISI violation column; it is computed here from the spike times with
  the formula of the Neuropixels column (Hill et al. 2011, 1.5 ms, as its description says).
  `sd` is computed as make_combined_unit_tbl.py computes it when no drift file exists
  (spike counts in 300 s windows stepped by 100 s, SD over mean), over the span of the trials;
  the code's per-unit drift cuts are not in the dandiset (a deviation).
- Session criteria follow metrics/beh_only.json where the dandiset allows: at least 90
  responded trials (`session_len`), probability of switching after no reward at least 0.04
  (`p_sw_L`), and the lag-1 reward minus no-reward coefficient of the choice regression at
  least 0 (`diff_1`). Its other two criteria (`aN`, the model's no-reward learning rate, and
  `bias`, the model's side bias) need the Q-learning fits, which are not in the dandiset.
- Windows. Go-cue response 0.01 to 0.3 s after the cue against 2 s to 0.01 s before it (claim
  fig4g criterion); tonic window 0.5 s before the cue (Methods, Comparison of phasic and tonic
  responses); switch window 0.01 to 0.5 s after the cue (Methods, Linear regression models of
  spike rates, "0.5 s after go cue"); photometry switch window 0.75 s after the cue and baseline
  2 s before it (Methods, Linear regression models of axonal GCaMP).
- Spatial tests (`linear_spatial_test`, `knn_spatial_test`) follow Methods, Analyzing
  relationships with space: ML mirrored by absolute value, OLS R2 with a one-sided permutation
  p over 5,000 permutations, distance-weighted kNN with k = 20 and 5-fold cross-validation. The
  kNN permutation count is 1,000 here to keep the run short (a standard choice; the p floor is
  1/1001).
- CCF coordinates in the files are in mm, in the frame the paper's code calls LPS (x ML, y AP,
  z DV); they are referenced to bregma at (-5.7, 5.4, -0.45) mm as in
  F_spatial-axis-comparison.ipynb, so that y is posterior and z dorsal.
"""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "001950"
DANDISET_VERSION = "0.260928.2230"
API = "https://api.dandiarchive.org/api"

BREGMA_LPS_MM = np.array([-5.7, 5.4, -0.45])  # F_spatial-axis-comparison.ipynb, cell 5

SWITCH_PREV_RESPONDED = True

TRIAL_COLUMNS = ["start_time", "stop_time", "goCue_start_time", "reward_outcome_time",
                 "animal_response", "rewarded_historyL", "rewarded_historyR", "trial_type",
                 "auto_waterL", "auto_waterR", "reward_delay", "response_duration",
                 "ITI_duration", "laser_on_trial"]

UNIT_SCALARS = ["unit_id", "default_qc", "peak", "isi_violations_ratio", "location_along_probe",
                "maximum_increase_of_p(response_cond_laser)",
                "spike_latency_at_maximum_p(response_cond_laser)",
                "waveform_euclidean_distance_at_maximum_p(response_cond_laser)",
                "waveform_correlation_at_maximum_p(response_cond_laser)",
                "number_of_pulses_passing_in_opto_tagging", "opto_tagged_lowbar",
                "opto_tagged_midbar", "firing_rate", "decoder_label", "peak_to_valley",
                "x_coordinate_in_ccf_space", "y_coordinate_in_ccf_space",
                "z_coordinate_in_ccf_space", "top_of_LC_range", "bottom_of_LC_range",
                "if_real_unit", "location_of_tagged_unit", "device_name"]

# metrics/beh_all.json bounds
OPTO_BOUNDS = {
    "maximum_increase_of_p(response_cond_laser)": (0.55, 1.0),
    "spike_latency_at_maximum_p(response_cond_laser)": (0.002, 0.02),
    "waveform_euclidean_distance_at_maximum_p(response_cond_laser)": (0.0, 0.35),
    "waveform_correlation_at_maximum_p(response_cond_laser)": (0.95, 1.0),
    "peak": (-1000, 500),
    "number_of_pulses_passing_in_opto_tagging": (4.5, 6),
}
ISI_MAX = 0.1
SD_MAX = 0.3
TRIAL_COUNT_BOUNDS = (100, 2000)
NP_LOCATION_BOUNDS = (0, 2000)
ISI_THRESHOLD_S = 0.0015


# ---------------------------------------------------------------- archive access

def list_assets(version: str = DANDISET_VERSION) -> pd.DataFrame:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += page["results"]
        url = page.get("next")
    df = pd.DataFrame([{"path": r["path"], "asset_id": r["asset_id"], "size": r["size"]} for r in rows])
    df["subject"] = df.path.str.split("/").str[0].str.replace("sub-", "", regex=False)
    df["kind"] = df.path.str.extract(r"_([a-z+]+)\.nwb$")[0]
    df["session"] = df.path.str.extract(r"_ses-(.+)_[a-z+]+\.nwb$")[0]
    return df.sort_values("path").reset_index(drop=True)


def s3_url(asset_id: str) -> str:
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


def open_nwb(asset_id: str) -> h5py.File:
    for attempt in range(4):
        try:
            return h5py.File(remfile.File(s3_url(asset_id)), "r")
        except Exception:
            if attempt == 3:
                raise
    raise RuntimeError


def pmap(fn, items, workers=16):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(fn, items))


def _decode(v):
    return v.decode() if isinstance(v, bytes) else v


# ---------------------------------------------------------------- trials

def read_trials(f: h5py.File) -> pd.DataFrame:
    t = f["intervals/trials"]
    d = {}
    for c in TRIAL_COLUMNS:
        if c in t:
            v = t[c][:]
            if v.dtype.kind in "OS":
                v = np.array([_decode(x) for x in v], dtype=object)
            d[c] = v
    df = pd.DataFrame(d)
    if "trial_type" not in df:
        df["trial_type"] = "CSplus"
    df["go"] = df.trial_type != "CSminus"
    df["responded"] = df.animal_response.isin([0, 1]) & df.go
    df["rewarded"] = (df.rewarded_historyL.astype(bool) | df.rewarded_historyR.astype(bool)) & df.responded
    df["choice_right"] = np.where(df.responded, (df.animal_response == 1).astype(float), np.nan)
    df["auto_water"] = (df.get("auto_waterL", 0) + df.get("auto_waterR", 0)) > 0
    return df


def go_trials(trials: pd.DataFrame) -> pd.DataFrame:
    """Go-cue trials only (no-go cues are part of the inter-trial interval)."""
    g = trials[trials.go].copy().reset_index(drop=True)
    resp = g[g.responded]
    prev = resp.choice_right.shift(1)
    sw = (resp.choice_right != prev).astype(float)
    sw[prev.isna()] = np.nan
    g["switch_prev_responded"] = np.nan
    g.loc[resp.index, "switch_prev_responded"] = sw.values
    prev_trial = g.choice_right.shift(1)
    g["switch_prev_trial"] = np.where(g.responded & prev_trial.notna(),
                                      (g.choice_right != prev_trial).astype(float), np.nan)
    return g


def read_licks(f: h5py.File) -> dict:
    out = {}
    for side in ("left", "right"):
        k = f"acquisition/{side}_lick_time/timestamps"
        out[side] = f[k][:] if k in f else np.array([])
    return out


# ---------------------------------------------------------------- behavior models

def history_matrix(g: pd.DataFrame, lags: int):
    """Choice regression of the Methods (Analyses and models of behavior): rightward choice on
    rewarded (R) and unrewarded (N) choice history and choice history, signed +1 right, -1 left,
    over the responded trials of one session."""
    r = g[g.responded].reset_index(drop=True)
    c = 2 * r.choice_right.values - 1
    R = c * r.rewarded.values
    N = c * (~r.rewarded.values.astype(bool))
    X, y = [], []
    for t in range(lags, len(r)):
        X.append(np.concatenate([R[t - lags:t][::-1], N[t - lags:t][::-1], c[t - lags:t][::-1]]))
        y.append(r.choice_right.values[t])
    return np.array(X), np.array(y)


def p_switch_after_loss(g):
    r = g[g.responded].reset_index(drop=True)
    lost = ~r.rewarded.values.astype(bool)
    sw = (r.choice_right.values[1:] != r.choice_right.values[:-1])
    return float(np.mean(sw[lost[:-1]])) if lost[:-1].sum() else np.nan


# ---------------------------------------------------------------- units

def read_units(f: h5py.File) -> pd.DataFrame:
    u = f["units"]
    d = {}
    for c in UNIT_SCALARS:
        if c in u:
            v = u[c][:]
            if v.dtype.kind in "OS":
                v = np.array([_decode(x) for x in v], dtype=object)
                if c not in ("decoder_label", "device_name", "unit_id"):
                    v = pd.to_numeric(pd.Series(v), errors="coerce").values
            d[c] = v
    df = pd.DataFrame(d)
    idx = u["spike_times_index"][:]
    df["spk_start"] = np.concatenate([[0], idx[:-1]])
    df["spk_stop"] = idx
    df["n_spikes"] = df.spk_stop - df.spk_start
    df["row"] = np.arange(len(df))
    df["probe"] = "NP" if "device_name" in u else "TT"
    return df


def spikes(f: h5py.File, units: pd.DataFrame) -> list:
    st = f["units/spike_times"]
    return [st[int(a):int(b)] for a, b in zip(units.spk_start, units.spk_stop)]


def isi_violation_ratio(spk: np.ndarray, duration: float, thr: float = ISI_THRESHOLD_S) -> float:
    """Hill et al. (2011) ratio, as spikeinterface's isi_violations_ratio (min ISI 0)."""
    n = len(spk)
    if n < 2 or duration <= 0:
        return np.nan
    nv = np.sum(np.diff(np.sort(spk)) < thr)
    return float(nv * duration / (2 * n * n * thr))


def slow_drift_ratio(spk, start, end, bin_short=100.0, bin_long=300.0):
    """make_combined_unit_tbl.py, branch without a drift file."""
    if end - start < bin_long * 2:
        return np.nan
    edges = np.arange(start, end, bin_short)
    counts = np.array([np.sum((spk >= edges[i] - 0.5 * bin_long) & (spk < edges[i + 1] + 0.5 * bin_long)) / bin_long
                       for i in range(len(edges) - 1)])
    return float(np.std(counts) / np.mean(counts)) if np.mean(counts) > 0 else np.nan


def opto_pass(units: pd.DataFrame) -> pd.Series:
    ok = units.default_qc.astype(bool)
    for c, (lo, hi) in OPTO_BOUNDS.items():
        ok &= units[c].between(lo, hi)
    if (units.probe == "NP").any():
        ok &= ~((units.probe == "NP") & ~units.location_along_probe.between(*NP_LOCATION_BOUNDS))
    return ok


def rate_in_windows(spk: np.ndarray, align: np.ndarray, start: float, stop: float) -> np.ndarray:
    """Spike rate (Hz) in [align + start, align + stop) for each event."""
    lo = np.searchsorted(spk, align + start)
    hi = np.searchsorted(spk, align + stop)
    return (hi - lo) / (stop - start)


# ---------------------------------------------------------------- regressions

def ols_t(y, X):
    """t-statistic and p of the first regressor of an OLS with intercept (statsmodels)."""
    import statsmodels.api as sm
    X = np.column_stack(X) if isinstance(X, (list, tuple)) else np.asarray(X)
    if X.ndim == 1:
        X = X[:, None]
    ok = np.isfinite(y) & np.all(np.isfinite(X), axis=1)
    y, X = y[ok], X[ok]
    if len(y) < X.shape[1] + 3 or np.std(X[:, 0]) == 0 or np.std(y) == 0:
        return np.nan, np.nan, np.nan
    m = sm.OLS(y, sm.add_constant(X, has_constant="add")).fit()
    return float(m.tvalues[1]), float(m.pvalues[1]), float(m.params[1])


# ---------------------------------------------------------------- spatial tests

def ccf_lps(units: pd.DataFrame) -> np.ndarray:
    """CCF coordinates relative to bregma, ML mirrored: columns ML, AP (posterior +), DV
    (dorsal +), in mm (F_spatial-axis-comparison.ipynb, cell 33)."""
    c = units[["x_coordinate_in_ccf_space", "y_coordinate_in_ccf_space",
               "z_coordinate_in_ccf_space"]].values.astype(float) - BREGMA_LPS_MM
    c[:, 0] = np.abs(c[:, 0])
    return c


def linear_spatial_test(y, X, n_perm=5000, rng=None):
    """OLS of y on the three coordinates; R2, unit gradient and one-sided permutation p."""
    rng = rng or np.random.default_rng(0)
    A = np.column_stack([np.ones(len(y)), X])

    def r2(v):
        beta, *_ = np.linalg.lstsq(A, v, rcond=None)
        res = v - A @ beta
        return 1 - res @ res / np.sum((v - v.mean()) ** 2), beta[1:]

    obs, beta = r2(y)
    null = np.array([r2(rng.permutation(y))[0] for _ in range(n_perm)])
    p = (1 + np.sum(null >= obs)) / (n_perm + 1)
    return {"r2": float(obs), "p": float(p), "axis": beta / np.linalg.norm(beta), "n": len(y)}


def knn_cv_r2(y, X, k=20, folds=5, seed=0):
    from sklearn.model_selection import KFold
    from sklearn.neighbors import KNeighborsRegressor
    pred = np.empty(len(y))
    for tr, te in KFold(folds, shuffle=True, random_state=seed).split(X):
        m = KNeighborsRegressor(n_neighbors=min(k, len(tr)), weights="distance").fit(X[tr], y[tr])
        pred[te] = m.predict(X[te])
    return 1 - np.sum((y - pred) ** 2) / np.sum((y - y.mean()) ** 2)


def knn_spatial_test(y, X, n_perm=1000, rng=None):
    rng = rng or np.random.default_rng(0)
    obs = knn_cv_r2(y, X)
    null = np.array([knn_cv_r2(rng.permutation(y), X) for _ in range(n_perm)])
    return {"r2": float(obs), "p": float((1 + np.sum(null >= obs)) / (n_perm + 1)), "n": len(y)}


# ---------------------------------------------------------------- one pass over the dandiset

FP_SIGNAL = "G_PL-L_tri-exp_mc"   # photometry_generation.py: channel 'G_tri-exp_mc', region PL
FP_ISO = "Iso_PL-L_tri-exp_mc"
WAVEFORM = "waveform_on_peak_channel_of_raw_waveform"


def load_session(asset: dict) -> dict:
    """Everything the notebook uses from one file: the trial table, licks, pupil diameter,
    PL photometry, and the units passing the opto-tagging criteria with their spike times and
    peak-channel mean waveforms. Other units keep only their scalar columns."""
    f = open_nwb(asset["asset_id"])
    out = {"path": asset["path"], "kind": asset["kind"], "subject": asset["subject"],
           "trials": read_trials(f), "licks": read_licks(f), "units": None, "spikes": None,
           "waveforms": None, "pupil": None, "fp": None}
    if "processing/behavior/pupil_diameter" in f:
        p = f["processing/behavior/pupil_diameter"]
        out["pupil"] = (p["timestamps"][:], p["data"][:])
    if f"acquisition/{FP_SIGNAL}" in f:
        out["fp"] = (f[f"acquisition/{FP_SIGNAL}/timestamps"][:], f[f"acquisition/{FP_SIGNAL}/data"][:],
                     f[f"acquisition/{FP_ISO}/data"][:])
    if "units" in f:
        u = read_units(f)
        sel = u[opto_pass(u)]
        out["units"] = u
        out["spikes"] = dict(zip(sel.row, spikes(f, sel)))
        if WAVEFORM in f["units"] and len(sel):
            w = f[f"units/{WAVEFORM}"]
            out["waveforms"] = {r: w[int(r)] for r in sel.row}
    return out


def load_all(assets: pd.DataFrame, workers: int = 24) -> list:
    rows = [r for _, r in assets.iterrows()]
    return pmap(lambda r: load_session(r.to_dict()), rows, workers=workers)


# ---------------------------------------------------------------- Q-learning model

def q_trajectory(params, choice, reward):
    """stan_qLearning_5params (aind_stan_fit_sim at 89371ee): Q starts at 0; the chosen value
    moves by aP * PE when PE >= 0 and aN * PE when PE < 0; the unchosen value is multiplied by
    aF; P(right) = logistic(beta * (Q_right - Q_left) + bias). Returns Q (before each trial's
    update, columns left, right), PE and P(right)."""
    aN, aP, aF, beta, bias = params
    Q = np.zeros(2)
    n = len(choice)
    Qs = np.zeros((n, 2))
    pe = np.zeros(n)
    pr = np.zeros(n)
    for t in range(n):
        Qs[t] = Q
        pr[t] = 1 / (1 + np.exp(-(beta * (Q[1] - Q[0]) + bias)))
        c = int(choice[t])
        d = reward[t] - Q[c]
        pe[t] = d
        Q[c] += (aN if d < 0 else aP) * d
        Q[1 - c] *= aF
    return Qs, pe, pr


def fit_q_session(choice, reward, starts=((0.3, 0.6, 0.8, 4.0, 0.0), (0.1, 0.3, 0.5, 2.0, 0.0), (0.6, 0.8, 0.95, 6.0, 0.0))):
    """Maximum-likelihood fit of the five parameters for one session (a substitute for the
    paper's hierarchical Bayesian fit; see the notebook)."""
    from scipy.optimize import minimize
    choice = np.asarray(choice, dtype=int)
    reward = np.asarray(reward, dtype=float)

    def nll(x):
        _, _, pr = q_trajectory(x, choice, reward)
        pr = np.clip(pr, 1e-9, 1 - 1e-9)
        return -np.sum(choice * np.log(pr) + (1 - choice) * np.log(1 - pr))

    bounds = [(1e-3, 1), (1e-3, 1), (0, 1), (1e-3, 10), (-5, 5)]
    best = None
    for x0 in starts:
        r = minimize(nll, x0, method="L-BFGS-B", bounds=bounds)
        if best is None or r.fun < best.fun:
            best = r
    return best.x, best.fun


# ---------------------------------------------------------------- circular statistics

def rayleigh(theta):
    n = len(theta)
    R = np.abs(np.mean(np.exp(1j * theta)))
    z = n * R ** 2
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - (n * R) ** 2)) - (1 + 2 * n))
    return float(z), float(min(p, 1.0))


def watson_wheeler(a, b, n_perm=5000, rng=None):
    """Mardia-Watson-Wheeler W on circular ranks, with a label-permutation p = (k + 1)/(N + 1)
    (Methods, Circular distribution comparison)."""
    rng = rng or np.random.default_rng(0)
    x = np.concatenate([a, b])
    N = len(x)
    ranks = stats_rankdata(np.mod(x, 2 * np.pi))
    ang = 2 * np.pi * ranks / N

    def W(lab):
        w = 0.0
        for g in (lab, ~lab):
            n = g.sum()
            w += (np.cos(ang[g]).sum() ** 2 + np.sin(ang[g]).sum() ** 2) / n
        return 2 * w

    lab = np.zeros(N, dtype=bool)
    lab[:len(a)] = True
    obs = W(lab)
    null = np.array([W(rng.permutation(lab)) for _ in range(n_perm)])
    return float(obs), float((np.sum(null >= obs) + 1) / (n_perm + 1))


def stats_rankdata(v):
    from scipy.stats import rankdata
    return rankdata(v)


def auroc(a, b):
    """Area under the ROC curve for a against b (Mann-Whitney U / n_a n_b)."""
    from scipy.stats import mannwhitneyu
    if len(a) == 0 or len(b) == 0:
        return np.nan
    return mannwhitneyu(a, b, alternative="two-sided").statistic / (len(a) * len(b))
