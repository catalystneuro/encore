# saez-2018 · claims · run 42933238381

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; ls claims | head; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
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

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2018.07.045.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2018.07.045.txt",
 "offset": 800,
 "limit": 722
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/ofc-3.data-description.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat papers/datasets/saez-2018.yaml 2>/dev/null; ls claims | grep -i saez; ls claims/*.yaml | xargs grep -l "crcns" | head -3; python tools/claims_check.py --help 2>&1 | head -20
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1016/j.cub.2018.07.045
title: Encoding of Multiple Reward-Related Computations in Transient and Sustained High-Frequency Activity
  in Human OFC
datasets:
- archive: crcns
  id: ofc-3
  relation: primary
saez-2016.yaml
claims/asari-2009.yaml
claims/bruno-2017.yaml
claims/deweese-2004.yaml
Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
[... 3 more lines not kept]
```

**Agent**

Full text, STAR Methods and supplement are all present; the paper links no code (custom MATLAB/R scripts, unpublished). Checking a CRCNS-format example before writing.

**Agent calls Bash**

```bash
cd  head -40 claims/asari-2009.yaml; grep -n "data:" claims/*.yaml | awk '{print $NF}' | sort | uniq -c; grep -n '"data"' -A15 schemas/claims.schema.json | head -40
```

```
# Claims for Asari & Zador (2009), J Neurophysiol 102:2638-2656, on CRCNS ac-1.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or
# files; only its description on crcns.org (paper/ac-1.data-description.txt) was read.
#
# Text read: the version of record, as a text extraction of the publisher's PDF (PyMuPDF), with
# the PDF. The extraction garbles some symbols (Greek letters, "<", ">", "~", "=" and "+/-" print
# as a replacement glyph); they were read from context, and quotes are cut around them. The PDF
# pages could not be rendered in this run, so figure axes were not read; every value used here is
# printed in the text or a legend. The online supplement (Supplemental Figures S1 to S10) was not
# supplied and was not read. The main findings rest on the main-text Figures 2 to 9 and their
# legends; the supplement holds example traces (S2 to S10) and the "silence probe" analysis (S1),
# whose one claim (figs1-silence-probe) is quoted from the Methods only.
#
# Code read: none. The paper links no code; it says all analysis was done in MATLAB.
#
# Data the paper used. Long-Evans rats, 20 to 28 days old, anesthetized with ketamine and
# medetomidine; in vivo blind patch recordings sampled at 10 kHz.
# - A1 current clamp (whole cell): 194 cells in 139 animals, of which 123 met the analysis
#   criterion (at least 4 repeats of a probe tested with at least 2 conditioning stimuli). By
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A4 "^schema_version" claims/asari-2009.yaml; grep -n "kind" schemas/claims.schema.json | head
```

```
55:schema_version: 2
56-paper: doi:10.1152/jn.00577.2009
57-claims:
58-- id: methods-recording-counts
59-  statement: Of 194 A1 cells recorded in current clamp, 123 met the analysis criterion (39 tested
86:          "kind": {
173:                "kind": {
178:                "kind"
217:          "kind",
225:          "kind": {
```

**Agent calls Bash**

```bash
python3 -c "
t={'risk':[1,1,25,0,14,0,0,3,4,2],'gamble':[2,1,7,0,14,0,1,4,3,2],'offer':[0,0,6,1,9,0,1,6,7,1],'cv':[0,0,5,2,8,0,3,1,6,1],
'win':[0,1,7,0,16,0,0,5,13,3],'loss':[3,1,2,0,14,0,3,1,8,1],'rpe':[0,1,2,0,10,0,2,1,11,1],'regret':[0,3,4,1,14,0,1,2,6,4],
'prisk':[0,0,4,0,4,0,1,2,6,0],'pgamble':[1,2,9,1,12,0,2,6,4,6],'pwp':[0,2,6,1,18,4,2,5,5,3],'pcv':[0,1,8,1,14,4,2,3,2,0],
'pwin':[0,2,9,1,22,1,1,5,6,2],'ploss':[1,0,1,2,35,1,6,0,7,3],'prpe':[0,1,8,1,21,1,4,1,11,2],'pregret':[3,1,14,3,36,0,2,2,1,2]}
a={'anych':[2,1,30,1,36,4,6,5,8,8],'anyout':[3,3,12,1,29,0,4,8,17,5],'anypch':[1,2,19,1,28,6,2,6,15,7],'anypout':[4,3,18,4,44,2,7,5,11,6],'tot':[5,4,44,5,54,7,10,9,17,12],'n':[5,6,52,5,61,7,11,10,19,16]}
import statistics as s
for k,v in {**t,**a}.items(): print(k,sum(v),round(100*sum(v)/192,1),sum(x>0 for x in v))
pres=[sum(v) for k,v in t.items() if not k.startswith('p')]; past=[sum(v) for k,v in t.items() if k.startswith('p')]
print(s.mean(pres+past)/192*100, s.mean(pres)/1.92, s.mean(past)/1.92)
c=[sum(x>0 for x in v) for v in t.values()]; print(s.mean(c), s.stdev(c)/4, s.mean(c[:8]+c[9:]))
"
```

```
risk 50 26.0 7
gamble 34 17.7 8
offer 31 16.1 7
cv 26 13.5 7
win 45 23.4 6
loss 33 17.2 8
rpe 28 14.6 7
regret 35 18.2 8
prisk 17 8.9 5
pgamble 43 22.4 9
pwp 46 24.0 9
pcv 35 18.2 8
pwin 49 25.5 9
ploss 56 29.2 8
prpe 50 26.0 9
pregret 64 33.3 9
anych 101 52.6 10
anyout 82 42.7 9
anypch 87 45.3 10
anypout 104 54.2 10
[... 4 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/saez-2018.yaml",
 "content": "# Claims for Saez, Lin, Stolk, Chang, Parvizi, Schalk, Knight & Hsu (2018), Current Biology\n# 28:2889-2899, on CRCNS ofc-3.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-11,\n# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or\n# files; only its description on crcns.org (paper/ofc-3.data-description.txt) was read, for which\n# experiments it holds.\n#\n# Text read: the version of record, as a text extraction of the publisher's PDF (PyMuPDF), with the\n# PDF: main text, figure legends, STAR Methods (pages e1 to e3) and the Supplemental Information\n# (Figures S1 to S7, Tables S1 and S2). The extraction garbles some symbols (minus signs, \"~\" and\n# the exponents of \"p < 10^-5\" and \"p < 10^-6\" print as a replacement glyph; the formulas of Table\n# S1 are garbled); they were read from context and from the PDF, and quotes are cut around them.\n#\n# Code read: none. The paper links no code; it says analysis was done \"in MATLAB and R using\n# custom scripts\" (STAR Methods, ECoG Recording).\n#\n# Data the paper used. 10 adult patients (4 female) with intractable epilepsy, implanted with\n# subdural grids or strips at UCSF (2), Stanford (2), UC Irvine (5) and Albany (1). 210 OFC\n# electrodes recorded, 192 artifact-free and confirmed in OFC kept (per patient 5, 6, 52, 5, 61,\n# 7, 11, 10, 19 and 16 for s01 to s10, Table S2). One session of 200 rounds per patient (plus\n# practice). Each round: fixation cross (t = 0), game presentation at 750 ms showing a gamble\n# prize ($10 to $30 in $5 steps) and a number 0 to 10; up to 2 s to choose the safe bet ($10) or\n# the gamble (left/right side randomized); outcome reveal 550 ms after the button press, a second\n# number, the gamble winning when it is greater than the first; new round 1 s after reveal.\n# Timeouts (9.98% of trials) excluded. The outcome is revealed whether or not the patient\n# gambled. 10 healthy comparison participants (UC Berkeley undergraduates) played the same task;\n# the paper does not say whether their data were deposited.\n# Signals: ECoG at 1 kHz after downsampling, common average reference, 1 Hz high-pass; HFA is the\n# 70-200 Hz band (two-way zero-phase FIR band-pass) and its analytic amplitude (Hilbert\n# transform); broadband field potential (FP) power is used for comparison. Epochs are locked to\n# game presentation (game epoch) and to the button press or reward (buttonpress epoch; outcome is\n# a fixed 550 ms after the press). The dataset description lists HFA epochs ([-1, 2] s around\n# game presentation and around the button press, raw and window averaged), the behavior files\n# with event times, choices and outcomes, the gamble parameters per trial, and per-subject files\n# of \"the behavioral regressors used for analysis\" (sXX_behav_globals.mat). It lists no broadband\n# signal and no electrode coordinates or Brodmann labels; whether the data hold them is the\n# author's to find.\n#\n# Method details fixed by the paper and used below (STAR Methods, ECoG analysis and behavioral\n# regression, and Behavioral Analysis):\n# - Dependent variable: HFA analytic amplitude, epoched with a 200-ms baseline \"to remove any\n#   pre-stimulus differences in baseline amplitude\", averaged in 200-ms windows stepped by 50 ms.\n# - Per electrode, regressor and window, a separate linear regression of trial HFA on one\n#   regressor; %EV is its R2 (in percent). Game and buttonpress epochs are analysed separately.\n# - Encoding (task-active) electrode for a regressor: p < 0.05 in 5 or more consecutive windows\n#   at any point in the epochs. The Behavioral Analysis section says \"over 5 consecutive\n#   windows\"; the ECoG analysis section and Figure S6 legend say 5 or more, which is used.\n# - Chance: labels shuffled against HFA 1,000 times per regressor and electrode.\n# - Duration of encoding: the longest stretch in which all time points have p < 0.05.\n# - Regressors (Table S1; Results, Economic Choice Behavior, paragraph 3): win probability p, risk\n#   (variance of the gamble), chosen value (p times prize for a gamble, $10 for the safe bet),\n#   gamble (1 gamble, 0 safe bet), win index (1 for gamble wins), loss index (1 for gamble losses),\n#   RPE (reward obtained minus chosen value), regret (reward obtained minus the maximum reward\n#   possible given the outcome, from -20 to 0). Past regressors are the same quantities from 1 to 5\n#   trials back (t-1 to t-5). Defined on all trials except timeouts.\n# - Stepwise regression: per electrode and regressor, sum of F statistics over the longest stretch\n#   of consecutive windows with p < 0.05; 10,000 label shuffles give a permutation p, Bonferroni\n#   corrected over 192 electrodes; surviving regressors enter forward selection by ANOVA at p <\n#   0.05, starting from the one with the highest peak %EV.\n# Details the paper leaves open, used by several claims, with the readings it allows:\n# - Baseline. Which 200 ms (the 200 ms before the locking event, or before game presentation for\n#   both epochs) and how removed (subtracted, or divided). Readings (a) subtract the mean of the\n#   200 ms before each epoch's event; (b) subtract the mean of the 200 ms before game\n#   presentation, for both epochs. Whether the dataset's HFA is already baseline corrected is\n#   the author's to find.\n# - Win probability. Table S1 and the Behavioral Analysis worked example give 0.8 for a shown 2,\n#   so p = (10 - n)/10 for a shown number n; the Behavioral task paragraph says a shown 2 \"had a\n#   win probability of 20%\". The first is used (it agrees with the rule that a greater second\n#   number wins and the example); the second is a variant.\n# - Risk. Table S1 gives E{(V - E(V))^2}, the variance of the gamble. Readings (a) p(1-p)x^2 with\n#   x the prize; (b) p(1-p). Both peak at p = 0.5 as the paper says.\n# - Offer value. The Results say \"offer value (win probability)\" and Figure 3 lists offer value in\n#   place of win probability, so offer value is read as win probability; the gamble's expected\n#   value p times x (Figure S2A) is a variant.\n# - Past regressors across timeouts. Readings (a) the regressor of the round before, with rounds\n#   whose previous round was a timeout (and round 1) dropped; (b) the regressor of the last\n#   non-timeout round.\n# The per-subject regressor files the dataset description lists may settle the regressor\n# readings; where they do, the author follows them and says so.\nschema_version: 2\npaper: doi:10.1016/j.cub.2018.07.045\nclaims:\n- id: methods-electrode-trial-counts\n  statement: Of 210 OFC electrodes recorded in 10 patients, 192 were artifact-free and included;\n    each patient played 200 rounds, and timeouts, 9.98% of all trials, were excluded.\n  source: STAR Methods, ECoG Recording, and Behavioral task; Table S2, last row\n  quote: Out of 210 OFC electrodes, 192 were artifact-free and included in subsequent analyses\n  expected:\n  - quantity: OFC electrodes included\n    value: 192\n    tolerance: 0\n    unit: electrodes\n  - quantity: patients\n    value: 10\n    tolerance: 0\n    unit: patients\n  - quantity: timeout trials, percent of all trials\n    value: 9.98\n    tolerance: 1.0\n    unit: percent\n  criterion: Exact counts for electrodes and patients (the per-patient electrode counts of Table\n    S2 are 5, 6, 52, 5, 61, 7, 11, 10, 19 and 16 for s01 to s10, which the author compares as\n    well). The timeout percentage is the number of Timeout trials over all 2,000 trials.\n- id: behavior-risk-neutral\n  statement: Patients were approximately risk neutral, choosing the gamble on 55.9% (plus or minus\n    8.5%) of trials.\n  source: Results, Economic Choice Behavior in Neurosurgical Patients, paragraph 4\n  quote: we found that subjects were approximately risk neutral, choosing to gamble only slightly\n    more often than a risk neutral baseline model (55.9% ± 8.5% of risky choices)\n  expected:\n  - quantity: percent of non-timeout trials on which the gamble was chosen\n    value: 55.9\n    tolerance: 8.5\n    unit: percent\n  criterion: The tolerance is the stated spread, which the paper does not name (SD or SEM). The\n    paper does not say how the percentage is formed. Readings (a) the mean over the 10 patients\n    of each patient's percentage of gamble choices among non-timeout trials; (b) the pooled\n    percentage over all non-timeout trials. The risk neutral baseline model is not defined; the\n    share of gamble choices a risk-neutral chooser would make (gamble when p times x exceeds $10,\n    ties split) is reported for comparison.\n- id: fig1c-choice-win-probability\n  statement: The proportion of risky choices increased with win probability, well captured by a\n    logit model (p < 0.001, random effects logit analysis).\n  source: Results, Economic Choice Behavior in Neurosurgical Patients, paragraph 4; Figure 1C\n  quote: The proportion of risky choices increased as the offer value (win probability) increased,\n    which was well captured by a logit model of decision under risk (p < 0.001; random effects\n    logit analysis; Figure 1C)\n  statistics:\n  - test: random effects logit analysis\n    p: 0.001\n    p_relation: \"<\"\n    n: 10 patients\n  criterion: A logistic regression of gamble choice (1 gamble, 0 safe bet; timeouts excluded) on\n    win probability with patient as random effect. The random-effects structure is not stated;\n    readings (a) random intercept per patient; (b) random intercept and slope per patient.\n    Reproduced when, under one reading, the slope is positive with p < 0.001.\n- id: figs2a-choice-gamble-ev\n  statement: Patients' choices were sensitive to the expected value of the gamble (prize times win\n    probability), with gamble choices more frequent at higher gamble expected value.\n  source: Figure S2A legend\n  quote: Patients' choices were sensitive to the expected value of the gamble (i.e., the gamble\n    prize times the win probability), with gamble choices more prevalent for higher gamble\n    expected value\n  criterion: The paper shows this in a figure and reports no test. As in fig1c-choice-win-probability,\n    a random-intercept logistic regression of gamble choice on gamble expected value (p times x);\n    reproduced when the slope is positive with p < 0.05. The proportions of gamble choices per\n    expected-value level are reported.\n- id: fig1c-patients-like-controls\n  statement: The patients' choices were comparable to those of 10 healthy comparison participants\n    (all p > 0.2).\n  source: Figure 1C legend; Results, Economic Choice Behavior in Neurosurgical Patients, paragraph 4\n  quote: Subjects' choices were significantly affected by likelihood of winning the gamble ... and\n    were comparable to those of healthy participants (gray line; all p > 0.2)\n  statistics:\n  - test: not named\n    p: 0.2\n    p_relation: \">\"\n    n: 10 patients and 10 healthy participants\n  criterion: A claim of absence. The paper does not name the test behind \"all p > 0.2\"; the plural\n    and Figure 1C suggest one comparison per win-probability level. Reading fixed from the legend\n    (a) per shown number, a two-sample t test of the proportion of gamble choices, patients\n    against controls; a variant (b) compares the slopes of per-subject logit fits (Figure S1B).\n    Reproduced when no comparison has p < 0.05 (the paper's 0.2 is reported against the result);\n    not reproduced when one does. Needs the healthy participants' choices, which the paper does\n    not say were deposited.\n- id: figs2b-rt-conflict\n  statement: Reaction times were longer in high-conflict trials (win probability 40 to 60%) than in\n    low-conflict trials (below 30% or above 70%), in patients and in healthy subjects (both p <\n    0.001, t test), with comparable effect sizes.\n  source: Figure S2B legend\n  quote: Patients and healthy subjects took longer to react in high-conflict trials (both p<0.001,\n    t-test), and the effect size was comparable between both groups\n  statistics:\n  - about: patients, high against low conflict\n    test: t test\n    p: 0.001\n    p_relation: \"<\"\n  - about: healthy subjects, high against low conflict\n    test: t test\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Reaction time is the button press time minus the game presentation time (the trial\n    start plus 750 ms, STAR Methods, Behavioral task; or the photodiode-derived presentation time\n    if the data give one). The unit and form of the t test are not stated; readings (a) a\n    two-sample t test over pooled trials; (b) a paired t test over the 10 subjects' mean RTs.\n    Reproduced for patients when, under one reading, high-conflict RTs are longer with p < 0.001.\n    The healthy-subject part needs data the paper does not say were deposited.\n- id: regressors-past-current-uncorrelated\n  statement: Past and current regressors were nearly uncorrelated (mean R2 2.1%, maximum R2 3.7%).\n  source: Results, Dissociable OFC Encoding of Past Choice and Outcome Information, paragraph 1\n  quote: past and current regressors were uncorrelated (mean R2 = 2.1%; max R2 = 3.7%)\n  expected:\n  - quantity: mean R2 between past and current regressors\n    value: 2.1\n    tolerance: 0.21\n    unit: percent\n  - quantity: maximum R2 between past and current regressors\n    value: 3.7\n    tolerance: 0.37\n    unit: percent\n  criterion: R2 is the squared Pearson correlation over non-timeout trials, within each patient.\n    Which pairs are meant is not stated; readings (a) each regressor with its own t-1 version (8\n    pairs); (b) every current regressor with every t-1 regressor (64 pairs); (c) as (b) with\n    t-1 to t-5. Also open whether R2 is averaged over patients or computed on trials pooled over\n    patients. Reproduced when both values are within tolerance under one reading.\n- id: figs6a-regressor-collinearity\n  statement: Regressors were weakly correlated between and within categories (mean R2 0.15, all R2\n    below 0.6).\n  source: Figure S6A legend\n  quote: Regressors were weakly correlated between and within categories (mean R2=0.15, all R2<0.6)\n  expected:\n  - quantity: mean R2 over pairs of regressors\n    value: 0.15\n    tolerance: 0.015\n  criterion: R2 is the squared Pearson correlation over non-timeout trials for all pairs of the\n    regressors used. Open which set (\"all pairs of regressors used in the study\"); readings (a)\n    the 8 current regressors; (b) the 8 current and 8 t-1 regressors; and whether pairs are\n    pooled over patients or averaged. Reproduced when, under one reading, the mean is within\n    tolerance and no pair reaches R2 0.6.\n- id: fig3-present-encoding\n  statement: OFC HFA encodes the choice regressors (risk, gamble choice, offer value, chosen value),\n    time locked to game presentation, and the outcome regressors (gamble win, gamble loss, RPE,\n    regret), time locked to outcome reveal, with average %EV above chance and a rise in the\n    number of encoding electrodes.\n  source: Results, OFC HFA Reflects Choice- and Outcome-Related Valuation Signals, paragraphs 2 and\n    3; Figure 3A to 3D; Table S2\n  quote: we found robust evidence within the HFA band for multiple valuation components related to\n    choice (risk, gamble choice, offer value, and expected value of chosen option ... and outcome\n    (gamble win, gamble loss, RPE, and regret) processing\n  expected:\n  - quantity: risk encoding electrodes (Table S2, sum over patients)\n    value: 50\n    tolerance: 5\n    unit: electrodes\n  - quantity: gamble encoding electrodes\n    value: 34\n    tolerance: 3.4\n    unit: electrodes\n  - quantity: offer value encoding electrodes\n    value: 31\n    tolerance: 3.1\n    unit: electrodes\n  - quantity: chosen value encoding electrodes\n    value: 26\n    tolerance: 2.6\n    unit: electrodes\n  - quantity: win index encoding electrodes\n    value: 45\n    tolerance: 4.5\n    unit: electrodes\n  - quantity: loss index encoding electrodes\n    value: 33\n    tolerance: 3.3\n    unit: electrodes\n  - quantity: RPE encoding electrodes\n    value: 28\n    tolerance: 2.8\n    unit: electrodes\n  - quantity: regret encoding electrodes\n    value: 35\n    tolerance: 3.5\n    unit: electrodes\n  criterion: Encoding electrodes as in the opening comment (p < 0.05 in 5 or more consecutive\n    windows, game or buttonpress epoch). The expected counts are the column sums of Table S2,\n    which the paper does not print; their mean proportion over all 16 current and past regressors\n    is 20.9%, the HFA value of hfa-more-than-fp, so Table S2 is read as this selection. Chance\n    for each regressor is the share of electrodes classified as encoding under the 1,000 label\n    shuffles (STAR Methods), and the chance %EV is the mean %EV of the electrodes so selected\n    under shuffles. Reproduced when at least six of the eight counts are within tolerance, every\n    regressor's count exceeds the 95th percentile of its shuffled count, the peak of the mean\n    %EV of choice regressors falls after game presentation in the game epoch and that of the\n    outcome regressors after outcome reveal (button press plus 550 ms); partially reproduced\n    when every count exceeds chance and the peaks fall as stated but fewer counts are within\n    tolerance.\n- id: fig3-latency-duration-similar\n  statement: The delays of choice encoding after game presentation and of outcome encoding after\n    outcome reveal did not differ (512.5 plus or minus 59 ms against 287 plus or minus 114.33 ms,\n    p = 0.14, t test), nor did their transient durations (612.15 plus or minus 132.9 ms against\n    712.5 plus or minus 112.5 ms, p = 0.58).\n  source: Results, OFC HFA Reflects Choice- and Outcome-Related Valuation Signals, paragraph 3\n  quote: The delays after the presentation of external information, game presentation and outcome\n    reveal, respectively, were not statistically different (512.5 ± 59 ms and 287 ± 114.33 ms; p\n    = 0.14; t test), with transient activation profiles of comparable duration (612.15 ± 132.9 ms\n    and 712.5 ± 112.5 ms, respectively; p = 0.58; t test)\n  statistics:\n  - about: delay, choice against outcome\n    test: t test\n    p: 0.14\n  - about: duration, choice against outcome\n    test: t test\n    p: 0.58\n  expected:\n  - quantity: delay of choice encoding after game presentation\n    value: 512.5\n    tolerance: 59\n    unit: ms\n  - quantity: delay of outcome encoding after outcome reveal\n    value: 287\n    tolerance: 114.33\n    unit: ms\n  - quantity: duration of choice encoding profile\n    value: 612.15\n    tolerance: 132.9\n    unit: ms\n  - quantity: duration of outcome encoding profile\n    value: 712.5\n    tolerance: 112.5\n    unit: ms\n  criterion: A claim of absence, judged by two-sample t tests at p < 0.05; tolerances are the stated\n    spreads. The paper does not define delay or duration here, nor the units of the t test. The\n    spreads and Figure 3B and 3D suggest one value per regressor (4 against 4). Readings (a) per\n    regressor, the delay is the time of the peak of the mean %EV of its encoding electrodes after\n    the event, and the duration is the time that mean profile stays above its shuffled chance\n    level; (b) per regressor, the delay is the first window centre after the event at which the\n    share of encoding electrodes exceeds chance, and the duration as in (a); (c) per electrode\n    and regressor, the delay to the start of the longest significant stretch and its length.\n    Reproduced when both t tests give p > 0.05 under the reading used; the values are compared\n    with the expected ones under each reading.\n- id: hfa-more-than-fp\n  statement: Across all regressors the proportion of encoding electrodes was greater with HFA than\n    with broadband field potentials (mean 20.9% against 3.3%, p < 10^-5, t test), and greater in\n    every instance.\n  source: Results, OFC HFA Reflects Choice- and Outcome-Related Valuation Signals, paragraph 4;\n    Figure S4A\n  quote: Across all regressors, the proportion of encoding electrodes identified using HFA was\n    significantly greater than using FP (mean HFA = 20.9% versus FP =\n  statistics:\n  - test: t test\n    p: 0.00001\n    p_relation: \"<\"\n    n: 16 regressors (8 current, 8 past)\n  expected:\n  - quantity: mean proportion of encoding electrodes, HFA\n    value: 20.9\n    tolerance: 2.09\n    unit: percent\n  - quantity: mean proportion of encoding electrodes, broadband FP\n    value: 3.3\n    tolerance: 0.33\n    unit: percent\n  criterion: For FP the same selection as for HFA, with broadband power in place of HFA (STAR\n    Methods). The 20.9% is the mean over the 16 current and t-1 regressors of the Table S2\n    proportions, so the t test is over 16 regressors; readings (a) paired; (b) two-sample.\n    Reproduced when both means are within tolerance, the HFA proportion is higher for every\n    regressor, and p < 10^-5 under one reading. Needs the broadband signal, which the dataset\n    description does not list.\n- id: figs4b-power-at-buttonpress\n  statement: Broadband power modulation across OFC was maximal at the button press and weak at the\n    time of maximal HFA outcome encoding (about 750 ms after outcome reveal), so HFA encoding is\n    distinct in time from broadband modulation.\n  source: Results, OFC HFA Reflects Choice- and Outcome-Related Valuation Signals, paragraph 4;\n    Figure S4B\n  quote: ERP modulation is maximal at the time of button press, and thus does not align in time\n    with maximal encoding of outcome information\n  criterion: The average broadband response over the 192 electrodes, locked to the button press,\n    against the mean %EV of the outcome regressors over their encoding electrodes. Whether the\n    \"ERP\" is the trial-averaged voltage or its power is open; readings (a) the mean absolute\n    trial-averaged voltage; (b) mean broadband power. Reproduced when, under one reading, the\n    maximum of the broadband response lies within 200 ms of the button press and the peak of\n    outcome %EV lies at least 400 ms after it (the outcome is revealed at 550 ms). Needs the\n    broadband signal.\n- id: fig4-past-encoding\n  statement: HFA encodes characteristics of the preceding trial; past choice and outcome features\n    are widely represented across OFC except past risk, dissociable from current signals.\n  source: Results, Dissociable OFC Encoding of Past Choice and Outcome Information, paragraphs 1\n    and 2; Figure 4A to 4D; Table S2\n  quote: past round features were widely represented across the OFC, with the exception of past\n    risk, and were dissociable from current choice and outcome signals\n  expected:\n  - quantity: past risk encoding electrodes (Table S2, sum over patients)\n    value: 17\n    tolerance: 1.7\n    unit: electrodes\n  - quantity: past gamble encoding electrodes\n    value: 43\n    tolerance: 4.3\n    unit: electrodes\n  - quantity: past win probability encoding electrodes\n    value: 46\n    tolerance: 4.6\n    unit: electrodes\n  - quantity: past chosen value encoding electrodes\n    value: 35\n    tolerance: 3.5\n    unit: electrodes\n  - quantity: past win index encoding electrodes\n    value: 49\n    tolerance: 4.9\n    unit: electrodes\n  - quantity: past loss index encoding electrodes\n    value: 56\n    tolerance: 5.6\n    unit: electrodes\n  - quantity: past RPE encoding electrodes\n    value: 50\n    tolerance: 5\n    unit: electrodes\n  - quantity: past regret encoding electrodes\n    value: 64\n    tolerance: 6.4\n    unit: electrodes\n  depends_on:\n  - fig3-present-encoding\n  criterion: The t-1 regressors, with the selection and chance of fig3-present-encoding, in both\n    epochs. Reproduced when at least six of the eight counts are within tolerance, each of the\n    seven past regressors other than risk has a count above the 95th percentile of its shuffled\n    count, and past risk has the lowest count of the eight. The paper does not define\n    \"dissociable\" here beyond Figures 4 and 5; that part is tested by fig5-past-sustained.\n- id: fig5-past-sustained\n  statement: Past-trial signals were sustained; the longest continuous stretch of significant\n    encoding was longer for past outcome (1,341.37 plus or minus 49.63 ms) and past choice\n    (1,169.15 plus or minus 61.2 ms) than for current choice (799.6 plus or minus 36.94 ms) and\n    current outcome (706.9 plus or minus 30.56 ms), all p < 10^-6, t test.\n  source: Results, Dissociable OFC Encoding of Past Choice and Outcome Information, paragraph 2;\n    Figure 5A and 5B\n  quote: both past outcome (average duration = 1,341.37 ± 49.63 ms) and past choice (1,169.15 ±\n    61.2 ms) showed significantly more sustained activation than current choice and outcome\n    signals (799.6 ± 36.94 and 706.9 ± 30.56 ms, respectively; all\n  statistics:\n  - about: each past group against each current group\n    test: t test\n    p: 0.000001\n    p_relation: \"<\"\n    n: electrode and regressor pairs with encoding, per group\n  expected:\n  - quantity: mean encoding duration, past outcome\n    value: 1341.37\n    tolerance: 49.63\n    unit: ms\n  - quantity: mean encoding duration, past choice\n    value: 1169.15\n    tolerance: 61.2\n    unit: ms\n  - quantity: mean encoding duration, current choice\n    value: 799.6\n    tolerance: 36.94\n    unit: ms\n  - quantity: mean encoding duration, current outcome\n    value: 706.9\n    tolerance: 30.56\n    unit: ms\n  depends_on:\n  - fig3-present-encoding\n  - fig4-past-encoding\n  criterion: Duration is the longest stretch in which all windows have p < 0.05 (STAR Methods),\n    for every encoding electrode and regressor pair in each group; groups as in the Figure 5\n    legend (choice is risk, gamble, offer value, chosen value; outcome is win, loss, RPE, regret;\n    past risk included). Tolerances are the SEMs the legend states; as SEMs are tight, a\n    secondary 10% band is reported. Open details, with readings. Stretch length (a) number of\n    windows times 50 ms; (b) that plus the 150 ms the 200-ms window adds; (c) from the first\n    window start to the last window end. Epoch (a) the longest stretch over both epochs, each\n    taken separately; (b) choice and past regressors in the game epoch and outcome regressors in\n    the buttonpress epoch. Reproduced when, under one reading, both past means exceed both\n    current means with two-sample t tests at p < 10^-6 for all four comparisons; partially\n    reproduced when all four are longer with p < 0.01 (the Figure 5 legend's level). The values\n    are compared with the expected ones under each reading.\n- id: behavior-past-no-effect\n  statement: None of the past trial characteristics significantly affected risk taking (all p >\n    0.15, random effects logistic regression).\n  source: Results, Dissociable OFC Encoding of Past Choice and Outcome Information, paragraph 3\n  quote: Random effects logistic regression showed that none of the past trial characteristics\n    significantly affected risk-taking\n  statistics:\n  - test: random effects logistic regression\n    p: 0.15\n    p_relation: \">\"\n    n: 10 patients\n  criterion: A claim of absence. Gamble choice regressed on each t-1 regressor with patient as\n    random effect (random intercept). Whether the past regressors enter one at a time or together,\n    and whether current win probability is in the model, is not stated; readings (a) one past\n    regressor at a time with current win probability as covariate; (b) one at a time alone.\n    Reproduced when no past regressor has p < 0.05 under reading (a), with (b) shown as a variant\n    and the paper's 0.15 compared; not reproduced when one does. Effect sizes are reported.\n- id: fig6-past-short-lived\n  statement: Encoding of past information was limited to the immediately preceding trial; the\n    proportion of electrodes encoding choices and outcomes 2 to 5 trials back was significantly\n    lower than for the current and previous trials (p < 0.01, t test), with no evidence of\n    encoding from earlier rounds.\n  source: Results, Dissociable OFC Encoding of Past Choice and Outcome Information, paragraph 3;\n    Figure 6A and 6B\n  quote: Strikingly, we found no evidence for encoding of information from earlier rounds\n  statistics:\n  - test: t test\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - fig3-present-encoding\n  - fig4-past-encoding\n  criterion: The proportion of encoding electrodes (selection of fig3-present-encoding) for each of\n    the 8 regressors at lags t, t-1 and t-2 to t-5 (Behavioral Analysis). The unit of the t test\n    is not stated; readings (a) per regressor proportions, t-2 to t-5 pooled against t and\n    against t-1 (two-sample); (b) per lag means over regressors, t-2 to t-5 against t and t-1.\n    \"No evidence\" is judged against the Null regressor line of Figure 6B, which the paper does\n    not define; read as the shuffled chance proportion of fig3-present-encoding. Reproduced when,\n    under one reading, t-2 to t-5 are lower than both t and t-1 with p < 0.01 and the t-2 to t-5\n    proportions do not exceed the 95th percentile of chance for more than one regressor in\n    five.\n- id: figs5d-sharp-boundary\n  statement: The distribution of encoding significance at the peak %EV shows a sharp boundary\n    between t-1 and t-2 but not between t and t-1 (one-sided Kolmogorov-Smirnov tests).\n  source: Figure S5C and S5D legends\n  quote: Summary statistical results for ECDFs in (C) highlighting the sharp temporal boundary in\n    encoding extent between t-1 and t-2, but not t and t-1\n  criterion: For each regressor and lag, the -log10 p of each electrode's linear regression at its\n    peak %EV window; ECDFs compared with one-sided Kolmogorov-Smirnov tests, t-1 greater than t\n    and t-2 greater than t-1, as the legend states (the direction \"t-1>t\" is read as t-1\n    stochastically larger). The paper prints no p values; the threshold is open, 0.05 is used as\n    a standard choice. Reproduced when the t-1 against t-2 comparison is significant and the t\n    against t-1 comparison is not, for a majority of the 8 regressors, or for the pooled\n    regressors.\n- id: mixed-effects-robust\n  statement: In nested mixed-effects models with patient and electrode as random effects, all\n    regressors were significant (all p < 10^-4, Bonferroni corrected).\n  source: Results, Dissociable OFC Encoding of Past Choice and Outcome Information, paragraph 4;\n    STAR Methods, Stepwise regression, paragraph 3\n  quote: We found that all of our regressors were significantly active\n  statistics:\n  - test: nested mixed-effects model\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  criterion: Concatenated HFA of all electrodes as dependent variable, round-by-round regressors as\n    fixed effects, electrode nested in patient as random effects (STAR Methods). Open, with\n    readings. Time point (a) the HFA in each window, one model per window, with a regressor\n    counted significant in any window after correction over windows and regressors; (b) the HFA\n    averaged over the epoch's post-event windows. Regressors (a) one model per regressor; (b) all\n    current and t-1 regressors together. Electrodes (a) all 192; (b) encoding electrodes only.\n    Bonferroni over the 16 regressors. Reproduced when, under one reading, every regressor has\n    corrected p < 10^-4.\n- id: figs6b-stepwise-similar\n  statement: Stepwise regression with model selection gave proportions of encoding electrodes per\n    regressor similar to those of the 5-consecutive-window selection.\n  source: Results, Dissociable OFC Encoding of Past Choice and Outcome Information, paragraph 4;\n    Figure S6B\n  quote: The proportion of electrodes encoding each reward-related computational component as\n    estimated by selecting electrodes with ≥5 consecutive encoding windows and stepwise regression\n    followed by model selection were similar\n  depends_on:\n  - fig3-present-encoding\n  - fig4-past-encoding\n  criterion: Stepwise procedure as in the opening comment (STAR Methods, Stepwise regression). The\n    paper gives no measure of \"similar\"; readings (a) the Spearman correlation across the 16\n    regressors of the two proportions is positive with p < 0.05; (b) every regressor's two\n    proportions differ by less than 10 percentage points. Reproduced when both hold, partially\n    when one does.\n- id: figs3a-risk-all-trials\n  statement: The risk regressor over all trials explains slightly more HFA variance than risk\n    restricted to gamble trials, so risk is encoded whatever the subsequent choice.\n  source: Figure S3A legend\n  quote: The regressor including all trials explains a slightly higher proportion of variance in\n    HFA (%EV), suggesting that risk is encoded regardless of subsequent patient choice\n  depends_on:\n  - fig3-present-encoding\n  criterion: Mean %EV time course of risk over risk-encoding electrodes, all non-timeout trials\n    against gamble trials only, game epoch. Open whether electrodes are those selected with all\n    trials or selected separately; the first is used as the one the legend implies (\"compared\n    the %EV of risk encoding\"). Reproduced when the all-trial peak mean %EV is at least as high as\n    the gamble-only peak.\n- id: figs3b-no-motor-encoding\n  statement: The direction of the response (left or right option) is not reflected in OFC HFA.\n  source: Figure S3B legend; Results, OFC HFA Reflects Choice- and Outcome-Related Valuation\n    Signals, paragraph 3; Discussion, paragraph 9\n  quote: Regressors encoding direction of choice (left/right options) are not reflected in OFC HFA\n  criterion: A claim of absence, judged with the paper's selection (p < 0.05 in 5 or more\n    consecutive windows) for a left or right response regressor in both epochs. Reproduced when\n    the proportion of electrodes so classified does not exceed the 95th percentile of its\n    shuffled chance proportion; not reproduced when it does. The proportion and the peak mean %EV\n    are reported.\n- id: anatomy-brodmann-counts\n  statement: Most electrodes lay in putative Brodmann area 11 (53 of 192), 13 (40) and 14 (67).\n  source: Results, Anatomical Distribution of Present and Past Valuation Signals, paragraph 1\n  quote: The majority of electrodes in our sample were located in putative BA 11 (n = 53 out of\n    192 total), 13 (n = 40/192), and 14 (n = 67/192)\n  expected:\n  - quantity: electrodes in BA 11\n    value: 53\n    tolerance: 0\n    unit: electrodes\n  - quantity: electrodes in BA 13\n    value: 40\n    tolerance: 0\n    unit: electrodes\n  - quantity: electrodes in BA 14\n    value: 67\n    tolerance: 0\n    unit: electrodes\n  criterion: Exact counts when the data carry the paper's area labels. When only coordinates are\n    available, the atlas assignment (JuBrain and AAL with visual confirmation from surgical\n    notes, STAR Methods) cannot be repeated exactly; counts within 10% are then partially\n    reproduced. Needs electrode locations, which the dataset description does not list.\n- id: fig7-all-areas-similar\n  statement: Electrodes encoding each signal type (present and past choice and outcome) were found\n    in all three areas (BA 11, 13 and 14), in similar proportions across areas.\n  source: Results, Anatomical Distribution of Present and Past Valuation Signals, paragraph 1;\n    Figure 7B to 7E; Figure S7A\n  quote: there was strong evidence for the presence of electrodes capturing each type of signal\n    (present and past choice and outcome) across all three areas\n  depends_on:\n  - anatomy-brodmann-counts\n  - fig3-present-encoding\n  - fig4-past-encoding\n  criterion: Electrodes encoding any regressor of a group (choice, outcome, past choice, past\n    outcome), as in Table S2's \"any\" rows. The paper names no test for \"similar\"; a chi-square\n    test of encoding against area per group is used, as the test the paper uses for the overlap\n    of groups (Figure S7). Reproduced when each group has encoding electrodes in all three areas\n    and no group's chi-square test has p < 0.05. Needs electrode locations.\n- id: no-anatomical-gradient\n  statement: There was no consistent evidence for differential encoding of individual valuation\n    components across BA 11, 13 and 14, nor along fronto-posterior or medio-lateral gradients.\n  source: Results, Anatomical Distribution of Present and Past Valuation Signals, paragraph 2;\n    STAR Methods, Anatomical reconstructions; Discussion, paragraph 7\n  quote: We found no consistent evidence for differential encoding of individual valuation\n    components across OFC subregions (BA 11/13/14), or across anatomical gradients\n    (fronto-posterior or medio-lateral; STAR Methods)\n  depends_on:\n  - anatomy-brodmann-counts\n  - fig3-present-encoding\n  criterion: A claim of absence, with the paper's tests (STAR Methods, Anatomical\n    reconstructions). For every electrode and regressor, the %EV at the window of the peak of the\n    regressor's mean %EV profile over encoding electrodes; per regressor, Kolmogorov-Smirnov\n    tests of these values between areas, and correlations with the x and y coordinates\n    (referenced to the anterior commissure). The paper gives no threshold, correlation type or\n    meaning of \"consistent\"; readings (a) p < 0.05 with Bonferroni over regressors and tests;\n    (b) p < 0.05 uncorrected, with \"consistent\" meaning the same area or direction for most\n    regressors of a group. Reproduced when no regressor is significant under (a) and no\n    consistent pattern appears under (b); the significant tests are listed either way. Pearson\n    correlation is used as the standard choice. Needs electrode locations.\n- id: tables2-patients-coverage\n  statement: All signals were present in at least 6 of the 10 patients (mean 7.41 plus or minus\n    0.4).\n  source: Results, Anatomical Distribution of Present and Past Valuation Signals, paragraph 2;\n    Table S2\n  quote: We found that all signals were present in at least 6 of the 10 patients in our sample\n    (mean = 7.41 ± 0.4; Table S2)\n  expected:\n  - quantity: mean number of patients with at least one encoding electrode per regressor\n    value: 7.41\n    tolerance: 0.4\n    unit: patients\n  depends_on:\n  - fig3-present-encoding\n  - fig4-past-encoding\n  criterion: Per regressor, the number of patients with at least one encoding electrode (selection\n    of fig3-present-encoding). The paper's own Table S2 does not give 7.41 by the plain reading;\n    counted from it, the 16 regressors give 7.75 patients on average and past risk is present in\n    only 5. Readings (a) the 16 current and t-1 regressors; (b) the 15 without past risk, which\n    the Results treat as the exception; (c) the four group rows (\"any choice\" and so on).\n    Reproduced when, under one reading, every regressor is present in at least 6 patients and the\n    mean is within tolerance; partially reproduced when the result matches Table S2 counted the\n    same way but not 7.41.\n- id: fig7f-multiplexing\n  statement: Most electrodes (132 of 192, 68.7%) encoded at least two of the four signal types\n    (choice, outcome, past choice, past outcome) and 30 of 192 (15.6%) encoded all four.\n  source: Results, Anatomical Distribution of Present and Past Valuation Signals, paragraph 3;\n    Figure 7F\n  quote: We observed significant overlap in electrode sets, with most electrodes (n = 132/192;\n    68.7%) encoding at least two types of signals and 15.6% of electrodes (n = 30/192) encoding\n    all four\n  expected:\n  - quantity: electrodes encoding at least two signal types\n    value: 132\n    tolerance: 13.2\n    unit: electrodes\n  - quantity: electrodes encoding all four signal types\n    value: 30\n    tolerance: 3\n    unit: electrodes\n  depends_on:\n  - figs6b-stepwise-similar\n  criterion: The Results say these sets come from the stepwise regression results, with an\n    electrode in a group when any regressor of the group survives model selection. Table S2's\n    selection (167 task-active electrodes) is a variant. Reproduced when both counts are within\n    tolerance under the stepwise reading; partially reproduced when they are within tolerance\n    only under the variant.\n- id: figs7-present-past-overlap\n  statement: Electrodes encoding both present and t-1 information were overrepresented, for choice\n    (39 of 120, 32.5%, against an expected 31, p < 0.05) and for outcome (43 of 120, 35.8%,\n    against an expected 34, p < 0.01), chi-square tests; many electrodes still encoded only\n    present or only past information.\n  source: Results, Anatomical Distribution of Present and Past Valuation Signals, paragraph 3;\n    Figure S7 legend\n  quote: We found an overrepresentation of electrodes that encoded both t+t-1 regressors both in\n    the case of choice (39/120 or 32.5%, vs. an expected 31/120 or 25.8% under assumption of\n    independence, p<0.05, chi-square test) and outcome information (n=43/120, or 35.8% vs. an\n    expected 34/120 or 28.5% under assumption of independence, p<0.01, chi-square test)\n  statistics:\n  - about: choice, present and past\n    test: chi-square test\n    p: 0.05\n    p_relation: \"<\"\n  - about: outcome, present and past\n    test: chi-square test\n    p: 0.01\n    p_relation: \"<\"\n  expected:\n  - quantity: electrodes encoding both present and past choice\n    value: 39\n    tolerance: 3.9\n    unit: electrodes\n  - quantity: electrodes encoding both present and past outcome\n    value: 43\n    tolerance: 4.3\n    unit: electrodes\n  depends_on:\n  - fig7f-multiplexing\n  criterion: A 2 by 2 chi-square test of independence of present and t-1 encoding, per signal\n    class, with the expected count under independence. The denominator 120 is not explained and\n    is not 192; readings (a) the 120 electrodes in BA 11, 13 and 14 with a confirmed label (the\n    Results give 53 + 40 + 67 = 160, so this is uncertain); (b) the electrodes encoding any\n    regressor under the stepwise selection; (c) all 192, with the counts scaled. Set membership\n    as in fig7f-multiplexing. Reproduced when, under one reading, both observed counts are within\n    tolerance and exceed the counts expected under independence with the stated p levels.\n- id: fig2-example-electrodes\n  statement: Example electrodes show risk encoding with an inverted U relation between win\n    probability and HFA at peak encoding, and regret encoding with a linear drop of HFA with\n    regret.\n  source: Figure 2D to 2G legends\n  quote: The relationship follows an inverted u shape with win probabilities as would be expected\n    for risk encoding\n  criterion: The paper does not identify the example electrodes. Among risk-encoding electrodes,\n    the HFA at each electrode's peak %EV window against win probability; among regret-encoding\n    electrodes, against regret. Reproduced when at least one risk electrode shows a significant\n    negative quadratic term in win probability (p < 0.05) and at least one regret electrode a\n    significant linear slope; the shares of encoding electrodes that do are reported.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import re
p='claims/saez-2018.yaml'; s=open(p).read()
s=s.replace("""is not 192; readings (a) the 120 electrodes in BA 11, 13 and 14 with a confirmed label (the
    Results give 53 + 40 + 67 = 160, so this is uncertain); (b) the electrodes encoding any
    regressor under the stepwise selection; (c) all 192, with the counts scaled.""","""is not 192 nor the 160 electrodes in BA 11, 13 and 14; readings (a) the electrodes encoding
    any choice or outcome regressor (current or t-1) under the stepwise selection; (b) the same
    under the 5-consecutive-window selection; (c) all 192, the counts compared as proportions.""")
s=s.replace("""Reproduced when no regressor is significant under (a) and no
    consistent pattern appears under (b); the significant tests are listed either way. Pearson
    correlation is used as the standard choice. Needs electrode locations.""","""The correlation is read as (a) Pearson or (b) Spearman. Reproduced when no
    regressor is significant under (a) and no consistent pattern appears under (b), with either
    correlation; the significant tests are listed either way. Needs electrode locations.""")
open(p,'w').write(s)
EOF
grep -nE "^[^#]*[^\"']: .*: " claims/saez-2018.yaml | grep -v "quote: \|statement: \|criterion: " | head; python tools/claims_check.py claims/saez-2018.yaml paper/10.1016-j.cub.2018.07.045.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The two unfound p-values are printed as "10�6" and "10�4" in the extraction (garbled minus); confirmed by reading. Fixing the fig4 quote, which straddles a page break.

**Agent calls Bash**

```bash
cd  sed -i 's/  quote: past round features were widely represented across the OFC, with the exception of past/  quote: features were widely represented across the OFC, with the exception of past/' claims/saez-2018.yaml; python tools/claims_check.py claims/saez-2018.yaml paper/10.1016-j.cub.2018.07.045.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/saez-2018.yaml`: 28 claims, all 28 with quotes. All quotes pass `tools/claims_check.py` word for word. The checker still flags two values it could not find: p < 10^-6 (fig5) and p < 10^-4 (mixed effects). The extraction prints their minus signs as "10�6" and "10�4"; I read them in the text and they are correct as recorded.

**Text read:** the version of record (PyMuPDF extraction plus the PDF), with the main text, legends, STAR Methods (e1 to e3) and the full Supplemental Information (Figures S1 to S7, Tables S1 and S2). Nothing the claims need is missing. The paper links no code; its analysis was in custom MATLAB and R scripts, so no code was read.

**Statistics:** 13 entries in 10 claims. **Criteria:** 27 claims have one; `behavior-risk-neutral` and `methods-electrode-trial-counts` have expected values as well.

**One finding from Table S2:** the paper does not print its column sums, so I added them up. Averaged over the 16 current and past regressors, they reproduce the paper's 20.9% of encoding electrodes for HFA. So Table S2 is the 5-consecutive-window selection, and its sums are used as expected counts.

**Two places where the paper disagrees with itself:**
- **Win probability:** the Methods say a shown 2 means 20%; Table S1 and the worked example say 0.8, i.e. (10 − n)/10. I used the second and kept the first as a variant.
- **"Mean = 7.41 patients":** counting from Table S2 gives 7.75, and past risk appears in only 5 patients, against the text's "at least 6". The criterion names three readings and allows partial reproduction.

**Details left open, with the readings named:**
- **Baseline:** the 200 ms before each epoch's own event, or before game presentation for both epochs.
- **Risk:** p(1−p)x², or p(1−p).
- **Offer value:** read as win probability, with p·x as a variant.
- **Past regressors after a timeout:** drop the trial, or use the last non-timeout round.
- **Behavior summary (55.9%):** the mean of per-patient percentages, or pooled over trials. The ± is not named (SD or SEM).
- **Random-effects logit:** random intercept only, or intercept and slope. For the past-trial effects: one regressor at a time, with or without current win probability as a covariate.
- **Test against healthy participants and reaction-time t tests:** per win-probability level or slope comparison; pooled trials or paired by subject.
- **Past–current R² and collinearity R²:** which pairs of regressors, and whether pooled or averaged over patients.
- **Latency and duration in Figure 3:** three definitions (peak of mean %EV, first window above chance, per-electrode stretch).
- **Figure 5 duration:** how stretch length is counted (window count × 50 ms, plus 150 ms, or start to end), and which epoch it is taken from.
- **Figure 6:** what the t test is run over, and the undefined "Null regressor" line, read as the shuffled chance level.
- **KS test threshold (Figure S5D):** none printed; 0.05 used as a standard choice.
- **Mixed-effects models:** which time point, which regressors per model, and which electrodes.
- **"Similar" in Figure S6B:** rank correlation, or within 10 percentage points.
- **Anatomical gradients:** the threshold (Bonferroni or uncorrected), what "consistent" means, and Pearson or Spearman correlation.
- **Overlap sets:** stepwise selection or the 5-window selection. The denominator of 120 in the Figure S7 chi-square tests is unexplained (it is not 192 nor 160).
- **Example electrodes in Figure 2:** not identified.

**Data the claims need that the paper does not place in the dataset:**
- **Healthy participants:** the paper does not say their data were deposited. This affects the patient-versus-control comparison and half of the reaction-time claim.
- **Broadband field-potential signal:** the dataset description lists only HFA. This affects `hfa-more-than-fp` and `figs4b-power-at-buttonpress`.
- **Electrode coordinates and Brodmann labels:** also not listed in the description. This affects the four anatomy claims.

Whether the dataset holds these is the author's to find.

## End of run

14 turns, 4 minutes, $1.40 at API prices, result: success.
