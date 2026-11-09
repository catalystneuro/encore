# 000011 · claims-check · run 39599286289

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000011/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,220p docs/protocol.md
```

```
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
     links, and the criterion says which. Search all of them before
     treating a detail as open.
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000011/10.1038-nature17643.yaml; python tools/claims_check.py claims/000011/10.1038-nature17643.yaml paper/10.1038-nature17643.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000011/10.1038-nature17643.yaml paper/10.1038-nature17643.txt | tail -30; wc -l claims/000011/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000011/10.1038-nature17643.yaml"
}
```

```
1	# Claims for Li, Daie, Svoboda & Druckmann (2016) on dandiset 000011.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
3	# as stated in docs/protocol.md, Reader steps 1 to 4.
4	#
5	# Text read: the HHMI author manuscript in PubMed Central (PMC5081260, NIHMS767125), as served by
6	# Europe PMC (paper/10.1038-nature17643.txt): main text, Methods, the legends of Figures 1 to 6 and
7	# of Extended Data Figures 1 to 10. It is the accepted manuscript, not the version of record. The
8	# paper has no Supplementary Information beyond the Extended Data (the record says no supplement).
9	# No PDF was supplied, so no figure could be read; values shown only in figures are not claimed.
10	# Not read: the Corrigendum (Nature 537, 122; doi:10.1038/nature18623), which the record lists and
11	# the text does not include. Whether it changes any value below is not known.
12	#
13	# Code read: none. The paper links no analysis or model code. It names the data deposit "Data have
14	# been deposited at https://crcns.org/ and can be accessed at http://doi:10.6080/K0RB72JW". The
15	# dandiset is listed for this paper; which of the experiments below it holds is for the author to
16	# find. The dataset's files were not looked at.
17	#
18	# The data the paper used, as it reports them (Methods). 33 mice, male and female, older than P60.
19	# Photoinhibition behaviour, 10 VGAT-ChR2-EYFP and 9 PV-ires-cre x Rosa26-LSL-ReaChR mice; of these,
20	# 5 VGAT and 7 PV x ReaChR mice also had electrophysiology during behaviour. Callosotomy, 7 mice (6
[... 835 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature17643.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature17643.txt",
 "offset": 7,
 "limit": 50
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature17643.txt",
 "offset": 7,
 "limit": 30
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && fold -s -w 200 paper/10.1038-nature17643.txt > p.txt && wc -l p.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
echo $TMPDIR
```

```
/tmp/claude-1001
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 200
}
```

```
1	DOI: 10.1038/nature17643
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	Nature Nature 544 hhmipa Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title Howard Hughes Medical Institute Author Manuscripts PMC5081260 PMC5081260.1 5081260 5081260 
8	NIHMS767125 27074502 10.1038/nature17643 NIHMS767125 HHMIPA767125 1 Article Robust neuronal dynamics in premotor cortex during motor planning Li Nuo * Daie Kayvon * Svoboda Karel # Druckmann Shaul # 
9	Janelia Research Campus, HHMI, Ashburn VA 20147 * co-first author # corresponding author Karel Svoboda, Janelia Research Campus, HHMI, 19700 Helix Drive, Ashburn, VA 20147, [removed: an e-mail address] 
10	., Shaul Druckmann, Janelia Research Campus, HHMI, 19700 Helix Drive, Ashburn, VA 20147, [removed: an e-mail address] . 13 4 2016 28 4 2016 532 7600 278020 459 464 13 03 2016 27 10 2016 27 10 2016 05 
11	08 2025 Reprints and permissions information is available at www.nature.com/reprints . Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of 
12	academic research, subject always to the full Conditions of use: http://www.nature.com/authors/editorial_policies/license.html#terms Corrigendum: Robust neuronal dynamics in premotor cortex during 
13	motor planning. 537 7618 29 6 2016 122 122 Nature 10.1038/nature18623 27362233 Neuroscience: Fault tolerance in the brain. 532 7600 13 4 2016 449 450 Nature 10.1038/nature17886 27074510 Neural 
14	activity maintains representations that bridge past and future events, often over many seconds. Network models can produce persistent and ramping activity, but the positive feedback that is critical 
15	for these slow dynamics can cause sensitivity to perturbations. Here we use electrophysiology and optogenetic perturbations in mouse premotor cortex to probe
[... 185 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 200,
 "limit": 370
}
```

```
200	sessions, Figs 3 , 4 , and Extended Data Figs 6 , 8 , 9 ). For a population of n neurons, we found an n × 1 vector, in the n dimensional activity space that maximally separated the response vectors 
201	in “lick right” trials and “lick left” trials, we term this vector the “coding direction“ ( cd ). Average spike counts were computed in a 400 ms window in 10 ms steps. For each movement direction 
202	(“lick right” and “lick left”, correct trials only) we computed the average spike counts x̄ lick right and x̄ lick left , n × 1 response vectors that described the population response at that time. 
203	During the sample and delay epochs the direction of the difference in the mean response vectors, w t = x̄ lick right – x̄ lick left , was stable (correlation of w t 's between late sample epoch vs. 
204	late delay epoch, 0.61 ± 0.05; Extended Data Fig. 9b ). We averaged the w t 's from the sample and delay epochs to obtain cd . Because our estimate of the covariance was noisy, the cd gave better 
205	discrimination than the linear discrimant vector ( cd divided by the within-group covariance). The projection along the cd captured 65.6±5.1% of the population selectivity for “lick left” and “lick 
206	right” trials over the sample and delay epochs (root mean square, RMS, of the spike rate difference between “lick right” trials and “lick left” trials), and 36.4±6.3% of the total variance in ALM 
207	task-related activity ( Extended Data Fig. 8a ). Activity variance was quantified as the RMS of the baseline subtracted activity over the sample and delay epoch. To project the ALM population 
208	activity along the cd we used independent control and perturbation trials from the trials used to compute the cd . For each trial we computed the spike counts for each neuron, x ( n × 1), at each 
209	time point. The projected trajectories in Fig. 3 , 5 and Extended Data Figs 6 , 7 , 8 , and 9 were obtained as cd T x . Both correct and incorrect trials were used to compute the proj
[... 360 more lines not kept]
```

**Agent**

Checker passes (38 claims, 0 problems). I've read the paper and all 38 claims; I'm now making the corrections I can support from the text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "#   sample, early delay and late delay conditions (Methods). Bilateral experiment",
 "new_string": "#   sample, early delay and late delay conditions (Methods). Whether this recorded \"late delay\"\n#   ends 0.3 s (Methods naming) or 0 s (Results naming) before the go cue is not fixed by the text;\n#   the author reads the photostimulus times from the dataset's trial metadata. Bilateral experiment"
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "    behavioral effects (middle delay, early delay; p > 0.1, two-tailed t-test)\n  statistics:\n  - test: two-tailed t-test\n    p: 0.1\n    p_relation: \">\"",
 "new_string": "    behavioral effects (middle delay, early delay; p > 0.1, two-tailed t-test)\n  statistics:\n  - test: two-tailed t-test\n    p: 0.1\n    p_relation: \">\"\n    n: 5 mice"
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "neurons; 20 Hz sinusoid, 0.53 mW, 1.3 s delay; Methods). The timing of the three conditions is\n    not given in the text (Extended Data Fig. 5a, b); read from the dataset's trial metadata.",
 "new_string": "neurons; 20 Hz sinusoid, 0.53 mW, 1.3 s delay; Methods; 500 ms photostimulus, Results). When in\n    the trial the three conditions fall is not given in the text (Extended Data Fig. 5a, b); read\n    from the dataset's trial metadata."
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "  criterion: Bilateral experiment, lick right trials, the six 400 ms windows of the legend.\n    In the first 400 ms after photoinhibition, ipsilateral condition, convention R. Reproduced when\n    the population mean rate is not higher than control (paired t-test across neurons, p > 0.05,\n    as a reading; the paper gives no test) and the number of neurons with a significant increase is\n    smaller than the number with a significant decrease.",
 "new_string": "  criterion: Bilateral experiment, photoinhibition 0.8 s at delay onset, lick right trials only\n    (legend; not the pooling of convention R), the six 400 ms windows of the legend. Per neuron,\n    control against photoinhibition by two-tailed t-test, p < 0.01 (legend). Judged in the first\n    400 ms and in 400 to 800 ms after photoinhibition, ipsilateral condition; contralateral and\n    bilateral are reported. Reproduced when, in both windows, the population mean rate is not\n    higher than control (paired t-test across neurons, p > 0.05, as a reading; the paper gives no\n    test) and the number of neurons with a significant increase is smaller than the number with a\n    significant decrease."
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "  criterion: Bilateral experiment behaviour (13 mice), convention P. Left and right hemisphere\n    pooled.",
 "new_string": "  criterion: Bilateral experiment behaviour (13 mice), photoinhibition at delay onset (the early\n    delay condition; sample epoch trials excluded), convention P. Left and right hemisphere\n    pooled."
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "  - about: one spot each side against control\n    test: two-tailed t-test\n    p: 0.001\n    p_relation: \"<\"\n  - about: one spot each side against four spots unilateral\n    test: two-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n  - about: four spots each side against control\n    test: two-tailed t-test\n    p: 0.001\n    p_relation: \"<\"",
 "new_string": "  - about: one spot each side against control\n    test: two-tailed t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 13 mice\n  - about: one spot each side against four spots unilateral\n    test: two-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 13 mice\n  - about: four spots each side against control\n    test: two-tailed t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 13 mice"
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now ed7 (the "less robust" reading), cd-captures-selectivity (broken reference), fig5 no-recovery, and fig6.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "  statement: Bilateral photoinhibition with one spot per side changed selectivity more persistently\n    than unilateral photoinhibition with four spots, and recovery after unilateral photoinhibition\n    was less robust with larger photoinhibition (ipsilateral four spots 490 ms, contralateral 235\n    ms, bilateral no recovery).",
 "new_string": "  statement: Bilateral photoinhibition with one spot per side changed selectivity more persistently\n    than unilateral photoinhibition with four spots; selectivity recovered to 80% of control 490 ms\n    after ipsilateral and 235 ms after contralateral four-spot photoinhibition, and did not recover\n    after bilateral one-spot photoinhibition; recovery after unilateral photoinhibition was less\n    robust with larger photoinhibition (Extended Data Fig. 7e)."
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "after ipsilateral four-spot photoinhibition. Less robust with size is read as the ipsilateral\n    selectivity change at the go cue being larger after four spots (this claim) than after one\n    spot (fig2e-selectivity-recovery-times); the paper gives no test, so the values are reported\n    and the comparison is part of the outcome only by sign.",
 "new_string": "after ipsilateral four-spot photoinhibition. Less robust with size is judged where the Results\n    cite it, Extended Data Fig. 7e: the ipsilateral four-spot ROC at the end of the delay\n    (ed7e-roc-larger-photoinhibition) lower than the ipsilateral one-spot ROC\n    (fig3c-cd-recovery-roc); the paper gives no test, so the comparison is part of the outcome only\n    by sign. The ipsilateral selectivity change at the go cue after four spots against one spot\n    (fig2e-selectivity-recovery-times) is reported as a variant."
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "defined; readings (a) the pre-sample period, (b) the mean over the trial. Modes as in fig3-modes.",
 "new_string": "defined; readings (a) the pre-sample period, (b) the mean over the trial. Modes as in\n    fig3d-persistent-mode and fig3e-ramping-mode."
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "    mean rate after ipsilateral photoinhibition returns to at least 90% of control by the go cue\n    (reading b of fig2-recordings-recovery; reading a as variant).",
 "new_string": "    rate after ipsilateral photoinhibition has recovered by the go cue under reading (a) or (b) of\n    fig2-recordings-recovery."
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "  statement: Modular networks of two coupled modules (attractor, integrator, trained recurrent\n    network) recover after silencing of one module, and drift to a random fixed point when both are\n    silenced.",
 "new_string": "  statement: Modular networks of two coupled modules (attractor, integrator, trained recurrent\n    network) recover after silencing of one module; the modular attractor drifts to a random fixed\n    point when both modules are silenced."
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "    unilateral silencing (0.2 to 1.0 s) and in 30% to 70% after bilateral silencing, and the",
 "new_string": "    unilateral silencing (0.2 to 1.0 s) and in 30% to 70% after bilateral silencing (the 90% and\n    the 30% to 70% are readings of \"restored\" and \"randomly\"; the paper gives no numbers), and the"
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
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
cd claims/000011 && python - <<'EOF'
p='10.1038-nature17643.yaml'
s=open(p).read()
old="""    by sign. The ipsilateral selectivity change at the go cue after four spots against one spot
    (fig2e-selectivity-recovery-times) is reported as a variant.
  depends_on:
  - selective-fraction
"""
assert old not in s
i=s.index("- id: ed7-larger-photoinhibition"); j=s.index("- id: ed7e-roc-larger-photoinhibition")
blk=s[i:j]
blk2=blk.replace("  depends_on:\n  - selective-fraction\n","  depends_on:\n  - selective-fraction\n  - fig2e-selectivity-recovery-times\n  - ed7e-roc-larger-photoinhibition\n  - fig3c-cd-recovery-roc\n")
assert blk2!=blk
s=s[:i]+blk2+s[j:]
open(p,'w').write(s)
EOF
grep -n "depends_on" -A4 10.1038-nature17643.yaml | sed -n '/ed7/,+0p'; tail -5 10.1038-nature17643.yaml
```

```
514-  - ed7e-roc-larger-photoinhibition
    modular attractor ends at the instructed fixed point in more than 90% of trials after
    unilateral silencing (0.2 to 1.0 s) and in 30% to 70% after bilateral silencing (the 90% and
    the 30% to 70% are readings of "restored" and "randomly"; the paper gives no numbers), and the
    modular integrator returns within 10% of its unperturbed trajectory by 2 s after unilateral
    silencing. The FORCE modular network is not specified enough to rebuild and is reported only.
```

**Agent**

Now the checks entry.

**Agent calls Bash**

```bash
cd  && cat >> claims/000011/10.1038-nature17643.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header, convention T. Added that the recorded "late delay" condition of the unilateral experiment ends 0.3 s (Methods naming) or 0 s (Results naming) before the go cue, which the text does not settle; the author reads the times from the trial metadata.
  - fig1d-earlier-photoinhibition-minimal. Added n (5 mice) to the statistics, from the same paragraph and the Extended Data Fig. 3b legend.
  - ed5-photoactivation-recovery. The criterion said the timing was not given; the Results give a 500 ms photostimulus. Added it; only its placement in the trial stays open.
  - ed2e-no-rebound. The criterion applied convention R, which pools lick left and lick right trials, while the legend uses lick right trials with a two-tailed t-test at p < 0.01. Now follows the legend. It judged only the first 400 ms after offset; the legend has two post-offset windows, both now used.
  - fig2b-unilateral-performance. Restricted to photoinhibition at delay onset, as the statement and the Results say ("during the early delay epoch"); the experiment also has a sample epoch condition.
  - fig2b-bilateral-performance. Added n (13 mice) to the statistics, from the Results.
  - ed7-larger-photoinhibition. The statement put the 490 ms and 235 ms recovery times as evidence of "less robust" recovery, which the Results cite to Extended Data Fig. 7e (ROC), and 490 ms is faster than the one-spot 538 ms. Separated them, and the criterion now judges "less robust" by the ROC comparison of Extended Data Fig. 7e with the one-spot ROC; the selectivity-change comparison, which the paper does not cite, is a variant. Added the claims it uses to depends_on.
  - cd-captures-selectivity. The criterion referred to a claim fig3-modes that does not exist; now points at fig3d-persistent-mode and fig3e-ramping-mode.
  - fig5-callosotomy-no-recovery. Spike rate recovery used only reading (b) of fig2-recordings-recovery, with (a) as a variant, though the two are readings of the same sentence; now either reading, as there.
  - fig6-modular-models-recover. The statement gave random drift after bilateral silencing for all modular models; the paper says it of the attractor model only. Marked the 90% and 30% to 70% thresholds as readings.
  - Open. ed7e-roc-larger-photoinhibition, the legend prints the bilateral s.e.m. as 0.8; the tolerance 0.08 assumes a dropped zero, which the text cannot confirm (the 10% default would be 0.054).
  - Open. The Corrigendum (doi:10.1038/nature18623) was not in the text supplied; whether it changes any value is not known.
  - Open. ED5 names the photoactivation conditions "late delay" (Extended Data Fig. 5c) and "middle delay" (Extended Data Fig. 5f); whether they are the same condition is not stated.
EOF
python tools/claims_check.py claims/000011/10.1038-nature17643.yaml paper/10.1038-nature17643.txt | tail -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/cite it, Extended Data Fig. 7e: the ipsilateral/cite it, Extended Data Fig. 7e, by the ipsilateral/' claims/000011/10.1038-nature17643.yaml && grep -n ': ' claims/000011/10.1038-nature17643.yaml | grep -vE '^[0-9]+:\s*(- )?[a-z_]+: ' | grep -v '^[0-9]*:#' | head; python tools/claims_check.py claims/000011/10.1038-nature17643.yaml paper/10.1038-nature17643.txt | tail -3
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file for DANDI:000011 against the paper. After my edits the file is fit for an attempt, and I marked it `ready: true`.

**Checker result** (after edits): `claims/000011/10.1038-nature17643.yaml: 38 claims, 38 quotes, 11 statistical values, 0 problems`

**Changes, by claim**
- **Opening comment (convention T):** the paper doesn't say whether the recorded "late delay" condition in the unilateral experiment ends 0.3 s before the go cue (as the Methods name it) or 0 s before (as the Results name it). I noted this; the author reads the actual times from the trial metadata.
- **fig1d-earlier-photoinhibition-minimal:** added `n: 5 mice` to the statistics.
- **ed5-photoactivation-recovery:** the criterion said the timing was not given, but the Results give a 500 ms photostimulus. I added it; only where it falls in the trial stays open.
- **ed2e-no-rebound:** the criterion pooled lick left and lick right trials. The legend uses lick right trials only, with a two-tailed t-test at p < 0.01, so the criterion now follows the legend. It also now judges both windows after photoinhibition offset, not just the first 400 ms.
- **fig2b-unilateral-performance:** limited to photoinhibition at delay onset, which is what the statement and the Results describe.
- **fig2b-bilateral-performance:** added `n: 13 mice` to the three tests.
- **ed7-larger-photoinhibition:** the statement offered the 490 and 235 ms recovery times as evidence that recovery was "less robust". The Results cite Extended Data Fig. 7e (ROC values) for that, and 490 ms is actually faster than the one-spot 538 ms. I separated the two parts. The criterion now judges "less robust" by the four-spot ROC against the one-spot ROC; the earlier comparison is kept as a variant, and I extended `depends_on` to match.
- **cd-captures-selectivity:** the criterion pointed to a claim `fig3-modes` that doesn't exist. It now points to fig3d-persistent-mode and fig3e-ramping-mode.
- **fig5-callosotomy-no-recovery:** spike-rate recovery now accepts either reading (a) or (b) of fig2-recordings-recovery, as that claim does. Before, it used only (b).
- **fig6-modular-models-recover:** the paper says only the attractor model drifts randomly when both modules are silenced, and the statement now says the same. The 90% and 30% to 70% thresholds are now marked as readings, since the paper gives no numbers.

**Still open** (recorded under `checks`)
- **ed7e-roc-larger-photoinhibition:** the legend prints the bilateral s.e.m. as 0.8, which can't be right for an ROC value. The tolerance of 0.08 assumes a dropped zero, which the text can't confirm; the 10% default would be 0.054.
- **Corrigendum:** the published correction (doi:10.1038/nature18623) was not in the supplied text, so it's unknown whether it changes any value.
- **Photoactivation condition names:** Extended Data Fig. 5c says "late delay" and Fig. 5f says "middle delay". The paper doesn't say whether they are the same condition.

Each of the paper's main findings has a claim, and every claim comes from this paper. Nothing was committed or pushed.

## End of run

29 turns, 3 minutes, result: success.
