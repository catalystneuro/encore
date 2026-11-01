"""Loading and measures for dandiset 001074 (Kalugin et al. 2026, MORSE).

The dandiset holds, for each MORSE recording, the CaImAn output of the paper's
pipeline: a trace per cell mask (RoiResponseSeries, the denoised trace C, and
`residuals`, the residual YrA) and the dense 3D masks. It holds no sensor
labels, no stimulus or well timing, and placeholder timing metadata (every
file says 30 Hz and starts at 0). What this module adds, and where each part
comes from:

- Well timing. Every well lasts 93 frames, 3 min at 31 frames per minute.
  Source: the paper's code, morse_figs3_rev cells 1, 8 (`mean_factor` 31,
  well onsets every `3*mean_factor` frames) and Methods "3-5 min/well". The
  frame counts of the files are multiples of 93 (checked in the notebook).
- Well order of the revision probes (the ten ten-sensor probes of Figure 1G-J
  and Table 1) and the mixture concentrations: morse_figs3_rev cells 0-2
  (well lists), 338 and 345 (`c_offset_rev`, concentrations 10**(k - offset) M
  for the k-th of the seven wells of a mixture). Outside input, pinned at
  commit fa4526ac02eaa2c5a24c4cfdcaab5c36ed5ae4ed.
- dF/F0 with F0 the mean of the lowest 10% of the trace: Methods Eq. 27.
- Peak normalization by Eq. 28 (lowest and highest 10%): Methods.
- Jump artefact at each well onset, an exponential decay scaled by the jump,
  decay constant about 30 s: Methods, "Quantification and statistical
  analysis", paragraph 2. The jump is measured as in morse_figs3_rev cell 23
  (the value 2 frames after onset minus the mean of the 5 frames before it).
  The decay constant is the Methods' 30 s (15.5 frames); the code fits it.
- Exponential background before activation (identification dipping): Methods,
  same paragraph. Fitted only when at least two wells precede the cell's
  activation (an assumption: the Methods say "tens of minutes").
- First derivative by a Savitzky-Golay filter, 1 min window (31 frames),
  order 1: Methods. The code uses 30 frames (cell 10, 25).
- HDBSCAN, min_cluster_size 3, on correlation distance of the derivatives:
  Methods and morse_figs3_rev cell 30; clusters matched to ligands by the
  correlation of the cluster mean derivative with the time course of ligand
  administration (Methods). The administration time course is taken as a
  boxcar over the first minute of each well, an assumption (the Methods do
  not give it).
- Eq. 8 and Eq. 9 (y = F/(1 + Kd/[L])), Powell least squares: Methods and
  morse_figs3_rev cell 365.
"""
import functools
import json
import urllib.request

import h5py
import numpy as np
import remfile
from scipy import optimize, signal

DANDISET = "001074"
VERSION = "0.260928.0807"
API = "https://api.dandiarchive.org/api"

FRAMES_PER_WELL = 93  # morse_figs3_rev cell 8: 3 * mean_factor (31)
FRAMES_PER_MIN = 31.0
TAU_JUMP_FRAMES = 30.0 / 60.0 * FRAMES_PER_MIN  # Methods, ~30 s
SG_WINDOW = 31  # Methods, 1 min
UM_PER_PLANE = 9.89  # morse_figs3_rev cells 712-718 (claims file); Methods "~9 um"

# The ten revision probes (morse_figs3_rev cell 0), in the code's order.
REV_PROBES = ["251003-PL65", "251115-ZS17", "251117-ZS6", "251117-ZS8", "251117-ZS22",
              "251119-PL62", "251119-ZS9", "251119-ZS16", "251122-ZS6", "251122-ZS8"]
ID_WELLS = ["AVP", "5HT", "NE", "ACh", "ATP", "OXT", "HA", "DA", "CCK", "MT", "P"]  # cell 1
SENSORS = ["AVP", "OXT", "5HT", "CCK", "NE", "DA", "ACh", "ATP", "MT", "HA"]
# Dose recording: A5NAA-7..-1 (frames 0-651), OHDCM-7..-1 (651-1302), P (cell 2).
MIX_A = ["AVP", "5HT", "NE", "ACh", "ATP"]
MIX_O = ["OXT", "HA", "DA", "CCK", "MT"]
# log10 offsets of the seven wells of a mixture, per (sensor, ligand): cell 338, 345.
C_OFFSET = {("AVP", "AVP"): 11, ("AVP", "OXT"): 10, ("OXT", "AVP"): 11, ("OXT", "OXT"): 10,
            ("5HT", "5HT"): 10, ("CCK", "CCK"): 11, ("NE", "NE"): 9, ("NE", "DA"): 10,
            ("DA", "NE"): 9, ("DA", "DA"): 10, ("ACh", "ACh"): 9, ("ATP", "ATP"): 9,
            ("MT", "MT"): 11, ("HA", "HA"): 9}
# Baseline well (1-based) and peak-normalization well (0-based) of each group: cell 338.
GR_WBASE = {("AVP", "AVP"): 1, ("AVP", "OXT"): 4, ("OXT", "AVP"): 1, ("OXT", "OXT"): 3,
            ("5HT", "5HT"): 1, ("CCK", "CCK"): 3, ("NE", "NE"): 1, ("NE", "DA"): 4,
            ("DA", "NE"): 1, ("DA", "DA"): 3, ("ACh", "ACh"): 2, ("ATP", "ATP"): 3,
            ("MT", "MT"): 2, ("HA", "HA"): 2}
GR_WPEAK = {("AVP", "AVP"): 6, ("AVP", "OXT"): 6, ("OXT", "AVP"): 6, ("OXT", "OXT"): 6,
            ("5HT", "5HT"): 6, ("CCK", "CCK"): 6, ("NE", "NE"): 5, ("NE", "DA"): 6,
            ("DA", "NE"): 5, ("DA", "DA"): 6, ("ACh", "ACh"): 5, ("ATP", "ATP"): 6,
            ("MT", "MT"): 5, ("HA", "HA"): 6}
# Groups whose last well is dropped from the fit (cell 365, `trimlast`).
TRIMLAST = {("NE", "NE"), ("DA", "NE"), ("ACh", "ACh"), ("MT", "MT")}
GROUP_ORDER = [("AVP", "AVP"), ("AVP", "OXT"), ("OXT", "AVP"), ("OXT", "OXT"), ("5HT", "5HT"),
               ("CCK", "CCK"), ("NE", "NE"), ("NE", "DA"), ("DA", "NE"), ("DA", "DA"),
               ("ACh", "ACh"), ("ATP", "ATP"), ("MT", "MT"), ("HA", "HA")]


@functools.lru_cache(maxsize=1)
def assets():
    """Path -> asset record for the pinned version."""
    out, url = {}, f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    while url:
        with urllib.request.urlopen(url) as r:
            d = json.load(r)
        for a in d["results"]:
            out[a["path"]] = a
        url = d.get("next")
    return out


def s3_url(path):
    aid = assets()[path]["asset_id"]
    req = urllib.request.Request(f"{API}/assets/{aid}/download/", headers={"Range": "bytes=0-0"})
    with urllib.request.urlopen(req) as r:
        return r.url


def open_nwb(path):
    return h5py.File(remfile.File(s3_url(path)), "r")


def file_path(probe, rec, kind="mr-raw-refit-matched"):
    sub = f"sub-{probe}-{rec}"
    return f"{sub}/{sub}_ses-ch0-means-movie-nobg-cnmf-{kind}_ophys.nwb"


def load_traces(path):
    """CY = C + YrA (the code's `CY_matched_raw`), cells x frames."""
    with open_nwb(path) as f:
        c = f["processing/ophys/Fluorescence/RoiResponseSeries/data"][:]
        r = f["processing/ophys/residuals/data"][:]
    return (c + r).T


def mask_z_profiles(path, workers=16):
    """Per-plane weight of every mask, cells x planes.

    The image_mask arrays are stored scrambled: each is the Fortran-order
    flattening of the (x, y, z) volume written into a C-order array of the same
    shape (the notebook shows this). Read in the file's own order, every mask
    spans the whole volume; reordered as `m.ravel().reshape(shape, order="F")`
    each is a compact blob. Since z varies slowest in Fortran order, plane z is
    the z-th contiguous block of x*y values. The dataset is contiguous and
    uncompressed, so each mask is read as one byte range of the streamed file.
    """
    from concurrent.futures import ThreadPoolExecutor
    url = s3_url(path)
    with h5py.File(remfile.File(url), "r") as f:
        ds = f["processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask"]
        assert ds.chunks is None and ds.compression is None
        off, shape, dt = ds.id.get_offset(), ds.shape, ds.dtype
    n = int(np.prod(shape[1:])) * dt.itemsize

    def one(i):
        req = urllib.request.Request(url, headers={"Range": f"bytes={off + i * n}-{off + (i + 1) * n - 1}"})
        with urllib.request.urlopen(req) as r:
            v = np.frombuffer(r.read(), dtype=dt)
        return v.reshape(shape[3], -1).sum(axis=1)

    with ThreadPoolExecutor(workers) as ex:
        w = list(ex.map(one, range(shape[0])))
    return np.array(w)


def z_centre(w):
    z = np.arange(w.shape[1])
    return (w * z).sum(axis=1) / w.sum(axis=1)


def dff(x):
    """Eq. 27, F0 the mean of the lowest 10% of each trace."""
    s = np.sort(x, axis=1)
    n = int(np.ceil(x.shape[1] / 10))
    f0 = s[:, :n].mean(axis=1, keepdims=True)
    return (x - f0) / f0


def peak_norm(x):
    """Eq. 28."""
    s = np.sort(x, axis=1)
    n = int(np.ceil(x.shape[1] / 10))
    lo = s[:, :n].mean(axis=1, keepdims=True)
    hi = s[:, -n:].mean(axis=1, keepdims=True)
    return (x - lo) / (hi - lo)


def remove_jumps(x, tau=TAU_JUMP_FRAMES, fpw=FRAMES_PER_WELL):
    """Subtract, from each well onset on, an exponential decay scaled by the jump."""
    y = x.copy()
    t = x.shape[1]
    for on in range(fpw, t, fpw):
        if on + 2 >= t:
            break
        jump = x[:, on + 2] - x[:, on - 7:on - 2].mean(axis=1)
        end = min(t, on + fpw)
        y[:, on:end] -= jump[:, None] * np.exp(-np.arange(end - on) / tau)[None, :]
    return y


def derivative(x, window=SG_WINDOW):
    return signal.savgol_filter(x, window, 1, deriv=1, axis=1)


def exp_background(x, act, min_frames=2 * FRAMES_PER_WELL):
    """Subtract a decaying exponential c1*exp(-t/k), c1 >= 0, fitted with an offset c0
    to each trace before its activation frame (Methods). k is bounded by the length of
    the fitted segment so that the fit cannot turn into a line that is then
    extrapolated; the bounds are an assumption the Methods do not fix."""
    y = x.copy()
    fitted = np.zeros(len(x), bool)
    t = np.arange(x.shape[1], dtype=float)
    for i in range(len(x)):
        a = int(act[i]) - 5
        if a < min_frames:
            continue
        seg = x[i, :a]
        try:
            p, _ = optimize.curve_fit(lambda tt, c0, c1, k: c0 + c1 * np.exp(-tt / k), t[:a], seg,
                                      p0=(seg[-10:].mean(), max(seg[:10].mean() - seg[-10:].mean(), 0.0), a / 4.0),
                                      maxfev=4000, bounds=([-np.inf, 0.0, 5.0], [np.inf, np.inf, float(a)]))
            y[i] -= p[1] * np.exp(-t / p[2])
            fitted[i] = True
        except Exception:
            pass
    return y, fitted


def onset_boxcar(n_frames, wells, ligand, width=int(FRAMES_PER_MIN), fpw=FRAMES_PER_WELL):
    b = np.zeros(n_frames)
    for w, name in enumerate(wells):
        if name == ligand:
            b[w * fpw:min(n_frames, w * fpw + width)] = 1
    return b


def fit_ec50(conc, y):
    """Least-squares fit of Eq. 9 with Hill coefficient 1 to pooled points (Powell)."""
    conc = np.asarray(conc, float)
    y = np.asarray(y, float)
    ok = np.isfinite(y)
    conc, y = conc[ok], y[ok]

    def loss(p):
        k, f = 10 ** p[0], p[1]
        return np.sum((y - f / (1 + k / conc)) ** 2)

    best = None
    for k0 in np.arange(-10, -2, 1.0):
        r = optimize.minimize(loss, [k0, 1.0], method="Powell",
                              bounds=[(-12, 0), (0.01, 10)])
        if best is None or r.fun < best.fun:
            best = r
    return 10 ** best.x[0], best.x[1]


def conc_eq8(y, kd, f):
    y = np.clip(y, 0, f * (1 - 1e-6))
    return kd * y / (f - y)


def load_rev():
    """Identification (wells001) and dose (wells101) traces of the ten revision probes.

    The matched files of a probe hold the same cells in the same row order
    (morse_figs3_rev cell 5). For 251119-ZS16 the identification file has one
    row more (143 against 142); the code deletes row 53 (cell 6), as here.
    """
    out = {}
    for p in REV_PROBES:
        idt = load_traces(file_path(p, "wells001"))
        dose = load_traces(file_path(p, "wells101"))
        if p == "251119-ZS16":
            idt = np.delete(idt, 53, axis=0)
        out[p] = {"id": idt, "dose": dose}
    return out


def id_preprocess(cy, background=True):
    """Identification traces: dF/F0, jump removal, optional exponential background, Eq. 28."""
    x = remove_jumps(dff(cy))
    fitted = np.zeros(len(x), bool)
    if background:
        act = derivative(peak_norm(x)).argmax(axis=1)
        x, fitted = exp_background(x, act)
    return x, peak_norm(x), fitted


def _hdbscan(der):
    from scipy.spatial.distance import pdist, squareform
    from sklearn.cluster import HDBSCAN
    d = squareform(pdist(der, "correlation"))
    return HDBSCAN(min_cluster_size=3, metric="precomputed", copy=True).fit(d).labels_


def label_clusters(der, lab, wells=ID_WELLS):
    """Match each cluster to the ligand whose administration time course its mean
    derivative correlates with best; keep the match only when the mean derivative
    also peaks in that ligand's well (else the cluster stays unlabelled)."""
    t = der.shape[1]
    ligs = [w for w in wells if w != "P"]
    box = np.array([onset_boxcar(t, wells, l) for l in ligs])
    out = np.array([""] * len(lab), dtype=object)
    for c in range(lab.max() + 1):
        m = der[lab == c].mean(axis=0)
        r = [np.corrcoef(m, b)[0, 1] for b in box]
        lig = ligs[int(np.argmax(r))]
        if wells[int(np.argmax(m)) // FRAMES_PER_WELL] == lig:
            out[lab == c] = lig
    return out


def identify(pn_list, window=SG_WINDOW):
    """Sensor labels. Reading (a): one HDBSCAN over the cells of all probes pooled.
    Reading (b): (a), then cells left unlabelled take the label of their cluster in
    an HDBSCAN of their own probe (the code's second pass, morse_figs3_rev cells
    62-69, without its hand corrections, cells 73-78)."""
    der = np.vstack([derivative(x, window) for x in pn_list])
    grp = np.concatenate([[i] * len(x) for i, x in enumerate(pn_list)])
    la = label_clusters(der, _hdbscan(der))
    lb = la.copy()
    for g in range(len(pn_list)):
        s = np.where(grp == g)[0]
        lg = label_clusters(der[s], _hdbscan(der[s]))
        for i, l in zip(s, lg):
            if lb[i] == "" and l != "":
                lb[i] = l
    return la, lb, grp, der


def yield_stats(lab, grp, n_probes=10):
    keep = lab != ""
    per = [len(set(lab[(grp == g) & keep])) for g in range(n_probes)]
    return {"cells": int(keep.sum()), "sensors_per_probe": per, "median": float(np.median(per)),
            "p25": float(np.percentile(per, 25)), "p75": float(np.percentile(per, 75)),
            "cells_per_sensor_per_probe": keep.sum() / sum(per)}


def well_plateaus(x, how="mean_third_minute", fpw=FRAMES_PER_WELL):
    """Plateau of each well. Methods: mean over the third minute (frames 62-92).
    Code (morse_figs3_rev cell 339): median of the sorted frames 47-77."""
    nw = x.shape[1] // fpw
    out = np.zeros((len(x), nw))
    for w in range(nw):
        seg = x[:, w * fpw:(w + 1) * fpw]
        if how == "mean_third_minute":
            out[:, w] = seg[:, 62:93].mean(axis=1)
        else:
            out[:, w] = np.median(np.sort(seg, axis=1)[:, 47:78], axis=1)
    return out


def block_of(ligand):
    """First well of the mixture block holding a ligand in the dose recording."""
    return 0 if ligand in MIX_A else 7


def group_points(plateaus, group, how="code"):
    """Concentrations and normalized plateaus of one (sensor, ligand) group, cells x wells.

    how="code": baseline-well plateau subtracted and divided by the peak-well plateau,
    wells from the baseline well on, last well dropped for some groups (morse_figs3_rev
    cells 338-339, 365). how="eq28": the plateaus of the Eq. 28-normalized trace, all
    seven wells.
    """
    s, l = group
    b = block_of(l)
    conc = 10.0 ** (np.arange(7) - C_OFFSET[group])
    y = plateaus[:, b:b + 7]
    if how == "eq28":
        return conc, y
    wb, wp = GR_WBASE[group], GR_WPEAK[group]
    yc = (y - y[:, [wb - 1]]) / (y[:, [wp]] - y[:, [wb - 1]])
    conc, yc = conc[wb - 1:], yc[:, wb - 1:]
    if group in TRIMLAST:
        conc, yc = conc[:-1], yc[:, :-1]
    return conc, yc


def fit_group(conc, y):
    ok = np.all(np.isfinite(y), axis=1)
    y = y[ok]
    if len(y) == 0:
        return np.nan, np.nan, 0
    kd, f = fit_ec50(np.tile(conc, len(y)), y.ravel())
    return kd, f, len(y)


def normalized_dose_trace(x, group, fpw=FRAMES_PER_WELL):
    """The code's per-cell dose trace of a group (cell 339): the 651-frame block of the
    ligand's mixture, minus the baseline-well plateau, over the peak-well plateau
    (plateaus by the Methods' mean of the third minute)."""
    s, l = group
    b = block_of(l) * fpw
    blk = x[:, b:b + 7 * fpw]
    pl = well_plateaus(blk)
    wb, wp = GR_WBASE[group], GR_WPEAK[group]
    return (blk - pl[:, [wb - 1]]) / (pl[:, [wp]] - pl[:, [wb - 1]])


def tau_on(trace, start, fpw=FRAMES_PER_WELL):
    """Exponential rise (x0 - xinf) exp(-t/tau) + xinf over frames 0-78 of a well, x0 the
    first frame and xinf the median of frames 47-78, tau free (morse_figs3_rev cells
    688-689). Returns tau in frames, NaN if the fit fails or tau > 200 frames."""
    seg = trace[start:start + 79]
    x0, xi = seg[0], np.median(seg[47:79])
    t = np.arange(len(seg), dtype=float)
    if not np.all(np.isfinite(seg)) or x0 == xi:
        return np.nan
    # least squares in tau: a grid, then a bounded scalar search around its best point
    sse = lambda b: np.sum(((x0 - xi) * np.exp(-t / b) + xi - seg) ** 2)
    grid = np.logspace(-1, 4, 200)
    k = int(np.argmin([sse(b) for b in grid]))
    lo, hi = grid[max(k - 1, 0)], grid[min(k + 1, len(grid) - 1)]
    tau = optimize.minimize_scalar(sse, bounds=(lo, hi), method="bounded").x
    return tau if tau <= 200 else np.nan


# CONSTANTS of the claims file: Kd = Table 1 MORSE EC50 (M), F from morse_figs3_rev cell 376.
KD_TABLE1 = {("AVP", "AVP"): 355e-9, ("AVP", "OXT"): 28.7e-6, ("OXT", "AVP"): 247e-9,
             ("OXT", "OXT"): 2.19e-6, ("5HT", "5HT"): 687e-9, ("CCK", "CCK"): 245e-9,
             ("NE", "NE"): 4.04e-6, ("NE", "DA"): 9.35e-6, ("DA", "NE"): 8.20e-6,
             ("DA", "DA"): 1.70e-6, ("ACh", "ACh"): 7.03e-6, ("ATP", "ATP"): 75.2e-6,
             ("MT", "MT"): 22.0e-9, ("HA", "HA"): 6.39e-6}
F_CODE = {("AVP", "AVP"): 1.0593, ("AVP", "OXT"): 1.2894, ("OXT", "AVP"): 1.0089,
          ("OXT", "OXT"): 1.0596, ("5HT", "5HT"): 1.0484, ("CCK", "CCK"): 1.0671,
          ("NE", "NE"): 1.0440, ("NE", "DA"): 1.0907, ("DA", "NE"): 1.0816, ("DA", "DA"): 1.0007,
          ("ACh", "ACh"): 1.0643, ("ATP", "ATP"): 1.0633, ("MT", "MT"): 1.0648, ("HA", "HA"): 1.0050}


def tau_well(group, kd):
    """Index (0-6) of the lowest concentration of the mixture above kd (morse_figs3_rev
    cells 692, 699: `s1_ec50_d`)."""
    conc = 10.0 ** (np.arange(7) - C_OFFSET[group])
    above = np.where(conc > kd)[0]
    return int(above[0]) if len(above) else None


def taus_for_group(x_block, group, kd, f):
    """tau-on (frames) per cell, on the normalized dF/F0 and on the Eq. 8 concentration,
    both after a 31-frame median filter (claims file, morse_figs3_rev cells 688-692)."""
    from scipy.ndimage import median_filter
    w = tau_well(group, kd)
    if w is None:
        return np.array([]), np.array([]), None
    sm = median_filter(x_block, size=(1, 31), mode="nearest")
    st = w * FRAMES_PER_WELL
    t_d = np.array([tau_on(sm[i], st) for i in range(len(sm))])
    conc = conc_eq8(sm, kd, f)
    t_c = np.array([tau_on(conc[i], st) for i in range(len(conc))])
    return t_d, t_c, w


def file_summary(path):
    """Shapes and metadata of one file, without its arrays (one value for duplicate checks)."""
    with open_nwb(path) as f:
        rr = f["processing/ophys/Fluorescence/RoiResponseSeries"]
        ts = rr["timestamps"]
        ps = f["processing/ophys/ImageSegmentation/PlaneSegmentation"]
        n_t, n_roi = rr["data"].shape
        return {
            "path": path, "subject": path.split("/")[0][4:],
            "session": f["general/session_id"][()].decode() if "session_id" in f["general"] else "",
            "frames": n_t, "cells": n_roi,
            "t0": float(ts[0]), "dt": float(ts[1] - ts[0]), "rate_hz": float(f["general/optophysiology/ImagingPlane/imaging_rate"][()]),
            "indicator": f["general/optophysiology/ImagingPlane/indicator"][()].decode(),
            "start": f["session_start_time"][()].decode(),
            "mask_shape": tuple(ps["image_mask"].shape[1:]),
            "accepted": int(ps["accepted"][:].sum()), "rejected": int(ps["rejected"][:].sum()),
            "acquisition": len(f["acquisition"]), "stimulus": len(f["stimulus/presentation"]),
            "first_values": tuple(np.round(rr["data"][0, :min(3, n_roi)], 3)),
        }


def survey(workers=32):
    from concurrent.futures import ThreadPoolExecutor
    paths = sorted(assets())
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(file_summary, paths))


def kind_of(path):
    """The pipeline stage in a file name: mr-raw (curated masks), mr-m-raw, and their
    -refit and -matched<k> forms (README of the paper's code, folder 5)."""
    import re
    m = re.search(r"_ses-ch0-means-movie-nobg-cnmf-(.*)_ophys", path)
    return m.group(1) if m else "unnamed"


def noise_keep(xn):
    """The code's noise cut (morse_figs3_rev cells 343, 365): the SD of each normalized
    trace minus its Savitzky-Golay smoothing (31 frames, order 1); cells are kept when it
    is below 1.25 x median - 0.25 x minimum of the group."""
    sd = np.std(xn - signal.savgol_filter(xn, 31, 1, axis=1), axis=1)
    ok = np.isfinite(sd)
    cut = 1.25 * np.median(sd[ok]) - 0.25 * np.min(sd[ok])
    return ok & (sd < cut)
