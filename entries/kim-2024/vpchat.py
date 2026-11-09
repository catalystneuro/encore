"""Loading and electrophysiological features for dandiset 001544.

Kim, Ananth, Desai, Role & Talmage (2024), Cell Reports 43(4) 114009,
doi:10.1016/j.celrep.2024.114009.

Each NWB file holds one cell recorded in current clamp: one CurrentClampSeries per sweep (voltage,
volts, 10 kHz) and the matching CurrentClampStimulusSeries (the injected current; the file says
amperes, the values are picoamperes). The group of the cell is in `session_description`
(home-cage "did not undergo the odor task", "activated by appetitive odor", "activated by aversive
odor"); the mouse is `subject_id`. Files are streamed from the archive at the pinned version;
nothing is written to disk.

Where the parameters come from:

- The step window, spike detection and the order of the steps follow the paper's code,
  https://github.com/nsdesai/patch_clamp_analysis at tag v1.0.0 (commit
  4ee112583392be14e294b172d497db13789227a2), as the claims file says: the step is located from
  the sweep with the largest current, the first 500 ms of it are analysed
  (analysis_of_neurophysiology_data.m), a spike is a peak above -10 mV with prominence at least
  30 mV, width at half prominence under 10 ms and at least 5 ms from the previous peak
  (rheobasecurrent.m, ficurve.m).
- Only steps from -60 to 200 pA are used: STAR Methods, Electrophysiology, "a family of current
  steps (500 ms duration, -60 to 200 pA amplitude)", and item 16, "a current step between 0 and
  200 pA". Some files also hold steps up to 500 pA; `use_all_steps=True` keeps them, as the code
  does (a variant).
- Membrane potential: the code's baselineVm, the mean over all sweeps of the voltage 10 to 1 ms
  before step onset (claims file, reading (a); no segment without the DC holding current exists in
  the files, so reading (b) cannot be run).
- Sag (Methods item 2, code sagpotential.m): the step at or just below -60 pA, 20 ms median
  filter, the maximum of the second half of the step minus the minimum of the first half, at
  least 0. The code means to move to the next step when the response is saturated, but its test
  (the mode of the indices where the voltage does not change) never fires, so it always uses
  -60 pA; that is the main reading. `skip_saturated_sag=True` applies the intended rule, with
  saturation as 10 ms at the trace's minimum (`saturated`, a standard choice). `code_saturation_test`
  repeats the code's test (the count of the most frequent index among the indices where the voltage
  does not change, against 1000), which is 1 for any trace, and gives the count of unchanged samples
  the test seems meant to compare. Dropping the saturated cells is a further variant.
- Input resistance and tau (Methods items 3 and 4): the response to the -20 pA step, steady state
  as the mean of the last 100 ms of the step against the 45 ms before it (inputresistance.m); tau
  from a single exponential fitted from 2 ms after step onset to the end of the step, as the code
  fits it, but on the -20 pA step the Methods name (the code fits the first valid step from -50 to
  0 pA, here -40 pA).
- Rheobase (item 5): the smallest positive step with a spike. Threshold (item 6): the voltage
  where dV/dt first exceeds 20 mV/ms (Methods; the code uses 10 mV/ms, `dvdt_threshold`) on the
  trace interpolated tenfold (code), searching from 3 ms before the first peak (code).
- Spike amplitude, width at half amplitude, upstroke (items 7, 8, 10) as the Methods and code.
  Downstroke (item 11): the minimum dV/dt from the first peak to 5 ms after it; the code's window
  runs to the end of the step (a coding slip, `downIdx = max(..., length)`), so the 5 ms window
  is a standard choice for "the downstroke of the first action potential".
- Spike latency (item 9): step onset to threshold crossing (Methods); the code measures to the
  peak (variant `latency_peak`).
- AHP amplitude (item 12), "the difference between threshold and the minimum potential 100 ms
  later": reading (a) the minimum within 100 ms after threshold, reading (b) the voltage 100 ms
  after threshold (both named in the claims file); and the code's definition (afterhyperpolarization.m,
  a variant): the first step at or above rheobase with two or more spikes, the minimum between the
  first spike and 0.75 ms before the second (or to the end of the window), threshold at 10 mV/ms on
  uninterpolated data. AHP latency and width (items 13, 14) from reading (a): threshold to the
  minimum, and the time between the half-amplitude crossings within the 100 ms. When the first spike
  comes less than 100 ms before the end of the analysed step, the window of reading (a) is cut at the
  end of the step (`ahp_window_ms` gives its length) and reading (b) has no value.
- f-I slope (item 15, code ficurve.m): linear fit of rate against current from the step before the
  first spiking step to the step with the most spikes. Max firing rate (item 16): the largest count
  over the 500 ms of any step from 0 to 200 pA, over 0.5 s.
- Adaptation index and CV of ISIs (items 17, 18): the Methods' "maximal current step", taken as the
  largest step used (200 pA where present); second half count over first 250 ms count; CV is 0
  with fewer than three spikes (code).
- Statistics. Reading (a): cell-level one-way ANOVA and two-tailed Student t-tests; reading (b):
  a mixed model with a random intercept per mouse, pairs by Wald tests against the normal (`p`) and
  against t on the number of mice minus 3 degrees of freedom (`p_t`, a small-sample reference, a
  standard choice). The STAR Methods (Quantification and statistical analysis) say "Non-parametric
  tests were conducted if the data failed these tests" (Shapiro-Wilk and Kolmogorov-Smirnov); the
  claims file's readings do not include this rule, so Kruskal-Wallis and two-sided Mann-Whitney U
  tests are given beside them (`p_kruskal`, `p_mw`).
- Exclusion rules (STAR Methods, Electrophysiology): input resistance under 50 MOhm, resting
  potential above -50 mV, or a change of more than 20% in these. Series resistance is not in the
  files. The change is checked on the -20 pA test pulse that every sweep carries after the step
  (1.5 to 1.6 s) and on the pre-step voltage, first sweep against last; that the test pulse serves
  this purpose is an assumption.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy.signal import find_peaks, medfilt
from scipy.optimize import curve_fit

DANDISET_ID = "001544"
DANDISET_VERSION = "0.260827.1410"
API = "https://api.dandiarchive.org/api"

GROUPS = {
    "Mouse VP cholinergic neurons that did not undergo the odor task": "ALL",
    "Mouse VP cholinergic neurons activated by appetitive odor": "APP",
    "Mouse VP cholinergic neurons activated by aversive odor": "AV",
}

ANALYSIS_MS = 500.0
SAG_CURRENT = -60.0
MIN_SPIKE_HEIGHT = -10.0   # mV, code v1.0.0
MIN_PROMINENCE = 30.0      # mV
MIN_DISTANCE_MS = 5.0
MAX_WIDTH_MS = 10.0
METHODS_DVDT = 20.0        # mV/ms, Methods item 6
CODE_DVDT = 10.0           # mV/ms, code v1.0.0
MAX_STEP = 200.0           # pA, Methods


def list_assets(version: str = DANDISET_VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    return out


def _s(x):
    v = x[()]
    if isinstance(v, np.ndarray):
        v = v[0]
    return v.decode() if isinstance(v, bytes) else v


def load_cell(asset: dict) -> dict:
    """Read one file: metadata, and current (pA) and voltage (mV) per sweep, in file order."""
    url = f"{API}/assets/{asset['asset_id']}/download/"
    with h5py.File(remfile.File(url), "r") as h:
        acq, st = h["acquisition"], h["stimulus/presentation"]
        an, sn = sorted(acq), sorted(st)
        V = np.array([acq[k]["data"][:] * acq[k]["data"].attrs["conversion"] for k in an]).T * 1e3
        I = np.array([st[k]["data"][:] * st[k]["data"].attrs["conversion"] for k in sn]).T
        rate = float(acq[an[0]]["starting_time"].attrs["rate"])
        meta = dict(
            path=asset["path"], asset_id=asset["asset_id"],
            identifier=_s(h["identifier"]), subject=_s(h["general/subject/subject_id"]),
            sex=_s(h["general/subject/sex"]), age=_s(h["general/subject/age"]),
            genotype=_s(h["general/subject/description"]),
            session_description=_s(h["session_description"]),
            session_start=_s(h["session_start_time"]),
            stimulus_unit=st[sn[0]]["data"].attrs["unit"],
            voltage_unit=acq[an[0]]["data"].attrs["unit"],
            bias_current=float(acq[an[0]]["bias_current"][()]),
            bridge_balance=float(acq[an[0]]["bridge_balance"][()]),
            stim_rates=sorted({float(st[k]["starting_time"].attrs["rate"]) for k in sn}),
            rates=sorted({float(acq[k]["starting_time"].attrs["rate"]) for k in an}),
            starting_times=sorted({float(acq[k]["starting_time"][()]) for k in an}),
            n_sweeps=len(an), n_stim=len(sn),
        )
    meta["group"] = GROUPS.get(meta["session_description"], "unknown")
    return dict(meta=meta, I=I, V=V, rate=rate)


def load_all(version: str = DANDISET_VERSION, workers: int = 8) -> list[dict]:
    assets = list_assets(version)
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_cell, assets))


# ---------------------------------------------------------------- step layout and spikes

def step_layout(cell: dict, use_all_steps: bool = False):
    """Start and stop index of the step (code), step amplitudes, and the sweep order to use."""
    I, dt = cell["I"], 1000.0 / cell["rate"]
    mx = I.max()
    col = int(I.max(0).argmax())
    w = np.nonzero(I[:, col] == mx)[0]
    start, stop = int(w[0]), int(w[-1])
    n = int(np.ceil(ANALYSIS_MS / dt))
    if n < stop - start:
        stop = start + n - 1
    steps = I[stop, :]
    keep = np.arange(I.shape[1]) if use_all_steps else np.nonzero((steps >= -60) & (steps <= MAX_STEP))[0]
    order = keep[np.argsort(steps[keep], kind="stable")]
    return start, stop, steps, order


def detect_peaks(v: np.ndarray, dt: float):
    """Peak indices by the code's findpeaks call (height, distance, half-prominence width, prominence)."""
    if v.max() < MIN_SPIKE_HEIGHT:
        return np.array([], dtype=int)
    p, _ = find_peaks(v, height=MIN_SPIKE_HEIGHT, distance=max(1, round(MIN_DISTANCE_MS / dt)),
                      prominence=MIN_PROMINENCE, width=(None, round(MAX_WIDTH_MS / dt)), rel_height=0.5)
    return p


def _interp10(v, dt):
    t = np.arange(len(v)) * dt
    dt1 = dt / 10
    t1 = np.arange(0, t[-1] + dt1 / 2, dt1)
    return np.interp(t1, t, v), dt1


# ---------------------------------------------------------------- features

def saturated(v: np.ndarray, n: int = 100) -> bool:
    """True when at least n samples (10 ms at 10 kHz) sit within 0.01 mV of the trace's minimum: the
    recording floor (-105.6 mV in five cells), not a membrane response."""
    return int((v <= np.nanmin(v) + 0.01).sum()) >= n


def code_saturation_test(v: np.ndarray) -> dict:
    """The saturation test of sagpotential.m (code v1.0.0) on the step part of one sweep:
    foo = find(diff(v) == 0); [~, boo] = mode(foo); saturated when boo >= 1000. `mode_count` is boo,
    the count of the most frequent index, which is 1 for any trace (each index occurs once) or 0 when
    no sample repeats; `zero_diffs` is the number of unchanged samples, the count the test seems
    meant to compare with 1000."""
    idx = np.nonzero(np.diff(v) == 0)[0]
    mode_count = int(np.unique(idx, return_counts=True)[1].max()) if len(idx) else 0
    return dict(mode_count=mode_count, code_fires=mode_count >= 1000, zero_diffs=len(idx),
                intended_fires=len(idx) >= 1000)


def features(cell: dict, dvdt_threshold: float = METHODS_DVDT, use_all_steps: bool = False,
             skip_saturated_sag: bool = False) -> dict:
    """The eighteen features of the STAR Methods for one cell, with the variants named above."""
    V, I, dt = cell["V"], cell["I"], 1000.0 / cell["rate"]
    start, stop, steps, order = step_layout(cell, use_all_steps)
    out = {}
    pre = V[start - round(10 / dt):start - round(1 / dt), :]
    out["vm"] = float(pre.mean())                     # code baselineVm (mean over all sweeps)
    out["vm_sweep_sd"] = float(pre.mean(0).std())

    # sag
    sag_cands = [j for j in order if steps[j] <= SAG_CURRENT]
    out["sag_saturated"] = bool(sag_cands) and saturated(V[start:stop + 1, sag_cands[-1]])
    if skip_saturated_sag and sag_cands:
        # the code's intent (sagpotential.m): go to the next step up while the response is saturated
        later = [j for j in order if steps[j] >= steps[sag_cands[-1]] and steps[j] < 0]
        ok = [j for j in later if not saturated(V[start:stop + 1, j])]
        sag_cands = ok[:1]
    if sag_cands:
        j = sag_cands[-1]
        d = medfilt(V[:, j], round(20 / dt) | 1)
        half = start + round((stop - start) / 2)
        out["sag"] = max(0.0, float(d[half:stop].max() - d[start:half + 1].min()))
        out["sag_step"] = float(steps[j])
    else:
        out["sag"], out["sag_step"] = np.nan, np.nan

    # input resistance and tau, -20 pA step
    r20 = [j for j in order if steps[j] == -20]
    out["rin"] = out["tau"] = np.nan
    if r20:
        j = r20[0]
        r = V[start - round(50 / dt):stop + 1, j]
        vss = r[-round(100 / dt):].mean() - r[:round(45 / dt)].mean()
        out["rin"] = float(abs(1000 * vss / 20))
        seg = r[round(52 / dt):]
        t = np.arange(len(seg)) * dt
        try:
            p, _ = curve_fit(lambda t, a, b, c: a * np.exp(-b * t) + c, t, seg,
                             p0=[seg[0] - seg[-1], 0.1, seg[-1]], maxfev=20000)
            out["tau"] = float(1 / p[1]) if p[1] > 0 else np.nan
        except Exception:
            pass

    # spike counts per step
    counts = {}
    for j in order:
        if steps[j] <= 0:
            counts[j] = 0
            continue
        counts[j] = len(detect_peaks(V[start:stop + 1, j], dt))
    spiking = [j for j in order if counts[j] > 0]
    dur = (stop - start + 1) * dt / 1000
    pos = [j for j in order if 0 <= steps[j]]
    out["max_rate"] = float(max(counts[j] for j in pos) / dur) if pos else np.nan
    out["n_steps"] = len(order)
    out["max_step"] = float(steps[order].max())
    for k in ["rheobase", "threshold", "amplitude", "width", "latency", "latency_peak", "upstroke",
              "downstroke", "ahp_a", "ahp_b", "ahp_latency", "ahp_width", "ahp_code", "fi_slope",
              "adaptation", "cv_isi", "ahp_window_ms"]:
        out[k] = np.nan
    if not spiking:
        return out
    jr = spiking[0]
    out["rheobase"] = float(steps[jr])

    # first spike at rheobase
    v = V[start:stop + 1, jr]
    vi, dti = _interp10(v, dt)
    pk = detect_peaks(vi, dti)
    if len(pk):
        p0 = pk[0]
        dvdt = np.gradient(vi, dti)
        g = dvdt.copy()
        g[:max(0, p0 - round(3 / dti))] = 0
        cross = np.nonzero(g > dvdt_threshold)[0]
        if len(cross):
            ti = cross[0]
            thr = vi[ti]
            out["threshold"] = float(thr)
            out["amplitude"] = float(vi[p0] - thr)
            out["latency"] = float(ti * dti)
            out["latency_peak"] = float(p0 * dti)
            half = thr + (vi[p0] - thr) / 2
            above = np.nonzero(np.diff((vi >= half).astype(int)))[0]
            above = above[above >= ti - 1]
            if len(above) >= 2:
                out["width"] = float((above[1] - above[0]) * dti)
            out["upstroke"] = float(dvdt[max(0, p0 - round(5 / dti)):p0 + 1].max())
            out["downstroke"] = float(dvdt[p0:p0 + round(5 / dti) + 1].min())
            w100 = round(100 / dti)
            seg = vi[ti:ti + w100 + 1]
            out["ahp_window_ms"] = float((len(seg) - 1) * dti)
            if len(seg) > w100:
                out["ahp_b"] = float(thr - vi[ti + w100])
            # reading (a): the minimum within 100 ms (to the end of the step if shorter)
            m = int(seg.argmin())
            out["ahp_a"] = float(thr - seg[m])
            out["ahp_latency"] = float(m * dti)
            hv = thr - (thr - seg[m]) / 2
            below = np.nonzero(np.diff((seg < hv).astype(int)))[0]
            if len(below) >= 2:
                out["ahp_width"] = float((below[1] - below[0]) * dti)
            elif len(below) == 1:
                out["ahp_width"] = float((len(seg) - below[0]) * dti)
    out["ahp_code"] = _ahp_code(V, dt, start, stop, order, jr)

    # f-I slope (code)
    rates = np.array([counts[j] / dur for j in order])
    amps = steps[order]
    i_first = order.tolist().index(jr)
    i_max = int(rates.argmax())
    lo = max(0, i_first - 1)
    if i_max > lo:
        out["fi_slope"] = float(np.polyfit(amps[lo:i_max + 1], rates[lo:i_max + 1], 1)[0])
    # adaptation and CV at the maximal step
    jm = order[-1]
    pkm = detect_peaks(V[start:stop + 1, jm], dt)
    n = stop - start + 1
    first = int((pkm <= n / 2).sum())
    second = len(pkm) - first
    out["adaptation"] = float(second / first) if first > 0 else np.nan
    if len(pkm) < 3:
        out["cv_isi"] = 0.0
    else:
        isi = np.diff(pkm) * dt
        out["cv_isi"] = float(isi.std(ddof=1) / isi.mean())
    return out


def _ahp_code(V, dt, start, stop, order, jr):
    """AHP amplitude as afterhyperpolarization.m of the code v1.0.0 computes it."""
    order = list(order)
    locs = data = thr = None
    for j in order[order.index(jr):]:
        d = V[start:stop + 1, j]
        p = detect_peaks(d, dt)
        if len(p) == 0:
            continue
        g = np.gradient(d, dt)
        g[:max(0, p[0] - round(3 / dt))] = 0
        c = np.nonzero(g > CODE_DVDT)[0]
        if not len(c):
            continue
        locs = list(p - round(0.75 / dt))
        data, thr = d, d[c[0]]
        if len(locs) > 1:
            break
        locs = [locs[0], stop - start]
    if locs is None:
        return np.nan
    seg = data[locs[0]:locs[1] + 1]
    return float(thr - seg.min())


def quality(cell: dict) -> dict:
    """Values for the Methods' exclusion rules that the files allow to be checked."""
    V, I, dt = cell["V"], cell["I"], 1000.0 / cell["rate"]
    start, stop, steps, order = step_layout(cell, use_all_steps=True)
    # the test pulse after the step: the last change points of the current
    j = order[len(order) // 2]
    ch = np.nonzero(np.diff(I[:, j]))[0]
    t0, t1 = int(ch[-2]) + 1, int(ch[-1]) + 1
    amp = float(np.median(I[t0:t1, j]))
    rin_tp, base = [], []
    for k in range(V.shape[1]):   # file order, which is the order of acquisition
        b = V[t0 - round(50 / dt):t0, k].mean()
        ss = V[t1 - round(30 / dt):t1, k].mean()
        rin_tp.append(abs(1000 * (ss - b) / amp))
        base.append(V[start - round(10 / dt):start - round(1 / dt), k].mean())
    rin_tp, base = np.array(rin_tp), np.array(base)
    ok = np.isfinite(rin_tp)          # a sweep cut short holds NaN after its end
    rin_tp, base = rin_tp[ok], base[ok]
    return dict(tp_start_ms=t0 * dt, tp_ms=(t1 - t0) * dt, tp_pA=amp,
                rin_tp_first=float(rin_tp[0]), rin_tp_last=float(rin_tp[-1]),
                rin_tp_change=float(abs(rin_tp[-1] - rin_tp[0]) / rin_tp[0]),
                vm_first=float(base[0]), vm_last=float(base[-1]),
                vm_change=float(abs(base[-1] - base[0]) / abs(base[0])),
                vm_max=float(base.max()),
                rin_tp_sweeps=rin_tp.round(1).tolist(), vm_sweeps=base.round(2).tolist(),
                rin_tp_maxdev=float(np.max(np.abs(rin_tp - rin_tp[0])) / rin_tp[0]))


# ---------------------------------------------------------------- statistics

def cell_tests(df: pd.DataFrame, col: str, pairs=(("ALL", "APP"), ("ALL", "AV"), ("APP", "AV"))) -> dict:
    """Reading (a): cell-level one-way ANOVA and uncorrected two-tailed Student t-tests."""
    from scipy import stats
    d = df.dropna(subset=[col])
    g = {k: d.loc[d.group == k, col].values for k in ["ALL", "APP", "AV"]}
    F, p = stats.f_oneway(*[g[k] for k in g if len(g[k])])
    out = {"F": F, "p_anova": p, "df": (2, len(d) - 3), "n": {k: len(v) for k, v in g.items()},
           "mean": {k: float(np.mean(v)) for k, v in g.items()},
           "sem": {k: float(np.std(v, ddof=1) / np.sqrt(len(v))) for k, v in g.items()}}
    kw = stats.kruskal(*g.values())
    out["p_kruskal"] = kw.pvalue
    out["shapiro_min_p"] = min(stats.shapiro(v).pvalue for v in g.values() if len(v) >= 3)
    for a, b in pairs:
        t = stats.ttest_ind(g[b], g[a])
        out[f"{a}-{b}"] = dict(t=t.statistic, p=t.pvalue, df=len(g[a]) + len(g[b]) - 2,
                               diff=float(np.mean(g[b]) - np.mean(g[a])),
                               p_mw=stats.mannwhitneyu(g[b], g[a], alternative="two-sided").pvalue)
    return out


def nested_tests(df: pd.DataFrame, col: str, pairs=(("ALL", "APP"), ("ALL", "AV"), ("APP", "AV"))) -> dict:
    """Reading (b): cells nested in mice nested in group, as a linear mixed model with a random
    intercept per mouse (REML), the model Prism fits for a nested ANOVA. The group effect is a Wald
    test of the two group coefficients; pairs are Wald tests of the contrasts."""
    import warnings
    import statsmodels.formula.api as smf
    from scipy import stats
    d = df.dropna(subset=[col]).copy()
    d["y"] = d[col]
    out = {}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        m = smf.mixedlm("y ~ C(group, Treatment('ALL'))", d, groups=d["subject"]).fit(reml=True)
    names = m.fe_params.index
    b, cov = m.fe_params.values, m.cov_params().loc[names, names].values
    L = np.zeros((2, len(names)))
    L[0, 1] = L[1, 2] = 1
    w = float(L @ b @ np.linalg.solve(L @ cov @ L.T, L @ b))
    out["wald_chi2"] = w
    out["p_group"] = float(stats.chi2.sf(w, 2))
    out["mouse_var"] = float(m.cov_re.iloc[0, 0])
    out["resid_var"] = float(m.scale)
    out["converged"] = bool(m.converged)
    df_t = d["subject"].nunique() - 3
    out["df_t"] = df_t
    idx = {"ALL": None, "APP": 1, "AV": 2}
    for a, c in pairs:
        v = np.zeros(len(names))
        if idx[c]:
            v[idx[c]] += 1
        if idx[a]:
            v[idx[a]] -= 1
        est = float(v @ b)
        se = float(np.sqrt(v @ cov @ v))
        out[f"{a}-{c}"] = dict(diff=est, z=est / se, p=float(2 * stats.norm.sf(abs(est / se))),
                               p_t=float(2 * stats.t.sf(abs(est / se), df_t)))
    # classical nested ANOVA: group mean square over the mouse-within-group mean square
    mice = d.groupby(["group", "subject"])["y"].agg(["mean", "count"]).reset_index()
    gm = d.groupby("group")["y"].mean()
    grand = d["y"].mean()
    ss_g = sum(d.loc[d.group == k, "y"].count() * (gm[k] - grand) ** 2 for k in gm.index)
    ss_m = sum(r["count"] * (r["mean"] - gm[r["group"]]) ** 2 for _, r in mice.iterrows())
    df_g, df_m = len(gm) - 1, len(mice) - len(gm)
    out["F_nested"] = float((ss_g / df_g) / (ss_m / df_m)) if ss_m > 0 else np.nan
    out["df_nested"] = (df_g, df_m)
    out["p_nested"] = float(stats.f.sf(out["F_nested"], df_g, df_m)) if ss_m > 0 else np.nan
    return out


def readings_table(sets: dict, col: str, pairs=(("ALL", "APP"), ("ALL", "AV"), ("APP", "AV"))) -> pd.DataFrame:
    """One row per cell set: group means, reading (a) cell-level tests and reading (b) nested tests.
    A pair "X-Y" gives the difference Y minus X."""
    rows = []
    for name, d in sets.items():
        a = cell_tests(d, col, pairs)
        b = nested_tests(d, col, pairs)
        r = {"cells": name, "n": "/".join(str(a["n"][k]) for k in ["ALL", "APP", "AV"])}
        for k in ["ALL", "APP", "AV"]:
            r[f"mean {k}"] = a["mean"][k]
        r["(a) F"] = a["F"]
        r["(a) df"] = f"{a['df'][0]},{a['df'][1]}"
        r["(a) p"] = a["p_anova"]
        for pr in pairs:
            k = f"{pr[0]}-{pr[1]}"
            r[f"(a) t {k}"] = a[k]["t"]
            r[f"(a) p {k}"] = a[k]["p"]
        r["(b) p group"] = b["p_group"]
        for pr in pairs:
            k = f"{pr[0]}-{pr[1]}"
            r[f"(b) p {k}"] = b[k]["p"]
        for pr in pairs:
            k = f"{pr[0]}-{pr[1]}"
            r[f"(b) p_t {k}"] = b[k]["p_t"]
        r["(b) df_t"] = b["df_t"]
        r["(b) nested F"] = b["F_nested"]
        r["(b) nested p"] = b["p_nested"]
        r["Kruskal p"] = a["p_kruskal"]
        for pr in pairs:
            k = f"{pr[0]}-{pr[1]}"
            r[f"MW p {k}"] = a[k]["p_mw"]
        r["Shapiro min p"] = a["shapiro_min_p"]
        rows.append(r)
    return pd.DataFrame(rows).set_index("cells")


def per_mouse(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Mean of a feature per mouse, with its number of cells."""
    return (df.groupby(["group", "subject"])[col].agg(["count", "mean", "min", "max"])
            .round(2).reset_index())
