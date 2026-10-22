# 001950 · claims-check · run 39537800060

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001950/ paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; python tools/claims_check.py claims/001950/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001950/*.yaml; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml"
}
```

```
1	# Claims for "Topographic structure and function of locus coeruleus norepinephrine neurons"
2	# (Allen Institute; bioRxiv doi:10.64898/2026.04.10.717727, preprint version 1) on dandiset 001950.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, under
4	# docs/protocol.md as it stands (version pilot-10).
5	#
6	# Text read: the preprint, version 1, full text from the bioRxiv JATS XML (paper/
7	# 10.64898-2026.04.10.717727.txt): Results, Discussion, Methods, the legends of Figures 1 to 6 and
8	# of Supplementary Figures S1 to S18. The supplementary figures exist in this text as legends
9	# only; their panels were not seen. The extraction lost every display equation of the Methods (the
10	# logistic regressions, the Q-learning update, the softmax, the change of choice likelihood, the
11	# drift contrast, the Watson-Wheeler statistic, the permutation p-values) and the contents of
12	# Tables 1 to 3 (injection coordinates and counts, Stan priors). Where these matter the code fixes
13	# them, as noted below. The analysis code's README cites a later version of record (Nature,
14	# doi:10.1038/s41586-026-11026-0), not read here; its figure numbering differs (code Fig. E9 to
15	# E15 are preprint Figs. S12 to S18).
16	#
17	# Code read (Data and code availability; Methods, Data analysis):
18	# - github.com/AllenNeuralDynamics/aind-beh-ephys-analysis, commit 971c1ca (2026-10-05): all in vivo
19	#   physiology and behaviour analyses. Prep scripts in code/beh_ephys_analysis/session_combine/
20	#   figure_preparation (unit tables, go-cue metrics in basic_ephys_generation.py, go-cue and
[... 853 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "offset": 873
}
```

```
873	    t-statistic; within each neuron, trials binned by outcome-window rate into 8 bins; mean change
874	    of choice likelihood per bin (measure readings as in fig6c). The paper gives no test; the
875	    reading of the figure is that the change rises with rate in the reward-excited group (legend
876	    6h) and falls with rate in the no-reward group, judged by the Spearman rho of group means over
877	    the 8 bins. Reproduced when the two rhos have opposite signs with the reward-excited one
878	    positive.
879	- id: fig6i-pl-axons-rpe
880	  statement: LC-NE axonal fluorescence in PL after the choice outcome correlates with RPE (9 mice).
881	  source: Results, Activity of LC-NE projections to frontal cortex correlates with reward prediction
882	    errors, paragraph 4; Figure 6i, 6l
883	  quote: LC-NE axonal activity in frontal cortex 1.5 s after choice outcome correlated with RPE (
884	    Figures 6i–6l )
885	  expected:
886	    quantity: mice with PL photometry
887	    value: 9
888	    tolerance: 0.9
889	  criterion: Photometry as in fig5jk-pl-switch. Windows, readings (a) 0 to 1.5 s after outcome (the
890	    text), (b) 0.2 to 2.2 s after the choice lick (code, Figure 6l). Per session, mean dF/F in the
891	    window binned by RPE into 6 equal-width bins split at 0, z-scored within session (code). The
892	    paper gives no test; the reading of the figure is that the mean over sessions rises with RPE
[... 159 more lines not kept]
```

**Agent**

Checker found 3 p-values it could not locate (fig5g, fig6a, figs12h). Now reading the paper to check each claim.

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "3.0 × 10\|3.40\|switch" paper/*.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '{print NR": "length($0)" "substr($0,1,80)}' paper/*.txt | head -400
```

Result: not kept, because it reads the paper's text.

**Agent**

Reading the Results section (physiology) closely.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.04.10.717727.txt",
 "offset": 11,
 "limit": 220
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.04.10.717727.txt",
 "offset": 11,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.04.10.717727.txt",
 "offset": 131,
 "limit": 100
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Results read. Now the physiology Methods sections.

**Agent calls Bash**

```bash
grep -n "^## " paper/*.txt | awk -F: '$1>400'
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.04.10.717727.txt",
 "offset": 531,
 "limit": 280
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "    go cue (paired t -tests, 240/241 cells, 19 mice; Figures 4e–4h )\n  statistics:\n  - test: paired t-test, per neuron\n    n: 241 neurons, 19 mice\n    p: 0.05\n    p_relation: \"<\"\n  expected:",
 "new_string": "    go cue (paired t -tests, 240/241 cells, 19 mice; Figures 4e–4h )\n  expected:"
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "    Reproduced when the fraction meets tolerance under one reading in the population of the header.\n    The p in statistics is the per-neuron alpha the code uses, which the paper does not print.",
 "new_string": "    Reproduced when the fraction meets tolerance under one reading in the population of the header.\n    The per-neuron alpha of 0.05 is the code's; the paper does not print it."
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "  criterion: The interval is the time between consecutive go-cue onsets minus the 3.0 or 3.1 s trial\n    duration (Methods, \"the times between consecutive cue onsets\"; the reported range starting at\n    1.1 s implies the trial duration is excluded). Readings (a) onset-to-onset minus trial\n    duration, (b) onset to onset, over all sessions.",
 "new_string": "  criterion: The Methods place the intervals \"After the 3.0 or 3.1 s trial duration\" but also call\n    them \"the times between consecutive cue onsets\"; which is meant is open. The reported minimum of\n    1.1 s fits only the time after the trial ends. Readings (a) onset-to-onset minus trial\n    duration, (b) onset to onset, over all sessions."
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "  (code seed 42; the waveform and cross-correlation notebooks use k = 30). The coefficient\n#   vector of the linear model, normalised, is the primary spatial axis.",
 "new_string": "  (code seed 42; the waveform and cross-correlation notebooks use k = 30). The coefficient\n#   vector of the linear model, normalised, is the primary spatial axis.\n# - Directions. The criteria state directions anatomically (dorsal, anterior). In Allen CCFv3 the\n#   DV coordinate grows ventrally and the AP coordinate posteriorly, so a coefficient pointing\n#   dorsally is negative there. The code's printed axes (fig5d) suggest it uses coordinates that\n#   grow dorsally and anteriorly. The author states the convention of the coordinates used, and\n#   for fig5d, fig5h and figs18d projects on the code's axes only in the code's convention."
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Grep**

```json
{
 "pattern": "DV coefficient|dorsally|anteriorly",
 "path": "claims/001950",
 "output_mode": "content"
}
```

```
claims/001950/10.64898-2026.04.10.717727.yaml:93:#   dorsally is negative there. The code's printed axes (fig5d) suggest it uses coordinates that
claims/001950/10.64898-2026.04.10.717727.yaml:94:#   grow dorsally and anteriorly. The author states the convention of the coordinates used, and
claims/001950/10.64898-2026.04.10.717727.yaml:192:    dorsally and spinal-cord-projecting somata ventrally.
claims/001950/10.64898-2026.04.10.717727.yaml:419:    0.05, and the post-peak time increases dorsally (positive DV coefficient). The paper does not
claims/001950/10.64898-2026.04.10.717727.yaml:420:    give the sign of "more symmetric"; readings (a) |slope symmetry| decreases dorsally, (b) slope
claims/001950/10.64898-2026.04.10.717727.yaml:565:    header. Reproduced when the linear model has p < 0.05, the t-statistic increases dorsally
claims/001950/10.64898-2026.04.10.717727.yaml:566:    (positive DV coefficient, ignore-preferring neurons ventral), and the kNN test has p < 0.05;
claims/001950/10.64898-2026.04.10.717727.yaml:648:    Reproduced when the linear model has p < 0.05 with the t-statistic increasing dorsally, under
claims/001950/10.64898-2026.04.10.717727.yaml:778:    dorsally and anteriorly.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "increases dorsally (positive DV coefficient). The paper does not",
 "new_string": "increases dorsally (DV coefficient pointing dorsally, see Directions in the header). The paper does not"
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "    (positive DV coefficient, ignore-preferring neurons ventral), and",
 "new_string": "    (DV coefficient pointing dorsally, see Directions in the header; ignore-preferring neurons\n    ventral), and"
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent**

Now fig6a (direction plus a categorical-label reading), fig6c, figs17, fig6jk and the pupil τ units.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "    Which test gave p = 3.0e-4 is not said; readings (a) linear model, (b) kNN. Reproduced when,\n    under one reading, p < 0.05 and the linear coefficients have the t-statistic increasing\n    dorsally and anteriorly.",
 "new_string": "    Which test gave p = 3.0e-4 is not said; readings (a) linear model, (b) kNN. The legend\n    describes groups (\"excited by reward (cyan) or no reward (pink)\"), so the feature may also be\n    the group label, the sign of the outcome t-statistic among neurons with outcome p < 0.05,\n    in the same two tests (readings (c), (d)). Reproduced when, under one reading, p < 0.05 and\n    the linear coefficients have the feature increasing dorsally and anteriorly (see Directions\n    in the header)."
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "  criterion: Change of choice likelihood (Methods, equation lost) is the likelihood of repeating the\n    current choice, from the logistic choice model, minus the likelihood of the current choice from\n    the Q-learning model, centred per session.",
 "new_string": "  criterion: Change of choice likelihood (Methods, equation lost) is built from the likelihood of\n    repeating the current choice, from the logistic choice model, and the likelihood of the current\n    choice from the Q-learning model, centred per session; the operator is lost with the equation,\n    and the difference (first minus second) is read from the word \"change\"."
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "  statement: LC-NE axon activity in PL before go cues is lower before responded than ignored trials,\n    differing in sign from the single-neuron population (Fisher's exact test with permutation, p =\n    4.2e-4), while",
 "new_string": "  statement: LC-NE axon activity in PL before go cues is lower before responded than ignored trials;\n    the fraction of positive respond-versus-ignore t-statistics differs between axonal\n    fluorescence and single-neuron spiking (Fisher's exact test with permutation, p = 4.2e-4), while"
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "    and the Fisher test of cortex-projecting against other neurons both have p >= 0.05. The code",
 "new_string": "    and the Fisher test of cortex-projecting neurons both have p >= 0.05. The comparison group is\n    open: the legend says \"the population of single neurons\", the Methods \"those that were not\"\n    identified as projecting to cortex; both are run, and the claim of absence holds only if\n    neither test finds the effect under the reading being judged. The code"
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "    open: the legend says \"the population of single neurons\", the Methods \"those that were not\"\n    identified as projecting to cortex; both are run, and the claim of absence holds only if\n    neither test finds the effect under the reading being judged. The code",
 "new_string": "    open: the legend, which reports the test, says \"the population of single neurons\", and the\n    absence is judged on that comparison; the Methods' comparison with neurons not identified as\n    projecting to cortex is shown as a variant. The code"
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "  statement: Regression t-statistics and coefficients of PL axonal activity on chosen value and\n    outcome are more positive than those of the single-neuron population and consistent with RPE\n    (Fisher's exact test, p < 0.01); their angles",
 "new_string": "  statement: Regression t-statistics and coefficients on chosen value and outcome of PL axonal\n    activity (and, per the Results, of single neurons projecting to cortex) are more positive than\n    those of the single-neuron population and consistent with RPE (Fisher's exact test, p < 0.01);\n    the angles of the axonal coefficients"
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "    positive), each PL sessions against single neurons. Reproduced when, under one",
 "new_string": "    positive), each PL sessions against single neurons. The Results name the regressions of\n    cortex-projecting neurons and of axonal dF/F before the comparison, so the first group may also\n    be (iii) PL sessions together with cortex-projecting neurons; Figure 6j and 6k show only the\n    axonal data, so PL sessions alone is the main reading. Reproduced when, under one"
}
```

```
<tool_use_error>String to replace not found in file.
String:     positive), each PL sessions against single neurons. Reproduced when, under one</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "  statement: The autocorrelation of pupil diameter decays exponentially with a time constant of 3.37\n    s on average (SD 1.03).",
 "new_string": "  statement: The autocorrelation of pupil diameter decays exponentially with a time constant of 3.37\n    on average (SD 1.03); the paper gives no unit."
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "    (b) one per neuron recorded with pupil, as the code (106 values). Reproduced when both values\n    are within tolerance under one reading.",
 "new_string": "    (b) one per neuron recorded with pupil, as the code (106 values). The unit of tau is not\n    given; readings (i) seconds, (ii) lags of the 0.5 s window. Reproduced when both values are\n    within tolerance under one combination of readings."
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Grep**

```json
{
 "pattern": "PL sessions against single neurons",
 "path": "claims/001950",
 "output_mode": "content",
 "-B": 2,
 "-A": 2
}
```

```
claims/001950/10.64898-2026.04.10.717727.yaml-929-    PL sessions against all single neurons. No code computes the Fisher test; readings for its
claims/001950/10.64898-2026.04.10.717727.yaml-930-    table (i) sign of the outcome t-statistic, (ii) membership of the RPE quadrant (outcome
claims/001950/10.64898-2026.04.10.717727.yaml:931:    positive, Qc negative), each PL sessions against single neurons. Reproduced when, under one
claims/001950/10.64898-2026.04.10.717727.yaml-932-    combination, Fisher p < 0.01 with PL sessions more often positive (or RPE-like), and the
claims/001950/10.64898-2026.04.10.717727.yaml-933-    Watson-Wheeler permutation p < 0.05.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "each PL sessions against single neurons. Reproduced when, under one\n    combination,",
 "new_string": "each PL sessions against single neurons. The Results name the regressions of\n    cortex-projecting neurons and of axonal dF/F before the comparison, so the first group may also\n    be (iii) PL sessions together with cortex-projecting neurons; Figure 6j and 6k show only the\n    axonal data, so PL sessions alone is the main reading. Reproduced when, under one\n    combination,"
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "    be (iii) PL sessions together with cortex-projecting neurons; Figure 6j and 6k show only the\n    axonal data, so PL sessions alone is the main reading. Reproduced",
 "new_string": "    be PL sessions together with cortex-projecting neurons (reading (iii), with table (i) or (ii));\n    Figure 6j and 6k show only the axonal data. Reproduced"
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "p < 0.05 with the t-statistic increasing dorsally, under\n    one reading.",
 "new_string": "p < 0.05 with the t-statistic increasing dorsally (see\n    Directions in the header), under one reading."
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent**

Edits done: fig4g, task-iti, the direction conventions, fig6a, fig6c, figs17, fig6jk and figs16 τ. Adding the `checks` entry and re-running the checker.

**Agent calls Bash**

```bash
cat >> claims/001950/10.64898-2026.04.10.717727.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig4g-go-cue-excitation, removed the statistics entry (p < 0.05 per neuron); it is the threshold used to count neurons, not a result, and the paper does not print it.
  - task-iti, the criterion asserted that the interval excludes the trial; the Methods both place the intervals after the trial and call them the times between cue onsets, so this is now named as open, with both readings kept.
  - header and fig5c, fig5g, fig6a, figs14 criteria, "positive DV coefficient" was used for dorsal; in Allen CCFv3 the DV coordinate grows ventrally, so directions are now stated anatomically, with a header note on coordinate conventions, including the code's axis vectors for fig5d, fig5h and figs18d.
  - fig6a-reward-dorsal-anterior, the legend describes groups of neurons excited by reward or by no reward, so readings with the group label as the spatial feature were added.
  - fig6c-rpe-choice-change, the criterion gave "minus" as the Methods' operator, but the equation is lost; it now says the difference is read from the word "change".
  - figs17-respond-ignore-axons, the statement said axons differ "in sign" from single neurons; both are higher before ignored trials, and the paper reports only a difference in the fraction of positive t-statistics, so the statement now says that.
  - figs17-respond-ignore-axons, the comparison group for cortex-projecting neurons was given as other neurons; the legend that reports the test says the population of single neurons, so the absence is judged on that, and the Methods' comparison with non-projecting neurons is a variant.
  - fig6jk-pl-axons-more-rpe, the Results compare both cortex-projecting neurons and axonal dF/F with the population; the statement now names both, and the criterion adds the reading with cortex-projecting neurons in the first group.
  - figs16-pupil-autocorrelation, the paper gives tau no unit; the statement no longer says seconds, and the criterion reads it as seconds or as 0.5 s lags.
  - Open, the checker reports VALUE NOT FOUND for p = 3.0e-4 (fig5g, fig6a) and 3.40e-5 (figs12h); all three are in the text, printed as "3.0 × 10 −4" and "3.40 × 10 −5", so the problem is in how the checker matches them.
  - Open, code details cited in the criteria (windows, permutation counts, k = 30, populations, axis vectors) were not checked against the repositories, which are not in this checkout; they are taken as the claims author recorded them.
  - Open, minor anatomical results without a claim (cortical co-projection to nearby regions, Figure S4d to S4g; dendrite orientation, Figure S6); they are not main findings and not tested by this dandiset.
EOF
python tools/claims_check.py claims/001950/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001950/10.64898-2026.04.10.717727.yaml",
 "old_string": "    open: the legend, which reports the test,",
 "new_string": "    open. The legend, which reports the test,"
}
```

```
The file claims/001950/10.64898-2026.04.10.717727.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
grep -nE '^\s+[^#-].*: ' claims/001950/*.yaml | grep -vE '^\S+:\s*[0-9]+:\s+(- )?[a-z_]+: ' | head; python tools/claims_check.py claims/001950/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

## Check of `claims/001950/10.64898-2026.04.10.717727.yaml`

**Checker result:** `44 claims, 44 quotes, 40 statistical values, 3 problems`

The 3 problems are all VALUE NOT FOUND, for p = 3.0e-4 (fig5g, fig6a) and 3.40e-5 (figs12h). All three are in the paper text, printed as "3.0 × 10 −4" and "3.40 × 10 −5", so the fault is in how the checker matches these numbers, not in the file. The statistical value count went from 41 to 40 because I removed one threshold entry from fig4g.

**Changes, by claim:**
- **fig4g-go-cue-excitation:** removed the `statistics` entry (p < 0.05 per neuron). It is the threshold used to count neurons, not a result, and the paper does not print it.
- **task-iti:** the criterion stated as fact that the interval excludes the trial. The Methods say both "after the 3.0 or 3.1 s trial" and "the times between consecutive cue onsets", so it is now named as open, with both readings kept.
- **Header, plus fig5c, fig5g, fig6a and figs14:** "positive DV coefficient" was used to mean dorsal, but in Allen CCFv3 the DV coordinate grows ventrally. Directions are now stated anatomically, and a header note on coordinate conventions also covers the code's axis vectors used in fig5d, fig5h and figs18d.
- **fig6a-reward-dorsal-anterior:** the legend describes groups of neurons, so I added readings that use the group label (excited by reward or by no reward) as the spatial feature.
- **fig6c-rpe-choice-change:** the criterion gave "minus" as the Methods' operator, but that equation was lost from the text. It now says the difference is read from the word "change".
- **figs17-respond-ignore-axons:**
  - The statement said axons and single neurons differ "in sign". Both have higher activity before ignored trials, and the paper reports only that the fraction of positive t-statistics differs. The statement now says that.
  - The comparison group for cortex-projecting neurons is now the legend's "population of single neurons". The Methods' comparison with non-projecting neurons is kept as a variant.
- **fig6jk-pl-axons-more-rpe:** the Results compare both cortex-projecting neurons and axonal dF/F with the single-neuron population. The statement now names both, and the criterion has a reading that includes cortex-projecting neurons.
- **figs16-pupil-autocorrelation:** the paper gives τ no unit. "s" is removed from the statement, and the criterion reads τ either as seconds or as lags of the 0.5 s window.

**Still open:**
- The checker's three p-value misses, described above.
- I did not check the code details the criteria cite (windows, permutation counts, k = 30, populations, axis vectors) against the code repositories, because they are not in this checkout. They stand as the claims author recorded them.
- Two minor anatomical results have no claim: cortical co-projection to nearby regions (Figures S4d to S4g) and dendrite orientation (Figure S6). They are not main findings, and this dandiset cannot test them.

All other quotes, sources, statistics and expected values matched the paper. Each main finding of the abstract and Results has a claim.

**Ready:** yes. The `checks` entry at the end of the file has `ready: true`. Nothing is committed.

## End of run

36 turns, 3 minutes, result: success.
