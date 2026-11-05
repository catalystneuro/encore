"""Loading and measures for dandiset 001708 (Ashworth et al., RVM ON, OFF and NEUTRAL cells).

Where each parameter comes from is said next to it:
- "criterion": the claim's criterion in claims/001708/10.64898-2025.12.15.693905.yaml, which cites
  the paper or its code (github.com/nox-lab/multi-timescale-rhythmic-dynamics-in-rvm-neurons at
  commit e12f3ee771f4b5506e5db0bac09762ba6044a4d6, called "the code" below).
- "paper": a passage of the paper (bioRxiv doi:10.64898/2025.12.15.693905, version 4), cited.
- "assumption": a choice the paper leaves open, said why.
- "standard": a detail that cannot change a result.

The data are streamed from the DANDI archive at a pinned version; nothing is written to disk.
"""
from __future__ import annotations

import json
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile

DANDISET = "001708"
VERSION = "0.260604.1023"  # the version the paper cites (reference 72) and the only published one
API = "https://api.dandiarchive.org/api"

CLASS_NAMES = {"ON": "ON", "OFF": "OFF", "NEUT": "NEUTRAL", "Neutral": "NEUTRAL"}


# ----------------------------------------------------------------------------------------------
# Loading
# ----------------------------------------------------------------------------------------------
def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=500"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out.extend(page["results"])
        url = page.get("next")
    return sorted(out, key=lambda a: a["path"])


def dandiset_metadata():
    with urllib.request.urlopen(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/") as r:
        return json.load(r)


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def _read_one(asset, tries=4):
    for k in range(tries):
        try:
            return _read_one_inner(asset)
        except Exception:  # transient network errors
            if k == tries - 1:
                raise
            time.sleep(2 + 3 * k)


def _read_one_inner(asset):
    url = f"{API}/assets/{asset['asset_id']}/download/"
    f = remfile.File(url)
    with h5py.File(f, "r") as h:
        g = h["general"]
        rec = dict(
            path=asset["path"],
            subject=_str(g["subject/subject_id"][()]),
            sex=_str(g["subject/sex"][()]),
            weight=_str(g["subject/weight"][()]),
            protocol=_str(g["protocol"][()]),
            identifier=_str(h["identifier"][()]),
            session_start=_str(h["session_start_time"][()]),
            experiment_description=_str(g["experiment_description"][()]),
        )
        u = h["units"]
        names = [_str(x) for x in u["_name"][:]]
        st = u["spike_times"][:]
        idx = u["spike_times_index"][:]
        obs = u["obs_intervals"][:]
        obs_idx = u["obs_intervals_index"][:]
        trains, starts, stops = [], [], []
        lo = 0
        olo = 0
        for i in range(len(names)):
            trains.append(np.asarray(st[lo:idx[i]], dtype=float))
            lo = idx[i]
            iv = obs[olo:obs_idx[i]]
            olo = obs_idx[i]
            starts.append(float(iv[0][0]))
            stops.append(float(iv[-1][1]))
        rec["unit_names"] = names
        rec["trains"] = trains
        rec["t_start"] = starts
        rec["t_stop"] = stops
        ev = {}
        for grp in ("acquisition", "stimulus/presentation"):
            if grp in h:
                for k in h[grp].keys():
                    ev[k] = np.asarray(h[f"{grp}/{k}/timestamps"][:], dtype=float)
                    ev[k + "_labels"] = [_str(x) for x in h[f"{grp}/{k}/data"][:]]
        rec["events"] = ev
        rec["n_obs_intervals"] = [int(obs_idx[0])] + list(np.diff(obs_idx).astype(int))
    return rec


def load_all(assets=None, workers=16):
    """Streams every NWB file of the pinned version; returns (sessions, cells).

    sessions: list of dicts (one per file) with events; cells: DataFrame, one row per unit.
    """
    assets = assets if assets is not None else list_assets()
    with ThreadPoolExecutor(workers) as ex:
        sessions = list(ex.map(_read_one, assets))
    rows = []
    for si, s in enumerate(sessions):
        for ui, name in enumerate(s["unit_names"]):
            rows.append(dict(session=si, path=s["path"], subject=s["subject"], protocol=s["protocol"],
                             unit=ui, label=name, cls=CLASS_NAMES[name],
                             t_start=s["t_start"][ui], t_stop=s["t_stop"][ui],
                             n_spikes=len(s["trains"][ui])))
    return sessions, pd.DataFrame(rows)


def heat(s):
    return np.sort(s["events"].get("heat", np.array([])))


def withdrawals(s):
    return np.sort(s["events"].get("paw_withdrawal", np.array([])))


def pinches(s):
    return np.sort(s["events"].get("pinch", np.array([])))


def ekg(s):
    return np.sort(s["events"].get("EKG", np.array([])))


# ----------------------------------------------------------------------------------------------
# Trials (criterion of fig1c-psth-counts and fig2-trial-counts: the rule of
# Spike2Tools.get_all_event_spike_trains with get_previous_event / get_next_event)
# ----------------------------------------------------------------------------------------------
def combined_events(s, with_pinch):
    ev = [(t, "heat") for t in heat(s)] + [(t, "flick") for t in withdrawals(s)]
    if with_pinch:
        ev += [(t, "keyboard") for t in pinches(s)]
    ev.sort(key=lambda x: x[0])
    return ev


def _prev_event(i, ev, ignore_heat):
    j = i - 1
    while j >= 0:
        if not (ignore_heat and ev[j][1] == "heat"):
            return ev[j]
        j -= 1
    return (0.0, "start")


def _next_event(i, ev, t_stop, ignore_flick):
    j = i + 1
    while j < len(ev):
        if not (ignore_flick and ev[j][1] == "flick"):
            return ev[j]
        j += 1
    return (t_stop, "end")


def trial_times(s, t_stop, event, pre, post, with_pinch):
    """Event times kept for one cell. event 'flick' (withdrawal) or 'heat'; pre < 0, post > 0 (s).

    For withdrawal alignment the previous event ignores heats and the next event is any event; for
    heat alignment the previous event is any event and the next event ignores withdrawals (the
    code's ignore_heat / ignore_flick flags). The trial is dropped when the next event is less than
    `post` after the event, or the window start falls before the previous event (or before 0), or
    the window end passes the recording end.
    """
    ev = combined_events(s, with_pinch)
    kept = []
    for i, (t, name) in enumerate(ev):
        if name != event:
            continue
        ignore_heat = event == "flick"
        prev = _prev_event(i, ev, ignore_heat)
        nxt = _next_event(i, ev, t_stop, ignore_flick=not ignore_heat)
        if nxt[0] - t < post:
            continue
        if t + pre < prev[0]:
            continue
        if t + post > t_stop:
            continue
        kept.append(t)
    return kept


def all_trials(sessions, cells, cls, event, pre, post, with_pinch):
    """List of (cell index, event time) for every kept trial of the class."""
    out = []
    for ci, c in cells[cells.cls == cls].iterrows():
        s = sessions[c.session]
        for t in trial_times(s, c.t_stop, event, pre, post, with_pinch):
            out.append((ci, t))
    return out


def summed_counts(sessions, cells, trials, pre=-10.0, post=100.0, bin_size=0.05):
    """Spike counts per 50 ms bin summed over all trials (criterion of fig2-trial-counts;
    Methods, Piecewise Bayesian modeling, "We binned spikes using a 50 ms time bin")."""
    nb = int(round((post - pre) / bin_size))
    edges = pre + bin_size * np.arange(nb + 1)
    total = np.zeros(nb)
    per_trial = []
    for ci, t in trials:
        c = cells.loc[ci]
        tr = sessions[c.session]["trains"][c.unit] - t
        h, _ = np.histogram(tr, edges)
        total += h
        per_trial.append(h)
    return edges[:-1], total, np.array(per_trial)


# ----------------------------------------------------------------------------------------------
# Piecewise Bayesian models, ported from bayesian_cell_models.py of the code (criterion); the
# priors are the Methods' (Piecewise Bayesian modeling) as the notebooks set them.
# ----------------------------------------------------------------------------------------------
ON_PRIORS = dict(T_LOWER=-4, T_UPPER=4, LBR_MU=3.0, LBR_SIGMA=0.5, LKPRE_MU=4.0, LKPRE_SIGMA=0.1,
                 LKPOST_MU=2.5, LKPOST_SIGMA=1.0)
# notebook 18a (heat-aligned ON): T_LOWER 0, T_UPPER 12 (its param_dict.json)
ON_PRIORS_HEAT = dict(ON_PRIORS, T_LOWER=0, T_UPPER=12)


def build_on_double(X, Y, p=ON_PRIORS):
    import pymc as pm
    import pytensor.tensor as pt
    with pm.Model() as m:
        ts = pm.Uniform("t_switch", p["T_LOWER"], p["T_UPPER"])
        lbr_pre = pm.Normal("log_base_rate_pre", p["LBR_MU"], p["LBR_SIGMA"])
        lbr_post = pm.Normal("log_base_rate_post", p["LBR_MU"], p["LBR_SIGMA"])
        b1pre = pm.LogNormal("beta_1_pre", mu=np.log(0.1), sigma=0.5)
        b1post = -pm.LogNormal("beta_1_post", mu=np.log(0.1), sigma=0.5)
        bslow = -pm.LogNormal("beta_slow_post", mu=np.log(1 / 50), sigma=0.5)
        lkpre = pm.Normal("log_k_pre", p["LKPRE_MU"], p["LKPRE_SIGMA"])
        lkpost = pm.Normal("log_k_post", p["LKPOST_MU"], p["LKPOST_SIGMA"])
        kslow = pm.Deterministic("k_slow", pt.exp(lkpre) + pt.exp(lbr_pre) - pt.exp(lbr_post) - pt.exp(lkpost))
        rate = pt.switch(X <= ts,
                         pt.exp(lbr_pre) + pt.exp(lkpre) * pt.exp((X - ts) * b1pre),
                         kslow * pt.exp((X - ts) * bslow) + pt.exp(lbr_post) + pt.exp(lkpost) * pt.exp((X - ts) * b1post))
        pm.Poisson("obs", mu=rate, observed=Y)
    return m


def build_on_single(X, Y, p=ON_PRIORS):
    import pymc as pm
    import pytensor.tensor as pt
    with pm.Model() as m:
        ts = pm.Uniform("t_switch", p["T_LOWER"], p["T_UPPER"])
        lbr_pre = pm.Normal("log_base_rate_pre", p["LBR_MU"], p["LBR_SIGMA"])
        lbr_post = pm.Normal("log_base_rate_post", p["LBR_MU"], p["LBR_SIGMA"])
        b1pre = pm.LogNormal("beta_1_pre", mu=np.log(0.1), sigma=0.5)
        b1post = -pm.LogNormal("beta_1_post", mu=np.log(1 / 50), sigma=0.5)
        lkpre = pm.Normal("log_k_pre", p["LKPRE_MU"], p["LKPRE_SIGMA"])
        kpost = pm.Deterministic("k_post", pt.exp(lbr_pre) + pt.exp(lkpre) - pt.exp(lbr_post))
        rate = pt.switch(X <= ts,
                         pt.exp(lbr_pre) + pt.exp(lkpre) * pt.exp((X - ts) * b1pre),
                         pt.exp(lbr_post) + kpost * pt.exp((X - ts) * b1post))
        pm.Poisson("obs", mu=rate, observed=Y)
    return m


def build_mean(X, Y, sigma=5.0):
    """Null model (build_mean_model; SIGMA_BASE_RATE 5 in notebooks 20 and 27)."""
    import pymc as pm
    with pm.Model() as m:
        r = pm.HalfNormal("base_rate", sigma=sigma)
        pm.Poisson("obs", mu=r * np.ones_like(X), observed=Y)
    return m


OFF_LIN_PRIORS = dict(SIGMA_B=4, SIGMA_A=4, T_LOWER=-4, T_UPPER=4, K=1, K2=1, K3=1)  # notebook 21
OFF_LIN_PRIORS_HEAT = dict(OFF_LIN_PRIORS, T_UPPER=20)  # notebook 21a
OFF_DOUBLE_PRIORS = dict(SIGMA_B=4, SIGMA_A=5, T_LOWER=-4, T_UPPER=4, K=(2, 2), K2=(2, 2), K3=(0, 2))  # nb 24 and 28
OFF_LINERF_PRIORS = dict(SIGMA_A=5, K2=(2, 2), K3=2)  # notebook 29


def build_off_linear(X, Y, p=OFF_LIN_PRIORS, log_k=True):
    """Sigmoid response, linear plus exponential recovery (build_linear_slope_recovery_off_model).
    log_k=True is the code (priors on log k and log k2); log_k=False is the Methods' k, k2 ~ N(0, 1)
    read literally on k and k2 themselves (the variant of the criterion of fig2g-switch-times)."""
    import pymc as pm
    import pytensor.tensor as pt
    with pm.Model() as m:
        b = pm.HalfNormal("b", sigma=p["SIGMA_B"])
        a = pm.Deterministic("a", b + pm.HalfNormal("a_bar", sigma=p["SIGMA_A"]))
        c = pm.Deterministic("c", b + pm.HalfNormal("c_bar", sigma=p["SIGMA_A"]))
        if log_k:
            lk = pm.Normal("log_k", 0, p["K"])
            lk2 = pm.Normal("log_k2", 0, p["K2"])
            k = pm.Deterministic("k", pt.exp(lk))
            k2 = pm.Deterministic("k2", pt.exp(lk2))
        else:
            k = pm.TruncatedNormal("k", 0, p["K"], lower=0)
            k2 = pm.TruncatedNormal("k2", 0, p["K2"], lower=0)
        k3 = pm.HalfNormal("k3", sigma=p["K3"])
        t = pm.Uniform("t_switch", p["T_LOWER"], p["T_UPPER"])
        u0 = pm.Uniform("u0", lower=b, upper=a)
        x0 = t - (1 / k) * pt.log((a - b) / (u0 - b) - 1)
        sig = b + (a - b) / (1 + pt.exp(k * (X - x0)))
        rec = u0 + (c - u0) * (1 - pt.exp(-k2 * (X - t))) + k3 * (X - t)
        pm.Poisson("obs", mu=pt.switch(X < t, sig, rec), observed=Y)
    return m


def build_off_double(X, Y, p=OFF_DOUBLE_PRIORS):
    """Sigmoid response, double-exponential recovery (build_double_exponential_off_model)."""
    import pymc as pm
    import pytensor.tensor as pt
    with pm.Model() as m:
        b = pm.HalfNormal("b", sigma=p["SIGMA_B"])
        a = pm.Deterministic("a", b + pm.HalfNormal("a_bar", sigma=p["SIGMA_A"]))
        lk = pm.Normal("log_k", *p["K"])
        lk2 = pm.Normal("log_k2", *p["K2"])
        lk3 = pm.Normal("log_k3", *p["K3"])
        t = pm.Uniform("t_switch", p["T_LOWER"], p["T_UPPER"])
        u0 = pm.Uniform("u0", lower=b, upper=a)
        c = pm.Deterministic("c", u0 + pm.HalfNormal("c_bar", sigma=p["SIGMA_A"]))
        d = pm.Deterministic("d", u0 + pm.HalfNormal("d_bar", sigma=p["SIGMA_A"]))
        x0 = t - (1 / pt.exp(lk)) * pt.log((a - b) / (u0 - b) - 1)
        sig = b + (a - b) / (1 + pt.exp(pt.exp(lk) * (X - x0)))
        e1 = (c - u0) * (1 - pt.exp(-pt.exp(lk2) * (X - t)))
        e2 = (d - u0) * (1 - pt.exp(-pt.exp(lk3) * (X - t)))
        pm.Poisson("obs", mu=pt.switch(X < t, sig, u0 + e1 + e2), observed=Y)
    return m


def build_off_erf_double(X, Y, p=OFF_DOUBLE_PRIORS):
    """Gaussian CDF response, double-exponential recovery (build_erf_off_model, notebook 28)."""
    import pymc as pm
    import pytensor.tensor as pt
    with pm.Model() as m:
        off = pm.HalfNormal("erfoffset", sigma=10)
        sc = pm.HalfNormal("erfscale", 10)
        sl = pm.HalfNormal("erfslope", 4)
        lk2 = pm.Normal("log_k2", *p["K2"])
        lk3 = pm.Normal("log_k3", *p["K3"])
        t = pm.Uniform("t_switch", -4, 4)
        u0 = pm.Uniform("u0", lower=off, upper=off + 2 * sc)
        c = pm.Deterministic("c", u0 + pm.HalfNormal("c_bar", sigma=p["SIGMA_A"]))
        d = pm.Deterministic("d", u0 + pm.HalfNormal("d_bar", sigma=p["SIGMA_A"]))
        x0 = t - pt.erfinv(1 - (u0 - off) / sc) / sl
        erf = off + sc * (1 - pt.erf(sl * (X - x0)))
        e1 = (c - u0) * (1 - pt.exp(-pt.exp(lk2) * (X - t)))
        e2 = (d - u0) * (1 - pt.exp(-pt.exp(lk3) * (X - t)))
        pm.Poisson("obs", mu=pt.switch(X < t, erf, u0 + e1 + e2), observed=Y)
    return m


def build_off_erf_linear(X, Y, p=OFF_LINERF_PRIORS):
    """Gaussian CDF response, linear plus exponential recovery (build_linear_erf_off_model, nb 29)."""
    import pymc as pm
    import pytensor.tensor as pt
    with pm.Model() as m:
        off = pm.HalfNormal("erfoffset", sigma=10)
        sc = pm.HalfNormal("erfscale", 10)
        sl = pm.HalfNormal("erfslope", 4)
        lk2 = pm.Normal("log_k2", *p["K2"])
        k3 = pm.HalfNormal("k3", sigma=p["K3"])
        t = pm.Uniform("t_switch", -4, 4)
        u0 = pm.Uniform("u0", lower=off, upper=off + 2 * sc)
        c = pm.Deterministic("c", u0 + pm.HalfNormal("c_bar", sigma=p["SIGMA_A"]))
        x0 = t - pt.erfinv(1 - (u0 - off) / sc) / sl
        erf = off + sc * (1 - pt.erf(sl * (X - x0)))
        rec = u0 + (c - u0) * (1 - pt.exp(-pt.exp(lk2) * (X - t))) + k3 * (X - t)
        pm.Poisson("obs", mu=pt.switch(X < t, erf, rec), observed=Y)
    return m


def sample(model, seed, draws=1000, tune=1000, chains=4, target_accept=0.8):
    """NUTS, 4 chains, 1000 tuning steps, 1000 draws (Methods, Piecewise Bayesian modeling);
    target_accept 0.8 (sample_model of the code). The seed is a standard choice."""
    import pymc as pm
    with model:
        idata = pm.sample(draws=draws, tune=tune, chains=chains, cores=chains, target_accept=target_accept,
                          random_seed=seed, progressbar=False, idata_kwargs={"log_likelihood": True},
                          compute_convergence_checks=False)
    return idata


def post(idata, name):
    return idata.posterior[name].values.reshape(-1)


def on_double_rate(idata, X):
    P = {k: post(idata, k)[:, None] for k in ["t_switch", "log_base_rate_pre", "log_base_rate_post", "beta_1_pre",
                                              "beta_1_post", "beta_slow_post", "log_k_pre", "log_k_post", "k_slow"]}
    d = X[None, :] - P["t_switch"]
    pre = np.exp(P["log_base_rate_pre"]) + np.exp(P["log_k_pre"]) * np.exp(d * P["beta_1_pre"])
    postr = (P["k_slow"] * np.exp(-d * P["beta_slow_post"]) + np.exp(P["log_base_rate_post"])
             + np.exp(P["log_k_post"]) * np.exp(-d * P["beta_1_post"]))
    return np.where(d <= 0, pre, postr)


def off_linear_rate(idata, X):
    P = {k: post(idata, k)[:, None] for k in ["a", "b", "c", "k", "k2", "k3", "t_switch", "u0"]}
    x0 = P["t_switch"] - (1 / P["k"]) * np.log((P["a"] - P["b"]) / (P["u0"] - P["b"]) - 1)
    with np.errstate(over="ignore"):
        sig = P["b"] + (P["a"] - P["b"]) / (1 + np.exp(P["k"] * (X[None, :] - x0)))
    d = X[None, :] - P["t_switch"]
    rec = P["u0"] + (P["c"] - P["u0"]) * (1 - np.exp(-P["k2"] * d)) + P["k3"] * d
    return np.where(d < 0, sig, rec)


def times_on(rate, X, pct):
    """calculate_rate_percentages_of_peak of the code, for one percentage: per draw, the first grid
    time before the peak at which the rate reaches base + pct (peak - base) (base: first grid
    point), and the first grid time after the peak at which it falls to base_post + pct (peak -
    base_post) (base_post: last grid point)."""
    n, T = rate.shape
    pk = np.argmax(rate, axis=1)
    peak = rate[np.arange(n), pk]
    base_r, base_f = rate[:, 0], rate[:, -1]
    grid = np.arange(T)[None, :]
    thr_r = base_r + pct * (peak - base_r)
    cand = (rate >= thr_r[:, None]) & (grid <= pk[:, None])
    rise = np.where(cand.any(1), X[np.argmax(cand, 1)], np.nan)
    thr_f = base_f + pct * (peak - base_f)
    cand = (rate <= thr_f[:, None]) & (grid >= pk[:, None])
    fall = np.where(cand.any(1), X[np.argmax(cand, 1)], np.nan)
    return rise, fall


def times_off(rate, X, pct):
    """calculate_rate_percentages_of_peak_OFF of the code: 'fall by pct' (first time before the
    nadir with rate <= base_pre - pct (base_pre - nadir)) and 'rise to pct' (first time after the
    nadir with rate >= base_post - pct (base_post - nadir))."""
    n, T = rate.shape
    dp = np.argmin(rate, axis=1)
    nadir = rate[np.arange(n), dp]
    b0, b1 = rate[:, 0], rate[:, -1]
    grid = np.arange(T)[None, :]
    thr = b0 - pct * (b0 - nadir)
    cand = (rate <= thr[:, None]) & (grid <= dp[:, None])
    fall = np.where(cand.any(1), X[np.argmax(cand, 1)], np.nan)
    thr = b1 - pct * (b1 - nadir)
    cand = (rate >= thr[:, None]) & (grid >= dp[:, None])
    rise = np.where(cand.any(1), X[np.argmax(cand, 1)], np.nan)
    return fall, rise


def hdi(x, prob=0.97):
    import arviz as az
    x = np.asarray(x)
    x = x[~np.isnan(x)]
    return tuple(float(v) for v in az.hdi(x, hdi_prob=prob))


def summarize(x, prob=0.97):
    x = np.asarray(x)
    lo, hi = hdi(x, prob)
    return dict(mean=float(np.nanmean(x)), hdi_low=lo, hdi_high=hi, n_nan=int(np.isnan(x).sum()))


# ----------------------------------------------------------------------------------------------
# Ongoing segments (criterion of ongoing-cell-counts: Spike2Tools.get_event_windows, size 1500 s;
# Methods, Data processing, paragraph 2)
# ----------------------------------------------------------------------------------------------
def ongoing_segment(s, t_stop, size=1500.0):
    """The `size` seconds ending at the heat onset (or recording end) that closes the longest gap
    between heat onsets. Returns (start, end, gap, buffer after the preceding heat onset)."""
    h = list(heat(s)) + [t_stop]
    gaps = np.diff(h)
    i = int(np.argmax(gaps))
    end = h[i + 1]
    start = end - size
    return start, end, float(gaps[i]), float(start - h[i])


def cut(train, start, end):
    """Spikes in [start, end], shifted to start at 0 (cut_out_spikes with zero=True)."""
    return train[(train >= start) & (train <= end)] - start


# ----------------------------------------------------------------------------------------------
# Generalized Poisson periodic GP (criterion of fig5b-train-r2; Methods, Gaussian process modeling,
# paragraph 2), the model of non_poisson_gpytorch_model.py of the code
# ----------------------------------------------------------------------------------------------
def bin_split(train, t_stop, cut_time, bin_width=5.0):
    """5 s bins from 0 to t_stop (bin_spikes_and_split of the code); training bins before cut_time."""
    nb = int(np.floor(t_stop / bin_width + 1e-9))
    edges = bin_width * np.arange(nb + 1)
    y, _ = np.histogram(train, edges)
    x = edges[:-1] + bin_width / 2
    tr = edges[1:] <= cut_time + 1e-9
    return x[tr], y[tr], x[~tr], y[~tr]


def fit_gp_fast(cells_xy, n_iter=10000, num_inducing=200, p_noise=0.001, lr=0.05, seed=0, max_count=200,
                snapshots=(), n_mc=30, threads=4, dtype="float64"):
    """The periodic GP and the constant-mean null GP of the code (PeriodicGPModel, MeanGPModel,
    PoissonUniformMixtureLikelihood, compare_log_liks), written out in plain torch as a batch of
    independent GPs (one per cell), for speed. The pseudo-R2 is 1 minus the summed expected log
    likelihood of the periodic GP over that of the null GP (compare_log_liks). Same model as gpytorch's whitened VariationalStrategy with a
    CholeskyVariationalDistribution, fixed inducing points evenly spaced over the training span,
    ConstantMean, ScaleKernel(PeriodicKernel) with gpytorch's form
    k = s exp(-2 sin^2(pi |t - t'| / p) / l), softplus constraints, jitter 1e-6 on K_zz, the
    lengthscale prior N(0.1, 0.1) on the raw lengthscale, the alpha prior N(0, 0.5) on alpha, the
    initial values of the code (period 300, lengthscale 0.1, outputscale var(y)/100, constant
    (max + min)(1 - alpha)/2/10, alpha 0) and the ELBO of VariationalELBO, each cell's terms divided
    by its number of training bins. The null model is the code's MeanGPModel: constant mean and
    a diagonal (white) kernel, whose inducing covariance with the data is zero. Expected log
    likelihoods use 30 draws from each bin's marginal (a standard Monte Carlo choice).
    Defaults are the Methods' (200 inducing points, p_noise 0.001) with params.json's 10000
    iterations; gp.ipynb passes the code's 100 inducing points, p_noise 0.01 and 5000 iterations
    (an assumption, said there). `snapshots` adds results at earlier iteration counts.
    """
    import torch
    torch.set_num_threads(threads)
    torch.manual_seed(seed)
    dt = getattr(torch, dtype)
    sp = torch.nn.functional.softplus

    def isp(v):
        v = torch.as_tensor(v, dtype=dt)
        return v + torch.log(-torch.expm1(-v))

    B = len(cells_xy)
    ntr = np.array([len(c[1]) for c in cells_xy]); nte = np.array([len(c[3]) for c in cells_xy])
    Ntr, Nte = int(ntr.max()), int(max(nte.max(), 1))

    def pad(arrs, N):
        out = np.zeros((B, N)); mask = np.zeros((B, N))
        for i, a in enumerate(arrs):
            out[i, :len(a)] = a; mask[i, :len(a)] = 1
        return torch.as_tensor(out, dtype=dt), torch.as_tensor(mask, dtype=dt)

    tx, tm = pad([c[0] for c in cells_xy], Ntr); ty, _ = pad([c[1] for c in cells_xy], Ntr)
    vx, vm = pad([c[2] for c in cells_xy], Nte); vy, _ = pad([c[3] for c in cells_xy], Nte)
    nt = torch.as_tensor(ntr, dtype=dt)
    M = num_inducing
    Z = torch.stack([torch.linspace(0.0, float(np.max(c[0])), M, dtype=dt) for c in cells_xy])  # (B, M)
    ymax = torch.as_tensor([float(np.max(c[1])) for c in cells_xy], dtype=dt)
    ymin = torch.as_tensor([float(np.min(c[1])) for c in cells_xy], dtype=dt)
    yvar = torch.as_tensor([float(np.var(c[1], ddof=1)) for c in cells_xy], dtype=dt)
    eye = torch.eye(M, dtype=dt).expand(B, M, M)
    tril = torch.tril_indices(M, M)

    def gp_logprob(y, rate, alpha):
        mu = rate * (1 - alpha)
        adj = mu + alpha * y
        ok = (mu > 0) & (adj > 0)
        smu = torch.where(ok, mu, torch.ones_like(mu)); sadj = torch.where(ok, adj, torch.ones_like(adj))
        lp = torch.log(smu) + (y - 1) * torch.log(sadj) - sadj - torch.lgamma(y + 1)
        return torch.where(ok, lp, torch.full_like(mu, -1e30))

    def mixture(y, f, alpha, ulog):
        lp = gp_logprob(y, 10.0 * sp(f), alpha)
        return torch.logsumexp(torch.stack([np.log(1 - p_noise) + lp, np.log(p_noise) + ulog.expand_as(lp)]), 0)

    def kern(a, b, P):
        d = (a[:, :, None] - b[:, None, :]).abs()
        return sp(P["raw_os"])[:, None, None] * torch.exp(
            -2.0 * torch.sin(np.pi * d / sp(P["raw_per"])[:, None, None]) ** 2 / sp(P["raw_ls"])[:, None, None])

    def alpha_of(P):
        return 1.0 - sp(-P["raw_alpha"])  # gpytorch LessThan(1.0)

    def new_params(periodic):
        P = {"const": ((ymax + ymin) / 2 / 10.0).clone(), "raw_alpha": isp(torch.ones(B, dtype=dt)) * -1.0,
             "vm": torch.zeros(B, M, dtype=dt), "vL": torch.eye(M, dtype=dt).repeat(B, 1, 1)}
        # LessThan(1): alpha = 1 - softplus(-raw); alpha 0 means softplus(-raw) = 1, raw = -isp(1)
        if periodic:
            P.update(raw_os=isp(yvar / 100), raw_ls=isp(torch.full((B,), 0.1, dtype=dt)),
                     raw_per=isp(torch.full((B,), 300.0, dtype=dt)))
        else:
            P.update(raw_var=torch.zeros(B, dtype=dt))
        for k in P:
            P[k] = P[k].clone().requires_grad_(True)
        return P

    def marg(P, x, periodic):
        if not periodic:
            v = sp(P["raw_var"])
            return P["const"][:, None].expand_as(x), v[:, None].expand_as(x), None
        Kzz = kern(Z, Z, P) + 1e-6 * eye
        L = torch.linalg.cholesky(Kzz)
        Kzx = kern(Z, x, P)
        A = torch.linalg.solve_triangular(L, Kzx, upper=False)  # (B, M, n)
        Ls = torch.tril(P["vL"])
        mean = P["const"][:, None] + (A * P["vm"][:, :, None]).sum(1)
        SA = Ls.transpose(-1, -2) @ A
        var = sp(P["raw_os"])[:, None] + (SA ** 2).sum(1) - (A ** 2).sum(1)
        return mean, var.clamp_min(1e-10), L

    def kl(P):
        Ls = torch.tril(P["vL"])
        diag = torch.diagonal(Ls, dim1=-2, dim2=-1)
        return 0.5 * ((Ls ** 2).sum((-1, -2)) + (P["vm"] ** 2).sum(-1) - M - 2 * torch.log(diag.abs()).sum(-1))

    def ell(P, x, y, mask, periodic, ulog, n_s=n_mc):
        mean, var, _ = marg(P, x, periodic)
        f = mean + var.sqrt() * torch.randn((n_s,) + mean.shape, dtype=dt)
        mix = mixture(y, f, alpha_of(P)[:, None], ulog)
        return torch.where(mask > 0, mix.mean(0), torch.zeros_like(mask)).sum(-1)

    def loss_fn(P, periodic, ulog):
        e = ell(P, tx, ty, tm, periodic, ulog)
        lprior = torch.distributions.Normal(0.0, 0.5).log_prob(alpha_of(P))
        if periodic:
            lprior = lprior + torch.distributions.Normal(0.1, 0.1).log_prob(P["raw_ls"])
        return -((e - kl(P) + lprior) / nt).sum()

    snaps_all = {}
    for periodic in (True, False):
        ulog = torch.log(1.0 / ((torch.full((B,), float(max_count), dtype=dt) if periodic else ymax) + 1))[:, None]
        P = new_params(periodic)
        opt = torch.optim.Adam(list(P.values()), lr=lr)
        snaps = {}
        for it in range(1, n_iter + 1):
            opt.zero_grad()
            loss = loss_fn(P, periodic, ulog)
            loss.backward()
            opt.step()
            if it in snapshots or it == n_iter:
                snaps[it] = {k: v.detach().clone() for k, v in P.items()}
        snaps_all[periodic] = (snaps, ulog)

    results = {}
    with torch.no_grad():
        for it in sorted(snaps_all[True][0]):
            P1 = snaps_all[True][0][it]; u1 = snaps_all[True][1]
            P0 = snaps_all[False][0][it]; u0 = snaps_all[False][1]
            e_tr = ell(P1, tx, ty, tm, True, u1); m_tr = ell(P0, tx, ty, tm, False, u0)
            e_te = ell(P1, vx, vy, vm, True, u1); m_te = ell(P0, vx, vy, vm, False, u0)
            grid = torch.stack([torch.linspace(0.0, float(np.max(c[0])), 400, dtype=dt) for c in cells_xy])
            mg, vg, _ = marg(P1, grid, True)
            fr = (10.0 * sp(mg + vg.sqrt() * torch.randn((200,) + mg.shape, dtype=dt))).mean(0)
            results[it] = dict(period=sp(P1["raw_per"]).numpy(), lengthscale=sp(P1["raw_ls"]).numpy(),
                               outputscale=sp(P1["raw_os"]).numpy(), alpha=alpha_of(P1).numpy(),
                               const=P1["const"].numpy(),
                               train_r2=(1 - e_tr / m_tr).numpy(), test_r2=(1 - e_te / m_te).numpy(),
                               grid=grid.numpy(), mean_rate=fr.numpy(), params=P1, Z=Z)
    return results


def gp_predict_rate(res_it, i, t, n_samples=200, seed=0):
    """Mean over draws of 10 softplus(f) at times t for cell i of a fit_gp_fast result (the
    periodic kernel extends the fit beyond the training span)."""
    import torch
    sp = torch.nn.functional.softplus
    g = torch.Generator().manual_seed(seed)
    P = {k: v[i:i + 1] for k, v in res_it["params"].items()}
    Z = res_it["Z"][i:i + 1]
    x = torch.as_tensor(np.atleast_1d(t), dtype=torch.float64)[None, :]

    def kern(a, b):
        d = (a[:, :, None] - b[:, None, :]).abs()
        return sp(P["raw_os"])[:, None, None] * torch.exp(
            -2.0 * torch.sin(np.pi * d / sp(P["raw_per"])[:, None, None]) ** 2 / sp(P["raw_ls"])[:, None, None])
    with torch.no_grad():
        M = Z.shape[1]
        L = torch.linalg.cholesky(kern(Z, Z) + 1e-6 * torch.eye(M, dtype=torch.float64))
        A = torch.linalg.solve_triangular(L, kern(Z, x), upper=False)
        Ls = torch.tril(P["vL"])
        mean = P["const"][:, None] + (A * P["vm"][:, :, None]).sum(1)
        var = (sp(P["raw_os"])[:, None] + ((Ls.transpose(-1, -2) @ A) ** 2).sum(1) - (A ** 2).sum(1)).clamp_min(1e-10)
        f = mean + var.sqrt() * torch.randn((n_samples,) + mean.shape, dtype=torch.float64, generator=g)
        return (10.0 * sp(f)).mean(0)[0].numpy()


# ----------------------------------------------------------------------------------------------
# The paper's code repository, at the commit the claims file read; only its stored outputs are
# fetched, as reference values the criteria compare with (never as data).
# ----------------------------------------------------------------------------------------------
CODE_REPO = "nox-lab/multi-timescale-rhythmic-dynamics-in-rvm-neurons"
CODE_COMMIT = "e12f3ee771f4b5506e5db0bac09762ba6044a4d6"


def code_file(path):
    import io
    url = f"https://raw.githubusercontent.com/{CODE_REPO}/{CODE_COMMIT}/{path}"
    with urllib.request.urlopen(url) as r:
        return io.BytesIO(r.read())


# ----------------------------------------------------------------------------------------------
# Spectra (criterion of fig3bc-psd-peaks: get_auto_correlation_freqs_with_rate of the code)
# ----------------------------------------------------------------------------------------------
def spike_psd(train, t_stop, nfft, bin_size=0.005, fmax_keep=0.2, hf_bin=0.5):
    """Periodogram of a spike train binned at 5 ms over [0, t_stop]: counts demeaned, Hann window
    over the whole train (one Welch segment), zero-padded to nfft, f >= 0 kept, normalized to unit
    area. Returns the low-frequency part (f <= fmax_keep), and the spectrum averaged in hf_bin Hz
    bins over the whole range (for the power above 10 Hz)."""
    from scipy.signal.windows import hann
    nb = int(round(t_stop / bin_size))
    x = np.bincount(np.minimum((np.asarray(train) / bin_size).astype(int), nb - 1), minlength=nb).astype(float)
    x -= x.mean()
    x *= hann(nb, sym=False)
    X = np.fft.rfft(x, n=nfft)
    f = np.fft.rfftfreq(nfft, d=bin_size)
    p = np.abs(X) ** 2
    if nfft % 2 == 0:  # the code's two-sided estimate keeps f >= 0 only, without the Nyquist bin
        f, p = f[:-1], p[:-1]
    p /= np.trapezoid(p, f)
    lo = f <= fmax_keep
    edges = np.arange(0, f[-1] + hf_bin, hf_bin)
    idx = np.minimum(np.digitize(f, edges) - 1, len(edges) - 2)
    hf = np.bincount(idx, weights=p) / np.maximum(np.bincount(idx), 1)
    return f[lo], p[lo], edges[:-1] + hf_bin / 2, hf


def highest_peak(f, p, lo, hi):
    """Index (into f) of the highest local maximum of p with lo <= f <= hi (get_maximum_power_peak),
    and the index the code passes to peak_widths (the position within the masked array)."""
    from scipy.signal import find_peaks
    m = (f >= lo) & (f <= hi)
    pk, _ = find_peaks(p[m])
    if len(pk) == 0:
        return None, None
    j = pk[np.argmax(p[m][pk])]
    return int(np.flatnonzero(m)[j]), int(j)


def fwhm_hz(f, p, idx):
    from scipy.signal import peak_widths
    w = peak_widths(p, [idx], rel_height=0.5)[0][0]
    return float(w * (f[1] - f[0]))


# ----------------------------------------------------------------------------------------------
# Period scan (criterion of fig4-nlml-minima: GP_period_scoping.ipynb of the code)
# ----------------------------------------------------------------------------------------------
def smoothed_rate(train, t_stop, sigma=2.0, dt=2.0, trunc=4.0):
    """Rate (Hz) sampled every dt s from a Gaussian kernel of sd sigma (elephant
    instantaneous_rate with a GaussianKernel, no border correction); the kernel truncation at 4
    sd is a standard choice."""
    n = int(np.floor(t_stop / dt))
    counts = np.bincount(np.minimum((np.asarray(train) / dt).astype(int), n - 1), minlength=n).astype(float)
    k = np.arange(-int(np.ceil(trunc * sigma / dt)), int(np.ceil(trunc * sigma / dt)) + 1) * dt
    ker = np.exp(-0.5 * (k / sigma) ** 2) / (np.sqrt(2 * np.pi) * sigma)
    return np.arange(n) * dt + dt / 2, np.convolve(counts, ker, mode="same")


def nlml_scan(t, y, periods, variance=5.0, lengthscale=1.0, noise=1.0):
    """Negative log marginal likelihood of GPy's GPRegression with a StdPeriodic kernel
    (k = variance exp(-0.5 (sin(pi (t - t') / period) / lengthscale)^2)), zero mean, Gaussian
    noise variance 1 (GPy's default), at each period."""
    from scipy.linalg import cho_factor, cho_solve
    d = t[:, None] - t[None, :]
    out = np.empty(len(periods))
    n = len(t)
    for i, per in enumerate(periods):
        K = variance * np.exp(-0.5 * (np.sin(np.pi * d / per) / lengthscale) ** 2) + noise * np.eye(n)
        c = cho_factor(K, lower=True)
        a = cho_solve(c, y)
        out[i] = 0.5 * y @ a + np.sum(np.log(np.diag(c[0]))) + 0.5 * n * np.log(2 * np.pi)
    return out


# ----------------------------------------------------------------------------------------------
# Coherence (criterion of fig6c-coherence-counts: multitaper_coherence.py of the code)
# ----------------------------------------------------------------------------------------------
def segments(x, seg_len, step):
    starts = np.arange(0, len(x) - seg_len + 1, step)
    return np.stack([x[s:s + seg_len] for s in starts])


def mt_coherence(xs, ys, fs, NW=3.5, K=6):
    from scipy.signal.windows import dpss
    n = xs.shape[1]
    tap = dpss(n, NW, K, sym=False)
    xs = xs - xs.mean(1, keepdims=True)
    ys = ys - ys.mean(1, keepdims=True)
    X = np.fft.rfft(xs[:, None, :] * tap[None], axis=-1)
    Y = np.fft.rfft(ys[..., None, :] * tap[None], axis=-1)
    Sxx = (np.abs(X) ** 2).mean(axis=(0, 1))
    Syy = (np.abs(Y) ** 2).mean(axis=(-3, -2))
    Sxy = (X * np.conj(Y)).mean(axis=(-3, -2))
    C = np.clip(np.abs(Sxy) ** 2 / (Sxx * Syy + 1e-20), 0, 1)
    return np.fft.rfftfreq(n, d=1 / fs), C, Syy


def phase_randomize(ys, rng):
    n = ys.shape[1]
    Y = np.fft.rfft(ys, axis=1)
    ph = rng.uniform(0, 2 * np.pi, size=Y.shape)
    ph[:, 0] = 0.0
    if n % 2 == 0:
        ph[:, -1] = 0.0
    return np.fft.irfft(np.abs(Y) * np.exp(1j * ph), n=n, axis=1)


def coherence_test(spikes, beats, start, end, seed=1, n_surr=1000, bin_size=2.0, seg_s=500.0, alpha=0.001):
    """Spike counts and heart-beat counts in 2 s bins over [start, end]; 500 s segments with 50%
    overlap; multitaper coherence (NW 3.5, K 6); 1000 surrogates with each heart-rate segment
    phase-randomized (rng seeded per cell, as the code); threshold the 99.9th percentile of the
    surrogates' maximum coherence over all frequencies. Returns f, C, threshold, heart-beat
    spectrum."""
    nb = int(np.floor((end - start) / bin_size))
    edges = start + bin_size * np.arange(nb + 1)
    x = np.histogram(spikes, edges)[0].astype(float)
    y = np.histogram(beats, edges)[0].astype(float)
    L = int(seg_s / bin_size)
    xs, ys = segments(x, L, L // 2), segments(y, L, L // 2)
    f, C, Syy = mt_coherence(xs, ys, 1 / bin_size)
    rng = np.random.default_rng(seed)
    mx = np.empty(n_surr)
    for b in range(n_surr):
        _, Cs, _ = mt_coherence(xs, phase_randomize(ys, rng), 1 / bin_size)
        mx[b] = Cs.max()
    thr = float(np.percentile(mx, 100 * (1 - alpha)))
    return f, C, thr, xs.shape[0]
