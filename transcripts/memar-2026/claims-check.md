# memar-2026 · claims-check · run 44898115995

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i memar; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80; cat claims/memar-2026.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; awk '/^## Reader/,/^## Author/' docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/memar-2026.yaml"
}
```

```
1	# Claims for Ostadsharif Memar & Dehghani (2026), "Spatially Masked Regression Reveals Local and
2	# Distributed Predictability in Electrophysiological Recordings", doi:10.48550/arxiv.2606.11415.
3	#
4	# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-21, protocol as stated in docs/protocol.md (pilot-18), Reader role.
6	#
7	# Text read. The arXiv preprint, version 1 (arXiv:2606.11415v1, dated 11 June 2026), full text as
8	# stored under paper/ (paper/10.48550-arxiv.2606.11415.txt, "Version: preprint"): main text,
9	# Material and Methods (sections II A to II H, Algorithms 1 to 4), Results, Discussion, and the
10	# appendix Tables II (iEEG) and III (EEG) and Figure 6. The paper has no separate supplement and
11	# cites none. No version of record was available. The PDF was not needed; the table values were
12	# read from the text, row by row in the column order the headers give.
13	#
14	# Code read. GitHub neurovium/SpatiallyMaskedRegression (linked in the paper's footnote and Code
15	# Availability), commit 244dcdbd67f217873c2a52b77485d97c6fa9bf0e (2026-06-24, after the preprint's
16	# date). It holds the model (ReconModel.py, model.py), intra-subject training and the EEG
17	# cross-subject path (train.py, main.py), the iEEG cross-subject path (similarity.py,
18	# generate_adj_matrix_ieeg_unseen.py, Test_new_subject_iEEG.py), the coverage experiment
19	# (run_coverage_experiment.py), surrogates (Load_preprocess_data.py), the neighborhood and mask
20	# (neighborhood.py), settings (configs/settings.yaml), a METHODS.md map from the paper to the code,
[... 478 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/memar-2026.yaml paper/10.48550-arxiv.2606.11415.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.48550-arxiv.2606.11415.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.48550-arxiv.2606.11415.txt",
 "offset": 1366,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker reports no problems. I've read the whole paper. Next I'll check the arithmetic the opening comment relies on (subject means and SDs).

**Agent calls Bash**

```bash
python3 -c "
import numpy as np
d={'ieeg_intra':[.585,.647,.535,.452,.524,.428,.531,.487,.635,.605,.612,.593],
'ieeg_cross':[.331,.483,.440,.325,.509,.285,.415,.377,.409,.363,.395,.340],
'ieeg_block':[.148,.112,.698,.397,.129,.126,.159,.180,.130,.113,.112,.107],
'eeg_intra':[.897,.925,.980,.927,.893,.864,.894,.883,.882,.925,.918,.918,.872,.909,.928],
'eeg_cross':[.784,.782,.522,.635,.770,.783,.823,.837,.773,.895,.899,.831,.750,.840,.819]}
for k,v in d.items(): v=np.array(v); print(k, round(v.mean(),3), round(v.std(),3), round(v.std(ddof=1),3))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
python3 -c "
import statistics as s
d={'ieeg_intra':[.585,.647,.535,.452,.524,.428,.531,.487,.635,.605,.612,.593],
'ieeg_cross':[.331,.483,.440,.325,.509,.285,.415,.377,.409,.363,.395,.340],
'ieeg_block':[.148,.112,.698,.397,.129,.126,.159,.180,.130,.113,.112,.107],
'eeg_intra':[.897,.925,.980,.927,.893,.864,.894,.883,.882,.925,.918,.918,.872,.909,.928],
'eeg_cross':[.784,.782,.522,.635,.770,.783,.823,.837,.773,.895,.899,.831,.750,.840,.819]}
for k,v in d.items(): print(k, round(s.mean(v),3), round(s.pstdev(v),3), round(s.stdev(v),3))
"
```

```
ieeg_intra 0.553 0.068 0.071
ieeg_cross 0.389 0.064 0.066
ieeg_block 0.201 0.168 0.175
eeg_intra 0.908 0.028 0.029
eeg_cross 0.783 0.093 0.096
```

**Agent**

The table arithmetic matches the opening comment. Now I'll make the edits.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "# - The mask intensity behind the intra-subject, lagged and surrogate columns of Table II and\n#   Figure 2 is not stated in the paper. The code settles it as m = 1.0, the full neighborhood",
 "new_string": "# - The mask intensity behind the intra-subject, lagged and surrogate columns of Table II and\n#   Figure 2 is not stated in the Results. The model as defined in Methods II B and II C (Eqs. 1,\n#   2 and 7, w_ij = 0 for every j in N(i)) masks the whole neighborhood, which is m = 1.0, and the\n#   EEG cross-subject transfer uses m = 1.0 checkpoints (Results III B). The code settles it as m = 1.0, the full neighborhood"
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "  criterion: No test is reported. In Tables II and III the lowest EEG subject (0.864) is above the\n    highest iEEG subject (0.647). Reproduced when the EEG average exceeds the iEEG average and\n    every EEG subject value exceeds every iEEG subject value; partially reproduced when only the\n    averages are ordered.",
 "new_string": "  criterion: No test is reported. In Tables II and III the lowest EEG subject (0.864) is above the\n    highest iEEG subject (0.647). The paper does not define \"consistently\"; readings (a) every EEG\n    subject value exceeds every iEEG subject value, as in the tables; (b) the EEG average exceeds\n    the iEEG average. Reproduced when the EEG average exceeds the iEEG average; whether reading (a)\n    also holds is reported."
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "    split 50/50 into validation and test (random_state 42); for each electrode, the donor whose",
 "new_string": "    split 50/50 into validation and test (random_state 42). Which of the target's trials enter C\n    is not stated (Algorithm 2 splits before computing C but does not say which part is used);\n    readings (a) all of the target's trials, as the code does; (b) the validation trials only.\n    For each electrode, the donor whose"
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "  criterion: No test is reported. In Table II every subject's cross-subject value is below its\n    intra-subject value. Reproduced when the cross-subject average is below the intra-subject\n    average and above the phase-shuffled surrogate average of surrogate-ieeg, and the\n    cross-subject value is below the intra-subject value in at least 11 of 12 subjects; partially\n    reproduced when only the averages are so ordered. Note that the two settings score different\n    signals (single trials against trial averages; Methods II D 2), as the paper does.",
 "new_string": "  criterion: No test is reported. In Table II every subject's cross-subject value is below its\n    intra-subject value. The paper gives no reference level for \"appreciable predictive power\";\n    its support is the cross-subject average itself (0.389, Results III B). Reproduced when the\n    cross-subject average is below the intra-subject average and cross-ieeg-mean is reproduced;\n    partially reproduced when the average is below the intra-subject average but cross-ieeg-mean\n    is not reproduced. The number of subjects with cross below intra is reported (12 of 12 in\n    Table II). The two settings score different signals (single trials against trial averages;\n    Methods II D 2), as the paper does."
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "    criterion: As lagged-ieeg-no-gain, on the EEG data.",
 "new_string": "  criterion: As lagged-ieeg-no-gain, on the EEG data."
}
```

```
<tool_use_error>String to replace not found in file.
String:     criterion: As lagged-ieeg-no-gain, on the EEG data.</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "    (Methods II E; main.py run_lagged_too). A claim of no material gain; the paper reports no\n    test. Reproduced when the lagged average is within tolerance and differs from the\n    instantaneous average by less than 10% of the instantaneous average; not reproduced when the\n    lagged average exceeds the instantaneous one by 10% or more. The paired per-subject\n    differences and a Wilcoxon signed-rank test over the 12 subjects are reported as context.",
 "new_string": "    (Methods II E; main.py run_lagged_too). A claim of no material gain; the paper reports no\n    test and no threshold for \"materially\" or \"minimal changes\". The 10% bound below is the\n    protocol's default tolerance applied to the instantaneous average, an assumption and not the\n    paper's. Reproduced when the lagged average is within tolerance and differs from the\n    instantaneous average by less than 10% of the instantaneous average, in either direction;\n    not reproduced otherwise. The paired per-subject differences are reported; a Wilcoxon\n    signed-rank test over the subjects may be shown as context but does not decide the claim."
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "  criterion: The m = 1.0 values of fig4a-mask-sweep-ieeg. The sample DistCorr is never negative,\n    so the paper's comparison with zero is read with the surrogate floor it reports. Reproduced\n    when every subject's m = 1.0 value exceeds that subject's phase-shuffled surrogate value from\n    surrogate-ieeg; partially reproduced when the average does but some subjects do not.",
 "new_string": "  criterion: The m = 1.0 values of fig4a-mask-sweep-ieeg. The paper compares them with zero only\n    and gives no test. Readings (a) as written, the m = 1.0 average is above zero; the sample\n    DistCorr of Eqs. 11 to 14 is never negative and is positive for almost any pair of finite\n    series, so this reading cannot fail and does not decide the claim; (b) the m = 1.0 average\n    exceeds the phase-shuffled surrogate average of surrogate-ieeg, the paper's own control for\n    reconstruction without temporal structure (Results III F), a comparison the paper does not\n    make for Figure 4. The author judges by reading (b), as an assumption, and reports reading\n    (a) and the number of subjects whose m = 1.0 value exceeds their own phase-shuffled value.\n    Reproduced when (b) holds; not reproduced otherwise."
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "    masked; All, only the target masked. Reproduced when, under one reading, the subject average\n    is ordered All > Local > Non-local and Local exceeds Non-local in at least 11 of 12 subjects\n    (\"consistently\"); partially reproduced when the averages are so ordered but fewer subjects\n    are. The per-subject values of the three conditions are reported.",
 "new_string": "    masked; All, only the target masked. The paper does not define \"consistently\"; readings (a)\n    Local exceeds Non-local in every subject; (b) Local exceeds Non-local in the subject average\n    of each dataset (Figure 5A and 5B). Reproduced when, under one reading of the open trial\n    details, the subject average is ordered All > Local > Non-local (which meets reading b);\n    not reproduced otherwise. The number of subjects with Local above Non-local, and so whether\n    reading (a) holds, and the per-subject values of the three conditions are reported."
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "  criterion: As fig5a-coverage-ieeg, on the EEG data, with at least 14 of 15 subjects for\n    \"consistently\".",
 "new_string": "  criterion: As fig5a-coverage-ieeg, on the EEG data (reading a, all 15 subjects)."
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "  criterion: No test is reported. From the paper's averages, the cross over intra ratio is 0.70\n    for iEEG (0.389 / 0.553) and 0.86 for EEG (0.783 / 0.908). Reproduced when the iEEG ratio is\n    below the EEG ratio; the ratios and the differences are reported.",
 "new_string": "  criterion: No test is reported, and the paper does not say how the penalty is measured.\n    Readings (a) the cross over intra ratio, 0.70 for iEEG (0.389 / 0.553) and 0.86 for EEG\n    (0.783 / 0.908) from the paper's averages; (b) the intra minus cross difference, 0.164 for\n    iEEG and 0.125 for EEG. Reproduced when the iEEG penalty is larger than the EEG penalty under\n    one reading; the ratios and the differences are reported."
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "  statement: In iEEG, phase shuffling degrades reconstruction most and IAAFT surrogates keep the\n    most reconstructability of the three surrogates.\n  source: Results, III F, paragraph 4; Table II",
 "new_string": "  statement: In iEEG, phase shuffling degrades reconstruction most on average, and IAAFT\n    surrogates retain somewhat more reconstructability.\n  source: Results, III F, paragraph 4; Table II"
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "  criterion: The three surrogate averages of surrogate-ieeg. Reproduced when phase shuffle <\n    block shuffle < IAAFT, the order of Table II (0.181, 0.201, 0.232); partially reproduced\n    when phase shuffle is lowest but block shuffle and IAAFT are in the other order.",
 "new_string": "  criterion: The three surrogate averages of surrogate-ieeg. The text does not say what IAAFT\n    retains more than; readings (a) more than phase shuffle; (b) the most of the three, the order\n    of Table II (phase 0.181, block 0.201, IAAFT 0.232). Reproduced when the phase-shuffle\n    average is the lowest of the three (which meets reading a); not reproduced otherwise.\n    Whether the block and IAAFT averages are in the order of Table II (reading b) is reported."
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/memar-2026.yaml",
 "old_string": "  statement: In EEG, phase shuffling degrades reconstruction most and IAAFT surrogates keep the\n    most reconstructability of the three surrogates.",
 "new_string": "  statement: In EEG, phase shuffling degrades reconstruction most on average, and IAAFT\n    surrogates retain somewhat more reconstructability."
}
```

```
The file claims/memar-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now I'll add the `checks` entry and re-run the checker.

**Agent calls Bash**

```bash
cd  tail -c 200 claims/memar-2026.yaml | od -c | tail -3; grep -rn "^checks:" claims/*.yaml | head -2; f=$(grep -l "^checks:" claims/*.yaml | head -1); [ -n "$f" ] && sed -n '/^checks:/,$p' "$f" | head -20
```

```
0000260   r       0   .   1   2   4   ,       0   .   1   6   0   ,    
0000300   0   .   1   8   4   )   .  \n
0000310
claims/alasfour-2024.yaml:645:checks:
claims/andrews-2024.yaml:850:checks:
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
  - fig5-pre-postcentral. The criterion cited Discussion paragraph 2 for the alpha sign; that paragraph gives theta and gamma only.
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> claims/memar-2026.yaml <<'EOF'
checks:
- date: 2026-11-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header, mask intensity. Said the paper does not state m for the intra-subject, lagged and surrogate columns; Methods II B and II C (Eqs. 1, 2 and 7, w_ij = 0 for all j in N(i)) define the model with the whole neighborhood masked, and Results III B uses m = 1.0 for EEG transfer. Added these as support for m = 1.0 alongside the code.
  - intra-eeg-above-ieeg. The criterion required every EEG subject above every iEEG subject; the paper does not define "consistently". Named the two readings (every subject, the averages) and judged on the averages, with reading (a) reported.
  - cross-ieeg-mean. Which of the target's trials enter the correlation matrix C is not stated (Algorithm 2 splits the trials before computing C); named the readings, all trials as the code, or the validation trials only.
  - cross-below-intra-ieeg. Removed the comparison with the phase-shuffled surrogate average and the 11 of 12 subjects rule; the paper makes neither, and the surrogates score single trials while cross-subject scores trial averages. "Appreciable" is now judged by cross-ieeg-mean, the number the paper gives for it; the per-subject count is reported.
  - lagged-ieeg-no-gain. The 10% bound on the difference is not the paper's; the criterion now says it is the protocol's default tolerance and an assumption. The criterion left a lagged average 10% or more below the instantaneous one undecided; it now fails the claim in either direction ("only minimal changes"). The Wilcoxon test no longer decides anything.
  - full-mask-above-zero-ieeg. The comparison with the surrogate floor was presented as the paper's reading; the paper compares with zero only. Named reading (a), as written, which the nonnegative DistCorr cannot fail, and reading (b), the phase-shuffled surrogate average, as an assumption the author judges by. Dropped the every-subject requirement, which the paper does not make, and report the subject count.
  - fig5a-coverage-ieeg, fig5b-coverage-eeg. Removed the 11 of 12 and 14 of 15 thresholds for "consistently", which the paper does not give; named the readings (every subject, the average of each dataset), judge on the averages, and report the subject counts.
  - transfer-penalty-larger-ieeg. The paper does not say how the penalty is measured; named the ratio and the difference as readings (both give iEEG the larger penalty on the paper's numbers).
  - surrogate-order-ieeg, surrogate-order-eeg. The statements said IAAFT keeps the most of the three; the paper says IAAFT "retained somewhat more", without saying more than what. Restated as in the paper; the criterion judges phase shuffle lowest and reports the block against IAAFT order as reading (b).
  - Open. The m = 1.0 intra-subject setting, the iEEG trial definition (which movement events, which days, where preprocessing is applied) and the subject order are readings the file names; the paper and code do not settle them, and the code may not be the version that produced the reported numbers.
  - Open. Tolerances for subject values and averages are the SDs the tables print (across electrodes, or across subjects for averages); this follows the protocol, but the cross-subject subject SDs are very small (0.004 to 0.016), so those per-subject claims are strict.
  - Open. How Figure 4 averages over electrodes and subjects is not stated; the criterion uses the subject average, with the per-subject counts reported.
  - Open. The EEG claims (data elsewhere) have no accession or version for the BNCI dataset, and the session and trial window used are not stated.
EOF
python tools/claims_check.py claims/memar-2026.yaml paper/10.48550-arxiv.2606.11415.txt; grep -n "rather\|—" claims/memar-2026.yaml; python3 -c "import yaml;yaml.safe_load(open('claims/memar-2026.yaml'))" && echo yaml ok
```

Result: not kept, because it reads the paper's text.

**Agent**

The file is ready for an attempt (`ready: true`). I made no commits and changed no claim ids.

**Checker result** (same before and after my edits): `claims/memar-2026.yaml: 20 claims, 20 quotes, 0 statistical values, 0 problems`

**What I confirmed:** every Table II and III value, source paragraph and quote matches the paper. I recomputed the Average rows: the ± is the population SD across subjects, as the opening comment says. All main findings have a claim, and none comes from outside this paper.

**Changes, by claim:**
- **Opening comment (mask intensity):** the file said the paper never states the mask intensity for the main columns. The Methods (Eqs. 1, 2 and 7) define the model with the whole neighborhood masked, and the EEG transfer uses m = 1.0. I added this as support for m = 1.0 alongside the code.
- **intra-eeg-above-ieeg:** the paper does not define "consistently". I named two readings (every subject, or the averages); the claim is judged on the averages and the every-subject reading is reported.
- **cross-ieeg-mean:** the paper does not say which of the target's trials go into the electrode correlation matrix. I named two readings: all trials (as the code does) or the validation trials only.
- **cross-below-intra-ieeg:** I removed a comparison with the surrogate floor and an 11-of-12-subjects rule; the paper makes neither. "Appreciable" is now judged by cross-ieeg-mean, the number the paper gives for it.
- **lagged-ieeg-no-gain:** the 10% bound on the difference is now marked as an assumption, not the paper's. A large drop now also fails the claim; before, it was left undecided. The Wilcoxon test no longer decides anything.
- **full-mask-above-zero-ieeg:** the paper compares with zero only, which can never fail because DistCorr is never negative. I named two readings: above zero as written, and above the phase-shuffled surrogate average, which the author judges by as an assumption. I dropped an every-subject requirement the paper does not make.
- **fig5a-coverage-ieeg, fig5b-coverage-eeg:** I removed the 11-of-12 and 14-of-15 thresholds for "consistently". The claims are judged on the averages, with subject counts reported.
- **transfer-penalty-larger-ieeg:** I named the ratio and the difference as readings of "transfer penalty". Both give iEEG the larger penalty on the paper's numbers.
- **surrogate-order-ieeg, surrogate-order-eeg:** the statements said IAAFT keeps the most of the three surrogates. The paper says only that it "retained somewhat more". I restated the claims and now judge them on phase shuffle being lowest.

**Still open (recorded in `checks`):**
- Several details are left as named readings because neither the paper nor the code settles them: the m = 1.0 setting, which movement events and recording days form the trials, where preprocessing is applied, and the subject order. The repository's code may also not be the version that produced the reported numbers.
- The per-subject cross-subject tolerances are the paper's own SDs across electrodes (0.004 to 0.016), so those claims are very strict.
- The paper does not say how Figure 4 averages over electrodes and subjects.
- For the EEG claims (data elsewhere), the paper gives no BNCI accession or version, and does not say which session or trial window was used.

## End of run

24 turns, 2 minutes, $1.06 at API prices, result: success.
