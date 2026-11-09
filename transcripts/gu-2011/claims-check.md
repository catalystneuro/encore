# crcns-stc-1 · claims-check · run 42255114199

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/crcns-stc-1/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 100,260p docs/protocol.md
```

```
better fit, p < 0.05") is a method, not a result, and is left out.
     Leave the field out when the paper reports no test or interval for the
     finding.
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
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml paper/10.1016-j.neuron.2011.06.015.txt; cat claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml"
}
```

```
1	# Claims for Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011), Neuron 71:750-761,
2	# "Perceptual Learning Reduces Interneuronal Correlations in Macaque Visual Cortex", on CRCNS data
3	# set stc-1 (doi:10.6080/K07P8WKF).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
5	# protocol as stated in docs/protocol.md (Reader).
6	#
7	# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
8	# with its Results, Discussion, Experimental Procedures and the legends of Figures 1 to 8, and
9	# the Supplemental Information PDF (legends of Figures S1 to S8). The article says the
10	# Supplemental Information "includes Experimental Procedures and eight figures"; the supplement
11	# as supplied, whose own contents page lists only the eight figures, holds no further
12	# procedures, so the Experimental Procedures of the article are taken as the whole Methods.
13	# The PDF could not be rendered here; the extracted text prints degree signs, minus signs and
14	# "approximately" as a replacement character, and quotes avoid those places. The paper links no
15	# analysis code, so none was read.
16	#
17	# Data the paper used. Eight male rhesus monkeys (Macaca mulatta): three "naive" animals trained
18	# only to fixate, and five "trained" animals extensively trained in a vestibular and visual
19	# heading discrimination task (left or right of straight ahead) before recording. Pairs of
20	# single units recorded simultaneously in area MSTd while the animals fixated passively and
[... 856 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2011.06.015.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "SUPPLEMENT\|=== supplement\|Figure S" paper/10.1016-j.neuron.2011.06.015.txt | head; awk 'NR>=1180' paper/10.1016-j.neuron.2011.06.015.txt | grep -n "" | head -0; sed -n '/Supplemental Information/,$p' paper/10.1016-j.neuron.2011.06.015.txt | tail -260
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes (34 claims, 0 problems). Now checking the schema for how ranges are expressed, and trying to render a few figures.

**Agent calls Bash**

```bash
cd  grep -n "range\|low\|high\|tolerance" tools/claims_check.py | head -40; ls schemas* tools | head -30; python -c "import fitz; print(fitz.__doc__)"
```

```
Exit code 1
38:    return re.sub(r"\s+", " ", s).strip().lower()
75:    return {f.lower() for f in out}
93:            for v in [s.get("p")] + ([s["ci"]["low"], s["ci"]["high"]] if "ci" in s else []):
schemas:
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json

tools:
__pycache__
agent_run.py
archive_transcripts.sh
archives
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_site.py
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));
import pprint
d=s.get('\$defs',s.get('definitions',{}))
for k in d:
  if 'expect' in k.lower() or 'check' in k.lower(): pprint.pprint(d[k])
" | head -80; which pdftoppm mutool
```

```
Exit code 1
{'additionalProperties': False,
 'properties': {'quantity': {'type': 'string'},
                'tolerance': {'minimum': 0, 'type': 'number'},
                'unit': {'type': 'string'},
                'value': {'type': 'number'}},
 'required': ['quantity', 'value'],
 'type': 'object'}
```

**Agent calls Bash**

```bash
cd  grep -n "checks" -A30 schemas/claims.schema.json | head -50; python -c "import pypdf" 2>&1; python -c "import pdfplumber" 2>&1
```

```
Exit code 1
202:    "checks": {
203-      "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
204-      "type": "array",
205-      "items": {
206-        "type": "object",
207-        "additionalProperties": false,
208-        "required": [
209-          "date",
210-          "kind",
211-          "ready"
212-        ],
213-        "properties": {
214-          "date": {
215-            "type": "string",
216-            "format": "date"
217-          },
218-          "kind": {
219-            "enum": [
220-              "agent",
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2011.06.015.pdf",
 "pages": "6-7"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

PDF rendering isn't available, so figure-only details stay open. Making the edits now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    value: 2\n    tolerance: 1.3\n    unit: degrees",
 "new_string": "    value: 2.1\n    tolerance: 1.2\n    unit: degrees"
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    for neurons with significant tuning (one-way ANOVA p < 0.05) in the\n    single-electrode database.",
 "new_string": "    for neurons with significant heading tuning in the horizontal plane (one-way ANOVA p <\n    0.05, Results) in the single-electrode database (visual 466 naive and 526 trained, Figure S4\n    legend)."
}
```

```
<tool_use_error>String to replace not found in file.
String:     for neurons with significant tuning (one-way ANOVA p < 0.05) in the
    single-electrode database.</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    curve at straight ahead (equation 2 for one neuron), with Poisson variance as in Figure S4\n    and Gu et al. 2010; how tuning curves are interpolated is not stated (readings, cubic\n    spline and linear interpolation). Fore-aft is a preference within 45 degrees of 0 or 180,\n    lateral within 45 degrees of -90 or 90. A factorial ANOVA on threshold with preference group\n    and training group, per condition; whether thresholds were log transformed is open (raw\n    and log are both run). Reproduced when lateral neurons have lower thresholds with p < 0.001\n    in both conditions under one reading.",
 "new_string": "    curve at straight ahead (equations 2 and 3 for one neuron), with variance equal to the mean\n    as equation 4 gives for i = j; how tuning curves are interpolated is not stated (readings,\n    cubic spline and linear interpolation). Fore-aft is a preference within 45 degrees of 0 or\n    180, lateral within 45 degrees of -90 or 90 (Results). How the preferred heading is\n    computed is not stated in this paper; the readings are the vector sum of the tuning curve\n    and the peak of the interpolated curve. A factorial ANOVA on threshold with preference\n    group and training group; whether it was run per condition (Figures 4D and 4H) or once with\n    condition as a third factor is not stated, and both are run; whether thresholds were log\n    transformed is open (raw and log are both run). Reproduced when lateral neurons have lower\n    thresholds with p < 0.001 under one reading (in both conditions for the per-condition\n    reading)."
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    at half maximum, for neurons with significant tuning (one-way ANOVA p < 0.05) in the\n    single-electrode database.",
 "new_string": "    at half maximum, for neurons with significant heading tuning in the horizontal plane\n    (one-way ANOVA p < 0.05, Results) in the single-electrode database (visual 466 naive and 526\n    trained, vestibular 216 naive and 340 trained, Figure S4 legend)."
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    as in the claims that use it, per condition and group (visual 466 naive, 526 trained; vestibular 216 naive, 340 trained).",
 "new_string": "x"
}
```

```
<tool_use_error>String to replace not found in file.
String:     as in the claims that use it, per condition and group (visual 466 naive, 526 trained; vestibular 216 naive, 340 trained).</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "  criterion: As in the Figure S4 legend, population threshold from equation 2 with independent\n    Poisson neurons, 95% bands from bootstrap resampling of 100 neurons with replacement, per\n    condition and group (visual 466 naive, 526 trained; vestibular 216 naive, 340 trained). The\n    number of bootstrap iterations and the reference headings sampled are not stated; 1,000\n    iterations and references every 22.5 degrees are standard choices.",
 "new_string": "  criterion: As in the Figure S4 legend, population threshold from equation 2 with independent\n    Poisson neurons, 95% bands by bootstrap, per condition and group (visual 466 naive, 526\n    trained; vestibular 216 naive, 340 trained). The legend's \"100 neurons were resampled with\n    replacement\" allows two readings, both run; populations of 100 neurons drawn with\n    replacement (1,000 iterations, a standard choice), and the whole group resampled with\n    replacement 100 times. The reference headings sampled are not stated; every 22.5 degrees\n    is a standard choice."
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    mean of rnoise minus the slope terms. Ordinary least squares",
 "new_string": "    mean of rnoise minus the slope terms, and (c) the slopes of an orthogonal fit to the naive\n    pairs, used for both groups as the Results describe structure (1), with the trained\n    intercept fitted with those slopes fixed. Ordinary least squares"
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    computed, and how bandwidth enters the wrapped Gaussian. The readings are amplitude 30\n    spikes/s on baseline 10 spikes/s over 1 s,",
 "new_string": "    computed, and how bandwidth enters the wrapped Gaussian. The readings are amplitude 30\n    spikes/s on baseline 10 spikes/s over 1 s (a standard choice, not from the paper; Figure 4\n    reports median amplitudes of 17 to 35 spikes/s and no baseline),"
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    for which rnoise stays within -1 and 1 (the grid range is read from Figure 6B; slope 0 to\n    0.4 and intercept 0 to 0.2 are the reading).",
 "new_string": "    for which rnoise stays within -1 and 1. The grid range is shown only in Figure 6B, whose\n    axes could not be read from the text; slope 0 to 0.4 and intercept 0 to 0.2, which contain\n    the measured naive and trained parameters, are a choice, not from the paper."
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    or 180, lateral within 45 degrees of -90 or 90). Two-sample t tests. Reproduced when fore-aft",
 "new_string": "    or 180, lateral within 45 degrees of -90 or 90; the preferred heading by the readings of\n    fig4dh-lateral-more-sensitive). Two-sample t tests. Reproduced when fore-aft"
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    heading (Figure 8C legend). The pairs are those of Figure 8C, recorded in trained animals\n    during fixation and discrimination; which pairs and which preference (visual or\n    vestibular) are not stated, and the readings are the trained pairs under 1 mm with visual\n    preference and with vestibular preference. Reproduced when no reading's test finds a\n    difference; the group means are reported either way.",
 "new_string": "    heading (Figure 8C legend), groups as in Figure 4. The Results speak of trained animals,\n    but the legend's 328 fixation points (164 pairs entered twice) exceed the 89 trained pairs\n    under 1 mm (178 points), so the sample is not settled. The readings are the trained pairs\n    under 1 mm, all trained pairs, and all 179 pairs, each with visual and with vestibular\n    preference, with and without the 55 discrimination-task points. The test is run under\n    each; the outcome is judged under the reading whose point count comes closest to 328 and\n    55, and the others are shown. Reproduced when that test finds no difference; the group\n    means are reported either way."
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "  - about: congruency in the ANCOVA with rsignal\n    test: ANCOVA\n    p: 0.6\n    p_relation: \">\"\n  criterion: Congruency index per neuron as the Pearson correlation of its visual and\n    vestibular tuning curves; pairs CC, OO or CO by the signs (Figure S5 legend). Two-way ANOVA\n    of pooled rnoise on training group and pair type, over the 127 pairs. Needs tuning curves.\n    Reproduced when the training effect has p < 0.05 and neither the congruency effect nor the\n    interaction has p < 0.05 (a claim of absence for these two, judged on this test).",
 "new_string": "  - about: congruency in the ANCOVA with rsignal\n    test: ANCOVA\n    p: 0.6\n    p_relation: \">\"\n  - about: interaction of congruency with rsignal in the ANCOVA\n    test: ANCOVA\n    p: 0.7\n    p_relation: \">\"\n  - about: interaction of congruency with training group in the ANCOVA\n    test: ANCOVA\n    p: 0.8\n    p_relation: \">\"\n  criterion: Congruency index per neuron as the Pearson correlation of its visual and\n    vestibular tuning curves; pairs CC, OO or CO by the signs (Figure S5 legend). Two-way ANOVA\n    of pooled rnoise on training group and pair type, over the 127 pairs. Then, as in the\n    legend, an ANCOVA of rnoise with rsignal as covariate and pair type and training group as\n    factors; which rsignal enters (visual, vestibular) is not stated, and both are run. Needs\n    tuning curves. Reproduced when the ANOVA training effect has p < 0.05 and none of the\n    ANOVA congruency effect, the ANOVA interaction and the three ANCOVA congruency terms has p\n    < 0.05 (claims of absence, judged on these tests)."
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    200 ms, Experimental Procedures), with 500 ms before onset as a variant. Reproduced when\n    the mean prestimulus rnoise exceeds the stimulus rnoise by a paired t test at p < 0.05.",
 "new_string": "    200 ms, Experimental Procedures), with 500 ms before onset as a variant. The paper names no\n    test; a paired t test over pairs is a standard choice, not the paper's. Reproduced when\n    the mean prestimulus rnoise exceeds the stimulus rnoise by that test at p < 0.05."
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "    0.3, Figure 1E\n  expected:",
 "new_string": "    0.3, Figure 1E\n  statistics:\n  - about: rnoise of the example pair, visual\n    test: Pearson correlation\n    statistic: rnoise = 0.29\n    p: 0.04\n  - about: rnoise of the example pair, vestibular\n    test: Pearson correlation\n    statistic: R = 0.14\n    p: 0.3\n  expected:"
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat >> claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml <<'EOF'
checks:
- date: 2026-11-06
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1-example-pair, added the two per-pair Pearson tests (p = 0.04 and 0.3) under statistics, which the statement reports and the file had left out.
  - fig2a-behavioral-learning, expected value 2 with tolerance 1.3 gave 0.7 to 3.3 degrees, not the 0.9 to 3.3 the criterion and the protocol rule for a range give; set to 2.1 with tolerance 1.2.
  - fig4-tuning-width-visual, selection now says tuning in the horizontal plane (Results) and gives the group sizes of the Figure S4 legend.
  - fig4dh-lateral-more-sensitive, Poisson variance is now taken from equation 4 (Q_ii = f_i) in place of Gu et al. 2010, which is not this paper; added as open how the preferred heading is computed and whether the ANOVA was per condition or with condition as a factor, each with readings.
  - fig8ab-choice-probability-lateral, preferred heading readings referred to fig4dh-lateral-more-sensitive.
  - figs4-population-sensitivity-any-reference, the legend's 100 resampled neurons allows two bootstrap readings (populations of 100 neurons, or 100 resamples of the whole group); both are now named.
  - fig5-regression-coefficients, added reading (c), slopes from the naive fit used for both groups, as the Results describe the naive structure.
  - fig6a-population-thresholds, tuning amplitude and baseline marked as a choice not from the paper.
  - fig6b-slope-not-intercept, the grid range was said to be read from Figure 6B, which the text does not show and no reader could render; marked as a choice.
  - fig8cd-noise-not-preference, the reading of 89 trained pairs under 1 mm (178 points) does not match the legend's 328 fixation points; readings widened to all trained pairs and all 179 pairs, with and without the 55 task points, judged under the reading whose counts come closest.
  - figs5-congruency, the statement's ANCOVA part had no criterion; added the ANCOVA of the Figure S5 legend and its two other terms (p > 0.7, p > 0.8) under statistics.
  - discussion-stimulus-reduces-correlation, said that the paired t test is a standard choice, since the paper names no test.
  - Open, fig5-regression-coefficients keeps the protocol's 10% tolerance on the trained intercept of 0.005 (0.0005), which no estimate from 89 pairs can meet; the claim will likely rest on its partial criterion.
  - Open, the PDF could not be rendered in this run either, so figure-only details (Figure 6B axes, the garbled approximately signs before 5-fold and 8%) were not checked against the figures.
  - Open, Figure 2A, Figure 4, Figure S4 and Figures 8A and 8B use single-electrode data and training histories from the authors' earlier studies; whether stc-1 holds them is for the author.
EOF
python tools/claims_check.py claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml paper/10.1016-j.neuron.2011.06.015.txt | head -3; grep -n ": .*: " claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml | grep -v "^\s*#" | head
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file against the paper. The file is ready for an attempt (`ready: true`). Nothing is committed.

**Checker:** `claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml: 34 claims, 33 quotes, 43 statistical values, 0 problems`. It also passed with 0 problems before my edits (39 statistical values then).

**Changes, by claim:**
- **fig1-example-pair:** added the two per-pair Pearson tests (p = 0.04 visual, p = 0.3 vestibular) under `statistics`. The statement already reported them.
- **fig2a-behavioral-learning:** the expected value 2 ± 1.3 covered 0.7 to 3.3 degrees, but the criterion and the protocol's range rule give 0.9 to 3.3. Changed it to 2.1 ± 1.2.
- **fig4-tuning-width-visual:** the selection now says tuning "in the horizontal plane", as the Results do, and gives the group sizes from the Figure S4 legend.
- **fig4dh-lateral-more-sensitive:** the Poisson variance was cited to Gu et al. 2010, which is not this paper. It now comes from equation 4. Two details the paper leaves open are now named, each with readings: how the preferred heading is computed, and whether the ANOVA was run per condition or once with condition as a factor.
- **fig8ab-choice-probability-lateral:** now uses the preferred-heading readings of fig4dh.
- **figs4-population-sensitivity-any-reference:** the legend's "100 neurons were resampled with replacement" can be read two ways. Both are named: populations of 100 neurons, or 100 resamples of the whole group.
- **fig5-regression-coefficients:** added a third reading, where the slopes from the naive fit are used for both groups, as the Results describe the naive structure.
- **fig6a-population-thresholds:** the tuning amplitude and baseline (30 on 10 spikes/s) are now marked as a choice, not taken from the paper.
- **fig6b-slope-not-intercept:** the grid range was said to be "read from Figure 6B", but the figure could not be rendered. It is now marked as a choice.
- **fig8cd-noise-not-preference:** the only reading (89 trained pairs under 1 mm, 178 points) does not fit the legend's 328 fixation points. I widened the readings to all trained pairs and all 179 pairs, with and without the 55 discrimination-task points. The claim is judged under the reading whose counts come closest to 328 and 55.
- **figs5-congruency:** the ANCOVA part of the statement had no criterion. I added one from the Figure S5 legend, plus its two other terms (p > 0.7 and p > 0.8) under `statistics`.
- **discussion-stimulus-reduces-correlation:** now says the paired t test is a standard choice, since the paper names no test.

**Still open (recorded in `checks`):**
- **Trained intercept tolerance:** fig5-regression-coefficients keeps the protocol's 10% tolerance on the trained intercept of 0.005 (± 0.0005). No estimate from 89 pairs can meet it, so the claim will likely only reach its partial criterion.
- **Figure-only details:** the PDF could not be rendered in this run either. The Figure 6B axes and the garbled "approximately" signs before "5-fold" and "8%" were not checked against the figures.
- **Data from earlier studies:** Figure 2A, Figure 4, Figure S4 and Figures 8A and 8B use the authors' earlier single-electrode recordings and training histories. Whether stc-1 holds them is for the author to find.

Coverage is complete: every main finding has a claim, and every claim comes from this paper.

## End of run

26 turns, 3 minutes, $1.19 at API prices, result: success.
