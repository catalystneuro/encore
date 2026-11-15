"""Loading and measures for CRCNS pvc-12 (Martinez-Conde et al. 2019, PLoS ONE 14(3) e0210941).

Dataset: crcns:pvc-12/unversioned (doi:10.6080/K05D8Q1T).

The data set is one zip, ``pvc-12/live/V1_Vasarely_data.zip``, read in place from the public
S3 bucket over range requests (docs/archives.md, "CRCNS"). It holds, per neuron and
experiment (folders ``Corners``, ``Star``, ``Edge-compare``), a ``<code>_SpikeRateMap.mat``
and a ``<code>_Stimulus.mat``, and a spreadsheet listing the neurons.

What the files hold, as checked in the notebook (the data descriptor differs in places):

- ``dat.image``: the unsmoothed spike rate map on the 480 x 640 DU screen, in spikes per ms
  (spike count divided by eye time in ms; the one file with an ``eyetime`` field shows that
  ``image * eyetime`` is integer). The descriptor calls it raw spike counts.
- ``dat.smoothed_image``: ``image`` smoothed with a Gaussian, in spikes per ms. These screen
  maps are in gaze coordinates, offset from the stimulus by the receptive field eccentricity.
- ``dat.Standard``: the same maps registered to the stimulus and rotated so that the aligned
  fold is vertical (the ROI frame of the paper's Fig 5), with the stimulus polygons in that
  frame. Present for every Edge-compare and Corners neuron and for 12 of the Star neurons.
- ``Standard.BaseActivity``: a baseline for some neurons, of undocumented origin.

Parameters and where they come from:

- Spike rate map: ``Standard.smoothed_image`` x 1000 (spikes/s); the paper's map is the rate
  smoothed after dividing by eye time (Fig 3B legend). ``Standard.image`` is the unsmoothed
  variant named in the claim fig4b-spike-rate-difference.
- Midpoint response: mean in an 8 x 8 DU square at the fold's 50% luminance point (Results,
  "Strength of neuronal responses...", paragraph 1). All squares and blocks weight each pixel by
  the fraction of its area inside (``rect_weights``), so that they cover the paper's sizes
  wherever their centres fall; pixel centres strictly inside is a variant. Two symmetric midpoints are averaged for
  the Square and the Star (Methods, Corners, paragraph 2).
- Blocks along a fold: ten non-overlapping blocks from 0% to 100% luminance, 8 DU wide and
  15, 15, 7, 15 and 10 DU long for Edge, P180, S90, S52 and S40 (Results, "Responses averaged
  along the entire fold", paragraph 1). For S90 the block length is taken as the half diagonal
  over ten (7.07 DU) so the ten blocks span the fold; the paper rounds it to 7 (standard choice
  that cannot change a result by more than the pixel grid).
- P180: the line 48 DU from the Edge inside the rectangle (Methods, Square and edge).
- Baselines: four 16 x 16 DU squares at the corners of the 138 x 138 DU square around the
  Square (Square and Edge) and of the square circumscribing the Star (Methods, Square and edge;
  Star), and two 16 x 16 DU squares "in 0% luminance areas within the ROI" for Corners (Methods,
  Corners), placed in the paper only in Fig 2C. The placement is open (squares centred on the
  box corners or inside them; for Corners, readings (a) to (c) of ``corners_baselines``). The
  main reading for each stimulus is the placement whose values are closest, neuron by neuron,
  to the files' own ``Standard.BaseActivity`` (the authors' baseline, of undocumented
  placement, present for 38 neurons): centred on the corners for Square and Edge, inside the
  corners for the Star, and the ROI corners on the 0% side for Corners (assumption; every
  reading is shown in the notebook). Pixels where the smoothed map is zero are kept, as the
  files' BaseActivity agrees better with baselines that keep them (checked in the notebook);
  leaving them out is a variant.
- Bright S40 fold: of the two 40 degree apices of the Corners pattern, the one pointing toward
  lower luminance, as the bright folds of the nested squares point toward the dark surround
  (Fig 1A legend); found per neuron from the stimulus image.
"""
from __future__ import annotations

import hashlib
import io
import re
import zipfile

import fsspec
import h5py
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy import ndimage

URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/V1_Vasarely_data.zip"
CHECKSUMS = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/checksums.md5"
COND = {"Edge-compare": "Square and Edge", "Star": "Star", "Corners": "Corners"}
STIM_KEY = {"Edge-compare": "EdgecompImage", "Star": "DiagImage", "Corners": "CornersImage"}


def open_zip():
    f = fsspec.open(URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def cell_of(code: str) -> str:
    """Neuron code from a file code: drop the 3-letter experiment prefix and a trailing run letter."""
    c = code[3:]
    if c[-1].isalpha() and c[-2].isdigit():
        c = c[:-1]
    return c


def monkey_of(cell: str) -> str:
    return re.search(r"[A-Z]", cell).group(0)


def _arr(x):
    if isinstance(x, np.ndarray) and x.dtype == object and x.shape == ():
        x = x.item()
    return x.toarray() if hasattr(x, "toarray") else np.asarray(x, dtype=float)


def _load_mat(z, name):
    raw = z.read("V1_Vasarely_data/" + name)
    if b"MATLAB 7.3" in raw[:20]:
        return h5py.File(io.BytesIO(raw), "r")
    return sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)["dat"]


def _verts(V):
    return [np.c_[np.atleast_1d(p.x), np.atleast_1d(p.y)].astype(float) for p in V]


def read_sheet(z):
    x = pd.read_excel(io.BytesIO(z.read("V1_Vasarely_data/V1_Vasarely_data_SMC.xlsx")), header=None)
    hdr = x.index[x.eq("Cell").any(axis=1)][0]
    t = x.iloc[hdr + 1:, 2:6]
    t.columns = ["cell", "Corners", "Star", "Edge-compare"]
    t = t.dropna(subset=["cell"]).copy()
    t["cell"] = t["cell"].astype(str).str.strip()
    for c in ["Corners", "Star", "Edge-compare"]:
        t[c] = t[c].astype(str).str.strip().eq("X")
    return t.reset_index(drop=True)


def load_all(z):
    """Read every map and stimulus, keeping only what the analysis uses.

    Returns a list of dicts, one per file pair, with the screen-level summaries and, where the
    file has one, the Standard (ROI frame) maps in spikes/s, the ROI-frame polygons, and the
    stimulus image warped into the ROI frame.
    """
    recs = []
    names = sorted(n for n in z.namelist() if n.endswith("_SpikeRateMap.mat"))
    for n in names:
        folder, fname = n.split("/")[1:]
        code = fname.split("_")[0]
        r = dict(folder=folder, code=code, cell=cell_of(code), monkey=monkey_of(cell_of(code)))
        m = _load_mat(z, f"{folder}/{code}_SpikeRateMap.mat")
        s = _load_mat(z, f"{folder}/{code}_Stimulus.mat")
        if isinstance(s, h5py.File):
            r["stim_type"] = "".join(map(chr, s["dat/type"][()].ravel()))
            r["has_standard"] = False
            r["fields"] = sorted(m["dat"].keys()) if isinstance(m, h5py.File) else list(m._fieldnames)
            recs.append(r)
            continue
        r["stim_type"] = STIM_KEY[folder]
        r["fields"] = list(m._fieldnames)
        img = _arr(m.image)
        r["screen_rate_max"] = img.max()
        r["screen_rate_nonint"] = not np.allclose(img, np.round(img))
        if "eyetime" in m._fieldnames:
            et = _arr(m.eyetime)
            r["eyetime_ms_total"] = et.sum()
            r["spike_count_from_eyetime"] = float((img * et).sum())
            r["count_integer_err"] = float(np.abs(img * et - np.round(img * et)).max())
        stim = np.asarray(getattr(s, STIM_KEY[folder]), float)
        r["stim_range"] = (stim.min(), stim.max())
        r["stim_hash"] = hashlib.md5(np.round(stim, 6).tobytes()).hexdigest()[:10]
        if folder == "Star":
            # screen position and orientation of the Star: its centre, and the angle of its outer
            # vertices modulo 30 degrees (the twelve-pointed star repeats every 30 degrees)
            V0 = _verts(s.DiagVert)
            c0 = V0[-1].mean(0)
            rad = np.linalg.norm(V0[0] - c0, axis=1)
            out = V0[0][rad > rad.max() - 1]
            r["star_centre"] = c0
            r["star_angle30"] = float(np.median(np.degrees(np.arctan2(out[:, 1] - c0[1], out[:, 0] - c0[0])) % 30))
        # what each top-level field holds (shape and range), and the screen map's summaries
        r["field_summary"] = {f: _summ(getattr(m, f)) for f in m._fieldnames if f != "Standard"}
        sm_screen = np.asarray(m.smoothed_image, float) * 1000.0
        r["screen_peak"] = float(sm_screen.max())
        r["screen_mean_nz"] = float(sm_screen[sm_screen > 0].mean())
        r["screen_frac_nz"] = float((sm_screen > 0).mean())
        r["has_standard"] = "Standard" in m._fieldnames
        if r["has_standard"]:
            st = m.Standard
            r["S"] = np.asarray(st.smoothed_image, float) * 1000.0
            r["I"] = _arr(st.image) * 1000.0
            r["base_file"] = float(st.BaseActivity) * 1000.0 if "BaseActivity" in st._fieldnames else np.nan
            if "smoothed_image_norm" in st._fieldnames and "BaseActivity" in st._fieldnames:
                # is Standard.smoothed_image_norm the map minus BaseActivity, or that divided by its maximum?
                sin_, S0, b0 = np.asarray(st.smoothed_image_norm, float), r["S"] / 1000.0, float(st.BaseActivity)
                r["sin_err_diff"] = float(np.abs(sin_ - (S0 - b0)).max())
                r["sin_err_scaled"] = float(np.abs(sin_ - (S0 - b0) / (S0.max() - b0)).max())
            vk = [k for k in st._fieldnames if k.endswith("Vert")][0]
            V = getattr(st, vk)
            if folder == "Edge-compare":
                r["vert"] = {"square": _verts(V.SquareVert), "rect": _verts(V.RectVert)}
                scr = {"square": _verts(s.SquareVert), "rect": _verts(s.RectVert)}
            else:
                r["vert"] = {"poly": _verts(V)}
                scr = {"poly": _verts(getattr(s, vk))}
            # Screen -> ROI transform from the polygons (exact for Edge and Corners, whose vertex
            # order is the same in both frames). Star polygons are numbered differently in the two
            # frames, so for the Star the ROI geometry is taken from the ROI-frame polygons alone.
            if folder != "Star":
                A = np.vstack([np.vstack(scr[k][::7]) for k in scr])
                B = np.vstack([np.vstack(r["vert"][k][::7]) for k in r["vert"]])
                X = np.c_[A, np.ones(len(A))]
                sol = np.linalg.lstsq(X, B, rcond=None)[0]
                r["xf_err"] = float(np.abs(X @ sol - B).max())
                r["xf_angle"] = float(np.degrees(np.arctan2(sol[0, 1], sol[0, 0])))
                H, W = r["S"].shape
                yy, xx = np.mgrid[0:H, 0:W]
                P = (np.c_[xx.ravel(), yy.ravel()] - sol[2]) @ np.linalg.inv(sol[:2])
                r["stim_roi"] = ndimage.map_coordinates(stim, [P[:, 1], P[:, 0]], order=1, cval=0.0).reshape(H, W)
                # Check that the Standard map is the screen map shifted by one offset: search the
                # offset that best matches, on a subsample, and keep the correlation.
                sm = np.asarray(m.smoothed_image, float)
                r["reg_corr"], r["reg_offset"] = _register(sm, r["S"] / 1000.0, np.linalg.inv(sol[:2]), sol[2])
                if "eyetime" in m._fieldnames:
                    # the eye time and unsmoothed maps moved into the ROI frame as the Standard map is
                    r["eyetime_roi"] = _to_roi(_arr(m.eyetime), np.linalg.inv(sol[:2]), sol[2], r["reg_offset"], (H, W))
                    r["image_roi"] = _to_roi(img, np.linalg.inv(sol[:2]), sol[2], r["reg_offset"], (H, W))
            else:
                # Star: the stimulus is drawn at one orientation on the screen for every neuron;
                # the ROI frame turns the aligned diagonal vertical. Find the rotation (one of the
                # twelve that bring an outer vertex to the vertical) and translation that match.
                sm = np.asarray(m.smoothed_image, float)
                cs = scr["poly"][99].mean(0)
                cr = r["vert"]["poly"][99].mean(0)
                best = (-2.0, None, None)
                for th in range(-165, 181, 30):
                    t = np.radians(th)
                    Rm = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
                    # ROI p -> screen: cs + Rm (p - cr), written as (p - tt) @ A_inv
                    A_inv = Rm.T
                    tt = cr - cs @ Rm
                    c, off = _register(sm, r["S"] / 1000.0, A_inv, tt)
                    if c > best[0]:
                        best = (c, off, th)
                r["reg_corr"], r["reg_offset"], r["star_rotation"] = best
                # the Star stimulus in the ROI frame, by the rotation found (no offset: the offset
                # is that of the gaze map from the stimulus)
                t = np.radians(best[2])
                Rm = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
                r["stim_roi"] = _to_roi(stim, Rm.T, cr - cs @ Rm, (0, 0), r["S"].shape, order=1)
        recs.append(r)
    return recs


def _summ(x):
    try:
        a = _arr(x)
    except (TypeError, ValueError):
        return (type(x).__name__,)
    return (a.shape, float(np.nanmin(a)), float(np.nanmax(a))) if a.size else (a.shape,)


def _to_roi(screen, A_inv, t, off, shape, order=0):
    """A screen-frame array moved into the ROI frame: ROI pixel (col, row) is the screen point
    ((col, row) + off - t) @ A_inv, as in ``_register``."""
    H, W = shape
    yy, xx = np.mgrid[0:H, 0:W]
    P = (np.c_[xx.ravel() + off[0], yy.ravel() + off[1]] - t) @ A_inv
    return ndimage.map_coordinates(screen, [P[:, 1], P[:, 0]], order=order, cval=0.0).reshape(H, W)


def _register(sm, S, A_inv, t):
    """Correlation between the Standard map and the screen map warped into the ROI frame at the
    best single translation (found by FFT cross-correlation), and that translation in DU."""
    from scipy.signal import fftconvolve
    H, W = S.shape
    pad = 400
    yy, xx = np.mgrid[-pad:H + pad, -pad:W + pad]
    P = (np.c_[xx.ravel(), yy.ravel()] - t) @ A_inv
    canvas = ndimage.map_coordinates(sm, [P[:, 1], P[:, 0]], order=1, cval=0.0).reshape(yy.shape)
    k = (S - S.mean())[::-1, ::-1]
    cc = fftconvolve(canvas, k, mode="valid")
    iy, ix = np.unravel_index(np.argmax(cc), cc.shape)
    win = canvas[iy:iy + H, ix:ix + W]
    c = float(np.corrcoef(win.ravel(), S.ravel())[0, 1])
    return c, (int(ix - pad), int(iy - pad))


# ---------------------------------------------------------------------------------------------
# Geometry in the ROI frame. Points are (x, y) = (column, row) of the Standard arrays.

SS = 4  # subpixels per DU side for the area-weighted squares


def rect_weights(shape, centre, u, half_along, half_across, ss=SS):
    """Pixels of a rectangle centred on ``centre``, with sides along ``u`` and across it, each
    pixel weighted by the fraction of its area inside (estimated on ss x ss subpixels), so that an
    8 x 8 DU square covers 64 DU2 wherever its centre lies. With ss=None, pixels whose centres lie
    strictly inside get weight 1 (at an integer centre an "8 x 8" square then holds 7 x 7 pixels;
    the variant of the first verification round). Returns the slices of the bounding box and the
    weights; parts outside the frame are dropped."""
    H, W = shape
    u = np.asarray(u, float) / np.linalg.norm(u)
    n = np.array([-u[1], u[0]])
    R = np.hypot(half_along, half_across) + 1
    x0, x1 = max(int(np.floor(centre[0] - R)), 0), min(int(np.ceil(centre[0] + R)) + 1, W)
    y0, y1 = max(int(np.floor(centre[1] - R)), 0), min(int(np.ceil(centre[1] + R)) + 1, H)
    if x0 >= x1 or y0 >= y1:
        return (slice(0, 0), slice(0, 0)), np.zeros((0, 0))
    k = 1 if ss is None else ss
    off = np.zeros(1) if ss is None else (np.arange(ss) + 0.5) / ss - 0.5
    xs = (np.arange(x0, x1)[:, None] + off[None, :]).ravel()
    ys = (np.arange(y0, y1)[:, None] + off[None, :]).ravel()
    X, Y = np.meshgrid(xs - centre[0], ys - centre[1])
    inside = (np.abs(X * u[0] + Y * u[1]) < half_along) & (np.abs(X * n[0] + Y * n[1]) < half_across)
    w = inside.reshape(y1 - y0, k, x1 - x0, k).mean(axis=(1, 3))
    return (slice(y0, y1), slice(x0, x1)), w


def region_mean(M, wm):
    sl, w = wm
    return float((M[sl] * w).sum() / w.sum()) if w.sum() > 0 else np.nan


def _cross2(a, b):
    return a[0] * b[1] - a[1] * b[0]


def fold_geometry(r):
    """Folds of one neuron in its ROI frame: for each fold a list of halves, each with the 0%
    point, the 100% point and the 50% midpoint; and the baseline square centres."""
    g = {}
    if r["folder"] == "Edge-compare":
        sq0 = r["vert"]["square"][0]
        C = r["vert"]["square"][99].mean(0)
        R0 = r["vert"]["rect"][0]
        # Edge: side of the rectangle collinear with the Square's aligned diagonal; its 0% end is
        # the corner nearest the Square (polygons shrink toward the 100% end).
        e0 = R0[np.argmin(np.linalg.norm(R0 - C, axis=1))]
        others = [p for p in R0 if np.linalg.norm(p - e0) > 1]
        d = (e0 - C) / np.linalg.norm(e0 - C)
        e1 = min(others, key=lambda p: abs(_cross2(d, (p - e0) / np.linalg.norm(p - e0))))
        far = max(others, key=lambda p: np.linalg.norm(p - e0))
        u = (e1 - e0) / np.linalg.norm(e1 - e0)
        nvec = far - e1
        nvec = nvec / np.linalg.norm(nvec)
        g["Edge"] = [dict(p0=e0, p100=e1)]
        g["P180"] = [dict(p0=e0 + 48 * nvec, p100=e1 + 48 * nvec)]
        diag = [v for v in sq0 if abs(_cross2(d, (v - C) / np.linalg.norm(v - C))) < 1e-3]
        g["S90"] = [dict(p0=v, p100=C) for v in diag]
        # baseline: 16 x 16 squares inside the corners of the 138 x 138 square around the Square,
        # axes along the aligned diagonal and across it
        nd = np.array([-d[1], d[0]])
        g["baseline"] = [C + sa * 61 * d + sb * 61 * nd for sa in (-1, 1) for sb in (-1, 1)]
        g["baseline_axis"] = d
    elif r["folder"] == "Star":
        P0 = r["vert"]["poly"][0]
        C = r["vert"]["poly"][99].mean(0)
        rad = np.linalg.norm(P0 - C, axis=1)
        outer = P0[rad > rad.max() - 1]
        ang = np.degrees(np.arctan2(outer[:, 1] - C[1], outer[:, 0] - C[0]))
        # aligned diagonal: the outer vertices on the vertical axis of the ROI frame
        al = outer[np.minimum(np.abs(ang - 90), np.abs(ang + 90)) < 1]
        g["S52"] = [dict(p0=v, p100=C) for v in al]
        half = rad.max()
        g["baseline"] = [C + np.array([sa, sb]) * (half - 8) for sa in (-1, 1) for sb in (-1, 1)]
        g["baseline_axis"] = np.array([0.0, 1.0])
    else:
        polys = r["vert"]["poly"]
        p0, p99 = polys[0], polys[99]
        # apices: vertices that are local extremes across the luminance gradient (the triangle tips)
        shift = (p99 - p0).mean(0)
        sdir = shift / np.linalg.norm(shift)
        cands = []
        for i in range(1, len(p0) - 1):
            a, b, c = p0[i - 1], p0[i], p0[i + 1]
            if np.linalg.norm(b - a) < 1e-6 or np.linalg.norm(c - b) < 1e-6:
                continue
            v1, v2 = a - b, c - b
            ang = np.degrees(np.arccos(np.dot(v1, v2) / np.linalg.norm(v1) / np.linalg.norm(v2)))
            if 30 < ang < 50 and np.all(np.abs(b) < 2000):
                cands.append(i)
        H, W = r["S"].shape
        res = []
        for i in cands:
            tip0 = polys[0][i]
            tip99 = polys[99][i]
            base_mid = (p0[i - 1] + p0[i + 1]) / 2
            point = (tip0 - base_mid) / np.linalg.norm(tip0 - base_mid)
            # luminance along the fold, 20 DU either side of the 50% tip
            t50 = polys[50][i]
            lum = lambda p: ndimage.map_coordinates(r["stim_roi"], [[p[1]], [p[0]]], order=1)[0]
            ahead, behind = lum(t50 + 20 * point), lum(t50 - 20 * point)
            res.append(dict(i=i, tip0=tip0, tip99=tip99, point=point, bright=ahead < behind,
                            lum_ahead=ahead, lum_behind=behind))
        br = [x for x in res if x["bright"]]
        dk = [x for x in res if not x["bright"]]
        lum0 = lambda p: ndimage.map_coordinates(r["stim_roi"], [[p[1]], [p[0]]], order=1)[0]
        for name, lst in (("S40", br), ("S40dark", dk)):
            if len(lst) == 1:
                x = lst[0]
                # 0% end of the fold: the tip whose surroundings are darker
                a, b = x["tip0"], x["tip99"]
                p0_, p100_ = (a, b) if lum0(a) < lum0(b) else (b, a)
                g[name] = [dict(p0=p0_, p100=p100_)]
        g["corners_apices"] = res
    return g


def corners_baselines(shape, g):
    """Readings of the two Corners baseline squares (centres), all in the 0% area of the ROI."""
    H, W = shape
    f = g["S40"][0]
    xb = f["p0"][0]
    y0 = f["p0"][1]
    up = np.sign(f["p0"][1] - f["p100"][1])  # direction from 100% to 0% along the fold
    out = {}
    # (a) the two corners of the ROI on the 0% side
    yc = (H - 8.5) if up > 0 else 7.5
    out["a_roi_corners"] = [np.array([7.5, yc]), np.array([W - 8.5, yc])]
    # (b) beside the 0% end of the bright fold, 24 DU either side of it, 16 DU past the 0% point
    out["b_beside_fold"] = [np.array([xb - 24, y0 + up * 16]), np.array([xb + 24, y0 + up * 16])]
    # (c) on the ROI's 0% edge, halfway between the fold and each side of the ROI
    out["c_roi_edge_mid"] = [np.array([xb / 2, yc]), np.array([(xb + W) / 2, yc])]
    return out


def baseline(M, centres, axis, ss=SS):
    return float(np.mean([region_mean(M, rect_weights(M.shape, c, axis, 8, 8, ss)) for c in centres]))


def midpoint(M, halves, axis_len=8, ss=SS):
    vals = []
    for h in halves:
        mid = (h["p0"] + h["p100"]) / 2
        u = h["p100"] - h["p0"]
        vals.append(region_mean(M, rect_weights(M.shape, mid, u, axis_len / 2, axis_len / 2, ss)))
    return float(np.mean(vals)), vals


def blocks(M, half, ss=SS):
    """Ten block means from 0% to 100% luminance along one fold half (8 DU wide)."""
    u = half["p100"] - half["p0"]
    L = np.linalg.norm(u)
    out = []
    for i in range(10):
        c = half["p0"] + u * (i + 0.5) / 10
        out.append(region_mean(M, rect_weights(M.shape, c, u, L / 20, 4, ss)))
    return np.array(out)


def summarise(b):
    return dict(min=np.nanmin(b), max=np.nanmax(b), mean=np.nanmean(b), median=np.nanmedian(b))


def rms_contrast_profile(stim, e0, e1, step_pct=1.5, size=16):
    """Local contrast of the stimulus in a size x size DU square centred on the Edge, moved from
    0% to 100% luminance in 1.5% steps (Results, "Neuron responses to corner-folds vs. different
    contrasts along edge", paragraph 1). Returns luminance levels and, per level, the pixel values
    in the square (sampled on a 1 DU grid aligned with the Edge)."""
    u = (e1 - e0) / np.linalg.norm(e1 - e0)
    n = np.array([-u[1], u[0]])
    L = np.linalg.norm(e1 - e0)
    g = np.arange(size) - (size - 1) / 2
    A, B = np.meshgrid(g, g)
    levels = np.arange(0, 100 + 1e-9, step_pct)
    vals = []
    for l in levels:
        c = e0 + u * L * l / 100
        P = c + A.ravel()[:, None] * u + B.ravel()[:, None] * n
        vals.append(ndimage.map_coordinates(stim, [P[:, 1], P[:, 0]], order=1, cval=0.0))
    return levels, np.array(vals)


def _base_nz(M, centres, axis, ss=SS):
    """Baseline leaving out pixels where the smoothed map is exactly zero (no spikes within the
    smoothing kernel, which at the ROI's edge usually means no gaze coverage). A variant."""
    v = []
    for c in centres:
        sl, w = rect_weights(M.shape, c, axis, 8, 8, ss)
        w = w * (M[sl] != 0)
        if w.sum() > 0:
            v.append(float((M[sl] * w).sum() / w.sum()))
    return float(np.mean(v)) if v else np.nan


def _zero_frac(M, centres, axis, ss=SS):
    return float(np.mean([region_mean((M == 0).astype(float), rect_weights(M.shape, c, axis, 8, 8, ss))
                          for c in centres]))


def edge_response(M, e, lum_pct, ss=SS):
    """Mean in a 16 x 16 DU square centred on the Edge at a luminance level (Results, "Neuron
    responses to corner-folds vs. different contrasts along edge", paragraph 1)."""
    u = e["p100"] - e["p0"]
    c = e["p0"] + u * lum_pct / 100.0
    return region_mean(M, rect_weights(M.shape, c, u, 8, 8, ss))


def measure(recs, which="S", ss=SS):
    """One row per neuron and fold, from the Standard maps (which = "S" smoothed, "I" unsmoothed;
    ss as in ``rect_weights``, None for the pixel-centre squares of the first round).

    Columns: baselines under each reading, the raw midpoint response, the ten block means (the
    two halves averaged block by block, and each half), and for the Edge the responses in 16 x 16
    squares at 0 to 100% luminance in 1% steps.
    """
    rows = []
    for r in recs:
        if not r["has_standard"] or r["stim_type"] == "CORNERS":
            continue
        M = r[which]
        S = r["S"]
        g = fold_geometry(r)
        b = {}
        if r["folder"] == "Corners":
            cb = corners_baselines(M.shape, g)
            ax = np.array([0.0, 1.0])
            for k, cs in cb.items():
                b["base_" + k] = baseline(M, cs, ax, ss)
            b["base_main"] = b["base_a_roi_corners"]
            b["base_nz"] = _base_nz(M, cb["a_roi_corners"], ax, ss)
            b["base_zero_frac"] = _zero_frac(S, cb["a_roi_corners"], ax, ss)
            folds = ["S40", "S40dark"]
        else:
            ax = g["baseline_axis"]
            C = np.mean(g["baseline"], axis=0)
            centred = [C + (c - C) * ((np.abs(c - C).max() + 8) / np.abs(c - C).max()) for c in g["baseline"]]
            b["base_inside"] = baseline(M, g["baseline"], ax, ss)
            b["base_centred"] = baseline(M, centred, ax, ss)
            # main reading: the placement closest to the files' own BaseActivity (see module docstring)
            main = centred if r["folder"] == "Edge-compare" else g["baseline"]
            b["base_main"] = baseline(M, main, ax, ss)
            b["base_nz"] = _base_nz(M, main, ax, ss)
            b["base_zero_frac"] = _zero_frac(S, main, ax, ss)
            folds = [k for k in ("Edge", "P180", "S90", "S52") if k in g]
        b["base_file"] = r.get("base_file", np.nan)
        for fd in folds:
            if fd not in g:
                continue
            mp, halves = midpoint(M, g[fd], ss=ss)
            bl = [blocks(M, h, ss) for h in g[fd]]
            row = dict(folder=r["folder"], code=r["code"], cell=r["cell"], monkey=r["monkey"], fold=fd,
                       mid_resp=mp, mid_halves=halves, blocks=np.mean(bl, 0), blocks_halves=bl, **b)
            if fd == "Edge":
                row["edge_profile"] = np.array([edge_response(M, g[fd][0], l, ss) for l in range(0, 101)])
            rows.append(row)
    return pd.DataFrame(rows)
