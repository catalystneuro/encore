# 001676 · claims-check · run 39578834471

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/001676/ paper/ | head; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 96,200p docs/protocol.md; python tools/claims_check.py claims/001676/*.yaml paper/*.txt; wc -l paper/*.txt claims/001676/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-10096-w.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml"
}
```

```
1	# Claims for Skromne Carrasco, Viejo & Peyrache (2026), "Months-long stability of the
2	# head-direction system", Nature 652, 167-173, on dandiset 001676.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record (Nature, 2026), from the PDF supplied by hand, as extracted to
7	# paper/10.1038-s41586-025-10096-w.txt: main text, Methods, and the legends of Extended Data
8	# Figs. 1 to 10. The Supplementary Information (Supplementary Table 1, recording details of the
9	# electrophysiology, and Supplementary Table 2, sessions and HD cells per animal) is not under
10	# paper/ and was not read; no claim rests on it. The Source Data files were not read. PDF pages
11	# 22 to 25 carry no extractable text (in Nature PDFs, the reporting summary) and could not be
12	# rendered. No figure was read from the PDF.
13	#
14	# Code. The paper's Code availability statement reads "Code will be made available upon
15	# request." No repository is linked, so no code was read. Every method detail below comes from
16	# the Methods or the figure legends; where they are silent the detail is named as open.
17	#
18	# Data the paper used, as it reports it.
19	# - Imaging. Mice 1 to 5 (adult male C57BL/6J), GRIN lens (1.0 mm) over the left
20	#   post-subiculum (PoSub), GCaMP6f, UCLA Miniscope V4, 20-min sessions of free foraging on
[... 1032 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-10096-w.txt",
 "offset": 1133
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "\.\.\.\|'p'\|\"p\"\|required\|checks\|ready\|kind" tools/claims_check.py | head -60; ls claims | head -3; grep -l "^checks:" claims/*/*.yaml | head -2
```

```
3:    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
6:(fragments split on "...", found in order) and looks for every recorded p-value and
49:    fragments = [f for f in (norm(x).strip(" .,;") for x in quote.split("...")) if f]
93:            for v in [s.get("p")] + ([s["ci"]["low"], s["ci"]["high"]] if "ci" in s else []):
000003
000004
000005
claims/000005/10.1038-nn.4412.yaml
claims/000006/10.1038-s41586-018-0642-9.yaml
```

**Agent calls Bash**

```bash
cd  sed -n '/^checks:/,$p' claims/000006/*.yaml | head -30; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=0)[:200])"; grep -n '"statistics"' -A30 schemas/claims.schema.json | grep -n required
```

```
checks:
- date: "2026-10-20"
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Opening comment. Added two code details read in Ephys.zip Code/ (Figshare doi:10.25378/janelia.7007846 v1),
    the zero weight of a neuron with rank-sum p of 1 in DirectionVector, and the epoch means taking time > start
    and <= end, unlike the CD windows.
  - pt-types-transcriptomic. Statement said the data divide PT neurons into two types; the paper says they suggest
    it.
  - pt-projection-cluster-mapping. Source was paragraphs 4 and 5; both counts are in paragraph 4.
  - pt-types-account-for-all-pt. Statement made the paper's "suggest" a conclusion; reworded to "suggesting".
  - pt-depth. The code plots each unit's depth field (meta.depth), not the session manipulator depth it also stores;
    both are named as readings.
  - pt-lower-heterogeneous-rates. Bartlett's test was made the main reading from the words "χ2 test", which do not
    name a two-sample test, and the code's F test only a variant; both are now readings, and the outcome is the one
    they give.
  - pt-upper-early-preparatory. The rule for "larger" (PTupper 5th percentile above the PTlower median) is not in the
    paper; it is now named as one of two readings fixed here, with the plain comparison of medians.
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
def find(o,k,path=''):
  if isinstance(o,dict):
    for a,b in o.items():
      if a==k: print(path, json.dumps(b)[:600])
      find(b,k,path+'/'+a)
  elif isinstance(o,list):
    for i,b in enumerate(o): find(b,k,path+'/'+str(i))
find(s,'statistics')"
```

```
/properties/claims/items/properties {"description": "The statistical support the paper reports for the finding: one entry per test or interval, as the paper gives it. A record of the paper, not a target with a tolerance (that is `expected`).", "type": "array", "minItems": 1, "items": {"$ref": "#/$defs/statistic"}}
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s['\$defs']['statistic'],indent=1)[:1500])"
```

```
{
 "type": "object",
 "additionalProperties": false,
 "anyOf": [
  {
   "required": [
    "p"
   ]
  },
  {
   "required": [
    "ci"
   ]
  }
 ],
 "properties": {
  "about": {
   "description": "What the test compares or the interval bounds, when the claim has more than one, e.g. 'GPi against VLa onset times'.",
   "type": "string"
  },
[... 41 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "  source: Fig. 1f legend; Results, The tuning of HD cells is stable over time, paragraph 2",
 "new_string": "  source: Fig. 1f legend; Results, The tuning of HD cells is stable over time, paragraph 3"
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "  - quantity: mean ROIs per session, animals 1 to 5\n    value: 72\n    tolerance: 16\n  criterion: The ROI means use the s.d. given per animal as tolerance (72 plus or minus 16, 42\n    plus or minus 5, 197 plus or minus 18, 48 plus or minus 12, 102 plus or minus 25); the\n    recording counts must match exactly.",
 "new_string": "  - quantity: mean ROIs per session, animal 1\n    value: 72\n    tolerance: 16\n  - quantity: mean ROIs per session, animal 2\n    value: 42\n    tolerance: 5\n  - quantity: mean ROIs per session, animal 3\n    value: 197\n    tolerance: 18\n  - quantity: mean ROIs per session, animal 4\n    value: 48\n    tolerance: 12\n  - quantity: mean ROIs per session, animal 5\n    value: 102\n    tolerance: 25\n  - quantity: recordings, animal 1\n    value: 19\n    tolerance: 0\n  - quantity: recordings, animal 2\n    value: 20\n    tolerance: 0\n  - quantity: recordings, animal 3\n    value: 19\n    tolerance: 0\n  - quantity: recordings, animal 4\n    value: 19\n    tolerance: 0\n  - quantity: recordings, animal 5\n    value: 20\n    tolerance: 0\n  criterion: The ROI means use the s.d. given per animal as tolerance; the recording counts must\n    match exactly."
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "    each of the five mice. Reproduced when this holds for all five; partially reproduced for three\n    or four.",
 "new_string": "    each of the five mice. Reproduced when this holds for all five; partially reproduced for three\n    or four. This test and its counts are the reader's, not the paper's, and are recorded as a\n    deviation."
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "  - quantity: pooled shuffle V median, previous session\n    value: 21.9\n    tolerance: 2.19",
 "new_string": "  - quantity: pooled shuffle V median, previous session\n    value: 21.9\n    tolerance: 2.19\n  - quantity: V statistic, previous session, animal 1\n    value: 12.5\n    tolerance: 1.25\n  - quantity: V statistic, previous session, animal 2\n    value: 15.6\n    tolerance: 1.56\n  - quantity: V statistic, previous session, animal 3\n    value: 16.7\n    tolerance: 1.67\n  - quantity: V statistic, previous session, animal 4\n    value: 12.9\n    tolerance: 1.29\n  - quantity: V statistic, previous session, animal 5\n    value: 10.1\n    tolerance: 1.01\n  criterion: As edf4ab-vtest-per-animal, with each session compared to the previous session.\n    Reproduced when the pooled V is within tolerance with p below 0.001 and at least four of the\n    five per-animal V are within tolerance."
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "  - quantity: median change in offset, animal 1\n    value: 12.0\n    tolerance: 1.2\n    unit: degrees\n  - quantity: median change in offset, animal 2\n    value: 9.0\n    tolerance: 0.9\n    unit: degrees\n  - quantity: median change in offset, animal 3\n    value: 12.0\n    tolerance: 1.2\n    unit: degrees\n  - quantity: median change in offset, animal 4\n    value: 24.0\n    tolerance: 2.4\n    unit: degrees\n  - quantity: median change in offset, animal 5\n    value: 12.0\n    tolerance: 1.2\n    unit: degrees",
 "new_string": "  - quantity: median change in offset, animal 1\n    value: 12.0\n    tolerance: 27.6\n    unit: degrees\n  - quantity: median change in offset, animal 2\n    value: 9.0\n    tolerance: 24.1\n    unit: degrees\n  - quantity: median change in offset, animal 3\n    value: 12.0\n    tolerance: 27.1\n    unit: degrees\n  - quantity: median change in offset, animal 4\n    value: 24.0\n    tolerance: 40.9\n    unit: degrees\n  - quantity: median change in offset, animal 5\n    value: 12.0\n    tolerance: 31.1\n    unit: degrees"
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "    circular protocol. Since the cross-correlation shift is on a 3 degree grid, a median within\n    one bin (3 degrees) of the reported value also counts. Reproduced when every animal's median\n    is below all 1,000 shuffled medians and at least four medians are within tolerance.",
 "new_string": "    circular protocol. The per-animal tolerances are the s.d. that Extended Data Fig. 4g gives\n    with each median. Reproduced when every animal's median is below all 1,000 shuffled medians\n    and at least four medians are within tolerance."
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "    shuffle 95th percentile. Reproduced when this holds for at least 80% of the mouse and\n    environment pairs over all six pairs of the four environments (mouse 2 included, as for\n    remapping in the Methods), and the average remapping of at least one environment pair differs\n    from 0 by more than 30 degrees in at least three mice, read as an orientation specific to each\n    environment.",
 "new_string": "    shuffle 95th percentile. The environment pairs are the three of Fig. 2i (circular to square,\n    square to radial maze, radial maze to circular), the environments of one room whose alignment\n    the paper measures in room coordinates; the open field, in another room, is shown as a\n    variant. Reproduced when this holds for at least 80% of the mouse and environment pairs\n    (mouse 2 included, as for remapping in the Methods), and the average remapping of at least\n    one environment pair differs from 0 by more than 30 degrees in at least three mice, read as an\n    orientation specific to each environment. The 80% and 30 degree thresholds are the reader's,\n    not the paper's, and are recorded as a deviation."
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "    identities.\n  source: Fig. 3e",
 "new_string": "    identities.\n  source: Fig. 3d (the mvl values printed in the panel) and Fig. 3e"
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "  criterion: The legend's spread (0.1) is far below the spread of a mean over four mice and is\n    read as a standard error of a fit; 10% of the value is used as tolerance.",
 "new_string": "  criterion: The legend calls its spread (0.1, for both rates) the s.d. over mice; a spread\n    this small for four mice is doubtful, so 10% of the value is used as tolerance, and whether the\n    rates fall within 0.1 of the values is also shown."
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "  statistics:\n  - test: V-test against 0 degrees\n    statistic: V = 11.3, 10.1, 10.8\n    p: 0.05\n    p_relation: \"<\"\n    n: 20, 20 and 18 sessions\n  expected:\n  - quantity: V statistic, week 2",
 "new_string": "  expected:\n  - quantity: V statistic, week 2"
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "  criterion: The legend says only that the V-tests are significant; p below 0.05 is the reading.",
 "new_string": "  criterion: V-tests against 0 degrees over 20, 20 and 18 sessions (weeks 2, 3 and 4). The legend\n    gives no p and says only that the V-tests are significant; p below 0.05 is the reading."
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "    sessions with CellReg score above 0.8 (OPEN, the 0.6 threshold of Fig. 3 is the other\n    reading); shuffle of cell identity, its value per mouse the median over 1,000 shuffles.",
 "new_string": "    sessions with CellReg score above 0.8 (Methods; the 0.6 score is allowed for Fig. 3 only);\n    shuffle of cell identity within a day, 1,000 times (Methods, Orientation remapping). OPEN, the\n    shuffle value per mouse, readings (a) the median and (b) the mean over the 1,000 shuffles."
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "    n: \"10\"",
 "new_string": "    n: 10 values, read as 5 mice by 2 environments"
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now adding the Jaccard claim after edf2 and the checks block.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "- id: edf2-no-registration-confound",
 "new_string": "- id: edf2ab-jaccard\n  statement: The Jaccard index of HD cell detection between sessions of the circular protocol\n    remained high regardless of the delay between sessions.\n  source: Results, The tuning of HD cells is stable over time, paragraph 2; Extended Data Fig. 2a,b\n  quote: The Jaccard index remained high regardless of... the delay between sessions, suggesting\n    that most ROIs were successfully registered and continued to exhibit activity across time\n  criterion: Method from the Methods (Jaccard score). Per mouse and pair of sessions, the Jaccard\n    index of the binary vectors of presence (1) or absence (0) of HD tuning in each ROI, over the\n    ROIs registered across the session pairs; the median over all session pairs with the same\n    interval. OPEN, which ROIs count as registered across \"all relevant session pairs\", readings\n    (a) ROIs registered in both sessions of the pair and (b) ROIs registered in every session of\n    the protocol. The paper gives no test or level for \"high\". Reproduced when, in at least four\n    of five mice, the median index at the longest interval is at least 80% of that at an interval\n    of one day; this threshold is the reader's and is recorded as a deviation. The Spearman\n    correlation of the median index with interval is shown.\n- id: edf2-no-registration-confound"
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  f=claims/001676/10.1038-s41586-025-10096-w.yaml; cat >> $f <<'EOF'
checks:
- date: "2026-10-21"
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1f-example-stable. Source said Results paragraph 2; the sentence citing Fig. 1e,f is in paragraph 3.
  - edf1e-hd-proportion. One expected entry, labelled "animals 1 to 5", held only animal 1's ROI mean; added
    the ROI means of animals 2 to 5 and the recording counts per animal, which the criterion says must match.
  - edf1h-ring. The circular correlation test and its counts are not in the paper; the criterion now says they
    are the reader's and a deviation.
  - edf4c-previous-session. Added the per-animal V statistics of Extended Data Fig. 4d to expected, and a
    criterion over them.
  - edf4g-pairwise-offset-stable. Tolerances were 10% though Extended Data Fig. 4g gives an s.d. with each
    median (protocol, stated spread first, as fig2e and edf7 already do); set them to those s.d. and removed
    the 3 degree bin clause, which was the reader's.
  - fig2h-coherent-remapping. The criterion used all six pairs of the four environments; Fig. 2i and the
    Results measure remapping over the three environments of one room in room coordinates, so these three
    pairs are now the test and the open field a variant. The 80% and 30 degree thresholds are now named as
    the reader's.
  - fig3e-mvl-delay. The mvl values are printed in Fig. 3d (whose legend defines mvl); source now names it.
  - fig3fg-probe-drift. The criterion called the legend's 0.1 a standard error, against the legend's "s.d.";
    reworded to say the legend calls it s.d., and the 0.1 band is also shown.
  - edf9-interference. Removed the statistics entry, a p < 0.05 the paper does not print (the legend says only
    "significantly centered"); the V values stay in expected and the reading of p in the criterion.
  - fig4d-single-visit-memory. Removed the CellReg 0.6 reading; the Methods allow 0.6 for Fig. 3 only. Named
    the shuffle (cell identity within a day, 1,000 times) and the median per mouse as one of two readings.
  - edf10c-environment-identity. n was the bare string "10"; now says 10 values, read as 5 mice by 2
    environments (W = 7 with p = 1.0 fits 5 pairs).
  - edf2ab-jaccard. Added; the Results state that the Jaccard index stayed high regardless of delay, and no
    claim covered it.
  - Open. Several criteria rest on thresholds the reader set where the paper has no test (roi-counts Spearman,
    edf4ef-not-diffusive, fig1k-decoding-across-days "up to 20 days except one", edf4ij-pv-decay Spearman,
    edf9-interference "reduced retention" comparison, fig2g 100 splits, edf2ab-jaccard 80%); they are recorded
    as deviations but cannot be settled from the paper.
  - Open. The Fig. 1 example mouse is animal 4 by Extended Data Fig. 1g, yet its V (17.06) matches the second
    value of Extended Data Fig. 4b (17.1), not the fourth (14.6); the order of animals in Extended Data Fig. 4
    cannot be settled.
  - Open. fig3fg tolerance; the legend's s.d. of 0.1 for both drift rates is implausibly small, and 10% is a
    reasoned departure from the stated spread.
  - Open. edf1e proportions are printed to one decimal with s.d. of 0.03 to 0.05, narrower than the rounding;
    tolerances kept at the stated s.d.
  - Open. Supplementary Tables 1 and 2 were not available; no claim rests on them, but they would fix the
    sessions and HD cells per animal.
EOF
python tools/claims_check.py $f paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001676/10.1038-s41586-025-10096-w.yaml",
 "old_string": "  quote: The Jaccard index remained high regardless of... the delay between sessions, suggesting\n    that most ROIs were successfully registered and continued to exhibit activity across time",
 "new_string": "  quote: The Jaccard index remained high regardless of... the delay between sessions, suggesting\n    that most ROIs were... registered and continued to exhibit activity across time"
}
```

```
The file claims/001676/10.1038-s41586-025-10096-w.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001676/*.yaml paper/*.txt; grep -n ': [^ ]*: ' claims/001676/*.yaml | grep -v '^\S*:[0-9]*: *#' | head; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The checked file is fit for an attempt, and the last check has `ready: true`.

**Checker result:** `claims/001676/10.1038-s41586-025-10096-w.yaml: 32 claims, 32 quotes, 34 statistical values, 0 problems`. The first run, before my edits, gave 31 claims, 35 statistical values and 0 problems.

**Changes, by claim**
- **fig1f-example-stable:** the source said Results paragraph 3 was paragraph 2; fixed.
- **edf1e-hd-proportion:** the entry labelled "animals 1 to 5" held only animal 1's ROI mean. I added the ROI means for animals 2 to 5 and the recording count for each animal, which the criterion already said must match.
- **edf1h-ring:** the criterion now says its circular-correlation test is the reader's, not the paper's, and is recorded as a deviation.
- **edf4c-previous-session:** added the per-animal V values from Extended Data Fig. 4d, and a criterion that uses them.
- **edf4g-pairwise-offset-stable:** tolerances were 10%, but the legend gives an s.d. with each median, and the protocol says to use the stated spread first. I switched to the s.d., as fig2e and edf7 already do, and dropped the reader's 3-degree-bin clause.
- **fig2h-coherent-remapping:** the test now uses only the three same-room environment pairs of Fig. 2i, where the paper measures alignment in room coordinates. The open field becomes a variant. The 80% and 30° thresholds are now marked as the reader's.
- **fig3e-mvl-delay:** the source now includes Fig. 3d, where the mvl values are printed.
- **fig3fg-probe-drift:** the criterion called the legend's ±0.1 a standard error, but the legend says s.d. I reworded it to say so. The 10% tolerance stays, with its reason given, and the ±0.1 band is also to be shown.
- **edf9-interference:** removed the statistics entry. It recorded p < 0.05, a value the paper never prints.
- **fig4d-single-visit-memory:** removed the CellReg 0.6 reading, because the Methods allow 0.6 only for Fig. 3. I named the shuffle the Methods use and gave median and mean over the shuffles as the two readings.
- **edf10c-environment-identity:** n now reads "10 values, read as 5 mice by 2 environments". W = 7 with p = 1.0 fits 5 pairs.
- **edf2ab-jaccard (new):** the Results say the Jaccard index stayed high regardless of the delay between sessions, and no claim covered that.

All the paper's other main findings already have claims, and every claim comes from this paper.

**Still open (also listed in `checks`)**
- **Reader-set thresholds:** several criteria rest on thresholds the reader chose where the paper gives no test. These are roi-counts, edf4ef, fig1k ("up to 20 days except one"), edf4ij, the edf9 "reduced retention" comparison, the fig2g splits and the edf2ab 80%. They are recorded as deviations but can't be settled from the paper.
- **Animal order:** Extended Data Fig. 1g names animal 4 as the Fig. 1 mouse. But that mouse's V (17.06) matches the second value in Extended Data Fig. 4b, not the fourth (14.6), so the animal order there can't be settled.
- **fig3fg tolerance:** the legend's s.d. of 0.1 for both drift rates is implausibly small for four mice.
- **edf1e tolerances:** the proportions are printed to one decimal, but their s.d. values (0.03 to 0.05) are smaller than that rounding.
- **Supplementary Tables 1 and 2** are not under `paper/`. No claim rests on them.

Nothing was committed or pushed.

## End of run

27 turns, 4 minutes, result: success.
