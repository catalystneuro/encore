# allen-2026 · claims · run 45687937389

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-19`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 180 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
cat papers/datasets/allen-2026.yaml 2>/dev/null; ls datasets 2>/dev/null | grep -i rjdfn; grep -rl rjdfn2zqz --include=*.yaml . | head; wc -c paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/match/dryad-rjdfn2zqz.yaml; grep -n -A15 rjdfn2zqz papers/manifest.yaml | head -40
```

```
# Whether each paper Dryad:rjdfn2zqz names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dryad
  id: rjdfn2zqz
date: '2026-11-25'
papers:
- doi: 10.1038/s42003-025-09506-6
  relation: primary_article
  checks:
    text: true
    title_in_text: true
    names_this: true
    names_others: []
  verdict: primary
  by: checks
  reason: The paper names Dryad:rjdfn2zqz and no other dataset.
3338:  dryad-rjdfn2zqz:
3339-  - doi: 10.1038/s42003-025-09506-6
3340-    status: stored
[... 13 more lines not kept]
```

**Agent**

Now reading the paper text in full.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s42003-025-09506-6.txt",
 "offset": 30,
 "limit": 500
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s42003-025-09506-6.txt",
 "offset": 530,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i -E "data availability|code availability|github|dryad|supplementary table [1-5]|=== page|supplement" paper/10.1038-s42003-025-09506-6.txt | sed -n '1,200p' | awk -F: '$1>1129'
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s42003-025-09506-6.txt",
 "offset": 1129,
 "limit": 40
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s42003-025-09506-6.txt",
 "offset": 1650,
 "limit": 650
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -rn -l "rjdfn2zqz" --include=*.{yaml,json,md} . 2>/dev/null | grep -v "^./claims" | head; grep -rn -B2 -A12 "rjdfn2zqz" targets* 2>/dev/null | head -40
```

```
./targets/dryad.json
./papers/match/dryad-rjdfn2zqz.yaml
./papers/manifest.yaml
./papers/datasets/allen-2026.yaml
targets/dryad.json-861-  },
targets/dryad.json-862-  {
targets/dryad.json:863:   "id": "rjdfn2zqz",
targets/dryad.json-864-   "name": "Physiological and behavioral dataset of squid exposed to ocean acidification",
targets/dryad.json:865:   "url": "https://datadryad.org/dataset/doi:10.5061/dryad.rjdfn2zqz",
targets/dryad.json:866:   "doi": "10.5061/dryad.rjdfn2zqz",
targets/dryad.json-867-   "published_version": "439366",
targets/dryad.json-868-   "version_number": 6,
targets/dryad.json-869-   "published": "2026-04-29",
targets/dryad.json-870-   "license": "https://spdx.org/licenses/CC0-1.0.html",
targets/dryad.json-871-   "asset_count": 12,
targets/dryad.json-872-   "size_gb": 0.3165,
targets/dryad.json-873-   "data_standards": [
targets/dryad.json-874-    "CSV",
targets/dryad.json-875-    "zip"
targets/dryad.json-876-   ],
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dryad.json'))
t=[x for x in d if x['id']=='rjdfn2zqz'][0]
print({k:v for k,v in t.items() if k not in ('files',)})"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    t=[x for x in d if x['id']=='rjdfn2zqz'][0]
                       ~^^^^^^
TypeError: string indices must be integers, not 'str'
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dryad.json'))
L=d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list))
t=[x for x in L if x.get('id')=='rjdfn2zqz'][0]
print({k:v for k,v in t.items() if k not in ('files',)})"
```

```
{'id': 'rjdfn2zqz', 'name': 'Physiological and behavioral dataset of squid exposed to ocean acidification', 'url': 'https://datadryad.org/dataset/doi:10.5061/dryad.rjdfn2zqz', 'doi': '10.5061/dryad.rjdfn2zqz', 'published_version': '439366', 'version_number': 6, 'published': '2026-04-29', 'license': 'https://spdx.org/licenses/CC0-1.0.html', 'asset_count': 12, 'size_gb': 0.3165, 'data_standards': ['CSV', 'zip'], 'readme': True, 'code': [], 'species': [], 'approaches': [], 'keywords': ['Squids', 'Ocean acidification', 'Animal behavior'], 'papers': [{'doi': '10.1038/s42003-025-09506-6', 'title': 'Neurometabolic rewiring in squid (Sepioteuthis lessoniana) optic lobes drives behavioral plasticity and visual integration under environmental acidification', 'relation': 'primary_article', 'resource_type': 'JournalArticle', 'preprint': False}], 'catalystneuro': []}
```

**Agent calls Bash**

```bash
grep -l "archive: dryad" claims/*.yaml | head -3; f=$(grep -l "archive: dryad" claims/*.yaml | head -1); head -60 $f; grep -n "def \|argv\|kind\|data:" tools/claims_check.py | head -40
```

```
claims/dias-2025.yaml
claims/didion-gency-2024.yaml
claims/wang-2024.yaml
# Claims for Dias, Lemoine, Yanco, Zimova, Bay & Weeks (2025), Proc. R. Soc. B, on Dryad
# dataset doi:10.5061/dryad.bvq83bkk9.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record, from Europe PMC (PMC11750374, full-text XML), with the
# electronic supplementary material (rspb20242556_si_001.pdf, Tables S1 to S11 and Fig. S1). The
# extracted text drops the model equations and priors of the Methods ("Testing whether climate
# drives changes in wing length allometry", paragraphs 3 to 5); the paper's code gives them.
#
# Code read: Zenodo doi:10.5281/zenodo.14226724, Code.zip (SHA-256 cc9f58b9855aec4e3aca09be41387
# 07d07fc34739ec5762e54e1f5bca48ddbc8). It holds lm_mod.stan (the hierarchical model),
# Script01_MainAnalyses.R (Tables 1 to 3 and S1 to S3) and Script02_SupplementAnalyses.R (Tables
# S4 to S11). Its inputs are morphdata.csv, ed_FHY.csv, ed_AHYspring.csv, ed_AHYfall.csv and
# chitree.rds; the Table S8 code also reads an object envdata3 that no script defines. The
# Dryad description says the deposit holds the morphological data from the Field Museum and the
# environmental data, already scaled within species to mean 0 and s.d. 1.
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,110p tools/claims_check.py; grep -n "^dataset\|^  archive\|^  id\|^paper" claims/dias-2025.yaml
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:])"
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
grep -h -i -B1 -A1 "spread\b\|± .*SD\|SEM" claims/*.yaml | grep -i "tolerance\|spread" | head -20
```

```
Tolerances are the paper's stated spread for the rates, one 5 ms bin for the epoch 2 peak time
    shown. The SEM is the regression's standard error. The tolerance is the paper's SEM. The
    the tolerance is the paper's SEM. The ratio uses the first-ramp slope under the same reading.
    readings (e) relative to the position at t = 0; (f) the readings of fig2b-lateral-spread
- id: fig2b-lateral-spread
  - fig2a-success-rate. Lateral position relative to t = 0 was stated as fixed; the paper does not set the zero. Named it open, with the readings of fig2b-lateral-spread.
    tolerance: 0
  criterion: Tolerances are 10% of each mean; the printed SDs (0.61, 0.77, 1.25, 16.9 Hz) are the
    spread over cells, not an uncertainty of the mean, and are reported for comparison (within
    tolerance: 0.08
  criterion: Tolerances are the stated SDs, as the paper gives them as the spread of the values
    cells of each class (Table S1). The tolerance is the paper's stated spread (protocol
    deviation over cells of each class (Panel_4.ipynb, make_latex_table). The tolerance is the
    stated spread over cells. Reproduced when all six means are within tolerance; partially
    median, and the three means are within the stated spread.
    within the stated spread; the class medians, whose order may differ given the spread, are
  statement: Control mice cluster at low PC1 and PC2 scores, while PACAPko mice spread along
    fig2a-pca-components, under each of its readings. Reproduced when the spread (SD) of
    the tolerance, and the SD and SEM over mice are both reported. Reproduced when the four means
    are within tolerance and both tests give corrected p < 0.05 with W+ faster; partially
```

**Agent**

The full text, Methods and supplement are all present. Next I'll render the figure pages to read the significance letters, which the text extraction drops.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import fitz
d=fitz.open('paper/10.1038-s42003-025-09506-6.pdf')
for i in (2,7,8):
    d[i].get_pixmap(dpi=130).save(f'p{i+1}.png')
s=fitz.open('paper/10.1038-s42003-025-09506-6.supp.pdf')
for i in (0,1,2,3):
    s[i].get_pixmap(dpi=110).save(f's{i+1}.png')
print(len(d))
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent**

The Read tool can open PDF pages directly.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s42003-025-09506-6.pdf",
 "pages": "3"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s42003-025-09506-6.pdf",
 "pages": "8-9"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "import pypdf" 2>&1; python3 -c "import pdfplumber" 2>&1; which mutool gs convert pdfimages 2>&1 | head
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Bash**

```bash
pip install --quiet --target $TMPDIR/pylib pymupdf 2>&1 | tail -2; ls $TMPDIR/pylib | head
```

```
_yaml
bin
fitz
flatbuffers
flatbuffers-25.12.19.dist-info
google
networkx
networkx-3.7.dist-info
numpy
numpy-2.5.5.dist-info
```

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python3 -c "
import fitz
d=fitz.open('paper/10.1038-s42003-025-09506-6.pdf')
for i in (2,7,8):
    d[i].get_pixmap(dpi=130).save(f'p{i+1}.png')
s=fitz.open('paper/10.1038-s42003-025-09506-6.supp.pdf')
for i in (1,2,3):
    s[i].get_pixmap(dpi=100).save(f's{i+1}.png')
print(len(d))
"; ls $TMPDIR/*.png; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p3.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p8.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p9.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python3 -W ignore -c "
import fitz
d=fitz.open('paper/10.1038-s42003-025-09506-6.pdf')
for i in (6,9):
    d[i].get_pixmap(dpi=140).save(f'p{i+1}.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p7.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p10.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd paper && grep -n -E "data_GSEA|GSEA results|DET Results|did not observe changes in optic|Squids that attempted|majority of examined|ROUT|area of 0.6992" 10.1038-s42003-025-09506-6.txt
```

```
564:(Supplementary data: DET Results). The shrunken log fold change of differential expression transcripts was then ranked and utilized as the input for
568:GSEA results).
588:ROUT (Q = 1%); however, no significant outliers were detected. If residuals
597:characteristic curve, which had an underlying area of 0.6992. Other behavioral parameters were investigated using ordinary one-way ANOVAs or
705:addition, while monitoring the attempted attacks, the majority of examined
773:chronically treated squids. Squids that attempted to capture prey at least one time
972:within the central nervous system, we did not observe changes in optic lobe
978:beta-4; Supplementary data_GSEA_results). These findings support growing evidence that cholinergic systems, along with GABAergic pathways,
```

**Agent calls Write**

```json
{
 "file_path": "claims/allen-2026.yaml",
 "content": "# Claims for Allen, Yan, Kuan et al. (2026), Communications Biology 9:229, \"Neurometabolic\n# rewiring in squid (Sepioteuthis lessoniana) optic lobes drives behavioral plasticity and visual\n# integration under environmental acidification\", on Dryad dataset doi:10.5061/dryad.rjdfn2zqz.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-25,\n# protocol pilot-19 as stated in docs/protocol.md.\n#\n# Text read: the version of record (Communications Biology PDF, uploaded by Ben Dichter), its\n# extracted text with the main text, Methods, figure legends and the one supplement PDF\n# (Supplementary Figures 1 to 5 and Supplementary Tables 1 to 5). Figure pages 3, 7, 8, 9 and 10\n# of the PDF were opened only to read the significance letters of Figures 1B to 1F, 2D and 2H and\n# the axes of Figure 3C and 3D. The supplementary data files the Methods name (\"Supplementary\n# data: DET Results\" and \"GSEA results\") are not under paper/; only the claim\n# chronic-nachr-subunits-down rests on them.\n#\n# Code read: none. The paper links no code repository. Its Data availability says the\n# bioinformatics code and \"custom scripts, if any\" are in the Dryad deposit itself, which the\n# reader does not open; statistics were run in GraphPad Prism v10.2.3 and R v4.3.2 (logistic\n# regression). Where the deposit's scripts fix a detail left open here, the author may take it\n# from them, citing the file.\n#\n# The dataset. Dryad title \"Physiological and behavioral dataset of squid exposed to ocean\n# acidification\". By the paper's Data availability it holds the raw physiological data\n# (metabolic rates, ammonia excretion rates, blood acid-base parameters), the behavioral tracking\n# data, the ERG recordings, the carbonate chemistry calculations and the bioinformatics code. The\n# RNA-seq reads are in NCBI SRA BioProject PRJNA1204452 and the assembled transcriptome in NCBI\n# TSA GLBY00000000 (version GLBY01000000), so the transcriptomic claims are data elsewhere.\n#\n# Data the paper used. Lab-reared bigfin reef squid (S. lessoniana), three groups: control (reared\n# 90 days at pH 8.2), acute-OA (reared 90 days at pH 8.2, then 7 days at pH 7.8) and chronic-OA\n# (reared 90 days from hatching at pH 7.8); four replicate tanks per condition, animals sampled\n# across tanks (Methods). Measured, per squid:\n# - Routine metabolic rate (closed respirometry, umol O2 per g fresh mass per h; n = 8 to 12 per\n#   group, 29 in all by the ANOVA df) and ammonia excretion rate (separate squid; 30 and 60 min\n#   water samples; n = 5 to 9, 21 in all), Fig. 1B and 1C, Supplementary Table 1.\n# - Blood pH and total CO2, from which PCO2 and [HCO3-] are derived (Eqs. 1 and 2; n = 7, 6 and 9\n#   in Supplementary Table 2, while the Fig. 1 legend says 7 to 9), Fig. 1D to 1F.\n# - 3-D tracking (X, Y, Z every 0.1 s) of a 10 min exploration of a 60 x 20 x 22 cm arena (control\n#   15, acute 8, chronic 11 squid by Fig. 2A, Supplementary Fig. 2 and the ANOVA df; the Fig. 2B\n#   legend and Supplementary Fig. 1 give 9 acute squid), with mantle length, Fig. 2C to 2F.\n# - Predator-prey assay after the partition is lifted (10 min max): attack or not (46 control, 36\n#   acute, 22 chronic squid, from both 2-D and 3-D tracking runs), hunt duration and strike\n#   attempts of those that attacked (29, 8 and 8), Fig. 2G to 2I; prey shrimp velocity at 10 and\n#   20 min (control n = 8, CO2 n = 11), Supplementary Fig. 3.\n# - ERG to flicker (white LED, 200 ms on and 200 ms off, 5 s per frequency, 4 kHz sampling),\n#   maximum response frequency per stimulus frequency (Fig. 3C, n = 8, 8, 9) and critical flicker\n#   fusion frequency (Fig. 3D, n = 3 to 6 per group).\n# - Optic lobe RNA-seq (control 4, acute 5, chronic 3), Fig. 4 and Supplementary Fig. 5.\n# - Seawater chemistry, weekly, per condition (Supplementary Table 5); body mass and mantle length.\n#\n# Notes on the text that bear on several claims.\n# - The \"±\" after means in the Results is not named as SD or SEM. The Fig. 2 legend says mean ±\n#   SEM for Fig. 2H and 2I, but 262.2 ± 193.0 s over 8 squid only fits an SD. The blood values of\n#   Supplementary Table 2 differ slightly in their spread from those of the Results (PCO2 control\n#   234.087 against 229.5). Tolerances below are 10% of each mean: the ± values are the spread over\n#   squid, not an uncertainty of the mean, and the attempt recomputes the means from the same\n#   squid. Both SD and SEM are to be reported.\n# - Supplementary Table 3 labels the left-zone and front-zone ANOVAs \"Y=log(Y)\", but their sums of\n#   squares (residual mean squares 793.5 and 918.6) are on the scale of raw percentages; the\n#   ammonia and hunt-duration ANOVAs labelled log(Y) have sums of squares on a log10 scale.\n# - The Results cite \"Fig. 3E\" and \"Fig. 3F\" for the left and front zone durations; these are Fig.\n#   2E and 2F.\n# - The Methods say the footage was recorded at five frames per second and that coordinates were\n#   recorded every 0.1 s; the Fig. 2B legend counts 6,000 observations per squid (10 per s).\nschema_version: 2\npaper: doi:10.1038/s42003-025-09506-6\nclaims:\n- id: fig1b-metabolic-rate\n  statement: Routine metabolic rate was 16.9 (control), 18.9 (acute-OA) and 23.9 (chronic-OA) umol\n    O2 per g fresh mass per h; chronic-OA squid had a 41% higher rate than controls, and acute-OA\n    did not differ from either.\n  source: Results, Metabolic and homeostatic performances, paragraph 1; Figure 1B; Supplementary\n    Table 1\n  quote: showed routine metabolic rates of 16.9 ± 4.1 and 18.9 ± 7.0 ... Compared to control squid,\n    squid being chronically exposed to acidified conditions for 90 days (chronic-OA) showed a 41%\n    increase in metabolic rate, reaching 23.9 ± 2.1\n  statistics:\n  - about: treatment effect\n    test: ordinary one-way ANOVA\n    statistic: F(2,26) = 4.473\n    p: 0.021407\n    n: 29 squid (8 to 12 per group)\n  - about: pairwise, by the letters of Figure 1B (control a, acute ab, chronic b)\n    test: Tukey's multiple comparisons\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: control mean routine metabolic rate\n    value: 16.9\n    tolerance: 1.69\n    unit: umol O2 gFM-1 h-1\n  - quantity: acute-OA mean routine metabolic rate\n    value: 18.9\n    tolerance: 1.89\n    unit: umol O2 gFM-1 h-1\n  - quantity: chronic-OA mean routine metabolic rate\n    value: 23.9\n    tolerance: 2.39\n    unit: umol O2 gFM-1 h-1\n  - quantity: increase of chronic-OA over control\n    value: 41\n    tolerance: 4.1\n    unit: percent\n  criterion: Per squid, the rate as the Methods define it (fall in dissolved O2, in moles, over the\n    run, less the blank chamber's fall, divided by fresh mass and duration), or the deposited rate\n    if the deposit gives it. Untransformed values, ordinary one-way ANOVA and Tukey's test\n    (Supplementary Table 1). Reproduced when the means are within tolerance, the ANOVA has p < 0.05,\n    and Tukey's test separates control from chronic-OA (p < 0.05) but neither from acute-OA.\n    Partially reproduced when the ANOVA and the control against chronic-OA difference hold but the\n    acute-OA comparisons differ from the letters.\n- id: fig1c-ammonia-excretion\n  statement: Ammonia excretion was similar in control (3.3) and acute-OA (2.9 umol per g per h)\n    squid and lower in chronic-OA squid (1.6), about 52% and 45% below control and acute-OA.\n  source: Results, Metabolic and homeostatic performances, paragraphs 1 and 2; Figure 1C;\n    Supplementary Table 1\n  quote: Ammonia excretion rates were also similar between control (3.3 ± 0.7 μmol TAmm gFM−1 h−1)\n    and acutely exposed squids (2.9 ± 1.5 μmol TAmm gFM−1 h−1) ... However, chronically exposed\n    squids had significantly lower ... ammonia excretion rates, at 1.6 ± 0.5\n  statistics:\n  - about: treatment effect, on log-transformed rates\n    test: ordinary one-way ANOVA\n    statistic: F(2,18) = 6.382\n    p: 0.008038\n    n: 21 squid (5 to 9 per group)\n  - about: pairwise, by the letters of Figure 1C (control a, acute a, chronic b)\n    test: Tukey's multiple comparisons\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: control mean ammonia excretion rate\n    value: 3.3\n    tolerance: 0.33\n    unit: umol TAmm gFM-1 h-1\n  - quantity: acute-OA mean ammonia excretion rate\n    value: 2.9\n    tolerance: 0.29\n    unit: umol TAmm gFM-1 h-1\n  - quantity: chronic-OA mean ammonia excretion rate\n    value: 1.6\n    tolerance: 0.16\n    unit: umol TAmm gFM-1 h-1\n  - quantity: reduction of chronic-OA against control\n    value: 52\n    tolerance: 5.2\n    unit: percent\n  - quantity: reduction of chronic-OA against acute-OA\n    value: 45\n    tolerance: 4.5\n    unit: percent\n  criterion: Per squid, the rate as the Methods define it (ammonium at 60 min minus at 30 min, in\n    moles, divided by fresh mass and the 30 min between samples), or the deposited rate. One-way\n    ANOVA on log-transformed rates (Supplementary Table 1; the base of the log cannot change F or\n    p) and Tukey's test. Reproduced when the means are within tolerance, the ANOVA has p < 0.05 and\n    chronic-OA differs from both other groups while control and acute-OA do not differ.\n- id: fig1d-blood-ph\n  statement: Blood pH was higher in chronic-OA squid (7.17) than in controls (7.09); acute-OA squid\n    were intermediate (7.15) and differed from neither.\n  source: Results, Metabolic and homeostatic performances, paragraph 3; Figure 1D; Supplementary\n    Table 2\n  quote: Blood pH in squids that developed under chronic acidification was significantly more\n    alkaline (7.17 ± 0.07) than in control squids (7.09 ± 0.02) ... they showed an intermediate\n    blood pH of 7.15 ± 0.09, which did not differ significantly from control (p = 0.391) or\n    chronic-OA squids (p = 0.754)\n  statistics:\n  - about: treatment effect\n    test: Welch's ANOVA\n    statistic: W = 5.983, df 2, 9.196\n    p: 0.00965\n    n: 7 control, 6 acute-OA, 9 chronic-OA squid\n  - about: control against chronic-OA\n    test: Dunnett's T3\n    p: 0.015\n    ci:\n      level: 0.95\n      low: -0.129\n      high: -0.036\n  - about: control against acute-OA\n    test: Dunnett's T3\n    p: 0.391\n  - about: acute-OA against chronic-OA\n    test: Dunnett's T3\n    p: 0.754\n  expected:\n  - quantity: control mean blood pH\n    value: 7.092\n    tolerance: 0.02\n  - quantity: acute-OA mean blood pH\n    value: 7.145\n    tolerance: 0.088\n  - quantity: chronic-OA mean blood pH\n    value: 7.175\n    tolerance: 0.068\n  criterion: Tolerances for pH are the per-group spreads of Supplementary Table 2, since 10% of a pH\n    value would not test anything. Welch's ANOVA and Dunnett's T3 (Methods, Statistics; Supplementary\n    Table 2). Reproduced when the means are within tolerance, Welch's ANOVA has p < 0.05, control\n    against chronic-OA has p < 0.05 and the two other pairs p >= 0.05. Group sizes are as the deposit\n    gives them; the 6 acute-OA squid of Supplementary Table 2 against the 7 to 9 of the Fig. 1\n    legend is reported.\n- id: fig1e-blood-pco2\n  statement: Blood PCO2 rose 1.5-fold under acute-OA (1583.8 uatm) and 2.6-fold under chronic-OA\n    (2778.7 uatm) from 1057.4 uatm in controls, and all three groups differ.\n  source: Results, Metabolic and homeostatic performances, paragraph 3; Figure 1E; Supplementary\n    Table 2\n  quote: This alkalinization was accompanied by a significant 2.6-fold increase in systemic PCO2\n    from 1057.4 ± 229.5 to 2778.7 ± 637.2 ... systemic PCO2 increased to 1583.8 ± 283.4 μatm,\n    representing a 1.5-fold increase compared to control squids\n  statistics:\n  - about: treatment effect\n    test: Welch's ANOVA\n    statistic: W = 27.653, df 2, 9.379\n    p: 0.0001\n    p_relation: \"<\"\n    n: 7 control, 6 acute-OA, 9 chronic-OA squid\n  - about: control against acute-OA\n    test: Dunnett's T3\n    p: 0.013\n    ci:\n      level: 0.95\n      low: -812.540\n      high: -240.322\n      unit: uatm\n  - about: control against chronic-OA\n    test: Dunnett's T3\n    p: 0.001\n    ci:\n      level: 0.95\n      low: -2158.015\n      high: -1284.671\n      unit: uatm\n  - about: acute-OA against chronic-OA\n    test: Dunnett's T3\n    p: 0.001\n    ci:\n      level: 0.95\n      low: -1655.776\n      high: -734.047\n      unit: uatm\n  expected:\n  - quantity: control mean blood PCO2\n    value: 1057.4\n    tolerance: 105.7\n    unit: uatm\n  - quantity: acute-OA mean blood PCO2\n    value: 1583.8\n    tolerance: 158.4\n    unit: uatm\n  - quantity: chronic-OA mean blood PCO2\n    value: 2778.7\n    tolerance: 277.9\n    unit: uatm\n  - quantity: fold change, chronic-OA over control\n    value: 2.6\n    tolerance: 0.26\n  - quantity: fold change, acute-OA over control\n    value: 1.5\n    tolerance: 0.15\n  criterion: PCO2 as deposited. If only pH and total CO2 are deposited, PCO2 is derived with Eq. 1\n    from the solubility and pKa1 of Carcinus maenas hemolymph (Methods, ref. 65); the paper does not\n    print these constants, so the author takes them from ref. 65 or the deposit and says which.\n    Welch's ANOVA and Dunnett's T3. Reproduced when the means and fold changes are within tolerance\n    and all three pairs differ at p < 0.05.\n- id: fig1f-blood-bicarbonate\n  statement: Blood [HCO3-] rose 1.7-fold under acute-OA (5.90 mmol/l) and 3.1-fold under chronic-OA\n    (11.08 mmol/l) from 3.56 mmol/l in controls, and all three groups differ.\n  source: Results, Metabolic and homeostatic performances, paragraph 3; Figure 1F; Supplementary\n    Table 2\n  quote: a 3.1-fold ... 3.56 ± 0.87 ... 11.08 ± 2.20 ... 5.90 ± 0.64 mmol l–1 HCO3−, representing a\n    1.7-fold increase over controls\n  statistics:\n  - about: treatment effect\n    test: Welch's ANOVA\n    statistic: W = 39.545, df 2, 12.59\n    p: 0.0001\n    p_relation: \"<\"\n    n: 7 control, 6 acute-OA, 9 chronic-OA squid\n  - about: each of the three pairs\n    test: Dunnett's T3\n    p: 0.001\n  expected:\n  - quantity: control mean blood HCO3-\n    value: 3.56\n    tolerance: 0.356\n    unit: mmol/l\n  - quantity: acute-OA mean blood HCO3-\n    value: 5.90\n    tolerance: 0.59\n    unit: mmol/l\n  - quantity: chronic-OA mean blood HCO3-\n    value: 11.08\n    tolerance: 1.108\n    unit: mmol/l\n  - quantity: fold change, chronic-OA over control\n    value: 3.1\n    tolerance: 0.31\n  - quantity: fold change, acute-OA over control\n    value: 1.7\n    tolerance: 0.17\n  criterion: As fig1e-blood-pco2, with Eq. 2 for [HCO3-] when it must be derived. Reproduced when\n    the means and fold changes are within tolerance and all three pairs differ at p < 0.05.\n- id: methods-body-size\n  statement: After 90 days of development the squid averaged 87.5 g fresh mass and 9.9 cm mantle\n    length.\n  source: Methods, Animal handling and rearing protocols, paragraph 1\n  quote: After 90 days of development, squid reached an average fresh mass of 87.5 ± 3.3 g and\n    mantle lengths of 9.9 ± 0.2 cm\n  expected:\n  - quantity: mean fresh mass at 90 days\n    value: 87.5\n    tolerance: 8.75\n    unit: g\n  - quantity: mean mantle length at 90 days\n    value: 9.9\n    tolerance: 0.99\n    unit: cm\n  criterion: The paper does not say which squid enter these means. Readings (a) all squid with a\n    recorded mass and mantle length in the deposit; (b) control squid only; (c) all 90-day squid\n    (control and chronic-OA). Reproduced when both means are within tolerance under one reading.\n- id: stable5-seawater-chemistry\n  kind: finding\n  statement: Exposure tanks were held at pH 8.20 and PCO2 414 uatm (control), pH 7.81 and 1187 uatm\n    (acute-OA) and pH 7.80 and 1155 uatm (chronic-OA).\n  source: Supplementary Table 5\n  inferred: Numbers from Supplementary Table 5 (weekly means ± SEM); no sentence of the Results\n    states them.\n  expected:\n  - quantity: control pH\n    value: 8.20\n    tolerance: 0.01\n  - quantity: acute-OA pH\n    value: 7.81\n    tolerance: 0.03\n  - quantity: chronic-OA pH\n    value: 7.80\n    tolerance: 0.01\n  - quantity: control PCO2\n    value: 414\n    tolerance: 9\n    unit: uatm\n  - quantity: acute-OA PCO2\n    value: 1187\n    tolerance: 81\n    unit: uatm\n  - quantity: chronic-OA PCO2\n    value: 1155\n    tolerance: 22\n    unit: uatm\n  criterion: Tolerances are the SEMs of Supplementary Table 5, the uncertainty of each weekly mean.\n    Means over the weekly measurements in the deposited carbonate chemistry, PCO2 as the deposit's\n    CO2SYS output. Reproduced when all six are within tolerance.\n- id: fig2c-velocity-unchanged\n  statement: Mean swimming velocity during the 10 min exploration did not differ between groups\n    (0.2, 0.21 and 0.25 mantle lengths per s for control, acute-OA and chronic-OA).\n  source: Results, Squids behavioral paradigms, paragraph 1; Figure 2C; Supplementary Table 3\n  quote: with a mean velocity of 0.2 ± 0.16 mantle lengths s–1 ... Thereby, mean swimming velocity\n    remained unchanged at 0.21 ± 0.1 and 0.25 ± 0.16 mantle lengths\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: KW = 0.4124\n    p: 0.813689\n    n: 15 control, 8 acute-OA, 11 chronic-OA squid\n  expected:\n  - quantity: control mean velocity\n    value: 0.2\n    tolerance: 0.02\n    unit: mantle lengths/s\n  - quantity: acute-OA mean velocity\n    value: 0.21\n    tolerance: 0.021\n    unit: mantle lengths/s\n  - quantity: chronic-OA mean velocity\n    value: 0.25\n    tolerance: 0.025\n    unit: mantle lengths/s\n  depends_on:\n  - sfig2-distance-unchanged\n  criterion: A claim of absence. Velocity is total distance (sfig2-distance-unchanged) divided by\n    the duration of the exploration, normalized to mantle length (Methods, Behavioral assays). The\n    paper's test, Kruskal-Wallis at p < 0.05 (Supplementary Table 3). Reproduced when it finds no\n    difference; the effect size is reported. The control mean is printed to one decimal (0.2); a\n    value from 0.15 to 0.25 rounds to it, and is reported. Group sizes as in the comment (acute-OA 8\n    by the df; the deposit's 9th acute squid, if present, is shown as a variant).\n- id: sfig2-distance-unchanged\n  statement: Total distance travelled during the 10 min exploration did not differ between groups\n    (132.9, 124.4 and 147.3 mantle lengths for control, acute-OA and chronic-OA).\n  source: Results, Squids behavioral paradigms, paragraph 1; Supplementary Figure 2; Supplementary\n    Table 3\n  quote: Squids reared under control conditions for 90 days traveled a total of 132.9 ± 93.4 mantle\n    lengths ... Total distance traveled was unaffected by acute (124.4 ± 56.7 mantle lengths) or\n    chronic exposure (147.3 ± 97.3 mantle lengths)\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: KW = 0.4124\n    p: 0.813689\n    n: 15 control, 8 acute-OA, 11 chronic-OA squid\n  expected:\n  - quantity: control mean distance\n    value: 132.9\n    tolerance: 13.3\n    unit: mantle lengths\n  - quantity: acute-OA mean distance\n    value: 124.4\n    tolerance: 12.4\n    unit: mantle lengths\n  - quantity: chronic-OA mean distance\n    value: 147.3\n    tolerance: 14.7\n    unit: mantle lengths\n  criterion: A claim of absence. Distance by Eq. 3, the sum of 3-D step lengths between points 0.1\n    s apart over the 10 min exploration, divided by the squid's mantle length (Methods, Behavioral\n    assays). The paper does not say how untracked samples are treated; steps across a missing\n    sample are left out, a standard choice that is stated. Kruskal-Wallis at p < 0.05. Reproduced\n    when it finds no difference; effect size reported.\n- id: fig2d-acute-upper-zone\n  statement: Acute-OA squid spent most of the exploration in the upper half of the arena (86.0%),\n    more than control (30.0%) and chronic-OA (14.7%) squid, which did not differ from each other.\n  source: Results, Squids behavioral paradigms, paragraph 2; Figure 2D; Supplementary Table 3\n  quote: squid reared in control and chronically acidified seawater spent 30.0 ± 39.0% and 14.7 ±\n    17.2% of the trial in the upper arena depths, respectively (Fig. 2D). In contrast, acute\n    acidified conditions substantially influenced the behavior of squid, as they spent 86.0 ± 34.6%\n    of the trial in the upper half of the arena\n  statistics:\n  - about: treatment effect\n    test: ordinary one-way ANOVA\n    statistic: F(2,31) = 12.07\n    p: 0.000133\n    n: 15 control, 8 acute-OA, 11 chronic-OA squid\n  - about: pairwise, by the letters of Figure 2D (control a, acute b, chronic a)\n    test: Tukey's multiple comparisons\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: control time in upper zone\n    value: 30.0\n    tolerance: 3.0\n    unit: percent\n  - quantity: acute-OA time in upper zone\n    value: 86.0\n    tolerance: 8.6\n    unit: percent\n  - quantity: chronic-OA time in upper zone\n    value: 14.7\n    tolerance: 1.47\n    unit: percent\n  criterion: Upper zone is the vertical coordinate above the halfway point of the 22 cm water\n    depth, after the Cartesian transform (Methods, Behavioral assays; zones A and B). Percentage of\n    the 10 min exploration. The paper does not fix the denominator; readings (a) all 0.1 s samples\n    of the 10 min, (b) tracked samples only. Untransformed one-way ANOVA and Tukey's test\n    (Supplementary Table 3). Reproduced when, under one reading, the means are within tolerance,\n    the ANOVA has p < 0.05 and acute-OA differs from both other groups while control and chronic-OA\n    do not. Partially reproduced when the ANOVA and the acute-OA differences hold but a mean is out\n    of tolerance.\n- id: stable3-acute-shallower\n  statement: Mean depth differed between groups, acute-OA squid swimming shallower.\n  source: Results, Squids behavioral paradigms, paragraph 2; Supplementary Table 3 (Mean Depth)\n  quote: of the trial in the upper half of the arena at a significantly shallower depth\n  statistics:\n  - test: ordinary one-way ANOVA\n    statistic: F(2,31) = 8.190\n    p: 0.001394\n    n: 15 control, 8 acute-OA, 11 chronic-OA squid\n  criterion: The paper does not define mean depth. Readings (a) the mean over the exploration of the\n    height above the arena bottom (the Cartesian vertical coordinate), higher meaning shallower;\n    (b) the mean distance below the surface (22 cm less that height). Both give the same F; the\n    direction is read accordingly. Untransformed one-way ANOVA (Supplementary Table 3). Reproduced\n    when the ANOVA has p < 0.05 with F within 10% of 8.190 and the acute-OA group is the shallowest.\n    Partially reproduced when p < 0.05 and acute-OA is shallowest but F is out of that range.\n- id: fig2e-left-right-unchanged\n  statement: Acidification did not change the preference for the left or right side of the arena\n    (55.8%, 54.1% and 57.1% of the trial on the left for control, acute-OA and chronic-OA).\n  source: Results, Squids behavioral paradigms, paragraph 2; Figure 2E (cited as Fig. 3E);\n    Supplementary Table 3\n  quote: Acidification did not influence the preference for the left or right side of the arena.\n    Control squids spent 55.8 ± 31.8% of the trial on the left side, while acute and chronic\n    exposure squids spent 54.1 ± 27.9% and 57.1 ± 22.4%, respectively\n  statistics:\n  - test: ordinary one-way ANOVA\n    statistic: F(2,31) = 0.02705\n    p: 0.973338\n    n: 15 control, 8 acute-OA, 11 chronic-OA squid\n  expected:\n  - quantity: control time on left\n    value: 55.8\n    tolerance: 5.58\n    unit: percent\n  - quantity: acute-OA time on left\n    value: 54.1\n    tolerance: 5.41\n    unit: percent\n  - quantity: chronic-OA time on left\n    value: 57.1\n    tolerance: 5.71\n    unit: percent\n  criterion: A claim of absence. Left is the half of the 60 cm main zone on the left of the front\n    camera (zones A, C, G, E). Denominator as fig2d-acute-upper-zone. The paper's test is a one-way\n    ANOVA at p < 0.05; Supplementary Table 3 labels it log(Y) but its sums of squares are on the\n    raw percentage scale, so both are run, untransformed as the main reading and log as a variant\n    (zero values cannot be logged and are left out of that variant). Reproduced when the ANOVA finds\n    no difference; effect size reported.\n- id: fig2f-front-back-unchanged\n  statement: Acidification did not change the preference for the front or back of the arena (58.3%,\n    80.0% and 66.1% of the trial near the front wall for control, acute-OA and chronic-OA).\n  source: Results, Squids behavioral paradigms, paragraph 2; Figure 2F (cited as Fig. 3F);\n    Supplementary Table 3\n  quote: The control squids spent 58.3 ± 35.6% of the trial near the front wall, compared to 80.0 ±\n    15.2% and 66.1 ± 30.1% for acute and chronic exposure, respectively ... Similarly, no\n    significant difference was observed in front/back preference\n  statistics:\n  - test: ordinary one-way ANOVA\n    statistic: F(2,31) = 1.326\n    p: 0.280094\n    n: 15 control, 8 acute-OA, 11 chronic-OA squid\n  expected:\n  - quantity: control time near front\n    value: 58.3\n    tolerance: 5.83\n    unit: percent\n  - quantity: acute-OA time near front\n    value: 80.0\n    tolerance: 8.0\n    unit: percent\n  - quantity: chronic-OA time near front\n    value: 66.1\n    tolerance: 6.61\n    unit: percent\n  criterion: A claim of absence. Front is the half of the 20 cm width nearer the front camera, from\n    the above camera (Methods; the Methods call it zones E and F, the Fig. 2 legend calls F the\n    front and E the back; the halfway split is used). Denominator, transform and test as\n    fig2e-left-right-unchanged. Reproduced when the ANOVA finds no difference; effect size\n    reported.\n- id: fig2g-attack-willingness\n  statement: Acidified conditions reduced the proportion of squid that attacked prey (logistic\n    regression, pH p = 0.0422) with no effect of exposure duration (p = 0.2461); acute-OA and\n    chronic-OA squid were 64.7% and 42.3% less likely to attack than controls.\n  source: Results, Squids behavioral paradigms, paragraph 3; Figure 2G; Supplementary Table 4\n  quote: Logistic regression showed that acidified conditions significantly reduced the proportion\n    of squid that attempted to attack prey (Fig. 2G, p = 0.0422), with no significant effect of\n    exposure duration (p = 0.2461). After 7- and 90-days of acidification, squid were 64.7% and\n    42.3% less likely to attack prey compared to controls\n  statistics:\n  - about: pH term\n    test: logistic regression (GLM, binomial, logit)\n    statistic: estimate 2.734246, SE 1.345676, z = 2.032\n    p: 0.0422\n    n: 104 squid (46 control, 36 acute-OA, 22 chronic-OA)\n  - about: exposure time term\n    test: logistic regression (GLM, binomial, logit)\n    statistic: estimate 0.008351, SE 0.00762, z = 1.16\n    p: 0.2461\n    n: 104 squid\n  expected:\n  - quantity: control squid that attacked\n    value: 29\n    tolerance: 0\n  - quantity: acute-OA squid that attacked\n    value: 8\n    tolerance: 0\n  - quantity: chronic-OA squid that attacked\n    value: 8\n    tolerance: 0\n  - quantity: acute-OA reduction in attack likelihood against control\n    value: 64.7\n    tolerance: 6.47\n    unit: percent\n  - quantity: chronic-OA reduction in attack likelihood against control\n    value: 42.3\n    tolerance: 4.23\n    unit: percent\n  - quantity: pH coefficient\n    value: 2.734\n    tolerance: 0.273\n  - quantity: residual deviance\n    value: 127.58\n    tolerance: 12.76\n  - quantity: area under the ROC curve\n    value: 0.6992\n    tolerance: 0.0699\n  criterion: Counts are of squid and must match exactly (Fig. 2 legend, 29 of 46, 8 of 36, 8 of\n    22). The reductions are 1 minus the group proportion over the control proportion, which these\n    counts give exactly (64.7% and 42.3%). Logistic regression in R, attack (yes or no) on pH and\n    exposure time (Methods, Statistics). The paper does not say how pH and time are coded. Readings\n    (a) pH nominal (8.2, 7.8) and time as days in the rearing condition (control 90, acute-OA 7,\n    chronic-OA 90); (b) pH nominal and time as days of acidification (control 0); (c) as (a) or (b)\n    with the measured tank pH of Supplementary Table 5. The deviances (null 142.28 on 103 df,\n    residual 127.58 on 101 df) and AIC 133.58 identify the coding. Reproduced when, under one\n    reading, the pH term has p < 0.05 with lower attack at lower pH, the time term p >= 0.05, and\n    the counts match. Partially reproduced when the counts and reductions match but no reading gives\n    p < 0.05 for pH.\n- id: fig2h-hunt-duration\n  statement: Acute-OA squid took about 2.5 times longer to capture prey than controls (262.2 against\n    106.7 s, p = 0.03); chronic exposure did not affect hunt duration.\n  source: Results, Squids behavioral paradigms, paragraph 3; Figure 2H; Supplementary Table 4\n  quote: Acute treatments significantly increased hunt duration, requiring 262.2 ± 193.0 s compared\n    to 106.7 ± 125.2 s for controls (2.5-fold change, p = 0.03; Fig. 2H and Supplementary Table 4).\n    Chronic exposure did not affect hunt duration\n  statistics:\n  - about: treatment effect, on log-transformed durations\n    test: ordinary one-way ANOVA\n    statistic: F(2,42) = 3.372\n    p: 0.0439\n    n: 45 squid that attacked (29 control, 8 acute-OA, 8 chronic-OA)\n  - about: acute-OA against control (letters a, b; chronic-OA ab)\n    test: Tukey's multiple comparisons\n    p: 0.03\n  expected:\n  - quantity: control mean hunt duration\n    value: 106.7\n    tolerance: 10.7\n    unit: s\n  - quantity: acute-OA mean hunt duration\n    value: 262.2\n    tolerance: 26.2\n    unit: s\n  - quantity: fold change, acute-OA over control\n    value: 2.5\n    tolerance: 0.25\n  criterion: Hunt duration is the time from partition removal to capture, in squid that attacked\n    (Methods; Fig. 2 legend). One-way ANOVA on log durations (Supplementary Table 4) and Tukey's\n    test. Reproduced when the means are within tolerance, the ANOVA has p < 0.05, acute-OA differs\n    from control at p < 0.05 and chronic-OA differs from neither. Partially reproduced when acute-OA\n    is significantly longer than control but another part fails.\n- id: fig2i-strike-attempts\n  statement: Most squid struck prey successfully within 1 to 2 attempts, strike attempts did not\n    differ between groups, and every squid that attempted to hunt captured its prey.\n  source: Results, Squids behavioral paradigms, paragraph 3; Figure 2I and legend; Supplementary\n    Table 4\n  quote: the majority of examined squids were able to strike at prey successfully within 1–2\n    attempts (Fig. 2I)\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: KW = 2.568\n    p: 0.2769\n    n: 45 squid that attacked (29 control, 8 acute-OA, 8 chronic-OA)\n  criterion: Of the squid that attacked, the fraction with 1 or 2 strike attempts, overall and per\n    group. Reproduced when over half of the squid in every group needed 1 or 2 attempts, every\n    attacking squid captured its prey, and Kruskal-Wallis on attempts finds no difference at p <\n    0.05 (the paper's test). \"Majority\" read overall instead of per group is shown as a variant.\n- id: sfig3-prey-velocity-unchanged\n  statement: The velocity of the prey shrimp was not affected by CO2 treatment, time (10 and 20 min)\n    or their interaction.\n  source: Results, Squids behavioral paradigms, paragraph 3; Supplementary Figure 3\n  quote: Two-way ANOVA revealed no significant effects of CO2 treatment, time, or their interaction\n    on prey velocity (all p > 0.05)\n  statistics:\n  - test: two-way ANOVA (treatment by time)\n    p: 0.05\n    p_relation: \">\"\n    n: 8 control and 11 CO2-exposed shrimp\n  criterion: A claim of absence. Shrimp velocity at 10 and 20 min of exposure, two-way ANOVA with\n    pH and exposure time as factors (Methods, Statistics). The paper does not say whether time is a\n    repeated measure; the ordinary two-way ANOVA the Methods name is the test, and a repeated\n    measures version is shown as a variant. Reproduced when no term has p < 0.05.\n- id: fig3c-ratio-declines\n  statement: As stimulus frequency increased, the ratio of maximum response frequency to stimulus\n    frequency decreased in all three groups, markedly above 40 Hz.\n  source: Results, Temporal visual processing in squids, paragraph 2; Figure 3C and legend\n  quote: As the stimulus frequency increased, the ratio of maximal response frequency to stimulus\n    frequency decreased in all groups\n  criterion: Per squid and stimulus frequency, the maximum response frequency is the peak of the\n    difference spectrum, the FFT of the stimulus period less that of a no-stimulus period\n    (Methods; Supplementary Fig. 4B), averaged over technical replicates; the ratio is that over\n    the stimulus frequency; group means per frequency (Fig. 3C, n = 8, 8, 9). The paper does not\n    give the FFT window or the length of the no-stimulus period; the whole 5 s stimulus train and a\n    no-stimulus period of the same length are used, a stated choice, unless the deposit holds the\n    per-frequency peaks. Reproduced when, in each group, the mean ratio at every tested frequency\n    above 40 Hz is below the mean at 20 Hz, and the mean at the highest frequency is the lowest or\n    within 0.1 of it. Partially reproduced when this holds in two groups.\n- id: sfig4a-amplitude-attenuation\n  statement: ERG response amplitude attenuated as flicker frequency increased from 20 to 50 Hz.\n  source: Methods, Electroretinogram (ERG) recording and analysis, paragraph 2; Supplementary\n    Figure 4A\n  quote: The ERG traces for different stimulus frequencies (20 Hz, 30 Hz, 40 Hz, and 50 Hz) revealed\n    a clear attenuation in response amplitude with increasing frequency\n  criterion: Response amplitude per squid and frequency, averaged over the frequency's responses\n    (Methods, \"Response amplitudes were averaged for each frequency\"); the paper does not define the\n    amplitude, so readings (a) the difference-spectrum power at the stimulus frequency, (b) the\n    peak-to-peak amplitude of the trace averaged over flicker cycles. Reproduced when, under one\n    reading, the mean over all squid falls from 20 to 50 Hz at each step and is lower at 50 than at\n    20 Hz in most squid.\n- id: fig3d-cff-unchanged\n  statement: Critical flicker fusion frequency did not differ between treatments (control 50.8,\n    acute-OA 50.8, chronic-OA 47.7 Hz).\n  source: Results, Temporal visual processing in squids, paragraph 2; Figure 3D\n  quote: \"Nevertheless, the CFF average values showed no significant difference between treatments\n    (control: 50.8 ± 1.4 Hz; acute: 50.8 ± 6.3 Hz; chronic: 47.7 ± 5.5 Hz; Fig. 3D)\"\n  statistics:\n  - test: one-way ANOVA with Tukey's multiple comparisons\n    p: 0.05\n    p_relation: \">\"\n    n: 3 to 6 squid per group\n  expected:\n  - quantity: control mean CFF\n    value: 50.8\n    tolerance: 5.08\n    unit: Hz\n  - quantity: acute-OA mean CFF\n    value: 50.8\n    tolerance: 5.08\n    unit: Hz\n  - quantity: chronic-OA mean CFF\n    value: 47.7\n    tolerance: 4.77\n    unit: Hz\n  depends_on:\n  - fig3c-ratio-declines\n  criterion: A claim of absence, judged on one-way ANOVA at p < 0.05 (Methods). CFF per squid as the\n    Methods define it, read as the highest stimulus frequency at which the ratio of\n    fig3c-ratio-declines is at least 0.9; Fig. 3D shows per-squid CFFs at discrete frequencies,\n    which fits this reading. The paper does not say which squid enter Fig. 3D (n = 3 to 6 per group\n    against 8, 8 and 9 in Fig. 3C); readings (a) every squid in the deposit, (b) the squid the\n    deposit marks or gives a CFF for. Linear interpolation of the 0.9 crossing is shown as a variant.\n    Reproduced when the ANOVA finds no difference; the means and effect size are reported.\n- id: fig3d-cff-variance\n  statement: The standard deviation of CFF was 4 to 5 times higher in the acidified groups than in\n    controls.\n  source: Results, Temporal visual processing in squids, paragraph 2; Figure 3D; Discussion,\n    paragraph 8\n  quote: though variance increased markedly under acidification, with 4- to 5-fold higher standard\n    deviations in treated groups compared to controls\n  expected:\n  - quantity: SD of CFF, acute-OA over control\n    value: 4.5\n    tolerance: 1.0\n  - quantity: SD of CFF, chronic-OA over control\n    value: 4.5\n    tolerance: 1.0\n  depends_on:\n  - fig3d-cff-unchanged\n  criterion: The reported range 4 to 5, widened by 10% of each bound, is 3.6 to 5.5; it is written\n    as 4.5 with a tolerance of 1.0. Sample SDs (n - 1) of per-squid CFF under the readings of\n    fig3d-cff-unchanged. Reproduced when both ratios lie in 3.6 to 5.5. The Results call the\n    increase not statistically significant and the Discussion calls it significant; no test is\n    reported, so none is judged.\n- id: rnaseq-assembly\n  statement: The de novo optic lobe transcriptome had 902,413 transcripts, an N50 of 476 bp overall\n    and 2038 bp for the top 78% of expressed transcripts, read mapping rates above 97% (mean\n    99.51%), and 69,368 transcripts after expression filtering.\n  source: Results, RNA-seq profiling in the optic lobes, paragraph 1; Supplementary Figure 5A;\n    Methods, RNA-seq de novo assembly and Differential expression\n  quote: achieving high-quality transcripts with mapping rates exceeding 97% (average 99.51%,\n    Bowtie2 v2.5.3)68. The output showed that the highest 78% of expressed transcripts had an N50\n    of 2038 bp, and that the in-total N50 of the assembled transcripts is 476 bp\n  data: elsewhere\n  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000\n  expected:\n  - quantity: mean mapping rate\n    value: 99.51\n    tolerance: 2.0\n    unit: percent\n  - quantity: E78N50\n    value: 2038\n    tolerance: 203.8\n    unit: bp\n  - quantity: N50 of all transcripts\n    value: 476\n    tolerance: 47.6\n    unit: bp\n  - quantity: transcripts after filtering\n    value: 69368\n    tolerance: 6937\n  criterion: The mapping-rate tolerance is 2 points, since 10% of 99.51 would admit rates below the\n    reported floor of 97%. Assembly statistics from the TSA assembly with Trinity's ExN50 tool;\n    mapping with Bowtie2 v2.5.3 through align_and_estimate_abundance.pl (Methods). The filter\n    \"expression counts less than 10 and were expressed in less than 3 samples\" is open; readings\n    (a) keep transcripts with at least 10 counts in at least 3 samples, (b) drop transcripts whose\n    total count is under 10 and also those detected in fewer than 3 samples. Reproduced when every\n    value is within tolerance under one reading.\n- id: fig4a-pca\n  statement: In a PCA of optic lobe transcriptomes, acute-OA samples lay near controls along PC1\n    (35% of variance), while chronic-OA samples diverged along PC1 and PC2 (15%).\n  source: Results, RNA-seq profiling in the optic lobes, paragraph 1; Figure 4A; Supplementary\n    Figure 5B\n  quote: acute-OA samples remained near controls along PC1 (35% variance), while chronic-OA samples\n    showed significant divergence along both PC1 and PC2 axes (15% variance)\n  data: elsewhere\n  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000\n  expected:\n  - quantity: variance explained by PC1\n    value: 35\n    tolerance: 3.5\n    unit: percent\n  - quantity: variance explained by PC2\n    value: 15\n    tolerance: 1.5\n    unit: percent\n  depends_on:\n  - rnaseq-assembly\n  criterion: RSEM counts per transcript, filtered as rnaseq-assembly, DESeq2 v1.42.0, variance\n    stabilizing transform, sva v3.50.0 batch effect removed, then DESeq2's PCA function with its\n    defaults (Methods, Differential expression; Transcriptomic data visualization). The paper does\n    not give the number of surrogate variables or how they are removed; readings (a) the number sva\n    estimates, removed with limma's removeBatchEffect; (b) the known sample batches, removed the\n    same way; the deposit's code is followed if it settles this. Reproduced when, under one\n    reading, both variances are within tolerance, the acute-OA centroid is nearer the control\n    centroid on PC1 than the chronic-OA centroid is, and chronic-OA is separated from controls on\n    both PCs (centroid distance larger than the control samples' spread on each).\n- id: sfig5b-acute-clusters-with-control\n  statement: After batch-effect removal, acute-OA samples clustered closer to controls than\n    chronic-OA samples did.\n  source: Results, RNA-seq profiling in the optic lobes, paragraph 1; Supplementary Figure 5B\n  quote: An initial analysis after batch-effect removal showed that acute-OA samples clustered closer\n    to controls than chronic-OA samples\n  data: elsewhere\n  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000\n  depends_on:\n  - fig4a-pca\n  criterion: Euclidean distances between samples on the batch-corrected variance-stabilized data of\n    fig4a-pca (Supplementary Fig. 5B), under its readings. Reproduced when the mean distance from\n    acute-OA to control samples is smaller than from chronic-OA to control samples.\n- id: fig4b-shared-down-sets\n  statement: Only 2 of 36 GO gene sets were down-regulated under both acute and chronic\n    acidification, organelle inner membrane and mitochondrial inner membrane.\n  source: Results, RNA-seq profiling in the optic lobes, paragraph 2; Figure 4B and 4C\n  quote: only 2 out of 36 GO gene sets were down-regulated in both acute and chronic acidified\n    conditions organelle inner membrane and mitochondrial inner membrane\n  data: elsewhere\n  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000\n  expected:\n  - quantity: gene sets down-regulated in both treatments\n    value: 2\n    tolerance: 0\n  depends_on:\n  - fig4a-pca\n  criterion: GSEA per treatment against control, on transcripts ranked by DESeq2 log fold change\n    shrunk with the normal estimator, clusterProfiler v4.10.0 with ont ALL, minGSSize 10,\n    maxGSSize 500, nPermSimple 1000, BH adjustment, cutoff 0.05 (Methods), using the paper's\n    AnnotationForge GO database built from Trinotate and UniProt (Methods, Functional annotation;\n    in the deposit or rebuilt as described). GSEA permutations are random; the seed is a standard\n    choice and is stated. \"36\" is open; readings (a) the number of down-regulated sets in either\n    treatment, (b) all sets in the Venn diagram. Reproduced when exactly two sets are down in both\n    and they are these two, and the count is within 10% of 36 under one reading.\n- id: fig4c-acute-ridge\n  statement: Acute acidification suppressed gene sets of lipid, carboxylic acid and organic acid\n    metabolism, transferase and endopeptidase complexes and ribosomal subunits, and up-regulated\n    cell-cell adhesion.\n  source: Results, RNA-seq profiling in the optic lobes, paragraph 2; Figure 4C\n  quote: Acute acidification significantly suppressed multiple metabolic functions, including\n    cellular lipid metabolism, carboxylic acid metabolism, and organic acid metabolic processes ...\n    evidenced by suppressed transferase and endopeptidase complexes ... The ribosomal subunit and\n    ribosome-related GO terms were considerably downregulated, ... while cell-cell adhesion pathways\n    showed significant upregulation\n  data: elsewhere\n  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000\n  depends_on:\n  - fig4b-shared-down-sets\n  criterion: GSEA of fig4b-shared-down-sets, acute-OA against control. Reproduced when, at BH\n    adjusted p < 0.05, at least one GO term matching each named family (cellular lipid metabolic\n    process, carboxylic acid metabolic process, organic acid metabolic process, transferase\n    complex, endopeptidase complex, ribosomal subunit) has negative NES and a cell-cell adhesion\n    term has positive NES. Partially reproduced when most of the seven hold.\n- id: fig4d-acute-tree\n  statement: Under acute acidification down-regulated clusters included mitochondrial and energy\n    metabolism (respirasome, electron transport chain complex IV, mitochondrial envelope), fatty\n    acid biosynthesis and elongase activity, and ncRNA ribonucleoprotein and 3'-end RNA processing.\n  source: Results, RNA-seq profiling in the optic lobes, paragraph 3; Figure 4D\n  quote: The key downregulated pathways included mitochondrial and energy metabolism components,\n    particularly respirasome cytochrome, electron transport chain complex IV, and mitochondrial\n    envelope. Fatty acid biosynthesis and elongase activity pathways showed substantial suppression\n  data: elsewhere\n  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000\n  depends_on:\n  - fig4b-shared-down-sets\n  criterion: As fig4c-acute-ridge. Reproduced when terms for respirasome, cytochrome c oxidase\n    (complex IV), mitochondrial envelope, fatty acid biosynthesis or elongase activity, and ncRNA\n    ribonucleoprotein or 3'-end RNA processing are each down-regulated at BH adjusted p < 0.05.\n    The tree-plot clustering (clusterProfiler treeplot defaults) is a display and is not judged.\n- id: fig4e-chronic-synaptic-down\n  statement: Under chronic acidification down-regulated gene sets included postsynaptic membrane,\n    synaptic membrane, transmitter-gated channel activity and neurotransmitter receptor activity,\n    NAD(P)H dehydrogenase activity, respiratory electron transport, cell adhesion molecules and\n    prefoldin complex.\n  source: Results, RNA-seq profiling in the optic lobes, paragraph 3; Figure 4E\n  quote: Under chronic exposure, the GSEA tree plot demonstrated distinct downregulation patterns\n    (Fig. 4E), particularly affecting neurotransmission and synaptic activity. This included reduced\n    expression in postsynaptic membrane, synaptic membrane, transmitter-gated channel activity, and\n    neurotransmitter receptor activity terms\n  data: elsewhere\n  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000\n  depends_on:\n  - fig4b-shared-down-sets\n  criterion: GSEA of fig4b-shared-down-sets, chronic-OA against control. Reproduced when the four\n    synaptic terms are down-regulated at BH adjusted p < 0.05 and at least one term each for\n    NAD(P)H dehydrogenase activity and respiratory electron transport chain is; partially\n    reproduced when the synaptic terms hold but not the others.\n- id: fig4fgh-chronic-up\n  statement: Chronic acidification up-regulated 82 cellular component, 308 biological process and\n    128 molecular function gene sets, including vesicle, endosome and Golgi components, purine\n    biosynthesis and carbohydrate catabolism, ribonucleoprotein and ubiquitin-related activities,\n    and oxidoreductase, hydrolase and transporter activities.\n  source: Results, RNA-seq profiling in the optic lobes, paragraph 4; Figure 4F to 4H and legend\n  quote: Cellular components (CC) showed enhanced vesicular, endosomal, and Golgi apparatus pathways\n    (Fig. 4F). Biological processes (BP) exhibited upregulated purine biosynthesis and carbohydrate\n    catabolism (Fig. 4G), while molecular functions (MF) displayed elevated ribonucleoprotein\n    activity and ubiquitin-related processes\n  data: elsewhere\n  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000\n  expected:\n  - quantity: up-regulated CC gene sets, chronic-OA\n    value: 82\n    tolerance: 8.2\n  - quantity: up-regulated BP gene sets, chronic-OA\n    value: 308\n    tolerance: 30.8\n  - quantity: up-regulated MF gene sets, chronic-OA\n    value: 128\n    tolerance: 12.8\n  depends_on:\n  - fig4b-shared-down-sets\n  criterion: GSEA of fig4b-shared-down-sets, chronic-OA against control; up-regulated sets are those\n    with positive NES at BH adjusted p < 0.05, counted per ontology. Reproduced when the three\n    counts are within tolerance and at least one up-regulated term matches each named family\n    (vesicle, endosome, Golgi; purine biosynthesis, carbohydrate catabolism; ribonucleoprotein,\n    ubiquitin; oxidoreductase, hydrolase, transporter activity). Partially reproduced when the\n    families hold but a count is out of tolerance.\n- id: chronic-nachr-subunits-down\n  statement: Chronic acidification down-regulated transcripts of several nicotinic acetylcholine\n    receptor subunits (alpha-7, alpha-10 and beta-4) in the optic lobes.\n  source: Discussion, paragraph 5; Supplementary data, GSEA results\n  quote: Chronic exposure to acidified conditions caused significant changes in transcripts related\n    to synaptic function, including the downregulation of several nicotinic acetylcholine receptor\n    subunits (alpha-7, alpha-10, and beta-4\n  data: elsewhere\n  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000\n  depends_on:\n  - fig4e-chronic-synaptic-down\n  criterion: The supplementary GSEA results file the claim cites was not available to the reader.\n    Transcripts annotated (Methods, Functional annotation) as nAChR alpha-7, alpha-10 and beta-4\n    subunits are read either (a) as core enrichment genes of a chronic-OA down-regulated synaptic\n    gene set of fig4e-chronic-synaptic-down, or (b) as having negative shrunken log fold change in\n    DESeq2, chronic-OA against control. Reproduced when all three subunits are down under one\n    reading; partially reproduced for one or two.\n- id: optic-lobe-no-ion-regulation\n  statement: No change was seen in optic lobe transcripts associated with acid-base or ion\n    regulatory processes.\n  source: Discussion, paragraph 3\n  quote: we did not observe changes in optic lobe transcripts associated with acid–base or ion\n    regulatory processes\n  data: elsewhere\n  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000\n  depends_on:\n  - fig4b-shared-down-sets\n  criterion: A claim of absence, judged on the paper's GSEA (fig4b-shared-down-sets) at BH adjusted\n    p < 0.05 for both treatments against control. The paper does not list the terms; the GO terms\n    whose names contain \"pH\", \"acid-base\", \"bicarbonate\", \"proton\", \"chloride\" or \"ion\n    transmembrane transport\" are read as these processes. Reproduced when none is significant in\n    either treatment; the terms that are, with their NES, are reported either way.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/allen-2026.yaml",
 "old_string": "    conditions organelle inner membrane and mitochondrial inner membrane",
 "new_string": "    conditions ... organelle inner membrane and mitochondrial inner membrane"
}
```

```
The file claims/allen-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  && python tools/claims_check.py claims/allen-2026.yaml paper/10.1038-s42003-025-09506-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && grep -n "1655" paper/*.txt | od -c | head -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import yaml;d=yaml.safe_load(open('claims/allen-2026.yaml'))['claims']
print(len(d),sum('quote' in c for c in d),sum('statistics' in c for c in d),sum('criterion' in c for c in d),sum('expected' in c for c in d),sum(c.get('data')=='elsewhere' for c in d))"; git status --short
```

```
31 30 16 31 20 10
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
?? claims/allen-2026.yaml
?? scripts
```

**Agent**

I wrote `claims/allen-2026.yaml` (not committed). It has 31 claims; the quote checker passes everything except one confidence-interval bound, which I confirmed by eye.

**Text read:** the version of record (Communications Biology PDF and its extracted text) with its one supplement: Supplementary Figs 1 to 5 and Supplementary Tables 1 to 5. I opened PDF pages 3 and 7 to 10 only to read the significance letters of Figs 1B–F, 2D and 2H and the axes of Fig. 3C and 3D. I read no code: the paper links no repository and says its scripts are in the Dryad deposit, which I did not open.

**Claims:** 31 in all.
- **Quotes:** 30 have one. The seawater chemistry claim (Supplementary Table 5) is marked `inferred` because no sentence states those numbers.
- **Statistics:** 16 claims record them.
- **Expected values:** 20 claims have them.
- **Criteria:** all 31 have one.
- **Data elsewhere:** 10 claims are `data: elsewhere`. These are the RNA-seq results, whose data are in NCBI SRA PRJNA1204452 and TSA GLBY01000000.
- **Checker:** `tools/claims_check.py` reports one problem: it cannot find the bound −1655.776 for the acute-OA against chronic-OA PCO2 difference. The value is printed in Supplementary Table 2; the checker rounds it to six significant digits before searching.

**Details the paper leaves open, and the readings named:**
- **Which number in the Results "±":** SD or SEM is not stated, and the Fig. 2 legend's "SEM" cannot be right for hunt duration. Tolerances are 10% of each mean, with both SD and SEM to be reported.
- **Logistic regression coding:** the pH and time coding is not given. Readings: nominal pH with time as days in the rearing condition, nominal pH with time as days of acidification, or either with the measured tank pH. The reported deviances and AIC identify which one.
- **Zone percentages:** the denominator is either all 0.1 s samples or tracked samples only.
- **Left and front zone tests:** Supplementary Table 3 labels them log(Y), but their sums of squares are on raw percentages. Raw is the main reading and log a variant.
- **Mean depth:** height above the bottom, or distance below the surface.
- **Acute 3-D group:** 8 squid (Fig. 2A, the ANOVA df) or 9 (Supplementary Fig. 1, Fig. 2B legend).
- **CFF definition:** the highest frequency with a ratio of at least 0.9 is the main reading, which Fig. 3D supports; linear interpolation is a variant. Which squid enter Fig. 3D is also open: it shows 3 to 6 per group against 8, 8 and 9 in Fig. 3C.
- **ERG analysis:** the FFT window and the length of the no-stimulus period are not given. The amplitude measure is either spectral power at the stimulus frequency or the peak-to-peak amplitude.
- **Body size:** which squid enter the 90-day mass and mantle length (all, control only, or control plus chronic).
- **Prey velocity:** whether the two-way ANOVA treats time as a repeated measure.
- **Strike attempts:** "majority" read per group or overall.
- **Seawater:** the blood PCO2 and HCO3− equations need the constants of ref. 65, which the paper does not print.
- **RNA-seq:**
  - The expression filter's wording allows two readings.
  - How sva batch effects were removed: estimated surrogate variables or known batches.
  - What "36" GO sets counts: down-regulated sets in either treatment, or all sets in the Venn diagram.
  - Which GO terms count as acid-base or ion regulation.
  - The nAChR claim reads "down" either as core-enrichment membership or as a negative fold change.

**Missing from the paper:** the supplementary data files "DET Results" and "GSEA results" are not under `paper/`. Only `chronic-nachr-subunits-down` rests on them (the alpha-7, alpha-10 and beta-4 subunits), and its criterion says so.

**Inconsistencies in the paper:**
- The Results cite Fig. 3E and 3F where they mean Fig. 2E and 2F.
- The Methods give the footage as 5 frames per second, but coordinates are recorded every 0.1 s.
- The blood spreads differ slightly between the Results and Supplementary Table 2.
- The acute blood group has 6 squid in Supplementary Table 2, while the Fig. 1 legend gives 7 to 9 per group.
- The Results call the higher CFF variance not significant; the Discussion calls it significant.

## End of run

38 turns, 7 minutes, $2.41 at API prices, result: success.
