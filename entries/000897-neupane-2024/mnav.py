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
  the group's units (an assumption: the Methods do not say how). 1,000 surrogates. The code's
  variant (claims) has no Poisson step: the GP around the mean rate, smoothed as the data.
  Surrogate neurons are built by averaging single-trial surrogate ACGs drawn at random from a bank
  (null_from_bank); the notebook compares one group's bank null with a null generated afresh.
- Classification readings (claims): (a) score = max PI - mean PI from the first positive lag
  on, periodic when it exceeds a threshold from the surrogates; the claims file's wording ("the
  maximum over lags of (mean + 2 SD) of the surrogate scores") is run two ways: (a1) the maximum
  over lags of the surrogate PI mean + 2 SD, (a2) the mean + 2 SD of the surrogate scores; (b) periodic when PI at any lag exceeds the surrogate mean + 2 SD at
  that lag. Surrogate durations: (own) each surrogate averages as many trials as the unit keeps
  (k, matched to a grid in steps of 25%, k_levels), with durations drawn from the session and
  direction's trials; (global) each surrogate averages the monkey's median k trials, all at its
  median duration.
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


def pi_scores(pis):
    """pi_score of each row of pis (curves x lags)."""
    pis = np.asarray(pis)
    pos = pis > 0
    first = np.where(pos.any(1), pos.argmax(1), 0)
    suffix = np.cumsum(pis[:, ::-1], axis=1)[:, ::-1]
    n = pis.shape[1] - first
    return pis.max(1) - suffix[np.arange(len(pis)), first] / n


def gp_surrogate_rates(rng, durations_ms, mean_rate_hz, poisson=True):
    """Surrogate smoothed rates: GP (SE kernel, length 100 ms, variance 1) -> Poisson -> smoothing.

    poisson=False is the code's get_gpfr variant (claims, opening comment): the GP around the mean
    rate, without the Poisson step, smoothed as the data (that it is smoothed is an assumption).
    Its ACG does not depend on the rate, as each trial is detrended and normalised."""
    out = []
    sig = GP_LENGTH_MS / np.sqrt(2)     # white noise * Gaussian(sd) has SE covariance of length sd*sqrt(2)
    pad = 4 * GP_LENGTH_MS
    for n in durations_ms:
        n = int(n)
        w = rng.standard_normal(n + 2 * pad)
        g = gaussian_filter1d(w, sig, mode="wrap")[pad:pad + n]
        g /= np.sqrt(1 / (2 * np.sqrt(np.pi) * sig))   # unit variance
        if poisson:
            lam = mean_rate_hz * np.exp(g - 0.5) / 1000
            x = rng.poisson(lam).astype(float)
        else:
            x = (mean_rate_hz + g) / 1000
        sm = gaussian_filter1d(x, SMOOTH_SD_MS, truncate=SMOOTH_TRUNCATE, mode="constant") * 1000
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


def pi_curves(acgs, lag_sets):
    """pi_curve for each row of acgs (surrogates x lags), for each lag set: {name: array}."""
    a = acgs - acgs.mean(1, keepdims=True)
    F = np.fft.fft(a, axis=1)
    rho = np.real(np.fft.ifft(F * np.conj(F), axis=1)) / np.sum(a * a, axis=1, keepdims=True)
    return {name: rho[:, lags] - rho[:, np.asarray(lags) // 2] for name, lags in lag_sets.items()}


def surrogate_bank(rng, durations_ms, mean_rate_hz, n, poisson=True):
    """n single-trial surrogate ACGs (lags -2400..2400) with durations drawn from durations_ms.

    Returns (acgs, durations). Used to build surrogate neurons by averaging bank entries drawn at
    random, which approximates generating each surrogate trial afresh at a fraction of the cost
    (the notebook compares the two for one group)."""
    d = rng.choice(np.asarray(durations_ms), size=n, replace=True)
    rates = gp_surrogate_rates(rng, d, mean_rate_hz, poisson=poisson)
    acgs, kept = [], []
    for r, dur in zip(rates, d):
        a, _k = mean_acg([r], min_rate=-1)
        if a is not None:        # a surrogate trial without spikes has no ACG
            acgs.append(a.astype(np.float32))
            kept.append(dur)
    return np.array(acgs), np.array(kept)


def null_from_bank(rng, bank, bank_durations, target_durations, n_trials, lag_sets, n=N_SURROGATES,
                   width=200):
    """Surrogate PI curves {lag set: n x lags}. Each surrogate neuron averages n_trials bank ACGs:
    for each trial a duration is drawn from target_durations, and a bank entry is drawn at random
    among the `width` entries nearest in duration (all entries when the bank has fewer)."""
    from scipy import sparse
    order = np.argsort(bank_durations)
    sd = bank_durations[order]
    nb = len(sd)
    width = min(width, nb)
    d = rng.choice(np.asarray(target_durations), size=(n, n_trials), replace=True)
    pos = np.searchsorted(sd, d)
    lo = np.clip(pos - width // 2, 0, nb - width)
    pick = order[lo + rng.integers(0, width, size=lo.shape)]
    W = sparse.csr_matrix((np.full(pick.size, 1.0 / n_trials), (np.repeat(np.arange(n), n_trials), pick.ravel())),
                          shape=(n, nb))
    return pi_curves(np.asarray(W @ bank, dtype=float), lag_sets)


def k_levels(k_values, ratio=1.25, low=MIN_TRIALS + 1):
    """Geometric grid of trial counts used to match a null to each unit's number of kept trials;
    returns (levels, level of each k: the nearest level on a log scale)."""
    k_values = np.asarray(k_values)
    top = max(int(k_values.max()), low)
    levels = np.unique(np.round(low * ratio ** np.arange(0, 1 + np.ceil(np.log(top / low) / np.log(ratio)))).astype(int))
    idx = np.abs(np.log(k_values[:, None] / levels[None, :])).argmin(1)
    return levels, levels[idx]


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


# ---------------------------------------------------------------- behaviour clock

def behaviour_clock_offset(ts, x, trials, bin_s=0.01, rest_v=1.0):
    """Offset (s) of the joystick trace's clock against the trial table's, by cross-correlating the
    time the trace is deflected (|x - median| > rest_v volts, 10 ms bins) with the time between
    joy1onttl and joy1offttl of the MNAV trials. Trace time = trial time + offset. Returns
    (offset, peak height in SD of the cross-correlation, highest value more than 2 s from the peak
    as a fraction of the peak). An estimate made here; the files do not give the offset."""
    rest = np.median(x)
    nx = int(np.ceil((ts[-1] - ts[0]) / bin_s)) + 1
    ix = ((ts - ts[0]) / bin_s).astype(np.int64)
    xs = np.bincount(ix, weights=(np.abs(x - rest) > rest_v).astype(float), minlength=nx)
    xs = xs / np.maximum(np.bincount(ix, minlength=nx), 1)
    g = trials[(trials.trial_type == 3) & (trials.tp.abs() < 99)]
    ny = int(np.ceil(trials.stop_time.max() / bin_s)) + 1
    y = np.zeros(ny)
    for a, b in zip((g.joy1onttl.values / bin_s).astype(int), (g.joy1offttl.values / bin_s).astype(int)):
        y[a:b] = 1
    xs, y = xs - xs.mean(), y - y.mean()
    n = 1 << int(np.ceil(np.log2(nx + ny)))
    cc = np.fft.irfft(np.fft.rfft(xs, n) * np.conj(np.fft.rfft(y, n)), n)   # cc[k] = sum_t xs[t + k] y[t]
    k = int(np.argmax(cc))
    far = np.abs(((np.arange(n) - k + n // 2) % n) - n // 2) > 2 / bin_s
    second = float(cc[far].max() / cc[k])
    if k > n // 2:
        k -= n
    return ts[0] + k * bin_s, float((cc[k % n] - np.median(cc)) / cc.std()), second


# ---------------------------------------------------------------- Bayesian observer models (fig4g)

PRIOR_C, PRIOR_M = 0.5846, -0.1026    # claims and the code's fbls: prior density c + m t on 0.65..3.25 s
_T_GRID = np.linspace(0.65, 3.25, 261)
_PRIOR = PRIOR_C + PRIOR_M * _T_GRID


def bls_estimator(wm, tm, reset):
    """Bayes least squares estimate E[t | tm] for measurements tm; measurement noise SD wm * t (no
    reset) or wm * sqrt(t) (reset), as in the code's models 2 and 1."""
    sd = wm * (np.sqrt(_T_GRID) if reset else _T_GRID)
    lik = np.exp(-0.5 * ((tm[:, None] - _T_GRID[None, :]) / sd) ** 2) / sd
    post = lik * _PRIOR
    return (post * _T_GRID).sum(1) / np.maximum(post.sum(1), 1e-300)


def bls_predict(params, ts, reset, n_tm=121):
    """For each interval in ts: (weights over tm, te(tm), production SD(tm)) of the observer.
    Production noise SD = wp * te (no reset, scalar) or wp * sqrt(te) (reset, Methods); the code's
    reset model (utilities/bls_offset_counter_nonuniformPrior_self.m) also scales the measurement
    noise with sqrt(t)."""
    wm, wp, b = abs(params[0]), abs(params[1]), params[2]
    out = []
    for t in ts:
        tm = t + wm * (np.sqrt(t) if reset else t) * np.linspace(-4, 4, n_tm)
        w = np.exp(-0.5 * np.linspace(-4, 4, n_tm) ** 2)
        w /= w.sum()
        te = bls_estimator(wm, tm, reset)
        sd = wp * (np.sqrt(te) if reset else te)
        out.append((w, te + b, np.maximum(sd, 1e-6)))
    return out


def bls_negloglik(params, ta, tp, reset):
    """Negative log-likelihood of produced intervals tp (s) given actual intervals ta (s)."""
    if abs(params[0]) < 1e-3 or abs(params[1]) < 1e-3:
        return np.inf
    ts = np.unique(ta)
    nll = 0.0
    for t, (w, mu, sd) in zip(ts, bls_predict(params, ts, reset)):
        x = tp[ta == t]
        dens = (w[None, :] * np.exp(-0.5 * ((x[:, None] - mu[None, :]) / sd[None, :]) ** 2) / (np.sqrt(2 * np.pi) * sd[None, :])).sum(1)
        nll -= np.sum(np.log(np.maximum(dens, 1e-300)))
    return nll


def bls_fit(ta, tp, reset):
    """Maximum likelihood fit (Nelder-Mead from [0.5, 0.5, 0], as the code's fminsearch)."""
    from scipy.optimize import minimize
    res = minimize(bls_negloglik, [0.5, 0.5, 0.0], args=(ta, tp, reset), method="Nelder-Mead",
                   options={"maxiter": 2000, "xatol": 1e-4, "fatol": 1e-4})
    return res


def bls_bias_var(params, ts, reset):
    """Model bias (E[tp] - t) and variance of tp at each interval."""
    bias, var = [], []
    for t, (w, mu, sd) in zip(ts, bls_predict(params, ts, reset)):
        m = np.sum(w * mu)
        bias.append(m - t)
        var.append(np.sum(w * (sd ** 2 + (mu - m) ** 2)))
    return np.array(bias), np.array(var)


def lapse_mask(ta, tp, n_iter=50):
    """Methods (Bayesian model): per interval, a mixture of a Gaussian and a uniform lapse
    distribution on 0 to 3 times the interval (the Methods' "0 to 3 v_p" read as 3 times the
    actual vector, an assumption), fit by EM; True for trials more likely Gaussian."""
    keep = np.ones(len(tp), bool)
    for t in np.unique(ta):
        i = np.nonzero(ta == t)[0]
        x = tp[i]
        mu, sd, pi_ = np.median(x), max(np.std(x), 1e-3), 0.9
        u = 1 / (3 * t)
        for _ in range(n_iter):
            g = pi_ * np.exp(-0.5 * ((x - mu) / sd) ** 2) / (np.sqrt(2 * np.pi) * sd)
            l_ = (1 - pi_) * u * ((x >= 0) & (x <= 3 * t))
            r = g / np.maximum(g + l_, 1e-300)
            pi_ = r.mean()
            mu = np.sum(r * x) / r.sum()
            sd = max(np.sqrt(np.sum(r * (x - mu) ** 2) / r.sum()), 1e-3)
        keep[i] = r >= 0.5
    return keep


# ---------------------------------------------------------------- CAN model (fig4d)
# A port of the paper's code (gc_CAN_model_simulation.m, utilities/gc1d_setup.m, gc1d_init.m and
# gc1d_run.m at commit 4bee109): two rings of 364 units with a centre-surround profile, shifted
# connections for the two directions, global drive 100, velocity gain 1, dt 0.5 ms, synaptic time
# constant 40 ms, ReLU; internal landmarks at network states 60 to 300 in steps of 60, each an
# input of Gaussians (SD 5 units, centred 3 units past each landmark state) whose amplitude rises
# and decays (50 exp(-(t - t_k - 500)^2 / (2 * 1500^2)), t in steps) after the network state
# crosses landmark k. Simulations are batched as columns; with constant velocity per simulation
# the dynamics are deterministic given the velocity.

CAN_N = 364
CAN_DT, CAN_TAU = 1 / 2000, 40 / 1000


def can_setup(N=CAN_N):
    z = np.arange(-N // 2, N // 2)
    mex = 1000 * np.exp(-1.05 / 100 * z ** 2) - 1000 * np.exp(-1.00 / 100 * z ** 2)
    mex = np.roll(mex, N // 2 - 1)
    W_RR = np.stack([np.roll(mex, i) for i in range(N)])
    W_LL = np.stack([np.roll(mex, i + 2) for i in range(N)])
    W_X = np.stack([np.roll(mex, i + 1) for i in range(N)])
    return np.block([[W_LL, W_X], [W_X, W_RR]])          # state vector [left ring; right ring]


def can_init(W, rng, N=CAN_N):
    """gc1d_init: 10 s with a weak landmark at unit 0 (SD 30, gain 3) and velocity 0.01 * randn."""
    v = 0.01 * rng.standard_normal()
    x = np.arange(1, N + 1)
    lm = np.exp(-x ** 2 / (2 * 30 ** 2))
    lm = 3 * lm / lm.max()
    vv = np.r_[np.full(N, 1 - v), np.full(N, 1 + v)]
    s = np.zeros(2 * N)
    lm2 = np.r_[lm, lm]
    for _ in range(int(10 / CAN_DT) - 1):
        s = s + (np.maximum(vv * (W @ s + 100) + lm2, 0) - s) * CAN_DT / CAN_TAU
    return s


def can_run(W, s0, v, landmarks, lm_loc=(60, 120, 180, 240, 300), start=30, end=360, N=CAN_N,
            max_steps=200000):
    """gc1d_run for each velocity in v (with landmarks where `landmarks` is True). Returns the
    network state (steps x simulations); a finished simulation keeps its last state."""
    v = np.asarray(v, float)
    landmarks = np.asarray(landmarks, bool)
    K = len(v)
    lm_loc = np.asarray(lm_loc)
    s = np.repeat(s0[:, None], K, axis=1)
    vv = np.r_[np.repeat((1 - v)[None, :], N, 0), np.repeat((1 + v)[None, :], N, 0)]
    shape = np.exp(-(np.arange(1, N + 1)[:, None] - (lm_loc + 3)[None, :]) ** 2 / (2 * 5 ** 2)).sum(1)
    state = np.full(K, start, int)
    t_cross = np.full((K, len(lm_loc)), -1)
    done = np.zeros(K, bool)
    idx = np.arange(N)
    cols = np.arange(K)
    traj = [state.copy()]
    t = 1
    while not done.all() and t < max_steps:
        t += 1
        k = (state[:, None] >= lm_loc[None, :]).sum(1)        # landmarks passed
        last = np.maximum(k - 1, 0)
        newly = (k > 0) & (t_cross[cols, last] < 0)
        t_cross[cols[newly], last[newly]] = t
        amp = np.where((k > 0) & landmarks, 50 * np.exp(-(t - t_cross[cols, last] - 500) ** 2 / (2 * 1500 ** 2)), 0.0)
        lmi = shape[:, None] * amp[None, :]
        s = s + (np.maximum(vv * (W @ s + 100) + np.r_[lmi, lmi], 0) - s) * CAN_DT / CAN_TAU
        zL = s[:N]
        # the first local maximum of the left ring from 10 units before the current state on
        pk = np.zeros_like(zL, bool)
        pk[1:-1] = (zL[1:-1] > zL[:-2]) & (zL[1:-1] >= zL[2:])
        first = np.argmax(pk & (idx[:, None] >= (state - 10)[None, :]), axis=0)
        state = np.where(done, state, first + 1)
        traj.append(state.copy())
        done |= state >= end
    return np.array(traj)


def first_reach(traj, state):
    """Step (1-based) at which each simulation first reaches `state`, NaN if never."""
    ok = traj >= state
    return np.where(ok.any(0), ok.argmax(0) + 1.0, np.nan)
