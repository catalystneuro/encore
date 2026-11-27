# sabatini-2024 · claims-check · run 44719584747

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/; cat claims/sabatini-2024.yaml; sed -n '/Reader/,/^## /p' docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -l claims/sabatini-2024.yaml paper/*.txt; python tools/claims_check.py claims/sabatini-2024.yaml paper/10.1038-s41467-024-51308-7.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/sabatini-2024.yaml"
}
```

```
1	# Claims for Sabatini & Kaufman (2024), Nat. Commun. 15:7007, "Reach-dependent reorientation of
2	# rotational dynamics in motor cortex", tested on dandiset 000070 (relation reuses).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-20,
4	# protocol pilot-18 as stated in docs/protocol.md. The writer did not look at the dandiset's data
5	# or files.
6	#
7	# Text read: the version of record (open access, CC BY-NC-ND), full text from PubMed Central
8	# (PMC11325044) with Methods, figure legends and Data and Code availability, and its one
9	# supplement, 41467_2024_51308_MOESM1_ESM.pdf (Supplementary Figures 1 to 8 with legends and the
10	# derivation of the basis function representation of a linear dynamical system). The Peer Review
11	# File and Reporting Summary were not read; no result rests on them. The supplement PDF was not
12	# opened beyond its extracted text.
13	#
14	# Code read: github.com/kaufmanlab/LDR-public at commit b65f28d (2024-08-02), the MATLAB code the
15	# Code availability statement links. It holds the analysis functions (TBF, single-condition LDS,
16	# alignment index, subspace excursion angles, rotation and location prediction, LDR encoding and
17	# decoding, jPCA reconciliation). It loads preprocessed .mat files that are not in the repository
18	# (ShenoyMonkeyData, ShenoyMonkeyDataSingleTrial, basisFxnNum, TBFResults and others; the paper
19	# says "Code-compatible data are available upon request"), and lacks kinFuncEval (the kinematic
20	# basis functions), the jPCA codepack, GPFA, and code for the location-from-kinematics regression
[... 725 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Reader" -A60 docs/protocol.md | head -150
```

```
15:  it against the paper. Readers never see the dataset's data.
16-- The **author** tests the claims on the dataset. It reads the paper to
17-  understand the claims, but the claims file binds it: it cannot change a
18-  claim's statement, expected values or criterion. A method detail the file
19-  lacks it takes from the paper, citing the passage, and it asks a reader
20-  only when it believes the file misreads the paper.
21-- The **verifier** checks the author's work and must not be the author.
22-
23-So every claim, the values it must match and how it is judged are fixed from
24-the paper before anyone analyses the data, and every method the analysis uses
25-comes from the paper. Where the paper leaves a method open, the choice made is
26-stated as an assumption, and the outcome is marked as resting on it.
27-
28:Reader runs are made with the [Paper run](../.github/workflows/papers.yml)
29-workflow (roles `claims`, `claims-check` and `answer`), the only runs that
30-write the claims file. The other runs are made with the
31-[Agent run](../.github/workflows/attempt.yml) workflow, one role at a time:
32-`author`, `author-answers` when a reader answered a question on the claims
33-file, `verifier-1`, `author-revise-1`, `verifier-2`, `author-revise-2`, and,
34-when the last of these proposes changes of outcome, `verifier-3` and `author-revise-3`. Each run's
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 104,220p docs/protocol.md
```

```
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
     Methods, the figure legends, the supplement, or the code the paper
[... 97 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-024-51308-7.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '56,763p' paper/10.1038-s41467-024-51308-7.txt | grep -v -E '^\s*\\(usepackage|setlength|documentclass)' | sed -E 's/\\documentclass\[12pt\]\{minimal\}//g' | sed -E 's/\\begin\{document\}.*\\end\{document\}/[EQ]/g'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=/home/runner/.claude/projects/-home-runner-work-encore-encore/d8d0e02a-13db-436c-bbe3-d86d934932fd/tool-results/bo4ze78of.txt; wc -c $f; fold -s -w 4000 $f | head -c 36000
```

```
<persisted-output>
Output too large (35.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d8d0e02a-13db-436c-bbe3-d86d934932fd/tool-results/buvr7i0zp.txt

Preview (first 2KB):
70545 /home/runner/.claude/projects/-home-runner-work-encore-encore/d8d0e02a-13db-436c-bbe3-d86d934932fd/tool-results/bo4ze78of.txt
				[EQ] B ’ ( c ) = L ( c ) † X ( c ) where B’ ( c ) is the recovered temporal basis functions for condition c and † indicates pseudo-inversion. We quantified the “recoverability” of temporal basis functions on condition c as the variance explained in the temporal basis functions by the projected neural activity. If this metric is 1, it suggests that the condition’s loading matrix is invertible, and therefore fulfills the requirements of rotations. More specifically, we expect recoverability to fail when two (or more) temporal basis functions are assigned the same dimension in state space by the loading matrix. As each temporal basis functions dynamically supports each other, this overlap would preclude neural activity from acting as a dynamical system. Control for data smoothing One potential concern is that the factorization described above works well on neural data simply because the data are smoothed before analysis, and smoothing limits the frequency spectrum and therefore allows neural activity to be reconstructed by a small number of temporal basis functions. To test these possibilities, for each trial of each condition independently we shuffled time bins before smoothing and averaging, to disrupt the temporal structure of motor cortex activity while preserving inter-neuron spike correlations and total spike counts. We then extracted temporal basis functions, with the number of temporal basis functions matched to the original dataset, and quantified the population variance explained and recoverability (defined above) of the temporal basis functions. We compared this null distribution to the data distribution using a 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=/home/runner/.claude/projects/-home-runner-work-encore-encore/d8d0e02a-13db-436c-bbe3-d86d934932fd/tool-results/bo4ze78of.txt; fold -s -w 200 $f | grep -v '^\s*$' > $TMPDIR/methods.txt; wc -l $TMPDIR/methods.txt; echo $TMPDIR
```

```
740 /tmp/claude-1001/methods.txt
/tmp/claude-1001
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/methods.txt"
}
```

```
1					[EQ] B ’ ( c ) = L ( c ) † X ( c ) where B’ ( c ) is the recovered temporal basis functions for condition c and † indicates pseudo-inversion. We quantified the 
2	“recoverability” of temporal basis functions on condition c as the variance explained in the temporal basis functions by the projected neural activity. If this metric is 1, it suggests that the 
3	condition’s loading matrix is invertible, and therefore fulfills the requirements of rotations. More specifically, we expect recoverability to fail when two (or more) temporal basis functions are 
4	assigned the same dimension in state space by the loading matrix. As each temporal basis functions dynamically supports each other, this overlap would preclude neural activity from acting as a 
5	dynamical system. Control for data smoothing One potential concern is that the factorization described above works well on neural data simply because the data are smoothed before analysis, and 
6	smoothing limits the frequency spectrum and therefore allows neural activity to be reconstructed by a small number of temporal basis functions. To test these possibilities, for each trial of each 
7	condition independently we shuffled time bins before smoothing and averaging, to disrupt the temporal structure of motor cortex activity while preserving inter-neuron spike correlations and total 
8	spike counts. We then extracted temporal basis functions, with the number of temporal basis functions matched to the original dataset, and quantified the population variance explained and 
9	recoverability (defined above) of the temporal basis functions. We compared this null distribution to the data distribution using a Wilcoxon signed-rank test to test for differences in distributions. 
10	Control for stereotyped time course of behavior One potential concern is that the factorization described above can find common frequencies between conditions simply because reaches take similar 
11	amounts of time, and motor cortex activity is likel
[... 371 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/methods.txt",
 "offset": 382
}
```

```
382	1 
383	Supplementary Figure 1: jPCA rotations incompletely describe motor cortex activity. a, 
384	Rotations uncovered by jPCA across datasets. jPCA identified two rotational planes in M1 activity, 
385	and one rotational plane in PMd. b, The fit of rotational dynamics identified by jPCA depended 
386	heavily on reach complexity. jPCA fit motor cortex activity on straight reaches substantially better 
387	than curved reaches (p < 0.001, Wilcoxon Signed Rank test). c, Multi-unit PSTHs and 
388	reconstruction by jPCA rotations and mean activity across conditions. Rotations captured little of 
389	the multi-phasic modulation of neural activity during reaching. Traces colored by target angle.  
390	M1-N
391	unit 61
392	unit 63
393	unit 63
394	unit 61
395	unit 44
396	unit 44
397	PMd-N
398	unit 35
399	unit 10
400	unit 49
401	unit 35
[... 340 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l "^checks:" claims/*.yaml | head -3; f=$(grep -l "^checks:" claims/*.yaml | head -1); sed -n '/^checks:/,$p' $f | head -30; grep -n "p_relation\|checks\|ready" tools/claims_check.py | head -30
```

```
claims/alasfour-2024.yaml
claims/andrews-2024.yaml
claims/armstrong-2026.yaml
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
  - fig7-exceeds-group. The comparison of Figure 7 with Figure 2
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A4 '"p_relation"' schemas/claims.schema.json
```

```
309:        "p_relation": {
310-          "description": "How p was reported: exactly (the default) or as a bound.",
311-          "enum": [
312-            "=",
313-            "<",
```

**Agent calls Bash**

```bash
cd  sed -n 309,325p schemas/claims.schema.json
```

```
"p_relation": {
          "description": "How p was reported: exactly (the default) or as a bound.",
          "enum": [
            "=",
            "<",
            ">"
          ]
        },
        "corrected": {
          "description": "The correction for multiple comparisons the paper applied, e.g. 'Bonferroni', 'FDR'.",
          "type": "string"
        },
        "ci": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "low",
```

**Agent**

Checker passes. Having read the full paper and supplement, I found several criteria that go beyond or against the paper. Applying fixes now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/sabatini-2024.yaml",
 "old_string": "    2 pi times the 100 Hz sampling rate, as in the code's extractParams.m). Reproduced when, in\n    each dataset, the median frequencies of the complex eigenvalue pairs, sorted by frequency,\n    lie within 10% of 0.5, 1.5, 2.5 and 4 Hz for the pairs present (at least three) and at least\n    one real eigenvalue is present on most conditions.",
 "new_string": "    2 pi times the 100 Hz sampling rate, as in the code's extractParams.m). An LDS of k dimensions\n    holds at most (k - 1)/2 complex pairs, so a dataset fitted with 5 or 7 dimensions (allowed by\n    fig2c) cannot show all four frequencies. Reproduced when, in each dataset, the median\n    frequencies of the complex eigenvalue pairs, sorted by frequency, lie within 10% of 0.5, 1.5,\n    2.5 and 4 Hz in that order for as many pairs as the dimensionality allows, and at least one\n    real eigenvalue is present on most conditions."
}
```

```
The file claims/sabatini-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/sabatini-2024.yaml",
 "old_string": "  criterion: Distance between two conditions is the norm of the difference of their\n    frequency-sorted eigenvalue vectors (code eigValDistance.m; the legend of Figure 3b says\n    averaging over corresponding eigenvalues, and the mean of the absolute differences is shown as\n    a variant). The null",
 "new_string": "  criterion: Distance between two conditions is the mean over corresponding (frequency-sorted)\n    eigenvalues of their distance in the complex plane (Figure 3b legend, \"averaging over the\n    distances between corresponding eigenvalues\"; Methods, \"mean distance between the\n    eigenvalues\"). The code's eigValDistance.m, the norm of the difference of the sorted\n    eigenvalue vectors, is shown as a variant. The null"
}
```

```
The file claims/sabatini-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/sabatini-2024.yaml",
 "old_string": "    on the fixed basis to two random halves of a condition's trials (Methods, Measuring the\n    across-condition alignment of rotations); repeats are open between 36 (Methods) and 200 (code\n    singleFrequencyOverlapControl.m). The paper's AUC is per rotation; the range covers rotations\n    and datasets. Reproduced when every rotation in every dataset has AUC in 0.765 to 1 with\n    observed alignment lower, and the test gives p < 0.001; partially when at least half of the\n    rotations do. The Results name a signed-rank test of unequal-size samples, so the code's\n    rank-sum test decides and the paper's name is recorded.",
 "new_string": "    on the fixed basis to two random halves of a condition's trials (Methods, Measuring the\n    across-condition alignment of rotations), 36 repeats (Methods); the code's 200 repeats\n    (singleFrequencyOverlapControl.m) are a variant. The paper's AUC is per rotation; the range\n    covers rotations and datasets. The Results name a Wilcoxon signed-rank test and do not say\n    what is paired; readings are (a) per condition, its mean alignment with the other conditions\n    against its mean noise alignment, signed-rank test over conditions; (b) the code's rank-sum\n    test of the two unpaired distributions. Reproduced when every rotation in every dataset has\n    AUC in 0.765 to 1 with observed alignment lower, and the test gives p < 0.001 under one\n    reading; partially when at least half of the rotations do."
}
```

```
The file claims/sabatini-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now fig4d (internal inconsistency), fig6e, fig7f and suppfig8.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/sabatini-2024.yaml",
 "old_string": "    per M1 dataset and one per PMd dataset); Pearson correlation per plane. Reproduced when every\n    plane's rho lies in 0.351 to 0.506 and the share with p < 0.05 is within tolerance (4 of 6\n    planes is 67%); partially when the rho range holds for at least half.",
 "new_string": "    per M1 dataset and one per PMd dataset); Pearson correlation per plane. Over 72 conditions any\n    rho above about 0.23 has p < 0.05, so the rho range and the 66% cannot both describe every\n    plane. Readings for the range are (a) per dataset, the mean rho over its retained planes; (b)\n    the rho of the planes correlated at p < 0.05. Reproduced when, under one reading, the values\n    lie in 0.351 to 0.506 and the share of planes with p < 0.05 is within tolerance (4 of 6\n    planes is 67%); partially when one of the two holds."
}
```

```
The file claims/sabatini-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/sabatini-2024.yaml",
 "old_string": "    kernel, length scale 400, lambda 0.1, of the rotation predictions (Methods). Shuffle, reach\n    parameters permuted across conditions, 1000 permutations. Reproduced",
 "new_string": "    kernel, length scale 400, lambda 0.1, of the rotation predictions (Methods). Shuffle, reach\n    parameters permuted across conditions; the paper gives no count, and 1000 permutations is a\n    standard choice, the fewest that can give p < 0.001. Reproduced"
}
```

```
The file claims/sabatini-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/sabatini-2024.yaml",
 "old_string": "    getVarExplainedKinematics.m, negatives set to 0). Kinematic readings as in fig6e. Reproduced\n    when, under one reading, every dataset's mean over trials lies in 75.6 to 100% and exceeds a\n    condition-shuffled null with p < 0.001.",
 "new_string": "    getVarExplainedKinematics.m, negatives set to 0). Kinematic readings as in fig6e. Reproduced\n    when, under one reading, every dataset's mean over trials lies in 75.6 to 100%. The Methods'\n    condition-shuffled null with a signed-rank test is run and reported; the paper reports no\n    result for it, so it does not decide."
}
```

```
The file claims/sabatini-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/sabatini-2024.yaml",
 "old_string": "  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.04\n    p_relation: \">\"\n  depends_on:\n  - fig7f-ldr-decoding",
 "new_string": "  statistics:\n  - about: lowest of the reported range\n    test: Wilcoxon signed-rank test\n    p: 0.04\n  - about: highest of the reported range\n    test: Wilcoxon signed-rank test\n    p: 0.96\n  depends_on:\n  - fig7f-ldr-decoding"
}
```

```
The file claims/sabatini-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat >> claims/sabatini-2024.yaml <<'EOF'
checks:
- date: 2026-11-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig3a-eigenvalue-clusters. The criterion required at least three complex pairs, but an LDS of 5 dimensions (within the 5 to 9 of fig2c) holds only two. The pairs are now judged as far as each dataset's dimensionality allows, in frequency order.
  - fig3c-eigenvalue-distance-auc. The code's vector norm was the main distance and the legend's average a variant. The Figure 3b legend and the Methods both give a mean over corresponding eigenvalues, so that is now the main measure and the code's norm the variant.
  - fig4b-plane-alignment (and suppfig6a-location-alignment, which follows it). The criterion set aside the Results' signed-rank test for the code's rank-sum test. The paper's test can be run with per-condition pairing, so that is now reading (a) and the rank-sum test reading (b). The Methods' 36 repeats now decide, with the code's 200 as a variant, as the file's own rule says.
  - fig4d-jpca-variance-correlation. The criterion required every plane's rho in 0.351 to 0.506 and also 4 of 6 planes at p < 0.05. Over 72 conditions every rho above about 0.23 is significant, so the two cannot both hold. Named two readings for the rho range (mean per dataset; significant planes only).
  - fig6e-kinematics-predict-location. The 1000 permutations are not in the paper; now marked as a standard choice.
  - fig7f-ldr-decoding. Removed the requirement to beat a condition-shuffled null at p < 0.001. The statement does not claim it and the paper reports no result for that null. It is now reported and does not decide.
  - suppfig8-no-output-potent-dependence. The statistics recorded p > 0.04, which the paper does not say; it reports p = 0.04 to 0.96. Now recorded as the two exact ends of the range.
  - Open. suppfig3-model-comparison compares a cross-validated TBF value with in-sample jPCA and LDS values. The Supplementary Figure 3 legend says the comparison is cross-validated, and the Methods give no held-out variance for jPCA or the single-condition LDS. The mix stays as the main reading, with all in-sample as the variant.
  - Open. suppfig8-no-output-potent-dependence uses p of at least 0.036 as its threshold for absence. The paper calls p = 0.04 not a substantial degradation and gives no threshold, so this is the file's own reading.
  - Open. fig6c-location-tracks-direction is qualitative in the paper; the circular correlation and its p < 0.05 are the file's reading.
  - Open. Many criteria rest on the code at commit b65f28d (windows, folds, penalties, SVD reductions, reach-duration definition). This check read only the paper and supplement and did not re-read the code, so those details are taken as the writer reported them.
EOF
python tools/claims_check.py claims/sabatini-2024.yaml paper/10.1038-s41467-024-51308-7.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes after my edits: `claims/sabatini-2024.yaml: 34 claims, 34 quotes, 22 statistical values, 0 problems`. It also passed before them, with 21 statistical values.

**Changes, by claim**
- **fig3a-eigenvalue-clusters:** the criterion required at least three rotation pairs. A 5-dimensional fit, which fig2c allows, can hold only two. Pairs are now judged as far as each dataset's dimensionality allows.
- **fig3c-eigenvalue-distance-auc:** the code's vector-norm distance was the main measure. The Figure 3b legend and the Methods both average over corresponding eigenvalues, so that is now the main measure and the code's norm is the variant.
- **fig4b-plane-alignment** (and **suppfig6a**, which follows it): the criterion replaced the paper's signed-rank test with the code's rank-sum test. The signed-rank test can be run by pairing per condition, so that is now reading (a) and rank-sum is reading (b). The Methods' 36 repeats now decide, with the code's 200 as a variant.
- **fig4d-jpca-variance-correlation:** the criterion could never pass. With 72 conditions, any correlation above about 0.23 is significant, so every plane in 0.39–0.46 contradicts only 66% of planes being significant. I named two readings for what the range covers.
- **fig6e-kinematics-predict-location:** the 1000 permutations are not in the paper. They are now marked as a standard choice.
- **fig7f-ldr-decoding:** I removed the requirement to beat a shuffled null at p < 0.001. The paper reports no result for that comparison, so it is now reported but does not decide.
- **suppfig8-no-output-potent-dependence:** the file recorded "p > 0.04", which the paper does not say. The paper gives p = 0.04 to 0.96, now recorded as those two values.

**Still open** (logged in `checks`)
- **suppfig3:** the main reading compares a cross-validated value for the paper's model with in-sample values for jPCA and the single-condition models. The legend says the comparison is cross-validated, but the Methods give no cross-validated value for those two.
- **suppfig8:** the pass threshold of p ≥ 0.036 is the file's own choice; the paper gives none.
- **fig6c:** the paper's finding is qualitative. The circular-correlation test is the file's own choice.
- **The analysis code:** many details (windows, folds, penalties) come from it, and I did not re-read it. I took those details as the writer reported them.

**Ready:** yes. All 34 claim ids are unchanged, every main finding has a claim, and none comes from outside this paper. Nothing was committed or pushed.

## End of run

23 turns, 3 minutes, $1.38 at API prices, result: success.
