# 000139 · recorder · run 40785694376

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls claims/000139 transcripts/000139; cat attempts/000139-churchland-2010-01.yaml; python tools/readme_row.py 000139; python -c "
import json;d=json.load(open('targets/dandisets.json'))
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '000139' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))
"
```

```
<persisted-output>
Output too large (52.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a96fb6f6-2142-4240-883d-413ddb2f07ac/tool-results/bd23kylm4.txt

Preview (first 2KB):
docs/pilot-notes/000233-tingley-2021-01.md
docs/pilot-notes/openneuro-ds000228-richardson-2018-01.md
docs/pilot-notes/openneuro-ds004752-dimakopoulos-2022-01.md
docs/pilot-notes/001177-zhuang-2025-01.md
docs/pilot-notes/000248-shin-2025-01.md
claims/000139:
10.1016-j.neuron.2010.09.015.yaml

transcripts/000139:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 50 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a96fb6f6-2142-4240-883d-413ddb2f07ac/tool-results/bd23kylm4.txt"
}
```

```
1	docs/pilot-notes/000233-tingley-2021-01.md
2	docs/pilot-notes/openneuro-ds000228-richardson-2018-01.md
3	docs/pilot-notes/openneuro-ds004752-dimakopoulos-2022-01.md
4	docs/pilot-notes/001177-zhuang-2025-01.md
5	docs/pilot-notes/000248-shin-2025-01.md
6	claims/000139:
7	10.1016-j.neuron.2010.09.015.yaml
8	
9	transcripts/000139:
10	answer-report.md
11	answer.md
12	author-answers-report.md
13	author-answers.md
14	author-report.md
15	author-revise-1-report.md
16	author-revise-1.md
17	author-revise-2-report.md
18	author-revise-2.md
19	author.md
20	claims-check-report.md
[... 836 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 -A15 '"000139"' targets/dandisets.json | head -40; head -30 README.md | grep -n '|' | head -5; for f in docs/pilot-notes/000233-tingley-2021-01.md docs/pilot-notes/openneuro-ds000228-richardson-2018-01.md docs/pilot-notes/001177-zhuang-2025-01.md docs/pilot-notes/000248-shin-2025-01.md docs/pilot-notes/openneuro-ds004752-dimakopoulos-2022-01.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (37.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a96fb6f6-2142-4240-883d-413ddb2f07ac/tool-results/blo1obm5u.txt

Preview (first 2KB):
1232-   "catalystneuro": []
1233-  },
1234-  {
1235:   "dandiset": "000139",
1236-   "name": "MC_Maze_Medium: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching",
1237-   "published_version": "0.220113.0408",
1238-   "asset_count": 2,
1239-   "size_gb": 0.08,
1240-   "data_standards": [
1241-    "Neurodata Without Borders (NWB)"
1242-   ],
1243-   "species": [
1244-    "Rhesus monkey"
1245-   ],
1246-   "approaches": [
1247-    "electrophysiological approach"
[... 26 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a96fb6f6-2142-4240-883d-413ddb2f07ac/tool-results/blo1obm5u.txt"
}
```

```
1	1232-   "catalystneuro": []
2	1233-  },
3	1234-  {
4	1235:   "dandiset": "000139",
5	1236-   "name": "MC_Maze_Medium: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching",
6	1237-   "published_version": "0.220113.0408",
7	1238-   "asset_count": 2,
8	1239-   "size_gb": 0.08,
9	1240-   "data_standards": [
10	1241-    "Neurodata Without Borders (NWB)"
11	1242-   ],
12	1243-   "species": [
13	1244-    "Rhesus monkey"
14	1245-   ],
15	1246-   "approaches": [
16	1247-    "electrophysiological approach"
17	1248-   ],
18	1249-   "papers": [
19	1250-    {
20	=== docs/pilot-notes/000233-tingley-2021-01.md
[... 526 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1234,1300p targets/dandisets.json; head -80 claims/000139/*.yaml; grep -n 'data:' claims/000139/*.yaml | sort | uniq -c | head; wc -l transcripts/000139/*-report.md
```

```
{
   "dandiset": "000139",
   "name": "MC_Maze_Medium: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching",
   "published_version": "0.220113.0408",
   "asset_count": 2,
   "size_gb": 0.08,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Rhesus monkey"
   ],
   "approaches": [
    "electrophysiological approach"
   ],
   "papers": [
    {
     "doi": "10.1016/j.neuron.2010.09.015",
     "title": "Cortical preparatory activity: representation of movement or first cog in a dynamical machine?",
     "relation": "IsDescribedBy",
[... 137 more lines not kept]
```

**Agent**

Gathered the attempt record and recent notes; now reading the run reports.

**Agent calls Bash**

```bash
cd transcripts/000139; for f in author-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (35.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a96fb6f6-2142-4240-883d-413ddb2f07ac/tool-results/b0bbjwrr0.txt

Preview (first 2KB):
=== author-report.md
I've done steps 1 to 6 for DANDI:000139, pinned at 0.220113.0408. It is the only published version and the paper cites none. The notebook passes `entry.py check` and ran clean under `entry.py all` in 362 s; the handover package is built. I did not verify my own work.

## 1. Outcomes (23 claims)

| Claim | Outcome |
|---|---|
| j-array-recordings | partially reproduced (152 units, but 27 conditions, not 108) |
| fig4d-mean-correlation-j-array | partially reproduced, assumed (r = 0.172, p = 0.042) |
| fig4-broad-unimodal | reproduced, assumed |
| fig4e-correlation-time-course | reproduced, assumed |
| suppfig1-population-psth-weak-movement-tuning | reproduced, assumed (reading (a) only; ratio 0.942) |
| fig6d-perimovement-best-j-array | reproduced, assumed |
| fig6-perimovement-best-each-dimensionality | reproduced, assumed (91 to 96% of comparisons) |
| fig6-dimensionality-peak | reproduced, assumed (S fixed across folds) |
| fig6-maze-task-spaces | blocked: methods_underspecified |
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a96fb6f6-2142-4240-883d-413ddb2f07ac/tool-results/b0bbjwrr0.txt"
}
```

```
1	=== author-report.md
2	I've done steps 1 to 6 for DANDI:000139, pinned at 0.220113.0408. It is the only published version and the paper cites none. The notebook passes `entry.py check` and ran clean under `entry.py all` in 362 s; the handover package is built. I did not verify my own work.
3	
4	## 1. Outcomes (23 claims)
5	
6	| Claim | Outcome |
7	|---|---|
8	| j-array-recordings | partially reproduced (152 units, but 27 conditions, not 108) |
9	| fig4d-mean-correlation-j-array | partially reproduced, assumed (r = 0.172, p = 0.042) |
10	| fig4-broad-unimodal | reproduced, assumed |
11	| fig4e-correlation-time-course | reproduced, assumed |
12	| suppfig1-population-psth-weak-movement-tuning | reproduced, assumed (reading (a) only; ratio 0.942) |
13	| fig6d-perimovement-best-j-array | reproduced, assumed |
14	| fig6-perimovement-best-each-dimensionality | reproduced, assumed (91 to 96% of comparisons) |
15	| fig6-dimensionality-peak | reproduced, assumed (S fixed across folds) |
16	| fig6-maze-task-spaces | blocked: methods_underspecified |
17	| fig6-preparatory-dimensionality | not reproduced (12 PCs; shuffled labels give 17) |
18	| fig7a-shuffled-space-poor | reproduced, assumed |
19	| fig7b-window-start-slide | reproduced, assumed (0.911) |
20	| ap-location-no-effect-j-array | reproduced, assumed (AP read as the array) |
[... 279 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A4 -E '^  - id:|^- id:|statement:' claims/000139/*.yaml | grep -v '^\-\-' | head -150; cat questions/000139.yaml 2>/dev/null | head -5; head -20 README.md | grep -i reproduced
```

```
95:- id: j-array-recordings
96:  statement: The J-array dataset holds 146 single- and multi-unit isolations recorded with two
97-    96-electrode arrays during the maze task, over 108 conditions, with a mean of 2166 trials per
98-    neuron.
99-  source: Results, Behavior and recordings, paragraph 1; Methods, Neural recordings and datasets
100-  quote: a pair of implanted 96-electrode arrays (J-array dataset, 146 single- and multi-unit
118:- id: fig4d-mean-correlation-j-array
119:  statement: For the J-array dataset, preparatory and peri-movement tuning are positively but only
120-    weakly correlated on average across neurons (mean r = 0.13, p = 0.03; mean Spearman r =
121-    0.11).
122-  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 1; Figure
123-    4D
147:- id: fig4abc-mean-correlation-other-datasets
148:  statement: For monkeys A, B and J (single electrodes) the mean correlation between preparatory
149-    and peri-movement tuning is 0.21, 0.19 and 0.06 (p = 0.01, 0.01, 0.12), with mean Spearman r
150-    of 0.20, 0.20 and 0.06.
151-  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 1; Figure
152-    4A to 4C
185:- id: fig4-broad-unimodal
186:  statement: Individual neurons span a broad range of preparatory to peri-movement correlations
[... 123 more lines not kept]
```

**Agent**

Now writing the note.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000139-churchland-2010-01.md",
 "content": "# 000139, Churchland et al. 2010\n\nFourteen claims reproduced, two partially, two not reproduced and five\nblocked, all on the dataset. It pins version 0.220113.0408, its only published\nversion, as the paper cites none. The paper, Churchland, Cunningham, Kaufman,\nRyu and Shenoy in Neuron, records three rhesus monkeys making delayed reaches\nand reports that preparatory and peri-movement tuning in PMd and M1 are only\nweakly correlated (mean r = 0.13 for the J-array dataset), that a preferred\ndirection (PD) captures preparatory tuning best when expressed in a space\nbuilt from peri-movement activity, better than kinematic, task and EMG\nspaces, and that a simulated linear dynamical system shows the same pattern.\nThe claims were written from the NIH author manuscript in PubMed Central\n(PMC2991102) with its one supplement, not the version of record; the paper\nlinks no code. The J-array claims were tested: the recordings, the tuning\ncorrelations of Figure 4D and 4E and Supplemental Figure 1, the PD performance\nof Figure 6D, the controls of Figure 7, the anterior and posterior\ncomparisons, and the Figure 8 simulation. The claims on the speed-task\ndatasets of monkeys A and B, the single-electrode monkey J dataset and EMG\n(Figures 4A to 4C, 6A to 6C and 6E, and the AP regression for those datasets)\nare blocked as `data_missing`, and `prep-activity-more-anterior` as\n`metadata_insufficient`, as nothing in the files says which unit id prefix is\nthe PMd array. `fig6-preparatory-dimensionality` is not reproduced (12 PCs\nfor 90% of the variance against 6.3 to 11; 17 with condition labels shuffled,\nand 7 by cross-validated PCA), and `fig7c-anterior-posterior-performance` is\nnot reproduced, as neither array is within 10% of the random halves (6-D, S\nfixed, 0.761 and -0.402 against 0.455). The author's first run gave 13\nreproduced, 2 partially, 3 not reproduced and 5 blocked. The author asked a\nreader no questions, so the answer run and the following author run changed\nnothing; two questions were put to a reader during the revisions, after the\nanswer step, on whether the partial clause of `j-array-recordings` fits a\n27-condition session and on the width of the fig7c band (+/- 0.046 against\nan SD of 0.153 for the random halves). Round 1 agreed with 20 of 23 outcomes;\nthe author took its outcomes for `fig6-maze-task-spaces` (from blocked as\n`methods_underspecified` to reproduced, as the claims file names both segment\ndivisions) and `prep-activity-more-anterior` (from not reproduced to blocked),\nand kept `fig6-dimensionality-peak` reproduced, resting on S fixed across\nfolds, where the verifier gave partially reproduced. Its points led to a\nlabel-shuffled reference for the 5 spikes/s threshold, a per-unit permutation\ntest, chance levels for the spaces, Figure 7C run with the paper's upper limit\nincluding the fitted neuron, a cross-validated ranking for Supplemental Figure\n1, cross-validated PCA and a printout of the session description and the\nelectrode metadata. Round 2 agreed with all 23, the verifier changing its\nround-1 position on the dimensionality peak after the chance curves (a fall\nof 2.292 from k = 6 to 14 with S fixed and 0.094 with S recomputed), so there\nwas no third round; it found statements the outputs did not support, among\nthem \"Only 59\" units passing on shuffled labels, chance stated for every space,\nupper limits all at or below zero where 2 of 8 are, 350 trials for units the\ntest file does not hold and a sentence on dandiset 000128 that nothing\nprinted, which were corrected, and `j-array-recordings` was marked as assumed.\nSome outcomes rest on weak ground: `fig4e-correlation-time-course` passes in\nthe main selection only with the trace spliced at the median RT, which sets\nthe decline (-263 ms) at the end of the preparatory window, and without the\nsplice holds in 6 of 8 selection readings with all preparatory neurons and 3\nof 8 with the neurons of Figure 4D; `suppfig1-population-psth-weak-movement-tuning`\ndoes not survive cross-validated ranking for the claim's 17 neurons (ratio\n1.115); `fig4d-mean-correlation-j-array` passes p < 0.05 by the t-test only\n(p = 0.042, Wilcoxon p = 0.071) and in 5 of 8 selection readings;\n`fig6-maze-task-spaces` has segment directions above zero in 2 of 8 selection\nreadings and rests on segments equal in time; and the check of\n`fig8-linear-dynamics-simulation` is weak and rests on the full-cycle gray\ninterval. The author's run went from 19:44 to about 20:23 UTC and nothing\nfailed; the notebook ran in 362 s at first and in 620 s in the last run.\n\nThe dandiset holds one maze-task array session of monkey J (2009-09-29) cut\nfor the Neural Latents Benchmark, with 152 units, 27 conditions (9 mazes in\nthree versions) and 250 labelled trials, where the paper's J-array dataset had\n108 conditions and about 2166 trials per neuron; the speed-task datasets of\nmonkeys A and B, the single-electrode monkey J dataset and all EMG are not\ndeposited, so 4 of the paper's main findings cannot be tested and the others\nrest on 6 to 10 trials per condition. With so few trials a median of 59 of 152\nunits pass the 5 spikes/s threshold on shuffled labels against 75 observed,\nonly 43 of the 76 PD neurons have tuning distinguishable from noise, and the\nsplit-half reliability of preparatory tuning is a median r of 0.374. Nothing\nin the files or the dandiset metadata says whether this session is the\npaper's J-array recording or how its 27 conditions relate to the paper's 108;\nthe trial timeline is rebuilt, so the files cannot show whether the session\nheld other mazes. Every unit's electrode reference points at a row of the PMd\nelectrode group, although the unit ids put 77 of the 152 units on a second\narray, whose references (rows 14 to 94) match their channel numbers without\nthe offset of 96 that would place them on the M1 rows. The electrode table's\nx, y, z and impedance columns are empty, and nothing says whether id prefix 1\nor 2 is the PMd array. The 100 test trials are 700 ms segments without\ncondition labels, go cue or behaviour, for the 114 held-in units only, and how\nthe trials and the 9 mazes were chosen from the session is not described.\nFive questions are put to the paper's authors: what the proto-trial of the\ntrial selection is and whether the horizontal and vertical velocity profiles\nare compared separately or together; whether tuning strength is the range or\nthe standard deviation of condition means; whether the PCA-based space S is\nrecomputed without the left-out condition; whether the reach is divided into\nsegments of equal time or equal path length; and how movement onset was\ndetected, where the Figure 4E trace is spliced and what the gray interval of\nFigure 8 is.\n\nThe author's points on the protocol: it does not say whether a reading adopted\nfor one claim carries to the claims that depend on it, so one main reading was\nadopted for all and the dependent outcomes marked assumed; it is unclear\nwhether `assumed` covers data identity, such as whether the 27 mazes are among\nthe paper's 108; it gives no rule for a criterion whose reference value comes\nout degenerate, as the Figure 7C normalization did; the criterion's rule that\nany reading suffices and step 1.6's rule that all open-detail readings must\nagree can conflict, as in suppfig1; and the repository root has untracked\nfiles from the sandbox.\n"
}
```

```
File created successfully at: docs/pilot-notes/000139-churchland-2010-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -nE '—|rather|\*\*' docs/pilot-notes/000139-churchland-2010-01.md
```

```
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? docs/pilot-notes/000139-churchland-2010-01.md
?? scripts
```

**Agent**

I wrote the note in `docs/pilot-notes/000139-churchland-2010-01.md`, which is new and the only file I added. It has no em dashes, no "rather", no bold and no lists, and nothing is committed. The repository root also has untracked files (`.bashrc`, `.idea`, `scripts` and others) that were there before; the author's report mentions them too, and I left them alone.

# 000139, Churchland et al. 2010

Fourteen claims reproduced, two partially, two not reproduced and five
blocked, all on the dataset. It pins version 0.220113.0408, its only published
version, as the paper cites none. The paper, Churchland, Cunningham, Kaufman,
Ryu and Shenoy in Neuron, records three rhesus monkeys making delayed reaches
and reports that preparatory and peri-movement tuning in PMd and M1 are only
weakly correlated (mean r = 0.13 for the J-array dataset), that a preferred
direction (PD) captures preparatory tuning best when expressed in a space
built from peri-movement activity, better than kinematic, task and EMG
spaces, and that a simulated linear dynamical system shows the same pattern.
The claims were written from the NIH author manuscript in PubMed Central
(PMC2991102) with its one supplement, not the version of record; the paper
links no code. The J-array claims were tested: the recordings, the tuning
correlations of Figure 4D and 4E and Supplemental Figure 1, the PD performance
of Figure 6D, the controls of Figure 7, the anterior and posterior
comparisons, and the Figure 8 simulation. The claims on the speed-task
datasets of monkeys A and B, the single-electrode monkey J dataset and EMG
(Figures 4A to 4C, 6A to 6C and 6E, and the AP regression for those datasets)
are blocked as `data_missing`, and `prep-activity-more-anterior` as
`metadata_insufficient`, as nothing in the files says which unit id prefix is
the PMd array. `fig6-preparatory-dimensionality` is not reproduced (12 PCs
for 90% of the variance against 6.3 to 11; 17 with condition labels shuffled,
and 7 by cross-validated PCA), and `fig7c-anterior-posterior-performance` is
not reproduced, as neither array is within 10% of the random halves (6-D, S
fixed, 0.761 and -0.402 against 0.455). The author's first run gave 13
reproduced, 2 partially, 3 not reproduced and 5 blocked. The author asked a
reader no questions, so the answer run and the following author run changed
nothing; two questions were put to a reader during the revisions, after the
answer step, on whether the partial clause of `j-array-recordings` fits a
27-condition session and on the width of the fig7c band (+/- 0.046 against
an SD of 0.153 for the random halves). Round 1 agreed with 20 of 23 outcomes;
the author took its outcomes for `fig6-maze-task-spaces` (from blocked as
`methods_underspecified` to reproduced, as the claims file names both segment
divisions) and `prep-activity-more-anterior` (from not reproduced to blocked),
and kept `fig6-dimensionality-peak` reproduced, resting on S fixed across
folds, where the verifier gave partially reproduced. Its points led to a
label-shuffled reference for the 5 spikes/s threshold, a per-unit permutation
test, chance levels for the spaces, Figure 7C run with the paper's upper limit
including the fitted neuron, a cross-validated ranking for Supplemental Figure
1, cross-validated PCA and a printout of the session description and the
electrode metadata. Round 2 agreed with all 23, the verifier changing its
round-1 position on the dimensionality peak after the chance curves (a fall
of 2.292 from k = 6 to 14 with S fixed and 0.094 with S recomputed), so there
was no third round; it found statements the outputs did not support, among
them "Only 59" units passing on shuffled labels, chance stated for every space,
upper limits all at or below zero where 2 of 8 are, 350 trials for units the
test file does not hold and a sentence on dandiset 000128 that nothing
printed, which were corrected, and `j-array-recordings` was marked as assumed.
Some outcomes rest on weak ground: `fig4e-correlation-time-course` passes in
the main selection only with the trace spliced at the median RT, which sets
the decline (-263 ms) at the end of the preparatory window, and without the
splice holds in 6 of 8 selection readings with all preparatory neurons and 3
of 8 with the neurons of Figure 4D; `suppfig1-population-psth-weak-movement-tuning`
does not survive cross-validated ranking for the claim's 17 neurons (ratio
1.115); `fig4d-mean-correlation-j-array` passes p < 0.05 by the t-test only
(p = 0.042, Wilcoxon p = 0.071) and in 5 of 8 selection readings;
`fig6-maze-task-spaces` has segment directions above zero in 2 of 8 selection
readings and rests on segments equal in time; and the check of
`fig8-linear-dynamics-simulation` is weak and rests on the full-cycle gray
interval. The author's run went from 19:44 to about 20:23 UTC and nothing
failed; the notebook ran in 362 s at first and in 620 s in the last run.

The dandiset holds one maze-task array session of monkey J (2009-09-29) cut
for the Neural Latents Benchmark, with 152 units, 27 conditions (9 mazes in
three versions) and 250 labelled trials, where the paper's J-array dataset had
108 conditions and about 2166 trials per neuron; the speed-task datasets of
monkeys A and B, the single-electrode monkey J dataset and all EMG are not
deposited, so 4 of the paper's main findings cannot be tested and the others
rest on 6 to 10 trials per condition. With so few trials a median of 59 of 152
units pass the 5 spikes/s threshold on shuffled labels against 75 observed,
only 43 of the 76 PD neurons have tuning distinguishable from noise, and the
split-half reliability of preparatory tuning is a median r of 0.374. Nothing
in the files or the dandiset metadata says whether this session is the
paper's J-array recording or how its 27 conditions relate to the paper's 108;
the trial timeline is rebuilt, so the files cannot show whether the session
held other mazes. Every unit's electrode reference points at a row of the PMd
electrode group, although the unit ids put 77 of the 152 units on a second
array, whose references (rows 14 to 94) match their channel numbers without
the offset of 96 that would place them on the M1 rows. The electrode table's
x, y, z and impedance columns are empty, and nothing says whether id prefix 1
or 2 is the PMd array. The 100 test trials are 700 ms segments without
condition labels, go cue or behaviour, for the 114 held-in units only, and how
the trials and the 9 mazes were chosen from the session is not described.
Five questions are put to the paper's authors: what the proto-trial of the
trial selection is and whether the horizontal and vertical velocity profiles
are compared separately or together; whether tuning strength is the range or
the standard deviation of condition means; whether the PCA-based space S is
recomputed without the left-out condition; whether the reach is divided into
segments of equal time or equal path length; and how movement onset was
detected, where the Figure 4E trace is spliced and what the gray interval of
Figure 8 is.

The author's points on the protocol: it does not say whether a reading adopted
for one claim carries to the claims that depend on it, so one main reading was
adopted for all and the dependent outcomes marked assumed; it is unclear
whether `assumed` covers data identity, such as whether the 27 mazes are among
the paper's 108; it gives no rule for a criterion whose reference value comes
out degenerate, as the Figure 7C normalization did; the criterion's rule that
any reading suffices and step 1.6's rule that all open-detail readings must
agree can conflict, as in suppfig1; and the repository root has untracked
files from the sandbox.

## End of run

11 turns, 1 minutes, result: success.
