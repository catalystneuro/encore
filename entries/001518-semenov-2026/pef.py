"""Loading and membrane-profile measures for dandiset 001518 (Semenov et al. 2026).

Each NWB file of the dandiset holds one set of 100 strobe images (512 x 512, uint16, 6 Hz)
of a field of CHO cells loaded with Di-8-ANEPPS or FluoVolt, taken 900 ns into 1-us pulses.
The session description gives the dye and the pulse amplitude in volts. The files hold no
cell outlines, field direction, pixel size or field strength in V/cm; these are derived or
assumed below, and each choice says where it comes from.

Sources of the parameters:
- 40 baseline images, then 60 images with the pulse; F0 the mean of the baseline; dF =
  100 x (F - F0) / F0; a 6-pixel-wide trace along the perimeter; 360 points along the
  perimeter; +-5 degree pole arcs: paper, Methods 2.3 (claims file, common method).
- Dark frames (laser misfires, whole-image mean below the midpoint between the darkest
  frame and the set median): excluded. The paper does not mention them; they carry no
  fluorescence, so this is a standard choice that cannot be avoided.
- Background: readings (a) none and (b) the median of cell-free pixels of the same image,
  as in the claims file header (from Methods 2.4, Ca2+ imaging).
- Cell outlines: found by thresholding the baseline image (standard choice, the paper drew
  the trace by hand in MetaMorph). The trace follows the membrane: at each of 360 angles
  from the cell centre, the radius of peak baseline intensity, smoothed over 15 degrees.
- Pixel size: 16 um camera pixel (iXon Ultra 897, Methods 2.3) / 60x objective =
  0.2667 um. Assumption: no other magnification in the light path; it gives a mean
  radius near the 8 um the paper gives for CHO cells (Methods 2.3).
- Charging time constant: tau = 44.5 ns/um x R, the fit through the origin of
  reference [20] (Semenov et al. 2025, doi:10.1016/j.bioelechem.2025.109143, Results),
  as Methods 2.3 says this study used.
- Field strength: the files give volts only; the factor from volts to V/cm is not in the
  paper, in reference [20] or in the dataset. Readings, see FIELD_PER_VOLT.
"""

import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from scipy import ndimage as ndi

DANDISET = "001518"
VERSION = "0.261006.1957"
API = "https://api.dandiarchive.org/api"

PIXEL_UM = 16.0 / 60.0  # assumption, see module docstring
TAU_NS_PER_UM = 44.5  # reference [20]
T_IMAGE_NS = 900.0  # Methods 2.3, 1-us pulses
SENS = {"Di8": 9.1, "FV": 26.0}  # % dF per 100 mV, paper Fig. 3
N_BASE = 40  # Methods 2.3
POLE_HALF_DEG = 5  # Methods 2.3
# Volts to V/cm. Readings (assumptions; the paper gives field strengths only):
# "top": the paper's highest level, 1400 V/cm, is the dataset's highest, 250 V.
# "bottom": the paper's lowest level, 43 V/cm, is the dataset's lowest, 25 V.
FIELD_PER_VOLT = {"top": 1400.0 / 250.0, "bottom": 43.0 / 25.0}
# The field strengths the paper names for the 1-us escalation (claims file header).
PAPER_LEVELS = [43, 150, 230, 360, 570, 780, 1000, 1200, 1400]


def list_assets():
    """Asset paths and ids of the pinned version."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    with urllib.request.urlopen(url) as r:
        res = json.load(r)["results"]
    return [(a["path"], a["asset_id"]) for a in res]


def good_frames(frames):
    """Boolean mask of frames lit by the laser (dark misfire frames are False)."""
    m = frames.reshape(len(frames), -1).mean(1)
    med = np.median(m)
    if m.min() > 0.75 * med:
        return np.ones(len(m), bool)
    return m > (m.min() + med) / 2


def find_cells(base):
    """Cells in a baseline image: list of (cy, cx, mask_radius) and the label image.

    Standard choice: local-contrast threshold at the 90th percentile, filled; objects under
    1500 pixels or closer to the edge than 1.5 radii are left out."""
    s = ndi.gaussian_filter(base, 2) - ndi.gaussian_filter(base, 30)
    m = s > np.percentile(s, 90)
    m = ndi.binary_opening(ndi.binary_fill_holes(ndi.binary_closing(m, iterations=3)), iterations=3)
    lab, n = ndi.label(m)
    out = []
    for i in range(1, n + 1):
        yy, xx = np.nonzero(lab == i)
        if len(yy) < 1500:
            continue
        r = np.sqrt(len(yy) / np.pi)
        cy, cx = yy.mean(), xx.mean()
        if min(cy, cx, 511 - cy, 511 - cx) < 1.5 * r:
            continue
        out.append((cy, cx, r))
    return out, lab


def trace(base, cy, cx, r):
    """Sampling coordinates of the 6-pixel-wide membrane trace at 360 angles.

    Angle 0 is +x (image right), 90 is +y (image down). Returns (Y, X, rmem, area_r):
    rmem the trace radius per angle, area_r the radius of the circle with the area inside
    the trace."""
    th = np.deg2rad(np.arange(360))
    rr = np.arange(0.5 * r, 1.3 * r, 0.5)
    pb = ndi.map_coordinates(base, [cy + np.outer(np.sin(th), rr), cx + np.outer(np.cos(th), rr)], order=1)
    pb = ndi.uniform_filter1d(pb, 15, axis=0, mode="wrap")
    rmem = ndi.uniform_filter1d(rr[pb.argmax(1)], 15, mode="wrap")
    off = np.arange(-2.5, 3.0, 1.0)  # 6 samples 1 px apart
    Y = cy + np.sin(th)[:, None] * (rmem[:, None] + off)
    X = cx + np.cos(th)[:, None] * (rmem[:, None] + off)
    area_r = np.sqrt(np.mean(rmem**2))
    return Y, X, rmem, area_r


def load_set(asset_id):
    """Read one file and reduce it to per-frame membrane profiles of every cell."""
    url = f"{API}/assets/{asset_id}/download/"
    with h5py.File(remfile.File(url), "r") as h:
        desc = h["/session_description"][()].decode()
        start = float(h["/acquisition/StrobeImaging/starting_time"][()])
        subject = h["/general/subject/subject_id"][()].decode()
        frames = h["/acquisition/StrobeImaging/data"][()].astype(np.float32)
    good = good_frames(frames)
    base = frames[:N_BASE][good[:N_BASE]].mean(0)
    cells, lab = find_cells(base)
    free = ~ndi.binary_dilation(lab > 0, iterations=15)
    bg = np.median(frames[:, free], axis=1)
    out = []
    for cy, cx, r in cells:
        Y, X, rmem, area_r = trace(base, cy, cx, r)
        prof = np.stack([ndi.map_coordinates(f, [Y, X], order=1).mean(1) for f in frames])
        out.append(dict(cy=cy, cx=cx, rmem=rmem, perim_r=None, area_r=area_r,
                        perim_len=float(np.sum(np.hypot(np.diff(np.r_[Y[:, 2], Y[0, 2]]),
                                                         np.diff(np.r_[X[:, 2], X[0, 2]])))),
                        prof=prof.astype(np.float32)))
    return dict(asset_id=asset_id, subject=subject, start=start,
                volt=int(re.search(r"at (\d+)V", desc).group(1)),
                dye="FV" if "FluoVolt" in desc else "Di8",
                spacing_mm=float(re.search(r"Distance between electrodes ([\d.]+) mm", desc).group(1)),
                good=good, bg=bg.astype(np.float32), frame_mean=frames.reshape(100, -1).mean(1),
                cells=out, desc=desc)


def load_all(assets=None, threads=16):
    """Load every set of the pinned version (or the given (path, asset_id) list)."""
    assets = assets or list_assets()
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(lambda a: load_set(a[1]), assets))


def track(sets, max_shift=10.0):
    """Group sets by subject in time order and link each set's cells to the cells of the
    subject's first set by nearest centre (within max_shift pixels). Returns
    {subject: (sets_in_order, [[cell index in each set or None] per first-set cell])}."""
    by = {}
    for s in sets:
        by.setdefault(s["subject"], []).append(s)
    out = {}
    for sub, ss in by.items():
        ss = sorted(ss, key=lambda s: s["start"])
        ref = ss[0]["cells"]
        links = []
        for c in ref:
            row = []
            for s in ss:
                d = [np.hypot(c["cy"] - k["cy"], c["cx"] - k["cx"]) for k in s["cells"]]
                row.append(int(np.argmin(d)) if d and min(d) <= max_shift else None)
            links.append(row)
        out[sub] = (ss, links)
    return out


def dF_profile(s, ci, frames=None, background=True):
    """Collapsed dF profile (360 points) of cell ci of set s: mean of the good baseline
    frames against the mean of the given pulse frames (default all 60)."""
    c = s["cells"][ci]
    g = s["good"]
    idx_b = np.arange(N_BASE)[g[:N_BASE]]
    fr = np.arange(N_BASE, 100) if frames is None else np.asarray(frames)
    idx_p = fr[g[fr]]
    P, bg = c["prof"], s["bg"]
    if background:
        F0 = (P[idx_b] - bg[idx_b, None]).mean(0)
        F = (P[idx_p] - bg[idx_p, None]).mean(0)
    else:
        F0 = P[idx_b].mean(0)
        F = P[idx_p].mean(0)
    return 100 * (F - F0) / F0


def per_frame_dF(s, ci, background=True):
    """dF of every frame (100 x 360) against the baseline mean; dark frames are NaN."""
    c = s["cells"][ci]
    g = s["good"]
    P = c["prof"] - (s["bg"][:, None] if background else 0)
    F0 = P[:N_BASE][g[:N_BASE]].mean(0)
    d = 100 * (P - F0) / F0
    d[~g] = np.nan
    return d


def arc(profile, centre_deg, half=POLE_HALF_DEG):
    """Mean of a 360-point profile over centre +- half degrees."""
    idx = (np.arange(-half, half + 1) + int(round(centre_deg))) % 360
    return np.nanmean(profile[..., idx], axis=-1)


def cos_phase(profile):
    """Angle (degrees, image convention) of the maximum of the best-fitting cosine."""
    th = np.deg2rad(np.arange(360))
    a = np.nansum(profile * np.cos(th))
    b = np.nansum(profile * np.sin(th))
    return np.rad2deg(np.arctan2(b, a)) % 360


def impc_mV(E_vcm, R_um, theta_deg):
    """Schwan equation, Eq. (1): IMPC = 1.5 E R cos(theta) (1 - exp(-t/tau)), in mV."""
    tau = TAU_NS_PER_UM * R_um
    return 1.5 * (E_vcm * 100.0) * (R_um * 1e-6) * np.cos(np.deg2rad(theta_deg)) * (1 - np.exp(-T_IMAGE_NS / tau)) * 1e3


def f_factor(lm, R=8e-6, d=5e-9, li=0.4, lo=1.64):
    """Eq. (2) of the paper: the factor that replaces 1.5 for a conducting membrane."""
    num = 3 * lo * (3 * R**2 * d * li + (3 * d**2 * R - d**3) * (lm - li))
    den = 2 * R**3 * (lm + 2 * lo) * (lm + 0.5 * li) - 2 * (R - d) ** 3 * (lo - lm) * (li - lm)
    return num / den


def responding(tracked, min_volt=60, tol_deg=30, frac=0.8):
    """Cells to analyse, per subject: cells found in every set whose fitted cosine phase lies
    within tol_deg of the subject's field direction in at least frac of the sets at or above
    min_volt. The field direction (cathode-facing side, where emission increases: Methods
    2.3) is the circular mean of those phases over the subject's tracked cells; the
    electrodes do not move during an experiment. Standard choice: objects that do not
    polarize along the field (debris, cells out of focus) cannot give a pole value.
    Returns {subject: (sets, rows, cathode_deg, n_tracked)}."""
    out = {}
    for sub, (ss, links) in tracked.items():
        V = np.array([s["volt"] for s in ss])
        full = [row for row in links if all(r is not None for r in row)]
        phs = [np.array([cos_phase(dF_profile(s, ci)) for s, ci in zip(ss, row)]) for row in full]
        allph = np.concatenate([p[V >= min_volt] for p in phs])
        cath = np.rad2deg(np.angle(np.mean(np.exp(1j * np.deg2rad(allph))))) % 360
        keep = [row for row, p in zip(full, phs)
                if np.mean(np.abs((p[V >= min_volt] - cath + 180) % 360 - 180) < tol_deg) >= frac]
        out[sub] = (ss, keep, cath, len(full))
    return out


def pole_rows(resp, background=True):
    """One row per subject, cell and set: pole values and cell geometry.

    dF_* are collapsed profiles (Methods 2.3, Fig. 3 onward); pi_* the mean over the pulse
    images of per-image pole dF (Methods 2.3, Fig. 2 measure); f10_* collapsed from the
    first 10 pulse images (Results 3.4, paragraph 3)."""
    import pandas as pd
    rows = []
    for sub, (ss, keep, cath, _) in resp.items():
        for k, row in enumerate(keep):
            c0 = ss[0]["cells"][row[0]]
            dist = np.hypot(c0["cy"] - 255.5, c0["cx"] - 255.5)
            for s, ci in zip(ss, row):
                c = s["cells"][ci]
                prof = dF_profile(s, ci, background=background)
                f10 = dF_profile(s, ci, frames=np.arange(N_BASE, N_BASE + 10), background=background)
                pf = per_frame_dF(s, ci, background=background)
                rows.append(dict(
                    subject=sub, dye=s["dye"], cell=k, volt=s["volt"], dist_centre_px=dist,
                    R_area_um=c["area_r"] * PIXEL_UM, R_perim_um=c["perim_len"] / (2 * np.pi) * PIXEL_UM,
                    dF_cath=arc(prof, cath), dF_anod=arc(prof, cath + 180),
                    f10_cath=arc(f10, cath), f10_anod=arc(f10, cath + 180),
                    pi_cath=np.nanmean(arc(pf[N_BASE:], cath)), pi_anod=np.nanmean(arc(pf[N_BASE:], cath + 180)),
                    frames_cath=arc(pf, cath), frames_anod=arc(pf, cath + 180),
                    profile=np.roll(prof, -int(round(cath))), cath_deg=cath))
    return pd.DataFrame(rows)


def nearest_sets(volts, k, levels=PAPER_LEVELS, max_rel=0.15):
    """{paper level (V/cm): dataset voltage} for the set whose field (volt x k) is nearest
    each level, within max_rel of it. Standard choice for naming sets by the paper's levels."""
    volts = np.unique(volts)
    out = {}
    for L in levels:
        E = volts * k
        i = int(np.argmin(np.abs(E - L)))
        if abs(E[i] - L) <= max_rel * L:
            out[L] = int(volts[i])
    return out
