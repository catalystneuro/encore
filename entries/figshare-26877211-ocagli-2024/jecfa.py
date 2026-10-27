"""Loading and measures for the JECFA index deposited on Figshare (item 26877211, version 1).

Ocagli et al. (2024), Scientific Data, doi:10.1038/s41597-024-04294-w.

The item holds one table twice: `jecfa.rds` (an R tibble) and `JECFA.csv`. Each row is one page of
the JECFA portal, https://apps.who.int/food-additives-contaminants-jecfa-database/Home/Chemical/<n>,
scraped in May 2024, with the 17 fields of the paper's Table 1 in lower-case column names. Both
files are streamed from Figshare at the pinned version and read in memory; nothing is written to
disk. The RDS file is parsed with the `rdata` package, which reads R serialisations without R.

Where the parameters come from:

- `present` (a field is present when it is not NA and not an empty string after trimming) is the
  reading E of the claims file's opening comment.
- `leading_class` reads the class name at the start of a `functional_class` string, as the
  criterion of claim table2-functional-class gives it (the class name runs on into the sub-class,
  "Food AdditivesEMULSIFIER..."). The data spell "Flavouring Agent", the paper "Flavoring Agent";
  a label that differs only in spelling is the same label (protocol, Author, step 1.4).
- `year_bin` uses the bins of Table 2, closed on the left and open on the right, the last closed
  ([1958, 2000), [2000, 2010), [2010, 2020), [2020, 2023]), as the criterion of claim
  table2-evaluation-year gives them.
- `fas_process_df` re-derives the FAS column from the Tox monograph as R/process_df.R does in the
  paper's code (https://github.com/UBESP-DCTV/jecfa at commit
  2d8a5340d5322cbae28eb3095d948313932f6c7e): the text after "FAS " when the Tox monograph
  starts with "FAS ", cut at the first "/" and then at the first "-", and "" otherwise. It is used
  to check that the deposited `fas` column is this derivation.
- `fas_add_metadata` applies the further step of R/add_metadata.R at the same commit, which the
  criteria of claims table1-availability and fas-codes name with process_df.R: a value longer
  than three characters is cut to its first two; an empty value is filled with "74", "60" or "27"
  when the monograph's abbreviation (R/extract_jecfa_tox_abbr.R: the part before the first "-",
  "/" and "JECFA", less a leading "See " or '">') begins "FAS 74", "FAS 60" or "FAS 27".
"""

from __future__ import annotations

import hashlib
import io
import json
import re
import warnings

import fsspec
import pandas as pd
import rdata

ARTICLE_ID = 26877211
VERSION = 1
DOI = "10.6084/m9.figshare.26877211.v1"
API_URL = f"https://api.figshare.com/v2/articles/{ARTICLE_ID}/versions/{VERSION}"
FILE_URL = "https://ndownloader.figshare.com/files/{}"
URL_PREFIX = "https://apps.who.int/food-additives-contaminants-jecfa-database/Home/Chemical/"
# The paper's code, at the commit the claims file read; its R sources are shown beside the ports.
CODE_COMMIT = "2d8a5340d5322cbae28eb3095d948313932f6c7e"
CODE_RAW_URL = "https://raw.githubusercontent.com/UBESP-DCTV/jecfa/{}/{}"

# Table 1 of the paper, in its order, with the deposited column that holds each field.
TABLE1_FIELDS = {
    "URL": "url",
    "JECFA name": "jecfa_name",
    "Chemical names": "chemical_names",
    "Synonyms": "synonyms",
    "CAS number": "cas_number",
    "JECFA number": "jecfa_number",
    "FEMA number": "fema_number",
    "COE number": "coe_number",
    "Functional class": "functional_class",
    "Evaluation year": "evaluation_year",
    "Report": "report",
    "Report sourcelink": "report_sourcelink",
    "Tox monograph": "tox_monograph",
    "Tox monograph sourcelink": "tox_monograph_sourcelink",
    "Specification": "specification",
    "Specification sourcelink": "specification_sourcelink",
    "FAS": "fas",
}
# The column names of R/process_df.R, in the order it selects them.
CODE_COLUMNS = [
    "Report", "Report_sourcelink", "Tox.Monograph", "Tox.Monograph_sourcelink", "Specification",
    "Specification_sourcelink", "Synonyms", "CAS.number", "Functional.Class", "Evaluation.year",
    "Chemical.Names", "JECFA.number", "COE.number", "FEMA.number", "JECFA_name", "URL", "FAS",
]

CLASSES = ["Flavoring Agent", "Food Additives", "Food Contaminant", "Veterinary Drug"]
_CLASS_RE = re.compile(r"^(flavou?ring agent|food additives|food contaminant|veterinary drug)",
                       re.IGNORECASE)
YEAR_BINS = ["[1958-2000)", "[2000-2010)", "[2010-2020)", "[2020-2023]"]


def metadata() -> dict:
    """The version's metadata from the Figshare API, with its file list."""
    with fsspec.open(API_URL, "rt") as f:
        return json.load(f)


def read_bytes(file_id: int) -> bytes:
    """Stream one file of the item into memory."""
    with fsspec.open(FILE_URL.format(file_id), "rb", block_size=2**20) as f:
        return f.read()


def r_source(path: str) -> str:
    """One file of the paper's code at CODE_COMMIT, as text."""
    with fsspec.open(CODE_RAW_URL.format(CODE_COMMIT, path), "rt") as f:
        return f.read()


def load() -> dict:
    """Read both files of the pinned version; return the metadata, MD5s and both tables."""
    meta = metadata()
    files = {f["name"]: f for f in meta["files"]}
    raw = {name: read_bytes(f["id"]) for name, f in files.items()}
    md5 = {name: (hashlib.md5(b).hexdigest(), files[name]["computed_md5"]) for name, b in raw.items()}
    with warnings.catch_warnings():
        # rdata warns that the RDS has no file header and that tibble classes fall back to
        # data.frame; both are expected for a tibble saved with saveRDS.
        warnings.simplefilter("ignore", UserWarning)
        rds = rdata.conversion.convert(rdata.parser.parse_data(raw["jecfa.rds"]))
    csv = pd.read_csv(io.BytesIO(raw["JECFA.csv"]), dtype=str, keep_default_na=False,
                      na_values=["NA"], encoding="utf-8-sig")
    return {"meta": meta, "md5": md5, "rds": rds.astype("string"), "csv": csv.astype("string")}


def page_id(df: pd.DataFrame) -> pd.Series:
    """The portal page number at the end of each URL (NA if the URL has another form)."""
    return pd.to_numeric(df["url"].str.extract(r"/Home/Chemical/(\d+)$")[0], errors="coerce")


def present(s: pd.Series) -> pd.Series:
    """Reading E: a value is present when it is not NA and not empty after trimming."""
    return s.notna() & (s.fillna("").str.strip() != "")


def leading_class(s: pd.Series) -> pd.Series:
    """The functional class named at the start of each string, in the paper's spelling, or NA."""
    m = s.str.extract(_CLASS_RE)[0].str.lower()
    names = {c.lower(): c for c in CLASSES}
    names["flavouring agent"] = "Flavoring Agent"
    return m.map(names, na_action="ignore").astype("string").rename("leading_class")


def year_bin(s: pd.Series) -> pd.Series:
    """Table 2's evaluation-year bins; NA for a missing or out-of-range year."""
    y = pd.to_numeric(s, errors="coerce")
    out = pd.Series(pd.NA, index=s.index, dtype="string")
    out[(y >= 1958) & (y < 2000)] = YEAR_BINS[0]
    out[(y >= 2000) & (y < 2010)] = YEAR_BINS[1]
    out[(y >= 2010) & (y < 2020)] = YEAR_BINS[2]
    out[(y >= 2020) & (y <= 2023)] = YEAR_BINS[3]
    return out


def fas_process_df(tox_monograph: pd.Series) -> pd.Series:
    """FAS as R/process_df.R derives it from the Tox monograph (NA stays NA)."""
    def one(t):
        if pd.isna(t):
            return pd.NA
        if not re.match(r"^FAS .*$", t):
            return ""
        return t[4:].split("/")[0].split("-")[0]
    return tox_monograph.map(one).astype("string")


def tox_abbr(t) -> object:
    """R/extract_jecfa_tox_abbr.R for one Tox monograph value."""
    if pd.isna(t):
        return pd.NA
    a = t.split("-")[0].split("/")[0].split("JECFA")[0]
    if a[:3] == "See":
        a = a[4:]
    if a[:2] == '">':
        a = a[2:]
    if a[:3] != "FAS" and a[:12] != "NOT PREPARED":
        a = "NOT A FAS"
    return a


def fas_add_metadata(fas: pd.Series, tox_monograph: pd.Series) -> pd.Series:
    """FAS after the case_when of R/add_metadata.R."""
    def one(f, t):
        if pd.isna(f):
            return pd.NA
        if len(f) > 3:
            return f[:2]
        if f != "":
            return f
        abbr = tox_abbr(t)
        if not pd.isna(abbr):
            for code in ("74", "60", "27"):
                if abbr[:6] == f"FAS {code}":
                    return code
        return f
    return pd.Series([one(f, t) for f, t in zip(fas, tox_monograph)], index=fas.index,
                     dtype="string")


def cas_check_digit_ok(cas: str) -> bool:
    """Whether a CAS number has the registry's form and a valid check digit."""
    m = re.fullmatch(r"(\d{2,7})-(\d{2})-(\d)", cas.strip())
    if not m:
        return False
    digits = (m.group(1) + m.group(2))[::-1]
    return sum((i + 1) * int(d) for i, d in enumerate(digits)) % 10 == int(m.group(3))
