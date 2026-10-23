"""Loading and measures for dandiset 000055 (AJILE12) and Peterson et al. (2021), eNeuro.

Other notebooks on this dandiset can import this module. It streams the NWB files from the
DANDI archive (remfile and h5py) and reads two public Figshare items of the paper by DOI.

Where the parameters come from:

- Segments of 10 s centred on each movement onset, Morlet power at 1 to 121 Hz in 5 Hz steps,
  n_cycles = frequency / 4, decimated by 50, 10*log10, minus each event's own mean over
  -1.5 to -1 s: the claims file's opening comment (Methods and the paper's code).
- LFB 8-32 Hz (bins 11 to 31 Hz) and HFB 76-100 Hz (bins 76 to 96 Hz) over 0 to 0.5 s, band
  mean (Methods) and band median (code): the claims file's opening comment.
- Region projection: the paper's own projection matrices (Figshare 10.6084/m9.figshare.12114408.v1),
  bad electrodes set to weight 0 and each region's weights renormalised to sum to 1; regions
  kept when the density row averaged over subjects exceeds 3: the claims file's opening comment.
- Rejection of segments by their power spectral density (power below 0 dB, or 115-125 Hz power
  more than 3 SD above all segments): the Methods, as the claims file gives them. The readings
  are the claims file's after the answer in questions/000055.yaml: (b1) one PSD per segment
  averaged over good electrodes, the main reading; (b2) the same per good electrode; the 3 SD
  over the subject's segments, or over all subjects' segments as a variant
  (`rejection_pooled`); and (b3), a time-resolved test, as a variant. The estimator and the
  frequencies of the 0 dB test are not given by the paper; Welch's method with 1 s windows in
  microvolts squared per Hz, and 1-200 Hz (the band of the preprocessing filter), are the
  attempt's choices (`rejection`).
- Time-of-day bins (0-8, 8-16, 16-24 h) and the folding of the reach angle: the claims file.
"""
import io
import json
import time

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "000055"
VERSION = "0.220127.0436"
API = "https://api.dandiarchive.org/api"
FS = 500.0                     # ECoG sampling rate in the files (checked in the notebook)
POSE_FS = 30.0
SEG_HALF = 5.0                 # 10 s segments centred on onset (claims file)
FREQS = np.arange(1, 122, 5)   # 1, 6, ..., 121 Hz (claims file, code)
DECIM = 50                     # 10 Hz time bins (claims file, code)
BASE = (-1.5, -1.0)            # baseline window (Methods)
KEEP = (-1.5, 1.5)             # time bins kept after the transform (covers every window used)
LFB = (8, 32)
HFB = (76, 100)
WIN = (0.0, 0.5)               # banded power window (Methods)
ROI_ARTICLE = 12114408         # Figshare "ROI projection matrices and labels", version 1
EPOCH_ARTICLE = 12115728       # Figshare "Naturalistic reach ECoG data", version 1
ROI_DOI = "10.6084/m9.figshare.12114408.v1"
EPOCH_DOI = "10.6084/m9.figshare.12115728.v1"


def assets():
    """The version's NWB assets as a DataFrame (path, asset_id, size, subject, day)."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    rows = []
    while url:
        r = requests.get(url, timeout=60).json()
        rows += r["results"]
        url = r["next"]
    df = pd.DataFrame([{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]}
                       for a in rows])
    df["subject"] = df.path.str.extract(r"sub-(\d+)/")[0].astype(int)
    df["day"] = df.path.str.extract(r"ses-(\d+)_")[0].astype(int)
    return df.sort_values(["subject", "day"]).reset_index(drop=True)


def s3_url(asset_id):
    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


def open_nwb(asset_id, cache_mb=0):
    """Open a streamed file with h5py. cache_mb sets h5py's chunk cache."""
    kw = {}
    if cache_mb:
        kw = dict(rdcc_nbytes=cache_mb * 2**20, rdcc_nslots=100003)
    return h5py.File(remfile.File(s3_url(asset_id)), "r", **kw)


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def read_meta(asset_id):
    """Everything but the ECoG and pose arrays: reaches, electrodes, epochs labels, attributes."""
    f = open_nwb(asset_id)
    out = {}
    r = f["intervals/reaches"]
    out["reaches"] = pd.DataFrame({k: r[k][:] for k in r.keys() if k != "id"})
    out["reach_events"] = f["processing/behavior/ReachEvents/timestamps"][:]
    out["reach_side"] = _s(f["processing/behavior/ReachEvents"].attrs["description"])
    e = f["general/extracellular_ephys/electrodes"]
    cols = [c for c in e.attrs["colnames"] if c != "group"]
    el = pd.DataFrame({c: e[c][:] for c in cols})
    for c in el.columns:
        if el[c].dtype == object:
            el[c] = el[c].map(_s)
    out["electrodes"] = el
    ep = f["intervals/epochs"]
    out["epochs"] = pd.DataFrame({"start": ep["start_time"][:], "stop": ep["stop_time"][:],
                                  "label": [_s(x) for x in ep["labels"][:]]})
    es = f["acquisition/ElectricalSeries"]
    out["ecog_shape"] = es["data"].shape
    out["ecog_rate"] = float(es["starting_time"].attrs["rate"])
    out["ecog_t0"] = float(es["starting_time"][()])
    out["ecog_unit"] = _s(es["data"].attrs["unit"])
    out["ecog_conversion"] = float(es["data"].attrs["conversion"])
    out["ecog_chunks"] = es["data"].chunks
    p = f["processing/behavior/Position"]
    out["pose_keys"] = sorted(p.keys())
    w = p["R_Wrist"]
    out["pose_shape"] = w["data"].shape
    out["pose_rate"] = float(w["starting_time"].attrs["rate"])
    out["pose_t0"] = float(w["starting_time"][()])
    out["pose_unit"] = _s(w["data"].attrs["unit"])
    out["session_start"] = _s(f["session_start_time"][()])
    out["subject_attrs"] = {k: _s(f["general/subject"][k][()]) for k in f["general/subject"].keys()}
    out["groups"] = {k: _s(f[f"general/extracellular_ephys/{k}"].attrs.get("description", ""))
                     for k in f["general/extracellular_ephys"].keys() if k != "electrodes"}
    out["acq"] = sorted(f["acquisition"].keys())
    f.close()
    return out


def wrist_traces(asset_id, onsets, side, t=(-1.5, 1.5)):
    """Wrist (x, y) around each onset, for the contralateral and the ipsilateral wrist.

    Returns arrays (events, frames, 2) and the time axis. Frames are the pose frames nearest
    to each onset plus offsets at 30 Hz."""
    f = open_nwb(asset_id, cache_mb=64)
    p = f["processing/behavior/Position"]
    contra = "R_Wrist" if side.startswith("r") else "L_Wrist"
    ipsi = "L_Wrist" if contra == "R_Wrist" else "R_Wrist"
    t0 = float(p[contra]["starting_time"][()])
    off = np.arange(int(round(t[0] * POSE_FS)), int(round(t[1] * POSE_FS)) + 1)
    res = {}
    for name, key in (("contra", contra), ("ipsi", ipsi)):
        d = p[key]["data"]
        n = d.shape[0]
        arr = np.full((len(onsets), len(off), 2), np.nan)
        for i, on in enumerate(onsets):
            c = int(round((on - t0) * POSE_FS))
            a, b = c + off[0], c + off[-1] + 1
            if a < 0 or b > n:
                continue
            arr[i] = d[a:b, :]
        res[name] = arr
    f.close()
    return res, off / POSE_FS


# ---------------------------------------------------------------- Figshare inputs

def figshare_files(article):
    d = requests.get(f"https://api.figshare.com/v2/articles/{article}/versions/1", timeout=60).json()
    return {x["name"]: x for x in d["files"]}


def roi_matrices():
    """The paper's projection matrices: per subject a DataFrame (electrodes x regions), and the
    density row (first numerical row of the file, as the Figshare description says)."""
    files = figshare_files(ROI_ARTICLE)
    out = {}
    for s in range(1, 13):
        name = f"aal_{s:02d}_elecs2ROI.csv"
        txt = requests.get(files[name]["download_url"], timeout=120).text
        out[s] = txt
    return out, files


def parse_roi(txt):
    df = pd.read_csv(io.StringIO(txt), header=None)
    return df


def epoch_metadata(name, files):
    """The pandas metadata stored in one Figshare MNE epochs file, read over HTTP range requests
    from the file's tag directory (the ECoG data in the file are not read)."""
    import fsspec
    from mne._fiff.constants import FIFF
    from mne._fiff.open import fiff_open
    from mne._fiff.tag import read_tag
    from mne._fiff.tree import dir_tree_find
    from mne.epochs import _prepare_read_metadata
    for attempt in range(3):
        try:
            f = fsspec.open(files[name]["download_url"], block_size=2**16,
                            cache_type="readahead").open()
            fid, tree, _ = fiff_open(f, preload=False)
            md = dir_tree_find(tree, FIFF.FIFFB_MNE_METADATA)
            s = None
            for d in md[0]["directory"]:
                if d.kind == FIFF.FIFF_DESCRIPTION:
                    s = read_tag(fid, d.pos).data
            bads = None
            meas = dir_tree_find(tree, FIFF.FIFFB_MEAS_INFO)
            for d in meas[0]["directory"]:
                if d.kind == FIFF.FIFF_MNE_CH_NAME_LIST:
                    pass
            f.close()
            return _prepare_read_metadata(s)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(5)


# ---------------------------------------------------------------- spectral power

_WAVELETS = None


def _wavelets():
    """Morlet wavelets as mne.time_frequency.morlet builds them (sigma = n_cycles / (2 pi f),
    support +-5 sigma, unit energy), n_cycles = f / 4."""
    global _WAVELETS
    if _WAVELETS is None:
        from mne.time_frequency import morlet
        _WAVELETS = morlet(FS, FREQS, n_cycles=FREQS / 4.0)
    return _WAVELETS


def morlet_power(x):
    """x: (channels, samples) in microvolts. Returns 10*log10 power, (channels, freqs, bins),
    decimated by DECIM, and the time axis of the bins relative to the segment centre."""
    from scipy.signal import fftconvolve
    ws = _wavelets()
    n = x.shape[1]
    out = np.empty((x.shape[0], len(FREQS), int(np.ceil(n / DECIM))), np.float32)
    for k, w in enumerate(ws):
        c = fftconvolve(x, w[None, :], mode="same", axes=1)
        p = (c.real ** 2 + c.imag ** 2)[:, ::DECIM]
        out[:, k, :] = 10 * np.log10(np.maximum(p, 1e-30))
    t = np.arange(out.shape[2]) * DECIM / FS - SEG_HALF
    return out, t


def welch_means(x):
    """Welch PSD per channel with 1 s windows (a standard choice; the Methods name no
    estimator), in microvolt^2/Hz. Returns the linear mean over 1-200 Hz and over 115-125 Hz
    per channel."""
    from scipy.signal import welch
    fr, p = welch(x, fs=FS, nperseg=int(FS), axis=1)
    return p[:, (fr >= 1) & (fr <= 200)].mean(1), p[:, (fr >= 115) & (fr <= 125)].mean(1)


def _band_idx(band):
    return np.where((FREQS >= band[0]) & (FREQS <= band[1]))[0]


# Morlet power is computed on -4.8 to +1.8 s of each 10 s segment. Every wavelet here has the
# same support, +-5 sigma = +-0.2 s (sigma = n_cycles / (2 pi f) = 1 / (8 pi) s), so every bin
# used (-4.5 to 1.5 s) is the same as on the full segment; -4.8 s keeps the decimation grid of
# the full segment (bins at -5 + k * 0.1 s).
SUB = 1.8


CTRL = -3.0                    # pseudo-onset of the clock check (a standard choice)


def segment_measures(x, proj=None, light=False):
    """Measures of one 10 s segment x (channels, samples), microvolts. light=True computes only
    the Welch means and the band powers (Morlet over -1.8 to 0.8 s; no clock check)."""
    wa, wh = welch_means(x)
    half = x.shape[1] // 2
    if light:
        k0, k1 = int(SUB * FS), int(0.8 * FS)
        p, t = morlet_power(x[:, half - k0:half + k1 + 1])
        t = t + SEG_HALF - SUB
    else:
        k0, k1 = int((SUB - CTRL) * FS), int(SUB * FS)
        p, t = morlet_power(x[:, half - k0:half + k1 + 1])
        t = t + SEG_HALF - (SUB - CTRL)          # time relative to onset
    lf, hf = _band_idx(LFB), _band_idx(HFB)

    def win(lo, hi):
        return (t >= lo - 1e-9) & (t <= hi + 1e-9)
    pb = p - p[:, :, win(*BASE)].mean(2, keepdims=True)
    wmask = win(*WIN)
    band = np.empty((x.shape[0], 8), np.float32)
    for j, src in enumerate((pb, p)):
        for bi, idx in enumerate((lf, hf)):
            sub = src[:, idx][:, :, wmask]
            band[:, j * 4 + bi * 2 + 0] = sub.mean((1, 2))
            band[:, j * 4 + bi * 2 + 1] = np.median(np.median(sub, 2), 1)
    # per 0.1 s bin from -1.5 s, the linear power averaged over frequencies (rejection b3)
    zb = win(KEEP[0], KEEP[1])
    binpow = (10 ** (p[:, :, zb] / 10)).mean(1).astype(np.float32)
    if light:
        return wa, wh, band, None, None, binpow
    # clock check: the same band means around a pseudo-onset at CTRL s, with its own baseline
    pc = p - p[:, :, win(CTRL + BASE[0], CTRL + BASE[1])].mean(2, keepdims=True)
    cm = win(CTRL + WIN[0], CTRL + WIN[1])
    ctrl = np.stack([pc[:, lf][:, :, cm].mean((1, 2)), pc[:, hf][:, :, cm].mean((1, 2))], 1)
    kmask = win(*KEEP)
    roi = None if proj is None else np.einsum("cr,cft->rft", proj, pb[:, :, kmask])
    return wa, wh, band, ctrl.astype(np.float32), roi, (t[kmask], binpow)


def extract_file(asset_id, onsets, proj=None, light=False):
    """Spectral measures for the events of one file, reading each chunk row of the ECoG once.

    onsets: event times in s. proj: (channels, regions) weights or None.
    Returns a dict, one row per event:
      'ok': whether the full 10 s segment is inside the recording;
      'psd_all', 'psd_hf': (events, channels) Welch mean PSD over 1-200 and 115-125 Hz;
      'band': (events, channels, 8), columns BAND_COLS;
      'ctrl': (events, channels, 2), LFB and HFB means around the pseudo-onset CTRL;
      'binpow': (events, channels, bins), power averaged over frequencies per 0.1 s bin from
      -1.5 s (to 1.5 s, or 0.8 s when light);
      'roi': (events, regions, freqs, bins) baseline-subtracted region power (if proj);
      'tbins': time of the kept bins; 'seconds': wall time."""
    t_start = time.time()
    f = open_nwb(asset_id)
    d = f["acquisition/ElectricalSeries/data"]
    n, nch = d.shape
    cs = d.chunks[0]
    half = int(SEG_HALF * FS)
    onsets = np.asarray(onsets, float)
    ne = len(onsets)
    res = {"ok": np.zeros(ne, bool), "psd_all": np.full((ne, nch), np.nan, np.float32),
           "psd_hf": np.full((ne, nch), np.nan, np.float32),
           "band": np.full((ne, nch, 8), np.nan, np.float32),
           "ctrl": np.full((ne, nch, 2), np.nan, np.float32), "roi": None, "tbins": None}
    cache = {}
    for i in np.argsort(onsets):
        c = int(round(onsets[i] * FS))
        a, b = c - half, c + half
        if a < 0 or b > n:
            continue
        c0, c1 = a // cs, (b - 1) // cs
        for k in list(cache):
            if k < c0:
                del cache[k]
        for k in range(c0, c1 + 1):
            if k not in cache:
                for attempt in range(4):
                    try:
                        cache[k] = d[k * cs:min((k + 1) * cs, n), :]
                        break
                    except Exception:
                        if attempt == 3:
                            raise
                        time.sleep(5)
        blk = np.concatenate([cache[k] for k in range(c0, c1 + 1)], axis=0)
        x = np.nan_to_num(blk[a - c0 * cs:b - c0 * cs, :].T.astype(np.float64))
        wa, wh, band, ctrl, roi, extra = segment_measures(x, proj, light)
        tb, binpow = extra if isinstance(extra, tuple) else (None, extra)
        if "binpow" not in res:
            res["binpow"] = np.full((ne,) + binpow.shape, np.nan, np.float32)
        res["binpow"][i] = binpow
        res["psd_all"][i], res["psd_hf"][i], res["band"][i] = wa, wh, band
        if ctrl is not None:
            res["ctrl"][i] = ctrl
        if roi is not None:
            if res["roi"] is None:
                res["roi"] = np.full((ne,) + roi.shape, np.nan, np.float32)
            res["roi"][i] = roi
        if tb is not None:
            res["tbins"] = tb
        res["ok"][i] = True
    f.close()
    if "binpow" not in res:
        res["binpow"] = np.full((ne, nch, 31), np.nan, np.float32)
    res["seconds"] = time.time() - t_start
    return res


def _extract_job(args):
    key, asset_id, onsets, proj = args[:4]
    light = args[4] if len(args) > 4 else False
    return key, extract_file(asset_id, onsets, proj, light)


def extract_many(jobs, workers=12):
    """jobs: list of (key, asset_id, onsets, proj). Runs files in parallel processes, the
    largest first. Returns {key: result}."""
    from concurrent.futures import ProcessPoolExecutor
    jobs = sorted(jobs, key=lambda j: -len(j[2]))
    out = {}
    with ProcessPoolExecutor(workers) as ex:
        for key, r in ex.map(_extract_job, jobs):
            out[key] = r
    return out


# band layout in res['band'][..., k]
BAND_COLS = ["lfb_mean_bl", "lfb_median_bl", "hfb_mean_bl", "hfb_median_bl",
             "lfb_mean_raw", "lfb_median_raw", "hfb_mean_raw", "hfb_median_raw"]


def fold_angle(a):
    """Fold the image angle to -90 (down) .. +90 (up) degrees, as the claims file gives it from
    the code: negate the image angle (image y points down) and fold 90-270 degrees."""
    a = -np.asarray(a, float)
    a = (a + 180) % 360 - 180          # -180..180
    a = np.where(a > 90, 180 - a, a)
    a = np.where(a < -90, -180 - a, a)
    return a


# ---------------------------------------------------------------- regions

REGIONS = ["Frontal_Mid", "Precentral", "Postcentral", "Parietal_Inf", "SupraMarginal",
           "Temporal_Sup", "Temporal_Mid", "Temporal_Inf"]
REGION_NAMES = {"Frontal_Mid": "middle frontal", "Precentral": "precentral",
                "Postcentral": "postcentral", "Parietal_Inf": "inferior parietal",
                "SupraMarginal": "supramarginal", "Temporal_Sup": "superior temporal",
                "Temporal_Mid": "middle temporal", "Temporal_Inf": "inferior temporal"}


def roi_tables(txt):
    """Parse a projection file: the density row (Series over regions) and the electrode
    weights (DataFrame, electrodes x regions), left-side columns with the '_L' dropped."""
    df = pd.read_csv(io.StringIO(txt))
    df = df[[c for c in df.columns if c.endswith("_L")]]
    df.columns = [c[:-2] for c in df.columns]
    return df.iloc[0], df.iloc[1:].reset_index(drop=True)


def projection(weights, good, regions=REGIONS):
    """Weights (electrodes x regions) with bad electrodes set to 0 and each region's column
    renormalised to sum to 1 (claims file, from the code). Rows beyond the file's channels
    are dropped by the caller."""
    w = weights[regions].to_numpy(float).copy()
    w[~np.asarray(good, bool)] = 0
    s = w.sum(0, keepdims=True)
    s[s == 0] = np.nan
    return w / s


# ---------------------------------------------------------------- regression (Figure 6)
# Every choice below is the claims file's (opening comment, "Regression method"): ten features,
# day and time of day one-hot (0-8, 8-16, 16-24 h), the others z-scored, reach duration and
# magnitude log transformed, missing bimanual ratios 0.5; forward selection by OLS adjusted R2
# on all of the subject's events, unselected features set to 0; sklearn HuberRegressor with
# its defaults; 200 random splits with equal numbers of test events from each day; Delta R2 by
# shuffling a feature (all its one-hot columns together) in the training events and scoring on
# the unshuffled test events (Methods), and on shuffled test events (code, variant).

FEATURES = ["day", "time_of_day", "reach_duration", "reach_magnitude", "reach_angle",
            "onset_speed", "speech_ratio", "bimanual_ratio", "bimanual_overlap", "bimanual_class"]


def design(ev):
    """ev: the subject's events with columns day, hour, duration, magnitude, angle_folded,
    onset_speed, speech_ratio, bimanual_ratio, bimanual_overlap, bimanual_class.
    Returns X (events, columns) and groups (feature name per column)."""
    cols, groups = [], []
    for d in sorted(ev.day.unique()):
        cols.append((ev.day == d).astype(float).to_numpy())
        groups.append("day")
    tod = np.digitize(ev.hour.to_numpy(), [8, 16])
    for b in range(3):
        cols.append((tod == b).astype(float))
        groups.append("time_of_day")
    cont = {"reach_duration": np.log(ev.duration.to_numpy()),
            "reach_magnitude": np.log(ev.magnitude.to_numpy()),
            "reach_angle": ev.angle_folded.to_numpy(),
            "onset_speed": ev.onset_speed.to_numpy(),
            "speech_ratio": ev.speech_ratio.to_numpy(),
            "bimanual_ratio": np.nan_to_num(ev.bimanual_ratio.to_numpy(), nan=0.5),
            "bimanual_overlap": ev.bimanual_overlap.to_numpy(),
            "bimanual_class": ev.bimanual_class.to_numpy()}
    for k, v in cont.items():
        sd = v.std()
        cols.append((v - v.mean()) / sd if sd > 0 else v * 0)
        groups.append(k)
    return np.column_stack(cols), np.array(groups)


def _adj_r2(X, y):
    A = np.column_stack([np.ones(len(y)), X]) if X.shape[1] else np.ones((len(y), 1))
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - A @ beta
    r2 = 1 - (res @ res) / ((y - y.mean()) @ (y - y.mean()))
    n, p = len(y), A.shape[1] - 1
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)


def forward_select(X, groups, y):
    """Greedy forward selection of features (column groups) by OLS adjusted R2."""
    chosen, best = [], -np.inf
    remaining = list(dict.fromkeys(groups))
    while remaining:
        scores = {}
        for g in remaining:
            m = np.isin(groups, chosen + [g])
            scores[g] = _adj_r2(X[:, m], y)
        g = max(scores, key=scores.get)
        if scores[g] <= best:
            break
        best = scores[g]
        chosen.append(g)
        remaining.remove(g)
    return chosen


def day_balanced_splits(days, n_splits, test_frac, rng):
    """Index arrays (train, test) with equal numbers of test events from each day."""
    days = np.asarray(days)
    ud = np.unique(days)
    per = max(1, int(round(test_frac * len(days))) // len(ud))
    per = min(per, min((days == d).sum() for d in ud) - 1)
    out = []
    for _ in range(n_splits):
        test = np.concatenate([rng.choice(np.where(days == d)[0], per, replace=False) for d in ud])
        mask = np.ones(len(days), bool)
        mask[test] = False
        out.append((np.where(mask)[0], test))
    return out


def fit_model(X, groups, y, days, seed, n_splits=200, test_frac=0.1):
    """One electrode and band. Returns dict with the selected features, the split-averaged
    test R2, Delta R2 per feature (Methods and code versions) and coefficients per column."""
    from sklearn.linear_model import HuberRegressor
    from sklearn.metrics import r2_score
    rng = np.random.default_rng(seed)
    ok = np.isfinite(y)
    X, y, days = X[ok], y[ok], np.asarray(days)[ok]
    sel = forward_select(X, groups, y)
    # Unselected features are set to 0 (code); a zero column gets a zero coefficient under
    # Huber's L2 penalty and does not change the fit, so the fit uses the selected columns.
    keep = np.isin(groups, sel)
    if not keep.any():
        keep = np.zeros(len(groups), bool)
    Xs = X[:, keep] if keep.any() else np.zeros((len(y), 1))
    gs = groups[keep] if keep.any() else np.array(["none"])
    feats = list(dict.fromkeys(groups))
    r2s, coefs = [], []
    d_m = {g: [] for g in feats}
    d_c = {g: [] for g in feats}
    for tr, te in day_balanced_splits(days, n_splits, test_frac, rng):
        h = HuberRegressor().fit(Xs[tr], y[tr])
        r2 = r2_score(y[te], h.predict(Xs[te]))
        r2s.append(r2)
        c = np.zeros(len(groups))
        if keep.any():
            c[keep] = h.coef_
        coefs.append(c)
        for g in feats:
            if g not in sel:
                d_m[g].append(0.0)
                d_c[g].append(0.0)
                continue
            m = gs == g
            Xtr = Xs[tr].copy()
            Xtr[:, m] = Xtr[rng.permutation(len(tr))][:, m]
            # warm start from the unshuffled fit: the Huber objective is convex, so the optimum is
            # the same; it only shortens the optimisation
            hs = HuberRegressor(warm_start=True)
            hs.coef_, hs.intercept_, hs.scale_ = h.coef_.copy(), h.intercept_, h.scale_
            hs.fit(Xtr, y[tr])
            d_m[g].append(r2 - r2_score(y[te], hs.predict(Xs[te])))
            Xte = Xs[te].copy()
            Xte[:, m] = Xte[rng.permutation(len(te))][:, m]
            d_c[g].append(r2 - r2_score(y[te], hs.predict(Xte)))
    return {"selected": sel, "r2": float(np.mean(r2s)),
            "delta_methods": {g: float(np.mean(v)) for g, v in d_m.items()},
            "delta_code": {g: float(np.mean(v)) for g, v in d_c.items()},
            "coef": np.mean(coefs, 0), "n": int(ok.sum())}


def _fit_job(args):
    key, X, groups, y, days, seed, kw = args
    return key, fit_model(X, groups, y, days, seed, **kw)


def fit_many(jobs, workers=4):
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return dict(ex.map(_fit_job, jobs, chunksize=4))


# ---------------------------------------------------------------- events

def clock_offset(session_start):
    """Seconds from midnight to the session start, read on the UTC clock of the stored time
    (the notebook shows the sleep labels fall at night on this reading)."""
    ss = pd.Timestamp(session_start).tz_convert("UTC")
    return ss.hour * 3600 + ss.minute * 60 + ss.second + ss.microsecond / 1e6


def events_table(A, meta, figmeta):
    """One row per DANDI event, with its features, the linked Figshare record and its
    false-positive flag. A: assets(); meta: {path: read_meta()}; figmeta: {fif name: DataFrame}."""
    rows = []
    for _, a in A.iterrows():
        m = meta[a.path]
        r = m["reaches"].copy()
        r["subject"], r["day"], r["path"], r["asset_id"] = a.subject, a.day, a.path, a.asset_id
        r["side"] = m["reach_side"]
        off = clock_offset(m["session_start"])
        r["offset"] = off
        r["hour"] = ((r.start_time) / 3600.0) % 24       # events count from midnight (see notebook)
        r["duration"] = r.stop_time - r.start_time
        r["magnitude"] = r.Reach_magnitude_px
        r["angle_folded"] = fold_angle(r.Reach_angle_degrees)
        r["onset_speed"] = r.Onset_speed_px_per_sec
        r["speech_ratio"] = r.Speech_ratio
        r["bimanual_ratio"] = r.Bimanual_ratio
        r["bimanual_overlap"] = r.Bimanual_overlap
        r["bimanual_class"] = r.Bimanual_class
        r["ev_index"] = np.arange(len(r))
        name = [k for k in figmeta if k.startswith(f"subj_{a.subject:02d}_day_{a.day}_")]
        if len(name) == 1:
            fm = figmeta[name[0]].copy()
            fm["key_ms"] = fm.event_timestamp.astype(np.int64)
            r["key_ms"] = np.round(r.start_time * 1000).astype(np.int64)
            fm = fm.drop_duplicates("key_ms")
            r = r.merge(fm.drop(columns=[c for c in fm.columns if c.endswith(("_x", "_y"))]),
                        on="key_ms", how="left", suffixes=("", "_fig"))
            r["fig_file"] = name[0]
        rows.append(r)
    return pd.concat(rows, ignore_index=True)


def _wrist_job(args):
    key, asset_id, onsets, side = args
    return key, wrist_traces(asset_id, onsets, side)


def wrist_many(jobs, workers=12):
    """jobs: list of (key, asset_id, onsets, side). Returns {key: (traces, time axis)}."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return dict(ex.map(_wrist_job, jobs))


def rejection(ev, A, meta, spec, subjects):
    """Segment rejection on the Welch PSD (Methods; the estimator is a standard choice, see the
    question in questions/000055.yaml). Returns (rej_b1, rej_b2, psd_db) over the rows of ev,
    which must hold the events of A's files in A's order.
    (b1) PSD averaged over good electrodes: mean over 1-200 Hz below 0 dB, or mean over
    115-125 Hz more than 3 SD above the subject's segments.
    (b2) the same on each good electrode; a segment fails when any good electrode fails.
    (b3) as (b1), and also a segment whose Morlet power averaged over good electrodes and
    frequencies is below 0 dB in any 0.1 s bin from -1.5 s on (ECoG zeroed by the preprocessing
    in the analysed window). Returns (rej_b1, rej_b2, psd_db, rej_b3)."""
    rej3 = np.zeros(len(ev), bool)
    rej1 = np.zeros(len(ev), bool)
    rej2 = np.zeros(len(ev), bool)
    psd_db = np.full(len(ev), np.nan)
    ok_all = np.concatenate([spec[p]["ok"] for p in A.path])
    for s in subjects:
        paths = list(A.path[A.subject == s])
        idx = np.where(ev.subject.to_numpy() == s)[0]
        good = np.concatenate([np.tile(meta[p]["electrodes"].good.to_numpy(), (len(spec[p]["ok"]), 1))
                               for p in paths])
        allc = np.concatenate([spec[p]["psd_all"] for p in paths])
        hfc = np.concatenate([spec[p]["psd_hf"] for p in paths])
        ok = ok_all[idx]
        with np.errstate(divide="ignore", invalid="ignore"):
            mean_all = 10 * np.log10(np.nansum(np.where(good, allc, 0), 1) / good.sum(1))
            mean_hf = 10 * np.log10(np.nansum(np.where(good, hfc, 0), 1) / good.sum(1))
            psd_db[idx] = np.where(ok, mean_all, np.nan)
            mu, sd = np.nanmean(mean_hf[ok]), np.nanstd(mean_hf[ok])
            rej1[idx] = ok & ((mean_all < 0) | (mean_hf > mu + 3 * sd))
            db_all = np.where(good, 10 * np.log10(allc), np.inf)
            db_hf = np.where(good, 10 * np.log10(hfc), np.nan)
            mu_c, sd_c = np.nanmean(db_hf[ok], 0), np.nanstd(db_hf[ok], 0)
            rej2[idx] = ok & ((np.min(db_all, 1) < 0) | np.any(db_hf > mu_c + 3 * sd_c, axis=1))
            bp = np.concatenate([spec[p]["binpow"] for p in paths])
            gm = np.nansum(np.where(good[:, :, None], bp, 0), 1) / good.sum(1)[:, None]
            low = np.nanmin(10 * np.log10(gm), 1) < 0
            rej3[idx] = rej1[idx] | (ok & low)
    return rej1, rej2, psd_db, rej3


def rejection_pooled(ev, A, meta, spec, subjects):
    """The variant of (b1) and (b2) the claims file allows, with the 3 SD of the 115-125 Hz
    test taken over the segments of all subjects together instead of the subject's. For (b2),
    whose test is per electrode, the mean and SD are over every good electrode of every
    segment (electrodes differ between subjects). The 0 dB test is as in `rejection`.
    Returns (rej_b1p, rej_b2p) over the rows of ev."""
    ok_all = np.concatenate([spec[p]["ok"] for p in A.path])
    n = len(ev)
    low1, low2 = np.zeros(n, bool), np.zeros(n, bool)
    hf1 = np.full(n, np.nan)
    hf2 = {}
    for s in subjects:
        paths = list(A.path[A.subject == s])
        idx = np.where(ev.subject.to_numpy() == s)[0]
        good = np.concatenate([np.tile(meta[p]["electrodes"].good.to_numpy(), (len(spec[p]["ok"]), 1))
                               for p in paths])
        allc = np.concatenate([spec[p]["psd_all"] for p in paths])
        hfc = np.concatenate([spec[p]["psd_hf"] for p in paths])
        ok = ok_all[idx]
        with np.errstate(divide="ignore", invalid="ignore"):
            low1[idx] = ok & (10 * np.log10(np.nansum(np.where(good, allc, 0), 1) / good.sum(1)) < 0)
            hf1[idx] = np.where(ok, 10 * np.log10(np.nansum(np.where(good, hfc, 0), 1) / good.sum(1)), np.nan)
            low2[idx] = ok & (np.min(np.where(good, 10 * np.log10(allc), np.inf), 1) < 0)
            hf2[s] = (idx, ok, np.where(good & ok[:, None], 10 * np.log10(hfc), np.nan))
    mu1, sd1 = np.nanmean(hf1), np.nanstd(hf1)
    rej1 = low1 | (ok_all & (hf1 > mu1 + 3 * sd1))
    vals = np.concatenate([v[2].ravel() for v in hf2.values()])
    vals = vals[np.isfinite(vals)]
    mu2, sd2 = vals.mean(), vals.std()
    rej2 = low2.copy()
    for idx, ok, db in hf2.values():
        rej2[idx] |= ok & np.any(db > mu2 + 3 * sd2, axis=1)
    return rej1, rej2


def _fit_batch(batch):
    return [_fit_job(a) for a in batch]


def regression_pipeline(file_jobs, subject_files, make_models, workers=12, batch=6):
    """Extraction and model fits in one process pool, so the fits of a subject start as soon as
    its files are read. file_jobs: (path, asset_id, onsets, None, True) per file; subject_files:
    {subject: [paths]}; make_models(subject, {path: result}) returns fit-job tuples
    (key, X, groups, y, days, seed, kwargs). Returns ({path: result}, {key: fit}, timings)."""
    from concurrent.futures import FIRST_COMPLETED, ProcessPoolExecutor, wait
    t0 = time.time()
    spec, fits, done_at = {}, {}, {}
    left = {s: set(p) for s, p in subject_files.items()}
    with ProcessPoolExecutor(workers) as ex:
        kinds = {ex.submit(_extract_job, j): "x" for j in sorted(file_jobs, key=lambda j: -len(j[2]))}
        pending = set(kinds)
        while pending:
            done, pending = wait(pending, return_when=FIRST_COMPLETED)
            for f in done:
                if kinds[f] == "x":
                    path, res = f.result()
                    spec[path] = res
                    for s in list(left):
                        left[s].discard(path)
                        if not left[s]:
                            del left[s]
                            done_at[s] = time.time() - t0
                            models = make_models(s, {p: spec[p] for p in subject_files[s]})
                            for i in range(0, len(models), batch):
                                g = ex.submit(_fit_batch, models[i:i + batch])
                                kinds[g] = "f"
                                pending.add(g)
                else:
                    for key, r in f.result():
                        fits[key] = r
    return spec, fits, {"subjects_read_at": done_at, "total": time.time() - t0}
