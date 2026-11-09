"""Loading and measures for dandiset 000036, the OpenScope differentiation experiment.

Mayner, Marshall, Billeh et al. (2022), eNeuro 9(1) ENEURO.0280-21.2021,
doi:10.1523/eneuro.0280-21.2021.

Each NWB file holds one two-photon session: dF/F per ROI (stored cells by frames), the ROI masks,
the running wheel velocity, and, per stimulus, an IndexSeries with one timestamp per displayed
frame (60 Hz, each 30 frames/s movie frame shown twice) and the movie itself (900 frames of
120 x 192 pixels). Files are streamed from the archive at the pinned version; nothing is
written to disk.

Where the parameters come from (the claims file is claims/000036/10.1523-eneuro.0280-21.2021.yaml):

- The measure ND (`nd_trial`) follows the claims file's opening comment, which cites the paper's
  code (https://github.com/wmayner/openscope-differentiation at commit 2d959bd,
  spectral_differentiation.py and main.ipynb): dF/F of every cell over the trial, truncated to a
  whole number of states (at most 23 samples dropped), the nominal 30 Hz sampling rate, |rfft|^2
  per window and cell with no taper and no detrending, states concatenated over cells, the median
  of pairwise distances, divided by sqrt(number of cells), log10. The windowed variants
  (Tukey and Kaiser) use scipy.signal.spectrogram rescaled as in the code (`scale_spectra`), and
  log-spaced frequencies use the code's `to_log_spacing`; both are named in the criterion of
  ext3-2-sensitivity.
- A trial is one presentation of a 30 s movie. Its first 2p frame is the first frame whose
  timestamp is at or after the first displayed frame, and its last is the frame before the first
  frame at or after the end of the last displayed frame (its timestamp plus 1/60 s). The paper's
  code reads start and end frames from a stimulus table that the dandiset does not hold; this
  rule is a standard choice, and the truncation to 900 samples makes the ND insensitive to a
  frame more or less at the end.
- The LME models (ML fits with a random intercept per session, likelihood ratio tests), the
  one-sided single-step post hoc tests (multcomp glht), the Tukey-adjusted pairwise tests
  (emmeans with asymptotic z) and Cohen's d with the pooled SD follow the claims file's opening
  comment and criteria, which cite stats.ipynb and analysis.py. They are implemented here with
  statsmodels and scipy, not R; the multivariate normal integrals use scipy's Genz algorithm.
- Running speed (reading (a) of the claims file's opening comment): the first wheel sample in
  each 2p frame, missing frames interpolated, a second-order Butterworth low-pass at 1 Hz applied
  forward and backward at the nominal 30 Hz frame rate (a standard choice: the series is per
  2p frame), locomotion when |filtered velocity| >= 2.5 cm/s.
"""

from __future__ import annotations

import io
import itertools
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import scipy.interpolate
import scipy.signal
import scipy.spatial
import scipy.stats
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000036"
DANDISET_VERSION = "0.230515.1917"

FS = 30.0                  # nominal 2p rate used by the paper's code (metadata.TWOP_SAMPLE_RATE)
TRUNCATION_TOLERANCE = 23  # samples, spectral_differentiation.py
DISPLAY_HZ = 60.0          # display frame rate, from the IndexSeries timestamps
LOCOMOTION_THRESHOLD = 2.5  # cm/s, Methods, Locomotion
BUTTER_CUTOFF_HZ, BUTTER_ORDER = 1.0, 2

AREA_NAMES = {"VISp": "V1", "VISl": "LM", "VISal": "AL", "VISpm": "PM", "VISam": "AM"}
AREAS = ["V1", "LM", "AL", "PM", "AM"]
LAYERS = ["L2/3", "L4", "L5"]
CRE_LAYER = {"Cux2": "L2/3", "Rorb": "L4", "Rbp4": "L5"}

# Stimulus names in the files, the names of the claims file and the paper's code, and the
# categories of the claims file's opening comment.
STIMULI = pd.DataFrame(
    [
        ("mouse_montage_1", "mouse montage 1", "natural", True, False),
        ("mouse_montage_2", "mouse montage 2", "natural", False, False),
        ("mousecam", "mousecam", "natural", True, True),
        ("conspecifics", "conspecifics", "natural", False, True),
        ("crickets", "crickets (prey)", "natural", False, True),
        ("snake", "snake (predator)", "natural", False, True),
        ("human_montage", "human montage", "natural", False, False),
        ("man_writing", "man writing", "natural", False, True),
        ("mouse_montage_1_temporal_phase_scramble", "mouse montage 1, temporal phase scramble",
         "artificial", True, False),
        ("mouse_montage_1_spatial_phase_scramble", "mouse montage 1, spatial phase scramble",
         "artificial", True, False),
        ("mousecam_spatial_phase_scramble", "mousecam, spatial phase scramble", "artificial", True,
         False),
        ("noise", "noise", "artificial", False, True),
    ],
    columns=["file_name", "stimulus", "stimulus_type", "scrambled_pair", "continuous"],
).set_index("file_name")
CONTRAST = STIMULI.loc[STIMULI.scrambled_pair, "stimulus"].tolist()
CONTINUOUS_NATURAL = STIMULI.loc[STIMULI.continuous & (STIMULI.stimulus_type == "natural"),
                                 "stimulus"].tolist()


# Archive access
# ---------------------------------------------------------------------------------------------

def list_assets():
    """Paths, sizes and S3 URLs of every asset at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = [{"path": a.path, "size": a.size, "asset_id": a.identifier,
                 "url": a.get_content_url(follow_redirects=1, strip_query=True)}
                for a in dandiset.get_assets()]
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def _open(url):
    return h5py.File(remfile.File(url), "r")


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def nwb_tree(url):
    """Every group and dataset of one file, with the shape of each dataset (data check)."""
    rows = []

    def visit(name, obj):
        rows.append({"path": "/" + name, "kind": "dataset" if isinstance(obj, h5py.Dataset) else "group",
                     "shape": obj.shape if isinstance(obj, h5py.Dataset) else None,
                     "neurodata_type": _str(obj.attrs.get("neurodata_type", ""))})

    with _open(url) as f:
        f.visititems(visit)
    return pd.DataFrame(rows)


def read_metadata(url):
    """Session metadata and array shapes, without reading the large arrays."""
    with _open(url) as f:
        ip = "/general/optophysiology/imaging_plane_1/"
        loc = eval(_str(f[ip + "location"][()]), {})  # stored as the repr of a dict
        dff = f["/processing/ophys/DfOverF/imaging_plane_1"]
        run = f["/processing/behavior/BehavioralTimeSeries/running_velocity"]
        genotype = _str(f["/general/subject/genotype"][()])
        cre = genotype.split("-")[0]
        return {
            "identifier": int(_str(f["/identifier"][()])),
            "mouse_id": int(_str(f["/general/subject/subject_id"][()])),
            "genotype": genotype,
            "cre": cre,
            "layer": CRE_LAYER.get(cre),
            "area": AREA_NAMES[loc["area"]],
            "location": loc["area"],
            "depth": int(loc["depth"]),
            "session_start_time": _str(f["/session_start_time"][()]),
            "imaging_rate": float(f[ip + "imaging_rate"][()]),
            "indicator": _str(f[ip + "indicator"][()]),
            "n_rois": dff["data"].shape[0],
            "n_frames": dff["data"].shape[1],
            "n_frame_timestamps": dff["timestamps"].shape[0],
            "n_masks": f["/processing/ophys/ImageSegmentation/PlaneSegmentation/id"].shape[0],
            "n_run": run["data"].shape[0],
            "n_run_timestamps": run["timestamps"].shape[0],
            "run_unit": _str(run["data"].attrs["unit"]),
            "stimuli": sorted(f["/stimulus/presentation"].keys()),
        }


def read_all_metadata(assets, workers=12):
    with ThreadPoolExecutor(workers) as ex:
        rows = list(ex.map(read_metadata, assets.url))
    meta = pd.DataFrame(rows)
    meta.insert(0, "path", assets.path.values)
    meta["url"] = assets.url.values
    return meta


def trial_table(f, frame_t):
    """One row per presentation of each block stimulus, with its 2p frames."""
    rows = []
    for name in STIMULI.index:
        t = f[f"/stimulus/presentation/{name}/timestamps"][:]
        idx = f[f"/stimulus/presentation/{name}/data"][:]
        breaks = np.where(np.diff(t) > 1.0)[0]
        starts = np.r_[0, breaks + 1]
        ends = np.r_[breaks + 1, len(t)]
        for trial, (a, b) in enumerate(zip(starts, ends)):
            start_t, end_t = t[a], t[b - 1] + 1.0 / DISPLAY_HZ
            first = int(np.searchsorted(frame_t, start_t, side="left"))
            stop = int(np.searchsorted(frame_t, end_t, side="left"))
            rows.append({"stimulus": STIMULI.loc[name, "stimulus"], "trial": trial,
                         "start_t": start_t, "end_t": end_t, "start_frame": first,
                         "end_frame": stop, "n_frames": stop - first,
                         "n_display": b - a, "movie_first": int(idx[a]),
                         "movie_last": int(idx[b - 1])})
    return pd.DataFrame(rows).sort_values("start_t").reset_index(drop=True)


def load_session(url, running=True):
    """dF/F (cells x frames, float64), frame times, trial table and running velocity."""
    with _open(url) as f:
        g = f["/processing/ophys/DfOverF/imaging_plane_1"]
        dff = g["data"][:]
        frame_t = g["timestamps"][:]
        out = {"dff": dff, "frame_t": frame_t[: dff.shape[1]],
               "trials": trial_table(f, frame_t[: dff.shape[1]])}
        if running:
            r = f["/processing/behavior/BehavioralTimeSeries/running_velocity"]
            v, t = r["data"][:], r["timestamps"][:]
            # Every file has one more sample than timestamps. The extra one is the first: the
            # rest equal the run_speed of the paper's Zenodo deposit, which its timestamps fit
            # (shown in the arousal notebook). It is dropped.
            if len(v) == len(t) + 1:
                v = v[1:]
            n = min(len(v), len(t))
            out["run_v"], out["run_t"] = v[:n].astype(float), t[:n]
    return out


def read_movie(url, name):
    """A stimulus movie (frames x 120 x 192, uint8) from the file's templates."""
    with _open(url) as f:
        return f[f"/stimulus/templates/{name}/data"][:]


# Neurophysiological differentiation
# ---------------------------------------------------------------------------------------------

def to_log_spacing(frequencies, spectrum, precision=8):
    """The paper's code, spectral_differentiation.to_log_spacing (frequency on the last axis)."""
    log_frequencies = np.logspace(frequencies[0], np.log10(frequencies[-1]),
                                  num=len(frequencies), base=10).round(precision)
    df = frequencies[1] - frequencies[0]
    cumulative = np.cumsum(spectrum, axis=-1) * df
    interp = scipy.interpolate.interp1d(frequencies, cumulative, axis=-1, copy=False)
    log_spectrum = np.diff(interp(log_frequencies), prepend=frequencies[0], axis=-1) / np.diff(
        frequencies, prepend=-df)
    return log_frequencies, log_spectrum


def _scale_spectra(S, window):
    scaled = S * window.sum() ** 2
    if len(window) % 2:
        scaled[..., 1:] /= 2
    else:
        scaled[..., 1:-1] /= 2
    return scaled


def spectral_states(data, state_length, log_frequency=False, window=None, window_param=None,
                    overlap=0.0, fs=FS):
    """States (window x concatenated cell spectra) of one trial, data shaped (cell, sample)."""
    nper = state_length * fs
    if not float(nper).is_integer():
        raise ValueError(f"state length {state_length} s gives fractional samples")
    nper = int(nper)
    if window is None:
        n_keep = nper * (data.shape[1] // nper)
        if data.shape[1] - n_keep > TRUNCATION_TOLERANCE:
            raise ValueError(f"truncation tolerance exceeded: {data.shape}")
        x = data[:, :n_keep].reshape(data.shape[0], -1, nper)       # cell, window, sample
        spectra = np.abs(np.fft.rfft(x, axis=-1)) ** 2
        frequencies = np.fft.rfftfreq(nper, d=1 / fs)
        spectra = np.moveaxis(spectra, 1, 0)                         # window, cell, freq
    else:
        win = scipy.signal.get_window((window, window_param), nper)
        frequencies, _, S = scipy.signal.spectrogram(
            data, axis=-1, fs=fs, window=win, nperseg=nper, noverlap=int(nper * overlap),
            detrend=False, return_onesided=True, scaling="spectrum", mode="psd")
        spectra = _scale_spectra(np.moveaxis(S, -1, 0), win)        # window, cell, freq
    if log_frequency:
        frequencies, spectra = to_log_spacing(frequencies, spectra)
    return spectra.reshape(spectra.shape[0], -1)


def nd_trial(data, state_length=1.0, metric="euclidean", log_frequency=False, window=None,
             window_param=None, overlap=0.0, fs=FS):
    """Median pairwise distance between the states of one trial (unnormalised ND)."""
    states = spectral_states(data, state_length, log_frequency, window, window_param, overlap, fs)
    return float(np.median(scipy.spatial.distance.pdist(states, metric=metric)))


def log_normalized(nd, ncells):
    return np.log10(np.asarray(nd) / np.sqrt(ncells))


# The 108 parameter sets of main.ipynb (ext3-2-sensitivity).
WINDOWS = [(None, -1.0, 0.0), ("tukey", 0.25, 0.125), ("kaiser", 14.0, 0.5)]
SENSITIVITY_SETS = [
    {"state_length": s, "metric": m, "log_frequency": lf, "window": w, "window_param": wp,
     "overlap": ov}
    for s, m, lf, (w, wp, ov) in itertools.product(
        [0.2, 0.5, 1, 2, 5, 10], ["cityblock", "euclidean", "chebyshev"], [False, True], WINDOWS)
]
MAIN_SET = {"state_length": 1, "metric": "euclidean", "log_frequency": False, "window": None,
            "window_param": -1.0, "overlap": 0.0}


def cohens_d(values, labels, a="natural", b="artificial", code_sd=False):
    """Cohen's d: mean difference over the pooled SD (sample SDs), as the Methods give it.

    With `code_sd`, the pooled SD as analysis.pooled_std_dev of the paper's code computes it: n1
    and n2 are the counts of `a` and `b`, but s1 and s2 come from a groupby, which sorts the
    labels by name, so for a = "natural" and b = "artificial" each group's SD is weighted by the
    other group's n - 1. This reproduces the code's results/effect_size.parquet (shown in the
    main notebook); it is a variant, not the Methods' formula.
    """
    values, labels = np.asarray(values, float), np.asarray(labels)
    x, y = values[labels == a], values[labels == b]
    n1, n2 = len(x), len(y)
    v1, v2 = x.var(ddof=1), y.var(ddof=1)
    if code_sd and sorted([a, b])[0] == b:
        v1, v2 = v2, v1
    pooled = np.sqrt(((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2))
    return (x.mean() - y.mean()) / pooled if pooled else 0.0


# Running speed
# ---------------------------------------------------------------------------------------------

def running_per_frame(run_v, run_t, frame_t):
    """Reading (a): first wheel sample per 2p frame, interpolated, filtered, locomotion flag."""
    frame = np.searchsorted(frame_t, run_t, side="right") - 1
    ok = (frame >= 0) & (frame < len(frame_t))
    frame, v = frame[ok], run_v[ok]
    first = np.r_[True, np.diff(frame) > 0]
    per_frame = pd.Series(np.nan, index=np.arange(len(frame_t)))
    per_frame.iloc[frame[first]] = v[first]
    per_frame = per_frame.interpolate(limit_area="inside")
    valid = per_frame.notna().to_numpy()
    filtered = np.full(len(per_frame), np.nan)
    b, a = scipy.signal.butter(BUTTER_ORDER, BUTTER_CUTOFF_HZ / (0.5 * FS), btype="lowpass")
    filtered[valid] = scipy.signal.filtfilt(b, a, per_frame.to_numpy()[valid])
    # Frames without a wheel sample count as not running: the fraction is over all 2p frames.
    locomotion = np.nan_to_num(np.abs(filtered), nan=0.0) >= LOCOMOTION_THRESHOLD
    return pd.DataFrame({"velocity": per_frame.to_numpy(), "filtered_velocity": filtered,
                         "locomotion": locomotion})


# Decoding
# ---------------------------------------------------------------------------------------------

def code_order(trials):
    """Trials in the order the paper's code stacks them (groupby trial, then stimulus name)."""
    return trials.sort_values(["trial", "stimulus"]).reset_index(drop=True)


def trial_features(dff, trials, shift=0):
    """Each trial's dF/F (frames x cells) flattened, all truncated to the shortest trial."""
    length = int(trials.n_frames.min())
    return np.stack([dff[:, a + shift: a + shift + length].T.ravel()
                     for a in trials.start_frame])


def decode(X, y):
    """Mean balanced accuracy of PCA (99% of variance) and shrinkage LDA, 5-fold stratified CV
    without shuffling (fig6-category-decoding criterion; code main.ipynb)."""
    from sklearn.decomposition import PCA
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.model_selection import StratifiedKFold, cross_val_score
    from sklearn.pipeline import Pipeline
    pipe = Pipeline([("reduce_dimensionality", PCA(n_components=0.99)),
                     ("classify", LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto"))])
    return float(cross_val_score(pipe, X, y, cv=StratifiedKFold(n_splits=5),
                                 scoring="balanced_accuracy").mean())


# One session, end to end
# ---------------------------------------------------------------------------------------------

TIMING_SHIFTS_S = [-34.0, -1.0, 1.0]   # data check: identity decoding with shifted windows
PAPER_OFFSETS = range(-8, 4)                            # data check: frames searched against the paper


def process_session(url, full=True, paper_nd=None, paper_sens=None):
    """Everything the main notebook needs from one session, so the dF/F is read once.

    `paper_nd` maps (stimulus, trial) to the paper's unnormalised ND for the same session (from
    the code's results/main.parquet); it is used only for the data check of trial timing.
    `paper_sens` maps a parameter set's index in SENSITIVITY_SETS to such a mapping for that
    set (from results/sensitivity_analysis.parquet); it checks the spectra of other sets.
    """
    import os
    import warnings
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    warnings.filterwarnings("ignore")
    S = load_session(url)
    dff_all = S["dff"]
    nan_rows = np.isnan(dff_all).any(axis=1)
    dff = dff_all[~nan_rows]
    tr = S["trials"].copy()
    ncells = dff.shape[0]
    tr["complete"] = (tr.end_frame <= dff.shape[1]) & (tr.n_frames >= 900)
    tr["nd"] = [nd_trial(dff[:, a:b]) if ok else np.nan
                for a, b, ok in zip(tr.start_frame, tr.end_frame, tr.complete)]
    tr["y"] = log_normalized(tr.nd, ncells)
    run = running_per_frame(S["run_v"], S["run_t"], S["frame_t"])
    out = {
        "trials": tr, "ncells": ncells, "n_rois": dff_all.shape[0],
        "nan_rois": int(nan_rows.sum()), "all_nan_rois": int(np.isnan(dff_all).all(axis=1).sum()),
        "n_frames": dff_all.shape[1],
        "frame_dt": np.diff(S["frame_t"]), "dff_range": (float(np.nanmin(dff)), float(np.nanmax(dff))),
        "dff_pct": np.nanpercentile(dff, [1, 50, 99]),
        "run_range": (float(np.nanmin(S["run_v"])), float(np.nanmax(S["run_v"]))),
        "run_dt": float(np.median(np.diff(S["run_t"]))),
        "run_span": (float(S["run_t"][0]), float(S["run_t"][-1])),
        "frame_span": (float(S["frame_t"][0]), float(S["frame_t"][-1])),
        "locomotion_fraction_a": float(run.locomotion.mean()),
        "signature": dff[0, :2000].copy() if ncells else None,
        "mean_trace": dff.mean(axis=0)[::30].astype(np.float32),
    }
    # Running and population activity on one clock: cross-correlation of the mean dF/F with
    # |filtered velocity| at lags of -5 to +5 s (in 2p frames).
    pop = dff.mean(axis=0)
    speed = np.abs(run.filtered_velocity.to_numpy())
    ok = np.isfinite(speed)
    lags = np.arange(-150, 151, 3)
    cc = []
    for lag in lags:
        a = pop[max(0, lag): len(pop) + min(0, lag)]
        b = speed[max(0, -lag): len(speed) - max(0, lag)]
        m = ok[max(0, -lag): len(speed) - max(0, lag)]
        cc.append(np.corrcoef(a[m], b[m])[0, 1] if m.sum() > 100 and b[m].std() > 0 else np.nan)
    out["run_xcorr"] = pd.Series(cc, index=lags / FS)
    if not full:
        return out
    complete = tr[tr.complete]
    contrast = complete[complete.stimulus.isin(CONTRAST)]
    rows = []
    for k, ps in enumerate(SENSITIVITY_SETS):
        for _, r in contrast.iterrows():
            nd = nd_trial(dff[:, r.start_frame:r.end_frame], **ps)
            rows.append({"set": k, "stimulus": r.stimulus, "trial": r.trial, "nd": nd})
    out["sensitivity"] = pd.DataFrame(rows)
    cat = code_order(contrast)
    out["decode_category"] = decode(
        trial_features(dff, cat), cat.stimulus.map(STIMULI.set_index("stimulus").stimulus_type))
    ident = code_order(complete)
    out["decode_identity"] = decode(trial_features(dff, ident), ident.stimulus.to_numpy())
    timing = {}
    for s in TIMING_SHIFTS_S:
        shift = int(round(s * FS))
        if ident.start_frame.min() + shift < 0 or (
                ident.start_frame.max() + shift + ident.n_frames.min() > dff.shape[1]):
            timing[s] = np.nan
            continue
        timing[s] = decode(trial_features(dff, ident, shift), ident.stimulus.to_numpy())
    timing[0.0] = out["decode_identity"]
    out["timing_decode"] = pd.Series(timing).sort_index()
    if paper_nd is not None:
        found = []
        for _, r in complete.iterrows():
            target = paper_nd.get((r.stimulus, r.trial))
            hits = [k for k in PAPER_OFFSETS if target is not None and abs(
                nd_trial(dff[:, r.start_frame + k: r.start_frame + k + 900]) - target) <= 1e-6 * target]
            found.append({"stimulus": r.stimulus, "trial": r.trial, "start_t": r.start_t,
                          "offset": hits[0] if len(hits) == 1 else np.nan, "n_hits": len(hits)})
        out["paper_offsets"] = pd.DataFrame(found)
        if paper_sens:
            # The spectra of other parameter sets against the paper's per-trial values
            # (results/sensitivity_analysis.parquet), at the start shift found above. The paper's
            # trial length is not known exactly, so this trial's length -2 to +2 frames and 900
            # are tried, until one matches to a relative 1e-6.
            offs = out["paper_offsets"].set_index(["stimulus", "trial"]).offset
            check = []
            for k, values in paper_sens.items():
                for _, r in contrast.iterrows():
                    target, shift = values.get((r.stimulus, r.trial)), offs.get((r.stimulus, r.trial))
                    if target is None or shift is None or not np.isfinite(shift):
                        continue
                    a = r.start_frame + int(shift)
                    best = np.inf
                    for length in [r.n_frames, r.n_frames - 1, r.n_frames + 1, 900, r.n_frames - 2, r.n_frames + 2]:
                        if a + length > dff.shape[1]:
                            continue
                        try:
                            nd = nd_trial(dff[:, a:a + length], **SENSITIVITY_SETS[k])
                        except ValueError:
                            continue
                        best = min(best, abs(nd - target) / target)
                        if best <= 1e-6:
                            break
                    check.append({"set": k, "stimulus": r.stimulus, "trial": r.trial, "rel_diff": best})
            out["sensitivity_check"] = pd.DataFrame(check)
    return out


# Statistics
# ---------------------------------------------------------------------------------------------

def _design(data, formula):
    import patsy
    y, X = patsy.dmatrices(formula, data, return_type="dataframe")
    return y.iloc[:, 0].to_numpy(), X


def fit_lme(data, formula, group="session"):
    """ML fit of a linear mixed model with a random intercept per group (lme4, REML = FALSE)."""
    import warnings
    import statsmodels.api as sm
    y, X = _design(data, formula)
    model = sm.MixedLM(y, X, groups=data[group].to_numpy())
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return _fit_best(model, formula)


def _fit_best(model, formula):
    # lbfgs and bfgs are both run and the higher finite likelihood kept; lbfgs can stop at a
    # degenerate point (random-effect variance 0, likelihood +inf), which is rejected.
    best = None
    for i, method in enumerate((["lbfgs"], ["bfgs"], ["powell", "lbfgs"], ["nm", "bfgs"])):
        if i >= 2 and best is not None and best.converged:
            break
        try:
            res = model.fit(reml=False, method=method)
        except Exception:  # noqa: BLE001 - try the next optimiser
            continue
        if not np.isfinite(res.llf) or not np.all(np.isfinite(res.bse)):
            continue
        if best is None or res.llf > best.llf + 1e-9:
            best = res
    if best is None:
        raise RuntimeError(f"no optimiser converged for {formula}")
    return best


def lrt(full, reduced):
    """Likelihood ratio test of nested ML fits: chi2, df, p."""
    chi2 = 2 * (full.llf - reduced.llf)
    df = len(full.fe_params) - len(reduced.fe_params)
    return max(chi2, 0.0), df, float(scipy.stats.chi2.sf(max(chi2, 0.0), df))


def _mvn_max_cdf(q, corr, seed=0):
    """P(max_k Z_k <= q) for Z ~ N(0, corr), by scipy's Genz integration."""
    if corr.shape[0] == 1:
        return float(scipy.stats.norm.cdf(q))
    mvn = scipy.stats.multivariate_normal(mean=np.zeros(corr.shape[0]), cov=corr,
                                          allow_singular=True, seed=seed, maxpts=200000,
                                          abseps=1e-7, releps=1e-7)
    return float(mvn.cdf(np.full(corr.shape[0], q)))


def posthoc_greater(fit, contrasts, level=0.95):
    """multcomp glht(alternative = "greater") with single-step adjustment.

    `contrasts` maps a name to {fixed-effect column: weight}. Returns the estimate, its SE, z,
    the single-step adjusted one-sided p, and the lower bound of the simultaneous interval.
    """
    names = list(fit.fe_params.index)
    K = np.array([[c.get(n, 0.0) for n in names] for c in contrasts.values()])
    beta = fit.fe_params.to_numpy()
    cov = fit.cov_params().loc[names, names].to_numpy()
    est = K @ beta
    vc = K @ cov @ K.T
    se = np.sqrt(np.diag(vc))
    corr = vc / np.outer(se, se)
    z = est / se
    p = np.array([1 - _mvn_max_cdf(zi, corr) for zi in z])
    # Simultaneous critical value: P(max Z <= c) = level.
    c = scipy.optimize.brentq(lambda q: _mvn_max_cdf(q, corr) - level, 0.5, 6.0)
    return pd.DataFrame({"estimate": est, "se": se, "z": z, "p_adj": np.clip(p, 0, 1),
                         "ci_low": est - c * se}, index=list(contrasts))


def category_models(data, factor, response="y"):
    """The layer (or area) by stimulus category models of stats.ipynb on per-trial data.

    `data` has columns session, layer, area, stimulus_type and the response. Returns the
    likelihood ratio test of the interaction and the post hoc tests per level.
    """
    levels = LAYERS if factor == "layer" else AREAS
    d = data.copy()
    d[factor] = pd.Categorical(d[factor], categories=levels)
    d["stimulus_type"] = pd.Categorical(d["stimulus_type"], categories=["artificial", "natural"])
    full = fit_lme(d, f"{response} ~ C({factor}) * C(stimulus_type)")
    reduced = fit_lme(d, f"{response} ~ C({factor}) + C(stimulus_type)")
    chi2, df, p = lrt(full, reduced)
    nat = "C(stimulus_type)[T.natural]"
    contrasts = {}
    for i, lev in enumerate(levels):
        c = {nat: 1.0}
        if i:
            c[f"C({factor})[T.{lev}]:{nat}"] = 1.0
        contrasts[lev] = c
    post = posthoc_greater(full, contrasts)
    return {"chi2": chi2, "df": df, "p": p, "posthoc": post, "n": len(d),
            "sessions": d.session.nunique()}


def emmeans_pairwise_tukey(fit, factor_levels, factor_name, level=0.95):
    """emmeans(model, pairwise ~ factor) with Tukey adjustment and asymptotic z (df = Inf)."""
    names = list(fit.fe_params.index)
    beta = fit.fe_params.to_numpy()
    cov = fit.cov_params().loc[names, names].to_numpy()
    k = len(factor_levels)
    rows = []
    for i, j in itertools.combinations(range(k), 2):
        c = np.zeros(len(names))
        for idx, sign in ((i, 1.0), (j, -1.0)):
            if idx:
                c[names.index(f"C({factor_name})[T.{factor_levels[idx]}]")] += sign
        est = c @ beta
        se = np.sqrt(c @ cov @ c)
        z = est / se
        p = scipy.stats.studentized_range.sf(abs(z) * np.sqrt(2), k, np.inf)
        q = scipy.stats.studentized_range.ppf(level, k, np.inf) / np.sqrt(2)
        rows.append({"contrast": f"{factor_levels[i]} - {factor_levels[j]}", "estimate": est,
                     "se": se, "z": z, "p_tukey": p, "ci_low": est - q * se,
                     "ci_high": est + q * se})
    return pd.DataFrame(rows)


def pearson(x, y, alternative="two-sided"):
    """Pearson r with its t statistic, p and 95% CI as R's cor.test gives them."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    n = len(x)
    r = float(np.corrcoef(x, y)[0, 1])
    t = r * np.sqrt((n - 2) / (1 - r ** 2))
    if alternative == "greater":
        p = scipy.stats.t.sf(t, n - 2)
        lo = np.tanh(np.arctanh(r) - scipy.stats.norm.ppf(0.95) / np.sqrt(n - 3))
        hi = 1.0
    else:
        p = 2 * scipy.stats.t.sf(abs(t), n - 2)
        h = scipy.stats.norm.ppf(0.975) / np.sqrt(n - 3)
        lo, hi = np.tanh(np.arctanh(r) - h), np.tanh(np.arctanh(r) + h)
    return {"r": r, "t": float(t), "df": n - 2, "p": float(p), "ci_low": float(lo),
            "ci_high": float(hi), "n": n}


# Linking to the paper's sessions
# ---------------------------------------------------------------------------------------------

CODE_COMMIT = "2d959bd71b47055d2a3fd306091fe9254ceb86fb"
CODE_RESULTS = (f"https://raw.githubusercontent.com/wmayner/openscope-differentiation/"
                f"{CODE_COMMIT}/results/")


def link_to_paper(meta, paper):
    """Match the dandiset's sessions to the paper's (results/main.parquet) on mouse id and start
    time: the NWB session_start_time minus 7 hours equals the paper's start_time (session-link)."""
    ps = (paper.groupby("session").first()[["mouse_id", "area", "layer", "ncells", "start_time"]]
          .reset_index().rename(columns={"session": "paper_session"}))
    m = meta.copy()
    m["start_minus_7h"] = pd.to_datetime(m.session_start_time.str[:23]) - pd.Timedelta(hours=7)
    out = m.merge(ps.rename(columns={"area": "paper_area", "layer": "paper_layer",
                                     "ncells": "paper_ncells", "mouse_id": "paper_mouse_id"}),
                  left_on=["mouse_id", "start_minus_7h"], right_on=["paper_mouse_id", "start_time"],
                  how="left")
    out["in_paper"] = out.paper_session.notna()
    return out


# Multivariate differentiation (fig5 claims)
# ---------------------------------------------------------------------------------------------

# umap-params.yml of the paper's code (the settings that differ from umap-learn's defaults, and
# those the file pins).
UMAP_PARAMS = {"n_neighbors": 50, "min_dist": 0.5, "n_components": 8, "metric": "euclidean",
               "init": "spectral", "random_state": 42, "transform_seed": 42, "low_memory": False,
               "spread": 1.0, "learning_rate": 1.0, "local_connectivity": 1.0,
               "negative_sample_rate": 5, "repulsion_strength": 1.0, "set_op_mix_ratio": 1.0}


def umap_session(url):
    """Mean centroid distance per contrast trial in an 8-dimensional UMAP embedding of all the
    session's frames of the 50 contrast trials (frames x cells dF/F)."""
    import os
    import warnings
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    warnings.filterwarnings("ignore")
    from umap import UMAP
    S = load_session(url, running=False)
    dff = S["dff"][~np.isnan(S["dff"]).any(axis=1)]
    tr = S["trials"]
    tr = tr[tr.stimulus.isin(CONTRAST) & (tr.end_frame <= dff.shape[1])].reset_index(drop=True)
    X = np.concatenate([dff[:, a:b].T for a, b in zip(tr.start_frame, tr.end_frame)])
    label = np.repeat(np.arange(len(tr)), (tr.end_frame - tr.start_frame).to_numpy())
    emb = UMAP(**UMAP_PARAMS).fit_transform(X)
    mcd = []
    for i in range(len(tr)):
        pts = emb[label == i]
        mcd.append(float(np.linalg.norm(pts - pts.mean(axis=0), axis=1).mean()))
    tr = tr[["stimulus", "trial", "n_frames"]].copy()
    tr["mcd"] = mcd
    return {"trials": tr, "n_frames": X.shape[0], "ncells": dff.shape[0]}


# The paper's processed data on Zenodo (arousal notebook)
# ---------------------------------------------------------------------------------------------

ZENODO_URL = "https://zenodo.org/api/records/5781567/files/data.tar.gz/content"   # doi:10.5281/zenodo.5781567


class _RangeStream(io.RawIOBase):
    """A read-only, in-order byte stream of a remote file, fetched as byte ranges by several
    threads at once (a single connection to Zenodo gives 2 to 3 MB/s, several give more). The
    chunks are handed on in order and dropped once read; nothing is written to disk."""

    def __init__(self, url, chunk=16 * 2**20, workers=16):
        import requests
        self.url, self.chunk = url, chunk
        self.size = int(requests.head(url, allow_redirects=True, timeout=60).headers["content-length"])
        self.n_chunks = -(-self.size // chunk)
        self.window = workers + 8
        self.pool = ThreadPoolExecutor(workers)
        self.local = threading.local()
        self.futures, self.next_submit, self.index = {}, 0, 0
        self.buf, self.offset = b"", 0

    def _fetch(self, i):
        import requests
        if not hasattr(self.local, "session"):
            self.local.session = requests.Session()
        start, end = i * self.chunk, min(self.size, (i + 1) * self.chunk) - 1
        for attempt in range(6):
            try:
                r = self.local.session.get(self.url, headers={"Range": f"bytes={start}-{end}"}, timeout=120)
                if r.status_code == 206 and len(r.content) == end - start + 1:
                    return r.content
            except requests.RequestException:
                pass
            time.sleep(2 * (attempt + 1))
        raise OSError(f"bytes {start}-{end} could not be fetched")

    def readable(self):
        return True

    def readinto(self, b):
        if self.offset >= len(self.buf):
            if self.index >= self.n_chunks:
                return 0
            while self.next_submit < min(self.n_chunks, self.index + self.window):
                self.futures[self.next_submit] = self.pool.submit(self._fetch, self.next_submit)
                self.next_submit += 1
            self.buf, self.offset = self.futures.pop(self.index).result(), 0
            self.index += 1
        n = min(len(b), len(self.buf) - self.offset)
        b[:n] = self.buf[self.offset:self.offset + n]
        self.offset += n
        return n

    def close(self):
        self.pool.shutdown(wait=False, cancel_futures=True)
        super().close()


def stream_zenodo(wanted, deadline, log):
    """Read members of the Zenodo tarball into memory as they stream past, until every
    member in `wanted` (a function of the member name returning True when needed, and a set of
    names that must all be seen) has been read, or until time.time() passes `deadline`.

    The tarball is gzip-compressed and cannot be read out of order: reaching a member means
    decompressing everything before it. The bytes are fetched as parallel range requests
    (`_RangeStream`) and decompressed in order. Nothing is written to disk.
    """
    import tarfile
    want, required = wanted
    got, seen = {}, []
    t0 = time.time()
    with _RangeStream(ZENODO_URL) as raw:
        tf = tarfile.open(fileobj=io.BufferedReader(raw, buffer_size=2**20), mode="r|gz")
        for m in tf:
            seen.append((m.name, m.size, time.time() - t0))
            if want(m.name):
                got[m.name] = tf.extractfile(m).read()
            if required <= set(got):
                log.append(f"all required members read after {time.time() - t0:.0f} s")
                break
            if time.time() > deadline:
                log.append(f"deadline reached after {time.time() - t0:.0f} s at {m.name}")
                break
    return got, seen


# The paper's artifact removal (load.py), for reading (b) of the claims file's opening comment.

def _interpolate(signal, **kwargs):
    return pd.Series(signal).interpolate(**kwargs)


def mask_intervals(array, intervals):
    idx = np.arange(array.shape[0])
    mask = np.zeros(array.shape[0], dtype=bool)
    for lower, upper in intervals:
        mask |= (idx >= lower) & (idx <= upper)
    return np.ma.MaskedArray(data=np.ma.getdata(array), mask=np.ma.getmaskarray(array) | mask)


def erase_transients(signal, prominence, wlen, rel_height=0.5):
    signal = np.ma.MaskedArray(signal, fill_value=np.nan)
    interpolated = _interpolate(signal.filled()).to_numpy()
    peaks, props = scipy.signal.find_peaks(interpolated, prominence=prominence, wlen=wlen)
    pdata = (props["prominences"], props["left_bases"], props["right_bases"])
    _, _, left, right = scipy.signal.peak_widths(interpolated, peaks, rel_height=rel_height,
                                                 prominence_data=pdata)
    intervals = np.stack([np.ceil(left), np.floor(right)], axis=1).astype(int)
    return mask_intervals(signal, intervals)


def clean_signal(signal, prominence, wlen, rel_height=0.5, n=None):
    """load.clean_signal: iterated removal of positive, then negative, transients."""
    def iterated(sig):
        p = prominence if np.iterable(prominence) else [prominence] * n
        w = wlen if np.iterable(wlen) else [wlen] * n
        r = rel_height if np.iterable(rel_height) else [rel_height] * len(p)
        for pp, ww, rr in zip(p, w, r):
            sig = erase_transients(sig, pp, ww, rel_height=rr)
        return sig
    cleaned = iterated(signal)
    return -iterated(-cleaned)


def running_code_reading(run_v, alignment, n_frames, params, session):
    """Reading (b): load.load_preprocessed_run with the deposit's per-session parameters, on the
    dandiset's running velocity, aligned by the deposit's stimulus_alignment (vsync to 2p frame).
    Returns per-2p-frame filtered velocity and locomotion (frames without a value count as not
    running, as in the code, where NaN >= threshold is False)."""
    alignment = np.asarray(alignment).astype(int).ravel()
    inverse = np.searchsorted(alignment, np.unique(alignment))
    inverse = inverse[inverse < len(run_v)]   # the code drops a last vsync with no sample
    v = run_v[inverse]
    frame = alignment[inverse]
    v = clean_signal(v, **params["clean_signal_params"])
    if session in params.get("bad_samples", {}):
        v = mask_intervals(v, params["bad_samples"][session])
    v = pd.Series(np.ma.filled(v.astype(float), np.nan)).interpolate(limit_area="inside")
    bw = params["butterworth_params"]
    b, a = scipy.signal.butter(bw["order"], bw["cutoff"] / (0.5 * bw["fs"]),
                               btype=bw.get("btype", "lowpass"))
    ok = v.notna().to_numpy()
    filt = np.full(len(v), np.nan)
    filt[ok] = scipy.signal.filtfilt(b, a, v.to_numpy()[ok])
    per_frame = pd.Series(np.nan, index=np.arange(n_frames))
    keep = frame < n_frames
    per_frame.iloc[frame[keep]] = filt[keep]
    per_frame = per_frame.interpolate(limit_area="inside")
    loco = np.nan_to_num(np.abs(per_frame.to_numpy()), nan=0.0) >= params["locomotion_threshold"]
    return per_frame.to_numpy(), loco


def pupil_code_reading(area, eye_alignment, n_frames, block_frames, params=None, session=None):
    """Normalized pupil diameter per 2p frame as the code computes it (load.py): pupil area
    indexed by the deposit's eye_tracking_alignment, optionally cleaned with the deposit's
    per-session parameters (reading (b)), diameter 2*sqrt(area/pi) (the code's reading; the
    Methods' semi-major axis is not in any public file), divided by its maximum over the frames
    of the 12 block stimuli."""
    a = np.asarray(area, float)[np.asarray(eye_alignment).astype(int).ravel()[:n_frames]]
    if params is not None:
        a = clean_signal(a, **params["clean_signal_params"][session])
        a = mask_intervals(a, params["bad_samples"].get(session, []))
        a = np.ma.filled(a.astype(float), np.nan)
    d = 2 * np.sqrt(a / np.pi)
    return d / np.nanmax(d[block_frames])


def arousal_session(url):
    """What the arousal notebook needs from one session: per-trial log10 ND of the contrast
    trials, the running velocity and its timestamps, the frame times, reading (a) of locomotion,
    and which frames belong to the 12 block stimuli."""
    S = load_session(url)
    dff = S["dff"][~np.isnan(S["dff"]).any(axis=1)]
    tr = S["trials"]
    block = np.zeros(dff.shape[1], dtype=bool)
    for a, b in zip(tr.start_frame, tr.end_frame):
        block[a:min(b, dff.shape[1])] = True
    c = tr[tr.stimulus.isin(CONTRAST) & (tr.end_frame <= dff.shape[1])].copy()
    c["y"] = log_normalized([nd_trial(dff[:, a:b]) for a, b in zip(c.start_frame, c.end_frame)],
                            dff.shape[0])
    run = running_per_frame(S["run_v"], S["run_t"], S["frame_t"])
    return {"trials": c, "n_frames": dff.shape[1], "frame_t": S["frame_t"], "run_v": S["run_v"],
            "run_t": S["run_t"], "loco_a": run.locomotion.to_numpy(), "block": block,
            "ncells": dff.shape[0]}
