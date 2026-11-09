"""Loading and measures for dandiset 001702 (Chaunsali et al. 2025, doi:10.1002/alz.70813).

The dandiset is streamed from the DANDI API at the pinned version `VERSION`. Its NWB files are read
with h5py over remfile; its videos are read with PyAV over remfile. Nothing is written to disk.

The bulk RNA-seq counts are not in the dandiset. They are read from the paper's GEO series
GSE317499 (the dandiset's metadata links it as a related resource), and checked against the
SHA-256 recorded in `GEO_COUNTS_SHA256`. GO annotations come from the Gene Ontology release
2024-06-17 (doi:10.5281/zenodo.12173881), read from the release's mirror.

Where each parameter comes from:
- DEG rule, adjusted p < 0.05 and |log2 fold change| > 1: Methods 2.5 (claim fig4b-3m-degs).
- DESeq2 defaults (Benjamini-Hochberg, independent filtering, Cooks outlier refit): the claim's
  criterion. Independent filtering is tuned at alpha 0.1, the default of R's results(), set
  explicitly since pydeseq2's default is 0.05; DESeq2 1.44.0 in R is replaced by pydeseq2, its Python port (deviation; R cannot be
  locked in the entry's environment).
- Model readings (separate per contrast, or one model on all 16 samples with a four-level group)
  and LFC readings (unshrunken, or apeglm-type shrinkage): the claim's criterion.
- GO enrichment, one-sided hypergeometric over-representation in Biological Process with
  Benjamini-Hochberg, backgrounds (a) genes tested by DESeq2 and (b) all BP-annotated mouse
  genes: the criterion of fig4d-3m-go-memory-terms-down. Annotations propagated over is_a and
  part_of, NOT qualifiers dropped, all evidence codes kept: standard choices of GO tools
  (goatools, GO.db). Term size: the paper names R and GOplot but no enrichment tool
  (Methods 2.5), so two readings are run, terms of 10 to 500 genes (clusterProfiler enrichGO's
  defaults) and no size limit.
- GOplot z-score, (up - down) / sqrt(count): the criterion (GOplot, Methods 2.5).
- GO release 2024-06-17: a standard choice near the paper's R 4.4.1 and DESeq2 1.44.0 (2024).
"""
from __future__ import annotations

import gzip
import hashlib
import io
import re
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy.stats import hypergeom
from statsmodels.stats.multitest import multipletests

DANDISET = "001702"
VERSION = "0.260216.2323"
API = "https://api.dandiarchive.org/api"

GEO_COUNTS_URL = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE317nnn/GSE317499/suppl/GSE317499_counts.csv.gz"
GEO_COUNTS_SHA256 = "dab6cf99a7c43d90ecea30b14d93099a7f522de4da17eaf2fd4bbb74b628e74a"
GEO_SAMPLES_URL = "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317499&targ=gsm&form=text&view=brief"

GO_RELEASE = "2024-06-17"
GO_DOI = "10.5281/zenodo.12173881"
# Two other releases, before and after, used only as a variant for the ECM claim (verifier, round 2).
GO_RELEASE_VARIANTS = {"2024-01-17": "10.5281/zenodo.10536401", "2025-03-16": "10.5281/zenodo.15066566"}
GO_URL = "https://release.geneontology.org/{release}/{path}"

DEG_PADJ = 0.05  # Methods 2.5
DEG_LFC = 1.0  # Methods 2.5
FILTER_ALPHA = 0.1  # R DESeq2 results() default; pydeseq2's DeseqStats default is 0.05
GO_MIN, GO_MAX = 10, 500  # clusterProfiler enrichGO defaults, one of two term-size readings (see docstring)


# ---------------------------------------------------------------- dandiset

def version_metadata() -> dict:
    """The archive's metadata of the pinned version (name, description, related resources)."""
    return requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60).json()


def list_assets() -> pd.DataFrame:
    """All assets of the pinned version: path, size, asset id, S3 URL and SHA-256."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000&metadata=1"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        for a in page["results"]:
            md = a.get("metadata") or {}
            rows.append(dict(path=a["path"], size=a["size"], asset_id=a["asset_id"],
                             s3=next((u for u in md.get("contentUrl", []) if "s3" in u), None),
                             sha256=(md.get("digest") or {}).get("dandi:sha2-256")))
        url = page["next"]
    df = pd.DataFrame(rows)
    missing = df.s3.isna() | df.sha256.isna()
    if missing.any():  # the list endpoint did not return metadata: ask per asset
        def one(aid):
            md = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{aid}/", timeout=60).json()
            return next(u for u in md["contentUrl"] if "s3" in u), md["digest"]["dandi:sha2-256"]
        with ThreadPoolExecutor(16) as ex:
            got = list(ex.map(one, df.loc[missing, "asset_id"]))
        df.loc[missing, "s3"] = [g[0] for g in got]
        df.loc[missing, "sha256"] = [g[1] for g in got]
    df["folder"] = df.path.str.split("/").str[0]
    df["ext"] = df.path.str.rsplit(".", n=1).str[-1]
    return df.sort_values("path").reset_index(drop=True)


def _text(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def scan_nwb(s3_url: str) -> dict:
    """What one NWB file holds: every dataset outside /specifications and /general, the members of
    the data groups, and the descriptive metadata."""
    with h5py.File(remfile.File(s3_url), "r") as f:
        datasets = []
        f.visititems(lambda n, o: datasets.append(n) if isinstance(o, h5py.Dataset)
                     and not n.startswith(("specifications", "general")) else None)
        groups = {k: sorted(f[k].keys()) for k in ("acquisition", "processing", "analysis", "stimulus") if k in f}
        stim = {k: sorted(f["stimulus"][k].keys()) for k in f["stimulus"].keys()} if "stimulus" in f else {}
        g = f["general"]
        return dict(
            datasets=tuple(sorted(datasets)),
            n_data_objects=sum(len(v) for v in groups.values()) + sum(len(v) for v in stim.values())
            - len(groups.get("stimulus", [])),
            groups=str(groups), stimulus_members=str(stim),
            identifier=_text(f["identifier"][()]),
            description=_text(g["experiment_description"][()]) if "experiment_description" in g else "",
            keywords=", ".join(_text(k) for k in g["keywords"][()]) if "keywords" in g else "",
            genotype=_text(g["subject/genotype"][()]) if "subject/genotype" in g else "",
            age=_text(g["subject/age"][()]) if "subject/age" in g else "",
            sex=_text(g["subject/sex"][()]) if "subject/sex" in g else "",
            subject_id=_text(g["subject/subject_id"][()]) if "subject/subject_id" in g else "",
        )


def scan_all_nwb(assets: pd.DataFrame, workers: int = 32) -> pd.DataFrame:
    nwb = assets[assets.ext == "nwb"]
    with ThreadPoolExecutor(workers) as ex:
        rows = list(ex.map(scan_nwb, nwb.s3))
    return pd.concat([nwb.reset_index(drop=True), pd.DataFrame(rows)], axis=1)


class _Clamped(io.RawIOBase):
    """A remfile that returns no bytes past its end, where PyAV reads (remfile raises there)."""

    def __init__(self, url):
        self.f = remfile.File(url)
        self.n = self.f.length
        self.pos = 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, off, whence=0):
        self.pos = {0: off, 1: self.pos + off, 2: self.n + off}[whence]
        return self.pos

    def tell(self):
        return self.pos

    def read(self, size=-1):
        size = self.n - self.pos if size is None or size < 0 else min(size, self.n - self.pos)
        if size <= 0:
            return b""
        self.f.seek(self.pos)
        data = self.f.read(size)
        self.pos += len(data)
        return data


def probe_video(s3_url: str, frame: bool = False):
    """Width, height, frame rate, duration and frame count of one video, and optionally its first
    frame as an array."""
    import av
    with av.open(_Clamped(s3_url)) as c:
        s = c.streams.video[0]
        out = dict(width=s.width, height=s.height, fps=float(s.average_rate),
                   duration_s=c.duration / 1e6, frames=s.frames)
        if frame:
            out["frame"] = next(c.decode(video=0)).to_ndarray(format="rgb24")
    return out


# ---------------------------------------------------------------- GEO counts

def load_counts() -> tuple[pd.DataFrame, pd.DataFrame]:
    """The GEO count matrix (genes by samples) and a sample table parsed from the column names
    (M3/M7 for age, 5xFAD+ or 5xFAD- for genotype), checked against GEO's sample records."""
    raw = requests.get(GEO_COUNTS_URL, timeout=120).content
    digest = hashlib.sha256(raw).hexdigest()
    if digest != GEO_COUNTS_SHA256:
        raise RuntimeError(f"GEO counts changed: sha256 {digest}")
    counts = pd.read_csv(io.BytesIO(gzip.decompress(raw))).set_index("Geneid")
    m = counts.columns.str.extract(r"^M(\d)_5xFAD([+-])(\d+)$")
    samples = pd.DataFrame({"age": "M" + m[0].values, "geno": np.where(m[1].values == "+", "pos", "neg"),
                            "number": m[2].astype(int).values}, index=counts.columns)
    samples["group"] = samples.age + "_" + samples.geno
    return counts, samples


def geo_sample_records() -> pd.DataFrame:
    """GEO's own record of each sample: title, genotype, batch, and the library description,
    whose leading number is the sample's number in the count matrix."""
    rows, cur = [], None
    for line in requests.get(GEO_SAMPLES_URL, timeout=60).text.splitlines():
        if line.startswith("^SAMPLE"):
            cur = {"gsm": line.split("= ")[1]}
            rows.append(cur)
        elif cur is not None and " = " in line:
            k, v = line.split(" = ", 1)
            if k == "!Sample_title":
                cur["title"] = v
            elif k == "!Sample_characteristics_ch1" and ":" in v:
                kk, vv = v.split(":", 1)
                cur[kk.strip()] = vv.strip()
            elif k == "!Sample_description":
                cur.setdefault("descriptions", []).append(v)
    df = pd.DataFrame(rows)
    df["library"] = df.descriptions.str[0].str.replace("Library name: ", "")
    df["run_name"] = df.descriptions.str[1]
    df["number"] = df.run_name.str.extract(r"^(\d+)_")[0].astype(int)
    return df.drop(columns="descriptions")


# ---------------------------------------------------------------- DESeq2 (pydeseq2)

def deseq(counts: pd.DataFrame, samples: pd.DataFrame, cols, factor: str, test: str, ref: str,
          alpha: float = FILTER_ALPHA, n_cpus: int | None = None) -> pd.DataFrame:
    """DESeq2 Wald test of `test` against `ref` for `factor`, on the samples `cols`, with DESeq2's
    defaults (independent filtering tuned at `alpha`, R results()'s default 0.1). Returns baseMean,
    the unshrunken log2 fold change (`lfc`), the apeglm-type shrunken one (`lfc_shrunk`), p,
    adjusted p, and the adjusted p with filtering tuned at 0.05 (`padj_filter005`, pydeseq2's
    default, as a variant). The reference level is renamed so that it sorts first,
    which makes `test` a coefficient of the model, as lfcShrink(coef=) needs."""
    from pydeseq2.dds import DeseqDataSet
    from pydeseq2.default_inference import DefaultInference
    from pydeseq2.ds import DeseqStats

    meta = samples.loc[cols, [factor]].copy()
    meta[factor] = meta[factor].replace({ref: "0ref"})
    inf = DefaultInference(n_cpus=n_cpus)
    dds = DeseqDataSet(counts=counts[cols].T, metadata=meta, design=f"~{factor}", inference=inf, quiet=True)
    dds.deseq2()
    st = DeseqStats(dds, contrast=[factor, test, "0ref"], alpha=alpha, inference=inf, quiet=True)
    st.summary()
    res = st.results_df[["baseMean", "log2FoldChange", "pvalue", "padj"]].rename(columns={"log2FoldChange": "lfc"})
    st05 = DeseqStats(dds, contrast=[factor, test, "0ref"], alpha=0.05, inference=inf, quiet=True)
    st05.summary()
    res["padj_filter005"] = st05.results_df["padj"]
    coeff = [c for c in dds.varm["LFC"].columns if test in c]
    st.lfc_shrink(coeff=coeff[0])
    res["lfc_shrunk"] = st.results_df["log2FoldChange"]
    return res


def degs(res: pd.DataFrame, lfc_col: str = "lfc", padj_col: str = "padj") -> tuple[set, set]:
    """Up and down DEGs, Methods 2.5: adjusted p < 0.05 and |log2 fold change| > 1."""
    sig = res[padj_col] < DEG_PADJ
    return set(res.index[sig & (res[lfc_col] > DEG_LFC)]), set(res.index[sig & (res[lfc_col] < -DEG_LFC)])


# ---------------------------------------------------------------- GO

def load_go(release: str = GO_RELEASE) -> tuple[dict, dict]:
    """GO Biological Process terms of a release, the pinned one by default (id -> name), and mouse
    gene symbol -> set of BP terms with their ancestors over is_a and part_of."""
    obo = requests.get(GO_URL.format(release=release, path="ontology/go-basic.obo"), timeout=300).text
    names, parents, space, obsolete = {}, defaultdict(set), {}, set()
    for block in obo.split("\n\n[Term]\n")[1:]:
        block = block.split("\n\n")[0]
        tid = re.search(r"^id: (GO:\d+)", block, re.M).group(1)
        names[tid] = re.search(r"^name: (.*)$", block, re.M).group(1)
        space[tid] = re.search(r"^namespace: (.*)$", block, re.M).group(1)
        if re.search(r"^is_obsolete: true", block, re.M):
            obsolete.add(tid)
        parents[tid] |= set(re.findall(r"^is_a: (GO:\d+)", block, re.M))
        parents[tid] |= set(re.findall(r"^relationship: part_of (GO:\d+)", block, re.M))
    anc = {}

    def ancestors(t):
        if t not in anc:
            s = {t}
            for p in parents.get(t, ()):
                s |= ancestors(p)
            anc[t] = s
        return anc[t]

    import sys
    sys.setrecursionlimit(10000)
    bp = {t for t, s in space.items() if s == "biological_process" and t not in obsolete}
    gaf = gzip.decompress(requests.get(GO_URL.format(release=release, path="annotations/mgi.gaf.gz"),
                                       timeout=300).content).decode()
    gene_terms = defaultdict(set)
    for line in gaf.splitlines():
        if line.startswith("!"):
            continue
        f = line.split("\t")
        if f[8] != "P" or "NOT" in f[3].split("|") or f[4] not in bp:
            continue
        gene_terms[f[2]] |= ancestors(f[4]) & bp
    return {t: names[t] for t in bp}, dict(gene_terms)


def enrich(up: set, down: set, universe: set, gene_terms: dict, names: dict,
           size: tuple[int, int] | None = (GO_MIN, GO_MAX)) -> pd.DataFrame:
    """Over-representation of the DEGs (up and down together) in GO BP terms against `universe`,
    one-sided hypergeometric test, Benjamini-Hochberg over the terms tested (those with at least
    one DEG and, when `size` is given, between size[0] and size[1] universe genes), as
    clusterProfiler's enrichGO does. Adds the GOplot z-score (up - down) / sqrt(count)."""
    universe = {g for g in universe if g in gene_terms}
    deg = (up | down) & universe
    term_genes = defaultdict(set)
    for g in universe:
        for t in gene_terms[g]:
            term_genes[t].add(g)
    rows = []
    n_univ, n_deg = len(universe), len(deg)
    for t, genes in term_genes.items():
        if size and not size[0] <= len(genes) <= size[1]:
            continue
        hit = genes & deg
        if not hit:
            continue
        rows.append(dict(term=t, name=names[t], size=len(genes), count=len(hit),
                         up=len(hit & up), down=len(hit & down),
                         p=hypergeom.sf(len(hit) - 1, n_univ, len(genes), n_deg)))
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["padj"] = multipletests(df.p, method="fdr_bh")[1]
    df["zscore"] = (df.up - df.down) / np.sqrt(df["count"])
    return df.sort_values(["padj", "p", "term"]).reset_index(drop=True)


MEMORY = re.compile(r"learning|memory|cognition", re.I)
IMMUNE = re.compile(r"immun|inflammat|defense response|(leukocyte|lymphocyte|T cell|B cell|myeloid|microglia\w*|"
                    r"macrophage|neutrophil|mononuclear|mast cell|natural killer|granulocyte|monocyte|"
                    r"dendritic cell)\b.*activation", re.I)
ECM = re.compile(r"extracellular matrix (organization|assembly|disassembly|secretion)|"
                 r"(organization|assembly|disassembly|secretion) of extracellular matrix", re.I)
