"""Loading and axon measures for the corpus callosum TEM images of dandiset 001350.

Iram, Garcia et al. (2024), PNAS 121(12) e2307250121, doi:10.1073/pnas.2307250121.

The dandiset is a BIDS microscopy dataset, not NWB: 8-bit PNG images of adult corpus callosum
(8000x TEM) from 5 SRF-Flox ("WT") and 5 SRF-cKO ("KO") mice (participants.tsv), with manual
segmentation masks under derivatives/labels for some of the images. Files are streamed from the
archive at the pinned version into memory; nothing is written to disk.

Masks (derivatives/labels): `seg-axonmyelin` holds axon (255, or 254 in one file) and myelin
(127, a few pixels 126) of myelinated fibres; `seg-uaxon` holds unmyelinated axons (255). Their
description says they are AxonDeepSeg pseudo-labels corrected by hand, made for a later
segmentation project, not the paper's own scoring.

Where the parameters come from:

- Pixel size, 0.00493 um, from each subject's `sub-<id>_TEM.json` (`PixelSize`, `PixelSizeUnits`);
  the claims' criteria (fig2d) take the image scale from the dataset's metadata.
- Using the masks in place of the paper's hand scoring is reading O1 of the claims file
  (claims/001350/10.1073-pnas.2307250121.yaml, opening comment); readings O2 to O7 are named
  there and each is computed here: O2 pooled or per-image percent myelinated, O3 pooled or
  per-image density, O4 objects cut by the image edge left out or kept, O5 equivalent-circle
  or minimum Feret diameter, O6 all myelinated axons or 100 drawn at random per mouse, O7
  Student or Welch t test.
- Myelin is assigned to its axon by a watershed of the fibre mask (axon plus myelin) from the
  axon objects, on the distance transform; this is how AxonDeepSeg's morphometrics separate
  touching fibres. A standard choice: the paper measured each fibre by hand with a line.
- Objects smaller than `MIN_OBJECT_PX` pixels (0.0005 um2, a disc of 25 nm) are dropped as mask
  specks; a standard choice, and the number dropped is reported.
- Objects are 4-connected components (`CONNECTIVITY = 1`), so that two masks touching at a
  corner count as two; a standard choice.
- The minimum Feret diameter is the smallest caliper width of the convex hull of the object's
  pixel centres, over 1 degree steps, plus one pixel; a standard choice.
- `RANDOM_SEED` for reading O6(b); a detail that cannot change an outcome, and the spread over
  100 draws is shown in the notebook.
"""

from __future__ import annotations

import io
from functools import lru_cache

import numpy as np
import pandas as pd
import requests
from PIL import Image, PngImagePlugin
from scipy import ndimage
from scipy.spatial import ConvexHull, QhullError
from skimage.measure import label, regionprops
from skimage.segmentation import watershed

DANDISET_ID = "001350"
DANDISET_VERSION = "0.250511.1527"
API = "https://api.dandiarchive.org/api"

MIN_OBJECT_PX = 20
CONNECTIVITY = 1
RANDOM_SEED = 1350
N_PER_MOUSE = 100          # Figure 2E legend: "the average of 100 myelinated axons from one animal"
FERET_ANGLES = np.deg2rad(np.arange(0, 180, 1.0))

Image.MAX_IMAGE_PIXELS = None


@lru_cache(maxsize=1)
def assets() -> pd.DataFrame:
    """Every asset of the pinned version: path, size and download URL."""
    rows, url = [], f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    while url:
        page = requests.get(url, timeout=60)
        page.raise_for_status()
        page = page.json()
        rows += page["results"]
        url = page["next"]
    df = pd.DataFrame(rows)[["path", "size", "asset_id"]]
    df["url"] = [f"{API}/assets/{a}/download/" for a in df.asset_id]
    return df.sort_values("path").reset_index(drop=True)


def version_metadata() -> dict:
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/", timeout=60)
    r.raise_for_status()
    return r.json()


def asset_metadata(asset_id: str) -> dict:
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/{asset_id}/",
                     timeout=60)
    r.raise_for_status()
    return r.json()


def _bytes(path: str) -> bytes:
    url = assets().set_index("path").loc[path, "url"]
    r = requests.get(url, timeout=300)
    r.raise_for_status()
    return r.content


def read_text(path: str) -> str:
    return _bytes(path).decode()


def read_tsv(path: str) -> pd.DataFrame:
    return pd.read_csv(io.StringIO(read_text(path)), sep="\t")


def read_png(path: str) -> np.ndarray:
    """A PNG streamed into memory. Grey with alpha is returned as its grey channel.

    The dataset's images and masks are themselves PNG files; they are decoded with PIL's PNG
    plugin from the bytes streamed from the archive."""
    im = np.array(PngImagePlugin.PngImageFile(io.BytesIO(_bytes(path))))
    if im.ndim == 3:
        im = im[..., 0]
    return im


def images() -> pd.DataFrame:
    """One row per raw image, with its subject, sample, size on the archive and its masks."""
    a = assets()
    raw = a[a.path.str.startswith("sub-") & a.path.str.endswith("_TEM.png")].copy()
    raw["subject"] = raw.path.str.extract(r"^(sub-[^/]+)/")[0]
    raw["sample"] = raw.path.str.extract(r"_(sample-[^/]+)_TEM\.png$")[0]
    labels = a[a.path.str.startswith("derivatives/labels/") & a.path.str.endswith(".png")]
    for kind in ["axonmyelin", "uaxon", "nuclei", "process"]:
        paths = {p.split("/")[-1].replace(f"_seg-{kind}-manual.png", ".png"): p
                 for p in labels.path if f"_seg-{kind}-manual" in p}
        raw[kind] = [paths.get(p.split("/")[-1]) for p in raw.path]
    return raw.reset_index(drop=True)


def pixel_size_um(subject: str) -> float:
    import json
    meta = json.loads(read_text(f"{subject}/micr/{subject}_TEM.json"))
    assert meta["PixelSizeUnits"] == "um" and meta["PixelSize"][0] == meta["PixelSize"][1]
    return float(meta["PixelSize"][0])


def split_axonmyelin(mask: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Axon and myelin masks from an axonmyelin label image (axon 254 or 255, myelin 126 or 127)."""
    return mask >= 200, (mask >= 100) & (mask < 200)


def min_feret(coords: np.ndarray) -> float:
    """Smallest caliper width (pixels) of the convex hull of pixel centres, plus one pixel."""
    pts = coords.astype(float)
    try:
        pts = pts[ConvexHull(pts).vertices]
    except (QhullError, ValueError):
        pass
    proj = pts @ np.stack([np.cos(FERET_ANGLES), np.sin(FERET_ANGLES)])
    return float((proj.max(0) - proj.min(0)).min() + 1.0)


def _touches_edge(bbox, shape) -> bool:
    r0, c0, r1, c1 = bbox
    return r0 == 0 or c0 == 0 or r1 == shape[0] or c1 == shape[1]


def measure_image(axonmyelin: np.ndarray, uaxon: np.ndarray, px_um: float) -> dict:
    """Objects of one image's masks.

    Returns a dict with `myelinated` (one row per myelinated axon: diameters in nm under both
    readings of O5, g-ratio, myelin thickness, whether the axon or its fibre touches the image
    edge), `unmyelinated` (one row per unmyelinated axon object), the image area in um2, and
    counts of what was dropped.
    """
    axon, myelin = split_axonmyelin(axonmyelin)
    shape = axon.shape
    ax_lab = label(axon, connectivity=CONNECTIVITY)
    sizes = np.bincount(ax_lab.ravel())
    small = np.flatnonzero(sizes < MIN_OBJECT_PX)
    small = small[small > 0]
    ax_lab[np.isin(ax_lab, small)] = 0
    fibre = (ax_lab > 0) | myelin
    dist = ndimage.distance_transform_edt(fibre)
    fib_lab = watershed(-dist, markers=ax_lab, mask=fibre)
    fib_props = {p.label: p for p in regionprops(fib_lab)}
    nm = px_um * 1000.0
    rows = []
    for p in regionprops(ax_lab):
        f = fib_props[p.label]
        a_d = 2 * np.sqrt(p.area / np.pi)
        f_d = 2 * np.sqrt(f.area / np.pi)
        a_fer = min_feret(p.coords)
        f_fer = min_feret(f.coords)
        rows.append({
            "axon_area_px": p.area, "fibre_area_px": f.area, "myelin_px": f.area - p.area,
            "axon_d_eq_nm": a_d * nm, "fibre_d_eq_nm": f_d * nm,
            "axon_d_feret_nm": a_fer * nm, "fibre_d_feret_nm": f_fer * nm,
            "axon_edge": _touches_edge(p.bbox, shape), "fibre_edge": _touches_edge(f.bbox, shape),
        })
    my = pd.DataFrame(rows)
    for r in ["eq", "feret"]:
        my[f"g_{r}"] = my[f"axon_d_{r}_nm"] / my[f"fibre_d_{r}_nm"]
        my[f"thick_{r}_nm"] = (my[f"fibre_d_{r}_nm"] - my[f"axon_d_{r}_nm"]) / 2
    u_lab = label(uaxon > 0, connectivity=CONNECTIVITY)
    u_rows = [{"area_px": p.area, "d_eq_nm": 2 * np.sqrt(p.area / np.pi) * nm,
               "edge": _touches_edge(p.bbox, shape)}
              for p in regionprops(u_lab) if p.area >= MIN_OBJECT_PX]
    n_u_all = int(u_lab.max())
    return {
        "myelinated": my,
        "unmyelinated": pd.DataFrame(u_rows),
        "area_um2": shape[0] * shape[1] * px_um ** 2,
        "shape": shape,
        "axon_specks_dropped": int(len(small)),
        "uaxon_specks_dropped": n_u_all - len(u_rows),
        "axons_without_myelin": int((my.myelin_px == 0).sum()) if len(my) else 0,
        "overlap_px": int(((axon | myelin) & (uaxon > 0)).sum()),
        "myelin_unassigned_px": int((myelin & (fib_lab == 0)).sum()),
        "myelin_px": int(myelin.sum()),
    }


def per_image_counts(measures: dict, keep_edge: bool) -> dict:
    """Counts for percent myelinated and density in one image, under reading O4."""
    my, un = measures["myelinated"], measures["unmyelinated"]
    if not keep_edge:
        my = my[~my.fibre_edge]
        un = un[~un.edge]
    return {"n_myelinated": len(my), "n_unmyelinated": len(un), "area_um2": measures["area_um2"]}


def phase_peak(a: np.ndarray, b: np.ndarray, step: int = 4) -> tuple[float, tuple[int, int]]:
    """Peak of the phase correlation of two images (cropped to a common shape, every `step`
    pixels), and its shift. Near 1 when one image holds a shifted copy of part of the other,
    near 0 for unrelated images; used to look for images deposited twice or overlapping."""
    h, w = min(a.shape[0], b.shape[0]), min(a.shape[1], b.shape[1])
    a = a[:h:step, :w:step].astype(float)
    b = b[:h:step, :w:step].astype(float)
    a, b = a - a.mean(), b - b.mean()
    fa, fb = np.fft.rfft2(a), np.fft.rfft2(b)
    cross = fa * np.conj(fb)
    corr = np.fft.irfft2(cross / (np.abs(cross) + 1e-12), s=a.shape)
    i = np.unravel_index(np.argmax(corr), corr.shape)
    return float(corr[i]), (int(i[0]) * step, int(i[1]) * step)


def mouse_percent_and_density(counts: pd.DataFrame) -> pd.DataFrame:
    """Per mouse, readings O2 (a) pooled, (b) mean of images and O3 (a) pooled, (b) mean of images.

    `counts` has one row per image with subject, n_myelinated, n_unmyelinated, area_um2.
    """
    c = counts.assign(total=counts.n_myelinated + counts.n_unmyelinated)
    c = c.assign(pct=100 * c.n_myelinated / c.total, dens=c.n_myelinated / c.area_um2)
    g = c.groupby("subject")
    return pd.DataFrame({
        "images": g.size(),
        "axons_counted": g.total.sum(),
        "area_um2": g.area_um2.sum(),
        "pct_pooled_O2a": 100 * g.n_myelinated.sum() / g.total.sum(),
        "pct_image_mean_O2b": g.pct.mean(),
        "dens_pooled_O3a": g.n_myelinated.sum() / g.area_um2.sum(),
        "dens_image_mean_O3b": g.dens.mean(),
    })


def mouse_morphometry(axons: pd.DataFrame, diameter: str, keep_edge: bool, sample: bool,
                      rng: np.random.Generator | None = None) -> pd.DataFrame:
    """Per mouse mean g-ratio, myelin thickness and axon diameter of myelinated axons.

    diameter: "eq" or "feret" (O5); keep_edge (O4); sample: 100 at random per mouse (O6 b) or
    all (O6 a). Axons with no myelin assigned are left out, as they have no g-ratio.
    """
    a = axons[axons.myelin_px > 0]
    if not keep_edge:
        a = a[~a.fibre_edge]
    out = {}
    for subject, grp in a.groupby("subject"):
        if sample:
            take = min(N_PER_MOUSE, len(grp))
            grp = grp.iloc[rng.choice(len(grp), size=take, replace=False)]
        out[subject] = {"n_axons": len(grp), "g_ratio": grp[f"g_{diameter}"].mean(),
                        "myelin_thickness_nm": grp[f"thick_{diameter}_nm"].mean(),
                        "axon_diameter_nm": grp[f"axon_d_{diameter}_nm"].mean()}
    return pd.DataFrame(out).T
