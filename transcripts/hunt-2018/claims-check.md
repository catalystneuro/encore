# hunt-2018 · claims-check · run 42929374192

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i hunt; cat claims/hunt-2018.yaml; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; wc -l claims/hunt-2018.yaml paper/*; python tools/claims_check.py claims/hunt-2018.yaml paper/$(ls paper | grep -v pfc | grep txt | head -1) 2>&1 | tail -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/hunt-2018.yaml"
}
```

```
1	# Claims for Hunt, Malalasekera, de Berker, Miranda, Farmer, Behrens & Kennerley (2018), Nature
2	# Neuroscience 21, 1471-1481, "Triple dissociation of attention and decision computations across
3	# prefrontal cortex", doi:10.1038/s41593-018-0239-5, on CRCNS data set pfc-7 (doi:10.6080/K0PZ5712).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record (PMC6331040, open access, JATS XML flattened to text, under
8	# paper/), main text, Discussion and Online Methods, and the supplement
9	# (41593_2018_239_MOESM1_ESM.pdf, extracted to text in the same file; legends of Supplementary
10	# Figures 1 to 12, Supplementary Table 1 and the Supplementary Note). The flattened main text has
11	# no main figure legends, and no PDF of the main article was supplied, so the legends of Figures 1
12	# to 8 (their sample sizes, tests and significance marks) were not read. Every claim on a main
13	# figure rests on the Results and Methods sentences that cite it. The extraction drops the minus
14	# sign in some exponents ("p<1*10 7" stands for p < 1e-7); quotes keep the extracted characters.
15	# The CRCNS data descriptor (paper/pfc-7.data-description.txt) was read only to know what the
16	# data set holds; no claim or method comes from it.
17	#
18	# Code. The Code Availability statement says the custom MATLAB analysis scripts are deposited with
19	# the raw data on CRCNS (dataset pfc-7). By the data descriptor they are among the data set's own
20	# files (Fig1_2_S1_behaviour, Fig4_RSA, Fig5_OFC_crosscorrelation, Fig6_ACC_multiplesignals,
[... 830 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-018-0239-5.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-018-0239-5.txt",
 "offset": 240,
 "limit": 432
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
L=open('paper/10.1038-s41593-018-0239-5.txt').read().splitlines()
def s(a,b):
  v=[int(x) for x in L[a-1:b] if x.strip()]
  r=[v[i:i+4] for i in range(0,len(v),4)]
  print(len(r),[sum(x[k] for x in r) for k in (1,2,3)])
  return r
m=s(387,502); f=s(509,604)
print([m[i][k]+f[i][k] for i in range(0) for k in range(0)])
print([sum(x[k] for x in m)+sum(x[k] for x in f) for k in (1,2,3)])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "toleran\|threshold\|open\b\|readings\|partially" docs/protocol.md | head -60
```

```
25:comes from the paper. Where the paper leaves a method open, the choice made is
48:`paper/`: the main text, the Methods, and the supplement. Read the text; open
63:open and the code settles it, follow the code and say so. Where they disagree,
100:     numbers the attempt must match, with tolerances, stay in `expected`.
101:     Record only tests whose result is the finding. A significance threshold
106:   - `expected`: each reported number the claim rests on, with a tolerance.
110:     widened by 10% of each bound. Give the reason for any other tolerance.
116:     readings the paper's text plausibly allows, before the analysis. The
122:     bins, thresholds, what a measure is compared with) is taken from the
125:     treating a detail as open.
130:     is chosen), the criterion names the readings the paper's text allows,
138:     criterion names the test and threshold the paper used. The claim is
141:     several readings does not apply: absence is judged on the paper's test
179:the paper's and are results, not thresholds; that every part of every
219:1. List the dataset's files and read its metadata from the archive. Open a
308:   a window, a threshold, what a measure is compared with), take it from the
316:     change the outcome, run every reading, as for the readings a criterion
318:   - When the readings give different outcomes, or the paper does not settle
331:     notes (what is open, the passages that bear on it, how the readings
414:   - When a threshold or criterion is a choice, show how the result changes
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 40,200p docs/protocol.md
```

```
on DANDI and `<archive>-<id>` otherwise ([archives.md](archives.md)). The
pipeline is described in [pipeline.md](pipeline.md).

## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold. A
data descriptor under `paper/` (`<id>.data-description.txt`, the dataset's own
documentation) is a longer description, to be read for that alone; it is not
the paper, and no claim comes from it.

### 2. Read the paper's code
[... 140 more lines not kept]
```

**Agent**

The checker reports 2 problems, both p < 1e-7 values that the text extraction garbled. Supplementary Table 1 sums as the file says. Next I'm correcting the paragraph numbers and several criteria.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='claims/hunt-2018.yaml'
s=open(p).read()
reps=[
("first saccade, paragraphs 3 and 4;\n    Figure 4a-d","first saccade, paragraphs 4 and 5;\n    Figure 4a-d"),
("first saccade, paragraph 3; Figure 4e","first saccade, paragraph 4; Figure 4e"),
("first saccade, paragraphs 3 and 6;\n    Figure 4a and 4f","first saccade, paragraphs 4 and 7;\n    Figure 4a and 4f"),
("first saccade, paragraph 3; Figure 4g","first saccade, paragraph 4; Figure 4g"),
("first saccade, paragraphs 3 and 7;\n    Figure 4c and 4h","first saccade, paragraphs 4 and 8;\n    Figure 4c and 4h"),
("first saccade, paragraph 3;\n    Supplementary Figure 2","first saccade, paragraph 4;\n    Supplementary Figure 2"),
("first saccade, paragraph 5;\n    Supplementary Figure 5B","first saccade, paragraph 6;\n    Supplementary Figure 5B"),
("Triply dissociable PFC population codes at first\n    saccade, paragraph 5\n","Triply dissociable PFC population codes at first\n    saccade, paragraph 6\n"),
]
for a,b in reps:
    assert s.count(a)==1,a
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "first saccade\|first$" claims/hunt-2018.yaml
```

```
133:  source: Results, Triply dissociable PFC population codes at first saccade, paragraph 1; Online
281:  source: Results, Triply dissociable PFC population codes at first saccade, paragraphs 4 and 5;
292:  source: Results, Triply dissociable PFC population codes at first saccade, paragraph 4; Figure 4e
300:  source: Results, Triply dissociable PFC population codes at first saccade, paragraphs 4 and 7;
310:  source: Results, Triply dissociable PFC population codes at first saccade, paragraph 4; Figure 4g
318:  source: Results, Triply dissociable PFC population codes at first saccade, paragraphs 4 and 8;
329:  source: Results, Triply dissociable PFC population codes at first saccade, paragraph 4;
359:  source: Results, Triply dissociable PFC population codes at first saccade, paragraph 6;
417:  source: Supplementary Figure 5C legend; Results, Triply dissociable PFC population codes at first
```

**Agent**

Now the criterion edits.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='claims/hunt-2018.yaml'
s=open(p).read()
reps=[
# figs1ab statement
("""    magnitude about equally and used all four viewed cues, and both showed a small bias towards
    choosing the second side on option trials.""",
"""    magnitude about equally and used all four viewed cues, with a slight upweighting of the
    antepenultimate (n-2) cue, and both showed a small bias towards choosing the second side on
    option trials."""),
("""    and the first-side bias on option trials is negative (towards the second side) with p < 0.05.""",
"""    and the first-side bias on option trials is negative (towards the second side) with p < 0.05.
    The legend gives no test for the upweighting of the n-2 cue; it is reported (the n-2 weight
    against the final and n-1 weights), not judged."""),
# fig4d
("""    region; open details O8 and O9. Reproduced when the spatial attention template is significant
    (permutation p < 0.05) in DLPFC, its CPD is larger in DLPFC than in ACC and OFC, and it is
    positive in OFC and ACC.""",
"""    region; open details O8 and O9. Reproduced when the spatial attention template is significant
    (permutation p < 0.05) in DLPFC, its CPD is larger in DLPFC than in ACC and OFC, and it is
    significant (permutation p < 0.05) in OFC and in ACC."""),
# fig4h
("""    which enters the model with the attended value template. Reproduced when it is significant
    (permutation p < 0.05) in ACC and its CPD in ACC exceeds that of the attended value template in
    ACC and that of the accept/reject template in DLPFC.""",
"""    which enters the model with the attended value template. "Best explained" by the categorical
    template is open, since the Supplementary Figure 5 legend warns that CPDs of different
    variables are not directly comparable. Readings (a) the accept/reject CPD in ACC exceeds the
    attended value CPD in ACC; (b) the accept/reject template is significant in ACC and the
    attended value template is not. Reproduced when the accept/reject template is significant
    (permutation p < 0.05) in ACC, its CPD in ACC exceeds that of the accept/reject template in
    DLPFC, and (a) or (b) holds."""),
# figs4
("""    but different rows (top left with bottom left), excluding the diagonal. Reproduced when this
    difference is positive in DLPFC and larger there than in ACC and OFC.""",
"""    but different rows (top left with bottom left), excluding the diagonal. Reproduced when this
    difference is positive in DLPFC and larger there than in ACC and OFC. The legend's "primarily
    replicate" is not judged, as the paper defines no templates for 40 conditions; the 40 x 40
    matrices are shown."""),
# fig4 t75 range
("""    time range are not stated. Readings of the step (a) 10 ms, as the GLM; (b) 1 ms. Range -100 to
    500 ms after cue 1, as the GLM's stimulus-locked range.""",
"""    time range are not stated. Readings of the step (a) 10 ms, as the GLM; (b) 1 ms. The range is
    open too; reading taken, -100 to 500 ms after cue 1, the GLM's stimulus-locked range, and the
    t75 values under -200 to 600 ms are reported."""),
# fig5a baseline
("""    cue 3, EVs 3, 7 and 9); (b) each trial type separately. Baseline is the cue 1 value CPD at -100
    ms from cue 1 (the first bin). Reproduced when, under one reading, the peak of each cue's value
    CPD after its own onset is within tolerance of 300 ms and the cue 1 and cue 2 value CPDs stay
    above their baseline at every time in the later cue epochs.""",
"""    cue 3, EVs 3, 7 and 9); (b) each trial type separately. The paper does not define the
    baseline. Readings (i) the cue 1 value CPD at -100 ms from cue 1 (the first bin); (ii) the mean
    CPD of the same EVs over -100 to 0 ms before cue 1. Reproduced when, under one reading, the peak
    of each cue's value CPD after its own onset is within tolerance of 300 ms and the cue 1 and cue
    2 value CPDs stay above the baseline at every time in the later cue epochs; "sustained above
    baseline" has no stated test, so the mean CPD over each later cue epoch above baseline is
    reported too."""),
# figs67 presence
("""    fit +/- 95% CI); Pearson's test at p < 0.05 two-sided is taken. Presence holds when the fig5b
    correlation is positive at p < 0.05 in each region.""",
"""    fit +/- 95% CI); Pearson's test at p < 0.05 two-sided is taken. Presence holds when the fig5b
    correlation (attended, panel B) and the fig5f correlation (stored, panel F; EV 1 with EV 2 at
    cue 3) are positive at p < 0.05 in each region (Supplementary Figures 6 and 7 legends)."""),
("""  depends_on:
  - fig5b-stable-attended-value-subspace
  criterion: The analyses of fig5b, fig5c and fig5de, run on ACC and on DLPFC.""",
"""  depends_on:
  - fig5b-stable-attended-value-subspace
  criterion: The analyses of fig5b, fig5c, fig5de and fig5f, run on ACC and on DLPFC."""),
# fig6a
("""    in fig5b) (Methods, Projection of ACC activity, paragraph 1); Pearson correlations across neurons
    for the 10 pairs, in each region, at p < 0.05. Reproduced when all 10 ACC correlations are
    positive with p < 0.05 and fewer than half of the 10 are positive with p < 0.05 in OFC and in
    DLPFC;""",
"""    in fig5b) (Methods, Projection of ACC activity, paragraph 1); Pearson correlations across neurons
    for the 10 pairs (Supplementary Figure 10 legend), in each region, at p < 0.05. What is
    correlated is open: the Methods for Figure 6A and the Supplementary Figure 10 legend say
    "parameter estimates", the Methods for Figure 5 correlate T-statistics. Readings (a)
    T-statistics; (b) the OLS coefficients. The paper gives no test for the absence in OFC and
    DLPFC in the text read (the Figure 6a legend is missing); the rule below for it, fewer than
    half of the 10 positive with p < 0.05, is this file's choice and not the paper's, and the 10 r
    values of each region are reported. Reproduced when all 10 ACC correlations are positive with p
    < 0.05 and fewer than half of the 10 are positive with p < 0.05 in OFC and in DLPFC;"""),
# fig6c
("""    evidence, faster responses), the shortest-RT bin above the longest. Reproduced when, under one
    reading, the mean projection in the window is higher for the shortest than for the longest RT
    bin and, with O4 reading (b), in at least 95 of the 100 splits; partially reproduced when the
    separation appears only after cue 2.""",
"""    evidence, faster responses), the shortest-RT bin above the longest. Reproduced when, under one
    reading, the mean projection in the window, averaged over splits as the paper does, is higher
    for the shortest than for the longest RT bin; with O4 reading (b) the number of the 100 splits
    in which it holds is reported. Partially reproduced when the separation appears only after cue
    2."""),
]
for a,b in reps:
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
# fig5gj statistics removal
a="""  statistics:
  - test: cluster-based permutation test, cluster-forming threshold |r| > 0.2, 1000 permutations
    p: 0.001
    p_relation: <
    corrected: cluster-level, for multiple comparisons
  depends_on:
  - fig5c-attribute-cue2-vs-cue1"""
assert s.count(a)==1
s=s.replace(a,"""  depends_on:
  - fig5c-attribute-cue2-vs-cue1""")
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  grep -l "^checks:" claims/*.yaml | head -2 | xargs -I{} sh -c 'sed -n "/^checks:/,\$p" {} | head -20'
```

```
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois. Removed the statistics entries (t-test against finite chance, BH FDR at 0.01); the threshold marks which features count as above chance (Figure 2 legend), a method and not a result. The criteria keep it through M6.
  - fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral. Removed the statistics entries (t-test of the mean difference against zero, BH FDR at 0.01); the threshold selects the consistent features whose signs are counted (Figure 5 legend), a method and not a result. The criteria keep it through M8.
  - table1-participants. Removed the rule that 13 of the 15 minute values suffice; the paper gives no such threshold, so every value must now be within tolerance.
  - fig6-sign-consistency. The tolerance of 0.9 allowed only 9 while the criterion accepted 8 to 10. Set the tolerance to 1 (10% of 9 rounded to a whole combination) and gave the reason.
  - Header O4. The SD of the channel was fixed as the whole recording, called a standard choice; it can change which blocks are dropped, so the readings (whole recording, the day's recording) are now named.
  - Header O10, anova-roi-band-effects, anova-no-interaction. The ANOVA's observations are not given (Methods 2.2); named fold accuracies and participant means as readings. The absence claim is judged on fold accuracies with type II sums of squares, marked as resting on an assumption, with the others as variants. Said that p < 0.001 for a printed 0 is this file's reading.
  - fig5-pre-postcentral. The criterion cited Discussion paragraph 2 for the alpha sign; that paragraph gives theta and gamma only. The alpha sign is cited to Results 3.1 paragraph 6.
  - fig7-exceeds-group. The comparison of Figure 7 with Figure 2 was fixed one way; the paper does not say which values are compared. Added a 
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> claims/hunt-2018.yaml <<'EOF'
checks:
- date: 2026-11-11
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig4d-spatial-attention, fig4e-ofc-stimulus-identity, fig4f-ofc-attended-value, fig4g-left-right-value, fig4h-acc-accept-reject, figs2-consistent-across-subjects, fig4-t75-latencies, figs5c-latency-order. Paragraph numbers in the sources were one short; the section "Triply dissociable PFC population codes" opens with "We recorded single unit activity" (paragraph 1), so "RSA revealed" is paragraph 4, "For intuition" 5, "Decision-related computations" 6, "Value encoding also differed" 7 and "By contrast, ACC value coding" 8.
  - figs1ab-cue-weights. The statement left out the legend's "slight upweighting of the antepenultimate cue"; added, and the criterion reports it since the legend gives no test.
  - fig4d-spatial-attention. "Spatial attention is represented in both OFC and ACC" was judged by a positive coefficient; the paper tests a template in a region by its permutation test (Methods, Statistical inference on RSA template-based regression model), so significance at p < 0.05 is now required in OFC and ACC.
  - fig4h-acc-accept-reject. The criterion compared the CPD of the accept/reject template with that of the attended value template in ACC, which the Supplementary Figure 5 legend warns against (CPDs of different variables are not directly comparable). "Best explained" is now named as open, with that comparison and a significance reading as the two readings.
  - figs4-dlpfc-top-bottom. The statement says the RSA results replicate, which the criterion did not test; it now says this part is not judged, as no 40-condition templates are defined.
  - fig4-t75-latencies. The time range -100 to 500 ms was presented as fixed; the paper does not state it, so it is now named as a reading and a wider range is reported.
  - fig5a-ofc-value-cpd. The baseline was fixed as the first bin, which the paper does not define; now open with two readings, and "sustained above baseline" is said to have no stated test.
  - fig5gj-cross-correlation-dynamics. Removed the statistics entry (cluster test, p < 0.001); it is the significance level set in the Methods, and the text read reports no cluster result. The criterion keeps it.
  - figs67-no-comparison-acc-dlpfc. The Supplementary Figures 6 and 7 legends say the stored subspaces (panel F) are present in ACC and DLPFC; the presence condition now includes the fig5f correlation, and fig5f is among the analyses run.
  - fig6a-acc-belief-subspace. The Methods for Figure 6A and the Supplementary Figure 10 legend correlate "parameter estimates", while Figure 5 uses T-statistics; named as open with both readings. Said that the fewer-than-half rule for absence in OFC and DLPFC is this file's choice and not the paper's.
  - fig6c-belief-subspace-rt. Removed the requirement that the separation hold in 95 of 100 splits; the paper averages over splits and gives no such threshold. The count is reported.
  - Open. The main figure legends (Figures 1 to 8) are not in the text supplied and no PDF of the main article is under paper/; the tests, sample sizes and significance marks of the main figures, and hence the tests for fig2a, fig2b, fig5b-f single correlations, fig7 region comparisons and the absence in fig6a, could not be read.
  - Open. The analysis scripts are among the CRCNS pfc-7 files and were not read; they may settle O1 to O9 and the cue 1 regression of Figure 8.
  - Open. The quote checker cannot match p < 1e-7 in fig8-cue1-value-all-regions and fig8-attribute-value-ofc; the extraction prints "p<1*10 7" with the minus sign lost. Confirmed by reading.
  - Open. Several criteria use this file's operational rules where the paper gives none ("virtually all" as 18 of 20 in fig6b, the ramp windows in fig6d and fig6e, the 0.167 bound in figs9); each says so or names them as readings.
  - Checked, unchanged. Supplementary Table 1 sums to 198 ACC, 195 OFC, 156 DLPFC over 29 sessions of M and 24 of F, as neuron-counts says; all percentages, t75 values, r2 values and p-values against the text.
EOF
python tools/claims_check.py claims/hunt-2018.yaml paper/10.1038-s41593-018-0239-5.txt 2>&1 | tail -5; grep -n "—\|rather" claims/hunt-2018.yaml | grep -v quote
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/    correlated is open: the Methods for Figure 6A/    correlated is open; the Methods for Figure 6A/' claims/hunt-2018.yaml; python tools/claims_check.py claims/hunt-2018.yaml paper/10.1038-s41593-018-0239-5.txt 2>&1 | tail -5; grep -n "—\|rather" claims/hunt-2018.yaml; grep -nE "^  - [^']*: " claims/hunt-2018.yaml | tail
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git status --short
```

```
M claims/hunt-2018.yaml
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

The file is ready for an attempt. I corrected 13 claims, mostly method details the earlier writer had fixed without support from the paper; three things remain open. Only `claims/hunt-2018.yaml` was changed, and nothing is committed.

**Checker:** `claims/hunt-2018.yaml: 40 claims, 40 quotes, 15 statistical values, 2 problems`. Both problems are the p < 1e-7 values in `fig8-cue1-value-all-regions` and `fig8-attribute-value-ofc`. The text extraction prints them as "p<1*10 7", dropping the minus sign; I confirmed both by reading.

**Changes, by claim**
- **Eight claims from the cue 1 population section of the Results** (`fig4d`, `fig4e`, `fig4f`, `fig4g`, `fig4h`, `figs2`, `fig4-t75-latencies`, `figs5c`): every paragraph number in the sources was one too low. Corrected.
- **`figs1ab-cue-weights`:** the statement left out the legend's "slight upweighting of the antepenultimate cue". Added; the legend gives no test for it, so it is reported, not judged.
- **`fig4d-spatial-attention`:** "represented in OFC and ACC" now needs the paper's permutation test at p < 0.05, not just a positive coefficient.
- **`fig4h-acc-accept-reject`:** the criterion compared CPDs of two different templates, which the Supplementary Figure 5 legend warns against. "Best explained" is now open, with two readings.
- **`figs4-dlpfc-top-bottom`:** says the "replicate" part is not judged, because the paper defines no templates for 40 conditions.
- **`fig4-t75-latencies`:** the time range is not in the paper, so it is now named as a reading.
- **`fig5a-ofc-value-cpd`:** the baseline was made up. It is now open, with two readings.
- **`fig5gj-cross-correlation-dynamics`:** removed the p < 0.001 entry from the statistics. It is the significance level set in the Methods, not a reported result.
- **`figs67-no-comparison-acc-dlpfc`:** the legends say the stored subspaces (panel F) are present in ACC and DLPFC, so the presence test now includes that correlation.
- **`fig6a-acc-belief-subspace`:** whether T-statistics or parameter estimates are correlated is now open, since the Figure 6A Methods and the Supplementary Figure 10 legend say parameter estimates. The file now says its rule for absence in OFC and DLPFC is its own choice, not the paper's.
- **`fig6c-belief-subspace-rt`:** removed the made-up rule that the effect must hold in 95 of 100 splits. The count is reported instead.

I checked Supplementary Table 1: its columns sum to 198, 195 and 156 units over 29 and 24 sessions, as the file says.

**Open**
- **Main figure legends:** the legends of Figures 1 to 8 are missing from the text, and there is no PDF of the main article. The tests behind several claims therefore could not be read: the Figure 2 behaviour, the single correlations in Figure 5, the region comparisons in Figure 7, and the absence in Figure 6a.
- **Analysis code:** the paper's scripts are among the CRCNS pfc-7 files and were not read. They might settle the open details O1 to O9 and the regressors of the Figure 8 model.
- **Unsupported rules:** some rules have no basis in the paper ("virtually all" read as 18 of 20, the ramp windows in Figure 6d and 6e, the bound in `figs9`). Each criterion now says so or names them as readings.

**Ready:** true.

## End of run

15 turns, 3 minutes, $1.26 at API prices, result: success.
