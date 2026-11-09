# 000013 · claims · run 39598579216

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/000013 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; wc -c paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 25,200p claims/001453/*.yaml; ls claims | head; ls claims/001535
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
[... 167 more lines not kept]
```

**Agent calls Bash**

```bash
head -40 claims/001535/*.yaml; grep -n "^[a-z_]*:" claims/001535/*.yaml claims/001453/*.yaml; grep -n "^  [a-z_]*:" claims/001535/*.yaml | awk -F: '{print $3}' | sort | uniq -c
```

```
# Claims for Natraj, Seko, Abiri, Miao, Yan, Graham, Tu-Chan, Chang & Ganguly (2025), Cell 188,
# 1208-1225, on dandiset 001535.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
# pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read: the accepted author manuscript in PubMed Central (PMC11932800, NIHMS2059472), full
# text as served by ncbi_pmc (paper/10.1016-j.cell.2025.02.001.txt): Results, Discussion, STAR
# Methods, the main figure legends and the supplementary legends (Figures S1 to S9, Videos S1 to
# S4, Supplementary Method S1). It is not the version of record. The supplement is present only as
# its legends; Supplementary Method S1 (a timeline schematic) and the supplementary figures
# themselves were not read, and no PDF was supplied. No claim needs a value that appears only in a
# figure image.
#
# Code read: the paper links "exemplar real-time BCI and neural signal processing code and
# decoders" at OSF (doi:10.17605/OSF.IO/TBDWG), one file BCI/bci.zip (17742715 bytes, modified
# 2025-02-26, sha256 575149d40829d135557d17cd5247c85a0d333033467f8c25df281bef8ddb091a). It holds the
# MATLAB real-time task modules (Robot3DArrow, RealRobotBatch, RobotR2GModeSwitch and others), the
# feature pipeline (neuro/), Kalman filter code, the PyBullet robot simulator, trained decoders
# (clicker/*.mat) and scripts that fine-tune the biLSTM (task_helpers/ToTrainDiscreteModel_7DoF_LSTM.m,
# get_lstm_features.m, extract_lstm_features.m) and run the mode filter (runningMode.m). It holds no
[... 223 more lines not kept]
```

**Agent**

I've read the protocol and the format. Now reading the paper.

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.06619.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/*.txt | tr '\n' ' ' | cut -c53700-100000
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/cd641e44-eba2-450b-8ac4-49c773eee3d4/tool-results/bmq5jqomv.txt"
}
```

```
1	ccount the latency of each cell). Each neuron was characterized by a curve, y t o n ( t i ) , representing the total number of spikes that occurred within a given time window ( t i w i t h i = 0 , 1 … e t c ) . In cells where most spikes occurred shortly after touch onset these curves rise steeply and then plateau. For each neuron we determined the touch response cutoff, the first time point t i = t o n in which the rate of increase Δ y t o n ( t i ) = y t o n ( t i ) − y t o n ( t i − 1 ) is below chance level of the overall firing rate (p < 0.05; bootstrap method). The chance level was estimated by shuffling the spike times (1000 repetitions) to create surrogate curves y t o n k ( t i ) . The derivative was calculated from these curves smoothed with a polynomial fit (degree 11). For each t i we estimated the 95% percentile of the slope of the surrogate curves. For whisking phase, each spike that was not attributed to touch onset was indexed by the time elapsed between the spike and the closest whisk cycle preferred phase (taking into account phase circularity and including whisking epochs with non-monotonic phase). As with touch, we built y w h i s k ( t i ) representing the number of spikes that occurred around the preferred whisking phase. We determined the whisking spike cutoff, the first time point t i = t w in which the rate of increase of explained spikes by whisking was below chance levels. Population decoding To decode touch based on spikes for each neuron ‘ i’ ( Figure 4 ) we extracted the spiking response r i , j ( t ) of all touch events ‘ j’ from t = 30 ms before touch up to t = 50 ms after touch (with j = 1 … N t o u c h ( i ) ; excluding events with a second touch in the 50 ms post-touch window). We randomly selected a set of neurons (up to N = 200) and for each neuron we randomly sampled (with replacement) 1000 of its touch aligned responses r i , j ( t ) . Each spike train was causally integrated with a defined window (i.e., w = 10 ms). At each t
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/*.txt | tr '\n' ' ' | cut -c100000-145000
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/cd641e44-eba2-450b-8ac4-49c773eee3d4/tool-results/b4u01m9jk.txt"
}
```

```
1	ature. If we now turn to the recent literature on somatosensory cortex, we see that it makes precisely the opposite case relative to neurons being “ noisy ” . Indeed, the paper might just as well have begun with “ Cortical spike trains are often considered to be made up of precisely timed spikes, whereby the timing of each spike carries some meaning about the stimulus. ” See for example Arabzadeh, Zorzin and Diamond “ Neuronal encoding of texture in the whisker sensory pathway ” (PLoS Biol 2005) and “ Deciphering the spike train of a sensory neuron: counts and temporal patterns in the rat whisker pathway ” (J Neurosci 2006). Additional contributions that should be considered in rethinking how to cast these results include those from G. Stanley (admittedly anesthetized, as noted in this study), E. Arabzadeh, G. Foffani, R. Petersen, and S. Panzeri. The latter include “ Information carried by population spike times in the whisker sensory cortex can be decoded without knowledge of stimulus time ” (Frontiers, 2010) – which is related to the authors' conclusion that “ Pooling activity from only fifteen L4 neurons […] in C2 was sufficient to detect 95 % of touches “ – and ” Complementary Contributions of Spike Timing and Spike Rate to Perceptual Decisions in Rat S1 and S2 Cortex “ (Current Biology, 2015). The latter is admittedly too recent to have shaped the present paper, but it is now in the literature . It’s been known since the classic studies of Dan Simons (cited) that after passive whisker deflection L4 neurons spike with short latencies and little timing jitter. We cite this and other papers in our Introduction. We show similar temporal precision in L4 neurons during active sensation. Furthermore we show that spike rates are extremely low except in a narrow time window after touch. This picture is very different compared to the only other L4 recordings during active behavior that we are aware of (Curtis and Kleinfeld, 2009); this study shows high baseline spike 
[... 1 more lines not kept]
```

**Agent**

The full text is complete (main text, Methods, all figure and supplement legends, decision letter). Next: the linked code (github.com/hireslab/HLab_Whiskers) and the dataset's archive description.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/hireslab/HLab_Whiskers 2>&1 | tail -3; cd HLab_Whiskers && git log -1 --format='%H %cd' && ls -R | head -80; curl -s https://api.dandiarchive.org/api/dandisets/000013/ | python -c "import json,sys;d=json.load(sys.stdin);print(d['draft_version']['name'])"; curl -s https://api.dandiarchive.org/api/dandisets/000013/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('description'));print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/HLab_Whiskers && cat README.md | head -40; ls Contacts +Whisker +Solo +Shared Docs WhiskerTrackerCode | head -100; grep -rli "fano\|optics\|bayes\|bandpass\|hilbert" --include=*.m . | head -30
```

```
+Shared:
tapply.m
tapply_min.m

+Solo:
@BTLightDetect
@BTLightDetectArray
@BTStimTiming
@BTStimTimingArray
@BehavSilenceTrial
@BehavSilenceTrialArray
@BehavTrial
@BehavTrial2AFCArray
@BehavTrialArray
@BehavTrialArray_NX
@BehavTrialArray_SKControl
@BehavTrialHLabArray
@BehavTrialStim
@BehavTrialStimArray
@BehavTrial_nx
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/HLab_Whiskers && git log --format='%h %ad %s' --date=short | head -20; git log --format='%h %ad' --date=short | wc -l; grep -n -i "hilbert\|butter\|bandpass\|amplitude\|phase" +Whisker/@WhiskerSignalTrial/WhiskerSignalTrial.m | head -40; grep -n -i "hilbert\|butter\|fano\|phase\|2\.5\|1\.25" +LCA/@Sweep/Sweep.m +LCA/@SiTrialArray/SiTrialArray.m +LCA/@TrialArray/TrialArray.m | head -60
```

```
cdbc914 2020-12-11 increased the speed, also bug fixes
c46a628 2020-12-09 fixed a few bugs added a few shortcuts
5867d2e 2020-12-07 Merge pull request #1 from hireslab/PhillipMaire-TCB-V2
9aa6915 2020-12-07 added renamed icons to avoid conflicts
c2afc01 2020-12-07 added file for the updated trial contact browser
f11ae72 2020-08-12 Create trialContactBrowserBIG_VIEW.m
527123a 2017-08-10 Merge branch 'master' into Phils_branch
89530c4 2017-08-10 changed save to include CellName and CellCode
8877249 2017-08-02 minor changes
65f1c08 2017-08-02 Removed auto close video fig edits
88a9aa1 2017-08-02 ignore asv files
1acd8ad 2017-08-02 finish last commit - save button opens in last saved location
a4c0ac2 2017-08-02 save button opens in last saved location
782afd3 2017-08-02 auto close video fig
ac5ef6f 2016-02-24 Added whisker tracker
9fbbbd5 2016-02-24 Merge https://github.com/hireslab/HLab_Whiskers
7604432 2016-02-24 Added whisker tracker
c162ef6 2015-08-19 updated autoContactAnalyzerSI for manualdel to be saved when updating contacts
0eb360a 2014-11-19 Make trialContactBrowser work with non-1000 fps sessions
8b8b6c4 2014-10-29 Modified BehavTrialArray to work with sp_detect style behaioral sessions
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/HLab_Whiskers && sed -n 420,460p +Whisker/@WhiskerSignalTrial/WhiskerSignalTrial.m; head -60 Contacts/autoContactAnalyzerSi.m; git log --format='%h %ad' --date=short | tail -8; git log -1 --format=%h --before=2015-08-06
```

```
end
            if numel(trajectory_id) > 1
                error('Only one trajectory_id is allowed.')
            end
            whisker_name = obj.whiskerNames(obj.trajectoryIDs==trajectory_id);
        end
        
        function  [pkVal,pkTime,pkBinarySignal] = get_whisk_peaks(obj,tid)
            %
            %   [pkVal,pkTime,pkBinarySignal] = get_whisk_peaks(obj,tid)
            %
            %
            %
            [y,t] = obj.get_position(tid);
            thresh = .01; % Should make argument. ***
            
            bandPassCutOffsInHz = [10 25];
            sampleRate = 500; % Should read from data.***
            W1 = bandPassCutOffsInHz(1) / (sampleRate/2);
            W2 = bandPassCutOffsInHz(2) / (sampleRate/2);
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/HLab_Whiskers && grep -rn -i "hilbert\|fano\|optics" --include=*.m . | head; grep -rn -i "touchThresh\|curvature\|deltaKappa" Contacts/autoContactAnalyzerSi.m | head -15
```

```
./+Solo/@BehavSilenceTrialArray/BehavSilenceTrialArray.m:253:            fanostim=setdiff(fa, fa_stim);
./+Solo/@BehavSilenceTrialArray/BehavSilenceTrialArray.m:258:            pcorrect_nostim=numel((intersect([hitnostim crnostim], performtrials)))/numel(intersect([hitnostim missnostim fanostim crnostim], performtrials))
./+Solo/@BehavSilenceTrialArray/BehavSilenceTrialArray.m:261:            pfar_nostim=numel((intersect(fanostim, performtrials)))/numel(intersect([fanostim crnostim], performtrials))
./+Solo/@BehavSilenceTrialArray/BehavSilenceTrialArray.m:278:                plot(fanostim,3+zeros(size(fanostim)), 'r.', 'MarkerSize',ms); hold on
22:% First use some generous limits for the touchThresh values.  Then, use the
23:% plot output of the Contact Segmenter cell to refine the touchThresh
65:kappa(whiskerTIN)                   = cellfun(@(x)x.whiskerTrial.deltaKappa{1},             array.trials(whiskerTIN),'UniformOutput',0);
171:% Find precontact curvature to adjust force calculations
178:                    mean(array.trials{k}.whiskerTrial.deltaKappa{1}(contacts{k}.segmentInds{1}(i,1)-(1:cLookBack)));
186:disp('Merging contact/curvature-derived moment (M0) and axial force (FaxialAdj) with acceleration based moment (M0I)')
188:M0combo=cell(1,length(array.trials)); % Combined moment calculated from acceleration for non-contact periods and curvature from contact periods.
209:% Generate M0comboAdj FaxialAdj to shift baseline curvature for each contact period
219:            .* (1-contacts{k}.preConCurve{1}(j) ./ array.trials{k}.whiskerTrial.deltaKappa{1}(adjind));
221:            .* (1-contacts{k}.preConCurve{1}(j) ./ array.trials{k}.whiskerTrial.deltaKappa{1}(adjind));
334:    ylabel('Mean Contact Curvature (\kappa)');
353:    text(-.3,.6, ['\fontsize{8}' 'Contact Threshold :\bf ' num2str(params.touchThresh(1)) ' / ' num2str(params.touchThresh(2)) ' / ' num2str(params.touchThresh(3)) ' / ' num2str(params.touchThresh(4))]);
354:    text(-.3,.5, ['\fontsize{8}' '
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; ls docs; grep -n "data:\|kind:" claims/*/*.yaml | awk '{print $2, $3}' | sort | uniq -c
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

[... 82 more lines not kept]
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
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
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

**Agent**

The text is complete, so I'm writing the claims file. The paper's code does not settle any analysis choice. The dataset is described as this paper's L4 recordings during the object-localization task.

**Agent calls Bash**

```bash
cd paper && for s in "fraction of trials correct" "1.54–4.05" "mean bout duration" "mean number of touches" "number of trials per neuron" "0.73 spk/s" "FF = 7.51" "1.51 spikes/first touch" "0.67 spikes/s" "74.4% spikes" "first touch, p = 1.4e-5" "p = 0.68" "p = 0.75" "6.53e-6" "2.88e-4" "4.6 ± 8.7%" "fifteen L4 neurons" "0.55 ms" "24° in C2" "mean modulation index" "4.3e-8" "binomial limit for most" "refractory period alone" "6.57 mean" "1.59 ± 0.49" "0.15 spikes/whisk" "significantly less behavioral" "four L4 outside" "∼0.03" "much higher firing rates"; do grep -o ".\{0,160\}$s.\{0,200\}" *.txt | head -1; echo ---; done
```

```
e We trained mice to locate an object by active touch with a single whisker (C2) ( O'Connor et al., 2010a ; O'Connor et al., 2013 ) ( n = 21 mice, 52 sessions; fraction of trials correct, 0.740 ± 0.086; mean ± s.d.; Figure 1A ; Figure 1—figure supplement 1 ). Single whisker experiments allowed us to track the relevant tactile variables with high precision during behavior. In each tri
---
experiments allowed us to track the relevant tactile variables with high precision during behavior. In each trial, during a sample epoch lasting a few seconds (1.54–4.05, mean 2.39 s), a pole appeared in one of two locations on the right side of the head. High-speed videography and automated whisker tracking quantified whisker movement (azimuthal angle, θ; whisking p
---
al., 2013 ), and contact time, all with 1 millisecond temporal precision ( Clack et al., 2012 ; O'Connor et al., 2013 ) ( Figure 1A,B ). Mice whisked in bouts (mean bout duration, 261 ms; peak-to-peak amplitude, 15.7°; frequency, 15.4 Hz) interspersed with periods of rest. Mice touched the pole multiple times (mean number of touches, 2.33) before reporting perceived object lo
---
 bouts (mean bout duration, 261 ms; peak-to-peak amplitude, 15.7°; frequency, 15.4 Hz) interspersed with periods of rest. Mice touched the pole multiple times (mean number of touches, 2.33) before reporting perceived object location with licking (mean reaction time 367 ± 234 ms; mean ± s.d.) ( Figure 1—figure supplement 1 ). Figure 1. Activity during tactile behavior in a layer 4
---
corresponding to the spared whisker (31 cells in C2; 10 additional outside C2) and L5 near the principal barrel (11 cells), guided by intrinsic signal imaging (number of trials per neuron 115 ± 60; Figure 1—figure supplement 2 ). We recorded single units via loose-seal juxtacellular methods to avoid potential artifacts of intracellular disruption from whole-cell patch or misassigned s
---
pikes from spike sorting ( DeWeese et al., 2003 ). The dynamics of a typi
[... 49 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "content": "# Claims for Hires, Gutnisky, Yu, O'Connor & Svoboda (2015), eLife 4, e06619, \"Low-noise encoding\n# of active touch by layer 4 in the somatosensory cortex\", on dandiset 000013.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, protocol\n# pilot-10 as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record (PMC4525079) as served by Europe PMC\n# (paper/10.7554-elife.06619.txt): Introduction, Results, Discussion, Materials and methods, Table 1,\n# the legends of Figures 1 to 6 and of their figure supplements (Figure 1, supplements 1 and 2;\n# Figure 2, supplement 1; Figure 3, supplements 1 and 2; Figure 4, supplement 1; Figure 6,\n# supplement 1), the decision letter and the author response. eLife has no supplement beyond\n# these figure supplements, whose legends are in the text. No PDF was supplied, so the figure\n# images were not read. Table 1 came through as one run of text; its columns were read in order\n# (9 measures, rows of mean +- s.d., median and range for each of three populations). One cell of\n# it is garbled, the L5 \"Spikes evoked (touch)\" mean printed \"24.0-18.6%\", read as 24.0 +- 18.6%\n# from Results, paragraph on Figure 3C.\n#\n# Code read: the paper links the Janelia Whisker Tracker (openwiki.janelia.org, not code for the\n# analyses) and https://github.com/hireslab/HLab_Whiskers for the detection of contact periods.\n# Read at HEAD, commit cdbc9148da6c505ba940b971fbe419b11cb80049 (2020-12-11); the last commit\n# before publication is 0eb360a (2014-11-19). It holds MATLAB classes for behaviour trials (+Solo),\n# whisker tracking output and curvature (+Whisker), ephys sweeps and trial arrays (+LCA) and the\n# semi-automatic contact detector and curation GUI (Contacts/autoContactAnalyzerSi.m,\n# trialContactBrowser). It holds none of the paper's analyses (no whisking-phase decomposition with\n# a 6 to 60 Hz filter and Hilbert transform, no touch windows, Fano factors, OPTICS clustering or\n# decoders). It therefore settles no criterion below; touch onsets and offsets are taken as given\n# by the contact detection. Its WhiskerSignalTrial.get_whisk_peaks uses a 10 to 25 Hz filter; the\n# paper does not use it, and the Methods' 6 to 60 Hz filter is followed.\n#\n# The dandiset's archive description: data from a study of the precision of cortical spike trains\n# during active tactile behaviour in mice performing whisker-based object localization, with\n# recordings from excitatory neurons of layer 4 of barrel cortex (this paper).\n#\n# The data the paper used, as it reports them:\n#   - 21 mice (7 C57BL/6, 3 VGAT-ChR2(H134R), 8 PV-ires-cre, 3 PV-ires-cre x Ai32), trimmed to the\n#     C2 whisker, performing a go/no-go pole localization task (lick for the posterior pole).\n#   - 52 loose-seal cell-attached (juxtacellular) single-unit recordings, one per session (52\n#     sessions), 10 kHz: 31 L4 cells in C2, 10 L4 cells outside C2 (>200 um from the C2 centre,\n#     in the barrel field), 11 L5 cells near C2 (98 to 324 um from the C2 centre). 115 +- 60 trials\n#     per neuron. Layer is assigned from manipulator depth and pipette shape; barrel from a DiI\n#     track. 7 of the recordings were reported in O'Connor et al. 2013.\n#   - Per trial, whisker video at 1000 fps for 4 to 5 s, tracked for azimuthal angle (theta) and\n#     curvature (kappa, change Delta kappa); contact (touch) periods detected and curated to 1 ms;\n#     pole timing (sample epoch, pole in reach), licks, trial outcome.\n#\n# Definitions used throughout, from the Methods (Whisker analysis; Spike analysis; Spikes\n# accounted by active sensation; Analysis of spike count variance) and legends:\n#   - Touch epochs are periods of contact. For other epochs theta is band-passed 6 to 60 Hz\n#     (fourth-order Butterworth) and Hilbert transformed; whisking epochs have amplitude >2.5 deg;\n#     whisking cycles during licking or within 70 ms after touch are excluded, and phase analyses\n#     use cycles with monotonic phase over a full cycle. Non-whisking periods are contiguous\n#     periods of at least 100 ms with no touch or licking and amplitude <1.25 deg.\n#   - Exploration time is whisking epochs including touch epochs, excluding touches >100 ms.\n#   - The touch spike window of a cell runs from its onset latency to its touch response cutoff\n#     t_on. Latency is where the 1 ms PCTH rises above the pre-touch mean (-50 to 0 ms) by two\n#     standard deviations. t_on is the first window size at which the increase of the cumulative\n#     count of spikes indexed to the closest touch onset falls below the 95th percentile of the\n#     slopes of 1000 spike-time shuffles, the curves smoothed by a degree-11 polynomial.\n#   - Phase tuning is a 12-bin histogram fitted by A[1 + cos(theta - phi_pref)] + B, A, B > 0;\n#     modulation depth A / (A + B).\n#   - The Fano factor (FF) is the variance of the spike count over its mean, across trials or\n#     touches; the binomial limit for a mean count m < 1 is 1 - m.\n# Unless a criterion says otherwise, a population value is the mean (or median) across the cells\n# of that population, each cell contributing one value, as Table 1 is laid out.\n#\n# Tolerances. Where the paper gives mean +- s.d., the tolerance is the s.d., the paper's stated\n# spread (protocol, Reader, step 3); otherwise 10% of the value. Counts of animals, sessions and\n# cells are given tolerance 0, as they are counts the dataset either holds or does not.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000013\"\npaper: doi:10.7554/elife.06619\nclaims:\n- id: recordings-counts\n  statement: The study holds 52 single-unit recordings, 31 L4 cells in the C2 barrel, 10 L4 cells\n    outside C2 and 11 L5 cells near C2, with 115 +- 60 (mean +- s.d.) trials per neuron.\n  source: Results, L4 responses are temporally precise, paragraph 2; Materials and methods,\n    Animals and Electrophysiology\n  quote: We targeted recordings to excitatory neurons in L4 of the principal barrel corresponding\n    to the spared whisker (31 cells in C2; 10 additional outside C2) and L5 near the principal\n    barrel (11 cells), guided by intrinsic signal imaging (number of trials per neuron 115 ± 60\n  expected:\n  - quantity: L4 cells in C2\n    value: 31\n    tolerance: 0\n  - quantity: L4 cells outside C2\n    value: 10\n    tolerance: 0\n  - quantity: L5 cells near C2\n    value: 11\n    tolerance: 0\n  - quantity: trials per neuron, mean over the 52 neurons\n    value: 115\n    tolerance: 60\n    unit: trials\n  criterion: Cells are assigned to the three groups by the paper's rules (Methods,\n    Electrophysiology), L4 or L5 by manipulator depth and pipette shank, inside C2 when the DiI\n    track midpoint is <160 um from the C2 centre and outside when >200 um, or by whatever labels\n    of these groups the dataset carries. The number of trials can be read as (a) all trials\n    recorded or (b) the performing trials analysed (Figure 1, figure supplement 1A says \"performing\n    trials analyzed per session\"); both are shown, and the claim holds under either.\n- id: recordings-mice\n  statement: The 52 recordings come from 21 mice of four lines, 21 neurons from 7 C57BL/6 mice, 6\n    from 3 VGAT-ChR2(H134R) mice, 17 from 8 PV-ires-cre mice and 8 from 3 PV-ires-cre x Ai32 mice.\n  source: Materials and methods, Animals\n  quote: We report recordings from a total of 21 mice. 52 loose-seal cell-attached recordings were\n    made in the following mice ... 21 recorded neurons from 7 C57BL/6 mice, 6 recorded neurons\n    from 3 VGAT-ChR2(H134R) mice\n  expected:\n  - quantity: mice\n    value: 21\n    tolerance: 0\n  - quantity: recordings\n    value: 52\n    tolerance: 0\n  - quantity: neurons from C57BL/6 mice\n    value: 21\n    tolerance: 0\n  - quantity: neurons from PV-ires-cre mice\n    value: 17\n    tolerance: 0\n  criterion: Counted from the subject identifiers and genotypes. Reproduced when the counts of\n    mice and recordings match and, where genotypes are given, the counts per line match (7, 3, 8\n    and 3 mice; 21, 6, 17 and 8 neurons).\n- id: behavior-performance\n  statement: Across the 52 sessions the fraction of trials correct was 0.740 +- 0.086 (mean +-\n    s.d.).\n  source: Results, L4 responses are temporally precise, paragraph 1; Figure 1, figure supplement\n    1B\n  quote: n = 21 mice, 52 sessions; fraction of trials correct, 0.740 ± 0.086; mean ± s.d.\n  expected:\n    quantity: fraction of trials correct, mean over sessions\n    value: 0.740\n    tolerance: 0.086\n  criterion: Per session, correct trials (hits and correct rejections) over trials. The trials can\n    be read as (a) all trials of the session or (b) the performing trials analysed (Figure 1,\n    figure supplement 1A); the paper does not say how performing trials were chosen, so under (b)\n    the dataset's own marking of trials used, if it has one, is taken. Both are shown.\n- id: behavior-sample-epoch\n  statement: The sample epoch, when the pole is presented, lasted 1.54 to 4.05 s, 2.39 s on\n    average.\n  source: Results, L4 responses are temporally precise, paragraph 1\n  quote: during a sample epoch lasting a few seconds (1.54–4.05, mean 2.39 s), a pole appeared in\n    one of two locations on the right side of the head\n  expected:\n  - quantity: mean sample epoch duration\n    value: 2.39\n    tolerance: 0.239\n    unit: s\n  - quantity: shortest sample epoch\n    value: 1.54\n    tolerance: 0.154\n    unit: s\n  - quantity: longest sample epoch\n    value: 4.05\n    tolerance: 0.405\n    unit: s\n  criterion: The sample epoch is the period the pole is in reach (Figure 1C legend, Figure 6E\n    legend). Open detail, the unit of the range and mean, read as (a) over all trials pooled or\n    (b) over per-session means. Both are shown; reproduced when all three values are within\n    tolerance under one reading.\n- id: behavior-whisking-bouts\n  statement: Mice whisked in bouts with a mean duration of 261 ms, a peak-to-peak amplitude of\n    15.7 deg and a frequency of 15.4 Hz, separated by rest.\n  source: Results, L4 responses are temporally precise, paragraph 1; Figure 1, figure supplement\n    1E-G\n  quote: Mice whisked in bouts (mean bout duration, 261 ms; peak-to-peak amplitude, 15.7°;\n    frequency, 15.4 Hz) interspersed with periods of rest\n  expected:\n  - quantity: mean whisking bout duration\n    value: 261\n    tolerance: 26.1\n    unit: ms\n  - quantity: mean peak-to-peak amplitude of bouts\n    value: 15.7\n    tolerance: 1.57\n    unit: deg\n  - quantity: mean whisking frequency\n    value: 15.4\n    tolerance: 1.54\n    unit: Hz\n  criterion: Whisking epochs as defined in the Methods (6 to 60 Hz band-pass, Hilbert amplitude\n    >2.5 deg); a bout is a contiguous whisking epoch. As in Figure 1, figure supplement 1E-G, the\n    amplitude is the maximum amplitude of each bout, the duration that of each bout, and the\n    frequency 1/cycle length of each whisk cycle, pooled across all sessions. Open details, (1)\n    whether \"peak-to-peak\" is twice the Hilbert amplitude or the range of band-passed theta within\n    a cycle, and (2) whether touch periods break a bout. All four combinations are shown;\n    reproduced when all three values are within tolerance under one.\n- id: behavior-touches-reaction\n  statement: Mice touched the pole 2.33 times on average before responding, and the reaction time\n    from first touch to first lick was 367 +- 234 ms (mean +- s.d.).\n  source: Results, L4 responses are temporally precise, paragraph 1; Figure 1, figure supplement\n    1C-D\n  quote: Mice touched the pole multiple times (mean number of touches, 2.33) before reporting\n    perceived object location with licking (mean reaction time 367 ± 234 ms; mean ± s.d.)\n  expected:\n  - quantity: mean number of touches before the response\n    value: 2.33\n    tolerance: 0.233\n  - quantity: mean reaction time\n    value: 367\n    tolerance: 234\n    unit: ms\n  criterion: Reaction time is the time from the first touch onset to the first lick, for every\n    trial with licks (Methods, Whisker analysis), pooled over all sessions (Figure 1, figure\n    supplement 1D). The number of touches is counted before the response time per trial (figure\n    supplement 1C). Open detail, which trials count touches, read as (a) trials with a lick, the\n    count before the first lick, or (b) all trials with at least one touch, counting touches in\n    the sample epoch when there is no lick. Both are shown.\n- id: example-cell-rates\n  statement: The example L4 C2 neuron of Figure 1 fired at 0.73 spikes/s in the 500 ms before the\n    sample epoch and 1.91 spikes/s during it, a 2.6-fold increase (Wilcoxon rank sum, p =\n    3.38e-7).\n  source: Results, L4 responses are temporally precise, paragraph 3; Figure 1C-D\n  quote: The neuron had a low baseline firing (0.73 spk/s; 500 ms before start of sample epoch)\n    that increased substantially during the sample epoch (2.6 fold; to 1.91 spk/s; p = 3.38e-7,\n    Wilcoxon rank sum)\n  statistics:\n  - test: Wilcoxon rank sum\n    p: 3.38e-7\n    n: trials of one neuron\n  expected:\n  - quantity: baseline rate, 500 ms before the sample epoch\n    value: 0.73\n    tolerance: 0.073\n    unit: spikes/s\n  - quantity: rate during the sample epoch\n    value: 1.91\n    tolerance: 0.191\n    unit: spikes/s\n  - quantity: fold increase\n    value: 2.6\n    tolerance: 0.26\n  criterion: The paper does not identify the example cell. It is one of the 31 L4 C2 cells; the\n    values are computed for every L4 C2 cell, and the claim holds when one cell matches all three\n    within tolerance and its per-trial baseline and sample-epoch rates differ by a Wilcoxon rank\n    sum test at p < 0.05 (the trials of the cell are the samples, as the test is named). The cell\n    so found is the example cell for the claims that depend on this one. If no cell matches,\n    example-cell claims are judged on the cell nearest in these values, and that is said.\n- id: example-cell-sample-ff\n  statement: For the example neuron, the Fano factor of spike counts over the whole sample epoch\n    was large, 7.51.\n  source: Results, L4 responses are temporally precise, paragraph 4\n  quote: FF computed by counting spikes over the entire sample epoch (stimulus presentation), was\n    huge (FF = 7.51)\n  depends_on:\n  - example-cell-rates\n  expected:\n    quantity: Fano factor of sample-epoch spike counts, example cell\n    value: 7.51\n    tolerance: 0.751\n  criterion: For the cell identified in example-cell-rates, the variance over its mean of the\n    per-trial spike count in the sample epoch (pole in reach), across trials.\n- id: example-cell-touch-window\n  statement: For the example neuron, 74.4% of spikes fell in a window 8 to 40 ms after touch\n    onset, which covers 15.3% of exploration time.\n  source: Results, L4 responses are temporally precise, paragraph 8; Figure 3A-C\n  quote: For the neuron illustrated in Figure 3A , 74.4% spikes fall into a time window spanning 8\n    to 40 ms after touch onset, comprising 15.3% of overall exploration time\n  depends_on:\n  - example-cell-rates\n  expected:\n  - quantity: fraction of exploration-time spikes in the touch window\n    value: 74.4\n    tolerance: 7.44\n    unit: '%'\n  - quantity: touch window start (onset latency)\n    value: 8\n    tolerance: 0.8\n    unit: ms\n  - quantity: touch window end\n    value: 40\n    tolerance: 4\n    unit: ms\n  - quantity: fraction of exploration time inside touch windows\n    value: 15.3\n    tolerance: 1.53\n    unit: '%'\n  criterion: As fig3c-touch-spikes-l4c2, for the cell identified in example-cell-rates. Since a\n    window end is a whole number of ms, the tolerance on 8 and 40 ms is read as at least 1 ms.\n- id: example-cell-ff-around-touch\n  statement: For the example neuron, the 10 ms sliding-window Fano factor is about 1 before and\n    after touch, where the mean spike count is about 0.03, and falls near the peak of the touch\n    response, where the mean count is about 0.7.\n  source: Figure 6B legend; Results, Low spike count variability, paragraph 5\n  quote: Since the spike rate is very low outside of the touch window, the mean spike count is\n    also very low (∼0.03), implying FF of ∼1 for both the binomial and Poisson models. In\n    contrast, around the peak of the touch response the mean spike count is high (∼0.7)\n  depends_on:\n  - example-cell-rates\n  expected:\n  - quantity: mean 10 ms spike count before touch\n    value: 0.03\n    tolerance: 0.003\n  - quantity: mean 10 ms spike count around the touch-response peak\n    value: 0.7\n    tolerance: 0.07\n  criterion: For the cell identified in example-cell-rates, spike counts in 10 ms windows slid in\n    1 ms steps around touch onset (Figure 6B), across touches with inter-contact interval >250 ms\n    (Methods, Analysis of spike count variance). Reproduced when the mean counts match, the FF\n    before touch is within 0.1 of 1, and the FF at the window of peak mean count is below 1.\n    Open detail, the touches used, read as (a) the >250 ms touches pooled or (b) one of the five\n    clustered groups; both are shown.\n- id: text-spikes-per-touch\n  statement: Each touch evoked on the order of one spike (1.51 spikes per first touch, 0.31 per\n    later touch) with an onset latency of 8 ms.\n  source: Results, L4 responses are temporally precise, paragraph 4; Table 1\n  quote: Each touch evoked on the order of one spike (1.51 spikes/first touch; 0.31/later touches)\n    with short latency (onset, 8 ms)\n  expected:\n  - quantity: spikes per first touch\n    value: 1.51\n    tolerance: 0.151\n  - quantity: spikes per later touch\n    value: 0.31\n    tolerance: 0.031\n  - quantity: onset latency\n    value: 8\n    tolerance: 0.8\n    unit: ms\n  depends_on:\n  - example-cell-rates\n  criterion: The sentence cites Table 1, whose L4 C2 values (mean 1.36 and 0.74, median 0.87 and\n    0.33, median latency 8 ms) do not match 1.51 and 0.31, and it sits in the paragraph on the\n    example cell. Readings, (a) the example cell identified in example-cell-rates; (b) the L4 C2\n    population mean; (c) the L4 C2 population median. Spikes per touch is the mean spike count in\n    the cell's touch spike window (Methods, Spike analysis), first touches of trials apart from\n    later ones. Reproduced when all three values are within tolerance under one reading (latency\n    tolerance at least 1 ms).\n- id: text-whisking-rates\n  statement: Spike rates were low in both whisking (0.67 spikes/s) and non-whisking (0.23\n    spikes/s) periods.\n  source: Results, L4 responses are temporally precise, paragraph 5\n  quote: Firing rates were low in both whisking (0.67 spikes/s) and non-whisking (0.23 spikes/s)\n    periods\n  expected:\n  - quantity: whisking spike rate\n    value: 0.67\n    tolerance: 0.067\n    unit: spikes/s\n  - quantity: non-whisking spike rate\n    value: 0.23\n    tolerance: 0.023\n    unit: spikes/s\n  depends_on:\n  - example-cell-rates\n  criterion: Whisking and non-whisking periods as in the Methods (Whisker analysis). The sentence\n    does not say whose rates these are, and Table 1 (L4 C2 means 1.39 and 1.31, medians 0.33 and\n    0.32) does not give them. Readings, (a) the example cell identified in example-cell-rates;\n    (b) the L4 C2 mean; (c) the L4 C2 median; (d) the rate over all L4 C2 spikes and time pooled.\n    Open detail, whether whisking periods include touch epochs, read both ways. Reproduced when\n    both values are within tolerance under one reading.\n- id: table1-l4-c2\n  statement: For the 31 L4 C2 cells Table 1 gives, as mean +- s.d. (median), spikes per first\n    touch 1.36 +- 1.32 (0.87), per later touch 0.74 +- 0.87 (0.33), touch-evoked spikes 70.6 +-\n    20.9% (74.7%), touch and whisking spikes 75.2 +- 19.0% (80.3%), phase modulation depth 0.67\n    +- 0.32 (0.70), non-whisking rate 1.31 +- 2.88 (0.32) spikes/s, whisking rate 1.39 +- 2.33\n    (0.33) spikes/s, onset latency 7.8 +- 3.0 (8) ms and minimum ISI 2.9 +- 1.9 (2.3) ms.\n  source: Table 1, row L4 Inside C2 (n=31)\n  inferred: Numbers from Table 1, row L4 Inside C2; no sentence states them all.\n  expected:\n  - quantity: spikes per first touch, mean\n    value: 1.36\n    tolerance: 1.32\n  - quantity: spikes per first touch, median\n    value: 0.87\n    tolerance: 0.087\n  - quantity: spikes per later touch, mean\n    value: 0.74\n    tolerance: 0.87\n  - quantity: spikes per later touch, median\n    value: 0.33\n    tolerance: 0.033\n  - quantity: spikes evoked by touch, mean\n    value: 70.6\n    tolerance: 20.9\n    unit: '%'\n  - quantity: spikes evoked by touch, median\n    value: 74.7\n    tolerance: 7.47\n    unit: '%'\n  - quantity: spikes evoked by touch and whisking, mean\n    value: 75.2\n    tolerance: 19.0\n    unit: '%'\n  - quantity: spikes evoked by touch and whisking, median\n    value: 80.3\n    tolerance: 8.03\n    unit: '%'\n  - quantity: phase modulation depth, mean\n    value: 0.67\n    tolerance: 0.32\n  - quantity: phase modulation depth, median\n    value: 0.70\n    tolerance: 0.07\n  - quantity: non-whisking spike rate, mean\n    value: 1.31\n    tolerance: 2.88\n    unit: spikes/s\n  - quantity: non-whisking spike rate, median\n    value: 0.32\n    tolerance: 0.032\n    unit: spikes/s\n  - quantity: whisking spike rate, mean\n    value: 1.39\n    tolerance: 2.33\n    unit: spikes/s\n  - quantity: whisking spike rate, median\n    value: 0.33\n    tolerance: 0.033\n    unit: spikes/s\n  - quantity: onset latency, mean\n    value: 7.8\n    tolerance: 3.0\n    unit: ms\n  - quantity: onset latency, median\n    value: 8\n    tolerance: 1\n    unit: ms\n  - quantity: minimum ISI, mean\n    value: 2.9\n    tolerance: 1.9\n    unit: ms\n  - quantity: minimum ISI, median\n    value: 2.3\n    tolerance: 0.23\n    unit: ms\n  criterion: Each measure per cell as defined in the Methods (see the opening comment), then the\n    mean, s.d. and median over the 31 cells. Spikes per touch, mean count in the touch spike\n    window, first touches of trials and later touches apart. Spikes evoked, as\n    fig3c-touch-spikes-l4c2 and fig3d-touch-phase-l4c2. Modulation depth from the cosine fit to\n    the 12-bin phase histogram of spike rate (Figure 3, figure supplement 1C), fitted by least\n    squares with A, B > 0 (the fitting method is not given; least squares is the standard choice\n    and is not expected to change the outcome). Rates in whisking and non-whisking periods. The\n    minimum ISI is the shortest interspike interval of the cell (Figure 2, figure supplement 1C).\n    Latency tolerance for the median is 1 ms, the bin size. Reproduced when at least 15 of the 18\n    values are within tolerance, partially reproduced for 10 to 14, not reproduced below 10; the\n    medians, which carry the tighter tolerances, are reported apart. Open detail for latency, the\n    PCTH used, read as (a) first touches or (b) all touches (Figure 3, figure supplement 1A shows\n    both); both are shown.\n- id: table1-l4-outside\n  statement: For the 10 L4 cells outside C2 Table 1 gives, as mean +- s.d. (median), spikes per\n    first touch 0.08 +- 0.19 (0), per later touch 0.02 +- 0.04 (0), touch-evoked spikes 9.2 +-\n    13.7% (3.6%), touch and whisking spikes 33.0 +- 30.2% (23.8%), modulation depth 0.58 +- 0.36\n    (0.61), non-whisking rate 2.20 +- 2.91 (1.10) spikes/s, whisking rate 2.41 +- 3.48 (1.31)\n    spikes/s, onset latency 18.5 +- 6.0 (18) ms and minimum ISI 3.3 +- 1.3 (2.8) ms.\n  source: Table 1, row L4 Outside C2 (n=10)\n  inferred: Numbers from Table 1, row L4 Outside C2; no sentence states them all.\n  expected:\n  - quantity: spikes per first touch, mean\n    value: 0.08\n    tolerance: 0.19\n  - quantity: spikes per later touch, mean\n    value: 0.02\n    tolerance: 0.04\n  - quantity: spikes evoked by touch, mean\n    value: 9.2\n    tolerance: 13.7\n    unit: '%'\n  - quantity: spikes evoked by touch, median\n    value: 3.6\n    tolerance: 0.36\n    unit: '%'\n  - quantity: spikes evoked by touch and whisking, mean\n    value: 33.0\n    tolerance: 30.2\n    unit: '%'\n  - quantity: spikes evoked by touch and whisking, median\n    value: 23.8\n    tolerance: 2.38\n    unit: '%'\n  - quantity: phase modulation depth, mean\n    value: 0.58\n    tolerance: 0.36\n  - quantity: phase modulation depth, median\n    value: 0.61\n    tolerance: 0.061\n  - quantity: non-whisking spike rate, mean\n    value: 2.20\n    tolerance: 2.91\n    unit: spikes/s\n  - quantity: non-whisking spike rate, median\n    value: 1.10\n    tolerance: 0.11\n    unit: spikes/s\n  - quantity: whisking spike rate, mean\n    value: 2.41\n    tolerance: 3.48\n    unit: spikes/s\n  - quantity: whisking spike rate, median\n    value: 1.31\n    tolerance: 0.131\n    unit: spikes/s\n  - quantity: onset latency, mean over the cells with a latency\n    value: 18.5\n    tolerance: 6.0\n    unit: ms\n  - quantity: minimum ISI, mean\n    value: 3.3\n    tolerance: 1.3\n    unit: ms\n  - quantity: minimum ISI, median\n    value: 2.8\n    tolerance: 0.28\n    unit: ms\n  criterion: As table1-l4-c2, over the 10 cells. The medians of spikes per touch (0 and 0) are\n    checked as exact. Latency is over the cells for which one can be determined (four, Figure 2,\n    figure supplement 1A). The Results give 8.4 +- 13.3% for touch-evoked spikes of this group\n    where Table 1 gives 9.2 +- 13.7%; both are within each other's tolerance, and the Table 1\n    value is used here (fig3c-touch-spikes-outside uses the text). Reproduced when at least 13 of\n    the 17 values are within tolerance, partially for 9 to 12, not reproduced below 9.\n- id: table1-l5\n  statement: For the 11 L5 cells near C2 Table 1 gives, as mean +- s.d. (median), spikes per first\n    touch 1.95 +- 2.96 (0.98), per later touch 1.28 +- 1.88 (0.42), touch-evoked spikes 24.0 +-\n    18.6% (24.4%), touch and whisking spikes 31.5 +- 16.4% (36.0%), modulation depth 0.18 +- 0.12\n    (0.13), non-whisking rate 12.0 +- 9.87 (12.8) spikes/s, whisking rate 16.2 +- 15.3 (13.5)\n    spikes/s, onset latency 9.7 +- 5.2 (8) ms and minimum ISI 3.7 +- 2.5 (2.7) ms.\n  source: Table 1, row L5 Near C2 (n=11)\n  inferred: Numbers from Table 1, row L5 Near C2, with the garbled mean of touch-evoked spikes\n    read from Results, paragraph on Figure 3C; no sentence states them all.\n  expected:\n  - quantity: spikes per first touch, mean\n    value: 1.95\n    tolerance: 2.96\n  - quantity: spikes per first touch, median\n    value: 0.98\n    tolerance: 0.098\n  - quantity: spikes per later touch, mean\n    value: 1.28\n    tolerance: 1.88\n  - quantity: spikes per later touch, median\n    value: 0.42\n    tolerance: 0.042\n  - quantity: spikes evoked by touch, mean\n    value: 24.0\n    tolerance: 18.6\n    unit: '%'\n  - quantity: spikes evoked by touch, median\n    value: 24.4\n    tolerance: 2.44\n    unit: '%'\n  - quantity: spikes evoked by touch and whisking, mean\n    value: 31.5\n    tolerance: 16.4\n    unit: '%'\n  - quantity: spikes evoked by touch and whisking, median\n    value: 36.0\n    tolerance: 3.6\n    unit: '%'\n  - quantity: phase modulation depth, mean\n    value: 0.18\n    tolerance: 0.12\n  - quantity: phase modulation depth, median\n    value: 0.13\n    tolerance: 0.013\n  - quantity: non-whisking spike rate, mean\n    value: 12.0\n    tolerance: 9.87\n    unit: spikes/s\n  - quantity: non-whisking spike rate, median\n    value: 12.8\n    tolerance: 1.28\n    unit: spikes/s\n  - quantity: whisking spike rate, mean\n    value: 16.2\n    tolerance: 15.3\n    unit: spikes/s\n  - quantity: whisking spike rate, median\n    value: 13.5\n    tolerance: 1.35\n    unit: spikes/s\n  - quantity: onset latency, mean\n    value: 9.7\n    tolerance: 5.2\n    unit: ms\n  - quantity: onset latency, median\n    value: 8\n    tolerance: 1\n    unit: ms\n  - quantity: minimum ISI, mean\n    value: 3.7\n    tolerance: 2.5\n    unit: ms\n  - quantity: minimum ISI, median\n    value: 2.7\n    tolerance: 0.27\n    unit: ms\n  criterion: As table1-l4-c2, over the 11 cells (latency over the cells for which it can be\n    determined, see latency-determinable). Reproduced when at least 15 of the 18 values are within\n    tolerance, partially for 10 to 14, not reproduced below 10.\n- id: latency-determinable\n  statement: A touch-response latency could be determined for all 31 L4 C2 cells but for only four\n    of the 10 L4 cells outside C2, for lack of a touch response.\n  source: Figure 2, figure supplement 1A legend\n  quote: Latency from touch onset to onset of spiking response for 31 L4 cells in C2 (red), four L4\n    outside C2 (grey) and eleven L5 near C2 (yellow). Latencies could not be determined for six L4\n    outside cells and one L5 cell due to lack of touch response\n  expected:\n  - quantity: L4 C2 cells with a latency\n    value: 31\n    tolerance: 0\n  - quantity: L4 outside C2 cells with a latency\n    value: 4\n    tolerance: 0\n  criterion: Latency as in the Methods (Spike analysis), the first 1 ms PCTH bin after touch onset\n    above the pre-touch mean (-50 to 0 ms) plus two standard deviations; a cell has no latency\n    when no bin crosses. The legend contradicts itself for L5 (eleven plotted, one undetermined,\n    of 11 cells), so L5 is read as 10 or 11 and not judged. Open details, (1) the PCTH used (first\n    touches, or all touches), (2) the standard deviation (across the 50 pre-touch bins), (3) the\n    window searched after onset, read as (a) 0 to 50 ms, the post-touch span of the decoding\n    analysis, or (b) up to the cell's touch response cutoff. All combinations of (1) and (3) are\n    shown; the outcome is the one they all give, else methods_underspecified.\n- id: l4-outside-weaker-touch\n  statement: L4 neurons outside C2 respond much more weakly to touch than L4 neurons in C2, for\n    first and for later touches.\n  source: Results, L4 responses are temporally precise, paragraph 6; Figure 2B\n  quote: In L4, but outside of C2, touch responses were much weaker (first touch, p = 1.4e-5; later\n    touches, p = 6.32e-6; Wilcoxon rank sum)\n  statistics:\n  - about: spikes per first touch, L4 C2 against L4 outside C2\n    test: Wilcoxon rank sum\n    p: 1.4e-5\n    n: 31 and 10 cells\n  - about: spikes per later touch, L4 C2 against L4 outside C2\n    test: Wilcoxon rank sum\n    p: 6.32e-6\n    n: 31 and 10 cells\n  criterion: Spikes per touch per cell as in table1-l4-c2. Reproduced when both rank-sum tests\n    give p < 0.05 with the C2 median higher; partially when one does. Open detail, the measure\n    tested, read as (a) spikes per touch (Table 1 columns 1 and 2) or (b) the peak touch rate\n    (Figure 2C); both are shown, the outcome being the one they agree on, else\n    methods_underspecified.\n- id: l5-higher-rates\n  statement: L5 neurons near C2 have much higher spike rates than L4 neurons, with more diverse\n    touch responses.\n  source: Results, L4 responses are temporally precise, paragraph 6; Figure 2B-D; Table 1\n  quote: Layer 5 neurons near C2 had much higher firing rates, with touch responses that were more\n    diverse\n  criterion: The paper reports no test. From Table 1, the L5 median non-whisking and whisking\n    rates (12.8 and 13.5 spikes/s) are many times those of L4 C2 (0.32 and 0.33). Reproduced when\n    the L5 median is above the L4 C2 median for both rates and a Wilcoxon rank sum (the paper's\n    test for group comparisons) gives p < 0.05 for both. Diversity is not judged; the touch PSTHs\n    are shown.\n- id: phase-mod-l4-inside-outside\n  statement: Modulation by whisking phase does not differ between L4 neurons inside and outside\n    C2.\n  source: Results, L4 responses are temporally precise, paragraph 6; Figure 2, figure supplement\n    1B\n  quote: Modulation by whisking phase was not significantly different between L4 neurons inside and\n    outside the C2 barrel (p = 0.68)\n  statistics:\n  - test: Wilcoxon rank sum\n    p: 0.68\n    n: 31 and 10 cells\n  criterion: A claim of absence, judged on the paper's test, a Wilcoxon rank sum of per-cell\n    modulation depth (as in table1-l4-c2) between the 31 L4 C2 and 10 L4 outside cells. The\n    paper states no alpha; 0.05 is used, the conventional level and consistent with the p values\n    it calls significant (up to 0.019). Reproduced when p >= 0.05; the medians are reported.\n- id: phase-mod-l4-vs-l5\n  statement: L4 neurons, inside and outside C2, are more modulated by whisking phase than L5\n    neurons.\n  source: Results, L4 responses are temporally precise, paragraph 6; Figure 2, figure supplement\n    1B\n  quote: but both were significantly more phase modulated than L5 (p = 4.3e-5 and p = 0.012\n    respectively, Wilcoxon rank sum)\n  statistics:\n  - about: L4 C2 against L5\n    test: Wilcoxon rank sum\n    p: 4.3e-5\n    n: 31 and 11 cells\n  - about: L4 outside C2 against L5\n    test: Wilcoxon rank sum\n    p: 0.012\n    n: 10 and 11 cells\n  criterion: Modulation depth per cell as in table1-l4-c2. Reproduced when both rank-sum tests give\n    p < 0.05 with the L4 median higher; partially when one does.\n- id: whisking-rate-l4-no-change\n  statement: Across L4 neurons, inside and outside C2, spike rate does not change between whisking\n    and non-whisking periods.\n  source: Results, L4 responses are temporally precise, paragraph 6; Figure 2D\n  quote: There were no significant changes in firing rate between whisking and non-whisking across\n    the L4 population (L4 inside C2, p = 0.75; L4 outside C2, p = 0.92)\n  statistics:\n  - about: L4 inside C2\n    test: Wilcoxon signed rank\n    p: 0.75\n    n: 31 cells\n  - about: L4 outside C2\n    test: Wilcoxon signed rank\n    p: 0.92\n    n: 10 cells\n  criterion: A claim of absence, judged on the paper's test, a Wilcoxon signed-rank test of\n    per-cell whisking against non-whisking rate (the test named for L5 in the same sentence),\n    each group apart, at alpha 0.05 (not stated; see phase-mod-l4-inside-outside). Reproduced\n    when both p >= 0.05, partially when one is. Periods as in text-whisking-rates, with whisking\n    read with and without touch epochs; the outcome is the one both give, else\n    methods_underspecified. The median difference is reported.\n- id: whisking-rate-l5-increase\n  statement: L5 neurons fire modestly but significantly more during whisking than during\n    non-whisking periods.\n  source: Results, L4 responses are temporally precise, paragraph 6; Figure 2D\n  quote: whereas L5 showed a modest, but significant increase with whisking (p = 0.019, Wilcoxon\n    signed rank)\n  statistics:\n  - test: Wilcoxon signed rank\n    p: 0.019\n    n: 11 cells\n  criterion: As whisking-rate-l4-no-change, for the 11 L5 cells. Reproduced when p < 0.05 with the\n    median whisking rate higher, under both readings of whisking periods.\n- id: fig3c-touch-spikes-l4c2\n  statement: In L4 C2 neurons 70.6 +- 20.9% (mean +- s.d.) of spikes during exploration are coupled\n    to touch, within an average of 14.9% of exploration time.\n  source: Results, L4 responses are temporally precise, paragraph 8; Figure 3C\n  quote: Over the L4 C2 population, 70.6% ± 20.9% (mean, s.d.) of spikes were coupled to touch in\n    an average of 14.9% of exploration time\n  expected:\n  - quantity: touch-coupled fraction of exploration spikes, mean over 31 cells\n    value: 70.6\n    tolerance: 20.9\n    unit: '%'\n  - quantity: fraction of exploration time in touch windows, mean\n    value: 14.9\n    tolerance: 1.49\n    unit: '%'\n  criterion: Methods, Spikes accounted by active sensation. Exploration time is whisking epochs\n    with touch epochs, leaving out touches >100 ms. Each spike in exploration time is indexed by\n    the time since the closest touch onset, less the cell's latency; y_ton(t_i) is the number of\n    spikes within t_i of onset; the cutoff t_on is the first t_i where the increment falls below\n    the 95th percentile of the increments of 1000 surrogate curves from shuffled spike times,\n    curves smoothed by a degree-11 polynomial before differencing. The touch-coupled fraction is\n    y_ton(t_on) over all exploration spikes; the time fraction is the time within [latency,\n    latency + t_on] after touch onsets over exploration time. Open details, (1) the step of t_i,\n    taken as 1 ms (the paper's bin for touch analyses); (2) the shuffle, read as (a) spike times\n    drawn uniformly over exploration time or (b) the cell's spike times circularly shifted within\n    each trial's exploration time; (3) \"closest touch onset\", read as (a) the nearest onset before\n    the spike or (b) the nearest onset either side. All four combinations of (2) and (3) are run;\n    reproduced when both values are within tolerance under all, methods_underspecified when they\n    disagree.\n- id: fig3c-touch-spikes-outside\n  statement: L4 neurons outside C2 have far fewer touch-coupled spikes, 8.4 +- 13.3%, in 3.5% of\n    exploration time.\n  source: Results, L4 responses are temporally precise, paragraph 8; Figure 3C\n  quote: L4 neurons outside of C2 had significantly less touch-evoked spikes, 8.4% ± 13.3% in 3.5%\n    of exploration time (p = 6.53e-6, Wilcoxon rank sum)\n  statistics:\n  - about: touch-coupled fraction, L4 C2 against L4 outside C2\n    test: Wilcoxon rank sum\n    p: 6.53e-6\n    n: 31 and 10 cells\n  expected:\n  - quantity: touch-coupled fraction, mean over 10 cells\n    value: 8.4\n    tolerance: 13.3\n    unit: '%'\n  - quantity: fraction of exploration time in touch windows, mean\n    value: 3.5\n    tolerance: 0.35\n    unit: '%'\n  depends_on:\n  - fig3c-touch-spikes-l4c2\n  criterion: As fig3c-touch-spikes-l4c2, with its readings. Cells without a touch latency\n    (latency-determinable) have no touch window and count as 0% of spikes and time. Reproduced\n    when both values are within tolerance and the rank-sum test against L4 C2 gives p < 0.05 with\n    the outside median lower.\n- id: fig3c-touch-spikes-l5\n  statement: L5 neurons have fewer touch-coupled spikes than L4 C2 neurons, 24.0 +- 18.6%, in\n    19.0% of exploration time.\n  source: Results, L4 responses are temporally precise, paragraph 8; Figure 3C\n  quote: L5 neurons in C2 also showed significantly less touch-evoked spikes, 24.0% ± 18.6% touch\n    spikes in 19.0% of exploration time (p = 2.30e-5, Wilcoxon rank sum)\n  statistics:\n  - about: touch-coupled fraction, L4 C2 against L5\n    test: Wilcoxon rank sum\n    p: 2.30e-5\n    n: 31 and 11 cells\n  expected:\n  - quantity: touch-coupled fraction, mean over 11 cells\n    value: 24.0\n    tolerance: 18.6\n    unit: '%'\n  - quantity: fraction of exploration time in touch windows, mean\n    value: 19.0\n    tolerance: 1.9\n    unit: '%'\n  depends_on:\n  - fig3c-touch-spikes-l4c2\n  criterion: As fig3c-touch-spikes-outside, for the 11 L5 cells.\n- id: fig3d-touch-phase-l4c2\n  statement: In L4 C2 neurons 75.2 +- 19.0% of exploration spikes are coupled to touch or to\n    whisking phase, within an average of 22.0% of exploration time.\n  source: Results, L4 responses are temporally precise, paragraph 9; Figure 3D\n  quote: Overall, for neurons in C2 75.2 ± 19.0% of spikes were coupled to touch or whisking phase\n    in an average of 22.0% of exploration time\n  expected:\n  - quantity: touch or phase coupled fraction, mean over 31 cells\n    value: 75.2\n    tolerance: 19.0\n    unit: '%'\n  - quantity: fraction of exploration time in touch or phase windows, mean\n    value: 22.0\n    tolerance: 2.2\n    unit: '%'\n  depends_on:\n  - fig3c-touch-spikes-l4c2\n  criterion: After fig3c-touch-spikes-l4c2, the spikes not attributed to touch are indexed by the\n    time to the closest preferred phase of a whisk cycle (preferred phase from the cosine fit;\n    whisking epochs including those with non-monotonic phase, phase circular), y_whisk(t_i) built\n    and its cutoff t_w found by the same shuffle rule (Methods). The fraction is (touch spikes +\n    phase spikes) over exploration spikes; the time is the union of touch windows and windows of\n    +-t_w around each cycle's preferred phase, truncated at cycle margins (Figure 3B legend), over\n    exploration time. Open details as fig3c-touch-spikes-l4c2, plus (4) whether the phase window\n    is +-t_w or t_w wide in total; all combinations are run, with the same rule for disagreement.\n- id: fig3d-touch-phase-outside\n  statement: L4 neurons outside C2 have fewer touch or phase coupled spikes than L4 C2, 33.0 +-\n    30.2% in 16.9% of exploration time.\n  source: Results, L4 responses are temporally precise, paragraph 9; Figure 3D\n  quote: significantly more than outside of C2 (33.0 ± 30.2 in 16.9% of time; p = 2.88e-4)\n  statistics:\n  - about: touch or phase coupled fraction, L4 C2 against L4 outside C2\n    test: Wilcoxon rank sum\n    p: 2.88e-4\n    n: 31 and 10 cells\n  expected:\n  - quantity: touch or phase coupled fraction, mean over 10 cells\n    value: 33.0\n    tolerance: 30.2\n    unit: '%'\n  - quantity: fraction of exploration time, mean\n    value: 16.9\n    tolerance: 1.69\n    unit: '%'\n  depends_on:\n  - fig3d-touch-phase-l4c2\n  criterion: As fig3d-touch-phase-l4c2, with its readings; reproduced when both values are within\n    tolerance and the rank-sum test gives p < 0.05 with the outside median lower.\n- id: fig3d-touch-phase-l5\n  statement: L5 neurons have fewer touch or phase coupled spikes than L4 C2, 31.5 +- 16.4% in 26.1%\n    of exploration time.\n  source: Results, L4 responses are temporally precise, paragraph 9; Figure 3D\n  quote: or in L5 (31.5 ± 16.4 in 26.1% of time; p = 2.96e-5, Wilcoxon rank sum)\n  statistics:\n  - about: touch or phase coupled fraction, L4 C2 against L5\n    test: Wilcoxon rank sum\n    p: 2.96e-5\n    n: 31 and 11 cells\n  expected:\n  - quantity: touch or phase coupled fraction, mean over 11 cells\n    value: 31.5\n    tolerance: 16.4\n    unit: '%'\n  - quantity: fraction of exploration time, mean\n    value: 26.1\n    tolerance: 2.61\n    unit: '%'\n  depends_on:\n  - fig3d-touch-phase-l4c2\n  criterion: As fig3d-touch-phase-outside, for the 11 L5 cells.\n- id: fig3d-phase-only\n  statement: Spikes coupled to whisking phase alone are 4.6 +- 8.7% in L4 C2, 23.8 +- 27.9% in L4\n    outside C2 and 7.6 +- 14.9% in L5.\n  source: Results, L4 responses are temporally precise, paragraph 9; Figure 3D\n  quote: Subtraction of the touch spikes from touch and phase spikes reveals that 4.6 ± 8.7% of\n    spikes were purely phase coupled in L4 C2, vs 23.8 ± 27.9% outside of C2 and 7.6 ± 14.9% in L5\n  expected:\n  - quantity: phase-only fraction, L4 C2\n    value: 4.6\n    tolerance: 8.7\n    unit: '%'\n  - quantity: phase-only fraction, L4 outside C2\n    value: 23.8\n    tolerance: 27.9\n    unit: '%'\n  - quantity: phase-only fraction, L5\n    value: 7.6\n    tolerance: 14.9\n    unit: '%'\n  depends_on:\n  - fig3d-touch-phase-l4c2\n  criterion: Per cell, the touch or phase fraction less the touch fraction (fig3d-touch-phase-l4c2\n    and fig3c-touch-spikes-l4c2, same readings), then mean and s.d. per group. Reproduced when all\n    three means are within tolerance and the L4 outside mean is the largest of the three.\n- id: fig4a-touch-detection-c2\n  statement: Pooling the activity of only 15 L4 C2 neurons, integrated over 10 ms, is enough to\n    detect 95% of touches.\n  source: Results, Decoding touch, paragraph 1; Figure 4A\n  quote: Pooling activity from only fifteen L4 neurons (out of approximately 1600 [ Lefort et al.,\n    2009 ]) in C2 was sufficient to detect 95% of touches (integration time, 10 ms)\n  expected:\n    quantity: L4 C2 population size reaching 95% touch detection\n    value: 15\n    tolerance: 1.5\n    unit: neurons\n  criterion: Methods, Population decoding. Per neuron, touch-aligned responses from 30 ms before\n    to 50 ms after each touch, leaving out touches with a second touch within 50 ms. For a\n    population of N neurons drawn at random, 1000 responses per neuron drawn with replacement,\n    each spike train causally integrated over 10 ms and pooled across neurons; at each time point\n    a one-dimensional threshold decoder separates the pooled response from that in epochs without\n    touch, the threshold chosen on half the data and performance measured on the other half;\n    repeated to give 95% bounds. Open details, (1) the non-touch epochs, read as (a) the 30 ms\n    before touch in the same responses or (b) 10 ms windows drawn from exploration time away from\n    touch; (2) the performance measure, read as (a) the fraction of touches detected at the best\n    post-touch time point, with the threshold set for equal error, or (b) the percent correct\n    over touch and non-touch samples; (3) whether the 1000 draws pair across neurons by touch\n    (they cannot, as neurons were recorded apart; independent draws are used, as the Methods\n    imply). The number of neurons where the mean performance first reaches 95% is found for each\n    reading of (1) and (2); reproduced when it is within tolerance under all, else\n    methods_underspecified with every result shown.\n- id: fig4a-touch-detection-outside\n  statement: Touch detection by neurons from surrounding barrels, outside C2, is poor.\n  source: Results, Decoding touch, paragraph 1; Figure 4A\n  quote: Touch detection by neurons from surrounding barrels (>200 µm from the principal whisker)\n    was poor\n  depends_on:\n  - fig4a-touch-detection-c2\n  criterion: As fig4a-touch-detection-c2, sampling from the 10 L4 outside cells (with\n    replacement, as for C2). Reproduced when, under every reading, performance with 15 neurons is\n    below that of C2 and its 95% bound excludes 95% detection; the Methods' note of \"several-fold\n    more information about touch in C2\" is shown as the ratio of the population sizes needed for\n    equal performance.\n- id: fig4b-touch-time-precision\n  statement: A naive Bayes decoder reading 200 L4 C2 neurons integrated over 10 ms decodes the time\n    elapsed since touch with high precision, a minimum uncertainty of 0.55 ms (95% confidence) at\n    10 ms after touch onset.\n  source: Results, Decoding touch, paragraph 1; Figure 4B; Figure 4, figure supplement 1\n  quote: a group of 200 neurons in C2, integrating in 10 ms windows after touch, also allowed\n    decoding of elapsed time from touch with high precision (minimum 0.55 ms uncertainty with 95%\n    confidence at 10 ms post-touch onset using a naïve Bayes decoder\n  expected:\n    quantity: minimum decoding uncertainty of time since touch, 200 neurons\n    value: 0.55\n    tolerance: 0.055\n    unit: ms\n  criterion: Methods, Population decoding. Responses sampled as fig4a-touch-detection-c2, each\n    neuron's spike train integrated in a 10 ms sliding window; a multinomial naive Bayes\n    classifier reports the most likely time since onset at each 1 ms time point, with the RMS\n    time error from 100 bootstrap runs (Figure 4, figure supplement 1). Open details, (1) the\n    uncertainty, read as (a) the RMS error, (b) the half width of the 95% bound of decoded time\n    or (c) 1.96 times the RMS error; (2) train and test split, read as (a) half and half as for\n    touch detection or (b) independent resampled sets for training and testing. Reproduced when\n    the minimum over time points, at or near 10 ms after onset, is within tolerance under one\n    reading of (1) for both readings of (2); the readings that match are said. Also shown, that\n    the error falls with population size (Figure 4B inset).\n- id: fig4c-phase-decoding\n  statement: Even 1000 L4 neurons give only a rough estimate of whisking phase, a resolution of 24\n    deg in C2 and 33 deg outside C2 at d' = 1 (76% correct discrimination).\n  source: Results, Decoding touch, paragraph 2; Figure 4C\n  quote: a large population of neurons (1000) was required to provide even a rough estimate of\n    whisking phase (24° in C2, 33° outside at d′ = 1 performance, equivalent to 76% correct\n    discrimination)\n  expected:\n  - quantity: phase resolution at 76% correct, 1000 L4 C2 neurons\n    value: 24\n    tolerance: 2.4\n    unit: deg\n  - quantity: phase resolution at 76% correct, 1000 L4 outside C2 neurons\n    value: 33\n    tolerance: 3.3\n    unit: deg\n  criterion: Methods, Population decoding. Per neuron, spikes aligned to the phase of each whisk\n    cycle with peak amplitude >2.5 deg, binned in 120 bins over -pi to pi; neurons drawn with\n    replacement and their responses circularly shifted to give uniformly distributed preferred\n    phases; a naive Bayes classifier discriminates the population response at two phases; the\n    phase difference reaching 76% correct is found, median over 100 runs (Figure 4C legend).\n    Open details, (1) the response per cycle, read as (a) the spike count in each phase bin of one\n    cycle (Poisson or multinomial likelihood over cycles) or (b) the cycle-averaged rate per bin\n    used as a Poisson mean; (2) the shifts, read as (a) random uniform shifts or (b) shifts that\n    place preferred phases evenly. Reproduced when both values are within tolerance and C2 is\n    better than outside under all readings, else methods_underspecified.\n- id: fig5c-modulation-index\n  statement: Touch response magnitude of L4 C2 neurons is strongly modulated by touch order,\n    whisker velocity before touch and maximum curvature during touch, with mean modulation indices\n    of 0.71 +- 0.25, 0.71 +- 0.27 and 0.72 +- 0.23.\n  source: Results, Low spike count variability, paragraph 2; Figure 5A-C\n  quote: Touch response magnitude was highly modulated by each of the three variables (mean\n    modulation index ... touch order, 0.71 ± 0.25; velocity, 0.71 ± 0.27; max curvature, 0.72 ±\n    0.23; mean ± std\n  expected:\n  - quantity: modulation index by touch order, mean over 31 cells\n    value: 0.71\n    tolerance: 0.25\n  - quantity: modulation index by pre-touch velocity, mean\n    value: 0.71\n    tolerance: 0.27\n  - quantity: modulation index by maximum curvature, mean\n    value: 0.72\n    tolerance: 0.23\n  criterion: Figure 5 legend. Per L4 C2 cell, touches sorted by the property and split into 10\n    bins with equal numbers of touches; the mean spikes per touch in the cell's spike integration\n    window (touch spike window) per bin; modulation index (max bin - min bin)/(max bin + min bin).\n    Properties, order of the touch in its trial; whisker velocity at touch onset (d theta/dt);\n    maximum curvature change during the touch. Open details, (1) velocity, read as (a) the\n    velocity at the onset frame or (b) the mean over the 1 to 5 ms before onset; (2) curvature,\n    read as (a) max |Delta kappa| over the whole touch or (b) over 0 to 20 ms after onset (the\n    window of the Methods for clustering); (3) touch order, where ties make equal bins\n    impossible, read as (a) ranks with ties broken at random or (b) bins of whole order values\n    as near equal as they can be. Reproduced when all three means are within tolerance under all\n    readings, else methods_underspecified.\n- id: fig5-modulation-correlations\n  statement: Across cells, responsiveness to pre-touch velocity and to maximum curvature covary\n    strongly (r = 0.80), and responsiveness to touch order is somewhat less correlated with both\n    (r = 0.70 and 0.65).\n  source: Results, Low spike count variability, paragraph 2; Figure 5B-C\n  quote: Responsiveness to pretouch velocity and max curvature covaried strongly (pairwise\n    correlation coefficient 0.80, p = 4.3e-8), whereas touch order response was somewhat less\n    correlated with velocity and curvature (correlation coefficients 0.70, 0.65, p = 1.0e-5, p =\n    8.2e-5)\n  statistics:\n  - about: velocity against curvature\n    test: correlation\n    statistic: r = 0.80\n    p: 4.3e-8\n  - about: touch order against velocity\n    test: correlation\n    statistic: r = 0.70\n    p: 1.0e-5\n  - about: touch order against curvature\n    test: correlation\n    statistic: r = 0.65\n    p: 8.2e-5\n  expected:\n  - quantity: correlation, velocity and curvature responsiveness\n    value: 0.80\n    tolerance: 0.08\n  - quantity: correlation, touch order and velocity responsiveness\n    value: 0.70\n    tolerance: 0.07\n  - quantity: correlation, touch order and curvature responsiveness\n    value: 0.65\n    tolerance: 0.065\n  depends_on:\n  - fig5c-modulation-index\n  criterion: The paper does not say what is correlated. Readings, (a) Pearson correlation across\n    the 31 L4 C2 cells of the modulation indices of fig5c-modulation-index (the reported p values\n    are those of Pearson r with 29 degrees of freedom, e.g. r = 0.70 gives p near 1e-5); (b)\n    Pearson correlation of the peak-normalized 10-bin tuning curves (Figure 5B) pooled over cells\n    and bins. Reproduced when all three r are within tolerance with p < 0.05 under one reading,\n    with velocity-curvature the largest; the readings that match are said.\n- id: fig6s1b-clusters-less-variable\n  statement: The clustering of touches into five groups finds subsets with significantly less\n    variability in touch properties than random samples of touches.\n  source: Figure 6, figure supplement 1B legend\n  quote: The procedure finds subset of points with significantly less behavioral variability than\n    in the full dataset\n  criterion: Methods, Analysis of spike count variance. Per L4 C2 cell, touches with inter-contact\n    interval >250 ms; z-scored pre-touch velocity and maximum curvature change 0 to 20 ms after\n    touch; OPTICS ordering; the run of N consecutive ordered touches with the smallest sum of\n    pairwise distances is the first group, removed, and repeated for five groups, N being 20% of\n    the touches (Figure 6, figure supplement 1A) and at least 20. Open details, (1) OPTICS\n    parameters (minimum points, maximum radius), not given, read as (a) minimum points 5 with\n    unbounded radius (the scikit-learn default) or (b) minimum points N; (2) inter-contact\n    interval, read as (a) time since the previous touch offset or (b) since the previous onset;\n    (3) N, read as 20% of the selected touches at the start, fixed for all five groups. The\n    standard deviation of z-scored velocity in each group is compared with that of 1000 random\n    samples of N touches; reproduced when, under all readings, the group standard deviation is\n    below the 5th percentile of the random ones for the first group in most (>50%) cells.\n- id: fig6cd-ff-near-binomial\n  statement: Across L4 C2 neurons, the Fano factor following touch drops below one, lying close to\n    the binomial limit (the theoretical minimum) for most cells.\n  source: Results, Low spike count variability, paragraph 4; Figure 6C-D\n  quote: Across the population of neurons within C2 the FF following touch dropped below one, with\n    the FF lying close to the binomial limit for most cells\n  depends_on:\n  - fig6s1b-clusters-less-variable\n  criterion: Figure 6C legend and Methods. Per cell and per touch group (fig6s1b, same readings),\n    FF of spike counts in 10 ms windows starting 0 to 20 ms after touch in 1 ms steps; the\n    minimum over windows per group, and the minimum across the five groups. Open details, (1)\n    which minimum, read as (a) per group (Figure 6C red circles) or (b) across groups (blue\n    circles); (2) \"close\", which the paper does not define, read as (a) the binomial limit 1 - m\n    lies inside the cell's 95% resampling interval of the FF (1000 resamples, Methods) or (b) the\n    FF lies nearer the binomial limit than the Poisson value 1. Reproduced when the population mean\n    of the minimum FF is below 1 and, for more than half of the cells, the FF is close under the\n    reading in force; every combination is run, the outcome being the one they all give, else\n    methods_underspecified.\n- id: fig6d-not-refractory\n  statement: The low Fano factor after touch cannot be explained by a Poisson process with a 2.3\n    ms refractory period and rates matched to each neuron.\n  source: Results, Low spike count variability, paragraph 6; Figure 6D\n  quote: Comparing the simulations with actual spike trains revealed that L4 neuron response\n    precision could not be explained by the refractory period alone\n  depends_on:\n  - fig6cd-ff-near-binomial\n  criterion: Methods, last paragraph, and Figure 6D. Per L4 C2 cell, spike trains simulated as a\n    Poisson process with an absolute refractory period of 2.3 ms (the median minimum ISI) and a\n    time-varying rate equal to the cell's touch PSTH (1 ms bins), one simulated train per real\n    touch; FF computed as for the data in 10 ms sliding windows. Open details, (1) which touches,\n    read as all >250 ms touches pooled, or per group as fig6cd; (2) the comparison, which the\n    paper gives only as a figure, read as (a) the population mean data FF below the model's at\n    the window of the data minimum, by more than the sum of the two s.e.m. (Figure 6D error\n    bars), or (b) the per-cell data FF below the model's in more than half of the cells by a\n    sign test at p < 0.05. Every combination is run; the outcome is the one they all give, else\n    methods_underspecified.\n- id: fig6e-sample-epoch-ff\n  statement: Counting spikes over the whole sample epoch, ignoring the millisecond structure of\n    behavior, gives a very large Fano factor of 6.57 +- 5.41 (mean +- s.d. over L4 C2 cells).\n  source: Results, Low spike count variability, paragraph 7; Figure 6E, condition 1\n  quote: Response variability was very large (FF = 6.57 mean ± 5.41 s.d.) when we ignored the\n    millisecond time scale of behavior\n  expected:\n    quantity: sample-epoch FF, mean over L4 C2 cells\n    value: 6.57\n    tolerance: 5.41\n  criterion: Figure 6E legend, condition 1. Per L4 C2 cell, FF across trials of the spike count\n    while the pole is within reach; mean and s.d. over the 31 cells. Reproduced when the mean is\n    within tolerance and above 1.\n- id: fig6e-random-38ms-ff\n  statement: Counting spikes in random 38 ms windows, as many per trial as there are touches, gives\n    a Fano factor of 1.59 +- 0.49.\n  source: Results, Low spike count variability, paragraph 7; Figure 6E, condition 2\n  quote: Integrating activity in time windows as wide as average touch response periods (38 ms)\n    gave a FF of 1.59 ± 0.49\n  expected:\n    quantity: random 38 ms window FF, mean over L4 C2 cells\n    value: 1.59\n    tolerance: 0.49\n  criterion: Figure 6E legend, condition 2. Per cell, in each trial as many 38 ms windows at random\n    times as the trial has touches; FF across all windows of the cell; mean over the 31 cells.\n    Open detail, where windows are drawn, read as (a) within the sample epoch or (b) anywhere in\n    the trial (\"randomly sampling from the trial\"); both are run with 100 random draws, the mean\n    reported. Reproduced when the mean is within tolerance under both, else\n    methods_underspecified.\n- id: fig6e-touch-38ms-ff\n  statement: Counting spikes in 38 ms windows aligned to touch onset (after a 6 ms latency) gives\n    a Fano factor of 1.37 +- 0.74.\n  source: Results, Low spike count variability, paragraph 7; Figure 6E, condition 3\n  quote: and FF of 1.37 ± 0.74 ( Figures 6E, 3 ) when aligned to touch onset\n  expected:\n    quantity: touch-aligned 38 ms window FF, mean over L4 C2 cells\n    value: 1.37\n    tolerance: 0.74\n  criterion: Figure 6E legend, condition 3. Per cell, spike counts in the window 6 to 44 ms after\n    each touch onset; FF across touches; mean over the 31 cells. Open detail, the touches, read\n    as (a) all touches or (b) touches with inter-contact interval >250 ms; both are run, and the\n    outcome is the one both give, else methods_underspecified.\n- id: fig6e-touch-10ms-ff\n  statement: A narrower 10 ms window after touch reduces the Fano factor to 0.73 +- 0.19.\n  source: Results, Low spike count variability, paragraph 7; Figure 6E, condition 4\n  quote: Using a narrower touch window of 10 ms reduced the FF to 0.73 ± 0.19\n  expected:\n    quantity: minimum 10 ms window FF after touch, mean over L4 C2 cells\n    value: 0.73\n    tolerance: 0.19\n  criterion: Figure 6E legend, condition 4. Per cell, the minimum over 10 ms windows starting 0 to\n    20 ms after touch onset (1 ms steps) of the FF across touches; mean over the 31 cells. Open\n    details, (1) the touches, as fig6e-touch-38ms-ff; (2) the window starts, read as (a) 0 to 20\n    ms or (b) 0 to 10 ms so that windows lie within 0 to 20 ms. Every combination is run; the\n    outcome is the one they all give, else methods_underspecified.\n- id: fig6e-similar-touch-ff\n  statement: Computed only across similar touches, the 10 ms Fano factor falls further to 0.54 +-\n    0.27, so that L4 responses to touch are almost noiseless.\n  source: Results, Low spike count variability, paragraph 7; Figure 6E, condition 5\n  quote: The FF was further reduced to 0.54 ± 0.27 when calculated only across similar touches\n  depends_on:\n  - fig6s1b-clusters-less-variable\n  expected:\n    quantity: minimum 10 ms window FF within touch groups, mean over L4 C2 cells\n    value: 0.54\n    tolerance: 0.27\n  criterion: Figure 6E legend, condition 5. As fig6e-touch-10ms-ff, within each of the five touch\n    groups of fig6s1b-clusters-less-variable (same readings). Open detail, the per-cell value,\n    read as (a) the minimum across the five groups (Figure 6C blue circles) or (b) the mean over\n    groups of each group's minimum. Every combination is run; reproduced when the mean is within\n    tolerance under all and, as the paragraph states, the five conditions of Figure 6E fall in\n    order (1 > 2 > 3 > 4 > 5) under the same readings; else methods_underspecified.\n- id: whisk-cycle-spikes\n  statement: L4 neurons fire few spikes during whisker movements, on average fewer than 0.15 spikes\n    per whisk cycle, which hinders decoding of whisking phase.\n  source: Discussion, paragraph 7; Figure 4\n  quote: their low spike rates during whisker movements (mean <0.15 spikes/whisk cycle) hinders\n    efficient decoding of whisking phase from population activity\n  criterion: Per L4 cell (inside and outside C2), spikes per whisk cycle over the whisking cycles\n    used for phase analysis (amplitude >2.5 deg, monotonic phase, not during licking or within 70\n    ms after touch). Open detail, the population, read as (a) L4 C2 cells or (b) all 41 L4 cells,\n    and the mean as (a) over cells or (b) over all cycles pooled. Reproduced when the mean is\n    below 0.15 under all readings, else methods_underspecified.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && python tools/claims_check.py claims/000013/10.7554-elife.06619.yaml paper/10.7554-elife.06619.txt; grep -n " — \|rather" claims/000013/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && grep -n "[^ ] #\| #[^ ]" claims/000013/*.yaml | grep -v "^[0-9]*:#" | head; grep -c "^- id:" claims/000013/*.yaml; grep -c "^  criterion:" claims/000013/*.yaml; grep -c "^  statistics:" claims/000013/*.yaml
```

```
44
44
11
```

**Agent**

I wrote `claims/000013/10.7554-elife.06619.yaml` with 44 claims. The checker passes the schema and every quote, but it exits non-zero on two p-values it can't match. The paper prints them with a trailing zero ("p = 2.30e-5", "p = 1.0e-5"), and I confirmed both against the text by reading. Nothing is committed.

**Text read:** the version of record (PMC4525079, from Europe PMC). It has the main text, Methods, Table 1, every figure and figure-supplement legend, the decision letter and the author response. eLife has no supplement beyond the figure supplements, whose legends are in the text. There was no PDF, so I read no figure images. One Table 1 cell is garbled (L5 "24.0–18.6%"); I read it as 24.0 ± 18.6% from the Results.

**Code:** the paper links github.com/hireslab/HLab_Whiskers, read at commit cdbc914 (2020); the last commit before publication is 0eb360a. It holds only whisker-tracking post-processing, contact detection and data classes. None of the paper's analyses are in it, so it settles no criterion.

**Counts:**
- 44 claims; 41 have quotes and 3 (the Table 1 rows) are marked `inferred`.
- 11 claims carry statistics, 16 entries in all: Wilcoxon rank-sum and signed-rank tests, and correlations.
- All 44 have criteria. All use the dataset's own data.

**Details the paper leaves open, and the readings named:**
- **The example cell is not identified.** I take it as the L4 C2 cell matching 0.73 → 1.91 spikes/s and FF 7.51. Two sets of numbers could be that cell or the population: "1.51/0.31 spikes per touch, 8 ms" and "0.67/0.23 spikes/s while whisking / not whisking". For each, the readings are the example cell, the L4 C2 mean, the median, and (for the rates) all spikes pooled.
- **Trials used:** all trials, or the "performing trials analyzed". **Sample-epoch range:** over trials or over session means.
- **Whisking bouts:** whether peak-to-peak is twice the Hilbert amplitude or the range of theta within a cycle, and whether touches break a bout.
- **Touch latency:** which PCTH (first touches or all touches) and how far after onset to search. The legend contradicts itself on L5 latencies, so L5 is not judged there.
- **Touch-coupled spikes (Figure 3):** how spike times are shuffled (uniform, or circular shift), "closest touch onset" (before the spike, or either side), and whether the phase window is ±t_w or t_w wide.
- **Decoders (Figure 4):**
  - What the "non-touch" epochs are, and the detection measure (hit rate, or percent correct).
  - The timing "uncertainty": RMS error, half-width of the 95% bound, or 1.96 × RMS.
  - The phase-decoder likelihood and how the shifts are drawn.
- **Figure 5:** the velocity window and the curvature window, how ties in touch order are binned, and what the correlations are taken over. Across the 31 cells' modulation indices fits the reported p-values; pooled tuning curves is the other reading.
- **Figure 6:**
  - OPTICS parameters, and whether the inter-contact interval runs from the previous touch's onset or offset.
  - Which minimum Fano factor counts: per group, or across the five groups.
  - What "close to the binomial limit" means: the limit inside the resampling interval, or nearer the limit than to 1.
  - How the data and the refractory-Poisson model are compared.
  - Which touches feed the Figure 6E conditions, where the random windows are drawn, and the range of sliding-window starts.
- **No alpha is stated** for the claims of no difference. I used 0.05, which fits the p-values the paper calls significant.

**Inconsistencies in the paper:** for L4 outside C2, the touch-evoked spike fraction is 8.4 ± 13.3% in the Results and 9.2 ± 13.7% in Table 1. Both are recorded.

**Missing:** nothing a claim needed. The text is complete.

## End of run

24 turns, 12 minutes, result: success.
