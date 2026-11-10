"""Loading and measures for dandiset 001955 (Gonzalez-Cabrera et al. 2026, doi:10.64898/2026.02.17.706301).

The dandiset holds three groups of NWB files: acute and chronic silicon-probe recordings (raw
broadband voltage and the Open Ephys ADC channels, nothing derived) and fiber photometry of VTA
dopamine neurons during optogenetic stimulation of VTA-PnO neurons (raw demodulated 470-nm GCaMP
and 405-nm isosbestic signals, and a table of stimulation intervals). Files are streamed from the
archive at the pinned version; nothing is written to disk.

Where the photometry parameters come from:

- Preprocessing follows the paper's notebook notebooks/Fiber_Photometry_PSTH.ipynb in
  https://github.com/CGonzC/VTAPnO_Locomotion_Analysis at tag v1.0_manuscript_submission (commit
  1ff5196e20fdaa86dd1b6d1efc26a981fb1e09ab), as the claims file's criterion for
  fig3b-photometry-continuous-only says: missing samples linearly interpolated, 405 fitted to 470
  by least squares with three passes that drop residuals beyond 3 SD (`_safe_linfit`), and
  dF/F = (470 - fit) / max(fit, 0.01 * median(fit)). The Methods (In vivo fiber photometry) say
  the same in words ("robust linear regression with iterative outlier rejection ... safeguarded
  denominator").
- Peri-stimulus traces: trials aligned to the start of each stimulation interval (Methods, Fiber
  photometry, "Trials were aligned to light onset"), read on the code's grid over -3 to +6 s
  (`compute_measures`, pre_time -3, post_time 6) by linear interpolation, z-scored per trial and
  averaged within the file (one file is one mouse and one condition). The z-score baseline is
  -1.0 to -0.1 s (Methods, "converted to z-scores using the -1.0 to -0.1 s baseline") or, as a
  variant, the code's -3.0 to -0.1 s. The z form is the baseline mean and SD (ddof 1) or the
  code's robust form, median and 1.4826 MAD. Both come from the claims file's criterion.
- The code skips a trial whose baseline has less than 1 s of valid samples (`min_baseline_sec`);
  under the Methods baseline of 0.9 s this would drop every trial, so the guard is applied only
  with the code's -3.0 s baseline (`code_guard`).
- "Corrected traces were downsampled" (Methods) gives no rate and the code does not downsample.
  `DOWNSAMPLE_HZ` is a standard choice (block means to 100 Hz); the native 12 kHz is run as a
  variant, since the rate scales the baseline SD of a z-score.
- Epochs: Pre -1.0 to -0.1 s, Stim 0.0 to 3.0 s (Methods, Fiber photometry). The epoch value is the
  mean of the trace over the epoch, or the code's area (`np.trapz` over the epoch), both named in
  the claims file's criterion.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import hashlib

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "001955"
DANDISET_VERSION = "0.261103.0758"

PRE = (-1.0, -0.1)              # Methods, Fiber photometry
STIM = (0.0, 3.0)               # Methods, Fiber photometry
BASELINES = {"methods": (-1.0, -0.1), "code": (-3.0, -0.1)}   # Methods; Fiber_Photometry_PSTH.ipynb
WINDOW = (-3.0, 6.0)            # Fiber_Photometry_PSTH.ipynb, pre_time and post_time
FIT_ITER, FIT_Z, EPS_FRAC = 3, 3.0, 0.01   # Fiber_Photometry_PSTH.ipynb, preprocess_signal
MAD_SCALE = 1.4826              # Fiber_Photometry_PSTH.ipynb, robust_scale_factor
DOWNSAMPLE_HZ = 100.0           # standard choice (the Methods give no rate)


def _text(value) -> str:
    value = value[()]
    return value.decode() if isinstance(value, bytes) else str(value)


def assets() -> pd.DataFrame:
    """Path, size, group and streaming URL of every file at the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = [{"path": a.path, "size_gb": a.size / 1e9,
                 "url": a.get_content_url(follow_redirects=1, strip_query=True)} for a in ds.get_assets()]
    df = pd.DataFrame(rows).sort_values("path").reset_index(drop=True)
    df["subject"] = df.path.str.split("/").str[0].str.replace("sub-", "", regex=False)
    df["group"] = np.select([df.subject.str.startswith("acute"), df.subject.str.startswith("chronic"),
                             df.subject.str.startswith("photometry")], ["acute", "chronic", "photometry"], "other")
    return df


def zenodo_files(record_id: int) -> pd.DataFrame:
    """Name and size of every file of a Zenodo record, from the Zenodo API (metadata only)."""
    import json
    import urllib.request
    with urllib.request.urlopen(f"https://zenodo.org/api/records/{record_id}", timeout=60) as r:
        rec = json.load(r)
    return pd.DataFrame([{"record": record_id, "file": f["key"], "size_mb": f["size"] / 1e6} for f in rec["files"]])


# ---------------------------------------------------------------- electrophysiology files

def ecephys_contents(url: str) -> dict:
    """What an ecephys file holds: its recordings (shape, rate), ADC channels, and whether it has any
    units, intervals, processing or analysis content. Reads metadata only."""
    with h5py.File(remfile.File(url), "r") as f:
        acq = f["acquisition"]
        ephys = {k: (acq[k]["data"].shape, float(acq[k]["starting_time"].attrs["rate"]))
                 for k in acq if not k.startswith("ADC")}
        adc = [k for k in acq if k.startswith("ADC")]
        return {
            "subject_id": _text(f["general/subject/subject_id"]),
            "session_description": _text(f["session_description"]),
            "recordings": len(ephys),
            "channels": sorted({s[0][1] for s in ephys.values()}),
            "rates_hz": sorted({s[1] for s in ephys.values()}),
            "samples": int(sum(s[0][0] for s in ephys.values())),
            "adc_series": len(adc),
            "units": "units" in f,
            "intervals": list(f["intervals"]) if "intervals" in f else [],
            "processing": list(f["processing"]) if "processing" in f else [],
            "analysis": list(f["analysis"]) if "analysis" in f else [],
            "electrode_columns": list(f["general/extracellular_ephys/electrodes"].attrs["colnames"]),
            "locations": sorted({_text_item(x) for x in f["general/extracellular_ephys/electrodes/location"][:]}),
            "adc_descriptions": sorted({acq[k].attrs["description"].split(".")[0] for k in adc})[:1],
        }


def _text_item(x) -> str:
    return x.decode() if isinstance(x, bytes) else str(x)


def adc_pulses(url: str, recording: str) -> pd.DataFrame:
    """Per ADC channel of one recording: its voltage range and the TTL-like pulses it carries (rising
    crossings of the mid-range, the median interval between them and the median pulse width)."""
    rows = []
    with h5py.File(remfile.File(url), "r") as f:
        acq = f["acquisition"]
        for k in sorted(k for k in acq if k.startswith(f"ADC_{recording}_")):
            d = acq[k]["data"]
            rate = float(acq[k]["starting_time"].attrs["rate"])
            x = d[:, 0].astype(np.float32) * d.attrs["conversion"]
            lo, hi = float(x.min()), float(x.max())
            row = {"channel": k.rsplit("_", 1)[1], "min_V": lo, "max_V": hi, "pulses": 0,
                   "median_interval_s": np.nan, "median_width_ms": np.nan, "first_s": np.nan}
            if hi - lo > 2.0:      # a digital-like swing; analog noise channels stay within a few 0.1 V
                high = x > (lo + hi) / 2
                on = np.flatnonzero(high[1:] & ~high[:-1]) + 1
                off = np.flatnonzero(~high[1:] & high[:-1]) + 1
                if len(on):
                    widths = [(off[off > o][0] - o) / rate * 1000 for o in on if (off > o).any()]
                    row.update(pulses=len(on), first_s=on[0] / rate,
                               median_interval_s=float(np.median(np.diff(on)) / rate) if len(on) > 1 else np.nan,
                               median_width_ms=float(np.median(widths)) if widths else np.nan)
            rows.append(row)
    return pd.DataFrame(rows)


def adc_scan(url: str) -> pd.DataFrame:
    """Every ADC channel of every recording in one ecephys file (`adc_pulses` per recording), with
    the recording's length, the pulse amplitude (the channel's max) and the number of long pulses of
    1.5 to 2.5 s with their median interval, to find the 2-s rotarod bouts (Methods, Chronic
    silicon-probe recordings: "driven in 2-s bouts ... inter-bout intervals were pseudo-random 4-35
    s"). The thresholds are a standard choice for a pulse search; no claim's outcome uses them."""
    rows = []
    with h5py.File(remfile.File(url), "r") as f:
        acq = f["acquisition"]
        # One series per channel (ADC_<recording>_ADC<j>) or, in one file, one series of 8 columns per
        # recording (ADC_<recording>).
        series = {}
        for k in acq:
            if k.startswith("ADC_"):
                rec = k[4:].rsplit("_ADC", 1)[0]
                series.setdefault(rec, []).append(k)
        for rec in sorted(series, key=lambda r: int(r.rsplit("recording", 1)[1])):
            channels = []
            for k in sorted(series[rec], key=lambda k: int(k.rsplit("ADC", 1)[1]) if "_ADC" in k[4:] else 0):
                ncol = acq[k]["data"].shape[1]
                channels += [(k, j, k.rsplit("_", 1)[1] if ncol == 1 else f"ADC{j + 1}") for j in range(ncol)]
            for k, j, name in channels:
                d = acq[k]["data"]
                rate = float(acq[k]["starting_time"].attrs["rate"])
                x = d[:, j].astype(np.float32) * d.attrs["conversion"]
                lo, hi = float(x.min()), float(x.max())
                row = {"recording": rec, "channel": name, "minutes": len(x) / rate / 60,
                       "min_V": lo, "max_V": hi, "pulses": 0, "median_interval_s": np.nan,
                       "median_width_ms": np.nan, "long_pulses": 0, "long_median_interval_s": np.nan}
                if hi - lo > 2.0:      # a digital-like swing, as in `adc_pulses`
                    high = x > (lo + hi) / 2
                    on = np.flatnonzero(high[1:] & ~high[:-1]) + 1
                    off = np.flatnonzero(~high[1:] & high[:-1]) + 1
                    if len(on):
                        nxt = np.searchsorted(off, on)
                        ok = nxt < len(off)
                        widths = (off[nxt[ok]] - on[ok]) / rate
                        long_on = on[ok][(widths >= 1.5) & (widths <= 2.5)]
                        row.update(pulses=len(on), median_width_ms=float(np.median(widths) * 1000) if ok.any() else np.nan,
                                   median_interval_s=float(np.median(np.diff(on)) / rate) if len(on) > 1 else np.nan,
                                   long_pulses=len(long_on),
                                   long_median_interval_s=float(np.median(np.diff(long_on)) / rate) if len(long_on) > 1 else np.nan)
                rows.append(row)
                del x
    return pd.DataFrame(rows)


def time_raw_read(url: str, recording: str, seconds: float = 20.0) -> tuple[float, float]:
    """Stream `seconds` of all channels of one raw recording; return (megabytes, seconds taken)."""
    import time
    with h5py.File(remfile.File(url), "r") as f:
        d = f[f"acquisition/{recording}/data"]
        n = int(seconds * f[f"acquisition/{recording}/starting_time"].attrs["rate"])
        t0 = time.time()
        x = d[:n, :]
        return x.nbytes / 1e6, time.time() - t0


# ---------------------------------------------------------------- photometry

def load_photometry(path: str, url: str) -> dict:
    """One photometry file: the two raw signals on their shared timestamps, the stimulation table and
    the metadata. The traces are reduced to dF/F as they load (`dff`), to keep one file in memory."""
    with h5py.File(remfile.File(url), "r") as f:
        g, i = f["acquisition/GCaMP_signal"], f["acquisition/Isosbestic_signal"]
        t = g["timestamps"][:]
        ca = g["data"][:].astype(np.float64)
        iso = i["data"][:].astype(np.float64)
        same_t = bool(np.array_equal(t, i["timestamps"][:]))
        iv = f["intervals/optogenetic_stimulation"]
        stim = pd.DataFrame({"start": iv["start_time"][:], "stop": iv["stop_time"][:],
                             "event": [_text_item(x) for x in iv["event"][:]],
                             "condition": [_text_item(x) for x in iv["condition"][:]]})
        meta = {"path": path, "subject": _text(f["general/subject/subject_id"]),
                "session_id": _text(f["general/session_id"]), "notes": _text(f["general/notes"]),
                "session_start": _text(f["session_start_time"]), "age": _text(f["general/subject/age"]),
                "sex": _text(f["general/subject/sex"]), "unit_ca": g["data"].attrs["unit"],
                "unit_iso": i["data"].attrs["unit"], "same_timestamps": same_t,
                "md5_ca": hashlib.md5(ca.tobytes()).hexdigest()[:12]}
    meta["group"] = "opsin" if "-exp-" in meta["subject"] else "control"
    meta["condition"] = stim.condition.iloc[0]
    dt = np.diff(t)
    meta.update(n=len(t), duration_s=float(t[-1] - t[0]), rate_hz=float(1 / np.median(dt)),
                dt_ratio_range=(float(dt.min() / np.median(dt)), float(dt.max() / np.median(dt))),
                nan_frac_ca=float(np.isnan(ca).mean()), nan_frac_iso=float(np.isnan(iso).mean()),
                ca_range=(float(np.nanmin(ca)), float(np.nanmax(ca))),
                iso_range=(float(np.nanmin(iso)), float(np.nanmax(iso))))
    d, fit_meta = dff(ca, iso)
    meta.update(fit_meta)
    return {"meta": meta, "stim": stim, "t": t, "dff": d, "ca": _interp_nan(ca).astype(np.float32)}


def _interp_nan(y: np.ndarray) -> np.ndarray:
    """Linear interpolation over missing samples, extended at both ends (pandas interpolate,
    limit_direction "both", as in Fiber_Photometry_PSTH.ipynb)."""
    bad = ~np.isfinite(y)
    if bad.any():
        idx = np.arange(len(y))
        y = y.copy()
        y[bad] = np.interp(idx[bad], idx[~bad], y[~bad])
    return y


def robust_linfit(x: np.ndarray, y: np.ndarray, max_iter: int = FIT_ITER, z: float = FIT_Z) -> tuple[float, float]:
    """Fiber_Photometry_PSTH.ipynb `_safe_linfit`: y ~ a + b x by least squares, refitted after
    dropping |residual| > z SD, `max_iter` times, then a final fit. Returns (slope, intercept)."""
    keep = np.isfinite(x) & np.isfinite(y)
    x, y = x[keep], y[keep]
    for _ in range(max_iter):
        slope, intercept = np.polyfit(x, y, 1)
        resid = y - (intercept + slope * x)
        s = np.std(resid)
        if not np.isfinite(s) or s == 0:
            break
        ok = np.abs(resid) <= z * s
        if ok.sum() < 10:
            break
        x, y = x[ok], y[ok]
    slope, intercept = np.polyfit(x, y, 1)
    return float(slope), float(intercept)


def dff(ca: np.ndarray, iso: np.ndarray) -> tuple[np.ndarray, dict]:
    """Fiber_Photometry_PSTH.ipynb `preprocess_signal`: dF/F = (470 - fit) / max(fit, eps), with
    fit the robust 405-to-470 regression and eps 1% of the fit's median."""
    ca, iso = _interp_nan(ca), _interp_nan(iso)
    slope, intercept = robust_linfit(iso, ca)
    fitted = intercept + slope * iso
    eps = EPS_FRAC * float(np.median(fitted))
    out = (ca - fitted) / np.maximum(fitted, eps)
    r2 = 1 - np.sum((ca - fitted) ** 2) / np.sum((ca - ca.mean()) ** 2)
    return out.astype(np.float32), {"slope": slope, "intercept": intercept, "r2": float(r2),
                                    "floored_frac": float(np.mean(fitted < eps))}


def downsample(t: np.ndarray, y: np.ndarray, hz: float | None) -> tuple[np.ndarray, np.ndarray]:
    """Block means to about `hz` (None keeps the native rate)."""
    if hz is None:
        return t, y
    k = max(1, int(round((1 / np.median(np.diff(t))) / hz)))
    n = len(t) // k * k
    return t[:n].reshape(-1, k).mean(1), y[:n].reshape(-1, k).mean(1)


def trial_traces(t: np.ndarray, y: np.ndarray, onsets: np.ndarray,
                 window: tuple[float, float] = WINDOW) -> tuple[np.ndarray, np.ndarray]:
    """Each trial interpolated onto the code's relative grid (`build_common_grid`, step = median
    sample interval) over `window`; samples outside the recording are NaN."""
    dt = float(np.median(np.diff(t)))
    grid = np.arange(window[0], window[1] + 0.5 * dt, dt)
    out = np.full((len(onsets), len(grid)), np.nan)
    for j, et in enumerate(onsets):
        m = (t >= et + window[0]) & (t <= et + window[1])
        if m.sum() >= 2:
            out[j] = np.interp(grid, t[m] - et, y[m], left=np.nan, right=np.nan)
    return grid, out


def zscore_trials(grid: np.ndarray, trials: np.ndarray, baseline: tuple[float, float], form: str,
                  code_guard: bool = False) -> tuple[np.ndarray, int]:
    """Per-trial z-score against the trial's own baseline. form "mean_sd": (x - mean) / SD (ddof 1);
    "robust": (x - median) / (1.4826 MAD), falling back to SD when MAD is 0 (Fiber_Photometry_PSTH.ipynb
    `compute_measures`). With `code_guard`, trials with less than 1 s or under 80% valid baseline are
    dropped, as the code does. Returns the z-scored trials and the number dropped."""
    dt = float(np.median(np.diff(grid)))
    bmask = (grid >= baseline[0]) & (grid <= baseline[1])
    kept, dropped = [], 0
    for y in trials:
        b = y[bmask]
        valid = np.isfinite(b)
        need = max(int(np.ceil(1.0 / dt)), 20) if code_guard else 2
        if valid.sum() < need or (code_guard and valid.mean() < 0.8):
            dropped += 1
            continue
        if form == "mean_sd":
            c, s = np.nanmean(b), np.nanstd(b, ddof=1)
        else:
            c = np.nanmedian(b)
            s = MAD_SCALE * np.nanmedian(np.abs(b - c))
            if not s > 0:
                s = np.nanstd(b, ddof=1)
        if not (np.isfinite(s) and s > 0):
            dropped += 1
            continue
        kept.append((y - c) / s)
    return (np.vstack(kept) if kept else np.empty((0, len(grid)))), dropped


def epoch_value(grid: np.ndarray, trace: np.ndarray, epoch: tuple[float, float], how: str) -> float:
    """The trace's mean over the epoch, or its area (trapezoid, as the code's AUC)."""
    m = (grid >= epoch[0]) & (grid <= epoch[1]) if how == "mean" else (grid >= epoch[0]) & (grid < epoch[1])
    if how == "mean":
        return float(np.nanmean(trace[m]))
    return float(np.trapezoid(trace[m], grid[m]))


def photometry_measures(rec: dict, onsets: np.ndarray, signal: str = "dff") -> list[dict]:
    """Pre and Stim epoch values of one file's trial-averaged z trace under every reading: z baseline
    (Methods, code), z form (mean_sd, robust), sampling (100 Hz, native) and epoch value (mean, area).
    Also returns the mean traces, at 100 Hz, for plotting. `signal` "dff" is the isosbestic-corrected
    dF/F; "ca" is the 470-nm signal alone, without the 405-nm fit (a variant asked for in
    verification; any fixed F0 cancels in the per-trial z-score, so the raw signal stands for its
    dF/F)."""
    rows = []
    for rate_name, hz in (("100Hz", DOWNSAMPLE_HZ), ("native", None)):
        t, y = downsample(rec["t"], rec[signal].astype(np.float64), hz)
        grid, trials = trial_traces(t, y, onsets)
        for bname, base in BASELINES.items():
            for form in ("mean_sd", "robust"):
                z, dropped = zscore_trials(grid, trials, base, form, code_guard=(bname == "code"))
                mean = np.nanmean(z, axis=0) if len(z) else np.full(len(grid), np.nan)
                for how in ("mean", "area"):
                    rows.append({"rate": rate_name, "baseline": bname, "form": form, "value": how,
                                 "pre": epoch_value(grid, mean, PRE, how), "stim": epoch_value(grid, mean, STIM, how),
                                 "trials": len(z), "dropped": dropped,
                                 "trace": (grid, mean) if (rate_name == "100Hz" and how == "mean") else None})
    return rows


def shifted_contrast(rec: dict, onsets: np.ndarray, shift: float) -> float:
    """Mean dF/F (at 100 Hz, from the full-rate trace) over 0-3 s minus -1.0 to -0.1 s around the onsets moved by `shift`
    seconds, averaged over trials; used to check that the stimulation table shares the signal's
    clock."""
    t, y = downsample(rec["t"], rec["dff"].astype(np.float64), DOWNSAMPLE_HZ)
    grid, trials = trial_traces(t, y, onsets + shift)
    pre = np.nanmean(trials[:, (grid >= PRE[0]) & (grid <= PRE[1])], axis=1)
    stim = np.nanmean(trials[:, (grid >= STIM[0]) & (grid <= STIM[1])], axis=1)
    return float(np.nanmean(stim - pre))


def regular_onsets(stim: pd.DataFrame) -> np.ndarray:
    """Onsets of the intervals whose length is within 20 ms of the file's median length: the regular
    train, without stray intervals of another length (the train lengths are 2.80 to 3.0 s, and the
    stray intervals of photometry-exp-5 at 5 Hz are 3.0 s against 2.80). The lengths are compared
    unrounded: an earlier version rounded them to 10 ms and dropped 10-Hz intervals of 2.905 s that
    rounded either way."""
    length = stim.stop - stim.start
    return stim.start[(length - length.median()).abs() <= 0.02].to_numpy()


def process_photometry(path: str, url: str) -> dict:
    """Load one file, compute its measures under every reading, for all intervals and for the regular
    train only (`regular_onsets`), and, for all intervals, on the 470-nm signal without the 405-nm
    fit; then keep only the 100-Hz dF/F, so that one file at a time is held at full rate."""
    rec = load_photometry(path, url)
    onsets_all = rec["stim"].start.to_numpy()
    onsets_reg = regular_onsets(rec["stim"])
    rec["n_onsets"] = {"all": len(onsets_all), "regular": len(onsets_reg)}
    rec["measures"] = {("dff", "all"): photometry_measures(rec, onsets_all)}
    rec["measures"]["dff", "regular"] = (rec["measures"]["dff", "all"] if len(onsets_reg) == len(onsets_all)
                                         else photometry_measures(rec, onsets_reg))
    rec["measures"]["470_only", "all"] = photometry_measures(rec, onsets_all, signal="ca")
    rec["contrast"] = {s: shifted_contrast(rec, onsets_all, s) for s in (0.0, 6.5, -6.5)}
    rec["t"], rec["dff"] = downsample(rec["t"], rec["dff"].astype(np.float64), DOWNSAMPLE_HZ)
    del rec["ca"]
    return rec


def load_all_photometry(table: pd.DataFrame, workers: int = 3) -> list[dict]:
    """Every photometry file, processed three at a time (under 1 GB of memory each)."""
    rows = table[table.group == "photometry"]
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda r: process_photometry(r.path, r.url), rows.itertuples()))


# ---------------------------------------------------------------- photometry statistics

FREQUENCIES = ["5hz", "10hz", "20hz", "Cont"]


def bh(p: list[float]) -> np.ndarray:
    """Benjamini-Hochberg adjusted p-values."""
    from statsmodels.stats.multitest import multipletests
    return multipletests(p, method="fdr_bh")[1]


def _pooled_t(diff: float, se: float, df: int) -> float:
    from scipy import stats
    return float(2 * stats.t.sf(abs(diff / se), df))


def within_opsin_tests(df: pd.DataFrame, anova: str, posthoc: str = "separate") -> dict:
    """Figure 3b as the claims file reads it: on opsin mice, a two-way ANOVA epoch (Pre, Stim) by
    frequency, with repeated measures on both factors (`anova` "rm") or as independent cells
    ("plain"); post hoc Pre against Stim per frequency, Benjamini-Hochberg over the four. The post
    hoc test is one of:

    - "separate": a paired t-test per frequency, df n - 1. This is also what GraphPad Prism does
      after a repeated-measures ANOVA when sphericity is not assumed ("For each comparison of two
      groups, it uses only the data in those two groups ... When two groups are matched, it is
      identical to a paired t test"; GraphPad, "How Prism 8.0 computes multiple comparisons tests
      following ANOVA", cdn.graphpad.com/faq/1688/file/MulitpleComparisonAlgorithmsPrism8.pdf).
    - "prism": Prism's error when sphericity is assumed (same document). For "rm", matched values
      both stacked and spread across a row, a simple effect uses MS(Error) = MS(Residual), the
      epoch x frequency x subject mean square, with df (2 - 1)(4 - 1)(n - 1); for "plain", the
      residual mean square of the two-way model, df 8(n - 1). SE = sqrt(2 MS / n) in both.
    - "pooled" ("rm" only): the variance of the Stim - Pre differences averaged over the four
      frequencies, df 4(n - 1), the form run before verification. It is not Prism's, and is kept as
      a variant.

    `df` has one row per mouse and frequency, with columns pre and stim. Returns, per frequency, the
    mean difference, the SE and df of the test, and the raw and BH p."""
    import pingouin as pg
    from scipy import stats
    op = df[df.group == "opsin"]
    long = op.melt(id_vars=["subject", "condition"], value_vars=["pre", "stim"], var_name="epoch", value_name="z")
    if anova == "rm":
        a = pg.rm_anova(data=long, dv="z", within=["epoch", "condition"], subject="subject")
    else:
        a = pg.anova(data=long, dv="z", between=["epoch", "condition"])
    inter = a[a.Source == "epoch * condition"]
    anova_p = float(inter["p_unc"].iloc[0]) if "p_unc" in a else float(inter["p-unc"].iloc[0])
    groups = {c: op[op.condition == c].sort_values("subject") for c in FREQUENCIES}
    diffs = {c: float((d.stim - d.pre).mean()) for c, d in groups.items()}
    ns = {c: len(d) for c, d in groups.items()}
    n = min(ns.values())
    if posthoc == "separate":
        se = {c: float(np.std(groups[c].stim - groups[c].pre, ddof=1) / np.sqrt(ns[c])) for c in FREQUENCIES}
        dfe = {c: ns[c] - 1 for c in FREQUENCIES}
    elif posthoc == "pooled" and anova == "rm":
        var = np.mean([np.var(groups[c].stim - groups[c].pre, ddof=1) for c in FREQUENCIES])
        se = {c: float(np.sqrt(var / n)) for c in FREQUENCIES}
        dfe = {c: len(FREQUENCIES) * (n - 1) for c in FREQUENCIES}
    elif posthoc == "prism" and anova == "rm":
        d = op.assign(d=op.stim - op.pre).pivot(index="subject", columns="condition", values="d")[FREQUENCIES].to_numpy()
        resid = d - d.mean(1, keepdims=True) - d.mean(0, keepdims=True) + d.mean()
        dfr = (len(FREQUENCIES) - 1) * (d.shape[0] - 1)
        ms = 0.5 * float((resid ** 2).sum()) / dfr      # SS(epoch x frequency x subject) from the differences
        se = {c: float(np.sqrt(2 * ms / n)) for c in FREQUENCIES}
        dfe = {c: dfr for c in FREQUENCIES}
    elif posthoc in ("prism", "pooled") and anova == "plain":
        mse = np.mean([np.var(groups[c][e], ddof=1) for c in FREQUENCIES for e in ("pre", "stim")])
        se = {c: float(np.sqrt(2 * mse / n)) for c in FREQUENCIES}
        dfe = {c: 2 * len(FREQUENCIES) * (n - 1) for c in FREQUENCIES}
    else:
        raise ValueError(posthoc)
    raw = [_pooled_t(diffs[c], se[c], dfe[c]) for c in FREQUENCIES]
    adj = bh(raw)
    return {"interaction_p": anova_p, "p_raw": dict(zip(FREQUENCIES, raw)), "p_bh": dict(zip(FREQUENCIES, adj)),
            "mean_diff": diffs, "se": se, "df": dfe, "n": ns}


def opsin_vs_control_tests(df: pd.DataFrame, anova: str, posthoc: str = "separate") -> dict:
    """Figure 3c as the claims file reads it: delta = Stim - Pre per mouse and frequency; a two-way
    ANOVA group by frequency, frequency repeated within mouse (`anova` "rm", a mixed ANOVA) or
    not ("plain"); post hoc opsin against control per frequency, Benjamini-Hochberg over the four.
    The post hoc test is a separate unpaired (Student) t-test per frequency (`posthoc`
    "separate"; Prism's form when sphericity is not assumed, "identical to an unpaired t test", in
    the GraphPad document cited in `within_opsin_tests`) or the contrast on the pooled within-cell
    error of the group by frequency cells ("pooled", df = mice x frequencies - 8). The pooled form is
    Prism's error when sphericity is assumed: for the mixed design, a comparison of the unmatched
    groups within a level of the repeated factor uses MS(Error) = (SS(Subjects) + SS(Residuals)) /
    (DF(Subjects) + DF(Residuals)) with df DF(Subjects) + DF(Residuals), which is the within-cell
    sum of squares over its df, 6 + 18 = 24 here; for the ordinary design it is MS(Residual), the
    same."""
    import pingouin as pg
    from scipy import stats
    d = df.assign(delta=df.stim - df.pre)
    if anova == "rm":
        a = pg.mixed_anova(data=d, dv="delta", within="condition", between="group", subject="subject")
        inter = a[a.Source == "Interaction"]
    else:
        a = pg.anova(data=d, dv="delta", between=["group", "condition"])
        inter = a[a.Source == "group * condition"]
    anova_p = float(inter["p_unc"].iloc[0]) if "p_unc" in a else float(inter["p-unc"].iloc[0])
    cells = {(g, c): d[(d.condition == c) & (d.group == g)].delta for g in ("opsin", "control") for c in FREQUENCIES}
    diffs = [float(cells["opsin", c].mean() - cells["control", c].mean()) for c in FREQUENCIES]
    se, dfe = {}, {}
    if posthoc == "separate":
        for c in FREQUENCIES:
            x, y = cells["opsin", c], cells["control", c]
            sp2 = ((len(x) - 1) * x.var(ddof=1) + (len(y) - 1) * y.var(ddof=1)) / (len(x) + len(y) - 2)
            se[c], dfe[c] = float(np.sqrt(sp2 * (1 / len(x) + 1 / len(y)))), len(x) + len(y) - 2
    else:
        ss = sum(((x - x.mean()) ** 2).sum() for x in cells.values())
        dfw = sum(len(x) for x in cells.values()) - len(cells)
        mse = ss / dfw
        for c in FREQUENCIES:
            se[c] = float(np.sqrt(mse * (1 / len(cells["opsin", c]) + 1 / len(cells["control", c]))))
            dfe[c] = dfw
    raw = [_pooled_t(diffs[k], se[c], dfe[c]) for k, c in enumerate(FREQUENCIES)]
    adj = bh(raw)
    return {"interaction_p": anova_p, "p_raw": dict(zip(FREQUENCIES, raw)), "p_bh": dict(zip(FREQUENCIES, adj)),
            "mean_diff": dict(zip(FREQUENCIES, diffs)), "se": se, "df": dfe}
