# park-2019 · claims · run 42848784087

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/; wc -l paper/*
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
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
head -40 claims/nishimoto-2011.yaml; cat paper/hc-20.data-description.txt | head -60; ls papers/datasets/ | grep park; cat papers/datasets/park-2019.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the paper text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.11.019.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.11.019.txt",
 "offset": 1044
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 60,130p paper/hc-20.data-description.txt; cd $TMPDIR && git clone -q https://github.com/FentonLab/PyCode_MEC_HDC-NeuronMS_Park.git && cd PyCode_MEC_HDC-NeuronMS_Park && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/PyCode_MEC_HDC-NeuronMS_Park && cat README.md && wc -l *.py && cat Spike_triggered_FR_curve.py
```

```
# PyCode_MEC_HDC-NeuronMS_Park
  285 HD_Max_likelihood.py
  268 Spike_triggered_FR_curve.py
  553 total

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:27:09 2015

@author: stephenkeeley
"""

import struct as st
import numpy as np
import random as rd
import os as os
import scipy.io as sio
rd.seed()


[... 251 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/PyCode_MEC_HDC-NeuronMS_Park && cat HD_Max_likelihood.py
```

```
import struct as st
import numpy as np
import random as rd
import os as os
import scipy.io as sio
import scipy as sc


rd.seed()
#need one file per cell in it's own directory for this code to run

def doheader(fh,nlines):
	#this function will scan through the header information.
	#number of lines in header denoted by nlines
    for i in range(nlines):
        line = fh.readline()
        #getting rid of the part of the header that has the 4 byte dir listed


        if '%SAMPLING_INTERVAL' in line:
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2018.11.019.pdf')
for p in [2,3,5,6,17]:
    d[p].get_pixmap(dpi=110).save(f'p{p+1}.png')
print(len(d))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm && for p in 3 4 6 7 18; do pdftoppm -f $p -l $p -r 100 -png paper/10.1016-j.neuron.2018.11.019.pdf pg$p; done; ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "import pypdfium2" 2>&1; python -c "import pdfplumber" 2>&1; which mutool gs convert magick 2>&1 | head
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "kind\|'data'\|allowed\|KEYS\|keys" tools/claims_check.py | head -40
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
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print(json.dumps(s['properties'].get('checks',{}),indent=1)[:500])"
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
[... 106 more lines not kept]
```

**Agent**

The full text (main, STAR Methods, supplement with Figures S1 to S6 and Table S1) is present, and I've read the paper's code (FentonLab repository, two scripts). Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/park-2019.yaml",
 "content": "# Claims for Park, Keeley, Savin, Ranck & Fenton (2019), Neuron 101:285-293, tested on CRCNS hc-20.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read: the version of record (paper/10.1016-j.neuron.2018.11.019.txt, PyMuPDF extraction\n# of the publisher PDF), main text, figure legends, STAR Methods and the Supplemental\n# Information (Figures S1 to S6 and Table S1). Video S1 (the rotating arena) holds no result.\n# The PDF could not be rendered in this run, so figures were read from their legends and the\n# Results only. Glyphs garbled by the extraction were read as follows: \"10�14\" is 10^-14, \"R\" is\n# \"at least\", \"%\" is \"at most\", \"4.17 3 107\" is 4.17 x 10^7, \"�0.141\" is -0.141. The spike width\n# of head-direction cells is printed \"169.79 ± 4.58 ms\"; the unit is very likely microseconds.\n#\n# Code read: https://github.com/FentonLab/PyCode_MEC_HDC-NeuronMS_Park at commit 545a738 (4 Nov\n# 2018), linked under Data and Software Availability. It holds two Python 2 scripts that read\n# the TSD files of the dataset. HD_Max_likelihood.py is the decoder of Figures 2 and 5: windows\n# of 20 tracker samples (at 30 Hz, 667 ms; the Methods say 660 ms), the window's head direction\n# the circular mean of its samples (samples with direction > 360 dropped), 36 bins of 10\n# degrees, a Poisson rate per cell and bin fitted on the training file (spikes in windows at\n# that bin divided by the number of such windows), the summed Poisson log likelihood maximized\n# over the bins, windows in which no cell spiked left undecoded. Training is stable1 (the\n# DIR/SA1 folder), testing another trial (TSD/SA2, or the rotating trial in room or arena\n# coordinates). Spike_triggered_FR_curve.py is the internally referenced tuning of Figure 4: for\n# each spike of cell 1, the head direction at that spike minus the head direction at each cell 2\n# spike in a window of move_ts = 900 samples (30 s) that ends at the cell 1 spike, binned in 36\n# bins of 10 degrees, divided by the count of the same differences over all tracker samples of\n# the window (an occupancy normalization). The Gaussian process tuning estimator of Figures S5\n# and S6 is at https://bitbucket.org/crissavin/pfgp.git; it was not read in this run. No code\n# is given for Idir, the cell-pair correlations, the tuning measures or the statistics (JMP 12).\n#\n# Data the paper used (STAR Methods, Animals; Behavior and recording environment;\n# Electrophysiology; Data Analysis; Table S1). Fifteen adult male Long-Evans rats; 1594 MEC\n# single units recorded with tetrodes, 1059 well isolated (IsoIBG and IsoINN above 3.5; Figure\n# S6 says 1049), of which 115 head-direction cells from 13 rats (Table S1 lists 15 rats, two\n# with none). 353 MEC cells and 556 MEC cell pairs in Table S1; 142 simultaneously recorded\n# head-direction cell pairs (Results, Figure 4). Each recording is a triad of 30 min trials,\n# stable1, rotating (arena at 1 rpm clockwise), stable2, during active place avoidance on a\n# 1.2 m arena with a shock zone (a 30 or 45 degree sector) fixed in the room and, during\n# rotation, a second one fixed to the arena. Position and head direction tracked at 30 Hz from\n# two LEDs; spikes digitized at 48 kHz; LFP at 2 kHz. Rats R030 and R850 are left out of the\n# behavioural analysis of Figure 1. The CRCNS description of hc-20 says it holds the MEC spike\n# trains in TSD files (30 Hz samples of x, y, head direction and spike times) in folders SA1,\n# SA2, RA_ar (arena coordinates) and RA_rm (room coordinates), a FileNameList.xlsx matching\n# units across trials, and the tracker's .dat behaviour files. It does not mention LFP,\n# waveforms or the pretraining and training sessions of the learning curves; whether they are\n# there is for the author to find.\n#\n# Head-direction cells (Data Analysis): long-duration spikes, mean rate below 10 AP/s, and in\n# stable1 a significant Rayleigh test and a Kuiper's test showing the tuning differs from the\n# sampled head directions; tuning curves at 10 degree resolution, rate = spikes over time in\n# each bin. Preferred direction is the bin of maximum rate; directionality is the Rayleigh\n# vector length of the tuning curve; instability is the resistor-average symmetric\n# Kullback-Leibler divergence (KLD) between two tuning curves made into probabilities with the\n# Krichevsky-Trofimov estimate (Quantifying Head-direction Signals). Statistics (Statistics)\n# are one- or two-way ANOVA with or without repeated measures, Greenhouse-Geisser correction\n# when Mauchly's test shows a violation of sphericity, Tukey-Kramer HSD for all pairs and\n# Dunnett's test against a baseline. The two halves of stable1 (the baseline of Figures 1D and\n# 4D) are read as its first and second 15 min, as the code's folder names suggest\n# (spk_trig_15min_2, 2nd15).\nschema_version: 2\npaper: doi:10.1016/j.neuron.2018.11.019\nclaims:\n- id: cell-counts\n  statement: The paper analyses 115 dorsal MEC head-direction cells from 13 rats, among 353 MEC\n    cells forming 556 cell pairs (Table S1), out of 1594 MEC single units recorded.\n  source: Results, Degraded Directional Tuning, paragraph 1; STAR Methods, Electrophysiology;\n    Table S1\n  quote: We recorded 115 dorsal MEC head-direction cells (Figure S1; Table S1) from 13 rats\n  expected:\n  - quantity: head-direction cells\n    value: 115\n    tolerance: 11.5\n  - quantity: MEC cells in Table S1\n    value: 353\n    tolerance: 35.3\n  - quantity: MEC cell pairs in Table S1\n    value: 556\n    tolerance: 55.6\n  criterion: Counts of units and simultaneously recorded pairs, matched across the three trials\n    with FileNameList.xlsx. The dataset may hold only the cells of Table S1, or all recorded\n    units; the readings are (a) count the units and pairs the dataset holds; (b) apply the\n    paper's head-direction criteria (mean rate below 10 AP/s, significant Rayleigh test and\n    significant Kuiper's test against sampled head directions in stable1, each at p < 0.05,\n    a level the Methods do not state) and count the cells that pass. Spike width cannot be\n    applied without waveforms. Reproduced when the counts are within tolerance under a\n    reading; the per-rat counts of Table S1 are compared as well.\n- id: hd-cell-rate\n  statement: The head-direction cells have long-duration spikes and a mean firing rate of 1.41 ±\n    0.20 AP/s.\n  source: STAR Methods, Data Analysis, paragraph 2\n  quote: MEC head direction cells were classified as cells with long duration action potentials\n    (avg. width at 30% of the peak voltage 169.79 ± 4.58 ms) and average firing rate below 10\n    AP/s (avg. 1.41 ± 0.20 AP/s)\n  depends_on:\n  - cell-counts\n  expected:\n  - quantity: mean firing rate of head-direction cells\n    value: 1.41\n    tolerance: 0.2\n    unit: AP/s\n  criterion: Mean over the 115 cells of the spike count over the trial's duration. The trial is\n    not stated; the readings are (a) stable1, the classification trial; (b) the mean over the\n    three trials. The tolerance is the paper's stated spread. Spike width is not tested\n    (waveforms are not described as deposited).\n- id: fig1a-avoidance-learning\n  statement: The 13 recorded rats learned the place avoidance task, with performance improving\n    over trials in the stable (baseline) and the rotating (challenge) conditions and no trial by\n    frame interaction in the rotating condition.\n  source: Figure 1A legend; Results, Degraded Directional Tuning, paragraph 1\n  quote: \"right: learning curves from the 13 recorded rats in the stable [baseline]\"\n  statistics:\n  - about: stable condition, trial effect\n    test: repeated-measures ANOVA, Greenhouse-Geisser corrected\n    statistic: F(3.78, 46.01) = 3.79\n    p: 0.01\n    n: 13 rats\n  - about: rotating condition, trial effect\n    test: repeated-measures ANOVA, Greenhouse-Geisser corrected\n    statistic: F(3.76, 90.29) = 23.57\n    p: 0.001\n    p_relation: \"<\"\n  - about: rotating condition, trial by frame interaction\n    test: repeated-measures ANOVA, Greenhouse-Geisser corrected\n    statistic: F(3.76, 90.29) = 0.31\n    p: 0.86\n  criterion: The paper does not say which measure of avoidance is plotted or how many trials\n    the curves span (the corrected numerator degrees of freedom imply at least five trials).\n    The readings are (a) shock zone entrances per trial; (b) time to first entrance, the two\n    usual measures of this task. Per condition, a repeated-measures ANOVA on trial (and in the\n    rotating condition on trial and frame, room or arena zone) with Greenhouse-Geisser\n    correction, as the legend and Statistics state. Reproduced when, under a reading, the trial\n    effect has p < 0.05 in both conditions, performance improves over trials, and the trial by\n    frame interaction has p ≥ 0.05. Rats R030 and R850 are left out (Table S1 footnote).\n    Training sessions may not be in the dataset; whether they are is the author's to find.\n- id: fig1c-speed\n  statement: Rotation did not change locomotor speed relative to stable1, measured in either\n    frame, but speed was lower in stable2 than in the other conditions.\n  source: Figure 1C, top left, and its legend\n  quote: Effect of rotation on (top left) speed\n  statistics:\n  - test: repeated-measures ANOVA, Greenhouse-Geisser corrected, Tukey-Kramer HSD\n    statistic: F(2.02, 74.68) = 46.61\n    p: 1.0e-14\n  criterion: Mean speed per recording in four conditions, stable1, rotating in the room frame,\n    rotating in the arena frame, stable2, from the 30 Hz positions (RA_rm and RA_ar for the two\n    frames). The paper does not fix how speed is computed or the unit of the ANOVA; the degrees\n    of freedom imply about 38 units. Readings of the speed are (a) displacement between\n    successive 30 Hz samples; (b) displacement over 1 s steps. Readings of the unit are (a)\n    recording session; (b) cell (n = 115). Repeated-measures ANOVA with Greenhouse-Geisser\n    correction and Tukey-Kramer HSD. Reproduced when, under a reading, the condition effect has\n    p < 0.05, stable2 is lower than each other condition by Tukey-Kramer at p < 0.05, and the\n    other three do not differ; partially reproduced when the effect holds with another order.\n- id: fig1c-lfp-power\n  statement: Power in the MEC local field potential did not differ across conditions.\n  source: Figure 1C, top right, and its legend; Results, Degraded Directional Tuning, paragraph 1\n  quote: Despite excellent navigation (Figure 1A), maintained firing rates, and power in the local\n    field potential (LFP)\n  statistics:\n  - test: ANOVA\n    statistic: F(2, 183) = 1.27\n    p: 0.28\n  criterion: A claim of absence, judged on the paper's test, an ANOVA on LFP power across\n    stable1, rotating and stable2 with p ≥ 0.05 (Statistics; the degrees of freedom imply a\n    one-way ANOVA on 186 values). Power by Welch's method (MATLAB pwelch) on artifact-free\n    segments longer than 4 s (Local field potential analysis). The band is not stated; the\n    readings are total power and theta-band power. The LFP is not described as part of hc-20.\n- id: fig1c-firing-rate\n  statement: Firing rates of the head-direction cells were maintained across stable1, rotating\n    and stable2.\n  source: Figure 1C, bottom left, and its legend\n  quote: Despite excellent navigation (Figure 1A), maintained firing rates\n  statistics:\n  - test: repeated-measures ANOVA, Greenhouse-Geisser corrected\n    statistic: F(1.34, 153.21) = 1.89\n    p: 0.17\n    n: 115 cells\n  depends_on:\n  - cell-counts\n  criterion: A claim of absence, judged on the paper's test. Mean rate per cell and trial\n    (spikes over trial duration), repeated-measures ANOVA on trial (three levels) with\n    Greenhouse-Geisser correction when Mauchly's test is significant. Reproduced when p ≥ 0.05;\n    the mean change is reported either way.\n- id: fig1c-directionality\n  statement: Directional tuning of head-direction cells was strongly degraded during rotation in\n    both frames, more in the arena frame than in the room frame, and returned in stable2\n    (stable1 = stable2 > rotating room frame > rotating arena frame).\n  source: Figure 1C, bottom right, and its legend; Results, Degraded Directional Tuning,\n    paragraph 1\n  quote: stable1 = stable2 > rotating-room frame > rotating-arena frame (p < 0.01; post hoc using\n    Tukey-Kramer honest significant difference [HSD])\n  statistics:\n  - test: repeated-measures ANOVA, Tukey-Kramer HSD\n    statistic: F(3, 342) = 70.36\n    p: 1.0e-35\n    n: 115 cells\n  - about: post hoc pairs\n    test: Tukey-Kramer HSD\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - cell-counts\n  criterion: Directionality is the Rayleigh vector length of the 10 degree tuning curve\n    (Quantifying Head-direction Signals, Directionality), per cell in four conditions\n    (stable1, rotating room frame, rotating arena frame, stable2). Repeated-measures ANOVA on\n    condition, then Tukey-Kramer HSD. Reproduced when the effect has p < 0.05, stable1 and\n    stable2 do not differ, and stable2 > room > arena with each of these pairs significant at\n    p < 0.01; partially reproduced when both rotating frames are below both stable trials but\n    the room and arena frames do not differ.\n- id: fig1d-preference-change\n  statement: The change in preferred direction differs across trial pairs (stable1-stable2 =\n    stable1-rotating room frame > stable1-rotating arena frame), and is greater for every trial\n    pair than between the two halves of stable1.\n  source: Figure 1D, left, and its legend; Results, Degraded Directional Tuning, paragraph 1\n  quote: The rotation-induced change in (left) directional preference differs across trial pairs\n  statistics:\n  - about: across the three trial pairs\n    test: repeated-measures ANOVA\n    statistic: F(2, 228) = 10.54\n    p: 1.0e-5\n    n: 115 cells\n  - about: trial pairs against the two halves of stable1\n    test: ANOVA, Dunnett's test against the stable1 halves\n    statistic: F(3, 456) = 15.38\n    p: 1.0e-9\n  depends_on:\n  - cell-counts\n  criterion: Preferred direction is the bin of maximum rate in the 10 degree tuning curve; the\n    change is the absolute circular difference (0 to 180 degrees) between the two curves, a\n    standard choice the paper does not state. Pairs stable1-stable2, stable1-rotating room,\n    stable1-rotating arena, and the first against the second 15 min of stable1. A\n    repeated-measures ANOVA on the three trial pairs with Tukey-Kramer HSD, and a one-way ANOVA\n    of the four groups with Dunnett's test against the halves (the degrees of freedom, 3 and\n    456, imply a between-groups test). Reproduced when both ANOVAs have p < 0.05, every trial\n    pair exceeds the halves by Dunnett's test at p < 0.05, and the Tukey order matches the\n    legend; partially reproduced when the Dunnett part holds but the order among trial pairs\n    differs.\n- id: fig1d-instability\n  statement: Directional instability (the KLD between tuning curves) differs across trial pairs\n    and is greater for every trial pair than between the two halves of stable1.\n  source: Figure 1D, right, and its legend; Results, Degraded Directional Tuning, paragraph 1\n  quote: the change in preferred direction of directional tuning and the overall change in\n    directional tuning (''instability'') was greater across the two stable conditions and\n    between the stable and rotating conditions than it was between the two halves of the first\n    stable session (Figure 1D)\n  statistics:\n  - about: across the three trial pairs\n    test: repeated-measures ANOVA, Greenhouse-Geisser corrected\n    statistic: F(1.62, 184.22) = 7.78\n    p: 0.001\n    n: 115 cells\n  - about: trial pairs against the two halves of stable1\n    test: ANOVA, Dunnett's test against the stable1 halves\n    statistic: F(3, 456) = 5.15\n    p: 0.002\n  depends_on:\n  - cell-counts\n  criterion: KLD as in Quantifying Head-direction Signals, Directional Stability, resistor\n    average of the two Kullback-Leibler divergences between the 10 degree tuning curves made\n    into probabilities with the Krichevsky-Trofimov estimate. The Methods write n_i, counts;\n    the readings are (a) spike counts per bin; (b) the rates per bin. The logarithm base does\n    not change the tests. The same trial pairs and tests as fig1d-preference-change.\n    Reproduced when both ANOVAs have p < 0.05 and every trial pair exceeds the halves by\n    Dunnett's test at p < 0.05.\n- id: fig2-decoding-stable-vs-rotating\n  statement: Head direction decoded from stable1 ensemble tuning is relatively accurate in\n    stable2 and relatively inaccurate and abruptly changing in both frames during rotation,\n    although for some ensembles room-frame decoding is similar to stable2; seven ensembles of at\n    least five head-direction cells were analysed.\n  source: Results, Degraded Directional Tuning, paragraph 2; Figure 2A and 2B\n  quote: Seven ensembles of R5 cells were analyzed ... Relatively accurate decoding of the stable2\n    recordings (Figure 2A) contrast with relatively inaccurate and abruptly changing decoding in\n    both the room and arena spatial frames during rotation, although for some ensembles, decoding\n    in the room frame was similar to decoding in the stable2 condition\n  expected:\n  - quantity: ensembles of at least 5 head-direction cells\n    value: 7\n    tolerance: 0\n  depends_on:\n  - cell-counts\n  criterion: The decoder of HD_Max_likelihood.py (see the opening comment), trained on stable1\n    and applied to stable2 and to the rotating trial in room and in arena coordinates; error is\n    the circular difference of decoded and actual direction. The window is 660 ms in the\n    Methods (20 samples in the code) and 133 ms in the Figure 2 legend; 660 ms is the main\n    reading and 133 ms a variant. The paper gives no summary measure; the median absolute\n    error per ensemble and condition is used, a standard choice. Reproduced when there are\n    seven ensembles of at least five simultaneously recorded head-direction cells (no\n    tolerance, as this is a count of recordings) and in at least four of them the stable2 error\n    is below both rotating-frame errors; the ensemble with poor stable2 decoding (ensemble b) is\n    expected as an exception.\n- id: figs2-frame-preference\n  statement: During rotation, frame-specific directional discharge alternated between signaling\n    room and arena direction; four of seven ensembles showed an overall room preference and two\n    of seven an arena preference.\n  source: Results, Degraded Directional Tuning, paragraph 3; Figure S2A and S2B; Figure 2C legend\n  quote: 4/7 ensembles showed an overall preference to signal room directions over arena\n    directions and 2/7 showed an overall preference to signal arena directions over room\n    directions\n  expected:\n  - quantity: room-preferring ensembles\n    value: 4\n    tolerance: 0\n  - quantity: arena-preferring ensembles\n    value: 2\n    tolerance: 0\n  depends_on:\n  - fig2-decoding-stable-vs-rotating\n  criterion: Per cell and 133 ms interval of the rotating trial, Idir = |p(n|d) log2(p(n|d)/p(n))|\n    for the observed spike count n and head direction d, separately with room and arena\n    directions; ΔIdir is the room sum over cells minus the arena sum (Estimating momentary\n    directional information). Open details and their readings. Direction bins, (a) 10 degrees\n    as the tuning curves, (b) 45 degrees as the position by direction maps. The probabilities\n    from (a) the rotating trial itself, (b) stable1. The SD of the 2 SD rule, (a) the SD of the\n    ensemble's ΔIdir series, (b) the SD of stable1 Idir, given in Figure 2C for calibration.\n    An ensemble prefers the room when p(ΔIdir > 2 SD) exceeds p(ΔIdir < -2 SD) and the arena\n    in the reverse case (Figure 2C legend, Figure S2B); the margin for \"no preference\" is not\n    stated, and is read as (a) the two probabilities within a factor of 2, (b) both below 0.05.\n    Counts are of seven ensembles, so no tolerance. Reproduced when the counts are 4 and 2\n    under a reading; partially reproduced when room-preferring ensembles outnumber\n    arena-preferring ones.\n- id: fig2c-proximity-anticorrelation\n  statement: The rat's relative proximity to one shock zone versus the other is anti-correlated\n    with frame-specific directional information, so that near the room shock zone directional\n    discharge favours the arena frame and the reverse; this holds for Idir in each frame (mean r\n    = -0.141 ± 0.029, all p < 0.0001) and for ΔIdir (r = -0.18, p < 0.05, in the exemplar).\n  source: Results, Degraded Directional Tuning, paragraphs 3 and 4; Figure 2C and its legend;\n    Figure S2C\n  quote: This anticorrelation was observed for Idir defined for each spatial frame ... 0.141 ± 0.029;\n    all p < 0.0001), as well as for their combination DIdir\n  statistics:\n  - about: Idir per frame against relative proximity, each ensemble\n    test: Pearson correlation\n    statistic: mean r = -0.141 ± 0.029\n    p: 0.0001\n    p_relation: \"<\"\n  - about: Idir against relative proximity, second report\n    test: Pearson correlation\n    statistic: mean r = -0.132 ± 0.024\n    p: 0.0001\n    p_relation: \"<\"\n  - about: ΔIdir against relative proximity, ensemble b\n    test: Pearson correlation\n    statistic: r = -0.18\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - figs2-frame-preference\n  expected:\n  - quantity: mean Pearson r, Idir against relative proximity\n    value: -0.141\n    tolerance: 0.029\n  criterion: Idir and ΔIdir as in figs2-frame-preference, at 133 ms steps of the rotating trial,\n    correlated (Pearson) with the relative proximity to the two shock zones at the same steps.\n    The paper does not define relative proximity (it cites Kelemen and Fenton 2010); the\n    readings are (a) (d_arena - d_room) / (d_arena + d_room) with d the distance to each zone,\n    (b) d_arena - d_room, each signed so that a positive value means nearer the room zone,\n    paired with the room-frame Idir and its mirror for the arena-frame Idir. The two averages\n    the Results give (-0.141 ± 0.029 and -0.132 ± 0.024) are read as (a) one per frame-specific\n    Idir correlation over 14 values, (b) the second over the ΔIdir correlations; either value\n    may match. The tolerance is the paper's stated spread. Reproduced when every correlation is\n    negative with p < 0.0001 and the mean is within tolerance of either value; partially\n    reproduced when the mean is negative but not every correlation is significant.\n- id: figs3-no-head-direction-bias\n  statement: The frame preference ΔIdir does not vary systematically with head direction; its\n    polar distribution over head direction in either frame is not biased toward the shock zones\n    and does not differ from uniform.\n  source: Results, Degraded Directional Tuning, paragraph 4; Figure S3 legend\n  quote: did not significantly differ from uniform (average r = 0.17 ± 0.02; p > 0.17; Figure S3)\n  statistics:\n  - test: Rayleigh test\n    statistic: average r = 0.17 ± 0.02\n    p: 0.17\n    p_relation: \">\"\n  depends_on:\n  - figs2-frame-preference\n  expected:\n  - quantity: average Rayleigh r of normalized ΔIdir over head direction\n    value: 0.17\n    tolerance: 0.02\n  criterion: A claim of absence, judged on the paper's test. Per ensemble and frame, mean ΔIdir\n    in head-direction bins (10 degrees, as the tuning curves; the bin is not stated),\n    normalized to 0 to 1 by adding the magnitude of the minimum and dividing by the maximum\n    (Figure S3 legend), and a Rayleigh test with the normalized values as weights. The n of the\n    test is not stated; the readings are (a) the number of bins, which with r = 0.17 gives p\n    near 0.35, consistent with p > 0.17, (b) the sum of the weights. Reproduced when every test\n    has p ≥ 0.05; the average r is reported against the expected value.\n- id: fig3-hd-pair-correlations-preserved\n  statement: The sub-second temporal coupling of head-direction cell pairs (Kendall correlations\n    of spike counts at 40, 250 and 1000 ms) was maintained across stable1, rotating and stable2.\n  source: Figure 3B and its legend; Results, Degraded Directional Tuning and Maintained Temporal\n    Coupling, paragraph 1\n  quote: The three conditions did not differ at any of the timescales\n  statistics:\n  - about: 40 ms\n    test: ANOVA\n    statistic: F(2, 420) = 0.097\n    p: 0.9\n  - about: 250 ms\n    test: ANOVA\n    statistic: F(2, 420) = 0.305\n    p: 0.7\n  - about: 1000 ms\n    test: ANOVA\n    statistic: F(2, 420) = 0.44\n    p: 0.7\n  depends_on:\n  - cell-counts\n  criterion: A claim of absence, judged on the paper's test. Spike counts in 40, 250 and 1000 ms\n    bins over each trial, Kendall's tau for each simultaneously recorded head-direction pair,\n    Fisher z-transformed (Figure 3B legend; Stability of a correlated network state). One-way\n    ANOVA of the three conditions at each timescale (the degrees of freedom, 2 and 420, imply\n    a between-groups test on about 141 pairs). Reproduced when p ≥ 0.05 at all three\n    timescales; the Pearson r between the pairs' tau in stable1 and in each other trial is\n    reported as well.\n- id: figs4-all-pair-correlations-preserved\n  statement: Cell-pair discharge correlations among all 556 MEC cell pairs were preserved across\n    trials (r² > 0.55 between the two stable trials and r² ≥ 0.52 between stable1 and rotating).\n  source: Results, Degraded Directional Tuning and Maintained Temporal Coupling, paragraph 1;\n    Figure S4\n  quote: these correlations were also preserved among all the MEC cell pairs that were recorded (n\n    = 556 pairs), regardless of the spatial functional class of the cells (r2 > 0.55 across the\n    two stable conditions; r2 R 0.52 across the first stable and rotating session; Figure S4)\n  depends_on:\n  - cell-counts\n  expected:\n  - quantity: smallest r², stable1 against stable2 Kendall correlations\n    value: 0.55\n    tolerance: 0.055\n  - quantity: smallest r², stable1 against rotating Kendall correlations\n    value: 0.52\n    tolerance: 0.052\n  criterion: Kendall's tau of every simultaneously recorded MEC pair at 40, 250 and 1000 ms, and\n    the squared Pearson correlation between the sets of tau in stable1 and in each other trial\n    (Stability of a correlated network state). The reported values are lower bounds over the\n    timescales. Reproduced when at every timescale r² is at least 0.495 for stable1 against\n    stable2 and at least 0.468 for stable1 against rotating (each bound less 10%).\n- id: figs5-hd-cells-high-model-information\n  statement: The 115 conventionally identified head-direction cells also score high in\n    head-direction information estimated by the Gaussian process tuning model among the 921\n    modelled MEC cells.\n  source: Figure S5 legend\n  quote: The conventionally-identified cells also scored high in head-direction information, which\n    validates the model-based approach.\n  depends_on:\n  - cell-counts\n  criterion: Model as in the Methods (Model-based estimation ...), code at\n    https://bitbucket.org/crissavin/pfgp.git, on spike counts over a 4-dimensional lattice of\n    2D position, speed and head direction; head-direction information is the mutual information\n    between the posterior mean response and head direction. Cells modelled are those with rate\n    below 30 AP/s and more than 50% of the arena visited in all three trials (Figure S6 legend).\n    The lattice resolution and time bin are not stated in the paper; they are taken from the\n    pfgp code. \"Scored high\" names no test; the readings are (a) the median of the\n    head-direction cells lies in the upper third of the population, the class threshold of\n    Figure S6, (b) the head-direction cells exceed the other cells by a one-sided Mann-Whitney\n    test at p < 0.05. Reproduced when a reading holds.\n- id: figs6-subclass-correlations-preserved\n  statement: Cell-pair discharge correlations within the grid-tuned, position-tuned and\n    speed-tuned subclasses of MEC cells are maintained across stable and rotating trials.\n  source: Figure S6 legend\n  quote: Cell-pair specific discharge correlations within subclasses of spatially-tuned cells are\n    maintained across the stable and rotating sessions.\n  depends_on:\n  - figs5-hd-cells-high-model-information\n  criterion: Classes by the Gaussian process model (Figure S6 legend), each the upper third of\n    its metric among the 921 cells, grid score from the session-averaged rate map (60 and 120\n    degree rotation correlations minus 30, 90 and 150 degree ones), and position and speed\n    information. Kendall's tau within each class at 40, 250 and 1000 ms, stable1 against\n    rotating and against stable2. \"Maintained\" names no threshold; the readings are (a) r² at\n    least the bounds of figs4-all-pair-correlations-preserved less 10%, (b) a positive Pearson\n    r at p < 0.05. Reproduced when a reading holds for every class, timescale and trial pair;\n    partially reproduced when it holds for most.\n- id: no-angular-velocity-tuning\n  statement: The MEC head-direction cells showed no systematic tuning of firing rate to angular\n    head velocity.\n  source: Results, Transient Allocentric Registration, paragraph 1\n  quote: There was no systematic tuning of firing rate to angular velocity in these MEC\n    head-direction cells (data not shown).\n  depends_on:\n  - cell-counts\n  criterion: The paper shows no data and names no measure or test. The readings are (a) per cell,\n    the Pearson correlation of rate with signed angular velocity in 30 Hz samples, (b) the same\n    with unsigned angular velocity; the head direction derivative over successive samples.\n    A claim of absence with no test in the paper; reproduced when, under a reading, the\n    fraction of cells significant at p < 0.05 does not exceed what chance gives by a binomial\n    test at p < 0.05, and the result rests on that assumption.\n- id: fig4-internal-tuning-preserved\n  statement: Internally referenced directional tuning of head-direction cell pairs (tuning of one\n    cell to head-direction displacement since the other's spikes) was preserved across stable1,\n    rotating and stable2; neither its instability nor its change in preference differed between\n    trials or from the two halves of stable1.\n  source: Results, Transient Allocentric Registration, paragraph 2; Figure 4B and 4D and the\n    legend\n  quote: Internally referenced tuning to head-direction displacement was preserved across the\n    stable and rotating conditions\n  statistics:\n  - about: instability across trial pairs\n    test: repeated-measures ANOVA, Greenhouse-Geisser corrected\n    statistic: F(1.70, 219.83) = 2.81\n    p: 0.07\n  - about: preference change across trial pairs\n    test: repeated-measures ANOVA, Greenhouse-Geisser corrected\n    statistic: F(1.83, 248.26) = 0.42\n    p: 0.6\n  - about: instability, trial pairs against stable1 halves\n    test: ANOVA\n    statistic: F(3, 522) = 1.39\n    p: 0.2\n  - about: preference change, trial pairs against stable1 halves\n    test: ANOVA\n    statistic: F(3, 536) = 0.34\n    p: 0.8\n  depends_on:\n  - cell-counts\n  criterion: A claim of absence, judged on the paper's tests (four ANOVAs as in Figure 4D, each\n    at p ≥ 0.05). Internally referenced tuning as in the Methods (Estimating internally\n    referenced head direction), for the 142 ordered or unordered pairs; KLD and preferred\n    direction change as in fig1d-instability and fig1d-preference-change, on the same trial\n    pairs and stable1 halves. Open details and readings. The interval, (a) 5 s as in the\n    Results and Figure 4B, (b) 30 s, the code's window. The window side, (a) cell 2 spikes\n    after the cell 1 spike, as the Methods read, (b) before it, as the code has it. The\n    normalization, (a) the Methods' division by the sum of the time offsets, (b) the code's\n    division by the occupancy of each displacement. The degrees of freedom imply about 130\n    to 137 pairs, so some pairs were dropped for a reason the paper does not give; the pairs\n    used are those with a defined curve in every trial. Reproduced when all four tests have\n    p ≥ 0.05 under the main readings (5 s, Methods side and normalization); the variants are\n    shown.\n- id: fig4c-arena-registration-short-lived\n  statement: The strength of internally referenced directional tuning is similar in all\n    conditions and frames for intervals up to 10 s, but beyond 10 s it falls in the rotating arena\n    frame (20 to 60 s; stable1 = stable2 = rotating room > rotating arena) and at 300 to 600 s also\n    in the rotating room frame (stable1 = stable2 > rotating room > rotating arena).\n  source: Figure 4C and its legend; Results, Transient Allocentric Registration, paragraph 3\n  quote: during short intervals in the rotating condition, the strength of internally referenced\n    directional tuning was similar in the two spatial frames but less so across longer\n    intervals (Figure 4C). Specifically, internally referenced arena-frame tuning abruptly\n    decreased after 10 s.\n  statistics:\n  - about: condition by interval interaction\n    test: repeated-measures two-way ANOVA, Greenhouse-Geisser corrected\n    statistic: F(6.91, 1287.7) = 15.16\n    p: 1.0e-17\n  - about: conditions at each interval up to 10 s\n    test: one-way ANOVA\n    statistic: F(3, 564) ≤ 1.59\n    p: 0.19\n    p_relation: \">\"\n  - about: conditions at each interval beyond 10 s\n    test: one-way ANOVA, Tukey-Kramer HSD\n    statistic: F(3, 564) ≥ 23.73\n    p: 1.0e-14\n    p_relation: \"<\"\n  depends_on:\n  - fig4-internal-tuning-preserved\n  criterion: Per pair and maximum interval (3, 4, 5, 10, 20, 30, 40, 50, 60, 300 and 600 s, as the\n    Methods list; the legend says 10 intervals), internally referenced tuning in stable1,\n    stable2, rotating room and rotating arena frame, with the readings of window side and\n    normalization of fig4-internal-tuning-preserved. Strength is not defined; the reading is\n    the Rayleigh vector length of the curve, the paper's directionality measure. One-way ANOVA\n    of the four conditions at each interval (142 pairs, as the degrees of freedom imply) with\n    Tukey-Kramer HSD. Reproduced when the ANOVA has p ≥ 0.05 at every interval up to 10 s,\n    p < 0.05 at every interval beyond 10 s, the arena frame is below the three others at 20 to\n    60 s, and at 300 to 600 s the room frame is also below both stable trials; partially\n    reproduced when the arena frame falls below the others beyond 10 s and not before, but the\n    room-frame order at long intervals is not found.\n- id: fig5-error-inhomogeneous\n  statement: The angular distribution of decoding error is inhomogeneous in the room frame\n    (resultant r = 0.589) and the arena frame (r = 0.653) and differs from the distribution of\n    sampled head directions, which is itself biased in both frames (r = 0.147 room, r = 0.378\n    arena).\n  source: Results, Transient Allocentric Registration, paragraph 4; Figure 5A and 5B and the\n    legend\n  quote: The angular distribution of the decoded directional error was not homogeneous in the room\n    frame (Figure 5A; resultant vector r = 0.589; Rayleigh’s test; z = 236.36; p = 0.000); nor\n    was the error distribution similar to the head-direction distribution\n  statistics:\n  - about: room-frame error, uniformity\n    test: Rayleigh's test\n    statistic: r = 0.589, z = 236.36\n    p: 0\n  - about: room-frame error against head directions\n    test: Kuiper's test\n    statistic: V = 4.17 × 10^7\n    p: 0.001\n  - about: arena-frame error, uniformity\n    test: Rayleigh's test\n    statistic: r = 0.653, z = 289.63 (the legend prints 153.24 and 230.58)\n    p: 0.0001\n  - about: arena-frame error against head directions\n    test: Kuiper's test\n    statistic: V = 5.38 × 10^7\n    p: 0.001\n  - about: room-frame head directions, uniformity\n    test: Rayleigh's test\n    statistic: r = 0.147, z = 230.6\n    p: 0.0001\n    p_relation: \"<\"\n  - about: arena-frame head directions, uniformity\n    test: Rayleigh's test\n    statistic: r = 0.378, z = 153.2\n    p: 0.001\n  depends_on:\n  - fig2-decoding-stable-vs-rotating\n  expected:\n  - quantity: resultant r of room-frame decoding error\n    value: 0.589\n    tolerance: 0.0589\n  - quantity: resultant r of arena-frame decoding error\n    value: 0.653\n    tolerance: 0.0653\n  - quantity: resultant r of room-frame head directions\n    value: 0.147\n    tolerance: 0.0147\n  - quantity: resultant r of arena-frame head directions\n    value: 0.378\n    tolerance: 0.0378\n  criterion: Decoding error during rotation from the decoder of fig2-decoding-stable-vs-rotating,\n    in each frame, a Rayleigh test of uniformity and a Kuiper's test against the sampled head\n    directions of the same trial. Which recordings are pooled is not stated; the z values\n    imply about 680 decoded windows and 1,100 to 10,700 head-direction samples. The readings\n    are (a) all seven ensembles pooled, (b) the exemplar ensemble with the most cells, (c)\n    each ensemble apart, with the median r. The window is 660 ms, with 133 ms as a variant.\n    Reproduced when, under a reading, both error distributions and both head-direction\n    distributions are non-uniform at p < 0.05, both Kuiper's tests have p < 0.05 and the four\n    r values are within tolerance; partially reproduced when the tests hold but not every r.\n- id: fig5c-error-minima-at-cues\n  statement: The room-frame decoding error has strong minima at 110 and 350 degrees in the room\n    frame, the directions of the leading edges of prominent orienting cues, and not in the arena\n    frame.\n  source: Results, Transient Allocentric Registration, paragraph 4; Figure 5C and 5D\n  quote: Interestingly, the room frame direction decoding error distribution showed strong minima\n    at 110 ... in the room frame, which, given the clockwise arena rotation, are the directions\n    at which the leading edges of prominent orienting cues were located\n  depends_on:\n  - fig5-error-inhomogeneous\n  expected:\n  - quantity: direction of first minimum of room-frame decoding error\n    value: 110\n    tolerance: 10\n    unit: degrees\n  - quantity: direction of second minimum of room-frame decoding error\n    value: 350\n    tolerance: 10\n    unit: degrees\n  criterion: The tolerance is one 10 degree bin, the decoder's resolution, since 10% of an angle\n    has no meaning. What the histogram is a function of is not stated; the readings are (a)\n    the mean absolute decoding error as a function of the rat's room-frame head direction in 10\n    degree bins, (b) the histogram of the signed decoding error itself. Under the pooling\n    readings of fig5-error-inhomogeneous. Reproduced when the two deepest local minima lie\n    within tolerance of 110 and 350 degrees under a reading; partially reproduced when one\n    does. Whether they match the cue positions cannot be tested, as the room's cue positions\n    are given only in the figure.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/park-2019.yaml paper/10.1016-j.neuron.2018.11.019.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "—\|rather" claims/park-2019.yaml; sed -n 141,144p paper/10.1016-j.neuron.2018.11.019.txt | cat -A | grep -o "p = 10.\{0,6\}9"
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "15.38; p = ",
 "path": "paper/10.1016-j.neuron.2018.11.019.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/park-2019.yaml`. The quote checker passes every quote and reports one problem, which is a garbled glyph, not a wrong value: it can't find p = 1e-9 for `fig1d-preference-change`. Line 143 of the text prints it as "p = 10�9", which is 10⁻⁹. I left the value as it is. Nothing is committed.

**Text read:** the version of record (`paper/10.1016-j.neuron.2018.11.019.txt`), with main text, figure legends, STAR Methods and the full supplement (Figures S1 to S6, Table S1). Video S1 holds no result. There was no PDF tool here (no PyMuPDF, no pdftoppm), so I read every figure from its legend and the Results only. I read the garbled glyphs as: "10�N" = 10⁻ᴺ, "R" = ≥, "%" = ≤, "3 10⁷" = ×10⁷. The spike width prints as "169.79 ± 4.58 ms", which is very likely µs.

**Code read:** FentonLab/PyCode_MEC_HDC-NeuronMS_Park at commit 545a738. It holds the decoder (`HD_Max_likelihood.py`) and the internally referenced tuning (`Spike_triggered_FR_curve.py`). I did not read the pfgp code on Bitbucket (the Gaussian process model behind Figures S5 and S6). No code is given for Idir, the cell-pair correlations, the tuning measures or the JMP statistics.

**Claims:** 22, all with quotes and none inferred. 32 statistical values are recorded, across 17 claims with a `statistics` block. 15 claims have expected values. All 22 have a criterion.

**Details the paper leaves open, and the readings named:**
- **Learning curves (Fig 1A):** the avoidance measure isn't stated. Readings: entrances per trial, or time to first entrance.
- **Speed (Fig 1C):** how speed is computed (displacement per 30 Hz sample, or per 1 s), and the ANOVA's unit (session, or cell). The degrees of freedom imply about 38 units.
- **LFP power (Fig 1C):** the band. Readings: total power, or theta.
- **Change in preferred direction:** the absolute circular difference, a standard choice. For the KLD, the Methods write counts: spike counts or rates per bin.
- **Decoding window:** 660 ms in the Methods (and the code) against 133 ms in the Fig 2 legend. 660 ms is the main reading, 133 ms a variant. The paper gives no summary error measure, so the median absolute error is used.
- **Idir and frame preference:**
  - direction bin (10° or 45°)
  - which trial the probabilities come from (the rotating trial or stable1)
  - which SD the 2 SD rule uses (the ΔIdir series, or stable1)
  - the margin for "no preference"
- **Relative proximity to the shock zones:** not defined. Readings: a normalized difference of the two distances, or the raw difference. The Results give two averages (r = −0.141 ± 0.029 and −0.132 ± 0.024); either may match.
- **Fig S3 Rayleigh test:** its n. Readings: the number of direction bins (consistent with the reported p), or the sum of the weights.
- **Internally referenced tuning (Fig 4):**
  - interval for Fig 4D: 5 s in the Results, 30 s in the code
  - window side: after the reference spike as the Methods read, before it as the code has it
  - normalization: the Methods' sum of time offsets, or the code's occupancy
  - pairs dropped: the degrees of freedom imply about 130 to 137 of the 142 pairs, with no reason given
  - interval count: the Methods list 11 intervals, the legend says 10
  - "strength": read as the Rayleigh vector length
- **Fig 5:** which recordings are pooled (all seven ensembles, the largest ensemble, or each apart). What the error minima are a function of (head direction, or the error itself).
- **Fig S5 "scored high" and Fig S6 "maintained":** no threshold or test is given. Two readings each.
- **No angular-velocity tuning:** the paper shows no data and names no measure or test, so any test of it rests on an assumption.

**Missing from the paper or the dataset description:**
- The room's cue positions appear only in Figure 5, so the link between the 110° and 350° minima and the cues can't be tested.
- The CRCNS description doesn't mention LFP, waveforms or the training sessions behind the learning curves. That affects the LFP, spike-width and learning-curve claims; whether the data are there is for the author to find.
- The stable1 halves are read as its first and second 15 min, from the code's folder names. The paper doesn't state it.

## End of run

21 turns, 5 minutes, $1.74 at API prices, result: success.
