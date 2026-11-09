# 000139 · claims-check · run 40755659922

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000139/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 100,220p docs/protocol.md
```

```
- `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
     Methods, the figure legends, the supplement, or the code the paper
     links, and the criterion says which. Search all of them before
     treating a detail as open.
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000139/*.yaml; python tools/claims_check.py claims/000139/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml"
}
```

```
1	# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000139.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol as stated in docs/protocol.md (version pilot-12).
4	#
5	# Text read: the NIH author manuscript in PubMed Central (PMC2991102), as extracted to
6	# paper/10.1016-j.neuron.2010.09.015.txt, with its Results, Methods, figure legends and the one
7	# supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1 to 5, Supplemental Text and
8	# Supplemental Experimental Procedures). Not the version of record. The figures themselves are not
9	# in the text; values plotted only in Figures 4, 6 and 7 are not available and no claim rests on
10	# them. The paper links no code, so every method below comes from the Methods, the legends or the
11	# supplement.
12	#
13	# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
14	# Procedures). Three adult male rhesus monkeys (A, B, J), delayed reaches from a central touch spot
15	# to a target on a fronto-parallel screen. Trial events: target onset (the target jitters), go cue
16	# (jitter stops and the touch spot disappears), movement onset. Delays about 0 to 1000 ms; only
17	# trials with delays above 400 ms analysed. Four datasets. Monkeys A and B, speed task, 28
18	# conditions (7 directions, 2 distances, 2 instructed speeds), single electrodes, 64 and 74
19	# single units. Monkey J, maze task, single electrodes, 172 single units, recorded on four sets of
20	# 27 conditions each (about 53 neurons per set; population analyses done per set, then averaged).
[... 449 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000139/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt | tail -20; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2010.09.015.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1016-j.neuron.2010.09.015.txt').read()
print(t[58000:82000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1016-j.neuron.2010.09.015.txt').read()
i=t.find('=== page 4 ===')
import re
s=t[i:]
print(s[:30000])"
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes (22 claims, 0 problems). I've read the paper and supplement and am now making the corrections.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "#   PD performance). S is fixed for all folds (Methods, \"The matrix S is the same for every\n#   neuron\"); only the regression leaves the condition out. Whether the variance uses c or c - 1\n#   is a standard choice that cannot change any comparison between spaces.",
 "new_string": "#   PD performance). Open: whether a PCA-based S is recomputed without the left-out condition.\n#   The Methods say only that the PD is found from the remaining conditions (\"The matrix S is the\n#   same for every neuron\" concerns neurons, not folds). Readings (a) S computed once from all\n#   conditions and only the regression leaves the condition out, (b) the PCA redone on the\n#   remaining conditions and the left-out condition projected onto its components. Whether the\n#   variance uses c or c - 1 is a standard choice that cannot change any comparison between spaces."
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    0.231) but outside tolerance. The number of neurons kept is reported.\n- id: fig4abc-mean-correlation-other-datasets",
 "new_string": "    0.231) but outside tolerance. The number of neurons kept is reported.\n- id: fig4abc-mean-correlation-other-datasets"
}
```

```
<tool_use_error>No changes to make: old_string and new_string are exactly the same.</tool_use_error>
```

**Agent**

Now the claim edits.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "  - quantity: mean r, monkey J\n    value: 0.06\n    tolerance: 0.006\n  criterion:",
 "new_string": "  - quantity: mean r, monkey J\n    value: 0.06\n    tolerance: 0.006\n  - quantity: mean Spearman r, monkey A\n    value: 0.20\n    tolerance: 0.02\n  - quantity: mean Spearman r, monkey B\n    value: 0.20\n    tolerance: 0.02\n  - quantity: mean Spearman r, monkey J\n    value: 0.06\n    tolerance: 0.006\n  criterion:"
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    centred near zero, with little sign of separate populations of concordant (r near 1) and\n    opposing (r near -1) tuning.",
 "new_string": "    centred near zero, with little sign of separate populations of concordant (r near 1) and\n    opposing (r near -1) tuning, except perhaps weakly for monkey B (Figure 4B)."
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "  criterion: Per neuron, the preparatory rate vector correlated with the vector of\n    condition-mean rates at each single time point of the movement-locked trace (20 ms Gaussian,\n    Figure 4E legend) from 400 ms before to 100 ms after movement onset, averaged over neurons.\n    Open, the neurons;",
 "new_string": "  criterion: Per neuron, the preparatory rate vector correlated with the vector of\n    condition-mean rates at each single time point (20 ms Gaussian, Figure 4E legend), averaged\n    over neurons. The trace is the one spliced from the go-cue-locked and movement-locked means\n    (Supplemental Experimental Procedures, Computing the mean firing rate, which names Figure 4E);\n    where the splice falls is not given. Open, the time range, which the paper does not give\n    beyond starting where preparatory tuning is correlated with itself (Figure 4E legend);\n    readings (a) the spliced trace from the preparatory window through 100 ms after movement\n    onset, (b) the movement-locked trace alone from 400 ms before to 100 ms after onset. Open, the\n    neurons;"
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    value at 400 ms before onset) between 300 and 100 ms before onset, a window read from the\n    paper's \"∼200 ms\". The curve is shown.",
 "new_string": "    value at 400 ms before onset) between 300 and 100 ms before onset, a window read from the\n    paper's \"∼200 ms\". The 10% rule and the 300 to 100 ms window are readings; the paper gives\n    neither. The curve is shown."
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    task space, under every reading of the kinematic window and replication; not reproduced",
 "new_string": "    task space, under every reading of the kinematic window and replication and of whether S is\n    recomputed in each fold (opening comment); not reproduced"
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    Reproduced when, for the peri-movement space, performance at the best k is above that at k =\n    1, the best k is between 2 and 10,",
 "new_string": "    \"Middle range\" is read as a best k between 2 and 10 (a reading; the paper gives no range).\n    Reproduced when, for the peri-movement space, performance at the best k is above that at k =\n    1, the best k is between 2 and 10,"
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the maze task spaces, preparatory dimensionality and Figure 7C claims.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "  statement: For the maze task, the segment directions and initial velocity task spaces perform\n    reasonably well, while the endpoints + maximum speed space does not perform well.\n  source: Results, PD performance in a variety of spaces, paragraphs 1 and 2; Figure 6C and 6D",
 "new_string": "  statement: Segment directions and initial velocity are among the task spaces that perform\n    reasonably well, segment directions doing so for the maze task, while for the maze task the\n    endpoints + maximum speed space does not perform well.\n  source: Results, PD performance in a variety of spaces, paragraphs 1 and 2; Figure 6C and 6D;\n    Figure 7D legend"
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "  criterion: Task-space performances from fig6d-perimovement-best-j-array. \"Reasonably well\" is\n    read from the Figure 6 legend sense, performance above zero (\"Points above zero indicate\n    performance considerably better than chance\").",
 "new_string": "  criterion: Task-space performances from fig6d-perimovement-best-j-array. The Results list the\n    spaces that performed reasonably well without saying for which datasets; the Figure 7D legend\n    says segment directions performed well for the maze task. That initial velocity does so for\n    the maze task is a reading. \"Reasonably well\" is read as performance above zero (Results, PD\n    performance in a variety of spaces, paragraph 1, \"Points above zero indicate performance\n    considerably better than chance\")."
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "  criterion: PCA of the c by n matrix of condition-mean preparatory rates of all neurons kept for\n    the PD analyses. The reported range",
 "new_string": "  criterion: PCA of the c by n matrix of condition-mean preparatory rates (Supplemental\n    Experimental Procedures, Estimating the upper limit of PD performance, \"each row containing\n    the mean preparatory activity for every neuron\"). Open, the neurons; readings (a) those kept\n    for the PD analyses (preparatory tuning threshold), (b) every recorded unit. Open, whether\n    rates are normalized before the PCA; the paper does not say. Readings (a) not normalized, as\n    for the peri-movement T-matrix (Methods, PCA-based spaces), (b) each neuron scaled to unit\n    range. The reported range"
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    in ap-location-no-effect-j-array. The paper averages over datasets. Reproduced when both\n    halves have normalized performance above zero and within 10% of the random halves' value;\n    which half is higher is reported.",
 "new_string": "    in ap-location-no-effect-j-array. The paper averages over datasets. \"Only slightly different\"\n    is read as within 10% of the random halves' value (a reading; the paper gives no value).\n    Reproduced when both halves have normalized performance above zero and within 10% of the\n    random halves' value, and the anterior half is higher than the posterior; partially\n    reproduced when the first two hold and the posterior half is higher."
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now I'll add the missing control claim and the checks entry.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    fraction is reported.\n- id: fig8-linear-dynamics-simulation",
 "new_string": "    fraction is reported.\n- id: high-dimensional-task-spaces-underperform\n  statement: The high-dimensional task spaces, including the kitchen-sink space, always perform\n    below the peri-movement space, so high dimensionality alone does not explain its performance.\n  source: Results, Controls, paragraph 2; Methods, Task spaces\n  quote: the high-dimensional task spaces (including the gratuitously high-dimensional\n    'kitchen-sink' space) always underperformed the peri-movement space\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: Task-space and peri-movement performances of fig6d-perimovement-best-j-array. For the\n    maze task the kitchen-sink space is 11-D (Methods, Task spaces). Open, which spaces count as\n    high-dimensional and what they are compared with; readings (a) the kitchen-sink (11-D) and\n    segment directions (6-D) spaces against the peri-movement space at the same k, (b) the same\n    spaces against the best peri-movement performance over k. Reproduced when every such space is\n    below the peri-movement space under a reading.\n- id: fig8-linear-dynamics-simulation"
}
```

```
The file claims/000139/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat >> claims/000139/10.1016-j.neuron.2010.09.015.yaml <<'EOF'
checks:
- date: 2026-10-28
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Opening comment, PD model. The file said S is fixed across cross-validation folds and cited "The matrix S is the same for every neuron", which concerns neurons, not folds; the Methods do not say whether a PCA-based S is recomputed without the left-out condition, so this is now named as open with two readings, and fig6d-perimovement-best-j-array requires its outcome under both.
  - fig4abc-mean-correlation-other-datasets. Added the three Spearman means the statement gives (0.20, 0.20, 0.06) as expected values with 10% tolerance, from Results, Correlations, paragraph 1.
  - fig4-broad-unimodal. The statement now keeps the paper's exception ("except perhaps weakly in panel B"), which it had dropped.
  - fig4e-correlation-time-course. The time range of 400 ms before to 100 ms after movement onset was given as if from the legend; the paper does not give it. The criterion now cites the spliced trace of the Supplemental Experimental Procedures (which names Figure 4E), names the range as open with two readings, and marks the 10% decline rule and the 300 to 100 ms window as readings.
  - fig6-dimensionality-peak. Marked "middle range" read as best k from 2 to 10 as a reading; the paper gives no range.
  - fig6-maze-task-spaces. The paper lists the spaces that performed reasonably well without tying them to the maze task; the statement now says so, cites the Figure 7D legend for segment directions on the maze task, and the criterion names initial velocity on the maze task as a reading. The above-zero sentence was attributed to the Figure 6 legend; it is in the Results, and the citation is corrected.
  - fig6-preparatory-dimensionality. The Supplemental Experimental Procedures say "every neuron" and do not say whether rates are normalized; both are now named as open with readings.
  - fig7c-anterior-posterior-performance. The statement says anterior sites perform slightly better but the criterion did not test it; it now requires it for reproduced (partially reproduced otherwise), and marks the 10% band for "only slightly different" as a reading.
  - Added high-dimensional-task-spaces-underperform, a control finding in Results, Controls, paragraph 2 that had no claim.
  - Open, not settled. The paper links no code, so the tuning-strength measure, the movement-onset rule, the proto-trial, the kinematic window end, the Figure 4E time range and the test of the mean correlation remain readings; the attempt must run each as the criteria say.
  - Open, not settled. The paper gives 2166 (Results) and 2155 (Methods) mean trials per neuron for J-array; the file accepts either and reports the count only.
  - Checked that no claim draws on paper/10.1038-nature11129.txt, another paper in the folder.
EOF
python tools/claims_check.py claims/000139/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/000139/10.1016-j.neuron.2010.09.015.yaml; grep -n "—\|rather" $f; sed -n '/^checks:/,$p' $f | grep -n '[^:]: .*: '; git status --short
```

```
M claims/000139/10.1016-j.neuron.2010.09.015.yaml
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
?? scripts
```

**Agent**

I've finished checking the claims file against the paper, and it is ready for an attempt. Nothing is committed.

**Checker:** `claims/000139/10.1016-j.neuron.2010.09.015.yaml: 23 claims, 23 quotes, 9 statistical values, 0 problems` (it was 22 claims before I added one).

**Changes, by claim:**
- **Opening comment, PD model:** the file said the PCA-based spaces stay fixed across the leave-one-out folds. It cited "The matrix S is the same for every neuron", but that sentence is about neurons, not folds. Whether the PCA is redone without the left-out condition is now listed as open, with two readings. `fig6d-perimovement-best-j-array` now needs its result to hold under both.
- **fig4abc-mean-correlation-other-datasets:** added the Spearman means from the statement (0.20, 0.20, 0.06) as expected values with 10% tolerance.
- **fig4-broad-unimodal:** the statement now keeps the paper's exception for monkey B ("except perhaps weakly in panel B").
- **fig4e-correlation-time-course:** the window of 400 ms before to 100 ms after movement onset is not in the paper. The criterion now cites the spliced firing-rate trace from the supplement and lists the time range as open, with two readings. It also marks the 10% decline rule and the 300 to 100 ms window as readings, not the paper's values.
- **fig6-dimensionality-peak:** "middle range", read as a best k of 2 to 10, is now marked as a reading.
- **fig6-maze-task-spaces:**
  - The paper lists the spaces that performed reasonably well without saying for which task. The statement now says this, and cites the Figure 7D legend for segment directions on the maze task.
  - Initial velocity on the maze task is marked as a reading.
  - The "points above zero" sentence was credited to the Figure 6 legend; it is in the Results, and the citation is fixed.
- **fig6-preparatory-dimensionality:** the supplement says "every neuron" and does not say whether rates are normalized. Both are now open, with readings.
- **fig7c-anterior-posterior-performance:** the statement says anterior sites do slightly better, but the criterion never tested it. It now requires it for "reproduced" and gives "partially reproduced" otherwise. The 10% band for "only slightly different" is marked as a reading.
- **New claim, `high-dimensional-task-spaces-underperform`:** the Controls finding that the high-dimensional task spaces, including kitchen-sink, always did worse than the peri-movement space had no claim.

The other claims stand as written. No claim draws on the other paper in `paper/` (nature11129).

**Still open (recorded under `checks`):**
- The paper links no code, so these stay as readings the attempt must run in each form:
  - how tuning strength is measured
  - how movement onset is detected
  - what the reference "proto-trial" is
  - where the kinematic window ends
  - the Figure 4E time range
  - which test was used for the mean correlation
- The paper gives two J-array trial counts, 2166 (Results) and 2155 (Methods). The file accepts either and only reports the count.

**Ready:** yes. The checks entry is recorded with `ready: true`.

## End of run

24 turns, 2 minutes, result: success.
