# crcns-pag-2 · claims · run 42194432415

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/001453/ claims/crcns-pag-2 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,185p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 301 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; cat paper/10.1038-s41598-020-74457-3.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41598-020-74457-3.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41598-020-74457-3.txt",
 "offset": 138
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat paper/pag-2.data-description.txt | head -150; sed -n 1,40p tools/claims_check.py; ls claims | head; ls claims/*/ | grep -i crcns
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 150,400p paper/pag-2.data-description.txt | grep -v "^ *$" | tail -120; ls claims/crcns-*/; head -50 claims/crcns-bf-1/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -m5 -A4 "^schema_version" claims/crcns-bf-1/*.yaml; grep -n "data:" claims/crcns-*/*.yaml | awk '{print $NF}' | sort | uniq -c; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:5000])"
```

```
57:schema_version: 2
58-dataset:
59-  archive: crcns
60-  id: bf-1
61-  doi: 10.6080/K0MK6B2Q
      2 with_inputs
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
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[5000:11000])"
```

```
'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
      "type": "string",
      "minLength": 1
     }
    },
    "allOf": [
     {
      "not": {
       "required": [
        "quote",
        "inferred"
       ]
      }
     },
     {
      "if": {
       "properties": {
        "kind": {
         "const": "link"
        }
[... 178 more lines not kept]
```

**Agent**

Now checking whether the lab's linked resources page can be reached.

**Agent calls Bash**

```bash
curl -sL -m 20 https://mcdannaldlab.org/resources | sed 's/<[^>]*>/ /g' | tr -s ' \n' | head -c 3000; echo; echo EXIT $?
```

Result: the fetched text is not kept.

**Agent**

The lab's resources page returns 404, so no code can be read. Before writing, I'm checking which chi-square variant gives the reported value.

**Agent calls Bash**

```bash
python -c "
from scipy.stats import chi2_contingency as c
t=[[133,70],[80,71]]
print(c(t,correction=False)[:2], c(t)[:2])
t=[[32+48,151-80],[49+84,203-133]]
from scipy.stats import norm
for z in (3.80,3.05,1.04,1.43,0.60): print(z, norm.sf(z), 2*norm.sf(z))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy.stats import chi2_contingency as c
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
python -c "
import math
a,b,c_,d=133,70,80,71
n=a+b+c_+d
def chi(y):
  return n*max(0,abs(a*d-b*c_)-y*n/2)**2/((a+b)*(c_+d)*(a+c_)*(b+d))
print(chi(0),chi(1))
sf=lambda z:0.5*math.erfc(z/2**.5)
for z in (3.80,3.05,1.04,1.43,0.60): print(z, sf(z), 2*sf(z))
"
```

```
5.67900602782931 5.167928328132761
3.8 7.234804392512014e-05 0.00014469608785024028
3.05 0.0011442068310227003 0.0022884136620454007
1.04 0.14916995033098143 0.29833990066196286
1.43 0.07635850953673912 0.15271701907347823
0.6 0.2742531177500736 0.5485062355001472
```

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-pag-2/10.1038-s41598-020-74457-3.yaml",
 "content": "# Claims for Moaddab, Wright & McDannald (2020), Sci Rep 10, 18035, on CRCNS data set pag-2.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-06,\n# protocol as stated in docs/protocol.md (Reader, version pilot-13).\n#\n# Text read: the version of record, PMC7582948 (open access), as supplied under paper/ (Europe PMC\n# JATS XML, flattened), with its Introduction, Materials and methods, Results, figure legends and\n# Discussion. The supplement (Supplementary Figures S1 to S6 and a Supplementary Information file)\n# is listed in the text, but its content is not in the text supplied, and no PDF was supplied.\n# The main results are stated, with their statistics, in the main text, so they do not rest on the\n# supplement; the claims that are shown only in Figs. S4 to S6 are kept from the sentences of the\n# Results that cite them, and have no expected values. The paper links no analysis code for the\n# neural analyses. It says Med Associates programs and Matlab programs for the behavioral\n# analyses are at https://mcdannaldlab.org/resources; on 2026-11-06 that address returned a 404\n# page, so no code was read and no repository or commit can be recorded. The two web calculators\n# the Methods name (socscistatistics.com chi-square; vassarstats.net r-to-z) were not run. Two\n# facts about them were checked arithmetically from the paper's own numbers (see the claims on\n# Fig. 2D and Figs. 6 and 7).\n#\n# Data the paper used. 20 female Long Evans rats born in the laboratory: 12 given early adolescent\n# adversity (EAA; P26 to P35, twice daily, tail pinch, restraint, forced cold swim, cat hair, five\n# times each) and 8 Controls (Con), handled but not stressed. Body weight taken Monday, Wednesday\n# and Friday from P24 to P55 (14 days). Eight pre-surgery fear discrimination sessions (P64 to\n# P71), then 16-wire drivable bundles implanted dorsal to the vlPAG (P77 to P87), then recording\n# sessions (about P90 to P143). Each session has 32 trials: 6 danger (shock p = 1.00), 6\n# uncertainty shock and 10 uncertainty no-shock (p = 0.375), and 10 safety (p = 0.00); 10 s\n# auditory cues; 0.5 mA, 0.5 s shock 2 s after cue offset; mean inter-trial interval 3.5 min.\n# Fear is the suppression of rewarded nose poking (VI-60). Recorded: 151 single units in 8 Con rats\n# over 72 sessions and 203 units in 12 EAA rats over 107 sessions, in vlPAG/DR; spike times, cue,\n# shock and nose poke times; mean waveforms. Bregma recording level per rat.\n#\n# The CRCNS data set, by its title and data description, holds these recordings: the 354 sorted\n# units (151 Con, 203 EAA) from the 179 recording sessions, one file per unit, with trial-aligned\n# firing, nose poke and suppression ratio data, waveforms and unit names that carry the rat and\n# session date. By that description it holds no body weights and no pre-surgery discrimination\n# sessions; the claims that need those are kept as the paper's findings, and the author finds\n# whether the data set holds their data. The data description also says the electrode bundle was\n# centered at -7.68, -7.92, -8.16 or -8.40 mm from bregma (6, 7, 5 and 2 rats).\n#\n# Method details from the Methods, used by the claims below unless a claim says otherwise.\n# - Trial types: danger, uncertainty (shock and no-shock trials pooled, 16 trials, as the Methods\n#   say uncertainty trial types were collapsed for the cue analyses) and safety.\n# - Suppression ratio per trial: (baseline poke rate - cue poke rate) / (baseline + cue), baseline\n#   from the 20 s before cue onset, cue rate from the 10 s cue, each trial with its own baseline.\n# - Normalized firing: per neuron and trial type, firing rate in 250 ms bins from 20 s before cue\n#   onset to 20 s after cue offset (200 bins), averaged over trials; the mean of the 2 s before cue\n#   onset for that trial type subtracted from each bin; the result Z scored across all trial types\n#   of the neuron (all bins together). Population ANOVAs use bins from 2 s before cue onset to 2 s\n#   after cue offset (56 bins).\n# - Cue-responsive selection (Methods, Identifying cue-responsive neurons; Results, Higher\n#   proportion, paragraph 2): raw firing rate in the 10 s before cue onset against cue epochs,\n#   dependent samples t test across trials, per cue, at p < 0.0083 (six comparisons).\n# - Single-unit regression: per neuron, all 32 trials of its session; the response is the Z score\n#   normalized firing in the interval; regressors are the trial's suppression ratio for the whole\n#   cue (fear output) and the cue's shock probability, 1.00, 0.375 or 0.00 (threat probability),\n#   with a constant, by ordinary least squares (Matlab regress). The betas are analyzed per\n#   neuron; 1 s intervals over the 10 s cue.\n#\n# Details the paper leaves open that apply to many claims, with the readings it allows.\n# - Trial-wise normalized firing for the regression. The Z score of the Methods is defined on\n#   trial-averaged firing. Readings: (a) each trial's firing in the interval, minus the 2 s\n#   pre-cue mean of its trial type, Z scored with the mean and SD of that neuron's normalization;\n#   (b) the same, with the trial's own 2 s baseline subtracted; (c) each trial's binned firing Z\n#   scored over all trials and bins of the neuron. Reading (a) follows the Methods most closely.\n# - Trials with no pokes in the baseline and the cue make the suppression ratio 0/0. The paper\n#   does not say how they are treated. Readings: (a) ratio set to 0; (b) trial left out.\n# - Beta for a multi-second window (whole cue, last 5 s). Readings: (a) the mean of the 1 s\n#   interval betas over the window, as the Results say for Fig. 5C (\"mean beta coefficient for\n#   the entirety of cue presentation\"); (b) one regression on the firing averaged over the window.\n# - Error degrees of freedom. Several reported tests have fewer degrees of freedom than the\n#   neuron counts give (Fig. 5A to C, t 66 and F 1,65 for 81 cue-excited neurons; Fig. 5D, F 1,78;\n#   Fig. 4A,B, F 110,8360; Fig. 2E,F, F 2,346 for 354 neurons). The paper does not say which\n#   neurons were left out. The author runs the tests on all selected neurons, reports the degrees\n#   of freedom obtained, and treats a mismatch as a deviation, not as a failure of the claim.\n# - ANOVA. The paper reports partial eta squared and observed power (SPSS style) but does not name\n#   the software or the sphericity correction. Readings: uncorrected repeated-measures ANOVA with\n#   neurons (or rats) as subjects; the reported degrees of freedom are uncorrected.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: pag-2\n  doi: 10.6080/K0833Q7F\npaper: doi:10.1038/s41598-020-74457-3\nclaims:\n- id: fig1bc-adversity-slows-weight-gain\n  statement: Early adolescent adversity slowed body weight gain. Body weight showed a group by\n    day interaction, and Control rats gained more weight from P24 to P35 (P35/P24) than EAA rats;\n    weights were equivalent before adversity and in adulthood.\n  source: Results, first paragraph (before the heading Higher proportion of EAA cue-responsive\n    neurons); Figure 1B and 1C\n  quote: Body weights were equivalent prior to adversity, weight gain slowed in EAA rats, but body\n    weights were equivalent between groups in adulthood. ... found a significant group × day\n    interaction (F 13,234 = 4.20, p = 3.00 × 10 –6 ... Independent samples t test for body weight\n    change found a significant difference between groups (t 18 = 6.11, p = 9.00 × 10 –6\n  statistics:\n  - about: body weight, group by day interaction, 14 days from P24 to P55\n    test: repeated-measures ANOVA\n    statistic: F(13, 234) = 4.20\n    p: 3.0e-06\n    n: 8 Con and 12 EAA rats\n  - about: body weight change P35/P24, Con against EAA\n    test: independent samples t test\n    statistic: t(18) = 6.11\n    p: 9.0e-06\n    n: 8 Con and 12 EAA rats\n  criterion: As the Methods (Body weight) say. A repeated-measures ANOVA of body weight on day (14\n    weighing days, P24 to P55) by group, and an independent samples t test of P35 weight divided by\n    P24 weight between groups. Reproduced when the interaction has p < 0.05 and the t test has p <\n    0.05 with the Control ratio higher. The sign of the difference is as Fig. 1C shows it (Control\n    gained more).\n- id: fig1ef-acquisition-equivalent-final\n  statement: Both groups acquired fear discrimination over the eight pre-surgery sessions (danger\n    > uncertainty > safety). EAA rats acquired it faster, giving a group by cue by session\n    interaction, but in the final session there was a main effect of cue and no group by cue\n    interaction.\n  source: Results, paragraph 3 (Control and EAA rats acquired discrimination); Figure 1E and 1F\n  quote: EAA rats acquired discrimination faster than Controls, but discrimination levels were\n    equivalent between groups by the final discrimination session ... found a group × cue ×\n    session interaction (F 14,252 = 1.99, p = 0.02 ... ANOVA restricted to the final\n    discrimination session found a main effect of cue (F 2,36 = 151.45, p = 2.97 × 10 –18 ... but\n    no group × cue interaction (F 2,36 = 1.55, p = 0.23\n  statistics:\n  - about: group by cue by session, sessions 1 to 8\n    test: ANOVA, repeated measures on session, factors group and cue\n    statistic: F(14, 252) = 1.99\n    p: 0.02\n  - about: final session, main effect of cue\n    test: ANOVA\n    statistic: F(2, 36) = 151.45\n    p: 2.97e-18\n  - about: final session, group by cue\n    test: ANOVA\n    statistic: F(2, 36) = 1.55\n    p: 0.23\n  criterion: Per rat, the mean suppression ratio per cue and session (Methods, Calculating\n    suppression ratios), uncertainty shock and no-shock trials pooled. Reproduced when the\n    three-way interaction has p < 0.05, the final-session cue effect has p < 0.05 with danger >\n    uncertainty > safety in both groups, and the final-session group by cue interaction has p >=\n    0.05 (the absence part is judged on that ANOVA). Needs the eight pre-surgery sessions, which\n    the data description does not list.\n- id: fig2b-baseline-poke-equivalent\n  statement: Control and EAA rats had equivalent baseline nose poke rates during recording\n    sessions.\n  source: Results, Higher proportion of EAA cue-responsive neurons, paragraph 1; Figure 2B\n  quote: Control and EAA rats showed equivalent baseline nose poke rates (t 18 = 1.24, p = 0.23\n  statistics:\n  - test: independent samples t test\n    statistic: t(18) = 1.24\n    p: 0.23\n    n: 8 Con and 12 EAA rats\n  criterion: A claim of absence, judged on the paper's test, an independent samples t test on one\n    baseline nose poke rate per rat (two-sided, alpha 0.05). The paper does not say which baseline\n    window or how sessions are combined. Readings for the window are (a) the 20 s before cue onset,\n    as for the suppression ratio (Methods); (b) the baseline nose poke rate field the data set\n    provides. Sessions are averaged per rat. Reproduced when p >= 0.05; the group means are\n    reported either way.\n- id: fig2c-recording-discrimination\n  statement: During recording sessions both groups showed high fear to danger, less to\n    uncertainty and least to safety, with a main effect of cue, no group by cue interaction, and\n    each cue pair differing in each group.\n  source: Results, Higher proportion of EAA cue-responsive neurons, paragraph 1; Figure 2C\n  quote: ANOVA for mean suppression ratios [factors ... found a main effect of cue (F 2,36 =\n    199.47, p = 3.33 × 10 –20 ... but no group × cue interaction (F 2,36 = 0.24, p = 0.79 ...\n    Paired samples t tests confirmed differing ratios for each group and cue (danger vs.\n    uncertainty; uncertainty vs. safety; all t > 3.00, all p ≤ 0.01)\n  statistics:\n  - about: main effect of cue\n    test: ANOVA, factors group and cue\n    statistic: F(2, 36) = 199.47\n    p: 3.33e-20\n  - about: group by cue\n    test: ANOVA, factors group and cue\n    statistic: F(2, 36) = 0.24\n    p: 0.79\n  - about: danger against uncertainty and uncertainty against safety, each group\n    test: paired samples t test\n    statistic: all t > 3.00\n    p: 0.01\n    p_relation: \"<\"\n  criterion: Per rat, the mean suppression ratio for danger, uncertainty (shock and no-shock pooled)\n    and safety over all its recording sessions (Fig. 2C legend). The paper does not say whether\n    the rat's value is the mean of its session means or of all its trials pooled; both are\n    readings. Mixed ANOVA, cue within, group between. Reproduced when the cue effect has p < 0.05,\n    the group by cue interaction has p >= 0.05 (absence judged on that ANOVA), and all four paired\n    t tests (two pairs in two groups) have p <= 0.01 with danger > uncertainty > safety. The\n    reported p <= 0.01 is recorded as a bound.\n- id: fig2d-cue-responsive-counts\n  statement: 32 of 151 Control neurons (21.2%) and 49 of 203 EAA neurons (24.1%) were cue-excited;\n    48 of 151 Control neurons (31.8%) and 84 of 203 EAA neurons (41.4%) were cue-inhibited.\n  source: Results, Higher proportion of EAA cue-responsive neurons, paragraph 2; Figure 2D\n  quote: We identified 32/151 Control neurons (21.2%) and 49/203 EAA neurons (24.1%) that were\n    cue-excited ... We identified 48/151 Control neurons (31.8%) and 84/203 EAA neurons (41.4%)\n    that were cue-inhibited\n  expected:\n  - quantity: Control cue-excited neurons\n    value: 32\n    tolerance: 3.2\n  - quantity: EAA cue-excited neurons\n    value: 49\n    tolerance: 4.9\n  - quantity: Control cue-inhibited neurons\n    value: 48\n    tolerance: 4.8\n  - quantity: EAA cue-inhibited neurons\n    value: 84\n    tolerance: 8.4\n  - quantity: total units, Control\n    value: 151\n    tolerance: 0\n  - quantity: total units, EAA\n    value: 203\n    tolerance: 0\n  criterion: Selection as the Methods (Identifying cue-responsive neurons) and Results give it. Per\n    neuron and cue (danger, uncertainty with its 16 trials pooled, safety), raw firing rate in the\n    10 s before cue onset against the rate in each of two cue epochs, dependent samples t test\n    across trials, two-sided, at p < 0.0083 (0.05/6). Cue-excited is a significant increase in at\n    least one of the six tests and no significant decrease; cue-inhibited the reverse; all other\n    neurons are outside the criteria. The epochs differ between the texts. Readings are (a) first\n    1 s and last 5 s of the cue for both types (Methods, \"first 1 s cue interval or the final 5 s\n    cue interval\"); (b) first 1 s and last 5 s for excitation, first 5 s and last 5 s for\n    inhibition (Results); (c) the three epochs first 1 s, first 5 s and last 5 s for both types.\n    Reproduced when all four counts are within tolerance under one reading, and the unit totals\n    match exactly. The unit counts are a check of the data, not a finding.\n- id: fig2d-higher-proportion-responsive\n  statement: A higher proportion of EAA neurons than Control neurons were cue-responsive (133/203,\n    65.5%, against 80/151, 53.0%).\n  source: Results, Higher proportion of EAA cue-responsive neurons, paragraph 2; Figure 2D\n  quote: Combining the cue-excited and cue-inhibited populations in each group revealed a higher\n    proportion of EAA cue-responsive neurons (133/203, 65.5%) compared to Controls (80/151, 53.0%);\n    χ 2 = 5.68, p = 0.02\n  statistics:\n  - test: Chi-square test\n    statistic: chi-square = 5.68\n    p: 0.02\n    n: 151 Con and 203 EAA neurons\n  depends_on:\n  - fig2d-cue-responsive-counts\n  expected:\n  - quantity: EAA cue-responsive fraction\n    value: 0.655\n    tolerance: 0.0655\n  - quantity: Control cue-responsive fraction\n    value: 0.53\n    tolerance: 0.053\n  criterion: Cue-responsive is cue-excited plus cue-inhibited, under the readings of\n    fig2d-cue-responsive-counts. A 2 by 2 Pearson chi-square test (responsive or not, by group)\n    without continuity correction; the paper's counts give 5.68 only without the Yates\n    correction, so that is the test the Methods' web calculator ran. Reproduced when both\n    fractions are within tolerance and the test has p < 0.05 with EAA higher, under one reading.\n- id: fig2ef-baseline-firing\n  statement: Baseline firing rates did not differ between Control and EAA neurons of any\n    functional type, while across groups baseline firing differed by functional type and was\n    lowest for cue-excited neurons.\n  source: Results, Higher proportion of EAA cue-responsive neurons, paragraph 3; Figure 2E and 2F\n  quote: Independent samples t tests found no differences in baseline firing between Control and\n    EAA cue-excited, cue-inhibited and neurons outside the selection criteria (all t < 1.10, all p\n    > 0.25). By contrast, one-way ANOVA for the three functional neuron types, collapsing across\n    Control and EAA groups found a main effect of functional type (F 2,346 = 7.35, p = 0.001).\n    Baseline firing rates were lowest for cue-excited neurons.\n  statistics:\n  - about: Con against EAA, each functional type\n    test: independent samples t test\n    statistic: all t < 1.10\n    p: 0.25\n    p_relation: \">\"\n  - about: functional type, groups pooled\n    test: one-way ANOVA\n    statistic: F(2, 346) = 7.35\n    p: 0.001\n  depends_on:\n  - fig2d-cue-responsive-counts\n  criterion: Baseline firing per neuron, raw rate. The paper does not fix the window. Readings are\n    (a) the 10 s before cue onset over all trials (the selection baseline); (b) the 2 s before\n    cue onset (the normalization baseline). The group comparisons are a claim of absence, judged\n    on three two-sided independent samples t tests at alpha 0.05 (the paper names no correction);\n    the type effect is a one-way ANOVA over the three types, groups pooled. Reproduced when no t\n    test has p < 0.05, the ANOVA has p < 0.05, and cue-excited neurons have the lowest mean, under\n    one reading. The degrees of freedom (346 against 351 for 354 neurons) are reported as obtained.\n- id: fig4ab-excited-temporal-pattern\n  statement: Control and EAA cue-excited neurons differed in the temporal pattern of their\n    cue-selective firing, a group by cue by bin interaction that held with bregma recording level\n    as a factor.\n  source: Results, Inflated cue responses in EAA neurons, paragraph 1; Figure 4A and 4B\n  quote: Critically, the temporal pattern of selective firing differed for Control and EAA\n    cue-excited neurons. ... revealed a group × cue × bin interaction (F 110,8360 = 3.32, p = 3.13 ×\n    10 –28 ... The interaction held when bregma recording level was included as an ANOVA factor (F\n    110,8360 = 1.49, p = 0.001\n  statistics:\n  - about: group by cue by bin\n    test: ANOVA, factors group, cue and bin\n    statistic: F(110, 8360) = 3.32\n    p: 3.13e-28\n    n: 32 Con and 49 EAA cue-excited neurons\n  - about: group by cue by bin, with bregma level as a factor\n    test: ANOVA\n    statistic: F(110, 8360) = 1.49\n    p: 0.001\n  depends_on:\n  - fig2d-cue-responsive-counts\n  criterion: Normalized firing (opening comment) for danger, uncertainty and safety, 56 bins of\n    250 ms from 2 s before cue onset to 2 s after cue offset; mixed ANOVA with cue and bin within\n    neurons and group between. Reproduced when the group by cue by bin interaction has p < 0.05,\n    both without and with bregma level (the four levels of the data description, a between\n    factor) in the model; partially reproduced when only the first holds.\n- id: fig4c-excited-inflated-onset\n  statement: In the first 1 s of the cue, EAA cue-excited neurons fired more than Control neurons\n    (main effect of group), most clearly to safety; both groups still discriminated danger from\n    uncertainty and uncertainty from safety.\n  source: Results, Inflated cue responses in EAA neurons, paragraph 1; Figure 4C\n  quote: ANOVA for the first 1 s cue interval revealed a main effect of group (F 1,79 = 4.96, p =\n    0.03 ... Compared to Controls, EAA neurons showed excessive firing to safety (Bonferroni-corrected,\n    independent samples t test, t 79 = 3.61, p = 0.001; Fig. 4 C). Yet in the first 1 s of cue\n    presentation, Control and EAA cue-excited neurons each showed cellular discrimination between\n    danger and uncertainty (Bonferroni-corrected, paired samples t test, all t > 2.50, all p <\n    0.025), as well as uncertainty and safety (all t > 3.00, all p < 0.025)\n  statistics:\n  - about: main effect of group\n    test: ANOVA, factors group and cue\n    statistic: F(1, 79) = 4.96\n    p: 0.03\n    n: 32 Con and 49 EAA cue-excited neurons\n  - about: safety, Con against EAA\n    test: independent samples t test\n    statistic: t(79) = 3.61\n    p: 0.001\n    corrected: Bonferroni, three comparisons\n  - about: danger against uncertainty, each group\n    test: paired samples t test\n    statistic: all t > 2.50\n    p: 0.025\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: uncertainty against safety, each group\n    test: paired samples t test\n    statistic: all t > 3.00\n    p: 0.025\n    p_relation: \"<\"\n    corrected: Bonferroni\n  depends_on:\n  - fig2d-cue-responsive-counts\n  criterion: Per neuron, the mean normalized firing over the four 250 ms bins of the first 1 s of\n    each cue. Mixed ANOVA (cue within, group between); independent samples t tests per cue\n    between groups at 0.05/3 (Methods, Population and single-unit firing analyses); paired t tests\n    within each group at p < 0.025 (two pairs). Reproduced when the group effect has p < 0.05 with\n    EAA higher, the safety t test passes the corrected level with EAA higher, and all four paired\n    tests pass with danger > uncertainty > safety; partially reproduced when the group effect\n    holds but one of the other parts fails.\n- id: fig4de-inhibited-temporal-pattern\n  statement: Control and EAA cue-inhibited neurons differed in the temporal pattern of their cue\n    firing (a group by cue by bin interaction that held with bregma level as a factor). Control\n    neurons decreased firing equally to danger and uncertainty with little change to safety,\n    sustained over the cue; EAA neurons decreased most to danger, less to uncertainty, mostly in\n    the first half of the cue.\n  source: Results, Inflated cue responses in EAA neurons, paragraph 2; Figure 4D and 4E\n  quote: EAA cue-inhibited neurons showed enhanced decreases in firing to danger, lesser decreases\n    in firing to uncertainty and little change to safety ... revealed a group × cue × bin\n    interaction (F 110,14190 = 1.69, p = 9.00 × 10 –6 ... The interaction was observed when bregma\n    recording level was included as an ANOVA factor (F 110,13970 = 1.34, p = 0.01\n  statistics:\n  - about: group by cue by bin\n    test: ANOVA, factors group, cue and bin\n    statistic: F(110, 14190) = 1.69\n    p: 9.0e-06\n    n: 48 Con and 84 EAA cue-inhibited neurons\n  - about: group by cue by bin, with bregma level as a factor\n    test: ANOVA\n    statistic: F(110, 13970) = 1.34\n    p: 0.01\n  depends_on:\n  - fig2d-cue-responsive-counts\n  criterion: As fig4ab-excited-temporal-pattern, on cue-inhibited neurons. Reproduced when the\n    interaction has p < 0.05 without and with bregma level; partially reproduced when only the\n    first holds. The descriptive pattern is reported from the population means.\n- id: fig4f-inhibited-danger-decrease\n  statement: In the first 5 s of the cue, EAA cue-inhibited neurons decreased firing more than\n    Control neurons (main effect of group), with a greater decrease to danger; the group\n    difference to uncertainty fell short of the corrected level.\n  source: Results, Inflated cue responses in EAA neurons, paragraph 2; Figure 4F\n  quote: EAA cue-inhibited neurons also showed greater decreases in firing to danger compared to\n    Control neurons (Bonferroni-corrected, independent samples t test, t 130 = 2.70, p = 0.008;\n    Fig. 4 F). The group difference in firing to uncertainty fell short of the Bonferroni-corrected\n    p value (t 130 = 2.38, p = 0.019). Finally, ANOVA for mean firing over the first 5 s of cue\n    presentation revealed a main effect of group (F 1,130 = 10.82, p = 0.001\n  statistics:\n  - about: danger, Con against EAA\n    test: independent samples t test\n    statistic: t(130) = 2.70\n    p: 0.008\n    corrected: Bonferroni, three comparisons\n  - about: uncertainty, Con against EAA\n    test: independent samples t test\n    statistic: t(130) = 2.38\n    p: 0.019\n    corrected: Bonferroni, three comparisons (not significant)\n  - about: main effect of group, first 5 s\n    test: ANOVA, factors group and cue\n    statistic: F(1, 130) = 10.82\n    p: 0.001\n    n: 48 Con and 84 EAA cue-inhibited neurons\n  depends_on:\n  - fig2d-cue-responsive-counts\n  criterion: Per neuron, mean normalized firing over the 20 bins of the first 5 s of each cue.\n    Mixed ANOVA (cue within, group between) and independent samples t tests per cue at 0.05/3.\n    Reproduced when the group effect has p < 0.05 with EAA lower and the danger t test has p <\n    0.0167 with EAA lower. The uncertainty difference is reported; it does not decide the claim.\n- id: fig4f-inhibited-danger-uncertainty-discrimination\n  statement: In the first half of the cue, EAA cue-inhibited neurons discriminated danger from\n    uncertainty, while Control cue-inhibited neurons did not.\n  source: Results, Inflated cue responses in EAA neurons, paragraph 2; Figure 4D to 4F\n  quote: Supporting an interaction, EAA cue-inhibited neurons (Bonferroni-corrected, paired samples\n    t test, t 83 = 3.14, p = 0.002), but not Control cue-inhibited neurons (t 47 = 1.40, p = 0.17),\n    showed cellular discrimination between danger and uncertainty in the first half of cue\n    presentation.\n  statistics:\n  - about: danger against uncertainty, EAA\n    test: paired samples t test\n    statistic: t(83) = 3.14\n    p: 0.002\n    corrected: Bonferroni\n    n: 84 EAA cue-inhibited neurons\n  - about: danger against uncertainty, Control\n    test: paired samples t test\n    statistic: t(47) = 1.40\n    p: 0.17\n    n: 48 Con cue-inhibited neurons\n  depends_on:\n  - fig2d-cue-responsive-counts\n  criterion: Per neuron, mean normalized firing over the first 5 s of danger and of uncertainty;\n    a paired t test in each group. The paper does not give the Bonferroni divisor. Readings are\n    (a) 0.05/2 (two groups) and (b) 0.05/3 (three cue pairs). The Control part is a claim of\n    absence, judged on the same test. Reproduced when the EAA test passes the corrected level with\n    danger lower and the Control test does not; the effect sizes are reported either way.\n- id: fig5abc-excited-reduced-threat-probability\n  statement: Control cue-excited neurons signaled threat probability (positive betas from cue\n    onset, rising over the cue) with fear output betas near zero; EAA cue-excited neurons showed\n    lower threat probability betas and similar fear output betas, a group by regressor\n    interaction.\n  source: Results, Diminished threat probability signaling in EAA cue-excited neurons, paragraph 2;\n    Figure 5A to 5C\n  quote: EAA cue-excited neurons showed diminished threat probability signaling (Fig. 5 B). ...\n    revealed a group × regressor interaction (F 1,65 = 6.80, p = 0.01 ... The mean beta coefficient\n    for the entirety of cue presentation differed for threat probability (independent samples t\n    test, t 66 = 2.71, p = 0.01), but not fear output (t 66 = 0.17, p = 0.86), between Control and\n    EAA cue-excited neurons\n  statistics:\n  - about: group by regressor\n    test: ANOVA, repeated measures on 1 s interval (10), factors group and regressor\n    statistic: F(1, 65) = 6.80\n    p: 0.01\n  - about: threat probability beta, whole cue, Con against EAA\n    test: independent samples t test\n    statistic: t(66) = 2.71\n    p: 0.01\n  - about: fear output beta, whole cue, Con against EAA\n    test: independent samples t test\n    statistic: t(66) = 0.17\n    p: 0.86\n  depends_on:\n  - fig2d-cue-responsive-counts\n  criterion: Regression as in the opening comment, per neuron and 1 s cue interval, under the\n    readings named there (trial-wise firing, empty-poke trials, window beta). Mixed ANOVA of betas\n    with interval and regressor within, group between. Reproduced when the group by regressor\n    interaction has p < 0.05, the whole-cue threat probability beta is higher in Control (t test p\n    < 0.05), and the fear output betas do not differ (t test p >= 0.05, judged on that test), under\n    one reading; partially reproduced when the threat probability difference holds but the\n    interaction does not. Degrees of freedom are reported as obtained (opening comment).\n- id: fig5d-threat-tuning-curve\n  statement: The threat tuning curve of cue-excited neurons peaked at an uncertainty assignment of\n    0.500 in both groups; the EAA curve had the same shape but was lower across all assignments\n    (main effect of assignment and of group, no interaction).\n  source: Results, Diminished threat probability signaling in EAA cue-excited neurons, paragraphs 3\n    and 4; Figure 5D\n  quote: The tuning curve for EAA cue-excited neurons was identical in shape, but was diminished\n    across all assignments. ... revealed a main effect of assignment (F 8,624 = 18.88, p = 1.71 ×\n    10 –25 ... but most critically a main effect of group (F 1,78 = 4.01, p = 0.049 ... and no group\n    × assignment interaction (F 8,624 = 1.25, p = 0.27\n  statistics:\n  - about: main effect of assignment\n    test: ANOVA, repeated measures on assignment (9), factor group\n    statistic: F(8, 624) = 18.88\n    p: 1.71e-25\n  - about: main effect of group\n    test: ANOVA\n    statistic: F(1, 78) = 4.01\n    p: 0.049\n  - about: group by assignment\n    test: ANOVA\n    statistic: F(8, 624) = 1.25\n    p: 0.27\n  expected:\n  - quantity: uncertainty assignment at the peak of the Control curve\n    value: 0.5\n    tolerance: 0\n  - quantity: uncertainty assignment at the peak of the EAA curve\n    value: 0.5\n    tolerance: 0\n  depends_on:\n  - fig5abc-excited-reduced-threat-probability\n  criterion: As the Methods (Threat probability tuning curve) say, nine regressions per neuron\n    with the uncertainty value set to 0 to 1 in steps of 0.125, each 1 s interval, the beta for\n    threat probability averaged over the 10 intervals; the curve is the mean over neurons. The\n    peak is on a grid of nine values, so its tolerance is zero. Reproduced when both peaks are at\n    0.500, the assignment and group effects have p < 0.05 with EAA lower, and the interaction has\n    p >= 0.05 (absence judged on that ANOVA), under one reading of the opening comment; partially\n    reproduced when the group effect holds and a peak falls at 0.375 or 0.625.\n- id: figs4-peak-assignment-same-pattern\n  statement: Using the peak uncertainty assignment (0.500) in place of the actual probability gave\n    the same pattern of threat probability signaling in cue-excited neurons and of fear output\n    signaling in cue-inhibited neurons.\n  source: Results, Diminished threat probability signaling, paragraph 4, and Enhanced fear output\n    signaling, paragraph 1; Supplementary Figure S4 (not in the text supplied)\n  quote: Importantly, using the peak uncertainty assignment for linear regression returned an\n    identical pattern of threat probability signaling as did the actual uncertainty assignment\n  depends_on:\n  - fig5d-threat-tuning-curve\n  - fig5abc-excited-reduced-threat-probability\n  - fig5efg-inhibited-fear-output\n  criterion: The tests of fig5abc-excited-reduced-threat-probability and\n    fig5efg-inhibited-fear-output, rerun with the uncertainty value 0.500. The supplement was not\n    available, so which statistics Fig. S4 shows is not known. Reproduced when the significance\n    and direction of the whole-cue threat probability group difference (cue-excited) and of the\n    last-5 s fear output group difference (cue-inhibited) are as with 0.375.\n- id: fig5efg-inhibited-fear-output\n  statement: Control cue-inhibited neurons signaled a mix of threat probability and fear output\n    (negative betas for both). In EAA cue-inhibited neurons the signals diverged in the second half\n    of the cue, fear output persisting and threat probability diminishing (group by regressor by\n    interval interaction); fear output betas in the last 5 s were more negative in EAA, threat\n    probability betas did not differ.\n  source: Results, Enhanced fear output signaling in EAA cue-inhibited neurons, paragraph 1; Figure\n    5E to 5G\n  quote: Signals diverged thereafter, with fear output persisting and threat probability\n    diminishing (Fig. 5 F). ... revealed a group × regressor × interval interaction (F 9,1170 =\n    2.14, p = 0.02 ... Mean beta coefficient for fear output was more negative in EAA cue-inhibited\n    neurons compared to Control neurons for the last half of cue presentation (independent samples\n    t test, t 130 = 2.31, p = 0.02; Fig. 5 G). Beta coefficients for threat probability in the same\n    period did not differ (t 130 = 0.81, p = 0.42).\n  statistics:\n  - about: group by regressor by interval\n    test: ANOVA, repeated measures on 1 s interval (10), factors group and regressor\n    statistic: F(9, 1170) = 2.14\n    p: 0.02\n    n: 48 Con and 84 EAA cue-inhibited neurons\n  - about: fear output beta, last 5 s, Con against EAA\n    test: independent samples t test\n    statistic: t(130) = 2.31\n    p: 0.02\n  - about: threat probability beta, last 5 s, Con against EAA\n    test: independent samples t test\n    statistic: t(130) = 0.81\n    p: 0.42\n  depends_on:\n  - fig2d-cue-responsive-counts\n  criterion: Regression as in fig5abc-excited-reduced-threat-probability, on cue-inhibited neurons;\n    the last 5 s window beta under the readings of the opening comment. Reproduced when the\n    three-way interaction has p < 0.05, the last-5 s fear output beta is more negative in EAA\n    (t test p < 0.05), and the threat probability betas do not differ (p >= 0.05, judged on that\n    test), under one reading; partially reproduced when the fear output difference holds without\n    the interaction.\n- id: fig6-excited-firing-threat-decoupled\n  statement: In Control cue-excited neurons, danger and uncertainty firing in the first 1 s of the\n    cue predicted the whole-cue threat probability beta; in EAA cue-excited neurons they did not,\n    and the relationships differed between groups. Safety firing was unrelated in both groups.\n  source: Results, Cue firing and threat probability signaling decoupled in EAA cue-excited\n    neurons, paragraph 1; Figure 6A to 6F\n  quote: Danger firing and threat probability signaling were coupled in Control cue-excited neurons\n    ... (R 2 = 0.56, p = 7.54 × 10 –7 ; Fig. 6 A). ... (R 2 = 0.01, p = 0.61; Fig. 6 B).\n    Importantly, the relationship between danger firing and threat probability signaling\n    significantly differed between Control and EAA cue-excited neurons (Fisher r-to-z\n    transformation, Z = 3.80, p = 0.0001). ... Control cue-excited neurons showed a positive\n    relationship (R 2 = 0.22, p = 0.007; Fig. 6 C), EAA cue-excited neurons showed zero relationship\n    (R 2 = 0.05, p = 0.14; Fig. 6 D) and these relationships significantly differed (Fisher r-to-z\n    transformation, Z = 3.05, p = 0.0011). Safety firing and threat probability signaling were not\n    related in either population\n  statistics:\n  - about: danger, Control\n    test: Pearson correlation\n    statistic: R2 = 0.56\n    p: 7.54e-07\n    n: 32 Con cue-excited neurons\n  - about: danger, EAA\n    test: Pearson correlation\n    statistic: R2 = 0.01\n    p: 0.61\n    n: 49 EAA cue-excited neurons\n  - about: danger, Control against EAA\n    test: Fisher r-to-z transformation\n    statistic: Z = 3.80\n    p: 0.0001\n  - about: uncertainty, Control\n    test: Pearson correlation\n    statistic: R2 = 0.22\n    p: 0.007\n  - about: uncertainty, EAA\n    test: Pearson correlation\n    statistic: R2 = 0.05\n    p: 0.14\n  - about: uncertainty, Control against EAA\n    test: Fisher r-to-z transformation\n    statistic: Z = 3.05\n    p: 0.0011\n  expected:\n  - quantity: R2, danger firing against threat probability beta, Control\n    value: 0.56\n    tolerance: 0.056\n  - quantity: R2, uncertainty firing against threat probability beta, Control\n    value: 0.22\n    tolerance: 0.022\n  depends_on:\n  - fig4c-excited-inflated-onset\n  - fig5abc-excited-reduced-threat-probability\n  criterion: Per neuron, first 1 s normalized firing to each cue (as fig4c) against the whole-cue\n    threat probability beta (as fig5abc), Pearson correlation per group and cue; groups compared by\n    Fisher r-to-z. The paper's p values for Z = 3.80 and 3.05 match the one-tailed p of the normal\n    distribution (7e-5 and 0.0011), so the comparison is one-tailed, as the vassarstats page\n    gives it. Reproduced when, under one reading, the Control danger and uncertainty correlations\n    are positive with p < 0.05, the EAA ones have p >= 0.05, both r-to-z comparisons have\n    one-tailed p < 0.05, and the safety correlations have p >= 0.05 in both groups; partially\n    reproduced when the danger part holds and the uncertainty part does not. The Control R2\n    values are given as expected values for comparison; the claim is decided by the tests.\n- id: figs5-excited-firing-fear-output-unrelated\n  statement: In cue-excited neurons, cue firing did not predict fear output signaling for any cue\n    in either group, and the relationships did not differ between groups.\n  source: Results, Cue firing and threat probability signaling decoupled, paragraph 1;\n    Supplementary Figure S5 (not in the text supplied)\n  quote: An identical analysis comparing firing to fear output signaling found no predictive\n    relationships for any cues, and no differences between these relationships for Control and EAA\n    cue-excited neurons\n  depends_on:\n  - fig6-excited-firing-threat-decoupled\n  criterion: A claim of absence. As fig6-excited-firing-threat-decoupled with the whole-cue fear\n    output beta. The supplement was not available, so the paper's statistics are not known; the\n    tests are the Pearson correlation at p < 0.05 and the Fisher r-to-z (one-tailed, as for Fig. 6)\n    at p < 0.05. Reproduced when none of the six correlations and none of the three comparisons is\n    significant; the r values are reported either way.\n- id: fig7-inhibited-firing-fear-output\n  statement: In cue-inhibited neurons, last-5 s danger firing did not predict the last-5 s fear\n    output beta in either group; uncertainty firing predicted it positively in EAA but not in\n    Control neurons, and safety firing predicted it negatively in both groups; none of these\n    relationships differed between groups.\n  source: Results, Cue firing and fear output signaling coupled in EAA cue-inhibited neurons,\n    paragraph 1; Figure 7A to 7F\n  quote: Degree of danger firing failed to predict fear output signaling in either population\n    (Control ... R 2 = 0.004, p = 0.67; EAA ... R 2 = 0.02, p = 0.24; Fig. 7 A, B) and these\n    relationships did not differ (Fisher r-to-z transformation, Z = 1.04, p = 0.15). EAA\n    cue-inhibited neurons, but not Control, showed a positive predictive relationship between\n    uncertainty firing and fear output (Control ... R 2 = 0.04, p = 0.16; EAA ... R 2 = 0. 20, p =\n    2.59 × 10 –5 ... but these relationships did not differ between groups (Fisher r-to-z\n    transformation, Z = 1.43, p = 0.08). Equivalent negative predictive relationships between\n    safety firing and fear output signaling were also found in both groups (Fisher r-to-z\n    transformation, Z = 0.60, p = 0.54).\n  statistics:\n  - about: danger, Control\n    test: Pearson correlation\n    statistic: R2 = 0.004\n    p: 0.67\n    n: 48 Con cue-inhibited neurons\n  - about: danger, EAA\n    test: Pearson correlation\n    statistic: R2 = 0.02\n    p: 0.24\n    n: 84 EAA cue-inhibited neurons\n  - about: danger, Control against EAA\n    test: Fisher r-to-z transformation\n    statistic: Z = 1.04\n    p: 0.15\n  - about: uncertainty, Control\n    test: Pearson correlation\n    statistic: R2 = 0.04\n    p: 0.16\n  - about: uncertainty, EAA\n    test: Pearson correlation\n    statistic: R2 = 0.20\n    p: 2.59e-05\n  - about: uncertainty, Control against EAA\n    test: Fisher r-to-z transformation\n    statistic: Z = 1.43\n    p: 0.08\n  - about: safety, Control\n    test: Pearson correlation\n    statistic: R2 = 0.14\n    p: 0.009\n  - about: safety, EAA\n    test: Pearson correlation\n    statistic: R2 = 0.22\n    p: 8.86e-06\n  - about: safety, Control against EAA\n    test: Fisher r-to-z transformation\n    statistic: Z = 0.60\n    p: 0.54\n  depends_on:\n  - fig5efg-inhibited-fear-output\n  criterion: Per neuron, last-5 s normalized firing to each cue (mean of the last 20 bins of the\n    cue) against the last-5 s fear output beta (as fig5efg), Pearson correlation per group and cue,\n    groups compared by Fisher r-to-z. The paper's r-to-z p values are one-tailed for Z = 1.04 and\n    1.43 (0.149 and 0.076) and two-tailed for Z = 0.60 (0.549); its own threshold is p < 0.05. The\n    absence parts (danger in both groups, uncertainty in Control, the three group comparisons) are\n    judged on these tests, one-tailed and two-tailed both shown. Reproduced when the danger\n    correlations have p >= 0.05, the EAA uncertainty correlation is positive with p < 0.05 and the\n    Control one has p >= 0.05, both safety correlations are negative with p < 0.05, and no\n    comparison has p < 0.05; partially reproduced when the safety and uncertainty parts hold but\n    one other part fails.\n- id: figs6-inhibited-firing-threat-probability\n  statement: In cue-inhibited neurons, cue firing also predicted threat probability signaling in\n    both groups, with no difference between Control and EAA for any relationship.\n  source: Results, Cue firing and fear output signaling coupled in EAA cue-inhibited neurons,\n    paragraph 1; Supplementary Figure S6 (not in the text supplied)\n  quote: Cue firing was also predictive of threat probability signaling in both groups (see\n    Supplementary Fig. S6 online), but there were no differences between Control and EAA\n    cue-inhibited neurons for any predictive relationship.\n  depends_on:\n  - fig7-inhibited-firing-fear-output\n  criterion: As fig7-inhibited-firing-fear-output with the last-5 s threat probability beta. The\n    supplement was not available, so which cues show the relationship is not known. Reproduced\n    when at least one cue's correlation has p < 0.05 in each group and no Fisher r-to-z comparison\n    has p < 0.05 (absence judged on that test, one-tailed and two-tailed both shown).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-pag-2/10.1038-s41598-020-74457-3.yaml paper/10.1038-s41598-020-74457-3.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-pag-2/10.1038-s41598-020-74457-3.yaml; grep -n "—\|rather" $f; grep -vn "^\s*#" $f | grep -E "[^\"]: [^ ]" | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: " | head
```

```
(Bash completed with no output)
```

**Agent**

I wrote the claims file at `claims/crcns-pag-2/10.1038-s41598-020-74457-3.yaml` and nothing is committed. `tools/claims_check.py` passes every quote. It flags 3 p-values only because the text prints them as "3.00 × 10 –6" and "9.00 × 10 –6", a form it doesn't parse; I confirmed those against the text by reading.

**Text read:** the version of record, PMC7582948 (Europe PMC JATS XML, flattened). It has the full main text, Methods, all figure legends and the Discussion.
- **Supplement:** Figs. S1 to S6 and a Supplementary Information file are listed but their content isn't in the text, and no PDF was supplied. The main results and their statistics are stated in the main text, so I went ahead. The three claims that only Figs. S4 to S6 show are written from the Results sentences that cite them, with no expected values.
- **Code:** none was read. The only link is https://mcdannaldlab.org/resources (behavioral programs only), and it returned a 404 on 2026-11-06, so no repository or commit is recorded.

**Counts:** 20 claims, all 20 with quotes and none inferred. 17 have statistics (49 statistical values), 4 have expected values, and all 20 have criteria. Some claims need data the dataset's description doesn't list (body weights, the eight pre-surgery sessions); they're kept as the paper's findings.

**Settled from the paper's own numbers:**
- **Fig. 2D chi-square:** χ² = 5.68 comes out only without the Yates correction.
- **Fisher r-to-z p-values:** they are one-tailed for Z = 3.80, 3.05, 1.04 and 1.43, and two-tailed for Z = 0.60. The criteria show both where it matters.

**Details left open, with the readings named:**
- **Selection epochs:** the Methods give first 1 s and last 5 s for both cell types; the Results give first 5 s and last 5 s for inhibited cells. A third reading uses all three epochs.
- **Trial-wise normalized firing for the regression:** (a) subtract the trial type's 2 s baseline and use the neuron's normalization mean and SD; (b) subtract the trial's own 2 s baseline instead; (c) Z score each trial's binned firing over all its trials and bins.
- **Suppression ratio of 0/0** (no pokes in baseline and cue): set to 0, or drop the trial.
- **Beta for a multi-second window:** the mean of the 1 s interval betas, or one regression on the window's averaged firing.
- **Baseline window:**
  - Fig. 2B nose poke rate: the 20 s before the cue, or the dataset's own baseline poke field.
  - Fig. 2E,F firing rate: 10 s or 2 s before the cue.
- **Fig. 2C rat means:** the mean of session means, or all trials pooled.
- **Bonferroni divisor for Fig. 4F's within-group test:** 2 or 3.
- **Degrees of freedom:** several tests report fewer than the neuron counts imply (t 66 and F 1,65 for 81 cells; F 1,78; F 110,8360; F 2,346 for 354 cells). The paper doesn't say which neurons were dropped, so a mismatch counts as a deviation, not a failure of the claim.
- **ANOVA software and sphericity correction:** not named. The criteria assume uncorrected repeated-measures ANOVA.

**Missing from the paper that claims needed:**
- The supplement's content, so the statistics behind the S4 to S6 claims are unknown.
- The lab's analysis code, which is unreachable, and no neural analysis code is linked at all.

## End of run

17 turns, 4 minutes, $1.39 at API prices, result: success.
