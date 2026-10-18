"""Loading and measures for the signal propagation recordings of dandiset 001075.

Randi, Sharma, Dvali & Leifer (2023), Nature 623, 406-414, doi:10.1038/s41586-023-06683-4.

Each subject has an `imaging` file (raw volumes, about 40 GB) and, for 110 of the 113
subjects, a `segmentation` file (a few MB) that holds, per tracked neuron (ROI), the green
(GCaMP6s) and red (tagRFP-T) intensity per volume, the ROI centroids in the reference
volume, the link from each ROI to a NeuroPAL ROI and its label, and the optogenetic
stimulation table with the target position of every stimulation. Only the segmentation
files and the small `depth_per_frame_in_um` and `timestamps` datasets of the imaging files
are read. Everything is streamed from the archive at the pinned version.

Where the parameters come from:

- The Methods (section "Calcium pre-processing"): missing values interpolated, photobleaching
  removed by fitting a double exponential, outliers more than 5 standard deviations from the
  mean removed, causal Savitzky-Golay smoothing (13 points, order 1); F0 is the mean of F in
  the 30 s before stimulation and <dF/F0>_t the mean over a 30 s post-stimulus window. A
  trace is excluded when imaging time points are absent in a contiguous segment longer than
  5% of the window.
- The paper's analysis code, https://github.com/leiferlab/pumpprobe at commit
  1dbc5e0a2b609d54bc9b1c90c73d4e3bf183d3c7, and https://github.com/leiferlab/wormdatamodel
  at commit 2ab956199e3931de41a190d2b9985e961df3810c, where the Methods leave a choice
  open:
  - the response classifier (`Fconn.from_objects`) with the parameters of
    `pipelines/fit_kernels_multi_datasets.sh`: amplitude threshold 1.3 times the third
    largest absolute pre-stimulus value, held contiguously for more than 4 s (or half the
    threshold for twice the time); derivative threshold 0.02 of the median pre-stimulus
    signal, for at least 4 s; NaN runs no longer than 30% of the window (`nan_thresh`
    default of `responses_detect.py`, which ignores the `--nan-th` flag); window from 30 s
    before to 60 s after the stimulation; derivative from an 11-point first-order
    Savitzky-Golay kernel applied by `np.convolve` (which gives minus the derivative, kept
    as in the code);
  - the photobleaching fit (`Signal.calc_photobl`): Y/max(Y) = a exp(-|b|x) + c exp(-|d|x)
    + |e| over the volume index x, refitted on the points within 2 standard deviations;
    the data are divided by the fit and multiplied by its first value;
  - spikes (outliers) are points above the mean by more than 5 standard deviations,
    replaced by the previous value (`Signal.remove_spikes`);
  - the "decaying" correction of `Funatlas.get_significance_features`, used here only as a
    variant: when the trace is falling at the stimulation, an exponential decay is
    subtracted in place of the constant F0;
  - 0.42 micrometres per pixel (`recording.frameUmPerPixel`);
  - the list of the 188 head neurons, the head ganglia of
    `pumpprobe/aconnectome_ids_ganglia.json`, fetched from GitHub at the commit above.
- Choices made here, because the dandiset lacks what the code uses:
  - which ROI was stimulated. The files give the manually located ROI for about half of
    the stimulations (`target_pumpprobe_id`) and, for all of them, the target's x and y in
    pixels and a z value in an unstated unit (`depth_in_um`, -0.875 to 0.875). The code finds
    the closest neuron in the volume at the stimulation and maps it to the reference volume
    through the tracking matches, which are not in the dandiset. Here the target is matched
    to the closest ROI centroid of the reference volume, with z mapped linearly to the
    plane index; the slope and offset are fitted per recording so that the mean distance
    to the nearest centroid is smallest (no outside data are used);
  - the stimulation volume is the volume whose timestamp is closest to the stimulation's
    start time;
  - distances use the median plane spacing of the imaging file's `depth_per_frame_in_um`;
  - the photobleaching fit runs by default on about 500 evenly spaced volumes with at most
    300 evaluations per round, for speed; `analyse_session(url, pb_points=None,
    pb_nfev=None)` runs it on every volume without a limit, as the code does, to check this.
  - F0 is used as it comes: the files hold some traces with negative values, and no check
    on the sign or size of F0 is made in <dF/F0>_t. F0 is returned with each value so that
    callers can exclude such rows.
"""

from __future__ import annotations

import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.optimize import least_squares
from scipy.signal import savgol_coeffs

DANDISET_ID = "001075"
DANDISET_VERSION = "0.240930.1859"

PUMPPROBE_COMMIT = "1dbc5e0a2b609d54bc9b1c90c73d4e3bf183d3c7"
GANGLIA_URL = ("https://raw.githubusercontent.com/leiferlab/pumpprobe/"
               f"{PUMPPROBE_COMMIT}/pumpprobe/aconnectome_ids_ganglia.json")

UM_PER_PIXEL = 0.42
DELTA_T_PRE = 30.0        # s, F0 window and pre-stimulus part of the response window
POST_T = 60.0             # s, response window after the stimulation (code)
DFF_WINDOW = 30.0         # s, <dF/F0>_t window (Methods)
SMOOTH_N, SMOOTH_POLY = 13, 1
OUTLIER_SD = 5.0
NAN_TH_OBS = 0.05         # Methods: contiguous gap longer than 5% of the window excludes a trace
AMPL_THRESH = 1.3
AMPL_MIN_TIME = 4.0
DERIV_THRESH = 0.02
DERIV_MIN_TIME = 4.0
NAN_TH_DETECT = 0.3
DERIV_KERNEL = np.arange(-5, 6) / 110.0   # savitzkygolay CC_011_001, as applied by np.convolve

_SEG = "processing/ophys"


# ----------------------------------------------------------------------------------------
# Archive access


def asset_list():
    """All assets of the pinned version: path, size and asset id."""
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return [{"path": a.path, "size": a.size, "asset": a} for a in ds.get_assets()]


def asset_url(asset):
    return asset.get_content_url(follow_redirects=1, strip_query=True)


def _open(url):
    return h5py.File(remfile.File(url), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def load_segmentation(url):
    """Everything the analysis uses from one segmentation file."""
    with _open(url) as f:
        subj = f["general/subject"]
        st = f["intervals/OptogeneticStimulusTable"]
        tps = f[f"{_SEG}/TargetedImageSegmentation/TargetPlaneSegmentation"]
        pp = f[f"{_SEG}/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation"]
        ppr = f[f"{_SEG}/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation"]
        npal = f[f"{_SEG}/NeuroPALSegmentations/NeuroPALPlaneSegmentation"]
        gb = f[f"{_SEG}/GreenSignals/BaseGreenSignal"]
        gi = f[f"{_SEG}/GreenSignals/InterpolatedGreenSignal"]
        rb = f[f"{_SEG}/RedSignals/BaseRedSignal"]
        pm = tps["pixel_mask"][:]
        out = {
            "subject_id": _s(subj["subject_id"][()]),
            "strain": _s(subj["strain"][()]),
            "genotype": _s(subj["genotype"][()]),
            "growth_stage": _s(subj["growth_stage"][()]),
            "age": _s(subj["age"][()]),
            "session_start": _s(f["session_start_time"][()]),
            "stim_start": st["start_time"][:],
            "stim_stop": st["stop_time"][:],
            "stim_power": st["power"][:],
            "stim_manual_roi": st["target_pumpprobe_id"][:],
            "target_x": pm["x"].astype(float),
            "target_y": pm["y"].astype(float),
            "target_z": tps["depth_in_um"][:],
            "centroids": pp["centroids"][:].astype(float),
            "centroids_red_equal": bool(np.array_equal(pp["centroids"][:], ppr["centroids"][:])),
            "neuropal_ids": np.array([_s(x) for x in pp["neuropal_ids"][:]]),
            "npal_ids": npal["id"][:],
            "npal_labels": np.array([_s(x) for x in npal["labels"][:]]),
            "npal_conf": npal["labels_confidences"][:],
            "t": gb["timestamps"][:],
            "green_base": gb["data"][:],
            "green_interp": gi["data"][:],
            "red_base": rb["data"][:],
            "green_unit": _s(gb["data"].attrs.get("unit", "")),
            "same_timestamps": bool(np.array_equal(gb["timestamps"][:], gi["timestamps"][:])
                                    and np.array_equal(gb["timestamps"][:], rb["timestamps"][:])),
        }
    labels = dict(zip(out["npal_ids"].tolist(), out["npal_labels"].tolist()))
    conf = dict(zip(out["npal_ids"].tolist(), out["npal_conf"].tolist()))
    # neuropal_ids holds the NeuroPAL ROI id as text; blank means unmatched, and a few
    # files hold other text (such as "merge"), which is treated as unmatched here.
    ids = out["neuropal_ids"]
    num = np.array([x.isdigit() for x in ids])
    out["neuropal_ids_other"] = sorted({x for x in ids if x != "" and not x.isdigit()})
    out["roi_label"] = np.array([labels.get(int(x), "").strip() if d else ""
                                 for x, d in zip(ids, num)])
    out["roi_conf"] = np.array([conf.get(int(x), np.nan) if d else np.nan
                                for x, d in zip(ids, num)])
    return out


def load_imaging_depth(url):
    """Frame depths and times of one imaging file (the raw volumes are not read)."""
    with _open(url) as f:
        g = f["acquisition/PumpProbeImagingGreen"]
        z = g["depth_per_frame_in_um"][:]
        t = g["timestamps"][:]
        shape = g["data"].shape
        red_indicator = _s(f["general/RedOpticalChannel"].attrs.get("indicator", ""))
    step = np.abs(np.diff(z))
    turns = np.sum(np.diff(np.sign(np.diff(z))) != 0)
    return {"n_frames": shape[0], "frame_shape": shape[1:], "depth_min": z.min(),
            "depth_max": z.max(), "plane_step_um": float(np.median(step[step > 0])),
            "frame_dt": float(np.median(np.diff(t))), "t0": t[0], "t1": t[-1],
            "n_sweeps": int(turns) + 1, "red_indicator": red_indicator}


def load_many(fn, assets, workers=8):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(fn, assets))


def head_neurons():
    """The 188 head neurons of the paper's code (head ganglia), fetched at a fixed commit."""
    with urllib.request.urlopen(GANGLIA_URL, timeout=60) as r:
        g = json.load(r)
    names = []
    for gang in g["head"]:
        for n in g[gang]:
            if n not in names:
                names.append(n)
    return names


def atlas_name(label):
    """The code's atlas name for a NeuroPAL label without merging (AWCOFF/AWCON as AWCL/AWCR)."""
    lab = label.strip()
    return {"AWCOFF": "AWCL", "AWCON": "AWCR"}.get(lab, lab)


# ----------------------------------------------------------------------------------------
# Stimulated neuron


def fit_target_z(sess, a_grid=np.linspace(-30, 30, 121), b_grid=np.arange(-10, 40, 0.5)):
    """Linear map from the target's z value to the plane index, fitted per recording by
    minimising the mean 3D distance from each target to its nearest ROI centroid."""
    c = sess["centroids"]
    valid = (sess["target_x"] > 0) | (sess["target_y"] > 0)   # (0, 0) marks a missing target
    if not valid.any():
        return (np.nan, 0.0, 0.0)
    dxy = ((c[None, :, 0] - sess["target_x"][valid, None]) ** 2
           + (c[None, :, 1] - sess["target_y"][valid, None]) ** 2)
    tz = sess["target_z"][valid, None]
    best = (np.inf, 0.0, 0.0)
    for a in a_grid:
        zz = a * tz
        for b in b_grid:
            d = np.sqrt(dxy + (c[None, :, 2] - (zz + b)) ** 2).min(1).mean()
            if d < best[0]:
                best = (d, a, b)
    return best


def identify_targets(sess):
    """Per stimulation: the stimulated ROI (manual where given, else nearest centroid with the
    fitted z map), how it was found, the distance in pixels, and the xy-only alternative."""
    _, a, b = fit_target_z(sess)
    c = sess["centroids"]
    tz = a * sess["target_z"] + b
    d3 = np.sqrt((c[None, :, 0] - sess["target_x"][:, None]) ** 2
                 + (c[None, :, 1] - sess["target_y"][:, None]) ** 2
                 + (c[None, :, 2] - tz[:, None]) ** 2)
    dxy = np.sqrt((c[None, :, 0] - sess["target_x"][:, None]) ** 2
                  + (c[None, :, 1] - sess["target_y"][:, None]) ** 2)
    roi = d3.argmin(1)
    how = np.array(["nearest"] * len(roi), dtype=object)
    missing = (sess["target_x"] == 0) & (sess["target_y"] == 0)
    roi[missing] = -1
    how[missing] = "no target"
    man = sess["stim_manual_roi"]
    has = np.isfinite(man)
    roi[has] = man[has].astype(int)
    how[has] = "manual"
    return {"roi": roi, "how": how, "dist_px": d3.min(1), "roi_xy": dxy.argmin(1),
            "z_slope": a, "z_offset": b}


def stim_volumes(t, start):
    return np.abs(t[None, :] - start[:, None]).argmin(1)


# ----------------------------------------------------------------------------------------
# Pre-processing


def _double_exp(p, x):
    return p[0] * np.exp(-x * abs(p[1])) + p[2] * np.exp(-x * abs(p[3])) + abs(p[4])


def _double_exp_jac(p, x):
    e1, e2 = np.exp(-x * abs(p[1])), np.exp(-x * abs(p[3]))
    return np.stack([e1, -p[0] * x * np.sign(p[1]) * e1, e2, -p[2] * x * np.sign(p[3]) * e2,
                     np.full_like(x, np.sign(p[4]))], 1)


def photobleach_fit(y, max_iter=10, n_points=500, max_nfev=300):
    """The code's double-exponential fit (`Signal.calc_photobl`), on at most about `n_points`
    evenly spaced volumes (all volumes when None) and with at most `max_nfev` evaluations per
    round (no limit when None). Returns the fit, or None when it fails; a trace with missing
    values ("missing") or whose maximum is not positive ("nonpositive") is not fitted, and the
    string is returned instead."""
    x = np.arange(len(y), dtype=float)
    ymax = np.max(y)
    if not np.isfinite(ymax):
        return "missing"
    if ymax <= 0:
        return "nonpositive"
    yn = y / ymax
    step = 1 if n_points is None else max(1, len(y) // n_points)
    xs, ys = x[::step], yn[::step]
    mask = np.ones(len(xs), bool)
    p = np.array([1.0, 0.006, 1.0, 0.001, 0.2])
    for _ in range(max_iter):
        if mask.sum() < 10:
            return None
        xm, ym = xs[mask], ys[mask]
        try:
            r = least_squares(lambda q: _double_exp(q, xm) - ym, p,
                              jac=lambda q: _double_exp_jac(q, xm), method="lm", max_nfev=max_nfev)
        except ValueError:
            return None   # as in the code, a failed fit leaves the trace uncorrected
        if np.sum(np.abs((p - r.x) / p)) < 1e-2:
            p = r.x
            break
        p = r.x
        with np.errstate(over="ignore", invalid="ignore"):
            res = _double_exp(p, xs) - ys
        if not np.all(np.isfinite(res)):
            return None
        mask = np.abs(res) < 2.0 * np.std(res[mask])
    with np.errstate(over="ignore", invalid="ignore"):
        fit = _double_exp(p, x) * ymax
    return fit if np.all(np.isfinite(fit)) else None


def preprocess(sess, pb_points=500, pb_nfev=300):
    """Interpolated green -> photobleaching corrected -> spikes removed -> causal SG smoothing.
    Returns the smoothed and unsmoothed traces, the derivative used by the classifier, the
    NaN mask of the original (base) trace, and per trace the outcome of the photobleaching
    fit: "ok", "missing" (values missing even after interpolation, as for an ROI never
    tracked), "nonpositive" (maximum not positive), "failed" (the fit did not
    converge to finite values) or "near zero" (the fit comes within 0.01 of zero, which the
    code also leaves uncorrected). Traces whose fit is not "ok" are left uncorrected."""
    g = sess["green_interp"].astype(float).copy()
    nan_mask = ~np.isfinite(sess["green_base"])
    status = np.array(["ok"] * g.shape[1], dtype=object)
    for k in range(g.shape[1]):
        fit = photobleach_fit(g[:, k], n_points=pb_points, max_nfev=pb_nfev)
        if isinstance(fit, str):
            status[k] = fit
            continue
        if fit is None:
            status[k] = "failed"
            continue
        if np.any(np.abs(fit) < 1e-2):
            status[k] = "near zero"
            continue
        g[:, k] = g[:, k] / fit * fit[0]
    n_fail = int(np.sum(status != "ok"))
    for k in range(g.shape[1]):
        y = g[:, k]
        if np.all(np.isfinite(y)):
            spikes = np.where(y - y.mean() > OUTLIER_SD * np.std(y))[0]
            for s in spikes:
                y[s] = y[s - 1]
    unsmoothed = g.copy()
    ker = savgol_coeffs(SMOOTH_N, SMOOTH_POLY, pos=SMOOTH_N - 1)
    shift = (SMOOTH_N - 1) // 2
    smoothed = g.copy()
    for k in range(g.shape[1]):
        smoothed[shift:, k] = np.convolve(g[:, k], ker, mode="same")[:-shift]
    deriv = np.zeros_like(unsmoothed)
    for k in range(g.shape[1]):
        deriv[:, k] = np.convolve(unsmoothed[:, k], DERIV_KERNEL, mode="same")
    return {"data": smoothed, "unsmoothed": unsmoothed, "deriv": deriv, "nan_mask": nan_mask,
            "photobleach_failed": n_fail, "photobleach_status": status}


# ----------------------------------------------------------------------------------------
# Response classifier and response amplitude


def _longest_run(cond):
    """Length of the longest run of True along axis 0, per column."""
    cond = np.asarray(cond, bool)
    if cond.ndim == 1:
        cond = cond[:, None]
    best = np.zeros(cond.shape[1], int)
    cur = np.zeros(cond.shape[1], int)
    for row in cond:
        cur = np.where(row, cur + 1, 0)
        best = np.maximum(best, cur)
    return best


def loc_std(y, window):
    """Square root of the median rolling variance (window points), per column."""
    if len(y) < window:
        return np.zeros(y.shape[1])
    w = np.lib.stride_tricks.sliding_window_view(y, window, axis=0)
    return np.sqrt(np.median(np.var(w, axis=-1), axis=0))


def detect_responses(sig, vols, dt, delta_t_pre=DELTA_T_PRE):
    """The code's classifier: for each stimulation, the ROIs whose response passes the
    amplitude, derivative and NaN criteria. Returns a list of index arrays and the windows."""
    data, raw, dr, nanm = sig["data"], sig["unsmoothed"], sig["deriv"], sig["nan_mask"]
    n_t, n_neu = data.shape
    set_shift = int(delta_t_pre / dt)
    ampl_min_vols = AMPL_MIN_TIME / dt
    deriv_min_vols = DERIV_MIN_TIME / dt
    n_30 = int(30 / dt)
    old_sel = np.zeros(n_neu, bool)
    int_btw = 10.0
    responders, windows = [], []
    for ie, ee in enumerate(vols):
        i0 = max(0, ee - set_shift)
        shift = set_shift if i0 > 0 else ee
        i1 = min(int(i0 + POST_T / dt + shift), n_t)
        if ie < len(vols) - 1:
            int_btw = (vols[ie + 1] - ee) * dt
        max_n = int((int_btw - 5) / dt)
        windows.append((i0, i1, shift))
        seg = data[i0:i1]
        base_rng = seg[shift // 2:shift]
        baseline = np.median(base_rng, axis=0) if len(base_rng) else 0.0
        seg = seg - baseline
        nan_ok = _longest_run(nanm[i0:i1]) <= NAN_TH_DETECT * (i1 - i0)
        prev_dr = np.mean(np.abs(dr[i0:i0 + max(shift - 6, 1)]), axis=0)
        post_dr = dr[i0 + shift:i0 + shift + max_n]
        pre_avg = np.median(data[i0:i0 + shift], axis=0) if shift > 0 else np.ones(n_neu)
        dsel = np.sum(np.abs(post_dr - prev_dr) / pre_avg > DERIV_THRESH, axis=0) >= deriv_min_vols
        if max_n * dt > 30:
            post_p = dr[i0 + shift:i0 + shift + n_30]
            dsel &= np.sum(np.abs(post_p - prev_dr) / pre_avg > DERIV_THRESH, axis=0) >= deriv_min_vols / 3
        r = seg[shift:shift + max_n]
        pre = seg[:shift]
        if len(pre) >= 3:
            absmax = np.sort(np.abs(pre), axis=0)[-3]
        else:
            absmax = np.zeros(n_neu)
        a1 = (_longest_run(r > AMPL_THRESH * absmax) > ampl_min_vols) | \
             (_longest_run(r > 0.5 * AMPL_THRESH * absmax) > 2 * ampl_min_vols)
        b1 = (_longest_run(r < -AMPL_THRESH * absmax) > ampl_min_vols) | \
             (_longest_run(r < -0.5 * AMPL_THRESH * absmax) > 2 * ampl_min_vols)
        if max_n * dt > 30:
            a1 &= np.sum(r[:n_30] > AMPL_THRESH * absmax, axis=0) > ampl_min_vols / 3
            b1 &= np.sum(r[:n_30] < -AMPL_THRESH * absmax, axis=0) > ampl_min_vols / 3
        asel1 = a1 | b1
        asel2 = np.zeros(n_neu, bool)
        if old_sel.any() and shift >= 25 and len(r) > 1:
            ls = loc_std(seg[6:shift - 6], 4)
            run2 = _longest_run(np.abs(r) > AMPL_THRESH * ls) > ampl_min_vols
            for k in np.where(old_sel & run2)[0]:
                s2a = seg[shift - 25:shift, k]
                len2b = min(25, len(seg) - shift)
                s2b = seg[shift:shift + len2b, k]
                d2a = np.polyfit(np.arange(25), s2a, 1)[0]
                d2b = np.polyfit(np.arange(len2b), s2b, 1)[0] if len2b > 1 else 0.0
                if d2a <= 5e-2 and d2b >= 5e-2:
                    asel2[k] = True
                else:
                    asel1[k] = False
        sel = dsel & (asel1 | asel2) & nan_ok
        old_sel = sel.copy()
        responders.append(np.where(sel)[0])
    return responders, windows


def dff_post(sig, windows, dt, decaying=False):
    """Per stimulation and ROI: <dF/F0>_t over the 30 s after the stimulation, with F0 the
    mean of the 30 s before (Methods); NaN where the trace fails the 5% NaN rule or its local
    standard deviation is 0. With decaying=True, the code's correction of decaying traces.
    Returns the values and F0 (same shape); F0 is not checked for sign or size."""
    data, nanm = sig["data"], sig["nan_mask"]
    n_w = int(DFF_WINDOW / dt)
    out = np.full((len(windows), data.shape[1]), np.nan)
    f0_out = np.full((len(windows), data.shape[1]), np.nan)
    for ie, (i0, i1, shift) in enumerate(windows):
        y = data[i0:i1]
        ok = _longest_run(nanm[i0:i1]) <= NAN_TH_OBS * (i1 - i0)
        ok &= loc_std(y, 8) != 0
        if shift < 2:
            continue
        f0 = y[:shift].mean(0)
        f0_out[ie] = f0
        post = y[shift:shift + n_w]
        val = (post - f0).mean(0) / f0
        if decaying:
            fder = savgol_coeffs(39, 1, pos=38, deriv=1, delta=dt)
            smk = savgol_coeffs(39, 1, deriv=0, delta=dt)
            for k in np.where(ok)[0]:
                yk = data[:, k]
                fd0 = np.convolve(fder, yk, mode="same")[i0 + shift]
                if fd0 < 0:
                    sm = np.convolve(smk, yk, mode="same")
                    if i0 + shift + 60 < len(sm):
                        zero, n_rem = sm[i0 + shift + 60], 60
                    else:
                        zero, n_rem = sm[-1], len(sm) - (i0 + shift)
                    tt = np.arange(n_rem) * dt
                    corr = (sm[i0 + shift] - zero) * np.exp(fd0 * tt) + zero
                    m = min(n_w, n_rem)
                    val[k] = np.mean(y[shift:shift + m, k] - corr[:m]) / f0[k]
        val[~ok] = np.nan
        out[ie] = val
    return out, f0_out


def roi_distance_um(sess, i, j, plane_step_um):
    c = sess["centroids"]
    d = (c[i] - c[j]) * np.array([UM_PER_PIXEL, UM_PER_PIXEL, plane_step_um])
    return np.sqrt(np.sum(d ** 2, axis=-1))


def session_key(path):
    m = re.match(r"sub-(\d+)/sub-\d+_ses-([\d-]+)_desc-(\w+)_", path)
    return int(m.group(1)), m.group(2), m.group(3)


# ----------------------------------------------------------------------------------------
# One recording, end to end


SHIFT_CHECK_S = 15.0   # stimulation times shifted by half the inter-stimulus interval


def analyse_session(url, pb_points=500, pb_nfev=300):
    """Load, pre-process and measure one recording. Returns only compact results."""
    sess = load_segmentation(url)
    tg = identify_targets(sess)
    sig = preprocess(sess, pb_points=pb_points, pb_nfev=pb_nfev)
    t = sess["t"]
    dt = float(np.median(np.diff(t)))
    vols = stim_volumes(t, sess["stim_start"])
    resp, win = detect_responses(sig, vols, dt)
    dff, f0 = dff_post(sig, win, dt)
    dff_dec, _ = dff_post(sig, win, dt, decaying=True)
    auto = np.array([tg["roi"][i] >= 0 and tg["roi"][i] in resp[i] for i in range(len(vols))])
    auto_xy = np.array([tg["roi_xy"][i] in resp[i] for i in range(len(vols))])
    shift = int(round(SHIFT_CHECK_S / dt))
    vols_s = np.clip(vols + shift, 0, len(t) - 1)
    resp_s, win_s = detect_responses(sig, vols_s, dt)
    dff_s, _ = dff_post(sig, win_s, dt)
    auto_s = np.array([tg["roi"][i] >= 0 and tg["roi"][i] in resp_s[i] for i in range(len(vols))])
    gb = sess["green_base"]
    keep = ["subject_id", "strain", "genotype", "growth_stage", "age", "session_start",
            "stim_start", "stim_stop", "stim_power", "stim_manual_roi", "target_x", "target_y",
            "target_z", "centroids", "centroids_red_equal", "roi_label", "roi_conf",
            "npal_labels", "npal_conf", "green_unit", "same_timestamps", "neuropal_ids",
            "neuropal_ids_other"]
    out = {k: sess[k] for k in keep}
    out.update({
        "url": url, "n_vol": len(t), "n_roi": gb.shape[1], "t0": t[0], "t1": t[-1], "dt": dt,
        "dt_max": float(np.max(np.diff(t))), "dt_min": float(np.min(np.diff(t))),
        "nan_frac": float(np.mean(~np.isfinite(gb))),
        "interp_matches_base": bool(np.allclose(sess["green_interp"][np.isfinite(gb)], gb[np.isfinite(gb)])),
        "green_range": (float(np.nanmin(gb)), float(np.nanmedian(gb)), float(np.nanmax(gb))),
        "red_range": (float(np.nanmin(sess["red_base"])), float(np.nanmedian(sess["red_base"])),
                      float(np.nanmax(sess["red_base"]))),
        "photobleach_failed": sig["photobleach_failed"],
        "photobleach_status": sig["photobleach_status"], "f0": f0,
        "stim_roi": tg["roi"], "stim_how": tg["how"], "stim_dist_px": tg["dist_px"],
        "stim_roi_xy": tg["roi_xy"], "z_slope": tg["z_slope"], "z_offset": tg["z_offset"],
        "stim_vol": vols, "windows": np.array(win), "responders": resp, "auto": auto,
        "auto_xy": auto_xy, "dff": dff, "dff_decay": dff_dec, "auto_shift": auto_s,
        "dff_shift": dff_s, "responders_shift": resp_s,
    })
    return out


def analyse_export(gcamp, t, stim_vols, labels, subject_id):
    """Pre-process and measure one recording of the paper's OSF export (`<k>_gcamp.txt`,
    `<k>_t.txt`, `<k>_stim_volume_i.txt`, `<k>_labels.txt`) as `analyse_session` does for a
    segmentation file. Missing values are interpolated linearly here (the dandiset provides its
    own interpolated copy), and the stimulation volumes are the exported ones. The result has
    the keys `observations` needs."""
    base = np.asarray(gcamp, float)
    interp = base.copy()
    x = np.arange(base.shape[0])
    for k in range(base.shape[1]):
        ok = np.isfinite(base[:, k])
        if 2 <= ok.sum() < len(ok):
            interp[:, k] = np.interp(x, x[ok], base[ok, k])
    sig = preprocess({"green_interp": interp, "green_base": base})
    dt = float(np.median(np.diff(t)))
    vols = np.asarray(stim_vols, int)
    resp, win = detect_responses(sig, vols, dt)
    dff, f0 = dff_post(sig, win, dt)
    dff_dec, _ = dff_post(sig, win, dt, decaying=True)
    return {"subject_id": subject_id, "n_roi": base.shape[1], "roi_label": np.asarray(labels),
            "dff": dff, "dff_decay": dff_dec, "f0": f0, "responders": resp,
            "photobleach_status": sig["photobleach_status"],
            "stim_how": np.array(["exported"] * len(vols), dtype=object)}


def analyse_all(urls, workers=4, **kwargs):
    """Run analyse_session over recordings in worker processes (kwargs go to analyse_session)."""
    import os
    from concurrent.futures import ProcessPoolExecutor
    from functools import partial
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    os.environ.setdefault("MKL_NUM_THREADS", "1")
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(partial(analyse_session, **kwargs), urls))


# ----------------------------------------------------------------------------------------
# Tables over recordings


def observations(results, head, stim_roi=None, labels=None):
    """One row per (stimulation, observed ROI) with a usable trace, for stimulations whose
    target ROI is known: the stimulated and observed neuron names, <dF/F0>_t (Methods and the
    code's decaying variant), whether the observed ROI passed the classifier, and whether the
    stimulated ROI did (autoresponse). `stim_roi` optionally replaces each recording's
    stimulated ROI array (used for the OSF variant). `f0` is the F0 of the observed trace and
    `pb_ok` says whether its photobleaching fit succeeded."""
    import pandas as pd
    head = set(head)
    parts = []
    for k, r in enumerate(results):
        roi = r["stim_roi"] if stim_roi is None else stim_roi[k]
        labs = r["roi_label"] if labels is None else labels[k]
        if roi is None or labs is None:
            continue
        names = np.array([atlas_name(x) for x in labs])
        in_head = np.array([x in head for x in names])
        for e in range(len(roi)):
            j = int(roi[e])
            if j < 0 or j >= r["n_roi"]:
                continue
            ii = np.where(np.isfinite(r["dff"][e]))[0]
            resp = set(r["responders"][e].tolist())
            parts.append(pd.DataFrame({
                "rec": k, "subject": r["subject_id"], "stim": e, "roi_j": j, "j": names[j],
                "j_head": in_head[j], "roi_i": ii, "i": names[ii], "i_head": in_head[ii],
                "dff": r["dff"][e, ii], "dff_decay": r["dff_decay"][e, ii], "f0": r["f0"][e, ii],
                "pb_ok": r["photobleach_status"][ii] == "ok",
                "responded": [x in resp for x in ii], "auto": j in resp,
                "how": r["stim_how"][e]}))
    return pd.concat(parts, ignore_index=True)


def pair_table(obs, value="dff"):
    """Per (i, j) head pair: number of observations and mean value."""
    h = obs[obs.i_head & obs.j_head & (obs.i != "") & (obs.j != "")]
    g = h.groupby(["i", "j"])[value]
    return g.agg(["size", "mean"]).rename(columns={"size": "n", "mean": "mean"}).reset_index()
