# crcns-ofc-4 · claims-check · run 41888751076

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/crcns-ofc-4/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 100,220p docs/protocol.md; cat claims/crcns-ofc-4/*.yaml; python tools/claims_check.py claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml paper/10.1016-j.neuron.2016.08.019.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml paper/10.1016-j.neuron.2016.08.019.txt; wc -l claims/crcns-ofc-4/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml"
}
```

```
1	# Claims for Schuck, Cai, Wilson & Niv (2016), Neuron 91:1402-1412, on CRCNS data set ofc-4
2	# (doi:10.6080/K0FN14CH).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-04,
4	# protocol as stated in docs/protocol.md (Reader).
5	#
6	# Text read: the version of record with its Supplemental Information, as supplied under paper/
7	# (PyMuPDF text of the journal PDF): Summary, Results, Discussion, Experimental Procedures, the
8	# legends of Figures 1 to 5, and the supplement (legends of Figures S1 to S5, Table S1, and the
9	# Supplemental Results 1.1 to 1.5). The supplement's text carries line numbers between its
10	# lines; quotes from it are cut with "..." at those breaks. The paper links no analysis code
11	# (it names SPM8, the PhysIO toolbox, LIBSVM, the Princeton MVPA toolbox, R with lmer and boot,
12	# neuRosim and AFNI), so no code was read. The data descriptor names BrainIAK for building
13	# design matrices; that is not the paper's code.
14	#
15	# Data the paper used. 30 adults scanned, 3 excluded, 27 analysed (13 female, mean age 22.18,
16	# range 18 to 31), most with five runs (mean 4.9). Face-house age-judgment task with
17	# mini-blocks; 16 states from previous category, previous age, current category and current
18	# age, labelled (Ho)Fy and so on; trial classes Enter (8 states, category switch), Internal
19	# (4 states) and Exit (4 states). Five scanner runs, 485 trials in all, after three training
20	# blocks of 97 trials outside the scanner. 3 T Siemens Skyra, EPI with TR 2.4 s, 46 slices.
[... 730 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.08.019.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.08.019.txt",
 "offset": 700,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker's two warnings are the CI bounds, printed in the text with a garbled minus sign ("[�0.8432, �0.0169]"); the values match. Reading the supplement now.

**Agent calls Bash**

```bash
sed -n 1000,2260p paper/10.1016-j.neuron.2016.08.019.txt | grep -v '^[0-9]\{1,3\}$'
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper and supplement are read. I'm making the corrections now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "  criterion: Error rate as error and time-out responses (both led to feedback, Methods, Task)\n    over all responded trials of the five runs, per participant, then the mean over\n    participants. The denominator is open; readings are (a) all trials including the\n    repetitions that follow errors, (b) all trials but the first of each run. Reproduced when\n    under one reading the mean is within tolerance.",
 "new_string": "  criterion: Error rate per participant over the trials of the five runs, then the mean over\n    participants. Whether time-outs count as errors is open (both led to feedback, Methods,\n    Task; time-outs were 0.3% of trials, Supplemental Results 1.1, more than the tolerance);\n    readings are errors only, and errors plus time-outs. The denominator is open; readings are\n    (a) all trials including the repetitions that follow errors, (b) all trials but the first\n    of each run. Reproduced when under one reading the mean is within tolerance."
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "    significant; the slope is reported either way. The model family is open as in\n    supp-errors-by-trial-class; both readings are shown and the absence is judged on (a).",
 "new_string": "    significant; the slope is reported either way. The model family is open as in\n    supp-errors-by-trial-class; both readings are shown and the absence is judged on (a), the\n    linear mixed model, as the Methods name lmer, which fits linear models."
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "  criterion: From the predictions of fig2a-16way-decoding, each test map scored correct on a\n    component when predicted and true state agree on it (Methods, fMRI Data Analysis); per\n    participant the proportion correct; one-sided one-sample t-test against 50%. Reproduced\n    when all three components have p < 0.05; partially reproduced when one or two do.",
 "new_string": "  criterion: From the predictions of fig2a-16way-decoding, each test map scored correct on a\n    component when predicted and true state agree on it (Methods, fMRI Data Analysis); per\n    participant the proportion correct; one-sided one-sample t-test against 50%. The paper's\n    numbers do not agree with each other (t26 > 3 gives a one-sided p below 0.003, not 0.014\n    or 0.007), so the p-values may come from the bootstrap of Figure S2B (participants\n    resampled with replacement, 10000 iterations, Supplemental Results 1.2); readings are the\n    t-test and that bootstrap. Reproduced when under one reading all three components have p\n    < 0.05; partially reproduced when one or two do."
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "  statistics:\n  - test: t-test against chance, one-sided\n    p: 0.72\n    p_relation: \">\"\n  depends_on:\n  - fig2a-16way-decoding\n  criterion: A claim of absence. Current-age accuracy as in fig2b-hidden-components, one-sided\n    one-sample t-test against 50% at p < 0.05. Reproduced when the test is not significant.",
 "new_string": "  statistics:\n  - test: test against chance, one-sided (test not named)\n    p: 0.72\n    p_relation: \">\"\n  depends_on:\n  - fig2a-16way-decoding\n  criterion: A claim of absence. Current-age accuracy as in fig2b-hidden-components, one-sided\n    one-sample t-test against 50% at p < 0.05, the test the Results imply for Figure 2B (t26);\n    the bootstrap of Figure S2B, which the sentence cites, is shown as a variant. Reproduced\n    when the t-test is not significant."
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "  statistics:\n  - test: t-test against chance, one-sided\n    p: 0.66\n    p_relation: \">\"\n  depends_on:\n  - fig2-two-back-state-space\n  criterion: A claim of absence. Component accuracies for category and age of two trials back\n    from the predictions of fig2-two-back-state-space, one-sided one-sample t-test against\n    50% at p < 0.05. Reproduced when neither is significant.",
 "new_string": "  statistics:\n  - test: test against chance, one-sided (test not named)\n    p: 0.66\n    p_relation: \">\"\n  depends_on:\n  - fig2-two-back-state-space\n  criterion: A claim of absence. Component accuracies for category and age of two trials back\n    from the predictions of fig2-two-back-state-space, one-sided one-sample t-test against\n    50% at p < 0.05, the test the Results imply for Figure 2B (t26); the bootstrap of Figure\n    S2B is shown as a variant. Reproduced when neither t-test is significant."
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "    value: 55.5\n    tolerance: 5.5\n    unit: percent",
 "new_string": "    value: 55.5\n    tolerance: 5.55\n    unit: percent"
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "    value: 51.5\n    tolerance: 0.15\n    unit: percent\n  - quantity: upper 95th percentile, previous age\n    value: 51.7\n    tolerance: 0.17\n    unit: percent\n  - quantity: upper 95th percentile, current category\n    value: 51.4\n    tolerance: 0.14\n    unit: percent\n  - quantity: upper 95th percentile, current age\n    value: 51.7\n    tolerance: 0.17\n    unit: percent\n  criterion: Training labels permuted in each fold, 10 permutations per participant, accuracies\n    averaged within participant, test labels unchanged (Supplemental Results 1.2). The\n    component tolerances are 10% of the distance from chance (1.5 to 1.7 points), as 10% of\n    the value would span chance. The distribution whose 95th percentile is reported, and the\n    test behind p < 0.025, are open; readings are (a) the participants' averaged permutation\n    accuracies, with a paired t-test of real against permuted; (b) all participant and\n    permutation values pooled, with the real group mean compared to the percentile.\n    Reproduced when under one reading the permuted 16-way mean is not above 6.25% at p < 0.05\n    and the real 16-way accuracy exceeds the permuted at p < 0.025; the percentiles are\n    compared with the expected values and reported.",
 "new_string": "    value: 51.5\n    tolerance: 5.15\n    unit: percent\n  - quantity: upper 95th percentile, previous age\n    value: 51.7\n    tolerance: 5.17\n    unit: percent\n  - quantity: upper 95th percentile, current category\n    value: 51.4\n    tolerance: 5.14\n    unit: percent\n  - quantity: upper 95th percentile, current age\n    value: 51.7\n    tolerance: 5.17\n    unit: percent\n  criterion: Training labels permuted in each fold, 10 permutations per participant, accuracies\n    averaged within participant, test labels unchanged (Supplemental Results 1.2). The\n    tolerances are the default 10% of the value; the percentiles are chance-level numbers\n    from 10 random permutations, so the claim rests on the comparison with the real accuracy.\n    The distribution whose 95th percentile is reported, and the test behind p < 0.025, are\n    open; readings are (a) the participants' averaged permutation accuracies, with a paired\n    t-test of real against permuted; (b) all participant and permutation values pooled, with\n    the real group mean compared to the percentile. Reproduced when under one reading the\n    permuted 16-way mean is not above 6.25% at p < 0.05 and the real accuracy exceeds the\n    permuted at p < 0.025 for the 16-way classification and each of the four components;\n    partially reproduced when this holds for the 16-way classification but not for every\n    component. The percentiles are compared with the expected values and reported."
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "    The participant's peak is read as the peak of the conjunction searchlight within OFC\n    (Figure S3C); the searchlight radius",
 "new_string": "    The Methods place the peak at each participant's maximum decoding and cite Figure S5,\n    which shows Euclidean distances, so the reference is wrong. Readings are (a) the peak of\n    the participant's conjunction searchlight within OFC (Figure S3C), (b) the peak of the\n    participant's 16-way searchlight accuracy within OFC. The Methods simulate whole-brain\n    data and match the real data's smoothness with AFNI's 3dFWHMx; with OFC voxels only, both\n    are restricted to the OFC mask, as a deviation. The searchlight radius"
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "    averaged within participant (Methods, fMRI Data Analysis); one-sample t-test against 50%,\n    one-sided as in the Figure 2 and S2 legends (two-sided shown).",
 "new_string": "    averaged within participant (Methods, fMRI Data Analysis); one-sample t-test against 50%,\n    one-sided as the Results state for Figure 2B and the Figure S2 legend for its panels\n    (two-sided shown)."
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "  statement: Hippocampus, DLPFC and FFA/PPA code current and previous category but not previous\n    age, and show neither complete nor task-specific encoding; decoding there is not related to\n    error rates or behavior as it is in OFC, except a weaker relation in PPA/FFA.",
 "new_string": "  statement: Hippocampus, DLPFC and FFA/PPA code current and previous category but not previous\n    age, and show neither complete nor task-specific encoding. Their decoding accuracy does\n    not correlate with error rate in hippocampus or DLPFC but does in PPA/FFA, and in none of\n    them does pattern similarity relate to transition error rates."
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "    shown. Reproduced when trial 0 is lower at p < 0.05.",
 "new_string": "    shown. The paper gives t24 for trial 0 though 24 participants enter the error analyses\n    (Methods, Participants), which implies 23 degrees of freedom; the difference is reported\n    with its degrees of freedom. Reproduced when trial 0 is lower at p < 0.05; trial -1 is\n    reported against p = 0.07."
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml",
 "old_string": "    age, current category and the correct response side, with GLM onsets at the response; the\n    analysis of fig2a-16way-decoding in OFC, t-test against chance at p < 0.05.",
 "new_string": "    age, current category and the correct response side, with GLM onsets at the response; the\n    analysis of fig2a-16way-decoding in OFC, t-test against chance at p < 0.05. Which accuracy\n    the ROI test uses is not given; readings are the 16-way accuracy against 6.25% and the\n    motor-response component against 50%. The test is not named; the t-test is a reading."
}
```

```
The file claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -l "^checks:" claims/*/*.yaml | head -2 | xargs -I{} sh -c 'sed -n "/^checks:/,\$p" {} | head -20'
```

```
checks:
- date: 2026-10-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
  - exc-thalamus-photoinhibition. Removed latency reading (b), a 3 s.d. threshold on Vm that appears nowhere in the paper. The Methods' touch-latency rule is applied to laser onset, and the criterion says this is an assumption.
  - pv-enphr-suppression. Same change for its latencies; the Methods' dPSTH/dt rule is applied to the laser-onset PSTH, as an assumption.
  - ion-cut-exc-no-touch. The post-touch Vm (Vm at the peak of the average PSP) is undefined without a PSP and biased upward on a flat average. The test now uses the paper's touch epoch (4 to 50 ms) against the 0 to 5 ms pre-touch mean, with the peak-based amplitude as a variant.
  - fs-suppress-movement-spiking. The paper does not name the groups of its Kruskal-Wallis test; the criterion now says the test is reported and does not enter the outcome.
  - auc-weak-strong. The criterion compared groups on the Fig. 
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml <<'EOF'
checks:
- date: 2026-11-04
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Checker. The two values it did not find, the CI bounds -0.8432 and -0.0169 of fig4a-decoding-error-correlation, are in the text with a garbled minus sign; they match the paper.
  - behavior-error-rate. The criterion counted time-outs as errors and spoke of responded trials, which excludes time-outs; whether they count is not stated and they are 0.3% of trials, more than the tolerance. Named it open, with both readings.
  - supp-errors-stable-over-blocks. Gave the reason for judging the absence on the linear mixed model, the Methods naming lmer.
  - fig2b-hidden-components. t26 > 3 implies a one-sided p below 0.003, which does not agree with the reported 0.014 and 0.007; the p-values may come from the Figure S2B bootstrap. Named the bootstrap as a second reading.
  - fig2b-current-age-absent and fig2b-two-back-absent. The test behind p > 0.72 and p > 0.66 is not named; the statistics no longer call it a t-test, and the criterion names the t-test as the one the Results imply with the bootstrap of Figure S2B as a variant.
  - figs2c-8way-decoding. The current-category tolerance was 5.5; 10% of 55.5 is 5.55.
  - figs2a-permutation-control. The component tolerances of 0.14 to 0.17 points were justified by spanning chance, which does not apply to a chance-level permutation percentile from 10 permutations; set to the default 10% of the value. The statement covers each binary component, but the criterion judged the 16-way result only; it now judges all four components, with partial reproduction when only the 16-way holds.
  - synthetic-data-control. The Methods cite Figure S5 for the participant peaks, which is the Euclidean-distance figure; the criterion read Figure S3C without saying so. Named the wrong reference and two readings (conjunction peak, 16-way searchlight peak), and noted that whole-brain simulation and smoothness matching are restricted to OFC.
  - fig2d-enter-nonenter-decoding. The criterion said the Figure 2 legend states one-sided tests; it does not. Cited the Results for Figure 2B and the Figure S2 legend.
  - other-rois-incomplete. The statement called the PPA/FFA relation weaker, which the paper does not say, and mixed the decoding-error correlation with the similarity analysis. Rewrote it to give each as the paper does.
  - fig4b-error-vs-matched. Noted that t24 does not fit the 24 participants of the error analyses, and that trial -1 is reported against p = 0.07, as the statement includes it.
  - supp-motor-action-not-in-ofc. Which accuracy the OFC ROI test (p = .40) uses and which test it is are not given; named the 16-way and motor-component readings.
  - Open. fig3-searchlight-conjunction gives the peak as left medial orbital gyrus at x = 3, as the Results do, while Table S1 lists the conjunction peak as right rectal gyrus; the claim cannot be tested on the data set either way.
  - Open. The paper's GLM nuisance set (26 cardiac regressors, SPM8) cannot be rebuilt from the data set as described (header, O5).
  - Coverage. The decoding of response mapping in visual cortex (Figure S3B) has no claim; it is an exploratory supplementary result and was not added.
EOF
python tools/claims_check.py claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml paper/10.1016-j.neuron.2016.08.019.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file is ready for an attempt. I changed only `claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml` and did not commit.

**Checker result:** `29 claims, 29 quotes, 47 statistical values, 2 problems`. Both problems are the confidence-interval bounds of `fig4a-decoding-error-correlation` (-0.8432 and -0.0169). They are in the paper; the text shows them with a garbled minus sign ("[�0.8432, �0.0169]"), so the values are correct.

**Changes, by claim:**
- **behavior-error-rate:** The criterion counted time-outs as errors, which the paper does not say. Time-outs are 0.3% of trials, more than the 0.23 tolerance, so counting them or not is now an open reading with both versions.
- **supp-errors-stable-over-blocks:** Added the reason for judging this on the linear mixed model: the Methods name lmer, which fits linear models.
- **fig2b-hidden-components:** The paper's numbers disagree. A t26 above 3 gives a one-sided p below 0.003, not the reported 0.014 or 0.007. The bootstrap of Figure S2B is now a second reading.
- **fig2b-current-age-absent, fig2b-two-back-absent:** The paper does not name the test behind p > 0.72 and p > 0.66, so the statistics no longer call it a t-test. The criterion still judges on the t-test the Results imply, with the bootstrap shown as a variant.
- **figs2c-8way-decoding:** The current-category tolerance was 5.5; 10% of 55.5 is 5.55.
- **figs2a-permutation-control:**
  - The component tolerances (0.14 to 0.17 points) rested on a weak reason, so they are now the default 10% of the value.
  - The statement covers all four components, but the criterion only judged the 16-way result. It now judges all four.
- **synthetic-data-control:** For the participant peak locations, the Methods cite Figure S5, which is the Euclidean-distance figure. The claim had silently read Figure S3C instead. Both the conjunction peak and the 16-way searchlight peak are now named as readings. Restricting the simulation to the OFC mask is recorded as a deviation.
- **fig2d-enter-nonenter-decoding:** The criterion said the Figure 2 legend states one-sided tests, which it does not. The citation now points to the Results for Figure 2B and to the Figure S2 legend.
- **other-rois-incomplete:** The statement called the PPA/FFA relation "weaker", which the paper does not say, and it mixed two analyses. It now states the decoding-and-error-rate correlation and the similarity analysis separately, as the paper does.
- **fig4b-error-vs-matched:** Noted that the paper's t24 does not fit the 24 participants in the error analyses. Trial -1 is now reported against p = 0.07.
- **supp-motor-action-not-in-ofc:** The paper does not say which accuracy or which test gives the OFC result (p = .40). Two readings are named: 16-way accuracy against 6.25%, and the motor-response component against 50%.

**What remains open:**
- **fig3-searchlight-conjunction:** The main text puts the peak in the left medial orbital gyrus at x = 3, while Table S1 lists the right rectal gyrus. The data set cannot test this claim either way.
- **Nuisance regressors:** The paper's GLM used 26 cardiac regressors in SPM8. These cannot be rebuilt from the data set as its description gives it; this is already recorded as O5 in the header.
- **Coverage:** Decoding of the response mapping in visual cortex (Figure S3B) has no claim. I left it out because it is an exploratory supplementary result.

**Ready:** yes. The new `checks` entry is marked `ready: true`.

## End of run

22 turns, 3 minutes, $1.12 at API prices, result: success.
