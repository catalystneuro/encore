"""Loading and checks for dandiset 002035 (Weible and Wehr 2022, J Alzheimers Dis 89:1385).

The dandiset is a BIDS microscopy dataset of single-channel OME-TIFF images, one channel per
image, with a JSON sidecar per image, a `sub-<id>_scans.tsv` per mouse and `participants.tsv`.
Everything is read from the archive at the pinned version: the asset list and digests from the
version's manifest (`assets.jsonld`), the tables from each asset's S3 URL, and the images by
streaming them with `remfile` and `tifffile`. Nothing is written to disk.

Parameters and where they come from:
- VERSION: the only published version of the dandiset (see the notebook header).
- The pixel sizes per magnification class are the dataset's own (README, "MAGNIFICATION").
- The nucleus-size check (`nucleus_diameter_um`) is a standard choice for checking a spatial
  scale, not a method of the paper: a Gaussian background subtraction (sigma 25 um), an Otsu
  threshold, and the median equivalent diameter of the connected components between 3 and 20 um.
  It is used only to check the dataset's description, never to test a claim.
"""

from __future__ import annotations

import io
import json
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
import remfile
import requests
import tifffile

DANDISET = "002035"
VERSION = "0.261022.1829"
API = "https://api.dandiarchive.org/api"
MANIFEST = f"https://dandiarchive.s3.amazonaws.com/dandisets/{DANDISET}/{VERSION}/assets.jsonld"

# Pixel size per magnification class, from the dataset's README ("MAGNIFICATION").
PIXEL_UM = {"12.5X": 5.16, "100X": 0.645, "200X": 0.3225}

AGES = [14, 21, 30, 45, 60, 90, 120, 150]


def version_metadata() -> dict:
    return requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60).json()


def manifest() -> pd.DataFrame:
    """Every asset of the pinned version: path, size, SHA-256 and S3 URL."""
    rows = []
    for a in requests.get(MANIFEST, timeout=120).json():
        s3 = [u for u in a["contentUrl"] if "s3.amazonaws.com" in u]
        rows.append({"path": a["path"], "size": a["contentSize"],
                     "sha256": a["digest"].get("dandi:sha2-256"), "url": s3[0] if s3 else None})
    return pd.DataFrame(rows)


def read_text(url: str) -> str:
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return r.text


def table(assets: pd.DataFrame, path: str) -> pd.DataFrame:
    return pd.read_csv(io.StringIO(read_text(assets.set_index("path").loc[path, "url"])), sep="\t")


def scans(assets: pd.DataFrame, workers: int = 16) -> pd.DataFrame:
    """All `sub-<id>_scans.tsv` tables, one row per image, with the subject and the run number."""
    paths = assets.loc[assets.path.str.endswith("_scans.tsv"), ["path", "url"]].values

    def one(item):
        path, url = item
        df = pd.read_csv(io.StringIO(read_text(url)), sep="\t")
        df["participant_id"] = path.split("/")[0]
        return df

    with ThreadPoolExecutor(workers) as ex:
        out = pd.concat(list(ex.map(one, paths)), ignore_index=True)
    out["path"] = out.participant_id + "/" + out.filename
    out["run"] = out.filename.str.extract(r"run-(\d+)", expand=False).astype(int)
    return out


def sidecar(assets: pd.DataFrame, image_path: str) -> dict:
    path = image_path.replace(".ome.tif", ".json")
    return json.loads(read_text(assets.set_index("path").loc[path, "url"]))


def image(url: str):
    """One streamed image: the pixel array and the OME physical pixel size (um)."""
    with tifffile.TiffFile(remfile.File(url)) as t:
        arr = t.asarray()
        ome = t.ome_metadata or ""
    size = None
    if 'PhysicalSizeX="' in ome:
        size = float(ome.split('PhysicalSizeX="')[1].split('"')[0])
    return arr, size


def nucleus_diameter_um(arr: np.ndarray, pixel_um: float) -> tuple[float, int]:
    """Median equivalent diameter (um) of bright blobs in a DAPI image, and their number.

    A standard choice for checking the scale of an image (module docstring), not the paper's
    DAPI count."""
    from scipy import ndimage
    from skimage.filters import threshold_otsu

    img = arr.astype(float)
    bg = ndimage.gaussian_filter(img, 25 / pixel_um)
    hp = ndimage.gaussian_filter(img, 0.5 / pixel_um) - bg
    mask = hp > threshold_otsu(hp)
    lab, n = ndimage.label(mask)
    if n == 0:
        return float("nan"), 0
    areas = np.bincount(lab.ravel())[1:] * pixel_um ** 2
    d = 2 * np.sqrt(areas / np.pi)
    keep = d[(d >= 3) & (d <= 20)]
    return (float(np.median(keep)) if len(keep) else float("nan")), int(len(keep))
