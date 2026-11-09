# 000231 · claims · run 40002946140

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000231/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md; ls claims/001453/ claims/000231/ paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -250; wc -l paper/*; head -20 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/10.1038-s41597-022-01728-1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
fold -s -w 200 paper/10.1038-s41597-022-01728-1.txt | sed -n '7,400p'
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a7ad5bfc-43c5-43e4-ac8f-39d4dbd02f22/tool-results/bpwev2wah.txt"
}
```

```
1	pmc Sci Data Sci Data Scientific Data 2052-4463 Nature Publishing Group UK London 9561117 1728 10.1038/s41597-022-01728-1 Data Descriptor A detailed behavioral, videographic, and neural dataset on 
2	object recognition in mice http://orcid.org/0000-0003-1762-3450 Rodgers Chris C. [removed: an e-mail address] grid.189967.8 0000 0001 0941 6502 Department of Neurosurgery, Emory University, Atlanta, 
3	GA 30322 USA 13 10 2022 13 10 2022 2022 9 620 16 5 2022 12 9 2022 © The Author(s) 2022 https://creativecommons.org/licenses/by/4.0/ Open Access This article is licensed under a Creative Commons 
4	Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) 
5	and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative 
6	Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory 
7	regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ . 
8	Mice adeptly use their whiskers to touch, recognize, and learn about objects in their environment. This behavior is enabled by computations performed by populations of neurons in the somatosensory 
9	cortex. To understand these computations, we trained mice to use their whiskers to recognize different shapes while we recorded activity in the barrel cortex, which processes whisker input. Here, we 
10	present a large dataset of high-speed video of the whiskers, along with rigorous tracking of the entire extent of multiple whiskers and every contact they made on the shape. We used spike sorti
[... 318 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a7ad5bfc-43c5-43e4-ac8f-39d4dbd02f22/tool-results/bpwev2wah.txt",
 "offset": 328
}
```

```
328	demonstrating how to load the data. It can be run directly on Dandi Hub without downloading any data. The same code is also available as a JupyterLab notebook at 
329	https://github.com/cxrodgers/NwbDandiData2022/blob/main/UsageNotes.ipynb . First, we import the required modules. We specify the location of an example NWB file. We load the data directly from DANDI. 
330	Alternatively, users could download the file(s) directly from DANDI, and specify the path to the downloaded NWB file, instead of the s3_path given above. In that case, there is no need to specify the 
331	“driver”. In any case, the next line reads the file into a variable called nwbfile, which we use for the rest of the demonstration. For the rest of the example code, the string “In [0]:” indicates a 
332	prompt, and the rest of the line following the prompt is the command the user should type. The lines following the prompt show the expected output. It is often useful to first identify the time 
333	within the session at which each trial occurred, using the trials table. We suggest aligning data to the “response_window_open_time” on each trial, which is locked to the presentation of the shape 
334	stimulus (see “Methods”/“Session control”). The position of the whiskers can be extracted over the entire session. Here we extract the angle of the C2 whisker over the entire session. The angle 
335	itself is stored in the field named data, and the timestamps of the angle are stored in the field name timestamps. Other field specify metadata. We can also extract the time of the contacts made by 
336	the same whisker. We can also extract full-bandwidth neural data from the entire session. Here, only the first 1e6 datapoints are loaded. The units table specifies all the individual neurons that 
337	were recorded, and all of their identified spike times. Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 
338	Acknowledgemen
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
head -5 paper/10.1101-2022.05.10.491259.txt | cut -c1-300; wc -c paper/*; sed -n '25,200p' claims/001453/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
tail -60 claims/001453/*.yaml; ls claims | head; ls claims | wc -l; grep -rh "^  kind:" claims | sort | uniq -c; grep -rh "^  data:" claims | sort | uniq -c; ls docs tools
```

```
0.010).
  source: Figure 2L
  quote: BI ratios show a higher fraction of binocular neurons in ZF compared to DC (ZF = 0.72, DC =
    0.24
  statistics:
  - test: Student's t-test
    p: 0.01
    n: 5 ZF and 5 DC fish
- id: fig3e-longer-swims
  statement: Head-fixed DC perform longer swims than ZF (median 0.75 s against 0.29 s, p <
    0.0001).
  source: Figure 3E and 3F
  quote: DC performed significantly longer swims than ZF (DC = 0.75 s, ZF = 0.29 s
  statistics:
  - test: two-way ANOVA main effect
    p: 0.0001
    p_relation: "<"
    n: 4 ZF fish (3568 events) and 3 DC fish (855 events)
- id: fig3cd-zf-turn-more
  statement: Head-fixed ZF show larger directional tail angles than DC to turn-inducing stimuli,
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/*/ | grep -i s41597 | head; grep -l "s41597" claims/*/*.yaml | head -3; grep -n "kind: agent" -B2 -A12 claims/*/*.yaml | head -40; grep -rn "kind" tools/claims_check.py | head
```

```
10.1038-s41597-020-0415-9.yaml
10.1038-s41597-023-02214-y.yaml
10.1038-s41597-023-02214-y.yaml
10.1038-s41597-024-02943-8.yaml
10.1038-s41597-024-03029-1.yaml
10.1038-s41597-024-03259-3.yaml
claims/000004/10.1038-s41597-020-0415-9.yaml
claims/000037/10.1038-s41597-023-02214-y.yaml
claims/000336/10.1038-s41597-023-02214-y.yaml
claims/000005/10.1038-nn.4412.yaml-1092-checks:
claims/000005/10.1038-nn.4412.yaml-1093-- date: 2026-10-20
claims/000005/10.1038-nn.4412.yaml:1094:  kind: agent
claims/000005/10.1038-nn.4412.yaml-1095-  model: claude-opus-5-5
claims/000005/10.1038-nn.4412.yaml-1096-  ready: true
claims/000005/10.1038-nn.4412.yaml-1097-  changes:
claims/000005/10.1038-nn.4412.yaml-1098-  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
claims/000005/10.1038-nn.4412.yaml-1099-  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
claims/000005/10.1038-nn.4412.yaml-1100-  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
claims/000005/10.1038-nn.4412.yaml-1101-  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
claims/000005/10.1038-nn.4412.yaml-1102-  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
[... 29 more lines not kept]
```

**Agent**

Let me look at a data descriptor example to match the style for this kind of paper.

**Agent calls Bash**

```bash
sed -n '1,140p' claims/000037/10.1038-s41597-023-02214-y.yaml
```

```
# Claims for Gillon, Lecoq et al. (2023, Sci Data 10, 287) on dandiset 000037.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol as stated in docs/protocol.md (version pilot-10).
#
# Source: the version of record, full text as served by Europe PMC (PMC10192216), read from its
# Background, Methods, Data Records, Overview of data, Technical Validation, Usage Notes, Code
# availability, Tables 1 and 2 and the figure legends. No PDF was stored; no figure image was
# seen. The paper is a data descriptor: it states that it reports no statistical analyses, so
# no claim has statistics. Its only supplement, Supplementary Table 1 (session metadata), is
# also published as metadata.csv at https://github.com/jeromelecoq/allen_openscope_metadata
# (projects/credit_assignement, commit 0e9c7aca3d67cbab7c493ab824b7287fb9508f47); that copy was
# read. It holds the columns of Tables 1 and 2 plus local subject and session numbers, UTC
# imaging times, ages and experimental notes. The two other texts under paper/ (bioRxiv
# 10.1101/2021.01.15.426915 and J Neurosci 10.1523/jneurosci.1009-23.2023) are the analysis
# papers on the same data and are not the target here.
#
# Code read: https://github.com/colleenjg/OpenScope_CA_Analysis at commit
# 046e7fef5f452cdc0775fe54040b0f13aeae1e57 (2024-06-30), linked in Code availability and Usage
# Notes, with its dependency https://github.com/colleenjg/util (tag osca_mult, commit
# 2b05f954a4aa871dbfdd83d1546ebe8e7f3069c6), which holds math_util.calculate_snr and
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/cxrodgers/NwbDandiData2022 && cd NwbDandiData2022 && git log -3 --format='%H %ad %s' && ls -la
```

```
33d610b63e8f43594d380443bf70ac1e4e6a48d0 Sat Apr 30 11:21:02 2022 -0400 fix filename
330b2594c16d0957ef4d0db2a4266d8a74e789ee Sat Apr 30 11:20:08 2022 -0400 add example usage notes
ee41e7d0e2d3605a69cbc783515b85882a5dd263 Sat Apr 30 11:17:48 2022 -0400 Initial commit
total 20
drwxr-xr-x 3 runner runner   120 Oct 23 18:27 .
drwx------ 6 runner runner   120 Oct 23 18:27 ..
drwxr-xr-x 7 runner runner   240 Oct 23 18:27 .git
-rw-r--r-- 1 runner runner  1799 Oct 23 18:27 .gitignore
-rw-r--r-- 1 runner runner    73 Oct 23 18:27 README.md
-rw-r--r-- 1 runner runner 11538 Oct 23 18:27 UsageNotes.ipynb
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/NwbDandiData2022 && cat README.md && python3 -c "
import json;nb=json.load(open('UsageNotes.ipynb'))
for c in nb['cells']:
  print('---',c['cell_type']);print(''.join(c['source']))
  for o in c.get('outputs',[]):
    print('>>', ''.join(o.get('text', '')) or ''.join(o.get('data',{}).get('text/plain','')))
"
```

```
# NwbDandiData2022
Example scripts for working with my NWB data on Dandi
--- markdown
# Usage Notes
This notebook demonstrates how to interact with the NWB files in the Rodgers 2022 dataset.
--- code
# NWB imports and DANDI imports
import pynwb
from pynwb import NWBHDF5IO
from dandi.dandiapi import DandiAPIClient
--- code
# This ID specifies the object recognition dataset
dandiset_id = '000231'

# This specifies a path to an example NWB file, for a single session from subject 231CR
filepath = 'sub-231CR/sub-231CR_ses-20190921T144923_behavior+ecephys+image.nwb'
--- code
## This loads the NWB file without requiring the user to download the file
# First get the URI for the NWB file on dandihub
with DandiAPIClient() as client:
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; for p in "88.9" "33.8" "115 sessions" "18,514" "63,979,800" "44/115" "7433" "2.8 pixels" "15 mice" "0.2%" "192" "90 trials" "95%" "133 ms" "processed_whisker_position" "Table 1" "Supplement" "supplement"; do echo "== $p: VoR $(grep -o "$p" 10.1038*.txt | wc -l) preprint $(grep -o "$p" 10.1101*.txt | wc -l)"; done
```

```
== 88.9: VoR 2 preprint 2
== 33.8: VoR 1 preprint 1
== 115 sessions: VoR 1 preprint 1
== 18,514: VoR 1 preprint 1
== 63,979,800: VoR 1 preprint 1
== 44/115: VoR 1 preprint 1
== 7433: VoR 1 preprint 1
== 2.8 pixels: VoR 1 preprint 1
== 15 mice: VoR 1 preprint 1
== 0.2%: VoR 2 preprint 2
== 192: VoR 1 preprint 1
== 90 trials: VoR 1 preprint 1
== 95%: VoR 1 preprint 1
== 133 ms: VoR 0 preprint 3
== processed_whisker_position: VoR 4 preprint 3
== Table 1: VoR 2 preprint 1
== Supplement: VoR 1 preprint 2
== supplement: VoR 0 preprint 0
```

**Agent calls Bash**

```bash
cd  sed -n '1,60p' tools/claims_check.py; grep -n "def " tools/claims_check.py
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

[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s,indent=1)[:5000])"
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
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
p=s['properties']['claims']['items']['properties']
for k in list(p)[list(p).index('where'):]: print(k, json.dumps(p[k])[:300])
print(json.dumps(s['\$defs'],indent=0)[:3000])
print([k for k in s['properties']])"
```

```
where {"description": "For a claim with data `elsewhere`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.", "type": "string", "minLength": 1}
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
[... 84 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/000231/10.1038-s41597-022-01728-1.yaml",
 "content": "# Claims for Rodgers (2022, Sci Data 9, 620) on dandiset 000231.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol as stated in docs/protocol.md (version pilot-10).\n#\n# Source: the version of record, full text as served by Europe PMC\n# (paper/10.1038-s41597-022-01728-1.txt), read from its Background & Summary, Methods, Data\n# Records, Technical Validation, Usage Notes, Code availability, Tables 1 to 6 and the legends of\n# Figs. 1 to 3. No PDF was stored, so no figure was seen; Fig. 2c (error rates per training set)\n# is known only from its legend and the Technical Validation text. The paper is a data\n# descriptor with no supplement and reports no statistical tests, so no claim has statistics.\n# The bioRxiv preprint (10.1101/2022.05.10.491259, version 1) is also under paper/; it was\n# compared for the reported counts (15 mice, 115 sessions, 18,514 trials, 63,979,800 frames,\n# 88.9 h, 33.8 h, 44/115, 7433 frames, 2.8 pixels, 90 trials, 95%), which are the same, and\n# was not otherwise used.\n#\n# Code read: https://github.com/cxrodgers/NwbDandiData2022 at commit\n# 33d610b63e8f43594d380443bf70ac1e4e6a48d0 (2022-04-30), linked in Usage Notes. It holds only\n# UsageNotes.ipynb, which loads sub-231CR/sub-231CR_ses-20190921T144923_behavior+ecephys+image.nwb\n# from dandiset 000231 and prints the trials table, the C2 angle, the C2 contacts, raw neural\n# data and the units table. Its printed outputs disagree with the paper's NWB names. It reads\n# the whisker data from nwbfile.processing['behavior']['processed_position_whisker_C2'] and the\n# contacts from nwbfile.processing['behavior']['contacts_by_whisker_C2'], where the Data Records\n# sections name processing groups \"processed_whisker_position\", \"identified_whisker_contacts\",\n# \"raw_whisker_position\" and \"behavioral_events\"; Table 1 itself says processing holds one\n# ProcessingModule named \"behavior\". Both namings are given as readings (claim nwb-structure).\n# The notebook also shows the electrode group named \"all_channels\" and the subject strain\n# \"C57BL6/J\". The tracking software the paper lists (github.com/cxrodgers/PoseTF,\n# github.com/cxrodgers/whisk) was not read: no criterion here rests on it. The analysis code of\n# the original study (ref. 8, Rodgers et al. 2021, Neuron) is not linked by this paper.\n#\n# Data the paper describes. 15 C57BL/6J mice, bred in-house, males and females in roughly\n# equal proportion, behavioral training begun between postnatal days 90 and 180, recorded at\n# Columbia University. Two groups: shape discrimination (convex, lick right; concave, lick left)\n# and shape detection (either shape, lick right; no shape, \"nothing\", lick left); no mouse did\n# both. Head-fixed, all whiskers but the C row trimmed; whiskers C0 (a straddler), C1, C2, C3\n# tracked. On each trial a servo moves a curved shape to one of three positions (close, medium,\n# far); the response window opens 2 s after the motor starts; the first lick in it decides the\n# outcome. 115 sessions, 18,514 trials, 88.9 h of 200 frames/s video (63,979,800 frames, most at\n# 640 x 550). In 44 of the sessions, a 64-channel linear silicon probe (Cambridge Neurotech H3,\n# 20 um pitch) in an identified column (typically C1, C2 or C3) of left barrel cortex, recorded\n# with Open Ephys at 30 kHz, 33.8 h in all, spike sorted with Kilosort and curated in Phy. One NWB\n# file per session (sub-<mouse>_ses-<session>_behavior+image[+ecephys].nwb), with a trials table\n# (start_time, stop_time, direct_delivery, stim_is_random, optogenetic, outcome, choice,\n# rewarded_side, servo_position, stimulus, ignore_trial, choice_time, response_window_open_time,\n# trial), lick and reward times, pose tracking of 8 markers on each of 4 whiskers, processed\n# whisker angle, bend, base and tip with an interpolated flag, whisker contacts per whisker, raw\n# neural data with timestamps, an electrodes table and a units table (inhibitory, depth, layer,\n# neuron_channel, spike_times, obs_intervals). All times are in the \"common video timebase\"\n# (frame F at F/200 s). Raw video (mkv, nominal 30 frames/s) is in a folder named as the NWB\n# file; raw Open Ephys files and Kilosort/Phy outputs are under sourcedata/. The paper cites the\n# dataset as DANDI 000231, version 0.220904.1554 (doi:10.48324/dandi.000231/0.220904.1554).\n#\n# Outside data. An earlier release of the same study's data is on Zenodo\n# (doi:10.5281/zenodo.4743837, ref. 13); no claim uses it. The curated whisker training sets\n# (curated datasets 1 to 5) and their cross-validated predictions, on which the tracking\n# accuracy claims rest, are not among the deposits the Data Records list; the paper does not\n# say where they are.\n#\n# Trials to analyse. Where a criterion counts trials \"to analyse\" it means trials with\n# ignore_trial False, as Table 6 and the trials-table section direct, unless it names readings.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000231\"\npaper: doi:10.1038/s41597-022-01728-1\nclaims:\n- id: dataset-size\n  statement: The dataset holds 15 mice, 115 sessions, 18,514 trials and 63,979,800 video frames,\n    which is 88.9 hours of video.\n  source: Methods, High-speed videography and whisker tracking, paragraph 1; Background &\n    Summary, last paragraph\n  quote: The size of the dataset ... 15 mice, 88.9 hours, 115 sessions, 18,514 trials, 63,979,800\n    frames\n  expected:\n  - quantity: mice\n    value: 15\n    tolerance: 0\n  - quantity: sessions\n    value: 115\n    tolerance: 0\n  - quantity: trials\n    value: 18514\n    tolerance: 0\n  - quantity: video frames\n    value: 63979800\n    tolerance: 0\n  - quantity: hours of video\n    value: 88.9\n    tolerance: 0.05\n    unit: h\n  criterion: Mice are subject folders and sessions are NWB files. Tolerance 0 for the counts,\n    as they are counts of deposited records, and 0.05 h for the hours, the rounding of the\n    printed value. The paper does not define which trials and frames are counted. Readings for\n    trials are (a) all rows of all trials tables, (b) rows with ignore_trial False. Readings for\n    frames are (a) the frame counts of the raw video files, (b) the number of frames of the\n    raw_whisker_position series (N_frames, Data Records), summed over sessions; hours are\n    frames divided by 200 and by 3600 under each. Reproduced when mice and sessions match and\n    trials and frames match exactly under one reading each; partially reproduced when mice and\n    sessions match and trials and frames are within 10% under some reading; not reproduced\n    otherwise.\n- id: neural-sessions\n  statement: Neural recordings from barrel cortex were made in 44 of the 115 sessions.\n  source: Methods, Neural recordings during behavior, paragraph 1\n  quote: For a subset (44/115) of the behavioral sessions that we report here, we also recorded\n    neuronal activity in identified columns of the barrel cortex\n  expected:\n    quantity: sessions with neural recordings\n    value: 44\n    tolerance: 0\n  criterion: Count of NWB files whose name includes \"ecephys\" (Data Records, Directory\n    structure) and, as a check, of files holding an \"extracellular array recording\"\n    ElectricalSeries and a units table. Tolerance 0 because it is a count of deposited\n    sessions. Reproduced when both counts are 44.\n- id: neural-hours\n  statement: The dataset includes 33.8 hours of 64-channel neural recording at 30 kHz.\n  source: Background & Summary, last paragraph\n  quote: includes 88.9 hours of behavioral video at 200 frames per second and 33.8 hours of\n    64-channel neural recording at 30 kHz\n  expected:\n    quantity: hours of neural recording\n    value: 33.8\n    tolerance: 0.05\n    unit: h\n  criterion: The paper does not say which recording is timed. Readings are (a) the summed\n    duration of the \"extracellular array recording\" timestamps in the NWB files (last minus\n    first), (b) the summed duration of the main Open Ephys recordings under sourcedata/\n    (test recordings of a few seconds left out, Data Records, Raw data, neural acquisition\n    files). Tolerance 0.05 h, the rounding of the printed value. Reproduced when one reading is\n    within it; partially reproduced when one is within 10%. The channel count of the raw files\n    (64) is checked; the NWB files exclude broken channels and may hold fewer.\n- id: task-rules\n  statement: In discrimination sessions convex shapes are rewarded on the right and concave\n    on the left; in detection sessions either shape is rewarded on the right and catch trials\n    with no shape on the left.\n  source: Methods, Two behavioral tasks, paragraph 1\n  quote: Shape discrimination mice were trained to lick right for convex shapes and left for\n    concave shapes. Shape detection mice were trained to lick right for either shape (concave\n    or convex) and to lick left on catch trials when no shape was presented at all\n  criterion: From the trials table, rewarded_side against stimulus. A session is a detection\n    session when any trial has stimulus \"nothing\" (Table 6, stimulus) or when its metadata\n    names the task; otherwise discrimination, with the session metadata (experiment\n    description) checked where it names the task. Reproduced when, over trials to analyse in\n    every session, rewarded_side follows the rule of the session's task on every trial;\n    partially reproduced when it does on at least 95% of trials in every session. All trials,\n    including ignored ones, are shown as a variant.\n- id: nothing-detection-only\n  statement: The stimulus \"nothing\" occurs only in the detection task.\n  source: Data Records, NWB file, trials table, Table 6 (stimulus)\n  quote: \"'nothing' was only used in the detection task, not in the discrimination task\"\n  depends_on:\n  - task-rules\n  criterion: Using the session metadata's task where it is given (experiment description or\n    keywords), reproduced when no discrimination session holds a trial with stimulus\n    \"nothing\". When the metadata do not name the task, the claim cannot be tested apart from\n    task-rules (which uses \"nothing\" to assign the task) and is reported as such.\n- id: one-task-per-mouse\n  statement: No mouse was trained on both tasks.\n  source: Methods, Two behavioral tasks, paragraph 1\n  quote: No mice were trained on both tasks\n  depends_on:\n  - task-rules\n  criterion: Each session's task as assigned in task-rules. Reproduced when every mouse's\n    sessions are all of one task.\n- id: servo-positions\n  statement: The shape stops at one of three positions, close, medium or far.\n  source: Methods, Two behavioral tasks, paragraph 1; Table 6 (servo_position)\n  quote: The shape stopped at one of three different positions (close, medium, or far)\n  criterion: Reproduced when the servo_position values over all trials with a shape (stimulus\n    not \"nothing\") are exactly the set close, medium, far, and each occurs in every session's\n    trials to analyse; partially reproduced when the set is right but some session lacks one.\n- id: response-window-timing\n  statement: The response window opens 2 s after the servo motor starts moving the shape, which\n    reaches its final position 0.8 to 0.4 s before the window opens, depending on the position.\n  source: Methods, Two behavioral tasks, paragraph 1\n  quote: which began exactly 2 seconds after the linear servo motor started moving the shape\n    toward the mouse ... reached its final position between −0.8 s and −0.4 s, depending on\n    whether the final position was close, medium, or far\n  criterion: Testable only if the dataset records the time the motor starts or stops. The\n    trial start_time is the synchronization pulse (Methods, Alignment of multiple data\n    streams), which the paper does not place relative to motor onset, so it is not used as\n    motor onset. When motor times exist, reproduced when the window opens 2 s (within one frame,\n    5 ms) after motor onset on at least 95% of trials and the motor stops between 0.8 and 0.4\n    s before it, with close, medium and far ordered as the paper gives. Otherwise blocked; the\n    distribution of response_window_open_time minus start_time is reported for information.\n- id: choice-time-first-lick\n  statement: The choice time is the first lick after the response window opens, and on spoiled\n    trials with no lick it is set 45 s after the window opens.\n  source: Data Records, NWB file, trials table, Table 6 (choice_time)\n  quote: choice_time (float) The time of the choice lick, which is the first lick after the\n    response window opened. On spoiled trials with no lick, this value is 45 seconds after the\n    response window opened\n  criterion: Lick times from the left, right and (where present) both lick series. For each\n    non-spoiled trial, the first lick at or after response_window_open_time, compared with\n    choice_time; its side compared with choice. For spoiled trials, choice_time minus\n    response_window_open_time compared with 45 s. Licks and trial times are both aligned\n    trial by trial, so a match within 5 ms (one frame, Methods, Alignment) counts. Reproduced\n    when all of these hold on at least 99% of trials of each kind; partially reproduced at\n    95%. All trials are used, as the definition does not depend on ignore_trial.\n- id: outcome-consistency\n  statement: The first lick in the response window decides the outcome; a choice on the\n    rewarded side is correct, any other choice is an error, and a trial with no choice is\n    spoiled.\n  source: Methods, Two behavioral tasks, paragraph 1; Table 6 (outcome, choice)\n  quote: Only the first lick (left or right) during the response window determined the trial\n    outcome (correct or incorrect)\n  criterion: From the trials table. Reproduced when on every trial outcome is \"correct\"\n    exactly when choice equals rewarded_side, \"error\" when choice is the other side, and\n    \"spoil\" exactly when choice is \"nogo\" (Table 6, choice); direct-delivery trials are shown\n    apart, as their water does not depend on the choice. Partially reproduced when this holds\n    on at least 99% of trials.\n- id: reward-and-timeout\n  statement: Correct licks were rewarded with water, and incorrect licks were punished with a\n    timeout, typically 9 s long.\n  source: Methods, Two behavioral tasks, paragraph 1\n  quote: Correct licks were rewarded with water and incorrect licks were punished with a\n    timeout, typically 9 seconds long\n  expected:\n    quantity: timeout after an error\n    value: 9\n    tolerance: 0.9\n    unit: s\n  depends_on:\n  - outcome-consistency\n  criterion: Over trials to analyse. Reward is a reward time on the rewarded side between\n    choice_time and stop_time; reproduced for this part when it occurs on every correct trial\n    and on no error trial (partially when on at least 95% and at most 5%). The paper does not\n    say how the timeout appears in the trial times. Readings are (a) the median over error\n    trials of stop_time minus choice_time, (b) that median on error trials minus the same median\n    on correct trials. The timeout part holds when the reading is within 0.9 s of 9 s. The\n    claim is reproduced when the reward part holds and both readings hold, not reproduced when\n    neither does, and blocked as methods_underspecified when they disagree, with both shown.\n- id: forced-alternation-start\n  statement: Every session began with 45 trials of Forced Alternation, which are non-random\n    trials, before random trials.\n  source: Methods, Session control and trial types to be dropped from analysis, paragraph 2\n  quote: Even in fully trained mice, we found it best to begin every session with 45 trials of\n    Forced Alternation, before switching to random trials\n  criterion: By the trial field (trial number), since trials before the video began are left\n    out of the table (Data Records, trials table). Reproduced when, in every session, every\n    present trial numbered 0 to 44 has stim_is_random False; partially reproduced when that\n    holds in more than half the sessions. The number of the first random trial in each session\n    is reported.\n- id: ignore-trial-definition\n  statement: A trial is marked ignore_trial when it is direct delivery, non-random, spoiled,\n    optogenetic or otherwise munged.\n  source: Data Records, NWB file, trials table, Table 6 (ignore_trial)\n  quote: \"ignore_trial (bool) This is True if 'direct_delivery' is True, or 'stim_is_random' is\n    False, or outcome is 'spoil', or 'optogenetic' is True, or the trial was otherwise munged\"\n  criterion: Munged trials carry no flag of their own, so only one direction is tested.\n    Reproduced when every trial with direct_delivery True, stim_is_random False, outcome\n    \"spoil\" or optogenetic True has ignore_trial True. The number of trials with ignore_trial\n    True and none of the four flags (the munged trials) is reported.\n- id: trials-table-structure\n  statement: Each trial's stop time equals the next trial's start time, and the table's index\n    is the trial number.\n  source: Data Records, NWB file, trials table, Table 6 and the paragraph after it\n  quote: stop_time (float) Stop time of the trial. (Equal to the start time of the next trial.)\n    ... The index of this DataFrame is called \"id\" and is identical to the field \"trial\"\n  criterion: Within each session, for consecutive rows, stop_time compared with the next\n    start_time, and id with trial. Reproduced when both are equal (times within 1 ms) for every\n    row; the last trial of a session is not compared.\n- id: video-timebase\n  statement: Times in the NWB file are in a common video timebase in which frame F falls at\n    exactly F/200 s.\n  source: Methods, Alignment of multiple data streams, paragraph 2\n  quote: Since the camera ran at 200 frames per second, frame F in the video is defined as\n    occurring at exactly time F/200 in the common video timebase\n  criterion: Reproduced when the timestamps of every processed whisker series and every pose\n    series are integer multiples of 0.005 s (within 1e-6 s) and their spacing is 0.005 s except\n    at gaps. Contact start and stop times are also checked against the 0.005 s grid.\n- id: sync-gap-and-interpolation\n  statement: Processed whisker timestamps have gaps, for instance during the 133 ms blackout at\n    each trial start, because gaps longer than 4 frames (20 ms) were not interpolated.\n  source: Data Records, NWB file, processing group processed_whisker_position, last paragraph\n  quote: these timestamps will in general contain gaps, for instance during the 133 ms blackout\n    synchronization pulse at the start of each trial. This is because we did not interpolate\n    over gaps longer than 4 frames (20 ms)\n  expected:\n    quantity: blackout gap duration at trial start\n    value: 0.133\n    tolerance: 0.0133\n    unit: s\n  depends_on:\n  - video-timebase\n  criterion: Two parts, per whisker and session. (1) Runs of consecutive frames with\n    interpolated True are at most 4 frames long. (2) For each trial, the longest gap in the\n    angle timestamps that begins within 0.2 s of start_time (missing time, gap minus one\n    frame) is within 10% of 133 ms. The paper says \"in general\", so (2) is read as holding on\n    more than half of trials for C1, C2 and C3. Reproduced when (1) holds everywhere and (2)\n    holds; partially reproduced when one of them holds. C0 is reported apart, as it may be\n    missing for long stretches.\n- id: bend-null-interpolated\n  statement: Whisker bend is null on interpolated frames.\n  source: Data Records, processed_whisker_position, Table 3 (bend)\n  quote: This is null on interpolated frames\n  criterion: Reproduced when, for every whisker and session, bend is NaN (or missing) on every\n    frame with interpolated True. Bend values on non-interpolated frames that are NaN are\n    counted and reported.\n- id: neural-timestamps\n  statement: The neural data timestamps are regularly spaced in the common video timebase, at\n    a rate near but not exactly 30 kHz.\n  source: Data Records, NWB file, acquisition group extracellular array recording, last\n    paragraph\n  quote: The sampling rate is nearly 30 kHz, but not exactly, because it has been converted to\n    the common video timebase used throughout the NWB file\n  criterion: Per ecephys session, the rate is (number of samples minus one) over the span of\n    the timestamps, and regular spacing is the spread of successive differences. Reproduced\n    when every session's spacing is constant to within 1e-9 s (a linear map, Methods, continuous\n    alignment), its rate differs from 30000 Hz by less than 1%, and it is not exactly 30000 Hz\n    in at least one session.\n- id: neural-video-alignment\n  statement: The neural and video timebases are related by a linear fit whose residuals at the\n    trial synchronization pulses are never more than one frame (5 ms).\n  source: Technical Validation, Alignment data\n  quote: In contrast the neural and video timebase were synchronized very well by a linear fit.\n    Residuals were never more than a single frame (5 ms)\n  expected:\n    quantity: largest residual of the neural to video linear fit\n    value: 0.005\n    tolerance: 0\n    unit: s\n  criterion: Needs the pulse times in both streams, the neural from the analog input of the\n    raw Open Ephys files under sourcedata/ (the sample at which it goes low), the video from the\n    frame on which the raw video goes dark (Methods, Alignment). The paper gives no threshold\n    for either detection; the input is read as low below half its range, and a frame as dark\n    when its mean brightness is below half the session median, a standard choice that is not\n    the paper's. A line is fit from neural to video pulse times per session. Reproduced when\n    the largest absolute residual is at most 5 ms in every session; partially reproduced in\n    more than 90% of sessions. When the raw files cannot give pulse times, blocked.\n- id: behavior-clock-drift\n  statement: The behavioral (Arduino) timebase fit the other two timebases poorly, with\n    residuals that varied slowly but predictably over the session, so behavioral events were\n    aligned trial by trial.\n  source: Technical Validation, Alignment data\n  quote: We observed that the behavioral timebase was a poor fit to the other two timebases and\n    that its residuals varied slowly but predictably over the session\n  criterion: Needs trial start times in the behavioral (Arduino) timebase, which the Data\n    Records do not list among the raw deposits (only video and Open Ephys files). If the dataset\n    holds them, a line is fit from behavioral to video trial starts per session; reproduced\n    when the residuals exceed one frame (5 ms) in most sessions and are autocorrelated over\n    trials (lag-1 autocorrelation above 0.5, a standard choice, the paper gives no measure).\n    Otherwise blocked.\n- id: unit-quality-isi\n  statement: Every unit in the dataset passed the objective quality criteria, among them at most\n    5% of inter-spike intervals below 3 ms and at most 20% of the recording below 5% of the\n    mean firing rate.\n  source: Technical Validation, Spike sorting\n  quote: single units had to pass all of the following objective criteria ... ≤5% of the\n    inter-spike intervals less than 3 ms; ≤1.5% change per minute in spike amplitude; ≤20% of\n    the recording at <5% of the mean firing rate\n  criterion: From the units table, as the NWB file holds only well-sorted single units (Data\n    Records, Raw data, neural acquisition files). ISI part, the fraction of a unit's\n    inter-spike intervals below 3 ms; holds when it is at most 5% for every unit. Firing-rate\n    part, the fraction of time bins within obs_intervals whose rate is below 5% of the unit's\n    mean rate; the paper gives no bin. Readings are (a) 60 s bins, the time unit of the\n    amplitude criterion beside it, (b) one bin per trial (start_time to stop_time). It holds\n    when the fraction is at most 20% for every unit. Reproduced when both parts hold under the\n    readings run; not reproduced when the ISI part fails; blocked as methods_underspecified\n    when the readings of the firing-rate part disagree. The amplitude criteria need Kilosort\n    amplitudes in microvolts and the detection threshold, which the paper does not give; they\n    are reported where sourcedata/ allows and do not enter the outcome.\n- id: unit-depth-layer\n  statement: Each unit's depth is the depth of the electrode its neuron_channel indexes, and its\n    layer is assigned from that depth.\n  source: Data Records, NWB file, units table, Table 5\n  quote: This is calculated by taking the depth of the electrode in the electrodes table which\n    is indexed by the field \"neuron_channel\" for this unit ... This specifies the laminar\n    location of the unit, based on its depth\n  criterion: Per ecephys session. (1) A unit's depth equals the y of the electrodes row at\n    index neuron_channel. (2) Layers are assigned by fixed boundaries (the paper uses ref. 26\n    and does not print them), so over all units of all sessions the depth ranges of the\n    layers do not overlap and run from superficial to deep in the order L1, L2/3, L4, L5, L6\n    (whichever occur). Reproduced when both hold for every unit.\n- id: electrodes-order\n  statement: The NWB electrodes are ordered from superficial to deep, broken channels are\n    excluded, the raw data columns follow the electrodes table, and the sites are 20 um apart\n    over 1280 um.\n  source: Methods, Ordering of neural data channels; Methods, Neural recordings during\n    behavior, paragraph 4; Data Records, electrodes table\n  quote: we ordered the channels in the Neurodata Without Borders (NWB) file in order of the\n    anatomical location of the corresponding recording site, from superficial to deepest. We\n    excluded broken channels from the NWB file\n  expected:\n    quantity: spacing between adjacent sites\n    value: 20\n    tolerance: 0\n    unit: um\n  criterion: Per ecephys session. Reproduced when electrodes y increases strictly down the\n    table, successive differences are multiples of 20 um (a larger step marks a broken\n    channel), the number of rows is at most 64 and equals the number of data columns of the\n    extracellular array recording, and the span of a full 64-site probe would be 63 steps of 20\n    um (1260 um between end site centres, which the paper's 1280 um, 64 x 20 um, includes).\n    The location string of each electrode is checked to hold the five items Data Records\n    lists.\n- id: recording-columns\n  statement: Each recording session names the barrel column the probe was in, sampling\n    typically C1, C2 and C3.\n  source: Data Records, electrodes table, Table 4 (electrode_group); Methods, Neural\n    recordings during behavior, paragraphs 2 and 3\n  quote: Its \"location\" field specifies the barrel-related cortical column in which the\n    recording device was inserted during this session\n  criterion: Reproduced when every ecephys session's electrode group location names a barrel\n    column (a row letter and arc number, or a straddler). The count of sessions per column is\n    reported; the paper gives only a goal of sampling C1, C2 and C3 equally often, which is\n    not judged.\n- id: units-obs-intervals\n  statement: Each unit has one observation interval, the start and stop of the neural recording,\n    with its spike times in the common video timebase.\n  source: Data Records, NWB file, units table, Table 5 (obs_intervals, spike_times)\n  quote: In this dataset, there is only one contiguous chunk of data included per session, so the\n    length of this list is one\n  criterion: Reproduced when every unit has exactly one interval, all its spikes fall inside\n    it, and the interval lies within the span of the session's raw neural timestamps (within\n    one sample).\n- id: pose-structure\n  statement: Each session holds pose tracking of four whiskers with eight markers each, whose\n    pixel to millimetre conversion is the same for all markers within a session.\n  source: Data Records, NWB file, processing group raw_whisker_position\n  quote: It comprises four data interfaces, each of which is an ndx_pose.pose.PoseEstimation\n    containing pose tracking data for one of the four whiskers that we tracked. In turn, each\n    PoseEstimation comprises eight PoseEstimationSeries ... which is the same for all markers\n    within a session but can vary across sessions\n  depends_on:\n  - nwb-structure\n  criterion: Reproduced when every session has four PoseEstimation objects (C0 to C3) of eight\n    series each, each series of shape (N_frames, 2), and one conversion value per session.\n    Whether the conversion varies across sessions is reported.\n- id: c0-rare-contacts\n  statement: The straddler whisker C0 rarely made contact with the shapes in most mice.\n  source: Methods, Two behavioral tasks, paragraph 2\n  quote: but this whisker rarely made contact with the shapes in most mice\n  criterion: Per mouse, contact counts of each whisker over its sessions' trials to analyse.\n    The paper gives no threshold for \"rarely\"; it is read as C0 making fewer contacts than each\n    of C1, C2 and C3. Reproduced when this holds in more than half the mice. Each mouse's\n    fraction of contacts made by C0 is reported.\n- id: session-min-trials\n  statement: Sessions with fewer than 90 trials to analyse were excluded.\n  source: Technical Validation, Inclusion criteria\n  quote: We also excluded sessions with fewer than 90 trials to analyze\n  criterion: Readings for \"trials to analyse\" are (a) trials with ignore_trial False, (b)\n    trials with stim_is_random True and outcome not spoil (the \"random trials\" of Methods,\n    Session control). Reproduced when every session has at least 90 under both readings; not\n    reproduced when a session has fewer under both; blocked as methods_underspecified when they\n    disagree. The smallest count is reported.\n- id: session-labeling-quality\n  statement: Each included session has every whisker labeled in at least 95% of frames, and at\n    most 2% of its contact events contain a frame with a missing label.\n  source: Technical Validation, Inclusion criteria\n  quote: we required that every whisker be labeled in ≥95% of the frames, that ≤2% of the\n    contact events contained even a single frame with a missing label\n  expected:\n  - quantity: smallest fraction of frames labeled, any whisker and session\n    value: 0.95\n    tolerance: 0\n  - quantity: largest fraction of contacts with a missing frame, any whisker and session\n    value: 0.02\n    tolerance: 0\n  criterion: A frame is labeled for a whisker when it was not interpolated. The paper does not\n    give the denominator or whether C0 counts. Readings for the frame fraction are (a) frames\n    with interpolated False over the frames of the processed series, (b) frames with all\n    eight markers in the raw pose series over the frames of the video. For contacts, a contact\n    of a whisker has a missing label when any frame from start_time to stop_time is\n    interpolated or absent from that whisker's processed series. Whiskers are (i) C0 to C3,\n    (ii) C1 to C3, C0 \"rarely made contact\" and may not have been held to this. Reproduced when\n    both thresholds hold in every session under every reading of each; not reproduced when\n    they fail under all; blocked as methods_underspecified otherwise.\n- id: contacts-structure\n  statement: Contacts are stored per whisker as time intervals with start, stop, location in\n    the frame and whisker angle.\n  source: Data Records, NWB file, processing group identified_whisker_contacts\n  quote: We have also added optional fields containing the location of each contact, expressed\n    both as a Cartesian location within the frame and also as the angle of the whisker at the\n    time of the contact\n  depends_on:\n  - nwb-structure\n  criterion: Reproduced when every session has a contacts table for each tracked whisker that\n    made contacts, with start_time not after stop_time on every row, a location (x and y) and\n    an angle column.\n- id: nwb-structure\n  statement: Each NWB file holds the groups Table 1 lists, acquisition (neural recording and\n    behavioral video), electrodes, processing, trials and units, with licks, rewards, raw and\n    processed whisker position and whisker contacts under processing.\n  source: Data Records, Annotated data in the NWB file, Table 1 and the sections after it\n  quote: processing A group containing a ProcessingModule named \"behavior\". This includes\n    processed data about behavioral events, whisker position, and whisker contacts\n  criterion: The text names the processing data in two ways, as separate groups\n    (\"behavioral_events\", \"raw_whisker_position\", \"processed_whisker_position\",\n    \"identified_whisker_contacts\", each holding interfaces such as \"whisker_C2\") and, in Table 1,\n    as one module \"behavior\". The paper's UsageNotes.ipynb (commit 33d610b) reads\n    processing['behavior']['processed_position_whisker_C2'] and\n    processing['behavior']['contacts_by_whisker_C2']. Reproduced when every file holds the\n    contents of each section (licks left and right, rewards left and right, pose per whisker,\n    angle, base, tip, bend and interpolated per whisker, contacts per whisker, the Table 6\n    columns of trials) under either naming, which is reported; ecephys files also the\n    extracellular array recording, electrodes (Table 4) and units (Table 5 columns). Partially\n    reproduced when a section's data are present under other names. The acquisition\n    \"behavioral video\" holds a relative path to an existing video file.\n- id: file-layout\n  statement: The dataset has one folder per mouse with one NWB file per session named\n    sub-<mouse>_ses-<session>_behavior+image(.nwb, with ecephys when neural data are present),\n    the video of each session in a folder of the same name, and raw neural data under\n    sourcedata.\n  source: Data Records, Directory structure of the entire dataset\n  quote: At the top level, there is one folder per subject ... Video files are stored in a\n    directory with the same name as the corresponding NWB file. Finally, we also provide the\n    raw neural data files in a directory called \"sourcedata\"\n  criterion: From the dataset's file list. Reproduced when every NWB file is in its subject's\n    folder and named as described, every session has a video in a folder named as its NWB\n    file, and sourcedata/ holds Open Ephys files and Kilosort/Phy outputs for the ecephys\n    sessions under sub-<mouse> folders; partially reproduced when one part fails for some\n    sessions.\n- id: video-format\n  statement: The raw videos are mkv files whose frame rate is set to 30 frames/s though the true\n    rate is 200 frames/s, and most sessions are 640 x 550 pixels.\n  source: Data Records, Raw data, video files; Methods, High-speed videography and whisker\n    tracking, paragraph 1\n  quote: Importantly, the frame rate of this video file is spuriously set to 30 frames per\n    second, even though the true frame rate is 200 frames per second\n  depends_on:\n  - file-layout\n  criterion: From the video file headers. Reproduced when every video is mkv (x264) with a\n    nominal rate of 30 frames/s, and more than half the sessions are 640 x 550 (in either axis\n    order); the frame count over 200 is compared with the span of the session's whisker\n    timestamps and reported.\n- id: subjects-sex-age-strain\n  statement: The mice were C57BL/6J, males and females in roughly equal proportion, and began\n    training between postnatal days 90 and 180.\n  source: Methods, Two behavioral tasks, paragraph 3\n  quote: We purchased breeder mice from the C57BL/6 J strain ... Mice began behavioral training\n    between postnatal days 90 and 180 ... We used males and females arbitrarily and in roughly\n    equal proportion\n  criterion: From subject metadata (sex, strain, date of birth) and session start times.\n    Strain holds when every subject is C57BL/6J (any spelling). Age holds when every mouse's\n    first session is at 90 days or older, as sessions came after training (the training start\n    itself is not recorded). The paper sets no threshold for \"roughly equal\"; readings are (a)\n    a two-sided binomial test of the sex counts against one half does not reject at p 0.05,\n    (b) the minority sex is at least one third of the mice. Reproduced when strain, age and\n    both sex readings hold; blocked as methods_underspecified when the two sex readings\n    disagree; not reproduced otherwise. The counts are reported.\n- id: tracking-mean-error\n  statement: The mean distance between true and predicted marker labels is 2.8 pixels.\n  source: Technical Validation, Validation of pose tracking data, paragraph 1\n  quote: The simplest metric of tracking accuracy is the mean distance between the true label\n    and the predicted label, which is 2.8 pixels in our case\n  expected:\n    quantity: mean distance between true and predicted marker positions\n    value: 2.8\n    tolerance: 0.28\n    unit: pixels\n  criterion: Needs the human-curated labels and the held-out predictions of the network\n    (Technical Validation, doubly held-out cross validation), which the Data Records do not\n    list among the deposits. The paper does not say over which curated datasets the mean is\n    taken; readings are (a) curated dataset 1, (b) all five pooled. Reproduced when a reading\n    is within tolerance; blocked when the labels are not in the dataset.\n- id: tracking-error-dataset1\n  statement: On curated dataset 1, 7433 randomly chosen typical frames, each type of tracking\n    error (poorly traced, incorrectly classified, false positive, false negative) is below\n    0.2%.\n  source: Technical Validation, Validation of pose tracking data, paragraphs 3 and 4; Fig. 2c\n  quote: each type of error is nearly zero (<0.2%) on dataset 1, which is the only dataset\n    representative of typical frames\n  expected:\n  - quantity: frames in curated dataset 1\n    value: 7433\n    tolerance: 0\n  - quantity: largest error rate of any type, curated dataset 1\n    value: 0.002\n    tolerance: 0\n  criterion: Error types as Technical Validation defines them (poorly traced, a tip or mean\n    marker distance above 20 pixels; incorrectly classified; false positive; false negative),\n    per whisker, on held-out predictions from the three-fold doubly held-out cross validation.\n    Needs curated dataset 1 and the predictions, not among the listed deposits. Reproduced\n    when all four rates are below 0.2%; blocked when the data are absent.\n- id: tracking-error-challenge\n  statement: Error rates rise with each later set of challenge frames (curated datasets 2 to 5),\n    and the most common error is the false negative.\n  source: Technical Validation, Validation of pose tracking data, paragraph 4; Fig. 2c\n  quote: Paradoxically, error rates increase with each subsequent set of challenge frames ...\n    The most common type of error is the false negative\n  depends_on:\n  - tracking-error-dataset1\n  criterion: As in tracking-error-dataset1, on curated datasets 1 to 5. The paper does not say\n    whether \"error rates\" means each type or their total; readings are (a) the total of the\n    four types, (b) each type. Reproduced when the rate rises from each set to the next and the\n    false negative is the largest type in each set, under both readings; blocked as\n    methods_underspecified when they disagree; blocked when the data are absent.\n- id: prior-task-strategies\n  statement: In the original study, shape discrimination mice compared the prevalence of\n    contacts across whiskers, while shape detection mice responded to the total number of\n    contacts across all whiskers.\n  source: Background & Summary, paragraph 3 (findings of ref. 8)\n  quote: We found that shape discrimination mice compared the prevalence of contacts across\n    whiskers, a comparison computation enabled by tuning changes in the barrel cortex. In\n    contrast, shape detection mice simply responded to the total number of contacts across all\n    whiskers\n  criterion: A finding of ref. 8 (Rodgers et al. 2021, Neuron 109, 2308), restated here\n    without any method; this paper gives no model, selection or test for it. Blocked as\n    methods_underspecified under this claims file; a test needs the methods of ref. 8.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000231/10.1038-s41597-022-01728-1.yaml paper/10.1038-s41597-022-01728-1.txt; python3 -c "
import yaml;d=yaml.safe_load(open('claims/000231/10.1038-s41597-022-01728-1.yaml'))
import re
for c in d['claims']:
  for k,v in c.items():
    if isinstance(v,str) and (': ' in v or '—' in v or 'rather' in v): print(c['id'],k)
print(len(d['claims']))"; grep -n "—\|rather" claims/000231/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/000231 && python3 - <<'EOF'
p='10.1038-s41597-022-01728-1.yaml'
s=open(p).read()
rep=[("""  statement: The dataset has one folder per mouse with one NWB file per session named
    sub-<mouse>_ses-<session>_behavior+image(.nwb, with ecephys when neural data are present),
    the video of each session in a folder of the same name, and raw neural data under
    sourcedata.""","""  statement: The dataset has one folder per mouse with one NWB file per session, named
    sub-<mouse>_ses-<session>_behavior+image.nwb with "ecephys" added when neural data are
    present, the video of each session in a folder of the same name, and raw neural data under
    sourcedata."""),
("""    for either detection; the input is read as low below half its range, and a frame as dark
    when its mean brightness is below half the session median, a standard choice that is not
    the paper's.""","""    for either detection. The input is read as low below half its range, and a frame as dark
    when its mean brightness is below half the session median; these are standard choices, not
    the paper's, and cannot change the outcome, as the paper says the video goes completely
    black and the input is a digital line. Detections are matched to trials by the intervals
    between trial starts (Methods, Alignment)."""),
("""    holds them, a line is fit from behavioral to video trial starts per session; reproduced
    when the residuals exceed one frame (5 ms) in most sessions and are autocorrelated over
    trials (lag-1 autocorrelation above 0.5, a standard choice, the paper gives no measure).
    Otherwise blocked.""","""    holds them, a line is fit from behavioral to video trial starts per session; reproduced
    when the largest residual exceeds one frame (5 ms), the bound the neural fit meets, in
    more than half the sessions. The paper gives no measure of "slowly but predictably"; the
    residuals are plotted against trial for every session and that part does not enter the
    outcome. Otherwise blocked."""),
]
for a,b in rep:
    assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
EOF
cd ../.. && python tools/claims_check.py claims/000231/10.1038-s41597-022-01728-1.yaml paper/10.1038-s41597-022-01728-1.txt && git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/000231/10.1038-s41597-022-01728-1.yaml`. The quote checker passes: 38 claims, 38 quotes, 0 problems. Nothing is committed.

**Text read.** I used the version of record (Sci Data 9, 620; Europe PMC full text) for the Methods, Data Records, Technical Validation, Usage Notes, Tables 1 to 6 and the figure legends. The paper is a data descriptor with no supplement. No PDF was stored, so I saw no figure; Fig. 2c is known only from its legend and the text. I compared the bioRxiv preprint (v1) only for the reported counts, which are the same in both.

**Code read.** github.com/cxrodgers/NwbDandiData2022 at commit 33d610b holds only `UsageNotes.ipynb`. Its outputs use different NWB names from the paper's text: it reads `processing['behavior']['processed_position_whisker_C2']` and `contacts_by_whisker_C2`, where the text names separate groups such as `processed_whisker_position` and `identified_whisker_contacts`. Table 1 itself says there is one module named "behavior". The criterion for claim nwb-structure accepts either naming. I did not read the tracking forks (PoseTF, whisk), since no criterion rests on them.

**Claims.**
- **Quotes:** all 38 have one; none needed an `inferred` note.
- **Statistics:** none. The paper reports no tests.
- **Criteria:** all 38 have one. They cover:
  - dataset counts and durations;
  - task rules and the trials-table logic;
  - timebase and gap structure;
  - neural timestamps and alignment;
  - unit quality, depth and layer;
  - electrode ordering;
  - pose, contact and file structure;
  - inclusion rules;
  - subject metadata;
  - tracking accuracy;
  - one claim restating findings of the original study (ref. 8), which this paper gives no method for, so it is blocked.

**Details the paper leaves open, with the readings named:**
- **Trials counted in 18,514:** all rows, or rows with `ignore_trial` False.
- **Frames counted in 63,979,800:** the video frame counts, or the pose-series frames.
- **33.8 h of neural recording:** NWB timestamp spans, or the raw Open Ephys main recordings.
- **Timeout:** error trials' (stop_time − choice_time), alone or minus the same value on correct trials.
- **Firing-rate stability bin:** 60 s, or one trial.
- **"Trials to analyse" (90-trial minimum):** `ignore_trial` False, or random non-spoiled trials.
- **≥95% labeled frames:** denominator either the processed-series frames or the video frames. The whiskers counted are C0 to C3, or C1 to C3.
- **Mean tracking error (2.8 px):** curated dataset 1, or all five sets pooled.
- **"Error rates increase":** the total of the four error types, or each type.
- **"Roughly equal" sexes:** a binomial test, or the minority sex being at least one third.
- **"Rarely" for C0 contacts:** read as fewer contacts than each of C1 to C3.

**Thresholds I set myself:** some criteria rest on choices that are mine, not the paper's.
- The pass shares in several criteria (99% or 95% of trials) and the reproduced and partial cut-offs are mine.
- **Sync-pulse detection** uses half-range and half-median-brightness cut-offs. I judged these unable to change the outcome, since the paper says the video goes completely black.
- **"Slowly but predictably" (Arduino clock drift):** I give no measure for it; that part is reported and not judged.

**Missing from the paper's deposits.** Several claims need data the Data Records do not list:
- The curated whisker training sets and held-out predictions, needed by the three tracking-accuracy claims.
- Behavioral trial times in the Arduino timebase, needed by the clock-drift claim.
- Motor onset times, needed by the response-window timing claim.
- The layer boundaries are not printed (only ref. 26 is cited), so that claim checks that layers are consistent with depth.
- The amplitude-based unit-quality criteria lack a detection threshold and units in microvolts; they are reported where possible but do not decide the outcome.

## End of run

21 turns, 6 minutes, result: success.
