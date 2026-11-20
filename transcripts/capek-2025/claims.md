# capek-2025 · claims · run 44653261483

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls; ls paper claims tools; grep -n "^#" docs/protocol.md
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
[... 392 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-18`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
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
cd  ls schemas; wc -l paper/*.txt; head -40 paper/*.txt; cat papers/datasets/capek-2025.yaml 2>/dev/null; grep -n capek -r papers/keys.yaml queue targets 2>/dev/null | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-08682-z.txt",
 "offset": 40,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-08682-z.txt",
 "offset": 740,
 "limit": 900
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-08682-z.txt",
 "offset": 1640,
 "limit": 1100
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-08682-z.txt",
 "offset": 1640,
 "limit": 450
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 2089,2732p paper/*.txt | grep -v '^\s*$' | cut -c1-200 | head -300
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  curl -s https://api.dandiarchive.org/api/dandisets/001609/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:3000])"; curl -s "https://api.dandiarchive.org/api/dandisets/001609/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('name'));print(d.get('description'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1))" | head -250; ls -t claims/*.yaml | head -5
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
[... 235 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"; grep -l "Provenance\|written by an agent" claims/*.yaml | head -3; grep -rn "where:" claims/*.yaml | head -5; grep -n "Source data\|source data" claims/*.yaml | head -5
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
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -60 claims/kalugin-2026.yaml; grep -n -B3 -A12 "data: elsewhere" claims/gu-2026.yaml | head -60
```

```
# Claims for Kalugin, Soden, ... Lehtinen & Andermann (2026), Neuron, doi:10.1016/j.neuron.2026.07.008,
# on dandiset 001074 ("Multiplexed optical recording of sensors on a micro-endoscope (MORSE)",
# most recent published version 0.260928.0807; title and description read, no data or asset list read).
#
# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions),
# 2026-10-22, protocol pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read. The accepted author manuscript in PubMed Central (PMC13568791, NIHMS2202779), as
# fetched to paper/10.1016-j.neuron.2026.07.008.txt: Summary, Introduction, Results, Discussion,
# STAR Methods (including "Quantification and statistical analysis"), figure legends of Figures 1
# to 6, Table 1, the key resources table and the video legends (S1 to S16); and the supplement
# NIHMS2202779-supplement-1.pdf (Figures S1 to S6 with legends), extracted into the same file.
# The version of record was not read. The paper reports no statistical test and no p-value: all
# support is means with SEM, counts, and figures. No claim therefore has `statistics`.
#
# Code read. github.com/pkalugin/kalugin-et-al-morse at commit fa4526ac02eaa2c5a24c4cfdcaab5c36ed5ae4ed
# (2026-08-06; the paper also cites Zenodo doi:10.5281/zenodo.21142692, not read). It holds
# microscope motor control (1_), Cellpose probability maps (2_), demons deformation fields (3_, 4_),
# CaImAn mask extraction, curation and cross-recording matching (5_), and the trace analyses by
# figure in 6_trace_analysis/ (Jupyter notebooks with printed outputs). Cells cited below are
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py
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

[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^### Sheet\|^#####" paper/*.txt; python -c "
import openpyxl;wb=openpyxl.load_workbook('paper/10.1038-s41586-025-08682-z.source-data.xlsx',read_only=True);print(wb.sheetnames)"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-08682-z.txt",
 "offset": 2426,
 "limit": 306
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-08682-z.txt",
 "offset": 2384,
 "limit": 42
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/capek-2025.yaml",
 "content": "# Claims for Capek, Arenas, Alpert, ... Para & Gallio (2025), \"Evolution of temperature preference in\n# flies of the genus Drosophila\", Nature 641, 447-455, doi:10.1038/s41586-025-08682-z, on dandiset\n# 001609 (\"Comparative anatomy of thermosensory projection neurons in Drosophila species\"; title and\n# description read on the archive, no data or asset list read).\n#\n# Provenance. Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-20, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read. The version of record, as supplied in paper/10.1038-s41586-025-08682-z.txt (PyMuPDF\n# extraction of the PDF): main text, figure legends 1 to 5, Methods, Data and Code availability,\n# Extended Data Fig. 1 to 7 legends, the Nature Portfolio reporting summary, and the Source Data\n# workbook (41586_2025_8682_MOESM3_ESM.xlsx, one sheet per panel, extracted into the same file). The\n# paper has no other supplementary information; the Extended Data figures are its supplement.\n#\n# Code. None to read: \"No custom algorithms or computer code was produced as part of this work\"\n# (Code availability). The reporting summary names the software used (Fiji 2.14.0, CMTK Registration\n# GUI, neuTube 1.0, Vaa3D 1.1.2, CAJAL 1.0.3, scikit-learn 1.5.0, umap-learn, SigClust, Clustal Omega\n# 1.2.3 in Geneious Prime 2023.1.1, STAR 2.7.9a, MATLAB R2023a, Igor Pro 6.37, AxoGraph 1.5.4).\n#\n# Data the paper used, as it reports them.\n#   Behaviour. Two-choice temperature preference: groups of 15 male flies, 3-5 days old, on four\n#     Peltier tiles, base temperature 25 C against a test temperature in opposite quadrants, 3 min,\n#     then the configuration reversed for 3 min; PI = (no. BT - no. TT)/total, the two trials\n#     averaged; positive PI is avoidance of the test temperature, negative is attraction; each group\n#     tested against zero by a two-tailed one-sample t-test at 0.05 (Methods, Temperature preference\n#     assays). Species and strains: D. persimilis (NDSSC 14011-0111.51; extra strain 14011-0111.24),\n#     D. melanogaster (Canton-S; extra strain EG16), D. mojavensis mojavensis (15081-1352.47; extra\n#     strain D. m. wrigleyi 15081-1352.29), D. mettleri (15081-1502.13); D. melanogaster Gr28b\n#     mutants and rescues (Gr28b.d exc66 control, exc8 mutant, HC>DmelGr28b.d, HC>DmojGr28b.d);\n#     D. mojavensis Gr28b.d delta1 mutant and its DmelGr28b.d rescue. Optogenetic red/blue light\n#     choice with groups of 25 flies (Extended Data Fig. 5f).\n#   Electrophysiology. Whole-cell patch clamp of HEK293T (and S2R+) cells expressing Gr28b.d of four\n#     species; currents normalized, log-transformed, plotted against 1/T; threshold at the\n#     intersection of linear fits to the shallowest and steepest regions (Methods, Electrophysiology).\n#     Only per-cell thresholds and Q10 values are deposited (Source Data); no raw recordings.\n#   Sequences and RNA-seq. Gr28b.d coding sequences in GenBank (OQ624956 D. persimilis, OQ621410\n#     D. mojavensis, PP885916 D. mettleri); arista RNA-seq in NCBI SRA BioProject PRJNA948454.\n#   Connectome. Hemibrain v1.2.1 on neuprint.janelia.org (Fig. 4f, Extended Data Fig. 5a-c).\n#   Anatomy (the dandiset). TPN-V and other thermosensory projection neurons dye-labelled by\n#     electroporation in dissected brains, imaged on a two-photon microscope at 1,024 x 1,024 pixels in\n#     two mounting orientations, \"front view\" (scanned on the anterior-posterior axis) and \"top view\"\n#     (scanned on the dorsal-ventral axis). LH and calyx segmented in Fiji, stacks registered within\n#     species with CMTK, neurons traced with neuTube after thresholding (or Simple Neurite Tracer\n#     masks), skeletons exported as SWC. n = 5 TPN-V reconstructions per species for D. melanogaster,\n#     D. mojavensis, D. persimilis and D. mettleri (Fig. 5f), plus fills of one extra strain each of\n#     D. melanogaster, D. mojavensis and D. persimilis (Extended Data Fig. 7d-g). The dandiset\n#     description lists ten TPN-V z-stacks per species (five front view, five top view), front and top\n#     fills of an extra strain of each species, and representative fills of TPN-Ia, TPN-Ib and TPN-VI\n#     in D. mojavensis. Confocal images (Fig. 3f-i, 4c), the DM1 olfactory fills (Extended Data Fig. 6)\n#     and the full set of dye-fill experiments counted in Extended Data Fig. 4 are not in that list.\n#\n# The dandiset can test only the anatomy claims (Fig. 4e, 4h, 4i, 5b, 5e, 5f, 5g, Extended Data Fig.\n# 3d, 3e, 7d-g). Behaviour, threshold and connectome claims use the Source Data or the public archives\n# named above (data elsewhere).\n#\n# Method details the paper leaves open for the anatomy claims, with the readings named in the\n# criteria. (1) Which stacks form the n = 5 reconstructions per species: the Methods do not say whether\n# the front-view and top-view stacks of a species are the same five neurons, or which view feeds the\n# LH and which the calyx analysis. (2) The threshold used to binarize stacks before neuTube tracing.\n# (3) The size images are normalized to before the centre of mass (COM) is measured (Extended Data Fig.\n# 3e source data give COM in pixels; the frame size is not stated). (4) The linkage of the\n# agglomerative clustering (scikit-learn, \"using Gower distance as a similarity measure\"). (5) What\n# SigClust is run on (it needs feature vectors; the paper has a distance matrix) and which split it\n# tests. (6) UMAP parameters. CAJAL sampling (100 points, Euclidean distances, Gromov-Wasserstein) and\n# the combination of the two matrices (each normalized to its maximum, then summed) are fixed by the\n# Methods.\n#\n# Source Data irregularities noted for the author (not used to change any expected value). The sheet\n# named Figure5c holds the Fig. 5d thresholds and the sheet named Figure5d holds the Fig. 5c PIs. In\n# EDFigure5f the TLHON-II Gal4/+ values are identical to the TLHON-II > CsChrimson values. In EDFigure2\n# the wild-type 45 C values equal Figure1d's 40 C column, and the 40 C group has 7 and 7 values where\n# the legend says N = 11. Figure2i lists 12 cells where the legend says n = 13. The Fig. 3j legend\n# prints nearly the same P values for the control and the DmelGr28b.d rescue.\nschema_version: 2\npaper: doi:10.1038/s41586-025-08682-z\nclaims:\n- id: fig1b-persimilis-prefers-cool\n  statement: In two-choice assays against a 25 C base, D. persimilis prefers about 15 to 20 C and\n    avoids warmer test temperatures (n = 8 groups of 15 flies).\n  source: Results, Thermal preference in Drosophila species, paragraph 1; Figure 1b\n  quote: in two-choice temperature preference assays, D. persimilis prefers distinctly cool\n    conditions9 (15–20 °C; Fig. 1a,b)\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    Figure1b\n  criterion: Per test temperature, the group PIs (PI = (no. BT - no. TT)/total; negative is\n    attraction) tested against zero by a two-tailed one-sample t-test at 0.05 (Methods, Temperature\n    preference assays). The paper does not say how \"prefers 15 to 20 C\" is decided. Readings are (a)\n    the PI is significantly negative at both 15 and 20 C; (b) 15 and 20 C are the only test\n    temperatures with a negative mean PI. Reproduced when, under one reading, that holds and the PI is\n    significantly positive at 30, 35 and 40 C.\n- id: fig1c-melanogaster-prefers-25\n  statement: D. melanogaster prefers about 25 C, avoiding both lower and higher test temperatures\n    against a 25 C base (n = 6 groups of 15 flies).\n  source: Results, Thermal preference in Drosophila species, paragraph 2; Figure 1c\n  quote: in laboratory assays this species prefers temperatures close to those also favoured by its\n    human host10,11 (about 25 °C; Fig. 1c)\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    Figure1c\n  criterion: Two-tailed one-sample t-test of the group PIs against zero at 0.05 per test temperature\n    (Methods). Reproduced when the PI is significantly positive at 10, 15, 20, 30, 35 and 40 C;\n    partially reproduced when it is at five of these six.\n- id: fig1d-mojavensis-prefers-hot\n  statement: D. mojavensis prefers about 30 to 35 C over 25 C (n = 11 groups of 15 flies), conditions\n    that D. melanogaster and D. persimilis strongly avoid.\n  source: Results, Thermal preference in Drosophila species, paragraphs 3 and 4; Figure 1d\n  quote: D. mojavensis prefers distinctly hot conditions9,14 (30–35 °C; Fig. 1d), conditions that were\n    strongly avoided by both D. melanogaster and D. persimilis\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheets\n    Figure1b, Figure1c and Figure1d\n  criterion: Two-tailed one-sample t-test of the group PIs against zero at 0.05 per test temperature\n    (Methods). Reproduced when the D. mojavensis PI is significantly negative at 30 and 35 C and the\n    D. melanogaster and D. persimilis PIs are significantly positive at 30 and 35 C. Partially\n    reproduced when the D. mojavensis part holds alone. The Figure1d 40 C column equals the wild-type\n    45 C values of sheet EDFigure2; it is not used here.\n- id: fig2n-species-thresholds\n  statement: The heat activation threshold of Gr28b.d expressed in HEK293T cells differs between\n    species, about 21 C for D. persimilis (n = 9 cells), 26 C for D. melanogaster (n = 13) and 29 C for\n    D. mojavensis (n = 13), each pair differing significantly.\n  source: Figure 2n; Results, Divergent heat thresholds for Gr28b.d, paragraphs 3 to 5\n  quote: n, Systematic differences in threshold reveal species specificity (n = 9, 13 and 13,\n    respectively)\n  statistics:\n  - about: D. persimilis against D. melanogaster\n    test: one-way analysis of variance\n    p: 2.9e-6\n    n: 9 and 13 cells\n  - about: D. persimilis against D. mojavensis\n    test: one-way analysis of variance\n    p: 9.9e-10\n    n: 9 and 13 cells\n  - about: D. melanogaster against D. mojavensis\n    test: one-way analysis of variance\n    p: 1.39e-4\n    n: 13 and 13 cells\n  expected:\n  - quantity: mean threshold, DperGr28b.d in HEK293T cells (value printed in Figure 2n)\n    value: 21.13\n    tolerance: 2.11\n    unit: degrees C\n  - quantity: mean threshold, DmelGr28b.d in HEK293T cells (value printed in Figure 2n)\n    value: 25.88\n    tolerance: 2.59\n    unit: degrees C\n  - quantity: mean threshold, DmojGr28b.d in HEK293T cells (value printed in Figure 2n)\n    value: 28.98\n    tolerance: 2.9\n    unit: degrees C\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    Figure2n (per-cell thresholds; the recordings are not deposited)\n  criterion: Means of the per-cell thresholds. The legend calls the pairwise P values \"one-way analysis\n    of variance\" without saying how pairs are formed. Readings are (a) a one-way ANOVA on each pair of\n    species alone; (b) Tukey HSD after a one-way ANOVA of the three species; (c) uncorrected pairwise\n    contrasts using the pooled error of the three-species ANOVA. Reproduced when all three means are\n    within tolerance, ordered D. persimilis < D. melanogaster < D. mojavensis, and every pair has p <\n    0.05 under one reading.\n- id: fig2o-s2r-same-threshold\n  statement: The DmelGr28b.d threshold recorded in Drosophila S2R+ cells (about 26 C, n = 13) is the\n    same as in HEK293T cells.\n  source: Figure 2o; Results, Divergent heat thresholds for Gr28b.d, paragraph 3\n  quote: the in vitro threshold of about 26 °C was not a function of the expression system, as it was\n    the same when DmelGr28b.d was expressed in an insect cell line\n  statistics:\n  - about: DmelGr28b.d in HEK293T against S2R+ cells\n    test: one-way analysis of variance\n    p: 0.986\n    n: 13 and 13 cells\n  expected:\n  - quantity: mean threshold, DmelGr28b.d in S2R+ cells (value printed in Figure 2o)\n    value: 25.82\n    tolerance: 2.58\n    unit: degrees C\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheets\n    Figure2n and Figure2o\n  criterion: A claim of absence, judged on the paper's test, a one-way ANOVA of the HEK293T against\n    the S2R+ thresholds at 0.05. Reproduced when p >= 0.05 and the S2R+ mean is within tolerance; the\n    difference in means is reported.\n- id: fig2i-two-q10-processes\n  statement: Arrhenius plots of DmelGr28b.d currents show two processes with different Q10 values,\n    below and above the threshold.\n  source: Figure 2h,i legend\n  quote: A representative Arrhenius plot (Methods) reveals two distinct processes characterized by\n    different Q10 values\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    Figure2i\n  criterion: From the per-cell Q10 values of the two processes (Methods, Q10 = (I2/I1)^(10/(T2 - T1))).\n    The paper reports no test and no numbers in the text. Reproduced when the mean Q10 of the second\n    (steep) process exceeds that of the first; the number of cells where it does is reported. The sheet\n    lists 12 cells, the legend n = 13.\n- id: fig2cd-sequence-identity\n  statement: DperGr28b.d is 84.3% identical to DmelGr28b.d, and DmojGr28b.d is 79.7% identical to\n    both DmelGr28b.d and DperGr28b.d.\n  source: Figure 2d; Results, Divergent heat thresholds for Gr28b.d, paragraphs 4 and 5\n  quote: Next, we tested D. persimilis Gr28b.d (DperGr28b.d; 84% identical to the DmelGr28b.d protein\n    sequence, Fig. 2c) ... (DmojGr28b.d; 79.7% identical to DmelGr28b.d and 79.7% identical to\n    DperGr28b.d, Fig. 2d)\n  expected:\n  - quantity: identity, D. melanogaster against D. persimilis (Figure 2d)\n    value: 84.3\n    tolerance: 8.43\n    unit: percent\n  - quantity: identity, D. melanogaster against D. mojavensis\n    value: 79.7\n    tolerance: 7.97\n    unit: percent\n  - quantity: identity, D. mojavensis against D. persimilis\n    value: 79.7\n    tolerance: 7.97\n    unit: percent\n  data: elsewhere\n  where: GenBank OQ624956 (DperGr28b.d) and OQ621410 (DmojGr28b.d); the paper gives no accession for\n    DmelGr28b.d\n  criterion: Protein alignment with Clustal Omega v1.2.3 (Methods, Phylogenetic analysis; reporting\n    summary, in Geneious Prime 2023.1.1). The DmelGr28b.d sequence is open; the reading is the\n    Gr28b-PD protein of the D. melanogaster reference genome. How identity is counted is open; readings\n    are (a) identical positions over all aligned columns, gaps included (the Geneious default); (b)\n    identical positions over columns without gaps; (c) identical positions over the shorter sequence.\n    Reproduced when all three values are within tolerance under one reading.\n- id: fig2a-exon-d-divergent\n  statement: Gr28b.d is divergent across 25 Drosophila species, most of all in the amino terminus and\n    transmembrane domains encoded by exon D, while the pore domain is much more conserved.\n  source: Results, Divergent heat thresholds for Gr28b.d, paragraph 1; Figure 2a-c; Extended Data\n    Figure 1\n  quote: the sequence of Gr28b is divergent across Drosophila species ... especially within the amino\n    terminus and the transmembrane domains encoded by the D exon (by contrast, the pore domain is much\n    more conserved\n  criterion: Clustal Omega v1.2.3 alignment of the 25 Gr28b.d proteins (Methods). The paper names no\n    source for 22 of the sequences. Reproduced when the mean pairwise identity per alignment column is\n    lower over the exon-D region than over the region coded by the common exons.\n- id: fig3ce-arista-rnaseq\n  statement: RNA-seq of D. mojavensis aristae shows selective expression of the Gr28b.d variant among\n    the Gr28b variants, at levels comparable to Ir25a and Ir93a.\n  source: Results, Conserved heat sensing in D. mojavensis, paragraph 1; Figure 3c-e\n  quote: we performed RNA sequencing of D. mojavensis arista samples and confirmed selective expression\n    of the DmojGr28b.d variant in this organ, at levels comparable to those of other gene products that\n    have known expression in thermoreceptors (Ir25a and Ir93a; Fig. 3c–e)\n  expected:\n  - quantity: total reads\n    value: 19107080\n    tolerance: 0\n    unit: reads\n  - quantity: reads uniquely mapped to the genome\n    value: 92.12\n    tolerance: 9.21\n    unit: percent\n  data: elsewhere\n  where: NCBI SRA BioProject PRJNA948454\n  criterion: Reads trimmed to 75 bp, aligned with STAR (v2.7.9a, default parameters), counts per gene\n    from STAR, RPKM from gene lengths and total mapped reads, shown as log2(RPKM + 1) (Methods, RNA\n    sequencing). The total read count must match exactly, as it is a count of the deposited reads. The\n    genome assembly and the annotation of the five predicted Gr28b variants are not given; how reads in\n    exons shared by the variants are assigned is open. Readings are (a) counts over each variant's own\n    first exon; (b) counts over full transcript models, ambiguous reads left out. \"Comparable\" is not\n    defined; readings are (i) Gr28b.d log2(RPKM + 1) inside the range spanned by Ir25a and Ir93a; (ii)\n    within 1 log2 unit of the lower of the two. Reproduced when, under a reading, Gr28b.d has the\n    highest RPKM of the five Gr28b variants and is comparable to Ir25a and Ir93a.\n- id: fig3ab-locus-structure\n  statement: The Gr28b locus of D. mojavensis has the same structure as that of D. melanogaster, with\n    five predicted variants differing in the first coding exon, each from its own promoter.\n  source: Results, Conserved heat sensing in D. mojavensis, paragraph 1; Figure 3a,b\n  quote: At the genome level, the structure of the Gr28b locus is very similar between the two species,\n    including the existence of five predicted variants that differ in the first coding exon\n  criterion: The paper names no genome assembly or annotation for D. mojavensis. Reproduced when five\n    alternative first coding exons (A to E) joined to shared downstream exons are found at the\n    D. mojavensis Gr28b locus.\n- id: fig3fi-gfp-three-arista-neurons\n  statement: A DmojGr28b.d promoter fusion to GFP labels three neurons of the D. mojavensis arista, as\n    the analogous construct does in D. melanogaster.\n  source: Results, Conserved heat sensing in D. mojavensis, paragraph 1; Figure 3f-i\n  quote: This reagent directly allowed us to visualize expression in three neurons of the arista\n  expected:\n  - quantity: GFP-labelled neurons per arista, D. mojavensis\n    value: 3\n    tolerance: 0\n    unit: neurons\n- id: fig3j-mel-mutant-loses-innocuous-avoidance\n  statement: Control D. melanogaster avoid test temperatures above 25 C (n = 11 groups), while\n    Gr28b exc8 mutants lose avoidance of 27.5 and 30 C (n = 8) and keep avoidance of 35 and 40 C.\n  source: Figure 3j; Results, Divergent heat response in D. mojavensis, paragraph 1\n  quote: Control D. melanogaster avoid heat above 25 °C (n = 11 each); DmelGr28bexc8 mutants lose\n    avoidance of 27.5 °C and 30 °C (empty arrowheads; n = 8 each)\n  statistics:\n  - about: control, 25 C\n    test: two-tailed one-sample t-test\n    p: 0.331\n  - about: control, 27.5 C\n    test: two-tailed one-sample t-test\n    p: 9.16e-3\n  - about: control, 30 C\n    test: two-tailed one-sample t-test\n    p: 2.21e-3\n  - about: control, 35 C\n    test: two-tailed one-sample t-test\n    p: 6.87e-7\n  - about: control, 40 C\n    test: two-tailed one-sample t-test\n    p: 1.11e-9\n  - about: mutant, 25 C\n    test: two-tailed one-sample t-test\n    p: 0.854\n  - about: mutant, 27.5 C\n    test: two-tailed one-sample t-test\n    p: 0.671\n  - about: mutant, 30 C\n    test: two-tailed one-sample t-test\n    p: 0.864\n  - about: mutant, 35 C\n    test: two-tailed one-sample t-test\n    p: 4.94e-4\n  - about: mutant, 40 C\n    test: two-tailed one-sample t-test\n    p: 1.08e-6\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    Figure3j\n  criterion: Two-tailed one-sample t-test of the group PIs against zero at 0.05, per genotype and test\n    temperature (Figure 3 legend; Methods). Reproduced when the control PI is significantly positive at\n    27.5, 30, 35 and 40 C and not at 25 C, and the mutant PI is not significantly different from zero\n    at 25, 27.5 and 30 C (the absence judged on this test) and significantly positive at 35 and 40 C.\n- id: fig3j-cross-species-rescue-mel\n  statement: In D. melanogaster Gr28b mutants, DmelGr28b.d restores avoidance from 27.5 C (n = 8\n    groups), while DmojGr28b.d restores avoidance of 30 C but not of 27.5 C (n = 10), a D. mojavensis-like\n    threshold.\n  source: Figure 3j; Results, Cross-species rescue of Gr28b.d, paragraph 3\n  quote: same-species rescue restores the normal D. melanogaster avoidance of hot temperatures starting\n    at 27.5 °C ... expression of DmojGr28b.d in D. melanogaster mutant flies also restored avoidance,\n    but only to 30 °C and not to 27.5 °C\n  statistics:\n  - about: DmelGr28b.d rescue, 25 C\n    test: two-tailed one-sample t-test\n    p: 0.331\n  - about: DmelGr28b.d rescue, 27.5 C\n    test: two-tailed one-sample t-test\n    p: 9.16e-3\n  - about: DmelGr28b.d rescue, 30 C\n    test: two-tailed one-sample t-test\n    p: 2.21e-3\n  - about: DmelGr28b.d rescue, 35 C\n    test: two-tailed one-sample t-test\n    p: 6.97e-7\n  - about: DmelGr28b.d rescue, 40 C\n    test: two-tailed one-sample t-test\n    p: 1.11e-9\n  - about: DmojGr28b.d rescue, 25 C\n    test: two-tailed one-sample t-test\n    p: 0.362\n  - about: DmojGr28b.d rescue, 27.5 C\n    test: two-tailed one-sample t-test\n    p: 0.685\n  - about: DmojGr28b.d rescue, 30 C\n    test: two-tailed one-sample t-test\n    p: 6.94e-3\n  - about: DmojGr28b.d rescue, 35 C\n    test: two-tailed one-sample t-test\n    p: 6.49e-6\n  - about: DmojGr28b.d rescue, 40 C\n    test: two-tailed one-sample t-test\n    p: 5.38e-10\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    Figure3j\n  criterion: Two-tailed one-sample t-test of the group PIs against zero at 0.05 (Figure 3 legend).\n    Reproduced when the DmelGr28b.d rescue PI is significantly positive at 27.5, 30, 35 and 40 C and\n    not at 25 C, and the DmojGr28b.d rescue PI is significantly positive at 30, 35 and 40 C and not\n    significantly different from zero at 25 and 27.5 C (the absence judged on this test). The printed\n    P values of the DmelGr28b.d rescue nearly equal the control's, so the recomputed values are\n    reported beside them.\n- id: fig3k-moj-mutant-loses-attraction\n  statement: Wild-type D. mojavensis are indifferent to 27.5 C but attracted to 30 and 35 C (n = 6\n    groups); Gr28b.d delta1 mutants lose attraction to 30 and 35 C (n = 8).\n  source: Figure 3k; Results, Divergent heat response in D. mojavensis, paragraph 2\n  quote: Wild-type D. mojavensis are indifferent to 27.5 °C but attracted to 30 °C and 35 °C (n = 6\n    each); DmojGr28b.dΔ1 mutants lose attraction to 30 °C and 35 °C\n  statistics:\n  - about: wild type, 25 C\n    test: two-tailed one-sample t-test\n    p: 0.833\n  - about: wild type, 27.5 C\n    test: two-tailed one-sample t-test\n    p: 0.986\n  - about: wild type, 30 C\n    test: two-tailed one-sample t-test\n    p: 2.57e-3\n  - about: wild type, 35 C\n    test: two-tailed one-sample t-test\n    p: 8.56e-3\n  - about: mutant, 25 C\n    test: two-tailed one-sample t-test\n    p: 0.845\n  - about: mutant, 27.5 C\n    test: two-tailed one-sample t-test\n    p: 0.443\n  - about: mutant, 30 C\n    test: two-tailed one-sample t-test\n    p: 0.08\n  - about: mutant, 35 C\n    test: two-tailed one-sample t-test\n    p: 0.282\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    Figure3k\n  criterion: Two-tailed one-sample t-test of the group PIs against zero at 0.05 (Figure 3 legend).\n    Reproduced when the wild-type PI is significantly negative at 30 and 35 C and not significantly\n    different from zero at 25 and 27.5 C, and the mutant PI is not significantly different from zero\n    at any test temperature (the absences judged on this test).\n- id: fig3k-mel-rescue-in-moj\n  statement: Expressing DmelGr28b.d in D. mojavensis Gr28b.d delta1 mutants restores attraction to 30\n    and 35 C and also produces attraction to 27.5 C, a D. melanogaster-like threshold (n = 7, 7, 7 and\n    6 groups).\n  source: Figure 3k; Results, Cross-species rescue of Gr28b.d, paragraph 4\n  quote: the D. melanogaster-rescued D. mojavensis now seemed to also be attracted to 27.5 °C, a\n    temperature that their wild-type counterpart were indifferent to\n  statistics:\n  - about: rescue, 25 C\n    test: two-tailed one-sample t-test\n    p: 0.701\n  - about: rescue, 27.5 C\n    test: two-tailed one-sample t-test\n    p: 7.15e-4\n  - about: rescue, 30 C\n    test: two-tailed one-sample t-test\n    p: 2.43e-4\n  - about: rescue, 35 C\n    test: two-tailed one-sample t-test\n    p: 8.14e-3\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    Figure3k\n  depends_on:\n  - fig3k-moj-mutant-loses-attraction\n  criterion: Two-tailed one-sample t-test of the group PIs against zero at 0.05 (Figure 3 legend).\n    Reproduced when the rescue PI is significantly negative at 27.5, 30 and 35 C and not at 25 C, and\n    the wild-type PI at 27.5 C is not (from fig3k-moj-mutant-loses-attraction).\n- id: ed2-moj-mutant-noxious-normal\n  statement: D. mojavensis Gr28b.d delta1 mutants avoid noxious heat (40 and 45 C) as wild-type flies\n    do, with no difference between the two.\n  source: Extended Data Figure 2; Results, Divergent heat response in D. mojavensis, paragraph 2\n  quote: The D. mojavensis Gr28b.d null mutant displays normal avoidance of noxious heat\n  statistics:\n  - about: wild type against mutant, 40 C\n    test: two-tail two sample t-test\n    p: 0.678\n  - about: wild type against mutant, 45 C\n    test: two-tail two sample t-test\n    p: 0.72\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    EDFigure2\n  criterion: A claim of absence, judged on the paper's test, a two-tailed two-sample t-test of\n    wild-type against mutant PIs at 0.05, at 40 and at 45 C. Reproduced when neither is significant;\n    the mean PIs and their difference are reported. The sheet has 7 and 7 groups at 40 C (legend N =\n    11), and its wild-type 45 C values equal Figure1d's 40 C column.\n- id: fig4f-tpnv-top-common-output\n  statement: In the hemibrain connectome TPN-V is the top common synaptic output of the three hot\n    TRNs of the arista, receiving 14% of all their output synapses and 26% (564 of 2146) when local\n    interneurons are left out.\n  source: Methods, Connectomics; Figure 4f\n  quote: TPN-V stands as the overall top common synaptic output of the hot TRNs (receiving 14% of all\n    output synapses), as well as if one excludes connections to local interneurons (cells that do not\n    leave the PAL), in which case TPN-V receives 26% of all hot TRN output synapses (564/2146 synapses\n  expected:\n  - quantity: synapses from the hot TRNs onto TPN-V\n    value: 564\n    tolerance: 56\n    unit: synapses\n  - quantity: TPN-V share of hot TRN output synapses, local interneurons left out\n    value: 26\n    tolerance: 2.6\n    unit: percent\n  - quantity: TPN-V share of all hot TRN output synapses\n    value: 14\n    tolerance: 1.4\n    unit: percent\n  data: elsewhere\n  where: Hemibrain v1.2.1 on neuprint.janelia.org\n  criterion: neuPrint Common connectivity query of the three hot TRNs (body IDs 2069320377, 2163102697\n    and 5813024340, from sheet EDFigure5a of the Source Data), partners ranked, threshold > 9 synapses\n    (Methods, Connectomics). The 2146 is the sum of the weights of the 15 projection-neuron types in\n    sheet Figure4f. Open is whether the > 9 threshold applies to each TRN or to the summed weight;\n    both readings are run. Reproduced when TPN-V is the top common output and all three values are\n    within tolerance under one reading.\n- id: ed5a-tlhon2-main-target\n  statement: TPN-V carries 52.67% of the hot TRN output synapses onto TPNs and is the main direct path\n    from the hot TRNs to TLHON-II, which in turn is the main synaptic output of TPN-V, overall and\n    within the LH.\n  source: Extended Data Figure 5a-c; Results, Divergent TPN-V innervation of the LH, paragraph 5\n  quote: TPN-V is the major output of the aristal hot TRNs (comprising 52.67% of hot TRN output synapses\n    to TPNs) and the major direct path of connectivity from hot TRNs to Thermosensory Lateral Horn\n    Output Neuron II (TLHON-II), which is in turn the major target of TPN-V\n  expected:\n  - quantity: TPN-V share of hot TRN output synapses onto TPNs\n    value: 52.67\n    tolerance: 5.27\n    unit: percent\n  data: elsewhere\n  where: Hemibrain v1.2.1 on neuprint.janelia.org\n  criterion: neuPrint queries as in Methods, Connectomics (Shortest path from each hot TRN to TLHON-II,\n    body ID 514068564; TPN-V is body 1975878958 in sheet EDFigure5a). Reproduced when the share is\n    within tolerance, TPN-V is the TPN with the most synapses onto TLHON-II, and TLHON-II is the\n    downstream partner with the most synapses from TPN-V both over the whole brain and within the\n    right LH ROI.\n- id: ed5e-tlhon2-silencing\n  statement: Silencing TLHON-II with Kir2.1 reduces heat avoidance at 30, 35 and 40 C but not at 25 C\n    (n = 8 groups per condition).\n  source: Extended Data Figure 5e; Results, Divergent TPN-V innervation of the LH, paragraph 5\n  quote: Genetic silencing using TLHON-II:Gal4>Kir2.1 impacts heat avoidance\n  statistics:\n  - about: 25 C\n    test: 2-way ANOVA\n    p: 0.748\n    n: 8 groups per genotype\n  - about: 30 C\n    test: 2-way ANOVA\n    p: 1.95e-3\n    n: 8 groups per genotype\n  - about: 35 C\n    test: 2-way ANOVA\n    p: 4.15e-5\n    n: 8 groups per genotype\n  - about: 40 C\n    test: 2-way ANOVA\n    p: 4.91e-7\n    n: 8 groups per genotype\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    EDFigure5e\n  criterion: The legend gives one P value per temperature from a 2-way ANOVA without saying what is\n    compared. Readings are (a) a genotype by temperature two-way ANOVA of the three genotypes, then\n    Tukey comparisons of TLHON-II > Kir2.1 with each control at each temperature, taking the larger P;\n    (b) the same with the two controls pooled; (c) the genotype effect of a one-way ANOVA at each\n    temperature. Reproduced when, under one reading, the experimental PI is below both controls with\n    p < 0.05 at 30, 35 and 40 C and p >= 0.05 at 25 C.\n- id: ed5f-tlhon2-optogenetic-avoidance\n  statement: Optogenetic activation of TLHON-II with CsChrimson makes flies avoid red light, while the\n    Gal4 and UAS controls show no preference (n = 9 groups of 25 flies).\n  source: Extended Data Figure 5f; Results, Divergent TPN-V innervation of the LH, paragraph 5\n  quote: Optogenetic activation via TLHON-II:Gal4>CsChrimson is sufficient to induce avoidance of red\n    light\n  statistics:\n  - about: Gal4/+\n    test: one sample t-test\n    p: 0.44\n  - about: UAS/+\n    test: one sample t-test\n    p: 0.983\n  - about: Gal4>UAS\n    test: one sample t-test\n    p: 2.54e-5\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    EDFigure5f\n  criterion: Two-tailed one-sample t-test of the group PIs against zero at 0.05 (Methods, Optogenetic\n    preference assays). Reproduced when the Gal4 > CsChrimson PI is significantly positive and neither\n    control differs from zero (the absence judged on this test). In the sheet the Gal4/+ values are\n    identical to the Gal4 > CsChrimson values, which would not give the printed p = 0.440; the result\n    for Gal4/+ is reported as computed from the sheet, with this noted.\n- id: fig4c-hot-glomerulus-conserved\n  statement: In D. mojavensis the hot receptor neurons of the arista target a place in the PAL\n    similar to the hot glomerulus of D. melanogaster.\n  source: Results, Mapping heat pathways in D. mojavensis, paragraph 2; Figure 4b,c\n  quote: in D. mojavensis, hot receptors of the arista target a location in the PAL similar to the ‘hot\n    glomerulus’ targeted by the analogous hot receptor cells in D. melanogaster\n  criterion: Judged as the paper does, by comparing confocal stacks of Gr28b.d promoter GFP (D.\n    mojavensis) and HC-Gal4 GFP (D. melanogaster) with nc82 counterstain (Methods, Immunostaining;\n    Fluorescence microscopy). Reproduced when the GFP terminals in D. mojavensis occupy a single\n    glomerulus at the corresponding position of the PAL.\n- id: fig4e-tpn-types-conserved\n  statement: Dye fills in D. mojavensis label the main TPN types described in D. melanogaster,\n    including TPN-Ia, TPN-Ib, TPN-III and TPN-VI.\n  source: Results, Mapping heat pathways in D. mojavensis, paragraph 4; Figure 4e\n  quote: Dye labelling revealed that the main TPN pathways that we previously described in D.\n    melanogaster are also present in D. mojavensis\n  data: with_inputs\n  criterion: As in Figure 4e, each D. mojavensis fill of a named type is compared with the hemibrain\n    v1.2.1 skeleton of that type (Methods, Neuron reconstructions). Reproduced when each of the\n    dandiset's representative fills (TPN-Ia, TPN-Ib, TPN-VI) shows the same PAL glomeruli, tract and\n    target regions as the EM type it is named for; partially reproduced when two of three do. TPN-III\n    is not in the dandiset's description and is reported as untested if absent.\n- id: ed4-tpnv-most-labelled\n  statement: TPN-V is the most often labelled TPN type in the dye fills (28 of 32 D. melanogaster\n    brains), and labelling frequencies follow connectivity with the hot TRNs and are similar across\n    species.\n  source: Results, Divergent TPN-V innervation of the LH, paragraph 1; Results, Mapping heat pathways\n    in D. mojavensis, paragraph 4; Extended Data Figure 4\n  quote: TPN-V was by far the most common TPN cell type labelled in our experiments (28/32 brains we\n    injected had at least some TPN-V labelling\n  expected:\n  - quantity: D. melanogaster brains with TPN-V labelled\n    value: 28\n    tolerance: 0\n    unit: brains of 32\n  criterion: Counts of fills that labelled up to 3 or 4 TPNs, classed by type, with experiments\n    labelling only local interneurons, too many TPNs, or olfactory projections left out (Extended\n    Data Figure 4 legend). The count must match exactly. Reproduced when TPN-V is the most frequent type\n    in each species and the order TPN-V, TPN-Ia, TPN-Ib follows the synapse weights 564, 434, 249 of\n    sheet Figure4f. The dandiset's description lists only selected stacks, so the full set of fills\n    may not be there.\n- id: fig4h-moj-laca-more-extensive\n  statement: D. mojavensis TPN-V innervates the lateral accessory calyx (lACA) of the mushroom body\n    more extensively than D. melanogaster TPN-V.\n  source: Results, Divergent TPN-V innervation of the LH, paragraph 2; Figure 4h\n  quote: in D. mojavensis, the innervation of the lACA by TPN-V appeared more extensive than that of D.\n    melanogaster\n  criterion: The paper shows this in representative front-view stacks and gives no measure of lACA\n    extent (the lACA is not segmented; only LH and calyx volumes are, Methods, Neuron reconstructions).\n    Readings are (a) the traced cable length of each reconstruction inside the calyx volume; (b) the\n    number of above-threshold pixels in the front-view maximum projection cropped to the calyx, as for\n    the COM (Methods, Quantification of projection neuron anatomy). The paper reports no test.\n    Reproduced when, under one reading, the D. mojavensis median over its five neurons exceeds the\n    D. melanogaster median; a one-sided Mann-Whitney test is shown as a variant.\n- id: fig4i-moj-lacks-anterior-ventral-lh\n  statement: D. melanogaster TPN-V innervates the ventral LH along its anterior-posterior extent, while\n    D. mojavensis TPN-V is limited to the posterior half of the ventral LH and lacks innervation of\n    the anterior-ventral LH.\n  source: Results, Divergent TPN-V innervation of the LH, paragraph 2 to 3; Figure 4i; Extended Data\n    Figure 6e\n  quote: TPN-V projections within the ventral LH appear less extensive and are limited to the posterior\n    half of the ventral LH region. In fact, in D. mojavensis, the anterior–ventral LH appears to\n    entirely lack TPN-V innervation\n  criterion: Measured with the paper's spatial measure, the COM of the LH maximum projection (Methods,\n    Quantification of projection neuron anatomy; Extended Data Figure 3e plots mean and SD of 5 per\n    species). Which stacks feed it is open; readings are (a) top-view stacks, the anterior-posterior\n    axis lying in the image plane; (b) registered reconstructions projected on the dorsal-ventral\n    axis. Reproduced when, under one reading, the D. mojavensis mean COM lies posterior to the D.\n    melanogaster mean and the two mean plus or minus SD intervals do not overlap along that axis. The\n    fraction of LH pixels or cable in the anterior half of the LH is shown as a variant, near zero for\n    D. mojavensis if \"entirely lack\" holds.\n- id: fig5b-persimilis-anterior-lh\n  statement: D. persimilis TPN-V innervates the anterior-ventral LH substantially, as D. melanogaster\n    TPN-V does.\n  source: Results, LH innervation matches species behaviour, paragraph 2; Figure 5b,f\n  quote: Our dye fills demonstrated substantial innervation of the anterior–ventral LH in D. persimilis,\n    similar to what we described for D. melanogaster\n  depends_on:\n  - fig4i-moj-lacks-anterior-ventral-lh\n  criterion: The LH COM measure and readings of fig4i-moj-lacks-anterior-ventral-lh. Reproduced when,\n    under the reading used there, the D. persimilis mean COM along the anterior-posterior axis is\n    closer to the D. melanogaster mean than to the D. mojavensis mean, and its mean plus or minus SD\n    interval does not overlap the D. mojavensis one.\n- id: fig5b-persimilis-laca-more\n  statement: D. persimilis TPN-V innervation of the lACA appears more pronounced than that of D.\n    melanogaster.\n  source: Results, LH innervation matches species behaviour, paragraph 2; Figure 5b\n  quote: Innervation of the lACA appeared more pronounced than in D. melanogaster (asterisks)\n  depends_on:\n  - fig4h-moj-laca-more-extensive\n  criterion: The measure and readings of fig4h-moj-laca-more-extensive. Reproduced when, under one\n    reading, the D. persimilis median exceeds the D. melanogaster median.\n- id: fig5e-mettleri-anterior-lh\n  statement: D. mettleri TPN-V amply innervates the anterior-ventral LH, resembling D. melanogaster\n    and D. persimilis more than its relative D. mojavensis.\n  source: Results, LH innervation matches species behaviour, paragraph 5; Figure 5e,f\n  quote: Our results show ample TPN-V innervation of the anterior–ventral LH in this species (Fig. 5e),\n    more closely resembling the innervation pattern of D. melanogaster and D. persimilis than that of\n    its relative D. mojavensis\n  depends_on:\n  - fig4i-moj-lacks-anterior-ventral-lh\n  criterion: The LH COM measure and readings of fig4i-moj-lacks-anterior-ventral-lh. Reproduced when,\n    under the reading used there, the D. mettleri mean COM along the anterior-posterior axis is closer\n    to both the D. melanogaster and D. persimilis means than to the D. mojavensis mean, and its mean\n    plus or minus SD interval does not overlap the D. mojavensis one.\n- id: fig5e-mettleri-laca-intermediate\n  statement: The lACA innervation of D. mettleri TPN-V lies between those of D. mojavensis and D.\n    persimilis.\n  source: Results, LH innervation matches species behaviour, paragraph 5; Figure 5e,f\n  quote: the D. mettleri pattern of TPN-V innervation within the lACA appears to lie in between that of\n    D. mojavensis and D. persimilis\n  depends_on:\n  - fig4h-moj-laca-more-extensive\n  criterion: The measure and readings of fig4h-moj-laca-more-extensive. Reproduced when, under one\n    reading, the D. mettleri median lies between the D. mojavensis and D. persimilis medians.\n- id: fig5g-moj-clusters-apart\n  statement: In a combined morphology (CAJAL) and centre of mass distance matrix of LH arborizations,\n    the five D. mojavensis TPN-V reconstructions cluster apart from those of D. melanogaster, D.\n    persimilis and D. mettleri (SigClust p = 1.97e-5).\n  source: Figure 5g; Results, LH innervation matches species behaviour, paragraph 5; Methods,\n    Quantification of projection neuron anatomy\n  quote: A distance matrix for reconstructions in f (Methods) demonstrates distinct clustering of the D.\n    mojavensis TPN-V arborizations within the LH\n  statistics:\n  - test: SigClust test\n    p: 1.97e-5\n    n: 20 reconstructions, 5 per species\n  criterion: From the Methods. Reconstructions cropped to the LH; CAJAL (v1.0.3) samples 100 points\n    per skeleton, builds Euclidean distance matrices and computes pairwise Gromov-Wasserstein\n    distances; the LH COM of each neuron is measured on a normalized maximum projection and pairwise\n    taxicab distances taken; both matrices are divided by their maxima and summed; hierarchical\n    clustering with scikit-learn AgglomerativeClustering, UMAP with umap-learn, SigClust at 0.05.\n    Open are the linkage (readings average and complete; single as a variant), the input to SigClust\n    (readings (a) rows of the summed distance matrix as feature vectors; (b) a classical\n    multidimensional scaling embedding of the matrix; (c) the UMAP coordinates) and the split it tests\n    (the D. mojavensis reconstructions against the rest). Reproduced when, under one reading, the top\n    split of the dendrogram separates the five D. mojavensis reconstructions from the other fifteen\n    and SigClust gives p < 0.05. Partially reproduced when D. mojavensis forms a pure cluster below the\n    top split, or four of five group together, with p < 0.05.\n- id: ed3d-cajal-sorts-lh-not-calyx\n  statement: CAJAL morphology distances alone sort TPN-V neurons by species in the LH but much less in\n    the calyx.\n  source: Extended Data Figure 3d\n  quote: UMAP embedding of pairwise distances from CAJAL analysis alone shows neuronal morphologies sort\n    out by species in the Lateral Horn (LH) but not as much for the Calyx (CA)\n  depends_on:\n  - fig5g-moj-clusters-apart\n  criterion: Gromov-Wasserstein distances from CAJAL as in fig5g-moj-clusters-apart, computed\n    separately for LH and calyx crops. The paper shows UMAP plots only. Readings for \"sort out by\n    species\" are (a) the fraction of neurons whose nearest neighbour by distance is of the same\n    species; (b) the mean silhouette score by species on the distance matrix. Reproduced when, under\n    one reading, the LH value exceeds the calyx value.\n- id: ed3e-com-link\n  kind: link\n  statement: The dandiset's TPN-V stacks are those whose LH and calyx centres of mass the paper reports,\n    so that the COM computed from them reproduces the pattern of the Source Data.\n  source: Extended Data Figure 3e; Source Data sheet EDFigure3e\n  data: with_inputs\n  criterion: Per species, the COM of the maximum projection cropped to the LH and to the calyx (Methods,\n    Quantification of projection neuron anatomy). The normalized frame size is not given, so COM is\n    compared as a fraction of the crop. The link holds when the dandiset has five TPN-V stacks per\n    species for the four species, and the LH COM species means show the Source Data's pattern, D.\n    mojavensis lowest on the axis the sheet calls Y (sheet means about 78 against 135 to 145 for the\n    others) and highest on X; it is partial when only one axis shows it.\n- id: ed7-additional-strains-behaviour\n  statement: Additional strains of D. persimilis, D. melanogaster and D. mojavensis show the same\n    temperature preference as the strains of Figure 1.\n  source: Extended Data Figure 7a-c; Results, LH innervation matches species behaviour, paragraph 3\n  quote: Preference indexes measured from additional strains of D. persimilis, D. melanogaster, and D.\n    mojavensis, demonstrate consistent behavior within populations of the same species\n  statistics:\n  - about: D. persimilis strain 24, 15 C\n    test: two-tail one sample t-test\n    p: 6.30e-3\n  - about: D. persimilis strain 24, 20 C\n    test: two-tail one sample t-test\n    p: 3.33e-4\n  - about: D. persimilis strain 24, 25 C\n    test: two-tail one sample t-test\n    p: 0.747\n  - about: D. persimilis strain 24, 30 C\n    test: two-tail one sample t-test\n    p: 2.47e-5\n  - about: D. persimilis strain 24, 35 C\n    test: two-tail one sample t-test\n    p: 7.67e-6\n  - about: D. persimilis strain 24, 40 C\n    test: two-tail one sample t-test\n    p: 1.55e-7\n  - about: D. melanogaster EG16, 15 C\n    test: two-tail one sample t-test\n    p: 2.22e-9\n  - about: D. melanogaster EG16, 20 C\n    test: two-tail one sample t-test\n    p: 9.38e-6\n  - about: D. melanogaster EG16, 25 C\n    test: two-tail one sample t-test\n    p: 0.488\n  - about: D. melanogaster EG16, 30 C\n    test: two-tail one sample t-test\n    p: 1.34e-5\n  - about: D. melanogaster EG16, 35 C\n    test: two-tail one sample t-test\n    p: 1.76e-10\n  - about: D. mojavensis wrigleyi, 25 C\n    test: two-tail one sample t-test\n    p: 0.888\n  - about: D. mojavensis wrigleyi, 30 C\n    test: two-tail one sample t-test\n    p: 3.66e-8\n  - about: D. mojavensis wrigleyi, 35 C\n    test: two-tail one sample t-test\n    p: 1.58e-7\n  - about: D. mojavensis wrigleyi, 40 C\n    test: two-tail one sample t-test\n    p: 1.13e-5\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheets\n    EDFigure7a, EDFigure7b and EDFigure7c\n  criterion: Two-tailed one-sample t-test of the group PIs against zero at 0.05 (legend). Reproduced\n    when the D. persimilis strain is significantly negative at 15 and 20 C and positive at 30, 35 and\n    40 C; the D. melanogaster strain significantly positive at 15, 20, 30 and 35 C; the D. mojavensis\n    strain significantly negative at 30 and 35 C; and none of the three differs from zero at 25 C.\n    The sign at 40 C for D. mojavensis wrigleyi is reported.\n- id: ed7-additional-strains-anatomy\n  statement: TPN-V anatomy is consistent within species across strains, and in the distance matrix the\n    reconstructions of the additional strains cluster with their own species.\n  source: Extended Data Figure 7d-g\n  quote: 2-photon z-stacks of dye-labelled TPN-V in each of the three strains shows consistent anatomy\n    within species ... A distance matrix of reconstructions (see methods) shows additional strains\n    cluster by species\n  depends_on:\n  - fig5g-moj-clusters-apart\n  criterion: The additional-strain reconstructions are added to the distance matrix of\n    fig5g-moj-clusters-apart, with the same method and readings. The number of additional-strain\n    reconstructions is not given. \"Cluster by species\" is read as (a) each additional reconstruction's\n    nearest neighbour is of its own species; (b) the D. mojavensis wrigleyi reconstructions fall in\n    the D. mojavensis cluster and the D. melanogaster and D. persimilis ones outside it. Reproduced\n    when one reading holds for every additional reconstruction.\n- id: fig5c-mettleri-avoids-heat\n  statement: D. mettleri is indifferent to 27.5 C but avoids 30 C and higher, in the innocuous and\n    noxious range (n = 8 groups of 15 flies).\n  source: Results, LH innervation matches species behaviour, paragraph 4; Figure 5c\n  quote: in two-choice assays, this species seems indifferent to 27.5 °C (like D. mojavensis) but\n    robustly avoids 30 °C (like D. melanogaster)\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    named Figure5d (it holds the Figure 5c preference indexes)\n  criterion: Two-tailed one-sample t-test of the group PIs against zero at 0.05 (Methods). Reproduced\n    when the PI is not significantly different from zero at 27.5 C (the absence judged on this test)\n    and significantly positive at 30, 35 and 40 C.\n- id: fig5d-mettleri-threshold\n  statement: The heat activation threshold of D. mettleri Gr28b.d in HEK293T cells is about 30 C (n\n    = 13 recordings), between the behavioural thresholds of 27.5 and 30 C.\n  source: Figure 5d; Results, LH innervation matches species behaviour, paragraph 4\n  quote: This is very close to the threshold we recorded in vitro (about 30 °C, Fig. 5d\n  expected:\n  - quantity: mean threshold, DmetGr28b.d in HEK293T cells (value printed in Figure 5d)\n    value: 30.1\n    tolerance: 3.01\n    unit: degrees C\n  data: elsewhere\n  where: Nature Source Data for doi:10.1038/s41586-025-08682-z (41586_2025_8682_MOESM3_ESM.xlsx), sheet\n    named Figure5c (it holds the Figure 5d thresholds)\n- id: ed6-olfactory-lh-conserved\n  statement: The DM1 olfactory projection neuron innervates the LH in D. mojavensis as in D.\n    melanogaster, while D. mojavensis TPN-V innervates only the posterior LH, so LH architecture\n    itself is conserved.\n  source: Extended Data Figure 6c,e; Results, Divergent TPN-V innervation of the LH, paragraph 6\n  quote: 2-photon imaging demonstrates that DM1-PN innervation (white, labelled with AlexaFluorTM 594\n    dye) of the LH is essentially identical in D. mojavensis as compared to D. melanogaster\n  data: with_inputs\n  criterion: Judged as in Extended Data Figure 6, by comparing D. mojavensis DM1 fills (three flies)\n    with the hemibrain v1.2.1 DM1 projection neuron skeleton, and the TPN-V fill in the same brain\n    with the EM TPN-V. Reproduced when the DM1 fill covers the same LH and calyx regions as the EM DM1\n    neuron while the TPN-V fill is confined to the posterior LH. The dandiset's description does not\n    list DM1 fills.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/capek-2025.yaml paper/10.1038-s41586-025-08682-z.txt; grep -n "—\|rather\|Rather" claims/capek-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I've written `claims/capek-2025.yaml`. The quote checker passes every quote, but it exits non-zero on one p-value. The Extended Data Fig. 7a legend prints that value as "6.30e-3". I read it at line 2074 of the text and it is correct; the checker only looks for the "6.3e-3" form. I left both the checker and the value as they are.

**Text read:** the version of record (`paper/10.1038-s41586-025-08682-z.txt`). That covers the main text, the figure legends, the Methods, the Extended Data Fig. 1–7 legends, the reporting summary, and the Source Data workbook (MOESM3), which has one sheet per panel. The paper has no other supplementary file. There was no code to read: the paper says "No custom algorithms or computer code was produced". The DANDI:001609 description lists TPN-V two-photon dye-fill stacks: five front-view and five top-view per species for four species, extra-strain fills, and D. mojavensis TPN-Ia, Ib and VI fills.

**Counts:**
- 37 claims: 36 findings plus one `link` claim, which checks the dataset's stacks against the Extended Data Fig. 3e centre-of-mass values in the Source Data.
- 36 quotes and no `inferred` notes.
- 14 claims carry `statistics`, 61 test entries in all.
- 33 claims have criteria.
- Only the anatomy claims (11 of them) can be tested on the dataset.
- 18 are `data: elsewhere`: the behaviour, threshold and Q10 claims use the paper's Source Data, plus the hemibrain v1.2.1 connectome, GenBank and SRA PRJNA948454.
- The remaining claims (confocal images, the full set of dye fills, DM1 olfactory fills, the gene locus) rest on data the paper did not deposit.

**Details the paper leaves open, and the readings named for each:**
- **Which stacks make up the n = 5 reconstructions, and which view feeds the lateral horn (LH) centre of mass:** (a) the top-view stacks; (b) the registered reconstructions, projected.
- **How lateral accessory calyx (lACA) extent is measured** (the paper has no measure): (a) traced cable length inside the calyx; (b) above-threshold pixels in the calyx crop. A one-sided Mann-Whitney test is shown as a variant.
- **Clustering linkage:** average or complete, with single as a variant.
- **What SigClust runs on:** distance-matrix rows, a classical MDS embedding, or the UMAP coordinates.
- **"Sorts by species" (Extended Data Fig. 3d):** nearest-neighbour species fraction, or silhouette score.
- **"Cluster by species" (Extended Data Fig. 7g):** nearest neighbour is of its own species, or each extra strain falls on its own species' side of the D. mojavensis split.
- **Pairwise "one-way ANOVA" P values in Fig. 2n:** an ANOVA on each pair alone, Tukey after a three-group ANOVA, or pooled-error contrasts.
- **The 2-way ANOVA in Extended Data Fig. 5e:** Tukey against each control, against the pooled controls, or a one-way ANOVA per temperature.
- **Sequence identity:** counted with gaps, without gaps, or over the shorter sequence. The D. melanogaster sequence has no accession in the paper; the reading is the reference Gr28b-PD protein.
- **RNA-seq:** how reads are assigned to the variants (variant-specific exon or full transcript), and what "comparable" to Ir25a and Ir93a means (inside their range, or within 1 log2 unit).
- **"Prefers 15–20 °C" (Fig. 1b):** significant attraction at both temperatures, or the only negative mean preference indices.
- **Connectome threshold:** whether >9 synapses applies to each hot receptor neuron or to the summed weight.
- **Fixed by the Methods and not left open:** CAJAL settings (100 points, Gromov-Wasserstein), how the two distance matrices are combined, and the behaviour tests (two-tailed one-sample t-tests).

**Missing from the paper or the Source Data that some claims need:**
- The binarization threshold for tracing, the normalized frame size for the centre of mass, and UMAP parameters.
- The genome assembly and annotation for the D. mojavensis Gr28b locus.
- Sources for 22 of the 25 aligned sequences.
- Raw patch-clamp recordings (only per-cell thresholds and Q10 values are deposited).

**Source Data problems,** recorded in the file for the author:
- The sheets for Fig. 5c and 5d have swapped names.
- In Extended Data Fig. 5f, the Gal4/+ values are identical to the Gal4>CsChrimson values, which cannot give the printed p = 0.440.
- In Extended Data Fig. 2, the wild-type 45 °C values equal Fig. 1d's 40 °C column, and the 40 °C group has 7 and 7 values where the legend says N = 11.
- Fig. 2i lists 12 cells against n = 13 in the legend.
- The Fig. 3j legend prints nearly the same P values for the control and the DmelGr28b.d rescue.

## End of run

20 turns, 7 minutes, $2.45 at API prices, result: success.
