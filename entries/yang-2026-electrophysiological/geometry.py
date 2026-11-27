"""Loading, sweep features and response geometries for Yang & Xiao (2026) on DANDI:000020.

Every NWB file of the dandiset is streamed (remfile + h5py) at the pinned version and reduced,
as it loads, to one small record per current-clamp sweep of the three stimulus families the
paper analyses. Nothing is written to disk.

Where each parameter comes from:

- Stimulus families (paper, Methods 1: "Sweeps were assigned to stimulation protocols using
  stimulus descriptions, current-command waveform structure, and recording mode"). Brief pulse:
  X5SP_Search_DA_0 only (Methods 1, named). Long pulse and ramp are not named; the families are
  taken from the stimulus descriptions present in the files (see LONG_FAMILIES, RAMP_FAMILIES)
  and the readings are listed in the notebook (claim fig1c-cells-per-protocol).
- Quality control (Methods 2 lists the criteria but gives no threshold). Assumption, standard
  choice: complete trace over the analysis window (no NaN, no zero padding), baseline potential
  between -100 and -40 mV, baseline SD below 1 mV, a detectable step, ramp or pulse of the
  expected duration, ramp command linear (R^2 > 0.99 over its first second). The notebook shows
  counts with and without the baseline criteria.
- Spike detection (open; claim fig3d-ramp-loadings names two readings): an upward crossing of
  0 mV ("zero"), or dV/dt rising through 20 V/s followed within 2 ms by a peak above -20 mV
  ("dvdt"). Both are computed for every sweep.
- Response windows for the brief pulse (open; claim fig4f-brief-gain-vip-cck-high names the
  readings): peak and mean from pulse onset to pulse end plus 10 ms ("w10") or 50 ms ("w50");
  the fast response from onset to pulse end plus 2 ms (assumption; 1 and 5 ms are computed too,
  FAST_ALT_MS, and shown as readings in the notebook). Baseline is the mean potential before
  the pulse.
- Long-pulse fraction thresholds (Supplementary Table 1 names the features, not thresholds):
  strong depolarization = peak response >= 20 mV, high spiking = rate >= 20 Hz; command bins
  0-50, 50-100, 100-200, 200-400, >=400 pA (assumptions; the notebook varies all three).
- Ramp post-recruitment firing rate = spikes / (end of the recorded ramp - first spike time);
  recruitment current = command at the first spike (claim fig3e-ramp-recruitment-current-order).
- PCA: missingness filter, imputation and standardization (Methods 4; scikit-learn, Methods 7);
  features with more than 50% missing dropped (claim fig2a-longpulse-low-dimensional).
"""
import re
import time

import numpy as np
import pandas as pd

DANDISET = "000020"
VERSION = "0.210913.1639"
API = "https://api.dandiarchive.org/api"

LONG_FAMILIES = {
    # reading L1, every long square step family in the files
    "all_long_square": re.compile(r"^(C1LS|X1PS|X2LP|X3LP|X4PS)"),
    # reading L2, the suprathreshold step family only
    "suprathreshold": re.compile(r"^(X4PS_SupraThresh|C1LSCOARSE)"),
    # reading L3, the families named "long pulse" (LP) in the newer naming
    "LP_named": re.compile(r"^(X2LP|X3LP)"),
}
LONG_RE = re.compile(r"^(C1LS|X1PS|X2LP|X3LP|X4PS)")
RAMP_RE = re.compile(r"^(C1RP|X7Ramp)")
BRIEF_NAME = "X5SP_Search_DA_0"

BASE_LO, BASE_HI, BASE_SD = -100.0, -40.0, 1.0
FAST_MS = 2.0
FAST_ALT_MS = (1.0, 5.0)
BIN_EDGES = [0, 50, 100, 200, 400, np.inf]


def list_assets(version=VERSION):
    import requests
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        d = requests.get(url, timeout=60).json()
        out += d["results"]
        url = d["next"]
    return out


def _s3_url(asset_id):
    import requests
    for i in range(5):
        try:
            r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
            return r.headers["Location"]
        except Exception:
            time.sleep(2 + 3 * i)
    raise RuntimeError("no url for " + asset_id)


def detect_spikes(v, rate):
    """Spike times (samples) under both readings: 'zero' 0 mV upward crossing, 'dvdt' 20 V/s."""
    v = np.asarray(v, dtype=np.float64)
    zero = np.flatnonzero((v[:-1] < 0) & (v[1:] >= 0)) + 1
    dvdt = np.diff(v) * rate / 1000.0  # mV/ms == V/s
    up = np.flatnonzero((dvdt[:-1] < 20) & (dvdt[1:] >= 20)) + 1
    w = int(0.002 * rate)
    keep = []
    last = -10 ** 9
    for i in up:
        if i - last < w:
            continue
        if v[i:i + w].max() > -20:
            keep.append(i)
            last = i
    return zero, np.array(keep, dtype=int)


def _runs(x):
    """Constant runs of a piecewise-constant command: (start, stop, value)."""
    ch = np.flatnonzero(np.abs(np.diff(x)) > 1e-6) + 1
    b = np.r_[0, ch, len(x)]
    return [(int(b[i]), int(b[i + 1]), float(x[b[i]])) for i in range(len(b) - 1)]


def _valid_end(v):
    """Index after the last sample that is neither NaN nor zero padding."""
    ok = np.flatnonzero(np.isfinite(v) & (v != 0))
    return int(ok[-1]) + 1 if len(ok) else 0


def _baseline(v, rate, on, tp_end):
    lo = max(on - int(0.1 * rate), tp_end + int(0.05 * rate) if tp_end else 0)
    lo = min(lo, on - int(0.01 * rate))
    seg = v[max(lo, 0):on]
    return float(np.mean(seg)), float(np.std(seg))


def _tp_end(runs, rate):
    """End of the test pulse (a 10 ms run near the start), or 0 when there is none."""
    for a, b, val in runs[:4]:
        if val != 0 and abs((b - a) / rate - 0.010) < 0.002 and a / rate < 0.1:
            return b
    return 0


def _long_sweep(v, x, rate):
    runs = _runs(x)
    tp = _tp_end(runs, rate)
    steps = [(a, b, val) for a, b, val in runs if val != 0 and (b - a) / rate >= 0.3 and a >= tp]
    if not steps:
        return dict(qc_stim=False)
    a, b, amp = steps[0]
    end = _valid_end(v)
    r = dict(qc_stim=True, amp=amp, dur=(b - a) / rate, qc_len=end >= b + int(0.05 * rate))
    bl, sd = _baseline(v, rate, a, tp)
    r.update(base=bl, noise=sd)
    if not r["qc_len"]:
        return r
    seg = v[a:b]
    z, d = detect_spikes(v[a:b + int(0.005 * rate)], rate)
    r.update(n_zero=int(len(z)), n_dvdt=int(len(d)), peak=float(seg.max() - bl),
             trough=float(seg.min() - bl),
             dv_pre=float(np.mean(v[a - int(0.02 * rate):a]) - bl),
             dv_post=float(np.mean(v[a + int(0.005 * rate):a + int(0.025 * rate)]) - bl))
    return r


def _ramp_sweep(v, x, rate):
    runs = _runs(x)
    tp = _tp_end(runs, rate)
    pos = np.flatnonzero(x[tp:] > 0)
    if len(pos) == 0:
        return dict(qc_stim=False)
    on = tp + int(pos[0]) - 1
    end = _valid_end(v)
    stim_end = tp + int(pos[-1]) + 1
    end = min(end, stim_end)
    r = dict(qc_stim=True, qc_len=end > on + int(0.5 * rate))
    if not r["qc_len"]:
        return r
    n1 = min(on + int(1.0 * rate), end)
    t = np.arange(on, n1) / rate
    c = np.polyfit(t, x[on:n1], 1)
    pred = np.polyval(c, t)
    ss = np.sum((x[on:n1] - x[on:n1].mean()) ** 2)
    r2 = 1 - np.sum((x[on:n1] - pred) ** 2) / ss if ss > 0 else 0.0
    bl, sd = _baseline(v, rate, on, tp)
    r.update(slope=float(c[0]), lin_r2=float(r2), base=bl, noise=sd, dur=(end - on) / rate,
             peak=float(v[on:end].max() - bl), mean=float(v[on:end].mean() - bl),
             abs_peak=float(v[on:end].max()))
    z, d = detect_spikes(v[on:end], rate)
    for name, s in (("zero", z), ("dvdt", d)):
        r["n_" + name] = int(len(s))
        if len(s):
            i = on + int(s[0])
            r["rec_" + name] = float(x[i])
            r["lat_" + name] = float((i - on) / rate)
            r["fr_" + name] = float(len(s) / max((end - i) / rate, 1e-3))
    return r


def _brief_sweep(v, x, rate):
    runs = _runs(x)
    p = [(a, b, val) for a, b, val in runs if val != 0 and (b - a) / rate <= 0.005]
    if not p:
        return dict(qc_stim=False)
    a, b, amp = p[0]
    end = _valid_end(v)
    r = dict(qc_stim=amp > 0, amp=amp, qc_len=end >= b + int(0.05 * rate) and a >= int(0.01 * rate))
    bl, sd = _baseline(v, rate, a, 0)
    r.update(base=bl, noise=sd)
    if not r["qc_len"]:
        return r
    for w in (10, 50):
        seg = v[a:b + int(w / 1000 * rate)]
        r[f"peak_w{w}"] = float(seg.max() - bl)
        r[f"mean_w{w}"] = float(seg.mean() - bl)
        r[f"lat_w{w}"] = float(np.argmax(seg) / rate * 1000)
    for fw in FAST_ALT_MS:  # other fast-response windows, shown as readings
        seg = v[a:b + int(fw / 1000 * rate)]
        r[f"fpeak_f{fw:g}"] = float(seg.max() - bl)
        r[f"fmean_f{fw:g}"] = float(seg.mean() - bl)
    seg = v[a:b + int(FAST_MS / 1000 * rate)]
    r.update(fpeak=float(seg.max() - bl), fmean=float(seg.mean() - bl),
             flat=float(np.argmax(seg) / rate * 1000),
             dv_pre=float(np.mean(v[a - int(0.005 * rate):a]) - bl),
             dv_post=float(np.mean(v[b:b + int(0.005 * rate)]) - bl))
    z, d = detect_spikes(v[a:b + int(0.05 * rate)], rate)
    for name, s in (("zero", z), ("dvdt", d)):
        r["n_" + name] = int(len(s))
        if len(s):
            r["slat_" + name] = float(s[0] / rate * 1000)
    return r


def read_file(asset):
    """Stream one NWB file; return its metadata and one record per sweep of the three families."""
    import h5py
    import remfile
    t0 = time.time()
    out = dict(path=asset["path"], asset_id=asset["asset_id"], sweeps=[], err=None)
    for attempt in range(3):
        try:
            rf = remfile.File(_s3_url(asset["asset_id"]))
            with h5py.File(rf, "r") as f:
                g = f["general/subject/genotype"][()]
                out["genotype"] = g.decode() if isinstance(g, bytes) else str(g)
                sid = f["general/session_id"][()]
                out["session"] = sid.decode() if isinstance(sid, bytes) else str(sid)
                out["subject"] = asset["path"].split("/")[0].replace("sub-", "")
                descs = {}
                sweeps = []
                fp = None
                for k in f["acquisition"]:
                    s = f["acquisition"][k]
                    nt = s.attrs.get("neurodata_type")
                    nt = nt.decode() if isinstance(nt, bytes) else str(nt)
                    d = s.attrs.get("stimulus_description")
                    d = d.decode() if isinstance(d, bytes) else str(d)
                    descs[d] = descs.get(d, 0) + 1
                    if nt != "CurrentClampSeries":
                        continue
                    fam = ("long" if LONG_RE.match(d) else "ramp" if RAMP_RE.match(d)
                           else "brief" if d == BRIEF_NAME else None)
                    if fam is None and fp is not None:
                        continue
                    v = s["data"][:].astype(np.float64)
                    conv = float(s["data"].attrs.get("conversion", 1.0))
                    v = v * conv * 1000.0  # mV
                    if fp is None:
                        fp = (len(v), round(float(np.nansum(v[:20000])), 3))
                    if fam is None:
                        continue
                    rate = float(s["starting_time"].attrs["rate"])
                    sk = k.replace("_AD", "_DA")
                    st = f["stimulus/presentation"][sk]
                    x = st["data"][:].astype(np.float64) * float(st["data"].attrs.get("conversion", 1.0)) * 1e12
                    fn = {"long": _long_sweep, "ramp": _ramp_sweep, "brief": _brief_sweep}[fam]
                    try:
                        r = fn(v, x, rate)
                    except Exception as e:  # recorded as a failed extraction
                        r = dict(qc_stim=False, fail=repr(e))
                    r.update(sweep=k, desc=d, fam=fam, rate=rate, unit=str(s["data"].attrs.get("unit")))
                    sweeps.append(r)
                out["sweeps"] = sweeps
                out["descs"] = descs
                out["fingerprint"] = fp
            out["err"] = None
            break
        except Exception as e:
            out["err"] = repr(e)
            time.sleep(3)
    out["seconds"] = time.time() - t0
    return out


def read_all(assets, workers=24, progress=True):
    """Read every asset in a pool of processes; returns (cells, sweeps) DataFrames."""
    import multiprocessing as mp
    from concurrent.futures import ProcessPoolExecutor
    res = []
    t0 = time.time()
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        for i, r in enumerate(ex.map(read_file, assets, chunksize=4)):
            res.append(r)
            if progress and (i + 1) % 500 == 0:
                print(f"{i + 1} files, {time.time() - t0:.0f} s", flush=True)
    cells = pd.DataFrame([{k: r.get(k) for k in ("path", "asset_id", "subject", "session", "genotype",
                                                   "err", "seconds", "fingerprint", "descs")}
                          for r in res])
    rows = []
    for r in res:
        for s in r["sweeps"]:
            s = dict(s)
            s["session"] = r.get("session")
            s["path"] = r["path"]
            rows.append(s)
    return cells, pd.DataFrame(rows)


def driver_line(genotype, reading="first"):
    """Driver-line label, the marker gene of a driver allele in the genotype string.

    Methods 1: "Cre-line labels were used as driver-defined cell-group labels"; the figures
    abbreviate lines "by primary marker genes" (Figure 2 legend). The files hold no Cre-line
    field, only the genotype.
    'first' (main reading): the gene of the first driver allele (Cre or FlpO; reporters such as
    Ai14 or Ai65 are skipped). This yields Sncg, a line the paper names, from the Flp-only
    genotype Sncg-IRES2-FlpO-neo. 'cre': the gene of the Cre allele only (no label for Flp-only
    genotypes). 'flp': for intersectional genotypes, the gene of the Flp allele.
    """
    if not isinstance(genotype, str):
        return None
    parts = [p.split("/")[0] for p in genotype.split(";")]
    drivers = [p for p in parts if ("Cre" in p or "Flp" in p) and not p.startswith("Ai")]
    cre = [p for p in drivers if "Cre" in p]
    flp = [p for p in drivers if "Flp" in p]
    if reading == "first":
        pick = drivers[0] if drivers else None
    elif reading == "cre":
        pick = cre[0] if cre else None
    else:
        pick = flp[0] if flp else (drivers[0] if drivers else None)
    if pick is None:
        return None
    return pick.split("-")[0]


# ---------------------------------------------------------------- cell-level features

def _qc(df, baseline=True):
    ok = df["qc_stim"].fillna(False).astype(bool) & df["qc_len"].fillna(False).astype(bool)
    if baseline:
        ok &= df["base"].between(BASE_LO, BASE_HI) & (df["noise"] < BASE_SD)
    return ok


def _slope(x, y):
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 2 or np.ptp(x[m]) == 0:
        return np.nan, np.nan
    c = np.polyfit(x[m], y[m], 1)
    r = np.corrcoef(x[m], y[m])[0, 1] if np.std(y[m]) > 0 else np.nan
    return c[0], r ** 2


def long_features(sw, spike="zero", depol=20.0, high=20.0, bins=None, per_second=False):
    """One row per cell from depolarizing long-pulse sweeps (Supplementary Table 1, long pulse).

    depol (mV) and high (Hz) are the strong-depolarization and high-spiking thresholds, bins the
    command-bin edges (BIN_EDGES by default); all are assumptions, varied in the notebook.
    per_second: spike counts divided by the step duration (in s), so that 0.5 s and 1 s steps are
    on one scale (a variant; the paper's feature is the count)."""
    bins = BIN_EDGES if bins is None else bins
    rows = {}
    for ses, g in sw.groupby("session"):
        g = g[g["amp"] > 0]
        if not len(g):
            continue
        n = g["n_" + spike].to_numpy(float)
        amp = g["amp"].to_numpy(float)
        fr = n / g["dur"].to_numpy(float)
        pk = g["peak"].to_numpy(float)
        cnt = fr if per_second else n
        r = {"spiking_fraction": np.mean(n > 0), "subthreshold_fraction": np.mean(n == 0),
             "strong_depol_fraction": np.mean(pk >= depol), "high_spiking_fraction": np.mean(fr >= high),
             "median_fr": np.median(fr), "mean_fr": np.mean(fr), "max_fr": np.max(fr),
             "median_spike_count": np.median(cnt), "max_spike_count": np.max(cnt),
             "first_spiking_command": amp[n > 0].min() if (n > 0).any() else np.nan,
             "median_peak_response": np.median(pk),
             "median_baseline": g["base"].median(), "median_baseline_noise": g["noise"].median()}
        supra = n > 0
        r["fr_slope"] = _slope(amp[supra], fr[supra])[0] if supra.sum() >= 2 else np.nan
        r["peak_slope"] = _slope(amp, pk)[0]
        for i in range(len(bins) - 1):
            m = (amp >= bins[i]) & (amp < bins[i + 1])
            lab = f"{bins[i]:g}-{bins[i + 1]:g}pA"
            r["bin_spiking_" + lab] = np.mean(n[m] > 0) if m.any() else np.nan
            r["bin_peak_" + lab] = np.median(pk[m]) if m.any() else np.nan
            r["bin_fr_" + lab] = np.median(fr[m]) if m.any() else np.nan
        rows[ses] = r
    return pd.DataFrame.from_dict(rows, orient="index")


def ramp_features(sw, spike="zero"):
    rows = {}
    for ses, g in sw.groupby("session"):
        n = g["n_" + spike].to_numpy(float)
        rec = g.get("rec_" + spike, pd.Series(np.nan, index=g.index)).to_numpy(float)
        lat = g.get("lat_" + spike, pd.Series(np.nan, index=g.index)).to_numpy(float)
        fr = g.get("fr_" + spike, pd.Series(np.nan, index=g.index)).to_numpy(float)
        fr = np.where(n > 0, fr, 0.0)
        rows[ses] = {"median_recruitment_current": np.nanmedian(rec) if np.isfinite(rec).any() else np.nan,
                     "min_recruitment_current": np.nanmin(rec) if np.isfinite(rec).any() else np.nan,
                     "spiking_fraction": np.mean(n > 0),
                     "median_first_spike_latency": np.nanmedian(lat) if np.isfinite(lat).any() else np.nan,
                     "min_first_spike_latency": np.nanmin(lat) if np.isfinite(lat).any() else np.nan,
                     "median_spike_count": np.median(n), "max_spike_count": np.max(n),
                     "median_fr": np.median(fr), "max_fr": np.max(fr),
                     "median_peak_response": g["peak"].median(), "median_mean_response": g["mean"].median(),
                     "median_abs_peak_voltage": g["abs_peak"].median(),
                     "median_baseline": g["base"].median(), "median_baseline_noise": g["noise"].median()}
    return pd.DataFrame.from_dict(rows, orient="index")


RAMP_RECRUIT = ["min_recruitment_current", "median_recruitment_current", "min_first_spike_latency",
                "median_first_spike_latency", "median_spike_count", "max_spike_count", "median_fr", "max_fr"]


def brief_features(sw, win="w50", spike="zero", fast=None):
    """One row per cell from X5SP_Search_DA_0 sweeps. fast: None for the 2 ms fast-response
    window (FAST_MS), or 1 or 5 for the other windows (FAST_ALT_MS)."""
    rows = {}
    fpk, fmn = ("fpeak", "fmean") if fast is None else (f"fpeak_f{fast:g}", f"fmean_f{fast:g}")
    for ses, g in sw.groupby("session"):
        amp = g["amp"].to_numpy(float)
        pk = g["peak_" + win].to_numpy(float)
        mn = g["mean_" + win].to_numpy(float)
        fp = g[fpk].to_numpy(float)
        fm = g[fmn].to_numpy(float)
        n = g["n_" + spike].to_numpy(float)
        sl = g.get("slat_" + spike, pd.Series(np.nan, index=g.index)).to_numpy(float)
        s, r2 = _slope(amp, pk)
        rows[ses] = {"sweep_count": len(g), "unique_command_count": len(np.unique(np.round(amp, 1))),
                     "median_command": np.median(amp), "max_command": np.max(amp), "command_range": np.ptp(amp),
                     "median_baseline": g["base"].median(), "median_baseline_noise": g["noise"].median(),
                     "median_peak_response": np.median(pk), "max_peak_response": np.max(pk),
                     "median_mean_response": np.median(mn),
                     "median_fast_peak": np.median(fp), "max_fast_peak": np.max(fp),
                     "median_fast_mean": np.median(fm),
                     "median_peak_gain": np.median(pk / amp), "median_mean_gain": np.median(mn / amp),
                     "peak_command_slope": s, "peak_slope_fit": r2,
                     "median_peak_latency": g["lat_" + win].median(), "median_fast_peak_latency": g["flat"].median(),
                     "spike_fraction": np.mean(n > 0), "max_spike_count": np.max(n),
                     "first_spiking_command": amp[n > 0].min() if (n > 0).any() else np.nan,
                     "median_first_spike_latency": np.nanmedian(sl) if np.isfinite(sl).any() else np.nan,
                     # extra summaries named in Figure 4C (reading b)
                     "mean_mean_response": np.mean(mn), "max_mean_response": np.max(mn),
                     "max_fast_mean": np.max(fm), "q25_peak_response": np.quantile(pk, 0.25),
                     "mean_peak_response": np.mean(pk)}
    return pd.DataFrame.from_dict(rows, orient="index")


BRIEF_RESPONSE_A = ["median_peak_response", "max_peak_response", "median_mean_response",
                    "median_fast_peak", "max_fast_peak", "median_fast_mean"]
BRIEF_GAIN = ["median_peak_gain", "median_mean_gain"]
BRIEF_RESPONSE_B = ["median_fast_mean", "mean_mean_response", "median_mean_response", "max_fast_mean",
                    "max_mean_response", "median_peak_response", "median_fast_peak", "q25_peak_response",
                    "mean_peak_response", "max_peak_response"]
BRIEF_TABLE = ["sweep_count", "unique_command_count", "median_command", "max_command", "command_range",
               "median_baseline", "median_baseline_noise", "median_peak_response", "max_peak_response",
               "median_mean_response", "median_fast_peak", "max_fast_peak", "median_fast_mean",
               "median_peak_gain", "median_mean_gain", "peak_command_slope", "peak_slope_fit",
               "median_peak_latency", "median_fast_peak_latency", "spike_fraction", "max_spike_count",
               "first_spiking_command", "median_first_spike_latency"]
BRIEF_GAIN_SET = ["median_peak_gain", "median_mean_gain", "peak_command_slope", "peak_slope_fit"]


# ---------------------------------------------------------------- geometry

def pca_geometry(X, impute="median", max_missing=0.5):
    """Methods 4: drop features with excessive missingness, impute, standardize, PCA."""
    from sklearn.decomposition import PCA
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import StandardScaler
    X = X.replace([np.inf, -np.inf], np.nan)
    keep = X.columns[X.isna().mean() <= max_missing]
    keep = [c for c in keep if X[c].nunique(dropna=True) > 1]
    Z = SimpleImputer(strategy=impute).fit_transform(X[keep])
    Z = StandardScaler().fit_transform(Z)
    p = PCA().fit(Z)
    scores = pd.DataFrame(p.transform(Z), index=X.index, columns=[f"PC{i + 1}" for i in range(len(keep))])
    load = pd.DataFrame(p.components_.T, index=keep, columns=scores.columns)
    return dict(scores=scores, loadings=load, evr=p.explained_variance_ratio_, features=list(keep),
                dropped=[c for c in X.columns if c not in keep])


def orient(geo, pc, feature):
    """Flip a PC so that `feature` loads positively (PC signs are arbitrary, Methods 4)."""
    if feature in geo["loadings"].index and geo["loadings"].loc[feature, pc] < 0:
        geo["scores"][pc] *= -1
        geo["loadings"][pc] *= -1
    return geo


def centroids(scores, labels, npc=None):
    S = scores if npc is None else scores.iloc[:, :npc]
    return S.groupby(labels).mean()


def centroid_distances(C):
    from scipy.spatial.distance import pdist, squareform
    return pd.DataFrame(squareform(pdist(C.to_numpy())), index=C.index, columns=C.index)


def upper(D, lines):
    D = D.loc[lines, lines].to_numpy()
    return D[np.triu_indices(len(lines), 1)]


def mean_centroid_distance(S, lab):
    """Mean pairwise distance among group centroids; S array, lab integer codes."""
    k = lab.max() + 1
    cnt = np.bincount(lab, minlength=k)
    C = np.zeros((k, S.shape[1]))
    np.add.at(C, lab, S)
    C /= cnt[:, None]
    d = np.sqrt(((C[:, None, :] - C[None, :, :]) ** 2).sum(-1))
    return d[np.triu_indices(k, 1)].mean()


def _dvec(S, lab, k):
    C = np.zeros((k, S.shape[1]))
    np.add.at(C, lab, S)
    C /= np.bincount(lab, minlength=k)[:, None]
    d = np.sqrt(((C[:, None, :] - C[None, :, :]) ** 2).sum(-1))
    return d[np.triu_indices(k, 1)]


def balanced(SA, labA, SB, labB, lines, m, iters, rng, shuffle=None):
    """Methods 6: m cells per line drawn without replacement in each geometry; Spearman r of the
    centroid distance vectors. shuffle: None, 'one' (labels permuted in geometry B) or 'both'."""
    from scipy.stats import spearmanr
    k = len(lines)
    idxA = [np.flatnonzero(labA == l) for l in lines]
    idxB = [np.flatnonzero(labB == l) for l in lines]
    lab = np.repeat(np.arange(k), m)
    out = np.empty(iters)
    for it in range(iters):
        a = np.concatenate([rng.choice(ix, m, replace=False) for ix in idxA])
        b = np.concatenate([rng.choice(ix, m, replace=False) for ix in idxB])
        la, lb = lab, lab
        if shuffle in ("one", "both"):
            lb = rng.permutation(lab)
        if shuffle == "both":
            la = rng.permutation(lab)
        out[it] = spearmanr(_dvec(SA[a], la, k), _dvec(SB[b], lb, k))[0]
    return out
