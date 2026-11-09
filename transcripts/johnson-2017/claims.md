# johnson-2017 · claims · run 42665012330

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,192p docs/protocol.md; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2017.05.046.txt"
}
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

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2017.05.046.txt",
 "offset": 766,
 "limit": 640
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/pfc-5.data-description.txt; cat papers/datasets/johnson-2017.yaml; grep -n "johnson-2017" -r papers/ | head; ls claims | wc -l
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -l "crcns" claims/*.yaml | head -5; f=$(grep -l "archive: crcns" claims/*.yaml | head -1); head -40 $f; grep -n "written by an agent" claims/*.yaml | head -3
```

```
claims/bruno-2017.yaml
claims/deweese-2004.yaml
claims/eyherabide-2008.yaml
claims/farrell-2020.yaml
claims/goncalves-2013.yaml
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
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A3 "^dataset\|^schema\|^paper:" claims/bruno-2017.yaml | head; grep -rn "analysis_scripts\|deposited in the data set\|code.*inside the data" claims/*.yaml | head -5; grep -n "open\b\|readings" claims/bruno-2017.yaml | head -5; sed -n 1,80p tools/claims_check.py | grep -n "def \|key\|field" | head -30
```

```
74:schema_version: 2
75:dataset:
76-  archive: crcns
77-  id: apl-1
78-  doi: 10.6080/K0SN074B
79:paper: doi:10.7554/elife.27342
80-claims:
81-- id: dataset-size
82-  statement: Three bouts of fictive locomotion were evoked in each of 10 isolated preparations
claims/johnson-2018.yaml:19:# analysis_scripts directory (one <metric>_compute script per analysis, with subfunctions, using
claims/johnson-2019.yaml:16:# data. By the data descriptor it is the analysis_scripts directory of data set fcx-3 itself. It is
6:# Text read: the version of record (PMC5546814, open access), as JATS XML flattened to text under
132:    measure of decay, so two readings, one from the Methods' own test of rate change for
154:    (Methods, Recurrence analysis; DataSet_Properties.m). Two details are open. The Gaussian SD
183:    not ("not all"; the paper does not count "many", so more than half is a rule fixed here). The SD and the readings of claim fig2b-dimensions are carried over; the
207:    code computes all three. The paper gives no measure of similarity, so two readings. (a) Across
34:def norm(s: str) -> str:
41:def flattenings(raw: str) -> list[str]:
48:def quote_found(quote: str, texts: list[str]) -> bool:
63:def printed_forms(v: float) -> set[str]:
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p claims/johnson-2018.yaml; sed -n 10,25p claims/johnson-2019.yaml; sed -n 78,200p tools/claims_check.py
```

```
# Claims for Johnson, Adams, Solbakk, Endestad, Larsson, Ivanovic, Meling, Lin & Knight (2018),
# PLoS Biology 16, e2004274, "Dynamic frontotemporal systems process space and time in working
# memory", doi:10.1371/journal.pbio.2004274, on CRCNS data set fcx-2 (doi:10.6080/K0VX0DQD).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record, open access, PMC5895055, as supplied under paper/ (Europe PMC
# full-text XML, flattened): Introduction, Results, Discussion, Materials and methods, the legends
# of Figures 1 to 8 and the captions of the supporting information. No PDF was supplied. The
# supporting information is S1 and S2 Fig (legends read) and S1 to S4 Table (DOCX files: group
# mixed-effects model outputs with degrees of freedom). Only the captions of the four tables were
# supplied; their contents were not read. Every claim below rests on a p-value the main text
# prints, so no claim needs the tables, but the full model outputs (degrees of freedom, F values
# of the PAC models) they hold were not available. Values shown only in figures (the percentages
# of Fig 4B, the grand means of Fig 8A, the per-subject PSI of Fig 3B) were not read.
#
# Code. The Data Availability statement says the "custom-built MATLAB codes" are deposited with
# the data on CRCNS (doi:10.6080/K0VX0DQD). The data descriptor says they are in the data set's
# analysis_scripts directory (one <metric>_compute script per analysis, with subfunctions, using
# FieldTrip). Being among the data set's files, they were not read in this run. Where a criterion
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas 2>/dev/null || grep -rn "def schema" tools/*.py | head -2; f=$(ls schemas/claims* 2>/dev/null | head -1); cat "$f" | head -150
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
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
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p schemas/claims.schema.json
```

```
"minLength": 1
          },
          "datasets": {
            "description": "Only when the paper is tested on more than one dataset: the folder names of those this claim rests on.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "minItems": 1
          }
        },
        "allOf": [
          {
            "not": {
              "required": [
                "quote",
                "inferred"
              ]
            }
          },
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm mutool; python -c "import fitz" && python - <<'E'
import fitz
d=fitz.open("paper/10.1016-j.cub.2017.05.046.pdf")
print(len(d))
for i in [3,4]:
    d[i].get_pixmap(dpi=130).save(f"p{i}.png")
E
ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2017.05.046.pdf",
 "pages": "4-5"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I can't render the PDF here (no pdftoppm or PyMuPDF), so the channels of the Figure 2 region of interest will be named as an open detail. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/johnson-2017.yaml",
 "content": "# Claims for Johnson, Dewar, Solbakk, Endestad, Meling & Knight (2017), Current Biology 27,\n# 1829-1835, \"Bidirectional Frontoparietal Oscillatory Systems Support Working Memory\",\n# doi:10.1016/j.cub.2017.05.046, on CRCNS data set pfc-5 (doi:10.6080/K0ZC811B).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-09,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record with its supplemental information, as supplied under paper/\n# (PDF extracted to text): main text (Results, Discussion), figure legends 1 to 4, STAR Methods\n# (pages e1 to e4), and the supplement (legends of Figures S1 to S4, Tables S1 to S3, read from\n# the text). The PDF could not be rendered in this run, so the figures themselves were not read:\n# the channel list of the Figure 2 cluster (the PFC region of interest of the PSI analysis) and\n# the time courses of Figures 2 to 4 are known only from the text and legends. The extraction\n# garbles symbols: \"3\" stands for the multiplication sign, \"/\" for an arrow, \"%\" for less than\n# or equal, \"R\" for greater than or equal, \"jZj\" for |Z|, and a replacement character for the\n# minus sign in exponents. Quotes keep the extracted characters. The CRCNS data descriptor\n# (paper/pfc-5.data-description.txt) was read only to know what the data set holds; no claim or\n# method comes from it.\n#\n# Code. The paper's Key Resources Table and Data and Software Availability say the custom MATLAB\n# code is deposited with the data at CRCNS (http://crcns.org). By the data descriptor it is the\n# analysis_scripts directory of pfc-5 itself (<metric>_compute, <metric>_stat_group,\n# <metric>_stat_group_hem, subfunctions; FieldTrip). Being among the data set's files, it was\n# not read in this run, and no commit is recorded. Every method below is from the paper's text.\n# Where those scripts settle a detail named as open below, the author may follow them (protocol,\n# Reader step 2) and should say so.\n#\n# Data the paper used (Experimental Model and Subject Details; Behavioral Task; Data\n# Acquisition; Data Preprocessing). 14 patients with unilateral lateral PFC lesions (7 left, 7\n# right; 5 stroke tested in Berkeley, 9 low-grade tumor resection tested in Oslo; 46 +- 16 years,\n# 5 males) and 20 healthy controls (44 +- 19 years, 11 males, all Berkeley). Per-patient lesion\n# hemisphere, etiology, size, years since lesion, age, gender, education, IQ and accuracy by\n# visual hemifield in Table S1. One session of 240 trials (at least 120 completed by every\n# subject), six bins of visual hemifield (left, right) by condition (identity, spatial relation,\n# temporal relation). Trial: 2 s pretrial fixation, start screen (IDENTITY or RELATION), 100 ms\n# fixation, two shapes of 200 ms each to one hemifield, a 900 or 1150 ms jittered maintenance\n# interval, a test prompt, an active processing interval of the same length as the maintenance,\n# then a two-alternative forced choice. 64-channel BioSemi EEG at 1024 Hz with EOG and earlobe\n# references; eye tracking used to drop trials in which gaze reached the ipsilateral hemifield.\n# Preprocessing: earlobe reference, 256 Hz, 1 to 70 Hz FIR, EMG removal (AAR), line noise\n# removal, ICA, channel interpolation, manual trial rejection (on average 187 trials per\n# subject kept). Then the surface Laplacian, swapping of channels across the midline for the 7\n# right-lesioned patients and 10 randomly chosen controls, so that the lesion is on the left, and\n# three segments per trial: pretrial baseline (550 to 50 ms before the start screen), encoding\n# and maintenance (1500 ms from first stimulus onset; the second stimulus ends at 400 ms), and\n# active processing (900 ms from the offset of the test prompt). Measured variables: accuracy,\n# ERPs, baseline power spectra, task-induced power, and phase slope index (PSI) between channels.\n# \"Lesioned visual hemifield\" trials are those whose stimuli went to the hemifield contralateral\n# to the lesion (Table S1 note).\n#\n# Methods shared by the EEG claims below, from STAR Methods (Spectral Decomposition; Phase Slope\n# Index; Statistical Bootstrapping; Cluster-Based Permutation Testing), fixed for every criterion\n# that cites \"the shared methods\":\n# - Correct trials only, except the baseline spectra (all trials). Each visual hemifield is\n#   analysed separately.\n# - Power, per subject: time-frequency representations at each frequency 1 to 40 Hz with a\n#   Hanning-tapered window of 3 cycles (3/f), 10 ms steps, segments zero-padded to 7500 ms. The\n#   baseline power of all correct trials and time points is pooled per channel and frequency;\n#   r values are drawn and averaged (r = the subject's trial count), 1000 times; the mean task\n#   power is Z scored on that distribution.\n# - PSI, per subject: the mean over correct trials (per visual hemifield) subtracted from each\n#   trial; the same time-frequency analysis in 100 ms steps; cross-spectra per frequency; PSI\n#   (Nolte et al. 2008) over 2 to 7 Hz (delta-theta) and 9 to 24 Hz (alpha-beta) for every\n#   channel pair. Null: frequency bins shuffled per channel pair and time point and PSI\n#   recomputed, 1000 times; raw PSI Z scored on the null. Encoding-maintenance and processing Z\n#   then have the temporal mean of the baseline Z subtracted. Positive PSI from A to B means A\n#   leads.\n# - Group tests: Monte Carlo cluster-based permutation (FieldTrip), independent-samples t test\n#   between patients (14) and controls (20), cluster-forming threshold 0.05 two-tailed, cluster\n#   size the sum of t, 1000 shuffles of group labels, cluster p < 0.05. Clusters over spatial\n#   adjacency and over time and/or frequency \"as appropriate\".\n# - Group by hemisphere interaction: a lesion-minus-intact index (e.g. F5 minus F6) for each\n#   non-midline channel pair, in both groups, then the group test on the index.\n#\n# Details the paper leaves open, shared by several criteria (each criterion names those it\n# needs):\n# - O1, channel neighbours for spatial clustering. Not given. Readings (a) FieldTrip's\n#   biosemi64 neighbour template; (b) neighbours by triangulation of the electrode positions.\n# - O2, which dimensions are clustered \"as appropriate\". Readings (a) channels by time by\n#   frequency (1 to 40 Hz) for power, channels by time for ERPs and band PSI; (b) channels by\n#   time on the band average named in the claim (3 to 4 Hz, 2 to 7 Hz, 9 to 24 Hz).\n# - O3, the hemisphere index. \"on all 54 non-midline channels\" with \"subtracting the signal in\n#   each intact-hemisphere channel from its lesioned-hemisphere homolog\". Readings (a) 27\n#   indices placed at the lesioned-hemisphere (left) positions; (b) 54 values, each channel\n#   minus its homolog.\n# - O4, which 10 controls were swapped across the midline: \"randomly chosen\". Readings (a) the\n#   swap already in the deposited preprocessed data, if it is there; (b) several random draws\n#   of 10, all shown.\n# - O5, the surface Laplacian's parameters. Not given; FieldTrip's ft_scalpcurrentdensity\n#   spline defaults are the standard choice. Whether the deposited preprocessed data already\n#   carry it is the author's to find.\n# - O6, the PFC region of interest for the PSI time courses (\"the lesioned PFC region of\n#   interest, as identified in the analysis of power asymmetry (see Figure 2)\"). The text does\n#   not list its channels. Readings (a) the lesioned-hemisphere anterior channels of the\n#   significant cluster found under claim power-lowtheta-interaction; (b) the ANTERIOR channels\n#   of Figure S4, AF7-F5-F7-FC5-FT7. Its partners, \"parieto-occipital channels in the same\n#   hemisphere\", are read as P1-P3-P5-P7-P9-PO3-PO7-O1, the left posterior set Figures S3 and\n#   S4 name.\n# - O7, the group summary behind a thresholded Z (\"single-subject analyses revealed ... Z >\n#   1.96\" on a figure of group means). Readings (a) the group mean of the subjects' Z crosses\n#   the threshold; (b) most subjects' Z crosses it.\nschema_version: 2\npaper: doi:10.1016/j.cub.2017.05.046\nclaims:\n- id: cohort-and-trials\n  statement: The study has 14 unilateral PFC patients and 20 age- and education-matched\n    controls; after cleaning, subjects kept on average 187 trials, 94 +- 21 (55 to 119) in the\n    lesioned and 93 +- 22 (51 to 120) in the intact visual hemifield.\n  source: Results, paragraph 1; STAR Methods, Data Preprocessing, EEG Cleaning, last sentence\n  quote: 'Fourteen unilateral PFC patients (mean ± SD: 46 ± 16 years of age; 15 ± 3 years of\n    education; Figures 1A and S1; Table S1) and 20 age- and education-matched healthy controls\n    ... The final dataset included an average of 187 trials per subject (mean ± SD [range]\n    trials: 94 ± 21 [55-119] lesioned visual hemifield, 93 ± 22 [51-120] intact visual\n    hemifield).'\n  expected:\n  - quantity: patients\n    value: 14\n    tolerance: 0\n  - quantity: controls\n    value: 20\n    tolerance: 0\n  - quantity: mean trials per subject after cleaning\n    value: 187\n    tolerance: 18.7\n  - quantity: mean trials, lesioned visual hemifield\n    value: 94\n    tolerance: 21\n  - quantity: mean trials, intact visual hemifield\n    value: 93\n    tolerance: 22\n  criterion: Subjects are counted, and trials are counted per subject and visual hemifield\n    after all exclusions. The paper does not say whether these counts include incorrect trials.\n    Readings (a) all trials kept after cleaning; (b) correct trials only. Means use the paper's\n    SD as tolerance. The ranges hold when the minimum and maximum fall within 55 to 119 and 51\n    to 120 widened by 10% of each bound.\n- id: demographics-matched\n  statement: Controls do not differ from patients in age or education, nor in variance.\n  source: STAR Methods, Experimental Model and Subject Details, paragraph 1\n  quote: independent-samples t tests with equal variance confirmed that the control group matched\n    on demographics (age t1,32 < 0.36, p > 0.72; education t1,32 < 1.22, p > 0.23; variance\n    F13,19 < 1.31, one-tailed p > 0.31)\n  statistics:\n  - about: age, patients against controls\n    test: independent-samples t test, equal variance\n    statistic: t(1,32) < 0.36\n    p: 0.72\n    p_relation: \">\"\n  - about: education, patients against controls\n    test: independent-samples t test, equal variance\n    statistic: t(1,32) < 1.22\n    p: 0.23\n    p_relation: \">\"\n  - about: variance, patients against controls\n    test: F test of variances, one-tailed\n    statistic: F(13,19) < 1.31\n    p: 0.31\n    p_relation: \">\"\n  expected:\n  - quantity: patient mean age\n    value: 46\n    tolerance: 16\n    unit: years\n  - quantity: control mean age\n    value: 44\n    tolerance: 19\n    unit: years\n  criterion: A claim of absence, judged on the paper's tests. Two-tailed independent-samples t\n    tests with pooled variance on age and on years of education, 14 patients against 20\n    controls, and a one-tailed F test of variances with 13 and 19 degrees of freedom (patients\n    in the numerator). The paper does not say which variable's variance was tested; readings\n    (a) age, (b) education, (c) both. Reproduced when none of the tests gives p < 0.05; not\n    reproduced when one does. The t, F and p values are reported either way.\n- id: patient-factors-no-effect\n  statement: In patients, no lesion or demographic factor (lesion hemisphere, etiology, size,\n    years since lesion, age, gender, education, IQ) nor visual hemifield or condition has a\n    significant effect on accuracy, which permits pooling the patients into one group.\n  source: Results, Behavior, paragraph 1; Table S2\n  quote: No significant effects were observed (p > 0.14; Table S2), permitting the normalization\n    of patient data into one group [24].\n  statistics:\n  - test: repeated-measures mixed ANCOVA\n    p: 0.14\n    p_relation: \">\"\n    n: 14 patients\n  criterion: A claim of absence, judged on the paper's test (STAR Methods, Behavioral Analysis;\n    Table S2). Patient accuracy per visual hemifield (lesion, intact) and condition (identity,\n    spatial, temporal) in a repeated-measures ANCOVA with lesion hemisphere, etiology (stroke\n    against tumor resection, one degree of freedom as Table S2 gives), lesion size, years\n    elapsed, age, gender, education and IQ as between-subject terms, and the terms Table S2\n    lists (hemisphere by etiology, hemisphere by gender, etiology by gender, and their\n    interactions with the within-subject factors). Reproduced when no term has p < 0.05; not\n    reproduced when one does. All F and p values are reported against Table S2. The\n    per-patient covariates are in Table S1; whether the data set holds them is the author's to\n    find.\n- id: table-s1-patient-accuracy\n  statement: Each patient's accuracy in the lesioned and intact visual hemifield is as Table S1\n    lists, from 0.65 to 0.98.\n  source: Table S1\n  inferred: Numbers from Table S1 (Accuracy, Lesion VHF and Intact VHF columns); no sentence of\n    the text states them.\n  criterion: Accuracy per patient and visual hemifield as the fraction of correct trials after\n    the eye-gaze exclusion. Patients are matched to Table S1 rows by subject number if the data\n    set numbers them alike, otherwise by lesion hemisphere, etiology, age and gender. Tolerance\n    0.02 per value (the table prints two decimals, and with about 100 trials per hemifield a\n    trial or two of exclusion moves the value by 0.01 to 0.02; 10% of the value would not tell\n    patients apart). Reproduced when at least 26 of the 28 values are within tolerance;\n    partially reproduced for 20 to 25. Readings for the denominator (a) all trials after the\n    eye-gaze exclusion; (b) the trials kept after EEG cleaning.\n- id: accuracy-patients-impaired\n  statement: PFC patients are less accurate than controls (mean +- SD 0.87 +- 0.08 against 0.95\n    +- 0.03), a group effect with p < 7 x 10^-5 in the mixed-effects model with group as the only\n    fixed effect.\n  source: Results, Behavior, paragraph 2; Figure 1C; Table S3\n  quote: 'Results revealed that PFC patients were impaired at the task relative to controls (mean\n    ± SD correct: controls 0.95 ± 0.03 versus patients 0.87 ± 0.08'\n  statistics:\n  - about: group, model with group as the only fixed effect\n    test: mixed-effects model (fitglme)\n    statistic: F(1,202) = 16.77, Cohen's d = 1.47\n    p: 0.00007\n    p_relation: \"<\"\n    n: 14 patients and 20 controls\n  - about: group, full model with group, visual hemifield and condition\n    test: mixed-effects model (fitglme)\n    statistic: F(1,196) = 4.70, Cohen's d = 0.78\n    p: 0.03\n    corrected: does not survive Bonferroni over 7 effects (alpha 0.0071)\n  expected:\n  - quantity: control mean accuracy\n    value: 0.95\n    tolerance: 0.03\n  - quantity: patient mean accuracy\n    value: 0.87\n    tolerance: 0.08\n  - quantity: F of group, group-only model\n    value: 16.77\n    tolerance: 1.68\n  criterion: The model is from STAR Methods, Behavioral Analysis, and Table S3. Its rows are\n    read as the 204 subject by visual hemifield by condition accuracies (34 x 6), with a random\n    intercept per subject; the denominator degrees of freedom of Table S3 (196, 202, 200) fit\n    this and a condition term of one degree of freedom (condition coded as one number). The\n    paper calls the model \"logit mixed-effects\" in the Results and \"linear mixed-effects\" in\n    the Methods. Readings (a) a Gaussian (linear) model on the cell accuracies; (b) a binomial\n    logit model on the cells, weighted by trial counts; (c) condition as a three-level factor\n    instead of one number. Group means are over each subject's accuracy, read (a) over all the\n    subject's trials or (b) as the mean of its six cells. Reproduced when, under one reading,\n    both means are within tolerance and the group effect of the group-only model has p < 7 x\n    10^-5 with patients lower; partially reproduced when the means hold and p < 0.0071 (the\n    paper's Bonferroni level). The full model's group effect is reported as well.\n- id: patients-above-chance\n  statement: Despite the impairment, patients perform well above the 0.5 chance rate.\n  source: Results, Behavior, paragraph 2\n  quote: Nonetheless, patients performed well above chance (pairedsample t1,13 > 15.43\n  statistics:\n  - test: paired-sample t test against chance, one-tailed\n    statistic: t(1,13) > 15.43\n    p: 5.0e-10\n    p_relation: \"<\"\n    n: 14 patients\n  expected:\n  - quantity: smallest t against chance\n    value: 15.43\n    tolerance: 1.54\n  criterion: Patient accuracy against 0.5 by a one-tailed t test with 13 degrees of freedom.\n    The \">\" in \"t1,13 > 15.43\" suggests more than one test; readings (a) one test on each\n    patient's overall accuracy; (b) one per visual hemifield; (c) one per visual hemifield and\n    condition. Reproduced when, under one reading, every test gives t above 13.89 (15.43 less\n    10%) and one-tailed p < 5 x 10^-10.\n- id: accuracy-no-hemifield-condition-effect\n  statement: Accuracy does not differ between visual hemifield presentations or between\n    conditions.\n  source: Results, Behavior, paragraph 2; Figure 1D; Table S3, third model\n  quote: There were no differences between visual hemifield presentations or conditions\n    (uncorrected p > 0.05).\n  statistics:\n  - about: visual hemifield, model with visual hemifield and condition only\n    test: mixed-effects model (fitglme)\n    statistic: F(1,200) = 0.46\n    p: 0.50\n  - about: condition, same model\n    test: mixed-effects model (fitglme)\n    statistic: F(1,200) = 1.74\n    p: 0.19\n  - about: visual hemifield by condition, same model\n    test: mixed-effects model (fitglme)\n    statistic: F(1,200) = 0.39\n    p: 0.53\n  depends_on:\n  - accuracy-patients-impaired\n  criterion: A claim of absence, judged on the paper's test, the model with only visual\n    hemifield and condition fixed effects (Table S3, third model; STAR Methods, Behavioral\n    Analysis), with the model readings of claim accuracy-patients-impaired. Reproduced when the\n    visual hemifield, condition and interaction effects all have uncorrected p > 0.05; not\n    reproduced when any has p < 0.05. Effect sizes are reported either way. The full model's\n    visual hemifield and condition effects (Table S3, p = 0.06 each) are shown as a variant.\n- id: erp-lesioned-maintenance\n  statement: For stimuli presented to the lesioned visual hemifield, patients show attenuated\n    positive ERPs in posterior channels and reversed-polarity signals in lesioned-hemisphere\n    anterior channels early in maintenance.\n  source: Results, Task-Induced ERPs; Figure S2A\n  quote: PFC patients exhibited attenuated positive-polarity ERPs in parieto-occipital channels\n    (pcluster = 0.03) and reversed-polarity signals in lesioned-hemisphere anterior channels\n    (F5-F7-FC5-FT7-C3C5-T7; pcluster = 0.002).\n  statistics:\n  - about: posterior channels, group main effect\n    test: cluster-based permutation test\n    p: 0.03\n    n: 14 patients and 20 controls\n  - about: lesioned-hemisphere anterior channels, group main effect\n    test: cluster-based permutation test\n    p: 0.002\n    n: 14 patients and 20 controls\n  criterion: ERPs from STAR Methods, Event-Related Potentials. Correct lesioned-hemifield\n    trials, segments zero-padded and 30 Hz low-pass FIR filtered, averaged, and the mean of the\n    500 ms pretrial baseline subtracted, over the 1500 ms encoding-maintenance segment. Group\n    test with the shared methods on all 64 channels by time, over the whole segment. The\n    zero-padding is written \"7,500\" with no unit (ms or samples); either is a standard choice\n    and cannot change the outcome much. Open details O1, O2, O4, O5. Reproduced when two\n    clusters have p < 0.05 after the second stimulus ends (400 ms), one with patients below\n    controls that includes P6, P8, P10 or PO8 (the POSTERIOR channels of Figure S2A), and one\n    of opposite sign to the controls' ERP in lesioned-hemisphere anterior channels among F5,\n    F7, FC5, FT7, C3, C5 and T7. Partially reproduced when only one of them holds.\n- id: erp-processing-interaction\n  statement: At active processing, for lesioned-hemifield stimuli, ERPs show a group by\n    hemisphere interaction without a group main effect; patients have enhanced signal in\n    lesioned-hemisphere anterior channels 100 ms after the test prompt, relative to the intact\n    homologs.\n  source: Results, Task-Induced ERPs\n  quote: At active processing, there was a group 3 hemisphere interaction (pcluster = 0.034) but no\n    group main effect (pcluster > 0.26). Enhanced signal was detected in patients 100 ms after\n    presentation of the test prompt in lesioned-hemisphere anterior channels\n    (FP1-AF3-AF7-F5-F7FC5-FT7), relative to the homologous, intact-hemisphere channels.\n  statistics:\n  - about: group by hemisphere interaction\n    test: cluster-based permutation test\n    p: 0.034\n  - about: group main effect\n    test: cluster-based permutation test\n    p: 0.26\n    p_relation: \">\"\n  criterion: ERPs as in claim erp-lesioned-maintenance over the 900 ms active processing\n    segment (from test prompt offset), correct lesioned-hemifield trials. The interaction is the\n    shared group test on the hemisphere index (O3) by time; the main effect the group test on\n    all 64 channels by time. Open details O1, O2, O3, O4, O5. Reproduced when an interaction\n    cluster has p < 0.05, with patients' lesion-minus-intact index above the controls' in\n    channels among FP1, AF3, AF7, F5, F7, FC5 and FT7 near 100 ms, and no group main effect\n    cluster has p < 0.05. Partially reproduced when the interaction holds and a main effect\n    cluster is also significant.\n- id: erp-intact-none\n  statement: None of the ERP group effects is seen when stimuli are presented to the intact\n    visual hemifield.\n  source: Results, Task-Induced ERPs; Figure S2B\n  quote: None of these effects was observed on trials in which stimuli were presented to the\n    intact visual hemifield (pcluster > 0.33)\n  statistics:\n  - test: cluster-based permutation test\n    p: 0.33\n    p_relation: \">\"\n  depends_on:\n  - erp-lesioned-maintenance\n  - erp-processing-interaction\n  criterion: A claim of absence, judged on the paper's tests, the group main effect and group by\n    hemisphere tests of claims erp-lesioned-maintenance and erp-processing-interaction run on\n    correct intact-hemifield trials, at cluster p < 0.05. Reproduced when no cluster in any of\n    them has p < 0.05; not reproduced when one does. The smallest cluster p of each test is\n    reported.\n- id: baseline-spectral-interaction\n  statement: In the pretrial baseline, patients have higher raw power between 6 and 18 Hz in\n    lesioned-hemisphere anterior channels (AF3, F3, F5) than in the intact homologs, a group by\n    hemisphere interaction (a steepened spectral slope over the lesion).\n  source: Results, Baseline Neurological Effects; Figure S3\n  quote: Cluster-based permutation testing of raw power spectra revealed a group 3 hemisphere\n    interaction (pcluster = 0.004) ... Enhanced power was detected between 6 and 18 Hz in\n    lesioned-hemisphere anterior channels, relative to the homologous, intact-hemisphere\n    channels, defining baseline effects in patients.\n  statistics:\n  - about: group by hemisphere interaction\n    test: cluster-based permutation test\n    p: 0.004\n    n: 14 patients and 20 controls\n  criterion: Spectra from STAR Methods, Baseline Spectral Power. All trials, the 500 ms pretrial\n    segment zero-padded to 7500 ms, Hanning taper, FFT, power at each frequency 1 to 40 Hz,\n    averaged over trials per subject (raw, not log). Group test on the hemisphere index (O3) by\n    frequency, with the shared methods. Open details O1, O3, O4, O5. Reproduced when a cluster\n    has p < 0.05 with patients' index above the controls', spanning frequencies within about 6\n    to 18 Hz and including AF3, F3 or F5; partially reproduced when the cluster is significant\n    but lies elsewhere in frequency or space.\n- id: baseline-no-group-effect\n  statement: Baseline raw power shows no main effect of group.\n  source: Results, Baseline Neurological Effects; Figure S3 legend\n  quote: but no main effect of group (uncorrected p > 0.05)\n  statistics:\n  - test: cluster-based permutation test (independent-samples t, uncorrected)\n    p: 0.05\n    p_relation: \">\"\n  criterion: A claim of absence, judged on the paper's test (STAR Methods, Cluster-Based\n    Permutation Testing, \"Baseline power was tested for main effects of group on all 64\n    channels\"). Spectra as in claim baseline-spectral-interaction; independent-samples t test\n    of patients against controls at each channel and frequency 1 to 40 Hz. The paper says p >\n    0.05 uncorrected, so no point passes the cluster-forming threshold. Reproduced when no\n    cluster has p < 0.05; the number of channel-frequency points with uncorrected p < 0.05 is\n    reported, and the claim is marked as only partly holding when any point passes.\n- id: power-anterior-theta-controls\n  statement: In controls, delta-theta (2 to 7 Hz) power in anterior channels rises during\n    encoding-maintenance and stays elevated through active processing, where it peaks, above Z\n    = 3.29 against the pretrial baseline.\n  source: Results, Task-Induced Power, paragraph 2; Figure S4A\n  quote: Activity in the delta-theta (2–7 Hz) range marked the encodingmaintenance interval in\n    anterior channels, which increased and then remained elevated through processing (Z > 3.29\n    versus pretrial baseline; p < 0.001; Figure S4).\n  statistics:\n  - test: bootstrapped Z against the pretrial baseline\n    statistic: Z > 3.29\n    p: 0.001\n    p_relation: \"<\"\n    n: 20 controls\n  criterion: Z-scored power with the shared methods, averaged over 2 to 7 Hz and the ANTERIOR\n    channels of Figure S4 (AF7, F5, F7, FC5, FT7), per control. Figure S4 does not split by\n    visual hemifield; readings (a) both hemifields pooled; (b) each hemifield. Open details O4,\n    O5, O7. Reproduced when the controls' Z exceeds 3.29 during active processing and its\n    maximum over the trial lies in active processing; partially reproduced when it exceeds\n    3.29 but peaks earlier.\n- id: power-posterior-alphabeta\n  statement: Posterior channels show beta-gamma (12 to 35 Hz) increases and alpha\n    desynchronization at encoding, then alpha-beta (9 to 24 Hz) decreases through maintenance\n    (|Z| > 1.96) and active processing (Z < -3.29), in both groups.\n  source: Results, Task-Induced Power, paragraph 3; Figure S4\n  quote: increased parieto-occipital activity in the betagamma range (12–35 Hz) and narrowband\n    alpha desynchronization marked visual processing during encoding, followed by widespread\n    alpha-beta (9–24 Hz) decreases throughout maintenance\n  statistics:\n  - about: alpha-beta at maintenance\n    test: bootstrapped Z against the pretrial baseline\n    statistic: '|Z| > 1.96'\n    p: 0.05\n    p_relation: \"<\"\n  - about: alpha-beta at active processing\n    test: bootstrapped Z against the pretrial baseline\n    statistic: Z < -3.29\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Z-scored power with the shared methods over the POSTERIOR channels of Figure S4 (P1,\n    P3, P5, P7, P9, PO3, PO7, O1), per group. Visual hemifield readings as in claim\n    power-anterior-theta-controls. Open details O4, O5, O7. Reproduced when, in each group, the\n    9 to 24 Hz Z is below -1.96 through maintenance (400 ms after first stimulus onset to the\n    test prompt) and below -3.29 during active processing, and the 12 to 35 Hz Z is above zero\n    during encoding (0 to 400 ms). Partially reproduced when the alpha-beta decreases hold in\n    one group only, or hold but not the encoding increase.\n- id: power-lowtheta-interaction\n  statement: At active processing, patients have reduced low-theta (3 to 4 Hz) power in\n    lesioned-hemisphere anterior channels relative to the intact homologs, a group by\n    hemisphere interaction found both when stimuli went to the lesioned and to the intact\n    visual hemifield.\n  source: Results, Task-Induced Power, paragraph 2; Figure 2A and 2B\n  quote: Cluster-based permutation testing revealed group 3 hemisphere interaction effects\n    (pcluster % 0.04; Figure 2) ... Reduced low-theta (3–4 Hz) power was detected in anterior\n    channels in the lesioned hemisphere, relative to the homologous channels in the intact\n    hemisphere.\n  statistics:\n  - about: lesioned visual hemifield\n    test: cluster-based permutation test, group by hemisphere\n    p: 0.04\n  - about: intact visual hemifield\n    test: cluster-based permutation test, group by hemisphere\n    p: 0.036\n  criterion: Z-scored power with the shared methods over the 900 ms active processing segment,\n    correct trials, each visual hemifield separately; group test on the hemisphere index (O3).\n    Open details O1, O2, O3, O4, O5. Reproduced when, for both hemifields, a cluster has p <\n    0.05 with patients' lesion-minus-intact index below the controls', covering 3 to 4 Hz in\n    lesioned-hemisphere anterior channels; partially reproduced when this holds for one\n    hemifield only.\n- id: power-no-group-main-effect\n  statement: Task-induced power shows no group main effect, neither for anterior theta nor for\n    the posterior alpha-beta decreases.\n  source: Results, Task-Induced Power, paragraphs 2 and 3; Figure 2A legend; Figure S4B legend\n  quote: but non-significant group main effects (pcluster > 0.10) ... These patterns did not\n    differ by group (pcluster > 0.52)\n  statistics:\n  - about: all task-induced power\n    test: cluster-based permutation test, group main effect\n    p: 0.10\n    p_relation: \">\"\n  - about: posterior alpha-beta patterns\n    test: cluster-based permutation test, group main effect\n    p: 0.52\n    p_relation: \">\"\n  - about: anterior theta at active processing (Figure 2A)\n    test: cluster-based permutation test, group main effect\n    p: 0.61\n    p_relation: \">\"\n  criterion: A claim of absence, judged on the paper's test, the group cluster test with the\n    shared methods on Z-scored power on all 64 channels, for encoding-maintenance and active\n    processing and each visual hemifield. Open details O1, O2, O4, O5. Reproduced when no\n    cluster has p < 0.05; not reproduced when one does. Cluster p values and the size of the\n    group difference in anterior 3 to 4 Hz and posterior 9 to 24 Hz Z are reported either way.\n- id: psi-deltatheta-bottomup-encoding\n  statement: In both groups, delta-theta PSI shows parieto-occipital regions leading PFC at the\n    offset of the second stimulus at encoding, at baseline-corrected Z of -10 or below.\n  source: Results, Task-Induced Directional Connectivity, paragraph 3; Figure 3A and 3B, left\n  quote: Parieto-occipital / PFC PSI marked the offset of the second stimulus at encoding\n  statistics:\n  - test: PSI Z against frequency-shuffled null, baseline-corrected\n    statistic: Z <= -10\n    p: 2.0e-23\n    p_relation: \"<\"\n  expected:\n  - quantity: baseline-corrected delta-theta PSI Z (PFC to parieto-occipital) at second stimulus\n      offset\n    value: -10\n    tolerance: 1\n  criterion: Delta-theta PSI Z with the shared methods, from PFC channels to parieto-occipital\n    channels of the lesioned hemisphere (O6), averaged over channel pairs, correct trials, each\n    visual hemifield. Open details O4, O5, O6, O7. Reproduced when, under one reading, both\n    groups reach Z of -9 or below (within 10% of -10) within 100 ms of 400 ms after first\n    stimulus onset, in both hemifields; partially reproduced when Z is negative and below -1.96\n    there but does not reach -9.\n- id: psi-deltatheta-pfc-lead-controls\n  statement: In delta-theta PSI, controls shift to PFC leading parieto-occipital regions in\n    mid-maintenance (Z > 1.96), and the PFC lead peaks early in active processing (Z of 10 or\n    more), whereas patients show zero directionality (Z < 1.96).\n  source: Results, Task-Induced Directional Connectivity, paragraph 3; Figure 3A and 3B, left\n  quote: Controls then exhibited a shift in directionality so that PFC drove parieto-occipital\n    regions mid-maintenance (Z > 1.96; p < 0.05). PFC / parieto-occipital PSI continued to\n    increase in controls with executive demands such that the PFC lead peaked early during\n    active processing ... whereas PFC patients exhibited zero directionality (Z < 1.96; p >\n    0.05).\n  statistics:\n  - about: controls, mid-maintenance\n    test: PSI Z against frequency-shuffled null, baseline-corrected\n    statistic: Z > 1.96\n    p: 0.05\n    p_relation: \"<\"\n  - about: controls, early active processing\n    test: PSI Z against frequency-shuffled null, baseline-corrected\n    statistic: Z >= 10\n    p: 2.0e-23\n    p_relation: \"<\"\n  - about: patients\n    test: PSI Z against frequency-shuffled null, baseline-corrected\n    statistic: Z < 1.96\n    p: 0.05\n    p_relation: \">\"\n  expected:\n  - quantity: controls' peak baseline-corrected delta-theta PSI Z (PFC to parieto-occipital),\n      early active processing\n    value: 10\n    tolerance: 1\n  depends_on:\n  - power-lowtheta-interaction\n  criterion: PSI as in claim psi-deltatheta-bottomup-encoding. Reproduced when, under one\n    reading, in both visual hemifields the controls' Z exceeds 1.96 at some point of\n    maintenance, reaches at least 9 (10 less 10%) in the first half of active processing, with\n    its maximum there, and the patients' Z stays below 1.96 through maintenance and\n    processing. Partially reproduced when the controls' pattern holds with a peak between 1.96\n    and 9, or holds in one hemifield only.\n- id: psi-deltatheta-group-clusters\n  statement: Across all 64 by 64 channel pairs, delta-theta PSI differs between groups\n    intermittently during encoding and maintenance and in a sustained way during active\n    processing.\n  source: Results, Task-Induced Directional Connectivity, paragraph 3; Figure 3, right\n  quote: 'Cluster-based permutation testing of all 64-by-64 channel pairs revealed intermittent\n    group effects during encoding and maintenance (lesioned/intact visual hemifield: 100–200/200–300\n    and 700–800/1,000–1,200 ms) and sustained effects during active processing (100–700/0–500 ms;\n    pcluster < 0.05).'\n  statistics:\n  - test: cluster-based permutation test, group main effect\n    p: 0.05\n    p_relation: \"<\"\n    n: 14 patients and 20 controls\n  criterion: Delta-theta PSI Z (baseline-corrected) with the shared methods for every channel\n    pair, 100 ms steps, each visual hemifield; group cluster test on pairs by time. How pairs\n    are clustered is open; readings (a) over time only, per pair; (b) over time and over pairs\n    whose both channels are neighbours (O1). The windows are read as lesioned hemifield 100 to\n    200 and 700 to 800 ms (encoding-maintenance) and 100 to 700 ms (processing), intact\n    hemifield 200 to 300 and 1000 to 1200 ms and 0 to 500 ms. Open details O1, O4, O5.\n    Reproduced when, under one reading and in both hemifields, significant clusters (p < 0.05)\n    cover most of the processing window and some of the encoding-maintenance windows, within\n    100 ms (one time step) of the stated edges; partially reproduced when only the processing\n    effects hold.\n- id: psi-network-degree\n  statement: A post hoc network analysis of delta-theta PSI shows group differences from\n    lesioned PFC to bilateral central-posterior regions, sustained for 200 ms early in active\n    processing, for both visual hemifields.\n  source: Results, Task-Induced Directional Connectivity, paragraph 4; Figure 3, right\n  quote: Cluster-based permutation testing of network data revealed group effects from lesioned\n    PFC to bilateral central-posterior regions that were sustained for 200 ms early during active\n    processing, regardless of whether stimuli were presented to the lesioned or intact visual\n    hemifield (pcluster % 0.01; Figure 3, right).\n  statistics:\n  - about: printed as pcluster at most 0.01\n    test: cluster-based permutation test, group main effect on network degree\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - psi-deltatheta-group-clusters\n  criterion: Network degree from STAR Methods, Graph Theory. On the Z-scored delta-theta PSI\n    (before baseline correction), a connection is true when |Z| > 1.96; degree per channel is\n    \"the weight of true directional connections\" to all other channels; then the temporal mean\n    of the baseline degree is subtracted. Readings for the degree (a) the sum of Z over true\n    connections leaving the channel (out-degree, signed); (b) the count of true connections\n    leaving the channel. Group cluster test with the shared methods on channels by time. Open\n    details O1, O4, O5. Reproduced when, under one reading and in both hemifields, a cluster\n    with p <= 0.01 lasting about 200 ms (two time steps) in the first half of active processing\n    shows patients below controls in degree from lesioned PFC, or in central-posterior\n    channels of both hemispheres; partially reproduced when it holds at p < 0.05 or in one\n    hemifield only.\n- id: psi-alphabeta-bottomup\n  statement: In alpha-beta (9 to 24 Hz) PSI, parieto-occipital regions lead PFC throughout\n    encoding, maintenance and active processing, for both visual hemifields.\n  source: Results, Task-Induced Directional Connectivity, paragraph 5; Figure 4A and 4B\n  quote: Parieto-occipital regions drove PFC throughout encoding, maintenance, and active\n    processing, regardless of whether stimuli were presented to the lesioned or intact visual\n    hemifield\n  statistics:\n  - test: PSI Z against frequency-shuffled null, baseline-corrected\n    statistic: Z < -1.96\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - power-lowtheta-interaction\n  criterion: PSI as in claim psi-deltatheta-bottomup-encoding, over 9 to 24 Hz. Open details O4,\n    O5, O6, O7. Reproduced when, under one reading, in both groups and both hemifields the\n    baseline-corrected Z from PFC to parieto-occipital channels is below -1.96 for most time\n    points of encoding-maintenance and of active processing; partially reproduced when it is\n    negative throughout but crosses -1.96 only in part.\n- id: psi-alphabeta-no-group-effect\n  statement: PFC lesions do not affect alpha-beta PSI at any point of encoding, maintenance or\n    active processing.\n  source: Results, Task-Induced Directional Connectivity, paragraph 5; Figure 4A and 4B\n  quote: PFC lesions did not affect alpha-beta PSI at any point during encoding, maintenance, or\n    active processing (group pcluster > 0.05).\n  statistics:\n  - test: cluster-based permutation test, group main effect\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - psi-deltatheta-group-clusters\n  criterion: A claim of absence, judged on the paper's test, the group cluster test of claim\n    psi-deltatheta-group-clusters on alpha-beta PSI, both segments and both hemifields, with\n    the same readings for clustering pairs. Reproduced when no cluster has p < 0.05; not\n    reproduced when one does. The smallest cluster p values and the group difference in the\n    PFC to parieto-occipital Z are reported either way.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/johnson-2017.yaml paper/10.1016-j.cub.2017.05.046.txt; grep -n "—\|rather" claims/johnson-2017.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/johnson-2017.yaml` with 22 claims. The quote checker found every quote in the text; its one flag is a value I checked by hand (below).

**Text read.** The version of record with its supplemental information: main text, figure legends 1 to 4, STAR Methods, Figures S1 to S4 legends and Tables S1 to S3. Nothing the claims need was missing. The PDF could not be rendered here (no pdftoppm or PyMuPDF), so I read no figure images. The data descriptor was read only to learn what the dataset holds.

**Code.** The paper says its MATLAB code is deposited with the data at CRCNS. According to the descriptor it sits in pfc-5's own `analysis_scripts` directory. Because it is one of the dataset's files I did not read it, and no commit is recorded. Every method in the file comes from the paper's text. The opening comment tells the author they may settle open details from those scripts.

**Counts.**
- **Quotes:** 21 of the 22 claims have one. `table-s1-patient-accuracy` is marked `inferred`, because its numbers appear only in Table S1.
- **Statistics:** 21 claims carry 33 statistical values.
- **Expected values:** 7 claims have them.
- **Criteria:** all 22 claims have one, and 8 of them are claims of absence judged on the paper's own test.
- **Coverage:** accuracy, ERP, baseline power, task-induced power, delta-theta and alpha-beta PSI, and network degree.

**Checker flag.** The checker could not find p = 5e-10 (`patients-above-chance`). Line 190 of the text prints it as "one-tailed p < 5 3 10�10", which is the extraction's garbling of 5 × 10⁻¹⁰, so the value is correct.

**Open details shared across claims (O1 to O7), with the readings named:**
- **O1, spatial neighbours for clustering:** FieldTrip's biosemi64 template, or triangulation.
- **O2, clustered dimensions:** channels by time by frequency, or channels by time on the band average.
- **O3, hemisphere index:** 27 lesioned-side indices, or 54 values (each channel minus its homolog).
- **O4, which 10 controls were swapped:** the deposited swap if there is one, or several random draws.
- **O5, surface Laplacian parameters:** FieldTrip spline defaults as the standard choice.
- **O6, the PFC region of interest for PSI:** the text gives no channel list. The readings are the anterior channels of the reproduced Figure 2 cluster, or AF7-F5-F7-FC5-FT7 from Figure S4. The parieto-occipital partners are read as P1-P3-P5-P7-P9-PO3-PO7-O1.
- **O7, how a thresholded Z is summarised:** the group mean crosses the threshold, or most subjects cross it.

**Open details in single claims:**
- **Mixed model:** a linear (Gaussian) model on the 204 cell accuracies or a binomial logit model; the paper calls it "logit" in the Results and "linear" in the Methods. Also condition coded as one number or as a three-level factor. The degrees of freedom in Table S3 fit 204 subject-by-hemifield-by-condition cells with a one-number condition term.
- **Accuracy means:** over all of a subject's trials, or the mean of its six cells.
- **Accuracy denominator:** trials after the eye-gaze exclusion, or trials kept after EEG cleaning.
- **Above-chance tests:** one test, one per hemifield, or one per hemifield and condition (suggested by "t1,13 > 15.43").
- **Variance F test:** on age, on education, or both.
- **Trial counts:** all trials kept, or correct trials only.
- **ERP zero-padding:** "7,500" has no unit (ms or samples), unlikely to matter.
- **Figure S4 hemifields:** pooled, or each separately.
- **Pair clustering for PSI:** over time per pair, or also over neighbouring pairs.
- **Network degree:** signed sum of Z over true connections, or a count.
- **Delta-theta PSI windows:** the lesioned/intact pairing of the stated time windows is my reading of the sentence.

**Missing from the paper.** No data a claim needed was absent. Two gaps come only from the figures I could not view: the channel list of the Figure 2 cluster, which is open detail O6, and the time courses of Figures 2 to 4, which the claims take from the text and legends instead.

**Tolerances.** Where the paper states a spread I used it, as the protocol says, so the means of accuracy, age and trial counts use the subjects' SDs. That makes some of these checks loose. For the per-patient values of Table S1 I set 0.02 instead of 10%, and the file gives the reason.

## End of run

16 turns, 5 minutes, $1.65 at API prices, result: success.
