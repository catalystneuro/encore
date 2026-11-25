"""Loading and measures for Schapiro, Rittenberg, Kenngott & Marder (2024), eLife 13:RP98844,
on Dryad dataset doi:10.5061/dryad.1rn8pk129, version 310115.

The Dryad files cannot be streamed without a token (docs/archives.md, "Dryad"); they are staged,
checked against their SHA-256, in DATA_DIR and read there, in place.

Where each parameter comes from:

- Burst detection (``extract_bursts``): two or more PD spikes, at least 200 ms between bursts
  (paper, Methods, Analysis: "Bursts were identified as two or more consecutive PD spikes with an
  inter-burst interval of at least 200 ms"). The details (how a lone spike is merged into the
  next burst, and the removal of cycles whose frequency jumps more than three times the mean
  neighbouring change) are a port of the deposited extractBurstFrequency_Final.m, the code the
  paper's Data availability statement says reproduces its results. The removal deletes a
  cycle's start with its frequency, so the cycle before it spans two bursts while keeping its own
  period; these cycles are marked (``gap``) and left out of the hold means and phases, an
  assumption (``hold_means``).
- Phase (``phase_calc``): delay of the first or last spike after the first PD spike, over the
  period (Methods, Analysis). Which spikes form the neuron's burst within a cycle (the longest
  run of spikes with inter-spike intervals of at most 0.11 s) is a port of the deposited
  Phase_Calc.m, called with 0.11 in CalculateFrequencyPhaseEtc.m.
- Temperature of a cycle (``cycle_temperature``): mean of Tempsub between the first spikes of two
  consecutive bursts (CalculateFrequencyPhaseEtc.m; the Results' "change in mean temperature").
- Condition windows (``condition_mask``): the cycles whose first PD spike lies between
  fileTimes(start+1) and fileTimes(end+2) of the Timings table (CalculateFrequencyPhaseEtc.m,
  ProbabilityUpDown.m; README, "Identified Spike and Temperature Data").
- Cycles slower than 1/8 Hz are dropped from the frequency and phase measures
  (CalculateFrequencyPhaseEtc.m, "Eliminate all cycles that have a period of > ... 8seconds").
- Holding temperature: cycles within 0.3 degrees C of 11, 13, ..., 21 degrees C (Results, The
  steady-state frequency increase, paragraph 3; claims file header). The deposited
  CalculateFrequencyPhaseEtc.m uses a strict bound (< 0.3) for the Cs+ frequency and temperature
  and <= 0.3 elsewhere; ``strict_cs`` follows it where a Cs+ frequency is formed.
- Jag measure (``jag_measure``): temperature smoothed over 10 cycles and frequency over 30
  (Methods, Analysis), with MATLAB's ``smooth`` (centred moving average, even spans reduced by one,
  shrinking at the ends) as the deposited ProbabilityUpDown.m uses it; increasing cycles have a
  smoothed temperature change > 0.01 degrees C, stable cycles a change within +-0.01 (the
  deposited code and the Figure 3A legend, "change less than 0.01 C/pyloric cycle"); thresholds
  0.002 Hz (Methods). O3 spans: the Timings window, the step protocol, and the window extended
  over the cooling to 11 degrees C.
- Q10 (``q10``): readings (a), (b), (c) of the claims file header, O1. Reading (b), the
  straight-line fit of log10 frequency on the measured mean temperature, is what the deposited
  CalculateFrequencyPhaseEtc.m does.
- Repeated-measures ANOVA and Tukey comparisons (``rm_anova``, ``tukey_rm``): the claims file's
  O5 readings.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
from scipy import stats

DATASET = "dryad:1rn8pk129"
VERSION = "310115"
# Staged copy of the pinned version, /tmp/dryad/<id>/<version id>/ (docs/archives.md, "Dryad"). Built from parts
# because the files cannot be streamed from Dryad without a token; this is the one place the entry names it.
DATA_DIR = Path("/", "tmp", "dryad", "1rn8pk129", VERSION)
TARGETS = np.arange(11, 22, 2)
MOE = 0.3


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


def load_mat(name: str) -> dict:
    """Read a MATLAB v5 file, MATLAB tables included (mat-io reads MCOS objects)."""
    import matio

    return matio.load_from_mat(str(DATA_DIR / name))


def _vec(x) -> np.ndarray:
    return np.asarray(x, dtype=float).ravel()


def load_spikes(expt: str) -> dict:
    """One <expt>_SpikeAndTemp.mat file: spike times (s), Tempsub (deg C), x_sub (min), fileTimes (s),
    and the Timings table as {condition: (starts, ends)} of file indices (0-based, as stored)."""
    d = load_mat(f"{expt}_SpikeAndTemp.mat")
    out = {"expt": expt}
    for k in ("PD", "PD2", "LP", "PY"):
        if k in d:
            out[k] = _vec(d[k])
    out["Tempsub"] = _vec(d["Tempsub"])
    out["x_sub"] = _vec(d["x_sub"])
    out["fileTimes"] = _vec(d["fileTimes"])
    T = d["Timings"]
    out["Timings"] = {c: (_vec(T[c].iloc[0]).astype(int), _vec(T[c].iloc[1]).astype(int)) for c in T.columns}
    return out


def extract_bursts(spikes: np.ndarray, min_time_bw_bursts: float = 0.2, min_sp_per_burst: int = 2, return_gaps: bool = False):
    """Port of extractBurstFrequency_Final.m. Returns StartTime (N), burstFreq (N-1),
    sp_per_burst, cyclePeriod (N-1), burstDuration (N-1), after the deposited outlier removal.

    As in the deposited code, the removal deletes StartTime(P) together with burstFreq(P), so the
    cycle before a removed one keeps its own period while the next start kept is two or more
    bursts later. With return_gaps, a sixth array (N-1) marks these cycles (True where the next
    start kept is not the next burst detected)."""
    s = np.asarray(spikes, float)
    n = len(s)
    # MATLAB 1-based indices are kept below and converted at the end.
    burst_end = []
    burst_start = [1]
    startidx = 1
    gaps = np.nonzero(np.diff(s) > min_time_bw_bursts)[0] + 1  # 1-based ii with s(ii+1)-s(ii) > thr
    for ii in gaps:
        burst_end.append(int(ii))
        if burst_end[-1] - startidx < min_sp_per_burst - 1:
            burst_start = burst_start[:-1]
            burst_end = burst_end[:-1]
        else:
            startidx = int(ii) + 1
        burst_start.append(startidx)
    bs = np.array(burst_start) - 1
    be = np.array(burst_end, dtype=int) - 1
    sp_per_burst = be - bs[:-1] + 1
    start = s[bs]
    period = np.diff(start)
    freq = 1.0 / period
    dur = s[be] - s[bs[:-1]]
    orig = np.arange(len(start))
    while True:
        remove = []
        L = len(freq)
        for P in range(11, L - 10 + 1):  # MATLAB P = 11 : length(burstFreq)-10
            p = P - 1
            past = np.nanmean(np.abs(np.diff(freq[p - 10 : p - 4])))
            fut = np.nanmean(np.abs(np.diff(freq[p + 5 : p + 11])))
            if abs(freq[p] - freq[p - 1]) > 3 * past and abs(freq[p] - freq[p + 1]) > 3 * fut:
                remove.append(p)
        if not remove:
            break
        keep = np.ones(len(start), bool)
        keep[remove] = False
        start = start[keep]
        orig = orig[keep]
        k2 = keep[: len(freq)]
        freq, period, dur, sp_per_burst = freq[k2], period[k2], dur[k2], sp_per_burst[k2]
    if return_gaps:
        return start, freq, sp_per_burst, period, dur, np.diff(orig) > 1
    return start, freq, sp_per_burst, period, dur


def phase_calc(spikes, max_isi, pd_starts, pd_cp, pd_dur):
    """Port of Phase_Calc.m. For each PD cycle i (0 .. N-2): onset phase, offset phase, duty cycle
    and the onset/offset latencies in s of the longest run of the neuron's spikes in the cycle."""
    s = np.asarray(spikes, float)
    m = len(pd_starts) - 1
    on = np.full(m, np.nan)
    off = np.full(m, np.nan)
    duty = np.full(m, np.nan)
    lat_on = np.full(m, np.nan)
    lat_off = np.full(m, np.nan)
    if len(s) == 0:
        return on, off, duty, lat_on, lat_off
    lo = np.searchsorted(s, pd_starts[:-1], side="left")
    hi = np.searchsorted(s, pd_starts[1:], side="left")
    for i in range(m):
        if hi[i] <= lo[i]:
            continue
        seg = s[lo[i] : hi[i]]
        if len(seg) == 1:
            a, b = 0, 0
        else:
            brk = np.nonzero(np.diff(seg) > max_isi)[0] + 1
            starts = np.concatenate([[0], brk])
            lengths = np.diff(np.concatenate([starts, [len(seg)]]))
            j = int(np.argmax(lengths))
            a, b = starts[j], starts[j] + lengths[j] - 1
        lat_on[i] = seg[a] - pd_starts[i]
        lat_off[i] = seg[b] - pd_starts[i]
        on[i] = lat_on[i] / pd_cp[i]
        off[i] = lat_off[i] / pd_cp[i]
        duty[i] = (seg[b] - seg[a]) / pd_cp[i]
    return on, off, duty, lat_on, lat_off


def cycle_temperature(starts, x_sub, tempsub):
    """Mean Tempsub over samples with x_sub*60 strictly between consecutive burst starts, excluding
    the last sample of Tempsub (CalculateFrequencyPhaseEtc.m). Returns N-1 values."""
    t = x_sub * 60.0
    nT = len(tempsub)
    lo = np.searchsorted(t, starts[:-1], side="right")
    hi = np.searchsorted(t, starts[1:], side="left")
    hi = np.minimum(hi, nT - 1)
    out = np.full(len(starts) - 1, np.nan)
    good = ~np.isnan(tempsub)
    cs = np.concatenate([[0.0], np.cumsum(np.where(good, tempsub, 0.0))])
    cn = np.concatenate([[0], np.cumsum(good)])
    for i in range(len(out)):
        a, b = lo[i], hi[i]
        if b > a and cn[b] - cn[a] > 0:
            out[i] = (cs[b] - cs[a]) / (cn[b] - cn[a])
    return out


def condition_mask(starts, file_times, start_idx, end_idx):
    """Cycles (by first PD spike) with fileTimes(start+1) < t < fileTimes(end+2) in MATLAB indexing."""
    return (starts > file_times[start_idx]) & (starts < file_times[min(end_idx + 1, len(file_times) - 1)])


def analyse(expt: str, pd_key: str = "PD") -> dict:
    """Per-cycle measures of one experiment: start, freq, period, PD burst duration, temperature,
    and onset/offset phases and latencies of PD, LP and PY."""
    d = load_spikes(expt)
    start, freq, spb, period, dur, gap = extract_bursts(d[pd_key], 0.2, 2, return_gaps=True)
    temp = cycle_temperature(start, d["x_sub"], d["Tempsub"])
    cyc = {"start": start[:-1], "freq": freq, "period": period, "pd_dur": dur, "temp": temp, "gap": gap}
    _, pd_off, _, _, pd_lat_off = phase_calc(d[pd_key], 0.11, start, period, dur)
    cyc["PD_OFF"] = pd_off
    for nrn in ("LP", "PY"):
        if nrn in d and len(d[nrn]):
            on, off, duty, lon, loff = phase_calc(d[nrn], 0.11, start, period, dur)
        else:
            on = off = duty = lon = loff = np.full(len(freq), np.nan)
        cyc[f"{nrn}_ON"], cyc[f"{nrn}_OFF"], cyc[f"{nrn}_duty"] = on, off, duty
        cyc[f"{nrn}_lat_on"] = lon
        cyc[f"{nrn}_lat_off"] = loff
    d["cycles"] = cyc
    d["all_starts"] = start
    return d


def matlab_smooth(y, span):
    """MATLAB smooth(y, span) with the default moving average: span reduced to odd, centred,
    the window shrinking symmetrically at both ends."""
    y = np.asarray(y, float)
    n = len(y)
    span = int(span)
    if span % 2 == 0:
        span -= 1
    span = min(span, n if n % 2 else n - 1)
    h = (span - 1) // 2
    out = np.empty(n)
    cs = np.concatenate([[0.0], np.cumsum(y)])
    for i in range(n):
        k = min(h, i, n - 1 - i)
        out[i] = (cs[i + k + 1] - cs[i - k]) / (2 * k + 1)
    return out


def trailing_mean(y, span):
    """Trailing moving average over up to `span` cycles (variant of O3)."""
    y = np.asarray(y, float)
    cs = np.concatenate([[0.0], np.cumsum(y)])
    i = np.arange(len(y))
    a = np.maximum(0, i - span + 1)
    return (cs[i + 1] - cs[a]) / (i + 1 - a)


def jag_measure(d: dict, cond: str, centred: bool = True, span: str = "window", up_thr=0.01, f_thr=0.002,
                smooth_within: bool = False):
    """Percent of temperature-increasing cycles with a smoothed frequency decrease, and percent of
    temperature-stable cycles with an increase, in one condition window.

    span "window": the cycles of the Timings window (as ProbabilityUpDown.m), stable meaning
    |dT| < 0.01 (the deposited code and the Figure 3A legend); span "steps": only cycles from the
    first 11 degrees C hold to the end of the 21 degrees C hold, stable meaning dT <= 0.01 (every
    cycle that did not warm, the Methods' wording), O3 (a); span "recording": the Timings window
    extended to the first cycle back within 0.3 degrees C of 11 degrees C after it (the cooling,
    which precedes the solution change, Methods, Temperature protocol) or to the next condition's
    window, stable meaning dT <= 0.01, O3 (b). smooth_within: smooth only the cycles of the span
    (a variant; the deposited code smooths the whole recording, across condition boundaries)."""
    c = d["cycles"]
    temp, freq, st = c["temp"], c["freq"], c["start"]
    sm = matlab_smooth if centred else trailing_mean
    s_idx, e_idx = d["Timings"][cond]
    m = condition_mask(st, d["fileTimes"], s_idx[0], e_idx[0])
    if span == "steps":
        idx = np.nonzero(m)[0]
        tt = temp[idx]
        first = idx[np.argmax(np.abs(tt - 11) <= MOE)] if np.any(np.abs(tt - 11) <= MOE) else idx[0]
        hot = idx[np.abs(tt - 21) <= MOE]
        last = hot[-1] if len(hot) else idx[-1]
        m = np.zeros_like(m)
        m[first : last + 1] = True
    elif span == "recording":
        idx = np.nonzero(m)[0]
        w_end = d["fileTimes"][min(e_idx[0] + 1, len(d["fileTimes"]) - 1)]
        nxt = [d["fileTimes"][a[0]] for a, _ in d["Timings"].values() if d["fileTimes"][a[0]] >= w_end]
        stop = min(nxt) if nxt else np.inf
        after = np.nonzero((st > w_end) & (st < stop))[0]
        back = after[np.abs(temp[after] - 11) <= MOE]
        last = back[0] if len(back) else (after[-1] if len(after) else idx[-1])
        m = np.zeros_like(m)
        m[idx[0] : last + 1] = True
    if smooth_within:
        idx = np.nonzero(m)[0]
        dT = np.full(len(temp) - 1, np.nan)
        dF = np.full(len(temp) - 1, np.nan)
        dT[idx[:-1]] = np.diff(sm(temp[idx], 10))
        dF[idx[:-1]] = np.diff(sm(freq[idx], 30))
    else:
        dT = np.diff(sm(temp, 10))
        dF = np.diff(sm(freq, 30))
    m = m[: len(dT)]
    if span in ("steps", "recording"):
        stable = m & (dT <= up_thr)
    else:
        stable = m & (dT < up_thr) & (dT > -up_thr)
    up = m & (dT > up_thr)
    dec = np.sum(up & (dF < -f_thr)) / max(np.sum(up), 1) * 100
    inc = np.sum(stable & (dF > f_thr)) / max(np.sum(stable), 1) * 100
    return dec, inc, int(np.sum(up)), int(np.sum(stable))


def hold_means(d: dict, cond: str, which: str = "all", min_freq: float = 1 / 8, strict_cs: bool = False, moe: float = MOE,
               drop_gaps: bool = True):
    """Per-target-temperature means of the per-cycle measures in a condition window.

    strict_cs: a strict bound |T - target| < moe, which the deposited CalculateFrequencyPhaseEtc.m
    uses for the Cs+ frequency and temperature (its phases, and every saline measure, use <=).
    drop_gaps: leave out the cycles left by the outlier removal before a removed cycle
    (extract_bursts), whose phases are divided by the period of a different cycle. This is an
    assumption: the deposited code keeps them, but leaving them out brings the phases far closer to
    the deposited SummaryStatistics.mat (checked in the notebook); drop_gaps=False is the variant.

    which: "all" = every cycle within 0.3 C of the target in the window (deposited code);
    "first" = for 11 C only the cycles from the first one within 0.3 C of 11 C to the first one
    above 12 C after it (the first hold, O2);
    "return" = for 11 C only the cycles after the last one within 0.3 C of 21 C."""
    c = d["cycles"]
    s_idx, e_idx = d["Timings"][cond]
    m = np.zeros(len(c["freq"]), bool)
    for a, b in zip(s_idx, e_idx):
        m |= condition_mask(c["start"], d["fileTimes"], a, b)
    m &= c["freq"] > min_freq
    if drop_gaps:
        m &= ~c["gap"]
    idx = np.nonzero(m)[0]
    temp = c["temp"][idx]
    keys = ["freq", "period", "pd_dur", "temp", "PD_OFF", "LP_ON", "LP_OFF", "PY_ON", "PY_OFF", "LP_duty", "LP_lat_on", "PY_lat_on", "LP_lat_off"]
    out = {k: np.full(len(TARGETS), np.nan) for k in keys}
    out["n"] = np.zeros(len(TARGETS), int)
    out["cycle_index"] = {}
    for j, T in enumerate(TARGETS):
        sel = np.abs(temp - T) < moe if strict_cs else np.abs(temp - T) <= moe
        if T == 11 and which != "all":
            pos = np.arange(len(idx))
            above12 = np.nonzero(temp > 12)[0]
            near21 = np.nonzero(np.abs(temp - 21) <= MOE)[0]
            if which == "first":
                near11 = np.nonzero(np.abs(temp - 11) <= MOE)[0]
                first11 = near11[0] if len(near11) else 0
                later = above12[above12 > first11]
                cut = later[0] if len(later) else len(idx)
                sel &= pos < cut
            elif which == "return":
                cut = near21[-1] if len(near21) else len(idx)
                sel &= pos > cut
        ii = idx[sel]
        out["cycle_index"][int(T)] = ii
        out["n"][j] = len(ii)
        for k in keys:
            if len(ii):
                with np.errstate(all="ignore"):
                    out[k][j] = np.nanmean(c[k][ii]) if np.any(~np.isnan(c[k][ii])) else np.nan
    return out


def q10(temps, freqs, reading: str = "a"):
    """Q10 from the six holding-temperature means. (a) nonlinear least squares of
    f = f11 * Q10**((T-11)/10); (b) log10 f linear in T, Q10 = 10**(10*slope) (deposited code);
    (c) (f21/f11)**(10/10)."""
    from scipy.optimize import curve_fit

    T = np.asarray(temps, float)
    f = np.asarray(freqs, float)
    if reading == "c":
        # the six values are the means at 11, 13, ..., 21 C; (f21/f11)**(10/10)
        return f[-1] / f[0]
    ok = ~np.isnan(T) & ~np.isnan(f) & (f > 0)
    T, f = T[ok], f[ok]
    if len(f) < 2:
        return np.nan
    b = np.polyfit(T, np.log10(f), 1)[0]
    if reading == "b":
        return 10 ** (10 * b)
    p0 = [f[0], 10 ** (10 * b)]
    try:
        p, _ = curve_fit(lambda t, f11, q: f11 * q ** ((t - 11) / 10), T, f, p0=p0, maxfev=10000)
        return p[1]
    except Exception:
        return np.nan


def rm_anova(Y):
    """One-way repeated-measures ANOVA on an (subjects x conditions) array, complete rows only.
    Returns F, df1, df2, p, MSE, n."""
    Y = np.asarray(Y, float)
    Y = Y[~np.isnan(Y).any(axis=1)]
    n, k = Y.shape
    gm = Y.mean()
    ss_cond = n * np.sum((Y.mean(0) - gm) ** 2)
    ss_subj = k * np.sum((Y.mean(1) - gm) ** 2)
    ss_tot = np.sum((Y - gm) ** 2)
    ss_err = ss_tot - ss_cond - ss_subj
    df1, df2 = k - 1, (k - 1) * (n - 1)
    F = (ss_cond / df1) / (ss_err / df2)
    return F, df1, df2, stats.f.sf(F, df1, df2), ss_err / df2, n


def tukey_rm(Y, names):
    """Pairwise Tukey comparisons after a one-way RM ANOVA, under the two O5 readings.
    (a) MATLAB multcompare on a fitrm model: SE of each difference from the paired differences,
    studentized range with k groups and n-1 df; (b) classic Tukey HSD with the ANOVA's
    within-subject MSE and (k-1)(n-1) df. Returns a list of dicts."""
    Y = np.asarray(Y, float)
    Y = Y[~np.isnan(Y).any(axis=1)]
    n, k = Y.shape
    _, _, df2, _, mse, _ = rm_anova(Y)
    out = []
    for i in range(k):
        for j in range(i + 1, k):
            dlt = Y[:, i] - Y[:, j]
            md = dlt.mean()
            se_a = dlt.std(ddof=1) / np.sqrt(n)
            pa = stats.studentized_range.sf(abs(md) / se_a * np.sqrt(2), k, n - 1)
            pb = stats.studentized_range.sf(abs(md) / np.sqrt(mse / n), k, df2)
            out.append({"pair": f"{names[i]} - {names[j]}", "diff": md, "p_multcompare": pa, "p_classic": pb})
    return out


def sw_test(x, y=None):
    """Shapiro-Wilk p of x (or of x - y), NaNs dropped."""
    v = np.asarray(x, float) if y is None else np.asarray(x, float) - np.asarray(y, float)
    v = v[~np.isnan(v)]
    return stats.shapiro(v).pvalue if len(v) >= 3 else np.nan


def paired(x, y):
    """Paired t-test and Wilcoxon signed-rank on complete pairs; returns dict."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ok = ~np.isnan(x) & ~np.isnan(y)
    x, y = x[ok], y[ok]
    t = stats.ttest_rel(x, y)
    w = stats.wilcoxon(x, y)
    return {"n": int(ok.sum()), "mean_x": x.mean(), "sd_x": x.std(ddof=1), "mean_y": y.mean(), "sd_y": y.std(ddof=1),
            "mean_diff": (x - y).mean(), "t": t.statistic, "p_t": t.pvalue, "p_w": w.pvalue, "sw_diff": sw_test(x - y)}


def raw_channels(expt: str) -> list:
    """Channel names (nerve_names) of Raw_Expt_<expt>.mat, without reading the traces."""
    import h5py
    import scipy.io as sio

    path = DATA_DIR / f"Raw_Expt_{expt}.mat"
    try:
        with h5py.File(path, "r") as h:
            return ["".join(chr(c) for c in np.ravel(h[r][()])) for r in np.ravel(h["nerve_names"][()])]
    except OSError:
        d = sio.loadmat(path, variable_names=["nerve_names"])
        return [str(np.ravel(x)[0]) for x in np.ravel(d["nerve_names"])]


def raw_trace(expt: str, channel: str, t0: float, t1: float, fs: float = 10_000.0):
    """Slice of channel `channel` of Raw_Expt_<expt>.mat between t0 and t1 s (10 kHz, Methods,
    Analysis; sample 0 at t = 0 of the spike times, checked in the notebook). v7.3 files are read
    with h5py slices; v5 files are loaded whole and sliced."""
    import h5py
    import scipy.io as sio

    path = DATA_DIR / f"Raw_Expt_{expt}.mat"
    a, b = int(round(t0 * fs)), int(round(t1 * fs))
    try:
        h = h5py.File(path, "r")
    except OSError:
        d = sio.loadmat(path)
        names = [str(np.ravel(x)[0]) for x in np.ravel(d["nerve_names"])]
        x = np.ravel(d["whole_traces"][0, names.index(channel)])
        n = len(x)
        out = x[a:b].copy()
        del d, x
        return out, n
    with h:
        names = ["".join(chr(c) for c in np.ravel(h[r][()])) for r in np.ravel(h["nerve_names"][()])]
        ref = np.ravel(h["whole_traces"][()])[names.index(channel)]
        ds = h[ref]
        n = ds.shape[1]
        return np.asarray(ds[0, a:b]), n


def step_onset(cyc: dict, mask: np.ndarray, t_from: float, t_to: float, hold_end: bool = False):
    """Index of the first cycle of the warming from t_from toward t_to within `mask`: going back
    from the first cycle above t_from + 0.3 C to the last cycle whose centred 10-cycle smoothed
    temperature did not rise by more than 0.01 C (the paper's increasing-temperature criterion).
    The crossing taken is the first one after which the temperature reaches t_to - 0.3 C without
    falling back below t_from, so that a brief rise during the hold is not taken for the step.
    hold_end: the crossing taken is the first one after the last cycle within 0.3 C of t_from
    before t_to - 0.3 C is reached, so that every cycle of the hold, brief rises above
    t_from + 0.3 C included, comes before the onset (the end of the holding period, O4 b)."""
    idx = np.nonzero(mask)[0]
    temp = cyc["temp"][idx]
    sm = matlab_smooth(cyc["temp"], 10)
    dT = np.diff(sm, append=sm[-1])
    hold = np.nonzero(np.abs(temp - t_from) <= MOE)[0]
    if not len(hold):
        return None
    pos = np.arange(len(idx))
    reach = np.nonzero((pos > hold[0]) & (temp >= t_to - MOE))[0]
    if not len(reach):
        return None
    back = np.nonzero((pos > hold[0]) & (pos < reach[0]) & ((temp <= t_from + MOE) if hold_end else (temp < t_from)))[0]
    after = np.nonzero((pos > (back[-1] if len(back) else hold[0])) & (temp > t_from + MOE))[0]
    if not len(after):
        return None
    k = idx[after[0]]
    while k > idx[hold[0]] and dT[k - 1] > 0.01:
        k -= 1
    return k


def trace_spikes(v, fs: float = 10_000.0, height: float = -40.0, prominence: float = 10.0):
    """Spike times (s from the trace's first sample) on an intracellular trace, for the one
    example with no deposited spike times (Raw_Expt_981_037.mat): peaks above `height` mV standing
    `prominence` mV above their surroundings, at least 2 ms apart. A standard choice, checked in
    the notebook against the trace (spikes reach about -27 mV from a trough near -70 mV)."""
    from scipy.signal import find_peaks

    pk, _ = find_peaks(np.asarray(v, float), height=height, prominence=prominence, distance=int(0.002 * fs))
    return pk / fs
