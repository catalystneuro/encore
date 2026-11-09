# 000637 · claims-check · run 39909541947

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/000637/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 96,200p docs/protocol.md
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
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/000637/*.yaml; python tools/claims_check.py claims/000637/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000637/*.yaml paper/*.txt | tail -30; wc -l claims/000637/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.2218-24.2025.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.2218-24.2025.txt",
 "offset": 326,
 "limit": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes (31 claims, 0 problems). One thing to note already: the paper's data statement points to dandiset 000946, not 000637. Now reading the claims file.

**Agent calls Read**

```json
{
 "file_path": "claims/000637/10.1523-jneurosci.2218-24.2025.yaml"
}
```

```
1	# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23):e2218242025, on dandiset 000637.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record as served by PubMed Central (PMC12139594), full text with
6	# Materials and Methods, Results, figure legends and Discussion (paper/10.1523-jneurosci.2218-24.2025.txt).
7	# The paper has no supplement. No PDF was supplied. The equation defining the directional spike time
8	# tiling coefficient (dSTTC) is lost in the text ("The definition for dSTTC is as follows:" is followed
9	# by the prose that defines its terms, without the formula); its form is treated as open below.
10	# The paper links no analysis code (no repository and no code availability statement in the text),
11	# so no code was read.
12	#
13	# Data the paper used (Materials and Methods). Male Wistar rats (Hsd WI), 250 to 350 g, 3 to 6 months,
14	# under 2% isoflurane. Group 1 (N = 16): two 32-channel NeuroNexus probes, one in S1 (AP -2, ML 2.5,
15	# 40 degrees, 1 to 1.3 mm deep, layers III to V) and one in POm (AP -4.5, ML 2.6, 20 degrees, 5.8 mm).
16	# Group 2 (N = 12, auditory confound): probes in S1 and auditory cortex (AC; AP -4.5, ML 6.5).
17	# tFUS from a 128-element random array (H276, 1.5 MHz) steered to S1; ultrasound duration (UD) 67 ms;
18	# intersonication interval 2.5 s with 10% jitter; 500 trials per parameter; condition order randomized.
19	# Conditions: PRF 30, 300, 1500, 3000 and 4500 Hz at constant 200 us pulse duration (which gives DC 0.6,
20	# 6, 30, 60 and 90%); DC 0.6, 6, 30, 60 and 90% at 3000 Hz and at 30 Hz PRF; PRFs at constant 60% DC;
[... 970 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000637/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "# signed-rank; the Bonferroni count is (M1) the number of conditions or windows in the panel each tested\n# against baseline, or (M2) the number of all pairs among them and baseline. The tail is the direction",
 "new_string": "# signed-rank; the rates compared are (R1) the raw spike rates in the two windows, or (R2) the normalized\n# rates, the baseline then being 100% for every unit (the Methods normalize before testing and do not say\n# which); the Bonferroni count is (M1) the number of conditions or windows in the panel each tested\n# against baseline, or (M2) the number of all pairs among them and baseline. The tail is the direction"
}
```

```
The file claims/000637/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000637/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "# fractions taken within the window; a trial where either unit has no spike in the window gives no value.",
 "new_string": "# fractions taken within the window. A trial where either unit has no spike in the window is open, as\n# the paper does not say: (E1) it gives no value, as the STTC is undefined then (Cutts and Eglen 2014), or\n# (E2) it gives 0. E1 and E2 apply to Method T too."
}
```

```
The file claims/000637/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000637/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    and that the highest response is at 1500 Hz, so the reading taken is 1500 Hz and above (the paper's Discussion\n    paragraph on parameters says POm delayed activity is inclined to 1500 Hz); 3000 and 4500 Hz alone is shown as\n    a variant. Reproduced when, under every reading of Method S, the Kruskal-Wallis across PRFs has p < 0.01, 1500,\n    3000 and 4500 Hz are significantly above baseline, and the highest mean is at 1500 Hz within tolerance; partially",
 "new_string": "    and that the highest response is at 1500 Hz, so the reading taken is 1500 Hz and above (Results, tFUS parameters\n    on affecting neuronal activities of CTC pathway, paragraph 2, says the delayed activities of POm RSUs were inclined\n    to 1500 Hz); 3000 and 4500 Hz alone is shown as a variant. Reproduced when, under every reading of Method S, the\n    Kruskal-Wallis across PRFs has p < 0.01, 1500, 3000 and 4500 Hz are significantly above baseline while 30 and\n    300 Hz are not, and the highest mean is at 1500 Hz within tolerance; partially"
}
```

```
The file claims/000637/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000637/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    rates, Bonferroni over the 10 pairs. The direction",
 "new_string": "    rates. The Bonferroni count is not given and is open, (B1) the 10 pairs among the five PRFs or (M2) the\n    15 pairs among them and baseline. The direction"
}
```

```
The file claims/000637/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000637/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    D1 and D2 and K1 and K2, the Kruskal-Wallis across PRFs has p < 0.05 and the two largest median changes are\n    at 1500 and 3000 Hz; partially",
 "new_string": "    D1 and D2 and K1 and K2, the Kruskal-Wallis across PRFs has p < 0.05 and the two largest changes are at 1500\n    and 3000 Hz, by the mean and by the median change (the paper does not say which it compares); partially"
}
```

```
The file claims/000637/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000637/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    D1 and D2 and K1 and K2, the Kruskal-Wallis across DCs at 30 Hz has p < 0.05 with the median changes at 6, 30\n    and 60% each above those at 0.6 and 90%, and",
 "new_string": "    D1 and D2 and K1 and K2, the Kruskal-Wallis across DCs at 30 Hz has p < 0.05 with the changes at 6, 30 and\n    60% each above those at 0.6 and 90%, by the mean and by the median change (the paper does not say which), and"
}
```

```
The file claims/000637/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000637/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    on their trial event times: one-tailed post hoc Wilcoxon test for an increase against baseline at corrected\n    p < 0.01 in the 0 to 67 ms and 201 to 268 ms windows, for the four groups. Reproduced when none of the eight\n    tests is significant; not reproduced when any is.",
 "new_string": "    on their trial event times: one-tailed post hoc Wilcoxon test against baseline at corrected p < 0.01 in the\n    0 to 67 ms and 201 to 268 ms windows, for the four groups, testing both an increase and a decrease (the paper\n    states no change and not the tail). Reproduced when none of these tests is significant; not reproduced when\n    any is."
}
```

```
The file claims/000637/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000637/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "CG1 control sessions. Reproduced when none\n    of the eight tests is significant at corrected p < 0.01; not reproduced when any is.",
 "new_string": "CG1 control sessions, both tails. Reproduced\n    when none of the tests is significant at corrected p < 0.01; not reproduced when any is."
}
```

```
The file claims/000637/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000637/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    two-sample Wilcoxon tests on units' normalized rates (W1 only, as units differ between sessions). Reproduced",
 "new_string": "    two-sample Wilcoxon tests on units' normalized rates (W1 only, as units differ between sessions), Bonferroni\n    over (B1) the 10 pairs among the five DCs or (M2) the 15 pairs among them and baseline, as the count is not\n    given. Reproduced"
}
```

```
The file claims/000637/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat >> claims/000637/10.1523-jneurosci.2218-24.2025.yaml <<'EOF'
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Method S, added readings R1 (raw rates) and R2 (normalized rates, baseline 100%) for the test against baseline, since the Methods normalize before testing and do not say which rates the Wilcoxon test compares.
  - Method D, the handling of trials where a unit has no spike in the window was a choice made by the writer; it is now open (E1 no value, E2 zero), for Methods D and T, as the paper does not say.
  - fig6c-pom-rsu-delayed, the support for reading 1500 Hz and above was cited to the Discussion; the sentence is in Results, tFUS parameters, paragraph 2. Added that 30 and 300 Hz are not significant, as the statement (responses induced from 1500 Hz up) implies and as the other PRF claims require.
  - fig9a-s1-rsu-60dc, the Bonferroni count of 10 pairs was a choice made by the writer; the paper gives no count, so the readings are 10 pairs among PRFs or 15 with baseline.
  - fig7d-pom-fsu-dc-3000, the same open Bonferroni count for the between-DC tests is now named (10 or 15 pairs).
  - fig10d-sttc-60dc and fig10ef-sttc-dc, median change was a choice made by the writer; the paper does not say whether it compares means or medians, so both must agree.
  - fig5-sham-no-response and fig5-cg1-control-no-response, tested an increase only; the paper states no change and no tail, and fig4-fsu-no-change tests both, so both tails are now tested.
  - Open, the paper says its data are in DANDI:000946, and the description of 000637 (S1 only, pulse durations 100, 200 and 400 us) may not match this paper's recordings; the author must establish which conditions, if any, the dataset holds.
  - Open, the dSTTC formula is missing from the text and no PDF was supplied; the form taken from the STTC of Cutts and Eglen (2014) is a reading.
  - Open, the Discussion's statement that 3000 Hz with 90% DC decreases local activity (Fig. 7) has no claim of its own; fig7a only requires 90% not to be significant.
  - Open, the reproduction grades (for example 10 of 12 counts in unit-counts, partially reproduced bands) are the writer's rules, not the paper's.
EOF
python tools/claims_check.py claims/000637/*.yaml paper/*.txt | tail -3; grep -n ": .*: " claims/000637/*.yaml | sed -n '/^9[89][0-9]\|^1[0-9][0-9][0-9]/p' | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file for DANDI:000637 is fit for an attempt (`ready: true`) after the corrections below. I left one problem open that the author must settle first: the paper puts its data in a different dandiset, DANDI:000946.

**Checker result:** `31 claims, 31 quotes, 84 statistical values, 0 problems`, before and after my edits.

**Changes, by claim**
- **Method S** (shared spiking method): the paper doesn't say whether the Wilcoxon test against baseline compares raw rates or normalized rates (where the baseline is 100% for every unit). Both are now named as readings.
- **Method D** (and Method T): the writer had decided on their own what to do with trials where a unit has no spike in the window. This is now open, with two readings: the trial gives no value, or it gives 0.
- **fig6c-pom-rsu-delayed**: the supporting sentence was cited to the Discussion, but it is in Results, tFUS parameters, paragraph 2. I also added that 30 and 300 Hz must not be significant, since the statement implies it and the other PRF claims require the same.
- **fig9a-s1-rsu-60dc** and **fig7d-pom-fsu-dc-3000**: the writer chose to Bonferroni-correct over 10 pairs, but the paper gives no count. Now open, with two readings: 10 pairs, or 15 including baseline.
- **fig10d-sttc-60dc** and **fig10ef-sttc-dc**: the writer chose median change, but the paper doesn't say whether it compares means or medians. The result must now hold under both.
- **fig5-sham-no-response** and **fig5-cg1-control-no-response**: these tested only for an increase. The paper says "no change" without naming a tail, and fig4-fsu-no-change already tests both, so both tails are now tested.

**Open**
- **Dataset mismatch:** the dataset description of 000637 lists S1 recordings only, with pulse durations of 100, 200 and 400 us. That may not match this paper's recordings. The author has to establish which conditions, if any, the dataset holds.
- **dSTTC formula:** the equation is missing from the text and there is no PDF. The form used is reconstructed from the STTC of Cutts and Eglen (2014).
- **Discussion finding with no claim:** the Discussion says 3000 Hz with 90% DC lowers local activity (Fig. 7). No claim covers it; fig7a only requires 90% not to be significant.
- **Grading rules:** the cut-offs for reproduced and partially reproduced (for example 10 of 12 counts in unit-counts) were set by the writer, not taken from the paper.

All other statements, quotes, statistics, expected values and tolerances matched the paper. The paper's main findings each have a claim, and no claim draws on another source. Nothing was committed or pushed.

## End of run

18 turns, 3 minutes, result: success.
