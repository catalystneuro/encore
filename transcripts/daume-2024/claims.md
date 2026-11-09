# 001187 · claims · run 39822909060

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/; ls claims/001187 2>/dev/null
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
cat claims/001453/*.yaml; head -50 paper/*.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | sed -n 30,400p
```

```
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
    the counts per species are compared instead. The sign of the zebrafish turning response
    to codes 9 and 11 is reported, as the code and the protocol file disagree on which of them
    is lateral right.
- id: fig1d-dc-faster-all-codes
  statement: Danionella cerebrum (DC) swim at a higher median velocity than zebrafish (ZF)
[... 272 more lines not kept]
```

**Agent calls Bash**

```bash
head -20 paper/10.1101-2024.07.15.603630.txt; echo ----; wc -c paper/*.txt; head -c 3000 paper/10.1016-j.neuron.2024.09.013.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.09.013.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.09.013.txt",
 "offset": 236,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "Supplement|Figure S|Table S1",
 "path": "paper/10.1016-j.neuron.2024.09.013.txt",
 "output_mode": "content",
 "offset": 0
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.09.013.txt",
 "offset": 605,
 "limit": 500
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper text, STAR Methods and supplement are all present. Next, the linked code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/rutishauserlab/SBCAT-NO-release-NWB.git && cd SBCAT-NO-release-NWB && git log -3 --format='%H %ad %s' && find . -type f -not -path './.git/*' | head -100
```

```
6d072040c0a53872d841a5e04cc98b8d741407d8 Wed Sep 4 16:24:01 2024 -0700 final main
eef022787c321a713de8bee7bb39360d9f3d9b6e Wed Sep 4 16:20:51 2024 -0700 Update LICENSE
2db71fbe53d763ae3aade028c4b924a5456e792b Wed Sep 4 16:20:05 2024 -0700 Delete CITATION.cff
./assets/Figure1.png
./README.md
./NWB_SBCAT_NO_analysis/helpers/internal/plotting/plot_raster_pic1_delayWM.m
./NWB_SBCAT_NO_analysis/helpers/internal/plotting/plot_raster_NewOld.m
./NWB_SBCAT_NO_analysis/helpers/internal/plotting/plot_behavior.m
./NWB_SBCAT_NO_analysis/helpers/internal/plotting/makeScatterPlot.m
./NWB_SBCAT_NO_analysis/helpers/internal/etc/spikePDFestimate.m
./NWB_SBCAT_NO_analysis/helpers/internal/etc/setCommonAxisRange.m
./NWB_SBCAT_NO_analysis/helpers/internal/etc/rateFilter_units.m
./NWB_SBCAT_NO_analysis/helpers/internal/etc/plotSpikeRaster_multiple_simplified.m
./NWB_SBCAT_NO_analysis/helpers/internal/etc/plotSpikeRaster_multiple.m
./NWB_SBCAT_NO_analysis/helpers/internal/etc/plotSpikeRasterMain.m
./NWB_SBCAT_NO_analysis/helpers/internal/etc/plotPSTH_forSpikeRaster.m
./NWB_SBCAT_NO_analysis/helpers/internal/etc/getTimestamps_forSortedRasterPlot.m
./NWB_SBCAT_NO_analysis/helpers/internal/etc/getTimestampsOfTrials.m
./NWB_SBCAT_NO_analysis/helpers/internal/etc/getRelativeTimestamps.m
./NWB_SBCAT_NO_analysis/helpers/internal/etc/getGaussianKernel.m
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SBCAT-NO-release-NWB && cat README.md && cat NWB_SBCAT_NO_analysis/NWB_SBCAT_NO_analysis_main.m
```

```
# Sample code for: Persistent activity during working memory maintenance predicts long-term memory formation in the human hippocampus

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Generic badge](https://img.shields.io/badge/release-1.0.0-green.svg)](https://github.com/rutishauserlab/SBCAT-release-NWB/releases/tag/v1.0.0)
[![Generic badge](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.13621888-orange.svg)](https://doi.org/10.5281/zenodo.13621888)

## Introduction

This repository contains the code that accompanies [Daume et al. (2024)](https://www.biorxiv.org/content/10.1101/2024.07.15.603630v1) 'Persistent activity during working memory maintenance predicts long-term memory formation in the human hippocampus'. The purpose of the code in this repository is to provide examples of how to use the released data, deposited at the DANDI archive ([DANDI:001187](https://dandiarchive.org/dandiset/001187)). This dataset is formatted in the [Neurodata Without Borders (NWB)](https://www.nwb.org/) format, which can be easily accessed from both MATLAB and Python as described [here](https://nwb-schema.readthedocs.io/en/latest/index.html). 

Abstract of the paper:
>Working Memory (WM) and Long-Term Memory (LTM) are often viewed as separate cognitive systems. Little is known about how these systems interact when forming memories. We recorded single neurons in the human medial temporal lobe while patients maintained novel items in WM and a subsequent recognition memory test for the same items. In the hippocampus but not the amygdala, the level of WM content-selective persist activity during WM maintenance was predictive of whether the item was later recognized with high confidence or forgotten. In contrast, visually evoked activity in the same cells was not predictive of LTM formation. During LTM retrieval, memory-selective neurons responded more strongly to familiar stimuli for which persistent activi
[... 349 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SBCAT-NO-release-NWB/NWB_SBCAT_NO_analysis/helpers && cat custom/NWB_computeGLM.m custom/NWB_calcCatSelective_SB.m custom/NWB_calcMemSelective_SB.m
```

```
<persisted-output>
Output too large (31.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/1b935f26-2a19-454c-a9a9-1c882f2f0866/tool-results/buggvmdnn.txt

Preview (first 2KB):
function m = NWB_computeGLM(nwbAll, all_units, cat_cells_all, params)
%NWB_computeGLM Takes the output of NWB_SB_extractUnits and runs
% a mixed-effects GLM across all category neurons

if isfield(params,'rateFilter') && ~isempty(params.rateFilter) && params.rateFilter > 0
    rateFilter = params.rateFilter;
else
    rateFilter = [];
end

whichWindow = [0 2.5]; % maintenance
whichWindow_bsl = [-.9 -.3]; % baseline

% Filtering for Global Rate (rateFilter should be a nonzero float)
if ~isempty(rateFilter)
    aboveRate = rateFilter_units(nwbAll,all_units,rateFilter);
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/1b935f26-2a19-454c-a9a9-1c882f2f0866/tool-results/buggvmdnn.txt"
}
```

```
1	function m = NWB_computeGLM(nwbAll, all_units, cat_cells_all, params)
2	%NWB_computeGLM Takes the output of NWB_SB_extractUnits and runs
3	% a mixed-effects GLM across all category neurons
4	
5	if isfield(params,'rateFilter') && ~isempty(params.rateFilter) && params.rateFilter > 0
6	    rateFilter = params.rateFilter;
7	else
8	    rateFilter = [];
9	end
10	
11	whichWindow = [0 2.5]; % maintenance
12	whichWindow_bsl = [-.9 -.3]; % baseline
13	
14	% Filtering for Global Rate (rateFilter should be a nonzero float)
15	if ~isempty(rateFilter)
16	    aboveRate = rateFilter_units(nwbAll,all_units,rateFilter);
17	else
18	    aboveRate = ones(length(all_units),1);
19	end
20	all_units = all_units(logical(aboveRate));
[... 631 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SBCAT-NO-release-NWB/NWB_SBCAT_NO_analysis/helpers && cat internal/etc/rateFilter_units.m internal/plotting/plot_behavior.m; grep -n "LTM\|conf\|new_old" internal/plotting/plot_raster_NewOld.m | head -30
```

```
function aboveRate = rateFilter_units(nwbAll,all_units,rateFilter)

aboveRate = ones(length(all_units),1);

for i = 1:length(all_units)
    SU = all_units(i);
    tsEvents_WM = nwbAll{SU.session_count}.acquisition.get('events_raw_WM').timestamps.load;
    tsEvents_LTM = nwbAll{SU.session_count}.acquisition.get('events_raw_LTM').timestamps.load;
    spike_times_WM = all_units(i).spike_times(all_units(i).spike_times<=tsEvents_WM(end));
    spike_times_LTM = all_units(i).spike_times(all_units(i).spike_times>=tsEvents_LTM(1));
    globalRate_WM = length(spike_times_WM)/(tsEvents_WM(end)-tsEvents_WM(1));
    globalRate_LTM = length(spike_times_LTM)/(tsEvents_LTM(end)-tsEvents_LTM(1));
    rateBool = globalRate_WM < rateFilter | globalRate_LTM < rateFilter;
    if rateBool % If the rate is below the filter threshold
        aboveRate(i) = 0;
    end
endfunction plot_behavior(nwbAll)
%% This script analyses behavior of all sessions in SternbergCAT_NO
% JD 2024

[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001187/versions/0.240904.2347/info/ | python -c "import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m['name']); print(m.get('description')); print(m.get('assetsSummary',{}).get('numberOfSubjects'), m.get('assetsSummary',{}).get('numberOfFiles'))"; curl -s https://api.dandiarchive.org/api/dandisets/001187/ | python -c "import json,sys; d=json.load(sys.stdin); print(d['most_recent_published_version']['version'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper && grep -n -i "median split\|3 SD\|±3\|nested\|baseline\|ROC\|chance\|load 1 and 3" 10.1101-2024.07.15.603630.txt | cut -c1-400
```

```
17:Despite the ubiquity of WM-LTM interactions seen behaviorally, little is known about the mechanisms by which the two memory systems interact. fMRI ( Davachi et al. 2001 ; Schon et al. 2004 ; Ranganath et al. 2005 ; Blumenfeld and Ranganath 2006 ; Axmacher et al. 2008 ), scalp M/EEG ( Khader et al. 2007 , 2010 ; Daume et al. 2017 ), and intracranial EEG studies ( Axmacher et al. 2009 , 2010b ) i
21:Neuroimaging, iEEG, and behavioral studies indicate that the medial temporal lobe, and in particular the hippocampus, are strong candidates for shared WM-LTM processes ( Squire 2004 ). Indeed, recent studies indicate that the MTL, particularly the hippocampus, is critical for both WM and LTM in many circumstances as assessed by behavior and neural activity ( Nichols et al. 2006 ; Piekema et al.
35:Patients performed well in both parts of the task, with an average accuracy of 93.3 ± 7.6 % (mean ± SD) in the WM task and 70.3 ± 9.8 % in the LTM task, respectively (both p < 0.0001 as compared to 50% chance; permutation-based t-test; 2 sessions from two different patients were excluded from all analyses due to an accuracy of less than 55% in at least one of the tasks; see Table S1; see Fig. S
43:Category neurons. (a-c) Characterization of category neurons in the hippocampus. (a) Example category neuron. The preferred category of this neuron was “animals”. Top: Peri-stimulus time histogram (PSTH, bin size = 200 ms, step size = 25 ms) during the first picture in each correct trial. Colored areas represent ± s.e.m. Bottom: raster plot with trials re-ordered into preferred and non-preferre
47:(a-c) Characterization of category neurons in the hippocampus. (a) Example category neuron. The preferred category of this neuron was “animals”. Top: Peri-stimulus time histogram (PSTH, bin size = 200 ms, step size = 25 ms) during the first picture in each correct trial. Colored areas represent ± s.e.m. Bottom: raster plot with trials re-ordered into preferred and non-preferred categories. 
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && sed -n 1,80p tools/claims_check.py; ls schema* docs/ 2>/dev/null; ls claims | head;
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

[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json; ls docs/agents; ls claims/*/ | head -60
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
[... 397 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/agents/claims.md; ls claims/ | grep -E "001193|001195|001199"; head -60 claims/001193/*.yaml
```

```
You are the reader for dataset {dataset} in the reproduction registry. The repository is checked out in the current directory. Read docs/protocol.md, the "Reader" section, first: it is the whole method for this run. Look at claims/001453/ for the file format.

Paper: doi:{paper}, "{title}". Its full text is under `paper/`: a `.txt` file per paper (main text, Methods and supplement, with a header saying where it came from), and the PDF where there is one. Read the text; open a PDF page only to read a figure or a table that the text garbles. If the full text, the Methods, or a supplement the results rest on is missing, stop and say what is missing: write no claims. Never write claims from the abstract. You may read the code the paper links to. Do not look at the dataset's data or its files; its title and description on the archive are enough to know which experiments it is meant to hold.

{existing}

Write the claims file as steps 1 to 4 of the Reader section say. Every part of every criterion's method comes from the paper or its code, cited; a detail none of them fixes is named as open, with the readings the paper allows. Check every quote with `python tools/claims_check.py claims/{folder}/<file>.yaml paper/<text>.txt` and fix the quote, never the checker. Do not commit or push: the workflow commits your changes. Only files under `claims/{folder}/` are kept.

Provenance for the opening comment: written by an agent (model "{model}", Claude Code in GitHub Actions), {date}, protocol as stated in docs/protocol.md.

Write prose plainly: no em dashes, never the word "rather". YAML plain scalars must not contain ": " (colon space).

Your final message is a report: the text read (version, supplement), the number of claims and how many have quotes, statistics and criteria; the details the paper leaves open and the readings named for each; anything missing from the paper that a claim needed. Be concise.

Run every command in the foreground and wait for it to finish.
001193
001
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,200p claims/001193/*.yaml
```

```
#   256 electrodes of a participant), significant for more than 50 ms, with amplitude above 0.55 z
#   (Methods, Electrode selection, paragraph 3; ERP amplitude; Results, paragraph 5). The violation
#   mean must be above the CORR mean at the significant samples ("reliably higher"). Open, (V1) "more
#   than 50 ms" as (a) a run of at least 6 consecutive significant samples, or (b) at least 6
#   significant samples in total, or (c) a run spanning more than 50 ms from its first to its last
#   sample (at least 7 consecutive samples); (V2) "> 0.55 z score in amplitude" as (a) the violation's mean HGA
#   above 0.55 z at some significant sample, or (b) the violation minus CORR difference above 0.55 z at
#   some significant sample. The window is 0 to 1,000 ms after T0, the extent of every keyword-locked
#   figure (Fig. 1e, 2a, 3b, 3c); the paper names no other.
# F, F value. The F statistic of the one-way ANOVA of the violation against CORR for an electrode
#   (Fig. 2b legend). An electrode "strongly responded" to a violation when F > 4 (Results, paragraph
#   5). Open, (F1) the maximum F over samples 0 to 1,000 ms; (F2) the mean F over the electrode's
#   significant samples; (F3) the F of the trial-wise mean HGA over 0 to 1,000 ms.
# L, latencies. Onset, peak and offset are the times at which 10%, 50% and 90% of the area of the
#   keyword-locked mean response is reached (fractional area latency; Methods, ERP amplitude). Open,
#   (L1) the response is (a) the violation's trial-mean HGA or (b) the violation minus CORR difference;
#   (L2) the area is taken over (a) 0 to 1,000 ms or (b) the electrode's discriminating period (its
#   significant samples under V, first to last); (L3) negative values are (a) set to zero or (b) kept.
#
# Data. Every claim uses the dataset alone unless it says otherwise. The paper uses no outside data,
[... 121 more lines not kept]
```

**Agent**

Now I have what I need from the code. Let me check whether Table S1's per-session neuron counts sum to the filtered totals (351/532), which decides how a dataset-count claim should read.

**Agent calls Bash**

```bash
sed -n 735,1090p paper/10.1016-j.neuron.2024.09.013.txt | grep -E '^[0-9]+/[0-9]+/[0-9]+ $' | python3 -c "
import sys
v=[list(map(int,l.strip().split('/'))) for l in sys.stdin]
H=v[0::2];A=v[1::2]
print(len(H),len(A))
print('H',[sum(x[i] for x in H) for i in range(3)])
print('A',[sum(x[i] for x in A) for i in range(3)])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/001187/10.1016-j.neuron.2024.09.013.yaml",
 "content": "# Claims for Daume, Kaminski, Salimpour, Gomez Palacio Schjetnan, Anderson, Valiante, Mamelak and\n# Rutishauser (2024), Neuron 112, 3957-3968, on dandiset 001187.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, under\n# docs/protocol.md, version pilot-10.\n#\n# Text read. The accepted author manuscript in PubMed Central (PMC11624075, NIHMS2025394), full text\n# with Results, figure legends and STAR Methods (paper/10.1016-j.neuron.2024.09.013.txt), and its\n# supplement (NIHMS2025394-supplement-1.pdf, extracted into the same file: Figures S1 to S4 and Table\n# S1). The bioRxiv preprint (10.1101/2024.07.15.603630 v1) was searched for method details only; it\n# adds none. The main-text figures were not viewed (no main-text PDF was supplied), so numbers printed\n# only inside panels are not used, and units of axes the text does not name are left open.\n#\n# Code read. https://github.com/rutishauserlab/SBCAT-NO-release-NWB, commit 6d07204 (2024-09-04,\n# \"final main\"), the repository the paper links (also Zenodo 10.5281/zenodo.13621888). It holds a\n# MATLAB script (NWB_SBCAT_NO_analysis_main.m) that loads the dandiset and computes the behaviour\n# plots of Fig. 1c-g (plot_behavior.m, no statistics), the 0.1 Hz rate filter (rateFilter_units.m),\n# the category-neuron selection (NWB_calcCatSelective_SB.m), the memory-selective selection\n# (NWB_calcMemSelective_SB.m), the mixed-effects GLM of Fig. 3a (NWB_computeGLM.m), and the example\n# neurons of Fig. 2a and 4a. It has no code for Fig. 2b,c,e,f, 3b-h or Fig. 4b-g; those analyses\n# rest on the Methods and legends alone, with the Fig. 3a code as the nearest implementation where\n# said.\n#\n# Which dataset. The dandiset's title and description say it holds the source data of this paper\n# (46 NWB files, 39 subjects on the archive), with the code above as the example analysis. The\n# Methods (Data and Code Availability) say it holds spike times and waveforms of the sorted neurons,\n# electrode coordinates, behaviour, stimuli, triggers and patient metadata of each session.\n#\n# Data the paper used (Results, paragraphs 1 to 3; STAR Methods; Table S1).\n# - Subjects. 41 epilepsy patients, 48 sessions, with Behnke-Fried hybrid depth electrodes in the\n#   hippocampus and amygdala, at Cedars-Sinai, Toronto Western and Johns Hopkins. Two sessions of two\n#   patients (P87cs, P1901jh in Table S1) were excluded for accuracy below 55% in one task, leaving 46\n#   sessions (t(45) in the behaviour tests). One patient gave no confidence ratings and is left out of\n#   every confidence analysis (t(44)).\n# - Tasks. A Sternberg WM task, 140 trials (70 load 1, 70 load 3), each encoding picture shown 2 s,\n#   maintenance 2.55 to 2.85 s, then a probe that was always a familiar picture (match or non-match),\n#   pictures from five categories (faces, animals, cars or tools, fruits, landscapes), one per\n#   category in load 3. Then, after 10 to 30 min, an LTM recognition task of 400 pictures (200 old\n#   from the WM task, 200 new), each judged old or new with confidence sure, unsure or guessing.\n# - Neurons. Spikes sorted with OSort jointly for both tasks; 950 isolated, 67 removed for a rate\n#   below 0.1 Hz in either task, leaving 883 (351 hippocampus, 532 amygdala). Table S1 gives per\n#   session the category-selective, memory-selective and recorded counts per area; its recorded\n#   counts sum to 386 and 587 (973), which matches neither 950 nor 883.\n#\n# Shared method. Criteria refer to these by letter. Each detail is taken from the place cited; a\n# detail none of the sources fixes is named as open with the readings the text allows, and the notebook\n# runs each. A claim's outcome is the one all its readings give; when they differ, it is blocked as\n# methods_underspecified with every result shown.\n# S, sessions. The 46 sessions with accuracy of at least 55% in both tasks (Results, paragraph 2;\n#   Table S1). For confidence analyses, sessions with confidence ratings only (the code drops trials\n#   whose confidence is NaN, NWB_computeGLM.m).\n# U, units. A unit is kept when its global rate is at least 0.1 Hz in both tasks (Methods, Spike\n#   sorting). The code computes the WM rate as the spikes up to the last WM event divided by the time\n#   from the first to the last WM event, and the LTM rate likewise from the first LTM event\n#   (rateFilter_units.m). Area is from the electrode location; the code calls amygdala_left and\n#   amygdala_right amygdala and every other location hippocampus (NWB_computeGLM.m).\n# L, LTM confidence. As the code reads the dataset's confidence field (plot_behavior.m,\n#   NWB_computeGLM.m), 1 to 3 are new responses and 4 to 6 old responses, 1 being sure new and 6 sure\n#   old; high confidence is 1 or 6 (sure), low confidence is 2 to 5 (unsure and guessing pooled). The\n#   author checks this coding in the dataset. Remembered is an old picture answered old; forgotten an\n#   old picture answered new.\n# C, category neurons. Per unit, the firing rate 0.2 to 1.2 s after the onset of every encoding\n#   picture (1 to 3) and of the probe, in all WM trials (the code does not restrict to correct\n#   trials); the category is the leading digit of the picture ID (NWB_calcCatSelective_SB.m;\n#   floor(ID/100) in NWB_computeGLM.m). A 1x5 permutation ANOVA over categories (statcond, unpaired,\n#   'perm', 10,000 permutations) at p < 0.05, then a permutation t-test of the category with the\n#   highest mean rate against all others pooled, right-sided at p < 0.05, which the code implements\n#   as the two-sided statcond p < 0.1 (Methods, Selection of neurons; code). The preferred category is\n#   the one with the highest mean. Counts vary slightly between runs of the permutations (code\n#   comment); the seed is a standard choice.\n# M, memory-selective (MS) neurons. Per unit, spike counts 0.2 to 1.2 s after picture onset in the\n#   correct LTM trials, old against new, by a two-sided permutation t-test (statcond, unpaired, 10,000\n#   permutations) at p < 0.05; familiarity-selective (FS) when the old mean is higher, novelty-selective\n#   (NS) otherwise (Methods, Selection of neurons; NWB_calcMemSelective_SB.m).\n# B, baseline normalization. Rates are spike counts divided by window length. Per neuron, the\n#   percent change (rate / mean baseline rate - 1) x 100, the baseline being -0.9 to -0.3 s before the\n#   onset of the first encoding picture (Fig. 2b and 3 legends; NWB_computeGLM.m). In the code the\n#   mean baseline is taken over every row of the neuron's table before any trial selection (one row\n#   per WM picture later shown in the LTM test, correct or not, preferred or not), and neurons with a\n#   zero baseline (infinite values) are removed. Where the code does not reach (Fig. 2), open, the\n#   baseline mean over (B1) all WM trials of the neuron or (B2) the rows of the code's table.\n# O, outlier neurons. Methods (Statistics), applied before each test: neurons with no spikes in a\n#   tested condition (the baseline included) are removed, and so are neurons whose value differs by\n#   more than 3 SD from the mean across all neurons and tested conditions (O-M: per neuron and\n#   condition value, removed when outside mean +- 3 SD of all such values). For the GLMs the code\n#   instead removes neurons whose mean normalized maintenance rate (over all their rows) exceeds 3 SD\n#   of the neuron means, without centring and on the upper side only (O-C). The Methods rule is the\n#   main reading and the code's a variant shown beside it, as protocol step 2 asks.\n# G, mixed-effects GLM. fitglme with a normal distribution, identity link and Laplace fit (maximum\n#   likelihood), random intercepts for patient and for neuron nested in patient, the formula\n#   FR ~ fixed effects + (1 | patientID) + (1 | patientID:neuronID) (Results, Category neurons\n#   paragraph 2, \"these random intercept terms were used for all GLMs\"; NWB_computeGLM.m). P-values as\n#   fitglme reports them (t statistics on residual degrees of freedom). Categorical factors take the\n#   level the paper's betas imply as reference (incorrect, load 3, forgotten, amygdala, non-preferred,\n#   new, weak), so that the signs compare with the paper's.\n# P, permutation t-tests. statcond with 'perm', 10,000 permutations, two-sided unless stated; paired\n#   across the units of the test (sessions, neurons or neuron pairs) where each unit gives both\n#   conditions (Results, paragraph 2, \"permutation-based paired t-tests were used throughout the\n#   manuscript unless stated otherwise\"; Methods, Statistics).\n#\n# Data. Every claim uses the dataset alone. The paper uses no outside data except the online study of\n# 100 healthy participants (Figure S1), whose data the paper does not deposit or locate; it is not\n# a main finding and no claim is made for it.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001187\"\npaper: doi:10.1016/j.neuron.2024.09.013\nclaims:\n- id: sessions-and-neurons\n  statement: After excluding two sessions, 46 sessions are analysed, in which 883 single units pass\n    the 0.1 Hz rate filter, 351 in the hippocampus and 532 in the amygdala, of 950 isolated.\n  source: Results, paragraph 3; STAR Methods, Spike sorting\n  quote: In total, we isolated 950 neurons across both areas of the MTL. Neurons with a firing rate\n    lower than 0.1 Hz in either the WM or the LTM tasks were excluded from analysis (67 neurons (7.1%)).\n    Analyses are based on 351 isolated neurons in the hippocampus and 532 in the amygdala\n  expected:\n  - {quantity: analysed sessions, value: 46, tolerance: 0}\n  - {quantity: isolated units, value: 950, tolerance: 0}\n  - {quantity: hippocampal units after the rate filter, value: 351, tolerance: 0}\n  - {quantity: amygdala units after the rate filter, value: 532, tolerance: 0}\n  criterion: Counts of sessions and of units by area, before and after the rate filter of U, in the\n    sessions of S. Tolerance zero, as these are counts of the deposited units. Reproduced when all\n    four match; partially reproduced when the counts after the filter match but the isolated count\n    does not (Table S1 sums to 973 recorded units, so the paper itself gives two totals). The Table S1\n    total is reported beside them.\n- id: table-s1-counts\n  statement: Per session, the numbers of recorded units in the hippocampus and the amygdala are those\n    of Table S1.\n  source: Table S1\n  inferred: Numbers from Table S1 (third number of each area column); no sentence of the text states\n    them. Their sums (386 hippocampus, 587 amygdala) differ from the 950 and 883 of the Methods.\n  criterion: Per session, matched by the session labels of Table S1 to the dataset's subject and\n    session through the patient metadata, the count of units per area in the dataset (before and\n    after the rate filter of U) against the table's recorded count. Reproduced when every one of the\n    46 sessions matches under one of the two counts; partially reproduced when at least 41 (90%) do.\n    The category-selective and memory-selective counts per session of the table are compared with\n    those of claims category-neuron-counts and ms-neuron-counts, as a report, not a test.\n- id: behaviour-overall-accuracy\n  statement: Patients answered 93.3% of WM trials and 70.3% of LTM trials correctly (d' 1.19), both\n    above the 50% chance level.\n  source: Results, paragraph 2\n  quote: Patients performed well in both parts of the task, with an average accuracy of 93.3 ± 7.6 %\n    (mean ± SD) in the WM task and 70.3 ± 9.8 % (d’ = 1.19 ± 0.62) in the LTM task, respectively\n    (both p < 0.0001 as compared to 50 % chance; permutation-based t-test\n  statistics:\n  - test: permutation-based t-test against 50% chance\n    p: 0.0001\n    p_relation: \"<\"\n    n: 46 sessions\n  expected:\n  - {quantity: mean WM accuracy across sessions, value: 93.3, tolerance: 1.1, unit: \"%\"}\n  - {quantity: mean LTM accuracy across sessions, value: 70.3, tolerance: 1.4, unit: \"%\"}\n  - {quantity: mean LTM d prime across sessions, value: 1.19, tolerance: 0.09}\n  criterion: Per session of S, the proportion of correct WM trials and of correct LTM trials (all 400),\n    and d' as z(hit rate) - z(false-alarm rate) of old and new pictures; means across sessions. The\n    tolerances are the standard errors of the mean (the stated SD over the square root of 46), since\n    the paper's stated spread is the SD across sessions and these are means of the same sessions; the\n    10% default would be looser. The correction for hit or false-alarm rates of 0 or 1 is not given;\n    none is applied unless a rate is 0 or 1, in which case the 1/(2N) rule, a standard choice, is used\n    and said. Reproduced when the three means are within tolerance and each accuracy exceeds 50% by\n    a one-sample permutation test (P) at p < 0.0001.\n- id: fig1c-wm-accuracy-load\n  statement: WM accuracy is higher in load 1 than in load 3 trials.\n  source: Results, paragraph 2; Figure 1c\n  quote: In the WM task, patients performed with higher accuracy (Fig. 1c; load 1 – load 3 t(45) = 4.89,\n    p < 0.0001\n  statistics:\n  - test: permutation-based paired t-test\n    statistic: t(45) = 4.89\n    p: 0.0001\n    p_relation: \"<\"\n    n: 46 sessions\n  criterion: Per session of S, the proportion correct in load 1 and in load 3 trials (plot_behavior.m),\n    compared by the paired permutation t-test of P. Reproduced when load 1 is higher at p < 0.0001;\n    partially reproduced when it is higher at p < 0.05 only.\n- id: fig1d-wm-rt-load\n  statement: WM responses are faster in load 1 than in load 3 trials.\n  source: Results, paragraph 2; Figure 1d\n  quote: and faster (Fig. 1d; t(45) = −4.29, p < 0.0001) in load 1 than load 3 trials\n  statistics:\n  - test: permutation-based paired t-test\n    statistic: t(45) = -4.29\n    p: 0.0001\n    p_relation: \"<\"\n    n: 46 sessions\n  criterion: Per session of S, the mean response time of load 1 and of load 3 trials, response times\n    above 5 s set to missing as in plot_behavior.m (the Methods name no exclusion; the variant without\n    it is shown), compared by the paired permutation t-test of P. Reproduced when load 1 is faster at\n    p < 0.0001; partially reproduced when it is faster at p < 0.05 only. All trials are used, as in\n    the code; the paper does not restrict to correct trials.\n- id: fig1e-ltm-confidence-accuracy\n  statement: LTM recognition is more accurate in high-confidence than in low-confidence trials.\n  source: Results, paragraph 2; Figure 1e\n  quote: In the LTM task, retrieval was more accurate (Fig. 1e; t(44) = 8.66, p < 0.0001; one patient\n    did not use confidence ratings and was therefore excluded from all confidence-related analyses)\n  statistics:\n  - test: permutation-based paired t-test\n    statistic: t(44) = 8.66\n    p: 0.0001\n    p_relation: \"<\"\n    n: 45 sessions\n  criterion: Per session of S with confidence ratings, LTM accuracy over all trials (old and new) of\n    high and of low confidence (L), compared by the paired permutation t-test of P. Open, the text\n    says \"Low confidence was defined as an average of “unsure” and “guessing” responses\"; readings\n    (a) accuracy of the unsure and guessing trials pooled, as plot_behavior.m computes it, and (b)\n    the mean of the unsure accuracy and the guessing accuracy. Reproduced when high is more accurate\n    at p < 0.0001; partially reproduced when at p < 0.05 only.\n- id: ltm-rt-confidence\n  statement: LTM responses are faster with high confidence (mean 1.83 s) than with low confidence\n    (2.62 s).\n  source: Results, paragraph 2\n  quote: and faster (mean RT high 1.83 ± 0.57 s; mean RT low 2.62 ± 0.66 s; t(44) = −11.13, p < 0.0001)\n    when patients indicated high confidence in their responses\n  statistics:\n  - test: permutation-based paired t-test\n    statistic: t(44) = -11.13\n    p: 0.0001\n    p_relation: \"<\"\n    n: 45 sessions\n  expected:\n  - {quantity: mean LTM response time with high confidence, value: 1.83, tolerance: 0.085, unit: s}\n  - {quantity: mean LTM response time with low confidence, value: 2.62, tolerance: 0.098, unit: s}\n  criterion: Per session with confidence ratings, the mean response time of high- and low-confidence\n    LTM trials (L), all trials; means across sessions; the paired permutation t-test of P. Tolerances\n    are the standard errors of the mean (stated SD over the square root of 45), for the reason given\n    in behaviour-overall-accuracy. Open, (a) all response times, as the text names no exclusion, or\n    (b) response times above 5 s set to missing, as plot_behavior.m does for every response time it\n    reads; and low confidence pooled or averaged as in fig1e-ltm-confidence-accuracy. Reproduced\n    when, under one reading, both means are within tolerance and high is faster at p < 0.0001;\n    partially reproduced when high is faster at p < 0.05 but a mean is outside tolerance under every\n    reading.\n- id: fig1f-ltm-load\n  statement: Pictures held in load 1 WM trials are later recognized better than pictures held in load\n    3 trials.\n  source: Results, paragraph 2; Figure 1f\n  quote: Items that were encoded in load 1 trials in the previous WM task were remembered better than\n    items encoded during load 3 trials (Fig. 1f; t(45) = 2.42; p = 0.018)\n  statistics:\n  - test: permutation-based paired t-test\n    statistic: t(45) = 2.42\n    p: 0.018\n    n: 46 sessions\n  criterion: Per session of S, the hit rate (old pictures answered old over all old pictures) for\n    pictures from load 1 and from load 3 trials, from the LTM trials' load field, as plot_behavior.m\n    computes it; the paired permutation t-test of P. Reproduced when load 1 is higher at p < 0.05.\n- id: fig1g-ltm-probe\n  statement: Pictures that were also used as WM probes, and so shown twice, are later recognized better\n    than pictures shown once.\n  source: Results, paragraph 2; Figure 1g\n  quote: items that were also used as the probe and therefore presented twice were remembered better\n    than items not used as the probe (Fig. 1g; t(45) = 7.25, p < 0.0001)\n  statistics:\n  - test: permutation-based paired t-test\n    statistic: t(45) = 7.25\n    p: 0.0001\n    p_relation: \"<\"\n    n: 46 sessions\n  criterion: Per session of S, the hit rate for old pictures shown twice and shown once in the WM task\n    (the LTM trials' num_times_shown field, plot_behavior.m); the paired permutation t-test of P.\n    Reproduced when shown twice is higher at p < 0.0001; partially reproduced when at p < 0.05 only.\n- id: category-neuron-counts\n  statement: 104 hippocampal units (29.65%) and 220 amygdala units (41.35%) are category neurons.\n  source: Results, Category neurons remain persistently active when their preferred category is held\n    in WM, paragraph 1\n  quote: In the hippocampus, 104 (29.65 %) neurons qualified as category neurons, and in the amygdala\n    220 (41.35 %) neurons qualified as category neurons\n  expected:\n  - {quantity: hippocampal category neurons, value: 104, tolerance: 10.4}\n  - {quantity: amygdala category neurons, value: 220, tolerance: 22}\n  criterion: Selection C on the units of U in the sessions of S. Reproduced when both counts are within\n    tolerance (10% of each, which also covers the run-to-run variation of the permutation tests that\n    the code warns of).\n- id: fig2b-hippocampus-persistent\n  statement: Hippocampal category neurons are persistently active above baseline during maintenance\n    and fire more when an image of their preferred category is held in WM.\n  source: Results, Category neurons remain persistently active, paragraph 2; Figure 2b\n  quote: In the hippocampus, category neurons remained persistently active throughout the maintenance\n    period (intercept beta = 17.86, p = 1.38 × 10−3; mixed-effects GLM) and had significantly higher\n    FRs during trials in which images from the preferred category were maintained in WM (Fig. 2b;\n    preferred category beta = 12.47, p = 8.82 × 10−7)\n  statistics:\n  - about: intercept\n    test: mixed-effects GLM\n    p: 0.00138\n    n: 104 hippocampal category neurons\n  - about: preferred category\n    test: mixed-effects GLM\n    p: 8.82e-7\n    n: 104 hippocampal category neurons\n  depends_on:\n  - category-neuron-counts\n  expected:\n  - {quantity: intercept beta, value: 17.86, tolerance: 1.79, unit: \"% change to baseline\"}\n  - {quantity: preferred-category beta, value: 12.47, tolerance: 1.25, unit: \"% change to baseline\"}\n  criterion: Hippocampal category neurons of C; all correct WM trials, both loads; the rate 0 to 2.5\n    s after maintenance onset, normalized as B; outliers removed as O; the GLM of G with the fixed\n    effect preferred category (true when an encoding picture of the trial is of the neuron's preferred\n    category). Open, (a) one row per trial, as the text describes, or (b) the rows of the code's table\n    (one per encoding picture later tested in the LTM test, the preferred flag per picture); and the\n    baseline B1 or B2. Reproduced when, under the readings, the intercept and the preferred-category\n    effect are positive at p < 0.05 and both betas within tolerance; partially reproduced when both\n    are positive at p < 0.05 but a beta is outside tolerance.\n- id: fig2c-hippocampus-correct-load\n  statement: When the preferred category is held, hippocampal category neurons fire more in correct\n    than incorrect trials and more in load 1 than load 3 trials.\n  source: Results, Category neurons remain persistently active, paragraph 2; Figure 2c\n  quote: Using only preferred trials and modelling WM accuracy (2 levels, WM correct/incorrect,\n    categorical) as well as load (2 levels, load 1/load 3, categorical) as fixed effects, we further\n    observed that category neurons in the hippocampus had higher FRs in (1) correct than incorrect\n    trials (beta = 16.22, p = 0.046) and (2) in load 1 than in load 3 trials (Fig. 2c; beta = 13.769,\n    p = 0.0023)\n  statistics:\n  - about: correct against incorrect\n    test: mixed-effects GLM\n    p: 0.046\n  - about: load 1 against load 3\n    test: mixed-effects GLM\n    p: 0.0023\n  depends_on:\n  - category-neuron-counts\n  expected:\n  - {quantity: WM accuracy beta, value: 16.22, tolerance: 1.62, unit: \"% change to baseline\"}\n  - {quantity: load beta, value: 13.769, tolerance: 1.377, unit: \"% change to baseline\"}\n  criterion: Hippocampal category neurons of C; WM trials holding a picture of the neuron's preferred\n    category, correct and incorrect, both loads; maintenance rate (0 to 2.5 s) normalized as B; O; the\n    GLM of G with fixed effects WM accuracy (incorrect as reference) and load (load 3 as reference).\n    Open, (a) main effects only, as the text names two effects, or (b) with their interaction; and B1\n    or B2. Reproduced when, under the readings, both effects are positive at p < 0.05 and both betas\n    within tolerance; partially reproduced when the load effect holds and the accuracy effect is\n    positive but p >= 0.05 (its reported p is 0.046), or when both hold with a beta outside tolerance.\n- id: fig2e-amygdala-persistent\n  statement: Amygdala category neurons are also persistently active during maintenance and fire more\n    for the preferred category.\n  source: Results, Category neurons remain persistently active, paragraph 3; Figure 2e\n  quote: In the amygdala, category neurons also remained persistently active throughout the maintenance\n    period across all correct trials (intercept beta = 9.78, p = 6.76 × 10−4) with FRs higher for\n    preferred than unpreferred categories (Fig. 2e; preferred category beta = 6.91, p = 9.38 × 10−7)\n  statistics:\n  - about: intercept\n    test: mixed-effects GLM\n    p: 0.000676\n    n: 220 amygdala category neurons\n  - about: preferred category\n    test: mixed-effects GLM\n    p: 9.38e-7\n    n: 220 amygdala category neurons\n  depends_on:\n  - category-neuron-counts\n  expected:\n  - {quantity: intercept beta, value: 9.78, tolerance: 0.98, unit: \"% change to baseline\"}\n  - {quantity: preferred-category beta, value: 6.91, tolerance: 0.69, unit: \"% change to baseline\"}\n  criterion: As fig2b-hippocampus-persistent, with the amygdala category neurons.\n- id: fig2f-amygdala-load-not-accuracy\n  statement: When the preferred category is held, amygdala category neurons fire more in load 1 than\n    load 3 trials, but not more in correct than incorrect trials.\n  source: Results, Category neurons remain persistently active, paragraph 3; Figure 2f\n  quote: using only preferred trials category neurons in the amygdala showed a significant main effect\n    only for load (Fig. 2f; load 1 – load 3; beta = 12.309; p = 2.46 × 10−7), but the effect for WM\n    accuracy (correct – incorrect beta = −6.13; p = 0.24) was not significant\n  statistics:\n  - about: load 1 against load 3\n    test: mixed-effects GLM\n    p: 2.46e-7\n  - about: correct against incorrect\n    test: mixed-effects GLM\n    p: 0.24\n  depends_on:\n  - category-neuron-counts\n  expected:\n  - {quantity: load beta, value: 12.309, tolerance: 1.231, unit: \"% change to baseline\"}\n  criterion: The model of fig2c-hippocampus-correct-load, with the amygdala category neurons and the\n    same readings. The accuracy part is a claim of absence, judged on the same GLM at p < 0.05.\n    Reproduced when the load effect is positive at p < 0.05 with its beta within tolerance and the\n    accuracy effect has p >= 0.05 under every reading; partially reproduced when only one part holds.\n    The accuracy beta is reported either way.\n- id: fig3a-area-interactions\n  statement: In a GLM over category neurons of both areas, no main effect of LTM accuracy, confidence\n    or area is significant, but every interaction with area is, so the relation of maintenance\n    activity to later memory differs between hippocampus and amygdala.\n  source: Results, Persistent activity of category neurons in the hippocampus - not the amygdala -\n    predicts LTM formation, paragraph 1; Figure 3a\n  quote: We did not observe any significant main effects nor was the interaction between LTM accuracy\n    and confidence significant (Fig. 3a; all p > 0.26). However, all interaction terms including area\n    showed significant modulations (confidence × area beta = 16.88, p = 0.025; LTM accuracy × area\n    beta = 59.78, p = 0.0030; confidence × LTM accuracy × area beta = −28.64, p = 0.0029)\n  statistics:\n  - about: main effects and the LTM accuracy by confidence interaction\n    test: mixed-effects GLM\n    p: 0.26\n    p_relation: \">\"\n  - about: confidence by area\n    test: mixed-effects GLM\n    p: 0.025\n  - about: LTM accuracy by area\n    test: mixed-effects GLM\n    p: 0.003\n  - about: confidence by LTM accuracy by area\n    test: mixed-effects GLM\n    p: 0.0029\n  depends_on:\n  - category-neuron-counts\n  expected:\n  - {quantity: confidence by area beta, value: 16.88, tolerance: 1.69}\n  - {quantity: LTM accuracy by area beta, value: 59.78, tolerance: 5.98}\n  - {quantity: three-way interaction beta, value: -28.64, tolerance: 2.86}\n  criterion: As NWB_computeGLM.m, which is the paper's code for this panel. Category neurons of C in\n    both areas; one row per WM picture later shown in the LTM test; maintenance rate 0 to 2.5 s after\n    maintenance onset, normalized as B (mean baseline over all the neuron's rows); then rows kept\n    when the WM trial was correct and the picture is of the preferred category, with a confidence\n    rating; confidence recoded as the Methods say (forgotten sure 1, unsure 2, guessing 3; remembered\n    guessing 1, unsure 2, sure 3; the code maps 4, 5, 6 to 1, 2, 3 and keeps 1, 2, 3, which is the\n    same under L); FR ~ LTMacc * conf * area with the random effects of G, area with amygdala as\n    reference so that the interactions are hippocampus minus amygdala. Outliers O-M for the main\n    result, O-C (the code) shown as a variant. Reproduced when the three interactions with area have\n    p < 0.05 with the reported signs and betas within tolerance, and the main effects and the LTMacc\n    by conf interaction have p >= 0.05; partially reproduced when the three interactions hold in sign\n    and significance with a beta out of tolerance or a main effect significant.\n- id: fig3b-hippocampus-predicts-ltm\n  statement: In the hippocampus, maintenance activity of category neurons for the preferred category\n    predicts later LTM accuracy and confidence, with an interaction between the two, so activity is\n    higher for pictures later remembered than forgotten.\n  source: Results, Persistent activity of category neurons in the hippocampus, paragraph 1; Figure 3b\n  quote: This revealed a significant main effect of confidence (Fig. 3b; beta = 20.30, p = 4.17 × 10−3)\n    and LTM accuracy (beta = 67.90, p = 4.43 × 10−4), as well as a significant interaction between the\n    two terms (beta = −30.80, p = 7.74 × 10−4) in the hippocampus\n  statistics:\n  - about: confidence\n    test: mixed-effects GLM\n    p: 0.00417\n  - about: LTM accuracy\n    test: mixed-effects GLM\n    p: 0.000443\n  - about: confidence by LTM accuracy\n    test: mixed-effects GLM\n    p: 0.000774\n  depends_on:\n  - category-neuron-counts\n  expected:\n  - {quantity: confidence beta, value: 20.30, tolerance: 2.03}\n  - {quantity: LTM accuracy beta, value: 67.90, tolerance: 6.79}\n  - {quantity: confidence by LTM accuracy beta, value: -30.80, tolerance: 3.08}\n  criterion: The table of fig3a-area-interactions restricted to hippocampal category neurons, FR ~\n    LTMacc * conf with the random effects of G (the Fig. 3a code with the area term dropped, as the\n    text says the analysis was \"repeated ... in each area separately\"). Outliers O-M, with O-C as a\n    variant; O applied over both areas together as in Fig. 3a (a) or within the hippocampus (b), the\n    text not saying which. Reproduced when, under the readings, the three effects have p < 0.05 with\n    the reported signs and betas within tolerance; partially reproduced when the three hold in sign\n    and significance with a beta out of tolerance.\n- id: fig3b-amygdala-no-prediction\n  statement: In the amygdala, maintenance activity of category neurons does not predict later LTM\n    accuracy or confidence.\n  source: Results, Persistent activity of category neurons in the hippocampus, paragraph 1; Figure 3b\n  quote: in the hippocampus but not in the amygdala (confidence beta = 1.54, p = 0.69; LTM accuracy\n    beta = −2.27, p = 0.82; confidence × LTM accuracy beta = 1.02, p = 0.83)\n  statistics:\n  - about: confidence\n    test: mixed-effects GLM\n    p: 0.69\n  - about: LTM accuracy\n    test: mixed-effects GLM\n    p: 0.82\n  - about: confidence by LTM accuracy\n    test: mixed-effects GLM\n    p: 0.83\n  depends_on:\n  - category-neuron-counts\n  criterion: A claim of absence, judged on the paper's test, the model of fig3b-hippocampus-predicts-ltm\n    on amygdala category neurons, with the same readings. Reproduced when none of the three effects\n    has p < 0.05; not reproduced when any does. The betas are reported either way.\n- id: fig3c-hippocampus-high-confidence\n  statement: Across hippocampal category neurons, maintenance firing for the preferred category is\n    higher for pictures later remembered than forgotten with high confidence, but not with low\n    confidence.\n  source: Results, Persistent activity of category neurons in the hippocampus, paragraph 2; Figure 3c\n  quote: In the hippocampus, FRs were higher for remembered than forgotten trials for high confidence\n    (Fig. 3c; t(82) = 2.16, p = 0.028; some neurons were removed due to insufficient data in at least\n    one of the conditions or since they differed ±3 SD from the mean across all neurons and conditions;\n    see Methods), but not low confidence trials (t(68) = −1.38, p = 0.17)\n  statistics:\n  - about: high confidence, remembered against forgotten\n    test: permutation-based t-test\n    statistic: t(82) = 2.16\n    p: 0.028\n    n: 83 hippocampal category neurons\n  - about: low confidence, remembered against forgotten\n    test: permutation-based t-test\n    statistic: t(68) = -1.38\n    p: 0.17\n    n: 69 hippocampal category neurons\n  depends_on:\n  - category-neuron-counts\n  criterion: Hippocampal category neurons of C; the rows of fig3a-area-interactions (correct WM\n    trials, preferred pictures later tested). Per neuron, the mean maintenance rate (0 to 2.5 s) of\n    pictures remembered with high confidence (L, rating 6) and of pictures forgotten with high\n    confidence (rating 1); for low confidence, remembered 4 or 5 against forgotten 2 or 3. Neurons\n    without trials in a condition, or outliers by O-M, are removed; the paired permutation t-test of\n    P. Open, the rate is (a) normalized as B, as the betas of Fig. 3 are, or (b) in spikes per second,\n    the legend not naming the unit of panel c. The low-confidence part is a claim of absence on the\n    same test at p < 0.05. Reproduced when, under both readings, the high-confidence difference is\n    positive at p < 0.05 and the low-confidence one has p >= 0.05; partially reproduced when only the\n    high-confidence part holds. The numbers of neurons tested (83 and 69 in the paper) are reported.\n- id: fig3d-amygdala-no-difference\n  statement: Across amygdala category neurons, maintenance firing does not differ between later\n    remembered and forgotten pictures, with high or low confidence.\n  source: Results, Persistent activity of category neurons in the hippocampus, paragraph 2; Figure 3d\n  quote: In the amygdala, we neither observed a significant effect for high (Fig. 3d; t(158) = 0.84,\n    p = 0.41) nor low confidence trials (t(152) = 1.15, p = 0.26)\n  statistics:\n  - about: high confidence\n    test: permutation-based t-test\n    statistic: t(158) = 0.84\n    p: 0.41\n    n: 159 amygdala category neurons\n  - about: low confidence\n    test: permutation-based t-test\n    statistic: t(152) = 1.15\n    p: 0.26\n    n: 153 amygdala category neurons\n  depends_on:\n  - category-neuron-counts\n  criterion: A claim of absence, judged on the test of fig3c-hippocampus-high-confidence applied to\n    amygdala category neurons, with the same readings. Reproduced when neither comparison has p <\n    0.05; not reproduced when either does. Mean differences are reported.\n- id: fig3e-early-delay-cluster\n  statement: In hippocampal category neurons, firing differs between pictures later remembered and\n    forgotten with high confidence early in the maintenance period, from 0 to 650 ms.\n  source: Results, Persistent activity of category neurons in the hippocampus, paragraph 3; Figure 3e\n  quote: In the hippocampus, FRs during the beginning of the maintenance period (0 – 650 ms) differed\n    significantly between the two conditions (Fig. 3e; cluster-p = 0.0042; cluster-based permutation\n    test\n  statistics:\n  - test: cluster-based permutation test\n    p: 0.0042\n  depends_on:\n  - fig3c-hippocampus-high-confidence\n  expected:\n  - {quantity: end of the significant cluster after maintenance onset, value: 650, tolerance: 65, unit: ms}\n  criterion: The high-confidence remembered and forgotten conditions and neurons of\n    fig3c-hippocampus-high-confidence; per neuron, time-resolved rates over the maintenance period 0 to\n    2.5 s; a cluster-based permutation test as FieldTrip's ft_freqstatistics (Methods, Statistics),\n    paired across neurons (dependent-samples t), 10,000 permutations, alpha 0.025 for each one-sided\n    cluster. Open, (T1) the binning, (a) 200 ms windows stepped by 25 ms, the only PSTH binning the\n    paper gives (Fig. 2a legend), or (b) 50 ms bins, the code's PSTH bin (spikePlotParams in\n    NWB_calcCatSelective_SB.m), each time point at the window centre; (T2) the cluster-forming\n    threshold, not given, taken as FieldTrip's default clusteralpha 0.05, a standard choice that\n    could change the cluster's extent; (T3) the rate normalized as B or in spikes per second, as in\n    fig3c. Reproduced when, under the readings, a cluster with remembered above forgotten has cluster\n    p < 0.025, begins within 65 ms of maintenance onset and ends within tolerance of 650 ms;\n    partially reproduced when such a significant cluster exists but its bounds are outside these.\n- id: fig3f-amygdala-no-cluster\n  statement: In amygdala category neurons, no period of the maintenance period shows a significant\n    difference between later remembered and forgotten pictures.\n  source: Results, Persistent activity of category neurons in the hippocampus, paragraph 3; Figure 3f\n  quote: In the amygdala, we did not observe any significant cluster throughout the entire maintenance\n    period of the WM task (Fig. 3f; cluster-p = 0.16)\n  statistics:\n  - test: cluster-based permutation test\n    p: 0.16\n  depends_on:\n  - fig3d-amygdala-no-difference\n  criterion: A claim of absence, judged on the test of fig3e-early-delay-cluster applied to amygdala\n    category neurons (the high-confidence conditions of fig3d), with the same readings. Reproduced when\n    no cluster has cluster p < 0.025 on either side; not reproduced when one does. The smallest cluster\n    p is reported.\n- id: fig3g-nonpreferred-no-effect\n  statement: Maintenance activity of category neurons while non-preferred pictures are held does not\n    predict later LTM accuracy or confidence.\n  source: Results, Persistent activity of category neurons in the hippocampus, paragraph 4; Figure 3g\n  quote: None of the main effects nor interactions in either of the mixed-effects GLMs showed any\n    significant relationship between FR and the factors tested (all p > 0.06)\n  statistics:\n  - test: mixed-effects GLM\n    p: 0.06\n    p_relation: \">\"\n  depends_on:\n  - category-neuron-counts\n  criterion: A claim of absence, judged on the paper's test, the model of fig3a-area-interactions\n    (LTMacc * conf * area, both areas) on the rows of non-preferred pictures in place of preferred\n    ones (Fig. 3g legend). Open, which rows, (a) every non-preferred picture of the code's table\n    (pref false), or (b) only pictures of trials that held no preferred picture. Reproduced when no\n    fixed effect other than the intercept has p < 0.05 under every reading; not reproduced when any\n    does under every reading. The coefficients are reported.\n- id: fig3h-encoding-no-effect\n  statement: Activity of category neurons during the presentation of the first encoding picture, for\n    preferred pictures, does not predict later LTM accuracy or confidence.\n  source: Results, Persistent activity of category neurons in the hippocampus, paragraph 4; Figure 3h;\n    STAR Methods, Relating WM maintenance activity to LTM formation, paragraph 2\n  quote: To test whether category-selective activity predicted LTM formation during the encoding window,\n    we based our GLM analysis on firing rates determined during the picture 1 window of preferred\n    images (0–2 s).\n  statistics:\n  - test: mixed-effects GLM\n    p: 0.06\n    p_relation: \">\"\n  depends_on:\n  - category-neuron-counts\n  criterion: A claim of absence, judged on the paper's test, the model of fig3a-area-interactions with\n    the rate 0 to 2 s after the onset of encoding picture 1 in place of the maintenance rate,\n    normalized as B, correct WM trials only (Fig. 3h legend). Open, which trials, (a) those whose\n    first encoding picture is of the preferred category, with the LTM outcome of that picture, or\n    (b) those holding a preferred picture in any encoding slot, with the LTM outcome of the preferred\n    picture and the rate of the picture 1 window. Reproduced when no fixed effect other than the\n    intercept has p < 0.05 under every reading; not reproduced when any does under every reading.\n- id: ms-neuron-counts\n  statement: 53 of the 351 hippocampal units (15.10%) are memory-selective, 25 of them (47%) firing\n    more to familiar than novel pictures.\n  source: Results, Activity during WM maintenance is linked to subsequent memory signal, paragraph 2\n  quote: Out of the 351 recorded cells, n = 53 (15.10 %) were MS cells. Of these, 25 (47%) responded\n    more to familiar than novel items, with the remaining responding more to novel than to familiar\n    items.\n  expected:\n  - {quantity: hippocampal MS neurons, value: 53, tolerance: 5.3}\n  - {quantity: hippocampal familiarity-selective neurons, value: 25, tolerance: 2.5}\n  criterion: Selection M on the hippocampal units of U in the sessions of S. Reproduced when both\n    counts are within tolerance. The amygdala count (68 in Table S1) is reported, not tested.\n- id: fig4b-ms-confidence-auc\n  statement: Hippocampal memory-selective neurons separate old from new pictures better for\n    high-confidence than for low-confidence decisions (higher ROC AUC), so they carry a memory-strength\n    signal.\n  source: Results, Activity during WM maintenance is linked to subsequent memory signal, paragraph 2;\n    Figure 4b; STAR Methods, Single-neuron AUC analysis\n  quote: The response of MS neurons differed significantly more for high- as compared to low-confidence\n    trials (Fig. 4b; t(40) = 2.89, p = 0.0039; 12 neurons excluded due to insufficient data in either\n    one of the conditions, see Methods)\n  statistics:\n  - test: permutation-based t-test\n    statistic: t(40) = 2.89\n    p: 0.0039\n    n: 41 hippocampal MS neurons\n  depends_on:\n  - ms-neuron-counts\n  criterion: Hippocampal MS neurons of M. Spike counts 0.2 to 1.2 s after LTM picture onset; per\n    neuron an ROC with 25 thresholds linearly spaced from the minimal to the maximal count observed,\n    AUC by the trapezoid rule; for FS neurons all true negatives against high-confidence true positives\n    (rating 6) and, separately, against low-confidence true positives (4, 5); for NS neurons all true\n    positives against high-confidence (1) and low-confidence (2, 3) true negatives (Methods,\n    Single-neuron AUC analysis). The AUC is oriented so that the neuron's preferred response (old for\n    FS, new for NS) above 0.5 means selectivity, the reading under which the paper's \"AUC was\n    significantly higher for high than low confidence\" holds across both types. Open, which neurons\n    are kept, (a) at least ten correct novel and ten correct familiar trials, as the Methods say, or\n    (b) at least ten trials in each of the groups compared; O-M then applies. High against low AUC by\n    the paired permutation t-test of P. Reproduced when, under both readings, high exceeds low at p <\n    0.05; the number of neurons kept (41 in the paper) is reported.\n- id: fig4c-overlap-chance\n  statement: 20 hippocampal neurons are both memory-selective and category neurons, an overlap no\n    greater than chance.\n  source: Results, Activity during WM maintenance is linked to subsequent memory signal, paragraph 3;\n    Figure 4c\n  quote: Of the 53 MS neurons and the 104 category neurons, 20 neurons (37.8% of MS cells; 19.2 % of\n    category neurons) were part of both groups ... This revealed that the overlap between category\n    neurons and MS cells was not significantly higher than chance (Fig. 4c; p = 0.11)\n  statistics:\n  - test: permutation test against random selection, 1000 repetitions\n    p: 0.11\n    n: 351 hippocampal neurons\n  depends_on:\n  - category-neuron-counts\n  - ms-neuron-counts\n  expected:\n  - {quantity: hippocampal neurons both MS and category, value: 20, tolerance: 2}\n  criterion: With the hippocampal category and MS sets of C and M, the overlap count; the null as the\n    paper describes, drawing as many hippocampal neurons as there are category neurons, without\n    replacement, 1000 times, and counting how many are MS; p as the fraction of draws with an\n    overlap at least the observed (a standard choice; the seed likewise). The absence part is judged\n    on this test at p < 0.05. Reproduced when the overlap is within tolerance and p >= 0.05; partially\n    reproduced when p >= 0.05 but the overlap is outside tolerance.\n- id: fig4d-category-no-memory-signal\n  statement: During LTM retrieval, hippocampal category neurons code neither familiarity nor confidence\n    for pictures of their preferred category.\n  source: Results, Activity during WM maintenance is linked to subsequent memory signal, paragraph 4;\n    Figure 4d\n  quote: None of the effects revealed significant modulations of FRs (Fig. 4d top; confidence beta =\n    6.05, p = 0.28; familiarity beta = 4.49, p = 0.71; confidence × familiarity beta = −4.32, p = 0.57).\n    To further confirm this result, we directly compared FRs of category neurons between preferred old\n    and new items and did not observe a significant difference (Fig. 4d bottom; t(94) = −0.28, p =\n    0.78).\n  statistics:\n  - about: confidence\n    test: mixed-effects GLM\n    p: 0.28\n  - about: familiarity\n    test: mixed-effects GLM\n    p: 0.71\n  - about: confidence by familiarity\n    test: mixed-effects GLM\n    p: 0.57\n  - about: preferred old against new\n    test: permutation-based t-test\n    statistic: t(94) = -0.28\n    p: 0.78\n    n: 95 hippocampal category neurons\n  depends_on:\n  - category-neuron-counts\n  criterion: A claim of absence, judged on the paper's two tests. Hippocampal category neurons of C;\n    correct LTM trials showing a picture of the neuron's preferred category; rate 0.2 to 1.2 s after\n    picture onset; the GLM of G with fixed effects confidence (continuous, 3 levels), familiarity\n    (old or new) and their interaction; and, per neuron, mean rate of preferred old against preferred\n    new pictures by the paired permutation t-test of P, after O-M. Open, (D1) the confidence coding,\n    (a) the coding of the Fig. 3a code (sure new 1 to guessing new 3, guessing old 1 to sure old 3) or\n    (b) certainty, sure 3, unsure 2, guessing 1 for both responses; (D2) the rate, (a) spikes per\n    second in the window, the measure the text names, or (b) normalized as B to the WM baseline, the\n    only baseline the paper defines. Reproduced when no GLM effect and not the t-test reach p < 0.05\n    under every reading; not reproduced when any does under every reading.\n- id: fig4e-fs-strong-maintenance\n  statement: Familiarity-selective hippocampal neurons respond more during LTM retrieval to familiar\n    pictures that were held with strong, compared with weak, maintenance activity of a simultaneously\n    recorded category neuron.\n  source: Results, Activity during WM maintenance is linked to subsequent memory signal, paragraphs 5\n    and 6; Figure 4e; STAR Methods, Interaction between simultaneously recorded category- and\n    memory-selective neurons\n  quote: This analysis revealed that FRs of familiarity-selective MS cells during LTM retrieval of items\n    that were previously accompanied by high persistent activity in the WM task were higher than those\n    previously accompanied by low persistent activity (Fig. 4e left; Maintenance FR beta = 14.63, p =\n    1.39 × 10−3)\n  statistics:\n  - about: strong against weak maintenance, GLM\n    test: mixed-effects GLM\n    p: 0.00139\n    n: 76 FS and category neuron pairs\n  - about: strong against weak maintenance, per pair\n    test: permutation-based t-test\n    statistic: t(75) = 3.43\n    p: 0.0003\n    n: 76 FS and category neuron pairs\n  depends_on:\n  - category-neuron-counts\n  - ms-neuron-counts\n  expected:\n  - {quantity: MS and category neuron pairs, value: 198, tolerance: 20}\n  - {quantity: FS pairs, value: 76, tolerance: 8}\n  - {quantity: maintenance beta, value: 14.63, tolerance: 1.46}\n  criterion: Pairs of a hippocampal MS neuron (M) and a hippocampal category neuron (C) of the same\n    session. Per category neuron, its maintenance rates (0 to 2.5 s) in correct WM trials holding a\n    preferred picture later shown in the LTM test, median-split into strong and weak separately within\n    load 1 and load 3 trials (Methods); a rate equal to the median goes to weak (a standard choice).\n    The MS neuron's rate 0.2 to 1.2 s after onset of those pictures in the LTM test. The GLM of G\n    with the fixed effect maintenance (strong or weak), FS pairs only; and, per pair, the mean MS\n    rate after strong against after weak by the paired permutation t-test of P (O-M applied). Open\n    (the Methods sentence on this GLM lost its variable names), (E1) the random intercept within\n    patient is (a) the MS neuron or (b) the pair; (E2) the LTM trials are (a) all trials of those\n    old pictures or (b) only those answered old; (E3) a neuron that is both MS and category is (a)\n    paired with itself or (b) not; (E4) the rate is (a) spikes per second or (b) normalized as B to\n    the WM baseline. Reproduced when, under the readings, both tests give strong above weak at p <\n    0.05; partially reproduced when one of them does under every reading. The pair counts and beta\n    are compared with expected values as a report, since E3 changes the counts.\n- id: fig4f-ns-no-effect\n  statement: The response of novelty-selective hippocampal neurons to familiar pictures does not\n    depend on whether the paired category neuron's maintenance activity was strong or weak.\n  source: Results, Activity during WM maintenance is linked to subsequent memory signal, paragraphs 5\n    and 6; Figure 4f\n  quote: No significant relationship was observed for the activity of novelty-selective MS neurons\n    (Fig. 4f left; Maintenance FR beta = 0.09, p = 0.98)\n  statistics:\n  - about: GLM\n    test: mixed-effects GLM\n    p: 0.98\n    n: 122 NS and category neuron pairs\n  - about: per pair\n    test: permutation-based t-test\n    statistic: t(121) = -0.48\n    p: 0.64\n    n: 122 NS and category neuron pairs\n  depends_on:\n  - fig4e-fs-strong-maintenance\n  criterion: A claim of absence, judged on the paper's two tests of fig4e-fs-strong-maintenance applied\n    to NS pairs, with the same readings. Reproduced when neither test has p < 0.05 under every\n    reading; not reproduced when either does under every reading. The number of NS pairs (122 in the\n    paper) and the beta are reported.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001187/10.1016-j.neuron.2024.09.013.yaml paper/10.1016-j.neuron.2024.09.013.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The failures are all quotes where I dropped the paper's colons to satisfy the YAML rule. I'll restore them verbatim inside double-quoted scalars (the rule applies to plain scalars only).

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='claims/001187/10.1016-j.neuron.2024.09.013.yaml'
s=open(p).read()
reps=[
("""  quote: In the WM task, patients performed with higher accuracy (Fig. 1c; load 1 – load 3 t(45) = 4.89,
    p < 0.0001""","""  quote: "In the WM task, patients performed with higher accuracy (Fig. 1c; load 1 – load 3: t(45) =
    4.89, p < 0.0001\""""),
("""  quote: and faster (mean RT high 1.83 ± 0.57 s; mean RT low 2.62 ± 0.66 s; t(44) = −11.13, p < 0.0001)
    when patients""","""  quote: "and faster (mean RT high: 1.83 ± 0.57 s; mean RT low: 2.62 ± 0.66 s; t(44) = −11.13, p <
    0.0001) when patients"""),
("""in their responses
  statistics:""","""in their responses"
  statistics:"""),
("""  quote: In the hippocampus, category neurons remained persistently active throughout the maintenance
    period (intercept beta = 17.86""","""  quote: "In the hippocampus, category neurons remained persistently active throughout the maintenance
    period (intercept: beta = 17.86"""),
("""    preferred category beta = 12.47, p = 8.82 × 10−7)""","""    preferred category: beta = 12.47, p = 8.82 × 10−7)\""""),
("""  quote: In the amygdala, category neurons also remained persistently active throughout the maintenance
    period across all correct trials (intercept beta = 9.78""","""  quote: "In the amygdala, category neurons also remained persistently active throughout the maintenance
    period across all correct trials (intercept: beta = 9.78"""),
("""    preferred than unpreferred categories (Fig. 2e; preferred category beta = 6.91, p = 9.38 × 10−7)""","""    preferred than unpreferred categories (Fig. 2e; preferred category: beta = 6.91, p = 9.38 × 10−7)\""""),
("""    accuracy (correct – incorrect beta = −6.13; p = 0.24) was not significant""","""    accuracy (correct – incorrect: beta = −6.13; p = 0.24) was not significant\""""),
("""  quote: using only preferred trials category neurons in the amygdala""","""  quote: "using only preferred trials category neurons in the amygdala"""),
("""  quote: We did not observe any significant main effects""","""  quote: "We did not observe any significant main effects"""),
("""    showed significant modulations (confidence × area beta = 16.88, p = 0.025; LTM accuracy × area
    beta = 59.78, p = 0.0030; confidence × LTM accuracy × area beta = −28.64, p = 0.0029)""","""    showed significant modulations (confidence × area: beta = 16.88, p = 0.025; LTM accuracy × area:
    beta = 59.78, p = 0.0030; confidence × LTM accuracy × area: beta = −28.64, p = 0.0029)\""""),
("""  quote: in the hippocampus but not in the amygdala (confidence beta = 1.54, p = 0.69; LTM accuracy
    beta = −2.27, p = 0.82; confidence × LTM accuracy beta = 1.02, p = 0.83)""","""  quote: "in the hippocampus but not in the amygdala (confidence: beta = 1.54, p = 0.69; LTM accuracy:
    beta = −2.27, p = 0.82; confidence × LTM accuracy: beta = 1.02, p = 0.83)\""""),
("""  quote: None of the effects revealed significant modulations of FRs (Fig. 4d top; confidence beta =
    6.05, p = 0.28; familiarity beta = 4.49, p = 0.71; confidence × familiarity beta = −4.32, p = 0.57).""","""  quote: "None of the effects revealed significant modulations of FRs (Fig. 4d top; confidence: beta =
    6.05, p = 0.28; familiarity: beta = 4.49, p = 0.71; confidence × familiarity: beta = −4.32, p = 0.57)."""),
("""    0.78).
  statistics:""","""    0.78).\"
  statistics:"""),
("""  quote: This analysis revealed that FRs of familiarity-selective""","""  quote: "This analysis revealed that FRs of familiarity-selective"""),
("""    previously accompanied by low persistent activity (Fig. 4e left; Maintenance FR beta = 14.63, p =
    1.39 × 10−3)""","""    previously accompanied by low persistent activity (Fig. 4e left; Maintenance FR: beta = 14.63, p =
    1.39 × 10−3)\""""),
("""  quote: No significant relationship was observed for the activity of novelty-selective MS neurons
    (Fig. 4f left; Maintenance FR beta = 0.09, p = 0.98)""","""  quote: "No significant relationship was observed for the activity of novelty-selective MS neurons
    (Fig. 4f left; Maintenance FR: beta = 0.09, p = 0.98)\""""),
]
for a,b in reps:
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/001187/10.1016-j.neuron.2024.09.013.yaml paper/10.1016-j.neuron.2024.09.013.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes. Final checks for style rules (em dashes, "rather", colon-space in plain scalars):

**Agent calls Bash**

```bash
f=claims/001187/10.1016-j.neuron.2024.09.013.yaml; grep -n "—\|rather" $f; python3 - <<'EOF'
import yaml
f='claims/001187/10.1016-j.neuron.2024.09.013.yaml'
d=yaml.safe_load(open(f))
lines=open(f).read().split('\n')
# find plain scalars containing ': '
ev=yaml.parse(open(f))
for e in ev:
    if isinstance(e,yaml.ScalarEvent) and e.style is None and ': ' in e.value:
        print('PLAIN COLON',e.start_mark.line+1,e.value[:60])
c=d['claims']
print(len(c),'claims;',sum('quote' in x for x in c),'quotes;',sum('inferred' in x for x in c),'inferred;',sum('statistics' in x for x in c),'with statistics;',sum('criterion' in x for x in c),'criteria;',sum('expected' in x for x in c),'with expected')
EOF
```

```
29 claims; 28 quotes; 1 inferred; 25 with statistics; 29 criteria; 14 with expected
```

**Agent**

I've written `claims/001187/10.1016-j.neuron.2024.09.013.yaml`. The quote checker passes with 0 problems (29 claims, 28 quotes, 43 statistical values checked), and the file has no em dashes, no "rather" and no colon-space in plain scalars. Nothing is committed.

**Text read**
- **Paper:** the accepted author manuscript from PubMed Central (PMC11624075). It has the full Results, figure legends and STAR Methods.
- **Supplement:** NIHMS2025394-supplement-1, with Figures S1 to S4 and Table S1.
- **Preprint:** I searched the bioRxiv preprint (v1) for method details only; it adds none.
- **Figures:** I could not view the main-text figures, because only the supplement PDF was supplied.
- **Code:** github.com/rutishauserlab/SBCAT-NO-release-NWB at commit 6d07204. It covers the behaviour plots, the 0.1 Hz rate filter, how category and memory-selective neurons are chosen, and the Fig. 3a GLM. There is no code for Fig. 2b–f, 3b–h or 4b–g.

**Counts**
- 29 claims: 28 quoted, 1 inferred (the per-session unit counts in Table S1).
- 25 claims record statistics, all 29 have criteria, and 14 have expected values.
- 10 are claims of absence, judged on the paper's own test.

**Method choices (code over Methods)**
- **How outlier neurons are removed:** the Methods say ±3 SD from the mean. The Fig. 3a code removes neurons above 3 SD of the neuron means, upper side only and not centred on the mean. The Methods rule is the main reading and the code's is a variant.
- **Confidence coding (1–6) and the baseline:** both are taken from the code, and the author must check the coding in the dataset.
- **Behaviour tolerances:** I used the standard error of the mean (the stated SD divided by √n) instead of the stated SD or the 10% default, since these are means of the same sessions. The reason is given in the file.

**Details the paper leaves open, with the readings named**
- **Fig. 2 baseline:** the mean over all WM trials, or over the rows of the code's table.
- **Fig. 2b, e rows:** one row per trial, or one row per picture as the code does.
- **Fig. 2c, f model:** main effects only, or with the accuracy × load interaction.
- **Fig. 1e and the LTM response times:** low confidence as unsure and guessing pooled (the code), or as the mean of the two. Response times above 5 s excluded or kept.
- **Fig. 3b outlier step:** applied over both areas together, or within each area.
- **Fig. 3c, 3e units:** baseline-normalised rates or spikes per second.
- **Fig. 3e binning:** 200 ms windows in 25 ms steps (Fig. 2a legend), or 50 ms bins (the code). The cluster-forming threshold is not given; I took FieldTrip's default of 0.05 and noted that it could change the cluster's extent.
- **Fig. 3g rows:** all non-preferred pictures, or only trials holding no preferred picture.
- **Fig. 3h rows:** trials whose first picture is preferred, or trials with a preferred picture in any slot.
- **Fig. 4b which neurons:** at least 10 correct trials per class, or at least 10 in each group compared. The AUC is oriented to each neuron's preferred direction.
- **Fig. 4d:** two confidence codings, and spikes per second or rates normalised to the WM baseline.
- **Fig. 4e, f:** the random intercept is the MS neuron or the pair; all old-picture LTM trials or hits only; whether a neuron that is both types is paired with itself; and the rate units. The Methods sentence on this GLM lost its variable names.
- **Standard choices that cannot change an outcome:** the d′ correction, which side of the median ties go to, ≥ for the Fig. 4c p-value, and permutation seeds.

**Missing from the paper**
- **Neuron totals don't agree:** Table S1's recorded units sum to 973, against 950 isolated and 883 analysed in the Methods. The session-count claims allow for this.
- **Healthy controls:** the data of the 100 healthy participants (Fig. S1) are neither deposited nor located, so I made no claim for them.
- **Missing units:** no text gives the axis units of Fig. 3c–f and 4d–g, so they are named as open readings.
- **Whole analyses without code:** nothing a claim needed is entirely absent, but every analysis except Fig. 3a, the neuron selection and the behaviour plots rests on the Methods and legends alone.

## End of run

26 turns, 7 minutes, result: success.
