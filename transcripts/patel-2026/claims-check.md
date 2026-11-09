# 001454 · claims-check · run 39655595903

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001454/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; cat claims/001454/*.yaml; python tools/claims_check.py claims/001454/10.1038-s41593-026-02413-x.yaml paper/10.1038-s41593-026-02413-x.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 120,200p docs/protocol.md; python tools/claims_check.py claims/001454/10.1038-s41593-026-02413-x.yaml paper/10.1038-s41593-026-02413-x.txt; wc -l claims/001454/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml"
}
```

```
1	# Claims for Patel, Kim et al. (2026), Nature Neuroscience, doi:10.1038/s41593-026-02413-x, on
2	# dandiset 001454.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record, open access (PMC13633117, as served by Europe PMC): main
7	# text, figure legends, Extended Data Fig. 1 to 10 legends, Methods, and the one supplement file
8	# fetched (the Nature Portfolio reporting summary). Supplementary Tables 1 and 2 (membrane
9	# properties by housing and by rank) are not in the text; only their legends are. The claims
10	# that rest on them (input resistance, firing threshold) carry no numbers. The bioRxiv
11	# preprint (doi:10.1101/2023.11.09.566421, version 1) was read only to compare Methods; it is
12	# cited once below where it settles a detail. No figure image was available (no PDF of the
13	# article), so no claim is read from a figure.
14	#
15	# Code: the paper links no code ("All custom code used in this study is available upon
16	# request"). No repository was read. Every method below comes from the Methods, the legends
17	# or the reporting summary.
18	#
19	# Data the paper used, as it reports them. Adult C57BL/6J mice, males and females, group
20	# housed 3 to 4 per cage, then socially isolated for 11 to 16 days.
[... 900 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "offset": 920
}
```

```
920	  criterion: >-
921	    Bouts (M1) of ChR2 mice, OFF (baseline session) against ON (stimulation session); an
922	    unpaired test with P < 0.0001 from 6 mice implies bouts as units. Reproduced when both
923	    measures are larger ON with two-sided unpaired p < 0.0001; partially when p < 0.05.
924	    The same test in eYFP mice (Fig. 4f) is reported; the paper says the effects were absent
925	    there.
926	- id: fig4g-chr2-bout-number-unchanged
927	  statement: Stimulation does not change the total number of alcohol bouts.
928	  source: Figure 4g inset; Results, BLA–mPFC terminal stimulation increases alcohol drinking in males, paragraph 2
929	  quote: >-
930	    Analysis of lick microstructure revealed that BLA–mPFC activation prolonged individual
931	    alcohol drinking bouts (Fig. 4h ) and increased the number of licks per bout (Fig. 4i ),
932	    without changing the total number of bouts (Fig. 4g ).
933	  criterion: >-
934	    A claim of absence; no test named. Read as a two-sided paired t-test over the 6 ChR2 mice,
935	    bouts OFF against ON (two groups per Statistics section), p < 0.05. Reproduced when p >=
936	    0.05.
937	- id: fig5b-isolation-increases-mpfc-alcohol
938	  statement: Isolation increases mPFC neuron responses to alcohol.
939	  source: Figure 5b legend; Extended Data Fig. 8l legend; Results, Social isolation increases mPFC responses to alcohol while decreasing responses to sucrose in males, paragraph 2
[... 358 more lines not kept]
```

**Agent**

The checker reports 60 claims, 0 problems. Now reading the paper to check each claim.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02413-x.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41593-026-02413-x.txt').read()
i=t.find('Methods',52000)
print(len(t)); print(t[52000:90000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/04a00008-74d2-4579-9bc3-6b2c02d3ee7c/tool-results/bu0zubomz.txt"
}
```

```
1	129586
2	 evident at low current injection ranges, such near-threshold shifts can strongly influence synaptic integration and circuit recruitment. The bidirectional modulation of BLA–mPFC excitability across sexes may arise from differential regulation of calcium-activated or A-type potassium conductances that shape near-threshold firing. Notably, female mice also showed higher basal BLA–mPFC excitability than males, reflecting their greater baseline alcohol intake 34 . Together, these findings suggest that while the BLA–mPFC circuit tracks alcohol vulnerability in both sexes, its adaptation to social isolation is governed by sex-specific physiological mechanisms. In addition to the challenges of social isolation, group living in social hierarchies presents its own social stressors that influence alcohol use. Across sexes, subordinates drank more alcohol than dominants, and baseline BLA–mPFC excitability was higher in lower-ranked males. Moreover, BLA–mPFC responses to alcohol were more strongly correlated with alcohol intake in lower-ranked mice. This is likely motivated by the negative emotional states associated with social subordination rather than dominance or aggression 35 – 37 . In our study, social rank influenced alcohol but not water drinking, consistent with the idea that our limited-access paradigm engaged reward-driven rather than territorial motivation, which typically increases water drinking in dominant animals 38 . Together, these findings suggest that previous social experience and hierarchy history shape individual differences in alcohol-related behavior. Notably, the heightened BLA–mPFC excitability observed in subordinate mice likely influences downstream mPFC activity, potentially contributing to the maintenance of social rank. Earlier work shows that subordinates exhibit lower mPFC activity than dominants 39 , aligning with evidence that increased BLA activity predominantly inhibits mPFC neurons 24 , 27 , 28 . Together, these findings sugges
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41593-026-02413-x.txt').read()
i=t.find('Reporting Summary',95000)
j=t.find('reporting summary',100000)
import re
k=[m.start() for m in re.finditer('Data exclusions|Replication|Sample size|Randomization',t)]
print(k)
print(t[k[0]-3000:k[-1]+3000] if k else t[-15000:])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import fitz
d=fitz.open('paper/10.1038-s41593-026-02413-x.supp.pdf'); print(d.page_count)
for p in d: print(p.get_text()[:400]); print('----')
" 2>&1 | head -60; grep -n "baseline\|Lick microstructure\|3 s\|3-s" paper/10.1101-2023.11.09.566421.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
pdftotext paper/10.1038-s41593-026-02413-x.supp.pdf - 2>&1 | head -20; pdfinfo paper/10.1038-s41593-026-02413-x.supp.pdf 2>&1 | grep Pages
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02413-x.supp.pdf",
 "pages": "1"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "#    the plausible families.\nschema_version: 2",
 "new_string": "#    the plausible families.\n# M8 Rank in correlations. The Methods define relative rank as the proportion of wins (Methods,\n#    Tube dominance test); the legends correlate \"Rank\" and Extended Data Fig. 1a plots percent\n#    wins per rank. Readings (a) the integer rank within the cage (1 dominant), (b) the\n#    proportion of wins (sign reversed, so that larger means more subordinate).\nschema_version: 2"
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    housing within mouse) is shown as a variant. Reproduced when the three-way interaction has\n    p < 0.001 under the first reading, partially reproduced when 0.001 <= p < 0.05.",
 "new_string": "    housing within mouse) is shown as a variant. Reproduced when the three-way interaction has\n    p < 0.05 under the first reading (paper p < 0.001)."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    Rank as the integer rank within the cage (1 dominant); licks are baseline alcohol licks\n    (last 3 baseline days). The Bonferroni family is not stated; readings (a) two tests\n    (alcohol and water, panels c and d), (b) no correction. Reproduced when r2 is within\n    tolerance, the slope is positive with rank number, the corrected p < 0.05 under both\n    readings, and the one-way ANOVA over ranks has p < 0.05 with rank 4 highest.",
 "new_string": "    Rank under both M8 readings; licks are baseline alcohol licks (last 3 baseline days). The\n    Bonferroni family is not stated; readings (a) two tests (alcohol and water, panels c and\n    d), (b) no correction (the printed p = 0.01 matches the uncorrected p for r2 = 0.25 and\n    26 mice). Reproduced when r2 is within tolerance, licks rise toward subordinate ranks, the\n    corrected p < 0.05 under every reading, and the one-way ANOVA over integer ranks has p <\n    0.05 with rank 4 highest."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    A claim of absence on the paper's test, a Pearson correlation of rank with baseline water\n    licks at p < 0.05. Reproduced when p >= 0.05; r2 is given either way.",
 "new_string": "    A claim of absence on the paper's test, a Pearson correlation of rank (M8, both readings)\n    with baseline water licks at p < 0.05. Reproduced when p >= 0.05; r2 is given either way."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    Licks averaged over the 11 isolation days. Bonferroni readings (a) two tests (e and f), (b)\n    four tests (c to f). Reproduced when r2 for alcohol is within tolerance with p < 0.05 after\n    correction under both readings, and the water correlation has corrected p >= 0.05.",
 "new_string": "    Licks averaged over the 11 isolation days; rank under both M8 readings. The Bonferroni\n    family is not stated; read as two tests (e and f). A four-test family (c to f) is not\n    allowed: with r2 = 0.41 and 14 mice it gives p of about 0.054, against the printed p <\n    0.05. Reproduced when r2 for alcohol is within tolerance with corrected p < 0.05, and the\n    water correlation has corrected p >= 0.05."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    Baseline licks; one-tailed in the male direction for alcohol. Bonferroni over the two\n    tests (l, m). Reproduced",
 "new_string": "    Baseline licks; rank under both M8 readings; one-tailed in the male direction for alcohol.\n    The Bonferroni family is not stated; read as the two tests (l, m), which matches the\n    printed p = 0.04 for r2 = 0.46 and 9 mice. Reproduced"
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    M6, unlabeled neighbouring neurons of males. Reproduced when the interaction has p < 0.05\n    with isolated neurons firing more, and its F is smaller than that of\n    fig2c-male-blampfc-excitability-up.",
 "new_string": "    M6, unlabeled neighbouring neurons of males. Reproduced when the interaction has p < 0.05\n    with isolated neurons firing more, under both spike readings. The paper gives no measure of\n    \"minimal\"; the F and the size of the difference are reported beside those of\n    fig2c-male-blampfc-excitability-up, not tested."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    groups, read as two-sided unpaired, p < 0.05. Distance from the tracked body centre over the\n    stimulation epoch (tracking point not given; readings skull base and haunch). Reproduced\n    when neither comparison (ChrimsonR 15 against tdTomato 16; NpHR 16 against eYFP 16) has p <\n    0.05 under either reading.",
 "new_string": "    groups, read as two-sided unpaired, p < 0.05. How distance was tracked is not given:\n    behaviour was recorded with EthoVision (body-centre tracking) and pose was tracked with\n    SLEAP; readings the EthoVision body centre where the dataset holds it, and the SLEAP skull\n    base and haunch points. The epoch is not given; readings the 3-min stimulation epoch and\n    the whole 6-min interaction. Reproduced when neither comparison (ChrimsonR 15 against\n    tdTomato 16; NpHR 16 against eYFP 16) has p < 0.05 under any reading."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    Cue-onset z-scores per M3 with cue onset in place of bout onset and a 3-s pre-cue baseline.\n    Reproduced",
 "new_string": "    Cue-onset z-scores per M3 with cue onset in place of bout onset. The Methods give baselines\n    only for bouts (\"3- or 5-s\"); readings 3 s and 5 s before cue onset (the intertrial interval\n    of 53 to 73 s allows both). Reproduced, under both readings,"
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    Ward linkage, Euclidean distance on each neuron's mean alcohol z trace (M3), the cut set to",
 "new_string": "    One clustering of the 736 neurons of both populations pooled (\"Hierarchical clustering of\n    responses to alcohol for all recorded BLA neurons\", Results, paragraph 3). Ward linkage,\n    Euclidean distance on each neuron's mean alcohol z trace (M3), the cut set to"
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "  - test: two-way ANOVA, group by session interaction, Tukey post hoc\n    statistic: F(2, 20) = 4.7\n    p: 0.02\n    n: 6 ChR2 and 6 eYFP male mice\n  criterion: >-\n    Alcohol licks per session for baseline, stimulation and recovery sessions (Methods,\n    Optogenetic stimulation during 2BC drinking). Two-way ANOVA group by session, session\n    repeated (df 20 = 2 times 10). Baseline read as the last baseline session; the mean of the\n    last 3 baseline days is a variant. Reproduced when the interaction has p < 0.05, Tukey shows\n    ChR2 stimulation above ChR2 baseline, and ChR2 recovery is not above baseline at p < 0.05.",
 "new_string": "  - test: two-way ANOVA, Tukey post hoc (effect not named)\n    statistic: F(2, 20) = 4.7\n    p: 0.02\n    n: 6 ChR2 and 6 eYFP male mice\n  criterion: >-\n    Alcohol licks per session for baseline, stimulation and recovery sessions (Methods,\n    Optogenetic stimulation during 2BC drinking). Two-way ANOVA group by session, session\n    repeated (df 20 = 2 times 10). The legend does not say which effect F(2, 20) is; both the\n    session main effect and the group by session interaction have these df, so both are\n    readings. Baseline is not defined; readings the last baseline session and the mean of the\n    last 3 baseline days (Methods, 2BC drinking). Reproduced when, under every reading, the\n    effect has p < 0.05, Tukey shows ChR2 stimulation above ChR2 baseline, and ChR2 recovery is\n    not above baseline at p < 0.05; methods_underspecified when readings disagree."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    Bouts (M1) of ChR2 mice, OFF (baseline session) against ON (stimulation session); an\n    unpaired test with P < 0.0001 from 6 mice implies bouts as units. Reproduced when both\n    measures are larger ON with two-sided unpaired p < 0.0001; partially when p < 0.05.",
 "new_string": "    Bouts (M1) of ChR2 mice, OFF against ON (stimulation session); an unpaired test with P <\n    0.0001 from 6 mice implies bouts as units. Every lick onset triggers stimulation in the\n    test session, so OFF is another session, not named; readings the preceding baseline\n    session and the recovery session. Reproduced when, under both readings, both measures are\n    larger ON with two-sided unpaired p < 0.0001; partially when p < 0.05."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    M3 alcohol responses of mPFC neurons on nonstimulated trials of the alcohol stimulation\n    session before and after isolation (imaging was obtained during the stimulation sessions,\n    Methods, Optogenetic stimulation and calcium imaging during cued-2BC drinking; the neuron\n    counts equal those of Fig. 6c,f). Neurons are units. Reproduced when the isolated mean\n    exceeds the group-housed mean with one-sided p < 0.05; the two-sided p of Extended Data\n    Fig. 8l is reported.",
 "new_string": "    M3 alcohol responses of mPFC neurons in the alcohol stimulation session before and after\n    isolation (imaging was obtained during the stimulation sessions, Methods, Optogenetic\n    stimulation and calcium imaging during cued-2BC drinking; the neuron counts equal those of\n    Fig. 6c,f). Which trials enter is not said; readings (a) nonstimulated trials only, (b) all\n    trials. Neurons are units. Reproduced when, under both readings, the isolated mean exceeds\n    the group-housed mean with one-sided p < 0.05; the two-sided p of Extended Data Fig. 8l is\n    reported (its p = 0.03 is not twice 0.006, so the two panels may use different trials)."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    A claim of absence on the test of fig5b-isolation-increases-mpfc-alcohol applied to water\n    bouts; neither direction is stated, so two-sided unpaired t-test at p < 0.05. Reproduced\n    when p >= 0.05.",
 "new_string": "    A claim of absence on the test of fig5b-isolation-increases-mpfc-alcohol applied to water\n    bouts, both trial readings; neither direction is stated, so two-sided unpaired t-test at p\n    < 0.05. Reproduced when p >= 0.05 under both."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    sessions. Reproduced when the isolated mean is below the group-housed mean with one-sided p\n    < 0.05. Extended Data Fig. 8g",
 "new_string": "    sessions, both trial readings. Reproduced when, under both, the isolated mean is below the\n    group-housed mean with one-sided p < 0.05. Extended Data Fig. 8g"
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    After isolation, BLA-mPFC stimulation decreases mPFC responses to alcohol, reversing its\n    group-housed effect.",
 "new_string": "    After isolation, BLA-mPFC stimulation decreases mPFC responses to alcohol."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    Per neuron, scalar M3 social response (0 to 3 s) with and without stimulation. Bonferroni\n    over the two tests. Reproduced when the group-housed r is negative with corrected p < 0.05\n    and the isolation correlation has corrected p >= 0.05, under both baseline readings.",
 "new_string": "    Per neuron, scalar M3 social response (0 to 3 s) with and without stimulation. The\n    Bonferroni family is not stated. A two-test family cannot give the printed p = 0.04: with\n    r2 = 0.02 and 199 neurons the uncorrected p is about 0.046, and r2 below 0.025 keeps the\n    doubled p above 0.05. Readings (a) uncorrected, (b) two tests, reported both; the outcome\n    is judged on (a), the only reading consistent with the printed numbers. Reproduced when the\n    group-housed r is negative with p < 0.05 and the isolation correlation has p >= 0.05, under\n    both baseline readings."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    mPFC activity decodes social interaction above chance; isolation lowers decoding accuracy,\n    and BLA-mPFC stimulation raises it in both housing conditions, rescuing it after\n    isolation.",
 "new_string": "    In group-housed mice mPFC activity decodes social interaction above chance with and\n    without stimulation; isolation abolishes decoding without stimulation and lowers accuracy,\n    and BLA-mPFC stimulation raises accuracy in both housing conditions, rescuing it after\n    isolation."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    per cell, so k = 10 folds here (readings: 10 folds; 5 folds repeated twice). Reproduced\n    when, under every reading, real exceeds shuffled in all four sessions (p < 0.05),\n    isolation no-stimulation accuracy is below group-housed no-stimulation (unpaired p <\n    0.05), and stimulation exceeds no-stimulation in both housing conditions (unpaired p <\n    0.05). Partially reproduced when some but not all of these hold.",
 "new_string": "    per cell, so k = 10 folds here (readings: 10 folds; 5 folds repeated twice). Panels k and l\n    are read as one two-way ANOVA per housing condition, data (real, shuffled) by stimulation,\n    over fold accuracies (2 by 2 by 10 values, error df 36). Reproduced when, under every\n    reading, the group-housed ANOVA has a real against shuffled main effect at p < 0.05 with\n    real above shuffled in both stimulation conditions (Sidak); the isolation ANOVA has a data\n    by stimulation interaction at p < 0.05, with isolation no-stimulation accuracy not above\n    shuffled and stimulation accuracy above shuffled (Sidak); isolation no-stimulation\n    accuracy is below group-housed no-stimulation (unpaired p < 0.05); and stimulation exceeds\n    no-stimulation in both housing conditions (unpaired p < 0.05). Partially reproduced when\n    some but not all of these hold."
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent**

Now adding a claim for Extended Data Fig. 8o,p, which had none, and the checks entry.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "    two-sided. Reproduced when the inhibited proportion falls with p < 0.05 and the excited\n    proportion does not change at p < 0.05.\n- id: fig6q-nphr-decreases-alcohol-bouts",
 "new_string": "    two-sided. Reproduced when the inhibited proportion falls with p < 0.05 and the excited\n    proportion does not change at p < 0.05.\n- id: ed8op-stim-no-alcohol-proportions-si\n  statement: >-\n    During isolation, BLA-mPFC stimulation does not change the proportions of mPFC neurons\n    excited or inhibited by alcohol.\n  source: Extended Data Fig. 8o,p legend\n  quote: >-\n    BLA-mPFC stimulation did not alter the proportion of mPFC neurons responsive to alcohol\n    during social isolation.\n  criterion: >-\n    A claim of absence. No test is named; the test of the neighbouring panels (Extended Data\n    Fig. 8m,n), a two-sided paired t-test over the 5 mice of the isolation alcohol stimulation\n    session, on the percentages of neurons excited and inhibited per M4 threshold, stimulated\n    against nonstimulated trials, at p < 0.05. Reproduced when neither reaches p < 0.05.\n- id: fig6q-nphr-decreases-alcohol-bouts"
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001454/10.1038-s41593-026-02413-x.yaml",
 "old_string": "  source: Figure 6g–j legends; Results, BLA–mPFC",
 "new_string": "  source: Figure 6g–j legends; Extended Data Fig. 8q,r legend; Results, BLA–mPFC"
}
```

```
The file claims/001454/10.1038-s41593-026-02413-x.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cat >> claims/001454/10.1038-s41593-026-02413-x.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header, added M8. The Methods define rank as the proportion of wins, the legends correlate "Rank"; both are now named readings, used in ed1c, ed1d, ed1e and ed1l.
  - fig1-threeway-sex-liquid-housing, the reproduced threshold was p < 0.001 with a partial grade below 0.05; the statement says only that the interaction is significant, so reproduced is now p < 0.05.
  - ed1c-rank-alcohol-males, rank readings added (M8); noted that the printed p = 0.01 matches the uncorrected p, which supports the no-correction reading.
  - ed1e-rank-alcohol-isolation, the four-test Bonferroni reading was dropped; with r2 = 0.41 and 14 mice it gives p of about 0.054, which the printed p < 0.05 excludes.
  - ed1l-rank-alcohol-females, the two-test Bonferroni family is now said to be a reading, checked against the printed p.
  - ed2e-nonspecific-bla-excitability, removed the requirement that its F be smaller than that of Fig. 2c; no part of the paper sets that test, and F values with different df are not comparable. Both spike readings now required.
  - ed4gm-locomotion-unchanged, the tracking source and the epoch are not given; readings added (EthoVision body centre or SLEAP points; 3-min stimulation epoch or the 6-min interaction).
  - ed5d-cue-response-modest, the 3-s pre-cue baseline was a choice; the Methods allow 3 or 5 s, now both readings.
  - fig3f-blampfc-distinct-clusters, added that the clustering is one clustering of both populations pooled, as the Results state.
  - fig4e-chr2-increases-alcohol, the legend does not name the effect of F(2, 20); the interaction was assumed. Session main effect and interaction are now both readings, as are the two baseline definitions (the mean of 3 days had been a variant only).
  - fig4hi-chr2-longer-bouts, OFF was fixed as the baseline session without a source; every lick triggers stimulation in the test session, so baseline and recovery sessions are now both readings.
  - fig5b, fig5c, fig5d, which trials of the stimulation sessions give the housing comparison is not said; nonstimulated only and all trials are now both readings.
  - fig6f-stim-decreases-mpfc-alcohol-si, removed "reversing its group-housed effect" from the statement; the paper does not say it.
  - fig6gj-stim-no-water-effect, source extended to Extended Data Fig. 8q,r, which shows the isolation water proportions the statement covers.
  - ed9hi-stim-inverts-social-response, a two-test Bonferroni cannot give the printed p = 0.04 with r2 = 0.02 and 199 neurons; the outcome is now judged uncorrected, the two-test result reported.
  - ed9k-o-social-decoding, the criterion required above-chance decoding in all four sessions, but the legend of panel l says isolation abolishes decoding without stimulation. Statement and criterion rewritten to the legends of k to o.
  - Added ed8op-stim-no-alcohol-proportions-si (Extended Data Fig. 8o,p), a finding with no claim.
  - Open, Supplementary Tables 1 and 2 are not in the text read; supt1 claims carry no numbers.
  - Open, ed9fg error df 7350 and fig6q error df 13 do not match the stated n; recorded in the claims, not resolved.
  - Open, Extended Data Fig. 1o-q (licking by sex within each rank) and Extended Data Fig. 9r have no claim; they are secondary panels.
  - Open, the grouping of Extended Data Fig. 4 readings (UMAP clusters or time bins) and the Fig. 1d time blocks are readings, not given by the paper; the criteria block on disagreement.
EOF
python tools/claims_check.py claims/001454/10.1038-s41593-026-02413-x.yaml paper/10.1038-s41593-026-02413-x.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^checks:/,$p' claims/001454/*.yaml | grep -n ': .*: \|—\|rather' ; git diff --stat
```

```
claims/001454/10.1038-s41593-026-02413-x.yaml | 173 ++++++++++++++++++--------
 1 file changed, 121 insertions(+), 52 deletions(-)
```

**Agent**

I made 17 corrections and the file is ready for an attempt, with four problems left open that the criteria already handle.

**Checker:** `claims/001454/10.1038-s41593-026-02413-x.yaml: 61 claims, 61 quotes, 64 statistical values, 0 problems`. It reported 60 claims and 0 problems before my edits.

**Changes, by claim**
- **Header:** added M8. The Methods define rank as the proportion of wins, but the legends correlate "Rank", so both are now readings. ed1c, ed1d, ed1e and ed1l use them.
- **fig1-threeway-sex-liquid-housing:** reproduced is now p < 0.05. It had been p < 0.001, stricter than the statement, which only says the interaction is significant.
- **ed1c:** added the M8 readings. The printed p = 0.01 equals the uncorrected p, which supports the no-correction reading.
- **ed1e:** dropped the four-test Bonferroni reading. With r² = 0.41 and 14 mice it gives p ≈ 0.054, which the printed p < 0.05 rules out.
- **ed1l:** the two-test Bonferroni family is now marked as a reading; it fits the printed p.
- **ed2e:** removed an invented condition (its F smaller than Fig. 2c's). Both spike readings are now required.
- **ed4gm:** the paper gives neither the tracking source nor the time window. Added readings: EthoVision body centre or SLEAP points, over the 3-min stimulation epoch or the whole 6-min interaction.
- **ed5d:** the cue baseline is now read as 3 s or 5 s, as the Methods allow. Only 3 s had been used.
- **fig3f:** stated that the clustering pools both populations, as the Results say.
- **fig4e:** the legend does not say which effect F(2, 20) is. Both the session main effect and the interaction are now readings, as are both baseline definitions.
- **fig4hi:** the "OFF" bouts had been fixed to the baseline session with no source. Baseline and recovery sessions are now both readings.
- **fig5b, fig5c, fig5d:** the paper does not say which trials enter the housing comparison. Nonstimulated trials only and all trials are now both readings.
- **fig6f:** removed "reversing its group-housed effect" from the statement, since the paper does not say that.
- **fig6gj:** the source now includes Extended Data Fig. 8q,r.
- **ed9hi:** a two-test Bonferroni cannot give the printed p = 0.04 at r² = 0.02 with 199 neurons. The outcome is now judged uncorrected, with the corrected result reported.
- **ed9k-o:** the criterion required above-chance decoding in all four sessions, but the panel l legend says isolation abolishes decoding without stimulation. I rewrote the statement and criterion to match the k to o legends.
- **New claim ed8op-stim-no-alcohol-proportions-si:** Extended Data Fig. 8o,p had no claim.

**Open**
- Supplementary Tables 1 and 2 are not in the text, so the two supt1 claims carry no numbers.
- The error df in ed9fg (7350) and fig6q (13) do not match the stated sample sizes.
- Several groupings are readings the paper does not give: the Fig. 1d time blocks and the Extended Data Fig. 4 levels (UMAP clusters or time bins). If the readings disagree, the criteria return methods_underspecified.
- Extended Data Fig. 1o–q and 9r have no claim; they are secondary panels.

**Ready:** yes (`ready: true` in the new checks entry). Nothing was committed or pushed.

## End of run

36 turns, 4 minutes, result: success.
