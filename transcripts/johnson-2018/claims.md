# crcns-fcx-2 · claims · run 42518931004

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453 claims/crcns-fcx-2 paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,185p docs/protocol.md; cat claims/001453/*.yaml
```

```
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 486 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -30 paper/10.1371-journal.pbio.2004274.txt; grep -n -i "supporting information\|S1 Fig\|S1 Table\|github\|code avail\|data avail" paper/10.1371-journal.pbio.2004274.txt | head -40; cat paper/fcx-2.data-description.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pbio.2004274.txt",
 "offset": 30
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pbio.2004274.txt",
 "offset": 30,
 "limit": 160
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pbio.2004274.txt",
 "offset": 190,
 "limit": 191
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git show --stat HEAD | head -30; ls transcripts/ | grep -i fcx; ls transcripts/crcns-fcx-2 2>/dev/null; grep -rl "supplement.*missing\|DOCX\|docx" claims/ | head
```

```
commit d9fbb315468ff24e7fd3bac48f7a5257b8c4e1af
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Sun Nov 8 20:11:56 2026 +0000

    Agent run on crcns-fcx-2: paper-match (success)
    
    Run: https://github.com/catalystneuro/encore/actions/runs/42518354278
    
    Account: verified

 papers/match/crcns-fcx-2.yaml | 17 +++++++++++++++++
 1 file changed, 17 insertions(+)
crcns-fcx-1
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml
claims/000943/10.7554-elife.89356.yaml
claims/001362/10.1111-jne.13286.yaml
claims/000483/10.1038-s41467-023-37704-5.yaml
claims/001545/10.26508-lsa.202403169.yaml
claims/000351/10.1126-science.abq6740.yaml
claims/001261/10.1002-cne.70001.yaml
```

**Agent calls Bash**

```bash
cd  cat papers/match/crcns-fcx-2.yaml; for f in claims/openneuro-ds000228/*.yaml claims/000943/*.yaml claims/001362/*.yaml; do echo "== $f"; grep -n -i -B2 -A3 "docx\|supplement" $f | head -20; done; ls claims/crcns-fcx-1 2>/dev/null
```

```
# Whether each paper CRCNS.org:fcx-2 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: crcns
  id: fcx-2
date: '2026-11-08'
papers:
- doi: 10.1371/journal.pbio.2004274
  relation: IsDescribedBy
  checks:
    text: true
    title_in_text: true
    names_this: false
    names_others: []
  verdict: primary
  by: checks
  reason: The archive says the paper describes the dataset, and the paper names no dataset.
== claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml
9-# Text read: the version of record (Nature Communications, open access, CC BY 4.0) as supplied
10-# under paper/ (text extracted from the PDF), with the main text, figure legends, Methods and the
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 80,214p paper/fcx-2.data-description.txt; cat claims/crcns-fcx-1/*.yaml | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; ls docs; grep -n "kind\|schema" docs/claims*.md 2>/dev/null | head -30
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

[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:5000])"; head -12 claims/crcns-fcx-1/*.yaml | tail -0; grep -n "^dataset\|^  archive\|^  id\|^paper\|^schema" claims/crcns-fcx-1/*.yaml
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
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1)[:4000]); print(list(d['properties']))"; sed -n 92,97p claims/crcns-fcx-1/*.yaml
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
[... 89 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-fcx-2/10.1371-journal.pbio.2004274.yaml",
 "content": "# Claims for Johnson, Adams, Solbakk, Endestad, Larsson, Ivanovic, Meling, Lin & Knight (2018),\n# PLoS Biology 16, e2004274, \"Dynamic frontotemporal systems process space and time in working\n# memory\", doi:10.1371/journal.pbio.2004274, on CRCNS data set fcx-2 (doi:10.6080/K0VX0DQD).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-08,\n# protocol as stated in docs/protocol.md (Reader), version pilot-13.\n#\n# Text read: the version of record, open access, PMC5895055, as supplied under paper/ (Europe PMC\n# full-text XML, flattened): Introduction, Results, Discussion, Materials and methods, the legends\n# of Figures 1 to 8 and the captions of the supporting information. No PDF was supplied. The\n# supporting information is S1 and S2 Fig (legends read) and S1 to S4 Table (DOCX files: group\n# mixed-effects model outputs with degrees of freedom). Only the captions of the four tables were\n# supplied; their contents were not read. Every claim below rests on a p-value the main text\n# prints, so no claim needs the tables, but the full model outputs (degrees of freedom, F values\n# of the PAC models) they hold were not available. Values shown only in figures (the percentages\n# of Fig 4B, the grand means of Fig 8A, the per-subject PSI of Fig 3B) were not read.\n#\n# Code. The Data Availability statement says the \"custom-built MATLAB codes\" are deposited with\n# the data on CRCNS (doi:10.6080/K0VX0DQD). The data descriptor says they are in the data set's\n# analysis_scripts directory (one <metric>_compute script per analysis, with subfunctions, using\n# FieldTrip). Being among the data set's files, they were not read in this run. Where a criterion\n# below names a detail as open, the author may find it settled by those scripts; the protocol's\n# order applies (Methods first, then the paper's analysis code).\n#\n# Data the paper used (Subjects; Data acquisition and preprocessing; Behavioral task). Ten adults\n# with intracranial electrodes for epilepsy monitoring (37 +- 13 years, 22 to 69; 7 male), from\n# UC Irvine (7 subjects, resampled to 1 kHz), Oslo (2 subjects, 512 Hz; 165 Hz low-pass, 50 Hz\n# line noise) and Stanford (1 subject, resampled to 1 kHz). Bipolar virtual electrodes, 254 in\n# all: 36 MTL, 116 lateral PFC, 102 OFC; MTL and PFC in the same hemisphere in 9 subjects, MTL\n# and OFC in 7. Task: 120 trials, 40 per condition (identity, spatial relation, temporal\n# relation). Trial: 1 s pretrial fixation, 800 ms start screen (\"identity\" or \"relation\"),\n# 100 ms fixation, two shapes of 200 ms each (top/bottom, first/second), a 900 or 1150 ms\n# precue delay, an 800 ms test cue, a postcue delay of the same length as the precue delay, and a\n# two-alternative response. Analysed: correct trials only, about 100 per subject. Segments: a\n# 200 ms baseline from 250 to 50 ms before the start screen; a 1500 ms encoding and precue\n# segment from first stimulus onset; a 900 ms postcue segment from test cue offset. Measured\n# variables: accuracy and correct-trial response time; ERPs; task-induced power; PLV; theta PSI;\n# cross-spectral PSI (theta phase to amplitude); time-frequency PAC by condition. By its\n# description the CRCNS data set holds, per subject, the filtered continuous data\n# (data_primary), the preprocessed bipolar data by segment (\"pre\", \"encmain\", \"proc\") with trial\n# information (accuracy, condition, delay jitter, response time), electrode MNI coordinates, a\n# per-trial table, a per-subject behaviour table, the list of channels analysed per region, and\n# the analysis scripts.\n#\n# Shared method details, used by the criteria below. Each is from the Materials and methods\n# unless stated.\n# M1. Trials and segments. Correct trials only (Behavioral task, last sentence). Delay segments\n#   are 900 ms. The postcue segment starts at test cue offset. The precue delay segment is not\n#   placed exactly by the paper: the encoding and precue segment is 1500 ms from first stimulus\n#   onset, and no gap between the two stimuli is given. Readings, (a) the last 900 ms of that\n#   segment, 600 to 1500 ms after first stimulus onset; (b) the 900 ms from the offset of the\n#   second stimulus, taken as 400 to 1300 ms if the stimuli are contiguous.\n# M2. Spectral decomposition. 24 logarithmically spaced bandpass FIR filters between 1 and 192 Hz\n#   (162 Hz for Oslo data), Hilbert amplitude squared, segments zero padded to 7500 ms (Spectral\n#   decomposition). The filters' band edges and order are not given; frequencies the paper names\n#   (9.5, 13.5, 16, 22.5, 64, 90.5, 128, 152.5 Hz) are to be matched by the chosen centres. This\n#   could move a peak by one bin; a standard log spacing is used and the centres stated.\n# M3. Task-induced power z. Baseline power pooled per channel and frequency, r points (r = trials\n#   in the subject's data set) drawn and averaged, 1000 times; encoding and delay power z-scored\n#   on that distribution, then down-sampled to 50 ms (Spectral decomposition). The paper does not\n#   say whether the z is taken on single-trial power or on the trial mean; since r is the number\n#   of trials, reading (a), the trial-mean power, is the one the procedure implies; (b) single-\n#   trial power, then averaged, is shown as a variant.\n# M4. Cluster-based permutation (ERPs, power). Within subject, per electrode; independent-samples\n#   t test (identity against relation, encoding and precue) or F test (identity, spatial,\n#   temporal, postcue), cluster-forming threshold 0.05 two-tailed, cluster statistic the sum of t\n#   or F, clustering over time (ERPs) or time and frequency (power), 1000 label shuffles, cluster\n#   p < 0.05 (ERPs section). The null is read as FieldTrip's maximum cluster sum per shuffle; the\n#   paper cites FieldTrip [48] for the testing.\n# M5. PSI (theta band). Delay segments demeaned by the trial-wise mean (the mean over trials is\n#   subtracted from each trial), zero padded to 4 s, 3-cycle sliding windows (dt = 3/f), 3 to\n#   7 Hz in 1 Hz steps, 2 Hz bandwidth, Hanning taper, cross-spectral density, PSI (PSI\n#   section). Null, 1000 shuffles of the frequencies in one signal; z = (raw - null mean) / null\n#   SD. MTL lead z > 1.96; frontal lead z < -1.96. Sign, positive when the MTL leads. Not fixed by\n#   the paper: how the time-resolved spectra of the sliding window are combined into one PSI per\n#   segment (read as averaging the cross-spectrum over the window positions inside the 900 ms\n#   segment, then over trials).\n# M6. Cross-spectral PSI. Theta input as in M5 from the phase electrode; amplitude envelopes by\n#   the Hilbert procedure of M2 at 9.5 to 152.5 Hz (128 Hz for Oslo data), each passed through the\n#   M5 decomposition; PSI between theta and each amplitude envelope; 1000-shuffle z as in M5; z\n#   averaged over amplitude frequencies; theta phase directing when the mean z > 1.96 (Cross-\n#   spectral directionality section). Within a region, phase and amplitude come from the same\n#   electrode; for a pair \"MTL -> PFC\", theta from the MTL electrode and amplitude from the PFC\n#   electrode, and the reverse for \"PFC -> MTL\" (read from the Results' use of the arrows).\n# M7. Group mixed-effects models for PSI and cross-spectral PSI, pre against postcue: per system,\n#   a linear mixed-effects model with task interval (2 levels) as fixed effect and subject and\n#   electrode or electrode pair as random effects, on all electrodes or pairs (PSI section, last\n#   paragraph; Cross-spectral directionality, last paragraph). Not fixed: whether the response\n#   is the raw or the z-scored PSI (readings (a) z-scored, (b) raw); random intercepts are used,\n#   with pair nested in subject, as the standard choice the text implies.\n# M8. Individual theta band. From task-induced power over the encoding and precue interval, the 6\n#   filters between 1.5 and 10 Hz averaged over trials, electrodes and time; the maximum gives a\n#   3 Hz wide band: 2 to 5, 3 to 6, 4 to 7 or 5 to 8 Hz (PAC section, paragraph 1). The paper\n#   also visually confirmed the peaks; the visual step is not reproducible and is left out.\n# M9. PAC. Postcue segment, theta-phase directing electrodes and pairs only (M6), trial-wise mean\n#   removed per condition, theta phase in the M8 band and amplitudes at 9.5 to 152.5 Hz (128 Hz\n#   Oslo) by Hilbert, circular-linear Pearson correlation across the trials of a condition at\n#   each time and amplitude frequency (PAC section, paragraph 2). Null, 100 shuffles; z as in M5.\n#   The shuffle \"randomly shuffled the amplitude frequencies across trials\" is not fixed.\n#   Readings, (a) amplitude values shuffled across trials relative to the phase (trial labels\n#   permuted), (b) the amplitude frequency labels shuffled within each trial. Down-sampled to\n#   50 ms.\n# M10. PAC group models. Per region and directional system, z-scored PAC in two models (spatial\n#   against identity, temporal against identity), fixed effects condition (2 levels), amplitude\n#   frequency (16 levels, 9.5 to 128 Hz) and time (19 levels), all interactions, random effects\n#   subject and electrode or pair. Direction models add direction (2 levels) as a fourth fixed\n#   effect, on the MTL -> frontal and frontal -> MTL data together. Significance at Bonferroni\n#   0.05/m, m the number of main and interaction effects (7 in three-factor models, 15 in the\n#   four-factor direction models) (PAC section, last paragraph). Not fixed: whether frequency and\n#   time enter as categorical factors (read as categorical, from \"16 amplitude frequency\" and \"19\n#   time-fixed effects\") and the random-effects structure (random intercepts, pairs nested in\n#   subject). The direction of a condition effect is read from the sign of the condition\n#   coefficient or the condition means (spatial or temporal minus identity).\nschema_version: 2\ndataset:\n  archive: crcns\n  id: fcx-2\n  doi: 10.6080/K0VX0DQD\npaper: doi:10.1371/journal.pbio.2004274\nclaims:\n- id: behavior-proficient\n  statement: All ten subjects performed the task well above chance, with accuracy from 0.79 to\n    0.97 (chance 0.5).\n  source: Results, paragraph 3 (before Theta activity is sustained during encoding and delay)\n  quote: We first confirmed that all subjects were proficient at the task (accuracy range\n    0.79–0.97, chance 0.5)\n  expected:\n  - quantity: lowest subject accuracy\n    value: 0.79\n    tolerance: 0.079\n  - quantity: highest subject accuracy\n    value: 0.97\n    tolerance: 0.097\n  criterion: Accuracy per subject over all 120 trials (correct over total). The paper does not say\n    whether accuracy is over all trials or over trials kept after artifact rejection; readings\n    (a) all 120 trials, (b) the trials kept in the preprocessed data. Reproduced when, under one\n    reading, every subject's accuracy lies in 0.711 to 1.0 (the range widened by 10% of each\n    bound) and the lowest and highest are within tolerance of 0.79 and 0.97.\n- id: behavior-no-difficulty-difference\n  statement: Accuracy and correct-trial response time did not differ between the identity,\n    spatial and temporal conditions (mean accuracy 0.90, 0.92, 0.89; mean response time 1659,\n    1335, 1475 ms).\n  source: Results, paragraph 3 (before Theta activity is sustained during encoding and delay);\n    Materials and methods, Behavioral task, paragraph 3\n  quote: 'any condition effects observed in the neural data could not be attributed to difficulty\n    (mixed-effects model, accuracy: F 1,28 < 0.10, p > 0.75; correct-trial response time: F 1,28\n    < 2.55, p > 0.12; mean ± SD, identity: 0.90 ± 0.04, 1659 ± 701 ms; spatial relation: 0.92 ±\n    0.09, 1335 ± 574 ms; temporal relation: 0.89 ± 0.09, 1475 ± 734 ms)'\n  statistics:\n  - about: accuracy across conditions\n    test: logit mixed-effects model, condition fixed effects, subject random effects\n    statistic: F(1,28) < 0.10\n    p: 0.75\n    p_relation: \">\"\n    n: 10 subjects\n  - about: correct-trial response time across conditions\n    test: linear mixed-effects model, condition fixed effects, subject random effects\n    statistic: F(1,28) < 2.55\n    p: 0.12\n    p_relation: \">\"\n    n: 10 subjects\n  expected:\n  - quantity: mean accuracy, identity\n    value: 0.90\n    tolerance: 0.04\n  - quantity: mean accuracy, spatial relation\n    value: 0.92\n    tolerance: 0.09\n  - quantity: mean accuracy, temporal relation\n    value: 0.89\n    tolerance: 0.09\n  - quantity: mean correct-trial response time, identity\n    value: 1659\n    tolerance: 701\n    unit: ms\n  - quantity: mean correct-trial response time, spatial relation\n    value: 1335\n    tolerance: 574\n    unit: ms\n  - quantity: mean correct-trial response time, temporal relation\n    value: 1475\n    tolerance: 734\n    unit: ms\n  criterion: A claim of absence, judged on the paper's test (Behavioral task, paragraph 3) a logit\n    mixed-effects model of accuracy and a linear mixed-effects model of correct-trial response\n    time, condition as fixed effect and subject as random effect, at p < 0.05. Reproduced when\n    neither model finds a condition effect; not reproduced when either does; the effect sizes\n    are reported either way. The F(1,28) the paper prints does not match a 3-level factor;\n    the readings named are (a) each relation condition tested against identity in turn (two\n    tests per measure, the claim holding when no test reaches p < 0.05), (b) a single 3-level\n    condition term. The tolerances are the paper's SDs across subjects; the means are taken\n    over subjects (the mean of each subject's condition value), as the reported SDs imply.\n- id: electrode-counts\n  statement: After bipolar rereferencing there were 254 electrodes, 36 MTL, 116 lateral PFC and\n    102 OFC; MTL and PFC were covered in the same hemisphere in 9 of 10 subjects and MTL and OFC\n    in 7 of 10.\n  source: Results, paragraph 1; Materials and methods, Data acquisition and preprocessing,\n    paragraph 2\n  quote: Signals were recorded directly from MTL ( n = 36 electrodes after bipolar montage\n    rereferencing), lateral PFC ( n = 116), and orbitofrontal cortex (OFC; n = 102) sites ...\n    the electrode arrays covered the MTL and PFC within the same hemisphere in 9 out of 10\n    subjects and the MTL and OFC in 7 out of 10 subjects\n  expected:\n  - quantity: MTL electrodes\n    value: 36\n    tolerance: 3.6\n  - quantity: PFC electrodes\n    value: 116\n    tolerance: 11.6\n  - quantity: OFC electrodes\n    value: 102\n    tolerance: 10.2\n  - quantity: subjects with MTL and PFC in the same hemisphere\n    value: 9\n    tolerance: 0\n  - quantity: subjects with MTL and OFC in the same hemisphere\n    value: 7\n    tolerance: 0\n  criterion: Counts of bipolar electrodes per region over all subjects, and of subjects with both\n    regions in one hemisphere. The subject counts are small integers, so they must match exactly\n    (10% of 9 or 7 is below one subject). It is not stated whether the 8 electrodes later\n    excluded for power differences (power-condition-exclusions) are in these counts; they are\n    (the text counts 254 before the exclusion).\n- id: correct-trial-counts\n  statement: The final data held on average 100 correct trials per subject, 33 +- 3 identity\n    (26 to 37), 34 +- 4 spatial (28 to 39) and 33 +- 3 temporal (28 to 37), and 10 +- 8 incorrect\n    trials (0 to 25).\n  source: Materials and methods, Data acquisition and preprocessing, paragraph 3\n  quote: 'The final dataset included an average of 100 correct trials per subject (mean ± SD\n    [range]): 33 ± 3 (26–37) identity, 34 ± 4 (28–39) spatial relation, 33 ± 3 (28–37) temporal\n    relation. There were too few incorrect trials for meaningful analysis: 10 ± 8 (0–25) per\n    subject.'\n  expected:\n  - quantity: mean correct trials per subject\n    value: 100\n    tolerance: 10\n  - quantity: mean correct identity trials per subject\n    value: 33\n    tolerance: 3\n  - quantity: mean correct spatial trials per subject\n    value: 34\n    tolerance: 4\n  - quantity: mean correct temporal trials per subject\n    value: 33\n    tolerance: 3\n  - quantity: mean incorrect trials per subject\n    value: 10\n    tolerance: 8\n  criterion: Counted from the trial information of the preprocessed segments (trials kept after\n    artifact rejection). Tolerances are the paper's SDs across subjects. Reproduced when every\n    mean is within tolerance and every subject's per-condition count lies in the paper's range\n    widened by 10% of each bound.\n- id: erp-no-condition-difference\n  statement: ERPs did not differ between identity, spatial and temporal conditions in any\n    electrode, over encoding, precue or postcue intervals.\n  source: Results, Theta activity is sustained during encoding and delay, paragraph 1; S1 Fig\n  quote: Cluster-based permutation testing [ 26 ] indicated that ERPs did not differ between\n    identity, spatial, and temporal conditions in any electrode (cluster-corrected p > 0.05; S1\n    Fig )\n  statistics:\n  - test: cluster-based permutation test, within subject\n    p: 0.05\n    p_relation: \">\"\n    corrected: cluster-based maximum correction\n    n: 254 electrodes in 10 subjects\n  criterion: A claim of absence, judged on the paper's test (ERPs section). Correct trials;\n    baseline, encoding and precue, and postcue segments zero padded to 7500 ms, 30 Hz low-pass FIR\n    filter, baseline-corrected by subtracting the temporal mean of the baseline. Cluster\n    permutation as in M4, identity against relation (t test) over the 1500 ms encoding and precue\n    segment and identity, spatial and temporal (F test) over the 900 ms postcue segment.\n    Reproduced when no electrode has a cluster with p < 0.05; not reproduced when any does. The\n    number of electrodes with a significant cluster, and the expected false-positive count at\n    alpha 0.05 over 254 electrodes and two tests, are reported either way.\n- id: power-theta-sustained\n  statement: Task-induced power showed sustained theta band (3 to 7 Hz) activity in MTL, PFC and\n    OFC over encoding and delay, with transient activity above 16 Hz, and alpha (8 to 13 Hz)\n    desynchronized in the MTL.\n  source: Results, Theta activity is sustained during encoding and delay, paragraph 2; Figure 2\n  quote: Single-subject analyses revealed sustained theta band (centered at 3–7 Hz) and variable\n    transient activities at higher frequencies (>16 Hz) in all regions (z > 1.96, p < 0.05; Fig\n    2 ). Activity in the alpha band (centered at 8–13 Hz) was desynchronized in the MTL (z <\n    −1.96, p < 0.05)\n  criterion: Power z as in M2 and M3 over the encoding and precue and the postcue segments. The\n    paper shows representative electrodes and gives no count of subjects or electrodes for\n    \"sustained\", so a measure is fixed here from its z threshold. For each subject and region,\n    the theta z (filters centred in 3 to 7 Hz, averaged) averaged over the region's electrodes;\n    theta is sustained when this z exceeds 1.96 over at least half of the encoding and delay time\n    points. Readings for the unit, (a) the region average per subject, (b) per electrode, the\n    fraction of electrodes meeting the rule. Reproduced when, under one reading, theta is\n    sustained in each of MTL, PFC and OFC in the majority of the subjects with that region, and\n    the MTL alpha z (filters centred in 8 to 13 Hz) is below -1.96 over at least half of the\n    time points in the majority of subjects with MTL electrodes. The half and the majority are\n    choices made here, as the paper gives none.\n- id: power-condition-exclusions\n  statement: Power did not differ between conditions at any time and frequency in 246 of 254\n    electrodes; the 8 that differed (5 PFC and 3 OFC, in 4 of 10 subjects) were excluded from\n    further analysis.\n  source: Results, Theta activity is sustained during encoding and delay, paragraph 3;\n    Materials and methods, Spectral decomposition, paragraph 3\n  quote: Cluster-based permutation testing indicated that power did not differ between identity,\n    spatial, and temporal conditions at any time–frequency point in 246 out of 254 electrodes\n    (cluster-corrected p > 0.05) ... the 8 electrodes exhibiting power effects (5 PFC plus 3 OFC\n    across 4 out of 10 subjects) were excluded from further analysis\n  expected:\n  - quantity: electrodes with a power condition difference\n    value: 8\n    tolerance: 0.8\n  - quantity: PFC electrodes with a power condition difference\n    value: 5\n    tolerance: 0.5\n  - quantity: OFC electrodes with a power condition difference\n    value: 3\n    tolerance: 0.3\n  - quantity: subjects with such electrodes\n    value: 4\n    tolerance: 0.4\n  criterion: Raw power (M2) z-scored on the baseline (M3), down-sampled to 50 ms, cluster\n    permutation as in M4 with clustering over time and frequency, identity against relation over\n    encoding and precue and the three conditions over postcue (the ERP design, which the\n    Methods say the power test is equivalent to). An electrode differs when any cluster in either\n    test has p < 0.05. The paper does not say whether the test runs on single-trial z or raw\n    power; readings (a) single-trial power z-scored on the baseline distribution, (b) single-\n    trial raw power. Reproduced when, under one reading, the counts match. The tolerances\n    are 10% of the reported counts, so they must match exactly. If the preprocessed data\n    already omit these electrodes, the claim cannot be tested on them and the author says so.\n- id: plv-theta-peak\n  statement: Phase-locking values over the delays peaked in the theta band within the MTL and\n    between MTL and frontal (PFC and OFC) electrodes, with broader synchrony in the alpha range.\n  source: Results, Theta oscillations direct local and long-range activity, paragraph 1; Figure\n    3A\n  quote: This analysis confirmed peak theta PLVs within the MTL and between MTL and frontal sites,\n    as well as more broadband synchrony in the alpha range ( Fig 3A )\n  criterion: PLV as in the Methods (PLV section) on the 900 ms pre and postcue segments (M1),\n    trial-wise mean removed, Hilbert filters from 2 to 20 Hz (M2 spacing), PLV across correct\n    trials at each time point, averaged over the segment and normalized by the maximum over\n    electrodes (Figure 3A legend). The paper computes PLV \"from the imaginary part\" without\n    a formula; readings (a) the absolute value of the mean over trials of the imaginary part of\n    the unit phase-difference vector (imaginary PLV), (b) the absolute value of the imaginary\n    part of the mean unit vector (the same quantity), (c) the phase-lag index. Figure 3A shows\n    one representative subject. Reproduced when, under one reading, the mean spectrum over MTL to\n    MTL pairs and over MTL to PFC and MTL to OFC pairs has a local maximum between 3 and 7 Hz, in\n    at least one subject for each of the three groups; the number of subjects with such a peak is\n    reported.\n- id: psi-theta-shift\n  statement: Theta-band PSI showed frontal-to-MTL leads during the precue delay and shifted toward\n    MTL leads (a bidirectional network) after the test cue, for MTL to PFC and MTL to OFC pairs.\n  source: Results, Theta oscillations direct local and long-range activity, paragraph 3; Figure\n    3B\n  quote: 'The precue delay was characterized by unidirectional frontal-to-MTL theta band\n    connectivity (threshold z < −1.96, p < 0.05) ... directionality shifted between frontotemporal\n    regions from a unidirectional to bidirectional network (postcue > precue, MTL–PFC: F 1,342 >\n    139, p < 4 × 10 −27 ; MTL–OFC: F 1,604 > 268, p < 4 × 10 −50 ; Fig 3B )'\n  statistics:\n  - about: MTL-PFC, postcue against precue\n    test: linear mixed-effects model\n    statistic: F(1,342) > 139\n    p: 4.0e-27\n    p_relation: \"<\"\n    n: 9 subjects, 172 electrode pairs\n  - about: MTL-OFC, postcue against precue\n    test: linear mixed-effects model\n    statistic: F(1,604) > 268\n    p: 4.0e-50\n    p_relation: \"<\"\n    n: 7 subjects, 303 electrode pairs\n  expected:\n  - quantity: MTL-PFC electrode pairs in the same hemisphere\n    value: 172\n    tolerance: 17.2\n  - quantity: MTL-OFC electrode pairs in the same hemisphere\n    value: 303\n    tolerance: 30.3\n  criterion: Theta PSI and its z as in M5, on all same-hemisphere MTL-PFC and MTL-OFC pairs,\n    precue and postcue segments (M1). Group test as in M7. Reproduced when, under one reading of\n    M1 and M7, for both networks (1) the mean precue PSI z over pairs is negative, with more pairs\n    below -1.96 than above 1.96, and (2) the mixed model finds postcue PSI greater than precue at\n    p < 0.05. Partially reproduced when (2) holds for one network only, or (2) holds for both but\n    (1) does not.\n- id: crossspectral-shift\n  statement: Theta phase to amplitude directionality (cross-spectral PSI) was absent in the precue\n    delay and shifted to theta phase leading amplitude after the test cue, within MTL, PFC and OFC\n    and in all four interregional directions.\n  source: Results, Theta oscillations direct local and long-range activity, paragraph 5; Figure\n    4A\n  quote: 'None of the electrodes or interregional electrode pairs were identified as\n    significantly theta phase directing during the precue delay ... cross-spectral directionality\n    shifted within and between all frontotemporal regions to a theta phase–driven network during\n    the postcue delay (postcue > precue, MTL: F 1,70 > 273, p < 7 × 10 −26 ; PFC: F 1,220 > 1 × 10\n    3 , p < 2 × 10 −88 ; OFC: F 1,196 > 911, p < 2 × 10 −75 ; MTL→PFC: F 1,342 > 1 × 10 3 , p < 7\n    × 10 −129 ; PFC→MTL: F 1,342 > 1 × 10 3 , p < 4 × 10 −121 ; MTL→OFC: F 1,604 > 2×10 3 , p < 8 ×\n    10 −211 ; OFC→MTL: F 1,604 > 2 × 10 3 , p < 4 × 10 −208 ; Fig 4A )'\n  statistics:\n  - about: MTL, postcue against precue\n    test: linear mixed-effects model\n    statistic: F(1,70) > 273\n    p: 7.0e-26\n    p_relation: \"<\"\n    n: 10 subjects, 36 electrodes\n  - about: PFC, postcue against precue\n    test: linear mixed-effects model\n    statistic: F(1,220) > 1000\n    p: 2.0e-88\n    p_relation: \"<\"\n    n: 9 subjects, 111 electrodes\n  - about: OFC, postcue against precue\n    test: linear mixed-effects model\n    statistic: F(1,196) > 911\n    p: 2.0e-75\n    p_relation: \"<\"\n    n: 8 subjects, 99 electrodes\n  - about: MTL to PFC, postcue against precue\n    test: linear mixed-effects model\n    statistic: F(1,342) > 1000\n    p: 7.0e-129\n    p_relation: \"<\"\n    n: 9 subjects, 172 electrode pairs\n  - about: PFC to MTL, postcue against precue\n    test: linear mixed-effects model\n    statistic: F(1,342) > 1000\n    p: 4.0e-121\n    p_relation: \"<\"\n    n: 9 subjects, 172 electrode pairs\n  - about: MTL to OFC, postcue against precue\n    test: linear mixed-effects model\n    statistic: F(1,604) > 2000\n    p: 8.0e-211\n    p_relation: \"<\"\n    n: 7 subjects, 303 electrode pairs\n  - about: OFC to MTL, postcue against precue\n    test: linear mixed-effects model\n    statistic: F(1,604) > 2000\n    p: 4.0e-208\n    p_relation: \"<\"\n    n: 7 subjects, 303 electrode pairs\n  expected:\n  - quantity: MTL electrodes in the model\n    value: 36\n    tolerance: 3.6\n  - quantity: PFC electrodes in the model\n    value: 111\n    tolerance: 11.1\n  - quantity: OFC electrodes in the model\n    value: 99\n    tolerance: 9.9\n  criterion: Cross-spectral PSI as in M6 on the precue and postcue segments (M1), for every\n    electrode (after the 8 exclusions) and every same-hemisphere MTL-frontal pair in both\n    directions. Group test as in M7 per system (7 models). Reproduced when, under one reading of\n    M1 and M7, (1) in all seven systems the model finds postcue greater than precue at p < 0.05,\n    and (2) no more than 5% of precue electrodes or pairs per system have mean z > 1.96 (the\n    paper reports none; 5% is the false-positive rate at its threshold, a choice made here).\n    Partially reproduced when (1) holds in four to six systems. The number of precue electrodes\n    and pairs above threshold is reported.\n- id: phase-directing-counts\n  statement: In the postcue delay, theta phase significantly led higher-frequency amplitude in 13\n    MTL, 52 PFC and 38 OFC electrodes, and in 56 MTL to PFC, 85 PFC to MTL, 93 MTL to OFC and 115\n    OFC to MTL electrode pairs.\n  source: Results, Theta oscillations direct local and long-range activity, paragraph 5; Figure\n    4B; Materials and methods, Cross-spectral directionality, paragraph 3\n  quote: we submitted only the electrodes and electrode pairs that showed significant theta phase\n    leads over amplitude to further analysis of cross-spectral directionality and PAC ( n = 13\n    MTL, 52 PFC, 38 OFC, 56 MTL→PFC, 85 PFC→MTL, 93 MTL→OFC, and 115 OFC→MTL)\n  depends_on:\n  - crossspectral-shift\n  expected:\n  - quantity: phase-directing MTL electrodes\n    value: 13\n    tolerance: 1.3\n  - quantity: phase-directing PFC electrodes\n    value: 52\n    tolerance: 5.2\n  - quantity: phase-directing OFC electrodes\n    value: 38\n    tolerance: 3.8\n  - quantity: phase-directing MTL to PFC pairs\n    value: 56\n    tolerance: 5.6\n  - quantity: phase-directing PFC to MTL pairs\n    value: 85\n    tolerance: 8.5\n  - quantity: phase-directing MTL to OFC pairs\n    value: 93\n    tolerance: 9.3\n  - quantity: phase-directing OFC to MTL pairs\n    value: 115\n    tolerance: 11.5\n  - quantity: subjects with phase-directing MTL electrodes\n    value: 8\n    tolerance: 0\n  - quantity: subjects with phase-directing MTL to OFC pairs\n    value: 5\n    tolerance: 0\n  criterion: Postcue mean cross-spectral PSI z > 1.96 (M6). Each count within 10%. The subject\n    counts the Methods give (8 MTL, 8 PFC, 8 OFC, 9 MTL to PFC, 9 PFC to MTL, 5 MTL to OFC, 5 OFC\n    to MTL) are reported; two are listed as expected values and must match exactly. Reproduced\n    when at least five of the seven electrode and pair counts are within tolerance; partially\n    reproduced for three or four. The 5 of 7 is a choice made here.\n- id: crossspectral-equal-strength\n  statement: Among phase-directing pairs, the strength of theta phase directionality did not\n    differ across amplitude frequencies or between the MTL to frontal and frontal to MTL\n    directions.\n  source: Results, Theta oscillations direct local and long-range activity, paragraph 6; S1 Table\n  quote: We used linear mixed-effects models to confirm that the strength of theta phase\n    directionality was equal across the amplitude frequency ranges (alpha through high-frequency\n    broadband) and in both MTL→PFC/OFC and PFC/OFC→MTL directions (uncorrected p > 0.11; S1\n    Table )\n  statistics:\n  - test: linear mixed-effects models, amplitude frequency and direction fixed effects\n    p: 0.11\n    p_relation: \">\"\n    n: phase-directing pairs, MTL-PFC (56 and 85) and MTL-OFC (93 and 115)\n  depends_on:\n  - phase-directing-counts\n  criterion: A claim of absence, judged on the paper's test (Cross-spectral directionality,\n    paragraph 3) per network (MTL-PFC, MTL-OFC), a linear mixed-effects model of the postcue\n    cross-spectral PSI z of the phase-directing pairs with 16 amplitude frequencies (9.5 to\n    128 Hz) and 2 directions as fixed effects (with their interaction) and subject and pair as\n    random effects. Reproduced when no frequency, direction or interaction effect has\n    uncorrected p < 0.05 in either network; not reproduced when any does; the effects are\n    reported either way. The paper's S1 Table, which holds these models, was not supplied; the\n    text also calls these models confirmatory with p > 0.11, so p < 0.05 is used as the\n    threshold. The paper's Methods list the local regions with these models; the Results speak\n    of the directions, so the local models (frequency only) are shown as a variant.\n- id: theta-peak-bands\n  statement: Individual theta peaks were found at 2 to 5 Hz in 3 subjects, 3 to 6 Hz in 2, 4 to\n    7 Hz in 2 and 5 to 8 Hz in 3.\n  source: Materials and methods, PAC, paragraph 1\n  quote: 'Peaks were detected across the theta band: n = 3 at 2 to 5 Hz, n = 2 at 3 to 6 Hz, n =\n    2 at 4 to 7 Hz, and n = 3 at 5 to 8 Hz.'\n  expected:\n  - quantity: subjects with peak band 2 to 5 Hz\n    value: 3\n    tolerance: 0\n  - quantity: subjects with peak band 3 to 6 Hz\n    value: 2\n    tolerance: 0\n  - quantity: subjects with peak band 4 to 7 Hz\n    value: 2\n    tolerance: 0\n  - quantity: subjects with peak band 5 to 8 Hz\n    value: 3\n    tolerance: 0\n  criterion: Peak as in M8. The paper does not say which electrodes are averaged; readings (a) all\n    of a subject's analysed electrodes, (b) only the electrodes entering the PAC analysis\n    (phase-directing). Counts of subjects must match exactly (10% of a count of 2 or 3 is below\n    one). Reproduced when, under one reading, all four counts match; partially reproduced when\n    at least seven subjects fall in the same band under one reading as the distribution implies\n    (the per-subject assignment is not given).\n- id: pac-mtl-spatial\n  statement: Within the MTL, theta PAC was greater for spatial than identity information, with\n    peak differences at beta and gamma amplitudes (centred at 22.5 and 64 Hz); PAC did not differ\n    between temporal and identity information.\n  source: Results, Dynamic theta PAC tracks information in working memory, paragraph 3; Figure 5;\n    S2 Table\n  quote: Locally within the MTL, PAC was greater for spatial than identity information (condition\n    p < 9 × 10 −6 ), with peak differences at broadband beta and gamma amplitudes (centered at\n    22.5 and 64 Hz; condition × frequency p < 3 × 10 −5 ; Fig 5 , S2 Table ). No differences were\n    observed in the temporal information model (i.e., temporal versus identity information;\n    Bonferroni-corrected p > 0.05).\n  statistics:\n  - about: condition, spatial against identity\n    test: linear mixed-effects model\n    p: 9.0e-6\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 13 MTL electrodes in 8 subjects\n  - about: condition by frequency, spatial against identity\n    test: linear mixed-effects model\n    p: 3.0e-5\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 13 MTL electrodes in 8 subjects\n  - about: temporal against identity, all effects\n    test: linear mixed-effects model\n    p: 0.05\n    p_relation: \">\"\n    corrected: Bonferroni\n    n: 13 MTL electrodes in 8 subjects\n  depends_on:\n  - phase-directing-counts\n  - theta-peak-bands\n  criterion: PAC as in M9 on the phase-directing MTL electrodes, models as in M10. Reproduced\n    when, under one reading of M9 and M10, (1) the spatial model has a condition effect and a\n    condition by frequency effect below 0.05/7 with spatial above identity, (2) the largest\n    spatial minus identity difference over amplitude frequencies (averaged over time and\n    electrodes) is at a frequency within one filter of 22.5 Hz or of 64 Hz, and (3) the temporal\n    model has no condition effect or condition interaction below 0.05/7. Partially reproduced\n    when (1) holds but (2) or (3) does not.\n- id: pac-frontal-no-condition\n  statement: Within the PFC and within the OFC, theta PAC did not differ between identity,\n    spatial and temporal information.\n  source: Results, Dynamic theta PAC tracks information in working memory, paragraph 3; S2 Fig; S2\n    Table\n  quote: In contrast, no condition effects were observed within the PFC or OFC\n    (Bonferroni-corrected p > 0.05; S2 Fig , S2 Table ), indicating that frontal PAC did not\n    distinguish between identity, spatial, and temporal information in working memory.\n  statistics:\n  - test: linear mixed-effects models\n    p: 0.05\n    p_relation: \">\"\n    corrected: Bonferroni\n    n: 52 PFC electrodes in 8 subjects and 38 OFC electrodes in 8 subjects\n  depends_on:\n  - phase-directing-counts\n  - theta-peak-bands\n  criterion: A claim of absence, judged on the paper's test, the M10 models (spatial against\n    identity, temporal against identity) for PFC and for OFC at Bonferroni 0.05/7. \"Condition\n    effects\" is read as the condition main effect and every interaction that includes condition.\n    Reproduced when none of these reaches 0.05/7 in any of the four models; not reproduced when\n    any does. The effects are reported either way.\n- id: pac-mtl-pfc-spatial\n  statement: In the MTL to PFC direction, theta PAC was greater for spatial than identity\n    information, with peak differences at PFC beta amplitudes (13.5 to 16 Hz) during 100 to 250 ms\n    and 800 to 900 ms of the postcue delay.\n  source: Results, Dynamic theta PAC tracks information in working memory, paragraph 4; Figure 6\n    top; S3 Table\n  quote: Between regions, PAC was greater for spatial than identity information in the MTL → PFC\n    direction (condition p < 2 × 10 −10 ), with peak differences at PFC beta amplitudes (centered\n    at 13.5–16 Hz) during the 100- to 250-ms and 800- to 900-ms epochs (condition × frequency p <\n    2 × 10 −4 ; condition × time p < 2×10 −9 ; condition × frequency × time p = 4 × 10 −4 ; Fig 6\n    top, S3 Table )\n  statistics:\n  - about: condition\n    test: linear mixed-effects model\n    p: 2.0e-10\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 56 MTL to PFC pairs in 9 subjects\n  - about: condition by frequency\n    test: linear mixed-effects model\n    p: 2.0e-4\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 56 MTL to PFC pairs in 9 subjects\n  - about: condition by time\n    test: linear mixed-effects model\n    p: 2.0e-9\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 56 MTL to PFC pairs in 9 subjects\n  - about: condition by frequency by time\n    test: linear mixed-effects model\n    p: 4.0e-4\n    corrected: Bonferroni\n    n: 56 MTL to PFC pairs in 9 subjects\n  depends_on:\n  - phase-directing-counts\n  - theta-peak-bands\n  criterion: PAC as in M9 on the phase-directing MTL to PFC pairs (theta phase from the MTL\n    electrode, amplitude from the PFC electrode), spatial model as in M10. Reproduced when, under\n    one reading of M9 and M10, (1) the condition, condition by frequency, condition by time and\n    three-way effects are each below 0.05/7 with spatial above identity, and (2) the largest\n    spatial minus identity difference (averaged over pairs) lies at an amplitude frequency within\n    one filter of 13.5 to 16 Hz and in a 50 ms time bin within 100 to 250 ms or 800 to 900 ms.\n    Partially reproduced when the condition effect holds with spatial above identity but some\n    of the rest does not.\n- id: pac-mtl-pfc-temporal\n  statement: In the MTL to PFC direction, theta PAC was also greater for temporal than identity\n    information.\n  source: Results, Dynamic theta PAC tracks information in working memory, paragraph 4; Figure 6\n    top; S3 Table\n  quote: MTL → PFC PAC was also greater for temporal than identity information (condition p < 9 ×\n    10 −5 ).\n  statistics:\n  - test: linear mixed-effects model, condition\n    p: 9.0e-5\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 56 MTL to PFC pairs in 9 subjects\n  depends_on:\n  - phase-directing-counts\n  - theta-peak-bands\n  criterion: PAC as in M9, temporal model as in M10, MTL to PFC pairs. Reproduced when, under one\n    reading of M9 and M10, the condition effect is below 0.05/7 with temporal above identity.\n- id: pac-pfc-mtl-no-condition\n  statement: In the PFC to MTL direction, theta PAC did not differ by condition.\n  source: Results, Dynamic theta PAC tracks information in working memory, paragraph 4; Figure 6\n    bottom; S3 Table\n  quote: In contrast, no condition effects were observed in the PFC → MTL direction\n    (Bonferroni-corrected p > 0.05; Fig 6 bottom, S3 Table ).\n  statistics:\n  - test: linear mixed-effects models\n    p: 0.05\n    p_relation: \">\"\n    corrected: Bonferroni\n    n: 85 PFC to MTL pairs in 9 subjects\n  depends_on:\n  - phase-directing-counts\n  - theta-peak-bands\n  criterion: A claim of absence, judged on the paper's test, the M10 spatial and temporal models\n    on the phase-directing PFC to MTL pairs (theta phase from the PFC electrode, amplitude from\n    the MTL electrode) at Bonferroni 0.05/7. Reproduced when neither the condition main effect nor\n    any interaction with condition reaches 0.05/7 in either model; not reproduced when any does;\n    the effects are reported either way.\n- id: pac-mtl-ofc-spatial\n  statement: In the MTL to OFC direction, theta PAC was greater for spatial than identity\n    information, with peak differences at alpha amplitudes (centred at 9.5 Hz); no effects were\n    found in the temporal model or in the OFC to MTL direction.\n  source: Results, Dynamic theta PAC tracks information in working memory, paragraph 4; Figure 7;\n    S4 Table\n  quote: In the MTL → OFC direction, PAC was greater for spatial than identity information\n    (condition p < 4 × 10 −6 ), with peak differences at alpha amplitudes (centered at 9.5 Hz;\n    condition × frequency p < 5 × 10 −3 ; Fig 7 top, S4 Table ). No effects were observed in the\n    temporal information model or in the OFC → MTL direction (Bonferroni-corrected p > 0.05; Fig\n    7 bottom, S4 Table ).\n  statistics:\n  - about: MTL to OFC, condition, spatial against identity\n    test: linear mixed-effects model\n    p: 4.0e-6\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 93 MTL to OFC pairs in 5 subjects\n  - about: MTL to OFC, condition by frequency, spatial against identity\n    test: linear mixed-effects model\n    p: 5.0e-3\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 93 MTL to OFC pairs in 5 subjects\n  - about: MTL to OFC temporal model, and OFC to MTL models\n    test: linear mixed-effects models\n    p: 0.05\n    p_relation: \">\"\n    corrected: Bonferroni\n    n: 93 MTL to OFC and 115 OFC to MTL pairs in 5 subjects\n  depends_on:\n  - phase-directing-counts\n  - theta-peak-bands\n  criterion: PAC as in M9, models as in M10. Reproduced when, under one reading of M9 and M10,\n    (1) in the MTL to OFC spatial model the condition and condition by frequency effects are below\n    0.05/7 with spatial above identity, (2) the largest spatial minus identity difference over\n    amplitude frequencies is within one filter of 9.5 Hz, and (3) no effect reaches 0.05/7 in the\n    MTL to OFC temporal model or in either OFC to MTL model (\"no effects\" read as no condition\n    main effect or interaction with condition, the paper's test for absence; all effects are\n    reported). Partially reproduced when (1) holds and (2) or (3) does not. The condition by\n    frequency p < 5e-3 is above 0.05/7 = 0.0071 only if m is larger than 7; it is below, so it\n    meets the paper's threshold as stated.\n- id: pac-mtl-pfc-direction\n  statement: Modelling both MTL-PFC directions together, the MTL directed the PFC preferentially\n    for spatial and temporal over identity information (condition by direction), while PAC was\n    greater overall in the PFC to MTL than the MTL to PFC direction.\n  source: Results, Dynamic theta PAC tracks information in working memory, paragraph 6; Figure 8A\n    top; S3 Table\n  quote: 'The MTL–PFC models confirmed that the MTL directed the PFC preferentially during the\n    processing of spatiotemporal over identity information (condition × direction; spatial model:\n    p < 3 × 10 −8 ; temporal model: p < 2 × 10 −5 ; Fig 8A top, S3 Table ). However, while PFC →\n    MTL PAC did not differ by condition, PAC was enhanced in the PFC → MTL relative to MTL → PFC\n    direction (direction; spatial model: p < 2 × 10 −11 ; temporal model: p < 2 × 10 −9 ).'\n  statistics:\n  - about: condition by direction, spatial model\n    test: linear mixed-effects model\n    p: 3.0e-8\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 56 MTL to PFC and 85 PFC to MTL pairs in 9 subjects\n  - about: condition by direction, temporal model\n    test: linear mixed-effects model\n    p: 2.0e-5\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 56 MTL to PFC and 85 PFC to MTL pairs in 9 subjects\n  - about: direction, spatial model\n    test: linear mixed-effects model\n    p: 2.0e-11\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 56 MTL to PFC and 85 PFC to MTL pairs in 9 subjects\n  - about: direction, temporal model\n    test: linear mixed-effects model\n    p: 2.0e-9\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 56 MTL to PFC and 85 PFC to MTL pairs in 9 subjects\n  depends_on:\n  - pac-mtl-pfc-spatial\n  - pac-mtl-pfc-temporal\n  criterion: Direction models as in M10 (four fixed effects, threshold 0.05/15), on the PAC z of\n    the MTL to PFC and PFC to MTL pairs. Reproduced when, under one reading of M9 and M10, in\n    both the spatial and the temporal model (1) the condition by direction effect is below the\n    threshold, with the relation minus identity difference larger in the MTL to PFC direction,\n    and (2) the direction effect is below the threshold with mean PAC higher for PFC to MTL.\n    Partially reproduced when (1) and (2) hold in one model only, or one of them holds in both.\n- id: pac-mtl-ofc-direction\n  statement: Modelling both MTL-OFC directions together, PAC was greater in the MTL to OFC than the\n    OFC to MTL direction and greater for spatial than identity information in that direction; the\n    MTL-OFC temporal model showed no effects.\n  source: Results, Dynamic theta PAC tracks information in working memory, paragraph 6; Figure 8A\n    bottom; S4 Table\n  quote: PAC was greater in the MTL → OFC direction than in reverse and greater for spatial than\n    identity information in the same direction (direction p < 2 × 10 −3 ; condition × direction p\n    < 3 × 10 −4 ; Fig 8A bottom, S4 Table ), highlighting a relatively unidirectional MTL → OFC\n    network for processing spatial information. No effects were observed in the MTL–OFC temporal\n    model (Bonferroni-corrected p > 0.05).\n  statistics:\n  - about: direction, spatial model\n    test: linear mixed-effects model\n    p: 2.0e-3\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 93 MTL to OFC and 115 OFC to MTL pairs in 5 subjects\n  - about: condition by direction, spatial model\n    test: linear mixed-effects model\n    p: 3.0e-4\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 93 MTL to OFC and 115 OFC to MTL pairs in 5 subjects\n  - about: temporal model, all effects\n    test: linear mixed-effects model\n    p: 0.05\n    p_relation: \">\"\n    corrected: Bonferroni\n    n: 93 MTL to OFC and 115 OFC to MTL pairs in 5 subjects\n  depends_on:\n  - pac-mtl-ofc-spatial\n  criterion: Direction models as in M10 (threshold 0.05/15), MTL to OFC and OFC to MTL pairs.\n    Reproduced when, under one reading of M9 and M10, (1) in the spatial model the direction\n    effect is below the threshold with MTL to OFC higher and the condition by direction effect is\n    below the threshold with the spatial minus identity difference larger for MTL to OFC, and\n    (2) no effect in the temporal model reaches the threshold (the paper's test for absence,\n    judged on all effects as the text says \"No effects\"). Partially reproduced when (1) holds and\n    (2) does not, or one part of (1) holds. The paper's direction p < 2e-3 is above 0.05/15 =\n    0.0033 only if m exceeds 25; with m = 15 it meets the threshold.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-fcx-2/10.1371-journal.pbio.2004274.yaml; python - "$f" <<'EOF'
import sys
p=sys.argv[1]; s=open(p).read()
reps=[("""reported). Partially reproduced when (1) holds and (2) or (3) does not. The condition by
    frequency p < 5e-3 is above 0.05/7 = 0.0071 only if m is larger than 7; it is below, so it
    meets the paper's threshold as stated.""","""reported). Partially reproduced when (1) holds and (2) or (3) does not."""),
("""Partially reproduced when (1) holds and
    (2) does not, or one part of (1) holds. The paper's direction p < 2e-3 is above 0.05/15 =
    0.0033 only if m exceeds 25; with m = 15 it meets the threshold.""","""Partially reproduced when (1) holds and
    (2) does not, or one part of (1) holds."""),
("""It is not stated whether the 8 electrodes later
    excluded for power differences (power-condition-exclusions) are in these counts; they are
    (the text counts 254 before the exclusion).""","""The counts include the 8 electrodes later excluded
    for power differences (power-condition-exclusions), as the text counts 254 before that
    exclusion.""")]
for a,b in reps:
    assert a in s, a[:40]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py $f paper/10.1371-journal.pbio.2004274.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-fcx-2/10.1371-journal.pbio.2004274.yaml; grep -n "—\|rather" $f; python -c "import yaml;d=yaml.safe_load(open('$f'));print(sum('criterion' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('expected' in c for c in d['claims']))"
```

```
21 13 9
```

**Agent**

I wrote the claims file at `claims/crcns-fcx-2/10.1371-journal.pbio.2004274.yaml`. The quote checker reports 21 claims, 21 quotes, 33 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (PMC5895055, open access): main text, Methods, the legends of Figures 1 to 8, and the captions of the supporting information. There was no PDF. Of the supplement, I read the S1 and S2 Fig legends. S1 to S4 Table are DOCX files of model outputs, and only their captions were supplied.

**Code:** the paper says its MATLAB scripts are deposited with the data on CRCNS, in the dataset's `analysis_scripts` folder. Because they are among the dataset's files, I did not read them. The author may find some of the open details below settled there.

**Claims:** 21, all with quotes; 13 report statistics, 9 have expected values and all 21 have criteria. They cover:
- behaviour: proficiency, and no difference in difficulty between conditions
- electrode and correct-trial counts
- event-related potentials (ERPs): no condition differences
- theta power: sustained theta, and the 8 electrodes excluded for condition differences in power
- phase locking: theta peak
- theta directionality (phase slope index): shift from precue to postcue
- theta phase-to-amplitude directionality: shift in seven systems, counts of phase-directing electrodes and pairs, and equal strength across frequencies and directions
- individual theta peak bands
- phase-amplitude coupling (PAC): ten effects across the MTL, PFC, OFC and the MTL-PFC and MTL-OFC directions, including the two models that compare directions

All claims use the dataset alone.

**Details the paper leaves open, with the readings named:**
- **Precue delay segment:** (a) 600 to 1500 ms after first stimulus onset, or (b) 400 to 1300 ms, if the two stimuli ran back to back.
- **Behaviour model:** the printed F(1,28) does not fit a three-level factor. (a) Each relation condition tested against identity, or (b) one three-level term. Accuracy is (a) over all trials or (b) over the trials kept after artifact rejection.
- **Power z-score:** (a) on trial-mean power, or (b) on single trials. For the power condition test, (a) z-scored or (b) raw single-trial power.
- **"Sustained" theta and the alpha drop:** no count is given. Unit (a) region average per subject or (b) per electrode. The "at least half the time points, in most subjects" threshold is my choice and is marked as one.
- **Phase locking "from the imaginary part":** (a or b) imaginary PLV, or (c) phase-lag index.
- **Group models for directionality:** (a) z-scored or (b) raw values.
- **PAC surrogate shuffle:** (a) trials permuted against phase, or (b) amplitude-frequency labels shuffled.
- **Electrodes for the theta peak:** (a) all analysed electrodes, or (b) the phase-directing ones only.
- **Fixed as standard choices and marked as such:** filter band edges, combining the sliding-window spectra, random-effects structure, frequency and time as categorical factors, and m = 7 or 15 in the Bonferroni correction.
- **My thresholds, marked in the criteria:** at most 5% of electrodes significant in the precue delay, and 5 of 7 counts within tolerance.

**Missing:** the contents of S1 to S4 Table. No claim's expected value needs them; the equal-strength claim rests on the main-text sentence "uncorrected p > 0.11". Without a PDF, I could not read values shown only in figures (the Fig 4B percentages, the Fig 8A means, the Fig 3B per-subject values).

## End of run

16 turns, 4 minutes, $1.50 at API prices, result: success.
