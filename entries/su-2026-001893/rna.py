"""Marker-gene read counts for the Patch-seq nuclei of dandiset 001893, from the
FASTQ files at the NeMO Archive (outside the dandiset).

Sources of every parameter:

- Which library belongs to which recorded cell: the dandiset's mapping.tsv
  (`session_id`, `library_aliquot_nhash_id`, `nemo_assets_url`), pinned with the
  dandiset; the files of each library and their MD5 sums come from the NeMO API
  (`/api/sample/<nemo id>`, `/api/file/<nemo id>`). The MD5 of every file read is
  checked, which pins the files.
- Markers: Dbh, Th, Slc6a2 and Slc18a2, the genes the paper uses for
  noradrenergic identity (Methods, Identification of noradrenergic cells;
  Retro-seq), as the claim's criterion names them. Controls (a standard choice
  that does not decide the outcome): Snap25 (pan-neuronal, expected present),
  Slc32a1 (GABAergic), Tph2 (serotonergic) and Alb (liver), expected absent.
- Counting: the paper aligned reads and counted exonic plus intronic reads as CPM
  (Methods, cDNA and sequencing); its aligner and reference are not stated in the
  claims file. Here a read pair counts for a gene when a 31-mer of either mate,
  taken every 4 bases, matches a 31-mer of the gene body (exons and introns, the
  mm39 = GRCm39 sequence between the gene's Ensembl release 116 coordinates, from
  the UCSC Genome Browser API) outside repeat-masked (lower-case) bases, on
  either strand. This substitutes exact k-mer matching for alignment, a deviation;
  31-mers are the length kallisto uses, a standard choice. CPM = pairs counted for
  the gene / all pairs x 1e6.
"""

from __future__ import annotations

import gzip
import hashlib
import io
import json
import time
import urllib.request

import numpy as np

NEMO_API = "https://assets.nemoarchive.org/api"
UCSC_API = "https://api.genome.ucsc.edu/getData/sequence"
K = 31
STRIDE = 4

# Ensembl release 116 gene coordinates on GRCm39 (1-based, inclusive), strand
GENES = {
    "Dbh": ("ENSMUSG00000000889", "chr2", 27055245, 27074212),
    "Th": ("ENSMUSG00000000214", "chr7", 142443466, 142484865),
    "Slc6a2": ("ENSMUSG00000055368", "chr8", 93686707, 93728295),
    "Slc18a2": ("ENSMUSG00000025094", "chr19", 59249238, 59284695),
    "Snap25": ("ENSMUSG00000027273", "chr2", 136533580, 136624362),
    "Slc32a1": ("ENSMUSG00000037771", "chr2", 158452605, 158464883),
    "Tph2": ("ENSMUSG00000006764", "chr10", 114914546, 115020927),
    "Alb": ("ENSMUSG00000029368", "chr5", 90608647, 90624696),
}
MARKERS = ("Dbh", "Th", "Slc6a2", "Slc18a2")

_COMP = str.maketrans("ACGTN", "TGCAN")


def _get(url, tries=6):
    """GET with retries; NeMO's file server drops some connections under parallel load."""
    for k in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=180) as r:
                return r.read()
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(5 * (k + 1))


def gene_sequence(chrom, start, end) -> str:
    """Soft-masked mm39 sequence, 1-based inclusive coordinates."""
    d = json.loads(_get(f"{UCSC_API}?genome=mm39;chrom={chrom};start={start - 1};end={end}"))
    return d["dna"]


def revcomp(s):
    return s.translate(_COMP)[::-1]


def gene_kmers() -> tuple[dict, dict]:
    """31-mer -> gene, over unmasked gene-body bases, both strands.

    K-mers shared by two genes are dropped. Returns (index, info per gene)."""
    index, info, shared = {}, {}, set()
    for g, (gid, chrom, a, b) in GENES.items():
        s = gene_sequence(chrom, a, b)
        n = 0
        for j in range(len(s) - K + 1):
            w = s[j:j + K]
            if not w.isupper() or "N" in w:
                continue
            for x in (w, revcomp(w)):
                if index.get(x, g) != g:
                    shared.add(x)
                index[x] = g
            n += 1
        info[g] = {"ensembl_id": gid, "region": f"{chrom}:{a}-{b}", "length": len(s),
                   "masked_fraction": float(np.mean([c.islower() for c in s])), "kmers": n}
    for x in shared:
        del index[x]
    return index, info


def library_files(nemo_lib_id: str) -> list[dict]:
    """The FASTQ files of one library aliquot: name, url, md5, size."""
    smp = json.loads(_get(f"{NEMO_API}/sample/{nemo_lib_id}"))
    out = []
    for furl in smp["files"]:
        f = json.loads(_get(furl))
        http = [u["url"] for u in f["manifest_file_urls"] if u["protocol"] == "http"]
        out.append({"nemo_id": f["id"], "name": f["file_name"], "url": http[0],
                    "md5": f["md5"], "size": f["size"], "library": smp["sample_name"]})
    return sorted(out, key=lambda x: x["name"])


def _reads(raw: bytes):
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as z:
        lines = z.read().decode().split("\n")
    return lines[1::4]


def count_library(files: list[dict], index: dict) -> dict:
    """Stream a library's FASTQ files into memory, check MD5, count read pairs per gene."""
    reads, md5_ok = [], True
    for f in files:
        raw = _get(f["url"])
        md5_ok &= hashlib.md5(raw).hexdigest() == f["md5"]
        reads.append(_reads(raw))
    n_pairs = min(len(r) for r in reads)
    counts = dict.fromkeys(GENES, 0)
    for j in range(n_pairs):
        hit = set()
        for r in reads:
            s = r[j]
            for p in range(0, len(s) - K + 1, STRIDE):
                g = index.get(s[p:p + K])
                if g is not None:
                    hit.add(g)
        for g in hit:
            counts[g] += 1
    return {"n_pairs": n_pairs, "n_reads": [len(r) for r in reads], "md5_ok": bool(md5_ok),
            "counts": counts, "cpm": {g: c / n_pairs * 1e6 for g, c in counts.items()}}


_INDEX = {}


def _count_one(lib):
    try:
        files = library_files(lib)
        res = count_library(files, _INDEX)
        if not res["md5_ok"]:
            return {"error": "MD5 mismatch", "files": files}
        return {"files": files, **res}
    except Exception as e:
        return {"error": repr(e)}


def count_all(nemo_lib_ids, index, workers=4) -> dict:
    """count_library for every library, in parallel processes (forked, sharing the index)."""
    import multiprocessing as mp
    from concurrent.futures import ProcessPoolExecutor
    global _INDEX
    _INDEX = index
    libs = list(nemo_lib_ids)
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as pool:
        out = dict(zip(libs, pool.map(_count_one, libs)))
    for _ in range(3):   # libraries whose download failed: again, one at a time
        for lib in [k for k, v in out.items() if "error" in v]:
            out[lib] = {**_count_one(lib), "retried": True}
    return out


# ----------------------------------------------------------------------------- NeMO collections
def nemo_collection(col_id: str) -> dict:
    """A NeMO collection record: name, child collections and manifest folder URLs."""
    c = json.loads(_get(f"{NEMO_API}/collection/{col_id}"))
    return {"id": c["id"], "name": c.get("name"),
            "children": [u.rsplit("/", 1)[-1] for u in c.get("child_collections") or []],
            "manifest_urls": [u["url"] for u in c.get("manifest_file_urls") or [] if u.get("protocol") == "http"]}


def list_http_dir(url: str) -> list[tuple[str, str]]:
    """(name, size) of every entry of an Apache directory listing, as the server gives them."""
    import re
    html = _get(url).decode()
    out = []
    for m in re.finditer(r'<a href="([^"?][^"]*)">[^<]*</a>\s*</td><td[^>]*>[^<]*</td><td[^>]*>\s*([^<]*?)\s*</td>', html):
        if not m.group(1).startswith("/"):
            out.append((m.group(1), m.group(2)))
    if not out:   # plain-text listings
        for m in re.finditer(r'<a href="([^"?/][^"]*)">[^<]*</a>\s+\S+\s+\S+\s+(\S+)', html):
            out.append((m.group(1), m.group(2)))
    return out


def read_manifest(url: str):
    """A tab-separated NeMO manifest, as a DataFrame."""
    import pandas as pd
    return pd.read_csv(io.BytesIO(_get(url)), sep="\t", dtype=str)


# ----------------------------------------------------------------------------- a check of the counting
# The Patch-seq libraries have no aligned counts at NeMO. The retro-seq nuclei of the same paper
# (SMART-seq v4, NeMO collection nemo:col-3qj1ect for the FASTQ files, nemo:col-afgz110 for the
# STAR 2.7 counts) have both, so the k-mer counts can be compared with STAR's for the same
# libraries. This checks the counting method only; the retro-seq claims are not tested here.
SSV4 = "https://data.nemoarchive.org/bican/grant/BICAN_Neuromodulation/aibs/transcriptome/nuclei/SSv4/house_mouse/"
SSV4_CPM = SSV4 + "processed/counts/NeMO_LC_260513_request_mouse_star2.7_cpm_sparse.Rdata"
SSV4_SAMPLES = SSV4 + "processed/cell_metrics/NeMO_LC_260513_request_mouse_star2.7_samp.dat.Rdata"
SSV4_FASTQ = SSV4 + "demultiplexed_fastq/"
SSV4_MANIFEST = SSV4_FASTQ + "col-3qj1ect_cohen_lcne1_RetroSeq_manifest.txt"


def _rdata(url):
    import warnings
    import rdata
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return rdata.conversion.convert(rdata.parser.parse_data(_get(url)), default_encoding="utf8")


def star_cpm(genes) -> "pd.DataFrame":
    """STAR CPM of the retro-seq nuclei for the given genes (nuclei x genes), from the
    dgCMatrix in the Rdata file, and the nuclei's sample table."""
    import pandas as pd
    m = next(iter(_rdata(SSV4_CPM).values()))
    rows, cols = m.Dimnames
    p, i, x = m.p, m.i, m.x
    out = pd.DataFrame(0.0, index=cols, columns=list(genes))
    where = {g: int(np.flatnonzero(rows == g)[0]) for g in genes if (rows == g).any()}
    for j, name in enumerate(cols):
        seg = slice(p[j], p[j + 1])
        hit = dict(zip(i[seg], x[seg]))
        for g, r in where.items():
            out.at[name, g] = hit.get(r, 0.0)
    samp = next(iter(_rdata(SSV4_SAMPLES).values()))
    return out, samp


def retroseq_files(names) -> dict:
    """FASTQ files (url, md5) of retro-seq libraries, from the collection's manifest."""
    man = read_manifest(SSV4_MANIFEST)
    out = {}
    for n in names:
        sel = man[man.library_aliquot_name == n].sort_values("filename")
        out[n] = [{"name": r.filename, "url": f"{SSV4_FASTQ}{n}/{r.filename}", "md5": r.checksum,
                   "size": int(r["size"]), "library": n} for _, r in sel.iterrows()]
    return out


def _count_files(files):
    try:
        res = count_library(files, _INDEX)
        if not res["md5_ok"]:
            return {"error": "MD5 mismatch", "files": files}
        return {"files": files, **res}
    except Exception as e:
        return {"error": repr(e)}


def count_files_all(files_by_name, index, workers=4) -> dict:
    import multiprocessing as mp
    from concurrent.futures import ProcessPoolExecutor
    global _INDEX
    _INDEX = index
    names = list(files_by_name)
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as pool:
        out = dict(zip(names, pool.map(_count_files, [files_by_name[n] for n in names])))
    for _ in range(3):   # downloads that failed: again, one at a time
        for n in [k for k, v in out.items() if "error" in v]:
            out[n] = {**_count_files(files_by_name[n]), "retried": True}
    return out
