"""Loading and morphometry for Pelot et al. (2020), Front. Neurosci. 14, 601479.

The data are seven SPARC datasets, streamed from the public bucket at pinned
versions (manifest object versions below). Nothing is written to disk.

Measures follow the paper's Methods (Imaging and Image Analysis, last
paragraph: boundaries by bwboundaries, areas by polyarea, effective diameter of
the circle of equal area, perineurium thickness half the difference of the outer
and inner effective diameters) and, where the Methods are silent, the paper's
own MATLAB code deposited in the datasets (files/code of sparc-60, sparc-64,
sparc-65 and sparc-89: HumanRatSegmentationAnalysis_v2.m,
PigSegmentationAnalysis_v2.m, SegmentationAnalysis_v2.m,
PerineuriumComplexMatch_v2.m, DataExtraction_v3.m, DataPlotting_v4.m). Each
parameter below says which.

Boundary convention. MATLAB's bwboundaries traces the centres of the boundary
pixels and polyarea gives the area of that polygon. By Pick's theorem that area
is N - B/2 - 1 for a simply connected region of N pixels with B boundary pixels.
This module computes areas that way (`matlab_area`), which reproduces the
code's convention without tracing contours. Objects are 8-connected and holes
4-connected, as bwboundaries' default.
"""
import base64
import functools
import hashlib
import io
import json

import fsspec
import numpy as np
import pandas as pd
from scipy import ndimage as ndi

BUCKET = "https://sparc-prod-aod-discover-publish50-use1.s3.amazonaws.com"

# Pinned versions: the version each dataset's target gives (none is cited by
# version in the paper's text read; see the notebook header).
DATASETS = {
    "sparc-60": dict(id=60, version=5, doi="10.26275/lg3c-1kjf",
                     manifest="7StJiyPYtSBkyV9XnmU0AcrXETX4pUUS"),
    "sparc-64": dict(id=64, version=4, doi="10.26275/maq2-eii4",
                     manifest="r5MEOSh3l2JKtHbFSUK3wQw4BNPRopiH"),
    "sparc-65": dict(id=65, version=8, doi="10.26275/qgja-q7zd",
                     manifest="B4BZWrzUYNzz8fp7Q36ub_fUwrn.SmdN"),
    "sparc-89": dict(id=89, version=1, doi="10.26275/8pc2-rhu2",
                     manifest="Eu20.3wWopX9n4CwwpIjyXbnls2PYuEU"),
    "sparc-16": dict(id=16, version=5, doi="10.26275/z3ab-7j9y",
                     manifest="lxU4bh4kRRuYY0l8_.Rru9KAU_V2M7VD"),
    "sparc-61": dict(id=61, version=3, doi="10.26275/sydt-lkiw",
                     manifest="fDBPkoUKXO0cU8Kx.YWTob7c6GjIAoga"),
    "sparc-82": dict(id=82, version=1, doi="10.26275/pgr9-bk2e",
                     manifest="RClwsf8wfXqNqmGbz5CvLdUecGmfoTCZ"),
}

READ_LOG = {}  # (dataset, path) -> sha256 hex of every file read


@functools.lru_cache(maxsize=None)
def manifest(ds):
    d = DATASETS[ds]
    url = f"{BUCKET}/{d['id']}/manifest.json?versionId={d['manifest']}"
    with fsspec.open(url, block_size=2**20) as f:
        return json.load(f)


@functools.lru_cache(maxsize=None)
def files(ds):
    """Manifest entries by path."""
    return {f["path"]: f for f in manifest(ds)["files"]}


# Other published versions, read only to show how they differ from the pinned
# one: (dataset, version) -> {path: {"s3VersionId", "sha256"}}, filled folder by
# folder from Pennsieve Discover's public file browser, which gives each file's
# object version (docs/archives.md, "SPARC").
OTHER_VERSIONS = {}


def browse(ds, version, folder):
    """Files of one folder of a published version, from Pennsieve Discover."""
    import urllib.request
    u = (f"https://api.pennsieve.io/discover/datasets/{DATASETS[ds]['id']}/versions/"
         f"{version}/files/browse?path={folder}&limit=500")
    with urllib.request.urlopen(u) as r:
        fs = json.load(r)["files"]
    d = OTHER_VERSIONS.setdefault((ds, version), {})
    for f in fs:
        if f.get("type") == "File":
            d[f["path"]] = {"s3VersionId": f["s3Version"], "sha256": f.get("sha256")}
    return [f["path"] for f in fs if f.get("type") == "File"]


def _entry(ds, path, version=None):
    if version is None or version == DATASETS[ds]["version"]:
        return files(ds)[path]
    return OTHER_VERSIONS[(ds, version)][path]


def url(ds, path, version=None):
    f = _entry(ds, path, version)
    return f"{BUCKET}/{DATASETS[ds]['id']}/{path}?versionId={f['s3VersionId']}"


def read_bytes(ds, path, version=None):
    """Read a whole (small) file at its pinned object version, checking its SHA-256."""
    with fsspec.open(url(ds, path, version), block_size=2**20) as f:
        b = f.read()
    h = hashlib.sha256(b)
    want = _entry(ds, path, version).get("sha256")
    if want is not None and base64.b64decode(want) != h.digest():
        raise ValueError(f"checksum mismatch for {ds}/{path}")
    READ_LOG[(ds, path, version or DATASETS[ds]['version'])] = h.hexdigest()
    return b


def read_excel(ds, path, **kw):
    return pd.read_excel(io.BytesIO(read_bytes(ds, path)), **kw)


def read_mat(ds, path, version=None):
    import scipy.io as sio
    return sio.loadmat(io.BytesIO(read_bytes(ds, path, version)), squeeze_me=True,
                       struct_as_record=False)


MASK_PHOTOMETRIC = {}  # (dataset, path) -> TIFF photometric tag of each mask read


def read_mask(ds, path, version=None):
    """A binary mask as MATLAB's imread gives it. Some masks are stored with
    photometric MinIsWhite (tag 0), where a raw 1 bit is black; imread returns
    them inverted relative to the raw bits, and the paper's code relies on
    that (its outputs for those samples match only after inversion). The raw
    bits are inverted here for such files."""
    import tifffile
    with tifffile.TiffFile(io.BytesIO(read_bytes(ds, path, version))) as t:
        page = t.pages[0]
        a = page.asarray()
        photometric = int(page.photometric)
    MASK_PHOTOMETRIC[(ds, path)] = photometric
    if a.ndim == 3:  # RGB(A) masks: any channel set
        a = a.max(axis=-1)
    a = a > 0
    return ~a if photometric == 0 else a


# ---------------------------------------------------------------- geometry
EIGHT = np.ones((3, 3), bool)
FOUR = ndi.generate_binary_structure(2, 1)


def matlab_area(region):
    """Area (px^2) of the polygon through the centres of the boundary pixels of
    a simply connected region, as bwboundaries + polyarea give it: N - B/2 - 1
    (Pick's theorem). B counts region pixels with a 4-neighbour outside."""
    n = int(region.sum())
    if n == 0:
        return 0.0
    er = ndi.binary_erosion(region, structure=FOUR, border_value=0)
    b = n - int(er.sum())
    return max(n - b / 2 - 1, 0.0)


def label_colmajor(mask, structure):
    """Label components numbered in MATLAB's bwlabel order (column-major scan),
    so that 'the first boundary' means what it means in the paper's code."""
    lab_t, n = ndi.label(mask.T, structure=structure)
    return lab_t.T, n


def objects(mask, with_holes=False):
    """Components of a binary mask, in bwlabel order. Each is a dict with the
    region (cropped), its offset, pixel count, MATLAB-style area, centroid
    (row, col) and, for with_holes, its holes as further regions."""
    lab, n = label_colmajor(mask, EIGHT)
    out = []
    for i, sl in enumerate(ndi.find_objects(lab), start=1):
        if sl is None:
            continue
        reg = lab[sl] == i
        filled = ndi.binary_fill_holes(reg, structure=FOUR)
        rr, cc = np.nonzero(filled)
        o = dict(slice=sl, region=reg, filled=filled, n=int(reg.sum()),
                 area=matlab_area(filled),
                 centroid=(rr.mean() + sl[0].start, cc.mean() + sl[1].start))
        if with_holes:
            hl, nh = label_colmajor(filled & ~reg, FOUR)
            holes = []
            for j, hs in enumerate(ndi.find_objects(hl), start=1):
                if hs is None:
                    continue
                h = hl[hs] == j
                hr, hc = np.nonzero(h)
                holes.append(dict(n=int(h.sum()), area=matlab_area(h),
                                  centroid=(hr.mean() + hs[0].start + sl[0].start,
                                            hc.mean() + hs[1].start + sl[1].start),
                                  slice=(slice(hs[0].start + sl[0].start, hs[0].stop + sl[0].start),
                                         slice(hs[1].start + sl[1].start, hs[1].stop + sl[1].start)),
                                  region=h))
            o["holes"] = holes
        out.append(o)
    return out


def inside(point, obj):
    """Whether a (row, col) point falls inside a filled object (the inpolygon
    test of PerineuriumComplexMatch_v2.m, on the filled region)."""
    r, c = int(round(point[0])), int(round(point[1]))
    sl = obj["slice"]
    if not (sl[0].start <= r < sl[0].stop and sl[1].start <= c < sl[1].stop):
        return False
    return bool(obj["filled"][r - sl[0].start, c - sl[1].start])


def eff_d(area):
    """Effective diameter, the diameter of the circle of the same area (Methods)."""
    return 2 * np.sqrt(np.asarray(area, float) / np.pi)


def shape(obj):
    """Shape of a filled region: aspect ratio of the ellipse with the same second
    moments, and circularity 4 pi A / P^2 (claims file, pig-oblong-human-round).
    The perimeter is regionprops' (skimage), a standard choice."""
    from skimage.measure import regionprops
    p = regionprops(obj["filled"].astype(np.uint8))[0]
    return dict(aspect=p.axis_major_length / p.axis_minor_length,
                circularity=4 * np.pi * p.area / p.perimeter ** 2)


def scale_um_per_px(scale_mask, length_um):
    """Microns per pixel from the scale bar mask, as the paper's code does:
    columns spanned by the bar (find(max(ScaleBar)) first to last, plus 1)."""
    cols = np.nonzero(scale_mask.any(axis=0))[0]
    return length_um / (cols[-1] - cols[0] + 1)


# ------------------------------------------------------------- per sample
def _prefix(sub, sam, letter):
    return (f"files/primary/sub-{sub}/sam-{sam}/sub-{sub}_sam-{sam}_"
            f"{letter}{sub}-{sam}")


def _scale_length(ds, pre, version=None):
    m = read_mat(ds, pre + "ScaleLength.mat", version)
    return float(np.asarray(m["slength"]).ravel()[0])


def match(outers, inners):
    """Assign each inner trace to the first outer trace whose region holds its
    centroid (PerineuriumComplexMatch_v2.m). Returns a list, per outer, of the
    indices of its inner traces, and the indices of unmatched inner traces."""
    groups = [[] for _ in outers]
    unmatched = []
    for j, inn in enumerate(inners):
        for i, o in enumerate(outers):
            if inside(inn["centroid"], o):
                groups[i].append(j)
                break
        else:
            unmatched.append(j)
    return groups, unmatched


def fascicle_table(outers, inners, k):
    """Per inner trace: its area and effective diameter (um), its outer trace,
    whether it is in a peanut fascicle (an outer trace holding more than one
    inner trace, Figure 2 legend), and for non-peanut fascicles the outer
    diameter and perineurium thickness, (d_outer - d_inner) / 2 (Methods)."""
    groups, unmatched = match(outers, inners)
    rows = []
    for i, g in enumerate(groups):
        a_out = outers[i]["area"] * k * k
        for j in g:
            a_in = inners[j]["area"] * k * k
            r = dict(outer=i, inner=j, a_in=a_in, d_in=float(eff_d(a_in)),
                     a_out=a_out, d_out=float(eff_d(a_out)), peanut=len(g) > 1)
            r["thk"] = (r["d_out"] - r["d_in"]) / 2 if len(g) == 1 else np.nan
            rows.append(r)
    for j in unmatched:
        a_in = inners[j]["area"] * k * k
        rows.append(dict(outer=-1, inner=j, a_in=a_in, d_in=float(eff_d(a_in)),
                         a_out=np.nan, d_out=np.nan, peanut=False, thk=np.nan))
    t = pd.DataFrame(rows)
    empty_outers = sum(1 for g in groups if not g)
    return t, empty_outers


def analyse_ihc(ds, sub, sam, letter, inner_name="PeriInnerMask", scale_len=None,
                keep_masks=False):
    """Human anti-claudin-1 (sparc-65, letter C) and pig anti-fibronectin
    (sparc-89, letter P, inner mask 'PeriInMask', scale bar 500 um hard-coded in
    SegmentationAnalysis_v2.m) samples: separate masks of the nerve, the outer
    perineurium and the inner perineurium."""
    pre = _prefix(sub, sam, letter)
    k = scale_um_per_px(read_mask(ds, pre + "ScaleMask.tif"),
                        scale_len if scale_len else _scale_length(ds, pre))
    nerve = objects(read_mask(ds, pre + "NerveMask.tif"))
    outers = objects(read_mask(ds, pre + "PeriExtMask.tif"), with_holes=True)
    inners = objects(read_mask(ds, pre + inner_name + ".tif"), with_holes=True)
    # bwboundaries returns hole boundaries too, and the paper's code counts
    # each as a further inner perineurium trace; so are they here
    inners = inners + [h for o in inners for h in o["holes"]]
    t, empty = fascicle_table(outers, inners, k)
    res = dict(sample=f"{letter}{sub}-{sam}", sub=sub, sam=sam, um_per_px=k,
               n_nerve_objects=len(nerve), nerve_area=nerve[0]["area"] * k * k,
               nerve_shape=shape(nerve[0]), fasc=t, n_outer=len(outers),
               n_inner=len(inners), empty_outers=empty,
               holes_outer=sum(len(o["holes"]) for o in outers),
               holes_inner=sum(len(o.get("holes", [])) for o in inners),
               outer_area_total=sum(o["area"] for o in outers) * k * k)
    res["nerve_d"] = float(eff_d(res["nerve_area"]))
    return res


def analyse_rat(sub, sam, version=None):
    """Rat MT traces (sparc-60): one mask of the perineurial rings; the outer
    boundary of each ring is the outer perineurium and its hole the inner
    perineurium (HumanRatSegmentationAnalysis_v2.m). A NerveMask, the
    connective tissue boundary, exists for multifascicular samples only.
    `version` reads another published version of sparc-60 (its folder is
    listed first with `browse`); version 1 has no ScaleLength.mat, and the
    scale bar length is then taken from samples.xlsx of the pinned version."""
    ds = "sparc-60"
    pre = _prefix(sub, sam, "R")
    have = files(ds) if version is None else OTHER_VERSIONS[(ds, version)]
    if pre + "ScaleLength.mat" in have:
        slen = _scale_length(ds, pre, version)
    else:
        sm = read_excel(ds, "files/samples.xlsx")
        row = sm[(sm.subject_id == f"sub-{sub}") & (sm.sample_id == f"sam-{sam}")]
        slen = float(row["Scale Bar Length"].iloc[0])
    k = scale_um_per_px(read_mask(ds, pre + "ScaleMask.tif", version), slen)
    rings = objects(read_mask(ds, pre + "PeriMask.tif", version), with_holes=True)
    inners = [h for r in rings for h in r["holes"]]
    t, empty = fascicle_table(rings, inners, k)
    p = pre + "NerveMask.tif"
    res = dict(sample=f"R{sub}-{sam}", sub=sub, sam=sam, um_per_px=k, fasc=t,
               n_outer=len(rings), n_inner=len(inners), empty_outers=empty,
               holes_per_ring=[len(r["holes"]) for r in rings],
               has_nerve_mask=p in have, scale_bar_um=slen)
    if res["has_nerve_mask"]:
        nerve = objects(read_mask(ds, p, version))
        res["n_nerve_objects"] = len(nerve)
        res["ct_area"] = nerve[0]["area"] * k * k  # connective tissue boundary
        res["ct_d"] = float(eff_d(res["ct_area"]))
    return res


def analyse_pig_mt(sub, sam):
    """Pig MT traces (sparc-64): masks of the fascicles (inner perineurium) and
    the nerve; scale bar 500 um, hard-coded in PigSegmentationAnalysis_v2.m
    (files/code/README.txt: 'Scale bar length hard-coded as 500 um'). The
    code counts every bwboundaries trace of the fascicle mask, holes included,
    as a fascicle; holes are counted here and reported."""
    ds = "sparc-64"
    pre = _prefix(sub, sam, "P")
    k = scale_um_per_px(read_mask(ds, pre + "ScaleMask.tif"), 500.0)
    nerve = objects(read_mask(ds, pre + "NerveMask.tif"))
    fasc = objects(read_mask(ds, pre + "FascMask.tif"), with_holes=True)
    fasc = fasc + [h for o in fasc for h in o["holes"]]  # as bwboundaries
    a = np.array([f["area"] for f in fasc]) * k * k
    t = pd.DataFrame(dict(inner=range(len(fasc)), a_in=a, d_in=eff_d(a)))
    res = dict(sample=f"P{sub}-{sam}", sub=sub, sam=sam, um_per_px=k,
               n_nerve_objects=len(nerve), nerve_area=nerve[0]["area"] * k * k,
               nerve_shape=shape(nerve[0]), fasc=t, n_inner=len(fasc),
               holes_inner=sum(len(f.get("holes", [])) for f in fasc))
    res["nerve_d"] = float(eff_d(res["nerve_area"]))
    return res


def sample_summary(r, species):
    """Per-sample metrics. For rats, the statistics use the largest fascicle
    only, its outer perineurium as the nerve boundary (Methods, Imaging and
    Image Analysis, paragraph 3; DataPlotting_v4.m). 'Largest' is the largest
    outer perineurium area, the boundary the code sorts on; the inner trace of
    that fascicle gives the fascicle diameter."""
    t = r["fasc"]
    out = dict(sample=r["sample"], sub=r["sub"], sam=r["sam"], species=species,
               n_fasc=len(t), endo_area=t["a_in"].sum())
    if species == "rat":
        big = t.loc[t["a_out"].idxmax()]
        out.update(nerve_d=big["d_out"], fasc_d_largest=big["d_in"],
                   largest_by_inner_same=bool(t["a_in"].idxmax() == t["a_out"].idxmax()),
                   peri_area=t.drop_duplicates("outer")["a_out"].sum() - t["a_in"].sum(),
                   nerve_area=big["a_out"], ct_d=r.get("ct_d", np.nan),
                   ct_area=r.get("ct_area", np.nan),
                   endo_area_largest=big["a_in"])
    else:
        out.update(nerve_d=r["nerve_d"], nerve_area=r["nerve_area"],
                   aspect=r["nerve_shape"]["aspect"],
                   circularity=r["nerve_shape"]["circularity"])
        if species in ("human", "pig_if"):
            out["peri_area"] = r["outer_area_total"] - t["a_in"].sum()
    return out


# ------------------------------------------------------------- sample sets
CODE_SHEETS = {  # species -> (dataset, letter); the paper's own sample lists
    "human": ("sparc-65", "C"), "pig": ("sparc-64", "P"), "rat": ("sparc-60", "R")}
LEVELS = {"C": "CervicalLeft", "S": "AbdominalAnterior"}


def analysed_samples():
    """The samples the paper analysed, from the Excel lists its code reads
    (files/code/<C|P|R><CervicalLeft|AbdominalAnterior><Male|Female>.xlsx,
    read by HumanRatSegmentationAnalysis_v2.m and PigSegmentationAnalysis_v2.m),
    with the sex of the list and the age column (human years, pig weeks, rat
    days; human ages of 90+ entered as 99, DataExtraction_v3.m)."""
    rows = []
    for species, (ds, letter) in CODE_SHEETS.items():
        for level, name in LEVELS.items():
            for sex in ("Male", "Female"):
                p = f"files/code/{letter}{name}{sex}.xlsx"
                t = read_excel(ds, p, header=None)
                for sid, age in zip(t[0], t[1]):
                    sub, sam = sid[1:].split("-")
                    rows.append(dict(sample=sid, species=species, level=level,
                                     sex=sex[0], age_code=age, sub=int(sub), sam=int(sam),
                                     subject=f"{species}-{sub}", dataset=ds))
    return pd.DataFrame(rows)


def if_samples():
    """Pig anti-fibronectin samples with traces in sparc-89 (a PeriInMask), with
    their level from samples.xlsx of sparc-89."""
    import re
    sm = read_excel("sparc-89", "files/samples.xlsx")
    rows = []
    for p in files("sparc-89"):
        m = re.match(r"files/primary/sub-(\d+)/sam-(\d+)/.*PeriInMask\.tif$", p)
        if not m:
            continue
        sub, sam = int(m.group(1)), int(m.group(2))
        r = sm[(sm.subject_id == f"sub-{sub}") & (sm.sample_id == f"sam-{sam}")].iloc[0]
        loc = str(r["specimen anatomical location"])
        rows.append(dict(sample=f"P{sub}-{sam}", sub=sub, sam=sam, sex=str(r["sex"])[0],
                         level="C" if "cervical" in loc else "S", location=loc,
                         subject=f"pig-{sub}"))
    return pd.DataFrame(rows).sort_values(["level", "sub"]).reset_index(drop=True)


def load_all(rat_version=None, only=None):
    """Morphometry of every analysed sample (54) and every pig IF sample (8).
    Returns (per-sample table, dict of full results by key). Keys are sample
    ids; pig IF samples are keyed 'IF' + id."""
    s = analysed_samples()
    if only is not None:
        s = s[s.species.isin(only)]
    res, rows = {}, []
    for _, r in s.iterrows():
        if r.species == "human":
            x = analyse_ihc("sparc-65", r["sub"], r.sam, "C")
        elif r.species == "pig":
            x = analyse_pig_mt(r["sub"], r.sam)
        else:
            if rat_version is not None:
                browse("sparc-60", rat_version, f"files/primary/sub-{r['sub']}/sam-{r.sam}")
            x = analyse_rat(r["sub"], r.sam, rat_version)
        res[r["sample"]] = x
        d = sample_summary(x, r.species)
        d.update(level=r.level, sex=r.sex, subject=r.subject, age_code=r.age_code)
        rows.append(d)
    for _, r in (if_samples().iterrows() if only is None or "pig_if" in only else []):
        x = analyse_ihc("sparc-89", r["sub"], r.sam, "P", inner_name="PeriInMask",
                        scale_len=500.0)
        res["IF" + r["sample"]] = x
        d = sample_summary(x, "pig_if")
        d.update(level=r.level, sex=r.sex, subject=r.subject)
        rows.append(d)
    return pd.DataFrame(rows), res


def fascicles(res, table, species):
    """One row per inner perineurium trace of the samples of a species in
    `table`, with its sample's level and subject."""
    out = []
    for _, r in table[table.species == species].iterrows():
        key = ("IF" if species == "pig_if" else "") + r["sample"]
        t = res[key]["fasc"].copy()
        t["sample"], t["level"], t["subject"] = r["sample"], r.level, r.subject
        out.append(t)
    return pd.concat(out, ignore_index=True)


def line_fit(x, y, zero=False):
    """Linear least squares, as MATLAB's fit with 'poly1' (DataPlotting_v4.m,
    SegmentationAnalysis_v2.m), or through the origin (Results, before Eq. 4).
    R2 is about the mean of y, as MATLAB's gof.rsquare; for the zero-intercept
    fit the uncentred R2 is returned as well."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    if zero:
        b = (x @ y) / (x @ x)
        a = 0.0
    else:
        b, a = np.polyfit(x, y, 1)
    res = y - (a + b * x)
    sst = ((y - y.mean()) ** 2).sum()
    out = dict(slope=b, intercept=a, r2=1 - (res @ res) / sst, n=len(x),
               sse=res @ res)
    if zero:
        out["r2_uncentred"] = 1 - (res @ res) / (y @ y)
    # 95% confidence bounds of the coefficients, as MATLAB's confint
    X = np.c_[x] if zero else np.c_[np.ones_like(x), x]
    dof = len(x) - X.shape[1]
    cov = (res @ res) / dof * np.linalg.inv(X.T @ X)
    tq = __import__("scipy").stats.t.ppf(0.975, dof)
    se = np.sqrt(np.diag(cov))
    if zero:
        out["slope_ci"] = (b - tq * se[0], b + tq * se[0])
    else:
        out["intercept_ci"] = (a - tq * se[0], a + tq * se[0])
        out["slope_ci"] = (b - tq * se[1], b + tq * se[1])
    return out


# ------------------------------------------------------------- micrographs
def micrograph_paths(ds):
    """MT micrographs of a collection: the JPEG 2000 derivatives of the nd2
    files (files/derivative/), keyed by the subject and sample in the file
    name (some are filed in another sample's folder, or with a copy suffix
    such as ' (1)'). One file per distinct name, the copy dropped when both
    exist; used for viewing."""
    import re
    best = {}
    for p in files(ds):
        if not (p.startswith("files/derivative/") and p.endswith(".jp2")):
            continue
        name = p.split("/")[-1]
        m = re.match(r"(sub-\d+)_?(sam-\d+)", name)
        if not m:
            continue
        base = re.sub(r" \(\d+\)", "", name)
        key = (m.group(1), m.group(2), base)
        folder_ok = p.startswith(f"files/derivative/{m.group(1)}/{m.group(2)}/")
        rank = (("(" in name), not folder_ok)
        if key not in best or rank < best[key][0]:
            best[key] = (rank, p)
    return sorted((k[0], k[1], v[1]) for k, v in best.items())


def thumbnail(ds, path, step=8):
    """Decode a JPEG 2000 micrograph and keep every `step`-th pixel."""
    import imagecodecs
    a = imagecodecs.jpeg2k_decode(read_bytes(ds, path))
    return a[::step, ::step]


# Readings made by eye by the author of this attempt on the micrographs the
# notebook displays (claims human-subdiaphragmatic-fatty-tissue,
# pig-cervical-cell-bodies, rat-carotid-sheath-bundles, whose criteria are
# judgements by eye). They are recorded here, not computed; the notebook shows
# the images they were read from, so that a reader can check them.
#
# Rat: nerve profiles bounded by their own perineurium within the carotid
# sheath, per cervical micrograph (sparc-16), counted on thumbnails of the
# JPEG 2000 derivatives (about 1 um per pixel); the smallest profiles may be
# missed at that scale. Muscle and vessels are not counted.
RAT_SHEATH_BUNDLES = {
    "R16-3": 2, "R17-3": 5, "R18-1": 4, "R20-3": 2, "R21-3": 3, "R22-3": 4,
    "R23-3": 3, "R24-3": 5, "R25-3": 2,                      # left (analysed)
    "R16-2": 2, "R17-2": 4, "R18-2": 5, "R20-2": 4, "R21-2": 4, "R22-2": 2,
    "R23-2": 4, "R24-2": 4, "R25-2": 2,                      # right
}
# Whether the traced vagus is the largest bundle in each analysed sample, by eye.
RAT_VAGUS_LARGEST = {k: True for k in ["R16-3", "R17-3", "R18-1", "R20-3", "R21-3",
                                        "R22-3", "R23-3", "R24-3", "R25-3"]}
# Adipose tissue (clusters of large, empty, polygonal cells) in the
# extrafascicular tissue, human subdiaphragmatic MT micrographs (sparc-61),
# by (subject, sample).
HUMAN_SUB_FAT = {
    ("sub-51", "sam-1"): False, ("sub-51", "sam-3"): True, ("sub-53", "sam-3"): True,
    ("sub-53", "sam-4"): True, ("sub-54", "sam-1"): True, ("sub-54", "sam-2"): True,
    ("sub-55", "sam-1"): False, ("sub-55", "sam-2"): True, ("sub-56", "sam-1"): True,
    ("sub-56", "sam-2"): True, ("sub-57", "sam-1"): True, ("sub-57", "sam-2"): True,
    ("sub-58", "sam-1"): True, ("sub-58", "sam-2"): False, ("sub-63", "sam-1"): True,
    ("sub-64", "sam-1"): True, ("sub-64", "sam-2"): True, ("sub-65", "sam-1"): True,
    ("sub-65", "sam-2"): True, ("sub-66", "sam-2"): True, ("sub-67", "sam-1"): True,
    ("sub-67", "sam-2"): True, ("sub-68", "sam-1"): True, ("sub-68", "sam-2"): True,
    ("sub-69", "sam-1"): True, ("sub-69", "sam-2"): True, ("sub-70", "sam-1"): True,
    ("sub-70", "sam-2"): True, ("sub-71", "sam-1"): True, ("sub-71", "sam-2"): True,
    ("sub-72", "sam-1"): True, ("sub-72", "sam-2"): True,
}
# Pig MT micrographs (sparc-82) with adipose tissue within the epineurium:
# from the 45 thumbnails, and for the nine analysed cervical samples from the
# half-resolution views of pig-cervical-cell-bodies (where it is clearer).
PIG_FAT = {("sub-5", "sam-3"), ("sub-6", "sam-1"), ("sub-6", "sam-5"), ("sub-7", "sam-1"),
           ("sub-7", "sam-5"), ("sub-8", "sam-1"), ("sub-8", "sam-3"),
           ("sub-5", "sam-1"), ("sub-6", "sam-7"), ("sub-8", "sam-7"), ("sub-9", "sam-3"),
           ("sub-11", "sam-1"), ("sub-13", "sam-1")}
# Fascicles holding neuronal cell bodies (large round somata with a nucleus),
# analysed pig cervical samples, on half-resolution views of the derivatives.
# P14-2 has one pale fascicle (lower right) that could not be called either
# way at this resolution and is counted as without.
PIG_CELL_BODIES = {"P11-1": True, "P13-1": True, "P12-1": False, "P5-1": False,
                   "P6-7": False, "P8-7": False, "P9-3": False, "P14-2": False,
                   "P15-2": False}
