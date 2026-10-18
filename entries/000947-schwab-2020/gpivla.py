"""Loading and measures for the pre-MPTP GPi and VLa recordings of dandiset 000947.

Schwab, Kase, Zimnik, Rosenbaum, Codianni, Rubin & Turner (2020), PLOS Biology,
doi:10.1371/journal.pbio.3000829.

Each NWB file holds one recording block of one monkey (Gaia or Isis): a trials table (cue onset,
movement onset and end, target, and in some files error onset), the curated single units in
`units` (spike times in seconds, a location label, channel id and sort letter), all sorted
clusters in `processing/ecephys/units`, and raw and 200 Hz high-pass filtered traces. Files are
streamed from the archive at the pinned version; nothing is written to disk. Only the curated
`units` table and the trials are read, except for the action potential width, which reads one
chunk of the filtered traces per unit.

Where the parameters come from:

- Paper's Methods: valid trials exclude errors and outliers in reaction time or movement duration
  (more than 6 median absolute differences from the mean); a unit needs at least 10 valid trials
  (applied here per direction); its mean rate over the recording must be at least 30 spikes/s in
  GPi and 1 spike/s in VLa; spike density functions (SDF) use a Gaussian kernel of 25 ms at 1 ms
  resolution; decreases are detected on the interspike interval (ISI) function, the current ISI
  at each ms smoothed with the same kernel; the control period is the 700 ms ending at the median
  cue onset, the test period the 700 ms after it; a linear trend fitted to the control period is
  removed; a change must last at least 70 ms at an omnibus p < 0.001 (Bonferroni). Correlation
  windows: rest 1.5 to 1.0 s before movement onset, movement 0.2 s before to 0.3 s after; CCFs in
  2 ms bins shifted by 1 ms, jitter of 20 ms, peaks in 0 to 10 ms after a 2 ms moving average; noise
  correlations on 500 ms spike counts, bins with fewer than 10 spikes in total left out, trials
  with |z| > 3 removed, 400 shuffles; bursts and pauses by the Poisson surprise method (surprise
  at least 5, bursts of at least 3 spikes at twice the baseline rate, pauses of at least 100 ms),
  outside the task (0.4 s before movement onset to 0.8 s after the return to the home key); VLa
  SDF with a 10 ms kernel, from 0.8 s before to 0.8 s after each event.
- Paper's code (Dryad doi:10.5061/dryad.0cfxpnvxm, mirrored on Zenodo record 4000719):
  `PeriEventChange_SDF_pctchng.m` fixes the threshold, p = alpha / (control length / 70) and
  threshold = norminv(1 - p) times the SD of the control, the test period of control length + 1
  samples, the first run of 70 consecutive supra-threshold samples as onset, and the offset as a
  return within threshold for 70 samples or a change of sign; `Fig2_3_S8_S9.m` fixes the window
  (-1500 to +1000 ms from movement onset), the rest rate as the mean SDF from -1500 to -301 ms, and
  the integrated change as the summed SDF minus that mean from -300 to +399 ms; `Fig4_S10to13.m`
  fixes the CCF lags (-20 to +20 ms) and that each pair is significant when its peak exceeds the
  95th percentile of its own jittered controls.
- The Methods define the surprise as S = -log(P); the natural log is used, as `log` is in the
  paper's MATLAB. (A first run used log10, which gave bursts far longer than the paper's; the
  notebook shows the burst durations with log10 as a variant.)
- Common choices, where neither says: the VLa spikes are the ones jittered; the Poisson
  probability for a burst uses the unit's mean rest rate.
"""

from __future__ import annotations

import re
import time
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats
from scipy.ndimage import gaussian_filter1d
from scipy.fft import irfft, next_fast_len, rfft
from scipy.special import gammainc

DANDISET_ID = "000947"
DANDISET_VERSION = "0.240510.2211"

WIN = (-1500, 1000)            # ms around movement onset (Fig2_3_S8_S9.m, IND_OFFSET = 1500)
NWIN = WIN[1] - WIN[0] + 1     # 2501 samples
SIGMA_MS = 25.0                # SDF and ISI kernel (Methods)
CNTL_MS = 700                  # control and test period length (Methods)
CONTIG = 70                    # ms a change must last (Methods)
ALPHA = 0.001                  # omnibus p (Methods)
MIN_TRIALS = 10                # per direction (Methods: 10 valid trials)
MIN_RATE = {"GPi": 30.0, "VLa": 1.0}   # spikes/s over the recording (Methods)
OUTLIER_MADS = 6.0             # Methods: > 6 median absolute differences from the mean
REST_WIN = (-1.5, -1.0)        # s from movement onset (Methods, correlations)
MVT_WIN = (-0.2, 0.3)
TASK_EXCL = (-0.4, 0.8)        # s: from movement onset, to after return end (Methods, bursts)


# --- loading -------------------------------------------------------------------------------

def area(label) -> str:
    """The dandiset's location label with case unified (GPI and GPi, VLA and VLa)."""
    text = "" if label is None else str(label)
    return {"GPI": "GPi", "VLA": "VLa", "VLP": "VLp", "GPE": "GPe"}.get(text.upper(), text)


def file_key(session_id: str) -> str:
    """'pre-MPTP-G-140511-3' -> 'G_140511_3', the file name used in the paper's code."""
    return re.sub(r"^(pre|post)-MPTP-", "", session_id).replace("-", "_")


def asset_urls(pre_only: bool = True) -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        out = sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                     for a in dandiset.get_assets() if a.path.endswith(".nwb"))
    return [p for p in out if not pre_only or "ses-pre-MPTP" in p[0]]


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def _open(url: str, tries: int = 4):
    for k in range(tries):
        try:
            return h5py.File(remfile.File(url), "r")
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(2 + 3 * k)


def load_session(path: str, url: str) -> dict:
    """Trials, curated units and metadata of one file."""
    f = _open(url)
    g = f["general"]
    s = {"path": path, "url": url, "session_id": _s(g["session_id"][()]),
         "subject": _s(g["subject/subject_id"][()]),
         "mptp": _s(g["MPTPMetaData"].attrs.get("MPTP_status", "")),
         "session_start": _s(f["session_start_time"][()]),
         "related_publications": [_s(x) for x in g["related_publications"][:]]
         if "related_publications" in g else [],
         "groups": {k: _s(v.attrs.get("location")) for k, v in g["extracellular_ephys"].items()
                    if k != "electrodes"}}
    s["key"] = file_key(s["session_id"])
    if "intervals" in f and "trials" in f["intervals"]:
        tr = f["intervals/trials"]
        df = pd.DataFrame({c: tr[c][:] for c in tr.attrs["colnames"]})
        df["target"] = df["target"].map(_s)
        s["trials"] = df
    else:
        s["trials"] = None
    units = []
    if "units" in f:
        u = f["units"]
        cols = list(u.attrs["colnames"])
        index = u["spike_times_index"][:]
        times = u["spike_times"][:]
        lo = 0
        for i in range(len(index)):
            row = {c: _s(u[c][i]) for c in cols if c != "spike_times"}
            row["spikes"] = np.sort(times[lo:index[i]])
            row["sorted_in_file"] = bool(np.all(np.diff(times[lo:index[i]]) >= 0))
            lo = index[i]
            units.append(row)
    s["units"] = units
    el = g["extracellular_ephys/electrodes"]
    s["electrodes"] = pd.DataFrame({"channel_ids": [_s(x) for x in el["channel_ids"][:]],
                                    "location": [_s(x) for x in el["location"][:]],
                                    "group_name": [_s(x) for x in el["group_name"][:]],
                                    **{c: el[c][:] for c in ("acx_x", "acx_y", "acx_z") if c in el}})
    proc = {}
    if "processing" in f and "ecephys" in f["processing"] and "Processed" in f["processing/ecephys"]:
        for name, es in f["processing/ecephys/Processed"].items():
            proc[name] = {"electrodes": es["electrodes"][:], "shape": es["data"].shape,
                          "chunks": es["data"].chunks,
                          "rate": float(es["starting_time"].attrs["rate"]),
                          "start": float(es["starting_time"][()])}
    s["processed"] = proc
    s["n_raw"] = f["acquisition/ElectricalSeries/data"].shape[0] if "ElectricalSeries" in f.get("acquisition", {}) else 0
    f.close()
    return s


def load_all(paths=None, workers: int = 16) -> list[dict]:
    """Load the pre-MPTP files (or the given (path, url) pairs) in parallel."""
    pairs = asset_urls() if paths is None else paths
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda pu: load_session(*pu), pairs))


# --- trials --------------------------------------------------------------------------------

def _outliers(x: np.ndarray) -> np.ndarray:
    """Methods: values more than 6 median absolute differences away from the mean."""
    x = np.asarray(x, float)
    ok = np.isfinite(x)
    if ok.sum() < 3:
        return np.zeros(len(x), bool)
    mad = np.median(np.abs(x[ok] - np.median(x[ok])))
    return ok & (np.abs(x - np.mean(x[ok])) > OUTLIER_MADS * mad)


def valid_trials(trials: pd.DataFrame) -> pd.DataFrame:
    """Trials with RT and MT, and the flag `valid`: no error, a target, cue and movement onset,
    and RT and MT (where the file has movement ends) not outliers within the file."""
    df = trials.copy()
    df["rt"] = df["movement_start_time"] - df["cue_onset_time"]
    df["mt"] = (df["movement_stop_time"] - df["movement_start_time"]) if "movement_stop_time" in df else np.nan
    err = df["error_onset_time"].notna() if "error_onset_time" in df else pd.Series(False, index=df.index)
    ok = (~err) & df["target"].isin(["Left", "Right"]) & df["rt"].notna() & (df["rt"] > 0)
    df["error"] = err
    out = pd.Series(False, index=df.index)
    out[ok] = _outliers(df.loc[ok, "rt"].to_numpy()) | _outliers(df.loc[ok, "mt"].to_numpy())
    df["outlier"] = out
    df["valid"] = ok & ~out
    return df


# --- activity functions --------------------------------------------------------------------

def _grid(align: np.ndarray, pad: int = 0) -> np.ndarray:
    ms = np.arange(WIN[0] - pad, WIN[1] + pad + 1) / 1000.0
    return np.asarray(align)[:, None] + ms[None, :]


def spike_counts_ms(spikes: np.ndarray, align: np.ndarray, pad: int = 100) -> np.ndarray:
    """Spike counts in 1 ms bins (trials x time) from WIN[0]-pad to WIN[1]+pad ms."""
    edges = np.arange(WIN[0] - pad, WIN[1] + pad + 2) / 1000.0
    out = np.zeros((len(align), len(edges) - 1))
    for i, a in enumerate(align):
        lo, hi = np.searchsorted(spikes, [a + edges[0], a + edges[-1]])
        out[i] = np.histogram(spikes[lo:hi] - a, edges)[0]
    return out


def sdf(spikes: np.ndarray, align: np.ndarray, sigma: float = SIGMA_MS) -> np.ndarray:
    """Mean spike density (spikes/s) over trials, -1500 to +1000 ms, Gaussian kernel."""
    pad = int(4 * sigma)
    c = spike_counts_ms(spikes, align, pad).mean(0) * 1000.0
    return gaussian_filter1d(c, sigma, mode="nearest")[pad:-pad]


def isi_function(spikes: np.ndarray, align: np.ndarray, sigma: float = SIGMA_MS) -> np.ndarray:
    """Mean over trials of the current interspike interval (ms) at each ms, smoothed."""
    pad = int(4 * sigma)
    t = _grid(align, pad)
    idx = np.searchsorted(spikes, t, side="right")
    ok = (idx > 0) & (idx < len(spikes))
    isi = np.full(t.shape, np.nan)
    isi[ok] = (spikes[np.minimum(idx[ok], len(spikes) - 1)] - spikes[idx[ok] - 1]) * 1000.0
    m = np.nanmean(isi, 0)
    m = pd.Series(m).interpolate(limit_direction="both").to_numpy()
    return gaussian_filter1d(m, sigma, mode="nearest")[pad:-pad]


# --- detection of peri-movement changes ----------------------------------------------------

def control_fit(func: np.ndarray, cue_idx: int):
    """OLS line over the 700 ms control period; returns (intercept, slope per ms, slope 95% CI)."""
    x = np.arange(cue_idx - CNTL_MS, cue_idx)
    y = func[x]
    res = stats.linregress(x, y)
    tcrit = stats.t.ppf(0.975, len(x) - 2)
    return res.intercept, res.slope, (res.slope - tcrit * res.stderr, res.slope + tcrit * res.stderr)


def detect(func: np.ndarray, median_rt_ms: float, alpha: float = ALPHA, contig: int = CONTIG,
           detrend: bool = True) -> dict:
    """Increase of `func` above its control period, as PeriEventChange_SDF_pctchng.m with
    incr_decr = +1, after removing the control period's linear trend (Methods).

    Returns onset and offset (ms from movement onset, NaN when none), the mean change over the
    response, the control slope per s and whether its 95% CI excludes zero, and the threshold."""
    cue_idx = int(round(-WIN[0] - median_rt_ms))
    b0, b1, ci = control_fit(func, cue_idx)
    data = func - (b0 + b1 * np.arange(len(func))) if detrend else func.copy()
    cntl = data[cue_idx - CNTL_MS:cue_idx]
    data = data - cntl.mean()
    p = alpha / (CNTL_MS / contig)
    thr = stats.norm.ppf(1 - p) * np.std(cntl, ddof=1)
    test = data[cue_idx:cue_idx + CNTL_MS + 1]
    out = {"onset": np.nan, "offset": np.nan, "mean_change": np.nan, "thr": thr,
           "slope_per_s": b1 * 1000.0, "slope_sig": bool(ci[0] > 0 or ci[1] < 0)}
    above = test > thr
    run = np.convolve(above.astype(int), np.ones(contig, int), "valid")
    hits = np.flatnonzero(run == contig)
    if len(hits) == 0:
        return out
    on = cue_idx + hits[0]
    after = data[on + 1:]
    inside = np.abs(after) < thr
    run2 = np.convolve(inside.astype(int), np.ones(contig, int), "valid")
    z = np.flatnonzero(run2 == contig)
    sw = np.flatnonzero((np.sign(after) < 0) & (np.abs(after) > thr))
    cands = ([z[0] + on + 1] if len(z) else []) + ([sw[0] + on + 1] if len(sw) else [])
    off = min(cands) if cands else len(data) - 1
    out.update(onset=on + WIN[0], offset=off + WIN[0], mean_change=float(data[on:off + 1].mean()))
    return out


def unit_direction(segments: list[tuple[np.ndarray, pd.DataFrame]], target: str) -> dict | None:
    """Detection for one unit and one target over its recording segments (each a spike train and
    its file's valid trials). Returns None when there are fewer than MIN_TRIALS valid trials."""
    counts, isis, rts = [], [], []
    for spikes, tr in segments:
        t = tr[tr.valid & (tr.target == target)]
        if len(t) == 0:
            continue
        align = t["movement_start_time"].to_numpy()
        counts.append(spike_counts_ms(spikes, align, int(4 * SIGMA_MS)))
        pad = int(4 * SIGMA_MS)
        g = _grid(align, pad)
        idx = np.searchsorted(spikes, g, side="right")
        ok = (idx > 0) & (idx < len(spikes))
        isi = np.full(g.shape, np.nan)
        isi[ok] = (spikes[np.minimum(idx[ok], len(spikes) - 1)] - spikes[idx[ok] - 1]) * 1000.0
        isis.append(isi)
        rts.append(t["rt"].to_numpy())
    n = sum(len(c) for c in counts)
    if n < MIN_TRIALS:
        return None
    pad = int(4 * SIGMA_MS)
    c = np.vstack(counts)
    f_sdf = gaussian_filter1d(c.mean(0) * 1000.0, SIGMA_MS, mode="nearest")[pad:-pad]
    m = pd.Series(np.nanmean(np.vstack(isis), 0)).interpolate(limit_direction="both").to_numpy()
    f_isi = gaussian_filter1d(m, SIGMA_MS, mode="nearest")[pad:-pad]
    med_rt = float(np.median(np.concatenate(rts))) * 1000.0
    inc, dec = detect(f_sdf, med_rt), detect(f_isi, med_rt)
    base = f_sdf[:1200].mean()                      # Fig2_3_S8_S9.m: -1500 to -301 ms
    integ = (f_sdf[1200:1900] - base).sum() / 1000  # -300 to +399 ms, spikes
    return {"n_trials": n, "median_rt_ms": med_rt, "sdf": f_sdf, "rest_rate": base,
            "integrated": integ, "inc_onset": inc["onset"], "dec_onset": dec["onset"],
            "inc_change": inc["mean_change"], "dec_change": dec["mean_change"],
            "slope_per_s2": inc["slope_per_s"], "slope_sig": inc["slope_sig"],
            "trial_counts": c[:, pad:-pad]}


def response_form(inc: float, dec: float) -> str:
    """'increase', 'decrease', 'inc_first', 'dec_first' or 'none' (Fig2_3_S8_S9.m)."""
    i, d = np.isfinite(inc), np.isfinite(dec)
    if i and d:
        return "inc_first" if inc <= dec else "dec_first"
    return "increase" if i else ("decrease" if d else "none")


# --- correlations --------------------------------------------------------------------------

CCF_LAGS = np.arange(-20, 21)            # ms, bin centres; 2 ms bins shifted by 1 ms


def _in_windows(t: np.ndarray, windows: np.ndarray) -> np.ndarray:
    idx = np.searchsorted(windows[:, 0], t, side="right") - 1
    ok = idx >= 0
    ok[ok] = t[ok] < windows[idx[ok], 1]
    return ok


def _bins(gpi: np.ndarray, vla: np.ndarray, reach: float = 0.0215):
    """Index pairs (GPi spike, VLa spike) whose 20 ms jitter window can fall within `reach` s of
    each other, with the start of the VLa spike's window and its offset in it."""
    w = np.floor(vla / 0.020) * 0.020
    lo = np.searchsorted(w, gpi - reach - 0.020)
    hi = np.searchsorted(w, gpi + reach, side="right")
    n = hi - lo
    gi = np.repeat(np.arange(len(gpi)), n)
    vj = (np.repeat(lo - np.cumsum(np.r_[0, n[:-1]]), n) + np.arange(n.sum())).astype(int)
    return gi, vj, w


def _lag_counts(d: np.ndarray) -> np.ndarray:
    """Counts in 2 ms bins centred on -20..+20 ms (each bin [L-1, L+1) ms)."""
    k = np.floor(d * 1000.0).astype(int) + 21            # 1 ms bins from -21 ms
    c1 = np.bincount(k[(k >= 0) & (k < 42)], minlength=42)
    return c1[:-1] + c1[1:]


def ccf_test(gpi: np.ndarray, vla: np.ndarray, dur: float, rng: np.random.Generator,
             n_surr: int = 400) -> dict:
    """Normalised CCF (Methods: VLa spikes at each lag after GPi spikes over the number of GPi
    spikes times the mean VLa count per bin) at lags -20..+20 ms in 2 ms bins, its jittered controls
    (VLa spikes moved uniformly within fixed 20 ms windows), and the peak of the control-corrected
    CCF in 0..10 ms after a 2 ms moving average, with the 95th percentile of the same peak over the
    controls. A pair is significant when its peak exceeds that percentile (Fig4_S10to13.m)."""
    gi, vj, w = _bins(gpi, vla)
    expected = len(gpi) * len(vla) / dur * 0.002
    real = _lag_counts(vla[vj] - gpi[gi]) / expected
    base = w[vj] - gpi[gi]
    ctrl = np.empty((n_surr, len(CCF_LAGS)))
    for k in range(n_surr):
        u = rng.random(len(vla)) * 0.020
        ctrl[k] = _lag_counts(base + u[vj]) / expected
    mean_ctrl = ctrl.mean(0)
    sel = (CCF_LAGS >= 0) & (CCF_LAGS <= 10)

    def peak(c):
        c = c - mean_ctrl
        c = (c + np.r_[c[0], c[:-1]]) / 2       # 2 ms moving average
        seg = c[sel]
        k = int(np.argmax(np.abs(seg)))
        return np.abs(seg[k]), np.sign(seg[k]), int(CCF_LAGS[sel][k])

    p_real, s_real, lag = peak(real)
    p_ctrl = np.array([peak(c)[0] for c in ctrl])
    thr = np.percentile(p_ctrl, 95)
    return {"peak": p_real, "sign": s_real, "lag_ms": lag, "ctrl_peaks": p_ctrl, "thr95": thr,
            "significant": bool(p_real > thr), "ccf": real - mean_ctrl, "expected": expected}


def min_detectable(expected: float, thr95: float, rng: np.random.Generator, n_sim: int = 400,
                   grid=np.round(np.arange(0.01, 1.001, 0.01), 2)) -> float:
    """Approximation of the Methods' minimum reliably detectable correlation c0: the lowest
    injected peak correlation p for which 95% of simulated peaks exceed the pair's control 95th
    percentile `thr95`. The paper simulates Poisson spike trains matched to each pair; its code
    is not in the deposit. Here the simulation is made on the CCF counts: independent Poisson
    counts with the pair's expected count per 2 ms bin (`expected`), plus an excess at a lag of
    5 ms scaled so that the peak of the smoothed, control-subtracted CCF is p on average. Peaks are
    measured as in `ccf_test`. Returns NaN when no p up to 1 is detectable."""
    sel = (CCF_LAGS >= 0) & (CCF_LAGS <= 10)
    lam = np.full(42, expected / 2.0)                     # 1 ms bins from -21 ms
    inj = np.zeros(42)
    inj[[25, 26]] = expected / 2.0 / 0.75                 # 1 ms bins [4, 5) and [5, 6) ms

    def p5(p):
        c1 = rng.poisson(lam + p * inj, size=(n_sim, 42))
        c = (c1[:, :-1] + c1[:, 1:]) / expected - 1.0
        c = (c + np.c_[c[:, :1], c[:, :-1]]) / 2
        return np.percentile(np.abs(c[:, sel]).max(1), 5)

    lo, hi = 0, len(grid) - 1                              # bisection on the grid
    if p5(grid[hi]) <= thr95:
        return np.nan
    while lo < hi:
        mid = (lo + hi) // 2
        if p5(grid[mid]) > thr95:
            hi = mid
        else:
            lo = mid + 1
    return float(grid[lo])


def ks_permutation(real: np.ndarray, ctrl: np.ndarray) -> float:
    """Fig4_S10to13.m: one-sided KS statistic of the real peaks against the pooled controls,
    compared with the same statistic for each control set against the others. Returns the
    fraction of control statistics larger than the real one (the p-value)."""
    def ks(a, b):
        grid = np.sort(np.concatenate([a, b]))
        fa = np.searchsorted(np.sort(a), grid, side="right") / len(a)
        fb = np.searchsorted(np.sort(b), grid, side="right") / len(b)
        return np.max(fb - fa)               # a shifted right of b
    k = ctrl.shape[1]
    real_stat = ks(real, ctrl[:, :-1].ravel())
    ctrl_stat = np.array([ks(ctrl[:, j], np.delete(ctrl, j, axis=1).ravel()) for j in range(k)])
    return float(np.mean(ctrl_stat > real_stat))


# --- bursts and pauses ---------------------------------------------------------------------

def _poisson_surprise(n_spikes: int, duration: float, rate: float, log=np.log) -> float:
    """-log of the Poisson probability of n or more spikes in `duration` at `rate`."""
    return -log(max(gammainc(n_spikes, rate * duration), 1e-300))


def bursts(spikes: np.ndarray, rate: float, min_surprise: float = 5.0, log=np.log) -> list[tuple[float, float]]:
    """Legendy and Salcman bursts: start at two consecutive ISIs below half the mean ISI, extend
    while the surprise grows (up to 10 spikes beyond its maximum), then trim the start while it
    grows. Kept with surprise >= 5, >= 3 spikes and an intraburst rate >= 2x the baseline.
    `log` is the logarithm of the surprise (natural by default; np.log10 for the variant)."""
    out = []
    if len(spikes) < 3 or rate <= 0:
        return out
    isi = np.diff(spikes)
    half = 0.5 / rate
    i, n = 0, len(spikes)
    while i < n - 2:
        if not (isi[i] < half and isi[i + 1] < half):
            i += 1
            continue
        j = i + 2
        best_j, best_s = j, _poisson_surprise(3, spikes[j] - spikes[i], rate, log)
        k = j
        while k + 1 < n and k + 1 - best_j <= 10:
            k += 1
            s = _poisson_surprise(k - i + 1, spikes[k] - spikes[i], rate, log)
            if s > best_s:
                best_s, best_j = s, k
        a = i
        while best_j - a + 1 > 3:
            s = _poisson_surprise(best_j - a, spikes[best_j] - spikes[a + 1], rate, log)
            if s >= best_s:
                best_s, a = s, a + 1
            else:
                break
        nsp = best_j - a + 1
        dur = spikes[best_j] - spikes[a]
        if best_s >= min_surprise and nsp >= 3 and dur > 0 and (nsp - 1) / dur >= 2 * rate:
            out.append((spikes[a], spikes[best_j]))
        i = best_j + 1
    return out


def pauses(spikes: np.ndarray, rate: float, min_surprise: float = 5.0, min_len: float = 0.1, log=np.log):
    """ISIs of at least 100 ms whose Poisson surprise of zero spikes is at least 5."""
    isi = np.diff(spikes)
    s = rate * isi * log(np.e)                  # -log(exp(-rate * isi))
    k = np.flatnonzero((isi >= min_len) & (s >= min_surprise))
    return [(spikes[i], spikes[i + 1]) for i in k]


def event_sums(rate_ms: np.ndarray, events_ms: np.ndarray) -> np.ndarray:
    """X(L) = sum over events e of rate_ms[e + L], for every lag L, by FFT on a zero-padded
    (circular) array of fast length; index it modulo its own length. The event-triggered
    average at lag L is X(L) / n; with the events shifted by k it is X(L + k) / n."""
    n = next_fast_len(len(rate_ms), real=True)
    ev = np.zeros(n)
    np.add.at(ev, events_ms, 1.0)
    r = np.zeros(n)
    r[:len(rate_ms)] = rate_ms
    return irfft(np.conj(rfft(ev)) * rfft(r), n)


# --- action potential width ----------------------------------------------------------------

def ap_widths(url: str, series: str, rate: float, start: float, chunk: int,
              units: list[tuple[str, int, np.ndarray]], max_spikes: int = 300) -> list[dict]:
    """Trough-to-peak time (ms) of the mean waveform of each unit on its channel of the filtered
    trace `series`, from the spikes inside one HDF5 chunk (the one holding the most spikes of
    these units), so that each file and series is read once. `units` holds (id, column, spikes).
    The window runs from 0.6 ms before to 1.2 ms after each spike time, which caps the width."""
    idx = {uid: np.round((sp - start) * rate).astype(int) for uid, _, sp in units}
    which = np.concatenate([v // chunk for v in idx.values()])
    vals, counts = np.unique(which, return_counts=True)
    c = int(vals[np.argmax(counts)])
    f = _open(url)
    d = f[f"processing/ecephys/Processed/{series}/data"]
    lo, hi = c * chunk, min((c + 1) * chunk, d.shape[0])
    block = d[lo:hi, :]
    f.close()
    pre, post = int(0.0006 * rate), int(0.0012 * rate)
    out = []
    for uid, col, _ in units:
        sel = idx[uid][(idx[uid] // chunk) == c] - lo
        sel = sel[(sel > pre) & (sel < len(block) - post)][:max_spikes]
        if len(sel) < 10:
            out.append({"uid": uid, "width_ms": np.nan, "n_spikes": len(sel), "at_end": False})
            continue
        w = np.mean([block[k - pre:k + post, col] for k in sel], 0)
        t0 = int(np.argmin(w))
        t1 = t0 + int(np.argmax(w[t0:]))
        out.append({"uid": uid, "width_ms": (t1 - t0) / rate * 1000.0, "n_spikes": len(sel),
                    "at_end": t1 == len(w) - 1})            # peak at the window's last sample: width capped
    return out
