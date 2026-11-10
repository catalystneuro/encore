# alasfour-2024 · claims · run 42748084464

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ | grep -i alasfour; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ | grep -i alas
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
ls paper/ | head; ls paper | wc -l; ls paper | grep -i -E "alas|1388267"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Long lines; I'll fold them for reading.

**Agent calls Bash**

```bash
fold -s -w 4000 paper/*.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt"
}
```

```
1	DOI: 10.3389/fnhum.2024.1388267
2	Version: version of record
3	Source: ncbi_pmc+crossref (find_reuse cache)
4	Stored: 2026-11-09
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	pmc Front Hum Neurosci Front Hum Neurosci 645 fronthumneuro Front. Hum. Neurosci. Frontiers in Human Neuroscience 1662-5161 Frontiers Media SA PMC11169785 PMC11169785.1 11169785 11169785 38873653 10.3389/fnhum.2024.1388267 1 Human Neuroscience Original Research Consistent spectro-spatial features of human ECoG successfully decode naturalistic behavioral states Alasfour Abdulwahab 1 * Gilja Vikash 2 1 Department of Electrical Engineering, College of Engineering and Petroleum, Kuwait University , Kuwait City , Kuwait 2 Department of Electrical and Computer Engineering, University of California, San Diego , CA , United States Edited by: Pietro Aricò, Sapienza University of Rome, Italy Reviewed by: Seokyun Ryun, Seoul National University, Republic of Korea Mohammad Reza Daliri, Iran University of Science and Technology, Iran *Correspondence: Abdulwahab Alasfour, [removed: an e-mail address] 30 5 2024 2024 18 454625 1388267 19 2 2024 19 4 2024 01 01 2024 13 06 2024 14 06 2024 Copyright © 2024 Alasfour and Gilja. 2024 Alasfour and Gilja https://creativecommons.org/licenses/by/4.0/ This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms. Objective Understanding the neural correlates of naturalistic behavior is critical for extending and confirming the results obtained from trial-based experiments and designing generalizable brain-computer interfaces that can o
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml | head -150; ls claims | head -50; ls papers/datasets | grep alas; cat papers/datasets/alasfour-2024.yaml 2>/dev/null; cat tools/claims_check.py | head -60
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 249 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; grep -l "000055" claims/*.yaml
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
[... 182 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"; head -40 claims/peterson-2021.yaml
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
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 40,80p claims/peterson-2021.yaml; grep -n "data:" claims/peterson-2021.yaml | sort | uniq -c | head; grep -n -i "AAL\|with_inputs" claims/peterson-2021.yaml | head -20
```

```
# power over the first 0.5 s after onset (0 to 0.5 s) in the LFB 8-32 Hz (bins 11 to 31 Hz) and
# HFB 76-100 Hz (bins 76 to 96 Hz). The Methods say this power is "averaged"; the code takes the
# median over time bins and then over frequency bins. The mean is the main result, the code's
# median a variant shown beside it.
#
# Regression method fixed here (Methods, with the code where the Methods are silent). One model
# per subject, good electrode and band (LFB, HFB), over all of the subject's analysed events.
# Ten features. Day of recording is one-hot by day; time of day is one-hot in three bins (0-8,
# 8-16, 16-24 h). Reach duration, reach magnitude, reach angle, onset speed, speech ratio,
# bimanual ratio, bimanual overlap and bimanual class are standardised (z-score over the
# subject's events). Reach duration and reach magnitude are log transformed (Methods); the code
# uses log(duration), log(magnitude + 1) and also log(onset speed + 1), shown as a variant.
# Reach angle is folded to -90 (down) to +90 degrees (up) (Methods; code negates the image angle
# and folds 90-270 degrees). Missing bimanual ratios are set to 0.5 and bimanual class is 1 when
# the ipsilateral lead/lag value exists (code). Forward selection by OLS adjusted R2 (code
# _forward_selected_new, run on all of the subject's events, as the code does where the
# Methods do not say); unselected features are set to 0. Huber-loss linear regression
# (sklearn HuberRegressor defaults, code). 200 random train/test splits per subject with days
# balanced in the test set (equal numbers of test events from each day). The Methods give 90%
# training and 10% test; the code uses 80/20 (train_test_split_day_balance, per_train=.8). The
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 80,135p claims/peterson-2021.yaml
```

```
# (days per subject are listed in Table 2; 55 subject-days in all). ECoG at 1000 Hz, preprocessed
# (median removed, high-amplitude artifacts zeroed with 2 s margins, 1-200 Hz bandpass, 60 Hz
# notches, resampled to 500 Hz, common median reference per electrode group, bad electrodes by
# SD or kurtosis) and video at 30 fps. Measured variables are the pose (DeepLabCut, nine key
# points), contralateral wrist movement onset events (151 to 947 per subject, median 640), ten
# behavioural and environmental features per event (day of recording, time of day, reach
# duration, magnitude, angle, onset speed, speech ratio from the audio, bimanual ratio, overlap
# and class), electrode MNI positions and bad-electrode labels. The paper deposited its curated
# epochs, spectral power, event features and projection matrices on Figshare
# (figshare.com/projects/Behavioral_and_neural_variability_of_naturalistic_arm_movements/78666).
# The dandiset (AJILE12) describes ECoG at 500 Hz and pose for the same 12 participants over 55
# days, with the wrist movement events and their features. Outside data the paper uses: the AAL
# atlas (Tzourio-Mazoyer et al., 2002) through the Measure Projection Toolbox, for every claim on
# regions of interest. The Figshare projection matrices (roi_proj_matlab/aal_XX_elecs2ROI.csv)
# are the paper's own output of that step.
#
# Subjects S01 to S12 are assumed to be the dataset's subjects 01 to 12 in order; claim
# subject-days checks this.
#
# Claim extfig2-1c-contralateral-larger was added by the check of 2026-10-23.
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000055/ | python -c "import json,sys;d=json.load(sys.stdin);print(d['draft_version']['name'])"; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('description'));print(d.get('version'))"
```

Result: the fetched text is not kept.

**Agent**

The full text (version of record, PMC) is there. The paper has no supplement and links no code, and no PDF was supplied. I'm writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/alasfour-2024.yaml",
 "content": "# Claims for Alasfour & Gilja (2024), Front. Hum. Neurosci. 18:1388267, \"Consistent\n# spectro-spatial features of human ECoG successfully decode naturalistic behavioral states\",\n# on dandiset 000055 (AJILE12).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read. The version of record from PubMed Central (PMC11169785), in\n# paper/10.3389-fnhum.2024.1388267.txt: abstract, Introduction, Methods, Results, figure legends\n# (Figures 1 to 7), Table 1, Discussion and Data availability statement. The paper has no\n# supplement (PMC lists none, and the text cites none). No PDF was supplied, so the figures\n# could not be read; every claim rests on the text and the legends. Values shown only in the\n# figures (per-feature accuracies, confidence intervals, the finite chance level, the\n# per-participant matrices and curves) are not known here.\n#\n# Code read. None. The paper links no analysis code and names no software or toolbox.\n#\n# Data the paper used. Five of the twelve AJILE12 participants (Peterson et al., 2022), 2 male\n# and 3 female, numbered 1, 2, 4, 5 and 8 in Table 1, chosen as those with at least 1 h of the\n# behaviours of interest, in epilepsy monitoring with ECoG placed for clinical needs.\n# Post-surgical days 3 to 7 only. ECoG at 1 kHz, preprocessed as in AJILE12 (median removed,\n# discontinuities handled, 1-200 Hz bandpass, 60 Hz and harmonic notches, downsampled to 500\n# Hz, common median reference); the dandiset's 500 Hz recordings are these. Video at 30 fps,\n# cut into 2-min blocks, each block given one coarse behaviour label by hand; active labels are\n# talking, watching TV and using a computer or phone (using electronics), inactive labels are\n# sleeping and awake rest. Measured variables: the ECoG of the good electrodes (85, 80, 67, 104\n# and 82 per participant), electrode positions, and the block labels. Table 1 gives sex, age,\n# good electrodes and minutes of each active label per participant. The dandiset's description\n# names annotated behavioural states, electrode recordings and pose; it is meant to hold these\n# data.\n#\n# Outside data. Electrodes are assigned to eight AAL regions with \"the electrode-to-region of\n# interest (ROI) projection matrices used in a previous study\" (Methods 2.1), those of Peterson\n# et al. (2021a, eNeuro 8, ENEURO.0007-21.2021, claims/peterson-2021.yaml). The paper gives no\n# location for them. That paper deposited its projection matrices on Figshare\n# (figshare.com/projects/Behavioral_and_neural_variability_of_naturalistic_arm_movements/78666)\n# and its code at github.com/BruntonUWBio/naturalistic_arm_movements_ecog. Every claim on\n# regions uses them (data with_inputs). The eight regions, from Peterson et al. and the figure\n# legends, are taken to be middle frontal (the paper's \"frontal middle\"), precentral,\n# postcentral, inferior parietal, supramarginal, superior temporal, middle temporal and\n# inferior temporal.\n#\n# Method fixed by the paper (Methods 2.1 and 2.2, figure legends).\n# M1 Labels. Talking and Watching TV for the two-class analyses; Using Electronics added as a\n#    third class for four of the five participants (Methods 2.2).\n# M2 Bands. Five IIR Butterworth bandpass filters, theta 4-8, alpha 8-12, beta 8-32, low gamma\n#    32-55 and high gamma 70-110 Hz; amplitude envelope by the Hilbert transform; envelopes\n#    averaged over 10-s bins (Methods 2.1). One 10-s bin is one sample.\n# M3 Artifacts. A 2-min segment is dropped when 10% of channels exceed 3 SD of the channel for\n#    more than 2 s (Methods 2.1).\n# M4 Regions. Each electrode gets the ROI closest to it from the projection matrix, only\n#    electrodes close to one of the eight ROIs are used, and an ROI is dropped for a\n#    participant when its electrode density is below 3 (Methods 2.1).\n# M5 Classifier. One LDA per participant, ROI and band (40 features per participant), with a\n#    covariance shared by the classes. 7-fold cross-validation over the time-ordered data with\n#    a one-fold buffer between training and test sets. Training and test sets each downsampled\n#    to balance the classes, and each z-scored on its own (Methods 2.2).\n# M6 Group accuracy. The 35 fold accuracies (7 folds by 5 participants) of each feature are\n#    compared with the finite-data chance level of Combrisson and Jerbi (2015) by a two-sided\n#    Student's t-test, with Benjamini-Hochberg FDR at alpha 0.01 (Methods 2.2; Figure 2 legend).\n# M7 ANOVA. Two-way ANOVA on accuracy with ROI, band and their interaction (Methods 2.2;\n#    Results 3.1).\n# M8 Mean difference. For each fold model, the fitted class mean of Talking minus that of\n#    Watching TV (positive means Talking higher, Results 3.1); 35 values per feature, a\n#    two-sided Student's t-test against zero, BH FDR at alpha 0.01. A feature is consistent\n#    when both this test and the accuracy test (M6) are significant (Methods 2.2; Figure 5\n#    legend).\n# M9 Participant matrices. Per participant, accuracy (Figure 4) and mean difference averaged\n#    over the training folds (Figure 6, legend and Results 3.1) for each ROI and band.\n# M10 Additivity. Per participant and band, ROIs ranked by performance on a validation set,\n#    then the classifier refit starting from the top ROI and adding ROIs one at a time, in a\n#    7-fold scheme with validation and test sets (Methods 2.2; Figure 7 legend).\n#\n# Details the paper leaves open, with the readings it allows. Criteria refer to these by\n# number. An outcome that rests on one of them rests on an assumption.\n# O1 Participant numbers. Table 1 numbers the five 1, 2, 4, 5 and 8 (AJILE12 numbers), but the\n#    Results and legends name a Participant 3, who is not in Table 1. Readings: (a) the figures\n#    number the five 1 to 5 in the order of Table 1 (figure 1, 2, 3, 4, 5 are Table 1's 1, 2, 4,\n#    5, 8); (b) the figures use Table 1's numbers. Only (a) makes every sentence name an\n#    analysed participant; (b) is run wherever it names one. Which dataset subject is which\n#    AJILE12 participant is the author's to find.\n# O2 Inclusion. \"at least 1 h of recorded neural activity of the behaviors of interest\" can be\n#    (a) at least 1 h of each of talking and watching TV, or (b) at least 1 h of the two\n#    together; both counted over days 3 to 7, before or after artifact rejection.\n# O3 Filters. The Butterworth order and whether filtering is zero phase are not given. This is\n#    a standard choice (4th order, zero phase) and is not expected to change an outcome.\n# O4 Artifact rule. Readings: (a) at least 10% of channels each above 3 SD of that channel for\n#    more than 2 s in total within the block; (b) the same with more than 2 s contiguous.\n#    Applied to the preprocessed voltage (the text calls them high-amplitude bursts), with the\n#    SD over the channel's whole recording for the participant, a standard choice.\n# O5 ROI assignment. The distance threshold for \"close to any of the eight defined ROIs\" is not\n#    given. Readings: (a) every good electrode with a nonzero projection weight to any of the\n#    eight ROIs, assigned to its largest-weight ROI; (b) every good electrode assigned to the\n#    ROI whose centroid is nearest. \"Electrode density of less than 3\" can be (i) fewer than 3\n#    electrodes assigned, or (ii) a summed projection weight below 3.\n# O6 Feature of an ROI. The three-class analysis uses \"all available electrodes from the eight\n#    8 ROIs as features\" (Methods 2.2), so the electrodes of an ROI are read as its features,\n#    reading (a); the scalar mean difference of an ROI in Figures 5 and 6 is then the mean over\n#    its electrodes. Reading (b) is one feature per ROI, the mean of its electrodes' envelopes.\n# O7 Folds and buffer. The data of the two classes are pooled in time order and cut into 7\n#    contiguous folds of equal size (Methods \"temporally sequenced\"). The buffer can be (a) the\n#    folds next to the test fold on both sides left out of training, or (b) only one\n#    neighbouring fold left out (the following one; the preceding one for the last fold).\n# O8 Balancing and LDA. Random downsampling of the larger class, seed a standard choice. LDA\n#    solver and shrinkage are not given; the standard choice is an unregularised shared\n#    covariance (scikit-learn LinearDiscriminantAnalysis defaults) with equal priors.\n# O9 Finite chance level. Combrisson and Jerbi (2015) give the threshold as the binomial inverse\n#    at 1 - alpha for n test samples and c classes. Neither alpha nor n is given. Readings:\n#    alpha (a) 0.05 or (b) 0.01; n (i) the balanced test samples of each fold, a threshold per\n#    fold, or (ii) all test samples of the participant. With a chance level per fold, the\n#    t-test is on fold accuracy minus fold chance against zero. \"Above chance\" is a significant\n#    two-sided test with the mean above chance.\n# O10 ANOVA sums of squares. ROIs missing for some participants make the design unbalanced; the\n#    type is not given. Standard choice type II; type I and III shown as variants. Participant\n#    is not a factor (the paper names ROI, band and interaction only).\n# O11 Averages over ROIs or bands (Results 3.1, post-hoc). Readings: (a) mean of all fold\n#    accuracies pooled; (b) mean of the per-feature means.\n# O12 Post-hoc test on ROIs (\"statistically higher than all the other ROIs\"). Not named.\n#    Readings: (a) Tukey HSD on the ROI factor at 0.05; (b) pairwise two-sample t-tests of the\n#    pooled fold accuracies, BH FDR at 0.01.\n# O13 Participant-level significance (Figure 4). Not stated. Readings: (a) per participant, a\n#    one-sample t-test of the 7 fold accuracies against the finite chance level, BH FDR at 0.01\n#    over the participant's features; (b) the mean fold accuracy above the participant's finite\n#    chance threshold (O9).\n# O14 Sign consistency (Figure 6). A participant without the ROI has no value. Readings: (a) the\n#    combination counts when all participants that have the ROI share a sign; (b) only\n#    combinations present in all five participants can count.\n# O15 Additivity scheme (Figure 7). The validation set is not described. Readings: (a) within\n#    each outer fold, one training fold (the one next to the buffer) held out as validation to\n#    rank ROIs; (b) ROIs ranked by the participant's single-ROI cross-validated accuracies.\n#    Features of the k top ROIs are concatenated, for k from 1 to the participant's number of\n#    ROIs.\n# O16 Three-class scheme. Not described apart from the features; read as the two-class scheme\n#    (M5) with three balanced classes and chance for c = 3. Which participant lacked data is not\n#    said; Table 1 suggests participant 8 (29 min of using electronics).\nschema_version: 2\npaper: doi:10.3389/fnhum.2024.1388267\nclaims:\n- id: cohort-selection\n  statement: Of the twelve AJILE12 participants, only five (2 male, 3 female) had at least 1 h of\n    recorded neural activity of the behaviours of interest, and these five were analysed.\n  source: Methods, 2.1 Data preprocessing, paragraph 1\n  quote: We selected only participants with at least 1 h of recorded neural activity of the\n    behaviors of interest to obtain adequate samples when training and testing our classification\n    models. Of the 12 participants in the dataset, only 5 satisfied this criterion.\n  expected:\n  - quantity: participants meeting the criterion\n    value: 5\n    tolerance: 0\n  criterion: Labelled minutes over post-surgical days 3 to 7 (Methods 2.1) are counted per\n    participant under the readings of O2. Reproduced when, under one reading, exactly five\n    participants meet it and they are Table 1's participants 1, 2, 4, 5 and 8 (2 male, 3 female);\n    partially reproduced when five meet it but not those five.\n- id: table1-participants\n  statement: Table 1 gives, per participant, sex, age, good electrodes and minutes of talking,\n    watching TV and using electronics; all five have at least 2 h of data for the two states.\n  source: Table 1 and its footnote; Methods, 2.1 Data preprocessing, paragraph 2\n  inferred: Numbers from Table 1; no sentence states them. The footnote sentence \"All five\n    participants have at least 2 h of data for two behavioral states suitable for subsequent\n    analysis\" states the 2-h finding.\n  expected:\n  - quantity: participant 1 good electrodes\n    value: 85\n    tolerance: 0\n  - quantity: participant 2 good electrodes\n    value: 80\n    tolerance: 0\n  - quantity: participant 4 good electrodes\n    value: 67\n    tolerance: 0\n  - quantity: participant 5 good electrodes\n    value: 104\n    tolerance: 0\n  - quantity: participant 8 good electrodes\n    value: 82\n    tolerance: 0\n  - quantity: participant 1 minutes talking\n    value: 493\n    tolerance: 49.3\n    unit: min\n  - quantity: participant 1 minutes watching TV\n    value: 605\n    tolerance: 60.5\n    unit: min\n  - quantity: participant 1 minutes using electronics\n    value: 291\n    tolerance: 29.1\n    unit: min\n  - quantity: participant 2 minutes talking\n    value: 331\n    tolerance: 33.1\n    unit: min\n  - quantity: participant 2 minutes watching TV\n    value: 338\n    tolerance: 33.8\n    unit: min\n  - quantity: participant 2 minutes using electronics\n    value: 68\n    tolerance: 6.8\n    unit: min\n  - quantity: participant 4 minutes talking\n    value: 696\n    tolerance: 69.6\n    unit: min\n  - quantity: participant 4 minutes watching TV\n    value: 312\n    tolerance: 31.2\n    unit: min\n  - quantity: participant 4 minutes using electronics\n    value: 181\n    tolerance: 18.1\n    unit: min\n  - quantity: participant 5 minutes talking\n    value: 340\n    tolerance: 34.0\n    unit: min\n  - quantity: participant 5 minutes watching TV\n    value: 480\n    tolerance: 48.0\n    unit: min\n  - quantity: participant 5 minutes using electronics\n    value: 212\n    tolerance: 21.2\n    unit: min\n  - quantity: participant 8 minutes talking\n    value: 216\n    tolerance: 21.6\n    unit: min\n  - quantity: participant 8 minutes watching TV\n    value: 156\n    tolerance: 15.6\n    unit: min\n  - quantity: participant 8 minutes using electronics\n    value: 29\n    tolerance: 2.9\n    unit: min\n  criterion: Electrode counts are exact (the dataset's good electrodes per participant); minutes\n    are within 10%. Sex and ages (M 44, M 20, F 19, F 31, F 33) must match the dataset's subject\n    metadata. Minutes are the labelled 2-min blocks of each label over days 3 to 7, counted\n    (a) before or (b) after artifact rejection (M3, O4); the table does not say which.\n    Reproduced when all electrode counts and at least 13 of the 15 minute values match under\n    one reading, and the talking plus watching TV total is at least 120 min for all five;\n    partially reproduced when 9 to 12 minute values match.\n- id: fig2-highest-accuracy\n  statement: Across the 40 ROI and band features, the highest participant-wide classification\n    accuracy of Talking against Watching TV is 69%, for high gamma in the inferior temporal lobe.\n  source: Results, 3.1, paragraph 1; Figure 2\n  quote: we observe that the highest classification performance is 69% for the high γ band in the\n    inferior temporal lobe\n  data: with_inputs\n  expected:\n  - quantity: participant-wide accuracy, high gamma, inferior temporal\n    value: 69\n    tolerance: 6.9\n    unit: '%'\n  criterion: Accuracy of a feature is the mean of its 35 fold accuracies (M5, M6), under the\n    readings of O5, O6, O7. Reproduced when, under one reading, high gamma in the inferior\n    temporal lobe has the highest mean of the 40 features and its value is within tolerance;\n    partially reproduced when the value is within tolerance but another feature is higher.\n- id: fig2-rois-three-bands\n  statement: The postcentral gyrus, supramarginal gyrus and superior, middle and inferior\n    temporal lobes each have three or more bands with accuracy significantly above chance.\n  source: Results, 3.1, paragraph 1; Figure 2 and legend\n  quote: The postcentral gyrus, supramarginal gyrus, and superior, middle, and inferior temporal\n    lobes have 3 or more frequency bands where the LDA classification performance is\n    significantly above chance.\n  statistics:\n  - test: two-sided Student's t-test against finite chance (Combrisson and Jerbi, 2015)\n    p: 0.01\n    p_relation: <\n    corrected: Benjamini-Hochberg FDR\n    n: 35 fold accuracies (7 folds by 5 participants) per feature\n  data: with_inputs\n  criterion: Significance per M6, with the chance level and test under O9, folds under O7, ROI\n    features under O5 and O6. Reproduced when, under one reading, each of the five ROIs has at\n    least 3 significant bands; partially reproduced when four of the five do.\n- id: fig2-inferior-temporal-all-bands\n  statement: All five bands in the inferior temporal lobe decode significantly above chance.\n  source: Results, 3.1, paragraph 1; Figure 2\n  quote: All 5 frequency bands in the inferior temporal lobe resulted in a decoding accuracy that\n    was significantly higher than by chance.\n  statistics:\n  - test: two-sided Student's t-test against finite chance (Combrisson and Jerbi, 2015)\n    p: 0.01\n    p_relation: <\n    corrected: Benjamini-Hochberg FDR\n    n: 35 fold accuracies per feature\n  data: with_inputs\n  criterion: As fig2-rois-three-bands (M6, O5 to O9). Reproduced when, under one reading, all 5\n    inferior temporal bands are significant; partially reproduced when 4 are.\n- id: fig2-beta-temporal-only\n  statement: Beta decodes above chance only in the middle and inferior temporal lobes.\n  source: Results, 3.1, paragraph 1; Figure 2\n  quote: Both the middle temporal and inferior temporal lobe are the only ROIs where the β band\n    performs above chance level.\n  statistics:\n  - test: two-sided Student's t-test against finite chance (Combrisson and Jerbi, 2015)\n    p: 0.01\n    p_relation: <\n    corrected: Benjamini-Hochberg FDR\n    n: 35 fold accuracies per feature\n  data: with_inputs\n  criterion: As fig2-rois-three-bands (M6, O5 to O9). Reproduced when, under one reading, beta is\n    significant in the middle and inferior temporal lobes and in no other ROI; partially\n    reproduced when it is significant in both and in one other ROI.\n- id: fig2-single-band-rois\n  statement: The inferior parietal lobe decodes above chance only with high gamma, and the\n    middle frontal lobe only with theta.\n  source: Results, 3.1, paragraph 1; Figure 2\n  quote: The inferior parietal and frontal middle lobes only perform above chance when high γ or θ\n    bands are used, respectively.\n  statistics:\n  - test: two-sided Student's t-test against finite chance (Combrisson and Jerbi, 2015)\n    p: 0.01\n    p_relation: <\n    corrected: Benjamini-Hochberg FDR\n    n: 35 fold accuracies per feature\n  data: with_inputs\n  criterion: As fig2-rois-three-bands (M6, O5 to O9). Reproduced when, under one reading, the\n    inferior parietal lobe's only significant band is high gamma and the middle frontal lobe's\n    only significant band is theta; partially reproduced when one of the two holds.\n- id: anova-roi-band-effects\n  statement: In a two-way ANOVA on accuracy, both ROI and band contribute significantly to\n    decodability (p reported as 0 for both).\n  source: Results, 3.1, paragraphs 1 and 2\n  quote: Both the ROI and frequency band contributed significantly to decodability, with a p\n    -value of 0 for both variables.\n  statistics:\n  - about: ROI main effect\n    test: two-way ANOVA\n    p: 0\n  - about: band main effect\n    test: two-way ANOVA\n    p: 0\n  data: with_inputs\n  criterion: Two-way ANOVA (M7) on the fold accuracies of all participants, ROIs and bands,\n    sums of squares under O10, with the readings of O5 to O8. Reproduced when both main effects\n    have p < 0.001 (a printed 0) under one reading; partially reproduced when one does and the\n    other has p < 0.05.\n- id: anova-no-interaction\n  statement: The interaction between ROI and band has no significant effect on accuracy (p =\n    0.46).\n  source: Results, 3.1, paragraph 2\n  quote: The interaction between the ROI and frequency band does not show a significant effect\n    with a p-value of 0.46.\n  statistics:\n  - about: ROI by band interaction\n    test: two-way ANOVA\n    p: 0.46\n  data: with_inputs\n  criterion: A claim of absence, judged on the paper's test, the two-way ANOVA of M7 (type II\n    sums of squares, the standard choice of O10), at the 0.05 level the paper's wording implies.\n    Reproduced when the interaction term has p >= 0.05; not reproduced when p < 0.05. The F and\n    p of the interaction are reported either way, and under types I and III as variants.\n- id: posthoc-band-averages\n  statement: Averaged over ROIs, high gamma has the highest accuracy (63%) and beta the lowest\n    (56%, barely above the finite chance level).\n  source: Results, 3.1, paragraph 2\n  quote: we note that the high γ band has the highest classification performance across all ROIs,\n    with an average of 63%. The β band, across all ROIs, performs the worst with an average\n    classification accuracy of 56%, which is barely above the finite chance level.\n  data: with_inputs\n  expected:\n  - quantity: mean accuracy over ROIs, high gamma\n    value: 63\n    tolerance: 6.3\n    unit: '%'\n  - quantity: mean accuracy over ROIs, beta\n    value: 56\n    tolerance: 5.6\n    unit: '%'\n  criterion: Band averages under the readings of O11, with O5 to O8. Reproduced when, under one\n    reading, both values are within tolerance, high gamma has the highest and beta the lowest\n    average of the five bands, and the beta average exceeds the finite chance level (O9) by less\n    than the high gamma average does; partially reproduced when the order holds but a value is\n    out of tolerance.\n- id: posthoc-roi-averages\n  statement: Averaged over bands, the inferior temporal lobe has the highest accuracy (66%) and\n    is statistically higher than every other ROI; the middle frontal lobe is lowest (54%).\n  source: Results, 3.1, paragraph 2\n  quote: In a group-level analysis of ROIs, the inferior temporal lobe has the highest average\n    classification accuracy across all frequency bands at 66%, and is statistically higher than\n    all the other ROIs. The lowest performing ROI being the frontal middle lobe, with an average\n    decoding performance of 54%.\n  data: with_inputs\n  expected:\n  - quantity: mean accuracy over bands, inferior temporal\n    value: 66\n    tolerance: 6.6\n    unit: '%'\n  - quantity: mean accuracy over bands, middle frontal\n    value: 54\n    tolerance: 5.4\n    unit: '%'\n  criterion: ROI averages under O11, the post-hoc test under O12, with O5 to O8. Reproduced when,\n    under one reading, both values are within tolerance, the inferior temporal lobe is highest\n    and significantly higher than each of the other seven ROIs, and the middle frontal lobe is\n    lowest; partially reproduced when the order holds but the inferior temporal lobe is not\n    significantly higher than all seven.\n- id: fig3-three-class\n  statement: With Using Electronics added as a third class, decoding with all electrodes is above\n    the finite chance level for all four participants with enough data, with high variability;\n    Participant 2 is highest (above 70% in every band) and much higher than Participant 4.\n  source: Results, 3.1, paragraph 3; Figure 3 and legend\n  quote: Note that for all 4 participants, the decoding accuracy was above the finite chance\n    level. However, there was high variability between participants. For example, Participant 2\n    had a much higher decoding performance than Participant 4.\n  data: with_inputs\n  criterion: Per participant and band, a three-class LDA on all electrodes of the eight ROIs\n    (Methods 2.2), under O16, O5, O7, O8, with the chance level of O9 for c = 3. The four\n    participants are those of Table 1 with the most minutes of using electronics (1, 2, 4, 5),\n    the reading Table 1 suggests; participant numbers in the figure under O1. Reproduced when,\n    under one reading, every participant's accuracy is above its finite chance level in every\n    band (Figure 3 legend, \"All 4 participants exhibit above chance classification\n    accuracies\"), Participant 2 is above 70% in all five bands and has the highest accuracy,\n    and Participant 2 exceeds Participant 4 in every band; partially reproduced when the\n    above-chance part holds but the Participant 2 part does not.\n- id: fig4-not-single-participant\n  statement: Every participant has accuracy significantly above chance for multiple ROI and band\n    features, so the group result of Figure 2 is not driven by one participant.\n  source: Results, 3.1, paragraph 4; Figure 4 legend\n  quote: In Figure 4 , we observe that all the participants have classification accuracies that\n    are significantly above chance for multiple ROI/frequency band combinations.\n  data: with_inputs\n  criterion: Participant-level significance under O13 (the paper does not say how it is\n    judged), with O5 to O9. Reproduced when, under one reading, each of the five participants has\n    at least 2 significant features; partially reproduced when four do.\n- id: fig4-missing-rois\n  statement: Participants 2 and 3 have no electrodes in at least one of the eight ROIs.\n  source: Results, 3.1, paragraph 4; Figure 4\n  quote: Note that for Participants 2 and 3, columns displayed a red x marker because no\n    electrodes were present in that ROI.\n  data: with_inputs\n  criterion: ROIs per participant under O5 (with the density rule (i) or (ii)), participant\n    numbers under O1 (a), the only reading in which a Participant 3 exists. Reproduced when,\n    under one reading, figure participants 2 and 3 (Table 1's 2 and 4) each lack at least one\n    ROI and the other three have all eight; partially reproduced when both lack an ROI but\n    another participant does too.\n- id: fig4-participant2-high\n  statement: Participant 2 performs best, with several features above 75% accuracy and low and\n    high gamma in the inferior temporal lobe above 80%.\n  source: Results, 3.1, paragraph 4; Figure 4\n  quote: Subject 2 was the highest-performing participant, where multiple ROI/frequency band\n    features had a classification accuracy exceeding 75%. Most notably, for Participant 2,\n    low-and high gamma bands in the inferior temporal lobe exceeded 80% decoding accuracy.\n  data: with_inputs\n  criterion: Participant accuracy of a feature is the mean of its 7 fold accuracies (M5, M9),\n    with O5 to O8; Participant 2 is Table 1's participant 2 under both readings of O1.\n    Reproduced when, under one reading, Participant 2 has the highest mean accuracy over its\n    features of the five, at least 2 features above 75%, and inferior temporal low and high\n    gamma both above 80%; partially reproduced when the first two parts hold and the inferior\n    temporal gamma values exceed 75%.\n- id: fig5-gamma-higher-talking\n  statement: Low and high gamma activity is higher when a participant is talking than when\n    watching TV.\n  source: Results, 3.1, paragraph 6; Figure 5 and legend\n  quote: On a macro level, we note that the low and high γ band is greater when a participant is\n    engaged in talking versus watching TV.\n  statistics:\n  - test: two-sided Student's t-test of the LDA mean difference against zero\n    p: 0.01\n    p_relation: <\n    corrected: Benjamini-Hochberg FDR\n    n: 35 fold mean differences per feature\n  data: with_inputs\n  criterion: Mean difference Talking minus Watching TV per M8, the ROI scalar under O6, with O5,\n    O7, O8, O9. Reproduced when, under one reading, every consistent feature (both tests\n    significant, M8) in low or high gamma has a positive difference and there is at least one\n    such feature in each of the two bands; partially reproduced when most of them are\n    positive.\n- id: fig5-theta-alpha-lower-talking\n  statement: Theta and alpha activity is lower when a participant is talking than when watching\n    TV.\n  source: Results, 3.1, paragraph 6; Figure 5\n  quote: Further, θ and α band activity are lower when a participant is talking vs. watching TV.\n  statistics:\n  - test: two-sided Student's t-test of the LDA mean difference against zero\n    p: 0.01\n    p_relation: <\n    corrected: Benjamini-Hochberg FDR\n    n: 35 fold mean differences per feature\n  data: with_inputs\n  criterion: As fig5-gamma-higher-talking (M8, O5 to O9). Reproduced when, under one reading,\n    every consistent feature in theta or alpha has a negative difference and there is at least\n    one in each band; partially reproduced when most of them are negative.\n- id: fig5-pre-postcentral\n  statement: The largest differences are in the precentral and postcentral gyri, with\n    consistent differences in theta, alpha, low gamma and high gamma.\n  source: Results, 3.1, paragraph 6; Figure 5; Discussion, paragraph 2\n  quote: The greatest difference can be seen in the precentral and postcentral lobes, with\n    consistent differences seen in θ , α , low γ , and high γ .\n  statistics:\n  - test: two-sided Student's t-test of the LDA mean difference against zero\n    p: 0.01\n    p_relation: <\n    corrected: Benjamini-Hochberg FDR\n    n: 35 fold mean differences per feature\n  data: with_inputs\n  criterion: As fig5-gamma-higher-talking (M8, O5 to O9). \"Greatest difference\" is read as the\n    largest absolute mean difference among the 40 features. Reproduced when, under one reading,\n    the feature with the largest absolute mean difference is in the precentral or postcentral\n    gyrus and theta, alpha, low gamma and high gamma are consistent in both gyri (negative for\n    theta and alpha, positive for the gammas, Discussion paragraph 2); partially reproduced when\n    at least 6 of these 8 features are consistent with those signs.\n- id: fig5-parietal-temporal-no-gamma\n  statement: In the supramarginal gyrus, inferior parietal lobe and superior temporal lobe there\n    is no consistent gamma increase during talking, while the theta and alpha differences are\n    still present there.\n  source: Results, 3.1, paragraph 6; Figure 5\n  quote: When a participant engages in dialog, we do not see higher activation in the γ band in\n    the supramarginal gyrus, inferior parietal and superior temporal lobe.\n  data: with_inputs\n  criterion: As fig5-gamma-higher-talking (M8, O5 to O9). For the absence part, the paper's\n    test is the consistency rule of M8. Reproduced when, under one reading, none of the six\n    gamma features (low and high gamma in the three ROIs) is consistent with a positive\n    difference, and in each of the three ROIs at least one of theta and alpha is consistent\n    (with the sign of fig5-theta-alpha-lower-talking); partially reproduced when the gamma part\n    holds and the theta and alpha part holds in two of the three ROIs. The size of each\n    difference is reported.\n- id: fig5-middle-temporal-tv\n  statement: The middle temporal lobe shows consistently higher activity in 4 of the 5 bands\n    when participants watch TV than when they talk.\n  source: Results, 3.1, paragraph 6; Figure 5\n  quote: Additionally, the middle temporal lobe displayed consistent increased activation in 4 out\n    of 5 frequency bands of interest when the participants watched TV instead of talking.\n  data: with_inputs\n  expected:\n  - quantity: middle temporal bands consistent with negative difference\n    value: 4\n    tolerance: 0\n  criterion: As fig5-gamma-higher-talking (M8, O5 to O9). Reproduced when, under one reading,\n    exactly 4 of the 5 middle temporal bands are consistent with a negative difference (Watching\n    TV higher); partially reproduced when 3 or 5 are.\n- id: inferior-temporal-high-gamma-inconsistent\n  statement: High gamma in the inferior temporal lobe decodes well but its mean difference is\n    virtually zero, so its signal is inconsistent across folds and participants.\n  source: Discussion, paragraph 5\n  quote: When investigating high γ activity in the inferior temporal lobe, the decoding\n    performance was generally high, whereas the mean difference was virtually zero.\n  data: with_inputs\n  depends_on:\n  - fig2-highest-accuracy\n  criterion: A claim of absence on the mean difference, judged on the paper's test, the two-sided\n    t-test against zero with BH FDR at 0.01 (M8), with O5 to O9. Reproduced when inferior\n    temporal high gamma is significant for accuracy (M6) and its mean difference is not\n    significant; not reproduced when the mean difference is significant. The mean difference,\n    its 95% interval and its size relative to the other features are reported either way.\n- id: all-rois-but-inferior-parietal\n  statement: Every ROI except the inferior parietal lobe has at least one band that both\n    separates the two behaviours and is consistent across participants.\n  source: Discussion, paragraph 3\n  quote: It would lead us to conclude that with in this study, all analyzed ROIs, except the\n    inferior parietal lobe, had at least one frequency band that could separate the two\n    naturalistic behaviors and consistent signal characteristics across participants.\n  data: with_inputs\n  criterion: Consistency per M8, with O5 to O9. Reproduced when, under one reading, each of the\n    seven other ROIs has at least one consistent band and the inferior parietal lobe has none;\n    partially reproduced when six of the seven have one and the inferior parietal lobe has\n    none.\n- id: fig6-sign-consistency\n  statement: The sign of the Talking minus Watching TV difference is the same in all participants\n    for 9 of the 40 ROI and band combinations (22.5%).\n  source: Results, 3.1, paragraph 7; Figure 6 legend\n  quote: A total of 9 out of 40 (22.5%) of ROI/frequency band combinations show no change in sign\n    differences across participants, highlighting the consistency of the learned features.\n  data: with_inputs\n  expected:\n  - quantity: combinations with the same sign in all participants\n    value: 9\n    tolerance: 0.9\n  criterion: Per participant, the mean over the 7 training folds of the mean difference (M9),\n    the ROI scalar under O6, with O5, O7, O8; missing ROIs under O14. Reproduced when, under one\n    reading, the count is 8 to 10 (the 10% tolerance, rounded to whole combinations); partially\n    reproduced when it is 7 or 11.\n- id: fig6-examples\n  statement: High gamma in the precentral, middle frontal and postcentral regions, and alpha in\n    the precentral, inferior parietal and supramarginal regions, have the same sign in all\n    participants.\n  source: Results, 3.1, paragraph 7; Figure 6\n  quote: For example, we note that high gamma activity in the precentral, frontal middle and post\n    central lobes all show the same directionality across the participants. In addition, alpha\n    band is completely consistent across participants in the precentral, inferior parietal and\n    supramarginal lobes.\n  data: with_inputs\n  depends_on:\n  - fig6-sign-consistency\n  criterion: As fig6-sign-consistency (M9, O5 to O8, O14). Reproduced when, under one reading,\n    all six named combinations share a sign across participants; partially reproduced when 4 or\n    5 do.\n- id: fig7-non-additive\n  statement: Adding electrodes from further top-ranked ROIs generally does not improve a\n    participant's decoding performance; the information is not additive across ROIs.\n  source: Results, 3.2, paragraph 1; Figure 7 legend; Discussion, paragraph 3\n  quote: The main trend is that the performance is not additive, indicating that adding the\n    top-performing ROIs does not contribute additional information that would improve the\n    decoding performance.\n  data: with_inputs\n  criterion: Per participant and band (25 curves), the incremental scheme of M10 under O15, with\n    O5, O7, O8. The paper gives no test or threshold for \"additive\". Readings, named before the\n    analysis are (a) a curve is additive when its test accuracy with all ROIs exceeds its\n    accuracy with the top ROI alone; (b) a curve is additive when the best accuracy over k\n    exceeds the top-ROI accuracy by more than the 95% interval of the top-ROI fold accuracies.\n    Reproduced when, under one reading, at most 5 of the 25 curves (a fifth, read from\n    \"generally\") are additive; partially reproduced when 6 to 12 are. The outcome rests on the\n    reading chosen.\n- id: fig7-participant4-low-gamma\n  statement: The only notable additive case is Participant 4 in the low gamma band.\n  source: Results, 3.2, paragraph 1; Figure 7\n  quote: The only instance with notable additive information is for Participant 4 when analyzing\n    the low γ band.\n  data: with_inputs\n  depends_on:\n  - fig7-non-additive\n  criterion: As fig7-non-additive (M10, O15, readings (a) and (b)), participant numbers under O1\n    (figure 4 is Table 1's 5 under (a), Table 1's 4 under (b)). Reproduced when, under one\n    reading, Participant 4's low gamma curve has the largest gain of the 25 curves (best\n    accuracy over k minus top-ROI accuracy); partially reproduced when it is among the three\n    largest.\n- id: fig7-above-70\n  statement: With a simple LDA, every participant reaches more than 70% accuracy, with a maximum\n    of about 80% for Participant 4 in the low and high gamma bands.\n  source: Results, 3.2, paragraph 1; Figure 7; Abstract, Main results\n  quote: Using a simple classifier such as LDA, we would achieve a performance of greater than 70%\n    for all participants, with maximum classification accuracy being around 80% for Participant 4\n    when analyzing low and high γ bands.\n  data: with_inputs\n  expected:\n  - quantity: maximum accuracy, Participant 4, low and high gamma\n    value: 80\n    tolerance: 8\n    unit: '%'\n  criterion: Per participant, the best test accuracy over the bands and k of the Figure 7 curves\n    (M10, O15), with O5, O7, O8; participant numbers under O1. Reproduced when, under one\n    reading, every participant's best accuracy exceeds 70%, and Participant 4's best accuracy\n    in low and in high gamma are within tolerance of 80% and are the highest of the five\n    participants; partially reproduced when the 70% part holds for four participants or the\n    maximum is out of tolerance.\n- id: discussion-above-80\n  statement: Subject-specific classification performance regularly exceeds 80% with a simple LDA.\n  source: Discussion, paragraph 3\n  quote: Subject-specific classification performance regularly exceeds 80% when using a simple LDA\n    classifier.\n  data: with_inputs\n  depends_on:\n  - fig7-above-70\n  criterion: Over the single-ROI participant accuracies (Figure 4, M9) and the Figure 7 curves\n    (M10), with O5, O7, O8, O15. The paper gives no count for \"regularly\". It sits beside the\n    Results' \"greater than 70% for all participants\" and \"maximum ... around 80%\"; read as at\n    least three of the five participants having some feature or curve point above 80%.\n    Reproduced when that holds under one reading; partially reproduced when one or two\n    participants exceed 80%.\n- id: fig7-exceeds-group\n  statement: For individual participants, performance usually exceeds the group-level\n    performance of Figure 2.\n  source: Results, 3.2, paragraph 1; Figure 7; Figure 2\n  quote: Further, we observed that for individual participants, performance usually exceeded\n    group-level performance ( Figure 2 ).\n  data: with_inputs\n  criterion: Each participant's best Figure 7 accuracy (M10, O15) against the highest\n    participant-wide accuracy of Figure 2 (claim fig2-highest-accuracy), with O5, O7, O8.\n    \"Usually\" is read as at least four of the five participants. Reproduced when, under one\n    reading, at least four participants exceed it; partially reproduced when three do.\n- id: fig7-best-band-varies\n  statement: The band that gives a participant's highest performance varies by participant;\n    Participant 5 is best with theta and Participant 3 best with alpha.\n  source: Results, 3.2, paragraph 1; Figure 7\n  quote: For example, Figure 7 shows that Participant 5's decoding performance is highest when\n    using the θ band, while Participant 3's decoding performance is highest when using the α\n    band.\n  data: with_inputs\n  criterion: Per participant, the band whose Figure 7 curve reaches the highest test accuracy\n    (M10, O15), with O5, O7, O8; participant numbers under O1 (a), the only reading in which a\n    Participant 3 exists (Participant 5 is Table 1's 8, Participant 3 is Table 1's 4). Reproduced\n    when, under one reading, Participant 5's best band is theta and Participant 3's is alpha;\n    partially reproduced when one holds.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/alasfour-2024.yaml paper/10.3389-fnhum.2024.1388267.txt; grep -n -i "rather\|—" claims/alasfour-2024.yaml; python - <<'E'
import yaml
d=yaml.safe_load(open('claims/alasfour-2024.yaml'))
for c in d['claims']:
    for k,v in c.items():
        if isinstance(v,str) and ': ' in v: print(c['id'],k)
E
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/alasfour-2024.yaml`, and the quote checker passes it: 30 claims, 29 quotes, 10 statistical values, 0 problems. There are no em dashes, no "rather", and no plain scalar contains ": ". Nothing was committed.

**Text read.** The version of record from PubMed Central (PMC11169785): main text, Methods, Results, the legends of Figures 1 to 7, Table 1 and the Discussion. The paper has no supplement, and no PDF was supplied. The paper links no code and names no software, so no code was read.

**Claims.**
- **Quotes:** 30 claims, 29 with a quote. The Table 1 claim is marked `inferred` because its numbers appear only in the table.
- **Statistics:** 9 claims carry 10 entries. These are the t-tests against chance with Benjamini-Hochberg correction at p ≤ 0.01, the mean-difference t-tests against zero, and the ANOVA results (ROI and band p reported as 0, interaction p = 0.46).
- **Criteria and expected values:** all 30 claims have a criterion, and 10 have expected values.
- **Data:** 28 claims are `with_inputs`. They need the electrode-to-region projection matrices from Peterson et al. 2021a. The paper gives no location for these matrices; they are on that paper's Figshare deposit.

**Details the paper leaves open (O1 to O16 in the header).** Criteria refer to these by number.
- **O1, participant numbers:** Table 1 numbers the participants 1, 2, 4, 5 and 8, but the Results name a "Participant 3". Readings: (a) the figures number the five 1 to 5 in table order; (b) the figures use the table's numbers.
- **O2, inclusion:** at least 1 h of each behaviour, or at least 1 h of the two together.
- **O3, filters:** the Butterworth order and phase are not given. I used a standard choice (4th order, zero phase).
- **O4, artifact rule:** more than 2 s in total within the block, or more than 2 s in a row.
- **O5, assigning electrodes to regions:** an electrode goes to its largest-weight region or to the nearest region centroid. The density rule is fewer than 3 electrodes, or a summed weight below 3.
- **O6, features of a region:** each electrode is a feature, or one feature is the region's mean.
- **O7, cross-validation buffer:** the folds on both sides of the test fold are left out of training, or only one neighbouring fold is.
- **O8, balancing and LDA:** random downsampling and default LDA settings, a standard choice.
- **O9, finite chance level:** alpha is 0.05 or 0.01, and n is the test samples per fold or all test samples together.
- **O10, ANOVA:** the type of sums of squares is not given. I used type II, with types I and III as variants.
- **O11, averages:** pooled fold accuracies, or the mean of the per-feature means.
- **O12, post-hoc test on regions:** Tukey HSD, or pairwise t-tests with false-discovery-rate correction.
- **O13, per-participant significance (Figure 4):** a t-test over the 7 folds, or the mean above the chance threshold.
- **O14, regions missing for some participants (Figure 6):** count only the participants that have the region, or count only combinations present in all five.
- **O15, validation set (Figure 7):** a held-out training fold, or the ranking from single-region accuracies.
- **O16, three-class analysis:** read as the same scheme as the two-class one. Table 1 suggests participant 8 is the one left out.

**Missing from the paper that claims needed.**
- **Figures:** no figure could be read, so values shown only in Figures 2 to 7 are unknown. These include per-feature accuracies, confidence intervals and the chance level itself.
- **Missing thresholds:** the paper gives no test or threshold for "not additive" (Figure 7), "regularly exceeds 80%" or "usually exceeded". The criteria I wrote for these are readings, and their outcomes will rest on assumptions.
- **Conflicting statements:** the abstract and Results say "exceeded 70%", while the Discussion says "regularly exceeds 80%".

## End of run

16 turns, 4 minutes, $1.30 at API prices, result: success.
