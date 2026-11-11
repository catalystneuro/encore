# saez-2016 · claims · run 42876250360

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; ls paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 43,
 "limit": 157
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
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml; cat paper/pvc-9.data-description.txt; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pone.0147642.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/saez-2016.yaml 2>/dev/null; grep -l "archive: crcns" claims/*.yaml | head -3; f=$(grep -l "archive: crcns" claims/*.yaml | head -1); sed -n 1,60p $f; grep -n "open\|reading" $f | head -20
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1371/journal.pone.0147642
title: Role of GABAA-Mediated Inhibition and Functional Assortment of Synapses onto Individual Layer 4
  Neurons in Regulating Plasticity Expression in Visual Cortex
datasets:
- archive: crcns
  id: pvc-9
  relation: primary
claims/bruno-2017.yaml
claims/deweese-2004.yaml
claims/eyherabide-2008.yaml
# Claims for Bruno, Frost & Humphries (2017), eLife 6:e27342, "A spiral attractor network drives
# rhythmic locomotion", doi:10.7554/elife.27342, on CRCNS data set apl-1 (doi:10.6080/K0SN074B).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record (PMC5546814, open access), as JATS XML flattened to text under
# paper/: main text, Materials and methods, and the legends of Figures 1 to 8 and of all twelve
# figure supplements. The paper has no other supplementary file. No PDF of the paper was supplied,
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,100p claims/bruno-2017.yaml; tail -5 claims/bruno-2017.yaml; python tools/claims_check.py -h 2>&1 | head
```

```
# responses, "programs"), each evoked by 8 V, 5 ms pulses at 20 Hz for 2.5 s to pedal nerve 9 at
# 30 s into a recording of about 125 s (30 s spontaneous, about 95 s evoked); stimulation
# intervals of 15 and 60 min. The same neurons were tracked across the three bouts of a
# preparation; the paper gives 120 to 180 neurons per recording and 1131 neurons in all
# (Figure 7B). Extracellular P10 nerve recordings for all three bouts in 3 preparations (nine
# responses). Neuron (x, y) positions on the array, reconstructed for 8 preparations (4 left,
# 4 right ganglia). The data set's description says it holds spike times of the 30 recordings,
# the P10 channel where recorded, and neuron location maps; so all claims use the data set.
# The data set's description gives 75 to 160 neurons per preparation, against the paper's 120 to
# 180 (claim dataset-size).
#
# Not made into claims: the three-neuron model of Figure 1, figure supplement 1 (a simulation, no
# data), and Figure 2, figure supplement 1, which describes the range of dynamics without a finding
# beyond the claims below.
schema_version: 2
dataset:
  archive: crcns
  id: apl-1
  doi: 10.6080/K0SN074B
paper: doi:10.7554/elife.27342
[... 36 more lines not kept]
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
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=0)[:4000]); print(list(s['properties']))"
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
[... 83 more lines not kept]
```

**Agent**

The paper is the version of record from PMC, with full Methods. It has no supplement and links no code. I'm writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/saez-2016.yaml",
 "content": "# Claims for Saez & Friedlander (2016), PLoS One 11(2):e0147642, \"Role of GABAA-Mediated\n# Inhibition and Functional Assortment of Synapses onto Individual Layer 4 Neurons in Regulating\n# Plasticity Expression in Visual Cortex\", doi:10.1371/journal.pone.0147642, on CRCNS data set\n# pvc-9 (doi:10.6080/K00V89R6).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record (PMC4739708, open access), as JATS XML flattened to text under\n# paper/: main text, Methods, and the legends of Figures 1 to 3. The paper has no supporting\n# information files. No PDF was supplied; no claim rests on a number shown only in a figure. The\n# flattened text prints each figure legend twice; sources cite the legend by panel.\n# Code: the paper links none. The simulations were run in R (Methods, Input mixing simulation) and\n# their code is not given. Every method below is from the Methods, Results or legends, or is named\n# as open. The data set's description (paper/pvc-9.data-description.txt) was read only to know\n# what the data set holds; no claim comes from it.\n#\n# Data the paper used. Acute coronal slices (300 um) of visual cortex from tri-color guinea pigs,\n# p6 to p14. Whole-cell recordings from layer 4 regular-spiking (excitatory) neurons, 20 kHz,\n# filtered at 4 kHz. Extracellular stimulation (ECS, 50 us pulse) by an electrode in L4 placed\n# 100 to 150 um lateral to the cell, intensity set (typically 20 to 30 uA) for a response of 3 to\n# 5 mV (current clamp) or 350 to 400 pA (voltage clamp). Baseline of 120 stimuli at 0.2 Hz (10\n# min); pairing of 60 trials at 0.1 Hz, each a current step giving 6 to 9 action potentials whose\n# onset leads the ECS pulse by 10 ms, in current clamp; then at least 10 more minutes of testing\n# in the original mode. Three groups. Control (intact inhibition), 28 cells, 14 in current clamp\n# (EPSPs) and 14 in voltage clamp (EPSCs). Bicuculline (2 uM, slices pre-incubated over 1 h and\n# perfused), voltage clamp, 26 cells in the Results (27 in the Methods). Quality control discarded\n# 32 recordings (9 I-clamp and 11 V-clamp control, 12 bicuculline) for input resistance changes,\n# unstable baseline or access resistance over 40 MOhm, over 20% of input resistance, or changing\n# by more than 20%. The measured variable is the peak amplitude of the evoked postsynaptic\n# response (PSR) per sweep. Figure 3 also uses the authors' earlier single-cell stimulation (SCS)\n# data of paired L4-L4 recordings (their reference 17; n = 42 in the Methods, 43 in the Results),\n# which this data set does not hold and whose location the paper does not give.\n#\n# Shared method, from the Methods (Plasticity induction) and the Results (Extracellular\n# stimulation, paragraph 1). Per cell, the PSR peak amplitude of each sweep; the pre-pairing epoch\n# is the 120 baseline sweeps; the change is the post-pairing mean over the pre-pairing mean minus\n# 1, in percent. A cell is LTP (LTD) when a Student's t-test of pre against post amplitudes gives\n# p < 0.05 and the change exceeds +15% (is below -15%); otherwise NC. Cells are those the paper\n# included; where the data set marks inclusion, that marking is used, otherwise the Methods'\n# quality control. The paper's \"mean +/- x\" values across cells are mean and SD: the control\n# V-clamp and I-clamp values (-5.67 +/- 9.47 and -1.41 +/- 10.92, n = 14 each) pool exactly to\n# the Figure 1B legend's -3.53 +/- 10.26 only as SDs, and the bicuculline subgroup means pool to\n# -3.7, the Figure 2B legend's -3.8.\n#\n# Details the paper leaves open, each of which could change a cell's class, named in the\n# criteria as readings. (P) The post-pairing window: (a) all post-pairing sweeps; (b) the first\n# 10 min (120 sweeps) after pairing; (c) the last 10 min recorded. (T) The per-cell t-test:\n# (a) two-sample Student's t-test (equal variance) on sweep amplitudes; (b) the same on the\n# 1-min bin means the time plots use (Figure 1B, 60 s bins). (M) The peak measure: the paper says\n# peak amplitude and nothing of baseline or search window. Fixed here as a standard choice, the\n# peak of the deflection in the PSR's sign (depolarizing for EPSPs, inward for EPSCs) from the\n# end of the stimulus artifact to 50 ms after the stimulus, less the mean of the 10 ms before\n# the stimulus; a 30 ms search window is a variant. A claim is reproduced when it holds under\n# one combination of (P) and (T) readings, with every combination shown, except claims of\n# absence, which are judged on the paper's test as named.\n#\n# Inconsistencies in the text, each named in the claims it touches. The Results' Dataset\n# paragraph calls the bicuculline cells I-clamp; the Methods (V-clamp, n = 27) and Figure 2\n# (EPSCs) say voltage clamp, read here. The Results' Extracellular stimulation paragraph gives the\n# combined control change as -3.8 +/- 34.3%, and the bicuculline paragraph labels -3.8 +/- 34.3%\n# as \"presence\" with Figure 1B and -3.5 +/- 10.3% as \"absence\" with Figure 2B; the figure legends\n# and the arithmetic above put -3.53 +/- 10.26% with control (Figure 1B) and -3.8 +/- 34.3% with\n# bicuculline (Figure 2B), read here. The Results cite the control histogram as Figure 1A; its\n# legend is Figure 1C. The Figure 3A legend colours ECS yellow and ECS with bicuculline green;\n# the Results call the control comparison green and the bicuculline one yellow; the p-values are\n# assigned to groups by the Results' words, not the colours.\nschema_version: 2\npaper: doi:10.1371/journal.pone.0147642\nclaims:\n- id: dataset-size\n  statement: Plasticity was analysed in 28 control cells (14 in voltage clamp, 14 in current\n    clamp) and 26 cells with 2 uM bicuculline in the bath.\n  source: Results, Dataset, paragraph 1; Methods, Electrophysiology\n  quote: We analyzed the plasticity outcomes in response to a Hebbian pairing protocol of L4\n    excitatory cell afferents using ECS in the absence (n = 28; n = 14 in V-clamp, n = 14 in\n    I-clamp) and presence (n = 26, I-clamp) of 2μM bicuculline in the bath.\n  expected:\n  - quantity: control cells in voltage clamp\n    value: 14\n    tolerance: 0\n  - quantity: control cells in current clamp\n    value: 14\n    tolerance: 0\n  - quantity: bicuculline cells\n    value: 26\n    tolerance: 0\n  criterion: Counts of the cells included in the paper, zero tolerance as they are counts of what\n    was deposited. The bicuculline cells are voltage clamp (Methods, Figure 2), though this\n    sentence says I-clamp. The Methods give 27 bicuculline cells; a count of 27 is partially\n    reproduced. The discarded recordings (9 I-clamp, 11 V-clamp control, 12 bicuculline;\n    Methods) are counted and reported where the data set holds them.\n- id: fig1c-control-outcomes\n  statement: With inhibition intact, few cells showed plasticity after pairing; 1 of 28 underwent\n    LTP, 3 of 28 LTD and 24 of 28 no change.\n  source: Figure 1C legend; Results, Extracellular stimulation, paragraph 1 (cited there as Fig 1A)\n  quote: LTD cells (n = 3/28) are shown as blue bars; a single LTP cell (n = 1/28) is shown as a\n    red bar; grey bars indicate cells whose strength did not change after pairing (n = 24/28).\n  expected:\n  - quantity: control LTP cells\n    value: 1\n    tolerance: 0\n  - quantity: control LTD cells\n    value: 3\n    tolerance: 0\n  - quantity: control NC cells\n    value: 24\n    tolerance: 2.4\n  depends_on:\n  - dataset-size\n  criterion: Classification as in the opening comment (t-test p < 0.05 and change beyond +/-15%,\n    Methods, Plasticity induction), on the 28 included control cells. Reproduced when, under one\n    reading of (P) and (T), the counts are 1 LTP, 3 LTD and 24 NC; partially reproduced when the\n    plastic cells (LTP plus LTD) number 2 to 6 and NC is within tolerance; not reproduced\n    otherwise. Every reading's counts are shown.\n- id: fig1-control-no-net-plasticity\n  statement: Over the 28 control cells, pairing gave no net plasticity of EPSPs or EPSCs.\n  source: Results, Extracellular stimulation, paragraph 1; Figure 1B\n  quote: overall the pairing protocol resulted in no net plasticity of EPSPs (recorded under\n    current clamp) or EPSCs (under voltage clamp) for the population of cells studied (n = 28;\n    p>0.8, Student’s t-test, Fig 1A ).\n  statistics:\n  - test: Student's t-test\n    p: 0.8\n    p_relation: \">\"\n    n: 28 control cells\n  depends_on:\n  - dataset-size\n  criterion: A claim of absence, judged on the paper's Student's t-test at p < 0.05. The paper\n    does not say which form; the readings it allows are (a) a one-sample t-test of the 28\n    percent changes against 0, and (b) a paired t-test of each cell's pre against post mean\n    amplitude, normalized to the pre mean. Reproduced when the test does not reach p < 0.05;\n    not reproduced when it does. The mean change and p are reported. A one-sample test on the\n    paper's own mean and SD (-3.53 +/- 10.26%, n = 28) gives p near 0.08, so the printed p >\n    0.8 is not expected to be matched.\n- id: fig1-control-mean-change\n  statement: The mean change in PSR after pairing was -5.67 +/- 9.47% in voltage clamp, -1.41 +/-\n    10.92% in current clamp, and -3.53 +/- 10.26% over all 28 control cells.\n  source: Results, Extracellular stimulation, paragraph 1; Figure 1B legend\n  quote: The net change in the compound postsynaptic response (PSR) was -5.67±9.47% in V-clamp\n    and -1.41±10.92 in I-clamp.\n  expected:\n  - quantity: V-clamp mean change\n    value: -5.67\n    tolerance: 2.53\n    unit: percent\n  - quantity: I-clamp mean change\n    value: -1.41\n    tolerance: 2.92\n    unit: percent\n  - quantity: combined control mean change (Figure 1B legend)\n    value: -3.53\n    tolerance: 1.94\n    unit: percent\n  - quantity: combined control SD of change\n    value: 10.26\n    tolerance: 1.03\n    unit: percent\n  depends_on:\n  - dataset-size\n  criterion: Per-cell change as in the opening comment. The tolerance of each mean is its\n    standard error from the paper's SD and n (SD over the square root of 14 or 28), the\n    paper's own uncertainty of a mean; the SD has 10%. Reproduced when, under one reading of (P),\n    all four values are within tolerance; partially reproduced when the three means are. The\n    Results' \"combined ... EPSR change = -3.8±34.3%\" is the bicuculline value (Figure 2B\n    legend) and is not used here.\n- id: fig1-vc-ic-same\n  statement: Voltage-clamp and current-clamp control outcomes did not differ; both were Gaussian,\n    and their means and variances did not differ, so the two were combined.\n  source: Results, Extracellular stimulation, paragraph 1\n  quote: both were Gaussian (p = 0.79 and p = 0.85 respectively, Shapiro-Wilks test) and their\n    means and variances did not differ (p = 0.28, Student’s t-test; p = 0.61, Fisher’s F-test,\n    respectively)\n  statistics:\n  - about: normality of V-clamp changes\n    test: Shapiro-Wilk test\n    p: 0.79\n    n: 14 V-clamp cells\n  - about: normality of I-clamp changes\n    test: Shapiro-Wilk test\n    p: 0.85\n    n: 14 I-clamp cells\n  - about: V-clamp against I-clamp means\n    test: Student's t-test\n    p: 0.28\n    n: 14 and 14 cells\n  - about: V-clamp against I-clamp variances\n    test: Fisher's F-test\n    p: 0.61\n    n: 14 and 14 cells\n  depends_on:\n  - fig1-control-mean-change\n  criterion: Claims of absence, judged on the paper's tests at p < 0.05 on the per-cell percent\n    changes; Shapiro-Wilk on each group, a two-sample Student's t-test (equal variance) and a\n    two-sided F-test of the variance ratio between groups. Reproduced when none of the four\n    tests reaches p < 0.05 under a reading of (P) (the readings change the values tested, not\n    the test); not reproduced when any does in every reading. The p-values are reported.\n- id: fig1fh-control-no-dependence-on-initial\n  statement: In control cells the plasticity outcome did not depend on the initial synaptic\n    strength, in current clamp or in voltage clamp.\n  source: Figure 1F and 1H legend; Results, Extracellular stimulation, paragraph 1\n  quote: Scatterplot showing lack of correlation between the initial recorded synaptic strength\n    under I-clamp (EPSP) and the plasticity outcome (p>0.9). (G-H) As (E-F), for V-clamp\n    experiments (p>0.1).\n  statistics:\n  - about: I-clamp, initial EPSP against change\n    test: correlation\n    p: 0.9\n    p_relation: \">\"\n    n: 14 I-clamp cells\n  - about: V-clamp, initial EPSC against change\n    test: correlation\n    p: 0.1\n    p_relation: \">\"\n    n: 14 V-clamp cells\n  depends_on:\n  - fig1-control-mean-change\n  criterion: A claim of absence. The paper names only a correlation; the test is fixed here as\n    the Pearson correlation of the pre-pairing mean amplitude against the percent change, per\n    clamp mode, at p < 0.05, with Spearman's rank correlation shown as a variant. Reproduced\n    when neither mode reaches p < 0.05; not reproduced when either does. r and p are reported.\n- id: fig1d-example-nc\n  statement: A representative current-clamp control cell showed no plasticity (EPSP change -1 +/-\n    0.1%, p = 0.48).\n  source: Figure 1D; Results, Extracellular stimulation, paragraph 1\n  quote: Fig 1D shows a representative example I-clamp experiment in which no plasticity was\n    induced (EPSP change = -1±0.1%, p = 0.48, Student’s t-test).\n  statistics:\n  - test: Student's t-test\n    p: 0.48\n    n: one I-clamp cell\n  expected:\n  - quantity: example EPSP change\n    value: -1\n    tolerance: 0.1\n    unit: percent\n  criterion: The paper does not say which cell is shown. Reproduced when, under one reading of (P)\n    and (T), at least one included I-clamp control cell has a change within tolerance and a\n    t-test p of 0.05 or more; the closest cell's change and p are reported either way.\n- id: fig2a-bicuculline-outcomes\n  statement: With GABAA receptors blocked by 2 uM bicuculline, more cells changed after pairing\n    (16 of 26), with outcomes of both signs; 7 of 26 underwent LTP, 9 of 26 LTD and 10 of 26 no\n    change.\n  source: Results, Extracellular stimulation in the presence of 2μM bicuculline, paragraph 1;\n    Figure 2A legend\n  quote: Under these conditions, a greater proportion of cells underwent changes in synaptic\n    response after pairing (16/26, or 63%). There was heterogeneity in the sign of the\n    plasticity outcome, with 7/26 (27%) of cells undergoing LTP ... and 9/26 (35%) of cells\n    undergoing LTD ... In a third subset of cells, no significant change in the evoked EPSC\n    occurred (10/26 or 38.5%\n  expected:\n  - quantity: bicuculline LTP cells\n    value: 7\n    tolerance: 0.7\n  - quantity: bicuculline LTD cells\n    value: 9\n    tolerance: 0.9\n  - quantity: bicuculline NC cells\n    value: 10\n    tolerance: 1\n  depends_on:\n  - dataset-size\n  criterion: Classification as in the opening comment on the 26 included bicuculline cells; the\n    tolerances (10%) make the counts exact. Reproduced when, under one reading of (P) and (T),\n    the counts are 7, 9 and 10; partially reproduced when LTP and LTD are each within 2 of the\n    paper and both are present. The paper's 63% is 16/26 rounded up (61.5%).\n- id: bicuculline-increases-plastic-fraction\n  statement: Blocking GABAA inhibition raised the fraction of cells with plasticity from 4 of 28\n    to 16 of 26, showing that inhibition limits plasticity induction onto L4 cells.\n  source: Discussion, Summary, paragraph 1\n  quote: With intact inhibition, a very small fraction of cells underwent a plastic change by our\n    criteria (n = 4/28; LTP in 1/28 and LTD in 3/28 cells). This proportion was considerably\n    increased when inhibition was abolished (n = 16/26; LTP in 7/26 and LTD in 9/26 cells)\n  expected:\n  - quantity: control cells with plasticity\n    value: 4\n    tolerance: 0.4\n  - quantity: bicuculline cells with plasticity\n    value: 16\n    tolerance: 1.6\n  depends_on:\n  - fig1c-control-outcomes\n  - fig2a-bicuculline-outcomes\n  criterion: The paper reports no test of the two proportions. Reproduced when, under the same\n    reading of (P) and (T) for both groups, the bicuculline fraction of LTP plus LTD cells is\n    larger than the control fraction and both counts are within tolerance; partially reproduced\n    when the bicuculline fraction is larger but a count is outside tolerance. A two-sided\n    Fisher's exact test of the two proportions is shown as a variant, chosen here.\n- id: fig2-subgroup-changes\n  statement: In bicuculline, LTP cells changed by +39.9 +/- 14.7%, LTD cells by -38.5 +/- 20.4%,\n    and NC cells by -3.0 +/- 7.6% on average.\n  source: Results, Extracellular stimulation in the presence of 2μM bicuculline, paragraph 1\n  quote: 7/26 (27%) of cells undergoing LTP (average LTP EPSC change = +39.9±14.7%) and 9/26 (35%)\n    of cells undergoing LTD (average LTD EPSC change = -38.5±20.4%). In a third subset of cells,\n    no significant change in the evoked EPSC occurred (10/26 or 38.5%; average change = -3.0\n    ±7.6%)\n  expected:\n  - quantity: mean change of LTP cells\n    value: 39.9\n    tolerance: 5.56\n    unit: percent\n  - quantity: mean change of LTD cells\n    value: -38.5\n    tolerance: 6.8\n    unit: percent\n  - quantity: mean change of NC cells\n    value: -3.0\n    tolerance: 2.4\n    unit: percent\n  depends_on:\n  - fig2a-bicuculline-outcomes\n  criterion: Means over the cells of each class from claim fig2a-bicuculline-outcomes, under the\n    same reading. Tolerances are the standard errors from the paper's SD and n (n = 7, 9, 10).\n    Reproduced when all three are within tolerance under one reading; partially reproduced when\n    two are.\n- id: fig2-mean-unchanged-variance-increased\n  statement: The mean change over all cells did not differ between bicuculline (-3.8 +/- 34.3%)\n    and control (-3.5 +/- 10.3%), but the variance of plasticity outcomes was significantly\n    larger in bicuculline.\n  source: Results, Extracellular stimulation in the presence of 2μM bicuculline, paragraph 1;\n    Figure 1B and Figure 2B legends\n  quote: whereas the mean EPSC change of all experiments (n = 26) was not different in the\n    presence (-3.8±34.3%; average time plot shown in Fig 1B ) or absence (-3.5±10.3%; average\n    time plot shown in Fig 2B ) of bicuculline (p = 0.97, Student’s t-test), the variance of\n    synaptic plasticity changes was significantly increased in bicuculline compared to control\n    (p<0.01, Fisher’s test)\n  statistics:\n  - about: bicuculline against control means\n    test: Student's t-test\n    p: 0.97\n    n: 26 bicuculline and 28 control cells\n  - about: bicuculline against control variances\n    test: Fisher's F-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 26 bicuculline and 28 control cells\n  expected:\n  - quantity: bicuculline mean change (Figure 2B legend)\n    value: -3.8\n    tolerance: 6.73\n    unit: percent\n  - quantity: bicuculline SD of change\n    value: 34.3\n    tolerance: 3.43\n    unit: percent\n  depends_on:\n  - fig1-control-mean-change\n  - fig2a-bicuculline-outcomes\n  criterion: Per-cell changes as in the opening comment, 26 bicuculline against 28 control\n    cells. The text swaps the figure references and the labels \"presence\" and \"absence\"; the\n    legends put -3.8 +/- 34.3% with bicuculline (Figure 2B) and -3.53 +/- 10.26% with control\n    (Figure 1B). The mean's tolerance is its standard error (34.3 over the square root of 26),\n    the SD's 10%. The equal means are a claim of absence, judged on a two-sample Student's\n    t-test (equal variance) at p < 0.05. Reproduced when, under one reading of (P), the t-test\n    does not reach p < 0.05, a two-sided F-test of the variance ratio gives p < 0.01 with the\n    bicuculline variance larger, and both values are within tolerance; partially reproduced\n    when the two tests hold but a value is outside tolerance.\n- id: fig2cd-example-ltp-ltd\n  statement: Representative bicuculline cells underwent LTP (+59.4 +/- 26%, p < 0.001) and LTD\n    (-37.6 +/- 19.9%, p < 0.001).\n  source: Figure 2C and 2D; Results, Extracellular stimulation in the presence of 2μM\n    bicuculline, paragraph 1\n  quote: For these connections, the change in strength was +59.4±26% for the LTP case (p<0.001,\n    Student’s t-test; Fig 2C ) and -37.6±19.9% for the LTD case (p<0.001, Student’s t-test; Fig\n    2D ).\n  statistics:\n  - about: example LTP cell\n    test: Student's t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: one cell\n  - about: example LTD cell\n    test: Student's t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: one cell\n  expected:\n  - quantity: example LTP change\n    value: 59.4\n    tolerance: 5.94\n    unit: percent\n  - quantity: example LTD change\n    value: -37.6\n    tolerance: 3.76\n    unit: percent\n  criterion: The paper does not say which cells are shown. The +/- values are a spread over\n    sweeps, not an uncertainty of the change, so the tolerances are 10%. Reproduced when, under\n    one reading of (P) and (T), one included bicuculline cell has a change within the LTP\n    tolerance and another within the LTD tolerance, each with t-test p < 0.001; partially\n    reproduced when one of the two is found. The closest cells are reported either way.\n- id: fig2f-bicuculline-no-dependence-on-initial\n  statement: In bicuculline the plasticity outcome did not depend on the initial synaptic\n    strength.\n  source: Figure 2E and 2F legend; Results, Extracellular stimulation in the presence of 2μM\n    bicuculline, paragraph 1\n  quote: We did not observe a dependency of plasticity outcomes on initial synaptic response ( Fig\n    2E and 2F ; p>0.5).\n  statistics:\n  - about: Results\n    test: correlation\n    p: 0.5\n    p_relation: \">\"\n    n: 26 bicuculline cells\n  - about: Figure 2F legend\n    test: correlation\n    p: 0.3\n    p_relation: \">\"\n    n: 26 bicuculline cells\n  depends_on:\n  - fig2a-bicuculline-outcomes\n  criterion: A claim of absence, judged as claim fig1fh-control-no-dependence-on-initial (Pearson\n    correlation of pre-pairing mean EPSC amplitude against percent change, p < 0.05, fixed here;\n    Spearman as a variant). Reproduced when p is 0.05 or more; not reproduced otherwise. The\n    Results give p > 0.5 and the legend p > 0.3; both are reported against the value found.\n- id: fig3a-ks-scs-vs-ecs\n  statement: The cumulative distribution of plasticity outcomes of single-cell stimulation differs\n    from that of ECS with intact inhibition, but not from that of ECS in bicuculline.\n  source: Results, Mixing of unitary L4-L4 inputs, paragraph 1; Figure 3A\n  quote: The cumulative distributions are different when the plasticity outcomes from SCS\n    experiments were compared to the ECS experiments performed in regular aCSF (green line;\n    p<0.001, Kolmogorov-Smirnov test), but not when compared to the ECS experiments with bath\n    application of 2μM bicuculline (yellow line; p = 0.16, Kolmogorov-Smirnov test).\n  statistics:\n  - about: SCS against control ECS\n    test: Kolmogorov-Smirnov test\n    p: 0.001\n    p_relation: \"<\"\n    n: 42 or 43 SCS connections and 28 control ECS cells\n  - about: SCS against bicuculline ECS\n    test: Kolmogorov-Smirnov test\n    p: 0.16\n    n: 42 or 43 SCS connections and 26 bicuculline ECS cells\n  data: with_inputs\n  depends_on:\n  - fig1-control-mean-change\n  - fig2-mean-unchanged-variance-increased\n  criterion: Needs the per-connection normalized strength changes of the SCS data of the paper's\n    reference 17, which the data set does not hold and the paper does not locate. Two-sample\n    two-sided Kolmogorov-Smirnov tests of the ECS percent changes against the SCS changes.\n    Groups are assigned by the Results' words (regular aCSF, bicuculline), as the Figure 3A\n    legend's colours are the reverse. Reproduced when, under one reading of (P), SCS against\n    control gives p < 0.001 and SCS against bicuculline p of 0.05 or more (a claim of absence\n    at the usual threshold); partially reproduced when the first gives p < 0.05 only.\n- id: fig3c-random-mixing-narrower\n  statement: Simulated compound responses built by random mixing of unitary L4-L4 connections\n    (18.05 +/- 6.19 inputs each) give a distribution of strength changes significantly narrower\n    than both the ECS (bicuculline) and the SCS data, so random independent mixing would not\n    produce the plasticity seen with ECS in bicuculline.\n  source: Results, Mixing of unitary L4-L4 inputs, paragraph 1; Figure 3C; Methods, Input\n    mixing simulation\n  quote: We found that the distribution of SCR Δ N Strengths was significantly narrower than that\n    of either ECS (p<0.001, Fisher’s F-test) or SCS (p<0.001, Fisher’s F-test) experimental data\n    ( Fig 3C ).\n  statistics:\n  - about: SCR (S = 0) against ECS in bicuculline variances\n    test: Fisher's F-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 26 SCRs and 26 ECS cells\n  - about: SCR (S = 0) against SCS variances\n    test: Fisher's F-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 26 SCRs and 43 SCS connections\n  expected:\n  - quantity: mean number of inputs per SCR\n    value: 18.05\n    tolerance: 1.21\n  data: with_inputs\n  depends_on:\n  - fig2-mean-unchanged-variance-increased\n  criterion: Needs the SCS pre- and post-pairing strengths (in pA) of reference 17, not in the\n    data set. As the Methods give it, connections drawn from the SCS database until their summed\n    pre-pairing strength is 350 pA or more; SCR pre and SCR post are the summed pre and post\n    strengths; the change is SCR post over SCR pre minus 1; 26 SCRs; F-tests of SCR variance\n    against the 26 bicuculline ECS changes and the SCS changes. The ECS group is bicuculline\n    (the Results compare with ECS, n = 26). Open, with readings. Sampling with replacement (a)\n    or without replacement within an SCR (b). The random seed can change a run of 26, so\n    (i) one run with a standard seed, and (ii) 1000 runs of 26, judged by the share of runs\n    with p < 0.001. The tolerance of the input count is the standard error of the paper's mean\n    (6.19 over the square root of 26). Reproduced when, under one reading, both F-tests give\n    p < 0.001 with the SCR variance smaller (in (ii), in more than half of runs) and the input\n    count is within tolerance; partially reproduced when both give p < 0.05.\n- id: fig3b-segregation-near-complete\n  statement: Adding a segregation parameter S that biases each SCR's connections toward the\n    plasticity class of the first, the SCR distribution broadens with S, and only for S of 0.9\n    or more does its variance not differ from that of ECS in bicuculline; segregation of inputs\n    by plasticity state would have to be almost complete.\n  source: Results, Mixing of unitary L4-L4 inputs, paragraph 1; Figure 3B and 3D; Methods, Input\n    mixing simulation\n  quote: We found that for most S values, the variance of the SCRs is lower (p≤0.05, Fisher’s\n    F-test); only for values of S≥0.9 was there no significant difference in variance between\n    the SCR and ECS Δ N Strength distributions (p>0.05, Fisher’s F-test).\n  statistics:\n  - about: SCR against ECS in bicuculline variances, S below 0.9 (printed as p≤0.05)\n    test: Fisher's F-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 26 SCRs and 26 ECS cells per S value\n  - about: SCR against ECS in bicuculline variances, S of 0.9 and 1\n    test: Fisher's F-test\n    p: 0.05\n    p_relation: \">\"\n    n: 26 SCRs and 26 ECS cells per S value\n  data: with_inputs\n  depends_on:\n  - fig3c-random-mixing-narrower\n  criterion: The simulation of claim fig3c-random-mixing-narrower for S from 0 to 1 in steps of\n    0.1. At S = 0 the class probabilities are the SCS proportions (7/43 LTP, 18/43 NC, 18/43\n    LTD, Results); at S = 1 every connection after the first is drawn from the first's class.\n    The Methods say only that between these the probability of a same-class connection rises\n    linearly; read here as P(same) = p + S(1 - p), with the other two classes sharing 1 -\n    P(same) in their SCS proportions, the reading the text allows. The readings of claim\n    fig3c-random-mixing-narrower (replacement; one run or 1000 runs) apply. Reproduced when the\n    F-test against the bicuculline ECS changes gives p of 0.05 or less for every S up to 0.8\n    (in (ii), the median p over runs) and above 0.05 for S of 0.9 and 1; partially reproduced\n    when the smallest S without a difference is 0.7 or more and the SCR SD increases with S.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/saez-2016.yaml paper/10.1371-journal.pone.0147642.txt; grep -nE "^[^#]*[^\"']: .*: " claims/saez-2016.yaml | head; grep -n "—\|rather" claims/saez-2016.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE "^ +[^-#][^:]*: " claims/saez-2016.yaml | grep -vE "^[0-9]+: +[a-z_]+: " | head; grep -c "criterion:" claims/saez-2016.yaml; grep -c "  - test:\|    test:" claims/saez-2016.yaml
```

```
78:  - quantity: control cells in voltage clamp
81:  - quantity: control cells in current clamp
84:  - quantity: bicuculline cells
99:  - quantity: control LTP cells
102:  - quantity: control LTD cells
105:  - quantity: control NC cells
122:  - test: Student's t-test
142:  - quantity: V-clamp mean change
146:  - quantity: I-clamp mean change
150:  - quantity: combined control mean change (Figure 1B legend)
16
20
```

**Agent calls Bash**

```bash
grep -nE ": " claims/saez-2016.yaml | grep -vE "^[0-9]+:#" | grep -vE "^[0-9]+: *(- )?[a-z_]+: " | head
```

```
(Bash completed with no output)
```

**Agent**

I wrote `claims/saez-2016.yaml`, and the quote checker passes it: 16 claims, 16 quotes, 20 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record (PMC4739708, open access), flattened from JATS XML: main text, Methods and the legends of Figures 1 to 3. The paper has no supplement and links no code. Its simulations were run in R, but the code is not given. No PDF was needed. I read the dataset's description only to see what the dataset holds.

**Claims:** all 16 have a quote, 10 have statistics and 16 have a criterion. They cover:
- the cell counts;
- control outcomes (1 LTP, 3 LTD and 24 no change out of 28), no net plasticity, and the mean changes by recording mode;
- voltage-clamp and current-clamp results being the same;
- no dependence on initial strength, in control and in bicuculline;
- the example cells in Figure 1D and Figures 2C and 2D;
- bicuculline outcomes (7 LTP, 9 LTD, 10 no change out of 26) and the mean change in each of those groups;
- bicuculline raising the share of cells that change, from 4/28 to 16/26;
- equal means but a larger variance in bicuculline;
- the Figure 3 Kolmogorov-Smirnov tests, the random-mixing simulation and the segregation parameter.

Three Figure 3 claims are `with_inputs`: they need the authors' earlier single-cell stimulation data (their reference 17), and the paper does not say where those data are.

**Details the paper leaves open, and the readings named:**
- **Post-pairing window:** all post-pairing sweeps; the first 10 minutes; or the last 10 minutes.
- **Per-cell t-test:** on individual sweeps, or on the 1-minute bin means.
- **How the peak is measured:** the paper says nothing. I fixed a standard choice (pre-stimulus baseline, peak up to 50 ms after the stimulus), with a 30 ms window as a variant.
- **Test of no net plasticity:** the paper's Student's t-test could be a one-sample test against 0 or a paired test. Its printed p > 0.8 does not fit its own mean and SD, which give p ≈ 0.08.
- **Correlation with initial strength:** the paper only says "correlation". I fixed Pearson, with Spearman as a variant.
- **Simulation:** sampling with or without replacement; one seeded run, or 1000 runs; and how the segregation parameter biases the sampling, read as P(same) = p + S(1 − p).
- **Example cells:** the paper does not say which cells are shown.
- **No test reported:** the paper gives no test for the difference in proportions, so Fisher's exact test is a variant I chose.
- **What ± means:** the arithmetic shows it is the SD across cells. Tolerances on means are the standard errors worked out from the paper's SD and n.

**Inconsistencies in the paper, recorded in the file:**
- The bicuculline cells are called current clamp in the Results but voltage clamp in the Methods and Figure 2, and number 26 in the Results against 27 in the Methods.
- The Results swap the control and bicuculline means (-3.5 against -3.8) and their figure references. I followed the legends.
- The control histogram is cited as Figure 1A in the text but is Figure 1C in its legend.
- The Figure 3A legend's colours are the reverse of the Results' wording.
- The single-cell dataset has n = 42 in the Methods and 43 in the Results.

**Missing:** the single-cell stimulation data and the simulation code, which the three Figure 3 claims need.

## End of run

14 turns, 3 minutes, $1.10 at API prices, result: success.
