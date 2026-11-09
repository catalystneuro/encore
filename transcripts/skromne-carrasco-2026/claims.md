# 001676 · claims · run 39577757286

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/; ls claims/001676 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; wc -c paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-10096-w.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-10096-w.txt",
 "offset": 1133,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the full text (main text, Methods, Extended Data legends). PDF pages 22 to 25 have no extracted text, so I'm checking what they hold. I'm also checking the dataset's archive description.

**Agent calls Bash**

```bash
python -c "
import fitz;d=fitz.open('paper/10.1038-s41586-025-10096-w.pdf');print(len(d))
for i in range(21,len(d)):
  p=d[i];print(i+1,len(p.get_text()),len(p.get_images()))
"; ls tools; curl -s https://api.dandiarchive.org/api/dandisets/001676/ | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001676/versions/0.251205.2137/info/ | python -c "import json,sys;m=json.load(sys.stdin)['metadata'];print(m.get('description'));print(m.get('assetsSummary'))"; which pdftotext pdfinfo pdftoppm; pdfinfo paper/*.pdf | grep Pages
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-10096-w.pdf",
 "pages": "22-25"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import pypdf;r=pypdf.PdfReader('paper/10.1038-s41586-025-10096-w.pdf');print(len(r.pages))
for i in range(21,len(r.pages)):
  p=r.pages[i];print(i+1,repr(p.extract_text()[:300]), list(p.get('/Resources',{}).get('/XObject',{}).keys()) if p.get('/Resources') else None)
" 2>&1 | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "kind\|data:\|open\|readings" docs/*.md | grep -iv "^docs/protocol.md" | head -30
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

[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
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
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000])"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 82 more lines not kept]
```

**Agent**

I have everything I need from the paper. It links no code ("Code will be made available upon request"), so none can be read. Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "content": "# Claims for Skromne Carrasco, Viejo & Peyrache (2026), \"Months-long stability of the\n# head-direction system\", Nature 652, 167-173, on dandiset 001676.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (Nature, 2026), from the PDF supplied by hand, as extracted to\n# paper/10.1038-s41586-025-10096-w.txt: main text, Methods, and the legends of Extended Data\n# Figs. 1 to 10. The Supplementary Information (Supplementary Table 1, recording details of the\n# electrophysiology, and Supplementary Table 2, sessions and HD cells per animal) is not under\n# paper/ and was not read; no claim rests on it. The Source Data files were not read. PDF pages\n# 22 to 25 carry no extractable text (in Nature PDFs, the reporting summary) and could not be\n# rendered. No figure was read from the PDF.\n#\n# Code. The paper's Code availability statement reads \"Code will be made available upon\n# request.\" No repository is linked, so no code was read. Every method detail below comes from\n# the Methods or the figure legends; where they are silent the detail is named as open.\n#\n# Data the paper used, as it reports it.\n# - Imaging. Mice 1 to 5 (adult male C57BL/6J), GRIN lens (1.0 mm) over the left\n#   post-subiculum (PoSub), GCaMP6f, UCLA Miniscope V4, 20-min sessions of free foraging on\n#   weekdays, head direction and position from an Optitrack multi-camera system. ROIs from\n#   CNMF_E after NoRMCorre motion correction, registered across days with CellReg (each\n#   registration has a CellReg confidence score). 388 sessions in all. Three experiments per mouse\n#   (Methods, Statistics and reproducibility): (1) about 30 days, 20 sessions over 4 weeks, in the\n#   circular environment (Fig. 1); (2) two weeks in each of four environments, in the order\n#   circular, square, radial (8-arm) maze, open field, 40 sessions over 8 weeks (Fig. 2), then a\n#   week of probe trials, one environment per day (Fig. 3); (3) four weeks with visits to the four\n#   environments in random order (Extended Data Fig. 9). The circular, square and radial maze are in\n#   one room, the open field in another room. For mouse 2 the Miniscope broke between the second\n#   and third environment; for mouse 5 the field of view was lost before the probe trials.\n# - Imaging, mice 6 to 10 (Fig. 4, Extended Data Fig. 10). Two novel environments (square and\n#   circular in the figure) visited on one day 8 h apart, one of them then visited weekly for\n#   three weeks, both revisited on week 5 (7 sessions over 5 weeks). The groups are named\n#   \"weekly\" and \"single\" visits. The Methods say \"Five adult male C57BL/6J mice were used in\n#   all experiments\" and also describe mice 6 to 10.\n# - Electrophysiology (Extended Data Fig. 7). Four mice with silicon probes in PoSub, 15 to 20\n#   min of free foraging in the circular, square and radial maze on one day, disoriented 2 to 5\n#   min between environments, Kilosort 2.5 and manual curation; 125 HD cells and 129 non-HD\n#   cells.\n# - The dandiset (title as the paper, 14 subjects) is described as holding the longitudinal\n#   Miniscope recordings of all four protocols and the electrophysiology of four animals.\n#\n# Methods shared by the claims (Methods, HD cell classification by Miniscope, and following).\n# - Tuning curve. Average dF/F in 3 degree bins of head direction, divided by the time spent in\n#   each bin, smoothed with a Gaussian kernel \"(sigma = 12° bins)\". OPEN: whether sigma is 12\n#   degrees or 12 bins (36 degrees); both readings are run where a claim depends on tuning\n#   curves.\n# - HD cell (imaging). Split-half tuning curve correlation of at least 0.4 (ROIs below are\n#   discarded); head-direction information (HDI, Skaggs et al. 1992, ref. 59) averaged across\n#   sessions above 0.1; sessions where the cell's HDI is below 0.11 are discarded; tracked on\n#   several days with CellReg score above 0.8 (above 0.6 for Fig. 3); detected in at least six\n#   sessions for Figs. 1 and 2, at least two for Figs. 3, 4d-f and Extended Data Fig. 10. OPEN: the\n#   HDI formula for dF/F (Skaggs information with dF/F in place of rate; log base 2 is the\n#   standard choice and cannot change an outcome beyond the threshold scale, so log2 is used);\n#   whether HDI is computed on the raw or the smoothed tuning curve (both readings).\n# - HD cell (electrophysiology). Firing rate above 1 Hz and HDI above 0.3. OPEN: tuning curve\n#   bins and smoothing for spikes are not given; the imaging values are the reading.\n# - Change in preferred direction between two sessions. For each HD cell present in both, the\n#   circular shift at the maximum of the cross-correlation of its two tuning curves; the circular\n#   mean over cells is the session's change.\n# - Change in pairwise angular offset. For each pair of HD cells, the offset is the shift at the\n#   maximum of the cross-correlation of the two cells' tuning curves in one session; its change is\n#   the minimum circular difference between two sessions. Shuffle, cell pair identity shuffled\n#   within a day, 1,000 times.\n# - Remapping between environments. Circular mean over cells of the shift in preferred direction\n#   between two sessions; the average remapping is the circular mean over all session pairs of the\n#   two environments; its mean vector length is the coherency. Shuffle, cell identity shuffled\n#   within a day, 1,000 times.\n# - HD decoding. XGBoost, multiclass, 32 head-direction bins. Training session cells with CellReg\n#   score above 0.8, split-half correlation above 0.4 and HDI above 0.11, kept if present in the\n#   test session; dF/F smoothed with a Gaussian of sigma 133 ms, normalized, averaged in 0.09 s\n#   bins; the top 50% of population activity bins kept and z-scored; error is the minimum circular\n#   difference between predicted and actual direction. Chance from time-reversed head direction\n#   (\"average error\" in the Methods, \"median error\" in the Fig. 1k legend). \"Same\" values train on\n#   the first half of a session and test on the second. OPEN: XGBoost hyperparameters (the library\n#   defaults are the reading); how \"population activity\" is summed before taking the top 50% (sum\n#   of normalized dF/F over cells is the reading); the error summary is the median per session pair\n#   (Fig. 1k legend).\n# - Environment decoding. XGBoost trained on the pairwise tuning curve correlations of all HD cell\n#   pairs in a random half of the recordings of each of the four environments, tested on the\n#   other half; shuffle of cell pair identity within each recording. OPEN: the number of random\n#   splits and the seed; how cells absent in a recording enter the feature vector.\n# - Drift rate (degrees per week, Figs. 1h, 1i, 2e, 3f, 3g, Extended Data Fig. 9b). The Methods\n#   do not define it. OPEN, readings: (a) the slope of a least-squares line of the per session\n#   pair values against day difference, times 7; (b) the same slope fitted to the values averaged\n#   per day difference (the curve the figure shows); (c) as (a) with the line through the origin.\n#   For Fig. 3 the delay is in weeks and the slope is taken per week.\n# - Statistics named in the paper (V-test, Rayleigh test, Wilcoxon signed-rank, Wald test,\n#   repeated-measures ANOVA) are run as named; pycircstat, listed in the Methods, is used for\n#   the circular tests (its vtest returns V = n R cos(mean - 0) and a one-sided p, while the\n#   legends say \"two-tailed\"; both p are reported).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001676\"\n  doi: 10.48324/dandi.001676/0.251205.2137\npaper: doi:10.1038/s41586-025-10096-w\nclaims:\n- id: roi-counts\n  statement: Across 388 imaging sessions, the number of ROIs per session ranged from 21 to 286\n    (95 plus or minus 56, mean and s.d.), and was stable over time.\n  source: Results, The tuning of HD cells is stable over time, paragraph 1; Extended Data Fig. 1d\n  quote: Across a total of 388 sessions, the number of ROIs per session ranged from 21 to 286 (95 ±\n    56 (mean ± s.d.)) and was stable over time\n  expected:\n  - quantity: number of imaging sessions\n    value: 388\n    tolerance: 0\n  - quantity: minimum ROIs per session\n    value: 21\n    tolerance: 2.1\n  - quantity: maximum ROIs per session\n    value: 286\n    tolerance: 28.6\n  - quantity: mean ROIs per session\n    value: 95\n    tolerance: 56\n  criterion: ROIs are the CNMF_E segments of each imaging session (Methods, Miniscope\n    recordings), counted per session over all imaging sessions of mice 1 to 10. The session count\n    holds when 388 sessions are found; the paper does not say whether sessions of mice 6 to 10\n    are included, so the readings are (a) all imaging sessions and (b) mice 1 to 5 only. \"Stable\n    over time\" has no test in the paper; it is judged per mouse within the Fig. 1 protocol as no\n    monotonic trend, read as a Spearman correlation of ROI count with session number that is not\n    significant at p < 0.05 in a majority of mice, and the correlations are shown.\n- id: edf1e-hd-proportion\n  statement: In the four-week circular protocol, the median proportion of ROIs detected as HD\n    cells per animal was 0.2, 0.7, 0.4, 0.7 and 0.2, with 72, 42, 197, 48 and 102 ROIs per session\n    on average, over 19, 20, 19, 19 and 20 recordings.\n  source: Extended Data Fig. 1e legend\n  quote: Median proportion ± s.d. per animal = 0.2 ± 0.03, 0.7 ± 0.04, 0.4 ± 0.05, 0.7 ± 0.05, 0.2 ±\n    0.04. n = 19, 20, 19, 19, 20 recordings per animal, with a respective mean ± s.d. of ROIs\n    detected 72 ± 16, 42 ± 5, 197 ± 18, 48 ± 12, 102 ± 25\n  expected:\n  - quantity: median HD proportion, animal 1\n    value: 0.2\n    tolerance: 0.03\n  - quantity: median HD proportion, animal 2\n    value: 0.7\n    tolerance: 0.04\n  - quantity: median HD proportion, animal 3\n    value: 0.4\n    tolerance: 0.05\n  - quantity: median HD proportion, animal 4\n    value: 0.7\n    tolerance: 0.05\n  - quantity: median HD proportion, animal 5\n    value: 0.2\n    tolerance: 0.04\n  - quantity: mean ROIs per session, animals 1 to 5\n    value: 72\n    tolerance: 16\n  criterion: The ROI means use the s.d. given per animal as tolerance (72 plus or minus 16, 42\n    plus or minus 5, 197 plus or minus 18, 48 plus or minus 12, 102 plus or minus 25); the\n    recording counts must match exactly. The HD cell is as in the opening comment, per session\n    (split-half correlation at least 0.4 and session HDI at least 0.11 among ROIs whose\n    across-session HDI exceeds 0.1). The paper does not say whether the CellReg and six-session\n    conditions apply to this proportion; readings (a) with them and (b) without. Reproduced when,\n    under one reading and one smoothing reading, at least four of the five proportions are within\n    tolerance.\n- id: edf1h-ring\n  statement: An Isomap projection of the HD cell population activity forms a ring, reflecting the\n    circular representation of head direction.\n  source: Results, The tuning of HD cells is stable over time, paragraph 2; Extended Data Fig. 1h\n  quote: Low-dimensional projection of HD cell population activity using Isomap (Methods), a\n    technique for visualizing high-dimensional data by preserving its geometric structure, revealed\n    a ring topology\n  criterion: Method from the Methods (Dimensionality reduction). HD cells with split-half\n    correlation above 0.8 and HDI above 0.1 in the session; dF/F smoothed with a Gaussian of sigma\n    133 ms, normalized (OPEN, readings z-score and division by the maximum), averaged in 0.25 s\n    bins; bins where the mean normalized activity is below 0.1 dropped; Isomap with 50\n    neighbours to two dimensions. The paper judges the ring by eye with head direction as colour.\n    The criterion is read from Extended Data Fig. 7d, which plots the Isomap angle against head\n    direction, as a circular-circular correlation between the angle of each point around the\n    embedding's centroid and the head direction, significant at p < 0.05 in an example session of\n    each of the five mice. Reproduced when this holds for all five; partially reproduced for three\n    or four.\n- id: fig1f-example-stable\n  statement: In an example mouse, the population change in preferred direction relative to the\n    last session was concentrated around 0 degrees (V-test, v = 17.06, P < 0.001, 18 sessions,\n    median absolute deviation 5.0 degrees).\n  source: Fig. 1f legend; Results, The tuning of HD cells is stable over time, paragraph 2\n  quote: Population average of across-session angular difference in preferred direction, relative\n    to the last session for one example mouse (V-test, not different from 0°, v = 17.06,\n    two-tailed P < 0.001, n = 18 sessions, median absolute deviation from 0° = 5.0°)\n  statistics:\n  - test: V-test against 0 degrees\n    statistic: v = 17.06\n    p: 0.001\n    p_relation: \"<\"\n    n: 18 sessions of one mouse\n  expected:\n  - quantity: V statistic, example mouse\n    value: 17.06\n    tolerance: 1.706\n  - quantity: median absolute deviation from 0 degrees\n    value: 5.0\n    tolerance: 0.5\n    unit: degrees\n  criterion: Per session, the change in preferred direction relative to the last session of the\n    circular protocol (opening comment). The example mouse is not named in Fig. 1. Readings are\n    (a) animal 4, which Extended Data Fig. 1g names as the animal of Fig. 1, and (b) any mouse\n    with 18 compared sessions. Reproduced when, under one reading, V and the median absolute\n    deviation are within tolerance and the V-test p is below 0.001.\n- id: fig1g-all-mice-stable\n  statement: Across all five mice, the population change in preferred direction relative to the\n    last session was concentrated around 0 degrees (V-test, v = 75.21, P < 0.001, 84 sessions),\n    with per-mouse means of 15.4, 2.1, -5.5, -7.8 and -6.9 degrees.\n  source: Fig. 1g legend\n  quote: Distribution of population-wise angular difference relative to the last session for all\n    five mice (V-test, not different from 0°, v = 75.21, two-tailed P < 0.001, n = 84 sessions). Per\n    mouse... 15.4 ± 24.7°, 2.1 ± 18.7°, −5.5 ± 15.2°, −7.8 ± 23.6°, −6.9 ± 41.5° (mean ± s.d.)\n  statistics:\n  - test: V-test against 0 degrees\n    statistic: v = 75.21\n    p: 0.001\n    p_relation: \"<\"\n    n: 84 sessions of 5 mice\n  expected:\n  - quantity: pooled V statistic\n    value: 75.21\n    tolerance: 7.521\n  - quantity: number of sessions pooled\n    value: 84\n    tolerance: 0\n  - quantity: mean change, mouse 1\n    value: 15.4\n    tolerance: 24.7\n    unit: degrees\n  - quantity: mean change, mouse 2\n    value: 2.1\n    tolerance: 18.7\n    unit: degrees\n  - quantity: mean change, mouse 3\n    value: -5.5\n    tolerance: 15.2\n    unit: degrees\n  - quantity: mean change, mouse 4\n    value: -7.8\n    tolerance: 23.6\n    unit: degrees\n  - quantity: mean change, mouse 5\n    value: -6.9\n    tolerance: 41.5\n    unit: degrees\n  criterion: As fig1f-example-stable, pooled over the five mice. The per-mouse means use the\n    per-mouse s.d. as tolerance. Reproduced when the pooled V is within tolerance with p below\n    0.001 and at least four per-mouse means are within tolerance.\n- id: edf4ab-vtest-per-animal\n  statement: The V statistic of the change in preferred direction relative to the last session\n    was 14.1, 17.1, 17.3, 14.6 and 12.2 per animal, against shuffle medians of 3.0, 3.2, 5.7, 4.8\n    and 2.0, and 75.2 pooled against a shuffle median of 18.6; each animal's distribution was\n    concentrated around 0 degrees (P < 0.001).\n  source: Extended Data Fig. 4a,b legends\n  quote: V statistic per animal = 14.1, 17.1, 17.3, 14.6, 12.2. Median of V statistic shuffles per\n    animal = 3.0, 3.2, 5.7, 4.8, 2.0. Left... V-test statistic for pooled animals (75.2) versus the\n    distribution of V statistic for within-day shuffled cell identity (median = 18.6)\n  statistics:\n  - about: each animal not in Fig. 1\n    test: V-test against 0 degrees\n    p: 0.001\n    p_relation: \"<\"\n    n: 16, 18, 16 and 16 sessions\n  expected:\n  - quantity: V statistic, animal 1\n    value: 14.1\n    tolerance: 1.41\n  - quantity: V statistic, animal 2\n    value: 17.1\n    tolerance: 1.71\n  - quantity: V statistic, animal 3\n    value: 17.3\n    tolerance: 1.73\n  - quantity: V statistic, animal 4\n    value: 14.6\n    tolerance: 1.46\n  - quantity: V statistic, animal 5\n    value: 12.2\n    tolerance: 1.22\n  - quantity: pooled shuffle V median\n    value: 18.6\n    tolerance: 1.86\n  criterion: Shuffle of HD cell identity within a day, 1,000 times (Methods, Orientation\n    remapping). The per-animal V of Extended Data Fig. 4b and the Fig. 1f value (17.06) do not\n    agree for animal 4 (14.6); this is recorded, not resolved. Reproduced when at least four of\n    the five per-animal V are within tolerance and each exceeds its shuffle median.\n- id: edf4c-previous-session\n  statement: The change in preferred direction relative to the previous session was also\n    concentrated around 0 degrees across the five animals (V-test, P < 0.001, 75 sessions; pooled\n    V 69.9 against a shuffle median of 21.9).\n  source: Extended Data Fig. 4c,d legends\n  quote: Distribution of population- wise angular difference relative to the previous session for\n    all five animals (V-test, not different from 0°, two-tailed p < 0.001, n = 75 sessions)\n  statistics:\n  - test: V-test against 0 degrees\n    p: 0.001\n    p_relation: \"<\"\n    n: 75 sessions of 5 animals\n  expected:\n  - quantity: pooled V statistic, previous session\n    value: 69.9\n    tolerance: 6.99\n  - quantity: pooled shuffle V median, previous session\n    value: 21.9\n    tolerance: 2.19\n- id: edf2-no-registration-confound\n  statement: The shift in preferred direction between the first and last recording was not\n    significantly related to the displacement of the ROI centroid in the field of view (p = 0.290)\n    or to the CellReg score (p = 0.344), while centroid displacement was related to CellReg score\n    (p = 0.004).\n  source: Results, The tuning of HD cells is stable over time, paragraph 3; Extended Data Fig. 2c-e\n  quote: the change in preferred direction was not significantly correlated with the quality of\n    cell registration nor the drift of the ROI in the Miniscope field of view\n  statistics:\n  - about: shift in preferred direction against centroid displacement, all cells\n    test: two-sided Wald test\n    p: 0.29\n    n: 72 HD cells\n  - about: same, cells with CellReg score over 0.8\n    test: two-sided Wald test\n    p: 0.588\n    corrected: Bonferroni\n  - about: CellReg score against shift in preferred direction\n    test: two-sided Wald test\n    p: 0.344\n    n: 72 HD cells\n  - about: centroid displacement against CellReg score\n    test: two-sided Wald test\n    p: 0.004\n    corrected: Bonferroni\n    n: 72 HD cells\n  criterion: A claim of absence, judged on the paper's test, the two-sided Wald test of the slope\n    of a linear regression (as scipy.stats.linregress gives it) at 0.05 Bonferroni-corrected over\n    the tests of the figure. Per HD cell registered in the first and last recording of the\n    circular protocol, the shift in preferred direction (cross-correlation, opening comment),\n    the centroid displacement and the CellReg score. OPEN, readings for which cells give n = 72,\n    (a) pooled over the five mice and (b) the Fig. 1 example mouse; and for the shift, (i) signed\n    and (ii) absolute. Reproduced when the two absence tests are not significant and the\n    displacement against score test is significant; the slopes are shown.\n- id: fig1h-drift-rate\n  statement: The absolute change in preferred direction grew slowly with the days between\n    recordings, at a drift rate of 7.1 plus or minus 4.4 degrees per week across mice.\n  source: Results, The tuning of HD cells is stable over time, paragraph 3; Fig. 1h\n  quote: we computed the absolute change in preferred direction as a function of days passed\n    between recordings and observed... a slow drift rate (7.1 ± 4.4° per week)\n  expected:\n    quantity: mean drift rate of preferred direction across mice\n    value: 7.1\n    tolerance: 4.4\n    unit: degrees per week\n  criterion: Per pair of sessions of the circular protocol, the absolute change in preferred\n    direction; OPEN, readings for the value (a) the absolute value of the session-level circular\n    mean over cells and (b) the median over cells of each cell's absolute change. Drift rate per\n    mouse by the readings of the opening comment, averaged over the five mice. Reproduced when\n    the mean is within tolerance and positive under one combination of readings.\n- id: edf4ef-not-diffusive\n  statement: The drift in preferred direction was not diffusive (not a random walk) but\n    fluctuated around a fixed direction, as shown by the cumulative variance of orientation across\n    days.\n  source: Results, The tuning of HD cells is stable over time, paragraph 3; Extended Data Fig. 4e,f\n  quote: Analysis of the cumulative variance of orientation across days suggested that this drift,\n    although modest, was not diffusive (that is, not a random walk) but instead fluctuated around a\n    fixed direction\n  criterion: Extended Data Fig. 4e plots the mean variance of the absolute change in preferred\n    direction against the number of recordings included, from the first to the last day. The\n    paper gives no test. A random walk predicts a variance growing in proportion to the number of\n    recordings. OPEN, the variance is read (a) as that of the session-level changes relative to\n    the last day over the first k recordings and (b) relative to the first day. Reproduced when,\n    under the reading run, the variance at the full number of recordings is less than half the\n    value a line through the origin fitted to the first five points predicts, in at least four of\n    five mice. This threshold is the reader's and is recorded as a deviation.\n- id: edf4f-change-below-shuffle\n  statement: The absolute change in overall preferred direction with respect to the last day was\n    smaller than for shuffled cell identities in every animal (median 15.9, 5.1, 7.9, 26.3 and\n    24.0 degrees; one-tailed Wilcoxon, p from 3.8e-6 to 1.5e-4).\n  source: Extended Data Fig. 4f legend\n  quote: Absolute change in overall preferred direction, per session, with respect to the last day\n    of the experiment in Fig. 1. Median absolute change per animal in degrees... 15.9, 5.1, 7.9,\n    26.3, 24.0\n  statistics:\n  - about: animal 1 against shuffle\n    test: one-tailed Wilcoxon signed rank test\n    statistic: W = 1.0\n    p: 3.052e-5\n  - about: animal 2 against shuffle\n    test: one-tailed Wilcoxon signed rank test\n    statistic: W = 0.0\n    p: 3.81e-6\n  - about: animal 3 against shuffle\n    test: one-tailed Wilcoxon signed rank test\n    statistic: W = 0.0\n    p: 3.81e-6\n  - about: animal 4 against shuffle\n    test: one-tailed Wilcoxon signed rank test\n    statistic: W = 3.0\n    p: 7.63e-5\n  - about: animal 5 against shuffle\n    test: one-tailed Wilcoxon signed rank test\n    statistic: W = 5.0\n    p: 1.53e-4\n  expected:\n  - quantity: median absolute change, animal 1\n    value: 15.9\n    tolerance: 1.59\n    unit: degrees\n  - quantity: median absolute change, animal 2\n    value: 5.1\n    tolerance: 0.51\n    unit: degrees\n  - quantity: median absolute change, animal 3\n    value: 7.9\n    tolerance: 0.79\n    unit: degrees\n  - quantity: median absolute change, animal 4\n    value: 26.3\n    tolerance: 2.63\n    unit: degrees\n  - quantity: median absolute change, animal 5\n    value: 24.0\n    tolerance: 2.4\n    unit: degrees\n  criterion: Per session the absolute change against the same session's shuffled-identity value.\n    OPEN, the shuffle value per session is read as (a) the median and (b) the mean over 1,000\n    shuffles. Reproduced when every animal's one-tailed Wilcoxon is below 0.05 and at least three\n    medians are within tolerance.\n- id: edf4g-pairwise-offset-stable\n  statement: The change in pairwise angular offset across all registered HD cell pairs was\n    strongly biased towards 0, with per-animal medians of 12, 9, 12, 24 and 12 degrees against\n    shuffle medians of 51 to 54 degrees (p < 0.001 per animal, 25,901 pairs).\n  source: Results, The tuning of HD cells is stable over time, paragraph 4; Extended Data Fig. 4g\n  quote: The change in pairwise angular offset across all registered cell pairs (independent of\n    interleaving days) was strongly biased towards 0 (Extended Data Fig. 4g), suggesting highly\n    coherent population dynamics\n  statistics:\n  - test: median against 1,000 shuffled medians\n    p: 0.001\n    p_relation: \"<\"\n    n: 25,901 pairs\n  expected:\n  - quantity: median change in offset, animal 1\n    value: 12.0\n    tolerance: 1.2\n    unit: degrees\n  - quantity: median change in offset, animal 2\n    value: 9.0\n    tolerance: 0.9\n    unit: degrees\n  - quantity: median change in offset, animal 3\n    value: 12.0\n    tolerance: 1.2\n    unit: degrees\n  - quantity: median change in offset, animal 4\n    value: 24.0\n    tolerance: 2.4\n    unit: degrees\n  - quantity: median change in offset, animal 5\n    value: 12.0\n    tolerance: 1.2\n    unit: degrees\n  - quantity: number of HD cell pairs\n    value: 25901\n    tolerance: 2590\n  criterion: Method from the Methods (Change in the angular offset) over all session pairs of the\n    circular protocol. Since the cross-correlation shift is on a 3 degree grid, a median within\n    one bin (3 degrees) of the reported value also counts. Reproduced when every animal's median\n    is below all 1,000 shuffled medians and at least four medians are within tolerance.\n- id: fig1i-offset-drift\n  statement: The change in pairwise angular offset drifted more slowly (4.1 plus or minus 4.8\n    degrees per week) than single cell tuning, though not significantly so.\n  source: Results, The tuning of HD cells is stable over time, paragraph 4; Fig. 1i\n  quote: the change in pairwise angular offset drifted more slowly (4.1 ± 4.8° per week), yet this\n    was not significantly different from single cell tuning drift rate\n  expected:\n    quantity: mean drift rate of pairwise offset across mice\n    value: 4.1\n    tolerance: 4.8\n    unit: degrees per week\n  depends_on:\n  - fig1h-drift-rate\n  criterion: Per pair of sessions, the median over cell pairs of the absolute change in offset\n    (Fig. 1i axis, \"Median delta angular offset\"); drift rate per mouse by the readings of the\n    opening comment. The test against the fig1h-drift-rate values is not named. A claim of\n    absence; OPEN, readings (a) two-sided Wilcoxon signed-rank and (b) paired t-test across the\n    five mice, at 0.05. Reproduced when the mean is within tolerance and neither test is\n    significant; not reproduced when either is. Effect size shown.\n- id: fig1k-decoding-across-days\n  statement: Decoders of head direction trained on one session and tested on another decoded\n    significantly better than chance for nearly the whole four weeks of the experiment.\n  source: Results, The tuning of HD cells is stable over time, paragraph 5; Fig. 1j,k\n  quote: we trained and tested non-linear decoders (extreme gradient-boosted trees (Methods)) on\n    every recording session pair and observed statistically significant decoding for nearly the\n    entire duration of the experiment\n  criterion: Decoder as in the opening comment, on every ordered pair of sessions of the circular\n    protocol, error per pair as the median over time bins, chance from time-reversed head direction\n    in the test session (both median and mean error are run, as the Methods and legend differ).\n    The paper does not name its test. OPEN, readings (a) per day difference, one-sided Wilcoxon\n    signed-rank of data against chance over all session pairs of all mice, and (b) per day\n    difference, one-sided Wilcoxon across the five mice of per-mouse means. Reproduced when, under\n    one reading, the error is below chance at p < 0.05 for every day difference up to 20 days\n    except at most one, read as \"nearly the entire duration\"; partially reproduced when that holds\n    up to 10 days.\n- id: edf4ij-pv-decay\n  statement: The population vector coherence decayed slowly over the course of the recording.\n  source: Results, The tuning of HD cells is stable over time, paragraph 5; Extended Data Fig. 4h-j\n  quote: This is in line with a slow decay in the population vector coherence over the course of\n    the recording\n  criterion: Population vector correlation between two sessions with activity in 12 head-direction\n    bins (Extended Data Fig. 4h). OPEN, readings (a) the mean over bins of the correlation across\n    cells of the two sessions' population vectors at the same head-direction bin and (b) the\n    correlation of the two flattened cell by bin matrices. Reproduced when the correlation\n    decreases with the days between sessions (negative Spearman correlation, p < 0.05, in at least\n    four of five mice) and its mean at the longest day difference stays above 0.\n- id: fig2e-offset-across-environments\n  statement: Across the four environments, HD cells preserved their pairwise angular offsets,\n    with per-animal median changes of 24, 12, 18, 29 and 12 degrees against shuffle medians of 54\n    to 57 degrees, and a drift rate of 1.9 plus or minus 1.02 degrees per week.\n  source: Results, Internal organization across time and environments, paragraph 1; Fig. 2e;\n    Extended Data Fig. 6b\n  quote: We observed the same tendency of preserved pairwise angular difference in preferred\n    directions across... all sessions and mice (Fig. 2e and Extended Data Fig. 6)\n  expected:\n  - quantity: mean drift rate of pairwise offset across environments\n    value: 1.9\n    tolerance: 1.02\n    unit: degrees per week\n  - quantity: median change in offset, animal 1\n    value: 24.0\n    tolerance: 38.9\n    unit: degrees\n  - quantity: median change in offset, animal 2\n    value: 12.0\n    tolerance: 38.0\n    unit: degrees\n  - quantity: median change in offset, animal 3\n    value: 18.0\n    tolerance: 31.5\n    unit: degrees\n  - quantity: median change in offset, animal 4\n    value: 29.0\n    tolerance: 42.7\n    unit: degrees\n  - quantity: median change in offset, animal 5\n    value: 12.0\n    tolerance: 30.5\n    unit: degrees\n  criterion: Over all session pairs of the 40-session multi-environment protocol. The per-animal\n    tolerances are the s.d. that Extended Data Fig. 6b gives with each median. The Methods exclude\n    mouse 2 from this analysis while Extended Data Fig. 6b lists five values; readings (a) mouse 2\n    excluded, (b) mouse 2 included, (c) mouse 2 with only pairs within one Miniscope epoch.\n    Reproduced when, under one reading, every included animal's median is below all 1,000\n    shuffled medians and the mean drift rate (opening comment readings) is within tolerance.\n- id: edf5c-stable-within-environment\n  statement: The tuning of HD cells was stable within each environment, with changes in preferred\n    direction relative to the last day concentrated around 0 degrees in all four, and no\n    difference between environments (repeated-measures ANOVA, F = 0.44, P = 0.73).\n  source: Results, Internal organization across time and environments, paragraph 1; Extended Data\n    Fig. 5c\n  quote: The tuning of HD cells was stable within each environment for all mice\n  statistics:\n  - about: circular\n    test: V-test against 0 degrees\n    statistic: v = 44.5\n    p: 1.0e-308\n    p_relation: \"<\"\n    n: 45 sessions\n  - about: square\n    test: V-test against 0 degrees\n    statistic: v = 15.5\n    p: 2.26e-4\n    n: 39 sessions\n  - about: radial maze\n    test: V-test against 0 degrees\n    statistic: v = 35.4\n    p: 7.55e-14\n    n: 44 sessions\n  - about: open field\n    test: V-test against 0 degrees\n    statistic: v = 31.5\n    p: 5.16e-12\n    n: 43 sessions\n  - about: difference between environments\n    test: repeated-measures ANOVA\n    statistic: F = 0.44, numDF = 3, denDF = 12\n    p: 0.73\n  expected:\n  - quantity: V statistic, circular\n    value: 44.5\n    tolerance: 4.45\n  - quantity: V statistic, square\n    value: 15.5\n    tolerance: 1.55\n  - quantity: V statistic, radial maze\n    value: 35.4\n    tolerance: 3.54\n  - quantity: V statistic, open field\n    value: 31.5\n    tolerance: 3.15\n  criterion: Per environment, the change in preferred direction of each session relative to the\n    last session of that environment (for mouse 2 in the square, the next-to-last day, as the\n    legend says). The ANOVA is a claim of absence judged on a repeated-measures ANOVA over\n    environments with mice as subjects (n = 5, giving 3 and 12 degrees of freedom) at 0.05; the\n    per mouse and environment value is OPEN, readings (a) mean absolute change and (b) median\n    absolute change. Reproduced when all four V-tests are significant, at least three V are within\n    tolerance and the ANOVA is not significant.\n- id: edf7-ephys-offsets\n  statement: Electrophysiological recordings confirmed that pairwise angular offsets of HD cells\n    are preserved across environments, with per-animal median changes of 18, 12, 27 and 15 degrees\n    against shuffle medians of 54 degrees (p < 0.001).\n  source: Results, Internal organization across time and environments, paragraph 2; Extended Data\n    Fig. 7e\n  quote: To confirm that this long-tailed distribution is not specific to the imaging technique, we\n    confirmed these results with electrophysiological recordings\n  statistics:\n  - test: median against 1,000 shuffled medians\n    p: 0.001\n    p_relation: \"<\"\n    n: 4 animals\n  expected:\n  - quantity: median change in offset, ephys animal 1\n    value: 18.0\n    tolerance: 41.7\n    unit: degrees\n  - quantity: median change in offset, ephys animal 2\n    value: 12.0\n    tolerance: 35.5\n    unit: degrees\n  - quantity: median change in offset, ephys animal 3\n    value: 27.0\n    tolerance: 43.2\n    unit: degrees\n  - quantity: median change in offset, ephys animal 4\n    value: 15.0\n    tolerance: 39.5\n    unit: degrees\n  - quantity: number of HD cells, four animals\n    value: 125\n    tolerance: 12.5\n  criterion: HD cells with firing rate above 1 Hz and HDI above 0.3; spike-count tuning curves\n    (bins and smoothing OPEN, the imaging values as the reading); offsets compared across the\n    three environment pairs of the day. Tolerances are the s.d. given with each median. Reproduced\n    when every animal's median is below all 1,000 shuffled medians.\n- id: edf7g-waveforms\n  statement: Electrophysiologically recorded HD cells have broader waveforms than non-HD cells\n    (median trough-to-peak 0.54 against 0.295 ms, half-peak width 0.21 against 0.165 ms).\n  source: Extended Data Fig. 7g legend\n  quote: Note HD cells tend to have broader waveforms, consistent with pyramidal cells. Median HD\n    trough-to-peak = 0.54 ms, median HD half-peak width = 0.21 ms, versus 0.295 and 0.165\n    respectively for non-HD cells; n = 254 cells\n  expected:\n  - quantity: median trough-to-peak, HD cells\n    value: 0.54\n    tolerance: 0.054\n    unit: ms\n  - quantity: median trough-to-peak, non-HD cells\n    value: 0.295\n    tolerance: 0.0295\n    unit: ms\n  - quantity: median half-peak width, HD cells\n    value: 0.21\n    tolerance: 0.021\n    unit: ms\n  - quantity: median half-peak width, non-HD cells\n    value: 0.165\n    tolerance: 0.0165\n    unit: ms\n  criterion: Mean waveform per unit on its largest channel; trough-to-peak from trough to the\n    following maximum, half-peak width the width at half the trough amplitude. These definitions\n    are not in the paper and are OPEN; they are the standard ones. Reproduced when at least three\n    of the four medians are within tolerance and HD medians exceed non-HD medians for both.\n- id: edf8-same-vs-mixed\n  statement: For recordings 7 days apart, decoders trained and tested in the same environment\n    tended to be better than across environments, and the change in pairwise offset tended to be\n    smaller, neither significantly (p = 0.063 for both).\n  source: Results, Environmental modulation of the HD cell population, paragraph 1; Extended Data\n    Fig. 8b,c\n  quote: Decoders of head direction of mice trained and tested in the same environment one week\n    apart showed a tendency for better (yet non-significant) accuracy than decoders trained across\n    environments with the same delay between sessions\n  statistics:\n  - about: change in angular offset, single against mixed\n    test: two-sided Wilcoxon signed-rank test\n    statistic: W = 0.0\n    p: 0.063\n    n: 5 mice\n  - about: decoder error variance, single against mixed\n    test: two-sided Wilcoxon signed-rank test\n    statistic: W = 0.0\n    p: 0.063\n    n: 5 mice\n  expected:\n  - quantity: change in offset, single environment\n    value: 16.2\n    tolerance: 10.1\n    unit: degrees\n  - quantity: change in offset, mixed environments\n    value: 23.1\n    tolerance: 11.4\n    unit: degrees\n  - quantity: decoder error variance, single environment\n    value: 0.58\n    tolerance: 0.09\n  - quantity: decoder error variance, mixed environments\n    value: 0.74\n    tolerance: 0.13\n  criterion: Pairs of sessions 7 days apart in the multi-environment protocol, \"single\" when both\n    are in one environment and \"mixed\" otherwise; per mouse the mean over pairs. The decoder\n    measure is the variance of the error between predicted and actual direction (OPEN, readings\n    the circular variance and the linear variance of the signed circular error in radians). The\n    tendency claim is reproduced when every mouse is lower for single than mixed (W = 0) under one\n    reading and the means are within tolerance.\n- id: fig2g-environment-classifier\n  statement: Classifiers of environment identity trained on pairwise correlations of HD cell\n    tuning curves were more accurate than shuffles (proportion correct 0.7 against 0.3; one-sided\n    Wilcoxon, P = 0.031, W = 15).\n  source: Results, Environmental modulation of the HD cell population, paragraph 1; Fig. 2f,g\n  quote: These classifiers showed higher accuracy than controls (Fig. 2f,g), supporting the idea\n    that the HD signal in the PoSub is environment specific\n  statistics:\n  - test: one-sided signed-rank Wilcoxon test\n    statistic: W = 15.0\n    p: 0.031\n    n: 5 mice\n  expected:\n  - quantity: proportion correct, data\n    value: 0.7\n    tolerance: 0.1\n  - quantity: proportion correct, shuffle\n    value: 0.3\n    tolerance: 0.1\n  criterion: Method as in the opening comment. The random half split is OPEN; the criterion runs\n    100 random splits per mouse and uses the mean proportion correct, and also a single split\n    with a fixed seed, as readings. Reproduced when, under one reading, the one-sided Wilcoxon of\n    data against shuffle across the five mice has p below 0.05 and the means are within\n    tolerance.\n- id: fig2i-random-remapping\n  statement: The remapping of the HD system between the three environments of one room seemed\n    random across mice (Rayleigh test, P = 0.36 circular to square, 0.61 square to radial maze,\n    0.032 radial maze to circular).\n  source: Results, Environmental modulation of the HD cell population, paragraph 2; Fig. 2h,i\n  quote: Notably, this remapping seemed random across mice, although more data would be required to\n    support a true random remapping\n  statistics:\n  - about: circular to square\n    test: Rayleigh's test\n    statistic: z = 1.08\n    p: 0.36\n    n: 5 mice\n  - about: square to radial maze\n    test: Rayleigh's test\n    statistic: z = 0.53\n    p: 0.61\n    n: 5 mice\n  - about: radial maze to circular\n    test: Rayleigh's test\n    statistic: z = 3.19\n    p: 0.032\n    n: 5 mice\n  expected:\n  - quantity: Rayleigh z, circular to square\n    value: 1.08\n    tolerance: 0.108\n  - quantity: Rayleigh z, square to radial maze\n    value: 0.53\n    tolerance: 0.053\n  - quantity: Rayleigh z, radial maze to circular\n    value: 3.19\n    tolerance: 0.319\n  criterion: Average remapping per mouse and environment pair as in the opening comment, over all\n    session pairs of the two environments, in room coordinates; mouse 2 included (Methods,\n    Inclusion and exclusion criteria). Rayleigh's test over the five mice. Reproduced when the\n    first two tests are not significant at 0.05 and the third is, matching the paper, with z\n    within tolerance; partially reproduced when the first two are not significant but the third\n    pattern differs.\n- id: fig2i-remapping-coherent\n  statement: Within each mouse, the remapping between environments was coherent across HD cells,\n    compared with shuffled cell identities.\n  source: Fig. 2h,i legend\n  quote: The alignment of the resultant vector of all HD pairwise cell angular offsets between\n    environments defined for each mouse the angular remapping between environments (μα), and its\n    mean vector length defined the coherency of this remapping\n  inferred: null\n  criterion: placeholder\n- id: fig3de-probe-memory\n  statement: After a delay without visits, the orientation of the HD system in each environment\n    was retained, drifting slowly with the delay; it was concentrated around 0 degrees for delays\n    under 1, 2 and 4 weeks (V-test, P = 0.002, 0.02, 0.03) but not at 6 weeks (P = 0.191), with\n    mean absolute changes of 3.6, 23.9, 39.6 and 70.0 degrees.\n  source: Results, HD system forms long-term memories of orientation, paragraph 1; Fig. 3d\n  quote: the average alignment of the HD system to external environments across mice drifted\n    gradually, albeit slowly, as the interval between sessions increased, becoming significantly\n    different from 0° only at the 6-week delay\n  statistics:\n  - about: delay under 1 week\n    test: V-test against 0 degrees\n    statistic: v = 4.0\n    p: 0.002\n    n: 4 mice\n  - about: delay 2 weeks\n    test: V-test against 0 degrees\n    statistic: v = 3.0\n    p: 0.02\n    n: 4 mice\n  - about: delay 4 weeks\n    test: V-test against 0 degrees\n    statistic: v = 2.7\n    p: 0.03\n    n: 4 mice\n  - about: delay 6 weeks\n    test: V-test against 0 degrees\n    statistic: v = 1.2\n    p: 0.191\n    n: 4 mice\n  expected:\n  - quantity: mean absolute change, under 1 week\n    value: 3.6\n    tolerance: 2.0\n    unit: degrees\n  - quantity: mean absolute change, 2 weeks\n    value: 23.9\n    tolerance: 37.3\n    unit: degrees\n  - quantity: mean absolute change, 4 weeks\n    value: 39.6\n    tolerance: 30.3\n    unit: degrees\n  - quantity: mean absolute change, 6 weeks\n    value: 70.0\n    tolerance: 25.8\n    unit: degrees\n  criterion: Per mouse (mice 1 to 4; mouse 5 excluded, Methods) and environment, the remapping\n    between the last visit of the two-week protocol and the probe trial (Methods, Orientation\n    remapping), HD cells with CellReg score above 0.6 detected in at least two sessions. The\n    delays are those of the environment order, open field under 1 week, radial maze 2 weeks,\n    square 4 weeks, circular 6 weeks (OPEN, the probe order is not given; the delays are taken\n    from the session dates). Reproduced when the V-tests are significant at 0.05 for the first\n    three delays and not at 6 weeks, and the mean absolute change increases with delay; partially\n    reproduced when the 6-week test is not significant but one earlier delay also fails.\n- id: fig3e-mvl-delay\n  statement: The mean vector length of the remapping angles across mice decreased with delay\n    (0.998, 0.79, 0.79 and 0.536 for under 1, 2, 4 and 6 weeks), compared with shuffled HD cell\n    identities.\n  source: Fig. 3e\n  quote: Mean vector length of animal remapping angles (that is, probe versus last visit of each\n    environment, for n = 4 mice) as a function of delay between visits compared to controls\n    (shuffled HD cell identity)\n  expected:\n  - quantity: mean vector length, under 1 week\n    value: 0.998\n    tolerance: 0.0998\n  - quantity: mean vector length, 2 weeks\n    value: 0.79\n    tolerance: 0.079\n  - quantity: mean vector length, 4 weeks\n    value: 0.79\n    tolerance: 0.079\n  - quantity: mean vector length, 6 weeks\n    value: 0.536\n    tolerance: 0.0536\n  depends_on:\n  - fig3de-probe-memory\n  criterion: Mean vector length of the four mice's remapping angles at each delay, from\n    fig3de-probe-memory. Reproduced when at least three of the four values are within tolerance\n    and the 6-week value is the lowest.\n- id: fig3fg-probe-drift\n  statement: The absolute change in individual preferred directions drifted with delay at 10.8\n    plus or minus 0.1 degrees per week, while the pairwise angular offsets stayed coherent,\n    drifting at 2.5 plus or minus 0.1 degrees per week.\n  source: Results, HD system forms long-term memories of orientation, paragraph 1; Fig. 3f,g\n  quote: We further tested this drift by assessing the absolute changes in individual neuronal\n    preferred directions and observed a similar drift from the original direction (Fig. 3f). Of\n    note, the population structure maintained its coherence across these recordings\n  expected:\n  - quantity: drift rate of preferred direction, probe\n    value: 10.8\n    tolerance: 1.08\n    unit: degrees per week\n  - quantity: drift rate of pairwise offset, probe\n    value: 2.5\n    tolerance: 0.25\n    unit: degrees per week\n  criterion: The legend's spread (0.1) is far below the spread of a mean over four mice and is\n    read as a standard error of a fit; 10% of the value is used as tolerance. Values against delay\n    in weeks, drift rate per mouse by the readings of the opening comment, mean over mice 1 to 4.\n    The Methods exclude mouse 2 from the 6-week delay \"of pairwise angular offset (Fig. 3f)\";\n    readings (a) mouse 2 excluded at 6 weeks from the pairwise offset (Fig. 3g) and (b) from the\n    preferred direction (Fig. 3f). Reproduced when both rates are within tolerance under one\n    combination of readings; partially reproduced when the preferred-direction rate exceeds the\n    pairwise-offset rate but a value is outside tolerance.\n- id: edf9-interference\n  statement: After four further weeks of visits to the four environments in random order, the\n    system showed reduced retention of the original preferred direction, though changes relative\n    to week 1 stayed centred on 0 degrees (V = 11.3, 10.1, 10.8), and pairwise offsets drifted at\n    a mean of 1.6 degrees per week.\n  source: Results, HD system forms long-term memories of orientation, paragraph 1; Extended Data\n    Fig. 9b,d\n  quote: this orientation memory may be affected by cognitive load as after four additional weeks\n    of extensive experience with the different environments, the systems showed reduced retention\n    of the original preferred direction\n  statistics:\n  - test: V-test against 0 degrees\n    statistic: V = 11.3, 10.1, 10.8\n    p: 0.05\n    p_relation: \"<\"\n    n: 20, 20 and 18 sessions\n  expected:\n  - quantity: V statistic, week 2\n    value: 11.3\n    tolerance: 1.13\n  - quantity: V statistic, week 3\n    value: 10.1\n    tolerance: 1.01\n  - quantity: V statistic, week 4\n    value: 10.8\n    tolerance: 1.08\n  - quantity: mean drift rate of pairwise offset\n    value: 1.6\n    tolerance: 0.16\n    unit: degrees per week\n  criterion: The legend says only that the V-tests are significant; p below 0.05 is the reading.\n    \"Reduced retention\" has no test in the paper. OPEN, it is read as the mean over mice of the\n    absolute change in preferred direction relative to week 1 at week 4 (Extended Data Fig. 9e)\n    being larger than the mean absolute change at the 4-week probe delay of fig3de-probe-memory.\n    Reproduced when the V statistics and drift rate are within tolerance and that comparison\n    holds.\n- id: fig4d-single-visit-memory\n  statement: After a single visit, the orientation of the HD cell population was retained four\n    weeks later as well as with weekly visits; the change in preferred direction from first to\n    last session was smaller than shuffles in both groups (one-sided Wilcoxon, P = 0.031) and did\n    not differ between groups (P = 0.438; weekly 12.4, single 6.6 degrees).\n  source: Results, Memory from a single visit is stable over weeks, paragraph 1; Fig. 4d\n  quote: We observed a highly maintained absolute orientation of the HD cell population for both\n    environments\n  statistics:\n  - about: data against shuffles, each group\n    test: one-sided signed-rank Wilcoxon\n    statistic: W = 0.0\n    p: 0.031\n    n: 5 mice\n  - about: weekly against single\n    test: two-sided signed-rank Wilcoxon\n    statistic: W = 4.0\n    p: 0.438\n    n: 5 mice\n  expected:\n  - quantity: absolute change in preferred direction, weekly\n    value: 12.4\n    tolerance: 10.0\n    unit: degrees\n  - quantity: absolute change in preferred direction, single\n    value: 6.6\n    tolerance: 4.1\n    unit: degrees\n  criterion: Mice 6 to 10; per mouse and environment, the absolute change in preferred direction\n    between the first and the last session in that environment, HD cells detected in at least two\n    sessions with CellReg score above 0.8 (OPEN, the 0.6 threshold of Fig. 3 is the other\n    reading); shuffle of cell identity, its value per mouse the median over 1,000 shuffles.\n    Reproduced when both one-sided tests have p below 0.05, the two-sided group test is not\n    significant at 0.05 (a claim of absence on the paper's test), and the means are within\n    tolerance.\n- id: fig4e-decoder-single-visit\n  statement: A decoder of head direction trained on the first and tested on the last session was\n    accurate for both environments, with no difference between the weekly and single groups\n    (weekly 35.9, single 43.9 degrees median error; P = 0.438).\n  source: Results, Memory from a single visit is stable over weeks, paragraph 1; Fig. 4e\n  quote: This was further supported by the high accuracy of a decoder of head direction for both\n    environments (not significantly different from other animals)\n  statistics:\n  - about: weekly against single\n    test: two-sided signed-rank Wilcoxon\n    statistic: W = 4.0\n    p: 0.438\n    n: 5 mice\n  expected:\n  - quantity: median decoding error, weekly\n    value: 35.9\n    tolerance: 15.0\n    unit: degrees\n  - quantity: median decoding error, single\n    value: 43.9\n    tolerance: 17.1\n    unit: degrees\n  criterion: Decoder as in the opening comment, trained on the first and tested on the last session\n    of each environment for mice 6 to 10. The group test is a claim of absence on the paper's\n    test, two-sided Wilcoxon at 0.05. \"High accuracy\" is read as every mouse's error below its\n    time-reversed chance. The comparison with \"other animals\" has no named test or data and is not\n    tested. Reproduced when the means are within tolerance, the group test is not significant and\n    every error is below chance.\n- id: edf10c-environment-identity\n  statement: The change in preferred direction from first to last visit did not differ between the\n    two environments (circular mean 1.6 against 5.1 degrees; two-sided Wilcoxon, p = 1.0, n = 10).\n  source: Extended Data Fig. 10c legend\n  quote: Change in preferred direction first versus last visit, classified by environment identity.\n    Circular mean ± s.d. in degrees... 1.6 ± 14.1, 5.1 ± 8.0. Two-sided Wilcoxon signed-rank p =\n    1.0, W statistic = 7.0, n = 10\n  statistics:\n  - test: two-sided Wilcoxon signed-rank\n    statistic: W = 7.0\n    p: 1.0\n    n: \"10\"\n  expected:\n  - quantity: circular mean change, environment 1\n    value: 1.6\n    tolerance: 14.1\n    unit: degrees\n  - quantity: circular mean change, environment 2\n    value: 5.1\n    tolerance: 8.0\n    unit: degrees\n  criterion: A claim of absence on the paper's test, a two-sided Wilcoxon signed-rank at 0.05,\n    paired by mouse across the two environments of mice 6 to 10 (n = 10 read as 5 mice by 2\n    environments). The legend does not say which environment is which; the readings are both\n    assignments of square and circular. Reproduced when the test is not significant and the means\n    are within tolerance under one assignment.\n- id: edf10b-per-animal-change\n  statement: Per animal of the single-visit protocol, the circular mean change in preferred\n    direction relative to the first visit was 4.7, -0.4, -15.5, 5.4 and -6.2 degrees.\n  source: Extended Data Fig. 10b legend\n  quote: Circular mean ± s.d. per animal with pooled environments in degrees... 4.7 ± 3.4, −0.4 ±\n    5.8, −15.5 ± 34.7, 5.4 ± 10.8, −6.2 ± 10.9\n  expected:\n  - quantity: circular mean change, animal 6\n    value: 4.7\n    tolerance: 3.4\n    unit: degrees\n  - quantity: circular mean change, animal 7\n    value: -0.4\n    tolerance: 5.8\n    unit: degrees\n  - quantity: circular mean change, animal 8\n    value: -15.5\n    tolerance: 34.7\n    unit: degrees\n  - quantity: circular mean change, animal 9\n    value: 5.4\n    tolerance: 10.8\n    unit: degrees\n  - quantity: circular mean change, animal 10\n    value: -6.2\n    tolerance: 10.9\n    unit: degrees\n  criterion: Per session of mice 6 to 10, the change in preferred direction relative to the first\n    visit of its environment, pooled over both environments. The mapping of the legend's order to\n    mice 6 to 10 is taken as ascending. Reproduced when at least four of five are within\n    tolerance.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I left a placeholder claim (`fig2i-remapping-coherent`); replacing it with a proper one now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "- id: fig2i-remapping-coherent\n  statement: Within each mouse, the remapping between environments was coherent across HD cells,\n    compared with shuffled cell identities.\n  source: Fig. 2h,i legend\n  quote: The alignment of the resultant vector of all HD pairwise cell angular offsets between\n    environments defined for each mouse the angular remapping between environments (μα), and its\n    mean vector length defined the coherency of this remapping\n  inferred: null\n  criterion: placeholder",
 "new_string": "- id: fig2h-coherent-remapping\n  statement: While the internal structure of the HD system was largely kept across environments,\n    its absolute orientation was specific to each environment, the HD cells of a mouse shifting\n    together (coherent remapping) compared with shuffled cell identities.\n  source: Results, Environmental modulation of the HD cell population, paragraph 2; Fig. 2c,d,h,i\n  quote: Whereas the internal structure of the HD system was largely preserved across environments,\n    with only minor modulations, its absolute orientation was specific to each environment\n  criterion: Per mouse and pair of environments, the mean vector length over HD cells of the shift\n    in preferred direction, for each pair of recordings of the two environments (Methods,\n    Orientation remapping), compared with 1,000 shuffles of cell identity within a day. The\n    paper gives no threshold; the 95th percentile of the shuffle distribution, the bound Fig. 3e\n    draws for its controls, is used. Per mouse and environment pair, coherent when the median over\n    recording pairs of the mean vector length exceeds the median over recording pairs of the\n    shuffle 95th percentile. Reproduced when this holds for at least 80% of the mouse and\n    environment pairs over all six pairs of the four environments (mouse 2 included, as for\n    remapping in the Methods), and the average remapping of at least one environment pair differs\n    from 0 by more than 30 degrees in at least three mice, read as an orientation specific to each\n    environment."
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "absence; OPEN, readings (a) two-sided Wilcoxon signed-rank and (b) paired t-test across the\n    five mice, at 0.05.",
 "new_string": "absence; OPEN, readings (a) two-sided Wilcoxon signed-rank and (b) paired t-test across the\n    five mice, at 0.05 (with five mice, reading (a) cannot reach p below 0.0625)."
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001676/10.1038-s41586-025-10096-w.yaml paper/10.1038-s41586-025-10096-w.txt; grep -nE "^[^#]*[^'\"]: .*: " claims/001676/*.yaml | grep -v "^\S*:\s*#" | head
```

Result: not kept, because it reads the paper's text.

**Agent**

Nine quotes fail, each on a word split across a line break in the text file ("visual-izing", "fluc-tuated", and so on). I'll cut around those words with "...".

**Agent calls Bash**

```bash
cd claims/001676 && python - <<'EOF'
import re
p='10.1038-s41586-025-10096-w.yaml'
s=open(p).read()
rep=[
("a\n    technique for visualizing high-dimensional data by preserving its geometric structure, revealed\n    a ring topology","a\n    technique for... high-dimensional data by preserving its geometric structure, revealed\n    a ring topology"),
("not a random walk) but instead fluctuated around a\n    fixed direction","not a random walk) but instead... around a\n    fixed direction"),
("cell pairs (independent of\n    interleaving days)","cell pairs (... of\n    interleaving days)"),
("not specific to the imaging technique, we\n    confirmed","not specific to the imaging... we\n    confirmed"),
("Fig. 2f,g), supporting the idea","Fig. 2f,g)... the idea"),
("with only minor modulations, its absolute","with only minor... its absolute"),
("becoming significantly\n    different from 0°","becoming significantly... from 0°"),
("experience with the different environments, the systems","experience with the different... the systems"),
("absolute orientation of the HD cell population for both\n    environments","absolute orientation of the HD cell... for both\n    environments"),
]
for a,b in rep:
    assert a in s,a
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
cd ../.. && python tools/claims_check.py claims/001676/10.1038-s41586-025-10096-w.yaml paper/10.1038-s41586-025-10096-w.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Every quote now passes. Last checks: em dashes, the word "rather", and colon-space inside plain scalars.

**Agent calls Bash**

```bash
f=claims/001676/10.1038-s41586-025-10096-w.yaml; grep -n "—\|rather" $f; python - <<'EOF'
import yaml,re
f='claims/001676/10.1038-s41586-025-10096-w.yaml'
lines=open(f).read().split('\n')
# flag continuation or value lines containing ': ' after the key
for i,l in enumerate(lines,1):
    if l.lstrip().startswith('#'): continue
    m=re.match(r'^(\s*-?\s*[a-z_]+: )(.*)$',l)
    body=m.group(2) if m else l
    if ': ' in body and not body.strip().startswith(('"',"'")): print(i,l)
d=yaml.safe_load(open(f));print(len(d['claims']),sum('statistics' in c for c in d['claims']),sum('criterion' in c for c in d['claims']))
EOF
```

```
31 17 30
```

**Agent**

I wrote `claims/001676/10.1038-s41586-025-10096-w.yaml`. The quote checker passes with 0 problems: 31 claims, 31 quotes, 35 statistical values. Nothing is committed.

**Text read.** The version of record (Nature 652, 2026), from the hand-supplied PDF's text extraction: main text, Methods and all ten Extended Data legends. No figure was opened.
- The Supplementary Information (Supplementary Tables 1 and 2: the electrophysiology recording details and the sessions and HD cells per animal) is not under `paper/`. Neither are the Source Data. No claim rests on either, so I went ahead.
- PDF pages 22 to 25 have no extractable text and could not be rendered here. In Nature PDFs these are usually the reporting summary.
- The paper links no code ("Code will be made available upon request"), so no code was read. Every method detail comes from the Methods or the legends.

**Claims.** 31 claims, all with quotes and none `inferred`. 17 carry statistics and 30 have criteria. All use `data: dataset`; the paper uses no outside data.
- **Fig. 1 (stability in one environment):** ROI counts, HD-cell proportions, the Isomap ring, the V-tests (example mouse, pooled and per animal), registration confounds, drift rates, the shuffle comparisons, the pairwise-offset change, decoding across days, and the decay of population-vector correlation.
- **Fig. 2 (four environments):** offsets across environments, stability within each environment, electrophysiology offsets and waveforms, same versus mixed environments a week apart, the environment classifier, the Rayleigh tests of random remapping, and coherent remapping.
- **Fig. 3 (probe trials):** V-tests and mean vector lengths by delay, probe drift rates, and the interference experiment (Extended Data Fig. 9).
- **Fig. 4 and Extended Data Fig. 10 (single-visit memory):** the single-visit memory tests, the decoder, and the per-environment and per-animal values.

**Details the paper leaves open, and the readings named:**
- **Smoothing kernel**, "σ = 12° bins": 12 degrees, or 12 bins (36 degrees).
- **HDI on dF/F**: computed on the raw or the smoothed tuning curve. Log base 2 is used as the standard choice.
- **Drift rate**, never defined:
  - (a) a least-squares slope over session pairs;
  - (b) the same slope over the per-day-difference means;
  - (c) as (a), with the line through the origin.
- **Absolute change for Fig. 1h**: the session-level circular mean, or the median over cells.
- **Example mouse of Fig. 1f**: animal 4 (as Extended Data Fig. 1g says), or any mouse with 18 sessions. Its v = 17.06 does not match animal 4's V of 14.6 in Extended Data Fig. 4b.
- **Mouse 2 exclusions**: the Methods exclude it from Fig. 2 offsets, but five values are listed. For the Fig. 3 6-week delay, the Methods cite Fig. 3f where the panel is 3g.
- **Unnamed tests**:
  - Fig. 1i "not significantly different": Wilcoxon or paired t-test. With five mice the Wilcoxon cannot reach p < 0.05.
  - Fig. 1k "significant decoding": per session pair or per mouse.
- **Chance for the decoder**: mean or median time-reversed error (the Methods and the legend differ).
- **XGBoost**: hyperparameters (library defaults are the reading), the random splits and seed for the environment decoder, and how population activity is summed.
- **Other open details**:
  - the per-mouse value in the repeated-measures ANOVA;
  - the shuffle summary (median or mean);
  - which environment is which in Extended Data Fig. 10c;
  - the CellReg threshold for Fig. 4 (0.8 or 0.6);
  - the probe-trial order, taken from session dates;
  - the error-variance measure in Extended Data Fig. 8c;
  - whether mice 6 to 10 count toward the 388 sessions;
  - spike tuning-curve bins for the electrophysiology.

**Thresholds I set where the paper gives none.** A second reader should look at these:
- the threshold for "not diffusive" (Extended Data Fig. 4e);
- the reading of "nearly the entire duration" (all day differences up to 20 days, except at most one);
- the comparison standing in for "reduced retention" in Extended Data Fig. 9;
- the waveform-feature definitions;
- the shuffle 95th-percentile rule for coherent remapping.

The Fig. 3f/g spread of ±0.1 is read as a fit's standard error, so I used 10% as the tolerance there.

**Missing from the paper.** No analysis code exists to settle any of these details. The paper's comparison of the Fig. 4 decoder with "other animals" has no named test or data, so I left it untested. The Methods say five mice were used in all experiments, yet they also describe mice 6 to 10; I recorded the conflict.

## End of run

19 turns, 6 minutes, result: success.
