"""Loading and measures for the YO-PRO-1 images of dandiset 000631.

Kim, Semenov, Kiester, Keppler, Ibey, Bixler, Colunga Biancatelli & Pakhomov (2023), Int J Mol
Sci 24, 10921, doi:10.3390/ijms241310921.

Each NWB file holds one dish: one stitched image (`acquisition/ScaningImaging/data`, uint16,
rows x columns x 2) whose channel 0 is MemBrite (all cells) and channel 1 is YO-PRO-1 (YP, the
electroporation marker), as the ImageSeries description lists them. The files hold no pixel
size, no electrode positions, no ROIs and no angles. Files are streamed from the archive at the
pinned version: each file is fetched into memory by parallel HTTP range requests and its chunks
are decompressed there; nothing is written to disk.

Where the parameters come from:

- `UM_PER_PX = 0.65`: an assumption. The files give no pixel size. Methods 4.4 names the camera
  (ORCA-Flash4 sCMOS) and a 10x objective; the camera's 6.5 um pixels through a 10x objective
  give 0.65 um per pixel. The notebook checks it against the footprint of the 1.5 mm needles
  (Methods 4.2) and against the 32 ROIs of 200 um that Methods 4.4 places from base to apex.
- `ROI_UM = 200`, `N_ROI = 32`: Methods 4.4 ("a total of 32 ROIs (200 x 200 um) were placed
  along the dashed line").
- `ELECTRODE_OD_MM = 1.5`: Methods 4.2 (outside diameter of the hollow needles).
- `DISH_RADIUS_MM = 17.5`: Methods 4.3 (35 mm dish) and the claims file's angle reading (B).
  The dish centre is taken as the image centre (an assumption: the stitched tiles are laid out
  in a circle around the dish; it cannot move an angle by much, as the wall is far from the array).
- `FOOTPRINT_BG_MM = 0.5`: radius of the disk inside each footprint whose mean YP is the
  "spontaneous" uptake of background reading (b) (Methods 4.4: "measurements were also
  performed within the hollow electrodes' footprints"). A standard choice, inside the dark
  footprint seen in the images (radius about 0.65 mm).
- ROI layouts L1 and L2 (the claims file's "ROI layout" detail, left open by the paper): L1, 32
  ROIs evenly spaced from the base midpoint to the edge of the apex footprint; L2, 32 contiguous
  ROIs from the edge of the apex footprint back along the bisector through the base midpoint.
- Angle readings (B) and (C) of the claims file: a 2D conduction model with equipotential
  electrode disks and an insulating dish wall solved on a grid (B), and line sources at the
  electrode centres with no wall (C).
- `BLOCK = 10` pixels: the images are reduced to block means of 10 x 10 pixels (6.5 um) as they
  load; an ROI of 200 um is about 31 blocks wide. A standard choice that cannot change a
  result.
"""

from __future__ import annotations

import hashlib
import io
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import requests
from scipy import ndimage as ndi
from scipy import sparse
from scipy.signal import fftconvolve
from scipy.sparse.linalg import spsolve

DANDISET_ID = "000631"
DANDISET_VERSION = "0.231012.1508"
API = "https://api.dandiarchive.org/api"

UM_PER_PX = 0.65
BLOCK = 10
ROI_UM = 200.0
N_ROI = 32
ELECTRODE_OD_MM = 1.5
DISH_RADIUS_MM = 17.5
FOOTPRINT_BG_MM = 0.5
GRID_MM = 0.1          # grid step of the conduction model (B); a standard choice, checked at 0.05 mm
SATURATED = 60000     # padding outside the stitched tiles is 0 or near 65535


# --- loading --------------------------------------------------------------------------------

def list_assets(version: str = DANDISET_VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    return sorted(out, key=lambda a: a["path"])


def condition_of(path: str) -> dict:
    """Frequency and pulse train from the file name (sub-<...>-<1Hz|0,8MHz><BP|UP>-<date>-BPAE-<n>)."""
    sub = path.split("/")[0]
    freq = "1 Hz" if "1Hz" in sub else "833 kHz"
    train = "paired" if ("BP-" in sub or "HzBP" in sub) else "single"
    date = sub.split("BP-")[-1] if train == "paired" else sub.split("UP-")[-1]
    date = "-".join(date.split("-")[:3])
    return {"subject": sub[len("sub-"):], "freq": freq, "train": train, "date": date,
            "dish": sub.split("-")[-1]}


def _fetch(url: str, size: int, span: int = 32 * 2**20, threads: int = 16) -> bytearray:
    buf = bytearray(size)

    def get(a):
        b = min(a + span, size) - 1
        err = None
        for _ in range(6):
            try:
                r = requests.get(url, headers={"Range": f"bytes={a}-{b}"}, timeout=180)
                if len(r.content) == b - a + 1:
                    buf[a:b + 1] = r.content
                    return
                err = IOError(f"short read {len(r.content)}")
            except requests.RequestException as e:  # retry
                err = e
        raise err

    with ThreadPoolExecutor(threads) as ex:
        list(ex.map(get, range(0, size, span)))
    return buf


def load(asset: dict, block: int = BLOCK) -> dict:
    """Stream one file into memory and return its metadata and block-mean images (2, n, n)."""
    url = requests.get(f"{API}/assets/{asset['asset_id']}/download/", allow_redirects=False,
                       timeout=60).headers["Location"]
    buf = _fetch(url, asset["size"])
    f = h5py.File(io.BytesIO(buf), "r")
    d = f["acquisition/ScaningImaging/data"]
    N, M, C = d.shape
    cr, cc, _ = d.chunks
    infos = []
    d.id.chunk_iter(lambda c: infos.append((c.chunk_offset, c.byte_offset, c.size)))
    full = np.zeros((C, N, M), np.uint16)
    mv = memoryview(buf)
    hashes = {}

    def dec(it):
        off, bo, sz = it
        raw = mv[bo:bo + sz]
        hashes[off] = hashlib.md5(raw).hexdigest()
        x = np.frombuffer(zlib.decompress(raw), np.uint16).reshape(cr, cc)
        r0, c0, ch = off
        r1, c1 = min(r0 + cr, N), min(c0 + cc, M)
        full[ch, r0:r1, c0:c1] = x[:r1 - r0, :c1 - c0]

    with ThreadPoolExecutor(4) as ex:
        list(ex.map(dec, infos))
    nb_r, nb_c = N // block, M // block
    img = full[:, :nb_r * block, :nb_c * block].reshape(C, nb_r, block, nb_c, block).mean(
        (2, 4), dtype=np.float64).astype(np.float32)
    meta = {
        "path": asset["path"], "asset_id": asset["asset_id"], "size": asset["size"],
        "shape": (N, M, C), "chunks": d.chunks,
        "dtype": str(d.dtype),
        "data_attrs": {k: (v.decode() if isinstance(v, bytes) else v) for k, v in d.attrs.items()},
        "series_description": d.parent.attrs["description"],
        "session_description": f["session_description"][()].decode(),
        "session_id": f["general/session_id"][()].decode(),
        "session_start_time": f["session_start_time"][()].decode(),
        "subject_id": f["general/subject/subject_id"][()].decode(),
        "acquisition": list(f["acquisition"].keys()),
        "processing": list(f["processing"].keys()),
        "analysis": list(f["analysis"].keys()),
        "stimulus": list(f["stimulus/presentation"].keys()) + list(f["stimulus/templates"].keys()),
        "intervals": list(f["intervals"].keys()) if "intervals" in f else [],
        "chunk_digest": hashlib.md5("".join(hashes[k] for k in sorted(hashes)).encode()).hexdigest(),
        "full_min": int(full.min()), "full_max": int(full.max()),
    }
    meta.update(condition_of(asset["path"]))
    del full, buf
    return {"meta": meta, "img": img, "block": block}


def mm_per_block(block: int = BLOCK) -> float:
    return block * UM_PER_PX / 1000.0


# --- electrodes -----------------------------------------------------------------------------

def _disk(r):
    y, x = np.mgrid[-r:r + 1, -r:r + 1]
    return (x * x + y * y <= r * r).astype(float)


def _ring(r0, r1):
    y, x = np.mgrid[-r1:r1 + 1, -r1:r1 + 1]
    d = x * x + y * y
    return ((d > r0 * r0) & (d <= r1 * r1)).astype(float)


def footprint_score(yp: np.ndarray, down: int = 5, r_mm: float = 0.62) -> tuple[np.ndarray, int]:
    """Contrast of a dark disk against its surround, (ring - disk) / ring, on a coarser grid.

    The footprint of a hollow needle is a disk without YP uptake (the ImageSeries description:
    "dark circles indicate electrode footprints"). Returns the score map and the down-sampling.
    """
    n0, n1 = yp.shape[0] // down, yp.shape[1] // down
    x = yp[:n0 * down, :n1 * down].reshape(n0, down, n1, down).mean((1, 3)).astype(float)
    valid = ((x > 0) & (x < SATURATED)).astype(float)
    xc = np.where(valid > 0, x, 0)
    r = int(round(r_mm / mm_per_block(BLOCK * down)))
    D, R = _disk(r), _ring(r + 3, r + 15)
    inside = fftconvolve(xc, D, "same") / np.maximum(fftconvolve(valid, D, "same"), 1)
    outside = fftconvolve(xc, R, "same") / np.maximum(fftconvolve(valid, R, "same"), 1)
    full_in = fftconvolve(valid, D, "same") / D.sum()
    full_out = fftconvolve(valid, R, "same") / R.sum()
    with np.errstate(divide="ignore", invalid="ignore"):
        s = (outside - inside) / outside
    s[(full_in < 0.98) | (full_out < 0.98) | ~np.isfinite(s)] = -1
    return s, down


def _peaks(s, k, min_sep):
    y, x = np.ogrid[:s.shape[0], :s.shape[1]]
    s2, pts = s.copy(), []
    for _ in range(k):
        iy, ix = np.unravel_index(np.argmax(s2), s2.shape)
        pts.append((float(iy), float(ix), float(s2[iy, ix])))
        s2[(y - iy) ** 2 + (x - ix) ** 2 < min_sep ** 2] = -1
    return pts


def label_triangle(pts: np.ndarray) -> dict:
    """Apex is the vertex opposite the shortest side (the array is an isosceles triangle with the
    shorter side between the base electrodes, Figure 1); base electrodes are ordered by x."""
    d = [np.linalg.norm(pts[(i + 1) % 3] - pts[(i + 2) % 3]) for i in range(3)]
    a = int(np.argmin(d))
    base = [pts[(a + 1) % 3], pts[(a + 2) % 3]]
    base.sort(key=lambda p: p[1])
    return {"apex": pts[a], "base1": base[0], "base2": base[1]}


def find_electrodes_free(yp: np.ndarray, centre_frac: float = 0.33) -> dict:
    """The three strongest footprint candidates within `centre_frac` of the image size from its
    centre (the dish rim also scores, so it is excluded)."""
    s, down = footprint_score(yp)
    n = np.array(s.shape)
    y, x = np.ogrid[:s.shape[0], :s.shape[1]]
    s[(y - n[0] / 2) ** 2 + (x - n[1] / 2) ** 2 > (centre_frac * n.min()) ** 2] = -1
    pk = _peaks(s, 3, min_sep=2.0 / mm_per_block(BLOCK * down))
    pts = np.array([[p[0], p[1]] for p in pk]) * down + down / 2
    out = label_triangle(pts)
    out["scores"] = [p[2] for p in pk]
    return out


def fit_template(yp: np.ndarray, template: np.ndarray, centre_frac: float = 0.33,
                 refine_mm: float = 0.25) -> dict:
    """Fit a rigid triangle (template, 3 x 2 in blocks, apex first) to the footprint score map:
    the rotation and translation that maximise the summed score at the three vertices, then each
    vertex refined to the best score within `refine_mm`."""
    s, down = footprint_score(yp)
    n = np.array(s.shape)
    yy, xx = np.ogrid[:s.shape[0], :s.shape[1]]
    s[(yy - n[0] / 2) ** 2 + (xx - n[1] / 2) ** 2 > (centre_frac * n.min()) ** 2] = -1
    t = (template - template.mean(0)) / down
    best = (-np.inf, None)
    for th in np.deg2rad(np.arange(0, 360, 1.0)):
        R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
        p = np.rint(t @ R.T).astype(int)
        tot = np.zeros_like(s)
        for dy, dx in p:
            tot += np.roll(np.roll(s, -dy, 0), -dx, 1)
        iy, ix = np.unravel_index(np.argmax(tot), tot.shape)
        if tot[iy, ix] > best[0]:
            best = (tot[iy, ix], np.array([iy, ix]) + p)
    pts = best[1].astype(float)
    r = int(round(refine_mm / mm_per_block(BLOCK * down)))
    scores = []
    for i, (py, px) in enumerate(pts.astype(int)):
        win = s[max(py - r, 0):py + r + 1, max(px - r, 0):px + r + 1]
        jy, jx = np.unravel_index(np.argmax(win), win.shape)
        pts[i] = [max(py - r, 0) + jy, max(px - r, 0) + jx]
        scores.append(float(win[jy, jx]))
    pts = pts * down + down / 2
    out = label_triangle(pts)
    out["scores"] = scores
    return out


def triangle_template(geoms: list[dict]) -> np.ndarray:
    """Mean triangle (apex, base1, base2) in the frame of each triangle's own axes."""
    shapes = []
    for g in geoms:
        a, b1, b2 = g["apex"], g["base1"], g["base2"]
        m = (b1 + b2) / 2
        u = (a - m) / np.linalg.norm(a - m)
        v = np.array([-u[1], u[0]])
        shapes.append([[np.dot(p - m, u), np.dot(p - m, v)] for p in (a, b1, b2)])
    sh = np.array(shapes).mean(0)
    sh[1:, 1] = np.array([-1, 1]) * np.abs(sh[1:, 1]).mean()   # symmetric base
    sh[0, 1] = 0
    return sh[:, 0:1] * np.array([1, 0]) + sh[:, 1:2] * np.array([0, 1])


# --- field models (angle readings B and C) ---------------------------------------------------

def field_line_sources(centres_mm: np.ndarray, volts: np.ndarray, pts_mm: np.ndarray,
                       a_mm: float = ELECTRODE_OD_MM / 2) -> np.ndarray:
    """Reading (C): 2D line sources at the electrode centres, no wall. Charges q and a constant c
    satisfy phi(surface of electrode j) = V_j and sum(q) = 0. Returns E (n x 2)."""
    k = len(centres_mm)
    A = np.zeros((k + 1, k + 1))
    for j in range(k):
        for i in range(k):
            dist = a_mm if i == j else np.linalg.norm(centres_mm[j] - centres_mm[i])
            A[j, i] = np.log(dist)
        A[j, k] = 1.0
    A[k, :k] = 1.0
    q = np.linalg.solve(A, np.r_[volts, 0.0])[:k]
    E = np.zeros((len(pts_mm), 2))
    for i in range(k):
        d = pts_mm - centres_mm[i]
        E -= q[i] * d / (d ** 2).sum(1, keepdims=True)
    return E


class GridModel:
    """Reading (B): 2D conduction on a grid (finite differences, uniform conductivity), electrode
    disks held at fixed potentials, insulating circular wall of radius DISH_RADIUS_MM. One
    factorisation per dish, then one solve per configuration."""

    def __init__(self, centres_mm: np.ndarray, dish_centre_mm: np.ndarray, h_mm: float = GRID_MM,
                 a_mm: float = ELECTRODE_OD_MM / 2, R_mm: float = DISH_RADIUS_MM):
        n =int(np.ceil(2 * R_mm / h_mm)) + 3
        self.x0 = dish_centre_mm - (n // 2) * h_mm
        ys, xs = np.mgrid[:n, :n] * h_mm
        ys = ys + self.x0[0]
        xs = xs + self.x0[1]
        self.ys, self.xs, self.n, self.h = ys, xs, n, h_mm
        inside = (ys - dish_centre_mm[0]) ** 2 + (xs - dish_centre_mm[1]) ** 2 <= R_mm ** 2
        elec = np.full((n, n), -1)
        for i, c in enumerate(centres_mm):
            elec[((ys - c[0]) ** 2 + (xs - c[1]) ** 2 <= a_mm ** 2) & inside] = i
        self.inside, self.elec = inside, elec
        free = inside & (elec < 0)
        idx = -np.ones((n, n), int)
        idx[free] = np.arange(free.sum())
        self.idx, self.free = idx, free
        rows, cols, vals = [], [], []
        diag = np.zeros(free.sum())
        self.bcoef = []   # (row, electrode) couplings
        fy, fx = np.nonzero(free)
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = fy + dy, fx + dx
            nin = inside[ny, nx]
            # Neumann wall: no flux to points outside the dish
            diag += nin
            nf = nin & free[ny, nx]
            rows.append(idx[fy[nf], fx[nf]])
            cols.append(idx[ny[nf], nx[nf]])
            vals.append(-np.ones(nf.sum()))
            ne = nin & (elec[ny, nx] >= 0)
            self.bcoef.append((idx[fy[ne], fx[ne]], elec[ny[ne], nx[ne]]))
        rows.append(np.arange(free.sum()))
        cols.append(np.arange(free.sum()))
        vals.append(diag)
        A = sparse.csc_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))))
        from scipy.sparse.linalg import splu
        self.lu = splu(A)

    def potential(self, volts):
        b = np.zeros(self.free.sum())
        for r, e in self.bcoef:
            np.add.at(b, r, np.asarray(volts)[e])
        phi = np.zeros((self.n, self.n))
        phi[self.free] = self.lu.solve(b)
        for i, v in enumerate(volts):
            phi[self.elec == i] = v
        return phi

    def field(self, volts, pts_mm):
        phi = self.potential(volts)
        gy, gx = np.gradient(phi, self.h)
        fy = (pts_mm[:, 0] - self.x0[0]) / self.h
        fx = (pts_mm[:, 1] - self.x0[1]) / self.h
        ey = ndi.map_coordinates(-gy, [fy, fx], order=1)
        ex = ndi.map_coordinates(-gx, [fy, fx], order=1)
        return np.c_[ey, ex]


def angle_deg(E1: np.ndarray, E2: np.ndarray) -> np.ndarray:
    c = (E1 * E2).sum(1) / (np.linalg.norm(E1, axis=1) * np.linalg.norm(E2, axis=1))
    return np.degrees(np.arccos(np.clip(c, -1, 1)))


# --- ROIs -----------------------------------------------------------------------------------

def roi_centres(geom: dict, layout: str, n_roi: int = N_ROI) -> np.ndarray:
    """ROI centres in blocks along the bisector, from the base end to the apex end.

    L1: n_roi centres evenly spaced from the base midpoint to the apex footprint edge less half
    an ROI. L2: n_roi contiguous ROIs, the last touching the apex footprint, running back along
    the bisector through the base midpoint."""
    a, m = geom["apex"], (geom["base1"] + geom["base2"]) / 2
    u = (a - m) / np.linalg.norm(a - m)
    mpb = mm_per_block()
    L = np.linalg.norm(a - m) * mpb
    end = L - ELECTRODE_OD_MM / 2 - ROI_UM / 2000
    if layout == "L1":
        s = np.linspace(0.0, end, n_roi)
    elif layout == "L2":
        s = end - np.arange(n_roi)[::-1] * ROI_UM / 1000
    else:
        raise ValueError(layout)
    return m + np.outer(s / mpb, u)


def square_mean(img: np.ndarray, centre: np.ndarray, u: np.ndarray, side_mm: float = ROI_UM / 1000) -> float:
    """Mean of the blocks whose centres fall in a square of side `side_mm`, centred at `centre`
    (blocks) and aligned with the unit vector u."""
    h = side_mm / mm_per_block() / 2
    r = int(np.ceil(h * 1.5)) + 1
    cy, cx = int(round(centre[0])), int(round(centre[1]))
    y0, x0 = max(cy - r, 0), max(cx - r, 0)
    win = img[y0:cy + r + 1, x0:cx + r + 1]
    yy, xx = np.mgrid[y0:y0 + win.shape[0], x0:x0 + win.shape[1]] + 0.5
    dy, dx = yy - centre[0], xx - centre[1]
    along = dy * u[0] + dx * u[1]
    across = -dy * u[1] + dx * u[0]
    m = (np.abs(along) <= h) & (np.abs(across) <= h)
    return float(win[m].mean())


def disk_mean(img: np.ndarray, centre: np.ndarray, r_mm: float) -> float:
    r = r_mm / mm_per_block()
    R = int(np.ceil(r)) + 1
    cy, cx = int(round(centre[0])), int(round(centre[1]))
    y0, x0 = max(cy - R, 0), max(cx - R, 0)
    win = img[y0:cy + R + 1, x0:cx + R + 1]
    yy, xx = np.mgrid[y0:y0 + win.shape[0], x0:x0 + win.shape[1]] + 0.5
    return float(win[(yy - centre[0]) ** 2 + (xx - centre[1]) ** 2 <= r * r].mean())


def footprint_background(yp: np.ndarray, geom: dict) -> float:
    """Background reading (b): mean YP within FOOTPRINT_BG_MM of each electrode centre, averaged
    over the three electrodes."""
    return float(np.mean([disk_mean(yp, geom[k], FOOTPRINT_BG_MM) for k in ("apex", "base1", "base2")]))


def bisector_profile(img: np.ndarray, geom: dict, layout: str) -> np.ndarray:
    a, m = geom["apex"], (geom["base1"] + geom["base2"]) / 2
    u = (a - m) / np.linalg.norm(a - m)
    return np.array([square_mean(img, c, u) for c in roi_centres(geom, layout)])


def bisector_angles(geom: dict, layout: str, model: str, img_shape, grid: GridModel | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Angle between the field vectors of the two configurations (base1 at 1 V, base2 at 1 V,
    the other electrodes at 0) at each ROI centre, and the field strength (V/mm at 1 V) of the
    base1 configuration."""
    mpb = mm_per_block()
    centres = np.array([geom["apex"], geom["base1"], geom["base2"]]) * mpb
    pts = roi_centres(geom, layout) * mpb
    if model == "C":
        E1 = field_line_sources(centres, np.array([0.0, 1.0, 0.0]), pts)
        E2 = field_line_sources(centres, np.array([0.0, 0.0, 1.0]), pts)
    else:
        E1 = grid.field([0.0, 1.0, 0.0], pts)
        E2 = grid.field([0.0, 0.0, 1.0], pts)
    return angle_deg(E1, E2), np.linalg.norm(E1, axis=1)


def make_grid(geom: dict, img_shape) -> GridModel:
    mpb = mm_per_block()
    centres = np.array([geom["apex"], geom["base1"], geom["base2"]]) * mpb
    dish_centre = np.array(img_shape[-2:]) / 2 * mpb
    return GridModel(centres, dish_centre)


# --- Figure 2 measures ----------------------------------------------------------------------

def normalised(paired: np.ndarray, single: np.ndarray, reading: str) -> np.ndarray:
    """Paired-pulse value as % of the single-pulse value in the same ROI (claims file, Figure 2
    normalisation). paired: dishes x ROIs; single: dishes x ROIs.

    (i) the mean over every paired dish and control dish of their per-ROI ratio (the controls are
    separate dishes with no stated pairing, so every pairing is used); (ii) the ratio of the
    mean paired to the mean control value in each ROI. Returns (n_values, ROIs): the per-pair
    ratios for (i), one row for (ii)."""
    if reading == "i":
        return np.array([100 * p / c for p in paired for c in single])
    if reading == "ii":
        return (100 * paired.mean(0) / single.mean(0))[None, :]
    raise ValueError(reading)


def at_180(curve: np.ndarray, angles: np.ndarray, reading: int) -> tuple[float, int]:
    """Value 'at the 180 degree change': (1) the ROI of largest angle, (2) the ROI of lowest value."""
    k = int(np.argmax(angles)) if reading == 1 else int(np.argmin(curve))
    return float(curve[k]), k


def crossover(curve: np.ndarray, angles: np.ndarray, level: float = 100.0) -> float:
    """Largest angle at which the curve reaches `level`, walking from the largest angle down and
    interpolating linearly between neighbouring ROIs (claims file, fig2-crossover-angle)."""
    o = np.argsort(angles)[::-1]
    a, v = angles[o], curve[o]
    if v[0] >= level:
        return float(a[0])
    for j in range(1, len(v)):
        if v[j] >= level:
            f = (level - v[j - 1]) / (v[j] - v[j - 1])
            return float(a[j - 1] + f * (a[j] - a[j - 1]))
    return float("nan")


def radial_profile(img: np.ndarray, centre: np.ndarray, r_max_mm: float = 1.6, step_mm: float = 0.05):
    """Mean of img in rings of width step_mm around centre (blocks); returns ring mid radii (mm)
    and means."""
    mpb = mm_per_block()
    R = int(np.ceil(r_max_mm / mpb)) + 1
    cy, cx = int(round(centre[0])), int(round(centre[1]))
    y0, x0 = max(cy - R, 0), max(cx - R, 0)
    win = img[y0:cy + R + 1, x0:cx + R + 1]
    yy, xx = np.mgrid[y0:y0 + win.shape[0], x0:x0 + win.shape[1]] + 0.5
    r = np.hypot(yy - centre[0], xx - centre[1]) * mpb
    edges = np.arange(0, r_max_mm + step_mm, step_mm)
    k = np.digitize(r.ravel(), edges) - 1
    means = np.array([win.ravel()[k == i].mean() for i in range(len(edges) - 1)])
    return (edges[:-1] + edges[1:]) / 2, means


def edge_radius(radii: np.ndarray, prof: np.ndarray) -> float:
    """Radius where the profile first rises above half-way between its value at the centre
    (mean of rings within 0.3 mm) and its maximum outside."""
    inner = prof[radii < 0.3].mean()
    peak = prof.max()
    half = inner + 0.5 * (peak - inner)
    j = int(np.argmax(prof > half))
    if j == 0:
        return float("nan")
    f = (half - prof[j - 1]) / (prof[j] - prof[j - 1])
    return float(radii[j - 1] + f * (radii[j] - radii[j - 1]))


def adjacent_rois(geom: dict, which: str, gap_mm: float, direction: str) -> list[np.ndarray]:
    """Centres (blocks) of 200 um ROIs next to an electrode: the ROI's near edge at `gap_mm` from
    the footprint edge (1.5 mm outer diameter). direction 'centroid': one ROI on the line to the
    triangle's centroid; 'ring': eight ROIs at 45 degree steps around the electrode."""
    mpb = mm_per_block()
    c = geom[which]
    d_mm = ELECTRODE_OD_MM / 2 + gap_mm + ROI_UM / 2000
    if direction == "centroid":
        g = (geom["apex"] + geom["base1"] + geom["base2"]) / 3
        u = (g - c) / np.linalg.norm(g - c)
        return [c + u * d_mm / mpb]
    return [c + np.array([np.sin(t), np.cos(t)]) * d_mm / mpb for t in np.deg2rad(np.arange(0, 360, 45))]


def tile_rois(geom: dict, radius_mm: float = 4.0) -> np.ndarray:
    """Centres (blocks) of a grid of 200 um ROIs within radius_mm of the triangle's centroid and
    outside every footprint (with 0.1 mm margin); for the field-map correlation of fig4."""
    mpb = mm_per_block()
    g = (geom["apex"] + geom["base1"] + geom["base2"]) / 3
    step = ROI_UM / 1000 / mpb
    k = int(radius_mm / mpb / step)
    out = []
    for i in range(-k, k + 1):
        for j in range(-k, k + 1):
            p = g + np.array([i, j]) * step
            if np.linalg.norm(p - g) * mpb > radius_mm:
                continue
            if min(np.linalg.norm(p - geom[e]) * mpb for e in ("apex", "base1", "base2")) < ELECTRODE_OD_MM / 2 + 0.1 + ROI_UM / 2000 * np.sqrt(2):
                continue
            out.append(p)
    return np.array(out)


def field_at(geom: dict, pts_blocks: np.ndarray, energised: str, model: str, grid: GridModel | None = None) -> np.ndarray:
    """|E| (V/mm per volt applied) at points, with `energised` at 1 V and the others at 0."""
    mpb = mm_per_block()
    order = ("apex", "base1", "base2")
    volts = np.array([1.0 if k == energised else 0.0 for k in order])
    pts = pts_blocks * mpb
    if model == "C":
        E = field_line_sources(np.array([geom[k] for k in order]) * mpb, volts, pts)
    else:
        E = grid.field(list(volts), pts)
    return np.linalg.norm(E, axis=1)
