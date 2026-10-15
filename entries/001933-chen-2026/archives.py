"""Loading and measures for the data of Chen, He et al. (2026) that are not in dandiset 001933.

The paper deposited the data of Figures 1 to 5 in other public archives: the tabular values
behind every figure and the uncropped blots on Zenodo (doi:10.5281/zenodo.19930567), the mass
spectrometry in PRIDE (PXD065003, PXD065006, PXD065125) and the images in the BioImage Archive
(S-BIAD2070, S-BIAD2071, S-BIAD2072, S-BIAD2074). Everything here is read in memory from those
archives; nothing is written to disk.

Where the parameters come from:

- Statistics follow the figure legends: two-tailed unpaired Student t-tests for two groups,
  a two-way ANOVA with Sidak-adjusted comparisons (Figures 2E, 2G, 5D and 5E), and paired
  two-sided t-tests for the pulldowns of Figure 3E and 3F. Sidak comparisons use the pooled
  residual variance of the ANOVA, as GraphPad Prism does.
- Phosphopeptides (Figure 2B): log2 abundances, two-tailed unpaired t-test, p <= 0.05 and
  |difference of log2 means| > 0.58, the legend's thresholds. Which peptides enter the test is
  not stated; ``min_values`` sets how many values each group needs.
- Pulldowns (Figure 3): log2 DIA-NN intensities. The imputation variant follows the Methods
  (draws from a Gaussian centred at the 1% quantile of each sample); its width, 0.3 times the
  sample's standard deviation, is a common choice (Perseus), as the Methods give none.
- Synaptosome images (Figure 4D and 4E): the Methods' FIJI procedure. Rolling-ball background
  of radius 33 pixels, done as ImageJ does it (3x3 mean, shrink by 4 with the minimum, ball of
  radius 33/4, bilinear enlargement); ImageJ's Default threshold (the IJ IsoData variant with
  the mode bin limited) on a 256-bin histogram, objects bright; particles 8-connected, area
  0.04 to 0.40 um2 (TH 0.06 to 0.60) and circularity 0.30 to 1.00; positive for a protein when
  the mean intensity in the particle is more than twice the image mean. The perimeter behind
  the circularity is scikit-image's, not ImageJ's traced polygon.
"""

import hashlib
import io
import json
import re
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

import numpy as np
import pandas as pd
import requests
from scipy import ndimage, stats

ZENODO_RECORD = "https://zenodo.org/api/records/19930567"
SOURCE_DATA_URL = ZENODO_RECORD + "/files/Source%20data.xlsx/content"
SOURCE_DATA_MD5 = "c26fe3de8f340a3db5fa29a40e5a8c10"
SUPPLEMENTARY_URL = ZENODO_RECORD + "/files/Supplementary%20files.zip/content"
PRIDE = "https://ftp.pride.ebi.ac.uk/pride/data/archive/2026/05/"
PHOSPHOPEPTIDES_URL = PRIDE + "PXD065006/020623-Loukia-mouse-synaptosome-phos-quant_phosphopeptides.xlsx"
PULLDOWN_URL = PRIDE + "PXD065125/FilteredDataset.pg_matrix.Brain_Rab3A.csv"
PULLDOWN_REPORT_URL = PRIDE + "PXD065125/report.pg_matrix.tsv"
PULLDOWN_LIMMA_URL = PRIDE + "PXD065125/Brain_Rab3A.DifferentialAbundance_volcano.csv"
PULLDOWN_SDRF_URL = PRIDE + "PXD065125/PXD065125_community_annotated.sdrf.tsv"
BIA = "https://ftp.ebi.ac.uk/biostudies/fire/S-BIAD/{n}/S-BIAD2{n}/Files/"
BIA_FILE_LISTS = {"S-BIAD2070": "LRRK2 expression.json", "S-BIAD2071": "Terminal analysis.json",
                  "S-BIAD2072": "TH-VMAT2.json", "S-BIAD2074": "synaptosome.json"}
PIXEL_UM = 0.031074  # synaptosome images, from their OME metadata (checked in the notebook)


def fetch(url, size=None, attempts=3):
    """Bytes of a file and their md5. A failed request is retried up to ``attempts`` times and
    then raised; with ``size``, a file of another length is an error."""
    for k in range(attempts):
        try:
            r = requests.get(url, timeout=600)
            r.raise_for_status()
            if size is not None and len(r.content) != size:
                raise IOError(f"{url}: {len(r.content)} bytes, the archive lists {size}")
            break
        except (requests.RequestException, IOError):
            if k == attempts - 1:
                raise
    return r.content, hashlib.md5(r.content).hexdigest()


@lru_cache(maxsize=None)
def source_workbook():
    import openpyxl

    content, md5 = fetch(SOURCE_DATA_URL)
    return md5, openpyxl.load_workbook(io.BytesIO(content), read_only=True, data_only=True)


def sheet(name):
    """Rows of a source data sheet, trailing empty cells removed."""
    rows = []
    for r in source_workbook()[1][name].iter_rows(values_only=True):
        r = list(r)
        while r and r[-1] is None:
            r.pop()
        rows.append(r)
    return rows


def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _col(rows, first, c):
    return [r[c] for r in rows[first:] if len(r) > c and _num(r[c])]


def fig1d():
    """Per-section mean LRRK2 intensity in Aldh1a1- and Aldh1a1+ neurons, with mouse."""
    out, mouse = [], None
    for r in sheet("Fig. 1c-d")[3:]:
        if len(r) > 13 and _num(r[11]):
            mouse = int(r[10]) if _num(r[10]) else mouse
            out.append({"mouse": mouse, "section": int(r[11]), "neg": float(r[12]), "pos": float(r[13])})
    return pd.DataFrame(out)


def fig2eg():
    """p-RAB3A (2E) and p-RAB3C (2G) ratios for WT, GS and GS with MLi-2."""
    rows = sheet("Fig. 2d-f")
    out = {}
    for name, c0 in (("RAB3A", 0), ("RAB3C", 9)):
        out[name] = {g: np.array(_col(rows, 3, c0 + k), float) for k, g in ((1, "WT"), (2, "GS"), (3, "GS+MLi2"))}
    return out


def fig4de():
    """Per-area values: percentage of TH+/VAMP2+ synaptosomes with bassoon (4D), bassoon area (4E)."""
    rows = sheet("Fig. 4d-e")
    out = []
    for panel, c0 in (("4D", 0), ("4E", 6)):
        rep = None
        for r in rows[2:]:
            if len(r) > c0 + 1 and _num(r[c0 + 1]):
                rep = int(r[c0]) if _num(r[c0]) else rep
                for k, g in ((2, "WT"), (3, "GS")):
                    if len(r) > c0 + k and _num(r[c0 + k]):
                        out.append({"panel": panel, "replicate": rep, "area": int(r[c0 + 1]), "group": g,
                                    "value": float(r[c0 + k])})
    return pd.DataFrame(out)


def fig4():
    """Western blot values of Figure 4G to 4L, by panel: WT and GS arrays."""
    rows = sheet("Fig. 4f-J")
    out = {}
    for panel, c0 in (("4G", 0), ("4H", 4), ("4I", 8), ("4J", 12)):
        out[panel] = {"WT": np.array(_col(rows, 3, c0 + 1), float), "GS": np.array(_col(rows, 3, c0 + 2), float)}
    rows = sheet("Fig. 4k-l ")
    out["4L"] = {"WT": np.array(_col(rows, 3, 1), float), "GS": np.array(_col(rows, 3, 2), float)}
    return out


def fig5de():
    """Per-section bassoon cluster density (5D) and volume (5E) in Aldh1a1+ and Aldh1a1- axons."""
    rows = sheet("Fig. 5d-e")
    out = []
    for panel, start in (("5D", 1), ("5E", 9)):
        head, animals, sections, pos, neg = rows[start:start + 5]
        gs_from = [str(v).strip() for v in head].index("GS")
        mouse = None
        for c in range(1, len(sections)):
            if not _num(sections[c]):
                continue
            mouse = int(animals[c]) if c < len(animals) and _num(animals[c]) else mouse
            group = "GS" if c >= gs_from else "WT"
            for cell, vals in (("Aldh1a1+", pos), ("Aldh1a1-", neg)):
                v = vals[c] if c < len(vals) else None
                out.append({"panel": panel, "group": group, "mouse": mouse, "column": c,
                            "section": int(sections[c]), "cell": cell, "value": float(v) if _num(v) else np.nan})
    return pd.DataFrame(out)


def fig5gh():
    """Per-section bassoon density (5G) and volume (5H) in Anxa1+ axons; the animal column as given."""
    rows = sheet("Fig. 5g-h")
    out = []
    for panel, c0 in (("5G", 0), ("5H", 5)):
        animal = None
        for r in rows[2:]:
            if len(r) > c0 + 1 and _num(r[c0 + 1]):
                animal = int(r[c0]) if _num(r[c0]) else animal
                for k, g in ((2, "WT"), (3, "GS")):
                    if len(r) > c0 + k and _num(r[c0 + k]):
                        out.append({"panel": panel, "animal_column": animal, "section": int(r[c0 + 1]),
                                    "group": g, "value": float(r[c0 + k])})
    return pd.DataFrame(out)


def fig5j():
    rows = sheet("Fig. 5j")
    out, animal = [], None
    for r in rows[1:]:
        if len(r) > 1 and _num(r[1]):
            animal = int(r[0]) if _num(r[0]) else animal
            for k, g in ((2, "WT"), (3, "GS")):
                if len(r) > k and _num(r[k]):
                    out.append({"animal_column": animal, "section": int(r[1]), "group": g, "value": float(r[k])})
    return pd.DataFrame(out)


# Statistics -------------------------------------------------------------------------------

def ttest(a, b, equal_var=True):
    """Two-tailed unpaired t-test of a against b: t, p."""
    r = stats.ttest_ind(a, b, equal_var=equal_var)
    return float(r.statistic), float(r.pvalue)


def cohens_d(a, b):
    """(mean a - mean b) / pooled standard deviation."""
    n1, n2 = len(a), len(b)
    sp = np.sqrt(((n1 - 1) * np.var(a, ddof=1) + (n2 - 1) * np.var(b, ddof=1)) / (n1 + n2 - 2))
    return float((np.mean(a) - np.mean(b)) / sp)


def sidak(p, m):
    return 1 - (1 - p) ** m


def pooled_contrasts(groups, pairs, m=None):
    """Pairwise contrasts of group means on the pooled within-group variance (one-way model).

    ``groups``: name -> values. Returns one row per pair with the difference (first minus
    second), t, df, the raw two-tailed p and the Sidak-adjusted p over ``m`` comparisons
    (default: the number of pairs)."""
    m = m or len(pairs)
    vals = list(groups.values())
    n = sum(len(v) for v in vals)
    df = n - len(vals)
    mse = sum(((v - v.mean()) ** 2).sum() for v in vals) / df
    out = []
    for a, b in pairs:
        x, y = groups[a], groups[b]
        t = (x.mean() - y.mean()) / np.sqrt(mse * (1 / len(x) + 1 / len(y)))
        p = 2 * stats.t.sf(abs(t), df)
        out.append({"pair": f"{a} vs {b}", "diff": x.mean() - y.mean(), "t": t, "df": df, "F": t ** 2,
                    "p": p, "p_sidak": sidak(p, m)})
    return pd.DataFrame(out)


def twoway_anova(df, value="value", a="cell", b="group"):
    """Two-way ANOVA with interaction, type III sums of squares (effect coding), as Prism uses for
    unequal group sizes. Returns a table of F, df and p, and the residual mean square and df."""
    d = df.dropna(subset=[value])
    la, lb = sorted(d[a].unique()), sorted(d[b].unique())
    xa = np.where(d[a] == la[0], 1.0, -1.0)
    xb = np.where(d[b] == lb[0], 1.0, -1.0)
    y = d[value].to_numpy(float)
    full = np.column_stack([np.ones_like(y), xa, xb, xa * xb])

    def rss(x):
        beta, *_ = np.linalg.lstsq(x, y, rcond=None)
        return float(((y - x @ beta) ** 2).sum())

    rss_full = rss(full)
    df_res = len(y) - 4
    mse = rss_full / df_res
    rows = []
    for name, k in ((a, 1), (b, 2), ("interaction", 3)):
        f = (rss(np.delete(full, k, axis=1)) - rss_full) / mse
        rows.append({"factor": name, "F": f, "df": f"1, {df_res}", "p": float(stats.f.sf(f, 1, df_res))})
    return pd.DataFrame(rows), mse, df_res


def sidak_within(df, mse, df_res, value="value", a="cell", b="group", first="GS", second="WT"):
    """GS against WT within each level of ``a`` on the pooled variance, Sidak over the levels."""
    d = df.dropna(subset=[value])
    levels = sorted(d[a].unique())
    out = []
    for lev in levels:
        x = d[(d[a] == lev) & (d[b] == first)][value].to_numpy(float)
        y = d[(d[a] == lev) & (d[b] == second)][value].to_numpy(float)
        t = (x.mean() - y.mean()) / np.sqrt(mse * (1 / len(x) + 1 / len(y)))
        p = 2 * stats.t.sf(abs(t), df_res)
        out.append({a: lev, f"n_{first}": len(x), f"n_{second}": len(y), f"mean_{first}": x.mean(),
                    f"mean_{second}": y.mean(), "t": t, "p": p, "p_sidak": sidak(p, len(levels))})
    return pd.DataFrame(out)


# Proteomics -------------------------------------------------------------------------------

def phosphopeptides():
    """The peptide groups table of PXD065006 and its md5."""
    content, md5 = fetch(PHOSPHOPEPTIDES_URL)
    return pd.read_excel(io.BytesIO(content)), md5


def volcano_test(pp, min_values):
    """Per phosphopeptide: log2 abundances, two-tailed Student t-test vehicle against MLi-2.

    Peptides with fewer than ``min_values`` values in either group are left out."""
    veh = [c for c in pp.columns if c.startswith("Abundance") and "Vehicle" in c]
    mli = [c for c in pp.columns if c.startswith("Abundance") and "MLi2" in c]
    a, b = np.log2(pp[veh].to_numpy(float)), np.log2(pp[mli].to_numpy(float))
    keep = (np.isfinite(a).sum(1) >= min_values) & (np.isfinite(b).sum(1) >= min_values)
    a, b = a[keep], b[keep]
    diff = np.nanmean(a, 1) - np.nanmean(b, 1)
    p = stats.ttest_ind(a, b, axis=1, nan_policy="omit").pvalue
    out = pp.loc[keep, ["Gene Name", "Annotated Sequence", "Modifications", "Modifications in Master Proteins"]].copy()
    out["diff"], out["p"] = diff, np.asarray(p, float)
    out["altered"] = (out.p <= 0.05) & (out["diff"].abs() > 0.58)
    return out


def supplementary_data():
    """The Supplementary data files (Zenodo, Supplementary files.zip): name -> bytes."""
    import zipfile

    content, md5 = fetch(SUPPLEMENTARY_URL)
    z = zipfile.ZipFile(io.BytesIO(content))
    return {n: z.read(n) for n in z.namelist() if n.endswith(".xlsx")}, md5


def pulldown():
    """DIA-NN protein intensities of the six p-RAB3A and six RAB3A pulldowns (PXD065125).

    Returns the table (log2, columns phos_1..6 and unphos_1..6 in run order) and the md5."""
    content, md5 = fetch(PULLDOWN_URL)
    d = pd.read_csv(io.BytesIO(content))
    phos = [c for c in d.columns if c.startswith("phosRab3Brain")]
    unphos = [c for c in d.columns if c.startswith("Rab3Brain")]
    out = d[["Genes", "Protein.Group"]].copy()
    for k, c in enumerate(phos, 1):
        out[f"phos_{k}"] = np.log2(d[c].astype(float))
    for k, c in enumerate(unphos, 1):
        out[f"unphos_{k}"] = np.log2(d[c].astype(float))
    return out, md5, list(d.columns)


def paired_test(row):
    """Paired two-sided t-test, RAB3A against p-RAB3A, over replicates with both values."""
    a = np.array([row[f"unphos_{k}"] for k in range(1, 7)], float)
    b = np.array([row[f"phos_{k}"] for k in range(1, 7)], float)
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 2:
        return {"pairs": int(ok.sum()), "log2FC_unphos_minus_phos": np.nan, "p": np.nan}
    r = stats.ttest_rel(a[ok], b[ok])
    return {"pairs": int(ok.sum()), "log2FC_unphos_minus_phos": float(np.mean(a[ok] - b[ok])), "p": float(r.pvalue)}


def impute(d, cols, rng, width=0.3):
    """The Methods' imputation: missing log2 values drawn per sample from a Gaussian centred at
    the sample's 1% quantile, with ``width`` times its standard deviation."""
    out = d.copy()
    for c in cols:
        v = np.array(out[c], dtype=float)
        ok = np.isfinite(v)
        fill = rng.normal(np.quantile(v[ok], 0.01), width * v[ok].std(), size=(~ok).sum())
        v[~ok] = fill
        out[c] = v
    return out


# Images -----------------------------------------------------------------------------------

def bia_files(accession):
    """The file list of a BioImage Archive study: path, size and attributes."""
    n = accession[-3:]
    url = BIA.format(n=n) + requests.utils.quote(BIA_FILE_LISTS[accession])
    files = json.loads(requests.get(url, timeout=120).content)
    return pd.DataFrame([{"path": f["path"], "size": f["size"],
                          **{a["name"]: a["value"] for a in f.get("attributes", [])}} for f in files])


def read_synaptosome_image(path, size=None):
    """One synaptosome image of S-BIAD2074 (three channels), its md5 and pixel size in um."""
    import tifffile

    content, md5 = fetch(BIA.format(n="074") + requests.utils.quote(path), size)
    with tifffile.TiffFile(io.BytesIO(content)) as tf:
        img = tf.asarray().astype(float)
        m = re.search(r'PhysicalSizeX="([0-9.]+)"', tf.ome_metadata or "")
    return img, md5, float(m.group(1)) if m else np.nan


def rolling_ball(channel, radius=33):
    """ImageJ's rolling-ball background (bright objects), returned subtracted and clipped at 0."""
    from skimage.restoration import rolling_ball as skball
    from skimage.transform import resize

    shrink = 1 if radius <= 10 else 2 if radius <= 30 else 4 if radius <= 100 else 8
    smooth = ndimage.uniform_filter(channel, 3, mode="nearest")
    h, w = smooth.shape
    small = smooth[:h - h % shrink, :w - w % shrink].reshape(h // shrink, shrink, w // shrink, shrink).min(axis=(1, 3))
    bg_small = skball(small, radius=radius / shrink)
    bg = resize(bg_small, (h, w), order=1, mode="edge", anti_aliasing=False)
    return np.clip(channel - np.minimum(bg, channel), 0, None)


def ij_default_threshold(channel):
    """ImageJ's Default auto-threshold (IJ IsoData with the mode limited), on a 256-bin histogram
    from the channel's minimum to its maximum. Returns the intensity above which pixels are
    foreground."""
    lo, hi = float(channel.min()), float(channel.max())
    hist, _ = np.histogram(channel, bins=256, range=(lo, hi))
    data = hist.astype(float)
    mode = int(np.argmax(data))
    second = np.max(np.delete(data, mode))
    if data[mode] > 2 * second and second != 0:
        data[mode] = int(second * 1.5)
    data[0] = 0
    data[255] = 0
    nz = np.nonzero(data)[0]
    if len(nz) < 2:
        return lo + (hi - lo) / 2
    mn, mx = nz[0], nz[-1]
    i = np.arange(256)
    moving = mn
    while True:
        s1, s2 = (i[mn:moving + 1] * data[mn:moving + 1]).sum(), data[mn:moving + 1].sum()
        s3, s4 = (i[moving + 1:mx + 1] * data[moving + 1:mx + 1]).sum(), data[moving + 1:mx + 1].sum()
        result = (s1 / s2 + s3 / s4) / 2
        moving += 1
        if not ((moving + 1) <= result and moving < mx - 1):
            break
    level = int(round(result))
    return lo + (level + 1) * (hi - lo) / 256


def particles(channel, pixel_um, area_um2, circularity=(0.30, 1.00)):
    """Analyze Particles: label image of the particles that pass the size and circularity limits."""
    from skimage.measure import label, regionprops

    lab = label(channel >= ij_default_threshold(channel), connectivity=2)
    keep = np.zeros(lab.max() + 1, bool)
    px2 = pixel_um ** 2
    for r in regionprops(lab):
        a = r.area * px2
        per = r.perimeter * pixel_um
        circ = min(1.0, 4 * np.pi * a / per ** 2) if per > 0 else 1.0
        keep[r.label] = area_um2[0] <= a <= area_um2[1] and circularity[0] <= circ <= circularity[1]
    lab[~keep[lab]] = 0
    return lab


def synaptosome_fraction(img, pixel_um, channels=(0, 1, 2)):
    """Figure 4D on one image: of the VAMP2 particles that are VAMP2+ and TH+, the percentage that
    are bassoon+. ``channels`` = (bassoon, TH, VAMP2)."""
    bsn, th, vamp = (rolling_ball(img[c]) for c in channels)
    lab = particles(vamp, pixel_um, (0.04, 0.40))
    present = np.unique(lab[lab > 0])
    if len(present) == 0:
        return {"vamp2_particles": 0, "th_vamp2": 0, "bassoon_th_vamp2": 0, "percent": np.nan}
    mv = np.asarray(ndimage.mean(vamp, lab, present))
    mt = np.asarray(ndimage.mean(th, lab, present))
    mb = np.asarray(ndimage.mean(bsn, lab, present))
    v_pos = mv > 2 * vamp.mean()
    double = v_pos & (mt > 2 * th.mean())
    triple = double & (mb > 2 * bsn.mean())
    return {"vamp2_particles": int(len(present)), "vamp2_pos": int(v_pos.sum()), "th_vamp2": int(double.sum()),
            "bassoon_th_vamp2": int(triple.sum()),
            "percent": 100 * triple.sum() / double.sum() if double.sum() else np.nan}


def synaptosome_area(img, pixel_um, channels=(0, 1, 2)):
    """Figure 4E on one image: the overlaps of bassoon and TH particles that are VAMP2+, and their
    mean area, read as (i) the overlap's area and (ii) the area of the bassoon particle."""
    from skimage.measure import label

    bsn, th, vamp = (rolling_ball(img[c]) for c in channels)
    lb = particles(bsn, pixel_um, (0.04, 0.40))
    lt = particles(th, pixel_um, (0.06, 0.60))
    lo = label((lb > 0) & (lt > 0), connectivity=2)
    present = np.unique(lo[lo > 0])
    if len(present) == 0:
        return {"overlaps": 0, "vamp2_pos": 0, "area_overlap": np.nan, "area_bassoon": np.nan}
    px2 = pixel_um ** 2
    mv = np.asarray(ndimage.mean(vamp, lo, present))
    pos = present[mv > 2 * vamp.mean()]
    if len(pos) == 0:
        return {"overlaps": int(len(present)), "vamp2_pos": 0, "area_overlap": np.nan, "area_bassoon": np.nan}
    ov_area = np.asarray(ndimage.sum(np.ones_like(vamp), lo, pos)) * px2
    b_sizes = np.bincount(lb.ravel()) * px2
    b_ids = sorted({int(np.bincount(lb[lo == k]).argmax()) for k in pos})
    return {"overlaps": int(len(present)), "vamp2_pos": int(len(pos)), "area_overlap": float(ov_area.mean()),
            "area_bassoon": float(b_sizes[b_ids].mean())}


def analyse_synaptosomes(files, workers=8):
    """Stream every image in ``files`` (a table of paths and sizes in S-BIAD2074) and run both
    measures on it."""

    def one(item):
        path, size = item
        img, md5, px = read_synaptosome_image(path, size)
        name = path.split("/")[-1]
        m = re.match(r"Export_(wt|ki)(\d+)_BSN(\d+)", name, re.I)
        row = {"path": path, "folder": path.split("/")[-2], "group": "WT" if m.group(1).lower() == "wt" else "GS",
               "mouse": int(m.group(2)), "image": int(m.group(3)), "md5": md5, "pixel_um": px,
               "shape": "x".join(map(str, img.shape))}
        if row["folder"] == "BSN":
            row.update(synaptosome_fraction(img, px))
        else:
            row.update(synaptosome_area(img, px))
        return row

    with ThreadPoolExecutor(workers) as ex:
        return pd.DataFrame(list(ex.map(one, zip(files["path"], files["size"]))))
