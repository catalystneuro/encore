# 001274 · claims · run 39722372968

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001274 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -c paper/*; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0347b8fb-2177-4605-9b3f-5dc8f3d18bc1/tool-results/bt4bi9nrc.txt",
 "limit": 260
}
```

```
File content (31395 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml",
 "limit": 180
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*; head -30 paper/*.txt; grep -n "Supplemental\|supplement\|github\|Github\|GitHub\|zenodo\|dandi\|DANDI" paper/*.txt | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; fold -s -w 200 10.1016-j.xcrp.2025.102660.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt
```

```
1007 /tmp/claude-1001/p.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 350
}
```

```
1	DOI: 10.1016/j.xcrp.2025.102660
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC12320893), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	319 nihpa Cell reports. Physical science Cell Rep Phys Sci PMC12320893 12320893 12320893 NIHMS2098259 40762005 10.1016/j.xcrp.2025.102660 Excitation and polarization of isolated neurons by 
8	high-frequency sine waves for temporal interference stimulation Semenov Iurii 1 Kim Vitalii 1 2 Silkuniene Giedre 1 Pakhomov Andrei G 1 3 4 * 1 Frank Reidy Research Center for Bioelectrics, Old 
9	Dominion University, Norfolk, VA 23508, USA 2 Present address: Department of Chemical and Biomolecular Engineering, University of California, Irvine, Irvine, CA 92697, USA 3 Senior author 4 Lead 
10	contact * Correspondence: [removed: an e-mail address] AUTHOR CONTRIBUTIONS Conceptualization, A.G.P.; methodology, V.K., I.S., and A.G.P.; investigation, V.K., I.S., and A.G.P.; dosimetry, V.K. and G.S.; data 
11	processing, V.K., I.S., G.S., and A.G.P.; writing – original draft, A.G.P.; writing – review & editing, V.K., I.S., G.S., and A.G.P.; funding acquisition, A.G.P.; supervision, A.G.P. 16 6 2025 6 7 
12	102660 102660 4 8 2025 This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). The publisher's version of this article is available at Cell Rep Phys 
13	Sci SUMMARY The capacity of temporal interference (TI) stimulation to target deep brain regions without affecting nearby surface electrodes remains uncertain. Using artifact-free optical recording, 
14	we compare excitation patterns and thresholds in hippocampal neurons stimulated by “pure” and amplitude-modulated sine waves, representing TI waveforms near electrodes and at the target, 
15	respectively. We sho
[... 335 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "Figure S1\b\|SUPPLEMENT\|Table S1\|Supplemental\|Document S1\|====\|----" $TMPDIR/p.txt | tail -30
```

```
6:------------------------------------------------------------------------
121:neurons using different electric field strengths tested in a random sequence. A typical experiment is illustrated in Figure S1 . Compared to FluoVolt recordings, the traces were expectedly noisier 
259:approximately 1 week before the experiments. Half of the medium was changed every 3 days during incubation. See Table S1 for more details. Recording of the optical APs and data analyses All 
264:incubation in this solution for 15–30 min, rinsed, and left in the dye-free solution. In one set of experiments ( Figure S1 ), neurons were loaded with 5 μM Di-8-ANEPPS dye (Thermo Fisher Scientific) 
335:protocols were followed but the signal amplitude was set to zero) and vehicle controls in experiments with tetrodotoxin. Supplementary Material 1 Supplemental information can be found online at 
809:Supplemental information 
819:Figure S1, related to Figure 1. Excitation and inhibition of firing in a neuron loaded with Di-8-ANEPPS 
931:Table S1: Key Resource Table
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 795
}
```

```
795	
796	[55] Action spectra and mechanisms of (in) efficiency of bipolar electric pulses at electroporation. Bioelectrochemistry. 2023. 10.1016/j.bioelechem.2022.108319
797	
798	[56] Four Channel 6.5 kV, 65 A, 100 ns - 100 micros Generator with Advanced Control of Pulse and Burst Protocols for Biomedical and Biotechnological Applications. Applied Sciences. 2021. 
799	10.3390/app112411782
800	
801	[57] Peculiarities of Neurostimulation by Intense Nanosecond Pulsed Electric Fields: How to Avoid Firing in Peripheral Nerve Fibers. Int. J. Mol. Sci.. 2021.
802	
803	[58] Electroporation and cell killing by milli- to nanosecond pulses and avoiding neuromuscular stimulation in cancer ablation. Sci. Rep.. 2022. 10.1038/s41598-022-04868-x
804	
805	##### Supplement: NIHMS2098259-supplement-1.pdf
806	
807	=== page 1 ===
808	Cell Reports Physical Science, Volume 6 
809	Supplemental information 
810	Excitation and polarization of isolated neurons 
811	by high-frequency sine waves 
812	for temporal interference stimulation 
813	Iurii Semenov, Vitalii Kim, Giedre Silkuniene, and Andrei G. Pakhomov 
814	
[... 194 more lines not kept]
```

**Agent**

The full text, Methods and supplement are all present, and the paper reports no original code. Next I'll check the dataset's title and description to see which experiments 001274 is meant to hold.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001274/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:3000])"; curl -s https://api.dandiarchive.org/api/dandisets/001274/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m.get('name'));print(m.get('description'));print(m.get('version'));print([r.get('identifier') for r in m.get('relatedResource',[])])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for i in 001030 001031 001032 001033 001034 001035 001271 001272 001273; do curl -s https://api.dandiarchive.org/api/dandisets/$i/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print('$i',m.get('name'));print('   ',m.get('description')[:600])"; curl -s "https://api.dandiarchive.org/api/dandisets/$i/" | python -c "import json,sys;d=json.load(sys.stdin);print('   published:',(d.get('most_recent_published_version') or {}).get('version'))"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd ..; ls claims/; grep -rl "xcrp.2025.102660" claims/ | head; grep -rn -A3 "data: elsewhere" claims/ | head -40
```

```
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
000016
000017
000019
000023
000034
000035
000036
000041
000044
000056
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "^  [a-z_]*:" -o claims/*/*.yaml | awk -F: '{print $NF? $3:$3}' | sort | uniq -c | sort -rn | head -30
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 78 more lines not kept]
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

**Agent calls Bash**

```bash
grep -rn -B2 -A8 "range widened\|widened by 10" claims/*/*.yaml | head -60
```

```
claims/000010/10.1038-nature14178.yaml-70-    sessions; (c) the mean over mice of per-mouse performance. Reproduced when, under one
claims/000010/10.1038-nature14178.yaml-71-    reading, the per cent correct is within tolerance and the fraction of lick early trials
claims/000010/10.1038-nature14178.yaml:72:    among control trials (same three readings) is below 13% widened by 10% (14.3%). Trials
claims/000010/10.1038-nature14178.yaml-73-    without a lick in the 1.5 s window after the go cue ("did not lick", Methods, Behaviour) are
claims/000010/10.1038-nature14178.yaml-74-    not named among the exclusions; the Methods exclude only lick early trials. Readings are
claims/000010/10.1038-nature14178.yaml-75-    (x) no-lick trials kept in the denominator as not correct, the literal reading of the
claims/000010/10.1038-nature14178.yaml-76-    Methods, and (y) no-lick trials left out, reading "fraction of correct reports" as among
claims/000010/10.1038-nature14178.yaml-77-    trials with a report. Both are run; either may decide.
claims/000010/10.1038-nature14178.yaml-78-- id: fig1d-delay-inhibition-ipsi-bias
claims/000010/10.1038-nature14178.yaml-79-  statement: Unilateral photoinhibition of ALM during the delay epoch biases licking to the
claims/000010/10.1038-nature14178.yaml-80-    ipsilateral side, raising performance on ipsilateral (lick left for left ALM) trials and
--
claims/000019/10.1038-nature11911.yaml-642-    configuration for vowels (OPEN; reading (b) the mean over the three feature sets);
claims/000019/10.1038-nature11911.yaml-643-    squared Pearson correlation over the epoch at 5 ms steps. Reproduced when the six R2
claims/000019/10.1038-nature11911.yaml:644:    values lie within 0.38 to 1 (the reported range widened by 10% of each bound) with each
claims/000019/10.1038-nature11911.yaml-645-    p < 1e-10; partially reproduced when all are positive and significant but some fall below
claims/000019/10.1038-nature11911.yaml-646-    0.38.
claims/000019/10.10
[... 42 more lines not kept]
```

**Agent**

I have what I need: the dataset holds the strobe recordings of sine-wave polarization (Figures 5, 6 and S3). The paper reports no code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/001274/10.1016-j.xcrp.2025.102660.yaml",
 "content": "# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,\n# on dandiset 001274.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, under\n# docs/protocol.md version pilot-10, as the reader.\n#\n# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with\n# its main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,\n# Figures S1 to S4 and Table S1, the Key Resource Table), all in\n# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was\n# available, so Figures 1 to 6 could not be looked at; numbers shown only in figures are not used.\n#\n# Code. The paper states that it does not report original code. Analyses were done with Fiji or\n# MetaMorph (ROI intensities), Origin 8.0 (exponential fits), Grapher 16 (linear regression) and,\n# per Table S1, RStudio 2024.04.2 (the LOESS fits are read here as R's loess, see below).\n#\n# Data the paper used. E18 Sprague-Dawley rat hippocampal neurons (BrainBits), cultured about one\n# week on coverslips, stained with FluoVolt (Di-8-ANEPPS in Figure S1). Two kinds of recording:\n# (1) Fast imaging of the optical membrane potential (64 x 64 pixels, 3,130 or 3,086.4 frames/s,\n# 1,200 images per session, 50 ms before, 250 ms during and about 90 ms after the stimulus), with\n# 250-ms unmodulated or 20-Hz amplitude-modulated sine waves at 2 and 20 kHz (Figures 1, 2), in\n# NaCl (16.4 mS/cm) or sodium gluconate (8.4 mS/cm) solution (Figure 3), 2-s ramped 2-kHz sine\n# waves (Figure 3C), Di-8-ANEPPS controls on eight neurons (Figure S1) and 1 uM tetrodotoxin\n# (Figure S2). Measured variables are whole-soma emission F and dF = 100% (F - F0)/F0, with F0 the\n# pre-stimulus mean; the field per session in V/cm.\n# (2) Pulsed laser strobe imaging (6-ns flashes, full sensor, no binning). Figure 4 has 2-us,\n# 140 V/cm pulses applied from two orthogonal directions with a three-electrode array, 160 images\n# at 50-ns steps, eight replicates, 19 neurons (3 elongated parallel, 6 elongated perpendicular,\n# 10 random). Figures 5, 6 and S3 have 9 neurons (C1 to C9; C7 is the cell of Figure 5, C8 the\n# cell of Figure S3), each imaged first with a subthreshold 2-us, 257 V/cm pulse at 50-ns steps,\n# then with a single beat of a 2-kHz sine wave modulated at 100 Hz (10 ms) or 154 Hz (6.5 ms),\n# imaged at 20-us steps, peak field 136 V/cm in Figure 5, repeated 4 to 12 times (12 in Figure 5).\n# Per cell, ROI 1 and ROI 2 over the most hyper- and depolarized regions, and one \"debris\" ROI\n# used to scale out laser-flash fluctuations; 16 further ROIs in Figure 5E to 5G.\n#\n# This dandiset. Its title and description (DANDI:001274, \"Characterization of Plasma Membrane\n# Polarization in Hippocampal Neurons During Sine Wave and Modulated Sine Wave Stimulation\"; 2 kHz\n# sine waves, or modulated at 100 or 154 Hz, FluoVolt) say it holds the strobe recordings of sine\n# wave polarization, that is the sine wave part of Figures 5, 6 and S3. The paper deposited its\n# raw images in ten dandisets (Data and code availability) without saying which figure is in\n# which. From the dandisets' titles only: 001030 holds the 2-s ramped 2-kHz stimulation (Figure\n# 3C); 001032 to 001035 the sine and modulated sine wave stimulation at varying frequencies\n# (Figures 1, 2, 3A and 3B); 001271 tetrodotoxin (Figure S2); 001272 Di-8-ANEPPS (Figure S1);\n# 001273 the 2-us pulse kinetics (Figure 4); 001031 (100-kHz bipolar pulses) matches no figure.\n# Claims on those data are marked data elsewhere with that dandiset, as read from its title.\n# The 2-us pulse recordings of the nine cells of Figures 5 and 6 are needed by several claims\n# here (data dataset); the description of 001274 names sine waves only, so they may be in 001274\n# or in 001273. The author finds where they are; if only in 001273, those claims use it as an\n# outside input of the same paper (author, step 4).\n#\n# Method details fixed from the paper, used by several criteria (STAR Methods, Pulsed laser\n# fluorescence microscopy, unless said otherwise). ROIs are the paper's, placed by hand over the\n# most polarized membrane regions of the pulse RATIO image; ROI intensity is the mean emission in\n# the ROI per frame, scaled to the debris ROI. The paper processed data \"with and without\n# scaling\", so both are run; the outcome is the one both give. For pulses F0 is the mean before\n# the pulse; for sine waves F0 is the mean of the frames of the first and last sine wave cycles.\n# Pulse sensitivity is the dF averaged from 1 to 2 us into the pulse (21 frames), divided by the\n# field in kV/cm (Results, paragraph on Figure 6; Figure 6B legend). Sine wave sensitivity is the\n# regression coefficient of the emission change on the electric field after subtracting the LOESS\n# fit of the whole-cell response (Figure 5H and 6C legends). Magnitudes are compared, as the\n# figures plot the hyperpolarized and depolarized ROIs as bars of one sign.\n#\n# Details the paper leaves open, with the readings named. (O1) The ROIs' size and position are\n# not given; the ROIs must come from the dataset, and when it holds none the claim is blocked as\n# metadata_insufficient, with an ROI rebuilt from the RATIO image (Methods) shown as a variant\n# only. (O2) The LOESS span and degree are not given; Table S1 lists RStudio, so the readings are\n# R's loess defaults (span 0.75, degree 2), and spans 0.5 and 0.25 (degree 2), all of which keep\n# the 2-kHz carrier (25 frames per cycle) out of the fit; the outcome is the one all give. (O3)\n# How \"the electric field strength\" enters the regression is not given; readings (a) frame by\n# frame, the dF after LOESS subtraction on the signed instantaneous field of the stimulus at that\n# frame (from the stimulus waveform or timing stored in the dataset), slope in % per kV/cm;\n# (b) per carrier cycle, half the peak-to-peak dF after subtraction on the peak field of that\n# cycle, with and without an intercept. (O4) Which recording is cell C7 or C8 is to be found\n# from the dataset (pulse 257 V/cm, peak sine field 136 V/cm and 12 sessions for C7); when no\n# recording can be matched the claims on those cells are blocked as metadata_insufficient.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001274\"\npaper: doi:10.1016/j.xcrp.2025.102660\nclaims:\n- id: fig1-pure-sine-excites-all\n  statement: Unmodulated 250-ms sine waves at 2 kHz and at 20 kHz excited every neuron tested,\n    with sustained firing and no on-off response.\n  source: Results, Stimulation by 2- and 20-kHz unmodulated sine waves, paragraph 1; Figure 1A to 1C\n  quote: Pure sine waves at 2 and even 20 kHz excited 100% of neurons. It was never an \"on-off\"\n    response\n  data: elsewhere\n  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles; the paper does not\n    map figures to dandisets)\n  expected:\n  - quantity: fraction of neurons excited by unmodulated 2- or 20-kHz sine waves\n    value: 100\n    tolerance: 10\n    unit: percent\n  criterion: Per neuron, excited when at least one session with an unmodulated 2- or 20-kHz sine\n    wave has an AP during the 250-ms stimulus. The Methods give no detection rule beyond \"brief\n    emission upticks\" in neurons whose APs peak above 5% dF and last about 10 ms (Recording of the\n    optical APs); readings (a) a peak of dF above 5% over F0, (b) a rise of at least 5% dF within\n    5 ms, which also counts APs riding on a depolarization. Reproduced when, under each reading,\n    at least 90% of neurons tested with each frequency are excited.\n- id: fig1-onset-delay\n  statement: Near threshold, isolated APs appear 100 to 200 ms after the sine wave onset, and\n    stronger fields shorten this delay and evoke sustained firing.\n  source: Results, Stimulation by 2- and 20-kHz unmodulated sine waves, paragraph 1; Figure 1A to 1C\n  quote: at near-threshold electric field strengths, isolated APs emerged with a delay of 100-200 ms\n    after the sine wave onset ... Increasing the field strength reduced this delay and evoked\n    sustained firing\n  data: elsewhere\n  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)\n  depends_on:\n  - fig1-pure-sine-excites-all\n  criterion: AP detection as in fig1-pure-sine-excites-all, both readings. Per neuron and\n    frequency, the near-threshold session is the session of lowest field with at least one AP.\n    Reproduced when the median first-AP latency of those sessions lies within 90 to 220 ms (the\n    range widened by 10% of each bound) and, per neuron, the first-AP latency falls with field\n    (Spearman correlation below zero in more than half of the neurons with at least three\n    sessions with APs).\n- id: fig1-max-rate-ceiling\n  statement: The maximum firing rate increases linearly with field strength until it reaches a\n    ceiling of 60 to 90 Hz.\n  source: Results, Stimulation by 2- and 20-kHz unmodulated sine waves, paragraph 1; Figure 1 inset\n  quote: The maximum firing rate increased linearly until reaching a ceiling of 60-90 Hz\n  data: elsewhere\n  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)\n  depends_on:\n  - fig1-pure-sine-excites-all\n  criterion: The maximum firing rate of a session is the inverse of the interval between the\n    peaks of its first two APs (Methods, Recording of the optical APs); AP detection as in\n    fig1-pure-sine-excites-all, both readings. The ceiling of a neuron is its highest maximum\n    firing rate over sessions with unmodulated sine waves. Reproduced when the median ceiling\n    over neurons lies within 54 to 99 Hz (60 to 90 Hz widened by 10% of each bound). The rise\n    below the ceiling is reported as the slope of a linear fit of rate on field over the\n    sessions before the ceiling; the inset shows three neurons only.\n- id: fig1-excitation-block\n  statement: At the highest field strengths, APs coalesce into low-amplitude oscillations on a\n    continuous depolarization, which can flatten and leave the membrane depolarized for the rest\n    of the sine wave (an excitation block).\n  source: Results, Stimulation by 2- and 20-kHz unmodulated sine waves, paragraph 1; Figure 1A to 1C\n  quote: At the highest field strengths, multiple APs coalesced into low-amplitude oscillations on top\n    of a continuous depolarization. These oscillations could flatten after several cycles, leaving\n    the membrane depolarized for the rest of the sine wave\n  data: elsewhere\n  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)\n  criterion: The paper gives no measure. Per neuron, the session of highest field with an\n    unmodulated sine wave is compared with the near-threshold session (as in fig1-onset-delay).\n    Reproduced when, in more than half of the neurons, the mean dF over the last 100 ms of the\n    stimulus in the highest-field session exceeds the pre-stimulus F0 by more than 5% dF (the\n    Methods' AP selection level) and exceeds that of the near-threshold session. The windows are\n    a standard choice; the mean over the whole second half of the stimulus is shown as a variant.\n- id: fig2d-20khz-twofold-threshold\n  statement: All excitation thresholds at 20 kHz were about twice those at 2 kHz, for modulated and\n    unmodulated sine waves and for 1 and 5 APs.\n  source: Results, Excitation thresholds are similar or lower for pure 2- and 20-kHz sine waves than\n    those for modulated sine waves, paragraph 1; Figure 2D\n  quote: All thresholds at 20 kHz were about 2-fold higher than at 2 kHz ( p < 0.0001, two-tailed\n    unpaired t test)\n  statistics:\n  - test: two-tailed unpaired t test\n    p: 0.0001\n    p_relation: \"<\"\n    n: n individual neurons per group (numbers in Figure 2D only)\n  data: elsewhere\n  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)\n  expected:\n  - quantity: ratio of 20-kHz to 2-kHz threshold, each of the four stimulus and AP-count pairs\n    value: 2\n    tolerance: 0.2\n  criterion: The threshold of a neuron for a stimulus is the lowest field of a session that\n    evoked at least 1 (or at least 5) APs during the 250-ms stimulus (Figure 2D legend; Methods,\n    5% to 10% amplitude steps); AP detection as in fig1-pure-sine-excites-all, both readings. For\n    each of the four groups (unmodulated and modulated, 1 and 5 APs) the ratio of mean 20-kHz to\n    mean 2-kHz threshold, and a two-tailed unpaired t test of the two (Methods, Quantification\n    and statistical analysis). Reproduced when each ratio is within tolerance and each p < 0.0001.\n    The field per session is taken from the dataset's metadata (the description of 001030 states\n    1 V = 36 V/cm for this electrode; the paper shows the conversion only in Figure S4C).\n- id: fig2d-modulated-thresholds-higher\n  statement: Thresholds for sine waves modulated at 20 Hz were significantly higher than for pure\n    sine waves of the same carrier, for 5 APs at 2 kHz and for 1 and 5 APs at 20 kHz.\n  source: Results, Excitation thresholds are similar or lower for pure 2- and 20-kHz sine waves than\n    those for modulated sine waves, paragraph 1; Figure 2D\n  quote: thresholds for modulated sine waves, which emulate the TI stimulus at the target, were\n    significantly higher than those for pure sine waves at the same frequency (for 2 kHz, 5 APs\n    p = 0.0079; for 20 kHz, 1 and 5 APs, respectively p = 0.0142 and p = 0.0037)\n  statistics:\n  - about: modulated against unmodulated, 2 kHz, 5 APs\n    test: two-tailed unpaired t test\n    p: 0.0079\n  - about: modulated against unmodulated, 20 kHz, 1 AP\n    test: two-tailed unpaired t test\n    p: 0.0142\n  - about: modulated against unmodulated, 20 kHz, 5 APs\n    test: two-tailed unpaired t test\n    p: 0.0037\n  data: elsewhere\n  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)\n  depends_on:\n  - fig2d-20khz-twofold-threshold\n  criterion: Thresholds as in fig2d-20khz-twofold-threshold. For each of the three pairs, a\n    two-tailed unpaired t test of modulated against unmodulated thresholds, as the Results and the\n    Figure 2D legend name it, although the same neurons were often tested with both; the paired\n    test on neurons with both is shown as a variant. Reproduced when all three have the modulated\n    mean higher with p < 0.05 (the Methods' level; the legend marks p < 0.02); partially\n    reproduced when one or two do. The 2-kHz 1-AP pair, for which the paper reports no\n    difference, is reported.\n- id: threshold-2khz-unmodulated\n  statement: The AP threshold for unmodulated 2-kHz sine waves was 57.7 plus or minus 3.6 V/cm.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraph 4; Figure 2D\n  quote: the AP threshold of 57.7 ± 3.6 V/cm for unmodulated 2-kHz sine waves ( Figure 2D )\n  data: elsewhere\n  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)\n  depends_on:\n  - fig2d-20khz-twofold-threshold\n  expected:\n    quantity: mean 1-AP threshold, unmodulated 2 kHz\n    value: 57.7\n    tolerance: 3.6\n    unit: V/cm\n  criterion: The mean over neurons of the 1-AP threshold as in fig2d-20khz-twofold-threshold,\n    under both AP readings; reproduced when one is within tolerance (the SEM the paper gives).\n- id: fig2-modulated-locks-to-beats\n  statement: With 20-Hz modulation, firing above threshold is locked to the beats, one AP near the\n    peak of each of the five beats and at most two per beat (ten in all), and modulated sine waves\n    trigger no sustained firing or sustained depolarization.\n  source: Results, Stimulation by 2- and 20-kHz sinusoids modulated at 20 Hz, paragraph 1; Figures 2A\n    and 2B\n  quote: single APs emerged near the peak of each beat, so the firing rate equaled the modulation\n    rate ... the maximum number of APs evoked by five beats was limited to ten. Unlike pure sine\n    waves, modulated stimuli did not trigger sustained firing or sustained depolarization\n  data: elsewhere\n  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)\n  criterion: AP detection as in fig1-pure-sine-excites-all, both readings. For sessions with\n    modulated sine waves, reproduced when (i) no session has more than 10 APs, (ii) in sessions\n    with 5 APs or more, at least 80% of APs fall within the middle half of a 50-ms beat (12.5 to\n    37.5 ms from the beat's start, the peak at 25 ms), and (iii) no session meets the excitation\n    block test of fig1-excitation-block. The 80% and the window are a reading of \"near the peak\",\n    which the paper does not quantify; the AP phase histogram over the beat is reported.\n- id: fig2c-pure-more-aps\n  statement: In the same neuron at the same field strength, pure sine waves trigger more APs than\n    modulated ones.\n  source: Results, Stimulation by 2- and 20-kHz sinusoids modulated at 20 Hz, paragraph 2; Figure 2C\n  quote: At the same field strengths, pure sine waves triggered a larger number of APs\n  data: elsewhere\n  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)\n  criterion: AP detection as in fig1-pure-sine-excites-all, both readings. Pairs are a neuron's\n    modulated and unmodulated sessions at the same carrier and the same field. Reproduced when\n    the unmodulated AP count exceeds the modulated count in more pairs than the reverse, with a\n    two-sided paired t test of the counts at p < 0.05 (Methods, Quantification and statistical\n    analysis); the paper reports no test, so the test is its general one.\n- id: fig3b-low-conductivity-halves-threshold\n  statement: Replacing NaCl with sodium gluconate, lowering conductivity from 16.4 to 8.4 mS/cm,\n    reversibly lowered excitation thresholds about 2-fold at all sine wave frequencies from 2 to\n    20 kHz.\n  source: Results, Decreased extracellular conductivity lowers excitation thresholds, paragraph 1;\n    Figures 3A and 3B\n  quote: Switching to the NaGlu-based solution reversibly and reproducibly decreased excitation\n    thresholds ~2-fold across all sine wave frequencies tested\n  data: elsewhere\n  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)\n  expected:\n    quantity: ratio of NaCl to NaGlu 1-AP threshold, each frequency\n    value: 2\n    tolerance: 0.2\n  criterion: The 1-AP threshold for 250-ms unmodulated sine waves (Figure 3B legend), as in\n    fig2d-20khz-twofold-threshold, per neuron, frequency and solution; 4 to 8 neurons per point.\n    Reproduced when the ratio of mean NaCl to mean NaGlu threshold is within tolerance at every\n    frequency tested; partially reproduced when it is above 1 at every frequency but outside\n    tolerance at some.\n- id: fig3c-sustained-firing-2s\n  statement: In the low-conductivity solution, a 2-s unmodulated 2-kHz sine wave ramped up over\n    250 ms evoked sustained firing for the whole stimulus; firing rate rose with field strength\n    until replaced by a firing block with sustained depolarization, which developed before the end\n    of the ramp.\n  source: Results, Decreased extracellular conductivity lowers excitation thresholds, paragraph 3;\n    Figure 3C\n  quote: we observed sustained firing for the entire duration of the sine wave ( Figure 3C ). The rate\n    of firing increased with the electric field strength until it was replaced by a firing block\n    and sustained depolarization. The block had already developed before the end of the 250-ms\n    ramp-up period\n  data: elsewhere\n  where: DANDI:001030 (assigned from its title)\n  criterion: Traces corrected for bleaching by subtracting a trace without APs (Methods); AP\n    detection as in fig1-pure-sine-excites-all, both readings. Reproduced when (i) at an\n    intermediate field, APs occur in the last 250 ms of the 2-s stimulus, (ii) the AP count rises\n    with field up to some field, and (iii) at the highest field there are no APs after 250 ms with\n    dF above F0 by more than 5% (as in fig1-excitation-block) over the rest of the stimulus.\n- id: figs1-di8-anepps-control\n  statement: With Di-8-ANEPPS instead of FluoVolt, in eight neurons, stimulation near threshold\n    elicited one or a few delayed APs and stronger fields induced sustained firing ending in\n    sustained depolarization, as with FluoVolt.\n  source: Results, Sensitivity to unmodulated sine waves was not caused by FluoVolt dye, paragraph 1;\n    Figure S1\n  quote: Stimulation near the threshold elicited one or a few delayed APs. Increasing the electric\n    field strength reduced the delay and induced sustained firing that culminated in sustained\n    depolarization\n  data: elsewhere\n  where: DANDI:001272 (assigned from its title)\n  criterion: Traces inverted, as Di-8-ANEPPS emission falls with depolarization (Methods). AP\n    detection and the tests of fig1-onset-delay and fig1-excitation-block, applied to the eight\n    neurons; the 5% dF level is the FluoVolt one, and the paper notes Di-8-ANEPPS is less\n    sensitive, so the readings add a level of 5 times the pre-stimulus SD of each trace.\n    Reproduced when, under one reading, every neuron is excited, latency falls with field in more\n    than half, and the highest field meets the block test in more than half.\n- id: figs2-ttx-blocks-depolarization\n  statement: 1 uM tetrodotoxin abolished both the APs and the sustained depolarization caused by\n    intense unmodulated 2-kHz sine waves.\n  source: Results, Tetrodotoxin blocks sustained depolarization, paragraph 1; Figure S2\n  quote: the inhibition of sodium channels with 1 μM tetrodotoxin not only abolished the APs but also\n    fully blocked the sustained depolarization\n  data: elsewhere\n  where: DANDI:001271 (assigned from its title)\n  criterion: Per neuron, the session in normal solution and the session about 5 min after TTX at\n    the same field (Figure S2 legend). Reproduced when, in every TTX neuron, APs (detection as in\n    fig1-pure-sine-excites-all) present before are absent after, and the mean dF over the last\n    100 ms of the stimulus (as in fig1-excitation-block) is above 5% before and below 5% after,\n    while the vehicle neuron keeps its response.\n- id: fig4-orientation-time-constants\n  statement: Elongated neurons aligned with the field have about twice the charging and discharging\n    time constants of the same cells perpendicular to it, or of randomly shaped cells.\n  source: Results, Kinetics of membrane charging by pulsed electric fields, paragraph 3; Figures 4A,\n    4D and 4E\n  quote: Aligning elongated cells with the electric field doubled the time constants, as compared to\n    either the same cells oriented perpendicular to the field ( p < 0.001, paired t test) or to\n    randomly shaped cells ( p < 0.01, unpaired t test)\n  statistics:\n  - about: elongated cells, parallel against perpendicular\n    test: paired t test\n    p: 0.001\n    p_relation: \"<\"\n  - about: elongated parallel cells against random cells\n    test: unpaired t test\n    p: 0.01\n    p_relation: \"<\"\n  data: elsewhere\n  where: DANDI:001273 (assigned from its title)\n  expected:\n    quantity: ratio of parallel to perpendicular time constants\n    value: 2\n    tolerance: 0.2\n  criterion: Per cell, pole and orientation, dF in the most de- and hyperpolarized ROIs averaged\n    over the eight replicates and fitted with dF = dFmax (1 - exp(-t/tau)) during the pulse and\n    dF = dFmax exp(-t/tau) after it (Methods), with and without debris scaling. Groups as in the\n    Figure 4D and 4E legend (parallel n = 3, perpendicular n = 6, random n = 10). The legend's n\n    differ, so the paired test is read as on the elongated cells with both orientations; the\n    readings for what is compared are (a) the charging tau, (b) the discharging tau, at each pole.\n    Reproduced when, under each, the parallel mean is within tolerance of twice the perpendicular\n    mean and both tests reach their stated p in at least one pole.\n- id: fig4-no-pole-difference\n  statement: The maximum optical TMP and the charging and discharging time constants did not differ\n    between the cathode- and anode-facing poles, indicating no rectification of the field.\n  source: Results, Kinetics of membrane charging by pulsed electric fields, paragraph 3; Figures 4D\n    and 4E\n  quote: Δ F max did not differ at the cathodic and anodic cell poles, indicating the lack of\n    rectification of the applied electric field. Charging and discharging time constants did not\n    differ between the two poles either\n  data: elsewhere\n  where: DANDI:001273 (assigned from its title)\n  depends_on:\n  - fig4-orientation-time-constants\n  criterion: A claim of absence. The paper does not name the test; the Methods use a two-sided\n    Student's t test, paired or unpaired as appropriate, at p < 0.05, and the two poles are in\n    the same cell, so the test is a two-sided paired t test over all 19 cells of |dFmax|, charging\n    tau and discharging tau, cathodic against anodic. Fits as in fig4-orientation-time-constants.\n    Reproduced when none of the three is significant; the mean differences are given either way.\n- id: fig4-discharging-slower\n  statement: Discharging time constants were larger than charging ones in the same cell, except in\n    elongated cells aligned with the field.\n  source: Results, Kinetics of membrane charging by pulsed electric fields, paragraph 3; Figures 4D\n    and 4E\n  quote: discharging time constants were always larger than the charging ones in the same cell ( p <\n    0.001, paired t test), with the exception of elongated cells aligned with the field\n  statistics:\n  - test: paired t test\n    p: 0.001\n    p_relation: \"<\"\n  data: elsewhere\n  where: DANDI:001273 (assigned from its title)\n  depends_on:\n  - fig4-orientation-time-constants\n  criterion: Fits as in fig4-orientation-time-constants. Two-sided paired t test of discharging\n    against charging tau over cells and poles. The pooling is not given; readings (a) all 19 cells,\n    both poles, (b) the cells other than elongated parallel ones, both poles, (c) as (b), each pole\n    alone (the legend's # marks p < 0.01 per group). Reproduced when, under one reading,\n    discharging tau is larger with p < 0.001, and the parallel group shows no significant\n    difference at p < 0.05.\n- id: fig4-pooled-time-constants\n  statement: Pooled over all 19 cells, the charging and discharging time constants were 0.7 and\n    0.91 us at the cathodic pole and 0.65 and 0.8 us at the anodic pole, so membranes charge fully\n    within 3 us.\n  source: Results, Kinetics of membrane charging by pulsed electric fields, paragraph 3; Figures 4D\n    and 4E (ALL)\n  quote: The time constants pooled together for all cells averaged 0.7 ± 0.08 (charging) and 0.91 ±\n    0.08 (discharging) μs for the cathodic cell pole and 0.65 ± 0.05 and 0.8 ± 0.07 μs for the\n    anodic pole, respectively (mean ± SEM, n = 19)\n  data: elsewhere\n  where: DANDI:001273 (assigned from its title)\n  depends_on:\n  - fig4-orientation-time-constants\n  expected:\n  - quantity: charging tau, cathodic pole\n    value: 0.7\n    tolerance: 0.08\n    unit: us\n  - quantity: discharging tau, cathodic pole\n    value: 0.91\n    tolerance: 0.08\n    unit: us\n  - quantity: charging tau, anodic pole\n    value: 0.65\n    tolerance: 0.05\n    unit: us\n  - quantity: discharging tau, anodic pole\n    value: 0.8\n    tolerance: 0.07\n    unit: us\n  criterion: Fits as in fig4-orientation-time-constants; for random cells both field orientations\n    are pooled (Figure 4D and 4E legend). Whether ALL averages per cell or per cell and\n    orientation is open; readings (a) the mean over the 19 cells of each cell's mean over its\n    orientations, (b) the mean over all cell and orientation fits. Reproduced when, under one\n    reading, all four are within tolerance (the SEMs the paper gives).\n- id: fig5-carrier-antiphasic\n  statement: During a single beat of a 2-kHz sine wave, the optical TMP in ROIs 1 and 2 oscillates\n    with the carrier in opposite phases, with amplitude proportional to the sine wave amplitude,\n    on top of a gradual whole-cell depolarization.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraph 2; Figures 5C, 5D and 5H\n  quote: Optical TMP oscillated in synchrony with the carrier sine wave in the opposite phases ...\n    These oscillations, proportional to the sine wave amplitude, were superimposed on the gradual\n    depolarization of the entire cell\n  criterion: Cell C7 (O4), both modulation rates (100 and 154 Hz), dF per frame averaged over its\n    sessions, LOESS-subtracted (O2, all readings). Reproduced when, under every reading, (i) the\n    largest peak of the power spectrum of each subtracted trace above 500 Hz is at 2 kHz within one\n    frequency bin, (ii) the Pearson correlation of the ROI 1 and ROI 2 subtracted traces is below\n    zero with p < 0.05 (the Methods' level), and (iii) the regression of fig6c-sine-sensitivity\n    (O3, reading a) has opposite signs in the two ROIs. The whole-cell depolarization is tested\n    in fig5-whole-cell-depolarization.\n- id: fig5-whole-cell-depolarization\n  statement: During the sine wave beat the whole cell gradually depolarizes as the sine wave\n    amplitude grows, then repolarizes.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraph 2; Figures 5C and 5D\n  quote: These high-frequency oscillations superimpose a gradual whole-cell depolarization that\n    develops as the sine wave amplitude increases\n  criterion: Cell C7 (O4), each modulation rate and ROI. The whole-cell response is the LOESS fit\n    of the raw dF (Figure 5 legend; O2, all readings), fitted per session. The paper gives no test;\n    its general test is the two-sided t test at p < 0.05 (Methods). The measure is open; readings\n    (a) the mean of the LOESS fit over the beat, (b) the LOESS fit at the beat's peak (half the\n    beat), each tested against zero over sessions with a one-sample two-sided t test. Reproduced\n    when, under every reading, both ROIs are depolarized (positive, FluoVolt emission rising with\n    depolarization) with p < 0.05 at both rates; partially reproduced when that holds at one rate.\n    The same measure in the other eight cells is reported.\n- id: fig5-sine-asymmetry-c7\n  statement: In the cell of Figure 5, the 2-us pulse depolarized ROI 2 about 30% less than it\n    hyperpolarized ROI 1, while the sine wave oscillations in ROI 2 were up to 90% smaller than\n    in ROI 1.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraphs 1 and 2; Figures 5B to 5D\n  quote: Unexpectedly, in this cell, the oscillations in ROI 2 were up to 90% smaller than those in\n    ROI 1 (compared to just 30% smaller when the same cell was polarized with the 2-μs pulse)\n  depends_on:\n  - fig6c-sine-sensitivity\n  expected:\n  - quantity: pulse, 1 - |dF ROI 2| / |dF ROI 1|\n    value: 30\n    tolerance: 3\n    unit: percent\n  - quantity: sine wave, largest 1 - (ROI 2 oscillation / ROI 1 oscillation)\n    value: 90\n    tolerance: 9\n    unit: percent\n  criterion: Cell C7 (O4). Pulse, readings (p1) the dF averaged 1 to 2 us into the pulse (Figure 6B\n    measure), (p2) the largest |dF| of the 5-point running average during the pulse (Figure 5B\n    legend). Sine wave, at 100 and 154 Hz, the larger of the two reductions, under readings (s1)\n    the ratio of the ROIs' sensitivities as in fig6c-sine-sensitivity (O3 a and b), (s2) per\n    carrier cycle half the peak-to-peak of the subtracted dF, taking the largest reduction over\n    cycles whose ROI 1 amplitude is at least half its maximum (\"up to\"). Each with all O2\n    readings. Reproduced when both values are within tolerance under one pulse and one sine\n    reading for every O2 reading.\n- id: figs3-sine-asymmetry-c8\n  statement: In a second neuron (Figure S3), polarization in ROI 1 was 20% smaller than in ROI 2\n    with the 2-us pulse and 40% smaller with sine waves, and the antiphasic oscillations did not\n    move to a new area.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraph 3; Figure S3\n  quote: With the 2-μs pulse, polarization in ROI 1 was 20% smaller than in ROI 2 ( Figure S3B );\n    however, with sine waves, it became 40% smaller\n  depends_on:\n  - fig5-sine-asymmetry-c7\n  expected:\n  - quantity: pulse, 1 - |dF ROI 1| / |dF ROI 2|\n    value: 20\n    tolerance: 2\n    unit: percent\n  - quantity: sine wave, 1 - (ROI 1 oscillation / ROI 2 oscillation)\n    value: 40\n    tolerance: 4\n    unit: percent\n  criterion: Cell C8 (O4), measures and readings as in fig5-sine-asymmetry-c7, except that the\n    sine wave value is not qualified by \"up to\", so reading (s2) uses the median over cycles whose\n    ROI 2 amplitude is at least half its maximum. Reproduced when both values are within tolerance\n    under one pulse and one sine reading for every O2 reading. The part on migration needs the\n    ROIs of Figure S3E and S3F and is reported, not judged, as their positions are only in the\n    figure.\n- id: fig5fg-no-migration\n  statement: Over 16 further ROIs around the cell of Figure 5, strong oscillations were found on one\n    side only, and the relatively large oscillations of ROIs 12 to 14 on the other side were not\n    antiphasic to them, so the small ROI 2 oscillations did not come from migration of the\n    polarized area.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraph 2; Figures 5E to 5G\n  quote: strong oscillations were observed on one side only ( Figure 5F ), and the relatively large\n    oscillations in ROIs 12-14 in Figure 5G were not antiphasic to those in Figure 5F\n  depends_on:\n  - fig6c-sine-sensitivity\n  criterion: Needs the 16 ROIs of Figure 5E with the paper's numbering (O1); blocked as\n    metadata_insufficient if the dataset lacks them. Cell C7, the 154-Hz beat (Figures 5F and 5G\n    are \"same as (D)\"), sensitivity per ROI as in fig6c-sine-sensitivity with its sign (O2 and O3\n    readings). Reproduced when, under every reading, the signed sensitivities of ROIs 12, 13 and\n    14 have the sign of the Figure 5F ROIs' median, and the largest |sensitivity| among the\n    Figure 5G ROIs is below the largest among the Figure 5F ROIs.\n- id: fig6b-pulse-sensitivity\n  statement: The FluoVolt response to 2-us pulses, averaged 1 to 2 us into the pulse, ranged from\n    15% to 47% per 1 kV/cm, averaging 28% plus or minus 2.5% over all ROIs in the nine cells.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraph 4; Figure 6B\n  quote: The electric field sensitivity of FluoVolt ranged between a 15% and 47% change per 1 kV/cm,\n    with an average value of 28% ± 2.5% across all ROIs in all the cells\n  expected:\n    quantity: mean pulse sensitivity over the 18 ROIs\n    value: 28\n    tolerance: 2.5\n    unit: percent per kV/cm\n  criterion: Per cell C1 to C9 and ROI 1 and 2 (O1), |dF| averaged over the 21 frames from 1 to 2 us\n    into the 257 V/cm pulse, divided by 0.257 kV/cm (or the field recorded for the cell), with and\n    without debris scaling. Reproduced when, under one of the two, the mean over the 18 ROIs is\n    within tolerance (the SEM the paper gives) and every ROI lies within 13.5% to 51.7% (15% to 47%\n    widened by 10% of each bound).\n- id: fig6c-sine-sensitivity\n  statement: The sine-wave-induced TMP oscillations were linearly correlated with the electric field\n    (p below 0.01% for both ROIs in eight of the nine cells), with sensitivities from 1.5% to\n    28.4% per 1 kV/cm.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraph 5; Figure 6C\n  quote: The oscillations displayed a robust linear correlation with the electric field ... <0.01% for\n    both ROIs in eight cells. The regression coefficient, which was the FluoVolt sensitivity to sine\n    waves, varied from 1.5% to 28.4%\n  statistics:\n  - test: linear regression of emission change on electric field strength\n    p: 0.0001\n    p_relation: \"<\"\n    n: both ROIs in eight of the nine cells\n  criterion: Per cell C1 to C9 and ROI 1 and 2 (O1), the 2-kHz beat modulated at 100 Hz (Figure 6C\n    legend), dF from the sine wave F0, averaged over sessions, LOESS-subtracted (O2), regressed on\n    the field (O3, readings a and b, with and without debris scaling); sensitivity is |slope| in %\n    per kV/cm. Reproduced when, under every O2 and O3 reading, both ROIs have p < 0.0001 in at least\n    eight cells and every sensitivity lies within 1.35% to 31.2% (1.5% to 28.4% widened by 10% of\n    each bound); blocked as methods_underspecified when the readings disagree.\n- id: fig6d-sine-less-than-pulse\n  statement: Every ROI's sensitivity to sine waves was smaller than to the pulse; averaged over all\n    ROIs it was 11.8% plus or minus 1.7% per 1 kV/cm, 42% of the pulse value.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraph 5; Figures 6C and 6D\n  quote: All numbers were invariably smaller than those measured for the same ROIs with the pulse (\n    Figure 6D ). The electric field sensitivity averaged across all ROIs in all the cells was 11.8% ±\n    1.7% per 1 kV/cm, just 42% of the value for the 2-μs pulses\n  depends_on:\n  - fig6b-pulse-sensitivity\n  - fig6c-sine-sensitivity\n  expected:\n  - quantity: mean sine wave sensitivity over the 18 ROIs\n    value: 11.8\n    tolerance: 1.7\n    unit: percent per kV/cm\n  - quantity: mean sine sensitivity over mean pulse sensitivity\n    value: 42\n    tolerance: 4.2\n    unit: percent\n  criterion: Sensitivities as in fig6b-pulse-sensitivity and fig6c-sine-sensitivity, with the same\n    scaling in both. The Figure 6D legend's \"ratio of values in (D) and (C)\" is read as sine (C) over\n    pulse (B). Reproduced when, under every O2 and O3 reading, the sine to pulse ratio is below 1 in\n    all 18 ROIs and both expected values are within tolerance; blocked as methods_underspecified\n    when the readings disagree.\n- id: threshold-depolarization-estimate\n  statement: Combining the sine wave sensitivity (11.8% per kV/cm) with the 2-kHz AP threshold\n    (57.7 V/cm) gives a 0.68% emission change, about 6.8 mV at FluoVolt's calibration of about 10%\n    per 100 mV, so the threshold depolarization is 5 to 15 mV.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraph 6\n  quote: This threshold corresponds to a 0.68% ± 0.11% FluoVolt emission change (11.8 × 57.7/1,000)\n    ... a 0.68% emission change corresponds to a 6.8-mV depolarization at the AP threshold\n  data: elsewhere\n  where: DANDI:001032, 001033, 001034 and 001035 for the threshold (assigned from their titles); the\n    sensitivity from this dataset\n  depends_on:\n  - fig6d-sine-less-than-pulse\n  - threshold-2khz-unmodulated\n  expected:\n  - quantity: emission change at the 2-kHz AP threshold\n    value: 0.68\n    tolerance: 0.11\n    unit: percent\n  - quantity: depolarization at the 2-kHz AP threshold\n    value: 6.8\n    tolerance: 0.68\n    unit: mV\n  criterion: The product of the mean sine wave sensitivity of fig6d-sine-less-than-pulse and the\n    mean threshold of threshold-2khz-unmodulated, divided by 1,000, and that times 10 mV per 1%\n    (the calibration of reference 47, as the paper uses it). Reproduced when both are within\n    tolerance under one reading of each claim it depends on.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001274/10.1016-j.xcrp.2025.102660.yaml paper/10.1016-j.xcrp.2025.102660.txt; grep -n -- "—\|rather" claims/001274/*.yaml; python - <<'E'
import yaml,re
d=yaml.safe_load(open('claims/001274/10.1016-j.xcrp.2025.102660.yaml'))
print(len(d['claims']))
E
grep -nE "^\s+[a-z_]+: .*[^\"']: " claims/001274/*.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001274/10.1016-j.xcrp.2025.102660.yaml",
 "old_string": "(the legend's # marks p < 0.01 per group)",
 "new_string": "(the legend's hash sign marks p < 0.01 per group)"
}
```

```
The file claims/001274/10.1016-j.xcrp.2025.102660.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001274/10.1016-j.xcrp.2025.102660.yaml paper/10.1016-j.xcrp.2025.102660.txt; grep -n -- "—\|rather\| #" claims/001274/*.yaml | grep -v "^[0-9]*:#"; python - <<'E'
import yaml
d=yaml.safe_load(open('claims/001274/10.1016-j.xcrp.2025.102660.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c))
E
grep -nE "^ +(statement|source|quote|criterion|quantity|where|n|about|test): [^\"'].*: " claims/001274/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001274/10.1016-j.xcrp.2025.102660.yaml",
 "old_string": "    significantly higher than those for pure sine waves at the same frequency (for 2 kHz, 5 APs\n    p = 0.0079; for 20 kHz, 1 and 5 APs, respectively p = 0.0142 and p = 0.0037)",
 "new_string": "    significantly higher than those for pure sine waves at the same frequency (for 2 kHz, 5 APs\n    ... p = 0.0079; for 20 kHz, 1 and 5 APs, respectively ... p = 0.0142 and p = 0.0037)"
}
```

```
The file claims/001274/10.1016-j.xcrp.2025.102660.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001274/10.1016-j.xcrp.2025.102660.yaml paper/10.1016-j.xcrp.2025.102660.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
git status --short
```

```
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
?? claims/001274/
?? scripts
```

**Agent**

I wrote `claims/001274/10.1016-j.xcrp.2025.102660.yaml`. The quote checker reports 26 claims, 26 quotes, 8 statistical values and 0 problems. Nothing was committed.

**Text read.** I read the NIH author manuscript (NIHMS2098259, PMC12320893) from Europe PMC: main text, figure legends, STAR Methods, and the supplement (Figures S1 to S4 and Table S1). I did not read the version of record. There was no PDF of the main text, so I could not look at Figures 1 to 6, and numbers shown only in figures are not used. The paper says it reports no original code, so there was no code to read.

**What this dataset holds.** The paper put its raw images in ten dandisets without saying which figure is in which. Going by its title and description, 001274 holds the strobe recordings of sine-wave polarization, the sine-wave part of Figures 5, 6 and S3. I assigned the other figures to the other dandisets from their titles alone:
- 001032 to 001035: Figures 1, 2, 3A and 3B
- 001030: Figure 3C
- 001271: Figure S2
- 001272: Figure S1
- 001273: Figure 4

Those 18 claims are marked `data: elsewhere`. The 8 claims on Figures 5, 6 and S3 are marked `dataset`. They also need the 2-µs pulse recordings of the same cells, which may be in 001274 or in 001273.

**Counts.**
- 26 claims, all with quotes, none inferred.
- 5 claims carry statistics, 8 entries in all: the t tests for Figure 2D (four), Figure 4 (three), and the regression for Figure 6C. For Figure 6C the paper prints the p-value as "<0.01%", recorded as `p: 0.0001`. The checker passed it, probably by matching another "p < 0.0001" in the text, so that value needs checking by reading.
- All 26 claims have a criterion.

**Details the paper leaves open, and the readings named:**
- **ROIs (O1):** their size and position are not given. The ROIs must come from the dataset. If it has none, the claims are blocked as `metadata_insufficient`, and an ROI rebuilt from the RATIO image is shown only as a variant.
- **LOESS fit (O2):** span and degree are not given. Readings are R's loess defaults (span 0.75), since Table S1 lists RStudio, plus spans 0.5 and 0.25.
- **How the field enters the Figure 6C regression (O3):** (a) frame by frame against the signed instantaneous field; (b) per carrier cycle, oscillation amplitude against the cycle's peak field, with and without an intercept.
- **Which recording is cell C7 or C8 (O4):** to be found from the dataset, using the pulse field, the peak field and the session count.
- **Debris scaling:** the paper processed data both with and without it, so both are run.
- **AP detection:** the paper says only "brief emission upticks" in neurons whose APs exceed 5% ΔF. Readings are a peak above 5% over F0, or a rise of 5% within 5 ms.
- **"Up to 90%" smaller (Figure 5):** read either as the ratio of the two ROIs' sensitivities, or as the largest per-cycle reduction.
- **Pulse asymmetry measure:** ΔF averaged from 1 to 2 µs into the pulse (Figure 6B), or the peak of the 5-point running average (Figure 5B).
- **Figure 4:** the legend gives n = 3 parallel and n = 6 perpendicular cells, yet the comparison is a paired test, so it is read as using cells with both orientations. The pooling for "discharging slower" and for the "ALL" averages has two or three readings each.
- **Figure 6D legend:** it says "ratio of (D) and (C)"; I read it as Figure 6C over 6B.
- **Volts to V/cm:** the paper shows the conversion only in Figure S4C. The dataset metadata is used (the 001030 description says 1 V = 36 V/cm).
- **Thresholds I set myself:** some criteria use windows or thresholds the paper does not fix. They are named in the criteria, not presented as the paper's:
  - the 5% depolarization block test
  - the "near the beat peak" window with an 80% share
  - the Spearman test of latency against field
  - the paired t test on AP counts in Figure 2C, which applies the paper's general test because it reports none for that panel

**Missing from the paper.** Nothing that blocks writing the claims; the full text, Methods and supplement were all present. Group sizes for Figure 2D and per-cell values for Figures 4 and 6 appear only in figures, so they could not be used. Which dandiset holds which figure is not stated anywhere. I left out the heating estimates, which are calculations and not measurements.

## End of run

24 turns, 6 minutes, result: success.
