"""Loading and measures for the two-pulse strobe imaging of dandiset 001525.

Semenov, Silkuniene, Silkunas, Pakhomova, Bixler, Ibey, Kochunov & Pakhomov (2026),
Bioelectrochemistry 171, 109283, doi:10.1016/j.bioelechem.2026.109283.

Each NWB file holds one set of 100 images (512 x 512, uint16) of one Di-8-ANEPPS-loaded CHO
cell, taken at 6 Hz, one laser flash per image. Its `session_description` gives the pulses in
generator volts: a single 1-us pulse at 50 V, or a 1-us conditioning pulse at 100 to 350 V
followed after 1 or 5 us by a 1-us test pulse at 50 V. Files are streamed from the archive at
the pinned version; nothing is written to disk.

Where the parameters come from:

- 40 baseline images then 60 images with the pulse, collapsed into one baseline and one
  polarization image, dF = 100% (F - F0)/F0 per perimeter point, 360 points, pole arcs of
  +-5 degrees (Methods 2.3; Results 3.7, "Fig. 7B compares polarization at cell poles (within
  +-5o)"). `N_BASELINE`, `POLE_HALF_WIDTH_DEG`, `N_POINTS`.
- A 6-pixel-wide trace along the cell perimeter (Methods 2.3). The paper draws it by hand in
  MetaMorph; here it is found automatically (`find_cells`, `trace`): at each angle the cell's
  outer edge is the steepest outward fall of intensity along the ray, the membrane is the
  intensity peak within 8 pixels inside it (`EDGE_WINDOW_PX`), smoothed over angle, and F at that
  angle is the mean over 6 radial pixels centred on it (`TRACE_WIDTH_PX`). The first round's
  trace, the plain intensity peak along the ray, fell on bright dye inside some cells (c5, c9)
  and is kept as a variant ('dF_peak'). This is the author's implementation of the Methods'
  trace; the windows and the smoothing are standard choices.
- Which object is the cell: the paper images "one cell per experiment" (Fig. 2 legend). The
  field holds several cells; the one analysed is the largest object found in the subject's
  first file, then the object nearest that position in each later file (`pick_cell`). An
  assumption.
- The angle to the field: the dataset does not give the field direction in image
  coordinates. It is taken as the phase of a cosine fit to the dF profile, pooled over all
  files of the 5-us cells (`field_angle`), with 0 degrees at the depolarized (cathodic,
  dF > 0) pole, as Fig. 7A plots it. An assumption the data support (see the notebook).
- Frames without a laser flash: some images are dark (field mean near the camera floor). The
  paper does not mention them. `DARK_FRACTION` marks an image dark when its field mean is
  below 0.9 of the file's median; readings (a) keep them, as "collapsed" says nothing of
  them, (b) drop them, since they hold no fluorescence image. Both are run.
- Background: Methods 2.3 describe none for the potentiometric images (Methods 2.4 subtract a
  cell-free region for Fluo-4). Readings (a) none; (b) the median of an annulus 1.6 to 2.2
  times the cell radius, per collapsed image (`BG_ANNULUS`), a standard choice of cell-free
  region.
- Eq. (2) and its parameters (Methods 2.3): li 0.4 S/m, lo 1.64 S/m, R 8 um, d 5 nm, intact
  lm 3e-7 S/m.
"""
from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy import ndimage

DANDISET_ID = "001525"
DANDISET_VERSION = "0.261006.1856"
API = "https://api.dandiarchive.org/api"

N_BASELINE = 40
POLE_HALF_WIDTH_DEG = 5
N_POINTS = 360
TRACE_WIDTH_PX = 6
DARK_FRACTION = 0.9
BG_ANNULUS = (1.6, 2.2)
EDGE_WINDOW_PX = 8

# Eq. (2) parameters, Methods 2.3
LAMBDA_I = 0.4
LAMBDA_O = 1.64
LAMBDA_M_INTACT = 3e-7
R_CELL = 8e-6
D_MEMBRANE = 5e-9


def list_assets(version: str = DANDISET_VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        page = requests.get(url, timeout=60).json()
        out += page["results"]
        url = page["next"]
    return out


def s3_url(asset_id: str) -> str:
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url


def parse_protocol(desc: str) -> dict:
    """Pulse voltages and interval from a file's session_description."""
    m = re.search(r"single 1us long rectangular pulse at (\d+)V", desc)
    if m:
        return dict(kind="single", cond_v=None, test_v=int(m.group(1)), interval_us=None)
    m = re.search(r"first 1us long at (\d+)V, followed by an interval of (\d+)us before the "
                  r"second 1us long pulse at (\d+)V", desc)
    return dict(kind="pair", cond_v=int(m.group(1)), test_v=int(m.group(3)),
                interval_us=int(m.group(2)))


def read_file_meta(asset: dict) -> dict:
    h = h5py.File(remfile.File(s3_url(asset["asset_id"])), "r")
    s = h["acquisition/StrobeImaging"]
    desc = h["session_description"][()].decode()
    d = dict(path=asset["path"], asset_id=asset["asset_id"],
             subject=h["general/subject/subject_id"][()].decode(),
             start=h["session_start_time"][()].decode(), shape=s["data"].shape,
             rate=float(s["starting_time"].attrs["rate"]), unit=s["data"].attrs["unit"],
             description=desc, series_description=s.attrs["description"],
             electrode_gap=re.search(r"Distance between electrodes ([\d.]+ mm)", desc).group(1),
             dye=re.search(r"dye (\S+)", desc).group(1) if "dye" in desc else None)
    d.update(parse_protocol(desc))
    return d


def read_all_meta(assets: list[dict], workers: int = 16) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(read_file_meta, assets))


def load_frames(asset_id: str) -> np.ndarray:
    h = h5py.File(remfile.File(s3_url(asset_id)), "r")
    return h["acquisition/StrobeImaging/data"][:].astype(np.float32)


def dark_frames(x: np.ndarray) -> np.ndarray:
    fm = x.mean(axis=(1, 2))
    return fm < DARK_FRACTION * np.median(fm)


def collapse(x: np.ndarray, drop_dark: bool) -> tuple[np.ndarray, np.ndarray]:
    """Mean baseline image (first 40) and mean polarization image (last 60)."""
    keep = ~dark_frames(x) if drop_dark else np.ones(len(x), bool)
    b = x[:N_BASELINE][keep[:N_BASELINE]].mean(0)
    p = x[N_BASELINE:][keep[N_BASELINE:]].mean(0)
    return b, p


def find_cells(img: np.ndarray, min_area: int = 600) -> np.ndarray:
    """Candidate cells in a baseline image: rows of (x, y, equivalent radius, area), pixels.

    Bright membrane rings are found by thresholding (Otsu) the image after removing the
    slow background (difference of Gaussians, sigma 2 and 25 px), closing and filling holes;
    objects under `min_area` pixels are left out. Standard image-processing choices.
    """
    from skimage.filters import threshold_otsu
    hp = ndimage.gaussian_filter(img, 2) - ndimage.gaussian_filter(img, 25)
    mask = ndimage.binary_fill_holes(ndimage.binary_closing(hp > threshold_otsu(hp), iterations=3))
    lab, n = ndimage.label(mask)
    rows = []
    for i in range(1, n + 1):
        a = int((lab == i).sum())
        if a < min_area:
            continue
        cy, cx = ndimage.center_of_mass(lab == i)
        rows.append((cx, cy, np.sqrt(a / np.pi), a))
    return np.array(rows)


def pick_cell(img: np.ndarray, near: tuple[float, float] | None):
    """The analysed cell: the largest object (first file of a subject, `near` None), else the
    object nearest the subject's cell position. An assumption: the paper images one cell per
    experiment and does not say how it was chosen; in every 5-us subject the largest object is a
    whole, well-stained ring near the field centre."""
    cells = find_cells(img)
    if near is None:
        i = int(np.argmax(cells[:, 3]))
    else:
        i = int(np.argmin(np.hypot(cells[:, 0] - near[0], cells[:, 1] - near[1])))
    return float(cells[i, 0]), float(cells[i, 1]), float(cells[i, 2])


def _edge_profiles(sm, cx, cy, r0, ang):
    rr = np.arange(0.6 * r0, 1.35 * r0, 0.5)
    prof = ndimage.map_coordinates(sm, [cy + np.outer(np.sin(ang), rr), cx + np.outer(np.cos(ang), rr)], order=1)
    prof = ndimage.uniform_filter1d(prof, 9, axis=0, mode="wrap")
    return rr, prof, np.argmin(np.gradient(prof, axis=1), axis=1)


def outer_edge(img: np.ndarray, cx: float, cy: float, r0: float) -> np.ndarray:
    """Radius (pixels) of the cell's outer edge per degree: the steepest outward fall of intensity."""
    ang = np.deg2rad(np.arange(N_POINTS) + 0.5)
    rr, _, edge = _edge_profiles(ndimage.gaussian_filter(img, 1), cx, cy, r0, ang)
    return rr[edge]


def trace(img: np.ndarray, cx: float, cy: float, r0: float, method: str = "edge"):
    """Membrane radius per degree, smoothed over angle.

    'edge' (main): along each ray the cell's outer edge is the steepest outward fall of intensity
    within 0.6 to 1.35 times the object's equivalent radius, and the membrane is the intensity peak
    within 8 pixels inside that edge. 'peak' (the first round's trace, a variant): the peak of
    intensity along the ray within 0.7 to 1.35 times the radius, which can fall on bright dye inside
    the cell. The windows and smoothing are standard choices."""
    ang = np.deg2rad(np.arange(N_POINTS) + 0.5)
    sm = ndimage.gaussian_filter(img, 1)
    if method == "peak":
        rr = np.arange(0.7 * r0, 1.35 * r0, 0.5)
        prof = ndimage.map_coordinates(sm, [cy + np.outer(np.sin(ang), rr), cx + np.outer(np.cos(ang), rr)], order=1)
        rpk = rr[np.argmax(prof, axis=1)]
    else:
        rr, prof, edge = _edge_profiles(sm, cx, cy, r0, ang)
        lo = np.maximum(edge - int(EDGE_WINDOW_PX / 0.5), 0)    # radii are in 0.5-pixel steps
        rpk = np.array([rr[lo[i] + np.argmax(prof[i, lo[i]:edge[i] + 1])] for i in range(N_POINTS)])
    rpk = ndimage.median_filter(rpk, size=15, mode="wrap")
    rpk = ndimage.uniform_filter1d(rpk, size=9, mode="wrap")
    return ang, rpk


def sample_trace(img: np.ndarray, cx: float, cy: float, ang: np.ndarray, rpk: np.ndarray):
    """Mean intensity across the 6-pixel-wide trace at each of the 360 points."""
    offs = np.arange(TRACE_WIDTH_PX) - (TRACE_WIDTH_PX - 1) / 2
    r = rpk[:, None] + offs[None, :]
    xs = cx + np.cos(ang)[:, None] * r
    ys = cy + np.sin(ang)[:, None] * r
    return ndimage.map_coordinates(img, [ys, xs], order=1).mean(1)


def annulus_background(img: np.ndarray, cx: float, cy: float, r0: float) -> float:
    yy, xx = np.indices(img.shape)
    d = np.hypot(xx - cx, yy - cy)
    m = (d >= BG_ANNULUS[0] * r0) & (d <= BG_ANNULUS[1] * r0)
    return float(np.median(img[m]))


def image_profiles(x: np.ndarray, near: tuple[float, float]) -> dict:
    """Everything one file gives: cell position, dark frames, and dF profiles under each reading.

    Profiles are indexed by image angle (degrees, 0.5 to 359.5, counter-clockwise in pixel
    coordinates with y down) and later rotated to the angle to the field.
    """
    dark = dark_frames(x)
    b_all, _ = collapse(x, drop_dark=False)
    cx, cy, r0 = pick_cell(b_all, near)
    ang, rpk = trace(b_all, cx, cy, r0, "edge")
    _, rpk_peak = trace(b_all, cx, cy, r0, "peak")
    out = dict(cx=cx, cy=cy, r0=r0, r_membrane=float(np.mean(rpk)), n_dark=int(dark.sum()),
               dark_idx=np.flatnonzero(dark).tolist(), frame_mean=x.mean(axis=(1, 2)), rpk=rpk,
               rpk_peak=rpk_peak)
    # per-frame trace intensity, for the clock check, and per-frame annulus background, for the
    # baseline trend
    out["frame_trace"] = np.array([sample_trace(f, cx, cy, ang, rpk) for f in x])
    yy, xx = np.indices(x.shape[1:])
    d = np.hypot(xx - cx, yy - cy)
    ring = (d >= BG_ANNULUS[0] * r0) & (d <= BG_ANNULUS[1] * r0)
    out["frame_bg"] = np.median(x[:, ring], axis=1)
    # the baseline image around the cell (2.5 radii), for the overlay of cell and trace
    h = int(round(2.5 * r0))
    y0, x0 = max(int(cy) - h, 0), max(int(cx) - h, 0)
    out["crop"], out["crop_origin"] = b_all[y0:int(cy) + h, x0:int(cx) + h].copy(), (x0, y0)
    for drop in (False, True):
        b, p = collapse(x, drop)
        for name, rr_ in (("dF", rpk), ("dF_peak", rpk_peak)):
            fb, fp = sample_trace(b, cx, cy, ang, rr_), sample_trace(p, cx, cy, ang, rr_)
            for bg in (False, True):
                bb = annulus_background(b, cx, cy, r0) if bg else 0.0
                bp = annulus_background(p, cx, cy, r0) if bg else 0.0
                out[(name, drop, bg)] = 100.0 * ((fp - bp) - (fb - bb)) / (fb - bb)
                if name == "dF":
                    out[("bg", drop, bg)] = (bb, bp)
    return out


def rotate_to_field(profile: np.ndarray, phi_deg: float) -> np.ndarray:
    """Resample an image-angle profile to the angle to the field (0 = cathodic pole)."""
    a = (np.arange(N_POINTS) + 0.5 + phi_deg) % 360
    src = np.arange(N_POINTS) + 0.5
    return np.interp(a, np.r_[src - 360, src, src + 360], np.r_[profile, profile, profile])


def cosine_fit(theta_deg: np.ndarray, y: np.ndarray):
    """Least-squares A cos(theta - phi): returns A, phi (degrees) and R^2 (about the mean)."""
    t = np.deg2rad(theta_deg)
    X = np.c_[np.cos(t), np.sin(t)]
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    A = float(np.hypot(*c))
    phi = float(np.rad2deg(np.arctan2(c[1], c[0])))
    fit = X @ c
    r2 = 1 - np.sum((y - fit) ** 2) / np.sum((y - y.mean()) ** 2)
    return A, phi, float(r2), fit


def pole_means(profile_field: np.ndarray) -> tuple[float, float]:
    """Mean dF in +-5 degree arcs at the cathodic (0) and anodic (180 degree) poles."""
    th = np.arange(N_POINTS) + 0.5
    d0 = np.abs((th + 180) % 360 - 180)
    d180 = np.abs(th - 180)
    return (float(profile_field[d0 <= POLE_HALF_WIDTH_DEG].mean()),
            float(profile_field[d180 <= POLE_HALF_WIDTH_DEG].mean()))


def f_factor(lm: np.ndarray, R: float = R_CELL, d: float = D_MEMBRANE, li: float = LAMBDA_I,
             lo: float = LAMBDA_O) -> np.ndarray:
    """Eq. (2): the factor replacing 1.5 in the Schwan equation (thin conducting shell)."""
    lm = np.asarray(lm, float)
    num = 3 * lo * (3 * R ** 2 * d * li + (3 * d ** 2 * R - d ** 3) * (lm - li))
    den = (2 * R ** 3 * (lm + 2 * lo) * (lm + li / 2)
           - 2 * (R - d) ** 3 * (lo - lm) * (li - lm))
    return num / den


def process_subject(files: list[dict]) -> list[dict]:
    """Profiles for every file of one subject, in recording order (`files` from read_all_meta)."""
    files = sorted(files, key=lambda d: d["start"])
    out, near = [], None
    for d in files:
        x = load_frames(d["asset_id"])
        o = image_profiles(x, near)
        if near is None:
            near = (o["cx"], o["cy"])
        o["data_digest"] = float(np.float64(x[::7, ::16, ::16].sum()))
        o.update({k: d[k] for k in ("path", "subject", "start", "kind", "cond_v", "test_v",
                                    "interval_us")})
        out.append(o)
    return out


def process_subjects(meta: list[dict], subjects: list[str], workers: int = 6) -> dict:
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(lambda s: process_subject([d for d in meta if d["subject"] == s]), subjects)
        return dict(zip(subjects, res))


def field_angle(results: dict, key=("dF", True, False)) -> tuple[float, list[float]]:
    """Image angle (degrees) of the depolarized pole, from cosine fits pooled over files.

    Each file's profile is fit with A cos(angle - phi); the field angle is the circular mean of
    phi weighted by A. Returns it with every file's phi."""
    th = np.arange(N_POINTS) + 0.5
    z, phis = 0j, []
    for files in results.values():
        for o in files:
            A, phi, _, _ = cosine_fit(th, o[key])
            phis.append(phi)
            z += A * np.exp(1j * np.deg2rad(phi))
    return float(np.rad2deg(np.angle(z))), phis


# Conditioning strengths of Fig. 7A (V/cm), in the order of the dataset's generator voltages.
# The files give volts only; the paper's Fig. 7A panels are labelled 150/150, 360/150,
# 570/150, 760/150, 1,000/150, 1,200/150 and 1,400/150, and the files hold a single 50 V pulse
# and conditioning pulses of 100 to 350 V in 50 V steps, each followed by a 50 V test pulse.
# The mapping by rank, with the single 50 V pulse as the 150/150 benchmark, is an assumption.
STRENGTH_V_CM = {"single": 150, 100: 360, 150: 570, 200: 760, 250: 1000, 300: 1200, 350: 1400}
LEVELS = list(STRENGTH_V_CM)


def level_of(o: dict):
    return "single" if o["kind"] == "single" else o["cond_v"]


def profiles_by_level(results: dict, subjects: list[str], key, phi: float,
                      benchmark: str = "mean") -> dict:
    """{level: array (cells, 360)} of dF against the angle to the field.

    `benchmark` says which single-pulse file is the cell's 150/150 control when it has two:
    'mean' of both, 'first' or 'last'."""
    out = {}
    for L in LEVELS:
        rows = []
        for s in subjects:
            fs = [o for o in results[s] if level_of(o) == L]
            if L == "single":
                fs = {"mean": fs, "first": fs[:1], "last": fs[-1:]}[benchmark]
            rows.append(np.mean([rotate_to_field(o[key], phi) for o in fs], axis=0))
        out[L] = np.array(rows)
    return out


def pole_values(prof: dict) -> dict:
    """{level: (cathodic dF per cell, anodic dF per cell)}."""
    return {L: tuple(np.array(v) for v in zip(*[pole_means(p) for p in P]))
            for L, P in prof.items()}


def polarization(poles: dict, L, pole: str) -> np.ndarray:
    """Per-cell polarization magnitude at a pole reading: 'cathodic' (dF), 'anodic' (-dF) or
    'mean' of both ((cathodic - anodic) / 2)."""
    c, a = poles[L]
    return {"cathodic": c, "anodic": -a, "mean": (c - a) / 2}[pole]
