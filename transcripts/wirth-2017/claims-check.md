# wirth-2017 · claims-check · run 42844155460

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i wirth; cat claims/wirth-2017.yaml; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/f7f136d4-3b7d-4388-aeab-411ba0416544/tool-results/b93q6bv3m.txt"
}
```

```
1	# Claims for Wirth, Baraduc, Plante, Pinede & Duhamel (2017), PLoS Biology 15(2), e2001045,
2	# tested on CRCNS hc-21.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
4	# protocol pilot-14 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record (PMC5328243, open access), full text from Europe PMC JATS
7	# XML as stored under paper/: Results, Discussion, Materials and Methods, the figure legends of
8	# Figs 1 to 7 and the legends of S1 to S7 Figs. The supplementary text files S1 Appendix
9	# (sections A1 to A5: point-of-gaze density maps, gaze before joystick actions, recording
10	# methods and cell selection, population averages, the control for space dimensionality) and
11	# S2 Appendix (description of the CRCNS files and scripts) are DOCX files that are not under
12	# paper/ and were not read. The claims that rest on them say so (gaze-anticipates-action,
13	# gaze-anticipates-landmarks, dimensionality-control, fields-per-cell). No PDF was read; the
14	# reference list is absent from the stored text, so reference 60 (the learning curve method)
15	# is not named.
16	#
17	# Code: the paper links no repository. It says some Matlab scripts are hosted with the data on
18	# CRCNS (Supporting data; S2 Appendix). These are files of the dataset and were not read. No
19	# criterion below takes a method from code.
20	#
[... 748 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/; sed -n '/^## Reader/,/^## [A-Z]/p' docs/protocol.md; python tools/claims_check.py claims/wirth-2017.yaml paper/*wirth*.txt 2>&1 | tail -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/wirth-2017.yaml paper/10.1371-journal.pbio.2001045.txt 2>&1 | tail -20; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the paper.

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
python3 -c "
from scipy.stats import binom
for k,n in [(12,111),(4,111),(20,56),(3,56),(1,42),(12,42),(14,111),(15,111),(29,111)]:
  for p0 in (0.05,0.025,0.01):
    print(k,n,p0,'P>=k %.4f'%binom.sf(k-1,n,p0),'P<=k %.4f'%binom.cdf(k,n,p0),'2side %.4f'%__import__('scipy.stats',fromlist=['x']).binomtest(k,n,p0).pvalue)
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
def pmf(k,n,p): return comb(n,k)*p**k*(1-p)**(n-k)
def cdf(k,n,p): return sum(pmf(i,n,p) for i in range(k+1))
def two(k,n,p):
  pk=pmf(k,n,p); return min(1,sum(pmf(i,n,p) for i in range(n+1) if pmf(i,n,p)<=pk*(1+1e-7)))
for k,n in [(12,111),(4,111),(20,56),(3,56),(1,42),(12,42),(14,111),(15,111),(29,111)]:
  for p0 in (0.05,0.025,0.01):
    print(k,n,p0,'P>=k %.4f'%(1-cdf(k-1,n,p0)),'P<=k %.4f'%cdf(k,n,p0),'2side %.4f'%two(k,n,p0))
"
```

```
12 111 0.05 P>=k 0.0097 P<=k 0.9963 2side 0.0131
12 111 0.025 P>=k 0.0000 P<=k 1.0000 2side 0.0000
12 111 0.01 P>=k 0.0000 P<=k 1.0000 2side 0.0000
4 111 0.05 P>=k 0.8111 P<=k 0.3437 2side 0.6636
4 111 0.025 P>=k 0.3019 P<=k 0.8540 2side 0.3620
4 111 0.01 P>=k 0.0258 P<=k 0.9947 2side 0.0258
20 56 0.05 P>=k 0.0000 P<=k 1.0000 2side 0.0000
20 56 0.025 P>=k 0.0000 P<=k 1.0000 2side 0.0000
20 56 0.01 P>=k 0.0000 P<=k 1.0000 2side 0.0000
3 56 0.05 P>=k 0.5354 P<=k 0.6931 2side 0.7587
3 56 0.025 P>=k 0.1646 P<=k 0.9486 2side 0.1646
3 56 0.01 P>=k 0.0187 P<=k 0.9976 2side 0.0187
1 42 0.05 P>=k 0.8840 P<=k 0.3724 2side 0.7234
1 42 0.025 P>=k 0.6547 P<=k 0.7172 2side 1.0000
1 42 0.01 P>=k 0.3443 P<=k 0.9338 2side 0.3443
12 42 0.05 P>=k 0.0000 P<=k 1.0000 2side 0.0000
12 42 0.025 P>=k 0.0000 P<=k 1.0000 2side 0.0000
12 42 0.01 P>=k 0.0000 P<=k 1.0000 2side 0.0000
14 111 0.05 P>=k 0.0013 P<=k 0.9996 2side 0.0013
14 111 0.025 P>=k 0.0000 P<=k 1.0000 2side 0.0000
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  tail -5 claims/wirth-2017.yaml; grep -n "checks" claims/*.yaml | head -3; grep -n -A12 "^checks" $(grep -l "^checks" claims/*.yaml | head -1) | head -20
```

```
dimensions in the state space ( S1 Appendix A5 and S7 Fig ).
  criterion: The control is described in S1 Appendix A5, which was not read; the S7 legend shows
    only that spikes were simulated on the animal's trajectory with a box-shaped place field.
    The method is not available from the text read; the author takes the claim as
    methods_underspecified unless S1 Appendix is supplied.
claims/alasfour-2024.yaml:645:checks:
claims/andrews-2024.yaml:119:    claim checks that such recordings exist). Reproduced when all 13 counts are within
claims/andrews-2024.yaml:850:checks:
645:checks:
646-- date: 2026-11-10
647-  kind: agent
648-  model: claude-opus-5-5
649-  ready: true
650-  changes:
651-  - fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois. Removed the statistics entries (t-test against finite chance, BH FDR at 0.01); the threshold marks which features count as above chance (Figure 2 legend), a method and not a result. The criteria keep it through M6.
652-  - fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral. Removed the statistics entries (t-test of the mean difference against zero, BH FDR at 0.01); the threshold selects the consistent features whose signs are counted (Figure 5 legend), a method and not a result. The criteria keep it through M8.
653-  - table1-participants. Removed the rule that 13 of the 15 minute values suffice; the paper gives no such threshold, so every value must now be within tolerance.
654-  - fig6-sign-consistency. The tolerance of 0.9 allowed only 9 while the criterion accepted 8 to 10. Set the tolerance to 1 (10% of 9 rounded to a whole combination) and gave the reason.
655-  - Header O4. The SD of the channel was fixed as the whole recording, called a standard choice; it can change which blocks are dropped, so the readings (whole recording, the day's recording) are now named.
656-  - Header O10, anova-roi-band-effects, anova-no-interaction. The ANO
[... 1 more lines not kept]
```

**Agent**

Now the edits.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "#    3 of 56 (direction correlation, p = 0.16) matches (b). Each claim names the reading its\n#    numbers fit.",
 "new_string": "#    3 of 56 (direction correlation, p = 0.16) matches (b); 1 of 42 (path invariance,\n#    p = 0.37) matches the lower tail P(X <= 1) under (a). Each claim names the reading its\n#    numbers fit."
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "    left turns (the distributions of S2A). Reproduced when, under one reading, eye position\n    before right turns lies to the right of that before left turns, with p < 0.001, in each\n    monkey.",
 "new_string": "    left turns (the distributions of S2A). The Results give one p while S2 Fig shows each\n    monkey; readings (i) each monkey separately, (ii) both monkeys pooled. Reproduced when,\n    under one reading, eye position before right turns lies to the right of that before left\n    turns, with p < 0.001 (in each monkey under (i))."
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "    Wilcoxon rank-sum test. Reproduced when eye position lies toward the side of the turn with\n    p < 0.001 in each monkey. The test the paper ran is not fully specified, a deviation.",
 "new_string": "    Wilcoxon rank-sum test. Per monkey or pooled, as in gaze-anticipates-action. Reproduced when,\n    under one of these readings, eye position lies toward the side of the turn with p < 0.001\n    (in each monkey when taken separately). The test the paper ran is not fully specified, a\n    deviation."
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "  criterion: How trials to criterion after the new entries are counted is not stated. Readings\n    (a) trials from the introduction of the new entries until the lower confidence bound again\n    exceeds 1/4, on the session's learning curve; (b) trials from the introduction until the\n    first correct trial from a new entry. Compared",
 "new_string": "  criterion: How trials to criterion after the new entries are counted is not stated. The\n    learning criterion is the lower confidence bound exceeding 1/4 (S3B legend); on the\n    session's running learning curve it is usually already met when the new entries come in\n    (S3C legend, trials 37 and 60), so the curve is taken from the introduction on. Readings\n    (a) a learning curve on all trials from the introduction of the new entries; (b) a learning\n    curve on the trials from the new entries only; in each, the number of trials until the\n    lower bound exceeds 1/4. Compared"
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "    size is reported. Per cell, the difference is significant when its surrogate p (the\n    difference recomputed on each surrogate) is below 0.05, bilateral. Reproduced",
 "new_string": "    size is reported. Per cell, the difference is significant when its surrogate p (the\n    difference recomputed on each surrogate) is below the per-cell level, bilateral. The level\n    is not stated (Fig 3 legend, \"permutation tests\"); readings (a) 0.05, the level the binomial\n    counts imply; (b) 0.01, the level of the IC tests. Reproduced"
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "    500 ms or (b) its mean. Binomial chance rate 0.05 or 0.025 (Method W); neither gives the\n    paper's p = 0.37 for one cell, which is reported, not judged. Reproduced",
 "new_string": "    500 ms or (b) its mean. Binomial chance rate 0.05 (Method W, reading (a)); the paper's\n    p = 0.37 for one cell equals the lower tail P(X <= 1) at 0.05 and is reported, not judged.\n    Reproduced"
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "  source: Results, What is encoded in hippocampal cell activity, paragraph 4; Discussion,",
 "new_string": "  source: Results, What is encoded in hippocampal cell activity, paragraph 3; Discussion,"
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "  source: S6C Fig legend; Results, What is encoded in hippocampal cell activity, paragraph 4",
 "new_string": "  source: S6C Fig legend; Results, What is encoded in hippocampal cell activity, paragraph 3"
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "    (b) bins over the landmark's rectangle on the flattened map. The excess is the peak mean\n    near a landmark over the mean elsewhere, minus 1. Reproduced",
 "new_string": "    (b) bins over the landmark's rectangle on the flattened map. How \"more activity\" is\n    measured is not stated; the excess is taken as the peak mean near a landmark over the mean\n    elsewhere, minus 1, a standard choice and a deviation. Reproduced"
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "    position IC among the 189; (b) responsive cells among the 189 (59%, responsive-cells).",
 "new_string": "    position IC among the 189; (b) responsive cells among the 189 (59%, responsive-cells);\n    (c) cells with significant position IC among the 111 responsive cells (Fig 3A)."
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent**

Now the checks entry.

**Agent calls Bash**

```bash
cd  cat >> claims/wirth-2017.yaml <<'EOF'
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header, Method W, binomial tests. Added that 1 of 42 with p = 0.37 matches the lower tail P(X <= 1) at a chance rate of 0.05 (computed, 0.372); the file had said no reading gives it.
  - path-selectivity. Same correction in the criterion; the chance rate is now 0.05 (reading (a)), and the p = 0.37 is still reported, not judged.
  - gaze-anticipates-action, gaze-anticipates-landmarks. The criteria required p < 0.001 in each monkey, but the Results give one p and do not say the monkeys were tested separately (S2 Fig shows them apart). Named per monkey and pooled as readings.
  - probe-faster-criterion. Reading (b), trials to the first correct trial from a new entry, is not the learning criterion (lower bound above 1/4, S3B legend) and was made up. Reading (a), the session's running curve, is in most sessions already past criterion when the new entries come in (S3C legend, trials 37 and 60). Replaced both with learning curves begun at the introduction, on all trials or on new-entry trials only.
  - sparsity-state-vs-position (and through it sparsity-gaze-vs-state). The per-cell significance level for the sparsity difference was fixed at 0.05 without a source; the paper does not state it. Named 0.05 and 0.01 as readings.
  - fields-per-cell, gaze-map-landmarks. The source said paragraph 4 of "What is encoded in hippocampal cell activity"; the sentences are in paragraph 3 (the section has three paragraphs before the Fig 2 legend).
  - gaze-map-landmarks. The excess measure (peak near a landmark over mean elsewhere, minus 1) is not the paper's; it is now marked as a standard choice and a deviation.
  - spatial-selectivity-fraction. Added reading (c), position-responsive cells among the 111 responsive cells, which the Discussion's "our cells" also allows (Fig 3A gives proportions per space).
  - Open. S1 Appendix (A1 to A5) is not under paper/. gaze-anticipates-action and gaze-anticipates-landmarks take their methods from the S2 legend alone, and fields-per-cell and dimensionality-control cannot be judged without it. Supplying S1 Appendix would settle them.
  - Open. Reference 60 (the learning curve method of learning-trials, learning-to-90 and probe-faster-criterion) is not named in the stored text, as the reference list is absent.
  - Open. landmark-identity-distance. The paper gives p < 0.001 for 14 of 111 interaction cells, but at a chance rate of 0.05 the binomial tail is 0.0013; the chance rate for these counts remains unsettled. The criterion does not judge this test.
  - Open. No claim covers the gaze density result that gaze was attracted to the rewarded path and the landmarks (Results, Animals use direction, paragraph 2; Fig 1H); its method is in S1 Appendix A1, not read. A minor finding, left without a claim.
EOF
python tools/claims_check.py claims/wirth-2017.yaml paper/10.1371-journal.pbio.2001045.txt; grep -n "—\|rather" claims/wirth-2017.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker reports `claims/wirth-2017.yaml: 28 claims, 28 quotes, 25 statistical values, 0 problems`, both before my edits and after. No claim id was changed, and nothing was committed.

**Changes, by claim**
- **Header (Method W) and path-selectivity:** the file said no chance rate gives the paper's p = 0.37 for 1 of 42 cells. That was wrong. At a chance rate of 0.05, the chance of 1 or fewer is 0.372. I corrected both places; the value is still reported, not judged.
- **gaze-anticipates-action and gaze-anticipates-landmarks:** the criteria demanded p < 0.001 in each monkey. The Results give a single p, so testing each monkey separately and pooling both monkeys are now two readings.
- **probe-faster-criterion:** both readings were flawed.
  - Reading (b), trials until the first correct trial from a new entry, is not the paper's learning criterion (lower confidence bound above 1/4).
  - Reading (a) used the session's running learning curve, which in most sessions is already past criterion when the new entries come in (trials 37 and 60 in the S3C examples).
  - The new readings start a learning curve when the new entries are introduced, using either all trials or only the trials from new entries.
- **sparsity-state-vs-position (also used by sparsity-gaze-vs-state):** the per-cell significance level of 0.05 had no source in the paper. It is now two readings, 0.05 and 0.01.
- **fields-per-cell and gaze-map-landmarks:** the source pointed to paragraph 4 of "What is encoded in hippocampal cell activity"; the sentences are in paragraph 3.
- **gaze-map-landmarks:** the "excess activity" measure is not the paper's. It is now marked as a standard choice and a deviation.
- **spatial-selectivity-fraction:** added a third reading, cells with significant position information among the 111 responsive cells.

The other claims' statements, statistics, expected values and methods hold against the paper.

**Still open**
- **S1 Appendix is missing.** It is a DOCX and is not under `paper/`. Without it, fields-per-cell and dimensionality-control cannot be judged, and the two gaze-behaviour claims rest on the S2 Fig legend alone.
- **Learning-curve method unknown.** The method comes from the paper's reference 60, but the stored text has no reference list, so it cannot be named.
- **landmark-identity-distance:** the paper gives p < 0.001 for 14 of 111 interaction cells, but at a chance rate of 0.05 the value is 0.0013. The chance rate for these counts is unclear; the criterion does not judge this test.
- **No claim for one minor finding:** that gaze was drawn to the rewarded path and the landmarks (Fig 1H). Its method is in S1 Appendix A1.

**Ready:** yes. I marked the file `ready: true`; supplying S1 Appendix would settle the claims that depend on it.

## End of run

21 turns, 3 minutes, $1.07 at API prices, result: success.
