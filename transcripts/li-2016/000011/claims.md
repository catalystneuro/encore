# 000011 · claims · run 39598323426

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/## Reader/,/^## [A-Z]/p'; ls claims/001453/ paper/ claims/000011 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 25,200p claims/001453/*.yaml
```

```
# pmc.ncbi.nlm.nih.gov).
schema_version: 2
dataset:
  archive: dandi
  id: "001453"
paper: doi:10.1016/j.cub.2025.04.027
claims:
- id: stimulus-code-link
  kind: link
  statement: The dandiset's stimulus codes can be linked to the stimuli the paper names, using
    the paper's analysis code and the protocol file of its stimulus software, and the values
    computed through that link agree with those the paper's code printed.
  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29
  data: with_labels
  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when
    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
[... 156 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; head -20 paper/*.txt; ls docs tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature17643.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk 'NR>=7 && NR<=40' 10.1038-nature17643.txt | fold -s -w 4000
```

```
<persisted-output>
Output too large (88.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/2dabb3e8-a5a2-4e00-a33f-82929930133e/tool-results/bk98m3ewm.txt

Preview (first 2KB):
Nature Nature 544 hhmipa Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title Howard Hughes Medical Institute Author Manuscripts PMC5081260 PMC5081260.1 5081260 5081260 NIHMS767125 27074502 10.1038/nature17643 NIHMS767125 HHMIPA767125 1 Article Robust neuronal dynamics in premotor cortex during motor planning Li Nuo * Daie Kayvon * Svoboda Karel # Druckmann Shaul # Janelia Research Campus, HHMI, Ashburn VA 20147 * co-first author # corresponding author Karel Svoboda, Janelia Research Campus, HHMI, 19700 Helix Drive, Ashburn, VA 20147, [removed: an e-mail address] ., Shaul Druckmann, Janelia Research Campus, HHMI, 19700 Helix Drive, Ashburn, VA 20147, [removed: an e-mail address] . 13 4 2016 28 4 2016 532 7600 278020 459 464 13 03 2016 27 10 2016 27 10 2016 05 08 2025 Reprints and permissions information is available at www.nature.com/reprints . Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use: http://www.nature.com/authors/editorial_policies/license.html#terms Corrigendum: Robust neuronal dynamics in premotor cortex during motor planning. 537 7618 29 6 2016 122 122 Nature 10.1038/nature18623 27362233 Neuroscience: Fault tolerance in the brain. 532 7600 13 4 2016 449 450 Nature 10.1038/nature17886 27074510 Neural activity maintains representations that bridge past and future events, often over many seconds. Network models can produce persistent and ramping activity, but the positive feedback that is critical for these slow dynamics can cause sensitivity to perturbations. Here we use electrophysiology and optogenetic perturbations in mouse premotor cortex to probe robustness of pers
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/10.1038-nature17643.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

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

**Agent calls Bash**

```bash
grep -oE '^ *-? ?[a-z_]+:' claims/*/*.yaml | sed 's/.*://' | sort | uniq -c | sort -rn | head -40; ls docs; sed -n 1,60p tools/claims_check.py
```

```
33294 
agents
archives.md
conversion-tracker.md
design.md
fixing-conversions.md
pilot-notes.md
pipeline.md
protocol.md
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1))" | head -250
```

```
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
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn -i -B3 -A12 "simulat\|model network" claims/*/*.yaml | grep -E "data:|criterion|id:" | head -20; ls claims | head -50
```

```
claims/000009/10.1038-nature22324.yaml:649:  criterion: A simulation, not a test on recorded data; its parameters are in the Supplementary
claims/000009/10.1038-nature22324.yaml-652-- id: fig5-weak-photoinhibition-rates
claims/000070/10.1038-nature11129.yaml-274-- id: fig6-velocity-model
claims/000070/10.1038-nature11129.yaml:285:  criterion: One simulated dataset per array dataset from that session's condition-mean hand
claims/000070/10.1038-nature11129.yaml-290-- id: fig6-complex-kinematic-model
claims/000070/10.1038-nature11129.yaml-298-  criterion: As for fig6-velocity-model, with the complex kinematic model.
claims/000070/10.1038-nature11129.yaml-299-- id: fig1-leech-and-walking
claims/000070/10.1038-nature11129.yaml-329-- id: fig5-generator-model
claims/000070/10.1038-nature11129.yaml-337-- id: fig6cd-speed-independent-frequency
claims/000947/10.1371-journal.pbio.3000829.yaml:499:- id: fig6-simulation
claims/000947/10.1371-journal.pbio.3000829.yaml-507-  data: elsewhere
claims/001710/10.1101-2023.11.20.567978.yaml:538:  criterion: A simulation, not a test on recorded data. The Methods give M=N=1000, input
claims/001710/10.1101-2023.11.20.567978.yaml-545-- id: fig3d-model-wider-fields-with-plasticity
claims/001710/10.1101-2023.11.20.567978.yaml:550:  criterion: A simulation, as fig3bc-model-stable-place-cells. The paper does not say how a
claims/001710/10.1101-2023.11.20.567978.yaml-553-- id: fig3e-model-more-fields-without-plasticity
claims/001710/10.1101-2023.11.20.567978.yaml:560:  criterion: A simulation, as fig3bc-model-stable-place-cells; the definition of a model place
claims/001710/10.1101-2023.11.20.567978.yaml-562-- id: fig3f-narrower-fields-cre-familiar
claims/001746/10.1038-s41556-026-02009-4.yaml-519-- id: ext9cd-ven-subtypes-ap
claims/001750/10.1038-s41556-026-02009-4.yaml-189-  data: elsewhere
claims/001750/10.1038-s41556-026-02009-4.yaml:192:  criterion: Simulations of the PC model as in the Methods (Computational model) with
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p claims/000009/10.1038-nature22324.yaml; sed -n 635,660p claims/000009/10.1038-nature22324.yaml
```

```
# Claims for Guo, Inagaki, Daie, Druckmann, Gerfen & Svoboda (2017) on dandiset 000009.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20, protocol
# as stated in docs/protocol.md (pilot-10), Reader steps 1 to 4.
#
# Text read: the HHMI author manuscript in PubMed Central (PMC6431254, NIHMS865428), as served by
# Europe PMC (paper/10.1038-nature22324.txt): main text, Methods, the legends of Figures 1 to 6 and
# of Extended Data Figures 1 to 10. It is the accepted manuscript, not the version of record. No PDF
# was supplied, so no figure could be read. Not in the text: the Supplementary Information
# (supp_info: further whole-cell methods, the model of the latency T3 and the network models of
# Extended Data Fig. 7c-e, lick-early, no-response and lick-latency rates under photoinhibition) and
# Supplementary Tables 1 and 2 (animals, coordinates, photostimulus powers, viruses). The claims
# latency-model-t3 and network-models rest on the Supplementary Information and are written from
# the main text and Extended Data legends only; no other claim needs it. The claims
# selectivity-time-course and alm-gabaergic-no-thalamic-projection were added by the check of
# 2026-10-20.
#
# Code read: none. The paper links no analysis code. It names the data deposit "CRCNS.ORG in the NWB
# format (https://doi.org/10.6080/K03F4MH2)". The dandiset's archive title is the paper's title, and
# its description (the abstract) says it holds spikes from ALM and thalamus during the task with
# photoinhibition; its metadata list Units, BehavioralTimeSeries, CurrentClampStimulusSeries and
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A16 "id: network-models" claims/000009/10.1038-nature22324.yaml; sed -n 40,70p claims/000009/10.1038-nature22324.yaml; tail -30 claims/000009/10.1038-nature22324.yaml
```

```
713:- id: network-models
714-  statement: The data are inconsistent with linear network models with specific or non-specific
715-    thalamocortical connectivity, but do not exclude non-linear models of either kind.
716-  source: Results, Thalamus contributes to selectivity in ALM, paragraph 2; Extended Data Figure 7c-e;
717-    Supplementary information
718-  quote: Our data are inconsistent with linear models with either specific (like-to-like) or
719-    non-specific (all-to-all) thalamocortical connectivity. However, our data do not exclude non-linear
720-    models
721-  criterion: A modelling result; its equations and parameters are in the Supplementary information,
722-    which is not in the text read. Cannot be specified from the text; recorded so the finding is
723-    covered.
724-- id: fig6c-vmval-reduced
725-  statement: ALM photoinhibition decreased the activity of VM/VAL neurons to 25% of control, inhibiting
726-    190 of 201 neurons (139 significantly) and significantly activating none.
727-  source: Results, ALM drives thalamic preparatory activity, paragraph 1; Figure 6c
728-  quote: ALM photoinhibition decreased activity in a majority of VM/VAL neurons (to 25% of control;
729-    190/201 inhibited, 11/201 activated, 139/201 significantly inhibited, 0/201 significantly
# spike width into putative fast-spiking (< 0.4 ms, 166), putative pyramidal (> 0.6 ms, 1006) and
# unclassified (42); thalamus 790 units in 73 sessions (11 mice), putative thalamic neurons with
# width > 0.5 ms (672), VM/VAL units within 0.4 mm of the VM/VAL centre (313 of 790; 295 in the
[... 58 more lines not kept]
```

**Agent**

I've read the whole text: the author manuscript with Methods and Extended Data legends. The paper links no code. Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "content": "# Claims for Li, Daie, Svoboda & Druckmann (2016) on dandiset 000011.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, protocol\n# as stated in docs/protocol.md, Reader steps 1 to 4.\n#\n# Text read: the HHMI author manuscript in PubMed Central (PMC5081260, NIHMS767125), as served by\n# Europe PMC (paper/10.1038-nature17643.txt): main text, Methods, the legends of Figures 1 to 6 and\n# of Extended Data Figures 1 to 10. It is the accepted manuscript, not the version of record. The\n# paper has no Supplementary Information beyond the Extended Data (the record says no supplement).\n# No PDF was supplied, so no figure could be read; values shown only in figures are not claimed.\n# Not read: the Corrigendum (Nature 537, 122; doi:10.1038/nature18623), which the record lists and\n# the text does not include. Whether it changes any value below is not known.\n#\n# Code read: none. The paper links no analysis or model code. It names the data deposit \"Data have\n# been deposited at https://crcns.org/ and can be accessed at http://doi:10.6080/K0RB72JW\". The\n# dandiset is listed for this paper; which of the experiments below it holds is for the author to\n# find. The dataset's files were not looked at.\n#\n# The data the paper used, as it reports them (Methods). 33 mice, male and female, older than P60.\n# Photoinhibition behaviour, 10 VGAT-ChR2-EYFP and 9 PV-ires-cre x Rosa26-LSL-ReaChR mice; of these,\n# 5 VGAT and 7 PV x ReaChR mice also had electrophysiology during behaviour. Callosotomy, 7 mice (6\n# VGAT, 1 PV x ReaChR); cut on the left (3) or right (4). Photoactivation, 2 Tlx_PL56-cre x Ai32\n# mice. Photoinhibition characterisation, 4 untrained mice (2 VGAT, 2 PV x ReaChR). Anatomy, 1\n# Tlx_PL56-cre mouse. Task: a pole at one of two positions 4.29 mm apart (posterior, lick right;\n# anterior, lick left); sample epoch 1.3 s from pole movement onset to 0.1 s after retraction\n# onset; delay epoch 1.3 s (unilateral experiment, Fig. 1), 1.7 s (bilateral experiment, Fig. 2),\n# or 1.2 to 1.7 s in 0.1 s steps (Extended Data Fig. 3c, d); go cue 3.4 kHz, 0.1 s; lick early\n# trials punished; no lick within 1.5 s of the go cue is rare. Photoinhibition on 25% of trials in\n# behaviour and 40% during electrophysiology; photoactivation on 40%. Recordings from left ALM with\n# 32-channel NeuroNexus probes (A4x8), 19531.25 Hz after demultiplexing, band-pass 300 Hz to 6 kHz,\n# manual spike sorting. 1012 single units in 58 sessions (20 unilateral, Fig. 1; 38 bilateral,\n# Fig. 2 and Extended Data Fig. 7) from 12 mice; callosotomy recordings 7 mice. Measured variables:\n# spike times and waveforms per unit, trial type (pole position), licks and outcome (correct,\n# incorrect, lick early), photostimulus condition and timing, delay duration.\n#\n# Conventions used by the criteria below (from the Methods and legends unless marked open).\n# T (photoinhibition timing). Unilateral experiment (Fig. 1): 0.5 s including a 100 ms ramp down,\n#   ending 1.6 s (sample), 0.8 s (early delay), 0.3 s (late delay) or 0 s (before cue) before the\n#   go cue (Methods). The Results name the conditions differently; the 0 s condition is called\n#   \"late delay\" and the 0.3 s one \"middle delay\". Electrophysiology in this experiment used the\n#   sample, early delay and late delay conditions (Methods). Bilateral experiment (Fig. 2): 0.8 s\n#   including a 200 ms ramp, from the start of the sample or of the delay epoch; recordings used the\n#   delay start (Extended Data Fig. 2e). Photoinhibition offset is the end of the ramp (Extended\n#   Data Fig. 3b, \"the end of ramp offset\"). The callosotomy experiment's delay duration and\n#   photostimulus are not given; the Fig. 5a legend says \"early delay epochs\". Open, with readings\n#   (C1) as the bilateral experiment, 1.7 s delay, 0.8 s from delay onset; (C2) as recorded in the\n#   dataset's trial metadata, which the author reads.\n# U (units). Trough-to-peak spike width < 0.35 ms, fast-spiking; > 0.45 ms, putative pyramidal;\n#   between, excluded. Analyses use putative pyramidal neurons.\n# S (selective). Spike counts in the sample, delay or response epoch differ between lick left and\n#   lick right trials, two-tailed t-test, p < 0.05; selective in any epoch. The response epoch\n#   length is not given; open, readings (R1) 1.3 s after the go cue, (R2) 1.5 s, the response\n#   window. Which outcomes enter is open; readings (O1) correct trials only, as for the cd, (O2)\n#   correct and incorrect trials grouped by instructed movement. Student's or Welch's t-test is not\n#   stated; open, readings (a) Student's, (b) Welch's.\n# D (selectivity and its recovery). Preferred trial type from 10 trials; selectivity is the spike\n#   rate difference preferred minus non-preferred on the remaining trials; all trials (correct and\n#   incorrect), grouped by instructed movement, when photoinhibition effects are quantified.\n#   Which 10 trials (random, or the first) and from which condition are not given; standard choice,\n#   10 random control trials, repeated across the bootstrap. Selectivity change is photoinhibition\n#   minus control selectivity. Recovery time is the first time bin after photoinhibition offset at\n#   which photoinhibition selectivity reaches 80% of control selectivity, mean and s.e.m. by\n#   bootstrap over neurons. The bin for the selectivity time course is not given; open, readings\n#   (B1) 200 ms (the PSTH window of Fig. 1e), (B2) 400 ms (the rate test window), both in 50 ms\n#   steps. Whether 80% is of the time-matched control selectivity is not stated; reading, the\n#   time-matched control, as the change is plotted against control in time. Neurons included,\n#   selective (S) and tested on more than 3 trials in every condition (Fig. 1g legend).\n# R (rate change). Two-tailed t-test on spike counts in 400 ms windows, control against\n#   photoinhibition, lick left and lick right trials pooled, tested in 50 ms steps, significant at\n#   p < 0.01. Whether a window is labelled by its start, centre or end is not given; readings (W1)\n#   end, (W2) centre. Neurons with mean rate below 1 spike/s or fewer than 3 trials are excluded in\n#   Extended Data Figs 5e and 7c; applied here to Figs 1f, 2d and 5d as a reading (the Fig. 1f, 2d\n#   and 5d legends do not say), with (X2) no exclusion as the other reading.\n# P (performance). Fraction correct, lick early trials excluded; photoinhibition against control by\n#   two-tailed t-test, per mouse values (figure symbols are mice). Paired or unpaired is not said;\n#   readings (P1) paired over mice, (P2) unpaired over mice.\n# A (activity space, Methods). Sessions of the bilateral experiment with > 5 neurons recorded\n#   simultaneously for > 5 trials per condition (16 of 38 sessions). Spike counts in 400 ms windows,\n#   10 ms steps. w_t is the lick right minus lick left mean response vector, correct control trials;\n#   cd is the average of w_t over the sample and delay epochs. The cd, the offsets and the decision\n#   boundary use a subset of control trials; projections use the other control trials and the\n#   perturbation trials. The size of the subset is not given; open, readings (H1) a random half of\n#   correct control trials, (H2) a random third. Projections use correct and incorrect trials,\n#   grouped by instructed movement. ROC is the area under the ROC curve of cd'x between lick right\n#   and lick left trials in the last 400 ms of the delay epoch, per session, mean and s.e.m. over\n#   sessions. Decision boundary as the Methods give it, the inverse-variance weighted mean of the\n#   two class means, from the last 400 ms before the go cue. Whether cd is normalised to unit\n#   length is not stated; it does not change ROC or the side of the boundary, and unit length is\n#   used as a standard choice.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000011\"\npaper: doi:10.1038/nature17643\nclaims:\n- id: unit-classification\n  statement: 1012 single units were recorded in left ALM during behaviour in 58 sessions (20\n    unilateral, 38 bilateral experiment sessions); by spike width 72 were fast-spiking, 890 putative\n    pyramidal, and 50 intermediate and excluded.\n  source: Methods, Electrophysiology data analysis, paragraph 1\n  quote: 1012 single units were recorded during behavior across 58 recording sessions (20 sessions of\n    unilateral experiments, Fig. 1 ; 38 sessions of bilateral experiments ... Units with spike width <\n    0.35 ms were defined as fast-spiking (FS) neurons (72/1012) and units with spike widths > 0.45 ms\n    as putative pyramidal neurons (890/1012). Units with intermediate values (0.35 - 0.45 ms, 50/1012)\n    were excluded\n  expected:\n  - quantity: single units\n    value: 1012\n    tolerance: 101.2\n  - quantity: recording sessions\n    value: 58\n    tolerance: 5.8\n  - quantity: fast-spiking units\n    value: 72\n    tolerance: 7.2\n  - quantity: putative pyramidal units\n    value: 890\n    tolerance: 89\n  - quantity: intermediate units\n    value: 50\n    tolerance: 5\n  criterion: Width is the trough-to-peak interval of the mean waveform (Methods). Units and\n    sessions of the control mice only; the Results give 12 mice for these 1012 units, so\n    callosotomy and photoactivation recordings are counted apart. Reproduced when all values are\n    within tolerance.\n- id: selective-fraction\n  statement: Most putative pyramidal neurons distinguished trial types (634 of 890); 176 in the\n    sample epoch, 337 in the delay epoch and 493 in the response epoch.\n  source: Results, Preparatory activity in ALM, paragraph 1; Extended Data Figure 1\n  quote: Most ALM pyramidal neurons distinguished trial types (634/890, p<0.05, t-test; sample epoch,\n    176/890; delay epoch, 337/890; response epoch, 493/890, Methods)\n  expected:\n  - quantity: selective putative pyramidal neurons, any epoch\n    value: 634\n    tolerance: 63.4\n  - quantity: selective in the sample epoch\n    value: 176\n    tolerance: 17.6\n  - quantity: selective in the delay epoch\n    value: 337\n    tolerance: 33.7\n  - quantity: selective in the response epoch\n    value: 493\n    tolerance: 49.3\n  depends_on:\n  - unit-classification\n  criterion: Convention S on the putative pyramidal neurons of unit-classification, control trials.\n    Reproduced when all four counts are within tolerance under one combination of readings (R1 or\n    R2, O1 or O2, a or b).\n- id: fig1d-late-delay-ipsilateral-bias\n  statement: Unilateral photoinhibition of ALM (0.5 s) ending at the go cue caused an ipsilateral\n    response bias.\n  source: Results, Preparatory activity after unilateral silencing, paragraph 1; Figure 1d\n  quote: Transient (duration, 0.5 s) unilateral photoinhibition of ALM up to the ‘go’ cue (late\n    delay) caused an ipsilateral response bias (n = 5 mice, p < 0.01, two-tailed t-test; Fig. 1d )\n  statistics:\n  - test: two-tailed t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 5 mice\n  criterion: Behaviour of the unilateral experiment (convention T, the condition ending 0 s before\n    the go cue). An ipsilateral bias lowers performance on trials whose instructed lick is\n    contralateral to the photoinhibited hemisphere (lick right for left ALM). The measure tested is\n    not stated; readings (M1) performance on contralateral trials, (M2) overall performance (Fig.\n    1d plots \"behavioral performance\"). Per mouse, photoinhibition against control (convention P,\n    readings P1 and P2), left and right hemisphere pooled per mouse. Reproduced when performance on\n    photoinhibition trials is lower with p < 0.01 under a reading, and contralateral trial\n    performance falls more than ipsilateral trial performance.\n- id: fig1d-earlier-photoinhibition-minimal\n  statement: Unilateral photoinhibition ending at least 0.3 s before the go cue had minimal\n    behavioural effects.\n  source: Results, Preparatory activity after unilateral silencing, paragraph 1; Figure 1d;\n    Extended Data Figure 3b\n  quote: In contrast, photoinhibition ending at least 0.3 s prior to the ‘go’ cue produced minimal\n    behavioral effects (middle delay, early delay; p > 0.1, two-tailed t-test)\n  statistics:\n  - test: two-tailed t-test\n    p: 0.1\n    p_relation: \">\"\n  criterion: A claim of absence, judged on the paper's test, a two-tailed t-test of performance on\n    photoinhibition against control trials over the 5 mice (convention P, readings P1 and P2), for\n    the conditions ending 0.8 s and 0.3 s before the go cue. Reproduced when p > 0.1 for both;\n    not reproduced when either has p < 0.1. The change in performance is reported either way. The\n    paper's naming of the conditions differs between Results and Methods (convention T); the\n    sample condition (1.6 s) is reported as a variant.\n- id: ed3-behaviour-recovery-interval\n  statement: Performance was not significantly affected when photoinhibition (0.5 s or 1.3 s) ended\n    more than 0.3 s before the go cue, and 0.5 s photoinhibition just before the go cue had an\n    effect similar to photoinhibition over the whole delay epoch.\n  source: Extended Data Figure 3b, d, e\n  quote: Performance was not significantly affected for T recovery > 0.3s\n  criterion: A claim of absence, judged on the paper's test, the two-tailed t-test of Extended Data\n    Fig. 3b, d against control (convention P), over mice (n = 5 for 3b; not given for 3d). Data of\n    Extended Data Fig. 3c, d have a delay of 1.2 to 1.7 s and 1.3 s photoinhibition. Reproduced when\n    no condition with T recovery above 0.3 s has p < 0.05 in either experiment, and at T recovery 0\n    the performance under 0.5 s and 1.3 s photoinhibition differ by less than the larger of their\n    s.e.m. over mice; not reproduced otherwise. The second half has no test in the paper; it is a\n    reading of \"similar\", and its numbers are shown.\n- id: ed4-return-to-trajectory\n  statement: Neurons whose spike rates decreased during the delay epoch also recovered after\n    unilateral photoinhibition, returning to the time-matched control trajectory and not decaying\n    to the end-point rate.\n  source: Extended Data Figure 4b, c; Results, Preparatory activity after unilateral silencing,\n    paragraph 2\n  quote: Spike rate difference relative to time-matched control show significantly smaller\n    root-mean-squared error (RMS) than spike rate difference relative to end point (p<0.001, paired\n    t-test)\n  statistics:\n  - test: paired t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 27 neurons from 6 mice\n  expected:\n    quantity: neurons with a significant delay-epoch decrease\n    value: 27\n    tolerance: 2.7\n  criterion: Unilateral experiment recordings. Neurons with a significant spike rate decrease at the\n    end against the beginning of the delay epoch (two-tailed t-test, p < 0.05, 400 ms windows,\n    trial types pooled; Extended Data Fig. 4b). Rate normalised to the neuron's mean rate. For\n    each perturbed condition the RMS, between photoinhibition offset and the go cue, of the\n    perturbed minus time-matched control rate, and of the perturbed rate minus the control rate at\n    the end of the delay. Which photoinhibition conditions are pooled and whether trial types are\n    taken apart (the legend plots preferred and non-preferred) are not given; readings (a) one\n    value per neuron averaged over conditions and trial types, (b) one per neuron, condition and\n    trial type. Reproduced when the time-matched RMS is smaller by a paired t-test with p < 0.001\n    under a reading.\n- id: fig1f-spike-rate-recovery\n  statement: Within 400 ms after unilateral photoinhibition, spike rates became indistinguishable\n    from control in 90% of neurons; 10% retained a sustained change.\n  source: Results, Preparatory activity after unilateral silencing, paragraph 2; Figure 1f\n  quote: Within 400 ms after photoinhibition, spike rates became indistinguishable from the\n    unperturbed condition in 90% of the neurons; only 10% of neurons retained a sustained change in\n    spike rate\n  expected:\n    quantity: fraction of neurons with a significant rate change 400 ms after offset\n    value: 0.1\n    tolerance: 0.01\n  criterion: Convention R on putative pyramidal neurons of the unilateral experiment, per condition\n    (Fig. 1f gives n = 168, 168, 175 neurons). The fraction of neurons with a significant change in\n    the 400 ms window at 400 ms after photoinhibition offset (convention T). Open which conditions\n    the 10% describes; readings (a) each of the sample, early delay and late delay conditions, (b)\n    the three pooled. Reproduced when the fraction is within tolerance under one combination of\n    readings (a or b, W1 or W2, with or without exclusion). The tolerance, 10% of the value, is one\n    percentage point; the counts 168, 168 and 175 are reported against the paper.\n- id: fig1g-selectivity-recovery\n  statement: After unilateral photoinhibition ALM neurons recovered more than 80% of their control\n    selectivity within about 0.5 s; recovery times were 373 ms (sample), 510 ms (early delay) and 327\n    ms (late delay).\n  source: Results, Preparatory activity after unilateral silencing, paragraph 2; Figure 1g legend\n  quote: Green lines, recovery to 80% of control (mean ± s.e.m. bootstrap). Sample, 373±260 ms; early\n    delay, 510±218 ms; late delay, 327±112 ms\n  expected:\n  - quantity: recovery time to 80% of control selectivity, sample\n    value: 373\n    tolerance: 260\n    unit: ms\n  - quantity: recovery time, early delay\n    value: 510\n    tolerance: 218\n    unit: ms\n  - quantity: recovery time, late delay\n    value: 327\n    tolerance: 112\n    unit: ms\n  - quantity: selective neurons tested on more than 3 trials in all conditions\n    value: 55\n    tolerance: 5.5\n  depends_on:\n  - selective-fraction\n  criterion: Convention D on the unilateral experiment. Tolerances are the paper's bootstrap s.e.m.\n    The Results give 514 ms as the bound, the legend 510 ms for early delay; the legend values are\n    used. Reproduced when all three times are within tolerance under one bin reading (B1, B2);\n    partially reproduced for two of three.\n- id: ed5-photoactivation-recovery\n  statement: After transient photoactivation of layer 5 intratelencephalic neurons, ALM selectivity\n    recovered on a time course similar to recovery after photoinhibition.\n  source: Results, Preparatory activity after unilateral silencing, paragraph 2; Extended Data\n    Figure 5f\n  quote: Sample epoch: 249 ± 68 ms to recover to 80 % of control selectivity; early delay: 275 ± 168\n    ms; middle delay: 250 ± 218 ms\n  expected:\n  - quantity: recovery time, sample\n    value: 249\n    tolerance: 68\n    unit: ms\n  - quantity: recovery time, early delay\n    value: 275\n    tolerance: 168\n    unit: ms\n  - quantity: recovery time, middle delay\n    value: 250\n    tolerance: 218\n    unit: ms\n  - quantity: selective neurons tested on more than 3 trials in all conditions\n    value: 26\n    tolerance: 2.6\n  criterion: Convention D on the photoactivation recordings (2 Tlx_PL56-cre x Ai32 mice, 69\n    neurons; 20 Hz sinusoid, 0.53 mW, 1.3 s delay; Methods). The timing of the three conditions is\n    not given in the text (Extended Data Fig. 5a, b); read from the dataset's trial metadata.\n    Reproduced when all three times are within tolerance under one bin reading.\n- id: ed5-photoactivation-rate-changes\n  statement: Photoactivation during the sample epoch excited 19% and suppressed 22% of neurons;\n    during the late delay epoch it excited 15% and suppressed 17%.\n  source: Extended Data Figure 5c\n  quote: 'Photoactivation during sample epoch: 19% excited, 22% suppressed; late delay epoch: 15%\n    excited, 17% suppressed'\n  expected:\n  - quantity: excited, sample\n    value: 0.19\n    tolerance: 0.019\n  - quantity: suppressed, sample\n    value: 0.22\n    tolerance: 0.022\n  - quantity: excited, late delay\n    value: 0.15\n    tolerance: 0.015\n  - quantity: suppressed, late delay\n    value: 0.17\n    tolerance: 0.017\n  criterion: Convention R during photoactivation (the 400 ms window ending at photostimulus offset,\n    or the window covering the photostimulus, as readings), trial types pooled; denominators 43 and\n    44 neurons (Extended Data Fig. 5e). Excited or suppressed by the sign of the change. Reproduced\n    when all four are within tolerance under a reading; partially when two or three are.\n- id: ed2b-silencing-strength\n  statement: Ipsilateral and bilateral photoinhibition reduced the activity of putative pyramidal\n    neurons by more than 90%, similarly in VGAT-ChR2-EYFP and PV x ReaChR mice; contralateral\n    photoinhibition had little effect on the average rate.\n  source: Extended Data Figure 2b; Methods, Photoinhibition\n  quote: Ipsilateral and bilateral photoinhibition similarly silenced neuronal activity. Average\n    spike rate across the population was little affected by contralateral photoinhibition\n  criterion: Per neuron (mean rate at least 1 spike/s), the rate during photoinhibition over the\n    control rate in the same window. The window is not given; readings (a) the whole photostimulus\n    before the ramp, (b) the last 400 ms of photoinhibition (Extended Data Fig. 2e). Reproduced\n    when the mean normalised rate is below 0.1 for ipsilateral photoinhibition in both mouse lines\n    (experiment 2) and for bilateral photoinhibition, and contralateral photoinhibition leaves it\n    above 0.8. The 0.8 is a reading of \"little affected\"; the value is reported. Neuron counts per\n    experiment and condition (117, 110, 109; 300, 294, 301; 52, 52, 102) are reported against the\n    legend.\n- id: ed2d-spatial-extent\n  statement: Photoinhibition with one laser spot silenced activity in a cortical area of 1 mm radius\n    at half-maximum, through all layers.\n  source: Methods, Photoinhibition; Extended Data Figure 2d\n  quote: The photoinhibition silenced 90% of spikes ( Extended Data Fig. 2b ) in a cortical area of\n    1mm radius (at half-max) through all cortical layers\n  expected:\n    quantity: radius at half-maximal silencing\n    value: 1\n    tolerance: 0.1\n    unit: mm\n  criterion: Recordings in 4 untrained awake mice (246 neurons), neurons pooled across depth;\n    normalised rate against distance from the laser centre. The fit or interpolation used for\n    half-max is not given; readings (a) linear interpolation of the binned mean, (b) a Gaussian fit.\n    Reproduced when the half-max radius is within tolerance under a reading. Whether the dataset\n    holds these recordings is for the author to find.\n- id: ed2e-no-rebound\n  statement: No rebound excitation was detected on average after photoinhibition offset; a small\n    fraction of neurons showed rebound, balanced by weak sustained inhibition in a larger fraction.\n  source: Extended Data Figure 2e\n  quote: No rebound excitation was detected after photoinhibition offset on average ( d ). A small\n    proportion of neurons showed rebound excitation which was balanced by a low level of sustained\n    inhibition in a larger proportion of neurons\n  criterion: Bilateral experiment, lick right trials, the six 400 ms windows of the legend.\n    In the first 400 ms after photoinhibition, ipsilateral condition, convention R. Reproduced when\n    the population mean rate is not higher than control (paired t-test across neurons, p > 0.05,\n    as a reading; the paper gives no test) and the number of neurons with a significant increase is\n    smaller than the number with a significant decrease.\n- id: fig2b-unilateral-performance\n  statement: Unilateral photoinhibition in the early delay epoch only slightly reduced performance\n    (one spot 70.3%, four spots 67.7%).\n  source: Results, Preparatory activity after bilateral silencing, paragraph 1; Figure 2b\n  quote: Behavioral performance was only slightly affected after unilateral photoinhibition with a\n    single spot during the early delay epoch ( Fig. 2b , 70.3% correct, p = 0.009, two-tailed t-test\n    against control); unilateral photoinhibition with four spots had small additional effect (67.7%,\n    p=0.003)\n  statistics:\n  - about: one spot unilateral against control\n    test: two-tailed t-test\n    p: 0.009\n    n: 13 mice\n  - about: four spots unilateral against control\n    test: two-tailed t-test\n    p: 0.003\n    n: 13 mice\n  expected:\n  - quantity: performance, one spot unilateral, early delay\n    value: 70.3\n    tolerance: 7.03\n    unit: '% correct'\n  - quantity: performance, four spots unilateral, early delay\n    value: 67.7\n    tolerance: 6.77\n    unit: '% correct'\n  criterion: Bilateral experiment behaviour (13 mice), convention P. Left and right hemisphere\n    pooled. The Results give durations of 0.8 s or 1.3 s; readings (a) both durations pooled per\n    mouse, (b) 0.8 s only (Methods). Performance as the mean over mice. Reproduced when both values\n    are within tolerance and both p < 0.05 under one combination of readings.\n- id: fig2b-bilateral-performance\n  statement: Bilateral photoinhibition degraded performance severely (two spots 58.0%, eight spots\n    51.4%, near chance), more than four-spot unilateral photoinhibition.\n  source: Results, Preparatory activity after bilateral silencing, paragraph 1; Figure 2b\n  quote: In contrast, using only two spots across both hemispheres caused performance to degrade\n    severely ( Fig. 2b , 58.0%, p<0.001; difference from 4 spot unilateral: p<0.05, two-tailed t-test);\n    four spots bilaterally further reduced performance to near chance level (4 laser spots: 51.4%,\n    p<0.001)\n  statistics:\n  - about: one spot each side against control\n    test: two-tailed t-test\n    p: 0.001\n    p_relation: \"<\"\n  - about: one spot each side against four spots unilateral\n    test: two-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n  - about: four spots each side against control\n    test: two-tailed t-test\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: performance, bilateral one spot per side\n    value: 58.0\n    tolerance: 5.8\n    unit: '% correct'\n  - quantity: performance, bilateral four spots per side\n    value: 51.4\n    tolerance: 5.14\n    unit: '% correct'\n  criterion: As fig2b-unilateral-performance. The comparison of bilateral one-spot with unilateral\n    four-spot uses the same t-test, readings P1 and P2. Reproduced when both values are within\n    tolerance and all three tests hold under one combination of readings.\n- id: ed6a-bilateral-inconsistent-bias\n  statement: Bilateral photoinhibition biased movements inconsistently across mice and sessions,\n    toward lick left in some and lick right in others.\n  source: Results, Preparatory activity after bilateral silencing, paragraph 1; Extended Data Figure\n    6a\n  quote: Bilateral photoinhibition biased movements inconsistently across mice and sessions\n  criterion: Per session of the bilateral experiment, bias as lick right performance minus lick\n    left performance under bilateral photoinhibition, minus the same in control. The paper gives no\n    test. Reproduced when, among sessions with a bias significant by Fisher's exact test (p < 0.05,\n    a reading; the paper gives no test), both signs occur, and occur in at least two mice.\n- id: fig2-recordings-recovery\n  statement: After ipsilateral (one spot) photoinhibition spike rate (more than 90%) and selectivity\n    (more than 80%) recovered within 600 ms; contralateral photoinhibition hardly affected activity;\n    after bilateral photoinhibition spike rates recovered on average but selectivity did not.\n  source: Results, Preparatory activity after bilateral silencing, paragraph 2; Figure 2c-e\n  quote: As before ( Fig. 1 ), spike rate (> 90 %) ( Fig. 2c, d ) and selectivity (> 80%) ( Fig. 2e )\n    recovered 600 ms after ipsilateral perturbation. ALM activity was hardly affected by\n    contralateral photoinhibition ... After bilateral photoinhibition neurons recovered their spike\n    rate on average ( Fig. 2c, d ), but selectivity failed to recover\n  criterion: Bilateral experiment recordings (7 mice; Fig. 2d n = 276, 283, 332 neurons). At 600 ms\n    after photoinhibition offset. Spike rate recovery is read two ways; (a) fewer than 10% of\n    neurons with a significant change (convention R), (b) population mean rate at least 90% of\n    control. Selectivity, convention D, at least 80% of control. Hardly affected (contralateral),\n    fewer than 10% of neurons significant in every window during and after photoinhibition, a\n    reading. Bilateral, rate recovered as in (a) or (b), and selectivity below 80% of control at\n    the go cue. Reproduced when all hold under one combination of readings.\n- id: fig2e-selectivity-recovery-times\n  statement: Selectivity recovered to 80% of control 538 ms after ipsilateral and 192 ms after\n    contralateral photoinhibition, and did not recover after bilateral photoinhibition.\n  source: Figure 2e legend\n  quote: 'Selectivity recovery: ipsilateral, 538±178 ms; contralateral, 192±114 ms; bilateral, no\n    recovery'\n  expected:\n  - quantity: recovery time, ipsilateral\n    value: 538\n    tolerance: 178\n    unit: ms\n  - quantity: recovery time, contralateral\n    value: 192\n    tolerance: 114\n    unit: ms\n  - quantity: selective neurons included\n    value: 143\n    tolerance: 14.3\n  depends_on:\n  - selective-fraction\n  criterion: Convention D on the bilateral experiment. Bilateral, no recovery means\n    photoinhibition selectivity stays below 80% of control up to the go cue. Reproduced when both\n    times are within tolerance and bilateral does not recover, under one bin reading.\n- id: ed7-larger-photoinhibition\n  statement: Bilateral photoinhibition with one spot per side changed selectivity more persistently\n    than unilateral photoinhibition with four spots, and recovery after unilateral photoinhibition\n    was less robust with larger photoinhibition (ipsilateral four spots 490 ms, contralateral 235\n    ms, bilateral no recovery).\n  source: Results, Preparatory activity after bilateral silencing, paragraph 2; Extended Data Figure\n    7d\n  quote: 'Ipsilateral: 490±280 ms to recover to 80% of control selectivity; contralateral: 235±156\n    ms; bilateral: no recovery at end of delay period'\n  expected:\n  - quantity: recovery time, ipsilateral four spots\n    value: 490\n    tolerance: 280\n    unit: ms\n  - quantity: recovery time, contralateral four spots\n    value: 235\n    tolerance: 156\n    unit: ms\n  - quantity: selective neurons included\n    value: 40\n    tolerance: 4\n  depends_on:\n  - selective-fraction\n  criterion: Convention D on experiment 3 (3 mice). Reproduced when both times are within\n    tolerance, bilateral one-spot selectivity stays below 80% of control at the end of the delay,\n    and the selectivity change at the go cue is larger (more negative) after bilateral one-spot than\n    after ipsilateral four-spot photoinhibition. Less robust with size is read as the ipsilateral\n    selectivity change at the go cue being larger after four spots (this claim) than after one\n    spot (fig2e-selectivity-recovery-times); the paper gives no test, so the values are reported\n    and the comparison is part of the outcome only by sign.\n- id: ed7e-roc-larger-photoinhibition\n  statement: Trajectory separation along cd at the end of the delay was 0.80 in control, 0.64 after\n    ipsilateral and 0.68 after contralateral four-spot photoinhibition, and 0.54 after bilateral\n    one-spot photoinhibition.\n  source: Extended Data Figure 7e\n  quote: 'We quantified the separation between trajectories at the end of delay epoch by computing ROC\n    values for each session: control, 0.80 ± 0.08; ipsilateral, 0.64 ± 0.10; contralateral, 0.68 ±\n    0.15; bilateral, 0.54 ± 0.8'\n  expected:\n  - quantity: ROC, control\n    value: 0.80\n    tolerance: 0.08\n  - quantity: ROC, ipsilateral four spots\n    value: 0.64\n    tolerance: 0.10\n  - quantity: ROC, contralateral four spots\n    value: 0.68\n    tolerance: 0.15\n  - quantity: ROC, bilateral one spot\n    value: 0.54\n    tolerance: 0.08\n  criterion: Convention A on experiment 3 sessions with > 5 simultaneously recorded neurons tested\n    on > 3 trials per condition (legend). The legend prints the bilateral s.e.m. as 0.8, which\n    cannot be an s.e.m. of an ROC value; 0.08 is used and the misprint recorded. Reproduced when\n    all four are within tolerance under one of H1, H2.\n- id: cd-stable-over-epochs\n  statement: The direction of the lick right minus lick left difference vector was stable over the\n    sample and delay epochs (correlation 0.61 between late sample and late delay).\n  source: Methods, Analysis of population dynamics in the activity space, paragraph 1; Extended Data\n    Figure 9b\n  quote: was stable (correlation of w t 's between late sample epoch vs. late delay epoch, 0.61 ±\n    0.05; Extended Data Fig. 9b )\n  expected:\n    quantity: correlation of w, late sample against late delay\n    value: 0.61\n    tolerance: 0.05\n  criterion: Convention A. Late sample and late delay are read as the last 400 ms window of each\n    epoch. Pearson correlation of the two w vectors per session, mean over the 16 sessions.\n    Reproduced when within the paper's s.e.m.\n- id: cd-captures-selectivity\n  statement: Projection on cd captured 65.6% of population selectivity and 36.4% of task-related\n    activity variance over the sample and delay epochs; modes 1 to 5 together captured 98.5% of\n    variance and 95.8% of selectivity.\n  source: Methods, Analysis of population dynamics in the activity space, paragraphs 1 and 3;\n    Extended Data Figure 8a\n  quote: The projection along the cd captured 65.6±5.1% of the population selectivity for “lick left”\n    and “lick right” trials over the sample and delay epochs ... and 36.4±6.3% of the total variance\n    in ALM task-related activity\n  expected:\n  - quantity: selectivity captured by cd\n    value: 65.6\n    tolerance: 5.1\n    unit: '%'\n  - quantity: variance captured by cd\n    value: 36.4\n    tolerance: 6.3\n    unit: '%'\n  - quantity: variance captured by modes 1-5\n    value: 98.5\n    tolerance: 0.5\n    unit: '%'\n  - quantity: selectivity captured by modes 1-5\n    value: 95.8\n    tolerance: 1.2\n    unit: '%'\n  criterion: Convention A. Selectivity is the RMS of the trial-averaged lick right minus lick left\n    rate over neurons and time in the sample and delay epochs; variance is the RMS of the\n    baseline-subtracted trial-averaged activity (Methods). Captured fraction is read as the RMS of\n    the projected quantity over the RMS of the full quantity; whether RMS or its square (variance)\n    enters the ratio is not stated, readings (a) RMS ratio, (b) squared ratio. The baseline is not\n    defined; readings (a) the pre-sample period, (b) the mean over the trial. Modes as in fig3-modes.\n    Tolerances are the paper's s.e.m. Reproduced when the cd values are within tolerance under a\n    reading; the mode 1-5 values are reported and must hold for a full reproduction, else partial.\n- id: fig3c-cd-recovery-roc\n  statement: Along cd, trajectories recovered after ipsilateral photoinhibition (ROC 0.73 against\n    0.76 in control) and were little changed by contralateral photoinhibition (0.74), but were\n    permanently altered by bilateral photoinhibition (0.58).\n  source: Results, Robustness along the coding direction, paragraph 1; Figure 3c; Extended Data\n    Figure 8\n  quote: 'After ipsilateral photoinhibition the cd mode recovered to trajectories similar to the\n    unperturbed trials ( Fig. 3c ; ROC values between trajectories at the end of delay epoch: control,\n    0.76 ± 0.03; ipsilateral, 0.73 ± 0.02; mean ± s.e.m. across sessions'\n  expected:\n  - quantity: ROC, control\n    value: 0.76\n    tolerance: 0.03\n  - quantity: ROC, ipsilateral\n    value: 0.73\n    tolerance: 0.02\n  - quantity: ROC, contralateral\n    value: 0.74\n    tolerance: 0.03\n  - quantity: ROC, bilateral\n    value: 0.58\n    tolerance: 0.03\n  criterion: Convention A on the 16 sessions. Reproduced when all four are within the paper's\n    s.e.m. under H1 or H2; partially when control, ipsilateral and bilateral are and their order\n    holds.\n- id: ed8-roc-during-photoinhibition\n  statement: During photoinhibition trajectory separation along cd fell to 0.54 (ipsilateral), 0.64\n    (contralateral) and 0.54 (bilateral), against 0.72 in control.\n  source: Extended Data Figure 8 legend\n  quote: 'ROC values during the time period of photoinhibition: control, 0.72 ± 0.02; ipsilateral,\n    0.54 ± 0.03; contralateral, 0.64 ± 0.03; bilateral 0.54 ± 0.01'\n  expected:\n  - quantity: ROC during photoinhibition, control\n    value: 0.72\n    tolerance: 0.02\n  - quantity: ROC during photoinhibition, ipsilateral\n    value: 0.54\n    tolerance: 0.03\n  - quantity: ROC during photoinhibition, contralateral\n    value: 0.64\n    tolerance: 0.03\n  - quantity: ROC during photoinhibition, bilateral\n    value: 0.54\n    tolerance: 0.01\n  criterion: Convention A, with cd'x in a window during photoinhibition. Which window is not given;\n    readings (a) the last 400 ms before the ramp, (b) the 400 ms window centred on the\n    photostimulus, (c) the mean over the photostimulus. Reproduced when all four are within\n    tolerance under a reading.\n- id: fig3c-cd-predicts-movement\n  statement: Activity along cd predicts the upcoming movement trial by trial; deviations toward the\n    lick right trajectory predict more lick right responses, and vice versa.\n  source: Results, Robustness along the coding direction, paragraph 1; Figure 3c bottom; Extended\n    Data Figures 8b and 9e\n  quote: Deviations toward the “lick right” trajectory predicted more frequent “lick right”\n    responses and vice versa\n  criterion: Convention A. For each session the decision boundary on held-out control trials; for\n    each held-out control and perturbation trial, the distance of cd'x from the boundary in the\n    last 400 ms before the go cue; trials pooled over sessions. The paper gives no test. Measure,\n    the fraction of trials whose lick falls on the side of the boundary (Extended Data Fig. 8b),\n    and performance on lick right and lick left trials binned along the distance (bin 4, Extended\n    Data Fig. 9e). Reproduced, for control and ipsilateral trials, when the fraction predicted is\n    above 0.5 by a one-sided binomial test at p < 0.05 (a reading of above chance) and lick right\n    performance rises and lick left performance falls with distance (Spearman correlation over\n    bins of the right sign, a reading).\n- id: fig3d-persistent-mode\n  statement: A persistent mode, built to capture the sustained effect of ipsilateral perturbation,\n    stays altered past movement onset but neither discriminates trial type nor predicts behaviour on\n    control trials.\n  source: Results, Robustness along the coding direction, paragraph 1; Figure 3d\n  quote: By construction, the persistent mode was altered by the perturbation, up to and beyond\n    movement onset. However, this projection did not discriminate trial type nor predict behavior on\n    control trials\n  depends_on:\n  - fig3c-cd-predicts-movement\n  criterion: Mode 2 (Methods), the difference of mean response vectors, ipsilateral perturbed minus\n    control lick right trials, correct trials, at the go cue (last 400 ms window). ROC between lick\n    right and lick left control trials on the projection, and the fraction of control trials\n    predicted with a decision boundary made as for cd. The paper gives no test for absence;\n    reproduced when the session mean ROC is within 2 bootstrap s.e.m. of 0.5 and the fraction\n    predicted is not above 0.5 by the one-sided binomial test of fig3c-cd-predicts-movement,\n    while the ipsilateral minus control difference at the go cue is outside 2 s.e.m. of zero (2\n    s.e.m. is a standard choice; values shown).\n- id: fig3e-ramping-mode\n  statement: A ramping mode capturing most remaining variance shows non-selective ramping in the\n    delay epoch, does not predict behaviour, and is resistant to unilateral and bilateral\n    perturbation.\n  source: Results, Robustness along the coding direction, paragraph 1; Figure 3e; Extended Data\n    Figure 8c-e\n  quote: Third, a mode that maximally captured the remaining activity variance, showed non-selective\n    ramping during the delay epoch, did not predict behavior, and was resistant to unilateral and\n    bilateral perturbations\n  depends_on:\n  - fig3c-cd-predicts-movement\n  criterion: Mode 4 (Methods), the first SVD eigenvector of the baseline-subtracted PSTH matrix\n    (lick right and lick left concatenated, sample and delay epochs as a reading of the time range)\n    made orthogonal to modes 1 to 3 by Gram-Schmidt; mode 3 from the lick left difference, made\n    orthogonal to mode 2. Reproduced when the control projection rises over the delay (end minus\n    start of delay, positive in the session mean), its ROC between trial types and its fraction\n    predicted fail the tests of fig3d-persistent-mode, and for ipsilateral, contralateral and\n    bilateral trials the perturbed minus control difference at the go cue is within 2 bootstrap\n    s.e.m. of zero (a standard choice). Mode 5 is reported as a variant.\n- id: fig4-bilateral-cd-predicts-movement\n  statement: Even after bilateral photoinhibition destroys average selectivity, single-trial\n    activity along cd predicts the upcoming movement.\n  source: Results, Robustness along the coding direction, paragraph 2; Figure 4b; Extended Data\n    Figures 6b and 9e\n  quote: This analysis shows that even after average selectivity is destroyed by perturbations, ALM\n    population dynamics still dictate upcoming movements\n  criterion: As fig3c-cd-predicts-movement, on bilateral photoinhibition trials. Reproduced when\n    both conditions of that criterion hold for bilateral trials.\n  depends_on:\n  - fig3c-cd-predicts-movement\n- id: ed6b-session-bias-predicted\n  statement: In each session the behavioural bias after bilateral photoinhibition followed the side\n    of the control trajectory that the perturbed cd trajectory ended closer to.\n  source: Extended Data Figure 6b\n  quote: The biases in movement were predicted based ALM activity trajectories\n  criterion: Per session with bilateral photoinhibition, the mean cd'x of bilateral trials at the go\n    cue relative to the decision boundary (convention A), and the behavioural bias of\n    ed6a-bilateral-inconsistent-bias. Reproduced when the signs agree in a majority of sessions\n    above chance by a one-sided binomial test at p < 0.05 (a reading; the paper shows five example\n    sessions and gives no test). The five sessions of the legend (20, 16, 18, 10, 12 neurons) are\n    reported if they can be identified.\n  depends_on:\n  - ed6a-bilateral-inconsistent-bias\n- id: ed9f-reaction-time\n  statement: Reaction times were faster on trials whose cd trajectory was far from the decision\n    boundary at the go cue.\n  source: Extended Data Figure 9f\n  quote: Reaction times are faster on trials in which the trajectory is far from the decision\n    boundary at the time of the ‘go’ cue\n  criterion: Convention A, 16 sessions. Reaction time, the first lick after the go cue, relative to\n    the session mean; distance, the absolute distance of cd'x from the boundary at the go cue;\n    lick right and lick left trials pooled. Which trial conditions enter is not given; readings (a)\n    control trials, (b) all trials. The paper gives no test. Reproduced when the Spearman\n    correlation between absolute distance and reaction time is negative with p < 0.05 (a reading).\n- id: ed9c-cd-window-robust\n  statement: The recovery along cd after unilateral perturbation does not depend on the window used\n    to compute cd (first or last 400 ms of the delay epoch).\n  source: Extended Data Figure 9c\n  quote: The recovery of ALM dynamics along the coding direction ( cd ) is robust to the choice of\n    time window for the calculation of cd\n  depends_on:\n  - fig3c-cd-recovery-roc\n  criterion: As fig3c-cd-recovery-roc with cd from the first or the last 400 ms of the delay epoch.\n    Reproduced when, for both windows, the ipsilateral ROC at the end of the delay is within 0.05 of\n    the control ROC (a reading of recovery, from the 0.73 against 0.76 of the main result) and the\n    bilateral ROC is lower than the ipsilateral.\n- id: fig5b-callosotomy-control-performance\n  statement: Bisecting the ALM corpus callosum did not affect performance on control trials.\n  source: Results, Contralateral input is required for recovery, paragraph 1; Figure 5b; Extended\n    Data Figure 10b\n  quote: Remarkably, behavioral performance was unaffected ( Fig. 5b , control trials, before vs.\n    after callosotomy, p>0.05, two-tailed t-test)\n  statistics:\n  - test: two-tailed t-test\n    p: 0.05\n    p_relation: \">\"\n    n: 7 mice\n  criterion: A claim of absence, judged on the paper's test, a two-tailed t-test of control-trial\n    performance before against after callosotomy over the 7 mice (readings P1, P2). Reproduced when\n    p > 0.05; not reproduced otherwise. The difference is reported. Needs behaviour sessions before\n    the cut, which the author must find.\n- id: fig5b-callosotomy-unilateral-sensitivity\n  statement: After callosotomy, performance became highly sensitive to unilateral (one spot)\n    photoinhibition, with a significant interaction between callosotomy and photoinhibition, and\n    dropped to the level of bilateral photoinhibition in control mice.\n  source: Results, Contralateral input is required for recovery, paragraph 1; Figure 5b\n  quote: 'However, behavioral performance was now highly sensitive to transient unilateral\n    photoinhibition ( Fig 2b , 1 laser spot: p=0.0019, two-tailed t-test against control). There was a\n    significant interaction between callosotomy and unilateral photoinhibition (p=0.0035, repeated\n    measure two-way ANOVA)'\n  statistics:\n  - about: unilateral one spot against control, after callosotomy\n    test: two-tailed t-test\n    p: 0.0019\n    n: 7 mice\n  - about: interaction of callosotomy and unilateral photoinhibition\n    test: repeated measure two-way ANOVA\n    p: 0.0035\n    n: 7 mice\n  criterion: Convention T (C1, C2) and P. ANOVA on per mouse performance with factors callosotomy\n    (before, after) and photoinhibition (control, unilateral one spot), both within mouse.\n    Reproduced when the t-test has p < 0.01 and the interaction p < 0.01 under a reading, and the\n    after-callosotomy unilateral performance is within the bilateral one-spot value of\n    fig2b-bilateral-performance plus or minus 10% (58.0, tolerance 5.8).\n  depends_on:\n  - fig2b-bilateral-performance\n- id: ed10-callosotomy-preparatory-activity\n  statement: Preparatory activity after callosotomy was similar to control; 254 of 496 putative\n    pyramidal neurons were selective.\n  source: Results, Contralateral input is required for recovery, paragraph 2; Extended Data Figure\n    10e-g\n  quote: Preparatory activity in callosotomized mice (n=7 mice) was similar to control mice ( Fig.\n    5c ; Extended Data Fig. 10 ), providing additional evidence that the two ALM hemispheres can\n    maintain preparatory activity independently\n  expected:\n  - quantity: selective putative pyramidal neurons after callosotomy\n    value: 254\n    tolerance: 25.4\n  - quantity: putative pyramidal neurons after callosotomy\n    value: 496\n    tolerance: 49.6\n  criterion: Conventions U and S on the callosotomy recordings, control trials. The paper gives no\n    test of similarity. Reproduced when both counts are within tolerance and the population\n    selectivity in the delay epoch (convention D, control trials) is positive with its bootstrap\n    95% interval above zero. The fraction selective, the delay selectivity and the contra- to\n    ipsi-preferring proportion are reported beside those of control mice.\n- id: fig5-callosotomy-no-recovery\n  statement: After callosotomy, ipsilateral photoinhibition left spike rates recovered on average\n    but selectivity failed to recover; contralateral photoinhibition selectivity recovered in 217 ms;\n    bilateral did not recover.\n  source: Results, Contralateral input is required for recovery, paragraph 2; Figure 5d, e legend\n  quote: After ipsilateral photoinhibition, ALM neurons recovered their average spike rate ( Fig. 5c,\n    d ), but selectivity failed to recover ( Fig. 5e )\n  expected:\n  - quantity: recovery time, contralateral\n    value: 217\n    tolerance: 228\n    unit: ms\n  - quantity: selective neurons included\n    value: 129\n    tolerance: 12.9\n  depends_on:\n  - ed10-callosotomy-preparatory-activity\n  criterion: Conventions R and D on the callosotomy recordings (Fig. 5d n = 325, 322, 313).\n    Reproduced when, under one bin reading, ipsilateral and bilateral selectivity stay below 80% of\n    control up to the go cue, contralateral recovery time is within tolerance, and the population\n    mean rate after ipsilateral photoinhibition returns to at least 90% of control by the go cue\n    (reading b of fig2-recordings-recovery; reading a as variant).\n- id: fig5f-callosotomy-cd-reduced\n  statement: After callosotomy, selectivity along cd was reduced following ipsilateral\n    photoinhibition.\n  source: Results, Contralateral input is required for recovery, paragraph 2; Figure 5f\n  quote: Selectivity in the cd direction was reduced ( Fig. 5f , 16 sessions)\n  criterion: Convention A on callosotomy sessions (> 5 neurons, > 5 trials per condition; 16\n    sessions expected). ROC at the end of the delay for control and ipsilateral trials per session.\n    The paper gives no test; reproduced when ipsilateral ROC is lower than control by a paired\n    t-test over sessions at p < 0.05 (a reading) under H1 or H2, and the session count is within\n    10% of 16.\n- id: ed1-monolithic-models-fail\n  statement: Monolithic network models (integrator, integrator with corrective feedback, trained\n    random recurrent networks) do not recover the unperturbed trajectory after transient silencing\n    of half their neurons.\n  source: Results, Robust model networks, paragraph 1; Extended Data Figure 1f-i\n  quote: Overall, all “monolithic” models consisting of one network were unable to explain\n    robustness\n  criterion: A simulation, not a test on recorded data. Parameters from the Methods and Extended\n    Data Fig. 1 legend (simple integrator N = 100, tau 100 ms, one eigenvalue 0.99; FORCE network N =\n    400, tau 200 ms, tanh, p = 0.1, gain 1.5, 30 iterations; silencing 0.2 to 1.0 s of 2 s). The\n    integration step, noise and random seeds are not given; standard choices (1 ms step, fixed\n    seeds, at least 10 networks). Reproduced when, at 2 s, the output of each model differs from\n    its unperturbed output by more than 10% of the unperturbed selectivity (a reading of failure to\n    recover), for the simple integrator and the transient-input FORCE network. The corrective\n    feedback and tamed chaos models lack parameters in the text (weights, tuning threshold) and are\n    reported only if they can be built from the cited methods.\n- id: fig6-modular-models-recover\n  statement: Modular networks of two coupled modules (attractor, integrator, trained recurrent\n    network) recover after silencing of one module, and drift to a random fixed point when both are\n    silenced.\n  source: Results, Robust model networks, paragraph 2; Figure 6b-d\n  quote: Selective commissural connections restored activity on the other side after unilateral\n    transient silencing ( Fig. 6b ). When the two sides are silenced, the network drifts to one of the\n    fixed points randomly\n  criterion: A simulation, not a test on recorded data. Modular attractor with the Methods'\n    weights (self 0.5235, within-module -0.5235, between-module 0.3), tau 100 ms, f(x) = g(x) -\n    g(0) with g(x) = 1.4 / (1 + exp(-(x - 0.5) / 0.3)), input 0.1 from 0.05 to 0.1 s, tonic 0.5,\n    noise variance 0.01; modular integrator with the 8 by 8 matrix printed in the Methods, tau 10\n    ms, input 0.04, tonic 40. Integration step and noise scaling with step are not given; standard\n    choice 1 ms with Euler-Maruyama. Reproduced when, over 100 simulated trials per trial type, the\n    modular attractor ends at the instructed fixed point in more than 90% of trials after\n    unilateral silencing (0.2 to 1.0 s) and in 30% to 70% after bilateral silencing, and the\n    modular integrator returns within 10% of its unperturbed trajectory by 2 s after unilateral\n    silencing. The FORCE modular network is not specified enough to rebuild and is reported only.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000011/10.1038-nature17643.yaml paper/10.1038-nature17643.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/000011 && python - <<'EOF'
import re
p='10.1038-nature17643.yaml'
s=open(p).read()
s=s.replace("""  quote: Sample epoch: 249 ± 68 ms to recover to 80 % of control selectivity; early delay: 275 ± 168
    ms; middle delay: 250 ± 218 ms""","""  quote: 'Sample epoch: 249 ± 68 ms to recover to 80 % of control selectivity; early delay: 275 ± 168
    ms; middle delay: 250 ± 218 ms'""")
open(p,'w').write(s)
# find other plain scalars with ': ' 
import yaml
d=yaml.safe_load(s)
for c in d['claims']:
    for k,v in c.items():
        pass
EOF
cd ../..; python tools/claims_check.py claims/000011/10.1038-nature17643.yaml paper/10.1038-nature17643.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -v '^#' claims/000011/10.1038-nature17643.yaml | grep -E '^[0-9]+: +(- )?[a-z_]+: .*: |^[0-9]+:    [^-].*: '
```

```
107:    value: 1012
108:    tolerance: 101.2
110:    value: 58
111:    tolerance: 5.8
113:    value: 72
114:    tolerance: 7.2
116:    value: 890
117:    tolerance: 89
119:    value: 50
120:    tolerance: 5
133:    value: 634
134:    tolerance: 63.4
136:    value: 176
137:    tolerance: 17.6
139:    value: 337
140:    tolerance: 33.7
142:    value: 493
143:    tolerance: 49.3
157:    p: 0.01
158:    p_relation: "<"
[... 158 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000011/10.1038-nature17643.yaml",
 "old_string": "  quote: In contrast, using only two spots across both hemispheres caused performance to degrade\n    severely ( Fig. 2b , 58.0%, p<0.001; difference from 4 spot unilateral: p<0.05, two-tailed t-test);\n    four spots bilaterally further reduced performance to near chance level (4 laser spots: 51.4%,\n    p<0.001)",
 "new_string": "  quote: 'In contrast, using only two spots across both hemispheres caused performance to degrade\n    severely ( Fig. 2b , 58.0%, p<0.001; difference from 4 spot unilateral: p<0.05, two-tailed t-test);\n    four spots bilaterally further reduced performance to near chance level (4 laser spots: 51.4%,\n    p<0.001)'"
}
```

```
The file claims/000011/10.1038-nature17643.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000011/10.1038-nature17643.yaml paper/10.1038-nature17643.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/000011/10.1038-nature17643.yaml; grep -c -i 'rather\|—' $f; python -c "
import yaml;d=yaml.safe_load(open('$f'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

```
0
38 7 11 38 19
```

**Agent**

I wrote `claims/000011/10.1038-nature17643.yaml`, with 38 claims. The quote checker reports 38 claims, 38 quotes, 11 statistical values and 0 problems. Nothing is committed.

**Text read:** the HHMI author manuscript (PMC5081260, served by Europe PMC), not the version of record. It has the main text, Methods, and the legends of Figures 1 to 6 and Extended Data Figures 1 to 10. The paper has no supplement beyond the Extended Data, so nothing the results rest on is missing. Two gaps:
- **No PDF:** no figure could be read, so values shown only in figures are not claimed.
- **Corrigendum not read:** the record lists one (doi:10.1038/nature18623) but its text was not supplied, so I don't know whether it changes any value.

**Code:** the paper links no code. It names its data deposit as CRCNS doi:10.6080/K0RB72JW.

**Counts:**
- **Quotes:** 38 of 38 claims; none needed an `inferred` note.
- **Statistics:** 7 claims carry 11 entries, all t-tests (two-tailed or paired) plus one repeated-measures two-way ANOVA.
- **Criteria:** every claim has one.
- **Expected values:** 19 claims. Tolerances are the paper's s.e.m. where it gives one, otherwise 10%.
- **Absence claims:** three, each judged on the paper's own test (p > 0.1, the t-test of Extended Data Fig. 3, and p > 0.05).
- **Simulations:** the two model claims are simulations, not tests on recorded data.

**Details the paper leaves open, with the readings named** (shared ones are set once in the opening comment):
- **Condition names:** the Results and Methods name the unilateral conditions differently. The Results call the 0 s condition "late delay" and the 0.3 s one "middle delay"; the Methods call the 0.3 s one "late delay".
- **Callosotomy timing:** either as in the bilateral experiment, or as recorded in the dataset's trial metadata.
- **Response epoch length:** 1.3 s or 1.5 s.
- **Selectivity t-test:** correct trials only, or all trials; Student's or Welch's.
- **Selectivity time-course bin:** 200 ms or 400 ms.
- **Rate-test windows:** labelled by their end or their centre; with the 1 spike/s and 3-trial exclusion or without it.
- **Performance t-test:** paired or unpaired over mice.
- **Trials held out to compute the coding direction:** half or a third of control trials.
- **Variance captured:** ratio of RMS or of squared RMS; baseline taken before the sample epoch or over the whole trial.
- **ROC window during photoinhibition:** three readings.
- **Fig. 1f:** whether the 10% describes each condition or the three pooled.
- **Fig. 2 recovery:** "spike rate (> 90%)" as a fraction of neurons not changed, or as the population mean rate.
- **Fig. 2b durations:** 0.8 s only, or 0.8 s and 1.3 s pooled.
- **Ipsilateral bias measure:** performance on contralateral trials, or overall performance.
- **Extended Data Fig. 4:** how photoinhibition conditions and trial types are pooled.
- **Half-max radius:** linear interpolation or a Gaussian fit.

Where the paper gives no test (above chance, "similar", "little affected", "resistant"), the criterion names the reading it uses and says it is one.

**Paper inconsistencies and gaps a claim needed:**
- **514 vs 510 ms:** the Results give 514 ms for selectivity recovery; the Fig. 1g legend gives 510 ms. The legend's values are used.
- **Misprinted s.e.m.:** Extended Data Fig. 7e prints the bilateral ROC as 0.54 ± 0.8; 0.08 is used.
- **Mislabelled figure:** the Methods cite "Extended Data Fig. 2h, i" for the trained recurrent networks, which are in Extended Data Fig. 1h, i.
- **Photoactivation timing:** not given in the text; the criterion reads it from the dataset's trial metadata.
- **Models:** the integration step and noise scaling are not given. The corrective-feedback, tamed-chaos and modular FORCE models lack parameters, so those parts are reported only.
- **Modular integrator:** its 8×8 weight matrix was read from flattened text, row by row, with no PDF to confirm it.

Whether the dataset holds the behaviour-only sessions, the untrained-mouse recordings (Extended Data Fig. 2d) and the sessions before callosotomy is for the author to find.

## End of run

23 turns, 6 minutes, result: success.
