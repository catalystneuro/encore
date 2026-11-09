# crcns-fcx-3 · claims · run 42511760187

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453 claims/crcns-fcx-3 paper/ 2>&1; ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 185
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 165 more lines not kept]
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

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -30 paper/10.3389-fnsys.2018.00065.txt; cat paper/fcx-3.data-description.txt | head -80; cat tools/claims_check.py | head -60
```

Result: not kept, because it reads the paper's text.

**Agent**

Now read the full paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnsys.2018.00065.txt",
 "offset": 30
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 80,202p paper/fcx-3.data-description.txt; ls claims | head; ls claims | grep -i crcns
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  head -40 claims/crcns-fcx-1/*.yaml; grep -l "analysis_scripts\|deposited with the data\|code is part of" -r claims | head; grep -n "dataset:" -A3 claims/crcns-fcx-1/*.yaml | head; grep -n "code" docs/archives.md | head -20
```

```
# Claims for Watson, Levenstein, Greene, Gelinas & Buzsaki (2016), Neuron 90, 839-852, "Network
# homeostasis and state dynamics of neocortical sleep", doi:10.1016/j.neuron.2016.03.036, on CRCNS
# data set fcx-1 (doi:10.6080/K02N506Q).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the accepted author manuscript in PubMed Central (PMC4873379, NIHMS776601), as supplied
# under paper/: Introduction, Results, Discussion, Experimental Procedures, and the legends of
# Figures 1 to 6; with its supplement 1 (Table S1, legends of Figures S1 to S5, Supplemental
# Experimental Procedures, and the figure pages as extracted text) and supplement 2 (the Figure 1
# artwork as extracted text). The version of record was not read. No PDF of the main paper was
# supplied and the supplement PDF could not be rendered in this run, so values printed only inside
# Figures 2 to 5 (the per-sextile R and p of Fig. 3B and 4A-B iv, the n of each triplet class and
# the asterisks of Fig. 5B) were not read; claims on those figures rest on the Results and legends.
# The per-sextile R and p of Figure S5A and S5B and the R and p of Figure S3C and S5C to S5G come
# from the extracted text of the supplement figure pages; the S5C to S5G values carry their panel
# titles; the assignment of the two S5A/S5B lists to WAKE and REM is read from the extraction order
# and agrees with the Results for REM only.
#
# Code. The paper links no analysis code. Its methods name MATLAB, KlustaKwik, Klusters, the
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"; sed -n 40,92p claims/crcns-fcx-1/*.yaml
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
[... 182 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print(json.dumps(s['properties'].get('checks',{}),indent=1)[:800])"
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
[... 123 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml",
 "content": "# Claims for Johnson, King-Stephens, Weber, Laxer, Lin & Knight (2019), Front. Syst. Neurosci. 12,\n# 65, \"Spectral Imprints of Working Memory for Everyday Associations in the Frontoparietal Network\",\n# doi:10.3389/fnsys.2018.00065, on CRCNS data set fcx-3 (doi:10.6080/K06971S9).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-08,\n# protocol as stated in docs/protocol.md (Reader), version pilot-13.\n#\n# Text read: the version of record, PMC6333050 (open access), full text from Europe PMC JATS XML as\n# supplied under paper/: Introduction, Materials and Methods, Results, Discussion, Table 1 and the\n# legends of Figures 1 to 5. The paper has no supplement. No PDF was supplied, so values shown only\n# inside figures (per-subject accuracy and RT of Fig. 1B, per-subject PSI of Fig. 4A and 4C, the\n# time courses of Fig. 5) were not read; claims on those figures rest on the Results and legends.\n# The CRCNS data descriptor was read only to know which experiments the data set holds; no claim or\n# method comes from it.\n#\n# Code. The paper's Data Availability says its custom MATLAB code is deposited at CRCNS with the\n# data. By the data descriptor it is the analysis_scripts directory of data set fcx-3 itself. It is\n# one of the data set's files, which this reader does not open, so it was not read and no commit is\n# recorded. Every method below is from the paper's text. Where the scripts settle a detail named as\n# open below, the author may follow them (protocol, Reader step 2) and should say so.\n#\n# Data the paper used. Seven adults with epilepsy (25.4 +- 3.3 years, four males) with intracranial\n# electrodes (subdural and/or stereotactic) over lateral prefrontal (PFC) and parietal cortex, from\n# UC Irvine (three), CPMC (two), UCSF (one) and Oslo (one; sampled at 512 Hz, the others at or\n# resampled to 1 kHz). One session each of a visuospatial working memory task, 120 trials split\n# evenly between identity, spatial and temporal conditions. Trial phases: 1 s pretrial fixation,\n# 800 ms start screen (IDENTITY or RELATION), 100 ms fixation, two shapes of 200 ms each, 900 or\n# 1150 ms pre-cue delay (maintenance), 800 ms test cue (SAME, TOP/BOTTOM or FIRST/SECOND), post-cue\n# delay of the same length (processing), two-alternative forced choice. Measured: accuracy and RT\n# per trial; iEEG on 192 bipolar virtual electrodes (Table 1: per subject PFC/parietal 21/2, 24/8,\n# 54/14, 12/10, 10/16, 8/4, 4/5), 1129 same-hemisphere PFC-parietal pairs. Analysis segments,\n# correct trials only: 200 ms pretrial baseline (-250 to -50 ms before the start screen), 900 ms\n# maintenance from the offset of the second stimulus, 900 ms processing from the offset of the test\n# cue. The data descriptor says fcx-3 holds, for the 7 subjects, the filtered continuous iEEG with\n# per-trial event tables (accuracy, condition, jitter, RT, epoch starts), the preprocessed bipolar\n# epochs (pre, encmain, proc), channel MNI coordinates and the analysis scripts.\n#\n# Shared method details, used by the criteria below.\n# B1. Behavior (Methods, Behavioral Task, paragraph 3). Accuracy in a logit and correct-trial RT in a\n#   linear mixed-effects model, condition fixed, subject random; post hoc pairs only after a\n#   significant omnibus. The unit of observation is not stated. The reported degrees of freedom,\n#   F(1,19) for three conditions and F(1,12) for pairs, equal 7 x 3 - 2 and 7 x 2 - 2, so the RT\n#   models were fit to one value per subject and condition with condition as a single-df term and\n#   residual degrees of freedom (as MATLAB fitlme does by default); this is reading (a). Reading (b)\n#   fits single trials. For accuracy, reading (a) is the logit model on single correct/incorrect\n#   trials, (b) on per-subject proportions. Whether accuracy is over all 120 trials or over the\n#   trials kept after artifact rejection is not stated; readings (a) all trials, (b) kept trials.\n#   How Cohen's d was computed is not stated; d is reported, not judged.\n# S1. Power (Methods, Spectral Decomposition). Correct trials; time-frequency power 2 to 40 Hz in\n#   1-Hz steps, Hanning-tapered windows of 3 cycles (3/f s), stepped by 10 ms, segments zero-padded\n#   to 7500 ms. How windows longer than the 900 ms segment (below about 3.3 Hz) are formed is open;\n#   readings (a) the segment is embedded in zeros and every window is computed, (b) FieldTrip-style\n#   padding where windows that leave the data are not estimated. The paper reports effects from\n#   2 Hz, which only (a) yields; (a) is the main reading. Baseline: the 200 ms pretrial power of all\n#   correct trials pooled per channel and frequency; r points (r = the subject's number of trials)\n#   drawn and averaged 1000 times; each trial's processing power z-scored on the mean and SD of\n#   these 1000 averages. Whether r counts all correct trials or the trials of the condition is\n#   open; reading (a) all correct trials.\n# S2. Per-subject cluster test (Methods, Event-Related Potentials, paragraph 2, and Spectral\n#   Decomposition, paragraph 3). Identity against spatial, and identity against temporal, correct\n#   trials; independent-samples t-test per point, threshold 0.05 two-tailed; cluster mass is the sum\n#   of t; 1000 shuffles of condition labels; a cluster is significant when fewer than 5% of\n#   shuffles give a larger one. Clustering over electrode, time and frequency (power) or electrode\n#   and time (ERP). Which electrodes are neighbours is not stated (\"neighboring electrodes\");\n#   readings (a) bipolar channels adjacent on the same strip, grid or shaft, (b) channels within\n#   the 4 to 10 mm contact spacing in the subject's coordinates, (c) no spatial clustering. Whether\n#   the 5% is applied per tail or split between tails is not stated; readings (a) 0.05 per tail,\n#   (b) 0.025 per tail. An electrode shows an effect of a sign when any of its points lies in a\n#   significant cluster of that sign; its percentage is over all of the subject's analysed\n#   electrodes, averaged (mean +- SD) over the subjects showing that effect.\n# P1. Phase slope index (Methods, Directional Connectivity, Task-Induced PSI). Correct trials; the\n#   mean over the correct trials is subtracted from each trial (readings (a) over all correct\n#   trials, (b) over the trials of the condition); PFC-parietal pairs in the same hemisphere;\n#   positive PSI means PFC leads. Spectra \"using the same parameters described above, but over the\n#   full delay interval\"; readings (a) one Hanning-tapered FFT of each 900 ms segment, zero-padded\n#   to 7500 ms, read at 1-Hz steps, (b) the 3-cycle windows of S1 averaged over time. PSI per band,\n#   delta-theta 2 to 7 Hz and alpha-beta 9 to 24 Hz; readings (a) one PSI from the cross-spectra\n#   over all 1-Hz bins of the band (Nolte et al. 2008), (b) PSI per frequency with a 2-Hz\n#   bandwidth, averaged over the band. Null: the frequencies of one signal shuffled and PSI\n#   recomputed 1000 times; PSI z-scored on the null mean and SD. Whether one permutation serves all\n#   trials or each trial gets its own is open; readings (a) one per shuffle, (b) one per trial.\n#   PFC leads at z > 1.96, parietal leads at z < -1.96.\n# P2. Group models. Task-induced PSI z per pair and interval in a linear mixed-effects model with\n#   interval fixed and subject and pair random (Methods, Task-Induced PSI, paragraph 3);\n#   F(1,2256) equals 2 x 1129 - 2, residual degrees of freedom. Time-resolved PSI (Methods,\n#   Time-Resolved PSI): recomputed at 10-ms steps per condition on the pairs with |z| > 1.96 over\n#   the whole processing interval (all conditions), z-scored per time point; at each time point a\n#   model with condition fixed and subject and pair random; FDR 0.05 over time points (read as\n#   Benjamini-Hochberg over the time points of the 900 ms interval, a standard choice); an effect\n#   is sustained when significant time points run for at least 100 ms. Per-subject values are the\n#   mean z over the subject's pairs; group values are mean +- SEM (figures) or mean +- SD (text)\n#   over subjects.\n# T1. Tolerances. 10% of the reported value unless a claim says otherwise. A mean +- SD in the text\n#   is a spread over subjects, not an uncertainty of the mean, and is not used as a tolerance. A\n#   value printed as a bound (\"z < -40.03\") also matches when the result lies beyond the bound.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: fcx-3\n  doi: 10.6080/K06971S9\npaper: doi:10.3389/fnsys.2018.00065\nclaims:\n- id: table1-electrodes\n  statement: The analysed data comprise 192 bipolar virtual electrodes in seven subjects, 4 to 54\n    (mean 19) in PFC and 2 to 16 (mean 8) in parietal cortex per subject, as listed per subject in\n    Table 1, forming 1129 same-hemisphere PFC-parietal pairs.\n  source: Methods, Data Acquisition and Preprocessing, paragraph 2; Table 1; Results, Directional\n    Connectivity, paragraph 1\n  quote: The final dataset contained 192 virtual electrodes, range (mean) per subject... 4–54 (19)\n    PFC, 2–16 (8) parietal cortex\n  expected:\n  - quantity: virtual electrodes, all subjects\n    value: 192\n    tolerance: 0\n  - quantity: same-hemisphere PFC-parietal pairs\n    value: 1129\n    tolerance: 0\n  - quantity: mean PFC electrodes per subject\n    value: 19\n    tolerance: 1.9\n  - quantity: mean parietal electrodes per subject\n    value: 8\n    tolerance: 0.8\n  criterion: Counts of analysed channels and pairs are fixed by the paper's channel selection, not\n    estimates, so the totals are matched exactly. Reproduced when the analysed channels number 192\n    and each subject's PFC and parietal counts and hemispheres equal Table 1, and the\n    same-hemisphere PFC-parietal pairs number 1129. Partially reproduced when the totals differ by\n    no more than 10%.\n- id: trial-counts\n  statement: After artifact rejection subjects kept on average 96 correct trials, 32 +- 3 (26 to 35)\n    identity, 33 +- 4 (27 to 39) spatial and 31 +- 6 (20 to 39) temporal, and made 17 +- 8 (4 to\n    25) incorrect responses.\n  source: Methods, Data Acquisition and Preprocessing, paragraph 3\n  quote: The final dataset included an average of 96 correct trials per subject, mean ± SD (range)\n    trials... 32 ± 3 (26–35) identity, 33 ± 4 (27–39) spatial relation, 31 ± 6 (20–39) temporal\n    relation. There were too few incorrect trials for meaningful electrophysiological data\n    analysis, mean ± SD (range) trials... 17 ± 8 (4–25) per subject\n  expected:\n  - quantity: mean correct trials per subject\n    value: 96\n    tolerance: 9.6\n  - quantity: mean identity correct trials\n    value: 32\n    tolerance: 3.2\n  - quantity: mean spatial correct trials\n    value: 33\n    tolerance: 3.3\n  - quantity: mean temporal correct trials\n    value: 31\n    tolerance: 3.1\n  - quantity: mean incorrect trials per subject\n    value: 17\n    tolerance: 1.7\n  criterion: Means over the seven subjects of the counts of correct trials kept after rejection,\n    per condition. The ranges hold inside the reported ranges widened by 10% of each bound. The\n    incorrect count is read as (a) incorrect trials of all 120, (b) incorrect trials kept after\n    rejection. Reproduced when the means are within tolerance and the ranges hold under one\n    reading.\n- id: fig1b-accuracy\n  statement: All subjects were proficient at the task (accuracy 0.63 to 0.98, chance 0.5), and\n    accuracy did not differ between conditions.\n  source: Results, Behavior; Figure 1B, top\n  quote: We confirmed that all subjects were proficient at the task (accuracy range 0.63–0.98,\n    chance 0.5... but no effect on accuracy ( p > 0.50)\n  statistics:\n  - about: effect of condition on accuracy\n    test: logit mixed-effects model, condition fixed, subject random\n    p: 0.5\n    p_relation: \">\"\n    n: 7 subjects\n  expected:\n  - quantity: lowest subject accuracy\n    value: 0.63\n    tolerance: 0.063\n  - quantity: highest subject accuracy\n    value: 0.98\n    tolerance: 0.098\n  criterion: Accuracy as in B1. Whether the range is over per-subject accuracy across conditions or\n    over per-subject, per-condition values is not stated; readings (a) and (b) respectively. The\n    range holds when every value lies inside 0.63 to 0.98 widened by 10% of each bound under one\n    reading. The absence of a condition effect is judged on the paper's test, the logit\n    mixed-effects model of B1 (reading (a) on single trials, the model the Methods name): it holds\n    when p > 0.05 for condition, and is not reproduced when p < 0.05; the p obtained is compared\n    with the paper's p > 0.50 and reported.\n- id: fig1b-rt-identity-slower\n  statement: Response times differed by condition, being longer on identity than on spatial and\n    temporal trials, with no difference between spatial and temporal trials.\n  source: Results, Behavior; Figure 1B, bottom\n  quote: There was a significant effect of condition on RT ( F (1,19) > 6.50, p < 0.02, d > 1.47;\n    Figure 1B , bottom), but no effect on accuracy ( p > 0.50). Post hoc testing revealed that RTs\n    were longer on identity than spatial ( F (1,12) > 13.78, p < 3 × 10 −3 , d = 2.14) and temporal\n    ( F (1,12) > 10.95, p < 7 × 10 −3 , d = 1.91) trials, with no difference between spatial and\n    temporal trials ( p > 0.22)\n  statistics:\n  - about: effect of condition on RT\n    test: linear mixed-effects model, condition fixed, subject random\n    statistic: F(1,19) > 6.50, d > 1.47\n    p: 0.02\n    p_relation: \"<\"\n    n: 7 subjects\n  - about: identity against spatial RT\n    test: linear mixed-effects model, post hoc\n    statistic: F(1,12) > 13.78, d = 2.14\n    p: 0.003\n    p_relation: \"<\"\n  - about: identity against temporal RT\n    test: linear mixed-effects model, post hoc\n    statistic: F(1,12) > 10.95, d = 1.91\n    p: 0.007\n    p_relation: \"<\"\n  - about: spatial against temporal RT\n    test: linear mixed-effects model, post hoc\n    p: 0.22\n    p_relation: \">\"\n  criterion: Correct-trial RT, models as in B1 under readings (a) and (b). Reproduced when, under one\n    reading, the condition effect has p < 0.05, both identity post hoc tests have p < 0.05 with\n    identity RT longer, and spatial against temporal has p > 0.05; the F values obtained are\n    reported beside the paper's bounds. Partially reproduced when the condition effect and one of\n    the identity contrasts hold. The spatial-temporal absence is judged on the same model.\n- id: erp-no-condition-difference\n  statement: ERPs over the processing interval did not differ between identity and spatial or\n    temporal trials in any subject.\n  source: Results, ERPs\n  quote: Cluster-based permutation testing of identity vs. spatial/temporal trials indicated that\n    ERPs did not differ between conditions in any subject (all p > 0.10)\n  statistics:\n  - test: cluster-based permutation test, per subject\n    p: 0.1\n    p_relation: \">\"\n    corrected: cluster-based\n    n: 7 subjects, identity against spatial and against temporal\n  criterion: ERPs per Methods, Event-Related Potentials, paragraph 1 (correct trials, 200 ms\n    baseline and 900 ms processing segments zero-padded to 7500 ms, 30-Hz low-pass FIR, processing\n    minus the baseline's temporal mean), tested per subject as in S2 over electrodes and time. A\n    claim of absence judged on the paper's test. Reproduced when no subject has a significant\n    cluster (p < 0.05) in either contrast; not reproduced when any does. The smallest cluster p\n    per subject and contrast is reported and compared with the paper's p > 0.10. Neighbour\n    readings of S2 are each run.\n- id: fig2-spatial-power\n  statement: In the identity against spatial contrast of processing-interval power, 5 of 7 subjects\n    showed spatial > identity effects (54 +- 22% of electrodes per subject) and 2 of 7 showed\n    identity > spatial effects (36 +- 12%).\n  source: Results, Spectral Effects, paragraph 2; Figure 2\n  quote: In the contrast between identity and spatial trials (Figure 2 ), 5/7 (71%) subjects showed\n    significant spatial > identity effects (mean ± SD... 54 ± 22% of electrodes/subject) and 2/7\n    (29%) showed identity > spatial effects (36 ± 12% of electrodes/subject)\n  statistics:\n  - test: cluster-based permutation test, per subject\n    p: 0.04\n    p_relation: \"<\"\n    corrected: cluster-based\n    n: 7 subjects\n  expected:\n  - quantity: subjects with spatial > identity clusters\n    value: 5\n    tolerance: 0\n  - quantity: subjects with identity > spatial clusters\n    value: 2\n    tolerance: 0\n  - quantity: mean percent of electrodes with spatial > identity effects, over those subjects\n    value: 54\n    tolerance: 5.4\n    unit: percent\n  - quantity: mean percent of electrodes with identity > spatial effects, over those subjects\n    value: 36\n    tolerance: 3.6\n    unit: percent\n  criterion: Power and tests as in S1 and S2. The subject counts are small integers, so they are\n    matched exactly. Reproduced when, under one of the S1 and S2 readings, both counts match and\n    both percentages are within tolerance; partially reproduced when the counts match within one\n    subject and most subjects have a significant cluster (p < 0.05). The paper's \"all p < 0.04\"\n    is compared with the cluster p obtained.\n- id: fig3-temporal-power\n  statement: In the identity against temporal contrast of processing-interval power, 4 of 7\n    subjects showed temporal > identity effects (68 +- 30% of electrodes per subject) and 2 of 7\n    showed identity > temporal effects (37 +- 10%).\n  source: Results, Spectral Effects, paragraph 2; Figure 3\n  quote: In the contrast between identity and temporal trials (Figure 3 ), 4/7 (57%) subjects\n    showed significant temporal > identity effects (68 ± 30% of electrodes/subject) and 2/7 (29%)\n    showed identity > temporal effects (37 ± 10% of electrodes/subject)\n  statistics:\n  - test: cluster-based permutation test, per subject\n    p: 0.04\n    p_relation: \"<\"\n    corrected: cluster-based\n    n: 7 subjects\n  expected:\n  - quantity: subjects with temporal > identity clusters\n    value: 4\n    tolerance: 0\n  - quantity: subjects with identity > temporal clusters\n    value: 2\n    tolerance: 0\n  - quantity: mean percent of electrodes with temporal > identity effects, over those subjects\n    value: 68\n    tolerance: 6.8\n    unit: percent\n  - quantity: mean percent of electrodes with identity > temporal effects, over those subjects\n    value: 37\n    tolerance: 3.7\n    unit: percent\n  criterion: As fig2-spatial-power, for the identity against temporal contrast.\n- id: power-difficulty-subjects\n  statement: The subjects with identity > spatial or temporal power effects were the same subjects\n    who had both longer RTs and lower accuracy on identity trials.\n  source: Results, Spectral Effects, paragraph 2\n  quote: Importantly, the subjects who exhibited significant identity > spatial/temporal effects were\n    the same subjects who exhibited both increased RTs and decreased accuracy on identity trials\n  depends_on:\n  - fig2-spatial-power\n  - fig3-temporal-power\n  criterion: Subjects with a significant negative cluster (identity > spatial or identity >\n    temporal) are taken from the two power claims. Per subject, accuracy (B1) and mean correct RT\n    per condition. What identity is compared with is not stated; readings (a) in each contrast,\n    identity against that contrast's condition (spatial for the spatial contrast, temporal for the\n    temporal one), (b) identity against the mean of spatial and temporal. Reproduced when, under\n    one reading, every subject with an identity > spatial or temporal effect has identity RT longer\n    and identity accuracy lower than the comparison, and no other subject has both.\n- id: power-low-frequencies\n  statement: Significant processing-interval power effects were most prominent at low frequencies,\n    in distinct delta-theta (2 to 7 Hz) and alpha-beta (9 to 24 Hz) ranges, whatever the contrast.\n  source: Results, Spectral Effects, paragraph 3; Figures 2B and 3B\n  quote: Statistically significant effects were most prominent at lower frequencies, regardless of\n    the exact contrast. Specifically, information about the contents of working memory appeared to\n    be carried at distinct delta-theta (2–7 Hz) and alpha-beta (9–24 Hz) frequency ranges\n  depends_on:\n  - fig2-spatial-power\n  - fig3-temporal-power\n  criterion: Per subject and effect (spatial > identity, temporal > identity, and identity >\n    spatial or temporal), the t values inside significant clusters averaged over all electrodes\n    and processing time points (Results, Spectral Effects, paragraph 3), and the spectral density,\n    \"mean significant t-values per frequency\" (Figure 2B legend). Whether points outside the mask\n    enter the mean as zeros is open; readings (a) mean over masked points only, (b) mean over all\n    points with unmasked points as zero. Reproduced when, under one reading, the mean density over\n    subjects of each of the three effects is larger over 2 to 24 Hz than over 25 to 40 Hz and has\n    local maxima inside 2 to 7 Hz and inside 9 to 24 Hz; partially reproduced when the first part\n    holds and only one band has a maximum.\n- id: fig4-maintenance-parietal-led\n  statement: During maintenance, PFC-parietal connectivity was unidirectional, parietal to PFC, in\n    both the delta-theta (z < -40.03 +- 8.73) and alpha-beta (z < -30.37 +- 2.60) ranges.\n  source: Results, Task-Induced Effects, paragraph 1; Figure 4A and 4C\n  quote: The maintenance interval was characterized by unidirectional parietal → PFC connectivity in\n    both frequency ranges (threshold z < −1.96, p < 0.05), mean ± SD, delta-theta... z < −40.03 ±\n    8.73; alpha-beta... z < −30.37 ± 2.60\n  expected:\n  - quantity: mean delta-theta PSI z, maintenance\n    value: -40.03\n    tolerance: 4.0\n  - quantity: mean alpha-beta PSI z, maintenance\n    value: -30.37\n    tolerance: 3.04\n  criterion: PSI as in P1 on the 900 ms maintenance segments of all correct trials. Which values\n    the mean +- SD is taken over is not stated; readings (a) per-subject mean z over pairs, mean\n    and SD over the seven subjects, (b) mean and SD over all 1129 pairs pooled. Reproduced when,\n    under one reading of P1 and of the mean, every subject's mean z is below -1.96 in both bands\n    and both group means are within tolerance or more negative (T1); partially reproduced when\n    every subject is parietal-led (below -1.96) in both bands but a mean is outside tolerance.\n- id: fig4a-delta-theta-shift\n  statement: After the test cue, delta-theta directionality shifted from a unidirectional\n    parietal-led network to a bidirectional frontoparietal one, with net PFC-led connectivity\n    above zero in 6 of 7 subjects during processing (z > 6.01 +- 6.42).\n  source: Results, Task-Induced Effects, paragraph 1; Figure 4A and 4B\n  quote: However, following presentation of the test cue to select identity, spatial, or temporal\n    information from working memory stores, delta-theta directionality shifted from a\n    unidirectional to bidirectional frontoparietal network (processing > maintenance, F (1,2256) =\n    1936.10, p < 8 × 10 −306 ... Importantly, the processing interval was characterized by net\n    connectivity greater than zero in 6/7 subjects (86%), mean ± SD... z > 6.01 ± 6.42\n  statistics:\n  - test: linear mixed-effects model, interval fixed, subject and pair random\n    statistic: F(1,2256) = 1936.10\n    p: 8.0e-306\n    p_relation: \"<\"\n    n: 7 subjects, 1129 electrode pairs\n  expected:\n  - quantity: subjects with net delta-theta PSI z above zero, processing\n    value: 6\n    tolerance: 0\n  - quantity: mean delta-theta PSI z, processing\n    value: 6.01\n    tolerance: 0.6\n  - quantity: F statistic, processing against maintenance\n    value: 1936.10\n    tolerance: 193.6\n  criterion: PSI as in P1 on maintenance and processing segments of all correct trials; the model\n    of P2 on z per pair and interval. Whether the mean +- SD is over all seven subjects or over the\n    six with net values above zero is not stated; readings (a) seven, (b) six, each with the\n    per-subject mean z over pairs. Reproduced when processing z exceeds maintenance z with p <\n    0.05 in the model, the count of subjects is 6, and, under one reading, the mean is within\n    tolerance or larger (T1). Partially reproduced when the model effect holds with processing\n    higher and at least 4 subjects have net z above zero.\n- id: fig4c-alpha-beta-shift\n  statement: Alpha-beta directionality also shifted with the test cue, but all subjects remained\n    net parietal-led during processing (z < -12.60 +- 7.51).\n  source: Results, Task-Induced Effects, paragraph 3; Figure 4C and 4D\n  quote: In the alpha-beta range, there was again a shift in directionality with presentation of\n    the test cue (processing > maintenance, F (1,2256) = 2302.30, p = 0; Figures 4C,D ). Despite\n    the shift, however, all subjects continued to exhibit net parietal → PFC connectivity at\n    processing, mean ± SD... z < −12.60 ± 7.51\n  statistics:\n  - test: linear mixed-effects model, interval fixed, subject and pair random\n    statistic: F(1,2256) = 2302.30\n    p: 0\n    n: 7 subjects, 1129 electrode pairs\n  expected:\n  - quantity: mean alpha-beta PSI z, processing\n    value: -12.6\n    tolerance: 1.26\n  - quantity: F statistic, processing against maintenance\n    value: 2302.30\n    tolerance: 230.2\n  criterion: As fig4a-delta-theta-shift, for 9 to 24 Hz. Reproduced when processing z exceeds\n    maintenance z with p < 0.05, every subject's processing mean z is below zero, and the mean over\n    subjects is within tolerance or more negative (T1). Partially reproduced when the model effect\n    holds and at least 6 subjects stay below zero.\n- id: directional-pairs\n  statement: During processing, 1008 pairs were significantly directional in the delta-theta range\n    and 984 in the alpha-beta range.\n  source: Results, Directional Connectivity, paragraph 2; Methods, Time-Resolved PSI, paragraph 2\n  quote: Time-resolved PSI was re-computed per condition over the post-cue processing interval at all\n    electrode pairs that were found to be significantly directional overall during the processing\n    interval ( n = 1,008 delta-theta, 984 alpha-beta)\n  expected:\n  - quantity: delta-theta pairs with |z| > 1.96, processing\n    value: 1008\n    tolerance: 100.8\n  - quantity: alpha-beta pairs with |z| > 1.96, processing\n    value: 984\n    tolerance: 98.4\n  criterion: Pairs of the 1129 with processing-interval PSI |z| > 1.96 under P1, all correct trials.\n    Reproduced when both counts are within tolerance under one P1 reading.\n- id: fig5a-delta-theta-epochs\n  statement: Time-resolved delta-theta PSI differed between conditions in sustained epochs at 0 to\n    120 ms and 470 to 610 ms (identity against spatial) and at 0 to 170 ms and 660 to 860 ms\n    (identity against temporal) after the test cue, the spatial late epoch ending about 50 ms\n    before the temporal one begins.\n  source: Results, Spatiotemporal Processing Effects, paragraphs 1 and 3; Figure 5A\n  quote: In the contrast between identity and spatial conditions (left), significant differences\n    were sustained at the beginning (0–120 ms) and early in the second half (470–610 ms) of the\n    post-cue processing interval (FDR-corrected p < 0.05, marked in black). In the contrast between\n    identity and temporal conditions (right), significant differences were again sustained at the\n    beginning (0–170 ms) and in the second half (660–860 ms) of the processing interval\n  statistics:\n  - test: linear mixed-effects model per 10-ms time point, condition fixed, subject and pair random\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n    n: 7 subjects, 1008 delta-theta pairs\n  expected:\n  - quantity: identity-spatial early epoch end\n    value: 120\n    tolerance: 12\n    unit: ms\n  - quantity: identity-spatial late epoch start\n    value: 470\n    tolerance: 47\n    unit: ms\n  - quantity: identity-spatial late epoch end\n    value: 610\n    tolerance: 61\n    unit: ms\n  - quantity: identity-temporal early epoch end\n    value: 170\n    tolerance: 17\n    unit: ms\n  - quantity: identity-temporal late epoch start\n    value: 660\n    tolerance: 66\n    unit: ms\n  - quantity: identity-temporal late epoch end\n    value: 860\n    tolerance: 86\n    unit: ms\n  - quantity: gap between the spatial late epoch end and the temporal late epoch start\n    value: 50\n    tolerance: 20\n    unit: ms\n  depends_on:\n  - directional-pairs\n  criterion: Time-resolved PSI and model as in P2 on the delta-theta directional pairs, identity\n    against spatial and identity against temporal. The early epochs start at 0 ms, matched within\n    one 10-ms step. The gap is \"~50 ms\" on a 10-ms grid, so it is matched within one step on each\n    of its two bounds (20 ms). The early identity minus spatial or temporal difference is positive\n    and the late one negative (fig5a-identity-direction). Reproduced when, under one P1 reading,\n    each contrast has exactly one sustained early and one sustained late epoch with the reported\n    signs and bounds within tolerance; partially reproduced when the two early epochs hold and\n    each contrast has a sustained late epoch of the right sign, bounds outside tolerance.\n- id: fig5a-identity-direction\n  statement: In identity trials the PFC led parietal sites early in processing (z > 2.62 and\n    z > 2.35 in the two contrasts' early epochs) and the parietal cortex led later (z < -3.04 and\n    z < -3.57).\n  source: Results, Spatiotemporal Processing Effects, paragraph 2; Figure 5A\n  quote: Further examination of the early post-cue processing data (0–120/170 ms) indicated that the\n    PFC led parietal sites during the ongoing maintenance of identity information (mean, identity >\n    spatial... z > 2.62, p < 9 × 10 −3 ; identity > temporal... z > 2.35, p < 0.02). Later in\n    processing (470–610/660–860 ms), however, the parietal cortex led prefrontal sites (mean,\n    identity < spatial... z < −3.04, p < 3 × 10 −3 ; identity < temporal... z < −3.57, p < 4 × 10\n    −4 )\n  statistics:\n  - about: identity PSI, 0 to 120 ms\n    statistic: z > 2.62\n    p: 0.009\n    p_relation: \"<\"\n  - about: identity PSI, 0 to 170 ms\n    statistic: z > 2.35\n    p: 0.02\n    p_relation: \"<\"\n  - about: identity PSI, 470 to 610 ms\n    statistic: z < -3.04\n    p: 0.003\n    p_relation: \"<\"\n  - about: identity PSI, 660 to 860 ms\n    statistic: z < -3.57\n    p: 0.0004\n    p_relation: \"<\"\n  expected:\n  - quantity: identity delta-theta PSI z, 0 to 120 ms\n    value: 2.62\n    tolerance: 0.26\n  - quantity: identity delta-theta PSI z, 0 to 170 ms\n    value: 2.35\n    tolerance: 0.24\n  - quantity: identity delta-theta PSI z, 470 to 610 ms\n    value: -3.04\n    tolerance: 0.3\n  - quantity: identity delta-theta PSI z, 660 to 860 ms\n    value: -3.57\n    tolerance: 0.36\n  depends_on:\n  - fig5a-delta-theta-epochs\n  criterion: Identity-trial time-resolved delta-theta PSI z (P2) in the reported epochs. Each p\n    equals the two-tailed normal p of its z, so the p values follow from the z values. What is\n    averaged is not stated; readings (a) the grand mean over subjects (each the mean over its\n    pairs) averaged over the epoch's time points, (b) the same over all pairs pooled, (c) the\n    least extreme time point of the grand mean within the epoch (reading the printed bound). The\n    epochs are the reported ones; the epochs found in fig5a-delta-theta-epochs are shown as a\n    variant. Reproduced when, under one reading, all four values have the reported sign, |z| >\n    1.96, and lie within tolerance or beyond the bound (T1); partially reproduced when sign and\n    |z| > 1.96 hold for at least three.\n- id: fig5a-spatiotemporal-bidirectional\n  statement: Delta-theta PSI during the selection of spatial and of temporal information stayed\n    bidirectional (net near zero) throughout the processing interval.\n  source: Results, Spatiotemporal Processing Effects, paragraph 3; Figure 5A\n  quote: In contrast, the selection of spatial (Figure 5A , left) and temporal (right) information\n    exhibited bidirectionality throughout the processing interval (all | z | < 1.60, p > 0.11)\n  statistics:\n  - test: PSI z against frequency-shuffled surrogates\n    statistic: all |z| < 1.60\n    p: 0.11\n    p_relation: \">\"\n  depends_on:\n  - directional-pairs\n  criterion: Spatial-trial and temporal-trial time-resolved delta-theta PSI z (P2). A claim of\n    absence, judged on the paper's measure; the averaging readings of fig5a-identity-direction\n    apply, the paper's \"all\" read as every 10-ms time point of 0 to 900 ms (reading (i)) or every\n    reported epoch (reading (ii)). Reproduced when |z| < 1.96 (the paper's PSI threshold, Methods,\n    Task-Induced PSI) at every point under one reading; not reproduced when any point exceeds it\n    under all readings. The largest |z| is reported and compared with the paper's 1.60.\n- id: fig5b-alpha-beta-no-sustained\n  statement: Time-resolved alpha-beta PSI showed significant condition differences at some time\n    points but no sustained effect for either condition in either contrast.\n  source: Results, Spatiotemporal Processing Effects, paragraph 4; Figure 5B\n  quote: Although there were significant differences between conditions (FDR-corrected p < 0.05,\n    marked in black), the differences were not sustained for one condition or the other during\n    either condition-pair contrast\n  statistics:\n  - test: linear mixed-effects model per 10-ms time point, condition fixed, subject and pair random\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n    n: 7 subjects, 984 alpha-beta pairs\n  depends_on:\n  - directional-pairs\n  criterion: The P2 analysis on the alpha-beta directional pairs. A claim of absence judged on the\n    paper's test. Reproduced when at least one time point is significant after FDR and no run of\n    significant points of one sign lasts 100 ms in either contrast; not reproduced when a\n    sustained run exists. Partially reproduced when no time point is significant. Run lengths are\n    reported either way.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml paper/10.3389-fnsys.2018.00065.txt; grep -nP '^\s+[a-z_]+: [^"|>].*: ' claims/crcns-fcx-3/*.yaml | head; grep -nP '^\s+(- )?[^#]*—' claims/crcns-fcx-3/*.yaml | head; grep -n -i rather claims/crcns-fcx-3/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml; sed -i 's/the model the Methods name): it holds/the model the Methods name). It holds/' $f; grep -n ': .*: ' $f | grep -v '^[0-9]*:#' ; python tools/claims_check.py $f paper/10.3389-fnsys.2018.00065.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml`. The quote checker reports 17 claims, 17 quotes, 17 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the version of record (PMC6333050, Europe PMC full text): Methods, Results, Discussion, Table 1 and the legends of Figures 1 to 5. The paper has no supplement and no PDF was supplied, so I did not read values shown only inside figures (Fig. 1B per subject, Fig. 4A/4C per subject, Fig. 5 time courses). The claims on those figures rest on the Results and the legends. I read the data descriptor only to see what the dataset holds.

**Code.** The paper's MATLAB scripts are deposited inside the dataset itself, in its `analysis_scripts` folder. Since readers do not open the dataset's files, I did not read them and recorded no commit. The opening comment says the author may use them to settle any detail named as open below.

**Claims.** There are 17, all with quotes and all with criteria. 11 carry statistics (17 entries) and 11 carry expected values. All use the dataset alone; the paper uses no outside data. They cover:
- Electrode and pair counts (192 electrodes, 1129 pairs) and trial counts.
- Behaviour: accuracy range with no condition effect, and identity RTs longer than spatial and temporal.
- No ERP difference between conditions.
- Per-subject power effects for spatial (5/7 and 2/7 subjects) and temporal (4/7 and 2/7).
- The same subjects being slower and less accurate on identity trials.
- Power effects concentrated at low frequencies.
- Phase slope index (PSI) results: parietal-led during maintenance; the delta-theta shift after the cue (6/7 subjects net PFC-led); the alpha-beta shift that stays parietal-led; and the counts of directional pairs (1008 and 984).
- Time-resolved delta-theta effects: the sustained epochs, identity trials PFC-led early and parietal-led late, and spatial and temporal trials staying bidirectional.
- No sustained alpha-beta effects.

**Details the paper leaves open, with the readings named:**
- **Behaviour models:** the reported degrees of freedom imply one value per subject and condition (a); fitting single trials is (b). Accuracy is either over all 120 trials or over the trials kept after rejection. How Cohen's d was computed is not stated, so d is recorded but not judged.
- **Accuracy range:** per subject, or per subject and condition.
- **Power windows longer than the 900 ms segment:** zero-embedded so every window is computed (a), which is the only reading that yields the reported 2 Hz effects; or left unestimated (b).
- **Baseline bootstrap:** r is either all correct trials or the condition's trials.
- **Cluster test:** spatial neighbours are adjacent channels on the same strip or shaft, channels within the contact spacing, or no spatial clustering; alpha is 0.05 per tail or split between tails.
- **"Difficulty" comparison:** identity against the contrast's own condition, or against the mean of spatial and temporal.
- **Spectral density:** masked points only, or all points with unmasked points as zero.
- **PSI computation:**
  - Mean subtraction is over all correct trials or per condition.
  - The spectrum is one FFT of the whole segment or time-averaged sliding windows.
  - Band PSI is a single slope across the band's bins, or per-frequency PSI averaged over the band.
  - The frequency shuffle uses one permutation for all trials or one per trial.
- **What a group mean or SD is taken over:** subjects or pooled pairs; for the processing z of 6.01, all 7 subjects or the 6 with positive values.
- **Epoch z values:** the epoch mean, the pooled-pair mean, or the least extreme time point (reading the printed "z >" as a bound).
- **"All |z| < 1.60":** every time point, or every reported epoch.
- **FDR method:** read as Benjamini-Hochberg over time points, a standard choice the paper does not name.

**Missing from the paper.** No claim was blocked. Only the per-subject figure values (Fig. 1B, 4A and 4C) could not be read without a PDF.

## End of run

13 turns, 4 minutes, $1.29 at API prices, result: success.
