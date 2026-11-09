# 001474 · claims · run 39650857745

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/001474/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^### 3. Write the claims file/,/^## Author/p' docs/protocol.md
```

```
### 3. Write the claims file

Write `claims/<folder>/<doi with / replaced by ->.yaml`. Its opening comment
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
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; wc -c paper/*; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml",
 "limit": 200
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
[... 180 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41598-025-19800-2.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41598-025-19800-2.txt').read()
print(t[51000:85000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0a75de0f-bcf8-4ffb-aeea-918eb351b9ea/tool-results/bcuvsjyr9.txt"
}
```

```
1	sponsive circuits. Consequently, the influence of leptin on these upstream neurons and on PVH MC4R activity is predicted to be blunted in HFD conditions. Moreover, in our study, we did not find evidence that PVH MC4R neurons themselves are “sick” or non-functional. Rather, they still respond dynamically during feeding. Importantly, administration of a leptin antagonist in DIO mice promotes additional food intake 60 . Hence, our finding of elevated food consumption response early in the meal may be due to the persistently high level of leptin in DIO mice, both before and after the meal. In both cases, leptin is likely to saturate its receptor, leading to consistently elevated excitability of POMC neurons and reduced excitability of AgRP neurons. Under these conditions, cAMP levels in PVH MC4R neurons may not return to a low level in between meals, potentially preventing a downward resetting of the strength of consumption-evoked synaptic inputs to PVH MC4R neurons. Concurrently, we observed that calorie-restricted HFD mice, despite being calorie-matched to the NCD group and theoretically having the same acute caloric deficit while exhibiting increased adiposity and leptin levels, exhibited small meal sizes during the recordings, as expected based on their higher early-session PVH MC4R neuron responses. This hypothesis is consistent with the counterintuitive finding from Scherer and colleagues that clamping leptin at a lower level in DIO mice actually reduces body weight, despite the anorexigenic actions of leptin in healthy mice 61 . This clamping may allow restoration of consumption-evoked responses to a lower magnitude early in the meal, and the associated restoration in leptin sensitivity may also be involved in restoring the normal increase in response magnitude throughout the meal. Our findings, together with the aforementioned effects of leptin antagonist administration in DIO mice, suggest that the mechanisms responsible for suppressing homeostatic feeding, s
[... 100 more lines not kept]
```

**Agent**

I've read the main text and Methods. Next I'll check the supplement portion of the text file.

**Agent calls Bash**

```bash
cd paper; grep -n -i -o ".\{0,80\}supplement.\{0,80\}" 10.1038-s41598-025-19800-2.txt | awk -F: '$1>5' | head; grep -n "^\[\|^=\|^---" 10.1038-s41598-025-19800-2.txt | head -30; wc -l 10.1038-s41598-025-19800-2.txt
```

```
7:insight into the pathological neural consequences of an obesogenic environment. Supplementary Information The online version contains supplementary material available at 
7:ls required a longer time to reach a steady-state level of reduced body weight (Supplementary Fig. 1a, b) and to engage in and learn the operant task (not shown). HFD-fed
7: steadily reduced their licking rates from early to late phases of the session (Supplementary Fig. 1c, d). Compared to NCD-fed animals, food-seeking-related locomotion wa
7:s negligible in HFD-fed animals (Fig. 1 e, f (top panels), Supplementary Fig. 1e), and it was further reduced to a minimum level late near the end of
7: the meal (Supplementary Fig. 1e). Using a head-fixed fiber photometry setup, we tracked calcium sign
7:als in real-time in parallel with licking behavior and locomotion (Fig. 1 e, f, Supplementary Fig. 1f, g). Of all the trials in a session, we only analyzed the trials in 
7:k feeding-evoked responses early in the meal (first 15 trials) (Fig. 1 e, i, j, Supplementary Fig. 1h). Similar to our prior study 5 , as the animals progressed through t
7:xperiment compared to the NCD-fed animals (Fig. 1 e, f (lower panels), see also Supplementary Fig. 1c, d (below)). As discussed above, we matched levels of total daily ca
7:animals, and these acute responses persisted until the end of the feeding bout (Supplementary Fig. 1h, i). We next assessed the magnitude of PVH MC4R neuron responses dur
7:early to late in the meal when considering a longer window of 0–20 s post tone (Supplementary Fig. 1i). These experiments confirm prior results 5 showing that PVH MC4R ne
6:------------------------------------------------------------------------
9:[HYPERLINKS]
241:[1] Andermann, M. L. & Lowell, B. B. Toward a wiring diagram understanding of appetite control. Neuron 95, 757–778 (2017). 10.1016/j.neuron.2017.06.014
243:[2] Garfield, A. S. et al. A neural basis for melanocortin-4 receptor–regulated appetite. Nat. Neurosci. 18, 8
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n '360,756p' 10.1038-s41598-025-19800-2.txt | grep -v "^\[[0-9]*\]" | grep -v '^$' | head -300
```

```
##### Supplement: 41598_2025_19800_MOESM1_ESM.pdf
=== page 1 ===
 
1 
Supplementary Figure 1. Validation of GCaMP6s photometry signals and behavioral 
2 
dynamics during food restriction in NCD- and HFD-fed mice 
3 
a, b, Post-surgical bodyweight dynamics during ad libitum feeding (light gray), food restriction 
4 
(FR, no shading), and continued food restriction maintenance during the photometry recording 
5 
(FR + recording, dark shading) of NCD-fed (a) and HFD-fed (b) mice. 
6 
c, Mean lick rate during early and late meal phases for NCD-fed (top panel) and HFD-fed (bottom 
7 
panel) mice. 
8 
d, Area under the curve (AUC) quantification of post-cue lick-rate, normalized to baseline pre-
9 
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; awk 'NR>360' 10.1038-s41598-025-19800-2.txt | grep -v '^$' | sed -n '/^=== page 7/,$p' | grep -v "^\[[0-9]*\]" | head -150
```

```
=== page 7 ===
mice (averaged across sessions per mouse) for NCD mice switched to HFD for 6 weeks (HFD6w) 
93 
or maintained on NCD. Two-tailed paired Student’s t-test 
94 
e – h, Single-trial mean lick rate during cue presentation (0 – 1 s post-cue onset) across 90 trials 
95 
averaged across recordings with at least 30 successfully triggered trials in the NCD→NCD (e), 
96 
HFD→NCD (f), HFD→HFD (g), NCD→HFD6w (h) groups, comparing pre-diet-switch (solid line) 
97 
and post-diet-switch (dashed line) conditions. 
98 
i, Mean Z-scored PVHMC4R neuronal responses during early (first 15 trials) and late meal (last 15 
99 
trials) phases of the meal, for individual mice (averaged across sessions per mouse) across the 
100 
following conditions post-diet switch: NCD→NCD, HFD→NCD, HFD→HFD. Paired, two-tailed t-
101 
test between early-meal and late-meal trials. 
[... 64 more lines not kept]
```

**Agent**

The text holds the main article, Methods, and the supplementary figure legends (MOESM1). Next I'll look at the linked code and the dandiset's description.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/xzhang03/Photometry_analysis && cd Photometry_analysis && git log -1 --format='%H %cd' && git ls-files | head -100 && git ls-files | wc -l; curl -s https://api.dandiarchive.org/api/dandisets/001474/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:3000])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001474/versions/0.251031.1725/info/ | python3 -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('description'));print(d.get('keywords'));print(json.dumps(d.get('assetsSummary'),indent=0)[:1500])"; cd $TMPDIR/Photometry_analysis; git ls-files | tail -55; cat README.md | head -60
```

Result: the fetched text is not kept.

**Agent**

The linked repository is the lab's general photometry preprocessing toolbox (MATLAB). Next I'll check which parts bear on the paper's steps (pulse extraction, filtering, dF/F, Z-score).

**Agent calls Bash**

```bash
cd $TMPDIR/Photometry_analysis; cat functions/tcpZscore.m functions/tcpZ.m; grep -n -i "median\|lowpass\|50\|freq\|filt" tcpPreprocess.m | head -40; grep -rl -i "zscore\|ensure\|lick" --include=*.m . | head -30
```

```
function dataz = tcpZscore(datainput, badframes, external_sigma)
% tcpZscore calculates zscore of data while excluding bad frames from being
% involved in calculating either standard deviation or mean. If an external
% standard deviation value is supplied, that value is used instead.

% dataz = tcpZscore(datainput, badframes, external_sigma)
if nargin < 3
    external_sigma = [];
    if nargin < 2
        badframes = [];
    end
end

% Make a copy of the data
datacopy = datainput;

% Remove bad frames
if ~isempty(badframes)
    datacopy(badframes) = [];
end
[... 270 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Photometry_analysis; grep -n "\bZ\b\|Z)" tcpTrigger.m functions/tcpDatasnapper.m "functions/Group analysis/mkdatastruct_mating.m" "functions/Group analysis/ppdatastruct.m" | head -40; sed -n 314,340p tcpPreprocess.m; grep -n "dff\|baseline\|prew\|10 s\|pre" tcpTrigger.m | head -40
```

```
functions/Group analysis/mkdatastruct_mating.m:35:if p.loadinternalz, datastruct.Z = []; end
functions/Group analysis/mkdatastruct_mating.m:59:        loaded = load (fullfile(loadingcell{i,1}, loadingcell{i,2}), 'Z');
functions/Group analysis/mkdatastruct_mating.m:60:        datastruct(i).Z = loaded.Z(1);
functions/Group analysis/ppdatastruct.m:27:addOptional(p, 'useinternalsigma', false); % Use internal sigma (which is calculated through tcpZ)
functions/Group analysis/ppdatastruct.m:115:            tcpZscore(datastruct_pp(i).photometry, zscore_badframes, datastruct_pp(i).Z);
%% Low pass filter
% Design a filter kernel
switch freq
    case 10
        d = designfilt("lowpassfir", 'PassbandFrequency', 4, 'StopbandFrequency', 5, ...
            'PassbandRipple', 0.1, 'StopbandAttenuation', 20, 'DesignMethod', 'equiripple',...
            'SampleRate', freq);
    otherwise
        d = designfilt("lowpassfir", 'PassbandFrequency', 8, 'StopbandFrequency', 10, ...
            'PassbandRipple', 0.1, 'StopbandAttenuation', 40, 'DesignMethod', 'equiripple',...
            'SampleRate', freq);
end
% fvtool(Hd)

% Filter data
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Photometry_analysis; sed -n 1,140p "functions/Group analysis/ppdatastruct.m"
```

```
function datastruct_pp = ppdatastruct(datastruct, varargin)
% ppdatastruct post-process data structure
% datastruct_pp = ppdatastruct(datastruct, ppcfg)

% Parse inputs
p = inputParser;

addOptional(p, 'Fs_ds', 5); % Fps to downsample to
addOptional(p, 'smooth_window', 5); % Window size for smoothing


addOptional(p, 'BlankTime', 20);    % Number of seconds to keep  after the 
                                    % last behavioral score. Leave empty if
                                    % no chopping.
addOptional(p, 'First_point', 1); % Throw away the first X points.
addOptional(p, 'merging', []);  % merge datasets if needed. Input is a 
                                % vector where 0 means no merging, and 
                                % every non-zero number is merged with the
                                % dataset with the same number
% Zscore parameters
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; which pdftoppm mutool; python3 -c "import fitz;print(fitz.__doc__)"; python3 -c "
import fitz
d=fitz.open('paper/10.1038-s41598-025-19800-2.supp.pdf')
print(len(d))
for i in [0,2,5]:
    d[i].get_pixmap(dpi=110).save(f'supp{i+1}.png')
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41598-025-19800-2.supp.pdf",
 "pages": "1,3,6"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I can't render the PDF pages (no pdftoppm or PyMuPDF), so stars shown only in figures stay unread. Next I'll check what schema the claims checker enforces.

**Agent calls Bash**

```bash
sed -n 1,400p tools/claims_check.py | grep -n "def \|required\|allowed\|KEYS\|keys\|'[a-z_]*'" | head -80
```

```
34:def norm(s: str) -> str:
41:def flattenings(raw: str) -> list[str]:
48:def quote_found(quote: str, texts: list[str]) -> bool:
63:def printed_forms(v: float) -> set[str]:
78:def check(claims_path: Path, paper_paths: list[Path]) -> int:
100:    print(f"{claims_path}: {len(doc.get('claims', []))} claims, {quotes} quotes, "
105:def main() -> int:
```

**Agent calls Bash**

```bash
sed -n 1,130p tools/claims_check.py; ls tools; grep -rn "statistics" tools/*.py | head -20
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

[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"
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
python3 -c "
import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1)[:5000])"
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
cd $TMPDIR/Photometry_analysis; sed -n 60,100p tcpPreprocess.m | head -5; grep -n "freq\s*=\|ppCfg.freq\|50" functions/ppCfg_UI.m | head
```

```
% Grab pulse info
    ch1_pulse = data(ch1_pulse_ind,:) > ch1_pulse_thresh;
    ch2_pulse = data(ch2_pulse_ind,:) > ch2_pulse_thresh;
end

249:    freq = ppCfg.freq;
262:    blackout_window = 9; % Ignore the first X points within each pulse due to capacitated currents (9 for 2500 Hz)
265:    freq = 50; % Sampling rate after downsampling (i.e., pulse rate of each channel in Hz)
282:hfig = figure('position', [300 200 250 550], 'MenuBar', 'none', 'ToolBar', 'none');
300:uicontrol(hfig, 'Style', 'text', 'String', 'Ch1 Data', 'Position', topleft + [0 2*majory 50 20]);
302:    'Position', topleft + [0 2*majory+minory 50 20], 'callback', @updaterigsfromboxes);
305:uicontrol(hfig, 'Style', 'text', 'String', 'Ch2 Data', 'Position', topleft + [minorx 2*majory 50 20]);
307:    'Position', topleft + [minorx 2*majory+minory 50 20], 'callback', @updaterigsfromboxes);
310:uicontrol(hfig, 'Style', 'text', 'String', 'Cam', 'Position', topleft + [minorx*2 2*majory 50 20]);
312:    'Position', topleft + [minorx*2 2*majory+minory 50 20], 'callback', @updaterigsfromboxes);
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "claims/001474/10.1038-s41598-025-19800-2.yaml",
 "content": "# Claims for Porniece, Baker, Ausfahl, Zhang & Andermann (2025), Sci Rep 15, 35837, on dandiset\n# 001474. Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions),\n# 2026-10-21, protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (open access) as served by Europe PMC (PMC12521569): main\n# text, figure legends and Methods, with Supplementary Material 1 (41598_2025_19800_MOESM1_ESM.pdf,\n# the legends of Supplementary Figures 1 to 3), all in paper/10.1038-s41598-025-19800-2.txt. The\n# supplementary PDF could not be rendered here, so significance marks shown only inside figures\n# were not read. The main figures were not available as images. Supplementary Materials 2 to 8\n# (presumably the source data) were not in the text.\n#\n# Code read: https://github.com/xzhang03/Photometry_analysis, commit b88d3943 (the repository the\n# Methods cite for the analysis). It is the lab's general MATLAB photometry toolbox. It holds\n# preprocessing: per-pulse median extraction (tcpPreprocess.m), a zero-phase FIR low-pass filter\n# (passband 8 Hz, stopband 10 Hz at 50 Hz sampling), trial cutting (tcpTrigger.m), and tcpZ.m, which\n# computes one standard deviation per mouse from all of that mouse's recordings concatenated, each\n# recording's filtered fluorescence mean-subtracted from sample 50 on. It holds none of this paper's\n# Python analysis (response windows, early and late phases, LME models, t-tests, correlations).\n# The Nanosec task software (github.com/xzhang03/NidaqGUI) was not read for analysis choices.\n#\n# Data the paper used. Male and female MC4R-Cre tg/wt mice, GCaMP6s in PVH MC4R neurons, one\n# optic fiber over the PVH, head-fixed on a circular treadmill (running speed by IR beam), lick\n# spout. Normal chow (NCD) or 60% fat diet (HFD) from 5 weeks of age, then calorie-matched food\n# restriction (~9.5 kcal/day). Sessions have a 5-min baseline, then one trial per 60 s; a 2 kHz\n# tone, and ~50 uL Ensure if the mouse licks within 1 s of tone onset (\"triggered\" trial). Signals\n# at 50 Hz after demodulation, 10 Hz low-pass; trials cut 10 s before to 50 s after the tone.\n# Measured variables are the 465 nm photometry signal (405 nm control), licks, running speed,\n# body weight, home-cage food and Ensure intake.\n#   Cohort 1 (Fig. 1, Supp. Fig. 1): 60-trial sessions; NCD 39 recordings/6 mice, HFD 33\n#     recordings/5 mice (recordings with at least 30 triggered trials).\n#   Cohort 2 (Fig. 2, Supp. Fig. 2), \"a new cohort\": 90-trial sessions; NCD 59 recordings/7 mice,\n#     HFD 54 recordings/7 mice. Supp. Fig. 2l splits these into food-restricted only (NCD 31, HFD\n#     31) and food-restricted plus 16 h fast (NCD 28, HFD 23) sessions. The meal-size groups of\n#     Fig. 2f-s sum to 57 NCD and 53 HFD recordings, not 59 and 54. Supp. Fig. 2k by sex: M-NCD 26/3,\n#     M-HFD 31/4, F-NCD 33/4, F-HFD 23/3.\n#   Diet switch (Fig. 3, Supp. Fig. 3): 90-trial sessions, first diet then second diet from ~21\n#     weeks after 6 weeks ad libitum. Legend counts (first/second diet): NCD->NCD 44/43 recordings,\n#     6 mice; NCD->HFD6w 47/36, 6 mice; HFD->NCD 52/42, 7 mice; HFD->HFD 35/23, 4 mice. The Results\n#     give other numbers (HFD->NCD 30 then 42 recordings, NCD 52 then 43, HFD 25 then 23); the\n#     legend counts are used here. The paper does not say whether these mice are those of Fig. 2.\n#   The dandiset (title as the paper; 24 subjects, NWB) is described as holding the fiber\n#   photometry and linked behavioural data of the paper.\n#\n# Shared method definitions, from the Methods unless said otherwise, referred to below.\n#   Triggered trials only; recordings with at least 30 triggered trials unless a claim says\n#   otherwise (Methods). Early meal is the first 15 triggered trials, late meal the last 15;\n#   mid-meal is the 15th to 29th triggered trial (Fig. 2p-s legends).\n#   F0 is the mean of the 10 s before the tone in each trial; dF/F0 = (F - F0)/F0.\n#   Response window (W). The paper gives three: 1-10 s post tone (Methods), 1-9 s post cue\n#   (Fig. 2, Fig. 3 and Supp. Fig. 2-3 legends), 0-10 s post tone (Results, Fig. 1 section). For\n#   Fig. 1 all three are readings; for Fig. 2 and 3 claims the readings are 1-9 s and 1-10 s.\n#   Z-scoring (Z). The Methods say one Z-score per animal from that animal's recordings\n#   concatenated. The paper's code fixes how the per-mouse SD is computed (tcpZ.m), not how it is\n#   applied to trials. Readings: Z1, per trial (F - F0)/sigma, with sigma the tcpZ SD of the\n#   mouse's concatenated, per-recording mean-subtracted filtered fluorescence; Z2, per trial\n#   dF/F0 divided by the SD of the mouse's dF/F0 over all its trial samples concatenated.\n#   A trial's response is the mean Z-scored signal in the window; an early or late value is the\n#   mean over the trials of that phase; a mouse value is the mean of its recordings' values.\n#   Delta Z-score (D). The Methods define it as the mean response of the last 5 triggered trials\n#   minus the first 5 (Figs. 2c, d, 3j); legends describe late minus early meal, and the early\n#   and late meal elsewhere are 15 trials. Readings: D5 (5 trials) and D15 (15 trials).\n#   Statistics in Python with scipy.stats and statsmodels mixedlm (Methods). Alpha 0.05.\n# Tolerances: for a mean with its s.e.m., the s.e.m.; otherwise 10% of the value.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001474\"\npaper: doi:10.1038/s41598-025-19800-2\nclaims:\n- id: fig1k-early-late-recordings\n  statement: Per recording, PVH MC4R consumption responses in NCD mice are small early in the\n    meal (Z 0.12 +- 0.11) and larger late (0.86 +- 0.09); in HFD mice they are already high early\n    (0.72 +- 0.09) and do not increase late (0.79 +- 0.09).\n  source: Results, Feeding-related responses ... elevated early in a meal in HFD-fed animals,\n    paragraph on response magnitude; Figure 1k\n  quote: On average, neural responses were minimal in NCD-fed animals in early trials (Z-score (NCD\n    early) = 0.12 ± 0.11), but exhibited a robust increase in late trials ... (Z-score (NCD late) =\n    0.86 ± 0.09) ... (Z-score (HFD early) = 0.72 ± 0.09), with no further increase observed\n    throughout the meal (Z-score (HFD late) = 0.79 ± 0.09)\n  expected:\n  - quantity: NCD early-meal response, mean over recordings\n    value: 0.12\n    tolerance: 0.11\n    unit: Z-score\n  - quantity: NCD late-meal response, mean over recordings\n    value: 0.86\n    tolerance: 0.09\n    unit: Z-score\n  - quantity: HFD early-meal response, mean over recordings\n    value: 0.72\n    tolerance: 0.09\n    unit: Z-score\n  - quantity: HFD late-meal response, mean over recordings\n    value: 0.79\n    tolerance: 0.09\n    unit: Z-score\n  criterion: Cohort 1, 60-trial sessions with at least 30 triggered trials (39 NCD, 33 HFD).\n    Early and late values per recording as in the opening comment, under each window W (0-10,\n    1-10, 1-9 s) and each Z reading (Z1, Z2). Reproduced when, under one combination, all four\n    means are within tolerance; partially reproduced when no combination puts all four in\n    tolerance but under one the order holds (NCD late above NCD early, HFD early above NCD early,\n    HFD late within 0.2 of HFD early is not used; only the first two orderings are judged). All\n    combinations are shown.\n- id: fig1k-lme\n  statement: In a linear mixed-effects model of recording-level responses with mouse as a random\n    intercept, HFD early-meal responses exceed NCD early-meal responses and the diet by meal-phase\n    interaction is significant.\n  source: Figure 1k legend; Methods, Statistical analysis\n  quote: Linear mixed-effects model (LME), p(NCD early vs. HFD early) < 0.001, p(Diet x Meal phase)\n    < 0.001\n  statistics:\n  - about: HFD against NCD, early meal (diet coefficient, NCD and early meal as reference)\n    test: linear mixed-effects model\n    p: 0.001\n    p_relation: \"<\"\n    n: 39 NCD and 33 HFD recordings, 6 and 5 mice\n  - about: diet x meal phase interaction\n    test: linear mixed-effects model\n    p: 0.001\n    p_relation: \"<\"\n    n: 39 NCD and 33 HFD recordings, 6 and 5 mice\n  depends_on:\n  - fig1k-early-late-recordings\n  criterion: The Methods model, Value ~ Diet * Meal phase + (1 | Mouse), statsmodels mixedlm with\n    its defaults (REML), on two rows per recording (early, late), Diet reference NCD. The\n    Methods say this model was used for \"Fig. 1 i\"; the legend places it on Fig. 1k, the\n    recording-level panel, which is followed. Early meal as the reference level is read from the\n    legend's \"p(NCD early vs. HFD early)\". Reproduced when, under one W and Z combination of\n    fig1k-early-late-recordings, the HFD coefficient is positive with p < 0.001 and the\n    interaction is negative with p < 0.001; partially reproduced when both hold at p < 0.05 only.\n    All combinations are shown.\n- id: fig1l-early-late-mice\n  statement: Per mouse, every NCD mouse increases its response from early to late in the meal\n    (Z 0.19 +- 0.24 to 0.91 +- 0.13), while HFD mice do not change (0.73 +- 0.19 to 0.80 +- 0.20).\n  source: Results, Feeding-related responses ... elevated early in a meal in HFD-fed animals,\n    paragraph on response magnitude; Figure 1l\n  quote: all individual NCD-fed animals exhibited an overall increase in consumption-related neural\n    responses in the late meal phase (Z-score (NCD early) = 0.19 ± 0.24, Z-score (NCD late) = 0.91\n    ± 0.13)) ... This pattern was consistent across all subjects (Z-score (HFD early) = 0.73 ± 0.19,\n    Z-score (HFD late) = 0.80 ± 0.20)\n  expected:\n  - quantity: NCD early-meal response, mean over mice\n    value: 0.19\n    tolerance: 0.24\n    unit: Z-score\n  - quantity: NCD late-meal response, mean over mice\n    value: 0.91\n    tolerance: 0.13\n    unit: Z-score\n  - quantity: HFD early-meal response, mean over mice\n    value: 0.73\n    tolerance: 0.19\n    unit: Z-score\n  - quantity: HFD late-meal response, mean over mice\n    value: 0.80\n    tolerance: 0.20\n    unit: Z-score\n  depends_on:\n  - fig1k-early-late-recordings\n  criterion: Mouse values are the mean of each mouse's recording values (Methods, heatmaps and\n    legend \"by combining the sessions for each mouse\"), under each W and Z reading. The legend's\n    test is a paired, two-tailed t-test between early and late per diet; the p-values are shown\n    only in the figure, not read here. Reproduced when, under one combination, the four means are\n    within tolerance, all 6 NCD mice have late above early, the NCD paired t-test has p < 0.05,\n    and the HFD paired t-test has p >= 0.05; partially reproduced when the tests come out so but\n    a mean is out of tolerance.\n- id: supp1i-hfd-no-change-1-20s\n  statement: With a longer response window of 1 to 20 s after the cue, HFD mice still show no\n    change in response from early to late in the meal.\n  source: Results, Feeding-related responses ... elevated early in a meal in HFD-fed animals,\n    paragraph on response magnitude; Supplementary Figure 1i\n  quote: HFD-fed animals did not show a change in response from early to late in the meal when\n    considering a longer window of 0–20 s post tone\n  depends_on:\n  - fig1k-early-late-recordings\n  criterion: A claim of absence. The Results say 0-20 s and the legend 1-20 s post-cue; both\n    windows are run. Mouse values (6 NCD, 5 HFD mice) under each Z reading; the legend's test, a\n    two-way ANOVA (diet x meal phase) with Tukey HSD across the four diet and phase groups.\n    Reproduced when the Tukey comparison of HFD early against HFD late has p >= 0.05; not\n    reproduced when p < 0.05. The difference is reported either way, as is the NCD early-late\n    comparison.\n- id: supp1h-dff-early-late\n  statement: Expressed as dF/F, HFD mice have stronger consumption responses than NCD mice at the\n    start of the meal, and these persist to the end of the feeding bout.\n  source: Results, Feeding-related responses ... elevated early in a meal in HFD-fed animals,\n    paragraph 4; Supplementary Figure 1h\n  quote: at the start of the meal, HFD-fed animals exhibited stronger feeding-evoked neural\n    responses than NCD-fed animals, and these acute responses persisted until the end of the\n    feeding bout\n  criterion: No test is reported. Per-recording mean dF/F0 in the response window (each W\n    reading), early and late meal, cohort 1. Reproduced when, under one window, the HFD\n    early-meal mean exceeds the NCD early-meal mean and the HFD late-meal mean is at least as\n    high as the HFD early-meal mean minus its s.e.m. over recordings.\n- id: fig1gh-hfd-less-ensure\n  statement: Despite calorie matching, HFD mice consume less Ensure than NCD mice, per recording\n    session and per mouse.\n  source: Results, Feeding-related responses ... elevated early in a meal in HFD-fed animals,\n    paragraph 2; Figure 1g, h\n  quote: Despite calorie matching to ensure comparable acute hunger states (Fig. 1 d), the HFD\n    animals consumed less Ensure volume during the experimental recordings (Fig. 1 g, h)\n  criterion: Cohort 1. Unpaired, two-tailed Student's t-test (equal variances, scipy default), as\n    the legend states, on per-session totals (g) and per-mouse means (h). The volume is the\n    recorded total Ensure consumed (Methods, \"The total consumed Ensure throughout the experiment\n    was noted\"); where it is not available, the number of triggered trials times ~50 uL (Methods)\n    is the reading used, and said. The paper does not say whether sessions with fewer than 30\n    triggered trials are in panel g; both sets are run. Reproduced when the HFD mean is lower with\n    p < 0.05 in both g and h under one session set; partially reproduced when in one of them.\n- id: fig1c-hfd-heavier\n  statement: During food restriction, HFD mice are about 30% heavier than NCD mice.\n  source: Results, Feeding-related responses ... elevated early in a meal in HFD-fed animals,\n    paragraph 2; Figure 1c\n  quote: HFD-fed mice were ~ 30% heavier than the NCD-fed mice\n  expected:\n    quantity: HFD over NCD mean body weight during food restriction, minus 1\n    value: 0.30\n    tolerance: 0.03\n  criterion: Cohort 1 body weights during the recording period. The paper does not say which days\n    or how they are averaged; readings are (a) the mean over recording days per mouse, then over\n    mice; (b) the mean over all recording-day weights pooled. Reproduced when one reading is\n    within tolerance; partially reproduced when HFD is heavier by 20% to 40%.\n- id: supp1cd-licking-declines\n  statement: Both NCD and HFD mice reduce their licking from the early to the late phase of the\n    session.\n  source: Results, Feeding-related responses ... elevated early in a meal in HFD-fed animals,\n    paragraph 2; Supplementary Figure 1c, d\n  quote: Both NCD- and HFD-fed animals steadily reduced their licking rates from early to late\n    phases of the session\n  criterion: Supp. Fig. 1d measure, per mouse, the area under the post-cue lick-rate curve\n    normalized to the pre-tone baseline lick rate, early against late meal. Open details, each run\n    as a reading. Normalization is (a) subtraction of or (b) division by the mean lick rate of the\n    10 s before the tone; the AUC window is (i) 1-10 s post tone (the Methods' reward-window lick\n    rate) or (ii) 0-50 s (the whole post-cue trace); the test is (x) unpaired two-tailed t-test\n    (Supp. Fig. 1d legend) or (y) paired two-tailed t-test (Methods list Supp. Fig. 1d under\n    paired tests). Reproduced when all readings give late below early with p < 0.05 in both diets;\n    partially reproduced when that holds in one diet under all readings; blocked as\n    methods_underspecified when readings disagree.\n- id: supp1e-hfd-less-locomotion\n  statement: Food-seeking locomotion is negligible in HFD mice compared with NCD mice, and falls\n    further near the end of the meal.\n  source: Results, Feeding-related responses ... elevated early in a meal in HFD-fed animals,\n    paragraph 2; Supplementary Figure 1e\n  quote: Compared to NCD-fed animals, food-seeking-related locomotion was negligible in HFD-fed\n    animals ... and it was further reduced to a minimum level late near the end of the meal\n  criterion: No test is reported. Per mouse mean running speed over triggered trials (whole\n    60-s trial), early and late meal, cohort 1. Reproduced when the HFD mean over mice is below\n    the NCD mean in both phases and the HFD late mean is below the HFD early mean. Per-mouse\n    values are shown.\n- id: fig2b-meal-size\n  statement: In 90-trial sessions NCD mice consume Ensure in 70.1 +- 2.1 trials and HFD mice in\n    52.9 +- 1.98 trials.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 1; Figure 2b\n  quote: NCD-fed mice consumed Ensure during 70.1 ± 2.1 out of 90 possible trials, whereas HFD-fed\n    animals only consumed Ensure during 52.9 ± 1.98 out of 90 trials\n  statistics:\n  - test: unpaired, two-tailed Student's t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 59 NCD and 54 HFD recordings\n  expected:\n  - quantity: NCD triggered trials per session\n    value: 70.1\n    tolerance: 2.1\n  - quantity: HFD triggered trials per session\n    value: 52.9\n    tolerance: 1.98\n  criterion: Cohort 2, 90-trial sessions, mean over recordings. The paper's p is shown only as\n    asterisks in the figure; the statistics entry records the paper's alpha for a reported\n    difference. Sessions included are open; readings are (a) all 90-trial sessions, (b) those with\n    at least 30 triggered trials (the Methods default, and 59/54 is the count of Fig. 2a-e),\n    (c) those with at least 15 (Fig. 2f-s). Reproduced when, under one reading, both means are\n    within tolerance and the Student's t-test gives p < 0.05.\n- id: fig2c-delta-z-recordings\n  statement: Per recording, the change in response from early to late in the meal is 0.52 +- 0.09\n    in NCD mice and only 0.12 +- 0.08 in HFD mice.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 1; Figure 2c\n  quote: in NCD-fed animals, excitatory responses increased over the meal, with a positive mean\n    change in Z-score (ΔZ-score) between early and late in the meal of 0.52 ± 0.09. However, in\n    HFD-fed animals, the increase was minimal (ΔZ-score = 0.12 ± 0.08; Fig. 2 c)\n  expected:\n  - quantity: NCD delta Z-score, mean over recordings\n    value: 0.52\n    tolerance: 0.09\n  - quantity: HFD delta Z-score, mean over recordings\n    value: 0.12\n    tolerance: 0.08\n  criterion: Cohort 2, recordings with at least 30 triggered trials (59 NCD, 54 HFD). Delta\n    Z-score under D5 and D15, each W (1-9, 1-10 s) and Z reading. The legend's test is an\n    unpaired two-tailed Student's t-test. Reproduced when, under one combination, both means are\n    within tolerance and the t-test gives NCD above HFD with p < 0.05; partially reproduced when\n    the t-test holds but a mean is out of tolerance. All combinations are shown.\n- id: fig2d-delta-z-mice\n  statement: Per mouse, the early-to-late change in response is 0.56 +- 0.10 in NCD mice and\n    0.28 +- 0.09 in HFD mice.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 1; Figure 2d\n  quote: Similar results were observed across individual animals (ΔZ-score\n  inferred: The numbers follow the quoted words in the same sentence, \"NCD = 0.56 ± 0.10, HFD = 0.28\n    ± 0.09\", which are not quoted whole because the sentence contains a colon.\n  expected:\n  - quantity: NCD delta Z-score, mean over mice\n    value: 0.56\n    tolerance: 0.10\n  - quantity: HFD delta Z-score, mean over mice\n    value: 0.28\n    tolerance: 0.09\n  depends_on:\n  - fig2c-delta-z-recordings\n  criterion: As fig2c-delta-z-recordings, with each mouse's value the mean of its recordings' delta\n    Z-scores (legend, \"averaged across sessions\"), 7 NCD and 7 HFD mice, unpaired two-tailed\n    Student's t-test. Reproduced when, under one combination, both means are within tolerance and\n    NCD is above HFD with p < 0.05; partially reproduced when the means hold and the test does not.\n- id: fig2e-lick-vigor\n  statement: Throughout the 90-trial meal NCD mice lick at a higher rate during the cue than HFD\n    mice; NCD licking begins to decline after about 50 trials and HFD licking after about 20.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 2; Figure 2e\n  quote: Throughout the meal, NCD-fed animals exhibited higher licking vigor than HFD-fed animals\n    (Fig. 2 e). In NCD-fed animals, licking vigor began to decline steadily after ~ 50 trials ...\n    in HFD-fed animals, licking vigor began to decline much earlier, after only ~ 20 trials\n  expected:\n  - quantity: trial at which NCD cue lick rate starts to decline\n    value: 50\n    tolerance: 5\n  - quantity: trial at which HFD cue lick rate starts to decline\n    value: 20\n    tolerance: 2\n  criterion: Cue lick rate is licks per second in the 0-1 s tone window (Methods), triggered trials\n    only, per trial index 1 to 90, averaged across mice (legend) of recording means, cohort 2\n    recordings with at least 30 triggered trials. \"Throughout\" has two readings, NCD above HFD (a)\n    at every trial index both groups have data or (b) in every 15-trial block. Onset of decline\n    is not defined; readings are (i) the trial index of the maximum of the curve smoothed with a\n    15-trial moving mean, (ii) the first trial after which the 15-trial moving mean stays below\n    the mean of the first 15 trials. Reproduced when NCD is higher under one reading and both\n    onsets are within tolerance under one reading; partially reproduced when NCD is higher and the\n    NCD onset is later than the HFD onset but the onsets are out of tolerance.\n- id: fig2fj-early-lick-by-meal-size\n  statement: Sessions with smaller meals have lower lick rates early in the meal; initial cue lick\n    rates span 4 to 5.5 licks/s across NCD meal-size groups and 2 to 5.7 licks/s across HFD groups.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 3; Figure 2f-j, p\n  quote: Sessions with smaller meal sizes (fewer total triggered trials and lower caloric intake)\n    exhibited lower lick rates early in the meal (i.e., the initial lick rate during the cue was\n    4–5.5 licks/s for NCD mice versus 2–5.7 licks/s for HFD mice)\n  expected:\n  - quantity: lowest NCD meal-size group initial cue lick rate\n    value: 4.0\n    tolerance: 0.4\n    unit: licks/s\n  - quantity: highest NCD meal-size group initial cue lick rate\n    value: 5.5\n    tolerance: 0.55\n    unit: licks/s\n  - quantity: lowest HFD meal-size group initial cue lick rate\n    value: 2.0\n    tolerance: 0.2\n    unit: licks/s\n  - quantity: highest HFD meal-size group initial cue lick rate\n    value: 5.7\n    tolerance: 0.57\n    unit: licks/s\n  criterion: Cohort 2 sessions with at least 15 triggered trials, grouped by triggered trials\n    (15-29, 30-44, 45-59, 60-74, 75-90). \"Initial lick rate\" is open; readings are (a) the group\n    mean cue lick rate of the first triggered trial, (b) of the first 15 triggered trials.\n    Reproduced when, under one reading, each group-range bound is within tolerance and the group\n    means rise with meal size in each diet (a Spearman correlation of group mean with group order\n    of +1 is not required; the smallest group is below the largest).\n- id: fig2p-lick-rate-meal-size\n  statement: The mid-meal cue lick rate correlates positively with meal size in both NCD and HFD\n    sessions.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 6; Figure 2p\n  quote: lick rate early in the meal positively correlated with the number of trials triggered in\n    the session for both diet groups (Fig. 2 p)\n  criterion: Pearson correlation (legend) per diet over recordings with at least 15 triggered\n    trials, of meal size (triggered trials) with the cue lick rate averaged over the 15th to 29th\n    triggered trial (legend); the Results' \"early in the meal\" (first 15 triggered trials) is a\n    reading too. Reproduced when, under one reading, r > 0 with p < 0.05 in both diets; partially\n    reproduced in one.\n- id: fig2km-elevated-early-at-matched-licking\n  statement: In sessions of 45 to 74 triggered trials, where early licking vigor is comparable\n    between groups, HFD mice still have larger PVH MC4R responses early in the meal than NCD mice.\n  source: Results, HFD alters neural and behavioral responses ..., paragraphs 4 and 5; Figure 2g, h,\n    l, m\n  quote: Critically, despite both HFD- and NCD-fed mice having similar licking vigor early during a\n    session (e.g., Fig. 2 h), HFD-fed mice still showed elevated PVH MC4R responses in the early\n    trials (e.g., Fig. 2 m)\n  criterion: No test is reported. Within the 45-59 and 60-74 meal-size groups, the mean over\n    recordings of the early-meal response (first 15 triggered trials, each W and Z reading) and of\n    the early-meal cue lick rate. Reproduced when, under one combination, in both groups the HFD\n    early response mean exceeds the NCD mean by more than the sum of their s.e.m.s while the HFD\n    and NCD early lick-rate means differ by less than the sum of their s.e.m.s; partially\n    reproduced when that holds in one group.\n- id: fig2q-midmeal-response-meal-size\n  statement: In HFD sessions, mid-meal PVH MC4R responses correlate negatively with meal size (r =\n    -0.46, p = 0.001).\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 6; Figure 2q\n  quote: the PVH MC4R responses in HFD-fed animals negatively correlated with meal size (HFD\n    r = − 0.46, p = 0.001)\n  statistics:\n  - test: Pearson correlation\n    statistic: r = -0.46\n    p: 0.001\n    n: HFD recordings with at least 15 triggered trials\n  expected:\n    quantity: Pearson r, HFD mid-meal response against triggered trials\n    value: -0.46\n    tolerance: 0.046\n  criterion: Mid-meal response is the mean response over the 15th to 29th triggered trial (legend),\n    each W and Z reading; recordings with at least 15 triggered trials (Results, \"in sessions with\n    at least 15 triggered trials\"), and with at least 30 as a reading (Methods default). Reproduced\n    when, under one combination, r is within tolerance and p < 0.05; partially reproduced when r <\n    0 with p < 0.05 but out of tolerance. The NCD correlation is reported.\n- id: fig2r-weight-midmeal-response\n  statement: In HFD mice, absolute body weight on the recording day correlates positively with\n    mid-meal Z-scored responses.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 7; Figure 2r\n  quote: We found that absolute body weight positively correlated with mid-meal Z-scored MC4R\n    activity for HFD mice, indicating that heavier HFD mice exhibit stronger neuronal activation\n    during the meal (Fig. 2 r)\n  depends_on:\n  - fig2q-midmeal-response-meal-size\n  criterion: Pearson correlation (legend) over HFD recordings of the recording-day body weight with\n    the mid-meal response, under the readings of fig2q-midmeal-response-meal-size. Reproduced when,\n    under one reading, r > 0 with p < 0.05; partially reproduced when r > 0 and p >= 0.05.\n- id: fig2s-weight-meal-length\n  statement: In HFD mice, meal length (triggered trials) correlates negatively with absolute body\n    weight.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 7; Figure 2s\n  quote: meal length (i.e. the number of triggered trials) correlated negatively with absolute body\n    weight in HFD-fed animals (Fig. 2 s)\n  criterion: Pearson correlation (legend) over HFD recordings, with at least 15 and, as a reading,\n    at least 30 triggered trials. Reproduced when, under one reading, r < 0 with p < 0.05;\n    partially reproduced when r < 0 and p >= 0.05.\n- id: supp2a-volume-trials\n  statement: Ensure volume consumed correlates robustly with the number of triggered trials in both\n    diet groups, so meal size is defined as triggered trials.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 1; Supplementary\n    Figure 2a\n  quote: there was a robust correlation between volume of Ensure consumed and number of triggered\n    trials for both NCD- and HFD-fed animals\n  criterion: No test is named; Pearson correlation, the paper's test for its other meal-size\n    correlations (Fig. 2p-s), per diet over cohort 2 recordings with a recorded Ensure volume.\n    Reproduced when r > 0 with p < 0.05 in both diets.\n- id: supp2h-delta-z-meal-size\n  statement: Across sessions, the within-meal change in response correlates with meal size with r =\n    -0.34 (p = 0.012) in NCD mice and r = 0.26 (p = 0.048) in HFD mice. The sentence calls the NCD\n    correlation positive and the HFD one negative, opposite to the printed signs.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 9; Supplementary\n    Figure 2h\n  quote: This analysis revealed a positive correlation in the NCD-fed group and a negative\n    correlation in the HFD-fed group (NCD\n  inferred: The quote breaks at a colon; the sentence goes on \"r = − 0.34, p = 0.012, HFD r = 0.26,\n    p = 0.048\". The words and the printed signs disagree, so the statement records both.\n  statistics:\n  - about: NCD\n    test: Pearson correlation\n    statistic: r = -0.34\n    p: 0.012\n  - about: HFD\n    test: Pearson correlation\n    statistic: r = 0.26\n    p: 0.048\n  expected:\n  - quantity: Pearson r, NCD delta Z-score against triggered trials\n    value: -0.34\n    tolerance: 0.034\n  - quantity: Pearson r, HFD delta Z-score against triggered trials\n    value: 0.26\n    tolerance: 0.026\n  criterion: Per diet over cohort 2 recordings, Pearson correlation of triggered trials with the\n    delta Z-score, read as the legend's late-meal minus early-meal mean (D15) and as the Methods'\n    D5, each W and Z reading. Reproduced when, under one combination, both r are within tolerance\n    with p < 0.05. If instead the signs come out as the sentence's words (NCD positive, HFD\n    negative, both p < 0.05), partially reproduced, noting that the words and numbers disagree.\n- id: supp2fg-locomotion-not-meal-size\n  statement: HFD mice show reduced locomotion, but locomotion does not correlate with meal size.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 8; Supplementary\n    Figure 2f, g\n  quote: Although HFD-fed animals exhibited reduced locomotion, this did not correlate with meal\n    size (Supplementary Fig. 2f, g)\n  criterion: The paper names no test for either part. Locomotion is the mean running speed in the\n    pre-cue period (Supp. Fig. 2g legend) over triggered trials, per recording. Reduced\n    locomotion holds when the HFD mean over recordings is below the NCD mean. The absence of a\n    correlation is judged with Pearson correlation of triggered trials against locomotion per\n    diet (the paper's test for its other meal-size correlations, a choice recorded as a\n    deviation); reproduced when p >= 0.05 in both diets and HFD locomotion is lower; not\n    reproduced when either correlation has p < 0.05. Locomotion after reward (1-10 s) is shown as\n    a variant.\n- id: supp2j-variability-weight\n  statement: Pre-Ensure spontaneous signal variability correlates weakly with absolute body weight\n    in HFD mice.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 10; Supplementary\n    Figure 2i, j\n  quote: Our analysis revealed a weak correlation when assessing absolute body weight for HFD-fed\n    animals (Supplementary Fig. 2 j)\n  criterion: Variability is a rolling standard deviation of dF/F0 in the period before the first\n    Ensure delivery, averaged per recording; the rolling window length and the F0 for this\n    continuous trace are not given anywhere. Readings for the window are 1 s, 10 s and 60 s, and\n    F0 is the mean of the pre-Ensure period. Pearson correlation over HFD recordings with\n    recording-day body weight. Reproduced when all readings give p < 0.05 with |r| below 0.5 (the\n    paper's \"weak\"); blocked as methods_underspecified when readings disagree.\n- id: supp2k-sex-early-response\n  statement: NCD females show slightly larger early-meal responses than males, a difference more\n    pronounced in HFD mice.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 11; Supplementary\n    Figure 2k\n  quote: NCD-fed females exhibited slightly larger neural responses than males early in the meal—a\n    trend that was even more pronounced in HFD-fed animals\n  criterion: No test is reported. Mean over recordings of the early-meal response (first 15\n    triggered trials) for M-NCD, F-NCD, M-HFD, F-HFD (26, 33, 31, 23 recordings), each W and Z\n    reading. Reproduced when, under one combination, F exceeds M in both diets and the F minus M\n    difference is larger in HFD than in NCD.\n- id: supp2lp-fasting-no-effect\n  statement: An additional overnight fast does not significantly alter licking or PVH MC4R\n    response dynamics in either diet group.\n  source: Results, HFD alters neural and behavioral responses ..., paragraph 12; Supplementary\n    Figure 2l-p\n  quote: However, additional fasting did not significantly alter licking or PVH MC4R response\n    dynamics for either group (Supplementary Fig. 2l–p)\n  criterion: A claim of absence for which the paper names no test. Fasted against nonfasted\n    recordings within each diet (NCD 28 and 31, HFD 23 and 31), on the mean cue lick rate over\n    triggered trials, the early-meal response and the delta Z-score (D15), each W and Z reading.\n    Readings for the test are (a) an unpaired two-tailed Student's t-test on recordings, the\n    paper's test for recording comparisons in Fig. 2b-c, and (b) a linear mixed-effects model,\n    measure ~ fasting + (1 | Mouse), the paper's model for repeated sessions. Reproduced when every\n    reading gives p >= 0.05 for every measure in both diets; not reproduced when every reading\n    finds some effect at p < 0.05; blocked as methods_underspecified when they disagree. Effect\n    sizes are reported.\n- id: supp2q-hfd-more-training\n  statement: HFD mice needed more training sessions than NCD mice to reach stable task performance.\n  source: Methods, Behavioral training on wheels; Supplementary Figure 2q\n  quote: Although HFD mice required more sessions to reach stable task performance (Supplementary\n    Fig. 2q)\n  criterion: Unpaired two-tailed Student's t-test (Methods, statistical analysis, item 3) on the\n    number of training sessions per mouse. Reproduced when HFD is higher with p < 0.05. Testable\n    only if training sessions are in the dataset.\n- id: fig3h-early-response-diet-switch\n  statement: After switching from HFD to NCD, early-meal PVH MC4R responses fall from their level on\n    HFD toward NCD levels, while HFD->HFD mice keep high early-meal responses.\n  source: Results, Effects of diet switching ..., paragraphs 2 and 5; Figure 3h\n  quote: PVH MC4R neuron responses remained attenuated relative to prior responses while on HFD for\n    most of the experiment (Fig. 3 f, h)\n  criterion: Early-meal response per recording (first 15 triggered trials, W 1-9 and 1-10 s, each\n    Z reading), recordings with at least 30 triggered trials, six groups (NCD->NCD, HFD->NCD,\n    HFD->HFD, each before and after the switch). The legend's test, a two-way ANOVA (condition x\n    phase) with Tukey HSD across the six groups. Reproduced when, under one combination, HFD->NCD\n    after is below HFD->NCD before with Tukey p < 0.05 and HFD->HFD after is not below HFD->HFD\n    before at p < 0.05; partially reproduced when HFD->NCD after is lower but not significantly.\n    The before-switch HFD groups against NCD->NCD are reported.\n- id: fig3i-ncd-increase-only\n  statement: After the diet switch, NCD->NCD mice show a significant increase in response from\n    early to late in the meal, while HFD->NCD mice show only a slight, nonsignificant increase.\n  source: Results, Effects of diet switching ..., paragraph 4; Figure 3i; Supplementary Figure 3i\n  quote: The HFD → NCD group displayed an intermediate pattern between the HFD → HFD and NCD → NCD\n    groups, with a slight but nonsignificant increase in PVH MC4R responses across the meal\n  statistics:\n  - about: NCD->NCD early against late, after the switch\n    test: linear mixed-effects model; paired, two-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Second-diet recordings. Two tests the paper names, both run. (1) The Fig. 3i LME,\n    Value ~ C(Condition, Treatment('NCD|NCD')) * Meal phase + (1 | Mouse) on two rows per\n    recording; within-group early-late effects are the meal-phase coefficient with each group in\n    turn as reference. (2) The Supp. Fig. 3i paired two-tailed t-test on mouse means. The NCD->NCD\n    increase is reproduced when both give late above early with p < 0.05 under one W and Z\n    combination. The HFD->NCD part is a claim of absence, judged on these two tests; reproduced when\n    neither finds p < 0.05 and the late mean is above the early mean, not reproduced when both do,\n    and blocked as methods_underspecified when they disagree. HFD->HFD is reported.\n- id: fig3j-delta-z-diet-switch\n  statement: After the switch, the per-mouse early-to-late change in response is 0.37 +- 0.03 in\n    NCD->NCD, 0.14 +- 0.05 in HFD->NCD and -0.05 +- 0.07 in HFD->HFD mice; it is significantly smaller\n    in HFD->HFD.\n  source: Results, Effects of diet switching ..., paragraph 4; Figure 3j\n  quote: we observed a significantly smaller increase in neural responses across trials in the HFD →\n    HFD group ... six weeks of NCD exposure in formerly HFD-fed animals failed to fully restore this\n    effect to NCD levels (ΔZ-score\n  inferred: The values follow the quote's last words, \"NCD → NCD = 0.37 ± 0.03, HFD → NCD = 0.14 ±\n    0.05, HFD → HFD = − 0.05 ± 0.07\", after a colon.\n  statistics:\n  - about: HFD->HFD against NCD->NCD\n    test: one-way ANOVA with Tukey HSD post hoc test\n    p: 0.05\n    p_relation: \"<\"\n    n: 6, 7 and 4 mice\n  expected:\n  - quantity: NCD->NCD delta Z-score, mean over mice\n    value: 0.37\n    tolerance: 0.03\n  - quantity: HFD->NCD delta Z-score, mean over mice\n    value: 0.14\n    tolerance: 0.05\n  - quantity: HFD->HFD delta Z-score, mean over mice\n    value: -0.05\n    tolerance: 0.07\n  criterion: Second-diet recordings with at least 30 triggered trials; mouse values are means of\n    recording delta Z-scores, D5 (the Methods name Fig. 3j) and D15, each W and Z reading.\n    One-way ANOVA with Tukey HSD (legend). Reproduced when, under one combination, the three means\n    are within tolerance and HFD->HFD is below NCD->NCD with Tukey p < 0.05; partially reproduced\n    when the order NCD->NCD > HFD->NCD > HFD->HFD holds and the Tukey test does, with means out of\n    tolerance.\n- id: fig3k-ensure-after-switch\n  statement: After the switch, HFD->NCD mice consume as much Ensure per session as NCD->NCD mice\n    and significantly more than HFD->HFD mice.\n  source: Results, Effects of diet switching ..., paragraph 4; Figure 3k\n  quote: the HFD → NCD group consumed a volume of Ensure comparable to the NCD → NCD group and\n    significantly higher than the HFD → HFD group during individual recording sessions (Fig. 3 k)\n  statistics:\n  - about: HFD->NCD against HFD->HFD, after the switch\n    test: two-way ANOVA with Tukey HSD post hoc test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Ensure volume per recording (recorded total; triggered trials times ~50 uL as a\n    reading where the total is absent), six groups (three conditions before and after), two-way\n    ANOVA (condition x phase) with Tukey HSD (legend). Whether recordings with fewer than 30\n    triggered trials are included is open; both sets are run. Reproduced when, under one set,\n    HFD->NCD after exceeds HFD->HFD after with p < 0.05 and the Tukey test of HFD->NCD after\n    against NCD->NCD after gives p >= 0.05; partially reproduced when only the first holds.\n- id: fig3-hfd-hfd-short-meals\n  statement: In the second diet phase, HFD->HFD mice stop consuming Ensure early, never exceeding\n    60 triggered trials.\n  source: Results, Effects of diet switching ..., paragraph 2; Figure 3d, g\n  quote: The HFD → HFD group maintained high early-meal PVH MC4R responses (Fig. 3 d, g, h) and\n    ceased to engage in Ensure consumption even earlier in the session, never exceeding 60\n    triggered trials\n  expected:\n    quantity: maximum triggered trials in a second-phase HFD->HFD session\n    value: 60\n    tolerance: 0\n  criterion: Over all second-phase HFD->HFD 90-trial recordings. Reproduced when no session has more\n    than 60 triggered trials; partially reproduced when no more than one of the 23 sessions does.\n- id: fig3c-hfd-ncd-licking-recovers\n  statement: After at least six weeks on NCD, formerly HFD mice lick with more vigor during the cue,\n    a reinstated motivation to consume food.\n  source: Results, Effects of diet switching ..., paragraph 2; Figure 3c; Supplementary Figure 3f\n  quote: After at least six weeks on NCD, these same animals displayed an increase in licking vigor\n    during cue presentation (Fig. 3 c (bottom right panel), Supplementary Fig. 3f)\n  criterion: No test is reported. Cue lick rate (0-1 s) over triggered trials per trial index,\n    averaged across HFD->NCD recordings with at least 30 triggered trials (Supp. Fig. 3f legend),\n    before against after the switch. Reproduced when the after curve's mean over trials 1-90 (each\n    trial index weighted equally, indices with data in both phases) is above the before curve's\n    and the mean over recordings of each recording's mean cue lick rate is higher after as well.\n- id: supp3c-ncd-hfd6w-dynamics-retained\n  statement: NCD mice switched to HFD for 6 weeks keep their response dynamics, with a significant\n    early-to-late increase in response both before and after the switch, and stable licking vigor.\n  source: Results, Effects of diet switching ..., paragraphs 3 and 4; Supplementary Figure 3a-d, h\n  quote: the NCD → HFD 6w group retained their response properties, exhibiting comparable changes in\n    response magnitude before (NCD) and after the diet switch (HFD 6w ) between early and late meal\n    stages, despite a significant weight gain after the diet switch\n  statistics:\n  - about: NCD->HFD6w early against late, second diet phase\n    test: paired, two-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 6 mice\n  criterion: Supp. Fig. 3c (1-9 s) and 3d (1-19 s) windows, each Z reading; mouse means of early\n    and late meal responses, paired two-tailed t-test (legend), in the NCD phase and the HFD6w\n    phase. Reproduced when late exceeds early with p < 0.05 in both phases under one Z reading in\n    the 1-9 s window; partially reproduced when in the HFD6w phase only. Licking stability is\n    reported as the mean cue lick rate per phase, not judged.\n- id: supp3j-body-weight-switch\n  statement: NCD->HFD6w mice gain significant body weight over the 6-week HFD phase, while HFD->NCD\n    mice do not lose weight (a slight, nonsignificant gain).\n  source: Results, Effects of diet switching ..., paragraphs 3, 4 and 7; Supplementary Figure 3j\n  quote: these animals showed a significant increase in body weight during the 6-week HFD phase\n    (Supplementary Fig. 3j)\n  statistics:\n  - about: NCD->HFD6w, before against after\n    test: linear mixed-effects model\n    p: 0.05\n    p_relation: \"<\"\n  criterion: The Methods model, per condition, body weight ~ phase + (1 | Mouse) on recording-day\n    weights, statsmodels mixedlm. Reproduced when the NCD->HFD6w phase effect is positive with p <\n    0.05 and the HFD->NCD phase effect has p >= 0.05 and is not negative with p < 0.05 (absence,\n    judged on this model); partially reproduced when only the first holds.\n- id: supp3m-weight-gain-response\n  statement: In the second diet phase, mid-meal responses correlate positively with weight gain in\n    NCD->HFD6w mice (r = 0.53, p = 0.001) and also in NCD->NCD mice (r = 0.46, p = 0.003).\n  source: Results, Effects of diet switching ..., paragraph 6; Supplementary Figure 3m (text) or 3n\n    (legend)\n  quote: we observed a strong positive correlation (r = 0.53, p = 0.001) between mid-meal neural\n    responses and the diet-induced weight gain in the NCD → HFD 6w group during the second diet\n    phase ... we also observed a positive correlation in the NCD → NCD group (r = 0.46, p = 0.003)\n  statistics:\n  - about: NCD->HFD6w\n    test: Pearson correlation\n    statistic: r = 0.53\n    p: 0.001\n  - about: NCD->NCD\n    test: Pearson correlation\n    statistic: r = 0.46\n    p: 0.003\n  expected:\n  - quantity: Pearson r, NCD->HFD6w\n    value: 0.53\n    tolerance: 0.053\n  - quantity: Pearson r, NCD->NCD\n    value: 0.46\n    tolerance: 0.046\n  criterion: Per second-phase recording, mid-meal response (15th-29th triggered trial, each W and Z\n    reading) against weight on the recording day (C) relative to weight at the start of ad\n    libitum feeding (A), as the Supp. Fig. 3n legend defines it (the text cites panel m, whose\n    legend is meal size). \"Relative to\" is read as C - A and as C / A. Reproduced when, under one\n    combination, both r are within tolerance with p < 0.05; partially reproduced when both are\n    positive with p < 0.05.\n- id: supp3l-weight-not-meal-length\n  statement: In the second diet phase, absolute body weight does not predict meal length in\n    NCD->NCD or NCD->HFD6w mice.\n  source: Results, Effects of diet switching ..., paragraph 6; Supplementary Figure 3l\n  quote: absolute body weight does not predict meal length in animals exposed to NCD or HFD 6w\n    during the second meal phase (Supplementary Fig. 3l)\n  criterion: A claim of absence; the test is Pearson correlation, read from the linear fits of the\n    legend and the paper's correlations in this section. Per group, second-phase recordings,\n    triggered trials against recording-day body weight. Reproduced when p >= 0.05 in both groups;\n    not reproduced when either has p < 0.05.\n- id: supp3q-hfd-ncd-weight-loss-meal-length\n  statement: In HFD->NCD mice, meal length correlates negatively with weight change, so mice that\n    lost more weight before the session tended to eat larger meals; neural responses do not\n    correlate with weight change.\n  source: Results, Effects of diet switching ..., paragraph 7; Supplementary Figure 3p, q\n  quote: In the HFD → NCD group, we observed no correlation with neural responses (Supplementary\n    Fig. 3j, p), but a significant negative correlation between meal length and weight change,\n    indicating that animals that lost more weight before the session tended to have larger meals\n  statistics:\n  - about: meal length against weight change, HFD->NCD\n    test: Pearson correlation\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Second-phase HFD->NCD recordings. Weight change is open; the text gives body weight\n    relative to (a) the maximum ad libitum weight or (b) the weight before HFD exposure, and the\n    legend relative to the start of ad libitum feeding (A); each as a difference and as a ratio.\n    Pearson correlation of triggered trials with weight change, and of mid-meal response with\n    weight change. Reproduced when, under one reading, the first has r < 0 with p < 0.05 and the\n    second has p >= 0.05; partially reproduced when only the first holds.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001474 && python3 - <<'EOF'
p='10.1038-s41598-025-19800-2.yaml'
s=open(p).read()
rep=[
("""  quote: Similar results were observed across individual animals (ΔZ-score
  inferred: The numbers follow the quoted words in the same sentence, "NCD = 0.56 ± 0.10, HFD = 0.28
    ± 0.09", which are not quoted whole because the sentence contains a colon.
""","""  quote: >-
    Similar results were observed across individual animals (ΔZ-score: NCD = 0.56 ± 0.10, HFD =
    0.28 ± 0.09) (Fig. 2 d)
"""),
("""  quote: This analysis revealed a positive correlation in the NCD-fed group and a negative
    correlation in the HFD-fed group (NCD
  inferred: The quote breaks at a colon; the sentence goes on "r = − 0.34, p = 0.012, HFD r = 0.26,
    p = 0.048". The words and the printed signs disagree, so the statement records both.
""","""  quote: >-
    This analysis revealed a positive correlation in the NCD-fed group and a negative correlation
    in the HFD-fed group (NCD: r = − 0.34, p = 0.012, HFD: r = 0.26, p = 0.048)
"""),
("""  quote: we observed a significantly smaller increase in neural responses across trials in the HFD →
    HFD group ... six weeks of NCD exposure in formerly HFD-fed animals failed to fully restore this
    effect to NCD levels (ΔZ-score
  inferred: The values follow the quote's last words, "NCD → NCD = 0.37 ± 0.03, HFD → NCD = 0.14 ±
    0.05, HFD → HFD = − 0.05 ± 0.07", after a colon.
""","""  quote: >-
    we observed a significantly smaller increase in neural responses across trials in the HFD → HFD
    group ... six weeks of NCD exposure in formerly HFD-fed animals failed to fully restore this
    effect to NCD levels (ΔZ-score: NCD → NCD = 0.37 ± 0.03, HFD → NCD = 0.14 ± 0.05, HFD → HFD =
    − 0.05 ± 0.07)
"""),
("""    tolerance; partially reproduced when no combination puts all four in
    tolerance but under one the order holds (NCD late above NCD early, HFD early above NCD early,
    HFD late within 0.2 of HFD early is not used; only the first two orderings are judged). All
    combinations are shown.""","""    tolerance; partially reproduced when no combination puts all four in
    tolerance but under one NCD late is above NCD early and HFD early is above NCD early. All
    combinations are shown."""),
("""    Reproduced when, under one reading, each group-range bound is within tolerance and the group
    means rise with meal size in each diet (a Spearman correlation of group mean with group order
    of +1 is not required; the smallest group is below the largest).""","""    Reproduced when, under one reading, the lowest and highest group means of each diet are within
    tolerance of the reported bounds and, in each diet, the smallest meal-size group has a lower
    mean than the largest."""),
]
for a,b in rep:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
cd ../..; python tools/claims_check.py claims/001474/10.1038-s41598-025-19800-2.yaml paper/10.1038-s41598-025-19800-2.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001474 && python3 - <<'EOF'
p='10.1038-s41598-025-19800-2.yaml'
s=open(p).read()
import re
def sub(a,b):
    global s
    assert a in s, a[:70]
    s=s.replace(a,b)
sub("""  quote: Similar results were observed across individual animals (ΔZ-score
  inferred: The numbers follow the quoted words in the same sentence, "NCD = 0.56 ± 0.10, HFD = 0.28
    ± 0.09", which are not quoted whole because the sentence contains a colon.
""","""  quote: >-
    Similar results were observed across individual animals (ΔZ-score: NCD = 0.56 ± 0.10, HFD =
    0.28 ± 0.09) (Fig. 2 d)
""")
sub("""  quote: This analysis revealed a positive correlation in the NCD-fed group and a negative
    correlation in the HFD-fed group (NCD
  inferred: The quote breaks at a colon; the sentence goes on "r = − 0.34, p = 0.012, HFD r = 0.26,
    p = 0.048". The words and the printed signs disagree, so the statement records both.
""","""  quote: >-
    This analysis revealed a positive correlation in the NCD-fed group and a negative correlation
    in the HFD-fed group (NCD: r = − 0.34, p = 0.012, HFD: r = 0.26, p = 0.048)
""")
sub("""  quote: we observed a significantly smaller increase in neural responses across trials in the HFD →
    HFD group ... six weeks of NCD exposure in formerly HFD-fed animals failed to fully restore this
    effect to NCD levels (ΔZ-score
  inferred: The values follow the quote's last words, "NCD → NCD = 0.37 ± 0.03, HFD → NCD = 0.14 ±
    0.05, HFD → HFD = − 0.05 ± 0.07", after a colon.
""","""  quote: >-
    we observed a significantly smaller increase in neural responses across trials in the HFD → HFD
    group ... six weeks of NCD exposure in formerly HFD-fed animals failed to fully restore this
    effect to NCD levels (ΔZ-score: NCD → NCD = 0.37 ± 0.03, HFD → NCD = 0.14 ± 0.05, HFD → HFD =
    − 0.05 ± 0.07)
""")
sub("""  quote: the PVH MC4R responses in HFD-fed animals negatively correlated with meal size (HFD
    r = − 0.46, p = 0.001)""","""  quote: >-
    the PVH MC4R responses in HFD-fed animals negatively correlated with meal size (HFD: r = − 0.46,
    p = 0.001)""")
sub("After at least six weeks on NCD, these same","After at least six subsequent weeks on NCD, these same")
s=re.sub(r"tolerance; partially reproduced when no combination puts all four in\n    tolerance but under one the order holds.*?All\n    combinations are shown\.",
 "tolerance; partially reproduced when no combination puts all four in\n    tolerance but under one NCD late is above NCD early and HFD early is above NCD early. All\n    combinations are shown.", s, flags=re.S)
sub("""    Reproduced when, under one reading, each group-range bound is within tolerance and the group
    means rise with meal size in each diet (a Spearman correlation of group mean with group order
    of +1 is not required; the smallest group is below the largest).""","""    Reproduced when, under one reading, the lowest and highest group means of each diet are within
    tolerance of the reported bounds and, in each diet, the smallest meal-size group has a lower
    mean than the largest.""")
open(p,'w').write(s)
EOF
grep -n "is not used\|Spearman" 10.1038-s41598-025-19800-2.yaml; cd ../..; python tools/claims_check.py claims/001474/10.1038-s41598-025-19800-2.yaml paper/10.1038-s41598-025-19800-2.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker now passes: 37 claims, 37 quotes, 14 statistical values, 0 problems. Last, a style pass: em dashes, the word "rather", and ": " inside plain scalars.

**Agent calls Bash**

```bash
cd claims/001474 && sed -i 's/than males early in the meal—a$/than males early in the meal ... a/' 10.1038-s41598-025-19800-2.yaml && grep -n "—\|[Rr]ather" 10.1038-s41598-025-19800-2.yaml; python3 - <<'EOF'
import yaml
p='10.1038-s41598-025-19800-2.yaml'
for ev in yaml.parse(open(p)):
    if isinstance(ev, yaml.ScalarEvent) and ev.style is None and ': ' in ev.value:
        print('PLAIN WITH COLON', ev.value[:80])
EOF
cd ../..; python tools/claims_check.py claims/001474/10.1038-s41598-025-19800-2.yaml paper/10.1038-s41598-025-19800-2.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/001474/10.1038-s41598-025-19800-2.yaml`. The quote checker passes on it with 0 problems. Nothing is committed.

**Text read:** the version of record (open access, Europe PMC PMC12521569): main text, figure legends and Methods. It came with Supplementary Material 1, the legends of Supplementary Figs. 1 to 3. I couldn't open the supplementary PDF as images (no renderer installed), and the main figures weren't available. So significance marks that appear only inside figures were not read. Supplementary Materials 2 to 8, likely the source data, were not supplied.

**Code read:** github.com/xzhang03/Photometry_analysis at commit b88d3943. It is the lab's general MATLAB preprocessing toolbox and contains none of this paper's Python statistics. The one detail it settles is the per-mouse Z-score: `tcpZ.m` computes one SD per mouse over all that mouse's recordings, joined end to end.

**Claims:** 37 findings, all with quotes. 14 claims carry statistics: 14 p-values, with tests in the paper's own words. 37 claims carry criteria, and 16 have expected values with tolerances. Where the paper gives mean ± s.e.m., the s.e.m. is the tolerance; otherwise it is 10%.

**Details the paper leaves open, and the readings named for each:**
- **Response window:** 1–10 s (Methods), 1–9 s (Fig. 2–3 legends), or 0–10 s (Results, Fig. 1).
- **How the Z-score is applied to each trial:** (F − F0) divided by the code's per-mouse SD, or dF/F0 divided by the SD of the mouse's dF/F0 over all its trials.
- **ΔZ-score:** last 5 minus first 5 triggered trials (Methods), or last 15 minus first 15 (legends and the early/late definition used elsewhere).
- **Which sessions count:** at least 15, at least 30, or all triggered-trial sessions (Fig. 2b, Fig. 3k and the correlations).
- **Ensure volume:** the recorded total, or triggered trials × ~50 µL.
- **Supp. Fig. 1d licking measure:** baseline subtracted or divided out; AUC over 1–10 s or the whole post-cue trace; paired or unpaired t-test (the legend and Methods disagree).
- **Fig. 2e lick vigour:** two readings of "throughout", and two of where the decline starts.
- **Fig. 2f–j "initial" lick rate:** the first triggered trial, or the mean of the first 15.
- **Rolling-SD window (Supp. Fig. 2j):** 1, 10 or 60 s.
- **Fasting comparison (Supp. Fig. 2l–p):** no test named; readings are a t-test or a mixed-effects model.
- **Within-group test for Fig. 3i:** the mixed-effects model or the paired t-test of Supp. Fig. 3i.
- **Weight change (Supp. Fig. 3m, q):** as a difference or a ratio, measured from the maximum ad libitum weight, the weight before HFD, or the start of ad libitum feeding.
- **Fig. 1c, ~30% heavier:** which body weights are averaged, and how.
- **Recording-day choice:** where meal-size groups or sessions are ambiguous, both sets are run.

**Where the paper contradicts itself (recorded in the file):**
- **Supp. Fig. 2h:** the sentence calls the NCD correlation positive and the HFD one negative, but the printed values are r = −0.34 and r = 0.26.
- **Fig. 3 counts:** the Results and the legends give different numbers of recordings.
- **Fig. 2f–s:** the meal-size groups add up to 57 NCD and 53 HFD recordings, not 59 and 54.
- **Mixed-effects model:** the Methods place it on "Fig. 1 i", while the legend places it on Fig. 1k.
- **Panel letters:** the text cites Supp. Fig. 3m and 3q for analyses the legends assign to other panels.

**What claims needed and the paper lacks:**
- p-values for Fig. 1l, Fig. 2c–d, 3h and the Supp. Fig. 1–3 tests appear only as figure asterisks, which I couldn't read. Where the text says "significant", the paper's alpha of 0.05 is recorded instead.
- The paper names no test for several claims of "no effect" or "comparable": fasting, locomotion against meal size, and absolute weight against meal length (Supp. Fig. 3l). The readings named for each are recorded as deviations.
- The paper's own analysis code isn't public.

## End of run

27 turns, 6 minutes, result: success.
