"""Loading and measures for dandiset 000402 (MICrONS two-photon functional imaging).

Used by reproduce_microns_2025.ipynb. Every file is streamed from the DANDI Archive at the
pinned version with remfile and h5py; nothing is downloaded to disk.

Where parameters come from:
- DANDISET_VERSION: the version the paper cites (reference 73, "version 0.230307.2132").
- BIRTH_DATE: Methods, Timeline ("19 December 2017"), as the claims file gives it.
- Oracle clips: the clips shown 10 times in a scan (Methods, Stimulus composition: "6 oracle
  clips of 10 s each repeated 10 times").
- A repeat of the oracle sequence is the 6 trials that follow each onset of the first oracle
  clip, in trial order (claims file, oracle-same-order, from the paper's code
  Fig 3/panel_f/get_data.ipynb).
- oracle_score: "the jackknife mean of correlations between each oracle trial and the mean of
  the remaining trials" (Methods, Oracle score, as the claims file gives it). The trace is
  sampled at the scan's frame times inside each trial; frames are aligned across repeats by
  their index from the trial onset. This alignment is a standard choice that cannot change the
  outcome, since all repeats are sampled at the same rate.
"""

import multiprocessing as mp
from datetime import date

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "000402"
DANDISET_VERSION = "0.230307.2132"
API = "https://api.dandiarchive.org/api"
BIRTH_DATE = date(2017, 12, 19)
N_WORKERS = 10


def list_assets():
    """Asset table of the pinned version: path, asset id and size, with session and scan."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in page["results"]]
        url = page["next"]
    df = pd.DataFrame(rows)
    key = df.path.str.extract(r"ses-(\d+)-scan-(\d+)").astype(int)
    df["session"], df["scan"] = key[0], key[1]
    return df.sort_values(["session", "scan"]).reset_index(drop=True)


def open_asset(asset_id):
    """Open an asset for streaming; returns an h5py File."""
    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return h5py.File(remfile.File(r.headers["Location"]), "r")


def _str(x):
    return x.decode() if isinstance(x, bytes) else x


def _table(g):
    out = {}
    for c in g.keys():
        if c.endswith("_index"):
            continue
        v = g[c][:]
        if v.dtype == object:
            v = np.array([_str(s) for s in v], dtype=object)
        out[c] = v
    return pd.DataFrame(out)


def _rate(t):
    """Median sampling rate, ignoring missing (NaN) timestamps."""
    return 1.0 / np.nanmedian(np.diff(t))


def scan_metadata(asset_id):
    """Everything the analysis uses from one file except the traces and image data.

    Returns a dict with the session metadata, one row per field (rate, depth, field of view,
    ROI counts by mask type and the EM columns), the three stimulus tables, and the time ranges
    and rates of the imaging, treadmill and eye data.
    """
    f = open_asset(asset_id)
    out = {"asset_id": asset_id}
    out["session_id"] = _str(f["general/session_id"][()])
    out["session_start_time"] = _str(f["session_start_time"][()])
    out["age"] = _str(f["general/subject/age"][()])
    out["subject_id"] = _str(f["general/subject/subject_id"][()])
    out["sex"] = _str(f["general/subject/sex"][()])
    out["related_publications"] = [_str(x) for x in f["general/related_publications"][:]]
    acq, oph = f["acquisition"], f["processing/ophys"]
    fields = []
    frame_ts = {}
    for name in sorted((k for k in acq.keys() if k.startswith("TwoPhotonSeries")), key=lambda k: int(k[15:])):
        i = int(name[15:])
        ts = acq[name]["timestamps"][:]
        frame_ts[i] = ts
        plane = f[f"general/optophysiology/ImagingPlane{i}"]
        ps = oph[f"ImageSegmentation/PlaneSegmentation{i}"]
        mask_type = np.array([_str(x) for x in ps["mask_type"][:]])
        row = {
            "field": i,
            "n_frames": len(ts),
            "rate_hz": _rate(ts),
            "description": _str(acq[name].attrs["description"]),
            "origin_x_um": plane["origin_coords"][0] * 1e6,
            "origin_y_um": plane["origin_coords"][1] * 1e6,
            "depth_um": plane["origin_coords"][2] * 1e6,
            "grid_spacing_um": plane["grid_spacing"][0] * 1e6,
            "imaging_rate_attr": float(plane["imaging_rate"][()]),
            "location": _str(plane["location"][()]),
            "fov_x_um": acq[name]["field_of_view"][0] * 1e6,
            "fov_y_um": acq[name]["field_of_view"][1] * 1e6,
            "dim_x": int(acq[name]["dimension"][0]),
            "dim_y": int(acq[name]["dimension"][1]),
            "image_shape": acq[name]["data"].shape,
            "n_rois": len(mask_type),
            "n_soma": int((mask_type == "soma").sum()),
            "n_artifact": int((mask_type == "artifact").sum()),
            "mask_types": sorted(set(mask_type)),
            "trace_shape": oph[f"Fluorescence/RoiResponseSeries{i}/data"].shape,
            "trace_same_ts": bool(np.array_equal(oph[f"Fluorescence/RoiResponseSeries{i}/timestamps"][:], ts)),
            "has_em_columns": "pt_root_id" in ps,
        }
        roi_ids = ps["id"][:]
        row["roi_ids_1_to_n"] = bool(np.array_equal(roi_ids, np.arange(1, len(roi_ids) + 1)))
        row["trace_rois_match"] = bool(np.array_equal(oph[f"Fluorescence/RoiResponseSeries{i}/rois"][:], np.arange(len(roi_ids))))
        if row["has_em_columns"]:
            root = ps["pt_root_id"][:]
            row["n_with_root_id"] = int(np.isfinite(root).sum())
            row["root_ids"] = root
            row["mask_type_arr"] = mask_type
        fields.append(row)
    out["fields"] = pd.DataFrame(fields)
    out["frame_ts"] = frame_ts
    out["clip"] = _table(f["intervals/Clip"])
    out["monet2"] = _table(f["intervals/Monet2"])
    out["trippy"] = _table(f["intervals/Trippy"])
    tread_t = acq["treadmill_velocity/timestamps"][:]
    out["treadmill"] = {"t0": np.nanmin(tread_t), "t1": np.nanmax(tread_t), "n": len(tread_t), "rate_hz": _rate(tread_t),
                        "max_gap_s": float(np.nanmax(np.diff(tread_t))),
                        "n_nan_t": int(np.isnan(tread_t).sum()),
                        "n_nan": int(np.isnan(acq["treadmill_velocity/data"][:]).sum())}
    eye_t = acq["EyeTracking/eye_position/timestamps"][:]
    pupil = acq["PupilTracking/pupil_major_radius/data"][:]
    eye = acq["EyeTracking/eye_position/data"][:]
    out["eye"] = {"t0": np.nanmin(eye_t), "t1": np.nanmax(eye_t), "n": len(eye_t), "rate_hz": _rate(eye_t),
                  "max_gap_s": float(np.nanmax(np.diff(eye_t))),
                  "n_nan_t": int(np.isnan(eye_t).sum()),
                  "pupil_fit_fraction": float(np.isfinite(pupil).mean()),
                  "position_fit_fraction": float(np.isfinite(eye).all(axis=1).mean()),
                  "pupil_ts_same": bool(np.array_equal(acq["PupilTracking/pupil_major_radius/timestamps"][:], eye_t, equal_nan=True)),
                  "minor_ts_same": bool(np.array_equal(acq["PupilTracking/pupil_minor_radius/timestamps"][:], eye_t, equal_nan=True))}
    video = [k for k in acq.keys() if k.startswith("Video")]
    out["video"] = {"name": video[0], "n_frames": acq[video[0]]["data"].shape[0]} if video else None
    if video:
        vt = acq[video[0]]["timestamps"][:]
        out["video"].update({"t0": vt[0], "t1": vt[-1], "rate_hz": _rate(vt)})
    other = {"stimulus/presentation": list(f["stimulus/presentation"].keys()),
             "stimulus/templates": list(f["stimulus/templates"].keys()),
             "analysis": list(f["analysis"].keys()),
             "processing/ophys": sorted(oph.keys())}
    out["other_groups"] = other
    f.close()
    return out


def load_all_metadata(asset_ids, workers=N_WORKERS):
    """scan_metadata for many files, in parallel processes (h5py serialises threads)."""
    with mp.get_context("fork").Pool(workers) as pool:
        return pool.map(scan_metadata, list(asset_ids))


def age_days(d):
    return (d - BIRTH_DATE).days


def oracle_hashes(clip):
    """Condition hashes of the clips shown 10 times in a scan (the oracle clips)."""
    counts = clip.condition_hash.value_counts()
    return list(counts[counts == 10].index)


def oracle_repeats(clip):
    """Split the oracle trials into repeats: the 6 trials from each onset of the first oracle clip.

    Returns (first_hash, list of DataFrames, one per repeat, in trial order).
    """
    clip = clip.sort_values("start_time").reset_index(drop=True)
    oracle = set(oracle_hashes(clip))
    first = clip[clip.condition_hash.isin(oracle)].iloc[0].condition_hash
    starts = clip.index[clip.condition_hash == first]
    return first, [clip.iloc[s:s + 6] for s in starts]


def oracle_score(trials):
    """Jackknife oracle score.

    trials: array (n_trials, n_frames, n_units). For each trial, the Pearson correlation over
    frames between that trial and the mean of the others, then the mean over trials, per unit.
    """
    n = trials.shape[0]
    total = trials.sum(axis=0)
    scores = []
    for k in range(n):
        x = trials[k]
        y = (total - x) / (n - 1)
        xc, yc = x - x.mean(0), y - y.mean(0)
        r = (xc * yc).sum(0) / np.sqrt((xc ** 2).sum(0) * (yc ** 2).sum(0))
        scores.append(r)
    return np.nanmean(np.array(scores), axis=0)


def oracle_frame_index(frame_ts, onsets, n_frames):
    """Frame indices of n_frames frames from the first frame at or after each onset."""
    first = np.searchsorted(frame_ts, onsets)
    return first[:, None] + np.arange(n_frames)[None, :]


def read_trace_rows(asset_id, field, frame_index):
    """Fluorescence of every ROI of a field at the given frames (a sorted 1D index).

    Reads contiguous blocks covering the frames, so that each block is one range request.
    Returns an array (len(frame_index), n_rois).
    """
    f = open_asset(asset_id)
    d = f[f"processing/ophys/Fluorescence/RoiResponseSeries{field}/data"]
    idx = np.asarray(frame_index)
    # contiguous runs
    breaks = np.where(np.diff(idx) != 1)[0] + 1
    out = []
    for run in np.split(idx, breaks):
        out.append(d[run[0]:run[-1] + 1, :])
    f.close()
    return np.concatenate(out, axis=0)


# ---------------------------------------------------------------------------------------------
# Monet2 motion directions, from the stimulus video stored in each file.
#
# The Monet2 table gives num_directions and the trial duration but not the direction of each
# period. Each period's direction is measured here from the video: the shift between successive
# frames by phase correlation (a standard image registration method), summed over the period.
# Period boundaries are the frames where the direction of the mean shift over the 15 frames
# before and after changes by more than BOUNDARY_DEG, at least 20 frames apart. These detection
# parameters are standard choices; the notebook shows the boundaries found.

BOUNDARY_DEG = 12.0
BOUNDARY_WINDOW = 15
EDGE_S = 0.1


def frame_shifts(frames):
    """Shift (dx, dy) in pixels between successive frames, by phase correlation.

    frames: array (n, ny, nx). dy is positive upwards on the screen (rows run downwards).
    """
    from scipy import fft as sfft
    x = frames.astype(np.float32)
    x -= x.mean(axis=(1, 2), keepdims=True)
    F = sfft.fft2(x, workers=1)
    R = F[1:] * np.conj(F[:-1])
    R /= np.abs(R) + 1e-9
    r = sfft.ifft2(R, workers=1).real
    n, ny, nx = r.shape
    flat = r.reshape(n, -1).argmax(axis=1)
    iy, ix = np.unravel_index(flat, (ny, nx))
    rows = np.arange(n)

    def sub(rm, rc, rp):
        d = rm - 2 * rc + rp
        return np.where(d == 0, 0.0, 0.5 * (rm - rp) / np.where(d == 0, 1, d))

    dy = iy + sub(r[rows, (iy - 1) % ny, ix], r[rows, iy, ix], r[rows, (iy + 1) % ny, ix])
    dx = ix + sub(r[rows, iy, (ix - 1) % nx], r[rows, iy, ix], r[rows, iy, (ix + 1) % nx])
    dy = np.where(dy > ny / 2, dy - ny, dy)
    dx = np.where(dx > nx / 2, dx - nx, dx)
    return np.column_stack([dx, -dy])


def direction_boundaries(shifts, t):
    """Times (from trial onset) where the motion direction changes."""
    c = np.vstack([[0, 0], np.cumsum(shifts, axis=0)])
    n, w = len(shifts), BOUNDARY_WINDOW
    d = np.zeros(n)
    for i in range(w, n - w):
        a, b = c[i] - c[i - w], c[i + w] - c[i]
        na, nb = np.linalg.norm(a), np.linalg.norm(b)
        if na > 0 and nb > 0:
            d[i] = np.degrees(np.arccos(np.clip(a @ b / na / nb, -1, 1)))
    peaks = [i for i in range(1, n - 1) if d[i] > BOUNDARY_DEG and d[i] == d[max(0, i - 20):i + 21].max()]
    return t[np.array(peaks, dtype=int)]


def period_directions(shifts, t, n_periods, duration):
    """Direction (degrees, 0 = rightward, counter-clockwise) of each of n equal periods.

    The first and last EDGE_S seconds of each period are left out so that the boundary frames
    do not mix two directions.
    """
    out = []
    p = duration / n_periods
    for j in range(n_periods):
        m = (t[:-1] >= j * p + EDGE_S) & (t[:-1] < (j + 1) * p - EDGE_S)
        v = shifts[m].sum(axis=0)
        out.append(np.degrees(np.arctan2(v[1], v[0])) % 360)
    return np.array(out)


def monet2_trial_directions(asset_id, video_name, starts, stops, num_directions, durations):
    """For each Monet2 trial: the boundaries found and the direction of each period."""
    f = open_asset(asset_id)
    v = f[f"acquisition/{video_name}"]
    vt = v["timestamps"][:]
    out = []
    for s, e, n, dur in zip(starts, stops, num_directions, durations):
        i0, i1 = np.searchsorted(vt, [s, e])
        frames = v["data"][i0:i1, :, :, 0].astype(np.float32)
        # 2 x 2 block average: halves the cost and leaves directions unchanged.
        n_, ny, nx = frames.shape
        frames = frames[:, :ny // 2 * 2, :nx // 2 * 2].reshape(n_, ny // 2, 2, nx // 2, 2).mean(axis=(2, 4))
        t = vt[i0:i1] - s
        sh = frame_shifts(frames)
        out.append({"boundaries": direction_boundaries(sh, t),
                    "directions": period_directions(sh, t, int(n), float(dur)),
                    "n_video_frames": i1 - i0,
                    "video_rate_hz": 1.0 / np.median(np.diff(t))})
    f.close()
    return out


def _monet2_scan(args):
    return monet2_trial_directions(*args)


def monet2_directions_all(jobs, workers=N_WORKERS):
    """monet2_trial_directions for several scans in parallel; jobs are argument tuples."""
    with mp.get_context("fork").Pool(workers) as pool:
        return pool.map(_monet2_scan, jobs)


def boundary_period(boundaries, nominal):
    """Period estimated from boundary times: slope of boundary time on its period index."""
    b = np.asarray(boundaries)
    if len(b) < 2:
        return np.nan, np.nan
    k = np.round(b / nominal)
    if len(np.unique(k)) < 2:
        return np.nan, np.nan
    slope, offset = np.polyfit(k, b, 1)
    return slope, offset


def n_distinct_directions(directions, tol_deg=10.0):
    """Number of distinct directions: directions closer than tol_deg (circularly) are one.

    tol_deg is a standard choice, well below the 22.5 degrees that separate 16 evenly spaced
    directions and above the error of the estimate shown in the notebook.
    """
    d = np.sort(np.asarray(directions) % 360)
    gaps = np.diff(np.concatenate([d, [d[0] + 360]]))
    return int((gaps >= tol_deg).sum()) if (gaps >= tol_deg).any() else 1


# ---------------------------------------------------------------------------------------------
# Responses of every ROI to the oracle clips and the Monet2 directions.
#
# The dataset holds fluorescence traces only (RoiResponseSeries); the paper uses the deconvolved
# traces, which are not in it. Fluorescence is used in their place (a deviation).
#
# Monet2: the central 500 ms of each direction period, "(15/16 - 0.5)/2 s" in from each end
# (claims file, fig3g-direction-tuning, from the paper's code Fig 3/panel_g/get_data.ipynb).
# The response is the mean of the frames whose time stamps fall in that window.

CENTRAL_S = 0.5
# Shifts of the Monet2 windows used to check that the traces and the stimulus table share a
# clock (protocol, author step 2): one and two direction periods either way, and half of one.
CLOCK_LAGS_S = (-1.875, -0.9375, -0.46875, 0.0, 0.46875, 0.9375, 1.875)


def split_half_r(by_dir):
    """Per ROI, Pearson correlation over the 16 directions between the two halves of the trials."""
    a, b = by_dir[1], by_dir[2]
    a = a - np.nanmean(a, axis=0)
    b = b - np.nanmean(b, axis=0)
    return np.nansum(a * b, axis=0) / np.sqrt(np.nansum(a ** 2, axis=0) * np.nansum(b ** 2, axis=0))


def _runs(idx):
    idx = np.unique(idx)
    breaks = np.where(np.diff(idx) != 1)[0] + 1
    return np.split(idx, breaks)


def field_responses(args):
    """Oracle scores and Monet2 direction responses for every ROI of one field.

    args: (asset_id, field, frame_ts, oracle_onsets, n_oracle_frames, clip_bounds, monet_starts,
    monet_dirs, period_s).
    clip_bounds: for reading (b), the frame offsets of the 6 clips within a repeat.
    monet_dirs: (n_trials, 16) direction (degrees on the 22.5 degree grid) of each period.
    Returns a dict of per-ROI arrays.
    """
    (asset_id, field, ts, oracle_onsets, nfr, clip_bounds, monet_starts, monet_dirs, period_s) = args
    oracle_idx = oracle_frame_index(ts, np.asarray(oracle_onsets), nfr)

    def windows(lag):
        out = []
        for s, row in zip(monet_starts, monet_dirs):
            for j in range(len(row)):
                lo = s + lag + j * period_s + (period_s - CENTRAL_S) / 2
                out.append(np.where((ts >= lo) & (ts < lo + CENTRAL_S))[0])
        return out

    lag_windows = {lag: windows(lag) for lag in CLOCK_LAGS_S}
    win_idx = lag_windows[0.0]
    need = np.concatenate([oracle_idx.ravel()] + [w for ws in lag_windows.values() for w in ws if len(w)])
    f = open_asset(asset_id)
    d = f[f"processing/ophys/Fluorescence/RoiResponseSeries{field}/data"]
    blocks = {}
    for run in _runs(need):
        blocks[(run[0], run[-1])] = d[run[0]:run[-1] + 1, :]
    f.close()
    lookup = np.full(len(ts), -1)
    rows = []
    pos = 0
    for (a, b), arr in blocks.items():
        lookup[a:b + 1] = np.arange(pos, pos + b - a + 1)
        rows.append(arr)
        pos += b - a + 1
    data = np.concatenate(rows, axis=0)
    oracle = data[lookup[oracle_idx]]                          # (10, nfr, n_rois)
    score_a = oracle_score(oracle)
    per_clip = [oracle_score(oracle[:, a:b]) for a, b in clip_bounds]
    score_b = np.nanmean(np.array(per_clip), axis=0)
    # mean pairwise correlation between single repeats (variant of fig3f)
    z = oracle - oracle.mean(axis=1, keepdims=True)
    z /= np.sqrt((z ** 2).sum(axis=1, keepdims=True))
    pair = []
    for i in range(len(z)):
        for j in range(i + 1, len(z)):
            pair.append((z[i] * z[j]).sum(axis=0))
    pairwise = np.nanmean(np.array(pair), axis=0)
    # Monet2: mean response per direction, over all trials and over each half of the trials
    dir_bin = np.round(np.asarray(monet_dirs) / 22.5).astype(int) % 16
    n_tr = len(monet_starts)
    halves = [np.arange(n_tr), np.arange(n_tr // 2), np.arange(n_tr // 2, n_tr)]

    def by_direction(wins):
        resp = np.array([data[lookup[w]].mean(axis=0) if len(w) else np.full(data.shape[1], np.nan) for w in wins])
        resp = resp.reshape(n_tr, dir_bin.shape[1], -1)   # (trials, periods, rois)
        out = np.full((3, 16, data.shape[1]), np.nan)
        for h, trials in enumerate(halves):
            for k in range(16):
                t_idx, p_idx = np.where(dir_bin[trials] == k)
                if len(t_idx):
                    out[h, k] = resp[trials[t_idx], p_idx].mean(axis=0)
        return out

    by_dir = by_direction(win_idx)
    by_dir_late = by_direction(lag_windows[CLOCK_LAGS_S[4]])
    # clock check: split-half reliability of the direction tuning with the windows shifted in time
    lag_reliability = {lag: float(np.nanmedian(split_half_r(by_direction(w)))) for lag, w in lag_windows.items()}
    return {"score_a": score_a, "score_b": score_b, "pairwise": pairwise, "by_dir": by_dir,
            "by_dir_late": by_dir_late, "lag_reliability": lag_reliability,
            "n_rois": data.shape[1],
            "n_frames_read": data.shape[0], "frames_per_window": [len(w) for w in win_idx]}


def all_field_responses(jobs, workers=N_WORKERS):
    with mp.get_context("fork").Pool(workers) as pool:
        return pool.map(field_responses, jobs)


def oracle_setup(meta):
    """Oracle repeat onsets, the number of frames per repeat, and the frame bounds of each clip.

    A repeat is n frames from its onset, n being the shortest repeat at the scan's frame rate.
    """
    first, reps = oracle_repeats(meta["clip"])
    on = np.array([r.start_time.iloc[0] for r in reps])
    off = np.array([r.stop_time.iloc[-1] for r in reps])
    rate = meta["fields"].rate_hz.iloc[0]
    nfr = int(np.floor(np.min(off - on) * rate))
    r0 = reps[0]
    bounds = []
    for k in range(6):
        a = int(np.ceil((r0.start_time.iloc[k] - r0.start_time.iloc[0]) * rate))
        b = int(np.floor((r0.stop_time.iloc[k] - r0.start_time.iloc[0]) * rate))
        bounds.append((a, min(b, nfr)))
    return on, nfr, bounds


def monet2_jobs(asset_id, meta, n_jobs):
    """Split a scan's Monet2 trials (in time order) into n_jobs argument tuples."""
    mo = meta["monet2"].sort_values("start_time").reset_index(drop=True)
    return [(asset_id, meta["video"]["name"], mo.start_time.values[i::n_jobs], mo.stop_time.values[i::n_jobs],
             mo.num_directions.values[i::n_jobs], mo.duration.values[i::n_jobs]) for i in range(n_jobs)]


def gather_monet2(results, n_jobs):
    """Undo the split of monet2_jobs: one list of trial results in time order."""
    n = sum(len(r) for r in results)
    out = [None] * n
    for i, r in enumerate(results):
        for j, x in enumerate(r):
            out[i + n_jobs * j] = x
    return out


def field_jobs(asset_id, meta, trial_dirs):
    """Argument tuples of field_responses for every field of a scan.

    trial_dirs: (n_trials, 16) measured directions of the scan's Monet2 trials, in time order;
    they are snapped to the 22.5 degree grid, which the notebook shows they lie on.
    """
    on, nfr, bounds = oracle_setup(meta)
    mo = meta["monet2"].sort_values("start_time").reset_index(drop=True)
    grid = np.round(np.asarray(trial_dirs) / 22.5) * 22.5 % 360
    period = float(mo.duration.iloc[0]) / int(mo.num_directions.iloc[0])
    return [(asset_id, int(fl), meta["frame_ts"][int(fl)], on, nfr, bounds, mo.start_time.values, grid, period)
            for fl in meta["fields"].field]


def von_mises_peak(R, step_deg=1.0, kappas=(0.5, 1, 2, 4, 8, 16), batch=5000):
    """Peak direction of a von Mises function a + b exp(k (cos(theta - mu) - 1)), b > 0, fitted
    by least squares to each row of R (n_units, 16 directions on the 22.5 degree grid).

    The fit is a grid search over mu (step_deg) and k, with a and b solved in closed form; a
    standard choice for the fit the claims file names as reading (b). Returns mu in degrees.
    """
    theta = np.radians(np.arange(16) * 22.5)
    mus = np.radians(np.arange(0, 360, step_deg))
    T = np.array([np.exp(k * (np.cos(theta[None, :] - mus[:, None]) - 1)) for k in kappas]).reshape(-1, 16)
    mu_of = np.tile(np.degrees(mus), len(kappas))
    Tc = T - T.mean(axis=1, keepdims=True)
    Stt = (Tc ** 2).sum(axis=1)
    out = np.full(len(R), np.nan)
    for i in range(0, len(R), batch):
        r = R[i:i + batch]
        rc = r - r.mean(axis=1, keepdims=True)
        sty = rc @ Tc.T
        gain = np.where(sty > 0, sty ** 2 / Stt, -np.inf)
        best = np.argmax(gain, axis=1)
        ok = np.isfinite(gain[np.arange(len(r)), best]) & np.all(np.isfinite(r), axis=1)
        out[i:i + batch] = np.where(ok, mu_of[best], np.nan)
    return out


def oracle_trace(asset_id, field, roi_index, frame_ts, onsets, nfr):
    """Fluorescence of one ROI over the oracle repeats: array (n_repeats, nfr)."""
    idx = oracle_frame_index(frame_ts, np.asarray(onsets), nfr)
    f = open_asset(asset_id)
    d = f[f"processing/ophys/Fluorescence/RoiResponseSeries{field}/data"]
    out = np.array([d[row[0]:row[-1] + 1, roi_index] for row in idx])
    f.close()
    return out
