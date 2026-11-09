# crcns-alm-3 · claims · run 42404175158

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453/ claims/ | head -50; ls paper/ claims/crcns-alm-3 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 185
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/001453/; ls claims | grep -i crcns; wc -c paper/*.txt; head -30 paper/10.1038-nature17643.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
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
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; awk '{print NR": "length($0)}' paper/10.1038-nature17643.txt | sort -t: -k2 -n -r | head; head -c 3000 paper/alm-3.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 7p paper/10.1038-nature17643.txt | cut -c1-30000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 7p paper/10.1038-nature17643.txt | fold -s -w 200 > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; sed -n 1,150p $TMPDIR/p.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 150,448p $TMPDIR/p.txt
```

```
<persisted-output>
Output too large (58.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4cecba25-1380-46f4-909a-ff40ab30b0ba/tool-results/btkvjxwkn.txt

Preview (first 2KB):
ALM silenced by photoinhibition, we estimated the boundaries of ALM using photoinhibition behavioral data from 3 . ALM was defined as the area where photoinhibition over the entire delay epoch 
produced significant behavioral effects. ALM boundaries ( Fig. 1b , grey area) were derived by deconvolving the area producing significant behavioral effects with the point-spread function of the 
photoinhibition method ( Extended Data Fig. 2d ) 3 . At 80% activity reduction, photoinhibition with 1 laser spot covered 58% of ALM in one hemisphere ( Fig. 1b ). Photoactivation For photoactivation 
we stimulated layer 5 intratelencephalic neurons in Tlx_PL56-cre mice 46 crossed to reporter mice expressing ChR2 (Ai32) 30 . The delay epoch was 1.3 s long. The photostimulus was a 20 Hz sinusoid 
(0.53 mW average power) applied during different task epochs ( Extended Data Fig. 5b ). Photoactivation was deployed on 40% of the behavioral trials during electrophysiology. Electrophysiology A 
small craniotomy (diameter, 1 mm) was made over left ALM (centered on 2.5 mm anterior, 1.5 mm lateral) one day prior to the recording session 3 . Extracellular spikes were recorded using NeuroNexus 
silicon probes (Part# A4×8-5mm-100-200-177). The 32 channel voltage signals were multiplexed, digitized by a PCI6133 board at 312.5 kHz (National instrument) at 14 bit, demultiplexed (sampling at 
19531.25Hz) and stored for offline analysis. Three to seven recordings were made from each craniotomy. To minimize brain movement, a drop of silicone gel (3-4680, Dow Corning, Midland, MI) was 
applied over the craniotomy after the electrode was in the tissue. The tissue was allowed to settle for several minutes before the recording started. During electrophysiology, photoinhibition was 
deployed on
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4cecba25-1380-46f4-909a-ff40ab30b0ba/tool-results/btkvjxwkn.txt"
}
```

```
1	ALM silenced by photoinhibition, we estimated the boundaries of ALM using photoinhibition behavioral data from 3 . ALM was defined as the area where photoinhibition over the entire delay epoch 
2	produced significant behavioral effects. ALM boundaries ( Fig. 1b , grey area) were derived by deconvolving the area producing significant behavioral effects with the point-spread function of the 
3	photoinhibition method ( Extended Data Fig. 2d ) 3 . At 80% activity reduction, photoinhibition with 1 laser spot covered 58% of ALM in one hemisphere ( Fig. 1b ). Photoactivation For photoactivation 
4	we stimulated layer 5 intratelencephalic neurons in Tlx_PL56-cre mice 46 crossed to reporter mice expressing ChR2 (Ai32) 30 . The delay epoch was 1.3 s long. The photostimulus was a 20 Hz sinusoid 
5	(0.53 mW average power) applied during different task epochs ( Extended Data Fig. 5b ). Photoactivation was deployed on 40% of the behavioral trials during electrophysiology. Electrophysiology A 
6	small craniotomy (diameter, 1 mm) was made over left ALM (centered on 2.5 mm anterior, 1.5 mm lateral) one day prior to the recording session 3 . Extracellular spikes were recorded using NeuroNexus 
7	silicon probes (Part# A4×8-5mm-100-200-177). The 32 channel voltage signals were multiplexed, digitized by a PCI6133 board at 312.5 kHz (National instrument) at 14 bit, demultiplexed (sampling at 
8	19531.25Hz) and stored for offline analysis. Three to seven recordings were made from each craniotomy. To minimize brain movement, a drop of silicone gel (3-4680, Dow Corning, Midland, MI) was 
9	applied over the craniotomy after the electrode was in the tissue. The tissue was allowed to settle for several minutes before the recording started. During electrophysiology, photoinhibition was 
10	deployed on 40% of the trials to obtain a larger number of trials per condition. Three photoinhibition conditions were tested during each recording session. In the unilateral photoinhibition 
11	experiment 
[... 289 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '8,113p' paper/10.1038-nature17643.txt | cut -c1-250
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 45,285p paper/alm-3.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; ls claims/crcns-fcx-1; head -40 claims/crcns-fcx-1/*.yaml
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

[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 40,140p claims/crcns-fcx-1/*.yaml; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:5000])"
```

```
# Shared method details, used by the criteria below.
# M1. Cells and sessions. Statistics are per cell on pE cells unless stated (Results, Assessment of
#   firing patterns). Analyses are confined to WAKE-SLEEP cycles (Supplemental Experimental
#   Procedures, Brain state scoring). A cell's rate in a state is its spike count over the summed
#   duration of that state's intervals. The paper does not say whether a cell recorded across two
#   WAKE-SLEEP cycles enters a per-episode comparison once per episode or once with its episodes
#   averaged; readings (a) one entry per cell and episode, (b) one per cell, averaged over episodes.
# M2. Sextiles. pE cells from the whole data set are split into six equal groups by WAKE firing
#   rate (Results, Firing pattern and LFP changes across the course of sleep; Fig. 2A legend;
#   Experimental Procedures), kept for all later analyses. "General WAKE firing rate" is read as the
#   rate over all WAKE intervals of the cell's session; reading (b) is the rate over the WAKE of
#   each cycle. The Fig. 2F groups are "based on mean rate", read as the same WAKE sextiles; reading
#   (b) is sextiles of the nonREM rate. Sextile numbers differ between figures: Figure S2 numbers
#   1 as the lowest rate (1 pE Low FR, 6 pE High FR), the Figure S5 legend says sextile 1 is the
#   highest. Criteria name sextiles by rate (top, bottom), or say which numbering they use.
# M3. Time-normalized correlations. SLEEP, nonREM episodes and packets are time-normalized to 0 to 1
#   and, for SLEEP, only nonREM time is used (Results, Firing pattern and LFP changes across the
#   course of sleep; Fig. 3B legend). Correlations are Pearson (Fig. 3B legend). The unit of a sample
#   in these correlations is not stated. Readings, (a) one point per nonREM packet (its mean value at
#   its normalized mid-time); (b) one point per 10 s bin of nonREM (the bin the Supplemental
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[5000:])"
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

The full text (author manuscript, Methods and Extended Data legends) is present and the paper links no code. Writing the claims file now.

**Agent calls Bash**

```bash
cd  grep -o "Corrigendum[^.]*" paper/10.1038-nature17643.txt | head -3; grep -c "" paper/10.1038-nature17643.txt; grep -n -i "code\b\|github\|matlab" paper/10.1038-nature17643.txt | cut -c1-200 | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-alm-3/10.1038-nature17643.yaml",
 "content": "# Claims for Li, Daie, Svoboda & Druckmann (2016), Nature 532, 459-464, \"Robust neuronal dynamics\n# in premotor cortex during motor planning\", doi:10.1038/nature17643, on CRCNS data set alm-3\n# (doi:10.6080/K0RB72JW).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-07,\n# protocol as stated in docs/protocol.md (Reader), version pilot-13.\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC5081260, NIHMS767125), as supplied\n# under paper/ (Europe PMC): main text, Methods, and the legends of Figures 1 to 6 and Extended Data\n# Figures 1 to 10. The paper has no separate Supplementary Information. No PDF of the paper was\n# supplied, so values printed only inside figures (per-condition performance in Fig. 1d and 5b,\n# fractions in ED Fig. 8a and 8b) were not read; claims on those panels rest on the text and\n# legends. The version of record was not read. The record lists a corrigendum\n# (doi:10.1038/nature18623) whose text was not supplied or read.\n#\n# Code. The paper links no analysis or simulation code. The CRCNS data set's description says it\n# holds MATLAB analysis scripts that reproduce the paper's figures; they are files of the data set\n# and were not read here. Every method below is from the paper's text.\n#\n# Data the paper used. 33 mice (age > P60). Electrophysiology during behaviour, left ALM, 12 mice\n# (5 VGAT-ChR2-EYFP, 7 PV-ires-cre x ReaChR), NeuroNexus 32-channel probes: 1012 single units in 58\n# sessions (20 unilateral, Experiment 1, Fig. 1; 38 bilateral, Experiments 2 and 3, Fig. 2 and ED\n# Fig. 7); 890 putative pyramidal (spike width > 0.45 ms), 72 FS (< 0.35 ms), 50 excluded.\n# Callosotomy, 7 mice (6 VGAT, 1 PV x ReaChR), recorded daily for 5 to 7 days from about 17 h after\n# the cut. Photoactivation (ED Fig. 5), 2 Tlx_PL56-cre x Ai32 mice. Behaviour-only photoinhibition\n# mice (Fig. 1d, 2b, ED Fig. 3) and 4 untrained mice for the spatial extent of photoinhibition (ED\n# Fig. 2d). Task: pole location discrimination, sample epoch 1.3 s, delay 1.3 s (Experiment 1),\n# 1.7 s (Experiments 2, 3), 1.2 to 1.7 s (ED Fig. 3c), auditory go cue, lick right (posterior) or\n# lick left (anterior). Photoinhibition on 40% of trials during electrophysiology. Experiment 1:\n# left ALM, 1 spot, 0.5 s with 100 ms ramp, in sample, early delay or a third delay window.\n# Experiment 2: 0.8 s with 200 ms ramp from delay onset, left ALM 1 spot (ipsilateral), right ALM 1\n# spot (contralateral), bilateral 4 spots per side. Experiment 3: ipsilateral 4 spots, contralateral\n# 4 spots, bilateral 1 spot. Variables: spike times per unit and trial, trial type, outcome (correct,\n# error, lick early), photostimulus condition, epoch times, licks. By its description the data set\n# holds 91 recording sessions from 19 mice (the 12 electrophysiology mice and the 7 callosotomy\n# mice), with spike times, cell type, trial types, photostimulation type, epoch times and lick\n# traces; its documentation says the behaviour-only sessions and the photoactivation data are not\n# included.\n#\n# Naming of the third Experiment 1 window. The Methods name the windows by when they end before the\n# go cue, 1.6 s (sample), 0.8 s (early delay), 0.3 s (late delay) and 0 s (before cue); the Results\n# call the window ending at the cue \"late delay\" and the one ending 0.3 s before it \"middle delay\".\n# The electrophysiology used sample, early delay and the window ending 0.3 s before the cue (it is\n# the one with a recovery time in Fig. 1g). Claims below say which window they mean by its end time.\n#\n# Shared method details, used by the criteria below.\n# M1. Trials. Performance is the fraction correct excluding lick-early trials (Methods, Behavioral\n#   data analysis). Whether lick-early trials enter the electrophysiology analyses is not stated;\n#   readings (a) excluded, as for performance (the data set's documentation also says to exclude\n#   them), (b) included. Selectivity changes under photoinhibition use all trials, correct and\n#   incorrect, grouped by instructed movement (Methods, Electrophysiology data analysis); the\n#   example PSTHs of ED Fig. 1a use correct trials only.\n# M2. Epochs. Sample epoch from pole movement onset to 0.1 s after pole retraction onset (1.3 s);\n#   delay epoch from then to the go cue (Methods, Behavior and surgery). The response epoch's length\n#   is not stated; readings (a) the first 400 ms after the go cue (the window ED Fig. 2e calls the\n#   first 400 ms of the response epoch), (b) the 1.5 s answer window after the go cue.\n# M3. Neurons. Putative pyramidal neurons only, spike width (trough to peak of the mean waveform)\n#   > 0.45 ms (Methods). A neuron is selective when spike counts on lick left and lick right trials\n#   differ by a two-tailed t-test at p < 0.05 in any of the sample, delay or response epochs\n#   (Methods). The trials of this test are not stated; readings (a) correct control trials, (b) all\n#   control trials grouped by instructed movement. Figure legends add \"selective neurons tested for\n#   >3 trials in all conditions\" (Fig. 1g, 2e, ED Fig. 5f, 7d); ED Fig. 2b, 5e and 7c exclude neurons\n#   with mean rate < 1 spike/s, and Fig. 1f, 2d and 5d do not say; readings (a) with that exclusion,\n#   (b) without.\n# M4. Selectivity and its recovery (Methods, Electrophysiology data analysis). Each neuron's\n#   preferred trial type from a subset of 10 trials, selectivity as the rate difference between\n#   preferred and non-preferred types on the remaining trials; delta selectivity is photoinhibition\n#   minus control; s.e.m. by bootstrap over neurons. Open details. Which 10 trials; readings (a) 10\n#   trials of each type drawn at random, (b) 10 trials in total drawn at random. The window that sets\n#   the preference; readings (a) the spike count over sample, delay and response epochs together,\n#   (b) the count in the epoch where the neuron is most selective. The time bins of the selectivity\n#   trace; readings (a) 200 ms windows (the PSTH window of Fig. 1e and ED Fig. 1a), (b) 400 ms\n#   windows (the rate-test window); in 50 ms steps in both (the step of the rate test; a standard\n#   choice). The recovery time is the first bin after photoinhibition offset at which the mean\n#   selectivity on photoinhibition trials reaches 80% of control (Methods), offset being the end of\n#   the ramp (ED Fig. 3b); the time stamp of a window is its centre in reading (a) and its end in\n#   reading (b) of a separate choice the paper leaves open. \"Control selectivity\" is read as the\n#   time-matched control value.\n# M5. Spike-rate change (Methods). Two-tailed t-test of spike counts in 400 ms windows, control\n#   against photoinhibition trials, lick right and lick left pooled, every 50 ms, significant at\n#   p < 0.01.\n# M6. Population analyses (Methods, Analysis of population dynamics). Sessions from the bilateral\n#   experiments (Experiment 2) with > 5 neurons recorded simultaneously for > 5 trials per condition\n#   (16 of 38 sessions; 7 mice). The paper does not say whether FS units enter; readings (a)\n#   putative pyramidal only (M3), (b) all single units. Spike counts in 400 ms windows in 10 ms\n#   steps. cd is the mean over windows in the sample and delay epochs of the difference of mean\n#   response vectors, correct lick right minus correct lick left trials; which windows count as in\n#   those epochs is open, readings (a) windows whose centre lies in them, (b) windows wholly inside\n#   them. cd, decision boundary and session offsets come from one set of control trials, and the\n#   projections from independent control and perturbation trials. The split is not stated; readings\n#   (a) one random half of control trials for cd, the other half projected, (b) leave-one-out over\n#   control trials. Projections are cd^T x on single trials, all trials grouped by instructed\n#   movement, minus the session offset. ROC values compare projections on lick right and lick left\n#   trials in the last 400 ms of the delay epoch, per session, reported as mean +- s.e.m. over\n#   sessions. Movement prediction uses the same window and the decision boundary of the Methods\n#   (the inverse-variance weighted mean of the two class means); a trial is predicted lick right when\n#   its projection lies on the lick right side; it is compared with the lick the mouse made.\n# M7. Behavioural tests. \"Two-tailed t-test against control\" across mice (Methods); whether paired\n#   is not stated, readings (a) paired over mice, (b) unpaired. A mouse's performance is read as\n#   (a) its trials pooled over sessions, (b) the mean of its session values.\n# M8. Tolerances. 10% of the reported value unless a claim says otherwise. Where the paper gives\n#   mean +- s.e.m. the s.e.m. is the tolerance. Counts of deposited units and sessions are exact\n#   (tolerance 0), as the units are sorted and labelled in the data set.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: alm-3\n  doi: 10.6080/K0RB72JW\npaper: doi:10.1038/nature17643\nclaims:\n- id: units-and-sessions\n  statement: 1012 single units were recorded in left ALM during behaviour across 58 sessions (20\n    unilateral, 38 bilateral) from 12 mice; 72 are fast-spiking, 890 putative pyramidal and 50 of\n    intermediate width are excluded.\n  source: Methods, Electrophysiology data analysis, paragraph 1; Results, Preparatory activity in ALM\n  quote: 1012 single units were recorded during behavior across 58 recording sessions (20 sessions\n    of unilateral experiments, Fig. 1 ; 38 sessions of bilateral experiments ... (FS) neurons\n    (72/1012) and units with spike widths > 0.45 ms as putative pyramidal neurons (890/1012). Units\n    with intermediate values (0.35 - 0.45 ms, 50/1012) were excluded\n  expected:\n  - quantity: single units, non-callosotomy experiments\n    value: 1012\n    tolerance: 0\n  - quantity: recording sessions, unilateral experiment\n    value: 20\n    tolerance: 0\n  - quantity: recording sessions, bilateral experiments\n    value: 38\n    tolerance: 0\n  - quantity: putative pyramidal neurons\n    value: 890\n    tolerance: 0\n  - quantity: FS neurons\n    value: 72\n    tolerance: 0\n  - quantity: mice\n    value: 12\n    tolerance: 0\n  criterion: Counts over the non-callosotomy sessions, units classed by the spike-width bounds of the\n    Methods (M3). Reproduced when the counts match; partially reproduced when the unit total matches\n    and the class counts are within 10%.\n- id: ed1-selective-fraction\n  statement: Most ALM pyramidal neurons distinguish trial types (634 of 890), 176 during the sample,\n    337 during the delay and 493 during the response epoch.\n  source: Results, Preparatory activity in ALM; Extended Data Fig. 1b, e\n  quote: Most ALM pyramidal neurons distinguished trial types (634/890, p<0.05, t-test; sample\n    epoch, 176/890; delay epoch, 337/890; response epoch, 493/890, Methods)\n  depends_on:\n  - units-and-sessions\n  expected:\n  - quantity: selective pyramidal neurons, any epoch\n    value: 634\n    tolerance: 63.4\n  - quantity: selective in sample epoch\n    value: 176\n    tolerance: 17.6\n  - quantity: selective in delay epoch\n    value: 337\n    tolerance: 33.7\n  - quantity: selective in response epoch\n    value: 493\n    tolerance: 49.3\n  criterion: Two-tailed t-test on epoch spike counts, lick left against lick right, p < 0.05 (M3),\n    on control trials, under the readings of M1, M2 and M3. Reproduced when all four counts are\n    within tolerance under one reading; partially reproduced when the any-epoch count is.\n- id: fig1d-late-delay-ipsilateral-bias\n  statement: Unilateral photoinhibition (0.5 s) of ALM ending at the go cue causes an ipsilateral\n    response bias.\n  source: Results, Preparatory activity after unilateral silencing, paragraph 1; Figure 1d\n  quote: Transient (duration, 0.5 s) unilateral photoinhibition of ALM up to the ‘go’ cue (late\n    delay) caused an ipsilateral response bias (n = 5 mice, p < 0.01, two-tailed t-test\n  statistics:\n  - test: two-tailed t-test against control\n    p: 0.01\n    p_relation: \"<\"\n    n: 5 mice\n  criterion: Performance (M1) on trials instructing a lick contralateral to the inhibited hemisphere\n    (lick right for left ALM), photoinhibition against control, two-tailed t-test across mice (M7).\n    Reproduced when performance drops with p < 0.01 under one reading. These are behaviour\n    experiments (Fig. 1d, ED Fig. 3); the condition is tested only if the data set holds it.\n- id: fig1d-earlier-photoinhibition-minimal\n  statement: Unilateral photoinhibition ending at least 0.3 s before the go cue (early and middle\n    delay) has minimal behavioural effect.\n  source: Results, Preparatory activity after unilateral silencing, paragraph 1; Figure 1d; Extended\n    Data Fig. 3b, d\n  quote: In contrast, photoinhibition ending at least 0.3 s prior to the ‘go’ cue produced minimal\n    behavioral effects (middle delay, early delay; p > 0.1, two-tailed t-test)\n  statistics:\n  - test: two-tailed t-test against control\n    p: 0.1\n    p_relation: \">\"\n  criterion: A claim of absence, judged on the paper's test. Per condition (window ending 0.8 s and\n    0.3 s before the cue), overall performance (M1), photoinhibition against control, two-tailed\n    t-test across mice (M7 reading a, paired; reading b shown as a variant). Reproduced when p > 0.1\n    for both; not reproduced when either has p < 0.05; the drop in performance is reported either\n    way. The sample-epoch condition is reported as well.\n- id: ed3-recovery-interval\n  statement: Performance is not significantly affected when photoinhibition (0.5 s or 1.3 s) ends\n    more than 0.3 s before the go cue, and 0.5 s of photoinhibition just before the cue has an effect\n    similar to photoinhibition of the whole delay epoch.\n  source: Extended Data Fig. 3b, d, e\n  quote: Performance was not significantly affected for T recovery >0.3s ... Photoinhibition (0.5 s)\n    immediately before the ‘go’ cue is similar to the behavioral effect caused by photoinhibition\n    during the entire delay epoch (1.3 s)\n  criterion: Behaviour-only experiments; the data set's documentation says these sessions are not\n    included. If they are found, judged as fig1d-earlier-photoinhibition-minimal per T recovery\n    (two-tailed t-test, p < 0.05 the threshold of the figure's asterisks).\n- id: ed2b-silencing\n  statement: Photoinhibition silences more than 90% of putative pyramidal activity, similarly with\n    ipsilateral and bilateral photoinhibition and in VGAT-ChR2 and PV x ReaChR mice, while\n    contralateral photoinhibition barely changes the average rate.\n  source: Extended Data Fig. 2b; Methods, Photoinhibition\n  quote: Ipsilateral and bilateral photoinhibition similarly silenced neuronal activity. Average\n    spike rate across the population was little affected by contralateral photoinhibition ...\n    Photoinhibition was similar in the two mouse lines (>90% activity reduction)\n  depends_on:\n  - units-and-sessions\n  expected:\n  - quantity: activity reduction, ipsilateral photoinhibition, Experiment 2\n    value: 0.9\n    tolerance: 0.09\n  criterion: Per neuron, spike rate during photoinhibition over the rate in the same window of\n    control trials (ED Fig. 2b), neurons with mean rate < 1 spike/s excluded; the window is the\n    photoinhibition period before the ramp (a), or the whole period with the ramp (b). Reproduced\n    when the mean normalized rate is at most 0.1 (within tolerance) for ipsilateral and bilateral\n    photoinhibition, the two mouse lines both show more than 80% reduction, and the contralateral\n    mean normalized rate lies within 0.8 to 1.2 (the 10% default applied to 1, doubled since the\n    paper gives no number; stated here as a choice).\n- id: ed2d-spatial-extent\n  statement: The standard photostimulus silences about 90% of spikes in a cortical area of 1 mm\n    radius at half maximum, through all layers.\n  source: Methods, Photoinhibition; Extended Data Fig. 2d\n  quote: The photoinhibition silenced 90% of spikes ( Extended Data Fig. 2b ) in a cortical area of\n    1mm radius (at half-max) through all cortical layers\n  expected:\n  - quantity: radius at half-maximal silencing\n    value: 1\n    tolerance: 0.1\n    unit: mm\n  criterion: Measured in 4 untrained, non-behaving mice (ED Fig. 2d), which the data set's\n    description does not list; tested only if those recordings are found.\n- id: ed2e-no-rebound\n  statement: No rebound excitation is seen on average after photoinhibition offset; a small\n    proportion of neurons show rebound, balanced by low-level sustained inhibition in a larger\n    proportion.\n  source: Extended Data Fig. 2c, e; Results, Preparatory activity after unilateral silencing,\n    paragraph 2\n  quote: No rebound excitation was detected after photoinhibition offset on average ( d ). A small\n    proportion of neurons showed rebound excitation which was balanced by a low level of sustained\n    inhibition in a larger proportion of neurons\n  criterion: Experiment 2, lick right trials, ipsilateral photoinhibition (ED Fig. 2e), windows the\n    first 400 ms and 400 to 800 ms after photoinhibition. Per neuron, a two-tailed t-test of spike\n    counts, control against photoinhibition, p < 0.01 (M5 on lick right trials). Reproduced when\n    the population mean rate after offset is not higher than control by a paired t-test over neurons\n    at p < 0.05 (a standard choice, the paper names no population test) and fewer neurons are\n    significantly excited than significantly suppressed in the first 400 ms after offset.\n- id: fig1f-rate-recovery\n  statement: Within 400 ms after unilateral photoinhibition, spike rates are indistinguishable from\n    control in 90% of neurons; only 10% keep a sustained change.\n  source: Results, Preparatory activity after unilateral silencing, paragraph 2; Figure 1f\n  quote: Within 400 ms after photoinhibition, spike rates became indistinguishable from the\n    unperturbed condition in 90% of the neurons; only 10% of neurons retained a sustained change in\n    spike rate\n  depends_on:\n  - units-and-sessions\n  expected:\n  - quantity: fraction of neurons with a significant rate change 400 ms after offset\n    value: 0.1\n    tolerance: 0.01\n  - quantity: neurons per condition (sample, early delay, delay ending 0.3 s before cue)\n    value: 168\n    tolerance: 0\n  criterion: Experiment 1, per neuron and condition, the rate test of M5. The fraction is over\n    neurons of a condition (n = 168, 168, 175 in Fig. 1f; the inclusion rule is open, M3). Which\n    window is \"within 400 ms after\" is open; readings (a) the 400 ms window starting at offset, (b)\n    the window whose time stamp, by its centre, is 400 ms after offset. Reproduced when, under one\n    reading, the fraction is within tolerance in each condition, or in their mean; partially\n    reproduced when it is below 0.2. The neuron counts are reported beside 168, 168 and 175.\n- id: fig1g-selectivity-recovery\n  statement: After unilateral photoinhibition ALM neurons recover more than 80% of their control\n    selectivity within 514 ms; recovery times are 373 +- 260 ms (sample), 510 +- 218 ms (early\n    delay) and 327 +- 112 ms (window ending 0.3 s before the cue).\n  source: Results, Preparatory activity after unilateral silencing, paragraph 2; Figure 1g\n  quote: ALM neurons recovered > 80% of their selectivity relative to the unperturbed trials within\n    514 ms after photoinhibition\n  depends_on:\n  - units-and-sessions\n  expected:\n  - quantity: recovery time to 80% of control, sample\n    value: 373\n    tolerance: 260\n    unit: ms\n  - quantity: recovery time to 80% of control, early delay\n    value: 510\n    tolerance: 218\n    unit: ms\n  - quantity: recovery time to 80% of control, window ending 0.3 s before cue\n    value: 327\n    tolerance: 112\n    unit: ms\n  - quantity: selective neurons tested for > 3 trials in all conditions\n    value: 55\n    tolerance: 5.5\n  criterion: Experiment 1, selective neurons with > 3 trials in every condition, M4 with all\n    readings. Reproduced when, under one reading, every condition's mean selectivity reaches 80% of\n    control within tolerance of the reported time; partially reproduced when every condition\n    reaches 80% before the go cue.\n- id: ed4-return-to-trajectory\n  statement: Neurons whose rates decrease during the delay epoch also recover after unilateral\n    photoinhibition, returning to the time-matched control trajectory and not decaying to the\n    end-point rate.\n  source: Extended Data Fig. 4b, c; Results, Preparatory activity after unilateral silencing,\n    paragraph 2; Figure 1e\n  quote: Spike rate difference relative to time-matched control show significantly smaller\n    root-mean-squared error (RMS) than spike rate difference relative to end point (p<0.001, paired\n    t-test)\n  statistics:\n  - test: paired t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 27 neurons from 6 mice\n  depends_on:\n  - units-and-sessions\n  expected:\n  - quantity: neurons with a significant delay-epoch decrease\n    value: 27\n    tolerance: 2.7\n  criterion: Experiment 1 pyramidal neurons with rate at the end of the delay lower than at its\n    start (two-tailed t-test, 400 ms windows, trial types pooled, p < 0.05; ED Fig. 4b). Rates\n    normalized to each neuron's mean rate, preferred and non-preferred types separately. Per\n    neuron, RMS over the time from photoinhibition offset to the go cue of (perturbed minus\n    time-matched control) and of (perturbed minus control rate in the last 400 ms of the delay);\n    which photoinhibition conditions are pooled is not stated, readings (a) the early-delay\n    condition, (b) all conditions ending before the cue pooled per neuron. Reproduced when the first\n    RMS is smaller by a paired t-test at p < 0.001 under one reading; partially reproduced at\n    p < 0.05. The same test on neurons with an increasing rate (Fig. 1e, neurons 1 and 2) is shown as\n    a variant.\n- id: ed5-photoactivation\n  statement: After transient photoactivation of layer 5 IT neurons, ALM selectivity recovers to 80%\n    of control in 249 +- 68 ms (sample), 275 +- 168 ms (early delay) and 250 +- 218 ms (middle delay).\n  source: Results, Preparatory activity after unilateral silencing, paragraph 2; Extended Data Fig.\n    5f\n  quote: After photostimulus offset, ALM activity and selectivity recovered with a time-course that\n    was similar to recovery after photoinhibition\n  expected:\n  - quantity: recovery time, sample\n    value: 249\n    tolerance: 68\n    unit: ms\n  - quantity: recovery time, early delay\n    value: 275\n    tolerance: 168\n    unit: ms\n  - quantity: recovery time, middle delay\n    value: 250\n    tolerance: 218\n    unit: ms\n  criterion: M4 on 26 selective neurons from 2 Tlx_PL56-cre x Ai32 mice. The data set's\n    documentation says the photoactivation data are not included; tested only if found.\n- id: fig2b-bilateral-behaviour\n  statement: Unilateral photoinhibition in the early delay reduces performance only slightly (1\n    spot 70.3%, 4 spots 67.7%), while bilateral photoinhibition degrades it severely (1 spot per\n    side 58.0%) or to near chance (4 spots per side 51.4%).\n  source: Results, Preparatory activity after bilateral silencing, paragraph 1; Figure 2b\n  quote: 'Behavioral performance was only slightly affected after unilateral photoinhibition with a\n    single spot during the early delay epoch ( Fig. 2b , 70.3% correct, p = 0.009, two-tailed t-test\n    against control); unilateral photoinhibition with four spots had small additional effect (67.7%,\n    p=0.003). In contrast, using only two spots across both hemispheres caused performance to\n    degrade severely ( Fig. 2b , 58.0%, p<0.001; difference from 4 spot unilateral: p<0.05,\n    two-tailed t-test); four spots bilaterally further reduced performance to near chance level (4\n    laser spots: 51.4%, p<0.001)'\n  statistics:\n  - about: unilateral 1 spot against control\n    test: two-tailed t-test\n    p: 0.009\n  - about: unilateral 4 spots against control\n    test: two-tailed t-test\n    p: 0.003\n  - about: bilateral 1 spot per side against control\n    test: two-tailed t-test\n    p: 0.001\n    p_relation: \"<\"\n  - about: bilateral 1 spot per side against unilateral 4 spots\n    test: two-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n  - about: bilateral 4 spots per side against control\n    test: two-tailed t-test\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: performance, unilateral 1 spot\n    value: 70.3\n    tolerance: 7.03\n    unit: '% correct'\n  - quantity: performance, unilateral 4 spots\n    value: 67.7\n    tolerance: 6.77\n    unit: '% correct'\n  - quantity: performance, bilateral 1 spot per side\n    value: 58.0\n    tolerance: 5.8\n    unit: '% correct'\n  - quantity: performance, bilateral 4 spots per side\n    value: 51.4\n    tolerance: 5.14\n    unit: '% correct'\n  criterion: Performance (M1) per condition over mice, tests of M7. The paper's numbers come from\n    13 mice including behaviour-only sessions and photoinhibition of 0.8 s and 1.3 s; the data set's\n    recording sessions hold 0.8 s photoinhibition from delay onset. Reproduced when each value is\n    within tolerance, each condition is below control with p < 0.05, and bilateral 1 spot is below\n    unilateral 4 spots; partially reproduced when the order (control > unilateral > bilateral 1 spot\n    > bilateral 4 spots) holds but some values are outside tolerance.\n- id: ed6-bilateral-bias-inconsistent\n  statement: Bilateral photoinhibition biases movements inconsistently across mice and sessions,\n    and the direction of a session's bias follows which control trajectory its perturbed cd\n    trajectories approach.\n  source: Results, Preparatory activity after bilateral silencing, paragraph 1; Extended Data Fig. 6\n  quote: Bilateral photoinhibition biased movements inconsistently across mice and sessions\n  depends_on:\n  - fig3-cd-roc\n  criterion: Experiment 2 sessions of M6, bilateral photoinhibition. Per session, bias = performance\n    on lick right trials minus performance on lick left trials under photoinhibition, and the mean\n    perturbed cd projection in the last 400 ms of the delay relative to the decision boundary. The\n    paper gives no test; as a standard choice, a session is biased when the two performances differ\n    by Fisher's exact test at p < 0.05. Reproduced when biased sessions of both signs occur and\n    the sign of the bias agrees with the side of the decision boundary in at least 80% of biased\n    sessions (the paper's five example sessions all agree; the 80% is a choice stated here).\n- id: fig2-bilateral-recovery\n  statement: Spike rate and selectivity of left ALM neurons recover within 600 ms after ipsilateral\n    photoinhibition, contralateral photoinhibition hardly affects activity, and after bilateral\n    photoinhibition the rate recovers on average but selectivity does not; selectivity recovery takes\n    538 +- 178 ms (ipsilateral), 192 +- 114 ms (contralateral) and does not occur (bilateral).\n  source: Results, Preparatory activity after bilateral silencing, paragraph 2; Figure 2c-e\n  quote: As before ( Fig. 1 ), spike rate (> 90 %) ( Fig. 2c, d ) and selectivity (> 80%) ( Fig. 2e\n    ) recovered 600 ms after ipsilateral perturbation. ALM activity was hardly affected by\n    contralateral photoinhibition ... After bilateral photoinhibition neurons recovered their spike\n    rate on average ( Fig. 2c, d ), but selectivity failed to recover\n  depends_on:\n  - units-and-sessions\n  expected:\n  - quantity: selectivity recovery time, ipsilateral\n    value: 538\n    tolerance: 178\n    unit: ms\n  - quantity: selectivity recovery time, contralateral\n    value: 192\n    tolerance: 114\n    unit: ms\n  - quantity: selective neurons in Fig. 2e\n    value: 143\n    tolerance: 14.3\n  criterion: Experiment 2 (1 spot ipsilateral, 1 spot contralateral, 4 spots per side bilateral),\n    M4 and M5. \"Spike rate (> 90 %)\" is read as (a) more than 90% of neurons without a significant\n    rate change (M5) in the window 600 ms after offset, or (b) population mean rate within 10% of\n    control there. Reproduced when, under one reading of each open detail, the ipsilateral rate and\n    selectivity recover as stated with the recovery times within tolerance, the contralateral\n    recovery time is within tolerance, and the bilateral selectivity stays below 80% of control up\n    to the go cue while the bilateral mean rate is back within 10% of control by the cue. Partially\n    reproduced when the ordering holds (ipsilateral recovers, bilateral does not) but a time is\n    outside tolerance.\n- id: ed7-unilateral-4-spots-bilateral-1-spot\n  statement: Bilateral photoinhibition with one spot per side causes a larger persistent change in\n    selectivity than unilateral photoinhibition with four spots; recovery takes 490 +- 280 ms\n    (ipsilateral 4 spots), 235 +- 156 ms (contralateral 4 spots) and does not occur (bilateral 1\n    spot).\n  source: Results, Preparatory activity after bilateral silencing, paragraph 2; Extended Data Fig.\n    7d\n  quote: Bilateral photoinhibition with one laser spot produced a larger persistent change in\n    selectivity than unilateral photoinhibiton with four laser spots\n  depends_on:\n  - units-and-sessions\n  expected:\n  - quantity: selectivity recovery time, ipsilateral 4 spots\n    value: 490\n    tolerance: 280\n    unit: ms\n  - quantity: selectivity recovery time, contralateral 4 spots\n    value: 235\n    tolerance: 156\n    unit: ms\n  - quantity: selective neurons\n    value: 40\n    tolerance: 4\n  criterion: Experiment 3 sessions, M4. Reproduced when the recovery times are within tolerance\n    under one reading, bilateral 1-spot selectivity does not reach 80% of control before the go\n    cue, and the mean delta selectivity in the last 400 ms of the delay is larger in magnitude for\n    bilateral 1 spot than for ipsilateral 4 spots.\n- id: ed7e-size-and-roc\n  statement: Recovery of selectivity after unilateral photoinhibition is less robust with larger\n    photoinhibition, and cd trajectories separate at the end of the delay with ROC 0.80 +- 0.08\n    (control), 0.64 +- 0.10 (ipsilateral 4 spots), 0.68 +- 0.15 (contralateral 4 spots) and 0.54\n    (bilateral 1 spot).\n  source: Results, Preparatory activity after bilateral silencing, paragraph 2; Extended Data Fig.\n    7e\n  quote: 'Recovery of selectivity after unilateral photoinhibition was less robust with larger\n    photoinhibition size ( Extended Data Fig. 7e ) ... control, 0.80 ± 0.08; ipsilateral, 0.64 ±\n    0.10; contralateral, 0.68 ± 0.15; bilateral, 0.54 ± 0.8'\n  depends_on:\n  - fig3-cd-roc\n  expected:\n  - quantity: ROC, control\n    value: 0.8\n    tolerance: 0.08\n  - quantity: ROC, ipsilateral 4 spots\n    value: 0.64\n    tolerance: 0.1\n  - quantity: ROC, contralateral 4 spots\n    value: 0.68\n    tolerance: 0.15\n  - quantity: ROC, bilateral 1 spot\n    value: 0.54\n    tolerance: 0.08\n  criterion: Experiment 3 sessions with > 5 simultaneously recorded neurons tested for > 3 trials in\n    each condition (ED Fig. 7e legend), M6 otherwise. The printed s.e.m. of the bilateral value,\n    0.8, cannot be an s.e.m. of an ROC value; 0.08 is taken as its tolerance, and this is a reading.\n    Reproduced when all four ROC values are within tolerance under one reading; \"less robust with\n    larger size\" is judged by the ipsilateral 4-spot ROC being below the Experiment 2 ipsilateral\n    1-spot ROC of fig3-cd-roc.\n- id: fig3-cd-roc\n  statement: Along the coding direction, trajectories for lick right and lick left recover after\n    ipsilateral photoinhibition (ROC at the end of the delay 0.73 +- 0.02 against control 0.76 +-\n    0.03), are little affected by contralateral photoinhibition (0.74 +- 0.03), and stay collapsed\n    after bilateral photoinhibition (0.58 +- 0.03).\n  source: Results, Robustness along the coding direction, paragraph 2; Figure 3b, c; Extended Data\n    Fig. 8\n  quote: 'ROC values between trajectories at the end of delay epoch: control, 0.76 ± 0.03;\n    ipsilateral, 0.73 ± 0.02; mean ± s.e.m. across sessions, Methods). Contralateral photoinhibition\n    had little effect ( Extended Data Fig. 8 ; ROC, 0.74 ± 0.03). As expected ( Fig. 2 ),\n    trajectories were permanently altered after bilateral photoinhibition, resulting in small\n    separation between the trajectories for different trial types at the time of movement onset\n    (ROC, 0.58 ± 0.03)'\n  depends_on:\n  - units-and-sessions\n  expected:\n  - quantity: sessions with > 5 simultaneous neurons and > 5 trials per condition\n    value: 16\n    tolerance: 0\n  - quantity: ROC, control\n    value: 0.76\n    tolerance: 0.03\n  - quantity: ROC, ipsilateral\n    value: 0.73\n    tolerance: 0.02\n  - quantity: ROC, contralateral\n    value: 0.74\n    tolerance: 0.03\n  - quantity: ROC, bilateral\n    value: 0.58\n    tolerance: 0.03\n  criterion: M6 with all readings. Reproduced when the 16 sessions are found and all four ROC values\n    are within tolerance under one reading; partially reproduced when the ordering holds (control,\n    ipsilateral and contralateral each above bilateral by more than 0.1) but a value is outside\n    tolerance.\n- id: ed8-roc-during-photoinhibition\n  statement: During photoinhibition the cd separation falls (ROC 0.54 +- 0.03 ipsilateral, 0.64 +-\n    0.03 contralateral, 0.54 +- 0.01 bilateral, against control 0.72 +- 0.02).\n  source: Extended Data Fig. 8 legend\n  quote: 'ROC values during the time period of photoinhibition: control, 0.72 ± 0.02; ipsilateral,\n    0.54 ± 0.03; contralateral, 0.64 ± 0.03; bilateral 0.54 ± 0.01'\n  depends_on:\n  - fig3-cd-roc\n  expected:\n  - quantity: ROC during photoinhibition, control\n    value: 0.72\n    tolerance: 0.02\n  - quantity: ROC during photoinhibition, ipsilateral\n    value: 0.54\n    tolerance: 0.03\n  - quantity: ROC during photoinhibition, contralateral\n    value: 0.64\n    tolerance: 0.03\n  - quantity: ROC during photoinhibition, bilateral\n    value: 0.54\n    tolerance: 0.01\n  criterion: M6; the window \"during photoinhibition\" is open, readings (a) the 400 ms window ending\n    at the start of the offset ramp, (b) projections averaged over the whole 0.8 s photoinhibition.\n    Reproduced when all four are within tolerance under one reading.\n- id: ed9b-cd-stability\n  statement: The direction of the lick right minus lick left response difference is stable through\n    the sample and delay epochs (correlation between late sample and late delay 0.61 +- 0.05).\n  source: Methods, Analysis of population dynamics in the activity space; Extended Data Fig. 9b\n  quote: During the sample and delay epochs the direction of the difference in the mean response\n    vectors, w t = x̄ lick right – x̄ lick left , was stable (correlation of w t 's between late\n    sample epoch vs. late delay epoch, 0.61 ± 0.05\n  depends_on:\n  - fig3-cd-roc\n  expected:\n    quantity: correlation of w, late sample against late delay\n    value: 0.61\n    tolerance: 0.05\n  criterion: M6 sessions. Per session, Pearson correlation of w in the last 400 ms of the sample\n    epoch and in the last 400 ms of the delay epoch (the \"late\" windows are read as these; a\n    reading), on correct control trials; mean +- s.e.m. over sessions. Reproduced when the mean is\n    within tolerance.\n- id: ed8a-mode-variance\n  statement: The projection on cd captures 65.6 +- 5.1% of population selectivity and 36.4 +- 6.3% of\n    task-related activity variance over the sample and delay epochs; modes 1 to 5 together explain\n    98.5 +- 0.5% of the variance and 95.8 +- 1.2% of the selectivity.\n  source: Methods, Analysis of population dynamics in the activity space; Extended Data Fig. 8a\n  quote: The projection along the cd captured 65.6±5.1% of the population selectivity ... and\n    36.4±6.3% of the total variance in ALM task-related activity ... Mode 1-5 together explained\n    98.5±0.5% of the total variance of task-related activity and 95.8±1.2% of population selectivity\n    over the sample and delay epochs\n  depends_on:\n  - fig3-cd-roc\n  expected:\n  - quantity: selectivity captured by cd\n    value: 65.6\n    tolerance: 5.1\n    unit: '%'\n  - quantity: variance captured by cd\n    value: 36.4\n    tolerance: 6.3\n    unit: '%'\n  - quantity: variance captured by modes 1-5\n    value: 98.5\n    tolerance: 0.5\n    unit: '%'\n  - quantity: selectivity captured by modes 1-5\n    value: 95.8\n    tolerance: 1.2\n    unit: '%'\n  criterion: M6 sessions; modes as in the Methods (mode 2, perturbed minus unperturbed lick right\n    mean response at the go cue; mode 3, the same for lick left, Gram-Schmidt orthogonal to mode 2;\n    modes 4 and 5, the first two singular vectors of the baseline-subtracted lick right and lick left\n    PSTHs concatenated, Gram-Schmidt orthogonal to modes 1 to 3), from correct control and\n    ipsilateral trials. Selectivity is the RMS over time of the lick right minus lick left rate\n    difference, variance the RMS of baseline-subtracted activity, over sample and delay. Open\n    details. The baseline; readings (a) the mean rate before sample onset, (b) the mean rate over the\n    whole trial. How a mode's share is computed; readings (a) the RMS of the projection over the\n    RMS of the full activity, (b) the ratio of squared norms. \"At the go cue\" read as the last 400\n    ms of the delay. Reproduced when all four values are within tolerance under one reading;\n    partially reproduced when the two cd values are.\n- id: fig3-cd-predicts-movement\n  statement: Deviations along the coding direction predict the upcoming movement trial by trial, in\n    control trials and after unilateral and bilateral perturbation, even when average selectivity\n    is destroyed.\n  source: Results, Robustness along the coding direction, paragraphs 2 and 4; Figure 3c; Figure 4b;\n    Extended Data Fig. 8b, 9e\n  quote: Individual trials with a deviation toward the “lick right” trajectory along the cd\n    predicted more frequent “lick right” responses and vice versa ( Fig. 4 , Extended Data Figs 6b\n    and 9 ). This analysis shows that even after average selectivity is destroyed by perturbations,\n    ALM population dynamics still dictate upcoming movements\n  depends_on:\n  - fig3-cd-roc\n  criterion: M6, trials pooled over sessions (Methods). For each condition (control, ipsilateral,\n    contralateral, bilateral), the fraction of trials whose lick matches the side of the decision\n    boundary, and performance on lick right and lick left trials binned by distance from the\n    boundary (bin 4 on the cd distance scale, ED Fig. 9e, read in the units of cd^T x after the\n    session offset; scaling of cd is open, readings (a) cd as the raw mean difference, (b) cd of\n    unit length). The paper gives no test; as a standard choice, the fraction of lick right\n    responses rises with distance toward the lick right side by logistic regression of the lick\n    on the signed distance, p < 0.05, and the prediction accuracy exceeds 0.5 by a binomial test,\n    p < 0.05. Reproduced when both hold in control and bilateral trials; partially reproduced when\n    they hold in control only.\n- id: fig3-other-modes\n  statement: The persistent mode is altered by perturbation up to and beyond movement onset but\n    neither discriminates trial type nor predicts behaviour; the ramping mode shows non-selective\n    ramping in the delay, is resistant to unilateral and bilateral perturbation and does not predict\n    behaviour.\n  source: Results, Robustness along the coding direction, paragraph 3; Figure 3d, e; Extended Data\n    Fig. 8b-e\n  quote: However, this projection did not discriminate trial type nor predict behavior on control\n    trials. Third, a mode that maximally captured the remaining activity variance, showed\n    non-selective ramping during the delay epoch, did not predict behavior, and was resistant to\n    unilateral and bilateral perturbations\n  depends_on:\n  - ed8a-mode-variance\n  criterion: Modes 2 and 4 of ed8a-mode-variance (persistent and ramping), decision boundaries as\n    for cd (Methods). The paper gives no test; standard choices stated here. Not discriminating or\n    predicting is judged by an ROC of lick right against lick left projections in the last 400 ms of\n    the delay within 0.5 +- 0.1 averaged over sessions and a prediction accuracy on control trials\n    whose binomial test against 0.5 has p > 0.05. Robustness of the ramping mode is judged by the\n    perturbed projection in the last 400 ms of the delay lying within the s.e.m. band over sessions\n    of the control projection for ipsilateral and bilateral trials, while the persistent-mode\n    projection lies outside it for ipsilateral trials. Reproduced when all hold.\n- id: ed9f-reaction-time\n  statement: Reaction times are faster on trials whose cd trajectory lies far from the decision\n    boundary at the go cue.\n  source: Extended Data Fig. 9f\n  quote: Reaction times are faster on trials in which the trajectory is far from the decision\n    boundary at the time of the ‘go’ cue\n  depends_on:\n  - fig3-cd-roc\n  criterion: M6, 16 sessions; reaction time relative to the session mean, lick right and lick left\n    trials pooled (ED Fig. 9f). The reaction time is not defined in the paper; read as the time from\n    go cue onset to the first lick. Which trials are used is open; readings (a) control trials, (b)\n    all conditions. The paper gives no test; as a standard choice, Spearman correlation of relative\n    reaction time with absolute distance from the boundary, negative with p < 0.05.\n- id: fig5b-callosotomy-behaviour\n  statement: Corpus callosum bisection leaves performance unaffected, but makes performance highly\n    sensitive to unilateral photoinhibition, with a significant interaction, dropping to the level\n    of bilateral photoinhibition in control mice.\n  source: Results, Contralateral input is required for recovery, paragraph 1; Figure 5b; Extended\n    Data Fig. 10b\n  quote: Remarkably, behavioral performance was unaffected ( Fig. 5b , control trials, before vs.\n    after callosotomy, p>0.05, two-tailed t-test) ... However, behavioral performance was now highly\n    sensitive to transient unilateral photoinhibition ( Fig 2b , 1 laser spot. p=0.0019, two-tailed\n    t-test against control). There was a significant interaction between callosotomy and unilateral\n    photoinhibition (p=0.0035, repeated measure two-way ANOVA)\n  statistics:\n  - about: control performance before against after callosotomy\n    test: two-tailed t-test\n    p: 0.05\n    p_relation: \">\"\n    n: 7 mice\n  - about: unilateral 1 spot against control after callosotomy\n    test: two-tailed t-test\n    p: 0.0019\n    n: 7 mice\n  - about: interaction of callosotomy and unilateral photoinhibition\n    test: repeated measure two-way ANOVA\n    p: 0.0035\n    n: 7 mice\n  criterion: Performance (M1) per mouse; tests of M7 and a repeated-measures two-way ANOVA on\n    performance with factors callosotomy (before, after) and photoinhibition (control, unilateral 1\n    spot). Reproduced when control performance after callosotomy does not differ from before\n    (p > 0.05), unilateral photoinhibition lowers it with p < 0.01, and the interaction has\n    p < 0.05; the after-callosotomy unilateral performance is compared with 58.0% (bilateral 1 spot\n    in control mice, fig2b-bilateral-behaviour). If the data set holds no sessions before the cut,\n    the before-and-after comparison and the interaction cannot be tested and the claim is judged on\n    the after-cut test alone, as partially testable.\n- id: fig5-callosotomy-recovery\n  statement: After callosotomy, ALM neurons recover their average spike rate after ipsilateral\n    photoinhibition but not their selectivity, selectivity recovers after contralateral\n    photoinhibition (217 +- 228 ms) and not after bilateral, and selectivity along cd is reduced.\n  source: Results, Contralateral input is required for recovery, paragraph 2; Figure 5c-f\n  quote: After ipsilateral photoinhibition, ALM neurons recovered their average spike rate ( Fig.\n    5c, d ), but selectivity failed to recover ( Fig. 5e ). Selectivity in the cd direction was\n    reduced ( Fig. 5f , 16 sessions)\n  expected:\n  - quantity: selectivity recovery time, contralateral, callosotomy\n    value: 217\n    tolerance: 228\n    unit: ms\n  - quantity: selective neurons in Fig. 5e\n    value: 129\n    tolerance: 12.9\n  - quantity: callosotomy sessions in Fig. 5f\n    value: 16\n    tolerance: 0\n  criterion: Callosotomy sessions (conditions ipsilateral 1 spot, contralateral 1 spot, bilateral\n    4 spots), M4, M5 and M6 (the session rule of M6 applied to these sessions). Reproduced when the\n    ipsilateral mean rate returns within 10% of control before the go cue while selectivity stays\n    below 80% of control up to the cue, the contralateral recovery time is within tolerance, the\n    bilateral selectivity does not recover, and the ipsilateral cd ROC at the end of the delay is\n    lower than the callosotomy control ROC and lower than the Experiment 2 ipsilateral ROC of\n    fig3-cd-roc.\n- id: ed10e-callosotomy-preparatory-activity\n  statement: Preparatory activity after callosotomy is similar to that of control mice, with 254 of\n    496 putative pyramidal neurons selective.\n  source: Results, Contralateral input is required for recovery, paragraph 2; Extended Data Fig.\n    10e, f\n  quote: Preparatory activity in callosotomized mice (n=7 mice) was similar to control mice ( Fig.\n    5c ; Extended Data Fig. 10 ), providing additional evidence that the two ALM hemispheres can\n    maintain preparatory activity independently\n  depends_on:\n  - ed1-selective-fraction\n  expected:\n  - quantity: selective pyramidal neurons, callosotomy\n    value: 254\n    tolerance: 25.4\n  - quantity: putative pyramidal neurons, callosotomy\n    value: 496\n    tolerance: 0\n  criterion: Selectivity test of M3 on callosotomy control trials. \"Similar\" is read as the selective\n    fraction within 10 percentage points of the control mice's 634/890 under the same reading (a\n    choice stated here), and the population selectivity (M4) during the delay epoch present and\n    rising toward the go cue as in ED Fig. 1c. Reproduced when the counts are within tolerance and\n    the fraction is similar.\n- id: models-monolithic-fail\n  statement: Monolithic network models (fixed-point attractor, integrators, trained recurrent\n    networks) do not recover their unperturbed trajectory after transient silencing of half of\n    their neurons.\n  source: Results, Robust model networks, paragraph 1; Figure 1c; Extended Data Fig. 1f-i, 4c\n  quote: Overall, all “monolithic” models consisting of one network were unable to explain\n    robustness\n  data: with_inputs\n  criterion: A simulation, using no recorded data beyond what the data set may hold as simulation\n    code; parameters from the Methods and ED Fig. 1 legend (simple integrator N = 100, tau 100 ms,\n    one eigenvalue 0.99; corrective-feedback integrator with the synaptic time constants given;\n    FORCE network N = 400, tau 200 ms, g 1.5, p 0.1, 30 iterations; tamed chaos, 20 iterations).\n    Silencing holds half the neurons at zero for 0.2 s < t < 1.0 s. Open details, each a standard\n    choice that should not change the outcome, Euler step 1 ms and random seeds; the connectivity of\n    the simple integrator beyond its spectrum, the weight-pruning threshold of the tamed chaos\n    network and the FORCE learning rate are open and could matter, so three random draws are run.\n    Reproduced when, in each model, the output at t = 2 s after perturbation differs from the\n    unperturbed output by more than 20% of the unperturbed selectivity (a threshold chosen here)\n    in at least two of three draws.\n- id: fig6-modular-models-robust\n  statement: Modular networks of two coupled modules (attractor, integrator, trained recurrent\n    network) restore activity after transient silencing of one module but drift to a random fixed\n    point when both are silenced.\n  source: Results, Robust model networks, paragraph 2; Figure 6b-d; Methods, Modeling and simulation\n  quote: Selective commissural connections restored activity on the other side after unilateral\n    transient silencing ( Fig. 6b ). When the two sides are silenced, the network drifts to one of\n    the fixed points randomly\n  data: with_inputs\n  criterion: A simulation with the parameters of the Methods (modular attractor, self weight 0.5235,\n    mutual -0.5235, inter-module 0.3, tau 100 ms, the given g(x), input 0.1, tonic 0.5, noise\n    variance 0.01; modular integrator with the printed 8 x 8 matrix, tau 10 ms, inputs +-0.04, tonic\n    40; modular FORCE network). Integration step 1 ms (a standard choice; for the noise, variance per\n    step as printed, and per unit time as a second reading). Unilateral silencing holds one module\n    at zero for 0.2 s < t < 1.0 s; bilateral silencing holds both. Reproduced when, for the\n    attractor and integrator, the silenced module returns within 10% of its unperturbed state by\n    t = 2 s in at least 90% of 100 noisy runs, and after bilateral silencing the attractor ends at\n    the wrong fixed point in between 25% and 75% of runs (thresholds chosen here; \"randomly\" read as\n    near one half). The FORCE network is reported, as its training is not fully specified.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-alm-3/10.1038-nature17643.yaml; python - <<'EOF'
p='claims/crcns-alm-3/10.1038-nature17643.yaml'
s=open(p).read()
old="""  quote: Remarkably, behavioral performance was unaffected ( Fig. 5b , control trials, before vs.
    after callosotomy, p>0.05, two-tailed t-test) ... However, behavioral performance was now highly
    sensitive to transient unilateral photoinhibition ( Fig 2b , 1 laser spot. p=0.0019, two-tailed
    t-test against control). There was a significant interaction between callosotomy and unilateral
    photoinhibition (p=0.0035, repeated measure two-way ANOVA)"""
new="""  quote: 'Remarkably, behavioral performance was unaffected ( Fig. 5b , control trials, before vs.
    after callosotomy, p>0.05, two-tailed t-test) ... However, behavioral performance was now highly
    sensitive to transient unilateral photoinhibition ( Fig 2b , 1 laser spot: p=0.0019, two-tailed
    t-test against control). There was a significant interaction between callosotomy and unilateral
    photoinhibition (p=0.0035, repeated measure two-way ANOVA)'"""
assert old in s; s=s.replace(old,new)
assert s.count("  data: with_inputs\n")==2
s=s.replace("  data: with_inputs\n","")
s=s.replace("A simulation, using no recorded data beyond what the data set may hold as simulation\n    code; parameters","A simulation that uses no recorded data (the data set's title says it holds simulations\n    as well); parameters")
open(p,'w').write(s)
EOF
python tools/claims_check.py $f paper/10.1038-nature17643.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-alm-3/10.1038-nature17643.yaml; grep -n "—\|rather" $f; python -c "
import yaml;d=yaml.safe_load(open('$f'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

```
29 29 11 5 29 18
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
?? claims/crcns-alm-3/
?? scripts
```

**Agent**

I wrote the claims file `claims/crcns-alm-3/10.1038-nature17643.yaml`. The quote checker passes: 29 claims, 29 quotes, 0 problems.

**Text read.** I read the accepted author manuscript from PubMed Central (PMC5081260), as supplied in `paper/`. It has the main text, the Methods, and the legends of Figures 1–6 and Extended Data Figures 1–10. The paper has no separate supplement. No PDF of the paper was supplied, so numbers that appear only inside figures were not read: the per-condition performance in Fig. 1d and 5b, and the bar values in ED Fig. 8a and 8b. I did not read the version of record or the listed corrigendum (doi:10.1038/nature18623), because neither was supplied. The paper links no code. The data set's description says it includes MATLAB scripts that reproduce the figures; those are data set files, so I did not open them.

**Counts.**
- **Claims:** 29, and all 29 have quotes. None needed an `inferred` note.
- **Criteria:** all 29 have one.
- **Expected values:** 18 claims have them.
- **Statistics:** 5 claims carry 11 test entries. These are Fig. 1d, the early-delay absence claim, Fig. 2b (5 tests), ED Fig. 4c (paired t-test), and the callosotomy behaviour (t-tests and the repeated-measures ANOVA). I left out the p < 0.05 and p < 0.01 thresholds the paper uses to count selective neurons or neurons with a changed rate.

**Details the paper leaves open, with the readings named:**
- **Lick-early trials in the electrophysiology analyses:** excluded, or included.
- **Response epoch length:** the first 400 ms after the go cue, or the 1.5 s answer window.
- **Trials for the selectivity test:** correct trials only, or all trials grouped by instructed movement.
- **Excluding neurons under 1 spike/s in Fig. 1f, 2d and 5d:** with, or without.
- **Preferred trial type:**
  - 10 trials of each type, or 10 trials in total.
  - The window that sets the preference: the whole trial, or the most selective epoch.
- **Selectivity time bins:** 200 ms or 400 ms windows. The 50 ms step is a standard choice.
- **Time stamp of a window:** its centre, or its end.
- **Window meant by "within 400 ms after" offset (Fig. 1f):** the window starting at offset, or the one centred 400 ms after it.
- **"Spike rate (> 90 %)" in Fig. 2:** more than 90% of neurons unchanged, or the mean rate within 10% of control.
- **Population analyses:**
  - Units: pyramidal only, or all units.
  - Which windows build cd: centre inside the sample and delay epochs, or wholly inside them.
  - How control trials are split: random halves, or leave-one-out.
  - Scaling of cd: raw, or unit length.
- **Mode decomposition:** the baseline (pre-sample, or whole trial) and how a mode's share is computed (RMS ratio, or squared-norm ratio).
- **The "during photoinhibition" ROC window:** the 400 ms before the ramp, or the whole 0.8 s.
- **Behavioural t-tests:** paired or unpaired. A mouse's performance as pooled trials, or the mean over sessions.
- **ED Fig. 4c:** which photoinhibition conditions are pooled.
- **Reaction time:** not defined; I read it as go cue to first lick.
- **Model simulations:** integration step, noise scaling and random seeds.

Where the paper gives no test at all (ED Fig. 6, ED Fig. 9f, the claims that the persistent and ramping modes do not predict, prediction along cd), I named a standard test as a choice and said so.

**Inconsistencies noted:**
- The paper uses two names for the third Experiment 1 window: "late delay" in the Methods and Fig. 1g, "middle delay" in the Results. The file identifies that window by its end time instead.
- The ED Fig. 7e bilateral ROC is printed as 0.54 ± 0.8. I took 0.08 as its tolerance and marked that as a reading.

**Data the claims need that the data set may not hold:** the data set's documentation says it does not contain the behaviour-only sessions or the photoactivation data. That affects:
- Fig. 1d at the go cue.
- ED Fig. 3.
- Most of the 13 mice behind Fig. 2b.
- ED Fig. 5.
- The untrained-mouse mapping in ED Fig. 2d.
- Possibly the pre-callosotomy sessions needed for the Fig. 5b interaction.

The two model claims are simulations built from the parameters in the Methods. The FORCE training is not fully specified, so those networks are to be reported but are not part of the pass/fail test.

## End of run

19 turns, 5 minutes, $1.86 at API prices, result: success.
