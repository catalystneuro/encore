# openneuro-ds002778 · claims · run 40592182477

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/Reader/,$p' | head -300; ls claims/001453/ claims/openneuro-ds002778/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^##" docs/protocol.md; awk '/^## Reader/,/^## Author/' docs/protocol.md | sed -n '60,200p'
```

```
40:## Reader
42:### 1. Get the paper
53:### 2. Read the paper's code
63:### 3. Write the claims file
148:### 4. Data from outside the paper's own recordings
156:### 5. Check
169:### 6. Answer questions
182:## Author
198:### 1. Establish what can be tested
325:### 2. Check the data against its description
340:### 3. Write the entry
398:### 4. Lock, check and run
409:### 5. Record the attempt
460:### 6. Hand over for verification
498:## Repeat attempts
540:## Local and remote datasets
563:## Verifier
567:### Round 1: without the author's conclusions
592:### Round 2: with the author's conclusions
604:### Round 3: proposed changes
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 63,100p docs/protocol.md; cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -30 paper/10.1523-eneuro.0151-19.2019.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 30,136p paper/10.1523-eneuro.0151-19.2019.txt; head -8 paper/10.1016-j.nicl.2013.07.013.txt; ls paper; grep -n "dataset\|description\|title" docs/archives.md | head; ls claims | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7f70e72f-f51b-423e-bac0-7c1d3e3c992b/tool-results/b0rxf8ze2.txt"
}
```

```
1	Data were preprocessed in MATLAB using custom scripts and EEGLAB functions (Delorme and Makeig, 2004). In brief, first, each electrode’s mean was removed and then a common average reference was applied. Excessively noisy electrodes were excluded. The data were then high pass filtered at 0.5 Hz to remove low frequency drift (using a two-way FIR filter, eegfilt; Delorme and Makeig, 2004). Then, data were manually examined for artifacts (eye blinks and movements, muscle activity, electrical noise, and other sources of noise), and indices containing these events were flagged for rejection. to avoid filtering over non-continuous data, rejection regions were excluded after filtering (as described below). A previously published report examining the same data (Swann et al., 2015) used a current source density (CSD) referencing montage to examine PAC (Kayser and Tenke, 2006a,b; Kayser, 2009). We opted not to use this approach here since this montage might produce more unpredictable phase inversions and complicate interpretation of waveform shape. Thus, to be consistent, we used an average reference approach for all measures. However, for direct comparison with the previous publication (Swann et al., 2015) we implemented a CSD referencing approach as a confirmatory analysis (CSDtoolbox in MATLAB, spline flexibility = 3; Kayser and Tenke, 2006a,b; Kayser, 2009).
2	We focused predominantly on electrodes closest to sensorimotor cortex (C3 and C4). To compare data from these electrodes to recordings more likely to be impacted by residual electromyogram (EMG) artifact we also examined the electrodes closest to the temporalis muscles (F7 and F8; Swann et al., 2015). Unless otherwise specified, statistical testing focused on a “composite” sensorimotor signal where measures from C3 and C4 were calculated separately and then results were averaged for each participant, such that each participant contributed one data point, before performing statistical testing across participants. Th
[... 176 more lines not kept]
```

**Agent**

Full text, Methods and tables are present; the supplement is the code ZIP (Extended Data 1), also on GitHub. Next I'll read the linked code and an OpenNeuro claims file for format.

**Agent calls Bash**

```bash
ls -d claims/openneuro-* | head; sed -n 1,60p tools/claims_check.py | head -80; cd $TMPDIR && git clone -q https://github.com/SwannLab/Jackson_2019 && cd Jackson_2019 && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | head -50
```

```
ls: cannot access 'claims/openneuro-*': No such file or directory
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
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Jackson_2019 && cat README.md utils.py shape.py pac.py
```

```
<persisted-output>
Output too large (45.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7f70e72f-f51b-423e-bac0-7c1d3e3c992b/tool-results/bw0houw63.txt

Preview (first 2KB):
<b>Jackson_2019</b>
<br>Analysis code used to create figures in Jackson et al, 2019
<br>Code used was adapted from: https://github.com/voytekresearch/Cole_2017
<br>Data can be found at: https://openneuro.org/datasets/ds002778/versions/1.0.0
<br>
<b>Notebooks</b>
<br>This repo contains notebooks used to generate figures.
<br>
<b>Libraries</b>
<br>utils.py - contains functions for loading data, running group analysis
<br>shape.py - contains functions for calculating waveform shape metrics 
<br>pac.py - contains functions for calculating phase amplitude coupling (PAC)
"""
util.py
Some functions for analyzing data in this repo
"""
[... 62 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7f70e72f-f51b-423e-bac0-7c1d3e3c992b/tool-results/bw0houw63.txt",
 "offset": 60
}
```

```
60	    eeg['C'] = np.zeros(Sc, dtype=dtype)
61	    return eeg
62	
63	def loadPD(filepath='AVG_motor.mat',filepathrej='rejectscombined.mat'):
64	    '''
65	    Load the data after following preprocessing:
66	    1. Average referenced
67	    
68	    Load rejection indices:
69	    1. Each index in an array
70	
71	    Parameters
72	    ----------
73	    filepath : string
74	        path to averaged referenced data
75	    filepathrej : string
76	        path to rejection indices
77	        
78	    Returns
79	    -------
[... 1408 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Jackson_2019 && python3 - <<'EOF'
import json
for nb in ['Figure_1.ipynb','Figures_2,3.ipynb','Figure_4.ipynb']:
    d=json.load(open(nb))
    print('=====',nb)
    for i,c in enumerate(d['cells']):
        src=''.join(c['source'])
        print(f'--- [{i}] {c["cell_type"]}')
        print(src)
        if c['cell_type']=='code':
            for o in c.get('outputs',[]):
                t=o.get('text') or o.get('data',{}).get('text/plain')
                if t: print('>>>', ''.join(t)[:1500])
EOF
```

```
===== Figure_1.ipynb
--- [0] markdown
<font size="5"><b>Figure 1
--- [1] markdown
Schematic summarizing waveform shape calculations
--- [2] markdown
<b>Imports
--- [3] code
%config InlineBackend.figure_format = 'retina'
%matplotlib inline
#python packages
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pac

import seaborn as sns
sns.set_style('white')

import imp
[... 593 more lines not kept]
```

**Agent**

The code (SwannLab/Jackson_2019 at a7c89f5) settles most method details, and its printed outputs match Tables 1 and 2. Next I'll get the dataset's title and description from OpenNeuro.

**Agent calls Bash**

```bash
curl -s -m 30 https://openneuro.org/crn/graphql -H 'content-type: application/json' -d '{"query":"{ dataset(id:\"ds002778\") { latestSnapshot { tag description { Name } readme } } }"}' | head -c 4000
```

Result: the fetched text is not kept.

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
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000])"
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

I have what the claims need. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml",
 "content": "# Claims for Jackson, Cole, Voytek & Swann (2019), eNeuro 6(3) ENEURO.0151-19.2019, on OpenNeuro ds002778.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-10-27,\n# protocol as stated in docs/protocol.md.\n#\n# Text read: the version of record, full text from Europe PMC PMC6553574 (main text, Methods, figure\n# legends, Tables 1 to 3). The only supplement is Extended Data 1, the analysis code, which is the\n# GitHub repository read below. Figures were not opened; no claim needs a value read off a figure.\n#\n# Code read: https://github.com/SwannLab/Jackson_2019 at commit a7c89f50106aa4ccec76ace18bbfa45a5440545e\n# (2020-05-19). It holds utils.py (loading the preprocessed traces, shape and PAC per recording),\n# shape.py (zero crossings, peaks and troughs, sharpness, steepness), pac.py (normalized modulation\n# index, Ozkurt and Schnitzler 2011) and notebooks Figure_1, Figures_2,3 and Figure_4. The notebooks\n# print the Wilcoxon, rank sum, Spearman and Cohen's d values of Tables 1 and 2 (beta) and Figure 3.\n# The code starts from preprocessed MATLAB files (AVG_motor.mat, rejectscombined.mat) that are not in\n# the repository: the MATLAB preprocessing, the manual artifact marks, the mu/alpha analysis, the\n# bipolar and CSD analyses, the F7/F8 and T7/T8 tests, the power spectra, the topographies and the Q4\n# effect sizes (Table 3) are not in the code.\n#\n# Data the paper used (Methods, Participants and Data collection): resting scalp EEG from a dataset\n# first published by George et al. (2013) and reanalysed by Swann et al. (2015). 15 PD patients (8\n# female, mean age 63.2 +/- 8.2 years), each recorded on and off dopaminergic medication on different\n# days in counterbalanced order (off means medication stopped at least 12 h before), and 16 age-matched\n# controls (9 female, 63.5 +/- 9.6 years) recorded once. 32-channel BioSemi ActiveTwo, 512 Hz, at least\n# 3 min of rest fixating a cross, with extra electrodes beside and below the left eye. Measured\n# variables used here: EEG at C3 and C4 (sensorimotor), F7, F8, T7 and T8 (near the temporalis\n# muscles), CP1 and CP2 (bipolar montage), all electrodes for topographies and the CSD montage, and\n# UPDRS scores on and off medication. The archive's title, \"UC San Diego Resting State EEG Data from\n# Patients with Parkinson's Disease\", and its README, which asks users to cite this paper, say it holds\n# these recordings.\n#\n# Method, from the Methods unless a step says otherwise.\n# Preprocessing: remove each electrode's mean, common average reference, exclude excessively noisy\n# electrodes, high-pass at 0.5 Hz with a two-way FIR filter (EEGLAB eegfilt), then exclude the\n# manually marked artifact samples after filtering. Every measure is computed per electrode and per\n# recording on the whole resting recording; the composite value of a participant is the mean of its C3\n# and C4 values (Methods, Data preprocessing, paragraph 2; the code's pooldata averages the two halves\n# of the 30 patient and 32 control recordings). The same is done for F7 and F8.\n# Peaks and troughs (Methods, Sharpness ratio; code shape.findpt): band-pass 13 to 30 Hz with\n# scipy.signal.firwin, floor(3 * 512 / 13) = 118 taps (the paper's \"order = 231 ms\"), applied with\n# filtfilt to the whole trace; rising and falling zero crossings of the filtered signal; the maximum\n# (peak) and minimum (trough) of the unfiltered signal between them; extrema within 100 samples of\n# either end of the trace are dropped (code, boundaryS=100); extrema whose sample index is a rejected\n# sample are dropped (code, measure_shape).\n# Sharpness (code shape.ex_sharp): the absolute value of the mean of the voltage at the extremum minus\n# the voltage 3 samples before and 3 samples after. Sharpness ratio is log10 of the larger of mean peak\n# sharpness / mean trough sharpness and its inverse (code uses log10; the paper says \"log\").\n# Steepness (code shape.rd_steep): rise steepness is the largest first difference from a trough to the\n# next peak, decay steepness the largest negative first difference (as a positive number) from a peak\n# to the next trough. Steepness ratio is log10 of the larger of mean rise / mean decay and its inverse.\n# In the code rise steepness values are deleted at the positions of rejected peaks and decay values at\n# the positions of rejected troughs; the Methods do not say how rejection applies to steepness.\n# Peak-to-trough ratio is log10(mean peak sharpness / mean trough sharpness) and rise-to-fall ratio is\n# log10(mean rise steepness / mean decay steepness), signed (Methods; code Figure_4 takes log10).\n# PAC (Methods, PAC; code pac.ozkurt): beta 13 to 30 Hz and gamma 50 to 150 Hz, firwin band-pass with\n# filtfilt, Hilbert phase of beta and amplitude of gamma, rejected samples removed after the Hilbert\n# transform, then |sum(a exp(i phi))| / (sqrt(N) sqrt(sum(a^2))). The Methods give filter orders of\n# 231 ms (beta) and 240 ms (gamma), that is 118 and 123 samples at 512 Hz; the code uses 231 and 240\n# taps. The Methods are the main reading and the code's taps a variant.\n# Statistics (Methods, Statistical tests; code Figures_2,3): Wilcoxon signed rank for off against on\n# (scipy.stats.wilcoxon defaults; the printed p-values match its normal approximation, for example\n# W = 12, n = 15 gives p = 0.0064), Wilcoxon rank sum for off against controls (scipy.stats.ranksums,\n# z statistic, positive when off is larger), Spearman correlation, Benjamini-Hochberg FDR. In Tables 1\n# and 2 the FDR family is the six tests of a table (three measures by two bands). Cohen's d (code\n# effectsize) is (mean1 - mean2) / sqrt((sd1^2 + sd2^2) / 2) with sample standard deviations, computed\n# as for unpaired groups also for the paired off and on comparison.\n#\n# Details left open, with the readings each criterion uses.\n# - Artifact rejection. The marks were made by hand and are not published with the paper or its code.\n#   Readings: (a) the dataset's own artifact annotations or bad-segment marks, if it holds any; (b) no\n#   rejection beyond the 100-sample edge rule. A criterion whose outcome differs between them rests on\n#   the choice.\n# - Noisy electrodes. Which electrodes were excluded, and by what rule, is not given. Readings: (a) the\n#   dataset's own bad-channel marks, if any; (b) all 32 scalp electrodes kept. The eye electrodes are\n#   not scalp electrodes and are left out of the common average in both.\n# - The 0.5 Hz high-pass order is eegfilt's default (3 * fix(512 / 0.5) samples), a standard choice\n#   that the paper fixes only by naming the function.\n# - Wilcoxon p-value. Main reading the normal approximation without continuity correction (as the\n#   code's printed p-values show); the exact distribution is a variant.\n# - PAC filter length, 118 and 123 samples (Methods) against 231 and 240 taps (code), as above.\n# - Filters for the mu/alpha band (8 to 12 Hz), which the code does not cover. Shape filter by the\n#   code's rule, 3 cycles of the low cutoff (floor(3 * 512 / 8) = 192 taps). PAC phase filter readings:\n#   (a) 3 cycles of 8 Hz, 192 taps (pacpy's default rule); (b) 231 taps as in the code for beta; (c)\n#   118 samples as the Methods give for beta. Gamma 50 to 150 Hz as for beta.\n# - Which half of the code's 30 patient recordings is C3 is not stated; the Q4 counts per electrode\n#   (9 at C3, 8 at C4) are judged without regard to which electrode has which count where noted.\n# - Cohen's d for PAC. The Methods say PAC was log-scaled for effect sizes; the code's d on raw PAC is\n#   0.83, the value in Table 1, and Table 3 gives 0.75 for all patients. Readings: raw PAC and log10 PAC.\nschema_version: 2\ndataset:\n  archive: openneuro\n  id: ds002778\npaper: doi:10.1523/eneuro.0151-19.2019\nclaims:\n- id: fig2-sharpness-off-on\n  statement: Over sensorimotor electrodes (C3 and C4 composite), beta sharpness ratio is higher in PD\n    patients off medication than on medication.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 1; Figure 2A, B; Table 1\n  quote: Medication reduced beta waveform sharpness ratio (p = 0.012, FDR corrected; Fig. 2)\n  statistics:\n  - test: Wilcoxon signed rank\n    statistic: signed rank = 12\n    p: 0.006\n    corrected: none (FDR corrected p = 0.0121)\n    n: 15 patients, on and off\n  - test: Wilcoxon signed rank\n    statistic: signed rank = 12\n    p: 0.0121\n    corrected: FDR\n    n: 15 patients, on and off\n  expected:\n  - quantity: Wilcoxon signed rank statistic, beta sharpness ratio, off against on\n    value: 12\n    tolerance: 1.2\n  - quantity: Cohen's d, beta sharpness ratio, off against on\n    value: 0.86\n    tolerance: 0.086\n  criterion: Composite C3 and C4 beta sharpness ratio per patient, off against on, Wilcoxon signed rank\n    test, FDR corrected over the six tests of Table 1. Reproduced when the corrected p is below 0.05\n    with off higher than on, and the statistic and d are within tolerance under one of the readings of\n    artifact rejection and noisy electrodes named in the opening comment. Partially reproduced when the\n    test holds and a value is out of tolerance.\n- id: fig2-steepness-off-on\n  statement: Over sensorimotor electrodes, beta steepness ratio is higher in PD patients off medication\n    than on medication.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 1; Figure 2A, B; Table 1\n  quote: steepness ratio (p = 0.012, FDR corrected; Fig. 2) in PD patients over sensorimotor electrodes\n  statistics:\n  - test: Wilcoxon signed rank\n    statistic: signed rank = 9\n    p: 0.004\n    n: 15 patients, on and off\n  - test: Wilcoxon signed rank\n    statistic: signed rank = 9\n    p: 0.0121\n    corrected: FDR\n    n: 15 patients, on and off\n  expected:\n  - quantity: Wilcoxon signed rank statistic, beta steepness ratio, off against on\n    value: 9\n    tolerance: 0.9\n  - quantity: Cohen's d, beta steepness ratio, off against on\n    value: 0.68\n    tolerance: 0.068\n  criterion: As for fig2-sharpness-off-on, with the steepness ratio.\n- id: fig2-pac-off-on\n  statement: Over sensorimotor electrodes, beta-gamma PAC is higher in PD patients off medication than\n    on medication.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 1; Figure 2A, B; Table 1\n  quote: PAC also decreased with medication (p = 0.017, FDR corrected; Fig. 2), as has been previously\n    published\n  statistics:\n  - test: Wilcoxon signed rank\n    statistic: signed rank = 15\n    p: 0.011\n    n: 15 patients, on and off\n  - test: Wilcoxon signed rank\n    statistic: signed rank = 15\n    p: 0.0166\n    corrected: FDR\n    n: 15 patients, on and off\n  expected:\n  - quantity: Wilcoxon signed rank statistic, beta PAC, off against on\n    value: 15\n    tolerance: 1.5\n  - quantity: Cohen's d, beta PAC, off against on (Table 1)\n    value: 0.83\n    tolerance: 0.083\n  criterion: As for fig2-sharpness-off-on, with PAC (normalized modulation index). The text gives\n    p = 0.017 corrected and Table 1 gives 0.0166; both are below 0.05. Readings for the filters are\n    the Methods' 118 and 123 samples and the code's 231 and 240 taps; for d, raw PAC (code, Table 1)\n    and log10 PAC (Methods). The claim holds when the test holds under one reading and d is within\n    tolerance under one reading.\n- id: bipolar-off-on\n  statement: With a bipolar montage (C3-CP1 and C4-CP2), sharpness ratio, steepness ratio and PAC each\n    differ between PD patients off and on medication.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 1\n  quote: we also calculated these measures using a bipolar scheme (C3-CP1 and C4-CP2) and found very\n    similar results (p < 0.004, FDR corrected for each of the three measures examined)\n  statistics:\n  - test: Wilcoxon signed rank\n    p: 0.004\n    p_relation: \"<\"\n    corrected: FDR, over the three measures\n    n: 15 patients, on and off\n  criterion: Bipolar signals C3 minus CP1 and C4 minus CP2 (the paper does not say whether they are\n    formed before or after the common average reference; a difference of two channels is unchanged by\n    it), composite of the two pairs, beta band, each measure as in fig2-sharpness-off-on and\n    fig2-pac-off-on. Reproduced when all three signed rank tests, FDR corrected over the three, give\n    p < 0.05 with off higher than on; partially reproduced for one or two of three. The p < 0.004\n    bound is reported against each.\n- id: temporalis-f7f8-null\n  statement: Over the electrodes closest to the temporalis muscles (F7 and F8), none of sharpness\n    ratio, steepness ratio or PAC differs between patients off and on medication.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 2\n  quote: none of these measures differed between patients on and off medication over these electrodes\n    ... sharpness ratio, p = 0.73, uncorrected, steepness ratio, p = 0.394, uncorrected PAC, p = 0.191,\n    uncorrected\n  statistics:\n  - about: sharpness ratio\n    test: Wilcoxon signed rank\n    p: 0.73\n    corrected: none\n    n: 15 patients, on and off\n  - about: steepness ratio\n    test: Wilcoxon signed rank\n    p: 0.394\n    corrected: none\n    n: 15 patients, on and off\n  - about: PAC\n    test: Wilcoxon signed rank\n    p: 0.191\n    corrected: none\n    n: 15 patients, on and off\n  criterion: A claim of absence. Composite of F7 and F8, beta band, each measure as for C3 and C4;\n    Wilcoxon signed rank, uncorrected, at 0.05. Reproduced when no measure has p < 0.05; not\n    reproduced when any does. Report the three p-values and d either way.\n- id: temporalis-t7t8-null\n  statement: Over T7 and T8, also near the temporalis muscles, none of the three measures differs\n    between patients off and on medication.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 2\n  quote: Results were similar for T7 and T8, also near temporalis muscles (p > 0.05, uncorrected for all\n    comparisons)\n  statistics:\n  - test: Wilcoxon signed rank\n    p: 0.05\n    p_relation: \">\"\n    corrected: none\n    n: 15 patients, on and off\n  criterion: As for temporalis-f7f8-null, with the composite of T7 and T8.\n- id: fig2c-topography-sensorimotor\n  statement: Scalp topographies of the off against on medication test statistic for each measure are\n    consistent with a sensorimotor origin.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 2; Figure 2C legend\n  quote: found that topographies were consistent with a sensorimotor origin (Fig. 2C)\n  criterion: For each of the three beta measures, a Wilcoxon signed rank test off against on at every\n    scalp electrode. The paper does not name the critical value used to blank electrodes in Figure 2C\n    nor define a sensorimotor pattern. Readings for significance are p < 0.05 uncorrected and FDR\n    corrected over electrodes. Reproduced when, for each measure, the electrode with the smallest p\n    is C3, Cz, C4 or one of their neighbours in the 32-channel montage (FC1, FC2, FC5, FC6, CP1, CP2,\n    CP5, CP6), and none of F7, F8, T7 and T8 is significant; partially reproduced for one or two of\n    the three measures. The neighbour set is this file's reading of \"sensorimotor\".\n- id: offctrl-sharpness-null\n  statement: Beta sharpness ratio over sensorimotor electrodes does not differ between patients off\n    medication and controls.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 3; Table 2\n  quote: There was no significant difference between these groups for beta waveform sharpness ratio\n    (p = 0.363, uncorrected)\n  statistics:\n  - test: Wilcoxon rank sum\n    statistic: rank sum = 0.91\n    p: 0.3631\n    corrected: none (FDR corrected p = 1)\n    n: 15 patients off medication and 16 controls\n  expected:\n  - quantity: Cohen's d, beta sharpness ratio, off against controls\n    value: 0.19\n    tolerance: 0.019\n  criterion: A claim of absence. Composite C3 and C4 beta sharpness ratio, patients off against\n    controls, Wilcoxon rank sum at 0.05 uncorrected. Reproduced when p >= 0.05; not reproduced when\n    p < 0.05. Report the z statistic and d either way.\n- id: offctrl-steepness\n  statement: Beta steepness ratio over sensorimotor electrodes is higher in patients off medication\n    than in controls, with the average reference and with a bipolar montage.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 3; Table 2\n  quote: however steepness ratio did distinguish patients from controls (p = 0.033 using the average\n    referencing scheme and p = 0.028 for a bipolar referencing scheme, both FDR corrected)\n  statistics:\n  - about: average reference\n    test: Wilcoxon rank sum\n    statistic: rank sum = 2.53\n    p: 0.011\n    corrected: none (FDR corrected p = 0.0331)\n    n: 15 patients off medication and 16 controls\n  - about: average reference\n    test: Wilcoxon rank sum\n    statistic: rank sum = 2.53\n    p: 0.0331\n    corrected: FDR\n    n: 15 patients off medication and 16 controls\n  - about: bipolar montage\n    test: Wilcoxon rank sum\n    p: 0.028\n    corrected: FDR\n    n: 15 patients off medication and 16 controls\n  expected:\n  - quantity: rank sum z statistic, beta steepness ratio, off against controls\n    value: 2.53\n    tolerance: 0.253\n  - quantity: Cohen's d, beta steepness ratio, off against controls\n    value: 0.88\n    tolerance: 0.088\n  criterion: Composite C3 and C4 beta steepness ratio, patients off against controls, Wilcoxon rank sum\n    (z positive when off is larger), FDR corrected over the six tests of Table 2 for the average\n    reference. For the bipolar montage the paper does not give the FDR family; readings are the three\n    bipolar measures and the single test. Reproduced when the average reference test has corrected\n    p < 0.05 with off higher, z and d are within tolerance, and the bipolar test is significant under\n    one reading; partially reproduced when only the average reference result holds.\n- id: offctrl-pac-null\n  statement: With the average reference, beta PAC over sensorimotor electrodes does not differ between\n    patients off medication and controls.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 3; Table 2\n  quote: Somewhat surprisingly there was also no significant difference between PD patients off\n    medication and control participants for the PAC calculation (p = 0.236, uncorrected)\n  statistics:\n  - test: Wilcoxon rank sum\n    statistic: rank sum = 1.19\n    p: 0.236\n    corrected: none\n    n: 15 patients off medication and 16 controls\n  criterion: A claim of absence. As for offctrl-sharpness-null, with beta PAC, under the Methods' filter\n    lengths; the code's taps are shown as a variant.\n- id: offctrl-pac-csd\n  statement: With a current source density montage, beta PAC over sensorimotor electrodes is higher in\n    patients off medication than in controls.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 3\n  quote: When we tested the CSD referencing scheme using the current method for PAC calculation, there\n    was a significant difference between patients off medication and controls (p = 0.022)\n  statistics:\n  - test: Wilcoxon rank sum\n    p: 0.022\n    n: 15 patients off medication and 16 controls\n  criterion: CSD transform of the preprocessed scalp data with the CSD toolbox method (Kayser and Tenke,\n    spherical spline, flexibility m = 3; the toolbox's defaults for the rest, a standard choice), then\n    beta PAC as in fig2-pac-off-on at C3 and C4, composite, rank sum test of off against controls.\n    The paper does not say whether p = 0.022 is corrected; it is judged uncorrected. Reproduced when\n    p < 0.05 with off higher.\n- id: updrs-improvement\n  statement: Clinical scores improve with medication, UPDRS being lower on medication than off.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 1\n  quote: these changes were in the context of significant clinical improvement with medication as\n    measured by Unified Parkinson's Disease Rating Scale measures (Wilcoxon signed rank test statistic =\n    3.5, p = 0.003)\n  statistics:\n  - test: Wilcoxon signed rank\n    statistic: signed rank = 3.5\n    p: 0.003\n    n: 15 patients, on and off\n  expected:\n    quantity: Wilcoxon signed rank statistic, UPDRS off against on\n    value: 3.5\n    tolerance: 0.35\n  criterion: The paper does not say which UPDRS score was tested. Readings are the motor part (III)\n    total and the total of all parts the dataset holds. Reproduced when, under one reading, the signed\n    rank test gives p < 0.05 with scores lower on medication and the statistic is within tolerance;\n    partially reproduced when the test holds and the statistic does not.\n- id: fig1c-beta-alpha-peaks\n  statement: The average power spectrum of each group shows an oscillation in the beta band and a\n    prominent mu/alpha oscillation.\n  source: Figure 1C legend; Results, Waveform metrics differentiate PD medication state, paragraph 4\n  quote: Plots confirm that there is a β oscillation as well as a prominent α/μ oscillation\n  criterion: Welch power spectra as in the Methods (window 256 samples, overlap 128, nFFT 450, at 512 Hz;\n    pwelch's default Hamming window), at C3 and C4, averaged over electrodes and participants of each\n    group (off, on, controls). The paper does not define a peak. Reproduced when, in every group's\n    average spectrum, there is a local maximum between 8 and 12 Hz and one between 13 and 30 Hz.\n    Partially reproduced when the alpha peak is present in all groups and the beta peak in some.\n- id: table1-alpha-shape-off-on\n  statement: In the mu/alpha band (8 to 12 Hz), sharpness ratio and steepness ratio are also higher off\n    medication than on.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 4; Table 1\n  quote: We found these values to be overall similar to those we found for β, with the exception of PAC\n  statistics:\n  - about: alpha sharpness ratio\n    test: Wilcoxon signed rank\n    statistic: signed rank = 20\n    p: 0.0278\n    corrected: FDR\n    n: 15 patients, on and off\n  - about: alpha steepness ratio\n    test: Wilcoxon signed rank\n    statistic: signed rank = 12\n    p: 0.0121\n    corrected: FDR\n    n: 15 patients, on and off\n  expected:\n  - quantity: signed rank statistic, alpha sharpness ratio\n    value: 20\n    tolerance: 2\n  - quantity: Cohen's d, alpha sharpness ratio\n    value: 0.70\n    tolerance: 0.07\n  - quantity: signed rank statistic, alpha steepness ratio\n    value: 12\n    tolerance: 1.2\n  - quantity: Cohen's d, alpha steepness ratio\n    value: 0.60\n    tolerance: 0.06\n  criterion: As for fig2-sharpness-off-on with the band 8 to 12 Hz for zero crossings (192 taps by the\n    code's 3-cycle rule), FDR over the six tests of Table 1. Reproduced when both tests have corrected\n    p < 0.05 with off higher and all four values are within tolerance; partially reproduced when both\n    tests hold and a value is out of tolerance, or one test holds.\n- id: table1-alpha-pac-null\n  statement: In the mu/alpha band, PAC does not differ significantly between patients off and on\n    medication.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 4; Table 1\n  quote: with the exception of PAC, which was non-significant for μ/α, while being significant for β\n  statistics:\n  - test: Wilcoxon signed rank\n    statistic: signed rank = 30\n    p: 0.0881\n    corrected: FDR\n    n: 15 patients, on and off\n  expected:\n    quantity: Cohen's d, alpha PAC, off against on\n    value: 0.51\n    tolerance: 0.051\n  criterion: A claim of absence. Alpha (8 to 12 Hz) phase and 50 to 150 Hz amplitude PAC, composite C3\n    and C4, signed rank test, FDR corrected over the six tests of Table 1, at 0.05. Reproduced when\n    corrected p >= 0.05; not reproduced otherwise. The phase filter length is open (readings a to c in\n    the opening comment); the outcome is the one all readings give, and each is reported.\n- id: table2-alpha-offctrl\n  statement: In the mu/alpha band, steepness ratio is higher in patients off medication than in\n    controls, while sharpness ratio and PAC do not differ after correction.\n  source: Table 2\n  inferred: Values from Table 2; the text says only that alpha values were overall similar to beta,\n    except PAC.\n  statistics:\n  - about: alpha sharpness ratio\n    test: Wilcoxon rank sum\n    statistic: rank sum = 1.03\n    p: 1\n    corrected: FDR\n    n: 15 patients off medication and 16 controls\n  - about: alpha steepness ratio\n    test: Wilcoxon rank sum\n    statistic: rank sum = 2.53\n    p: 0.0331\n    corrected: FDR\n    n: 15 patients off medication and 16 controls\n  - about: alpha PAC\n    test: Wilcoxon rank sum\n    statistic: rank sum = 2.17\n    p: 0.0602\n    corrected: FDR\n    n: 15 patients off medication and 16 controls\n  expected:\n  - quantity: rank sum z, alpha steepness ratio\n    value: 2.53\n    tolerance: 0.253\n  - quantity: Cohen's d, alpha steepness ratio\n    value: 0.87\n    tolerance: 0.087\n  criterion: Composite C3 and C4 alpha measures, off against controls, rank sum tests FDR corrected over\n    the six tests of Table 2. Reproduced when steepness ratio has corrected p < 0.05 with off higher\n    and its z and d are within tolerance, and sharpness ratio and PAC have corrected p >= 0.05.\n    Partially reproduced when the steepness result holds and one of the others does not.\n- id: pac-beta-larger-than-alpha\n  statement: The off against on medication difference in PAC is larger in the beta band than in the\n    mu/alpha band.\n  source: Results, Waveform metrics differentiate PD medication state, paragraph 4\n  quote: for PAC, the difference between off medication and on medication in β was significantly larger\n    than the difference in μ/α for the same comparison (Wilcoxon signed rank test statistic = 11, p =\n    0.005)\n  statistics:\n  - test: Wilcoxon signed rank\n    statistic: signed rank = 11\n    p: 0.005\n    n: 15 patients\n  expected:\n    quantity: signed rank statistic, beta against alpha off-on PAC difference\n    value: 11\n    tolerance: 1.1\n  depends_on:\n  - fig2-pac-off-on\n  - table1-alpha-pac-null\n  criterion: Per patient, the composite PAC off minus on in beta and in alpha; signed rank test of the\n    two differences. The paper does not say whether raw or log PAC is differenced; raw PAC is the\n    measure of Tables 1 and 2 and the main reading, log PAC a variant. Reproduced when p < 0.05 with the\n    beta difference larger and the statistic within tolerance under one filter reading.\n- id: fig3-sharpness-pac-correlation\n  statement: Across patients, beta sharpness ratio and PAC over sensorimotor electrodes are positively\n    correlated both off and on medication.\n  source: Results, Relationships between sharpness/steepness ratio and PAC, paragraph 1; Figure 3\n  quote: sharpness ratio and PAC were correlated in both on and off medication states in sensorimotor\n    electrodes (off medication: r = 0.70, p = 0.004; on medication: r = 0.74, p = 0.002; Fig. 3)\n  statistics:\n  - about: off medication\n    test: Spearman correlation\n    statistic: r = 0.70\n    p: 0.004\n    n: 15 patients\n  - about: on medication\n    test: Spearman correlation\n    statistic: r = 0.74\n    p: 0.002\n    n: 15 patients\n  expected:\n  - quantity: Spearman r, sharpness ratio and PAC, off\n    value: 0.70\n    tolerance: 0.07\n  - quantity: Spearman r, sharpness ratio and PAC, on\n    value: 0.74\n    tolerance: 0.074\n  criterion: Spearman correlation across the 15 patients of composite beta sharpness ratio and composite\n    PAC, separately off and on (code Figures_2,3). Reproduced when both are positive with p < 0.05 and\n    within tolerance under one PAC filter reading; partially reproduced when both are significant and\n    one r is out of tolerance.\n- id: fig3-steepness-pac-correlation\n  statement: Across patients, beta steepness ratio and PAC over sensorimotor electrodes are positively\n    correlated both off and on medication.\n  source: Results, Relationships between sharpness/steepness ratio and PAC, paragraph 1; Figure 3\n  quote: steepness ratio and PAC are also highly correlated for both medication states (off medication\n    r = 0.74, p = 0.002; on medication r = 0.68, p = 0.006)\n  statistics:\n  - about: off medication\n    test: Spearman correlation\n    statistic: r = 0.74\n    p: 0.002\n    n: 15 patients\n  - about: on medication\n    test: Spearman correlation\n    statistic: r = 0.68\n    p: 0.006\n    n: 15 patients\n  expected:\n  - quantity: Spearman r, steepness ratio and PAC, off\n    value: 0.74\n    tolerance: 0.074\n  - quantity: Spearman r, steepness ratio and PAC, on\n    value: 0.68\n    tolerance: 0.068\n  criterion: As for fig3-sharpness-pac-correlation, with the steepness ratio.\n- id: fig4a-sensorimotor-q4\n  statement: Over sensorimotor electrodes, patients' beta waveforms mostly have sharper peaks than\n    troughs and steeper decays than rises (quadrant 4 of peak-to-trough against rise-to-fall ratio).\n  source: Results, Waveform shape, paragraph 1; Figure 4A, C\n  quote: In general, sensorimotor electrode oscillations had a sharper peak with a steeper decay,\n    falling in quadrant 4 (Q4) in Figure 4\n  criterion: One point per patient, electrode (C3, C4) and medication state, 60 points, of log10\n    peak-to-trough ratio against log10 rise-to-fall ratio (code Figure_4). Q4 is positive\n    peak-to-trough and negative rise-to-fall (the shaded quadrant in Figure_4). Reproduced when more\n    than half the points are in Q4 and Q4 holds more points than any other quadrant; partially\n    reproduced when Q4 is the most common quadrant without a majority.\n- id: q4-patient-counts\n  statement: Nine of 15 patients have both off and on data in Q4 at C3, eight at C4; eight have both\n    electrodes in Q4, giving nine patients with at least one electrode in Q4 on and off.\n  source: Results, Waveform shape, paragraph 2\n  quote: Out of 15 patients, nine patients met this criterion for C3 and eight met the criterion for C4\n    ... Using this approach there were nine total Q4 observations for each waveform metric\n  expected:\n  - quantity: patients with off and on in Q4 at C3\n    value: 9\n    tolerance: 1\n  - quantity: patients with off and on in Q4 at C4\n    value: 8\n    tolerance: 1\n  - quantity: patients with at least one electrode in Q4 both off and on\n    value: 9\n    tolerance: 1\n  depends_on:\n  - fig4a-sensorimotor-q4\n  criterion: A patient meets the criterion at an electrode when both its off and its on point are in Q4\n    (Results, Waveform shape, paragraph 2). Counts are integers; 10% of 8 or 9 is under one patient,\n    so the tolerance is one patient. The two electrode counts are compared to 9 and 8 in the order\n    C3, C4, and, since the code does not label which half of its recordings is C3, also in the swapped\n    order as a second reading.\n- id: fig4b-temporalis-variable-shape\n  statement: Electrodes closest to the temporalis muscles (F7 and F8) show a more variable waveform\n    shape than sensorimotor electrodes.\n  source: Results, Waveform shape, paragraph 1; Figure 4B\n  quote: In contrast, electrodes closest to temporalis muscles had a more variable waveform shape pattern\n  depends_on:\n  - fig4a-sensorimotor-q4\n  criterion: The same 60 patient points at F7 and F8 as at C3 and C4. The paper does not define\n    variability. Readings are (a) the share of points in the most common quadrant is lower at F7 and F8\n    than at C3 and C4; (b) the standard deviation of the points about their centroid (both log ratios)\n    is larger at F7 and F8. Reproduced when both readings agree; resting on the reading when one does.\n- id: controls-q4\n  statement: Control participants show the same pattern, their sensorimotor beta waveforms falling\n    mainly in Q4.\n  source: Results, Waveform shape, paragraph 1\n  quote: Although not shown, control participant data exhibited the same pattern (i.e., sensorimotor\n    electrode data fell mainly in Q4)\n  criterion: As for fig4a-sensorimotor-q4, with the 32 control points (16 controls, C3 and C4).\n- id: table3-q4-effect-size\n  statement: Restricting to patients whose sensorimotor waveforms fall in Q4 both off and on increases\n    the off against on effect size of all three measures.\n  source: Results, Waveform shape, paragraph 2; Table 3\n  quote: Effect size increased for all measures, at least marginally, when using the Q4 shape as an\n    inclusion criterion (Table 3)\n  expected:\n  - quantity: Cohen's d, sharpness ratio, Q4 patients\n    value: 0.95\n    tolerance: 0.095\n  - quantity: Cohen's d, steepness ratio, Q4 patients\n    value: 0.70\n    tolerance: 0.07\n  - quantity: Cohen's d, PAC, Q4 patients\n    value: 0.83\n    tolerance: 0.083\n  - quantity: Cohen's d, PAC, all patients (Table 3)\n    value: 0.75\n    tolerance: 0.075\n  depends_on:\n  - q4-patient-counts\n  - fig2-sharpness-off-on\n  - fig2-steepness-off-on\n  - fig2-pac-off-on\n  criterion: For each included patient, the mean over the electrodes in Q4 both off and on (one\n    electrode when only one qualifies), then Cohen's d off against on as in the code's effectsize, for\n    beta sharpness ratio, steepness ratio and PAC. Table 3's all-patient PAC d (0.75) differs from\n    Table 1's (0.83); readings for PAC are raw (code) and log10 (Methods), the same scaling used for\n    all and Q4. Reproduced when, under one reading, d in Q4 patients exceeds d in all patients for all\n    three measures; the Q4 values are compared to Table 3 within tolerance and reported. Partially\n    reproduced when d increases for two of three.\n"
}
```

```
File created successfully at: claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml paper/10.1523-eneuro.0151-19.2019.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml
python3 - "$f" <<'EOF'
import sys
p=sys.argv[1]; s=open(p).read()
s=s.replace("electrodes (off medication: r = 0.70, p = 0.004; on medication: r = 0.74, p = 0.002; Fig. 3)",
            "electrodes (off medication ... r = 0.70, p = 0.004; on medication ... r = 0.74, p = 0.002; Fig. 3)")
s=s.replace("(off medication\n    r = 0.74, p = 0.002; on medication r = 0.68, p = 0.006)",
            "(off medication\n    ... r = 0.74, p = 0.002; on medication ... r = 0.68, p = 0.006)")
open(p,'w').write(s)
EOF
grep -n ': .*: ' $f | grep -v '^\S*#' | head; python tools/claims_check.py $f paper/10.1523-eneuro.0151-19.2019.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml; grep -nE '—|rather' $f; grep -vE '^\s*#' $f | grep -nE '^\s+[^-#][^:]*: .*: |^\s{4,}[a-z(].*: ' | head; grep -c 'criterion:' $f
```

```
14:    statistic: signed rank = 12
15:    p: 0.006
16:    corrected: none (FDR corrected p = 0.0121)
17:    n: 15 patients, on and off
19:    statistic: signed rank = 12
20:    p: 0.0121
21:    corrected: FDR
22:    n: 15 patients, on and off
25:    value: 12
26:    tolerance: 1.2
24
```

**Agent calls Bash**

```bash
python3 -c "
import yaml;d=yaml.safe_load(open('claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

```
24 23 17 29 24 14
```

**Agent**

I wrote the claims file at `claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml`. The quote checker reports 24 claims, 23 quotes, 29 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record, full text from Europe PMC (PMC6553574). It includes the Methods, the figure legends and Tables 1 to 3. The only supplement, Extended Data 1, is the analysis code. I read it at github.com/SwannLab/Jackson_2019, commit a7c89f5. The code's printed outputs match the beta values in Tables 1 and 2 and the Figure 3 correlations. I opened no PDF pages. For the dataset I read only its OpenNeuro title and README, which ask users to cite this paper.

**Claims:**
- 24 claims: 23 have quotes and 1 is marked `inferred` (the mu/alpha patients-off-against-controls results, which appear only in Table 2).
- 17 claims carry statistics, 29 entries in all.
- 14 claims have expected values with tolerances.
- All 24 have a criterion.
- They cover:
  - **Off against on medication:** sharpness ratio, steepness ratio and PAC; the bipolar montage; the null results at F7/F8 and T7/T8; the topography; UPDRS.
  - **Off against controls:** sharpness null, steepness higher, PAC null with the average reference, PAC higher with the CSD reference.
  - **Power spectra:** beta and alpha peaks in Figure 1C.
  - **Mu/alpha band:** Tables 1 and 2, and PAC difference larger in beta than in alpha.
  - **Figure 3:** sharpness and steepness each correlate with PAC.
  - **Figure 4 shapes:** most sensorimotor waveforms fall in quadrant 4 (Q4: sharper peaks, steeper decays), with patient counts of 9 at C3 and 8 at C4; F7/F8 shapes vary more; controls show the same pattern.
  - **Table 3:** effect sizes are larger when only Q4 patients are included.

**Details the paper leaves open, with the readings named:**
- **Artifact rejection:** the marks were made by hand and are not published. Readings: (a) the dataset's own annotations, if it has any; (b) no rejection beyond the code's rule that drops extrema within 100 samples of either end.
- **Noisy electrode exclusion:** (a) the dataset's bad-channel marks; (b) all 32 scalp electrodes kept. The eye electrodes stay out of the average reference in both.
- **PAC filter length:** the Methods say 231 ms and 240 ms (118 and 123 samples at 512 Hz). The code uses 231 and 240 taps. The Methods' values are the main reading and the code's are a variant.
- **Mu/alpha PAC phase filter:** 192 taps (3 cycles), 231 taps, or 118 samples.
- **Cohen's d for PAC:** raw PAC (what the code does; gives 0.83, as in Table 1) or log10 PAC (what the Methods say). Table 3 gives 0.75 for the same all-patient effect size, which is inconsistent with Table 1.
- **Wilcoxon p-value:** normal approximation, which is what the code's printed p-values show, with the exact test as a variant.
- **Which UPDRS score:** the motor part (III) total, or the total of all parts.
- **Bipolar montage, FDR family:** the three bipolar measures or the single test.
- **CSD result (p = 0.022):** the paper does not say whether it is corrected; I judge it uncorrected.
- **Undefined terms:** "peak" in the power spectrum is read as a local maximum in the band. "Sensorimotor" topography is read as the most significant electrode being C3, Cz, C4 or their neighbours. "More variable" shape at F7/F8 is read two ways: a smaller share of points in the most common quadrant, or a larger spread.
- **Electrode order in the code:** the code does not say which half of its patient recordings is C3, so the 9 and 8 Q4 counts are also checked in swapped order.

**Missing from the paper or its code:**
- **Preprocessing:** the MATLAB preprocessing and the manual artifact marks.
- **Analyses not in the code:** the mu/alpha, bipolar, CSD, F7/F8, T7/T8, power-spectrum and topography analyses, and the Q4 effect sizes. Their criteria rest on the Methods text alone.

No claim had to be dropped for missing text.

## End of run

18 turns, 4 minutes, result: success.
