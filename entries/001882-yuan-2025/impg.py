"""Loading and measures for dandiset 001882 (IMPG1 and IMPG2 patients, West Virginia University).

Yuan, Chatterjee, Leys, Odom & Salido (2025), Genes 16(1):43, doi:10.3390/genes16010043.

The dandiset holds no NWB file. At version 0.260701.1757 it has 13 files: a spreadsheet of the
seven patients (`derivatives/small table for 7 patients 20241127.xlsx`, the paper's Table 1), a
Word document with tool outputs for the in silico tables (`sourcedata/protein structure and
stabilityIMPG2 TABLE original.docx`), the paper's Figures 1 to 4 as image files under
`sub-01/micr/`, a script that made the folder layout (`setup_bids.py`) and six Windows
`desktop.ini` files. Files are streamed from the archive at the pinned version into memory;
nothing is written to disk.

Where the parameters come from:

- The spreadsheet's first column holds what look like hospital record numbers. They are never
  returned by `load_patients` or printed.
- Panel boxes of Figures 2 and 3 (`FIG2_PANELS`, `FIG3_PANELS`) are read off the figure layout
  (pixel rows and columns of each panel in the full-resolution files); they only cut the
  figure into its panels and are a standard choice that cannot change a result.
- FAF lesion centres (`FAF_LESIONS`) are the points the yellow arrows of Figure 3 mark, read off
  the figure by the author; the lesion disc radius and the surrounding annulus
  (`FAF_RADII`) are a standard choice, and the notebook shows the contrast at several radii.
  The arrow pixels are left out of every FAF measure (`overlay_mask`). The background discs
  (`NULL_RADIUS`, `NULL_N`) that decide whether a lesion is brighter than the fundus are an
  assumption (the paper graded by inspection and gives no criterion); the notebook shows four
  other readings beside the one adopted.
- `arrow_boxes` and `ARROW_COLOURS` only find the arrows for the full-resolution crops; display
  only, they cannot change a result.
- MuPRO and I-Mutant 2.0 are the web servers Methods 2.4 names, run from sequence as the claims
  file says (I-Mutant at its default 25 C and pH 7); the FATHMM-MKL web server is the FATHMM site
  of Methods 2.2. None has a version that can be pinned.
- Outside tools and data follow the claims file: SIFT and PolyPhen-2 (HumVar) through the Ensembl
  VEP REST service on the MANE Select transcripts (the claims file's transcript reading); PolyPhen-2
  HumDiv, FATHMM and MutationTaster scores from dbNSFP through MyVariant.info (version printed); CADD
  through its versioned API (v1.6 and v1.7, GRCh37 and GRCh38, the claims file's readings),
  gnomAD through its GraphQL API (v3.1.2 genomes and v4.1, the claims file's readings),
  ClinVar from its dated November 2024 VCF releases, UniProt from UniSave at the entry
  versions current in November 2024, and InterPro from its API (release printed).
- Physicochemical values follow the ExPASy ProtParam definitions (Gasteiger et al. 2005, the
  documentation of the tool Methods 2.6 names): average residue masses of ExPASy's Compute
  pI/Mw table, the Bjellqvist pK values for pI and the Guruprasad instability index (as in
  Biopython's ProteinAnalysis, which implements ProtParam), the Ikai aliphatic index and the
  Kyte-Doolittle GRAVY.
"""

from __future__ import annotations

import io
import re
import time
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

import fsspec
import imagecodecs
import numpy as np
import pandas as pd
import requests
import tifffile

DANDISET_ID = "001882"
DANDISET_VERSION = "0.260701.1757"
API = "https://api.dandiarchive.org/api"

TABLE_PATH = "derivatives/small table for 7 patients 20241127.xlsx"
DOCX_PATH = "sourcedata/protein structure and stabilityIMPG2 TABLE original.docx"
FIG1_PATH = "sub-01/micr/sub-01_sample-01_microscopy.ome.tif.jpg"
FIG2_PATH = "sub-01/micr/sub-01_sample-02_microscopy.ome.tif.tif"
FIG3_PATH = "sub-01/micr/Fig 3. VMD 20241122.1-01.tif"
FIG4A_PATH = "sub-01/micr/sub-01_sample-04a_microscopy.ome.tif.tif"
FIG4B_PATH = "sub-01/micr/sub-01_sample-04b_microscopy.ome.tif.tif"


def _get(url, tries=4, **kw):
    for i in range(tries):
        try:
            r = requests.get(url, timeout=kw.pop("timeout", 120), **kw)
            if r.status_code == 200:
                return r
        except requests.RequestException:
            pass
        time.sleep(5 * (i + 1))
    raise RuntimeError(f"could not fetch {url}")


def _post(url, tries=4, **kw):
    for i in range(tries):
        try:
            r = requests.post(url, timeout=600, **kw)
            if r.status_code == 200:
                return r
        except requests.RequestException:
            pass
        time.sleep(10 * (i + 1))
    raise RuntimeError(f"could not post to {url}")


# ---------------------------------------------------------------- the dandiset

@lru_cache(maxsize=1)
def assets() -> pd.DataFrame:
    """Every asset of the pinned version: path, size and asset id."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    rows = [dict(path=a["path"], size=a["size"], asset_id=a["asset_id"])
            for a in _get(url).json()["results"]]
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


@lru_cache(maxsize=1)
def dandiset_metadata() -> dict:
    return _get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/").json()


def asset_url(path: str) -> str:
    aid = assets().set_index("path").loc[path, "asset_id"]
    r = requests.head(f"{API}/assets/{aid}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


def read_bytes(path: str) -> bytes:
    return _get(asset_url(path)).content


def read_image(path: str) -> np.ndarray:
    """A figure file streamed from the archive into an array (rows, columns, RGB)."""
    if path.endswith(".jpg"):
        return imagecodecs.jpeg8_decode(read_bytes(path))
    with fsspec.open(asset_url(path), block_size=2**25) as f:
        a = tifffile.TiffFile(f).pages[0].asarray()
    return a[..., :3]


def image_header(path: str) -> dict:
    """Shape, software and date of a TIFF figure file, from its header only."""
    with fsspec.open(asset_url(path), block_size=2**20) as f:
        p = tifffile.TiffFile(f).pages[0]
        tags = {t.name: t.value for t in p.tags.values()}
    return dict(shape=p.shape, dtype=str(p.dtype), software=tags.get("Software"),
                datetime=tags.get("DateTime"), xmp="XMP" in tags)


# ---------------------------------------------------------------- the patient table

TABLE_COLUMNS = ["patient", "gene", "cdna", "protein", "zygosity", "mutation_type",
                 "diagnosis", "va", "refraction", "clinvar", "pathogenicity", "location"]


def load_patients() -> pd.DataFrame:
    """The spreadsheet's patients, without its first column (record numbers, never shown)."""
    raw = pd.read_excel(io.BytesIO(read_bytes(TABLE_PATH)), header=None)
    header = [str(h).strip() for h in raw.iloc[0]]
    body = raw.iloc[1:, 2:].copy()                       # column 0: record numbers; column 1 empty
    body = body.drop(columns=[10])                       # empty column between VA and Refraction
    body.columns = TABLE_COLUMNS
    body = body.map(lambda v: v.strip() if isinstance(v, str) else v).reset_index(drop=True)
    body.attrs["header"] = [h for i, h in enumerate(header) if i >= 2 and i != 10]
    body["sex"] = body["patient"].str[0]
    body["age"] = body["patient"].str[1:].astype(int)
    va = body["va"].str.split(r"\s*[–-]\s*", regex=True)
    body["va_od"] = va.str[0]
    body["va_os"] = va.str[1]
    return body


def table_shape() -> tuple[int, int]:
    raw = pd.read_excel(io.BytesIO(read_bytes(TABLE_PATH)), header=None)
    return raw.shape


def snellen_denominator(v: str) -> int:
    """20/x as x (larger is worse)."""
    num, den = v.split("/")
    assert num == "20", v
    return int(den)


# ---------------------------------------------------------------- the Word document

def load_docx():
    """Paragraphs and tables of the source document (python-docx)."""
    import docx
    d = docx.Document(io.BytesIO(read_bytes(DOCX_PATH)))
    paragraphs = [p.text for p in d.paragraphs if p.text.strip()]
    tables = [[[c.text.strip() for c in r.cells] for r in t.rows] for t in d.tables]
    return paragraphs, tables, len(d.inline_shapes)


def docx_images() -> list[tuple[str, np.ndarray]]:
    """The images embedded in the source document, decoded in memory: (part name, RGB array)."""
    import docx
    d = docx.Document(io.BytesIO(read_bytes(DOCX_PATH)))
    out = []
    for s in d.inline_shapes:
        part = d.part.related_parts[s._inline.graphic.graphicData.pic.blipFill.blip.embed]
        if "tif" in part.content_type:
            a = tifffile.TiffFile(io.BytesIO(part.blob)).pages[0].asarray()
        else:
            a = {"image/png": imagecodecs.png_decode, "image/jpeg": imagecodecs.jpeg8_decode}[part.content_type](part.blob)
        out.append((part.partname, a[..., :3] if a.ndim == 3 else a))
    return out


def first_number(text: str) -> float | None:
    m = re.search(r"-?\d+(?:\.\d+)?", text.replace("−", "-"))
    return float(m.group()) if m else None


# ---------------------------------------------------------------- figure panels

# Full-resolution pixel boxes (row0, row1, col0, col1) of each panel; layout, not data.
FIG2_ROWS = {"F32 OD": (191, 1297), "F32 OS": (1310, 2424),
             "M83 OD": (2543, 3657), "M83 OS": (3666, 4784)}
FIG2_COLS = {"FF": (361, 1480), "FAF": (1544, 2662), "GVF": (2722, 3849), "OCT": (3904, 8441)}
FIG3_ROWS = {"M75 OD": (295, 1852), "M75 OS": (1852, 3409), "M82 OD": (3619, 5185),
             "M82 OS": (5185, 6750), "M73 OD": (6969, 8535), "M73 OS": (8535, 10100),
             "F57 OD": (10311, 11877), "F57 OS": (11877, 13442), "M34 OD": (13652, 15235),
             "M34 OS": (15235, 16809)}
FIG3_COLS = {"OCT": (337, 5151), "FF": (5193, 6776), "FAF": (6835, 8418), "FFA": (8476, 10058)}


def panel(img: np.ndarray, figure: int, eye: str, modality: str) -> np.ndarray:
    rows, cols = (FIG2_ROWS, FIG2_COLS) if figure == 2 else (FIG3_ROWS, FIG3_COLS)
    r0, r1 = rows[eye]
    c0, c1 = cols[modality]
    return img[r0:r1, c0:c1]


def panel_signal(p: np.ndarray) -> dict:
    """Mean grey level and fraction of non-black pixels; an empty (NA) panel is near zero."""
    g = p.mean(axis=2)
    return dict(mean=float(g.mean()), nonblack=float((g > 20).mean()))


# FAF lesion centres (full-resolution row, column of Figure 3), where the yellow arrows point.
FAF_LESIONS = {"M75 OD": (1072, 7586), "M75 OS": (2588, 7676), "M73 OD": (7738, 7586),
               "M73 OS": (9282, 7612), "F57 OD": (11062, 7612), "F57 OS": (12654, 7598),
               "M34 OD": (14454, 7598), "M34 OS": (16074, 7676)}
FAF_RADII = (16, 32, 48)          # lesion disc radii, full-resolution pixels
SURROUND = (80, 140)              # annulus around the lesion centre, full-resolution pixels
MACULA = (24, 48)                 # inner annulus: the macula next to the lesion
NULL_RADIUS, NULL_N = 110, 36     # background discs: centres on a circle of this radius


def overlay_mask(win: np.ndarray) -> np.ndarray:
    """Pixels of the yellow arrows (and yellow labels) drawn on the figure: red and green high,
    blue low. Grey FAF pixels have equal channels, so no image pixel is caught."""
    w = win.astype(int)
    return (w[..., 0] > 180) & (w[..., 1] > 180) & (w[..., 2] < 120)


def faf_measures(img: np.ndarray, centre: tuple[int, int]) -> dict:
    """Lesion measures on an FAF panel, relative to the median grey level of the annulus around it.

    Arrow pixels are left out of every measure (`overlay_mask`). `mean_r<R>`: mean in a disc of
    radius R (above 1 brighter than the surrounding fundus); `p95_r16` and `max_r16`: 95th
    percentile and maximum within 16 pixels, which pick up small bright (hyper-autofluorescent)
    foci; `p95_mac`: the same 95th percentile against the median of the macula next to the lesion
    (`MACULA`); `hypo_area`: pixels within 100 of the centre darker than 0.85 of the surround.

    Reference for a bright focus: `NULL_N` discs of radius 16 centred `NULL_RADIUS` pixels from the
    lesion, on the background fundus of the same panel, skipping any disc that touches an arrow.
    `null_p95_q95` and `null_max_q95` are the 95th percentiles over those discs of the same two
    statistics, and `frac_null_p95`, `frac_null_max` the fraction of discs at least as bright as
    the lesion. The normal macula is darker than its surround on FAF (macular pigment), so a mean
    below 1 alone does not show a lesion. The radii are a standard choice, not the paper's."""
    r, c = centre
    h = NULL_RADIUS + 30
    raw = img[r - h:r + h + 1, c - h:c + h + 1]
    win = raw.mean(axis=2)
    ok = ~overlay_mask(raw)
    yy, xx = np.mgrid[-h:h + 1, -h:h + 1]
    d = np.hypot(yy, xx)
    sur = float(np.median(win[(d >= SURROUND[0]) & (d <= SURROUND[1]) & ok]))
    mac = float(np.median(win[(d >= MACULA[0]) & (d <= MACULA[1]) & ok]))
    out = {f"mean_r{R}": float(win[(d <= R) & ok].mean() / sur) for R in FAF_RADII}
    les = win[(d <= 16) & ok]
    out["p95_r16"] = float(np.percentile(les, 95) / sur)
    out["max_r16"] = float(les.max() / sur)
    out["p95_mac"] = float(np.percentile(les, 95) / mac)
    out["hypo_area"] = int(((win < 0.85 * sur) & (d <= 100) & ok).sum())
    null = []
    for t in np.linspace(0, 2 * np.pi, NULL_N, endpoint=False):
        m = np.hypot(yy - NULL_RADIUS * np.sin(t), xx - NULL_RADIUS * np.cos(t)) <= 16
        if (m & ~ok).any():
            continue
        null.append((np.percentile(win[m], 95) / sur, win[m].max() / sur))
    null = np.array(null)
    out.update(n_null=len(null), null_p95_q95=float(np.quantile(null[:, 0], 0.95)),
               null_max_q95=float(np.quantile(null[:, 1], 0.95)),
               frac_null_p95=float((null[:, 0] >= out["p95_r16"]).mean()),
               frac_null_max=float((null[:, 1] >= out["max_r16"]).mean()))
    out["arrow_px_in_ring"] = int((~ok & (d >= SURROUND[0]) & (d <= SURROUND[1])).sum())
    out["surround"] = sur
    return out


# Arrow colours of each figure and modality, read off the figures (yellow, blue, magenta, red).
ARROW_COLOURS = {(2, "FF"): ("yellow",), (2, "GVF"): ("red",), (3, "FF"): ("blue",)}
ARROW_DEFAULT = ("yellow", "magenta", "blue")


def arrow_boxes(p: np.ndarray, figure: int, modality: str, min_px: int = 300,
                margin: int = 200) -> list[tuple[int, int, int, int]]:
    """Boxes (row0, row1, col0, col1) around each arrow of a panel, widened by `margin` pixels on
    every side and clipped to the panel, for full-resolution crops of what the arrows point at.
    The colours looked for are `ARROW_COLOURS` (yellow is not looked for on the colour photographs
    of Figure 3, whose fundus has yellow areas). A standard choice for display only."""
    from scipy import ndimage
    w = p.astype(int)
    r, g, b = w[..., 0], w[..., 1], w[..., 2]
    masks = dict(yellow=overlay_mask(p), magenta=(r > 180) & (g < 90) & (b > 90),
                 blue=(r < 60) & (g > 130) & (g < 210) & (b > 200), red=(r > 150) & (g < 60) & (b < 60))
    mask = np.zeros(p.shape[:2], bool)
    for c in ARROW_COLOURS.get((figure, modality), ARROW_DEFAULT):
        mask |= masks[c]
    lab, n = ndimage.label(mask)
    out = []
    for i, sl in enumerate(ndimage.find_objects(lab), start=1):
        h, wd = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        if h > 400 or wd > 400 or (lab[sl] == i).sum() < min_px:
            continue                                                       # a panel frame or a speck
        out.append((max(sl[0].start - margin, 0), min(sl[0].stop + margin, p.shape[0]),
                    max(sl[1].start - margin, 0), min(sl[1].stop + margin, p.shape[1])))
    return out


# ---------------------------------------------------------------- variants and outside data

# Table 1 variants as HGVS on the gene symbol (VEP maps them to the MANE Select transcript).
VARIANTS = {"IMPG1 p.Leu740Phe": "IMPG1:c.2218C>T", "IMPG1 p.Asp423Glu": "IMPG1:c.1269C>A",
            "IMPG2 p.Cys1019Tyr": "IMPG2:c.3056G>A", "IMPG2 p.Arg131Cys": "IMPG2:c.391C>T",
            "IMPG2 p.Leu249Phe": "IMPG2:c.745C>T", "IMPG2 p.Arg964*": "IMPG2:c.2890C>T",
            "IMPG2 p.Arg1088*": "IMPG2:c.3262C>T"}
ENSEMBL = "https://rest.ensembl.org"
MYVARIANT = "https://myvariant.info/v1"


def ensembl_release() -> int:
    return _get(f"{ENSEMBL}/info/data", headers={"Accept": "application/json"}).json()["releases"][0]


def positions() -> pd.DataFrame:
    """GRCh38 (and GRCh37) position of each Table 1 variant: the dbNSFP record (MyVariant.info) whose MANE Select
    transcript (ENST00000369950, IMPG1; ENST00000193391, IMPG2) carries the cDNA change."""
    mane = {"IMPG1": "ENST00000369950", "IMPG2": "ENST00000193391"}
    rows = []
    for name, hgvs in VARIANTS.items():
        gene, c = hgvs.split(":")
        hits = _get(f"{MYVARIANT}/query", params={"q": f'dbnsfp.genename:{gene} AND dbnsfp.hgvsc:"{c}"',
                                                  "assembly": "hg38", "fields": "dbnsfp.ensembl.transcriptid,dbnsfp.hgvsc,dbnsfp.hg19"}).json()["hits"]
        keep = []
        for h in hits:
            tx, hc = h["dbnsfp"]["ensembl"]["transcriptid"], h["dbnsfp"]["hgvsc"]
            tx, hc = (tx if isinstance(tx, list) else [tx]), (hc if isinstance(hc, list) else [hc])
            if (mane[gene], c) in zip(tx, hc):
                keep.append(h["_id"])
                pos37 = h["dbnsfp"]["hg19"]["start"]
        assert len(keep) == 1, (hgvs, keep)
        m = re.match(r"chr(\w+):g\.(\d+)([ACGT])>([ACGT])", keep[0])
        assert (m.group(3), m.group(4)) == genomic_alleles(hgvs), (hgvs, keep[0])
        rows.append(dict(variant=name, hgvs=hgvs, chrom=m.group(1), pos=int(m.group(2)), pos37=int(pos37),
                         transcript=mane[gene]))
    return pd.DataFrame(rows)


def vep(pos: pd.DataFrame, server: str = ENSEMBL) -> pd.DataFrame:
    """SIFT and PolyPhen-2 (HumVar, VEP's default) on the MANE Select transcript, one request per
    variant, sent together; a variant VEP does not answer for is left empty and reported."""
    def one(r):
        row = dict(variant=r.variant, answered=False, pos_vep=None, refseq=None, aa=None, protein_pos=None,
                   sift=None, sift_call=None, polyphen=None, polyphen_call=None, rsid=None, consequence=None)
        for i in range(3):
            try:
                resp = requests.get(f"{server}/vep/human/hgvs/{requests.utils.quote(r.hgvs)}",
                                    params={"mane": 1, "canonical": 1}, headers={"Accept": "application/json"},
                                    timeout=300)
                if resp.status_code != 200:
                    time.sleep(10)
                    continue
                v = resp.json()[0]
                t = [x for x in v["transcript_consequences"] if x["transcript_id"] == r.transcript][0]
                rs = [c["id"] for c in v.get("colocated_variants", []) if c["id"].startswith("rs")]
                row.update(answered=True, pos_vep=v["start"], refseq=t.get("mane_select"), aa=t.get("amino_acids"),
                           protein_pos=t.get("protein_start"), sift=t.get("sift_score"),
                           sift_call=t.get("sift_prediction"), polyphen=t.get("polyphen_score"),
                           polyphen_call=t.get("polyphen_prediction"), rsid=",".join(rs),
                           consequence=",".join(t["consequence_terms"]))
                break
            except (requests.RequestException, ValueError, IndexError, KeyError):
                time.sleep(10)
        return row

    todo, done = list(pos.itertuples()), {}
    for _ in range(3):                                         # VEP answers slowly; ask for all at once
        with ThreadPoolExecutor(max_workers=len(todo)) as ex:
            for r, row in zip(todo, ex.map(one, todo)):
                done[r.variant] = row
        todo = [r for r in todo if not done[r.variant]["answered"]]
        if not todo:
            break
    rows = [done[v] for v in pos.variant]
    return pd.DataFrame(rows)


_COMPLEMENT = str.maketrans("ACGT", "TGCA")


def genomic_alleles(hgvs: str) -> tuple[str, str]:
    """Forward-strand reference and alternate alleles; IMPG1 and IMPG2 are on the minus strand."""
    ref, alt = re.search(r"([ACGT])>([ACGT])", hgvs).groups()
    return ref.translate(_COMPLEMENT), alt.translate(_COMPLEMENT)


def cadd(chrom: str, pos: int, alt: str, build: str, version: str) -> tuple[float, float]:
    """CADD PHRED and raw score from the versioned CADD API."""
    r = _get(f"https://cadd.gs.washington.edu/api/v1.0/{build}-{version}/{chrom}:{pos}").json()
    hit = [x for x in r if x["Alt"] == alt]
    return float(hit[0]["PHRED"]), float(hit[0]["RawScore"])


def dbnsfp(chrom: str, pos: int, ref: str, alt: str) -> dict:
    """dbNSFP scores of a GRCh38 variant through MyVariant.info: SIFT, PolyPhen-2 HumDiv and HumVar,
    FATHMM, FATHMM-MKL and FATHMM-XF coding scores, MutationTaster and CADD.

    dbNSFP gives some scores once per transcript (SIFT, FATHMM) and MutationTaster once per model,
    and MyVariant.info drops the missing entries of these lists, so a list cannot always be lined
    up with the transcript list. Every value is kept, as a list, with the transcript list beside
    it; `mane_index` is the place of the MANE Select transcript in that list."""
    fields = ",".join(f"dbnsfp.{f}" for f in ("ensembl.transcriptid", "sift.score", "polyphen2", "fathmm.score",
                                               "fathmm-mkl.coding_score", "fathmm-xf.coding_score",
                                               "mutationtaster.score", "mutationtaster.pred",
                                               "mutationtaster.model", "cadd.phred"))
    d = _get(f"{MYVARIANT}/variant/chr{chrom}:g.{pos}{ref}>{alt}",
             params={"assembly": "hg38", "fields": fields}).json().get("dbnsfp", {})

    def lst(v):
        return None if v is None else (v if isinstance(v, list) else [v])
    pp = d.get("polyphen2") or {}
    tx = lst((d.get("ensembl") or {}).get("transcriptid")) or []
    mane = [t for t in tx if t in ("ENST00000369950", "ENST00000193391")]
    return dict(transcripts=tx, mane_index=tx.index(mane[0]) if mane else None,
                sift=lst((d.get("sift") or {}).get("score")),
                polyphen_hdiv=(pp.get("hdiv") or {}).get("score"), polyphen_hvar=(pp.get("hvar") or {}).get("score"),
                fathmm=lst((d.get("fathmm") or {}).get("score")),
                fathmm_mkl=(d.get("fathmm-mkl") or {}).get("coding_score"),
                fathmm_xf=(d.get("fathmm-xf") or {}).get("coding_score"),
                mutationtaster=lst((d.get("mutationtaster") or {}).get("score")),
                mutationtaster_model=lst((d.get("mutationtaster") or {}).get("model")),
                mutationtaster_pred=lst((d.get("mutationtaster") or {}).get("pred")),
                cadd=(d.get("cadd") or {}).get("phred"))


def dbnsfp_version() -> dict:
    m = _get(f"{MYVARIANT}/metadata").json()
    return dict(build=m.get("build_version"), dbnsfp=m["src"]["dbnsfp"]["version"])


FATHMM_MKL = "http://fathmm.biocompute.org.uk"


def fathmm_mkl(variants: list[tuple[str, int, str, str]]) -> pd.DataFrame:
    """FATHMM-MKL web server (the FATHMM site of Methods 2.2), GRCh37 positions, forward strand:
    coding and non-coding scores and feature groups of each (chromosome, position, ref, alt)."""
    batch = "\n".join(f"{c},{p},{r},{a}" for c, p, r, a in variants)
    page = _post(f"{FATHMM_MKL}/cgi-bin/submitMKL.cgi", files={"batch": (None, batch)}).text
    session = re.search(r"session=([\w-]+)", page).group(1)
    for _ in range(30):
        time.sleep(10)
        html = _get(f"{FATHMM_MKL}/cgi-bin/results.cgi", params={"session": session}).text
        cells = [re.sub(r"<[^>]+>|\s+", " ", x).strip() for x in re.findall(r"<td[^>]*>(.*?)</td>", html, flags=re.S)]
        rows = [cells[i:i + 7] for i in range(0, len(cells) - 6) if re.fullmatch(r"\d+|X|Y", cells[i])
                and cells[i + 1].isdigit() and "/" in cells[i + 2]]
        if len(rows) >= len(variants):
            return pd.DataFrame([dict(chrom=r[0], pos37=int(r[1]), alleles=r[2], noncoding=float(r[3]),
                                      noncoding_groups=r[4], coding=float(r[5]), coding_groups=r[6]) for r in rows])
    raise RuntimeError("FATHMM-MKL did not answer")


def mutationtaster2021_status() -> dict:
    """What the MutationTaster2021 API (the documented URL, with its own example variant) answers."""
    url = "https://www.genecascade.org/MT2021/MT_API102.cgi?variants=21:33039603A%3EC"
    r = requests.get(url, timeout=120, allow_redirects=False)
    return dict(url=url, status=r.status_code, location=r.headers.get("Location"))


MUPRO = "https://mupro.proteomics.ics.uci.edu/cgi-bin/predict.pl"
IMUTANT = "https://folding.biofold.org/cgi-bin/i-mutant2.0.cgi"


def mupro(seq: str, pos: int, wt: str, mut: str) -> dict:
    """MuPRO web server, sequence only, its recommended output (SVM value and sign of the change)."""
    assert seq[pos - 1] == wt
    html = _post(MUPRO, files={"input_name": (None, "q"), "position": (None, str(pos)), "org_aa": (None, wt),
                               "rep_aa": (None, mut), "input_text": (None, seq)}).text
    txt = re.sub(r"<[^>]+>", " ", html)
    m = re.search(r"delta G =\s*(-?[\d.]+)\s*\((\w+) stability\)", txt)
    return dict(ddg=float(m.group(1)), effect=m.group(2))


def imutant(seq: str, pos: int, mut: str, mode: str) -> dict:
    """I-Mutant 2.0 web server from sequence, at its default 25 C and pH 7. `mode` 'ddg' gives the
    regression DDG (kcal/mol; DDG<0 decrease stability, as the server prints), 'sddg' the sign
    classifier (Increase or Decrease, with its reliability index 0 to 10)."""
    page = _post(IMUTANT, data={"proteina": seq, "posizione": str(pos), "newres": mut, "temp": "25", "ph": "7",
                                "pred": mode, "email": "", "submit": "Submit"}).text
    url = re.search(r"https://folding\.biofold\.org/i-mutant//www-data/output/Mut\d+/output\.html", page).group()
    for _ in range(40):
        time.sleep(10)
        txt = re.sub(r"<[^>]+>", " ", requests.get(url, timeout=60).text)
        if mode == "ddg":
            m = re.search(rf"\b{pos}\s+([A-Z])\s+{mut}\s+(-?[\d.]+)\s+7\.0\s+25", txt)
            if m:
                return dict(wt=m.group(1), ddg=float(m.group(2)))
        else:
            m = re.search(rf"\b{pos}\s+([A-Z])\s+{mut}\s+(Increase|Decrease)\s+(\d+)\s+7\.0\s+25", txt)
            if m:
                return dict(wt=m.group(1), sign=m.group(2), ri=int(m.group(3)))
    raise RuntimeError("I-Mutant did not answer")


GNOMAD = "https://gnomad.broadinstitute.org/api"
_GNOMAD_Q = """query($v:String!,$d:DatasetId!){ variant(variantId:$v, dataset:$d){ variant_id
 %s } }"""
_POP = "ac an populations{ id ac an }"


def gnomad(variant_id: str, dataset: str) -> dict:
    """Allele counts and numbers per part (exome, genome, joint) and population."""
    parts = ["genome"] if dataset == "gnomad_r3" else ["exome", "genome", "joint"]
    q = _GNOMAD_Q % " ".join(f"{p}{{ {_POP} }}" for p in parts)
    for i in range(6):
        time.sleep(2)
        try:
            r = requests.post(GNOMAD, json={"query": q, "variables": {"v": variant_id, "d": dataset}},
                              timeout=120)
            d = r.json()
            break
        except (requests.RequestException, ValueError):
            time.sleep(10 * (i + 1))
    else:
        raise RuntimeError("gnomAD did not answer")
    var = (d.get("data") or {}).get("variant")
    if not var:
        return {}
    return {p: {**{"all": (var[p]["ac"], var[p]["an"])},
                **{x["id"]: (x["ac"], x["an"]) for x in var[p]["populations"]}}
            for p in parts if var.get(p)}


CLINVAR_ARCHIVE = "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/archive_2.0/{}/clinvar_{}.vcf.gz"
CLINVAR_NOV_2024 = ("20241103", "20241111", "20241120", "20241126")


def clinvar_releases(year: int) -> list[str]:
    """Dates of the ClinVar GRCh38 VCF releases archived for a year."""
    html = _get(f"https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/archive_2.0/{year}/").text
    dates = sorted(set(re.findall(r"clinvar_(\d{8})\.vcf\.gz\"", html)))
    _CLINVAR_DIR.update({d: str(year) for d in dates})
    return dates


_CLINVAR_DIR = {}      # release date -> archive folder, where the two differ (releases late in December)


def clinvar_url(release: str) -> str:
    return CLINVAR_ARCHIVE.format(_CLINVAR_DIR.get(release, release[:4]), release)


def clinvar_summary(vcv: str) -> dict:
    """ClinVar's current summary of a variation (NCBI E-utilities esummary): title, classification,
    its last evaluation date, review status and conditions."""
    d = _get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
             params={"db": "clinvar", "id": vcv, "retmode": "json"}).json()["result"][vcv]
    g = d["germline_classification"]
    return dict(accession=d["accession_version"], title=d["title"], classification=g["description"],
                last_evaluated=g["last_evaluated"], review_status=g["review_status"],
                conditions=[t["trait_name"] for t in g["trait_set"]], submissions=d["supporting_submissions"]["scv"])


def clinvar_records(release: str, chrom: str, pos: int) -> list[dict]:
    """ClinVar VCF records at one position of a dated release, read through its tabix index."""
    import os
    import tempfile

    import pysam
    here = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp:     # htslib saves the remote index in the working directory
        os.chdir(tmp)
        try:
            lines = list(pysam.TabixFile(clinvar_url(release)).fetch(chrom, pos - 1, pos))
        finally:
            os.chdir(here)
    out = []
    for line in lines:
        f = line.split("\t")
        info = dict(kv.split("=", 1) for kv in f[7].split(";") if "=" in kv)
        out.append(dict(release=release, pos=int(f[1]), vcv=f[2], ref=f[3], alt=f[4],
                        clnsig=info.get("CLNSIG"), mc=info.get("MC"), gene=info.get("GENEINFO"),
                        rs=info.get("RS"), clnhgvs=info.get("CLNHGVS"), clndn=info.get("CLNDN"),
                        clnrevstat=info.get("CLNREVSTAT")))
    return out


def clinvar_md5(release: str) -> str:
    return _get(clinvar_url(release) + ".md5").text.split()[0]


# UniProt entry versions current in November 2024 (UniSave), when ProtParam was run (23 November).
UNISAVE = {"IMPG1": ("Q17R60", 129), "IMPG2": ("Q9BZV3", 146)}


def unisave(gene: str) -> tuple[str, list[tuple[str, int, int, str]], str]:
    """Sequence, features (type, start, end, note) and release line of a pinned UniProt entry."""
    acc, ver = UNISAVE[gene]
    t = _get(f"https://rest.uniprot.org/unisave/{acc}?format=txt&versions={ver}").text
    seq = re.sub(r"[^A-Z]", "", t.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0])
    feats, cur = [], None
    for line in t.splitlines():
        m = re.match(r"FT   (\w+)\s+(\d+)\.\.(\d+)", line)
        if m:
            cur = [m.group(1), int(m.group(2)), int(m.group(3)), ""]
            feats.append(cur)
        elif cur and line.startswith("FT   ") and "/note=" in line:
            cur[3] = line.split("/note=")[1].strip('"')
    feats = [tuple(f) for f in feats]
    return seq, feats, t.splitlines()[0]


def unisave_dates(gene: str) -> list[tuple[int, str, str]]:
    """Version, UniProt release and release date of the pinned entry version and the one after it."""
    acc, ver = UNISAVE[gene]
    d = _get(f"https://rest.uniprot.org/unisave/{acc}?format=json&versions={ver},{ver + 1}").json()
    return sorted((r["entryVersion"], r["firstRelease"], r["firstReleaseDate"]) for r in d["results"])


def interpro(acc: str) -> tuple[pd.DataFrame, dict]:
    """InterPro member-database domain locations of a UniProt entry, with the releases."""
    d = _get(f"https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{acc}?page_size=100").json()
    rows = []
    for e in d["results"]:
        m = e["metadata"]
        for p in e["proteins"]:
            for loc in p["entry_protein_locations"]:
                for fr in loc["fragments"]:
                    rows.append(dict(accession=m["accession"], db=m["source_database"],
                                     type=m["type"], name=m["name"], start=fr["start"], end=fr["end"]))
    rel = _get("https://www.ebi.ac.uk/interpro/api/").json()["databases"]
    return pd.DataFrame(rows), {k: rel[k]["version"] for k in ("interpro", "pfam", "smart", "profile")}


# ---------------------------------------------------------------- ProtParam

EXPASY_MASS = dict(A=71.0788, R=156.1875, N=114.1038, D=115.0886, C=103.1388, E=129.1155,
                   Q=128.1307, G=57.0519, H=137.1411, I=113.1594, L=113.1594, K=128.1741,
                   M=131.1926, F=147.1766, P=97.1167, S=87.0782, T=101.1051, W=186.2132,
                   Y=163.1760, V=99.1326)
WATER = 18.01524
# Atoms (C, H, N, O, S) of each residue within a chain; the chain adds one water.
RESIDUE_ATOMS = dict(A=(3, 5, 1, 1, 0), R=(6, 12, 4, 1, 0), N=(4, 6, 2, 2, 0), D=(4, 5, 1, 3, 0),
                     C=(3, 5, 1, 1, 1), Q=(5, 8, 2, 2, 0), E=(5, 7, 1, 3, 0), G=(2, 3, 1, 1, 0),
                     H=(6, 7, 3, 1, 0), I=(6, 11, 1, 1, 0), L=(6, 11, 1, 1, 0), K=(6, 12, 2, 1, 0),
                     M=(5, 9, 1, 1, 1), F=(9, 9, 1, 1, 0), P=(5, 7, 1, 1, 0), S=(3, 5, 1, 2, 0),
                     T=(4, 7, 1, 2, 0), W=(11, 10, 2, 1, 0), Y=(9, 9, 1, 2, 0), V=(5, 9, 1, 1, 0))


def protparam(seq: str) -> dict:
    from Bio.SeqUtils.ProtParam import ProteinAnalysis
    p = ProteinAnalysis(seq)
    n = len(seq)
    return dict(
        molecular_weight=sum(EXPASY_MASS[a] for a in seq) + WATER,
        theoretical_pI=p.isoelectric_point(),
        atoms=sum(sum(RESIDUE_ATOMS[a]) for a in seq) + 3,
        instability_index=p.instability_index(),
        aliphatic_index=100 * (seq.count("A") + 2.9 * seq.count("V")
                               + 3.9 * (seq.count("I") + seq.count("L"))) / n,
        gravy=p.gravy())


def mutate(seq: str, pos: int, ref: str, alt: str) -> str:
    assert seq[pos - 1] == ref, (pos, seq[pos - 1], ref)
    return seq[:pos - 1] + alt + seq[pos:]
