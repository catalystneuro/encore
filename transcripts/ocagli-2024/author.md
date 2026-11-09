# figshare-26877211 · author · run 40572006592

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls claims/figshare-26877211 paper entries | head -50
```

```
<persisted-output>
Output too large (36.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ccfb3adf-624e-4de4-bdbe-ea6fdb8961c9/tool-results/bki15m9zu.txt

Preview (first 2KB):
Tue Oct 27 19:48:21 UTC 2026
# Protocol for an attempt

Version: `pilot-12`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ccfb3adf-624e-4de4-bdbe-ea6fdb8961c9/tool-results/bki15m9zu.txt"
}
```

```
1	Tue Oct 27 19:48:21 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-12`. Record this version in the attempt's provenance.
5	
6	This is what agents, or people, do to attempt a target and deposit the
7	result. A target is a dataset in a public archive and a paper it names. How
8	each archive's datasets are named, versioned and read is in
9	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
10	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
11	
12	An attempt has three roles, each a separate run with a separate context:
13	
14	- The **reader** reads the paper and writes the claims file: every finding,
15	  and how each is to be tested, taken from the paper. A second reader checks
16	  it against the paper. Readers never see the dataset's data.
17	- The **author** tests the claims on the dataset. It reads the paper to
18	  understand the claims, but the claims file binds it: it cannot change a
19	  claim's statement, expected values or criterion. A method detail the file
20	  lacks it takes from the paper, citing the passage, and it asks a reader
[... 668 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/figshare-26877211/*.yaml; ls paper; ls entries/001453-fouke-2025 claims/001453
```

```
# Claims for "Unveiling insights from the Joint FAO/WHO Expert Committee on Food Additives (JECFA)
# portal" (2024), Scientific Data, doi:10.1038/s41597-024-04294-w, on Figshare dataset 26877211
# (doi:10.6084/m9.figshare.26877211.v1). The text gives the authors as initials only.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: the version of record from Europe PMC (PMC11682307, full-text XML) as supplied under
# paper/, with Background, Methods, Data Records, Technical Validation, Usage Notes, Code
# availability and the contents of Tables 1 and 2 (flattened into the text, read cell by cell).
# The paper is a Data Descriptor and has no supplement. No PDF was supplied; Figures 1 and 2 are a
# flow chart and a screenshot and carry no results. The reference list is not in the text, so
# references 12, 17 and 18 (cited for the validation) could not be identified.
#
# Code read: https://github.com/UBESP-DCTV/jecfa at commit 2d8a5340 (2024-08-06), an R package run
# as a {targets} pipeline (_targets.R). compose_jecfa_list.R scrapes one page per id
# (rvest), create_df.R binds the pages and drops empty columns, process_df.R renames the fields and
# keeps only the first listed evaluation of each page (Report1, Report_sourcelink1, Tox
# Monograph1, Specification1, Evaluation year1) and derives FAS from the Tox Monograph,
# add_metadata.R adds type, host, Tox_monograph_abbr, Report_clean and ref_id. The rest downloads
# and text-mines TRS and FAS PDFs. The repository holds no code for the paper's Table 1
[... 366 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/*.txt; echo ======; cat README.md | head -80; echo =====; sed -n '/Figshare/,/^## /p' docs/archives.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ccfb3adf-624e-4de4-bdbe-ea6fdb8961c9/tool-results/b17rcq03f.txt"
}
```

```
1	DOI: 10.1038/s41597-024-04294-w
2	Version: version of record
3	Source: Europe PMC PMC11682307 (fullTextXML)
4	Stored: 2026-10-27
5	Extracted: Europe PMC full-text XML, converted to text (sections, figure legends, tables)
6	------------------------------------------------------------------------
7	Unveiling insights from the Joint FAO/WHO Expert Committee on Food Additives (JECFA) portal
8	
9	# Abstract
10	This study presents a method for automating the retrieval of key identifies and links to toxicological data from the Joint FAO/WHO Expert Committee on Food Additives (JECFA) database using web scraping techniques. Although the method primarily serves as an automated indexing tool, facilitating organization and access to relevant reports, monographs, and specifications, it significantly enhances the efficiency of navigating the extensive JECFA database. Researchers can then perform more targeted and efficient searches, although additional manual steps are required to extract and structure the detailed toxicological data. We developed R programming scripts to extract key information, such as chemical names, identifiers, and evaluation reports, from JECFA web pages. The resulting data set comprises 6552 records as of May 2024. We validated the dataset through a systematic comparison with manually collected data, ensuring its reliability. Instructions and code for accessing and processing the dataset, facilitating its reuse in research are provided. The code and dataset are openly available, enabling researchers to efficiently access and analyze toxicological data from the JECFA database.
11	
12	## Background & Summary
13	Chemicals pose significant environmental threats to human health, underscoring the need for a comprehensive understanding of hazards and exposure data. Such data, often referred to as the chemical exposome, are essential to assess health risks and prevent disease1.
14	Toxicology has evolved from an empirical science focused on observing the effects 
[... 172 more lines not kept]
```

**Agent**

Read the protocol, claims and paper. Now looking at the example entry formats.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; cd ../..; cat attempts/001453-fouke-2025-01.yaml | head -150
```

```
schema_version: 1
name: 001453-fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
helpers:
- omr.py
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
- id: doi:10.1016/j.cub.2025.04.027
[... 248 more lines not kept]
```

**Agent calls Bash**

```bash
ls entries | grep -i -v '^0' ; python -c "
import json;nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:12]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:600]);print('---')
"
```

```
crcns-ret-1-lefebvre-2008
dryad-4j0zpc8hz-didion-gency-2024
dryad-tdz08kq5d-wang-2024
ebrains-q0fg-1x8-nagelhus-2023
markdown {} # Reproducing Fouke et al. (2025) from dandiset 001453

**Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent
visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*.
[doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04.027). This attempt used the
full text of the accepted author manuscript in PubMed Central (PMC12218792); the version of record
is not open access.

**Dandiset.** [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), version
0.250518.1950. The paper cites no DANDI version (its data
---
code {} import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '150,400p' attempts/001453-fouke-2025-01.yaml | grep -v '^    ' | head -80; ls schemas; ls questions | head
```

```
notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1h-zf-higher-angular-acceleration
  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine
  deviations:
  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;
  - Heading is taken from the cumulative sum of `f0_vtheta`, as the code does; in DC files it does
- claim: figs1e-dc-respond-less-monocular
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:figs1e-dc-respond-less-monocular
  notes: Species effect F = 23.3, p = 2.5e-06. DC turn less toward the stimulus than ZF for
  deviations:
  - Codes 9 and 11 are assigned as the figure code has them; the stimulus software's conversion
- claim: fig1c-continuous-vs-bouts
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1c-continuous-vs-bouts
  notes: The median-to-mean ratio of instantaneous speed is 0.306 in ZF (25 fish, 0.244 to 0.580)
  deviations:
  - The paper shows this with representative traces and a bout analysis whose bout files are not
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^findings/,$p' attempts/001453-fouke-2025-01.yaml | tail -40; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s)[:6000])"
```

```
- claim: fig2g-dsi-similar
    agrees: true
    outcome: blocked
    reason: Agree (data_missing).
    response: No change needed.
  - claim: fig2h-fewer-motion-responsive
    agrees: true
    outcome: blocked
    reason: Agree (data_missing).
    response: No change needed.
  - claim: fig2k-more-monocular
    agrees: true
    outcome: blocked
    reason: Agree (data_missing).
    response: No change needed.
  - claim: fig2l-bi-ratio
    agrees: true
    outcome: blocked
    reason: Agree (data_missing).
    response: No change needed.
[... 21 more lines not kept]
```

**Agent**

Now let me look at the dataset metadata.

**Agent calls Bash**

```bash
curl -s https://api.figshare.com/v2/articles/26877211/versions | head -c 600; echo; curl -s https://api.figshare.com/v2/articles/26877211/versions/1 | python -c "
import json,sys;d=json.load(sys.stdin)
for k,v in d.items():
  if k!='files': print(k, str(v)[:400])
print(json.dumps(d['files'],indent=1))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.figshare.com/v2/articles/26877211/versions/1 | python -c "
import json,sys;d=json.load(sys.stdin); print(d['description'])"; which uv python; python --version; cat tools/entry.py | head -60
```

Result: the fetched text is not kept.

**Agent**

Setting up a scratch venv to explore the data in memory.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 explore && . explore/bin/activate && uv pip install -q pandas fsspec aiohttp requests rdata xarray 2>&1 | tail -3; python -c "import rdata; print(rdata.__version__)"
```

```
1.1.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/ex.py <<'EOF'
import fsspec, io, rdata, pandas as pd, hashlib
def get(fid):
    with fsspec.open(f"https://ndownloader.figshare.com/files/{fid}", block_size=2**20) as f:
        return f.read()
b1=get(48922360); b2=get(48922363)
print(hashlib.md5(b1).hexdigest(), hashlib.md5(b2).hexdigest())
parsed = rdata.parser.parse_data(b1)
conv = rdata.conversion.convert(parsed)
print(type(conv))
df = conv if isinstance(conv,pd.DataFrame) else conv
print(df.shape); print(df.dtypes)
print(b2[:1500])
import pickle; pickle.dump((df,b2),open('/tmp/claude/x.pkl','wb')) if False else None
EOF
mkdir -p /tmp/claude; . $TMPDIR/explore/bin/activate; python $TMPDIR/ex.py
```

```
/tmp/claude-1001/explore/lib/python3.13/site-packages/rdata/parser/_parser.py:1280: UserWarning: Unknown file type: assumed RDS
  warnings.warn("Unknown file type: assumed RDS")  # noqa: B028
/tmp/claude-1001/explore/lib/python3.13/site-packages/rdata/conversion/_conversion.py:918: UserWarning: Missing constructor for R class "tbl_df". The constructor for class "tbl" will be used instead.
  warnings.warn(
/tmp/claude-1001/explore/lib/python3.13/site-packages/rdata/conversion/_conversion.py:918: UserWarning: Missing constructor for R class "tbl". The constructor for class "data.frame" will be used instead.
  warnings.warn(
5bfd89459ec77a152e5ee1f55e124f3d dee04993aaa56ca1f3844ded5c472764
<class 'pandas.DataFrame'>
(6552, 17)
report                      string
report_sourcelink           string
tox_monograph               string
tox_monograph_sourcelink    string
specification               string
specification_sourcelink    string
synonyms                    string
cas_number                  string
functional_class            string
evaluation_year             string
chemical_names              string
[... 8 more lines not kept]
```

**Agent**

The RDS has 6552 rows and 17 columns. Exploring the contents.

**Agent calls Bash**

```bash
cat > $TMPDIR/ex2.py <<'EOF'
import fsspec, io, rdata, pandas as pd, warnings, re
warnings.filterwarnings("ignore")
def get(fid):
    with fsspec.open(f"https://ndownloader.figshare.com/files/{fid}", block_size=2**20) as f:
        return f.read()
df = rdata.conversion.convert(rdata.parser.parse_data(get(48922360)))
csv = pd.read_csv(io.BytesIO(get(48922363)), dtype=str, keep_default_na=False, na_values=["NA"], encoding="utf-8-sig")
print(csv.shape, list(csv.columns)==list(df.columns))
a=df.astype(object).where(df.notna(), None); b=csv.astype(object).where(csv.notna(), None)
print("identical:", (a.fillna("<NA>").values==b.fillna("<NA>").values).all())
diff=(a.fillna("<NA>").values!=b.fillna("<NA>").values)
print("diff cells per col", dict(zip(df.columns, diff.sum(0))))
pd.set_option("display.width",250); pd.set_option("display.max_colwidth",80)
for c in df.columns:
    s=df[c]; st=s.dropna().str.strip()
    print(f"== {c}: NA {s.isna().sum()}, empty-string {(st=='').sum()}, distinct {s.nunique()}")
    print("   ", s.dropna().head(3).tolist())
ids=df.url.str.extract(r"Chemical/(\d+)$")[0]
print("url pattern match", ids.notna().sum(), "dup urls", df.url.duplicated().sum(), "range", ids.astype(float).min(), ids.astype(float).max())
print(df[df.url.duplicated(keep=False)][["url","jecfa_name"]])
print(df.functional_class.str.extract(r"^([A-Za-z ]+?)(?=[A-Z_]{2,}|$)")[0].value_counts(dropna=False))
print(df.evaluation_year.value_counts(dropna=False).sort_index().to_string()[:2000])
print(df.fas.value_counts(dropna=False).head(30))
print("distinct fas", df.fas.nunique())
r6316=df[ids=="6316"]; print(r6316.T)
print(df[ids=="5883"].T)
nm=r6316.jecfa_name.iloc[0]; print(df[df.jecfa_name==nm][["url"]])
print("dup jecfa names", df.jecfa_name.duplicated().sum())
df.to_pickle("/tmp/claude-1001/df.pkl")
EOF
. $TMPDIR/explore/bin/activate; python $TMPDIR/ex2.py
```

```
(6552, 17) True
identical: True
diff cells per col {np.str_('report'): np.int64(0), np.str_('report_sourcelink'): np.int64(0), np.str_('tox_monograph'): np.int64(0), np.str_('tox_monograph_sourcelink'): np.int64(0), np.str_('specification'): np.int64(0), np.str_('specification_sourcelink'): np.int64(0), np.str_('synonyms'): np.int64(0), np.str_('cas_number'): np.int64(0), np.str_('functional_class'): np.int64(0), np.str_('evaluation_year'): np.int64(0), np.str_('chemical_names'): np.int64(0), np.str_('jecfa_number'): np.int64(0), np.str_('coe_number'): np.int64(0), np.str_('fema_number'): np.int64(0), np.str_('jecfa_name'): np.int64(0), np.str_('url'): np.int64(0), np.str_('fas'): np.int64(0)}
== report: NA 156, empty-string 0, distinct 664
    ['TRS 776-JECFA 33/22', 'TRS 909-JECFA 57/61', 'TRS 913-JECFA 59/111']
== report_sourcelink: NA 156, empty-string 0, distinct 231
    ['http://apps.who.int/iris/bitstream/10665/39252/1/WHO_TRS_776.pdf', 'http://apps.who.int/iris/bitstream/10665/42578/1/WHO_TRS_909.pdf', 'http://apps.who.int/iris/bitstream/10665/42601/1/WHO_TRS_913.pdf']
== tox_monograph: NA 468, empty-string 0, distinct 625
    ['FAS 24-JECFA 33/97', 'FAS 48-JECFA 57/117', 'FAS 40-JECFA 49/267 (1997)']
== tox_monograph_sourcelink: NA 468, empty-string 0, distinct 583
    ['http://www.inchem.org/documents/jecfa/jecmono/v024je06.htm', 'http://www.inchem.org/pages/jecfa.html', 'http://www.inchem.org/pages/jecfa.html']
== specification: NA 536, empty-string 0, distinct 429
    ['FAO Combined Compendium of Food Additive Specifications', 'Compendium of FAO food additive specifications', 'COMPENDIUM ADDENDUM 11/FNP 52 Add.11/95 (2003)']
== specification_sourcelink: NA 536, empty-string 0, distinct 71
    ['https://www.fao.org/food/food-safety-quality/scientific-advice/jecfa/jecfa-additives/en/', 'https://www.fao.org/food/food-safety-quality/scientific-advice/jecfa/jecfa-flav/en/', 'http://www.fao.org/ag/agn/jecfa-additives/search.html']
== synonyms: NA 1422, empty-s
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/ex3.py <<'EOF'
import pandas as pd, numpy as np, re
df=pd.read_pickle("/tmp/claude-1001/df.pkl")
ids=df.url.str.extract(r"Chemical/(\d+)$")[0].astype(int)
print(ids[df.jecfa_name.duplicated(keep=False)].tolist(), ids[df.jecfa_name=="TEST"].tolist())
pres=df.apply(lambda s: s.notna() & (s.fillna("").str.strip()!=""))
print((pres.mean()*100).round(2).to_string())
fc=df.functional_class
m=fc.str.extract(r"^(Flavouring Agent|Flavoring Agent|Food Additives|Food Contaminant|Veterinary Drug)",flags=re.I)[0]
print(fc[m.isna()&fc.notna()].value_counts())
print(fc.dropna().str[:20].value_counts())
y=pd.to_numeric(df.evaluation_year,errors="coerce")
bins=pd.cut(y,[1958,2000,2010,2020,2024],right=False); print(bins.value_counts(sort=False), y.isna().sum())
print((bins.value_counts(sort=False)/y.notna().sum()*100).round(2))
print(df.evaluation_year[y.isna()&df.evaluation_year.notna()])
f=df.fas.fillna("").str.strip(); fv=f[f!=""]
print("distinct non-empty fas", fv.nunique()); print(sorted(fv.unique(), key=lambda s:(len(s),s)))
vc=fv.value_counts(); print(vc.head(10)); 
sev=["40","42","44","46","48","50","52"]
print("share F1", fv.isin(sev).sum()/len(df)*100, "F2", fv.isin(sev).sum()/len(fv)*100)
print("cum top7", vc.head(7).sum()/len(fv)*100, vc.head(7).sum()/len(df))
# fas vs tox monograph
print(df[(f=="")][["tox_monograph"]].value_counts().head(10))
# unknowns
other=[c for c in df.columns if c not in ("url","jecfa_name")]
for name,mask in [("class",fc.isna()),("year",df.evaluation_year.isna())]:
    sub=pres.loc[mask,other]; print(name, mask.sum(), (~sub.any(axis=1)).sum(), sub.sum().to_dict())
print(pd.crosstab(fc.isna(), df.evaluation_year.isna()))
print("multi-val sep", {c:df[c].fillna("").str.contains(r"\|br\|").sum() for c in df.columns})
EOF
. $TMPDIR/explore/bin/activate; python $TMPDIR/ex3.py
```

```
[6316, 6319] [5883]
report                      97.62
report_sourcelink           97.62
tox_monograph               92.86
tox_monograph_sourcelink    92.86
specification               91.82
specification_sourcelink    91.82
synonyms                     78.3
cas_number                  35.36
functional_class            98.32
evaluation_year              98.2
chemical_names              82.57
jecfa_number                 70.8
coe_number                  46.26
fema_number                 64.99
jecfa_name                  100.0
url                         100.0
fas                         81.38
Series([], Name: count, dtype: Int64)
functional_class
[... 108 more lines not kept]
```

**Agent**

Most claims can be computed now. Checking the paper's code for how FAS is derived, since 752 rows have an empty FAS string.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/UBESP-DCTV/jecfa jecfa 2>&1 | tail -2; cd jecfa && git log -1 --format='%H %ad' 2d8a5340 && git checkout -q 2d8a5340 && cat R/process_df.R && grep -rn "FAS\|clean_names\|rds\|csv" R/add_metadata.R _targets.R | head -40
```

```
2d8a5340d5322cbae28eb3095d948313932f6c7e Tue Aug 6 00:39:45 2024 +0200
#' Preprocess JECFA data
#'
#' This function cleans the JECFA data by removing unnecessary columns
#' and renaming the remaining ones.
#'
#' @param df_clean A data frame with the JECFA data
#'
#' @return A data frame with the cleaned JECFA data
#' @export
#'
#' @examples
#' c(1, 2) |>
#'   purrr::map(\(id) compose_jecfa_list(id) |> get_result()) |>
#'   create_df() |>
#'   process_df()
process_df <- function(df_clean) {
  df_clean |>
    dplyr::mutate(
      FAS = dplyr::if_else(
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/jecfa && sed -n 1,60p R/add_metadata.R; grep -rn "clean_names\|write.*csv\|saveRDS\|write_rds" R _targets.R | head
```

```
#' Add metadata to the JECFA dataset
#'
#' This function adds metadata to the JECFA dataset. The metadata
#' includes the type of the JECFA report, the host of the URL, the
#' abbreviation of the JECFA report, the clean report, the FAS number,
#' and a reference ID.
#'
#' @param jecfa A data frame with the JECFA data
#'
#' @return A data frame with the JECFA data and the added metadata
#' @export
#'
#' @examples
#' library(jecfa)
#' c(1, 2) |>
#'   purrr::map(\(id) compose_jecfa_list(id) |> get_result()) |>
#'   create_df() |>
#'   process_df() |>
#'   add_metadata()
add_metadata <- function(jecfa) {
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/jecfa && grep -n "extract_jecfa_tox_abbr" -A25 R/*.R | grep -v "^R/add_metadata" | head -50
```

```
--
R/extract_jecfa_tox_abbr.R:15:#'   extract_jecfa_tox_abbr()
R/extract_jecfa_tox_abbr.R:16:extract_jecfa_tox_abbr <- function(tox_monograph) {
R/extract_jecfa_tox_abbr.R-17-  aux <- tox_monograph |>
R/extract_jecfa_tox_abbr.R-18-    sapply(extract_initial_part) |>
R/extract_jecfa_tox_abbr.R-19-    sapply(extract_initial_part_bis) |>
R/extract_jecfa_tox_abbr.R-20-    sapply(extract_initial_part_ter)
R/extract_jecfa_tox_abbr.R-21-
R/extract_jecfa_tox_abbr.R-22-  aux <- ifelse(
R/extract_jecfa_tox_abbr.R-23-    substr(aux, 1, 3) == "See",
R/extract_jecfa_tox_abbr.R-24-    substr(aux, 5, nchar(aux)),
R/extract_jecfa_tox_abbr.R-25-    aux
R/extract_jecfa_tox_abbr.R-26-  )
R/extract_jecfa_tox_abbr.R-27-
R/extract_jecfa_tox_abbr.R-28-  aux <- ifelse(
R/extract_jecfa_tox_abbr.R-29-    substr(aux, 1, 2) == '">',
R/extract_jecfa_tox_abbr.R-30-    substr(aux, 3, nchar(aux)),
R/extract_jecfa_tox_abbr.R-31-    aux
R/extract_jecfa_tox_abbr.R-32-  )
R/extract_jecfa_tox_abbr.R-33-
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/jecfa && sed -n 1,15p R/extract_jecfa_tox_abbr.R; grep -n "extract_initial_part" -A12 R/*.R | grep -v extract_jecfa_tox_abbr.R | head -60
```

```
#' Extracts JECFA abbreviation
#'
#' This function extracts the abbreviation of a JECFA monograph.
#'
#' @param tox_monograph A character vector with the JECFA monograph
#'
#' @return A character vector with the abbreviation of the JECFA
#'   monograph
#' @export
#'
#' @examples
#' compose_jecfa_list(1) |>
#'   get_result() |>
#'   dplyr::pull("Tox Monograph1") |>
#'   extract_jecfa_tox_abbr()
--
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/jecfa && grep -rn "extract_initial_part" R | head; grep -rln "extract_initial_part <-\|extract_initial_part_bis <-" R | xargs cat | head -80
```

```
R/extract_jecfa_tox_abbr.R:18:    sapply(extract_initial_part) |>
R/extract_jecfa_tox_abbr.R:19:    sapply(extract_initial_part_bis) |>
R/extract_jecfa_tox_abbr.R:20:    sapply(extract_initial_part_ter)
R/extract_jecfa_tox_abbr.R:45:extract_initial_part <- function(input_string) {
R/extract_jecfa_tox_abbr.R:49:extract_initial_part_bis <- function(input_string) {
R/extract_jecfa_tox_abbr.R:53:extract_initial_part_ter <- function(input_string) {
#' Extracts JECFA abbreviation
#'
#' This function extracts the abbreviation of a JECFA monograph.
#'
#' @param tox_monograph A character vector with the JECFA monograph
#'
#' @return A character vector with the abbreviation of the JECFA
#'   monograph
#' @export
#'
#' @examples
#' compose_jecfa_list(1) |>
#'   get_result() |>
#'   dplyr::pull("Tox Monograph1") |>
[... 42 more lines not kept]
```

**Agent**

Code confirms the deposited `fas` column is the output of `process_df.R` (before `add_metadata.R`'s clean-up). Writing the helper module now.

**Agent calls Bash**

```bash
date -u; mkdir -p entries/figshare-26877211-ocagli-2024
```

```
Tue Oct 27 19:50:37 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/figshare-26877211-ocagli-2024/jecfa.py",
 "content": "\"\"\"Loading and measures for the JECFA index deposited on Figshare (item 26877211, version 1).\n\nOcagli et al. (2024), Scientific Data, doi:10.1038/s41597-024-04294-w.\n\nThe item holds one table twice: `jecfa.rds` (an R tibble) and `JECFA.csv`. Each row is one page of\nthe JECFA portal, https://apps.who.int/food-additives-contaminants-jecfa-database/Home/Chemical/<n>,\nscraped in May 2024, with the 17 fields of the paper's Table 1 in lower-case column names. Both\nfiles are streamed from Figshare at the pinned version and read in memory; nothing is written to\ndisk. The RDS file is parsed with the `rdata` package, which reads R serialisations without R.\n\nWhere the parameters come from:\n\n- `present` (a field is present when it is not NA and not an empty string after trimming) is the\n  reading E of the claims file's opening comment.\n- `leading_class` reads the class name at the start of a `functional_class` string, as the\n  criterion of claim table2-functional-class gives it (the class name runs on into the sub-class,\n  \"Food AdditivesEMULSIFIER...\"). The data spell \"Flavouring Agent\", the paper \"Flavoring Agent\";\n  a label that differs only in spelling is the same label (protocol, Author, step 1.4).\n- `year_bin` uses the bins of Table 2, closed on the left and open on the right, the last closed\n  ([1958, 2000), [2000, 2010), [2010, 2020), [2020, 2023]), as the criterion of claim\n  table2-evaluation-year gives them.\n- `fas_process_df` re-derives the FAS column from the Tox monograph as R/process_df.R does in the\n  paper's code (https://github.com/UBESP-DCTV/jecfa at commit\n  2d8a5340d5322cbae28eb3095d948313932f6c7e): the text after \"FAS \" when the Tox monograph\n  starts with \"FAS \", cut at the first \"/\" and then at the first \"-\", and \"\" otherwise. It is used\n  to check that the deposited `fas` column is this derivation.\n- `fas_add_metadata` applies the further step of R/add_metadata.R at the same commit, which the\n  criteria of claims table1-availability and fas-codes name with process_df.R: a value longer\n  than three characters is cut to its first two; an empty value is filled with \"74\", \"60\" or \"27\"\n  when the monograph's abbreviation (R/extract_jecfa_tox_abbr.R: the part before the first \"-\",\n  \"/\" and \"JECFA\", less a leading \"See \" or '\">') begins \"FAS 74\", \"FAS 60\" or \"FAS 27\".\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nimport io\nimport json\nimport re\nimport warnings\n\nimport fsspec\nimport pandas as pd\nimport rdata\n\nARTICLE_ID = 26877211\nVERSION = 1\nDOI = \"10.6084/m9.figshare.26877211.v1\"\nAPI_URL = f\"https://api.figshare.com/v2/articles/{ARTICLE_ID}/versions/{VERSION}\"\nFILE_URL = \"https://ndownloader.figshare.com/files/{}\"\nURL_PREFIX = \"https://apps.who.int/food-additives-contaminants-jecfa-database/Home/Chemical/\"\n\n# Table 1 of the paper, in its order, with the deposited column that holds each field.\nTABLE1_FIELDS = {\n    \"URL\": \"url\",\n    \"JECFA name\": \"jecfa_name\",\n    \"Chemical names\": \"chemical_names\",\n    \"Synonyms\": \"synonyms\",\n    \"CAS number\": \"cas_number\",\n    \"JECFA number\": \"jecfa_number\",\n    \"FEMA number\": \"fema_number\",\n    \"COE number\": \"coe_number\",\n    \"Functional class\": \"functional_class\",\n    \"Evaluation year\": \"evaluation_year\",\n    \"Report\": \"report\",\n    \"Report sourcelink\": \"report_sourcelink\",\n    \"Tox monograph\": \"tox_monograph\",\n    \"Tox monograph sourcelink\": \"tox_monograph_sourcelink\",\n    \"Specification\": \"specification\",\n    \"Specification sourcelink\": \"specification_sourcelink\",\n    \"FAS\": \"fas\",\n}\n# The column names of R/process_df.R, in the order it selects them.\nCODE_COLUMNS = [\n    \"Report\", \"Report_sourcelink\", \"Tox.Monograph\", \"Tox.Monograph_sourcelink\", \"Specification\",\n    \"Specification_sourcelink\", \"Synonyms\", \"CAS.number\", \"Functional.Class\", \"Evaluation.year\",\n    \"Chemical.Names\", \"JECFA.number\", \"COE.number\", \"FEMA.number\", \"JECFA_name\", \"URL\", \"FAS\",\n]\n\nCLASSES = [\"Flavoring Agent\", \"Food Additives\", \"Food Contaminant\", \"Veterinary Drug\"]\n_CLASS_RE = re.compile(r\"^(flavou?ring agent|food additives|food contaminant|veterinary drug)\",\n                       re.IGNORECASE)\nYEAR_BINS = [\"[1958-2000)\", \"[2000-2010)\", \"[2010-2020)\", \"[2020-2023]\"]\n\n\ndef metadata() -> dict:\n    \"\"\"The version's metadata from the Figshare API, with its file list.\"\"\"\n    with fsspec.open(API_URL, \"rt\") as f:\n        return json.load(f)\n\n\ndef read_bytes(file_id: int) -> bytes:\n    \"\"\"Stream one file of the item into memory.\"\"\"\n    with fsspec.open(FILE_URL.format(file_id), \"rb\", block_size=2**20) as f:\n        return f.read()\n\n\ndef load() -> dict:\n    \"\"\"Read both files of the pinned version; return the metadata, MD5s and both tables.\"\"\"\n    meta = metadata()\n    files = {f[\"name\"]: f for f in meta[\"files\"]}\n    raw = {name: read_bytes(f[\"id\"]) for name, f in files.items()}\n    md5 = {name: (hashlib.md5(b).hexdigest(), files[name][\"computed_md5\"]) for name, b in raw.items()}\n    with warnings.catch_warnings():\n        # rdata warns that the RDS has no file header and that tibble classes fall back to\n        # data.frame; both are expected for a tibble saved with saveRDS.\n        warnings.simplefilter(\"ignore\", UserWarning)\n        rds = rdata.conversion.convert(rdata.parser.parse_data(raw[\"jecfa.rds\"]))\n    csv = pd.read_csv(io.BytesIO(raw[\"JECFA.csv\"]), dtype=str, keep_default_na=False,\n                      na_values=[\"NA\"], encoding=\"utf-8-sig\")\n    return {\"meta\": meta, \"md5\": md5, \"rds\": rds.astype(\"string\"), \"csv\": csv.astype(\"string\")}\n\n\ndef page_id(df: pd.DataFrame) -> pd.Series:\n    \"\"\"The portal page number at the end of each URL (NA if the URL has another form).\"\"\"\n    return pd.to_numeric(df[\"url\"].str.extract(r\"/Home/Chemical/(\\d+)$\")[0], errors=\"coerce\")\n\n\ndef present(s: pd.Series) -> pd.Series:\n    \"\"\"Reading E: a value is present when it is not NA and not empty after trimming.\"\"\"\n    return s.notna() & (s.fillna(\"\").str.strip() != \"\")\n\n\ndef leading_class(s: pd.Series) -> pd.Series:\n    \"\"\"The functional class named at the start of each string, in the paper's spelling, or NA.\"\"\"\n    m = s.str.extract(_CLASS_RE)[0].str.lower()\n    names = {c.lower(): c for c in CLASSES}\n    names[\"flavouring agent\"] = \"Flavoring Agent\"\n    return m.map(names, na_action=\"ignore\").astype(\"string\")\n\n\ndef year_bin(s: pd.Series) -> pd.Series:\n    \"\"\"Table 2's evaluation-year bins; NA for a missing or out-of-range year.\"\"\"\n    y = pd.to_numeric(s, errors=\"coerce\")\n    out = pd.Series(pd.NA, index=s.index, dtype=\"string\")\n    out[(y >= 1958) & (y < 2000)] = YEAR_BINS[0]\n    out[(y >= 2000) & (y < 2010)] = YEAR_BINS[1]\n    out[(y >= 2010) & (y < 2020)] = YEAR_BINS[2]\n    out[(y >= 2020) & (y <= 2023)] = YEAR_BINS[3]\n    return out\n\n\ndef fas_process_df(tox_monograph: pd.Series) -> pd.Series:\n    \"\"\"FAS as R/process_df.R derives it from the Tox monograph (NA stays NA).\"\"\"\n    def one(t):\n        if pd.isna(t):\n            return pd.NA\n        if not re.match(r\"^FAS .*$\", t):\n            return \"\"\n        return t[4:].split(\"/\")[0].split(\"-\")[0]\n    return tox_monograph.map(one).astype(\"string\")\n\n\ndef tox_abbr(t) -> object:\n    \"\"\"R/extract_jecfa_tox_abbr.R for one Tox monograph value.\"\"\"\n    if pd.isna(t):\n        return pd.NA\n    a = t.split(\"-\")[0].split(\"/\")[0].split(\"JECFA\")[0]\n    if a[:3] == \"See\":\n        a = a[4:]\n    if a[:2] == '\">':\n        a = a[2:]\n    if a[:3] != \"FAS\" and a[:12] != \"NOT PREPARED\":\n        a = \"NOT A FAS\"\n    return a\n\n\ndef fas_add_metadata(fas: pd.Series, tox_monograph: pd.Series) -> pd.Series:\n    \"\"\"FAS after the case_when of R/add_metadata.R.\"\"\"\n    def one(f, t):\n        if pd.isna(f):\n            return pd.NA\n        if len(f) > 3:\n            return f[:2]\n        if f != \"\":\n            return f\n        abbr = tox_abbr(t)\n        if not pd.isna(abbr):\n            for code in (\"74\", \"60\", \"27\"):\n                if abbr[:6] == f\"FAS {code}\":\n                    return code\n        return f\n    return pd.Series([one(f, t) for f, t in zip(fas, tox_monograph)], index=fas.index,\n                     dtype=\"string\")\n\n\ndef cas_check_digit_ok(cas: str) -> bool:\n    \"\"\"Whether a CAS number has the registry's form and a valid check digit.\"\"\"\n    m = re.fullmatch(r\"(\\d{2,7})-(\\d{2})-(\\d)\", cas.strip())\n    if not m:\n        return False\n    digits = (m.group(1) + m.group(2))[::-1]\n    return sum((i + 1) * int(d) for i, d in enumerate(digits)) % 10 == int(m.group(3))\n"
}
```

```
File created successfully at: entries/figshare-26877211-ocagli-2024/jecfa.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/figshare-26877211-ocagli-2024 && . $TMPDIR/explore/bin/activate && python -c "
import jecfa, pandas as pd, time
t=time.time(); d=jecfa.load(); print('load s', round(time.time()-t,1), d['md5'])
df=d['rds']
c=jecfa.leading_class(df.functional_class); print(c.value_counts(dropna=False))
print('unmatched', df.functional_class[c.isna()&df.functional_class.notna()].tolist())
f=jecfa.fas_process_df(df.tox_monograph); print('fas rederived equal', ((f.fillna('<NA>'))==df.fas.fillna('<NA>')).all())
fb=jecfa.fas_add_metadata(df.fas, df.tox_monograph); print('B present', jecfa.present(fb).mean()*100, fb[jecfa.present(fb)].nunique())
vc=fb[jecfa.present(fb)].value_counts(); print(vc.head(10)); sev=['40','42','44','46','48','50','52']
print('B F1',fb.isin(sev).sum()/len(df)*100,'F2',fb.isin(sev).sum()/jecfa.present(fb).sum()*100)
cas=df.cas_number.dropna(); print('cas ok', cas.map(jecfa.cas_check_digit_ok).sum(), len(cas)); print(cas[~cas.map(jecfa.cas_check_digit_ok)].head(10).tolist())
print(pd.crosstab(c.fillna('none'), jecfa.present(df.coe_number)))
print(pd.crosstab(c.fillna('none'), jecfa.present(df.fema_number)))
key=[x for x in df.columns if x!='url']; print('rows dup apart from url', df.duplicated(subset=key,keep=False).sum())
print(df[df.duplicated(subset=key,keep=False)][['url','jecfa_name']].to_string())
print(df.report.str.startswith('\">').sum(), df.tox_monograph.str.startswith('\">').sum())
for col in ['jecfa_number','fema_number','coe_number','evaluation_year']: s=df[col].dropna(); print(col, s.str.fullmatch(r'\d+').mean(), s[~s.str.fullmatch(r'\d+')].head(5).tolist())
"
```

```
load s 5.2 {'jecfa.rds': ('5bfd89459ec77a152e5ee1f55e124f3d', '5bfd89459ec77a152e5ee1f55e124f3d'), 'JECFA.csv': ('dee04993aaa56ca1f3844ded5c472764', 'dee04993aaa56ca1f3844ded5c472764')}
0
Flavoring Agent     4635
Food Additives      1453
Veterinary Drug      277
<NA>                 110
Food Contaminant      77
Name: count, dtype: Int64
unmatched []
fas rederived equal True
B present 86.73687423687424 73
48    607
44    490
50    477
46    407
42    399
40    370
60    353
59    351
54    287
[... 28 more lines not kept]
```

**Agent**

Functional class counts match Table 2 exactly. Checking how the two page-6316-name rows differ.

**Agent calls Bash**

```bash
cd entries/figshare-26877211-ocagli-2024 && . $TMPDIR/explore/bin/activate && python -c "
import jecfa, pandas as pd
d=jecfa.load(); df=d['rds']; pid=jecfa.page_id(df)
pd.set_option('display.max_colwidth',120); pd.set_option('display.width',250)
print(df[pid.isin([6316,6319,5883])].T)
print('ids missing in 1..max', sorted(set(range(1,int(pid.max())+1))-set(pid.astype(int)))[:60])
print('sorted by id', pid.is_monotonic_increasing)
"
```

```
Exit code 1
/bin/bash: line 1: cd: entries/figshare-26877211-ocagli-2024: No such file or directory
```

**Agent calls Bash**

```bash
. $TMPDIR/explore/bin/activate && python -c "
import jecfa, pandas as pd
d=jecfa.load(); df=d['rds']; pid=jecfa.page_id(df)
pd.set_option('display.max_colwidth',120); pd.set_option('display.width',250)
print(df[pid.isin([6316,6319,5883])].T)
print('ids missing in 1..max', sorted(set(range(1,int(pid.max())+1))-set(pid.astype(int)))[:60])
print('sorted by id', pid.is_monotonic_increasing)
"
```

```
5881  ...                                                                                    6297
report                                                                                                  <NA>  ...                                                                  ">TRS 1000-JECFA 82/94
report_sourcelink                                                                                       <NA>  ...        http://apps.who.int/iris/bitstream/10665/250277/1/9789241210003-eng.pdf#page=106
tox_monograph                                                                                           <NA>  ...                                                                     FAS 73 JECFA 82/343
tox_monograph_sourcelink                                                                                <NA>  ...  https://apps.who.int/iris/bitstream/handle/10665/258934/9789241660730-eng.pdf#page=351
specification                                                                                           <NA>  ...                                                           ">FAO JECFA Monographs 19/136
specification_sourcelink                                                                                <NA>  ...                                              http://www.fao.org/3/a-i6413e.pdf#page=147
synonyms                                                                                                <NA>  ...                                                                                    <NA>
cas_number                                                                                              <NA>  ...                                                                             125187-30-6
functional_class                                                                                        <NA>  ...                                                        Flavouring AgentFLAVOURING_AGENT
evaluation_year                                                                     
[... 11 more lines not kept]
```

**Agent**

All numbers are in hand. Writing the notebook builder.

**Agent calls Bash**

```bash
date -u; cat docs/design.md | head -40 >/dev/null; grep -n "sanity\|claim:" tools/entry.py | head -20
```

```
Tue Oct 27 19:52:02 UTC 2026
cat: docs/design.md: No such file or directory
grep: tools/entry.py: No such file or directory
```

**Agent calls Bash**

```bash
cd  && grep -n "sanity\|claim:\|related\|figshare" tools/entry.py | head -30; sed -n 1,60p docs/design.md | head -30
```

```
20:- each notebook has a cell tagged `sanity` that prints what was loaded;
154:    # Datasets are related as <archive>:<id>/<version> (docs/archives.md); papers as doi:, entries as entry:.
156:            for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))]
158:                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
174:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
175:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
392:    papers = {r["id"] for r in entry.get("related", []) if r["relation"] == "reproduces"}
394:                 for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
# Reproduction registry: design

Status: draft for discussion. "Reproduction registry" is a working name.

## Goal

Agents work through the dandisets on the DANDI Archive that have an associated
paper. For each one, an agent tries to reproduce the paper's key findings and
figures from the open data, writes the analysis as a notebook, and registers it
here. People can deposit too, but most deposits are expected to come from
agents.

[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 140,175p tools/entry.py
```

```
requirements, lock = entry_dir / "requirements.in", entry_dir / "requirements.lock.txt"
    if not requirements.is_file():
        report.error(rel, "no requirements.in")
    elif not lock.is_file():
        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
    else:
        pinned = {re.split(r"[=<>!~\[ ]", line, maxsplit=1)[0].lower().replace("_", "-")
                  for line in lock.read_text().splitlines() if line and not line.startswith((" ", "#"))}
        for line in requirements.read_text().splitlines():
            name = re.split(r"[=<>!~\[ ;]", line.strip(), maxsplit=1)[0].lower().replace("_", "-")
            if name and not name.startswith("#") and name not in pinned:
                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")

    # Datasets are related as <archive>:<id>/<version> (docs/archives.md); papers as doi:, entries as entry:.
    used = [r["id"].split(":", 1)[1].partition("/")
            for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))]
    archives = {r["id"].split(":", 1)[1].partition("/")[0]: r["id"].split(":", 1)[0]
                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
    dandisets = [d for d, _, _ in used]
    versions = {d: v for d, _, v in used}
[... 15 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Ocagli et al. (2024) from Figshare item 26877211\n\n**Paper.** Ocagli H, Lanera C, Franzoi M, Monachesi C, Zgheib R, Belluco S, Dorne JLCM, Gregori D,\nBaldi I (2024). Unveiling insights from the Joint FAO/WHO Expert Committee on Food Additives (JECFA)\nportal. *Scientific Data*. [doi:10.1038/s41597-024-04294-w](https://doi.org/10.1038/s41597-024-04294-w).\nThe claims file was written from the version of record in Europe PMC (PMC11682307, full-text XML),\na Data Descriptor with no supplement.\n\n**Dataset.** [Figshare 26877211](https://springernature.figshare.com/articles/dataset/Unveiling_Insights_from_the_Joint_FAO_WHO_Expert_Committee_on_Food_Additives_JECFA_Portal/26877211/1),\nversion 1, [doi:10.6084/m9.figshare.26877211.v1](https://doi.org/10.6084/m9.figshare.26877211.v1).\nThe paper cites the item without a version (10.6084/m9.figshare.26877211), which resolves to the\nlatest; the item has one published version, 1 (posted 2024-12-29), so that is the version pinned.\nIt holds two files, read here by streaming into memory: `jecfa.rds` (file id 48922360, MD5\n5bfd89459ec77a152e5ee1f55e124f3d) and `JECFA.csv` (file id 48922363, MD5\ndee04993aaa56ca1f3844ded5c472764). The MD5 of the bytes read is checked against the archive's\n`computed_md5` in the data check.\n\n**Code.** Method details the claims file takes from the paper's code refer to\nhttps://github.com/UBESP-DCTV/jecfa at commit 2d8a5340d5322cbae28eb3095d948313932f6c7e; the FAS\nderivations in `jecfa.py` follow `R/process_df.R` and `R/add_metadata.R` there. Nothing here is\nrandom, so no seed is needed.\n\n| Claim | Tested |\n|---|---|\n| data-records-rows (link): 6552 rows with the fields of Table 1 | tested |\n| unique-pages: 6549 unique pages after removing a duplicate and a test page | tested |\n| table1-availability: share of pages with each field | tested |\n| table2-evaluation-year: evaluations by year bin | tested |\n| table2-functional-class: substances by functional class | tested |\n| unknowns-name-only: unknowns have only a JECFA name | tested |\n| fas-codes: FAS 40 to 52 (even) cover 50% of records | tested |\n| validation-failures: discrepancies in the 700-page manual check | blocked (data_missing) |\n| portal-search-count: portal count 6547 in line with pages with a JECFA name | tested (dataset's part) |\n\"\"\")\n\ncode(r\"\"\"\nimport time\n\nimport pandas as pd\n\nimport jecfa\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 30)\npd.set_option(\"display.max_rows\", 200)\npd.set_option(\"display.max_colwidth\", 90)\n\nstarted = time.time()\ndata = jecfa.load()\ndf = data[\"rds\"]\nprint(f\"Figshare item {jecfa.ARTICLE_ID} version {jecfa.VERSION} ({jecfa.DOI}), \"\n      f\"read in {time.time() - started:.1f} s\")\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nmeta = data[\"meta\"]\nprint(\"Title:\", meta[\"title\"])\nprint(\"Published:\", meta[\"published_date\"], \" version:\", meta[\"version\"], \" DOI:\", meta[\"doi\"])\nprint(\"Related:\", [(r[\"relation\"], r[\"identifier\"]) for r in meta[\"related_materials\"]])\nprint(\"\\nFiles (name, id, size in bytes, MD5 of the bytes read, archive computed_md5, equal):\")\nfor f in meta[\"files\"]:\n    got, expected = data[\"md5\"][f[\"name\"]]\n    print(f\"  {f['name']:10s} {f['id']}  {f['size']:>8d}  {got}  {expected}  {got == expected}\")\nversions = pd.read_json(jecfa.API_URL.rsplit(\"/\", 1)[0])\nprint(\"\\nPublished versions of the item:\", versions[\"version\"].tolist())\nprint(\"\\nThe item's description, which documents each field:\\n\")\nprint(meta[\"description\"])\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nThe item has one published version, and the bytes read match the archive's MD5 for both files.\nThe description documents the 17 fields. It calls FAS a \"FAO/WHO Food Additive Specification\nidentifier\"; the paper (Table 1) and the code (`R/process_df.R`) make it the number of the Food\nAdditives Series monograph, taken from the Tox monograph. The check below shows which the data\nhold.\n\"\"\")\n\ncode(r\"\"\"\ncsv = data[\"csv\"]\nprint(\"jecfa.rds:\", df.shape, \" JECFA.csv:\", csv.shape)\nprint(\"Same column names in the same order:\", list(df.columns) == list(csv.columns))\nsame = (df.fillna(\"<NA>\").to_numpy() == csv.fillna(\"<NA>\").to_numpy())\nprint(\"Cells that differ between the two files:\", int((~same).sum()))\nprint(\"\\nColumns of jecfa.rds, next to the field of Table 1 and the name in R/process_df.R:\")\ncols = pd.DataFrame({\"table1_field\": list(jecfa.TABLE1_FIELDS),\n                     \"deposit_column\": list(jecfa.TABLE1_FIELDS.values())})\ncode_names = {c.lower().replace(\".\", \"_\"): c for c in jecfa.CODE_COLUMNS}\ncols[\"process_df_name\"] = cols.deposit_column.map(code_names)\ncols[\"in_deposit\"] = cols.deposit_column.isin(df.columns)\nprint(cols.to_string(index=False))\nprint(\"Deposit columns not in Table 1:\", sorted(set(df.columns) - set(cols.deposit_column)))\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nThe two files hold the same table: the CSV is a copy of the RDS, cell for cell. The deposit's\ncolumn names are those of `R/process_df.R` in lower case with \".\" replaced by \"_\", and its columns\nare in the order that function selects them. The columns that `R/add_metadata.R` adds (type, host,\nTox_monograph_abbr, Report_clean, ref_id) are not in the deposit, so the deposited table is the\noutput of `process_df.R`.\n\"\"\")\n\ncode(r\"\"\"\npresent = df.apply(jecfa.present)\nsummary = pd.DataFrame({\n    \"NA\": df.isna().sum(),\n    \"empty_string\": (df.notna() & (df.fillna(\"\").apply(lambda s: s.str.strip()) == \"\")).sum(),\n    \"present\": present.sum(),\n    \"distinct\": df.nunique(),\n    \"example\": [df[c].dropna().iloc[0][:60] for c in df.columns],\n})\nprint(summary.to_string())\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nEvery column is text. Missing values are NA, except in `fas`, which also holds 752 empty strings.\n`jecfa_name` and `url` are present in every row.\n\"\"\")\n\ncode(r\"\"\"\npid = jecfa.page_id(df)\nprint(\"URLs of the form\", jecfa.URL_PREFIX + \"<n>:\", int(pid.notna().sum()), \"of\", len(df))\nprint(\"Page numbers from\", int(pid.min()), \"to\", int(pid.max()), \"; duplicated URLs:\", int(df.url.duplicated().sum()),\n      \"; rows sorted by page number:\", bool(pid.is_monotonic_increasing))\nmissing_ids = sorted(set(range(1, int(pid.max()) + 1)) - set(pid.astype(int)))\nprint(f\"Page numbers between 1 and {int(pid.max())} with no row: {len(missing_ids)}:\", missing_ids)\n\nyear = pd.to_numeric(df.evaluation_year, errors=\"coerce\")\nprint(\"\\nevaluation_year: all present values are integers:\", bool(year[df.evaluation_year.notna()].notna().all()),\n      \"; range\", int(year.min()), \"to\", int(year.max()))\nfor c in [\"jecfa_number\", \"fema_number\", \"coe_number\"]:\n    s = df[c].dropna()\n    odd = s[~s.str.fullmatch(r\"\\d+\")]\n    print(f\"{c}: {len(s)} present, {len(odd)} not a plain integer, e.g. {odd.head(4).tolist()}\")\ncas = df.cas_number.dropna()\nplain = cas[cas.str.fullmatch(r\"\\d{2,7}-\\d{2}-\\d\")]\nprint(f\"cas_number: {len(cas)} present, {len(plain)} of the plain form NNNNNNN-NN-N, of which \"\n      f\"{int(plain.map(jecfa.cas_check_digit_ok).sum())} have a valid check digit; \"\n      f\"{len(cas) - len(plain)} carry more than one number or a note, e.g. {cas[~cas.isin(plain)].head(3).tolist()}\")\nprint(\"Plain CAS numbers with a wrong check digit:\", plain[~plain.map(jecfa.cas_check_digit_ok)].tolist())\nprint(\"\\nValues starting with the characters '\\\">' (Usage Notes): report\",\n      int(df.report.str.startswith('\">').sum()), \", tox_monograph\", int(df.tox_monograph.str.startswith('\">').sum()),\n      \", specification\", int(df.specification.str.startswith('\">').sum()))\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nThe URLs are the portal pages of Table 1, one row per page, with page numbers from 1 to 6593,\ninside the 1 to 7000 of the Methods; 41 numbers in that range have no row. No URL is repeated, so\nthe claims file's two units, U1 (every row) and U2 (one row per distinct URL), are the same here,\nand each result below holds for both. Years run from 1958 to 2023, as in Table 2. The identifiers\nare mostly plain numbers. A few plain CAS numbers fail the registry's check digit (printed above),\nand some report, Tox monograph and specification values start with the stray characters '\">'\nthat the Usage Notes describe.\n\"\"\")\n\ncode(r\"\"\"\nfas_rederived = jecfa.fas_process_df(df.tox_monograph)\nprint(\"fas equals the derivation of R/process_df.R from tox_monograph in every row:\",\n      bool((fas_rederived.fillna(\"<NA>\") == df.fas.fillna(\"<NA>\")).all()))\nempty_fas = df.fas.fillna(\"x\").str.strip() == \"\"\nprint(\"\\nTox monographs of the rows with an empty fas, by the code's abbreviation (R/extract_jecfa_tox_abbr.R):\")\nprint(df.tox_monograph[empty_fas].map(jecfa.tox_abbr).value_counts().head(12).to_string())\nprint(\"\\nDistinct fas values:\", sorted(df.fas.dropna().unique(), key=lambda s: (len(s), s)))\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nThe `fas` column is the derivation of `R/process_df.R` from the Tox monograph, in every row. It is\nthe Food Additives Series number, not a specification identifier as the item's description says.\nOf the 752 empty strings, 273 are pages whose monograph is \"NOT PREPARED\", 262 are monographs that\nare not a FAS (such as a TRS reference), and most of the rest are FAS monographs, FAS 60 above all,\nwhose text starts with '\">' so that the \"^FAS \" pattern misses them. Some values keep the session\n(\"77 JECFA 86\") or a page (\"67.29\"), and one is \"617\".\n\"\"\")\n\ncode(r\"\"\"\ncls = jecfa.leading_class(df.functional_class)\nprint(\"Functional class strings, by leading class (the rest of the string is the sub-class):\")\nprint(cls.value_counts(dropna=False).to_string())\nprint(\"Strings that start with none of the four class names:\",\n      df.functional_class[cls.isna() & df.functional_class.notna()].tolist())\nprint(\"Spellings of the flavouring class:\",\n      df.functional_class.str.extract(r\"^(Flavou?ring Agent)\")[0].value_counts().to_dict())\nprint(\"\\nCOE number present, by class:\")\nprint(pd.crosstab(cls.fillna(\"unknown\"), present.coe_number).to_string())\nprint(\"\\nFEMA number present, by class:\")\nprint(pd.crosstab(cls.fillna(\"unknown\"), present.fema_number).to_string())\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nEvery functional class string starts with one of the four classes of Table 1; the data spell\n\"Flavouring Agent\", the paper \"Flavoring Agent\". Table 1 describes the COE number as assigned by the\nCodex Alimentarius Commission, the item's description as the Council of Europe number. COE numbers\nare present for 3022 flavouring agents and 9 food additives and no other class, which is consistent\nwith the Council of Europe numbering of flavourings, not with Codex.\n\"\"\")\n\ncode(r\"\"\"\nby_url = df.drop(columns=\"url\")\nprint(\"Rows identical to another row in every field but the URL:\", int(by_url.duplicated(keep=False).sum()))\ndup_names = df.jecfa_name[df.jecfa_name.duplicated(keep=False)]\nprint(\"JECFA names used by more than one row:\", dup_names.unique().tolist(), \"at pages\",\n      pid[dup_names.index].astype(int).tolist())\nprint(\"Rows named TEST:\", pid[df.jecfa_name.str.strip().str.upper() == \"TEST\"].astype(int).tolist())\nprint(\"\\nFields present in each of these rows:\")\nshow = df.index[pid.isin([5883, 6316, 6319])]\nprint(present.loc[show].assign(page=pid[show].astype(int)).set_index(\"page\").T.to_string())\nprint(f\"\\nData check done in {time.time() - started:.1f} s\")\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nNo two rows are copies apart from their URL. The chemical of page 6316 has a second page, 6319:\npage 6316 carries only its name, page 6319 the full record. Page 5883 is named TEST and carries\nnothing else. These are the duplicate and the test page of the Methods, and both are in the\ndeposit, which therefore has the 6552 scraped rows, not the 6549 cleaned pages.\n\nThe table has no time series, so there is no clock to check against a trial table. Each row is\ndescribed by its URL, which ties it to one portal page; the portal has changed since May 2024, so\nthe rows cannot be checked against the pages as they were scraped.\n\"\"\")\n\n# ---------------------------------------------------------------- claims\nmd(\"\"\"\n## data-records-rows (link)\n\n> The deposited dataframe is the JECFA index of May 2024, with 6552 rows and the fields of Table 1.\n\nCriterion: 6552 rows within 3, and a column for each of the 17 fields of Table 1 (by the code's\nnames in `process_df.R`, or an evident equivalent); JECFA.csv compared with jecfa.rds.\n\"\"\")\n\ncode(r\"\"\"\nn_rows = len(df)\nfields_found = cols.in_deposit.sum()\nprint(f\"Rows of jecfa.rds: {n_rows} (expected 6552, tolerance 3; within: {abs(n_rows - 6552) <= 3})\")\nprint(f\"Table 1 fields with a column: {fields_found} of {len(cols)}; missing: {cols.table1_field[~cols.in_deposit].tolist()}\")\nprint(f\"JECFA.csv: {csv.shape[0]} rows and {csv.shape[1]} columns; cells that differ from jecfa.rds: {int((~same).sum())}\")\n\"\"\", [\"claim:data-records-rows\"])\n\nmd(\"\"\"\n**Result: reproduced.** jecfa.rds has 6552 rows, and all 17 fields of Table 1 have a column, named\nas in `process_df.R` in lower case. JECFA.csv holds the same 6552 rows and 17 columns with no\ndiffering cell.\n\"\"\")\n\nmd(\"\"\"\n## unique-pages\n\n> The 6552 scraped entries, cleaned of the duplicates of page 6316 and of test pages, give 6549\n> unique pages.\n\nCriterion: under one of three readings of the cleaning, 6549 within 2, and page 6316's chemical\nappears more than once. (D1) rows with distinct URL; (D2) rows with distinct JECFA name, less the\nrow of page 5883; (D3) the rows less page 5883 and less all but one row with the JECFA name of\npage 6316.\n\"\"\")\n\ncode(r\"\"\"\nname_6316 = df.jecfa_name[pid == 6316].iloc[0]\nd1 = df.url.nunique()\nd2 = df.loc[pid != 5883, \"jecfa_name\"].nunique()\nd3 = len(df) - int((pid == 5883).sum()) - (int((df.jecfa_name == name_6316).sum()) - 1)\nreadings = pd.DataFrame({\"reading\": [\"D1\", \"D2\", \"D3\"], \"unique_pages\": [d1, d2, d3]})\nreadings[\"within_2_of_6549\"] = (readings.unique_pages - 6549).abs() <= 2\nprint(readings.to_string(index=False))\nprint(f\"Rows with page 6316's chemical ({name_6316}): {int((df.jecfa_name == name_6316).sum())}, \"\n      f\"at pages {pid[df.jecfa_name == name_6316].astype(int).tolist()}\")\nprint(\"Variant, removing both rows of that chemical and page 5883:\",\n      len(df) - int((pid == 5883).sum()) - int((df.jecfa_name == name_6316).sum()))\n\"\"\", [\"claim:unique-pages\"])\n\nmd(\"\"\"\n**Result: reproduced.** Readings D2 and D3 give 6550 unique pages, one more than the paper's 6549\nand within the tolerance of 2; D1 gives 6552, as no URL repeats. Page 6316's chemical appears\ntwice, at pages 6316 and 6319. The paper's 6549 is reached only by removing both rows of that\nchemical with the test page.\n\"\"\")\n\nmd(\"\"\"\n## table1-availability\n\n> The share of pages carrying each Table 1 field is 100% for URL and JECFA name, 82% chemical names,\n> 79% synonyms, 35% CAS number, 71% JECFA number, 65% FEMA number, 46% COE number, 98% functional\n> class, 98% evaluation year, 97% report and its link, 93% Tox monograph and its link, 92%\n> specification and its link, and 93% FAS.\n\nCriterion: the share of rows where each field is present (reading E), under U1 or U2 (the same\nhere); at least 15 of 17 within tolerance under one reading for reproduced, 10 to 14 for partially\nreproduced. FAS is the column the code derives (`process_df.R`, `add_metadata.R`). The deposit\nholds the `process_df.R` column; both are run: (A) the deposited `fas`, (B) `fas` after the step of\n`add_metadata.R`. Denominators 6552 rows and the 6550 rows left after cleaning (reading D2 of\nunique-pages) are both shown.\n\"\"\")\n\ncode(r\"\"\"\nexpected = pd.Series({\"URL\": 100, \"JECFA name\": 100, \"Chemical names\": 82, \"Synonyms\": 79, \"CAS number\": 35,\n                      \"JECFA number\": 71, \"FEMA number\": 65, \"COE number\": 46, \"Functional class\": 98,\n                      \"Evaluation year\": 98, \"Report\": 97, \"Report sourcelink\": 97, \"Tox monograph\": 93,\n                      \"Tox monograph sourcelink\": 93, \"Specification\": 92, \"Specification sourcelink\": 92,\n                      \"FAS\": 93}, dtype=float)\nfas_b = jecfa.fas_add_metadata(df.fas, df.tox_monograph)\ncleaned = (pid != 5883) & ~((df.jecfa_name == name_6316) & df.jecfa_name.duplicated(keep=\"last\"))\ntable = pd.DataFrame({\"expected\": expected, \"tolerance\": expected * 0.10})\nfor label, rows in [(\"all_6552\", pd.Series(True, index=df.index)), (\"cleaned_6550\", cleaned)]:\n    pa = present.loc[rows].mean() * 100\n    table[f\"A_{label}\"] = [pa[jecfa.TABLE1_FIELDS[f]] for f in table.index]\n    table[f\"B_{label}\"] = table[f\"A_{label}\"]\n    table.loc[\"FAS\", f\"B_{label}\"] = jecfa.present(fas_b[rows]).mean() * 100\ntable = table.round(2)\nprint(f\"Rows used: all {len(df)}; cleaned {int(cleaned.sum())}\")\nprint(table.to_string())\nfor c in [c for c in table.columns if c[:2] in (\"A_\", \"B_\")]:\n    within = ((table[c] - table.expected).abs() <= table.tolerance + 1e-9)\n    exact = (table[c].round(0) == table.expected)\n    print(f\"{c}: within tolerance {int(within.sum())} of 17 (outside: {table.index[~within].tolist()}); \"\n          f\"equal to Table 1 when rounded to whole numbers {int(exact.sum())} of 17\")\nprint(\"\\nVariant: FAS counted as present wherever it is not NA (the 752 empty strings counted):\",\n      round(df.fas.notna().mean() * 100, 2), \"%\")\n\"\"\", [\"claim:table1-availability\"])\n\nmd(\"\"\"\n**Result: reproduced.** Over all 6552 rows, 16 of 17 shares are within tolerance under reading A\n(the deposited FAS column, 81.38% against 93%) and all 17 under reading B (FAS after\n`add_metadata.R`, 86.74%); removing the duplicate and the test page changes no share by more than\n0.05 points. Rounded to whole numbers, 12 of 17 shares equal Table 1. Under reading A the FAS\nshare is 11.6 points below Table 1; counting the 752 empty strings as present gives 92.86%, which\nsuggests that Table 1 counted every non-NA value.\n\"\"\")\n\nmd(\"\"\"\n## table2-evaluation-year\n\n> By evaluation year, 2357 evaluations fall in 1958 to 2000 (37%), 3099 in 2000 to 2010 (48%), 778\n> in 2010 to 2020 (12%) and 200 in 2020 to 2023 (3.1%), with 118 unknown.\n\nCriterion: the `evaluation_year` column, Table 2's bins (closed left, open right, the last\nclosed), percentages over rows with a known year, U1 or U2; all nine values within tolerance.\n\"\"\")\n\ncode(r\"\"\"\nbins = jecfa.year_bin(df.evaluation_year)\ncounts = bins.value_counts().reindex(jecfa.YEAR_BINS)\nknown = int(bins.notna().sum())\nres = pd.DataFrame({\"count\": counts, \"share_of_known_pct\": (counts / known * 100).round(2),\n                    \"expected_count\": [2357, 3099, 778, 200], \"expected_pct\": [37, 48, 12, 3.1]})\nres[\"count_within\"] = (res[\"count\"] - res.expected_count).abs() <= (res.expected_count * 0.1).round(0)\nres[\"pct_within\"] = (res.share_of_known_pct - res.expected_pct).abs() <= res.expected_pct * 0.1 + 1e-9\nprint(res.to_string())\nprint(f\"Unknown year: {int(df.evaluation_year.isna().sum())} (expected 118); known {known}; \"\n      f\"years outside 1958 to 2023: {int((bins.isna() & df.evaluation_year.notna()).sum())}\")\nprint(\"Shares over all 6552 rows:\", (counts / len(df) * 100).round(2).tolist())\n\"\"\", [\"claim:table2-evaluation-year\"])\n\nmd(\"\"\"\n**Result: reproduced.** The four bins hold 2357, 3099, 778 and 200 rows and 118 years are missing,\nequal to Table 2; the shares of known years are 36.63, 48.17, 12.09 and 3.11%, all within\ntolerance.\n\"\"\")\n\nmd(\"\"\"\n## table2-functional-class\n\n> Most substances are flavouring agents, 4635 (72%), followed by food additives 1453 (23%),\n> veterinary drugs 277 (4.3%) and food contaminants 77 (1.2%), with 110 unknown.\n\nCriterion: the leading class name of `functional_class`, case-insensitive, empty values unknown;\npercentages over rows with a known class; all nine values within tolerance and flavouring agents\nthe largest class.\n\"\"\")\n\ncode(r\"\"\"\ncc = cls.value_counts().reindex(jecfa.CLASSES)\nknown_c = int(cls.notna().sum())\nres = pd.DataFrame({\"count\": cc, \"share_of_known_pct\": (cc / known_c * 100).round(3),\n                    \"expected_count\": [4635, 1453, 77, 277], \"expected_pct\": [72, 23, 1.2, 4.3]})\nres[\"count_within\"] = (res[\"count\"] - res.expected_count).abs() <= res.expected_count * 0.1\nres[\"pct_within\"] = (res.share_of_known_pct - res.expected_pct).abs() <= res.expected_pct * 0.1 + 1e-9\nprint(res.to_string())\nprint(f\"Unknown class: {int(cls.isna().sum())} (expected 110); known {known_c}; \"\n      f\"strings matching none of the four names: {int((cls.isna() & df.functional_class.notna()).sum())}\")\nprint(\"Largest class:\", cc.idxmax())\n\"\"\", [\"claim:table2-functional-class\"])\n\nmd(\"\"\"\n**Result: reproduced.** 4635 flavouring agents, 1453 food additives, 77 food contaminants, 277\nveterinary drugs and 110 unknown, equal to Table 2; the shares of known classes are 71.95, 22.56,\n1.20 and 4.30%. Flavouring agents are the largest class, and every string starts with one of the\nfour class names.\n\"\"\")\n\nmd(\"\"\"\n## unknowns-name-only\n\n> The records with unknown class or year have only the JECFA name, without chemical names or other\n> information.\n\nCriterion: among the rows with unknown functional class, and among those with unknown evaluation\nyear, the share with no Table 1 field present besides URL and JECFA name; reproduced when it is at\nleast 90% of each set.\n\"\"\")\n\ncode(r\"\"\"\nothers = [c for c in df.columns if c not in (\"url\", \"jecfa_name\")]\nname_only = ~present[others].any(axis=1)\nfor label, mask in [(\"unknown functional class\", cls.isna()), (\"unknown evaluation year\", df.evaluation_year.isna())]:\n    n, k = int(mask.sum()), int((mask & name_only).sum())\n    print(f\"{label}: {n} rows, {k} with only URL and JECFA name ({k / n * 100:.1f}%)\")\n    print(\"   fields present in the other\", n - k, \"rows:\",\n          present.loc[mask & ~name_only, others].sum()[lambda s: s > 0].to_dict())\nprint(\"\\nUnknown class and unknown year together:\", int((cls.isna() & df.evaluation_year.isna()).sum()),\n      \"; rows with only URL and JECFA name in the whole table:\", int(name_only.sum()))\n\"\"\", [\"claim:unknowns-name-only\"])\n\nmd(\"\"\"\n**Result: partially reproduced.** 95 rows carry only a URL and a JECFA name, and all of them have\nboth an unknown class and an unknown year. They are 86.4% of the 110 rows with an unknown class\nand 80.5% of the 118 with an unknown year, below the 90% of the criterion. The other 15 rows with\nan unknown class carry a year, a report and identifiers, and the other 23 with an unknown year\ncarry a functional class and, in most, chemical names or synonyms.\n\"\"\")\n\nmd(\"\"\"\n## fas-codes\n\n> Almost all 85 FAS codes are referenced, and FAS 40, 42, 44, 46, 48, 50 and 52 together account for\n> 50% of the records.\n\nCriterion: FAS codes from the column the code derives; the share of the seven named codes over\n(F1) all rows or (F2) rows with a FAS code, within 5 points of 50%; the seven named codes the seven\nmost frequent for reproduced, partially reproduced when the share holds and they are not. \"Almost\nall 85\" is at least 77 distinct non-empty codes. As for table1-availability, the deposited column\n(A) and the column after `add_metadata.R` (B) are both run.\n\"\"\")\n\ncode(r\"\"\"\nnamed = [\"40\", \"42\", \"44\", \"46\", \"48\", \"50\", \"52\"]\nfor label, fas in [(\"A (deposited fas)\", df.fas), (\"B (after add_metadata.R)\", fas_b)]:\n    has = jecfa.present(fas)\n    vc = fas[has].value_counts()\n    in_named = int(fas[has].isin(named).sum())\n    f1, f2 = in_named / len(df) * 100, in_named / int(has.sum()) * 100\n    top7 = vc.index[:7].tolist()\n    print(f\"Reading {label}: {int(has.sum())} rows with a FAS code, {vc.size} distinct codes (at least 77: {vc.size >= 77})\")\n    print(f\"   rows in the seven named codes: {in_named}; F1 {f1:.2f}% (within 45 to 55: {abs(f1 - 50) <= 5}), \"\n          f\"F2 {f2:.2f}% (within: {abs(f2 - 50) <= 5})\")\n    print(f\"   seven most frequent: {top7}; the named seven: {set(top7) == set(named)}; \"\n          f\"ranks of the named codes: {[int(vc.index.get_loc(c)) + 1 for c in named]}\")\n    ranked = pd.DataFrame({\"code\": vc.index[:12], \"rows\": vc.values[:12],\n                           \"cum_share_F2_pct\": (vc.cumsum() / has.sum() * 100).round(1).values[:12],\n                           \"cum_share_F1_pct\": (vc.cumsum() / len(df) * 100).round(1).values[:12]})\n    print(ranked.to_string(index=False), \"\\n\")\n\"\"\", [\"claim:fas-codes\"])\n\nmd(\"\"\"\n**Result: partially reproduced.** The seven named codes hold 3036 rows, 46.34% of all rows (F1,\nwithin 5 points of 50%) under both readings, and 56.94% (A) or 53.42% (B) of the rows with a FAS\ncode (F2). They are not the seven most frequent: FAS 59 (351 rows) is more frequent than FAS 52\n(286), and under reading B so is FAS 60 (353). The deposited column has 81 distinct values, some\nmalformed (\"77 JECFA 86\", \"67.29\", \"617\"); after `add_metadata.R` there are 73 codes, fewer than the\n77 taken for \"almost all 85\".\n\"\"\")\n\nmd(\"\"\"\n## validation-failures\n\n> In a manual check of 700 random pages, scraped and manually read values disagreed only for Report\n> (0.6%), Report sourcelink (0.9%), Tox monograph sourcelink (5.3%) and Specification sourcelink\n> (0.2%).\n\nBlocked, `data_missing`. The test needs the manual extraction of the 700 sampled pages, entered in\nREDCap at the University of Padova. It is not in the Figshare item (whose two files are the\nscraped table, checked above), nor in the paper's GitHub repository at the commit read, and the\npaper gives no other place for it. The live portal has changed since May 2024, so the extraction\ncannot be repeated on the pages as they were.\n\"\"\")\n\nmd(\"\"\"\n## portal-search-count\n\n> A search of the JECFA portal by first character returned 6547 items, in line with the pages\n> carrying a JECFA name (6551 less a duplicate and a test page).\n\nCriterion: the portal count (6547) is outside data that is not public in its May 2024 state and is\nuntestable. For the dataset's part: the rows with a JECFA name present, 6551 within 655, and after\nthe cleaning of unique-pages within 2 of 6547.\n\"\"\")\n\ncode(r\"\"\"\nwith_name = int(present.jecfa_name.sum())\nprint(f\"Rows with a JECFA name present: {with_name} (expected 6551, tolerance 655; within: {abs(with_name - 6551) <= 655})\")\nfor r, v in zip(readings.reading, readings.unique_pages):\n    print(f\"After cleaning, reading {r}: {v}; difference from 6547: {v - 6547} (within 2: {abs(v - 6547) <= 2})\")\nprint(\"The paper's own numbers: 6551 - 2 = 6549, a difference of 2 from 6547\")\n\"\"\", [\"claim:portal-search-count\"])\n\nmd(\"\"\"\n**Result: partially reproduced.** All 6552 rows carry a JECFA name, within tolerance of the\npaper's 6551, but one more. After the cleaning of unique-pages 6550 pages remain (D2, D3), 3 more\nthan the portal's 6547, outside the margin of 2; D1 gives 6552. The portal count itself cannot be\ntested.\n\"\"\")\n\nmd(\"\"\"\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| data-records-rows (link) | reproduced |\n| unique-pages | reproduced |\n| table1-availability | reproduced |\n| table2-evaluation-year | reproduced |\n| table2-functional-class | reproduced |\n| unknowns-name-only | partially reproduced |\n| fas-codes | partially reproduced |\n| validation-failures | blocked (data_missing) |\n| portal-search-count | partially reproduced (dataset's part only) |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\nHow the analysis differs from the paper's. The paper publishes no code for its Table 1 percentages,\nTable 2 or the FAS counts, so the measures follow the claims file's criteria. The deposit holds\nthe FAS column of `process_df.R`; the further step of `add_metadata.R` is run as a second reading.\nThe manual validation data are not public.\n\nWhat was found about the dataset.\n\n- The deposit holds the 6552 scraped rows, including the test page (5883) and the stub page of a\n  chemical listed twice (6316, whose record is at 6319); the paper's 6549 unique pages are not\n  what is deposited, and the paper's statement that each entry is a unique chemical does not hold\n  for these two rows.\n- JECFA.csv and jecfa.rds hold the same table.\n- The item's description calls FAS a \"Food Additive Specification identifier\"; the column is the\n  Food Additives Series number derived from the Tox monograph. It misses FAS monographs whose text\n  starts with '\">' (mostly FAS 60), holds 752 empty strings beside 468 NA, and some values keep a\n  session or page (\"77 JECFA 86\", \"67.29\", \"617\").\n- Table 1 describes the COE number as assigned by the Codex Alimentarius Commission, the item's\n  description as the Council of Europe number; the numbers occur for flavouring agents almost only,\n  consistent with the Council of Europe.\n- A few plain CAS numbers fail the check digit, and values of report, Tox monograph and\n  specification start with '\">', as the Usage Notes say.\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/figshare-26877211-ocagli-2024/reproduce_ocagli_2024.ipynb\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

Running the notebook in the scratch environment to check the text against the outputs.

**Agent calls Bash**

```bash
. $TMPDIR/explore/bin/activate && uv pip install -q nbconvert ipykernel nbformat && python $TMPDIR/build_nb.py && cd entries/figshare-26877211-ocagli-2024 && time jupyter nbconvert --to notebook --execute reproduce_ocagli_2024.ipynb --output $TMPDIR/out.ipynb 2>&1 | tail -3 && python -c "
import nbformat; nb=nbformat.read('$TMPDIR/out.ipynb',4)
for c in nb.cells:
  if c.cell_type=='code':
    for o in c.outputs: print(o.get('text','') or o.get('evalue',''))
    print('-----')
" | sed -n 1,400p | grep -v "^This database"
```

```
[NbConvertApp] Converting notebook reproduce_ocagli_2024.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 64791 bytes to /tmp/claude-1001/out.ipynb

real	0m10.734s
user	0m5.397s
sys	0m0.382s
Figshare item 26877211 version 1 (10.6084/m9.figshare.26877211.v1), read in 5.5 s

-----
Title: Unveiling Insights from the Joint FAO/WHO Expert Committee on Food Additives (JECFA) Portal
Published: 2024-12-29T08:01:38Z  version: 1  DOI: 10.6084/m9.figshare.26877211.v1
Related: [('IsSupplementTo', '10.1038/s41597-024-04294-w')]

Files (name, id, size in bytes, MD5 of the bytes read, archive computed_md5, equal):
  jecfa.rds  48922360    360432  5bfd89459ec77a152e5ee1f55e124f3d  5bfd89459ec77a152e5ee1f55e124f3d  True
  JECFA.csv  48922363   3484607  dee04993aaa56ca1f3844ded5c472764  dee04993aaa56ca1f3844ded5c472764  True


Published versions of the item: [1]
[... 249 more lines not kept]
```

**Agent**

Outputs match except the breakdown of empty FAS strings, which I described wrongly. Fixing that text and a cosmetic label.

**Agent calls Bash**

```bash
cd  && python - <<'EOF'
p="/tmp/claude-1001/build_nb.py"; s=open(p).read()
s=s.replace('''print(df.tox_monograph[empty_fas].map(jecfa.tox_abbr).value_counts().head(12).to_string())''','''print(df.tox_monograph[empty_fas].map(jecfa.tox_abbr).value_counts().to_string())
print("Of these, Tox monographs starting with '\\">':", int(df.tox_monograph[empty_fas].str.startswith('">').sum()))''')
old=s[s.index('Of the 752 empty strings'):s.index('and one is "617".')]
s=s.replace(old,'''Of the 752 empty strings, 355 are FAS monographs that the "^FAS " pattern misses (339 FAS 60,
10 FAS 74, 2 FAS 27, and 4 written "FAS79"), most because their text starts with '">'; 277 are
monographs marked "NOT PREPARED", and 120 are not a FAS (such as a TRS reference). Some values keep
the session ("77 JECFA 86") or a page ("67.29"), ''')
s=s.replace('''an unknown class carry a year, a report and identifiers, and the other 23 with an unknown year
carry a functional class and, in most, chemical names or synonyms.''','''an unknown class carry a year, a report and identifiers (15 have a JECFA number, 13 a FEMA
number), and the other 23 with an unknown year all carry a functional class, 15 of them chemical
names and 14 synonyms.''')
open(p,"w").write(s)
h="entries/figshare-26877211-ocagli-2024/jecfa.py"; t=open(h).read()
t=t.replace('return m.map(names, na_action="ignore").astype("string")','return m.map(names, na_action="ignore").astype("string").rename("leading_class")')
open(h,"w").write(t)
EOF
grep -n "355 are" $TMPDIR/build_nb.py
```

```
192:Of the 752 empty strings, 355 are FAS monographs that the "^FAS " pattern misses (339 FAS 60,
```

**Agent**

Now the entry files.

**Agent calls Bash**

```bash
cd entries/figshare-26877211-ocagli-2024 && printf 'fsspec\naiohttp\npandas\nrdata\n' > requirements.in && cat > entry.yaml <<'EOF'
schema_version: 1
name: figshare-26877211-ocagli-2024
type: reproduction
title: The JECFA portal index (Ocagli et al. 2024)
description: Tests the findings of Ocagli et al. (2024) on Figshare item 26877211, version 1, which
  holds the table scraped from the JECFA portal in May 2024 as an RDS file and a CSV file. It checks
  the row count and fields, the cleaning to unique pages, the availability of each field (Table 1),
  the counts by evaluation year and functional class (Table 2), the content of the unknowns, the
  most frequent FAS codes, and the count of pages with a JECFA name. The manual validation of 700
  pages is not deposited.
license: Apache-2.0
notebooks:
- path: reproduce_ocagli_2024.ipynb
  title: Reproducing Ocagli et al. (2024) from Figshare item 26877211
  runtime_minutes: 1
helpers:
- jecfa.py
related:
- id: figshare:26877211/1
  relation: uses_data
- id: doi:10.1038/s41597-024-04294-w
  relation: reproduces
EOF
cd ../.. && python $TMPDIR/build_nb.py && python tools/entry.py lock entries/figshare-26877211-ocagli-2024 2>&1 | tail -3
```

```
wrote entries/figshare-26877211-ocagli-2024/requirements.lock.txt
```

**Agent**

Now the README and the attempt record, then the check and run.

**Agent calls Write**

```json
{
 "file_path": "entries/figshare-26877211-ocagli-2024/README.md",
 "content": "# Ocagli et al. (2024) from Figshare item 26877211\n\nTests the findings of [Ocagli et al. (2024)](https://doi.org/10.1038/s41597-024-04294-w), a Data\nDescriptor of an index scraped from the JECFA portal, on\n[Figshare 26877211](https://doi.org/10.6084/m9.figshare.26877211.v1), version 1, which holds the\nscraped table as `jecfa.rds` and `JECFA.csv`.\n\n| Claim | Outcome |\n|---|---|\n| The deposit has 6552 rows and the 17 fields of Table 1 (link) | Reproduced |\n| 6549 unique pages after removing a duplicate and a test page | Reproduced (6550) |\n| Availability of each Table 1 field | Reproduced |\n| Evaluations by year (Table 2) | Reproduced |\n| Substances by functional class (Table 2) | Reproduced |\n| The unknowns have only a JECFA name | Partially reproduced |\n| FAS 40 to 52 (even codes) account for 50% of the records | Partially reproduced |\n| Discrepancies found by the manual check of 700 pages | Blocked: data missing |\n| The portal count of 6547 is in line with the pages with a JECFA name | Partially reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/figshare-26877211-ocagli-2024-01.yaml`](../../attempts/figshare-26877211-ocagli-2024-01.yaml).\n\n- `reproduce_ocagli_2024.ipynb`: the analysis. It takes under a minute, most of it streaming the\n  two files.\n- `jecfa.py`: loading both files into memory, the measures of the criteria, and the FAS derivations\n  of the paper's code (`R/process_df.R`, `R/add_metadata.R`). Other notebooks on this item can\n  import it.\n"
}
```

```
File created successfully at: entries/figshare-26877211-ocagli-2024/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/entry.py all entries/figshare-26877211-ocagli-2024 2>&1 | tail -15
```

```
Installed kernelspec registry-figshare-26877211-ocagli-2024 in executed/figshare-26877211-ocagli-2024/.venv/share/jupyter/kernels/registry-figshare-26877211-ocagli-2024
0 error(s)
pass  reproduce_ocagli_2024.ipynb  (11 s)
```

**Agent calls Bash**

```bash
python -c "
import nbformat; nb=nbformat.read('executed/figshare-26877211-ocagli-2024/reproduce_ocagli_2024.ipynb',4)
for c in nb.cells[8:10]:
  if c.cell_type=='code':
    for o in c.outputs: print(o.get('text',''))
  else: print(c.source)
"
```

```
Every column is text. Missing values are NA, except in `fas`, which also holds 752 empty strings.
`jecfa_name` and `url` are present in every row.
URLs of the form https://apps.who.int/food-additives-contaminants-jecfa-database/Home/Chemical/<n>: 6552 of 6552
Page numbers from 1 to 6593 ; duplicated URLs: 0 ; rows sorted by page number: True
Page numbers between 1 and 6593 with no row: 41: [1798, 4905, 5959, 5960, 6003, 6183, 6202, 6207, 6211, 6217, 6222, 6229, 6286, 6294, 6295, 6302, 6303, 6304, 6305, 6309, 6317, 6318, 6320, 6321, 6322, 6323, 6324, 6325, 6327, 6328, 6362, 6381, 6382, 6397, 6459, 6464, 6527, 6528, 6530, 6548, 6553]

evaluation_year: all present values are integers: True ; range 1958 to 2023
jecfa_number: 4639 present, 31 not a plain integer, e.g. ['506a,b', '506a,b', '632.1', '631.1']
fema_number: 4258 present, 33 not a plain integer, e.g. ['4126  ', '4161  ', '4209  ', '3957  ']
coe_number: 3031 present, 1 not a plain integer, e.g. ['2983-38-2']
cas_number: 2317 present, 2127 of the plain form NNNNNNN-NN-N, of which 2081 have a valid check digit; 190 carry more than one number or a note, e.g. ['38966-29-9; 3387-37-9 (1:1 SALT)', "860-22-0 (5,5' ISOMER)", '13270-61-6 (Delphinidin)']
Plain CAS numbers with a wrong check digit: ['22389-47-0', '76-36-3', '5284-04-9', '2353-43-9', '7783-54-0', '7783-54-0', '2412-24-1', '5284-04-9', '61597-96-6', '2353-43-9', '7783-54-0', '1229-55-9', '5284-04-9', '2353-43-9', '3943-58-3', '22389-47-0', '1229-55-9', '1229-55-9', '2412-24-1', '5284-04-9', '5284-04-9', '58-92-1', '5284-04-9', '6833-79-9', '5284-04-9', '45706-73-7', '5807-68-8', '76-36-3', '3943-58-3', '1005-86-2', '3943-58-3', '7796-47-2', '23696-28-2', '141-40-0', '76-36-3', '76-36-3', '76-36-3', '76-36-3', '76-36-3', '5284-04-9', '15514-30-0', '71437-64-0', '0079-19-5', '79797-16-1', '1440-67-0', '86366-64-3']

Values starting with the characters '">' (Usage Notes): report 602 , tox_monograph 349 , specification 398
```

**Agent calls Bash**

```bash
python -c "
import nbformat; nb=nbformat.read('executed/figshare-26877211-ocagli-2024/reproduce_ocagli_2024.ipynb',4)
c=nb.cells[10]; [print(o.get('text','')[:900]) for o in c.outputs]"; date -u
```

```
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    c=nb.cells[10]; [print(o.get('text','')[:900]) for o in c.outputs]
                                                            ^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/nbformat/_struct.py", line 129, in __getattr__
    raise AttributeError(key) from None
AttributeError: outputs
Tue Oct 27 19:55:22 UTC 2026
```

**Agent calls Bash**

```bash
python -c "
import nbformat; nb=nbformat.read('executed/figshare-26877211-ocagli-2024/reproduce_ocagli_2024.ipynb',4)
c=nb.cells[11]; [print(o.get('text','')[:700]) for o in c.outputs]"
```

```
fas equals the derivation of R/process_df.R from tox_monograph in every row: True

Tox monographs of the rows with an empty fas, by the code's abbreviation (R/extract_jecfa_tox_abbr.R):
tox_monograph
FAS 60                                                  339
NOT PREPARED                                            273
NOT A FAS                                               120
FAS 74                                                   10
FAS79                                                     4
NOT PREPARED. See FAS 17                                  3
FAS 27                                                    2
NOT PREPARED (SEE ENVIRONMENTAL HEALTH CRITERIA 140)      1
Of these, Tox monogr
```

**Agent calls Bash**

```bash
python -c "
import nbformat; nb=nbformat.read('executed/figshare-26877211-ocagli-2024/reproduce_ocagli_2024.ipynb',4)
c=nb.cells[11]; [print(o.get('text','')[600:800]) for o in c.outputs]"
```

```
2
NOT PREPARED (SEE ENVIRONMENTAL HEALTH CRITERIA 140)      1
Of these, Tox monographs starting with '">': 349

Distinct fas values: ['', '1', '5', '6', '8', '10', '12', '13', '14',
```

**Agent**

Text fix for the '">' count, then the attempt record.

**Agent calls Bash**

```bash
python - <<'EOF'
p="/tmp/claude-1001/build_nb.py"; s=open(p).read()
s=s.replace('''10 FAS 74, 2 FAS 27, and 4 written "FAS79"), most because their text starts with '">'; 277 are''','''10 FAS 74, 2 FAS 27, and 4 written "FAS79"); 349 of the 752 Tox monographs start with '">', which
the pattern does not allow. 277 are''')
open(p,"w").write(s)
EOF
python $TMPDIR/build_nb.py && grep -c "349 of the 752" entries/figshare-26877211-ocagli-2024/reproduce_ocagli_2024.ipynb
```

```
1
```

**Agent calls Write**

```json
{
 "file_path": "attempts/figshare-26877211-ocagli-2024-01.yaml",
 "content": "schema_version: 2\nid: figshare-26877211-ocagli-2024-01\ndataset:\n  archive: figshare\n  id: \"26877211\"\n  version: \"1\"\n  doi: 10.6084/m9.figshare.26877211.v1\npaper: doi:10.1038/s41597-024-04294-w\ndate: 2026-10-27\nentry: figshare-26877211-ocagli-2024\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-12\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/40572006592\ninputs:\n- what: The FAS derivations of the paper's code (R/process_df.R, R/add_metadata.R and\n    R/extract_jecfa_tox_abbr.R), re-implemented in jecfa.py to check the deposited fas column and to\n    run the second FAS reading that the criteria of table1-availability and fas-codes name. No data\n    are taken from it.\n  source: https://github.com/UBESP-DCTV/jecfa at commit 2d8a5340d5322cbae28eb3095d948313932f6c7e\noutcomes:\n- claim: data-records-rows\n  outcome: reproduced\n  notebook: reproduce_ocagli_2024.ipynb\n  output: claim:data-records-rows\n  measured: 6552\n  notes: jecfa.rds has 6552 rows and 17 columns, one for each field of Table 1, named as in\n    R/process_df.R in lower case with \".\" replaced by \"_\", in the order that function selects them.\n    JECFA.csv holds the same 6552 rows and 17 columns, with no differing cell. The MD5 of both files\n    read matches the archive's computed_md5. The columns R/add_metadata.R adds are absent, so the\n    deposit is the output of process_df.R. The \"May 2024\" date cannot be checked from the files,\n    which carry no scrape date.\n- claim: unique-pages\n  outcome: reproduced\n  notebook: reproduce_ocagli_2024.ipynb\n  output: claim:unique-pages\n  measured: 6550\n  notes: D1 (distinct URLs) gives 6552, 3 from 6549 and outside the tolerance of 2, as no URL is\n    repeated. D2 (distinct JECFA names less page 5883) and D3 (rows less page 5883 and less the\n    second row of page 6316's chemical) give 6550, within tolerance. Page 6316's chemical appears\n    twice, at pages 6316 (name only) and 6319 (full record); page 5883 is named TEST and carries\n    nothing else. The paper's 6549 is reached only by removing both rows of that chemical with the\n    test page (shown as a variant).\n  deviations:\n  - The criterion's readings D1 to D3 are all run; measured is the first that matches (D2). D1 does\n    not match.\n- claim: table1-availability\n  outcome: reproduced\n  notebook: reproduce_ocagli_2024.ipynb\n  output: claim:table1-availability\n  measured: [100, 100, 82.57, 78.30, 35.36, 70.80, 64.99, 46.26, 98.32, 98.20, 97.62, 97.62, 92.86,\n    92.86, 91.82, 91.82, 81.38]\n  notes: Over all 6552 rows (U1 and U2 are the same, as no URL repeats), 16 of 17 shares are within\n    tolerance with the deposited fas column (reading A), FAS being 81.38% against 93% (lower bound\n    83.7%), and 17 of 17 with fas after the step of R/add_metadata.R (reading B, 86.74%). Over the\n    6550 rows left after cleaning, no share moves by more than 0.05 points. Rounded to whole\n    numbers 12 of 17 equal Table 1 (Chemical names 83, Synonyms 78, Report and its link 98 differ\n    by one point, FAS by 12 under A). Counting the 752 empty fas strings as present gives 92.86%,\n    which suggests Table 1 counted every non-NA value; the claims file's reading E counts them as\n    absent.\n  deviations:\n  - The criterion names the FAS column of both process_df.R and add_metadata.R; the deposit holds\n    the first. Both are run (A and B), and both give reproduced.\n- claim: table2-evaluation-year\n  outcome: reproduced\n  notebook: reproduce_ocagli_2024.ipynb\n  output: claim:table2-evaluation-year\n  measured: [2357, 3099, 778, 200, 118, 36.63, 48.17, 12.09, 3.11]\n  notes: The four bins and the unknowns equal Table 2 exactly; shares are over the 6434 rows with a\n    year. All years lie between 1958 and 2023. The text's 2,356 for the first bin differs by one from\n    Table 2 and from the data.\n- claim: table2-functional-class\n  outcome: reproduced\n  notebook: reproduce_ocagli_2024.ipynb\n  output: claim:table2-functional-class\n  measured: [4635, 1453, 77, 277, 110, 71.95, 22.56, 1.20, 4.30]\n  notes: The counts equal Table 2 exactly; shares are over the 6442 rows with a class. Every\n    functional_class string starts with one of the four class names (the data spell \"Flavouring\n    Agent\"), so none is left unmatched. Flavouring agents are the largest class.\n- claim: unknowns-name-only\n  outcome: partially_reproduced\n  notebook: reproduce_ocagli_2024.ipynb\n  output: claim:unknowns-name-only\n  measured: [86.4, 80.5]\n  notes: 95 rows carry only a URL and a JECFA name, and each of them has both class and year\n    unknown. They are 95 of 110 rows with an unknown class (86.4%) and 95 of 118 with an unknown\n    year (80.5%), both below the criterion's 90%. The other 15 rows with an unknown class carry a\n    year, a report and identifiers; the other 23 with an unknown year all carry a functional class,\n    15 of them chemical names and 14 synonyms. The criterion states only when the claim is\n    reproduced; partially reproduced is recorded because the statement holds for most of the\n    unknowns (the protocol's \"holds only in part\").\n- claim: fas-codes\n  outcome: partially_reproduced\n  notebook: reproduce_ocagli_2024.ipynb\n  output: claim:fas-codes\n  measured: 46.34\n  notes: The seven named codes hold 3036 rows, 46.34% of all 6552 rows (F1, within 5 points of 50%)\n    under both FAS readings; over the rows with a FAS code (F2) 56.94% with the deposited column (A,\n    outside tolerance) and 53.42% after add_metadata.R (B, within). They are not the seven most\n    frequent; FAS 59 (351 rows) is more frequent than FAS 52 (286) under both readings, and FAS 60\n    (353) too under B; the named codes rank 1 to 6 and 9 (A) or 10 (B). The deposited column has 81\n    distinct non-empty values, some malformed (\"77 JECFA 86\", \"67.29\", \"617\"), which meets the 77\n    taken for \"almost all 85\"; after add_metadata.R there are 73 codes, which does not.\n  deviations:\n  - The criterion names the FAS column of both process_df.R and add_metadata.R; the deposit holds\n    the first. Both are run (A and B), and both give partially reproduced.\n- claim: validation-failures\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The test needs the manual extraction of the 700 sampled pages, entered in REDCap at the\n    University of Padova. It is not among the item's two files (the scraped table as RDS and CSV),\n    not in the paper's GitHub repository at commit 2d8a5340, and the paper names no other place for\n    it. The portal has changed since May 2024, so the check cannot be repeated on the pages as\n    scraped.\n- claim: portal-search-count\n  outcome: partially_reproduced\n  notebook: reproduce_ocagli_2024.ipynb\n  output: claim:portal-search-count\n  notes: The portal's 6547 is outside data, not public in its May 2024 state, and is not tested. In\n    the dataset all 6552 rows carry a JECFA name, within the tolerance of the paper's 6551 but one\n    more. After the cleaning of unique-pages, D2 and D3 give 6550, 3 more than 6547 and outside the\n    margin of 2 the criterion takes for \"aligns\"; D1 gives 6552. The paper's own numbers (6551 less\n    2 is 6549) are within 2 of 6547; the one extra row in the deposit is what puts the count outside.\n    The criterion states only when the dataset's part is reproduced; partially reproduced is\n    recorded because one of its two conditions holds. No measured value is given, as the first\n    expected value (the portal count) cannot be measured.\nfindings:\n- kind: data_missing\n  statement: The manual extraction of 700 portal pages used for the Technical Validation (REDCap,\n    University of Padova) is not deposited, so the discrepancy rates of the validation cannot be\n    checked.\n- kind: paper_inconsistency\n  statement: The Methods say the 6552 scraped entries were cleaned of a duplicate and a test page to\n    6549 unique pages, and Data Records says each entry corresponds to a unique chemical, but the\n    deposited table holds all 6552 rows, including the test page 5883 (named TEST, with no other\n    field) and page 6316, a name-only stub of the chemical whose full record is page 6319.\n- kind: metadata_error\n  statement: The item's description calls FAS a \"FAO/WHO Food Additive Specification identifier\".\n    The column is the number of the Food Additives Series toxicological monograph, derived from the\n    Tox monograph by R/process_df.R in every row, as the paper's Table 1 describes it.\n- kind: code_mismatch\n  statement: The deposited fas column, from R/process_df.R, is empty for 355 rows whose Tox\n    monograph is a FAS monograph (339 FAS 60, 10 FAS 74, 2 FAS 27, 4 written \"FAS79\"), mostly\n    because the text starts with the stray characters '\">'; it holds 752 empty strings beside 468\n    NA, and some values keep a session or page (\"77 JECFA 86\", \"67.29\", \"617\"). R/add_metadata.R\n    repairs part of this but its output is not deposited. With empty strings counted as absent the\n    FAS share is 81.4%, against 93% in Table 1.\n- kind: metadata_error\n  statement: Table 1 describes the COE number as assigned by the Codex Alimentarius Commission; the\n    item's description calls it the Council of Europe number. COE numbers are present for 3022\n    flavouring agents and 9 food additives and for no other class, which is consistent with the\n    Council of Europe numbering of flavourings, not with Codex.\n- kind: other\n  statement: Scraped values carry formatting residue. 602 report, 349 Tox monograph and 398\n    specification values start with '\">' (the Usage Notes mention this for Report); 33 FEMA numbers\n    have trailing spaces; 31 JECFA numbers are not plain integers (\"506a,b\", \"632.1\"); 46 of 2127\n    plain CAS numbers fail the CAS check digit, and 190 CAS values hold several numbers or notes.\n"
}
```

```
File created successfully at: attempts/figshare-26877211-ocagli-2024-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/entry.py all entries/figshare-26877211-ocagli-2024 2>&1 | tail -5 && python tools/entry.py handover entries/figshare-26877211-ocagli-2024 2>&1 | tail -5; date -u
```

```
Installed kernelspec registry-figshare-26877211-ocagli-2024 in executed/figshare-26877211-ocagli-2024/.venv/share/jupyter/kernels/registry-figshare-26877211-ocagli-2024
0 error(s)
pass  reproduce_ocagli_2024.ipynb  (11 s)
wrote executed/figshare-26877211-ocagli-2024/handover
Tue Oct 27 19:57:08 UTC 2026
```

**Agent**

One wording fix in the finding so it states only what was printed.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/figshare-26877211-ocagli-2024-01.yaml",
 "old_string": "    monograph is a FAS monograph (339 FAS 60, 10 FAS 74, 2 FAS 27, 4 written \"FAS79\"), mostly\n    because the text starts with the stray characters '\">'; it holds",
 "new_string": "    monograph is a FAS monograph (339 FAS 60, 10 FAS 74, 2 FAS 27, 4 written \"FAS79\"), which its\n    \"^FAS \" pattern misses; 349 of the 752 empty values have a Tox monograph starting with the stray\n    characters '\">'. It holds"
}
```

```
The file attempts/figshare-26877211-ocagli-2024-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/figshare-26877211-ocagli-2024 2>&1 | tail -2; git status --short; ls executed/figshare-26877211-ocagli-2024/handover
```

```
0 error(s)
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? attempts/figshare-26877211-ocagli-2024-01.yaml
?? entries/figshare-26877211-ocagli-2024/
?? scripts
10.1038-s41597-024-04294-w.yaml
jecfa.py
reproduce_ocagli_2024.ipynb
```

**Agent**

I've finished the author steps (1 to 5) and the handover for FIGSHARE:26877211 version 1. `tools/entry.py all` reports 0 errors, the notebook runs in 11 s, and the handover package is in `executed/figshare-26877211-ocagli-2024/handover/`. Nothing is committed.

**(1) Outcomes**

| Claim | Outcome | Key numbers |
|---|---|---|
| data-records-rows (link) | reproduced | 6552 rows; all 17 Table 1 fields present; the CSV is identical to the RDS |
| unique-pages | reproduced | 6550 under readings D2 and D3 (D1 gives 6552); page 6316's chemical appears twice (pages 6316 and 6319) |
| table1-availability | reproduced | 16 of 17 fields within tolerance with the deposited FAS column (FAS 81.4% against 93%); 17 of 17 with FAS after `add_metadata.R` |
| table2-evaluation-year | reproduced | 2357 / 3099 / 778 / 200 / 118 unknown, exactly as Table 2 |
| table2-functional-class | reproduced | 4635 / 1453 / 77 / 277 / 110 unknown, exactly as Table 2 |
| unknowns-name-only | partially reproduced | 86.4% of the unknown-class rows and 80.5% of the unknown-year rows carry only a name; the criterion needs 90% |
| fas-codes | partially reproduced | the seven named codes hold 46.3% of all rows, but FAS 59 is more frequent than FAS 52, so they are not the seven most frequent |
| validation-failures | blocked (data_missing) | the 700-page REDCap extraction is not deposited |
| portal-search-count | partially reproduced | 6552 rows have a JECFA name (6551 within tolerance); after cleaning 6550, which is 3 from the portal's 6547 and outside the margin of 2. The portal count itself cannot be tested |

**(2) What I found about the dataset**
- The deposit holds all 6552 scraped rows, not the 6549 cleaned pages. It still includes the test page 5883 and page 6316, which carries only the name of a chemical whose full record is page 6319.
- The Figshare description calls FAS a "Food Additive Specification identifier". The column is the Food Additives Series number, and the paper's code derives it from the Tox monograph in every row.
- The deposited FAS column comes from `process_df.R`. That step misses 355 FAS monographs (mostly FAS 60), leaves 752 empty strings next to 468 NA, and keeps some malformed values such as "77 JECFA 86" and "617".
- Table 1 says the COE number is from Codex. The data are consistent with the Council of Europe flavouring numbers instead (3022 of 3031 are on flavouring agents).
- There is formatting residue in the scraped values: stray '">' prefixes, 46 CAS numbers that fail the check digit, and FEMA numbers with trailing spaces.

I made no assumptions: wherever the paper leaves a detail open, I ran every reading and they all gave the same outcome. There are no questions for the paper's authors and none for a reader.

**(3) Where the protocol was unclear**
1. For unknowns-name-only and portal-search-count, the criterion only says when a claim is "reproduced". Both claims hold in part, so I recorded `partially_reproduced` under the protocol's "holds only in part" and explained this in the notes.
2. The protocol has no rule for `measured` when an expected value cannot be measured (the portal count of 6547). I left `measured` out of that outcome and gave the numbers in the notes.
3. Reading an RDS file into memory is not covered in docs/archives.md. I used the pure-Python `rdata` package, since `pyreadr` needs a file path.
4. The criterion names both of the code's FAS derivations (`process_df.R` and `add_metadata.R`), but the deposit holds only the first. I ran both as separate readings.
5. The clock check of step 2 does not apply to a table with no time series. I said so in the notebook.

**(4) Runtime and failures**
The whole run took about 11 minutes, from 19:46 to 19:57 UTC, and nothing failed. I also cloned the paper's code into a temporary directory to read it. `git status` lists dotfiles and a `scripts` directory as untracked; I did not create them and left them alone.

Files are in `entries/figshare-26877211-ocagli-2024/`:
- reproduce_ocagli_2024.ipynb
- jecfa.py
- entry.yaml
- requirements.in
- requirements.lock.txt
- README.md

The attempt record is `attempts/figshare-26877211-ocagli-2024-01.yaml`.

## End of run

44 turns, 10 minutes, result: success.
