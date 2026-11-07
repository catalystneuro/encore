"""Loading and measures for AJILE12, dandiset 000055, for Peterson et al. (2021), eNeuro.

Peterson, Singh, Wang, Rao & Brunton (2021), "Behavioral and Neural Variability of Naturalistic
Arm Movements", eNeuro 8(3), doi:10.1523/ENEURO.0007-21.2021.

Each NWB file holds one subject and one 24 h recording day: preprocessed ECoG at 500 Hz
(`acquisition/ElectricalSeries`, stored in microvolts with a conversion of 1e-6 to volts), the
electrode table (MNI x, y, z, group, `good`, and the paper's regression R2 per electrode), pose
of nine key points at 30 frames per second (`processing/behavior/Position`, in pixels though the
files say meters), the contralateral wrist movement events (`processing/behavior/ReachEvents`)
and their ten features (`intervals/reaches`), and coarse behaviour labels (`intervals/epochs`).
Files are streamed from the archive at the pinned version with remfile and h5py; nothing is
written to disk.

Where the parameters come from:

- The spectral method follows the claims file's opening comment (Methods, "ECoG-event
  synchronization and segmentation", and the paper's code at commit 04c6faf of
  github.com/BruntonUWBio/naturalistic_arm_movements_ecog, config.py and tfr_utils.py):
  10 s segments centred on each event; Morlet power at 1 to 121 Hz in 5 Hz steps with
  n_cycles = f/4, decimated by 50 (10 Hz bins); the 0.5 s at each end cropped off (config
  `pad_val`, `compute_tfr`), giving -4.5 to 4.5 s; 10*log10, with infinite values set to 0
  (`compute_tfr`); the mean over -1.5 to -1 s subtracted per electrode and frequency
  (`tfr_subtract_baseline(compute_mean=True)`). The code uses `tfr_morlet(use_fft=False)`;
  here the same wavelets (MNE's `morlet`, zero mean) are convolved by FFT, as MNE does with
  `use_fft=True`, which gives the same values away from the segment edges, and the edges are
  cropped. A standard choice that cannot change a result; `segment_power` is checked against
  MNE in the notebook.
- Band power (Methods, "Single-event spectral power linear regression"; Figure 5 legend): 0 to
  0.5 s, LFB 8-32 Hz (bins 11 to 31 Hz) and HFB 76-100 Hz (bins 76 to 96 Hz); the band mean
  (Methods, "averaged") as the main measure and the code's median over time bins then over
  frequency bins (Plot_banded_power_Fig5.ipynb) as a variant.
- Bad segment rejection (Methods, "ECoG-event synchronization and segmentation": "discarding
  segments with power <0 dB or with abnormally high power at 115-125 Hz (>3 SDs) compared with
  all segments"). The paper's preprocessing code is not published, so how the segment's power
  is summarised is an assumption: Welch power spectral density of each good electrode (1 s
  Hann windows, half overlap, a standard choice) in microvolts squared per Hz, averaged over
  1-200 Hz, converted to dB and averaged over good electrodes for the 0 dB test, and the same
  over 115-125 Hz for the 3 SD test, the SD taken over all of a subject's segments. The other
  reading, the mean of the log density, is returned as well (`segment_quality`).
- Projection onto the eight regions uses the paper's projection matrices deposited on Figshare
  (doi:10.6084/m9.figshare.12114408.v1, aal_XX_elecs2ROI.csv), read as the code
  `load_project_spectral_power` reads them: the first row is the electrode density, the rows
  whose mean is not zero are the electrodes in order, bad electrodes get weight 0 and each
  region's weights are renormalised to sum to 1 (`rem_bad_chans=True` in the Figure 3 to 5
  notebooks). The bad electrodes are those of the subject's first file, as the code takes the
  bad list of the first file.
- The wrist traces of Extended Data Figure 2-1 use the code's window (config
  `metadata_pos_min_time = -1.5`, `baseline_vals_movement = [-1.5, -1]`) and a 1.5 s end,
  as the claims file says.
- Time of day: the files start at midnight local time (data descriptor, Methods: "each file
  contained data from one entire 24-hour recording day that started and ended at midnight"),
  so the hour of an event is its start time in the file divided by 3600.
"""

from __future__ import annotations

import os
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "000055"
DANDISET_VERSION = "0.220127.0436"
API = "https://api.dandiarchive.org/api"

FIGSHARE_ROI = "https://api.figshare.com/v2/articles/12114408/versions/1"
ROI_COLUMNS = ["Frontal_Mid_L", "Precentral_L", "Postcentral_L", "Parietal_Inf_L",
               "SupraMarginal_L", "Temporal_Sup_L", "Temporal_Mid_L", "Temporal_Inf_L"]
ROI_NAMES = ["middle frontal", "precentral", "postcentral", "inferior parietal",
             "supramarginal", "superior temporal", "middle temporal", "inferior temporal"]

FS = 500.0
SEG_HALF_S = 5.0                 # 10 s segments centred on the event
PAD_S = 0.5                      # code: pad_val, cropped off each end
FREQS = np.arange(1, 124, 5)     # code: np.arange(1, 124, 5) = 1, 6, ..., 121 Hz
DECIM = 50                       # code: decim
TIMES = np.round(np.arange(-SEG_HALF_S + PAD_S, SEG_HALF_S - PAD_S + 1e-9, DECIM / FS), 2)
BASELINE = (-1.5, -1.0)          # Methods and code
T_AVE = (0.0, 0.5)               # Methods: first 0.5 s after onset
LFB = (8, 32)
HFB = (76, 100)
POSE_HZ = 30.0
POSE_WIN = (-1.5, 1.5)           # code: metadata_pos_min_time; end of plotting axis


def asset_url(asset_id: str) -> str:
    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


def list_assets() -> pd.DataFrame:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    rows = []
    while url:
        d = requests.get(url, timeout=60).json()
        for a in d["results"]:
            p = a["path"]
            sub = p.split("/")[0].split("-")[1]
            day = int(p.split("_ses-")[1].split("_")[0])
            rows.append({"path": p, "subject": sub, "day": day, "asset_id": a["asset_id"],
                         "size_gb": a["size"] / 1e9})
        url = d["next"]
    return pd.DataFrame(rows).sort_values(["subject", "day"]).reset_index(drop=True)


def _open(asset_id):
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def _s(v):
    return v.decode() if isinstance(v, bytes) else v


def read_session(asset_id: str) -> dict:
    """Metadata, electrodes, events with their features, and wrist traces of one file."""
    f = _open(asset_id)
    out = {"asset_id": asset_id,
           "subject_id": _s(f["general/subject/subject_id"][()]),
           "species": _s(f["general/subject/species"][()]),
           "session_id": _s(f["general/session_id"][()]),
           "session_start_time": _s(f["session_start_time"][()])}
    subj_keys = list(f["general/subject"].keys())
    out["subject_fields"] = subj_keys
    e = f["general/extracellular_ephys/electrodes"]
    el = pd.DataFrame({c: e[c][:] for c in ["x", "y", "z", "group_name", "good", "low_freq_R2",
                                             "high_freq_R2", "standard_deviation", "kurtosis"]})
    el["group_name"] = el["group_name"].map(_s)
    el["location"] = [_s(v) for v in e["location"][:]]
    out["group_desc"] = {g: _s(f[f"general/extracellular_ephys/{g}"].attrs["description"])
                         for g in f["general/extracellular_ephys"].keys()
                         if g != "electrodes"}
    out["electrodes"] = el
    es = f["acquisition/ElectricalSeries"]
    out["ecog_shape"] = es["data"].shape
    out["ecog_rate"] = float(es["starting_time"].attrs["rate"])
    out["ecog_start"] = float(es["starting_time"][()])
    out["ecog_unit"] = _s(es["data"].attrs["unit"])
    out["ecog_conversion"] = float(es["data"].attrs["conversion"])
    out["ecog_electrodes"] = es["electrodes"][:]
    r = f["intervals/reaches"]
    ev = pd.DataFrame({c: r[c][:] for c in r.attrs["colnames"]})
    ev.columns = [_s(c) for c in ev.columns]
    out["reach_columns"] = list(ev.columns)
    ev["duration"] = ev["stop_time"] - ev["start_time"]
    out["events"] = ev
    re_ = f["processing/behavior/ReachEvents"]
    out["reach_event_desc"] = _s(re_.attrs["description"])
    out["reach_event_times"] = re_["timestamps"][:]
    lab = [_s(v) for v in f["intervals/epochs/labels"][:]]
    out["epochs"] = pd.DataFrame({"start": f["intervals/epochs/start_time"][:],
                                  "stop": f["intervals/epochs/stop_time"][:], "label": lab})
    pos = f["processing/behavior/Position"]
    out["pose_names"] = list(pos.keys())
    out["pose_shape"] = pos["R_Wrist/data"].shape
    out["pose_rate"] = float(pos["R_Wrist/starting_time"].attrs["rate"])
    out["pose_start"] = float(pos["R_Wrist/starting_time"][()])
    out["pose_unit"] = _s(pos["R_Wrist/data"].attrs["unit"])
    # Wrist traces around each event, both wrists, -1.5 to 1.5 s at 30 frames per second.
    n = int(round((POSE_WIN[1] - POSE_WIN[0]) * POSE_HZ)) + 1
    tr = {}
    for w in ["L_Wrist", "R_Wrist"]:
        d = pos[f"{w}/data"]
        arr = np.full((len(ev), n, 2), np.nan)
        for k, t0 in enumerate(ev["start_time"].values):
            i0 = int(round((t0 - out["pose_start"] + POSE_WIN[0]) * out["pose_rate"]))
            if i0 >= 0 and i0 + n <= d.shape[0]:
                arr[k] = d[i0:i0 + n, :]
        tr[w] = arr
    out["wrist"] = tr
    f.close()
    return out


def load_sessions(assets: pd.DataFrame, workers: int = 8) -> list[dict]:
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(read_session, assets["asset_id"]))
    for r, (_, a) in zip(res, assets.iterrows()):
        r["subject"], r["day"], r["path"] = a["subject"], a["day"], a["path"]
    return res


def fold_angle(a):
    """Reach angle folded to -90 (down) to 90 (up) degrees, if not already."""
    a = np.asarray(a, float) % 360
    out = np.where(a > 270, a - 360, a)
    out = np.where((a >= 90) & (a <= 270), 180 - a, out)
    return out


# ---------------------------------------------------------------- regions of interest

def roi_files() -> dict:
    d = requests.get(FIGSHARE_ROI, timeout=60).json()
    return {f["name"]: (f["download_url"], f["computed_md5"]) for f in d["files"]}


def read_roi_matrix(subject: str, files: dict) -> pd.DataFrame:
    url, _ = files[f"aal_{subject}_elecs2ROI.csv"]
    return pd.read_csv(url)


def roi_weights(df: pd.DataFrame, good: np.ndarray) -> np.ndarray:
    """Electrodes x 8 weights as load_project_spectral_power(rem_bad_chans=True) builds them.

    The code keeps the rows whose mean is not zero. Where the file has one row per electrode
    of the NWB file (10 of 12 subjects, with all-zero rows for some depth electrodes), every
    row is kept in order, so that the zero rows stay with their electrodes; where it has more
    rows (S01: 98 rows, the last four all zero, for 94 electrodes), the code's rule is used.
    """
    if len(df) - 1 == len(good):
        rows = np.arange(1, len(df))       # one row per electrode, in the file's order
    else:
        rows = np.nonzero(df.transpose().mean().values != 0)[0][1:]   # the code's rule
    w = df.iloc[rows][ROI_COLUMNS].to_numpy(float)
    if len(w) != len(good):
        raise ValueError(f"{len(w)} projection rows for {len(good)} electrodes")
    w[~good] = 0
    return w / w.sum(0, keepdims=True)


# ---------------------------------------------------------------- spectral power

def _band_idx(band):
    return np.nonzero((FREQS >= band[0]) & (FREQS <= band[1]))[0]


def _tidx(lo, hi):
    return np.nonzero((TIMES >= lo - 1e-9) & (TIMES <= hi + 1e-9))[0]


_WAVELET_FFT = {}


def _wavelet_fft(n_fft: int) -> np.ndarray:
    """FFTs of MNE's Morlet wavelets (mne.time_frequency.morlet, zero_mean=True) for FREQS."""
    if n_fft not in _WAVELET_FFT:
        ws = []
        for f, nc in zip(FREQS, FREQS / 4.0):
            sigma_t = nc / (2.0 * np.pi * f)
            t = np.arange(0.0, 5.0 * sigma_t, 1.0 / FS)
            t = np.r_[-t[::-1], t[1:]]
            osc = np.exp(2.0 * 1j * np.pi * f * t) - np.exp(-2.0 * (np.pi * f * sigma_t) ** 2)
            w = osc * np.exp(-(t ** 2) / (2.0 * sigma_t ** 2))
            w /= np.sqrt(0.5) * np.linalg.norm(w.ravel())
            ws.append(w)
        _WAVELET_FFT[n_fft] = (np.array([np.fft.fft(w, n_fft) for w in ws]),
                               np.array([len(w) for w in ws]))
    return _WAVELET_FFT[n_fft]


def segment_power(x: np.ndarray) -> np.ndarray:
    """x: electrodes x samples (10 s, microvolts) -> electrodes x freqs x times, dB, cropped.

    Convolution with each wavelet by FFT, 'same' mode as in mne.time_frequency.tfr_array_morlet
    (use_fft=True), then every 50th sample, cropped to TIMES, 10*log10 with infinite values
    set to 0 (code, compute_tfr).
    """
    n = x.shape[-1]
    n_fft = 1 << int(np.ceil(np.log2(n + 400)))
    wf, wl = _wavelet_fft(n_fft)
    xf = np.fft.fft(x, n_fft, axis=-1)
    out = np.empty((x.shape[0], len(FREQS), len(range(0, n, DECIM))))
    for i, (w, L) in enumerate(zip(wf, wl)):
        c = np.fft.ifft(xf * w[None], axis=-1)
        start = (L - 1) // 2
        c = c[:, start:start + n][:, ::DECIM]
        out[:, i] = c.real ** 2 + c.imag ** 2
    t_all = np.arange(out.shape[-1]) * DECIM / FS - SEG_HALF_S
    keep = np.nonzero((t_all >= TIMES[0] - 1e-6) & (t_all <= TIMES[-1] + 1e-6))[0]
    p = out[..., keep]
    with np.errstate(divide="ignore"):
        p = 10 * np.log10(p)
    p[np.isinf(p)] = 0
    return p


def segment_quality(x: np.ndarray, good: np.ndarray) -> tuple[float, float, float]:
    """Welch power of a segment's good electrodes (microvolts squared per Hz), in dB.

    Returns (a) 10*log10 of the power density averaged over 1-200 Hz, then averaged over
    electrodes (the reading used for the 0 dB test); (b) the same over 115-125 Hz (the 3 SD
    test); (c) the log density averaged over 1-200 Hz (the other reading of the 0 dB test).
    """
    from scipy.signal import welch
    f, pxx = welch(x[good], fs=FS, nperseg=int(FS), axis=-1)
    with np.errstate(divide="ignore"):
        a = 10 * np.log10(pxx[:, (f >= 1) & (f <= 200)].mean(-1))
        b = 10 * np.log10(pxx[:, (f >= 115) & (f <= 125)].mean(-1))
        c = 10 * np.log10(pxx[:, (f >= 1) & (f <= 200)])
    a[np.isinf(a)], b[np.isinf(b)], c[np.isinf(c)] = -300.0, -300.0, -300.0
    return float(a.mean()), float(b.mean()), float(c.mean())


def band_values(p: np.ndarray) -> dict:
    """p: ... x freqs x times (dB). Band power over 0-0.5 s: mean (Methods) and median (code)."""
    ti = _tidx(*T_AVE)
    out = {}
    for name, band in [("lfb", LFB), ("hfb", HFB)]:
        fi = _band_idx(band)
        sub = p[..., fi, :][..., ti]
        out[f"{name}_mean"] = sub.mean(axis=(-1, -2))
        out[f"{name}_median"] = np.median(np.median(sub, axis=-1), axis=-1)
    return out


def ecog_session(args) -> dict:
    """Read each event's 10 s segment of one file and reduce it.

    Returns per event: segment quality, region spectrograms (8 x freqs x times, baseline
    subtracted), region and electrode band power with and without baseline subtraction.
    `starts` are event times on the ECoG clock (seconds from the series' first sample).
    """
    asset_id, starts, weights, good = args[:4]
    max_events = args[4] if len(args) > 4 else None
    f = _open(asset_id)
    d = f["acquisition/ElectricalSeries/data"]
    t0 = float(f["acquisition/ElectricalSeries/starting_time"][()])
    n_total = d.shape[0]
    half = int(SEG_HALF_S * FS)
    bi = _tidx(*BASELINE)
    res = {k: [] for k in ["ok", "q_all", "q_hf", "q_log", "roi_spec", "roi_band", "roi_band_raw",
                           "el_band", "el_band_raw"]}
    for k, s in enumerate(starts):
        if max_events is not None and k >= max_events:
            break
        c = int(round((s - t0) * FS))
        if c - half < 0 or c + half > n_total:
            res["ok"].append(False)
            for key in ["q_all", "q_hf", "q_log"]:
                res[key].append(np.nan)
            for key in ["roi_spec", "roi_band", "roi_band_raw", "el_band", "el_band_raw"]:
                res[key].append(None)
            continue
        x = d[c - half:c + half, :].T.astype(np.float64)
        qa, qh, ql = segment_quality(x, good)
        p = segment_power(x)                                  # elec x f x t, dB
        raw_roi = np.einsum("er,eft->rft", weights, p)
        pb = p - p[..., bi].mean(-1, keepdims=True)           # baseline subtracted per electrode
        roi = np.einsum("er,eft->rft", weights, pb)
        res["ok"].append(True)
        res["q_all"].append(qa)
        res["q_hf"].append(qh)
        res["q_log"].append(ql)
        res["roi_spec"].append(roi.astype(np.float32))
        res["roi_band"].append(band_values(roi))
        res["roi_band_raw"].append(band_values(raw_roi))
        res["el_band"].append(band_values(pb))
        res["el_band_raw"].append(band_values(p))
    f.close()
    return res


def load_ecog(jobs: list, workers: int = 8) -> list[dict]:
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(ecog_session, jobs))


# ---------------------------------------------------------------- group statistics

def boot_sig_mask(curr_power: np.ndarray, baseidx: np.ndarray, rng: np.random.Generator,
                  n_perms: int = 2000, alpha: float = 0.05, use_median: bool = False) -> np.ndarray:
    """tfr_boot_sig_mask of the paper's code: curr_power is freq x time x subjects.

    The baseline time bins are shuffled within frequency and subject, the median over subjects
    is taken, ceil(n_perms / n_baseline) times; two-sided percentile p; Benjamini-Hochberg over
    all frequency and time bins at alpha; non-significant values set to 0. The average over
    subjects is the mean (plot_specs_group is called with useMedian=False), while the bootstrap
    takes the median, as in the code.
    """
    from scipy.stats import percentileofscore
    from statsmodels.stats.multitest import multipletests
    ave = np.median(curr_power, axis=2) if use_median else np.mean(curr_power, axis=2)
    n_iter = int(np.ceil(n_perms / len(baseidx)))
    nf = curr_power.shape[0]
    boot = np.zeros((nf, len(baseidx), n_iter))
    base = curr_power[:, baseidx, :]
    for it in range(n_iter):
        order = np.argsort(rng.random(base.shape), axis=1)   # shuffle time within freq, subject
        boot[:, :, it] = np.median(np.take_along_axis(base, order, axis=1), 2)
    boot = boot.reshape(nf, -1)
    p = np.zeros(ave.shape)
    for j in range(nf):
        q = percentileofscore(boot[j], ave[j], kind="rank") / 100
        p[j] = np.where(q > 0.5, 2 * (1 - q), 2 * q)
    pc = multipletests(p.ravel(), alpha=alpha, method="fdr_bh")[1].reshape(ave.shape)
    out = ave.copy()
    out[pc >= alpha] = 0
    return out


def ecog_offset(session: dict) -> float:
    """Seconds from midnight to the ECoG series' first sample.

    The files' events (`intervals/reaches`) and pose are on a clock that starts at midnight.
    Three files hold less than 24 h of ECoG (S01 day 7, S04 day 3, S06 day 3); their ECoG
    `starting_time` is 0, but `ReachEvents` and the session start time put its first sample at
    midnight plus the missing time, i.e. the series ends at midnight. The notebook checks this
    against the neural response.
    """
    return 24 * 3600.0 - session["ecog_shape"][0] / session["ecog_rate"]


def ecog_jobs(sessions: list, weights: dict, offset: bool = True) -> list:
    jobs = []
    for s in sessions:
        good = s["subject_good"]
        off = ecog_offset(s) if offset else 0.0
        jobs.append((s["asset_id"], s["events"]["start_time"].values - off, weights[s["subject"]],
                     good))
    return jobs


# ---------------------------------------------------------------- regression (timing only)

def regression_design(ev: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """The ten features of one subject's events as the claims file's opening comment sets them:
    day one-hot, time of day one-hot in 0-8, 8-16, 16-24 h, log duration, log magnitude, folded
    angle, onset speed, speech ratio, bimanual ratio, overlap and class, all z-scored."""
    cols, groups = {}, {}
    for d in sorted(ev["day"].unique()):
        cols[f"day_{d}"] = (ev["day"] == d).astype(float)
    groups["day"] = [c for c in cols]
    for b in range(3):
        cols[f"tod_{b}"] = (ev["tod_bin"] == b).astype(float)
    groups["time_of_day"] = [f"tod_{b}" for b in range(3)]
    cols["duration"] = np.log(ev["duration"])
    cols["magnitude"] = np.log(ev["magnitude"])
    groups["duration"], groups["magnitude"] = ["duration"], ["magnitude"]
    for c in ["angle", "speed", "speech", "bimanual_ratio", "bimanual_overlap", "bimanual_class"]:
        cols[c] = ev[c].astype(float)
        groups[c] = [c]
    X = pd.DataFrame(cols, index=ev.index)
    sd = X.std(ddof=0).replace(0, 1)
    return (X - X.mean()) / sd, groups


def _adj_r2(X, y):
    A = np.column_stack([np.ones(len(y)), X])
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - A @ beta
    r2 = 1 - (res @ res) / ((y - y.mean()) @ (y - y.mean()))
    n, k = len(y), A.shape[1] - 1
    return 1 - (1 - r2) * (n - 1) / (n - k - 1)


def forward_select(X: pd.DataFrame, groups: dict, y: np.ndarray) -> list:
    """Forward selection by OLS adjusted R2 (code, _forward_selected_new), over feature groups."""
    remaining, selected, current = list(groups), [], 0.0
    while remaining:
        scores = [(_adj_r2(X[sum((groups[g] for g in selected + [c]), [])].to_numpy(), y), c)
                  for c in remaining]
        best, cand = max(scores)
        if best > current:
            selected.append(cand)
            remaining.remove(cand)
            current = best
        else:
            break
    return selected


def regression_model(X, groups, y, days, rng, n_splits=200, per_train=0.9):
    """One electrode and band: Huber regression over day-balanced splits, full R2 and Delta R2.

    Used here only to time one model (sklearn HuberRegressor defaults, as the code)."""
    from sklearn.linear_model import HuberRegressor
    from sklearn.metrics import r2_score
    sel = forward_select(X, groups, y)
    cols = sum((groups[g] for g in sel), [])
    Xs = X[cols].to_numpy()
    days = np.asarray(days)
    uni = np.unique(days)
    n_test_day = int(((1 - per_train) * len(days)) // len(uni))
    r2s, dr2 = [], {g: [] for g in groups}
    for _ in range(n_splits):
        tr, te = [], []
        for d in uni:
            idx = rng.permutation(np.nonzero(days == d)[0])
            tr.extend(idx[:-n_test_day])
            te.extend(idx[-n_test_day:])
        tr, te = np.array(tr), np.array(te)
        if not cols:
            r2s.append(0.0)
            continue
        m = HuberRegressor().fit(Xs[tr], y[tr])
        full = r2_score(y[te], m.predict(Xs[te]))
        r2s.append(full)
        for g in groups:
            if g not in sel:
                dr2[g].append(0.0)
                continue
            Xsh = Xs[tr].copy()
            gi = [cols.index(c) for c in groups[g]]
            Xsh[:, gi] = Xsh[rng.permutation(len(tr))][:, gi]
            ms = HuberRegressor().fit(Xsh, y[tr])
            dr2[g].append(full - r2_score(y[te], ms.predict(Xs[te])))
    return {"selected": sel, "r2": float(np.mean(r2s)),
            "delta_r2": {g: float(np.mean(v)) if v else 0.0 for g, v in dr2.items()}}
