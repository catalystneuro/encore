# gonzalez-cabrera-2026 · claims · run 42864301257

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ | grep -i gonzalez; ls claims | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la paper/ | head; ls paper | wc -l; ls paper/*gonzalez* paper/*/ 2>/dev/null | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.02.17.706301.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.02.17.706301.txt",
 "offset": 149
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml | head -150; echo ----; cat papers/datasets/gonzalez-cabrera-2026.yaml; ls datasets 2>/dev/null | grep 001955; grep -rl 001955 --include=*.yaml . | head
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
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cat papers/match/001955.yaml; ls -t claims | head -5
```

```
# Whether each paper DANDI:001955 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dandi
  id: 001955
date: '2026-11-10'
papers:
- doi: 10.64898/2026.02.17.706301
  relation: IsDescribedBy
  checks:
    text: true
    title_in_text: true
    names_this: false
    names_others: []
  verdict: primary
  by: checks
  reason: The archive says the paper describes the dataset, and the paper names no dataset.
zhu-2022.yaml
zhuang-2025.yaml
zhong-2026.yaml
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001955/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin);m=d.get('metadata',d);print(m.get('name'));print(m.get('description'))"; git ls-remote https://github.com/CGonzC/VTAPnO_Locomotion_Analysis
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/CGonzC/VTAPnO_Locomotion_Analysis code && cd code && git checkout -q v1.0_manuscript_submission && git log -1 --format='%H %ad' && find . -path ./.git -prune -o -type f -print | head -100 && git diff --stat v1.0_manuscript_submission main | tail -5
```

```
1ff5196e20fdaa86dd1b6d1efc26a981fb1e09ab Mon Feb 16 20:06:10 2026 +0100
./requirements.txt
./notebooks/Fiber_Photometry_PSTH.ipynb
./notebooks/.gitkeep
./notebooks/Backward_Loc_min.ipynb
./README.md
./matlab/optoTag_classification_unifiedCriteria_v2.m
./matlab/.gitkeep
 .../optotag/optotag_unified_6ms_fixed.csv          |     45 +
 output_examples/photometry/.gitkeep                |      1 +
 output_examples/photometry/psth_dff_rec1.png       |    Bin 0 -> 121275 bytes
 requirements.txt                                   |     14 +-
 23 files changed, 713354 insertions(+), 208 deletions(-)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat README.md && git diff --stat v1.0_manuscript_submission main && git log --oneline main | head
```

```
# VTAPnO_Locomotion_Analysis

Jupyter notebooks for behavioral, photometry, and electrophysiology analyses used in the VTAPnO pathway study.

## Contents
- Open-field locomotion direction classification from DeepLabCut tracking
- Fiber photometry PSTH processing (ΔF/F, z-scoring, peri-stimulus alignment)
- Opto-tagging classification (MATLAB)

## Usage
1. Install required Python packages (see `requirements.txt`).
2. Place input files in `data/raw/` (not included).
3. Run notebooks in `notebooks/` top-to-bottom.

## Notes
This repository contains analysis code only. Raw data are not included.
 License                                            |     22 +
 README.md                                          |     68 +-
 examples/behavior/1.h5                             |    Bin 0 -> 809488 bytes
 examples/behavior/README.md                        |     58 +
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat matlab/optoTag_classification_unifiedCriteria_v2.m; git diff v1.0_manuscript_submission main -- matlab/
```

```
%% ====================  OPTOTAGGING — Unified (2ms vs 6ms)  ====================
% Switch between two criteria with 'criterion':
%   '2ms_peak_anywhere'  -> Cerniauskas 2019
%   '6ms_fixed'          -> De Jong 2024 (orthodromic)
%
% Both modes:
%   - Build null by circularly shuffling trials 10,000× in 0–100 ms window
%   - Threshold = 99.9th percentile of shuffled maxima (matching window width)
%   - Fidelity exclusion (>= 0.1) uses the same window as the criterion
%
% I/O:
%   - Input spikes CSV: first row = neuron IDs, subsequent rows = spike times (samples)
%   - Input stim MAT: contains 'selectedPoints' (stim times in samples)
%   - Output: CSV summarizing results + quick plots for passing units
% ------------------------------------------------------------------------

%clc; clear; close all;

%% ---------- USER SETTINGS ----------
criterion            = '6ms_fixed';  % '2ms_peak_anywhere' | '6ms_fixed'
[... 240 more lines not kept]
```

**Agent**

Paper full text, Methods and supplementary legends are present. Reading the linked code (tag v1.0_manuscript_submission, 1ff5196) now.

**Agent calls Bash**

```bash
cd $TMPDIR/code && python - <<'EOF'
import json
for nb in ["notebooks/Fiber_Photometry_PSTH.ipynb","notebooks/Backward_Loc_min.ipynb"]:
    d=json.load(open(nb))
    print("=========",nb)
    for c in d["cells"]:
        if c["cell_type"] in("code","markdown"):
            print("---",c["cell_type"]); print("".join(c["source"]))
EOF
```

```
<persisted-output>
Output too large (31.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b9c42bc7-62c8-4339-abd3-f8cb196dd2d1/tool-results/bbqf4xbe6.txt

Preview (first 2KB):
========= notebooks/Fiber_Photometry_PSTH.ipynb
--- markdown
## Fiber Photometry PSTH Analysis

This notebook:

This notebook aligns ΔF/F photometry traces to behavioral or stimulation events,
computes peri-event averages, applies baseline normalization and z-scoring,
and generates trial-averaged summaries.

Input files should be placed in:
data/raw/photometry/

# Tested with Python 3.10
# Required packages: numpy, pandas, matplotlib, scipy

[... 49 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b9c42bc7-62c8-4339-abd3-f8cb196dd2d1/tool-results/bbqf4xbe6.txt"
}
```

```
1	========= notebooks/Fiber_Photometry_PSTH.ipynb
2	--- markdown
3	## Fiber Photometry PSTH Analysis
4	
5	This notebook:
6	
7	This notebook aligns ΔF/F photometry traces to behavioral or stimulation events,
8	computes peri-event averages, applies baseline normalization and z-scoring,
9	and generates trial-averaged summaries.
10	
11	Input files should be placed in:
12	data/raw/photometry/
13	
14	# Tested with Python 3.10
15	# Required packages: numpy, pandas, matplotlib, scipy
16	
17	--- code
18	#CONFIG
19	--- code
20	import os
[... 778 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && git diff v1.0_manuscript_submission main -- notebooks/ | grep -E '^[+-]' | grep -v '"image/png"' | cut -c1-200 | grep -vE '^\+\s+"[A-Za-z0-9+/=]{60,}' | head -150
```

```
--- a/notebooks/Backward_Loc_min.ipynb
+++ b/notebooks/Backward_Loc_min.ipynb
-   "metadata": {},
+   "metadata": {
+    "editable": true,
+    "slideshow": {
+     "slide_type": ""
+    },
+    "tags": []
+   },
-    "scrolled": true
+    "editable": true,
+    "scrolled": true,
+    "slideshow": {
+     "slide_type": ""
+    },
+    "tags": []
-    "data_directory = r'data/raw/'\n",
+    "data_directory = \"examples/behavior\"\n",
-    "# Loop over animals (MouseID from 1 to 8)\n",
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && git show main:notebooks/Fiber_Photometry_PSTH.ipynb | grep -nE 'pre_time=|baseline_end=|post_time=' | head; git show main:notebooks/Backward_Loc_min.ipynb | grep -nE 'threshold|window_size =' | head
```

```
325:    "                     pre_time=-3.0, post_time=6.0, baseline_end=-0.1,\n",
421:    "                            pre_time=-3.0, post_time=6.0, baseline_end=-0.1,\n",
453:    "            pre_time=pre_time, post_time=post_time, baseline_end=baseline_end,\n",
624:    "    pre_time=-3.0,\n",
625:    "    post_time=6.0,\n",
626:    "    baseline_end=-0.1,\n",
18:    "Movement direction is computed from the angle between the movement vector (Back displacement) and the body-axis vector (Tailbase→Back), with a speed threshold applied to exclude low-motion frames.\n",
61:    "# Angle thresholds\n",
62:    "forward_threshold = 60\n",
63:    "backward_threshold = 120\n",
65:    "# Speed threshold\n",
66:    "speed_threshold = 0.2  # Adjust as appropriate\n",
112:    "    window_size = 6  # Adjust window size as needed\n",
130:    "    # Set a speed threshold to exclude insignificant movements\n",
131:    "    significant_movement = movement_magnitude >= speed_threshold\n",
161:    "    backward_movement = (angles_deg > backward_threshold) & significant_movement\n",
Shell cwd was reset to
```

**Agent calls Bash**

```bash
head -80 claims/zhong-2026.yaml; grep -hoE '^\s+[a-z_]+:' claims/*.yaml | sort | uniq -c | sort -rn | head -40; ls tools | grep -i claim
```

```
# Claims for Zhong, Katkov & Tsodyks (2026), "Synaptic Theory of Chunking in Working Memory",
# eLife, doi:10.7554/elife.109538, tested on DANDI:000207.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read. paper/10.7554-elife.109538.txt, fetched from eLife's site. Its header says
# "version of record", but the page it holds is the eLife Reviewed Preprint version 1
# (doi:10.7554/eLife.109538.1, 9 January 2026, "Not revised"). It holds the main text, the
# Methods (sections A to E), the legends of Figures 1 to 4 and of the supplementary Figures S1
# to S3, and the Data availability statement. No PDF was supplied. The equations (1) to (15)
# and the values of Table I (simulation parameters) did not survive extraction; Eq. (1) is
# known from the text as M* = 2^(C-1) ("M ∗ = 24−1 = 8" for C = 4, and "M ∗ = 2C−1" in the
# Figure 4 legend, superscripts lost). Figure axes and plotted values could not be read.
#
# Code. The paper links none. Data availability says "The code for simulation will be made
# available in a Github repository at a later stage"; no analysis code for Figure 3 or Figure 4
# is named. No repository or commit was read.
#
# Data the paper used.
# - Figures 1, 2 and S1, S2 are numerical simulations of the rate model of Methods A, with the
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
grep -h -B2 -A4 '^  where:' claims/*.yaml | head -30; grep -h -A6 '    ci:' claims/*.yaml | head -14; grep -h -B1 -A3 'about:' claims/*.yaml | head -12; sed -n 1,60p tools/claims_check.py
```

```
50% of the granule cell population ( Extended data Fig. 3 )
  data: elsewhere
  where: GitHub braingeneers/AndrewsGengVoitiukEtAl_SourceCode at commit 6865bf68cc3c8ea36a9b4f853b9248288fa1e52b,
    Simulation directory (model code, rerun)
  criterion: Run Simulation/simulation.py as published (NEST 3.4, NESTML, 1000 granule and 12
    basket cells, channel reversal -85 mV, 20 pS, decay 50 ms, first second discarded; Methods,
    Simulation Prototype) with the opsin fraction 0, 0.10, 0.25 and 0.50. The measure of
--
    mean of 1,683 features.
  data: elsewhere
  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
  expected:
  - quantity: Nuclei after quality control
    value: 12065
    tolerance: 1206.5
--
    Aldh1a1-expressing neurons.
  data: elsewhere
  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
  depends_on:
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));
c=s['\$defs'] if '\$defs' in s else s.get('definitions');print(list(c.keys()) if c else '');
print(json.dumps(s,indent=1)[:5000])"
```

```
['expected', 'statistic']
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));
p=s['properties']['claims']['items']['properties']
for k in list(p)[list(p).index('where'):]: print(k, json.dumps(p[k])[:400])
print(json.dumps(s['\$defs'],indent=0)[:3000])
print([k for k in s['properties']])"
```

```
where {"description": "For a claim with data `elsewhere`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.", "type": "string", "minLength": 1}
datasets {"description": "Only when the paper is tested on more than one dataset: the folder names of those this claim rests on.", "type": "array", "items": {"type": "string"}, "minItems": 1}
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
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
grep -h -i -B3 's\.e\.m\.' claims/*.yaml | grep -iE 'toleran|s\.e\.m' | head -15
```

```
Reproduced when in each of the nine responses the mean forecast R minus 2 s.e.m. over its
    windows is above 0 (Figure 6D shows means plus or minus 2 s.e.m.; "accurately" is otherwise
  - quantity: Shepherding events per hour with pups present (Extended Data Fig. 3b, mean +/- s.e.m.,
    Reproduced when, in the mean over mice (the panels show mean ± s.e.m.), P(switch) over the
    the mean ± s.e.m. over mice, so the rule is now on the mean, with per-mouse values reported.
    against 0.25 +/- 0.02, mean +/- s.e.m., P < 0.01).
  quote: "exhibited higher early selectivity (PTupper: 0.41 ± 0.04; mean ± s.e.m.; PTlower: 0.25 ± 0.02;
    tolerance: 0.02
  criterion: Tolerances are the reported s.e.m. The paper does not define "early selectivity" or name
    (PTupper: 64.4 ± 1.0%; PTlower: 58.9 ± 0.6%, mean ± s.e.m.; P = 1 × 10−4, two-sided Mann–Whitney test).
    match under one. Mean tolerances are the reported s.e.m. Reproduced when all four
    21 of the most predictive neurons (PTupper: 62.7 ± 1.1%; PTlower: 56.7 ± 0.4%, mean ± s.e.m.; P = 9 × 10−7,
    counts. Removed the statistic field, which held group means and s.e.m., not a test statistic; the means are in
    p < 0.05, the paired t-test on SOM- rates gives p >= 0.05, and the values are within tolerance
    (the stated spread, s.e.m. per the legend). The evoked-firing panels (2J, 2K) name no test,
```

**Agent calls Write**

```json
{
 "file_path": "claims/gonzalez-cabrera-2026.yaml",
 "content": "# Claims for Gonzalez-Cabrera et al. (2026), \"A VTA-pontine GABA pathway biases locomotor\n# direction via local and distal inhibition\", doi:10.64898/2026.02.17.706301, tested on\n# DANDI:001955.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read. paper/10.64898-2026.02.17.706301.txt, the bioRxiv preprint, version 1, flattened\n# from bioRxiv's JATS XML. Its title line reads \"biases backward locomotion\"; the registry title\n# reads \"biases locomotor direction\". It holds the main text, the figure legends of Figures 1\n# to 4, the Methods, and the legends of Supplementary Figures 1 to 4. No PDF was supplied, so\n# figure panels were not seen; the reference list is empty in the text. Every claim rests on a\n# sentence of the main text, a legend or the Methods.\n#\n# Code. The paper links github.com/CGonzC/VTAPnO_Locomotion_Analysis, release\n# \"v1.0_manuscript_submission\", read at that tag, commit\n# 1ff5196e20fdaa86dd1b6d1efc26a981fb1e09ab. It holds three files: notebooks/Backward_Loc_min.ipynb\n# (open-field DLC frame classification, 200-ms peri-stimulus bins, a linear mixed model\n# Proportion ~ Time_bin * MovementType with mouse as group), notebooks/Fiber_Photometry_PSTH.ipynb\n# (405-to-470 robust linear fit, dF/F, per-trial baseline-subtracted dF/F, mean/SD z-score and\n# median/MAD robust z-score, AUC per 1-s bin) and matlab/optoTag_classification_unifiedCriteria_v2.m\n# (opto-tag shuffle test, 6-ms fixed window and fidelity). The branch main (b3b3628) adds example\n# inputs and reformats the same code; no parameter changes. No code for the per-bin statistics,\n# the frequency-screen mixed model, the auROC activation criterion, the temporal classes, the\n# direction analysis, the waveform metrics or the 2-ms DA analysis is in the repository.\n# Where the code and the Methods differ (named in the claims concerned):\n# - Photometry z-score baseline. Methods, −1.0 to −0.1 s; code, pre_time −3.0 to −0.1 s. The\n#   Methods reading is primary, the code's a variant.\n# - Open-field tracking. Methods, likelihood filter p ≥ 0.9 and gap filling; the code applies\n#   neither (it smooths raw DLC positions with a 6-frame moving average, np.convolve mode\n#   \"same\"). The Methods reading is primary, the code's a variant.\n# - Opto-tagging. Methods add a third, waveform-stability criterion (pre/post Pearson r ≥ 0.90);\n#   the MATLAB script has only the shuffle test and fidelity. The Methods are followed.\n#\n# Data the paper used, as it reports them.\n# - Juxtacellular recordings and Neurobiotin fills in urethane-anaesthetised mice (Fig. 1,\n#   Supplementary Fig. 1): 42 neurons; 32 recovered TH− neurons (20 local-and-projection, LP;\n#   12 projection-only, PO) and 10 TH+ neurons; 200-s baseline and three 15-s hindpaw pinches.\n#   Gad2-Cre bulk tracing with AAV-DIO-mNeon (Fig. 1a).\n# - Ex vivo slices (Fig. 2a-c, Supplementary Fig. 2a-c): C57BL/6 mice (n = 5), retroAAV-Cre in\n#   PnO and DIO-ChR2-mCherry in VTA; whole-cell recordings of light-evoked IPSCs in putative DA\n#   and putative GABA VTA neurons (control n = 14, cocktail n = 9 for latency).\n# - Open-field optogenetics (Fig. 2d-i, Supplementary Fig. 2d-f): somatic stimulation of VTA-PnO\n#   neurons (retroAAV-Flp in PnO, Flp-dependent Chrimson in VTA; 3 s of 635-nm light every 10 s\n#   in 5-min sessions; n = 8; the Fig. 2d legend says retroAAV-Flp, the Methods describe it in\n#   DAT-Cre mice, and Supplementary Fig. 2d calls the group DAT-Cre); terminal stimulation of\n#   Gad2-Cre VTA GABA axons in PnO (DIO-ChR2, 3 s of 60-Hz 470-nm light; n = 5); a frequency\n#   screen at 20 to 60 Hz and continuous light. DeepLabCut tracking at 30 fps (nose, back, tail\n#   base).\n# - Fiber photometry (Fig. 3a-c, Supplementary Fig. 3a): DAT-Cre mice with retroAAV-FlpO in PnO,\n#   Flp-dependent Chrimson and DIO-GCaMP8f in VTA (opsin n = 5) and controls with a DIO-mCherry\n#   virus in place of the GCaMP-plus-opsin pair (n = 3; the control virus list is as written in\n#   the Methods); freely moving; 470-nm and 405-nm channels; Chrimson driven at 568 nm; 5, 10, 20\n#   Hz trains and continuous light, 3 s.\n# - Acute silicon-probe recordings (Fig. 3d-k, Supplementary Fig. 3b-d): isoflurane-anaesthetised\n#   DAT-Cre mice (n = 7), ChR2 in DA neurons and Chrimson in VTA-PnO neurons; 64-channel optrodes,\n#   3-4 penetrations per mouse; tagging with 1-ms pulses at 5 Hz (3 s on, 10 s off, 210 pulses),\n#   470 nm for DA and 635 nm for VTA-PnO; then 1-s continuous 635-nm light every 10 s for 3 min.\n#   173 tagged VTA-PnO and 30 tagged DA units. Kilosort and Phy curation; 30 kHz.\n# - Chronic silicon-probe recordings (Fig. 4, Supplementary Fig. 4): DAT-Cre mice (n = 3) with the\n#   same two opsins and a 32-channel optrode; tagging as above; then a rotarod turned for 2 s at\n#   2 rad/s, in reverse (backward stepping) and, in separate blocks, forward. 40 tagged VTA-PnO\n#   units; 17 units in one bidirectional session per mouse.\n#\n# The dandiset's description lists acute electrophysiology, chronic electrophysiology during\n# forward and reverse rotarod locomotion, and fiber photometry at 5, 10, 20 Hz and continuous\n# stimulation. Claims on the juxtacellular, slice, tracing and open-field experiments are listed\n# because they are main findings; the author finds whether the dandiset holds their data. The\n# paper's Links section names Zenodo doi:10.5281/zenodo.18661700 for \"Figures and KRT\"; the\n# dandiset description names Zenodo doi:10.5281/zenodo.21390830 for figure-level source data and\n# behavioral source data. Neither is said by the paper to hold raw recordings.\n#\n# Method details fixed by the paper for the recorded data in the dandiset. Opto-tagging (Methods,\n# Acute silicon-probe recordings): spikes summed in 0-6 ms after each 1-ms pulse; null from\n# 10,000 circular shuffles of each trial's 0-100 ms spike train, taking the maximum 6-ms count;\n# pass when the real count exceeds the 99.9th percentile; fidelity ≥ 0.1; pre (−180 to 0 ms) and\n# post (0-6 ms) mean waveforms correlated at r ≥ 0.90. The MATLAB script fixes 1-ms bins, shifts\n# drawn uniformly from 1 to 100 bins, a sliding 6-bin maximum for the null, and a strict \">\".\n# Acute activation (Methods, Acute recordings): 0.5-s bins, baseline −1.25 to −0.25 s, auROC per\n# bin, paired two-tailed tests against time-matched baseline, FDR across bins, activated when\n# significant with auROC > 0.5. Chronic activation (Methods, Chronic silicon-probe recordings):\n# 100-ms bins, pooled baseline −1.25 to −0.25 s, six 0.5-s windows W1-W6 over 0-3 s, FDR across\n# windows (and directions), class rules as quoted in the claims. Photometry: Pre −1.0 to −0.1 s,\n# Stim 0-3 s, trials averaged within animal. Details left open are named in each criterion.\nschema_version: 2\npaper: doi:10.64898/2026.02.17.706301\nclaims:\n- id: fig1a-gad2-long-range-projections\n  statement: Bulk labelling of VTA GABAergic neurons in Gad2-Cre mice shows axons across forebrain\n    and brainstem regions, including nucleus accumbens, lateral hypothalamus and PnO.\n  source: Results, VTA outputs previewed by bulk labeling, paragraph 1; Figure 1a\n  quote: we observed widespread axonal labeling across forebrain and brainstem regions, including\n    nucleus accumbens, lateral hypothalamus and PnO\n  criterion: Histology (Methods, Axonal projection quantification; ABBA registration, QuPath mean\n    mNeon intensity minus a local background ROI, averaged per animal and region). Reproduced\n    when the background-corrected mean intensity is above zero in nucleus accumbens, lateral\n    hypothalamus and PnO in every animal. The paper gives no values or animal count.\n- id: fig1-th-neg-all-project\n  statement: All 32 recovered juxtacellularly labelled TH− VTA neurons sent axons outside the\n    VTA.\n  source: Results, VTA outputs previewed by bulk labeling, paragraph 1; Figure 1c\n  quote: Surprisingly, all recovered TH − neurons (32/32) extended axons outside the VTA\n  expected:\n  - quantity: TH− neurons with axons leaving the VTA\n    value: 32\n    tolerance: 0\n    unit: neurons of 32\n  criterion: From the per-neuron target matrix of reconstructed fills (Methods, Three-dimensional\n    reconstructions). The tolerance is 0 because the claim is \"all\".\n- id: fig1-lp-majority\n  statement: Most TH− projection neurons (62%; 20 of 32, the LP group) also had local axon\n    collaterals in the VTA; the other 12 were projection-only (PO).\n  source: Results, VTA outputs previewed by bulk labeling, paragraph 1; Figure 1c,e legend\n  quote: The majority of them (62%) also formed local collaterals in the VTA, consistent with a\n    dual projection architecture\n  expected:\n  - quantity: fraction of TH− neurons with intra-VTA collaterals\n    value: 62\n    tolerance: 6.2\n    unit: percent\n  - quantity: LP neurons\n    value: 20\n    tolerance: 2\n    unit: neurons\n  - quantity: PO neurons\n    value: 12\n    tolerance: 1.2\n    unit: neurons\n- id: fig1-pno-subset\n  statement: Four of the 32 TH− neurons (12%), all in the LP group, projected to the PnO.\n  source: Results, VTA outputs previewed by bulk labeling, paragraph 1; Figure 1c\n  quote: Among the LP neurons, a subset projected to the PnO (12%, 4/32 TH − ), identifying a VTA\n    PnO subpopulation\n  expected:\n  - quantity: TH− neurons with axons in PnO\n    value: 4\n    tolerance: 0.4\n    unit: neurons of 32\n  criterion: Counted from the target matrix (terminals or en passant profiles in PnO, Figure 1c\n    legend). The paper does not say whether en passant profiles alone count as projecting to\n    PnO; the readings are (a) terminals or en passant, (b) terminals only. Reproduced when 4 of\n    32 neurons, all LP, project to PnO under one reading. 4/32 is 12.5%, printed as 12%.\n- id: supp1d-cv2-lp-po\n  statement: LP TH− neurons fire more irregularly than PO TH− neurons (CV2 0.871 ± 0.069 against\n    0.609 ± 0.116).\n  source: Supplementary Figure 1d, left; Results, VTA outputs previewed by bulk labeling,\n    paragraph 1\n  quote: 'Left: spike-time variability (CV2) across juxtacellularly labeled TH − cells: LP (0.871\n    ± 0.069) vs. PO (0.609 ± 0.116) ( p = 0.0468, unpaired t -test)'\n  statistics:\n  - test: unpaired t-test\n    p: 0.0468\n    n: 20 LP and 12 PO neurons (Figure 1 legend; Supplementary Fig. 1d right has 19 LP)\n  expected:\n  - quantity: CV2, LP\n    value: 0.871\n    tolerance: 0.069\n  - quantity: CV2, PO\n    value: 0.609\n    tolerance: 0.116\n  criterion: Tolerances are the reported s.e.m. (Methods, data are mean ± s.e.m.). CV2 is not\n    defined in the Methods; the standard definition, the mean over consecutive interspike\n    intervals of 2|ISI(n+1) − ISI(n)|/(ISI(n+1) + ISI(n)), is used, on the 200-s baseline\n    (Methods, Juxtacellular recordings). Whether the baseline or the whole recording is used is\n    open; both are run. Reproduced when both means are within tolerance and the unpaired t-test\n    gives p < 0.05 with LP higher, under one reading.\n- id: supp1d-cv2-rate-correlation\n  statement: Within both LP and PO TH− neurons, firing rate falls as spike-time variability\n    rises (Spearman r −0.76 and −0.73).\n  source: Supplementary Figure 1d, right; Results, VTA outputs previewed by bulk labeling,\n    paragraph 1\n  quote: 'relationship between CV2 and mean firing rate of all recorded TH − neurons (LP: Spearman\n    r = −0.76, p = 0.0002, n = 19; PO: r = −0.73, p = 0.0096, n = 12)'\n  statistics:\n  - about: LP\n    test: Spearman correlation\n    statistic: r = −0.76\n    p: 0.0002\n    n: 19 LP neurons\n  - about: PO\n    test: Spearman correlation\n    statistic: r = −0.73\n    p: 0.0096\n    n: 12 PO neurons\n  expected:\n  - quantity: Spearman r, LP\n    value: -0.76\n    tolerance: 0.076\n  - quantity: Spearman r, PO\n    value: -0.73\n    tolerance: 0.073\n  depends_on:\n  - supp1d-cv2-lp-po\n  criterion: CV2 as in supp1d-cv2-lp-po; mean firing rate over the same epoch. The paper does not\n    say which LP neuron is left out (19 of 20); run with all 20 and report. Reproduced when both\n    r values are within tolerance and both p < 0.05.\n- id: fig1e-spike-duration\n  statement: Spikes of TH− neurons, both LP and PO, are shorter in duration than those of TH+\n    (dopaminergic) neurons.\n  source: Figure 1e legend; Results, VTA outputs previewed by bulk labeling, paragraph 1\n  quote: Spike duration was shorter in TH − than in TH + neurons (TH + vs. LP p = 0.0023; TH + vs.\n    PO p = 0.0185; one-way ANOVA, FDR-corrected post hoc tests)\n  statistics:\n  - about: TH+ against LP\n    test: one-way ANOVA, post hoc test\n    p: 0.0023\n    corrected: FDR\n    n: 10 TH+ and 20 LP neurons\n  - about: TH+ against PO\n    test: one-way ANOVA, post hoc test\n    p: 0.0185\n    corrected: FDR\n    n: 10 TH+ and 12 PO neurons\n  criterion: The paper does not define spike duration or the post hoc test. Readings for the\n    measure are (a) the full action-potential width from onset to return to baseline of the\n    average juxtacellular waveform, (b) peak-to-trough width. Post hoc tests are pairwise\n    t-tests (Welch or pooled) with Benjamini-Hochberg FDR over the three pairs. Reproduced when\n    under one reading both TH+ against LP and TH+ against PO give corrected p < 0.05 with TH+\n    longer.\n- id: fig1e-firing-rate-no-difference\n  statement: Baseline firing rate does not differ between LP, PO and TH+ neurons.\n  source: Figure 1e legend; Results, VTA outputs previewed by bulk labeling, paragraph 1\n  quote: Mean firing rate did not differ between cell groups (Kruskal–Wallis test, FDR-corrected\n    post hoc tests)\n  criterion: A claim of absence, judged on the paper's test, a Kruskal-Wallis test across LP (n\n    = 20), PO (n = 12) and TH+ (n = 10) mean rates over the 200-s baseline (Methods,\n    Juxtacellular recordings), at alpha 0.05. Reproduced when it is not significant; not\n    reproduced when it is. The group medians and the effect size are reported either way.\n- id: supp1e-pinch-response-profiles\n  statement: Hindpaw pinch mostly decreases the firing of TH+ neurons, while TH− neurons show\n    both increases and decreases.\n  source: Supplementary Figure 1e, left and centre; Results, VTA outputs previewed by bulk\n    labeling, paragraph 1\n  quote: 'TH+ cells showed predominant decreases in firing rate, whereas TH − neurons exhibited\n    heterogeneous rate changes (both increases and decreases)'\n  criterion: Classification as in Methods, Juxtacellular pinch, 1-s bins over −20 to +20 s\n    from pinch onset, baseline −10 to 0 s, Stim 0-15 s; responsive with at least two consecutive\n    FDR-significant Stim bins (excited, inhibited, or mixed). The per-bin test is not named;\n    readings are (a) each bin's counts over the three pinch trials against the baseline bins by\n    Mann-Whitney, (b) a z-test of each bin against the baseline mean and SD. Reproduced when\n    under one reading inhibited is the largest class among TH+ neurons and TH− neurons include\n    both excited and inhibited cells.\n- id: supp1e-pinch-rate-th-pos-lower\n  statement: The firing rate in response to hindpaw pinch is lower in TH+ neurons than in TH−\n    neurons.\n  source: Supplementary Figure 1e, right\n  quote: 'Right: mean firing rate in response to paw pinch is lower for TH + ( n = 9) than TH − (\n    n = 31) cells ( p = 0.021, Mann–Whitney test)'\n  statistics:\n  - test: Mann-Whitney\n    p: 0.021\n    n: 9 TH+ and 31 TH− neurons\n  criterion: Stim window 0-15 s and baseline −10 to 0 s (Methods, Juxtacellular pinch). The\n    measure is not defined; readings are (a) mean rate in 0-15 s, (b) that minus the baseline\n    rate, (c) the mean peri-event z-score in 0-15 s (Supplementary Fig. 1e centre is z-scored).\n    Each neuron's value is its mean over the three pinches. Reproduced when under one reading\n    the Mann-Whitney test gives p < 0.05 with TH+ lower.\n- id: supp1f-pinch-burst-th-pos-lower\n  statement: Pinch-evoked bursting is lower in TH+ neurons than in TH− neurons.\n  source: Supplementary Figure 1f; Results, VTA outputs previewed by bulk labeling, paragraph 1\n  quote: 'Right: mean firing rate of bursting activity in response to paw pinch is lower for TH +\n    ( n = 8) than TH − ( n = 18) cells ( p = 0.047, Mann–Whitney test)'\n  statistics:\n  - test: Mann-Whitney\n    p: 0.047\n    n: 8 TH+ and 18 TH− neurons\n  criterion: The paper gives no burst definition. Readings are (a) for TH+ neurons the standard\n    dopamine-neuron rule (burst onset at an ISI ≤ 80 ms, end at an ISI > 160 ms) and the same\n    rule for TH− neurons, (b) a rate-independent rule (Poisson surprise). The measure is the\n    rate of spikes in bursts in 0-15 s, read as in supp1e-pinch-rate-th-pos-lower (raw, minus\n    baseline, or z-scored). Neurons with no bursts are left out (n = 8 and 18 of 9 and 31).\n    Reproduced when under one reading the Mann-Whitney test gives p < 0.05 with TH+ lower.\n- id: fig2a-local-oipsc\n  statement: Light activation of the local axons of PnO-projecting VTA neurons in slices evokes\n    IPSCs in both putative dopaminergic and putative GABAergic VTA neurons.\n  source: Results, A VTA GABA subpopulation combines long-range output, paragraph 1; Figure 2a\n  quote: Brief photostimulation evoked optical IPSCs in dopaminergic and putative GABAergic neurons\n    in the VTA\n  criterion: Whole-cell recordings at −60 mV with high-chloride internal (Methods, Ex-vivo\n    electrophysiology). Reproduced when light-evoked inward currents locked to 5-ms pulses are\n    present in cells of both putative types (classified as in fig2b-intrinsic-separation).\n- id: fig2c-gabaa-monosynaptic\n  statement: The light-evoked IPSCs persist with TTX and 4-AP (monosynaptic) and are abolished by\n    picrotoxin (GABA-A).\n  source: Figure 2c legend; Results, A VTA GABA subpopulation combines long-range output,\n    paragraph 1\n  quote: Single-pulse IPSCs persist in control and cocktail conditions (CNQX + D-AP5 + 4-AP + TTX)\n    but are abolished by picrotoxin, indicating monosynaptic GABA A transmission\n  criterion: Reproduced when in the cells tested, oIPSC amplitude in TTX plus 4-AP stays above\n    noise and in picrotoxin (100 µM) falls to noise. Noise is read as the SD of the 50 ms before\n    the pulse, and \"above noise\" as a peak over 3 SD; these thresholds are not in the paper.\n- id: fig2c-latency-cocktail\n  statement: IPSC peak delay is longer in the TTX/4-AP cocktail (5.09 ms) than in control (3.32\n    ms).\n  source: Figure 2c legend; Results, A VTA GABA subpopulation combines long-range output,\n    paragraph 1\n  quote: IPSC peak delay is increased in cocktail (5.09 ± 0.26 ms, n = 9) vs. control (3.32 ± 0.14\n    ms, n = 14; unpaired t -test, p < 0.0001)\n  statistics:\n  - test: unpaired t-test\n    p: 0.0001\n    p_relation: <\n    n: 9 cocktail and 14 control cells\n  expected:\n  - quantity: IPSC peak delay, cocktail\n    value: 5.09\n    tolerance: 0.26\n    unit: ms\n  - quantity: IPSC peak delay, control\n    value: 3.32\n    tolerance: 0.14\n    unit: ms\n  criterion: Tolerances are the reported s.e.m. Delay is from light onset to IPSC peak (legend,\n    \"peak delay\"); the Results speak of synaptic latency from light-on, which reads as onset.\n    Readings are (a) light onset to peak, (b) light onset to IPSC onset. Reproduced when under\n    one reading both means are within tolerance and the unpaired t-test gives p < 0.0001.\n- id: fig2b-intrinsic-separation\n  statement: AP half-width, Ih and AHP area separate putative DA from putative GABA neurons in\n    the slice recordings.\n  source: Figure 2b legend\n  quote: Intrinsic properties (AP half-width, I h , AHP area) separate putative DA from putative\n    GABA neurons ( p = 0.0012, p = 0.0012, p = 0.0105, respectively; unpaired t -tests)\n  statistics:\n  - about: AP half-width\n    test: unpaired t-test\n    p: 0.0012\n  - about: Ih\n    test: unpaired t-test\n    p: 0.0012\n  - about: AHP area\n    test: unpaired t-test\n    p: 0.0105\n  criterion: Cells are typed by location and Ih with slow firing under 5 Hz (Methods, Ex-vivo\n    electrophysiology), so the test is partly circular. Ih, half-width and AHP area are not\n    defined further; readings for Ih are the sag current at the end of a step to −120 mV or the\n    largest step used. Reproduced when all three unpaired t-tests give p < 0.05.\n- id: supp2c-oipsc-depression\n  statement: Repeated light trains at several frequencies evoke reliable oIPSCs whose amplitude\n    decreases along the train.\n  source: Results, A VTA GABA subpopulation combines long-range output, paragraph 1;\n    Supplementary Figure 2b,c\n  quote: Repetitive stimulation trains at various frequencies, evoked reliable oIPSCs with\n    decreasing amplitude\n  criterion: Trains at 8, 20 and 50 Hz (Supplementary Fig. 2c). Reproduced when for each\n    frequency every pulse evokes an oIPSC and the mean normalised amplitude of the last pulse is\n    below that of the first.\n- id: fig2e-somatic-backward\n  statement: Continuous 3-s red-light stimulation of VTA-PnO cell bodies drives backward walking\n    in the open field, with a sharp onset peak in backward movement that declines during the\n    light and falls below baseline after offset, while forward movement moves inversely.\n  source: Results, Optogenetic activation of the VTA PnO pathway, paragraph 1; Figure 2e\n  quote: The population PSTH (peristimulus time histogram) showed a sharp onset peak in the\n    backward movement ratio (blue) that declined across the 3-s light window and fell below\n    baseline after offset, while forward movement (green) shows inverse relation\n  depends_on:\n  - fig2f-somatic-bins\n  criterion: Frame classification from the Methods (Open-Field; Open-field video) and the\n    notebook Backward_Loc_min.ipynb, DLC back and tail base, likelihood ≥ 0.9, gap filled,\n    6-frame moving average, movement vector of Back between consecutive frames, body axis tail\n    base to back, speed gate ≥ 0.2 px per frame, forward < 60°, backward > 120°; 200-ms bins over\n    −1 to +4 s, proportion per trial, averaged per mouse, then over mice (n = 8). Gap filling is\n    not specified (linear interpolation is used, a standard choice); the notebook applies no\n    likelihood filter, run as a variant. Reproduced when the mouse-averaged backward proportion\n    peaks in 0-1 s, is lower in 2-3 s than in 0-1 s, and is below the pre-stimulus mean in 3-4\n    s, and the forward proportion is lower in 0-1 s than before the light.\n- id: fig2f-somatic-bins\n  statement: With somatic stimulation, the backward movement ratio exceeds baseline in the 0-1 s\n    and 1-2 s bins, does not differ at 2-3 s, and falls below baseline at 3-4 s.\n  source: Figure 2f legend; Results, Optogenetic activation of the VTA PnO pathway, paragraph 1\n  quote: Backward ratio exceeded baseline at 0–1 s and 1–2 s ( p < 0.0001 and p = 0.0088,\n    respectively), dropped to baseline at 2–3 s ( p = 0.086), and fell below baseline at 3–4 s (\n    p = 0.04; one-way ANOVA with repeated measures, FDR-corrected post hoc tests)\n  statistics:\n  - about: 0-1 s against baseline\n    test: one-way repeated-measures ANOVA, post hoc test\n    p: 0.0001\n    p_relation: <\n    corrected: FDR\n    n: 8 mice\n  - about: 1-2 s against baseline\n    test: one-way repeated-measures ANOVA, post hoc test\n    p: 0.0088\n    corrected: FDR\n    n: 8 mice\n  - about: 2-3 s against baseline\n    test: one-way repeated-measures ANOVA, post hoc test\n    p: 0.086\n    corrected: FDR\n    n: 8 mice\n  - about: 3-4 s against baseline\n    test: one-way repeated-measures ANOVA, post hoc test\n    p: 0.04\n    corrected: FDR\n    n: 8 mice\n  criterion: Frames classified as in fig2e-somatic-backward; per mouse, the backward proportion\n    in each 1-s bin from light onset (0-1, 1-2, 2-3 during light, 3-4 after offset) and in the\n    baseline. The legend's \"light stimulation at 1-3 s\" cannot be the time base, since 0-1 s then\n    precedes the light; bins are read from light onset, as in the Results. Open details, all run\n    (a) baseline −1 to 0 s (the peri-stimulus window of Methods, Open-Field) or −1.0 to −0.1 s\n    (the frequency screen's baseline); (b) correction, FDR as in the legend or Holm as in the\n    Methods (\"Per-bin (1-s) open-field comparisons ... used Holm step-down across bins\"); (c)\n    post hoc tests as paired t-tests of each bin against baseline. Reproduced when under one\n    reading 0-1 s and 1-2 s are above baseline with corrected p < 0.05, 2-3 s is not significant,\n    and 3-4 s is below baseline with p < 0.05. Partially reproduced when the 0-1 s and 1-2 s\n    results hold and one of the other two does not.\n- id: fig2h-terminal-backward\n  statement: 60-Hz blue-light stimulation of VTA GABA terminals in PnO in Gad2-Cre mice also\n    triggers backward walking, with a transient rise in the backward ratio that returns to\n    baseline after the light.\n  source: Results, Optogenetic activation of the VTA PnO pathway, paragraph 1; Figure 2h\n  quote: This stimulation likewise triggered backward walking and yielded a transient increase in\n    the backward movement ratio that returned to baseline after the stimulus\n  depends_on:\n  - fig2i-terminal-bins\n  criterion: Classification as in fig2e-somatic-backward, n = 5 Gad2-Cre mice, 3-s 60-Hz 470-nm\n    trains. Reproduced when the mouse-averaged backward proportion is above its pre-stimulus mean\n    in each 1-s bin of 0-3 s and within the pre-stimulus range (mean ± 2 s.e.m. over mice) in 3-4\n    s; the 2 s.e.m. band is the reader's choice.\n- id: fig2i-terminal-bins\n  statement: With PnO terminal stimulation, the backward ratio is above baseline at 0-1, 1-2 and\n    2-3 s and not different from baseline at 3-4 s.\n  source: Figure 2i legend; Results, Optogenetic activation of the VTA PnO pathway, paragraph 1\n  quote: Backward ratio was above baseline at 0–1 s, 1–2 s, and 2–3 s ( p = 0.0006, p = 0.0194,\n    and p = 0.03, respectively) and not different from baseline at 3–4 s ( p = 0.33\n  statistics:\n  - about: 0-1 s against baseline\n    test: one-way repeated-measures ANOVA, post hoc test\n    p: 0.0006\n    corrected: FDR\n    n: 5 mice\n  - about: 1-2 s against baseline\n    test: one-way repeated-measures ANOVA, post hoc test\n    p: 0.0194\n    corrected: FDR\n    n: 5 mice\n  - about: 2-3 s against baseline\n    test: one-way repeated-measures ANOVA, post hoc test\n    p: 0.03\n    corrected: FDR\n    n: 5 mice\n  - about: 3-4 s against baseline\n    test: one-way repeated-measures ANOVA, post hoc test\n    p: 0.33\n    corrected: FDR\n    n: 5 mice\n  criterion: As fig2f-somatic-bins, with the same open readings (baseline −1 to 0 or −1.0 to\n    −0.1 s; FDR or Holm). Reproduced when under one reading the three light bins are above\n    baseline with corrected p < 0.05 and 3-4 s is not significant. Partially reproduced when two\n    of the three light bins hold.\n- id: supp2e-latency-to-peak-backward-similar\n  statement: Latency to peak backward movement is similar for somatic and terminal stimulation\n    (0.425 against 0.404 s).\n  source: Supplementary Figure 2e, lower panel; Results, Optogenetic activation of the VTA PnO\n    pathway, paragraph 1\n  quote: 'both stimulation protocols resulted in a similar latency to peak movement across animals.\n    VTA PnO somatic stimulation (0.425 ± 0.066 s) vs. PnO terminals (0.404 ± 0.035 s) (unpaired t\n    -test, p = 0.8217)'\n  statistics:\n  - test: unpaired t-test\n    p: 0.8217\n    n: 8 somatic and 5 terminal mice\n  expected:\n  - quantity: latency to peak backward ratio, somatic\n    value: 0.425\n    tolerance: 0.066\n    unit: s\n  - quantity: latency to peak backward ratio, terminal\n    value: 0.404\n    tolerance: 0.035\n    unit: s\n  depends_on:\n  - fig2e-somatic-backward\n  - fig2h-terminal-backward\n  criterion: A claim of absence, judged on the unpaired t-test at alpha 0.05; the means are\n    within tolerance (the reported s.e.m.) as well. Latency is not defined. Per mouse, the time\n    of the maximum of the mouse-averaged backward proportion in 200-ms bins within 0-3 s; the\n    readings for the time stamp are (a) bin end (as the notebook labels bins), (b) bin centre,\n    (c) bin start. Reproduced when the t-test is not significant and, under one reading, both\n    means are within tolerance; partially reproduced when the test holds but the means do not.\n- id: supp2f-latency-to-peak-speed\n  statement: Time to maximum speed is shorter for somatic stimulation (0.590 s) than for PnO\n    terminal stimulation (1.164 s).\n  source: Supplementary Figure 2f, lower panel; Results, Optogenetic activation of the VTA PnO\n    pathway, paragraph 1; Discussion, paragraph 5\n  quote: By contrast, the time to maximum speed for VTA somatic stimulation was less than for PnO\n    terminals\n  statistics:\n  - test: unpaired t-test\n    p: 0.0131\n    n: 8 somatic and 5 terminal mice\n  expected:\n  - quantity: latency to peak speed, somatic\n    value: 0.590\n    tolerance: 0.104\n    unit: s\n  - quantity: latency to peak speed, terminal\n    value: 1.164\n    tolerance: 0.184\n    unit: s\n  criterion: The legend says latency \"was higher for VTA PnO somatic stimulation (0.590 ± 0.104\n    s) than PnO terminals (1.164 ± 0.184 s)\", which contradicts its own numbers; the Results and\n    Discussion (≈ 0.6 s against ≈ 1.16 s) say somatic is faster, and that is the statement.\n    Speed is not defined; readings are (a) the magnitude of the smoothed Back displacement per\n    frame on all frames, (b) on frames passing the speed gate, (c) on backward frames only.\n    Latency per mouse is the time of the maximum of the mouse-averaged speed in 200-ms bins\n    within 0-3 s (bin end, centre or start). Reproduced when under one reading both means are\n    within tolerance (the reported s.e.m.) and the unpaired t-test gives p < 0.05 with somatic\n    shorter.\n- id: supp2d-frequency-trend\n  statement: Backward movement during somatic stimulation scales with light frequency, minimal\n    at 20 Hz or below and robust at 60 Hz and continuous light, with a significant linear trend\n    and greater responses at 30-60 Hz than at 20 Hz.\n  source: Results, Optogenetic activation of the VTA PnO pathway, paragraph 1; Supplementary\n    Figure 2d\n  quote: A per-trial mixed-effects model on Δ (backward ratio) showed a significant linear trend\n    across frequencies ( n = 8 mice, 14 trials/mouse). Post-hoc pairwise tests with Holm’s\n    step-down correction indicated that 30–60 Hz elicited greater responses than 20 Hz\n  statistics:\n  - about: linear trend across frequencies\n    test: linear mixed-effects model\n    p: 0.0001\n    p_relation: <\n    n: 8 mice, 14 trials per mouse\n  depends_on:\n  - fig2e-somatic-backward\n  criterion: Methods, Open-field video and frequency screen. Per trial, Δ = mean backward ratio\n    in the stimulus window minus that in the baseline −1.0 to −0.1 s; a mixed model Δ ~\n    frequency with a random intercept per mouse, frequencies 20, 30, 40, 50, 60 Hz; the trend\n    with frequency coded numerically; planned contrasts of each ≥ 30 Hz level against 20 Hz,\n    Holm-corrected. Open details, all run. (a) The window, 0-1 s (initiation) or 1-2 s (early\n    maintenance), both named in the Methods. (b) The mice, 8 (Results) or \"the same three mice\"\n    (Methods). Reproduced when under one reading the trend has p < 0.0001 with Δ rising and each\n    of 30, 40, 50 and 60 Hz exceeds 20 Hz with Holm p < 0.05; partially reproduced when the\n    trend holds and some of the four contrasts do not. The Supplementary Figure 2d legend shows\n    the same screen for Gad2-Cre mice; no result is stated for them.\n- id: supp2d-continuous-vs-60hz\n  statement: For somatic stimulation, continuous light and 60 Hz do not differ in the backward\n    response.\n  source: Results, Optogenetic activation of the VTA PnO pathway, paragraph 1; Supplementary\n    Figure 2d\n  quote: whereas 60 Hz vs. continuous light were not significantly different for VTA somatic\n    stimulation\n  depends_on:\n  - supp2d-frequency-trend\n  criterion: A claim of absence, judged on the paper's test, the per-trial mixed model of Δ with\n    reference 60 Hz and continuous light as the other level (Methods, Open-field video), at alpha\n    0.05, under the readings of supp2d-frequency-trend. Reproduced when not significant under\n    the window and mice reading that reproduces supp2d-frequency-trend (both windows reported\n    when neither does); the effect size is reported.\n- id: fig3b-photometry-continuous-only\n  statement: In opsin mice, VTA-PnO stimulation raises the DA population calcium signal above\n    its pre-stimulus level with continuous light, but not with 5, 10 or 20 Hz trains.\n  source: Figure 3b legend; Results, Optogenetic activation of VTA PnO elevates dopaminergic\n    population signals, paragraph 1\n  quote: Within-opsin pre-post comparison was significant at continuous stimulation, with 5-20 Hz\n    yielding non-significant differences\n  statistics:\n  - about: continuous, Pre against Stim\n    test: two-way ANOVA, post hoc comparison\n    p: 0.0001\n    p_relation: <\n    corrected: FDR\n    n: 5 opsin mice\n  - about: 5, 10 and 20 Hz, Pre against Stim\n    test: two-way ANOVA, post hoc comparison\n    p: 0.05\n    p_relation: '>'\n    corrected: FDR\n    n: 5 opsin mice\n  criterion: Methods, In vivo fiber photometry and Fiber photometry, with the notebook\n    Fiber_Photometry_PSTH.ipynb for preprocessing; 405 fitted to 470 by least squares with\n    three passes trimming residuals over 3 SD, dF/F = (470 − fit)/fit with the denominator\n    floored at 1% of its median; trials aligned to light onset; z-scored per trial; averaged\n    within mouse per condition; Pre = −1.0 to −0.1 s, Stim = 0-3 s; per mouse the mean z in\n    each epoch. Open details, all run. (a) z-score baseline, −1.0 to −0.1 s (Methods; Pre is\n    then 0 by construction for the mean/SD z) or −3.0 to −0.1 s (notebook, a variant). (b)\n    z-score form, mean/SD or median/MAD (the notebook computes both; the Methods say z-scores).\n    (c) The epoch value, the mean over the window or the area (the notebook's AUC). (d) The\n    ANOVA, epoch by frequency with repeated measures on both factors or without; post hoc paired\n    Pre against Stim per frequency, Benjamini-Hochberg over the four. The control mice are not\n    in this test. Reproduced when under one reading continuous gives p < 0.0001 with Stim\n    higher and 5, 10 and 20 Hz each give p > 0.05; partially reproduced when continuous holds at\n    p < 0.05 but not at 0.0001, or one train frequency is significant.\n- id: fig3c-photometry-opsin-vs-control\n  statement: The stimulation-evoked change in DA calcium signal (Stim minus Pre) is larger in\n    opsin mice than in controls for continuous light only, not for 5-20 Hz.\n  source: Figure 3c legend; Results, Optogenetic activation of VTA PnO elevates dopaminergic\n    population signals, paragraph 1\n  quote: change-scores (Δ = Stim-Pre) were larger in the opsin group compared to the controls (n =\n    3) for continuous illumination only, with no effects at 5-20 Hz\n  statistics:\n  - about: continuous, opsin against control\n    test: two-way ANOVA, post hoc comparison\n    p: 0.002\n    corrected: FDR\n    n: 5 opsin and 3 control mice\n  - about: 5, 10 and 20 Hz, opsin against control\n    test: two-way ANOVA, post hoc comparison\n    p: 0.05\n    p_relation: '>'\n    corrected: FDR\n    n: 5 opsin and 3 control mice\n  depends_on:\n  - fig3b-photometry-continuous-only\n  criterion: Δ per mouse and frequency as in fig3b-photometry-continuous-only under the same\n    readings; a two-way ANOVA group by frequency (frequency repeated within mouse, or not);\n    post hoc unpaired opsin against control per frequency, Benjamini-Hochberg over the four.\n    Reproduced when under one reading continuous gives p < 0.05 with opsin larger and 5, 10 and\n    20 Hz each give p > 0.05.\n- id: fig3-optotag-counts\n  statement: Across seven anaesthetised DAT-Cre mice, 173 VTA-PnO units and 30 DA units were\n    opto-tagged.\n  source: Results, Acute opto-tagging reveals transient DA activation, paragraph 1; Figure 3i\n    legend\n  quote: Across seven mice, we isolated 173 opto-tagged VTA PnO neurons and 30 opto-tagged DA\n    neurons\n  expected:\n  - quantity: opto-tagged VTA-PnO units\n    value: 173\n    tolerance: 17.3\n    unit: units\n  - quantity: opto-tagged DA units\n    value: 30\n    tolerance: 3\n    unit: units\n  criterion: The three criteria of Methods, Acute silicon-probe recordings, implemented as the\n    MATLAB script (6ms_fixed; 1-ms bins over 0-100 ms; 10,000 circular shifts drawn from 1 to\n    100 bins per trial; null = sliding 6-bin maximum; real 0-6 ms count > 99.9th percentile;\n    fidelity, the share of pulses with a spike in 0-6 ms, ≥ 0.1), plus the waveform rule\n    (pre −180 to 0 ms and post 0-6 ms mean waveforms, r ≥ 0.90). Pulses are the 635-nm tagging\n    pulses for VTA-PnO and the 470-nm pulses for DA. Open details. (a) Waveform channel, the\n    unit's peak channel or all channels concatenated. (b) A unit passing for both colours; the\n    paper does not say, and such units are reported apart. Reproduced when both counts are\n    within tolerance under one reading; the shuffle has a random seed, a choice that cannot\n    change the count by more than units near threshold, which are reported.\n- id: fig3e-onset-latency\n  statement: Light-evoked spikes of tagged VTA-PnO units have a shorter onset latency (3.82 ms)\n    than those of tagged DA units (4.99 ms).\n  source: Figure 3e legend; Results, Acute opto-tagging reveals transient DA activation,\n    paragraph 1\n  quote: 'Onset latency: DA (4.99 ± 0.24 ms) vs. VTA PnO (3.82 ± 0.07 ms) ( p < 0.0001)'\n  statistics:\n  - test: Mann-Whitney\n    p: 0.0001\n    p_relation: <\n    n: 30 DA and 173 VTA-PnO units\n  expected:\n  - quantity: onset latency, DA\n    value: 4.99\n    tolerance: 0.24\n    unit: ms\n  - quantity: onset latency, VTA-PnO\n    value: 3.82\n    tolerance: 0.07\n    unit: ms\n  depends_on:\n  - fig3-optotag-counts\n  criterion: Tolerances are the reported s.e.m. Onset latency is not defined in the Methods, and\n    the MATLAB script leaves latency undefined for the 6-ms criterion. Readings per unit are (a)\n    the mean first-spike latency in 0-6 ms over pulses with a spike, (b) the median of the same,\n    (c) the mean of all spike times in 0-6 ms (the script's rule for its 2-ms mode). Reproduced\n    when under one reading both means are within tolerance and the Mann-Whitney test gives p <\n    0.0001 with DA longer; partially reproduced when the order and p < 0.05 hold but a mean is\n    out of tolerance.\n- id: fig3f-spike-width\n  statement: Tagged DA units have broader spikes (574.1 µs) than tagged VTA-PnO units (451.5 µs).\n  source: Figure 3f legend; Results, Acute opto-tagging reveals transient DA activation,\n    paragraph 1\n  quote: 'Spike width: DA (574.1 ± 27.3 µ s) vs. VTA PnO (451.5 ± 14.3 µ s) ( p = 0.0002)'\n  statistics:\n  - test: Mann-Whitney\n    p: 0.0002\n    n: 30 DA and 173 VTA-PnO units\n  expected:\n  - quantity: spike width, DA\n    value: 574.1\n    tolerance: 27.3\n    unit: µs\n  - quantity: spike width, VTA-PnO\n    value: 451.5\n    tolerance: 14.3\n    unit: µs\n  depends_on:\n  - fig3-optotag-counts\n  criterion: Tolerances are the reported s.e.m. Spike width is not defined; readings are (a)\n    trough-to-peak time of the mean waveform on the peak channel, (b) full width at half\n    maximum of the trough, (c) the \"AP width\" of Supplementary Fig. 3c, taken as (a). Reproduced\n    when under one reading both means are within tolerance and the Mann-Whitney test gives p <\n    0.05 with DA broader.\n- id: fig3g-firing-rate-no-difference\n  statement: Tagged DA and VTA-PnO units have the same mean firing rate (about 7.1 Hz).\n  source: Figure 3g legend\n  quote: 'Firing rate: DA (7.142 ± 1.02 Hz) vs. VTA PnO (7.162 ± 0.48 Hz) ( p = 0.649)'\n  statistics:\n  - test: Mann-Whitney\n    p: 0.649\n    n: 30 DA and 173 VTA-PnO units\n  expected:\n  - quantity: firing rate, DA\n    value: 7.142\n    tolerance: 1.02\n    unit: Hz\n  - quantity: firing rate, VTA-PnO\n    value: 7.162\n    tolerance: 0.48\n    unit: Hz\n  depends_on:\n  - fig3-optotag-counts\n  criterion: A claim of absence, judged on the Mann-Whitney test at alpha 0.05; means within\n    tolerance (the reported s.e.m.) as well. The epoch is open; readings are (a) the baseline\n    epoch before tagging (Methods, Acute recordings), (b) the whole recording. Reproduced when\n    the test is not significant and, under one reading, both means are within tolerance.\n- id: fig3i-recruitment-beyond-tagged\n  statement: VTA-PnO stimulation modulates many simultaneously recorded VTA units beyond the\n    tagged ones, sharply at light onset.\n  source: Figure 3i legend, left; Results, Acute opto-tagging reveals transient DA activation,\n    paragraph 1\n  quote: Many units show sharp onset modulation, indicating recruitment beyond the opto-tagged\n    subset\n  criterion: Activation as in Methods, Acute recordings (classification of responsive units), on\n    1-s continuous 635-nm light; windows read as in fig3i-da-responsive-subset. \"Many\" is not\n    quantified; the reader sets it at one fifth or more of the untagged units of a session, a\n    threshold not in the paper. Reproduced when in at least one session one fifth or more of the\n    untagged units are activated with the first post-onset window significant. The fraction per\n    session is reported.\n- id: fig3i-da-responsive-subset\n  statement: Some, but not all, tagged DA units are activated by continuous light on VTA-PnO\n    neurons.\n  source: Results, Acute opto-tagging reveals transient DA activation, paragraph 1; Figure 3i\n  quote: a subset of recorded DA units was classified as responsive to VTA PnO stimulation, while\n    the remaining DA units did not meet the criterion\n  depends_on:\n  - fig3-optotag-counts\n  criterion: Methods, Acute recordings; per DA unit, counts in 0.5-s bins after the onset of\n    each 1-s 635-nm pulse, auROC of each bin against baseline −1.25 to −0.25 s, paired\n    two-tailed tests per bin against time-matched baseline, Benjamini-Hochberg over bins,\n    activated when a bin is significant with auROC > 0.5. Open details, all run. (a) The bins,\n    −1 to +1.5 s (Methods; 0-0.5, 0.5-1, 1-1.5 after onset) or six 0.5-s windows over 0-3 s\n    (Results, \"per-unit auROC in six 0.5-s windows\"). (b) Time-matched baseline, per trial the\n    count in a 0.5-s piece of the baseline, or the 1-s baseline count halved. (c) Paired test,\n    paired t-test or Wilcoxon signed-rank. The paper gives no count. Reproduced when under one\n    reading at least one and fewer than 30 DA units are activated; the counts are reported.\n- id: fig3j-vta-pno-light-locked\n  statement: Tagged VTA-PnO units show reliable light-locked activation during continuous light.\n  source: Figure 3j legend; Results, Acute opto-tagging reveals transient DA activation,\n    paragraph 1\n  quote: Population responses show reliable, light-locked VTA PnO (GABA) activation and\n    heterogeneous DA outcomes\n  depends_on:\n  - fig3-optotag-counts\n  criterion: auROC per unit as in fig3i-da-responsive-subset. \"Reliable\" is not quantified; the\n    reader reads it as the mean auROC of the 173 tagged VTA-PnO units in the first post-onset\n    window above 0.5 by a one-sample t-test (the test the paper uses for DA units in Fig. 3j) at\n    p < 0.05, and more than half of them activated. Reproduced when both hold under one reading.\n- id: fig3j-da-onset-transient\n  statement: Responsive DA units show an onset-locked transient, with time-binned auROC above\n    chance.\n  source: Figure 3j legend; Results, Acute opto-tagging reveals transient DA activation,\n    paragraph 1\n  quote: Responsive DA units exhibited an onset-locked signal transient ( p = 0.0013, one-sample t\n    -test against chance)\n  statistics:\n  - test: one-sample t-test against chance\n    p: 0.0013\n    n: responsive DA units (count not given)\n  depends_on:\n  - fig3i-da-responsive-subset\n  criterion: The paper does not say which bin is tested. Readings are (a) the auROC of the first\n    post-onset 0.5-s window across responsive DA units against 0.5, (b) each unit's mean auROC\n    over the post-onset windows against 0.5. Reproduced when under one reading p < 0.05 with\n    auROC above 0.5. The test is on units selected for activation, so it is circular; it is\n    run as the paper ran it.\n- id: fig3k-da-early-timing\n  statement: At 2-ms resolution, responsive DA units rise within about 3 ms of light onset, peak\n    at 7 ms, have a response centroid at 37.8 ms, and increase their firing by 0.50 spikes/s\n    over 0-100 ms.\n  source: Figure 3k legend; Results, Acute opto-tagging reveals transient DA activation,\n    paragraph 1\n  quote: At 2-ms bin resolution, within the set of responsive DA neurons, firing rose within ∼3\n    ms, peaked at 7.0 ms (IQR 2.5-22.5 ms), and had a centroid of 37.8 ms (IQR 35.5-43.6 ms) with\n    a consistent early-window increase (0-100 ms, baseline-subtracted 0.50 spikes·s-1\n  statistics:\n  - about: early-window increase, 0-100 ms\n    test: permutation test\n    p: 0.029\n    ci: {level: 0.95, low: 0.30, high: 0.66, unit: spikes/s}\n    n: responsive DA units (count not given)\n  expected:\n  - quantity: peak latency\n    value: 7.0\n    tolerance: 2\n    unit: ms\n  - quantity: centroid latency\n    value: 37.8\n    tolerance: 3.78\n    unit: ms\n  - quantity: baseline-subtracted rate increase, 0-100 ms\n    value: 0.50\n    tolerance: 0.20\n    unit: spikes/s\n  depends_on:\n  - fig3i-da-responsive-subset\n  criterion: Methods, Acute recordings; responsive labels inherited from the auROC criterion,\n    2-ms bins over 0-100 ms. The peak tolerance is one 2-ms bin, as 10% of 7 ms is below the\n    bin width; the increase tolerance is the larger distance from 0.50 to a bound of the 95% CI.\n    Open details, all run. (a) The event, the onset of the 1-s continuous 635-nm light (the\n    responsive set comes from it) or the 1-ms 635-nm tagging pulses. (b) Peak and centroid, of\n    the pooled PSTH (legend, \"P ... C ... computed over 0-100 ms\") or medians of per-unit values\n    (Results give IQRs). (c) The baseline for subtraction, −1.25 to −0.25 s (the auROC\n    baseline) or −100 to 0 ms. (d) The permutation test, sign-flip of per-unit increases, or\n    shuffling of event times; the CI by bootstrap over units. Onset \"within ∼3 ms\" is read as\n    the first bin above the baseline mean plus 2 SD, a standard choice. Reproduced when under\n    one reading the three expected values are within tolerance and the permutation p < 0.05;\n    partially reproduced when the increase holds but a latency is out of tolerance.\n- id: chronic-optotag-count\n  statement: In chronic recordings from three mice, 40 VTA-PnO units were opto-identified.\n  source: Results, Chronic single-unit recordings show direction-selective engagement, paragraph\n    1; Methods, Chronic silicon-probe recordings\n  quote: We opto-identified 40 VTA PnO GABA units\n  expected:\n  - quantity: opto-tagged VTA-PnO units, chronic\n    value: 40\n    tolerance: 4\n    unit: units\n  criterion: The tagging criteria are written for the acute recordings; the paper does not say\n    they were applied unchanged to the chronic ones. They are applied as in fig3-optotag-counts\n    to the 635-nm 1-ms pulses of the chronic sessions. Reproduced when the count is within\n    tolerance.\n- id: fig4c-activated-fraction\n  statement: During reverse rotation, 65% (26 of 40) of opto-identified VTA-PnO units are\n    activated and 35% (14 of 40) are not modulated.\n  source: Results, Chronic single-unit recordings show direction-selective engagement, paragraph\n    1; Figure 4c\n  quote: Among opto-identified VTA PnO neurons, 65% (26/40) were classified as activated and 35%\n    (14/40) as non-modulated\n  expected:\n  - quantity: activated units, reverse rotation\n    value: 26\n    tolerance: 2.6\n    unit: units of 40\n  - quantity: fraction activated\n    value: 65\n    tolerance: 6.5\n    unit: percent\n  depends_on:\n  - chronic-optotag-count\n  criterion: Methods, Chronic silicon-probe recordings; reverse rotations; spikes in 100-ms bins;\n    baseline −1.25 to −0.25 s; six 0.5-s windows W1-W6 over 0-3 s from rotation onset; per unit\n    and window, auROC and a test against time-matched baseline; FDR (Benjamini-Hochberg) across\n    windows; activated when a window is significant with auROC > 0.5. Open details, all run.\n    (a) Time-matched baseline, per trial the count in a 0.5-s piece of the baseline or the 1-s\n    baseline halved. (b) Test, paired two-tailed t-test or Wilcoxon signed-rank (Results, \"the\n    same criterion as in the acute experiment\"). (c) The FDR family, windows only, or windows\n    and both directions (Methods, \"and directions, when applicable\"). (d) Units with only\n    suppressed windows; 26 + 14 = 40 leaves none, so they count as non-modulated. Which session\n    each unit comes from is not stated; all reverse sessions are used. Reproduced when under one\n    reading the activated count is within tolerance.\n- id: fig4c-temporal-classes\n  statement: Activated VTA-PnO units split into early-onset (13 of 26), late-onset (6 of 26) and\n    offset-only (7 of 26) classes.\n  source: Results, Chronic single-unit recordings show direction-selective engagement, paragraph\n    1; Figure 4c\n  quote: Using the W1-W6 scheme, activated units segregated into early-onset 50% (13/26),\n    late-onset 23% (6/26), offset-only 27% (7/26) classes\n  expected:\n  - quantity: early-onset units\n    value: 13\n    tolerance: 1.3\n    unit: units\n  - quantity: late-onset units\n    value: 6\n    tolerance: 0.6\n    unit: units\n  - quantity: offset-activated units\n    value: 7\n    tolerance: 0.7\n    unit: units\n  depends_on:\n  - fig4c-activated-fraction\n  criterion: Class rules from Methods, Chronic silicon-probe recordings, on reverse rotations\n    (\"Early-Onset (W1, with later significance or run ≥ 2), Late-Onset (W2–W3, with later\n    significance), Offset-Activated (none in W1–W4, ≥ 1 in W5–W6)\"). The rules leave some units\n    unclassed (W1 alone; first at W2-W3 with nothing later; first at W4). Readings are (a) such\n    units are non-activated, (b) they join the class of their first significant window. Counts\n    of 6 and 7 have tolerances under one unit, so a class within one unit of its value is taken\n    as within tolerance. Reproduced when under one reading all three counts are within one unit\n    (13 ± 1.3); partially reproduced when the order early > offset ≥ late holds.\n- id: fig4d-reverse-activated-direction-selective\n  statement: Reverse-activated VTA-PnO units fire more during reverse than forward rotation\n    across the rotation epoch.\n  source: Figure 4d legend; Results, Chronic single-unit recordings show direction-selective\n    engagement, paragraph 1\n  quote: population PSTHs (100-ms bins) restricted to reverse-activated units showed sustained\n    elevation during reverse relative to forward across the rotation epoch\n  depends_on:\n  - fig4c-activated-fraction\n  criterion: One bidirectional session per mouse, 17 units over 3 mice (Methods, Chronic\n    silicon-probe recordings, direction contrasts), restricted to units activated in reverse.\n    PSTH in 100-ms bins over 0-2 s, averaged over trials then units. Open details, all run.\n    (a) Units as raw rate, or minus each direction's own baseline. (b) Activation in reverse\n    from the per-direction or the joint FDR family. \"Sustained\" is not quantified; the reader\n    reads it as reverse above forward in at least 15 of the 20 bins of 0-2 s, a threshold not\n    in the paper. Reproduced when under one reading that holds; the bin count is reported.\n- id: fig4e-reverse-greater-magnitude\n  statement: Across all opto-tagged VTA-PnO units of the bidirectional sessions, mean response\n    magnitude over 0-3 s is higher during reverse than forward rotation.\n  source: Figure 4e legend; Methods, Chronic silicon-probe recordings, direction contrasts\n  quote: Mean response magnitude of all opto-tagged VTA PnO units over 0–3 s (0–2 s rod rotation\n    and 1 s post stimulus) is higher in reverse than forward condition (paired t -test, p =\n    0.0038)\n  statistics:\n  - test: paired t-test\n    p: 0.0038\n    n: 17 units from 3 mice\n  depends_on:\n  - chronic-optotag-count\n  criterion: Per unit and direction, the mean over W1-W6 of the window response, compared within\n    unit by paired t-test (Methods). \"Response magnitude\" is not defined; readings are (a)\n    auROC against baseline per window, (b) baseline-subtracted rate per window, (c) rate per\n    window divided by baseline rate. Reproduced when under one reading p < 0.05 with reverse\n    higher.\n- id: fig4f-paired-unit-profiles\n  statement: Paired units show a larger fraction of activated windows in reverse than forward,\n    and one unit not modulated in reverse is activated in forward.\n  source: Results, Chronic single-unit recordings show direction-selective engagement, paragraph\n    1; Figure 4f\n  quote: A paired-unit analysis revealed a greater fraction of activated bins during reverse and\n    distinct temporal motifs that reorganized across directions; notably, one unit non-modulated\n    in reverse was activated during forward\n  depends_on:\n  - fig4c-activated-fraction\n  criterion: The 17 units of the bidirectional sessions, windows W1-W6 classified per direction as\n    in fig4c-activated-fraction, under its readings. Reproduced when under one reading the\n    fraction of activated unit-windows is larger in reverse than forward and at least one unit\n    non-modulated in reverse is activated in forward; the number of such units is reported. The\n    paper gives no test.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import re
p='claims/gonzalez-cabrera-2026.yaml'
s=open(p).read()
old="""  quote: Spike duration was shorter in TH − than in TH + neurons (TH + vs. LP p = 0.0023; TH + vs.
    PO p = 0.0185; one-way ANOVA, FDR-corrected post hoc tests)"""
new="""  quote: 'Spike duration was shorter in TH − than in TH + neurons (TH + vs. LP: p = 0.0023; TH +
    vs. PO: p = 0.0185; one-way ANOVA, FDR-corrected post hoc tests)'"""
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
python tools/claims_check.py claims/gonzalez-cabrera-2026.yaml paper/10.64898-2026.02.17.706301.txt; grep -n '—' claims/gonzalez-cabrera-2026.yaml; grep -niw rather claims/gonzalez-cabrera-2026.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import re
lines=open('claims/gonzalez-cabrera-2026.yaml').read().split('\n')
inq=False
for i,l in enumerate(lines,1):
    if l.startswith('#'): continue
    m=re.match(r"^\s*(- )?[a-z_]+: (.*)$",l)
    if m:
        val=m.group(2)
        inq = val.startswith("'")
        if not inq and ': ' in val: print(i,l)
        if inq and val.rstrip().endswith("'") and len(val)>1: inq=False
    else:
        if not inq and ': ' in l: print(i,l)
        if inq and l.rstrip().endswith("'"): inq=False
EOF
grep -c "criterion:" claims/gonzalez-cabrera-2026.yaml; grep -c "statistics:" claims/gonzalez-cabrera-2026.yaml; grep -c "expected:" claims/gonzalez-cabrera-2026.yaml
```

```
785     ci: {level: 0.95, low: 0.30, high: 0.66, unit: spikes/s}
40
20
16
```

**Agent**

I wrote `claims/gonzalez-cabrera-2026.yaml` with 41 claims, and the quote checker passes with 0 problems. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1, flattened from bioRxiv's XML. It has the main text, the figure legends, the Methods and the legends of Supplementary Figures 1 to 4. No PDF was supplied, so I saw no figure panels, and the reference list is empty. The title in the text says "biases backward locomotion"; the registry title says "biases locomotor direction".

**Code read:** github.com/CGonzC/VTAPnO_Locomotion_Analysis at the release the paper cites (`v1.0_manuscript_submission`, commit 1ff5196). It holds the open-field tracking notebook, the photometry notebook and the MATLAB opto-tagging script. Later commits on main only add examples and reformat the code. Where the code and the Methods disagree, I followed the Methods and kept the code's choice as a variant:
- **Photometry baseline:** −1.0 to −0.1 s in the Methods, −3.0 to −0.1 s in the code.
- **Tracking filter:** the code has no likelihood filter and no gap filling.
- **Opto-tagging:** the script lacks the waveform-stability criterion.

**Counts:**
- All 41 claims have quotes; none needed an `inferred` note.
- 20 claims carry statistics (34 values the checker verified), 16 have expected values, and 40 have a criterion.
- The dataset can test 17 claims: photometry (Fig. 3a-c), acute recordings (Fig. 3d-k) and chronic recordings (Fig. 4).
- The other 24 cover the juxtacellular, tracing, slice and open-field experiments. The DANDI description does not list these. I left them at the default data setting and named in the opening comment the two Zenodo records, one cited by the paper and one by the DANDI description. Neither is said to hold raw recordings.

**Details the paper leaves open, with the readings named:**
- **Open-field per-bin tests (Fig. 2f,i):**
  - Correction: FDR (legend) or Holm (Methods).
  - Baseline: −1 to 0 s, or −1.0 to −0.1 s.
  - Time base: the legend's "light at 1–3 s" cannot be the time base, so bins are read from light onset.
- **Frequency screen (Supp. 2d):**
  - Window: 0–1 s or 1–2 s.
  - Mice: 8 (Results) or "the same three mice" (Methods).
- **Latency to peak and speed (Supp. 2e,f):**
  - Bin time stamp: bin end, centre or start.
  - Speed: all frames, gated frames or backward frames only.
  - The Supp. 2f legend's "higher" contradicts its own numbers and the Results; I followed the Results.
- **Photometry:**
  - z-score baseline and form (mean/SD or median/MAD). With the Methods baseline, Pre is 0 by construction.
  - Window measure: mean or area.
  - ANOVA with or without repeated measures.
- **Acute recordings:**
  - Onset latency is not defined (first spike, mean or median).
  - Spike width is not defined (trough to peak or half-width).
  - Firing-rate epoch: baseline epoch or whole recording.
  - auROC windows: −1 to +1.5 s (Methods) or six 0.5-s windows (Results).
  - Time-matched baseline, and paired t-test or Wilcoxon.
  - Fig. 3k: the triggering event (continuous light or tagging pulses), pooled peak or per-unit median, the subtraction baseline, and how the permutation test is built.
- **Chronic recordings:**
  - Whether the acute tagging criteria apply unchanged.
  - The FDR family (windows only, or windows and directions).
  - How units the class rules leave unclassed are counted.
  - "Response magnitude" (auROC, baseline-subtracted rate or rate ratio).
  - Normalisation of the reverse and forward PSTHs.
- **Juxtacellular recordings:** CV2 epoch, spike duration, the pinch measure (raw, change or z-score), the per-bin pinch test and the burst rule.
- **Thresholds I set:** where the paper gives no number ("many", "reliable", "sustained", "above noise"), I set a threshold and the criterion says it is not from the paper.

**Missing from the paper that claims need:**
- The number of responsive DA units behind Fig. 3j,k.
- Definitions of onset latency, spike width, burst and response magnitude.
- No code for the auROC classification, the temporal classes, the direction analysis, the 2-ms DA analysis or the statistics.
- Which LP neuron is left out of the n = 19 correlation.

The reading notes are under each claim in the file.

## End of run

24 turns, 6 minutes, $2.08 at API prices, result: success.
