"""Loading and population measures for dandiset 000688 (Perich, Gallego & Miller 2018).

Perich MG, Gallego JA, Miller LE (2018). A neural population mechanism for rapid learning.
Neuron 100, 964-976. doi:10.1016/j.neuron.2018.09.030.

Each NWB file holds one session of one monkey: sorted units (spike times, the electrode of
each unit and so its array, M1 or PMd), cursor position, velocity and acceleration (cm, 100 Hz),
and a trial table (start, stop, target onset, go cue, target id, direction and corners, and the
result: R reward, A abort, F fail, I incomplete). The files have no epoch or perturbation column.
Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from (claim ids and the shared methods M1 to M8 and open details O1
to O10 are those of claims/000688/10.1016-j.neuron.2018.09.030.yaml):

- `BIN_S` = 50 ms bins, square root of counts, non-causal Gaussian kernel of "width 100 ms":
  STAR Methods, Dimensionality reduction (M2). `KERNEL_SD_S` holds both readings of the width
  (O4): a standard deviation of 100 ms, or a full width at half maximum of 100 ms. The claims
  file expected this not to change an outcome; it changes the fig3b medians and the fig6c
  significance, so both readings are run throughout. The notebook adopts the standard deviation
  for every claim.
- PCA per area per session on Baseline reward trials only, 8 M1 and 16 PMd components: STAR
  Methods, Output-potent and output-null subspaces ("We used only trials from the Baseline period
  of each session to find the axes for PCA") and Results ("for M1 we used the first eight").
- The trial window is open (O3): (a) target presentation to target acquisition, (b) the whole
  trial. Target acquisition is not in the trial table. It is taken as the trial's stop time minus
  the 0.5 s target hold ("The monkeys had one second to reach the target, and were required to
  hold there for 0.5 s", STAR Methods, Behavioral task), assuming that a reward trial stops at
  the end of the hold. The cursor cannot be used: in several sessions it never enters the square
  given by `target_corners` (the data check shows this).
- W: ordinary least squares from the 16 PMd to the 8 M1 latent dimensions at zero lag (O7, the
  claims file's standard choice); the first R = 8 rows of V' are potent, the last 8 null (O7).
- Dimensionality (`dimensionality`): STAR Methods, Dimensionality reduction, paragraph 2, after
  Machens et al. 2010: trial-averaged rates per target, noise from differences between random
  pairs of trials to the same target, 1000 repetitions, the 99th percentile of each noise
  eigenvalue; threshold rules (a) and (b) of O9. For averaging, trials are aligned on the
  window start and cut to the shortest window of the session (a standard choice; the paper does not say
  how trials of unequal length are averaged). The scale of the noise is not stated. Three readings
  are computed: the raw differences (the text's wording), the difference over the square root of
  two (single-trial noise), and the difference over the square root of 2K (the noise of an average
  of K trials). The first two give 0 dimensions everywhere, so the third is adopted as an
  assumption (notebook, fig3b-pmd-higher-dimensional, which also checks it on synthetic data of
  known rank: rule (b) recovers the rank, rule (a) overestimates it).
- Null/potent index (`null_potent_index`): STAR Methods, Output-potent and output-null
  subspaces, last paragraph: the PCA loading matrix times V, (|potent| - |null|) / (|potent| +
  |null|) summed over dimensions; "magnitude" as the sum of absolute values or of squares.
- Lag (`cca_lag`): STAR Methods, Calculating the lag: Baseline trials, 700 ms after target
  presentation, potent activity shifted from -350 to 350 ms in 10 ms steps, first canonical
  correlation at each lag. Time resolution is open (claims file): (a) 10 ms bins smoothed as M2,
  (b) 50 ms latent activity interpolated to 10 ms. A negative lag means null precedes potent
  (Figure 6B legend, "A peak left of zero indicates that output-null leads output-potent").
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "000688"
DANDISET_VERSION = "0.250122.1735"

# The dual-array (M1 and PMd) center-out sessions of Monkeys C and M whose unit counts the
# notebook compares with the paper's; selected in the notebook's data check, listed here so that
# later notebooks can load them by name.
CANDIDATE_SESSIONS = [
    "sub-C_ses-CO-20160909", "sub-C_ses-CO-20160912", "sub-C_ses-CO-20160914",
    "sub-C_ses-CO-20160915", "sub-C_ses-CO-20160919", "sub-C_ses-CO-20160921",
    "sub-C_ses-CO-20160923", "sub-C_ses-CO-20160929", "sub-C_ses-CO-20161005",
    "sub-C_ses-CO-20161006", "sub-C_ses-CO-20161007", "sub-C_ses-CO-20161011",
    "sub-C_ses-CO-20161013", "sub-C_ses-CO-20161021",
    "sub-M_ses-CO-20140203", "sub-M_ses-CO-20140217", "sub-M_ses-CO-20140218",
    "sub-M_ses-CO-20140303", "sub-M_ses-CO-20140304", "sub-M_ses-CO-20140306",
    "sub-M_ses-CO-20140307",
]

TARGET_HOLD_S = 0.5                              # STAR Methods, Behavioral task
BIN_S = 0.05                                     # M2
KERNEL_SD_S = {"sd": 0.100, "fwhm": 0.100 / 2.3548}  # O4 readings
N_M1, N_PMD = 8, 16                              # Results, "first eight" and sixteen
NOISE_REPS = 1000                                # Methods, "We repeated this 1000 times"
NOISE_PCT = 99                                   # Methods, "the 99% limit"
VAR_EXPLAINED = 0.95                             # Methods, "95% of the remaining variance"
LAG_WINDOW_S = 0.700                             # Methods, Calculating the lag
LAGS_S = np.round(np.arange(-0.35, 0.3501, 0.01), 3)
FINE_BIN_S = 0.010                               # Methods, "10ms steps"


def asset_urls() -> dict[str, str]:
    """Session id -> S3 URL for every NWB file of the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        out = {}
        for a in ds.get_assets():
            if a.path.endswith(".nwb"):
                sid = a.path.split("/")[1].replace("_behavior+ecephys.nwb", "")
                out[sid] = a.get_content_url(follow_redirects=1, strip_query=True)
        return out


def _text(x):
    return x.decode() if isinstance(x, bytes) else x


def read_metadata(url: str) -> dict:
    """Trial counts, unit areas and descriptions of one file, without spikes or kinematics."""
    with h5py.File(remfile.File(url), "r") as f:
        tr = f["intervals/trials"]
        loc = f["general/extracellular_ephys/electrodes/location"][:]
        ue = f["units/electrodes"][:]
        ue_idx = f["units/electrodes_index"][:]
        first = np.r_[0, ue_idx[:-1]]
        areas = [_text(loc[ue[s]]) for s in first]
        res = [_text(x) for x in tr["result"][:]]
        return {
            "experiment": _text(f["general/experiment_description"][()]),
            "session_description": _text(f["session_description"][()]),
            "trial_columns": sorted(k for k in tr.keys() if k != "id"),
            "n_trials": len(res),
            "results": pd.Series(res).value_counts().to_dict(),
            "n_M1": sum(a == "Primary Motor Cortex" for a in areas),
            "n_PMd": sum(a == "Dorsal Premotor Cortex" for a in areas),
            "n_spikes": int(f["units/spike_times"].shape[0]),
            "first_start": float(tr["start_time"][0]),
            "last_stop": float(tr["stop_time"][-1]),
        }


def load_session(sid: str, url: str) -> dict:
    """Spikes, cursor kinematics and the trial table of one session."""
    with h5py.File(remfile.File(url), "r") as f:
        st = f["units/spike_times"][:]
        idx = f["units/spike_times_index"][:]
        loc = f["general/extracellular_ephys/electrodes/location"][:]
        ue = f["units/electrodes"][:]
        ue_idx = f["units/electrodes_index"][:]
        first = np.r_[0, ue_idx[:-1]]
        area = np.array(["M1" if _text(loc[ue[s]]) == "Primary Motor Cortex" else "PMd" for s in first])
        pos_g = f["processing/behavior/Position/cursor_pos"]
        pos = pos_g["data"][:]
        pos_t = pos_g["timestamps"][:]
        pos_unit = _text(pos_g["data"].attrs["unit"])
        tr = f["intervals/trials"]
        trials = pd.DataFrame({
            "start": tr["start_time"][:], "stop": tr["stop_time"][:],
            "target_on": tr["target_on_time"][:], "go_cue": tr["go_cue_time"][:],
            "target_id": tr["target_id"][:], "target_dir": tr["target_dir"][:],
            "result": [_text(x) for x in tr["result"][:]],
        })
        corners = tr["target_corners"][:]
    spikes = np.split(st, idx[:-1])
    trials["acquire"] = trials["stop"] - TARGET_HOLD_S
    trials["cursor_enters_target"] = _acquisition_times(trials, corners, pos_t, pos)
    trials["hand_radius_at_acquire"] = [
        np.hypot(*pos[min(np.searchsorted(pos_t, t), len(pos_t) - 1)]) if np.isfinite(t) else np.nan
        for t in trials["acquire"]]
    trials["target_radius"] = np.hypot((corners[:, 0] + corners[:, 2]) / 2, (corners[:, 1] + corners[:, 3]) / 2)
    return {"sid": sid, "monkey": sid[4], "spikes": spikes, "area": area, "trials": trials,
            "pos": pos, "pos_t": pos_t, "pos_unit": pos_unit}


def _acquisition_times(trials, corners, t, pos):
    """First time after the go cue at which the cursor is inside the target square (a check)."""
    out = np.full(len(trials), np.nan)
    for i, (go, stop) in enumerate(zip(trials["go_cue"], trials["stop"])):
        c = corners[i]
        if not (np.isfinite(go) and np.all(np.isfinite(c))):
            continue
        a, b = np.searchsorted(t, [go, stop])
        x, y = pos[a:b, 0], pos[a:b, 1]
        inside = (x >= min(c[0], c[2])) & (x <= max(c[0], c[2])) & (y >= min(c[1], c[3])) & (y <= max(c[1], c[3]))
        if inside.any():
            out[i] = t[a + np.argmax(inside)]
    return out


def initial_errors(sess, onset_frac=0.2, after_s=0.150):
    """Angle (degrees) between the cursor's direction 150 ms after movement onset and the target.

    Movement onset is the first sample after the go cue at which speed exceeds onset_frac of the
    trial's peak speed (O10 readings 0.1, 0.2, 0.3); the deviation from the target direction is
    taken after subtracting nothing (the Baseline mean per target is subtracted by the caller).
    Reward trials only; returns a DataFrame with the trial index, target and error.
    """
    t, pos = sess["pos_t"], sess["pos"]
    vel = np.gradient(pos, t, axis=0)
    speed = np.hypot(vel[:, 0], vel[:, 1])
    rows = []
    for i, r in sess["trials"].iterrows():
        if r.result != "R" or not np.isfinite(r.go_cue):
            continue
        a, b = np.searchsorted(t, [r.go_cue, r.stop])
        if b - a < 5:
            continue
        sp = speed[a:b]
        on = a + int(np.argmax(sp > onset_frac * sp.max()))
        k = min(np.searchsorted(t, t[on] + after_s), len(t) - 1)
        d = pos[k] - pos[on]
        err = np.degrees(np.angle(np.exp(1j * (np.arctan2(d[1], d[0]) - r.target_dir))))
        rows.append({"trial": i, "target_id": r.target_id, "error": err, "peak_speed": sp.max()})
    return pd.DataFrame(rows)


def load_sessions(sids, urls, workers=8):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda s: load_session(s, urls[s]), sids))


def baseline_trials(sess: dict, window: str) -> pd.DataFrame:
    """Reward trials with a target onset and go cue, whose acquisition follows target onset."""
    tr = sess["trials"]
    keep = (tr.result == "R") & tr.target_on.notna() & tr.go_cue.notna() & (tr.acquire > tr.target_on)
    return tr[keep].reset_index(drop=True)


def trial_bounds(tr: pd.DataFrame, window: str):
    """(start, end) of each trial's analysis window: (a) target onset to acquisition, (b) whole trial."""
    if window == "a":
        return tr.target_on.to_numpy(), tr.acquire.to_numpy()
    return tr.start.to_numpy(), tr.stop.to_numpy()


def binned(spikes, starts, ends, bin_s):
    """Spike counts per trial (list of arrays time x neurons) in bins from start to end."""
    out = []
    for s, e in zip(starts, ends):
        edges = s + bin_s * np.arange(int(np.floor((e - s) / bin_s + 1e-9)) + 1)
        out.append(np.stack([np.diff(np.searchsorted(sp, edges)) for sp in spikes], axis=1).astype(float))
    return out


def smooth(counts_list, bin_s, kernel_sd_s):
    """Square root of counts, then a non-causal Gaussian kernel along time, per trial (M2)."""
    return [gaussian_filter1d(np.sqrt(c), kernel_sd_s / bin_s, axis=0, mode="nearest") for c in counts_list]


def mean_rates(spikes, tr):
    """Trial-averaged firing rate of each unit (spikes/s) over the whole of the given trials."""
    dur = (tr.stop - tr.start).sum()
    return np.array([sum(np.searchsorted(sp, e) - np.searchsorted(sp, s) for s, e in zip(tr.start, tr.stop))
                     for sp in spikes]) / dur


def pca_axes(X: np.ndarray, k: int):
    """Mean and the first k principal axes (neurons x k) of time x neurons data."""
    mu = X.mean(0)
    _, _, vt = np.linalg.svd(X - mu, full_matrices=False)
    return mu, vt[:k].T


def subspaces(m1_latent: np.ndarray, pmd_latent: np.ndarray):
    """W (M1 = W PMd, least squares at zero lag) and its potent (first R rows of V') and null axes."""
    P = pmd_latent - pmd_latent.mean(0)
    M = m1_latent - m1_latent.mean(0)
    Wt, *_ = np.linalg.lstsq(P, M, rcond=None)  # P @ Wt = M, W = Wt.T (R x N)
    W = Wt.T
    _, _, vt = np.linalg.svd(W, full_matrices=True)
    R = W.shape[0]
    return W, vt[:R].T, vt[R:].T  # potent and null axes as N x R and N x (N - R)


def null_potent_index(loadings: np.ndarray, potent: np.ndarray, null: np.ndarray, power: int = 1):
    """Per neuron (|potent weights| - |null weights|) / total, from loading matrix times V."""
    wp = np.abs(loadings @ potent) ** power
    wn = np.abs(loadings @ null) ** power
    p, n = wp.sum(1), wn.sum(1)
    return (p - n) / (p + n)


def target_averages(rates_list, target_ids, n_bins):
    """Trial-averaged rates per target, each trial cut to n_bins from its start: targets x time x neurons."""
    targets = np.unique(target_ids)
    return np.stack([np.mean([r[:n_bins] for r, t in zip(rates_list, target_ids) if t == tg], axis=0)
                     for tg in targets])


NOISE_SCALES = ("raw", "sqrt2", "sqrt2K")


def _eigs(X):
    """Eigenvalues (descending) of the covariance of data (..., time, neurons), from the smaller Gram matrix."""
    Xc = X - X.mean(-2, keepdims=True)
    rows, cols = X.shape[-2:]
    G = np.swapaxes(Xc, -1, -2) @ Xc if cols <= rows else Xc @ np.swapaxes(Xc, -1, -2)
    ev = np.clip(np.linalg.eigvalsh(G)[..., ::-1], 0, None) / (rows - 1)
    out = np.zeros(X.shape[:-2] + (cols,))
    out[..., :ev.shape[-1]] = ev[..., :cols]
    return out


def dimensionality(rates_list, target_ids, rng, n_bins=None, reps=NOISE_REPS, chunk=100):
    """Machens et al. (2010) style dimensionality, as the Methods adapt it (O9 readings).

    Data: trial-averaged rates per target, trials aligned on the window start and cut to n_bins
    (default the shortest trial). Noise: the difference between two random trials to the same
    target, concatenated over targets, `reps` times; the 99th percentile of each noise eigenvalue.
    The scale of the noise is not given; readings: "raw" (the difference, as the text says),
    "sqrt2" (difference / sqrt 2, the single-trial noise) and "sqrt2K" (difference / sqrt(2 K),
    the noise of an average of K trials, K the mean number of trials per target).

    Returns {scale: (dim_a, dim_b)}: (a) the number of leading components whose variance exceeds
    the matching noise limit; (b) the number of components needed to explain 95% of the variance
    left after subtracting the noise limit from each eigenvalue (negative remainders set to 0).
    """
    if n_bins is None:
        n_bins = min(len(r) for r in rates_list)
    tids = np.asarray(target_ids)
    targets = np.unique(tids)
    trials_by_t = [np.stack([r[:n_bins] for r, t in zip(rates_list, tids) if t == tg]) for tg in targets]
    avg = np.concatenate([a.mean(0) for a in trials_by_t])
    eig = _eigs(avg)
    K = np.mean([len(a) for a in trials_by_t])
    noise = []
    for start in range(0, reps, chunk):
        n = min(chunk, reps - start)
        parts = []
        for arr in trials_by_t:
            i = rng.integers(0, len(arr), n)
            j = (i + rng.integers(1, len(arr), n)) % len(arr)   # a different trial, uniformly
            parts.append(arr[i] - arr[j])
        noise.append(_eigs(np.concatenate(parts, axis=1)))
    noise = np.concatenate(noise)
    raw_limit = np.percentile(noise, NOISE_PCT, axis=0)
    out = {}
    for name, factor in (("raw", 1.0), ("sqrt2", 0.5), ("sqrt2K", 1.0 / (2 * K))):
        limit = raw_limit * factor
        above = eig > limit
        dim_a = int(np.argmin(above)) if not above.all() else len(eig)
        remaining = np.clip(eig - limit, 0, None)
        if remaining.sum() > 0:
            dim_b = int(np.searchsorted(np.cumsum(remaining) / remaining.sum(), VAR_EXPLAINED) + 1)
        else:
            dim_b = 0
        out[name] = (dim_a, dim_b)
    return out


def latent_fit(sess, window, kernel_sd_s, units_m1=None, units_pmd=None):
    """PCA axes per area and the potent and null subspaces from Baseline reward trials.

    Returns a dict with the trials used and, per area, the units, the smoothed rates per trial,
    the PCA mean and axes and the latent activity; and W with the potent and null axes (in PMd
    latent space).
    """
    tr = baseline_trials(sess, window)
    s, e = trial_bounds(tr, window)
    out = {"trials": tr}
    for area, k, units in (("M1", N_M1, units_m1), ("PMd", N_PMD, units_pmd)):
        if units is None:
            units = np.flatnonzero(sess["area"] == area)
        rates = smooth(binned([sess["spikes"][u] for u in units], s, e, BIN_S), BIN_S, kernel_sd_s)
        X = np.concatenate(rates)
        mu, axes = pca_axes(X, k)
        out[area] = {"units": units, "rates": rates, "mu": mu, "axes": axes, "latent": (X - mu) @ axes}
    W, pot, nul = subspaces(out["M1"]["latent"], out["PMd"]["latent"])
    out.update(W=W, potent=pot, null=nul)
    return out


def first_cc(A: np.ndarray, B: np.ndarray) -> float:
    """First canonical correlation between two sets of variables (time x dims)."""
    def basis(X):
        q, _ = np.linalg.qr(X - X.mean(0))
        return q
    return float(np.linalg.svd(basis(A).T @ basis(B), compute_uv=False)[0])


LAG_PAD_S = 0.6  # data kept on each side of the 700 ms window, so that shifts and smoothing fit


def lag_grid_latents(sess, units, onsets, axes, resolution, kernel_sd_s):
    """Latent activity per trial on a 10 ms grid from onset - LAG_PAD_S to onset + 0.7 s + LAG_PAD_S.

    resolution "a": 10 ms bins, square root, Gaussian kernel; "b": the same on 50 ms bins, then
    linear interpolation to the 10 ms grid. axes is neurons x dims (PCA axes times V).
    """
    spikes = [sess["spikes"][u] for u in units]
    n_fine = int(round((LAG_WINDOW_S + 2 * LAG_PAD_S) / FINE_BIN_S))
    grid = -LAG_PAD_S + FINE_BIN_S * (np.arange(n_fine) + 0.5)
    starts = np.asarray(onsets) - LAG_PAD_S
    ends = starts + n_fine * FINE_BIN_S
    if resolution == "a":
        rates = smooth(binned(spikes, starts, ends, FINE_BIN_S), FINE_BIN_S, kernel_sd_s)
        return [r @ axes for r in rates]
    rates = smooth(binned(spikes, starts, ends, BIN_S), BIN_S, kernel_sd_s)
    out = []
    for r in rates:
        centers = -LAG_PAD_S + BIN_S * (np.arange(len(r)) + 0.5)
        lat = r @ axes
        out.append(np.stack([np.interp(grid, centers, lat[:, d]) for d in range(lat.shape[1])], axis=1))
    return out


def cca_lag(null_trials, potent_trials):
    """Lag (s) maximizing the first canonical correlation of null(t) with potent(t - lag).

    Inputs are per-trial latent arrays from `lag_grid_latents`; the window is the 700 ms after
    target onset, concatenated over trials. Returns (best lag, lags, correlations).
    """
    i0 = int(round(LAG_PAD_S / FINE_BIN_S))
    win = i0 + np.arange(int(round(LAG_WINDOW_S / FINE_BIN_S)))
    nul = np.concatenate([n[win] for n in null_trials])
    ccs = []
    for lag in LAGS_S:
        shift = int(round(lag / FINE_BIN_S))
        ccs.append(first_cc(nul, np.concatenate([p[win - shift] for p in potent_trials])))
    ccs = np.array(ccs)
    return float(LAGS_S[np.argmax(ccs)]), LAGS_S, ccs
