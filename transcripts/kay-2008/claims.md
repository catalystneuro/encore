# kay-2008 · claims · run 42839821635

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls -la paper/
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

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml; cat paper/vim-1.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/kay-2008.yaml 2>/dev/null; grep -l "archive: crcns" claims/*.yaml | head -3; grep -n -i crcns docs/archives.md | head -20
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1038/nature06713
title: Identifying natural images from human brain activity
datasets:
- archive: crcns
  id: vim-1
  relation: primary
claims/bruno-2017.yaml
claims/deweese-2004.yaml
claims/eyherabide-2008.yaml
33:## CRCNS
35:- **Datasets.** A CRCNS data set, identified by its short name (`ret-1`,
37:  `targets/crcns.json`, written by hand; for now it holds one data set, to test
39:- **Versions.** CRCNS data sets are not versioned. Record the version as
43:- **Reading.** The files are in the public S3 bucket `crcnsarchive` (region
45:  `https://crcnsarchive.s3-us-west-2.amazonaws.com/<id>/<file>`; list a data
47:  crcns.org asks for a login to download; the bucket does not. Most data sets
57:- **In an entry.** The entry names the data set as `crcns:<id>/unversioned`
266:`tools/archives/crcns.py` for the simplest). Nothing else lists the archives:
```

**Agent calls Bash**

```bash
head -40 claims/bruno-2017.yaml; tail -30 claims/bruno-2017.yaml
```

```
# Claims for Bruno, Frost & Humphries (2017), eLife 6:e27342, "A spiral attractor network drives
# rhythmic locomotion", doi:10.7554/elife.27342, on CRCNS data set apl-1 (doi:10.6080/K0SN074B).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record (PMC5546814, open access), as JATS XML flattened to text under
# paper/: main text, Materials and methods, and the legends of Figures 1 to 8 and of all twelve
# figure supplements. The paper has no other supplementary file. No PDF of the paper was supplied,
# and none was needed: no claim rests on a number shown only in a figure. The extraction garbles
# some formulas: the Gaussian width reads "σ = {median ISI in population}/12" (a square root may be
# lost) and the rotation period reads "ω = 2πbΔt"; the code settles the second (see below).
# The data set's description (paper/apl-1.data-description.txt) was read only to know what it
# holds; no claim comes from it.
#
# Code read: https://github.com/mdhumphries/AplysiaAttractorAnalysis, commit e5f28e98 (2018-07-11),
# MATLAB, linked from the paper's Data and code availability. Analysis/DataSet_Properties.m builds
# the spike-density functions and the PCA; Analysis/Classify_attractors/ holds the recurrence
# analysis (Analyse_by_Recurrence_Points.m, LocalLinearDynamics.m, recurrence_point_results_Viz.m),
# manifold comparisons (Are_sequential_attractors_the_same.m and _CommonAxes.m,
# Initial_Conditions.m), perturbations (Are_jumps_perturbations_or_transitions2.m), period change
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 40,80p claims/bruno-2017.yaml
```

```
# eigenvalue.
#
# Places where the code and the Methods differ, each named again in the claims it touches:
# (1) the Gaussian SD: the Methods give the median ISI divided by 12 (or its square root, if the
# extraction lost it); the code uses the median ISI itself, and computes it from the post-onset
# ISIs of all recordings of the same stimulation number read so far, not of the recording alone;
# (2) the number of PCs: the Methods say at least 80% of variance; the recurrence code keeps the
# PCs whose cumulative variance is at most 80% (sum(prctVar <= 0.8)), the manifold code the
# smallest number reaching at least 80%; (3) the dominant period: the Methods and Figure 2F say
# the mean recurrence time of the dominant peak, the code stores and plots the median;
# (4) P10 decoding: the Methods fit 40 s windows stepped by 1 s with histories 50 to 200 ms; the
# code trains on 50% of the post-33 s series, steps 0.2 s, and tries histories 50 to 250 ms;
# (5) the period-change permutation test: 10000 permutations in the Methods, 100000 in the code,
# which permutes the pooled time and period values and is one-sided in the direction of rho.
# Following the protocol, the Methods are the main reading and the code's choice is a variant.
#
# Data the paper used. Aplysia californica, isolated cerebral, pleural and pedal ganglia (15 to
# 17 C). Voltage-sensitive dye RH-155 imaged with a 464-element photodiode array at 1600 Hz over
# the dorsal pedal ganglion, bandpassed 5 to 100 Hz and spike-sorted by independent component
# analysis. 10 preparations, three evoked bouts of fictive locomotion each (30 evoked population
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature06713.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature06713.txt",
 "offset": 1065,
 "limit": 1070
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, Methods and the supplement are all present, and the paper links no code. Next I'll look at the figure pages whose numbers the text garbles (Fig. 4, Supplementary Figs 4, 5 and 8).

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature06713.pdf",
 "pages": "3"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "import fitz; print(fitz.__doc__)" && python - <<'EOF'
import fitz, os
t=os.environ.get("TMPDIR","/tmp/claude")
d=fitz.open("paper/10.1038-nature06713.pdf"); d[2].get_pixmap(dpi=130).save(f"{t}/p3.png")
s=fitz.open("paper/10.1038-nature06713.supp.pdf")
for i in (4,5,8): s[i].get_pixmap(dpi=110).save(f"{t}/s{i+1}.png")
print(t)
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
which mutool gs pdftocairo convert qpdf 2>&1; python -c "import pypdfium2" 2>&1; python -c "import pypdf" 2>&1; ls .venv 2>/dev/null; uv --version 2>&1
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
uv 0.13.7 (x86_64-unknown-linux-gnu)
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv run --quiet --with pymupdf python - <<'EOF'
import fitz, os
t=os.environ["TMPDIR"]; r="paper/"
d=fitz.open(r+"10.1038-nature06713.pdf"); d[2].get_pixmap(dpi=130).save(f"{t}/p3.png")
s=fitz.open(r+"10.1038-nature06713.supp.pdf")
for i in (4,5,8): s[i].get_pixmap(dpi=110).save(f"{t}/s{i+1}.png")
print(t)
EOF
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
 "file_path": "/tmp/claude-1001/s9.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s5.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s6.png"
}
```

Result: no output.

**Agent**

Paper and supplement are complete; figure values read from Fig. 4 and Supplementary Figs 4, 5 and 8. Now checking the claims schema before writing.

**Agent calls Bash**

```bash
sed -n 1,200p tools/claims_check.py | head -150; ls tools/ schemas 2>/dev/null
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

[... 135 more lines not kept]
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
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:])"; head -40 claims/deweese-2004.yaml
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
[... 173 more lines not kept]
```

**Agent**

I have what I need. Writing the claims file now: 22 findings, with the shared identification method and its open details set out once in the opening comment.

**Agent calls Write**

```json
{
 "file_path": "claims/kay-2008.yaml",
 "content": "# Claims for Kay, Naselaris, Prenger & Gallant (2008), Nature 452:352-355, \"Identifying natural\n# images from human brain activity\", doi:10.1038/nature06713, on CRCNS data set vim-1.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record with its supplement, as PyMuPDF text under paper/\n# (10.1038-nature06713.txt): the Letter, its Methods, and the Supplementary Information\n# (Supplementary Figures 1 to 11, Supplementary Table 1, Supplementary Discussion 1 to 3,\n# Supplementary Methods 1 to 11). PDF pages were rendered only for Figure 4 and Supplementary\n# Figures 4, 5 and 8, whose numbers the text garbles. The data set's description\n# (paper/vim-1.data-description.txt) was read only to know what it holds; no claim comes from it.\n#\n# Code: the paper links no analysis code, so none was read. It names outside code for two steps:\n# m-sequence generation by T. Liu (stimulus design only) and Gaussian kernel density estimation by\n# A. Ihler (http://ttic.uchicago.edu/~ihler/code/), used for the set-size extrapolation.\n#\n# Data the paper used. Two subjects, S1 (author T.N., 33) and S2 (author K.N.K., 25). 4 T Varian\n# INOVA scanner, 18 coronal slices over occipital cortex, 64 x 64 matrix, TR 1 s, nominal 2 x 2 x\n# 2.5 mm. Stimuli are 20 x 20 degree greyscale natural photographs (500 x 500 px, circular mask),\n# each trial 4 s, an image flashed ON-OFF-ON-OFF-ON (200 ms each) for 1 s then 3 s grey. Five scan\n# sessions per subject; each has five model estimation runs (70 distinct images shown twice, 168\n# trials) and two image identification runs (12 distinct images shown 13 times, an m-sequence of\n# 168 trials with 12 null trials, the first 6 trials repeated at the end). In all, 1,750 model\n# estimation images and 120 identification images per subject. Responses are estimated per voxel\n# by the basis-restricted separable (BRS) model (Supplementary Methods 3 and 4): one amplitude per\n# distinct image (repeated-trial analysis; the first 6 trials of each identification run are left\n# out) or per trial (single-trial analysis; all trials, 1,620 identification trials per subject,\n# that is 10 runs x 162 image trials), standardized per session with the model estimation\n# responses' mean and SD. Voxels are assigned to V1, V2 and V3 from separate multifocal retinotopic\n# mapping sessions (Supplementary Methods 10 and 11); about 5,000 voxels lie in the stimulated\n# parts of V1 to V3 (Supplementary Table 1 gives 1331, 2208 and 1973 for S1, 1513, 1982 and 1780\n# for S2). S1 had three further sessions of identification runs only: two about two months later\n# (five runs each, 120 new images) and one about 14 months later (one run, 12 new images). The\n# set-size analyses use a library of 999 further images, randomly selected and distinct from the\n# 1,870 above, that the paper does not deposit or name a source for. The data set, by its\n# description, holds the two subjects' five main sessions as time series and as estimated\n# responses to the 1,750 and 120 images, ROI labels (V1, V2, V3, V3A, V3B, V4, lateral occipital),\n# the stimuli and anatomy; it does not mention the later S1 sessions, the retinotopic mapping\n# data or the 999-image library. Whether it holds what each claim needs is the author's to find.\n#\n# The identification method, used by most claims below (\"the pipeline\"), from the paper:\n# (P1) Receptive-field model, Gabor wavelet pyramid (GWP), Supplementary Methods 5 and 6 and\n# Supplementary Figures 2 and 3. Stimuli downsampled to min(500, round(2^(9 - x/8))) px for x = 0\n# to 24 (the extracted text garbles the formula; this reading gives the two printed examples,\n# 500 px at x = 0 and 215 px at x = 10), converted to luminance and mean-subtracted. Wavelets at\n# 1, 2, 4, 8, 16 (and 32 at 128 px) cycles per field of view, on an f x f grid, 8 orientations\n# (0 to 157.5 degrees), 2 quadrature phases, isotropic Gaussian masks with 1-octave spatial\n# frequency and 41-degree orientation bandwidth, masks zeroed below 0.01 of peak, each wavelet\n# zero-mean and unit-length, plus one luminance-only wavelet over the image (its projection\n# squared, times 2, square-rooted). Projection zeroed for a wavelet whose mask lies more than half\n# beyond 90% of the stimulus radius. Input channels are quadrature contrast energies (square root\n# of summed squared projections); prediction is a weighted sum plus a DC offset.\n# (P2) Fitting (Supplementary Methods 6). Gradient descent with early stopping: 20% of responses\n# drawn at random as a stopping set, responses mean-subtracted, channels z-scored, kernel from\n# zero, step 0.001, normalized gradient with momentum 0.9, stop when stopping-set (or training)\n# squared error no longer decreases. 100 bootstrap samples with the iteration count fixed to that\n# of the fit on the original data; final parameters are the bootstrap mean.\n# (P3) Three steps (Supplementary Methods 5). Initial models at 128 px over the central 20, 10.1\n# and 5.2 degrees, orientation invariant (channels summed over orientation; 1,367 parameters);\n# an isotropic 2-D Gaussian fit to each spatial envelope, RF location = the region within +/-2 SD\n# (valid for the 10.1 and 5.2 degree models only if wholly inside their field of view); the valid\n# initial model with least stopping-set error is the best initial model; only voxels whose best\n# initial model has significant predictive power go on; a final 64 px model, not orientation\n# invariant (2,730 parameters), fitted over the estimated RF location.\n# (P4) Predictive power is Pearson r between measured and predicted responses to the 120\n# identification images; its significance is one-tailed (r > 0) by a bootstrap (Supplementary\n# Methods 6), p < 0.01 where a threshold is used (Supplementary Table 1).\n# (P5) Identification (main text and Supplementary Methods 7). For each measured pattern, the 500\n# voxels with highest predictive power, computed without the image to be identified (so over the\n# other 119 images); the image whose predicted pattern has the highest Pearson r with the\n# measured pattern is chosen. Set size 120; chance 1/120.\n# (P6) Larger sets (Supplementary Methods 7). With a 999-image library, f(m,s) = product over\n# i = 1 to s - 1 of (1000 - g(m) - i) / (1000 - i), g(m) the number of library images whose\n# predicted pattern correlates more with m than the correct image's does (the garbled formula\n# read as drawing s - 1 images without replacement); beyond 1,000, the 999 correlations are\n# smoothed by a Gaussian kernel with width by pseudo-likelihood cross-validation and\n# f(m,s) = (1 - h(m))^(s - 1), h(m) the fraction of the smoothed distribution above the correct\n# image's correlation; f is averaged over all measured patterns.\n#\n# Details the paper leaves open, named again where a claim rests on them:\n# (O1) the candidate voxels. The paper uses V1, V2 and V3 only, and only voxels whose best initial\n# model has significant predictive power (P3). The threshold for that step is not stated in\n# Supplementary Methods 5; Supplementary Table 1 uses p < 0.01. Readings are (a) V1 to V3 voxels\n# passing p < 0.01, (b) all V1 to V3 voxels, ranked by predictive power alone.\n# (O2) the bootstrap for the significance of predictive power: what is resampled and how often is\n# not stated. Standard choice, resampling the 120 image pairs with replacement, 1,000 times; it\n# changes only which voxels pass a threshold near p = 0.01.\n# (O3) wavelet grid placement and the exact mask SD in pixels are fixed by the bandwidths only up\n# to convention; standard choice, centres at the cell centres of the f x f grid.\n# (O4) the goggles' luminance response is not given (only 0.8, 11.1 and 6.3 cd/m2 minimum,\n# maximum and mean); reading, the stimulus values taken as linear in luminance.\n# (O5) the final model's field of view, \"specifically tailored to the estimated RF location\".\n# Readings are (a) the square bounded by +/-2 SD of the fitted Gaussian, at 64 px, (b) the best\n# initial model's field of view, at 64 px.\n# (O6) single-trial identification. The paper does not say whether models and voxel selection for\n# single trials use the repeated-trial model estimation responses. Readings are (a) models and\n# predictive power from the repeated-trial responses, with single-trial patterns as the measured\n# patterns, (b) models fitted to single-trial model estimation responses.\n# (O7) random seeds (stopping sets, bootstraps, library draws) are standard choices.\nschema_version: 2\npaper: doi:10.1038/nature06713\nclaims:\n- id: fig3-s1-repeated-120\n  statement: For subject S1, the image seen was identified correctly for 92% (110 of 120) of the\n    repeated-trial voxel activity patterns from 120 novel natural images, against chance of 0.8%.\n  source: Main text, paragraph 6 (\"Identification performance for one subject is illustrated in\n    Fig. 3\"); Figure 3 and its legend; Figure 4a\n  quote: For this subject, 92% (110/120) of the images were identified correctly (subject S1),\n    whereas chance performance is just 0.8% (1/120)\n  expected:\n  - quantity: S1 repeated-trial identification performance, set size 120\n    value: 92\n    tolerance: 9.2\n    unit: percent correct\n  criterion: The pipeline of the opening comment (P1 to P5) on S1's 1,750 model estimation and 120\n    identification repeated-trial responses. The value must hold under one of the readings of O1\n    and O5; every combination is shown.\n- id: fig4a-s2-repeated-120\n  statement: For subject S2, 72% (86 of 120) of the images were identified correctly from\n    repeated-trial patterns.\n  source: Main text, paragraph 6; Figure 4a\n  quote: For a second subject, 72% (86/120) of the images were identified correctly (subject S2)\n  expected:\n  - quantity: S2 repeated-trial identification performance, set size 120\n    value: 72\n    tolerance: 7.2\n    unit: percent correct\n  criterion: As fig3-s1-repeated-120, for S2.\n- id: fig4a-single-trial\n  statement: Identification from single-trial voxel activity patterns was 51% (834 of 1,620) for S1\n    and 32% (516 of 1,620) for S2, against chance of 0.8%.\n  source: Main text, paragraph 7; Figure 4a\n  quote: Single-trial performance was 51% (834/1620) and 32% (516/1620) for subjects S1 and S2,\n    respectively (Fig. 4a); once again, chance performance is just 0.8% (13.5/1620)\n  expected:\n  - quantity: S1 single-trial identification performance, set size 120\n    value: 51\n    tolerance: 5.1\n    unit: percent correct\n  - quantity: S2 single-trial identification performance, set size 120\n    value: 32\n    tolerance: 3.2\n    unit: percent correct\n  criterion: Single-trial responses are BRS amplitudes per trial with the HRF from the\n    repeated-trial analysis, all trials of the identification runs used, standardized per session\n    (Supplementary Methods 1, 3 and 4), giving 1,620 patterns per subject; each is identified among\n    the 120 images by P5. The models and voxel selection follow O6, readings (a) and (b); the\n    value must hold under one reading, with O1 and O5 as in fig3-s1-repeated-120.\n- id: fig4a-noise-ceiling\n  statement: The estimated noise ceilings show that the lower performance of S2 is due to\n    intrinsically noisier data; the ceilings are near 98% for both subjects with repeated trials,\n    and about 80% (S1) and 62% (S2) with single trials.\n  source: Figure 4a and its legend; Supplementary Methods 7, Estimation of the noise ceiling\n  quote: The noise ceiling estimates suggest that the difference in performance across subjects is\n    due to intrinsic differences in the level of noise\n  expected:\n  - quantity: S1 repeated-trial noise ceiling, read from the Figure 4a marker\n    value: 98\n    tolerance: 9.8\n    unit: percent correct\n  - quantity: S2 repeated-trial noise ceiling, read from the Figure 4a marker\n    value: 98\n    tolerance: 9.8\n    unit: percent correct\n  - quantity: S1 single-trial noise ceiling, read from the Figure 4a marker\n    value: 80\n    tolerance: 8\n    unit: percent correct\n  - quantity: S2 single-trial noise ceiling, read from the Figure 4a marker\n    value: 62\n    tolerance: 6.2\n    unit: percent correct\n  criterion: Noise ceiling as Supplementary Methods 7 gives it. For each of the 120 images, 25\n    simulations; in each, the measured pattern is the mean of a random sample of the correct\n    image's single-trial patterns, each candidate's predicted pattern the mean of a random sample\n    of its own single-trial patterns, and the most correlated candidate is chosen; the ceiling is\n    the percentage of successes. The values are read from the figure, no sentence gives them.\n    Open are the voxels and the sample size. Voxels, the 500 selected for identification (P5).\n    Sample size, readings (a) a bootstrap sample with replacement of the size of the available\n    trials (13) for the repeated-trial ceiling and of size 1 for the single-trial ceiling, (b)\n    without replacement, same sizes. Reproduced when, under one reading, the four values are within\n    tolerance and the ceilings differ less between subjects than the empirical performance does\n    relative to its ceiling, that is S2's single-trial ceiling is below S1's.\n  depends_on:\n  - fig4a-single-trial\n- id: fig4b-set-size-1000\n  statement: For S1 with repeated trials, performance declined only from 92% to 82% as the set size\n    rose from 100 to 1,000 images.\n  source: Main text, paragraph 8; Figure 4b; Supplementary Methods 7, Identification performance\n    for different set sizes\n  quote: As set size increased tenfold from 100 to 1,000, performance only declined slightly, from\n    92% to 82% (subject S1, ... repeated trial)\n  data: with_inputs\n  expected:\n  - quantity: S1 repeated-trial performance, set size 100\n    value: 92\n    tolerance: 9.2\n    unit: percent correct\n  - quantity: S1 repeated-trial performance, set size 1,000\n    value: 82\n    tolerance: 8.2\n    unit: percent correct\n  criterion: P6 with the paper's 999-image library, the predicted patterns for the library images\n    coming from the S1 models of fig3-s1-repeated-120. The library images are not deposited and no\n    source is given beyond the image collections of the Methods; without them the claim cannot be\n    tested as the paper did it.\n  depends_on:\n  - fig3-s1-repeated-120\n- id: fig4b-extrapolation\n  statement: Extrapolated, performance falls to 10% at set sizes of 10^11.3 (S1, repeated trial),\n    10^7.3 (S2, repeated), 10^5.5 (S1, single trial) and 10^3.5 (S2, single).\n  source: Figure 4b; main text, paragraph 8; Supplementary Methods 7, extrapolation\n  quote: Extrapolation of these measurements (see Supplementary Methods) suggests that performance\n    for this subject would remain above 10% even up to a set size of 1011.3 images\n  data: with_inputs\n  expected:\n  - quantity: log10 set size at 10% performance, S1 repeated trial\n    value: 11.3\n    tolerance: 1.13\n  - quantity: log10 set size at 10% performance, S2 repeated trial (Figure 4b)\n    value: 7.3\n    tolerance: 0.73\n  - quantity: log10 set size at 10% performance, S1 single trial (Figure 4b)\n    value: 5.5\n    tolerance: 0.55\n  - quantity: log10 set size at 10% performance, S2 single trial (Figure 4b)\n    value: 3.5\n    tolerance: 0.35\n  criterion: The extrapolation of P6 over the 999 library images, the set size at which the mean of\n    f(m,s) over patterns reaches 0.1. Tolerances are 10% of the printed exponent. Needs the library\n    of fig4b-set-size-1000.\n  depends_on:\n  - fig4b-set-size-1000\n  - fig4a-single-trial\n- id: fig4c-retinotopy-only-extrapolation\n  statement: A retinotopy-only model, capturing only the location and size of each voxel's receptive\n    field, falls to 10% correct at a set size of 10^5.1 images, against 10^9.5 for the Gabor wavelet\n    pyramid model (repeated trials, averaged across subjects); it is worse for each subject, with\n    single trials too.\n  source: Main text, paragraph 9; Figure 4c; Supplementary Figure 5a to 5d\n  quote: Performance for this retinotopy-only model declined to 10% correct at a set size of just\n    105.1 images, whereas performance for the Gabor wavelet pyramid model did not decline to 10%\n    correct until 109.5 images were included in the set\n  data: with_inputs\n  expected:\n  - quantity: log10 set size at 10% performance, retinotopy-only, repeated trial, subject average\n    value: 5.1\n    tolerance: 0.51\n  - quantity: log10 set size at 10% performance, GWP, repeated trial, subject average\n    value: 9.5\n    tolerance: 0.95\n  criterion: Retinotopy-only model as Supplementary Methods 8 gives it, two channels, the absolute\n    spatially-weighted luminance and the spatially-weighted contrast with weights from the Gaussian\n    fitted to the best initial model's envelope, at the original resolution, fitted by the gradient\n    descent of P2; voxels selected by its own predictive power (Supplementary Methods 7). How the\n    subjects are averaged is open. Readings are (a) the mean of the two subjects' performance curves,\n    then the set size at 10%, (b) the mean of the two exponents; Supplementary Figure 5 gives 11.3\n    and 7.3 for the GWP model and 7.0 and 3.8 for the retinotopy-only model, whose means (9.3, 5.4)\n    are not the printed 9.5 and 5.1, so (a) is the better supported. Reproduced when, under one\n    reading, both values are within tolerance and the retinotopy-only exponent is below the GWP\n    exponent for each subject and for repeated and single trials (Supplementary Figure 5 gives\n    3.7 against 5.5, S1, and 2.5 against 3.5, S2, single trial). Needs the library of\n    fig4b-set-size-1000.\n  depends_on:\n  - fig4b-extrapolation\n- id: suppm8-retinotopy-only-120\n  statement: At set size 120 with repeated trials, averaged across subjects, the retinotopy-only\n    model identified 55% of images with spatially-weighted luminance and contrast and 42% with the\n    standard (unweighted) metrics, both below the Gabor wavelet pyramid model.\n  source: Supplementary Methods 8, Validation of the spatially-weighted metrics; Figure 4c\n  quote: Identification performance was 55% and 42% for the spatiallyweighted metrics and standard\n    metrics, respectively (repeated trial, 120 images, performance averaged across subjects)\n  expected:\n  - quantity: retinotopy-only performance, spatially-weighted metrics, mean of S1 and S2\n    value: 55\n    tolerance: 5.5\n    unit: percent correct\n  - quantity: retinotopy-only performance, standard metrics, mean of S1 and S2\n    value: 42\n    tolerance: 4.2\n    unit: percent correct\n  criterion: The retinotopy-only model of fig4c-retinotopy-only-extrapolation, identification by P5\n    at set size 120 on each subject, the two subjects' percentages averaged. Standard metrics are\n    the mean and SD of pixel luminance within +/-2 SD of the Gaussian G (Supplementary Methods 8).\n    Reproduced when both values are within tolerance and both are below the GWP mean of\n    fig3-s1-repeated-120 and fig4a-s2-repeated-120 computed here.\n  depends_on:\n  - fig3-s1-repeated-120\n  - fig4a-s2-repeated-120\n- id: suppfig8-constrained-models\n  statement: In constrained versions of the GWP model, both orientation and spatial frequency tuning\n    add to identification (C > A, G > A), spatial frequency more (G > C), and voxel-to-voxel variation\n    in both adds too (F > E, H > E); at 1,000 images the nine models give A 17%, B 22%, C 28%, D 30%,\n    E 51%, F 60%, G 64%, H 62% and I 63%.\n  source: Supplementary Figure 8a and 8b; main text, paragraph 10; Supplementary Methods 9\n  quote: Both orientation and spatial frequency tuning contribute to identification performance\n    (C > A and G > A), but spatial frequency tuning is relatively more important (G > C).\n    Voxel-to-voxel variation in orientation and spatial frequency tuning also contributes to\n    identification performance (F > E and H > E)\n  statistics:\n  - about: C > A, G > A, G > C, F > E and H > E\n    test: one-tailed paired sign test\n    p: 0.05\n    p_relation: \"<\"\n    n: repeated-trial patterns of both subjects, 1,000 images\n  data: with_inputs\n  expected:\n  - quantity: model A (flat orientation, flat spatial frequency)\n    value: 17\n    tolerance: 1.7\n    unit: percent correct\n  - quantity: model C (individual orientation, flat spatial frequency)\n    value: 28\n    tolerance: 2.8\n    unit: percent correct\n  - quantity: model E (ROI-averaged both)\n    value: 51\n    tolerance: 5.1\n    unit: percent correct\n  - quantity: model F (individual orientation, ROI-averaged spatial frequency)\n    value: 60\n    tolerance: 6\n    unit: percent correct\n  - quantity: model G (flat orientation, individual spatial frequency)\n    value: 64\n    tolerance: 6.4\n    unit: percent correct\n  - quantity: model H (ROI-averaged orientation, individual spatial frequency)\n    value: 62\n    tolerance: 6.2\n    unit: percent correct\n  criterion: The nine models of Supplementary Methods 9 at 64 px, the spatial envelope fixed by the\n    Gaussian of the RF location, channels summed over position, transformed by the 640-grating\n    least-squares map and summed over phase, then flat, ROI-averaged (mean tuning across the voxels\n    of the same area) or individual tuning on each dimension, fitted by P2 over one fixed voxel set\n    selected by the unconstrained model I (Supplementary Methods 7). Performance at 1,000 images by\n    P6, averaged across subjects. The figure's p-values (C over A 8e-6, G over A 2e-22, G over C\n    2e-16, F over E 4e-4, H over E 4e-5) are read from the low-resolution table of panel b; the\n    legend states only that all five are below 0.05. Which unit the sign test pairs (each measured\n    pattern's f(m,1000), pooled over subjects) is a reading, the one the legend's \"paired\" allows.\n    Reproduced when the five orderings hold with one-tailed sign-test p < 0.05 and at least four of\n    the six values are within tolerance. Needs the library of fig4b-set-size-1000; the orderings at\n    set size 120 can be shown as a variant, which does not decide the outcome.\n  depends_on:\n  - fig4b-set-size-1000\n- id: time-two-months\n  statement: For 120 novel images seen about two months after the main experiment, 82% (99 of 120)\n    were identified correctly (S1, repeated trials), using the models from the main experiment.\n  source: Main text, paragraph 11; Methods, Data collection, paragraph 3\n  quote: In this case 82% (99/120) of the images were identified correctly (chance performance 0.8%;\n    subject S1, repeated trial)\n  expected:\n  - quantity: S1 repeated-trial performance, sessions two months later, set size 120\n    value: 82\n    tolerance: 8.2\n    unit: percent correct\n  criterion: The S1 models of fig3-s1-repeated-120, applied to the identification responses of the\n    two later sessions, estimated by the BRS model and standardized within each session\n    (Supplementary Methods 3, Analysis for additional scan sessions); P5 on the 120 images. Needs\n    those sessions, which the data set's description does not mention.\n  depends_on:\n  - fig3-s1-repeated-120\n- id: time-fourteen-months\n  statement: For 12 novel images seen more than a year (about 14 months) after the main experiment,\n    all 12 were identified correctly (S1, repeated trials; chance 8%).\n  source: Main text, paragraph 11; Methods, Data collection, paragraph 3\n  quote: In this case 100% (12/12) of the images were identified correctly (chance performance 8%;\n    subject S1, repeated trial)\n  expected:\n  - quantity: S1 repeated-trial performance, session 14 months later, set size 12\n    value: 100\n    tolerance: 10\n    unit: percent correct\n  criterion: As time-two-months, for the single-run session about 14 months later, set size 12. A\n    tolerance of 10 points allows 11 of 12.\n  depends_on:\n  - fig3-s1-repeated-120\n- id: errors-similar-images\n  statement: Identification errors tended to occur when the selected image was visually similar to\n    the correct image.\n  source: Main text, paragraph 12\n  quote: Inspection revealed that identification errors tended to occur when the selected image was\n    visually similar to the correct image\n  criterion: The paper judged this by inspection and gives no measure. The two image similarity\n    measures the paper itself uses (Supplementary Discussion 1) are the readings, (a) correlation of\n    pixel luminance, (b) correlation of local RMS contrast in 0.6 degree blocks. For each error of\n    fig3-s1-repeated-120 and fig4a-s2-repeated-120, the percentile of the selected image's\n    similarity to the correct image among the correct image's similarities to the other 119 images.\n    The test is fixed here, not by the paper. Reproduced when, under one reading, the errors pooled\n    over subjects have a median percentile above 50 by a one-sided Wilcoxon signed-rank test against\n    50 at p < 0.05.\n  depends_on:\n  - fig3-s1-repeated-120\n  - fig4a-s2-repeated-120\n- id: suppfig4-500-voxels\n  statement: Identification performance rises with the number of voxels used and is best at about\n    500 voxels for both subjects, with repeated and single trials.\n  source: Supplementary Figure 4 and legend; Supplementary Methods 7, Voxel selection\n  quote: In all cases optimal performance was achieved using about 500 voxels\n  criterion: P5 at set size 120 with 1, 5, 10, 20, 50, 100, 200, 500 and 1,000 voxels (the figure's\n    axis), for S1 and S2, repeated and single trials. \"About 500\" is not made exact by the paper;\n    the rule here is that, in each of the four conditions, performance at 500 voxels is the highest\n    of the nine or within 3 percentage points of the highest, and performance at 500 is above that\n    at 50. Partially reproduced when this holds in two or three conditions.\n  depends_on:\n  - fig3-s1-repeated-120\n  - fig4a-s2-repeated-120\n  - fig4a-single-trial\n- id: supptable1-voxel-counts\n  statement: The visual areas hold 1331 (V1), 2208 (V2) and 1973 (V3) voxels in S1, and 1513, 1982 and\n    1780 in S2.\n  source: Supplementary Table 1, column Total number of voxels\n  inferred: Numbers from Supplementary Table 1; no sentence states them. Supplementary Methods 7\n    says about 5000 voxels lay in the stimulated parts of V1 to V3.\n  expected:\n  - quantity: S1 V1 voxels\n    value: 1331\n    tolerance: 133.1\n  - quantity: S1 V2 voxels\n    value: 2208\n    tolerance: 220.8\n  - quantity: S1 V3 voxels\n    value: 1973\n    tolerance: 197.3\n  - quantity: S2 V1 voxels\n    value: 1513\n    tolerance: 151.3\n  - quantity: S2 V2 voxels\n    value: 1982\n    tolerance: 198.2\n  - quantity: S2 V3 voxels\n    value: 1780\n    tolerance: 178\n  criterion: Counts of voxels assigned to each area by the retinotopic mapping (Supplementary\n    Methods 10). Reproduced when all six counts are within tolerance; partially when four or five are.\n- id: supptable1-predictive-power-by-area\n  statement: The fraction of voxels whose best initial model has significant predictive power falls\n    from V1 to V2 to V3 (S1 40%, 31%, 17%; S2 25%, 21%, 13%).\n  source: Supplementary Table 1 and legend, column High predictive power\n  quote: Predictive power generally decreased from V1 to V2 to V3, likely reflecting the fact that the\n    Gabor wavelet pyramid model is not optimal for visual areas beyond V1\n  expected:\n  - quantity: S1 V1 fraction with significant predictive power\n    value: 40\n    tolerance: 4\n    unit: percent of voxels\n  - quantity: S1 V2 fraction\n    value: 31\n    tolerance: 3.1\n    unit: percent of voxels\n  - quantity: S1 V3 fraction\n    value: 17\n    tolerance: 1.7\n    unit: percent of voxels\n  - quantity: S2 V1 fraction\n    value: 25\n    tolerance: 2.5\n    unit: percent of voxels\n  - quantity: S2 V2 fraction\n    value: 21\n    tolerance: 2.1\n    unit: percent of voxels\n  - quantity: S2 V3 fraction\n    value: 13\n    tolerance: 1.3\n    unit: percent of voxels\n  criterion: Predictive power of the best initial model (P3, P4), significant at p < 0.01 by the\n    bootstrap (O2), as a percentage of each area's voxels. Reproduced when the order V1 > V2 > V3\n    holds in both subjects and at least four of the six values are within tolerance; partially when\n    the order holds in both subjects only.\n- id: supptable1-snr\n  statement: SNR differs greatly between subjects but is similar across V1, V2 and V3 within a\n    subject; the fraction of voxels with SNR above 1.5 is 32%, 30% and 22% in S1 and 18%, 19% and 13%\n    in S2.\n  source: Supplementary Table 1 and legend, column High SNR\n  quote: Although SNR varied greatly across subjects, SNR was fairly consistent for areas V1, V2, and\n    V3 within each subject\n  expected:\n  - quantity: S1 V1 fraction with SNR above 1.5\n    value: 32\n    tolerance: 3.2\n    unit: percent of voxels\n  - quantity: S1 V2 fraction\n    value: 30\n    tolerance: 3\n    unit: percent of voxels\n  - quantity: S1 V3 fraction\n    value: 22\n    tolerance: 2.2\n    unit: percent of voxels\n  - quantity: S2 V1 fraction\n    value: 18\n    tolerance: 1.8\n    unit: percent of voxels\n  - quantity: S2 V2 fraction\n    value: 19\n    tolerance: 1.9\n    unit: percent of voxels\n  - quantity: S2 V3 fraction\n    value: 13\n    tolerance: 1.3\n    unit: percent of voxels\n  criterion: A voxel's SNR is the median, over its model estimation responses aggregated across\n    sessions, of the absolute response divided by its standard error, from the BRS fits\n    (Supplementary Methods 3). The paper does not say how the standard error of an amplitude is\n    obtained; readings are (a) the ordinary least-squares standard error from the final iteration\n    of the BRS fit after the autoregressive transform, (b) a bootstrap over runs. Reproduced when,\n    under one reading, at least four of the six values are within tolerance and each subject's\n    fraction is higher in S1 than in S2 for every area.\n- id: methods-v4-poor\n  statement: The GWP model characterizes the responses of voxels in V1, V2 and V3 but does poorly for\n    higher areas such as V4.\n  source: Methods, Model estimation, paragraph 1\n  quote: The model was able to characterize responses of voxels in visual areas V1, V2 and V3\n    (Supplementary Table 1), but it did a poor job of characterizing responses in higher visual\n    areas such as V4\n  criterion: The paper shows no V4 result. Measure from Supplementary Table 1, the percentage of\n    voxels whose best initial model has significant predictive power (p < 0.01, P3, P4, O2), for V4\n    voxels as labelled in the data set and for V1 to V3. Reproduced when, in both subjects, the V4\n    percentage is below the V3 percentage; the median predictive power per area is reported too.\n  depends_on:\n  - supptable1-predictive-power-by-area\n- id: fig2-representative-voxel\n  statement: A representative V1 voxel of S1 (voxel 42205) has its receptive field in the left\n    hemifield just below the horizontal meridian, broadband orientation tuning and high-pass spatial\n    frequency tuning.\n  source: Figure 2a and 2b and legend\n  quote: This receptive field is located in the left hemifield, just below the horizontal meridian\n    ... This receptive field has broadband orientation tuning and high-pass spatial frequency tuning\n  criterion: Final GWP model of that voxel (P1 to P3, O5), spatial envelope and grating tuning curves\n    as Supplementary Methods 6 (Calculation of tuning curves) gives them. How the paper numbers\n    voxels is not stated; whether 42205 is an index the data set keeps is the author's to find, and\n    if it is not, the claim cannot be tested. Reproduced when the envelope peak lies left of the\n    vertical meridian and below the horizontal meridian within the central half of the stimulus\n    height, the spatial frequency tuning is highest at the highest frequency (2.9 cycles per degree\n    on the figure's axis), and the orientation tuning's maximum is less than twice its minimum\n    (the ratio for \"broadband\" is fixed here).\n- id: suppfig7-roi-tuning\n  statement: The V1-averaged orientation tuning curve is nearly flat and the V1-averaged spatial\n    frequency tuning curve is band-pass; voxels have only a slight orientation bias.\n  source: Supplementary Figure 7a and 7b and legend; main text, paragraph 10\n  quote: The orientation tuning curve is nearly flat ... The spatial frequency tuning curve is\n    band-pass\n  criterion: The ROI-averaged tuning curves of Supplementary Methods 9, the mean over V1 voxels of\n    the grating tuning curves of the final GWP models, with bootstrap SE across voxels. Which V1\n    voxels are averaged is not stated; readings are (a) all V1 voxels with a final model, (b) the\n    fixed voxel set of suppfig8-constrained-models. Reproduced when, under one reading, the\n    orientation curve's range is under 10% of its mean (the bound for \"nearly flat\" is fixed here)\n    and the spatial frequency curve peaks at an intermediate frequency, above both its lowest and\n    highest frequency values by more than 2 SE.\n  depends_on:\n  - fig3-s1-repeated-120\n- id: suppfig10-retinotopy-validation\n  statement: Receptive-field angle and eccentricity estimated from the GWP model match those from\n    independent multifocal retinotopic mapping, with discrepancies in eccentricity at the lowest and\n    highest eccentricities.\n  source: Supplementary Figure 10a to 10c and legend\n  quote: Notice that the MF and GWP angle estimates are well matched ... The MF and GWP eccentricity\n    estimates are generally well matched, but there appear to be systematic discrepancies at the\n    lowest and highest eccentricities\n  criterion: GWP angle and eccentricity from the RF location of P3, voxels with predictive power\n    significant at p < 0.01 (as the legend says); multifocal estimates by the vector sum and centre\n    of mass of Supplementary Methods 11, from the separate mapping sessions, pooled across subjects.\n    The paper gives no statistic; the measures fixed here are the circular correlation of angles and\n    the Spearman correlation of eccentricities. Reproduced when both are positive with p < 0.05.\n    Needs the retinotopic mapping data, which the data set's description says are not included.\n- id: suppfig11-rf-size-eccentricity\n  statement: Receptive-field size increases with eccentricity, and from V1 to V2 to V3.\n  source: Supplementary Figure 11 and legend\n  quote: RF size increases with eccentricity and across visual areas, consistent with previous fMRI\n    studies\n  criterion: RF size is the extent of +/-2 SD of the Gaussian fitted to the best initial model's\n    envelope (P3); voxels kept when predictive power is significant at p < 0.01 and the RF lies\n    wholly inside the stimulus; pooled across subjects, binned by eccentricity, median per bin with\n    at least 10 voxels (the legend). The bin edges are not given; standard choice, 1 degree bins\n    from 0 to 10 degrees, with 0.5 degree bins as a variant. Reproduced when, for each area, the\n    Spearman correlation of RF size with eccentricity over voxels is positive at p < 0.05, and in\n    most bins shared by the three areas the medians order V1 < V2 < V3 (tests fixed here).\n- id: suppdisc1-classification-extension\n  statement: Extending classification to novel images (matching the measured pattern to the most\n    similar of the 1,750 training patterns, then picking the identification image most similar to\n    that training image) works poorly, 1.7% and 0.8% correct with pixel luminance similarity (not\n    above chance) and 5% and 5.8% with local contrast (above chance), for S1 and S2.\n  source: Supplementary Discussion 1, An extension of classification-based decoding methods yields\n    poor identification performance, paragraphs 2 and 3\n  quote: Identification performance using the pixel luminance metric was 1.7% (2/120) and 0.8% (1/120)\n    for subjects S1 and S2, respectively (repeated trial). These values were not significantly above\n    chance (p ≥ 0.05, one-tailed binomial test). Identification performance using the local contrast\n    metric was 5% (6/120) and 5.8% (7/120) for subjects S1 and S2, respectively (repeated trial).\n    These values were above chance (p < 0.0001, one-tailed binomial test)\n  statistics:\n  - about: pixel luminance metric, each subject against chance 1/120\n    test: one-tailed binomial test\n    p: 0.05\n    p_relation: \">\"\n    n: 120 repeated-trial patterns per subject\n  - about: local contrast metric, each subject against chance 1/120\n    test: one-tailed binomial test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 120 repeated-trial patterns per subject\n  expected:\n  - quantity: S1, pixel luminance metric\n    value: 1.7\n    tolerance: 0.17\n    unit: percent correct\n  - quantity: S2, pixel luminance metric\n    value: 0.8\n    tolerance: 0.08\n    unit: percent correct\n  - quantity: S1, local contrast metric\n    value: 5\n    tolerance: 0.5\n    unit: percent correct\n  - quantity: S2, local contrast metric\n    value: 5.8\n    tolerance: 0.58\n    unit: percent correct\n  criterion: As Supplementary Discussion 1 gives it. Pattern similarity by Pearson r; image\n    similarity by correlation of pixel luminance, or of local RMS contrast in 0.6 degree blocks\n    (n = 0.6, the best of the values the paper tried). Open are the voxels and the contrast measure.\n    Voxels, readings (a) the 500 voxels of P5, (b) all V1 to V3 voxels of O1. RMS contrast,\n    readings (a) the SD of luminance in the block, (b) that SD over the block mean. With 120 images\n    a tolerance of 10% is less than one image, so the counts are judged instead. Reproduced when,\n    under one reading, each count is within one image of the paper's (2, 1, 6, 7), the luminance\n    results are not above chance (one-tailed binomial p at or above 0.05) and the contrast results\n    are (p < 0.0001); partially when the significance pattern holds but a count is further off.\n    The paper wrote p ≥ 0.05, recorded here as p > 0.05.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/kay-2008.yaml paper/10.1038-nature06713.txt; grep -n -- "—\|rather" claims/kay-2008.yaml; grep -nP '^\s+[a-z_]+: .*[^"]: ' claims/kay-2008.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/kay-2008.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print(p, x[:80])
walk(d)
print(sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']))
EOF
```

```
2 22
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kay-2008.yaml",
 "old_string": "    tolerance and the ceilings differ less between subjects than the empirical performance does\n    relative to its ceiling, that is S2's single-trial ceiling is below S1's.",
 "new_string": "    tolerance and S2's single-trial ceiling is below S1's, as S2's performance is (the paper's\n    argument, read from the figure; no test is reported)."
}
```

```
The file claims/kay-2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/kay-2008.yaml paper/10.1038-nature06713.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I've written `claims/kay-2008.yaml`, and the quote checker passes it with no problems. Nothing is committed.

**Text read.** The version of record (Letter, Methods) with its full Supplementary Information: Supplementary Figures 1 to 11, Table 1, Discussion 1 to 3 and Methods 1 to 11. Nothing the claims needed was missing from the text. I rendered PDF pages only for Figure 4 and Supplementary Figures 4, 5 and 8, whose numbers the text garbles. The paper links no analysis code, so I read none. It names only Liu's m-sequence code and Ihler's kernel density estimation code.

**Claims.** There are 22 claims:
- 21 have quotes. The voxel counts of Supplementary Table 1 are marked `inferred`, as no sentence states them.
- 2 have statistics (3 values): the binomial tests of Supplementary Discussion 1, and the sign test of Supplementary Figure 8, recorded as p < 0.05.
- All 22 have criteria.

The claims cover:
- identification at set size 120: S1 92%, S2 72%; single trials 51% and 32%
- the noise ceilings
- set size up to 1,000 and the extrapolations to 10% performance
- the retinotopy-only model, at 120 images and extrapolated
- the nine constrained models
- the two later sessions (82% at two months, 100% at 14 months)
- errors falling on similar images
- the best voxel count (about 500)
- Supplementary Table 1: voxel counts, SNR, predictive power by area
- the poor fit in V4
- the example voxel of Figure 2
- the area-averaged tuning curves
- the check against retinotopic mapping
- receptive-field size against eccentricity
- the classification-extension control

**Details left open, with the readings named:**
- **O1, candidate voxels:** (a) V1 to V3 voxels whose first model is significant at p < 0.01, or (b) all V1 to V3 voxels.
- **O2, the significance bootstrap:** not described. Standard choice: resample the 120 images, 1,000 times.
- **O3, wavelet grid placement:** a standard convention.
- **O4, the goggles' luminance response:** not given. Pixel values are taken as linear in luminance.
- **O5, the final model's field of view:** (a) the ±2 SD square of the fitted Gaussian, or (b) the best first model's field of view.
- **O6, single trials:** models fitted to (a) the repeated-trial responses or (b) the single-trial responses.
- **Averaging across subjects (Fig. 4c):** (a) average the performance curves, or (b) average the exponents. (a) fits better, since averaging the per-subject exponents gives 9.3 and 5.4, not the printed 9.5 and 5.1.
- **Noise-ceiling sampling:** sampling with or without replacement.
- **SNR standard error:** least-squares or bootstrap.
- **Contrast in Supplementary Discussion 1:** RMS contrast as the SD, or the SD over the mean; and which voxels are used.
- **Which V1 voxels are averaged for the tuning curves:** two readings.
- **Image similarity for the errors claim:** pixel luminance or local contrast. Its test is set by me, and so are the bounds for "broadband", "nearly flat" and "about 500 voxels". Each criterion says so.

**Readings of garbled text.**
- **Formulas:** the stimulus resolution formula is read as min(500, round(2^(9 − x/8))), which reproduces both printed examples. The set-size formula is read as drawing images without replacement.
- **Figure values:** the noise ceilings and the Supplementary Figure 8 p-values were read from the figures. The p-values come from a low-resolution table and are only cited in the criterion.

**Missing data.** These are not missing from the paper, but some claims need data the paper never deposited:
- **The 999-image library:** the paper gives no source for it. Without it, the claims on set size, extrapolation, retinotopy-only extrapolation and constrained models cannot be tested as the paper did them (marked `with_inputs`).
- **S1's later sessions and the retinotopic mapping data:** the dataset's description does not list them.
- **Voxel 42205:** the paper does not say how its voxel numbers map onto the dataset's indexing.

## End of run

26 turns, 5 minutes, $1.89 at API prices, result: success.
