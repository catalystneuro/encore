# schapiro-2024 · claims-check · run 45671681369

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/; cat claims/schapiro-2024.yaml; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/schapiro-2024.yaml"
}
```

```
1	# Claims for Schapiro, Rittenberg, Kenngott & Marder (2024), eLife, doi:10.7554/elife.98844, on Dryad
2	# dataset doi:10.5061/dryad.1rn8pk129 ("Effects of Cs on temperature response of C. borealis pyloric
3	# rhythm").
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-25,
5	# protocol as stated in docs/protocol.md (version pilot-19).
6	#
7	# Text read: the version of record, full text from Europe PMC (PMC11479588, open access JATS), with
8	# Results, Discussion, Methods, the figure legends of Figures 1 to 6, Figure 1-figure supplement 1
9	# (the paper's only supplement) and Table 1. The dataset's files were not opened.
10	#
11	# Code. The Data availability statement says the code and data to reproduce the results and figures
12	# were uploaded to the Dryad dataset itself. Being among the dataset's files, that code was not read
13	# in this run and no commit is recorded. The Methods also link Crabsort (github.com/sg-s/crabsort,
14	# commit ee237eaea4565d4139a31a40fe180f884175a20b, read), the MATLAB spike-sorting software used to
15	# detect and assign spikes. It holds the sorting interface, file loading, clustering and generic
16	# helpers (computePeriods, consolidate); the paper does not say those helpers were used, and nothing
17	# in it fixes the frequency, Q10, phase or jag measures below. Every method below is from the paper's
18	# text. Where the deposited scripts settle a detail named as open here, the author may follow them
19	# and should say so.
20	#
[... 621 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/schapiro-2024.yaml paper/10.7554-elife.98844.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.98844.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -E "threshold|p_relation|statistics|claim of absence|partially|checks|ready" docs/protocol.md | head -60
```

```
14:  and how each is to be tested, taken from the paper. A second reader checks
21:- The **verifier** checks the author's work and must not be the author.
93:   - `statistics`: the statistical support the paper reports for the
97:     `p_relation: "<"`; a printed "P = 0" is recorded as 0), any `corrected`
101:     Record only tests whose result is the finding. A significance threshold
122:     bins, thresholds, what a measure is compared with) is taken from the
137:   - For a claim of absence ("no difference", "did not change"), the
138:     criterion names the test and threshold the paper used. The claim is
175:A second reader, in a separate run, checks the claims file against the paper:
178:mechanically); that each source points at the place; that the statistics are
179:the paper's and are results, not thresholds; that every part of every
182:show is wrong, and records each change, with its reason, under `checks` at
183:the end of the file. A claims file is ready for an attempt when its last check
192:takes it from the paper. The reader, who has not seen the data, checks each
212:it got, then write the attempt record and run the entry's checks. A record
250:     dataset already holds, such as stimulus names for its stimulus codes.
255:     claims are the registry's checks, not findings of the paper, so the
320:   a window, a threshold, what a measure is compared with), take it from the
430:  run. The verifier's re-run and the pull request's checks allow eighty, as a
468:   - When a threshold or criterion is a choice, show how the result changes
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 85,200p docs/protocol.md
```

```
reader check the statement against the paper without opening it. For a
     finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
     states it (numbers only in a table, a result spread over several
     legends), a short note under `inferred` saying so. The statement is
     then a reading of the paper, and the note says what it was
     read from.
   - `statistics`: the statistical support the paper reports for the
     finding, one entry per test or interval: what it compares (`about`,
     when there is more than one), the `test` and `statistic` as named, the
     `p`-value as a number (a bound such as "p < 0.05" is `p: 0.05` with
     `p_relation: "<"`; a printed "P = 0" is recorded as 0), any `corrected`
     for multiple comparisons, a confidence interval (`ci`), and `n` in
     words. It records the paper; the
     numbers the attempt must match, with tolerances, stay in `expected`.
     Record only tests whose result is the finding. A significance threshold
     used to select or count units, cells or pairs ("238 of 288 neurons were
     better fit, p < 0.05") is a method, not a result, and is left out.
     Leave the field out when the paper reports no test or interval for the
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -E "'p'|\"p\"|required|checks|ready|kind" tools/claims_check.py | head -40; ls claims | head; grep -l "checks:" claims/*.yaml | head -3
```

```
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
93:            for v in [s.get("p")] + ([s["ci"]["low"], s["ci"]["high"]] if "ci" in s else []):
alasfour-2024.yaml
amjad-2025.yaml
andrews-2024.yaml
armstrong-2026.yaml
asari-2009.yaml
ashworth-2025.yaml
athalye-2023.yaml
azcorra-2023.yaml
bakalar-2023.yaml
bech-2026.yaml
claims/alasfour-2024.yaml
claims/andrews-2024.yaml
claims/armstrong-2026.yaml
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));
import pprint
def find(o,k,path=''):
  if isinstance(o,dict):
    for kk,v in o.items():
      if kk in ('statistics','checks'): print(path+'/'+kk); pprint.pprint(v)
      find(v,k,path+'/'+kk)
find(s,'')
" | head -80; sed -n '/^checks:/,$p' claims/alasfour-2024.yaml | head -20
```

```
/properties/claims/items/properties/statistics
{'description': 'The statistical support the paper reports for the finding: '
                'one entry per test or interval, as the paper gives it. A '
                'record of the paper, not a target with a tolerance (that is '
                '`expected`).',
 'items': {'$ref': '#/$defs/statistic'},
 'minItems': 1,
 'type': 'array'}
/properties/checks
{'description': 'Checks of the claims file against the paper by a second '
                'reader (docs/protocol.md, Reader, step 5), oldest first. The '
                'file is ready for an attempt when the last says so.',
 'items': {'additionalProperties': False,
           'properties': {'by': {'type': 'string'},
                          'changes': {'items': {'minLength': 1,
                                                'type': 'string'},
                                      'type': 'array'},
                          'date': {'format': 'date', 'type': 'string'},
                          'kind': {'enum': ['agent', 'person']},
                          'model': {'type': 'string'},
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs']['statistic'],indent=1))" | head -60
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
[... 40 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "#   squares; (b) a straight-line fit of log10 frequency on temperature, Q10 = 10^(10 * slope);\n#   (c) the two-point ratio (f21/f11)^(10/10).",
 "new_string": "#   squares; (b) a straight-line fit of log10 frequency on temperature, Q10 = 10^(10 * slope);\n#   (c) the two-point ratio (f21/f11)^(10/10). The Figure 1C legend (\"Line represents the best fit\n#   Q 10 equations for each condition\") supports (a) as the main reading; (b) and (c) are variants."
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "#   t-test (normal), Bonferroni-adjusted for 10 tests (5 phases by 2 conditions).",
 "new_string": "#   t-test (normal), Bonferroni-adjusted for 10 tests (5 phases by 2 conditions). The Figure 6\n#   legend names a \"paired Student's t-test\" for the normal case; a test of slopes against zero is\n#   a one-sample test, as the Methods say, and the two coincide when the paired values are slope\n#   and zero."
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "  source: Results, The steady-state frequency increase, paragraph 3; Figure 1D\n  quote:",
 "new_string": "  source: Results, The steady-state frequency increase, paragraph 3; Figure 1D legend\n  quote:"
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "  criterion: A claim of absence. Per experiment and protocol, mean frequency within 0.3 degrees C of\n    21 degrees C minus that of 11 degrees C; a paired",
 "new_string": "  criterion: A claim of absence. Per experiment and protocol, mean frequency within 0.3 degrees C of\n    21 degrees C minus that of 11 degrees C (the first 11 degrees C hold of the protocol, O2); a paired"
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "  criterion: A claim of absence, judged on a paired t-test of the two Q10 values over the 6\n    experiments (Figure 1E legend). Q10 under the readings of O1; the absence is judged under each\n    and reported for all. Reproduced when p >= 0.05, not reproduced when p < 0.05.",
 "new_string": "  criterion: A claim of absence, judged on a paired t-test of the two Q10 values over the 6\n    experiments (Figure 1E legend). Q10 under reading (a) of O1, the one the Figure 1C legend\n    supports, marked as resting on that reading; (b) and (c) are shown as variants. Reproduced\n    when p >= 0.05, not reproduced when p < 0.05; the mean difference is reported either way."
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "    12 pooled values are variants. Q10 under O1. Reproduced when p >= 0.05, not reproduced when\n    p < 0.05.",
 "new_string": "    12 pooled values are variants. The paper gives no N for this test; the n recorded is this\n    file's reading of the two designs. Q10 under reading (a) of O1 (Figure 1C legend), (b) and (c)\n    as variants. Reproduced when p >= 0.05, not reproduced when p < 0.05."
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "  statement: In Cs+, the frequency decrease right after a temperature increase came from an\n    elongation of the PD depolarizing phase, with bursting and repolarization phases maintained.\n  source: Results, Cs+ revealed dynamic transitory frequency response, paragraph 1; Figure 2C; also\n    Figure 4G for Cs+ + PTX",
 "new_string": "  statement: In an example preparation in Cs+, the frequency decrease right after the temperature\n    step from 13 toward 15 degrees C came from an elongation of the PD depolarizing phase, not of\n    the bursting, repolarization or inhibitory phases; a Cs+ + PTX example showed the same.\n  source: Results, Cs+ revealed dynamic transitory frequency response, paragraph 1; Figure 2C\n    legend; Results, In Cs+, follower neurons determined frequency-temperature sensitivity,\n    paragraph 3, and Figure 4G for Cs+ + PTX; Discussion, The jags in frequency, paragraph 2"
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "  criterion: The paper shows this in one example preparation, not identified, for the step from 13\n    toward 15 degrees C, and gives no measure. A measure is fixed here from the legend's phases. On\n    the intracellular PD trace, per cycle, burst duration (first to last spike), repolarization\n    (last spike to the voltage minimum), and depolarization (voltage minimum to the next first\n    spike). In each Cs+ experiment with intracellular PD, cycles of the 30 s before the 13 to 15\n    degrees C step are compared with the cycles of the first 30 s of warming in which the period\n    exceeds the pre-step mean. Reproduced when, in most such experiments, the depolarizing phase\n    accounts for more than half of the period increase. Partially reproduced when this holds in the\n    example-like experiments with the largest decrease only. Not testable without intracellular PD\n    traces.",
 "new_string": "  criterion: The paper shows this in one example preparation, not identified, for the step from 13\n    toward 15 degrees C, and gives no measure; the Discussion treats it as general (\"the frequency\n    decrease is associated with an elongation of the depolarizing phase\", Figures 2C and 4G). The\n    phase boundaries and windows are open; the paper names the phases (bursting, repolarization,\n    inhibitory, depolarizing in the Results; bursting, repolarization, depolarizing in the Figure 2C\n    legend) without defining them. Readings for the phases on the intracellular PD trace, per\n    cycle, are (a) three phases as in the legend, burst (first to last PD spike), repolarization\n    (last PD spike to the voltage minimum), depolarization (voltage minimum to the next first PD\n    spike); (b) four phases as in the Results, burst (first to last PD spike), repolarization (last\n    PD spike to the first LP spike), inhibition (first to last LP spike), depolarization (last LP\n    spike to the next first PD spike). Windows, from the Discussion's \"~30 s of temperature\n    increase\": the cycles of the 30 s before the 13 to 15 degrees C step against the cycles of the\n    first 30 s of warming whose period exceeds the pre-step mean. In each Cs+ experiment with\n    intracellular PD, the share of the period increase carried by each phase. Reproduced when,\n    under one reading, in most such experiments the depolarizing phase accounts for more than half\n    of the period increase; partially reproduced when this holds only in the experiments with the\n    largest frequency decrease. Not testable without intracellular PD traces."
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "    n: 6 experiments\n  - about: pairwise comparisons of conditions\n    test: post hoc Tukey's honestly significant difference\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Per experiment and condition, mean frequency within 0.3 degrees C of 21 degrees C minus\n    that of 11 degrees C; a one-way",
 "new_string": "    n: 6 experiments\n  criterion: Per experiment and condition, mean frequency within 0.3 degrees C of 21 degrees C minus\n    that of 11 degrees C (O2); a one-way"
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "    statistic: F(2,10) = 13.077\n    p: 0.002\n    n: 6 experiments\n  - about: pairwise comparisons of conditions\n    test: Tukey's honestly significant difference\n    p: 0.05\n    p_relation: \"<\"\n  criterion:",
 "new_string": "    statistic: F(2,10) = 13.077\n    p: 0.002\n    n: 6 experiments\n  criterion:"
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "    n: 6 experiments\n  - about: pairwise comparisons of conditions\n    test: Tukey's honestly significant difference\n    p: 0.05\n    p_relation: \"<\"\n  criterion: As fig4d-ptx-keeps-decrease-while-warming, for stable cycles with an increase. The\n    legend names the Cs+ against saline and Cs+ + PTX against Cs+ comparisons; the Results say all\n    three differ. Reproduced when, under one reading, the condition effect has p < 0.05, the means\n    are ordered saline < Cs+ < Cs+ + PTX, and all three pairs are significant; partially reproduced\n    when the two pairs the legend names are significant and saline against Cs+ + PTX also is, but\n    the ordering is not as stated, or when two of the three pairs are significant with the stated\n    ordering.",
 "new_string": "    n: 6 experiments\n  criterion: As fig4d-ptx-keeps-decrease-while-warming, for stable cycles with an increase. The\n    legend names the Cs+ against saline and Cs+ + PTX against Cs+ comparisons; the Results say all\n    three differ. Reproduced when, under one reading, the condition effect has p < 0.05, the means\n    are ordered saline < Cs+ < Cs+ + PTX, and all three Tukey pairs are significant; partially\n    reproduced when the condition effect and the two pairs the legend names (Cs+ above saline,\n    Cs+ + PTX above Cs+) are significant but saline against Cs+ + PTX is not."
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "    C of 11 degrees C, at the first 11 degrees C hold of the condition (O2). Reproduced when both",
 "new_string": "    C of 11 degrees C, at the first 11 degrees C hold of the condition (O2). The sentence gives no\n    N; 21 is read from the design (Figures 1D and 1E). Reproduced when both"
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat >> claims/schapiro-2024.yaml <<'EOF'
checks:
- date: 2026-11-25
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig4c-ptx-restores-frequency-change, fig4d-ptx-keeps-decrease-while-warming, fig4e-stable-increase-ordering. Removed the Tukey HSD statistics entries (p < 0.05); the paper prints no p-value for the post hoc comparisons, only that they were significant, so the bound was this file's significance threshold and not a reported result. The criteria keep the Tukey tests through O5.
  - fig4e-stable-increase-ordering. The partial rule allowed the two legend pairs and the third pair all significant with the ordering not as stated, which cannot happen when the legend pairs are directional. Partial is now the condition effect and the two legend pairs significant, saline against Cs+ + PTX not.
  - Header O1. The Figure 1C legend ("best fit Q 10 equations") supports the fitted Q10 equation; reading (a) is now named the main reading, (b) and (c) variants.
  - fig1e-two-saline-q10-same, fig1e-saline-q10-same-across-designs. These are claims of absence, judged on the paper's test alone; judging under every Q10 reading left the outcome undecided. Now judged under O1 reading (a), marked as resting on it, others shown as variants.
  - fig1e-saline-q10-same-across-designs. Said the paper gives no N for the two-sample test and the n recorded is this file's reading.
  - fig1-cs-lower-frequency-11c. Said the sentence gives no N and 21 is read from the design.
  - fig2c-decrease-by-depolarizing-phase. The statement generalized from one example; it now says an example preparation (and the Cs+ + PTX example), and names the inhibitory phase the Results list. Source adds the Figure 4G paragraph and the Discussion. The criterion's phase boundaries were fixed as if from the paper; they are now named as open, with readings (a) the legend's three phases and (b) the Results' four phases using LP spikes, and the 30 s windows are cited to the Discussion.
  - fig1d-difference-grows-with-temperature. Source names the Figure 1D legend, where the quote and statistic are.
  - fig1f-two-saline-frequency-change-same, fig4c-ptx-restores-frequency-change. The 11 degrees C hold now cites O2.
  - Header, phase constancy. Noted that the Figure 6 legend names a paired t-test where the Methods name a one-sample t-test of slopes against zero.
  - Open. Whether the reported Figure 6 p-values (p < 0.01) are Bonferroni-adjusted is not stated beyond the Methods' statement that p-values were adjusted; the file reads them as adjusted.
  - Open. F(5,85) for Figure 1D and r(21) for the matched-period correlation do not fit N=21 (about 18 experiments each); the paper does not say which experiments entered.
  - Open. How periods were matched (matched-period-lp-earlier) and whether PD offset advance is in ms or phase are not given; the readings in the criterion are this file's.
  - Open. Ih window definitions (figs1 claims), the jag smoothing alignment and span (O3), and cycles forming a phase (O4) remain open with the readings named; the deposited scripts in the dataset may settle them.
EOF
python tools/claims_check.py claims/schapiro-2024.yaml paper/10.7554-elife.98844.txt; grep -n ": " claims/schapiro-2024.yaml | sed -n '/^[0-9]*:  - /p' | grep -E "^[0-9]+:  - .*: " | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/schapiro-2024.yaml",
 "old_string": "spike). Windows, from the Discussion's \"~30 s of temperature\n    increase\": the cycles",
 "new_string": "spike). Windows, from the Discussion's \"~30 s of temperature\n    increase\", are the cycles"
}
```

```
The file claims/schapiro-2024.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/schapiro-2024.yaml paper/10.7554-elife.98844.txt; grep -nE "^\s{4,}[^-].*: " claims/schapiro-2024.yaml | grep -v "^\s*[a-z_]*:" ; grep -nE "  - .*[^:]: " claims/schapiro-2024.yaml | sed -n '/changes/,$p' | tail -5; grep -n -i -E "rather|—" claims/schapiro-2024.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git status --short
```

```
M claims/schapiro-2024.yaml
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

I checked `claims/schapiro-2024.yaml` against the paper, fixed what the paper shows to be wrong, and think the file is ready for an attempt. Nothing is committed.

**Checker result** (after my edits): `claims/schapiro-2024.yaml: 25 claims, 25 quotes, 24 statistical values, 0 problems`. Before the edits it gave 27 statistical values; the drop is the three post hoc test entries I removed.

**Changes, by claim**
- **fig4c, fig4d, fig4e:** I removed the post hoc Tukey test entries recorded as "p < 0.05". The paper never prints a p-value for those comparisons, only that they were significant, so the bound was a threshold the file supplied, not a result. The criteria still use the Tukey tests.
- **fig4e:** The rule for "partially reproduced" described a case that cannot happen. It now reads: the condition effect and the two comparisons the legend names are significant, but saline against Cs+ + PTX is not.
- **Header O1 (how Q10 is computed):** The Figure 1C legend says "best fit Q 10 equations", which supports fitting the Q10 equation. That reading is now the main one and the other two are variants.
- **fig1e-two-saline-q10-same, fig1e-saline-q10-same-across-designs:** These are claims of absence, which the protocol judges on the paper's test alone. They had been judged under every Q10 reading, which could leave the outcome undecided. They are now judged under the main reading, marked as resting on it, with the others shown as variants. For the second claim I also noted that the paper gives no N for its two-sample test.
- **fig1-cs-lower-frequency-11c:** Noted that the sentence gives no N; the 21 comes from the design.
- **fig2c:** The statement generalised from one example preparation and left out the "inhibitory" phase the Results list. It now says it is an example and names that phase. The phase boundaries had been written as if they came from the paper. They are now named as open, with two readings: the three phases in the figure legend, and the four phases in the Results, using LP spikes. The 30 s windows now cite the Discussion. The source also cites the Figure 4G paragraph and the Discussion.
- **fig1d:** The source now points at the Figure 1D legend, where the quote and the statistic are.
- **fig1f, fig4c:** Which 11 degrees C hold is used now cites the open detail O2.
- **Header, phase constancy:** Noted that the Figure 6 legend says "paired t-test" where the Methods say one-sample t-test.

**What remains open** (recorded under `checks`)
- The paper doesn't say whether the Figure 6 p-values are the Bonferroni-adjusted ones; the file reads them as adjusted.
- F(5,85) in Figure 1D and r(21) in the matched-period correlation each fit about 18 experiments, not 21. The paper doesn't say which experiments entered.
- How periods were matched, and whether the PD offset advance is in ms or in phase, are not given.
- The time windows for measuring Ih, the smoothing alignment and span for the jag measure, and which cycles form a phase all remain open, with readings named. The scripts deposited in the dataset may settle them; I did not open the dataset.

Every main finding has a claim, and every claim comes from this paper. The last check entry has `ready: true`.

## End of run

26 turns, 3 minutes, $1.08 at API prices, result: success.
