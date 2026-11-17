# hunt-2018 · author · run 43627464018

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper
```

```
<persisted-output>
Output too large (55.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8aa49093-d98c-4c6e-8505-65fa3d5b2f8b/tool-results/btnkuix9e.txt

Preview (first 2KB):
Sat Nov 14 18:42:46 UTC 2026
# Protocol for an attempt

Version: `pilot-15`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-15`. Record this version in the attempt's provenance.
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
[... 657 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; echo ----; wc -l docs/design.md docs/archives.md; ls entries/fouke-2025 paper; cat claims/hunt-2018.yaml
```

```
<persisted-output>
Output too large (68.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8aa49093-d98c-4c6e-8505-65fa3d5b2f8b/tool-results/b0qg54iqq.txt

Preview (first 2KB):
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://encorescience.org/>
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/hunt-2018.yaml"
}
```

```
1	# Claims for Hunt, Malalasekera, de Berker, Miranda, Farmer, Behrens & Kennerley (2018), Nature
2	# Neuroscience 21, 1471-1481, "Triple dissociation of attention and decision computations across
3	# prefrontal cortex", doi:10.1038/s41593-018-0239-5, on CRCNS data set pfc-7 (doi:10.6080/K0PZ5712).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record (PMC6331040, open access, JATS XML flattened to text, under
8	# paper/), main text, Discussion and Online Methods, and the supplement
9	# (41593_2018_239_MOESM1_ESM.pdf, extracted to text in the same file; legends of Supplementary
10	# Figures 1 to 12, Supplementary Table 1 and the Supplementary Note). The flattened main text has
11	# no main figure legends, and no PDF of the main article was supplied, so the legends of Figures 1
12	# to 8 (their sample sizes, tests and significance marks) were not read. Every claim on a main
13	# figure rests on the Results and Methods sentences that cite it. The extraction drops the minus
14	# sign in some exponents ("p<1*10 7" stands for p < 1e-7); quotes keep the extracted characters.
15	# The CRCNS data descriptor (paper/pfc-7.data-description.txt) was read only to know what the
16	# data set holds; no claim or method comes from it.
17	#
18	# Code. The Code Availability statement says the custom MATLAB analysis scripts are deposited with
19	# the raw data on CRCNS (dataset pfc-7). By the data descriptor they are among the data set's own
20	# files (Fig1_2_S1_behaviour, Fig4_RSA, Fig5_OFC_crosscorrelation, Fig6_ACC_multiplesignals,
[... 867 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper entries/fouke-2025; cat paper/pfc-7.data-description.txt | head -300; grep -n -A60 "## CRCNS" docs/archives.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=pfc-7/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(s,k)
print(re.findall(r'<IsTruncated>(.*?)</IsTruncated>',t))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in entries/fouke-2025/README.md; head -c 3000 entries/fouke-2025/omr.py; cat attempts/fouke-2025-01.yaml | head -150
```

```
schema_version: 1
name: fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
helpers:
- omr.py
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
- id: doi:10.1016/j.cub.2025.04.027
[... 248 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/fouke-2025-01.yaml | grep -n -E "^[a-z_]+:|^- (kind|about)" ; grep -n -B2 -A12 "^findings:" attempts/fouke-2025-01.yaml | head -40; python3 -c "import fsspec,scipy,h5py,numpy,openpyxl;print('ok')"
```

```
Exit code 1
95:findings:
96:- kind: data_missing
101:- kind: metadata_insufficient
105:- kind: code_mismatch
111:- kind: metadata_error
115:- kind: metadata_error
119:- kind: other
126:- kind: metadata_insufficient
130:- kind: other
136:- kind: code_mismatch
142:- kind: code_mismatch
146:- kind: code_mismatch
151:- kind: other
157:- kind: code_mismatch
160:- kind: selection_undocumented
165:verifications:
242-  notes: Needs the imaging, the tail tracking and the registration to the mapzebrain atlas, none
243-    of which is in the dandiset.
244:findings:
[... 17 more lines not kept]
```

**Agent**

Set up a working venv for exploration.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q fsspec aiohttp requests scipy h5py numpy pandas openpyxl statsmodels matplotlib && python -c "import fsspec;print('ok')"; ls tools; sed -n 1,80p tools/entry.py 2>/dev/null | head -5
```

```
ok
ls: cannot access 'tools': No such file or directory
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import fsspec, zipfile, io
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/"
f=fsspec.open(B+"scripts.zip",block_size=2**20).open()
z=zipfile.ZipFile(f)
import os
os.makedirs("scripts",exist_ok=True)
for i in z.infolist():
    print(i.file_size,i.filename)
z.extractall("scripts")
for n in ["filelist.txt","checksums.md5"]:
    print(fsspec.open(B+n).open().read().decode()[:5000])
import pandas as pd
x=pd.read_excel(io.BytesIO(fsspec.open(B+"docs/preprocessed_data_variables.xlsx").open().read()),sheet_name=None,header=None)
for k,v in x.items():
    pd.set_option('display.width',250,'display.max_colwidth',200,'display.max_rows',500)
    print(k); print(v.to_string())
EOF
```

```
<persisted-output>
Output too large (63.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8aa49093-d98c-4c6e-8505-65fa3d5b2f8b/tool-results/b1f937ttr.txt

Preview (first 2KB):
0 scripts/
27034 scripts/InfoGathering_Behaviour.m
8422 scripts/Fig8_single_neuron_coding.m
8917 scripts/InfoGathering_Neurons_Ramp_to_choice.m
5527 scripts/Fig7_single_neurons_cue2and3.m
5018 scripts/Fig1_2_S1_behaviour.m
16990 scripts/Fig6_ACCmultiplesignals_R3_version.m
3390 scripts/FigS4_RSA_split.m
112 scripts/get_basedir.m
15558 scripts/InfoGathering_Neurons_Cue1_regression.m
10525 scripts/Fig5_OFCcrosscorrelation.m
16385 scripts/InfoGathering_Neurons_Cue123_alltrials_attentional_value_final.m
0 scripts/essential_scripts/
2780 scripts/essential_scripts/cross_corr_tstats.m
475 scripts/essential_scripts/normalise.m
683 scripts/essential_scripts/plotmse.m
[... 32 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8aa49093-d98c-4c6e-8505-65fa3d5b2f8b/tool-results/b1f937ttr.txt",
 "offset": 50
}
```

```
50	 behavioural_data/Frank_InfoGathering_All_Data.mat	1100764798 (1.0 GB)
51	 behavioural_data/Miles_InfoGathering_All_Data.mat	1658192071 (1.5 GB)
52	 docs/crcns_pfc-7_data_description.docx	23528 (22.9 KB)
53	 docs/crcns_pfc-7_data_description.pdf	54926 (53.6 KB)
54	 docs/preprocessed_data_variables.xlsx	15843 (15.4 KB)
55	 docs/README.docx	964075 (941.4 KB)
56	 docs/README.pdf	50261 (49.0 KB)
57	 docs/scripts_data_flowchart.pdf	967119 (944.4 KB)
58	 neuronal_data/F002.zip	1535426170 (1.4 GB)
59	 neuronal_data/F003.zip	1155407311 (1.0 GB)
60	 neuronal_data/F004.zip	1964915990 (1.8 GB)
61	 neuronal_data/F008.zip	1235432148 (1.1 GB)
62	 neuronal_data/F009.zip	1117275409 (1.0 GB)
63	 neuronal_data/F010.zip	1945589711 (1.8 GB)
64	 neuronal_data/F012.zip	1637590161 (1.5 GB)
65	 neuronal_data/F013.zip	1503564304 (1.4 GB)
66	 neuronal_data/F015.zip	1708545401 (1.5 GB)
67	 neuronal_data/F016.zip	2017264345 (1.8 GB)
68	 neuronal_data/F017.zip	2300872589 (2.1 GB)
69	 neuronal_data/F018.zip	1248288341 (1.1 GB)
[... 247 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import fsspec, zipfile
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/"
f=fsspec.open(B+"neuronal_data/LTH_processed_data.zip",block_size=2**20).open()
z=zipfile.ZipFile(f)
L=z.infolist()
print(len(L)); 
for i in L[:5]+L[-5:]: print(i.file_size,i.compress_size,i.filename)
import collections
print(sum(i.file_size for i in L)/1e9)
z2=zipfile.ZipFile(fsspec.open(B+"neuronal_data/M005.zip",block_size=2**20).open())
for i in z2.infolist()[:20]: print(i.file_size,i.filename)
print(len(z2.infolist()))
EOF
date -u
```

```
725
0 0 LTH_processed_data/
137168 105972 LTH_processed_data/Unit0231.mat
394794 293124 LTH_processed_data/Unit0540.mat
378507 282627 LTH_processed_data/Unit0133.mat
1139217 1080176 LTH_processed_data/Unit0046.mat
311374 254817 LTH_processed_data/Unit0310.mat
305830 234728 LTH_processed_data/Unit0212.mat
386602 340254 LTH_processed_data/Unit0175.mat
848737 782861 LTH_processed_data/Unit0266.mat
399596 302511 LTH_processed_data/Unit0498.mat
0.417965541
104870117 M005_C18_U1.mat
105095660 M005_C19_U1.mat
105194925 M005_C19_U2.mat
105349400 M005_C1_U1.mat
105298502 M005_C1_U2.mat
104980624 M005_C20_U1.mat
104841246 M005_C21_U1.mat
104768831 M005_C24_U1.mat
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts && cat InfoGathering_Neurons_Cue123_alltrials_attentional_value_final.m
```

```
Exit code 1
cat: InfoGathering_Neurons_Cue123_alltrials_attentional_value_final.m: No such file or directory
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && cat InfoGathering_Neurons_Cue123_alltrials_attentional_value_final.m
```

```
function out = InfoGathering_Neurons_Cue123_alltrials_attentional_value_final(dosave,doproj)

% out = InfoGathering_Neurons_Cue123_alltrials_attentional_value_final(dosave,doproj)
%
% Runs regression of Cue 1,2,3,4 value, belief confirmation, on firing
%   rates timelocked to cue 1, 2, 3 presentation and response 
%
% if dosave == 1 (default 0), stores results in
% neuronal_regression_results/info_gathering_cue123_alltrials_attentional_final.mat
%
% Key output variables include:
%   significant_neuron (nUnits*nContrasts) - whether a unit significantly
%       encodes this contrast of parameter estimates, at p<0.05 corrected for
%       multiple comparisons across time
%   cpd1,2,3,R (nUnits*nRegressors*nTimeBins) - the coefficient of partial
%       determination for 18 different regressors of interest, time-locked 
%       to cue 1, 2, 3, response
%   t_stats1,2,3,R - cell array of units, each nTimeBins*nContrasts - sliding
%       T-statistic for each unit for each contrast of parameter estimates
%       across time, time-locked to cue 1, 2, 3, response
[... 326 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts/essential_scripts && for f in sliding_regression_ols_perm.m ols.m cpd.m sliding_regression_CPD.m calculate_RSA_matrices.m calculate_RSA_matrices_updown.m calculate_t75max.m cross_corr_tstats.m normalise.m chi2.m calculate_atts_seen.m calc_rank.m neuron_matrix.m; do echo "=== $f"; grep -v "^\s*$" $f; done
```

```
=== sliding_regression_ols_perm.m
function [betas,t_stats,min_contrast_thresholds,max_contrast_thresholds,c_first_bin,permute_beta,permute_tstat]=...
    sliding_regression_ols_perm(design_matrix,SpikeMatrix,contrasts,variables,perm_mat)
%
%
%
window_size=variables(1);
slide_width=variables(2);       %how frequently to subsample firing rate in output
epoch_duration=variables(3); 
pre_cue=variables(4);
if nargin<5
    num_perms=variables(5);
else
    num_perms = size(perm_mat,2);
end
totbins2=(epoch_duration/slide_width)-((window_size/slide_width)-1);
BINS=[1:slide_width:(epoch_duration-slide_width+1)];
%% smooth data
for thisbin=1:floor(totbins2)
    smoothed_data(:,thisbin)=mean(SpikeMatrix(:,BINS(thisbin):(BINS(thisbin)+(window_size-1))),2);
[... 504 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && grep -v "^\s*$" Fig4_RSA.m | head -400
```

```
clear all; close all;
[bd] = get_basedir;
addpath(genpath(fullfile(bd)));
%% load in info about units
load('all_units_info.mat');
nUnits = length(all_units);
for i = 1:nUnits
    area(i) = all_units{i}.UnitInfo.area;
    average_firing_rate(i) = all_units{i}.UnitInfo.average_firing_rate;
    isfrank(i) = all_units{i}.UnitInfo.isfrank;
    ismiles(i) = all_units{i}.UnitInfo.ismiles;
end
%% define areas. indices 1 = ACC; 2 = LPFC 3 = OFC
area_index = [1 2 3 5];
color_index = {'r' 'g' 'b' 'c' 'k'};
area_name = {'ACC' 'DLPFC' 'OFC' '' 'Other' ''};
area([87 find(average_firing_rate<1)]) = nan; %bad cells
%area(isfrank) = nan; %to look only at Miles's RSA matrix, see Fig S2
%area(ismiles) = nan; %to look only at Frank's RSA matrix, see Fig S2
ACCcells = find(area==1);
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && grep -v "^\s*$" Fig5_OFCcrosscorrelation.m | grep -v -E "^\s*(set|xlabel|ylabel|title|tidyfig|colormap|axis|line|box|xlim|ylim|caxis|subplot|hold|freezeColors)"
```

```
clear all; close all;
[bd] = get_basedir;
addpath(genpath(bd));
%% load in neuronal analyses
load(fullfile(bd,'neuronal_regression_results','info_gathering_cue123_alltrials_attentional_final.mat'));
% n.b. these results can also be obtained by running
% out = InfoGathering_Neurons_Cue123_alltrials_attentional_value_final(0);
% fields_to_workspace(out);
 %% load in info about units
load('all_units_info.mat');
nUnits = length(all_units);
for i = 1:nUnits
    area(i) = all_units{i}.UnitInfo.area;
    average_firing_rate(i) = all_units{i}.UnitInfo.average_firing_rate;
    isfrank(i) = all_units{i}.UnitInfo.isfrank;
    ismiles(i) = all_units{i}.UnitInfo.ismiles;
end
area([87 653 find(average_firing_rate<1)]) = nan; %bad cells - 653 contains nans in T-stats
%% load in tstats 
for i = 1:length(t_stats1); tt1(:,:,i) = t_stats1{i}; end
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && F='^\s*(set|xlabel|ylabel|title|tidyfig|colormap|axis|line|box|xlim|ylim|caxis|subplot|hold|freezeColors|plot|legend|figure|text|drawnow)'; grep -v "^\s*$" InfoGathering_Neurons_Ramp_to_choice.m | grep -v -E "$F"; echo =======; grep -v "^\s*$" Fig6_ACCmultiplesignals_R3_version.m | grep -v -E "$F"
```

```
function out = InfoGathering_Neurons_Ramp_to_choice(dosave,doproj)
% out = InfoGathering_Neurons_Ramp_to_choice(dosave)
%
% averages neuron responses in different bins of reaction time, and with
% different reaction times
%
% output structure:
%     out.av_RespRT_LR_even (units*timebins*RTbins*2) - response-locked firing rate on
%       even trials, split by left choices (:,:,:,1) and right choices (:,:,:,2)
%     out.av_RespRT_LR_odd  - as above, for odd trials
%     out.av_RespRT_even (units*timebins*RTbins) - as above, but averaged across left/right choices
%     out.av_RespRT_odd - as above, for odd trials
%     out.timebins_ResponseLong - vector of timestamps for response-locked data
%
%     out.av_Cue1RT_LR_even - (units*timebins*RTbins*2) - cue1-locked firing rate on
%       even trials, split by left choices (:,:,:,1) and right choices (:,:,:,2)
%     out.av_Cue1RT_LR_odd - as above, for odd trials
%     out.av_Cue1L_even (units*timebins*RTbins) - as above, but averaged across left/right choices
%     out.av_Cue1L_odd - as above, for odd trials
%     out.timebins_Cue1Long - vector of timestamps for cue-locked data
[... 408 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && F='^\s*(set|xlabel|ylabel|title|tidyfig|colormap|axis|line|box|xlim|ylim|caxis|subplot|hold|freezeColors|plot|legend|figure|text|drawnow|bar|errorbar)'; grep -v "^\s*$" Fig7_single_neurons_cue2and3.m | grep -v -E "$F"; echo =====; grep -v "^\s*$" Fig8_single_neuron_coding.m | grep -v -E "$F"
```

```
clear all; close all;
bd = get_basedir;
addpath(genpath(bd));
%% load in neuronal analyses
load(fullfile(bd,'neuronal_regression_results','info_gathering_cue123_alltrials_attentional_final.mat'));
% n.b. these results can also be obtained by running
% out = InfoGathering_Neurons_Cue1_regression(0);
% fields_to_workspace(out);
 %% load in info about units
load('all_units_info.mat');
nUnits = length(all_units);
for i = 1:nUnits
    area(i) = all_units{i}.UnitInfo.area;
    average_firing_rate(i) = all_units{i}.UnitInfo.average_firing_rate;
    isfrank(i) = all_units{i}.UnitInfo.isfrank;
    ismiles(i) = all_units{i}.UnitInfo.ismiles;
end
area([87 653 find(average_firing_rate<1)]) = nan; %bad cells - 653 contains nans in T-stats
%% load in tstats 
for i = 1:length(t_stats1); tt1(:,:,i) = t_stats1{i}; end
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && grep -v "^\s*$" InfoGathering_Neurons_Cue1_regression.m | sed -n 1,400p | grep -v -E "^\s*%\s*$"
```

```
function out = InfoGathering_Neurons_Cue1_regression(dosave)
% out = InfoGathering_Neruons_Cue1_regression(dosave)
% Runs regression of Attended Value, Left/Right Value, Prob/Mag. Value,
%   Top/Bottom Value on firing rates timelocked to Cue 1 presentation
% if dosave == 1 (default 0), stores results in
% neuronal_regression_results/info_gathering_cue1_both.mat
% Key output variables include:
%   significant_neuron (nUnits*nContrasts) - whether a unit significantly
%       encodes this contrast of parameter estimates, at p<0.05 corrected for
%       multiple comparisons across time
%   varCPD (nUnits*nRegressors*nTimeBins) - the coefficient of partial
%       determination for 8 different regressors of interest
%   t_stats1 - cell array of units, each nTimeBins*nContrasts - sliding
%       T-statistic for each unit for each contrast of parameter estimates
%       across time
% see comments inside this function for meaning of each of the contrasts of
%   parameter estimates (lines 186 onwards) and CPD variables (lines 296
%   onwards)
%%
% save results after running regression?
[... 266 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && grep -v "^\s*$" Fig1_2_S1_behaviour.m | grep -v -E '^\s*(set|xlabel|ylabel|title|tidyfig|colormap|axis|line|box|xlim|ylim|caxis|subplot|hold|freezeColors|plot|legend|figure|text|drawnow|bar|errorbar)'; echo ====; grep -v "^\s*$" InfoGathering_Behaviour.m | head -250
```

```
clear all; close all;
[bd] = get_basedir;
%% load in behavioural data
addpath(genpath(fullfile(bd)));
load('Miles InfoGathering All Data');MCB=zInfoGatheringInfo;
load('Frank InfoGathering All Data');FCB=zInfoGatheringInfo;
clear zInfoGatheringInfo
%% process data
outM = InfoGathering_Behaviour(MCB);
outF = InfoGathering_Behaviour(FCB);
%% make figure 1
%probability of choosing left/right on attribute trials
diffmat = repmat(1:5,5,1)'-repmat(1:5,5,1);
dd = -4:0.01:4; b = outM.attchoice_b; l(1) = plot(dd,1./(1+exp(-(b(1)+dd.*b(2)))),'r','LineWidth',2);
dd = -4:0.01:4; b = outF.attchoice_b; l(2) = plot(dd,1./(1+exp(-(b(1)+dd.*b(2)))),'b','LineWidth',2);
ll = legend(l,{'Subject M','Subject F'},'Location','SouthEast');
t = title('Attribute trials');
%probability of choosing 1/2 on option trials
summat = repmat(-2:2,5,1)'+repmat(-2:2,5,1);
dd = -4:0.01:4; b = outM.optchoice_b; l(1) = plot(dd,1./(1+exp(-(b(1)+dd.*b(2)))),'r','LineWidth',2);
[... 283 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && grep -v "^\s*$" InfoGathering_Behaviour.m | sed -n 250,600p
```

```
if Lreg(t,3)>Rreg(t,3)
                third_sideL(t)=1;
            else
                third_sideL(t)=0;
            end
            if position_code{t}(2)==91||position_code{t}(2)==92
                if position_code{t}(3)==92||position_code{t}(3)==91
                    vert(t)=1;
                else
                    vert(t)=0;
                end
            elseif position_code{t}(2)==93||position_code{t}(2)==94
                if position_code{t}(3)==94||position_code{t}(3)==93
                    vert(t)=1;
                else
                    vert(t)=0;
                end
            end
        else
            vert(t)=NaN;
[... 257 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import fsspec
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/"
f=fsspec.open(B+"behavioural_data/Frank_InfoGathering_All_Data.mat",block_size=2**20).open()
print(f.read(200))
EOF
```

```
b'MATLAB 7.3 MAT-file, Platform: PCWIN64, Created on: Fri Feb 27 10:20:03 2015 HDF5 schema 1.00 .                     \x00\x00\x00\x00\x00\x00\x00\x00\x00\x02IM\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && timeout 600 python - <<'EOF'
import fsspec,h5py,time
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/"
t=time.time()
f=fsspec.open(B+"behavioural_data/Frank_InfoGathering_All_Data.mat",block_size=2**18).open()
h=h5py.File(f,'r')
print(list(h.keys()))
z=h['zInfoGatheringInfo']; print(z.shape,z.dtype)
s=h[z[0,0] if z.shape[0]==1 else z[0,0]]
print(type(s), list(s.keys()) if hasattr(s,'keys') else s)
for k in s.keys():
    o=s[k]; print(k, o.shape if hasattr(o,'shape') else list(o.keys()), getattr(o,'dtype',None))
print(time.time()-t)
EOF
```

```
['#refs#', 'BhvInfo', 'files', 'zInfoGatheringInfo']
(25, 1) object
<class 'h5py._hl.group.Group'> ['AnalogData', 'CodeNumbers', 'CodeTimes', 'ConditionNumber', 'NumCodes', 'TrialError', 'TrialNumber', 'Uservars']
AnalogData (450, 1) object
CodeNumbers (450, 1) object
CodeTimes (450, 1) object
ConditionNumber (450, 1) float64
NumCodes (450, 1) float64
TrialError (450, 1) float64
TrialNumber (450, 1) float64
Uservars (450, 1) object
1.2979583740234375
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && timeout 900 python - <<'EOF'
import fsspec,h5py,time,numpy as np
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/"
t=time.time()
f=fsspec.open(B+"behavioural_data/Frank_InfoGathering_All_Data.mat",block_size=2**18,cache_type='readahead').open()
h=h5py.File(f,'r')
z=h['zInfoGatheringInfo']
s=h[z[0,0]]
te=s['TrialError'][:].ravel(); cn=s['ConditionNumber'][:].ravel()
print(np.unique(te,return_counts=True), np.unique(cn,return_counts=True))
u=h[s['Uservars'][0,0]]
print(type(u), u.shape if hasattr(u,'shape') else list(u.keys()))
def show(o,ind=''):
    if isinstance(o,h5py.Group):
        for k in o.keys(): print(ind,k); show(o[k],ind+'  ')
    else:
        print(ind,o.shape,o.dtype, o[()] if o.size<20 and o.dtype!=object else '')
        if o.dtype==object:
            show(h[o[0,0]],ind+'  ')
show(u)
cnum=h[s['CodeNumbers'][0,0]]; print('codes',cnum.shape, cnum[()].ravel()[:40])
t1=time.time()
for i in range(50):
    u=h[s['Uservars'][i,0]]
    c=h[s['CodeNumbers'][i,0]][()]; ct=h[s['CodeTimes'][i,0]][()]
print('50 trials',time.time()-t1, 'total',time.time()-t)
EOF
```

```
(array([0., 6.]), array([371,  79])) (array([3., 4.]), array([221, 229]))
<class 'h5py._hl.dataset.Dataset'> (1, 1)
 (1, 1) object 
   AcqTime
     (2,) uint64 [0 0]
   ChoiceTime
     (1, 1) float64 [[nan]]
   ChosenTarget
     (1, 1) float64 [[2.]]
   EVTracker
     (1, 4) float64 [[0.165 0.105 0.    0.   ]]
   LocationTracker
     (1, 4) float64 [[1. 1. 0. 0.]]
   PayoffAmounts
     (1, 4) float64 [[1430.  910.    0.    0.]]
   PayoffTracker
     (1, 4) float64 [[0.55 0.35 0.   0.  ]]
   ProbTop
     (1, 1) float64 [[1.]]
   ProbabilityTracker
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && timeout 900 python - <<'EOF'
import fsspec,h5py,time,numpy as np
from concurrent.futures import ThreadPoolExecutor
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/"
def opn():
    f=fsspec.open(B+"behavioural_data/Frank_InfoGathering_All_Data.mat",block_size=2**16,cache_type='readahead').open()
    return h5py.File(f,'r')
h=opn()
s=h[h['zInfoGatheringInfo'][0,0]]
a=h[s['AnalogData'][0,0]]
print(a.shape,a.dtype)
a0=h[a[0,0]]; print(list(a0.keys()))
for k in a0.keys(): 
    o=a0[k]; print(k, getattr(o,'shape',None), getattr(o,'dtype',None), getattr(o,'chunks',None), getattr(o,'compression',None))
def work(rng):
    h=opn(); s=h[h['zInfoGatheringInfo'][0,0]]
    out=[]
    for i in rng:
        u=h[h[s['Uservars'][i,0]][0,0]]
        d={k:u[k][()] for k in ['ChosenTarget','PayoffTracker','ProbabilityTracker','ProbTop']}
        d['c']=h[s['CodeNumbers'][i,0]][()].ravel(); d['t']=h[s['CodeTimes'][i,0]][()].ravel()
        a=h[h[s['AnalogData'][i,0]][0,0]]
        d['j']=a['Joystick'][()]
        out.append(d)
    return out
t=time.time()
with ThreadPoolExecutor(8) as ex:
    res=list(ex.map(work,[range(k,80,8) for k in range(8)]))
print('80 trials 8 threads',time.time()-t)
d=res[0][0]; print(d['j'].shape, d['c'][:30], d['t'][:30])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
AttributeError: 'Group' object has no attribute 'shape'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && timeout 900 python - <<'EOF'
import fsspec,h5py,time,numpy as np
from concurrent.futures import ThreadPoolExecutor
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/"
def opn():
    f=fsspec.open(B+"behavioural_data/Frank_InfoGathering_All_Data.mat",block_size=2**16,cache_type='readahead').open()
    return h5py.File(f,'r')
h=opn()
s=h[h['zInfoGatheringInfo'][0,0]]
a=h[s['AnalogData'][0,0]]
print(list(a.keys()))
for k in a.keys(): 
    o=a[k]; print(k, getattr(o,'shape',None), getattr(o,'dtype',None))
def work(rng):
    h=opn(); s=h[h['zInfoGatheringInfo'][0,0]]
    out=[]
    for i in rng:
        u=h[h[s['Uservars'][i,0]][0,0]]
        d={k:u[k][()] for k in ['ChosenTarget','PayoffTracker','ProbabilityTracker','ProbTop']}
        d['c']=h[s['CodeNumbers'][i,0]][()].ravel(); d['t']=h[s['CodeTimes'][i,0]][()].ravel()
        a=h[s['AnalogData'][i,0]]
        d['j']=a['Joystick'][()]
        out.append(d)
    return out
t=time.time()
with ThreadPoolExecutor(8) as ex:
    res=list(ex.map(work,[range(k,80,8) for k in range(8)]))
print('80 trials 8 threads',time.time()-t)
d=res[0][0]; print(d['j'].shape, d['c'][:30], d['t'][:30])
EOF
```

```
['EyeSignal', 'General', 'Joystick', 'PhotoDiode']
EyeSignal (2, 8064) float64
General None None
Joystick (2, 8064) float64
PhotoDiode (2,) uint64
80 trials 8 threads 49.93226408958435
(2, 8064) [ 9.  9.  9. 16. 10. 11. 12. 89. 93. 90. 91. 90. 62. 92. 90. 94. 90. 72.
 73.  1.  2.  3. 18. 18. 18.] [ 113.  114.  114.  127.  160.  331.  833.  843. 1076. 2274. 2757. 3073.
 3090. 3273. 3622. 3789. 3955. 3972. 4988. 5004. 5936. 8090. 8099. 8100.
 8101.]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && timeout 900 python - <<'EOF'
import fsspec,h5py,time,numpy as np,io,resource
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/"
t=time.time()
with fsspec.open(B+"behavioural_data/Frank_InfoGathering_All_Data.mat",block_size=2**24).open() as f:
    b=f.read()
print(len(b)/1e6,'MB',time.time()-t)
h=h5py.File(io.BytesIO(b),'r')
t=time.time()
z=h['zInfoGatheringInfo']; n=0
for k in range(z.shape[0]):
    s=h[z[k,0]]
    for i in range(s['Uservars'].shape[0]):
        u=h[h[s['Uservars'][i,0]][0,0]]
        d={kk:u[kk][()] for kk in ['ChosenTarget','PayoffTracker','ProbabilityTracker','ProbTop']}
        c=h[s['CodeNumbers'][i,0]][()]; ct=h[s['CodeTimes'][i,0]][()]
        j=h[s['AnalogData'][i,0]]['Joystick'][()]
        n+=1
print(n,time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
print(h['BhvInfo'], list(h['BhvInfo'].keys())[:20] if hasattr(h['BhvInfo'],'keys') else '', h['files'])
EOF
```

```
1100.764798 MB 53.401050329208374
9863 23.803316831588745 2.557524 GB
<HDF5 group "/BhvInfo" (12 members)> ['AbsoluteTrialStartTime', 'AnalogData', 'BlockIndex', 'BlockNumber', 'CodeNumbers', 'CodeTimes', 'ConditionNumber', 'NumCodes', 'ReactionTime', 'TrialError', 'TrialNumber', 'Uservars'] <HDF5 group "/files" (5 members)>
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && timeout 900 python - <<'EOF'
import fsspec,h5py,time,numpy as np,io,zipfile,scipy.io as sio
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/"
a=sio.loadmat(io.BytesIO(fsspec.open(B+"other_data/all_units_info.mat").open().read()),squeeze_me=True,struct_as_record=False)
print([k for k in a if not k.startswith('__')])
au=a['all_units']; print(len(au)); u=au[0]; print(u._fieldnames); print(u.UnitInfo._fieldnames, vars(u.UnitInfo))
for nm in ['frank_area','miles_area']:
    m=sio.loadmat(io.BytesIO(fsspec.open(B+f"other_data/{nm}.mat").open().read()),squeeze_me=True)
    for k,v in m.items():
        if not k.startswith('__'): print(nm,k,getattr(v,'shape',v), v[:3] if hasattr(v,'__len__') else v)
print(fsspec.open(B+"other_data/unit_count.m").open().read().decode())
z=zipfile.ZipFile(fsspec.open(B+"neuronal_data/LTH_processed_data.zip",block_size=2**20).open())
b=z.read('LTH_processed_data/Unit0001.mat'); print(b[:120])
EOF
```

```
['all_units']
724
['UnitInfo']
['area_name', 'subject', 'session_number', 'channel_number', 'average_firing_rate', 'area', 'isfrank', 'ismiles'] {'_fieldnames': ['area_name', 'subject', 'session_number', 'channel_number', 'average_firing_rate', 'area', 'isfrank', 'ismiles'], 'area_name': 'ACC', 'subject': 'f', 'session_number': 2, 'channel_number': 1, 'average_firing_rate': 8.211532853418149, 'area': 1, 'isfrank': 1, 'ismiles': 0}
frank_area area_index (524, 12) [[ 1.          1.          1.          2.         31.5         5.
  35.5         1.5        11.83333333  0.5        19.5         0.        ]
 [ 1.          2.          1.          2.         31.5         6.
  35.5         1.5        11.83333333  0.5        19.5         0.        ]
 [ 1.         17.          1.          1.         34.          5.
  33.75        0.25       11.25        0.08333333 19.5         0.        ]]
miles_area miles_area (641, 12) [[ 1.          1.          6.          2.         30.5        -2.
  20.          3.          6.66666667  1.         17.          0.        ]
 [ 1.          2.          6.          2.         31.5        -2.
  20.          0.          6.66666667  0.         17.          0.        ]
 [ 1.          3.          6.          2.         32.5        -2.
  20.          0.          6.66666667  0.         17.          0.        ]]
% script to return table of session ID, number of units recorded from
% ACC/OFC/DLPFC

% fsess and msess are recording sessions for Frank and Miles respectively
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && grep -n -i -E "men|sdev|average_firing|SpikeTable|inf_responded|realign|Cue1_ON\s*\(|Response_time\s*=|Response_time\(" InfoGathering_Preprocess_Neurons.m | head -60
```

```
35:%% main loop over each unit from information gathering experiment
54:    inf_responded_trials=inf_trials(trial_error(inf_trials)==0|trial_error(inf_trials)==6);
55:    inf_cond=BhvInfo.ConditionNumber(inf_responded_trials);
56:    condition=BhvInfo.ConditionNumber(inf_responded_trials); %3 = option trial; 4 = attribute trial
79:    sdev=nanstd(smoothed_std_neurons);
80:    men=nanmean(smoothed_std_neurons);
84:    nInfoGatheringTrials = length(inf_responded_trials); %number of InfoGathering Trials
87:        ct=inf_responded_trials(tr); %ct = current trial, note that this
120:        %time of first sizeable joystick movement, Move_time (should precede 'Response'):
141:        % the joystick movement
258:        Cue1_ON(tr)=picture_codes{tr}(1,2);
287:        Realign_plex_code(tr)=Plex_codes{tr}(1,2); %time of first code, to which timings may be realigned - normally 0
288:        Plex_codes{tr}(:,2)=round((Plex_codes{tr}(:,2)-Realign_plex_code(tr))); %realign timings
291:        Response_time(tr)=Plex_codes{tr}(find(Plex_codes{tr}(:,1)==72),2);
298:        SpikeTable{tr}=BhvInfo.SpikeCodes{ct}; %timing of action potentials in the current trial
307:        FSpikes(tr)=(sum(SpikeTable{tr}>FixationEND(tr)-299&SpikeTable{tr}<=FixationEND(tr))/300)*1000;
308:        C1Spikes(tr)=(sum(SpikeTable{tr}>Cue1_ON(tr)&SpikeTable{tr}<=Cue1_ON(tr)+299)/300)*1000;
309:        C2Spikes(tr)=(sum(SpikeTable{tr}>Cue2_ON(tr)&SpikeTable{tr}<=Cue2_ON(tr)+299)/300)*1000;
311:            C3Spikes(tr)=(sum(SpikeTable{tr}>Cue3_ON(tr)&SpikeTable{tr}<=Cue3_ON(tr)+299)/300)*1000;
316:            C4Spikes(tr)=(sum(SpikeTable{tr}>Cue4_ON(tr)&SpikeTable{tr}<=Cue4_ON(tr)+299)/300)*1000;
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && sed -n 30,90p InfoGathering_Preprocess_Neurons.m; sed -n 250,300p InfoGathering_Preprocess_Neurons.m
```

```
% column 12= which session of a given stimulus set (0 = learning day
%            when stimulus values were learnt, not information sampling session;
%            1 = first day with this stimulus set in information sampling task;
%            2= second day; 3 = third day);

%% main loop over each unit from information gathering experiment

new_correct=100; %this is the minimum length of time for a picture to be considered 'viewed', used below

for u=1:length(filenames) %u = 'unit'
    tic
    %% load in the data
    load(filenames(u).name);
    u
    
    disp('Epoch/pre-process');
    
    %% isolate information gathering trials where error code doesn't indicate
    %  timeout etc., and therefore where subject completed the trial
    inf_trials=find(BhvInfo.ConditionNumber==3|BhvInfo.ConditionNumber==4);
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && timeout 900 python - <<'EOF'
import fsspec,numpy as np,io,zipfile,scipy.io as sio,time
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/"
z=zipfile.ZipFile(fsspec.open(B+"neuronal_data/LTH_processed_data.zip",block_size=2**20).open())
b=z.read('LTH_processed_data/Unit0001.mat')
for w in sio.whosmat(io.BytesIO(b)): print(w)
t=time.time()
m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
print('load',time.time()-t)
bi=m['BhvInfo']; print(bi._fieldnames)
for f in bi._fieldnames:
    v=getattr(bi,f); print(f, type(v), getattr(v,'shape',None))
for k in ['men','sdev','sb','snum','chnum','brain_region','str_area','new_correct','nInfoGatheringTrials','pre_cue','post_cue']:
    print(k,m[k])
print(m['Cue1_MatrixRaw'].shape, np.unique(m['Cue1_MatrixRaw']), m['Cue1_MatrixRaw'].dtype)
print(m['reg_mat'][:5], m['condition'][:5], m['num_pics_viewed'][:10], m['pictures_views'][:10], m['npv'][:10])
print(m['SpikeTable'][0][:10], m['Prob_top'][:5])
EOF
```

```
('BhvInfo', (1, 1), 'struct')
('C1Spikes', (1, 450), 'double')
('C2Spikes', (1, 450), 'double')
('C3Spikes', (1, 450), 'double')
('C4Spikes', (1, 450), 'double')
('Chosen_target', (450, 1), 'double')
('Codes', (1, 450), 'cell')
('Cue1_Matrix', (450, 800), 'double')
('Cue1_MatrixRaw', (450, 800), 'double')
('Cue1_ON', (1, 450), 'double')
('Cue2_Matrix', (450, 800), 'double')
('Cue2_MatrixRaw', (450, 800), 'double')
('Cue2_ON', (1, 450), 'double')
('Cue3_Matrix', (450, 800), 'double')
('Cue3_MatrixRaw', (450, 800), 'double')
('Cue3_ON', (1, 450), 'double')
('Cue4_ON', (1, 450), 'double')
('FSpikes', (1, 450), 'double')
('First_pos', (450, 1), 'double')
('First_side', (1, 450), 'double')
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && cat essential_scripts/smooth_wa.m | grep -v "^\s*%" | head -40; cd  grep -n -i -E "odd|five separate|normalis|z-scor|random split|baseline|1000 permutations|10,000|chance|binomial" paper/10.1038-s41593-018-0239-5.txt | cut -c1-400
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 199,215p paper/10.1038-s41593-018-0239-5.txt; grep -n -i -E "Supplementary Table 1|Table S1" paper/10.1038-s41593-018-0239-5.txt | head; grep -n "^\s*##\|^[A-Z][A-Za-z ]*$" paper/10.1038-s41593-018-0239-5.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/scripts && sed -n 45,90p essential_scripts/smooth_wa.m; sed -n 600,625p paper/10.1038-s41593-018-0239-5.txt; sed -n 375,420p paper/10.1038-s41593-018-0239-5.txt | tr '\n' ' '
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
mkdir -p entries/hunt-2018; ls tools/ 2>/dev/null; ls; python3 --version; sed -n 1,60p tools/entry.py 2>/dev/null | head -0; ls tools 2>/dev/null || find . -name entry.py -path "*tools*" | head
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
contributors.py
conversion_issue.py
datasets.py
entry.py
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cat papers/datasets/hunt-2018.yaml; ls questions | head; ls schemas; f=$(ls questions/*.yaml | head -1); head -30 $f
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1038/s41593-018-0239-5
title: Triple dissociation of attention and decision computations across prefrontal cortex
datasets:
- archive: crcns
  id: pfc-7
  relation: primary
README.md
asari-2009.yaml
ashworth-2025.yaml
athalye-2023.yaml
bech-2026.yaml
bellvila-2026.yaml
bennett-2024.yaml
berg-2020.yaml
boran-2022.yaml
bouchard-2013.yaml
attempt.schema.json
claims.schema.json
[... 23 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/hunt-2018/pfc7.py",
 "content": "\"\"\"Loading and measures for CRCNS pfc-7 (Hunt, Malalasekera et al. 2018, Nature Neuroscience).\n\nHunt, Malalasekera, de Berker, Miranda, Farmer, Behrens & Kennerley (2018), \"Triple dissociation\nof attention and decision computations across prefrontal cortex\", doi:10.1038/s41593-018-0239-5.\nThe data set (doi:10.6080/K0PZ5712) is read anonymously from the public S3 bucket crcnsarchive,\nunder pfc-7/live/. Each file is read into memory and parsed there; nothing is written to disk.\n\nWhat is read:\n\n- behavioural_data/<Miles|Frank>_InfoGathering_All_Data.mat (MATLAB 7.3): per session, the\n  completed option and attribute trials, with the cue values, the choice, the event codes and the\n  joystick trace. `load_behaviour` reads one file at a time (about 1.1 and 1.7 GB in memory).\n- neuronal_data/LTH_processed_data.zip: one MATLAB 5 file per unit (Unit0001 to Unit0724),\n  the authors' preprocessed data (rasters at 1 ms locked to cues 1 to 3 and the response, the\n  trial variables and the spike times per trial). `load_units` reduces each unit as it loads.\n- other_data/all_units_info.mat: area, subject, session, channel and mean rate per unit.\n\nWhere the parameters come from. The paper's own MATLAB scripts are files of the data set\n(scripts.zip); the Code Availability statement points to them. Where the claims file leaves a\ndetail open and those scripts settle it, the script is named next to the parameter.\n\n- GLM (`glm_design`, `sliding_ols`): EVs 1 to 18 as InfoGathering_Neurons_Cue123_alltrials_\n  attentional_value_final.m builds them, with its contrasts 19 to 35; no further constant (EVs 11\n  and 12 sum to it); 200 ms windows stepped by 10 ms on rasters from -199 to 600 ms, giving 61\n  bins centred from -100 to 500 ms (response-locked rasters run from -600 to 199 ms, so the\n  response bins are centred from -500 to 100 ms); trials with fewer than 3 cues viewed dropped;\n  odd and even trials numbered before that drop. Claims file, shared GLM method; Methods, GLM.\n- CPD (`cpd`): (SSE without the regressor - SSE full) / SSE without it (cpd.m; Methods, RSA\n  template-based regression).\n- RSA (`rsa_inputs`, `rsa_matrix`, `rsa_design`): calculate_RSA_matrices.m and Fig4_RSA.m;\n  conditions LP1-5, LM1-5, RP1-5, RM1-5 by cue 1's side, attribute and rank; mean spike count in\n  100 < t < 500 ms; each unit z-scored over the 20 conditions; Pearson correlation between\n  conditions. Sliding RSA uses a 200 ms boxcar at every 1 ms (conv2 'same').\n- Unit exclusion: mean rate below 1 Hz (Methods, Neuronal Recordings), and unit 87, which every\n  figure script of the paper drops as a \"bad cell\" (Fig4_RSA.m: `area([87 find(average_firing_\n  rate<1)]) = nan`). Fig5 and Fig7 scripts also drop unit 653 (\"contains nans in T-stats\").\n- Fig 6 rasters (`acc_long_rasters`): InfoGathering_Neurons_Ramp_to_choice.m; spike times\n  from SpikeTable, cue 1 locked -500 to 3000 ms and response locked -3000 to 500 ms, z-scored by\n  the unit's session mean and SD (`men`, `sdev`), 200 ms boxcar ('valid'), every 10 ms.\n- Joystick movement time (`move_time`): InfoGathering_Behaviour.m, a 5-sample boxcar of the\n  first joystick channel from fixation end to response, threshold 1 when the fixation-period\n  mean is below 0.8 in absolute value, otherwise 2.9.\n- Random seeds are standard choices that cannot change a result beyond permutation noise; each\n  analysis passes its own generator.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport zipfile\n\nimport fsspec\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport scipy.io as sio\nfrom scipy import ndimage, stats\n\nBASE = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/\"\nAREAS = {1: \"ACC\", 2: \"DLPFC\", 3: \"OFC\"}\nBAD_UNITS = (87,)          # Fig4_RSA.m, Fig6, Fig8 scripts\nNAN_TSTAT_UNITS = (653,)   # Fig5_OFCcrosscorrelation.m, Fig7_single_neurons_cue2and3.m\nTIMEBINS = np.arange(-100, 501, 10)       # centres of the 61 GLM bins, cue locked\nRESP_TIMEBINS = np.arange(-500, 101, 10)  # the same bins, response locked\nCUE1_LONG = np.arange(-400, 2901, 10)     # Ramp_to_choice.m timebins_Cue1Long\nRESP_LONG = np.arange(-2900, 401, 10)     # Ramp_to_choice.m timebins_ResponseLong\n\n\ndef read_bytes(path: str) -> bytes:\n    with fsspec.open(BASE + path, block_size=2**24).open() as f:\n        return f.read()\n\n\ndef checksums() -> dict:\n    \"\"\"MD5 sums of the data set's files, from its checksums.md5.\"\"\"\n    out = {}\n    for line in read_bytes(\"checksums.md5\").decode().splitlines():\n        if line.strip() and not line.startswith(\"#\"):\n            md5, name = line.split(None, 1)\n            out[name.strip()] = md5\n    return out\n\n\ndef listing() -> pd.DataFrame:\n    import re\n    import urllib.request\n    url = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=pfc-7/\"\n    txt = urllib.request.urlopen(url).read().decode()\n    rows = re.findall(r\"<Key>(.*?)</Key>.*?<Size>(\\d+)</Size>\", txt)\n    return pd.DataFrame(rows, columns=[\"key\", \"size\"]).astype({\"size\": int})\n\n\n# --------------------------------------------------------------------------- units table\n\ndef units_info() -> pd.DataFrame:\n    m = sio.loadmat(io.BytesIO(read_bytes(\"other_data/all_units_info.mat\")), squeeze_me=True,\n                    struct_as_record=False)\n    rows = []\n    for i, u in enumerate(m[\"all_units\"], start=1):\n        ui = u.UnitInfo\n        rows.append(dict(unit=i, area=int(ui.area), area_name=str(ui.area_name),\n                         subject=str(ui.subject).upper(), session=int(ui.session_number),\n                         channel=int(ui.channel_number), info_rate=float(ui.average_firing_rate)))\n    return pd.DataFrame(rows).set_index(\"unit\")\n\n\n# --------------------------------------------------------------------------- behaviour\n\ndef smooth_wa_boxcar(x: np.ndarray, window: int) -> np.ndarray:\n    \"\"\"smooth_wa.m with a boxcar kernel (window made even, ends padded with local means).\"\"\"\n    if window % 2:\n        window += 1\n    half = window // 2\n    n = len(x)\n    padded = np.concatenate([np.full(half, x[:half].mean()), x,\n                             np.full(half, x[n - half - 1:].mean())])\n    out = np.convolve(padded, np.ones(window) / window)\n    return out[window:n + window]\n\n\ndef move_time(joy: np.ndarray, fix_end: int, response: int) -> float:\n    \"\"\"Time of the first sizeable joystick movement, as InfoGathering_Behaviour.m computes it.\"\"\"\n    fix_joy = joy[fix_end - 101:fix_end].mean()\n    jt = smooth_wa_boxcar(joy[fix_end - 1:response], 5)\n    thr = 1.0 if abs(fix_joy) < 0.8 else 2.9\n    idx = np.flatnonzero(np.abs(jt) > thr)\n    return float(idx[0] + 1 + fix_end) if len(idx) else np.nan\n\n\ndef _rank(v):\n    \"\"\"calc_rank.m: 0.1/0.15 -> 1 ... 0.9/0.95 -> 5.\"\"\"\n    return int(np.floor(round(v, 2) * 5 + 1e-9)) + 1 if v > 0 else 0\n\n\ndef load_behaviour(subject: str) -> pd.DataFrame:\n    \"\"\"One row per trial of behavioural_data/<Miles|Frank>_InfoGathering_All_Data.mat.\"\"\"\n    name = {\"M\": \"Miles\", \"F\": \"Frank\"}[subject]\n    raw = read_bytes(f\"behavioural_data/{name}_InfoGathering_All_Data.mat\")\n    h = h5py.File(io.BytesIO(raw), \"r\")\n    z = h[\"zInfoGatheringInfo\"]\n    rows = []\n    for s in range(z.shape[0]):\n        g = h[z[s, 0]]\n        cond = g[\"ConditionNumber\"][()].ravel()\n        terr = g[\"TrialError\"][()].ravel()\n        tnum = g[\"TrialNumber\"][()].ravel()\n        for i in range(len(cond)):\n            u = h[h[g[\"Uservars\"][i, 0]][0, 0]]\n            codes = h[g[\"CodeNumbers\"][i, 0]][()].ravel()\n            times = h[g[\"CodeTimes\"][i, 0]][()].ravel()\n            joy = h[g[\"AnalogData\"][i, 0]][\"Joystick\"][0, :]\n            pay = u[\"PayoffTracker\"][()].ravel()\n            prob = u[\"ProbabilityTracker\"][()].ravel()\n            fix_end = int(times[codes == 12][0])\n            resp = int(times[codes == 72][0])\n            pos = codes[(codes > 90) & (codes < 95)].astype(int)\n            pos_t = times[(codes > 90) & (codes < 95)]\n            rows.append(dict(\n                subject=subject, session=s + 1, trial=int(tnum[i]), condition=int(cond[i]),\n                trial_error=int(terr[i]), LP=prob[0], RP=prob[1], LM=pay[0], RM=pay[1],\n                chosen=int(u[\"ChosenTarget\"][()].ravel()[0]), prob_top=int(u[\"ProbTop\"][()].ravel()[0]),\n                fix_end=fix_end, response=resp, cue1_on=float(pos_t[0]) if len(pos_t) else np.nan,\n                positions=tuple(pos), pos_times=tuple(pos_t),\n                move_time=move_time(joy, fix_end, resp)))\n    h.close()\n    del raw\n    return add_behaviour_measures(pd.DataFrame(rows))\n\n\ndef add_behaviour_measures(b: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"Per-trial measures of InfoGathering_Behaviour.m.\"\"\"\n    b = b.copy()\n    b[\"left_choice\"] = (b.chosen == 1).astype(int)\n    b[\"LEV\"] = b.LP * b.LM\n    b[\"REV\"] = b.RP * b.RM\n    b[\"npv\"] = b.positions.map(len)\n    b[\"new_last_time\"] = b.move_time - b.pos_times.map(lambda t: t[-1])\n    # joystick moved before the last picture was fixated (num_pics_viewedprezero), or within\n    # 250 ms of fixating it (num_pics_viewed250)\n    b[\"npv_prezero\"] = b.npv - ((b.new_last_time < 0) & (b.npv > 2))\n    b[\"npv250\"] = b.npv - ((b.new_last_time <= 250) & (b.npv > 2))\n    # value at each position: 91 top left, 92 bottom left, 93 top right, 94 bottom right\n    def vals(r):\n        top_l, top_r = (r.LP, r.RP) if r.prob_top == 1 else (r.LM, r.RM)\n        bot_l, bot_r = (r.LM, r.RM) if r.prob_top == 1 else (r.LP, r.RP)\n        return {91: top_l, 92: bot_l, 93: top_r, 94: bot_r}\n    seq_rank, seq_left, seq_isprob = [], [], []\n    for r in b.itertuples():\n        v = vals(r)\n        seq_rank.append(tuple(_rank(v[p]) - 3 for p in r.positions))\n        seq_left.append(tuple(p in (91, 92) for p in r.positions))\n        seq_isprob.append(tuple(((p in (91, 93)) == (r.prob_top == 1)) for p in r.positions))\n    b[\"seq_rank\"] = seq_rank      # rank -2..2 of each viewed picture, in order\n    b[\"seq_left\"] = seq_left\n    b[\"seq_isprob\"] = seq_isprob\n    return b\n\n\ndef seen_values(b: pd.DataFrame, npv_col: str, unseen=(0.5, 0.5), mag_shift=True):\n    \"\"\"Left/right probability and magnitude of the pictures seen within the first `npv_col`\n    fixations; unseen ones take `unseen` (probability, magnitude). With mag_shift the magnitudes\n    0.15..0.95 become 0.1..0.9, as InfoGathering_Behaviour.m does for accuracy_seen.\"\"\"\n    out = np.zeros((len(b), 4))  # LP, LM, RP, RM\n    for k, r in enumerate(b.itertuples()):\n        n = getattr(r, npv_col)\n        lp, lm, rp, rm = unseen[0], unseen[1], unseen[0], unseen[1]\n        for p in r.positions[:n]:\n            isprob = (p in (91, 93)) == (r.prob_top == 1)\n            left = p in (91, 92)\n            if isprob and left:\n                lp = r.LP\n            elif isprob:\n                rp = r.RP\n            elif left:\n                lm = r.LM - 0.05 if mag_shift else r.LM\n            else:\n                rm = r.RM - 0.05 if mag_shift else r.RM\n        out[k] = lp, lm, rp, rm\n    return out\n\n\n# --------------------------------------------------------------------------- units\n\nUNIT_VARS = [\"Cue1_MatrixRaw\", \"Cue2_MatrixRaw\", \"Cue3_MatrixRaw\", \"Response_MatrixRaw\",\n             \"reg_mat\", \"condition\", \"attendsac1\", \"Left_choice\", \"num_pics_viewed\", \"Lreg\", \"Rreg\",\n             \"P_first\", \"First_pos\", \"Second_pos\", \"Left_prob\", \"Left_pay\", \"Right_prob\",\n             \"Right_pay\", \"pictures_views\", \"Prob_top\", \"Cue1_ON\", \"Response_time\", \"SpikeTable\",\n             \"men\", \"sdev\", \"sb\", \"snum\", \"chnum\", \"brain_region\", \"BhvInfo\", \"inf_trials\",\n             \"nInfoGatheringTrials\"]\n\n\ndef slide(raster: np.ndarray, window=200, step=10) -> np.ndarray:\n    \"\"\"sliding_regression_ols_perm.m smoothing: mean of `window` ms starting every `step` ms.\"\"\"\n    n = raster.shape[1]\n    nb = n // step - (window // step - 1)\n    c = np.concatenate([np.zeros((raster.shape[0], 1)), np.cumsum(raster, axis=1, dtype=float)], 1)\n    starts = np.arange(nb) * step\n    return (c[:, starts + window] - c[:, starts]) / window\n\n\ndef conv_same_200(x: np.ndarray) -> np.ndarray:\n    \"\"\"MATLAB conv2(1, ones(1,200)/200, x, 'same') along rows.\"\"\"\n    n = x.shape[1]\n    c = np.concatenate([np.zeros((x.shape[0], 1)), np.cumsum(x, axis=1, dtype=float)], 1)\n    k = np.arange(n)\n    lo = np.clip(k - 99, 0, n)\n    hi = np.clip(k + 101, 0, n)\n    return (c[:, hi] - c[:, lo]) / 200\n\n\ndef _long_raster(spikes, events, pre, post, men, sdev):\n    \"\"\"neuron_matrix.m (1000 per spike), z-scored by men/sdev, 200 ms 'valid' boxcar, every\n    10 ms (InfoGathering_Neurons_Ramp_to_choice.m).\"\"\"\n    n = pre + post + 1\n    out = np.zeros((len(events), n))\n    for a, (st, ev) in enumerate(zip(spikes, events)):\n        st = np.atleast_1d(st)\n        t = st[(st >= ev - pre) & (st <= ev + post)]\n        idx = (t - (ev - pre)).astype(int)\n        out[a, idx] = 1000.0\n    out = (out - men) / sdev\n    c = np.concatenate([np.zeros((len(events), 1)), np.cumsum(out, axis=1)], 1)\n    valid = (c[:, 200:] - c[:, :-200]) / 200\n    return valid[:, ::10].astype(np.float32)\n\n\ndef rsa_inputs(lreg1, rreg1, p_first, raster, first_pos=None):\n    \"\"\"calculate_RSA_matrices.m: mean spike count 100 < t < 500 ms per condition (20), the\n    1 ms smoothed condition means (20 x 800), and with `first_pos` the 40 conditions split by\n    top/bottom (calculate_RSA_matrices_updown.m).\"\"\"\n    pf = p_first.astype(bool)\n    cond = np.full(len(lreg1), -1)\n    L, R = lreg1 > 0, rreg1 > 0\n    cond[L & pf] = lreg1[L & pf] - 1\n    cond[L & ~pf] = lreg1[L & ~pf] - 1 + 5\n    cond[R & pf] = rreg1[R & pf] - 1 + 10\n    cond[R & ~pf] = rreg1[R & ~pf] - 1 + 15\n    tb = np.arange(-199, 601)\n    nsp = raster[:, (tb > 100) & (tb < 500)].sum(1)\n    sm = conv_same_200(raster)\n    m20 = np.zeros(20)\n    s20 = np.zeros((20, raster.shape[1]), np.float32)\n    for c in range(20):\n        sel = cond == c\n        if sel.any():\n            m20[c] = nsp[sel].mean()\n            s20[c] = sm[sel].mean(0)\n        else:\n            m20[c] = np.nan\n    out = dict(m20=m20, s20=s20)\n    if first_pos is not None:\n        up = (first_pos % 2) == 1\n        m40 = np.zeros(40)\n        for c in range(20):\n            for k, sel_up in enumerate((up, ~up)):\n                sel = (cond == c) & sel_up\n                m40[c + 20 * k] = nsp[sel].mean() if sel.any() else 0.0\n        out[\"m40\"] = m40\n    return out\n\n\ndef load_units(info: pd.DataFrame, areas=(1, 2, 3), long_areas=(1,)) -> dict:\n    \"\"\"Read the preprocessed units of `areas` and reduce each as it loads.\n\n    Returns a dict unit -> dict with the trial variables, the GLM bins of each epoch\n    (`X1`, `X2`, `X3`, `XR`: trials x 61, spikes per ms), RSA inputs, mean rates, and for units\n    of `long_areas` the long rasters of Figure 6 (`L1`, `LR`).\n    \"\"\"\n    raw = read_bytes(\"neuronal_data/LTH_processed_data.zip\")\n    z = zipfile.ZipFile(io.BytesIO(raw))\n    out = {}\n    for u in info.index[info.area.isin(areas)]:\n        m = sio.loadmat(io.BytesIO(z.read(f\"LTH_processed_data/Unit{u:04d}.mat\")),\n                        variable_names=UNIT_VARS, squeeze_me=True, struct_as_record=False)\n        d = {}\n        for k in [\"reg_mat\", \"condition\", \"attendsac1\", \"Left_choice\", \"num_pics_viewed\", \"Lreg\",\n                  \"Rreg\", \"P_first\", \"First_pos\", \"Second_pos\", \"Left_prob\", \"Left_pay\",\n                  \"Right_prob\", \"Right_pay\", \"pictures_views\", \"Prob_top\", \"Cue1_ON\",\n                  \"Response_time\"]:\n            d[k] = np.asarray(m[k], dtype=float)\n        for k in [\"men\", \"sdev\", \"snum\", \"chnum\", \"brain_region\", \"nInfoGatheringTrials\"]:\n            d[k] = float(m[k])\n        d[\"sb\"] = str(m[\"sb\"])\n        for k, src in [(\"X1\", \"Cue1_MatrixRaw\"), (\"X2\", \"Cue2_MatrixRaw\"),\n                       (\"X3\", \"Cue3_MatrixRaw\"), (\"XR\", \"Response_MatrixRaw\")]:\n            d[k] = slide(np.asarray(m[src], dtype=np.float32)).astype(np.float32)\n        r1 = np.asarray(m[\"Cue1_MatrixRaw\"], dtype=np.float32)\n        d[\"rsa\"] = rsa_inputs(d[\"Lreg\"][:, 0].astype(int), d[\"Rreg\"][:, 0].astype(int),\n                              d[\"P_first\"], r1, d[\"First_pos\"].astype(int))\n        bi = m[\"BhvInfo\"]\n        osc = np.asarray(bi.OverallSpikeCodes, dtype=float)\n        # reading (a): whole session, spikes over the span of the session's spike train\n        d[\"rate_session\"] = 1000.0 * (len(osc) - 1) / max(osc.max(), 1.0)\n        # reading (b): analysed trials, from trial start to response\n        st = m[\"SpikeTable\"]\n        resp = d[\"Response_time\"]\n        nsp = sum(np.sum((np.atleast_1d(s) >= 0) & (np.atleast_1d(s) <= r)) for s, r in zip(st, resp))\n        d[\"rate_trials\"] = 1000.0 * nsp / resp.sum()\n        te = np.asarray(bi.TrialError, dtype=float)\n        cn = np.asarray(bi.ConditionNumber, dtype=float)\n        d[\"n_info_trials_all\"] = int(np.isin(cn, (3, 4)).sum())\n        d[\"n_info_completed\"] = int((np.isin(cn, (3, 4)) & np.isin(te, (0, 6))).sum())\n        if int(d[\"brain_region\"]) in long_areas:\n            d[\"L1\"] = _long_raster(st, d[\"Cue1_ON\"], 500, 3000, d[\"men\"], d[\"sdev\"])\n            d[\"LR\"] = _long_raster(st, d[\"Response_time\"], 3000, 500, d[\"men\"], d[\"sdev\"])\n        out[u] = d\n    del raw, z\n    return out\n\n\n# --------------------------------------------------------------------------- GLM\n\ndef glm_design(d: dict) -> np.ndarray:\n    \"\"\"EVs 1 to 18 (InfoGathering_Neurons_Cue123_alltrials_attentional_value_final.m).\"\"\"\n    rm, cond, a1 = d[\"reg_mat\"], d[\"condition\"], d[\"attendsac1\"]\n    n = len(cond)\n    X = np.zeros((n, 18))\n    X[:, 0:4] = rm * (cond == 3)[:, None]\n    X[:, 4:6] = rm[:, 0:2] * (cond == 4)[:, None]\n    X[:, 6:8] = rm[:, 2:4] * (a1 == 1)[:, None]\n    X[:, 8:10] = rm[:, 2:4] * (a1 == -1)[:, None]\n    X[:, 10] = cond == 3\n    X[:, 11] = cond == 4\n    sg = np.sign\n    X[:, 12] = sg(X[:, 0]) * X[:, 1]\n    X[:, 13] = -sg(X[:, 4]) * X[:, 5]\n    X[:, 14] = -sg(X[:, 0] + X[:, 1]) * X[:, 2]\n    X[:, 15] = -sg(X[:, 4] - X[:, 5]) * X[:, 8] + sg(X[:, 4] - X[:, 5]) * X[:, 6]\n    lc = np.where(d[\"Left_choice\"] == 0, -1.0, d[\"Left_choice\"])\n    X[:, 16] = lc * (cond == 3)\n    X[:, 17] = lc * (cond == 4)\n    return X\n\n\ndef glm_contrasts() -> np.ndarray:\n    \"\"\"Contrasts 1 to 35 of the GLM script (rows; 0-based index = contrast number - 1).\"\"\"\n    c = np.zeros((35, 18))\n    c[:18] = np.eye(18)\n    e = np.eye(18)\n    c[18:20] = e[0:2] + e[4:6]\n    c[20:22] = e[6:8] + e[8:10]\n    c[22] = e[12] + e[13]\n    c[23:25] = e[6:8] - e[8:10]\n    c[25:27] = e[0:2] - e[4:6]\n    c[27] = e[12] - e[13]\n    c[28] = e[16] + e[17]\n    c[29] = e[14] + e[15]\n    c[30] = e[5] - e[4]\n    c[31] = e[2] - e[0]\n    c[32] = e[2] - e[1]\n    c[33] = e[0] + e[1]\n    c[34] = e[4] + e[5]\n    return c\n\n\ndef ols(Y: np.ndarray, X: np.ndarray, C: np.ndarray):\n    \"\"\"ols.m: contrasts of parameter estimates, their variances and T-statistics.\n    Y is trials x bins. Returns (cope, varcope, t), each contrasts x bins.\"\"\"\n    P = np.linalg.pinv(X)\n    pe = P @ Y\n    res = Y - X @ pe\n    dof = X.shape[0] - np.linalg.matrix_rank(X)\n    sig = (res * res).sum(0) / dof\n    pre = np.einsum(\"ij,jk,ik->i\", C, P @ P.T, C)\n    cope = C @ pe\n    var = pre[:, None] * sig[None, :]\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        t = cope / np.sqrt(var)\n    return cope, var, t\n\n\ndef cpd(Y: np.ndarray, X: np.ndarray) -> np.ndarray:\n    \"\"\"cpd.m: coefficient of partial determination of each column of X (regressors x bins).\"\"\"\n    def sse(A):\n        return ((Y - A @ (np.linalg.pinv(A) @ Y)) ** 2).sum(0)\n    full = sse(X)\n    out = np.zeros((X.shape[1], Y.shape[1]))\n    for i in range(X.shape[1]):\n        red = sse(np.delete(X, i, axis=1))\n        with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n            out[i] = (red - full) / red\n    return out\n\n\ndef fit_glm(d: dict, epochs=(\"X1\", \"X2\", \"X3\", \"XR\"), with_cpd=False, halves=True) -> dict:\n    \"\"\"Sliding GLM of one unit on trials with 3 or more cues viewed.\"\"\"\n    X = glm_design(d)\n    keep = d[\"num_pics_viewed\"] >= 3\n    n = len(keep)\n    odd = np.zeros(n, bool)\n    odd[0::2] = True\n    C = glm_contrasts()\n    out = {\"keep\": keep, \"odd\": odd}\n    for ep in epochs:\n        Y = d[ep].astype(float)[keep]\n        Xk = X[keep]\n        out[\"t\" + ep] = ols(Y, Xk, C)[2]\n        out[\"b\" + ep] = ols(Y, Xk, C)[0]\n        if halves:\n            for name, sel in ((\"odd\", odd[keep]), (\"even\", ~odd[keep])):\n                out[f\"t{ep}_{name}\"] = ols(Y[sel], Xk[sel], C)[2]\n        if with_cpd:\n            out[\"cpd\" + ep] = cpd(Y, Xk)\n    return out\n\n\n# --------------------------------------------------------------------------- RSA\n\ndef rsa_matrix(M: np.ndarray) -> np.ndarray:\n    \"\"\"Fig4_RSA.m: corrcoef(normalise(unitmat(:,ok),1)') for a conditions x units matrix;\n    units that never fire in the window are left out.\"\"\"\n    ok = ~np.all(M == 0, axis=0) & np.all(np.isfinite(M), axis=0)\n    Z = M[:, ok]\n    Z = (Z - Z.mean(0)) / Z.std(0, ddof=1)\n    return np.corrcoef(Z)\n\n\ndef rsa_design(alternative=False) -> tuple[np.ndarray, list]:\n    \"\"\"The seven columns of Fig4_RSA.m: mean, diagonal, stimulus identity, attended value,\n    accept/reject, spatial attention, left/right value; templates 3 to 7 divided by their\n    maximum absolute value. With `alternative`, attended value is the Supplementary Note's\n    -|rank(i) - rank(j)| (demeaned, as the commented line of Fig4_RSA.m), and left/right value\n    follows it.\"\"\"\n    m1 = np.tile(np.arange(-2, 3), (5, 1))\n    m2 = m1.T\n    r1 = np.ones((20, 20))\n    r2 = np.eye(20)\n    r3 = np.block([[np.zeros((10, 10)), np.eye(10)], [np.eye(10), np.zeros((10, 10))]])\n    if alternative:\n        r4 = -np.tile(np.abs(m1 - m2), (4, 4)).astype(float)\n        r4 = r4 - r4.mean()\n    else:\n        r4 = np.tile(m1 * m2, (4, 4)).astype(float)\n    r5 = (np.tile(((m1 < 0) & (m2 < 0)) | ((m1 > 0) & (m2 > 0)), (4, 4)).astype(float)\n          - np.tile(((m1 > 0) & (m2 < 0)) | ((m1 < 0) & (m2 > 0)), (4, 4)).astype(float))\n    r6 = np.block([[np.ones((10, 10)), np.zeros((10, 10))], [np.zeros((10, 10)), np.ones((10, 10))]])\n    r7 = (r6 > 0) * r4\n    dm = np.column_stack([r.ravel(order=\"F\") for r in (r1, r2, r3, r4, r5, r6, r7)])\n    dm[:, 2:] = dm[:, 2:] / np.abs(dm[:, 2:]).max(0)\n    names = [\"mean\", \"diagonal\", \"stimulus identity\", \"attended value\", \"accept/reject\",\n             \"spatial attention\", \"left/right value\"]\n    return dm, names\n\n\ndef rsa_ftest_parts(dm: np.ndarray):\n    \"\"\"Design for the between-region F-tests of Fig4_RSA.m (ols.m with Ftests): three regions\n    stacked, one F per template comparing its three coefficients.\"\"\"\n    k = dm.shape[1]\n    dmS = np.zeros((3 * 400, 3 * k))\n    for r in range(3):\n        dmS[400 * r:400 * (r + 1), k * r:k * (r + 1)] = dm\n    cmatS = np.hstack([np.eye(2 * k), -np.vstack([np.eye(k), np.eye(k)])])\n    full_R = np.eye(dmS.shape[0]) - dmS @ np.linalg.pinv(dmS)\n    parts = []\n    for i in range(k):\n        tc = cmatS[[i, i + k]]\n        corth = np.eye(dmS.shape[1]) - tc.T @ np.linalg.pinv(tc.T)\n        desorth = dmS @ corth\n        resO = np.eye(dmS.shape[0]) - desorth @ np.linalg.pinv(desorth)\n        M = resO - full_R\n        parts.append((M, np.linalg.matrix_rank(M @ dmS)))\n    dof = dmS.shape[0] - np.linalg.matrix_rank(dmS)\n    return dmS, full_R, parts, dof\n\n\ndef rsa_fstats(y: np.ndarray, ftp) -> np.ndarray:\n    dmS, full_R, parts, dof = ftp\n    pe = np.linalg.pinv(dmS) @ y\n    fitted = dmS @ pe\n    den = y @ full_R @ y\n    return np.array([(fitted @ M @ fitted) / den * dof / r for M, r in parts])\n\n\ndef t75(vec: np.ndarray, times: np.ndarray) -> tuple[float, float, float]:\n    \"\"\"calculate_t75max.m: first time the curve exceeds 3/4 of its maximum.\"\"\"\n    i = int(np.argmax(vec))\n    mx = vec[i]\n    above = np.flatnonzero(vec > 0.75 * mx)\n    return float(times[above[0]]), float(times[i]), float(mx)\n\n\n# --------------------------------------------------------------------------- statistics\n\ndef fisher_z(r1, n1, r2, n2, two_sided=True):\n    z = (np.arctanh(r1) - np.arctanh(r2)) / np.sqrt(1 / (n1 - 3) + 1 / (n2 - 3))\n    p = 2 * stats.norm.sf(abs(z)) if two_sided else stats.norm.sf(z)\n    return z, p\n\n\ndef chi2_yates(k1, n1, k2, n2):\n    \"\"\"chi2.m: 2 x 2 chi-square with Yates' correction.\"\"\"\n    obs = np.array([[k1, k2], [n1 - k1, n2 - k2]], float)\n    if (obs == 0).any():\n        return np.nan, np.nan\n    exp = obs.sum(1, keepdims=True) * obs.sum(0, keepdims=True) / obs.sum()\n    chi = (((np.abs(obs - exp) - 0.5) ** 2) / exp).sum()\n    return chi, stats.chi2.sf(chi, 1)\n\n\ndef binom_p_code(k, n, p0=0.05):\n    \"\"\"Fig8_single_neuron_coding.m: (1 - binocdf(k, n, p0)) * 2.\"\"\"\n    return 2 * stats.binom.sf(k, n, p0)\n\n\ndef clusters(mask: np.ndarray):\n    lab, n = ndimage.label(mask)\n    return lab, n\n"
}
```

```
File created successfully at: entries/hunt-2018/pfc7.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > t1.py <<'EOF'
import sys,time,resource; sys.path.insert(0,'entries/hunt-2018')
import pfc7, numpy as np, pandas as pd
t=time.time()
info=pfc7.units_info(); print(info.area.value_counts().sort_index(), info.head())
print(info.loc[[87,653]])
sub=info[info.area.isin([1,2,3])].iloc[:12]
U=pfc7.load_units(sub)
print('units',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
for u,d in list(U.items())[:5]:
    print(u, d['sb'], d['snum'], d['chnum'], d['brain_region'], info.loc[u,['subject','session','channel','area','info_rate']].tolist(), d['men'], d['rate_session'], d['rate_trials'], d['X1'].shape, d.get('L1',np.zeros(0)).shape, d['n_info_completed'], d['nInfoGatheringTrials'])
g=pfc7.fit_glm(U[sub.index[0]],with_cpd=True)
print(g['tX1'].shape, g['tX1'][18,::10])
import pickle; pickle.dump((sub.index.tolist(),{u:pfc7.fit_glm(U[u]) for u in sub.index}),open('glm_sub.pkl','wb'))
print(time.time()-t)
EOF
python t1.py
```

```
area
1    198
2    156
3    195
4      9
5    160
6      6
Name: count, dtype: int64       area area_name subject  session  channel  info_rate
unit                                                     
1        1       ACC       F        2        1   8.211533
2        1       ACC       F        2       17  11.270330
3        1       ACC       F        2       18   7.057437
4        1       ACC       F        2       18  10.312200
5        1       ACC       F        2       18   8.195438
      area area_name subject  session  channel  info_rate
unit                                                     
87       2     DLPFC       F       10       23   4.844635
653      3       OFC       M       46        5   1.826318
units 6.716336965560913 0.959116
1 F 2.0 1.0 1.0 ['F', np.int64(2), np.int64(1), np.int64(1), np.float64(8.211532853418149)] 8.498957326272127 8.499129594707028 6.524070566509254 (450, 61) (450, 331) 450 450.0
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > t2.py <<'EOF'
import sys,time,io; sys.path.insert(0,'entries/hunt-2018')
import pfc7, numpy as np, pickle, h5py
ids,G=pickle.load(open('glm_sub.pkl','rb'))
t=time.time()
raw=pfc7.read_bytes("neuronal_regression_results/info_gathering_cue123_alltrials_attentional_final.mat")
print(len(raw), raw[:100], time.time()-t)
try:
    h=h5py.File(io.BytesIO(raw),'r'); print(list(h.keys())[:80])
    ts=h['t_stats1']; print(ts.shape)
    for k,u in enumerate(ids[:4]):
        a=h[ts[u-1,0] if ts.shape[1]==1 else ts[0,u-1]][()]
        print(u, a.shape, np.abs(a.T - G[u]['tX1']).max(), a.T[18,::10])
except Exception as e:
    import scipy.io as sio
    print('not h5',e)
    m=sio.loadmat(io.BytesIO(raw),variable_names=['t_stats1','t_stats2','timebins'],squeeze_me=True)
    for u in ids[:4]:
        a=m['t_stats1'][u-1]; print(u,a.shape, np.nanmax(np.abs(a.T-G[u]['tX1'])))
EOF
python t2.py
```

```
314620182 b'MATLAB 5.0 MAT-file, Platform: MACI64, Created on: Mon May 14 20:17:30 2018                         ' 4.869426012039185
not h5 Unable to synchronously open file (file signature not found)
1 (61, 35) 2.2548306688463526e-07
2 (61, 35) 4.5248298974343015e-07
3 (61, 35) 1.6168598726551409e-07
4 (61, 35) 4.065984704482162e-07
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > t3.py <<'EOF'
import sys,time,resource; sys.path.insert(0,'entries/hunt-2018')
import pfc7, numpy as np, pandas as pd
t=time.time()
b=pfc7.load_behaviour('F'); print(time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
b.to_pickle('behF.pkl')
print(len(b), b.session.nunique(), b.trial_error.value_counts().to_dict(), b.condition.value_counts().to_dict(), b.move_time.isna().sum())
acc = ((b.LEV>=b.REV)&(b.left_choice==1))|((b.REV>=b.LEV)&(b.left_choice==0))
print('acc code', acc.mean())
ne=b.LEV!=b.REV
print('acc ties out', (((b.LEV>b.REV)==(b.left_choice==1))[ne]).mean(), 'ties', (~ne).sum())
print('early prezero',1-(b.npv_prezero==4).mean(), 'npv',1-(b.npv==4).mean(), 'npv250', 1-(b.npv250==4).mean())
print(b.npv.value_counts().to_dict(), b.npv250.value_counts().to_dict())
EOF
python t3.py
```

```
43.430981397628784 2.638584
9863 25 {0: 7753, 6: 2110} {4: 5040, 3: 4823} 0
acc code 0.766602453614519
acc ties out 0.7571473784154447 ties 384
early prezero 0.8552164655784245 npv 0.5423299199026665 npv250 0.9558957720774612
{4: 4514, 3: 4119, 2: 1230} {3: 4790, 2: 4638, 4: 435}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/hunt-2018 && python3 - <<'EOF'
p='pfc7.py'; s=open(p).read()
s=s.replace('''def glm_contrasts() -> np.ndarray:
    """Contrasts 1 to 35 of the GLM script (rows; 0-based index = contrast number - 1)."""
    c = np.zeros((35, 18))''','''def glm_contrasts() -> np.ndarray:
    """Contrasts 1 to 35 of the GLM script (rows; 0-based index = contrast number - 1), and
    four more for Figure 7 read as attribute trials at cue 3 (36 EV7 - EV5, 37 EV7 - EV6,
    38 EV9 - EV5, 39 EV9 - EV6)."""
    c = np.zeros((39, 18))''')
s=s.replace('''    c[34] = e[4] + e[5]
    return c''','''    c[34] = e[4] + e[5]
    c[35] = e[6] - e[4]
    c[36] = e[6] - e[5]
    c[37] = e[8] - e[4]
    c[38] = e[8] - e[5]
    return c''')
open(p,'w').write(s)
EOF
date -u
```

```
Sat Nov 14 18:54:13 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/nbsrc.py",
 "content": "# %% [markdown]\n# # Reproducing Hunt, Malalasekera et al. (2018) from CRCNS pfc-7\n#\n# Paper: Hunt, Malalasekera, de Berker, Miranda, Farmer, Behrens & Kennerley (2018), \"Triple\n# dissociation of attention and decision computations across prefrontal cortex\", Nature\n# Neuroscience 21, 1471-1481, doi:10.1038/s41593-018-0239-5.\n#\n# Data: CRCNS data set pfc-7 (doi:10.6080/K0PZ5712), read anonymously from the public S3 bucket\n# `crcnsarchive` under `pfc-7/live/`. CRCNS data sets are not versioned, so the version is\n# recorded as `unversioned`; the only published copy is the one under `live/` (data description\n# version 0.5, September 6, 2018), and it is the one pinned here. The MD5 sums of the files read,\n# from the data set's `checksums.md5`, are printed below, so that a later change is detectable.\n#\n# Claims: `claims/hunt-2018.yaml`, written from the version of record (PMC6331040) with its\n# supplement. The paper's MATLAB scripts are files of the data set (`scripts.zip`); where the\n# claims file leaves a detail open and a script settles it, the script is cited (see `pfc7.py`).\n#\n# CLAIMS_TABLE\n\n# %%\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport resource\nimport time\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport statsmodels.api as sm\nfrom scipy import stats\n\nimport pfc7\n\nT0 = time.time()\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\n\n\ndef section_rng(name):\n    \"\"\"One generator per claim section, seeded from its name.\"\"\"\n    return np.random.default_rng(abs(hash(name)) % (2**32) if False else sum(map(ord, name)) * 7919)\n\n\n# %% [markdown]\n# ## Loading\n#\n# The file listing and checksums, the units table, the two behavioural files (one at a time, in\n# memory), and the preprocessed units of ACC, DLPFC and OFC (reduced as they load).\n\n# %%\nlisting = pfc7.listing()\nmd5 = pfc7.checksums()\nREAD = [\"behavioural_data/Miles_InfoGathering_All_Data.mat\",\n        \"behavioural_data/Frank_InfoGathering_All_Data.mat\",\n        \"neuronal_data/LTH_processed_data.zip\", \"other_data/all_units_info.mat\",\n        \"neuronal_regression_results/info_gathering_cue123_alltrials_attentional_final.mat\",\n        \"scripts.zip\"]\nprint(f\"{len(listing)} keys under pfc-7/, {listing['size'].sum() / 1e9:.1f} GB\")\nfor f in READ:\n    print(f\"{md5[f]}  {f}\")\ninfo = pfc7.units_info()\nbeh = pd.concat([pfc7.load_behaviour(\"M\"), pfc7.load_behaviour(\"F\")], ignore_index=True)\nprint(f\"behaviour loaded, {time.time() - T0:.0f} s\")\nU = pfc7.load_units(info, areas=(1, 2, 3), long_areas=(1,))\nprint(f\"{len(U)} units loaded, {time.time() - T0:.0f} s, peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB\")\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nzips = listing[listing.key.str.match(r\"pfc-7/live/neuronal_data/[FM]\\d{3}\\.zip\")]\nzip_sessions = zips.key.str.extract(r\"/([FM])(\\d{3})\\.zip\")\nprint(\"raw recording sessions (zip files):\", zip_sessions[0].value_counts().to_dict())\nprint(\"behavioural sessions:\", beh.groupby(\"subject\").session.nunique().to_dict(),\n      \" trials:\", beh.groupby(\"subject\").size().to_dict())\nprint(\"trial errors in the behavioural files:\", beh.trial_error.value_counts().to_dict(),\n      \" conditions:\", beh.condition.value_counts().to_dict())\nprint(\"units in all_units_info.mat by area:\", info.area_name.value_counts().to_dict())\nprint(\"subject by session counts of units (all areas):\",\n      info.groupby(\"subject\").session.nunique().to_dict())\n# the unit files agree with all_units_info.mat on subject, session, channel and area\nmism = [u for u, d in U.items() if (d[\"sb\"], int(d[\"snum\"]), int(d[\"chnum\"]), int(d[\"brain_region\"]))\n        != (info.loc[u, \"subject\"], info.loc[u, \"session\"], info.loc[u, \"channel\"], info.loc[u, \"area\"])]\nprint(\"units whose file disagrees with all_units_info.mat:\", mism)\n# value ranges\nprint(\"probabilities:\", sorted(np.round(pd.unique(beh[[\"LP\", \"RP\"]].values.ravel()), 3)))\nprint(\"magnitudes:\", sorted(np.round(pd.unique(beh[[\"LM\", \"RM\"]].values.ravel()), 3)))\nprint(\"pictures viewed (eye codes):\", beh.npv.value_counts().sort_index().to_dict())\nprint(\"joystick movement time found on\", beh.move_time.notna().sum(), \"of\", len(beh), \"trials\")\nrt = beh.response - beh.cue1_on\nprint(f\"response time from cue 1, ms: median {rt.median():.0f}, range {rt.min():.0f} to {rt.max():.0f}\")\nu0 = U[1]\nprint(\"rasters: Cue1_MatrixRaw holds 0/1 per ms (spikes, not the 1000 per spike of neuron_matrix.m);\"\n      f\" GLM bins {u0['X1'].shape[1]} centred {pfc7.TIMEBINS[0]} to {pfc7.TIMEBINS[-1]} ms\")\nrates = pd.DataFrame({u: dict(area=AREA, session_rate=d[\"rate_session\"], trial_rate=d[\"rate_trials\"],\n                              men=d[\"men\"], info_rate=info.loc[u, \"info_rate\"])\n                      for u, d in U.items() for AREA in [pfc7.AREAS[int(d[\"brain_region\"])]]}).T\nprint(\"mean rate (Hz) per unit, medians by area:\")\nprint(rates.groupby(\"area\")[[\"session_rate\", \"trial_rate\", \"men\", \"info_rate\"]].median().round(2))\nprint(\"whole-session rate from OverallSpikeCodes against the stored men: max |diff| \"\n      f\"{np.abs(rates.session_rate.astype(float) - rates.men.astype(float)).max():.3f} Hz\")\n# duplicate recordings: identical spike-count vectors in the cue 1 window\nsig = {}\nfor u, d in U.items():\n    key = (d[\"sb\"], int(d[\"snum\"]), tuple(np.round(d[\"X1\"][:, 40] * 1000, 3)))\n    sig.setdefault(key, []).append(u)\ndups = [v for v in sig.values() if len(v) > 1]\nprint(\"pairs of units with identical cue 1 activity in every trial:\", dups)\n# behaviour in the unit files against the behavioural files (one unit per session)\nchk = []\nfor (sb, sn), grp in info[info.area.isin([1, 2, 3])].groupby([\"subject\", \"session\"]):\n    d = U[grp.index[0]]\n    bs = beh[(beh.subject == sb)]\n    sess_ids = sorted(bs.session.unique())\n    chk.append(dict(subject=sb, session=sn, unit_trials=int(d[\"nInfoGatheringTrials\"])))\nchk = pd.DataFrame(chk)\nprint(\"sessions with units in ACC/DLPFC/OFC:\", chk.groupby(\"subject\").size().to_dict())\n\n# %% [markdown]\n# The GLM written here (`pfc7.fit_glm`) is checked against the T-statistics the authors stored in\n# `neuronal_regression_results/info_gathering_cue123_alltrials_attentional_final.mat`, which the\n# data set's scripts load for Figures 5 to 7. This checks the implementation; no result below uses\n# the stored values.\n\n# %% tags=[\"sanity\"]\nG = {u: pfc7.fit_glm(d, with_cpd=(int(d[\"brain_region\"]) == 3)) for u, d in U.items()}\nprint(f\"GLM fitted, {time.time() - T0:.0f} s\")\nimport io as _io\nimport scipy.io as _sio\n_raw = pfc7.read_bytes(READ[4])\n_st = _sio.loadmat(_io.BytesIO(_raw), variable_names=[\"t_stats1\", \"t_stats2\", \"t_stats3\", \"t_statsR\"],\n                   squeeze_me=True)\ndel _raw\ndev = []\nfor u in G:\n    for k, ep in [(\"t_stats1\", \"tX1\"), (\"t_stats2\", \"tX2\"), (\"t_stats3\", \"tX3\"), (\"t_statsR\", \"tXR\")]:\n        a = np.asarray(_st[k][u - 1], float).T\n        b = G[u][ep][:35]\n        ok = np.isfinite(a) & np.isfinite(b)\n        dev.append(np.abs(a[ok] - b[ok]).max() if ok.any() else 0.0)\ndel _st\nprint(f\"max |T here - T stored| over {len(G)} units and 4 epochs: {max(dev):.2e}\")\nnan_units = [u for u in G if not np.isfinite(G[u][\"tX3\"][:35]).all()]\nprint(\"units with non-finite T-statistics:\", nan_units)\n\n# %% [markdown]\n# ### Clock check\n#\n# Every stream shares the clock of the trial table: the cue 1 rasters are cut from each trial's\n# spike times at the cue 1 onset code, the GLM T-statistic for the attended cue 1 value (EVs 1 + 5)\n# rises only after cue 1 onset, and with the trial labels shifted by one trial the response\n# vanishes. The contrast is shown for OFC, the region with the strongest value code.\n\n# %% tags=[\"sanity\"]\nofc_sel = [u for u in U if int(U[u][\"brain_region\"]) == 3 and info.loc[u, \"info_rate\"] >= 1 and u != 87]\ndef mean_abs_t(shift):\n    out = []\n    for u in ofc_sel:\n        d = dict(U[u])\n        if shift:\n            for k in [\"reg_mat\", \"condition\", \"attendsac1\", \"Left_choice\", \"num_pics_viewed\"]:\n                d[k] = np.roll(d[k], shift, axis=0)\n        out.append(np.abs(pfc7.fit_glm(d, epochs=(\"X1\",), halves=False)[\"tX1\"][18]))\n    return np.mean(out, axis=0)\nclk = pd.DataFrame({\"true labels\": mean_abs_t(0), \"labels shifted 1 trial\": mean_abs_t(1)},\n                   index=pfc7.TIMEBINS)\nprint(\"mean |T| of cue 1 value across OFC neurons, by bin centre (ms after cue 1):\")\nprint(clk.iloc[::5].round(2).T)\nfor s in [\"Miles\", \"Frank\"]:\n    pass\n\n# %% [markdown]\n# ## Unit selection\n#\n# Units in ACC, DLPFC and OFC with mean rate of at least 1 Hz. The paper's scripts take the rate\n# from `all_units_info.mat` and also drop unit 87 (Fig4_RSA.m and the other figure scripts) and,\n# for Figures 5 and 7, unit 653. That is the selection used below (`SEL`, `SEL5`); the claim\n# neuron-counts compares the counts under the claims file's readings of the rate.\n\n# %%\nbase = info[info.area.isin([1, 2, 3])].copy()\nbase[\"session_rate\"] = [U[u][\"rate_session\"] for u in base.index]\nbase[\"trial_rate\"] = [U[u][\"rate_trials\"] for u in base.index]\nkeep = (base.info_rate >= 1) & ~base.index.isin(pfc7.BAD_UNITS)\nSEL = {a: base.index[keep & (base.area == a)].tolist() for a in (1, 2, 3)}\nSEL5 = {a: [u for u in SEL[a] if u not in pfc7.NAN_TSTAT_UNITS] for a in (1, 2, 3)}\nprint({pfc7.AREAS[a]: len(v) for a, v in SEL.items()}, \"Figures 5 and 7:\",\n      {pfc7.AREAS[a]: len(v) for a, v in SEL5.items()})\nNAMES = pfc7.AREAS\n\n# %% [markdown]\n# ## sessions-and-trials\n#\n# > Behaviour comes from 25 sessions of monkey F and 32 of monkey M, 9,863 trials for F and\n# > 14,251 for M.\n#\n# The behavioural files hold only completed option and attribute trials (trial errors 0 and 6),\n# so reading (a) is their trial count. Aborted trials are counted from the full trial lists\n# (`BhvInfo`) in the unit files, which exist only for sessions with units; reading (c) drops\n# trials of equal expected value. \"Miles\" is M and \"Frank\" is F (the unit files' `sb` field and the\n# data descriptor's naming).\n\n# %% tags=[\"claim:sessions-and-trials\"]\nsess = beh.groupby(\"subject\").session.nunique()\nntr_a = beh.groupby(\"subject\").size()\nntr_c = beh[beh.LEV != beh.REV].groupby(\"subject\").size()\nab = {}\nfor (sb, sn), grp in base.groupby([\"subject\", \"session\"]):\n    d = U[grp.index[0]]\n    ab[(sb, sn)] = (d[\"n_info_trials_all\"], d[\"n_info_completed\"])\nab = pd.DataFrame(ab, index=[\"all info trials\", \"completed\"]).T\nab.index.names = [\"subject\", \"session\"]\nabs_ = ab.groupby(level=0).sum()\nabs_[\"sessions with units\"] = ab.groupby(level=0).size()\nprint(\"sessions:\", sess.to_dict(), \" expected F 25, M 32\")\nprint(\"(a) completed option and attribute trials:\", ntr_a.to_dict(), \" expected F 9863, M 14251\")\nprint(\"(c) the same without equal expected values:\", ntr_c.to_dict())\nprint(\"(b) with aborted trials, sessions with units only:\")\nprint(abs_)\ncs = beh.groupby([\"subject\", \"session\"]).size()\nprint(\"completed trials per session, unit files against behavioural files (sessions in both, by order):\")\nfor sb in [\"F\", \"M\"]:\n    a = ab.loc[sb, \"completed\"].values\n    b_ = cs.loc[sb].values\n    print(sb, \"unit-file sessions\", len(a), \"behaviour sessions\", len(b_),\n          \"unit-file counts all found among behaviour counts:\", set(a) <= set(b_))\n\n# %% [markdown]\n# RESULT:sessions-and-trials\n\n# %% [markdown]\n# ## neuron-counts\n#\n# > After excluding units with mean firing rate below 1 Hz (9 ACC, 21 DLPFC, 12 OFC), the analyses\n# > use 189 ACC, 135 DLPFC and 183 OFC neurons.\n\n# %% tags=[\"claim:neuron-counts\"]\nrows = []\nfor name, col in [(\"(a) whole session (OverallSpikeCodes)\", \"session_rate\"),\n                  (\"(b) analysed trials, start to response\", \"trial_rate\"),\n                  (\"all_units_info.mat average_firing_rate\", \"info_rate\")]:\n    for drop87 in (False, True):\n        k = base[col] >= 1\n        if drop87:\n            k &= ~base.index.isin(pfc7.BAD_UNITS)\n        r = dict(reading=name + (\", unit 87 dropped\" if drop87 else \"\"))\n        for a in (1, 2, 3):\n            r[NAMES[a]] = int((k & (base.area == a)).sum())\n            r[NAMES[a] + \" excluded\"] = int((~k & (base.area == a)).sum())\n        rows.append(r)\nnc = pd.DataFrame(rows).set_index(\"reading\")\nprint(nc)\nprint(\"expected: ACC 189, DLPFC 135, OFC 183; excluded 9, 21, 12\")\nprint(\"units recorded in these areas:\", base.area.map(NAMES).value_counts().to_dict())\ntab = base.assign(ok=base.info_rate >= 1).groupby([\"subject\", \"session\", \"area_name\"]).size().unstack(fill_value=0)\nprint(\"sessions with units:\", tab.groupby(level=0).size().to_dict(),\n      \" units per area over those sessions:\", tab.sum().to_dict())\nprint(\"unit 87:\", base.loc[87, [\"area_name\", \"subject\", \"session\", \"info_rate\", \"session_rate\"]].to_dict())\n\n# %% [markdown]\n# RESULT:neuron-counts\n\n# %% [markdown]\n# ## choice-accuracy-ev\n#\n# > Monkeys F and M chose the option with the higher expected value on 76.6% and 79.8% of trials.\n\n# %% tags=[\"claim:choice-accuracy-ev\"]\ndef acc_ev(b, ties):\n    hi_left = b.LEV > b.REV\n    eq = b.LEV == b.REV\n    corr = (hi_left & (b.left_choice == 1)) | (~hi_left & ~eq & (b.left_choice == 0))\n    if ties == \"out\":\n        return 100 * corr[~eq].mean()\n    if ties == \"wrong\":\n        return 100 * corr.mean()\n    return 100 * (corr | eq).mean()   # InfoGathering_Behaviour.m counts ties as correct\nr = pd.DataFrame({t: beh.groupby(\"subject\").apply(acc_ev, ties=t) for t in [\"out\", \"wrong\", \"right\"]})\nr.columns = [\"(a) ties left out\", \"(b) ties counted wrong\", \"script: ties counted right\"]\nprint(r.round(2))\nprint(\"ties:\", beh[beh.LEV == beh.REV].groupby(\"subject\").size().to_dict())\nprint(\"expected F 76.6 +/- 7.66, M 79.8 +/- 7.98\")\nprint(\"by session (reading a): \", beh.groupby([\"subject\", \"session\"]).apply(acc_ev, ties=\"out\")\n      .groupby(level=0).agg([\"min\", \"median\", \"max\"]).round(1).to_dict(\"index\"))\n\n# %% [markdown]\n# RESULT:choice-accuracy-ev\n\n# %% [markdown]\n# ## chose-on-partial-information\n#\n# > Monkeys F and M chose before seeing all four cues on 85.5% and 71.4% of trials.\n#\n# The claims file gives no method. InfoGathering_Behaviour.m counts a trial as an early choice\n# when, after correcting the number of pictures for a joystick movement made before the last\n# picture was fixated (`num_pics_viewedprezero`), fewer than four were viewed\n# (`out.earlychoices = 1 - mean(num_pics_viewedprezero==4)`); that is taken here, and the raw count\n# of fixated pictures is shown too.\n\n# %% tags=[\"claim:chose-on-partial-information\"]\npp = pd.DataFrame({\n    \"script (joystick-corrected)\": beh.groupby(\"subject\").apply(lambda b: 100 * (b.npv_prezero < 4).mean()),\n    \"pictures fixated\": beh.groupby(\"subject\").apply(lambda b: 100 * (b.npv < 4).mean()),\n    \"250 ms rule\": beh.groupby(\"subject\").apply(lambda b: 100 * (b.npv250 < 4).mean())})\nprint(pp.round(2))\nprint(\"expected F 85.5 +/- 8.55, M 71.4 +/- 7.14\")\n\n# %% [markdown]\n# RESULT:chose-on-partial-information\n\n# %% [markdown]\n# ## choice-accuracy-observed\n#\n# > Judged by the pictures observed, choice accuracy was 86.3% for monkey F and 87.4% for monkey M.\n#\n# Which pictures count as observed is taken from InfoGathering_Behaviour.m (`accuracy_seen`):\n# those fixated before the joystick moved, dropping a last picture fixated for 250 ms or less\n# (`num_pics_viewed250`). The script also sets unseen cues to 0.5, shifts magnitudes by -0.05 and\n# counts ties as correct; that is shown as a variant.\n\n# %% tags=[\"claim:choice-accuracy-observed\"]\ndef acc_seen(b, npv_col, reading):\n    if reading == \"script\":\n        v = pfc7.seen_values(b, npv_col, unseen=(0.5, 0.5), mag_shift=True)\n        L, R = v[:, 0] * v[:, 1], v[:, 2] * v[:, 3]\n        ties = \"right\"\n    elif reading in (\"a\", \"b\"):\n        v = pfc7.seen_values(b, npv_col, unseen=(0.5, 0.55), mag_shift=False)\n        L, R = v[:, 0] * v[:, 1], v[:, 2] * v[:, 3]\n        ties = \"out\" if reading == \"a\" else \"wrong\"\n    else:  # (c) sum of the observed ranks per option\n        L = np.zeros(len(b)); R = np.zeros(len(b))\n        for k, row in enumerate(b.itertuples()):\n            n = getattr(row, npv_col)\n            for rk, lf in zip(row.seq_rank[:n], row.seq_left[:n]):\n                if lf:\n                    L[k] += rk\n                else:\n                    R[k] += rk\n        ties = \"out\"\n    L = np.round(L, 6); R = np.round(R, 6)\n    lc = b.left_choice.values == 1\n    eq = L == R\n    corr = ((L > R) & lc) | ((R > L) & ~lc)\n    if ties == \"out\":\n        return 100 * corr[~eq].mean()\n    if ties == \"wrong\":\n        return 100 * corr.mean()\n    return 100 * (corr | eq).mean()\nrows = {}\nfor npv_col in [\"npv250\", \"npv\"]:\n    for rd in [\"a\", \"b\", \"c\", \"script\"]:\n        rows[(npv_col, rd)] = beh.groupby(\"subject\").apply(acc_seen, npv_col=npv_col, reading=rd)\naso = pd.DataFrame(rows).T\naso.index.names = [\"pictures seen\", \"reading\"]\nprint(aso.round(2))\nprint(\"expected F 86.3 +/- 8.63, M 87.4 +/- 8.74\")\n\n# %% [markdown]\n# RESULT:choice-accuracy-observed\n\n# %% [markdown]\n# ## figs1ab-cue-weights\n#\n# > In logistic regressions of choice, both monkeys weighted reward probability and magnitude\n# > about equally and used all four viewed cues, with a slight upweighting of the antepenultimate\n# > (n-2) cue, and both showed a small bias towards choosing the second side on option trials.\n#\n# Model B follows InfoGathering_Behaviour.m (choice on left minus right seen probability and seen\n# magnitude, unseen at 0.5, with a constant and a first-side term, separately for option and\n# attribute trials, no further constant). Model A regresses choice on a constant and the final,\n# n-1, n-2 and n-3 viewed pictures, signed + left and - right (the script uses\n# `lastLreg - lastRreg` on the pictures fixated).\n\n# %% tags=[\"claim:figs1ab-cue-weights\"]\ndef model_b(b, seen=True):\n    if seen:\n        v = pfc7.seen_values(b, \"npv250\", unseen=(0.5, 0.5), mag_shift=True)\n        dp, dm = v[:, 0] - v[:, 2], v[:, 1] - v[:, 3]\n    else:\n        dp, dm = (b.LP - b.RP).values, (b.LM - b.RM).values\n    fs = np.array([r.seq_left[0] for r in b.itertuples()], float)\n    base_ = np.column_stack([np.ones(len(b)), dp, dm, fs])\n    X = np.hstack([base_ * (b.condition.values == 3)[:, None], base_ * (b.condition.values == 4)[:, None]])\n    res = sm.GLM(b.left_choice.values, X, family=sm.families.Binomial()).fit()\n    names = [f\"{t} {n}\" for t in (\"option\", \"attribute\") for n in (\"left bias\", \"prob\", \"mag\", \"first side\")]\n    out = pd.DataFrame({\"b\": res.params, \"se\": res.bse, \"p\": res.pvalues}, index=names)\n    waldp = {}\n    for t, o in ((\"option\", 0), (\"attribute\", 4)):\n        c = np.zeros(8); c[o + 1] = 1; c[o + 2] = -1\n        w = res.t_test(c)\n        waldp[t] = float(w.pvalue)\n    return out, waldp\ndef model_a(b, scale):\n    Xs = np.zeros((len(b), 4))\n    for k, r in enumerate(b.itertuples()):\n        n = r.npv\n        for j in range(min(n, 4)):\n            idx = n - 1 - j\n            rk = r.seq_rank[idx]\n            val = rk if scale == \"rank\" else (0.1 + 0.2 * (rk + 2))\n            Xs[k, j] = val if r.seq_left[idx] else -val\n    X = np.column_stack([np.ones(len(b)), Xs])\n    res = sm.GLM(b.left_choice.values, X, family=sm.families.Binomial()).fit()\n    return pd.DataFrame({\"b\": res.params, \"se\": res.bse, \"p\": res.pvalues},\n                        index=[\"left bias\", \"final\", \"n-1\", \"n-2\", \"n-3\"])\nS1 = {}\nfor sb in [\"F\", \"M\"]:\n    b = beh[beh.subject == sb]\n    for seen in (True, False):\n        mb, wp = model_b(b, seen)\n        ci = mb.b.values[:, None] + np.array([-1.96, 1.96]) * mb.se.values[:, None]\n        print(f\"--- {sb}, model B, {'seen values (script)' if seen else 'true values'}\")\n        print(mb.round(4))\n        for t, o in ((\"option\", 0), (\"attribute\", 4)):\n            ov = not (ci[o + 1, 1] < ci[o + 2, 0] or ci[o + 2, 1] < ci[o + 1, 0])\n            print(f\"  {t}: prob/mag ratio {mb.b.iloc[o + 1] / mb.b.iloc[o + 2]:.2f}, 95% CIs overlap {ov},\"\n                  f\" Wald p(prob = mag) {wp[t]:.3g}\")\n            S1[(sb, seen, t)] = dict(pos=(mb.b.iloc[o + 1] > 0) and (mb.b.iloc[o + 2] > 0), overlap=ov, wald=wp[t])\n        S1[(sb, seen, \"first\")] = (mb.b.iloc[3], mb.p.iloc[3])\n    for scale in (\"rank\", \"raw\"):\n        ma = model_a(b, scale)\n        print(f\"--- {sb}, model A, {scale}\")\n        print(ma.round(4))\n        S1[(sb, \"A\", scale)] = ma\n\n# %% tags=[\"claim:figs1ab-cue-weights\"]\nfor seen in (True, False):\n    for eq in (\"overlap\", \"wald\"):\n        ok = True\n        for sb in [\"F\", \"M\"]:\n            for t in (\"option\", \"attribute\"):\n                s = S1[(sb, seen, t)]\n                ok &= s[\"pos\"] and (s[\"overlap\"] if eq == \"overlap\" else s[\"wald\"] > 0.05)\n        print(f\"model B {'seen' if seen else 'true'} values, equal weight by {eq}: holds in both monkeys = {ok}\")\nfor sb in [\"F\", \"M\"]:\n    for seen in (True, False):\n        b_, p_ = S1[(sb, seen, \"first\")]\n        print(f\"{sb} first-side bias, option trials ({'seen' if seen else 'true'}): b = {b_:.3f}, p = {p_:.2g}\")\n    for scale in (\"rank\", \"raw\"):\n        ma = S1[(sb, \"A\", scale)]\n        w = ma.loc[[\"final\", \"n-1\", \"n-2\", \"n-3\"]]\n        print(f\"{sb} model A {scale}: all picture weights > 0 with p < 0.05: {bool(((w.b > 0) & (w.p < 0.05)).all())};\"\n              f\" n-2 weight {w.b['n-2']:.3f} against final {w.b['final']:.3f} and n-1 {w.b['n-1']:.3f}\")\n\n# %% [markdown]\n# RESULT:figs1ab-cue-weights\n\n# %% [markdown]\n# ## figs1cd-fewer-cues-more-accurate\n#\n# > Choices were more often optimal on trials where 2 pictures were viewed than on trials with 3\n# > or 4, because trials ended early when the first two cues gave a larger value difference.\n#\n# The number of pictures viewed is taken from InfoGathering_Behaviour.m (`num_pics_viewed250`,\n# used for Supplementary Figure 1c/d); the raw count of fixated pictures is shown too. Accuracy is\n# reading (a) of choice-accuracy-ev (ties left out).\n\n# %% tags=[\"claim:figs1cd-fewer-cues-more-accurate\"]\ndef vd_cues12(b):\n    out = np.zeros(len(b))\n    for k, r in enumerate(b.itertuples()):\n        lp, lm, rp, rm = 0.5, 0.55, 0.5, 0.55\n        for p in r.positions[:2]:\n            isprob = (p in (91, 93)) == (r.prob_top == 1)\n            left = p in (91, 92)\n            if isprob and left: lp = r.LP\n            elif isprob: rp = r.RP\n            elif left: lm = r.LM\n            else: rm = r.RM\n        out[k] = abs(lp * lm - rp * rm)\n    return out\nbeh[\"vd_true\"] = (beh.LEV - beh.REV).abs()\nbeh[\"vd_12\"] = vd_cues12(beh)\nrows = []\nfor col in [\"npv250\", \"npv\"]:\n    for sb in [\"F\", \"M\"]:\n        b = beh[beh.subject == sb]\n        for n in (2, 3, 4):\n            bb = b[b[col] == n]\n            rows.append(dict(count=col, subject=sb, n=n, trials=len(bb), accuracy=acc_ev(bb, \"out\"),\n                             vd_true=bb.vd_true.mean(), vd_cues12=bb.vd_12.mean()))\ns1cd = pd.DataFrame(rows).set_index([\"count\", \"subject\", \"n\"])\nprint(s1cd.round(3))\nfor col in [\"npv250\", \"npv\"]:\n    for sb in [\"F\", \"M\"]:\n        t = s1cd.loc[(col, sb)]\n        print(col, sb, \"accuracy 2 > 3 and 2 > 4:\", bool(t.accuracy[2] > t.accuracy[3] and t.accuracy[2] > t.accuracy[4]),\n              \"| largest mean value difference at 2 cues, true EV:\", bool(t.vd_true.idxmax() == 2),\n              \", cues 1-2:\", bool(t.vd_cues12.idxmax() == 2))\n\n# %% [markdown]\n# RESULT:figs1cd-fewer-cues-more-accurate\n\n# %% [markdown]\n# ## fig2a-sample-the-favourite\n#\n# > On attribute trials, the free third saccade went preferentially to the option with the higher\n# > value between cue 1 and cue 2.\n#\n# Attribute trials with a third picture fixated (`num_pics_viewed > 2`, as the script's\n# `AvSaccDir12Att`); the third saccade returns to the first option when the third picture is on\n# the first picture's side.\n\n# %% tags=[\"claim:fig2a-sample-the-favourite\"]\nfor sb in [\"F\", \"M\", \"both\"]:\n    b = beh[(beh.condition == 4) & (beh.npv >= 3)]\n    if sb != \"both\":\n        b = b[b.subject == sb]\n    back = np.array([r.seq_left[2] == r.seq_left[0] for r in b.itertuples()], float)\n    d12 = np.array([r.seq_rank[0] - r.seq_rank[1] for r in b.itertuples()], float)\n    res = sm.GLM(back, sm.add_constant(d12), family=sm.families.Binomial()).fit()\n    hi1, lo1 = back[d12 > 0], back[d12 < 0]\n    chi, pchi, _, _ = stats.chi2_contingency([[hi1.sum(), len(hi1) - hi1.sum()], [lo1.sum(), len(lo1) - lo1.sum()]])\n    print(f\"{sb}: n = {len(b)}; (a) slope on rank1 - rank2 {res.params[1]:.3f}, p = {res.pvalues[1]:.2g};\"\n          f\" (b) back to option 1 when cue 1 > cue 2 {hi1.mean():.3f} (n={len(hi1)}), when cue 1 < cue 2\"\n          f\" {lo1.mean():.3f} (n={len(lo1)}), chi2 = {chi:.1f}, p = {pchi:.2g}\")\n\n# %% [markdown]\n# RESULT:fig2a-sample-the-favourite\n\n# %% [markdown]\n# ## fig2b-positive-evidence\n#\n# > On option trials, subjects sampled the fewest cues when cues 1 and 2 were highest in value and\n# > the most when they were lowest.\n#\n# The count is `num_pics_viewed250`, as the script's `nPicView12Opt` for Figure 2b; the raw count\n# is shown too.\n\n# %% tags=[\"claim:fig2b-positive-evidence\"]\nfor col in [\"npv250\", \"npv\"]:\n    for sb in [\"F\", \"M\", \"both\"]:\n        b = beh[beh.condition == 3]\n        if sb != \"both\":\n            b = b[b.subject == sb]\n        r1 = np.array([r.seq_rank[0] for r in b.itertuples()])\n        r2 = np.array([r.seq_rank[1] for r in b.itertuples()])\n        n = b[col].values\n        hi = n[(r1 == 2) & (r2 == 2)]\n        lo = n[(r1 == -2) & (r2 == -2)]\n        rho, prho = stats.spearmanr(r1 + r2, n)\n        print(f\"{col} {sb}: (a) mean cues, both ranks +2: {hi.mean():.2f} (n={len(hi)}); both -2: \"\n              f\"{lo.mean():.2f} (n={len(lo)}); (b) Spearman rho {rho:.3f}, p = {prho:.2g}\")\nb = beh[(beh.condition == 3) & (beh.subject == \"M\")]\ntbl = pd.crosstab([r.seq_rank[0] for r in b.itertuples()], [r.seq_rank[1] for r in b.itertuples()],\n                  values=b.npv250, aggfunc=\"mean\")\nprint(\"monkey M, mean npv250 by cue 1 rank (rows) and cue 2 rank (columns):\")\nprint(tbl.round(2))\n\n# %% [markdown]\n# RESULT:fig2b-positive-evidence\n\n# %% [markdown]\n# ## RSA at cue 1 (claims fig4d to fig4h, figs2, figs4, figs11)\n#\n# Fig4_RSA.m and calculate_RSA_matrices.m: per unit the mean spike count 100 < t < 500 ms after\n# cue 1 in each of 20 conditions, z-scored across conditions; Pearson correlation between\n# conditions; OLS of the 400 elements on the seven columns of `pfc7.rsa_design`. T-statistics and\n# the between-region F-statistics are compared with 10,000 permutations of the 20 condition labels.\n# The script's test is one-sided (`1 - mean(t > tp)`), reading (a) of O8; reading (b), two-sided\n# on |T|, is shown too. Reading (a) of O9 (all completed trials) is what calculate_RSA_matrices.m\n# uses; reading (b) keeps trials with 3 or more cues.\n\n# %%\ndef rsa_unitmat(units, min_npv=0, key=\"m20\"):\n    cols = []\n    for u in units:\n        d = U[u]\n        if min_npv:\n            sel = d[\"num_pics_viewed\"] >= min_npv\n            # recompute the condition means on the kept trials from the 1 ms rasters' window counts\n            r = pfc7.rsa_inputs(d[\"Lreg\"][sel, 0].astype(int), d[\"Rreg\"][sel, 0].astype(int),\n                                d[\"P_first\"][sel], RAW1[u][sel], d[\"First_pos\"][sel].astype(int))\n            cols.append(r[key])\n        else:\n            cols.append(d[\"rsa\"][key])\n    return np.column_stack(cols)\n\n# rasters for O9 reading (b) only: reread nothing; the window counts are rebuilt from the GLM bins\nRAW1 = {}\nfor u, d in U.items():\n    # a 0/1 raster is not kept in memory; for reading (b) rebuild an equivalent window count raster:\n    # spikes in 100 < t < 500 equal 400 * mean over that window, which the 10 ms GLM bins tile\n    pass\nDM, TN = pfc7.rsa_design()\nDM_ALT, _ = pfc7.rsa_design(alternative=True)\nFTP = pfc7.rsa_ftest_parts(DM)\nFTP_ALT = pfc7.rsa_ftest_parts(DM_ALT)\nNPERM = 10000\n\ndef rsa_run(mats, dm, ftp, rng, nperm=NPERM):\n    \"\"\"mats: list of three conditions x units matrices (ACC, DLPFC, OFC).\"\"\"\n    Y = np.column_stack([pfc7.rsa_matrix(M).ravel(order=\"F\") for M in mats])\n    C = np.eye(dm.shape[1])\n    _, _, t = pfc7.ols(Y, dm, C)\n    cp = pfc7.cpd(Y, dm)\n    F = pfc7.rsa_fstats(Y.ravel(order=\"F\"), ftp)\n    tp = np.zeros((nperm,) + t.shape)\n    Fp = np.zeros((nperm, len(F)))\n    for p in range(nperm):\n        pp = rng.permutation(20)\n        Yp = np.column_stack([pfc7.rsa_matrix(M[pp]).ravel(order=\"F\") for M in mats])\n        tp[p] = pfc7.ols(Yp, dm, C)[2]\n        Fp[p] = pfc7.rsa_fstats(Yp.ravel(order=\"F\"), ftp)\n    p1 = 1 - (t[None] > tp).mean(0)\n    p2 = (np.abs(tp) >= np.abs(t)[None]).mean(0)\n    pF = 1 - (F[None] > Fp).mean(0)\n    pdiff = {}\n    for i in range(2, 7):\n        for r1 in range(3):\n            for r2 in range(3):\n                if r1 != r2:\n                    pdiff[(i, r1, r2)] = 1 - ((t[i, r1] - t[i, r2]) > (tp[:, i, r1] - tp[:, i, r2])).mean()\n    return dict(Y=Y, t=t, cpd=cp, F=F, p1=p1, p2=p2, pF=pF, pdiff=pdiff)\n\ndef rsa_table(res, names=TN):\n    rows = []\n    for i in range(2, 7):\n        for r in range(3):\n            rows.append(dict(template=names[i], area=NAMES[r + 1], T=res[\"t\"][i, r],\n                             p_one=res[\"p1\"][i, r], p_two=res[\"p2\"][i, r], CPD=100 * res[\"cpd\"][i, r]))\n    tb = pd.DataFrame(rows).pivot(index=\"template\", columns=\"area\")\n    return tb\n\nt_rsa = time.time()\nMATS = {\"a\": [rsa_unitmat(SEL[a]) for a in (1, 2, 3)]}\nprint(\"units entering the RSA:\", {NAMES[a]: int((~np.all(m == 0, 0)).sum()) for a, m in zip((1, 2, 3), MATS[\"a\"])})\nRSA = {\"a\": rsa_run(MATS[\"a\"], DM, FTP, section_rng(\"rsa-a\"))}\nprint(f\"RSA reading (a) with {NPERM} permutations: {time.time() - t_rsa:.0f} s\")\nprint(rsa_table(RSA[\"a\"]).round(4))\nprint(\"between-region F:\", {TN[i]: (round(RSA[\"a\"][\"F\"][i], 2), RSA[\"a\"][\"pF\"][i]) for i in range(2, 7)})\n"
}
```

```
File created successfully at: /tmp/claude/nbsrc.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='pfc7.py'; s=open(p).read()
old='''                              d["P_first"], r1, d["First_pos"].astype(int))
'''
new='''                              d["P_first"], r1, d["First_pos"].astype(int))
        k3 = d["num_pics_viewed"] >= 3   # claims file O9 reading (b)
        d["rsa3"] = rsa_inputs(d["Lreg"][k3, 0].astype(int), d["Rreg"][k3, 0].astype(int),
                               d["P_first"][k3], r1[k3])
'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
p='/tmp/claude/nbsrc.py'; s=open(p).read()
a=s.index('def rsa_unitmat'); b=s.index('DM, TN = pfc7.rsa_design()')
s=s[:a]+'''def rsa_unitmat(units, key="rsa", field="m20"):
    return np.column_stack([U[u][key][field] for u in units])

'''+s[b:]
s=s.replace('''def section_rng(name):
    """One generator per claim section, seeded from its name."""
    return np.random.default_rng(abs(hash(name)) % (2**32) if False else sum(map(ord, name)) * 7919)''','''def section_rng(name):
    """One generator per claim section, seeded from its name (a standard choice)."""
    return np.random.default_rng(zlib.crc32(name.encode()))''')
s=s.replace("import time\n","import time\nimport zlib\n",1)
open(p,'w').write(s)
EOF
grep -n "rsa_unitmat\|zlib" /tmp/claude/nbsrc.py | head
```

```
26:import zlib
43:    return np.random.default_rng(zlib.crc32(name.encode()))
569:def rsa_unitmat(units, key="rsa", field="m20"):
613:MATS = {"a": [rsa_unitmat(SEL[a]) for a in (1, 2, 3)]}
```

**Agent calls Bash**

```bash
cat >> /tmp/claude/nbsrc.py <<'EOF'

# %%
MATS["b"] = [rsa_unitmat(SEL[a], key="rsa3") for a in (1, 2, 3)]
RSA["b"] = rsa_run(MATS["b"], DM, FTP, section_rng("rsa-b"))
print("O9 reading (b), trials with 3 or more cues:")
print(rsa_table(RSA["b"]).round(4))
print("between-region F:", {TN[i]: (round(RSA["b"]["F"][i], 2), RSA["b"]["pF"][i]) for i in range(2, 7)})
fig, ax = plt.subplots(1, 3, figsize=(12, 4))
for k, a in enumerate((3, 2, 1)):
    M = RSA["a"]["Y"][:, a - 1].reshape(20, 20, order="F")
    ax[k].imshow(M, vmin=-0.3, vmax=0.3, cmap="hot")
    ax[k].set_title(f"{NAMES[a]} (values {M[~np.eye(20, dtype=bool)].min():.2f} to "
                    f"{M[~np.eye(20, dtype=bool)].max():.2f} off the diagonal)", fontsize=8)
plt.show()

# %% [markdown]
# A helper to judge the template claims under each reading (O8 sidedness, O9 trials).

# %%
IDX = {n: i for i, n in enumerate(TN)}
def sig(res, tmpl, area, side):
    return (res["p1"] if side == "one" else res["p2"])[IDX[tmpl], area - 1] < 0.05
def cpdv(res, tmpl, area):
    return res["cpd"][IDX[tmpl], area - 1]
def readings():
    for o9 in ("a", "b"):
        for o8 in ("one", "two"):
            yield o9, o8

# %% [markdown]
# ## fig4d-spatial-attention
#
# > At cue 1, DLPFC representational similarity reflects whether the subject is attending left or
# > right; spatial attention is also represented in OFC and ACC.

# %% tags=["claim:fig4d-spatial-attention"]
for o9, o8 in readings():
    r = RSA[o9]
    ok = (sig(r, "spatial attention", 2, o8) and cpdv(r, "spatial attention", 2) > cpdv(r, "spatial attention", 1)
          and cpdv(r, "spatial attention", 2) > cpdv(r, "spatial attention", 3)
          and sig(r, "spatial attention", 3, o8) and sig(r, "spatial attention", 1, o8))
    print(f"O9 ({o9}) O8 {o8}-sided: CPD % ACC {100*cpdv(r,'spatial attention',1):.2f}, DLPFC "
          f"{100*cpdv(r,'spatial attention',2):.2f}, OFC {100*cpdv(r,'spatial attention',3):.2f}; p ACC/DLPFC/OFC "
          f"{[round(float(x), 4) for x in (r['p1'] if o8 == 'one' else r['p2'])[IDX['spatial attention']]]};"
          f" F p = {r['pF'][IDX['spatial attention']]:.4f} -> criterion holds: {ok}")

# %% [markdown]
# RESULT:fig4d-spatial-attention

# %% [markdown]
# ## fig4e-ofc-stimulus-identity
#
# > At cue 1, OFC representational similarity reflects the attended stimulus identity irrespective
# > of its spatial position.

# %% tags=["claim:fig4e-ofc-stimulus-identity"]
def judge_ofc(tmpl):
    for o9, o8 in readings():
        r = RSA[o9]
        ok = sig(r, tmpl, 3, o8) and cpdv(r, tmpl, 3) > cpdv(r, tmpl, 1) and cpdv(r, tmpl, 3) > cpdv(r, tmpl, 2)
        print(f"O9 ({o9}) O8 {o8}-sided: T OFC {r['t'][IDX[tmpl], 2]:.2f}, p "
              f"{(r['p1'] if o8 == 'one' else r['p2'])[IDX[tmpl], 2]:.4f}; CPD % ACC {100*cpdv(r,tmpl,1):.2f}, DLPFC "
              f"{100*cpdv(r,tmpl,2):.2f}, OFC {100*cpdv(r,tmpl,3):.2f}; F p = {r['pF'][IDX[tmpl]]:.4f} -> holds: {ok}")
judge_ofc("stimulus identity")

# %% [markdown]
# RESULT:fig4e-ofc-stimulus-identity

# %% [markdown]
# ## fig4f-ofc-attended-value
#
# > At cue 1, OFC representational similarity is high for cues of similar attended value,
# > consistent with a linear value code.

# %% tags=["claim:fig4f-ofc-attended-value"]
judge_ofc("attended value")

# %% [markdown]
# RESULT:fig4f-ofc-attended-value

# %% [markdown]
# ## fig4g-left-right-value
#
# > At cue 1, ACC and DLPFC representational similarity shows a value code modulated by whether the
# > subject attends the left or right option.

# %% tags=["claim:fig4g-left-right-value"]
def judge_lr(res_by_reading, tmpl="left/right value"):
    out = {}
    for o9, o8 in readings():
        r = res_by_reading[o9]
        ok = (sig(r, tmpl, 1, o8) and sig(r, tmpl, 2, o8) and cpdv(r, tmpl, 1) > cpdv(r, tmpl, 3)
              and cpdv(r, tmpl, 2) > cpdv(r, tmpl, 3))
        pv = (r['p1'] if o8 == 'one' else r['p2'])[IDX[tmpl]]
        print(f"O9 ({o9}) O8 {o8}-sided: T ACC/DLPFC/OFC {np.round(r['t'][IDX[tmpl]], 2)}, p {np.round(pv, 4)};"
              f" CPD % {np.round(100 * r['cpd'][IDX[tmpl]], 2)}; F p = {r['pF'][IDX[tmpl]]:.4f} -> holds: {ok}")
        out[(o9, o8)] = ok
    return out
LR_OK = judge_lr(RSA)

# %% [markdown]
# RESULT:fig4g-left-right-value

# %% [markdown]
# ## fig4h-acc-accept-reject
#
# > At cue 1, ACC representational similarity divides high-valued from low-valued cues, best
# > explained as a categorical (accept/reject) function of value.

# %% tags=["claim:fig4h-acc-accept-reject"]
for o9, o8 in readings():
    r = RSA[o9]
    pv = r['p1'] if o8 == 'one' else r['p2']
    ra = cpdv(r, "accept/reject", 1) > cpdv(r, "attended value", 1)
    rb = sig(r, "accept/reject", 1, o8) and not sig(r, "attended value", 1, o8)
    ok = sig(r, "accept/reject", 1, o8) and cpdv(r, "accept/reject", 1) > cpdv(r, "accept/reject", 2) and (ra or rb)
    print(f"O9 ({o9}) O8 {o8}-sided: accept/reject T ACC/DLPFC/OFC {np.round(r['t'][IDX['accept/reject']], 2)},"
          f" p {np.round(pv[IDX['accept/reject']], 4)}, CPD % {np.round(100 * r['cpd'][IDX['accept/reject']], 2)};"
          f" attended value in ACC T {r['t'][IDX['attended value'], 0]:.2f}, p {pv[IDX['attended value'], 0]:.4f},"
          f" CPD % {100 * cpdv(r, 'attended value', 1):.2f}; (a) {ra}, (b) {rb} -> holds: {ok}")

# %% [markdown]
# RESULT:fig4h-acc-accept-reject

# %% [markdown]
# ## figs2-consistent-across-subjects
#
# > The triple dissociation of RSA matrices at cue 1 is consistent across the two monkeys.
#
# Fig4_RSA.m, with the commented lines `area(isfrank) = nan` / `area(ismiles) = nan` that the
# script names for Supplementary Figure 2: the same RSA on each monkey's units.

# %% tags=["claim:figs2-consistent-across-subjects"]
CHECKS = [("spatial attention", 2), ("stimulus identity", 3), ("attended value", 3),
          ("left/right value", 1), ("left/right value", 2), ("accept/reject", 1)]
for o9 in ("a", "b"):
    hold = {}
    for sb in ["M", "F"]:
        mats = [rsa_unitmat([u for u in SEL[a] if info.loc[u, "subject"] == sb],
                            key="rsa" if o9 == "a" else "rsa3") for a in (1, 2, 3)]
        Y = np.column_stack([pfc7.rsa_matrix(M).ravel(order="F") for M in mats])
        b_, _, t_ = pfc7.ols(Y, DM, np.eye(7))
        vals = {f"{tm} {NAMES[a]}": b_[IDX[tm], a - 1] for tm, a in CHECKS}
        hold[sb] = sum(v > 0 for v in vals.values())
        print(f"O9 ({o9}) monkey {sb}, units {[m.shape[1] for m in mats]}: coefficients",
              {k: round(float(v), 4) for k, v in vals.items()})
    print(f"  positive of 6: {hold}")

# %% [markdown]
# RESULT:figs2-consistent-across-subjects

# %% [markdown]
# ## figs4-dlpfc-top-bottom
#
# > Split by top and bottom cue position (40 conditions), the RSA results replicate, and DLPFC
# > similarity is also modulated by top/bottom position, so DLPFC represents spatial position more
# > than left/right action.
#
# 40 conditions as calculate_RSA_matrices_updown.m (conditions 1-20 with cue 1 on top, 21-40 at
# the bottom; within each, LP, LM, RP, RM). The measure is the criterion's: mean similarity of
# pairs in the same quadrant against pairs on the same side in different rows, off the diagonal.

# %% tags=["claim:figs4-dlpfc-top-bottom"]
side = np.r_[np.zeros(10), np.ones(10), np.zeros(10), np.ones(10)]
row = np.r_[np.zeros(20), np.ones(20)]
same_q = (side[:, None] == side[None]) & (row[:, None] == row[None]) & ~np.eye(40, dtype=bool)
same_side_diff_row = (side[:, None] == side[None]) & (row[:, None] != row[None])
S4 = {}
for a in (1, 2, 3):
    M = pfc7.rsa_matrix(rsa_unitmat(SEL[a], field="m40"))
    S4[a] = M[same_q].mean() - M[same_side_diff_row].mean()
    print(f"{NAMES[a]}: same quadrant {M[same_q].mean():.4f}, same side other row "
          f"{M[same_side_diff_row].mean():.4f}, difference {S4[a]:.4f}; matrix range "
          f"{M[~np.eye(40, dtype=bool)].min():.2f} to {M[~np.eye(40, dtype=bool)].max():.2f}")
# null for the difference: permute the 40 condition labels within each unit set
rng = section_rng("figs4")
null = {a: [] for a in (1, 2, 3)}
for a in (1, 2, 3):
    X = rsa_unitmat(SEL[a], field="m40")
    for p in range(1000):
        M = pfc7.rsa_matrix(X[rng.permutation(40)])
        null[a].append(M[same_q].mean() - M[same_side_diff_row].mean())
    print(f"{NAMES[a]}: permutation p (one-sided, 1000 label permutations, a reference not in the criterion) "
          f"{np.mean(np.array(null[a]) >= S4[a]):.3f}")
print("criterion: DLPFC difference > 0 and larger than ACC and OFC:", S4[2] > 0 and S4[2] > S4[1] and S4[2] > S4[3])

# %% [markdown]
# RESULT:figs4-dlpfc-top-bottom

# %% [markdown]
# ## fig4-t75-latencies
#
# > Spatial attention reached 75% of its peak CPD at about the saccade (24, 72 and 67 ms in ACC,
# > DLPFC, OFC); stimulus identity and attended value in OFC (269, 241 ms) and accept/reject (238
# > ms ACC, 224 ms OFC) followed; left/right value came later (457 ms ACC, 369 ms DLPFC).
#
# Fig4_RSA.m computes the RSA matrix at every 1 ms from 200 ms boxcar-smoothed condition means,
# the CPD of each template over time, and t75 with calculate_t75max.m over the whole epoch (-199
# to 600 ms). Readings of the claims file: step (a) 10 ms, (b) 1 ms; range -100 to 500 ms, with
# -200 to 600 ms (the script's) reported.

# %% tags=["claim:fig4-t75-latencies"]
TIMEIND = np.arange(-199, 601)
def sliding_rsa_cpd(units_by_area, dm):
    Ys = []
    for units in units_by_area:
        S = np.stack([U[u]["rsa"]["s20"] for u in units], axis=1)   # 20 x units x 800
        Yt = np.zeros((400, S.shape[2]))
        for k in range(S.shape[2]):
            Yt[:, k] = pfc7.rsa_matrix(S[:, :, k]).ravel(order="F")
        Ys.append(Yt)
    Yall = np.hstack(Ys)
    c = pfc7.cpd(Yall, dm) * 100
    return Yall, c.reshape(dm.shape[1], 3, -1)   # templates x areas x time
YT, CPDT = sliding_rsa_cpd([SEL[a] for a in (1, 2, 3)], DM)
EXP75 = [("spatial attention", 1, 24), ("spatial attention", 2, 72), ("spatial attention", 3, 67),
         ("stimulus identity", 3, 269), ("attended value", 3, 241), ("accept/reject", 1, 238),
         ("accept/reject", 3, 224), ("left/right value", 1, 457), ("left/right value", 2, 369)]
TOL75 = [10, 10, 10, 26.9, 24.1, 23.8, 22.4, 45.7, 36.9]
rows = []
for step in (10, 1):
    for lo, hi in ((-100, 500), (-200, 600)):
        sel = (TIMEIND >= lo) & (TIMEIND <= hi)
        idx = np.flatnonzero(sel)[::step]
        r = dict(step=step, range=f"{lo} to {hi}")
        nwithin = 0
        for (tm, a, e), tol in zip(EXP75, TOL75):
            v, tmax, mx = pfc7.t75(CPDT[IDX[tm], a - 1, idx], TIMEIND[idx])
            r[f"{tm} {NAMES[a]}"] = v
            nwithin += abs(v - e) <= tol
        r["within tolerance"] = nwithin
        rows.append(r)
T75 = pd.DataFrame(rows).set_index(["step", "range"])
print(T75.T)
print("expected:", {f"{tm} {NAMES[a]}": e for tm, a, e in EXP75})
peak = {f"{tm} {NAMES[a]}": round(float(CPDT[IDX[tm], a - 1].max()), 2) for tm, a, e in EXP75}
print("peak CPD (%) of each curve:", peak)
fig, ax = plt.subplots(1, 3, figsize=(13, 3.5))
for a in (1, 2, 3):
    for i in range(2, 7):
        ax[a - 1].plot(TIMEIND, CPDT[i, a - 1], label=TN[i])
    ax[a - 1].set_title(NAMES[a]); ax[a - 1].set_xlabel("ms after cue 1")
ax[0].legend(fontsize=7); ax[0].set_ylabel("CPD (%)")
plt.show()
print("CPD range plotted:", round(float(CPDT[2:].min()), 2), "to", round(float(CPDT[2:].max()), 2), "%")

# %% [markdown]
# RESULT:fig4-t75-latencies

# %% [markdown]
# ## figs5c-latency-order
#
# > Spatial attention is encoded significantly earlier than stimulus identity, attended value and
# > accept/reject, and left/right value (in ACC and DLPFC) significantly later than the other
# > variables.
#
# Fig4_RSA.m: 100 simulations adding permuted residuals of the sliding template regression to its
# fitted values; the script draws one permutation of the 400 elements and applies it at every
# time point (reading (b)). Reading (a) draws one per time point. t75 over -199 to 600 ms at 1 ms,
# as the script. The variables compared in each region are those whose template is significant at
# 100-500 ms (one-sided permutation p < 0.05, O9 reading (a)).

# %% tags=["claim:figs5c-latency-order"]
rng = section_rng("figs5c")
Xb = DM @ np.linalg.pinv(DM) @ YT
RX = YT - Xb
sims = {"a": [], "b": []}
for rd in ("a", "b"):
    for p in range(100):
        if rd == "b":
            new = Xb + RX[rng.permutation(400)]
        else:
            perm = np.argsort(rng.random(RX.shape), axis=0)
            new = Xb + np.take_along_axis(RX, perm, axis=0)
        c = (pfc7.cpd(new, DM) * 100).reshape(7, 3, -1)
        sims[rd].append({(i, a): pfc7.t75(c[i, a - 1], TIMEIND)[0] for i in range(2, 7) for a in (1, 2, 3)})
for rd in ("a", "b"):
    df = pd.DataFrame(sims[rd])
    print(f"--- reading ({rd}): t75 range (min to max over 100 simulations), ms")
    ok_all = True
    for a in (1, 2, 3):
        keep_v = [i for i in (2, 3, 4) if RSA["a"]["p1"][i, a - 1] < 0.05]
        if a in (1, 2) and RSA["a"]["p1"][IDX["left/right value"], a - 1] < 0.05:
            keep_v.append(IDX["left/right value"])
        rng_ = {TN[i]: (df[(i, a)].min(), df[(i, a)].max()) for i in [IDX["spatial attention"]] + keep_v}
        print(NAMES[a], {k: (float(v[0]), float(v[1])) for k, v in rng_.items()})
        sp = rng_["spatial attention"]
        others = [v for k, v in rng_.items() if k not in ("spatial attention", "left/right value")]
        early = all(sp[1] < o[0] for o in others)
        late = True
        if "left/right value" in rng_:
            lr = rng_["left/right value"]
            late = all(lr[0] > v[1] for k, v in rng_.items() if k != "left/right value")
        elif a in (1, 2):
            late = False
        print(f"   spatial attention below all others: {early}; left/right value above all others: {late}")
        ok_all &= early and late
    print(f"reading ({rd}) criterion holds in every region: {ok_all}")

# %% [markdown]
# RESULT:figs5c-latency-order
EOF
date -u
```

```
Sat Nov 14 18:57:12 UTC 2026
```

**Agent calls Bash**

```bash
cat >> /tmp/claude/nbsrc.py <<'EOF'

# %% [markdown]
# ## GLM claims (Figures 5 to 7)
#
# T-statistics of the shared GLM for every unit (fitted above). Bin indices: the bin centred at
# 250 ms after a cue is index 35, at 300 ms index 40; response locked, the bin centred at -200 ms is
# index 30 (the scripts' `ttR(30, ...)`, 1-based, is the bin centred at -210 ms; both are shown
# where they matter). Contrast numbers are the GLM script's (19 = EV1 + EV5, 20 = EV2 + EV6).

# %%
B250, B300 = int(np.flatnonzero(pfc7.TIMEBINS == 250)[0]), int(np.flatnonzero(pfc7.TIMEBINS == 300)[0])
def tst(units, ep, con, b, kind="t"):
    """T-statistic (or `kind`='b' the contrast estimate) of contrast number `con` at bin `b`."""
    return np.array([G[u][kind + ep][con - 1, b] for u in units])
def tmean(units, ep, evs, b):
    """Reading (a): the mean of the EVs' T-statistics."""
    return np.mean([tst(units, ep, e, b) for e in evs], axis=0)
def pear(x, y):
    ok = np.isfinite(x) & np.isfinite(y)
    r, p = stats.pearsonr(x[ok], y[ok])
    return r, p, int(ok.sum())

# %% [markdown]
# ## fig5a-ofc-value-cpd
#
# > Value encoding by OFC neurons peaked about 300 ms after each cue was revealed and stayed above
# > baseline as further cues were attended.
#
# Mean CPD across OFC neurons (Fig5_OFCcrosscorrelation.m plots `cpd1(area==3, 1, :)` and so on,
# the option-trial EVs). Readings (a) mean of the CPDs of the option and attribute EVs of a cue; (b)
# each trial type separately.

# %% tags=["claim:fig5a-ofc-value-cpd"]
ofc = SEL5[3]
CP = {ep: np.nanmean([G[u]["cpd" + ep] for u in ofc], axis=0) * 100 for ep in ("X1", "X2", "X3")}
EVSETS = {"a": {1: [0, 4], 2: [1, 5], 3: [2, 6, 8]}, "b-option": {1: [0], 2: [1], 3: [2]},
          "b-attribute": {1: [4], 2: [5], 3: [6, 8]}}
post = pfc7.TIMEBINS >= 0
for rd, sets in EVSETS.items():
    curves = {(c, ep): CP[ep][sets[c]].mean(0) for c in (1, 2, 3) for ep in ("X1", "X2", "X3")}
    peaks = {c: int(pfc7.TIMEBINS[post][np.argmax(curves[(c, f"X{c}")][post])]) for c in (1, 2, 3)}
    for bl in ("i", "ii"):
        base_v = {c: (curves[(1, "X1")][0] if bl == "i" else curves[(c, "X1")][pfc7.TIMEBINS <= 0].mean())
                  for c in (1, 2)}
        above_all = (bool((curves[(1, "X2")] > base_v[1]).all() and (curves[(1, "X3")] > base_v[1]).all()
                          and (curves[(2, "X3")] > base_v[2]).all()))
        means = {f"cue{c} in X{e}": round(float(curves[(c, f'X{e}')].mean() - base_v[c]), 3)
                 for c, e in ((1, 2), (1, 3), (2, 3))}
        within = all(abs(peaks[c] - 300) <= 30 for c in (1, 2, 3))
        print(f"reading ({rd}), baseline ({bl}): peaks after own onset {peaks} ms; baselines "
              f"{ {c: round(float(v), 3) for c, v in base_v.items()} } %; above baseline at every later bin: "
              f"{above_all}; epoch mean minus baseline {means} -> holds: {within and above_all}")
fig, ax = plt.subplots(1, 3, figsize=(12, 3), sharey=True)
for k, ep in enumerate(("X1", "X2", "X3")):
    for c in (1, 2, 3):
        ax[k].plot(pfc7.TIMEBINS, CP[ep][EVSETS["a"][c]].mean(0), label=f"cue {c} value")
    ax[k].set_title(f"locked to cue {k + 1}"); ax[k].set_xlabel("ms")
ax[0].legend(); ax[0].set_ylabel("mean CPD (%), OFC")
plt.show()
print("plotted range:", round(min(CP[ep][[0, 1, 2, 4, 5, 6, 8]].min() for ep in CP), 3), "to",
      round(max(CP[ep][[0, 1, 2, 4, 5, 6, 8]].max() for ep in CP), 3))

# %% [markdown]
# RESULT:fig5a-ofc-value-cpd

# %% [markdown]
# ## fig5b-stable-attended-value-subspace
#
# > In OFC, T-statistics for cue 1 value at cue 1 correlate positively across neurons with those
# > for cue 2 value at cue 2, a stable subspace for the currently attended value.
#
# Fig5_OFCcrosscorrelation.m correlates contrast 19 at cue 1 with contrast 20 at cue 2 (reading
# (b)); reading (a) averages the T-statistics.

# %% tags=["claim:fig5b-stable-attended-value-subspace"]
def c5b(units):
    ra = pear(tmean(units, "X1", [1, 5], B250), tmean(units, "X2", [2, 6], B250))
    rb = pear(tst(units, "X1", 19, B250), tst(units, "X2", 20, B250))
    return ra, rb
for a in (3, 2, 1):
    ra, rb = c5b(SEL5[a])
    print(f"{NAMES[a]}: (a) r = {ra[0]:.3f}, p = {ra[1]:.2g}, n = {ra[2]};  (b) r = {rb[0]:.3f}, p = {rb[1]:.2g}")
for sb in ("M", "F"):
    ra, rb = c5b([u for u in SEL5[3] if info.loc[u, "subject"] == sb])
    print(f"OFC monkey {sb}: (b) r = {rb[0]:.3f}, p = {rb[1]:.2g}, n = {rb[2]}")

# %% [markdown]
# RESULT:fig5b-stable-attended-value-subspace

# %% [markdown]
# ## fig5c-attribute-cue2-vs-cue1
#
# > In OFC, at cue 2 of attribute trials, the attended cue 2 value subspace correlates negatively
# > with the stored cue 1 value subspace (the other option).

# %% tags=["claim:fig5c-attribute-cue2-vs-cue1"]
CORR5 = {}
for a in (1, 2, 3):
    u = SEL5[a]
    CORR5[a] = {"6v5@2": pear(tst(u, "X2", 6, B250), tst(u, "X2", 5, B250)),
                "3v1@3": pear(tst(u, "X3", 3, B250), tst(u, "X3", 1, B250)),
                "3v2@3": pear(tst(u, "X3", 3, B250), tst(u, "X3", 2, B250)),
                "1v2@3": pear(tst(u, "X3", 1, B250), tst(u, "X3", 2, B250)),
                "1v2@2": pear(tst(u, "X2", 1, B250), tst(u, "X2", 2, B250))}
print(pd.DataFrame({NAMES[a]: {k: f"r={v[0]:.3f} p={v[1]:.2g} n={v[2]}" for k, v in CORR5[a].items()}
                    for a in (3, 2, 1)}))
for sb in ("M", "F"):
    u = [x for x in SEL5[3] if info.loc[x, "subject"] == sb]
    print(f"OFC monkey {sb}: EV6 vs EV5 at cue 2 r = {pear(tst(u, 'X2', 6, B250), tst(u, 'X2', 5, B250))[0]:.3f}")

# %% [markdown]
# RESULT:fig5c-attribute-cue2-vs-cue1

# %% [markdown]
# ## fig5de-option-cue3-vs-stored
#
# > In OFC, at cue 3 of option trials, the attended cue 3 value subspace correlates negatively with
# > both the stored cue 1 and the stored cue 2 value subspaces.

# %% tags=["claim:fig5de-option-cue3-vs-stored"]
for k in ("3v1@3", "3v2@3"):
    r, p, n = CORR5[3][k]
    print(f"OFC EV{k[0]} vs EV{k[2]} at cue 3: r = {r:.3f}, p = {p:.2g}, n = {n}; negative with p < 0.05: {r < 0 and p < 0.05}")

# %% [markdown]
# RESULT:fig5de-option-cue3-vs-stored

# %% [markdown]
# ## fig5f-option-stored-combined
#
# > In OFC, at cue 3 of option trials, the stored cue 1 and stored cue 2 value subspaces correlate
# > positively, so the two previously attended cues are combined.

# %% tags=["claim:fig5f-option-stored-combined"]
for k in ("1v2@3", "1v2@2"):
    r, p, n = CORR5[3][k]
    print(f"OFC EV1 vs EV2 at cue {k[-1]}: r = {r:.3f}, p = {p:.2g}, n = {n}")

# %% [markdown]
# RESULT:fig5f-option-stored-combined

# %% [markdown]
# ## fig5gj-cross-correlation-dynamics
#
# > Cross-correlating the OFC value subspaces across time shows the same population subspace
# > shifting its value encoding from positive to negative as the subject saccades around the
# > screen.
#
# Fig5_OFCcrosscorrelation.m and cross_corr_tstats.m: for each of four EV pairs (EV6/EV5, EV2/EV1,
# EV3/EV1, EV3/EV2) the correlation across OFC neurons of the T-statistics at every pair of bins,
# for every pair of cue epochs (rows: the first EV's epoch); clusters of |r| > 0.2; a cluster is
# significant when larger than the 99.9th percentile of the largest cluster in 1000 permutations of
# neurons of the second EV.

# %% tags=["claim:fig5gj-cross-correlation-dynamics"]
rng = section_rng("fig5gj")
def tmat(units, ep, ev):
    return np.stack([G[u]["t" + ep][ev - 1] for u in units])   # neurons x bins
def ccmat(A, B):
    A = (A - A.mean(0)) / A.std(0); B = (B - B.mean(0)) / B.std(0)
    return A.T @ B / A.shape[0]
def cluster_test(A, B, thr=0.2, nperm=1000):
    cm = ccmat(A, B)
    lab, n = pfc7.clusters(np.abs(cm) > thr)
    sizes = np.bincount(lab.ravel())[1:]
    null = np.zeros(nperm)
    for p in range(nperm):
        cp = ccmat(A, B[rng.permutation(B.shape[0])])
        l2, n2 = pfc7.clusters(np.abs(cp) > thr)
        null[p] = np.bincount(l2.ravel())[1:].max() if n2 else 0
    crit = np.percentile(null, 99.9)
    return cm, lab, sizes, crit
units = SEL5[3]
PAIRS = [(6, 5, "X2", "X2"), (2, 1, "X3", "X3"), (3, 1, "X3", "X3"), (3, 2, "X3", "X3")]
SIGN = {(6, 5): -1, (2, 1): 1, (3, 1): -1, (3, 2): -1}
GJ = {}
for e1, e2, ep1, ep2 in PAIRS:
    cm, lab, sizes, crit = cluster_test(tmat(units, ep1, e1), tmat(units, ep2, e2))
    l = lab[B250, B250]
    sgn = np.sign(cm[B250, B250])
    sig_ = l > 0 and sizes[l - 1] > crit
    GJ[(e1, e2)] = sig_ and sgn == SIGN[(e1, e2)]
    print(f"EV{e1} ({ep1}) x EV{e2} ({ep2}): r at (250, 250) = {cm[B250, B250]:.3f}; cluster there of "
          f"{sizes[l - 1] if l else 0} bins, threshold {crit:.0f}; significant with the expected sign: {GJ[(e1, e2)]}")
cm, lab, sizes, crit = cluster_test(tmat(units, "X2", 6), tmat(units, "X1", 5))
l = lab[B250, B250]
pos_early = l > 0 and sizes[l - 1] > crit and cm[B250, B250] > 0
print(f"EV6 (cue 2) x EV5 (cue 1): r at (250, 250) = {cm[B250, B250]:.3f}; cluster {sizes[l - 1] if l else 0} bins, "
      f"threshold {crit:.0f}; significant positive: {pos_early}")
print("criterion holds:", all(GJ.values()) and pos_early)
fig, ax = plt.subplots(1, 4, figsize=(14, 3.2))
for k, (e1, e2, ep1, ep2) in enumerate(PAIRS):
    m = ccmat(tmat(units, ep1, e1), tmat(units, ep2, e2))
    ax[k].imshow(m, vmin=-0.3, vmax=0.3, cmap="RdBu_r", origin="lower", extent=[-100, 500, -100, 500])
    ax[k].set_title(f"EV{e1} x EV{e2}, {ep1} (range {m.min():.2f} to {m.max():.2f})", fontsize=8)
plt.show()

# %% [markdown]
# RESULT:fig5gj-cross-correlation-dynamics

# %% [markdown]
# ## fig5k-ofc-comparison-unique
#
# > The value comparison correlations of Figure 5c-e are stronger in OFC than in DLPFC (p = 0.040,
# > 0.067, 0.011) and than in ACC (p = 0.003, 0.0003, 0.00013), by Fisher r-to-Z tests.
#
# Fig5_OFCcrosscorrelation.m tests two-sided (reading (a) of O1), with n the region's units.

# %% tags=["claim:fig5k-ofc-comparison-unique"]
rows = []
for k in ("6v5@2", "3v1@3", "3v2@3"):
    for other in (2, 1):
        r_o, n_o = CORR5[3][k][0], len(SEL5[3])
        r_x, n_x = CORR5[other][k][0], len(SEL5[other])
        z, p2 = pfc7.fisher_z(r_o, n_o, r_x, n_x)
        rows.append(dict(corr=k, versus=NAMES[other], r_OFC=r_o, r_other=r_x, z=z, p_two=p2,
                         p_one=stats.norm.cdf(z), ofc_more_negative=r_o < r_x))
f5k = pd.DataFrame(rows)
print(f5k.round(4))
print("paper: p = 0.040, 0.067, 0.011 (DLPFC); 0.003, 0.0003, 0.00013 (ACC)")
for col in ("p_two", "p_one"):
    print(f"{col}: all six OFC more negative {bool(f5k.ofc_more_negative.all())}, p < 0.05 in {int((f5k[col] < 0.05).sum())} of 6")

# %% [markdown]
# RESULT:fig5k-ofc-comparison-unique

# %% [markdown]
# ## figs67-no-comparison-acc-dlpfc
#
# > ACC and DLPFC carry the currently attended value subspace (and stored subspaces) but show no
# > negative correlation between attended and stored value subspaces.

# %% tags=["claim:figs67-no-comparison-acc-dlpfc"]
for a in (1, 2):
    ra, rb = c5b(SEL5[a])
    f = CORR5[a]["1v2@3"]
    pres = (rb[0] > 0 and rb[1] < 0.05) and (f[0] > 0 and f[1] < 0.05)
    pres_a = (ra[0] > 0 and ra[1] < 0.05) and (f[0] > 0 and f[1] < 0.05)
    neg = [k for k in ("6v5@2", "3v1@3", "3v2@3") if CORR5[a][k][0] < 0 and CORR5[a][k][1] < 0.05]
    print(f"{NAMES[a]}: fig5b r = {rb[0]:.3f} (p = {rb[1]:.2g}; reading (a) r = {ra[0]:.3f}, p = {ra[1]:.2g}),"
          f" fig5f r = {f[0]:.3f} (p = {f[1]:.2g}); presence {pres} (reading (a) {pres_a});"
          f" attended-against-stored r = {[round(CORR5[a][k][0], 3) for k in ('6v5@2', '3v1@3', '3v2@3')]},"
          f" p = {[float('%.2g' % CORR5[a][k][1]) for k in ('6v5@2', '3v1@3', '3v2@3')]}; negative with p < 0.05: {neg}")

# %% [markdown]
# RESULT:figs67-no-comparison-acc-dlpfc
EOF
date -u
```

```
Sat Nov 14 18:58:03 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='pfc7.py'; s=open(p).read()
old='''        out["t" + ep] = ols(Y, Xk, C)[2]
        out["b" + ep] = ols(Y, Xk, C)[0]
        if halves:
            for name, sel in (("odd", odd[keep]), ("even", ~odd[keep])):
                out[f"t{ep}_{name}"] = ols(Y[sel], Xk[sel], C)[2]'''
new='''        cope, _, t = ols(Y, Xk, C)
        out["t" + ep], out["b" + ep] = t, cope
        if halves:
            for name, sel in (("odd", odd[keep]), ("even", ~odd[keep])):
                cope, _, t = ols(Y[sel], Xk[sel], C)
                out[f"t{ep}_{name}"], out[f"b{ep}_{name}"] = t, cope'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
cat >> /tmp/claude/nbsrc.py <<'EOF'

# %% [markdown]
# ## fig6a-acc-belief-subspace
#
# > In ACC the T-statistics of the four belief confirmation regressors (cues 2 and 3, option and
# > attribute trials) correlate positively with each other and with cue 1 value, a stable belief
# > confirmation code not present in OFC or DLPFC.
#
# Fig6_ACCmultiplesignals_R3_version.m: contrast 19 at cue 1 and EVs 13 and 14 at cue 2, 15 and
# 16 at cue 3, all at 300 ms, correlated across neurons in each region (units: SEL, the script's
# selection). Readings of the claims file: (a) T-statistics, (b) OLS coefficients; cue 1 value as
# the mean of the EV1 and EV5 T-statistics or as contrast 19.

# %% tags=["claim:fig6a-acc-belief-subspace"]
LAB6 = ["cue1 value", "EV13", "EV14", "EV15", "EV16"]
def belief_mat(units, kind, cue1):
    if kind == "t" and cue1 == "mean":
        c1 = tmean(units, "X1", [1, 5], B300)
    else:
        c1 = tst(units, "X1", 19, B300, kind)
    return np.column_stack([c1, tst(units, "X2", 13, B300, kind), tst(units, "X2", 14, B300, kind),
                            tst(units, "X3", 15, B300, kind), tst(units, "X3", 16, B300, kind)])
R6 = {}
for kind in ("t", "b"):
    for cue1 in ("contrast", "mean"):
        if kind == "b" and cue1 == "mean":
            continue
        for a in (1, 2, 3):
            M = belief_mat(SEL[a], kind, cue1)
            M = M[np.isfinite(M).all(1)]
            r = np.corrcoef(M.T)
            p = np.ones_like(r)
            for i in range(5):
                for j in range(5):
                    if i != j:
                        p[i, j] = stats.pearsonr(M[:, i], M[:, j])[1]
            iu = np.triu_indices(5, 1)
            R6[(kind, cue1, a)] = dict(r=r, p=p, n=len(M))
            npos = int(((r[iu] > 0) & (p[iu] < 0.05)).sum())
            print(f"{'T-statistics' if kind == 't' else 'coefficients'}, cue 1 as {cue1}, {NAMES[a]} (n = {len(M)}):"
                  f" r = {np.round(r[iu], 3)}, positive with p < 0.05: {npos} of 10")
    print()

# %% [markdown]
# RESULT:fig6a-acc-belief-subspace

# %% [markdown]
# ## fig6b-acc-belief-stronger
#
# > Virtually all belief confirmation correlations are stronger in ACC than in OFC and DLPFC, and
# > most of the individual comparisons are significant by Fisher r-to-Z.

# %% tags=["claim:fig6b-acc-belief-stronger"]
iu = np.triu_indices(5, 1)
for key in [("t", "contrast"), ("t", "mean"), ("b", "contrast")]:
    rA = R6[key + (1,)]
    for side in ("two", "one"):
        larger = 0; nsig = 0
        for other in (2, 3):
            rO = R6[key + (other,)]
            z, p2 = pfc7.fisher_z(rA["r"][iu], rA["n"], rO["r"][iu], rO["n"], two_sided=(side == "two"))
            larger += int((rA["r"][iu] > rO["r"][iu]).sum())
            nsig += int((p2 < 0.05).sum()) if side == "two" else int((p2 < 0.05).sum())
        print(f"{key}, {side}-sided: ACC larger in {larger} of 20, p < 0.05 in {nsig} of 20")

# %% [markdown]
# RESULT:fig6b-acc-belief-stronger

# %% [markdown]
# ## Projections onto the ACC subspaces (fig6c, fig6d, fig6e)
#
# Fig6_ACCmultiplesignals_R3_version.m and InfoGathering_Neurons_Ramp_to_choice.m. Weights per ACC
# unit from the GLM on one half of trials: belief confirmation, the mean of the T-statistics of
# EVs 13 to 16 at 300 ms after their cues; action, the mean of EVs 17 and 18 at the response bin the
# scripts index as 30 (centred 210 ms before the response); the scripts' design is [demeaned belief,
# demeaned action, constant, mean of EVs 11 and 12 at that bin], and the projected data are each
# unit's mean firing in five reaction-time bins (all trials of the other half, including those with
# 2 cues), z-scored by the session mean and SD, 200 ms boxcar every 10 ms; baseline the projection
# at cue 1 onset +/- 50 ms of the same bin (and choice). The scripts' RT bins are fixed: below
# 1200, 1200-1400, 1400-1600, 1600-1800 and from 1800 ms after cue 1 onset. The claims file's
# readings: O4 (a) odd/even, (b) 100 random halves; O5 (a) quintiles per session, (b) quintiles per
# monkey, and the scripts' fixed bins; O6 (a) Hz, (b) z-scored; O7 (a) mean of T-statistics, (b)
# T-statistic of the mean coefficient.

# %%
acc = SEL[1]
RB = 29   # response bin of the scripts (1-based 30)
def weights_from(tg, kind):
    """tg: dict of epoch -> (cope, t) arrays (contrasts x bins) from one half."""
    def comb(items):
        if kind == "a":
            return np.mean([tg[ep][1][ev - 1, b] for ep, ev, b in items])
        cs = np.array([tg[ep][0][ev - 1, b] for ep, ev, b in items])
        vs = np.array([(tg[ep][0][ev - 1, b] / tg[ep][1][ev - 1, b]) ** 2 for ep, ev, b in items])
        return cs.mean() / np.sqrt(vs.mean() / len(items))
    bel = comb([("X3", 15, B300), ("X3", 16, B300), ("X2", 14, B300), ("X2", 13, B300)])
    lr = comb([("XR", 17, RB), ("XR", 18, RB)])
    o, a_ = tg["XR"][1][10, RB], tg["XR"][1][11, RB]
    return np.array([bel, lr, o, a_])
def half_fit(d, mask):
    """GLM on the trials of `mask` (and 3 or more cues), only the bins the weights use."""
    X = pfc7.glm_design(d)
    k = mask & (d["num_pics_viewed"] >= 3)
    C = pfc7.glm_contrasts()[:18]
    out = {}
    for ep, b in (("X2", B300), ("X3", B300), ("XR", RB)):
        cope, _, t = pfc7.ols(d[ep][k][:, [b]].astype(float), X[k], C)
        full_c = np.full((18, 61), np.nan); full_t = np.full((18, 61), np.nan)
        full_c[:, b], full_t[:, b] = cope[:, 0], t[:, 0]
        out[ep] = (full_c, full_t)
    return out
# RT bins
rt_all = {u: U[u]["Response_time"] - U[u]["Cue1_ON"] for u in acc}
sess_rt = {}
for u in acc:
    sess_rt.setdefault((U[u]["sb"], U[u]["snum"]), rt_all[u])
mon_rt = {sb: np.concatenate([v for (s, _), v in sess_rt.items() if s == sb]) for sb in ("M", "F")}
def rt_labels(u, rd):
    rt = rt_all[u]
    if rd == "script":
        edges = [1200, 1400, 1600, 1800]
    elif rd == "a":
        edges = np.quantile(sess_rt[(U[u]["sb"], U[u]["snum"])], [0.2, 0.4, 0.6, 0.8])
    else:
        edges = np.quantile(mon_rt[U[u]["sb"]], [0.2, 0.4, 0.6, 0.8])
    return np.searchsorted(edges, rt, side="right")
LAB = {rd: {u: rt_labels(u, rd) for u in acc} for rd in ("script", "a", "b")}
print("trials per RT bin, pooled over ACC units:",
      {rd: np.bincount(np.concatenate(list(v.values())), minlength=5).tolist() for rd, v in LAB.items()})
def averages(u, mask, labels, hz):
    """Mean cue-locked and response-locked activity per RT bin (5) and per bin x choice (10)."""
    d = U[u]
    L1, LR = d["L1"].astype(float), d["LR"].astype(float)
    if hz:
        L1 = L1 * d["sdev"] + d["men"]; LR = LR * d["sdev"] + d["men"]
    left = d["Left_choice"] == 1
    W5 = np.zeros((len(mask), 5)); W10 = np.zeros((len(mask), 10))
    for k in range(5):
        s = mask & (labels == k)
        if s.any():
            W5[s, k] = 1 / s.sum()
        for c, cs in enumerate((left, ~left)):
            s2 = s & cs
            if s2.any():
                W10[s2, 2 * k + c] = 1 / s2.sum()
    W5[:, W5.sum(0) == 0] = np.nan; W10[:, W10.sum(0) == 0] = np.nan
    sgn = np.where(left, 1.0, -1.0)
    Wsg = np.zeros((len(mask), 5))
    for k in range(5):
        s = mask & (labels == k)
        if s.any():
            Wsg[s, k] = sgn[s] / s.sum()
    return dict(c5=W5.T @ L1, r10=W10.T @ LR, c10=W10.T @ L1, rsg=Wsg.T @ LR, csg=Wsg.T @ L1)
def project(W, D, design):
    """OLS of neurons x columns data on the neurons x k design; NaN neurons dropped."""
    ok = np.isfinite(D).all(1) & np.isfinite(W).all(1)
    if design == "script":
        dm = np.column_stack([W[ok, 0] - W[ok, 0].mean(), W[ok, 1] - W[ok, 1].mean(), np.ones(ok.sum()),
                              (W[ok, 2] + W[ok, 3]) / 2])
    else:
        dm = np.column_stack([W[ok, 0] - W[ok, 0].mean(), W[ok, 1] - W[ok, 1].mean(), np.ones(ok.sum())])
    return np.linalg.pinv(dm) @ D[ok], int(ok.sum())
CUE_T, RESP_T = pfc7.CUE1_LONG, pfc7.RESP_LONG
BASE_W = (CUE_T >= -50) & (CUE_T <= 50)
def run_projection(splits, rd5, hz, o7, design="script"):
    """splits: list of (weight mask, data mask) per unit. Returns per-split projections."""
    res = []
    for wmask, dmask in splits:
        W = np.array([weights_from(half_fit(U[u], wmask[u]) if wmask[u] is not None else HALF[(u, dmask[u][1])], o7)
                      for u in acc]) if False else np.array([weights_from(wmask[u], o7) for u in acc])
        A = [averages(u, dmask[u], LAB[rd5][u], hz) for u in acc]
        out = {}
        for key in ("c5", "r10", "c10", "rsg", "csg"):
            D = np.stack([a[key].ravel() for a in A])
            coef, n = project(W, D, design)
            out[key] = coef.reshape(coef.shape[0], A[0][key].shape[0], -1)
            out["n_" + key] = n
        res.append(out)
    return {k: np.nanmean([r[k] for r in res], axis=0) for k in res[0]}
EOF
date -u
```

```
Sat Nov 14 18:59:11 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude/nbsrc.py'; s=open(p).read()
a=s.index('def half_fit(d, mask):')
s=s[:a]+'''def half_fit(d, mask):
    """GLM on the trials of `mask` with 3 or more cues, at the bins the weights use only."""
    X = pfc7.glm_design(d)
    k = mask & (d["num_pics_viewed"] >= 3)
    P = np.linalg.pinv(X[k])
    dof = k.sum() - np.linalg.matrix_rank(X[k])
    pre = np.diag(P @ P.T)
    out = {}
    for ep, b in (("X2", B300), ("X3", B300), ("XR", RB)):
        y = d[ep][k][:, b].astype(float)
        pe = P @ y
        sig2 = ((y - X[k] @ pe) ** 2).sum() / dof
        cope = np.full((18, 61), np.nan); t = np.full((18, 61), np.nan)
        cope[:, b] = pe
        with np.errstate(divide="ignore", invalid="ignore"):
            t[:, b] = pe / np.sqrt(pre * sig2)
        out[ep] = (cope, t)
    return out
# RT bins
rt_all = {u: U[u]["Response_time"] - U[u]["Cue1_ON"] for u in acc}
sess_rt = {}
for u in acc:
    sess_rt.setdefault((U[u]["sb"], U[u]["snum"]), rt_all[u])
mon_rt = {sb: np.concatenate([v for (s_, _), v in sess_rt.items() if s_ == sb]) for sb in ("M", "F")}
def rt_labels(u, rd):
    rt = rt_all[u]
    if rd == "script":
        edges = [1200, 1400, 1600, 1800]
    elif rd == "a":
        edges = np.quantile(sess_rt[(U[u]["sb"], U[u]["snum"])], [0.2, 0.4, 0.6, 0.8])
    else:
        edges = np.quantile(mon_rt[U[u]["sb"]], [0.2, 0.4, 0.6, 0.8])
    return np.searchsorted(edges, rt, side="right")
O5S = ("script", "a", "b")
LAB = {rd: {u: rt_labels(u, rd) for u in acc} for rd in O5S}
print("trials per RT bin, pooled over ACC units:",
      {rd: np.bincount(np.concatenate(list(v.values())), minlength=5).tolist() for rd, v in LAB.items()})
def averages(u, mask, labels):
    """Mean z-scored activity per RT bin: cue locked (c5), and per bin and choice, cue and response
    locked (c10, r10: left, right), and the choice-signed mean (csg, rsg; right trials times -1).
    Also the mean sign per bin (for converting the signed mean to Hz)."""
    d = U[u]
    left = d["Left_choice"] == 1
    sgn = np.where(left, 1.0, -1.0)
    W5 = np.full((len(mask), 5), 0.0); W10 = np.zeros((len(mask), 10)); Wsg = np.zeros((len(mask), 5))
    msg = np.full(5, np.nan)
    for k in range(5):
        s_ = mask & (labels == k)
        if s_.any():
            W5[s_, k] = 1 / s_.sum(); Wsg[s_, k] = sgn[s_] / s_.sum(); msg[k] = sgn[s_].mean()
        else:
            W5[:, k] = np.nan; Wsg[:, k] = np.nan
        for c, cs in enumerate((left, ~left)):
            s2 = s_ & cs
            if s2.any():
                W10[s2, 2 * k + c] = 1 / s2.sum()
            else:
                W10[:, 2 * k + c] = np.nan
    L1, LR = d["L1"], d["LR"]
    return dict(c5=W5.T @ L1, c10=W10.T @ L1, r10=W10.T @ LR, csg=Wsg.T @ L1, rsg=Wsg.T @ LR, msg=msg)
def to_hz(A, u):
    d = U[u]
    out = {k: A[k] * d["sdev"] + d["men"] for k in ("c5", "c10", "r10")}
    for k in ("csg", "rsg"):
        out[k] = A[k] * d["sdev"] + d["men"] * A["msg"][:, None]
    return out
def project(W, D, design="script"):
    """OLS of the neurons x columns data on the design built from the neurons x 4 weights."""
    ok = np.isfinite(D).all(1) & np.isfinite(W).all(1)
    cols = [W[ok, 0] - W[ok, 0].mean(), W[ok, 1] - W[ok, 1].mean(), np.ones(ok.sum())]
    if design == "script":
        cols.append((W[ok, 2] + W[ok, 3]) / 2)
    return np.linalg.pinv(np.column_stack(cols)) @ D[ok], int(ok.sum())
CUE_T, RESP_T = pfc7.CUE1_LONG, pfc7.RESP_LONG
BASE_W = (CUE_T >= -50) & (CUE_T <= 50)
KEYS = ("c5", "c10", "r10", "csg", "rsg")
def projections(tg_list, avg_list, o7, design="script"):
    """Average over splits of the projections; tg_list[s][u] the half's GLM, avg_list[s][u] the
    other half's averages."""
    acc_res = {k: [] for k in KEYS}
    nkeep = []
    for tg, av in zip(tg_list, avg_list):
        W = np.array([weights_from(tg[u], o7) for u in acc])
        for k in KEYS:
            D = np.stack([av[u][k].ravel() for u in acc])
            coef, n = project(W, D, design)
            acc_res[k].append(coef.reshape(coef.shape[0], av[acc[0]][k].shape[0], -1))
            nkeep.append(n)
    return {k: np.mean(v, axis=0) for k, v in acc_res.items()}, (min(nkeep), max(nkeep))

t6 = time.time()
rng = section_rng("fig6-projection")
SPLITS = {}
# O4 (a): odd/even, weights from one half's GLM (already fitted), data from the other half
tg_oe, dm_oe = [], []
for wh, dh in (("odd", "even"), ("even", "odd")):
    tg_oe.append({u: {ep: (G[u][f"b{ep}_{wh}"], G[u][f"t{ep}_{wh}"]) for ep in ("X2", "X3", "XR")} for u in acc})
    dm_oe.append({u: (G[u]["odd"] if dh == "odd" else ~G[u]["odd"]) for u in acc})
SPLITS["a"] = (tg_oe, dm_oe)
# O4 (b): 100 random halves of the trials with 3 or more cues (the R3 scripts)
tg_r, dm_r = [], []
for s_ in range(100):
    tg, dmk = {}, {}
    for u in acc:
        d = U[u]
        draw = rng.random(len(d["condition"])) > 0.5
        tg[u] = half_fit(d, draw)
        dmk[u] = ~(draw & (d["num_pics_viewed"] >= 3))
    tg_r.append(tg); dm_r.append(dmk)
SPLITS["b"] = (tg_r, dm_r)
print(f"weights for 100 random halves: {time.time() - t6:.0f} s")
PROJ = {}
for o4, (tgl, dml) in SPLITS.items():
    for o5 in O5S:
        avz = [{u: averages(u, dml[s_][u], LAB[o5][u]) for u in acc} for s_ in range(len(dml))]
        avh = [{u: to_hz(a[u], u) for u in acc} for a in avz]
        for o6, avl in (("a", avh), ("b", avz)):
            for o7 in ("a", "b"):
                PROJ[(o4, o5, o6, o7)] = projections(tgl, avl, o7)
        del avz, avh
print(f"projections for {len(PROJ)} reading combinations: {time.time() - t6:.0f} s; neurons kept per projection "
      f"{sorted(set(v[1] for v in PROJ.values()))}")

def bl(P, comp, key):
    """Baseline-corrected projection of component `comp` (0 belief, 1 action) for data `key`."""
    base_key = {"c5": "c5", "c10": "c10", "r10": "c10", "csg": "csg", "rsg": "csg"}[key]
    b0 = P[base_key][comp][:, BASE_W].mean(1, keepdims=True)
    return P[key][comp] - b0
'''
open(p,'w').write(s)
EOF
date -u
```

```
Sat Nov 14 18:59:48 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude/nbsrc.py'; s=open(p).read()
a=s.index('def projections(tg_list'); b=s.index('t6 = time.time()')
s=s[:a]+'''def proj_one(tg, av, o7, design="script"):
    W = np.array([weights_from(tg[u], o7) for u in acc])
    out, ns = {}, []
    for k in KEYS:
        D = np.stack([av[u][k].ravel() for u in acc])
        coef, n = project(W, D, design)
        out[k] = coef.reshape(coef.shape[0], av[acc[0]][k].shape[0], -1)
        ns.append(n)
    return out, ns

'''+s[b:]
a=s.index('PROJ = {}'); b=s.index('def bl(P, comp, key):')
s=s[:a]+'''PROJ, NKEEP = {}, set()
for o4, (tgl, dml) in SPLITS.items():
    for o5 in O5S:
        acc_ = {}
        for s_ in range(len(dml)):
            avz = {u: averages(u, dml[s_][u], LAB[o5][u]) for u in acc}
            avh = {u: to_hz(avz[u], u) for u in acc}
            for o6, av in (("a", avh), ("b", avz)):
                for o7 in ("a", "b"):
                    pr, ns = proj_one(tgl[s_], av, o7)
                    NKEEP.update(ns)
                    for k, v in pr.items():
                        acc_.setdefault((o6, o7, k), []).append(v)
        for (o6, o7, k), v in acc_.items():
            PROJ.setdefault((o4, o5, o6, o7), {})[k] = np.mean(v, axis=0)
        del acc_
print(f"projections for {len(PROJ)} reading combinations: {time.time() - t6:.0f} s; neurons kept per projection "
      f"{min(NKEEP)} to {max(NKEEP)} of {len(acc)}")

'''+s[b:]
open(p,'w').write(s)
EOF
date -u
```

```
Sat Nov 14 18:59:58 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude/nbsrc.py'; s=open(p).read()
old='''                    pr, ns = proj_one(tgl[s_], av, o7)
                    NKEEP.update(ns)'''
new='''                    pr, ns = proj_one(tgl[s_], av, o7)
                    NKEEP.update(ns)
                    cb = pr["c5"][0] - pr["c5"][0][:, BASE_W].mean(1, keepdims=True)
                    for wn, (lo, hi) in W6C.items():
                        w = (CUE_T >= lo) & (CUE_T <= hi)
                        SPLIT6C.setdefault((o4, o5, o6, o7, wn), []).append(bool(cb[0, w].mean() > cb[4, w].mean()))'''
assert old in s; s=s.replace(old,new)
s=s.replace("PROJ, NKEEP = {}, set()","PROJ, NKEEP, SPLIT6C = {}, set(), {}\nW6C = {\"a\": (100, 500), \"b\": (0, 500)}")
open(p,'w').write(s)
EOF
cat >> /tmp/claude/nbsrc.py <<'EOF'

# %% [markdown]
# ## fig6c-belief-subspace-rt
#
# > ACC activity in the belief confirmation subspace separates short from long reaction time
# > trials early in the trial, even at cue 1 presentation.

# %% tags=["claim:fig6c-belief-subspace-rt"]
rows = []
for key, P in PROJ.items():
    c = bl(P, 0, "c5")
    r = dict(zip(("O4", "O5", "O6", "O7"), key))
    for wn, (lo, hi) in W6C.items():
        w = (CUE_T >= lo) & (CUE_T <= hi)
        r[f"short-long {lo}-{hi}"] = c[0, w].mean() - c[4, w].mean()
        if key[0] == "b":
            r[f"splits {lo}-{hi}"] = int(np.sum(SPLIT6C[key + (wn,)]))
    w2 = (CUE_T >= 500) & (CUE_T <= 1000)
    r["short-long 500-1000"] = c[0, w2].mean() - c[4, w2].mean()
    rows.append(r)
f6c = pd.DataFrame(rows).set_index(["O4", "O5", "O6", "O7"])
print(f6c.round(4))
print("readings where the shortest RT bin is above the longest, 100-500 ms:", int((f6c["short-long 100-500"] > 0).sum()),
      "of", len(f6c), "; 0-500 ms:", int((f6c["short-long 0-500"] > 0).sum()))
P = PROJ[("a", "script", "b", "a")]
fig, ax = plt.subplots(1, 3, figsize=(14, 3.5))
c = bl(P, 0, "c5")
for k in range(5):
    m = (CUE_T >= -100) & (CUE_T <= 2200)
    ax[0].plot(CUE_T[m], c[k, m], label=f"RT bin {k + 1}")
ax[0].set_title("belief, cue 1 locked (odd/even, script bins, z, mean T)", fontsize=8); ax[0].legend(fontsize=7)
rb_ = np.stack([bl(P, 0, "r10")[0::2], bl(P, 0, "r10")[1::2]]).mean(0)
m = (RESP_T >= -500) & (RESP_T <= 100)
for k in range(5):
    ax[1].plot(RESP_T[m], rb_[k, m])
ax[1].set_title("belief, response locked", fontsize=8)
lr = bl(P, 1, "r10")
for k in range(5):
    ax[2].plot(RESP_T[m], lr[2 * k, m] - lr[2 * k + 1, m])
ax[2].set_title("action, response locked, left minus right", fontsize=8)
plt.show()
print("plotted ranges:", [round(float(x), 3) for x in (c[:, (CUE_T >= -100) & (CUE_T <= 2200)].min(),
      c[:, (CUE_T >= -100) & (CUE_T <= 2200)].max(), rb_[:, m].min(), rb_[:, m].max())])

# %% [markdown]
# RESULT:fig6c-belief-subspace-rt

# %% [markdown]
# ## fig6d-belief-ramp-to-choice
#
# > Irrespective of reaction time, ACC activity in the belief confirmation subspace ramps up
# > shortly before the joystick movement.
#
# The scripts' response-locked belief trace averages the left- and right-choice projections; the
# criterion compares the mean over -200 to 0 ms with that over -500 to -300 ms in each RT bin.

# %% tags=["claim:fig6d-belief-ramp-to-choice"]
late = (RESP_T >= -200) & (RESP_T <= 0)
early = (RESP_T >= -500) & (RESP_T <= -300)
rows = []
for key, P in PROJ.items():
    r10 = bl(P, 0, "r10")
    tr = np.stack([r10[0::2], r10[1::2]]).mean(0)
    rise = tr[:, late].mean(1) - tr[:, early].mean(1)
    rows.append(dict(zip(("O4", "O5", "O6", "O7"), key), **{f"bin{k + 1}": rise[k] for k in range(5)},
                     n_rising=int((rise > 0).sum())))
f6d = pd.DataFrame(rows).set_index(["O4", "O5", "O6", "O7"])
print(f6d.round(4))
print("readings with all five bins rising:", int((f6d.n_rising == 5).sum()), "of", len(f6d))

# %% [markdown]
# RESULT:fig6d-belief-ramp-to-choice

# %% [markdown]
# ## fig6e-action-subspace-ramp
#
# > ACC activity in the left/right action selection subspace ramps up as evidence is revealed and
# > peaks immediately before the response.

# %% tags=["claim:fig6e-action-subspace-ramp"]
win = (RESP_T >= -500) & (RESP_T <= 100)
rows = []
for key, P in PROJ.items():
    r10 = bl(P, 1, "r10")
    for sgn_rd, tr in (("a", r10[0::2] - r10[1::2]), ("b", bl(P, 1, "rsg"))):
        rise = tr[:, late].mean(1) - tr[:, early].mean(1)
        tpk = RESP_T[win][np.argmax(tr[:, win], axis=1)]
        ok = (rise > 0) & (tpk >= -200) & (tpk <= 100)
        rows.append(dict(zip(("O4", "O5", "O6", "O7"), key), sign=sgn_rd,
                         **{f"rise{k + 1}": rise[k] for k in range(5)},
                         **{f"peak{k + 1}": int(tpk[k]) for k in range(5)}, n_ok=int(ok.sum())))
f6e = pd.DataFrame(rows).set_index(["O4", "O5", "O6", "O7", "sign"])
print(f6e.round(3).to_string())
print("readings where every bin rises and peaks between -200 and 100 ms:", int((f6e.n_ok == 5).sum()), "of", len(f6e))

# %% [markdown]
# RESULT:fig6e-action-subspace-ramp

# %% [markdown]
# ## fig7a-ofc-value-difference-neurons
#
# > At all three time points (cue 2 against cue 1, cue 3 against cue 1, cue 3 against cue 2), a
# > greater proportion of single neurons encoded value difference between attended and unattended
# > cues in OFC than in ACC and DLPFC.
#
# Units SEL5 (Fig7_single_neurons_cue2and3.m). The script's own threshold is |T| > 1.64 on each of
# the three tests (its comment reads `norminv(0.05)`), shown as a variant beside the claims file's
# readings p < 0.05 (|T| > 1.96) and p < 0.01 (|T| > 2.576).

# %% tags=["claim:fig7a-ofc-value-difference-neurons"]
TESTS = {"a": [("X2", 6, 5, 31), ("X3", 3, 1, 32), ("X3", 3, 2, 33)],
         "b": [("X2", 6, 5, 31), ("X3", (7, 9), 5, (36, 38)), ("X3", (7, 9), 6, (37, 39))]}
def passes(units, test, b, thr):
    ep, att, un, dif = test
    out = np.zeros(len(units), bool)
    atts = att if isinstance(att, tuple) else (att,)
    difs = dif if isinstance(dif, tuple) else (dif,)
    for at, df in zip(atts, difs):
        ta, tu, td = tst(units, ep, at, b), tst(units, ep, un, b), tst(units, ep, df, b)
        out |= (np.abs(ta) > thr) & (np.abs(tu) > thr) & (np.abs(td) > thr) & (np.sign(ta) != np.sign(tu))
    return out
F7 = {}
for tt in ("a", "b"):
    for o3, b in (("250", B250), ("300", B300)):
        for o2, thr in (("0.05", 1.96), ("0.01", 2.576), ("script 1.64", 1.64)):
            fr = {}
            anyp = {}
            for a in (1, 2, 3):
                ps = [passes(SEL5[a], t, b, thr) for t in TESTS[tt]]
                fr[a] = [100 * p.mean() for p in ps]
                anyp[a] = 100 * np.any(ps, axis=0).mean()
            ofc_top = all(fr[3][i] > fr[1][i] and fr[3][i] > fr[2][i] for i in range(3))
            F7[(tt, o3, o2)] = dict(fr=fr, any=anyp, ofc_top=ofc_top,
                                    any_top=anyp[3] > anyp[1] and anyp[3] > anyp[2])
            chis = [pfc7.chi2_yates(round(fr[3][i] * len(SEL5[3]) / 100), len(SEL5[3]),
                                    round(fr[x][i] * len(SEL5[x]) / 100), len(SEL5[x]))[1] for i in range(3) for x in (1, 2)]
            print(f"trial types ({tt}), bin {o3} ms, threshold {o2}: % ACC {np.round(fr[1], 1)}, DLPFC "
                  f"{np.round(fr[2], 1)}, OFC {np.round(fr[3], 1)}; OFC highest at all three: {ofc_top};"
                  f" chi2 p OFC vs ACC/DLPFC {[float('%.2g' % c) for c in chis]}")
# time course with the script's threshold, any bin: the script plots the percentage per bin
for a in (1, 2, 3):
    ps = np.mean([[passes(SEL5[a], t, b, 1.64) for b in range(61)] for t in TESTS["a"]], axis=2)
    print(f"{NAMES[a]}: % passing per bin (script threshold), max over bins of each test: {np.round(ps.max(1) * 100, 1)}")

# %% [markdown]
# RESULT:fig7a-ofc-value-difference-neurons

# %% [markdown]
# ## fig7b-ofc-value-difference-any
#
# > Collapsed across the three tests, the fraction of neurons passing the value difference
# > criteria at any of the three cues is greater in OFC than in ACC and DLPFC.

# %% tags=["claim:fig7b-ofc-value-difference-any"]
for k, v in F7.items():
    print(f"{k}: any of three, % ACC {v['any'][1]:.1f}, DLPFC {v['any'][2]:.1f}, OFC {v['any'][3]:.1f}; OFC highest: {v['any_top']}")

# %% [markdown]
# RESULT:fig7b-ofc-value-difference-any

# %% [markdown]
# ## fig7c-acc-belief-neurons
#
# > At all four time points, a greater proportion of single neurons significantly encoded belief
# > confirmation in ACC than in OFC or DLPFC.
#
# Fig7_single_neurons_cue2and3.m uses |T| > 1.96 (its comment, `norminv(0.05/2)`).

# %% tags=["claim:fig7c-acc-belief-neurons"]
for o3, b in (("250", B250), ("300", B300)):
    for o2, thr in (("0.05", 1.96), ("0.01", 2.576)):
        fr = {a: [100 * np.mean(np.abs(tst(SEL5[a], ep, ev, b)) > thr) for ep, ev in
                  (("X2", 13), ("X2", 14), ("X3", 15), ("X3", 16))] for a in (1, 2, 3)}
        n_top = sum(fr[1][i] > fr[2][i] and fr[1][i] > fr[3][i] for i in range(4))
        chis = [float('%.2g' % pfc7.chi2_yates(round(fr[1][i] * len(SEL5[1]) / 100), len(SEL5[1]),
                                                round(fr[x][i] * len(SEL5[x]) / 100), len(SEL5[x]))[1])
                for i in range(4) for x in (2, 3)]
        print(f"bin {o3} ms, p < {o2}: % EV13/14/15/16 ACC {np.round(fr[1], 1)}, DLPFC {np.round(fr[2], 1)},"
              f" OFC {np.round(fr[3], 1)}; ACC highest in {n_top} of 4; chi2 p ACC vs DLPFC/OFC {chis}")

# %% [markdown]
# RESULT:fig7c-acc-belief-neurons
EOF
date -u
```

```
Sat Nov 14 19:00:36 UTC 2026
```

**Agent calls Bash**

```bash
cat >> pfc7.py <<'EOF'


# --------------------------------------------------------------------------- cue 1 regression

def cue1_script_design(d: dict) -> np.ndarray:
    """The 13 regressors of InfoGathering_Neurons_Cue1_regression.m: cue 1 value by attribute
    (magnitude, probability), side and row (raw values, minus 0.55 for magnitude and 0.5 for
    probability), four position constants, and the demeaned number of pictures viewed / 4."""
    fp = d["First_pos"].astype(int)
    lp, lm, rp, rm, pt = d["Left_prob"], d["Left_pay"], d["Right_prob"], d["Right_pay"], d["Prob_top"]
    n = len(fp)
    val = np.zeros(n)
    isprob = np.zeros(n, bool)
    for i in range(n):
        top = fp[i] in (1, 3)
        left = fp[i] in (1, 2)
        isprob[i] = top == (pt[i] == 1)
        val[i] = (lp[i] if left else rp[i]) if isprob[i] else (lm[i] if left else rm[i])
    cols = []
    for prob in (False, True):            # M1LT M1RT M1LB M1RB, then P1..
        for pos in (1, 3, 2, 4):          # LT, RT, LB, RB
            c = np.where((fp == pos) & (isprob == prob), val - (0.5 if prob else 0.55), 0.0)
            cols.append(c)
    for pos in (1, 2, 3, 4):
        cols.append((fp == pos).astype(float))
    pv = d["pictures_views"] / 4
    cols.append(pv - pv.mean())
    return np.column_stack(cols)


def cue1_script_contrasts() -> np.ndarray:
    """Contrasts 26 (value), 41 (left minus right value), 51 (probability minus magnitude value)
    and 42 (top minus bottom value) of the script, over its 13 regressors."""
    e = np.eye(13)
    # columns: 0 M1LT, 1 M1RT, 2 M1LB, 3 M1RB, 4 P1LT, 5 P1RT, 6 P1LB, 7 P1RB
    value = e[0:8].sum(0)
    lr = e[[0, 2, 4, 6]].sum(0) - e[[1, 3, 5, 7]].sum(0)
    pm = e[4:8].sum(0) - e[0:4].sum(0)
    tb = e[[0, 1, 4, 5]].sum(0) - e[[2, 3, 6, 7]].sum(0)
    return np.vstack([value, lr, pm, tb])


def perm_significant(Y, X, C, rng, nperm=1000, first_bin=10, chunk=200):
    """sliding_regression_ols_perm.m: T-statistics of contrasts C over the bins of Y, against the
    2.5th and 97.5th percentiles of the minimum and maximum over bins of the T-statistics from
    `nperm` permutations of the trials; significant when any bin from `first_bin` on passes."""
    P = np.linalg.pinv(X)
    dof = X.shape[0] - np.linalg.matrix_rank(X)
    pre = np.einsum("ij,jk,ik->i", C, P @ P.T, C)
    XtX = X.T @ X
    yy = (Y ** 2).sum(0)

    def tstats(Ys):  # Ys: perms x trials x bins
        pe = np.einsum("kn,pnb->pkb", P, Ys)
        fit = np.einsum("pkb,kl,plb->pb", pe, XtX, pe)
        sig = (yy[None] - fit) / dof
        cope = np.einsum("ck,pkb->pcb", C @ np.eye(X.shape[1]), pe)
        return cope / np.sqrt(pre[None, :, None] * sig[:, None, :])

    t = tstats(Y[None])[0]
    mx, mn = [], []
    for s in range(0, nperm, chunk):
        idx = np.stack([rng.permutation(Y.shape[0]) for _ in range(min(chunk, nperm - s))])
        tp = tstats(Y[idx])
        mx.append(tp.max(2)); mn.append(tp.min(2))
    mx, mn = np.vstack(mx), np.vstack(mn)
    hi = np.percentile(mx, 97.5, axis=0)
    lo = np.percentile(mn, 2.5, axis=0)
    tt = t[:, first_bin:]
    return ((tt >= hi[:, None]) | (tt <= lo[:, None])).any(1), t
EOF
cat >> /tmp/claude/nbsrc.py <<'EOF'

# %% [markdown]
# ## Cue 1 single-neuron regression (claims fig8-*)
#
# The claims file's readings: regressors (a) value (rank -2 to 2), value x side (left 1, right
# -1), value x attribute (probability 1, magnitude -1), value x row (top 1, bottom -1), the three
# main effects and a constant; (b) the four value regressors and a constant. Windows (i) 100-500 ms
# (the mean of the bins centred at 200 and 400 ms, which tile 101-500 ms), (ii) the bin at 250 ms,
# (iii) at 300 ms. Trials O9 (a) all, (b) 3 or more cues. Significance O2 (a) p < 0.05, (b) p < 0.01,
# two-sided on the coefficient. The binomial test is the script's, 2 x P(X > k) at a chance rate
# equal to the significance level; the chi-square is chi2.m (Yates). Units SEL (Fig8 script).
#
# The script's own regression (InfoGathering_Neurons_Cue1_regression.m: 13 regressors on raw
# values, significance from 1000 permutations corrected over the bins from 0 to 500 ms) is run as
# a further variant.

# %%
B200, B400 = int(np.flatnonzero(pfc7.TIMEBINS == 200)[0]), int(np.flatnonzero(pfc7.TIMEBINS == 400)[0])
def cue1_X(d, rd):
    v = d["Lreg"][:, 0] + d["Rreg"][:, 0] - 3
    s_ = np.where(d["Lreg"][:, 0] > 0, 1.0, -1.0)
    a_ = np.where(d["P_first"] > 0, 1.0, -1.0)
    r_ = np.where(np.isin(d["First_pos"], (1, 3)), 1.0, -1.0)
    cols = [v, v * s_, v * a_, v * r_]
    if rd == "a":
        cols += [s_, a_, r_]
    return np.column_stack(cols + [np.ones(len(v))])
def cue1_y(d, win):
    X1 = d["X1"].astype(float) * 1000
    return {"i": (X1[:, B200] + X1[:, B400]) / 2, "ii": X1[:, B250], "iii": X1[:, B300]}[win]
F8 = {}
for rd in ("a", "b"):
    for win in ("i", "ii", "iii"):
        for o9 in ("a", "b"):
            P_ = {}
            for a in (1, 2, 3):
                ps = []
                for u in SEL[a]:
                    d = U[u]
                    k = np.ones(len(d["condition"]), bool) if o9 == "a" else d["num_pics_viewed"] >= 3
                    X = cue1_X(d, rd)[k]
                    y = cue1_y(d, win)[k]
                    _, _, t = pfc7.ols(y[:, None], X, np.eye(X.shape[1])[:4])
                    dof = X.shape[0] - np.linalg.matrix_rank(X)
                    ps.append(2 * stats.t.sf(np.abs(t[:, 0]), dof))
                P_[a] = np.array(ps)   # units x 4 (value, action, attribute, spatial)
            F8[(rd, win, o9)] = P_
VAR8 = ["value", "action value", "attribute value", "spatial value"]
def f8_counts(key, alpha):
    P_ = F8[key]
    return {a: (P_[a] < alpha).sum(0) for a in (1, 2, 3)}, {a: len(P_[a]) for a in (1, 2, 3)}
rng = section_rng("fig8-script")
C8 = pfc7.cue1_script_contrasts()
SIG8 = {}
t8 = time.time()
for a in (1, 2, 3):
    SIG8[a] = np.array([pfc7.perm_significant(U[u]["X1"].astype(float) * 1000, pfc7.cue1_script_design(U[u]),
                                              C8, rng)[0] for u in SEL[a]])
print(f"script regression with permutations: {time.time() - t8:.0f} s")
rows = []
for key in F8:
    for o2, alpha in (("0.05", 0.05), ("0.01", 0.01)):
        k_, n_ = f8_counts(key, alpha)
        r = dict(regressors=key[0], window=key[1], trials=key[2], alpha=o2)
        for a in (1, 2, 3):
            for j, vn in enumerate(VAR8):
                r[f"{NAMES[a]} {vn} %"] = 100 * k_[a][j] / n_[a]
        rows.append(r)
r = dict(regressors="script", window="0-500 corrected", trials="all", alpha="0.05")
for a in (1, 2, 3):
    for j, vn in enumerate(VAR8):
        r[f"{NAMES[a]} {vn} %"] = 100 * SIG8[a][:, j].mean()
rows.append(r)
F8T = pd.DataFrame(rows).set_index(["regressors", "window", "trials", "alpha"])
print(F8T.round(1).to_string())
def f8_all():
    """(key, alpha, counts k[a][var], n[a]) for every reading, the script's last."""
    for key in F8:
        for alpha in (0.05, 0.01):
            k_, n_ = f8_counts(key, alpha)
            yield key + (str(alpha),), alpha, k_, n_
    yield ("script",), 0.05, {a: SIG8[a].sum(0) for a in (1, 2, 3)}, {a: len(SIG8[a]) for a in (1, 2, 3)}

# %% [markdown]
# ## fig8-cue1-value-all-regions
#
# > At cue 1, a significant fraction of neurons in all three regions encoded the cue's value
# > irrespective of its attribute, action or spatial position.

# %% tags=["claim:fig8-cue1-value-all-regions"]
nrd = 0; nok = 0
for key, alpha, k_, n_ in f8_all():
    pb = {a: pfc7.binom_p_code(k_[a][0], n_[a], alpha) for a in (1, 2, 3)}
    ok = all(p < 1e-7 for p in pb.values())
    nrd += 1; nok += ok
    print(key, {NAMES[a]: f"{100 * k_[a][0] / n_[a]:.1f}% p={pb[a]:.1g}" for a in (1, 2, 3)}, "holds:", ok)
print(f"holds under {nok} of {nrd} readings (the last is the script's)")

# %% [markdown]
# RESULT:fig8-cue1-value-all-regions

# %% [markdown]
# ## fig8-action-value-acc-dlpfc
#
# > About 18% of ACC and DLPFC neurons encoded left/right action value at cue 1, above chance and
# > more than OFC, which encoded action value at chance level.

# %% tags=["claim:fig8-action-value-acc-dlpfc"]
for key, alpha, k_, n_ in f8_all():
    fr = {a: 100 * k_[a][1] / n_[a] for a in (1, 2, 3)}
    pb = {a: pfc7.binom_p_code(k_[a][1], n_[a], alpha) for a in (1, 2, 3)}
    pc = {a: pfc7.chi2_yates(k_[a][1], n_[a], k_[3][1], n_[3])[1] for a in (1, 2)}
    tests = (all(pb[a] < 1e-5 for a in (1, 2)) and all(fr[a] > fr[3] and pc[a] < 0.05 for a in (1, 2))
             and pb[3] >= 0.05)
    within = all(abs(fr[a] - 18) <= 1.8 for a in (1, 2))
    print(key, f"ACC {fr[1]:.1f}% (binom p={pb[1]:.1g}, chi2 vs OFC p={pc[1]:.2g}), DLPFC {fr[2]:.1f}% "
          f"(p={pb[2]:.1g}, chi2 p={pc[2]:.2g}), OFC {fr[3]:.1f}% (p={pb[3]:.2g}); tests hold {tests}, within 18 +/- 1.8 {within}")

# %% [markdown]
# RESULT:fig8-action-value-acc-dlpfc

# %% [markdown]
# ## fig8-spatial-value-dlpfc
#
# > In DLPFC, top/bottom spatial value neurons are as prevalent as left/right action value
# > neurons, while in ACC they are significantly fewer, so DLPFC encodes value by spatial position
# > and ACC by action.

# %% tags=["claim:fig8-spatial-value-dlpfc"]
for key, alpha, k_, n_ in f8_all():
    pb = pfc7.binom_p_code(k_[2][3], n_[2], alpha)
    pd_ = pfc7.chi2_yates(k_[2][3], n_[2], k_[2][1], n_[2])[1]
    pa_ = pfc7.chi2_yates(k_[1][3], n_[1], k_[1][1], n_[1])[1]
    ok = pb < 1e-6 and pd_ >= 0.05 and k_[1][3] < k_[1][1] and pa_ < 0.05
    print(key, f"DLPFC spatial {100 * k_[2][3] / n_[2]:.1f}% (binom p={pb:.1g}) vs action {100 * k_[2][1] / n_[2]:.1f}% "
          f"(chi2 p={pd_:.2g}); ACC spatial {100 * k_[1][3] / n_[1]:.1f}% vs action {100 * k_[1][1] / n_[1]:.1f}% "
          f"(chi2 p={pa_:.2g}) -> holds {ok}")

# %% [markdown]
# RESULT:fig8-spatial-value-dlpfc

# %% [markdown]
# ## fig8-attribute-value-ofc
#
# > About 24% of OFC neurons encoded attribute value at cue 1 (preferring probability or magnitude
# > cues), above chance and more than in ACC or DLPFC.

# %% tags=["claim:fig8-attribute-value-ofc"]
for key, alpha, k_, n_ in f8_all():
    fr = {a: 100 * k_[a][2] / n_[a] for a in (1, 2, 3)}
    pb = pfc7.binom_p_code(k_[3][2], n_[3], alpha)
    pc = {a: pfc7.chi2_yates(k_[3][2], n_[3], k_[a][2], n_[a])[1] for a in (1, 2)}
    tests = pb < 1e-7 and all(fr[3] > fr[a] and pc[a] < 0.05 for a in (1, 2))
    print(key, f"OFC {fr[3]:.1f}% (binom p={pb:.1g}); ACC {fr[1]:.1f}% (chi2 p={pc[1]:.2g}); DLPFC {fr[2]:.1f}% "
          f"(chi2 p={pc[2]:.2g}); tests hold {tests}, within 24 +/- 2.4 {abs(fr[3] - 24) <= 2.4}")

# %% [markdown]
# RESULT:fig8-attribute-value-ofc

# %% [markdown]
# ## figs9-ev16-correlation
#
# > The GLM's regressors of interest are decorrelated by design except EV 16, whose mean r2 with
# > EVs 7 and 9 is 0.167 and 0.194.
#
# The criterion uses trials with 3 or more cues; the GLM script computes `DM_crosscorr` before
# dropping trials with 2 cues, over all 724 units (shown as a variant over the units loaded here).

# %% tags=["claim:figs9-ev16-correlation"]
def r2mats(trials):
    out = {}
    for u, d in U.items():
        X = pfc7.glm_design(d)
        if trials == "3+":
            X = X[d["num_pics_viewed"] >= 3]
        with np.errstate(invalid="ignore", divide="ignore"):
            out[u] = np.corrcoef(X.T) ** 2
    return out
INT = list(range(0, 6)) + list(range(12, 18))
for trials in ("3+", "all"):
    R2 = r2mats(trials)
    by_sess = {}
    for u, m in R2.items():
        by_sess.setdefault((U[u]["sb"], U[u]["snum"]), m)
    for over, mats in (("sessions", list(by_sess.values())), ("neurons", list(R2.values()))):
        M = np.nanmean(np.stack(mats), axis=0)
        others = [M[i, j] for i in INT for j in INT if i < j and 15 not in (i, j)]
        print(f"trials {trials}, mean over {over} (n = {len(mats)}): r2 EV16-EV7 {M[15, 6]:.3f}, EV16-EV9 {M[15, 8]:.3f};"
              f" largest other pair among EVs 1-6 and 13-18 {max(others):.3f}"
              f" (EV{INT[np.argmax([M[i, j] if i < j and 15 not in (i, j) else -1 for i in INT for j in INT]) // len(INT)] + 1}"
              f"-EV{INT[np.argmax([M[i, j] if i < j and 15 not in (i, j) else -1 for i in INT for j in INT]) % len(INT)] + 1})")

# %% [markdown]
# RESULT:figs9-ev16-correlation

# %% [markdown]
# ## figs11-alternative-value-template
#
# > Replacing the attended value and left/right value templates by a uniform-diagonal form
# > (negative absolute value difference) gives qualitatively the same functional dissociation
# > across OFC, DLPFC and ACC.
#
# The commented line of Fig4_RSA.m for Supplementary Figure 11 (`r4 = -repmat(abs(m1-m2),4,4);
# r4 = r4 - mean(r4(:))`), with left/right value following it.

# %% tags=["claim:figs11-alternative-value-template"]
RSA_ALT = {o9: rsa_run(MATS[o9], DM_ALT, FTP_ALT, section_rng("rsa-alt-" + o9)) for o9 in ("a", "b")}
print(rsa_table(RSA_ALT["a"]).round(4))
for o9, o8 in readings():
    r = RSA_ALT[o9]
    tm = "attended value"
    f = sig(r, tm, 3, o8) and cpdv(r, tm, 3) > cpdv(r, tm, 1) and cpdv(r, tm, 3) > cpdv(r, tm, 2)
    print(f"O9 ({o9}) O8 {o8}: attended value in OFC T {r['t'][IDX[tm], 2]:.2f}, p "
          f"{(r['p1'] if o8 == 'one' else r['p2'])[IDX[tm], 2]:.4f}, CPD % {np.round(100 * r['cpd'][IDX[tm]], 2)}"
          f" -> fig4f holds {f}")
ALT_LR = judge_lr(RSA_ALT)

# %% [markdown]
# RESULT:figs11-alternative-value-template

# %%
print(f"total run time {(time.time() - T0) / 60:.1f} min, peak memory "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB")

# %% [markdown]
# ## Summary
#
# SUMMARY
EOF
date -u
```

```
Sat Nov 14 19:01:48 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='pfc7.py'; s=open(p).read()
s=s.replace('pe = np.einsum("kn,pnb->pkb", P, Ys)','pe = np.einsum("kn,pnb->pkb", P, Ys, optimize=True)')
s=s.replace('fit = np.einsum("pkb,kl,plb->pb", pe, XtX, pe)','fit = np.einsum("pkb,kl,plb->pb", pe, XtX, pe, optimize=True)')
s=s.replace('cope = np.einsum("ck,pkb->pcb", C @ np.eye(X.shape[1]), pe)','cope = np.einsum("ck,pkb->pcb", C, pe, optimize=True)')
open(p,'w').write(s)
p='/tmp/claude/nbsrc.py'; s=open(p).read()
a=s.index('        M = np.nanmean(np.stack(mats), axis=0)')
b=s.index('# %% [markdown]\n# RESULT:figs9-ev16-correlation')
s=s[:a]+'''        M = np.nanmean(np.stack(mats), axis=0)
        pairs = [(M[i, j], i, j) for i in INT for j in INT if i < j and 15 not in (i, j)]
        mx = max(pairs)
        print(f"trials {trials}, mean over {over} (n = {len(mats)}): r2 EV16-EV7 {M[15, 6]:.3f}, EV16-EV9 {M[15, 8]:.3f};"
              f" largest other pair among EVs 1-6 and 13-18: EV{mx[1] + 1}-EV{mx[2] + 1} {mx[0]:.3f}")

'''+s[b:]
s=s.replace('''for s in ["Miles", "Frank"]:
    pass
''','')
open(p,'w').write(s)
EOF
cd $TMPDIR && sed -e 's/^NPERM = 10000/NPERM = 200/' -e 's/for s_ in range(100):/for s_ in range(5):/' -e 's/for p in range(100):/for p in range(10):/' -e 's/nperm=1000, first_bin/nperm=100, first_bin/' /tmp/claude/nbsrc.py > dev.py && grep -n "NPERM = \|range(5)\|range(10)" dev.py | head; date -u
```

```
574:NPERM = 200
885:    for p in range(10):
1196:            for i in range(5):
1197:                for j in range(5):
1309:    for k in range(5):
1360:for s_ in range(5):
1426:for k in range(5):
1432:for k in range(5):
1436:for k in range(5):
1463:    rows.append(dict(zip(("O4", "O5", "O6", "O7"), key), **{f"bin{k + 1}": rise[k] for k in range(5)},
Sat Nov 14 19:02:01 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && export MPLBACKEND=Agg PYTHONPATH=entries/hunt-2018 && /usr/bin/time -v python -u dev.py > dev.log 2>&1; tail -5 dev.log; grep -E "Maximum resident|Elapsed" dev.log
```

```
Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 1
	Elapsed (wall clock) time (h:mm:ss or m:ss): 3:13.95
	Maximum resident set size (kbytes): 3870960
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" dev.log | head -150
```

```
83 keys under pfc-7/, 70.7 GB
b821300630d337838de951dd3a19fa5b  behavioural_data/Miles_InfoGathering_All_Data.mat
fb7545f884e5789c70196ec360e18f65  behavioural_data/Frank_InfoGathering_All_Data.mat
1d9e29eccbcdb2a8610f9268f4150c18  neuronal_data/LTH_processed_data.zip
99d5b71e652d9d70108890bcb335622a  other_data/all_units_info.mat
386cf609f60e8dfc0aa3cfa46c85496e  neuronal_regression_results/info_gathering_cue123_alltrials_attentional_final.mat
dbf1eabfa9abc27f982c1b501b64d875  scripts.zip
behaviour loaded, 105 s
549 units loaded, 162 s, peak memory 3.9 GB
raw recording sessions (zip files): {'M': 29, 'F': 25}
behavioural sessions: {'F': 25, 'M': 32}  trials: {'F': 9863, 'M': 14251}
trial errors in the behavioural files: {0: 19359, 6: 4755}  conditions: {4: 12104, 3: 12010}
units in all_units_info.mat by area: {'ACC': 198, 'OFC': 195, 'VMPFC': 160, 'DLPFC': 156, '[]': 15}
subject by session counts of units (all areas): {'F': 25, 'M': 29}
units whose file disagrees with all_units_info.mat: [681, 682, 683, 684, 685, 686, 687, 690, 691, 692, 695, 696, 697, 698, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724]
probabilities: [np.float64(0.1), np.float64(0.3), np.float64(0.5), np.float64(0.7), np.float64(0.9)]
magnitudes: [np.float64(0.15), np.float64(0.35), np.float64(0.55), np.float64(0.75), np.float64(0.95)]
pictures viewed (eye codes): {2: 1581, 3: 9833, 4: 12700}
joystick movement time found on 24114 of 24114 trials
response time from cue 1, ms: median 1415, range 732 to 7241
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" dev.log | sed -n 150,400p
```

```
final      0.2843  0.0177  0.0
n-1        1.2289  0.0229  0.0
n-2        1.1614  0.0229  0.0
n-3        1.1760  0.0283  0.0
--- M, model A, raw
                b      se       p
left bias -0.0447  0.0227  0.0486
final      2.3829  0.0583  0.0000
n-1        3.4941  0.0578  0.0000
n-2        2.2209  0.0534  0.0000
n-3        2.4088  0.0668  0.0000
model B seen values, equal weight by overlap: holds in both monkeys = False
model B seen values, equal weight by wald: holds in both monkeys = False
model B true values, equal weight by overlap: holds in both monkeys = False
model B true values, equal weight by wald: holds in both monkeys = False
F first-side bias, option trials (seen): b = -0.467, p = 1.5e-07
F first-side bias, option trials (true): b = -0.175, p = 0.015
F model A rank: all picture weights > 0 with p < 0.05: True; n-2 weight 1.186 against final 0.270 and n-1 1.347
F model A raw: all picture weights > 0 with p < 0.05: True; n-2 weight 2.174 against final 2.156 and n-1 2.892
M first-side bias, option trials (seen): b = -1.220, p = 2.7e-54
[... 215 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hunt-2018 && python3 - <<'EOF'
p='pfc7.py'; s=open(p).read()
s=s.replace('        d["sb"] = str(m["sb"])','        d["sb_raw"] = str(m["sb"])\n        d["sb"] = d["sb_raw"].upper()')
open(p,'w').write(s)
p='/tmp/claude/nbsrc.py'; s=open(p).read()
old='''tbl = pd.crosstab([r.seq_rank[0] for r in b.itertuples()], [r.seq_rank[1] for r in b.itertuples()],
                  values=b.npv250, aggfunc="mean")'''
new='''tbl = pd.crosstab(np.array([r.seq_rank[0] for r in b.itertuples()]), np.array([r.seq_rank[1] for r in b.itertuples()]),
                  values=b.npv250.values, aggfunc="mean")'''
assert old in s; s=s.replace(old,new)
old='''print("units whose file disagrees with all_units_info.mat:", mism)'''
new='''print("units whose file disagrees with all_units_info.mat on subject, session, channel or area:", mism)
print("subject letter as stored in the unit files:", pd.Series([d["sb_raw"] for d in U.values()]).value_counts().to_dict(),
      "; lower case in units", [u for u, d in U.items() if d["sb_raw"].islower()][:3], "...",
      [u for u, d in U.items() if d["sb_raw"].islower()][-1:])'''
assert old in s; s=s.replace(old,new)
old='''nan_units = [u for u in G if not np.isfinite(G[u]["tX3"][:35]).all()]
print("units with non-finite T-statistics:", nan_units)'''
new='''nan_units = [u for u in G if not all(np.isfinite(G[u][ep][:35]).all() for ep in ("tX1", "tX2", "tX3", "tXR"))]
print("units with non-finite T-statistics here:", nan_units)
for u in sorted(set(nan_units) | set(pfc7.NAN_TSTAT_UNITS)):
    print(f"  unit {u} ({info.loc[u, 'area_name']}, rate {info.loc[u, 'info_rate']:.2f} Hz): non-finite T per epoch",
          {ep: int((~np.isfinite(G[u][ep][:35])).sum()) for ep in ("tX1", "tX2", "tX3", "tXR")},
          "; spikes in the cue 3 epoch on trials with 3+ cues:", int(U[u]["X3"][U[u]["num_pics_viewed"] >= 3].sum() * 200))'''
assert old in s; s=s.replace(old,new)
# fig s1cd: add the script's variant (accuracy by seen EV, ties right, per-session mean)
old='''s1cd = pd.DataFrame(rows).set_index(["count", "subject", "n"])'''
new='''s1cd = pd.DataFrame(rows).set_index(["count", "subject", "n"]).sort_index()
# InfoGathering_Behaviour.m (accuracyNPV, mvd): accuracy judged on the seen values (unseen 0.5,
# magnitudes shifted, ties counted right), per session, then averaged over sessions
sv = pfc7.seen_values(beh, "npv250", unseen=(0.5, 0.5), mag_shift=True)
beh["Lseen"], beh["Rseen"] = sv[:, 0] * sv[:, 1], sv[:, 2] * sv[:, 3]
beh["acc_seen"] = (((beh.Lseen >= beh.Rseen) & (beh.left_choice == 1)) | ((beh.Rseen >= beh.Lseen) & (beh.left_choice == 0)))
scr = (beh.groupby(["subject", "session", "npv250"]).agg(acc=("acc_seen", "mean"), vd=("vd_true", "mean"))
       .groupby(level=[0, 2]).mean())
print("script's measure (mean over sessions of accuracy on seen values; mean |EV difference|):")
print((scr.assign(acc=100 * scr.acc)).round(3))'''
assert old in s; s=s.replace(old,new)
old='''              ", cues 1-2:", bool(t.vd_cues12.idxmax() == 2))'''
new='''              ", cues 1-2:", bool(t.vd_cues12.idxmax() == 2))
for sb in ["F", "M"]:
    t = scr.loc[sb]
    print("script measure", sb, "accuracy 2 > 3 and 2 > 4:", bool(t.acc[2] > t.acc[3] and t.acc[2] > t.acc[4]),
          "| largest value difference at 2:", bool(t.vd.idxmax() == 2))'''
assert old in s; s=s.replace(old,new)
# figs5c: also the script's set of variables
old='''for rd in ("a", "b"):
    df = pd.DataFrame(sims[rd])
    print(f"--- reading ({rd}): t75 range (min to max over 100 simulations), ms")
    ok_all = True
    for a in (1, 2, 3):
        keep_v = [i for i in (2, 3, 4) if RSA["a"]["p1"][i, a - 1] < 0.05]
        if a in (1, 2) and RSA["a"]["p1"][IDX["left/right value"], a - 1] < 0.05:
            keep_v.append(IDX["left/right value"])'''
new='''# the script's set: the variables Fig4_RSA.m stacks for Supplementary Figure 5C (peak CPD above 10%)
SCRIPT_SET = {1: [IDX["accept/reject"], IDX["left/right value"]], 2: [IDX["left/right value"]],
              3: [IDX["attended value"], IDX["accept/reject"], IDX["stimulus identity"]]}
print("peak CPD (%) by template and area:", {f"{TN[i]} {NAMES[a]}": round(float(CPDT[i, a - 1].max()), 1)
                                              for i in range(2, 7) for a in (1, 2, 3)})
for rd, vset in [(r_, v_) for r_ in ("a", "b") for v_ in ("significant", "script")]:
    df = pd.DataFrame(sims[rd])
    print(f"--- reading ({rd}), variables {vset}: t75 range (min to max over 100 simulations), ms")
    ok_all = True
    for a in (1, 2, 3):
        if vset == "script":
            keep_v = SCRIPT_SET[a]
        else:
            keep_v = [i for i in (2, 3, 4) if RSA["a"]["p1"][i, a - 1] < 0.05]
            if a in (1, 2) and RSA["a"]["p1"][IDX["left/right value"], a - 1] < 0.05:
                keep_v.append(IDX["left/right value"])'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    print(f"reading ({rd}) criterion holds in every region: {ok_all}")''','''    print(f"reading ({rd}), variables {vset}: criterion holds in every region: {ok_all}")''')
open(p,'w').write(s)
EOF
grep -n "sb\b\|\"sb\"" /tmp/claude/nbsrc.py | head
```

```
85:mism = [u for u, d in U.items() if (d["sb"], int(d["snum"]), int(d["chnum"]), int(d["brain_region"]))
111:    key = (d["sb"], int(d["snum"]), tuple(np.round(d["X1"][:, 40] * 1000, 3)))
117:for (sb, sn), grp in info[info.area.isin([1, 2, 3])].groupby(["subject", "session"]):
119:    bs = beh[(beh.subject == sb)]
121:    chk.append(dict(subject=sb, session=sn, unit_trials=int(d["nInfoGatheringTrials"])))
208:# trials of equal expected value. "Miles" is M and "Frank" is F (the unit files' `sb` field and the
216:for (sb, sn), grp in base.groupby(["subject", "session"]):
218:    ab[(sb, sn)] = (d["n_info_trials_all"], d["n_info_completed"])
230:for sb in ["F", "M"]:
231:    a = ab.loc[sb, "completed"].values
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -e 's/^NPERM = 10000/NPERM = 200/' -e 's/for s_ in range(100):/for s_ in range(5):/' -e 's/for p in range(100):/for p in range(10):/' /tmp/claude/nbsrc.py > dev.py && . env/bin/activate && export MPLBACKEND=Agg PYTHONPATH=entries/hunt-2018 && /usr/bin/time -v python -u dev.py > dev.log 2>&1; grep -E "Maximum resident|Elapsed" dev.log; grep -v "^\s*$" dev.log | sed -n '/disagrees/,/sessions with units in/p'; grep -n -A12 "non-finite" dev.log | head -20
```

```
Elapsed (wall clock) time (h:mm:ss or m:ss): 5:28.97
	Maximum resident set size (kbytes): 3772100
units whose file disagrees with all_units_info.mat on subject, session, channel or area: []
subject letter as stored in the unit files: {'F': 312, 'M': 198, 'm': 39} ; lower case in units [681, 682, 683] ... [724]
probabilities: [np.float64(0.1), np.float64(0.3), np.float64(0.5), np.float64(0.7), np.float64(0.9)]
magnitudes: [np.float64(0.15), np.float64(0.35), np.float64(0.55), np.float64(0.75), np.float64(0.95)]
pictures viewed (eye codes): {2: 1581, 3: 9833, 4: 12700}
joystick movement time found on 24114 of 24114 trials
response time from cue 1, ms: median 1415, range 732 to 7241
rasters: Cue1_MatrixRaw holds 0/1 per ms (spikes, not the 1000 per spike of neuron_matrix.m); GLM bins 61 centred -100 to 500 ms
mean rate (Hz) per unit, medians by area:
      session_rate trial_rate       men info_rate
area                                             
ACC       7.643562   6.749231   7.64354  7.121908
DLPFC     4.583736   4.650717  4.583021  4.566408
OFC       5.062659   5.159219  5.062621  5.155348
whole-session rate from OverallSpikeCodes against the stored men: max |diff| 0.004 Hz
pairs of units with identical cue 1 activity in every trial: []
sessions with units in ACC/DLPFC/OFC: {'F': 24, 'M': 29}
34:units with non-finite T-statistics here: [154, 556, 653]
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" dev.log | sed -n '/script measure/,$p' | head -30; grep -v "^\s*$" dev.log | sed -n '/peak CPD (%) by template/,/plotted range/p' | head -40; grep -v "^\s*$" dev.log | sed -n '/trials per RT bin/,$p' | grep -v "^\s*Command\|^\s*[A-Z][a-z].*:" | head -250
```

```
<persisted-output>
Output too large (41.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8aa49093-d98c-4c6e-8505-65fa3d5b2f8b/tool-results/bsh3pv0ku.txt

Preview (first 2KB):
script measure F accuracy 2 > 3 and 2 > 4: True | largest value difference at 2: True
script measure M accuracy 2 > 3 and 2 > 4: True | largest value difference at 2: True
F: n = 4508; (a) slope on rank1 - rank2 0.729, p = 3.3e-190; (b) back to option 1 when cue 1 > cue 2 0.598 (n=1641), when cue 1 < cue 2 0.087 (n=1914), chi2 = 1051.0, p = 1.5e-230
M: n = 6910; (a) slope on rank1 - rank2 1.210, p = 0; (b) back to option 1 when cue 1 > cue 2 0.867 (n=2735), when cue 1 < cue 2 0.100 (n=2852), chi2 = 3290.1, p = 0
both: n = 11418; (a) slope on rank1 - rank2 0.944, p = 0; (b) back to option 1 when cue 1 > cue 2 0.766 (n=4376), when cue 1 < cue 2 0.095 (n=4766), chi2 = 4226.9, p = 0
npv250 F: (a) mean cues, both ranks +2: 2.05 (n=184); both -2: 2.69 (n=189); (b) Spearman rho -0.356, p = 7.1e-144
npv250 M: (a) mean cues, both ranks +2: 2.22 (n=274); both -2: 3.15 (n=317); (b) Spearman rho -0.499, p = 0
npv250 both: (a) mean cues, both ranks +2: 2.15 (n=458); both -2: 2.98 (n=506); (b) Spearman rho -0.434, p = 0
npv F: (a) mean cues, both ranks +2: 2.47 (n=184); both -2: 3.54 (n=189); (b) Spearman rho -0.425, p = 2.5e-211
npv M: (a) mean cues, both ranks +2: 3.06 (n=274); both -2: 3.86 (n=317); (b) Spearman rho -0.461, p = 0
npv both: (a) mean cues, both ranks +2: 2.82 (n=458); both -2: 3.74 (n=506); (b) Spearman rho -0.436, p = 0
monkey M, mean npv250 by cue 1 rank (rows) and cue 2 rank (columns):
col_0    -2    -1     0     1     2
row_0                              
-2     3.15  3.13  3.06  3.12  3.05
-1     3.09  3.07  3.11  3.02  3.00
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" dev.log | sed -n '/^--- reading/,/reading (b), variables script: criterion/p'; grep -v "^\s*$" dev.log | sed -n '/trials per RT bin/,/total run time/p' | cut -c1-250 | head -150
```

```
--- reading (a), variables significant: t75 range (min to max over 100 simulations), ms
ACC {'spatial attention': (11.0, 30.0), 'stimulus identity': (159.0, 342.0), 'accept/reject': (232.0, 242.0), 'left/right value': (437.0, 492.0)}
   spatial attention below all others: True; left/right value above all others: True
DLPFC {'spatial attention': (70.0, 74.0), 'stimulus identity': (261.0, 339.0), 'accept/reject': (358.0, 511.0), 'left/right value': (344.0, 380.0)}
   spatial attention below all others: True; left/right value above all others: False
OFC {'spatial attention': (26.0, 79.0), 'stimulus identity': (262.0, 282.0), 'attended value': (-2.0, 262.0), 'accept/reject': (211.0, 270.0)}
   spatial attention below all others: False; left/right value above all others: True
reading (a), variables significant: criterion holds in every region: False
--- reading (a), variables script: t75 range (min to max over 100 simulations), ms
ACC {'spatial attention': (11.0, 30.0), 'accept/reject': (232.0, 242.0), 'left/right value': (437.0, 492.0)}
   spatial attention below all others: True; left/right value above all others: True
DLPFC {'spatial attention': (70.0, 74.0), 'left/right value': (344.0, 380.0)}
   spatial attention below all others: True; left/right value above all others: True
OFC {'spatial attention': (26.0, 79.0), 'attended value': (-2.0, 262.0), 'accept/reject': (211.0, 270.0), 'stimulus identity': (262.0, 282.0)}
   spatial attention below all others: False; left/right value above all others: True
reading (a), variables script: criterion holds in every region: False
--- reading (b), variables significant: t75 range (min to max over 100 simulations), ms
ACC {'spatial attention': (11.0, 55.0), 'stimulus identity': (153.0, 327.0), 'accept/reject': (230.0, 281.0), 'left/right value': (262.0, 474.0)}
   spatial attention below all others: True; left/right value above all others: False
DLPFC {'spatial attention': (70.0, 81.0), 'stimulus identity': (-175.0, 350.0), 'acc
[... 163 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" dev.log | sed -n '/^script regression with permutations/,/total run time/p' | cut -c1-400 | sed -n 1,200p | python3 -c "
import sys
for l in sys.stdin:
    print(l.rstrip()[:400])
" | head -150
```

```
script regression with permutations: 106 s
                                         ACC value %  ACC action value %  ACC attribute value %  ACC spatial value %  DLPFC value %  DLPFC action value %  DLPFC attribute value %  DLPFC spatial value %  OFC value %  OFC action value %  OFC attribute value %  OFC spatial value %
regressors window          trials alpha
a          i               a      0.05          48.7                19.0                    5.8                  5.3           38.1                  18.7                     11.9                   11.9         47.0                10.4                   26.2                  6.6
                                  0.01          39.2                13.2                    1.1                  2.6           20.9                   7.5                      6.7                    8.2         36.6                 1.6                   13.7                  2.7
                           b      0.05          47.1                14.8                    4.8                  5.8           29.9                  16.4                     10.4                   11.2         44.8                 7.1                   20.2                  8.7
                                  0.01          33.9                10.6                    1.1                  3.2           21.6                   4.5                      6.7                    5.2         32.2                 1.6                   12.0                  1.6
           ii              a      0.05          47.6                19.0                    5.8                  4.8           21.6                  10.4                     11.2                    9.0         45.4                 6.0                   19.1                  6.6
                                  0.01          37.0                13.2                    1.1                  1.1           15.7                   4.5                      6.7                    3.0         36.6                 1.1         
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -A12 "Supplementary Figure 1 " paper/10.1038-s41593-018-0239-5.txt | head -40; grep -n -i -B2 -A8 "Supplementary Figure 5 " paper/10.1038-s41593-018-0239-5.txt | head -30; grep -n -i -A10 "Supplementary Figure 9 \|Figure S9\b" paper/10.1038-s41593-018-0239-5.txt | head -20; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 308,320p paper/10.1038-s41593-018-0239-5.txt; grep -n "Figure 7\b\|Fig. 7a\|Fig. 7 \|1.64\|uncorrected" paper/10.1038-s41593-018-0239-5.txt | head; sed -n 75,80p paper/10.1038-s41593-018-0239-5.txt | cut -c1-1500
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude/nbsrc.py'; s=open(p).read()
# fig6a per monkey
old='''# %% [markdown]
# RESULT:fig6a-acc-belief-subspace'''
new='''# %% tags=["claim:fig6a-acc-belief-subspace"]
for sb in ("M", "F"):
    for a in (1, 2, 3):
        M = belief_mat([u for u in SEL[a] if info.loc[u, "subject"] == sb], "t", "contrast")
        M = M[np.isfinite(M).all(1)]
        r = np.corrcoef(M.T)
        npos = sum(1 for i, j in zip(*iu5) if r[i, j] > 0 and stats.pearsonr(M[:, i], M[:, j])[1] < 0.05)
        print(f"monkey {sb}, {NAMES[a]} (n = {len(M)}): T-statistics, positive with p < 0.05 in {npos} of 10; "
              f"median r {np.median(r[iu5]):.3f}")

# %% [markdown]
# RESULT:fig6a-acc-belief-subspace'''
assert old in s; s=s.replace(old,new)
s=s.replace('''LAB6 = ["cue1 value", "EV13", "EV14", "EV15", "EV16"]''','''LAB6 = ["cue1 value", "EV13", "EV14", "EV15", "EV16"]
iu5 = np.triu_indices(5, 1)''')
# fig7 per monkey
old='''# %% [markdown]
# RESULT:fig7a-ofc-value-difference-neurons'''
new='''# %% tags=["claim:fig7a-ofc-value-difference-neurons"]
for sb in ("M", "F"):
    for o3, b in (("250", B250), ("300", B300)):
        fr = {a: [100 * passes([u for u in SEL5[a] if info.loc[u, "subject"] == sb], t, b, 1.96).mean()
                  for t in TESTS["a"]] for a in (1, 2, 3)}
        print(f"monkey {sb}, trial types (a), bin {o3}, p < 0.05: % ACC {np.round(fr[1], 1)}, DLPFC {np.round(fr[2], 1)},"
              f" OFC {np.round(fr[3], 1)}")

# %% [markdown]
# RESULT:fig7a-ofc-value-difference-neurons'''
assert old in s; s=s.replace(old,new)
old='''# %% [markdown]
# RESULT:fig7c-acc-belief-neurons'''
new='''# %% tags=["claim:fig7c-acc-belief-neurons"]
for sb in ("M", "F"):
    fr = {a: [100 * np.mean(np.abs(tst([u for u in SEL5[a] if info.loc[u, "subject"] == sb], ep, ev, B300)) > 1.96)
              for ep, ev in (("X2", 13), ("X2", 14), ("X3", 15), ("X3", 16))] for a in (1, 2, 3)}
    print(f"monkey {sb}, bin 300, p < 0.05: % ACC {np.round(fr[1], 1)}, DLPFC {np.round(fr[2], 1)}, OFC {np.round(fr[3], 1)}")

# %% [markdown]
# RESULT:fig7c-acc-belief-neurons'''
assert old in s; s=s.replace(old,new)
# fig8 per monkey after table
old='''def f8_all():'''
new='''print("by monkey, the script's reading (% significant: value, action, attribute, spatial):")
for sb in ("M", "F"):
    print(sb, {NAMES[a]: np.round(100 * SIG8[a][[info.loc[u, "subject"] == sb for u in SEL[a]]].mean(0), 1).tolist()
               for a in (1, 2, 3)})
def f8_all():'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
date -u
```

```
Sat Nov 14 19:13:14 UTC 2026
```

**Agent calls Bash**

```bash
sed -n 1,60p tools/entry.py | head -80; grep -n "def cmd_\|argparse\|add_parser" tools/entry.py | head -30; cat schemas/entry.schema.json | head -60
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "names the dataset\|unversioned\|crcns" tools/entry.py | head -20
```

```
20:- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
327:        # names the datasets it is about (docs/protocol.md, the attempt record).
```

**Agent calls Bash**

```bash
grep -n "def check_dataset_named\|def _dataset_refs\|version.*in text\|def check_names" tools/entry.py | head; grep -n -B3 -A30 "def check_dataset" tools/entry.py | head -60
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
sed -n 300,420p tools/entry.py
```

```
# A deprecated attempt no longer stands: its claims are being read again, and the claims file it was
        # tested on may already have been replaced (docs/pipeline.md), so it is not held to the current one.
        if attempt.get("deprecated"):
            continue
        known = lookup(claims_by_target, attempt)
        if lookup(labels_used, attempt):
            kinds = {f.get("kind") for f in attempt.get("findings") or []}
            if not attempt.get("inputs") or not kinds & {"metadata_insufficient", "identifier_missing"}:
                report.error(where, "claims take names for the dataset's codes from elsewhere (`with_labels`), so "
                                    "list the source under `inputs` and record the missing names as a finding "
                                    "(metadata_insufficient or identifier_missing)")
        if known is None:
            report.error(where, "no claims file for this paper")
            continue
        recorded = [o.get("claim") for o in attempt.get("outcomes", [])]
        # Claims read again since the attempt (a dataset added to its paper opens it again, and the checked claims
        # reach main ahead of the repeat attempt: the checkpoint in docs/pipeline.md) are the next attempt's to test.
        # Without this, main fails its own check from the checkpoint until that attempt merges, as it did for
        # kim-2022 on 2026-11-10, and every other attempt's pull request fails with it.
        reread = str(attempt.get("date") or "") < (lookup(claims_checked, attempt) or "")
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cat > entries/hunt-2018/requirements.in <<'EOF'
aiohttp
fsspec
h5py
matplotlib
numpy
pandas
requests
scipy
statsmodels
EOF
cat > /tmp/claude/build_nb.py <<'EOF'
"""Build the notebook from nbsrc.py (cells marked '# %%'), filling RESULT and CLAIMS_TABLE markers."""
import re, sys, json, nbformat, yaml
src = open("/tmp/claude/nbsrc.py").read()
texts = yaml.safe_load(open("/tmp/claude/results.yaml")) if len(sys.argv) > 1 else {}
cells = []
for block in re.split(r"^# %%", src, flags=re.M)[1:]:
    head, _, body = block.partition("\n")
    head = head.strip()
    if head.startswith("[markdown]"):
        lines = [l[2:] if l.startswith("# ") else l.lstrip("#") for l in body.strip("\n").split("\n")]
        text = "\n".join(lines).strip()
        m = re.fullmatch(r"RESULT:(\S+)", text)
        if m:
            text = texts.get(m.group(1), f"**Result: (pending)** {m.group(1)}")
        if "CLAIMS_TABLE" in text:
            text = text.replace("CLAIMS_TABLE", texts.get("CLAIMS_TABLE", ""))
        if "SUMMARY" in text:
            text = text.replace("SUMMARY", texts.get("SUMMARY", ""))
        cells.append(nbformat.v4.new_markdown_cell(text))
    else:
        tags = []
        m = re.search(r'tags=\[(.*?)\]', head)
        if m:
            tags = [t.strip().strip('"') for t in m.group(1).split(",")]
        c = nbformat.v4.new_code_cell(body.strip("\n"))
        if tags:
            c.metadata["tags"] = tags
        cells.append(c)
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, "entries/hunt-2018/reproduce_hunt_2018.ipynb")
print(len(cells), "cells")
EOF
cd $TMPDIR && . env/bin/activate && uv pip install -q nbformat pyyaml && python /tmp/claude/build_nb.py && date -u
```

```
149 cells
Sat Nov 14 19:13:34 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/hunt-2018 && python3 - <<'EOF'
p='pfc7.py'; s=open(p).read()
s=s.replace('''of attention and decision computations across prefrontal cortex", doi:10.1038/s41593-018-0239-5.
The data set (doi:10.6080/K0PZ5712)''','''of attention and decision computations across prefrontal cortex", doi:10.1038/s41593-018-0239-5.
The data set is CRCNS pfc-7 (crcns:pfc-7/unversioned; doi:10.6080/K0PZ5712); CRCNS data sets are
not versioned, so the files read are identified by the MD5 sums of its checksums.md5. It''')
open(p,'w').write(s)
EOF
head -12 pfc7.py; cd $TMPDIR && cp /tmp/claude/nbsrc.py full.py && . env/bin/activate && export MPLBACKEND=Agg PYTHONPATH=entries/hunt-2018 && /usr/bin/time -v python -u full.py > full.log 2>&1; grep -E "Maximum resident|Elapsed|Exit" full.log; tail -3 full.log
```

```
"""Loading and measures for CRCNS pfc-7 (Hunt, Malalasekera et al. 2018, Nature Neuroscience).

Hunt, Malalasekera, de Berker, Miranda, Farmer, Behrens & Kennerley (2018), "Triple dissociation
of attention and decision computations across prefrontal cortex", doi:10.1038/s41593-018-0239-5.
The data set is CRCNS pfc-7 (crcns:pfc-7/unversioned; doi:10.6080/K0PZ5712); CRCNS data sets are
not versioned, so the files read are identified by the MD5 sums of its checksums.md5. It is read anonymously from the public S3 bucket crcnsarchive,
under pfc-7/live/. Each file is read into memory and parsed there; nothing is written to disk.

What is read:

- behavioural_data/<Miles|Frank>_InfoGathering_All_Data.mat (MATLAB 7.3): per session, the
  completed option and attribute trials, with the cue values, the choice, the event codes and the
	Elapsed (wall clock) time (h:mm:ss or m:ss): 13:20.72
	Maximum resident set size (kbytes): 4367372
	Exit status: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && date -u && grep -v "^\s*$" full.log | sed -n '/RSA reading (a) with/,/between-region F/p;/^O9 reading (b)/,/between-region F/p' ; grep -v "^\s*$" full.log | grep -E "^O9|positive of 6|criterion:|permutation p" | cut -c1-300
```

```
Sat Nov 14 19:27:05 UTC 2026
RSA reading (a) with 10000 permutations: 99 s
                         T                     p_one                   p_two                      CPD                  
area                   ACC    DLPFC      OFC     ACC   DLPFC     OFC     ACC   DLPFC     OFC      ACC    DLPFC      OFC
template                                                                                                               
accept/reject      10.3000   4.3869   8.7141  0.0000  0.0101  0.0001  0.0000  0.0136  0.0001  21.2568   4.6684  16.1933
attended value      2.1924   0.7291   5.8642  0.0632  0.2724  0.0019  0.1264  0.5767  0.0022   1.2082   0.1351   8.0462
left/right value    6.0493   6.5065   0.0672  0.0073  0.0036  0.4059  0.0073  0.0036  0.9614   8.5182   9.7245   0.0011
spatial attention   7.8992  39.9022   4.5754  0.0028  0.0000  0.0181  0.0028  0.0000  0.0181  13.7017  80.2034   5.0573
stimulus identity   3.8517   4.4998  14.8158  0.0059  0.0020  0.0000  0.0111  0.0040  0.0000   3.6376   4.8998  35.8375
between-region F: {'stimulus identity': (np.float64(23.84), np.float64(0.0)), 'attended value': (np.float64(4.84), np.float64(0.029200000000000004)), 'accept/reject': (np.float64(14.43), np.float64(0.0016000000000000458)), 'spatial attention': (np.float64(348.53), np.float64(0.0)), 'left/right value': (np.float64(14.43), np.float64(0.0038000000000000256))}
O9 reading (b), trials with 3 or more cues:
                        T                     p_one                   p_two                      CPD                  
area                  ACC    DLPFC      OFC     ACC   DLPFC     OFC     ACC   DLPFC     OFC      ACC    DLPFC      OFC
template                                                                                                              
accept/reject      9.5741   3.9682   6.9427  0.0001  0.0142  0.0007  0.0001  0.0194  0.0007  18.9127   3.8525  10.9248
attended value     3.5392   2.0626   6.4313  0.0189  0.0810  0.0006  0.0301  0.1561  0
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" full.log | sed -n '/peak CPD (%) by template/,/reading (b), variables script: criterion/p' | cut -c1-400; grep -v "^\s*$" full.log | sed -n '/weights for 100/,/readings with all five/p' | grep -v "^\s*$" | head -40; grep -v "^\s*$" full.log | grep -E "readings where|readings with" ; grep -v "^\s*$" full.log | sed -n '/sign *$/,/readings where every/p' | awk '$NF==5'
```

```
peak CPD (%) by template and area: {'stimulus identity ACC': 5.8, 'stimulus identity DLPFC': 9.0, 'stimulus identity OFC': 45.4, 'attended value ACC': 6.7, 'attended value DLPFC': 2.5, 'attended value OFC': 12.9, 'accept/reject ACC': 34.2, 'accept/reject DLPFC': 13.8, 'accept/reject OFC': 15.0, 'spatial attention ACC': 56.7, 'spatial attention DLPFC': 84.0, 'spatial attention OFC': 34.4, 'left/rig
--- reading (a), variables significant: t75 range (min to max over 100 simulations), ms
ACC {'spatial attention': (4.0, 45.0), 'stimulus identity': (121.0, 342.0), 'accept/reject': (229.0, 272.0), 'left/right value': (252.0, 492.0)}
   spatial attention below all others: True; left/right value above all others: False
DLPFC {'spatial attention': (69.0, 75.0), 'stimulus identity': (-196.0, 433.0), 'accept/reject': (269.0, 537.0), 'left/right value': (319.0, 399.0)}
   spatial attention below all others: False; left/right value above all others: False
OFC {'spatial attention': (13.0, 93.0), 'stimulus identity': (261.0, 284.0), 'attended value': (-10.0, 286.0), 'accept/reject': (190.0, 442.0)}
   spatial attention below all others: False; left/right value above all others: True
reading (a), variables significant: criterion holds in every region: False
--- reading (a), variables script: t75 range (min to max over 100 simulations), ms
ACC {'spatial attention': (4.0, 45.0), 'accept/reject': (229.0, 272.0), 'left/right value': (252.0, 492.0)}
   spatial attention below all others: True; left/right value above all others: False
DLPFC {'spatial attention': (69.0, 75.0), 'left/right value': (319.0, 399.0)}
   spatial attention below all others: True; left/right value above all others: True
OFC {'spatial attention': (13.0, 93.0), 'attended value': (-10.0, 286.0), 'accept/reject': (190.0, 442.0), 'stimulus identity': (261.0, 284.0)}
   spatial attention below all others: False; left/right value above all others: True
reading (a), variables script: criterion holds in every region: False
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" full.log | sed -n '/rise1  rise2/,/readings where every/p' | head -60
```

```
rise1  rise2  rise3  rise4  rise5  peak1  peak2  peak3  peak4  peak5  n_ok
O4 O5     O6 O7 sign                                                                            
a  script a  a  a     0.399  0.240  0.545  0.531  0.283   -160   -140   -190   -180   -230     4
                b     0.193  0.124  0.259  0.273  0.136   -200   -140   -190   -180   -230     4
             b  a     0.282  0.172  0.387  0.376  0.200   -160   -140   -190   -180   -230     4
                b     0.137  0.089  0.184  0.193  0.096   -200   -140   -190   -180   -230     4
          b  a  a     0.035  0.018  0.047  0.050  0.034   -160   -210   -190   -160   -160     4
                b     0.018  0.009  0.021  0.026  0.015   -200   -210   -190   -160   -160     4
             b  a     0.025  0.013  0.033  0.035  0.024   -160   -210   -190   -160   -160     4
                b     0.012  0.006  0.015  0.018  0.010   -160   -210   -190   -160   -160     4
   a      a  a  a     0.321  0.234  0.483  0.455  0.415   -160   -190   -190   -170   -230     4
                b     0.160  0.117  0.252  0.226  0.203   -160   -200   -190   -180   -120     5
             b  a     0.227  0.163  0.343  0.326  0.292   -160   -190   -190   -170   -230     4
                b     0.113  0.083  0.179  0.162  0.144   -160   -200   -190   -180   -120     5
          b  a  a     0.028  0.018  0.040  0.045  0.040   -160   -210   -190   -170   -120     4
                b     0.015  0.009  0.020  0.022  0.019   -160   -210   -190   -170   -120     4
             b  a     0.020  0.012  0.028  0.032  0.029   -160   -210   -190   -170   -120     4
                b     0.010  0.006  0.014  0.016  0.013   -160   -210   -190   -170   -120     4
   b      a  a  a     0.394  0.173  0.462  0.534  0.369   -160   -200   -180   -220   -160     4
                b     0.197  0.101  0.237  0.264  0.173   -160   -200   -160   -220   -160     4
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" full.log | grep -E "^monkey|^by monkey|^M \{|^F \{|script regression|GLM fitted|units loaded|behaviour loaded|total run" | cut -c1-300; grep -n "Warning\|warn" full.log | head
```

```
behaviour loaded, 103 s
549 units loaded, 160 s, peak memory 3.9 GB
GLM fitted, 169 s
monkey M, mean npv250 by cue 1 rank (rows) and cue 2 rank (columns):
monkey M, ACC (n = 94): T-statistics, positive with p < 0.05 in 10 of 10; median r 0.395
monkey M, DLPFC (n = 37): T-statistics, positive with p < 0.05 in 0 of 10; median r 0.084
monkey M, OFC (n = 82): T-statistics, positive with p < 0.05 in 1 of 10; median r 0.021
monkey F, ACC (n = 95): T-statistics, positive with p < 0.05 in 7 of 10; median r 0.328
monkey F, DLPFC (n = 97): T-statistics, positive with p < 0.05 in 2 of 10; median r 0.107
monkey F, OFC (n = 101): T-statistics, positive with p < 0.05 in 0 of 10; median r 0.048
monkey M, trial types (a), bin 250, p < 0.05: % ACC [5.3 3.2 2.1], DLPFC [0.  2.7 0. ], OFC [6.2 6.2 8.6]
monkey M, trial types (a), bin 300, p < 0.05: % ACC [3.2 6.4 2.1], DLPFC [5.4 5.4 5.4], OFC [7.4 4.9 6.2]
monkey F, trial types (a), bin 250, p < 0.05: % ACC [5.3 3.2 7.4], DLPFC [2.1 2.1 3.1], OFC [5.9 3.  5. ]
monkey F, trial types (a), bin 300, p < 0.05: % ACC [3.2 3.2 6.3], DLPFC [3.1 2.1 3.1], OFC [4.  4.  6.9]
monkey M, bin 300, p < 0.05: % ACC [12.8 23.4 19.1  9.6], DLPFC [16.2 10.8  5.4 10.8], OFC [ 9.9  8.6 14.8  2.5]
monkey F, bin 300, p < 0.05: % ACC [20.  16.8 20.  12.6], DLPFC [ 8.2 13.4  7.2  5.2], OFC [4.  7.9 3.  1. ]
script regression with permutations: 95 s
by monkey, the script's reading (% significant: value, action, attribute, spatial):
M {'ACC': [51.1, 24.5, 2.1, 7.4], 'DLPFC': [43.2, 24.3, 0.0, 10.8], 'OFC': [62.2, 8.5, 14.6, 9.8]}
F {'ACC': [56.8, 16.8, 13.7, 10.5], 'DLPFC': [41.2, 15.5, 15.5, 17.5], 'OFC': [56.4, 4.0, 29.7, 5.9]}
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" full.log | sed -n "/script's measure/,/script measure M/p"
```

```
script's measure (mean over sessions of accuracy on seen values; mean |EV difference|):
                   acc     vd
subject npv250               
F       2       90.188  0.268
        3       82.631  0.227
        4       82.270  0.219
M       2       93.652  0.272
        3       85.196  0.239
        4       83.694  0.226
                  trials  accuracy  vd_true  vd_cues12
count  subject n                                      
npv    F       2    1230    78.939    0.305      0.241
               3    4119    74.068    0.249      0.175
               4    4514    76.341    0.227      0.155
       M       2     351    72.086    0.223      0.167
               3    5714    79.463    0.270      0.198
               4    8186    78.977    0.232      0.160
npv250 F       2    4638    74.955    0.266      0.198
               3    4790    76.103    0.229      0.153
               4     435    79.616    0.219      0.148
[... 10 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/results.yaml",
 "content": "CLAIMS_TABLE: |-\n  All 40 claims of the claims file are tested; none is blocked. Outcomes are in the summary at the end.\n\n  | Claim | Tested | Claim | Tested |\n  |---|---|---|---|\n  | sessions-and-trials | yes | fig5c-attribute-cue2-vs-cue1 | yes |\n  | neuron-counts | yes | fig5de-option-cue3-vs-stored | yes |\n  | choice-accuracy-ev | yes | fig5f-option-stored-combined | yes |\n  | chose-on-partial-information | yes | fig5gj-cross-correlation-dynamics | yes |\n  | choice-accuracy-observed | yes | fig5k-ofc-comparison-unique | yes |\n  | figs1ab-cue-weights | yes | figs67-no-comparison-acc-dlpfc | yes |\n  | figs1cd-fewer-cues-more-accurate | yes | fig6a-acc-belief-subspace | yes |\n  | fig2a-sample-the-favourite | yes | fig6b-acc-belief-stronger | yes |\n  | fig2b-positive-evidence | yes | fig6c-belief-subspace-rt | yes |\n  | fig4d-spatial-attention | yes | fig6d-belief-ramp-to-choice | yes |\n  | fig4e-ofc-stimulus-identity | yes | fig6e-action-subspace-ramp | yes |\n  | fig4f-ofc-attended-value | yes | fig7a-ofc-value-difference-neurons | yes |\n  | fig4g-left-right-value | yes | fig7b-ofc-value-difference-any | yes |\n  | fig4h-acc-accept-reject | yes | fig7c-acc-belief-neurons | yes |\n  | figs2-consistent-across-subjects | yes | fig8-cue1-value-all-regions | yes |\n  | figs4-dlpfc-top-bottom | yes | fig8-action-value-acc-dlpfc | yes |\n  | fig4-t75-latencies | yes | fig8-spatial-value-dlpfc | yes |\n  | figs5c-latency-order | yes | fig8-attribute-value-ofc | yes |\n  | fig5a-ofc-value-cpd | yes | figs9-ev16-correlation | yes |\n  | fig5b-stable-attended-value-subspace | yes | figs11-alternative-value-template | yes |\nsessions-and-trials: |-\n  **Result: reproduced.** The behavioural files hold 25 sessions of monkey F (Frank) and 32 of\n  monkey M (Miles), with 9,863 and 14,251 completed option and attribute trials, the paper's counts\n  exactly under reading (a). Reading (c) gives 9,479 and 13,691; reading (b) can be counted only for\n  the 24 and 29 sessions with units (10,688 and 14,391 trials there).\nneuron-counts: |-\n  **Result: reproduced, with the rate the paper's scripts use.** The data set holds 198 ACC, 156\n  DLPFC and 195 OFC units over 24 F and 29 M sessions, the totals and session counts the claims file\n  derives from Supplementary Table 1. With the `average_firing_rate` of `all_units_info.mat`, which\n  every figure script uses to select units, 189 ACC, 135 DLPFC and 183 OFC units are at or above\n  1 Hz, and 9, 21 and 12 are excluded, as the paper says. Neither of the claims file's readings\n  gives these counts: the whole-session rate gives 190, 136 and 182, the trial rate 186, 137 and 179.\n  The scripts also drop unit 87 (DLPFC), so the analyses here, as the paper's, use 134 DLPFC units.\nchoice-accuracy-ev: |-\n  **Result: reproduced.** With ties left out (reading a) F chose the higher expected value on\n  75.71% and M on 79.01% of trials, within 7.66 and 7.98 points of 76.6% and 79.8%. Counting the 384\n  and 560 tied trials as correct, as InfoGathering_Behaviour.m does, gives 76.66% and 79.83%.\nchose-on-partial-information: |-\n  **Result: reproduced.** With the script's joystick-corrected count, F chose before all four cues\n  on 85.52% and M on 71.43% of trials (paper 85.5% and 71.4%). The raw count of fixated pictures\n  gives 54.23% and 42.56%, so the correction for a joystick movement made before the last fixation\n  is what the paper's number counts.\nchoice-accuracy-observed: |-\n  **Result: reproduced.** Under reading (a), with the pictures seen as the script counts them\n  (`num_pics_viewed250`), accuracy is 86.00% for F and 87.75% for M, within 8.63 and 8.74 points of\n  86.3% and 87.4%. Readings (c) and the script's own measure also fall within tolerance (89.17/89.20\n  and 87.80/89.48); reading (b) gives 79.88/82.26.\nfigs1ab-cue-weights: |-\n  **Result: partially reproduced.** In model A every picture weight is positive with p < 0.05 in\n  both monkeys under both scales, and the first-side term on option trials is negative in both (F\n  b = -0.467, p = 1.5e-07; M b = -1.220, p = 2.7e-54, seen values). Equal weighting of probability\n  and magnitude fails in M: the ratio is 1.11 on option and 1.13 on attribute trials, the 95% CIs do\n  not overlap and the Wald test gives p = 1.1e-06 and 4.1e-07; with true values the ratios are 1.11\n  and 1.15 and the attribute CIs do not overlap. In F the CIs overlap on both trial types. The n-2\n  weight (F 1.186, M 1.161 on ranks) is below the n-1 weight (1.347, 1.229), so the slight\n  upweighting of the antepenultimate cue is not seen against n-1; it is above the final weight.\nfigs1cd-fewer-cues-more-accurate: |-\n  **Result: not reproduced.** With the claims file's measure (higher true expected value, ties left\n  out) and the script's count of pictures, accuracy on 2-picture trials is not the highest: F 74.96%\n  against 76.10% and 79.62% on 3 and 4 pictures, M 78.83% against 78.79% and 81.51%. The mean value\n  difference is largest on 2-picture trials in both monkeys (F 0.266 against 0.229 and 0.219). With\n  the script's own measure (accuracy on the seen values, averaged over sessions) the claim holds in\n  both monkeys (F 90.19% against 82.63% and 82.27%; M 93.65% against 85.20% and 83.69%). The measure\n  is asked of a reader.\nfig2a-sample-the-favourite: |-\n  **Result: reproduced.** On attribute trials with a third picture, the third saccade returned to\n  the first option on 59.8% (F) and 86.7% (M) of trials when cue 1 outranked cue 2, against 8.7% and\n  10.0% when it did not (chi-square p = 1.5e-230 and p < 1e-300); the logistic slopes are 0.729 and\n  1.210 (both p < 1e-189).\nfig2b-positive-evidence: |-\n  **Result: reproduced.** On option trials with both cues at rank +2 F sampled 2.05 and M 2.22\n  pictures on average, against 2.69 and 3.15 with both at -2 (script count; raw count 2.47/3.06\n  against 3.54/3.86), and the Spearman correlation with the summed rank is negative in each monkey\n  and pooled (rho -0.356, -0.499, -0.434, all p < 1e-143).\nfig4d-spatial-attention: |-\n  **Result: reproduced.** The spatial attention template is significant in DLPFC (T = 39.90,\n  permutation p < 0.0001), OFC (T = 4.58, p = 0.018) and ACC (T = 7.90, p = 0.0028), and its CPD is\n  largest in DLPFC (80.2% against 13.7% in ACC and 5.1% in OFC); the between-region F is 348.5 (p <\n  0.0001). All four readings of O8 and O9 agree.\nfig4e-ofc-stimulus-identity: |-\n  **Result: reproduced.** Stimulus identity is significant in OFC (T = 14.82, p < 0.0001) with a\n  CPD of 35.8% against 3.6% (ACC) and 4.9% (DLPFC), under all four readings.\nfig4f-ofc-attended-value: |-\n  **Result: reproduced.** Attended value is significant in OFC (T = 5.86, one-sided p = 0.0019) with\n  a CPD of 8.05% against 1.21% (ACC) and 0.14% (DLPFC), under all four readings.\nfig4g-left-right-value: |-\n  **Result: reproduced.** Left/right value is significant in ACC (T = 6.05, p = 0.0073) and DLPFC\n  (T = 6.51, p = 0.0036) and absent in OFC (T = 0.07), with CPDs of 8.5% and 9.7% against 0.0%,\n  under all four readings.\nfig4h-acc-accept-reject: |-\n  **Result: reproduced.** Accept/reject is significant in ACC (T = 10.30, p < 0.0001) with a CPD of\n  21.3% against 4.7% in DLPFC, and it exceeds the attended value CPD in ACC (1.2%; reading a); the\n  attended value template is not significant in ACC with all trials (p = 0.063) but is with 3 or\n  more cues (p = 0.019). In OFC accept/reject has T = 8.71 and a CPD of 16.2%.\nfigs2-consistent-across-subjects: |-\n  **Result: reproduced.** In each monkey all six coefficients are positive under both trial\n  readings (smallest 0.014, left/right value in ACC of F with 3 or more cues).\nfigs4-dlpfc-top-bottom: |-\n  **Result: reproduced.** In the 40-condition matrices, pairs in the same quadrant are more similar\n  than pairs on the same side in different rows by 0.112 in DLPFC, against 0.042 in ACC and -0.001\n  in OFC (a label-permutation reference, not part of the criterion, gives p < 0.001, 0.022 and 0.46).\nfig4-t75-latencies: |-\n  **Result: reproduced.** With the sliding RSA at every 1 ms (reading b), all nine t75 values equal\n  the paper's to the millisecond (24, 72, 67, 269, 241, 238, 224, 457 and 369 ms) over -100 to 500\n  ms, and over -200 to 600 ms. With a 10 ms step all nine are within tolerance over -100 to 500 ms.\nfigs5c-latency-order: |-\n  **Result: partially reproduced.** The point estimates follow the paper's order (above), but the\n  simulated t75 distributions overlap under every reading and either set of variables. In OFC the\n  attended value range reaches down to -10 ms, below the top of the spatial attention range (93 ms);\n  in ACC the left/right value range (252 to 492 ms) overlaps accept/reject (229 to 272 ms) under the\n  script's permutation (reading b, 9 to 93 ms spatial). Spatial attention is below every other kept\n  variable in ACC and DLPFC, and left/right value above the others in DLPFC, with the script's set.\nfig5a-ofc-value-cpd: |-\n  **Result: reproduced.** The mean OFC CPD of each cue's value peaks 290, 300 and 290 ms after the\n  cue's own onset (reading a), and the cue 1 and cue 2 value CPDs stay above either baseline at every\n  bin of the later cue epochs (epoch means 0.18 to 0.52 points above baseline).\nfig5b-stable-attended-value-subspace: |-\n  **Result: reproduced.** In OFC the cue 1 value T-statistics at cue 1 correlate with the cue 2\n  value T-statistics at cue 2, r = 0.845 (p = 7.7e-51, n = 182; reading a r = 0.843), in each monkey\n  (r = 0.860 and 0.809).\nfig5c-attribute-cue2-vs-cue1: |-\n  **Result: reproduced.** In OFC at cue 2 of attribute trials, EV 6 and EV 5 correlate negatively,\n  r = -0.270 (p = 0.00023, n = 182); M r = -0.236, F r = -0.356.\nfig5de-option-cue3-vs-stored: |-\n  **Result: reproduced.** In OFC at cue 3 of option trials, EV 3 correlates negatively with EV 1\n  (r = -0.283, p = 0.00011) and with EV 2 (r = -0.379, p = 1.3e-07).\nfig5f-option-stored-combined: |-\n  **Result: reproduced.** At cue 3 of option trials EV 1 and EV 2 correlate positively in OFC (r =\n  0.523, p = 3.4e-14); at cue 2 they do not (r = -0.033, p = 0.66), as the Discussion says.\nfig5gj-cross-correlation-dynamics: |-\n  **Result: reproduced.** Each of the four maps has a cluster through the 250 ms point of its cue,\n  of the expected sign and larger than the 99.9th percentile of 1000 permutations (884, 1839, 1105\n  and 817 bins against thresholds of 500 to 584), and EV 6 at cue 2 with EV 5 at cue 1 forms a\n  positive cluster (r = 0.755 at 250, 250 ms; 1622 bins).\nfig5k-ofc-comparison-unique: |-\n  **Result: reproduced.** All six OFC correlations are more negative than the DLPFC and ACC ones,\n  and the two-sided Fisher tests give p = 0.040, 0.067, 0.011 (DLPFC) and 0.0032, 0.0003, < 0.0001\n  (ACC), the paper's values; five of six are below 0.05, as in the paper.\nfigs67-no-comparison-acc-dlpfc: |-\n  **Result: reproduced.** The attended value subspace is present in ACC (r = 0.852) and DLPFC (r =\n  0.658) and the stored subspaces correlate at cue 3 (r = 0.559 and 0.519), all p < 1e-9; none of the\n  attended-against-stored correlations is negative with p < 0.05 (ACC r = 0.031 to 0.084, DLPFC\n  r = -0.105 to -0.040, smallest p 0.23).\nfig6a-acc-belief-subspace: |-\n  **Result: reproduced.** With T-statistics all 10 ACC correlations are positive with p < 0.05 (r =\n  0.165 to 0.483), against 3 of 10 in DLPFC and 2 of 10 in OFC. With OLS coefficients ACC has 8 of 10.\n  By monkey, ACC has 10 of 10 in M and 7 of 10 in F.\nfig6b-acc-belief-stronger: |-\n  **Result: reproduced.** The ACC correlation is the larger in 19 of 20 comparisons, and 13 of 20\n  are significant by the two-sided Fisher test (16 one-sided).\nfig6c-belief-subspace-rt: |-\n  **Result: reproduced.** In all 24 combinations of readings the belief projection is higher for\n  the shortest than for the longest RT bin over 100-500 ms and 0-500 ms after cue 1 (for example\n  0.445 z-units with odd/even halves, the scripts' bins and rates in Hz), and with 100 random halves\n  in 98 to 100 of the splits.\nfig6d-belief-ramp-to-choice: |-\n  **Result: reproduced.** In all 24 combinations the belief projection is higher over -200 to 0 ms\n  than over -500 to -300 ms before the response in each of the five RT bins.\nfig6e-action-subspace-ramp: |-\n  **Result: reproduced, under 2 of 48 readings.** The action projection rises before the response\n  in every RT bin under all 48 readings. Its peak falls between -200 and 100 ms in all five bins only\n  with odd/even halves, per-session quintiles, rates in Hz and the signed average (either O7); in the\n  other readings one or two bins peak 10 to 70 ms earlier (for example -230 ms in the longest bin\n  with the scripts' choices).\nfig7a-ofc-value-difference-neurons: |-\n  **Result: partially reproduced.** No single reading of the bin and trial types gives OFC the\n  largest proportion at all three tests at both thresholds the criterion requires: at 250 ms it\n  holds at p < 0.05 (OFC 6.0, 4.4, 6.6% against at most 5.3, 3.2, 4.8%) but not at p < 0.01, and at\n  300 ms the reverse. With the script's threshold (|T| > 1.64) it holds at both bins. No pairwise\n  chi-square test reaches p < 0.05 except one (0.015). The threshold is asked of a reader.\nfig7b-ofc-value-difference-any: |-\n  **Result: reproduced.** With the Figure 5 trial types, the fraction passing any of the three\n  tests is highest in OFC at both bins and every threshold (for example 11.5% against 9.0% in ACC and\n  6.0% in DLPFC at 250 ms, p < 0.05).\nfig7c-acc-belief-neurons: |-\n  **Result: reproduced.** ACC has the largest proportion for all four belief confirmation EVs at\n  both bins and both thresholds (at 300 ms, p < 0.05: 16.4, 20.1, 19.6, 11.1% against at most 10.4,\n  12.7, 8.2, 6.7%).\nfig8-cue1-value-all-regions: |-\n  **Result: reproduced.** Under all 24 readings and the script's own regression, the fraction\n  encoding cue 1 value is above chance with binomial p < 1e-7 in every region (script: ACC 54.0%,\n  DLPFC 41.8%, OFC 59.0%).\nfig8-action-value-acc-dlpfc: |-\n  **Result: partially reproduced.** The tests hold under several readings, the script's included\n  (ACC 20.6% and DLPFC 17.9%, binomial p = 2e-14 and 3e-08, both above OFC by chi-square p = 6.8e-05\n  and 0.0016, OFC 6.0% at chance, p = 0.41), but in no reading are both fractions within 18 +/- 1.8%\n  with the tests holding: ACC is 20.6% in the script's reading, and where both fall within tolerance\n  (19.0 and 18.7%, reading a, i, all trials, p < 0.05) OFC is above chance (10.4%, p = 0.0018).\nfig8-spatial-value-dlpfc: |-\n  **Result: reproduced, under 2 of 24 readings.** With the full model, the 100-500 ms window, all\n  trials and p < 0.01, DLPFC spatial value (8.2%, binomial p = 3e-08) equals action value (7.5%,\n  chi-square p = 1), while in ACC spatial value (2.6%) is below action value (13.2%, p = 0.0003); the\n  same holds with the value-only model. In the script's reading the DLPFC binomial p is 2e-06, above\n  the 1e-6 bound, with spatial 15.7% and action 17.9% (p = 0.74) and ACC 9.0% against 20.6% (p =\n  0.0024).\nfig8-attribute-value-ofc: |-\n  **Result: reproduced.** In the script's reading 23.0% of OFC neurons encode attribute value\n  (binomial p = 3e-17), more than ACC (7.9%, chi-square p = 0.00011) and DLPFC (11.2%, p = 0.011);\n  readings with the full model at p < 0.05 give 23.0 to 26.2%.\nfigs9-ev16-correlation: |-\n  **Result: reproduced.** Averaged over neurons on trials with 3 or more cues (reading b), the mean\n  r2 of EV 16 is 0.180 with EV 7 and 0.190 with EV 9, within tolerance of 0.167 and 0.194, and the\n  largest other pair among EVs 1-6 and 13-18 is 0.046. Averaged over sessions the values are 0.190\n  and 0.204, the first outside tolerance.\nfigs11-alternative-value-template: |-\n  **Result: reproduced.** With the uniform-diagonal templates, attended value is significant in OFC\n  (T = 3.31, p = 0.0021) with the largest CPD (2.72% against 0.37% and 0.29%), and left/right value\n  is significant in ACC and DLPFC (T = 6.75 and 6.56) and absent in OFC (T = -0.01), under all four\n  readings.\nSUMMARY: |-\n  A failure to reproduce here may be a failure of this attempt, not of the paper: see the\n  reasoning and the differences from the paper's method.\n\n  | Claim | Outcome |\n  |---|---|\n  | sessions-and-trials | reproduced |\n  | neuron-counts | reproduced |\n  | choice-accuracy-ev | reproduced |\n  | chose-on-partial-information | reproduced |\n  | choice-accuracy-observed | reproduced |\n  | figs1ab-cue-weights | partially reproduced |\n  | figs1cd-fewer-cues-more-accurate | not reproduced |\n  | fig2a-sample-the-favourite | reproduced |\n  | fig2b-positive-evidence | reproduced |\n  | fig4d-spatial-attention | reproduced |\n  | fig4e-ofc-stimulus-identity | reproduced |\n  | fig4f-ofc-attended-value | reproduced |\n  | fig4g-left-right-value | reproduced |\n  | fig4h-acc-accept-reject | reproduced |\n  | figs2-consistent-across-subjects | reproduced |\n  | figs4-dlpfc-top-bottom | reproduced |\n  | fig4-t75-latencies | reproduced |\n  | figs5c-latency-order | partially reproduced |\n  | fig5a-ofc-value-cpd | reproduced |\n  | fig5b-stable-attended-value-subspace | reproduced |\n  | fig5c-attribute-cue2-vs-cue1 | reproduced |\n  | fig5de-option-cue3-vs-stored | reproduced |\n  | fig5f-option-stored-combined | reproduced |\n  | fig5gj-cross-correlation-dynamics | reproduced |\n  | fig5k-ofc-comparison-unique | reproduced |\n  | figs67-no-comparison-acc-dlpfc | reproduced |\n  | fig6a-acc-belief-subspace | reproduced |\n  | fig6b-acc-belief-stronger | reproduced |\n  | fig6c-belief-subspace-rt | reproduced |\n  | fig6d-belief-ramp-to-choice | reproduced |\n  | fig6e-action-subspace-ramp | reproduced |\n  | fig7a-ofc-value-difference-neurons | partially reproduced |\n  | fig7b-ofc-value-difference-any | reproduced |\n  | fig7c-acc-belief-neurons | reproduced |\n  | fig8-cue1-value-all-regions | reproduced |\n  | fig8-action-value-acc-dlpfc | partially reproduced |\n  | fig8-spatial-value-dlpfc | reproduced |\n  | fig8-attribute-value-ofc | reproduced |\n  | figs9-ev16-correlation | reproduced |\n  | figs11-alternative-value-template | reproduced |\n\n  How the analysis differs from the paper's. The data are the authors' preprocessed units and\n  behavioural files of the data set, not the raw recordings. Where the claims file names readings,\n  each was run, and the paper's scripts (files of the data set) settled the rest: the unit selection\n  (the stored mean rate, unit 87 dropped, unit 653 dropped for Figures 5 and 7), the count of pictures\n  viewed (joystick-corrected), the RSA conditions and permutation test, the projection design and\n  reaction-time bins, and the cue 1 regression shown as a further reading for Figure 8. The GLM\n  written here gives the T-statistics the authors stored in the data set to within 1.6e-06. The\n  Figure 6 traces are not cut at each bin's longest reaction time, as the script does for plotting;\n  the windows the criteria use lie before those cuts.\n\n  What was found about the data set. Its files hold what the paper describes: 25 and 32 behavioural\n  sessions with the paper's trial counts, 549 units in the three regions over 24 and 29 sessions,\n  every unit file agreeing with the units table on subject, session, channel and area, and the\n  rasters on the clock of the trial events (the cue 1 value code rises after cue 1 and vanishes when\n  trial labels are shifted by one trial). The mean rate that selects units (`average_firing_rate` in\n  `all_units_info.mat`) is not documented and is not the whole-session or trial rate; the units of\n  session M049 onwards (unit files 681 to 724) store the subject as \"m\" where all others store \"M\";\n  and the data descriptor names the preprocessed folder `LTH_preprocessed_data` while the archive\n  holds `LTH_processed_data.zip`.\n"
}
```

```
File created successfully at: /tmp/claude/results.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -E "^EV|criterion holds" full.log; grep -E "^\('script',\)" full.log | cut -c1-250; . env/bin/activate; PYTHONPATH=entries/hunt-2018 python -c "
import pfc7; i=pfc7.units_info(); print(i.loc[681:724].groupby(['subject','session']).size())"
```

```
O9 (a) O8 one-sided: CPD % ACC 13.70, DLPFC 80.20, OFC 5.06; p ACC/DLPFC/OFC [0.0028, 0.0, 0.0181]; F p = 0.0000 -> criterion holds: True
O9 (a) O8 two-sided: CPD % ACC 13.70, DLPFC 80.20, OFC 5.06; p ACC/DLPFC/OFC [0.0028, 0.0, 0.0181]; F p = 0.0000 -> criterion holds: True
O9 (b) O8 one-sided: CPD % ACC 13.89, DLPFC 78.93, OFC 2.97; p ACC/DLPFC/OFC [0.0038, 0.0, 0.0324]; F p = 0.0000 -> criterion holds: True
O9 (b) O8 two-sided: CPD % ACC 13.89, DLPFC 78.93, OFC 2.97; p ACC/DLPFC/OFC [0.0038, 0.0, 0.0331]; F p = 0.0000 -> criterion holds: True
reading (a), variables significant: criterion holds in every region: False
reading (a), variables script: criterion holds in every region: False
reading (b), variables significant: criterion holds in every region: False
reading (b), variables script: criterion holds in every region: False
EV6 (X2) x EV5 (X2): r at (250, 250) = -0.270; cluster there of 884 bins, threshold 577; significant with the expected sign: True
EV2 (X3) x EV1 (X3): r at (250, 250) = 0.523; cluster there of 1839 bins, threshold 500; significant with the expected sign: True
EV3 (X3) x EV1 (X3): r at (250, 250) = -0.283; cluster there of 1105 bins, threshold 577; significant with the expected sign: True
EV3 (X3) x EV2 (X3): r at (250, 250) = -0.379; cluster there of 817 bins, threshold 584; significant with the expected sign: True
EV6 (cue 2) x EV5 (cue 1): r at (250, 250) = 0.755; cluster 1622 bins, threshold 580; significant positive: True
criterion holds: True
('script',) {'ACC': '54.0% p=5e-81', 'DLPFC': '41.8% p=1e-37', 'OFC': '59.0% p=2e-91'} holds: True
('script',) ACC 20.6% (binom p=2e-14, chi2 vs OFC p=6.8e-05), DLPFC 17.9% (p=3e-08, chi2 p=0.0016), OFC 6.0% (p=0.41); tests hold True, within 18 +/- 1.8 False
('script',) DLPFC spatial 15.7% (binom p=2e-06) vs action 17.9% (chi2 p=0.74); ACC spatial 9.0% vs action 20.6% (chi2 p=0.0024) -> holds False
('script',) OFC 23.0% (binom p=3e-17); ACC 7.9% (chi2 p=0.00011); DLPFC 11.2% (chi2 p=0.011); tests 
[... 7 more lines not kept]
```

**Agent**

Now apply the text fixes and build the notebook.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude/results.yaml'; s=open(p).read()
rep=[("the units of\n  session M049 onwards (unit files 681 to 724) store the subject as \"m\" where all others store \"M\";",
      "unit files 681 to 724\n  (sessions 5, 11, 23 and 27 of M) store the subject as \"m\" where all others store \"M\";"),
("(chi-square p = 1.5e-230 and p < 1e-300); the logistic slopes are 0.729 and\n  1.210 (both p < 1e-189).",
 "(chi-square p = 1.5e-230, and printed as 0 for M); the logistic slopes are 0.729 and\n  1.210 (p = 3.3e-190, and printed as 0)."),
("(for example\n  0.445 z-units with odd/even halves, the scripts' bins and rates in Hz)",
 "(for example\n  a difference of 0.445 with odd/even halves, the scripts' bins and rates in Hz)"),
("in the\n  other readings one or two bins peak 10 to 70 ms earlier (for example -230 ms in the longest bin\n  with the scripts' choices).",
 "in the\n  other readings one or two bins peak 10 to 70 ms earlier (for example -230 ms in the longest bin\n  with odd/even halves and the scripts' bins, -270 ms in the fourth bin with the scripts' random\n  halves, bins and z-scored rates)."),
("No pairwise\n  chi-square test reaches p < 0.05 except one (0.015). The threshold is asked of a reader.",
 "At 250 ms and\n  p < 0.05 none of the six pairwise chi-square tests is below 0.05 (smallest p = 0.084). The\n  threshold is asked of a reader."),
("readings with the full model at p < 0.05 give 23.0 to 26.2%.",
 "the full model on all trials at p < 0.05 gives 26.2%, 19.1% and 24.0% in the three windows."),
("in ACC the left/right value range (252 to 492 ms) overlaps accept/reject (229 to 272 ms) under the\n  script's permutation (reading b, 9 to 93 ms spatial).",
 "in ACC, with the script's shared permutation (reading b), left/right value (246 to 528 ms)\n  overlaps accept/reject (227 to 291 ms)."),
]
for a,b in rep:
    assert a in s, a[:40]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && python /tmp/claude/build_nb.py x && grep -c "pending" entries/hunt-2018/reproduce_hunt_2018.ipynb; date -u
```

```
149 cells
0
Sat Nov 14 19:29:48 UTC 2026
Shell cwd was reset to
```

**Agent**

Now entry.yaml, README, then lock and run.

**Agent calls Bash**

```bash
cat > entries/hunt-2018/entry.yaml <<'EOF'
schema_version: 1
name: hunt-2018
type: reproduction
title: Attention and decision computations across prefrontal cortex (Hunt, Malalasekera et al. 2018)
description: Tests the findings of Hunt, Malalasekera et al. (2018) on CRCNS data set pfc-7, which
  holds the behaviour of two macaques in an information sampling task and single units from ACC,
  DLPFC and OFC. It covers the behaviour, the representational similarity analysis at cue 1, the
  value comparison subspaces in OFC, the belief confirmation and action subspaces in ACC, and the
  single-neuron analyses, all from the data set's preprocessed units and behavioural files.
license: Apache-2.0
notebooks:
- path: reproduce_hunt_2018.ipynb
  title: Reproducing Hunt, Malalasekera et al. (2018) from CRCNS pfc-7
  runtime_minutes: 14
helpers:
- pfc7.py
related:
- id: crcns:pfc-7/unversioned
  relation: uses_data
- id: doi:10.1038/s41593-018-0239-5
  relation: reproduces
EOF
cat > entries/hunt-2018/README.md <<'EOF'
# Hunt, Malalasekera et al. (2018) from CRCNS pfc-7

Tests the findings of [Hunt, Malalasekera et al. (2018)](https://doi.org/10.1038/s41593-018-0239-5)
on CRCNS data set [pfc-7](https://doi.org/10.6080/K0PZ5712): the behaviour of two macaques in an
information sampling task (25 and 32 sessions) and 549 single units from ACC, DLPFC and OFC. All 40
claims of the claims file are tested; 33 are reproduced, 5 partially reproduced and 1 not
reproduced, and 1 is reproduced under the paper's scripts' unit selection (neuron-counts).

| Claim | Outcome |
|---|---|
| Sessions and trial counts | Reproduced |
| Neuron counts after the 1 Hz exclusion | Reproduced |
| Choice accuracy, on expected value and on the pictures seen; early choices | Reproduced |
| Logistic regressions of choice (Supplementary Figure 1a/b) | Partially reproduced |
| More accurate on 2-picture trials (Supplementary Figure 1c/d) | Not reproduced |
| Information sampling (Figure 2a/b) | Reproduced |
| RSA templates at cue 1 (Figure 4d-h, Supplementary Figures 2, 4, 11) | Reproduced |
| t75 latencies (Figure 4) | Reproduced |
| Latency order from simulations (Supplementary Figure 5c) | Partially reproduced |
| OFC value comparison subspaces (Figure 5a-k, Supplementary Figures 6, 7) | Reproduced |
| ACC belief confirmation and action subspaces (Figure 6) | Reproduced |
| Single-neuron value difference in OFC at each test (Figure 7a) | Partially reproduced |
| Single-neuron value difference collapsed, belief confirmation (Figure 7b/c) | Reproduced |
| Cue 1 single-neuron coding (Figure 8): value, spatial value, attribute value | Reproduced |
| Cue 1 action value in about 18% of ACC and DLPFC neurons (Figure 8) | Partially reproduced |
| EV 16 correlation (Supplementary Figure 9) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's MATLAB scripts are files of the data set; where the claims file leaves a detail open
and a script settles it, the analysis follows the script and says so. The GLM written here gives the
T-statistics the authors stored in the data set to within 1.6e-06. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/hunt-2018-01.yaml`](../../attempts/hunt-2018-01.yaml).

- `reproduce_hunt_2018.ipynb`: the analysis. It takes about 14 minutes, a third of it streaming
  the files (about 3 GB, read into memory one file at a time).
- `pfc7.py`: loading the behavioural files and the preprocessed units, and the GLM, RSA and
  regression measures of the paper's scripts. Other notebooks on this data set can import it.
EOF
python tools/entry.py lock entries/hunt-2018 2>&1 | tail -5; date -u
```

```
wrote hunt-2018/requirements.lock.txt (Python 3.13, with hashes)
Sat Nov 14 19:30:02 UTC 2026
```

**Agent calls Bash**

```bash
sed -i 's/claims of the claims file are tested; 33 are reproduced, 5 partially reproduced and 1 not\nreproduced/X/' entries/hunt-2018/README.md && python3 - <<'EOF'
p='entries/hunt-2018/README.md'; s=open(p).read()
s=s.replace("""claims of the claims file are tested; 33 are reproduced, 5 partially reproduced and 1 not
reproduced, and 1 is reproduced under the paper's scripts' unit selection (neuron-counts).""","""claims of the claims file are tested: 35 are reproduced, 4 partially reproduced and 1 not
reproduced.""")
open(p,'w').write(s)
EOF
grep -n "35 are" entries/hunt-2018/README.md; timeout 7000 python tools/entry.py all entries/hunt-2018 2>&1 | tail -20; date -u
```

```
6:claims of the claims file are tested: 35 are reproduced, 4 partially reproduced and 1 not
Installed kernelspec registry-hunt-2018 in executed/hunt-2018/.venv/share/jupyter/kernels/registry-hunt-2018
0 error(s)
pass  reproduce_hunt_2018.ipynb  (787 s)
Sat Nov 14 19:43:23 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/hunt-2018 && ls -la && python3 - <<'EOF'
import nbformat
nb=nbformat.read('reproduce_hunt_2018.ipynb',4)
out=[]
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream': out.append(o['text'])
            elif 'data' in o and 'text/plain' in o['data']: out.append(o['data']['text/plain'])
txt="\n".join(out)
open('/tmp/claude/exec.txt','w').write(txt)
EOF
cd $TMPDIR && python3 - <<'EOF'
import re
a=open('/tmp/claude/exec.txt').read(); b=open('full.log').read()
def lines(t): return [l.strip() for l in t.splitlines() if l.strip() and not re.search(r'\d+ s\b|min, peak|loaded|fitted|permutations: |halves: |combinations: ', l)]
la, lb = lines(a), lines(b)
sa=set(la); diff=[l for l in lb if l not in sa and not l.startswith(('Command','User time','System time','Percent','Elapsed','Average','Maximum','Major','Minor','Voluntary','Involuntary','Swaps','File system','Socket','Signals','Page size','Exit'))]
print(len(lb), len(diff)); print("\n".join(diff[:30]))
EOF
```

```
total 776
drwxr-xr-x 3 runner runner   4096 Nov 14 19:43 .
drwxr-xr-x 3 runner runner   4096 Nov 14 19:30 ..
-rw-r--r-- 1 runner runner    312 Nov 14 19:43 .clean-run.json
drwxr-xr-x 5 runner runner   4096 Nov 14 19:30 .venv
-rw-r--r-- 1 runner runner 772358 Nov 14 19:43 reproduce_hunt_2018.ipynb
-rw-r--r-- 1 runner runner    166 Nov 14 19:43 result.json
701 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required')); 
for k,v in s['properties'].items(): print(k, json.dumps(v)[:300])
" | head -60; ls questions | grep -i hunt
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
schema_version {"const": 3}
id {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}
datasets {"description": "Every dataset the attempt used (docs/protocol.md, \"Record the attempt\").", "type": "array", "minItems": 1, "items": {"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.", "type": "object", "a
missing_datasets {"description": "Datasets the paper's claims rest on that this attempt could not use; claims that need one are blocked with dataset_missing.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["why"], "properties": {"archive": {"type": "string"}, "id": {"type":
paper {"type": "string", "pattern": "^doi:10\\.[0-9]{4,9}/.+$"}
date {"type": "string", "format": "date"}
entry {"description": "The entry this attempt produced (its name), if any.", "type": "string"}
deprecated {"description": "Set when the attempt no longer stands, for example because its claims were written without the paper's full text. The record is kept as it was; its outcomes are shown but not counted.", "type": "object", "additionalProperties": false, "required": ["date", "reason"], "properties": {"
provenance {"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"
outcomes {"description": "One per claim attempted.", "type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["claim", "outcome"], "properties": {"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reprodu
verifications {"type": "array", "items": {"type": "object", "additio
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties']['datasets']['items'],indent=0)[:1200]); print(json.dumps(s['properties']['outcomes']['items']['properties'],indent=0)[:2500]); print(json.dumps(s['properties']['findings']['items'],indent=0)[:1500]); print(json.dumps(s['properties']['provenance'],indent=0)[:1500])"; head -30 questions/README.md
```

```
{
"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.",
"type": "object",
"additionalProperties": false,
"required": [
"archive",
"id",
"version",
"relation"
],
"properties": {
"archive": {
"description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.",
"type": "string",
"pattern": "^[a-z][a-z0-9-]*$"
},
"id": {
"description": "The dataset's identifier in that archive, e.g. 000003 on DANDI.",
"type": "string",
"minLength": 1
[... 259 more lines not kept]
```

**Agent calls Bash**

```bash
head -5 questions/asari-2009.yaml; grep -n "^[a-z_]*:" questions/asari-2009.yaml | head; grep -rn "questions" tools/entry.py | head -5
```

```
questions:
- claim: fig2-example-long-context
  question: The criterion says the example cell and probe are not identified and accepts any
    current-clamp cell with seven natural sound fragments and a probe tested after silence and
    two other fragments. Does the Figure 2 legend identify them? Figure 2A gives the cell's
1:questions:
```

**Agent calls Write**

```json
{
 "file_path": "questions/hunt-2018.yaml",
 "content": "questions:\n- claim: figs1cd-fewer-cues-more-accurate\n  question: The criterion measures accuracy as the choice of the higher true expected value (as\n    choice-accuracy-ev, reading a). The paper's script for Supplementary Figure 1c\n    (InfoGathering_Behaviour.m, `out.accuracyNPV`, plotted by Fig1_2_S1_behaviour.m) judges each\n    choice on the expected values of the pictures seen (unseen pictures at 0.5, the same measure as\n    the reported 86.3% and 87.4%), per session, and averages over sessions. Should the criterion\n    use that measure?\n  passage: 'Supplementary Figure 1 legend, \"(C) Subjects paradoxically were more likely to choose\n    optimally, on average, on trials where 2 pictures were viewed rather than 3 or 4 pictures. (D)\n    This effect can be straightforwardly explained by subjects terminating information sampling\n    earlier, on average, on trials where the first two cues are more informative\"; Results,\n    Experimental paradigm and subject behaviour, paragraph 2, \"Choice accuracy based upon the\n    pictures observed\".'\n  why: With the criterion's measure, accuracy on 2-picture trials is not the highest (F 74.96%\n    against 76.10% and 79.62%; M 78.83% against 78.79% and 81.51%) and the claim is not reproduced.\n    With the script's measure it is highest in both monkeys (F 90.19% against 82.63% and 82.27%; M\n    93.65% against 85.20% and 83.69%), and the claim would be reproduced.\n- claim: fig7a-ofc-value-difference-neurons\n  question: The criterion requires the OFC proportion to be the largest at both significance levels\n    of O2 (p < 0.05 and p < 0.01). The paper's script for Figure 7 (Fig7_single_neurons_cue2and3.m)\n    uses one threshold for the value difference tests, |T| > 1.64 on each of the three T-statistics\n    (its comment, `norminv(0.05)`), and 1.96 for belief confirmation. Should the criterion use the\n    script's threshold, or require one of the two readings, in place of both?\n  passage: 'Results, Single neuron analyses recapitulate core findings at population level,\n    paragraph 2, \"To consider a neuron as representing value difference, we required that the\n    contrast of parameter estimates (i.e. (Value Attended) - (Value Unattended)) be significant,\n    and also that (Value Attended) and (Value Unattended) be independently significant with\n    opposing signs. At all three relevant timepoints, we found that a greater proportion of single\n    neurons passed these criteria in OFC than in ACC/DLPFC ( Fig. 7a ).\"'\n  why: With the Figure 5 trial types, OFC has the largest proportion at all three tests at 250 ms\n    for p < 0.05 and at 300 ms for p < 0.01, but no single bin passes at both levels, so the claim\n    is partially reproduced. With the script's threshold it passes at both bins and would be\n    reproduced.\n"
}
```

```
File created successfully at: questions/hunt-2018.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/hunt-2018-01.yaml",
 "content": "schema_version: 3\nid: hunt-2018-01\ndatasets:\n- archive: crcns\n  id: pfc-7\n  version: unversioned\n  doi: 10.6080/K0PZ5712\n  relation: primary\npaper: doi:10.1038/s41593-018-0239-5\ndate: 2026-11-14\nentry: hunt-2018\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43627464018\noutcomes:\n- claim: sessions-and-trials\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:sessions-and-trials\n  measured: [25, 32, 14251, 9863]\n  notes: The behavioural files hold 25 sessions of Frank (F) and 32 of Miles (M), with 9863 and\n    14251 completed option and attribute trials (trial errors 0 and 6 only), the paper's counts\n    under reading (a). Without trials of equal expected value (reading c) there are 9479 and 13691.\n    Aborted trials (reading b) can be counted only from the unit files, for the 24 and 29 sessions\n    with units (10688 and 14391 trials there).\n  deviations:\n  - Reading (b) could be counted only for sessions with units, as the behavioural files hold\n    completed trials only.\n- claim: neuron-counts\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:neuron-counts\n  measured: [189, 135, 183, 9, 21, 12]\n  notes: With the average_firing_rate of other_data/all_units_info.mat, the rate every figure script\n    of the paper uses to select units (Fig4_RSA.m and others), 189 ACC, 135 DLPFC and 183 OFC units\n    are at or above 1 Hz, with 9, 21 and 12 excluded, the paper's numbers. The claims file's readings\n    do not give them; the whole-session rate (from OverallSpikeCodes, equal to the stored session\n    mean within 0.004 Hz) gives 190, 136 and 182, the rate from trial start to response 186, 137 and\n    179. The data set holds 198 ACC, 156 DLPFC and 195 OFC units over 24 F and 29 M sessions, the\n    totals and session counts of Supplementary Table 1 as the claims file gives them. The scripts\n    also drop unit 87 (DLPFC, 4.8 Hz) as a bad cell, so the paper's DLPFC analyses, and these, use\n    134 units.\n  deviations:\n  - The rate is the stored average_firing_rate that the paper's scripts use, a third reading\n    besides the claims file's two; how it was computed is not documented in the data set.\n- claim: choice-accuracy-ev\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:choice-accuracy-ev\n  measured: [75.71, 79.01]\n  notes: Reading (a), ties left out, gives 75.71% (F) and 79.01% (M); reading (b) 72.77% and 75.90%.\n    InfoGathering_Behaviour.m counts the 384 and 560 tied trials as correct, which gives 76.66% and\n    79.83%, the paper's numbers.\n- claim: chose-on-partial-information\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:chose-on-partial-information\n  measured: [85.52, 71.43]\n  notes: With the count of pictures corrected for a joystick movement made before the last picture\n    was fixated (num_pics_viewedprezero of InfoGathering_Behaviour.m), F chose before all four cues on\n    85.52% and M on 71.43% of trials. The raw count of fixated pictures gives 54.23% and 42.56%.\n  deviations:\n  - The claims file gives no method; the count is the script's (InfoGathering_Behaviour.m,\n    out.earlychoices), with its joystick threshold and smoothing.\n- claim: choice-accuracy-observed\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:choice-accuracy-observed\n  measured: [86.0, 87.75]\n  notes: Reading (a) gives 86.00% (F) and 87.75% (M), reading (b) 79.88% and 82.26%, reading (c)\n    89.17% and 89.20%, the script's own measure (unseen at 0.5, ties counted correct) 87.80% and\n    89.48%. Counting every fixated picture as seen gives 79.14% and 81.35% under reading (a).\n  deviations:\n  - Which pictures count as observed is taken from InfoGathering_Behaviour.m (accuracy_seen) as\n    those fixated before the joystick moved, dropping a last picture fixated for 250 ms or less.\n- claim: figs1ab-cue-weights\n  outcome: partially_reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:figs1ab-cue-weights\n  notes: Model A gives positive picture weights with p < 0.05 for all four positions in both\n    monkeys and both scales. The first-side term on option trials is negative in both (F b = -0.467,\n    p = 1.5e-07; M b = -1.220, p = 2.7e-54). Probability and magnitude weights are both positive, but\n    in M they are not approximately equal under either reading (option ratio 1.11, attribute 1.13;\n    95% CIs do not overlap; Wald p = 1.1e-06 and 4.1e-07); with true values the M ratios are 1.11\n    and 1.15. In F the CIs overlap on both trial types (Wald p = 0.53 and 0.002 with seen values).\n    The n-2 weight is below the n-1 weight (ranks F 1.186 against 1.347, M 1.161 against 1.229) and\n    above the final weight (0.270 and 0.284), so the legend's slight upweighting of the\n    antepenultimate cue is not seen against n-1.\n  deviations:\n  - Model B uses the seen values (unseen at 0.5, magnitudes shifted by -0.05) as\n    InfoGathering_Behaviour.m does; the true values are shown too.\n- claim: figs1cd-fewer-cues-more-accurate\n  outcome: not_reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:figs1cd-fewer-cues-more-accurate\n  notes: With the criterion's measure and the script's count of pictures, accuracy on 2-picture\n    trials is 74.96% (F) and 78.83% (M), against 76.10% and 79.62% (F) and 78.79% and 81.51% (M) on 3\n    and 4 pictures. The mean value difference is largest on 2-picture trials in both monkeys (F 0.266,\n    0.229, 0.219; M 0.271, 0.240, 0.228). With the paper's script measure (accuracy on the seen\n    values, averaged over sessions) accuracy is 90.19%, 82.63%, 82.27% (F) and 93.65%, 85.20%, 83.69%\n    (M), and the claim holds. Whether the criterion should use that measure is asked of a reader\n    (questions/hunt-2018.yaml).\n  deviations:\n  - The number of pictures is the script's num_pics_viewed250; with the raw count F holds and M\n    does not.\n- claim: fig2a-sample-the-favourite\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig2a-sample-the-favourite\n  notes: On attribute trials with a third picture, the logistic slope of returning to the first\n    option on rank 1 minus rank 2 is 0.729 (F, p = 3.3e-190) and 1.210 (M, printed p = 0); the third\n    saccade returns on 59.8% and 86.7% of trials when cue 1 outranks cue 2, against 8.7% and 10.0%\n    otherwise.\n- claim: fig2b-positive-evidence\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig2b-positive-evidence\n  notes: With both cues at rank +2, F sampled 2.05 and M 2.22 pictures, against 2.69 and 3.15 with\n    both at -2; Spearman rho with the summed rank is -0.356 (F), -0.499 (M) and -0.434 (pooled), all\n    p < 1e-143. The raw count gives the same direction.\n- claim: fig4d-spatial-attention\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig4d-spatial-attention\n  notes: Spatial attention T = 39.90 in DLPFC (permutation p < 0.0001), 4.58 in OFC (p = 0.018) and\n    7.90 in ACC (p = 0.0028); CPD 80.2% in DLPFC against 13.7% (ACC) and 5.1% (OFC); F = 348.5,\n    p < 0.0001. All four readings of O8 and O9 hold.\n- claim: fig4e-ofc-stimulus-identity\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig4e-ofc-stimulus-identity\n  notes: Stimulus identity T = 14.82 in OFC (p < 0.0001), CPD 35.8% against 3.6% (ACC) and 4.9%\n    (DLPFC); F = 23.8, p < 0.0001. All four readings hold.\n- claim: fig4f-ofc-attended-value\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig4f-ofc-attended-value\n  notes: Attended value T = 5.86 in OFC (one-sided p = 0.0019, two-sided 0.0022), CPD 8.05% against\n    1.21% (ACC) and 0.14% (DLPFC); F = 4.84, p = 0.029. All four readings hold.\n- claim: fig4g-left-right-value\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig4g-left-right-value\n  notes: Left/right value T = 6.05 in ACC (p = 0.0073) and 6.51 in DLPFC (p = 0.0036), 0.07 in OFC;\n    CPD 8.5% and 9.7% against 0.0% in OFC. All four readings hold.\n- claim: fig4h-acc-accept-reject\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig4h-acc-accept-reject\n  notes: Accept/reject T = 10.30 in ACC (p < 0.0001), CPD 21.3% against 4.7% in DLPFC; its CPD in ACC\n    exceeds that of attended value (1.2%), reading (a). Attended value in ACC is not significant with\n    all trials (one-sided p = 0.063) and is with 3 or more cues (p = 0.019), so reading (b) holds\n    only with all trials. In OFC accept/reject has T = 8.71 and CPD 16.2%.\n- claim: figs2-consistent-across-subjects\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:figs2-consistent-across-subjects\n  notes: All six coefficients are positive in each monkey under both trial readings (94, 37, 82\n    units in M and 95, 97, 101 in F); the smallest is 0.014 (left/right value in ACC of F, trials\n    with 3 or more cues).\n- claim: figs4-dlpfc-top-bottom\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:figs4-dlpfc-top-bottom\n  notes: Same-quadrant minus same-side-other-row similarity is 0.112 in DLPFC, 0.042 in ACC and\n    -0.001 in OFC. A label-permutation reference outside the criterion gives p < 0.001, 0.022 and\n    0.46.\n- claim: fig4-t75-latencies\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig4-t75-latencies\n  measured: [20, 80, 70, 270, 250, 240, 230, 470, 360]\n  notes: With a 10 ms step (reading a) all nine values are within tolerance over -100 to 500 ms (the\n    measured values above). With a 1 ms step (reading b), as Fig4_RSA.m computes it, all nine equal\n    the paper's (24, 72, 67, 269, 241, 238, 224, 457, 369 ms) over both ranges. Over -200 to 600 ms\n    with a 10 ms step 8 of 9 are within tolerance (spatial attention in ACC 41 ms).\n- claim: figs5c-latency-order\n  outcome: partially_reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:figs5c-latency-order\n  notes: The t75 point estimates follow the paper's order in every region, but the 100 simulated t75\n    values overlap under both readings and with either set of variables (the criterion's significant\n    templates, or the set Fig4_RSA.m stacks for the panel, peak CPD above 10%). In OFC the attended\n    value range reaches -10 ms (reading a) and -13 ms (reading b), below the top of the spatial\n    attention range (93 and 99 ms). In ACC left/right value (246 to 528 ms, reading b) overlaps\n    accept/reject (227 to 291 ms). With the script's set and reading (b), spatial attention lies below\n    the other variables in ACC and DLPFC and left/right value above them in DLPFC.\n  deviations:\n  - Fig4_RSA.m draws one permutation of the residuals shared over time points (reading b) and\n    computes t75 over -199 to 600 ms at 1 ms, as done here; it keeps the variables with peak CPD\n    above 10% (Supplementary Figure 5B legend, \"Regressors explaining little variance have been\n    removed\"), shown beside the criterion's significance rule.\n- claim: fig5a-ofc-value-cpd\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig5a-ofc-value-cpd\n  measured: 290\n  notes: Under reading (a) the mean OFC CPD of cue 1, 2 and 3 value peaks 290, 300 and 290 ms after\n    its own cue, and the cue 1 and cue 2 value CPDs are above either baseline at every bin of the\n    later epochs (epoch means 0.18 to 0.52 points above). Reading (b) gives peaks of 290 to 320 ms and\n    the same result.\n- claim: fig5b-stable-attended-value-subspace\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig5b-stable-attended-value-subspace\n  notes: r = 0.845 (p = 7.7e-51, n = 182) with contrasts 19 and 20 (the script's), r = 0.843 with the\n    mean T-statistics; M r = 0.860, F r = 0.809.\n  deviations:\n  - Unit 653 is dropped, as Fig5_OFCcrosscorrelation.m does (its T-statistics at cue 2 are not\n    finite), so OFC has 182 units.\n- claim: fig5c-attribute-cue2-vs-cue1\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig5c-attribute-cue2-vs-cue1\n  notes: r = -0.270, p = 0.00023, n = 182 (M -0.236, F -0.356).\n- claim: fig5de-option-cue3-vs-stored\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig5de-option-cue3-vs-stored\n  notes: EV 3 against EV 1 r = -0.283 (p = 0.00011), against EV 2 r = -0.379 (p = 1.3e-07).\n- claim: fig5f-option-stored-combined\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig5f-option-stored-combined\n  notes: At cue 3 r = 0.523 (p = 3.4e-14); at cue 2 r = -0.033 (p = 0.66), as the Discussion says.\n- claim: fig5gj-cross-correlation-dynamics\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig5gj-cross-correlation-dynamics\n  notes: The clusters through the 250 ms point have 884, 1839, 1105 and 817 bins against\n    99.9th-percentile thresholds of 577, 500, 577 and 584, with the signs of Figure 5c-f; EV 6 at\n    cue 2 against EV 5 at cue 1 forms a positive cluster of 1622 bins (threshold 580, r = 0.755).\n  deviations:\n  - The map pairs are those of Fig5_OFCcrosscorrelation.m (EV 6/5, 2/1, 3/1, 3/2); its correlation\n    divides a population covariance by sample standard deviations, a factor of 181/182 on r, which\n    is not reproduced here.\n- claim: fig5k-ofc-comparison-unique\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig5k-ofc-comparison-unique\n  notes: Two-sided Fisher tests (as the script) give p = 0.0397, 0.0670, 0.0108 against DLPFC and\n    0.0032, 0.0003, < 0.0001 against ACC, the paper's values; all six OFC correlations are more\n    negative, five of six p < 0.05 (six of six one-sided).\n- claim: figs67-no-comparison-acc-dlpfc\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:figs67-no-comparison-acc-dlpfc\n  notes: Presence holds in ACC (r = 0.852 and 0.559) and DLPFC (r = 0.658 and 0.519), all p < 1e-9.\n    No attended-against-stored correlation is negative with p < 0.05 (ACC r = 0.031, 0.084, 0.058;\n    DLPFC r = -0.040, -0.080, -0.105; smallest p 0.23).\n- claim: fig6a-acc-belief-subspace\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig6a-acc-belief-subspace\n  notes: With T-statistics all 10 ACC correlations are positive with p < 0.05 (r = 0.165 to 0.483),\n    against 3 of 10 in DLPFC and 2 of 10 in OFC; with OLS coefficients ACC has 8 of 10. By monkey,\n    ACC has 10 of 10 (M) and 7 of 10 (F).\n- claim: fig6b-acc-belief-stronger\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig6b-acc-belief-stronger\n  notes: The ACC correlation is larger in 19 of 20 comparisons; 13 of 20 have p < 0.05 two-sided (16\n    one-sided). With OLS coefficients 16 of 20 and 10 of 20.\n- claim: fig6c-belief-subspace-rt\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig6c-belief-subspace-rt\n  notes: Under all 24 combinations of O4 to O7 (with the scripts' fixed RT bins added to O5) the\n    shortest RT bin is above the longest over 100-500 and 0-500 ms after cue 1 (odd/even, scripts'\n    bins, Hz, mean T, a difference of 0.445); with 100 random halves it holds in 98 to 100 splits.\n  deviations:\n  - The projection design is the scripts' (Fig6_ACCmultiplesignals_R3_version.m) [demeaned belief\n    weights, demeaned action weights, constant, mean of EVs 11 and 12], and the action weights are\n    taken at the bin the scripts index as 30 (centred 210 ms before the response).\n  - The scripts' RT bins (below 1.2 s, 1.2-1.4, 1.4-1.6, 1.6-1.8, from 1.8 s) are run beside the\n    claims file's quintile readings.\n  - The traces are not cut at each bin's longest RT, which the script does for plotting; the\n    windows used lie before those cuts.\n- claim: fig6d-belief-ramp-to-choice\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig6d-belief-ramp-to-choice\n  notes: Under all 24 combinations the mean belief projection over -200 to 0 ms exceeds that over\n    -500 to -300 ms in all five RT bins.\n  deviations:\n  - As fig6c; the response-locked trace averages the left- and right-choice projections, as the\n    script does.\n- claim: fig6e-action-subspace-ramp\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig6e-action-subspace-ramp\n  notes: The action projection rises over -500 to 0 ms in every RT bin under all 48 readings. Its\n    maximum over -500 to 100 ms lies between -200 and 100 ms in all five bins under 2 of 48 readings\n    (odd/even halves, per-session quintiles, rates in Hz, the signed average, either O7); in the\n    others one or two bins peak 10 to 70 ms earlier (-230 ms in the longest bin with odd/even halves\n    and the scripts' bins; -270 ms in the fourth bin with the scripts' random halves). The outcome\n    follows the criterion's rule (one reading suffices) and rests on the peak window's lower edge.\n  deviations:\n  - As fig6c.\n- claim: fig7a-ofc-value-difference-neurons\n  outcome: partially_reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig7a-ofc-value-difference-neurons\n  notes: With the Figure 5 trial types (reading a), OFC has the largest proportion at all three tests\n    at 250 ms for p < 0.05 (6.0, 4.4, 6.6% against at most 5.3, 3.2, 4.8%) and at 300 ms for p < 0.01\n    (1.6, 1.6, 3.3%), but not at both levels in one bin; with the attribute-trial reading (b) it fails\n    in every combination. With the script's threshold (|T| > 1.64) it holds at both bins. At 250 ms\n    and p < 0.05 the smallest pairwise chi-square p is 0.084. The threshold is asked of a reader.\n- claim: fig7b-ofc-value-difference-any\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig7b-ofc-value-difference-any\n  notes: With reading (a), OFC has the largest fraction passing any test at both bins and all\n    thresholds (250 ms, p < 0.05 OFC 11.5%, ACC 9.0%, DLPFC 6.0%).\n- claim: fig7c-acc-belief-neurons\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig7c-acc-belief-neurons\n  notes: ACC is highest for all four EVs at both bins and both thresholds (300 ms, p < 0.05 ACC 16.4,\n    20.1, 19.6, 11.1% against at most 10.4, 12.7, 8.2, 6.7%); in M alone DLPFC is higher for EV 13\n    (16.2% against 12.8%).\n- claim: fig8-cue1-value-all-regions\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig8-cue1-value-all-regions\n  notes: All 24 readings and the script's regression give binomial p < 1e-7 in every region (script\n    ACC 54.0%, DLPFC 41.8%, OFC 59.0%).\n  deviations:\n  - The script's own regression (InfoGathering_Neurons_Cue1_regression.m, 13 regressors on raw\n    values, significance from 1000 trial permutations corrected over the bins from 0 to 500 ms) is\n    run as a further reading.\n- claim: fig8-action-value-acc-dlpfc\n  outcome: partially_reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig8-action-value-acc-dlpfc\n  measured: [19.0, 18.7]\n  notes: The first reading the criterion lists (full model, 100-500 ms, all trials, p < 0.05) gives\n    19.0% and 18.7%, within tolerance, but OFC is above chance there (10.4%, p = 0.0018). The tests\n    all hold in five readings and in the script's (ACC 20.6%, DLPFC 17.9%, binomial p = 2e-14 and\n    3e-08, chi-square against OFC p = 6.8e-05 and 0.0016, OFC 6.0%, p = 0.41), in none of them with\n    both fractions within 18 +/- 1.8%.\n- claim: fig8-spatial-value-dlpfc\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig8-spatial-value-dlpfc\n  notes: Holds under 2 of 24 readings (100-500 ms, all trials, p < 0.01, either model); with the full\n    model DLPFC spatial value 8.2% (binomial p = 3e-08) against action value 7.5% (chi-square p = 1),\n    ACC 2.6% against 13.2% (p = 0.0003). In the script's reading DLPFC spatial is 15.7% against 17.9%\n    (p = 0.74) and ACC 9.0% against 20.6% (p = 0.0024), but the DLPFC binomial p is 2e-06, above the\n    1e-6 bound. The outcome follows the criterion's rule (one reading suffices).\n- claim: fig8-attribute-value-ofc\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:fig8-attribute-value-ofc\n  measured: 26.2\n  notes: The first reading gives 26.2% of OFC (binomial p = 4e-22), above ACC (5.8%, chi-square\n    p = 1.6e-07) and DLPFC (11.9%, p = 0.0028); the script's reading gives 23.0% (p = 3e-17), above\n    ACC (7.9%, p = 0.00011) and DLPFC (11.2%, p = 0.011).\n- claim: figs9-ev16-correlation\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:figs9-ev16-correlation\n  measured: [0.18, 0.19]\n  notes: Over neurons on trials with 3 or more cues (reading b) the mean r2 is 0.180 (EV 7) and 0.190\n    (EV 9), and the largest other pair among EVs 1-6 and 13-18 is 0.046 (EV 2 with EV 13). Over\n    sessions (reading a) 0.190 and 0.204, the first outside tolerance. The script computes the matrix\n    on all trials (0.180 and 0.198 over neurons).\n- claim: figs11-alternative-value-template\n  outcome: reproduced\n  notebook: reproduce_hunt_2018.ipynb\n  output: claim:figs11-alternative-value-template\n  notes: Attended value in OFC T = 3.31 (one-sided p = 0.0021) with CPD 2.72% against 0.37% and\n    0.29%; left/right value T = 6.75 (ACC) and 6.56 (DLPFC), -0.01 in OFC. Both fig4f and fig4g\n    criteria hold under all four readings.\n  deviations:\n  - The alternative template is the commented line of Fig4_RSA.m, -|rank(i) - rank(j)| demeaned.\nfindings:\n- kind: selection_undocumented\n  about: data\n  statement: Units are selected by the average_firing_rate field of other_data/all_units_info.mat,\n    which the paper's scripts use for the 1 Hz exclusion. How it was computed is not documented, and\n    it is neither the whole-session rate (the stored men) nor the rate over the analysed trials;\n    those select 190, 136 and 182 or 186, 137 and 179 units in ACC, DLPFC and OFC, where the field\n    gives the paper's 189, 135 and 183.\n- kind: metadata_error\n  statement: The unit files 681 to 724 (sessions 5, 11, 23 and 27 of Miles) store the subject letter\n    sb as lower case \"m\", while all other units of Miles store \"M\" and all_units_info.mat gives \"m\"\n    for every Miles unit.\n- kind: metadata_error\n  statement: The data descriptor, the README and the scripts' flowchart name the preprocessed units\n    neuronal_data/LTH_preprocessed_data, but the archive holds them as\n    neuronal_data/LTH_processed_data.zip, the folder name the scripts read.\n- kind: code_mismatch\n  statement: Every figure script drops unit 87 (DLPFC, 4.8 Hz) as a bad cell, and the Figure 5 and 7\n    scripts also drop unit 653 (OFC, whose cue 2 T-statistics are not finite), so the DLPFC analyses\n    use 134 units and the OFC analyses of Figures 5 and 7 use 182, where the paper reports 135 and 183\n    (for example n = 135 DLPFC units in the Supplementary Figure 5 legend). The paper does not\n    mention these exclusions.\n- kind: paper_inconsistency\n  statement: For Figure 7a the Results say the cue 3 tests were made \"at cue 3 of attribute trials\"\n    while citing Figure 5d/e, which are option trials; the script (Fig7_single_neurons_cue2and3.m)\n    tests EV 3 against EVs 1 and 2, the option-trial regressors.\n- kind: code_mismatch\n  statement: The Methods for Figure 6 describe a neurons x 2 projection matrix from odd and even\n    trials, with weights for action 200 ms before the response. The published script\n    (Fig6_ACCmultiplesignals_R3_version.m) averages 100 random half splits, adds a constant and the\n    mean option/attribute response to the projection design, takes the action weights at the bin\n    centred 210 ms before the response, and uses fixed reaction-time bins (below 1.2 s, 1.2-1.4,\n    1.4-1.6, 1.6-1.8, from 1.8 s) that the Methods do not give.\n- kind: methods_unavailable\n  statement: Two thresholds of the single-neuron analyses are not in the text. Figure 7 counts a\n    neuron as encoding value difference when each of three T-statistics exceeds 1.64 in absolute\n    value (Fig7_single_neurons_cue2and3.m), and belief confirmation at 1.96, and Supplementary Figure\n    1c judges accuracy on the pictures seen, averaged over sessions (InfoGathering_Behaviour.m); the\n    results here depend on both choices (fig7a, figs1cd). The authors could confirm that these are\n    the choices behind the figures.\n"
}
```

```
File created successfully at: attempts/hunt-2018-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/hunt-2018-01.yaml'; s=open(p).read()
a='''    as lower case "m", while all other units of Miles store "M" and all_units_info.mat gives "m"
    for every Miles unit.'''
b='''    as lower case "m", while all other units of Miles store "M".'''
assert a in s; s=s.replace(a,b)
a='The tests\n    all hold in five readings'
assert a in s; s=s.replace(a,'The tests\n    all hold in six readings')
open(p,'w').write(s)
import yaml,re
d=yaml.safe_load(open(p)); print(len(d['outcomes']))
for o in d['outcomes']:
    for k in ('notes',):
        pass
EOF
grep -n -E "^\s+[a-z_]+: [^'\"\[].*: " attempts/hunt-2018-01.yaml | head; python tools/entry.py check entries/hunt-2018 2>&1 | tail -15; date -u
```

```
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
AssertionError
0 error(s)
Sat Nov 14 19:45:41 UTC 2026
```

**Agent calls Bash**

```bash
grep -n -A2 'lower case "m"' attempts/hunt-2018-01.yaml; grep -n "five readings" attempts/hunt-2018-01.yaml
```

```
395:    sb as lower case "m", while all other units of Miles store "M" and all_units_info.mat gives "m"
396-    for every Miles unit.
397-- kind: metadata_error
347:    all hold in five readings and in the script's (ACC 20.6%, DLPFC 17.9%, binomial p = 2e-14 and
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/hunt-2018-01.yaml'; s=open(p).read()
s=s.replace('''    sb as lower case "m", while all other units of Miles store "M" and all_units_info.mat gives "m"
    for every Miles unit.''','''    sb as lower case "m", while all other units of Miles store "M".''')
s=s.replace('all hold in five readings','all hold in six readings')
open(p,'w').write(s)
import yaml; d=yaml.safe_load(open(p)); print(len(d['outcomes']), len(d['findings']))
EOF
python tools/entry.py check entries/hunt-2018 2>&1 | tail -15
```

```
40 7
0 error(s)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude/nbsrc.py'; s=open(p).read()
old='''      [u for u, d in U.items() if d["sb_raw"].islower()][-1:])'''
new='''      [u for u, d in U.items() if d["sb_raw"].islower()][-1:], "; their sessions:",
      sorted({(d["sb"], int(d["snum"])) for d in U.values() if d["sb_raw"].islower()}))'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && python /tmp/claude/build_nb.py x && cd  && timeout 7000 python tools/entry.py all entries/hunt-2018 2>&1 | tail -4; date -u
```

```
149 cells
Installed kernelspec registry-hunt-2018 in executed/hunt-2018/.venv/share/jupyter/kernels/registry-hunt-2018
0 error(s)
pass  reproduce_hunt_2018.ipynb  (797 s)
Sat Nov 14 19:59:28 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/hunt-2018 && python3 - <<'EOF'
import nbformat
nb=nbformat.read('reproduce_hunt_2018.ipynb',4)
out=[]
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream': out.append(o['text'])
            elif 'data' in o and 'text/plain' in o['data']: out.append(o['data']['text/plain'])
            elif o.get('output_type')=='error': print("ERROR", o.get('ename'))
txt="\n".join(out)
import re
print([l for l in txt.splitlines() if 'lower case' in l])
a=txt; b=open('/tmp/claude/exec.txt').read()
la=set(l.strip() for l in a.splitlines()); diff=[l for l in b.splitlines() if l.strip() and l.strip() not in la and not re.search(r'\d+ s\b|min, peak|loaded|fitted', l)]
print(len(diff), diff[:5])
EOF
cd  && python tools/entry.py handover entries/hunt-2018 2>&1 | tail -5; ls executed/hunt-2018/handover; git status --short
```

```
["subject letter as stored in the unit files: {'F': 312, 'M': 198, 'm': 39} ; lower case in units [681, 682, 683] ... [724] ; their sessions: [('M', 5), ('M', 11), ('M', 23), ('M', 27)]"]
1 ["subject letter as stored in the unit files: {'F': 312, 'M': 198, 'm': 39} ; lower case in units [681, 682, 683] ... [724]"]
wrote executed/hunt-2018/handover
hunt-2018.yaml
pfc7.py
reproduce_hunt_2018.ipynb
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
?? attempts/hunt-2018-01.yaml
?? entries/hunt-2018/
?? questions/hunt-2018.yaml
?? scripts
```

**Agent calls Bash**

```bash
ls -la --time-style=full-iso scripts .bashrc .idea .mcp.json 2>&1 | head -20; git check-ignore -v scripts || true
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 2026-11-14 18:32:20.809441061 +0000 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 2026-11-14 18:32:20.809441061 +0000 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 2026-11-14 18:32:20.809441061 +0000 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 2026-11-14 18:32:20.809441061 +0000 scripts
```

**Agent calls Bash**

```bash
python tools/entry.py hash entries/hunt-2018 2>&1 | tail -2; sed -i 's/It takes about 14 minutes, a third of it streaming\nthe files/X/' entries/hunt-2018/README.md; python3 - <<'EOF'
p='entries/hunt-2018/README.md'; s=open(p).read()
s=s.replace("It takes about 14 minutes, a third of it streaming\n  the files (about 3 GB, read into memory one file at a time).","It takes about 14 minutes, about three of them streaming\n  the files (about 3 GB, read into memory one file at a time).")
open(p,'w').write(s)
EOF
python tools/entry.py hash entries/hunt-2018 2>&1 | tail -2; grep -n "three of them" entries/hunt-2018/README.md
```

```
407ebcb0b84520deb4c2aa568119570c8f13fee1215e7eeb3607d898a0193aba
e17c1d8d8ac38f09ef72a3350c6d61b6878b89479e3d460853c3b2d37cc449f7
37:- `reproduce_hunt_2018.ipynb`: the analysis. It takes about 14 minutes, about three of them streaming
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='entries/hunt-2018/pfc7.py'; s=open(p).read()
s=s.replace('''The data set is CRCNS pfc-7 (crcns:pfc-7/unversioned; doi:10.6080/K0PZ5712); CRCNS data sets are
not versioned, so the files read are identified by the MD5 sums of its checksums.md5. It is read anonymously from the public S3 bucket crcnsarchive,
under pfc-7/live/. Each file is read into memory and parsed there; nothing is written to disk.''','''The data set is CRCNS pfc-7 (crcns:pfc-7/unversioned; doi:10.6080/K0PZ5712); CRCNS data sets are
not versioned, so the files read are identified by the MD5 sums of its checksums.md5. It is read
anonymously from the public S3 bucket crcnsarchive, under pfc-7/live/. Each file is read into
memory and parsed there; nothing is written to disk.''')
open(p,'w').write(s)
EOF
sed -n 1,12p entries/hunt-2018/pfc7.py; timeout 7000 python tools/entry.py all entries/hunt-2018 2>&1 | tail -3; python tools/entry.py handover entries/hunt-2018 2>&1 | tail -1; date -u
```

```
"""Loading and measures for CRCNS pfc-7 (Hunt, Malalasekera et al. 2018, Nature Neuroscience).

Hunt, Malalasekera, de Berker, Miranda, Farmer, Behrens & Kennerley (2018), "Triple dissociation
of attention and decision computations across prefrontal cortex", doi:10.1038/s41593-018-0239-5.
The data set is CRCNS pfc-7 (crcns:pfc-7/unversioned; doi:10.6080/K0PZ5712); CRCNS data sets are
not versioned, so the files read are identified by the MD5 sums of its checksums.md5. It is read
anonymously from the public S3 bucket crcnsarchive, under pfc-7/live/. Each file is read into
memory and parsed there; nothing is written to disk.

What is read:

- behavioural_data/<Miles|Frank>_InfoGathering_All_Data.mat (MATLAB 7.3): per session, the
Installed kernelspec registry-hunt-2018 in executed/hunt-2018/.venv/share/jupyter/kernels/registry-hunt-2018
0 error(s)
pass  reproduce_hunt_2018.ipynb  (804 s)
wrote executed/hunt-2018/handover
Sat Nov 14 20:14:03 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/hunt-2018 && python3 - <<'EOF'
import nbformat,re
nb=nbformat.read('reproduce_hunt_2018.ipynb',4)
out=[];err=0
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream': out.append(o['text'])
            elif 'data' in o and 'text/plain' in o['data']: out.append(o['data']['text/plain'])
            elif o.get('output_type')=='error': err+=1
a="\n".join(out); b=open('/tmp/claude/exec.txt').read()
la=set(l.strip() for l in a.splitlines()); diff=[l for l in b.splitlines() if l.strip() and l.strip() not in la and not re.search(r'\d+ s\b|min, peak|loaded|fitted|lower case', l)]
print("errors",err,"diff",len(diff), [l for l in a.splitlines() if 'total run time' in l])
EOF
cd  && git status --short | grep -v "^?? \.\|scripts"
```

```
errors 0 diff 0 ['total run time 13.2 min, peak memory 4.4 GB']
?? attempts/hunt-2018-01.yaml
?? entries/hunt-2018/
?? questions/hunt-2018.yaml
```

**Agent**

All 40 claims were tested and none are blocked: 35 reproduced, 4 partially reproduced, 1 not reproduced. The entry's checks pass (`python tools/entry.py all`, 0 errors), and the handover is built in `executed/hunt-2018/handover/`. I did not verify my own work and did not commit anything.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| sessions-and-trials, neuron-counts, choice-accuracy-ev, chose-on-partial-information, choice-accuracy-observed | reproduced |
| figs1ab-cue-weights | partially: monkey M weights probability and magnitude unequally (ratio about 1.11, Wald p about 1e-6) |
| figs1cd-fewer-cues-more-accurate | not reproduced under the criterion's measure; it holds under the paper's script measure (question to a reader) |
| fig2a, fig2b | reproduced |
| fig4d to fig4h, figs2, figs4, figs11 (RSA templates) | reproduced |
| fig4-t75-latencies | reproduced; at 1 ms steps all nine t75 values equal the paper's exactly |
| figs5c-latency-order | partially: the order holds, but the simulated t75 ranges overlap in every reading |
| fig5a to fig5k, figs67 | reproduced; the Fisher p-values equal the paper's (0.040, 0.067, 0.011, 0.003, 0.0003) |
| fig6a to fig6d | reproduced |
| fig6e | reproduced, but only under 2 of 48 readings (peak timing); the ramp itself holds in all |
| fig7a | partially: the criterion needs both significance levels in one time bin, which no bin gives (question to a reader) |
| fig7b, fig7c | reproduced |
| fig8 value, spatial (2 of 24 readings), attribute | reproduced |
| fig8-action-value-acc-dlpfc | partially: the tests hold, but no reading has both fractions within 18 ± 1.8% |
| figs9-ev16-correlation | reproduced (mean over neurons) |

**2. The dataset, assumptions and questions**
- **What it holds:** what the paper describes. The behaviour files give 25 F and 32 M sessions, with exactly 9,863 and 14,251 trials. There are 549 units in ACC, DLPFC and OFC across 24 and 29 sessions. Every unit file agrees with the units table, and the spikes line up with the trial events (the clock check passed).
- **The paper's code is in the dataset** (`scripts.zip`). I followed it where the claims file left a detail open. My GLM matches the T-statistics the authors stored to within 1.6e-6.
- **Findings about the data:**
  - The `average_firing_rate` field that selects units is undocumented. Neither whole-session nor trial rates reproduce 189/135/183; only the stored field does.
  - Unit files 681 to 724 store the subject as lower-case "m".
  - The docs name the folder `LTH_preprocessed_data`, but the archive holds `LTH_processed_data.zip`.
- **Findings about the paper:**
  - The scripts silently drop unit 87, so DLPFC analyses use 134 units, not 135; Figures 5 and 7 also drop unit 653.
  - The text describes the Figure 7a cue-3 tests as attribute trials, but they use option trials.
  - The Figure 6 script differs from the Methods (random halves, a 4-column design, fixed RT bins).
- **Assumptions:** none. No outcome is marked `assumed`.
- **Question for the paper's authors** (a `methods_unavailable` finding): please confirm the two thresholds the text omits, the |T| > 1.64 used in Figure 7 and the "pictures seen" accuracy measure behind Supplementary Figure 1c.
- **Questions to a reader** (`questions/hunt-2018.yaml`): two, on figs1cd (which accuracy measure) and fig7a (which significance threshold).
- **Version:** CRCNS is unversioned. I pinned `live/` and printed the MD5 sums of the files read.

**3. Where the protocol was unclear**
1. The claims reader did not read the paper's code because it is part of the dataset, so several criteria list readings that differ from what the code does (the firing-rate definition, the RT bins, thresholds, the variable set for Supplementary Figure 5C). I ran the criterion's readings, added the code's choice as a further reading, and judged by the criterion. The exception is neuron-counts, which I judged on the code's rate; that is recorded as a deviation.
2. The criterion's rule "reproduced under one reading" conflicts with step 1.6, which says the outcome is what all readings give. I followed the criterion and reported the reading counts in the notes (fig6e 2 of 48, fig8-spatial 2 of 24).
3. There is no rule for "partially reproduced" when a criterion has no partial clause but holds in part. I used it for figs1ab, figs5c and fig7a and explained each.
4. Reading a 1.1 to 1.7 GB HDF5 file over HTTP range requests was too slow (about 0.6 s per trial). I read each file into memory instead, as `archives.md` permits, and noted it.

**4. Runtime and failures**
- The notebook runs in about 13.3 minutes with 4.4 GB peak memory. The session ran from 18:36 to about 20:15 UTC.
- Nothing failed in the final runs. One development run crashed on a lower-case subject letter; I fixed that.

## End of run

95 turns, 92 minutes, $11.26 at API prices, result: success.
