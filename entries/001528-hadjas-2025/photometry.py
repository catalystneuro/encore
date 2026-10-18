"""Loading and response measures for the fiber photometry data of dandiset 001528.

Hadjas et al. (2025), "Parkinson's Disease-vulnerable and -resilient dopamine neurons display
opposite responses to excitatory input", bioRxiv, doi:10.1101/2025.06.03.657460.

Each NWB file holds one recording of one mouse: the raw modulated photodetector signal, the
demodulated and 100 Hz downsampled 465 nm and 405 nm signals, and the dF/F computed by the lab's
MATLAB pipeline (series `deltaF_over_F_<site>`), with a table of optogenetic stimulation epochs
(start, stop, frequency). Files are streamed from the archive; nothing is written to disk. Only
the 100 Hz series and the epoch table are read.

The dandiset has no published version. `DANDISET_VERSION` is the draft, and
`DRAFT_MODIFIED` is the modification time of the draft that this entry was written against;
`check_version` reports whether the draft has changed since.

Where the parameters come from:

- The dF/F is the lab's own (stored in the files). Its recomputation in `recompute_dff` follows
  the Methods (biexponential fit of the 405 nm signal, scaled to the 465 nm signal by robust
  linear regression) with the details of the lab's MATLAB scripts as described in
  `reproduced_analysis/analysis_notes.md` of https://github.com/catalystneuro/hnasko-lab-to-nwb
  at commit deaefa7b1776a5ffb98fd50c5ff4d7b899bdaf59: the first 1 s excluded from the fit, an
  intercept in the robust fit, dF/F in percent. The MATLAB scripts themselves are not public.
- Trial windows and the baseline follow the Methods: traces aligned to stimulation onset, the
  mean dF/F over the 1 s before onset subtracted. The window from 5 s before to 10 s after onset
  is that of the MATLAB scripts (analysis_notes.md).
- The response to a train is the mean baseline-subtracted dF/F during the train (the Figure 3C
  legend, "mean dF/F during stim train"); the pre-stimulus comparison window has the length of
  the train and ends at onset, as in the MATLAB windows `preStm250ms`, `stm_n1_0s` and
  `stm_n4_0s` (analysis_notes.md). The post-stimulus (rebound) window is the 1 s after offset
  (the MATLAB windows `stm250_1250ms`, `stm1_2s` and `stm4_5s`). These are choices where the
  Methods are not explicit.
- Per mouse, trials of one condition are averaged ("trials within session and subject were
  averaged", Methods).
"""

from __future__ import annotations

import hashlib
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "001528"
DANDISET_VERSION = "draft"
DRAFT_MODIFIED = "2026-09-01T15:27:47.076206Z"

FS = 100.0                 # Hz, the downsampled series and the stored dF/F
PRE_S, POST_S = 5.0, 10.0  # trial window around onset, MATLAB scripts
BASELINE = (-1.0, 0.0)     # s, Methods: 1 s pre-stimulation baseline subtracted
DURATIONS = (0.25, 1.0, 4.0, 16.0)
FREQUENCIES = (5.0, 10.0, 20.0, 40.0)
MIN_TRAIN_S = 0.2          # epochs shorter than this are not trains (zero-length entries exist)

GROUP_PREFIX = {
    "SNr GABAergic": "GABA",
    "SNc pan-dopaminergic": "panDA",
    "Striatal dopamine release": "GRABDA",
    "Dopaminergic axon terminals": "DAterm",
    "Parkinson's resilient Vglut2+": "Vglut2",
    "Parkinson's-vulnerable Anxa1+": "Anxa1",
}


def check_version() -> dict:
    """Return the draft's modification time, asset count and whether it matches DRAFT_MODIFIED."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        raw = ds.get_raw_metadata()
        info = ds.version
    return {"modified": info.modified.isoformat(), "asset_count": info.asset_count,
            "matches_pinned": info.modified.isoformat().replace("+00:00", "Z") == DRAFT_MODIFIED,
            "name": raw.get("name")}


def nwb_assets() -> list[dict]:
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return [{"path": a.path, "asset_id": a.identifier, "size": a.size,
                 "url": a.get_content_url(follow_redirects=1, strip_query=True)}
                for a in ds.get_assets() if a.path.endswith(".nwb")]


def _str(x):
    x = x[()] if hasattr(x, "shape") else x
    return x.decode() if isinstance(x, bytes) else x


def _raw_rate(f) -> float:
    raw = f["acquisition"][[k for k in f["acquisition"] if k.startswith("raw_signal")][0]]
    if "starting_time" in raw:
        return float(raw["starting_time"].attrs["rate"])
    return float(1 / np.median(np.diff(raw["timestamps"][:100000])))


def load_file(asset: dict) -> dict:
    """Read the metadata, the 100 Hz series and the epoch table of one file."""
    last = None
    for _ in range(3):
        try:
            f = h5py.File(remfile.File(asset["url"]), "r")
            break
        except OSError as e:  # transient network errors
            last = e
    else:
        raise last
    with f:
        g = f["general"]
        ophys = f["processing/ophys"]
        dff_name = [k for k in ophys if k.startswith("deltaF_over_F_")]
        assert len(dff_name) == 1, (asset["path"], list(ophys))
        site = dff_name[0].removeprefix("deltaF_over_F_")
        series = {}
        for key, name in (("dff", f"deltaF_over_F_{site}"), ("gc", f"downsampled_calcium_signal_{site}"),
                          ("af", f"downsampled_isosbestic_control_{site}")):
            ts = ophys[name]
            series[key] = ts["data"][:].astype(float)
            series[key + "_unit"] = _str(ts["data"].attrs["unit"])
            series[key + "_has_timestamps"] = "timestamps" in ts
            if "timestamps" in ts:
                series[key + "_t"] = ts["timestamps"][:]
            else:
                rate, t0 = float(ts["starting_time"].attrs["rate"]), float(ts["starting_time"][()])
                series[key + "_t"] = t0 + np.arange(len(series[key])) / rate
        ep = f["intervals/optogenetic_epochs_table"]
        epochs = pd.DataFrame({
            "start": ep["start_time"][:], "stop": ep["stop_time"][:],
            "frequency": ep["stimulus_frequency"][:], "pulses": ep["number_pulses_per_pulse_train"][:],
            "period_ms": ep["period_in_ms"][:], "power_mW": ep["power_in_mW"][:],
            "wavelength_nm": ep["wavelength_in_nm"][:]})
        effectors = list(g["optogenetic_experiment_metadata/optogenetic_effectors"].keys())
        exp = _str(g["experiment_description"])
        group = [v for k, v in GROUP_PREFIX.items() if exp.startswith(k)]
        assert len(group) == 1, (asset["path"], exp[:80])
        rec = {
            "path": asset["path"], "asset_id": asset["asset_id"],
            "subject": _str(g["subject/subject_id"]).upper(), "subject_id_raw": _str(g["subject/subject_id"]),
            "genotype": _str(g["subject/genotype"]), "sex": _str(g["subject/sex"]),
            "session_id": _str(g["session_id"]), "session_start": _str(f["session_start_time"]),
            "experiment_description": exp, "group": group[0], "site": site,
            "fp_table_locations": sorted({x.decode() for x in g["fiber_photometry/fiber_photometry_table/location"][:]}),
            "input": "+".join(sorted(e.split("_")[-1] for e in effectors)),
            "protocol": "durations" if _str(g["session_id"]).startswith("varying_durations") else "frequencies",
            "raw_rate": _raw_rate(f),
            "epochs": epochs, **series,
        }
    rec["dff_md5"] = hashlib.md5(np.ascontiguousarray(rec["dff"]).tobytes()).hexdigest()
    return rec


def load_all(workers: int = 16) -> list[dict]:
    """Load every NWB file of the dandiset. Processes, not threads: h5py holds a global lock."""
    assets = nwb_assets()
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(load_file, assets, chunksize=1))


def label_epochs(rec: dict) -> pd.DataFrame:
    """Epochs with their train duration (rounded to the protocol's values) and whether usable.

    An epoch is dropped when it is shorter than MIN_TRAIN_S, or when its trial window does not
    lie within the recorded dF/F or is not contiguous in time. Windows holding missing values
    (`nan_in_window`) are kept; means skip the missing samples.
    """
    ep = rec["epochs"].copy()
    ep["length"] = ep.stop - ep.start
    ep["duration"] = [min(DURATIONS, key=lambda d: abs(d - x)) for x in ep.length]
    ts = rec["dff_t"]
    ep["in_signal"] = (ep.start - PRE_S >= ts[0]) & (ep.start + POST_S <= ts[-1])
    # the window's samples must be contiguous in time (some files hold segments separated by gaps)
    pre, post = int(PRE_S * FS), int(POST_S * FS)
    idx = np.searchsorted(ts, ep.start.values, side="right") - 1
    lo, hi = np.clip(idx - pre, 0, len(ts) - 1), np.clip(idx + post, 0, len(ts) - 1)
    ep["contiguous"] = np.abs((ts[hi] - ts[lo]) - (pre + post) / FS) < 1.5 / FS
    sig = rec["dff"]
    ep["nan_in_window"] = [bool(np.isnan(sig[a:b + 1]).any()) for a, b in zip(lo, hi)]
    ep["is_train"] = ep.length >= MIN_TRAIN_S
    ep["usable"] = ep.in_signal & ep.contiguous & ep.is_train
    return ep


def trial_matrix(signal: np.ndarray, times: np.ndarray, onsets: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Trials x samples, from PRE_S before to POST_S after each onset, with the mean over BASELINE
    subtracted from each trial. The onset sample is the last one at or before the onset time
    (the MATLAB scripts take floor(t * 100) on a clock starting at 0)."""
    pre, post = int(PRE_S * FS), int(POST_S * FS)
    t = np.arange(-pre, post + 1) / FS
    idx = np.searchsorted(times, np.asarray(onsets), side="right") - 1
    m = np.stack([signal[i - pre:i + post + 1] for i in idx]) if len(idx) else np.empty((0, len(t)))
    base = (t >= BASELINE[0]) & (t < BASELINE[1])
    return m - np.nanmean(m[:, base], axis=1, keepdims=True), t


def window_mean(trace: np.ndarray, t: np.ndarray, a: float, b: float) -> np.ndarray:
    """Mean over the last axis for a <= t < b."""
    w = (t >= a) & (t < b)
    return np.nanmean(trace[..., w], axis=-1)


def condition_traces(rec: dict, signal: np.ndarray | None = None, shift: float = 0.0) -> pd.DataFrame:
    """One row per condition of a recording: the trial-averaged, baseline-subtracted trace.

    Conditions are the train duration for the durations protocol, and duration and frequency for
    the frequencies protocol (all trains of the durations protocol are at 40 Hz). `shift` moves
    every onset by that many seconds, for the clock check.
    """
    sig = rec["dff"] if signal is None else signal
    if shift:
        rec = dict(rec, epochs=rec["epochs"].assign(start=rec["epochs"].start + shift,
                                                    stop=rec["epochs"].stop + shift))
    ep = label_epochs(rec)
    rows = []
    for (dur, freq), e in ep[ep.usable].groupby(["duration", "frequency"]):
        m, t = trial_matrix(sig, rec["dff_t"], e.start.values)
        rows.append({"duration": dur, "frequency": freq, "n_trials": len(e),
                     "n_dropped": int(((ep.duration == dur) & (ep.frequency == freq) & ~ep.usable).sum()),
                     "trace": np.nanmean(m, axis=0), "t": t})
    return pd.DataFrame(rows)


def response_measures(trace: np.ndarray, t: np.ndarray, duration: float) -> dict:
    """Mean dF/F during the train, in the pre-stimulus window of the same length, in the 1 s after
    offset, the area under the curve during the train, and the time of the peak from onset to
    2.25 s after onset."""
    peak_w = (t >= 0) & (t < 2.25)
    return {"during": window_mean(trace, t, 0.0, duration),
            "pre": window_mean(trace, t, -duration, 0.0),
            "post": window_mean(trace, t, duration, duration + 1.0),
            "auc": np.trapezoid(trace[(t >= 0) & (t <= duration)], dx=1 / FS),
            "peak_latency": t[peak_w][np.nanargmax(trace[peak_w])]}


def recompute_dff(gc: np.ndarray, af: np.ndarray, times: np.ndarray, exclude_s: float = 1.0) -> np.ndarray:
    """dF/F in percent from the 100 Hz 465 nm (gc) and 405 nm (af) signals, as the Methods and the
    MATLAB scripts describe: a biexponential fit of af over time (first `exclude_s` excluded),
    scaled to gc by robust (Huber) linear regression with an intercept. Each contiguous segment
    (separated by missing values or gaps in time) is fitted on its own, as the frequencies
    protocol concatenates separate recordings."""
    from scipy.optimize import curve_fit
    import statsmodels.api as sm

    def biexp(z, a, b, c, d):
        return a * np.exp(b * z) + c * np.exp(d * z)

    out = np.full(len(gc), np.nan)
    good = np.isfinite(gc) & np.isfinite(af)
    breaks = np.flatnonzero(~good[1:] | ~good[:-1] | (np.diff(times) > 1.5 / FS)) + 1
    for seg in np.split(np.arange(len(gc)), breaks):
        seg = seg[good[seg]]
        if len(seg) < 10 * FS:
            continue
        x = (seg - seg[0]) / len(seg)
        fit_on = (seg - seg[0]) >= exclude_s * FS
        a0 = np.median(af[seg])
        p, _ = curve_fit(biexp, x[fit_on], af[seg][fit_on], p0=[a0 * 0.1, -5.0, a0 * 0.9, -0.1], maxfev=20000)
        fit = biexp(x, *p)
        rlm = sm.RLM(gc[seg][fit_on], sm.add_constant(fit[fit_on]), M=sm.robust.norms.HuberT()).fit()
        base = rlm.params[0] + rlm.params[1] * fit
        out[seg] = 100.0 * (gc[seg] - base) / base
    return out


# --- per-mouse response table ---------------------------------------------------------------

def recording_kind(rec: dict) -> str:
    """For Anxa1 mice: 'dual' for mice with separate DLS and SNc files (site in the session id),
    'single' for the files without a site suffix. Other groups: 'single'."""
    return "dual" if rec["session_id"].endswith(("_DLS", "_SNc")) else "single"


def response_table(recs: list[dict]) -> pd.DataFrame:
    """One row per recording and condition, with the response measures of the trial-averaged trace."""
    rows = []
    for rec in recs:
        for _, c in condition_traces(rec).iterrows():
            rows.append({"subject": rec["subject"], "group": rec["group"], "site": rec["site"],
                         "input": rec["input"], "protocol": rec["protocol"], "kind": recording_kind(rec),
                         "path": rec["path"], "duration": c.duration, "frequency": c.frequency,
                         "n_trials": c.n_trials, "n_dropped": c.n_dropped,
                         **response_measures(c.trace, c.t, c.duration)})
    return pd.DataFrame(rows)


# --- statistics -------------------------------------------------------------------------------

def paired_t(a, b) -> dict:
    from scipy import stats
    a, b = np.asarray(a, float), np.asarray(b, float)
    r = stats.ttest_rel(a, b)
    return {"test": "paired t", "n": len(a), "stat": float(r.statistic), "p": float(r.pvalue),
            "mean_diff": float(np.mean(a - b))}


def wilcoxon_w(a, b) -> dict:
    """Wilcoxon signed-rank test; `stat` is the sum of signed ranks (the W that GraphPad Prism
    reports), positive when a > b."""
    from scipy import stats
    d = np.asarray(a, float) - np.asarray(b, float)
    d = d[d != 0]
    ranks = stats.rankdata(np.abs(d))
    p = stats.wilcoxon(d).pvalue
    return {"test": "Wilcoxon", "n": len(d), "stat": float(np.sum(np.sign(d) * ranks)), "p": float(p),
            "mean_diff": float(np.mean(d))}


def friedman(matrix) -> dict:
    """Friedman test on a mice x conditions matrix (complete rows only)."""
    from scipy import stats
    m = np.asarray(matrix, float)
    m = m[np.isfinite(m).all(axis=1)]
    r = stats.friedmanchisquare(*m.T)
    return {"test": "Friedman", "n": m.shape[0], "stat": float(r.statistic), "p": float(r.pvalue)}


def rm_anova(matrix) -> dict:
    """One-way repeated-measures ANOVA on a mice x conditions matrix (complete rows only), with
    the Greenhouse-Geisser epsilon, corrected degrees of freedom and p-value."""
    from scipy import stats
    m = np.asarray(matrix, float)
    m = m[np.isfinite(m).all(axis=1)]
    n, k = m.shape
    grand = m.mean()
    ss_cond = n * ((m.mean(axis=0) - grand) ** 2).sum()
    ss_subj = k * ((m.mean(axis=1) - grand) ** 2).sum()
    ss_err = ((m - grand) ** 2).sum() - ss_cond - ss_subj
    df1, df2 = k - 1, (k - 1) * (n - 1)
    f = (ss_cond / df1) / (ss_err / df2)
    s = np.cov(m, rowvar=False)
    c = np.eye(k) - 1.0 / k
    sc = c @ s @ c
    eps = np.trace(sc) ** 2 / ((k - 1) * np.trace(sc @ sc))
    return {"test": "RM ANOVA (GG)", "n": n, "stat": float(f), "df1": float(eps * df1), "df2": float(eps * df2),
            "epsilon": float(eps), "p": float(stats.f.sf(f, eps * df1, eps * df2)),
            "p_uncorrected": float(stats.f.sf(f, df1, df2))}


def mixed_2x2(pre_a, during_a, pre_b, during_b) -> dict:
    """Two-way mixed ANOVA with two groups of mice (a, b) and two within-mouse levels (pre,
    during). For a 2 x 2 design the group effect is the pooled two-sample t-test on each mouse's
    mean over the two levels, squared, and the interaction is that on the difference, squared."""
    from scipy import stats
    pa, da, pb, db = (np.asarray(x, float) for x in (pre_a, during_a, pre_b, during_b))
    site = stats.ttest_ind((pa + da) / 2, (pb + db) / 2)
    inter = stats.ttest_ind(da - pa, db - pb)
    df2 = len(pa) + len(pb) - 2
    return {"test": "mixed ANOVA", "df": (1, df2), "F_site": float(site.statistic ** 2), "p_site": float(site.pvalue),
            "F_interaction": float(inter.statistic ** 2), "p_interaction": float(inter.pvalue)}
