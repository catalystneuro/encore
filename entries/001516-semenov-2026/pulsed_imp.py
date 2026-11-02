"""Loading and pole measures for dandiset 001516 (Semenov et al. 2026, Bioelectrochemistry 171, 109283).

The dandiset holds 72 NWB files, one per imaging set: 12 fields of view ("subjects" CHO_20230622_c1
to c12), six sets each, each set an ImageSeries of 60 frames of 512 x 512 pixels at 6 Hz. The
protocol of each set (sham, single pulse, or a pulse pair with its amplitudes and interval) is only
in the free-text `session_description`, which `parse_protocol` reads.

Where each parameter comes from:

- Collapsed images, 6-pixel-wide perimeter trace, 360 points, dF = 100 (F - F0) / F0, +-5 degree pole
  arcs: Methods 2.3 of the paper ("40 baseline images and 60 images taken during the electric pulse
  were collapsed, respectively, into one 'baseline image' and one 'polarization image' ... pixel
  intensity was measured along the 6-pixel-wide trace drawn along the cell perimeter ... resampled to
  360 datapoints ... mean dF values in +-5 degree arcs at the cathodic and anodic poles"), and the
  common method of the claims file. The files hold 20 baseline and 40 pulse frames (the dandiset's
  description), so the collapsed images are the means of those (claims file header).
- Per-frame pole dF with F0 the mean of the baseline frames: Methods 2.3, the Fig. 2 measure.
- F0 leaves out frame 0 (`BASE_FIRST = 1`): in these files the first frame of every set is about
  a third dimmer than the rest (notebook, data check), an artefact the paper does not report, so
  F0 is the mean of baseline frames 1 to 19. A deviation from Methods 2.3, which uses every
  baseline image; the notebook shows the effect of including frame 0.
- The trace is placed, for each degree of angle about the cell centre, on the brightest radius of the
  set's mean image, and averaged over 6 pixels across it. The paper drew it by hand in MetaMorph;
  this placement is a standard choice that follows the membrane ring.
- Cells are found by an Otsu threshold of the smoothed mean image, with holes filled. Touching
  cells are split: each local maximum of the distance transform above 0.6 of the object's maximum
  is a cell centre, and each pixel of the object goes to its nearest centre. Kept are pieces of 700
  to 12000 pixels that do not touch the image border and are round (elongation, the ratio of the
  axes of the second moments, at most 1.3, and solidity at least 0.9). The paper measured
  spheroidal cells assumed spherical (Methods 2.1 and 2.3); the thresholds are standard choices,
  and `find_cells` reports the objects it drops. The files do not say which of
  the cells in the field was the experiment's cell (the paper used one cell per experiment), so every
  whole cell is measured (an assumption, stated in the notebook).
- Field direction: not recorded in the files. It is taken from the data as the phase of the first
  angular harmonic of dF, pooled over the pulse sets of each field of view; each set's poles are
  placed with the direction from the other pulse sets of its field of view (`cathode_angles_loo`),
  so that a set's own noise does not choose the poles it is measured at (an assumption: the
  cathode-facing pole is the one that brightens, Methods 2.3, "The emission of both potentiometric
  dyes increased when cell membrane depolarized (in the cathode-facing cell hemisphere)").
- Smoothing widths for finding cells and the ring (Gaussian sigma 3 and 1 pixel) are standard
  choices for locating objects; the measured values use unsmoothed frames.
"""

import hashlib
import json
import re
import urllib.request
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
from scipy import ndimage
from scipy.spatial import ConvexHull

DANDISET_ID = "001516"
DANDISET_VERSION = "0.261006.1833"
API = "https://api.dandiarchive.org/api"

N_BASE = 20  # sham frames at the start of each set (dandiset description: 20 sham, 40 pulse)
BASE_FIRST = 1  # first baseline frame in F0; frame 0 is dimmed in every set (see the docstring)
N_ANG = 360  # points along the perimeter (Methods 2.3)
TRACE_WIDTH = 6  # pixels (Methods 2.3)
POLE_HALF = 5  # degrees (Methods 2.3)

# The description lists the field strengths 0.15, 0.52, 0.9, 1.27 and 1.57 kV/cm, and the sets
# name amplitudes of 50 to 250 V. The mapping in order is read from the description; the notebook
# checks it against the responses.
FIELD_LIST_KVCM = [0.15, 0.52, 0.9, 1.27, 1.57]
VOLTS = [50, 100, 150, 200, 250]


def list_assets():
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += page["results"]
        url = page.get("next")
    return out


def version_metadata():
    with urllib.request.urlopen(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/") as r:
        return json.load(r)


def asset_url(asset_id):
    return f"{API}/assets/{asset_id}/download/"


def parse_protocol(desc):
    """Pulse protocol of one set from its session_description."""
    s = desc.split("####")[0]
    m = re.search(r"first 1us long at (\d+)V, followed by an interval of (\d+)us before the second 1us long pulse at (\d+)", s)
    if m:
        return dict(kind="pair", v1=int(m.group(1)), interval_us=int(m.group(2)), v2=int(m.group(3)))
    m = re.search(r"single 1us long rectangular pulse at (\d+)V", s)
    if m:
        return dict(kind="single", v1=int(m.group(1)), interval_us=None, v2=None)
    if "sham recording" in s:
        return dict(kind="sham", v1=0, interval_us=None, v2=None)
    raise ValueError(s[:200])


def field_of(volts):
    """Field strength in V/cm for an amplitude in V, by the description's list in order."""
    if not volts:
        return 0.0
    return 1000 * FIELD_LIST_KVCM[VOLTS.index(volts)]


def otsu(x):
    h, e = np.histogram(x, 256)
    c = (e[:-1] + e[1:]) / 2
    w = np.cumsum(h)
    m = np.cumsum(h * c)
    wb, wf = w[:-1], w[-1] - w[:-1]
    mb = m[:-1] / np.maximum(wb, 1)
    mf = (m[-1] - m[:-1]) / np.maximum(wf, 1)
    return c[np.argmax(wb * wf * (mb - mf) ** 2)]


def split_touching(mask):
    """Label a mask, splitting touching cells: the local maxima of the distance transform above 0.6
    of the object's maximum are centres, and each pixel goes to the nearest centre of its object."""
    dist = ndimage.distance_transform_edt(mask)
    lab0, n0 = ndimage.label(mask)
    out = np.zeros(mask.shape, np.int32)
    k = 0
    for i in range(1, n0 + 1):
        obj = lab0 == i
        d = np.where(obj, dist, 0)
        dmax = d.max()
        if dmax < 3:
            continue
        pk = (d == ndimage.maximum_filter(d, size=int(1.2 * dmax) | 1)) & (d > 0.6 * dmax)
        pl, npk = ndimage.label(ndimage.binary_dilation(pk, iterations=2) & obj)
        mk = np.where(pl > 0, pl + k, 0)
        k += npk
        _, (iy, ix) = ndimage.distance_transform_edt(mk == 0, return_indices=True)
        out[obj] = mk[iy, ix][obj]
    return out, k


def solidity(ys, xs):
    """Area over convex-hull area (pixel centres; about 1.01 for a disc)."""
    return len(ys) / ConvexHull(np.c_[ys, xs]).volume


def find_cells(mean_img, dropped=None):
    """Whole, round cells of a mean image; objects left out for shape are appended to `dropped`.

    Each cell carries `own`, the pixels of the image that are its piece or background, so that the
    trace of a cell that touches another does not cross into it."""
    s = ndimage.gaussian_filter(mean_img, 3)
    lab, n = split_touching(ndimage.binary_fill_holes(s > otsu(s)))
    cells = []
    for i in range(1, n + 1):
        ys, xs = np.nonzero(lab == i)
        area = len(ys)
        if area < 700 or area > 12000:
            continue
        if ys.min() < 3 or xs.min() < 3 or ys.max() > mean_img.shape[0] - 4 or xs.max() > mean_img.shape[1] - 4:
            continue
        ev = np.linalg.eigvalsh(np.cov(np.c_[ys, xs].T))
        c = dict(cy=float(ys.mean()), cx=float(xs.mean()), area=int(area), r_eq=float(np.sqrt(area / np.pi)),
                 elongation=float(np.sqrt(ev[1] / ev[0])), solidity=float(solidity(ys, xs)))
        if c["elongation"] > 1.3 or c["solidity"] < 0.9:
            if dropped is not None:
                dropped.append(c)
            continue
        c["own"] = (lab == i) | (lab == 0)
        cells.append(c)
    return cells


def trace_coords(mean_img, cell):
    """Pixel coordinates of the 6-pixel-wide trace on the membrane ring, 360 angles x 6 offsets.

    Angle phi in degrees, counterclockwise from the image +x axis with the image y axis up."""
    sm = ndimage.gaussian_filter(mean_img, 1)
    phi = np.deg2rad(np.arange(N_ANG) + 0.5)
    r = cell["r_eq"] * np.linspace(0.3, 1.6, 131)
    yy = cell["cy"] - np.outer(np.sin(phi), r)
    xx = cell["cx"] + np.outer(np.cos(phi), r)
    prof = ndimage.map_coordinates(sm, [yy, xx], order=1)
    # outer edge of the membrane: the steepest fall of intensity along the ray between 0.7 and 1.4
    # equivalent radii; bright structures inside the cell do not move it
    grad = np.gradient(prof, axis=1)
    ok = (r >= 0.7 * cell["r_eq"]) & (r <= 1.4 * cell["r_eq"])
    grad[:, ~ok] = np.inf
    if "own" in cell:
        # a ray stops where it enters a touching cell
        inside = ndimage.map_coordinates(cell["own"].astype(np.float32), [yy, xx], order=0) > 0.5
        grad[~np.minimum.accumulate(inside, axis=1)] = np.inf
    rr = ndimage.median_filter(r[np.argmin(grad, axis=1)], size=15, mode="wrap")
    # the trace lies on the six pixels just inside the outer edge
    off = -np.arange(TRACE_WIDTH)[::-1] - 0.5
    rad = rr[:, None] + off[None, :]
    ty = cell["cy"] - np.sin(phi)[:, None] * rad
    tx = cell["cx"] + np.cos(phi)[:, None] * rad
    return ty, tx, rr


def load_set(asset):
    """Stream one set and reduce it: per cell, the trace of every frame (60 x 360)."""
    h = h5py.File(remfile.File(asset_url(asset["asset_id"])), "r")
    ds = h["acquisition/StrobeImaging/data"]
    x = ds[:].astype(np.float32)
    out = dict(
        path=asset["path"], asset_id=asset["asset_id"],
        subject=h["general/subject/subject_id"][()].decode(),
        session_id=h["general/session_id"][()].decode(),
        description=h["session_description"][()].decode(),
        session_start=h["session_start_time"][()].decode(),
        starting_time=float(h["acquisition/StrobeImaging/starting_time"][()]),
        rate=float(h["acquisition/StrobeImaging/starting_time"].attrs["rate"]),
        unit=h["acquisition/StrobeImaging/data"].attrs["unit"],
        shape=tuple(ds.shape), dtype=str(ds.dtype),
        acquisition=sorted(h["acquisition"].keys()),
        stimulus=sorted(h["stimulus/presentation"].keys()),
        processing=sorted(h["processing"].keys()),
        min=float(x.min()), max=float(x.max()), n_near_max=int((x >= 16000).sum()),
        frame_mean=x.reshape(len(x), -1).mean(1),
        data_hash=hashlib.md5(x.tobytes()).hexdigest(),
    )
    h.close()
    out.update(parse_protocol(out["description"]))
    mean_img = x.mean(0)
    out["mean_img_small"] = mean_img[::4, ::4].copy()
    out["base_img"] = x[:N_BASE].mean(0)
    out["pulse_img"] = x[N_BASE:].mean(0)
    dropped = []
    cells = find_cells(mean_img, dropped)
    out["dropped"] = dropped
    for c in cells:
        lab = np.hypot(*np.mgrid[:x.shape[1], :x.shape[2]] - np.array([c["cy"], c["cx"]])[:, None, None]) <= 1.3 * c["r_eq"]
        c["n_near_max"] = int((x[:, lab] >= 16000).sum())
        ty, tx, rr = trace_coords(mean_img, c)
        c["ring_r"] = float(np.median(rr))
        c["trace"] = np.stack([ndimage.map_coordinates(f, [ty, tx], order=1).mean(1) for f in x])
        # full-resolution crop of the mean image and the trace's outer edge, to show the placement
        h0 = int(np.ceil(1.7 * c["r_eq"]))
        y0, x0 = max(int(c["cy"]) - h0, 0), max(int(c["cx"]) - h0, 0)
        c["crop"] = mean_img[y0:int(c["cy"]) + h0, x0:int(c["cx"]) + h0].copy()
        c["crop_origin"] = (y0, x0)
        c["edge_r"] = rr.copy()
        del c["own"]
    out["cells"] = cells
    del out["base_img"], out["pulse_img"]
    return out


def load_all(assets, workers=8):
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(load_set, assets))


def profile_df(trace, start=N_BASE, stop=None, base_first=BASE_FIRST):
    """Collapsed dF profile (360 points, %): pulse frames start:stop against baseline frames
    base_first to N_BASE - 1."""
    f0 = trace[base_first:N_BASE].mean(0)
    f = trace[start:stop].mean(0)
    return 100 * (f - f0) / f0


def harmonic_phase(df):
    """Phase (degrees, image frame) and amplitude of the first angular harmonic of a profile."""
    phi = np.deg2rad(np.arange(N_ANG) + 0.5)
    z = np.mean(df * np.exp(1j * phi))
    return float(np.rad2deg(np.angle(z)) % 360), float(2 * np.abs(z))


def arc_index(center_deg, half=POLE_HALF):
    a = (np.arange(N_ANG) + 0.5 - center_deg + 180) % 360 - 180
    return np.abs(a) <= half


def pole_values(df, cathode_deg):
    """Mean dF in the +-5 degree arcs at the cathode-facing and anode-facing poles."""
    return float(df[arc_index(cathode_deg)].mean()), float(df[arc_index(cathode_deg + 180)].mean())


def pole_frames(trace, cathode_deg, base_first=BASE_FIRST):
    """Per-frame pole dF (Fig. 2 measure): arc mean F in each frame against F0, the baseline mean."""
    out = []
    for c in (cathode_deg, cathode_deg + 180):
        f = trace[:, arc_index(c)].mean(1)
        f0 = f[base_first:N_BASE].mean()
        out.append(100 * (f - f0) / f0)
    return np.array(out)


def lambda_f(lam_m, lam_i=0.4, lam_o=1.64, R=8e-6, d=5e-9):
    """Eq. (2) of the paper: the factor f that replaces 1.5 in Eq. (1) (Methods 2.3 constants)."""
    num = 3 * lam_o * (3 * R**2 * d * lam_i + (3 * d**2 * R - d**3) * (lam_m - lam_i))
    den = 2 * R**3 * (lam_m + 2 * lam_o) * (lam_m + lam_i / 2) - 2 * (R - d) ** 3 * (lam_o - lam_m) * (lam_i - lam_m)
    return num / den


def fov(subject):
    """Short name of a field of view ("subject"), such as c6."""
    return subject.replace("CHO_20230622_", "")


def match_cells(sets, max_drift=15):
    """Number each cell by the nearest cell of the first set of its field of view (centroid), and keep
    only the cells found, within `max_drift` pixels, in every set of the field of view, so that each
    measured cell is the same cell in all its sets. Returns the cells left out, per field of view."""
    first = {}
    for s in sets:
        ref = first.setdefault(s["subject"], s["cells"])
        for c in s["cells"]:
            d = [np.hypot(c["cy"] - r["cy"], c["cx"] - r["cx"]) for r in ref]
            c["cell_id"] = int(np.argmin(d))
            c["drift_px"] = float(np.min(d))
    left_out = {}
    for subj in first:
        group = [s for s in sets if s["subject"] == subj]
        ids = [{c["cell_id"] for c in s["cells"] if c["drift_px"] <= max_drift} for s in group]
        keep = set.intersection(*ids)
        for s in group:
            gone = [c for c in s["cells"] if c["cell_id"] not in keep or c["drift_px"] > max_drift]
            left_out.setdefault(subj, []).append(len(gone) + len(s.get("dropped", [])))
            s["cells"] = [c for c in s["cells"] if c["cell_id"] in keep and c["drift_px"] <= max_drift]
    return left_out


def _set_vectors(sets):
    """Amplitude-weighted first-harmonic vector of each pulse set, summed over its cells."""
    v = {}
    for s in sets:
        if s["kind"] == "sham":
            continue
        for c in s["cells"]:
            ph, amp = harmonic_phase(profile_df(c["trace"]))
            v[s["asset_id"]] = v.get(s["asset_id"], 0) + amp * np.exp(1j * np.deg2rad(ph))
    return v


def cathode_angles(sets):
    """Cathode-facing direction per field of view (degrees, image frame), from the data.

    The amplitude-weighted circular mean of the first-harmonic phase of the collapsed dF profile
    over every cell and every set with a pulse (sham sets left out)."""
    v = _set_vectors(sets)
    z = {}
    for s in sets:
        if s["asset_id"] in v:
            z[s["subject"]] = z.get(s["subject"], 0) + v[s["asset_id"]]
    return {k: float(np.rad2deg(np.angle(v)) % 360) for k, v in z.items()}


def cathode_angles_loo(sets):
    """Cathode-facing direction for each set (keyed by asset_id), from the other pulse sets of its
    field of view only, so that the set measured does not choose its own poles."""
    v = _set_vectors(sets)
    out = {}
    for s in sets:
        z = sum(v[t["asset_id"]] for t in sets
                if t["subject"] == s["subject"] and t["asset_id"] != s["asset_id"] and t["asset_id"] in v)
        out[s["asset_id"]] = float(np.rad2deg(np.angle(z)) % 360)
    return out


def angle_of(cath, s):
    """The cathode direction for set s from a dict keyed by asset_id or by subject."""
    return cath[s["asset_id"]] if s["asset_id"] in cath else cath[s["subject"]]


def pole_table(sets, cath, start=N_BASE, stop=None):
    """Collapsed pole dF per cell and set (Methods 2.3), with the uniform part of the profile.

    `cath_c` and `anod_c` subtract the profile's mean (its angle-independent part, which the sham sets
    show is not a field response); this is a variant, not the paper's measure."""
    import pandas as pd
    rows = []
    for s in sets:
        for c in s["cells"]:
            df = profile_df(c["trace"], start, stop)
            ca, an = pole_values(df, angle_of(cath, s))
            ph, amp = harmonic_phase(df)
            rows.append(dict(fov=fov(s["subject"]), cell=c["cell_id"], kind=s["kind"], interval_us=s["interval_us"],
                             V1=s["v1"], E1=field_of(s["v1"]), cath=ca, anod=an, offset=float(df.mean()),
                             cath_c=ca - float(df.mean()), anod_c=an - float(df.mean()), h1_phase=ph, h1_amp=amp,
                             r_eq=c["r_eq"], ring_r=c["ring_r"]))
    return pd.DataFrame(rows)


def log_asym(trace, cath_deg, half=20):
    """Per-frame log ratio of the cathode-facing to the anode-facing arc (+-20 degrees). A ratio of
    two parts of the same frame cancels the flash-to-flash laser fluctuation."""
    a = trace[:, arc_index(cath_deg, half)].mean(1)
    b = trace[:, arc_index(cath_deg + 180, half)].mean(1)
    return np.log(a / b)
