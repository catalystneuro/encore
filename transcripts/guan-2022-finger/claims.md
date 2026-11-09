# 000252 · claims · run 39994237119

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453 claims/000252 paper; ls claims | head
```

```
<persisted-output>
Output too large (29.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/785101a2-e5c5-4219-8184-d1574cc9929e/tool-results/bb9wvb7gf.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-10`. Record this version in the attempt's provenance.

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
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453 claims/000252 paper
```

```
Exit code 2
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -250; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2022.12.07.22283227.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2022.12.07.22283227.txt",
 "offset": 363
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the full text: preprint v1, with Methods and the supplementary figure legends. Next I'll look for a code link and check the claims schema tooling.

**Agent calls Bash**

```bash
grep -n -i -E "github|gitlab|code avail|zenodo|osf" paper/*.txt; ls tools docs; sed -n 1,80p tools/claims_check.py | head -80; ls claims | wc -l
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -rn "kind:\|data:\|reading\|open" claims/*/*.yaml | grep -v "^claims/001453" | head -40; grep -rln "rsatoolbox\|Mahalanobis" claims/ | head
```

```
claims/000003/10.1016-j.neuron.2016.12.011.yaml:3:# Results, figure legends and STAR Methods. The version of record is not open access. The
claims/000003/10.1016-j.neuron.2016.12.011.yaml:9:# rates by state, burst indices and trough-to-peak latencies; the open-field remapping index and
claims/000003/10.1016-j.neuron.2016.12.011.yaml:41:# Method choices fixed here, where the Methods leave them open (also in the helper's docstring):
claims/000003/10.1016-j.neuron.2016.12.011.yaml:46:# peak as the "local maximum" in the open field; the T-maze run is the trial's outbound run from
claims/000003/10.1016-j.neuron.2016.12.011.yaml:48:# open-field and T-maze speed from positions smoothed with a 0.25 s Gaussian.
claims/000003/10.1016-j.neuron.2016.12.011.yaml:84:    both readings are tested. Reproduced when, under one reading, at least 90% of labelled
claims/000003/10.1016-j.neuron.2016.12.011.yaml:109:  criterion: The rate is not defined in the paper; readings are (a) spikes over the span of the
claims/000003/10.1016-j.neuron.2016.12.011.yaml:111:    interneurons, which the paper counts apart. Reproduced when, under one reading, both medians
claims/000003/10.1016-j.neuron.2016.12.011.yaml:138:    when, under one reading, the MC fraction is within tolerance and the GC fraction is below
claims/000003/10.1016-j.neuron.2016.12.011.yaml:139:    0.05; partially reproduced when, under one reading, the MC fraction exceeds four times the GC
claims/000003/10.1016-j.neuron.2016.12.011.yaml:156:    reading of wake, the MC median exceeds the GC median in wake and in NREM with Kruskal-Wallis
claims/000003/10.1016-j.neuron.2016.12.011.yaml:169:    reading of wake, NREM exceeds wake and REM (adjusted P < 0.05 for both) and wake against REM
claims/000003/10.1016-j.neuron.2016.12.011.yaml:186:  criterion: As in gc-nrem-highest. Reproduced when, under one reading of wake, the wake median is
claims/000003/10.1016-j.neuron.2016.12.011.yaml:197:    Reproduced when, under one reading of wake, the 
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; sed -n 1,130p claims/000005/10.1038-nn.4412.yaml | sed -n 100,130p
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
[... 216 more lines not kept]
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

**Agent calls Bash**

```bash
curl -s -m 20 https://api.dandiarchive.org/api/dandisets/000252/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin);m=d.get('metadata',d);print(m.get('name'));print(m.get('description'))"
```

Result: the fetched text is not kept.

**Agent**

The dataset is "Finger_RL", the right- and left-hand finger task. The paper links no analysis code. I'll write the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000252/10.1101-2022.12.07.22283227.yaml",
 "content": "# Claims for Guan et al., \"Compositional coding of individual finger movements in human posterior\n# parietal cortex and motor cortex enables ten-finger decoding\", on dandiset 000252.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md (Reader).\n#\n# Text read. The bioRxiv preprint, version 1 (doi:10.1101/2022.12.07.22283227), full text from\n# bioRxiv JATS XML (paper/10.1101-2022.12.07.22283227.txt): main text, Methods, figure legends and\n# the supplementary figure legends (Supplementary Figures 1 to 11). The contents of Supplementary\n# Table 1 (phase durations) and Supplementary Table 2 (session dates) are not in the text, only\n# their legends; no claim here rests on their numbers, since every analysis window is defined from\n# a phase onset. The equation of the cross-validated Mahalanobis distance (Methods, Neural distance\n# between fingers) is lost in the text; its description in words is used. No PDF was supplied.\n#\n# Code. The paper links no analysis code. It names two Python libraries: the representational\n# similarity analysis toolbox (rsatoolbox, ref 57) for cross-validated Mahalanobis distances, and\n# DABEST (ref 53) for Hedges' g with bootstrap confidence intervals.\n#\n# Dataset. Its archive title is \"Finger_RL: human intracortical recordings during attempted finger\n# movements of right and left hands\", and the paper's Data Availability names dandiset 000252. It is\n# meant to hold the ten-finger (right and left hand) task; whether it also holds the\n# contralateral-only, reaction-time and BMI sessions is for the author to find.\n#\n# Data the paper used.\n# - Participants. N, tetraplegic woman (C3-C4, AIS-A), one working 96-channel Utah array in left\n#   PPC at the junction of the intraparietal and postcentral sulci (PC-IP), called N-PPC. J,\n#   tetraplegic man (C4-C5), two 96-channel arrays recorded simultaneously, J-PPC in the superior\n#   parietal lobule and J-MC near the hand knob of left motor cortex.\n# - Ten-finger press task (Figure 3, 7, 8). Text-cued, instructed delay, all ten fingers (R or L\n#   hand; t, i, m, r, p) interleaved in each run-block. N, 100 trials per session over 10\n#   sessions; J, 100 trials per session over 2 sessions. N-PPC 111 neurons per session (102 to\n#   119), 1111 pooled; J-PPC 160 (159 to 160); J-MC 130 (120 to 130).\n# - Alternating-cues task with delay (Figures 1, 4, 5). Right-hand fingers T, I, M, R, P and a\n#   No-Go X, Spatial-Cue and Text-Cue variants interleaved. N, 120 trials per session over 4\n#   sessions (480); J, 112 per session (96 to 120) over 3 sessions (336). N-PPC 118 neurons per\n#   session (111 to 128); J-PPC 103 (92 to 116); J-MC 93 (90 to 95). The legends correct for 466,\n#   308 and 278 neurons pooled.\n# - Reaction-time task with randomized cue location (Figure 2, 6). 3 x 4 letter grid, 48 trials per\n#   run-block, decoded finger shown 1.5 s after the cue. Online BMI, N 4016 trials over 9 sessions\n#   (previously reported in ref 46), J 1488 trials over 8 sessions (right hand), J 336 trials over\n#   3 sessions (left hand).\n# - Measured variables. Sorted single-neuron spike times (k-medoids clusters) for offline\n#   analyses; threshold crossings (-3.5 x RMS) per electrode for online control.\n#\n# Method fixed by the paper (Methods, Feature Extraction and following sections). Firing rate is\n# the spike count in a 500 ms window over its duration. Go (move) window 200 to 700 ms after the Go\n# cue; Delay (plan) window 200 to 700 ms after the Delay screen; Cue window 200 to 700 ms after the\n# Cue screen; ITI window the last 500 ms of the ITI. Neurons with mean rate below 0.5 Hz are\n# excluded from all analyses. Single-neuron selectivity is a one-way ANOVA across conditions,\n# Benjamini-Hochberg FDR over the neurons of a participant (pooled across sessions), q < 0.05;\n# large effect eta2 > 0.14; Dunnett's test against No-Go for which fingers differ. Offline\n# classifier is diagonal-covariance LDA (Gaussian naive Bayes with one shared covariance), one per\n# session, stratified 8-fold cross-validation, accuracies pooled over trials of all sessions.\n# CCGP uses a pseudo-population of neurons pooled across sessions, and a permutation test with 1001\n# label shuffles.\n#\n# Details the paper leaves open, with the readings each criterion runs (all are run; the outcome is\n# the one they all give, or the claim is methods_underspecified).\n# - O1 The 0.5 Hz exclusion. (a) mean rate over the whole session; (b) mean rate over the analysis\n#   windows of all trials of the task.\n# - O2 Fold assignment of stratified 8-fold cross-validation. (a) folds in trial order, no\n#   shuffling (scikit-learn StratifiedKFold default); (b) shuffled folds, repeated over 10 seeds\n#   and averaged (the seed is a standard choice and is reported).\n# - O3 Noise covariance of the cross-validated Mahalanobis distance (rsatoolbox). (a) from the\n#   residuals about the condition means, with diagonal shrinkage ('shrinkage_diag'); (b) the same\n#   with shrinkage toward identity ('shrinkage_eye'); (c) diagonal only ('diag'). The Methods say\n#   a noise covariance is used and that both folds' covariances enter, not how it is estimated.\n# - O4 Cross-validation partition of the distance. (a) two independent halves A and B of each\n#   condition's trials (odd and even repetitions), as the Methods' wording of partitions A and B\n#   reads; (b) leave-one-repetition-out over all fold pairs (rsatoolbox crossnobis with each\n#   repetition index as the cross-validation descriptor).\n# - O5 The 95% confidence interval of the matching against non-matching distance difference.\n#   (a) bias-corrected and accelerated bootstrap of the difference of means, as DABEST (the\n#   estimation library the Methods name) computes it, 5000 resamples; (b) percentile bootstrap.\n#   Both resample the RDM elements pooled over sessions, which Figure 8b plots.\n# - O6 Pseudo-trials of the CCGP pseudo-population. (a) trials matched across sessions by their\n#   repetition index within condition; (b) trials matched at random within condition, resampled\n#   100 times and averaged.\n# - O7 The linear decoder of the CCGP analysis. (a) the diagonal LDA of the Methods' offline\n#   classification; (b) a linear support vector machine, as in the CCGP literature the Methods cite\n#   (ref 60). The paper says only \"linear decoders\".\n# - O8 Within-condition (standard) finger-type accuracy that bounds finger-type CCGP. (a) a 5-class\n#   finger decoder trained and tested within each hand by stratified 8-fold cross-validation,\n#   averaged over hands (the \"within-hand accuracy\" of Results, last paragraph); (b) a 5-class\n#   finger-type decoder over the trials of both hands, cross-validated the same way.\n# - O9 \"Close to\" standard accuracy (Figure 8e). The paper prints no margin. (a) CCGP at least 0.9\n#   of the standard accuracy; (b) the CCGP to accuracy ratio above that of J-PPC finger-type, which\n#   the paper calls much lower (36% against 65%, ratio 0.55).\n# - O10 Features of the retrospective single-array BMI decoder. (a) threshold crossing rates per\n#   electrode in [0.5, 1.5] s after the cue, as online; (b) sorted neurons in the same window.\n#\n# Tolerances. 10% of each reported value, except where the paper gives a confidence interval or a\n# spread, as each claim says.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000252\"\npaper: doi:10.1101/2022.12.07.22283227\nclaims:\n- id: tenfinger-recording-counts\n  statement: In the ten-finger task, N-PPC yielded 111 neurons per session (102 to 119) over 10\n    sessions of 100 trials, J-PPC 160 (159 to 160) and J-MC 130 (120 to 130) over 2 sessions of\n    100 trials.\n  source: Results, Decoding individual finger presses of either hand, paragraph 2\n  quote: \"participant N: 100 trials / session for 10 sessions; participant J: 100 trials / session\n    for 2 sessions). We recorded 111 neurons per session (min: 102; max: 119) from N-PPC, 160\n    neurons per session (min: 159; max: 160) from J-PPC, and 130 neurons per session (min: 120;\n    max: 130) from J-MC\"\n  expected:\n  - quantity: N-PPC sessions\n    value: 10\n    tolerance: 0\n  - quantity: J sessions\n    value: 2\n    tolerance: 0\n  - quantity: trials per session\n    value: 100\n    tolerance: 10\n  - quantity: N-PPC neurons per session, mean\n    value: 111\n    tolerance: 11.1\n  - quantity: J-PPC neurons per session, mean\n    value: 160\n    tolerance: 16\n  - quantity: J-MC neurons per session, mean\n    value: 130\n    tolerance: 13\n  criterion: Neurons counted after the 0.5 Hz exclusion under both readings of O1, and before it.\n    Reproduced when the session and trial counts match and, under one reading, each mean count is\n    within tolerance and each range is within 10% of its bounds.\n- id: tenfinger-pooled-npcc-neurons\n  statement: 1111 N-PPC neurons were recorded across the 10 sessions of the ten-finger task.\n  source: Supplementary Figure 11 legend\n  quote: 1111 N-PPC neurons were recorded across 10 sessions\n  expected:\n    quantity: N-PPC neurons pooled over 10 sessions\n    value: 1111\n    tolerance: 111\n  criterion: Counted under both readings of O1 and before the exclusion; reproduced when one count\n    is within tolerance.\n- id: tenfinger-discriminative-fraction\n  statement: Most neurons discriminate firing rates across the ten fingers in the Go window (N-PPC\n    66%, J-PPC 57%, J-MC 78%, q < 0.05).\n  source: Results, Decoding individual finger presses of either hand, paragraph 2\n  quote: \"most neurons (N-PPC: 66%; J-PPC: 57%; J-MC: 78%) discriminated firing rates across\n    fingers (q < 0.05)\"\n  expected:\n  - quantity: N-PPC fraction of discriminative neurons\n    value: 66\n    tolerance: 6.6\n    unit: \"%\"\n  - quantity: J-PPC fraction of discriminative neurons\n    value: 57\n    tolerance: 5.7\n    unit: \"%\"\n  - quantity: J-MC fraction of discriminative neurons\n    value: 78\n    tolerance: 7.8\n    unit: \"%\"\n  criterion: As in Methods, Single-neuron selectivity. Per neuron, a one-way ANOVA of Go-window\n    firing rates (200 to 700 ms after Go) across the ten finger conditions; Benjamini-Hochberg FDR\n    over all neurons of the participant's array pooled across sessions; discriminative when q <\n    0.05; neurons pooled across sessions for the percentage (Methods). J-PPC and J-MC are\n    corrected separately, as each legend gives an array's own neuron count. Reproduced when,\n    under one reading of O1, all three percentages are within tolerance; partially reproduced when\n    one or two are.\n- id: tenfinger-decoding-accuracy\n  statement: A linear classifier discriminates all ten fingers well above the 10% chance level\n    (cross-validated accuracy N-PPC 70%, J-PPC 66%, J-MC 75%).\n  source: Results, Decoding individual finger presses of either hand, paragraph 3; Figure 7c to 7e\n  quote: \"A linear classifier (Methods) was able to discriminate between all ten fingers\n    (cross-validated classification accuracy, N-PPC: 70%; J-PPC: 66%; J-MC: 75%; chance: 10%)\"\n  expected:\n  - quantity: N-PPC ten-finger accuracy (1000 trials over 10 sessions)\n    value: 70\n    tolerance: 7\n    unit: \"%\"\n  - quantity: J-PPC ten-finger accuracy (200 trials over 2 sessions)\n    value: 66\n    tolerance: 6.6\n    unit: \"%\"\n  - quantity: J-MC ten-finger accuracy (200 trials over 2 sessions)\n    value: 75\n    tolerance: 7.5\n    unit: \"%\"\n  criterion: As in Methods, Offline classification with cross-validation. Diagonal LDA (one\n    variance per neuron, shared across classes) on Go-window firing rates of sorted neurons, one\n    classifier per session and array, stratified 8-fold cross-validation, predictions on the\n    held-out folds pooled over all trials of all sessions. Readings O1 x O2. Reproduced when,\n    under one reading, all three accuracies are within tolerance; partially reproduced when all\n    three exceed 10% chance by a one-sided binomial test at p < 0.05 but not all are within\n    tolerance.\n- id: tenfinger-error-structure\n  statement: Most ten-finger classification errors confuse an adjacent finger of the same hand or\n    the matching finger of the other hand (N-PPC 76%, J-PPC 66%, J-MC 68% of errors).\n  source: Results, Decoding individual finger presses of either hand, paragraph 3; Figure 7c to 7e\n  quote: \"The majority (N-PPC: 76%; J-PPC: 66%; J-MC: 68%) of classification errors were\n    adjacent-finger-confusion or matching-across-hand-confusion\"\n  depends_on:\n  - tenfinger-decoding-accuracy\n  expected:\n  - quantity: N-PPC share of errors adjacent or matching\n    value: 76\n    tolerance: 7.6\n    unit: \"%\"\n  - quantity: J-PPC share of errors adjacent or matching\n    value: 66\n    tolerance: 6.6\n    unit: \"%\"\n  - quantity: J-MC share of errors adjacent or matching\n    value: 68\n    tolerance: 6.8\n    unit: \"%\"\n  criterion: From the pooled confusion matrices of tenfinger-decoding-accuracy. An error is\n    adjacent when the predicted finger is on the same hand and next to the true one in the order\n    thumb, index, middle, ring, pinky; matching when it is the same finger type of the other hand\n    (Methods, Shared representations across hands, defines matching pairs). Reproduced when,\n    under one reading, all three shares are within tolerance.\n- id: fig8b-matching-closer\n  statement: Matching right and left finger pairs are closer in neural distance than non-matching\n    pairs, by 1.56 units in N-PPC (95% CI 1.33 to 1.78) and 4.30 in J-MC (2.74 to 5.46), but not\n    conclusively in J-PPC (0.27, -0.17 to 0.64).\n  source: Results, Compositional representation of finger and laterality, paragraph 1; Figure 8b;\n    Supplementary Figures 9b and 10b\n  quote: \"On average, matching right/left finger pairs were 1.56 distance-units (95% CI: [1.33,\n    1.78], Figure 8b ) closer to each other than non-matching fingers were. Matching fingers were\n    also represented more similarly than non-matching fingers in J-MC (mean difference: 4.30, 95%\n    CI: [2.74, 5.46]), but this result was not conclusive in J-PPC (mean difference: 0.27, 95% CI:\n    [-0.17, 0.64])\"\n  statistics:\n  - about: N-PPC, non-matching minus matching distance\n    ci:\n      level: 0.95\n      low: 1.33\n      high: 1.78\n    n: RDM elements of 10 sessions\n  - about: J-MC, non-matching minus matching distance\n    ci:\n      level: 0.95\n      low: 2.74\n      high: 5.46\n    n: RDM elements of 2 sessions\n  - about: J-PPC, non-matching minus matching distance\n    ci:\n      level: 0.95\n      low: -0.17\n      high: 0.64\n    n: RDM elements of 2 sessions\n  expected:\n  - quantity: N-PPC mean difference, non-matching minus matching\n    value: 1.56\n    tolerance: 0.23\n  - quantity: J-MC mean difference, non-matching minus matching\n    value: 4.30\n    tolerance: 1.56\n  - quantity: J-PPC mean difference, non-matching minus matching\n    value: 0.27\n    tolerance: 0.44\n  criterion: Tolerances are the distance from each value to the farther bound of its paper CI.\n    Per session and array, cross-validated squared Mahalanobis distances between the ten\n    conditions from Go-window firing rates, computed with rsatoolbox (Methods, Neural distance\n    between fingers), normalized by the number of neurons; readings O3 x O4 (and O1). Matching\n    pairs are the five different-hand same-finger pairs and non-matching the twenty different-hand\n    different-finger pairs (Methods, Shared representations across hands); the elements of all\n    sessions are pooled (Figure 8b legend), and the difference is the mean non-matching minus the\n    mean matching, with its 95% CI by O5. Reproduced when, under one reading, the N-PPC and J-MC\n    differences are positive with CIs excluding 0 and all three values are within tolerance, and\n    the J-PPC CI includes 0 (the paper's own test for the J-PPC absence). Partially reproduced\n    when the N-PPC and J-MC CIs exclude 0 with positive differences but a value is out of\n    tolerance or the J-PPC CI excludes 0.\n- id: fig8a-npcc-index-distinct\n  statement: In N-PPC the inter-finger geometry is similar across hands, with the index finger\n    relatively distinct from the middle and ring fingers in both hands.\n  source: Results, Compositional representation of finger and laterality, paragraph 4; Figure 8a\n    and 8d\n  quote: We found that inter-finger vectors were similar across hands, with the index finger\n    relatively distinct from the middle and ring fingers\n  depends_on:\n  - fig8b-matching-closer\n  criterion: From the N-PPC distances of fig8b-matching-closer averaged over the 10 sessions (Figure\n    8a legend), read as the MDS of Figure 8d preserves them. Reproduced when, under one reading,\n    in each hand the index-middle and index-ring distances both exceed the middle-ring distance,\n    and the ten within-hand distances of the right hand correlate positively with the\n    corresponding left-hand distances (Pearson r > 0). The MDS with Generalized Procrustes\n    alignment (with scaling) across sessions, as the Methods describe, is shown.\n- id: fig8e-hand-ccgp\n  statement: Hand (left against right) decoders trained on four finger types generalize to the\n    held-out finger type significantly above chance (p < 0.001, permutation test), with hand CCGP\n    close to standard decoding accuracy, in N-PPC, J-MC and J-PPC.\n  source: Results, Compositional representation of finger and laterality, paragraphs 5 and 6;\n    Figure 8e; Supplementary Figures 8, 9e, 10e and 11\n  quote: Consistent with this hypothesis, cross-condition hand-decoding generalization performance\n    (hand CCGP) was significantly above chance (p < 0.001, permutation test). Furthermore, hand CCGP\n    was close to the standard decoding accuracy\n  statistics:\n  - about: N-PPC hand CCGP against chance\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: pseudo-population of N-PPC neurons pooled over 10 sessions, 1001 shuffles\n  - about: J-MC hand CCGP against chance\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: pseudo-population of J-MC neurons pooled over 2 sessions\n  - about: J-PPC hand CCGP against chance\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: pseudo-population of J-PPC neurons pooled over 2 sessions\n  criterion: As in Methods, Compositionality of finger representations, and the Supplementary\n    Figure 8 legend. Per array, neurons of all sessions pooled into a pseudo-population (O6);\n    Go-window firing rates; a two-class hand decoder (O7) trained on four finger-type pairs and\n    tested on the held-out pair, CCGP averaged over the five folds. Null distribution from 1001\n    label shuffles; p is the fraction of shuffles whose CCGP reaches the observed one. Standard\n    hand accuracy by stratified 8-fold cross-validation over all ten conditions. Reproduced when,\n    under one reading, every array has p < 0.001 and CCGP close to standard accuracy by O9 (Figure\n    8e and Supplementary Figure 11 say hand CCGP matched standard accuracy in all three);\n    partially reproduced when every p < 0.001 but closeness fails for an array. The CCGP and\n    accuracy values are reported.\n- id: fig8e-finger-ccgp\n  statement: Finger-type decoders trained on one hand generalize to the other hand significantly\n    above chance (p < 0.001), with finger-type CCGP close to standard decoding accuracy, in N-PPC\n    and J-MC.\n  source: Results, Compositional representation of finger and laterality, paragraphs 5 and 6;\n    Figure 8e; Supplementary Figure 9e\n  quote: The finger-type dimension also generalized across hands (p < 0.001), and finger-type CCGP\n    was close to the standard decoding accuracy\n  statistics:\n  - about: N-PPC finger-type CCGP against chance\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: pseudo-population of N-PPC neurons pooled over 10 sessions, 1001 shuffles\n  - about: J-MC finger-type CCGP against chance\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: pseudo-population of J-MC neurons pooled over 2 sessions\n  criterion: As fig8e-hand-ccgp, with a 5-class finger-type decoder trained on the right hand and\n    tested on the left and the reverse, CCGP the mean of the two directions (Supplementary Figure\n    8 legend); chance 20%; standard accuracy by O8. Reproduced when, under one reading, both arrays\n    have p < 0.001 and CCGP close to standard accuracy by O9; partially reproduced when both p <\n    0.001 but closeness fails for one.\n- id: jppc-finger-ccgp-low\n  statement: J-PPC finger representations are less compositional; finger-type CCGP (36%) is above\n    chance (p < 0.001) but much lower than within-hand accuracy (65%).\n  source: Results, Compositional representation of finger and laterality, paragraph 6;\n    Supplementary Figure 10e\n  quote: \"Interestingly, J-PPC finger representations were less compositional. While above chance\n    (p < 0.001), the finger-type CCGP (36%) was much lower than the within-hand accuracy (65%)\"\n  statistics:\n  - test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: pseudo-population of J-PPC neurons pooled over 2 sessions\n  expected:\n  - quantity: J-PPC finger-type CCGP\n    value: 36\n    tolerance: 3.6\n    unit: \"%\"\n  - quantity: J-PPC within-hand finger accuracy\n    value: 65\n    tolerance: 6.5\n    unit: \"%\"\n  criterion: As fig8e-finger-ccgp for J-PPC, with within-hand accuracy by O8 (a), which the\n    Results name; O8 (b) is reported. Reproduced when, under one reading of O6 and O7, p < 0.001\n    and both values are within tolerance; partially reproduced when p < 0.001 and CCGP is below\n    0.9 of the within-hand accuracy but a value is out of tolerance.\n- id: figs11-jppc-lower-matched-size\n  statement: Even at matched neural population size, J-PPC finger-type CCGP is lower than that of\n    N-PPC and J-MC, while hand CCGP matches standard accuracy in all three.\n  source: Results, Compositional representation of finger and laterality, paragraph 6;\n    Supplementary Figure 11\n  quote: Even when accounting for differences in neural population size, finger-type CCGP for J-PPC\n    was lower than finger-type CCGP for N-PPC and J-MC\n  depends_on:\n  - fig8e-finger-ccgp\n  - jppc-finger-ccgp-low\n  criterion: Neuron-dropping curves (Methods, Offline classification, on neuron-dropping curves,\n    random subsets of neurons stacked across sessions) of finger-type CCGP per array, under the\n    readings of fig8e-finger-ccgp. The number of random subsets per size (100) is a standard\n    choice that cannot change the outcome. Reproduced when, at the J-PPC pooled population size\n    and at every smaller size from 50 neurons in steps of 50, the mean J-PPC finger-type CCGP is\n    below the means of N-PPC and J-MC at that size.\n- id: fig4c-contra-discriminative\n  statement: In the contralateral alternating-cues task many neurons discriminate between finger\n    conditions in the Go window (N-PPC 54%, J-PPC 30%, J-MC 78%), selective neurons differ from\n    No-Go for about two fingers on average (2.1, 1.9, 2.7), and many have large effect sizes (eta2\n    > 0.14 in 40%, 25%, 64%).\n  source: Results, Single-neuron modulation to individual finger presses, paragraph 2; Figure 4c to\n    4e; Supplementary Figures 2 and 3\n  quote: \"A large portion of neurons (N-PPC: 54%; J-PPC: 30%; J-MC: 78%; Figure 4c ) discriminated\n    firing rates across conditions (q < 0.05), and selective neurons were often selective for\n    multiple finger movements (mean number of significant fingers, N-PPC: 2.1; J-PPC: 1.9; J-MC:\n    2.7). Moreover, many neurons discriminated between finger conditions with large effect sizes\n    (percentage of neurons with η 2 > 0.14, N-PPC: 40%; J-PPC: 25%; J-MC: 64%\"\n  expected:\n  - quantity: N-PPC discriminative\n    value: 54\n    tolerance: 5.4\n    unit: \"%\"\n  - quantity: J-PPC discriminative\n    value: 30\n    tolerance: 3\n    unit: \"%\"\n  - quantity: J-MC discriminative\n    value: 78\n    tolerance: 7.8\n    unit: \"%\"\n  - quantity: N-PPC mean number of significant fingers\n    value: 2.1\n    tolerance: 0.21\n  - quantity: J-PPC mean number of significant fingers\n    value: 1.9\n    tolerance: 0.19\n  - quantity: J-MC mean number of significant fingers\n    value: 2.7\n    tolerance: 0.27\n  - quantity: N-PPC eta2 above 0.14\n    value: 40\n    tolerance: 4\n    unit: \"%\"\n  - quantity: J-PPC eta2 above 0.14\n    value: 25\n    tolerance: 2.5\n    unit: \"%\"\n  - quantity: J-MC eta2 above 0.14\n    value: 64\n    tolerance: 6.4\n    unit: \"%\"\n  criterion: As in Methods, Single-neuron selectivity. One-way ANOVA across the six conditions\n    (five fingers and No-Go) of Go-window rates; FDR over the neurons of an array pooled across\n    sessions (466, 308 and 278, per the legends of Figure 4c and Supplementary Figures 2c and\n    3c); Dunnett's test of each finger against No-Go, at 0.05, counted over discriminative\n    neurons; eta2 from the ANOVA. Both cue variants pooled. The paper does not say whether\n    the number of significant fingers is averaged over discriminative neurons or over all neurons;\n    readings (a) discriminative neurons, as \"selective neurons\" reads; (b) all neurons. Likewise\n    the eta2 share is read (a) over all neurons, (b) over neurons with q < 0.05. Reproduced when,\n    under one reading of each, all nine values are within tolerance; partially reproduced when the\n    three discriminative fractions are.\n- id: fig4e-plan-vs-move\n  statement: Slightly fewer PPC neurons are strongly tuned (q < 0.05 and eta2 > 0.14) during\n    movement preparation (N-PPC 24%, J-PPC 23%) than during execution (N-PPC 43%, J-PPC 24%).\n  source: Results, Single-neuron modulation to individual finger presses, paragraph 3; Figure 4e\n    and Supplementary Figure 2e\n  quote: \"slightly fewer PPC neurons had strong tuning (q < 0.05 and η 2 > 0.14) during movement\n    preparation (N-PPC: 24%; J-PPC: 23%) than during movement execution (N-PPC: 43%; J-PPC: 24%)\"\n  expected:\n  - quantity: N-PPC strongly tuned, Delay window\n    value: 24\n    tolerance: 2.4\n    unit: \"%\"\n  - quantity: J-PPC strongly tuned, Delay window\n    value: 23\n    tolerance: 2.3\n    unit: \"%\"\n  - quantity: N-PPC strongly tuned, Go window\n    value: 43\n    tolerance: 4.3\n    unit: \"%\"\n  - quantity: J-PPC strongly tuned, Go window\n    value: 24\n    tolerance: 2.4\n    unit: \"%\"\n  criterion: As fig4c-contra-discriminative, in the Delay window (200 to 700 ms after the Delay\n    screen) and the Go window. Whether the FDR correction is applied per window or over both is\n    not stated; readings (a) per window, (b) over both windows. Reproduced when, under one reading,\n    all four values are within tolerance.\n- id: fig5a-contra-decoding\n  statement: Contralateral finger movements (five fingers and No-Go) are classified offline well\n    above the 17% chance level (N-PPC 86%, J-PPC 64%, J-MC 84%), and most errors are adjacent\n    fingers (75%, 42%, 67%).\n  source: Results, Classifying finger presses from neural activity, paragraph 1; Figure 5a;\n    Supplementary Figures 4a and 5a\n  quote: \"Classification accuracies substantially exceeded chance (N-PPC: 86%; J-PPC: 64%; J-MC:\n    84%; chance: 17%). The majority (N-PPC: 75%; J-PPC: 42%; J-MC: 67%) of errors misclassified an\n    adjacent finger\"\n  expected:\n  - quantity: N-PPC accuracy (480 trials over 4 sessions)\n    value: 86\n    tolerance: 8.6\n    unit: \"%\"\n  - quantity: J-PPC accuracy (336 trials over 3 sessions)\n    value: 64\n    tolerance: 6.4\n    unit: \"%\"\n  - quantity: J-MC accuracy (336 trials over 3 sessions)\n    value: 84\n    tolerance: 8.4\n    unit: \"%\"\n  - quantity: N-PPC adjacent-finger share of errors\n    value: 75\n    tolerance: 7.5\n    unit: \"%\"\n  - quantity: J-PPC adjacent-finger share of errors\n    value: 42\n    tolerance: 4.2\n    unit: \"%\"\n  - quantity: J-MC adjacent-finger share of errors\n    value: 67\n    tolerance: 6.7\n    unit: \"%\"\n  criterion: As tenfinger-decoding-accuracy, over six classes (T, I, M, R, P, No-Go) in the Go\n    window. J-PPC 42% is called a majority in the text although below half; it is reproduced as a\n    number. Errors involving No-Go are counted in the denominator and are not adjacent. Reproduced\n    when, under one reading of O1 and O2, all six values are within tolerance; partially\n    reproduced when the three accuracies are.\n- id: fig5bcd-npcc-data-requirements\n  statement: For N-PPC, cross-validated accuracy reaches 80% with about 40 training trials, about 70\n    neurons, and window durations of about 350 ms.\n  source: Results, Classifying finger presses from neural activity, paragraphs 3 and 4; Figure 5b\n    to 5d\n  quote: Cross-validated accuracy increased with more training data, reaching 80% accuracy when\n    training on about 40 trials (2.7 minutes) for N-PPC. Higher neuron counts provide more finger\n    information and thus improved classification accuracy, reaching 80% accuracy at about 70\n    neurons for N-PPC\n  depends_on:\n  - fig5a-contra-decoding\n  expected:\n  - quantity: training trials to reach 80%\n    value: 40\n    tolerance: 4\n  - quantity: neurons to reach 80%\n    value: 70\n    tolerance: 7\n  - quantity: window duration to reach 80%\n    value: 350\n    tolerance: 35\n    unit: ms\n  criterion: As in Methods, Offline classification. Learning curve from subsets of each training\n    fold; neuron-dropping curve from random subsets of neurons stacked across the 4 sessions;\n    window sweep [200 ms, 200 ms + duration] after Go. Each value is the smallest training size,\n    neuron count or duration at which mean accuracy reaches 80%. Step sizes and the number of\n    random subsets (100) are standard choices. How stacked neurons of different sessions form\n    trials is not stated; readings as O6. Reproduced when, under one reading, all three values are\n    within tolerance.\n- id: fig5e-planning-decoding\n  statement: Finger movements are also decoded from PPC during the planning period, with lower\n    accuracy than during execution (N-PPC 66%, J-PPC 61%, chance 17%).\n  source: Results, Classifying finger presses from neural activity, paragraph 5; Figure 5e\n  quote: \"Finger movements could also be decoded from PPC during the planning period ( Figure 5e\n    )), although classification accuracy was lower (N-PPC: 66%; J-PPC: 61%; chance: 17%) than\n    during movement execution\"\n  depends_on:\n  - fig5a-contra-decoding\n  expected:\n  - quantity: N-PPC Delay-window accuracy\n    value: 66\n    tolerance: 6.6\n    unit: \"%\"\n  - quantity: J-PPC Delay-window accuracy\n    value: 61\n    tolerance: 6.1\n    unit: \"%\"\n  criterion: As fig5a-contra-decoding in the Delay window. Reproduced when, under one reading, both\n    values are within tolerance and below the Go-window accuracies.\n- id: fig6-online-bmi\n  statement: During online BMI control of right-hand fingers, participant N reached 86% accuracy\n    (4016 trials over 9 sessions) and J 92% (1488 trials over 8 sessions), against 17% chance.\n  source: Results, Brain-machine interface control of finger movements, paragraphs 3 and 4; Figure\n    6a and 6b\n  quote: Confusion matrix for participant N (PPC), right-hand finger presses. 86% accuracy, 4016\n    trials over 9 sessions ... Confusion matrix for participant J (PPC+MC), right-hand finger\n    presses. 92% accuracy, 1488 trials over 8 sessions\n  expected:\n  - quantity: N online accuracy\n    value: 86\n    tolerance: 8.6\n    unit: \"%\"\n  - quantity: J online accuracy\n    value: 92\n    tolerance: 9.2\n    unit: \"%\"\n  criterion: Accuracy is the share of online trials whose decoded class (shown 1.5 s after the cue)\n    equals the cued class, over all trials of the BMI runs (calibration runs without classifier\n    output excluded). Reproduced when both are within tolerance and the trial and session counts\n    match.\n- id: figs6-single-array-retrospective\n  statement: Retrospectively decoding J's BMI trials from a single array, with a classifier trained\n    on earlier run-blocks, gives 83% (plus or minus 7%) from J-PPC and 87% (plus or minus 8%) from\n    J-MC.\n  source: Results, Brain-machine interface control of finger movements, paragraph 4; Supplementary\n    Figure 6\n  quote: We trained the linear classifier on earlier run-blocks [0, 1, …, M-1] and evaluated on\n    run-block M, repeating for all run-blocks in each session. 83% +/- 7% accuracy (chance 17%),\n    1488 trials over 8 sessions\n  expected:\n  - quantity: J-PPC retrospective accuracy\n    value: 83\n    tolerance: 7\n    unit: \"%\"\n  - quantity: J-MC retrospective accuracy\n    value: 87\n    tolerance: 8\n    unit: \"%\"\n  criterion: Tolerances are the paper's spread. Diagonal LDA trained on run-blocks 0 to M-1 of a\n    session and tested on block M, for every block, features by O10; accuracy pooled over the 1488\n    trials. Whether block 0 (the calibration run) is itself tested is not stated; it is not, as it\n    has no earlier block to train on. Reproduced when, under one reading, both values are within\n    tolerance.\n- id: figs7-left-hand-bmi\n  statement: Participant J controlled left-hand finger presses through the BMI with 94% accuracy\n    (336 trials over 3 sessions).\n  source: Supplementary Figure 7\n  quote: Confusion matrix for participant J (PPC+MC), left-hand finger presses. 94% accuracy, 336\n    trials over 3 sessions\n  expected:\n    quantity: J left-hand online accuracy\n    value: 94\n    tolerance: 9.4\n    unit: \"%\"\n  criterion: As fig6-online-bmi, for the left-hand runs.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000252/10.1101-2022.12.07.22283227.yaml",
 "old_string": "    3c); Dunnett's test of each finger against No-Go, at 0.05, counted over discriminative\n    neurons; eta2 from the ANOVA.",
 "new_string": "    3c); Dunnett's test of each finger against No-Go, at 0.05; eta2 from the ANOVA."
}
```

```
The file claims/000252/10.1101-2022.12.07.22283227.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000252/10.1101-2022.12.07.22283227.yaml paper/10.1101-2022.12.07.22283227.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i -E "—|rather" claims/000252/*.yaml; grep -c "criterion:" claims/000252/*.yaml
```

```
19
```

**Agent**

I wrote `claims/000252/10.1101-2022.12.07.22283227.yaml`. The quote checker reports 19 claims, 19 quotes and 0 problems. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1, from the JATS XML. It includes the main text, Methods, figure legends and the legends of Supplementary Figures 1 to 11. There is no PDF. The paper links no analysis code. It names two Python libraries, rsatoolbox (for the neural distances) and DABEST (for effect sizes and bootstrap intervals).

**Dataset:** its archive title is "Finger_RL", attempted finger movements of the right and left hands, so it should hold the ten-finger task. The claims about the right-hand-only task and the online BMI sessions may have no data in it. The author has to find out.

**Claims:** 19, all with quotes and all with criteria; 15 have expected values.
- **Statistics:** 9 entries in 4 claims.
  - Three 95% confidence intervals: matching right/left finger pairs are closer than non-matching ones.
  - Six permutation tests at p < 0.001: decoders generalize across hand and across finger type.
- **Ten-finger task (8 claims):**
  - neuron and session counts, and the 1111 pooled N-PPC neurons
  - share of neurons that tell fingers apart (66%, 57%, 78%)
  - ten-finger decoding accuracy (70%, 66%, 75%) and the kinds of errors made
  - matching against non-matching distances, and the index finger standing apart in N-PPC
  - generalization of hand and finger-type decoders, with J-PPC's finger-type result low (36% against 65%), even at matched neuron counts
- **Right-hand task, offline (5 claims):** single-neuron tuning, planning against execution, decoding with its error structure, how much data N-PPC needs, and planning-period decoding.
- **BMI (3 claims):** online accuracy (86% and 92%), single-array decoding after the fact (83% and 87%), and left-hand control (94%).

**Details the paper leaves open, with the readings named:**
- **O1, the 0.5 Hz neuron exclusion:** the average rate over the whole session, or over the analysis windows.
- **O2, how trials go into the 8 folds:** in trial order, or shuffled over 10 seeds.
- **O3, the noise covariance for the distances:** rsatoolbox's `shrinkage_diag`, `shrinkage_eye` or `diag`.
- **O4, how trials are split for the distances:** odd and even halves, or leave one repetition out.
- **O5, the confidence interval method:** DABEST's bias-corrected bootstrap, or a percentile bootstrap.
- **O6, how trials from different sessions are combined into one population:** matched by repetition index, or matched at random and resampled.
- **O7, the decoder for the generalization test:** the Methods' diagonal LDA, or a linear SVM.
- **O8, the accuracy that generalization is compared with:** decoding within each hand, or decoding finger type over both hands.
- **O9, what "close to" that accuracy means:** the paper gives no margin. I named two readings: at least 0.9 of it, or a ratio above J-PPC's 0.55, which the paper calls "much lower". The 0.9 is my own figure, so a checker may want to look at it.
- **O10, the inputs to the single-array BMI decoder:** threshold crossings, or sorted neurons.
- **Inside single claims:**
  - whether "mean number of significant fingers" and the share with large effect sizes are taken over selective neurons or over all neurons
  - whether the false discovery rate correction is applied per window or over both windows

**Missing from the text:**
- The contents of Supplementary Tables 1 (phase durations) and 2 (session dates); only their captions are there. No claim rests on them, because every analysis window is timed from a phase onset.
- The equation for the cross-validated distance; it is lost in the text, so I used its description in words.
- **Minor count mismatch:** the pooled right-hand-task neuron count in the Figure 4c legend (466) does not match 118 neurons per session over 4 sessions (472). The count claims accept counts taken before or after the 0.5 Hz exclusion.

## End of run

15 turns, 4 minutes, result: success.
