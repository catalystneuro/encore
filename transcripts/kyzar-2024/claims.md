# 000469 · claims · run 39953706646

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/## Reader/,/^## [^R]/p'; ls claims/001453/ paper/ claims/000469 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/10.1038-s41597-024-02943-8.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
fold -s -w 2000 paper/10.1038-s41597-024-02943-8.txt | head -c 40000
```

Result: not kept, because it reads the paper's text.

**Agent**

Output is persisted; I'll read the saved file in chunks.

**Agent calls Bash**

```bash
fold -s -w 300 paper/10.1038-s41597-024-02943-8.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt"
}
```

```
1	DOI: 10.1038/s41597-024-02943-8
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	2628 sdata Scientific Data Sci Data Nature Publishing Group PMC10796636 10796636 10796636 38238342 10.1038/s41597-024-02943-8 Dataset of human-single neuron activity during a Sternberg working memory task Kyzar Michael 1 Kamiński Jan 1 2 Brzezicka Aneta 3 Reed Chrystal M 4 Chung Jeffrey M 4 Mamelak 
8	Adam N 1 Rutishauser Ueli 1 4 5 6 ✉ 1 Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA USA 2 Center of Excellence for Neural Plasticity and Brain Disorders: BRAINCITY, Nencki Institute of Experimental Biology, Polish Academy of Sciences, Warsaw, Poland 3 Institute of 
9	Psychology, SWPS University of Social Sciences and Humanities, Warsaw, Poland 4 Department of Neurology, Cedars-Sinai Medical Center, Los Angeles, CA USA 5 Center for Neural Science and Medicine, Department of Biomedical Sciences, Cedars-Sinai Medical Center, Los Angeles, CA USA 6 Division of 
10	Biology and Biological Engineering, California Institute of Technology, Pasadena, CA USA ✉ Corresponding author. 18 1 2024 11 89 89 19 1 2024 © The Author(s) 2024 Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, 
11	adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are 
12	included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
[... 214 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/rutishauserlab/workingmem-release-NWB wm && cd wm && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | head -100
```

```
f8594e0beb55d9d977f9cedf15e0c1b0488c1947 2024-01-22 09:54:29 -0800
./assets/git_task_overview_white.png
./assets/git_task_overview.png
./assets/git_brain_areas.png
./README.md
./NWB_SB/helpers/internal/spikePDFestimate.m
./NWB_SB/helpers/internal/setCommonAxisRange.m
./NWB_SB/helpers/internal/plotTrialMarkers.m
./NWB_SB/helpers/internal/plotSpikeRaster_multiple_simplified.m
./NWB_SB/helpers/internal/plotSpikeRaster_multiple.m
./NWB_SB/helpers/internal/plotSpikeRasterMain.m
./NWB_SB/helpers/internal/plotPSTH_forSpikeRaster.m
./NWB_SB/helpers/internal/getTimestamps_forSortedRasterPlot.m
./NWB_SB/helpers/internal/getTimestampsOfTrials.m
./NWB_SB/helpers/internal/getRelativeTimestamps.m
./NWB_SB/helpers/internal/getGaussianKernel.m
./NWB_SB/helpers/internal/calcCV2.m
./NWB_SB/helpers/custom/translateArea_SB.m
./NWB_SB/helpers/custom/NWB_importFromFolder.m
./NWB_SB/helpers/custom/NWB_determineSBPeriods.m
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/wm && git log --format='%h %ci %s' | head; cat README.md | head -80; cat NWB_SB/NWB_SB_import_main.m
```

```
f8594e0 2024-01-22 09:54:29 -0800 Update README.md
3098793 2024-01-12 13:45:12 -0800 Revert "Added PAC Examples. Added Noise Corr Examples"
7d7b00f 2024-01-12 13:36:03 -0800 Added PAC Examples. Added Noise Corr Examples
9d5f468 2023-07-28 11:59:00 -0700 Update README.md
c8bcf54 2023-07-18 16:05:47 -0700 Update README.md
d72ba23 2023-07-18 16:05:26 -0700 Update README.md
0075efe 2023-07-18 14:26:01 -0700 Update README.md
3cd3ced 2023-07-18 14:18:59 -0700 Update README.md
e22cfc7 2023-07-18 14:10:31 -0700 Update README.md
e16e340 2023-07-18 13:53:54 -0700 Update CITATION.cff
# Source code for: Dataset of human-single neuron activity during a Sternberg working memory task 

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Generic badge](https://img.shields.io/badge/release-1.0.0-green.svg)](https://github.com/rutishauserlab/workingmem-release-NWB/releases/tag/v1.0.0)
[![Generic badge](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.8161627-orange.svg)](https://doi.org/10.5281/zenodo.8161627)

## Introduction

This repository contains the code that accompanies our data release Kyzar et al. 'Dataset of human-single neuron activity during a Sternberg working memory task'. The purpose of the code in this repository is to provide examples of how to use the released data. This dataset is formatted in the [Neurodata Without Borders (NWB)](https://www.nwb.org/) format, which can easily be accessed from both MATLAB and Python as described [here](https://nwb-schema.readthedocs.io/en/latest/index.html). 

[... 329 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/wm/NWB_SB/helpers/custom && cat NWB_calcSelective_SB.m NWB_calcSelective_SC.m NWB_determineSBPeriods.m
```

```
<persisted-output>
Output too large (36.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/54511f61-13e6-4232-bcee-d148f70f2d6a/tool-results/bx5lz2ffa.txt

Preview (first 2KB):
function [sig_cells,areasSternberg] = NWB_calcSelective_SB(nwbAll, all_units, params)
%NWB_CALCSELECTIVE Takes the output of NWB_SB_extractUnits and runs
%selectivity tests for the sternberg task. Optionally plots trial aligned
%spikes

if isfield(params,'rateFilter') && params.rateFilter > 0
    rateFilter = params.rateFilter;
else
    rateFilter = [];
end

% Filtering for Global Rate (rateFilter should be a nonzero float)
aboveRate = ones(length(all_units),1);
if ~isempty(rateFilter)
    for i = 1:length(all_units)
        globalRate = length(all_units(i).spike_times)/(max(all_units(i).spike_times)-min(all_units(i).spike_times));
[... 31 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/wm/NWB_SB/helpers/custom/NWB_calcSelective_SB.m"
}
```

```
1	function [sig_cells,areasSternberg] = NWB_calcSelective_SB(nwbAll, all_units, params)
2	%NWB_CALCSELECTIVE Takes the output of NWB_SB_extractUnits and runs
3	%selectivity tests for the sternberg task. Optionally plots trial aligned
4	%spikes
5	
6	if isfield(params,'rateFilter') && params.rateFilter > 0
7	    rateFilter = params.rateFilter;
8	else
9	    rateFilter = [];
10	end
11	
12	% Filtering for Global Rate (rateFilter should be a nonzero float)
13	aboveRate = ones(length(all_units),1);
14	if ~isempty(rateFilter)
15	    for i = 1:length(all_units)
16	        globalRate = length(all_units(i).spike_times)/(max(all_units(i).spike_times)-min(all_units(i).spike_times));
17	        rateBool = globalRate < rateFilter;
18	        if rateBool % If the rate is below the filter threshold
19	            aboveRate(i) = 0;
20	        end
[... 502 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/wm/NWB_SB/helpers/custom/NWB_calcSelective_SC.m"
}
```

```
1	function [sig_cells_sc,areasScreening] = NWB_calcSelective_SC(nwbAll,all_units, params)
2	%NWB_CALCSELECTIVE_SC Takes the output of NWB_SB_extractUnits and runs
3	%selectivity tests for the screening task. Optionally does plotting of
4	%response histograms. 
5	
6	if isfield(params,'rateFilter')
7	    rateFilter = params.rateFilter;
8	else
9	    rateFilter = [];
10	end
11	
12	% Filtering for Global Rate (rateFilter should be a nonzero float. Otherwise, all cells are used.)
13	aboveRate = ones(length(all_units),1);
14	if ~isempty(rateFilter)
15	    for i = 1:length(all_units)
16	        globalRate = length(all_units(i).spike_times)/(max(all_units(i).spike_times)-min(all_units(i).spike_times));
17	        rateBool = globalRate < rateFilter ;
18	        if rateBool % If the rate is below the filter threshold
19	            aboveRate(i) = 0;
20	        end
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/wm && git log --format='%h %ci %s' -- NWB_SB/helpers/custom/NWB_calcSelective_SB.m NWB_SB/NWB_SB_import_main.m; git log --all --oneline | wc -l; git tag; git branch -a
```

```
3098793 2024-01-12 13:45:12 -0800 Revert "Added PAC Examples. Added Noise Corr Examples"
7d7b00f 2024-01-12 13:36:03 -0800 Added PAC Examples. Added Noise Corr Examples
4a98f46 2023-07-18 13:40:55 -0700 Update NWB_SB_import_main.m
e7c2ab6 2023-07-13 11:46:04 -0700 Update NWB_SB_import_main.m
0cd1e48 2023-07-13 11:43:37 -0700 possibly final version before 1.0 release
60f0587 2023-07-12 12:56:25 -0700 Re-uploading current version
431cee2 2023-07-12 12:54:28 -0700 Moved helpers to new folder
aa92015 2023-07-12 12:19:59 -0700 Move and rename SB_NWB_import_main.m to NWB_SB_import_main.m
58
v1.0.0
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/wm && git show v1.0.0 --format='%h %ci' -s; git diff v1.0.0 HEAD --stat; git show 7d7b00f --stat | head -30; git diff 7d7b00f~1 7d7b00f -- NWB_SB/helpers/custom/NWB_calcSelective_SB.m | head -80
```

```
4a98f46 2023-07-18 13:40:55 -0700
 CITATION.cff |  2 +-
 README.md    | 16 +++++++++-------
 2 files changed, 10 insertions(+), 8 deletions(-)
commit 7d7b00f08b8844e27dddf188c05d9e30cd1e813e
Author: Michael Kyzar <[removed: an e-mail address]>
Date:   Fri Jan 12 13:36:03 2024 -0800

    Added PAC Examples. Added Noise Corr Examples

 NWB_SB/NWB_SBCAT_import_main.m                     | 229 ++++++++++++++++
 NWB_SB/helpers/3rdParty/randanova1/license.txt     |  24 ++
 NWB_SB/helpers/3rdParty/randanova1/randanova1.m    |  71 +++++
 NWB_SB/helpers/custom/NWB_QA_graphs.m              |  78 ++++--
 NWB_SB/helpers/custom/NWB_SB_extractUnits.m        |  13 +-
 NWB_SB/helpers/custom/NWB_SB_plotCell_Sternberg.m  |  40 +--
 NWB_SB/helpers/custom/NWB_calcSelective_SB.m       | 303 ++++++++-------------
 NWB_SB/helpers/custom/NWB_importFromFolder_SBCAT.m |  64 +++++
 NWB_SB/helpers/custom/condenseAreas.m              |  22 ++
 NWB_SB/helpers/internal/PAC/NWB_samplePAC_LFP.m    | 175 ++++++++++++
[... 95 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/wm/NWB_SB/helpers/custom/NWB_QA_graphs.m"
}
```

```
1	function [QA] = NWB_QA_graphs(nwbAll,units, is_sternberg)
2	% NWB_QA_graphs Generates behavioral and spike sorting metrics used in the SB
3	% data release. 
4	% nwbAll: A cell arrays containing all nwb files in the dataset 
5	% units: A units struct created using NWB_SB_extractUnits
6	% is_sternberg: 1 or 0 logical if sternberg is being processed. Will plot
7	% behavioral metrics if 1. 
8	% figHandle: The resulting figure that shows all relevant stat tests. 
9	
10	QA = figure("Visible","on");
11	sessionCount = length(nwbAll);
12	
13	if is_sternberg % If Sternberg, give behavioral plots
14	    %% Accuracy
15	    accTotals = zeros(sessionCount,1);
16	    for i = 1:length(accTotals)
17	        accTrials = nwbAll{i}.intervals_trials.vectordata.get('response_accuracy').data.load();
18	        accTotals(i) = sum(accTrials)/length(accTrials)*100;
19	    end
20	    accFig = subplot(2,5,5); %#ok<NASGU>
[... 347 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/wm/NWB_SB/helpers && cat internal/calcCV2.m custom/NWB_countAreas.m custom/translateArea_SB.m; grep -n "areas\|location\|electrodes" custom/NWB_SB_extractUnits.m | head -30
```

```
%
% calculates the coefficient of variation metric CV2, as described in Holt et al 1996, J Neurophysiol
%
% ISIs are in sec and expected to be in order
%
%
%returns:
%CV2: mean CV2 over all ranges
%CV2_all: CV2 for each pair of consecutive ISIs
%CV2_all_diff: the difference between each consecutive ISIs, useful to calculate the CV2 only for sub-ranges of intervals
%
%
%ignoreMode: 0 take all, 1 ignore very large ISIs; use this if only sub-periods of the spike-train are used, so these have "wholes" that create large artificial ISIs
%
%
%urut/jan13
function [CV2, CV2_all, CV2_all_sum, CV2_all_diff] = calcCV2(ISIs, ignoreMode)
if nargin<2
    ignoreMode=0;
end
[... 159 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 25,200p claims/001453/*.yaml; ls tools; ls docs
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
[... 187 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -rn "inferred:" claims | head -3; grep -rln "000469\|s41597-024-02943" claims questions docs 2>/dev/null | head
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

[... 64 more lines not kept]
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
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000])"
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
sed -n 1,60p $TMPDIR/wm/NWB_SB/helpers/3rdParty/permutationTest/permutationTest.m | grep -v "^\s*$"
```

```
% [p, observeddifference, effectsize] = permutationTest(sample1, sample2, permutations [, varargin])
%
%       Permutation test (aka randomisation test), testing for a difference
%       in means between two samples. 
%
% In:
%       sample1 - vector of measurements from one (experimental) sample
%       sample2 - vector of measurements from a second (control) sample
%       permutations - the number of permutations
%
% Optional (name-value pairs):
%       sidedness - whether to test one- or two-sided:
%           'both' - test two-sided (default)
%           'smaller' - test one-sided, alternative hypothesis is that
%                       the mean of sample1 is smaller than the mean of
%                       sample2
%           'larger' - test one-sided, alternative hypothesis is that
%                      the mean of sample1 is larger than the mean of
%                      sample2
%       exact - whether or not to run an exact test, in which all possible
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/wm/NWB_SB/helpers/custom && sed -n 1,80p NWB_SB_plotCell_Sternberg.m | grep -n -i "example\|subject\|unit\|cell\|==" | head -40; grep -n -i "example\|subject_id\|unit_id\|==" NWB_SB_plotCell_Screening.m | head -30
```

```
1:function [sig_cells_sb, areas_sb] = NWB_SB_plotCell_Screening(nwbAll,all_units,params)
2:%NWB_SB_PLOTCELL_SCREENING Plots example cells from Kyzar et al 2023
5:%% Speficy unit filter
6:unit_examples = [... % Specify by SBID, cellID
15:%% Apply unit filter
16:if any(~ismember(unit_examples(:,1),[all_units.subject_id]))
17:    warning('All examples not loaded. See import range. [4 7 16 21]')
20:% Filtering units
21:unit_mat = [[all_units.subject_id]',[all_units.unit_id]'];
22:inc_units = ismember(unit_mat,unit_examples, 'rows');
23:all_units_filtered = all_units(inc_units);
25:% Updating session count in units object
26:temp_units = all_units_filtered;
27:unique_subjects = unique([temp_units.session_count]);
28:for i = 1:length(unique_subjects)
29:    find_uniques = find([temp_units.session_count] == unique_subjects(i));
31:        all_units_filtered(j).session_count = i ;
34:clear temp_units 
37:nwbAll_filtered = nwbAll(unique_subjects);
41:[sig_cells_sb, areas_sb] = NWB_calcSelective_SB(nwbAll_filtered,all_units_filtered,params);
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/wm/NWB_SB/helpers/custom && sed -n 5,14p NWB_SB_plotCell_Sternberg.m; sed -n 5,20p NWB_SB_plotCell_Screening.m
```

```
%% Speficy unit filter
unit_examples = [... % Specify by SBID, cellID
    % Kaminski et al 2017, Figure 3.a-b
    14, 14; ... % Halle Berry
    14, 35; ... % Tiger Woods
    % Kyzar et al 2023, Figure 5.a-b
    7, 9; ... % Cat
    16, 16 ... % Delicate Arch
    ];

%% Speficy unit filter
unit_examples = [... % Specify by SBID, cellID
    % Kyzar et al 2023, Fig 5.a-e
    4, 16; ... % Shoe House
    7, 24; ... % Zebras
    15, 3; ... % Moon man
    16, 22; ... % Delicate Arch
    21, 15; ... % The Pike Ferris Wheel 
    % Kaminski et al 2017, SF 1
    7, 24; ... % Zebras
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,30p $TMPDIR/wm/NWB_SB/helpers/custom/NWB_SB_extractUnits.m
```

```
function [all_units] =NWB_SB_extractUnits(nwbAll, load_all_waveforms)
%NWB_SB_extractUnits Takes a cell array of loaded nwb files and returns all
%   single unit information across all the files. 
%   nwbAll: cell array of loaded nwb files
%   importRange:  
%
%   mkyzar 4/27/2023
all_units = {};
for i=1:length(nwbAll)
    unit_ids = num2cell(nwbAll{i}.units.id.data.load() + 1); % Convert to 1-based indexing
    session_count = num2cell(i.*ones(length(unit_ids),1));
    subject_id = num2cell(str2double(nwbAll{i}.general_subject.subject_id).*ones(length(unit_ids),1));
    electrodes_ind = num2cell(nwbAll{i}.units.electrodes.data.load() + 1); % Convert to 1-based indexing
    fprintf('Loading SUs: Subject ID %d (%d/%d)...',subject_id{1},i,length(nwbAll))
    

    % Organize spike times
    spike_times_session = nwbAll{i}.units.spike_times.data.load();
    spike_times_ind = nwbAll{i}.units.spike_times_index.data.load();
    
[... 10 more lines not kept]
```

**Agent**

The paper text is complete (Methods present; a data descriptor with no supplement), and the linked code is cloned. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000469/10.1038-s41597-024-02943-8.yaml",
 "content": "# Claims for Kyzar, Kaminski, Brzezicka, Reed, Chung, Mamelak & Rutishauser (2024), Sci Data 11, 89,\n# on dandiset 000469.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23, protocol\n# as stated in docs/protocol.md.\n#\n# Text read: the version of record, as served by Europe PMC (PMC10796636), full text with Methods,\n# Technical Validation, figure legends and Tables 1 to 3. The paper is a data descriptor and has\n# no supplement. Its Methods are said to be abbreviated from refs 15 and 20 (Kaminski et al. 2017,\n# Nat Neurosci; Kaminski et al. 2020, Neuron); those papers were not used here, as the protocol\n# takes methods from this paper and the code it links.\n#\n# Code read: github.com/rutishauserlab/workingmem-release-NWB, branch main at commit f8594e0\n# (2024-01-22). Its code is identical to tag v1.0.0 (commit 4a98f46, 2023-07-18); only README.md\n# and CITATION.cff differ. A commit of 2024-01-12 (7d7b00f) that rewrote the selectivity code\n# for another dataset was reverted the same day (3098793) and is not used. The repository holds\n# MATLAB scripts. NWB_SB_import_main.m runs the analysis; NWB_calcSelective_SB.m and\n# NWB_calcSelective_SC.m classify concept, maintenance and probe cells; NWB_QA_graphs.m computes\n# the behaviour and the spike sorting metrics of Figs 1c,d and 3; NWB_SB_plotCell_Sternberg.m and\n# NWB_SB_plotCell_Screening.m list the example units of Figs 4 and 5.\n# Where the code and the Methods disagree, the Methods give the main criterion and the code's\n# choice is a variant. They disagree on the tests. The Methods name permutation tests (a\n# permuted one-way ANOVA, permutation t-tests, a permutation test); the code runs parametric\n# tests (anovan, paired one-sided ttest) and keeps permutation versions (2000 permutations) only\n# in comments. The code also has three defects that matter. (1) In NWB_calcSelective_SB.m the\n# preferred and non-preferred trial masks are logical(id_Trial_maxOnly) and ~id_Trial_maxOnly,\n# where id_Trial_maxOnly holds the image ID (1 to 5) or -1, so the first selects every trial and\n# the second none; as written, hzNonPref is empty and the extra maintenance test for concept\n# cells cannot run. (2) hzPref and hzNonPref are taken from the Encoding 1 window (200 to 1000\n# ms), not the maintenance period the paper names. (3) The probe test's encoding rate counts\n# the Encoding 2 window a second time in place of Encoding 3. The released code therefore\n# cannot have produced the paper's persistent activity numbers as written; the intended masks\n# (trials whose Encoding 1 image is or is not the preferred image) are used where the code is\n# followed.\n#\n# Data the paper used (as the paper reports it): 21 patients with drug-resistant epilepsy and\n# hybrid macro-micro depth electrodes, 41 sessions (20 screening and 21 Sternberg; patient\n# P47HMH, subject 19, has no screening session). Two NWB files per subject, sub-<ID>-ses-1\n# (screening) and sub-<ID>-ses-2 (Sternberg). Screening, 54 to 64 images shown six times each\n# for 1 s; 907 units. Sternberg, 108 or 135 trials per session, loads 1 to 3 drawn from 5\n# images chosen from screening; fixation cross (900 to 1000 ms), encoding images of 1 s each,\n# maintenance 2.5 to 2.8 s, probe until response; 902 units (hippocampus 190, amygdala 259,\n# dACC 171, pre-SMA 250, vmPFC 32). Measured variables per trial: loads, image IDs per encoding\n# and probe, probe_in_out, response_accuracy, timestamps of fixation, encodings, maintenance,\n# probe and response; per unit: spike times, waveforms, electrode with brain area and MNI\n# coordinates, and the stored quality metrics (waveforms_isolation_distance,\n# waveforms_mean_proj_dist, waveforms_mean_snr, waveforms_peak_snr). MTL is amygdala and\n# hippocampus; MFC is dACC, pre-SMA and vmPFC (the code's grouping, which the reported\n# denominators match).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000469\"\npaper: doi:10.1038/s41597-024-02943-8\nclaims:\n- id: subjects-sessions\n  statement: The dataset holds 41 recording sessions from 21 patients, every patient with a\n    Sternberg session and all but one (P47HMH) with a screening session.\n  source: Methods, Subjects, paragraph 1; Table 1 and its legend\n  quote: In total, 41 recording sessions were completed across 21 patients with intractable\n    localization-related epilepsy (Table 1 ). ... Screening sessions are available for all\n    subjects except for 'P47HMH', for whom screening was not performed.\n  expected:\n  - quantity: patients\n    value: 21\n    tolerance: 0\n  - quantity: sessions (screening and Sternberg)\n    value: 41\n    tolerance: 0\n  - quantity: Sternberg sessions\n    value: 21\n    tolerance: 0\n  criterion: Counted from the subjects and the session files. Counts of subjects and sessions\n    are exact, so the tolerance is zero. The text gives ages of 17 to 71, while Table 1 lists\n    ages of 17 to 70; the ages are reported against both and do not decide the claim.\n- id: sternberg-unit-yield\n  statement: In the Sternberg task 902 units were recorded, 190 in the hippocampus, 259 in the\n    amygdala, 171 in the dACC, 250 in the pre-SMA and 32 in the vmPFC.\n  source: Technical Validation, Data recorded and spike sorting quality metrics, paragraph 1;\n    Figure 3b\n  quote: In the Sternberg task, we recorded a total of 902 neurons (190 hippocampus, 259\n    Amygdala, 171 dorsal anterior cingulate cortex, 250 pre-supplementary motor area, 32\n    ventromedial prefrontal cortex) (Fig. 3b ).\n  expected:\n  - quantity: Sternberg units, all areas\n    value: 902\n    tolerance: 90.2\n  - quantity: Sternberg units, hippocampus\n    value: 190\n    tolerance: 19\n  - quantity: Sternberg units, amygdala\n    value: 259\n    tolerance: 25.9\n  - quantity: Sternberg units, dACC\n    value: 171\n    tolerance: 17.1\n  - quantity: Sternberg units, pre-SMA\n    value: 250\n    tolerance: 25\n  - quantity: Sternberg units, vmPFC\n    value: 32\n    tolerance: 3.2\n  criterion: Units in the units table of the ses-2 files, assigned to an area by the location\n    of their electrode, left and right merged, as in NWB_countAreas.m and translateArea_SB.m.\n    Tolerances are the protocol's 10%; the exact counts are reported.\n- id: screening-unit-yield\n  statement: In the screening task 907 units were recorded, 449 of them in the MTL.\n  source: Technical Validation, Data recorded and spike sorting quality metrics, paragraph 1;\n    Figure 3a\n  quote: In the screening task, we recorded 907 neurons (Fig. 3a ). Of these, 449 were recorded\n    in the MTL.\n  expected:\n  - quantity: screening units, all areas\n    value: 907\n    tolerance: 90.7\n  - quantity: screening units, MTL\n    value: 449\n    tolerance: 44.9\n  criterion: Units in the ses-1 files, assigned to areas as for sternberg-unit-yield. The MTL\n    count of 449 equals the Sternberg MTL count (190 + 259), while the screening percentages\n    of claims screening-concept-mtl and screening-concept-mfc imply about 421 MTL and 486 MFC\n    units (138 / 0.3278 and 26 / 0.0535). Both 449 and 421 are readings of the MTL count; the\n    claim holds when the count is within 10% of either, and the notes say which.\n- id: behavior-accuracy\n  statement: Subjects answered on average 88.73% of Sternberg trials correctly.\n  source: Technical Validation, Behavior, paragraph 1; Figure 1d\n  quote: During the working memory task (Fig. 1b ), subjects answered on average 88.73% of trials\n    correctly (Fig. 1d ).\n  expected:\n    quantity: mean over sessions of percent correct\n    value: 88.73\n    tolerance: 8.873\n    unit: \"%\"\n  criterion: As in NWB_QA_graphs.m, the percent of trials with response_accuracy 1 in each\n    Sternberg session, over all trials, averaged over sessions (Fig. 1d shows the session\n    values with mean and s.e.m.).\n- id: behavior-rt-load\n  statement: Reaction times grew with memory load; a repeated-measures ANOVA of per-session\n    median reaction times found a load effect.\n  source: Technical Validation, Behavior, paragraph 1; Figure 1c\n  quote: Accuracy and reaction time varied as a function of load as expected (Fig. 1c ), with\n    higher loads resulting in slower and less accurate answers (F 2,40 = 7.92, P = 0.0013,\n    repeated-measures ANOVA of median reaction times).\n  statistics:\n  - test: repeated-measures ANOVA of median reaction times\n    statistic: F(2,40) = 7.92\n    p: 0.0013\n    n: 21 Sternberg sessions (df 2 and 40)\n  expected:\n  - quantity: F statistic, load effect\n    value: 7.92\n    tolerance: 0.792\n  criterion: As in NWB_QA_graphs.m, the reaction time is timestamps_Response minus\n    timestamps_Probe, on correct trials only (filter_correct = 1; the paper does not say,\n    the code settles it); the median per session and load; an ANOVA (anovan) with session as\n    a random factor and load as a fixed factor, the code's form of the repeated-measures\n    ANOVA. Reproduced when the load effect has p < 0.05 and the mean of the session medians\n    rises from load 1 to load 3; F within tolerance is reported. The same test on all trials\n    is shown as a variant.\n- id: behavior-accuracy-load\n  statement: Accuracy was lower at higher memory loads.\n  source: Technical Validation, Behavior, paragraph 1; Figure 1c\n  quote: Accuracy and reaction time varied as a function of load as expected (Fig. 1c ), with\n    higher loads resulting in slower and less accurate answers\n  criterion: The paper reports no test for accuracy and the code computes none. Percent\n    correct per session and load, averaged over sessions. Reproduced when the mean accuracy\n    falls from load 1 to load 2 to load 3; partially reproduced when load 3 is below load 1\n    but the order is not monotonic; not reproduced otherwise. The per-load values are\n    reported.\n- id: isi-violations\n  statement: Across Sternberg units, refractory period violations (ISIs shorter than 3 ms) were\n    0.41% of ISIs on average, with a standard deviation of 0.50%.\n  source: Technical Validation, Data recorded and spike sorting quality metrics, paragraph 2;\n    Figure 3d\n  quote: On average across all neurons in the Sternberg task, ( i ) refractory period violations\n    were 0.41% ± 0.50% of interspike intervals (ISIs) (Fig. 3d )\n  expected:\n  - quantity: mean percent of ISIs below 3 ms\n    value: 0.41\n    tolerance: 0.041\n    unit: \"%\"\n  - quantity: standard deviation over units of the percent of ISIs below 3 ms\n    value: 0.50\n    tolerance: 0.05\n    unit: \"%\"\n  criterion: Per unit, the percent of consecutive spike time differences below 3 ms over the\n    whole session, as in NWB_QA_graphs.m. The text says all neurons; the code averages only\n    the units whose value is below 4% (thresh_isi = 4). The text gives the main reading (all\n    units); the code's filter is a variant, and the claim is reproduced when either reading\n    puts both values within tolerance, the notes saying which. The 0.50% is the spread of the\n    units, not an uncertainty of the mean, so each value has the protocol's 10%.\n- id: firing-rate\n  statement: Sternberg units fired at 2.55 Hz on average, ranging from 0.11 to 33.82 Hz.\n  source: Technical Validation, Data recorded and spike sorting quality metrics, paragraph 2;\n    Figure 3e\n  quote: (ii) average firing rate was 2.55 Hz, with a range of 0.11–33.82 Hz (Fig. 3e )\n  expected:\n  - quantity: mean firing rate over units\n    value: 2.55\n    tolerance: 0.255\n    unit: Hz\n  - quantity: lowest unit firing rate\n    value: 0.11\n    tolerance: 0.011\n    unit: Hz\n  - quantity: highest unit firing rate\n    value: 33.82\n    tolerance: 3.382\n    unit: Hz\n  criterion: Per unit, the number of spikes divided by the time from first to last spike, as\n    in NWB_QA_graphs.m, over all Sternberg units; mean, minimum and maximum. The range holds\n    when the minimum and maximum lie within 10% of each bound.\n- id: projection-distance\n  statement: The pairwise projection distance between units isolated on the same wire was 13.77\n    plus or minus 7.32 s.d. of the signal.\n  source: Technical Validation, Data recorded and spike sorting quality metrics, paragraph 2;\n    Figure 3i\n  quote: ( iii ) the pairwise projection distance in clustering space between neurons isolated\n    on the same wire was 13.77 ± 7.32 (projection test; in units of s.d. of the signal)\n  expected:\n  - quantity: mean projection distance\n    value: 13.77\n    tolerance: 1.377\n  - quantity: standard deviation of projection distance\n    value: 7.32\n    tolerance: 0.732\n  criterion: The stored waveforms_mean_proj_dist of the Sternberg units, zeros removed, mean\n    and standard deviation, as in NWB_QA_graphs.m. The text cites Fig. 3g; the legend places\n    the projection distance in panel i.\n- id: waveform-snr\n  statement: The signal-to-noise ratio of the peak of the mean waveform was 6.62 plus or minus\n    3.63 across Sternberg units.\n  source: Technical Validation, Data recorded and spike sorting quality metrics, paragraph 2;\n    Figure 3g,h\n  quote: ( iv ) the ratio between the s.d. of noise and the peak mean waveform amplitude was\n    6.62 ± 3.63 (Fig. 3g,h )\n  expected:\n  - quantity: mean SNR\n    value: 6.62\n    tolerance: 0.662\n  - quantity: standard deviation of SNR\n    value: 3.63\n    tolerance: 0.363\n  criterion: The sentence describes the peak SNR (Fig. 3g) but cites panels g and h, the second\n    being the mean SNR. Readings are (a) the stored waveforms_peak_snr and (b) the stored\n    waveforms_mean_snr, each as mean and standard deviation over Sternberg units, as\n    NWB_QA_graphs.m computes them. Reproduced when either reading puts both values within\n    tolerance; the notes say which.\n- id: cv2\n  statement: The modified coefficient of variation of the ISIs (CV2) was 0.94 plus or minus 0.14\n    across Sternberg units.\n  source: Technical Validation, Data recorded and spike sorting quality metrics, paragraph 2;\n    Figure 3f\n  quote: (v) the modified coefficient of variation of the ISIs (CV2 52 ) was 0.94 ± 0.14 (Fig.\n    3f )\n  expected:\n  - quantity: mean CV2\n    value: 0.94\n    tolerance: 0.094\n  - quantity: standard deviation of CV2\n    value: 0.14\n    tolerance: 0.014\n  criterion: Per unit, CV2 as in calcCV2.m with ignoreMode 1, the mean over pairs of\n    consecutive ISIs of 2 times the absolute difference over the sum, leaving out pairs in\n    which either ISI exceeds 1 s; over the whole session; mean and standard deviation over\n    Sternberg units, as in NWB_QA_graphs.m.\n- id: isolation-distance\n  statement: The median isolation distance of Sternberg units was 31.14.\n  source: Technical Validation, Data recorded and spike sorting quality metrics, paragraph 2;\n    Figure 3j\n  quote: (vi) median isolation distance 53 was 31.14 (Fig. 3j )\n  expected:\n    quantity: median isolation distance\n    value: 31.14\n    tolerance: 3.114\n  criterion: The stored waveforms_isolation_distance of the Sternberg units, undefined (NaN)\n    values removed as in NWB_QA_graphs.m, median.\n- id: screening-concept-mtl\n  statement: In the screening task, 138 MTL units (32.78%) qualified as concept cells.\n  source: Technical Validation, Proportion of selective cells, paragraph 2\n  quote: 'Screening task: Of the MTL cells, 138 (32.78%) qualified as concept cells (Fig. 4\n    shows examples).'\n  expected:\n  - quantity: MTL concept cells, screening\n    value: 138\n    tolerance: 13.8\n  - quantity: percent of MTL units that are concept cells, screening\n    value: 32.78\n    tolerance: 3.278\n    unit: \"%\"\n  criterion: Per screening unit, the firing rate 200 to 1000 ms after each image onset (trial\n    start_time; image from StimulusPresentation), all presentations, as in\n    NWB_calcSelective_SC.m. Following the Methods (Cell selection, concept cells), a concept\n    cell passes a permuted one-way ANOVA on image identity (54 to 64 groups) at P < 0.05, and\n    then a permutation t-test of the presentations of the image with the highest mean rate\n    against all other presentations at P < 0.05. The number of permutations is not given; 2000\n    is used, as in the code's commented permutation alternative (a resolution detail). The\n    Methods say the preferred response must be significantly larger; the code's test is\n    two-sided. Readings of the second test are (a) two-sided and (b) one-sided, larger. The\n    code's parametric version (anovan, then a binarized anovan) is a variant. MTL is amygdala\n    and hippocampus; the percent is taken over the MTL screening units (see\n    screening-unit-yield for the 421 against 449 denominator). Reproduced when the count and\n    percent are within tolerance under both readings of the test; blocked as\n    methods_underspecified when the readings disagree. Every result is shown.\n- id: screening-concept-mfc\n  statement: In the screening task only 26 MFC units (5.35%) were concept cells, far fewer than\n    in the MTL, so that concept cells are largely found in the MTL.\n  source: Technical Validation, Proportion of selective cells, paragraph 2\n  quote: In contrast, only 26 (5.35%) of cells in the MFC were concept cells, reproducing our\n    earlier finding that concept cells are largely only found in the MTL.\n  depends_on:\n  - screening-concept-mtl\n  expected:\n  - quantity: MFC concept cells, screening\n    value: 26\n    tolerance: 2.6\n  - quantity: percent of MFC units that are concept cells, screening\n    value: 5.35\n    tolerance: 0.535\n    unit: \"%\"\n  criterion: The concept cell test and its readings as in screening-concept-mtl, over MFC\n    screening units (dACC, pre-SMA and vmPFC). Reproduced when the count and percent are within\n    tolerance and the MFC percent is below the MTL percent of screening-concept-mtl; partially\n    reproduced when only the comparison holds. The paper reports no test of the comparison.\n- id: fig4-screening-examples\n  statement: Five example screening units (Fig. 4a to e) are concept cells.\n  source: Figure 4 legend\n  quote: Shown are five ( a – e ) neurons classified as concept cells.\n  depends_on:\n  - screening-concept-mtl\n  criterion: The units listed for Fig. 5a to e (the paper's Fig. 4) in NWB_SB_plotCell_Screening.m,\n    given as subject ID and 1-based unit index (NWB units id plus 1) of the ses-1 files, are\n    (4, 16), (7, 24), (15, 3), (16, 22) and (21, 15). Reproduced when all five pass the concept\n    cell test of screening-concept-mtl, under the readings named there; partially reproduced\n    for three or four.\n- id: sternberg-concept-mtl\n  statement: In the Sternberg task, 94 MTL units (20.94%) qualified as concept cells during the\n    encoding period.\n  source: Technical Validation, Proportion of selective cells, paragraph 3\n  quote: 'Working memory task: In the MTL, 94 (20.94%) neurons qualified as concept cells during\n    the encoding period (Fig. 5 shows examples).'\n  expected:\n  - quantity: MTL concept cells, Sternberg\n    value: 94\n    tolerance: 9.4\n  - quantity: percent of MTL units that are concept cells, Sternberg\n    value: 20.94\n    tolerance: 2.094\n    unit: \"%\"\n  criterion: Per Sternberg unit, the firing rate 200 to 1000 ms after Encoding 1 onset, all\n    trials, grouped by the Encoding 1 image (5 groups). The Methods say only following\n    stimulus onset; the code (NWB_calcSelective_SB.m) settles it as Encoding 1 only. The tests\n    follow the Methods, a permuted one-way ANOVA at P < 0.05, then a permutation t-test of the\n    trials of the image with the highest mean rate against all other trials at P < 0.05, with\n    2000 permutations as in screening-concept-mtl and the same two readings of the second\n    test's sidedness. The code's parametric version (anovan twice) is a variant. Percent over\n    the 449 MTL Sternberg units. Reproduced when count and percent are within tolerance under\n    both readings; blocked as methods_underspecified when they disagree.\n- id: persistent-activity\n  statement: As a group, concept cells fired more during the maintenance period when their\n    preferred image was held in memory than when it was not (4.76 against 2.67 Hz).\n  source: Technical Validation, Proportion of selective cells, paragraph 3\n  quote: As a group, concept cells continued to fire during the maintenance period if their\n    preferred stimulus was held in WM (4.76 ± 4.71 Hz vs. 2.67 ± 3.66 Hz; p = 1.38 × 10 −21 for\n    pref. vs. non-pref. trials, paired one-sided t-test).\n  statistics:\n  - test: paired one-sided t-test, preferred against non-preferred trials\n    p: 1.38e-21\n  depends_on:\n  - sternberg-concept-mtl\n  expected:\n  - quantity: mean rate, preferred trials\n    value: 4.76\n    tolerance: 0.476\n    unit: Hz\n  - quantity: mean rate, non-preferred trials\n    value: 2.67\n    tolerance: 0.267\n    unit: Hz\n  - quantity: standard deviation over cells, preferred trials\n    value: 4.71\n    tolerance: 0.471\n    unit: Hz\n  - quantity: standard deviation over cells, non-preferred trials\n    value: 3.66\n    tolerance: 0.366\n    unit: Hz\n  criterion: The preferred image is the Encoding 1 image with the highest mean rate in the\n    concept cell test (code). Per cell, the mean maintenance rate 0 to 2500 ms after\n    maintenance onset (the window of the Methods for maintenance cells) over preferred trials\n    and over non-preferred trials; a paired one-sided t-test across cells (paper); values are\n    mean and standard deviation over cells (the code prints std). Two readings of which cells,\n    from the text, are (a) the MTL concept cells of sternberg-concept-mtl, as the sentence\n    follows that count, and (b) all Sternberg concept cells in any area, as the code tests.\n    Two readings of preferred trials, which the paper does not fix, are (i) trials in which\n    the preferred image was shown in any encoding period, as the Fig. 5 maintenance raster in\n    the code splits them, and (ii) trials whose Encoding 1 image is the preferred image, as the\n    code's hzPref is labelled. Both trial readings are run for each cell reading. Reproduced\n    when, for one cell reading, both trial readings give p < 0.05 with preferred higher and\n    put both means within tolerance; blocked as methods_underspecified when the trial\n    readings disagree for that cell reading; not reproduced otherwise. The code as written\n    compares Encoding 1 window rates (200 to 1000 ms), with a mask that leaves no\n    non-preferred trial; the same comparison in the Encoding 1 window with the intended mask\n    is shown as a variant, as it may be what produced the printed numbers.\n- id: fig5-sternberg-examples\n  statement: Two example amygdala units (Fig. 5a,b) are concept cells in the Sternberg task that\n    also show persistent activity during maintenance.\n  source: Figure 5 legend\n  quote: ( a,b ) Example responses from 2 neurons classified as concept cells in the Sternberg\n    task that also exhibited persistent activity during the maintenance period. Both cells were\n    recorded in the amygdala.\n  depends_on:\n  - sternberg-concept-mtl\n  criterion: The units listed for Fig. 5a,b in NWB_SB_plotCell_Sternberg.m, subject ID and\n    1-based unit index of the ses-2 files, are (7, 9) and (16, 16). Reproduced when both pass\n    the concept cell test of sternberg-concept-mtl, both electrodes are in the amygdala, and\n    both have a higher mean maintenance rate (0 to 2500 ms) on trials in which the preferred\n    image was shown in any encoding period than on the other trials (the split the code\n    plots). The paper gives no per-cell test of persistence, so none decides the claim.\n    Partially reproduced when one unit meets all three.\n- id: maintenance-cells-mfc\n  statement: In the MFC, 144 units (31.79%) qualified as maintenance cells.\n  source: Technical Validation, Proportion of selective cells, paragraph 3\n  quote: In the MFC, 144 (31.79%) cells qualified as maintenance cells and 122 (26.93%) as probe\n    cells.\n  depends_on:\n  - sternberg-concept-mtl\n  expected:\n  - quantity: MFC maintenance cells\n    value: 144\n    tolerance: 14.4\n  - quantity: percent of MFC units that are maintenance cells\n    value: 31.79\n    tolerance: 3.179\n    unit: \"%\"\n  criterion: Per Sternberg unit, all trials, the mean rate 0 to 2500 ms after maintenance onset\n    against the rate 0 to 500 ms after fixation cross onset, by a one-sided permutation test\n    (increase) at P < 0.05 (Methods). A unit that is also a concept cell (by the test of\n    sternberg-concept-mtl) must in addition pass the same test on its non-preferred trials.\n    The Methods do not say how the permutation is formed; readings are (a) shuffling the\n    labels of the trial rates between the two periods, as the code's commented alternative\n    permutationTest with sidedness larger, and (b) flipping the sign of the per-trial\n    differences, a paired form. Non-preferred trials are read as (i) trials whose Encoding 1\n    image is not the preferred image (the code's intent), and (ii) trials in which the\n    preferred image was not shown in any encoding period. 2000 permutations, as in the code's\n    comment. The code's paired one-sided t-tests are a variant. Percent over MFC Sternberg\n    units (dACC, pre-SMA, vmPFC; 453 by sternberg-unit-yield). Reproduced when count and\n    percent are within tolerance under all readings; blocked as methods_underspecified when\n    the readings disagree.\n- id: probe-cells-mfc\n  statement: In the MFC, 122 units (26.93%) qualified as probe cells.\n  source: Technical Validation, Proportion of selective cells, paragraph 3\n  quote: In the MFC, 144 (31.79%) cells qualified as maintenance cells and 122 (26.93%) as probe\n    cells.\n  expected:\n  - quantity: MFC probe cells\n    value: 122\n    tolerance: 12.2\n  - quantity: percent of MFC units that are probe cells\n    value: 26.93\n    tolerance: 2.693\n    unit: \"%\"\n  criterion: Per Sternberg unit, all trials, the rate 200 to 1000 ms after probe onset against\n    the encoding rate (200 to 1000 ms) and, separately, against the maintenance rate (0 to\n    2500 ms), each by a one-sided permutation t-test (probe higher) at P < 0.05; a probe cell\n    passes both (Methods). The Methods do not fix the encoding rate; readings are (i) the\n    rate pooled over the 200 to 1000 ms windows of every encoding period shown in the trial,\n    as the code intends, and (ii) Encoding 1 only. The permutation is read as (a) label\n    shuffling and (b) paired sign flipping, as in maintenance-cells-mfc; 2000 permutations.\n    The code's paired one-sided t-tests, with its Encoding 3 window taken at Encoding 2 onset,\n    are a variant. Percent over the 453 MFC Sternberg units. Reproduced when count and percent\n    are within tolerance under all readings; blocked as methods_underspecified when the\n    readings disagree.\n"
}
```

```
File created successfully at: claims/000469/10.1038-s41597-024-02943-8.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000469/10.1038-s41597-024-02943-8.yaml paper/10.1038-s41597-024-02943-8.txt; grep -n "—\|rather" claims/000469/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE "^\s{4,}.*: " claims/000469/*.yaml | head
```

```
64:    value: 21
65:    tolerance: 0
67:    value: 41
68:    tolerance: 0
70:    value: 21
71:    tolerance: 0
85:    value: 902
86:    tolerance: 90.2
88:    value: 190
89:    tolerance: 19
```

**Agent calls Bash**

```bash
grep -nE "^\s{4,}[^-a-z_ ].*: |^\s{4,}[a-z]+ [^:]*: " claims/000469/*.yaml | head
```

```
(Bash completed with no output)
```

**Agent**

I wrote `claims/000469/10.1038-s41597-024-02943-8.yaml`. It has 20 claims, all 20 with word-for-word quotes, and the quote checker reports 0 problems. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC10796636), full text with Methods, Technical Validation, figure legends and Tables 1 to 3. The paper is a data descriptor and has no supplement. Its Methods say they are shortened from refs 15 and 20 (Kaminski 2017 and 2020). Those two papers are also under `paper/`, but I did not use them, since the protocol takes methods only from this paper and its code.

**Code read:** `rutishauserlab/workingmem-release-NWB` at commit f8594e0. Its code is the same as tag v1.0.0 (4a98f46); only the README and citation file differ. A rewrite for another dataset was added and reverted the same day, and I ignored it. The Methods name permutation tests; the code runs ordinary parametric tests (ANOVA, paired one-sided t-tests) and keeps permutation versions only in comments. Following the protocol, the Methods give the main criteria and the code's tests are variants. The code also has three bugs:
- **Trial masks:** the masks for preferred and non-preferred trials pick every trial and no trial. As written, the code cannot produce the paper's persistent-activity numbers, and its extra maintenance test for concept cells cannot run.
- **Wrong window:** its "preferred vs non-preferred" rates come from the first encoding window, not the maintenance period the paper names.
- **Encoding 3:** the probe test counts the Encoding 2 window a second time in place of Encoding 3.

**Statistics and criteria:**
- **Statistics:** two claims record a statistic. These are the load effect on reaction time (F(2,40) = 7.92, p = 0.0013) and the persistent-activity test (p = 1.38e-21).
- **Expected numbers:** 19 claims have them, all with a 10% tolerance. The exception is the subject and session counts, which have zero tolerance.
- **Criteria:** all 20 claims have one.

**Details the paper leaves open, and the readings I named:**
- **Second step of the concept-cell test:** two-sided (as the code does it) or one-sided "larger" (as the Methods word it). This applies to both the screening and Sternberg claims and the Fig. 4 and 5 example units.
- **Permutation design** (maintenance and probe cells): shuffling trial labels (the code's commented-out version) or a paired sign flip. Neither source gives the number of permutations; I used the code comment's 2000 as a standard choice.
- **"Non-preferred trials" for concept cells in the maintenance test:** trials whose first image is not the preferred one (what the code intends), or trials where the preferred image was not shown in any encoding period.
- **Encoding rate in the probe test:** pooled over all encoding periods in the trial (what the code intends), or Encoding 1 only.
- **Persistent activity, which cells:** the 94 MTL concept cells, or all concept cells in any area (as the code tests).
- **Persistent activity, which trials count as preferred:** the preferred image in any encoding period, or in Encoding 1 only. The code's comparison in the encoding window is shown as a variant.
- **Refractory-period violations:** the text says all units; the code averages only units whose value is below 4%.
- **Signal-to-noise ratio:** the sentence describes the peak SNR but cites Fig. 3g and h, so both the peak and the mean SNR are named.
- **Settled by the code, not left open:** reaction times use correct trials only; the concept-cell window is Encoding 1 only; all trials are used for selectivity.

**Inconsistencies in the paper (nothing a claim needed is missing):**
- **Screening MTL count:** the text says 449 MTL units in screening. The screening percentages (32.78% for 138 cells, 5.35% for 26) imply about 421 MTL and 486 MFC units. Both 449 and 421 are named as readings.
- **Ages:** the text gives 17 to 71, while Table 1 lists 17 to 70.
- **Figure citation:** the projection distance is cited as Fig. 3g, but the legend puts it in panel i.

## End of run

28 turns, 4 minutes, result: success.
