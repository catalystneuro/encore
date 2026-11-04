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


def faf_measures(img: np.ndarray, centre: tuple[int, int]) -> dict:
    """Lesion measures on an FAF panel, relative to the median grey level of the annulus around it.

    `mean_r<R>`: mean in a disc of radius R (above 1 brighter than the surrounding fundus);
    `p95_r16`: 95th percentile within 16 pixels, which picks up small bright (hyper-
    autofluorescent) foci; `hypo_area`: pixels within 100 of the centre darker than 0.85 of the
    surround. The normal macula is darker than its surround on FAF (macular pigment), so a
    mean below 1 alone does not show a lesion."""
    r, c = centre
    h = SURROUND[1]
    win = img[r - h:r + h + 1, c - h:c + h + 1].mean(axis=2)
    yy, xx = np.mgrid[-h:h + 1, -h:h + 1]
    d = np.hypot(yy, xx)
    sur = float(np.median(win[(d >= SURROUND[0]) & (d <= SURROUND[1])]))
    out = {f"mean_r{R}": float(win[d <= R].mean() / sur) for R in FAF_RADII}
    out["p95_r16"] = float(np.percentile(win[d <= 16], 95) / sur)
    out["hypo_area"] = int(((win < 0.85 * sur) & (d <= 100)).sum())
    out["surround"] = sur
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
    FATHMM, FATHMM-MKL and FATHMM-XF coding scores, MutationTaster and CADD."""
    fields = ",".join(f"dbnsfp.{f}" for f in ("sift.score", "polyphen2", "fathmm.score", "fathmm-mkl.coding_score",
                                               "fathmm-xf.coding_score", "mutationtaster.score",
                                               "mutationtaster.pred", "cadd.phred"))
    d = _get(f"{MYVARIANT}/variant/chr{chrom}:g.{pos}{ref}>{alt}",
             params={"assembly": "hg38", "fields": fields}).json().get("dbnsfp", {})

    def first(v):
        return v[0] if isinstance(v, list) else v
    pp = d.get("polyphen2") or {}
    return dict(sift=first((d.get("sift") or {}).get("score")),
                polyphen_hdiv=(pp.get("hdiv") or {}).get("score"), polyphen_hvar=(pp.get("hvar") or {}).get("score"),
                fathmm=first((d.get("fathmm") or {}).get("score")),
                fathmm_mkl=(d.get("fathmm-mkl") or {}).get("coding_score"),
                fathmm_xf=(d.get("fathmm-xf") or {}).get("coding_score"),
                mutationtaster=first((d.get("mutationtaster") or {}).get("score")),
                mutationtaster_pred=first((d.get("mutationtaster") or {}).get("pred")),
                cadd=(d.get("cadd") or {}).get("phred"))


def dbnsfp_version() -> dict:
    m = _get(f"{MYVARIANT}/metadata").json()
    return dict(build=m.get("build_version"), dbnsfp=m["src"]["dbnsfp"]["version"])


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


CLINVAR = "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/archive_2.0/2024/clinvar_{}.vcf.gz"
CLINVAR_NOV_2024 = ("20241103", "20241111", "20241120", "20241126")


def clinvar_records(release: str, chrom: str, pos: int) -> list[dict]:
    """ClinVar VCF records at one position of a dated release, read through its tabix index."""
    import os
    import tempfile

    import pysam
    here = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp:     # htslib saves the remote index in the working directory
        os.chdir(tmp)
        try:
            lines = list(pysam.TabixFile(CLINVAR.format(release)).fetch(chrom, pos - 1, pos))
        finally:
            os.chdir(here)
    out = []
    for line in lines:
        f = line.split("\t")
        info = dict(kv.split("=", 1) for kv in f[7].split(";") if "=" in kv)
        out.append(dict(release=release, pos=int(f[1]), vcv=f[2], ref=f[3], alt=f[4],
                        clnsig=info.get("CLNSIG"), mc=info.get("MC"), gene=info.get("GENEINFO"),
                        rs=info.get("RS")))
    return out


def clinvar_md5(release: str) -> str:
    return _get(CLINVAR.format(release) + ".md5").text.split()[0]


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
