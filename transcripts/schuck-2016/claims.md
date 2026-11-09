# crcns-ofc-4 · claims · run 41886851998

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls claims/001453/ claims/crcns-ofc-4/ paper/ 2>&1
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
ls docs tools; ls claims | head -50; wc -l paper/*.txt; head -30 paper/10.1016-j.neuron.2016.08.019.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.08.019.txt",
 "limit": 1100
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.08.019.txt",
 "offset": 1100,
 "limit": 1170
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text, Methods and supplement are present. Now the data description, for what the dataset holds.

**Agent calls Read**

```json
{
 "file_path": "paper/ofc-4.data-description.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Let me look at a recent CRCNS claims file and the checker for format conventions.

**Agent calls Bash**

```bash
ls -d claims/crcns-* | head; ls claims/crcns-hc-9 claims/crcns-ia-1 2>/dev/null; sed -n 1,80p tools/claims_check.py
```

```
claims/crcns-hc-9
claims/crcns-ia-1
claims/crcns-ret-1
claims/crcns-hc-9:
10.1523-jneurosci.5680-12.2013.yaml

claims/crcns-ia-1:
10.3389-neuro.10.003.2008.yaml
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,60p claims/crcns-hc-9/*.yaml; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"
```

```
# Claims for Quattrocolo & Maccaferri (2013), J Neurosci 33:5486-5498, on CRCNS data set hc-9
# (doi:10.6080/K0HQ3WTH).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-04,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
# with its Materials and Methods, Results, Discussion and the legends of Figures 1 to 13. The
# paper has no supplement. It links no analysis code, so none was read. The PDF could not be
# rendered here, and the extracted text prints the signs =, < and > (and minus, plus/minus,
# mu, Omega) as a replacement character. Each p_relation below is read from the sentence it
# sits in: a difference the text calls significant, or a change it reports, is p < 0.05; one
# it calls absent ("did not change significantly", "similar", "ineffective", "returned to
# baseline") is p > 0.05. Values printed with that character between them are read as mean
# plus/minus SE, as the Methods state ("Data are presented as mean ±SE").
#
# Data the paper used. Acute hippocampal slices (350 um) from mice of either sex, P10 to P19:
# CXCR4-EGFP mice (Cajal-Retzius cells labelled by EGFP; 56 animals) and Sst-IRES-Cre;
# ChR2(H134R)-EYFP mice (8 animals) for the optogenetic experiments. Recordings at 30-32 C,
# filtered at 3 kHz and digitized at 10-20 kHz (Multiclamp 700, Clampex 9). Experiments:
# spontaneous GABAergic currents in Cajal-Retzius cells (Figure 1); paired recordings from
[... 245 more lines not kept]
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

**Agent**

No analysis code is linked (only LIBSVM, the Princeton MVPA toolbox, SPM8, PhysIO, neuRosim). I have what I need; writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "content": "# Claims for Schuck, Cai, Wilson & Niv (2016), Neuron 91:1402-1412, on CRCNS data set ofc-4\n# (doi:10.6080/K0FN14CH).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-04,\n# protocol as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record with its Supplemental Information, as supplied under paper/\n# (PyMuPDF text of the journal PDF): Summary, Results, Discussion, Experimental Procedures, the\n# legends of Figures 1 to 5, and the supplement (legends of Figures S1 to S5, Table S1, and the\n# Supplemental Results 1.1 to 1.5). The supplement's text carries line numbers between its\n# lines; quotes from it are cut with \"...\" at those breaks. The paper links no analysis code\n# (it names SPM8, the PhysIO toolbox, LIBSVM, the Princeton MVPA toolbox, R with lmer and boot,\n# neuRosim and AFNI), so no code was read. The data descriptor names BrainIAK for building\n# design matrices; that is not the paper's code.\n#\n# Data the paper used. 30 adults scanned, 3 excluded, 27 analysed (13 female, mean age 22.18,\n# range 18 to 31), most with five runs (mean 4.9). Face-house age-judgment task with\n# mini-blocks; 16 states from previous category, previous age, current category and current\n# age, labelled (Ho)Fy and so on; trial classes Enter (8 states, category switch), Internal\n# (4 states) and Exit (4 states). Five scanner runs, 485 trials in all, after three training\n# blocks of 97 trials outside the scanner. 3 T Siemens Skyra, EPI with TR 2.4 s, 46 slices.\n# Measured variables: per-trial state, correctness and reaction time; fMRI. Analyses on 27\n# participants, except the trial-wise decoding around errors (24 participants; two lost error\n# time stamps, one had errors only at the start of scans).\n#\n# The CRCNS data set, by its description, holds the 24 participants of the trial-wise analysis\n# (the first with four runs, the others five): slice-timing corrected and realigned fMRI time\n# series within each participant's OFC mask (the Kahnt et al. 2012 mask, in native space),\n# design matrices built with AFNI from boxcars from stimulus onset to response, with 16 state\n# columns plus 'first' and 'err', nuisance time courses (four Legendre drift terms and six\n# motion parameters), and per-state event files with onsets, reaction times and stimulus\n# durations. It holds no whole-brain data, no other ROI, no cardiac or respiratory regressors,\n# and no training-session data. Claims on whole-brain maps, other ROIs and training are kept\n# because they are main findings; their data are not in the description.\n#\n# Method details fixed by the paper (Experimental Procedures, fMRI Data Analysis, State Space\n# Similarities, Behavioral Analyses, and the Supplemental Results). The first trial of each\n# run, error trials and trials following errors are left out of all analyses but error rates.\n# GLM on realigned, non-normalized, unsmoothed data with one regressor per state (boxcar of\n# the trial's reaction time, convolved with the canonical HRF), nuisance regressors and the\n# run mean, giving one beta map per state and run. Beta maps z-scored and spatially smoothed\n# within each run. Linear SVM (LIBSVM, cost 1), leave-one-run-out, trained and tested on the\n# 16 states; the test set is the held-out run's beta maps. Component accuracies come from\n# comparing predicted and true state on each of the four components, with no new classifier.\n# Trial-wise decoding uses the same classifier, tested on raw data smoothed at FWHM 3 mm and\n# z-scored run-wise, taking the volume 2 TRs after stimulus onset (4.8 to 7.2 s). Similarity\n# is the Pearson correlation of OFC beta maps between runs (each run's maps against all maps\n# of the other runs, averaged, then averaged over runs), with negative correlations set to\n# NaN. Reaction times are medians within each factor cell. Mixed-effects models (lmer) have\n# participants as a random effect on the intercept and on the linear effect of trial or\n# errors, tested by Wald chi-square. Chance is 6.25% for 16-way, 12.5% for 8-way and 50% for\n# a component.\n#\n# Details the paper leaves open, used by several claims (each claim's criterion names those it\n# needs). (O1) The smoothing kernel for the beta maps is not given; readings are 3 mm FWHM, the\n# kernel given for the trial-wise test data, and no smoothing. Smoothing needs voxel positions;\n# if the data set has none, only the unsmoothed reading can be run. (O2) Which way the beta\n# maps are z-scored is not given; readings are (a) each voxel across the state maps of a run,\n# (b) each map across voxels. (O3) How trials following errors are left out of the GLM is not\n# given; readings are (a) as a separate nuisance regressor, (b) merged with the 'err'\n# regressor. (O4) Where a t-test against chance is not said to be one-sided, the side is open;\n# readings are one-sided (as the paper states for Figure 2B and Figure S2) and two-sided.\n# (O5) The paper's GLM had 26 cardiac regressors and SPM8; the data set's design matrix was\n# built with AFNI and has drift and motion terms only. The paper's nuisance set cannot be\n# rebuilt from the data set as described, which the author records as a deviation.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: ofc-4\n  doi: 10.6080/K0FN14CH\npaper: doi:10.1016/j.neuron.2016.08.019\nclaims:\n- id: behavior-error-rate\n  statement: Participants performed the task nearly without errors, with a mean error rate of\n    2.3% in the scanner.\n  source: Results, paragraph 4 (after Figure 1); Supplemental Results 1.1\n  quote: \"Participants performed the task with near optimal performance (mean error rate: 2.3%; Figure S1)\"\n  expected:\n    quantity: mean error rate in the scanner\n    value: 2.3\n    tolerance: 0.23\n    unit: percent\n  criterion: Error rate as error and time-out responses (both led to feedback, Methods, Task)\n    over all responded trials of the five runs, per participant, then the mean over\n    participants. The denominator is open; readings are (a) all trials including the\n    repetitions that follow errors, (b) all trials but the first of each run. Reproduced when\n    under one reading the mean is within tolerance. The data set holds 24 of the 27\n    participants, so the value is compared as given and the subset is noted.\n- id: supp-errors-by-trial-class\n  statement: Error rates differed by trial class (Enter 3.4%, Exit 2.3%, Internal 1.4%).\n  source: Supplemental Results 1.1, paragraph 1\n  quote: but were affected by the class ... of the trial (Enter 3.4%, Exit 2.3%, Internal 1.4%\n  statistics:\n  - test: mixed-effects model, Wald chi-square\n    statistic: χ2(2) = 20.8\n    p: 0.001\n    p_relation: \"<\"\n    n: 27 participants\n  expected:\n  - quantity: error rate, Enter trials\n    value: 3.4\n    tolerance: 0.34\n    unit: percent\n  - quantity: error rate, Exit trials\n    value: 2.3\n    tolerance: 0.23\n    unit: percent\n  - quantity: error rate, Internal trials\n    value: 1.4\n    tolerance: 0.14\n    unit: percent\n  criterion: Trial class of each trial from its state (Enter when previous and current category\n    differ, Internal when category and age repeat, Exit when the age changes; Figure S1). A\n    mixed-effects model of errors on trial class with participants as random intercept, tested\n    by Wald chi-square (Methods, Behavioral Analyses). The model family is open; readings are\n    (a) a linear mixed model on each participant's error rate per class, (b) a logistic mixed\n    model on trial-wise errors. Reproduced when under one reading the class effect has p <\n    0.001, the three rates are within tolerance and their order is Enter, Exit, Internal.\n- id: supp-errors-stable-over-blocks\n  statement: Error rates did not change over the blocks of the main experiment.\n  source: Supplemental Results 1.1, paragraph 1\n  quote: Behavioral error rates were 2.3% during the main experiment, with no evidence for error\n    rates ... changing over time (main effect Block\n  statistics:\n  - test: mixed-effects model, main effect of block, Wald chi-square\n    statistic: χ2(1) = 0.08\n    p: 0.77\n    n: 27 participants\n  criterion: A claim of absence. A mixed-effects model of errors on block (scanner run) as a\n    linear term, participants as random effect on intercept and on the block slope (Methods,\n    Behavioral Analyses), Wald chi-square at p < 0.05. Reproduced when the block effect is not\n    significant; the slope is reported either way. The model family is open as in\n    supp-errors-by-trial-class; both readings are shown and the absence is judged on (a).\n- id: supp-errors-not-by-age-category\n  statement: Error rates were not affected by the age or the category judged, nor by their\n    interaction.\n  source: Supplemental Results 1.1, paragraph 1\n  quote: Error rates were not affected by factors Age, Category or their interaction (all p’s > .13)\n  statistics:\n  - test: mixed-effects model, Wald chi-square\n    p: 0.13\n    p_relation: \">\"\n    n: 27 participants\n  criterion: A claim of absence. A mixed-effects model of errors on current age, current\n    category and their interaction, participants as random intercept, Wald chi-square at p <\n    0.05. Reproduced when none of the three terms is significant. Model family as in\n    supp-errors-by-trial-class, judged on reading (a), with (b) shown.\n- id: supp-training-errors-higher\n  statement: Errors were higher during training than in the main experiment in the scanner.\n  source: Supplemental Results 1.1, paragraph 1\n  quote: errors were significantly higher during ... training than during the main experiment, t(26) = 5.6, p < .001\n  statistics:\n  - test: t-test\n    statistic: t(26) = 5.6\n    p: 0.001\n    p_relation: \"<\"\n    n: 27 participants\n  criterion: Paired t-test across participants of training against scanner error rates.\n    Needs the training session (three blocks of 97 trials outside the scanner), which the data\n    set's description does not list.\n- id: supp-training-rt-unchanged\n  statement: Reaction times did not change between training and the main experiment (991\n    against 985 ms).\n  source: Supplemental Results 1.1, paragraph 1\n  quote: not change between training and main experiment (991 vs 985 ms, t(26) = 0.27, p = .79)\n  statistics:\n  - test: t-test\n    statistic: t(26) = 0.27\n    p: 0.79\n    n: 27 participants\n  criterion: A claim of absence, judged by a paired t-test at p < 0.05 on per-participant\n    median RTs. Needs the training session, which the data set's description does not list.\n- id: supp-rt-stable-over-blocks\n  statement: Reaction times did not change between blocks of the main experiment.\n  source: Supplemental Results 1.1, paragraph 1\n  quote: nor ... between blocks within the main experiment (χ2(1) = 1.7, p = .18)\n  statistics:\n  - test: mixed-effects model, Wald chi-square\n    statistic: χ2(1) = 1.7\n    p: 0.18\n    n: 27 participants\n  criterion: A claim of absence. Per participant and block, the median RT of correct trials\n    (Methods, Behavioral Analyses, RTs are medians within each factor cell); a linear mixed\n    model of RT on block as a linear term with participants as random effect on intercept and\n    slope, Wald chi-square at p < 0.05. Reproduced when the block effect is not significant.\n    Whether error trials enter the RT medians is open; readings are correct trials only (the\n    paper leaves error trials out of all but error-rate analyses) and all responded trials.\n- id: supp-rt-faces-faster\n  statement: Reaction times were faster for faces than for houses (944 against 1028 ms), with no\n    effect of age and no interaction.\n  source: Supplemental Results 1.1, paragraph 1\n  quote: by age (p = .67), but were faster for faces than for houses (944 vs 1028 ms\n  statistics:\n  - about: category\n    test: mixed-effects model, Wald chi-square\n    statistic: χ2(1) = 78.3\n    p: 0.001\n    p_relation: \"<\"\n  - about: age\n    test: mixed-effects model, Wald chi-square\n    p: 0.67\n  - about: age by category interaction\n    test: mixed-effects model, Wald chi-square\n    p: 0.98\n  expected:\n  - quantity: median RT, faces\n    value: 944\n    tolerance: 94.4\n    unit: ms\n  - quantity: median RT, houses\n    value: 1028\n    tolerance: 102.8\n    unit: ms\n  criterion: Per participant, median RT of correct trials in each cell of current category by\n    current age; a linear mixed model of these medians on category, age and their interaction\n    with participants as random intercept, Wald chi-square. The RT for faces and houses is the\n    mean over participants of their category medians; whether it is that or the median over\n    trials pooled is open, and both are shown. Reproduced when the category effect has p <\n    0.001 with faces faster, the age effect and interaction have p > 0.05, and both RTs are\n    within tolerance under one reading.\n- id: supp-rt-by-trial-class\n  statement: Reaction times differed by trial class, slightly faster on repeat (Internal) trials\n    than on the other classes.\n  source: Supplemental Results 1.1, paragraph 1\n  quote: RTs were also affected by trial ... class with slightly faster trials in Repeat than in the other trial classes\n  statistics:\n  - test: mixed-effects model, Wald chi-square\n    statistic: χ2(2) = 153.7\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Per participant, median RT of correct trials per trial class; a linear mixed model\n    on trial class with participants as random intercept, Wald chi-square. \"Repeat\" is read as\n    the Internal class, the trials in which category and age repeat (Figure 1 legend).\n    Reproduced when the class effect has p < 0.001 and the Internal median is below both the\n    Enter and the Exit median.\n- id: fig2a-16way-decoding\n  statement: The 16 task states can be decoded from multivoxel patterns in anatomically defined\n    OFC above chance (mean 12.2% against 6.25%).\n  source: Results, paragraph 5; Figure 2A\n  quote: we could decode significantly above chance in which of the 16 possible task-states\n    participants were during the task (mean classification accuracy 12.2%, i.e., almost twice the 6.25% chance baseline\n  statistics:\n  - test: t-test against chance\n    statistic: t26 = 9.04\n    p: 0.001\n    p_relation: \"<\"\n    n: 27 participants\n  expected:\n    quantity: mean 16-way classification accuracy in OFC\n    value: 12.2\n    tolerance: 1.22\n    unit: percent\n  criterion: As the Methods (fMRI Data Analysis) fix it. One beta map per state and run from a\n    GLM of the OFC time series with the 16 state regressors, the 'first' and 'err' regressors,\n    nuisance regressors and the run mean; the beta maps z-scored and smoothed within run\n    (open, O1 and O2); linear SVM, cost 1, leave-one-run-out, tested on the held-out run's 16\n    beta maps; accuracy per participant over all test maps. One-sample t-test of the\n    participants' accuracies against 6.25%, side open (O4). Post-error trials as O3.\n    Reproduced when under one reading the mean is within tolerance and p < 0.001; partially\n    reproduced when the accuracy is above chance at p < 0.05 but outside tolerance.\n- id: fig2-two-back-state-space\n  statement: A classifier for an alternative 16-state space built from the task-irrelevant\n    category and age of two trials back decodes worse than the hypothesized state space (8.1%\n    against 12.2%).\n  source: Results, paragraph 5\n  quote: Training and testing a classifier on this state space resulted in lower 16-way\n    classification compared to the hypothesized state space (8.1% versus 12.2%, t26 = 2.8, p = 0.01)\n  statistics:\n  - test: t-test\n    statistic: t26 = 2.8\n    p: 0.01\n    n: 27 participants\n  depends_on:\n  - fig2a-16way-decoding\n  expected:\n    quantity: mean 16-way accuracy, two-back state space\n    value: 8.1\n    tolerance: 0.81\n    unit: percent\n  criterion: States relabelled by current category and age with the category and age of two\n    trials back in place of one trial back (Results, paragraph 5), each trial's label taken\n    from the trial sequence; a new GLM with these 16 regressors, then the analysis of\n    fig2a-16way-decoding unchanged. Paired t-test across participants against the\n    hypothesized space, two-sided (the paper does not say one-sided here). Reproduced when the\n    two-back accuracy is within tolerance and below the hypothesized accuracy with p < 0.05.\n    How trials are labelled when two trials back is the first trial of a run or an error is\n    open; readings are leaving such trials out (as a nuisance regressor) and labelling them\n    from the trials as presented.\n- id: fig2b-hidden-components\n  statement: Within the 16-way classification, the three hidden, task-relevant components\n    (previous category, previous age, current category) are each classified above chance.\n  source: Results, paragraph 5; Figure 2B\n  quote: In contrast, the category and age from one trial ago, as well as the current category—all hidden and\n    task-relevant components—were classified above chance\n  statistics:\n  - about: previous category\n    test: t-test against chance, one-sided\n    statistic: t26 > 3\n    p: 0.014\n  - about: previous age\n    test: t-test against chance, one-sided\n    statistic: t26 > 3\n    p: 0.003\n  - about: current category\n    test: t-test against chance, one-sided\n    statistic: t26 > 3\n    p: 0.007\n  depends_on:\n  - fig2a-16way-decoding\n  criterion: From the predictions of fig2a-16way-decoding, each test map scored correct on a\n    component when predicted and true state agree on it (Methods, fMRI Data Analysis); per\n    participant the proportion correct; one-sided one-sample t-test against 50%. Reproduced\n    when all three components have p < 0.05; partially reproduced when one or two do.\n- id: fig2b-current-age-absent\n  statement: The observable component, current age, is not classified above chance within the\n    16-way classification.\n  source: Results, paragraph 5; Figure 2B\n  quote: the analysis revealed no evidence that the current age, which was task-relevant but\n    observable given the current category, contributed to state representations in the OFC\n    (rightmost bar in Figure 2B, p > 0.72\n  statistics:\n  - test: t-test against chance, one-sided\n    p: 0.72\n    p_relation: \">\"\n  depends_on:\n  - fig2a-16way-decoding\n  criterion: A claim of absence. Current-age accuracy as in fig2b-hidden-components, one-sided\n    one-sample t-test against 50% at p < 0.05. Reproduced when the test is not significant.\n- id: fig2b-two-back-absent\n  statement: The task-irrelevant category and age from two trials back are not classified above\n    chance by the two-back classifier.\n  source: Results, paragraph 5; Figure 2B\n  quote: This analysis confirmed that no information about irrelevant events from two trials ago\n    could be detected (two leftmost bars in Figure 2B, p > 0.66)\n  statistics:\n  - test: t-test against chance, one-sided\n    p: 0.66\n    p_relation: \">\"\n  depends_on:\n  - fig2-two-back-state-space\n  criterion: A claim of absence. Component accuracies for category and age of two trials back\n    from the predictions of fig2-two-back-state-space, one-sided one-sample t-test against\n    50% at p < 0.05. Reproduced when neither is significant.\n- id: figs2c-8way-decoding\n  statement: Decoding an 8-state space without current age (previous category, previous age,\n    current category) is above chance (16.7%), and its three components are decoded above\n    baseline (53.5%, 52.9%, 55.5%).\n  source: Results, paragraph 6; Supplemental Results 1.2, paragraph 2; Figure S2C\n  quote: Decoding eight different states in the OFC in this manner, we indeed found significant\n    decoding accuracy, albeit at a slightly lower level relative to chance baseline (16.7%,\n    corresponding to 4.2% above chance baseline, t26 = 3.3, p = 0.002); all components involved\n    in this reduced state space also showed above baseline decoding (53.5%, 52.9%, and 55.5%\n  statistics:\n  - about: 8-way accuracy against chance, main text\n    test: t-test against chance\n    statistic: t26 = 3.3\n    p: 0.002\n    n: 27 participants\n  - about: 8-way accuracy against chance, Supplemental Results 1.2\n    test: t-test against chance\n    statistic: t26 = 6.6\n    p: 0.001\n    p_relation: \"<\"\n  - about: previous category\n    test: t-test against chance\n    p: 0.03\n  - about: previous age\n    test: t-test against chance\n    p: 0.09\n  - about: current category\n    test: t-test against chance\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: mean 8-way accuracy\n    value: 16.7\n    tolerance: 1.67\n    unit: percent\n  - quantity: previous category accuracy, 8-way\n    value: 53.5\n    tolerance: 5.35\n    unit: percent\n  - quantity: previous age accuracy, 8-way\n    value: 52.9\n    tolerance: 5.29\n    unit: percent\n  - quantity: current category accuracy, 8-way\n    value: 55.5\n    tolerance: 5.5\n    unit: percent\n  criterion: States with different current ages modelled as the same event type (Figure S2C\n    legend), giving 8 regressors; then the analysis of fig2a-16way-decoding with chance 12.5%\n    and components against 50%. The paper reports the test twice with different numbers (main\n    text 4.2% above chance, t26 = 3.3; supplement 8.5% above chance, t26 = 6.6; 16.7 less\n    12.5 is 4.2) and calls previous age above baseline in the main text but marginal (p = .09)\n    in the supplement. Reproduced when the 8-way mean is within tolerance with p < 0.05 against\n    12.5%, and previous category and current category are above 50% at p < 0.05; the previous\n    age result is reported against both statements. The 10% tolerance on the component\n    accuracies spans chance, so they are judged on their tests.\n- id: figs2a-permutation-control\n  statement: Classifiers trained on permuted labels decode at chance, and the real decoding is\n    above the permutation results for the 16-way classification and each binary component.\n  source: Results, paragraph 7; Supplemental Results 1.2, paragraph 1; Figure S2A\n  quote: First, a permutation analysis showed at chance decoding levels and was significantly\n    lower than decoding on the real data, both in the 16-way analysis as well as regarding the\n    binary classification (see black bar in Figures 2A and S2A, all p < 0.025)\n  statistics:\n  - test: permutation test\n    p: 0.025\n    p_relation: \"<\"\n  depends_on:\n  - fig2a-16way-decoding\n  expected:\n  - quantity: upper 95th percentile of permutation accuracy, 16-way\n    value: 7.04\n    tolerance: 0.704\n    unit: percent\n  - quantity: upper 95th percentile, previous category\n    value: 51.5\n    tolerance: 0.15\n    unit: percent\n  - quantity: upper 95th percentile, previous age\n    value: 51.7\n    tolerance: 0.17\n    unit: percent\n  - quantity: upper 95th percentile, current category\n    value: 51.4\n    tolerance: 0.14\n    unit: percent\n  - quantity: upper 95th percentile, current age\n    value: 51.7\n    tolerance: 0.17\n    unit: percent\n  criterion: Training labels permuted in each fold, 10 permutations per participant, accuracies\n    averaged within participant, test labels unchanged (Supplemental Results 1.2). The\n    component tolerances are 10% of the distance from chance (1.5 to 1.7 points), as 10% of\n    the value would span chance. The distribution whose 95th percentile is reported, and the\n    test behind p < 0.025, are open; readings are (a) the participants' averaged permutation\n    accuracies, with a paired t-test of real against permuted; (b) all participant and\n    permutation values pooled, with the real group mean compared to the percentile.\n    Reproduced when under one reading the permuted 16-way mean is not above 6.25% at p < 0.05\n    and the real 16-way accuracy exceeds the permuted at p < 0.025; the percentiles are\n    compared with the expected values and reported.\n- id: synthetic-data-control\n  statement: Decoding on synthetic fMRI data with univariate stimulus-driven OFC activation and\n    each participant's event timing is not above chance (6.8%).\n  source: Results, paragraph 7; Experimental Procedures, Synthetic fMRI Data and Noise Simulations\n  quote: This analysis also showed no above-chance decoding (mean accuracy across simulated\n    ‘‘participants’’ 6.8%, p = 0.43 when compared to the chance baseline of 6.25%)\n  statistics:\n  - test: comparison with chance baseline\n    p: 0.43\n  expected:\n    quantity: mean 16-way accuracy on synthetic data\n    value: 6.8\n    tolerance: 0.68\n    unit: percent\n  criterion: A claim of absence. Synthetic data made with neuRosim as the Methods give (one\n    spherical OFC peak of mean size 5 voxels, SD 1, fading 0.01, at each participant's peak of\n    decoding plus spatial noise of mean 3 and SD 2 voxels; state amplitudes from a normal\n    distribution of mean 25, SD 5; double-gamma HRF; default noise mixture, baseline 10, SNR\n    2.87; smoothed to the real data's smoothness), then the analysis of fig2a-16way-decoding.\n    The participant's peak is read as the peak of the conjunction searchlight within OFC\n    (Figure S3C); the searchlight radius is not given anywhere and is open, with 2 and 3 voxels\n    as the readings run (a standard choice, not the paper's). The test is not named; reading,\n    a one-sample t-test against 6.25%. Reproduced when that test is not significant at p <\n    0.05; the mean is reported against 6.8%. Being a simulation, the result is reported over\n    at least 10 random seeds.\n- id: fig2c-enter-cluster\n  statement: In the similarity structure of OFC state patterns, pairs of states are more similar\n    when both are Enter or both non-Enter states than when they differ.\n  source: Results, paragraph 9; Figure 2C\n  quote: indicates that pairs of activity patterns were indeed more similar if two states were\n    both Enter or both non-Enter states (p < 0.01; paired t test comparing each subjects’\n    average within-class versus between-class correlations)\n  statistics:\n  - test: paired t test\n    p: 0.01\n    p_relation: \"<\"\n    n: 27 participants\n  criterion: Per participant, the 16 by 16 between-run correlation matrix of OFC beta maps as\n    in the Methods (State Space Similarities), negative values set to NaN. Mean within-class\n    (Enter with Enter, non-Enter with non-Enter) against mean between-class correlation, paired\n    t-test across participants. Whether the diagonal (a state with itself across runs) is in\n    the within-class mean is open; readings are without and with it. Whether the beta maps\n    are z-scored and smoothed first, as for classification, is open (O1, O2). The dendrogram's\n    linkage method is not given and is shown only. Reproduced when under one reading\n    within-class exceeds between-class at p < 0.01; partially reproduced at p < 0.05.\n- id: fig2d-enter-nonenter-decoding\n  statement: All three hidden components are decoded above chance even when the 16-way\n    classifier is tested separately on Enter and on non-Enter trials.\n  source: Results, paragraph 9; Figure 2D\n  quote: a decoding analysis done separately for Enter and non-Enter trials that showed that\n    even within these subsets of trials the 16-way classifier could successfully detect all\n    three hidden state components (Figure 2D, all t26 > 2, p < 0.05\n  statistics:\n  - test: t-test against chance\n    statistic: t26 > 2\n    p: 0.05\n    p_relation: \"<\"\n    n: 27 participants\n  depends_on:\n  - fig2a-16way-decoding\n  criterion: The classifiers of fig2a-16way-decoding unchanged; the test set split into the 8\n    Enter and 8 non-Enter state maps, component accuracies computed in each subset and then\n    averaged within participant (Methods, fMRI Data Analysis); one-sample t-test against 50%,\n    one-sided as in the Figure 2 and S2 legends (two-sided shown). Which averages are tested\n    is open; readings are (a) per component, the mean of the Enter and non-Enter accuracies,\n    (b) per component and subset, each of the six tested. Reproduced when under one reading\n    all tested accuracies have p < 0.05.\n- id: fig3-searchlight-conjunction\n  statement: In whole-brain searchlight decoding, medial OFC is the only area where all three\n    hidden components are decoded together, peaking in the left medial orbital gyrus at MNI [3,\n    44, -14].\n  source: Results, paragraph 10; Figure 3E; Table S1\n  quote: a voxel-wise conjunction analysis on the information maps of hidden state components\n    confirmed that, across participants, only medial OFC activity carried complete information\n    about all three hidden state components\n  statistics:\n  - test: voxel-wise conjunction, uncorrected\n    statistic: Zpeak = 3.14\n    p: 0.01\n    p_relation: \"<\"\n    n: 27 participants\n  expected:\n    quantity: conjunction peak Z\n    value: 3.14\n    tolerance: 0.314\n  criterion: Needs whole-brain data in MNI space (16-way searchlight, component maps, group\n    t-tests, conjunction at p < 0.01 uncorrected per component, minimum cluster 5 voxels),\n    which the data set's description does not list; it holds OFC voxels in native space only.\n    The searchlight radius is not given (open).\n- id: other-rois-incomplete\n  statement: Hippocampus, DLPFC and FFA/PPA code current and previous category but not previous\n    age, and show neither complete nor task-specific encoding; decoding there is not related to\n    error rates or behavior as it is in OFC, except a weaker relation in PPA/FFA.\n  source: Results, paragraphs 10, 11 and 15; Figure S2D to S2F\n  quote: None of these areas showed either complete encoding of all hidden state components nor\n    specific encoding of only task-relevant variables\n  statistics:\n  - about: correlation of decoding with error rate, PPA/FFA\n    test: Pearson correlation\n    statistic: r = -0.40, t25 = -2.2\n    p: 0.03\n  - about: correlation of decoding with error rate, hippocampus and DLPFC\n    test: Pearson correlation\n    p: 0.14\n    p_relation: \">\"\n  - about: similarity and error rate, hippocampus, DLPFC, FFA/PPA\n    p: 0.17\n    p_relation: \">\"\n  criterion: Needs the hippocampus, DLPFC and PPA/FFA ROIs (AAL labels, Methods), which the data\n    set's description does not list.\n- id: fig4a-decoding-error-correlation\n  statement: Across participants, mean classification accuracy of the three hidden components in\n    OFC correlates negatively with error rate.\n  source: Results, paragraph 11; Figure 4A; Figure S4\n  quote: participants’ average error rates were significantlycorrelated with themean\n    classificationaccuracyofallthree hidden state components\n  statistics:\n  - test: Pearson correlation\n    statistic: r = -0.58, t25 = -3.6\n    p: 0.002\n    ci:\n      level: 0.95\n      low: -0.8432\n      high: -0.0169\n    n: 27 participants\n  depends_on:\n  - fig2b-hidden-components\n  expected:\n    quantity: Pearson r, error rate against mean hidden-component accuracy\n    value: -0.58\n    tolerance: 0.2632\n  criterion: Per participant, the mean of the three hidden-component accuracies of\n    fig2b-hidden-components and the scanner error rate of behavior-error-rate; Pearson\n    correlation, and a bootstrap 95% CI over participants with the boot package defaults. The\n    number of bootstrap iterations is given as 10,000 (Methods) and 1000 (Supplemental Results\n    1.4, Figure S4); both are run. The tolerance is the distance from r to the nearer bound of\n    the paper's CI. Reproduced when r is negative with p < 0.05 and within tolerance;\n    partially reproduced when r lies inside the paper's CI but outside the tolerance. The data\n    set holds 24 of the 27 participants.\n- id: fig4b-error-trial-drop\n  statement: Trial-wise 16-way decoding is lower on error trials (4.2%) than in the five trials\n    preceding an error (11%).\n  source: Results, paragraph 12; Figure 4B\n  quote: incorrect responses were accompanied by worse classification—the average 16-way\n    classification in the five trials preceding an error was 11% whereas accuracy was only 4.2%\n    on error trials (t23 = 2.2, p = 0.04\n  statistics:\n  - test: t-test\n    statistic: t23 = 2.2\n    p: 0.04\n    n: 24 participants\n  depends_on:\n  - fig2a-16way-decoding\n  expected:\n  - quantity: 16-way accuracy, five trials before an error\n    value: 11\n    tolerance: 1.1\n    unit: percent\n  - quantity: 16-way accuracy, error trials\n    value: 4.2\n    tolerance: 0.42\n    unit: percent\n  criterion: Trial-wise test data as the Methods fix it (raw time series smoothed at FWHM 3 mm,\n    z-scored per run, the volume 2 TRs after stimulus onset, 4.8 to 7.2 s), classified by the\n    classifier trained on the other runs in fig2a-16way-decoding. The true state of an error\n    trial is the state the task rules assign to it; how it is reconstructed is not stated, and\n    the reading is from the trial sequence. Errors whose five preceding trials do not lie in\n    the run are left out (Methods, Participants). Per participant, mean accuracy over the five\n    preceding trials and over error trials; paired t-test, two-sided. Reproduced when both\n    values are within tolerance and the difference has p < 0.05; partially reproduced when the\n    difference holds but a value is outside tolerance. Which volume is \"2 TRs after onset\" is\n    open; readings are the first volume acquired at or after onset plus 4.8 s, and the volume\n    nearest onset plus 4.8 s.\n- id: fig4b-decline-before-errors\n  statement: Decoding accuracy declines linearly over the trials leading up to and including an\n    error, and no such decline is seen in matched time courses without errors.\n  source: Results, paragraph 12; Figure 4B\n  quote: there was a negative linear effect of trial on decoding in the trials leading up to and\n    including an error ... No such decrease was detected in matched decoding time-courses that\n    did not include errors\n  statistics:\n  - about: linear effect of trial, error time courses\n    test: mixed-effects model, Wald chi-square\n    statistic: χ2(1) = 4.7\n    p: 0.03\n  - about: condition by trial interaction\n    test: mixed-effects model, Wald chi-square\n    statistic: χ2(1) = 4.3\n    p: 0.04\n  - about: linear effect of trial, non-error time courses\n    test: mixed-effects model, Wald chi-square\n    p: 0.33\n  depends_on:\n  - fig4b-error-trial-drop\n  criterion: Trial-wise accuracy as in fig4b-error-trial-drop for trials -5 to 0 around each\n    error; a mixed-effects model of classifier accuracy on trial number relative to the\n    error, participants as random effect on intercept and slope, Wald chi-square. Matched\n    courses are seven consecutive trials without errors (Figure 4B legend); how they are\n    chosen is open, with readings (a) every non-overlapping run of seven correct trials, (b)\n    one such run per error from the same run. The interaction is condition by trial in a joint\n    model. Whether accuracy enters as 0 or 1 per trial or as a mean per participant and\n    position is open; both are run. Reproduced when under one reading the error slope is\n    negative with p < 0.05, the interaction has p < 0.05, and the non-error slope has p >\n    0.05.\n- id: fig4b-error-vs-matched\n  statement: Decoding on the error trial is lower than on matched correct trials, and marginally\n    lower on the trial before the error.\n  source: Results, paragraph 13; Figure 4B\n  quote: decoding in the error trial was significantly lower than decoding in the matched correct\n    trials (trial ‘‘0’’ in the figure; t24 = 2.3, p = 0.01) and marginally lower in the trial\n    prior to the error\n  statistics:\n  - about: trial 0\n    test: t-test\n    statistic: t24 = 2.3\n    p: 0.01\n  - about: trial -1\n    test: t-test\n    statistic: t23 = 1.5\n    p: 0.07\n  depends_on:\n  - fig4b-decline-before-errors\n  criterion: Per participant, accuracy at position 0 (and -1) in the error and in the matched\n    non-error courses of fig4b-decline-before-errors; paired t-test. The side is not stated;\n    t24 = 2.3 with p = 0.01 fits a one-sided test, so the reading is one-sided, with two-sided\n    shown. Reproduced when trial 0 is lower at p < 0.05.\n- id: fig5-similarity-predicts-errors\n  statement: Across the eight Exit to Enter transitions, transitions between states whose OFC\n    patterns are more correlated have lower error rates.\n  source: Results, paragraph 14; Figure 5B and 5C\n  quote: Results showed that transitions to ‘‘nearer’’ states (i.e., transitions between pairs of\n    states whose neural representations were more highly correlated) were associated with lower\n    error rates\n  statistics:\n  - about: linear effect of correlation on error rate, eight transition types\n    test: linear regression\n    statistic: t6 = -3.23\n    p: 0.02\n  - about: within-subject mixed-effects analysis\n    test: mixed-effects model, Wald chi-square\n    statistic: χ2(1) = 3.0\n    p: 0.08\n  - about: Figure 5B, group average by ordinal position\n    p: 0.04\n  - about: Figure 5C, within-subject correlations against zero\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - fig2c-enter-cluster\n  criterion: Between-run correlations of OFC beta maps as in fig2c-enter-cluster, negative\n    values NaN. For each of the eight transitions from an Exit state to the following Enter\n    state, the correlation of the two states' patterns and the error rate on the Enter trial\n    (Results, paragraph 14). The regression with t6 is open between (a) the eight transition\n    types, group-mean correlation against group error rate, and (b) the eight ordinal\n    positions of Figure 5B (transitions ranked by correlation within participant, averaged\n    over participants); the paper gives p = 0.02 in the text and p = 0.04 in the Figure 5B\n    legend, which may be these two. The mixed model has error rate on correlation with\n    participants as random effect. Figure 5C is each participant's Pearson correlation of error\n    rate with pattern correlation over the eight transitions, tested against 0 (test not\n    named; reading a one-sample t-test). Reproduced when under one reading the regression is\n    negative with p < 0.05 and the Figure 5C mean is below 0 at p < 0.05; partially reproduced\n    when one of the two holds. The mixed model is reported against p = 0.08.\n- id: figs5-euclidean-distance\n  statement: The relation between pattern similarity and error rate holds with between-run\n    Euclidean distances in place of correlations.\n  source: Results, paragraph 14; Supplemental Results 1.5; Figure S5\n  quote: we repeated this same analysis using Euclidean distances instead of correlations and\n    obtained the same results (see Figure S5)\n  statistics:\n  - about: Figure S5B, group average by ordinal position\n    p: 0.03\n  - about: Figure S5C, within-subject correlations against zero\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - fig5-similarity-predicts-errors\n  criterion: The analysis of fig5-similarity-predicts-errors with Euclidean distance between\n    beta maps of different runs in place of correlation (Methods, State Space Similarities),\n    under the same readings. Reproduced when under one reading the regression of error rate\n    on distance is positive with p < 0.05 and the Figure S5C mean is above 0 at p < 0.05.\n- id: fig5-synthetic-control\n  statement: The similarity and error-rate analysis on synthetic data with univariate\n    stimulus-driven OFC activation finds no correlation with performance.\n  source: Results, paragraph 14\n  quote: These control analyses found no significant correlations with performance (p > 0.18 for all)\n  statistics:\n  - p: 0.18\n    p_relation: \">\"\n  depends_on:\n  - synthetic-data-control\n  - fig5-similarity-predicts-errors\n  criterion: A claim of absence. The synthetic data of synthetic-data-control, analysed as in\n    fig5-similarity-predicts-errors with the real error rates. Reproduced when none of its\n    tests reaches p < 0.05, over the seeds run.\n- id: supp-motor-action-not-in-ofc\n  statement: The current motor response, decoded as part of an alternative state space, is\n    found in left motor and visual cortex, and not in an ROI analysis of the whole OFC.\n  source: Supplemental Results 1.3, paragraphs 1 and 2; Figure S3A\n  quote: the effect was detected only at a ... lenient threshold and was not confirmed in an ROI analysis of the whole OFC (p = .40)\n  statistics:\n  - about: OFC ROI decoding of states with motor response\n    p: 0.4\n  criterion: A claim of absence for the OFC part. States defined by previous category, previous\n    age, current category and the correct response side, with GLM onsets at the response; the\n    analysis of fig2a-16way-decoding in OFC, t-test against chance at p < 0.05. Needs the\n    response side of each trial; whether the data set has it is the author's to find. The\n    whole-brain part needs data the description does not list.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml paper/10.1016-j.neuron.2016.08.019.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Two quotes cross the supplement's line numbers or drop a colon; fixing them. The two CI bounds are printed with a garbled minus sign (line 340, `[�0.8432, �0.0169]`), confirmed by reading.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "  quote: but were affected by the class ... of the trial (Enter 3.4%, Exit 2.3%, Internal 1.4%",
 "new_string": "  quote: \"but were affected by the class ... of the trial (Enter: 3.4%, Exit: 2.3%, Internal: 1.4%\""
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "  quote: Error rates were not affected by factors Age, Category or their interaction (all p’s > .13)",
 "new_string": "  quote: Error rates were not affected ... by factors Age, Category or their interaction (all p’s > .13)"
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml paper/10.1016-j.neuron.2016.08.019.txt; python - <<'EOF'
import yaml,re
p='claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml'
t=open(p).read()
print('emdash', '—' in t.replace('classification—the','').replace('category—all','').replace('components—were',''), 'rather' in t.lower())
d=yaml.safe_load(t)
print(sum('criterion' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('expected' in c for c in d['claims']))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml`: 29 claims, every one with a quote, 22 with statistics (47 statistical values in all) and 28 with criteria. The quote checker passes except on two values. The confidence-interval bounds −0.8432 and −0.0169 are printed in the text with a garbled minus sign (line 340), and I confirmed them by reading.

**Text read:** the version of record with its full Supplemental Information (Figures S1 to S5, Table S1, Supplemental Results 1.1 to 1.5), from the PyMuPDF text. Nothing the claims need is missing. The paper links no analysis code (it names only SPM8, PhysIO, LIBSVM, the Princeton MVPA toolbox, R, neuRosim and AFNI), so I read none.

**The dataset, from its description:** 24 of the paper's 27 participants, the subset used in the trial-wise analysis. It holds OFC time series in native space, design matrices built with AFNI, drift and motion nuisance terms, and per-state event files. It has no whole-brain data, no other brain regions, no cardiac regressors and no training sessions. Claims that need those are kept, and their criteria say so: the whole-brain conjunction map, the other regions, and training against scanner performance.

**Details the paper leaves open, with the readings named:**
- **Beta-map smoothing kernel:** 3 mm FWHM (the kernel given for the trial-wise test data) or no smoothing. Smoothing needs voxel positions.
- **Z-scoring:** each voxel across the state maps of a run, or each map across voxels.
- **Trials after errors:** left out of the GLM as their own nuisance regressor, or merged with the error regressor.
- **Side of t-tests not stated:** one-sided or two-sided. For t24 = 2.3 with p = 0.01, I read it as one-sided.
- **Behavioral mixed models:** linear on per-participant cell rates, or logistic on single trials.
- **Error-rate denominator.**
- **Permutation test:** which distribution gives the 95th percentile, and which test gives p < 0.025.
- **Searchlight radius:** not given anywhere. I named 2 and 3 voxels as standard choices, not the paper's.
- **"2 TRs after onset":** the first volume at or after onset plus 4.8 s, or the volume nearest that time.
- **How the matched non-error time courses are chosen.**
- **Whether the diagonal is in the within-class similarity mean.**
- **Figure 5:** the eight transition types, or Figure 5B's ordinal positions. The text gives p = 0.02 and the legend p = 0.04, which may be these two readings.
- **Number of bootstrap iterations:** 10,000 in the Methods, 1,000 in the supplement.
- **How the true state of an error trial is reconstructed.**

**Inconsistencies in the paper, recorded in the claims:**
- The 8-way decoding is reported as 4.2% above chance with t26 = 3.3 in the main text, and as 8.5% above chance with t26 = 6.6 in the supplement. The arithmetic supports 4.2.
- Previous age in the 8-way analysis is "above baseline" in the main text but only marginal (p = .09) in the supplement.

**Missing details a claim needed:**
- The synthetic-data controls need each participant's decoding peak and the searchlight radius; the paper gives no radius.
- The motor-action claim needs the response side of each trial; whether the dataset has it is left to the author.

## End of run

16 turns, 5 minutes, $1.55 at API prices, result: success.
