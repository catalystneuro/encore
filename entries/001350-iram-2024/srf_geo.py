"""Loading and measures for the sequencing data of Iram, Garcia et al. (2024), deposited in NCBI GEO.

Iram, Garcia et al. (2024), PNAS 121(12) e2307250121, doi:10.1073/pnas.2307250121. The paper's
TEM images are dandiset 001350 (version 0.250511.1527, `srf_tem.py`); its ChIP-seq, bulk RNA-seq
and snRNA-seq are in GEO SuperSeries GSE241561 (claims file, `where`). Files are read into memory;
nothing is written to disk.

- ChIP-seq, GSE241559: the nf-core/chipseq outputs the paper describes (SI Methods,
  "Bioinformatics analysis of ChIP-seq data": nf-core ChIP-seq v1.2.1, BWA on Rnor 6.0, MACS2
  narrow peaks at BH FDR 0.05, HOMER annotation of the closest Ensembl feature). The SRF consensus
  peaks, their HOMER annotation, and the MACS2 peaks of each replicate (OPC R1 to R4, OLG R1 to R3)
  and of each IgG control.
- RNA-seq, GSE241560 (samples GSM7731029 to GSM7731043): RSEM `genes.results` per sample from
  nf-core RNA-seq v3.0 on GRCm38, read from the series' GSE241560_RAW.tar (SI Methods, "Bioinformatics analysis of RNA-seq data").
- Mouse gene names for the Ensembl gene ids come from the Ensembl release 102 GTF (the last
  GRCm38 release); the paper says only that annotations were "based on the Ensembl database".
- Peak sequences come from the UCSC rn6 genome (the same assembly as Ensembl Rnor 6.0), read by
  range requests from its 2bit file.

Where the parameters come from:

- DESeq2 "with standard settings" on the raw gene counts (SI Methods): pydeseq2 with its
  defaults (Wald test, Cook's distance filtering, independent filtering at alpha 0.05, BH
  adjustment), the Python port, as R is not available here. RSEM expected counts are rounded to
  integers, as DESeq2 requires; the length offsets that a tximport import would add are not
  applied (a deviation). Differentially expressed means padj < 0.05 (Results, "157
  differentially expressed genes ( P .adj < 0.05)").
- `MOTIF_HALF_WIDTH` = 250: the paper's motif search window, "-250 to +250 nt regions around
  detected peaks" (SI Methods), taken around the peak centre.
- CArG box, three readings: FIMO (the paper's tool, SI Methods: "FIMO (14) was used to get
  individual motif matches") with the JASPAR SRF matrix MA0083.3 at FIMO's default p < 1e-4, on a
  background of the peaks' base composition (MEME-ChIP builds its background from the input
  sequences); the consensus CC(A/T)6GG ("the SRF CArG consensus"); and the consensus with one
  mismatch. The paper ran FIMO on the motifs MEME-ChIP found; which motif it used is not stated,
  and MEME-ChIP's motif discovery is not run here (a deviation).
- `FLANK_OFFSET`: background windows of the same width centred 3 kb either side of the peak
  centre, a standard choice for a local background.
- `SHUFFLE_SEED` for the shuffled background; a detail that cannot change an outcome.
"""

from __future__ import annotations

import gzip
import hashlib
import io
import re
import struct
import tarfile
import time
from functools import lru_cache

import numpy as np
import pandas as pd
import requests

DANDISET_ID = "001350"
DANDISET_VERSION = "0.250511.1527"

GEO_SERIES = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE241nnn/GSE241559/suppl/"
GEO_RNA_TAR = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE241nnn/GSE241560/suppl/GSE241560_RAW.tar"
ENSEMBL_GTF = "https://ftp.ensembl.org/pub/release-102/gtf/mus_musculus/Mus_musculus.GRCm38.102.gtf.gz"
RN6_2BIT = "https://hgdownload.soe.ucsc.edu/goldenPath/rn6/bigZips/rn6.2bit"

RNASEQ_SAMPLES = pd.DataFrame(
    [("GSM7731029", "control_R1", "OPC", "Flox"), ("GSM7731030", "control_R2", "OPC", "Flox"),
     ("GSM7731031", "control_R3", "OPC", "Flox"), ("GSM7731032", "control_R4", "OPC", "Flox"),
     ("GSM7731033", "SRF-KO_R1", "OPC", "KO"), ("GSM7731034", "SRF-KO_R2", "OPC", "KO"),
     ("GSM7731035", "SRF-KO_R3", "OPC", "KO"),
     ("GSM7731036", "CTR_R1", "OL", "Flox"), ("GSM7731037", "CTR_R2", "OL", "Flox"),
     ("GSM7731038", "CTR_R3", "OL", "Flox"), ("GSM7731039", "CTR_R4", "OL", "Flox"),
     ("GSM7731040", "KO_R1", "OL", "KO"), ("GSM7731041", "KO_R2", "OL", "KO"),
     ("GSM7731042", "KO_R3", "OL", "KO"), ("GSM7731043", "KO_R4", "OL", "KO")],
    columns=["gsm", "name", "stage", "genotype"])   # sample titles in GEO: "control OPC replicate 1" and so on

CHIP_REPLICATES = {"OPC": ["OPC_IP_R1", "OPC_IP_R2", "OPC_IP_R3", "OPC_IP_R4"],
                   "OLG": ["OLG_IP_R1", "OLG_IP_R2", "OLG_IP_R3"]}
CHIP_IGG = {"OPC": "OPC_IgG_IP_R1", "OLG": "OLG_IgG_IP_R1"}

ALPHA = 0.05
MOTIF_HALF_WIDTH = 250
FLANK_OFFSET = 3000
SHUFFLE_SEED = 241561
CARG = re.compile(r"(?=(CC[AT]{6}GG))")

# Fig. S4E of the paper: "the main actin disassembly genes expressed by OPCs and oligodendrocytes".
DISASSEMBLY_GENES = ["Cfl1", "Cfl2", "Dstn", "Gsn", "Cap1", "Coro1a", "Coro1b", "Coro2b", "Ssh3",
                     "Mical3", "Twf1", "Gmfb", "Rhoa"]

fetched: dict[str, str] = {}   # url -> sha256 of what was read, for the notebook header


retries: dict[str, int] = {}   # url -> failed requests before it was read


def get(url: str, tries: int = 45) -> bytes:
    """A file into memory. NCBI's server refuses many requests from this runner (HTTP 403, or a
    dropped connection), sometimes for minutes at a time; each request is retried after a pause that
    grows from 10 to 60 seconds (about 40 minutes in all), and the last failure is raised."""
    for k in range(tries):
        try:
            r = requests.get(url, timeout=300)
            r.raise_for_status()
            break
        except requests.RequestException:
            if k == tries - 1:
                raise
            time.sleep(min(60, 10 + 5 * k))
    retries[url] = k
    fetched[url] = hashlib.sha256(r.content).hexdigest()
    return r.content


def get_gz_text(url: str) -> str:
    return gzip.decompress(get(url)).decode()


# --- RNA-seq ------------------------------------------------------------------------------------

def rnaseq_tables() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Expected counts, TPM and effective lengths, genes by sample (sample names as in GEO), from
    the series' archive of the per-sample files (one request in place of fifteen)."""
    tar = tarfile.open(fileobj=io.BytesIO(get(GEO_RNA_TAR)))
    members = {m.name: m for m in tar.getmembers()}
    counts, tpm, length = {}, {}, {}
    for s in RNASEQ_SAMPLES.itertuples():
        raw = tar.extractfile(members[f"{s.gsm}_{s.name}.genes.results.gz"]).read()
        df = pd.read_csv(io.StringIO(gzip.decompress(raw).decode()), sep="\t", index_col="gene_id")
        counts[s.name], tpm[s.name], length[s.name] = df.expected_count, df.TPM, df.effective_length
    return pd.DataFrame(counts), pd.DataFrame(tpm), pd.DataFrame(length)


def length_scaled_counts(counts: pd.DataFrame, tpm: pd.DataFrame, length: pd.DataFrame) -> pd.DataFrame:
    """tximport's lengthScaledTPM: TPM times the gene's mean effective length over samples, scaled
    to each sample's total expected count."""
    scaled = tpm * length.mean(1).to_numpy()[:, None]
    return scaled / scaled.sum() * counts.sum()


@lru_cache(maxsize=1)
def mouse_gene_names() -> pd.Series:
    names = {}
    with gzip.open(io.BytesIO(get(ENSEMBL_GTF)), "rt") as f:
        for line in f:
            if "\tgene\t" in line:
                gid = re.search(r'gene_id "([^"]+)"', line).group(1)
                m = re.search(r'gene_name "([^"]+)"', line)
                names[gid] = m.group(1) if m else gid
    return pd.Series(names, name="gene")


def deseq(counts: pd.DataFrame, samples: pd.DataFrame, design: str = "~genotype",
          contrast=("genotype", "KO", "Flox")) -> pd.DataFrame:
    """pydeseq2 with default settings on rounded counts; KO against Flox."""
    from pydeseq2.dds import DeseqDataSet
    from pydeseq2.ds import DeseqStats
    from pydeseq2.default_inference import DefaultInference
    meta = samples.set_index("name").loc[counts.columns]
    mat = counts.round().astype(int).T
    mat = mat.loc[:, mat.sum(0) > 0]
    dds = DeseqDataSet(counts=mat, metadata=meta, design=design, quiet=True,
                       inference=DefaultInference(n_cpus=1))
    dds.deseq2()
    st = DeseqStats(dds, contrast=list(contrast), alpha=ALPHA, quiet=True,
                    inference=DefaultInference(n_cpus=1))
    st.summary()
    res = st.results_df.copy()
    res["gene"] = mouse_gene_names().reindex(res.index).fillna(pd.Series(res.index, index=res.index))
    return res


# --- ChIP-seq -----------------------------------------------------------------------------------

def read_bed(name: str) -> pd.DataFrame:
    df = pd.read_csv(io.StringIO(get_gz_text(GEO_SERIES + name)), sep="\t", header=None)
    return df.iloc[:, :4].set_axis(["chr", "start", "end", "name"], axis=1).astype({"chr": str})


def read_macs_xls(sample: str) -> pd.DataFrame:
    txt = get_gz_text(GEO_SERIES + f"GSE241559_{sample}_peaks.xls.gz")
    df = pd.read_csv(io.StringIO(txt), sep="\t", comment="#")
    return df.astype({"chr": str})


def read_annotation() -> pd.DataFrame:
    df = pd.read_csv(io.StringIO(get_gz_text(GEO_SERIES + "GSE241559_SRF.consensus_peaks.annotatePeaks.txt.gz")),
                     sep="\t")
    df = df.rename(columns={df.columns[0]: "name"}).astype({"Chr": str})
    return df


def overlaps(a: pd.DataFrame, b: pd.DataFrame) -> np.ndarray:
    """For each interval of a, whether any interval of b overlaps it (same chromosome)."""
    out = np.zeros(len(a), bool)
    for c, ga in a.groupby("chr"):
        gb = b[b.chr == c]
        if gb.empty:
            continue
        s, e = gb.start.to_numpy(), gb.end.to_numpy()
        order = np.argsort(s)
        s, e = s[order], e[order]
        emax = np.maximum.accumulate(e)
        for i, (st, en) in zip(ga.index, zip(ga.start.to_numpy(), ga.end.to_numpy())):
            k = np.searchsorted(s, en, side="left")   # intervals starting before this one ends
            out[a.index.get_loc(i)] = k > 0 and emax[k - 1] > st
    return out


# --- rn6 sequence by range requests -----------------------------------------------------------

class TwoBit:
    """Minimal reader of a remote .2bit file (UCSC format), by HTTP range requests."""

    def __init__(self, url: str = RN6_2BIT):
        self.url = url
        head = self._range(0, 16)
        sig, ver, n, _ = struct.unpack("<IIII", head)
        assert sig == 0x1A412743 and ver == 0
        buf = self._range(16, 16 + n * 260)
        self.offsets, pos = {}, 0
        for _ in range(n):
            ln = buf[pos]
            name = buf[pos + 1:pos + 1 + ln].decode()
            self.offsets[name] = struct.unpack("<I", buf[pos + 1 + ln:pos + 5 + ln])[0]
            pos += 5 + ln
        self._records = {}

    def _range(self, start: int, end: int) -> bytes:
        r = requests.get(self.url, headers={"Range": f"bytes={start}-{end - 1}"}, timeout=120)
        r.raise_for_status()
        return r.content

    def _record(self, chrom: str):
        if chrom not in self._records:
            off = self.offsets[chrom]
            size, nblocks = struct.unpack("<II", self._range(off, off + 8))
            body = self._range(off + 8, off + 8 + 8 * nblocks + 4)
            nstarts = np.frombuffer(body[:4 * nblocks], "<u4")
            nsizes = np.frombuffer(body[4 * nblocks:8 * nblocks], "<u4")
            nmask = struct.unpack("<I", body[8 * nblocks:])[0]
            dna = off + 8 + 8 * nblocks + 4 + 8 * nmask + 4
            self._records[chrom] = (size, nstarts, nsizes, dna)
        return self._records[chrom]

    def sequence(self, chrom: str, start: int, end: int) -> str:
        size, nstarts, nsizes, dna = self._record(chrom)
        start, end = max(0, start), min(size, end)
        b0, b1 = start // 4, (end + 3) // 4
        raw = np.frombuffer(self._range(dna + b0, dna + b1), np.uint8)
        bases = np.stack([(raw >> 6) & 3, (raw >> 4) & 3, (raw >> 2) & 3, raw & 3], 1).ravel()
        seq = np.array(list("TCAG"))[bases][start - 4 * b0:end - 4 * b0]
        for s, n in zip(nstarts, nsizes):
            lo, hi = max(s, start), min(s + n, end)
            if lo < hi:
                seq[lo - start:hi - start] = "N"
        return "".join(seq)


def ucsc_chrom(ensembl_chr: str) -> str | None:
    """Ensembl Rnor 6.0 chromosome name to UCSC rn6; unplaced scaffolds are not mapped."""
    if ensembl_chr in [str(i) for i in range(1, 21)] + ["X", "Y"]:
        return "chr" + ensembl_chr
    if ensembl_chr == "MT":
        return "chrM"
    return None


def carg_sites(seq: str, mismatches: int = 0) -> int:
    """Number of CArG boxes CC(A/T)6GG in a sequence (the box is its own reverse complement), with
    up to `mismatches` mismatches in the ten bases."""
    seq = seq.upper()
    if mismatches == 0:
        return len(CARG.findall(seq))
    n = 0
    for i in range(len(seq) - 9):
        w = seq[i:i + 10]
        if "N" in w:
            continue
        mm = (w[0] != "C") + (w[1] != "C") + (w[8] != "G") + (w[9] != "G") + sum(ch not in "AT" for ch in w[2:8])
        n += mm <= mismatches
    return n


def shuffle(seq: str, rng: np.random.Generator) -> str:
    """Base composition preserving shuffle (a standard background)."""
    a = np.array(list(seq))
    rng.shuffle(a)
    return "".join(a)


# --- FIMO with the JASPAR SRF matrix ------------------------------------------------------------

JASPAR_SRF = "https://jaspar.elixir.no/api/v1/matrix/MA0083.3/?format=jaspar"
FIMO_THRESHOLD = 1e-4   # FIMO's default p-value threshold; the paper ran FIMO (SI Methods) and names none


def srf_motif_meme(background: dict[str, float]) -> bytes:
    """JASPAR MA0083.3 (SRF) as a MEME motif file, with the given background letter frequencies."""
    lines = get(JASPAR_SRF).decode().splitlines()
    rows = {ln[0]: [float(x) for x in ln.split("[")[1].split("]")[0].split()] for ln in lines[1:5]}
    m = np.array([rows[b] for b in "ACGT"]).T
    m = m / m.sum(1, keepdims=True)
    bg = " ".join(f"{b} {background[b]:.4f}" for b in "ACGT")
    body = "\n".join(" ".join(f"{v:.6f}" for v in r) for r in m)
    return (f"MEME version 4\n\nALPHABET= ACGT\n\nstrands: + -\n\nBackground letter frequencies\n{bg}\n\n"
            f"MOTIF MA0083.3 SRF\nletter-probability matrix: alength= 4 w= {len(m)} nsites= 20 E= 0\n{body}\n").encode()


def base_composition(seqs: list[str]) -> dict[str, float]:
    s = "".join(seqs).upper()
    n = {b: s.count(b) for b in "ACGT"}
    tot = sum(n.values())
    at, gc = (n["A"] + n["T"]) / 2 / tot, (n["C"] + n["G"]) / 2 / tot   # strand-symmetric
    return {"A": at, "C": gc, "G": gc, "T": at}


def fimo_sites(seqs: list[str], meme: bytes, threshold: float = FIMO_THRESHOLD) -> np.ndarray:
    """Number of FIMO matches (both strands, p < threshold) in each sequence."""
    from pymemesuite.common import MotifFile, Sequence
    from pymemesuite.fimo import FIMO
    mf = MotifFile(io.BytesIO(meme))
    motif = mf.read()
    sequences = [Sequence(s.upper(), name=str(i).encode())
                 for i, s in enumerate(seqs)]
    pattern = FIMO(both_strands=True, threshold=threshold).score_motif(motif, sequences, mf.background)
    n = np.zeros(len(seqs), int)
    for e in pattern.matched_elements:
        n[int(e.source.accession.decode())] += 1
    return n
