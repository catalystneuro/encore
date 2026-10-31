"""Loading and measures for dandiset 000897 (Neupane, Fiete & Jazayeri 2024, Nature 630, 704-711).

Each session has two files: `*_ecephys.nwb` (raw voltage, not read here) and
`*_behavior+ecephys.nwb`, which holds the trial table (`intervals/trials`), the sorted units
(`processing/ecephys/units`) and the eye and joystick traces (`processing/behavior`). Only the
second file is streamed, at the pinned version; nothing is written to disk.

Where the parameters come from (claims file claims/000897/10.1038-s41586-024-07557-z.yaml,
"opening comment" for the periodicity index, PI):

- MNAV trials are `trial_type == 3`; correct trials are `attempt == 1` (Methods, MNAV: "only
  single-attempt trials are considered correct trials"); error trials are `attempt == 2`, whose
  row holds the first attempt (Methods, MNAV, last sentences). Distance is |ta| / 0.65 (Fig. 1a,
  0.65 s between landmarks). In monkey M, `seqq` 3 trials have vectors in steps of 0.975 s, which
  the paper does not describe; their distance is |ta| / 0.975, and analyses that use distance keep
  `seqq` < 3, as the code's PI selection does (claims, opening comment).
- PI trials (claims, opening comment): first attempt, distance >= 3, |tp| > 1 s, `seqq < 3`;
  each direction (sign of ta) separately; more than 15 trials.
- Rate: 1 ms spike counts smoothed with a Gaussian of SD 100 ms (Methods, Analysis of neural
  data) cut at 1 SD (claims, opening comment, the code's 200 ms kernel); window from joystick
  onset to 500 ms before joystick offset (Methods, PI step 2); each trial linearly detrended
  (step 3).
- ACG: per trial, normalised to 1 at lag 0, lags to 2,400 ms (step 4); trials with mean smoothed
  rate <= 0.05 dropped (claims, code line 3756). The claims file gives no unit for 0.05; it is
  taken here as spikes/s, so that it drops silent trials only (an assumption; at 0.05 spikes/ms,
  50 spikes/s, most trials would be dropped).
- PI(L) = corr(ACG, ACG shifted by L) - corr(ACG, ACG shifted by L/2), circular shifts (claims;
  Methods steps 5 and 7). Lags 0 to 1,300 ms (Methods) or 100 to 1,600 ms (code), 10 ms steps.
- Null (Methods): Gaussian process with squared exponential kernel (variance 1, length 100 ms)
  passed through an inhomogeneous Poisson process and smoothed as the data. A zero-mean GP is not
  a rate; it is turned into one as rate = r * exp(g - 1/2), whose mean is r, the median rate of
  the group's units (an assumption: the Methods do not say how). 1,000 surrogates.
- Classification readings (claims): (a) score = max PI - mean PI from the first positive lag
  on, periodic when it exceeds a threshold from the surrogates; the claims file's wording ("the
  maximum over lags of (mean + 2 SD) of the surrogate scores") is run two ways: (a1) the maximum
  over lags of the surrogate PI mean + 2 SD, (a2) the mean + 2 SD of the surrogate scores; (b) periodic when PI at any lag exceeds the surrogate mean + 2 SD at
  that lag. Surrogate durations: (own) each surrogate averages ACGs over trials with the
  durations of the session and direction's trials; (global) each surrogate averages the median
  number of trials, all at the monkey's median duration.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "000897"
DANDISET_VERSION = "0.240605.1710"

LANDMARK_S = 0.65            # Fig. 1a
SMOOTH_SD_MS = 100           # Methods, Analysis of neural data
SMOOTH_TRUNCATE = 1.0        # claims, the code's kernel cut at 1 SD
OFFSET_CUT_S = 0.5           # Methods, PI step 2
MAX_LAG_MS = 2400            # Methods, PI step 4
MIN_TRIAL_RATE = 0.05        # claims (code line 3756), read as spikes/s (assumption)
MIN_TRIALS = 15              # Methods: "higher than 15"
LAGS_METHODS = np.arange(0, 1301, 10)
LAGS_CODE = np.arange(100, 1601, 10)
GP_LENGTH_MS = 100           # Methods
N_SURROGATES = 1000          # Methods
NFFT = 8192
MAX_TP_S = 5.0


def assets():
    ds = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return sorted([a for a in ds.get_assets() if a.path.endswith("_behavior+ecephys.nwb")],
                  key=lambda a: a.path)


def _open(asset):
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    return h5py.File(remfile.File(url), "r")


def load_session(asset):
    """Trial table, spike times of every unit and unit metadata of one session."""
    f = _open(asset)
    tr = pd.DataFrame({k: f["intervals/trials"][k][:] for k in f["intervals/trials"] if k != "id"})
    u = f["processing/ecephys/units"]
    st = u["spike_times"][:]
    idx = u["spike_times_index"][:]
    starts = np.concatenate([[0], idx[:-1]])
    spikes = [np.sort(st[a:b]) for a, b in zip(starts, idx)]
    meta = pd.DataFrame({"unit_name": [x.decode() if isinstance(x, bytes) else str(x) for x in u["unit_name"][:]]})
    for col in ("quality", "KSLabel"):
        if col in u:
            meta[col] = [x.decode() if isinstance(x, bytes) else str(x) for x in u[col][:]]
    subject = f["general/subject/subject_id"][()]
    subject = subject.decode() if isinstance(subject, bytes) else str(subject)
    session = asset.path.split("ses-")[1].split("_")[0]
    # monkey M's sequence 3 has vectors in steps of 0.975 s (see the notebook's data check)
    spacing = np.where(tr.seqq == 3, 1.5 * LANDMARK_S, LANDMARK_S)
    tr["distance"] = np.round(np.abs(tr.ta) / spacing)
    tr["direction"] = np.sign(tr.ta)
    eye_ts = f["processing/behavior/eye_position/timestamps"]
    hand_ts = f["processing/behavior/hand_position/timestamps"]
    info = {"eye_ts_first": float(eye_ts[0]), "eye_ts_last": float(eye_ts[-1]), "eye_n": eye_ts.shape[0],
            "hand_ts_first": float(hand_ts[0]), "hand_ts_last": float(hand_ts[-1]), "hand_n": hand_ts.shape[0],
            "eye_unit": f["processing/behavior/eye_position/data"].attrs.get("unit"),
            "hand_unit": f["processing/behavior/hand_position/data"].attrs.get("unit")}
    return {"path": asset.path, "subject": subject, "monkey": "A" if subject.startswith("amadeus") else "M",
            "session": session, "trials": tr, "spikes": spikes, "units": meta, "info": info}


def load_all(max_workers=8):
    with ThreadPoolExecutor(max_workers) as ex:
        return list(ex.map(load_session, assets()))


# ---------------------------------------------------------------- rates

def trial_counts(spikes, t0, t1, pad_ms=0):
    """1 ms spike counts for windows [t0, t1) (seconds), padded by pad_ms; rows zero beyond length."""
    t0 = np.asarray(t0, float) - pad_ms / 1000
    t1 = np.asarray(t1, float) + pad_ms / 1000
    n = np.maximum(np.round((t1 - t0) * 1000).astype(int), 0)
    out = np.zeros((len(t0), max(int(n.max()), 1) if len(n) else 1))
    lo = np.searchsorted(spikes, t0)
    hi = np.searchsorted(spikes, t1)
    for i in range(len(t0)):
        b = ((spikes[lo[i]:hi[i]] - t0[i]) * 1000).astype(int)
        b = b[b < n[i]]
        np.add.at(out[i], b, 1)
    return out, n


def smoothed_rates(spikes, t0, t1):
    """Smoothed rate (spikes/s) in 1 ms bins from t0 to t1, as a list of arrays."""
    pad = int(SMOOTH_SD_MS * SMOOTH_TRUNCATE) + 1
    counts, n = trial_counts(spikes, t0, t1, pad_ms=pad)
    sm = gaussian_filter1d(counts, SMOOTH_SD_MS, axis=1, truncate=SMOOTH_TRUNCATE, mode="constant") * 1000
    return [sm[i, pad:n[i] - pad] for i in range(len(n))]


def mean_rate(spikes, t0, t1):
    """Spike count / duration (spikes/s) in [t0, t1)."""
    t0 = np.asarray(t0, float)
    t1 = np.asarray(t1, float)
    return (np.searchsorted(spikes, t1) - np.searchsorted(spikes, t0)) / (t1 - t0)


# ---------------------------------------------------------------- periodicity index

def _detrend(x):
    t = np.arange(len(x))
    if len(x) < 3:
        return x - x.mean()
    p = np.polyfit(t, x, 1)
    return x - np.polyval(p, t)


def mean_acg(rates, min_rate=MIN_TRIAL_RATE):
    """Mean over trials of the detrended single-trial ACG, lags -2400..2400 ms, 1 at lag 0.

    Returns (acg, number of trials kept)."""
    keep = [r for r in rates if len(r) > 10 and r.mean() > min_rate]
    if not keep:
        return None, 0
    X = np.zeros((len(keep), NFFT))
    for i, r in enumerate(keep):
        d = _detrend(r)
        X[i, :len(d)] = d
    F = np.fft.rfft(X, axis=1)
    ac = np.fft.irfft(F * np.conj(F), NFFT, axis=1)
    ac0 = ac[:, :1]
    ok = ac0[:, 0] > 0
    ac = ac[ok] / ac0[ok]
    if len(ac) == 0:
        return None, 0
    pos = ac[:, :MAX_LAG_MS + 1]
    full = np.concatenate([pos[:, :0:-1], pos], axis=1)
    return full.mean(0), len(ac)


def pi_curve(acg, lags):
    """PI at each lag (ms): circular autocorrelation of the ACG at L minus at L/2."""
    a = acg - acg.mean()
    F = np.fft.fft(a)
    rho = np.real(np.fft.ifft(F * np.conj(F))) / np.sum(a * a)
    lags = np.asarray(lags)
    return rho[lags] - rho[lags // 2]


def pi_score(pi):
    """Reading (a): max PI minus mean PI from the first positive lag on."""
    pos = np.nonzero(pi > 0)[0]
    if len(pos) == 0:
        return float(pi.max() - pi.mean())
    return float(pi.max() - pi[pos[0]:].mean())


def gp_surrogate_rates(rng, durations_ms, mean_rate_hz):
    """Surrogate smoothed rates: GP (SE kernel, length 100 ms, variance 1) -> Poisson -> smoothing."""
    out = []
    sig = GP_LENGTH_MS / np.sqrt(2)     # white noise * Gaussian(sd) has SE covariance of length sd*sqrt(2)
    pad = 4 * GP_LENGTH_MS
    for n in durations_ms:
        n = int(n)
        w = rng.standard_normal(n + 2 * pad)
        g = gaussian_filter1d(w, sig, mode="wrap")[pad:pad + n]
        g /= np.sqrt(1 / (2 * np.sqrt(np.pi) * sig))   # unit variance
        lam = mean_rate_hz * np.exp(g - 0.5) / 1000
        counts = rng.poisson(lam).astype(float)
        sm = gaussian_filter1d(counts, SMOOTH_SD_MS, truncate=SMOOTH_TRUNCATE, mode="constant") * 1000
        out.append(sm)
    return out


def surrogate_pis(rng, durations_ms, n_trials, mean_rate_hz, lags, n=N_SURROGATES):
    """n surrogate PI curves; each averages ACGs over n_trials trials drawn from durations_ms."""
    curves = []
    durations_ms = np.asarray(durations_ms)
    for _ in range(n):
        d = rng.choice(durations_ms, size=n_trials, replace=True)
        acg, _k = mean_acg(gp_surrogate_rates(rng, d, mean_rate_hz), min_rate=-1)
        curves.append(pi_curve(acg, lags))
    return np.array(curves)


def pi_trials(tr, direction=None, extra=None, attempt=1):
    """Trials used for the PI (claims, opening comment); attempt=2 gives error trials (first attempt)."""
    m = (tr.trial_type == 3) & (tr.attempt == attempt) & (tr.distance >= 3) & (tr.tp.abs() > 1) & (tr.seqq < 3)
    # productions above MAX_TP_S (error trials only; the longest correct vector is 3.25 s) are
    # left out, so that every trial fits the ACG's FFT length (a standard choice)
    m &= tr.tp.abs() < MAX_TP_S
    if direction is not None:
        m &= tr.direction == direction
    if extra is not None:
        m &= extra
    return tr[m]


def nav_windows(trs):
    """Joystick onset to 500 ms before joystick offset (Methods, PI step 2)."""
    return trs.joy1onttl.values, trs.joy1offttl.values - OFFSET_CUT_S


def surrogate_bank(rng, durations_ms, mean_rate_hz, n):
    """n single-trial surrogate ACGs (lags -2400..2400) with durations drawn from durations_ms.

    Returns (acgs, durations). Used to build surrogate neurons by averaging bank entries, which
    gives the same null as generating each surrogate trial afresh at a fraction of the cost."""
    d = rng.choice(np.asarray(durations_ms), size=n, replace=True)
    rates = gp_surrogate_rates(rng, d, mean_rate_hz)
    acgs, kept = [], []
    for r, dur in zip(rates, d):
        a, _k = mean_acg([r], min_rate=-1)
        if a is not None:        # a surrogate trial without spikes has no ACG
            acgs.append(a)
            kept.append(dur)
    return np.array(acgs), np.array(kept)


def null_from_bank(rng, bank, bank_durations, target_durations, lags, n=N_SURROGATES):
    """Surrogate PI curves: each averages one bank ACG per target duration (nearest duration)."""
    order = np.argsort(bank_durations)
    sd = bank_durations[order]
    pos = np.clip(np.searchsorted(sd, np.asarray(target_durations)), 0, len(sd) - 1)
    curves = []
    for _ in range(n):
        # nearest-duration neighbourhood of 20 bank entries for each target trial
        jitter = rng.integers(-10, 10, size=len(pos))
        pick = order[np.clip(pos + jitter, 0, len(sd) - 1)]
        curves.append(pi_curve(bank[pick].mean(0), lags))
    return np.array(curves)


def periodicity_table(sessions, extra=None, lag_sets=None, attempt=1):
    """PI curve of every unit, per direction, on the PI trials (optionally restricted by `extra`,
    a function of the trial table returning a boolean mask)."""
    lag_sets = lag_sets or {"methods": LAGS_METHODS, "code": LAGS_CODE}
    rows = []
    for s in sessions:
        tr = s["trials"]
        for d in (1, -1):
            trs = pi_trials(tr, d, None if extra is None else extra(tr), attempt=attempt)
            t0, t1 = nav_windows(trs)
            for u, sp in enumerate(s["spikes"]):
                label = s["units"].get("quality", s["units"].get("KSLabel"))
                row = {"monkey": s["monkey"], "session": s["session"], "unit": u, "direction": d,
                       "label": label.iloc[u],
                       "n_trials": len(trs), "durations": np.round((t1 - t0) * 1000)}
                acg, k = mean_acg(smoothed_rates(sp, t0, t1)) if len(trs) else (None, 0)
                row["k"] = k
                for name, lags in lag_sets.items():
                    row["pi_" + name] = None if acg is None else pi_curve(acg, lags)
                rows.append(row)
    return pd.DataFrame(rows)
