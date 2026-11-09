"""Loading and measures for DANDI:000559 (Markowitz, Gillis, Jay et al. 2023, Nature).

The dandiset holds one NWB file per 30-min open-field session of the paper: dLight photometry
sessions (`ses-photometry-*`), closed-loop optogenetic sessions (`ses-reinforcement-*`, some with
dLight), velocity-conditioned sessions (`ses-velocity-*`), keypoint sessions and HEK-cell imaging.
Files are streamed from the archive with remfile and read with h5py, which is much faster than
building pynwb objects for the 1942 files.

Where parameters come from:
- 30 Hz frame rate, 20-s rolling z-score, RANSAC fit of the low-passed reference without
  intercept, syllable-associated dLight as the maximum z-scored dLight from 0 to 0.3 s after a
  syllable onset: the paper's Methods ("Photometry pre-processing", "Photometry active
  referencing", "Analysing the relationship between dLight and syllable statistics").
- Rolling z-score window of 600 samples, centred, at least 30 samples; session quality criteria
  (90th percentile of the smoothed dLight dF/F above 1.5 %, dLight to reference correlation below
  0.6, no dF/F value above 1.0); exponential smoothing of 50 samples with tau 10 for those
  criteria: the paper's code (dattalab/dopamine-reinforces-spontaneous-behavior at 14ed714,
  analysis_configuration.TEMPLATE, rl_analysis/photometry/signal.py, rl_analysis/io/df.py).
- Closed-loop counts: onsets of the online syllable label in 30-s bins over the first 1800 s of a
  session, session filters (last frame after 1750 s, first frame before 180 s, under 5 % missing
  frames, no gap of 300 frames or more) and the "Monday" baseline rule: the paper's code
  (notebooks_preprocessing/behavior_01..03, rl_analysis/behavior/util.py).
"""

from __future__ import annotations

import os
import re
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000559"
DANDISET_VERSION = "0.260528.0858"
FS = 30.0
N_NAMED_SYLLABLES = 37  # labels 0..36 carry names; the rest are "Uncommon Syllable (frequency < 1%)"


# ----------------------------------------------------------------------------------------------
# Archive access
# ----------------------------------------------------------------------------------------------

def asset_table() -> pd.DataFrame:
    """All NWB assets of the pinned version, with subject and session kind parsed from the path."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = [dict(path=a.path, asset_id=a.identifier, size=a.size) for a in ds.get_assets()]
    df = pd.DataFrame(rows)
    df["is_nwb"] = df["path"].str.endswith(".nwb")
    parts = df["path"].str.extract(r"^sub-([^/]+)/sub-[^_]+_ses-([a-z]+)")
    df["subject"], df["kind"] = parts[0], parts[1]
    return df


def _url(asset_id: str) -> str:
    return (f"https://api.dandiarchive.org/api/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}"
            f"/assets/{asset_id}/download/")


def open_nwb(asset_id: str) -> h5py.File:
    """Stream one NWB file (no download to disk)."""
    import requests
    url = requests.head(_url(asset_id), allow_redirects=True, timeout=60).url.split("?")[0]
    return h5py.File(remfile.File(url), "r")


def _str(x):
    v = x[()]
    return v.decode() if isinstance(v, bytes) else v


def parallel_map(func, items, n_workers: int = 12):
    """Map over files in separate processes (h5py serialises threads)."""
    items = list(items)
    with ProcessPoolExecutor(n_workers) as ex:
        return list(ex.map(func, items, chunksize=1))


def _retry(func, *args, tries: int = 3):
    err = None
    for _ in range(tries):
        try:
            return func(*args)
        except OSError as e:  # network hiccups while streaming
            err = e
    raise err


# ----------------------------------------------------------------------------------------------
# Session metadata and loaders
# ----------------------------------------------------------------------------------------------

def _ogen(f) -> dict:
    out = {}
    if "stimulus/presentation/OptogeneticSeries" not in f:
        return out
    o = f["stimulus/presentation/OptogeneticSeries"]
    data, ts = o["data"][:], o["timestamps"][:]
    on = np.flatnonzero(data > 0)
    targets = re.findall(r"\d+", str(o.attrs.get("comments", "")))
    out["targets"] = [int(t) for t in targets]
    out["ogen_location"] = _str(f["general/optogenetics/OptogeneticStimulusSite/location"])
    out["excitation_lambda"] = float(f["general/optogenetics/OptogeneticStimulusSite/excitation_lambda"][()])
    out["pulse_on"] = ts[on]
    out["pulse_off"] = ts[np.minimum(on + 1, len(ts) - 1)]
    out["power_w"] = float(data.max()) if len(data) else np.nan
    return out


def session_meta(f) -> dict:
    g = f["general"]
    meta = dict(
        subject=_str(g["subject/subject_id"]),
        sex=_str(g["subject/sex"]),
        description=_str(f["session_description"]),
        start=pd.Timestamp(_str(f["session_start_time"])),
    )
    if "stimulus" in g:
        meta["stimulus_notes"] = _str(g["stimulus"])
    return meta


def _syllables(f, which: str):
    key = f"processing/behavior/BehavioralSyllable{which}"
    if key not in f:
        return None, None
    ts = f[key + "/timestamps"][:]
    lab = f[key + "/data"][:].astype(np.int16)
    # In some files the rows are rotated (mostly one backward jump of about a session length), and
    # in two every row is stored twice; the frames are put back in time order here. The labels
    # share the rows of the timestamps.
    order = np.argsort(ts, kind="stable")
    return ts[order], lab[order]


def _clock_order(f, which: str) -> dict:
    """Whether the stored syllable timestamps are out of time order, the number of non-ascending
    steps, the size of the largest backward step (s), the number of repeated timestamps, and the
    median interval between distinct timestamps after sorting (s)."""
    key = f"processing/behavior/BehavioralSyllable{which}/timestamps"
    if key not in f or f[key].shape[0] < 2:
        return dict(clock_rotated=False, clock_backward_steps=0, clock_jump_s=0.0, clock_repeated=0,
                    clock_dt_unique=np.nan)
    t = f[key][:]
    dt = np.diff(t)
    n = int((dt <= 0).sum())
    u = np.unique(t)
    return dict(clock_rotated=n > 0, clock_backward_steps=n, clock_jump_s=float(-dt.min()) if n else 0.0,
                clock_repeated=len(t) - len(u), clock_dt_unique=float(np.median(np.diff(u))))


def _on_clock(series_ts, values, clock):
    """Place a series on the (sorted) syllable frame clock by nearest timestamp; frames without a
    sample within 1 ms get NaN. Returns the series and the fraction of its samples placed."""
    out = np.full(len(clock), np.nan)
    idx = np.clip(np.searchsorted(clock, series_ts), 1, len(clock) - 1)
    left = np.abs(clock[idx - 1] - series_ts) <= np.abs(clock[idx] - series_ts)
    idx = np.where(left, idx - 1, idx)
    ok = np.abs(clock[idx] - series_ts) < 1e-3
    out[idx[ok]] = values[ok]
    return out, float(ok.mean()) if len(ok) else np.nan


def load_photometry_session(asset_id: str) -> dict:
    """dLight, references, offline and online syllables and 2D speed on one frame clock."""
    def _load(asset_id):
        f = open_nwb(asset_id)
        d = session_meta(f)
        d.update(_ogen(f))
        ts, off = _syllables(f, "Offline")
        _, on = _syllables(f, "Online")
        d["t"], d["offline"], d["online"] = ts, off, on
        d.update(_clock_order(f, "Offline"))
        d["has_ophys"] = "processing/ophys/SignalDfOverF" in f
        if ts is None or len(ts) == 0 or not d["has_ophys"]:
            f.close()
            return d
        o = f["processing/ophys"]
        pts = o["SignalDfOverF/timestamps"][:]
        d["signal_dff"], d["ophys_on_clock"] = _on_clock(pts, o["SignalDfOverF/data"][:], ts)
        d["reference_dff"], _ = _on_clock(pts, o["ReferenceDfOverF/data"][:], ts)
        d["reference_smoothed"], _ = _on_clock(pts, o["ReferenceDfOverFSmoothed/data"][:], ts)
        m = f["processing/behavior/moseq_extract_group"]
        d["speed_mm_per_frame"], d["speed_on_clock"] = _on_clock(
            m["speed_2d/timestamps"][:], m["speed_2d/data"][:].astype(float), ts)
        f.close()
        return d
    return _retry(_load, asset_id)


def load_closed_loop_session(asset_id: str, with_speed: bool = False) -> dict:
    """Online syllables, stimulation times and (optionally) 2D speed of a closed-loop session."""
    def _load(asset_id):
        f = open_nwb(asset_id)
        d = session_meta(f)
        d.update(_ogen(f))
        ts, on = _syllables(f, "Online")
        d["t"], d["online"] = ts, on
        d.update(_clock_order(f, "Online"))
        if with_speed and ts is not None and len(ts):
            m = f["processing/behavior/moseq_extract_group"]
            d["speed_mm_per_frame"], d["speed_on_clock"] = _on_clock(
                m["speed_2d/timestamps"][:], m["speed_2d/data"][:].astype(float), ts)
        f.close()
        return d
    return _retry(_load, asset_id)


def load_closed_loop_with_speed(asset_id: str) -> dict:
    return load_closed_loop_session(asset_id, with_speed=True)


# ----------------------------------------------------------------------------------------------
# dLight processing
# ----------------------------------------------------------------------------------------------

def rereference(signal: np.ndarray, reference_smoothed: np.ndarray, seed: int = 0) -> np.ndarray:
    """Subtract the RANSAC fit (no intercept) of the low-passed reference from the dLight dF/F."""
    from sklearn import linear_model
    ok = np.isfinite(signal) & np.isfinite(reference_smoothed)
    clf = linear_model.RANSACRegressor(linear_model.LinearRegression(fit_intercept=False),
                                       random_state=seed)
    clf.fit(reference_smoothed[ok, None], signal[ok])
    out = np.full_like(signal, np.nan)
    out[ok] = signal[ok] - clf.predict(reference_smoothed[ok, None])
    return out


def rolling_z(x: np.ndarray, window: int = 600, min_periods: int = 30) -> np.ndarray:
    s = pd.Series(x)
    r = s.rolling(window, min_periods=min_periods, center=True)
    return ((s - r.mean()) / r.std()).to_numpy()


def quality(signal: np.ndarray, reference: np.ndarray) -> dict:
    """The paper's session quality metrics, on exponentially smoothed dF/F."""
    sm = lambda x: pd.Series(x).rolling(window=50, win_type="exponential", center=True).mean(tau=10)
    s, r = sm(signal), sm(reference)
    ok = s.notna() & r.notna()
    return dict(signal_max=100 * s.quantile(0.9),
                signal_reference_corr=float(np.corrcoef(s[ok], r[ok])[0, 1]),
                raw_dff_max=float(np.nanmax(signal)))


def passes_quality(q: dict, dff_threshold: float = 1.5, corr_threshold: float = 0.6,
                   raw_dff_threshold: float = 1.0) -> bool:
    return (q["signal_max"] > dff_threshold and q["signal_reference_corr"] < corr_threshold
            and q["raw_dff_max"] <= raw_dff_threshold)


# ----------------------------------------------------------------------------------------------
# Syllables
# ----------------------------------------------------------------------------------------------

def onsets(labels: np.ndarray) -> np.ndarray:
    """Frame indices where a new syllable starts (run-length encoding); the first frame counts."""
    labels = np.asarray(labels)
    return np.flatnonzero(np.r_[True, labels[1:] != labels[:-1]])


def syllable_table(t, labels, dlight_z=None, window_s: float = 0.3) -> pd.DataFrame:
    """One row per syllable instance: label, onset time, duration and the peak z-scored dLight
    from onset to onset + window_s (inclusive of the frame at window_s)."""
    on = onsets(labels)
    dur = np.diff(np.r_[t[on], t[-1] + 1 / FS])
    df = pd.DataFrame(dict(onset=on, t=t[on], syllable=labels[on], duration=dur))
    if dlight_z is not None:
        nwin = int(round(window_s * FS)) + 1
        idx = on[:, None] + np.arange(nwin)[None, :]
        valid = idx[:, -1] < len(dlight_z)
        idx = np.minimum(idx, len(dlight_z) - 1)
        w = dlight_z[idx]
        peak = np.where(np.all(np.isnan(w), axis=1), np.nan, np.nanmax(np.where(np.isnan(w), -np.inf, w), axis=1))
        peak[~valid] = np.nan
        df["peak"] = peak
        df["waveform"] = list(w)
    return df


def outgoing_entropy(labels_seq: np.ndarray, K: int) -> np.ndarray:
    """Shannon entropy (nats) of the outgoing transition distribution of each syllable."""
    a, b = labels_seq[:-1], labels_seq[1:]
    keep = (a < K) & (b < K)
    tm = np.zeros((K, K))
    np.add.at(tm, (a[keep], b[keep]), 1)
    with np.errstate(divide="ignore", invalid="ignore"):
        p = tm / tm.sum(1, keepdims=True)
        h = -np.nansum(np.where(p > 0, p * np.log(p), 0), axis=1)
    h[tm.sum(1) == 0] = np.nan
    return h


# ----------------------------------------------------------------------------------------------
# Closed-loop sessions
# ----------------------------------------------------------------------------------------------

def session_passes_filters(t: np.ndarray, first_cutoff=180.0, last_cutoff=1750.0,
                           missing_cutoff=0.05, gap_cutoff=300) -> bool:
    """The paper's filters for truncated sessions (filter_feedback_dataframe), on file time."""
    if t is None or len(t) < 2:
        return False
    gaps = np.round(np.diff(t) * FS - 1)
    frac_missing = gaps.sum() / ((t.max() - t.min()) * FS)
    return bool(t.max() > last_cutoff and t.min() < first_cutoff and frac_missing < missing_cutoff
                and gaps.max() < gap_cutoff)


def binned_onset_counts(t, labels, syllable: int, bin_s: float = 30.0, t_max: float = 1800.0):
    """Counts of onsets of `syllable` in (k*bin_s, (k+1)*bin_s], time from the first frame."""
    on = onsets(labels)
    tt = t[on] - t[0]
    tt = tt[(labels[on] == syllable)]
    edges = np.arange(0, t_max + 1e-9, bin_s)
    return np.histogram(tt[tt > 0], bins=edges)[0]


def monday_baseline(stim_day: pd.Timestamp, baseline_days: pd.Series, lookback: int = 5):
    """The baseline day the paper's code uses: among baseline days up to `lookback` days before
    the first stimulation day, the latest Monday, or the latest baseline day if there is none."""
    days = pd.Series(sorted(set(baseline_days)))
    diff = (days - stim_day).dt.days
    days = days[(diff < 0) & (diff >= -lookback)]
    if len(days) == 0:
        return None
    mondays = days[days.dt.dayofweek == 0]
    if len(mondays):
        days = mondays
    return days.max()


# ----------------------------------------------------------------------------------------------
# Statistics helpers
# ----------------------------------------------------------------------------------------------

def huber_heldout_r(x, y, rng, n_repeats: int = 20, n_splits: int = 5) -> float:
    """Pearson r between held-out Huber-regression predictions and data (repeated K-fold)."""
    from sklearn import linear_model, model_selection
    from scipy.stats import pearsonr
    x = np.asarray(x, float)[:, None]
    y = np.asarray(y, float)
    cv = model_selection.RepeatedKFold(n_splits=n_splits, n_repeats=n_repeats,
                                       random_state=int(rng.integers(1 << 31)))
    preds, vals = [], []
    for tr, te in cv.split(x):
        clf = linear_model.HuberRegressor(fit_intercept=True, epsilon=1.05, max_iter=500)
        clf.fit(x[tr], y[tr])
        preds.append(clf.predict(x[te]))
        vals.append(y[te])
    return float(pearsonr(np.concatenate(preds), np.concatenate(vals))[0])


def set_threads(n: int = 1) -> None:
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[k] = str(n)
