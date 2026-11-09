# 001642 · claims · run 39579540594

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001642 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -c paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 150,400p claims/001453/*.yaml | grep -v "^    " | head -60; tail -40 claims/001453/*.yaml
```

```
data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: For each fish, the mean of its median angular velocities for the rightward
- id: fig1h-zf-higher-angular-acceleration
  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
  data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: Angular acceleration as the Methods define it (degrees per second squared), from
- id: figs1e-dc-respond-less-monocular
  statement: DC generally respond less than ZF to monocular stimuli, suggesting that they need
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure S1E
  quote: DC generally responded less to monocular stimuli, suggesting that DC require more visual
  data: with_labels
  depends_on:
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 30,400p paper/*.txt | grep -v '^\[[0-9]*\] 10\.' | cat -s
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/dbbb6413-e07e-4fec-8340-71dca6929479/tool-results/bwkyb54d9.txt"
}
```

```
1	
2	[16] Houk JC Adams JL Barto AG (1995) in Models of information processing in the basal ganglia, A model of how the basal ganglia generate and use neural signals that predict reinforcement, eds Houk JC Davis JL Beiser DG (Massachusetts Institute of Technology, Cambridge, MA). 10.7551/mitpress/4708.003.0020
3	
4	[31] Paxinos G Watson C (1998) The rat brain stereotaxic coordinates (Academic, San Diego), Ed 4.
5	
6	[37] Sutton RS Barto AG (1998) Reinforcement learning (Massachusetts Institute of Technology, Cambridge, MA).
7	
8	Skip to main content
9	
10	An official website of the United States government
11	
12	Here's how you know
13	Search
14	Log in
15	
16	Primary site navigation
17	
18	Search PMC Full-Text Archive
19	Search in PMC
20	Journal List 
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -E "github|supplement|code avail|http|extended data" paper/*.txt | head; grep -rn "001642" --include=*.yaml --include=*.json --include=*.md . | grep -v transcripts | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 6770,6800p targets/dandisets.json; sed -n 140,155p targets/description_papers.yaml; sed -n 2030,2045p papers/manifest.yaml
```

```
"preprint": false,
     "source": "description"
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "001642",
   "name": "Neural activities in dorsolateral, dorsomedial, and ventral striatum during fixed- and free-choice tasks in rats (Ito & Doya 2015)",
   "published_version": "0.260205.0153",
   "asset_count": 87,
   "size_gb": 0.54,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Rattus norvegicus - Norway rat"
   ],
   "approaches": [
    "electrophysiological approach"
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,60p tools/claims_check.py; grep -n "kind\|data:\|open\|where" claims/*/*.yaml | grep -v "^claims/001453" | awk -F: '{print $3":"$4}' | sort | uniq -c | sort -rn | head -30
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

[... 71 more lines not kept]
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
python -c "
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

**Agent calls Write**

```json
{
 "file_path": "claims/001642/10.1523-jneurosci.1962-14.2015.yaml",
 "content": "# Claims for Ito & Doya (2015), J Neurosci 35(8):3499-3514, on dandiset 001642.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record, open access, as served by PMC (PMC4339358), stored in\n# paper/10.1523-jneurosci.1962-14.2015.txt: abstract, Introduction, Materials and Methods,\n# Results, Discussion and the figure legends. The paper has no supplement. No PDF was available.\n# The display equations of the Methods (decision-tree probability, normalized likelihood,\n# Markov model, DFQ update and choice rule, parameter drift, mutual information, BIC, and the\n# regression model (2)) are images on PMC and are missing from the text; only the words around\n# them were read. Where a criterion needs one of them, it is named as open with the readings\n# the surrounding text allows. Figure panels (such as the windows drawn in Fig. 6A) could not\n# be read. The paper links no code, so no code was read.\n#\n# Data the paper used, as it reports them. Seven male Long-Evans rats. 86 recording sessions,\n# 78,107 trials: 12,185 single fixed-choice, 22,234 double fixed-choice, 36,292 free-choice and\n# 3505 extinction-test trials. Each trial starts with a start tone; a center-hole poke of\n# 500-1000 ms brings one of three cue tones (left tone 900 Hz, right tone 6500 Hz, choice tone\n# white noise, 1000-2000 ms); after cue offset the rat pokes the left or right hole and hears\n# a reward tone (followed by a sucrose pellet) or a no-reward tone. Reward probabilities\n# (left, right) are (50%, 0%) for the left tone, (0%, 50%) for the right tone, and one of\n# (90, 50), (50, 90), (50, 10), (10, 50) per block for the choice tone. Block sequence per\n# repeat: two single fixed-choice blocks (left tone, then right tone), two double fixed-choice\n# blocks (left and right tones at random), four free-choice blocks (choice tone), with\n# extinction tests of 5 unrewarded trials for left and right tones between the third and fourth\n# blocks and for the choice tone between the sixth and seventh. Repeated two or three times per\n# session. Wait-error trials (leaving the center hole early) and error trials (no L/R poke in\n# 60 s) end with an error tone. Six task events per trial: E1 center-hole entry, E2 cue onset,\n# E3 cue offset, E4 center-hole exit, E5 L/R-hole entry, E6 L/R-hole exit; E0 is 2 s before E1\n# and E7 2 s after E6 (the Methods print \"2 s after E8\", a typo). Phases 1 to 7 lie between\n# them; the mean durations of Phases 2 to 6 are 0.75, 1.50, 0.54, 0.76 and 0.38 s.\n# Units: spike-sorted single units from three bundles of eight microwires per rat, DLS and DMS\n# in the left hemisphere, VS in the right. 260 DLS, 178 DMS and 179 VS neurons passed the\n# stability criteria; of these 190, 105 and 119 were phasically active neurons (PANs), the\n# only units analysed. Behavioural model comparison used 202 sessions (101 training, 101\n# test), more than the 86 recording sessions; the paper does not say where the others are from.\n#\n# Methods fixed by the paper and used throughout (Materials and Methods):\n#  - Unit inclusion: the five exclusion conditions of Electrophysiological recording, the\n#    cross-correlation duplicate check, then PAN = proportion of time spent in ISIs longer than\n#    1 s greater than 0.4.\n#  - EASH: spike times within Phases 2 to 6 of each trial scaled linearly onto the mean phase\n#    durations above, spike counts per phase preserved; Phases 1 and 7 (2 s each) unscaled;\n#    10 ms bins.\n#  - Mutual information (Figs. 5, 9, 10): firing F in a window takes four levels f1 to f4;\n#    the event X is binary (left or right action; fixed- or free-choice block; rewarded or\n#    not). MI is in bits/s. Fig. 5 uses 100 ms EASH bins and all trials of single fixed,\n#    double fixed and free-choice blocks. Figs. 9 and 10 use the last 20 trials of each block\n#    and a sliding window of the preceding 500 ms, step 50 ms. Significance threshold for a\n#    region average, p < 0.01, is the second largest of 100 region averages of MI with random\n#    binary events.\n#  - Regression (Figs. 7, 8): y(t), the spike count of trial t in a time bin, on a constant, the\n#    trial index t, a(t) (1 left, 2 right), r(t) (1 reward, 0 none), a(t-1), r(t-1), QL(t) and\n#    QR(t) from the FQ-learning model with time-varying parameters. For each neuron and bin, the\n#    subset of regressors with the smallest BIC is chosen, and a regressor is coded when its\n#    coefficient has p < 0.01 in that model. Action-value coding is QL or QR coded; state-value\n#    coding is QL and QR coded with the same sign; policy coding is both with opposite signs.\n#\n# Details the paper leaves open and that bear on several claims (each criterion names those\n# it needs):\n#  - O1, MI estimation. The four firing levels and any bias correction are referred to Ito and\n#    Doya (2009) and not restated. Readings: (a) levels as quartiles of the neuron's spike\n#    counts in that window across the trials used (equal occupancy), no bias correction;\n#    (b) the same with the mean MI of the random-event shuffles subtracted. The plug-in\n#    estimate from the 4 x 2 table is used in both, divided by the window length for bits/s.\n#  - O2, smoothing of EASHs for Fig. 4. The Methods use a 10 ms Gaussian (unit exclusion), the\n#    Fig. 3 legend 30 ms. Readings: (a) 10 ms SD; (b) 30 ms SD; (c) none.\n#  - O3, trials in EASHs and Fig. 5. \"Whole trials\" may (a) exclude or (b) include the\n#    extinction-test trials; wait-error and error trials have no action and are left out.\n#  - O4, chi-square tests of proportions. Readings: 2 x 2 test (a) without or (b) with Yates\n#    continuity correction.\n#  - O5, \"Mann-Whitney U test\" for proportions of coding neurons (Figs. 8 and 6). Read as a\n#    Mann-Whitney U test on per-neuron 0/1 coding indicators, two-sided.\n#  - O6, regression time bins for Fig. 8, \"500 ms before and after the seven trial events\".\n#    Readings: (a) 500 ms windows before and after each of E1 to E7 in real time; (b) the\n#    same windows on the EASH time axis. The Results refer to phases (Phase 1, first half of\n#    Phase 4, Phase 5); a phase result is taken from the windows lying in that phase.\n#  - O7, trials in the regression. The values come from the free-choice model, so readings are\n#    (a) free-choice trials only, (b) all choice trials with QL and QR carried through the\n#    session. The text says the full model has \"six variables (including the constant\n#    variable for β0)\" and \"26 models\" (2^6 garbled), which does not match the eight terms\n#    listed; reading (c) of the subset search keeps all eight terms as candidates (2^8 subsets,\n#    or 2^7 with the constant always in).\n#  - O8, FQ model. The update and choice equations are missing. The text's description implies\n#    Q of the chosen action moves toward kappa1 after reward and toward -kappa2 after no reward\n#    with rate alpha1, the unchosen Q decays toward 0 with rate alpha2 (= alpha1 in FQ), and\n#    P(left) is a logistic function of QL - QR. Initial values, the priors of the particle\n#    filter and the search for sigma_alpha and sigma_kappa are referred to Ito and Doya (2009).\n#    5000 particles; QL and QR are the means of the predictive distribution.\n#\n# Paper inconsistencies noted: the Results cite \"Fig. 7F\" for state-value neurons, meaning\n# Fig. 8F; the Discussion cites Fig. 8C for action-value neurons, meaning Fig. 8E; E7 is defined\n# as \"2 s after E8\".\n#\n# All claims use the dataset's own recordings and behaviour (data: dataset). The paper relies on\n# no outside data.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001642\"\npaper: doi:10.1523/jneurosci.1962-14.2015\nclaims:\n- id: trial-counts\n  statement: The analysis covers 78,107 trials in 86 recording sessions from seven rats, of which\n    12,185 are single fixed-choice, 22,234 double fixed-choice, 36,292 free-choice and 3505\n    extinction-test trials.\n  source: Results, opening section, paragraph 2\n  quote: Here, we report the results of all 78,107 trials in 86 recording sessions, performed by\n    seven rats, consisting of 12,185 single fixed-choice trials (16.4%), 22,234 double\n    fixed-choice trials (30.0%), 36,292 free-choice trials (48.9%), and 3505 extinction test\n    trials (4.7%)\n  expected:\n  - quantity: trials\n    value: 78107\n    tolerance: 7810.7\n  - quantity: recording sessions\n    value: 86\n    tolerance: 8.6\n  - quantity: rats\n    value: 7\n    tolerance: 0\n  - quantity: single fixed-choice trials\n    value: 12185\n    tolerance: 1218.5\n  - quantity: double fixed-choice trials\n    value: 22234\n    tolerance: 2223.4\n  - quantity: free-choice trials\n    value: 36292\n    tolerance: 3629.2\n  - quantity: extinction-test trials\n    value: 3505\n    tolerance: 350.5\n  criterion: The rat count must match exactly. The paper does not say which trials it counts\n    (the four categories sum to 74,216, not 78,107). Readings are (a) all trials started,\n    including wait-error and error trials; (b) trials with an L/R choice only. Reproduced when,\n    under one reading, every count is within tolerance.\n- id: trials-per-block\n  statement: Completing a block took 22.56 ± 8.70 trials for single fixed-choice blocks, 47.11 ±\n    20.29 for double fixed-choice blocks and 41.10 ± 27.58 for free-choice blocks (mean ± SD).\n  source: Results, opening section, paragraph 2\n  quote: Numbers of trials required to complete one block were 22.56 ± 8.70 for single\n    fixed-choice blocks, 47.11 ± 20.29 for double fixed-choice blocks, and 41.10 ± 27.58 for\n    free-choice blocks, (mean ± SD)\n  expected:\n  - quantity: mean trials per single fixed-choice block\n    value: 22.56\n    tolerance: 8.70\n  - quantity: mean trials per double fixed-choice block\n    value: 47.11\n    tolerance: 20.29\n  - quantity: mean trials per free-choice block\n    value: 41.10\n    tolerance: 27.58\n  - quantity: SD of trials per single fixed-choice block\n    value: 8.70\n    tolerance: 0.87\n  - quantity: SD of trials per double fixed-choice block\n    value: 20.29\n    tolerance: 2.03\n  - quantity: SD of trials per free-choice block\n    value: 41.10\n    tolerance: 2.76\n  criterion: The tolerance of each mean is the stated SD (protocol); each SD is checked to 10%.\n    The paper leaves open which trials are counted and which blocks enter. Readings are\n    (a) choice trials only (the block rule counts \"choice trials\"), completed blocks only;\n    (b) all trials including wait-error and error trials, completed blocks only; (c) as (a)\n    with the last, possibly unfinished, block of a session included; (d) as (b) with it\n    included. Extinction trials are not counted in any reading. Reproduced when, under one\n    reading, all six values are within tolerance.\n- id: fig2c-extinction-differs\n  statement: During extinction tests, choice probabilities for the left and right tones differ\n    significantly from those for the choice tone.\n  source: Results, Behavioral performance, paragraph 1; Figure 2B and 2C\n  quote: Choice probabilities during extinction tests were significantly different between the\n    left and right tones and the choice tone (Fig. 2C; p < 0.0001, χ2 test)\n  statistics:\n  - test: χ2 test\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Choices over the five trials of each extinction test (Fig. 2C legend). The\n    contingency table of the χ2 test is not given. Readings are (a) left-tone trials against\n    choice-tone trials after a left-optimal free-choice block, and right-tone trials against\n    choice-tone trials after a right-optimal block, each a 2 x 2 table of left and right\n    choices; (b) one 2 x 2 table of choices of the previously optimal action, fixed tones pooled\n    against the choice tone pooled. Reproduced when every test of a reading gives p < 0.0001\n    with the fixed tones further from 50% than the choice tone.\n- id: fig2b-extinction-time-course\n  statement: In extinction tests the choice-tone choice probability shifts toward 50% after the\n    first unrewarded trial, while the left- and right-tone choice probabilities stay biased\n    after five unrewarded trials.\n  source: Results, Behavioral performance, paragraph 1; Figure 2B\n  quote: whereas the choice probabilities for the free-choice tone shifted toward 50% following\n    the first nonrewarded trial (orange lines, Fig. 2B), choice probabilities for the left and\n    right tones remained biased even after five no-reward trials\n  criterion: Left-choice probability at each of the five extinction trials, per tone, with the\n    choice tone split by the optimal action of the previous free-choice block (Fig. 2B legend),\n    with 95% confidence intervals of a binomial proportion (the interval method is not given;\n    Wilson intervals are a standard choice and are shown with Clopper-Pearson). Reproduced when\n    (1) for both choice-tone groups the probability at trial 2 is closer to 0.5 than at trial 1,\n    and (2) at trial 5 the 95% interval for the left tone lies above 0.5 and that for the right\n    tone below 0.5.\n- id: fig2d-f-decision-trees\n  statement: Choice-tone choices depend on the previous one or two trials' actions and rewards\n    (a decision tree that expands symmetrically), while left- and right-tone choices stay\n    biased toward left and right whatever the previous experience.\n  source: Results, Behavioral performance, paragraph 2; Figure 2D to 2F\n  quote: The decision tree for choice tones expands symmetrically (Fig. 2D), indicating that\n    action selection was sensitive to past experiences ... action probabilities for the left or\n    right tones (in both single and double fixed-choice blocks) are biased toward 1 (Fig. 2E) or\n    0 (Fig. 2F), respectively, indicating insensitivity to past experiences\n  criterion: Conditional left-choice probabilities for d = 1 and d = 2 from counts NL and NR after\n    each experience sequence, within choice-tone trials and within left- and right-tone trials\n    (single and double fixed-choice blocks), as the Methods define (Decision trees); 95%\n    binomial intervals as in fig2b-extinction-time-course. Experience sequences are taken over\n    consecutive trials of the same tone within a session (the Methods say \"sequences of choice\n    behavior in choice-tone trials\"); whether they run across block borders is open, and both\n    are shown. The paper gives no test or threshold. Reproduced when (1) for choice tones P(L)\n    after L1 exceeds P(L) after R1 with non-overlapping 95% intervals, and (2) every d = 1 and\n    d = 2 conditional probability with at least 10 trials is above 0.5 for the left tone and\n    below 0.5 for the right tone. The 10-trial floor is a standard choice for a plotted\n    estimate; the result without it is shown too.\n- id: fig2g-fq-variable-best\n  statement: Of six DFQ-learning variants and the Markov models, the FQ-learning model with\n    time-varying parameters predicts held-out rat choices in free-choice blocks best.\n  source: Results, Behavioral performance, paragraph 5; Figure 2G\n  quote: found that the FQ-learning model with time-varying parameters predicted rat behaviors\n    best (Fig. 2G). Prediction accuracy was higher than that of Markov models\n  statistics:\n  - about: each other model against FQ-learning (variable)\n    test: paired-sample Wilcoxon's signed rank test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Choice-tone trials of free-choice blocks; models Q (alpha2 = kappa2 = 0), FQ\n    (alpha1 = alpha2) and DFQ, each with constant or time-varying parameters, and Markov models\n    of order d (Methods, Evaluation of decision-making models). Sessions split into training\n    and test halves (the paper used 101 and 101 sessions; how the split was made is not\n    given, so the readings are alternate sessions and a seeded random half, both shown);\n    parameters fitted by maximum likelihood on training data, the time-varying models with a\n    particle filter of 5000 particles. Model equations as O8 (opening comment). The normalized\n    likelihood formula is missing; it is read as the geometric mean of per-trial choice\n    likelihoods, which is 0.5 at chance, computed per test session for the paired Wilcoxon\n    test across sessions. Reproduced when FQ (variable) has the highest normalized likelihood\n    of test data and exceeds every Markov model, under a reading.\n- id: actor-critic-near-chance\n  statement: A regular actor-critic model with constant parameters predicts test choices close\n    to chance, with normalized likelihood 0.5080.\n  source: Results, Behavioral performance, last paragraph\n  quote: We also tested a regular actor-critic model with constant variables (Sutton and Barto,\n    1998), but the normalized likelihood of test data was close to the chance level (0.5080; data\n    not shown)\n  expected:\n  - quantity: normalized likelihood of test data, actor-critic\n    value: 0.5080\n    tolerance: 0.0508\n  criterion: The paper names the model only as a regular actor-critic model with constant\n    parameters (Sutton and Barto, 1998) and gives neither its equations nor its parameters. The\n    author tests the standard tabular actor-critic for one state and two actions (critic\n    V updated by the reward prediction error, actor preferences updated by the same error,\n    softmax choice) and, as a variant, the same with a fixed inverse temperature; if neither is\n    accepted as the paper's model, the claim is blocked as methods_underspecified.\n  depends_on:\n  - fig2g-fq-variable-best\n- id: neuron-counts\n  statement: Stable recordings were made from 260 DLS, 178 DMS and 179 VS neurons, of which 190,\n    105 and 119 were phasically active neurons.\n  source: Results, Activity patterns of phasically active neurons, paragraph 1\n  quote: Stable recordings were made from 260 neurons in DLS, 178 neurons in DMS, and 179 neurons\n    in VS from seven rats ... Among these, 190, 105, and 119 neurons from DLS, DMS, and VS,\n    respectively, were classified as PANs\n  expected:\n  - quantity: stable DLS neurons\n    value: 260\n    tolerance: 26\n  - quantity: stable DMS neurons\n    value: 178\n    tolerance: 17.8\n  - quantity: stable VS neurons\n    value: 179\n    tolerance: 17.9\n  - quantity: DLS PANs\n    value: 190\n    tolerance: 19\n  - quantity: DMS PANs\n    value: 105\n    tolerance: 10.5\n  - quantity: VS PANs\n    value: 119\n    tolerance: 11.9\n  criterion: Counts of units per region; PANs by the rule of the Methods (proportion of time in\n    ISIs longer than 1 s greater than 0.4), over the whole session. If the dataset holds only\n    curated units, the stable counts are compared as deposited and the PAN rule is applied to\n    them. Reproduced when all six counts are within tolerance.\n- id: fig4b-vs-phase1\n  statement: More than 60% of VS PANs increase their activity as the rat approaches the center\n    hole (Phase 1), significantly more than in DLS and DMS.\n  source: Results, Activity patterns of phasically active neurons, paragraph 3; Figure 4B\n  quote: The proportion of neurons that increased their activity as a rat approached the center\n    hole (trial Phase 1) was >60% in VS, significantly larger than in DLS and DMS (p = 0.0015 and\n    p < 0.0001, respectively, χ2 test)\n  statistics:\n  - about: VS against DLS\n    test: χ2 test\n    p: 0.0015\n  - about: VS against DMS\n    test: χ2 test\n    p: 0.0001\n    p_relation: \"<\"\n  depends_on:\n  - neuron-counts\n  expected:\n  - quantity: proportion of VS PANs activated in Phase 1, lower bound\n    value: 0.60\n    tolerance: 0.06\n  criterion: Per PAN, the EASH over all trials (O3), normalized to a maximum of 1 (Fig. 4A\n    legend), smoothing as O2. A neuron is activated in a phase when its normalized EASH reaches\n    0.5 during that phase (Fig. 4B legend); readings are (a) any bin at or above 0.5 in the\n    phase, (b) the first crossing of 0.5 falls in the phase (the sort of Fig. 4A). 2 x 2 χ2\n    tests between regions, O4. Reproduced when, under one reading, the VS proportion exceeds\n    0.54 and VS exceeds DLS and DMS with p < 0.05 in both tests.\n- id: fig4b-dms-phase5\n  statement: More than 60% of DMS PANs are activated between center-hole exit and L/R-hole entry\n    (Phase 5), significantly more than in DLS and VS.\n  source: Results, Activity patterns of phasically active neurons, paragraph 3; Figure 4B\n  quote: After a rat's exit from the center hole until its entrance into the L/R hole (trial Phase\n    5), >60% of DMS neurons were activated, which was significantly larger than the proportions of\n    DLS and VS (p = 0.00021 for DLS, p = 0.040 for VS, χ2 test)\n  statistics:\n  - about: DMS against DLS\n    test: χ2 test\n    p: 0.00021\n  - about: DMS against VS\n    test: χ2 test\n    p: 0.040\n  depends_on:\n  - neuron-counts\n  expected:\n  - quantity: proportion of DMS PANs activated in Phase 5, lower bound\n    value: 0.60\n    tolerance: 0.06\n  criterion: As fig4b-vs-phase1, for Phase 5. Reproduced when, under one reading, the DMS\n    proportion exceeds 0.54 and DMS exceeds DLS and VS with p < 0.05 in both tests.\n- id: fig4b-vs-phase7\n  statement: During pellet retrieval (Phase 7) the proportion of activated neurons is\n    significantly larger in VS than in DLS.\n  source: Results, Activity patterns of phasically active neurons, paragraph 3; Figure 4B\n  quote: During the trial phase of receiving a sugar pellet (trial Phase 7), the proportion of\n    activated neurons was significantly larger in VS than in DLS (p = 0.0040, χ2 test)\n  statistics:\n  - test: χ2 test\n    p: 0.0040\n  depends_on:\n  - neuron-counts\n  criterion: As fig4b-vs-phase1, for Phase 7. Reproduced when, under one reading, the VS\n    proportion exceeds the DLS proportion with p < 0.05.\n- id: fig4c-activation-duration\n  statement: VS PANs stay active longer than DLS and DMS PANs, and DLS PANs have the shortest\n    activation, shorter than VS and DMS.\n  source: Results, Activity patterns of phasically active neurons, paragraph 3; Figure 4C\n  quote: VS neurons maintained activation longer (more than half of peak activity) than DLS (p <\n    0.0001, Mann–Whitney U test) and DMS neurons (p < 0.0001, Mann–Whitney U test), and DLS\n    neurons had shorter durations of activation than VS neurons and DMS neurons (p < 0.0001 for\n    VS, p = 0.040 for DMS, Mann–Whitney U test)\n  statistics:\n  - about: VS against DLS\n    test: Mann–Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: VS against DMS\n    test: Mann–Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: DLS against DMS\n    test: Mann–Whitney U test\n    p: 0.040\n  depends_on:\n  - neuron-counts\n  criterion: Per PAN, the activity ratio of each phase (time the normalized EASH is above 0.5,\n    divided by the phase duration), averaged over the seven phases (Fig. 4C legend); EASH as in\n    fig4b-vs-phase1 (O2, O3). Two-sided Mann-Whitney U tests between regions. Reproduced when,\n    under one reading of O2, the medians order VS > DMS > DLS and all three tests give p < 0.05.\n- id: fig5b-state-info-vs\n  statement: Information about the block type (fixed- or free-choice) is strongest in VS,\n    especially during the approach to the center hole (Phase 1).\n  source: Results, Information coding of state, action, and reward, paragraph 2; Figure 5A and 5B\n  quote: State information (fixed- or free-choice block) was strongest in VS, especially, during\n    the approach to the center hole (trial Phase 1) (p < 0.0001 for DLS, p = 0.022 for DMS,\n    Mann–Whitney U tests)\n  statistics:\n  - about: VS against DLS, Phase 1\n    test: Mann–Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: VS against DMS, Phase 1\n    test: Mann–Whitney U test\n    p: 0.022\n  depends_on:\n  - neuron-counts\n  criterion: Per PAN, MI between firing and block type (fixed-choice blocks, single and double,\n    against free-choice blocks) in each 100 ms EASH bin over all trials (Methods, Mutual\n    information; O1, O3). The test's unit of comparison is not stated; readings are per-neuron\n    MI (a) averaged over the bins of Phase 1, (b) in each Phase 1 bin, the result read from the\n    bins that pass. Two-sided Mann-Whitney U tests. Reproduced when, under one reading, VS\n    exceeds DLS and DMS with p < 0.05 and the VS region average exceeds the shuffle threshold in\n    Phase 1.\n- id: fig5e-action-info-rises-dls\n  statement: Action information (left or right choice) starts rising during cue presentation\n    (Phase 3) only in DLS.\n  source: Results, Information coding of state, action, and reward, paragraph 2; Figure 5C to 5E;\n    Discussion, paragraph 1\n  quote: Action information (left or right hole choice) started increasing during the tone\n    presentation (trial Phase 3) specifically in DLS (Fig. 5C–E)\n  depends_on:\n  - neuron-counts\n  criterion: Region averages of per-PAN action MI in 100 ms EASH bins (O1, O3), against the\n    shuffle threshold of the Methods (100 random-event repeats, second largest, p < 0.01).\n    Reproduced when, under one reading, the DLS average exceeds its threshold in at least one\n    Phase 3 bin and the DMS and VS averages exceed theirs in no Phase 3 bin.\n- id: fig5e-action-info-cue-offset-dls\n  statement: In the 100 ms before cue offset, action information is significantly higher in DLS\n    than in DMS and VS.\n  source: Results, Information coding of state, action, and reward, paragraph 3; Figure 5E\n  quote: Action information during the 100 ms before the offset of the cue tone was significantly\n    higher in DLS than in DMS and VS (p = 0.0175 for DMS, p = 0.00091 for VS, Mann–Whitney U\n    tests)\n  statistics:\n  - about: DLS against DMS\n    test: Mann–Whitney U test\n    p: 0.0175\n  - about: DLS against VS\n    test: Mann–Whitney U test\n    p: 0.00091\n  depends_on:\n  - neuron-counts\n  criterion: Per-PAN action MI in the 100 ms EASH bin ending at E3 (O1, O3); two-sided\n    Mann-Whitney U tests. Reproduced when, under one reading, DLS exceeds DMS and VS with p <\n    0.05 in both tests.\n- id: fig5e-action-info-center-exit\n  statement: In the 100 ms before center-hole exit, action information in DMS is higher than in\n    DLS (not significant) and VS, and is weakest in VS.\n  source: Results, Information coding of state, action, and reward, paragraph 3; Figure 5D and 5E\n  quote: Immediately after the offset of the cue tone (trial Phase 4) action information in DMS\n    rapidly increased and became higher than that in DLS and VS during the 100 ms before the\n    offset from the center hole, while information in VS was weakest (p = 0.16 for DLS, p = 0.0027\n    for VS, p < 0.0001 for DLS vs VS, Mann–Whitney U tests)\n  statistics:\n  - about: DMS against DLS\n    test: Mann–Whitney U test\n    p: 0.16\n  - about: DMS against VS\n    test: Mann–Whitney U test\n    p: 0.0027\n  - about: DLS against VS\n    test: Mann–Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n  depends_on:\n  - neuron-counts\n  criterion: Per-PAN action MI in the 100 ms EASH bin ending at E4 (O1, O3); two-sided\n    Mann-Whitney U tests. Reproduced when, under one reading, the region means order DMS > DLS\n    > VS, and DMS against VS and DLS against VS give p < 0.05. DMS against DLS is reported;\n    its significance is not part of the claim.\n- id: fig5d-action-info-phase5-dms\n  statement: During action execution (Phase 5), action information is highest in DMS.\n  source: Results, Information coding of state, action, and reward, paragraph 3; Figure 5D\n  quote: During action execution (trial Phase 5), the action information was the highest in DMS\n    (p < 0.0001 for DLS, p < 0.0001 for VS, p < 0.0001 for DLS vs VS, Mann–Whitney U tests)\n  statistics:\n  - about: DMS against DLS\n    test: Mann–Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: DMS against VS\n    test: Mann–Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: DLS against VS\n    test: Mann–Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n  depends_on:\n  - neuron-counts\n  criterion: Per-PAN action MI in the 100 ms EASH bins of Phase 5 (O1, O3); the bins compared\n    are not stated, so the readings are (a) the mean over Phase 5 bins, (b) the bin of the\n    DMS region peak. Two-sided Mann-Whitney U tests. Reproduced when, under one reading, DMS\n    exceeds DLS and VS with p < 0.05 in both tests. The DLS against VS test is reported.\n- id: fig5g-reward-info\n  statement: Reward information rises in all regions after L/R-hole entry and is strongest in VS,\n    then DMS, with DLS significantly below both.\n  source: Results, Information coding of state, action, and reward, paragraph 4; Figure 5F and 5G\n  quote: Reward information was strongest in VS, followed by DMS, and reward information in DLS\n    was significantly less than that in VS and DMS (p = 0.012 for DLS vs DMS, p < 0.0001 for DLS vs\n    VS, p = 0.13 for DMS vs VS, Mann–Whitney U tests)\n  statistics:\n  - about: DLS against DMS\n    test: Mann–Whitney U test\n    p: 0.012\n  - about: DLS against VS\n    test: Mann–Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: DMS against VS\n    test: Mann–Whitney U test\n    p: 0.13\n  depends_on:\n  - neuron-counts\n  criterion: Per-PAN reward MI (rewarded against unrewarded choices) in 100 ms EASH bins (O1,\n    O3). The window of the test is not stated; readings are the mean over the bins of (a) Phase\n    6, (b) Phases 6 and 7, (c) the bin of the VS region peak. Two-sided Mann-Whitney U tests.\n    Reproduced when, under one reading, the means order VS > DMS > DLS and DLS is below DMS and\n    VS with p < 0.05.\n- id: fig6-event-coding-proportions\n  statement: Proportions of event-coding neurons follow the MI results. State-coding neurons\n    during cue presentation are most common in VS, action-coding neurons in DLS before action\n    execution and in DMS during it, and reward-coding neurons in VS during L/R poking.\n  source: Results, Information coding of state, action, and reward, paragraph 4; Figure 6D\n  quote: the proportion of state-coding neurons during cue presentation (trial Phase 3) was the\n    largest in VS, and the proportion of action-coding neurons was the largest in DLS before\n    action execution and in DMS during action execution. The proportion of reward-coding neurons\n    was the largest in VS during the L/R poking (Fig. 6D)\n  statistics:\n  - about: differences between regions\n    test: χ2 test\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - neuron-counts\n  criterion: Over all trials (Fig. 6D; O3), a PAN codes an event when firing differs between\n    the two conditions by a Mann-Whitney U test with p < 0.01 (Fig. 6 legend). Windows from the\n    legend; action command (AC) the 500 ms before E4, action the 500 ms after E4, Reward1 the\n    500 ms before E6, Reward2 the 500 ms after E6. The state window is drawn only in Fig. 6A,\n    which could not be read; readings are (a) all of Phase 3 on the EASH axis, (b) the 500 ms\n    before E3. Reward \"during the L/R poking\" is read as Reward1. Reproduced when, under one\n    reading, VS has the largest state and Reward1 proportions, DLS the largest AC proportion and\n    DMS the largest action proportion. The paper's χ2 tests between regions (O4) are reported;\n    which pairs it marked significant could not be read from the figure.\n- id: fig6-above-chance\n  statement: Every proportion of event-coding neurons, in every region, in fixed-choice blocks,\n    free-choice blocks and all trials, is significantly larger than chance.\n  source: Figure 6B to 6D legend\n  quote: All populations are significantly larger than the chance level (binomial test, p < 0.01)\n  statistics:\n  - test: binomial test\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - fig6-event-coding-proportions\n  criterion: As fig6-event-coding-proportions, for fixed-choice trials (Fig. 6B), free-choice\n    trials (Fig. 6C) and all trials (Fig. 6D); state coding exists only for all trials. The\n    chance level is not given; it is read as 0.01, the selection threshold. One-sided binomial\n    test per region and event. Reproduced when every test gives p < 0.01.\n- id: fig6bc-similar-fixed-free\n  statement: The proportions of action- and reward-coding neurons are similar in fixed- and\n    free-choice blocks.\n  source: Results, Information coding of state, action, and reward, paragraph 4; Figure 6B and 6C\n  quote: These proportions in the population were similar in fixed-choice and free-choice blocks\n    (Fig. 6B,C)\n  depends_on:\n  - fig6-event-coding-proportions\n  criterion: The paper names no test. Proportions of AC, action, Reward1 and Reward2 neurons per\n    region, computed separately in fixed-choice and free-choice trials, as in\n    fig6-event-coding-proportions. Reproduced when the region with the largest proportion is the\n    same in both block types for each event. The difference per event and region, with a 2 x 2\n    χ2 test (O4), is reported.\n- id: fig8a-d-action-reward-coding\n  statement: Substantial proportions of neurons in all three regions code the current action\n    before and after action execution and the reward after L/R poking, and rewards of the\n    previous trial are coded in all phases in all regions; a significant proportion of DMS\n    neurons codes the previous action during action execution.\n  source: Results, Model-based analysis of action value and state value coding, paragraph 3;\n    Figure 8A to 8D\n  quote: Substantial proportions of neurons in DLS, DMS, and VS coded actions before and after\n    action execution (Fig. 8A) ... a significant proportion of DMS neurons coded previous actions\n    during action execution (trial Phase 5; Fig. 8B). Substantial proportions of neurons in all\n    subareas coded rewards after the start of L/R hole poking (Fig. 8C), and rewards in the\n    previous trial were also strongly coded in all trial phases in all striatal regions (Fig. 8D)\n  statistics:\n  - about: proportion against chance\n    test: binominal test\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - fig2g-fq-variable-best\n  - neuron-counts\n  criterion: Regression with BIC selection as the Methods give it (opening comment; O6, O7,\n    O8), coding at p < 0.01 per coefficient. Proportions per region and window against chance\n    by a one-sided binomial test at p < 0.01 (Fig. 8 legend); the chance level is not given and\n    is read as 0.01. Reproduced when, under one reading, (1) a(t) is coded above chance in every\n    region in at least one window before and one after E4, (2) r(t) above chance in every\n    region in at least one window after E5, (3) r(t-1) above chance in every region in at least\n    one window of every phase, and (4) a(t-1) above chance in DMS in a Phase 5 window.\n- id: fig8e-action-value-dms\n  statement: The proportion of action-value-coding neurons is highest in DMS during action\n    execution, significantly above DLS.\n  source: Results, Model-based analysis of action value and state value coding, paragraph 4;\n    Figure 8E\n  quote: the proportion of action-value coding neurons was highest in DMS during action execution\n    (Fig. 8E; p = 0.00058 for DLS, p = 0.081 for VS, Mann–Whitney U test)\n  statistics:\n  - about: DMS against DLS\n    test: Mann–Whitney U test\n    p: 0.00058\n  - about: DMS against VS\n    test: Mann–Whitney U test\n    p: 0.081\n  depends_on:\n  - fig8a-d-action-reward-coding\n  criterion: Action-value coding is QL or QR coded (Fig. 8E legend), regression as in\n    fig8a-d-action-reward-coding. Per-neuron 0/1 indicators in the Phase 5 windows compared by\n    Mann-Whitney U tests (O5). Reproduced when, under one reading, DMS has the highest\n    proportion of the three regions in a Phase 5 window and exceeds DLS there with p < 0.05.\n    DMS against VS is reported; its significance is not part of the claim.\n- id: fig8e-qr-dms\n  statement: Most action-value-coding DMS neurons represent QR, and the proportion coding QR\n    during action execution is significantly larger in DMS than in DLS.\n  source: Results, Model-based analysis of action value and state value coding, paragraph 4\n  quote: The majority of these action value-coding neurons in DMS represented QR, the action\n    value for right hole choice, and the proportion of neurons coding QR during action execution\n    was significant larger in DMS than in DLS (p = 0.00017, Mann–Whitney U test)\n  statistics:\n  - test: Mann–Whitney U test\n    p: 0.00017\n  depends_on:\n  - fig8e-action-value-dms\n  criterion: As fig8e-action-value-dms, with QR coding alone. Reproduced when, under one reading,\n    more than half of the DMS action-value-coding neurons in the Phase 5 window code QR and the\n    DMS proportion coding QR exceeds the DLS proportion with p < 0.05.\n- id: fig8f-state-value-vs\n  statement: State-value-coding neurons (QL and QR coded with the same sign) are most common in VS\n    in all phases, significantly more than in DLS and DMS in Phase 1 and in the first half of\n    Phase 4.\n  source: Results, Model-based analysis of action value and state value coding, paragraph 5;\n    Figure 8F (cited as Fig. 7F in the text)\n  quote: The proportion of state-value coding neurons was the highest in VS in all trial phases,\n    especially in starting phase (trial Phase 1) and action initiation phase (trial Phase 4), the\n    proportion was significantly larger in VS than in DLS and DMS (p = 0.039 for DMS and p =\n    0.0027 for DLS, in trial Phase 1; p = 0.024 for DMS and p = 0.0045 for DLS, first half of Phase\n    4; Mann–Whitney U test)\n  statistics:\n  - about: VS against DMS, Phase 1\n    test: Mann–Whitney U test\n    p: 0.039\n  - about: VS against DLS, Phase 1\n    test: Mann–Whitney U test\n    p: 0.0027\n  - about: VS against DMS, first half of Phase 4\n    test: Mann–Whitney U test\n    p: 0.024\n  - about: VS against DLS, first half of Phase 4\n    test: Mann–Whitney U test\n    p: 0.0045\n  depends_on:\n  - fig8a-d-action-reward-coding\n  criterion: State-value coding as the Fig. 8F legend defines it, regression as in\n    fig8a-d-action-reward-coding, Mann-Whitney U tests on 0/1 indicators (O5). Reproduced when,\n    under one reading, VS has the largest proportion in every phase (at least one window per\n    phase) and exceeds DLS and DMS with p < 0.05 in a Phase 1 window and in the window covering\n    the first half of Phase 4.\n- id: no-policy-coding\n  statement: No region has a significant number of policy-coding neurons (QL and QR coded with\n    opposite signs) in any time bin.\n  source: Results, Model-based analysis of action value and state value coding, paragraph 5\n  quote: We did not find significant numbers of policy-coding neurons (those with significant\n    correlations with both action values with opposite signs), in any subarea or in any time bin\n    (data not shown)\n  depends_on:\n  - fig8a-d-action-reward-coding\n  criterion: A claim of absence, on the paper's test for Fig. 8, a one-sided binomial test of the\n    proportion against chance at p < 0.01, with chance read as 0.01 (as in\n    fig8a-d-action-reward-coding). Reproduced when no region and window gives p < 0.01; not\n    reproduced when any does. The largest proportion is reported either way.\n- id: fig9-temporal-order-all-blocks\n  statement: In every block type, action information rises first in DLS during cue presentation,\n    then in DMS after cue offset (Phase 4), and last in VS after the onset of action execution\n    (Phase 5); the pattern holds in free-choice blocks too.\n  source: Results, Action-command information in fixed- and free-choice blocks, paragraph 1;\n    Figure 9A to 9D\n  quote: Action information in the single and double fixed-choice blocks started to rise first in\n    DLS during cue presentation and then in DMS after cue offset (trial Phase 4), and finally in\n    VS after onset of action execution (trial Phase 5) (Fig. 9A,B). Contrary to expectation, this\n    temporal pattern of action information was seen also in free-choice blocks (Fig. 9C,D)\n  depends_on:\n  - neuron-counts\n  criterion: Per PAN and block type (single fixed, double fixed, free with higher probabilities\n    (90, 50) and (50, 90), free with lower probabilities (50, 10) and (10, 50)), action MI from\n    the last 20 trials of each block, in a sliding window of the preceding 500 ms with 50 ms\n    steps (Fig. 9 legend), averaged per region; first time the average exceeds the p < 0.01\n    shuffle threshold (the triangle of Fig. 9). How the last 20 trials of several blocks of one\n    type in a session are combined is not stated; readings are (a) pooled into one MI estimate\n    per neuron, (b) MI per block, averaged. O1 applies. Reproduced when, under one reading, in\n    each of the four block types the first crossing falls in Phase 3 for DLS, in Phase 4 for DMS\n    and in Phase 5 for VS (a VS crossing elsewhere before Phase 5 fails it).\n- id: fig9-dms-never-above-dls\n  statement: In no block type is the action command in DMS stronger than in DLS.\n  source: Results, Action-command information in fixed- and free-choice blocks, paragraph 1;\n    Figure 9\n  quote: There were no conditions in which the action command in DMS was stronger than in DLS\n  depends_on:\n  - fig9-temporal-order-all-blocks\n  criterion: A claim of absence for which the paper gives no test. Action command is action MI\n    before action execution (Fig. 9 legend, upcoming action for Phases 2 to 4), as in\n    fig9-temporal-order-all-blocks, in the two windows the paper tests in Fig. 10 (the 500 ms\n    before E3 and the 500 ms before E4). Judged with the paper's test of Fig. 10 between\n    regions, a two-sided Mann-Whitney U test at p < 0.05. Reproduced when DMS is not\n    significantly above DLS in any block type and window; not reproduced when it is. The\n    differences are reported either way.\n- id: fig10a-dls-fixed-above-free\n  statement: In DLS, action information is significantly stronger in fixed-choice than in\n    free-choice blocks in Phase 3 and Phase 4; it rises right after cue onset in fixed-choice\n    blocks, more slowly in free-choice blocks with higher rewards, and later and weaker with\n    lower rewards.\n  source: Results, Action-command information in fixed- and free-choice blocks, paragraph 2;\n    Figure 10A\n  quote: Action information in free-choice blocks with higher rewards increased more slowly than\n    that in fixed-choice blocks, and action information in free-choice blocks with lower rewards\n    appeared later and was weaker. There were significant differences in action information\n    between fixed-choice blocks and free-choice blocks in trial Phase 3 (during the 500 ms before\n    cue presentation) and trial Phase 4 (during the 500 ms before center hole exit) (p = 0.00047\n    and p = 0.00037, respectively, paired-Mann–Whitney U test)\n  statistics:\n  - about: Phase 3\n    test: paired-Mann–Whitney U test\n    p: 0.00047\n  - about: Phase 4\n    test: paired-Mann–Whitney U test\n    p: 0.00037\n  depends_on:\n  - fig9-temporal-order-all-blocks\n  criterion: Per-PAN action MI as in fig9-temporal-order-all-blocks. Windows from the text, the\n    500 ms windows ending at the end of Phase 3 and of Phase 4 (\"500 ms before cue\n    presentation\" is read as the 500 ms before cue offset, the end of Phase 3, since the\n    window must lie in Phase 3; the 500 ms before cue onset is shown as a variant). Fixed is SF\n    and DF, free is FH and FL; readings of how they are combined are (a) the per-neuron mean of\n    the two block types, (b) trials pooled. \"Paired-Mann-Whitney U test\" is read as (a) the\n    Wilcoxon signed-rank test over neurons, (b) the Mann-Whitney U test unpaired. Reproduced\n    when, under one reading, fixed exceeds free with p < 0.05 in both windows and the DLS\n    region average crosses threshold first in SF or DF, then FH, then FL, with FL's peak in\n    Phases 3 and 4 the lowest of the four.\n- id: fig10b-dms-fixed-above-free\n  statement: In DMS too, action information is significantly stronger in fixed-choice than in\n    free-choice blocks in Phases 3 and 4, against the paper's prediction.\n  source: Results, Action-command information in fixed- and free-choice blocks, paragraph 2;\n    Figure 10B\n  quote: In DMS, action information was stronger in single and double fixed-choice blocks than in\n    free-choice blocks (Fig. 10B), similar to that in DLS, with significant differences in trial\n    Phases 3 and 4 (p = 0.040 for Phase 3, p = 0.0029 for Phase 4, paired-Mann–Whitney U test)\n  statistics:\n  - about: Phase 3\n    test: paired-Mann–Whitney U test\n    p: 0.040\n  - about: Phase 4\n    test: paired-Mann–Whitney U test\n    p: 0.0029\n  depends_on:\n  - fig9-temporal-order-all-blocks\n  criterion: As fig10a-dls-fixed-above-free, for DMS, without the order of crossings. Reproduced\n    when, under one reading, fixed exceeds free with p < 0.05 in both windows.\n- id: fig10c-vs-no-fixed-free-difference\n  statement: In VS, action information shows a transient peak during cue presentation only in\n    single fixed-choice blocks and stays low until action execution, with no significant\n    difference between fixed- and free-choice blocks in Phases 3 and 4.\n  source: Results, Action-command information in fixed- and free-choice blocks, paragraph 2;\n    Figure 10C\n  quote: Action information in VS had a transient peak during cue presentation only in single,\n    fixed-choice blocks and remained low until the onset of action execution (Fig. 10C) with no\n    significant differences between fixed- and free-choice blocks in trial Phases 3 and 4 (p =\n    0.23 and p = 0.28, respectively, paired-Mann–Whitney U test)\n  statistics:\n  - about: Phase 3\n    test: paired-Mann–Whitney U test\n    p: 0.23\n  - about: Phase 4\n    test: paired-Mann–Whitney U test\n    p: 0.28\n  depends_on:\n  - fig9-temporal-order-all-blocks\n  criterion: A claim of absence, on the paper's test as in fig10a-dls-fixed-above-free (each of\n    its readings of the test, as the test itself is ambiguous), at p < 0.05. Reproduced when\n    neither window gives p < 0.05 under the reading used for fig10a; not reproduced when either\n    does. The effect sizes are reported. The SF peak is reported, as whether the SF region\n    average crosses threshold in Phase 3 while DF, FH and FL do not.\n- id: fig10d-dls-stay-above-switch\n  statement: In free-choice blocks, DLS action information is stronger in stay trials than in\n    switch trials in Phase 3, while DMS shows no difference between stay and switch trials.\n  source: Results, Action-command information in fixed- and free-choice blocks, paragraph 3;\n    Figure 10D and 10E\n  quote: In DLS, action information was stronger in stay trials than in switch trials in trial\n    Phase 3 (during the 500 ms before cue presentation) (p = 0.019, Mann–Whitney U test). In DMS,\n    however, we could not find any difference in the action-command signal between switch and stay\n    trials\n  statistics:\n  - about: DLS, stay against switch, Phase 3\n    test: Mann–Whitney U test\n    p: 0.019\n  depends_on:\n  - fig10a-dls-fixed-above-free\n  criterion: Free-choice trials split by whether the action repeats the previous trial's (stay)\n    or not (switch). The trials used are not stated; the Fig. 9 and 10 legends say the last 20\n    trials of each block, so readings are (a) the last 20 trials of each free-choice block, (b)\n    all free-choice trials. Per-PAN action MI in the Phase 3 window of\n    fig10a-dls-fixed-above-free (O1); two-sided Mann-Whitney U test. Reproduced when, under one\n    reading, DLS stay exceeds switch with p < 0.05 and, for DMS (a claim of absence on the same\n    test), neither the Phase 3 nor the Phase 4 window gives p < 0.05.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001642/10.1523-jneurosci.1962-14.2015.yaml",
 "old_string": "  - quantity: SD of trials per free-choice block\n    value: 41.10",
 "new_string": "  - quantity: SD of trials per free-choice block\n    value: 27.58"
}
```

```
The file claims/001642/10.1523-jneurosci.1962-14.2015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001642/10.1523-jneurosci.1962-14.2015.yaml paper/10.1523-jneurosci.1962-14.2015.txt; grep -n -E "—|rather" claims/001642/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('claims/001642/10.1523-jneurosci.1962-14.2015.yaml'))['claims']
print(len(d),sum('statistics' in c for c in d),sum('criterion' in c for c in d),sum('expected' in c for c in d))"
```

```
32 21 32 6
```

**Agent**

I wrote `claims/001642/10.1523-jneurosci.1962-14.2015.yaml`, and the quote checker passes it: 32 claims, 32 quotes, 40 statistical values, 0 problems.

**Text read.** I read the version of record (J Neurosci 2015, open access on PMC as PMC4339358): Methods, Results, Discussion and figure legends. The paper has no supplement and links no code, so I read no code, and there was no PDF.

**What is missing from the text.** All the display equations in the Methods are images on PMC and did not come through. That covers the decision-tree probability, the normalized likelihood, the Markov and DFQ update and choice equations, parameter drift, mutual information, BIC and regression model (2). I could not read figure panels either, in particular the windows drawn in Fig. 6A. Where a criterion needs one of these, it names the readings the surrounding text allows.

**Claims.**
- **Quotes:** all 32 claims have one.
- **Statistics:** 21 claims record them, mostly χ2, Mann–Whitney, "paired-Mann–Whitney", binomial and Wilcoxon signed-rank tests.
- **Expected numbers:** 6 claims (trial counts, trials per block, neuron counts, the >60% proportions and the actor-critic likelihood of 0.5080).
- **Criteria:** all 32 have one.
- **Data:** every claim uses the dataset's own recordings; the paper relies on no outside data.

**Details the paper leaves open, with the readings named:**
- **Mutual information:** how firing is cut into four levels, and whether there is a bias correction, are referred to Ito & Doya 2009. Readings: quartile levels with no correction, or the same minus the shuffle mean.
- **Fig. 4 EASH smoothing:** 10 ms, 30 ms or none.
- **Trials in "whole trials":** with or without the extinction trials.
- **χ2 tests:** with or without Yates correction.
- **"Mann–Whitney" on proportions:** read as the test on per-neuron 0/1 coding indicators.
- **Fig. 8 regression windows:** real time or the EASH time axis.
- **Trials in the regression:** free-choice trials only, or all choice trials.
- **Regression model size:** the text says six variables and 2^6 models but lists eight terms, so the full set of eight is named as a reading.
- **FQ model:** the update and choice equations are written out from the text's description; initial values and particle-filter priors are open.
- **Model comparison:** how the 101/101 session split was made (alternate sessions, or a seeded random half), and whether the normalized likelihood is taken per session.
- **Trial counts:** whether error trials are counted. The four categories sum to 74,216, not the 78,107 stated. For trials per block, whether the last unfinished block of a session counts.
- **Extinction test:** which contingency table the χ2 uses (per tone, or pooled).
- **Fig. 6:** the state-coding window (only drawn in Fig. 6A), and the chance level for the binomial tests (read as 0.01).
- **Figs. 9 and 10:** how the last 20 trials of several blocks are combined (pooled, or averaged per block); "500 ms before cue presentation" (read as before cue offset, with cue onset as a variant); how fixed and free blocks are combined; and whether "paired-Mann–Whitney" means a signed-rank or an unpaired test.
- **Stay/switch analysis:** last 20 trials per block, or all free-choice trials.
- **Actor-critic model:** the paper does not specify it, so that claim may be blocked as `methods_underspecified`.

**Other gaps a claim needed.** The model comparison used 202 sessions, more than the 86 recording sessions, and the paper does not say where the rest come from. The ">60%" proportions are stated only as bounds. Fig. 6E states no result, so it has no claim.

**Paper errors noted in the file's opening comment:**
- The Results cite "Fig. 7F" for state-value neurons; this should be Fig. 8F.
- The Discussion cites "Fig. 8C" for action-value neurons; this should be Fig. 8E.
- The Methods define E7 as "2 s after E8"; this should be E6.

Nothing is committed.

## End of run

15 turns, 5 minutes, result: success.
