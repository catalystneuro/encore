# 000140 · claims · run 40790041940

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/## Reader/,/^## [A-Z]/p'; ls claims/001453/ claims/000140 paper/ 2>&1; ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; wc -l *.txt; head -30 10.1016-j.neuron.2010.09.015.txt; grep -n -i "supplement\|experimental procedures\|methods" 10.1016-j.neuron.2010.09.015.txt | head -60; cat ../claims/001453/*.yaml | head -150
```

```
<persisted-output>
Output too large (151KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/15c848b5-b666-4bc8-92b7-4a2fdf18ea0e/tool-results/btk0cd7yo.txt

Preview (first 2KB):
   700 10.1016-j.neuron.2010.09.015.txt
    92 10.1038-nature11129.txt
   792 total
DOI: 10.1016/j.neuron.2010.09.015
Version: as served by ncbi_pmc
Source: ncbi_pmc+crossref (paper-text-fetcher)
Stored: 2026-10-20
Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC2991102), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
------------------------------------------------------------------------
Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC2991102 PMC2991102.1 2991102 2991102 NIHMS240235 21040842 10.1016/j.neuron.2010.09.015 NIHMS240235 NIHPA240235 1 Article Cortical preparatory activity: representation of movement or first cog in a dynamical machine? Churchland MM 1 Cunningham JP 1 3 Kaufman MT 2 Ryu SI 1 4 Shenoy KV 1 2 5 1 Dept. of Electrical Engineering, Stanford University, Stanford CA, 94305, USA 2 Neurosciences Program, Stanford University, Stanford CA, 94305, USA 3 Dept. of Engineering, University of Cambridge, Cambridge, UK 4 Dept. of Neurosurgery, Palo Alto Medical Foundation, Palo Alto CA, 94301, USA 5 Dept. of Bioengineering, Stanford University, Stanford CA, 94705, USA 4 11 2010 68 3 191982 387 400 06 10 2010 04 11 2011 04 11 2011 06 10 2011 14 10 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Summary The motor cortices are active during both movement and movement preparation. A common assumption is that preparatory activity constitutes a sub-threshold form of movement activity: a neuron active during rightwards movements becomes modestly active during preparation of a rightwards movement. We asked wheth
[... 2 more lines not kept]
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
 "file_path": "paper/10.1016-j.neuron.2010.09.015.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python3 -c "
s=open('10.1016-j.neuron.2010.09.015.txt').read()
print(s[58000:])"
```

```
<persisted-output>
Output too large (44.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/15c848b5-b666-4bc8-92b7-4a2fdf18ea0e/tool-results/bci7owl4d.txt

Preview (first 2KB):
black bar : performance when data were randomly subdivided. D. PD consistency for the peri-movement space versus that for a variety of other spaces. Kinematic and EMG spaces were chosen because they had performed the best overall (after the peri-movement space) in the analysis in Fig. 6 . ‘ Targs. + inst. speed ’ and ‘ segment directions ’ spaces were chosen because they performed well for the speed and maze tasks respectively. ‘ Targs. + inst. speed ’ was undefined for the maze task; the similar ‘ endpoints + max. spd. ’ space was analyzed instead. Figure 8 Illustration of the behavior of a simple linear dynamical system: a harmonic oscillator. A. Changes in the initial state produce a linear scaling of the subsequent activity pattern. In this case, the larger the initial state of unit 1, the greater the amplitude of the oscillation. B. State space containing 25 randomly chosen initial states (25 ‘conditions’). Symbol size/color indicates the initial firing rate of unit 1. For the simulations below, activity evolved counterclockwise from the initial state: x (t+1) = W x (t), where x is the 2-dimensional vector of unit activities, and the matrix W = [1 - 2π/360; 2π/360 1]. Thus, the state rotates one degree with each time-step. C. Activity of unit 1 versus time for the initial states shown in B. The initial state was at first held constant (as if W were the identity matrix) to emulate preparatory activity. The dynamics were then released to produce sinusoidal ‘peri-movement’ activity. Asterisks indicate the same two conditions as in B. D. The pattern of initial states (the ‘preparatory tuning’) from C is captured by a PD in peri-movement space. Analysis/format are the same as for figure 5C . Traces on each axis plot the time-evolving pattern correspondin
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/15c848b5-b666-4bc8-92b7-4a2fdf18ea0e/tool-results/bci7owl4d.txt"
}
```

```
1	black bar : performance when data were randomly subdivided. D. PD consistency for the peri-movement space versus that for a variety of other spaces. Kinematic and EMG spaces were chosen because they had performed the best overall (after the peri-movement space) in the analysis in Fig. 6 . ‘ Targs. + inst. speed ’ and ‘ segment directions ’ spaces were chosen because they performed well for the speed and maze tasks respectively. ‘ Targs. + inst. speed ’ was undefined for the maze task; the similar ‘ endpoints + max. spd. ’ space was analyzed instead. Figure 8 Illustration of the behavior of a simple linear dynamical system: a harmonic oscillator. A. Changes in the initial state produce a linear scaling of the subsequent activity pattern. In this case, the larger the initial state of unit 1, the greater the amplitude of the oscillation. B. State space containing 25 randomly chosen initial states (25 ‘conditions’). Symbol size/color indicates the initial firing rate of unit 1. For the simulations below, activity evolved counterclockwise from the initial state: x (t+1) = W x (t), where x is the 2-dimensional vector of unit activities, and the matrix W = [1 - 2π/360; 2π/360 1]. Thus, the state rotates one degree with each time-step. C. Activity of unit 1 versus time for the initial states shown in B. The initial state was at first held constant (as if W were the identity matrix) to emulate preparatory activity. The dynamics were then released to produce sinusoidal ‘peri-movement’ activity. Asterisks indicate the same two conditions as in B. D. The pattern of initial states (the ‘preparatory tuning’) from C is captured by a PD in peri-movement space. Analysis/format are the same as for figure 5C . Traces on each axis plot the time-evolving pattern corresponding to that PC (black and blue traces for units one and two). The pattern at the end of the arrow is the weighted sum of the two PCs, with weights corresponding to the PD. This work was supported by a Helen Hay Whitn
[... 695 more lines not kept]
```

**Agent**

The full text, Methods and supplement are all present. Next I'll check what the registry says about dataset 000140 and look at a sibling claims file.

**Agent calls Bash**

```bash
cd  grep -rl "000140" --include=*.yaml --include=*.json --include=*.md . 2>/dev/null | grep -v node_modules | head; ls claims | head -50; grep -i -n "github\|code avail\|software" paper/10.1016-j.neuron.2010.09.015.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -B3 -A25 "000140" papers/manifest.yaml | head -80; ls claims/000138 claims/000139 claims/000128;
```

```
399-    source: europe_pmc+crossref (paper-text-fetcher)
400-    pdf: false
401-    supplements: 0
402:  '000140':
403-  - doi: 10.1016/j.neuron.2010.09.015
404-    status: stored
405-    version: as served by ncbi_pmc
406-    source: ncbi_pmc+crossref (paper-text-fetcher)
407-    pdf: false
408-    supplements: 1
409-  - doi: 10.1038/nature11129
410-    status: stored
411-    version: as served by europe_pmc
412-    source: europe_pmc+crossref (paper-text-fetcher)
413-    pdf: false
414-    supplements: 0
415-  '000147':
416-  - doi: 10.7554/elife.74478
417-    status: stored
418-    version: as served by europe_pmc
[... 17 more lines not kept]
```

**Agent**

Three sibling dandisets (000128, 000138, 000139) already have claims for this paper. I'll check the 000139 header for how the dataset is described.

**Agent calls Bash**

```bash
cd  head -60 claims/000139/*.yaml; grep -n "^- id:\|^  data:" claims/000139/*.yaml; grep -n -i "000140\|MC_Maze" transcripts/000139/claims.md | head
```

```
<persisted-output>
Output too large (37.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/15c848b5-b666-4bc8-92b7-4a2fdf18ea0e/tool-results/b6tkkupvr.txt

Preview (first 2KB):
# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000139.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol as stated in docs/protocol.md (version pilot-12).
#
# Text read: the NIH author manuscript in PubMed Central (PMC2991102), as extracted to
# paper/10.1016-j.neuron.2010.09.015.txt, with its Results, Methods, figure legends and the one
# supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1 to 5, Supplemental Text and
# Supplemental Experimental Procedures). Not the version of record. The figures themselves are not
# in the text; values plotted only in Figures 4, 6 and 7 are not available and no claim rests on
# them. The paper links no code, so every method below comes from the Methods, the legends or the
# supplement.
#
# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
# Procedures). Three adult male rhesus monkeys (A, B, J), delayed reaches from a central touch spot
# to a target on a fronto-parallel screen. Trial events: target onset (the target jitters), go cue
# (jitter stops and the touch spot disappears), movement onset. Delays about 0 to 1000 ms; only
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; sed -n 1,60p tools/claims_check.py
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
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
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
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
cd  python3 -c "
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
cd  grep -rn -i "000140" transcripts/000139/claims.md transcripts/000130/author.md | head -5; grep -rn -i "mc_maze" queue targets entries 2>/dev/null | head
```

```
transcripts/000139/claims.md:147:ls claims/000128 claims/000138 claims/000140 claims/000129 2>&1; grep -l "neuron.2010" -r claims | head
transcripts/000139/claims.md:152:ls: cannot access 'claims/000140': No such file or directory
transcripts/000130/author.md:569:ts vs set-ready max abs diff ms 23.500000000140062
targets/dandisets.json:1118:   "name": "MC_Maze: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching",
targets/dandisets.json:1203:   "name": "MC_Maze_Large: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching",
targets/dandisets.json:1236:   "name": "MC_Maze_Medium: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching",
targets/dandisets.json:1269:   "name": "MC_Maze_Small: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching",
entries/000128-churchland-2010/reproduce_churchland_2010.ipynb:14:    "**Dataset.** DANDI:000128 (MC_Maze, Neural Latents Benchmark), version `0.220113.0400`,\n",
entries/000128-churchland-2010/entry.yaml:6:  000128 (MC_Maze), which holds the J-array session of monkey Jenkins on the maze task, recorded with two
entries/000128-churchland-2010/README.md:4:be tested on [DANDI:000128](https://dandiarchive.org/dandiset/000128/0.220113.0400) (MC_Maze), which
entries/000128-churchland-2010/mcmaze.py:1:"""Loading and measures for dandiset 000128 (MC_Maze, monkey Jenkins, maze task, two Utah arrays).
entries/000139-churchland-2010/maze.py:1:"""Loading and measures for dandiset 000139 (MC_Maze_Medium), used to test
entries/000139-churchland-2010/reproduce_churchland_2010.ipynb:8:    "# Churchland et al. (2010) on dandiset 000139 (MC_Maze_Medium)\n",
```

**Agent calls Bash**

```bash
cd  sed -n 1260,1300p targets/dandisets.json
```

```
"relation": "IsDescribedBy",
     "resource_type": null,
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "000140",
   "name": "MC_Maze_Small: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching",
   "published_version": "0.220113.0408",
   "asset_count": 2,
   "size_gb": 0.03,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Rhesus monkey"
   ],
   "approaches": [
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:\|^  data:\|^  kind:" claims/000139/*.yaml
```

```
95:- id: j-array-recordings
118:- id: fig4d-mean-correlation-j-array
147:- id: fig4abc-mean-correlation-other-datasets
185:- id: fig4-broad-unimodal
202:- id: fig4e-correlation-time-course
229:- id: suppfig1-population-psth-weak-movement-tuning
244:- id: fig6d-perimovement-best-j-array
257:- id: fig6-perimovement-best-each-dimensionality
270:- id: fig6-dimensionality-peak
284:- id: fig6-maze-task-spaces
304:- id: fig6abc-perimovement-best-other-datasets
314:- id: fig6e-summary-rank
329:- id: fig6-preparatory-dimensionality
349:- id: fig7a-shuffled-space-poor
363:- id: fig7b-window-start-slide
384:- id: ap-location-no-effect-j-array
403:- id: ap-location-no-effect-other-datasets
424:- id: fig7c-anterior-posterior-performance
443:- id: prep-activity-more-anterior
452:- id: fig7d-pd-consistency
[... 4 more lines not kept]
```

**Agent**

I have what I need: full text, Methods, legends and supplement are present, and the paper links no code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000140/10.1016-j.neuron.2010.09.015.yaml",
 "content": "# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000140.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-10-28,\n# protocol as stated in docs/protocol.md.\n#\n# Text read: the NIH author manuscript in PubMed Central (PMC2991102), not the version of record,\n# as extracted to paper/10.1016-j.neuron.2010.09.015.txt: Summary, Results, Discussion, Methods,\n# figure legends, and its one supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1\n# to 5 with legends, Supplemental Text, Supplemental Experimental Procedures). The figures are not\n# in the text; values shown only in Figures 4, 6 and 7 are not stated and no expected value is\n# taken from them. The paper links no code, so every method below comes from the Methods, the\n# legends or the supplement. The archive also lists doi:10.1038/nature11129 for this dandiset;\n# these claims are for the 2010 paper only.\n#\n# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental\n# Procedures). Three adult male rhesus monkeys (A, B, J, about 10 kg) made delayed reaches on a\n# fronto-parallel screen from a central touch spot to a target. Events per trial: target onset\n# (the target jitters), go cue (jitter stops, touch spot disappears), movement onset. Delays about\n# 0 to 1000 ms; only trials with delays above 400 ms analysed. Hand tracked at 60 Hz, eye at\n# 240 Hz. Four datasets:\n#   monkeys A and B, speed task, 28 conditions (7 directions, 2 distances, 2 instructed speeds),\n#   single electrodes, 64 and 74 single units, mean 311 and 492 trials per neuron, EMG from 6 and\n#   11 recordings;\n#   monkey J, maze task, single electrodes, 172 single units, four sets of 27 conditions (about 53\n#   neurons per set; population analyses per set, then averaged), mean 388 trials per neuron, EMG\n#   from 8 recordings;\n#   monkey J-array, maze task, all 108 conditions interleaved, two 96-electrode arrays (caudal PMd,\n#   and surface M1 perhaps extending into caudal PMd), 146 single- and multi-unit isolations, mean\n#   2166 trials per neuron (2155 in the Methods), no EMG.\n# Maze conditions: one third straight reaches without barriers, one third curved around virtual\n# barriers, one third the same barrier mazes with distractor targets. For the maze task only trials\n# whose horizontal and vertical velocity profiles correlate with a reference proto-trial at r > 0.9\n# were kept (typically about 90%). Measured variables: spike times per unit, hand position, the\n# trial events, condition identity; EMG for A, B and J only.\n#\n# The dandiset's archive title is \"MC_Maze_Small: macaque primary motor and dorsal premotor cortex\n# spiking activity during delayed reaching\" (Neural Latents Benchmark). By that title it is meant to\n# hold maze-task array recordings of monkey J, that is a part of the J-array dataset. Claims about\n# monkeys A, B and the single-electrode J recordings, and claims that need EMG, are listed because\n# they are findings of the paper; the author finds what the dandiset holds.\n#\n# Method details fixed by the paper and used throughout (Methods; Supplemental Experimental\n# Procedures): spike trains smoothed with a 20 ms Gaussian before averaging; condition means\n# computed separately locked to target onset, go cue and movement onset; preparatory rate is the\n# mean from 200 ms before to 100 ms after the go cue; peri-movement rate (for correlations) the mean\n# from 100 ms before to 350 ms after movement onset; trials with delay > 400 ms; inclusion of\n# J-array units with > 5 spikes/s of preparatory tuning (10 spikes/s for single electrodes).\n# Details the paper leaves open, used by several claims, with the readings named:\n#   O1 \"spikes/s of preparatory tuning\" is not defined. Readings: (a) the range (maximum minus\n#      minimum) of the preparatory rate across conditions; (b) its standard deviation across\n#      conditions.\n#   O2 \"robust peri-movement tuning (at least 1.5 times as strong as preparatory tuning)\" uses the\n#      same undefined measure. Readings follow O1, applied to (i) the peri-movement epoch means, or\n#      (ii) the largest across-condition range or SD at any time from 100 ms before to 350 ms after\n#      movement onset.\n#   O3 movement onset is not defined in this paper (it cites Churchland et al., 2006c). Readings:\n#      (a) the movement-onset time the dataset provides; (b) the first time hand speed exceeds a\n#      fixed fraction of its peak on that trial, the fraction stated in the notebook.\n#   O4 the proto-trial for the maze trial filter is not defined. Readings: (a) per condition, the\n#      trial whose velocity profile best correlates with the condition mean; (b) the condition mean\n#      itself; (c) no filter, when the dandiset holds only trials already kept.\n#   O5 the time step of the T matrices is not given; 10 ms samples of the 20 ms smoothed rates are\n#      used as a standard choice that should not change the outcome.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000140\"\npaper: doi:10.1016/j.neuron.2010.09.015\nclaims:\n- id: fig4d-mean-correlation-j-array\n  statement: For the J-array dataset, the correlation across conditions between a unit's\n    preparatory and peri-movement firing rates is positive on average but small (mean Pearson r =\n    0.13, p = 0.03; mean Spearman r = 0.11).\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 1; Figure\n    4D\n  quote: Across the four datasets the mean correlation was positive (p=0.01, p=0.01, p=0.12, p=0.03)\n    but only very modestly so (mean r = 0.21, 0.19, 0.06 and 0.13). Non-parametric correlations\n    were similarly modest (mean Spearman's r = 0.20, 0.20, 0.06 and 0.11)\n  statistics:\n  - about: mean Pearson correlation against zero, J-array\n    test: not named\n    p: 0.03\n    n: J-array units passing the preparatory and peri-movement tuning criteria (count not given)\n  expected:\n  - quantity: mean Pearson r, J-array\n    value: 0.13\n    tolerance: 0.013\n  - quantity: mean Spearman r, J-array\n    value: 0.11\n    tolerance: 0.011\n  criterion: Per unit, the vector of condition-mean preparatory rates (200 ms before to 100 ms\n    after the go cue) is correlated with the vector of condition-mean peri-movement rates (100 ms\n    before to 350 ms after movement onset), Methods. Units with > 5 spikes/s of preparatory tuning\n    and peri-movement tuning at least 1.5 times as strong (Methods), under readings O1 and O2;\n    trials with delay > 400 ms; trial filter under O4; movement onset under O3. The test of the\n    mean against zero is not named; readings are (a) a two-sided one-sample t-test on r, (b) the\n    same on Fisher z-transformed r, (c) a two-sided Wilcoxon signed-rank test. Reproduced when,\n    under one reading, both means are within tolerance and the mean is positive at p < 0.05;\n    partially reproduced when the mean is positive at p < 0.05 and below 0.3 but outside\n    tolerance. Fewer conditions than the paper's 108 make r noisier per unit; the number of\n    conditions and units used is reported.\n- id: fig4abc-mean-correlation-other-datasets\n  statement: For the monkey A, B and J single-electrode datasets, mean preparatory to peri-movement\n    tuning correlations are small (Pearson r = 0.21, 0.19 and 0.06, p = 0.01, 0.01 and 0.12;\n    Spearman r = 0.20, 0.20 and 0.06).\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 1; Figure\n    4A to 4C\n  quote: Across the four datasets the mean correlation was positive (p=0.01, p=0.01, p=0.12, p=0.03)\n    but only very modestly so (mean r = 0.21, 0.19, 0.06 and 0.13)\n  statistics:\n  - about: monkey A, mean r against zero\n    test: not named\n    p: 0.01\n  - about: monkey B, mean r against zero\n    test: not named\n    p: 0.01\n  - about: monkey J, mean r against zero\n    test: not named\n    p: 0.12\n  expected:\n  - quantity: mean Pearson r, monkey A\n    value: 0.21\n    tolerance: 0.021\n  - quantity: mean Pearson r, monkey B\n    value: 0.19\n    tolerance: 0.019\n  - quantity: mean Pearson r, monkey J\n    value: 0.06\n    tolerance: 0.006\n  - quantity: mean Spearman r, monkey A\n    value: 0.20\n    tolerance: 0.02\n  - quantity: mean Spearman r, monkey B\n    value: 0.20\n    tolerance: 0.02\n  - quantity: mean Spearman r, monkey J\n    value: 0.06\n    tolerance: 0.006\n  criterion: As fig4d-mean-correlation-j-array, with the single-electrode inclusion of 10\n    spikes/s of preparatory tuning (Methods); for monkey J the correlation is computed within each\n    27-condition set. These data are single-electrode recordings and are expected outside this\n    dandiset.\n- id: fig4-broad-near-zero\n  statement: Correlations between preparatory and peri-movement tuning span a broad range centred\n    near zero, with no separate populations of concordant (r near 1) and opposing (r near -1)\n    tuning; most neurons have weakly correlated tuning.\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraphs 3 and 4;\n    Figure 4A to 4D\n  quote: different neurons show markedly different relationships between preparatory and\n    peri-movement activity, with a broad range of correlations centered near zero ... Instead, most\n    neurons have weakly correlated tuning\n  depends_on:\n  - fig4d-mean-correlation-j-array\n  criterion: The paper gives no test; the judgement rule is fixed here. On the J-array units and\n    correlations of fig4d-mean-correlation-j-array, reproduced when the median r lies between\n    -0.3 and 0.3, the interquartile range spans at least 0.3, and fewer than 15% of units have r\n    above 0.8 or fewer than 15% below -0.8 (no cluster at either end). The histogram is shown in\n    bins of 0.1, a standard choice.\n- id: fig4e-correlation-time-course\n  statement: When peri-movement activity is taken at single time points, its correlation with\n    preparatory tuning starts to fall about 200 ms before movement onset and is near zero by\n    movement onset.\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 2; Figure\n    4E\n  quote: The correlation with preparatory activity began to decline ... prior to movement onset,\n    and reached values near zero by movement onset\n  depends_on:\n  - fig4d-mean-correlation-j-array\n  criterion: As the Figure 4E legend and Supplemental Experimental Procedures say, the rate at a\n    single time point of the 20 ms smoothed condition means, swept along the trace spliced from the\n    go-locked and movement-locked means, correlated per unit with the preparatory rate vector, and\n    averaged over units. Which units are averaged is not stated; readings are (a) the units of\n    Figure 4A to 4D, (b) all units with > 5 spikes/s preparatory tuning. Judgement thresholds fixed\n    here, as the paper gives none. Reproduced when the mean correlation at movement onset is below\n    0.1 and below half its value at 200 ms before onset, and the largest drop over any 50 ms step\n    begins between 300 ms before and movement onset; partially reproduced when the correlation\n    falls toward movement onset but stays above 0.1.\n- id: suppfig1-population-averages-lose-tuning\n  statement: Population-average PSTHs grouped by each neuron's preparatory preference show weak\n    peri-movement differences that shrink with time, with little relationship to preparatory\n    tuning by movement onset.\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 3;\n    Supplemental Figure 1\n  quote: In population averages ( Supp. Fig. 1 ) the lack of correlation averages out and the means\n    are dominated by the weak agreement between preparatory and peri-movement tuning. However, such\n    effects grow dramatically smaller with time. By movement onset even population averages show\n    little relationship with preparatory tuning\n  depends_on:\n  - fig4d-mean-correlation-j-array\n  criterion: As the Supplemental Figure 1 legend says, for each unit of fig4d-mean-correlation-j-array\n    the conditions with the strongest and weakest preparatory response and two intermediate ones\n    (taken here as the conditions at the 1/3 and 2/3 ranks, a choice the legend leaves open) are\n    found, each unit's rates normalised by its maximum rate, and averaged across units. Reproduced\n    when the spread between the strongest and weakest averaged traces at movement onset is less\n    than half the spread in the preparatory epoch, with the strongest-preparatory trace still on\n    top at 150 ms before movement onset. The unnormalised average is shown as a variant (the\n    legend says results were similar).\n- id: fig6d-perimovement-best-j-array\n  statement: For the J-array dataset, the cross-validated performance of a preferred direction in\n    capturing preparatory tuning is highest when the PD is expressed in the PCA-based\n    peri-movement space, compared with the kinematic space and the task spaces.\n  source: Results, PD performance in a variety of spaces, paragraphs 1 to 3; Figure 6D\n  quote: For every dataset, the highest level of performance was achieved ... when PDs were\n    expressed in the peri-movement space\n  criterion: Methods, Using a PD to capture preparatory tuning, PCA-based spaces and PD\n    performance. Per unit (> 5 spikes/s preparatory tuning under O1, no peri-movement\n    criterion), the preparatory rate vector is regressed on a c x k matrix S of condition\n    locations plus an offset, with leave-one-condition-out cross-validation; performance is one\n    minus the mean squared prediction error divided by the variance of the preparatory rates\n    across conditions; averaged over units. The peri-movement space is the first k PC scores of\n    the c x nt matrix of condition-mean rates from 150 ms before to 800 ms after movement onset\n    of all units except the one fitted, not normalised, columns mean-centred (Supplemental Text).\n    The kinematic space is the PC scores of a c x 2t-style matrix of horizontal and vertical hand\n    position, velocity and acceleration from 150 ms before movement onset to the end of the reach,\n    each variable scaled to unit range across times and conditions; the Methods say each neuron\n    contributed one kinematic variable so the matrix matches the neural one in size, which is read\n    as (a) the six variables each repeated equally to about n columns, or (b) the six variables\n    once, as the stated scaling makes repetition change only the relative weights; the end of the\n    reach is taken as 600 ms after movement onset (Figure 1 legend, reaches last about 200 to\n    600 ms) or as 800 ms, the neural window. Task spaces for the maze task as listed in Methods,\n    Task spaces (initial velocity, endpoints + maximum speed, endpoints + orthogonal excursion,\n    endpoints + viapoint, endpoints + maximum velocity, endpoints + halfpoint, segment directions,\n    kitchen sink of 11 dimensions with barrier and distractor flags). PCA dimensionalities tested\n    are not listed; readings are k = 1 to 14 (the range the Results give) and k = 1 to 20. Time\n    step under O5. Reproduced when, under each reading, the best peri-movement performance\n    over k exceeds the best kinematic performance and every task space; partially reproduced when\n    it exceeds all but one. No EMG space can be built for J-array (no EMG recorded).\n- id: fig6abc-perimovement-best-other-datasets\n  statement: For the monkey A, B and J single-electrode datasets as well, PD performance is best\n    in the peri-movement space, including against the PCA-based EMG space.\n  source: Results, PD performance in a variety of spaces, paragraph 3; Figure 6A to 6C\n  quote: performance was nearly always best for the space derived from the population-level\n    peri-movement response. For every dataset, the highest level of performance was achieved\n  criterion: As fig6d-perimovement-best-j-array, with the speed-task window ending 400 ms after\n    movement onset, the speed-task task spaces including targets + instructed speed, the EMG space\n    built as the Methods say (all muscles, same window, each muscle scaled to unit range), and for\n    monkey J the analysis done per 27-condition set and averaged. These are single-electrode data\n    with EMG, expected outside this dandiset.\n- id: fig6-perimovement-best-each-dimensionality\n  statement: Taken one dimensionality at a time, performance is almost always higher in the\n    peri-movement space than in other spaces of the same dimensionality, the exception being the 3-D\n    targets + instructed speed and endpoints + maximum speed spaces for the speed task.\n  source: Results, PD performance in a variety of spaces, paragraph 3; Figure 6A to 6D\n  quote: Even if we consider each dimensionality individually, performance was almost always higher\n    for the peri-movement space. An exception was that, among 3-dimensional spaces, the\n    'targs+instr. spd.' and 'endpoints + max. spd.' performed very well for the datasets collected\n    using the speed task\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: With the performances of fig6d-perimovement-best-j-array, for each k from 1 to 12\n    the peri-movement space is compared with the kinematic space at the same k and with every task\n    space of that dimensionality. \"Almost always\" is judged here as at least 80% of these\n    comparisons won by the peri-movement space, under each reading of fig6d.\n- id: fig6-maze-endpoint-speed-space-poor\n  statement: In the maze task the endpoints + maximum speed space, which did well for the speed\n    task, does not perform well.\n  source: Results, PD performance in a variety of spaces, paragraph 3; Figure 6C and 6D\n  quote: The former is undefined for the maze task, but the latter did not perform well\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: From fig6d-perimovement-best-j-array. \"Did not perform well\" is judged here as\n    performance of the 3-D endpoints + maximum speed space below that of the 3-D peri-movement\n    space by at least 0.1 and below half of the best peri-movement performance over k.\n- id: fig6-dimensionality-trend\n  statement: Performance of the PCA-based spaces typically improves with dimensionality and then\n    declines above about 10 dimensions, an indication of overfitting.\n  source: Results, PD performance in a variety of spaces, paragraph 2; Figure 6A to 6D\n  quote: Performance typically improved with dimensionality ... Performance typically declined at\n    dimensionalities >10, an indication of over-fitting\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: From the peri-movement and kinematic performance curves of\n    fig6d-perimovement-best-j-array over k = 1 to 20. Reproduced when, for the peri-movement\n    space, performance at its best k exceeds performance at k = 2 and the best k lies between 3 and\n    14 (the range the Results give for k), and performance at k = 20 is below the best; partially\n    reproduced when only the rise holds.\n- id: fig6e-summary-rank\n  statement: Across monkeys A, B and J, the peri-movement space gives the highest average\n    performance at every dimensionality limit (3, 6, 12), followed by the PCA-based kinematic and EMG\n    spaces, with the task spaces worst; other spaces are significantly worse than the best.\n  source: Results, PD performance in a variety of spaces, paragraph 4; Figure 6E and legend\n  quote: Performance (averaged across neurons) was highest when the PD employed the space based on\n    peri-movement neural activity ... the task spaces were largely outcompeted by the PCA-based\n    kinematic and EMG spaces, which were in turn outperformed by the peri-movement space\n  statistics:\n  - about: other spaces against the best space (asterisks)\n    test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: neurons of monkeys A, B and J\n  criterion: Figure 6E excludes J-array (no EMG). For each limit (3, 6, 12), the best PCA-based\n    performance with k up to the limit and each task space defined for all three datasets at or\n    under the limit, averaged over neurons of A, B and J; SEs across neurons. The test behind the\n    asterisks is not named; readings are (a) paired t-test across neurons and (b) Wilcoxon\n    signed-rank test, each against the best space. Not testable unless the dandiset holds the\n    single-electrode and EMG data. As a variant on J-array, the same ranking without EMG is\n    reported.\n- id: prep-dimensionality-7-to-10\n  statement: Preparatory activity is moderately high dimensional; depending on the dataset 7 to 10\n    dimensions capture 90% of its variance.\n  source: Supplemental Experimental Procedures, Estimating the upper limit of PD performance;\n    Results, PD performance in a variety of spaces, paragraph 2\n  quote: depending on the dataset, 7-10 dimensions were required to capture 90% of the data variance\n  expected:\n  - quantity: PCs needed for 90% of variance of the c x n preparatory matrix\n    value: 8.5\n    tolerance: 2.5\n  criterion: PCA of the c x n matrix of condition-mean preparatory rates (one row per condition),\n    as the supplement defines it, on the units of fig6d-perimovement-best-j-array. The number of\n    components whose cumulative explained variance first reaches 90%. The tolerance is the\n    reported range 7 to 10 widened by 10% of each bound (6.3 to 11). Whether rates are normalised\n    is not stated; the supplement's T matrices for neurons are not normalised, so unnormalised\n    is the main reading and z-scored units a variant. With fewer conditions than the paper's 108\n    the count is bounded by c - 1; this is reported.\n- id: fig7a-shuffled-space-poor\n  statement: A control peri-movement space in which each condition's peri-movement response is\n    inverted at random on half the conditions performs poorly.\n  source: Results, Controls, paragraph 1; Figure 7A and legend\n  quote: The PCA-based 'shuffled-space' performed poorly\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: As the Figure 7A legend says, for each unit and condition, with probability 0.5 the\n    activity after 150 ms before movement onset is reflected vertically around the rate at that\n    time; the shuffled T matrix is then used as the peri-movement space. Whether the coin is drawn\n    per unit and condition (the legend's wording) or per condition for all units is read the first\n    way, with the second as a variant. Twenty random shuffles, a standard choice. Reproduced when\n    the best shuffled performance over k is below half the best intact peri-movement performance\n    and below the best kinematic performance.\n- id: fig7b-window-start-slide\n  statement: Sliding the start of the peri-movement window later costs little; with the window\n    starting at movement onset, performance is still 97% (monkey J) and 94% (monkeys A, B) of its\n    original value.\n  source: Results, Controls, paragraph 1; Figure 7B\n  quote: Even when the window began at movement onset ... performance was still at 97% (monkey J),\n    and 94% (monkeys A, B) of its original value\n  expected:\n  - quantity: performance with window starting at movement onset, relative to start at -150 ms, monkey J\n    value: 0.97\n    tolerance: 0.097\n  - quantity: same ratio, monkeys A and B\n    value: 0.94\n    tolerance: 0.094\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: As the Figure 7B legend says, performance averaged across neurons at the best k for\n    each start time, with the window end fixed. \"Monkey J\" can be read as (a) the J-array dataset,\n    (b) the single-electrode J dataset only, or (c) both averaged; on this dandiset only (a) can\n    be computed, so the J value is compared under reading (a). Reproduced when the ratio is within\n    tolerance.\n- id: ap-location-no-effect-j-array\n  statement: For J-array, the preparatory to peri-movement tuning correlation does not depend on\n    anterior-posterior recording location (r = 0.20, p = 0.27).\n  source: Results, Comparison of anterior versus posterior sites, paragraph 1\n  quote: Regressing tuning correlation (as in Figure 4 ) against AP location yielded little or no\n    effect ... and r =0.20, p =0.27 for the four datasets\n  statistics:\n  - about: J-array, tuning correlation regressed on AP location\n    test: linear regression\n    statistic: r = 0.20\n    p: 0.27\n  depends_on:\n  - fig4d-mean-correlation-j-array\n  criterion: A claim of absence. The per-unit correlations of fig4d-mean-correlation-j-array are\n    regressed on each unit's anterior-posterior location (Pearson r, two-sided p of the slope).\n    Reproduced when p >= 0.05; the r is reported either way. The AP location of an array unit is\n    its electrode's position along the anterior-posterior axis; if the dandiset gives only array\n    identity (PMd or M1), the two-group comparison of correlations by a two-sided t-test is\n    shown as a variant.\n- id: ap-location-no-effect-other-datasets\n  statement: For monkeys A, B and J, tuning correlation is not related to anterior-posterior location\n    (r = -0.05, -0.03, -0.07; p = 0.82, 0.85, 0.52).\n  source: Results, Comparison of anterior versus posterior sites, paragraph 1\n  quote: Regressing tuning correlation (as in Figure 4 ) against AP location yielded little or no\n    effect: r =-0.05, p =0.82; r =-0.03, p =0.85; r =-0.07, p =0.52\n  statistics:\n  - about: monkey A\n    test: linear regression\n    statistic: r = -0.05\n    p: 0.82\n  - about: monkey B\n    test: linear regression\n    statistic: r = -0.03\n    p: 0.85\n  - about: monkey J\n    test: linear regression\n    statistic: r = -0.07\n    p: 0.52\n  depends_on:\n  - fig4abc-mean-correlation-other-datasets\n  criterion: As ap-location-no-effect-j-array, with each penetration's AP coordinate. These\n    single-electrode data are expected outside this dandiset.\n- id: fig7c-anterior-posterior-performance\n  statement: The peri-movement space captures preparatory tuning at both anterior and posterior\n    sites, with normalised performance slightly better at anterior sites.\n  source: Results, Comparison of anterior versus posterior sites, paragraph 1; Figure 7C and legend\n  quote: The ability of the peri-movement space to capture tuning also held for both anterior and\n    posterior sites ( Figure 7C ) ... Performance was slightly better at anterior sites\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: As the Figure 7C legend says, a six-dimensional peri-movement space; units split at the\n    median AP location (>= median anterior, <= median posterior); performance normalised by its\n    upper limit (the PCA space of the c x n preparatory matrix of all units, Supplemental\n    Experimental Procedures) and compared with random halves. Whether the space for a half is\n    built from that half's units or from all units is open; both are run. Reproduced when both\n    halves reach at least 70% of the normalised performance of random halves (judgement fixed\n    here) and the anterior half is not lower than the posterior by more than 0.05.\n- id: prep-activity-more-anterior\n  statement: Preparatory activity is more prevalent at anterior sites.\n  source: Results, Comparison of anterior versus posterior sites, paragraph 1\n  quote: We similarly found preparatory activity to be more prevalent at anterior sites (data not\n    shown)\n  criterion: Data not shown, so no method is given. Read here as the fraction of units passing the\n    > 5 spikes/s preparatory tuning criterion (O1) being higher among units anterior of the median\n    AP location than posterior of it, tested by a two-sided Fisher exact test at p < 0.05;\n    partially reproduced when higher without significance.\n- id: fig7d-pd-consistency\n  statement: The PD measured on two random sets of 25 conditions is more stable (higher dot product)\n    in the peri-movement space than in the task, kinematic and EMG spaces, for every comparison and\n    every dataset.\n  source: Results, Stability of the PD, paragraphs 1 and 2; Figure 7D and legend\n  quote: Yet for every comparison, and for all four datasets, the PD was most stable when measured\n    in the peri-movement space\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: Per unit, 25 conditions drawn with replacement, the PD fitted (unit-length b), another\n    25 drawn and the PD refitted; consistency is the dot product, averaged over units (Results,\n    Stability of the PD). Spaces for the maze task as Figure 7D legend gives them, endpoints + max.\n    spd. and segment directions, and the kinematic space at its best k from Figure 6; the\n    peri-movement space at the same dimensionality as each comparison space. The number of\n    repeats per unit is not given; 100, a standard choice. Reproduced when on J-array the\n    peri-movement space is more consistent than each comparison space. If the dandiset has fewer\n    than 25 conditions, drawing 25 with replacement still follows the text and is reported as\n    such.\n- id: fig8-linear-dynamics-simulation\n  statement: In a simulated two-unit rotational linear system with 25 random initial states, the\n    single-unit correlation between initial (preparatory) and later (peri-movement) activity is\n    near zero (0.08), yet a PD in the PCA-based peri-movement space captures the initial state\n    perfectly.\n  source: Results, Tuning from a dynamical systems perspective, paragraphs 2 and 3; Figure 8 and\n    legend\n  quote: The correlation of preparatory activity with peri-movement activity (averaged over the\n    gray interval) was 0.08 ... The PD points towards the pattern recruited by the activity of unit\n    one (panel A ), and perfectly captures preparatory\n  expected:\n  - quantity: correlation of unit 1 initial rate with mean later rate across 25 conditions\n    value: 0.08\n    tolerance: 0.3\n  criterion: A simulation, using no recorded data. x(t+1) = W x(t) with W = [1, -2pi/360; 2pi/360,\n    1] (Figure 8 legend), 25 random initial states. The distribution of initial states, the\n    length of the hold and the gray averaging interval are not given, so the single value 0.08\n    depends on random draws; the tolerance of 0.3 is set wide for that reason and the criterion\n    is the distribution over 1000 simulations (initial states uniform in the unit disk and in a\n    square, interval of 360 steps), reproduced when the median |r| is below 0.3 and the PD in the\n    2-D PCA space of the released trajectories gives cross-validated performance above 0.99.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000140/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt; grep -n "—\|rather" claims/000140/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000140/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    effect: r =-0.05, p =0.82; r =-0.03, p =0.85; r =-0.07, p =0.52",
 "new_string": "    effect ... r =-0.05, p =0.82; r =-0.03, p =0.85; r =-0.07, p =0.52"
}
```

```
The file claims/000140/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000140/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt; grep -n "^    .*: \|—\|rather" claims/000140/*.yaml | grep -v "^[0-9]*:  *- \|^[0-9]*:    [a-z_]*: "
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/000140/10.1016-j.neuron.2010.09.015.yaml`. The quote checker reports 20 claims, 20 quotes, 9 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the NIH author manuscript in PubMed Central (PMC2991102), not the version of record. That covers the Results, Discussion, Methods, figure legends and the one supplement (Supplemental Figures 1 to 5, the Supplemental Text and the Supplemental Experimental Procedures). The paper links no code, so every method comes from the Methods, the legends or the supplement. The archive names this dandiset MC_Maze_Small, which the file reads as part of the monkey J maze-task array data ("J-array"). The opening comment describes all four datasets as the paper reports them.

**Claims.**
- **Quotes:** all 20 claims have one, so none needed `inferred`.
- **Statistics:** 6 claims record them:
  - the mean tuning correlation tests (p = 0.03 for J-array; 0.01, 0.01 and 0.12 for A, B and J);
  - the regressions on anterior-posterior location (four r and p pairs);
  - the Figure 6E asterisks (p < 0.001).
- **Expected values:** 5 claims carry them: mean Pearson and Spearman r per dataset, the 7 to 10 dimensions for 90% of preparatory variance, the 97% and 94% ratios in Figure 7B, and the simulated r = 0.08.
- **Criteria:** 18 claims have one.
- **Data elsewhere:** the claims for monkeys A, B and single-electrode J, and those needing EMG (Figures 6A to 6C and 6E), are listed but are probably not in this dandiset. The Figure 8 claim is a simulation and uses no recorded data.

**Details the paper leaves open, with the readings named:**
- **O1, "spikes/s of preparatory tuning":** the range across conditions, or the standard deviation across conditions.
- **O2, peri-movement tuning "1.5 times as strong":** O1 applied to the epoch means, or to the largest value over time within the window.
- **O3, movement onset:** the dataset's marker, or a speed-threshold onset.
- **O4, the maze "proto-trial" filter:** the best-matching trial, the condition mean, or no filter if the trials are already curated.
- **O5, time step of the matrices:** 10 ms, a standard choice.
- **Test behind the correlation p-values:** one-sample t-test on r, the same on Fisher-z values, or Wilcoxon signed-rank.
- **Test behind the Figure 6E asterisks:** paired t-test or Wilcoxon signed-rank.
- **Range of PCA dimensions:** 1 to 14 or 1 to 20.
- **Kinematic matrix:** each of the six kinematic variables repeated to match the neuron count, or each used once; the window ending at 600 ms or 800 ms.
- **Units in Figure 4E:** those of Figures 4A to 4D, or all tuned units.
- **Intermediate conditions in Supplemental Figure 1:** taken at the 1/3 and 2/3 ranks.
- **Shuffle in Figure 7A:** drawn per unit and condition, or per condition only.
- **"Monkey J" in the 97% figure:** the array data, the single-electrode data, or both.
- **Space used for each half in Figure 7C:** built from that half's units or from all units.
- **Normalisation for the dimensionality count:** none, or z-scored units.
- **Simulation settings:** the initial-state distribution and averaging interval.

Where the paper gives no test (the broad distribution in Figure 4, "near zero", "almost always", "poorly"), the criterion sets its own threshold and says so.

**Missing from the paper.** Values shown only in the figures (the Figure 4 histograms, the Figure 6 and 7 performance curves) are never stated in the text, so no expected value rests on them. Unit counts after the inclusion criteria are not given. Anterior-posterior locations for the units are not given. The "more preparatory activity at anterior sites" finding is "data not shown", so the method used to test it is set in the criterion.

## End of run

20 turns, 4 minutes, result: success.
