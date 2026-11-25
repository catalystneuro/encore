"""Loading for Dryad dataset rjdfn2zqz (version 439366), squid under ocean acidification.

Allen, Yan, Kuan et al. (2026), Communications Biology 9:229, doi:10.1038/s42003-025-09506-6.

The dataset holds one CSV per measurement (per squid, with its group), the hemolymph carbonate
calculations, and squid.zip, which holds the authors' R workspace `Squid.RData`, the RSEM count
matrix, the ExN50 statistics of the assembly and their shell and R scripts. Dryad needs a token to
download, so the workflow stages the files of the pinned version in `STAGED`, checked against the
SHA-256 of Dryad's file list; they are read from there into memory and never written.

`read_rdata` reads R's serialization format (XDR, version 2 or 3) and builds only the top-level
objects asked for, skipping the rest; the workspace is 1.1 GB uncompressed, and a general reader
(the `rdata` package) needs about 12 GB and 5 minutes for it. R objects become `RObj` (type,
value, attributes): numeric vectors are numpy arrays, character vectors lists of str (None for
NA), lists Python lists, pairlists lists of (tag, value). `df_from` turns a data.frame into pandas.

No analysis parameter is set here; the claims' methods are in the notebook, with their sources.
"""

from __future__ import annotations

import gzip
import hashlib
import io
import struct
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

DRYAD_ID = "rjdfn2zqz"
DRYAD_VERSION = "439366"
STAGED = Path("/tmp") / "dryad" / DRYAD_ID / DRYAD_VERSION  # where the workflow stages them (docs/archives.md)
SHA256 = {  # Dryad file list, https://datadryad.org/api/v2/versions/439366/files
    "Carbonate_calibration.csv": "31c3cb7319a7866914a2aaac1c414e84f4d172ba0046948b683bf95ae0f38902",
    "README.md": "6358bb541d7437d091326ba3dae5fe26001e369cd3873bd090e727f8be7a699b",
    "Squid_Ammonia.csv": "9ebf5ec10209d345c658c4968533ba96e630afc06fbbe2b05731f604e4fdba8d",
    "Squid_Behavioral_assessment.csv": "53cc4017d75ae7392a9b3177d73086abfe80850e9080367fd47f73acd5c8f6f0",
    "Squid_CFF.csv": "cae6cb27a6373b51706c526fb605937e5d40cddb7ab45ec1514213fab4ec2c85",
    "Squid_ERG.csv": "f679f6b4edfb42f154202001c5bca30891a1cbb1951f3b2f5d7d7641339c8001",
    "Squid_Hemolymph.csv": "eafdc713c4b50303a2ede1fc7852cb7d184edbe1e259a70a108217de490654e9",
    "Squid_normalized_total_distance.csv": "1d6ccf12641cc879c13c8818534fb236f350fe84a5f1fa2fda1422fd468c1e5e",
    "Squid_normalized_velocities.csv": "323742b0f9c84aa4d93ae62c085faf54cf1f5f79105e4e9fc3ec1cb2ad794fde",
    "Squid_Prey_Capture.csv": "fbb32ca33344fd3906c8684823b7783e7386d359e6c7573d378faed122832dc1",
    "Squid_RMR.csv": "9d643e82fe3094eea53a5bc967302201f41a47e63ce3c5960dba0efde982c9a8",
    "squid.zip": "60ba0ca6d534fb2b7353593b320ec8dc81073872748915b89a0867e040807d93",
}
ZIP_DIR = "squid/squid/"
GROUPS = ["Control", "Acute-OA", "Chronic-OA"]


def check_files() -> dict[str, str]:
    """SHA-256 of every staged file against Dryad's file list; returns name -> 'ok' or the digest found."""
    out = {}
    for name, want in SHA256.items():
        h = hashlib.sha256()
        with open(STAGED / name, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 22), b""):
                h.update(chunk)
        out[name] = "ok" if h.hexdigest() == want else h.hexdigest()
    return out


def read_csv(name: str) -> pd.DataFrame:
    """One of the dataset's CSV files (UTF-8 with a byte order mark), group names as in GROUPS."""
    df = pd.read_csv(STAGED / name, encoding="utf-8-sig")
    for col in df.columns:
        if col.lower() == "group":
            df[col] = df[col].str.strip().replace({"control": "Control", "Acute-OA": "Acute-OA"})
    return df


def zip_names() -> list[tuple[str, int]]:
    with zipfile.ZipFile(STAGED / "squid.zip") as z:
        return [(i.filename, i.file_size) for i in z.infolist()]


def zip_text(name: str) -> str:
    with zipfile.ZipFile(STAGED / "squid.zip") as z:
        return z.read(ZIP_DIR + name).decode("utf-8", "replace")


def count_matrix_rows() -> tuple[list[str], int]:
    """Header and number of transcript rows of RSEM.isoform.counts.matrix, read as a stream."""
    with zipfile.ZipFile(STAGED / "squid.zip") as z, z.open(ZIP_DIR + "RSEM.isoform.counts.matrix") as f:
        header = f.readline().decode().rstrip("\n").split("\t")
        n = sum(1 for _ in f)
    return header, n


def read_count_matrix(names: str = "first") -> pd.DataFrame:
    """RSEM.isoform.counts.matrix: transcripts by samples (expected counts). The header names 16
    samples and each row holds a transcript id and 15 values. `names="r"` names them as R's
    read.csv(row.names = 1) does in the authors' script (the first header name taken as that of the
    id column); `names="first"` gives the values the first 15 header names, which the notebook
    shows is the right reading (the last sample, Re_8.1_OL-3, has no values)."""
    with zipfile.ZipFile(STAGED / "squid.zip") as z, z.open(ZIP_DIR + "RSEM.isoform.counts.matrix") as f:
        header = f.readline().decode().rstrip("\n").split("\t")
        df = pd.read_csv(f, sep="\t", header=None, index_col=0).astype(np.float64)
    df.columns = header[1:] if names == "r" else header[:df.shape[1]]
    df.index.name = None
    return df


TSA_ACCESSION = "GLBY00000000.1"   # the paper's assembled transcriptome (Data availability), NCBI TSA


def tsa_summary() -> dict:
    """NCBI's summary of the TSA master record (E-utilities esummary): its version, title and number
    of sequences (`slen` of a master record)."""
    import json
    import urllib.request
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&retmode=json&id="
           + TSA_ACCESSION)
    with urllib.request.urlopen(url, timeout=60) as r:
        d = json.load(r)["result"]
    rec = d[d["uids"][0]]
    if rec["accessionversion"] != TSA_ACCESSION:
        raise ValueError(f"NCBI returned {rec['accessionversion']}, not {TSA_ACCESSION}")
    return {k: rec[k] for k in ("accessionversion", "title", "slen", "updatedate")}


# --- R serialization ----------------------------------------------------------

@dataclass
class RObj:
    type: str
    value: object = None
    attr: dict = field(default_factory=dict)

    def __getitem__(self, key):
        """A named element of a list, or an attribute (S4 slot) by name."""
        if self.type in ("list", "pairlist"):
            names = self.attr.get("names")
            if self.type == "pairlist":
                for tag, v in self.value:
                    if tag == key:
                        return v
            elif names is not None and key in names.value:
                return self.value[names.value.index(key)]
        if key in self.attr:
            return self.attr[key]
        raise KeyError(key)

    def names(self):
        if self.type == "pairlist":
            return [t for t, _ in self.value]
        n = self.attr.get("names")
        return list(n.value) if n is not None else None


_TYPES = {10: "logical", 13: "integer", 14: "double", 15: "complex", 24: "raw"}
_SPECIAL = {254: "NULL", 253: "globalenv", 252: "unbound", 251: "missing", 250: "basenamespace",
            242: "emptyenv", 241: "baseenv"}


class _Reader:
    def __init__(self, buf: bytes):
        self.b = memoryview(buf)
        self.p = 0
        self.refs: list = []

    def int(self) -> int:
        v = struct.unpack_from(">i", self.b, self.p)[0]
        self.p += 4
        return v

    def length(self) -> int:
        n = self.int()
        if n == -1:
            hi, lo = struct.unpack_from(">ii", self.b, self.p)
            self.p += 8
            n = (hi << 32) + lo
        return n

    def charsxp(self, keep: bool):
        n = self.int()
        if n == -1:
            return None
        s = self.p
        self.p += n
        return bytes(self.b[s:s + n]).decode("utf-8", "replace") if keep else None

    def item(self, keep: bool):
        flags = self.int()
        t = flags & 0xFF
        has_attr, has_tag = bool(flags & 0x200), bool(flags & 0x400)
        if t in _SPECIAL:
            return RObj(_SPECIAL[t])
        if t == 255:  # REFSXP
            i = flags >> 8
            if i == 0:
                i = self.int()
            return self.refs[i - 1]
        if t in (247, 248, 249):  # PERSISTSXP, PACKAGESXP, NAMESPACESXP
            self.int()
            n = self.int()
            v = RObj("namespace", [self.item(True).value for _ in range(n)])
            self.refs.append(v)
            return v
        if t == 1:  # SYMSXP
            v = RObj("symbol", self.item(True).value)
            self.refs.append(v)
            return v
        if t == 4:  # ENVSXP: contents skipped
            self.int()
            v = RObj("environment")
            self.refs.append(v)
            for _ in range(4):
                self.item(False)
            return v
        if t in (2, 3, 5, 6, 17, 239, 240):  # pairlist-like, read iteratively along the CDR
            out, first_attr = [], None
            while True:
                attr = self.item(keep) if has_attr else None
                if first_attr is None:
                    first_attr = attr
                tag = self.item(True).value if has_tag else None
                car = self.item(keep)
                out.append((tag, car))
                flags = self.int()
                t2 = flags & 0xFF
                if t2 not in (2, 3, 5, 6, 17, 239, 240):
                    self.p -= 4
                    self.item(keep)  # the final CDR, normally NULL
                    break
                has_attr, has_tag = bool(flags & 0x200), bool(flags & 0x400)
            v = RObj("pairlist" if t in (2, 239) else "language", out if keep else None)
            if keep and first_attr is not None:
                v.attr = _attr_dict(first_attr)
            return v
        if t in (7, 8):  # SPECIALSXP, BUILTINSXP
            n = self.int()
            self.p += n
            return RObj("builtin")
        if t == 9:
            return RObj("char", self.charsxp(keep))
        if t in _TYPES:
            n = self.length()
            size = {10: 4, 13: 4, 14: 8, 15: 16, 24: 1}[t]
            s = self.p
            self.p += n * size
            val = None
            if keep:
                dt = {10: ">i4", 13: ">i4", 14: ">f8", 15: ">c16", 24: "u1"}[t]
                val = np.frombuffer(self.b[s:s + n * size], dtype=dt).astype(dt[1:] if t != 24 else "u1")
            v = RObj(_TYPES[t], val)
        elif t == 16:  # STRSXP
            n = self.length()
            vals = []
            for _ in range(n):
                self.int()  # CHARSXP flags
                vals.append(self.charsxp(keep))
            v = RObj("character", vals if keep else None)
        elif t in (19, 20):  # VECSXP, EXPRSXP
            n = self.length()
            v = RObj("list", [self.item(keep) for _ in range(n)])
        elif t == 21:  # BCODESXP (compiled closures in environments), skipped
            self.int()
            self._bc1()
            v = RObj("bytecode")
        elif t == 25:  # S4SXP
            v = RObj("S4")
        elif t == 22:  # EXTPTRSXP
            v = RObj("externalptr")
            self.refs.append(v)
            self.item(False)
            self.item(False)
        elif t == 23:  # WEAKREFSXP
            v = RObj("weakref")
            self.refs.append(v)
        elif t == 238:  # ALTREP: class info, state, attributes
            info = self.item(True)
            state = self.item(keep)
            attr = self.item(keep)
            cls = info.value[0][1].value if info.value else None
            v = _altrep(cls, state) if keep else RObj("altrep")
            if keep and attr.type == "pairlist":
                v.attr = _attr_dict(attr)
            return v
        else:
            raise ValueError(f"unsupported R type {t} at byte {self.p}")
        if has_attr:
            a = self.item(keep)
            if keep:
                v.attr = _attr_dict(a)
        return v


def _bc1(self) -> None:
    self.item(False)  # the code vector
    for _ in range(self.int()):
        t = self.int()
        if t == 21:
            self._bc1()
        elif t in (2, 6, 243, 244, 239, 240):
            self._bclang(t)
        else:
            self.item(False)


def _bclang(self, t: int) -> None:
    if t == 243:  # BCREPREF
        self.int()
        return
    if t in (244, 2, 6, 239, 240):
        if t == 244:  # BCREPDEF
            self.int()
            t = self.int()
        if t in (239, 240):
            self.item(False)
        self.item(False)  # tag
        self._bclang(self.int())
        self._bclang(self.int())
        return
    self.item(False)


_Reader._bc1 = _bc1
_Reader._bclang = _bclang


def _attr_dict(a: RObj) -> dict:
    return {tag: val for tag, val in a.value} if a is not None and a.type == "pairlist" else {}


def _altrep(cls: str, state: RObj) -> RObj:
    """The ALTREP classes R writes for compact sequences and deferred strings."""
    if cls in ("compact_intseq", "compact_realseq"):
        n, start, step = state.value[:3]
        seq = start + step * np.arange(int(n))
        return RObj("integer" if cls == "compact_intseq" else "double", seq.astype(int if cls == "compact_intseq" else float))
    if cls == "deferred_string":
        src = state.value[0][1] if state.type == "pairlist" else state
        return RObj("character", [None if x is None else str(x) for x in np.asarray(src.value).tolist()])
    if cls == "wrap_real" or cls == "wrap_integer" or cls == "wrap_string" or cls == "wrap_logical":
        return state.value[0][1] if state.type == "pairlist" else state
    raise ValueError(f"unsupported ALTREP class {cls}")


def read_rdata(keep: set[str]) -> dict[str, RObj]:
    """The top-level objects named in `keep` from Squid.RData (others are skipped, not built)."""
    with zipfile.ZipFile(STAGED / "squid.zip") as z:
        raw = gzip.decompress(z.read(ZIP_DIR + "Squid.RData"))
    if raw[:5] != b"RDX3\n" and raw[:5] != b"RDX2\n":
        raise ValueError("not an R workspace")
    r = _Reader(raw[5:])
    r.p += 2  # "X\n"
    version = r.int()
    r.int()
    r.int()
    if version == 3:
        n = r.int()
        r.p += n  # native encoding
    out = {}
    # The workspace is a pairlist of (name, object); walk it, building only the objects asked for.
    while True:
        flags = r.int()
        if flags & 0xFF != 2:
            break
        if flags & 0x200:
            r.item(False)
        tag = r.item(True).value if flags & 0x400 else None
        obj = r.item(tag in keep)
        if tag in keep:
            out[tag] = obj
    del raw
    return out


def top_level_names() -> list[tuple[str, str]]:
    """Name and R type of every object in Squid.RData, without building any of them."""
    with zipfile.ZipFile(STAGED / "squid.zip") as z:
        raw = gzip.decompress(z.read(ZIP_DIR + "Squid.RData"))
    r = _Reader(raw[5:])
    r.p += 2
    version = r.int()
    r.int()
    r.int()
    if version == 3:
        n = r.int()
        r.p += n
    out = []
    while True:
        flags = r.int()
        if flags & 0xFF != 2:
            break
        if flags & 0x200:
            r.item(False)
        tag = r.item(True).value if flags & 0x400 else None
        start = r.p
        t = struct.unpack_from(">i", r.b, start)[0] & 0xFF
        r.item(False)
        out.append((tag, {25: "S4", 19: "list", 14: "double", 13: "integer", 16: "character", 4: "environment"}.get(t, str(t)), r.p - start))
    return out


def r_class(o: RObj) -> list[str]:
    c = o.attr.get("class")
    return list(c.value) if c is not None else []


def as_py(o: RObj):
    """An atomic R vector as numpy or list, with NA as nan or None."""
    if o.type == "integer" or o.type == "logical":
        v = o.value.astype(float)
        v[o.value == -2147483648] = np.nan
        return v
    return o.value


def df_from(o: RObj) -> pd.DataFrame:
    """A data.frame (or a list of equal-length vectors) as pandas, factors as their labels."""
    cols = {}
    for name, col in zip(o.names(), o.value):
        if "factor" in r_class(col):
            levels = col.attr["levels"].value
            cols[name] = [None if x == -2147483648 else levels[x - 1] for x in col.value]
        else:
            cols[name] = as_py(col)
    df = pd.DataFrame(cols)
    rn = o.attr.get("row.names")
    if rn is not None and rn.type == "character":
        df.index = rn.value
    return df


def s4_dataframe(o: RObj) -> pd.DataFrame:
    """An S4Vectors DataFrame (DESeqResults and the like) as pandas."""
    ld = o["listData"]
    df = pd.DataFrame({n: as_py(v) for n, v in zip(ld.names(), ld.value)})
    rn = o.attr.get("rownames")
    if rn is not None and rn.type == "character":
        df.index = rn.value
    return df


def matrix(o: RObj) -> pd.DataFrame:
    """A numeric R matrix with its dimnames."""
    nr, nc = o.attr["dim"].value
    arr = np.asarray(o.value).reshape((nc, nr)).T
    dn = o.attr.get("dimnames")
    rows = cols = None
    if dn is not None:
        rows = dn.value[0].value if dn.value[0].type == "character" else None
        cols = dn.value[1].value if dn.value[1].type == "character" else None
    return pd.DataFrame(arr, index=rows, columns=cols)


# --- statistics ---------------------------------------------------------------
# The tests the paper names (Methods, "Statistics and reproducibility"; Supplementary Tables 1 to 4),
# written out here because GraphPad Prism's Welch ANOVA and Dunnett's T3 have no SciPy equivalent.

def welch_anova(groups: list[np.ndarray]) -> dict:
    """Welch's one-way ANOVA (Welch 1951), as GraphPad Prism reports it: W, df1, df2, p."""
    from scipy import stats
    k = len(groups)
    n = np.array([len(g) for g in groups], float)
    m = np.array([np.mean(g) for g in groups])
    v = np.array([np.var(g, ddof=1) for g in groups])
    w = n / v
    mw = np.sum(w * m) / np.sum(w)
    a = np.sum(w * (m - mw) ** 2) / (k - 1)
    lam = np.sum((1 - w / w.sum()) ** 2 / (n - 1))
    b = 1 + 2 * (k - 2) / (k ** 2 - 1) * lam
    f = a / b
    df2 = (k ** 2 - 1) / (3 * lam)
    return {"W": f, "df1": k - 1, "df2": df2, "p": stats.f.sf(f, k - 1, df2)}


def _smm_cdf(c: float, k: int, df: float) -> float:
    """Studentized maximum modulus distribution: P(max of k |t| <= c) with df degrees of freedom."""
    from scipy import integrate, stats
    s = stats.chi(df, scale=1 / np.sqrt(df))
    f = lambda x: (2 * stats.norm.cdf(c * x) - 1) ** k * s.pdf(x)
    hi = s.ppf(1 - 1e-12)
    return integrate.quad(f, 0, hi, limit=200)[0]


def dunnett_t3(groups: dict[str, np.ndarray], level: float = 0.95) -> pd.DataFrame:
    """Dunnett's T3 (Dunnett 1980): every pair, Welch standard error and df, studentized maximum
    modulus with k = number of comparisons. Mean difference is first minus second, as Prism prints."""
    from scipy import optimize
    names = list(groups)
    pairs = [(a, b) for i, a in enumerate(names) for b in names[i + 1:]]
    k = len(pairs)
    rows = []
    for a, b in pairs:
        x, y = np.asarray(groups[a]), np.asarray(groups[b])
        va, vb = np.var(x, ddof=1) / len(x), np.var(y, ddof=1) / len(y)
        se = np.sqrt(va + vb)
        df = (va + vb) ** 2 / (va ** 2 / (len(x) - 1) + vb ** 2 / (len(y) - 1))
        d = x.mean() - y.mean()
        t = abs(d) / se
        p = 1 - _smm_cdf(t, k, df)
        crit = optimize.brentq(lambda c: _smm_cdf(c, k, df) - level, 0.5, 50)
        rows.append({"comparison": f"{a} vs {b}", "mean_diff": d, "ci_low": d - crit * se,
                     "ci_high": d + crit * se, "df": df, "p_adj": max(p, 0.0)})
    return pd.DataFrame(rows)


def oneway(groups: dict[str, np.ndarray]) -> dict:
    """Ordinary one-way ANOVA with Tukey's multiple comparisons (scipy.stats.tukey_hsd)."""
    from scipy import stats
    vals = [np.asarray(v, float) for v in groups.values()]
    f, p = stats.f_oneway(*vals)
    n = sum(len(v) for v in vals)
    grand = np.concatenate(vals).mean()
    ss_t = sum(len(v) * (v.mean() - grand) ** 2 for v in vals)
    ss_r = sum(((v - v.mean()) ** 2).sum() for v in vals)
    tk = stats.tukey_hsd(*vals)
    names = list(groups)
    pairs = {f"{names[i]} vs {names[j]}": tk.pvalue[i, j]
             for i in range(len(names)) for j in range(i + 1, len(names))}
    return {"F": f, "df1": len(vals) - 1, "df2": n - len(vals), "p": p, "SS_treat": ss_t,
            "SS_resid": ss_r, "eta2": ss_t / (ss_t + ss_r), "tukey": pairs}


def describe(groups: dict[str, np.ndarray]) -> pd.DataFrame:
    """n, mean, SD and SEM per group."""
    return pd.DataFrame({g: {"n": len(v), "mean": np.mean(v), "sd": np.std(v, ddof=1),
                             "sem": np.std(v, ddof=1) / np.sqrt(len(v))} for g, v in groups.items()}).T


def by_group(df: pd.DataFrame, col: str, group_col: str = "Group") -> dict[str, np.ndarray]:
    """Values of `col` per group, in the order of GROUPS, NA dropped."""
    return {g: df.loc[df[group_col] == g, col].dropna().to_numpy(float) for g in GROUPS}


def auc(y: np.ndarray, score: np.ndarray) -> float:
    """Area under the ROC curve (the Mann-Whitney statistic, ties counted half)."""
    from scipy import stats
    r = stats.rankdata(score)
    n1 = int(y.sum())
    n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


def plotpca(assay: pd.DataFrame, ntop: int = 500) -> tuple[pd.DataFrame, np.ndarray]:
    """DESeq2's plotPCA: the `ntop` rows of highest variance, prcomp centred and unscaled; returns
    sample scores and the fraction of variance of each component."""
    v = assay.var(axis=1, ddof=1)
    top = assay.loc[v.sort_values(ascending=False).index[:ntop]]
    x = top.T.to_numpy()
    x = x - x.mean(axis=0)
    u, s, vt = np.linalg.svd(x, full_matrices=False)
    scores = pd.DataFrame(u * s, index=assay.columns, columns=[f"PC{i + 1}" for i in range(len(s))])
    return scores, s ** 2 / np.sum(s ** 2)


def remove_batch_effect(assay: pd.DataFrame, design: np.ndarray, covariates: np.ndarray) -> pd.DataFrame:
    """limma's removeBatchEffect with covariates: fit each row on [design, covariates] by least
    squares and subtract the covariates' part."""
    x = np.column_stack([design, covariates])
    beta, *_ = np.linalg.lstsq(x, assay.to_numpy().T, rcond=None)
    out = assay.to_numpy() - (covariates @ beta[design.shape[1]:]).T
    return pd.DataFrame(out, index=assay.index, columns=assay.columns)


def s4_assay(o: RObj) -> pd.DataFrame:
    """The first assay of a SummarizedExperiment (DESeqTransform), with its row and column names."""
    a = o["assays"]["data"]["listData"].value[0]
    m = matrix(a)
    return m
