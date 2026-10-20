# 000582 · claims · run 39470465287

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls claims/001453/ claims/000582/ paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 170
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-10`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. It is written from the pilot attempts
7	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
8	
9	An attempt has three roles, each a separate run with a separate context:
10	
11	- The **reader** reads the paper and writes the claims file: every finding,
12	  and how each is to be tested, taken from the paper. A second reader checks
13	  it against the paper. Readers never see the dandiset's data.
14	- The **author** tests the claims on the dandiset. It reads the paper to
15	  understand the claims, but the claims file binds it: it cannot change a
16	  claim, and it asks a reader for any method detail the file lacks.
17	- The **verifier** checks the author's work and must not be the author.
18	
19	So every claim and its method are fixed from the paper before anyone analyses
20	the data, and no method is chosen by the agent that runs the analysis.
[... 150 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
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

**Agent calls Read**

```json
{
 "file_path": "claims/000582/10.1126-science.1125572.yaml"
}
```

```
1	# Claims for Sargolini et al. (2006) on dandiset 000582.
2	# Source: the paper's abstract. The paper is not open access, so no
3	# figure-level claims are listed.
4	# Quotes from the abstract added 2026-10-19 where it states the finding; the rest are marked
5	# inferred (no open full text).
6	# Quotes and statistics added 2026-10-20 from the full text (PDF of the version of record, and its
7	# supplement).
8	schema_version: 2
9	dataset:
10	  archive: dandi
11	  id: "000582"
12	paper: doi:10.1126/science.1125572
13	claims:
14	- id: layer2-grid
15	  statement: Layer II of the medial entorhinal cortex was predominated by grid cells.
16	  source: Main text, paragraph 2; Fig. 1D; table S1A
17	  quote: The proportion of cells with a sinusoidal modulation was layer-dependent (Fig. 1D and table
18	    S1). Whereas most well-separated layer II cells had strongly periodic firing fields, only a
19	    smaller proportion of the deeper neurons had such characteristics
20	- id: deep-hd-conjunctive
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat paper/10.1126-science.1125572.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.1125572.txt",
 "offset": 40,
 "limit": 1000
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk 'NR>1039' 10.1126-science.1125572.txt | grep -n -v -E '^\s*-?[0-9.]+\s*$|^\s*$|^(Correlation \(r\)|Rotation \(deg\))\s*$' | head -400
```

```
3:2. Supporting figures
4:Sargolini et al.
6:=== page 11 ===
7:Fig. S2: Discharge profile of grid cells in each principal cell layer of MEC. 
8:Grid cells were defined as in Fig. 1D.  Data are from all 17 rats, except directional information and angular 
9:deviation, which are shown only for the 9 rats tested with two LEDs. Spatial correlation is shown for the 
10:subset of cells recorded in two subsequent trials. Grid spacing is the median distance between the central 
11:peak and the six nearest peaks in the autocorrelogram.  Grid orientation is relative to a horizontal reference 
12:line. The broad range of orientations could be due to differences in preferred grid-cell orientation between 
13:rats; the extent of intra-MEC differences in grid orientation has not been determined. Angular deviation 
14:refers to the circular standard deviation as defined in the Supplementary Materials and Methods. For further 
15:definitions of parameters, see Supplementary Materials and Methods.
17:Sargolini et al.
18:Average rate (Hz)
19:Peak rate (Hz)
20:Spatial info (bits/spike)
21:LAYER II
22:LAYER V
23:LAYER VI
24:LAYER III
[... 270 more lines not kept]
```

**Agent**

Table S1 numbers are garbled in the text; let me see them.

**Agent calls Bash**

```bash
cd  awk 'NR>1039' paper/10.1126-science.1125572.txt | sed -n '1920,1985p'; python -c "import fitz" && echo ok
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "Table S1: Overall" paper/*.txt; sed -n '/Table S1: Overall/,/page 20/p' paper/10.1126-science.1125572.txt | tr '\n' '|'; echo; sed -n '/^(A) Total number of cells sampled/,+0p' paper/*.txt >/dev/null; which pdftoppm pdftotext
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000582/versions/draft/info/ | python -c "import json,sys; d=json.load(sys.stdin); m=d.get('metadata',d); print(m.get('name')); print(m.get('description'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; ls schemas 2>/dev/null; grep -rn "inferred" --include=*.py tools | head
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

[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));
c=s
import pprint
print(json.dumps(s,indent=1)[:6000])"
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
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
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

**Agent calls Bash**

```bash
python -c "
from scipy.stats import chi2_contingency as c
print(c([[0,34],[37,19],[9,1],[7,18]],correction=False)[:2])
print(c([[37,19],[9,1],[7,18]],correction=False)[:2])
print(c([[66,42],[78,145],[17,93],[42,144]])[:2])"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy.stats import chi2_contingency as c
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
python -c "
def chi(t):
  R=[sum(r) for r in t];C=[sum(x) for x in zip(*t)];N=sum(R)
  return sum((t[i][j]-R[i]*C[j]/N)**2/(R[i]*C[j]/N) for i in range(len(t)) for j in range(len(t[0])))
print(chi([[0,34],[37,19],[9,1],[7,18]]), chi([[37,19],[9,1],[7,18]]))"
```

```
49.27619141209943 14.959649950347568
```

**Agent calls Bash**

```bash
python -c "
def chi(t):
  R=[sum(r) for r in t];C=[sum(x) for x in zip(*t)];N=sum(R)
  return sum((t[i][j]-R[i]*C[j]/N)**2/(R[i]*C[j]/N) for i in range(len(t)) for j in range(len(t[0])))
print('conj/all',chi([[0,64],[37,138],[9,65],[7,129]]), chi([[37,138],[9,65],[7,129]]))
print('conj/gridall17',chi([[0,66],[37,41],[9,8],[7,35]]), chi([[37,41],[9,8],[7,35]]))
print('1-sample props',sum((o-e)**2/e for o,e in []) if 0 else '')
"
```

```
conj/all 29.024292078033756 16.692934722210676
conj/gridall17 49.996190367777494 12.559062037974357
1-sample props
```

**Agent**

Paper and supplement are complete (version of record + SOM with Methods, figs S1–S9, table S1). No code is linked. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000582/10.1126-science.1125572.yaml",
 "content": "# Claims for Sargolini, Fyhn, Hafting, McNaughton, Witter, Moser & Moser (2006) on dandiset 000582.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-20,\n# protocol as stated in docs/protocol.md (pilot-10).\n#\n# Text read: the version of record (Science 312, 758-762, PDF supplied by a person, text extracted\n# with PyMuPDF), with its Supporting Online Material (sargolini_som.pdf: Materials and Methods, figs.\n# S1 to S9, table S1). The extracted text garbles symbols: \"P G\" is P <, \"P 9\" is P >, \"r 0\" is\n# r =, \"c(3)\" is chi-square with 3 degrees of freedom, \"T\" is plus or minus. The numbers of table S1\n# were read from the extracted text and agree with every total and percentage the paper prints.\n# The paper links no code; no code was read.\n#\n# What changed. This file replaces an attempt written from the abstract only. The three claims of\n# that attempt keep their ids (layer2-grid, deep-hd-conjunctive, speed) and their findings; each\n# now has the paper's numbers and a criterion. layer2-grid now classifies grid cells by the paper's\n# own criterion, gridness above 0 (SOM, Autocorrelation of rate maps), and no stricter cut.\n# deep-hd-conjunctive now holds the per-layer proportions of conjunctive cells and the chi-square.\n# speed no longer lists P < 0.001 as a statistic, as it is the threshold used to count cells.\n# New claims cover the findings the old file left out: grid cells in every layer, the gridness\n# range, grid stability, grid spacing and field size along the dorsoventral axis, grid phase and\n# orientation, head-direction cells by layer, their tuning breadth, range of directions,\n# stability and colocalization with grid cells, the continuum of gridness and directionality,\n# tuning of conjunctive cells, the coherent response to cue rotation, the slope comparison and the\n# intercepts of the speed regression.\n#\n# Data the paper used (SOM, Subjects; Recording procedures; Spike sorting; Histology). Seventeen\n# male Long Evans rats, 3 to 5 months old, implanted with 4 tetrodes in dorsocaudal MEC (five rats\n# with a second drive in the other hemisphere). Each rat foraged for chocolate crumbs in two\n# successive 10-min trials in the same familiar enclosure, 10 min apart: a circular box of 90 or\n# 180 cm diameter, or a square box of 100 or 150 cm. In five rats a cue card was rotated 90 degrees\n# and back on separate trials in the small circular box. Position from an overhead camera at\n# 50 Hz; nine rats had two LEDs (red and green, 7 cm apart), giving head direction, and only their\n# cells (449 of 627) were used for directional analyses; eight rats had a red LED only. 627 cells\n# were sorted, assigned to layers II, III, V and VI by histology, with each recording site's\n# distance from the postrhinal border measured in sagittal sections. Table S1A gives cells and\n# grid cells per layer for all 17 rats; table S1B gives grid, head-direction, conjunctive and other\n# cells per layer for the nine two-LED rats. The Histology section speaks of 16 rats, the rest of\n# the paper of 17. The dandiset's description says it holds spike times of grid cells and LED\n# positions, a sample of the paper's data; whether it holds the cells, layers, distances and\n# trials a claim needs is the author's to find.\n#\n# Methods common to the criteria, all from the SOM Materials and Methods unless said otherwise.\n# Positions from the red LED, smoothed with a 15-point mean filter. Rate maps in 3 x 3 cm bins,\n# each bin's rate the Gaussian-kernel-smoothed spike count over the kernel-smoothed occupancy\n# (h = 3), bins more than 3 cm from the path unvisited. Spatial autocorrelogram by Pearson\n# correlation over lags, not estimated where fewer than 20 bins overlap. Gridness: the\n# autocorrelogram rotated in 6-degree steps and correlated with the original, within a circle\n# around the outermost of the six peaks closest to the centre (peaks are 100 or more contiguous\n# pixels of 1.5 x 1.5 cm above a threshold, in most cases r = 0.10; with fewer than six peaks, the\n# outermost found), the central peak left out; gridness is the lower of the correlations at 60\n# and 120 degrees minus the highest at 30, 90 and 150 degrees; a grid cell has gridness above 0.\n# Grid spacing is the median distance from the centre to the six inner peaks; orientation the\n# angle from a camera-fixed reference to the nearest inner peak counterclockwise. Head direction\n# from the two LEDs; tuning curve in 60 bins of 6 degrees, unsmoothed; breadth the angular\n# standard deviation of the mean vector. A head-direction cell has a significant Watson U2 test\n# of head directions at spikes against all tracked head directions, and a significant Pearson\n# correlation of its 60-bin rate distribution between alternating 1-min blocks (odd against even\n# minutes). A conjunctive cell meets both the grid and the head-direction criteria. Speed in 1-s\n# bins, unsmoothed, regressed linearly against firing rate per cell.\n#\n# Details the paper leaves open, used by several criteria, each with the readings the text\n# allows; every reading is run.\n# (O1) Trials. Rate maps, gridness and tuning are computed (a) on the two trials pooled, as the\n#   figures show both trials together, or (b) on each trial, a cell passing when it passes in\n#   the first trial.\n# (O2) Autocorrelogram pixels. The rate map has 3 cm bins but peaks are counted in 1.5 cm pixels:\n#   (a) the autocorrelogram of the 3 cm map, peaks of 25 or more contiguous bins (the same area);\n#   (b) a rate map in 1.5 cm bins with the same smoothing, peaks of 100 pixels.\n# (O3) The gridness circle. Its radius is (a) the distance from the centre to the outermost peak's\n#   centre plus that peak's radius (the circle encloses the peak), or (b) the distance to the\n#   outermost peak's centre. The central peak is removed (a) as its contiguous pixels above the\n#   threshold, or (b) as a disc of the radius of that peak. The threshold is r = 0.10; the paper's\n#   \"in most cases\" leaves the others unknown.\n# (O4) Significance level for the head-direction criteria (Watson U2 and the block correlation).\n#   Not stated: (a) 0.05, the level the paper reports for its tests elsewhere; (b) 0.01.\n#   Watson U2 is the two-sample test on the head direction at each spike against the head\n#   direction at each tracker sample.\n# A claim reproduced under one combination of readings and not under another is blocked as\n# methods_underspecified, with every result shown, unless its criterion says otherwise.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000582\"\npaper: doi:10.1126/science.1125572\nclaims:\n- id: layer2-grid\n  statement: The proportion of cells with grid structure depended on layer. Most well-separated\n    layer II cells were grid cells (66 of 108), against a smaller proportion in layers III (78 of\n    223), V (17 of 110) and VI (42 of 186).\n  source: Main text, paragraph 2; Fig. 1D; table S1A\n  quote: The proportion of cells with a sinusoidal modulation was layer-dependent (Fig. 1D and table\n    S1). Whereas most well-separated layer II cells had strongly periodic firing fields, only a\n    smaller proportion of the deeper neurons had such characteristics\n  expected:\n  - quantity: fraction of layer II cells that are grid cells (66 of 108, table S1A)\n    value: 0.611\n    tolerance: 0.061\n  - quantity: fraction of layer III cells that are grid cells (78 of 223)\n    value: 0.350\n    tolerance: 0.035\n  - quantity: fraction of layer V cells that are grid cells (17 of 110)\n    value: 0.155\n    tolerance: 0.015\n  - quantity: fraction of layer VI cells that are grid cells (42 of 186)\n    value: 0.226\n    tolerance: 0.023\n  criterion: All cells of all 17 rats, grouped by layer; a grid cell has gridness above 0, the\n    paper's criterion (SOM, Autocorrelation of rate maps), with readings O1 to O3. The paper\n    reports no test of the layer difference. Reproduced when the layer II fraction is above 0.5\n    and above that of each deeper layer, and the four fractions are within tolerance. Partially\n    reproduced when the order holds but a fraction is outside tolerance. The fractions need every\n    sorted cell of a layer as the denominator; if the dataset holds grid cells only, the claim\n    cannot be tested.\n- id: grid-all-layers\n  statement: Grid cells with tessellating firing fields were found in all four principal cell\n    layers of MEC (II, III, V and VI).\n  source: Main text, paragraph 2; Fig. 1, A and B; table S1A\n  quote: Grid cells with tessellating firing fields (7) were observed in all principal cell layers\n    (Fig. 1, A and B).\n  criterion: Grid cells as in layer2-grid (gridness above 0, readings O1 to O3). Reproduced when at\n    least one grid cell is found in each of layers II, III, V and VI.\n- id: gridness-range-similar\n  statement: Among deeper-layer cells with periodic firing, the range of gridness did not differ\n    from that of layer II cells.\n  source: Main text, paragraph 2; Fig. 1D\n  quote: however, the range of Bgridness[ among those cells was not different from that of the layer\n    II cells\n  criterion: A claim of absence for which the paper names no test and no level. Cells are the grid\n    cells of each layer (gridness above 0, readings O1 to O3). The readings of the test are (a) a\n    two-sided Mann-Whitney test of gridness, layer II against layers III to VI pooled; (b) a\n    Kruskal-Wallis test across the four layers; each at p < 0.05, the level the paper uses for\n    its other comparisons. Reproduced when no reading finds a difference; not reproduced when all\n    do; methods_underspecified when they disagree. The median and range of gridness per layer are\n    reported either way.\n- id: grid-stable\n  statement: All 203 grid cells had stable periodic firing patterns within and between trials.\n  source: Main text, paragraph 3; figs. S1 and S2\n  quote: All 203 neurons that passed this criterion had stable periodic firing patterns both within\n    and between trials (figs. S1 and S2).\n  expected:\n  - quantity: number of grid cells, all 17 rats (table S1A)\n    value: 203\n    tolerance: 20\n  criterion: Grid cells as in layer2-grid. Between trials, the paper's measure is the spatial\n    correlation of the two trials' rate maps, bin by bin (SOM, Analysis of place fields; fig. S2),\n    for cells recorded in two trials. The paper gives no threshold for \"stable\" and does not\n    define stability within a trial. Readings for stable between trials are (a) a positive map\n    correlation with Pearson p < 0.05; (b) gridness above 0 in each trial's map. Within a trial\n    the readings are (a) the same tests on the maps of the first and second halves of each trial;\n    (b) on the maps of odd and even minutes, as the head-direction Methods split a trial.\n    Reproduced when every grid cell passes under every reading; partially reproduced when at\n    least 90% do; methods_underspecified when the readings disagree on these outcomes. The count\n    of grid cells is checked only if the dataset holds all sorted cells.\n- id: spacing-dorsoventral\n  statement: In every layer grid spacing increased with distance from the postrhinal border, by a\n    factor of 1.5 to 2 over the sampled range, with the densest spacing (about 35 to 40 cm) near\n    the border; the correlations (0.46 to 0.94) were significant in every layer and did not differ\n    between layers.\n  source: Main text, paragraphs 3 and 4; fig. S3\n  quote: Irrespective of layer, the scale of the grid in these cells increased by a factor of 1.5 to\n    2 from the dorsalmost to the ventralmost recording location, such that cells near the postrhinal\n    border had the densest spacing (È35 to 40 cm) ... The correlations between distance from the\n    ... postrhinal border on the one hand and spacing and field size on the other were significant\n    in all layers (spacing, 0.46 e r e 0.94; field size, 0.44 e r e 0.94; all, P G 0.005)\n  statistics:\n  - about: spacing against distance from the postrhinal border, each layer\n    test: Pearson product-moment correlation\n    statistic: 0.46 ≤ r ≤ 0.94\n    p: 0.005\n    p_relation: \"<\"\n  expected:\n  - quantity: Pearson r, spacing against distance, layer II (fig. S3)\n    value: 0.84\n    tolerance: 0.084\n  - quantity: Pearson r, spacing against distance, layer III (fig. S3)\n    value: 0.46\n    tolerance: 0.046\n  - quantity: Pearson r, spacing against distance, layer V (fig. S3)\n    value: 0.94\n    tolerance: 0.094\n  - quantity: Pearson r, spacing against distance, layer VI (fig. S3)\n    value: 0.65\n    tolerance: 0.065\n  - quantity: ratio of spacing, ventralmost to dorsalmost location (range 1.5 to 2, widened by 10%)\n    value: 1.775\n    tolerance: 0.425\n  - quantity: spacing of cells near the postrhinal border (range 35 to 40, widened by 10%)\n    value: 37.75\n    tolerance: 6.25\n    unit: cm\n  criterion: Grid cells of each layer, spacing as in the SOM (median distance from the centre to the\n    six inner peaks of the autocorrelogram, readings O1 and O2), against the distance of the\n    recording site from the postrhinal border, from the histology (SOM, Histology; fig. S3).\n    Reproduced when, in every layer, Pearson r is positive with p < 0.005 and within tolerance,\n    and the ratio and near-border spacing are within tolerance. Partially reproduced when every\n    layer's correlation is positive and significant but a number is outside tolerance. The paper\n    does not say how the ratio is formed; readings are (a) per layer, the mean spacing at the most\n    ventral recording location over that at the most dorsal; (b) the values of the regression\n    line at those two locations. Near the border means the cells at each layer's most dorsal\n    location. The fig. S3 legend adds that there was no significant difference between layers,\n    with no test named; readings are (a) pairwise comparisons of the correlations by Fisher's z,\n    (b) the layer by distance interaction in a linear model of spacing, each at p < 0.05. That\n    part is reported, and it is judged as an absence; if a reading finds a difference the claim\n    is at most partially reproduced. Needs the recording sites' distances from the postrhinal\n    border.\n- id: fieldsize-dorsoventral\n  statement: In every layer grid field size increased with distance from the postrhinal border\n    (0.44 ≤ r ≤ 0.94, all P < 0.005), with the smallest fields (about 500 cm2) near the border.\n  source: Main text, paragraphs 3 and 4; fig. S3\n  quote: cells near the postrhinal border had the densest spacing (È35 to 40 cm) and the smallest\n    firing fields (È500 cm2) (fig. S3)\n  statistics:\n  - about: field size against distance from the postrhinal border, each layer\n    test: correlation (named Pearson for spacing in fig. S3)\n    statistic: 0.44 ≤ r ≤ 0.94\n    p: 0.005\n    p_relation: \"<\"\n  expected:\n  - quantity: Pearson r, field size against distance, each layer (range 0.44 to 0.94, widened by 10%)\n    value: 0.6935\n    tolerance: 0.2935\n  - quantity: field size of cells near the postrhinal border\n    value: 500\n    tolerance: 50\n    unit: cm2\n  criterion: Grid cells of each layer against the distance of the recording site from the\n    postrhinal border. The paper does not define field size. Readings are (a) the area of the\n    central peak of the autocorrelogram, as contiguous pixels above the r = 0.10 threshold the SOM\n    uses for peaks; (b) the mean area of the firing fields of the rate map, as contiguous bins\n    above 20% of the cell's peak rate, a common definition that this paper does not give.\n    Reproduced when, under a reading, r is positive with p < 0.005 in every layer, each r within\n    the widened range and the field size of the cells at each layer's most dorsal location within\n    tolerance; methods_underspecified when the readings disagree. Needs the recording sites'\n    distances from the postrhinal border.\n- id: grid-phase-orientation\n  statement: In all layers the spatial phase of nearby grid cells was distributed (their vertices\n    were offset), while grid orientation was consistent across simultaneously recorded cells.\n  source: Main text, paragraph 4; fig. S2 legend\n  quote: In all layers, the phase of the grid was distributed, i.e., the vertices of most nearby grid\n    cells were offset relative to each other, but the orientation of the grids was consistent\n    across all simultaneously recorded cells.\n  criterion: Pairs of grid cells recorded simultaneously (same rat and trial), orientation as in the\n    SOM, compared modulo 60 degrees. The paper gives no measure of phase offset and no threshold\n    for either part. Orientation is consistent when the within-session pairwise differences are\n    smaller than the differences between sessions of different rats (the fig. S2 legend ascribes\n    the broad range of orientations to differences between rats), by a one-sided Mann-Whitney\n    test at p < 0.05; this test is a standard choice, not the paper's. Phase is distributed when,\n    for most pairs (more than half), the peak of the rate-map crosscorrelogram nearest the centre\n    is displaced from the centre; readings for displaced are (a) by more than one fifth of the\n    grid spacing, (b) by more than the 3 cm bin. Reproduced when both parts hold under every\n    reading, in each layer with at least one simultaneous pair.\n- id: hd-layers\n  statement: No head-direction cells were found in layer II, whereas most cells in layers III to VI\n    were directionally tuned (273 of 385 cells, counting conjunctive cells).\n  source: Main text, paragraph 5; Fig. 2E; table S1B\n  quote: No head-direction cells were found in layer II (Fig. 2E). In contrast, a large proportion\n    of the cells in layers III to VI had directional preferences (273 of 385 cells) (Fig. 2E).\n  expected:\n  - quantity: directional cells in layer II (table S1B)\n    value: 0\n    tolerance: 0\n  - quantity: fraction of layers III to VI cells with directional tuning (273 of 385)\n    value: 0.709\n    tolerance: 0.071\n  - quantity: fraction directional, layer III ((80 + 37) of 175, table S1B)\n    value: 0.669\n    tolerance: 0.067\n  - quantity: fraction directional, layer V ((56 + 9) of 74)\n    value: 0.878\n    tolerance: 0.088\n  - quantity: fraction directional, layer VI ((84 + 7) of 136)\n    value: 0.669\n    tolerance: 0.067\n  criterion: Cells of the nine two-LED rats only; head-direction cells by the SOM criteria with\n    readings O1 and O4; directional cells are head-direction cells plus conjunctive cells (220 +\n    53 = 273, table S1B). Reproduced when no layer II cell passes and the fractions are within\n    tolerance; partially reproduced when no layer II cell passes and the deeper fraction is above\n    0.5 but a number is outside tolerance. The fractions need every sorted cell as denominator;\n    if the dataset holds grid cells only, only the layer II part can be tested, and the claim is\n    at most partially reproduced.\n- id: hd-with-grid-colocalized\n  statement: Beneath layer II, head-direction cells were usually recorded together with grid cells.\n  source: Main text, paragraph 5; fig. S6\n  quote: Beneath layer II, grid cells were colocalized with head-direction cells ... Head-direction\n    cells were usually encountered together with grid cells (fig. S6).\n  depends_on:\n  - hd-layers\n  criterion: Two-LED rats, layers III to VI, cell classes as in hd-layers and layer2-grid. The paper\n    does not fix the unit of colocalization or what \"usually\" means. Readings of the unit are (a)\n    the recording session (rat, location and trial); (b) the tetrode within a session. Reproduced\n    when, under both readings, more than half of the units holding a head-direction cell also\n    hold a grid or conjunctive cell; methods_underspecified when the readings disagree.\n- id: hd-tuning-breadth-layers\n  statement: The breadth of directional tuning did not differ between layers III, V and VI (mean U2\n    18.2, 25.2 and 18.3; mean angular standard deviation 55.9, 52.2 and 58.2 degrees; P > 0.05).\n  source: Main text, paragraph 5; fig. S4\n  quote: The breadth of tuning was not significantly different between layers III, V, and VI (mean\n    U2 values, 18.2, 25.2, and 18.3, respectively; mean angular standard deviations, 55.9-, 52.2-,\n    and 58.2-; P 9 0.05) (fig. S4).\n  statistics:\n  - test: not named\n    p: 0.05\n    p_relation: \">\"\n    n: head-direction cells of layers III, V and VI, nine two-LED rats\n  expected:\n  - quantity: mean Watson U2, layer III\n    value: 18.2\n    tolerance: 1.82\n  - quantity: mean Watson U2, layer V\n    value: 25.2\n    tolerance: 2.52\n  - quantity: mean Watson U2, layer VI\n    value: 18.3\n    tolerance: 1.83\n  - quantity: mean angular standard deviation, layer III\n    value: 55.9\n    tolerance: 5.59\n    unit: degrees\n  - quantity: mean angular standard deviation, layer V\n    value: 52.2\n    tolerance: 5.22\n    unit: degrees\n  - quantity: mean angular standard deviation, layer VI\n    value: 58.2\n    tolerance: 5.82\n    unit: degrees\n  depends_on:\n  - hd-layers\n  criterion: A claim of absence; the paper names the level (P > 0.05) but not the test. Readings of\n    the test are (a) a one-way ANOVA across the three layers, the test the paper uses for its\n    slope comparison; (b) a Kruskal-Wallis test; each on U2 and on angular standard deviation.\n    Readings of the cells are (a) pure head-direction cells; (b) head-direction and conjunctive\n    cells together. Reproduced when no reading finds a difference at p < 0.05; not reproduced when\n    all do; methods_underspecified when they disagree. The means are reported and compared with\n    tolerance either way; a reproduced absence with means outside tolerance is partially\n    reproduced. Fig. S4 gives 388 cells for layers III to VI, the main text 385.\n- id: hd-full-range\n  statement: The entire range of head directions was represented by the preferred directions of\n    head-direction cells in each of layers III, V and VI.\n  source: Main text, paragraph 5; Fig. 2F\n  quote: The entire range of head directions was represented in all three layers (Fig. 2F).\n  depends_on:\n  - hd-layers\n  criterion: Head-direction and conjunctive cells of each layer; preferred direction as the bin of\n    peak rate (SOM, Analysis of head-direction cells). The paper gives no measure of coverage.\n    Readings are that each (a) 30-degree, (b) 60-degree or (c) 90-degree sector of the circle holds\n    the preferred direction of at least one cell of the layer. Reproduced when all readings hold\n    in all three layers; not reproduced when none does in some layer; otherwise\n    methods_underspecified.\n- id: hd-colocalized-distributed\n  statement: Preferred directions of simultaneously recorded head-direction cells in the same area\n    were widely distributed; in most ensembles of five or more cells (8 of 12) they showed no\n    significant clustering.\n  source: Main text, paragraph 5; Fig. 2G; fig. S5\n  quote: When several head-direction cells were recorded simultaneously in the same area, their peak\n    firing directions were widely distributed (Fig. 2G and fig. S5).\n  statistics:\n  - about: clustering of the mean vectors of 7 colocalized layer VI cells (Fig. 2G)\n    test: Watson's U2 test\n    statistic: U2 = 0.01, critical value 0.18, n.s.\n    p: 0.05\n    p_relation: \">\"\n  expected:\n  - quantity: ensembles of 5 or more simultaneous head-direction cells with significant clustering\n      (fig. S5, D, E, F and J)\n    value: 4\n    tolerance: 0.4\n  - quantity: ensembles of 5 or more simultaneous head-direction cells (fig. S5)\n    value: 12\n    tolerance: 1.2\n  depends_on:\n  - hd-layers\n  criterion: As in fig. S5, every session with 5 or more simultaneously recorded head-direction\n    cells; the mean vectors of the cells (direction and rate) tested for clustering with Watson's\n    one-sample U2 test of uniformity at p < 0.05, against the critical value for the number of\n    cells. Whether conjunctive cells count is not stated; readings are (a) pure head-direction\n    cells, (b) with conjunctive cells. Reproduced when, under a reading, fewer than half of the\n    ensembles show significant clustering; the counts are compared with the expected values.\n    methods_underspecified when the readings disagree on this.\n- id: hd-stable-trials\n  statement: Directional tuning was stable across the two trials (circular correlation r = 0.84,\n    P < 0.001).\n  source: Main text, paragraph 5\n  quote: Directional tuning curves were always stable across trials (circular correlation, r 0 0.84,\n    P G 0.001).\n  statistics:\n  - test: circular correlation\n    statistic: r = 0.84\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n    quantity: circular correlation between trials\n    value: 0.84\n    tolerance: 0.084\n  depends_on:\n  - hd-layers\n  criterion: Head-direction and conjunctive cells recorded in both trials of the same session. The\n    paper does not say what was correlated. Readings are (a) across cells, the circular-circular\n    correlation of the preferred direction in trial 1 with that in trial 2; (b) per cell, the\n    circular correlation of head direction at spikes between the two trials' tuning curves, as\n    the Pearson correlation of the two 60-bin rate distributions, averaged over cells. Reproduced\n    when, under a reading, r is within tolerance with p < 0.001; methods_underspecified when one\n    reading reproduces and another fails.\n- id: deep-hd-conjunctive\n  statement: The proportion of grid cells with conjunctive head-direction tuning depended on layer\n    (66% in layer III, 90% in layer V, 28% in layer VI, none in layer II); the difference was\n    significant across all four layers and across layers III to VI.\n  source: Main text, paragraph 6; table S1B\n  quote: The proportion of grid cells with conjunctive properties was layer-dependent (table S1).\n    The largest proportion was encountered in layers III and V, where 66% and 90% of the grid cells\n    had dual response properties, respectively. In layer VI, the proportion was 28%. No conjunctive\n    cells were observed in layer II. Differences between layers were significant (all four cell\n    layers, c(3) 0 28.4, P G 0.001; layers III to VI, c(2) 0 6.2, P G 0.05)\n  statistics:\n  - about: all four layers\n    test: chi-square test\n    statistic: χ2(3) = 28.4\n    p: 0.001\n    p_relation: \"<\"\n  - about: layers III to VI\n    test: chi-square test\n    statistic: χ2(2) = 6.2\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: conjunctive fraction of grid cells, layer II (0 of 34, table S1B)\n    value: 0\n    tolerance: 0\n  - quantity: conjunctive fraction of grid cells, layer III (37 of 56)\n    value: 0.66\n    tolerance: 0.066\n  - quantity: conjunctive fraction of grid cells, layer V (9 of 10)\n    value: 0.90\n    tolerance: 0.09\n  - quantity: conjunctive fraction of grid cells, layer VI (7 of 25)\n    value: 0.28\n    tolerance: 0.028\n  depends_on:\n  - layer2-grid\n  - hd-layers\n  criterion: Two-LED rats; grid cells (gridness above 0) and conjunctive cells (grid and\n    head-direction criteria) by the SOM, readings O1 to O4. The paper does not give the table its\n    chi-square was run on, and the counts of table S1B do not yield 28.4 and 6.2 under the\n    obvious tables. Readings are (a) conjunctive against non-conjunctive grid cells per layer,\n    the proportion the text describes; (b) conjunctive cells against all other cells per layer.\n    Reproduced when, under a reading, both chi-square tests are significant (p < 0.001 for four\n    layers, p < 0.05 for layers III to VI) and the four fractions are within tolerance; partially\n    reproduced when no layer II cell is conjunctive and the four-layer test is significant but a\n    fraction or the three-layer test fails. Layer V holds 10 grid cells in the paper, so its\n    fraction is coarse.\n- id: gridness-hd-continuous\n  statement: Grid cells and head-direction cells formed overlapping populations; the joint\n    distribution of gridness and directional tuning was continuous, with some grid cells\n    directionally tuned and some head-direction cells having grid structure.\n  source: Main text, paragraph 6; Fig. 3, A to E; fig. S7\n  quote: Grid cells and head-direction cells formed overlapping populations. The 2D distribution of\n    gridness and directional tuning was continuous, such that some grid cells were directionally\n    tuned and some head-direction cells had grid correlates (Fig. 3, A to D, and fig. S7).\n  depends_on:\n  - deep-hd-conjunctive\n  criterion: Two-LED rats, all cells, gridness against Watson U2 (log scale) as in Fig. 3E. The\n    paper gives no test of continuity. Reproduced when conjunctive cells exist (cells passing both\n    criteria) and, under readings O1 to O4, the cells passing either criterion form no separate\n    clusters; the last part is read as the absence of a gap, along each axis, wider than a\n    quarter of that axis's range among them, a standard choice and not the paper's.\n- id: conj-tuning-similar\n  statement: Directional tuning of conjunctive cells did not differ from that of pure head-direction\n    cells (mean U2 18.0 against 19.4, P > 0.05).\n  source: Main text, paragraph 6; Fig. 3, D and E\n  quote: The degree of directional tuning in cells that met selection criteria for both gridness and\n    directionality was not significantly different from that of pure headdirection cells (mean U2\n    values, 18.0 and 19.4, respectively; P 9 0.05) (Fig. 3, D and E).\n  statistics:\n  - test: not named\n    p: 0.05\n    p_relation: \">\"\n    n: 53 conjunctive and 220 head-direction cells (table S1B)\n  expected:\n  - quantity: mean Watson U2, conjunctive cells\n    value: 18.0\n    tolerance: 1.8\n  - quantity: mean Watson U2, pure head-direction cells\n    value: 19.4\n    tolerance: 1.94\n  depends_on:\n  - deep-hd-conjunctive\n  criterion: A claim of absence; the paper names the level but not the test. Readings are (a) a\n    two-sided t-test, (b) a two-sided Mann-Whitney test, of U2 in conjunctive against pure\n    head-direction cells, at p < 0.05. Reproduced when no reading finds a difference; not\n    reproduced when all do; methods_underspecified when they disagree. A reproduced absence with\n    means outside tolerance is partially reproduced.\n- id: cue-rotation-coherent\n  statement: Cells with different degrees of gridness and directionality responded as a coherent\n    ensemble to rotation of a polarizing cue card; in the example, a grid cell and four\n    head-direction cells recorded together all rotated by 90 degrees with the card.\n  source: Main text, paragraph 6; Fig. 3F; fig. S8\n  quote: Cells with different degrees of gridness and directionality always responded as a coherent\n    ensemble during environmental manipulations such as the rotation of a polarizing cue card (Fig.\n    3F and fig. S8) (22).\n  criterion: The cue-rotation sessions of the five rats tested (small circular box, card rotated 90\n    degrees and back). The paper gives no measure of rotation. For each cell, the rotation from\n    the standard trial to the rotated trial is the angle that maximizes (a) for grid structure,\n    the correlation between the rotated standard rate map and the rotated-trial map, in 6-degree\n    steps; (b) for head-direction tuning, the correlation of the 60-bin tuning curves under\n    circular shift. Coherent means all cells of a session rotate by the same angle; readings of\n    \"the same\" are within (a) 18 degrees (three tuning bins) and (b) 30 degrees of each other.\n    Reproduced when every session with two or more cells is coherent under both readings;\n    methods_underspecified when they disagree. The rotation of each session relative to the 90\n    degrees of the card is reported.\n- id: speed\n  statement: Firing rate increased with running speed in nearly all grid cells (141 of 150),\n    most head-direction cells (153 of 220) and most conjunctive cells (45 of 53).\n  source: Main text, paragraph 7; Fig. 4, A and B\n  quote: Yet, regression analyses showed a consistent positive speed-rate relation in nearly all grid\n    cells (141/150 cells, P G 0.001), headdirection cells (153/220 cells, P G 0.001) and grid ...\n    head-direction cells (45/53 cells, P G 0.001), suggesting that a substantial proportion of the\n    network expressed information about how fast the animal was moving (Fig. 4B).\n  expected:\n  - quantity: fraction of grid cells with a significant positive speed-rate relation (141 of 150)\n    value: 0.94\n    tolerance: 0.094\n  - quantity: fraction of head-direction cells (153 of 220)\n    value: 0.695\n    tolerance: 0.070\n  - quantity: fraction of conjunctive cells (45 of 53)\n    value: 0.849\n    tolerance: 0.085\n  depends_on:\n  - layer2-grid\n  - deep-hd-conjunctive\n  criterion: Per cell, speed and firing rate in 1-s bins over the trial, unsmoothed, all bins kept\n    including those outside firing fields, and a linear regression of rate on speed (SOM, Velocity\n    tuning). A cell counts when the slope is positive with P < 0.001 (main text). Grid cells are\n    the 150 grid cells that are not conjunctive (203 - 53), which include the grid cells of the\n    single-LED rats; head-direction and conjunctive cells from the two-LED rats. Open details,\n    each with readings. Speed in a 1-s bin is (a) the path length of the tracked positions over\n    the bin, (b) the distance between the positions at the start and end of the bin; positions\n    are (a) the 15-point mean-filtered positions of the place-field Methods, (b) the raw tracked\n    positions. Trials as O1. The significance of the relation is that of (a) the regression slope,\n    (b) Pearson's r, (c) Spearman's rank correlation, which the SOM reports gave nearly identical\n    values. Reproduced when, under a combination of readings, all three fractions are within\n    tolerance; partially reproduced when the grid and conjunctive fractions exceed the\n    head-direction fraction and all exceed one half but a fraction is outside tolerance.\n    methods_underspecified when readings disagree between these outcomes.\n- id: speed-slope-steeper\n  statement: The slope of the speed-rate regression was steeper for conjunctive cells and grid\n    cells than for head-direction cells, and did not differ between conjunctive and grid cells.\n  source: Main text, paragraph 7; Fig. 4B\n  quote: The slope of the regression line was steeper for conjunctive cells and grid cells than for\n    headdirection cells EF(2,422) 0 5.5, P G 0.005; conjunctive versus head-direction, P 0 0.009;\n    grid versus head-direction, P 0 0.01; conjunctive versus grid, P 0 0.60; Tukey HSD test).\n  statistics:\n  - about: slope across the three cell classes\n    test: ANOVA\n    statistic: F(2,422) = 5.5\n    p: 0.005\n    p_relation: \"<\"\n    n: 423 cells (150 grid, 220 head-direction, 53 conjunctive)\n  - about: conjunctive against head-direction\n    test: Tukey HSD test\n    p: 0.009\n  - about: grid against head-direction\n    test: Tukey HSD test\n    p: 0.01\n  - about: conjunctive against grid\n    test: Tukey HSD test\n    p: 0.60\n  depends_on:\n  - speed\n  criterion: Slopes from the regressions of the speed claim, all 423 cells, with its readings.\n    One-way ANOVA of slope on cell class and Tukey HSD (main text). Reproduced when the ANOVA has\n    p < 0.005, Tukey gives conjunctive and grid each steeper than head-direction at p < 0.05 and\n    conjunctive against grid p > 0.05. Partially reproduced when the ANOVA is significant at\n    p < 0.05 and one of the two comparisons with head-direction is significant. The printed\n    F(2,422) has one more error degree of freedom than 423 cells in three groups allow (420); the\n    degrees of freedom are reported.\n- id: speed-intercept\n  statement: The intercept of the speed-rate regression was positive in all cells but one (422 of\n    423), and mean rates at the lowest speeds (0 to 3 cm/s) were about 2.3 to 2.5 Hz in each cell\n    class, so firing persisted during brief stops.\n  source: Main text, paragraph 7; Fig. 4C\n  quote: The yintercept of the regression line was positive in 422 out of 423 cells (Fig. 4C).\n    Average rates at the lowest velocity (0 to 3 cm/s) were 2.26 T 0.03 Hz (grid cells), 2.50 T\n    0.02 Hz (headdirection cells) and 2.39 T 0.05 Hz (grid ... head-direction cells).\n  expected:\n  - quantity: fraction of cells with a positive intercept (422 of 423)\n    value: 0.998\n    tolerance: 0.0998\n  - quantity: mean rate at 0 to 3 cm/s, grid cells\n    value: 2.26\n    tolerance: 0.03\n    unit: Hz\n  - quantity: mean rate at 0 to 3 cm/s, head-direction cells\n    value: 2.50\n    tolerance: 0.02\n    unit: Hz\n  - quantity: mean rate at 0 to 3 cm/s, conjunctive cells\n    value: 2.39\n    tolerance: 0.05\n    unit: Hz\n  depends_on:\n  - speed\n  criterion: Regressions and readings as in the speed claim. The tolerances on the rates are the\n    paper's printed spread, whose kind (SEM or SD) is not stated. The paper does not say how the\n    average was taken; readings are (a) the mean over cells of each cell's mean rate in the 1-s\n    bins with speed from 0 to 3 cm/s; (b) the mean over all such bins of all cells of a class\n    pooled. Reproduced when, under a reading, the fraction is within tolerance and the three\n    rates are within their tolerances; partially reproduced when the fraction holds and the rates\n    are within 10% of the printed values.\n"
}
```

```
The file claims/000582/10.1126-science.1125572.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000582/10.1126-science.1125572.yaml",
 "old_string": "(b) per cell, the\n    circular correlation of head direction at spikes between the two trials' tuning curves, as\n    the Pearson correlation of the two 60-bin rate distributions, averaged over cells.",
 "new_string": "(b) per cell, the\n    Pearson correlation of the two trials' 60-bin tuning curves, averaged over cells, with the\n    significance of that mean tested against 0 by a one-sample t-test (a standard choice)."
}
```

```
The file claims/000582/10.1126-science.1125572.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000582/10.1126-science.1125572.yaml",
 "old_string": "readings for displaced are (a) by more than one fifth of the\n    grid spacing, (b) by more than the 3 cm bin.",
 "new_string": "readings for displaced, standard choices since the paper gives\n    none, are (a) by more than one fifth of the grid spacing, (b) by more than the 3 cm bin."
}
```

```
The file claims/000582/10.1126-science.1125572.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000582/10.1126-science.1125572.yaml paper/10.1126-science.1125572.txt; grep -n -E "—|rather" claims/000582/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/000582/10.1126-science.1125572.yaml'))
def walk(x):
  if isinstance(x,dict): [walk(v) for v in x.values()]
  elif isinstance(x,list): [walk(v) for v in x]
  elif isinstance(x,str) and ': ' in x: print(repr(x[:80]))
walk(d)"
```

```
(Bash completed with no output)
```

**Agent**

I rewrote `claims/000582/10.1126-science.1125572.yaml` from the full text. It now has 20 claims, all with quotes and criteria. The quote checker reports 0 problems.

**Text read:** the version of record (Science 312:758) and its supplement, which has the Materials and Methods, figs. S1 to S9 and table S1. Nothing the claims needed was missing. Table S1's numbers came out of the extracted text without the table layout, so I placed them using the paper's totals and percentages, which all agree. The paper links no code, so none was read.

**Claims:**
- **Kept ids:** `layer2-grid` now uses the paper's own grid-cell criterion (gridness above 0) and the per-layer counts from table S1A. `deep-hd-conjunctive` now has the conjunctive proportions per layer and the two chi-square tests. `speed` no longer lists P < 0.001 as a statistic, because it is the threshold used to count cells, not a result.
- **17 new claims:**
  - Grid cells: present in all layers, gridness range similar across layers, stable within and between trials.
  - Spacing and field size along the dorsoventral axis, and grid phase and orientation.
  - Head-direction cells: counts per layer, recorded together with grid cells, tuning breadth across layers, full range of directions, spread of directions within an ensemble, stability across trials.
  - The continuous spread between grid and head-direction properties, conjunctive tuning matching pure head-direction tuning, and the coherent response to cue-card rotation.
  - Speed: steeper slopes for grid and conjunctive cells, and positive intercepts with rates at low speed.
- **Statistics:** 12 entries across 8 claims. Two of them are absence tests whose test the paper does not name.
- The opening comment records what changed and why, and describes the data.

**Details the paper leaves open, with the readings named:**
- **Throughout:**
  - Whether maps are built from the two trials pooled or from each trial.
  - Autocorrelogram pixel size: the rate maps use 3 cm bins but peaks are counted in 1.5 cm pixels.
  - The radius of the gridness circle and how the central peak is removed.
  - The significance level for the head-direction criteria (0.05 or 0.01).
- **Tests the paper does not name:** gridness range across layers (Mann-Whitney or Kruskal-Wallis), tuning breadth across layers (ANOVA or Kruskal-Wallis), conjunctive against pure head-direction tuning (t-test or Mann-Whitney), and the "no difference between layers" for spacing (Fisher z or a layer-by-distance interaction).
- **Measures the paper does not define:**
  - Field size: the autocorrelogram's central peak, or rate-map fields above 20% of peak.
  - Within-trial stability: half against half, or odd against even minutes.
  - The thresholds for phase offset and orientation consistency.
  - Coverage of the full direction range: 30, 60 or 90 degree sectors.
  - What the 0.84 circular correlation correlates.
  - The colocalization unit: session or tetrode.
  - How rotation is measured and how close counts as coherent in the cue-card claim.
  - How the 1.5 to 2 spacing ratio is formed.
- **Speed analysis:** path length or displacement per 1-s bin, smoothed or raw positions, and slope, Pearson or Spearman significance. For the rates at low speed: mean per cell or over pooled bins. The paper also does not say whether its ± values are SEM or SD.
- Some thresholds in the criteria are my standard choices, not the paper's (the orientation test, the phase-offset thresholds, the gap rule for continuity, the rotation tolerances). Each is labelled as such in the file.

**Inconsistencies in the paper, noted in the claims:**
- **Chi-square:** the table S1B counts do not reproduce the paper's χ²(3) = 28.4 or χ²(2) = 6.2 under either obvious table. I got 49.3 and 15.0 for conjunctive against other grid cells, and 29.0 and 16.7 against all cells. Both readings are named.
- **Degrees of freedom:** F(2,422) does not fit 423 cells in three groups, which allows 420.
- **Rat counts:** the Histology section says 16 rats, the rest of the paper says 17.
- **Cell counts:** fig. S4 says 388 cells for layers III to VI, the main text says 385.

**What the dataset may not support:** its description says it holds spike times of grid cells only, a sample of the paper's data. If so, the layer proportions in `layer2-grid`, `hd-layers` and `deep-hd-conjunctive` cannot be tested, since they need every sorted cell. The spacing and field-size claims need each recording site's distance from the postrhinal border.

## End of run

22 turns, 6 minutes, result: success.
