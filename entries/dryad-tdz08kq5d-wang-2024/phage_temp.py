"""Loading and statistics for Dryad dataset doi:10.5061/dryad.tdz08kq5d (version 263142).

Wang, Wang, Yang, Lu, Fields, Xu, Shen, Wei & Friman (2024), Evolution Letters, doi:10.1093/evlett/qrad056.

The dataset is one Excel workbook, temperature_phage_data_allfigures2.xlsx, with one sheet per figure, and a
README. Dryad lets no one download a file without a token, so the registry's workflow stages the pinned
version's files under /tmp/dryad/<id>/<version>/ before a run (docs/archives.md, "Dryad"). `load_workbook`
reads the workbook from there into memory, after checking its SHA-256 against the one Dryad's file list gives;
nothing is written to disk.

Where the parameters come from:

- The ANOVA models, their terms and order, and the sums of squares readings are those of the claims file
  (claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml), which takes them from the paper's Methods and
  Supplementary Tables S1 to S3. `rm_anova` is a repeated-measures ANOVA with the subject as error stratum,
  as R's aov with Error(ID) computes it for a balanced design; `clone_anova` is an ordinary least squares ANOVA
  with sequential (type I) or type II sums of squares.
- The colony type of each clone is read from its strain name ("a" mucoid, "s" small colony variant) or from
  the sheet's morphotype column, which agree wherever both exist; the twitching sheet has no morphotype column
  and is handled in `twitching` (see its docstring).
- The replicate population of a clone is read from its strain name: in "6b1s3", "b" is 35 degrees C and "d"
  25 degrees C, "1" the replicate tube, "s" the colony type and "3" the clone. This reading is checked in the
  notebook against the treatment column and the colony counts of the Figure 1D sheet.
"""

from __future__ import annotations

import hashlib
import io
import re
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.formula.api import ols

DATASET_ID = "tdz08kq5d"
DOI = "10.5061/dryad.tdz08kq5d"
VERSION = "263142"                  # Dryad API version id; the only version the API lists
WORKBOOK = "temperature_phage_data_allfigures2.xlsx"
WORKBOOK_SHA256 = "6bc2c64abc9e1c65bcdc4080fcaa81c669c39f56a6f63708483e47c563c5c0dd"   # Dryad file list
README_SHA256 = "79a23ead0ade6ec77d36e7d1dc34ed51508417d827175829093609d8740c051a"
STAGED = Path("/tmp") / "dryad" / DATASET_ID / VERSION
FILES_API = f"https://datadryad.org/api/v2/versions/{VERSION}/files"

TREATMENTS = ["25_0", "25_1", "35_0", "35_1"]   # temperature _ phage (1 = evolved with phage)


def _read_checked(name: str, sha256: str) -> bytes:
    data = (STAGED / name).read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != sha256:
        raise RuntimeError(f"{name}: SHA-256 {digest}, not the {sha256} of Dryad's file list")
    return data


def load_readme() -> str:
    return _read_checked("README.md", README_SHA256).decode("utf-8")


def load_workbook() -> dict[str, pd.DataFrame]:
    """Every sheet of the workbook, as read with its first row as header."""
    data = _read_checked(WORKBOOK, WORKBOOK_SHA256)
    return pd.read_excel(io.BytesIO(data), sheet_name=None)


# --- tidy tables -----------------------------------------------------------------------------------------

STRAIN = re.compile(r"^6?([bd])(\d)([as])(\d)$")


def parse_strain(name: str) -> dict:
    """Temperature, replicate tube and colony type from a strain name such as 6b1s3 or b5a2."""
    m = STRAIN.match(str(name).strip())
    if not m:
        return {"name_temp": np.nan, "name_rep": np.nan, "name_type": np.nan}
    return {"name_temp": 35 if m.group(1) == "b" else 25, "name_rep": int(m.group(2)),
            "name_type": "m" if m.group(3) == "a" else "scv"}


def transfer_od(wb) -> pd.DataFrame:
    d = wb["transfer_OD_FIG 1B"].rename(columns={"time(days)": "day", "OD": "od"})
    d["subject"] = d.temperature.astype(str) + "_" + d.phage.astype(str) + "_" + d.replicate.astype(str)
    return d


def phage_density(wb) -> pd.DataFrame:
    return wb["phage_density_FIG 1C"].rename(columns={"time(days)": "day",
                                                       "phagedensity (log10 PFU)": "log10_pfu"})


def colony_counts(wb) -> pd.DataFrame:
    d = wb["scv frequency_FIG 1D"].copy()
    d.columns = ["temp", "phage", "replicate", "scv", "mucoid", "total", "p_scv", "p_m"]
    d["temp"] = d.temp.astype(str).str.extract(r"(\d+)")[0].astype(int)
    return d


def clone_table(wb, sheet: str, value: str) -> tuple[pd.DataFrame, float]:
    """The per-clone values of a Figure 2 sheet, with the ancestor's value given beside them."""
    raw = wb[sheet]
    cols = list(raw.columns)
    d = raw.iloc[:, :4].dropna(how="all").copy()
    d.columns = ["treatment", "strain", "morphotype", value] if cols[1] == "strain" else \
        ["treatment", "morphotype", "strain", value]
    anc_col = [i for i, c in enumerate(cols) if re.match(r"^(strian|strain)(\.\d+)?$", str(c).strip()) and i > 2][0]
    anc = raw.iloc[:, anc_col + 1][raw.iloc[:, anc_col].astype(str).str.strip() == "anc"]
    d = _annotate(d)
    return d, float(anc.iloc[0])


def _annotate(d: pd.DataFrame) -> pd.DataFrame:
    d = d.copy()
    d["temp"] = d.treatment.str.split("_").str[0].astype(int)
    d["phage"] = d.treatment.str.split("_").str[1].astype(int)
    parsed = pd.DataFrame([parse_strain(s) for s in d.strain], index=d.index)
    d = pd.concat([d, parsed], axis=1)
    d["ctype"] = d.morphotype.astype(str).str.strip().str.lower()
    d["unit"] = d.treatment + "_r" + d.name_rep.astype("Int64").astype(str) + "_" + d.ctype
    return d


def twitching(wb) -> tuple[pd.DataFrame, float]:
    """The twitching sheet, with a colony type for each row under two readings.

    The sheet has no morphotype column, and its strain names do not identify the clones: the four 35_1 rows
    carry the names of four 35_0 SCV clones (6b6s1, 6b6s2, 6b8s1, 6b8s2), and in 25_0 the four mucoid names
    6d5a2, 6d7a2, 6d6a2, 6d8a2 appear twice with different values. `type_design` reads the second 25_0 block
    as the four SCVs, in the order the biofilm and disease sheets list them (6d5s2, 6d7s2, 6d6s2, 6d8s2 by
    position), and every other row by the letter of its name; the 35_1 rows are SCVs either way.
    `type_as_named` reads every row by the letter of its name.
    """
    raw = wb["twitching_FIG2D"]
    d = raw.iloc[:, :4].dropna(how="all").copy()
    d.columns = ["treatment", "strain", "hours", "diameter_mm"]
    anc = float(raw.iloc[:, 6][raw.iloc[:, 5].astype(str).str.strip() == "anc"].iloc[0])
    d = d.reset_index(drop=True)
    d["temp"] = d.treatment.str.split("_").str[0].astype(int)
    d["phage"] = d.treatment.str.split("_").str[1].astype(int)
    d["type_as_named"] = [parse_strain(s)["name_type"] for s in d.strain]
    d["type_design"] = d.type_as_named
    seen = set()
    for i, r in d.iterrows():
        key = (r.treatment, r.strain)
        if key in seen:
            d.loc[i, "type_design"] = "scv"
        seen.add(key)
    return d, anc


def disease(wb) -> tuple[pd.DataFrame, float]:
    d, anc = clone_table(wb, "disease incidence_FIG 2F", "incidence")
    return d, anc


# --- statistics ------------------------------------------------------------------------------------------

def rm_anova(d: pd.DataFrame, dv: str, subject: str, between: list[str], within: str) -> pd.DataFrame:
    """Repeated-measures ANOVA for a balanced design: between-subject factors tested against subjects
    within groups (stratum "subject"), the within factor and its interactions against the residual of
    the within stratum. Each subject must have one value per level of `within`."""
    n_w = d[within].nunique()
    counts = d.groupby(subject)[within].nunique()
    if not (counts == n_w).all() or d.groupby([subject, within]).size().max() != 1:
        raise ValueError("unbalanced: every subject needs one value at every level of the within factor")
    rows = []
    # Between stratum: subject means, scaled by the number of within levels.
    sm_ = d.groupby([subject] + between, as_index=False)[dv].mean()
    f_b = " * ".join(f"C({b})" for b in between)
    a_b = sm.stats.anova_lm(ols(f"{dv} ~ {f_b}", sm_).fit(), typ=1)
    for term, r in a_b.iterrows():
        rows.append({"stratum": "subject", "term": term, "df": r.df, "ss": r.sum_sq * n_w})
    # Within stratum: deviations from subject means.
    dd = d.copy()
    dd["dev"] = dd[dv] - dd.groupby(subject)[dv].transform("mean")
    f_w = " * ".join([f"C({within})"] + [f"C({b})" for b in between])
    a_w = sm.stats.anova_lm(ols(f"dev ~ {f_w}", dd).fit(), typ=1)
    a_w = a_w[[within in t for t in a_w.index]]
    ss_within_total = (dd.dev ** 2).sum()
    df_within_total = d[subject].nunique() * (n_w - 1)
    for term, r in a_w.iterrows():
        rows.append({"stratum": "within", "term": term, "df": r.df, "ss": r.sum_sq})
    rows.append({"stratum": "within", "term": "Residual", "df": df_within_total - a_w.df.sum(),
                 "ss": ss_within_total - a_w.sum_sq.sum()})
    out = pd.DataFrame(rows)
    for st in ("subject", "within"):
        m = out.stratum == st
        res = out[m & (out.term == "Residual")].iloc[0]
        ms_res = res.ss / res.df
        eff = m & (out.term != "Residual")
        out.loc[eff, "F"] = (out.loc[eff, "ss"] / out.loc[eff, "df"]) / ms_res
        out.loc[eff, "p"] = stats.f.sf(out.loc[eff, "F"], out.loc[eff, "df"], res.df)
        out.loc[eff, "df_resid"] = res.df
    out["ms"] = out.ss / out.df
    return out[["stratum", "term", "df", "ss", "ms", "F", "df_resid", "p"]]


CLONE_TERMS = "C(temp) + C(phage) + C(ctype) + C(temp):C(phage) + C(temp):C(ctype) + C(phage):C(ctype)"


def clone_anova(d: pd.DataFrame, dv: str, typ: int, formula: str = CLONE_TERMS) -> pd.DataFrame:
    """ANOVA with the terms of Supplementary Table S3 (three main effects and the three two-way
    interactions), sequential (typ=1) in the order of the table, or type II (typ=2)."""
    a = sm.stats.anova_lm(ols(f"{dv} ~ {formula}", d).fit(), typ=typ)
    a = a.rename(columns={"sum_sq": "ss", "PR(>F)": "p"})
    a["df_resid"] = a.loc["Residual", "df"]
    return a[["df", "ss", "F", "df_resid", "p"]]


def one_way(*groups) -> tuple[float, float, int, int]:
    """One-way ANOVA: F, p and the two degrees of freedom."""
    f, p = stats.f_oneway(*groups)
    n = sum(len(g) for g in groups)
    return float(f), float(p), len(groups) - 1, n - len(groups)


def unit_means(d: pd.DataFrame, dv: str) -> pd.DataFrame:
    """Mean of the clones of each colony type within each replicate population."""
    return d.groupby(["unit", "treatment", "temp", "phage", "ctype"], as_index=False)[dv].mean()


# --- sequencing and transcriptome sheets -------------------------------------------------------------------

def variants(wb) -> pd.DataFrame:
    """The snp_indel sheet: one row per variant and group of sequenced clones (temperature, phage, colony
    type), with the number of the group's clones that carry it. The sheet does not say which clones."""
    s = wb["snp_indel"].copy()
    s["group"] = s.treatment.str.replace("evolved alone", "-P").str.replace("evolved with phage", "+P")
    s["protein_changing"] = s.EFFECT.notna() & (s.FTYPE == "CDS")
    return s


def gene_names(wb) -> pd.Series:
    """Gene names by PROKKA locus tag, from the dataset's gene_blast in uniprot sheet."""
    g = wb["gene_blast in uniprot"]
    return pd.Series(g["gene name"].astype(str).str.strip().values, index=g.LOCUS_TAG.str.strip())


def rnaseq_id(locus_tag: str) -> str:
    """The transcriptome sheet's gene id for a PROKKA locus tag: RS-N_03191 is RS-N003191."""
    return "RS-N" + locus_tag.split("_")[1].zfill(6)


def transcriptome(wb) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """The DESeq2 table of Figure 4A (one row per gene), and the gene lists of Figures 4B and 4C as the
    sheet gives them beside it."""
    t = wb["transcriptome"]
    full = t.iloc[1:, :7].copy()
    full.columns = [str(c) for c in t.iloc[0, :7]]
    full = full.dropna(subset=["gene"])
    for c in full.columns[1:]:
        full[c] = pd.to_numeric(full[c], errors="coerce")
    full = full.set_index("gene")
    b = t.iloc[1:, 8:12].dropna(how="all").copy()
    b.columns = ["gene", "label", "log2FoldChange", "padj"]
    c = t.iloc[1:, 13:17].dropna(how="all").copy()
    c.columns = ["label", "log2FoldChange", "padj", "regulation"]
    c["gene"] = c.label.str.extract(r"(RS-N\d{6})")[0]
    for x in (b, c):
        x["log2FoldChange"] = pd.to_numeric(x.log2FoldChange)
        x["padj"] = pd.to_numeric(x.padj)
    return full, b.reset_index(drop=True), c.reset_index(drop=True)
