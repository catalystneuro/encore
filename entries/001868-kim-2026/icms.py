"""Loading and measures for DANDI:001868 (Kim, Lycke et al. 2026, Science Advances, eaef0343).

Every NWB file is streamed from the DANDI archive at the pinned version (remfile + h5py); nothing is
written to disk. Where each parameter comes from is said next to it:

- "claims, common method" is the method block at the top of claims/001868/10.1126-sciadv.aef0343.yaml,
  which cites the paper's Methods and its code (XieLuanLab/icms-activation-plasticity at d1922d1);
- "Methods, <section>" is a passage of the paper (paper/10.1126-sciadv.aef0343.txt) taken by the author
  (protocol, author step 1.6);
- "assumption" is a choice the paper leaves open, stated as such;
- "standard choice" is a detail that cannot change an outcome.
"""
from __future__ import annotations

import math
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy import stats
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import minimize

DANDISET = "001868"
VERSION = "0.260715.2016"  # the only published version (see the notebook header)
API = "https://api.dandiarchive.org/api"

# Paper names (Methods; claims file opening comment): Mouse 1 to 6.
MOUSE = {"ICMS92": "Mouse 1", "ICMS93": "Mouse 2", "ICMS98": "Mouse 3",
         "ICMS100": "Mouse 4", "ICMS101": "Mouse 5", "ICMS83": "Mouse 6"}
BEHAVIOUR = list(MOUSE)
CURRENTS = (4.0, 5.0, 6.0)  # claims, common method (Methods, Analysis of behavioral data)
EARLY_WEEKS = (0, 1)        # claims, common method
LATE_WEEKS = (2, 3, 4)

TRAIN_S = 0.7    # 700 ms train of 70 pulses at 100 Hz (Methods; dataset table description)
IPI_S = 0.010    # interpulse interval


# --------------------------------------------------------------------------------------- access
def list_assets():
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/",
                     params={"page_size": 400}, timeout=60)
    r.raise_for_status()
    return r.json()["results"]


def open_asset(asset_id):
    return h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/"), "r")


def _table(g, cols=None):
    cols = cols or [c for c in g.attrs["colnames"]]
    out = {}
    for c in cols:
        if c not in g:
            continue
        v = g[c][()]
        if v.dtype.kind in "OS":
            v = v.astype(str)
        out[c] = v
    return out


def load_session(asset, wheel=True):
    """Reduce one behavioural session to what the analyses use."""
    f = open_asset(asset["asset_id"])
    s = {"path": asset["path"], "subject": f["general/subject/subject_id"][()].decode(),
         "sex": f["general/subject/sex"][()].decode(),
         "date": f["session_start_time"][()].decode()[:10]}
    el = f["general/extracellular_ephys/electrodes"]
    s["el_channel"] = el["channel_name"][()].astype(str).astype(int)
    s["el_y"] = el["rel_y"][()]
    u = f["units"]
    st = u["spike_times"][()]
    idx = u["spike_times_index"][()]
    s["spikes"] = np.split(st, idx[:-1])
    s["cell_type"] = u["cell_type"][()].astype(str)
    s["unit_y"] = u["unit_y_um"][()] if "unit_y_um" in u else np.full(len(idx), np.nan)
    s["peak_ch"] = u["peak_channel_index"][()]
    s["accepted"] = u["accepted"][()]
    s["waveform"] = u["waveform_mean"][()]
    s["unit_ids"] = u["id"][()]
    s["trials"] = _table(f["intervals/trials"])
    s["stim"] = _table(f["intervals/electrical_stimulation"])
    s["ephys_end"] = float(st.max()) if len(st) else 0.0
    if wheel and "processing/behavior/wheel/wheel_position_processed" in f:
        w = f["processing/behavior/wheel/wheel_position_processed"]
        s["wheel"] = w["data"][()].astype(np.float64)
        s["wheel_rate"] = float(w["starting_time"].attrs["rate"])
        s["wheel_t0"] = float(w["starting_time"][()])
    f.close()
    return s


def load_behaviour_sessions(threads=8, wheel=True):
    assets = [a for a in list_assets() if "behavior" in a["path"]]
    with ThreadPoolExecutor(threads) as ex:
        sessions = list(ex.map(lambda a: load_session(a, wheel), assets))
    sessions.sort(key=lambda s: (s["subject"], s["date"]))
    add_weeks(sessions)
    return sessions


def add_weeks(sessions):
    """Week = ceil(days since the animal's first session / 7), day 0 being week 0 (claims, common
    method, from the paper's code)."""
    first = {}
    for s in sessions:
        d = np.datetime64(s["date"])
        first[s["subject"]] = min(first.get(s["subject"], d), d)
    for s in sessions:
        days = int((np.datetime64(s["date"]) - first[s["subject"]]) / np.timedelta64(1, "D"))
        s["day"] = days
        s["week"] = int(math.ceil(days / 7))
        s["phase"] = "early" if s["week"] in EARLY_WEEKS else ("late" if s["week"] in LATE_WEEKS else None)


def ephys_trains(s):
    """The 700 ms, 70-pulse trains recorded with electrophysiology. The planar-imaging block has
    longer trains outside the electrophysiology recording (dataset table; checked in the notebook)."""
    st = s["stim"]
    keep = (st["pulse_count"] == 70) & (st["stop_time"] < s["ephys_end"])
    return {k: v[keep] for k, v in st.items()}


# ----------------------------------------------------------------------------------- behaviour
def _psi(x, mu, sigma, g, l):
    return g + (1 - g - l) * stats.norm.cdf((x - mu) / sigma)


def fit_cumulative_gaussian(currents, n_hit, n_tot):
    """Cumulative Gaussian with free guess and lapse, fitted by maximum likelihood (claims,
    fig2a-threshold-decrease: psignifit 'norm', YesNo, free guess and lapse). psignifit is
    Bayesian; here the guess and lapse are bounded to [0, 0.5] as psignifit's default priors are,
    and the threshold (mu) to [0, 30] uA. Returns mu (threshold at 50% of the unscaled sigmoid,
    psignifit's default) and the current at which the full function reaches 0.5."""
    x = np.asarray(currents, float)
    k = np.asarray(n_hit, float)
    n = np.asarray(n_tot, float)

    def nll(p):
        mu, ls, g, l = p
        q = np.clip(_psi(x, mu, np.exp(ls), g, l), 1e-9, 1 - 1e-9)
        return -np.sum(k * np.log(q) + (n - k) * np.log(1 - q))

    best = None
    for mu0 in np.linspace(max(x.min(), 0.5), x.max() + 1, 5):
        for ls0 in (np.log(0.5), np.log(2.0)):
            r = minimize(nll, [mu0, ls0, 0.02, 0.05], method="L-BFGS-B",
                         bounds=[(0, 30), (np.log(0.05), np.log(20)), (0, 0.5), (0, 0.5)])
            if best is None or r.fun < best.fun:
                best = r
    mu, ls, g, l = best.x
    sig = np.exp(ls)
    # current where psi = 0.5 (the full function)
    frac = (0.5 - g) / max(1 - g - l, 1e-9)
    x50 = mu + sig * stats.norm.ppf(frac) if 0 < frac < 1 else np.nan
    return {"mu": mu, "sigma": sig, "guess": g, "lapse": l, "x50": x50}


def fit_psignifit(currents, n_hit, n_tot, grid_steps=None):
    """psignifit 4 (Python port of the MATLAB toolbox the paper's code calls), sigmoid 'norm',
    experiment type yes/no, so guess and lapse are free (claims fig2a-threshold-decrease), at
    psignifit's default grid unless `grid_steps` is given. Returns the two thresholds the fit
    defines: `ps_x50`, the current at which the fitted (scaled) function reaches 0.5, which is
    what the paper's code takes (processing/dataloader.py, get_block_detection_threshold:
    ps.getThreshold(result, 0.5), whose default is the scaled function) and what the claim's
    criterion names ("the current at 50% detection of the fitted function"); and
    `ps_threshold`, psignifit's own threshold parameter, the midpoint of the unscaled sigmoid."""
    import psignifit as ps
    data = np.column_stack([currents, n_hit, n_tot]).astype(float)
    kw = {} if grid_steps is None else {"grid_steps": grid_steps}
    r = ps.psignifit(data, sigmoid="norm", experiment_type="yes/no", **kw)
    e = r.parameter_estimate
    x50 = float(r.threshold(0.5, unscaled=False, return_ci=False))
    return {"ps_x50": x50 if np.isfinite(x50) else np.nan, "ps_threshold": float(e["threshold"]),
            "ps_width": float(e["width"]), "ps_guess": float(e["gamma"]), "ps_lapse": float(e["lambda"])}


def block_data(s):
    """Per channel and block, (currents, hits, totals) with the block's catch trials as a 0 uA
    point (Methods, Analysis of behavioral data: four blocks of 100 trials, each with 10 catch
    trials). Blocks are the 100-trial groups of the volumetric blocks; the fifth (planar) block is
    left out, as the Methods count four."""
    T = s["trials"]
    vol = np.ones(len(T["trial_index"]), bool)
    if "imaging_modality" in T:
        vol = T["imaging_modality"] == "volumetric"
    order = np.argsort(T["trial_index"])
    pos = np.empty(len(order), int)
    pos[order] = np.arange(len(order))
    block = pos // 100
    out = []
    for b in np.unique(block[vol]):
        m = vol & (block == b)
        cur, ch, hit = T["current_uA"][m], T["stim_channel"][m], T["is_hit"][m]
        catch = cur == 0
        fa_n, fa_k = catch.sum(), hit[catch].sum()
        for c in np.unique(ch[~catch]):
            mc = (ch == c) & ~catch
            xs, ks, ns = [], [], []
            if fa_n:
                xs.append(0.0); ks.append(int(fa_k)); ns.append(int(fa_n))
            for i in np.unique(cur[mc]):
                mi = mc & (cur == i)
                xs.append(float(i)); ks.append(int(hit[mi].sum())); ns.append(int(mi.sum()))
            if len(xs) < 3:
                continue
            out.append({"block": int(b), "channel": int(c), "n_currents": len(xs) - (1 if fa_n else 0),
                        "has_catch": bool(fa_n), "x": xs, "k": ks, "n": ns})
    return out


def fit_block(d):
    """Both fits for one block: psignifit (main) and the bounded maximum likelihood fit (variant)."""
    return {**{k: d[k] for k in ("block", "channel", "n_currents", "has_catch")},
            **fit_psignifit(d["x"], d["k"], d["n"]), **fit_cumulative_gaussian(d["x"], d["k"], d["n"])}


def wheel_displacement(s, onsets, t_before=0.0, t_after=1.0):
    """Wheel position minus its value at each onset, sampled at the processed 1000 Hz rate."""
    w, r, t0 = s["wheel"], s["wheel_rate"], s["wheel_t0"]
    n_after = int(round(t_after * r))
    out = np.full((len(onsets), n_after), np.nan)
    for i, t in enumerate(onsets):
        a = int(round((t - t0) * r))
        if a < 0 or a + n_after > len(w):
            continue
        out[i] = w[a:a + n_after] - w[a]
    return out


def movement_onset(disp, thr, rate=1000.0, sustain_s=0.050):
    """First time |displacement| exceeds 50% of the response threshold and stays above it for
    50 ms (fig. S5 legend; sustain from the code, claims figs5c-wheel-onset-decrease)."""
    above = np.abs(disp) > 0.5 * thr
    k = int(round(sustain_s * rate))
    on = np.full(disp.shape[0], np.nan)
    for i, a in enumerate(above):
        if np.isnan(disp[i]).all():
            continue
        run = np.convolve(a.astype(int), np.ones(k, int), "valid") == k
        j = np.flatnonzero(run)
        if len(j):
            on[i] = j[0] / rate
    return on


# ---------------------------------------------------------------------------------- ephys measures
def counts_in(spk, starts, a, b):
    """Spike counts in [start + a, start + b) for each start."""
    lo = np.searchsorted(spk, starts + a)
    hi = np.searchsorted(spk, starts + b)
    return hi - lo


def time_to_max(spk, starts, window=TRAIN_S, bin_s=0.010, sigma_s=0.020):
    """Argmax over the window of the trial-averaged rate in `bin_s` bins smoothed by a Gaussian of
    `sigma_s` (claims, common method, from the code: 10 ms and 20 ms; 2 ms and 5 ms for 120 ms)."""
    nb = int(round(window / bin_s))
    h = np.zeros(nb)
    for t in starts:
        a, b = np.searchsorted(spk, [t, t + window])
        if b > a:
            h += np.histogram(spk[a:b] - t, bins=nb, range=(0, window))[0]
    if h.sum() == 0:
        return np.nan
    sm = gaussian_filter1d(h / len(starts) / bin_s, sigma_s / bin_s, mode="nearest")
    return (np.argmax(sm) + 0.5) * bin_s * 1000.0  # ms, bin centre


PL_BIN_MS = 0.5         # 0.5 ms bins in each interpulse interval (Methods)
PL_POST_BLANK_MS = 1.5  # first 1.5 ms after each pulse blanked (Methods)
PL_PRE_BLANK_MS = 0.5   # last 0.5 ms before the next pulse blanked (Methods)


def pulse_starts(train_starts, n_pulses=70, ipi_s=IPI_S):
    """Onset of every pulse, from the train onsets and the nominal interpulse interval. The files
    give train onsets only; the trains are 70 pulses at 100 Hz (table description), so pulse k is
    taken at onset + k x 10 ms (assumption; checked against the stored train durations in the
    notebook)."""
    t = np.asarray(train_starts, float)
    return (t[:, None] + np.arange(n_pulses)[None, :] * ipi_s).ravel()


def pulse_matrix(spk, pulses, win_ms=10.0):
    """Spikes per 0.5 ms bin in the `win_ms` after each pulse: shape (pulses, win_ms / 0.5)."""
    nb = int(round(win_ms / PL_BIN_MS))
    M = np.zeros((len(pulses), nb), np.int32)
    lo = np.searchsorted(spk, pulses)
    hi = np.searchsorted(spk, pulses + win_ms / 1000.0)
    for i in np.flatnonzero(hi > lo):
        b = np.floor((spk[lo[i]:hi[i]] - pulses[i]) * 1000.0 / PL_BIN_MS).astype(int)
        b = b[(b >= 0) & (b < nb)]
        np.add.at(M[i], b, 1)
    return M


def _pli_code(v):
    """PLI of the code's calculate_pulse_locked_index: mean of the 3 values around the peak (the
    first or last 3 at an edge) minus the median, over the unblanked values `v`."""
    j = int(np.argmax(v))
    if j == 0:
        top = v[0:3]
    elif j == len(v) - 1:
        top = v[-3:]
    else:
        top = v[j - 1:j + 2]
    return float(np.mean(top) - np.median(v))


def pulse_locking(M, rng, win_ms=10.0, n_boot=500, frac=0.2, n_null=100):
    """Pulse-locking as the paper's code computes it (processing/batch_process/postprocessing/
    responses_v2/pulse_locked_response_metrics.py at d1922d1, called from responses_v3/
    stim_condition_response.py; claims, common method). `M` is the pulse matrix of one response.

    - Spike probability: spikes per 0.5 ms bin over the pulses drawn, bins centred before 1.5 ms or
      after win - 0.5 ms set to 0, and two points inserted at 1.5 ms (a 0 and a copy of the first
      unblanked bin), as get_spike_prob_distribution does.
    - 500 draws of 20% of the pulses without replacement (get_bootstrapped_metrics); the PLI is
      taken on their mean curve over the values centred from 1.5 to win - 0.5 ms (which include
      the two inserted points); latency is the mean over draws of the bin centre of the curve's
      maximum and jitter the variance of those times (ms^2).
    - Null (get_null_distribution): 100 times, the spikes of one draw of 20% of the pulses are
      placed uniformly at random from 1.5 to win - 0.5 ms and divided by the number of pulses
      drawn; PL when the PLI exceeds the 99th percentile of the null PLIs."""
    nb = M.shape[1]
    c = (np.arange(nb) + 0.5) * PL_BIN_MS
    valid = (c >= PL_POST_BLANK_MS) & (c <= nb * PL_BIN_MS - PL_PRE_BLANK_MS)
    Mv = M * valid
    n = M.shape[0]
    k = max(int(n * frac), 1)
    i3 = int(np.searchsorted(c, PL_POST_BLANK_MS))
    cf = np.concatenate([c[:i3], [PL_POST_BLANK_MS, PL_POST_BLANK_MS], c[i3:]])
    vf = (cf >= PL_POST_BLANK_MS) & (cf <= nb * PL_BIN_MS - PL_PRE_BLANK_MS)
    sel = np.zeros((n_boot, n), np.float32)
    for i in range(n_boot):
        sel[i, rng.choice(n, k, replace=False)] = 1.0
    probs = (sel @ Mv.astype(np.float32)) / k
    curves = np.concatenate([probs[:, :i3], np.zeros((n_boot, 1)), probs[:, i3:i3 + 1], probs[:, i3:]], axis=1)
    lat = cf[np.argmax(curves, axis=1)]
    mean_curve = curves.mean(0)
    pli = _pli_code(mean_curve[vf])
    nvalid = int(valid.sum())
    first = int(np.flatnonzero(valid)[0])
    null = np.empty(n_null)
    for i in range(n_null):
        ns = int(Mv[rng.choice(n, k, replace=False)].sum())
        h = np.zeros(nb)
        h[first:first + nvalid] = np.bincount(rng.integers(0, nvalid, ns), minlength=nvalid) / k
        null[i] = _pli_code(h[valid])
    peak_bin = int(np.argmax(mean_curve[vf]))
    return {"pli": pli, "pl": bool(pli > np.percentile(null, 99)),
            "peak_prob": float(mean_curve.max()), "latency_ms": float(lat.mean()),
            "jitter_ms2": float(lat.var()), "peak_ms": float(cf[vf][peak_bin]),
            "n_pl_spikes": int(Mv.sum())}


def response_table(sessions, rng_seed=0, currents=None, window=TRAIN_S, tmax_bin=0.010,
                   tmax_sigma=0.020, with_pl=True, with_trials=False):
    """One row per session x unit x stimulation channel x current (claims, common method).

    Spike counts per trial in [0, window) after train onset and in [-window, 0) before it.
    Modulation score (z) = (mean stimulation rate - mean prestimulus rate) / STD of the per-trial
    prestimulus rates (Methods, Quantifying neuromodulation metrics). The paired t test and the
    filters are applied by `modulated`."""
    rng = np.random.default_rng(rng_seed)
    rows = []
    for si, s in enumerate(sessions):
        tr = ephys_trains(s)
        Tt = s["trials"]
        hit_of = dict(zip(Tt["trial_index"], Tt["is_hit"]))
        for c in np.unique(tr["stim_channel"]):
            for cur in np.unique(tr["current_uA"][tr["stim_channel"] == c]):
                if currents is not None and cur not in currents:
                    continue
                m = (tr["stim_channel"] == c) & (tr["current_uA"] == cur)
                starts = np.sort(tr["start_time"][m])
                tidx = tr["trial_index"][m][np.argsort(tr["start_time"][m])]
                hits = np.array([hit_of.get(t, False) for t in tidx])
                for ui, spk in enumerate(s["spikes"]):
                    sc = counts_in(spk, starts, 0, window)
                    pc = counts_in(spk, starts, -window, 0)
                    srate, prate = sc / window, pc / window
                    sd = prate.std(ddof=1) if len(prate) > 1 else np.nan
                    z = (srate.mean() - prate.mean()) / sd if sd and sd > 0 else np.nan
                    p = stats.ttest_rel(sc, pc).pvalue if len(sc) > 1 and np.any(sc != pc) else 1.0
                    row = {"si": si, "subject": s["subject"], "date": s["date"], "week": s["week"],
                           "phase": s["phase"], "unit": ui, "cell_type": s["cell_type"][ui],
                           "channel": int(c), "current": float(cur), "n_trials": len(starts),
                           "stim_spikes": int(sc.sum()), "base_rate": float(prate.mean()),
                           "z": z, "p": p}
                    row["tmax_ms"] = time_to_max(spk, starts, window, tmax_bin, tmax_sigma)
                    if with_trials:
                        row["trial_delta"] = (sc - pc).astype(int)
                        row["trial_hit"] = hits
                        row["starts"] = starts
                    rows.append(row)
    return rows


def add_pulse_locking(rows, sessions, rng_seed=1):
    rng = np.random.default_rng(rng_seed)
    for r in rows:
        if not r.get("mod"):
            continue
        s = sessions[r["si"]]
        tr = ephys_trains(s)
        m = (tr["stim_channel"] == r["channel"]) & (tr["current_uA"] == r["current"])
        M = pulse_matrix(s["spikes"][r["unit"]], pulse_starts(np.sort(tr["start_time"][m])))
        r.update(pulse_locking(M, rng))


def channel_days(sessions):
    """Number of recording days of each animal's stimulation channel (for the code's filter that
    drops channels recorded on fewer than 5 days; claims, common method)."""
    d = {}
    for s in sessions:
        for c in np.unique(ephys_trains(s)["stim_channel"]):
            d.setdefault((s["subject"], int(c)), set()).add(s["date"])
    return {k: len(v) for k, v in d.items()}


def modulated(r, zcap=50.0, code_filters=True, ch_days=None):
    """Modulated response (claims, common method): paired t test P < 0.05 with z > 0, more than 50
    spikes, baseline rate at least 0.5 Hz (Methods); with the code's filters, more than 5 trials,
    z below the cap and a channel recorded on at least 5 days."""
    ok = (r["p"] < 0.05) and (r["z"] > 0) and (r["stim_spikes"] > 50) and (r["base_rate"] >= 0.5)
    if code_filters:
        ok = ok and r["n_trials"] > 5 and r["z"] < zcap
        if ch_days is not None:
            ok = ok and ch_days.get((r["subject"], r["channel"]), 0) >= 5
    return bool(ok)


# ------------------------------------------------------------------------------------ statistics
def mwu(a, b, alternative="two-sided"):
    """Mann-Whitney U with the rank-biserial effect size 1 - 2U/(n1 n2) of the paper's ephys code
    (claims, common method), signed so that a positive r means b > a."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    if len(a) == 0 or len(b) == 0:
        return {"n1": len(a), "n2": len(b), "p": np.nan, "r": np.nan, "med1": np.nan, "med2": np.nan}
    res = stats.mannwhitneyu(a, b, alternative=alternative)
    return {"n1": len(a), "n2": len(b), "p": float(res.pvalue),
            "r": float(1 - 2 * res.statistic / (len(a) * len(b))),
            "med1": float(np.median(a)), "med2": float(np.median(b))}


def fdr_bh(p):
    p = np.asarray(p, float)
    o = np.argsort(p)
    q = p[o] * len(p) / (np.arange(len(p)) + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    out = np.empty_like(q)
    out[o] = np.minimum(q, 1)
    return out


# ------------------------------------------------------------------------------ population coupling
def population_coupling(sessions, rows, rng_seed=2, window=TRAIN_S, half_win_ms=100, min_spikes=50,
                        n_shift=200, subjects=None, pop_label=None):
    """Population coupling per unit, condition (channel x current) and session (Methods,
    Population coupling; claims fig6f-population-coupling): spikes within the trains
    concatenated; population rate of all other modulated units in 1 ms bins, Gaussian sigma
    10 ms, mean-centred; coupling is the spike-triggered population rate at zero lag, divided by
    the median of 200 absolute values from circular shifts of the unit's spike train. Only the
    zero-lag value is needed, so the +-window of the stPR does not enter. `pop_label` restricts
    the population to modulated units with that PL label (claims figs9a, reading b)."""
    rng = np.random.default_rng(rng_seed)
    by_cond = {}
    for r in rows:
        if r.get("mod") and r["current"] in CURRENTS and (subjects is None or r["subject"] in subjects):
            by_cond.setdefault((r["si"], r["channel"], r["current"]), []).append(r)
    out = []
    nb = int(round(window * 1000))
    for (si, c, cur), rs in by_cond.items():
        if len(rs) < 2:
            continue
        s = sessions[si]
        tr = ephys_trains(s)
        m = (tr["stim_channel"] == c) & (tr["current_uA"] == cur)
        starts = np.sort(tr["start_time"][m])
        B = {}
        for r in rs:
            spk = s["spikes"][r["unit"]]
            v = np.zeros(len(starts) * nb)
            for i, t in enumerate(starts):
                a, b = np.searchsorted(spk, [t, t + window])
                k = np.floor((spk[a:b] - t) * 1000).astype(int)
                k = k[(k >= 0) & (k < nb)]
                np.add.at(v, i * nb + k, 1)
            B[r["unit"]] = v
        for r in rs:
            v = B[r["unit"]]
            if v.sum() < min_spikes:
                continue
            others = [q for q in rs if q["unit"] != r["unit"] and
                      (pop_label is None or q.get("pl") == pop_label)]
            if not others:
                continue
            pop = sum(B[q["unit"]] for q in others) * 1000.0
            pop = gaussian_filter1d(pop, 10.0)
            pop = pop - pop.mean()
            idx = np.repeat(np.arange(len(v)), v.astype(int))
            c0 = pop[idx].mean()
            sh = rng.integers(1, len(v), size=n_shift)
            null = np.array([pop[(idx + k) % len(v)].mean() for k in sh])
            med = np.median(np.abs(null))
            out.append({**{k: r[k] for k in ("subject", "si", "unit", "channel", "current", "week",
                                             "phase", "cell_type")},
                        "pl": r.get("pl"), "coupling": c0 / med if med > 0 else np.nan})
    return out


# ------------------------------------------------------------------------------------- KL and PSTH
def kl_bootstrap(hit, miss, rng, wins=0.01, frac=0.4, n_boot=1000, bins=25, lo=-30, hi=50):
    """Bootstrap KL(hit || miss) of delta-spikes histograms (claims fig6c-kl-divergence, from the
    code hit_miss_histograms.py): values winsorized, 25 bins over -30 to 50, draws with
    replacement of a fraction of min(n_hit, n_miss) per group. A small constant (1e-10) is added
    to empty bins (standard choice)."""
    def winsor(x):
        a, b = np.quantile(x, [wins, 1 - wins])
        return np.clip(x, a, b)
    hit, miss = winsor(np.asarray(hit, float)), winsor(np.asarray(miss, float))
    k = max(int(frac * min(len(hit), len(miss))), 2)
    edges = np.linspace(lo, hi, bins + 1)
    out = np.empty(n_boot)
    for i in range(n_boot):
        h = np.histogram(rng.choice(hit, k), edges)[0] + 1e-10
        m = np.histogram(rng.choice(miss, k), edges)[0] + 1e-10
        h, m = h / h.sum(), m / m.sum()
        out[i] = np.sum(h * np.log(h / m))
    return out


def psth(spk, starts, bin_s, window=TRAIN_S):
    nb = int(round(window / bin_s))
    h = np.zeros(nb)
    for t in starts:
        a, b = np.searchsorted(spk, [t, t + window])
        if b > a:
            h += np.histogram(spk[a:b] - t, bins=nb, range=(0, window))[0]
    return h / max(len(starts), 1) / bin_s


def cluster_test(H, M, rng, n_perm=1000, alpha=0.05):
    """Cluster-based permutation test of hit against miss rows (claims fig6d, from the code
    hit_miss_psth.py): per bin a two-sided Mann-Whitney test, statistic sign(mean difference) x
    -log10 P; clusters of adjacent bins with |statistic| > -log10 0.05 summed; null of the
    maximum |cluster mass| from permutations of hit and miss labels over rows."""
    thr = -np.log10(alpha)

    def stat(A, B):
        p = stats.mannwhitneyu(A, B, axis=0).pvalue
        p = np.where(np.isnan(p), 1.0, p)
        return np.sign(A.mean(0) - B.mean(0)) * -np.log10(p)

    def clusters(t):
        cl, cur = [], None
        for i, v in enumerate(t):
            if abs(v) > thr:
                if cur is not None and np.sign(v) == np.sign(t[cur[-1]]):
                    cur.append(i)
                else:
                    if cur:
                        cl.append(cur)
                    cur = [i]
            else:
                if cur:
                    cl.append(cur)
                cur = None
        if cur:
            cl.append(cur)
        return [(c[0], c[-1], float(t[c].sum())) for c in cl]

    t = stat(H, M)
    obs = clusters(t)
    X = np.vstack([H, M])
    nh = len(H)
    null = np.zeros(n_perm)
    for i in range(n_perm):
        # swap the hit and miss rows of a random subset of responses (paired rows)
        sw = rng.random(nh) < 0.5
        A = np.where(sw[:, None], M, H)
        B = np.where(sw[:, None], H, M)
        cs = clusters(stat(A, B))
        null[i] = max([abs(c[2]) for c in cs], default=0.0)
    res = [{"start_bin": a, "end_bin": b, "mass": m, "p": float((null >= abs(m)).mean())} for a, b, m in obs]
    return res, t


# ------------------------------------------------------------------------------------- control animals
CONTROL_PULSE_WIN_MS = 20.0  # 50 Hz bursts: 20 ms pulse window (code processing/control/postprocessing/
                             # create_session_responses.py docstring: "50 Hz stim (20ms pulse window)")
CONTROL_PRE_S = 0.7          # baseline before each train (code: analyze_stimulus_train_response with the
                             # 700 ms pre-stim window of WindowConfig, called by the responses_v2 classes
                             # the control pipeline reuses)


def load_control_ephys(asset):
    """One control electrophysiology session: units and the burst table (one row per burst)."""
    f = open_asset(asset["asset_id"])
    s = {"path": asset["path"], "subject": f["general/subject/subject_id"][()].decode(),
         "date": f["session_start_time"][()].decode()[:10]}
    u = f["units"]
    st = u["spike_times"][()]
    idx = u["spike_times_index"][()]
    s["spikes"] = np.split(st, idx[:-1])
    s["stim"] = _table(f["intervals/electrical_stimulation"])
    s["ephys_end"] = float(st.max()) if len(st) else 0.0
    f.close()
    return s


def control_trial_ids(st):
    """A session-wide trial number for each burst row of a control stimulation table. The stored
    trial_index restarts in each recording block (the trials table's rep_num), so the same index
    names several trials; a trial is taken as the bursts from one burst_index_in_trial 0 to the
    next, in time order (the bursts of a trial are 0.5 s apart, trials 10 s apart)."""
    order = np.argsort(st["start_time"], kind="stable")
    ids = np.empty(len(order), dtype=int)
    ids[order] = np.cumsum(st["burst_index_in_trial"][order] == 0) - 1
    return ids


def control_responses(sessions, rng_seed=40, currents=(5.0,), baseline="burst"):
    """Responses of control units, following the paper's control pipeline (processing/control/
    postprocessing/create_session_responses.py and process_control_responses.py at d1922d1), which
    reuses the behavioural response classes with a 20 ms pulse window:

    - a train is one burst (the code groups pulses into trains at gaps above 3 pulse windows, 60 ms,
      and the bursts are 300 ms apart), so the paired t test and z-score are over bursts;
    - stimulation spikes are those from the first pulse to 20 ms after the last, outside the
      blanked 1.5 ms after and 0.5 ms before each pulse; the baseline is the 700 ms before the first
      pulse (code: analyze_stimulus_train_response); paired t test on the per-burst counts; z-score =
      (stimulation rate - baseline rate) / STD (ddof 0) of the per-burst baseline rates;
    - baseline_too_slow when the baseline rate is below 0.5 Hz; num_spikes is the number of
      unblanked pulse-window spikes; time to maximum as `time_to_max` over the burst (200 ms; the
      code searches 0 to 700 ms of a raster that holds spikes after the burst only for the last burst
      of a trial, an assumption);
    - pulse-locking by `pulse_locking` with 20 ms windows over the 10 pulses of each burst.
    Pulses are taken at burst onset + k x 20 ms (50 Hz, table description).

    The bursts of a trial start 0.5 s apart, so for the second and third burst the 700 ms baseline
    holds the burst before it. `baseline="trial"` is a variant that takes every burst's baseline
    from the 700 ms before the first burst of its trial (the trials are 10 s apart), so that no
    baseline holds stimulation; it does not change the pulse-locking draws."""
    rng = np.random.default_rng(rng_seed)
    rows = []
    for si, s in enumerate(sessions):
        st = s["stim"]
        keep = st["stop_time"] < s["ephys_end"]
        for c in np.unique(st["stim_channel"][keep]):
            for cur in np.unique(st["current_uA"][keep & (st["stim_channel"] == c)]):
                if currents is not None and cur not in currents:
                    continue
                m = keep & (st["stim_channel"] == c) & (st["current_uA"] == cur)
                order = np.argsort(st["start_time"][m])
                starts = st["start_time"][m][order]
                base_starts = starts
                if baseline == "trial":
                    tri = control_trial_ids(st)[m][order]
                    first = {k: starts[tri == k].min() for k in np.unique(tri)}
                    base_starts = np.array([first[k] for k in tri])
                npul = int(np.median(st["pulse_count"][m]))
                ipi = CONTROL_PULSE_WIN_MS / 1000.0
                pulses = pulse_starts(starts, npul, ipi)
                stim_dur = (npul - 1) * ipi + ipi + PL_PRE_BLANK_MS / 1000.0
                for ui, spk in enumerate(s["spikes"]):
                    M = pulse_matrix(spk, pulses, CONTROL_PULSE_WIN_MS)
                    nb = M.shape[1]
                    cc = (np.arange(nb) + 0.5) * PL_BIN_MS
                    valid = (cc >= PL_POST_BLANK_MS) & (cc <= CONTROL_PULSE_WIN_MS - PL_PRE_BLANK_MS)
                    sc = (M * valid).reshape(len(starts), npul, nb).sum((1, 2))
                    pc = counts_in(spk, base_starts, -CONTROL_PRE_S, -PL_PRE_BLANK_MS / 1000.0)
                    pre_dur = CONTROL_PRE_S - PL_PRE_BLANK_MS / 1000.0
                    srate, prate = sc.sum() / (stim_dur * len(starts)), pc.sum() / (pre_dur * len(starts))
                    sd = np.std(pc / pre_dur)
                    z = (srate - prate) / sd if sd > 0 else np.nan
                    p = stats.ttest_rel(sc, pc).pvalue if len(sc) > 1 and np.any(sc != pc) else np.nan
                    row = {"si": si, "subject": s["subject"], "date": s["date"], "week": s["week"],
                           "phase": s["phase"], "unit": ui, "channel": int(c), "current": float(cur),
                           "num_trials": len(starts), "num_spikes": int(sc.sum()), "base_rate": prate,
                           "z": z, "p": p, "tmax_ms": time_to_max(spk, starts, 0.2, 0.010, 0.020)}
                    row.update(pulse_locking(M, rng, win_ms=CONTROL_PULSE_WIN_MS))
                    rows.append(row)
    return rows


def coupling_on_segments(spikes, segments, rng, min_spikes=50, n_shift=200):
    """Population coupling of each unit in `spikes` (dict unit -> spike times) to the summed rate
    of the other units, on spikes inside `segments` (list of (start, stop) in s) concatenated, with
    the method of `population_coupling` (1 ms bins, Gaussian sigma 10 ms, mean-centred, zero-lag
    value over the median absolute value of 200 circular shifts; code pop_coupling_control.py)."""
    lens = [int(round((b - a) * 1000)) for a, b in segments]
    off = np.concatenate([[0], np.cumsum(lens)])
    B = {}
    for u, spk in spikes.items():
        v = np.zeros(off[-1])
        for (a, b), o, L in zip(segments, off[:-1], lens):
            i, j = np.searchsorted(spk, [a, b])
            k = np.floor((spk[i:j] - a) * 1000).astype(int)
            k = k[(k >= 0) & (k < L)]
            np.add.at(v, o + k, 1)
        B[u] = v
    out = {}
    for u, v in B.items():
        if v.sum() < min_spikes or len(B) < 2:
            continue
        pop = sum(B[q] for q in B if q != u) * 1000.0
        pop = gaussian_filter1d(pop, 10.0)
        pop = pop - pop.mean()
        idx = np.repeat(np.arange(len(v)), v.astype(int))
        c0 = pop[idx].mean()
        sh = rng.integers(1, len(v), size=n_shift)
        med = np.median(np.abs([pop[(idx + k) % len(v)].mean() for k in sh]))
        out[u] = c0 / med if med > 0 else np.nan
    return out


# ------------------------------------------------------------------------- imaging (metadata)
def imaging_metadata(asset):
    """What a behavioural file holds for imaging: ROI counts, the segmentation descriptions, whether
    reference images are stored, the volumetric mask layout, and whether any ROI or plane carries a
    position of the stimulation contacts. Metadata and shapes only, no traces."""
    f = open_asset(asset["asset_id"])
    o = "processing/ophys"
    d = {"file": asset["path"].split("/")[1], "subject": f["general/subject/subject_id"][()].decode(),
         "date": f["session_start_time"][()].decode()[:10]}
    for kind in ["Planar", "Volumetric"]:
        k = f"{o}/ImageSegmentation_{kind}/PlaneSegmentation_{kind}"
        if k not in f:
            d[f"{kind}_rois"] = 0
            continue
        g = f[k]
        d[f"{kind}_rois"] = len(g["id"])
        d[f"{kind}_description"] = str(g.attrs.get("description", ""))
        d[f"{kind}_columns"] = ",".join(str(c) for c in g.attrs["colnames"])
        d[f"{kind}_reference_images"] = len(g["reference_images"]) if "reference_images" in g else None
        rid = g["roi_id_source"][()]
        d[f"{kind}_roi_id_is_row_index"] = bool(np.array_equal(rid, np.arange(len(rid))))
        if "voxel_mask" in g:
            z = g["voxel_mask"]["z"]
            d[f"{kind}_mask_planes"] = int(z.max()) + 1
    d["imaging_planes"] = sorted(k for k in f["general/optophysiology"])
    d["ophys_entries"] = sorted(k for k in f[o]) if o in f else []
    f.close()
    return d
