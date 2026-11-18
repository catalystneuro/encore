"""Loading and tests for the derivative tables of SPARC dataset 212, version 1.

Wang, Morotti, Tapa et al. (2019), J Physiol 597, 3867-3883, doi:10.1113/jp278016. The dataset
(doi:10.26275/lok5-wje6) holds no optical maps. Its `files/derivative/exp_data_Wang_et_al.xlsx` has
one sheet per figure (Fig1, Fig2, Fig3, Fig5, Fig7) with one value per heart and time point, and
four CSV files repeat the Fig2 tables. Files are read from the public S3 bucket at the object
versions the version's manifest lists; nothing is written to disk.

Where the parameters come from:

- The tests are those of the paper's Methods ("Data analysis and statistics"): "Repeated measures
  ANOVA or paired t-tests were used to analyse data obtained before and during/after stimulation
  from the same hearts. A probability value of P<0.05 was considered statistically significant."
  The claims file names both as readings; both are run.
- Paired t-tests are two-sided, the claims file's reading (fig1a-rabbit-hr-increase).
- The comparisons against time 0 after a repeated measures ANOVA are not named in the paper. Here
  they are paired t-tests against time 0 with the Holm-Sidak adjustment over the time points, the
  default comparison against a control after a one-way repeated measures ANOVA in SigmaPlot; this
  is an assumption, stated in the attempt record. Unadjusted paired t-tests are reading (i).
- Hearts with a missing value are left out of the repeated measures ANOVA (it needs complete
  data) and out of a paired t-test only for the pair that is missing. This is a standard choice.
"""

from __future__ import annotations

import io
import json

import fsspec
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.anova import AnovaRM
from statsmodels.stats.multitest import multipletests

BUCKET = "https://sparc-prod-aod-discover-publish50-use1.s3.amazonaws.com"
DATASET_ID = "212"
VERSION = "1"
DOI = "10.26275/lok5-wje6"
MANIFEST_VERSION = "l2e2XW7fUmH2p21D9NS6akGrrQ.3EJzF"
WORKBOOK = "files/derivative/exp_data_Wang_et_al.xlsx"


def read_bytes(url: str) -> bytes:
    with fsspec.open(url, block_size=2**20) as f:
        return f.read()


def manifest() -> dict:
    """The manifest of the pinned version: every file with its path, size, s3VersionId and sha256."""
    url = f"{BUCKET}/{DATASET_ID}/manifest.json?versionId={MANIFEST_VERSION}"
    return json.loads(read_bytes(url))


def file_table(man: dict) -> pd.DataFrame:
    return pd.DataFrame([{"path": f["path"], "size": f["size"], "type": f.get("fileType"),
                          "s3VersionId": f.get("s3VersionId")} for f in man["files"]])


def read_file(man: dict, path: str) -> bytes:
    """Read one file of the pinned version; refuses a file without an object version."""
    entry = next(f for f in man["files"] if f["path"] == path)
    if not entry.get("s3VersionId"):
        raise ValueError(f"{path} has no s3VersionId in the manifest")
    data = read_bytes(f"{BUCKET}/{DATASET_ID}/{path}?versionId={entry['s3VersionId']}")
    if len(data) != entry["size"]:
        raise ValueError(f"{path}: read {len(data)} bytes, the manifest says {entry['size']}")
    return data


def read_excel_sheets(man: dict, path: str) -> dict[str, pd.DataFrame]:
    return pd.read_excel(io.BytesIO(read_file(man, path)), sheet_name=None, header=None)


def _find(sheet: pd.DataFrame, text: str, start: int = 0) -> int:
    """Row index of the first cell in column 0 at or after `start` that starts with `text`."""
    for i in range(start, len(sheet)):
        v = sheet.iat[i, 0]
        if isinstance(v, str) and v.strip().startswith(text):
            return i
    raise KeyError(text)


def _numeric_block(sheet: pd.DataFrame, first_row: int) -> pd.DataFrame:
    """Rows from `first_row` while column 0 holds a number."""
    rows = []
    i = first_row
    while i < len(sheet) and isinstance(sheet.iat[i, 0], (int, float, np.integer, np.floating)) \
            and not pd.isna(sheet.iat[i, 0]):
        rows.append(i)
        i += 1
    return sheet.iloc[rows]


def _time_course(sheet: pd.DataFrame, header_row: int, groups: dict[str, tuple[int, int]],
                 extra: dict[int, str] | None = None) -> pd.DataFrame:
    """Long table (time, variable, heart, value) from a block whose header is at `header_row`.

    `groups` maps a variable to its column range [first, last); hearts are numbered by the column's
    position within the range, from 1. `extra` keeps other single columns as their own variable.
    """
    block = _numeric_block(sheet, header_row + 1)
    out = []
    for var, (a, b) in groups.items():
        for k, c in enumerate(range(a, b), start=1):
            for t, v in zip(block[0], block[c]):
                out.append({"time": float(t), "variable": var, "heart": k,
                            "value": float(v) if not pd.isna(v) else np.nan})
    for c, var in (extra or {}).items():
        for t, v in zip(block[0], block[c]):
            out.append({"time": float(t), "variable": var, "heart": 0,
                        "value": float(v) if not pd.isna(v) else np.nan})
    return pd.DataFrame(out)


def load_tables(man: dict) -> dict:
    """Every table of the workbook, as long tables with one row per time point, variable and heart.

    Column positions are those of the sheets in version 1; `sanity` in the notebook prints the
    header cells they rest on.
    """
    sheets = read_excel_sheets(man, WORKBOOK)
    t = {"sheets": sheets}

    s = sheets["Fig1"]
    for species, title in (("mouse", "Mouse"), ("rabbit", "Rabbit")):
        h = _find(s, title)
        block = _numeric_block(s, h + 2)
        t[f"fig1_{species}_hr"] = pd.DataFrame({"heart": range(1, len(block) + 1),
                                                "baseline": block[0].astype(float).values,
                                                "sns": block[1].astype(float).values})

    s = sheets["Fig2"]
    tc = {"CaTD80": (2, 7), "APD80": (7, 12), "HR": (12, 17)}
    h = _find(s, "SNS Time")
    t["fig2_mouse"] = _time_course(s, h, tc)
    h = _find(s, "SNS Time", h + 1)
    t["fig2_rabbit"] = _time_course(s, h, tc)
    h = _find(s, "SNS Time", h + 1)
    t["fig2_mouse_cat"] = _time_course(s, h, {"CaT amplitude": (2, 8)})
    h = _find(s, "SNS Time", h + 1)
    t["fig2_rabbit_cat"] = _time_course(s, h, {"CaT amplitude": (2, 8)})

    s = sheets["Fig3"]
    tc = {"CaTD80": (2, 7), "APD80": (7, 12), "HR": (12, 16)}
    h = _find(s, "Effects of tyramine")
    t["fig3_tyramine"] = _time_course(s, _find(s, "SNS Time", h), tc, extra={1: "unlabelled column B"})
    h = _find(s, "Effects of Noradrenaline")
    t["fig3_na"] = _time_course(s, _find(s, "SNS Time", h), tc, extra={1: "unlabelled column B"})
    h = _find(s, "Effects of propranolol")
    t["fig3_propranolol"] = _time_course(s, _find(s, "SNS Time", h), tc)
    h = _find(s, "APD in response to a step")
    t["fig3e"] = _time_course(s, _find(s, "Time (sec)", h), {"no SNS": (2, 7), "SNS": (7, 12)},
                              extra={12: "pacing rate (bpm)"})
    h = _find(s, "APD over 60")
    t["fig3f"] = _time_course(s, _find(s, "Time (sec)", h), {"no SNS": (2, 7), "SNS": (7, 12)})

    for sheet, key in (("Fig5", "fig5f_rabbit"), ("Fig7", "fig7f_mouse")):
        s = sheets[sheet]
        h = _find(s, "Base")
        block = _numeric_block(s, h + 1)
        t[key] = pd.DataFrame({"heart": range(1, len(block) + 1), "base": block[0].astype(float).values,
                               "apex": block[1].astype(float).values})
    return t


def wide(long: pd.DataFrame, variable: str) -> pd.DataFrame:
    """Hearts as columns, time points as rows, empty hearts dropped."""
    w = long[long.variable == variable].pivot(index="time", columns="heart", values="value")
    return w.loc[:, w.notna().any()]


def mean_sd(w: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"n": w.notna().sum(axis=1), "mean": w.mean(axis=1), "sd": w.std(axis=1, ddof=1)})


def paired(a, b) -> dict:
    """Two-sided paired t-test of b against a over the pairs where both exist."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    ok = ~np.isnan(a) & ~np.isnan(b)
    d = b[ok] - a[ok]
    if ok.sum() < 2:
        return {"n": int(ok.sum()), "mean_diff": float(np.mean(d)) if ok.any() else np.nan, "t": np.nan,
                "p": np.nan}
    r = stats.ttest_rel(b[ok], a[ok])
    return {"n": int(ok.sum()), "mean_diff": float(d.mean()), "t": float(r.statistic), "p": float(r.pvalue)}


def against_time0(w: pd.DataFrame) -> pd.DataFrame:
    """Each time point against time 0: reading (i), paired t-tests; reading (ii), a one-way repeated
    measures ANOVA over the hearts with complete data, then paired t-tests against time 0 on those
    hearts with the Holm-Sidak adjustment (assumption; see the module docstring)."""
    t0 = w.index.min()
    rows = []
    for t in w.index[w.index > t0]:
        rows.append({"time": t, **paired(w.loc[t0], w.loc[t])})
    out = pd.DataFrame(rows).set_index("time")
    complete = w.loc[:, w.notna().all()]
    out.attrs["anova_hearts"] = complete.shape[1]
    if complete.shape[1] >= 2:
        long = complete.stack().rename("value").reset_index()
        long["time"] = long["time"].astype(str)
        res = AnovaRM(long, "value", "heart", within=["time"]).fit().anova_table
        out.attrs["anova_F"] = float(res["F Value"].iloc[0])
        out.attrs["anova_df"] = (float(res["Num DF"].iloc[0]), float(res["Den DF"].iloc[0]))
        out.attrs["anova_p"] = float(res["Pr > F"].iloc[0])
        p = [paired(complete.loc[t0], complete.loc[t])["p"] for t in out.index]
        out["p_rm_holm_sidak"] = multipletests(p, method="holm-sidak")[1]
    else:
        out.attrs["anova_p"] = np.nan
        out["p_rm_holm_sidak"] = np.nan
    return out


def anova_line(res: pd.DataFrame) -> str:
    if np.isnan(res.attrs.get("anova_p", np.nan)):
        return f"repeated measures ANOVA not run ({res.attrs['anova_hearts']} hearts with complete data)"
    a, b = res.attrs["anova_df"]
    return (f"repeated measures ANOVA over {res.attrs['anova_hearts']} hearts: F({a:.0f}, {b:.0f}) = "
            f"{res.attrs['anova_F']:.2f}, p = {res.attrs['anova_p']:.3g}")


def monotonic(w: pd.DataFrame, direction: int) -> dict:
    """The claims file's two readings of "monotonic" (fig2a-rabbit-monotonic).

    (a) the mean over hearts moves in `direction` (+1 up, -1 down) at every successive time point;
    (b) no successive pair of time points differs in the opposite direction by a paired t-test at
    p < 0.05. Returns both, with the steps that break each.
    """
    m = w.mean(axis=1)
    steps = np.sign(np.diff(m.values))
    broken_a = [(float(m.index[i]), float(m.index[i + 1]), float(m.values[i + 1] - m.values[i]))
                for i in range(len(steps)) if steps[i] != direction]
    broken_b = []
    for i in range(len(w.index) - 1):
        r = paired(w.iloc[i], w.iloc[i + 1])
        if r["p"] < 0.05 and np.sign(r["mean_diff"]) == -direction:
            broken_b.append((float(w.index[i]), float(w.index[i + 1]), r["mean_diff"], r["p"]))
    return {"a": not broken_a, "a_broken": broken_a, "b": not broken_b, "b_broken": broken_b}
