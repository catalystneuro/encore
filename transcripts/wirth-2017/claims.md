# wirth-2017 · claims · run 42841815032

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; ls claims | head; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

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
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml
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
[... 301 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/datasets/wirth-2017.yaml; head -60 claims/jones-2021.yaml; grep -l "open" claims/*.yaml | head -3; grep -n "open\|reading" claims/jones-2021.yaml | head -20
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1371/journal.pbio.2001045
title: Gaze-informed, task-situated representation of space in primate hippocampus during virtual navigation
datasets:
- archive: crcns
  id: hc-21
  relation: primary
# Claims for Aery Jones, Rao, Zilberter, ..., Huang & Frank (2021), Cell Reports 37, 110159,
# tested on dandiset 000165.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol pilot-14 as stated in docs/protocol.md.
#
# Text read: the accepted author manuscript in PubMed Central (PMC9069800, NIHMS1795940), full
# text with STAR Methods and figure legends, and its main supplement PDF
# (NIHMS1795940-supplement-Main_supplement.pdf: Figures S1 to S7 and Tables S1 to S6), as
# stored under paper/. The version of record was not read. Supplementary Table S7 (an xlsx file,
# effects stratified by sex) is not under paper/ and was not read; only the claim
# sex-stratified-effects needs it.
#
[... 71 more lines not kept]
```

**Agent**

Now the paper.

**Agent calls Bash**

```bash
cd  cat paper/10.1371-journal.pbio.2001045.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pbio.2001045.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pbio.2001045.txt",
 "offset": 188
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  head -80 paper/hc-21.data-description.txt; grep -il "S1 Appendix\|not under paper" claims/*.yaml | head; grep -n "missing\|not read" docs/pilot-notes.md | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 80,192p paper/hc-21.data-description.txt; sed -n 295,315p docs/pilot-notes.md; git show d46830c7c6 --stat;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat papers/match/crcns-hc-21.yaml; ls papers/match | grep -i crcns | head -30; grep -rn "K0R49NQV" --include=*.yaml . | head
```

```
# Whether each paper CRCNS.org:hc-21 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: crcns
  id: hc-21
date: '2026-11-10'
papers:
- doi: 10.1371/journal.pbio.2001045
  relation: IsDescribedBy
  checks:
    text: true
    title_in_text: true
    names_this: false
    names_others: []
  verdict: primary
  by: checks
  reason: The archive says the paper describes the dataset, and the paper names no dataset.
crcns-ac-2.yaml
crcns-ac-4.yaml
crcns-ac-5.yaml
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
from scipy.stats import binom
def up(k,n,p): return binom.sf(k-1,n,p)
for (k,n) in [(12,111),(4,111),(20,56),(3,56),(1,42),(12,42),(14,111),(15,111),(29,111)]:
  print(k,n,[round(up(k,n,p),4) for p in (0.005,0.01,0.025,0.05)])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy.stats import binom
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
python3 -c "
from math import comb
def up(k,n,p): return sum(comb(n,i)*p**i*(1-p)**(n-i) for i in range(k,n+1))
for (k,n) in [(12,111),(4,111),(20,56),(3,56),(1,42),(12,42),(14,111),(15,111),(29,111),(12,111)]:
  print(k,n,[round(up(k,n,p),4) for p in (0.005,0.01,0.025,0.05)])
"
```

```
12 111 [0.0, 0.0, 0.0, 0.0097]
4 111 [0.0024, 0.0258, 0.3019, 0.8111]
20 56 [0.0, 0.0, 0.0, 0.0]
3 56 [0.0028, 0.0187, 0.1646, 0.5354]
1 42 [0.1898, 0.3443, 0.6547, 0.884]
12 42 [0.0, 0.0, 0.0, 0.0]
14 111 [0.0, 0.0, 0.0, 0.0013]
15 111 [0.0, 0.0, 0.0, 0.0004]
29 111 [0.0, 0.0, 0.0, 0.0]
12 111 [0.0, 0.0, 0.0, 0.0097]
```

**Agent calls Write**

```json
{
 "file_path": "claims/wirth-2017.yaml",
 "content": "# Claims for Wirth, Baraduc, Plante, Pinede & Duhamel (2017), PLoS Biology 15(2), e2001045,\n# tested on CRCNS hc-21.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read: the version of record (PMC5328243, open access), full text from Europe PMC JATS\n# XML as stored under paper/: Results, Discussion, Materials and Methods, the figure legends of\n# Figs 1 to 7 and the legends of S1 to S7 Figs. The supplementary text files S1 Appendix\n# (sections A1 to A5: point-of-gaze density maps, gaze before joystick actions, recording\n# methods and cell selection, population averages, the control for space dimensionality) and\n# S2 Appendix (description of the CRCNS files and scripts) are DOCX files that are not under\n# paper/ and were not read. The claims that rest on them say so (gaze-anticipates-action,\n# gaze-anticipates-landmarks, dimensionality-control, fields-per-cell). No PDF was read; the\n# reference list is absent from the stored text, so reference 60 (the learning curve method)\n# is not named.\n#\n# Code: the paper links no repository. It says some Matlab scripts are hosted with the data on\n# CRCNS (Supporting data; S2 Appendix). These are files of the dataset and were not read. No\n# criterion below takes a method from code.\n#\n# Data the paper used (Results; Materials and Methods). Two rhesus macaques, monkey S and\n# monkey K, navigating with a joystick a virtual 3-D star maze of five arms (radius 16 m,\n# speed 5 m/s) with five landmarks placed between the arms at twice the arm length, projected\n# in stereo on a 152 x 114 cm screen at 101 cm, 70 degree horizontal field of view. The reward\n# is at the end of one arm (by convention north, between the two landmarks neighboring it).\n# Each day a new landmark layout; sessions of 80 (plus or minus 5) trials. A trial starts at an\n# arm end, the animal moves to the center, rotates (72 degrees facing a path, 36 degrees facing\n# a landmark), enters an arm, is rewarded at its end if correct, and is relocated passively to\n# a random new start along a path outside the arms (\"return paths\"). Probe sessions (9 for S,\n# 15 for K) started from one or two eastern entries, with the western entries introduced later.\n# Binocular eye tracking (ASL) gives the point of gaze. 270 cells recorded in the right\n# hippocampus (128 S, 142 K), sites in CA3 (99), CA1 (101) and dentate gyrus (8); 189 cells\n# with more than 100 spikes per session are analysed, on successful trials only. Measured\n# variables are spike times, virtual position and head (camera) direction, eye position, task\n# events, and the state-space coordinates.\n#\n# The archive's descriptor (paper/hc-21.data-description.txt, read for this alone) describes\n# 101 cells from the two monkeys (files \"sn\" for monkey 1, Snorre, and \"ke\" for monkey 2,\n# Kevin), each file with a familiar maze (\"famallo\") and a daily new maze (\"newallo\"), and the\n# state-space coordinates and transition tags. The paper describes only daily new layouts and\n# names no familiar maze. The figure legends give the underlying data as doi 10.6080/K0R49NQV,\n# while the descriptor asks that hc-21 be cited as doi 10.6080/K0GX48R9. Whether hc-21 holds\n# the paper's cells, and which ones, is the author's to find.\n#\n# Method shared by the claims (every claim that says \"Method W\"). Each part is cited.\n#  - Trials. Only successful trials (Results, What is encoded, paragraph 1). Whether the\n#    passive return following a correct trial belongs to it is open; the paper analyses return\n#    paths (Results, Direction selectivity) and the state space includes them (Fig 1F legend).\n#    Readings (a) from trial start to the end of the following return; (b) from trial start to\n#    reward, return paths taken from the returns that follow correct trials. A deviation.\n#  - Cells. The 189 cells with more than 100 spikes per session; responsive cells are those\n#    with significant IC (p < 0.01) in at least one of the four spaces (Results, Sensitivity\n#    of the cells, paragraph 2).\n#  - Spaces. Position (virtual X, Y), direction (virtual head direction), point of gaze\n#    (Methods, Mapping the animal's point of gaze), and state space (Fig 1F; Results, What is\n#    encoded, paragraph 2). Point of gaze combines horizontal and vertical eye position with\n#    virtual position and camera orientation; points beyond the landmark wall, or above the\n#    horizon, are put on a vertical cylinder through the landmark centroids, flattened into an\n#    annulus (Methods; Fig 1G legend). Open: which eye (left, right, or the mean of both), the\n#    eye units and calibration, the virtual eye height and the vertical field of view. A\n#    deviation; the readings are the three eye choices.\n#  - Maps. Rate per bin is spikes over time in the bin, unsmoothed for comparisons; bins kept\n#    with at least four successful trials (Methods, Activity maps) and, for IC, more than\n#    400 ms of time in successful trials (Methods, Information Content). The resolution of each\n#    map is adjusted so that the number of valid bins is as close to 200 as possible (Methods,\n#    Information Content). How the resolution is stepped in each space is open; a standard\n#    choice (square grid for position and gaze, equal angular bins for direction, equal\n#    lengths along graph edges for the state space), stated as a deviation.\n#  - IC is Skaggs information in bits per spike, sparsity is (M - (sum rate)^2 / sum rate^2) /\n#    (M - 1) over M bins (Methods, Information Content; Sparsity index). Normalized indexes\n#    subtract the mean of the 999 surrogate values (Methods; Results, Hippocampal cells encode,\n#    paragraph 1).\n#  - Surrogates. 999 surrogate spike sets from 5 s chunks of recording time randomly shifted;\n#    p is the rank of the actual value among the 1,000, bilateral (Methods, Permutation\n#    statistics). How chunks are shifted is open; readings (a) the order of the chunks is\n#    permuted (Results, \"randomly shuffling periods of spiking activity in time\"); (b) each\n#    chunk is displaced by an independent random time shift. The bilateral p is taken as twice\n#    the smaller tail rank fraction, a standard choice.\n#  - Binomial tests of a count of significant cells against chance. The chance rate is not\n#    stated. Readings (a) 0.05; (b) 0.025, one tail of a bilateral 0.05 test. From the paper's\n#    own numbers, 12 and 4 of 111 (state-space selectivity, p = 0.01 and p = 0.81) match (a);\n#    3 of 56 (direction correlation, p = 0.16) matches (b). Each claim names the reading its\n#    numbers fit.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: hc-21\npaper: doi:10.1371/journal.pbio.2001045\nclaims:\n- id: gaze-anticipates-action\n  statement: During the 500 ms before each joystick action, gaze anticipated the direction of the\n    subsequent movement.\n  source: Results, Animals use direction and compute trajectory, paragraph 2; S1 Fig and S2 Fig\n    (S2A and S2B legend)\n  quote: During the 500 ms before each action on the joystick ( Fig 1D , S1 Fig , S2 Fig , and S1\n    Appendix A2), gaze anticipated the direction of the subsequent movement (Wilcoxon test, p <\n    0.001\n  statistics:\n  - test: Wilcoxon test\n    p: 0.001\n    p_relation: \"<\"\n  criterion: The analysis is described in S1 Appendix A2, which was not read. The paper's text\n    and the S2 Fig legend disagree on the window, 500 ms (Results) or 300 ms (S2A legend). Per\n    monkey, the mean horizontal eye position in the window before each left or right joystick\n    move (event codes for rotation), with Method W's trials. Readings (a) 500 ms; (b) 300 ms;\n    the Wilcoxon test is read as a rank-sum test of eye positions before right against before\n    left turns (the distributions of S2A). Reproduced when, under one reading, eye position\n    before right turns lies to the right of that before left turns, with p < 0.001, in each\n    monkey.\n- id: gaze-anticipates-landmarks\n  statement: When relocated to a new entry, the monkeys gazed proactively at the location where\n    the landmarks would appear.\n  source: Results, Animals use direction and compute trajectory, paragraph 2; S2C Fig\n  quote: Similarly, when being relocated to a new entry, monkeys proactively gazed at the location\n    at which the landmarks would appear (see S2 Fig and S1 Appendix A2) (Wilcoxon test, p < 0.001)\n  statistics:\n  - test: Wilcoxon test\n    p: 0.001\n    p_relation: \"<\"\n  criterion: The analysis is in S1 Appendix A2, which was not read; the S2C legend shows the mean\n    horizontal eye position during passive returns toward the right against toward the left.\n    Per monkey, mean horizontal eye position during returns turning right against left, by a\n    Wilcoxon rank-sum test. Reproduced when eye position lies toward the side of the turn with\n    p < 0.001 in each monkey. The test the paper ran is not fully specified, a deviation.\n- id: learning-trials\n  statement: Both monkeys learned the rewarded arm in about a dozen trials; monkey S performed\n    above chance after 12.3 plus or minus 2 trials (SEM) and monkey K after 14.8 plus or minus 2.4.\n  source: Results, Animals use direction and compute trajectory, paragraph 3; S3A and S3B Fig\n  quote: monkey S performed above chance after 12.3 ± 2 trials (SEM), and monkey K did so after 14.8\n    ± 2.4 trials\n  expected:\n  - quantity: monkey S, mean trials to above-chance performance\n    value: 12.3\n    tolerance: 2\n  - quantity: monkey K, mean trials to above-chance performance\n    value: 14.8\n    tolerance: 2.4\n  criterion: Per session, the first trial at which the lower confidence bound of the probability\n    of a correct response exceeds 1/4 (S3B legend; the reward is never at the end of the entry\n    arm). The bounds come from the method of the paper's reference 60, which the stored text\n    does not name; the descriptor says each file holds learning curves with bounds, which may be\n    used, the curves recomputed otherwise being a variant. Which sessions enter is open;\n    readings (a) all sessions of the monkey; (b) the sessions that are not probe sessions.\n    Tolerances are the paper's SEM. Reproduced when both means fall within tolerance under one\n    reading.\n- id: learning-to-90\n  statement: From above-chance performance to the upper confidence bound of success reaching 90%,\n    fewer than 10 trials were usually needed (89% of sessions).\n  source: Results, Animals use direction and compute trajectory, paragraph 3\n  quote: From then to when the upper confidence bound of success reached 90%, less than 10 trials\n    were usually necessary (89% of sessions).\n  expected:\n  - quantity: fraction of sessions with fewer than 10 trials from above chance to upper bound 90%\n    value: 0.89\n    tolerance: 0.089\n  criterion: With the learning curves of learning-trials, per session the number of trials from\n    the first trial with lower bound above 1/4 to the first with upper bound at or above 0.9;\n    the fraction of sessions where it is below 10, both monkeys pooled. Sessions as in the\n    readings of learning-trials.\n  depends_on:\n  - learning-trials\n- id: probe-transfer\n  statement: In probe sessions, performance after the new western entries were introduced was\n    higher than at the start of the session (monkey K 73% against 44%, monkey S 80% against 55%).\n  source: Results, Animals use direction and compute trajectory, paragraph 4; S3C Fig and legend\n  quote: Monkey K was 73% correct after introducing the new entries versus 44% correct at beginning\n    of the sessions; monkey S was 80% versus 55% correct ( S3C Fig , Wilcoxon, p = 0.01).\n  statistics:\n  - test: Wilcoxon\n    p: 0.01\n    n: 9 probe sessions for monkey S and 15 for monkey K\n  expected:\n  - quantity: monkey K, percent correct after new entries\n    value: 73\n    tolerance: 7.3\n    unit: percent\n  - quantity: monkey K, percent correct at beginning of session\n    value: 44\n    tolerance: 4.4\n    unit: percent\n  - quantity: monkey S, percent correct after new entries\n    value: 80\n    tolerance: 8\n    unit: percent\n  - quantity: monkey S, percent correct at beginning of session\n    value: 55\n    tolerance: 5.5\n    unit: percent\n  criterion: Probe sessions are those that start from one or two entries (northeastern and\n    southeastern) and later add the others (Results; S3C legend). Per session, percent correct\n    over the 5 trials after the new entries are introduced and over the first 5 trials of the\n    session (S3C legend). The test is a Wilcoxon signed-rank on paired session values; whether\n    the two monkeys are pooled is open (the legend says \"for both monkeys\"); readings (a) the 24\n    sessions pooled; (b) each monkey separately. Reproduced when the four means are within\n    tolerance and, under one reading, the test gives p < 0.05 with performance higher after\n    the new entries.\n- id: probe-faster-criterion\n  statement: In probe sessions, performance above the learning criterion was reached faster\n    after the new entries (within 4 trials for monkey K and 2.7 for monkey S, against 14.8 and\n    12.3).\n  source: Results, Animals use direction and compute trajectory, paragraph 4\n  quote: Further, performances above the learning criterion were reached significantly faster\n    (within 4 trials for monkey K and within 2.7 trials for monkey S, compared to 14.8 and 12.3\n    trials; Wilcoxon, p = 0.002).\n  statistics:\n  - test: Wilcoxon\n    p: 0.002\n  expected:\n  - quantity: monkey K, trials to criterion after new entries\n    value: 4\n    tolerance: 0.4\n  - quantity: monkey S, trials to criterion after new entries\n    value: 2.7\n    tolerance: 0.27\n  depends_on:\n  - learning-trials\n  - probe-transfer\n  criterion: How trials to criterion after the new entries are counted is not stated. Readings\n    (a) trials from the introduction of the new entries until the lower confidence bound again\n    exceeds 1/4, on the session's learning curve; (b) trials from the introduction until the\n    first correct trial from a new entry. Compared with the session's trials to criterion of\n    learning-trials by a Wilcoxon test (signed-rank for paired sessions; rank-sum against all\n    sessions as a variant). Reproduced when, under one reading, both means are within\n    tolerance and the test gives p < 0.05 with fewer trials after the new entries.\n- id: cells-recorded\n  statement: Of 270 cells recorded in the right hippocampus (128 in monkey S, 142 in monkey K), 189\n    fired more than 100 spikes per session and were analysed.\n  source: Results, What is encoded in hippocampal cell activity, paragraph 1; Methods,\n    Electrophysiological recordings\n  quote: Of the 270 cells recorded in the full extent of the right hippocampus (128 cells in monkey\n    S, 142 in monkey K; S4 Fig ), we focused on 189 cells that fired more than 100 spikes per\n    session\n  expected:\n  - quantity: cells recorded\n    value: 270\n    tolerance: 27\n  - quantity: cells with more than 100 spikes per session\n    value: 189\n    tolerance: 18.9\n  criterion: Counts of cells, per monkey and in total, and of cells with more than 100 spikes in\n    the session (the new maze session, as the paper describes only new layouts). The site\n    counts of the Methods (CA3 99, CA1 101, dentate gyrus 8) sum to 208, which matches neither\n    count, and are reported from the recording locations for comparison only. The full cell\n    selection is in S1 Appendix A3, not read.\n- id: responsive-cells\n  statement: 111 of the 189 cells (59%) had significant information content in at least one of\n    the four coding spaces.\n  source: Results, Sensitivity of the cells to a combination of variables, paragraph 2; Fig 3A\n  quote: Significant IC ( p < 0.01) was present in at least one of the spaces for 111 out of the\n    189 cells (59%, responsive cells).\n  expected:\n  - quantity: responsive cells\n    value: 111\n    tolerance: 11.1\n  - quantity: fraction of analysed cells responsive\n    value: 0.59\n    tolerance: 0.059\n  criterion: Method W. For each cell and each space, normalized IC and its surrogate p-value; a\n    cell is responsive when p < 0.01 in at least one space. Every reading of Method W is run.\n    Reproduced when the count and fraction are within tolerance under one reading.\n  depends_on:\n  - cells-recorded\n- id: state-space-most-responsive\n  statement: The proportions of cells responsive to each space were unequal; the state space\n    accounted for the most cells (84), and more cells were responsive to state space than to\n    point of gaze.\n  source: Results, Sensitivity of the cells to a combination of variables, paragraph 2; Fig 3A\n  quote: The proportion of cells responsive to each space was significantly unequal (chi-squared\n    test, p = 0.014). The state space accounted for the largest number (84 cells, Fig 3A ), and\n    pitting state space against the other three, there were more cells responsive to state space\n    than to point of gaze (chi-squared test, p = 0.012, Bonferroni corrected\n  statistics:\n  - about: proportions across the four spaces\n    test: chi-squared test\n    p: 0.014\n  - about: state space against point of gaze\n    test: chi-squared test\n    p: 0.012\n    corrected: Bonferroni\n  expected:\n  - quantity: cells with significant IC in state space\n    value: 84\n    tolerance: 8.4\n  depends_on:\n  - responsive-cells\n  criterion: Method W. Per space, the number of the 189 cells with IC p < 0.01. The chi-squared\n    test's layout is not stated; readings (a) a 4 x 2 contingency test of responsive and not\n    responsive counts across the four spaces, over the 189 cells; (b) the same over the 111\n    responsive cells; the pairwise tests are the 2 x 2 tables of state space against each other\n    space, Bonferroni over three. Reproduced when the state-space count is within tolerance and\n    the largest, and under one reading the overall test gives p < 0.05 and state space against\n    point of gaze gives a corrected p < 0.05 with more state-space cells. The other pairwise\n    comparisons were not significant in the paper; their p-values are reported.\n- id: multi-space-coding\n  statement: Sensitivity to the four variables was not mutually exclusive; most responsive cells\n    carried significant activity in more than one coding space.\n  source: Results, Sensitivity of the cells to a combination of variables, paragraph 2; Fig 3B\n    legend\n  quote: Most responsive cells carry significant activity in more than one coding space.\n  depends_on:\n  - responsive-cells\n  criterion: Method W. Among responsive cells, the number with significant IC (p < 0.01) in two or\n    more spaces. Reproduced when it exceeds half of the responsive cells.\n- id: direction-center-vs-periphery\n  statement: For direction-selective cells, both information per spike and sparsity of\n    directional firing were higher in the maze center than on the peripheral return paths.\n  source: Results, Direction selectivity, paragraph 1; Fig 3C\n  quote: Both IC and sparsity measures were significantly higher in the center, which is the choice\n    point, when compared to return tracks (both p < 0.001).\n  statistics:\n  - about: IC, center against return paths\n    p: 0.001\n    p_relation: \"<\"\n  - about: sparsity, center against return paths\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Method W. Directional maps of each cell from time in the maze center and from time on\n    return paths. Which cells enter is open; readings (a) cells with significant direction IC;\n    (b) all responsive cells (Fig 3C legend, \"the responsive cells\"). The test is not named;\n    it is taken as a Wilcoxon signed-rank test across cells of the paired normalized values, the\n    test the Results use for the comparisons of Fig 3D to 3F. Reproduced when, under one\n    reading, IC and sparsity are both higher in the center with p < 0.001; partially reproduced\n    when both are higher at p < 0.05 or one at p < 0.001.\n- id: direction-tuning-not-maintained\n  statement: Direction tuning was not maintained across positions; the correlation between\n    directional tuning in the center and on return paths was significantly low in 20 of 56 cells\n    (36%), more than chance, and significantly high in only 3, consistent with chance.\n  source: Results, Direction selectivity, paragraph 1; Fig 3C inset\n  quote: \"the correlation between direction selectivity in the center and in the return paths was\n    significantly lower in 20 out of 56 cells (inset in Fig 3C , blue bars). This represents 36% of\n    the population and is higher than what is expected by chance ( p < 0.001, binomial test; note\n    that correlation was only significantly higher in 3 cells, consistent with chance: p = 0.16,\n    binomial test)\"\n  statistics:\n  - about: cells with significantly low correlation\n    test: binomial test\n    p: 0.001\n    p_relation: \"<\"\n    n: 20 of 56 cells\n  - about: cells with significantly high correlation\n    test: binomial test\n    p: 0.16\n    n: 3 of 56 cells\n  expected:\n  - quantity: cells with significantly low center-periphery correlation\n    value: 20\n    tolerance: 2\n  - quantity: cells tested\n    value: 56\n    tolerance: 5.6\n  - quantity: cells with significantly high correlation\n    value: 3\n    tolerance: 0.3\n  criterion: Method W. Per cell, the uncentered correlation of center and return-path directional\n    rates over the directional bins valid in both (Methods, Directional correlations); its\n    significance from the surrogates, bilateral, at 0.05 per test with 0.025 per tail as the\n    binomial chance rate (reading (b) of Method W, the one that gives p = 0.16 for 3 of 56).\n    The 56 cells are read as the cells of direction-center-vs-periphery with enough common\n    valid bins; the cell readings of that claim apply. Reproduced when, under one reading, the\n    counts are within tolerance (the high count within 2 to 4, as a count of 3 cannot carry a\n    10% tolerance) and the low count passes the binomial test at p < 0.001.\n  depends_on:\n  - direction-center-vs-periphery\n- id: state-space-ic-higher\n  statement: Spike information content was systematically higher in state space than in position,\n    direction or point-of-gaze space, for cells responsive in both spaces compared.\n  source: Results, Hippocampal cells encode a fine-grained state-space representation, paragraph\n    1; Fig 3D to 3F\n  quote: The spike information content for the state space was systematically higher when compared\n    to position, direction, or gaze space (Wilcoxon, all p < 0.01).\n  statistics:\n  - test: Wilcoxon\n    p: 0.01\n    p_relation: \"<\"\n  criterion: Method W. For each other space, the cells responsive in both it and state space;\n    per cell the normalized state-space IC minus the normalized IC in the other space; a\n    Wilcoxon signed-rank test across cells. Reproduced when all three differences are positive\n    with p < 0.01; partially reproduced for two of three.\n  depends_on:\n  - responsive-cells\n- id: sparsity-state-vs-direction\n  statement: Sparsity was significantly higher in state space than in direction space.\n  source: Results, Hippocampal cells encode a fine-grained state-space representation, paragraph\n    1; Fig 3E\n  quote: Sparsity was significantly higher (Wilcoxon test) in state space compared to direction\n    space ( p = 0.006)\n  statistics:\n  - test: Wilcoxon test\n    p: 0.006\n  criterion: Method W, as in state-space-ic-higher with normalized sparsity. Reproduced when the\n    median difference is positive with p < 0.05.\n  depends_on:\n  - responsive-cells\n- id: sparsity-state-vs-position\n  statement: Sparsity was not significantly higher in state space than in position space overall,\n    but the 15 cells whose difference was individually significant were sparser in state space.\n  source: Results, Hippocampal cells encode a fine-grained state-space representation, paragraph\n    1; Fig 3D\n  quote: but not significantly higher compared to position space ( p = 0.19), although the 15 cells\n    for which the difference was individually significant (as assessed with permutation tests on\n    surrogate data) were sparser in state space ( p = 0.001)\n  statistics:\n  - about: all cells responsive in both spaces\n    test: Wilcoxon test\n    p: 0.19\n  - about: the 15 cells with an individually significant difference\n    test: Wilcoxon test\n    p: 0.001\n    n: 15 cells\n  expected:\n  - quantity: cells with individually significant sparsity difference\n    value: 15\n    tolerance: 1.5\n  criterion: Method W, as in state-space-ic-higher with normalized sparsity. The overall part is\n    a claim of absence, judged on the paper's Wilcoxon signed-rank test at p < 0.05; the effect\n    size is reported. Per cell, the difference is significant when its surrogate p (the\n    difference recomputed on each surrogate) is below 0.05, bilateral. Reproduced when the\n    overall test is not significant, the count is within tolerance, and those cells' signed-rank\n    test gives p < 0.05 with state space sparser.\n  depends_on:\n  - responsive-cells\n- id: sparsity-gaze-vs-state\n  statement: Sparsity was higher overall in point-of-gaze space than in state space, an effect\n    not confirmed among the 18 cells whose difference was individually significant.\n  source: Results, Hippocampal cells encode a fine-grained state-space representation, paragraph\n    1; Fig 3F\n  quote: Conversely, sparsity was significantly higher overall in gaze space than in state space (\n    p < 0.001), but this effect could not be confirmed when considering only 18 cells for which the\n    difference was individually significant ( p = 0.68).\n  statistics:\n  - about: all cells responsive in both spaces\n    test: Wilcoxon test\n    p: 0.001\n    p_relation: \"<\"\n  - about: the 18 cells with an individually significant difference\n    test: Wilcoxon test\n    p: 0.68\n    n: 18 cells\n  expected:\n  - quantity: cells with individually significant sparsity difference\n    value: 18\n    tolerance: 1.8\n  criterion: Method W, with the per-cell significance of sparsity-state-vs-position. Reproduced\n    when the overall signed-rank test gives p < 0.001 with gaze sparser, the count is within\n    tolerance, and the test on those cells is not significant at p < 0.05 (the absence part,\n    judged on the paper's test).\n  depends_on:\n  - responsive-cells\n- id: state-space-selectivity\n  statement: In the maze center, at the same position and direction, 12 of 111 responsive cells\n    (11%) showed significantly high state-space selectivity, discriminating the current\n    rotational move, more than chance; only 4 showed significantly low selectivity, as expected\n    by chance.\n  source: Results, Cells discriminate different contexts for the same position and direction,\n    paragraph 1; Fig 4B\n  quote: Only 4 cells showed significantly low state-space selectivity, as expected by chance ( p =\n    0.81, binomial test), but 12 cells out of 111 (11%, p = 0.01, binomial test) showed\n    significantly high state-space selectivity\n  statistics:\n  - about: cells with significantly high selectivity\n    test: binomial test\n    p: 0.01\n    n: 12 of 111 responsive cells\n  - about: cells with significantly low selectivity\n    test: binomial test\n    p: 0.81\n    n: 4 of 111 responsive cells\n  expected:\n  - quantity: cells with significantly high state-space selectivity\n    value: 12\n    tolerance: 1.2\n  - quantity: cells with significantly low state-space selectivity\n    value: 4\n    tolerance: 0.4\n  criterion: Method W. Time in the maze center only; per 3.6 degree head-direction bin, firing\n    rates in each of the three rotational moves, keeping bins with at least 400 ms in each of at\n    least two move types; SSI = sum over bins of (max - min) over sum of (max + min), centered\n    by the surrogate mean; significance from the surrogates (Methods, State-space selectivity).\n    The rotational moves are taken from the state-space transition tags. Binomial chance rate\n    0.05 (reading (a) of Method W, which gives the paper's p = 0.01 and 0.81). Reproduced when\n    the high count is within tolerance (or 11 to 13) and passes the binomial test at p < 0.05,\n    and the low count (3 to 5) does not.\n  depends_on:\n  - responsive-cells\n- id: landmark-identity-distance\n  statement: A two-way ANOVA of firing on the entry paths by landmark viewed and relative distance\n    gave a main effect of landmark identity in 30 of 111 responsive cells and of relative distance\n    in 64; 29 cells coded a combination (14 with a significant interaction, 15 with both main\n    effects), more than chance.\n  source: Results, Cells encode landmark identity and distance with respect to landmark, paragraph\n    1; Fig 5\n  quote: A two-way ANOVA revealed a main effect of landmark identity (30 cells out of 111\n    responsive cells) and relative distance (64 cells out of 111 responsive cells).\n  statistics:\n  - about: cells with a significant interaction (14) or both factors (15)\n    test: binomial test\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: cells with a main effect of landmark identity\n    value: 30\n    tolerance: 3\n  - quantity: cells with a main effect of relative distance\n    value: 64\n    tolerance: 6.4\n  - quantity: cells with a significant interaction\n    value: 14\n    tolerance: 1.4\n  - quantity: cells with both main effects significant\n    value: 15\n    tolerance: 1.5\n  criterion: Per responsive cell, firing rate per lap in each of four equal segments of each of\n    the four entry paths facing a landmark, RD1 16 to 12 m, RD2 12 to 8 m, RD3 8 to 4 m, RD4 4\n    to 0 m from the center (Methods, ANOVA for landmark identity and relative distance); a 4 x 4\n    two-way ANOVA with interaction, at alpha 0.05 (not stated; the standard level, and the one\n    matching the binomial reading (a) of the one-way count). Whether \"both factors significant\"\n    excludes cells with an interaction is open; readings (a) both main effects and no\n    interaction; (b) both main effects regardless. Reproduced when all four counts are within\n    tolerance under one reading; partially reproduced when the identity and distance counts are.\n    Fig 5 reports F(9,756), the interaction degrees of freedom, for two example cells recorded\n    together (F = 4.4076, p < 0.001 and F = 2.1243, p = 0.025); the cells are not identified,\n    and the session's cells whose interaction tests come nearest are reported.\n  depends_on:\n  - responsive-cells\n- id: landmark-identity-center\n  statement: The main effect of landmark identity was confirmed by a one-way ANOVA on firing to\n    the four landmark views at the center, significant in 12 of 111 responsive cells, more than\n    chance.\n  source: Results, Cells encode landmark identity and distance with respect to landmark, paragraph\n    1\n  quote: The main effect of landmark identity was confirmed by a one-way ANOVA on the activity to\n    the four landmark views at the center only (12 cells out of 111 responsive cells, which is a\n    higher proportion than expected by chance; p = 0.01, binomial test).\n  statistics:\n  - test: binomial test\n    p: 0.01\n    n: 12 of 111 responsive cells\n  expected:\n  - quantity: cells with a significant one-way landmark effect at the center\n    value: 12\n    tolerance: 1.2\n  criterion: Per responsive cell, firing rate in the maze center while facing each of the four\n    landmarks (head direction toward the landmark, one value per visit); one-way ANOVA at alpha\n    0.05, binomial chance rate 0.05 (reading (a) of Method W, which gives p = 0.01 for 12 of\n    111). How a view is delimited is open; readings (a) time with the landmark straight ahead\n    within the 3.6 degree bin of state-space-selectivity; (b) the whole rotation step facing\n    the landmark (the 36 degree rotation tags). Reproduced when, under one reading, the count is\n    within tolerance (11 to 13) and passes the binomial test at p < 0.05.\n  depends_on:\n  - responsive-cells\n- id: path-selectivity\n  statement: Of 42 cells responding to the appearance of a landmark neighboring the reward, only\n    one was significantly path invariant, while 12 (29%) discriminated significantly between\n    viewpoints of the same landmark; the distribution of indices differed from the surrogates.\n  source: Results, Landmark-triggered activity and viewpoint dependence, paragraph 2; Fig 6D\n  quote: We found that only one landmark-responsive cell was significantly path invariant ( Fig 6B ,\n    corresponding to cell 1 in Fig 2 , 5% of the 42 cells, p = 0.37, binomial test), whereas 12/42\n    cells (29%, p < 0.001, binomial test) discriminated significantly amongst different viewpoints\n    of the same landmark\n  statistics:\n  - about: path-invariant cells\n    test: binomial test\n    p: 0.37\n    n: 1 of 42 cells\n  - about: viewpoint-dependent cells\n    test: binomial test\n    p: 0.001\n    p_relation: \"<\"\n    n: 12 of 42 cells\n  - about: actual against surrogate index distributions\n    test: Kolmogorov-Smirnov test\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: landmark-responsive cells analysed\n    value: 42\n    tolerance: 4.2\n  - quantity: viewpoint-dependent cells\n    value: 12\n    tolerance: 1.2\n  criterion: For the northwestern and northeastern landmarks, the five trajectories on which the\n    landmark enters the field of view; rate from -400 to 500 ms around entry at 10 ms\n    resolution. A cell enters when it has significant point-of-gaze IC and the evoked rate\n    exceeds the 400 ms baseline mean plus 2.5 SD (Methods, Path selectivity index; Results).\n    Index S = (N - sum of rates over max rate) / (N - 1), N = 5, on the mean rate of the 500 ms\n    window, for the most informative landmark; significance from the surrogates (Method W).\n    Open, each a deviation, (1) the start of the 500 ms window, (a) 120 ms after entry\n    (Results) or (b) at entry (Methods); (2) entry into the field of view, (a) the landmark\n    centroid within the 70 degree horizontal field or (b) any part of it; (3) \"most\n    informative landmark\", (a) the higher index or (b) the stronger evoked response; (4) how\n    the evoked rate is compared with the threshold, (a) the peak of the 10 ms rate in 0 to\n    500 ms or (b) its mean. Binomial chance rate 0.05 or 0.025 (Method W); neither gives the\n    paper's p = 0.37 for one cell, which is reported, not judged. Reproduced when, under one\n    reading, the counts of 42 and 12 are within tolerance, 12 passes the binomial test at\n    p < 0.001, and the Kolmogorov-Smirnov test gives p < 0.001.\n  depends_on:\n  - responsive-cells\n- id: gaze-aligned-dynamics\n  statement: Aligned on first foveation of the best-driving landmark, mean activity rose until\n    the saccade to the landmark and peaked shortly after.\n  source: Results, Visual exploration and hippocampal activity dynamics, paragraph 1; Fig 7E\n  quote: Gaze-aligned activity significantly rose until the saccade to the landmark and peaked\n    shortly after.\n  criterion: Per cell, the best-driving landmark (maximal activity; Methods, Latencies); foveation\n    is gaze within plus or minus 10 degrees of the landmark in azimuth and elevation for more\n    than 100 ms (Methods, Landmark foveation). Population mean rate aligned on the first\n    foveation after the landmark appears. Which cells enter is open; readings (a) the responsive\n    cells; (b) the 42 landmark-responsive cells of path-selectivity. No test or window is named\n    for the rise; it is judged by a Wilcoxon signed-rank test across cells of the rate in the\n    100 ms before foveation against the rate at -500 to -150 ms (the baseline of Methods,\n    Latencies), and the peak of the mean must fall after 0 and within the 500 ms post-foveation\n    window the paper uses (Results, paragraph 3). Reproduced when, under one reading, both hold\n    with p < 0.05. The test is not the paper's, a deviation.\n  depends_on:\n  - responsive-cells\n- id: latency-skew\n  statement: Response latencies to the best landmark are left skewed when aligned on gaze and\n    right skewed when aligned on landmark onset, and some cells respond before the landmark\n    enters the field of view.\n  source: Results, Visual exploration and hippocampal activity dynamics, paragraph 1; Fig 7F\n  quote: The distribution of the latencies of the responses to the best landmark are left skewed\n    when aligned on gaze and right skewed when aligned on landmark onset ( Fig 7F , see Materials\n    and Methods ). For a small but nonnegligible proportion of cells, the response latency even\n    preceded the landmark's entry in the FOV\n  criterion: Per cell, latency to its best landmark as the first time after alignment when the rate\n    exceeds the mean of the -500 to -150 ms baseline plus 2.5 SD for 100 consecutive ms\n    (Methods, Latencies), aligned on onset and on foveation. How a latency before entry is found\n    when the search starts after onset is open; readings (a) the search starts at the end of\n    the baseline (-150 ms); (b) at alignment, with no negative latencies (then the last part of\n    the claim cannot hold). Cells as in gaze-aligned-dynamics. Reproduced when, under one\n    reading, the sample skewness is negative for gaze-aligned and positive for onset-aligned\n    latencies, and some onset-aligned latencies are negative.\n  depends_on:\n  - gaze-aligned-dynamics\n- id: eccentricity-modulation\n  statement: Activity was modulated by the eccentricity of the best-driving landmark, more so just\n    after the landmark appeared, and cells could fire for a landmark not yet visible.\n  source: Results, Visual exploration and hippocampal activity dynamics, paragraph 1; Fig 7G and\n    legend\n  quote: Overall, cells showed a modulation of their activity by landmark eccentricity ( Fig 7G ,\n    blue line). This modulation was increased by the recent appearance of the landmark (red line).\n  criterion: Population mean rate against eccentricity of the best-driving landmark in four sets\n    of epochs, (1) 500 ms after appearance, (2) 500 ms before appearance with eccentricity as\n    in a 180 x 180 degree field, (3) after the landmark has been visible 1,000 ms or more, (4)\n    all data (Results). The eccentricity bins are not given; 10 degree bins, a standard choice.\n    Reproduced when rate decreases with eccentricity in set 4 (Spearman correlation of bin means\n    below 0), the range of bin means is larger in set 1 than in set 4, and set 2 lies above the\n    mean firing rate in its lowest-eccentricity bin. The comparisons are read from the figure's\n    description, no test being reported, a deviation.\n  depends_on:\n  - gaze-aligned-dynamics\n- id: foveation-selectivity\n  statement: Landmark selectivity was significantly enhanced when the landmark was foveated\n    compared with appearing in the visual periphery, while path selectivity was only moderately\n    improved by direct gaze.\n  source: Results, Visual exploration and hippocampal activity dynamics, paragraph 2; Fig 7H and\n    7I (the Results cite them as Fig 7G and 7H)\n  quote: Landmark selectivity was significantly enhanced if the landmark was foveated compared to\n    appearing in the visual periphery (one-sided logit-Wilcoxon, p < 0.001, Fig 7G ).\n  statistics:\n  - about: landmark selectivity, foveated against peripheral\n    test: one-sided logit-Wilcoxon\n    p: 0.001\n    p_relation: \"<\"\n  - about: path selectivity, foveated against peripheral\n    p: 0.036\n  criterion: Per cell, (a) rate in the 500 ms after landmark appearance, leaving out appearances\n    with a saccade to the landmark in that period, and (b) rate in the 500 ms after foveation\n    (Results, paragraph 2). Landmark selectivity index with N = 4 (Methods, Landmark\n    selectivity, with a 150 ms offset after onset) and path selectivity index with N = 5\n    (Methods, Path selectivity index), each from (a) and from (b). The test is a one-sided\n    Wilcoxon signed-rank on the logit of the paired indices; the path test is read the same\n    way. Open, the cells (as in gaze-aligned-dynamics) and whether the 150 ms offset applies to\n    the foveation window, (a) no offset after foveation or (b) the same 150 ms. Reproduced when,\n    under one reading, landmark selectivity is higher foveated with p < 0.001 and path\n    selectivity higher with p < 0.05.\n  depends_on:\n  - gaze-aligned-dynamics\n- id: fields-per-cell\n  statement: Most cells had narrow selectivity and fewer than three positional fields, with an\n    average of 2.7 fields per cell, more than the about 1.5 reported in the rat.\n  source: Results, What is encoded in hippocampal cell activity, paragraph 4; Discussion,\n    Differences and similarities, paragraph 1; S5B Fig\n  quote: In addition, the number of fields per cell (average = 2.7) was greater than the number of\n    fields described in the rat (about 1.5)\n  expected:\n  - quantity: mean number of position fields per spatially selective cell\n    value: 2.7\n    tolerance: 0.27\n  criterion: The paper does not define a field in its main text or legends (S5B counts \"peaks\" of\n    cells \"displaying a spatial selectivity\"); the definition is presumably in S1 Appendix, which\n    was not read. Cells are read as those with significant position IC (Method W). No field\n    definition is fixed by the paper, so the author takes the claim as methods_underspecified\n    unless a definition is found in the paper; a count with a standard definition may be shown\n    as a variant.\n  depends_on:\n  - responsive-cells\n- id: spatial-selectivity-fraction\n  statement: Approximately 50% of the cells showed spatial selectivity like that reported in rats.\n  source: Discussion, Differences and similarities across mammalian hippocampal codes, paragraph 1\n  quote: Approximately 50% of our cells showed spatial selectivity like that in rats\n  expected:\n  - quantity: fraction of cells with spatial selectivity\n    value: 0.5\n    tolerance: 0.05\n  criterion: Method W. Which fraction is meant is open; readings (a) cells with significant\n    position IC among the 189; (b) responsive cells among the 189 (59%, responsive-cells).\n    Reproduced when the fraction under one reading is within tolerance.\n  depends_on:\n  - responsive-cells\n- id: gaze-map-landmarks\n  statement: In the population average of point-of-gaze maps, areas surrounding the landmarks\n    elicited up to 40% more activity than other areas, and all landmarks appeared represented.\n  source: S6C Fig legend; Results, What is encoded in hippocampal cell activity, paragraph 4\n  quote: Point of gaze map. Areas surrounding the landmarks (black rectangles) elicit up to 40% more\n    activity than other areas.\n  expected:\n  - quantity: maximal excess of mean normalized activity near landmarks over other areas\n    value: 0.4\n    tolerance: 0.04\n  criterion: Method W. Cells with point-of-gaze IC p < 0.001; each map normalized to its peak and\n    averaged (S6 legend). The area around a landmark is not delimited; readings (a) bins within\n    plus or minus 10 degrees of the landmark's direction (the foveation zone of the Methods);\n    (b) bins over the landmark's rectangle on the flattened map. The excess is the peak mean\n    near a landmark over the mean elsewhere, minus 1. Reproduced when, under one reading, the\n    excess is within tolerance and every landmark's area exceeds the mean elsewhere. The\n    population averages are described in S1 Appendix A4, not read.\n- id: dimensionality-control\n  statement: The higher information content of the state space is not due to the higher number of\n    dimensions of that space.\n  source: Results, Sensitivity of the cells, paragraph 3, and Hippocampal cells encode,\n    paragraph 1; S7 Fig\n  quote: This effect cannot be attributed to a modeling bias related to the higher number of\n    dimensions in the state space ( S1 Appendix A5 and S7 Fig ).\n  criterion: The control is described in S1 Appendix A5, which was not read; the S7 legend shows\n    only that spikes were simulated on the animal's trajectory with a box-shaped place field.\n    The method is not available from the text read; the author takes the claim as\n    methods_underspecified unless S1 Appendix is supplied.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/wirth-2017.yaml paper/10.1371-journal.pbio.2001045.txt; grep -n "—\|rather" claims/wirth-2017.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -nE '^\s+[^#-][^:]*: .*: ' claims/wirth-2017.yaml | grep -v '^\S*\s*quote: "' ; grep -nE '^\s{4,}[a-z].*: ' claims/wirth-2017.yaml | grep -vE '^\S+\s+(quantity|value|tolerance|unit|test|p|p_relation|n|about|corrected):' | head
```

```
332:    that correlation was only significantly higher in 3 cells, consistent with chance: p = 0.16,
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('claims/wirth-2017.yaml'))['claims']
print(len(d),sum('statistics' in c for c in d),sum('criterion' in c for c in d),sum('expected' in c for c in d))"
```

```
28 16 28 17
```

**Agent**

I wrote `claims/wirth-2017.yaml`. The quote checker reports 28 claims, 28 quotes, 25 statistical values and 0 problems.

**Text read**
- The version of record, PMC5328243 (Europe PMC full text). It includes the Results, Discussion, Methods, and the legends of Figs 1–7 and S1–S7. No PDF was read.
- **Missing:** the S1 Appendix (supplementary methods A1–A5) and the S2 Appendix are DOCX files and are not under `paper/`. The reference list is also absent, so reference 60, the learning-curve method, is not named.
- I went ahead anyway, because the core results (Figs 3–7) rest on the main Methods, which are present. Four claims need S1 Appendix and say so: `gaze-anticipates-action`, `gaze-anticipates-landmarks`, `fields-per-cell` and `dimensionality-control`. The last two are flagged as likely `methods_underspecified`: the text read never defines a "field" and does not describe the dimensionality control.
- **Code:** the paper links no repository. Its Matlab scripts are stored with the dataset on CRCNS, so I did not read them.

**Claims:** 28 in all. Every one has a quote and a criterion, 16 have statistics and 17 have expected values. They cover behaviour (gaze anticipation, learning, probe transfer), cell counts, information content and sparsity by coding space, direction tuning, state-space selectivity, the landmark ANOVAs, path selectivity, the gaze-aligned dynamics and latencies, eccentricity, foveation selectivity, place fields and population maps.

**Details left open, with the readings named**
- **Trial span:** whether the return path after a correct trial counts as part of it.
- **Surrogates:** whether the 5 s chunks are permuted in order or each shifted at random.
- **Binomial chance rate:** 0.05 or 0.025. The paper's own p-values fit 0.05 for state-space selectivity and 0.025 for the direction correlations. Neither rate gives p = 0.37 for the single path-invariant cell.
- **Point of gaze:** which eye (left, right or the mean), eye calibration, and how bin resolution is stepped in each space.
- **Unnamed tests and cell sets:** which cells enter, and which test, for centre against periphery, the gaze-aligned rise and the latencies.
- **Two conflicts within the paper:**
  - The gaze-before-action window is 500 ms in the Results and 300 ms in the S2 legend.
  - The path-selectivity offset is 120 ms in the Results while the Methods window starts at onset, and the Methods give 150 ms for landmark selectivity.
- **Landmarks:** how entry into the field of view and the "most informative landmark" are defined.
- **Behaviour:** which sessions count for learning, whether the probe test pools the two monkeys, and how trials to criterion are counted after new entries.
- **Landmark ANOVA:** whether "both factors" excludes cells with an interaction, and how a landmark view at the centre is delimited.
- **Spatial selectivity:** what "approximately 50%" counts (position-responsive cells or all responsive cells).
- **Gaze map:** how the area around a landmark is delimited.

**For the author:** the dataset's description says it holds 101 cells, each with a familiar and a new maze, and asks to be cited as doi 10.6080/K0GX48R9. The paper analysed 189 cells, describes only new mazes, and gives its data as doi 10.6080/K0R49NQV. I recorded this in the opening comment and did not try to resolve it.

## End of run

17 turns, 5 minutes, $1.44 at API prices, result: success.
