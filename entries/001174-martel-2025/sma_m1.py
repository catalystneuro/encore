"""Loading and measures for dandiset 001174 (Martel et al. 2025, iScience 28, 112767).

The dandiset holds, for each imaging session, two NWB files: one for the
"spontaneous" condition and one for the "arm reaching" condition (the
`session_description` says which, and the site). Each file has the miniscope
movie (`acquisition/OnePhotonSeries`), the footprints of the accepted cells
(`PlaneSegmentation/image_mask`), one trace per cell
(`Fluorescence/RoiResponseSeries`, which is the CNMFe denoised trace, not the
raw one: see the notebook's data check) and the deconvolved events as a dense
frame-by-cell array of amplitudes (`EventAmplitude`, zero where there is no
event). There is no trial table and no TTL channel.

Where each parameter comes from:

- Event rate, mean amplitude and IEI CV (method D of the claims file): from
  ReorganizedData_Final.m and ISI_Final.m (Zenodo doi:10.5281/zenodo.14963213).
  The rate is the number of events over the segment duration, which the code
  takes as the time of the segment's last frame from its first; the CV is the
  SD (n - 1) over the mean of the inter-event intervals.
- Z-Jaccard (method J): Methods, "Cell coactivation (Jaccard index method)",
  and permfun.R (doi:10.5281/zenodo.14977106): 0.2 s bins, a bin is 1 when the
  cell has an event in it or in the four bins after, Jaccard per pair, null from
  1000 random circular shifts of one cell's series (the shift drawn uniformly
  from 1..T, Methods), Z = (observed - null mean) / null SD (SD with n - 1, as
  R's sd). In the dandiset the two conditions are separate files, so each file
  is binned on its own; the claims file's rule of dropping the bin that mixes
  the two parts and the last four bins of each part is applied by dropping the
  last four bins of each file (the forward smoothing cannot look past them).
- Distances: centroid pixel distance times 3.2 um (permfun.R). Centroids are
  the footprint-weighted means of `image_mask` (a standard choice; the paper's
  centroids are IDPS's, which the link claim compares).
- Random seeds: fixed per claim in the notebook (a standard choice).
"""

from __future__ import annotations

import functools
import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile

DANDISET = "001174"
VERSION = "0.250331.2218"
API = "https://api.dandiarchive.org/api"

# Zenodo deposits of the paper (key resources table), pinned by record DOI.
ZENODO_DESCRIPTORS = "14727695"   # General descriptors of calcium activity per cell
ZENODO_JACCARD = "15116617"       # Jaccard (Fig. 3) outputs per pair
UM_PER_PIXEL = 3.2                # permfun.R, distmat * 3.2


def list_assets():
    """Assets of the pinned version, with subject, date and condition parsed."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=500"
    with urllib.request.urlopen(url) as r:
        res = json.load(r)["results"]
    rows = []
    for a in res:
        rows.append({"path": a["path"], "asset_id": a["asset_id"], "size": a["size"],
                     "subject": a["path"].split("/")[0][4:]})
    return pd.DataFrame(rows)


def _s3_url(asset_id):
    """The asset's S3 address, from its metadata (contentUrl)."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{asset_id}/"
    with urllib.request.urlopen(url) as r:
        meta = json.load(r)
    return [u for u in meta["contentUrl"] if "s3" in u][0]


def centroids(mask):
    """Footprint-weighted centroid of each mask, in pixels.

    x is along the masks' first spatial axis and y along the second, which is
    how the centroids of the paper's descriptors table (IDPS) correspond to
    them (the notebook's link check).
    """
    m = np.asarray(mask, dtype=float)
    w = m.sum(axis=(1, 2))
    xs, ys = np.mgrid[0:m.shape[1], 0:m.shape[2]]
    cx = (m * xs).sum(axis=(1, 2)) / w
    cy = (m * ys).sum(axis=(1, 2)) / w
    return np.c_[cx, cy]


def load_file(row):
    """Read what the analysis needs from one file: no movie frames are read."""
    f = h5py.File(remfile.File(_s3_url(row["asset_id"])), "r")
    po = f["processing/ophys"]
    ea = po["EventAmplitude/data"][:]
    den = po["Fluorescence/RoiResponseSeries/data"][:]
    mask = po["ImageSegmentation/PlaneSegmentation/image_mask"][:]
    desc = f["session_description"][()].decode()
    out = {
        "path": row["path"], "subject": row["subject"],
        "description": desc,
        "start": f["session_start_time"][()].decode(),
        "region": "SMA" if " SMA " in desc else ("M1" if " M1 " in desc else "?"),
        "condition": "spontaneous" if "spontaneous" in desc else ("task" if "reaching" in desc else "?"),
        "rate_ea": float(po["EventAmplitude/starting_time"].attrs["rate"]),
        "rate_den": float(po["Fluorescence/RoiResponseSeries/starting_time"].attrs["rate"]),
        "rate_movie": float(f["acquisition/OnePhotonSeries/starting_time"].attrs["rate"]),
        "imaging_rate": float(f["general/optophysiology/ImagingPlane/imaging_rate"][()]),
        "movie_shape": f["acquisition/OnePhotonSeries/data"].shape,
        "mask_shape": mask.shape,
        "roi_ids": po["ImageSegmentation/PlaneSegmentation/id"][:],
        "events": ea, "denoised": den,
        "centroid": centroids(mask),
        "mask_hash": hash(mask.tobytes()),
        "indicator": f["general/optophysiology/ImagingPlane/indicator"][()].decode(),
        "location": f["general/optophysiology/ImagingPlane/location"][()].decode(),
        "sex": f["general/subject/sex"][()].decode(),
        "age": f["general/subject/age"][()].decode(),
    }
    out["date"] = out["start"][:10]
    f.close()
    return out


@functools.lru_cache(maxsize=1)
def load_all(threads=12):
    """Load every file of the pinned version (about a minute, streamed)."""
    assets = list_assets()
    with ThreadPoolExecutor(threads) as ex:
        files = list(ex.map(load_file, [r for _, r in assets.iterrows()]))
    return sorted(files, key=lambda x: (x["subject"], x["start"]))


def sessions(files):
    """Pair the spontaneous and task files of each subject, site and date."""
    ses = {}
    for x in files:
        key = (x["subject"], x["region"], x["date"])
        ses.setdefault(key, {})[x["condition"]] = x
    return ses


# ---------------------------------------------------------------- descriptors (method D)

def descriptors(x):
    """Per cell: number of events, rate (events/s), mean amplitude and IEI CV.

    Events are the frames with a non-zero amplitude in `EventAmplitude`. The
    duration is (n_frames - 1) / rate, the time of the last frame from the first,
    as ReorganizedData_Final.m divides by Raw_timing(end) (spontaneous) or by the
    task part's last time minus its first.
    """
    ea = x["events"]
    fs = x["rate_ea"]
    dur = (ea.shape[0] - 1) / fs
    rows = []
    for c in range(ea.shape[1]):
        idx = np.flatnonzero(ea[:, c] > 0)
        amp = ea[idx, c]
        isi = np.diff(idx) / fs
        rows.append({
            "cell": c, "n_events": len(idx), "rate": len(idx) / dur,
            "amplitude": amp.mean() if len(idx) else np.nan,
            "iei_cv": isi.std(ddof=1) / isi.mean() if len(isi) >= 2 else np.nan,
            "duration_s": dur,
        })
    return pd.DataFrame(rows)


def read_zenodo_csv(record, name):
    """Read a CSV of a Zenodo record (fixed by its record DOI) into a frame."""
    with urllib.request.urlopen(f"https://zenodo.org/api/records/{record}") as r:
        meta = json.load(r)
    f = [f for f in meta["files"] if f["key"] == name][0]
    df = pd.read_csv(f["links"]["self"], encoding="latin-1")
    df.columns = [re.sub(r"^\W+", "", c).strip() for c in df.columns]
    return df, f["checksum"]


# ---------------------------------------------------------------- Z-Jaccard (method J)

def binned_logical(x, bin_s=0.2, ahead=4):
    """0.2 s bins of events, forward smoothed over the bin and the `ahead` bins after.

    The last `ahead` bins are dropped, as the smoothing cannot look past them
    (claims file, method J). Returns (bins x cells) of 0/1.
    """
    ea = x["events"]
    fs = x["rate_ea"]
    t = np.arange(ea.shape[0]) / fs
    nb = int(np.floor(t[-1] / bin_s)) + 1
    b = np.minimum((t / bin_s).astype(int), nb - 1)
    y = np.zeros((nb, ea.shape[1]), dtype=np.int8)
    for c in range(ea.shape[1]):
        y[b[ea[:, c] > 0], c] = 1
    ys = y.copy()
    for k in range(1, ahead + 1):
        ys[:-k] |= y[k:]
    return ys[:-ahead] if ahead else ys


def zjaccard(ys, n_shift=1000, rng=None):
    """Jaccard, Z-Jaccard and null of every pair, from all circular shifts at once.

    For a pair (c, c'), the overlap of c with c' shifted by k is the circular
    cross-correlation of the two 0/1 series, computed for every k with an FFT;
    the null takes `n_shift` shifts drawn uniformly from 1..T (Methods). The
    union is n_c + n_c' - overlap, as the counts do not change with a shift.
    Pairs with a cell with no events give NaN (left out, as the code's
    jaccard_calc gives NaN there).
    """
    rng = np.random.default_rng(0) if rng is None else rng
    T, C = ys.shape
    Y = np.fft.rfft(ys.astype(float), axis=0)
    n = ys.sum(axis=0).astype(float)
    out = []
    for i in range(C - 1):
        for j in range(i + 1, C):
            # overlap[k] = sum_t y_i[t] * y_j[(t + k) mod T]
            ov = np.rint(np.fft.irfft(np.conj(Y[:, i]) * Y[:, j], n=T)).astype(float)
            union = n[i] + n[j] - ov
            with np.errstate(invalid="ignore", divide="ignore"):
                jac = ov / union
            k = rng.integers(1, T + 1, size=n_shift) % T
            null = jac[k]
            obs = jac[0]
            sd = np.std(null, ddof=1)
            z = (obs - null.mean()) / sd if sd > 0 else np.nan
            out.append((i, j, obs, z, n[i], n[j]))
    return pd.DataFrame(out, columns=["i", "j", "jaccard", "z", "n_i", "n_j"])


def pair_distances(cent, pairs):
    d = np.hypot(cent[pairs.i, 0] - cent[pairs.j, 0], cent[pairs.i, 1] - cent[pairs.j, 1])
    return d * UM_PER_PIXEL


def bh(p):
    """Benjamini-Hochberg adjusted p-values (NaN kept)."""
    p = np.asarray(p, float)
    out = np.full_like(p, np.nan)
    ok = ~np.isnan(p)
    q = p[ok]
    n = len(q)
    if n == 0:
        return out
    o = np.argsort(q)
    adj = q[o] * n / np.arange(1, n + 1)
    adj = np.minimum.accumulate(adj[::-1])[::-1]
    r = np.empty(n)
    r[o] = np.minimum(adj, 1)
    out[ok] = r
    return out


# ---------------------------------------------------------------- the paper's per-cell table

def zenodo_descriptors():
    """The paper's per-cell descriptors (Zenodo doi:10.5281/zenodo.14727695), cleaned.

    Each row is a cell and condition in the session where the cell was first
    identified (the table holds first occurrences only). `cell` is the 0-based
    index of the accepted cell in the session (column `cells`, C1 = 0).
    """
    z, md5 = read_zenodo_csv(ZENODO_DESCRIPTORS, "Ca_Imaging_dataset_Tidy version.csv")
    z["subject"] = z["Monkey ID"].str.strip().str[-1]
    z["region"] = z["Structure"].str.strip()
    z["date"] = pd.to_datetime(z["Date"].str.strip(), format="%m/%d/%Y").dt.strftime("%Y-%m-%d")
    z["cell"] = z["cells"].str.strip().str[1:].astype(int) - 1
    z["condition"] = z["Condition"].str.strip().map({"Spontaneous": "spontaneous", "Reaching task": "task"})
    return z, md5


def descriptor_table(files):
    """Method D for every cell of every file, with its centroid."""
    rows = []
    for x in files:
        d = descriptors(x)
        d["subject"], d["region"], d["date"], d["condition"] = x["subject"], x["region"], x["date"], x["condition"]
        d["cx"], d["cy"] = x["centroid"][:, 0], x["centroid"][:, 1]
        rows.append(d)
    return pd.concat(rows, ignore_index=True)
