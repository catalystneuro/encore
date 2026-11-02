"""Loading and c-Fos cell counts for dandiset 001362 (Bakalar et al. 2023, J Neuroendocrinol,
doi:10.1111/jne.13286).

The dandiset is a BIDS derivative dataset, not NWB. Per hemisphere (sample) it holds the
deconvolved, N4-corrected light-sheet stack, the registered atlas label image (`AtlasLabel`,
and for 16 of 22 hemispheres `AtlasLabelMasked`, the labels inside the hemisphere mask), the FRST
image, binary FRST segmentations at several thresholds (`acq-<threshold>`), atlas-space heatmaps,
and, for 13 hemispheres only, per-region cell counts at each threshold
(`FastRadialSymmetryTransformSegmentationCounts`, columns label_id, name, acronym, cell_count,
label_volume_pixels). Everything is streamed from the archive at the pinned version; nothing is
written to disk.

Where the parameters come from:

- Counting follows the Supplemental Methods, "Cell counting": "connected components were used to
  analyze potential cells. For any connected object to be considered a 'cell', its volume was
  chosen to be within 9 and 900 voxels ... Any cell residing on the boundary of two or more labels
  was assigned to the label which contained the highest proportion of the cell volume."
  (`VMIN`, `VMAX`, `assign by majority label`). The connectivity is not stated; 26-connectivity
  (`CONNECTIVITY`) is the 3-D default of MATLAB's bwconncomp, the tool of the CATNIP binaries
  (Supplemental Methods, "Atlas alignment"); with it, counting every component reproduces the
  dataset's own count tables to about 1% per region (shown in the notebook). The counts are also returned without the size rule
  (`all components`), the reading that matches the dataset's count tables.
- Counting is done in slabs of `CORE` z-planes with `OVERLAP` planes on each side, so that the
  volume never has to be held in memory. A component is counted in the slab where its first plane
  lies; a component that reaches the edge of the extended slab (which takes more than `OVERLAP`
  planes) cannot be measured and is dropped. This is a computational choice that changes no count
  of components of at most `OVERLAP` planes (cells are under 900 voxels); the notebook checks it
  against scipy.ndimage.label on a synthetic volume. The number dropped is counted in pieces, an
  upper bound on the components dropped.
- The labels counted on are `AtlasLabelMasked` where the dataset has it, else `AtlasLabel`: CATNIP.sh
  (commit 4fb92da, the code the paper links) counts on `atlaslabel_def_origspace_masked`, and the
  region volumes of the dataset's count tables equal the voxel counts of `AtlasLabelMasked`
  (shown in the notebook). With `unmasked`, the counts on the unmasked `AtlasLabel` are returned
  too, from the same pass, so that every hemisphere can be counted on the same kind of label image.
- Thresholds: the FRST threshold the paper used is not stated ("An expert user determined which
  threshold(s) to use", Supplemental Methods, "Segmentation") and the dataset does not mark one.
  `THRESHOLDS` are the five thresholds the segmentations of all 22 hemispheres share. The claims
  file (fig5-dg-fos, reading 1) asks for every threshold the derivatives hold: 14000 to 40000,
  which 18 hemispheres hold, and 2000, 3000, 5000, 7000, 9000 and 11000, which the other 4 hold,
  are counted by passing them to `count_hemisphere` (`HIGH_THRESHOLDS`).
"""

from __future__ import annotations

import io
import re
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache

import numpy as np
import pandas as pd
import remfile
import requests
import tifffile

DANDISET_ID = "001362"
DANDISET_VERSION = "0.260923.2152"
API = "https://api.dandiarchive.org/api"

THRESHOLDS = (4000, 6000, 8000, 10000, 12000)
HIGH_THRESHOLDS = tuple(range(14000, 40001, 2000))
VMIN, VMAX = 9, 900          # Supplemental Methods, "Cell counting"
CONNECTIVITY = 26            # assumption, see docstring
CORE, OVERLAP = 96, 48       # slab size in z-planes (computational choice)
NLAB = 65536
THREADS = 2                  # decoding threads per process


@lru_cache(maxsize=1)
def assets() -> dict:
    """Path -> asset record of every asset of the pinned version."""
    out, url = {}, f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    while url:
        r = requests.get(url, timeout=60).json()
        out.update({a["path"]: a for a in r["results"]})
        url = r["next"]
    return out


def asset_url(path: str) -> str:
    """S3 URL of an asset (the API's download endpoint redirects there)."""
    a = assets()[path]
    r = requests.head(f"{API}/assets/{a['asset_id']}/download/", allow_redirects=True, timeout=60)
    return r.url


def read_text(path: str) -> bytes:
    return requests.get(asset_url(path), timeout=120).content


def read_tsv(path: str) -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(read_text(path)), sep="\t", encoding="latin1")


def open_tiff(path: str) -> tifffile.TiffFile:
    return tifffile.TiffFile(remfile.File(asset_url(path)))


def samples() -> pd.DataFrame:
    """One row per hemisphere: subject, hemisphere, genotype, and which derivatives exist."""
    s = read_tsv("samples.tsv")
    s["subject"] = s.participant_id.str.replace("sub-", "", regex=False)
    s["hemisphere"] = s.sample_id.str.replace("sample-", "", regex=False).str.replace("Hemisphere", "")
    s["genotype"] = s.pathology.map({"PACAP_fl/fl": "flox", "PACAPko": "ko"})
    paths = list(assets())
    def has(prefix, sub, hem):
        return any(p.startswith(prefix) and f"sub-{sub}_sample-{hem}Hemisphere" in p for p in paths)
    s["atlas_masked"] = [has("derivatives/AtlasLabelMasked/", r.subject, r.hemisphere) for r in s.itertuples()]
    s["count_tables"] = [has("derivatives/FastRadialSymmetryTransformSegmentationCounts/", r.subject, r.hemisphere)
                         for r in s.itertuples()]
    s["seg_thresholds"] = [sorted(seg_paths(r.subject, r.hemisphere)) for r in s.itertuples()]
    return s[["subject", "hemisphere", "genotype", "atlas_masked", "count_tables", "seg_thresholds"]] \
        .sort_values(["genotype", "subject", "hemisphere"]).reset_index(drop=True)


def seg_paths(sub: str, hem: str) -> dict:
    out = {}
    for p in assets():
        m = re.search(rf"FastRadialSymmetryTransformSegmentation/sub-{sub}/micr/sub-{sub}_sample-{hem}Hemisphere_acq-(\d+)_SPIM", p)
        if m:
            out[int(m[1])] = p
    return out


def count_table_paths(sub: str, hem: str) -> dict:
    out = {}
    for p in assets():
        m = re.search(rf"SegmentationCounts/sub-{sub}/micr/sub-{sub}_sample-{hem}Hemisphere_acq-(\d+)_SPIM\.tsv", p)
        if m:
            out[int(m[1])] = p
    return out


def label_path(sub: str, hem: str, masked: bool = True) -> str:
    kind = "AtlasLabelMasked" if masked else "AtlasLabel"
    p = f"derivatives/{kind}/sub-{sub}/micr/sub-{sub}_sample-{hem}Hemisphere_space-orig_dseg.ome.btf"
    if p not in assets():
        if masked:
            return label_path(sub, hem, masked=False)
        raise KeyError(p)
    return p


def _bbox(seg: np.ndarray, lab_any: np.ndarray):
    """In-plane bounding box of the voxels that are labelled or segmented; cropping to it changes
    no component."""
    m = lab_any | seg.any(axis=0)
    if not m.any():
        return None
    y = np.flatnonzero(m.any(axis=1))
    x = np.flatnonzero(m.any(axis=0))
    return y[0], y[-1] + 1, x[0], x[-1] + 1


def _components(seg: np.ndarray, labs: list, box, a: int, z0: int, z1: int, b: int, nz: int):
    """Components of one extended slab (`seg`, cropped to `box`; `labs` a list of (label image,
    y offset, x offset), each cropped to its labelled area) whose first plane is in [z0, z1). Returns, per label image, (label, size) pairs, and
    the number of pieces dropped for reaching the slab edge.

    A piece that does not touch the first or last plane of the extended slab is a whole component
    (its neighbours all lie in the slab), so every kept count is exact. A component that reaches
    the edge is dropped; it can appear as more than one piece in a slab and in more than one slab,
    so `dropped` counts pieces and is an upper bound on the components dropped."""
    import cc3d
    y0, y1, x0, x1 = box
    cc = cc3d.connected_components(np.ascontiguousarray(seg[:, y0:y1, x0:x1]), connectivity=CONNECTIVITY)
    flat = cc.ravel()
    idx = np.flatnonzero(flat)
    if idx.size and idx[-1] < 2 ** 31:                     # int32 indices halve the memory of a dense slab
        idx = idx.astype(np.int32)
    empty = [np.zeros((0, 2), np.int64) for _ in labs]
    if idx.size == 0:
        return empty, 0
    ids = flat[idx].astype(np.int32)
    del cc, flat
    ny, nx = y1 - y0, x1 - x0
    plane = ny * nx
    u, first = np.unique(ids, return_index=True)          # idx is sorted, so first = lowest plane
    _, last_r = np.unique(ids[::-1], return_index=True)
    zmin = idx[first] // plane
    zmax = idx[len(idx) - 1 - last_r] // plane
    keep = (zmin + a >= z0) & (zmin + a < z1)
    edge = ((zmin == 0) & (a > 0)) | ((zmax == seg.shape[0] - 1) & (b < nz))
    dropped = int((keep & edge).sum())
    keep &= ~edge
    kept_ids = u[keep]
    if kept_ids.size == 0:
        return empty, dropped
    sel = np.isin(ids, kept_ids)
    ids_k = ids[sel]
    i = idx[sel]
    zz, rem = np.divmod(i, plane)
    yy, xx = np.divmod(rem, nx)
    size_all = np.bincount(ids_k)
    out = []
    for lab, ly0, lx0 in labs:
        Y, X = yy + y0 - ly0, xx + x0 - lx0                # label images are cropped to their labels
        inside = (Y >= 0) & (Y < lab.shape[1]) & (X >= 0) & (X < lab.shape[2])
        lv = np.zeros(len(zz), np.int64)
        lv[inside] = lab[zz[inside], Y[inside], X[inside]]
        key = ids_k.astype(np.int64) * NLAB + lv
        del lv, inside, Y, X
        k, c = np.unique(key, return_counts=True)
        cid, cl = k // NLAB, k % NLAB
        order = np.lexsort((-c, cid))                      # largest overlap first within component
        cid, cl = cid[order], cl[order]
        firsts = np.r_[True, cid[1:] != cid[:-1]]
        comp, comp_lab = cid[firsts], cl[firsts]
        out.append(np.c_[comp_lab, size_all[comp]])
    return out, dropped


def count_slabs(read_labs: list, read_seg: dict, nz: int, core: int = CORE, overlap: int = OVERLAP) -> dict:
    """Count components per label in slabs. `read_labs` are functions (planes) -> label array, one
    per label image; `read_seg` maps threshold -> function (planes) -> binary array. Returns, per
    label image k, `volume`[k] (voxels per label) and, per threshold, `all`[k][t] and `sized`[k][t]
    (component counts per label without and with the 9 to 900 voxel rule); per threshold `dropped`
    (pieces reaching the slab edge, see `_components`) and `n_components` (all, within 9 to 900,
    below 9, above 900; on the first label image)."""
    nl = len(read_labs)
    volume = [np.zeros(NLAB, np.int64) for _ in range(nl)]
    pairs = {t: [[] for _ in range(nl)] for t in read_seg}
    dropped = {t: 0 for t in read_seg}
    for z0 in range(0, nz, core):
        z1 = min(z0 + core, nz)
        a, b = max(0, z0 - overlap), min(nz, z1 + overlap)
        labs, lab_any = [], None
        for k, rd in enumerate(read_labs):
            lab = rd(range(a, b))
            any_k = np.zeros(lab.shape[1:], bool)
            for zp in range(lab.shape[0]):
                any_k |= lab[zp] > 0
                if a + zp >= z0 and a + zp < z1:
                    volume[k] += np.bincount(lab[zp].ravel(), minlength=NLAB)
            lab_any = any_k if lab_any is None else lab_any | any_k
            if any_k.any():                                # crop to the labelled area (all zero outside)
                y = np.flatnonzero(any_k.any(axis=1)); x = np.flatnonzero(any_k.any(axis=0))
                labs.append((lab[:, y[0]:y[-1] + 1, x[0]:x[-1] + 1].copy(), y[0], x[0]))
            else:
                labs.append((lab[:, :0, :0].copy(), 0, 0))
            del lab
        for t, rd in read_seg.items():
            seg = rd(range(a, b))
            box = _bbox(seg, lab_any)
            if box is not None:
                p, d = _components(seg, labs, box, a, z0, z1, b, nz)
                for k in range(nl):
                    pairs[t][k].append(p[k])
                dropped[t] += d
            del seg
        del labs
    out = {"volume": volume, "dropped": dropped, "all": [{} for _ in range(nl)],
           "sized": [{} for _ in range(nl)], "n_components": {}}
    for t in read_seg:
        for k in range(nl):
            p = np.concatenate(pairs[t][k]) if pairs[t][k] else np.zeros((0, 2), np.int64)
            ok = (p[:, 1] >= VMIN) & (p[:, 1] <= VMAX)
            out["all"][k][t] = np.bincount(p[:, 0], minlength=NLAB)
            out["sized"][k][t] = np.bincount(p[ok, 0], minlength=NLAB)
            if k == 0:
                out["n_components"][t] = (len(p), int(ok.sum()), int((p[:, 1] < VMIN).sum()), int((p[:, 1] > VMAX).sum()))
    return out


def count_hemisphere(sub: str, hem: str, thresholds=THRESHOLDS, unmasked: bool = False,
                     zlimit: int | None = None) -> dict:
    """Recount cells per atlas label from the binary segmentations of one hemisphere.

    Returns a dict with `volume` (voxels per label, length NLAB), and per threshold `all` and
    `sized` (component counts per label, without and with the 9 to 900 voxel rule), `dropped`
    (pieces of components taller than the slab overlap) and `n_components` (all, within 9 to 900,
    below 9, above 900), on the labels of `label_path` (masked where the dataset has them). With
    `unmasked`, also `volume_u`, `all_u` and `sized_u` on the unmasked `AtlasLabel` (the same
    image where no masked one exists)."""
    lp = label_path(sub, hem)
    paths = [lp]
    lu = label_path(sub, hem, masked=False)
    if unmasked and lu != lp:
        paths.append(lu)
    tfs = [open_tiff(p) for p in paths]
    segs = seg_paths(sub, hem)
    seg_tf = {t: open_tiff(segs[t]) for t in thresholds}
    nz = len(tfs[0].pages) if zlimit is None else zlimit
    r = count_slabs([lambda k, tf=tf: tf.asarray(key=k, maxworkers=THREADS) for tf in tfs],
                    {t: (lambda k, tf=tf: tf.asarray(key=k, maxworkers=THREADS)) for t, tf in seg_tf.items()}, nz)
    out = {"volume": r["volume"][0], "all": r["all"][0], "sized": r["sized"][0],
           "dropped": r["dropped"], "n_components": r["n_components"]}
    if unmasked:
        k = len(paths) - 1
        out.update(volume_u=r["volume"][k], all_u=r["all"][k], sized_u=r["sized"][k])
    return out


def _count_job(args):
    sub, hem, thresholds, unmasked = args
    return (sub, hem), count_hemisphere(sub, hem, thresholds, unmasked)


def count_all(hemis, thresholds=THRESHOLDS, workers: int = 2, unmasked: bool = False) -> dict:
    """count_hemisphere for a list of (subject, hemisphere), in parallel processes. `thresholds` is
    one tuple for every hemisphere or a dict (subject, hemisphere) -> tuple."""
    jobs = [(s, h, tuple(thresholds[(s, h)] if isinstance(thresholds, dict) else thresholds), unmasked)
            for s, h in hemis]
    with ProcessPoolExecutor(workers) as ex:
        return dict(ex.map(_count_job, jobs))


# ---------------------------------------------------------------------------------------------
# Regions and statistics (Supplemental Methods, "Statistical analysis")

def regions() -> pd.DataFrame:
    """The atlas labels (derivatives/AtlasLabel/dseg.tsv) with the paper's exclusions marked.

    Supplemental Methods: "After excluding white matter tracts, nerves, and ventricles, 462
    regions remained. The cerebellum was excluded ... The SPVI was also excluded ... Finally, layer
    1 regions were excluded ... The total number of regions included in this analysis is 431."
    The dataset's label table has no hierarchy, so the groups are read from it as follows (an
    assumption; the paper does not list the regions): tracts and nerves are the labels with the
    Allen fibre-tract colour #cccccc, ventricles those with #aaaaaa, the cerebellum the vermal,
    hemispheric and nuclear labels (Allen colours #f0f280, #f0f180, #f0f052), layer 1 the labels
    whose name ends in "layer_1" and NLOT1 (the molecular layer, layer 1, of the NLOT). The
    catch-all labels root and grey (Basic cell groups and regions) are not regions and are left out.
    """
    d = read_tsv("derivatives/AtlasLabel/dseg.tsv").rename(columns={"index": "label_id", "abbreviation": "acronym"})
    d["tract_or_nerve"] = d.color.eq("#cccccc")
    d["ventricle"] = d.color.eq("#aaaaaa")
    d["cerebellum"] = d.color.isin(["#f0f280", "#f0f180", "#f0f052"])
    d["layer1"] = d.name.str.contains(r"[Ll]ayer_1$", regex=True) | d.acronym.eq("NLOT1")
    d["spvi"] = d.acronym.eq("SPVI")
    d["catch_all"] = d.acronym.isin(["root", "grey"])
    d["included"] = ~(d.tract_or_nerve | d.ventricle | d.cerebellum | d.layer1 | d.spvi | d.catch_all)
    return d


def iqr_keep(x: np.ndarray) -> np.ndarray:
    """Supplemental Methods: outliers "more than 1.5 IQR below Q1 or more than 1.5 IQR above Q3".
    Quartiles by numpy's default (linear) interpolation, a standard choice."""
    if x.size == 0:
        return np.zeros(0, bool)
    q1, q3 = np.nanpercentile(x, [25, 75])
    r = q3 - q1
    return (x >= q1 - 1.5 * r) & (x <= q3 + 1.5 * r)


def region_tests(values: pd.DataFrame, genotype: pd.Series, iqr: str = "within",
                 alpha: float = 0.05) -> pd.DataFrame:
    """Per region (column of `values`, rows are hemispheres): IQR outlier removal, two-sided exact
    Mann-Whitney U of PACAPko against PACAP fl/fl (U of the PACAPko sample), PACAPko as % of
    PACAP fl/fl by ratio of means and of medians, and Benjamini-Krieger-Yekutieli two-stage
    adjustment over the regions tested (statsmodels "fdr_tsbky")."""
    from scipy.stats import mannwhitneyu
    from statsmodels.stats.multitest import multipletests
    ko_rows = genotype.values == "ko"
    rows = []
    for reg in values.columns:
        x = values[reg].values.astype(float)
        ok = np.isfinite(x)
        if iqr == "within":
            for g in (ko_rows, ~ko_rows):
                m = ok & g
                if m.sum() > 0:
                    ok[m] = iqr_keep(x[m])
        elif iqr == "pooled":
            ok[ok] = iqr_keep(x[ok])
        ko, fl = x[ok & ko_rows], x[ok & ~ko_rows]
        if len(ko) < 2 or len(fl) < 2:
            continue
        if np.all(np.r_[ko, fl] == ko[0]):
            u, p = len(ko) * len(fl) / 2, 1.0
        else:
            r = mannwhitneyu(ko, fl, alternative="two-sided", method="exact")
            u, p = r.statistic, r.pvalue
        rows.append(dict(region=reg, n_ko=len(ko), n_flox=len(fl), out_ko=int(ko_rows.sum() - len(ko) - (~np.isfinite(x) & ko_rows).sum()),
                         out_flox=int((~ko_rows).sum() - len(fl) - (~np.isfinite(x) & ~ko_rows).sum()),
                         U=u, p=p, mean_ko=ko.mean(), mean_flox=fl.mean(),
                         pct_mean=100 * ko.mean() / fl.mean() if fl.mean() > 0 else np.nan,
                         pct_median=100 * np.median(ko) / np.median(fl) if np.median(fl) > 0 else np.nan))
    t = pd.DataFrame(rows).set_index("region")
    t["p_adj"] = multipletests(t.p.values, alpha=alpha, method="fdr_tsbky")[1]
    return t.sort_values("p")
