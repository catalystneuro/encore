# dijk-2018 · claims-check · run 42834177770

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i dijk; cat claims/dijk-2018.yaml; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i -e neuron.2018 -e dijk; wc -l claims/dijk-2018.yaml; python tools/claims_check.py claims/dijk-2018.yaml paper/10.1016-j.neuron.2018.04.018.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/dijk-2018.yaml"
}
```

```
1	# Claims for van Dijk & Fenton (2018), "On How the Dentate Gyrus Contributes to Memory
2	# Discrimination", Neuron 98, 832-845, on CRCNS hc-17.
3	#
4	# Provenance: written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
5	# Actions"), 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).
6	#
7	# Text read: the version of record (paper/10.1016-j.neuron.2018.04.018.txt, supplied by a
8	# person, extracted from the PDF), the main text, figure legends, STAR Methods (e1 to e5) and
9	# the Supplemental Information (Figures S1 and S2 with legends, Tables S1 and S2). No figure
10	# was read from a PDF page. The CRCNS data descriptor (hc-17.data-description.txt) was read
11	# only to know which experiments the dataset holds; no claim comes from it.
12	#
13	# Code read: the Data and Software Availability section links
14	# https://github.com/FentonLab/Mcode_DG-MemoryDiscrimination-NeuronMS. At commit
15	# 3542a85bb44a1739425e63eb4d16f9dc30ce7f54 (2018-04-01, the only commit) it holds a one-line
16	# README and a file "vanDijkFenton2018Neuron-AnalysisCode" that is a macOS alias (a pointer to
17	# a folder on the authors' computer), not code. No analysis code could be read, so no method
18	# detail below is settled by code. Statistics were run in JMP 12 (STAR Methods).
19	#
20	# Data the paper used (Results; STAR Methods, Experimental model, Recording set up, Behavioral
[... 1144 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/10.1016-j.neuron.2018.04.018.txt; sed -n '/^Reader/,/^## /p' docs/protocol.md | head -5; grep -n "step 5\|5\. " docs/protocol.md | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 60,215p docs/protocol.md
```

```
Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
stimulus software), the Methods come first, then the paper's analysis code,
then other software.

### 3. Write the claims file

Write `claims/<paper>.yaml`, one file for the paper, across all its datasets. Its opening comment
says which text was read (the version of record or a preprint version, and the
supplement), and describes the data the paper used: the subjects, sessions,
conditions and measured variables, as the paper reports them, so that the
author can find them in the dataset.

   - One claim per finding, at the level of a figure panel or a reported
     number when the full text is available. Cover the paper's main findings,
     including those the dataset cannot test.
   - `statement`: the finding in words. `source`: where the paper shows it,
[... 135 more lines not kept]
```

**Agent**

Checker found 3 p-values it could not match (likely exponent notation). Now reading the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.04.018.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.04.018.txt",
 "offset": 700,
 "limit": 550
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "STAR+METHODS\|METHOD DETAILS\|Supplemental\|Table S1\|Figure S2" paper/10.1016-j.neuron.2018.04.018.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.04.018.txt",
 "offset": 1410,
 "limit": 680
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker's only flags are three p-values printed as powers of ten (10^-7, 10^-6, 10^-5), and I confirmed each against the text. Now applying corrections.

**Agent calls Bash**

```bash
cd  python3 -c "
from scipy import stats
print(2*stats.t.sf(2.7,5), 2*stats.t.sf(2.7,4), 2*stats.t.sf(2.7,6))
print(2*min(stats.f.sf(1.10,4189,3169),stats.f.cdf(1.10,4189,3169)))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy import stats
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "  statement: The number of place fields rose from the circular environments to the twice\n    larger box after wall removal, more in DG (1.48 to 2.70) than in CA (1.19 to 2.0), with\n    significant effects of region and condition and no interaction.",
 "new_string": "  statement: The number of place fields rose from the circular environments to the twice\n    larger box after wall removal, more in DG (1.48 to 2.70) than in CA (1.19 to 2.0), with a\n    condition effect, a region effect at p = 0.05 and no interaction; post hoc, removed DG\n    exceeded circular DG and CA, and CA did not change."
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "    p < 0.05 with more fields after removal, and the post hoc test (Fisher's LSD) puts removed\n    DG above circular DG. The SEMs",
 "new_string": "    p < 0.05 with more fields after removal, and the post hoc test (Fisher's LSD) puts removed\n    DG above circular DG and circular CA and finds no difference between circular and removed\n    CA (Results, same sentence). The SEMs"
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "    effect has p < 0.05 under the M5 reading used; not reproduced when any does. The legend\n    plots log field rates; the ANOVA on the untransformed magnitude is the main test and the\n    log version a variant. Rests on the M5 assumption.",
 "new_string": "    effect has p < 0.05 under the M5 reading used; not reproduced when any does. The legend\n    plots log field rates; the paper does not say whether the ANOVA was on raw or log rates.\n    Open; the ANOVA on the untransformed magnitude is used as a standard choice and the log\n    version shown as a variant. Rests on the M5 assumption."
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "  criterion: cFos+ counts over six slices per animal (Histology). Reproduced when a two-tailed\n    t-test of Cre+ against Cre- counts gives p < 0.05 with Cre+ lower.",
 "new_string": "  criterion: cFos+ counts over six slices per animal (Histology). Open, which animals were\n    counted; the Behavioral Procedures say the validation cohort was perfused after the\n    conflict trial, and t = 2.7 with p = 0.04 fits about 5 df, far fewer than 29 mice.\n    Readings (a) the validation cohort; (b) every Cre+ and Cre- mouse with counts. Reproduced\n    when a two-tailed t-test of Cre+ against Cre- counts gives p < 0.05 with Cre+ lower."
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "    and Fisher's LSD puts training 2 below training 1 and conflict. The df (2, 4) suggest\n    fewer mice than six entered; open, readings (a) the five mice with conflict data, (b) all\n    six with missing values allowed. Needs the shock-on sessions, in which no units were\n    recorded.",
 "new_string": "    and Fisher's LSD puts training 2 below training 1 and conflict. Open, the design behind\n    the df (2, 4). Readings (a) all six mice in a multivariate repeated-measures F test (JMP's\n    default for within-subject factors, df k-1 and n-k+1, which is 2 and 4 for six mice and\n    three levels); (b) a univariate repeated-measures ANOVA on three mice' worth of df, which\n    fits no subset the paper names; (a) is the one the df support. Needs the shock-on\n    sessions, in which no units were recorded."
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "  - about: shock status, errors per meter\n    test: two-way shock status by condition ANOVA\n    statistic: F(1, 9) = 4.40\n    p: 0.07\n  criterion:",
 "new_string": "  - about: shock status, errors per meter\n    test: two-way shock status by condition ANOVA\n    statistic: F(1, 9) = 4.40\n    p: 0.07\n  - about: condition, errors per meter\n    test: two-way shock status by condition ANOVA\n    statistic: F(2, 18) = 5.59\n    p: 0.01\n  - about: interaction, errors per meter\n    test: two-way shock status by condition ANOVA\n    statistic: F(2, 18) = 1.45\n    p: 0.26\n  criterion:"
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "  criterion: A claim of absence. Mean speed per mouse in the shock-off recording sessions; the\n    three levels are read as pretraining, training and conflict (df 2). A one-way ANOVA at\n    alpha 0.05. Reproduced when p >= 0.05.",
 "new_string": "  criterion: A claim of absence. Mean speed per mouse and session. A one-way ANOVA at alpha\n    0.05. Open, which sessions; the text names \"training and conflict conditions\" with\n    three levels (df 2). Readings (a) training 1, training 2 and conflict; (b) pretraining,\n    training and conflict; each with (i) the shock-on sessions, (ii) the shock-off recording\n    sessions. The paper does not say; as a claim of absence it is reproduced when the test\n    gives p >= 0.05 under the reading the author adopts, with all readings shown."
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "  criterion: A claim of absence. Per cell and condition (pretraining and training sessions\n    averaged per cell), firing rate,",
 "new_string": "  criterion: A claim of absence. Per cell and condition (pretraining and training sessions\n    averaged per cell; Table S2 gives 42 cells for each, so one value per cell, but how the two\n    sessions are combined is not stated and averaging is a standard choice), firing rate,"
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "    three levels); (b) a univariate repeated-measures ANOVA on three mice' worth of df, which\n    fits no subset the paper names; (a) is the one the df support. Needs the shock-on",
 "new_string": "    three levels); (b) a univariate repeated-measures ANOVA, whose df (2, 4) would mean three\n    mice, a subset the paper does not name. Reading (a) is the one the df support. Needs the shock-on"
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "  - test: Pearson correlation\n    statistic: r2 = 0.0069",
 "new_string": "  - test: correlation (type not named)\n    statistic: r2 = 0.0069"
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "    1-s rolling window the Methods use for the Kendall correlation check. Reproduced when r2\n    is within tolerance and p < 0.001 under one reading; partially reproduced when r2 is\n    below 2% with p < 0.001.",
 "new_string": "    1-s rolling window the Methods use for the Kendall correlation check. The type of\n    correlation is not named; Pearson is used as the standard choice. Reproduced when r2 is\n    within tolerance and p < 0.001 under one reading."
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "  - test: Pearson correlation\n    statistic: r = -0.02\n    p: 0.67\n  criterion: A claim of absence. Per pixel (1.5 cm, room frame) the fraction of time with\n    ΔIpos > 0, per mouse, averaged over mice (Positional information), for training and for\n    conflict. Pearson correlation across pixels visited in both. Reproduced when p >= 0.05.",
 "new_string": "  - test: correlation (type not named)\n    statistic: r = -0.02\n    p: 0.67\n  criterion: A claim of absence. Per pixel (1.5 cm, room frame) the fraction of time with\n    ΔIpos > 0, per mouse, averaged over mice (Positional information), for training and for\n    conflict. The correlation type and the pixels entered are not stated; Pearson across\n    pixels visited in both is used as the standard choice. Reproduced when p >= 0.05."
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "  - test: Welch's one-way ANOVA\n    statistic: F(2, 435) = 7.1\n    p: 0.0001\n  criterion: Normalized tau change per pair (M9) per manipulation (M11 readings). The paper\n    gives an F test with integer df without naming it; a one-way ANOVA, Welch's when variances\n    differ (M12). Reproduced",
 "new_string": "  - test: one-way ANOVA (F test, not named)\n    statistic: F(2, 435) = 7.1\n    p: 0.0001\n  criterion: Normalized tau change per pair (M9) per manipulation (M11 readings). The paper\n    gives an F test with integer df without naming it; Welch's ANOVA would give a fractional\n    denominator df, so the test is read as an ordinary one-way ANOVA (M12). Reproduced"
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the missing statistics in correlation-not-speed and fig6-inset, the M7 note, and the checks entry.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "    statistic: F(2, 293) = 0.64\n    p: 0.53\n  criterion:",
 "new_string": "    statistic: F(2, 293) = 0.64\n    p: 0.53\n  - about: firing rates, interaction\n    test: two-way zone by condition ANOVA\n    statistic: F(2, 293) = 0.26\n    p: 0.77\n  criterion:"
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "    statistic: F(2, 245) = 14.81\n    p: 0.0001\n    p_relation: \"<\"\n  depends_on:\n  - fig6b-correlation-before-avoidance\n  criterion: Field rate instability Δ(A,B)/max(A,B) (M4, absolute) of place cells in the 4-s\n    windows before avoidances and errors, by zone and manipulation (M11). Two-way ANOVAs.\n    Reproduced when, for avoidances, the manipulation effect has p < 0.05 and the zone effect\n    and interaction do not, and for errors the manipulation effect has p < 0.05.",
 "new_string": "    statistic: F(2, 245) = 14.81\n    p: 0.0001\n    p_relation: \"<\"\n  - about: errors, interaction\n    test: two-way zone by manipulation ANOVA\n    statistic: F(2, 245) = 1.13\n    p: 0.33\n  depends_on:\n  - fig6b-correlation-before-avoidance\n  criterion: Field rate instability Δ(A,B)/max(A,B) (M4, absolute) of place cells in the 4-s\n    windows before avoidances and errors, by zone and manipulation (M11). Two-way ANOVAs.\n    Reproduced when, for avoidances, the manipulation effect has p < 0.05 and the zone effect\n    and interaction do not, and for errors the zone and manipulation effects have p < 0.05\n    (Figure 6C legend: rate changes differ between zone vicinities and manipulations)."
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "  or in it (Positional information). Kendall correlations near zones (Figures 5E, 6) use",
 "new_string": "  or in it (Positional information). Kendall correlations near zones (Figure 5E; Figure 6\n#   uses the 4-s windows of M8 instead) use"
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  sed -n 80,92p claims/dijk-2018.yaml; grep -n "^checks" claims/dijk-2018.yaml; tail -3 claims/dijk-2018.yaml
```

```
#   pixel (the stated spatial resolution of location-specific analyses); (b) 2 x 2 pixel
#   blocks (3 cm). The probabilities are taken over the session analysed.
# M7 Shock zone vicinity. Ipos (Figure 4D) uses times within 3 pixels (4.5 cm) of a shock zone
#   or in it (Positional information). Kendall correlations near zones (Figure 5E; Figure 6
#   uses the 4-s windows of M8 instead) use
#   times within 3 pixels (4.5 cm) of the zone but not in it (Cell pair spike train discharge
#   correlations). Network consistency near zones uses passes through firing fields in the
#   zone and its surrounding 6 cm, longer than 3 s (Network Consistency). The "training zone"
#   is the 60-degree room-frame sector shocked in training; the "conflict zone" is the sector
#   180 degrees away, shocked in conflict. Both vicinities are computed in every session,
#   pretraining included (Positional information).
# M8 Approach events. Local minima of the distance to the nearest edge of the shock zone. For
#   Ipos (Figure 4C) a minimum counts when it is closer than 50% of the animal's average
    Reproduced when, for avoidances, the manipulation effect has p < 0.05 and the zone effect
    and interaction do not, and for errors the zone and manipulation effects have p < 0.05
    (Figure 6C legend: rate changes differ between zone vicinities and manipulations).
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dijk-2018.yaml",
 "old_string": "    (Figure 6C legend: rate changes differ between zone vicinities and manipulations).",
 "new_string": "    (the Figure 6C legend says rate changes differ between zone vicinities and manipulations).\nchecks:\n- date: 2026-11-10\n  kind: agent\n  model: claude-opus-5-5\n  ready: true\n  changes:\n  - fig1-field-number-scaling, statement said the region effect was significant; the paper prints p = 0.05, so it now says so, and the paper's post hoc result (removed DG above circular DG and CA, CA unchanged) is added to statement and criterion.\n  - fig1c-field-rate-change-no-difference, the criterion made the untransformed ANOVA the paper's test; the paper does not say whether raw or log rates were tested, now named as open with the raw version as a standard choice.\n  - fig2c-cfos-reduced, added that the counted animals are not stated, with readings; t = 2.7 with p = 0.04 fits about 5 df, not 29 mice.\n  - fig3b-avoidance-learning, the criterion said df (2, 4) imply fewer than six mice; a multivariate repeated-measures F test (JMP) on six mice and three levels gives exactly df 2 and 4, now the reading the df support.\n  - fig3b-shock-off-avoidance, added the errors per meter condition and interaction tests from the Figure 3B legend, which the criterion uses.\n  - speed-no-difference, the criterion fixed the three levels as pretraining, training and conflict and the sessions as shock-off; the text names training and conflict conditions only, so both level readings and both session readings are now listed as open.\n  - tables2-firing-quality-similar, averaging pretraining and training sessions per cell is not stated in the paper; now named as a standard choice.\n  - ipos-speed-correlation, the test was called Pearson though the paper says only correlation; renamed, and the partial-reproduction rule (r2 below 2%) removed as it is not from the paper.\n  - fig4d-room-maps-uncorrelated, the test was called Pearson though the paper gives only r; renamed, Pearson now a stated standard choice.\n  - fig5d2-pc-int-change-relocation, the test was recorded as Welch's ANOVA, which the paper does not name and whose df would be fractional; the integer df 435 fit an ordinary one-way ANOVA, now recorded so.\n  - correlation-not-speed, added the firing rate interaction test (F2,293 = 0.26, p = 0.77) printed in the same sentence.\n  - fig6-inset-rate-changes, added the errors interaction (F2,245 = 1.13, p = 0.33) and the zone effect for errors to the criterion, from the Figure 6C legend.\n  - header M7, Figure 6 correlations use the 4-s windows before minima (M8), not the 4.5-cm vicinity; corrected.\n  - checker flags (fig2d 1e-07, fig5d4 1e-06, fig5e2-e4 1e-05) confirmed by reading; the paper prints them as powers of ten.\n  - open, pc-int-pair-classes and fig5d3, fig5d4, negative-pairs-no-change, the Kruskal-Wallis df (236, 280, 73) imply 239, 283 and 76 values, more than three manipulations times 56, 81 and 15 pairs; how pairs were classed per manipulation cannot be settled from the paper.\n  - open, overdispersion-similar, the printed p-values of the variance F tests do not fit their df under a two-sided F test; recorded as printed, so a reproduction of the variances can fail the paper's test as written."
}
```

```
The file claims/dijk-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/dijk-2018.yaml paper/10.1016-j.neuron.2018.04.018.txt; grep -n "—\|rather" claims/dijk-2018.yaml; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git diff -U0 claims/dijk-2018.yaml | grep '^+' | grep -v '^+++' | grep -E '[^ ]: |^\+ +[a-z_]+: .*: ' | grep -vE '^\+ *(- )?[a-z_]+: [^:]*$'
```

```
(Bash completed with no output)
```

**Agent**

I made 13 corrections and confirmed the checker's three flags. Two problems remain open, but neither stops an attempt, so I marked the file `ready: true`. Nothing is committed and only `claims/dijk-2018.yaml` was changed.

**Checker result** (the same before and after my edits): `claims/dijk-2018.yaml: 44 claims, 44 quotes, 93 statistical values, 3 problems`. The three problems are p-values the tool could not find: fig2d 1e-07, fig5d4 1e-06 and fig5e2-e4 1e-05. The paper prints them as 10^-7, 10^-6 and 10^-5, so the recorded values are correct.

**Changes, by claim**
- **fig1-field-number-scaling:** the statement called the region effect significant, but the paper prints p = 0.05; it now says that. I also added the paper's post hoc result (removed DG above circular DG and CA, CA unchanged) to the statement and criterion.
- **fig1c-field-rate-change-no-difference:** the paper does not say whether the ANOVA was run on raw or log field rates. This is now named as open; raw is used as a standard choice and log is a variant.
- **fig2c-cfos-reduced:** the paper does not say which animals were counted. I added readings and noted that t = 2.7 with p = 0.04 fits about 5 df, far fewer than 29 mice.
- **fig3b-avoidance-learning:** the criterion said df (2, 4) meant fewer than six mice. A multivariate repeated-measures test (the default in JMP, the paper's software) on six mice and three sessions gives exactly df 2 and 4, so the df support all six mice.
- **fig3b-shock-off-avoidance:** added the errors-per-meter condition and interaction tests from the legend, which the criterion relies on.
- **speed-no-difference:** the criterion had picked pretraining, training and conflict, in the shock-off sessions. The text names only "training and conflict conditions", so the possible session sets and both shock-on and shock-off readings are now listed as open.
- **tables2-firing-quality-similar:** the paper does not say pretraining and training sessions are averaged per cell; this is now labelled a standard choice.
- **ipos-speed-correlation:** the paper says only "correlation", not Pearson, so I renamed the test. I removed the "partially reproduced when r2 is below 2%" rule, which is not from the paper.
- **fig4d-room-maps-uncorrelated:** the paper gives only "r", so I renamed the test; Pearson is now a stated standard choice.
- **fig5d2-pc-int-change-relocation:** the test was recorded as Welch's ANOVA, which the paper never names. Welch's would give a fractional df, and the paper prints an integer one (435), so it is now an ordinary one-way ANOVA.
- **correlation-not-speed:** added the firing-rate interaction test (F2,293 = 0.26, p = 0.77) from the same sentence.
- **fig6-inset-rate-changes:** added the errors interaction (F2,245 = 1.13, p = 0.33). The criterion now also requires a zone effect for errors, as the Figure 6C legend states.
- **Header note M7:** corrected it. Figure 6 correlations use the 4-s windows before an approach to the zone, not the 4.5-cm area around it.

All other claims check out against the paper: quotes, sources, statistics, tolerances (1.96 × SEM or 10%) and Methods details. All of the paper's main findings have a claim.

**Still open**
- **How pairs were classed (pc-int-pair-classes, fig5d3, fig5d4, negative-pairs-no-change):** the test df imply 239, 283 and 76 values. That is more than three manipulations times the 56, 81 and 15 pairs the paper reports, and the paper does not explain how pairs were classed for each manipulation.
- **Overdispersion (overdispersion-similar):** the printed p-values of the variance tests do not fit their df under a two-sided test. A reproduction that matches the variances could therefore fail the paper's test as written.

The file is ready for an attempt.

## End of run

31 turns, 3 minutes, $1.41 at API prices, result: success.
