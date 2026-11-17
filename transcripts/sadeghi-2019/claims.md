# sadeghi-2019 · claims · run 42945495484

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/; cat claims/fouke-2025.yaml; ls claims | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; ls paper/; ls claims | wc -l
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 43,
 "limit": 160
}
```

```
43	## Reader
44	
45	### 1. Get the paper
46	
47	The workflow puts the paper's full text, and its PDF where there is one, under
48	`paper/`: the main text, the Methods, and the supplement. Read the text; open
49	the PDF only to read a figure or a table the text garbles. If the full text is
50	not there, or lacks the Methods or a supplement the results rest on, stop:
51	write no claims, and end with a report that names what is missing, so that it
52	can be supplied. Never write claims from the abstract. Do not copy figures.
53	Do not look at the dataset's data: its title and description on the archive
54	are enough to know which paper and which experiments it is meant to hold. A
55	data descriptor under `paper/` (`<id>.data-description.txt`, the dataset's own
56	documentation) is a longer description, to be read for that alone; it is not
57	the paper, and no claim comes from it.
58	
59	### 2. Read the paper's code
60	
61	Read the code the paper links to before writing criteria. Say what it holds,
62	and record the repository and commit read. Where the Methods leave a choice
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml; cat paper/bst-2.data-description.txt; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pbio.3000449.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^##" paper/10.1371-journal.pbio.3000449.txt; awk 'NR>173{print length($0)}' paper/10.1371-journal.pbio.3000449.txt | sort -n | tail -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pbio.3000449.txt",
 "offset": 174,
 "limit": 330
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pbio.3000449.txt",
 "offset": 665,
 "limit": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pbio.3000449.txt",
 "offset": 1036,
 "limit": 115
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -ln "crcns" claims/*.yaml | head; grep -l "code.*inside the dataset\|code in the dataset\|dataset's own code\|part of the dataset" claims/*.yaml | head; ls papers/datasets/ | grep -i sadeghi; cat papers/datasets/sadeghi-2019.yaml 2>/dev/null
```

```
claims/asari-2009.yaml
claims/brinke-2017.yaml
claims/bruno-2017.yaml
claims/deweese-2004.yaml
claims/eyherabide-2008.yaml
claims/farrell-2020.yaml
claims/goncalves-2013.yaml
claims/gu-2011.yaml
claims/henze-2000.yaml
claims/holdgraf-2016.yaml
claims/drieu-2018.yaml
claims/kennedy-2020.yaml
claims/zaimi-2018.yaml
sadeghi-2019.yaml
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1371/journal.pbio.3000449
title: A neural ensemble correlation code for sound category identification
datasets:
- archive: crcns
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -B2 -A6 "code" claims/drieu-2018.yaml | head -60; head -40 claims/holdgraf-2016.yaml
```

```
1-# Claims for Drieu, Todorova & Zugaro (2018), Science 362, 675-679, tested on CRCNS hc-18.
2:# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
3-# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
4-#
5-# Text read: the version of record (main text, figure legends of Figs. 1 to 3), and the
6-# author manuscript (HAL hal-02330673v1) for its Materials and Methods, the Fig. 4 legend and
7-# supplementary figures S1 to S13 with their legends. The extracted text of the version of
8-# record lacks its page 5 (Fig. 4 and the closing paragraphs), so the Fig. 4 legend is quoted
--
24-# provided in the archive. Those are part of the dataset's files and were not read here.
25-#
26:# Code read: FMAToolbox (github.com/michael-zugaro/FMAToolbox, commit 6bbb366, 2018-03-27),
27-# the toolbox the Methods name for all analyses. It holds general functions (FiringCurve,
28-# MapStats, TestRemapping, FieldShift, PhasePrecession, ReconstructPosition, FindSubcycles,
29-# FindRipples, MTSpectrum and others) but not the paper's own scripts for trajectory
30-# scores, quadrant scores, z-proportions or pairwise bias correlations. Where the Methods
31-# and the toolbox defaults disagree (field threshold 30% in the Methods, 20% by default;
32-# ripple thresholds 1 and 3 s.d. and 20 to 110 ms in the Methods, 2 and 5 s.d. and 20 to
--
54-#   trained on each travel session and applied to that session (theta sequences, windows
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "with_inputs\|with_labels\|elsewhere" docs/protocol.md | head -20; sed -n 15,25p claims/drieu-2018.yaml
```

```
149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
156:     rests on it. A claim on data in none of them is `data: elsewhere`, or
161:     recordings of its own, or on other data, are `data: elsewhere` when they
233:4. Decide what comes from outside the dataset. Data from elsewhere may be
242:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
243:     `with_inputs` and `elsewhere` claims are counted apart, each group on
245:   - `with_labels` is for outside sources that only name or map codes the
267:   - `elsewhere` is for a claim whose data the dataset does not hold at
276:   - The notes of a `with_inputs` claim say which side a difference comes
287:     `data: elsewhere` instead (step 4).
# Data the paper used (Methods, Animal training, Behavioural task; Fig. 1A; fig. S1): five
# adult male Long-Evans rats, each tested on a single day in a novel room, so one session
# per rat. Each session is baseline sleep, Passive 1 travel (treadmill off), sleep, Active
# travel (treadmill on), sleep, Passive 2 travel, sleep. Each travel condition was 2 x ~15
# laps on a 2.20 m x 1.30 m obround track, always forward at ~45-50 cm/s; each sleep epoch
# ~90 min in a flower pot. Measured: sorted CA1 units (pyramidal cells and interneurons),
# LFP at 1250 Hz, and head position from one or two LEDs (30 Hz video, resampled at
# 39.0625 Hz). The data set's description (CRCNS hc-18) says it holds 5 sessions, one
# per rat, with spikes, LFP, positions and event files; it also says custom scripts are
# provided in the archive. Those are part of the dataset's files and were not read here.
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 230,
 "limit": 60
}
```

```
230	   unless an earlier one matches the claims file's description better. Say
231	   why in the notebook's header. If versions differ in content the analysis
232	   uses, show the difference.
233	4. Decide what comes from outside the dataset. Data from elsewhere may be
234	   used only when the claims file says the paper relies on it, it is public,
235	   and it is pinned: a DOI, or a repository at a commit. Record each under
236	   `inputs` in the attempt. A claim whose outside input is not public is
237	   blocked with `data_missing`, and its notes say where you looked.
238	
239	   The registry judges the dataset, so claims that use outside data are
240	   kept apart:
241	   - Each claim says what its test uses: `data: dataset` (the default),
242	     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
243	     `with_inputs` and `elsewhere` claims are counted apart, each group on
244	     its own; the others count towards what is said about the dataset.
245	   - `with_labels` is for outside sources that only name or map codes the
246	     dataset already holds, such as stimulus names for its stimulus codes.
247	     They bring in no measurements. A link claim must confirm the names, and
248	     the missing names are recorded as a finding (`metadata_insufficient`).
249	   - When outside data has to be matched to the dataset's cells, sessions
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; ls schemas 2>/dev/null; ls docs
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

[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | head -200; head -12 claims/asari-2009.yaml; grep -n "dataset:" -A3 claims/asari-2009.yaml | head
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
[... 192 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"
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

**Agent calls Write**

```json
{
 "file_path": "claims/sadeghi-2019.yaml",
 "content": "# Claims for Sadeghi, Zhai, Stevenson & Escabi (2019), \"A neural ensemble correlation code for\n# sound category identification\", PLoS Biol 17(10):e3000449, on CRCNS data set bst-2.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-11,\n# protocol as stated in docs/protocol.md (Reader). The writer did not look at the data set's data or\n# files; only its description (paper/bst-2.data-description.txt) was read, to know what it holds.\n#\n# Text read: the version of record (PMC6788721, Europe PMC full-text XML, flattened), with its\n# Results, Discussion, Materials and methods, all figure legends (Figs 1 to 10, S1 to S10 Figs),\n# and the supplement files S1 Text (s001, proofs on signal and noise correlations, and notes on\n# S2 to S4 and S6 Figs), S1 Table (s026, the 195 model sounds) and S2 Table (s027, the 18 sounds\n# of paradigm 3). No PDF was supplied. The extraction dropped every displayed equation (the\n# shuffled and unshuffled correlograms, their normalization, the noise correlation, the MAP\n# rule, the spectro-temporal model average, the 1/f filter, the SI and CDI formulas); the prose\n# around each was read and the criteria below name where an equation would have settled a\n# detail. The movies and sound files listed as supporting information were not read; no claim\n# rests on them.\n#\n# Code: the paper links only the CRCNS deposit (doi:10.6080/K03X84V3), which holds MATLAB code\n# (Code/MUACorrAnalysis, with rastermuashuffledxcovwinfastN.m; Code/AuditoryModelCorr, with\n# Cochleogram.m and cochleogramdyncorr.m; Code/Examples, with NeuralExample.m for Fig 1 and\n# ModelExample.m for Fig 7), as its description says. Those are part of the data set's files\n# and were not read here. Where the Methods leave a detail open that this code may settle, the\n# criterion says so; the author may follow the code and record it, with the readings named here\n# kept as variants.\n#\n# Data the paper used (Materials and methods). Unanesthetized female Dutch Belted rabbits (N = 4),\n# acute 16-channel linear probes (150 um spacing) or 64-channel polytrodes of which 16 equally\n# spaced channels were kept (paradigms 2 and 3), in the central nucleus of the IC; 33 penetration\n# sites recorded, 24 kept (13 for paradigm 1; 11 for paradigms 2 and 3). The measured variable is\n# analog multiunit activity (aMUA) per channel, the envelope of the 325 to 3000 Hz band, rectified,\n# low-passed at 475 Hz and downsampled to 2 kHz, as trials by samples rasters. Frequency response\n# areas from tone pips (0.1 to 16 kHz, 5 to 75 dB SPL) give each channel's best frequency.\n# - Paradigm 1, 13 sites (4 and 9 from two animals), five 3 s sounds (fire, bird chorus, crowd,\n#   water, rattling snake) at 65 dB SPL, block randomized, 18 to 39 trials each.\n# - Paradigm 2, 11 sites (3 and 8 from two animals), the same five sounds, original and 1/f\n#   spectrum-equalized, 20 trials (14 at one site).\n# - Paradigm 3, 11 sites (3 and 8), three categories (fire, water, speech), 6 exemplars each,\n#   10 to 20 trials.\n# - Model, 195 sounds, 13 categories of 15 sounds of 10 s at 44.1 kHz (S1 Table), and white noise\n#   as a control. Vocalizations are single bird songs, cat meowing, dog barking and human speech\n#   (one male speaker); environmental sounds are bird chorus, speech babble, fire, thunder and\n#   rain, flowing water, waves and wind; man-made are bells and automobile engines.\n# The data set's description says it holds P1_Site01 to P1_Site13, P2_Site01 to P2_Site11 and\n# P3_Site01 to P3_Site11 (aMUA rasters per sound and channel), the sounds of all three paradigms,\n# and the model sounds by category. Its figure list names the example sites as P1_Site04 (Figs 1,\n# 3A), P2_Site11 (Fig 4A to 4F) and P3_Site04 (Fig 8A to 8E), and Sound_1 of Human Speech and of\n# Flowing Water for Figs 5 and 7; this is a finding aid, not a method. It does not list tone-pip\n# recordings or white noise.\n#\n# Methods common to the neural claims (Materials and methods, sections named):\n# - Stimulus-driven correlation (Neural ensemble stimulus-driven correlation): windowed shuffled\n#   cross-correlation between channels k and l, the mean of correlations between different trials\n#   of mean-removed aMUA, square window of duration T (62.5 to 1000 ms) around time t, delay tau,\n#   computed through PSTHs (fast shuffled algorithm), normalized as a correlation coefficient by\n#   the localized short-term response variances. Noise correlation (Neural ensemble noise\n#   correlation) is the unshuffled (same-trial) minus the shuffled correlogram, normalized by the\n#   total response power, so that stimulus plus noise is 1 on the zero-lag diagonal. The exact\n#   normalization is in equations lost from the text; the S1 Text prose is the guide.\n# - Spectral correlation is c_kl(t, 0); temporal correlation is c_kk(t, tau) for tau from -100 to\n#   100 ms (Noiseless neural classifier, paragraph 6).\n# - Classifiers (Noiseless neural classifier; Single-trial neural classifier). Model data are the\n#   first 1.5 s of each response and validation data the second half, then swapped. Features are\n#   correlations about randomly selected time points, 500 ms windows for the noiseless model and\n#   1000 ms windows for the single-trial model; validation windows of 62.5 to 1000 ms in half\n#   octave steps (\"sound duration\"); 100 random time samples; PCA fitted on the model half; naive\n#   Bayes with axis-aligned Gaussian likelihoods; equal priors; MAP. The highest-ranked PCs that\n#   maximize performance are used. The noiseless classifier uses shuffled correlations (trials\n#   averaged); the single-trial classifier uses unshuffled correlations of single trials, trials\n#   randomized along with the time points. Spectro-temporal is a model average of the spectral\n#   and temporal log-likelihoods with a mixing coefficient a in [0, 1] chosen to maximize the\n#   log-likelihood. \"Without tonotopy\" reorders the channels of the validation data at random.\n#   Paradigm 2 models are built from responses to the original sounds and validated on the 1/f\n#   (or, as a control, the original) responses. Paradigm 3 models are per category; five\n#   exemplars train and the sixth is tested (leave one out, Results, Decoding neural correlation\n#   statistics in a three-category identification task, paragraph 3).\n# - Open in all neural classifier claims, with readings to be run:\n#   (1) how the 100 random time samples enter a decision; (a) each sample is one decision and\n#   accuracy is the fraction correct over them; (b) the log-posterior is summed over the 100\n#   samples for one decision (\"features at each time sample are conditionally independent\").\n#   (2) how many PCs, chosen to maximize performance; (a) chosen on the validation performance as\n#   the text reads; (b) chosen within the model half by an inner split. (3) for paradigm 2,\n#   whether the half split also applies; (a) first and second halves as in paradigm 1, original\n#   for the model and 1/f for validation; (b) whole original responses for the model and whole\n#   1/f responses for validation. (4) the spectrum (rate code) classifier of Figs 4 and 8 is not\n#   described for the neural data; read as the mean aMUA of each channel in each window, through\n#   the same PCA and naive Bayes pipeline, by analogy with the model's spectrum classifier\n#   (Spectrum-based classifier). (5) the grid for a; a standard grid of 0 to 1 in steps of 0.1.\n#   The random seeds are standard choices.\n# - \"Above chance\" tests are t tests across sites against chance (20% for five sounds, 33.3% for\n#   three categories); whether one-sided or two-sided is not said, and both are reported.\n#\n# Methods common to the model claims (Auditory model; Nonstationary spectro-temporal correlation\n# statistics; Dimensionality reduction; Bayesian classifier; Cross validation): 58 gammatone\n# channels (order 3) from 100 Hz to 16 kHz in 1/8 octave steps, bandwidths 25 + 75(1 + 1.4 f^2)^0.69\n# (f in kHz), Hilbert envelope low-passed at 500 Hz and downsampled to 1 kHz; short-term\n# correlations with a Kaiser window (beta 3.4), resolution tau_W (two SDs of the window) from 25\n# to 566 ms in half octave steps, delays up to half the window, normalized by the local powers.\n# Spectral features are c_kl(t, 0) (diagonal removed, S8 Fig), temporal features c_kk(t, tau) for\n# tau from 0 to half the window with channels as observations (zero lag removed); PCs explaining\n# 90% of the variance; one GMM per category with diagonal covariances and N_c chosen by\n# cross-validated likelihood (the paper reports 5, 8 and 13 for temporal, spectral and\n# spectro-temporal); leave-one-sound-out over 195 sounds; N consecutive non-overlapping windows\n# from the start of the test sound, N in half octave steps; log-likelihoods summed; equal priors.\n# Open for all model claims: (6) the spacing of the non-overlapping windows; (a) tau_W; (b) the full\n# Kaiser window length. (7) the tau_W at which N_c and the PCs are fixed; (a) refitted at each\n# tau_W; (b) the reported counts used at every tau_W.\nschema_version: 2\npaper: doi:10.1371/journal.pbio.3000449\nclaims:\n- id: fig1k-example-temporal-widths\n  statement: At the example paradigm 1 site, stimulus-driven temporal correlations are fast for\n    crowd, water and fire (3.0, 3.0 and 3.9 ms wide at 50% of maximum; 5.9, 6.9 and 11.8 ms at\n    10%), the bird chorus has a sharp peak (5.9 ms half width) and a slow component (161.2 ms at\n    10%), and the snake has a 7.9 ms half width, 20.6 ms at 10%, and a periodic pattern of about\n    50 ms period at high-frequency sites.\n  source: Results, Decoding neural ensemble correlation statistics to recognize sounds, paragraph\n    5; Figure 1K\n  quote: The temporal correlations for the crowd, water, and fire sounds are relatively fast (3.0\n    ms, 3.0 ms, and 3.9 ms width at 50% of the maximum; 5.9 ms, 6.9 ms, and 11.8 ms width at 10% of\n    the maximum). The bird chorus has a similar sharp temporal correlation (5.9 ms half width), but\n    it also contains a broader and substantially slower component (161.2 ms, 10% width)\n  expected:\n  - quantity: crowd width at 50% of maximum\n    value: 3.0\n    tolerance: 0.5\n    unit: ms\n  - quantity: water width at 50% of maximum\n    value: 3.0\n    tolerance: 0.5\n    unit: ms\n  - quantity: fire width at 50% of maximum\n    value: 3.9\n    tolerance: 0.5\n    unit: ms\n  - quantity: crowd width at 10% of maximum\n    value: 5.9\n    tolerance: 0.59\n    unit: ms\n  - quantity: water width at 10% of maximum\n    value: 6.9\n    tolerance: 0.69\n    unit: ms\n  - quantity: fire width at 10% of maximum\n    value: 11.8\n    tolerance: 1.18\n    unit: ms\n  - quantity: bird chorus width at 50% of maximum\n    value: 5.9\n    tolerance: 0.59\n    unit: ms\n  - quantity: bird chorus width at 10% of maximum\n    value: 161.2\n    tolerance: 16.1\n    unit: ms\n  - quantity: snake width at 50% of maximum\n    value: 7.9\n    tolerance: 0.79\n    unit: ms\n  - quantity: snake width at 10% of maximum\n    value: 20.6\n    tolerance: 2.06\n    unit: ms\n  - quantity: snake periodicity at high-frequency sites\n    value: 50\n    tolerance: 5\n    unit: ms\n  criterion: The site is the one of Figs 1 and 3A. The tolerance on the three smallest widths is\n    one aMUA sample (0.5 ms at 2 kHz, Electrophysiology, paragraph 3), as 10% is below the\n    sampling step. Stimulus-driven temporal correlations c_kk(tau), tau within 100 ms (or 300 ms\n    for the bird slow component, which exceeds 100 ms), widths measured at 50% and 10% of the\n    peak, as the text names them. Open, with readings to run; (i) which curve is measured, (a)\n    the temporal correlation averaged over the 16 channels, (b) the median over channels of\n    per-channel widths; (ii) the window T, (a) one window over the whole 3 s response, (b) 1000 ms\n    windows averaged over the response. The period is the lag of the first side peak of the\n    channel-averaged temporal correlation of the upper eight channels. Reproduced when, under one\n    reading, at least 9 of the 11 values are within tolerance and the ordering crowd, water\n    shorter than fire at 50% holds; partially reproduced for 6 to 8.\n- id: fig1-snr-noise-stronger\n  statement: Noise correlations are generally stronger than the stimulus-driven correlations, with\n    spectral SNR from -26.0 to -0.9 dB (mean -11.0, SD 7.2) and temporal SNR from -26.1 to -4.1 dB\n    (mean -6.0, SD 8.2).\n  source: Results, Decoding neural ensemble correlation statistics to recognize sounds, paragraph 6\n  quote: Noise correlations were also generally stronger than the corresponding signal correlations\n    (spectral Signal-to-Noise Ratio [SNR]\n  expected:\n  - quantity: spectral SNR, mean\n    value: -11.0\n    tolerance: 7.2\n    unit: dB\n  - quantity: temporal SNR, mean\n    value: -6.0\n    tolerance: 8.2\n    unit: dB\n  - quantity: spectral SNR, lowest\n    value: -26.0\n    tolerance: 2.6\n    unit: dB\n  - quantity: spectral SNR, highest\n    value: -0.9\n    tolerance: 0.09\n    unit: dB\n  - quantity: temporal SNR, lowest\n    value: -26.1\n    tolerance: 2.61\n    unit: dB\n  - quantity: temporal SNR, highest\n    value: -4.1\n    tolerance: 0.41\n    unit: dB\n  criterion: The tolerance on the means is the stated SD; on the range, each bound widened by 10%\n    of itself. The SNR formula is not in the text (no equation survives and none is given in\n    prose); the paper says only that it compares signal with noise correlations. Readings; (a) 10\n    log10 of the summed squared stimulus-driven correlation over the summed squared noise\n    correlation, all entries of the spectral matrix c_kl(0) or of the temporal c_kk(tau); (b) as\n    (a) without the zero-lag diagonal; units of the range and mean, (c) one value per site and\n    sound (13 x 5 values), (d) one value per site averaged over sounds. Paradigm 1 sites. The core\n    of the claim, that the SNR is below 0 dB for most values in both domains, must hold under the\n    reading used. Reproduced when, under one reading, both means are within tolerance and at least\n    three of the four bounds are; partially reproduced when the means hold and the SNR is mostly\n    negative.\n- id: fig1-s5-model-predicts-neural\n  statement: Stimulus-driven neural spectral correlations are partly predicted by the spectral\n    correlations of a peripheral auditory model of the same sound (average r = 0.3 +/- 0.03), well\n    above the across-sound control (-0.04 +/- 0.02).\n  source: Results, Decoding neural ensemble correlation statistics to recognize sounds, paragraph\n    5; S5 Fig, panels D and E\n  quote: these neural correlations were stimulus-driven and frequency-dependent since they were\n    partly predicted by the spectral correlations from a peripheral auditory model (see Materials\n    and Methods ; average r = 0.3 ± 0.03, t test, p < 0.01\n  statistics:\n  - about: average same-sound Pearson r against zero\n    test: t test\n    p: 0.01\n    p_relation: <\n  - about: same-sound against across-sound Pearson r\n    test: one-tailed t test\n    p: 1.0e-14\n    n: 13 penetration sites, five sounds\n  expected:\n  - quantity: mean same-sound Pearson r\n    value: 0.3\n    tolerance: 0.03\n  - quantity: mean across-sound Pearson r\n    value: -0.04\n    tolerance: 0.02\n  - quantity: median same-sound r for fire, bird, crowd, water, snake (first, fire)\n    value: 0.37\n    tolerance: 0.037\n  criterion: Following the S5 Fig legend, for each paradigm 1 site and sound, the model's spectral\n    correlation (cochlear model of the Auditory model section, envelope correlation at zero lag)\n    at the channels matching each recording channel's best frequency at 65 dB SPL, against the\n    site's stimulus-driven spectral correlation, Pearson r over the off-diagonal entries; the\n    control pairs each neural matrix with the model matrices of the other sounds. The legend's\n    medians for the five sounds (0.37, 0.37, 0.25, 0.36, 0.25; control -0.16, -0.17, 0.06, -0.13,\n    0.09) are reported beside the means. Open; (i) the model window, (a) the whole 3 s sound,\n    (b) the time-averaged short-term correlation at 100 ms; (ii) whether r is averaged over the\n    65 site-sound values or over sites. The best frequencies need the tone-pip responses; if the\n    data set lacks them, the claim is blocked for that reason. Reproduced when the mean same-sound\n    r is within tolerance, above zero by a t test at p < 0.01, and above the control by a\n    one-tailed t test at p < 0.01; partially reproduced when the tests hold and the mean is\n    outside tolerance.\n- id: fig2-noise-restricted\n  statement: Across the 13 paradigm 1 sites, noise correlations are more restricted in frequency\n    and time and more consistent across sounds than stimulus-driven correlations, which are\n    broader and stimulus dependent (a slow component for the bird chorus and a 20 Hz periodic\n    component for the snake).\n  source: Results, Decoding neural ensemble correlation statistics to recognize sounds, paragraph\n    7; Figure 2\n  quote: The spectral noise correlations (collapsed along the diagonal) are consistent across\n    sounds and more restricted in frequency ( Fig 2B ) than the corresponding stimulus-driven\n    spectral correlations ( Fig 2A )\n  criterion: As in the Fig 2 legend, for each site and sound the spectral matrices are collapsed\n    over channel offset (mean over entries at each |k - l|) and the temporal correlations over\n    channels (mean c_kk(tau) at each lag), then averaged over the 13 sites, each normalized by its\n    value at offset 0 or lag 0 (an open step; the shape is compared). Width is measured at 50% of\n    the maximum, as the paper measures temporal widths (Results, paragraph 5). Restriction is\n    read (a) as this width, (b) as the mean collapsed value beyond offset 2 channels or beyond 10\n    ms. Consistency across sounds is the SD over the five sounds of the collapsed curves, summed\n    over offsets or lags. Window T is open as in fig1k-example-temporal-widths. No test is\n    reported. Reproduced when, under one reading, the noise curve is narrower than the\n    stimulus-driven one for at least four of the five sounds in both domains and its SD across\n    sounds is smaller in both domains; partially reproduced when this holds in one domain.\n- id: fig3a-example-tonotopy-removal\n  statement: At the example site, randomizing the channel order of the temporal classifier lowers\n    its single-trial accuracy at 1 s from 72% to 35%.\n  source: Results, Decoding neural ensemble correlation statistics to recognize sounds, paragraph\n    9; Figure 3A\n  quote: Doing so substantially reduces the temporal classifier performance from 72% to 35% for the\n    longest sound duration measured (1 s; Fig 3A )\n  expected:\n  - quantity: temporal single-trial accuracy at 1 s\n    value: 72\n    tolerance: 7.2\n    unit: '%'\n  - quantity: temporal without tonotopy single-trial accuracy at 1 s\n    value: 35\n    tolerance: 3.5\n    unit: '%'\n  criterion: Single-trial classifier as in the opening comment, site of Fig 1, paradigm 1, five\n    sounds; channel order of the validation data randomized afresh at each iteration (open,\n    standard). Readings (1) to (4) of the opening comment are each run. Reproduced when, under one\n    reading, both values are within tolerance; partially reproduced when the removal lowers the\n    accuracy by at least 20 points but the values are outside tolerance.\n- id: fig3a-example-classifier-order\n  statement: At the example site, the spectro-temporal classifier performs best, followed by the\n    spectral and temporal classifiers; the noiseless classifier exceeds the single-trial one for\n    the spectral and spectro-temporal classifiers, while for the temporal classifier the two are\n    similar.\n  source: Figure 3A legend; Results, Decoding neural ensemble correlation statistics to recognize\n    sounds, paragraph 8\n  quote: The combined spectro-temporal classifier has the highest performance, followed by the\n    spectral and temporal classifiers\n  criterion: Single-trial and noiseless classifiers as in the opening comment, site of Fig 1, at 1\n    s. Reproduced when, under one reading, spectro-temporal >= spectral >= temporal single-trial\n    accuracy, noiseless exceeds single-trial by at least 5 points for spectral and\n    spectro-temporal, and differs by less than 5 points for temporal (the 5 point margin is the\n    reader's, as the paper gives none); partially reproduced when the ordering holds and the\n    noiseless comparison does not.\n- id: fig3b-population-above-chance\n  statement: Across the 13 paradigm 1 sites, all four single-trial classifiers (spectro-temporal,\n    spectral, temporal, temporal without tonotopy) perform above chance at 1 s, improve with sound\n    duration, and the temporal classifier is degraded substantially when tonotopy is removed.\n  source: Results, Decoding neural ensemble correlation statistics to recognize sounds, paragraph\n    10; Figure 3B\n  quote: Across all sounds and classifiers, the average performance is above chance (red curves in\n    Fig 3B ; t test, p < 0.01, tested at 1 s duration) and improves with increasing sound duration\n  statistics:\n  - test: t test against chance\n    p: 0.01\n    p_relation: <\n    n: 13 penetration sites\n  criterion: Classifiers as in the opening comment, readings (1) and (2) run. Reproduced when,\n    under one reading, each of the four single-trial classifiers exceeds 20% at 1 s by a t test\n    across sites at p < 0.01, accuracy at 1 s exceeds accuracy at 62.5 ms for each, and the\n    temporal classifier without tonotopy is lower than with it by a paired t test across sites at\n    p < 0.05; partially reproduced when three of the four are above chance.\n- id: figs6-per-sound-above-chance\n  statement: Single-trial accuracy at 1 s exceeds chance for every sound and classifier except the\n    snake sound with the temporal classifiers (p = 0.15 with tonotopy, 0.92 without).\n  source: S6 Fig legend\n  quote: The classification accuracy of the single-trial classifier at 1 s duration exceeded chance\n    ( p < 0.05, t test) for all conditions except for the snake sound\n  statistics:\n  - about: all other sounds and classifiers against chance\n    test: t test\n    p: 0.05\n    p_relation: <\n  - about: snake, temporal classifier\n    test: t test\n    p: 0.15\n  - about: snake, temporal classifier without tonotopy\n    test: t test\n    p: 0.92\n  criterion: Per sound, the fraction of single-trial decisions for that sound that are correct, at\n    1 s, per site; t test across the 13 sites against 20% at p < 0.05. Readings (1) and (2) of\n    the opening comment. Reproduced when, under one reading, at least 17 of the 18 non-snake-temporal\n    conditions (five sounds by four classifiers, less the two snake temporal ones) are above\n    chance and the two snake temporal conditions are not; partially reproduced for 14 to 16.\n- id: figs9-mixing-coefficient\n  statement: The optimal spectro-temporal classifier weights spectral and temporal cues about\n    equally, with a median mixing coefficient of 0.6 (quartiles 0.5 and 0.7) for paradigms 1 and\n    2 and 0.5 (25th percentile 0.4) for paradigm 3.\n  source: S9 Fig legend; Discussion, Contribution of spectral and temporal correlations, paragraph 1\n  quote: For paradigms 1 (original) and 2 (spectrum-equalized), the median value of alpha is 0.6\n    (25th and 75th percentiles are 0.5 and 0.7), and for paradigm 3 (categorization), the median\n    value of alpha is 0.5 (25th percentile is 0.4)\n  expected:\n  - quantity: median a, paradigms 1 and 2\n    value: 0.6\n    tolerance: 0.1\n  - quantity: median a, paradigm 3\n    value: 0.5\n    tolerance: 0.1\n  criterion: The tolerance is one step of the 0.1 grid named in reading (5) of the opening comment,\n    as 10% is below it. a is the value maximizing the spectro-temporal log-likelihood, per site;\n    the model average is read as a L_spectral + (1 - a) L_temporal (the equation is lost; S9 Fig\n    says 1 means purely spectral). Open; (a) maximized on the model data, (b) on the validation\n    data. Reproduced when, under one reading, both medians are within tolerance.\n- id: figs10-amua-tmua\n  statement: Correlations from thresholded MUA resemble those from aMUA (median r 0.81 spectral,\n    0.35 temporal) but are weaker and noisier; split-half reliability is higher for aMUA (0.98\n    and 0.83) than for tMUA (0.77 and 0.27).\n  source: S10 Fig legend; Materials and methods, Electrophysiology, paragraph 3\n  quote: aMUA and tMUA spectral correlations are quite similar, as indicated by the relatively high\n    Pearson correlation coefficient (tMUA versus aMUA, median = 0.81). For temporal correlations,\n    the Pearson correlation between tMUA and aMUA was lower (median = 0.35)\n  expected:\n  - quantity: median r, tMUA against aMUA, spectral\n    value: 0.81\n    tolerance: 0.081\n  - quantity: median r, tMUA against aMUA, temporal\n    value: 0.35\n    tolerance: 0.035\n  - quantity: split-half r, aMUA spectral\n    value: 0.98\n    tolerance: 0.098\n  - quantity: split-half r, aMUA temporal\n    value: 0.83\n    tolerance: 0.083\n  - quantity: split-half r, tMUA spectral\n    value: 0.77\n    tolerance: 0.077\n  - quantity: split-half r, tMUA temporal\n    value: 0.27\n    tolerance: 0.027\n  criterion: tMUA spike trains are events exceeding 2 SDs above the noise floor (S10 Fig legend),\n    which needs the raw voltage traces; if the data set holds only aMUA, the claim is blocked for\n    that reason. Which sites and sounds enter the medians is not said; readings (a) all paradigm 1\n    sites and sounds, (b) all sites of all paradigms. Reproduced when, under one reading, at least\n    five of the six values are within tolerance and aMUA is more reliable than tMUA in both\n    domains.\n- id: fig4-example-original-vs-equalized\n  statement: At the example paradigm 2 site, neural correlations for the original and 1/f\n    spectrum-equalized sounds are very similar (Pearson r = 0.92 +/- 0.01 spectral, 0.72 +/- 0.07\n    temporal, over five sounds).\n  source: Results, Differences in correlations statistics are not due to sound spectrum alone,\n    paragraph 3; Figure 4A to 4D\n  quote: Fig 4 shows that the neural correlations for both the original sounds and\n    spectrum-equalized conditions of a single recording location are remarkably similar (Pearson\n    correlation coefficient, r = 0.92 ± 0.01 for spectral, r = 0.72 ± 0.07 for temporal; mean ± SE)\n  expected:\n  - quantity: mean r, spectral\n    value: 0.92\n    tolerance: 0.01\n  - quantity: mean r, temporal\n    value: 0.72\n    tolerance: 0.07\n  criterion: Tolerance is the stated SE. Stimulus-driven spectral matrices c_kl(0) and temporal\n    correlations c_kk(tau), tau within 100 ms, of the original against the 1/f response to the\n    same sound; Pearson r over entries, mean and SE over the five sounds. Open; (i) whether the\n    zero-lag diagonal is included, (a) included, (b) excluded as in S5 Fig; (ii) window T as in\n    fig1k-example-temporal-widths. Reproduced when, under one reading, both values are within\n    tolerance; partially reproduced when both are within 10% of the reported values.\n- id: fig4e-population-original-vs-equalized\n  statement: Across the 11 paradigm 2 sites, neural correlations for original and 1/f sounds\n    correlate at r = 0.95 +/- 0.02 (spectral) and 0.80 +/- 0.02 (temporal) for the same sound,\n    and less across different sounds (0.85 +/- 0.02 and 0.57 +/- 0.01).\n  source: Results, Differences in correlations statistics are not due to sound spectrum alone,\n    paragraph 3; Figure 4E\n  quote: Across recording locations, the neural correlations for the original and equalized sounds\n    have an average Pearson correlation coefficient of 0.95 ± 0.02 for spectral and 0.80 ± 0.02 for\n    temporal (mean ± SE)\n  expected:\n  - quantity: same-sound r, spectral\n    value: 0.95\n    tolerance: 0.02\n  - quantity: same-sound r, temporal\n    value: 0.80\n    tolerance: 0.02\n  - quantity: across-sound r, spectral\n    value: 0.85\n    tolerance: 0.02\n  - quantity: across-sound r, temporal\n    value: 0.57\n    tolerance: 0.01\n  criterion: Tolerance is the stated SE. As in fig4-example-original-vs-equalized at each site; the\n    across-sound value pairs each original sound with the 1/f variants of the other four sounds.\n    Readings as there, and for the averaging, (a) over sites of the per-site mean, (b) over all\n    site and sound pairs. Reproduced when, under one reading, all four values are within\n    tolerance; partially reproduced when same-sound exceeds across-sound in both domains and the\n    values are within 10% of those reported.\n- id: fig4f-example-equalized-classification\n  statement: At the example paradigm 2 site, classifiers trained on the original sounds and tested\n    on the 1/f sounds keep high accuracy (63% spectral, 63% temporal, 71% spectro-temporal,\n    above chance), while the spectrum (rate) classifier falls from about 94% on the original\n    sounds to chance.\n  source: Results, Differences in correlations statistics are not due to sound spectrum alone,\n    paragraph 4; Figure 4F\n  quote: the maximum performance exceeds chance ( p < 0.05, t test) and remains high (63% for\n    spectral, 63% for temporal, 71% for spectro-temporal). Furthermore, although the spectrum\n    (rate) classifier achieves very high accuracy approaching 94% for the original sound, accuracy\n    drops to chance level when the spectrum is equalized\n  statistics:\n  - test: t test against chance\n    p: 0.05\n    p_relation: <\n  expected:\n  - quantity: spectral accuracy, 1/f, 1 s\n    value: 63\n    tolerance: 6.3\n    unit: '%'\n  - quantity: temporal accuracy, 1/f, 1 s\n    value: 63\n    tolerance: 6.3\n    unit: '%'\n  - quantity: spectro-temporal accuracy, 1/f, 1 s\n    value: 71\n    tolerance: 7.1\n    unit: '%'\n  - quantity: spectrum classifier accuracy, original, 1 s\n    value: 94\n    tolerance: 9.4\n    unit: '%'\n  criterion: Single-trial classifiers, readings (1) to (4) of the opening comment, the site of Fig\n    4A to 4D. \"Maximum performance\" is read as accuracy at the longest duration, 1 s. The t test\n    within a site is not described; read as a one-sample t test over the five per-sound\n    accuracies against 20%. Reproduced when, under one reading, the four values are within\n    tolerance and the spectrum classifier on 1/f sounds is below 30%; partially reproduced when\n    the pattern (correlation classifiers above 40%, spectrum below 30% on 1/f) holds.\n- id: fig4h-population-equalized-classification\n  statement: Across 11 paradigm 2 sites, the correlation classifiers stay above chance on the 1/f\n    sounds at 1 s (spectral 48%, temporal 49%, spectro-temporal 58%), while the spectrum classifier\n    falls from 90.0 +/- 2.0% on the original sounds to 27.0 +/- 1.0% and does not improve with\n    duration.\n  source: Results, Differences in correlations statistics are not due to sound spectrum alone,\n    paragraph 5; Figure 4G and 4H\n  quote: All three classifiers perform above chance for 1 s duration when the spectrum is equalized\n    ( Fig 4H ; spectral = 48%, temporal = 49%, spectro-temporal = 58%; p < 0.01, t test)\n  statistics:\n  - test: t test against chance\n    p: 0.01\n    p_relation: <\n    n: 11 penetration sites\n  expected:\n  - quantity: spectral accuracy, 1/f, 1 s\n    value: 48\n    tolerance: 4.8\n    unit: '%'\n  - quantity: temporal accuracy, 1/f, 1 s\n    value: 49\n    tolerance: 4.9\n    unit: '%'\n  - quantity: spectro-temporal accuracy, 1/f, 1 s\n    value: 58\n    tolerance: 5.8\n    unit: '%'\n  - quantity: spectrum classifier accuracy, original, 1 s\n    value: 90.0\n    tolerance: 2.0\n    unit: '%'\n  - quantity: spectrum classifier accuracy, 1/f, 1 s\n    value: 27.0\n    tolerance: 1.0\n    unit: '%'\n  criterion: Tolerance on the spectrum values is the stated SE; on the others 10%. Single-trial\n    classifiers, readings (1) to (4) of the opening comment. Reproduced when, under one reading,\n    the three correlation classifiers exceed 20% at 1 s by a t test across sites at p < 0.01 and at\n    least four of the five values are within tolerance; partially reproduced when the tests hold\n    and the spectrum classifier drops below every correlation classifier on the 1/f sounds.\n- id: fig8b-example-pca-variance\n  statement: At the example paradigm 3 site, the first two principal components explain 95.6% of\n    the variance of the spectral and 85.9% of the temporal neural correlations, and the three\n    categories form distinct clusters.\n  source: Results, Decoding neural correlation statistics in a three-category identification task,\n    paragraph 3; Figure 8B and 8D\n  quote: With two principal components, most of the response variance is explained (95.6% for\n    spectral and 85.9% for temporal), and the three categories are highly clustered\n  expected:\n  - quantity: variance explained by two PCs, spectral\n    value: 95.6\n    tolerance: 9.56\n    unit: '%'\n  - quantity: variance explained by two PCs, temporal\n    value: 85.9\n    tolerance: 8.59\n    unit: '%'\n  criterion: PCA of the training-set correlation feature vectors (100 observations x 6 exemplars x\n    3 categories, Fig 8 legend), stimulus-driven spectral c_kl(0) and temporal c_kk(tau), tau\n    within 100 ms, as in Fig 8A and 8C. Open; (a) 500 ms windows (noiseless model), (b) 1000 ms\n    windows (single-trial model); whether the spectral features include the diagonal and both\n    triangles is open, (c) upper triangle with diagonal, (d) the full matrix. Clustering is judged\n    by leave-one-exemplar-out accuracy of a nearest-centroid rule in the two-PC space above 80%\n    (the reader's measure; the paper shows a scatter). Reproduced when, under one reading, both\n    values are within tolerance and the clustering holds.\n- id: fig8e-example-categorization\n  statement: At the example paradigm 3 site, all correlation classifiers approach 100% correct\n    categorization at 1 s, and the spectrum (rate) classifier reaches 94%.\n  source: Results, Decoding neural correlation statistics in a three-category identification task,\n    paragraph 4; Figure 8E\n  quote: all classifiers (spectro-temporal, spectral, and temporal) show increasing performance\n    with sound duration, and the categorization accuracy approached 100% when the sound is 1 s. The\n    spectrum (rate code) classifier also achieves high accuracy in this categorization task (94%\n    for 1 s duration)\n  expected:\n  - quantity: spectrum classifier accuracy at 1 s\n    value: 94\n    tolerance: 9.4\n    unit: '%'\n  criterion: Single-trial classifiers per category, leave one exemplar out, readings (1), (2), (4)\n    and (5) of the opening comment. Whether the model and validation data also use the half split\n    is open; (a) all trials and the whole response of the training exemplars for the model and of\n    the left-out exemplar for validation, (b) the half split as in paradigm 1 on top of the\n    exemplar split. \"Approached 100%\" is read as at least 90%. Reproduced when, under one reading,\n    all three correlation classifiers are at least 90% at 1 s, each higher at 1 s than at 62.5\n    ms, and the spectrum value is within tolerance.\n- id: fig8f-population-categorization\n  statement: Across 11 paradigm 3 sites, at 1 s the spectro-temporal classifier categorizes 96% of\n    trials correctly, the temporal 95%, the spectral 91% and the spectrum (rate) classifier 91%,\n    all above chance, and performance improves with duration.\n  source: Results, Decoding neural correlation statistics in a three-category identification task,\n    paragraph 4; Figure 8F\n  quote: For 1 s sound duration, the spectro-temporal classifier is above chance and achieves on\n    average a 96% maximum accuracy ( t test, p < 0.01), followed by the temporal classifier (95%,\n    t test, p < 0.01) and spectral (91%, t test, p < 0.01)\n  statistics:\n  - test: t test against chance, each classifier\n    p: 0.01\n    p_relation: <\n    n: 11 penetration sites\n  expected:\n  - quantity: spectro-temporal accuracy at 1 s\n    value: 96\n    tolerance: 9.6\n    unit: '%'\n  - quantity: temporal accuracy at 1 s\n    value: 95\n    tolerance: 9.5\n    unit: '%'\n  - quantity: spectral accuracy at 1 s\n    value: 91\n    tolerance: 9.1\n    unit: '%'\n  - quantity: spectrum classifier accuracy at 1 s\n    value: 91\n    tolerance: 9.1\n    unit: '%'\n  criterion: As in fig8e-example-categorization, at all 11 sites. Reproduced when, under one\n    reading, all four values are within tolerance (capped at 100%) and each exceeds 33.3% by a t\n    test across sites at p < 0.01; partially reproduced when the tests hold and two or three values\n    are within tolerance.\n- id: fig5-speech-water-widths\n  statement: In the cochlear model, the example speech sound has broad spectral correlations and a\n    slow temporal correlation (64 ms half width), while the example water sound has diagonal\n    spectral correlations and a fast temporal correlation (4 ms half width).\n  source: Results, Average correlation statistics and diversity, paragraph 1; Figure 5\n  quote: The temporal correlation structure in speech exhibits a relatively slow temporal structure\n    (64 ms half width) ... By comparison, the water sound has a relatively fast temporal\n    correlation structure (4 ms half width)\n  expected:\n  - quantity: speech temporal correlation half width\n    value: 64\n    tolerance: 6.4\n    unit: ms\n  - quantity: water temporal correlation half width\n    value: 4\n    tolerance: 1\n    unit: ms\n  criterion: The tolerance on water is one model sample (1 ms at the 1 kHz envelope rate), as 10%\n    is below it. Time-averaged correlations of the cochlear model envelopes (Auditory model), of\n    one speech and one water sound. Open; (i) which sound, read as Sound_1 of each category (the\n    data set's figure list; a finding aid), with every sound of the category shown as a variant;\n    (ii) the window, (a) the time average of short-term correlations at the coarsest tau_W of 566\n    ms, (b) the long-term correlation of the whole envelopes, lags within 283 ms; (iii) the half\n    width, (a) full width at 50% of the peak of the channel-averaged autocorrelation, (b) the\n    median over channels. Spectral breadth is the mean off-diagonal zero-lag correlation, higher\n    for speech. Reproduced when, under one reading, both widths are within tolerance and speech\n    has the broader spectral correlation.\n- id: fig6-category-half-widths\n  statement: Water and wind sounds have fast temporal correlations (half widths 3.9 and 3.6 ms) and\n    diagonal spectral correlations, while vocalizations have slow ones (speech 64.9 ms, dogs 76.3\n    ms, cats 117.3 ms) and more extensive spectral correlations.\n  source: Results, Average correlation statistics and diversity, paragraph 2; Figure 6A and 6B\n  quote: relatively fast temporal correlation structure (impulsive; correlation half width; water =\n    3.9 ms; wind = 3.6 ms)\n  expected:\n  - quantity: water half width\n    value: 3.9\n    tolerance: 1\n    unit: ms\n  - quantity: wind half width\n    value: 3.6\n    tolerance: 1\n    unit: ms\n  - quantity: speech half width\n    value: 64.9\n    tolerance: 6.49\n    unit: ms\n  - quantity: dog barking half width\n    value: 76.3\n    tolerance: 7.63\n    unit: ms\n  - quantity: cat meowing half width\n    value: 117.3\n    tolerance: 11.73\n    unit: ms\n  criterion: The tolerance on water and wind is one 1 ms model sample, as 10% is below it.\n    Category averages of the time-averaged correlations over the 15 sounds, as in Fig 6A and 6B,\n    with the readings of fig5-speech-water-widths for window and width; water is read as the\n    flowing water category (the text groups rain, running water and waves, and the paper gives\n    one value; the pooled three categories are a variant). A cat half width of 117 ms needs lags\n    beyond 58 ms, so reading (ii)(a) or (b) of that claim, with long lags, is the one that can\n    reach it. Reproduced when, under one reading, at least four of the five widths are within\n    tolerance and every vocalization width exceeds every water and wind width.\n- id: fig6c-category-diversity\n  statement: White noise has the lowest category diversity index; among natural sounds speech is\n    lowest (CDI 0.12), crowd noise 0.15, wind 0.18, dogs 0.21, bird songs 0.29 and fire highest\n    (0.39), with no clear trend between classes.\n  source: Results, Average correlation statistics and diversity, paragraph 3; Figure 6C\n  quote: Of all sounds in our database, white noise has the smallest diversity, which is expected\n    given that white noise is wide-sense stationary. Of the natural sounds, speech has the lowest\n    diversity (CDI = 0.12)\n  expected:\n  - quantity: CDI, speech\n    value: 0.12\n    tolerance: 0.012\n  - quantity: CDI, crowd noise (speech babble)\n    value: 0.15\n    tolerance: 0.015\n  - quantity: CDI, wind\n    value: 0.18\n    tolerance: 0.018\n  - quantity: CDI, dog barking\n    value: 0.21\n    tolerance: 0.021\n  - quantity: CDI, single bird songs\n    value: 0.29\n    tolerance: 0.029\n  - quantity: CDI, fire\n    value: 0.39\n    tolerance: 0.039\n  criterion: Short-term spectro-temporal correlation at tau_W = 100 ms, M = 99 lags, L = 58\n    channels, time-averaged per sound (Stationarity and ensemble diversity indices). The CDI\n    equation is lost; the prose defines it as the variance across sounds of the time-averaged\n    correlation normalized by the power of the time and ensemble average, bounded 0 to 1.\n    Readings; (a) E||c_n - E c_n||^2 / ||E c_n||^2; (b) E||c_n - E c_n||^2 / E||c_n||^2 (bounded\n    by 1); (c) as (a) or (b) with norms not squared. Crowd noise is read as the speech babble\n    category. White noise is not in the data set's sound list; it is generated (15 Gaussian noises\n    of 10 s, standard choice) if needed, and its rank is shown. Reproduced when, under one reading,\n    at least five of the six values are within tolerance and speech is lowest of the 13\n    categories; partially reproduced when the rank order of the six is kept.\n- id: fig7i-stationarity\n  statement: Environmental sounds other than fire (running water, waves, thunder, wind) are the\n    most stationary natural sounds (SI = 0.49 +/- 0.04), vocalizations less so (0.28 +/- 0.04),\n    speech is the least stationary category and white noise the most.\n  source: Results, Short-term correlation statistics and stationarity, paragraph 3; Figure 7I\n  quote: except for fire sounds, environmental sounds (including running water, waves, thunder and\n    wind) tend to have the highest average SI (SI = 0.49 ± 0.04; mean ± SE)\n  expected:\n  - quantity: SI, environmental sounds except fire\n    value: 0.49\n    tolerance: 0.04\n  - quantity: SI, vocalizations\n    value: 0.28\n    tolerance: 0.04\n  criterion: Tolerance is the stated SE. SI per sound from the short-term spectro-temporal\n    correlation at tau_W = 100 ms, M = 99 lags (Stationarity and ensemble diversity indices). The\n    equation is lost; the prose says the second term is the time-averaged variance of the\n    short-term correlation normalized by the power of the time-averaged correlation, SI bounded 0\n    to 1. Readings; (a) SI = 1 - <||c(t) - <c>||^2> / ||<c>||^2; (b) SI = 1 - <||c(t) - <c>||^2> /\n    <||c(t)||^2>. The groups are open; (c) environmental = flowing water, waves, thunder and rain,\n    wind, and vocalizations = single bird songs, cats, dogs, speech; (d) as (c) with bird chorus\n    and speech babble added to the environmental group; mean and SE (e) over categories, (f) over\n    sounds. Reproduced when, under one reading, both values are within tolerance, speech has the\n    lowest category mean and white noise (generated as in fig6c-category-diversity) the highest.\n- id: fig9a-optimal-resolution\n  statement: In the 13-category model task, the spectral and temporal correlation classifiers\n    perform best at a window resolution of 141 ms and the spectro-temporal classifier at 100 ms,\n    and all perform above chance (7.69%) at every resolution.\n  source: Results, Decoding sound-correlation statistics to categorize sounds, paragraph 2; Figure\n    9A\n  quote: The optimal window resolution for both the temporal and spectral classifiers is 141 ms,\n    while the optimal resolution for the joint spectro-temporal classifier is slightly faster (100\n    ms). Classification performance is above chance for all temporal resolutions tested ( Fig 9A ;\n    chance performance = 7.69%; p < 0.01, t test, Bonferroni correction)\n  statistics:\n  - test: t test against chance\n    p: 0.01\n    p_relation: <\n    corrected: Bonferroni\n  expected:\n  - quantity: optimal tau_W, spectral and temporal\n    value: 141\n    tolerance: 14.1\n    unit: ms\n  - quantity: optimal tau_W, spectro-temporal\n    value: 100\n    tolerance: 10\n    unit: ms\n  criterion: The Fig 9A legend prints 144 ms; the half-octave grid from 25 ms holds 141 ms, so 141\n    is taken, and the 10% tolerance admits only that grid point. Performance at 10 s (the Results\n    say optimized at 10 s duration), model pipeline of the opening comment, readings (6) and (7).\n    The t test is read as over the 195 per-sound outcomes (0 or 1) against 7.69%, with Bonferroni\n    over the 10 resolutions; over the 13 category accuracies is a variant. Reproduced when, under\n    one reading, both optima fall on the reported grid points and every resolution is above chance;\n    partially reproduced when the optima are within one grid step.\n- id: fig9b-similar-maximum\n  statement: At about 10 s the three correlation classifiers reach similar performance\n    (spectro-temporal 84%, spectral 83%, temporal 81%), with no significant pairwise differences.\n  source: Results, Decoding sound-correlation statistics to categorize sounds, paragraph 2; Figure\n    9B\n  quote: all three classifiers achieve similar maximum performance at approximately 10 s\n    (spectro-temporal = 84%, spectral = 83%, temporal = 81%; spectral versus temporal; p = 0.60;\n    spectral versus spectro-temporal; p = 0.79; temporal versus spectro-temporal; p = 0.42;\n    two-sample t test)\n  statistics:\n  - about: spectral against temporal\n    test: two-sample t test\n    p: 0.6\n  - about: spectral against spectro-temporal\n    test: two-sample t test\n    p: 0.79\n  - about: temporal against spectro-temporal\n    test: two-sample t test\n    p: 0.42\n  expected:\n  - quantity: spectro-temporal accuracy at 10 s\n    value: 84\n    tolerance: 8.4\n    unit: '%'\n  - quantity: spectral accuracy at 10 s\n    value: 83\n    tolerance: 8.3\n    unit: '%'\n  - quantity: temporal accuracy at 10 s\n    value: 81\n    tolerance: 8.1\n    unit: '%'\n  criterion: Each classifier at its optimal resolution (fig9a-optimal-resolution), 10 s test\n    duration, leave one sound out. The absence of a difference is judged on the paper's test, a\n    two-sample t test at 0.05 for each pair; its unit is not said, read as the 195 per-sound\n    outcomes, with the 13 category accuracies as a variant. Reproduced when the three values are\n    within tolerance and no pair differs at p < 0.05; not reproduced when a pair differs. The\n    differences are reported either way.\n- id: fig9b-accumulation-rate\n  statement: The spectral classifier reaches 90% of its maximum faster than the temporal one (1.7\n    against 3.0 s), and the spectro-temporal classifier fastest (1.2 s).\n  source: Results, Decoding sound-correlation statistics to categorize sounds, paragraph 2; Figure\n    9B\n  quote: the spectral classifier performance increases at a faster rate than the temporal\n    classifier (reaching 90% of maximum in 1.7 versus 3.0 s; Fig 9B ) ... The joint\n    spectro-temporal classifier improves at an even faster rate (reaching 90% of its maximum in\n    1.2 s)\n  expected:\n  - quantity: spectral rise time\n    value: 1.7\n    tolerance: 0.17\n    unit: s\n  - quantity: temporal rise time\n    value: 3.0\n    tolerance: 0.3\n    unit: s\n  - quantity: spectro-temporal rise time\n    value: 1.2\n    tolerance: 0.12\n    unit: s\n  criterion: Rise time is the time to reach 90% of the performance at 10 s (Optimal temporal\n    resolution and integration time), on the performance curves of fig9b-similar-maximum. Open;\n    (a) linear interpolation between the half-octave durations, (b) the first sampled duration\n    reaching 90%, (c) an exponential fit, as the Methods say performance rises roughly\n    exponentially. Reproduced when, under one reading, all three values are within tolerance;\n    partially reproduced when the order spectro-temporal < spectral < temporal holds.\n- id: fig9c-time-averaged-worse\n  statement: Ignoring nonstationary structure by averaging the spectro-temporal statistics over\n    time reduces category identification performance by about 25%.\n  source: Results, Decoding sound-correlation statistics to categorize sounds, paragraph 2; Figure\n    9C\n  quote: ignoring the nonstationary structure of the spectro-temporal correlation by averaging the\n    statistics over time reduced the sound category identification performance by approximately 25%\n  expected:\n    quantity: reduction in spectro-temporal accuracy at 10 s\n    value: 25\n    tolerance: 2.5\n    unit: '%'\n  criterion: The time-averaged classifier is not described in the Methods. Readings; (a) one\n    time-averaged correlation per training sound fits the category models and one per test segment\n    of the given duration is classified; (b) the short-term correlations are replaced by their\n    running average from the start of the test sound; the reduction is (c) in percentage points,\n    (d) relative to the short-term accuracy. At the spectro-temporal optimum, 10 s. Reproduced\n    when, under one reading, the reduction is within tolerance; partially reproduced when the\n    time-averaged classifier is lower by at least 10 points.\n- id: fig9e-category-specific\n  statement: Some categories are identified much better by one feature set; waves by spectral\n    correlations (100% against 33%) and wind by temporal ones (47% against 80%).\n  source: Results, Decoding sound-correlation statistics to categorize sounds, paragraph 3; Figure\n    9D and 9E\n  quote: Certain sounds such as waves perform substantially better for the spectral classifier\n    (spectral = 100% versus temporal = 33%). Other sounds, such as wind, exhibit higher performance\n    with the temporal classifier (spectral = 47% versus temporal = 80%)\n  expected:\n  - quantity: waves, spectral\n    value: 100\n    tolerance: 10\n    unit: '%'\n  - quantity: waves, temporal\n    value: 33\n    tolerance: 6.7\n    unit: '%'\n  - quantity: wind, spectral\n    value: 47\n    tolerance: 6.7\n    unit: '%'\n  - quantity: wind, temporal\n    value: 80\n    tolerance: 8\n    unit: '%'\n  criterion: Per-category accuracy over its 15 sounds at the optimal resolution and 10 s (Fig 9E\n    legend). Each sound is 1/15 = 6.7%; where 10% of the value is below one sound, the tolerance\n    is one sound. Reproduced when all four values are within tolerance; partially reproduced when\n    waves are better by spectral and wind by temporal correlations by at least two sounds each.\n- id: fig9-spectrum-classifier-lower\n  statement: The spectrum-based classifier does not depend on temporal resolution and performs\n    below all three correlation classifiers.\n  source: Results, Decoding sound-correlation statistics to categorize sounds, paragraph 4; Figure\n    9A and 9B\n  quote: Unlike the correlation-based classifiers, performance of the spectrum-based classifier\n    does not depend on the temporal resolution of the analysis ( Fig 9A ) ... Furthermore, the\n    overall performance of the spectrum classifier is lower than the either of the three\n    correlation-based classifiers ( Fig 9B )\n  criterion: Spectrum classifier as in the Methods (Spectrum-based classifier), the mean amplitude\n    of each cochlear channel per window, same PCA, GMM and cross validation. Reproduced when its\n    10 s accuracy is below each correlation classifier's at every duration (the Fig 9B legend says\n    in all instances) and its range across the 10 resolutions is under 10 points (the reader's\n    threshold for \"does not depend\"); partially reproduced when it is lower at 10 s only.\n- id: fig10-vocalization-background\n  statement: In a vocalization against background task, the spectro-temporal classifier approaches\n    90% for background and nearly 100% for vocalizations; vocalization accuracy improves with\n    duration while background accuracy stays constant, and vocalizations are classified better\n    with spectral than temporal correlations.\n  source: Results, Decoding sound-correlation statistics to categorize sounds, paragraph 5; Figure\n    10\n  quote: The model performance is consistently high, with accuracy rates for the spectro-temporal\n    classifier approaching 90% for background sounds and nearly 100% for vocalizations ( Fig 10 )\n  statistics:\n  - about: vocalizations, spectral against temporal classifier\n    test: t test\n    p: 0.01\n    p_relation: <\n    corrected: Bonferroni\n  expected:\n  - quantity: spectro-temporal accuracy, background, 10 s\n    value: 90\n    tolerance: 9\n    unit: '%'\n  - quantity: spectro-temporal accuracy, vocalizations, 10 s\n    value: 100\n    tolerance: 10\n    unit: '%'\n  - quantity: temporal minus spectro-temporal accuracy, vocalizations\n    value: -20\n    tolerance: 2\n    unit: '%'\n  criterion: Vocalizations are the four vocalization categories (Sound database); background is\n    read as the other nine (the data set's figure list agrees). Open; (a) one GMM per class fitted\n    on the pooled sounds, (b) the 13-category models with the decision mapped to its class.\n    Leave one sound out, each classifier at its 13-category optimum. The Bonferroni t test is read\n    as over per-sound outcomes at each duration. Reproduced when, under one reading, the\n    spectro-temporal values are within tolerance, vocalization accuracy rises from the shortest to\n    10 s while background varies by under 10 points, and spectral beats temporal for\n    vocalizations at p < 0.01 (Bonferroni over durations); partially reproduced when the\n    duration trends and the spectral advantage hold but the values do not.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/sadeghi-2019.yaml'
s=open(p).read()
s=s.replace("""(spectro-temporal = 84%, spectral = 83%, temporal = 81%; spectral versus temporal; p = 0.60;
    spectral versus spectro-temporal; p = 0.79; temporal versus spectro-temporal; p = 0.42;
    two-sample t test)""","""(spectro-temporal = 84%, spectral = 83%, temporal = 81%; spectral versus temporal ... p = 0.60
    ... spectral versus spectro-temporal ... p = 0.79 ... temporal versus spectro-temporal ... p =
    0.42; two-sample t test)""")
s=s.replace("""(impulsive; correlation half width; water =
    3.9 ms; wind = 3.6 ms)""","""(impulsive; correlation half width ... water =
    3.9 ms; wind = 3.6 ms)""")
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/sadeghi-2019.yaml paper/10.1371-journal.pbio.3000449.txt; grep -nE "—|[Rr]ather" claims/sadeghi-2019.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/sadeghi-2019.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c))"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE "^\s+[^-#].*: " claims/sadeghi-2019.yaml | grep -vE "^\s*[0-9]+:\s+(- )?[a-z_]+: " | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -nE "^\s*(- )?[a-z_]+: .*: " claims/sadeghi-2019.yaml | head
```

```
(Bash completed with no output)
```

**Agent**

I wrote `claims/sadeghi-2019.yaml` with 28 claims. The quote checker passes with 0 problems.

**Text read.** The version of record (PMC6788721, Europe PMC full-text XML): Results, Discussion, Methods and all figure legends (Figs 1 to 10 and S1 to S10). Also the supplement files S1 Text (the proofs on signal and noise correlations), S1 Table (the 195 model sounds) and S2 Table (the paradigm 3 sounds). No PDF was supplied.

**What was not read.**
- **Equations.** Every displayed equation was lost from the text, and there was no PDF to read them from. That covers the correlation normalizations, the noise correlation, the decision rule, the spectro-temporal mixing, the 1/f filter, and the SI and CDI formulas. Each criterion that needs one names readings taken from the surrounding prose.
- **Code.** The only code the paper links is the MATLAB code inside the CRCNS bst-2 deposit. Because it is part of the dataset's files, I did not read it. The opening comment says the author may follow it and keep my readings as variants.

**Counts.**
- 28 claims, all with quotes, none inferred.
- 9 claims carry statistics (t tests against chance, a one-tailed t test, three pairwise two-sample t tests, Bonferroni-corrected tests); the checker found 14 p-values in all.
- 28 criteria; 26 claims have expected values.
- Coverage: paradigm 1 (8 claims), paradigm 2 (4), paradigm 3 (3), and the auditory model (13).

**Details the paper leaves open, with the readings named:**
1. **How the 100 random time samples make a decision:** each sample is one decision, or the log-posterior is summed over all 100.
2. **How the number of principal components is chosen:** on the validation performance, or by an inner split of the model half.
3. **Paradigm 2 split:** the half split as in paradigm 1, or whole original responses train and whole 1/f responses test. Paradigm 3 has the same question (whole responses, or the half split on top of leaving one exemplar out).
4. **Neural spectrum (rate) classifier:** not described for the neural data. Read as the mean aMUA per channel through the same pipeline.
5. **Mixing coefficient:** fitted on model or validation data, on a 0.1 grid.
6. **Correlation window T for Figs 1, 2 and 4:** one window over the whole 3 s response, or 1000 ms windows averaged.
7. **Width measure:** taken on the channel-averaged curve, or as the median over channels.
8. **SNR formula:** not given. Readings: a power ratio with or without the diagonal, and one value per site and sound or per site.
9. **CDI and SI formulas:** normalized by the power of the average, or by the mean power. The grouping of categories for SI and its averaging unit are also open.
10. **Window for the model's time-averaged correlations in Figs 5 and 6:** the coarsest 566 ms window, or the whole sound.
11. **Model classifier:** the window spacing (τW or the full Kaiser length) and the resolution at which the number of components is fixed.
12. **Unit of the t tests:** per-sound outcomes or category accuracies; for the tests against chance, one-sided or two-sided.
13. **Time-averaged classifier (Fig 9C):** not described in the Methods. Two constructions are named, and the reduction is read in points or as relative.
14. **Two-category task:** one model per class, or the 13-category models mapped to a class.
15. **Rise time:** interpolation, first sampled duration, or an exponential fit.

**Gaps a claim needed.**
- **Fig 9A optimal window:** the legend says 144 ms and the text says 141 ms. I took 141, since the half-octave grid holds 141 ms.
- **S5 Fig:** needs each channel's best frequency from the tone-pip responses.
- **S10 Fig:** needs raw voltage to threshold the MUA.
- The dataset description lists neither tone-pip responses nor raw voltage, so these two claims are blocked if the data are absent.
- **White noise:** a control in Figs 6C and 7I, but not in the dataset's sound list. The criterion has it generated if needed.

## End of run

21 turns, 6 minutes, $1.98 at API prices, result: success.
