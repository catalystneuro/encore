# 001893 · claims-check · run 39541720562

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001893/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; python tools/claims_check.py claims/001893/*.yaml paper/*.txt; cat claims/001893/*.yaml; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/29c89c09-7723-4cd2-ace3-b1a8798ac26c/tool-results/b3fy696y9.txt"
}
```

```
1	   - `expected`: each reported number the claim rests on, with a tolerance.
2	     Use the paper's own uncertainty when it gives one (a confidence
3	     interval, or the stated spread); otherwise 10% of the reported value.
4	     For a reported range ("2 to 13%"), the claim holds inside the range
5	     widened by 10% of each bound. Give the reason for any other tolerance.
6	   - `criterion`: how the claim will be judged, for any claim that is not
7	     settled by its expected values alone ("similar", "many", "tended to").
8	     It is written from the paper alone, before anyone analyses the data.
9	   - When a reported number can be read in more than one way (which trials
10	     form the denominator, which subset is meant), list in the criterion the
11	     readings the paper's text plausibly allows, before the analysis. The
12	     claim is reproduced if the result matches under any of them. The
13	     notebook shows every reading, the notes say which ones match, and the
14	     ambiguity is recorded as a deviation.
15	   - Methods come from the paper, never from the author. Every part of a
16	     criterion's method (the selection, the measure, the test, windows,
17	     bins, thresholds, what a measure is compared with) is taken from the
18	     Methods, the figure legends, the supplement, or the code the paper
19	     links, and the criterion says which. Search all of them before
20	     treating a detail as open.
[... 559 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "" *.txt | awk -F: 'length($0)>0' | cut -c1-300 | head -80; grep -c "" *.txt
```

```
1:DOI: 10.64898/2026.04.10.717727
2:Version: preprint, version 1
3:Source: bioRxiv JATS XML (api.biorxiv.org)
4:Stored: 2026-10-20
5:Extracted: JATS XML flattened
6:------------------------------------------------------------------------
7:Topographic structure and function of locus coeruleus norepinephrine neurons
8:
9:## Abstract
10:
11:Norepinephrine (NE) is released throughout most of the central nervous system by neurons in the locus coeruleus (LC). We found a relationship between the morphologies, gene expression, and activity of LC-NE neurons in mice. Axonal projections of individual neurons were extensive but largely confi
12:
13:## Introduction
14:
15:Monoamine neurotransmitters are released by small populations of neurons that project extensively throughout the central nervous system (CNS). The locus coeruleus (LC) in the pons supplies the monoamine norepinephrine (NE, also known as noradrenaline) to most of the CNS ( Swanson 1976 ; Amaral & 
16:
17:The panoply of functions of LC-NE neurons is often ascribed to their complex axonal projections, which span most of the brain and spinal cord. Although the LC-NE system has often been treated as homogeneous, several observations point to heterogeneity among LC-NE neurons ( Poe et al. 2020 ). LC n
18:
19:We asked two questions about the LC-NE system: First, is NE released by different LC neurons in different brain regions? To answer this, we examined the morphologies and gene expression patterns of NE neurons across the LC. The projections of individual neurons largely targeted specific brain reg
20:
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "^## " *.txt | head -100
```

```
9:## Abstract
13:## Introduction
21:## Results
23:## LC-NE projections are spatially organized
29:## Spatial distribution of LC-NE neurons.
35:## Organization of LC-NE neurons and their brain-wide projections.
43:## Brain-wide projections of LC-NE neurons in the right hemisphere.
51:## Individual LC-NE morphologies.
57:## Spatial distribution of LC-NE axon innervation.
63:## LC-NE projections are spatially organized.
73:## LC-NE projections measured with MAPseq and BARseq.
81:## Somatodendritic morphologies of LC-NE neurons vary continuously.
87:## Retrograde tracing to quantify locations of somata with projections to olfactory bulb, frontal cortex, thalamus, periaqueductal gray, cerebellar cortex, or spinal cord.
91:## LC-NE neurons have graded gene expression in space
97:## LC-NE neurons have distinct gene expression from surrounding cells.
103:## Expression levels of genes in different categories of putative functions.
109:## LC-NE gene expression is graded in space and varies by projection target.
117:## MERFISH analysis.
125:## Retro-seq.
131:## Spatial variation of LC-NE activity during action-outcome learning
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; f=*.txt; for l in 11 25 39 47 67 69 77 91 93 95 111 113 115 131 133 135 137 147 149 151 153 165 167 169 171 199 201 203 207 211 217; do echo "== $l"; sed -n "${l}p" $f; done
```

```
<persisted-output>
Output too large (29.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/29c89c09-7723-4cd2-ace3-b1a8798ac26c/tool-results/bpb9hrm9j.txt

Preview (first 2KB):
== 11
Norepinephrine (NE) is released throughout most of the central nervous system by neurons in the locus coeruleus (LC). We found a relationship between the morphologies, gene expression, and activity of LC-NE neurons in mice. Axonal projections of individual neurons were extensive but largely confined to subsets of brain regions. Axonal projections and graded gene expression correlated with locations of cell bodies in LC. In a behavioral task requiring ongoing learning from actions, neurons in dorsal LC projecting to the cerebral cortex were excited when mice made a different choice from the previous one and by reward prediction errors, a signal driving learning. Background activity of neurons in ventral LC was higher when mice ignored stimuli indicating potential reward availability. These observations reveal a topographically organized structure and function of a neurotransmitter system and show that it contains learning signals for flexible behavior.
== 25
We begin by defining the boundary of mouse LC in the standardized common coordinate framework (CCFv3) (Q. Wang et al. 2020 ) by mapping NE neurons in the pons. We labeled nuclei of NE neurons expressing Cre recombinase under the control of dopamine beta hydroxylase ( Dbh -Cre), the rate-limiting enzyme for NE production. We extracted whole brains, made them optically transparent, and imaged them with selective plane illumination microscopy (SPIM; 34,998 cells, 8 mice; Figures 1a, 1b , and S1 ). We defined LC in the CCF as a small dorsal region (0.13 mm 3 in volume) containing approximately two-thirds of all pontine NE neurons (67th density percentile, 1507 ± 55, mean ± SD). Additional NE neurons were found in sub-coeruleus (367 ± 95) ( Amaral & Sinnamon 1977 ).
== 3
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/29c89c09-7723-4cd2-ace3-b1a8798ac26c/tool-results/bpb9hrm9j.txt"
}
```

```
1	== 11
2	Norepinephrine (NE) is released throughout most of the central nervous system by neurons in the locus coeruleus (LC). We found a relationship between the morphologies, gene expression, and activity of LC-NE neurons in mice. Axonal projections of individual neurons were extensive but largely confined to subsets of brain regions. Axonal projections and graded gene expression correlated with locations of cell bodies in LC. In a behavioral task requiring ongoing learning from actions, neurons in dorsal LC projecting to the cerebral cortex were excited when mice made a different choice from the previous one and by reward prediction errors, a signal driving learning. Background activity of neurons in ventral LC was higher when mice ignored stimuli indicating potential reward availability. These observations reveal a topographically organized structure and function of a neurotransmitter system and show that it contains learning signals for flexible behavior.
3	== 25
4	We begin by defining the boundary of mouse LC in the standardized common coordinate framework (CCFv3) (Q. Wang et al. 2020 ) by mapping NE neurons in the pons. We labeled nuclei of NE neurons expressing Cre recombinase under the control of dopamine beta hydroxylase ( Dbh -Cre), the rate-limiting enzyme for NE production. We extracted whole brains, made them optically transparent, and imaged them with selective plane illumination microscopy (SPIM; 34,998 cells, 8 mice; Figures 1a, 1b , and S1 ). We defined LC in the CCF as a small dorsal region (0.13 mm 3 in volume) containing approximately two-thirds of all pontine NE neurons (67th density percentile, 1507 ± 55, mean ± SD). Additional NE neurons were found in sub-coeruleus (367 ± 95) ( Amaral & Sinnamon 1977 ).
5	== 39
6	We next explored the structure of LC-NE neuron projections ( Swanson & Hartman 1975 ; Nomura et al. 2014 ). To quantify the distribution of LC-NE axons across the brain, we densely labeled LC-NE neurons unilaterally in Dbh -Cre mice
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; f=*.txt; for l in 117 119 121 123 125 127 129 155 157 159 161 163 175 177 179 181 183 185 187 189 191 193 195 197; do echo "== $l"; sed -n "${l}p" $f; done
```

```
== 117
## MERFISH analysis.
== 119
a , CCA analyses of population gene expression. b , CI around CCA analysis of population gene expression. c , Example genes with spatial gradients from MERFISH data.
== 121
What is the link between spatial variation in projection targets and graded gene expression? We answered this by measuring gene expression in LC-NE neurons retrogradely labeled from neocortex, cerebellum, or spinal cord (“retro-seq”). We embedded the gene expression from cells in each group into the low-dimensional space describing the population from snRNAseq ( Figure S11 ). Neurons projecting to each region occupied different parts of gene expression space ( Figure 3d ). Cortex-projecting neurons shared gene expression with dorsal LC-NE neurons, spinal cord-projecting neurons with ventral neurons, and cerebellum-projecting neurons were in between.
== 123
Retro-seq. a , GradientBoosting classifiers were trained on the retro-seq dataset (raw counts) to predict projection targets. b , Retro-seq cells embedded by PCA using the scVI normalized counts. Projection target labels were restricted to frontal cortex, cerebellum, and spinal cord. c , Right: projection targets were imputed onto snRNA-seq cells by k-nearest neighbor matching (k = 10). Cells were assigned by majority vote among labeled neighbors with ≥80% agreement; otherwise left unassigned. Left, inferred projection target; middle, imputation disagreement score (1 – nmax/nvalid,), where (nmax) is the count of the most frequent neighbor label and (nvalid) is the number of labelled neighbors (range 0–1). Only the first two subpanels of the three-panel display are shown.
== 125
## Retro-seq.
== 127
a , GradientBoosting classifiers were trained on the retro-seq dataset (raw counts) to predict projection targets. b , Retro-seq cells embedded by PCA using the scVI normalized counts. Projection target labels were restricted to frontal cortex, cerebellum, and spinal cord. c , Right: projection targets were imputed 
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 509,530p paper/*.txt; grep -n "more dorsal and" paper/*.txt | cut -c1-400; grep -n "VALUE NOT FOUND" -B30 tools/claims_check.py | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 209p paper/*.txt; sed -n 219,230p paper/*.txt | cut -c1-1500; grep -n -i "availability\|dandi\|github" paper/*.txt | cut -c1-600
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/AllenNeuralDynamics/LCNE-patchseq-figures.git 2>&1 | tail -2; cd LCNE-patchseq-figures && git checkout -q 79fa20a && ls -R code | head -40
```

```
code:
dandi_assets.py
data
ephys.py
example_traces.py
generate_S14jk.py
run
spikes.py

code/data:
LCNE_patchseq_S14_cell_table.csv
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/LCNE-patchseq-figures && cat code/spikes.py; grep -n "ttest\|welch\|equal_var\|contrast\|tau\|def \|Cortex\|Cerebellum\|Spinal" code/generate_S14jk.py | head -80; head -3 code/data/LCNE_patchseq_S14_cell_table.csv; ls; cat README* | head -60
```

```
"""Recompute representative spike waveforms from raw patch-seq sweeps."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from ephys import (
    CurrentClampSweep,
    NwbSource,
    list_current_clamp_sweeps,
    load_current_clamp_sweep,
)

LONG_SQUARE_RHEO_LABELS = ("X3LP_Rheo_DA_0", "X5LP_Rheo_DA_0")
SPIKE_THRESHOLD_MV = -10.0
SPIKE_WINDOW_MS = (-5.0, 10.0)

[... 276 more lines not kept]
```

**Agent**

Code at 79fa20a matches what the criterion says about waveform PC1 and the Welch tests. Now I'm checking where the time-constant sweep detail comes from, and the schema for `data`.

**Agent calls Bash**

```bash
cd $TMPDIR/LCNE-patchseq-figures && grep -rn "SubThresh\|SupraThresh\|tau" code/*.py README.md | head; cd  ls schemas* 2>/dev/null; grep -rn "with_inputs\|elsewhere" docs/protocol.md | head; grep -rln "checks" claims/*/ | head -3
```

```
code/example_traces.py:44:    "supra": "X4PS_SupraThresh_DA_0",
code/example_traces.py:46:    "hyperpol": "X1PS_SubThresh_DA_0",
code/generate_S14jk.py:297:    tau_groups = _group_values(frame, "membrane_time_constant_ms")
code/generate_S14jk.py:308:    tau_axis = figure.add_subplot(cdf_grid[1])
code/generate_S14jk.py:311:        tau_axis,
code/generate_S14jk.py:312:        tau_groups,
code/generate_S14jk.py:332:            tau_groups, "membrane_time_constant_ms"
README.md:44:IPFX analysis (`ipfx_tau` converted from seconds to milliseconds), rather than
attempt.schema.json
claims.schema.json
entry.schema.json
137:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
197:4. Decide what comes from outside the dataset. Data from elsewhere may be
206:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
207:     `with_inputs` and `elsewhere` claims are counted apart, each group on
231:   - `elsewhere` is for a claim whose data the dataset does not hold at
240:   - The notes of a `with_inputs` claim say which side a difference comes
251:     `data: elsewhere` instead (step 4).
claims/000005/10.1038-nn.4412.yaml
claims/000006/10.1038-s41586-018-0642-9.yaml
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 195,255p docs/protocol.md; tail -30 claims/000008/*.yaml; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:4000])" 2>/dev/null || ls schemas
```

```
why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
     the missing names are recorded as a finding (`metadata_insufficient`).
   - When outside data has to be matched to the dataset's cells, sessions
     or subjects, a claim of its own (`kind: link`) tests the link. Link
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd  awk 'NR>131 && NR<199 && length($0)>0 {print NR": "substr($0,1,90)}' paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Paragraph counts check out except fig5jk-pl-switch, which is paragraph 9, not 10. Making the edits now.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/001893/10.64898-2026.04.10.717727.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep("""  source: Results, Spatial variation of LC-NE activity during action-outcome learning, paragraph 10;
    Figure 5j, 5k""","""  source: Results, Spatial variation of LC-NE activity during action-outcome learning, paragraph 9;
    Figure 5j, 5k""")
rep("""  statistics:
  - about: respond against ignore t-statistics on location, linear model
    test: permutation test of linear regression
    statistic: R2 = 0.152
    p: 1.4e-3
    n: 103 cells, 15 mice
""","""  statistics:
  - about: respond against ignore t-statistics on location, linear model
    test: permutation test of linear regression
    statistic: R2 = 0.152
    p: 1.4e-3
    n: 103 cells, 15 mice
  - about: respond against ignore t-statistics on location, kNN
    test: kNN cross-validated permutation test
    statistic: R2 = 5.57e-2
    p: 8.4e-3
    n: 103 cells, 15 mice
""")
rep("""  statistics:
  - test: permutation test of linear regression
    statistic: R2 = 0.168
    p: 3.0e-4
    n: 114 cells, 15 mice
""","""  statistics:
  - about: switch against stay t-statistics on location, linear model
    test: permutation test of linear regression
    statistic: R2 = 0.168
    p: 3.0e-4
    n: 114 cells, 15 mice
  - about: switch against stay t-statistics on location, kNN (not significant)
    test: kNN cross-validated permutation test
    statistic: R2 = -4.96e-2
    p: 0.15
    n: 114 cells, 15 mice
""")
rep("""    variant. Two-sided Welch t-test (the code's; the legend's "paired" t-test cannot apply to
    independent groups), Student's t-test a variant. Reproduced""","""    variant. Two-sided Welch t-test (the code's; the legend's "paired" t-test cannot apply to
    independent groups), Student's t-test a variant. The IPFX settings are the reader's standard
    choice, not the paper's, so they cannot decide the outcome alone. The test is also run on the
    code's frozen values (the paper's own IPFX output); if that gives a different outcome from
    the recomputed values, the claim is blocked as methods_underspecified with both shown.
    Reproduced""")
rep("""    and per-cell values compared""","""    and per-cell values compared""") if False else None
# tau-cerebellum inherits by reference ("variants and test as in"); make explicit
rep("""  criterion: Time constants, cells, variants and test as in figs14k-tau-cortex-vs-spinal, cortex
    against cerebellum cells.""","""  criterion: Time constants, cells, variants, test and the rule on the frozen values as in
    figs14k-tau-cortex-vs-spinal, cortex against cerebellum cells.""")
rep("""- id: fig5jk-pl-switch""","""- id: fig5d-ignore-on-anatomy-axes
  statement: Respond against ignore t-statistics of LC-NE neurons, projected onto the primary
    spatial axes of axonal projections and of gene expression, correlate significantly with
    position along both axes.
  source: Results, Spatial variation of LC-NE activity during action-outcome learning, paragraph 7;
    Figure 5d legend
  quote: We found a significant mapping of cellular activity onto axonal projections and gene
    expression
  statistics:
  - about: position on the axonal projection axis
    statistic: r = 0.23
    p: 6.1e-3
    n: 103 cells, 15 mice
  - about: position on the gene expression axis
    statistic: r = 0.23
    p: 5.8e-3
    n: 103 cells, 15 mice
  expected:
  - quantity: r, axonal projection axis
    value: 0.23
    tolerance: 0.023
  - quantity: r, gene expression axis
    value: 0.23
    tolerance: 0.023
  depends_on:
  - fig5c-ignore-ventral
  - fig3e-axes-angle
- id: fig5h-switch-on-anatomy-axes
  statement: Switch against stay t-statistics of LC-NE neurons, projected onto the primary spatial
    axes of axonal projections and of gene expression, correlate significantly with position
    along both axes.
  source: Results, Spatial variation of LC-NE activity during action-outcome learning, paragraph 8;
    Figure 5h legend
  quote: Comparing again to the anatomy, we found spatial variation of switch versus stay activity
    relative to axonal projections and gene expression
  statistics:
  - about: position on the axonal projection axis
    statistic: r = 0.32
    p: 6.1e-5
    n: 114 cells, 15 mice
  - about: position on the gene expression axis
    statistic: r = 0.30
    p: 1.7e-4
    n: 114 cells, 15 mice
  expected:
  - quantity: r, axonal projection axis
    value: 0.32
    tolerance: 0.032
  - quantity: r, gene expression axis
    value: 0.3
    tolerance: 0.03
  depends_on:
  - fig5g-switch-dorsal
  - fig3e-axes-angle
- id: fig5jk-pl-switch""")
rep("""- id: fig6jk-pl-axons-rpe""","""- id: fig6h-outcome-groups-choice
  statement: Neurons correlated with RPE and neurons excited by lack of reward have opposing
    correlations with choice behaviour on the next trial.
  source: Results, Activity of LC-NE projections to frontal cortex correlates with reward prediction
    errors, paragraph 2; Figure 6h
  quote: Neurons that correlated with RPE or lack of reward had opposing correlations with choice
    behavior on subsequent trials
- id: fig6jk-pl-axons-rpe""")
rep("""- id: figs5-mapseq-consistent""","""- id: figs4dg-cortical-coprojection
  statement: Individual cortex-innervating LC-NE neurons send axons to nearby cortical regions,
    with no evidence of consistent targeting of separated but functionally related regions.
  source: Results, LC-NE projections are spatially organized, paragraph 4; Figure S4d to S4g
  quote: Individual cells tended to project to nearby regions, without evidence of individual cells
    consistently targeting spatially separated, but functionally related regions
- id: figs5-mapseq-consistent""")
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/001893/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Only the two known false alarms remain. Adding the checks entry.

**Agent calls Bash**

```bash
cd  cat >> claims/001893/10.64898-2026.04.10.717727.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Checker. The two VALUE NOT FOUND flags (fig5g-switch-dorsal and fig6a-outcome-space, 0.0003) are false alarms; the text prints "3.0 × 10 −4" in the Results paragraph 8 and the Figure 5g and 6a legends, confirmed by reading.
  - fig5jk-pl-switch. Source said paragraph 10; the section has nine paragraphs and the switch versus stay PL result is paragraph 9.
  - fig5c-ignore-ventral. Added the Figure 5c legend's kNN cross-validated test (R2 = 5.57e-2, p = 8.4e-3), which the paper reports for the same finding.
  - fig5g-switch-dorsal. Added the Figure 5g legend's kNN cross-validated test (R2 = -4.96e-2, p = 0.15, not significant), which the paper reports alongside the linear model; leaving it out overstated the support. Named the linear model entry with an about.
  - figs14k-tau-cortex-vs-spinal, figs14k-tau-cortex-vs-cerebellum. The IPFX settings are the reader's standard choice and could change the outcome, so they could not decide it alone; added that the test is also run on the code's frozen per-cell values and the claim is blocked as methods_underspecified when the two give different outcomes.
  - Added fig5d-ignore-on-anatomy-axes and fig5h-switch-on-anatomy-axes for coverage (Results paragraphs 7 and 8, Figure 5d and 5h legends); in vivo data, not tested on this dandiset.
  - Added fig6h-outcome-groups-choice and figs4dg-cortical-coprojection for coverage of findings stated in the Results with no claim; not tested on this dandiset.
  - Code checked. LCNE-patchseq-figures at 79fa20a, code/spikes.py and code/generate_S14jk.py, match what the waveform and time constant criteria say (rheobase sweep choice, eFEL-style peaks at -10 mV, -5 to 10 ms average, min-max over -2 to 4 ms, PCA over -3 to 6 ms, scipy ttest_ind with equal_var False).
  - Open. patchseq-ne-identity. The paper does not say how NE identity was confirmed; the marker readings (Dbh, or the four Figure S8c markers, detected at CPM > 0) are the reader's, and the NeMO collection is named only in the code's README, which says it was not used for the manuscript figures.
  - Open. The sweep inclusion criteria of the Methods need bridge balance, bias current and RMS noise per sweep; whether the dandiset holds them is the author's to find, and the code applies none.
  - Open. Minor supplementary findings have no claim (pupil correlations in Figure S16, axonal activity before ignored trials in Figure S17i, cross-correlogram PC1 in Figure S15t, go-cue and baseline anticorrelation in Figure 4h); none is a main finding or in this dandiset.
EOF
python tools/claims_check.py claims/001893/*.yaml paper/*.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file for DANDI:001893 and made the changes below. I think it is ready for an attempt. Nothing was committed or pushed, and only `claims/001893/` was changed.

**Checker result:** `29 claims, 29 quotes, 24 statistical values, 2 problems`

Both problems are false alarms. They flag the value 0.0003 in `fig5g-switch-dorsal` and `fig6a-outcome-space`, but the paper prints it as "3.0 × 10 −4" and the checker looks for "3 × 10-4". I confirmed both values by reading the Results and the Figure 5g and 6a legends.

**Changes, by claim:**
- **`fig5jk-pl-switch`:** the source said paragraph 10. The section has nine paragraphs, and this result is in paragraph 9.
- **`fig5c-ignore-ventral`:** added the kNN cross-validated test from the Figure 5c legend (R2 = 5.57e-2, p = 8.4e-3), which the paper reports for the same finding.
- **`fig5g-switch-dorsal`:** added the kNN cross-validated test from the Figure 5g legend (R2 = -4.96e-2, p = 0.15). It is not significant, so leaving it out overstated the support.
- **`figs14k-tau-cortex-vs-spinal` and `figs14k-tau-cortex-vs-cerebellum`:** the IPFX settings are the first reader's own standard choice and could change the outcome. The test now also runs on the code's frozen per-cell values (the paper's own IPFX output). If the two give different outcomes, the claim is blocked as `methods_underspecified`.
- **New claims for coverage**, none testable on this dandiset:
  - `fig5d-ignore-on-anatomy-axes` and `fig5h-switch-on-anatomy-axes` (the r and p values from the Figure 5d and 5h legends)
  - `fig6h-outcome-groups-choice`
  - `figs4dg-cortical-coprojection`
- **Code:** I read `LCNE-patchseq-figures` at commit 79fa20a. Its `spikes.py` and `generate_S14jk.py` do what the waveform and time-constant criteria describe, including the two-sided Welch t-test.

The other claims match the paper: statements, sources, quotes, statistics and tolerances. The cell counts in `fig4g` are correctly left without statistics, because the t-test there only counts cells.

**Still open:**
- **`patchseq-ne-identity`:** the paper does not say how NE identity was confirmed. The marker readings in the criterion (Dbh, or four marker genes, detected at CPM > 0) are the first reader's own. The NeMO transcriptome collection is named only in the code's README, which says it was not used for the paper's figures.
- **Sweep inclusion:** the Methods' criteria need per-sweep bridge balance, bias current and noise. Whether the dandiset holds these is for the author to find out; the code applies none of them.
- **Minor findings without a claim:** the pupil results in Figure S16, Figures S15t and S17i, and Figure 4h. None is a main finding or in this dandiset.

**Ready:** yes. The checks entry is recorded with `ready: true`.

## End of run

18 turns, 3 minutes, result: success.
