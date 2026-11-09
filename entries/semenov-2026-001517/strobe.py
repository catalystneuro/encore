"""Loading and measures for dandiset 001517 (Semenov et al. 2026, Bioelectrochemistry 171, 109283).

The dandiset holds raw strobe images: each NWB file is one set of 100 frames (512 x 512, uint16)
of one CHO cell, the first 40 without a pulse and the next 60 taken 900 ns into a 1-us pulse
(Methods 2.3). The pulse amplitude (in volts) and the dye are given only in the session
description. Nothing else (no cell outline, no field direction, no field strength in V/cm, no
pixel size) is stored, so the measures are rebuilt here from the images.

Where each parameter comes from:

- 40 baseline and 60 pulse frames, 6-pixel-wide trace along the perimeter, 360 points, +-5 degree
  pole arcs, dF = 100 (F - F0) / F0: Methods 2.3 of the paper (claims file, common method).
- Background: ROIs outside the cell near the poles, 6 pixels wide and about 20 degrees wide,
  subtracted from every measurement. Reference [20] of the paper (Semenov et al. 2025,
  Bioelectrochemistry 168, 109143, PMC12553484, section 2.4: "Similarly sized ROIs were selected
  near the poles outside of the cell to measure the background fluorescence"), which the
  paper's Methods say it follows ("Most methods were identical to those described in detail
  recently [20]"). Their distance from the membrane is not given, and it matters here: the
  out-of-focus glow of the membrane decays slowly outside the cell (shown in the notebook's data
  check). Two distances are run: "near", 8 to 14 pixels (2 to 4 um) outside the membrane centre
  line, just outside the 6-pixel trace; and "far", 30 to 36 pixels (8 to 10 um) outside it, where
  the glow has mostly decayed (a "cell-free region", as the paper's Ca2+ method words it,
  Methods 2.4). The claims file also asks for the unsubtracted reading ("none"). For the
  verifier's round 1, a sweep of 6-pixel bands from 8 to 44 pixels out (SWEEP_BANDS) shows how
  the results move with the distance, and a "local" variant subtracts at each pole its own ROI
  (and, for whole profiles, the background at the same angle, averaged over +-10 degrees) in
  place of the mean of the two pole ROIs.
- Charging time constant: tau = 44.5 ns per um of radius, the linear fit through the origin of
  reference [20], Fig. 5C ("yielding the slope coefficient of 44.5 ns/um"), which the paper
  says it used (Methods 2.3).
- Volts to V/cm (VOLT_TO_VCM): see the comment there. VOLT_TO_VCM_PROP is the alternative reading,
  field proportional to the volts (the paper: current "scaling linearly with voltage", Methods
  2.2), scaled so that 250, 300 and 350 V give the paper's 1000, 1200 and 1400 V/cm (4 V/cm per V),
  the three steps where the in-order matching is already proportional.
- Pixel size 16 um / 60 = 0.267 um: an assumption. The paper names the iXon Ultra 897 camera
  (512 x 512 pixels of 16 um, the frame size of the files) and a 60x objective; the files give no
  pixel size. The radius it yields is compared with the paper's 8 um average in the notebook.
- Frames without a laser flash: frame 0 of every set and some others hold no fluorescence (their
  mean is near the camera offset). The paper does not mention them; they are left out of every
  average here (a frame without a flash holds no measurement), and the notebook shows the
  result with them kept as a variant. A frame is dark when its mean is below the midpoint
  between the camera floor (1st percentile of all pixels of the set) and the median frame mean.
- The cell outline: the membrane is found on each of 360 rays from the cell centre as the radius
  of peak intensity in the baseline image, median-filtered over 15 degrees. The paper drew the
  trace by hand in MetaMorph; this is a standard automatic choice. Angles are polar angles from
  the cell centre (the paper resamples by perimeter length; for these near-circular cells the
  two agree closely). After verification round 2, a variant outline (membrane_line_outer) takes the
  outermost strong peak on each ray and keeps only the first six angular harmonics, for the
  Di-8-ANEPPS cells whose outline the overlays showed to cut inside the membrane.
- Field direction: not stored. The cathode-facing pole is where dF is positive (Methods 2.3:
  emission increased in the cathode-facing hemisphere). Its direction is estimated once per
  recording day from the first angular harmonic of dF at low fields, pooled over cells, and the
  same axis is then used for every set of that day.
"""
from __future__ import annotations

import hashlib
import re

import h5py
import numpy as np
import remfile
import requests
from scipy import ndimage

DANDISET = "001517"
VERSION = "0.261006.1856"
API = "https://api.dandiarchive.org/api"

N_BASE, N_PULSE = 40, 60          # Methods 2.3
TRACE_WIDTH = 6                   # pixels, Methods 2.3
N_POINTS = 360                    # Methods 2.3
POLE_HALF_WIDTH = 5               # degrees, Methods 2.3
BG_OFFSETS = {"near": (8, 14), "far": (30, 36)}   # pixels outside the membrane line (see above)
SWEEP_BANDS = [(8, 14), (14, 20), (20, 26), (26, 32), (32, 38), (38, 44)]   # sweep of the distance
SWEEP = {f"d{a}-{b}": (a, b) for a, b in SWEEP_BANDS}
BACKGROUNDS = ("far", "near", "none")
BG_HALF_WIDTH = 10                # degrees, ref [20] "about 20 degrees wide"
UM_PER_PIXEL = 16.0 / 60.0        # assumption, see above
TAU_NS_PER_UM = 44.5              # ref [20], Fig. 5C
T_IMAGE_NS = 900.0                # Methods 2.3, 1-us pulses

# Volts in the files -> the nine field strengths the paper names for its 1-us escalations
# (Results 3.1 to 3.4, Fig. 2A and 4A/B: 43 to 1400 V/cm). An assumption: the files give volts
# only and the paper V/cm only; the two series have nine steps each and are matched in order.
VOLT_TO_VCM = {25: 43, 50: 150, 70: 230, 100: 360, 150: 570, 200: 780, 250: 1000,
               300: 1200, 350: 1400}
VOLT_TO_VCM_PROP = {v: 4 * v for v in VOLT_TO_VCM}     # alternative reading, field proportional to volts
CROP = 72                         # half-size of the baseline crop kept for the outline overlays


def list_assets() -> list[dict]:
    """Every asset of the pinned version with its subject, start time, dye and pulse volts."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000&metadata=1"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        for a in r["results"]:
            m = a.get("metadata") or requests.get(
                f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{a['asset_id']}/",
                timeout=60).json()
            ses = [g for g in m["wasGeneratedBy"] if g.get("schemaKey") == "Session"][0]
            d = ses["description"]
            out.append(dict(
                path=a["path"], asset_id=a["asset_id"], size=a["size"],
                subject=a["path"].split("/")[0].replace("sub-", ""),
                start=ses["startDate"],
                dye="Di-8-ANEPPS" if "Di-8-ANEPPS" in d else ("FluoVolt" if "FluoVolt" in d else "?"),
                volts=int(re.search(r"at (\d+)\s*V amplitude", d).group(1)),
                pulse_us=float(re.search(r"single ([\d.]+) µs", d).group(1)),
                electrode_mm=float(re.search(r"Distance between electrodes ([\d.]+) mm", d).group(1)),
                description=d))
        url = r.get("next")
    return out


def open_asset(asset_id: str) -> h5py.File:
    url = f"{API}/assets/{asset_id}/download/"
    s3 = requests.head(url, allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(s3), "r")


def nwb_tree(asset_id: str) -> list[str]:
    """Every group and dataset of one file, with shapes, dtypes and attributes (array data not
    read), to show which metadata the files hold."""
    out = []
    with open_asset(asset_id) as f:
        def visit(name, obj):
            kind = "dataset" if isinstance(obj, h5py.Dataset) else "group"
            extra = f" shape={obj.shape} dtype={obj.dtype}" if kind == "dataset" else ""
            if kind == "dataset" and obj.size <= 4 and obj.dtype.kind in "OSUif":
                v = obj[()]
                extra += f" value={v.decode() if isinstance(v, bytes) else v!r}"[:300]
            attrs = {k: (v.decode() if isinstance(v, bytes) else v) for k, v in obj.attrs.items()
                     if k not in ("namespace", "object_id")}
            out.append(f"{kind:7s} /{name}{extra} {attrs if attrs else ''}"[:400])
        f.visititems(lambda n, o: None if n.startswith("specifications") else visit(n, o))
        out.insert(0, f"root attrs {dict((k, v) for k, v in f.attrs.items() if k != 'object_id')}")
    return out


def dark_frames(data: np.ndarray) -> np.ndarray:
    """Boolean mask of frames without a laser flash (see module docstring)."""
    means = data.reshape(len(data), -1).mean(1)
    floor = np.percentile(data[::10], 1)
    return means < floor + 0.5 * (np.median(means) - floor)


def find_cell(img: np.ndarray, search: int = 60, centre=None, radii=None) -> tuple[float, float, float]:
    """Centre (row, col) and radius (pixels) of the cell nearest the image centre: the circle,
    centred within +-search pixels of the image centre (or of a given centre), whose ring is
    brightest relative to the ring 4 pixels outside it (the membrane is the bright outline of a
    stained cell). radii limits the radii tried (default 20 to 55 pixels)."""
    sm = ndimage.gaussian_filter(img, 1.5)
    phi = np.linspace(0, 2 * np.pi, 90, endpoint=False)
    radii = np.arange(20, 56) if radii is None else np.asarray(radii)

    sin, cos = np.sin(phi)[None], np.cos(phi)[None]

    def score(cy, cx):
        on = ndimage.map_coordinates(sm, [cy - radii[:, None] * sin, cx + radii[:, None] * cos], order=1)
        out = ndimage.map_coordinates(sm, [cy - (radii[:, None] + 4) * sin, cx + (radii[:, None] + 4) * cos], order=1)
        inn = ndimage.map_coordinates(sm, [cy - (radii[:, None] - 4) * sin, cx + (radii[:, None] - 4) * cos], order=1)
        # a membrane is brighter than both sides (the edge of a bright interior blob is not);
        # median, so that a neighbouring cell touching part of the circle does not dominate
        v = np.median(np.minimum(on - out, on - inn), axis=1)
        k = int(v.argmax())
        return v[k], radii[k]

    c0 = np.array(img.shape) / 2 if centre is None else np.asarray(centre, float)
    step = 4 if search > 12 else 2
    grid = [(c0[0] + dy, c0[1] + dx) for dy in range(-search, search + 1, step) for dx in range(-search, search + 1, step)]
    res = [(score(cy, cx), cy, cx) for cy, cx in grid]
    (v, rr), cy, cx = max(res, key=lambda t: t[0][0])
    fine = [(score(cy + dy, cx + dx), cy + dy, cx + dx) for dy in range(-3, 4) for dx in range(-3, 4)]
    (v, rr), cy, cx = max(fine, key=lambda t: t[0][0])
    return float(cy), float(cx), float(rr)


def membrane_line(img: np.ndarray, cy: float, cx: float, r0: float):
    """Radius of the membrane on each of 360 rays (1-degree steps): the peak of intensity within
    +-5 pixels of the circle found by find_cell, median-filtered over 15 degrees and smoothed
    over 9 degrees; the centre is then moved to the outline's centroid."""
    sm = ndimage.gaussian_filter(img, 1)
    ang = np.deg2rad(np.arange(N_POINTS))
    for _ in range(2):
        rr = np.linspace(r0 - 5, r0 + 5, 41)
        ys = cy - np.outer(np.sin(ang), rr)
        xs = cx + np.outer(np.cos(ang), rr)
        prof = ndimage.map_coordinates(sm, [ys, xs], order=1)
        r = ndimage.median_filter(rr[prof.argmax(1)], size=15, mode="wrap")
        r = ndimage.uniform_filter1d(r, 9, mode="wrap")
        y = cy - r * np.sin(ang)
        x = cx + r * np.cos(ang)
        cy, cx = y.mean(), x.mean()
        r0 = float(np.hypot(y - cy, x - cx).mean())
    r = np.hypot(y - cy, x - cx)
    # re-index to angles about the new centre
    a = np.rad2deg(np.arctan2(-(y - cy), x - cx)) % 360
    o = np.argsort(a)
    r = np.interp(np.arange(N_POINTS), a[o], r[o], period=360)
    return cy, cx, r


def membrane_line_outer(img: np.ndarray, cy: float, cx: float, r0: float, frac: float = 0.8, nharm: int = 6):
    """Variant outline (verification round 2): on each ray, the outermost local peak of intensity
    within +-5 pixels of the circle that reaches frac of the ray's range above its minimum (in
    place of the highest peak, which a bright body just inside the membrane can capture),
    median-filtered over 15 degrees and low-passed to the first nharm angular harmonics (waves
    shorter than 60 degrees removed); the centre is then moved to the outline's centroid."""
    sm = ndimage.gaussian_filter(img, 1)
    ang = np.deg2rad(np.arange(N_POINTS))
    for _ in range(2):
        rr = np.linspace(r0 - 5, r0 + 5, 41)
        ys = cy - np.outer(np.sin(ang), rr)
        xs = cx + np.outer(np.cos(ang), rr)
        prof = ndimage.map_coordinates(sm, [ys, xs], order=1)
        lo, hi = prof.min(1, keepdims=True), prof.max(1, keepdims=True)
        pk = np.zeros_like(prof, bool)
        pk[:, 1:-1] = (prof[:, 1:-1] >= prof[:, :-2]) & (prof[:, 1:-1] >= prof[:, 2:])
        pk[:, -1] = prof[:, -1] >= prof[:, -2]
        strong = pk & (prof >= lo + frac * (hi - lo))
        idx = np.where(strong.any(1), strong.shape[1] - 1 - np.argmax(strong[:, ::-1], 1), prof.argmax(1))
        r = ndimage.median_filter(rr[idx], size=15, mode="wrap")
        f = np.fft.rfft(r)
        f[nharm + 1:] = 0
        r = np.fft.irfft(f, N_POINTS)
        y = cy - r * np.sin(ang)
        x = cx + r * np.cos(ang)
        cy, cx = y.mean(), x.mean()
        r0 = float(np.hypot(y - cy, x - cx).mean())
    r = np.hypot(y - cy, x - cx)
    a = np.rad2deg(np.arctan2(-(y - cy), x - cx)) % 360
    o = np.argsort(a)
    r = np.interp(np.arange(N_POINTS), a[o], r[o], period=360)
    return cy, cx, r


def radius_um(r: np.ndarray) -> dict:
    """Cell radius from the membrane line: (a) perimeter / 2 pi, (b) radius of equal area."""
    ang = np.deg2rad(np.arange(N_POINTS))
    x, y = r * np.cos(ang), r * np.sin(ang)
    per = np.hypot(np.diff(np.r_[x, x[0]]), np.diff(np.r_[y, y[0]])).sum()
    area = 0.5 * np.sum(r ** 2) * np.deg2rad(1.0)
    return dict(perimeter=per / (2 * np.pi) * UM_PER_PIXEL, area=np.sqrt(area / np.pi) * UM_PER_PIXEL)


def extract_set(asset_id: str, hint: tuple[float, float, float] | None = None, outline: str = "peak") -> dict:
    """Stream one set and reduce it to per-frame traces.

    hint (centre row, centre col, radius in pixels) restricts the search for the cell to within 8
    pixels of that centre and 4 pixels of that radius; it is used to re-trace a set whose outline
    jumped to a structure inside the cell (see the notebook's loading cell). outline "outer" uses
    membrane_line_outer (a variant) in place of membrane_line.

    Returns per-frame trace intensities (100 x 360, the 6-pixel band averaged across its width,
    1-degree polar angles in image coordinates, 0 = image right, counter-clockwise), per-frame
    background (100), the dark-frame mask, the cell centre, membrane radius per angle, and a
    hash of the raw data (to find duplicate recordings).
    """
    with open_asset(asset_id) as f:
        data = f["acquisition/StrobeImaging/data"][:]
        rate = float(f["acquisition/StrobeImaging/starting_time"].attrs["rate"])
    digest = hashlib.sha1(data.tobytes()).hexdigest()
    data = data.astype(np.float32)
    dark = dark_frames(data)
    base = data[:N_BASE][~dark[:N_BASE]].mean(0)
    if hint is None:
        cy, cx, r0 = find_cell(base)
    else:
        cy, cx, r0 = find_cell(base, search=8, centre=hint[:2], radii=np.arange(int(hint[2]) - 4, int(hint[2]) + 5))
    cy, cx, r = (membrane_line_outer if outline == "outer" else membrane_line)(base, cy, cx, r0)
    ang = np.deg2rad(np.arange(N_POINTS))
    offs = np.arange(TRACE_WIDTH) - (TRACE_WIDTH - 1) / 2
    ys = (cy - (r[:, None] + offs) * np.sin(ang)[:, None]).ravel()
    xs = (cx + (r[:, None] + offs) * np.cos(ang)[:, None]).ravel()
    trace = np.empty((len(data), N_POINTS), np.float32)
    bands = {**BG_OFFSETS, **SWEEP}
    bgprof = {k: np.empty((len(data), N_POINTS), np.float32) for k in bands}
    for i, fr in enumerate(data):
        trace[i] = ndimage.map_coordinates(fr, [ys, xs], order=1).reshape(N_POINTS, TRACE_WIDTH).mean(1)
        for k, (o1, o2) in bands.items():
            bo = np.arange(o1, o2)
            by = (cy - (r[:, None] + bo) * np.sin(ang)[:, None]).ravel()
            bx = (cx + (r[:, None] + bo) * np.cos(ang)[:, None]).ravel()
            bgprof[k][i] = ndimage.map_coordinates(fr, [by, bx], order=1).reshape(N_POINTS, len(bo)).mean(1)
    base = data[:N_BASE][~dark[:N_BASE]].mean(0)
    radial = radial_profile(base, cy, cx, r)
    y0, x0 = int(round(cy)) - CROP, int(round(cx)) - CROP
    crop = np.pad(base, CROP)[y0 + CROP:y0 + 3 * CROP, x0 + CROP:x0 + 3 * CROP]
    return dict(asset_id=asset_id, trace=trace, bgprof=bgprof, dark=dark, cy=cy, cx=cx, r=r, radial=radial,
                crop=crop, crop_origin=(y0, x0),
                frame_mean=data.reshape(len(data), -1).mean(1), floor=float(np.percentile(data[::10], 1)),
                n_frames=len(data), shape=data.shape[1:], rate=rate, sha1=digest,
                **{f"radius_{k}": v for k, v in radius_um(r).items()})


def arc(theta_deg: np.ndarray, centre: float, half: float) -> np.ndarray:
    """Mask of angles within +-half degrees of centre (circular)."""
    d = (theta_deg - centre + 180) % 360 - 180
    return np.abs(d) <= half


def field_angle(sets: list[dict]) -> float:
    """Image angle (degrees) of the cathode-facing pole, from the first harmonic of collapsed dF
    pooled over the given sets (no background subtraction, so it does not depend on the axis)."""
    z = 0j
    ang = np.deg2rad(np.arange(N_POINTS))
    for s in sets:
        dfp = collapsed_df(s, axis=None, background="none")
        z += np.sum(dfp * np.exp(1j * ang))
    return float(np.rad2deg(np.angle(z)) % 360)


RADIAL_OFFSETS = np.arange(-6, 41, 2)


def radial_profile(img, cy, cx, r):
    """Mean intensity of an image at offsets from the membrane line (pixels, all angles)."""
    ang = np.deg2rad(np.arange(N_POINTS))
    return np.array([ndimage.map_coordinates(img, [cy - (r + o) * np.sin(ang), cx + (r + o) * np.cos(ang)],
                                             order=1).mean() for o in RADIAL_OFFSETS])


def _bg(s: dict, axis: float | None, which: str) -> np.ndarray:
    """Background per frame and perimeter angle (frames x 360). For "near", "far" or a sweep band:
    the mean of the two ROIs outside the cell, +-10 degrees about each pole, the same at every
    angle. With the suffix "_local" (e.g. "far_local"): at each angle the band outside the cell
    averaged over +-10 degrees about that angle, so each pole has its own background."""
    if which == "none":
        return np.zeros((s["n_frames"], N_POINTS))
    if which.endswith("_local"):
        return ndimage.uniform_filter1d(s["bgprof"][which[:-6]].astype(float), 2 * BG_HALF_WIDTH + 1,
                                        axis=1, mode="wrap")
    th = np.arange(N_POINTS)
    if axis is None:
        b = s["bgprof"][which].mean(1)
    else:
        m = arc(th, axis, BG_HALF_WIDTH) | arc(th, axis + 180, BG_HALF_WIDTH)
        b = s["bgprof"][which][:, m].mean(1)
    return np.repeat(b[:, None], N_POINTS, axis=1)


def rotate(profile: np.ndarray, axis: float) -> np.ndarray:
    """Re-index a 360-point profile so that index k is the polar angle k degrees from the
    cathode-facing pole (0 = cathodic pole, 180 = anodic pole)."""
    idx = (np.arange(N_POINTS) + int(round(axis))) % N_POINTS
    return profile[..., idx]


def frames(s: dict, keep_dark: bool = False):
    ok = np.ones(s["n_frames"], bool) if keep_dark else ~s["dark"]
    b = np.where(ok[:N_BASE])[0]
    p = N_BASE + np.where(ok[N_BASE:N_BASE + N_PULSE])[0]
    return b, p


def collapsed_df(s: dict, axis: float | None, background: str = "far", keep_dark: bool = False,
                 pulse_frames: slice | None = None) -> np.ndarray:
    """dF (%) along the perimeter between the collapsed baseline and polarization images
    (Methods 2.3). With an axis, the profile is rotated so index 0 is the cathodic pole.
    pulse_frames selects a part of the 60 pulse images (e.g. slice(0, 10), the first 10)."""
    b, p = frames(s, keep_dark)
    if pulse_frames is not None:
        allp = np.arange(N_BASE, N_BASE + N_PULSE)[pulse_frames]
        p = np.intersect1d(p, allp)
    tr = s["trace"].astype(float) - _bg(s, axis, background)
    F0 = tr[b].mean(0)
    F = tr[p].mean(0)
    df = 100 * (F - F0) / F0
    return df if axis is None else rotate(df, axis)


def pole_values(dfp: np.ndarray) -> tuple[float, float]:
    """Mean dF in the +-5 degree arcs at the cathodic (0) and anodic (180) poles of a rotated
    profile."""
    th = np.arange(N_POINTS)
    return float(dfp[arc(th, 0, POLE_HALF_WIDTH)].mean()), float(dfp[arc(th, 180, POLE_HALF_WIDTH)].mean())


def per_image_pole_df(s: dict, axis: float, background: str = "far", keep_dark: bool = False):
    """Per-image pole dF (Fig. 2 measure, Methods 2.3): F is the mean trace intensity in the +-5
    degree arc at each pole in each image, F0 its mean over the baseline images. Returns two
    arrays of 100 values (NaN for dark frames unless kept) for the cathodic and anodic poles."""
    th = np.arange(N_POINTS)
    tr = s["trace"].astype(float) - _bg(s, axis, background)
    out = []
    for c in (axis, axis + 180):
        F = tr[:, arc(th, c, POLE_HALF_WIDTH)].mean(1)
        ok = np.ones(len(F), bool) if keep_dark else ~s["dark"]
        F0 = F[:N_BASE][ok[:N_BASE]].mean()
        d = 100 * (F - F0) / F0
        d[~ok] = np.nan
        out.append(d)
    return out[0], out[1]


def impc_profile(E_vcm: float, R_um: float, t_ns: float = T_IMAGE_NS) -> np.ndarray:
    """Eq. (1): IMPC (mV) at polar angles 0..359 degrees from the cathodic pole."""
    tau = TAU_NS_PER_UM * R_um
    th = np.deg2rad(np.arange(N_POINTS))
    # E in V/cm -> V/m (x100), R in um -> m (1e-6), result in V -> mV (x1000)
    return 1.5 * E_vcm * 100 * R_um * 1e-6 * np.cos(th) * (1 - np.exp(-t_ns / tau)) * 1000


def f_factor(lam_m: float, R: float = 8e-6, d: float = 5e-9, lam_i: float = 0.4, lam_o: float = 1.64):
    """Eq. (2) of the paper (constants of Methods 2.3)."""
    num = 3 * lam_o * (3 * R ** 2 * d * lam_i + (3 * d ** 2 * R - d ** 3) * (lam_m - lam_i))
    den = 2 * R ** 3 * (lam_m + 2 * lam_o) * (lam_m + 0.5 * lam_i) - 2 * (R - d) ** 3 * (lam_o - lam_m) * (lam_i - lam_m)
    return num / den
