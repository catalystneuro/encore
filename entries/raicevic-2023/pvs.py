"""Loading and cross-section measures for dandiset 000491 (Raicevic et al. 2023).

The dandiset holds, for 14 pial artery segments (locations A to N), the 3D two-photon stacks and
the final binary segmentations of the vessel (``PlaneSegmentationChanA``) and of the perivascular
space (``PlaneSegmentationChanC``). This module streams the masks and repeats the paper's pipeline
from the segmentation onwards: isotropic sampling, vessel centerline, normal cross sections,
exclusion of cross sections near the edge of the volume, areas, the circle fit of the vessel, the
ellipse, spline and polynomial fits of the PVS, and the hydraulic resistance per unit length.

Where each parameter comes from is said next to it. "Claims P<n>" refers to the pipeline in the
opening comment of ``claims/000491/10.21203-rs.3.rs-2587250-v1.yaml``, whose open details are run
under every reading it names; "Methods, <section>" cites the paper's Methods (Research Square
preprint v1); "standard choice" marks a detail that cannot change a result; "assumption" marks a
choice the paper does not make that could, stated in the attempt record.
"""
from __future__ import annotations

import numpy as np
import requests
import h5py
import remfile
from scipy import ndimage, sparse
from scipy.interpolate import CubicSpline
from scipy.sparse.csgraph import connected_components, dijkstra
from scipy.sparse.linalg import spsolve
from skimage.morphology import skeletonize, convex_hull_image

DANDISET = "000491"
VERSION = "0.230602.1307"  # latest published version; the earlier one lacks the PVS masks of L, M, N
API = "https://api.dandiarchive.org/api"
XY_UM = 0.648  # Methods, In vivo two-photon laser scanning microscopy; and reference_frame in the files
MU = 7.058e-4  # Pa s, viscosity of water at 36 C (Methods, Hydraulic resistance)
EROSIONS = (1, 3, 5)  # claims P6 readings
DPDX = 500.0  # Pa/m, pressure gradient for the velocity profile (Methods, Hydraulic resistance)


# ----------------------------------------------------------------------------------------------
# Loading
# ----------------------------------------------------------------------------------------------
def list_assets(version: str = VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=100"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    return sorted(out, key=lambda a: a["path"])


def open_asset(asset: dict) -> h5py.File:
    url = f"{API}/assets/{asset['asset_id']}/download/"
    return h5py.File(remfile.File(url), "r")


def location_of(f: h5py.File) -> str:
    """The paper's location letter, from the file's experiment_description."""
    d = f["general/experiment_description"][()].decode()
    return d.split("labeled as location")[1].strip()[0]


def voxel_size(f: h5py.File) -> tuple[float, float, float]:
    """(x, y, z) voxel size in um from reference_frame of imaging_plane1."""
    s = f["general/optophysiology/imaging_plane1/reference_frame"][()].decode()
    return tuple(float(v) for v in s.strip("()").split(","))


FILLED_PLANE = 0.9  # assumption, see clear_filled_planes


def clear_filled_planes(pvs: np.ndarray) -> np.ndarray:
    """Clear the PVS mask in planes where it covers more than 90% of the field. In locations E and
    F the deposited PVS mask fills every plane below a depth (87 and 58 planes); no other plane of
    any file is more than 50% PVS. A plane filled edge to edge is not a segmentation of the space
    around the artery (assumption)."""
    out = pvs.copy()
    out[pvs.mean((1, 2)) > FILLED_PLANE] = False
    return out


def load_masks(f: h5py.File):
    """Vessel and PVS masks as stored, indexed (z, y, x); z increases with depth."""
    seg = f["processing/ophys/ImageSegmentation"]
    ves = seg["PlaneSegmentationChanA/image_mask"][()].astype(bool)
    pvs = seg["PlaneSegmentationChanC/image_mask"][()].astype(bool)
    return ves, pvs


# ----------------------------------------------------------------------------------------------
# Centerline (claims P1, P2; Methods, Creating normal cross sections)
# ----------------------------------------------------------------------------------------------
def isotropic(mask: np.ndarray, dz: float, target: float, dxy: float = XY_UM) -> np.ndarray:
    """Resample a (z, y, x) mask to cubic voxels of size ``target`` um (claims P1), by linear
    interpolation thresholded at 0.5 (standard choice)."""
    zoom = (dz / target, dxy / target, dxy / target)
    if np.allclose(zoom, 1):
        return mask.copy()
    return ndimage.zoom(mask.astype(np.float32), zoom, order=1) > 0.5


def centerline(ves: np.ndarray, dz: float, target: float, reading: str = "a", info: dict | None = None):
    """Vessel centerline points in um, (x, y, z) with z the depth.

    The skeleton is skimage's 3D thinning, the equivalent of MATLAB bwskel (claims P2), of the
    largest connected vessel region on the isotropic grid. Reading "a" keeps the longest path
    through the skeleton (side branches dropped), then removes erroneous points with
    ``clean_path``; reading "b" keeps all skeleton points (claims P2). ``info``, when given, is
    filled with the path's length before and after cleaning.
    """
    z0, z1 = np.nonzero(ves.any((1, 2)))[0][[0, -1]]
    sub = ves[z0 : z1 + 1]
    iso = isotropic(sub, dz, target)
    lab, n = ndimage.label(iso)
    if n > 1:
        sizes = ndimage.sum(iso, lab, range(1, n + 1))
        iso = lab == (1 + int(np.argmax(sizes)))
    sk = skeletonize(iso)
    pts = np.argwhere(sk)  # (z, y, x) on the isotropic grid
    # graph of 26-connected skeleton voxels
    idx = -np.ones(sk.shape, dtype=np.int64)
    idx[tuple(pts.T)] = np.arange(len(pts))
    rows, cols, w = [], [], []
    for dzz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if (dzz, dy, dx) <= (0, 0, 0):
                    continue
                q = pts + (dzz, dy, dx)
                ok = np.all((q >= 0) & (q < sk.shape), axis=1)
                j = np.full(len(pts), -1)
                j[ok] = idx[tuple(q[ok].T)]
                m = j >= 0
                rows.append(np.nonzero(m)[0]); cols.append(j[m])
                w.append(np.full(m.sum(), np.sqrt(dzz * dzz + dy * dy + dx * dx)))
    rows, cols, w = map(np.concatenate, (rows, cols, w))
    g = sparse.coo_matrix((w, (rows, cols)), shape=(len(pts),) * 2).tocsr()
    g = g + g.T
    nc, comp = connected_components(g, directed=False)
    big = comp == np.bincount(comp).argmax()
    if reading == "a":
        start = np.nonzero(big)[0][0]
        d = dijkstra(g, indices=start)
        d[~np.isfinite(d)] = -1
        a = int(np.argmax(d))
        d, pred = dijkstra(g, indices=a, return_predecessors=True)
        d[~np.isfinite(d)] = -1
        b = int(np.argmax(d))
        path = [b]
        while path[-1] != a:
            path.append(pred[path[-1]])
        sel = pts[np.array(path[::-1])]
    else:
        sel = pts[big]
    zyx_um = sel * target
    zyx_um[:, 0] += z0 * dz
    xyz = zyx_um[:, ::-1]  # (x, y, z)
    if reading != "a":
        return xyz
    # inscribed radius of the vessel at each path point, from the stored (anisotropic) mask
    edt = ndimage.distance_transform_edt(ves, sampling=(dz, XY_UM, XY_UM))
    ijk = np.round(xyz[:, ::-1] / (dz, XY_UM, XY_UM)).astype(int)
    ijk = np.clip(ijk, 0, np.array(ves.shape) - 1)
    keep = clean_path(xyz, edt[tuple(ijk.T)])
    if info is not None:
        info["_path"] = (xyz, keep)
        step = np.linalg.norm(np.diff(xyz, axis=0), axis=1)
        info.update(path_points=len(xyz), path_length_um=float(step.sum()),
                    path_chord_um=float(np.linalg.norm(xyz[-1] - xyz[0])), kept_points=int(keep.sum()),
                    kept_chord_um=float(np.linalg.norm(xyz[keep][-1] - xyz[keep][0])),
                    tube_radius_um=float(np.percentile(edt[tuple(ijk.T)], 95)))
    return xyz[keep]


def _curve(pts, keep):
    """Second-order polynomial fit of the centerline (as in ``fit_centerline``), sampled densely:
    the distance of every point from the fitted curve, and the arc length along the curve of the
    nearest curve point."""
    from scipy.spatial import cKDTree

    p = pts[keep]
    ax = int(np.ptp(p[:, 1]) > np.ptp(p[:, 0]))
    o = 1 - ax
    po, pz = np.polyfit(p[:, ax], p[:, o], 2), np.polyfit(p[:, ax], p[:, 2], 2)
    u = np.linspace(pts[:, ax].min() - 50, pts[:, ax].max() + 50, 8000)
    c = np.zeros((len(u), 3))
    c[:, ax], c[:, o], c[:, 2] = u, np.polyval(po, u), np.polyval(pz, u)
    s = np.r_[0, np.cumsum(np.linalg.norm(np.diff(c, axis=0), axis=1))]
    d, j = cKDTree(c).query(pts)
    return d, s[j]


def clean_path(pts: np.ndarray, radius: np.ndarray) -> np.ndarray:
    """Remove erroneous centerline points, which the paper did by hand (Methods, Creating normal
    cross sections: "We estimated the vessel centerline using MATLAB's bwskel function, then
    manually removed erroneous points"). Assumption, two rules, since the paper does not say
    which points it removed:

    1. A point farther from the second-order polynomial fit of the centerline than the vessel's
       radius lies outside the vessel around the fitted centerline (a branch, or a spur of the
       thinning toward a corner of a cut end). The radius is the 95th percentile of the vessel's
       inscribed radius along the path (robust to the thin branches the path may run through);
       the fit is repeated without the removed points until no point changes.
    2. A point whose position along the fitted centerline does not go beyond every earlier point
       on the path revisits a stretch already sampled (a loop, or the path doubling back), and
       would give a second cross section at the same place.

    Returns a boolean mask over ``pts`` (path order)."""
    keep = np.ones(len(pts), bool)
    thr = np.percentile(radius, 95)
    for _ in range(50):
        d, s = _curve(pts, keep)
        new = d <= thr
        if (new == keep).all() or new.sum() < 10:
            break
        keep = new
    idx = np.nonzero(keep)[0]
    ss = s[idx]
    if np.corrcoef(np.arange(len(ss)), ss)[0, 1] < 0:
        ss = -ss
    out = np.zeros(len(pts), bool)
    m = -np.inf
    for i, v in zip(idx, ss):
        if v > m:
            out[i] = True
            m = v
    return out


def fit_centerline(pts: np.ndarray):
    """Second-order polynomials of the centerline in the transverse plane and in the axial plane
    containing the vessel's main horizontal direction (Methods, Creating normal cross sections).
    Returns the main axis (0 for x, 1 for y), the two polynomials, and unit tangents at pts."""
    ax = int(np.ptp(pts[:, 1]) > np.ptp(pts[:, 0]))
    other = 1 - ax
    u = pts[:, ax]
    p_other = np.polyfit(u, pts[:, other], 2)
    p_z = np.polyfit(u, pts[:, 2], 2)
    t = np.zeros_like(pts, dtype=float)
    t[:, ax] = 1.0
    t[:, other] = np.polyval(np.polyder(p_other), u)
    t[:, 2] = np.polyval(np.polyder(p_z), u)
    t /= np.linalg.norm(t, axis=1, keepdims=True)
    order = np.argsort(u)
    return ax, p_other, p_z, t, order


# ----------------------------------------------------------------------------------------------
# Normal cross sections (claims P3, P4)
# ----------------------------------------------------------------------------------------------
def slice_frames(t: np.ndarray):
    """In-plane unit vectors for each tangent: ``ev`` is the projection of the upward direction
    (toward the brain surface, -z) on the plane, ``eh`` = ev x t, so left and right follow the
    direction along the centerline (claims P3)."""
    up = np.array([0.0, 0.0, -1.0])
    ev = up - (t @ up)[:, None] * t
    ev /= np.linalg.norm(ev, axis=1, keepdims=True)
    eh = np.cross(ev, t)
    return eh, ev


def edge_distance(c, t, shape_xyz, dz):
    """Distance in um, within the plane through ``c`` normal to ``t``, from ``c`` to the nearest
    edge of the imaging volume: for each face, the distance from c to the face along the plane is
    the distance to the face over the sine of the angle between the plane and the face's
    normal (claims P4, measured in the slice)."""
    size = np.array([(shape_xyz[0] - 1) * XY_UM, (shape_xyz[1] - 1) * XY_UM, (shape_xyz[2] - 1) * dz])
    t = np.asarray(t, float) / np.linalg.norm(t)
    out = np.inf
    for k in range(3):
        s = np.sqrt(max(1 - t[k] ** 2, 1e-12))
        out = min(out, c[k] / s, (size[k] - c[k]) / s)
    return float(out)


def cross_sections(ves, pvs, dz, centers, tangents, px, half_um=166.0):
    """Sample the masks on planes normal to the centerline (the equivalent of MATLAB
    obliqueslice), centered on each centerline point, ``px`` um per pixel (claims P1).

    Returns vessel and PVS slices (n, H, W) as bool, with rows running from top (surface side) to
    bottom, and for each slice the distance in um from the center to the nearest point outside
    the imaging volume (claims P4). Masks are interpolated linearly and thresholded at 0.5
    (standard choice). ``half_um`` covers the 332 um field of view (standard choice).
    """
    nz, ny, nx = ves.shape
    n = int(round(half_um / px))
    g = np.arange(-n, n + 1) * px
    eh, ev = slice_frames(tangents)
    vf = ves.astype(np.float32)
    pf = pvs.astype(np.float32)
    V, P, E = [], [], []
    hh, vv = np.meshgrid(g, -g)  # rows: top (+ev) first
    for c, a, b in zip(centers, eh, ev):
        xyz = c[None, None, :] + hh[..., None] * a + vv[..., None] * b
        coords = np.stack([xyz[..., 2] / dz, xyz[..., 1] / XY_UM, xyz[..., 0] / XY_UM])
        V.append(ndimage.map_coordinates(vf, coords, order=1, cval=0) > 0.5)
        P.append(ndimage.map_coordinates(pf, coords, order=1, cval=0) > 0.5)
        E.append(edge_distance(c, np.cross(a, b), (nx, ny, nz), dz))
    return np.array(V), np.array(P), np.array(E)


# ----------------------------------------------------------------------------------------------
# Per-slice measures
# ----------------------------------------------------------------------------------------------
def vessel_component(v: np.ndarray) -> np.ndarray:
    """The connected vessel region at or nearest the slice center (standard choice: the paper
    kept a single vessel region)."""
    lab, n = ndimage.label(v)
    if n == 0:
        return v
    c = np.array(v.shape) // 2
    if lab[tuple(c)] > 0:
        return lab == lab[tuple(c)]
    d, (iy, ix) = ndimage.distance_transform_edt(lab == 0, return_indices=True)
    return lab == lab[iy[tuple(c)], ix[tuple(c)]]


def pvs_lobes(pv: np.ndarray, vc: np.ndarray) -> np.ndarray:
    """The PVS of the cross section: of the PVS regions in the slice (8-connected), the two
    largest of those that come within one vessel radius, sqrt(area / pi) of the vessel region,
    of the vessel (assumption; in some files a gap of 5 to 9 um parts the lobes from the vessel).
    The paper's PVS is the space around the vessel of interest, its segmentation kept the two
    largest PVS regions ("removed ... all but the two largest regions in the PVS segmentation",
    Methods, Segmentation) and its fits are of
    the lobes beside the vessel (Figure 4); PVS pixels elsewhere in the 332 um plane (around other
    vessels, or the planes the deposited PVS mask fills below some vessels) are not this PVS."""
    lab, n = ndimage.label(pv, structure=np.ones((3, 3)))
    if n == 0 or not vc.any():
        return np.zeros_like(pv)
    gap = ndimage.distance_transform_edt(~vc)
    near = gap <= np.sqrt(vc.sum() / np.pi)
    ids = np.unique(lab[near & (lab > 0)])
    if len(ids) == 0:
        return np.zeros_like(pv)
    sizes = ndimage.sum(pv, lab, ids)
    ids = ids[np.argsort(sizes)[::-1][:2]]
    return np.isin(lab, ids)


def fit_circle(vc: np.ndarray, erosions=EROSIONS):
    """Circle fit of the vessel (Methods, Idealized geometries): edge points of the segmentation,
    excluding those inside the convex hull eroded by k pixels, for each k in ``erosions`` (claims
    P6 readings 1, 3, 5), fit by algebraic least squares (claims P6, a standard choice). Returns
    {k: (x, y, r)} in pixels, x along columns and y along rows."""
    rr, cc = np.nonzero(vc)
    r0, c0 = rr.min() - 2, cc.min() - 2
    sub = np.pad(vc, 2)[r0 + 2 : rr.max() + 5, c0 + 2 : cc.max() + 5]
    edge = sub & ~ndimage.binary_erosion(sub)
    hull = convex_hull_image(sub)
    out = {}
    for k in erosions:
        hull_e = ndimage.binary_erosion(hull, iterations=k) if k > 0 else hull
        use = edge & ~hull_e
        yy, xx = np.nonzero(use)
        if len(xx) < 10:
            yy, xx = np.nonzero(edge)
        A = np.column_stack([xx, yy, np.ones_like(xx)]).astype(float)
        bb = xx.astype(float) ** 2 + yy.astype(float) ** 2
        c = np.linalg.lstsq(A, bb, rcond=None)[0]
        x0, y0 = c[0] / 2, c[1] / 2
        out[k] = (x0 + c0, y0 + r0, float(np.sqrt(c[2] + x0 ** 2 + y0 ** 2)))
    return out


def disk(shape, x0, y0, r):
    yy, xx = np.indices(shape)
    return (xx - x0) ** 2 + (yy - y0) ** 2 <= r ** 2


def ellipse_params(p: np.ndarray):
    """Ellipse with the centroid and second central moments of the region ``p`` (Methods,
    Idealized geometries, after Tithof et al.). Returns center (x, y), semi-axes (major, minor)
    and angle, in pixels of ``p``."""
    yy, xx = np.nonzero(p)
    cx, cy = xx.mean(), yy.mean()
    cov = np.cov(np.vstack([xx - cx, yy - cy]), bias=True)
    w, vec = np.linalg.eigh(cov)
    a, b = 2 * np.sqrt(w[1]), 2 * np.sqrt(max(w[0], 0))
    ang = np.arctan2(vec[1, 1], vec[0, 1])
    return cx, cy, a, b, ang


def ellipse_region(pv: np.ndarray, vc: np.ndarray) -> np.ndarray:
    """The region the ellipse is fit to (claims P9, as amended after the question on
    fig8-ellipse-parameters): the region the PVS's outer boundary encloses, the PVS (both lobes)
    and the vessel together, holes filled, as the outer ellipse of Tithof et al.'s elliptical
    annulus. Figure 4 legend: "We fit each of these idealized shapes to the PVS and vessel
    segmentation"; Results, Characteristics of the typical PVS shape: "The major axis of the
    ellipse fit represents the distance from the PVS center and so, it includes the vessel
    radius"."""
    return ndimage.binary_fill_holes(pv | vc)


def ellipse_fit(p: np.ndarray):
    """``ellipse_params`` of ``p`` and the ellipse's mask on the grid of ``p``."""
    cx, cy, a, b, ang = ellipse_params(p)
    Y, X = np.indices(p.shape)
    u = (X - cx) * np.cos(ang) + (Y - cy) * np.sin(ang)
    v = -(X - cx) * np.sin(ang) + (Y - cy) * np.cos(ang)
    m = (u / a) ** 2 + (v / max(b, 1e-9)) ** 2 <= 1
    return cx, cy, a, b, ang, m


# Spline control points (Table 1), in units of R1: horizontal from the vessel center, vertical
# above the PVS midline. Interpolating cubic spline (claims P9, standard choice).
SPLINE_X = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
SPLINE_Y = np.array([1.1111, 0.85, 0.2667, 0.1111, 0.1111, 0.1111])
SPLINE_OF = 0.0667  # vessel center below the PVS midline, in R1 (Methods, Idealized geometries)
_SPL = CubicSpline(SPLINE_X, SPLINE_Y)


def spline_mask(shape, x0, y0, r):
    """Spline-fit PVS mirrored about both axes, minus the vessel circle; rows grow downward."""
    Y, X = np.indices(shape)
    xr = np.abs(X - x0) / r
    ymid = y0 - SPLINE_OF * r  # midline above the vessel center (rows grow downward)
    half = _SPL(np.clip(xr, 0, 5)) * r
    m = (xr <= 5) & (np.abs(Y - ymid) <= half)
    return m & ~disk(shape, x0, y0, r)


def polynomial_fit(p: np.ndarray, x0, y0, r):
    """Polynomial fit (Methods, Idealized geometries; claims P9). Heights are measured upward,
    in pixels. Per column crossing the PVS, the topmost PVS pixel is a top-edge point and the
    bottommost a bottom-edge point; the line is fit to all top-edge points, and on each side a
    second-order polynomial to the bottom-edge points of columns outside the vessel's horizontal
    extent. Each side ends at its outermost PVS column. Returns a dict of parameters (pixels) and
    the fit's mask, or None when a side has fewer than 3 columns outside the vessel."""
    cols = np.nonzero(p.any(0))[0]
    if len(cols) < 6:
        return None
    H = p.shape[0]
    top = np.array([H - 1 - np.nonzero(p[:, c])[0][0] for c in cols], float)  # height, upward
    bot = np.array([H - 1 - np.nonzero(p[:, c])[0][-1] for c in cols], float)
    yc = H - 1 - y0  # vessel center height
    line = np.polyfit(cols, top, 1)
    left = cols < x0 - r
    right = cols > x0 + r
    if left.sum() < 3 or right.sum() < 3:
        return None
    pl = np.polyfit(cols[left], bot[left], 2)
    pr = np.polyfit(cols[right], bot[right], 2)
    xL, xR = cols.min(), cols.max()
    out = {}
    for side, pp, edge, end in (("L", pl, x0 - r, xL), ("R", pr, x0 + r, xR)):
        mid = (edge + end) / 2
        h = lambda x: np.polyval(line, x) - np.polyval(pp, x)
        out["W" + side] = abs(edge - end)
        out["H1" + side] = h(edge)
        out["H2" + side] = h(mid)
        out["H3" + side] = h(end)
    out["HC"] = np.polyval(line, x0) - (yc + r)
    Y, X = np.indices(p.shape)
    hgt = H - 1 - Y
    ltop = np.polyval(line, X)
    bottom = np.where(X < x0 - r, np.polyval(pl, X), np.where(X > x0 + r, np.polyval(pr, X), yc))
    m = (X >= xL) & (X <= xR) & (hgt <= ltop) & (hgt >= bottom)
    out["mask"] = m & ~disk(p.shape, x0, y0, r)
    return out


# ----------------------------------------------------------------------------------------------
# Hydraulic resistance (claims P8; Methods, Hydraulic resistance)
# ----------------------------------------------------------------------------------------------
def poiseuille(mask: np.ndarray, px_um: float, refine: int = 1):
    """Fully developed flow through a channel of cross section ``mask``: solves the Poisson
    equation mu * lap(u) = -dP/dx with u = 0 on the boundary, by finite differences on the pixel
    grid refined ``refine`` times. This replaces the paper's finite elements (MATLAB solvepde);
    the domain is the region at least 1.5 pixels inside the mask's pixel edges, which is the
    polygon through the boundary pixel centers after the paper's one-pixel erosion.

    Returns resistance per unit length (Pa s / m^4), max and mean velocity (m/s) at 500 Pa/m.
    Separate lobes form one cross section, with their flow summed (claims P8).
    """
    if refine > 1:
        mask = np.kron(mask, np.ones((refine, refine), bool))
    h = px_um * 1e-6 / refine
    edt = ndimage.distance_transform_edt(np.pad(mask, 1))[1:-1, 1:-1]
    dom = edt > 1.5 * refine + 0.5
    n = int(dom.sum())
    if n == 0:
        return np.inf, 0.0, 0.0
    idx = -np.ones(mask.shape, dtype=np.int64)
    idx[dom] = np.arange(n)
    yy, xx = np.nonzero(dom)
    rows = [np.arange(n)]; cols = [np.arange(n)]; vals = [np.full(n, 4.0)]
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        j = idx[yy + dy, xx + dx]
        ok = j >= 0
        rows.append(np.nonzero(ok)[0]); cols.append(j[ok]); vals.append(-np.ones(ok.sum()))
    A = sparse.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                          shape=(n, n))
    u = spsolve(A.tocsc(), np.full(n, DPDX / MU * h * h))
    Q = u.sum() * h * h
    area = mask.sum() * h * h
    return DPDX / Q, float(u.max()), Q / area


def optimal_annulus(K, r1_m):
    """Optimal elliptical annulus, Equation 3 as read in the claims file: mu 6.67 K^-1.96 / R1^4."""
    return MU * 6.67 * np.asarray(K, float) ** -1.96 / np.asarray(r1_m, float) ** 4


# ----------------------------------------------------------------------------------------------
# Statistics
# ----------------------------------------------------------------------------------------------
def outlier_free(x):
    """Values not more than 1.5 IQR beyond the quartiles (Methods, Defining the distribution
    peak and excluding outliers)."""
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    q1, q3 = np.percentile(x, [25, 75])
    i = q3 - q1
    return x[(x >= q1 - 1.5 * i) & (x <= q3 + 1.5 * i)]


def peak(x, reading: str = "a", log: bool = False):
    """Distribution peak: center of the bin of largest density among 20 evenly spaced bins
    (Methods). Reading "a" bins min to max of all values, "b" the values left after removing
    outliers (claims P7). ``log`` bins evenly in log10 (claims, fig6b reading b)."""
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    if log:
        if reading == "b":
            x = outlier_free(x)
        x = x[x > 0]
        lx = np.log10(x)
        cnt, e = np.histogram(lx, bins=20)
        k = int(np.argmax(cnt))
        return float(10 ** ((e[k] + e[k + 1]) / 2))
    if reading == "b":
        x = outlier_free(x)
    cnt, e = np.histogram(x, bins=20)
    k = int(np.argmax(cnt))
    return float((e[k] + e[k + 1]) / 2)


# ----------------------------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------------------------
def measure_slice(v, p, px, erosions=EROSIONS, resist=True, resist_erosions=(3,)):
    """All per-slice measures for one cross section. Pixels in both masks are counted as vessel
    (assumption: the paper resolved overlaps by hand, case by case, and the deposited masks still
    overlap). Lengths in um, areas in um^2, resistance in Pa s/m^4. The slice is cropped to a
    window holding the vessel, the PVS and every fit (standard choice, for speed). The PVS is
    the lobes beside the vessel (``pvs_lobes``); ``pvs_area_all`` is all PVS pixels in the slice.
    ``cx``, ``cy`` are the vessel center in slice pixels (circle fit, erosion 3; the vessel
    region's centroid when there is no fit), to which the paper shifts the slice."""
    vc = vessel_component(v)
    pall = p & ~v
    pv = pvs_lobes(pall, vc)
    row = {"ves_area": vc.sum() * px * px, "pvs_area": pv.sum() * px * px,
           "pvs_area_all": pall.sum() * px * px, "overlap_area": (p & v).sum() * px * px,
           "pvs_regions": int(ndimage.label(pall, structure=np.ones((3, 3)))[1])}
    cols = np.nonzero(pv.any(0))[0]
    row["pvs_hext"] = (cols.max() - cols.min() + 1) * px if len(cols) else 0.0
    cols = np.nonzero(pall.any(0))[0]
    row["pvs_hext_all"] = (cols.max() - cols.min() + 1) * px if len(cols) else 0.0
    if vc.any():
        rr, cc = np.nonzero(vc)
        row["ves_h"], row["ves_w"] = (np.ptp(rr) + 1) * px, (np.ptp(cc) + 1) * px
        row["cx"], row["cy"] = cc.mean(), rr.mean()
    if vc.sum() < 20 or pv.sum() < 20:
        if resist and pv.sum() > 0:
            row["R_seg"], row["umax_seg"], row["umean_seg"] = poiseuille(pv, px)
        return row
    circ = fit_circle(vc, erosions)
    x3, y3, r3 = circ[3] if 3 in circ else next(iter(circ.values()))
    row["cx"], row["cy"] = x3, y3
    near = disk(pv.shape, x3, y3, 3 * r3)
    row["pvs_near_share"] = (pv & near).sum() / pv.sum()
    row["pvs_all_near_share"] = (pall & near).sum() / pall.sum()
    # window: vessel, PVS, the ellipse and the spline extent of every circle fit
    rr, cc = np.nonzero(vc | pv)
    r0, r1, c0, c1 = rr.min(), rr.max(), cc.min(), cc.max()
    sub = ellipse_region(pv[r0 : r1 + 1, c0 : c1 + 1], vc[r0 : r1 + 1, c0 : c1 + 1])
    ex, ey, a, b, ang = ellipse_params(sub)
    ex, ey = ex + c0, ey + r0
    hx = np.hypot(a * np.cos(ang), b * np.sin(ang))  # half extents of the ellipse
    hy = np.hypot(a * np.sin(ang), b * np.cos(ang))
    r0, r1, c0, c1 = min(r0, ey - hy), max(r1, ey + hy), min(c0, ex - hx), max(c1, ex + hx)
    for x0, y0, r in circ.values():
        r0, r1 = min(r0, y0 - 1.4 * r), max(r1, y0 + 1.4 * r)
        c0, c1 = min(c0, x0 - 5.2 * r), max(c1, x0 + 5.2 * r)
    H, W = v.shape
    r0, c0 = max(int(r0) - 4, 0), max(int(c0) - 4, 0)
    r1, c1 = min(int(r1) + 5, H), min(int(c1) + 5, W)
    vc, pv = vc[r0:r1, c0:c1], pv[r0:r1, c0:c1]
    if resist:
        row["R_seg"], row["umax_seg"], row["umean_seg"] = poiseuille(pv, px)
    ex, ey = ex - c0, ey - r0
    Y, X = np.indices(pv.shape)
    u = (X - ex) * np.cos(ang) + (Y - ey) * np.sin(ang)
    w = -(X - ex) * np.sin(ang) + (Y - ey) * np.cos(ang)
    em = (u / a) ** 2 + (w / max(b, 1e-9)) ** 2 <= 1
    # variant, not used by any criterion since the answer on fig8: the ellipse of the PVS alone
    _, _, ap, bp, _ = ellipse_params(pv)
    row["R2p"], row["R3p"] = ap * px, bp * px
    for k in erosions:
        x0, y0, r = circ[k]
        x0, y0 = x0 - c0, y0 - r0
        c = disk(pv.shape, x0, y0, r)
        s = f"_e{k}"
        row["R1" + s] = r * px
        row["R2" + s] = a * px
        row["R3" + s] = b * px
        row["Oh" + s] = (x0 - ex) * px
        row["Ov" + s] = (y0 - ey) * px  # rows grow downward: positive when vessel below center
        ell = em & ~c
        row["ell_area_a" + s] = ell.sum() * px * px
        row["ell_area_b" + s] = (np.pi * a * b - np.pi * r * r) * px * px
        sp = spline_mask(pv.shape, x0, y0, r)
        row["spl_area" + s] = sp.sum() * px * px
        pf = polynomial_fit(pv, x0, y0, r)
        if pf is not None:
            for key in ("WL", "WR", "H1L", "H1R", "H2L", "H2R", "H3L", "H3R", "HC"):
                row[f"{key}{s}"] = pf[key] * px
            row["pol_area" + s] = pf["mask"].sum() * px * px
        if resist and k in resist_erosions:
            for name, m in (("ell", ell), ("spl", sp), ("pol", None if pf is None else pf["mask"])):
                if m is None or m.sum() == 0:
                    continue
                R, umax, umean = poiseuille(m, px)
                row[f"R_{name}{s}"] = R
                row[f"umax_{name}{s}"] = umax
                row[f"umean_{name}{s}"] = umean
    return row


RESIST_EROSIONS = EROSIONS  # resistance of the fits is solved for every reading of P6


def fit_masks(v, p, k=3):
    """For a figure: the vessel region, the PVS lobes, the circle (x, y, r) of erosion ``k`` and
    the ellipse, spline and polynomial fits of one slice, as masks on the slice's grid."""
    vc = vessel_component(v)
    pv = pvs_lobes(p & ~v, vc)
    out = {"vessel": vc, "pvs": pv}
    if vc.sum() < 20 or pv.sum() < 20:
        return out
    x0, y0, r = fit_circle(vc, (k,))[k]
    c = disk(v.shape, x0, y0, r)
    out["circle"] = (x0, y0, r)
    out["ellipse"] = ellipse_fit(ellipse_region(pv, vc))[-1] & ~c
    out["spline"] = spline_mask(v.shape, x0, y0, r)
    pf = polynomial_fit(pv, x0, y0, r)
    if pf is not None:
        out["polynomial"] = pf["mask"]
    return out


def exclusion(df):
    """Claims P4: keep a cross section when the distance from the vessel center to the edge of
    the imaging plane is at least the segment's median PVS width over 2.5. Reading "a" takes the
    width as the horizontal extent of the PVS in each slice, reading "b" as the polynomial-fit
    width W, both sides pooled (erosion 3 for the circle fit)."""
    med_a = np.median(df["pvs_hext"])
    w = np.r_[df.get("WL_e3", pd_nan(df)), df.get("WR_e3", pd_nan(df))]
    med_b = np.nanmedian(w) if np.isfinite(w).any() else np.nan
    return df["edge_dist"] >= med_a / 2.5, df["edge_dist"] >= med_b / 2.5, med_a, med_b


def pd_nan(df):
    return np.full(len(df), np.nan)


def process_segment(f, target, reading="a", resist=True):
    """Cross sections of one file under P1 = ``target`` (um) and P2 reading "a", one slice per
    centerline point in path order. First pass: every measure but resistance, for all slices;
    second pass: resistance and velocity for the slices kept under either reading of P4."""
    import pandas as pd

    import hashlib

    ves, pvs = load_masks(f)
    dz = voxel_size(f)[2]
    digest = hashlib.sha1(np.packbits(ves).tobytes() + np.packbits(pvs).tobytes()).hexdigest()
    pvs = clear_filled_planes(pvs)
    info = {}
    pts = centerline(ves, dz, target, reading, info)
    ax, p_other, p_z, t, order = fit_centerline(pts)
    step = np.linalg.norm(np.diff(pts, axis=0), axis=1)
    adjacent = step <= np.sqrt(3) * target * 1.01  # steps across a removed stretch are gaps
    V, P, E = cross_sections(ves, pvs, dz, pts, t, target)
    shape_xyz = (ves.shape[2], ves.shape[1], ves.shape[0])
    mips = (ves.any(0), pvs.any(0))
    del ves, pvs
    eh, ev = slice_frames(t)
    n = int(round(166.0 / target))
    rows = []
    for i in range(len(pts)):
        r = measure_slice(V[i], P[i], target, resist=False)
        r["edge_dist_skel"] = E[i]
        # the paper shifts the slice so the vessel center is at the image center (Methods,
        # Creating normal cross sections); the edge distance is measured from that center
        if "cx" in r:
            c = pts[i] + (r["cx"] - n) * target * eh[i] - (r["cy"] - n) * target * ev[i]
            r["edge_dist"] = edge_distance(c, t[i], shape_xyz, dz)
        else:
            r["edge_dist"] = E[i]
        r["i"] = i
        rows.append(r)
    df = pd.DataFrame(rows)
    keep_a, keep_b, med_a, med_b = exclusion(df)
    df["keep_a"], df["keep_b"] = keep_a.values, keep_b.values
    if resist:
        extra = {}
        for i in np.nonzero((keep_a | keep_b).values)[0]:
            r = measure_slice(V[i], P[i], target, erosions=RESIST_EROSIONS, resist=True,
                              resist_erosions=RESIST_EROSIONS)
            extra[i] = {k: v for k, v in r.items() if k.startswith(("R_", "umax", "umean"))}
        ext = pd.DataFrame.from_dict(extra, orient="index")
        df = df.join(ext)
    kept = np.nonzero(df.keep_b.values)[0]
    ex = int(kept[np.argmin(np.abs(kept - len(pts) / 2))]) if len(kept) else len(pts) // 2
    df.attrs.update(spacing=float(step[adjacent].mean()), spacing_all=float(step.mean()),
                    gaps=int((~adjacent).sum()), med_a=float(med_a), med_b=float(med_b),
                    digest=digest, **{k: v for k, v in info.items() if k != "_path"})
    df.attrs["example"] = {"i": ex, "v": V[ex], "p": P[ex], "path": info["_path"][0],
                           "keep": info["_path"][1], "mip_vessel": mips[0], "mip_pvs": mips[1]}
    return df


def run_asset(args):
    """Worker: all cross sections of one asset under P1 = target, P2 reading "a"."""
    asset, target = args
    f = open_asset(asset)
    df = process_segment(f, target, "a")
    df.insert(0, "location", location_of(f))
    df.insert(1, "target", target)
    return df


def run_all(assets, target, workers=4):
    import os
    import pandas as pd
    from concurrent.futures import ProcessPoolExecutor

    os.environ.setdefault("OMP_NUM_THREADS", "1")
    with ProcessPoolExecutor(workers) as ex:
        dfs = list(ex.map(run_asset, [(a, target) for a in assets]))
    meta = pd.DataFrame([{"location": d["location"].iloc[0], "points": len(d),
                          **{k: v for k, v in d.attrs.items() if k != "example"}}
                         for d in dfs]).set_index("location")
    examples = {d["location"].iloc[0]: d.attrs["example"] for d in dfs}
    for d in dfs:
        d.attrs = {}
    out = pd.concat(dfs, ignore_index=True)
    meta.attrs["examples"] = examples
    return out, meta


def count_all_points(args):
    """Worker for P2 reading "b" (all skeleton points). Slicing at every one of the 10^4 to 10^5
    points is not feasible here, so the median PVS widths of P4 are estimated from 150 evenly
    spaced points (standard choice: a median of 150 values), and the edge distance, which needs no
    slice, is computed at every point."""
    asset, target = args
    f = open_asset(asset)
    ves, pvs = load_masks(f)
    pvs = clear_filled_planes(pvs)
    dz = voxel_size(f)[2]
    pts = centerline(ves, dz, target, "b")
    ax, p_other, p_z, t, order = fit_centerline(pts)
    pts, t = pts[order], t[order]
    nz, ny, nx = ves.shape
    E = np.array([edge_distance(c, tt, (nx, ny, nz), dz) for c, tt in zip(pts, t)])
    sel = np.linspace(0, len(pts) - 1, min(150, len(pts))).astype(int)
    V, P, _ = cross_sections(ves, pvs, dz, pts[sel], t[sel], target)
    hext, wpol = [], []
    for v, p in zip(V, P):
        vc = vessel_component(v)
        pv = pvs_lobes(p & ~v, vc)
        cols = np.nonzero(pv.any(0))[0]
        hext.append((cols.max() - cols.min() + 1) * target if len(cols) else 0.0)
        if vc.sum() >= 20 and pv.sum() >= 20:
            x0, y0, r = fit_circle(vc, (3,))[3]
            pf = polynomial_fit(pv, x0, y0, r)
            if pf is not None:
                wpol += [pf["WL"] * target, pf["WR"] * target]
    step = np.linalg.norm(np.diff(pts, axis=0), axis=1)
    return {
        "location": location_of(f), "n_points": len(pts), "edge_dist": E,
        "med_hext": float(np.median(hext)), "med_wpol": float(np.median(wpol)) if wpol else np.nan,
        "spacing": float(step.mean()),
    }


def run_counts_b(assets, target, workers=4):
    from concurrent.futures import ProcessPoolExecutor

    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(count_all_points, [(a, target) for a in assets]))
