# crcns-ssc-7 · claims · run 42231875162

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/crcns-ssc-7/ paper/;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^### 5. Record/' docs/protocol.md | sed -n '30,400p'
```

```
says which text was read (the version of record or a preprint version, and the
supplement), and describes the data the paper used: the subjects, sessions,
conditions and measured variables, as the paper reports them, so that the
author can find them in the dataset.

   - One claim per finding, at the level of a figure panel or a reported
     number when the full text is available. Cover the paper's main findings,
     including those the dataset cannot test.
   - `statement`: the finding in words. `source`: where the paper shows it,
     precise enough to find without searching: a figure panel, or a section
     and paragraph ("Results, Place fields, paragraph 3").
   - `quote`: the sentence at `source` that states the finding, copied word
     for word from the full text, cut with "..." where it runs long. It lets a
     reader check the statement against the paper without opening it. For a
     finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
     states it (numbers only in a table, a result spread over several
     legends), a short note under `inferred` saying so. The statement is
     then a reading of the paper, and the note says what it was
[... 324 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/001453/ claims/crcns-ssc-7/ paper/ 2>&1; ls claims | head -50; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; ls claims | grep -i crcns
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
[... 318 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/crcns-ssc-3/; head -60 claims/crcns-ssc-3/*.yaml; cat paper/ssc-7.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Read the protocol and the example; now reading the paper text.

**Agent calls Bash**

```bash
head -c 40000 paper/10.1038-nn.4412.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4412.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4412.txt",
 "offset": 1225,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4412.txt",
 "offset": 1925,
 "limit": 620
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "Code read|code deposited|inside the dataset|with the dataset",
 "path": "claims",
 "glob": "crcns-*/*.yaml",
 "output_mode": "content",
 "-A": 3
}
```

```
claims/crcns-pfc-1/10.1016-j.neuron.2014.04.031.yaml:14:# Code read: github.com/cxrodgers/Rodgers2014 at commit 390b6089c429877dfea9c56de153bbea0380c20f
claims/crcns-pfc-1/10.1016-j.neuron.2014.04.031.yaml-15-# (2016-07-09), linked from the Experimental Procedures. It holds one folder of Python 2 scripts per
claims/crcns-pfc-1/10.1016-j.neuron.2014.04.031.yaml-16-# figure (2-1-behavres, 3-1-hold, 3-2-errhold, 3-3-vs_spont, 3-4-RT_vs_hold, 3-5-vidtrack,
claims/crcns-pfc-1/10.1016-j.neuron.2014.04.031.yaml-17-# 5-1-timecourse, 5-2-timecourse_exemplars, 6-1-evoked, 6-2-evokmisc, 6-3-evokgain, 7-1-zap, 8-1-model),
--
claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml:18:# Code read: none. The paper links no analysis or model code. Its Data Availability names the
claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml-19-# deposit "http://dx.doi.org/10.6080/K07D2S2F" at CRCNS, which is ssc-3. The data descriptor
claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml-20-# (ssc-3 data description, version 0.8) was read only to know what the dataset holds; no claim
claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml-21-# comes from it.
--
claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml:16:# Code read (the Key Resources Table links three FentonLab repositories, for Figures 3, 4, 5 and
claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml-17-# S5). SpikeField, commit 4dfbc35 (MATLAB, getLFPphase.m and getWavelets.m): spike phases from
claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml-18-# complex Morlet wavelets (wavelet factor 8) at 100 log-spaced frequencies from 2 to 250 Hz on LFP
claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml-19-# sampled at 2 kHz, the wire of each tetrode with the least artifact, spikes in artifact periods
--
claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml:13:# Code read: the model code the paper links, ModelDB accession 153280 ("superdeep", NEURON),
claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml-14-# downloaded from modeldb.science
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A6 "^schema_version" claims/crcns-ssc-3/*.yaml; grep -n "^  data:\|^  kind\|elsewhere\|with_inputs" claims/crcns-*/*.yaml | head; sed -n 1,60p tools/claims_check.py
```

```
75:schema_version: 2
76-dataset:
77-  archive: crcns
78-  id: ssc-3
79-  doi: 10.6080/K07D2S2F
80-paper: doi:10.1371/journal.pcbi.1004858
81-claims:
claims/crcns-ac-2/10.1152-jn.00197.2004.yaml:462:    the paper uses elsewhere, (b) a paired t-test over the 16 neurons in both sets. The p
claims/crcns-ac-2/10.1152-jn.00197.2004.yaml:732:  kind: agent
claims/crcns-bf-1/10.1073-pnas.1712431115.yaml:698:  kind: agent
claims/crcns-bf-3/10.1038-s42003-020-01554-4.yaml:1415:  kind: agent
claims/crcns-bf-3/10.1038-s42003-020-01554-4.yaml:1419:  - recorded-units and cue-responsive-screen, source changed from Results paragraph 3 to paragraph 2; the 435 and 257 counts are in the second paragraph ("Electrode placement was confirmed..."), legends not counted, as elsewhere in the file.
claims/crcns-ear-1/10.1085-jgp.201912447.yaml:77:  kind: link
claims/crcns-ear-1/10.1085-jgp.201912447.yaml:768:  data: with_inputs
claims/crcns-ear-1/10.1085-jgp.201912447.yaml:786:  data: with_inputs
claims/crcns-ear-1/10.1085-jgp.201912447.yaml:1102:  data: with_inputs
claims/crcns-ear-1/10.1085-jgp.201912447.yaml:1141:  data: with_inputs
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
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
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000])"
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

**Agent calls Grep**

```json
{
 "pattern": "tolerance.*(s\\.d\\.|standard error|s\\.e\\.m)|(s\\.d\\.|s\\.e\\.m\\.).*tolerance",
 "path": "claims",
 "output_mode": "content",
 "head_limit": 15
}
```

```
claims/000045/10.7554-elife.63711.yaml:412:    40. Reproduced when the mean rises and the s.d. falls, with all four values within tolerance
claims/000045/10.7554-elife.63711.yaml:506:    means. The bias tolerance is 8.4/sqrt(7), the paper's s.d. over n = 7, because 10% of a value
claims/000045/10.7554-elife.63711.yaml:664:    above chance. The accuracy tolerance is the paper's stated s.d. of the subsample distribution.
claims/000045/10.7554-elife.63711.yaml:1261:  - fig3de-threshold-bias-basic, expected. Added the reported s.d. values 3.8 and 8.4 (10% tolerance); the statement rests on them and they separate the per-mouse and per-lab readings.
claims/000253/10.1038-s41586-020-03171-x.yaml:758:    mice. The d-prime spread is read as the s.e.m. and used as its tolerance. Reproduced when,
claims/000011/10.1038-nature17643.yaml:640:    Tolerances are the paper's s.e.m. Reproduced when the cd values are within tolerance under a
claims/000011/10.1038-nature17643.yaml:955:  - Open. ed7e-roc-larger-photoinhibition, the legend prints the bilateral s.e.m. as 0.8; the tolerance 0.08 assumes a dropped zero, which the text cannot confirm (the 10% default would be 0.054).
claims/001187/10.1016-j.neuron.2024.09.013.yaml:164:    tolerances are the standard errors of the mean (the stated SD over the square root of 46), since
claims/001266/10.1038-s41467-025-55819-9.yaml:994:    within tolerance (tolerances are the paper's s.d. or 10%).
claims/001326/10.1126-science.adt3971.yaml:59:# Tolerances. Where table S3 gives mean +- s.e.m., the tolerance is 1.96 x s.e.m., the paper's own
claims/000008/10.1038-s41586-020-2907-3.yaml:929:    of about 1,300 cells, so the tolerance is 0.05, about one standard error (1 over the
claims/dryad-bvq83bkk9/10.1098-rspb.2024.2556.yaml:63:#   criteria, and the posterior means, with the reported s.d. as tolerance, under expected.
claims/001361/10.1038-s41593-025-01985-4.yaml:52:# Tolerances. A value given as mean +/- s.e.m. takes the s.e.m. as its toleranc
[... 4 more lines not kept]
```

**Agent**

I have what I need from the text. Opening one PDF page to confirm which comparison the Fig. 8d P values (0.55, 0.02) label, since the text garbles the panel.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4412.pdf",
 "pages": "9"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1038-nn.4412.pdf')
p=d[8]
for b in p.get_text('dict')['blocks']:
  for l in b.get('lines',[]):
    t=''.join(s['text'] for s in l['spans'])
    if 'P =' in t or t.strip() in ('NW','W','Control','eNpHR stimulation','L4 excitatory neurons'): print(round(l['bbox'][0]),round(l['bbox'][1]),t)
pix=p.get_pixmap(dpi=110, clip=fitz.Rect(0,0,612,420)); pix.save('p9.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-ssc-7/10.1038-nn.4412.yaml",
 "content": "# Claims for Yu, Gutnisky, Hires & Svoboda (2016), \"Layer 4 fast-spiking interneurons filter\n# thalamocortical signals during active somatosensation\", Nat Neurosci 19(12), 1647-1657,\n# doi:10.1038/nn.4412, on CRCNS ssc-7 (doi:10.6080/K0T43R01).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-06,\n# protocol as stated in docs/protocol.md (version pilot-13), Reader steps 1 to 4.\n#\n# Text read: the version of record (PDF supplied by a person, extracted to text), its main text,\n# figure legends and Online Methods, with the supplement (41593_2016_BFnn4412_MOESM61_ESM.pdf), the\n# legends of Supplementary Figures 1 to 14 and Supplementary Tables 1 (mice) and 2 (mouse lines and\n# cell counts by recording method). The supplementary videos are not text and were not used. The\n# PDF pages could not be rendered here (no renderer installed), so no figure was read as an image;\n# values printed only inside figure panels were not claimed, except where the text extraction\n# keeps them and says which comparison they label.\n#\n# Code read: none. The paper's only code statement is \"Data and code related to this study are\n# available at http://crcns.org/ at http://doi.org/10.6080/K0T43R01\", which is this dataset. The\n# data descriptor says the code is the dataset's folder \"example_analysis_code\". That folder is one\n# of the dataset's files, which a reader does not open, so every method below is taken from the\n# paper alone; the author may read that code and cite it for a detail the claims file leaves open.\n# The data descriptor (ssc-7, version 0.6, and unit_names.txt) was read only to know what the\n# dataset holds; no claim comes from it.\n#\n# The data the paper used, as it reports them. Head-fixed mice performing a lick/no-lick pole\n# localization task with 1 to 3 whiskers of one row (Results, paragraph 1; Online Methods,\n# Behavior). Pole in an anterior (no-lick) or one of several posterior (lick) locations; a sample\n# epoch of at least 1.1 s; whisker video at 1,000 fps for 5 s per trial, tracked with the Janelia\n# Whisker Tracker (whisker angle, curvature change, touch onsets and offsets); licks. Only\n# touches by the principal whisker are analysed. Recordings, by cell type (Results; Supplementary\n# Table 2):\n#   VPM. 29 single units from chronic 32-channel silicon probes in 6 VGAT-ChR2-EYFP mice, sampled\n#   at 19,531.25 Hz, spike sorted (Figs. 1, 5; Supplementary Figs. 1, 2). Example units 14.3.244,\n#   8.2.99 and 2.3.95. 17 thalamic multiunit recordings with patch pipettes during TRN\n#   photostimulation (Fig. 6b,c).\n#   L4 excitatory (E) neurons. 37 whole-cell recordings in control mice (Figs. 2, 3, 5;\n#   Supplementary Figs. 3 to 5), 6 of them with depolarizing current injection (Fig. 3); 48\n#   loose-seal cell-attached recordings; 85 in all for spiking (Fig. 5). 40 neurons (cell-attached\n#   and whole-cell) in PV-IRES-Cre mice expressing eNpHR3.0 in PV cells, with and without yellow\n#   light (Fig. 8). Whole-cell recordings during thalamic photoinhibition (Supplementary Fig. 9,\n#   n = 12). After infraorbital nerve (ION) transection, 8 to 10 whole-cell L4 E neurons (Fig. 7b\n#   to e, Supplementary Fig. 11). Example neurons E No. 1, 24 and 32 (whole-cell) and cell-attached\n#   No. 1 to 3.\n#   L4 fast-spiking (FS) interneurons. 26 neurons, 7 whole-cell (Fig. 4) and the rest\n#   cell-attached, identified by ChR2 tagging in VGAT-ChR2-EYFP mice, by eNpHR inactivation in\n#   PV-IRES-Cre mice (4) or by spike waveform (Online Methods, Barrel cortex recordings; Figs. 4, 5;\n#   Supplementary Figs. 6, 7). FS neurons during thalamic photoinhibition (13 to 15, Fig. 6d,e). 10\n#   FS neurons after ION transection (Fig. 7f to i).\n#   Whole-cell Vm sampled at 10 or 20 kHz. Laser trials (ChR2 tagging pulses; 100 Hz 5 ms pulses\n#   to TRN axons in VPM, 25 to 50% of trials; constant 594 nm light for eNpHR).\n#   Behavior across sessions (Online Methods, Behavior, paragraph 2) and PV suppression in 8 mice\n#   (Supplementary Fig. 14). Rabies tracing (Supplementary Fig. 10) is histology.\n#   The paper disagrees with itself on two counts. L4 FS neurons are 26 in the Results and in the\n#   Online Methods (19 + 4 + 1 + 2), but 25 in the Supplementary Fig. 7 legend and in the sum of\n#   Supplementary Table 2 (5 + 1 + 1 whole-cell, 14 + 4 cell-attached). L4 E neurons after ION\n#   transection are 8 (Fig. 7b), 9 (Results, Fig. 7c,d; Supplementary Table 2) or 10\n#   (Supplementary Fig. 11). Each claim keeps the n of its own passage.\n#\n# Tolerances. A mean reported as mean +- s.d. over n neurons, trials or sessions takes as\n# tolerance the standard error derived from the paper's spread, s.d./sqrt(n), or 10% of the value\n# when that is larger: the s.d. describes the spread of neurons, not the precision of the mean, and\n# the standard error is the paper's own uncertainty on the mean. A mean +- s.e.m. takes the s.e.m.\n# Medians, single neurons' values, percentages and correlation coefficients take 10%. A count of\n# neurons or mice takes 10%, and at least 1. A reported range holds inside the range widened by 10%\n# of each bound. All tolerances are computed this way unless the claim says otherwise.\n#\n# Methods the analysis rests on, with what is open. Criteria below refer to these by label. Every\n# part is from the Online Methods (Data analysis, Statistical analysis) unless said otherwise.\n# M-STAT. \"Statistical comparisons used the Wilcoxon rank sum test (unpaired), Wilcoxon signed-rank\n#   test (paired) and Kruskal-Wallis one-way analysis of variance.\" Where a passage gives a P value\n#   without naming its test, the test is the signed-rank test for paired comparisons (the same\n#   neurons in two conditions) and the rank-sum test for unpaired ones, two-sided, as this sentence\n#   implies. Where the paper reports a finding with no test at all, a criterion fixes one from this\n#   list and says so.\n# M-TOUCH. Touches by the principal whisker only, pooled across pole locations. Intertouch interval\n#   (offset of the previous touch to onset of the next) at least 25 ms for Figs. 1 to 7 and at least\n#   10 ms for Fig. 8e. Touch PSTHs in 1 ms bins. Spikes per touch, for cortical neurons, the mean\n#   spike count 0 to 50 ms after touch onset minus 2 times the mean count 0 to 25 ms before (Fig. 5),\n#   or 4 to 20 ms after minus 0 to 16 ms before (Fig. 8e); for VPM, 0 to 25 ms after minus 0 to\n#   25 ms before. Open, whether touches with a short interval are dropped or only their windows\n#   shortened; reading, touches whose interval to the previous touch is below the minimum are\n#   dropped.\n# M-LAT. Spike latency, from touch onset to the time dPSTH/dt crosses 3 s.d. of dPSTH/dt 0 to 25 ms\n#   before touch; cells excluded whose touch PSTH never reaches 10 spikes/s in any 1 ms bin 0 to\n#   100 ms after touch, or whose dPSTH/dt never crosses. Vm latency, from touch onset to the time\n#   dVm/dt crosses 3 s.d. of dVm/dt 0 to 25 ms before touch. Open, the duration of the VPM touch\n#   response \"(25% of spike rate increase from baseline to peak)\"; reading, the time between the\n#   rising and falling crossings of baseline + 25% of (peak - baseline) on the touch PSTH, baseline\n#   the mean rate 0 to 25 ms before touch.\n# M-EPOCH. Whisker angle bandpass filtered 6 to 60 Hz (4th order Butterworth), Hilbert transform\n#   for amplitude and phase (0 most protracted, +-pi most retracted). Whisking epochs are whisking\n#   cycles whose amplitude at phase 0 exceeds 2.5 degrees, excluding +-100 ms around licks and -10\n#   to 100 ms around touches. Nonwhisking epochs are periods of at least 100 ms with amplitude\n#   below 1.25 degrees, without touch or licking. Whisking onsets (transitions) are the end of a\n#   nonwhisking epoch followed by a rise of mean amplitude of at least 2 degrees, with no touch\n#   within 250 ms; data after a later touch are set to NaN; PSTHs in 10 ms bins. Open, with\n#   readings. A cycle runs from one phase crossing of -pi to the next (the reading the phase\n#   convention implies). The margin around touches and licks for nonwhisking epochs is (a) the\n#   same as for whisking epochs, or (b) none beyond their absence. The rise of 2 degrees is\n#   measured (a) over the 250 ms after onset, the window the touch rule uses, or (b) over 100 ms,\n#   the shortest nonwhisking epoch. If the dataset holds the paper's own epoch or event times,\n#   those are used and the rebuild is a variant.\n# M-RATE. Spike rate in nonwhisking and whisking is estimated from the extracted epochs, with a\n#   bootstrap (1,000 iterations) for its 95% confidence interval. Open, how epochs are combined;\n#   readings, (a) total spikes over total epoch time, (b) the mean of per-epoch rates. In\n#   experiments with laser trials, the Fig. 5 measures use control (no laser) trials only, the\n#   reading the comparisons with photostimulation imply.\n# M-SIG. A neuron \"significantly increased\" or decreased its rate with whisking by a Wilcoxon\n#   rank-sum test (Results, paragraphs 3 and 9), at p < 0.05 (the smallest P the paper lists is\n#   0.046). Open, the samples compared; readings, (a) per-epoch spike rates of whisking against\n#   nonwhisking epochs, (b) per-trial rates in whisking against nonwhisking periods.\n# M-VM. Spikes removed by interpolating Vm from 1 ms before to 4 ms after each spike threshold;\n#   threshold where dVm/dt exceeds 3 s.d. of the trial's dVm/dt. Spike threshold per trial from a\n#   line fitted to thresholds against trial number; -42 mV for silent neurons. Open, with readings.\n#   Resting Vm, (a) mean Vm in nonwhisking epochs, spikes removed, (b) median Vm outside touch\n#   (Supplementary Fig. 9d computes resting Vm \"from Vm outside touch\"). Touch PSP amplitude, the\n#   peak of the average touch-aligned Vm (Supplementary Fig. 4 legend, \"the time of peak average\n#   touch-evoked PSP\") minus the mean 0 to 5 ms before touch, the peak sought (a) 0 to 50 ms after\n#   touch, the window of Figs. 2d and 4d, or (b) 0 to 25 ms. Whisking depolarization, from the\n#   Supplementary Fig. 4 legend, (a) mean Vm 100 to 300 ms after whisking onset minus mean 0 to\n#   200 ms before, per transition, averaged per neuron; or (b) mean Vm in whisking epochs minus\n#   mean Vm in nonwhisking epochs. The s.d. given for a single example neuron is read as the s.d.\n#   across that neuron's touches or transitions.\n# M-DTT. Distance to threshold is spike threshold minus Vm over all time, in nonwhisking, whisking\n#   and touch (4 to 50 ms after touch onset) epochs, with its 10th percentile per neuron and epoch.\n#   The \"shift toward spike threshold\" of the Results is the nonwhisking 10th percentile minus the\n#   whisking or touch 10th percentile (Fig. 2g,h). Open, whether spikes are removed first; reading,\n#   removed, as M-VM does for every Vm measure.\n# M-PHASE. Spike rate or Vm binned by whisking phase and fit with a sinusoid (Supplementary Figs.\n#   2, 3, 7) or a sum of a sinusoid and one of twice the frequency (Supplementary Fig. 7g, used when\n#   its r2 is 50% higher); coupling strength is half the peak-to-trough of the fit; r2 > 0.25 marks\n#   a good fit (Supplementary Figs. 2e, 3f, 12). Open, the number of phase bins; readings, 8 and 16\n#   equal bins over -pi to pi, both reported.\n# M-SPEC. Multitaper spectra (Chronux) of 500 ms Vm segments from nonwhisking and whisking epochs,\n#   mean removed, spikes removed, resampled to 4,096 Hz, 3 Slepian tapers (4 Hz resolution),\n#   jackknife confidence intervals.\n# M-ROC. For each trial, spikes around the first touch, or, without touch, in the sample epoch;\n#   spike counts in 250 ms before and after; the count difference as the detection variable; an ROC\n#   curve over thresholds and its AUC, touch against no-touch, computed separately for control and\n#   eNpHR trials; \"We resampled the touch or no-touch periods 5,000 times\". Open, with readings,\n#   the reference time in a no-touch trial and the resampling, (a) 5,000 reference times drawn at\n#   random within the sample epochs of no-touch trials, each giving a count difference, (b) the\n#   reference at the median first-touch time of the session's touch trials, with 5,000 bootstrap\n#   resamples of trials and the mean AUC. The touch-evoked rate of Fig. 8g,h is the mean rate 0 to\n#   250 ms after touch onset minus the mean 0 to 250 ms before (Fig. 8 legend).\n# M-LIGHT. Photostimulation measures compare laser trials with control trials. Open, the period\n#   used; readings, (a) the epochs (nonwhisking, whisking, touches) that fall within the laser-on\n#   period of laser trials, against the same epochs within the same period of control trials, (b)\n#   the epochs of whole trials. For thalamic photoinhibition, laser power varied (Supplementary\n#   Fig. 9i,j); readings, (c) all laser trials pooled, (d) the highest power only. \"To x% of\n#   control\" is read as (e) the ratio of population mean rates, laser over control, or (f) the\n#   median over neurons of the per-neuron ratio.\n#\n# Data. Every claim's test uses the paper's own recordings (data: dataset). The paper relies on no\n# outside data. Whether the dataset holds each recording type (for example the rabies histology,\n# the ION-cut L5 recordings or the behavioral sessions of Supplementary Fig. 14) is for the author\n# to find.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: ssc-7\n  doi: 10.6080/K0T43R01\npaper: doi:10.1038/nn.4412\nclaims:\n- id: behavior-performance\n  statement: Mice performed the task at 0.72 +- 0.11 correct during the cortical recordings (111\n    cells) and 0.71 +- 0.07 during the VPM recordings (29 cells); they touched the pole 5.7 +- 5.3\n    times per trial at a proximal location (4,147 trials) and 0.9 +- 3.4 times at a distal location\n    (4,173 trials), and licked 286 +- 329 ms after the first touch.\n  source: Online Methods, Behavior, paragraph 2\n  quote: Mice touched the pole at a proximal location multiple times (number of touches, 5.7 ± 5.3,\n    mean ± s.d., 4,147 trials) ... Average performance (proportion of correct trials) was 0.72 ±\n    0.11 (mean ± s.d., during the recordings of 111 cells) for cortical recordings and 0.71 ± 0.07\n    for VPM recordings\n  expected:\n  - quantity: proportion correct, cortical recordings, mean over 111 cells' sessions\n    value: 0.72\n    tolerance: 0.072\n  - quantity: proportion correct, VPM recordings, mean over 29 cells' sessions\n    value: 0.71\n    tolerance: 0.071\n  - quantity: touches per trial, proximal (lick) pole, mean\n    value: 5.7\n    tolerance: 0.57\n  - quantity: touches per trial, distal (no-lick) pole, mean\n    value: 0.9\n    tolerance: 0.09\n  - quantity: reaction time from first touch, mean\n    value: 286\n    tolerance: 28.6\n    unit: ms\n  criterion: Performance per recorded cell is the proportion of correct trials in that cell's\n    trials, averaged over cells. Touches are principal-whisker touch onsets per trial, counted over\n    all trials (M-TOUCH, without the interval rule). Reaction time is the first lick after the\n    first touch, in trials with both. Which trials count is open; readings, (a) all trials, (b)\n    control trials only, in sessions with laser trials. Reproduced when all five values are within\n    tolerance under one reading.\n- id: vpm-baseline-rate\n  statement: VPM neurons fire at substantial rates in the absence of whisker movement and touch\n    (5.1 +- 5.5 spikes/s, median 3.3, n = 29).\n  source: Results, Chronic extracellular recordings from somatosensory thalamus, paragraph 1\n  quote: Typical VPM neurons showed significant spike rates (mean ± s.d., 5.1 ± 5.5 spikes per s;\n    median, 3.3 spikes per s; n = 29 neurons), even in the absence of whisker movement and touch\n  expected:\n  - quantity: VPM nonwhisking spike rate, mean over neurons\n    value: 5.1\n    tolerance: 1.02\n    unit: spikes/s\n  - quantity: VPM nonwhisking spike rate, median over neurons\n    value: 3.3\n    tolerance: 0.33\n    unit: spikes/s\n  criterion: Rate in nonwhisking epochs (M-EPOCH, M-RATE) for each of the 29 VPM units. Reproduced\n    when both values are within tolerance under one reading.\n- id: vpm-touch-response\n  statement: VPM neurons respond to active touch with a sharp, short-latency, brief increase in\n    spike rate (0.6 +- 0.5 spikes per touch, median 0.4; latency 3.2 +- 1.0 ms, median 2.5 ms;\n    duration 2.9 +- 1.7 ms).\n  source: Results, Chronic extracellular recordings from somatosensory thalamus, paragraphs 1 and 2;\n    Fig. 1d; Supplementary Fig. 2\n  quote: showed a sharp peak in spike rate (mean ± s.d., 0.6 ± 0.5 spikes per touch; median, 0.4\n    spikes per touch), with short latency after touch onset (mean ± s.d., 3.2 ± 1.0 ms; median, 2.5\n    ms) and brief duration (2.9 ± 1.7 ms, 25% of spike rate increase from baseline to peak\n  expected:\n  - quantity: VPM spikes per touch, mean\n    value: 0.6\n    tolerance: 0.093\n  - quantity: VPM spikes per touch, median\n    value: 0.4\n    tolerance: 0.04\n  - quantity: VPM touch latency, mean\n    value: 3.2\n    tolerance: 0.32\n    unit: ms\n  - quantity: VPM touch latency, median\n    value: 2.5\n    tolerance: 0.25\n    unit: ms\n  - quantity: VPM touch response duration, mean\n    value: 2.9\n    tolerance: 0.32\n    unit: ms\n  criterion: Spikes per touch with the VPM definition (0 to 25 ms after minus 0 to 25 ms before),\n    touches with interval at least 25 ms (M-TOUCH); latency by M-LAT, over the units that pass its\n    exclusion; duration by the M-LAT reading. Reproduced when all five values are within tolerance.\n- id: vpm-whisking-count\n  statement: Most VPM neurons (25 of 29) significantly increase their spike rate during whisking\n    without touch; 3 of 29 do not increase but still respond to touch, and one decreases\n    significantly.\n  source: Results, Chronic extracellular recordings from somatosensory thalamus, paragraph 2; Fig.\n    1c,e; Supplementary Fig. 2\n  quote: Most VPM neurons increased their spike rate during whisking in the absence of touch (25 out\n    of 29 neurons ... A minority of VPM neurons (3 of 29) did not increase their spike rate with\n    whisking but still responded to touch ... One neuron showed a significant decrease in spike\n    rate during whisking (P < 0.0001)\n  expected:\n  - quantity: VPM neurons with a significant increase in whisking\n    value: 25\n    tolerance: 2.5\n  - quantity: VPM neurons without an increase\n    value: 3\n    tolerance: 1\n  - quantity: VPM neurons with a significant decrease\n    value: 1\n    tolerance: 1\n  criterion: Per neuron, whisking against nonwhisking by M-SIG, two-sided rank-sum at p < 0.05,\n    rates by M-RATE. Reproduced when the counts are within tolerance under one reading. The\n    paper's counts sum to 29 with the decreasing neuron counted apart from the 3, which the\n    notebook states; the count of neurons with no significant change is shown too.\n- id: vpm-whisking-rate\n  statement: The average VPM spike rate increases severalfold with whisker movement, from 5.1 +-\n    5.5 to 13.5 +- 12.7 spikes/s (n = 29, P = 4e-6, Wilcoxon signed-rank).\n  source: Results, Chronic extracellular recordings from somatosensory thalamus, paragraph 2; Fig.\n    5d; Supplementary Fig. 2\n  quote: The average spike rate increased severalfold after onset of whisker movement (from 5.1 ±\n    5.5 spikes per s to 13.5 ± 12.7 spikes per s; P = 4 × 10−6; n = 29 neurons, Wilcoxon signed-rank\n    test\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 4.0e-6\n    n: 29 VPM neurons\n  expected:\n  - quantity: VPM nonwhisking rate, mean\n    value: 5.1\n    tolerance: 1.02\n    unit: spikes/s\n  - quantity: VPM whisking rate, mean\n    value: 13.5\n    tolerance: 2.36\n    unit: spikes/s\n  criterion: Open, what \"after onset of whisker movement\" measures; readings, (a) rates in\n    whisking against nonwhisking epochs (M-EPOCH, M-RATE), which Fig. 5d plots and whose\n    nonwhisking mean is the 5.1 of the baseline, (b) the rate 0 to 400 ms after whisking onsets\n    against 200 ms before, the window of Fig. 1e and Supplementary Fig. 2b. Reproduced when, under\n    one reading, both means are within tolerance and a two-sided signed-rank test over the 29\n    neurons gives p < 0.05 with whisking higher.\n- id: vpm-phase-modulation\n  statement: VPM spike rate is modulated by the phase of whisker movement.\n  source: Results, Chronic extracellular recordings from somatosensory thalamus, paragraph 2;\n    Supplementary Fig. 2d to f\n  quote: The spike rate was modulated by the phase of the movement (Supplementary Fig. 2d)\n  criterion: Per neuron, whisking-epoch spike rate by phase with a sinusoid fit (M-PHASE). The\n    paper gives no count, so the rule is fixed here from its own cutoff (Supplementary Fig. 2e,\n    r2 = 0.25). Reproduced when more than half of the 29 neurons have r2 > 0.25 under one binning;\n    the distribution of coupling strength and preferred phase of those neurons is reported.\n- id: vpm-rate-amplitude-trials\n  statement: Within a single behavioral session, VPM spike rate and whisking amplitude co-vary\n    across trials (Pearson r = 0.61, P = 1e-78, 310 trials).\n  source: Supplementary Fig. 1e\n  quote: Spike rate and whisking amplitude co-vary across trials within single behavioral sessions\n    (Pearson correlation coefficient ρ=0.61; P = 10-78; number of trials n=310)\n  statistics:\n  - test: Pearson correlation\n    statistic: rho = 0.61\n    p: 1.0e-78\n    n: 310 trials of one session\n  expected:\n  - quantity: Pearson r, trial spike rate against trial whisking amplitude, example session\n    value: 0.61\n    tolerance: 0.061\n  criterion: The legend names no unit. Per trial, the unit's spike rate over the trial and the mean\n    whisking amplitude (M-EPOCH, Hilbert amplitude) over the same time. Reproduced when a VPM unit\n    recorded over a session of 310 trials gives r within tolerance and p < 0.05. If no session has\n    310 trials, the claim is tested on every VPM unit, and reproduced when most units show a\n    significant positive r; the r of each unit is reported.\n- id: l4e-example-e1\n  statement: The example L4 spiny stellate cell E No. 1 rests at -76 mV, far from its spike\n    threshold (-45.1 +- 3.7 mV); touch evokes large (14.4 +- 8.2 mV), short-latency (4.7 ms),\n    transient (24.5 ms at half max) depolarizations with 0 to 7 spikes per touch, while whisking\n    without touch causes a smaller sustained depolarization (6.7 +- 4.0 mV) with little increase\n    in spike rate (0.4 spikes/s).\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 1; Fig. 2a to e\n  quote: The neuron rested at a hyperpolarized potential (−76 mV) far from the spike threshold (mean\n    ± s.d., −45.1 ± 3.7 mV). Active touch evoked large-amplitude (14.4 ± 8.2 mV), short-latency (4.7\n    ms) and transient (duration at half max, 24.5 ms) depolarizations that often triggered spikes\n    (0–7 spikes per touch). In the absence of touch, whisking caused a sustained smaller\n    depolarization (6.7 ± 4.0 mV)\n  expected:\n  - quantity: E No. 1 resting Vm\n    value: -76\n    tolerance: 7.6\n    unit: mV\n  - quantity: E No. 1 spike threshold, mean over spikes\n    value: -45.1\n    tolerance: 4.51\n    unit: mV\n  - quantity: E No. 1 touch PSP amplitude, mean over touches\n    value: 14.4\n    tolerance: 1.44\n    unit: mV\n  - quantity: E No. 1 touch PSP latency\n    value: 4.7\n    tolerance: 0.47\n    unit: ms\n  - quantity: E No. 1 touch PSP duration at half max\n    value: 24.5\n    tolerance: 2.45\n    unit: ms\n  - quantity: E No. 1 whisking depolarization, mean over transitions\n    value: 6.7\n    tolerance: 0.67\n    unit: mV\n  - quantity: E No. 1 whisking increase in spike rate\n    value: 0.4\n    tolerance: 0.04\n    unit: spikes/s\n  criterion: The neuron is the one the dataset's cell list names E No. 1 (Fig. 2). Resting Vm,\n    touch amplitude and whisking depolarization by M-VM; threshold by M-VM, mean over spikes;\n    latency by M-LAT on the average touch-aligned Vm; duration at half max, the width of the\n    average touch PSP at half its amplitude. Spikes per touch counted 0 to 50 ms after each touch,\n    range over touches. The rate increase is the whisking minus the nonwhisking rate (M-RATE).\n    Reproduced when, under one reading, at least six of the seven values are within tolerance and\n    the spike count range is 0 to 7 within one spike.\n- id: l4e-example-e24-e32\n  statement: In the more depolarized example neurons, whisking causes a small depolarization (1.0\n    +- 1.4 mV, E No. 24) or a hyperpolarization (-1.8 +- 2.7 mV, E No. 32).\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 1; Fig. 2d,e\n  quote: For these neurons, whisking caused either small membrane potential depolarization (1.0 ±\n    1.4 mV, No. 24) or hyperpolarization (−1.8 ± 2.7 mV, No. 32)\n  expected:\n  - quantity: E No. 24 whisking Vm change\n    value: 1.0\n    tolerance: 0.1\n    unit: mV\n  - quantity: E No. 32 whisking Vm change\n    value: -1.8\n    tolerance: 0.18\n    unit: mV\n  criterion: Whisking depolarization by M-VM for the neurons the cell list names E No. 24 and 32.\n    Reproduced when both values are within tolerance under one reading; partially reproduced when\n    both have the stated sign but a value lies outside tolerance.\n- id: l4e-resting-vm\n  statement: The resting membrane potential of L4 excitatory neurons spans a large range, -76 to\n    -45 mV (mean -63 +- 8 mV, median -64 mV, n = 37).\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 2; Fig. 2f\n  quote: Across the excitatory population, the resting membrane potential (Vm) spanned a large range\n    (−76 to −45 mV, mean ± s.d., −63 ± 8 mV; median, −64 mV, n = 37 neurons\n  expected:\n  - quantity: lowest resting Vm\n    value: -76\n    tolerance: 7.6\n    unit: mV\n  - quantity: highest resting Vm\n    value: -45\n    tolerance: 4.5\n    unit: mV\n  - quantity: mean resting Vm\n    value: -63\n    tolerance: 6.3\n    unit: mV\n  - quantity: median resting Vm\n    value: -64\n    tolerance: 6.4\n    unit: mV\n  criterion: Resting Vm by M-VM for the 37 whole-cell L4 E neurons in control mice. Reproduced when\n    all four values are within tolerance under one reading.\n- id: l4e-touch-psp\n  statement: Touch evokes short-latency depolarizations in every L4 excitatory neuron (latency 4.8\n    +- 0.8 ms, median 4.7; amplitude 6.0 +- 2.9 mV, median 5.7; n = 37).\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 2; Fig. 2f;\n    Supplementary Fig. 3a\n  quote: Touches evoked short-latency depolarizations (latency, mean ± s.d., 4.8 ± 0.8 ms; median,\n    4.7 ms; amplitude, mean ± s.d., 6.0 ± 2.9 mV; median, 5.7 mV; n = 37 neurons) for all neurons\n  expected:\n  - quantity: touch PSP latency, mean\n    value: 4.8\n    tolerance: 0.48\n    unit: ms\n  - quantity: touch PSP latency, median\n    value: 4.7\n    tolerance: 0.47\n    unit: ms\n  - quantity: touch PSP amplitude, mean\n    value: 6.0\n    tolerance: 0.6\n    unit: mV\n  - quantity: touch PSP amplitude, median\n    value: 5.7\n    tolerance: 0.57\n    unit: mV\n  criterion: Latency by M-LAT and amplitude by M-VM on each neuron's average touch-aligned Vm\n    (M-TOUCH). Reproduced when the four values are within tolerance under one reading and every\n    neuron's amplitude is positive.\n- id: l4e-whisking-vm\n  statement: Whisking induces only a small depolarization or hyperpolarization in L4 excitatory\n    neurons (1.2 +- 2.1 mV, median 1.2 mV).\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 2; Fig. 2f\n  quote: Whisking induced small depolarization or hyperpolarization (mean ± s.d., 1.2 ± 2.1 mV;\n    median, 1.2 mV; Fig. 2f)\n  expected:\n  - quantity: whisking Vm change, mean over 37 neurons\n    value: 1.2\n    tolerance: 0.35\n    unit: mV\n  - quantity: whisking Vm change, median\n    value: 1.2\n    tolerance: 0.12\n    unit: mV\n  criterion: Whisking depolarization by M-VM over the 37 neurons. Reproduced when both values are\n    within tolerance under one reading.\n- id: l4e-distance-threshold\n  statement: Touch moves the membrane potential of L4 excitatory neurons much closer to spike\n    threshold than whisking does (shift 6.1 +- 3.2 mV against 1.1 +- 2.0 mV, P = 1e-7, Wilcoxon\n    signed-rank).\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 2; Fig. 2g,h\n  quote: Compared to whisking, touch caused a larger shift of membrane potential toward spike\n    threshold (whisking, 1.1 ± 2.0 mV; touch, 6.1 ± 3.2 mV; P = 1 × 10−7, Wilcoxon signed-rank test\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 1.0e-7\n    n: 37 L4 excitatory neurons\n  expected:\n  - quantity: whisking shift of 10th-percentile distance to threshold, mean\n    value: 1.1\n    tolerance: 0.33\n    unit: mV\n  - quantity: touch shift of 10th-percentile distance to threshold, mean\n    value: 6.1\n    tolerance: 0.61\n    unit: mV\n  criterion: Shifts by M-DTT, threshold by M-VM. Reproduced when both means are within tolerance\n    and a two-sided signed-rank test of touch against whisking shifts over the 37 neurons gives p\n    < 0.05 with touch larger.\n- id: l4e-reversal-potential\n  statement: The effective reversal potential of the touch response in L4 excitatory neurons is\n    more depolarized than resting Vm, while that of the whisking response is close to resting Vm\n    and more hyperpolarized than that of touch.\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 2;\n    Supplementary Fig. 4\n  quote: The effective reversal potential29 of the touch response was more depolarized than the\n    resting Vm and sometimes crossed the spike threshold (Supplementary Fig. 4). In contrast, the\n    effective reversal potential for whisker movement was close to the resting Vm, below the spike\n    threshold and more hyperpolarized than that for touch\n  criterion: From the Supplementary Fig. 4 legend. Per touch, pre-Vm the mean 0 to 5 ms before\n    onset and post-Vm at the time of the neuron's peak average PSP; per whisking onset, pre-Vm the\n    mean 0 to 200 ms before and post-Vm the mean 100 to 300 ms after. A line fitted to delta Vm\n    against pre-Vm per neuron and event type; the reversal potential is where it crosses zero. Open\n    whether one line is fitted per neuron or one over all neurons (Supplementary Fig. 4b shows\n    \"all neurons\"); readings, (a) per neuron, (b) pooled, both reported. The paper names no test,\n    so one is fixed from M-STAT. Reproduced when, per neuron, the touch reversal exceeds the\n    whisking reversal by a two-sided signed-rank test at p < 0.05, the touch reversal exceeds\n    resting Vm in most neurons, and the median whisking reversal lies within 5 mV of the median\n    resting Vm (a margin fixed here, as the paper gives none). Neurons whose fit has a\n    non-negative slope have no crossing and are counted and left out.\n- id: l4e-hf-fluctuations\n  statement: Whisking enhances membrane potential fluctuations of L4 excitatory neurons at high\n    frequencies (above 10 Hz).\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 2; Supplementary\n    Fig. 5\n  quote: and enhanced membrane potential fluctuations at high frequencies (>10 Hz; Supplementary\n    Fig. 5)\n  criterion: Spectra by M-SPEC per neuron in nonwhisking and whisking epochs. The paper names no\n    test or upper frequency, so these are fixed here; readings, mean power (a) 10 to 100 Hz, (b) 10\n    to 500 Hz. Reproduced when, under one reading, whisking power exceeds nonwhisking power by a\n    two-sided signed-rank test over the 37 neurons at p < 0.05. The number of neurons whose\n    jackknife 95% intervals separate above 10 Hz is reported.\n- id: l4e-inhibition-window\n  statement: In L4 excitatory neurons depolarized near the excitatory reversal potential, touch\n    evokes strong transient inhibition that follows excitation with a short delay (0.4 +- 0.8 ms at\n    half max, range -0.8 to 1.6 ms, n = 6).\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 3; Fig. 3b to d;\n    Discussion, paragraph 3\n  quote: Touch elicited strong and transient inhibitory input (Fig. 3b,c), which followed excitation\n    with a short delay (mean ± s.d., 0.4 ± 0.8 ms at half max; n = 6 neurons; Fig. 3d)\n  expected:\n  - quantity: delay of inhibition after excitation at half max, mean over 6 neurons\n    value: 0.4\n    tolerance: 0.33\n    unit: ms\n  - quantity: smallest delay\n    value: -0.8\n    tolerance: 0.08\n    unit: ms\n  - quantity: largest delay\n    value: 1.6\n    tolerance: 0.16\n    unit: ms\n  criterion: For each of the 6 neurons, touch-aligned averages (M-TOUCH) at rest and during\n    depolarizing current injection (Online Methods, Barrel cortex recordings, paragraph 3, for the\n    depolarized state near 0 mV). Each average is normalized to its peak (Fig. 3d); the delay is\n    the time the depolarized average reaches half its negative peak minus the time the resting\n    average reaches half its positive peak. Reproduced when the mean is within tolerance and both\n    extremes lie within the range widened by 10% of each bound (the range is from the Discussion,\n    paragraph 3).\n- id: l4e-whisking-inhibition\n  statement: Without touch, inhibitory input in L4 excitatory neurons is more prevalent at the\n    onset of whisker movement, and after onset excitation and inhibition increase gradually with\n    indistinguishable time courses over about 100 ms.\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 3; Fig. 3e to g\n  quote: In the absence of touch, inhibitory inputs occurred spontaneously but were more prevalent\n    at onset of whisker movement (Fig. 3e,f) ... After the onset of whisker movement, excitation\n    and inhibition increased gradually, with indistinguishable time courses, over approximately 100\n    ms (Fig. 3g)\n  criterion: For the 6 neurons, whisking-onset averages (M-EPOCH) at rest and depolarized. The\n    paper names no test; one is fixed here from M-STAT. Inhibition at onset, the depolarized\n    average 0 to 200 ms after onset falls below its mean 0 to 200 ms before, by a two-sided\n    signed-rank test over the 6 neurons or in at least 5 of 6. Time course, each average\n    normalized to its mean 100 to 300 ms after onset; the time to half of that level lies between\n    0 and 150 ms for both, and the two times do not differ by a two-sided signed-rank test (p >=\n    0.05). Reproduced when both parts hold.\n- id: fs-baseline-rate\n  statement: L4 FS interneurons are active at baseline, even without whisker movement (9.3 +- 8.5\n    spikes/s, median 6.4, n = 26).\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 1; Figs. 4b,c and 5\n  quote: FS interneurons were active during baseline conditions, even in the absence of whisker\n    movements (mean ± s.d., 9.3 ± 8.5 spikes per s; median, 6.4 spikes per s; n = 26 neurons\n  expected:\n  - quantity: FS nonwhisking rate, mean\n    value: 9.3\n    tolerance: 1.67\n    unit: spikes/s\n  - quantity: FS nonwhisking rate, median\n    value: 6.4\n    tolerance: 0.64\n    unit: spikes/s\n  criterion: Nonwhisking rate (M-EPOCH, M-RATE) for the L4 FS neurons of control mice. Reproduced\n    when both values are within tolerance under one reading. The paper gives 26 neurons and 25 (see\n    the opening comment); the notebook uses the neurons the dataset marks as L4 FS in control mice\n    and reports their number.\n- id: fs-touch-vm\n  statement: Touch depolarizes L4 FS interneurons (7.0 +- 5.2 mV, median 6.7 mV, n = 7) with short\n    onset latency (4.0 +- 0.6 ms, median 4.2 ms).\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 1; Fig. 4d,f\n  quote: Membrane potential depolarized (mean ± s.d., 7.0 ± 5.2 mV; median, 6.7 mV; n = 7 neurons,\n    Fig. 4d,f) ... Response latencies were short for membrane potential depolarization (onset,\n    mean ± s.d., 4.0 ± 0.6 ms; median, 4.2 ms, n = 7 neurons\n  expected:\n  - quantity: FS touch PSP amplitude, mean\n    value: 7.0\n    tolerance: 1.97\n    unit: mV\n  - quantity: FS touch PSP amplitude, median\n    value: 6.7\n    tolerance: 0.67\n    unit: mV\n  - quantity: FS touch PSP latency, mean\n    value: 4.0\n    tolerance: 0.4\n    unit: ms\n  - quantity: FS touch PSP latency, median\n    value: 4.2\n    tolerance: 0.42\n    unit: ms\n  criterion: Amplitude by M-VM and latency by M-LAT on the 7 whole-cell FS neurons. Reproduced\n    when all four values are within tolerance under one reading.\n- id: fs-touch-spikes\n  statement: L4 FS interneurons fire about two spikes per touch (1.9 +- 1.0, median 1.9, n = 26)\n    with short latency (5.3 +- 2.1 ms, median 4.5 ms, n = 24).\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 1; Fig. 5b,c\n  quote: spike rates increased after touch (mean ± s.d., 1.9 ± 1.0 spikes per touch; median, 1.9\n    spikes per touch; n = 26 neurons ... and spiking (mean ± s.d., 5.3 ± 2.1 ms; median, 4.5 ms, n =\n    24 neurons; Fig. 5c)\n  expected:\n  - quantity: FS spikes per touch, mean\n    value: 1.9\n    tolerance: 0.2\n  - quantity: FS spikes per touch, median\n    value: 1.9\n    tolerance: 0.19\n  - quantity: FS spike latency, mean\n    value: 5.3\n    tolerance: 0.53\n    unit: ms\n  - quantity: FS spike latency, median\n    value: 4.5\n    tolerance: 0.45\n    unit: ms\n  - quantity: FS neurons passing the latency exclusion\n    value: 24\n    tolerance: 2.4\n  criterion: Spikes per touch with the cortical Fig. 5 definition (M-TOUCH); latency by M-LAT.\n    Reproduced when all five values are within tolerance.\n- id: fs-whisking-count\n  statement: Most L4 FS neurons (23 of 26) significantly increase their spike rate during whisker\n    movement without touch, and the rest (3 of 26) decrease it.\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 2\n  quote: most L4 FS neurons significantly increased their spike rate during whisker movement without\n    touch (23 of 26 neurons ... and a small subset (3 of 26 neurons, P ranged from 0.011 to 4.7 ×\n    10−6) decreased spike rate\n  expected:\n  - quantity: FS neurons with a significant increase\n    value: 23\n    tolerance: 2.3\n  - quantity: FS neurons with a significant decrease\n    value: 3\n    tolerance: 1\n  criterion: Per neuron by M-SIG. Reproduced when both counts are within tolerance under one\n    reading.\n- id: fs-whisking-vm\n  statement: After whisking onset the membrane potential of L4 FS neurons depolarizes toward spike\n    threshold (2.7 +- 2.1 mV, median 2.4 mV, n = 7).\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 2; Fig. 4e to h\n  quote: Overall, after onset of whisking, the membrane potential of FS neurons depolarized closer to\n    spike threshold (mean ± s.d., 2.7 ± 2.1 mV; median, 2.4 mV, n = 7 neurons\n  expected:\n  - quantity: FS whisking depolarization, mean\n    value: 2.7\n    tolerance: 0.79\n    unit: mV\n  - quantity: FS whisking depolarization, median\n    value: 2.4\n    tolerance: 0.24\n    unit: mV\n  criterion: Whisking depolarization by M-VM for the 7 whole-cell FS neurons. Open whether the\n    figure's measure, the shift of 10th-percentile distance to threshold (M-DTT, Fig. 4h), is\n    meant; it is reading (c). Reproduced when both values are within tolerance under one reading.\n- id: fs-whisking-rate\n  statement: With whisking the L4 FS spike rate doubles (to 21.1 +- 15.8 spikes/s, median 14.6, n =\n    26, P = 2.7e-5).\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 2; Fig. 5d\n  quote: and the spike rate doubled (mean ± s.d., 21.1 ± 15.8 spikes per s; median, 14.6 spikes per\n    s, n = 26 neurons, P = 2.7 × 10−5; Fig. 5d)\n  statistics:\n  - test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 2.7e-5\n    n: 26 L4 FS neurons\n  expected:\n  - quantity: FS whisking rate, mean\n    value: 21.1\n    tolerance: 3.1\n    unit: spikes/s\n  - quantity: FS whisking rate, median\n    value: 14.6\n    tolerance: 1.46\n    unit: spikes/s\n  criterion: Whisking-epoch rates (M-EPOCH, M-RATE) against the nonwhisking rates of\n    fs-baseline-rate, two-sided signed-rank (M-STAT). Reproduced when both values are within\n    tolerance, the test gives p < 0.05 with whisking higher, and the ratio of mean whisking to\n    mean nonwhisking rate lies between 1.8 and 2.5 (doubled, read with the 10% rule on 2 and a\n    margin for the paper's own ratio of 21.1 to 9.3, 2.27).\n  depends_on:\n  - fs-baseline-rate\n- id: fs-phase-coupling\n  statement: L4 FS spikes are coupled to whisking phase; the phase relation is fit by a single\n    sinusoid in 18 neurons and needs a second harmonic in 7 (n = 25).\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 2; Supplementary Fig. 7g\n  quote: Coupling between the spikes of L4 FS interneurons and the whisking phase was either fit with\n    a single sinusoidal function (left, n=18) or a sum of a single sinusoidal function (black) and a\n    sinusoidal function of twice the frequency (purple) (right, n=7) if the fitting quality (r2)\n    was 50% higher than with only a single sinusoidal function\n  expected:\n  - quantity: FS neurons fit by a single sinusoid\n    value: 18\n    tolerance: 1.8\n  - quantity: FS neurons fit by a sum with the second harmonic\n    value: 7\n    tolerance: 1\n  criterion: By M-PHASE on whisking-epoch spikes. Reproduced when both counts are within tolerance\n    under one binning.\n- id: l4e-spikes-touch-selective\n  statement: L4 excitatory neurons respond mostly to touch (0.3 +- 0.4 spikes per touch, median 0.1,\n    n = 85) and only weakly to whisker movement, with no significant change between nonwhisking\n    (0.4 +- 0.6 spikes/s, median 0.1) and whisking (0.6 +- 0.9 spikes/s, median 0.2; P = 0.20).\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 3; Fig. 5b,d,e; Fig. 1f to j\n  quote: Excitatory neurons responded mostly to touch (mean ± s.d., 0.3 ± 0.4 spikes per touch;\n    median, 0.1 spikes per touch; n = 85 neurons; Fig. 5b,d) and showed weak response to whisker\n    movement (nonwhisking, mean ± s.d., 0.4 ± 0.6 spikes per s; median, 0.1 spikes per s; whisking,\n    mean ± s.d., 0.6 ± 0.9 spikes per s; median, 0.2 spikes per s; n = 85, P = 0.20\n  statistics:\n  - test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 0.2\n    n: 85 L4 excitatory neurons\n  expected:\n  - quantity: L4 E spikes per touch, mean\n    value: 0.3\n    tolerance: 0.043\n  - quantity: L4 E spikes per touch, median\n    value: 0.1\n    tolerance: 0.01\n  - quantity: L4 E nonwhisking rate, mean\n    value: 0.4\n    tolerance: 0.065\n    unit: spikes/s\n  - quantity: L4 E nonwhisking rate, median\n    value: 0.1\n    tolerance: 0.01\n    unit: spikes/s\n  - quantity: L4 E whisking rate, mean\n    value: 0.6\n    tolerance: 0.098\n    unit: spikes/s\n  - quantity: L4 E whisking rate, median\n    value: 0.2\n    tolerance: 0.02\n    unit: spikes/s\n  criterion: The 85 L4 E neurons of Fig. 5 (37 whole-cell and 48 cell-attached in Supplementary\n    Table 2, control trials only by M-RATE). Spikes per touch with the cortical Fig. 5 definition\n    (M-TOUCH); rates by M-EPOCH and M-RATE. The values are matched under one reading. The absence\n    of a whisking effect is judged on the paper's test as M-STAT reads it, a two-sided signed-rank\n    test of whisking against nonwhisking rates over the 85 neurons at p < 0.05; reproduced when the\n    values are within tolerance and that test is not significant, not reproduced when it is\n    significant. The median and mean whisking minus nonwhisking difference is reported either way.\n- id: thalamus-inhibition-vpm\n  statement: Photoactivating TRN axons in VPM reduces thalamic activity to 17% of control (P =\n    3e-4, n = 17 multiunit recordings).\n  source: Results, Inhibition is driven by thalamus, paragraph 1; Fig. 6b,c\n  quote: Photoactivation of TRN axons reduced activity in the thalamus (to 17% of control, P = 3 ×\n    10−4, n = 17 multiunit recordings\n  statistics:\n  - test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 3.0e-4\n    n: 17 thalamic multiunit recordings\n  expected:\n    quantity: thalamic multiunit rate under photoinhibition, percent of control\n    value: 17\n    tolerance: 1.7\n    unit: percent\n  criterion: Multiunit rates in laser and control trials by M-LIGHT; Supplementary Fig. 9i says\n    these rates are not split by behavioral epoch. Reproduced when, under one reading, the\n    percentage is within tolerance and a two-sided signed-rank test over the 17 recordings gives p\n    < 0.05 with lower rates under photoinhibition.\n- id: thalamus-inhibition-l4e-vm\n  statement: Thalamic photoinhibition hyperpolarizes L4 excitatory neurons and reduces their Vm\n    fluctuations, with an onset latency of 4.2 ms, longer than the 2.8 ms of direct cortical\n    GABAergic activation.\n  source: Results, Inhibition is driven by thalamus, paragraph 1; Supplementary Fig. 9b to f\n  quote: photoinhibition of thalamus hyperpolarized excitatory neurons and reduced the amplitudes of\n    their membrane voltage fluctuations (Supplementary Fig. 9a–e). Onset latency of Vm\n    hyperpolarization induced by thalamus inactivation was 4.2 ms. This was longer than the 2.8-ms\n    latency measured with direct cortical GABAergic activation\n  expected:\n  - quantity: onset latency of hyperpolarization, thalamic photoinhibition\n    value: 4.2\n    tolerance: 0.42\n    unit: ms\n  - quantity: onset latency of hyperpolarization, direct cortical GABAergic activation\n    value: 2.8\n    tolerance: 0.28\n    unit: ms\n  criterion: For the 12 L4 E neurons of Supplementary Fig. 9c to e, resting Vm outside touch and\n    the variance of Vm high-pass filtered at 10 Hz, outside touch, in laser and control trials\n    (Supplementary Fig. 9d,e legend). The paper names no test; one is fixed from M-STAT, a\n    two-sided signed-rank test at p < 0.05 for lower Vm and lower variance. Latency on the grand\n    average Vm aligned to laser onset (Supplementary Fig. 9c, and 9f for the 7 neurons with direct\n    cortical stimulation), by the M-LAT Vm rule with the 25 ms before laser onset as baseline, a\n    rule adapted here from the touch latency since the paper does not define this one. Reproduced\n    when both tests hold and both latencies are within tolerance; partially reproduced when the\n    tests hold and the thalamic latency exceeds the cortical one without both being in tolerance.\n- id: thalamus-inhibition-fs\n  statement: Thalamic photoinhibition reduces L4 FS spike rates during nonwhisking (to 4% of\n    control, n = 13), whisking (to 13%, n = 15) and touch (to 32%, n = 14).\n  source: Results, Inhibition is driven by thalamus, paragraph 2; Fig. 6d,e\n  quote: Photoinhibition reduced spike rates in FS interneurons during nonwhisking (to 4% of control,\n    P = 5 × 10−4, n = 13 neurons) and whisking epochs (to 13% of control, P = 6 × 10−5, n = 15\n    neurons), as well as in response to touch (to 32% of control, P = 1 × 10−4, n = 14 neurons\n  statistics:\n  - about: nonwhisking rate, photoinhibition against control\n    test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 5.0e-4\n    n: 13 L4 FS neurons\n  - about: whisking rate, photoinhibition against control\n    test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 6.0e-5\n    n: 15 L4 FS neurons\n  - about: spikes per touch, photoinhibition against control\n    test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 1.0e-4\n    n: 14 L4 FS neurons\n  expected:\n  - quantity: FS nonwhisking rate under photoinhibition, percent of control\n    value: 4\n    tolerance: 0.4\n    unit: percent\n  - quantity: FS whisking rate under photoinhibition, percent of control\n    value: 13\n    tolerance: 1.3\n    unit: percent\n  - quantity: FS touch response under photoinhibition, percent of control\n    value: 32\n    tolerance: 3.2\n    unit: percent\n  criterion: FS neurons recorded with thalamic photoinhibition, rates by M-EPOCH and M-RATE and\n    spikes per touch by M-TOUCH (Fig. 5 definition), in laser against control trials by M-LIGHT.\n    The differing n per epoch are read as the neurons with enough of that epoch in both trial\n    types; the notebook reports its own n. Reproduced when, under one reading, all three\n    percentages are within tolerance and each two-sided signed-rank test gives p < 0.05 with lower\n    activity under photoinhibition; partially reproduced when the three tests hold and not all\n    percentages are within tolerance.\n- id: thalamus-inhibition-dose\n  statement: The reduction of L4 FS spiking by thalamic photoinhibition is dose dependent, as is\n    the reduction of VPM multiunit rates.\n  source: Results, Inhibition is driven by thalamus, paragraph 2; Supplementary Fig. 9i,j\n  quote: in a dose-dependent manner (Supplementary Fig. 9i,j)\n  criterion: Rates by laser power, per behavioral epoch for FS neurons and unsplit for multiunits\n    (Supplementary Fig. 9i,j legend). The paper names no test; fixed here, a Spearman correlation\n    between laser power (control as zero) and rate per neuron, and a two-sided signed-rank test\n    over neurons of the correlations against zero. Reproduced when the test gives p < 0.05 with\n    negative correlations for FS neurons in at least two of the three epochs.\n- id: rabies-vpm-input\n  statement: Monosynaptic rabies tracing from L4 PV interneurons labels thalamic neurons mostly in\n    VPM (over 90%) and few in POM (under 10%).\n  source: Results, Inhibition is driven by thalamus, paragraph 3; Supplementary Fig. 10\n  quote: The vast majority of trans-synaptically labeled thalamic neurons were in VPM (>90%), with\n    only a small minority in POM (<10%; Supplementary Fig. 10)\n  criterion: Counts of GFP-labeled neurons in VPM and POM across sections (Online Methods, Virus\n    injection, paragraph 2). Reproduced when the VPM share exceeds 90%.\n- id: ion-cut-behavior\n  statement: After ION transection mice still whisk but perform the task at chance (48% correct).\n  source: Results, Inhibition is driven by sensory input, paragraph 2\n  quote: however, as they were unable to sense the object, they performed at chance level (48%\n    correct)\n  expected:\n    quantity: proportion correct after ION transection\n    value: 0.48\n    tolerance: 0.048\n  criterion: Proportion of correct trials in sessions after ION transection. Open, the unit of\n    averaging; readings, (a) pooled over all trials, (b) mean over sessions or recorded cells as\n    in behavior-performance. Reproduced when the value is within tolerance under one reading.\n- id: ion-cut-l4e-touch\n  statement: After ION transection L4 excitatory neurons do not depolarize after touch.\n  source: Results, Inhibition is driven by sensory input, paragraph 2; Fig. 7b\n  quote: As expected, L4 excitatory neurons did not depolarize after touch (Fig. 7b)\n  criterion: A claim of absence. Touch PSP amplitude by M-VM and M-TOUCH for the ION-cut L4 E\n    neurons (8 in Fig. 7b). The paper names no test; fixed from M-STAT, a two-sided signed-rank\n    test of the amplitude against zero over neurons at p < 0.05. Reproduced when it is not\n    significant, not reproduced when it is significant with positive amplitudes. The mean amplitude\n    is reported beside the control value of l4e-touch-psp.\n- id: ion-cut-l4e-whisking\n  statement: After ION transection whisking-related depolarization of L4 excitatory neurons is\n    reduced (0.62 +- 0.50 mV, n = 9, against 1.54 +- 0.79 mV in 15 control neurons with matched\n    resting potential; P = 0.005, Wilcoxon rank-sum).\n  source: Results, Inhibition is driven by sensory input, paragraph 2; Fig. 7c,d\n  quote: Depolarizations in response to whisker movement were reduced (ION cut, mean ± s.d., 0.62 ±\n    0.50 mV, n = 9 neurons versus Control with matched resting potential, mean ± s.d., 1.54 ± 0.79\n    mV, n = 15 neurons; P = 0.005, Wilcoxon rank-sum test\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.005\n    n: 9 ION-cut and 15 control L4 excitatory neurons\n  expected:\n  - quantity: whisking depolarization, ION cut, mean\n    value: 0.62\n    tolerance: 0.17\n    unit: mV\n  - quantity: whisking depolarization, matched controls, mean\n    value: 1.54\n    tolerance: 0.2\n    unit: mV\n  criterion: Whisking depolarization by M-VM. The control neurons are whole-cell L4 E neurons from\n    control mice \"with matched resting potential\"; open how matched; readings, (a) control neurons\n    whose resting Vm lies within the range of the ION-cut neurons' resting Vm, (b) the 15 control\n    neurons whose resting Vm is nearest the ION-cut mean. The count under (a) is reported against\n    15. Reproduced when, under one reading, both means are within tolerance and a two-sided\n    rank-sum test gives p < 0.05 with ION cut lower.\n- id: ion-cut-l4e-phase\n  statement: After ION transection phase-locking of L4 excitatory Vm to whisker movement is\n    abolished (coupling 0.12 +- 0.04 mV against 0.38 +- 0.31 mV in controls, P = 0.005).\n  source: Results, Inhibition is driven by sensory input, paragraph 2; Fig. 7e\n  quote: phase-locking of membrane potential to whisker movement was abolished (ION cut, 0.12 ± 0.04\n    mV versus Control, 0.38 ± 0.31 mV; P = 0.005; Fig. 7e)\n  statistics:\n  - test: not named; unpaired comparison, Wilcoxon rank-sum by the Statistical analysis paragraph\n    p: 0.005\n    n: ION-cut and control L4 excitatory neurons, as in the preceding comparison\n  expected:\n  - quantity: Vm phase coupling, ION cut, mean\n    value: 0.12\n    tolerance: 0.013\n    unit: mV\n  - quantity: Vm phase coupling, controls, mean\n    value: 0.38\n    tolerance: 0.08\n    unit: mV\n  criterion: Coupling strength by M-PHASE on whisking-epoch Vm, spikes removed (M-VM). The groups\n    are read as those of ion-cut-l4e-whisking (9 and 15, under its readings), the passage running\n    on from it; the control tolerance uses n = 15. Reproduced when, under one reading, both means\n    are within tolerance and a two-sided rank-sum test gives p < 0.05 with ION cut lower.\n  depends_on:\n  - ion-cut-l4e-whisking\n- id: ion-cut-l4e-spectra\n  statement: After ION transection the Vm fluctuations of L4 excitatory neurons do not differ\n    between nonwhisking and whisking epochs.\n  source: Results, Inhibition is driven by sensory input, paragraph 2; Supplementary Fig. 11\n  quote: Spectral analysis revealed no difference in membrane potential fluctuations between\n    nonwhisking and whisking epochs (Supplementary Fig. 11)\n  criterion: A claim of absence, tested as l4e-hf-fluctuations is (M-SPEC, readings (a) and (b)\n    of the band) over the ION-cut L4 E neurons (10 in Supplementary Fig. 11). The paper names no\n    test; the signed-rank test fixed in l4e-hf-fluctuations is used. Reproduced when it is not\n    significant under reading (a), not reproduced when it is significant; reading (b) is shown as\n    a variant, and the median whisking to nonwhisking power ratio is reported.\n- id: ion-cut-fs-touch\n  statement: After ION transection touch does not evoke spikes in L4 FS interneurons (n = 10).\n  source: Results, Inhibition is driven by sensory input, paragraph 3; Fig. 7g\n  quote: Touch did not evoke spikes in FS interneurons (Fig. 7g)\n  criterion: A claim of absence. Spikes per touch by the cortical Fig. 5 definition (M-TOUCH) for\n    the 10 ION-cut FS neurons. The paper names no test; fixed from M-STAT, a two-sided signed-rank\n    test against zero at p < 0.05. Reproduced when it is not significant, not reproduced when it is\n    significant with positive values. The mean is reported beside the control 1.9 of\n    fs-touch-spikes.\n- id: ion-cut-fs-whisking\n  statement: After ION transection whisking-related activation of L4 FS interneurons is absent in\n    most cells (P = 0.80, n = 10).\n  source: Results, Inhibition is driven by sensory input, paragraph 3; Fig. 7h,i\n  quote: In addition, whisking-related activation of FS interneurons was also absent in most cells (P\n    = 0.80, n = 10 neurons; Fig. 7h,i)\n  statistics:\n  - test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 0.8\n    n: 10 ION-cut L4 FS neurons\n  criterion: A claim of absence, judged on the paper's test as M-STAT reads it, a two-sided\n    signed-rank test of whisking against nonwhisking rates (M-EPOCH, M-RATE) over the 10 neurons at\n    p < 0.05. Reproduced when it is not significant, not reproduced when it is. The number of\n    neurons with a significant increase by M-SIG is reported for \"in most cells\", and the median\n    whisking to nonwhisking ratio beside that of fs-whisking-rate.\n- id: ion-cut-fs-phase\n  statement: After ION transection phase-locking of L4 FS spikes to whisker movement is reduced but\n    not entirely abolished.\n  source: Results, Inhibition is driven by sensory input, paragraph 3; Supplementary Fig. 12\n  quote: Phase-locking of spikes to whisker movement was reduced but not entirely abolished\n    (Supplementary Fig. 12)\n  criterion: Goodness of fit (r2) of the spike-phase fit by M-PHASE, compared between control and\n    ION-cut L4 FS neurons (Supplementary Fig. 12b, which marks the medians). The paper names no\n    test; fixed from M-STAT, a two-sided rank-sum test at p < 0.05. Reproduced when the ION-cut r2\n    is lower by that test and at least one ION-cut neuron has r2 > 0.25.\n- id: ion-cut-l5-fs\n  statement: Unlike L4 FS neurons, many L5 FS interneurons (658 to 819 um deep, n = 7) still\n    increase their spike rates with whisking after ION transection.\n  source: Results, Inhibition is driven by sensory input, paragraph 3\n  quote: many L5 FS interneurons still increased their spike rates in response to whisking after ION\n    cut (depth, 658 to 819 μm, n = 7 neurons; data not shown)\n  criterion: The paper shows no data. If the dataset holds these neurons, per neuron by M-SIG;\n    reproduced when more than half of them increase significantly.\n- id: enphr-kruskal-wallis\n  statement: Partially suppressing PV (FS) interneurons with eNpHR changes the responses of L4\n    excitatory neurons (P = 1e-6, Kruskal-Wallis).\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 1; Fig. 8b to e\n  quote: Partially suppressing PV (FS) interneurons changed the responses of excitatory neurons (Fig.\n    8b–e; P = 1 × 10−6, Kruskal-Wallis test)\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 1.0e-6\n    n: 40 L4 excitatory neurons\n  criterion: The 40 L4 E neurons recorded with eNpHR in PV cells. Open, the groups of the test;\n    readings, (a) the four groups of Fig. 8d, nonwhisking and whisking rates in control and eNpHR\n    trials (M-EPOCH, M-RATE, M-LIGHT), (b) these four and the spikes per touch of Fig. 8e is a\n    different unit, so (b) is the two groups control and eNpHR with nonwhisking and whisking rates\n    pooled. Reproduced when the test gives p < 0.05 under one reading.\n- id: enphr-l4e-rates\n  statement: Suppressing PV interneurons increases L4 excitatory spike rates during nonwhisking\n    (0.6 +- 0.1 to 1.6 +- 0.3 spikes/s, P = 6e-5) and whisking (0.8 +- 0.2 to 2.7 +- 0.5 spikes/s,\n    P = 2e-6), mean +- s.e.m., n = 40.\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 1; Fig. 8d;\n    Supplementary Fig. 13\n  quote: L4 excitatory neurons increased their spike rate during both nonwhisking periods (from 0.6 ±\n    0.1 spikes per s to 1.6 ± 0.3 spikes per s; mean ± s.e.m., n = 40 neurons, P = 6 × 10−5) and\n    whisking periods(from 0.8 ± 0.2 spikes per s to 2.7 ± 0.5 spikes per s, P = 2 × 10−6\n  statistics:\n  - about: nonwhisking rate, eNpHR against control\n    test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 6.0e-5\n    n: 40 L4 excitatory neurons\n  - about: whisking rate, eNpHR against control\n    test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 2.0e-6\n    n: 40 L4 excitatory neurons\n  expected:\n  - quantity: nonwhisking rate, control\n    value: 0.6\n    tolerance: 0.1\n    unit: spikes/s\n  - quantity: nonwhisking rate, eNpHR\n    value: 1.6\n    tolerance: 0.3\n    unit: spikes/s\n  - quantity: whisking rate, control\n    value: 0.8\n    tolerance: 0.2\n    unit: spikes/s\n  - quantity: whisking rate, eNpHR\n    value: 2.7\n    tolerance: 0.5\n    unit: spikes/s\n  criterion: Rates by M-EPOCH and M-RATE in control and eNpHR trials (M-LIGHT, readings (a) and\n    (b)). Reproduced when, under one reading, all four means are within tolerance and both\n    two-sided signed-rank tests give p < 0.05 with higher rates under eNpHR; partially reproduced\n    when both tests hold and not all values are within tolerance.\n- id: enphr-whisking-driven\n  statement: With PV interneurons suppressed, L4 excitatory neurons become driven by whisker\n    movement (whisking against nonwhisking, P = 0.02).\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 1; Fig. 8d\n  quote: L4 excitatory neurons were instead driven by whisker movements (P = 0.02, Fig. 8d), implying\n    that their selectivity for touch was normally maintained in part by FS interneurons\n  statistics:\n  - test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 0.02\n    n: 40 L4 excitatory neurons\n  criterion: Whisking against nonwhisking rates in eNpHR trials, from enphr-l4e-rates, two-sided\n    signed-rank over the 40 neurons. Reproduced when p < 0.05 with whisking higher. The same test\n    in control trials is reported as a variant (the figure prints P = 0.55 beside the 0.02,\n    read here as that comparison, which the text extraction cannot confirm).\n  depends_on:\n  - enphr-l4e-rates\n- id: enphr-spikes-per-touch\n  statement: PV interneuron suppression changes touch-evoked spiking of L4 excitatory neurons\n    heterogeneously, with no significant mean change (0.27 +- 0.06 to 0.32 +- 0.06 spikes per touch,\n    n = 40, P = 0.09, Wilcoxon signed-rank); weakly responding neurons tend to respond more, and\n    strongly driven neurons stay the same or decrease.\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 2; Fig. 8e;\n    Supplementary Fig. 13b\n  quote: PV interneuron suppression also modulated touch-evoked spiking in L4 excitatory neurons, but\n    they did so in a heterogeneous manner (mean ± s.e.m., from 0.27 ± 0.06 spikes per touch to 0.32\n    ± 0.06 spikes per touch, n = 40 neurons, P = 0.09, Wilcoxon signed-rank test\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.09\n    n: 40 L4 excitatory neurons\n  expected:\n  - quantity: spikes per touch, control, mean\n    value: 0.27\n    tolerance: 0.06\n  - quantity: spikes per touch, eNpHR, mean\n    value: 0.32\n    tolerance: 0.06\n  criterion: Spikes per touch with the Fig. 8e definition (4 to 20 ms after minus 0 to 16 ms\n    before, touches with interval at least 10 ms; M-TOUCH), control against eNpHR trials\n    (M-LIGHT). The mean change is a claim of absence judged on the paper's two-sided signed-rank\n    test at p < 0.05. The heterogeneity has no test in the paper; fixed here, a Spearman\n    correlation between control spikes per touch and the change (eNpHR minus control) that is\n    negative with p < 0.05. Reproduced when both means are within tolerance, the signed-rank test\n    is not significant and the correlation holds; partially reproduced when two of the three hold.\n- id: enphr-auc\n  statement: PV interneuron suppression improves touch detection (AUC) for neurons with weak touch\n    responses and diminishes it for neurons with robust touch responses.\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 3; Fig. 8f,g\n  quote: suppression of PV interneurons improved AUC for neurons with weak responses to touch and\n    diminished AUC for neurons with robust responses to touch (Fig. 8f,g)\n  criterion: AUC per neuron in control and eNpHR trials by M-ROC; the touch-evoked rate of Fig. 8g\n    from control trials (M-ROC, last sentence). The paper names no test; fixed here, a Spearman\n    correlation between the control touch-evoked rate and the AUC change (eNpHR minus control),\n    negative at p < 0.05, with a two-sided rank-sum test of the control touch-evoked rate between\n    neurons whose AUC rose and those whose AUC fell (higher in the latter) as a variant.\n    Reproduced when the correlation holds under one M-ROC reading.\n- id: enphr-auc-groups\n  statement: Of the 40 neurons, eNpHR stimulation increased AUC in 19 and reduced it in 21. Those\n    with increased AUC raised their touch-evoked rates (3.4 +- 0.8 to 8.7 +- 1.9 spikes/s, P =\n    0.0001); those with reduced AUC kept their touch-evoked rates (7.3 +- 1.5 to 7.0 +- 1.4\n    spikes/s, P = 0.98) but raised their baseline rates (0.9 +- 0.2 to 2.6 +- 0.6 spikes/s, P =\n    0.0002).\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 4; Fig. 8h\n  quote: L4 excitatory neurons with increased AUCs showed a population increase in touch-evoked\n    responses on average (from 3.4 ± 0.8 spikes per s to 8.7 ± 1.9 spikes per s, P = 0.0001). Neurons\n    with reduced AUC showed unchanged touchevoked responses as a population (from 7.3 ± 1.5 spikes\n    per s to 7.0 ± 1.4 spikes per s, P = 0.98, average 0–250 ms after touch onset) but elevated\n    baseline spike rates (from 0.9 ± 0.2 spikes per s to 2.6 ± 0.6 spikes per s, mean ± s.e.m., P =\n    0.0002\n  statistics:\n  - about: touch-evoked rate, increased-AUC group, eNpHR against control\n    test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 0.0001\n    n: 19 L4 excitatory neurons\n  - about: touch-evoked rate, reduced-AUC group, eNpHR against control\n    test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 0.98\n    n: 21 L4 excitatory neurons\n  - about: baseline rate, reduced-AUC group, eNpHR against control\n    test: not named; paired comparison, Wilcoxon signed-rank by the Statistical analysis paragraph\n    p: 0.0002\n    n: 21 L4 excitatory neurons\n  expected:\n  - quantity: neurons with AUC increased\n    value: 19\n    tolerance: 1.9\n  - quantity: neurons with AUC reduced\n    value: 21\n    tolerance: 2.1\n  - quantity: increased-AUC group, touch-evoked rate, control\n    value: 3.4\n    tolerance: 0.8\n    unit: spikes/s\n  - quantity: increased-AUC group, touch-evoked rate, eNpHR\n    value: 8.7\n    tolerance: 1.9\n    unit: spikes/s\n  - quantity: reduced-AUC group, touch-evoked rate, control\n    value: 7.3\n    tolerance: 1.5\n    unit: spikes/s\n  - quantity: reduced-AUC group, touch-evoked rate, eNpHR\n    value: 7.0\n    tolerance: 1.4\n    unit: spikes/s\n  - quantity: reduced-AUC group, baseline rate, control\n    value: 0.9\n    tolerance: 0.2\n    unit: spikes/s\n  - quantity: reduced-AUC group, baseline rate, eNpHR\n    value: 2.6\n    tolerance: 0.6\n    unit: spikes/s\n  criterion: Groups by the sign of the AUC change (enphr-auc, M-ROC). Touch-evoked rate is the mean\n    rate 0 to 250 ms after touch onset on the touch PSTH (Fig. 8h, \"average 0-250 ms after touch\n    onset\"); baseline the mean 0 to 250 ms before (Fig. 8g legend). Open, whether the touch-evoked\n    rate here is raw or baseline-subtracted; readings, (a) raw, as the 7.3 against 0.9 baseline\n    suggests, (b) baseline-subtracted as in Fig. 8g. Touches by M-TOUCH with interval at least 25\n    ms. Reproduced when, under one combination of readings, the group sizes are within tolerance,\n    at least five of the six rates are within tolerance, the two increases are significant\n    (two-sided signed-rank, p < 0.05) and the touch-evoked change of the reduced group is not.\n  depends_on:\n  - enphr-auc\n- id: enphr-pv-latency\n  statement: eNpHR stimulation strongly inhibits 3 of 4 recorded L4 PV interneurons; their spike\n    rate falls 3 ms after laser onset and L4 excitatory activity rises only 2 ms later.\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 6; Supplementary\n    Fig. 13a,c\n  quote: First, the spike rate of L4 PV interneurons decreased 3 ms after laser onset, and activity in\n    L4 neurons increased only 2 ms later (Supplementary Fig. 13c)\n  expected:\n  - quantity: latency of PV rate decrease after laser onset\n    value: 3\n    tolerance: 0.3\n    unit: ms\n  - quantity: delay of L4 E increase after the PV decrease\n    value: 2\n    tolerance: 0.2\n    unit: ms\n  - quantity: PV interneurons strongly inhibited by eNpHR, of 4\n    value: 3\n    tolerance: 1\n  criterion: Grand-average spike rate of the L4 PV (FS) neurons and of the L4 E neurons aligned to\n    laser onset in 1 ms bins (Supplementary Fig. 13c). The paper defines no latency for this; the\n    M-LAT rule (dPSTH/dt crossing 3 s.d. of its value over the 25 ms before onset) is adapted, and\n    a crossing of the rate itself by 3 s.d. of the baseline rate is a second reading. \"Strongly\n    inhibited\" is read as a significant rate decrease by a two-sided rank-sum test over trials\n    (M-STAT), and a fall below half the control rate. Latencies are in whole 1 ms bins, so the\n    tolerance on each is one bin; reproduced when, under one reading, both latencies are within 1\n    ms and 3 of 4 PV neurons are strongly inhibited.\n- id: enphr-behavior\n  statement: With PV interneurons suppressed most mice (6 of 8) are more likely to report touch\n    with the pole out of reach; in an example session the false alarm rate rose from 20% to 61%.\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 5; Supplementary\n    Fig. 14b,c\n  quote: Consistently, with PV interneuron suppressed, most mice (6 of 8) were more likely to report\n    touches with the pole out of reach (Supplementary Fig. 14)\n  statistics:\n  - test: Chi-squared test, per mouse\n    p: 0.05\n    p_relation: \"<\"\n    n: 8 mice\n  expected:\n  - quantity: mice with a significant decrease in no-lick performance under PV suppression\n    value: 6\n    tolerance: 1\n  - quantity: example session false alarm rate, control\n    value: 20\n    tolerance: 2\n    unit: percent\n  - quantity: example session false alarm rate, PV suppression\n    value: 61\n    tolerance: 6.1\n    unit: percent\n  criterion: Per mouse, the proportion correct in no-lick (distal pole) trials with and without\n    PV suppression, compared by a chi-squared test at p < 0.05 (Supplementary Fig. 14c legend).\n    Open whether sessions of a mouse are pooled; reading, pooled. Reproduced when the count is\n    within tolerance; the example session, if found, is reported against its two rates, and the one\n    mouse with a significant increase in performance (legend) is reported.\n"
}
```

```
File created successfully at: claims/crcns-ssc-7/10.1038-nn.4412.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ssc-7/10.1038-nn.4412.yaml",
 "old_string": "    trials (M-EPOCH, M-RATE, M-LIGHT), (b) these four and the spikes per touch of Fig. 8e is a\n    different unit, so (b) is the two groups control and eNpHR with nonwhisking and whisking rates\n    pooled. Reproduced when the test gives p < 0.05 under one reading.",
 "new_string": "    trials (M-EPOCH, M-RATE, M-LIGHT), (b) two groups, control and eNpHR, with the nonwhisking and\n    whisking rates of each neuron pooled. Reproduced when the test gives p < 0.05 under one reading."
}
```

```
The file claims/crcns-ssc-7/10.1038-nn.4412.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/crcns-ssc-7/10.1038-nn.4412.yaml paper/10.1038-nn.4412.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/crcns-ssc-7 && python - <<'EOF'
p='10.1038-nn.4412.yaml'
s=open(p).read()
R=[
("""  quote: Mice touched the pole at a proximal location multiple times (number of touches, 5.7 ± 5.3,
    mean ± s.d., 4,147 trials) ... Average""","""  quote: Mice touched the pole at a proximal location multiple times ... 5.7 ± 5.3, mean ± s.d.,
    4,147 trials) ... Average"""),
("""  quote: Touches evoked short-latency depolarizations (latency, mean ± s.d., 4.8 ± 0.8 ms; median,
    4.7 ms; amplitude, mean ± s.d., 6.0 ± 2.9 mV; median, 5.7 mV; n = 37 neurons) for all neurons""",
"""  quote: Touches evoked short-latency depolarizations ... mean ± s.d., 4.8 ± 0.8 ms; median, 4.7 ms
    ... mean ± s.d., 6.0 ± 2.9 mV; median, 5.7 mV; n = 37 neurons) for all neurons"""),
("""Response latencies were short for membrane potential depolarization (onset,
    mean ± s.d., 4.0 ± 0.6 ms""","""Response latencies were short for membrane potential depolarization ... mean
    ± s.d., 4.0 ± 0.6 ms"""),
("""    movement (nonwhisking, mean ± s.d., 0.4 ± 0.6 spikes per s; median, 0.1 spikes per s; whisking,
    mean ± s.d., 0.6""","""    movement ... mean ± s.d., 0.4 ± 0.6 spikes per s; median, 0.1 spikes per s ... mean ± s.d., 0.6"""),
("""  quote: however, as they were unable to sense the object, they performed at chance level (48%
    correct)""","""  quote: however, as they were unable to sense the object ... they performed at chance level (48%
    correct)"""),
("""  quote: Depolarizations in response to whisker movement were reduced (ION cut, mean ± s.d., 0.62 ±
    0.50 mV, n = 9 neurons versus Control with matched resting potential, mean ± s.d., 1.54 ± 0.79
    mV, n = 15 neurons""","""  quote: Depolarizations in response to whisker movement were reduced ... 0.62 ± 0.50 mV, n = 9
    neurons versus Control with matched resting potential ... 1.54 ± 0.79 mV, n = 15 neurons"""),
("""average 0–250 ms after touch onset) but elevated""","""average 0–250 ms after touch onset) ... but elevated"""),
]
for a,b in R:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
cd ../.. && python tools/claims_check.py claims/crcns-ssc-7/10.1038-nn.4412.yaml paper/10.1038-nn.4412.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/crcns-ssc-7 && grep -n "—\|rather" *.yaml; python - <<'EOF'
import yaml
d=yaml.safe_load(open('10.1038-nn.4412.yaml'))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print(path, x[:80])
walk(d)
EOF
grep -n "^  [a-z_]*: \".*\|^    [a-z_]*: \"" 10.1038-nn.4412.yaml | head
```

```
1192:    p_relation: "<"
```

**Agent**

The checker passes (47 claims, 47 quotes, 0 problems) and the style checks are clean. One fix left: the expected tolerances of `enphr-pv-latency` disagree with its criterion's one-bin rule.

**Agent calls Bash**

```bash
cd  && python - <<'EOF'
p='claims/crcns-ssc-7/10.1038-nn.4412.yaml'
s=open(p).read()
a="""    value: 3
    tolerance: 0.3
    unit: ms
  - quantity: delay of L4 E increase after the PV decrease
    value: 2
    tolerance: 0.2
    unit: ms"""
b="""    value: 3
    tolerance: 1
    unit: ms
  - quantity: delay of L4 E increase after the PV decrease
    value: 2
    tolerance: 1
    unit: ms"""
assert a in s; s=s.replace(a,b)
a="""    tolerance on each is one bin; reproduced"""
b="""    tolerance on each is one bin, not 10%, which is below the bin width; reproduced"""
assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/crcns-ssc-7/10.1038-nn.4412.yaml paper/10.1038-nn.4412.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/crcns-ssc-7/10.1038-nn.4412.yaml`, and the quote checker passes on it (47 claims, 47 quotes, 0 problems). Nothing is committed.

**Text read.** The version of record: main text, figure legends and Online Methods, plus the supplement PDF with the legends of Supplementary Figs. 1 to 14 and Supplementary Tables 1 and 2. The supplementary videos aren't text and weren't used. No PDF renderer is installed here, so I read no figure as an image; I only claimed numbers that appear in the text.

**Code.** I read none. The paper says its code is at the CRCNS DOI, which is this dataset, and the data descriptor names the folder `example_analysis_code`. That folder is one of the dataset's files, so I didn't open it. Every method comes from the paper alone, and the author may read that code to settle the open details below.

**Claims.**
- **Count:** 47, all of them findings and all with quotes, none inferred. Every claim uses the paper's own recordings (`data: dataset`).
- **Statistics:** 34 claims have a `statistics` block or `expected` values (31 with `expected`). The checker found 21 of the recorded p-values in the text.
- **Criteria:** all 47 have one. They cover VPM, L4 excitatory and L4 FS activity during touch and whisking, thalamic photoinhibition, rabies tracing, nerve transection (ION cut), PV suppression with eNpHR (including AUC and behaviour), and task performance.

**Tolerances.** For a mean ± s.d. I used s.d./√n, or 10% of the value if that is larger, because the s.d. is the spread of neurons, not the precision of the mean. A mean ± s.e.m. takes the s.e.m. Medians, single-neuron values and percentages take 10%. Counts take 10%, with a minimum of 1. The two latencies in `enphr-pv-latency` take one 1 ms bin, because 10% is smaller than the bin.

**Unnamed tests.** Many P values come without a named test. The Methods list only the rank-sum test (unpaired), the signed-rank test (paired) and Kruskal-Wallis, so I read paired comparisons as signed-rank and unpaired ones as rank-sum. Where the paper reports no test at all, the criterion fixes one from that list and says so.

**Details the paper leaves open, with the readings named.** These are defined once in the file's opening comment (labels M-…) and referred to by the criteria.
- **Whisking epochs:** the margin around touches and licks for nonwhisking epochs is either the whisking one or none. The 2° rise at whisking onset is measured over 250 ms or over 100 ms.
- **Epoch rates:** total spikes over total epoch time, or the mean of per-epoch rates. In laser experiments, control trials only.
- **Per-neuron whisking test:** rank-sum on per-epoch rates or on per-trial rates.
- **Vm measures:** resting Vm is the nonwhisking mean or the median outside touch. The touch-response peak is sought within 0–50 ms or 0–25 ms. Whisking depolarization is the 100–300 ms after onset minus the 0–200 ms before, or whisking-epoch Vm minus nonwhisking-epoch Vm.
- **Duration of the VPM touch response:** the width at 25% of the rise from baseline to peak.
- **Phase coupling:** 8 or 16 phase bins.
- **Spectra:** band 10–100 Hz or 10–500 Hz.
- **ROC for touch detection:** in no-touch trials, the reference time is either drawn at random within the sample epoch 5,000 times, or set at the median first-touch time with 5,000 trial bootstraps.
- **Photostimulation:** epochs within the laser-on period or whole trials; all laser powers or the highest only; "to x% of control" as a ratio of population means or a median of per-neuron ratios.
- **ION-cut controls "with matched resting potential":** controls within the ION-cut neurons' range, or the 15 nearest to the ION-cut mean.
- **Kruskal-Wallis groups for eNpHR:** four groups (nonwhisking and whisking, control and eNpHR) or two (control and eNpHR).
- **Fig. 8h touch-evoked rate:** raw or baseline-subtracted.
- **Two thalamic-photoinhibition latencies** that the paper doesn't define: the Methods' touch-latency rule, adapted to laser onset.
- **Fig. 8d:** the extracted text shows P = 0.55 beside P = 0.02. I read it as the control-trial comparison, which the text can't confirm, so it is only a variant.

**Missing or inconsistent in the paper.**
- L4 FS neurons are 26 in the Results and Methods, but 25 in the Supplementary Fig. 7 legend and in the sum of Supplementary Table 2.
- ION-cut L4 excitatory neurons are 8, 9 or 10 depending on the passage.
- The rabies tracing and the L5 FS ION-cut recordings ("data not shown") may not be in the dataset; whether they are is for the author to find.
- The example session of Supplementary Fig. 1e names no unit.

Nothing the claims needed was missing.

## End of run

23 turns, 8 minutes, $2.60 at API prices, result: success.
