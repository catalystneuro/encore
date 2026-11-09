# 000128 · claims-check · run 39809594552

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000128/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; cat claims/000128/*.yaml; python tools/claims_check.py claims/000128/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/918ee474-61d4-47bf-87c7-c18ae969003e/tool-results/be1rofs78.txt"
}
```

```
1	   - `expected`: each reported number the claim rests on, with a tolerance.
2	     Use the paper's own uncertainty when it gives one (a confidence
3	     interval, or the stated spread); otherwise 10% of the reported value.
4	     For a reported range ("2 to 13%"), the claim holds inside the range
5	     widened by 10% of each bound. Give the reason for any other tolerance.
6	   - `criterion`: how the claim will be judged, for any claim that is not
7	     settled by its expected values alone ("similar", "many", "tended to").
8	     It is written from the paper alone, before anyone analyses the data.
9	   - When a reported number can be read in more than one way (which trials
10	     form the denominator, which subset is meant), list in the criterion the
11	     readings the paper's text plausibly allows, before the analysis. The
12	     claim is reproduced if the result matches under any of them. The
13	     notebook shows every reading, the notes say which ones match, and the
14	     ambiguity is recorded as a deviation.
15	   - Methods come from the paper, never from the author. Every part of a
16	     criterion's method (the selection, the measure, the test, windows,
17	     bins, thresholds, what a measure is compared with) is taken from the
18	     Methods, the figure legends, the supplement, or the code the paper
19	     links, and the criterion says which. Search all of them before
20	     treating a detail as open.
[... 583 more lines not kept]
```

**Agent**

Checker: 21 claims, 0 problems. Now the paper.

**Agent calls Bash**

```bash
wc -l paper/*.txt; grep -n "Results\|Methods\|^Discussion\|EXPERIMENTAL\|Supplement" paper/10.1016-j.neuron.2010.09.015.txt | head -50
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
i=t.find('D. PD consistency for the peri-movement')
print(t[i:i+46000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1016-j.neuron.2010.09.015.txt').read()
i=t.find('This work was supported by a Helen')
j=t.find('Supplement',i)
print(i,j,len(t))
k=t.find('Supplemental Experimental Procedures',i)
print(k)
print(t[j-200:j+300])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1016-j.neuron.2010.09.015.txt').read()
print(t[79035:])" > $TMPDIR/supp.txt; wc -c $TMPDIR/supp.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp.txt"
}
```

```
1	Supplement: NIHMS240235-supplement-01.pdf
2	
3	=== page 1 ===
4	Inventory of Supplemental Information 
5	 
6	Supplemental Figure 1. Population PSTHs.  
7	This figure relates to the interpretation of Figure 4 of the main text, and is briefly 
8	discussed in the main text. 
9	 
10	 
11	Supplemental Figure 2. Illustration of how PCA is used to assign each condition a 
12	location in a space based on the population peri-movement responses.  
13	This figure relates to Figure 5 of the main text, and visually illustrates some 
14	mathematical procedures. 
15	 
16	 
17	Supplemental Figure 3. Array locations in monkey J.  
18	A figure showing our recording locations. Referred to in the Experimental 
19	Procedures. 
20	 
[... 564 more lines not kept]
```

**Agent**

The checker passes. I've read the full paper and supplement and am now checking the schema for fields the file may be missing, such as `data`.

**Agent calls Bash**

```bash
ls tools schema* 2>/dev/null; grep -n "data\b\|\"data\"\|'data'\|with_labels\|elsewhere\|checks" tools/claims_check.py | head -30; ls claims | head; grep -l "^  data:" claims/*/*.yaml | head -3
```

```
schemas:
attempt.schema.json
claims.schema.json
entry.schema.json

tools:
__pycache__
agent_run.py
archive_transcripts.sh
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
notify.py
papers_manifest.py
progress.py
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
c=s['\$defs'] if '\$defs' in s else s.get('definitions')
print(json.dumps(s,indent=1)[:6000])"; grep -h "^  data:" claims/*/*.yaml | sort | uniq -c
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
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 189 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s['properties']['checks'],indent=1)); print(json.dumps(s['\$defs'],indent=1)[:2500])"
```

```
{
 "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "date",
   "kind",
   "ready"
  ],
  "properties": {
   "date": {
    "type": "string",
    "format": "date"
   },
   "kind": {
    "enum": [
     "agent",
     "person"
[... 123 more lines not kept]
```

**Agent**

Checker passes. Main problems found: a few statements that their criteria or expected values don't fully cover, one overstatement, and a few unnamed readings. Making the edits now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "# M6 Neuron selection. Neurons with at least 5 spikes/s of preparatory tuning for J-array, 10\n#    spikes/s for the single-electrode datasets",
 "new_string": "# M6 Neuron selection. Neurons with more than 5 spikes/s of preparatory tuning for J-array, at\n#    least 10 spikes/s for the single-electrode datasets"
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    Reproduced when all three are within tolerance under one reading.",
 "new_string": "    The condition count has tolerance 0 because it is a design count, not a measurement.\n    Reproduced when all three are within tolerance under one reading."
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "  quote: A total of 310 single-electrode isolations (64, 74, and 172 single-unit isolations for\n    monkeys A, B and J) were recorded from caudal PMd, surface M1 and sulcal M1.\n  expected:",
 "new_string": "  quote: A total of 310 single-electrode isolations (64, 74, and 172 single-unit isolations for\n    monkeys A, B and J) were recorded from caudal PMd, surface M1 and sulcal M1. ... High trial\n    counts (mean trials/neuron = 311, 492, 388 and 2166 for monkey A, B, J, J-array)\n  expected:\n  - quantity: mean trials per neuron, monkey A\n    value: 311\n    tolerance: 31.1\n  - quantity: mean trials per neuron, monkey B\n    value: 492\n    tolerance: 49.2\n  - quantity: mean trials per neuron, monkey J\n    value: 388\n    tolerance: 38.8"
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    tuning correlation of claim fig4abc-mean-correlation-single-electrode. Reproduced when at\n    least one speed-task neuron has r within tolerance of 0.72 and a preparatory preference up and\n    left; blocked if the dataset holds no speed-task data.",
 "new_string": "    tuning correlation of claim fig4abc-mean-correlation-single-electrode. The paper gives no\n    measure of \"prefers reaches ending up and leftwards\"; the Figure 2B legend shows the near\n    distance and fast speed and shades traces by the rate 50 ms before the go cue. It is read as:\n    among those 7 conditions, the one with the highest rate 50 ms before the go cue has its target\n    in the upper-left quadrant. Reproduced when at least one speed-task neuron has r within\n    tolerance of 0.72 and that preference; blocked if the dataset holds no speed-task data."
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "  criterion: Speed task only. With conditions restricted to the far distance and fast speed (the 7\n    directions, as in Figure 2C-E legend), tuning correlation as in M4 for neurons passing M6.\n    Reproduced when at least three neurons have negative correlations; blocked if the dataset holds\n    no speed-task data.",
 "new_string": "  criterion: Speed task only, neurons passing M6, tuning correlation as in M4. The paper does not\n    say over which conditions the negative correlations of these neurons were computed. Readings\n    (F1) the 7 far, fast conditions shown in the Figure 2C-E legend; (F2) all 28 conditions, as in\n    Figure 4. Reproduced when at least three neurons have negative correlations under one reading;\n    blocked if the dataset holds no speed-task data."
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "  quote: Across the four datasets the mean correlation was positive (p=0.01, p=0.01, p=0.12, p=0.03)\n    but only very modestly so (mean r = 0.21, 0.19, 0.06 and 0.13).\n  statistics:",
 "new_string": "  quote: Across the four datasets the mean correlation was positive (p=0.01, p=0.01, p=0.12, p=0.03)\n    but only very modestly so (mean r = 0.21, 0.19, 0.06 and 0.13). Non-parametric correlations were\n    similarly modest (mean Spearman's r = 0.20, 0.20, 0.06 and 0.11).\n  statistics:"
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "  - quantity: mean tuning correlation, monkey J\n    value: 0.06\n    tolerance: 0.006",
 "new_string": "  - quantity: mean tuning correlation, monkey J\n    value: 0.06\n    tolerance: 0.006\n  - quantity: mean Spearman tuning correlation, monkey A\n    value: 0.20\n    tolerance: 0.020\n  - quantity: mean Spearman tuning correlation, monkey B\n    value: 0.20\n    tolerance: 0.020\n  - quantity: mean Spearman tuning correlation, monkey J\n    value: 0.06\n    tolerance: 0.006"
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    \"Almost always\" has no threshold in the paper; it is read as all\n    comparisons but at most one, the paper naming one class of exception (3-D spaces on the speed\n    task). Reproduced on J-array when the peri-movement space wins all comparisons but at most one\n    and the 3-D endpoints + maximum speed space falls below the 3-D peri-movement space.",
 "new_string": "    \"Almost always\" has no threshold in the paper. Readings (L1) all comparisons but at most one,\n    the paper naming one class of exception (3-D spaces on the speed task); (L2) at least 90% of\n    comparisons. \"Did not perform well\" for the 3-D endpoints + maximum speed space is read as\n    below the 3-D peri-movement space. Reproduced on J-array when that space falls below the 3-D\n    peri-movement space and the peri-movement space wins under L1 or L2; the outcome is\n    methods_underspecified if L1 and L2 disagree."
}
```

```
<tool_use_error>String to replace not found in file.
String:     "Almost always" has no threshold in the paper; it is read as all
    comparisons but at most one, the paper naming one class of exception (3-D spaces on the speed
    task). Reproduced on J-array when the peri-movement space wins all comparisons but at most one
    and the 3-D endpoints + maximum speed space falls below the 3-D peri-movement space.</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    dimensionality, and task spaces are outperformed by the kinematic and EMG spaces, which are in\n    turn outperformed by the peri-movement space.",
 "new_string": "    dimensionality, and task spaces are largely outperformed by the kinematic and EMG spaces, which\n    are in turn outperformed by the peri-movement space."
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    Reproduced when the peri-movement space is best under all three limits and no other space is\n    significantly better; blocked if the archive lacks those datasets.",
 "new_string": "    The paper gives no threshold for \"increased\" or \"largely\"; they are read as the gap between\n    the peri-movement space and the next best space being larger at the 12-dimension limit than\n    at the 3-dimension limit, and the kinematic and EMG spaces each exceeding more than half of\n    the task spaces at the 12-dimension limit. Reproduced when the peri-movement space is best\n    under all three limits, no other space is significantly better, and both readings hold;\n    blocked if the archive lacks those datasets."
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Grep**

```json
{
 "pattern": "Almost always",
 "path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "output_mode": "content",
 "-B": 3,
 "-A": 4
}
```

```
335-  - fig6-peri-movement-space-best
336-  criterion: Performances from fig6-peri-movement-space-best. Comparisons are each task space against
337-    the peri-movement space at the task space's dimensionality, and the kinematic space against the
338:    peri-movement space at each k. "Almost always" has no threshold in the paper; it is read as all
339-    comparisons but at most one, the paper naming one class of exception (3-D spaces on the speed
340-    task). Reproduced on J-array when the peri-movement space wins all comparisons but at most one
341-    and the 3-D endpoints + maximum speed space falls below the 3-D peri-movement space.
342-- id: fig6-performance-vs-dimensionality
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    peri-movement space at each k. \"Almost always\" has no threshold in the paper; it is read as all\n    comparisons but at most one, the paper naming one class of exception (3-D spaces on the speed\n    task). Reproduced on J-array when the peri-movement space wins all comparisons but at most one\n    and the 3-D endpoints + maximum speed space falls below the 3-D peri-movement space.",
 "new_string": "    peri-movement space at each k. \"Almost always\" has no threshold in the paper. Readings (L1) all\n    comparisons but at most one, the paper naming one class of exception (3-D spaces on the speed\n    task); (L2) at least 90% of comparisons. \"Did not perform well\" for the 3-D endpoints + maximum\n    speed space is read as below the 3-D peri-movement space. Reproduced on J-array when that\n    space falls below the 3-D peri-movement space and the peri-movement space wins under L1 and\n    L2; the outcome is methods_underspecified if L1 and L2 disagree."
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent**

Now adding a claim for the Figure 4 distribution finding, which had none, plus the checks entry.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "- id: fig4e-correlation-time-course",
 "new_string": "- id: fig4-no-separate-populations\n  statement: The distributions of tuning correlations give little evidence (except perhaps weakly\n    for monkey B) of one population with concordant tuning (r near 1) and another with opposing\n    tuning (r near -1); most neurons have weakly correlated tuning, with a broad range of\n    correlations centred near zero.\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraphs 3 and 4;\n    Figure 4A-D\n  quote: Even more disconcertingly, different neurons show markedly different relationships between\n    preparatory and peri-movement activity, with a broad range of correlations centered near zero.\n    ... Yet there is little evidence in Figure 4 (except perhaps weakly in panel B ) for one\n    population of concordant tuning ( r ≈ 1) and another of opposing tuning ( r ≈ -1). Instead,\n    most neurons have weakly correlated tuning.\n  depends_on:\n  - fig4d-mean-correlation-jarray\n  criterion: Per-neuron correlations from fig4d (and fig4abc for datasets the archive holds). A\n    claim of absence judged by eye in the paper, which names no test and no threshold. Readings\n    (U1) Hartigan's dip test of unimodality gives p >= 0.05; (U2) more neurons have |r| < 0.5 than\n    have |r| >= 0.5. Reproduced when both hold, not reproduced when neither holds, and\n    methods_underspecified when they disagree; the dip statistic and the share of |r| >= 0.8 are\n    reported either way.\n- id: fig4e-correlation-time-course"
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cat >> claims/000128/10.1016-j.neuron.2010.09.015.yaml <<'EOF'
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header M6, J-array threshold is more than 5 spikes/s and the single-electrode one at least 10 spikes/s, as the Methods word them.
  - recordings-jarray, criterion gives the reason for the zero tolerance on the condition count.
  - recordings-single-electrode, the statement names mean trial counts of 311, 492 and 388 but had no expected values or quote for them; added both from Results, Behavior and recordings.
  - fig2b-example-concordant-tuning, the up-and-left preference had no measure; named the reading from the Figure 2B legend (near/fast conditions, rate 50 ms before the go cue) and said it is a reading.
  - fig2ce-example-opposing-tuning, the paper does not say over which conditions these neurons' correlations were taken; added the 28-condition reading (F2) beside the 7-condition one (F1).
  - fig4abc-mean-correlation-single-electrode, the statement gives mean Spearman correlations that had no quote or expected values; quote extended and three expected values added.
  - fig6-each-dimensionality, the threshold for "almost always" was a single choice by the writer; added a second reading (L2) and the rule for disagreement.
  - fig6e-summary-across-datasets, the statement said task spaces are outperformed where the paper says "largely outcompeted"; restored "largely". The criterion did not test the growing differential or the task versus kinematic/EMG ordering; added readings for both.
  - Added claim fig4-no-separate-populations, a Results finding (no concordant and opposing populations, correlations centred near zero) that had no claim. The paper names no test; both readings are the checker's and are named as such.
  - Open, fig3-maze-most-not-maintained uses r >= 0.72 as "similar tuning"; the paper sets no threshold, and 0.72 is only the value it calls quite high.
  - Open, header M9 sets the end of reach by a 5% speed threshold when the dataset marks none; the paper does not define the end of reach and this may shift endpoint, halfpoint and segment spaces.
  - Open, fig7c-anterior-posterior-performance, the dimensionality of the upper-limit space used to normalise and the meaning of "within the spread" of random subdivisions are not fixed by the paper.
  - Open, fig8-model-weak-correlation tests the 0.08 correlation but not the statement's second part (a given preparatory rate leading to opposing patterns), which the paper shows only by example.
  - Open, several criteria (fig4e, suppfig1, fig6-performance-vs-dimensionality, fig7a) turn qualitative words into thresholds the paper does not give; each is named as a reading in its criterion.
EOF
python tools/claims_check.py claims/000128/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "before the go cue. It is read as:\n    among those",
 "new_string": "before the go cue. It is read as\n    follows. Among those"
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000128/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt; grep -n ': .*: ' claims/000128/*.yaml | grep -v '^\S*:[0-9]*:#' | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker probably requires the quote's parts in text order. Reordering.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "  quote: A total of 310 single-electrode isolations (64, 74, and 172 single-unit isolations for\n    monkeys A, B and J) were recorded from caudal PMd, surface M1 and sulcal M1. ... High trial\n    counts (mean trials/neuron = 311, 492, 388 and 2166 for monkey A, B, J, J-array)",
 "new_string": "  quote: High trial counts (mean trials/neuron = 311, 492, 388 and 2166 for monkey A, B, J, J-array)\n    ... A total of 310 single-electrode isolations (64, 74, and 172 single-unit isolations for\n    monkeys A, B and J) were recorded from caudal PMd, surface M1 and sulcal M1."
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000128/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file for 000128 is ready for an attempt: the last check says `ready: true`. I changed eight existing claims and the header, and added one claim. Nothing is committed or pushed.

**Checker result:** `claims/000128/10.1016-j.neuron.2010.09.015.yaml: 22 claims, 22 quotes, 9 statistical values, 0 problems`. It was 21 claims with 0 problems before my edits.

**Changes, by claim**
- **Header, M6:** the thresholds now match the Methods' wording: more than 5 spikes/s for J-array, at least 10 spikes/s for the single-electrode datasets.
- **recordings-jarray:** the criterion now says why the condition count has zero tolerance: it is a count fixed by the task design, not a measurement.
- **recordings-single-electrode:** the statement gives mean trial counts (311, 492, 388) that had no quote or expected values. I added both, from Results, Behavior and recordings.
- **fig2b-example-concordant-tuning:** "prefers up and left" had no measure. I added a reading taken from the Figure 2B legend (near/fast conditions, rate 50 ms before the go cue) and labelled it as a reading.
- **fig2ce-example-opposing-tuning:** the criterion only used the 7 far/fast conditions. The paper doesn't say which conditions these correlations used, so I added the 28-condition reading as well.
- **fig4abc-mean-correlation-single-electrode:** the statement gives mean Spearman values that had no quote or expected values. I extended the quote and added three expected values.
- **fig6-each-dimensionality:** "almost always" rested on one threshold the first writer chose. I added a second reading (at least 90% of comparisons) and a rule for when the two readings disagree.
- **fig6e-summary-across-datasets:** the statement said task spaces are "outperformed" where the paper says "largely outcompeted", so I restored "largely". The criterion also didn't test two parts of the statement: that the gap grows with dimensionality, and that task spaces rank below the kinematic and EMG spaces. I added readings for both.
- **New claim, fig4-no-separate-populations:** a Results finding that had no claim. It says the correlations show no separate concordant and opposing groups and are centred near zero. The paper names no test, so both readings in the criterion are mine and are labelled that way.

**Still open** (recorded in `checks`)
- **fig3-maze-most-not-maintained:** r ≥ 0.72 is used as the cut-off for "similar tuning". The paper sets no threshold; 0.72 is just the one value it calls "quite high".
- **Header, M9:** when the dataset doesn't mark the end of a reach, it is taken as speed falling below 5% of peak. The paper doesn't define the end of a reach, and this choice could shift the endpoint, halfpoint and segment spaces.
- **fig7c-anterior-posterior-performance:** the paper fixes neither the dimensionality of the upper-limit space used for normalising nor what "within the spread" of the random subdivisions means.
- **fig8-model-weak-correlation:** the second part of the statement (one preparatory rate leading to opposing patterns) isn't tested. The paper shows it only by example.
- **fig4e, suppfig1, fig6-performance-vs-dimensionality, fig7a:** these turn qualitative words into thresholds the paper doesn't give. Each is labelled as a reading in its criterion.

The other paper under `paper/` (10.1038-nature11129) isn't used by any claim. Several untracked files outside `claims/` (dotfiles, `scripts`) were already in the working tree; I left them alone.

## End of run

31 turns, 3 minutes, result: success.
