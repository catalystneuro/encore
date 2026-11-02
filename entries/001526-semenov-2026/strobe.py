"""Loading and membrane-trace measures for DANDI:001526 (Semenov et al. 2026).

The dandiset holds strobe (pulsed laser) fluorescence images of single CHO cells
loaded with Di-8-ANEPPS, one NWB file per set of 100 images at 6 Hz: the first
40 without a pulsed electric field (PEF) and the next 60 with it (paper, section
2.3). The files give the pulse duration and amplitude in volts in their
`session_description`; they give no field strength, no cell outline and no
pixel size.

Where each parameter comes from:

- Sets of 100 images, 40 baseline and 60 PEF; F0 the mean of the first 40
  images; dF = 100 (F - F0) / F0; mean F in the +-5 degree arcs at the poles;
  a 6-pixel-wide trace along the cell perimeter; 360 points along it
  (paper, section 2.3).
- Field strengths in V/cm: the paper labels its recordings in V/cm (Fig. 2C,
  Fig. 4D), the files in volts. The two are matched by order, which is
  monotonic in both (`FIELD_1US`, `FIELD_03US`). The labels are the paper's
  (Fig. 2C: 150, 230 and 1000 V/cm; Fig. 4D: 357, 760, 1000, 1200, 1420, 1630,
  2050, 2473 and 3320 V/cm, read from the figure's axis labels).
- The cell: the paper analyses one cell per experiment and outlines it by
  hand in MetaMorph. The files do not say which cell in the field of view was
  analysed. Assumption: the cell nearest the centre of the image, since the
  paper centres the field of view between the electrodes (section 2.2).
- The perimeter: the paper draws it by hand. Here it is found automatically as
  the ridge of the membrane staining (the radius of maximum baseline intensity
  along each of 360 rays from the cell centre), smoothed along the angle. The
  6-pixel-wide trace is sampled at radial offsets -2.5 to +2.5 pixels around
  that ridge. Points are spaced by 1 degree of polar angle, not by equal arc
  length; for the near-circular cells here the two differ little (a standard
  choice, stated as a deviation).
- Field direction: the angle of the cathodic pole is the phase of a cosine
  fitted to the polarization profile, pooled over the cells of a session
  (the electrodes do not move within a session; an assumption).
- Background: the paper subtracts none for the potentiometric dyes (section
  2.3) but subtracts a cell-free region for Fluo-4 (section 2.4); the claims
  file names both readings. `bg_annulus` is the per-image median of a
  cell-free annulus 2 to 3 radii from the cell centre, with other cells masked
  out (a standard choice of region).
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from pynwb import NWBHDF5IO
from scipy import ndimage

DANDISET = "001526"
VERSION = "0.261006.1851"
API = "https://api.dandiarchive.org/api"

N_BASE = 40      # images without PEF (paper, section 2.3)
N_PEF = 60       # images with PEF (paper, section 2.3)
N_POINTS = 360   # points along the perimeter (paper, section 2.3)
POLE_HALF_DEG = 5  # +-5 degree arcs at the poles (paper, section 2.3)
TRACE_WIDTH = 6    # pixels (paper, section 2.3)

# Field strength (V/cm) for each pulse amplitude (V), matched by order to the
# paper's labels: Fig. 2C for 1 us pulses, Fig. 4D for 0.3 us pulses.
FIELD_1US = {50: 150, 70: 230, 250: 1000}
FIELD_03US = {100: 357, 200: 760, 250: 1000, 300: 1200, 350: 1420, 400: 1630,
              500: 2050, 600: 2473, 800: 3320}


def list_assets() -> pd.DataFrame:
    """Every asset of the pinned version, with path, id and size."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        j = r.json()
        rows += [dict(path=a["path"], asset_id=a["asset_id"], size=a["size"]) for a in j["results"]]
        url = j["next"]
    return pd.DataFrame(rows)


def asset_url(asset_id: str) -> str:
    return f"{API}/assets/{asset_id}/download/"


def _open(asset_id: str):
    f = h5py.File(remfile.File(asset_url(asset_id)), "r")
    io = NWBHDF5IO(file=f, mode="r", load_namespaces=True)
    return f, io, io.read()


def parse_description(text: str) -> dict:
    """Pulse duration (us), amplitude (V), electrode distance (mm) and kind of recording."""
    head = text.split("####")[0]
    kind = "pef"
    if "sham" in head:
        kind = "sham"
    elif "background region" in head:
        kind = "background"
    dur = re.search(r"single ([\d.]+) (µs|ns) ", head)
    duration_us = None
    if dur:
        duration_us = float(dur.group(1)) / (1000.0 if dur.group(2) == "ns" else 1.0)
    amp = re.search(r"at (\d+) V amplitude", head)
    gap = re.search(r"Distance between electrodes ([\d.]+) mm", head)
    return dict(kind=kind, duration_us=duration_us,
                volts=int(amp.group(1)) if amp else (0 if kind == "sham" else None),
                electrode_mm=float(gap.group(1)) if gap else None)


def read_metadata(asset_id: str) -> dict:
    """Small metadata of one file, without reading the images."""
    f, io, nwb = _open(asset_id)
    try:
        s = nwb.acquisition["StrobeImaging"]
        out = dict(subject=nwb.subject.subject_id, session_id=nwb.session_id,
                   session_start=str(nwb.session_start_time),
                   starting_time=float(s.starting_time), rate=float(s.rate),
                   shape=tuple(s.data.shape), dtype=str(s.data.dtype), unit=s.unit,
                   description=nwb.session_description)
        out.update(parse_description(nwb.session_description))
        return out
    finally:
        io.close()
        f.close()


def table(max_workers: int = 16) -> pd.DataFrame:
    """One row per file: subject, kind, pulse, field strength and time order within the cell."""
    assets = list_assets()
    with ThreadPoolExecutor(max_workers) as ex:
        meta = list(ex.map(read_metadata, assets.asset_id))
    df = pd.concat([assets, pd.DataFrame(meta)], axis=1)
    df["cell"] = df.subject.str.replace("_bckg", "", regex=False)
    df = df.sort_values(["cell", "starting_time"]).reset_index(drop=True)

    def field(r):
        if r.kind != "pef" or r.volts is None:
            return np.nan
        lut = FIELD_1US if r.duration_us == 1.0 else FIELD_03US
        return lut.get(r.volts, np.nan)

    df["field"] = df.apply(field, axis=1)
    df["order"] = df.groupby("subject").cumcount()
    return df


def read_stack(asset_id: str) -> np.ndarray:
    """The 100 images of a file, as float32 (frames, rows, columns)."""
    f, io, nwb = _open(asset_id)
    try:
        return np.asarray(nwb.acquisition["StrobeImaging"].data[:], dtype=np.float32)
    finally:
        io.close()
        f.close()


# --- finding the cell and its membrane -------------------------------------------------

def cell_masks(img: np.ndarray) -> tuple[np.ndarray, int]:
    """Labelled masks of the stained cells in a baseline image (smoothed, thresholded, filled)."""
    s = ndimage.gaussian_filter(img, 3)
    bg = ndimage.median_filter(s[::4, ::4], size=25)
    bg = ndimage.zoom(bg, 4, order=1)[: img.shape[0], : img.shape[1]]
    hi = s - bg
    thr = 0.25 * np.percentile(hi, 99.9)
    m = ndimage.binary_fill_holes(ndimage.binary_opening(hi > thr, iterations=2))
    lab, n = ndimage.label(m)
    return lab, n


def central_cell(img: np.ndarray, near: tuple[float, float] | None = None, min_area: int = 800):
    """Centre (row, col) and equivalent radius of the cell nearest `near` (default: image centre)."""
    lab, n = cell_masks(img)
    if near is None:
        near = ((img.shape[0] - 1) / 2, (img.shape[1] - 1) / 2)
    best = None
    for i in range(1, n + 1):
        rr, cc = np.nonzero(lab == i)
        if rr.size < min_area:
            continue
        c = (rr.mean(), cc.mean())
        d = np.hypot(c[0] - near[0], c[1] - near[1])
        if best is None or d < best[0]:
            best = (d, c, np.sqrt(rr.size / np.pi), i)
    if best is None:
        raise ValueError("no cell found")
    return best[1], best[2], lab, best[3]


ANGLES = np.deg2rad(np.arange(N_POINTS))  # image angle of each perimeter point, from +column, counter-clockwise on screen


def _ray(center, r, ang):
    """Row and column of points at radii r along image angle ang (rows grow downwards)."""
    return center[0] - np.outer(np.sin(ang), r), center[1] + np.outer(np.cos(ang), r)


def membrane(img: np.ndarray, center, r0: float):
    """Centre and ridge radius (one per degree) of the membrane staining around a cell."""
    s = ndimage.gaussian_filter(img, 1.0)
    c = np.array(center, float)

    def ridge(c, r0, lo=0.4, hi=1.6):
        # The plasma membrane is the outer ridge of the staining: along each ray,
        # the steepest outward fall of intensity marks its outer edge, and the
        # ridge is the maximum within 6 pixels inside that edge. Internal
        # staining nearer the centre is ignored.
        r = np.arange(lo * r0, hi * r0, 0.25)
        rows, cols = _ray(c, r, ANGLES)
        prof = ndimage.map_coordinates(s, [rows, cols], order=1)
        grad = np.gradient(ndimage.uniform_filter1d(prof, 9, axis=1), axis=1)
        rm = np.empty(N_POINTS)
        for k in range(N_POINTS):
            e = int(np.argmin(grad[k]))
            win = (r >= r[e] - 6) & (r <= r[e])
            rm[k] = r[win][np.argmax(prof[k, win])]
        rm = ndimage.median_filter(rm, size=21, mode="wrap")
        return ndimage.uniform_filter1d(rm, size=9, mode="wrap")

    for _ in range(2):
        # first passes: wide search, then recentre
        rm = ridge(c, r0)
        y = c[0] - np.sin(ANGLES) * rm
        x = c[1] + np.cos(ANGLES) * rm
        A = np.c_[2 * x, 2 * y, np.ones_like(x)]
        sol = np.linalg.lstsq(A, x ** 2 + y ** 2, rcond=None)[0]
        c = np.array([sol[1], sol[0]])
        r0 = float(np.sqrt(sol[2] + sol[0] ** 2 + sol[1] ** 2))
    # last pass: search within 25% of the fitted circle
    return c, ridge(c, r0, 0.75, 1.25)


def trace_coords(center, rm):
    """Sampling points of the 6-pixel-wide trace: (2, 360, 6) rows and columns."""
    off = np.arange(TRACE_WIDTH) - (TRACE_WIDTH - 1) / 2
    rr = rm[:, None] + off[None, :]
    rows = center[0] - np.sin(ANGLES)[:, None] * rr
    cols = center[1] + np.cos(ANGLES)[:, None] * rr
    return np.stack([rows, cols])


def sample_trace(stack: np.ndarray, coords) -> np.ndarray:
    """Mean intensity across the trace width at each of the 360 points, per image: (frames, 360)."""
    out = np.empty((stack.shape[0], N_POINTS), np.float32)
    for k in range(stack.shape[0]):
        v = ndimage.map_coordinates(stack[k], coords.reshape(2, -1), order=1)
        out[k] = v.reshape(N_POINTS, TRACE_WIDTH).mean(1)
    return out


def annulus_mask(shape, center, radius, lab, inner=2.0, outer=3.0, dilate=6):
    """Cell-free annulus between inner and outer radii, other cells (dilated) masked out."""
    yy, xx = np.ogrid[: shape[0], : shape[1]]
    d = np.hypot(yy - center[0], xx - center[1])
    ring = (d >= inner * radius) & (d < outer * radius)
    cells = ndimage.binary_dilation(lab > 0, iterations=dilate)
    return ring & ~cells


def shift_between(ref: np.ndarray, img: np.ndarray, center, half: int = 80, max_shift: int = 15):
    """Integer (row, column) shift of `img` relative to `ref` near `center`, by cross-correlation.

    Used to follow a cell that drifts by a few pixels between recordings.
    """
    r, c = int(round(center[0])), int(round(center[1]))
    sl = (slice(max(r - half, 0), r + half), slice(max(c - half, 0), c + half))
    a = ref[sl] - ref[sl].mean()
    b = img[sl] - img[sl].mean()
    xc = np.fft.ifft2(np.fft.fft2(b) * np.conj(np.fft.fft2(a))).real
    xc = np.fft.fftshift(xc)
    cy, cx = np.array(xc.shape) // 2
    win = xc[cy - max_shift: cy + max_shift + 1, cx - max_shift: cx + max_shift + 1]
    dy, dx = np.unravel_index(np.argmax(win), win.shape)
    return dy - max_shift, dx - max_shift


def process(asset_id: str, ref: dict | None = None) -> dict:
    """Read one file and reduce it to the perimeter trace of the analysed cell, per image.

    Without `ref`, the cell nearest the image centre is found and its membrane
    traced. With `ref` (the result for the cell's first recording), the same
    trace is used, moved by the drift of the image measured by cross-correlation
    of the baseline images.

    Returns the trace (100, 360), the per-image background of the cell-free
    annulus (100,), the cell centre, radius and ridge radii, the shift from the
    reference, the whole-frame mean per image, and the baseline image.
    """
    st = read_stack(asset_id)
    base = st[:N_BASE].mean(0)
    lab, _ = cell_masks(base)
    if ref is None:
        c0, r0, lab, idx = central_cell(base)
        c, rm = membrane(base, c0, r0)
        shift = (0, 0)
    else:
        shift = shift_between(ref["base"], base, ref["center"])
        c = np.asarray(ref["center"]) + np.asarray(shift, float)
        rm = ref["rm"]
    coords = trace_coords(c, rm)
    tr = sample_trace(st, coords)
    ann = annulus_mask(base.shape, c, float(np.median(rm)), lab)
    bg = np.median(st[:, ann], axis=1) if ann.sum() > 50 else np.full(st.shape[0], np.nan)
    return dict(asset_id=asset_id, trace=tr, bg=bg.astype(np.float32), center=c, radius=float(np.median(rm)),
                rm=rm, shift=shift, frame_mean=st.reshape(st.shape[0], -1).mean(1), n_annulus=int(ann.sum()),
                base=base)


def process_background(asset_id: str, coords) -> np.ndarray:
    """Trace of a cell-free background recording sampled at a cell's trace coordinates: (100, 360)."""
    st = read_stack(asset_id)
    return sample_trace(st, coords)


# --- measures -------------------------------------------------------------------------

def pole_index(theta_cath_deg: float, half=POLE_HALF_DEG):
    """Indices of the perimeter points in the +-5 degree arcs at the cathodic and anodic poles."""
    k = np.arange(-half, half + 1)
    cath = (int(round(theta_cath_deg)) + k) % N_POINTS
    anod = (int(round(theta_cath_deg)) + 180 + k) % N_POINTS
    return cath, anod


def cosine_phase(profile: np.ndarray) -> tuple[float, float, float]:
    """Least-squares fit a + b cos(phi - phi0) with b > 0: returns (phi0 in degrees, b, a)."""
    X = np.c_[np.ones(N_POINTS), np.cos(ANGLES), np.sin(ANGLES)]
    a, p, q = np.linalg.lstsq(X, profile, rcond=None)[0]
    return float(np.rad2deg(np.arctan2(q, p)) % 360), float(np.hypot(p, q)), float(a)


def relative_angle(theta_cath_deg: float) -> np.ndarray:
    """Polar angle of each perimeter point from the cathodic pole, -180 to 180 degrees."""
    return (np.arange(N_POINTS) - theta_cath_deg + 180) % 360 - 180


def per_image_pole_df(trace, cath, anod, bg=None):
    """Pole dF (%) per image against F0, the mean of the first 40 images (paper, section 2.3)."""
    t = trace if bg is None else trace - bg[:, None]
    fc = t[:, cath].mean(1)
    fa = t[:, anod].mean(1)
    dfc = 100 * (fc - fc[:N_BASE].mean()) / fc[:N_BASE].mean()
    dfa = 100 * (fa - fa[:N_BASE].mean()) / fa[:N_BASE].mean()
    return dfc, dfa


def profile_df(trace, bg=None, pef=slice(N_BASE, N_BASE + N_PEF)):
    """dF (%) at each perimeter point, polarization image against baseline image (section 2.3)."""
    t = trace if bg is None else trace - bg[:, None]
    f0 = t[:N_BASE].mean(0)
    f = t[pef].mean(0)
    return 100 * (f - f0) / f0


# --- Eq. (2) ----------------------------------------------------------------------------

LAMBDA_I = 0.4      # S/m, cytoplasm (paper, section 2.3)
LAMBDA_O = 1.64     # S/m, medium (paper, section 2.3)
LAMBDA_M0 = 3e-7    # S/m, intact membrane (paper, section 2.3)
R_CELL = 8e-6       # m (paper, section 2.3)
D_MEM = 5e-9        # m (paper, section 2.3)


def f_eq2(lam_m, R=R_CELL, d=D_MEM, li=LAMBDA_I, lo=LAMBDA_O):
    """Eq. (2) of the paper, as printed in the PDF (section 2.3)."""
    lam_m = np.asarray(lam_m, float)
    num = 3 * lo * (3 * R ** 2 * d * li + (3 * d ** 2 * R - d ** 3) * (lam_m - li))
    den = 2 * R ** 3 * (lam_m + 2 * lo) * (lam_m + 0.5 * li) - 2 * (R - d) ** 3 * (lo - lam_m) * (li - lam_m)
    return num / den


def extract(df: pd.DataFrame, max_workers: int = 12) -> dict:
    """Reduce every cell recording of `df` (from `table`) to its perimeter trace.

    Each cell's first recording (the sham) fixes which cell is analysed (the
    cell nearest the image centre) and its membrane trace. Later recordings
    use the same trace, moved by the drift of the image between recordings. Background recordings (cell-free fields) are sampled at the trace
    coordinates of the cell's sham recording. Returns {asset_id: result}.
    """
    cells = df[df.kind != "background"]
    first = cells.groupby("cell").head(1)
    with ThreadPoolExecutor(max_workers) as ex:
        res = dict(zip(first.asset_id, ex.map(process, first.asset_id)))
    ref = {r.cell: res[r.asset_id] for r in first.itertuples()}
    rest = cells[~cells.asset_id.isin(first.asset_id)]
    with ThreadPoolExecutor(max_workers) as ex:
        res.update(zip(rest.asset_id, ex.map(lambda r: process(r.asset_id, ref[r.cell]),
                                             rest.itertuples())))
    for v in res.values():
        v["base"] = None  # keep memory small; geometry is kept
    bk = df[df.kind == "background"]
    coords = {r.cell: trace_coords(res[r.asset_id]["center"], res[r.asset_id]["rm"]) for r in first.itertuples()}
    with ThreadPoolExecutor(max_workers) as ex:
        res.update(zip(bk.asset_id, ex.map(lambda r: dict(asset_id=r.asset_id, trace=process_background(r.asset_id, coords[r.cell])),
                                           bk.itertuples())))
    return res


def session_phase(df: pd.DataFrame, res: dict, low: pd.Series) -> tuple[float, pd.DataFrame]:
    """Angle of the cathodic pole for a session: median over cells of the cosine phase.

    Each cell's phase is fitted to its mean polarization profile over the
    recordings selected by `low` (non-electroporating fields), without
    background subtraction (the phase does not depend on it).
    """
    rows = []
    for cell, g in df[low].groupby("cell"):
        p = np.mean([profile_df(res[a]["trace"]) for a in g.asset_id], 0)
        phi, amp, off = cosine_phase(p)
        rows.append(dict(cell=cell, phase_deg=phi, amplitude=amp, offset=off, n_sets=len(g)))
    t = pd.DataFrame(rows)
    return float(np.median(t.phase_deg)), t


def background_trace(res: dict, bk_asset: str | None, n=100):
    """Mean over images of a cell-free background recording, at the cell's trace points: (360,)."""
    if bk_asset is None:
        return None
    return res[bk_asset]["trace"].mean(0)


def corrected(trace, bg_mode: str, r: dict, bk_mean=None):
    """Trace with the background of the chosen reading removed.

    'none': raw intensities (section 2.3 describes no subtraction);
    'annulus': the per-image median of the cell-free annulus (as section 2.4 does for Fluo-4);
    'bckg_file': the mean of the cell-free background recording of the same cell, point by point.
    """
    if bg_mode == "none":
        return trace
    if bg_mode == "annulus":
        return trace - r["bg"][:, None]
    if bg_mode == "bckg_file":
        return trace - bk_mean[None, :]
    raise ValueError(bg_mode)


def per_image_table(df: pd.DataFrame, res: dict, phi: float, bg_mode: str,
                    bk: dict | None = None, f0_from: int = 0) -> pd.DataFrame:
    """Pole dF per image (100 per set) for every recording in `df`: long table.

    F0 is the mean of baseline images f0_from to 39 (section 2.3 uses all 40;
    f0_from=1 drops the first image, which is darker in most files).
    """
    cath, anod = pole_index(phi)
    rows = []
    for r in df.itertuples():
        R = res[r.asset_id]
        bkm = None if bk is None else bk.get(r.cell)
        t = corrected(R["trace"], bg_mode, R, bkm)
        fc = t[:, cath].mean(1)
        fa = t[:, anod].mean(1)
        f0c, f0a = fc[f0_from:N_BASE].mean(), fa[f0_from:N_BASE].mean()
        rows.append(pd.DataFrame(dict(asset_id=r.asset_id, cell=r.cell, field=r.field, order=r.order,
                                      image=np.arange(len(fc)),
                                      cathodic=100 * (fc - f0c) / f0c, anodic=100 * (fa - f0a) / f0a)))
    return pd.concat(rows, ignore_index=True)


def profile_table(df: pd.DataFrame, res: dict, bg_mode: str, pef=slice(N_BASE, N_BASE + N_PEF)):
    """Perimeter dF profile (360 points) of every recording: polarization against baseline image."""
    out = {}
    for r in df.itertuples():
        R = res[r.asset_id]
        t = corrected(R["trace"], bg_mode, R)
        out[r.asset_id] = profile_df(t, pef=pef)
    return out
