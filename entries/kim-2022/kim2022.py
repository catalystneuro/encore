"""Loading and measures for Kim et al. (2022), Bioelectrochemistry 149:108319.

Two dandisets, streamed from the DANDI archive at pinned versions:

- 000489: stitched two-channel images of BPAE monolayers after 5 pulses of
  600 ns (unipolar) or 600+600 ns (bipolar, second phase 25 to 100%) at 1 Hz
  (the experiment of Fig. 2). Channel index 0 is MemBrite (350/460 nm),
  index 1 is YO-PRO-1 (480/535 nm); this is checked in the notebook.
- 000448: strobe image stacks (500 frames, 25 ns apart) of FluoVolt-loaded CHO
  cells given trains of 5 pulses at 833 kHz (Fig. 7).

Where each parameter comes from is said where it is defined.
"""

from __future__ import annotations

import h5py
import numpy as np
import remfile
import requests
from scipy import ndimage as ndi
from scipy.signal import fftconvolve

API = "https://api.dandiarchive.org/api"
VERSIONS = {"000489": "0.230518.1811", "000448": "0.230421.1844"}

# ---------------------------------------------------------------- archive


def list_assets(dandiset: str) -> list[dict]:
    """Asset records of the pinned version, sorted by path."""
    url = f"{API}/dandisets/{dandiset}/versions/{VERSIONS[dandiset]}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        j = r.json()
        out += j["results"]
        url = j["next"]
    return sorted(out, key=lambda a: a["path"])


def s3_url(dandiset: str, asset_id: str) -> str:
    r = requests.get(
        f"{API}/dandisets/{dandiset}/versions/{VERSIONS[dandiset]}/assets/{asset_id}/", timeout=60
    )
    r.raise_for_status()
    return [u for u in r.json()["contentUrl"] if "s3" in u][0]


def open_nwb(dandiset: str, asset_id: str) -> h5py.File:
    """Open an asset as a streamed HDF5 file (no download to disk)."""
    return h5py.File(remfile.File(s3_url(dandiset, asset_id)), "r")


# ---------------------------------------------------------------- 000489: dish images

# Pixel size. The files give none (resolution -1). Methods 2.5 names the camera
# (ORCA-Flash4 sCMOS, 6.5 um pixels by its specification) and the 10x objective,
# hence 0.65 um per pixel; the notebook checks it against the electrode spacing
# (Methods 2.2, 3 mm side to side, 1.5 mm diameter, so 4.5 mm centre to centre).
UM_PER_PX = 0.65
BLOCK = 7  # block averaging factor on loading (22323 = 7 x 3189); 4.55 um, a standard choice
UM_PER_BLOCK = UM_PER_PX * BLOCK
ROI_UM = 200.0  # Methods 2.5, "200-um square ROI"
FIRST_PHASE_KV = 5.75  # Results 3.1, first phase kept at 5.75 kV

# Electrode geometry for the field model, Methods 2.3: two cylinders 1.5 mm in
# diameter, 3 mm apart (side to side).
ELECTRODE_RADIUS_MM = 0.75
ELECTRODE_HALF_SPACING_MM = 0.75 + 1.5  # centre at +-2.25 mm


def dish_info(f: h5py.File) -> dict:
    k = list(f["acquisition"])[0]
    return {
        "series": k,
        "session_description": f["session_description"][()].decode(),
        "subject_id": f["general/subject/subject_id"][()].decode(),
        "session_id": f["general/session_id"][()].decode(),
        "session_start_time": f["session_start_time"][()].decode(),
        "shape": f["acquisition"][k]["data"].shape,
        "description": f["acquisition"][k].attrs["description"],
    }


def load_dish(dandiset: str, asset_id: str, block: int = BLOCK) -> np.ndarray:
    """Stream a stitched dish image and return its block means, float32 (rows, cols, 2).

    The image is read in bands of 1225 rows (7 rows of HDF5 chunks), so that one
    band (about 110 MB) is in memory at a time.
    """
    with open_nwb(dandiset, asset_id) as f:
        d = f["acquisition"][list(f["acquisition"])[0]]["data"]
        n0, n1, nc = d.shape
        out = np.zeros((n0 // block, n1 // block, nc), np.float32)
        step = 175 * block
        for r0 in range(0, (n0 // block) * block, step):
            r1 = min(r0 + step, (n0 // block) * block)
            a = d[r0:r1, : (n1 // block) * block, :].astype(np.float32)
            h = a.shape[0] // block
            out[r0 // block : r0 // block + h] = a.reshape(h, block, n1 // block, block, nc).mean(axis=(1, 3))
    return out


def find_footprints(yp: np.ndarray, r_px: float = 160.0) -> dict:
    """Find the two electrode footprints, the dark discs of the YP channel (Fig. 1F).

    A disc of radius r_px (block pixels) is compared with the ring from 1.3 to
    1.8 r_px around it; the two deepest minima of disc minus ring that are more
    than 6 r_px apart are the footprints. The search is a standard choice; the
    notebook shows the result for every dish. Returns centres (row, col) in block
    pixels, refined to the centroid of the dark pixels within 1.3 r_px.
    """
    s = 4
    small = yp[: yp.shape[0] // s * s, : yp.shape[1] // s * s]
    small = small.reshape(small.shape[0] // s, s, small.shape[1] // s, s).mean(axis=(1, 3))
    r = r_px / s
    yy, xx = np.mgrid[-int(2 * r) : int(2 * r) + 1, -int(2 * r) : int(2 * r) + 1]
    rr = np.hypot(yy, xx)
    disc = (rr <= r).astype(float)
    ring = ((rr >= 1.3 * r) & (rr <= 1.8 * r)).astype(float)
    m_disc = fftconvolve(small, disc / disc.sum(), mode="same")
    m_ring = fftconvolve(small, ring / ring.sum(), mode="same")
    score = m_disc - m_ring
    # Only the central part of the image holds the electrodes; the glass edge is
    # also dark-against-bright, so the outer 30% on each side is excluded.
    n0, n1 = score.shape
    mask = np.zeros_like(score, bool)
    mask[int(0.25 * n0) : int(0.75 * n0), int(0.15 * n1) : int(0.85 * n1)] = True
    sc = np.where(mask, score, np.inf)
    i1 = np.unravel_index(np.argmin(sc), sc.shape)
    yy2, xx2 = np.mgrid[0:n0, 0:n1]
    far = np.hypot(yy2 - i1[0], xx2 - i1[1]) > 4 * r
    i2 = np.unravel_index(np.argmin(np.where(far, sc, np.inf)), sc.shape)
    centres, radii = [], []
    for (a, b) in (i1, i2):
        c = np.array([a * s + s / 2, b * s + s / 2])
        # refine: the smoothed window is thresholded at 30% of the way from the
        # dark level (5th percentile) to the median of the window, and the centroid
        # of the dark component holding the estimate is taken; repeated twice.
        cc = c.copy()
        w = int(2 * r_px)
        for _ in range(3):
            y0, x0 = int(round(cc[0])), int(round(cc[1]))
            win = ndi.gaussian_filter(yp[y0 - w : y0 + w + 1, x0 - w : x0 + w + 1].astype(float), 3)
            lo, hi = np.percentile(win, 5), np.median(win)
            lab, _ = ndi.label(win < lo + 0.3 * (hi - lo))
            g0, g1 = np.mgrid[-w : w + 1, -w : w + 1]
            ids = lab[np.hypot(g0, g1) < 0.3 * r_px]
            ids = ids[ids > 0]
            if len(ids) == 0:
                break
            comp = lab == np.bincount(ids).argmax()
            cc = np.array([y0 + g0[comp].mean(), x0 + g1[comp].mean()])
        dy, dx = cc[0] - y0 + w, cc[1] - x0 + w
        gy, gx = np.mgrid[-w : w + 1, -w : w + 1]
        dist = np.hypot(gy - (dy - w), gx - (dx - w))
        prof = np.array([win[(dist >= q) & (dist < q + 2)].mean() for q in range(0, int(1.8 * r_px), 2)])
        half = (prof[: int(0.5 * r_px / 2)].mean() + prof[int(1.3 * r_px / 2) :].mean()) / 2
        above = np.nonzero(prof > half)[0]
        above = above[above > int(0.3 * r_px / 2)]
        centres.append(cc)
        radii.append(float(above[0] * 2) if len(above) else np.nan)
    order = np.argsort([c[1] for c in centres])  # left electrode first
    return {"centres": np.array(centres)[order], "radius_px": np.array(radii)[order],
            "score": [float(score[i1]), float(score[i2])]}


def field_kv_cm(x_mm, y_mm, volts: float = FIRST_PHASE_KV * 1000):
    """Electric field (kV/cm) of two parallel cylinders in a conducting layer.

    The geometry is that of Methods 2.3 (cylinders 1.5 mm in diameter, 3 mm apart,
    touching the glass, solution 3.5 mm deep). As the electrodes cross the whole
    solution layer, the field does not depend on height and the problem is two
    dimensional; it is solved exactly with the two line charges of the
    two-cylinder problem. The dish wall (17.5 mm away) is ignored. x is along the
    line through both electrode centres (aa'), y along bb', both from the midpoint.
    This replaces the paper's finite element model (Sim4Life), whose output is not
    deposited; the notebook compares it with the paper's 15.1 kV/cm at the centre.
    """
    d = ELECTRODE_HALF_SPACING_MM
    a = ELECTRODE_RADIUS_MM
    b = np.sqrt(d * d - a * a)
    c = volts / (2 * np.log((d + b) / a))  # volts per unit of ln(r2/r1)
    x = np.asarray(x_mm, float)
    y = np.asarray(y_mm, float)
    r1 = (x - b) ** 2 + y**2
    r2 = (x + b) ** 2 + y**2
    ex = c * ((x + b) / r2 - (x - b) / r1)
    ey = c * (y / r2 - y / r1)
    return np.hypot(ex, ey) / 1000 * 10  # V/mm -> kV/cm


def roi_mean_field(x_mm: float, y_mm: float, side_mm: float = ROI_UM / 1000, n: int = 21) -> float:
    """Mean field over a square ROI (Methods 2.5: the mean field of each ROI is used)."""
    g = (np.arange(n) + 0.5) / n - 0.5
    gx, gy = np.meshgrid(x_mm + g * side_mm, y_mm + g * side_mm)
    return float(field_kv_cm(gx, gy).mean())


def dish_frame(centres: np.ndarray):
    """Midpoint, unit vector along aa' (left to right electrode) and along bb'."""
    c0, c1 = centres
    mid = (c0 + c1) / 2
    ua = (c1 - c0) / np.linalg.norm(c1 - c0)
    ub = np.array([-ua[1], ua[0]])
    return mid, ua, ub


def square_mean(img: np.ndarray, centre_rc: np.ndarray, ua: np.ndarray, ub: np.ndarray, side_px: float) -> float:
    """Mean of img over a square of side side_px centred at centre_rc, aligned with ua and ub."""
    n = int(np.ceil(side_px))
    g = (np.arange(n) + 0.5) / n * side_px - side_px / 2
    s, t = np.meshgrid(g, g)
    rr = centre_rc[0] + s * ua[0] + t * ub[0]
    cc = centre_rc[1] + s * ua[1] + t * ub[1]
    return float(ndi.map_coordinates(img, [rr.ravel(), cc.ravel()], order=1).mean())


def footprint_mean(img: np.ndarray, centre_rc: np.ndarray, radius_px: float) -> float:
    n0, n1 = img.shape
    r0, c0 = int(round(centre_rc[0])), int(round(centre_rc[1]))
    w = int(np.ceil(radius_px)) + 1
    gy, gx = np.mgrid[-w : w + 1, -w : w + 1]
    m = np.hypot(gy, gx) <= radius_px
    return float(img[r0 - w : r0 + w + 1, c0 - w : c0 + w + 1][m].mean())


# Footprint area used for YP0 and MB0 (Methods 2.5: "the monolayer area within the
# footprints of the hollow electrodes ... was used to measure the spontaneous YP
# uptake"). The disc of radius 0.2 mm around each footprint centre, well inside the
# dark disc (radius about 0.35 mm in these images); a standard choice, varied in
# the notebook.
FOOTPRINT_RADIUS_MM = 0.2


def roi_table(img: np.ndarray, centres: np.ndarray, line: str = "bb", max_mm: float = 3.0,
              fp_radius_mm: float = FOOTPRINT_RADIUS_MM) -> list[dict]:
    """YP per ROI along a line (Methods 2.5).

    ROI are contiguous 200 um squares tiled outward from the midpoint between the
    electrodes on both sides of it (the claims file's reading (a); reading (b), one
    side, is the subset with offset of one sign). Along bb' the first ROI is centred
    on the midpoint and the others at multiples of 0.2 mm. Along aa' the ROI start at
    the midpoint and stop before the electrode edge. YP = YP_ROI x MB0 / MB_ROI - YP0,
    with YP0 and MB0 the means over both footprints.
    """
    mb, yp = img[..., 0], img[..., 1]
    mid, ua, ub = dish_frame(centres)
    side = ROI_UM / UM_PER_BLOCK
    fp_r = fp_radius_mm * 1000 / UM_PER_BLOCK
    yp0 = np.mean([footprint_mean(yp, c, fp_r) for c in centres])
    mb0 = np.mean([footprint_mean(mb, c, fp_r) for c in centres])
    rows = []
    step = ROI_UM / 1000
    if line == "bb":
        offsets = np.arange(-int(round(max_mm / step)), int(round(max_mm / step)) + 1) * step
        for o in offsets:
            ctr = mid + ub * (o * 1000 / UM_PER_BLOCK)
            rows.append({"offset_mm": round(float(o), 3), "x_mm": 0.0, "y_mm": float(o)})
    else:
        lim = ELECTRODE_HALF_SPACING_MM - ELECTRODE_RADIUS_MM - step / 2
        k = int(np.floor(lim / step + 1e-9))
        offsets = (np.arange(-k, k + 1)) * step
        for o in offsets:
            rows.append({"offset_mm": round(float(o), 3), "x_mm": float(o), "y_mm": 0.0})
    for r in rows:
        if line == "bb":
            ctr = mid + ub * (r["y_mm"] * 1000 / UM_PER_BLOCK)
        else:
            ctr = mid + ua * (r["x_mm"] * 1000 / UM_PER_BLOCK)
        y = square_mean(yp, ctr, ua, ub, side)
        m = square_mean(mb, ctr, ua, ub, side)
        r.update({
            "field_kv_cm": roi_mean_field(r["x_mm"], r["y_mm"]),
            "YP_roi": y, "MB_roi": m, "YP0": yp0, "MB0": mb0,
            "YP": y * mb0 / m - yp0,
        })
    return rows


# ---------------------------------------------------------------- 000448: strobe imaging

FRAME_NS = 25.0  # Methods 2.6, 25 ns steps; the files' rate of 40 MHz agrees
N_BASE = 40  # Methods 2.6, "the mean value for the 40 datapoints before the pulse"
PERIOD_NS = 1200.0  # 833 kHz
PULSE_NS = 600.0


def strobe_info(f: h5py.File) -> dict:
    d = f["acquisition/StrobeImaging/data"]
    desc = f["session_description"][()].decode()
    kv = dict(p.split(": ", 1) for p in desc.split(", "))
    return {
        "subject_id": f["general/subject/subject_id"][()].decode(),
        "session_id": f["general/session_id"][()].decode(),
        "start": f["session_start_time"][()].decode(),
        "shape": d.shape,
        "rate": float(f["acquisition/StrobeImaging/starting_time"].attrs["rate"]),
        "pulse_shape": kv["Pulse_shape"],
        "recording": kv["Recording"].split(" ")[0],
        "cell": kv["Recording"].split("(")[1].rstrip(")"),
        "field": kv["Electric_field"],
        "rate_label": kv["Pulse_repetition_rate"],
        "n_pulses": kv["Number_of_pulses"],
    }


def load_stack(asset_id: str) -> np.ndarray:
    """Stream a strobe stack (500, 512, 512) as float32."""
    with open_nwb("000448", asset_id) as f:
        return f["acquisition/StrobeImaging/data"][()].astype(np.float32)


def membrane_and_poles(mean_img: np.ndarray, pct: float = 85.0, cone_deg: float = 45.0, sigma: float = 6.0):
    """Cell membrane mask and the two pole masks along the image's vertical axis.

    The paper does not say how the pole regions were drawn (Methods 2.6 says only
    that the signals of the cathode- and anode-facing poles were scaled to the
    whole-cell signal). Assumption, varied in the notebook: the membrane is the
    pixels of the frame-averaged image above its 85th percentile, in the largest
    connected group (cells imaged alone or in small groups, Methods 2.6); its
    holes filled give the cells' outline, and a pole is the membrane where the
    outward normal of the smoothed outline points within 45 degrees of the field
    axis. The field axis is the image's vertical axis, the axis of the response
    dipole in every file (checked in the notebook); upper and lower poles are
    returned, and which faces the cathode is decided from the data.
    """
    m = ndi.gaussian_filter(mean_img, 1)
    mask = m > np.percentile(m, pct)
    lab, n = ndi.label(mask)
    counts = np.bincount(lab.ravel())
    counts[0] = 0
    memb = lab == counts.argmax()
    filled = ndi.binary_fill_holes(memb)
    g = ndi.gaussian_filter(filled.astype(float), sigma)
    gy, gx = np.gradient(g)
    mag = np.hypot(gy, gx)
    strong = mag > 0.2 * mag[memb].max()
    with np.errstate(invalid="ignore", divide="ignore"):
        ny = -gy / mag  # outward normal, y component (image rows grow downwards)
    c = np.cos(np.deg2rad(cone_deg))
    upper = memb & strong & (ny < -c)
    lower = memb & strong & (ny > c)
    return memb, upper, lower


def pole_traces(stack: np.ndarray, memb, upper, lower) -> dict:
    """Per-frame mean of each pole divided by the whole-cell (membrane) mean (Methods 2.6)."""
    wc = stack[:, memb].mean(axis=1)
    return {"upper": stack[:, upper].mean(axis=1) / wc, "lower": stack[:, lower].mean(axis=1) / wc, "whole": wc}


def process_dish(asset: dict) -> dict:
    """Load one dish image and reduce it to what the analysis needs.

    Returns the file's metadata, the footprints, ROI tables along bb' (footprint
    disc of 0.2 mm, and 0.1 and 0.3 mm as variants), channel summaries, a digest
    of each channel's block means (to find images deposited twice) and a
    thumbnail of the YP channel.
    """
    import hashlib

    with open_nwb("000489", asset["asset_id"]) as f:
        info = dish_info(f)
    img = load_dish("000489", asset["asset_id"])
    out = {"path": asset["path"], "asset_id": asset["asset_id"], **info}
    out["digest"] = [hashlib.sha1(np.ascontiguousarray(img[..., c]).tobytes()).hexdigest()[:12] for c in range(img.shape[2])]
    out["channel_median"] = [float(np.median(img[..., c])) for c in range(img.shape[2])]
    out["channel_max"] = [float(img[..., c].max()) for c in range(img.shape[2])]
    out["thumb_yp"] = img[::8, ::8, 1].copy()
    out["thumb_mb"] = img[::8, ::8, 0].copy()
    if "Fig2" not in info["subject_id"]:
        return out
    fp = find_footprints(img[..., 1])
    out["footprints"] = fp
    out["rois"] = roi_table(img, fp["centres"], "bb", max_mm=3.0)
    out["rois_fp01"] = roi_table(img, fp["centres"], "bb", max_mm=3.0, fp_radius_mm=0.1)
    out["rois_fp03"] = roi_table(img, fp["centres"], "bb", max_mm=3.0, fp_radius_mm=0.3)
    # channel identity: mean of each channel in the 1 mm square between the
    # electrodes over its mean in squares 3 mm away along bb'
    mid, ua, ub = dish_frame(fp["centres"])
    side = 1000 / UM_PER_BLOCK
    out["centre_over_far"] = [
        square_mean(img[..., c], mid, ua, ub, side)
        / np.mean([square_mean(img[..., c], mid + s * ub * 3000 / UM_PER_BLOCK, ua, ub, side) for s in (-1, 1)])
        for c in range(img.shape[2])
    ]
    return out


def process_strobe(asset: dict, pct: float = 85.0, cone_deg: float = 45.0) -> dict:
    """Load one strobe stack (2x2 binned on loading, a standard choice) and return
    its pole traces, the frame-averaged image and the response map."""
    with open_nwb("000448", asset["asset_id"]) as f:
        info = strobe_info(f)
        s = f["acquisition/StrobeImaging/data"][()].astype(np.float32)
    s = s.reshape(s.shape[0], s.shape[1] // 2, 2, s.shape[2] // 2, 2).mean(axis=(2, 4))
    wc_all = s.mean(axis=(1, 2))
    mean_img = s[wc_all > 0.5 * np.median(wc_all)].mean(axis=0)
    out = {"path": asset["path"], **info, "mean_img": mean_img}
    for p, c in [(pct, cone_deg), (80.0, cone_deg), (90.0, cone_deg), (pct, 30.0), (pct, 60.0)]:
        memb, up, lo = membrane_and_poles(mean_img, p, c)
        tr = pole_traces(s, memb, up, lo)
        out[f"traces_{p:.0f}_{c:.0f}"] = tr
        out[f"npx_{p:.0f}_{c:.0f}"] = (int(memb.sum()), int(up.sum()), int(lo.sum()))
    memb, up, lo = membrane_and_poles(mean_img, pct, cone_deg)
    out["masks"] = (memb, up, lo)
    out["frame_mean"] = wc_all
    return out


def dark_frames(whole: np.ndarray) -> np.ndarray:
    """Frames whose whole-cell signal is below half the median: failed flashes
    (the first frame of most files). Left out; a standard choice."""
    return whole < 0.5 * np.median(whole)


def align_lag(ref: np.ndarray, x: np.ndarray, max_lag: int = 150) -> int:
    """Lag (frames) that best aligns x to ref, by correlation of the mean-removed
    signals; x shifted by the lag (x[i - lag]) matches ref[i]."""
    a = np.nan_to_num(ref - np.nanmean(ref))
    b = np.nan_to_num(x - np.nanmean(x))
    best, lag_best = -np.inf, 0
    for lag in range(-max_lag, max_lag + 1):
        c = np.sum(a * np.roll(b, lag))
        if c > best:
            best, lag_best = c, lag
    return lag_best


def shift(x: np.ndarray, lag: int) -> np.ndarray:
    y = np.full_like(x, np.nan, dtype=float)
    if lag >= 0:
        y[lag:] = x[: len(x) - lag]
    else:
        y[:lag] = x[-lag:]
    return y


def charge_fit(t, v):
    """Least-squares fit of A (1 - exp(-t / tau)) (Fig. 7 legend, single exponential)."""
    from scipy.optimize import curve_fit

    f = lambda t, a, tau: a * (1 - np.exp(-t / tau))
    p, _ = curve_fit(f, t, v, p0=[np.nanmax(v), 200.0], maxfev=20000)
    return p, f(t, *p)


def charge_fit_free(t, v):
    """V0 + (A - V0)(1 - exp(-t / tau)), for pulses that start from a charged membrane."""
    from scipy.optimize import curve_fit

    f = lambda t, a, v0, tau: v0 + (a - v0) * (1 - np.exp(-t / tau))
    p, _ = curve_fit(f, t, v, p0=[np.nanmax(v), v[0] if np.isfinite(v[0]) else 0.0, 200.0], maxfev=20000)
    return p, f(t, *p)


def discharge_fit(t, v):
    """Least-squares fit of A exp(-t / tau) (Fig. 7 legend, single exponential)."""
    from scipy.optimize import curve_fit

    f = lambda t, a, tau: a * np.exp(-t / tau)
    p, _ = curve_fit(f, t, v, p0=[np.nanmax(v), 500.0], maxfev=20000)
    return p, f(t, *p)
