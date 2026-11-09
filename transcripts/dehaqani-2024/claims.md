# 000931 · claims · run 39884468008

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/; ls claims/000931 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ paper/; ls claims/000931 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -250; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 250,400p claims/001453/*.yaml
```

```
- id: fig2k-more-monocular
  statement: DC have a higher proportion of purely monocular neurons than ZF (0.37 against 0.16,
    p < 0.05).
  source: Figure 2K
  quote: DC show a higher proportion of purely monocular neurons (ZF = 0.16, DC = 0.37
  statistics:
  - test: Student's t-test
    p: 0.05
    p_relation: "<"
    n: 5 ZF and 5 DC fish
- id: fig2l-bi-ratio
  statement: The binocularity index ratio is higher in ZF than in DC (0.72 against 0.24, p =
    0.010).
  source: Figure 2L
  quote: BI ratios show a higher fraction of binocular neurons in ZF compared to DC (ZF = 0.72, DC =
    0.24
  statistics:
  - test: Student's t-test
    p: 0.01
    n: 5 ZF and 5 DC fish
[... 52 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114013.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "=== page\|STAR\|Supplemental\|Figure S1\b\|KEY RESOURCES\|github\|zenodo\|dandi" paper/*.txt | sed -n 1,200p | tail -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114013.txt",
 "offset": 948,
 "limit": 742
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, STAR Methods and supplement are all present. Next I'll look at the linked code (Zenodo) and the dandiset's title and description.

**Agent calls Bash**

```bash
curl -s -m 30 https://zenodo.org/api/records/10381293 | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['metadata'].get('title'),d['metadata'].get('version'),d.get('doi'));print(d['metadata'].get('related_identifiers'));[print(f['key'],f['size'],f['links']['self']) for f in d['files']]"; curl -s -m 30 https://api.dandiarchive.org/api/dandisets/000931/versions/draft/info/ | python3 -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m['name']);print(m.get('description'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/code && cd $TMPDIR/code && curl -sL -m 120 -o c.zip "https://zenodo.org/api/records/10381293/files/iurillilab/mechano-olfactory_code-v1.1.zip/content" && unzip -q c.zip && find . -type f | grep -v '\.zip$' | head -100; md5sum c.zip
```

Result: the fetched text is not kept.

**Agent**

The code is `iurillilab/mechano-olfactory_code` v1.1 (commit 3bec502), with MATLAB scripts per figure panel. I'll read the README and the scripts behind the main claims.

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && cat README.md && wc -l *.m script_for_panels_that_needs_long_run/*.m
```

```
# mechano-olfactory_code
Analysis code for A.Dehaqani, Michelon et al. (2023): https://www.biorxiv.org/content/10.1101/2023.04.04.535405v1.full

Main contributor: 
https://github.com/ArAbolghasemi

Other contributors:
https://github.com/paolahydra
https://github.com/vigji
   175 fig1_D_raw_data_raster.m
   408 fig1_G_single_cell_PITH_single_conc.m
   386 fig1_H_I_mech_induced_change_olf_resp.m
   257 fig1_J_slow_to_fast_change_vs_01_to_1.m
   228 fig1_K_PITH_mech_mess_up_conc.m
   430 fig1_L_CDI_svmAcc_typeSpecific_vs_mix.m
   479 fig2_C_D_GLM_coeff.m
   267 fig2_findExampleCells_fourQuadrants.m
   398 fig3_C_artificial_inhalation_expriment.m
   365 fig3_F_PCx_mech_tuning.m
   184 fig4_A_raw_data_raster.m
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && cat fig1_H_I_mech_induced_change_olf_resp.m fig1_J_slow_to_fast_change_vs_01_to_1.m fig1_L_CDI_svmAcc_typeSpecific_vs_mix.m
```

```
<persisted-output>
Output too large (36KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6eed4a66-4768-403c-b2cf-e8eeec9f13ab/tool-results/b0thusthq.txt

Preview (first 2KB):
% this scripts is amied to assessing whether the diffrent responce to the
% stimulit during diffrent inh type is real or just because of random
% diffrence 071522 - regardless of mechano sensitivity
%%
clear; clc; close all;
[~, mouseNameList, dataPathPrefixList] =....
    get_all_conc_mice('paola');

pltDir = fullfile(final_figs_path('paola'),...
    'fig1_E_G_multcomp_corrected');
if ~exist(pltDir , 'dir')
   mkdir(pltDir)
end
cd(pltDir)


[... 61 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6eed4a66-4768-403c-b2cf-e8eeec9f13ab/tool-results/b0thusthq.txt",
 "offset": 60,
 "limit": 330
}
```

```
60	    load(fullfile(mouseDirName,...
61	        sprintf('%s_odorStatistics_wholeStimulus.mat',...
62	        mouseNameList{mn})))
63	    %%
64	    if isfield(respData,'rawXpeakPuffFree')
65	        xpeaksTrialId = respData.xpeakRealTrialId;
66	    else
67	        xpeaksTrialId = respData.xpeakTrialId;
68	    end
69	    %%
70	    goodAndSafe_unitsFlag =...
71	        get_goodAndSafe_units(dataPathPrefix, mouseName,...
72	        6, .5);
73	    num_of_all_cells = [num_of_all_cells;...
74	        sum(goodAndSafe_unitsFlag)];
75	    %%
76	    avg_fr = inh_NR.after_sc/inh_NR.cacheInfo.windSizeSec;
77	    
78	    %% get fast-slow delta
79	%     deltaR = get_inh_modulated_averageDeltaResp(inh_NR, respData, respLabelsData,recordingData);
[... 310 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && grep -v "^\s*%" fig1_J_slow_to_fast_change_vs_01_to_1.m | grep -v "^\s*$" | head -260
```

```
clear; clc; close all;
clear; clc; close all;
[~, mouseNameList, dataPathPrefixList] =....
    get_all_conc_mice('paola');
[tBeginning, tEnd, trialsToRemove]=...
    get_removal_variables();
pVal_threshold = 0.05;
lowConc = 1;
highConc = 2;
conc_set = [lowConc, highConc];
inhInducedChange = [];
concInducedChange = [];
diffRespTestResults = [];
count = 0;
for mn = 1 : length(mouseNameList)
    mouseName = mouseNameList{mn};
    dataPathPrefix = dataPathPrefixList{mn};
    mouseDirName = fullfile(dataPathPrefix,'processedDataStorage',...
        mouseName);
    load(fullfile(mouseDirName,...
[... 192 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && grep -v "^\s*%" fig1_L_CDI_svmAcc_typeSpecific_vs_mix.m | grep -v "^\s*$" | grep -v "print_it\|xlabel\|ylabel\|xlim\|ylim\|set(gcf\|title\|xticks\|yticks\|box off" | head -330
```

```
clear; clc; close all;
[~, mouseNameList, dataPathPrefixList] =....
    get_all_conc_mice('paola');
dataDir = fullfile('G:\My Drive\sinff-odor-project\Figuers_data_Marh2023',...
    'fig1_L_data_auROC_svmAcc_typeSpesefic_vs_mix');
[colorSet, SandR_colors] = set_plot_seting(15, 4);
plotDir = fullfile(final_figs_path('uniTn1'),...
    'fig1_L');
if ~exist(plotDir , 'dir')
   mkdir(plotDir)
end
pooled_Rtype_auROC = [];
pooled_Stype_auROC = [];
pooled_mixType_auROC = [];
pooled_Rtype_SVM_Acc = [];
pooled_Stype_SVM_Acc = [];
pooled_mixType_SVM_Acc = [];
for mn = 1 : length(mouseNameList)
    mouseName = mouseNameList{mn};
    dataPathPrefix = dataPathPrefixList{mn};
[... 265 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && grep -v "^\s*$" script_for_panels_that_needs_long_run/GLM_model.m; grep -v "^\s*$" fig2_C_D_GLM_coeff.m | grep -v "print_it\|xlabel\|ylabel\|xlim\|ylim\|set(gcf\|title\|xticks\|yticks\|box off\|Color\|scatter\|legend" | head -200
```

```
clear; clc; close all;
dataFilesDirList = {'M1\102721', 'M2\102821','M3\102921',...
    'M5\120221'};
mouseNameList = {'M1_102721', 'M2_102821','M3_102921',...
    'M5_120221'};
dataPathPrefix = 'E:\Ephys\sniffOdorProject\Conc_Series';
% dataPathPrefix = 'D:\Reza\sniffOdorProject\Conc_Series';
%%
tBeginning = .4;
tEnd = 5;
trialsToRemove = 2;
add_ndt_paths_and_init_rand_generator
numberOfBalanceSampling = 100;
%%
ptionsGlmnet= glmnetSet;
ptionsGlmnet.alpha = .95; 
optsGlmfit = statset('glmfit');
optsGlmfit.MaxIter = 1000;
numberOFShuffleing = 100;
%%
[... 342 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && sed -n 330,479p fig2_C_D_GLM_coeff.m | grep -v "^\s*$" | grep -iv "print_it\|xlabel\|ylabel\|xlim\|ylim\|set(gcf\|title\|xticks\|yticks\|box off"; grep -rn "tBeginning =\|tEnd =\|trialsToRemove =\|tBegining =" . | head -40
```

```
'pooled')
%%
DOTSIZE = 10; %doesnt do anything
close all; figure;
raincloud_plot((alpha(:)),...
    'color',[.5,.5,.5], 'box_on', 1, 'alpha', .5,...
    'lwr_bnd', 1, 'line_width', .5, 'band_width', .005,...
    'dot_size', DOTSIZE);
     'pooled')
%%
close all; figure;
raincloud_plot((beta(:)),...
    'color',[.5,.5,.5], 'box_on', 1, 'alpha', .5,...
    'lwr_bnd', 1, 'line_width', .5, 'band_width', .005,...
    'dot_size', DOTSIZE);
     'pooled')
%%
close all; figure;
raincloud_plot((gamma(:)),...
    'color',[.5,.5,.5], 'box_on', 1, 'alpha', .5,...
[... 86 more lines not kept]
```

**Agent**

Code so far: Figure 1 and 2 scripts use inhalations 0.4 to 5 s after odor onset with the first 2 trials dropped, and slow = label 2, fast = label 1. Now the Figure 3 and 4 scripts.

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && for f in fig3_F_PCx_mech_tuning.m fig3_C_artificial_inhalation_expriment.m; do echo "=== $f"; grep -v "^\s*$" $f | grep -v "^\s*%" | grep -iv "print_it\|xlabel\|ylabel\|xlim\|ylim\|set(gcf\|title\|xticks\|yticks\|box off\|colormap\|caxis\|imagesc\|Color'\|legend\|axis \|hold on\|figure\|close all\|^\s*plot(" ; done | head -400
```

```
=== fig3_F_PCx_mech_tuning.m
[dataFilesDirList, mouseNameList, dataPathPrefixList] =....
    get_all_healthy_mice('uniTn1');
add_ndt_paths_and_init_rand_generator
rasterMapPooled = [];
rasterMap_sem_Pooled = [];
slopeVecPooled = [];
slopePvalVecPooled = [];
unitsIdsPooled = [];
mouseIdPooled = [];
numOfQuantileSplit = 9;
for mn = 1  : length(mouseNameList)    
    mouseName = mouseNameList{mn};
    fprintf('Analysis %s data... \n', mouseName);
    mouseNameToPrint = mouseName(4:end);
    dataPathPrefix = dataPathPrefixList{mn};
    mouseDirName = fullfile(dataPathPrefix,'processedDataStorage',...
        mouseName);
    load(fullfile(mouseDirName,...
        sprintf('\\%s_respData.mat', mouseName)));
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && grep -v "^\s*$" "fig4_C-E_bulbectomy_responses_firstsniff.m" | grep -v "^\s*%" | grep -iv "print_it\|xlabel\|ylabel\|xlim\|ylim\|set(gcf\|title\|xticks\|yticks\|box off\|colormap\|caxis\|imagesc\|legend\|axis \|hold on\|figure\|close all\|^\s*plot(\|fprintf\|fopen\|fclose" | head -400
```

```
clearvars -except T B R tests M
folderDataSave = '[removed: a home directory path]/Dropbox (Personal)/SniffOdor_project_processedData/sniffOdorProject/Bulbectomy/processedDataStorage';
generalOutputDir = fullfile('supp_bulbectomized_tuning_newCode', 'firstSniff', 'across_comparisons');
generalPlotDir = fullfile(final_figs_path('paola'), generalOutputDir, 'Aug14_0to180vsSLOW_ttest_RightTail_p001', 'rightTail_test3');
mkdir(generalPlotDir)
cd(generalPlotDir)
testNuse = 2;
if ~exist('B', 'var')
    load('[removed: a home directory path]/Dropbox (Personal)/SniffOdor_project_processedData/sniffOdorProject/Bulbectomy/processedDataStorage/analysisTables.mat', 'T', 'B', 'R');
end
if exist(fullfile(folderDataSave, 'firstSniffTest_metadata.mat'), 'file')
    tests = load(fullfile(folderDataSave, 'firstSniffTest_metadata.mat'));
else
    tests = [];
end
load('[removed: a home directory path]/Dropbox (Personal)/SniffOdor_project_processedData/sniffOdorProject/Bulbectomy/processedDataStorage/sigOdorResponse_bulbect.mat')
fnames = {'fs', 'lr', 'slr', 'sniffs', 'rRr'};
brforeInhOnsetWind = .6;
afterInhOnsetWind = .6;
PITH_time = -1*brforeInhOnsetWind:.001 : afterInhOnsetWind +.001; 
[... 272 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/script_for_panels_that_needs_long_run && grep -v "^\s*$" decoding_of_inh_type_bulbectomized.m decoding_of_inh_type_control.m | grep -v "^\S*:\s*%"; grep -v "^\s*$" fig5_Decoding_of_conc_and_type_in_each_PC.m | grep -v "^\s*%" | head -170
```

```
decoding_of_inh_type_bulbectomized.m:clear; clc; close all;
decoding_of_inh_type_bulbectomized.m:mouseNameList = {'M1_122121', 'M4_011522', 'M5_021022', 'M6_021122'};
decoding_of_inh_type_bulbectomized.m:dataPathPrefixList = {'E:\Ephys\Bulbectomy', 'E:\Ephys\Bulbectomy',...
decoding_of_inh_type_bulbectomized.m:    'E:\Ephys\Bulbectomy', 'E:\Ephys\Bulbectomy'};
decoding_of_inh_type_bulbectomized.m:add_ndt_paths_and_init_rand_generator
decoding_of_inh_type_bulbectomized.m:regionsAcroNames = {'Octx', 'MCtx'};
decoding_of_inh_type_bulbectomized.m:regionsNames = {'priform','motor'};
decoding_of_inh_type_bulbectomized.m:regionsMappedId = [6,1];
decoding_of_inh_type_bulbectomized.m:numberOfBlanceSampling = 100;
decoding_of_inh_type_bulbectomized.m:num_cv_splits = 10;
decoding_of_inh_type_bulbectomized.m:numOfResample = 100;
decoding_of_inh_type_bulbectomized.m:the_feature_preprocessors{1} =...
decoding_of_inh_type_bulbectomized.m:    zscore_normalize_FP;
decoding_of_inh_type_bulbectomized.m:the_classifier = libsvm_CL;
decoding_of_inh_type_bulbectomized.m:blanceSmapleSize = 400;
decoding_of_inh_type_bulbectomized.m:maxNumberOfNeurons = 175;
decoding_of_inh_type_bulbectomized.m:num_of_neurons_set = 5:10:maxNumberOfNeurons;
decoding_of_inh_type_bulbectomized.m:for ri = 1 : length(regionsMappedId)    
decoding_of_inh_type_bulbectomized.m:    rgName = regionsNames{ri};
decoding_of_inh_type_bulbectomized.m:    regionDecodingResults =... 
[... 292 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && grep -v "^\s*$" script_for_panels_that_needs_long_run/fig5_cis_and_trans_decoding_of_conc.m | grep -v "^\s*%" | head -150; echo =====; grep -v "^\s*$" script_for_panels_that_needs_long_run/linear_model.m | grep -v "^\s*%" | head -120
```

```
clear; clc; close all;
dataFilesDirList = {'M1\102721', 'M2\102821','M3\102921',...
    'M5\120221'};
mouseNameList = {'M1_102721', 'M2_102821','M3_102921',...
    'M5_120221'};
 dataPathPrefix = 'E:\Ephys\Conc_Series';
[tBeginning, tEnd, trialsToRemove]=...
    get_removal_variables();
add_ndt_paths_and_init_rand_generator
conc_set = [1,2,4];
numberOfBalanceSampling = 100;
num_cv_splits = 10;
numOfResample = 100;
the_feature_preprocessors{1} =...
    zscore_normalize_FP;
the_classifier = libsvm_CL;
fullSpaceDecodingAcc_R_o1 =...
    nan(numOfResample, numberOfBalanceSampling);
fullSpaceDecodingAcc_S_o1 =...
    nan(numOfResample, numberOfBalanceSampling);
[... 252 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && grep -n "std\|\.75\|1\.5\|tan(\|pi/12\|ttest\|anova\|ranksum\|signrank\|numOfUnits\|143\|randperm\|time_bin\|binSize" script_for_panels_that_needs_long_run/fig5_H_I_high_correlated_sub_units.m fig5_H_I_high_correlated_units_decoder.m fig5_G_high_correlated_units_PCA.m fig5_E_F_sic_and_trans_decoder.m | head -60
```

```
script_for_panels_that_needs_long_run/fig5_H_I_high_correlated_sub_units.m:104:            find((abs(beta(:, oId)) <= abs(alpha(:, oId)*tan(pi/4+angleRange))) &...
script_for_panels_that_needs_long_run/fig5_H_I_high_correlated_sub_units.m:108:            find((abs(beta(:, oId)) <= abs(alpha(:, oId)*tan(pi/4+angleRange))) &...
script_for_panels_that_needs_long_run/fig5_H_I_high_correlated_sub_units.m:113:            find((abs(beta(:, oId)) <= abs(alpha(:, oId)*tan(pi/4+angleRange))) &...
script_for_panels_that_needs_long_run/fig5_H_I_high_correlated_sub_units.m:122:            randperm(size(selectedUnits_neg_corr,1),...
script_for_panels_that_needs_long_run/fig5_H_I_high_correlated_sub_units.m:125:            randperm(size(selectedUnits_poss_corr,1),...
script_for_panels_that_needs_long_run/fig5_H_I_high_correlated_sub_units.m:128:            randperm(size(controlSelection,1),...
fig5_H_I_high_correlated_units_decoder.m:29:                nanstd(squeeze(decodingAcc_Mix(:, sId, oId, sc, :)),[],[1,2]),...
fig5_H_I_high_correlated_units_decoder.m:34:                nanstd(squeeze(decodingAcc_R(:, sId, oId, sc, :)),[],[1,2]),...
fig5_H_I_high_correlated_units_decoder.m:39:                nanstd(squeeze(decodingAcc_S(:, sId, oId, sc, :)),[],[1,2]),...
fig5_H_I_high_correlated_units_decoder.m:44:                nanstd(squeeze(decodingAcc_Strain_Rtest(:, sId, oId, sc, :)),[],[1,2]),...
fig5_H_I_high_correlated_units_decoder.m:49:                nanstd(squeeze(decodingAcc_Rtrain_Stest(:, sId, oId, sc, :)),[],[1,2]),...
fig5_H_I_high_correlated_units_decoder.m:55:                nanstd(squeeze(decodingAcc_Mix(:, sId, oId, 3, :)),[],[1,2]),...
fig5_H_I_high_correlated_units_decoder.m:60:                nanstd(squeeze(decodingAcc_R(:, sId, oId, 3, :)),[],[1,2]),...
fig5_H_I_high_correlated_units_decoder.m:65:                nanstd(squeeze(decodingAcc_S(:, sId, oId, 3, :)),[],[1,2]),...
fig5_H_I_high_correlated_units_decoder.m:70:                nanstd(squeeze(decodingAcc_Strain
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && sed -n 1,140p script_for_panels_that_needs_long_run/fig5_H_I_high_correlated_sub_units.m | grep -v "^\s*$"
```

```
clear; clc; close all;
%%
dataFilesDirList = {'M1\102721', 'M2\102821','M3\102921',...
    'M5\120221'};
mouseNameList = {'M1_102721', 'M2_102821','M3_102921',...
    'M5_120221'};
  dataPathPrefix = 'E:\Ephys\sniffOdorProject\Conc_Series';
%  dataPathPrefix = 'D:\Reza\sniffOdorProject\Conc_Series';
%dataPathPrefix = 'D:\sniffOdorProject\Conc_Series';
%%
linearity_Coeff_poold = [];
linearity_pVal_poold = [];
nonlinearity_Coeff_poold = [];
nonlinearity_pVal_poold = [];
%%
for mn = 1 : length(mouseNameList)
    %%
    mouseName = mouseNameList{mn};
    mouseDirName = fullfile(dataPathPrefix,'processedDataStorage',...
        mouseName);
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 758,947p paper/*.txt | grep -n "Figure\|Methods" | head; grep -n "kind\|schema_version\|data:\|depends_on\|deviation\|open" docs/protocol.md | head -40; ls tools/; python tools/claims_check.py --help 2>&1 | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 205,262p docs/protocol.md; python3 -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | head -250
```

```
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
     the missing names are recorded as a finding (`metadata_insufficient`).
   - When outside data has to be matched to the dataset's cells, sessions
     or subjects, a claim of its own (`kind: link`) tests the link. Link
     claims are the registry's checks, not findings of the paper, so the
     author adds them to the claims file; they are the only claims the
[... 288 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"
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

Next I'll check two more code details: the neuron count in the angle analysis and the rate function in the Figure 6 simulation.

**Agent calls Bash**

```bash
cd $TMPDIR/code/iurillilab-*/ && grep -v "^\s*$" fig5_D_encoding_angle_full_space.m | grep -v "^\s*%" | head -60; python3 - <<'EOF'
import json,glob
for f in ["script_for_panels_that_needs_long_run/fig5_encoding_angle_full.ipynb","script_for_panels_that_needs_long_run/simulation_effect_of_inh_on_con_lrModel_exponential.ipynb","script_for_panels_that_needs_long_run/simulation_effect_of_inh_on_con_lrModel_multiply.ipynb"]:
    nb=json.load(open(f))
    print("=====",f)
    for c in nb['cells']:
        if c['cell_type']=='code':
            s=''.join(c['source'])
            if any(k in s for k in ['poisson','Poisson','exp(','log(','n_neuron','sample(','LinearDiscriminant','angle','k_range','np.linspace','SVC','shrink']):
                print(s[:1500]); print('--')
EOF
```

```
clear; clc; close all;
dataDir = fullfile('G:\My Drive',...
    'sinff-odor-project\Figuers_data_Marh2023');
load(fullfile(dataDir, 'fig5_encoding_angle_full_space_data',...
    'encoding_angle_full_space_data'));
pltDir = fullfile(final_figs_path('uniTn1'),...
    'Fig5_D_full_space');
if ~exist(pltDir , 'dir')
   mkdir(pltDir)
end
[colorSet, SandR_colors] =...
    set_plot_seting(15, 8);
conditions = {'odor 1', 'odor 2', 'pooled-two-odor'};
for i = 1: 3
    switch i 
        case 1
            concEncodingsAngleTransferred =...
                90 - concVec_Stype_vs_concVec_Rtype(:,1);
            concVsSampelingAngleTransferred =...
                90 - [concVec_Stype_vs_samplingVec(:,1);...
[... 349 more lines not kept]
```

**Agent**

I've read the paper and code. Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/000931/10.1016-j.celrep.2024.114013.yaml",
 "content": "# Claims for Dehaqani, Michelon, Patella, Petrucco, Piasini & Iurilli (2024), Cell Reports 43,\n# 114013, on dandiset 000931.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23, under\n# docs/protocol.md (Reader), protocol version pilot-10.\n#\n# Text read: the version of record (paper/10.1016-j.celrep.2024.114013.txt, extracted from the\n# publisher PDF supplied by a person): main text, figure legends, STAR Methods, and the\n# supplemental information (legends of Figures S1 to S6). No supplementary table exists. The PDF\n# was not opened; no figure value is needed beyond the legends and the text.\n#\n# Dataset: DANDI 000931, \"A mechanosensory feedback that uncouples external and self-generated\n# sensory responses in the olfactory cortex\", described as the dataset for this paper. Its data\n# were not looked at.\n#\n# Data the paper used (STAR Methods, Mice; Odor delivery; Artificial mechanical stimulation):\n# C57BL/6J mice, 6 to 9 weeks old, both sexes, head-fixed, Neuropixels 1.0 recordings in the\n# anterior piriform cortex (PCx, layers 2 and 3; 22 mice in all, Figure 1B) at 30 kHz. Groups:\n#  - concentration series, 4 mice: alpha-pinene and eucalyptol at 0.01, 0.1 and 1% v/v, 8 blocks\n#    (Figures 2, 5, 6; 464 neurons; the GLM and pseudo-population analyses);\n#  - two-concentration experiment, 2 mice: four odors at 0.01 and 0.1% v/v, 16 blocks. Pooled\n#    with the 4 mice above at 0.01 and 0.1% for Figure 1 (6 mice, 660 neurons, 205\n#    odor-responsive, \"five odors\"). The Methods list the odors inconsistently (three odors at\n#    \"0.01 and 1%\" in the odor panel), so the author takes the odors and concentrations from the\n#    files;\n#  - odor identity experiment, 4 mice: four odors at one concentration (0.01%) (Figure S5E);\n#  - awake mice without odor for airflow tuning and first sniffs: 10 control mice, 955 PCx\n#    neurons (Figures 3D to 3F, 4D to 4G); motor cortex (MCx) neurons, 548 (Figure S4C);\n#  - artificial airflow, 3 tracheostomized mice under urethane: 150 ms suction pulses of\n#    odorless air at 50, 100, 150, 200 and 250 ml/min, 252 neurons (Figures 3A to 3C, S3A, S3B);\n#  - bulbectomy, 4 awake mice, 153 PCx neurons (Figures 4, S4);\n#  - anterior ethmoidal nerve (AEN) neurectomy, 5 mice, 752 neurons (Figures S3C to S3E).\n# Signals besides spikes: nasal airflow from a flow sensor in the nose cone, odor from a\n# photo-ionization detector, a TTL at each odor trial and a TTL at each detected inhalation onset,\n# all at 30 kHz; odor pulses of 5 s triggered at an inhalation onset. Single units from Kilosort3\n# and Phy, kept above 0.5 Hz (0.1 Hz under urethane). Inhalations are sorted into slow and fast\n# (\"sniff\") per mouse by the clustering pipeline of STAR Methods, Inhalation clustering.\n#\n# Code read: iurillilab/mechano-olfactory_code, tag v1.1, commit 3bec502, from the Zenodo\n# deposit the key resources table gives (doi:10.5281/zenodo.10381293; zip md5\n# 0e4e72b5a207513498369615b50a9253). It holds per-panel MATLAB scripts and three Python\n# notebooks (encoding angle, Figure 6 simulation). Panel letters in file names follow the\n# bioRxiv preprint (code fig5_D = paper Figure 5C, code fig5_E_F = 5D, code fig5_G/H_I = 5E/5F).\n# The scripts load preprocessed .mat files and call helpers that are not in the repository\n# (get_aSample, get_removal_variables, get_goodAndSafe_units, the per-neuron odor-response\n# statistics, the CDI values, the first-sniff test tables), so some choices remain open.\n# Nothing in the code covers Figure 5G to 5I, the inhalation clustering, the phase decoding,\n# Figure S2C or Figure S6H.\n#\n# Choices fixed for all claims, with their sources:\n#  - Inhalation response: spike count in the 180 ms (or 70 ms) after inhalation onset (STAR\n#    Methods, Analysis of sniff-by-sniff responses).\n#  - Odor inhalations: the Methods take inhalations in a window \"starting at the odor onset and\n#    lasting for 5 seconds\"; the code (GLM_model.m, linear_model.m) takes those from 0.4 to 5 s\n#    after odor onset. The Methods window is the main reading, the code's a variant, for every\n#    claim on odor inhalations. The first two trials of each odor-concentration are dropped\n#    (Methods; trialsToRemove = 2 in the code).\n#  - Odorless inhalations: those 13 to 4 s before an odor onset (Methods).\n#  - Slow and fast labels: as the dataset gives them, produced by the paper's clustering; if the\n#    dataset lacks them, the clustering of STAR Methods, Inhalation clustering, is rerun and the\n#    claims depend on inhalation-sorting.\n#  - Concentration regressor in the GLM and the linear model: 0 for odorless inhalations, then\n#    0.33, 0.66 and 1 for 0.01, 0.1 and 1% (code, GLM_model.m and linear_model.m), which the\n#    Methods describe as the log concentration scaled from 0 to 1.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000931\"\npaper: doi:10.1016/j.celrep.2024.114013\nclaims:\n- id: inhalation-sorting\n  statement: Inhalation durations are bimodal, and a Gaussian-mixture and hierarchical\n    clustering of inhalation waveforms sorts them into slow and fast inhalations; fast\n    inhalations are shorter and have steeper airflow changes than slow ones.\n  source: Results, Sniffing causes unstable odor responses in the PCx, paragraph 1; Figure 1C;\n    STAR Methods, Inhalation clustering\n  quote: Since the distribution of inhalation durations appeared bimodal, we developed a\n    semi-unsupervised method that sorted inhalations into slow and fast depending on their airflow\n    rate waveforms ... Fast inhalations had shorter duration and steeper changes in airflow rate\n    than slow inhalations.\n  expected:\n  - quantity: accuracy of the clustering on held-out mice (leave-one-mouse-out, eight mice)\n    value: 98\n    tolerance: 9.8\n    unit: percent\n  criterion: Per STAR Methods, Analysis of the breathing signal and Inhalation clustering (the\n    code does not hold this step). Breathing signal band-passed 0.5 to 50 Hz, smoothed with a\n    Gaussian of SD 25 ms; peaks at local minima, peaks closer than 65 ms to the next dropped;\n    onset and offset at the zero crossings around the peak. Waveforms of 100 ms centred on the\n    peak, normalised by their 2-norm, PCA to the fewest PCs explaining 98% of variance, GMM\n    (full covariance, regularisation 0.05, 15 replicates, 10,000 iterations) with the number of\n    clusters by the Calinski-Harabasz index, centroids merged by a correlation-distance\n    hierarchical dendrogram into two clusters, the one with shorter mean inhalation length\n    named fast. Where the dataset gives slow and fast labels, they are compared with this\n    output (fraction of agreement reported). Reproduced when, in every mouse, the fast class\n    has a shorter median inhalation length and steeper negative and positive inhalation slopes\n    (10% to 90% of peak amplitude, Methods) than the slow class, and the leave-one-mouse-out\n    accuracy is within tolerance. Open, and named as readings, is how the dendrogram is cut\n    when it gives three clusters (\"two clusters were similar and stemmed from the same branch\"\n    was decided by visual inspection) - (a) merge the two clusters sharing the nearest parent;\n    (b) cut the dendrogram at two clusters. Which eight mice formed the cross-validation is not\n    stated; all awake mice with breathing are used, and the eight-mouse sets are a variant\n    when the count differs.\n- id: figs1a-phase-decoding\n  statement: PCx population activity encodes the inhalation phase; a cross-validated support\n    vector regression predicts the phase above a shuffle null in individual mice.\n  source: Results, Sniffing causes unstable odor responses in the PCx, paragraph 3; Figures 1E\n    and S1A\n  quote: Hence, PCx activity encoded the phase and speed of each inhalation (Figures 1E and 1F;\n    Figures S1A and S1B).\n  depends_on:\n  - inhalation-sorting\n  criterion: Per STAR Methods, Inhalation phase decoding. Firing rates from spikes smoothed with\n    a Gaussian of SD 20 ms, downsampled to 10 ms bins; mice with at least 20 PCx neurons; PCs up\n    to a cumulative explained variance above 0.5 (at least two); phase in [0, 1] linearly from\n    onset to offset of each sorted inhalation; non-overlapping epochs of 30 s of concatenated\n    inhalation periods, all ordered pairs of epochs as train and test; SVR with scikit-learn\n    defaults (RBF kernel); score the squared Pearson correlation, averaged over pairs; null from\n    shuffling the phase array before prediction. Reproduced when in every mouse the R2 exceeds\n    the 95th percentile of its null; partially reproduced when that holds in most mice. The\n    number of shuffles is not given; 1000 is used, a standard choice that does not change the\n    outcome.\n- id: figs1b-speed-decoding-single-mice\n  statement: The inhalation speed (fast against slow) can be decoded above chance from the mean\n    firing rate in the first 180 ms of inhalation in individual mice.\n  source: Figure S1B; Results, Sniffing causes unstable odor responses in the PCx, paragraph 3\n  quote: Decoding the inhalation speed (fast versus slow) using the mean firing rate in the early\n    180 ms of inhalation in individual mice.\n  depends_on:\n  - inhalation-sorting\n  criterion: Per STAR Methods, Inhalation speed decoding, and decoding_of_inh_type_control.m and\n    decoding_of_inh_type_control_single_mice.m. Odorless inhalations, 180 ms spike counts, a\n    sample of 400 inhalations balanced between slow and fast, linear SVM (libsvm through the\n    Neural Decoding Toolbox), 10-fold cross-validation, z-scoring with training-set statistics,\n    100 resampling runs and 100 draws of inhalations. Whether 400 is the total or the count per\n    class is open; readings (a) 200 slow and 200 fast, (b) 400 of each. Reproduced when in every\n    mouse the mean accuracy minus one SD exceeds the 50% chance level (the panel shows mean and\n    SD with the chance line).\n- id: fig1-odor-responsive-fraction\n  statement: Of 660 PCx neurons in six mice, 31.1% (205) reliably respond to at least one odor\n    concentration.\n  source: Results, Sniffing causes unstable odor responses in the PCx, paragraph 3; Figure 1H\n    legend\n  quote: Of the recorded neurons, 31.1% reliably responded to at least one odor concentration\n    (205 of 660 neurons; six mice).\n  expected:\n  - quantity: odor-responsive neurons\n    value: 205\n    tolerance: 20.5\n    unit: neurons\n  - quantity: recorded neurons in the six mice\n    value: 660\n    tolerance: 66\n    unit: neurons\n  - quantity: fraction of neurons odor-responsive\n    value: 31.1\n    tolerance: 3.11\n    unit: percent\n  criterion: Neurons of the six mice with 0.01 and 0.1% concentrations, kept as in STAR Methods,\n    Spike sorting and inclusion criteria (above 0.5 Hz). A neuron is odor-responsive when, for\n    any odor at 0.01 or 0.1%, a Wilcoxon signed-rank test (Figure 1H legend) is significant at\n    p < 0.05 after Benjamini-Hochberg adjustment; the code (fig1_H_I_mech_induced_change_olf_resp.m)\n    adjusts across the odor-concentration tests of each neuron and calls the neuron responsive\n    if any adjusted p < 0.05. The paired values of the signed-rank test are not stated, and the\n    code loads them precomputed (\"odorStatistics_wholeStimulus\", a \"greater\" test). Readings\n    (a) per trial, the spike count over the whole 5 s odor period against the same-length\n    period before odor onset, one-sided (odor greater); (b) as (a), two-sided; (c) per trial,\n    the mean 180 ms inhalation response during the odor against the mean over odorless\n    inhalations of that trial, one-sided. Reproduced when one reading gives counts within\n    tolerance.\n- id: fig1hi-sniff-changes-responses\n  statement: In 72.2% of odor-responsive neurons (148 of 205) the response amplitude during\n    inhalation depends on how fast the animal inhales, more than expected by chance.\n  source: Results, Sniffing causes unstable odor responses in the PCx, paragraph 3; Figures 1H\n    and 1I\n  quote: Strikingly, how fast an animal inhaled influenced the response amplitude during\n    inhalation in 72.2% of those neurons (148 of 205 neurons; Figures 1G–1I).\n  depends_on:\n  - fig1-odor-responsive-fraction\n  expected:\n  - quantity: odor-responsive neurons with at least one response differing between fast and slow\n      inhalations\n    value: 148\n    tolerance: 14.8\n    unit: neurons\n  - quantity: fraction of odor-responsive neurons\n    value: 72.2\n    tolerance: 7.22\n    unit: percent\n  - quantity: odor-concentration responses of odor-responsive neurons tested\n    value: 750\n    tolerance: 75\n    unit: responses\n  criterion: Per the Figure 1H legend and fig1_H_I_mech_induced_change_olf_resp.m. For every\n    odor-responsive neuron and every odor and concentration (0.01, 0.1%) for which its adjusted\n    p < 0.05, the mean firing rate in 180 ms after onset of each fast and each slow odor\n    inhalation; two-sided Wilcoxon rank-sum test, fast against slow, at p <= 0.01. A neuron\n    counts when any of its responses differs. Figure 1I compares the count of differing\n    responses with a null from 1000 shuffles of the slow and fast labels; reproduced when the\n    counts are within tolerance and the observed number of differing responses exceeds every\n    shuffle (or at least the 95th percentile). The odor-inhalation window follows the Methods\n    (0 to 5 s), with the code's 0.4 to 5 s as a variant.\n- id: fig1h-direction-of-change\n  statement: A faster inhalation increases 37.3% of odor responses and decreases 19.2% of them.\n  source: Results, Sniffing causes unstable odor responses in the PCx, paragraph 3; Figure 1H\n  quote: 'The impact of a faster inhalation was not uniform across odor responses: 37.3% of the\n    odor responses increased with a rapid inhalation, whereas 19.2% decreased in amplitude.'\n  depends_on:\n  - fig1hi-sniff-changes-responses\n  expected:\n  - quantity: odor-concentration responses larger during fast inhalations\n    value: 37.3\n    tolerance: 3.73\n    unit: percent\n  - quantity: odor-concentration responses smaller during fast inhalations\n    value: 19.2\n    tolerance: 1.92\n    unit: percent\n  criterion: As in fig1_H_I_mech_induced_change_olf_resp.m, over the same responses as\n    fig1hi-sniff-changes-responses, one-sided Wilcoxon rank-sum tests at p <= 0.005 each way\n    (fast greater; fast smaller), as fractions of all tested responses. A variant takes the\n    sign of the mean difference among the responses that differ in the two-sided test at p <=\n    0.01.\n- id: figs1c-early-70ms\n  statement: The sniff-driven variability in odor responses is already significant in the first\n    70 ms of an inhalation.\n  source: Results, Sniffing causes unstable odor responses in the PCx, paragraph 3; Figure S1C\n  quote: This sniffdriven variability in odor responses was already significant during the first\n    70 ms of an inhalation (Figure S1C).\n  depends_on:\n  - fig1-odor-responsive-fraction\n  criterion: As fig1hi-sniff-changes-responses with the 70 ms window after inhalation onset\n    (Figure S1C legend; two-sided rank-sum at p < 0.01; null from 1000 label shuffles).\n    \"Significant\" is read as the observed fraction of differing responses exceeding the 95th\n    percentile of the shuffle null; reproduced when it does.\n- id: figs1d-rs-fs-similar\n  statement: Regular-spiking (putatively excitatory or feedforward inhibitory) and fast-spiking\n    (putatively feedback inhibitory) neurons show similar effects of inhalation speed on their\n    odor responses.\n  source: Results, Sniffing causes unstable odor responses in the PCx, paragraph 3; Figure S1D\n  quote: After sorting neurons into regular spiking (RS; putatively excitatory or feedforward\n    inhibitory) and fast spiking (FS; putatively feedback inhibitory), we observed similar\n    effects of the inhalation speed in both types (Figure S1D).\n  depends_on:\n  - fig1hi-sniff-changes-responses\n  expected:\n  - quantity: RS neurons among the odor-responsive neurons\n    value: 127\n    tolerance: 12.7\n    unit: neurons\n  - quantity: FS neurons among the odor-responsive neurons\n    value: 78\n    tolerance: 7.8\n    unit: neurons\n  criterion: RS and FS units per STAR Methods, Spike sorting and inclusion criteria, k-means\n    (squared Euclidean, 10,000 iterations, 2,500 replicates) per mouse on trough-to-peak\n    latency, waveform asymmetry (p2 - p1)/(p2 + p1) and mean firing rate, the cluster with\n    higher rate, shorter latency and larger asymmetry named FS. Per mouse and type, the\n    fraction of responses enhanced by a fast inhalation, by a slow inhalation, and sniff\n    invariant (rank-sum, p < 0.01, as in the legend). The paper reports no test. Readings for\n    \"similar\" (a) for each of the three fractions, a Wilcoxon signed-rank test of RS against\n    FS over the six mice gives p >= 0.05; (b) the same with a Mann-Whitney test. Reproduced\n    when all three fractions pass under a reading and both types have a nonzero fraction of\n    responses changed by speed.\n- id: fig1j-sniff-change-larger-than-concentration\n  statement: Across odor-responsive neurons, the absolute response change caused by a\n    slow-to-fast switch in inhalation (at 0.01%) is larger than that caused by a tenfold\n    increase in concentration (0.01 to 0.1%, slow inhalations).\n  source: Results, Sniffing causes unstable odor responses in the PCx, paragraph 4; Figure 1J\n  quote: On average, sniffs caused a response amplitude change bigger than that caused by a\n    10-fold increase in odor concentration in the odor-responsive neurons (Figure 1J).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.0001\n    p_relation: <\n    n: 477 neuron-odor pairs of odor-responsive neurons\n  depends_on:\n  - fig1-odor-responsive-fraction\n  expected:\n  - quantity: neuron-odor pairs\n    value: 477\n    tolerance: 47.7\n    unit: pairs\n  criterion: As fig1_J_slow_to_fast_change_vs_01_to_1.m. Pairs are odor-responsive neurons with\n    an odor for which either concentration is responsive (adjusted p < 0.05). Per pair, mean\n    rate at 0.01% fast minus 0.01% slow, and 0.1% slow minus 0.01% slow, in 180 ms after\n    inhalation onset; absolute values compared by a paired Wilcoxon signed-rank test (the\n    legend). Reproduced when the sniff change is larger (higher median) at p < 0.0001;\n    partially reproduced when p < 0.05 only. The code's tests (two-sided rank-sum and paired t\n    test) are reported as variants.\n- id: fig1l-cdi-mixed-lower\n  statement: Concentration discriminability (CDI) of single neurons is lower when slow and fast\n    inhalations are mixed than when computed within one inhalation speed.\n  source: Results, Sniffing causes unstable odor responses in the PCx, paragraph 4; Figure 1L\n  quote: Combining responses from slow and fast inhalations decreased the CDI compared with\n    responses observed during uniform inhalation speeds (Figure 1L).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.0001\n    p_relation: <\n    n: 477 neuron-odor pairs\n  depends_on:\n  - fig1j-sniff-change-larger-than-concentration\n  criterion: Per STAR Methods, Concentration discrimination index. For each pair of\n    fig1j-sniff-change-larger-than-concentration, CDI = abs(1 - 2*auROC) of 180 ms spike counts\n    at 0.01% against 0.1%, from equal-size random samples of inhalations for the two\n    concentrations, 100 draws averaged, for slow, fast and mixed inhalations. The within-speed\n    value is the mean of the slow and fast CDI (fig1_L_CDI_svmAcc_typeSpecific_vs_mix.m).\n    Paired Wilcoxon signed-rank test of within against mixed; reproduced when mixed is lower at\n    p < 0.0001, partially when p < 0.05 only. The sample size per draw and the make-up of the\n    mixed sample are not given (the code loads the CDI precomputed). Readings (a) the sample\n    size is the smallest count over slow and fast at both concentrations, and the mixed sample\n    is half slow and half fast; (b) the same size, mixed sample drawn at random from all\n    inhalations; (c) per set, the smaller count of the two concentrations. The code's tests\n    (rank-sum, Kolmogorov-Smirnov) are variants.\n- id: fig2-glm-variance\n  statement: A regularised Poisson GLM with inhalation speed, concentration and their interaction\n    explains 91.9% of the variance in the mean spike count during the first 180 ms of odor\n    inhalation across neurons.\n  source: Results, PCx neurons randomly mix olfactory and non-olfactory inputs during\n    inhalations, paragraph 2\n  quote: This model explained 91.9% of the variance in the mean number of spikes generated\n    during the first 180 ms of odor inhalation across all neurons.\n  depends_on:\n  - fig2c-interaction-small\n  expected:\n    quantity: variance explained\n    value: 91.9\n    tolerance: 9.19\n    unit: percent\n  criterion: The GLM fits of fig2c-interaction-small. How the variance is computed is not\n    stated. Readings (a) R2 between predicted and observed mean spike counts per neuron-odor\n    pair and condition (4 concentrations by 2 speeds), pooled over all pairs; (b) the mean over\n    pairs of the same R2 within each pair; (c) the deviance explained of each fit on single\n    inhalations, averaged over pairs. Reproduced when one reading is within tolerance.\n- id: fig2c-interaction-small\n  statement: In the GLM, the interaction between inhalation speed and concentration has a small\n    effect on the odor response, while the inhalation-speed (non-olfactory) term has a larger\n    additive or subtractive effect.\n  source: Results, PCx neurons randomly mix olfactory and non-olfactory inputs during\n    inhalations, paragraph 3; Figure 2C\n  quote: The GLM analysis revealed that the interaction between inhalation speed and\n    concentration response had a small effect on the odor response amplitude during an inhalation\n    (Figure 2C). Instead, the non-olfactory input had a more significant additive or subtractive\n    effect (Figure 2C).\n  expected:\n  - quantity: neuron-odor pairs\n    value: 928\n    tolerance: 92.8\n    unit: pairs\n  - quantity: neurons in the four concentration-series mice\n    value: 464\n    tolerance: 46.4\n    unit: neurons\n  criterion: Per STAR Methods, Encoding models, and GLM_model.m with fig2_C_D_GLM_coeff.m. All\n    kept neurons of the four concentration-series mice, each odor separately. Spike count in\n    the 180 ms after inhalation onset; regressors I (fast 1, slow 0), C (0 odorless, 0.33, 0.66,\n    1 for 0.01, 0.1, 1%) and I*C; Poisson GLM with glmnet elastic net, alpha 0.95, the penalty\n    at lambda_1se of 10-fold cross-validation (nFold = min(smallest class - 3, 10)), as the\n    code settles; inhalations resampled to equal numbers per speed and concentration 100 times\n    and coefficients averaged. Reproduced when the median absolute interaction weight is below\n    the median absolute inhalation-speed weight, over all pairs. The 95th percentile of each\n    absolute weight is reported (the figure's whiskers).\n- id: fig2d-mixed-sensitivities\n  statement: The signs of the inhalation-speed and concentration weights can differ within a\n    neuron, so that a fast inhalation can raise or lower a response regardless of how the\n    neuron responds to a higher concentration; the combination is heterogeneous across neurons.\n  source: Results, PCx neurons randomly mix olfactory and non-olfactory inputs during\n    inhalations, paragraph 3; Figure 2D\n  quote: Importantly, the sign of the weight for the non-olfactory input and the odor\n    concentration factors could differ in the same neuron (Figure 2D). The non-olfactory input\n    caused by a fast inhalation could increase or decrease the odor response amplitude regardless\n    of how the neuron responded to a higher concentration of that odor.\n  depends_on:\n  - fig2c-interaction-small\n  criterion: The weights of fig2c-interaction-small. Reproduced when neuron-odor pairs with\n    nonzero weights lie in all four sign quadrants of inhalation against concentration weight,\n    including both opposite-sign quadrants. The Pearson correlation of the two weights (as\n    fig2_C_D_GLM_coeff.m computes it) and the count per quadrant are reported.\n- id: figs2ab-rs-fs-heterogeneous\n  statement: RS and FS neurons both show a heterogeneous distribution of inhalation-speed and\n    concentration sensitivities.\n  source: Results, PCx neurons randomly mix olfactory and non-olfactory inputs during\n    inhalations, paragraph 3; Figures S2A and S2B\n  quote: We similarly found a heterogeneous distribution of non-olfactory sensitivities in RS and\n    FS neurons (Figures S2A and S2B).\n  depends_on:\n  - fig2d-mixed-sensitivities\n  - figs1d-rs-fs-similar\n  expected:\n  - quantity: RS neurons among the 464\n    value: 289\n    tolerance: 28.9\n    unit: neurons\n  - quantity: FS neurons among the 464\n    value: 175\n    tolerance: 17.5\n    unit: neurons\n  criterion: The criterion of fig2d-mixed-sensitivities applied to RS and FS neurons separately,\n    with RS and FS as in figs1d-rs-fs-similar.\n- id: figs2c-waveform-no-prediction\n  statement: Spike waveform features (asymmetry and trough-to-peak delay) cannot predict a\n    neuron's inhalation-speed weight, concentration weight, or both, with any of three models.\n  source: Results, PCx neurons randomly mix olfactory and non-olfactory inputs during\n    inhalations, paragraph 3; Figure S2C; STAR Methods, Prediction of encoding properties from\n    waveforms\n  quote: In none of the 9 cases, the predictive model could extract a significant relationship\n    (as measured by the cross-validated R2 of the regression) between the spike waveform and the\n    encoding parameters.\n  depends_on:\n  - fig2c-interaction-small\n  criterion: Per STAR Methods, standardised features; elastic-net linear model (95% ridge, 5%\n    lasso, penalty by nested 10-fold CV), KNN regressor (k by nested CV), 1000 bagged trees\n    (minimum leaf 5); 10-fold CV over cells; targets a, b, and a and b jointly. The Methods do\n    not say which weights (GLM or linear model) are the a and b used, nor what makes an R2\n    significant. Readings for the weights (a) the GLM weights of fig2c-interaction-small; (b)\n    the linear-model weights of fig5ef-correlated-subpopulations. Readings for significance\n    (i) cross-validated R2 not above 0; (ii) R2 not above the 95th percentile of a null from\n    shuffling the targets across cells (1000 shuffles). Reproduced when no model and target\n    is significant under each reading.\n- id: figs2d-70ms-similar\n  statement: Restricting the GLM analysis to the first 70 ms of inhalation gives similar results.\n  source: Results, PCx neurons randomly mix olfactory and non-olfactory inputs during\n    inhalations, paragraph 3; Figure S2D\n  quote: Finally, restricting the analysis to the early 70 ms of inhalation also gave similar\n    results (Figure S2D).\n  depends_on:\n  - fig2c-interaction-small\n  criterion: The criteria of fig2c-interaction-small and fig2d-mixed-sensitivities with spike\n    counts in the 70 ms after inhalation onset; reproduced when both hold.\n- id: fig3c-airflow-tuning-anesthetized\n  statement: In tracheostomized anesthetized mice, 57.1% of PCx neurons (144 of 252) encode the\n    rate of artificial nasal airflow, 117 with positive and 27 with negative slopes.\n  source: Results, A mechanosensory input signals the nasal airflow rate to the PCx, paragraph\n    2; Figure 3C\n  quote: We found that 57.1% of neurons displayed mechanosensory responses, meaning that they\n    encoded the airflow rate.\n  expected:\n  - quantity: airflow-tuned neurons\n    value: 144\n    tolerance: 14.4\n    unit: neurons\n  - quantity: neurons recorded\n    value: 252\n    tolerance: 25.2\n    unit: neurons\n  - quantity: tuned neurons with positive slope\n    value: 117\n    tolerance: 11.7\n    unit: neurons\n  - quantity: tuned neurons with negative slope\n    value: 27\n    tolerance: 2.7\n    unit: neurons\n  criterion: As fig3_C_artificial_inhalation_expriment.m. Single units above 0.1 Hz in olfactory\n    areas (OLF, EPd, PIR) more than 50 um from an area border. Per pulse, firing rate in (0,\n    500] ms after pulse onset minus (-500, 0] ms; responses z-scored over all pulses of the\n    unit; linear regression on the airflow rank (1 to 5); tuned when the slope p <= 0.01 (t test\n    of the slope, as the legend says). Reproduced when all four counts are within tolerance;\n    partially when the tuned count is but the split by sign is not. If the dataset lacks the\n    anatomical labels, all units are used and the count of 252 is compared.\n- id: fig3b-latency-shortens\n  statement: Faster artificial airflow shortens response latency without significantly changing\n    the order in which neurons are activated.\n  source: Results, A mechanosensory input signals the nasal airflow rate to the PCx, paragraph\n    2; Figures 3B and S3B\n  quote: Faster airflow also decreased the response latency without significantly changing the\n    sequential activation order across neurons (Figure 3B; Figure S3B).\n  depends_on:\n  - fig3c-airflow-tuning-anesthetized\n  criterion: Over the 144 tuned neurons, the latency to the peak of the PETH (Gaussian of SD 10\n    ms, Methods and code) after onset of the 100 and the 250 ml/min pulses (Figure S3B). The\n    paper names no test. Readings (a) latency shorter at 250 ml/min by a paired Wilcoxon\n    signed-rank test at p < 0.05, and the activation order kept, read as a positive Spearman\n    correlation of the latencies at the two rates with p < 0.05; (b) the same with a paired t\n    test. Reproduced when both parts hold under a reading.\n- id: fig3f-airflow-tuning-awake\n  statement: In awake, normally breathing mice without odor, 78.3% of PCx neurons (748 of 955,\n    10 mice) and 77.2% of odor-responsive neurons encode the peak inhalation airflow with a\n    monotonic change; 36.7% increase and 41.7% decrease their response with faster inhalation.\n  source: Results, A mechanosensory input signals the nasal airflow rate to the PCx, paragraph\n    3; Figures 3E and 3F\n  quote: This analysis revealed that 78.3% of the PCx neurons (77.2% of the odorresponsive\n    neurons) encoded the peak inhalation airflow rate with a monotonic change in spiking activity\n    after the inhalation (Figure 3E) ... 36.7% of the neurons increased the amplitude of their\n    responses when the inhalation speed increased, and another 41.7% decreased their responses\n  expected:\n  - quantity: neurons tuned to peak airflow\n    value: 748\n    tolerance: 74.8\n    unit: neurons\n  - quantity: neurons recorded\n    value: 955\n    tolerance: 95.5\n    unit: neurons\n  - quantity: fraction tuned\n    value: 78.3\n    tolerance: 7.83\n    unit: percent\n  - quantity: fraction of odor-responsive neurons tuned\n    value: 77.2\n    tolerance: 7.72\n    unit: percent\n  - quantity: neurons with positive slope\n    value: 350\n    tolerance: 35\n    unit: neurons\n  - quantity: neurons with negative slope\n    value: 398\n    tolerance: 39.8\n    unit: neurons\n  criterion: As fig3_F_PCx_mech_tuning.m. Per mouse, odorless inhalations; peak airflow is the\n    absolute flow at the inhalation peak; ten quantile bins (MATLAB quantile with 9 cut points)\n    with equal counts; response is the 180 ms rate after inhalation onset, z-scored per neuron\n    over inhalations; linear regression of single-inhalation responses on the bin index (1 to\n    10); tuned when the slope p <= 0.01 (legend t test). Reproduced when the counts and\n    fractions are within tolerance. The 77.2% uses the odor-responsive neurons of\n    fig1-odor-responsive-fraction among these mice; it is reported, and checked only where\n    those neurons are among the 10 mice. The code also reports the Spearman correlation of the\n    bin means as \"monotonic\"; it is shown as a variant.\n- id: figs3-aen-neurectomy\n  statement: Cutting the anterior ethmoidal nerve leaves PCx responses to inhalation intact;\n    airflow tuning curves after neurectomy (551 of 752 neurons tuned, 5 mice) are similar to\n    those of control mice.\n  source: Results, A mechanosensory input signals the nasal airflow rate to the PCx, paragraph\n    4; Figures S3D and S3E\n  quote: Severing the AEN left intact the responses of PCx neurons to inhalations. The tuning\n    curves for the airflow rate after the neurectomy remained similar to those of control mice\n    (Figures S3D and S3E).\n  depends_on:\n  - fig3f-airflow-tuning-awake\n  expected:\n  - quantity: tuned neurons after neurectomy\n    value: 551\n    tolerance: 55.1\n    unit: neurons\n  - quantity: neurons recorded after neurectomy\n    value: 752\n    tolerance: 75.2\n    unit: neurons\n  criterion: The method of fig3f-airflow-tuning-awake on the neurectomy mice. The paper names no\n    test for \"similar\". Readings (a) a two-sample Kolmogorov-Smirnov test of tuning slopes,\n    neurectomy against control, gives p >= 0.05; (b) the fraction of tuned neurons and the\n    fractions with positive and negative slopes each differ from control by less than 10\n    percentage points. Reproduced when counts are within tolerance and a reading holds.\n- id: figs4-bulbectomy-no-odor-no-phase\n  statement: After bulbectomy, PCx neurons do not respond to odors and the population does not\n    encode the inhalation phase.\n  source: Results, A top-down input may supply behavioral state information during a sniff,\n    paragraph 2; Figures S4A and S4B\n  quote: In bulbectomized mice, PCx neurons were unresponsive to odors (Figure S4A). Moreover,\n    the population activity did not encode the inhalation phase (Figure 4B; Figure S4B).\n  depends_on:\n  - figs1a-phase-decoding\n  - fig1-odor-responsive-fraction\n  criterion: Phase decoding as in figs1a-phase-decoding; reproduced for this part when in no\n    bulbectomized mouse the R2 exceeds the 95th percentile of its null. Odor responses by the\n    test of fig1-odor-responsive-fraction (each of its readings); reproduced for this part when\n    the fraction of odor-responsive neurons is at or below the 5% false-positive rate. The\n    average odor PETH aligned to the first odor inhalation (Figure S4A) is shown. Both parts\n    must hold.\n- id: fig4-sniff-preferring-fraction\n  statement: After bulbectomy, 15.7% of PCx neurons still fire more during fast sniffs than\n    normal inhalations, against 29.7% in control mice.\n  source: Results, A top-down input may supply behavioral state information during a sniff,\n    paragraph 2; Figure 4D\n  quote: Nonetheless, 15.7% of PCx neurons exhibited increased spiking activity during fast\n    sniffs compared with normal inhalations (see example neuron in Figure 4C). For comparison,\n    this proportion was 29.7% in control mice.\n  depends_on:\n  - inhalation-sorting\n  expected:\n  - quantity: sniff-preferring PCx neurons, bulbectomized\n    value: 15.7\n    tolerance: 1.57\n    unit: percent\n  - quantity: sniff-preferring PCx neurons, control\n    value: 29.7\n    tolerance: 2.97\n    unit: percent\n  - quantity: sniff-preferring neurons, bulbectomized (23 of 153 in 4 mice, Figure 4D)\n    value: 23\n    tolerance: 2.3\n    unit: neurons\n  - quantity: sniff-preferring neurons, control (284 of 955 in 10 mice, Figure 4D)\n    value: 284\n    tolerance: 28.4\n    unit: neurons\n  criterion: Per STAR Methods, Analysis of sniff-by-sniff responses. Odorless inhalations only;\n    the first fast inhalation after at least five consecutive slow ones against the remaining\n    slow inhalations, spike counts 0 to 180 ms after onset; a t test at p < 0.01 (Figure S4C\n    legend), one-sided with sniff greater (the code's output folder is named\n    \"0to180vsSLOW_ttest_RightTail_p001\"), two-sample. Two readings of the percentages, as 23 of\n    153 is 15.0% and not 15.7% (a) pooled over neurons; (b) the mean of per-mouse fractions,\n    which fig4_C-E_bulbectomy_responses_firstsniff.m computes. Reproduced when the counts are\n    within tolerance and a reading puts both percentages within tolerance. A two-sided test is\n    a variant.\n- id: fig4e-sniff-response-smaller\n  statement: In bulbectomized mice the sniff-induced response of sniff-preferring PCx neurons\n    is smaller in amplitude than in control mice.\n  source: Results, A top-down input may supply behavioral state information during a sniff,\n    paragraph 2; Figure 4E\n  quote: However, the sniff-induced activity in bulbectomized mice was smaller in amplitude and\n    more variable across sniffs than in control mice (Figures 4D–4F).\n  statistics:\n  - test: two-tailed t test with unequal variances\n    p: 0.0002\n    n: 284 control and 23 bulbectomized sniff-preferring neurons\n  - about: PCx control, PCx bulbectomized and MCx control (Figure S4D)\n    test: 1-way ANOVA, Tukey-Kramer post hoc\n    p: 0.0001\n    p_relation: <\n  depends_on:\n  - fig4-sniff-preferring-fraction\n  criterion: Per sniff-preferring neuron, the mean 0 to 180 ms spike count (or rate) after first\n    sniffs minus that after slow inhalations; Welch two-sample t test, control against\n    bulbectomized, as the legend and fig4_C-E_bulbectomy_responses_firstsniff.m. Reproduced\n    when control is larger at p < 0.05, with p reported; the one-way ANOVA over the three\n    groups with Tukey-Kramer comparisons (Figure S4D) is reported as well.\n- id: fig4f-sniff-response-more-variable\n  statement: The coefficient of variation of the response across first sniffs is larger in\n    bulbectomized than in control mice.\n  source: Figure 4F; Results, A top-down input may supply behavioral state information during\n    a sniff, paragraph 2\n  quote: Coefficient of variation of the response amplitude across first sniffs in control and\n    bulbectomized mice (p < 0.0001; two-tailed t test).\n  statistics:\n  - test: two-tailed t test\n    p: 0.0001\n    p_relation: <\n    n: sniff-preferring neurons, 284 control and 23 bulbectomized\n  - about: PCx control, PCx bulbectomized and MCx control (Figure S4E)\n    test: 1-way ANOVA, Tukey-Kramer post hoc\n    p: 0.0001\n    p_relation: <\n  depends_on:\n  - fig4-sniff-preferring-fraction\n  criterion: As fig4_C-E_bulbectomy_responses_firstsniff.m. Per sniff-preferring neuron, the\n    mean spike count in 0 to 180 ms of each first sniff; CV = SD over mean across first sniffs.\n    Two-tailed two-sample t test, equal or unequal variances chosen by an F test (vartest2) as\n    the code does. Reproduced when bulbectomized CV is larger at p < 0.0001; partially when p <\n    0.05 only.\n- id: fig4g-sniff-decoding-reduced\n  statement: A linear classifier distinguishes sniffs from regular inhalations from PCx activity\n    in both control and bulbectomized mice, but with clearly lower accuracy after bulbectomy.\n  source: Results, A top-down input may supply behavioral state information during a sniff,\n    paragraph 2; Figure 4G\n  quote: Correspondingly, while a linear classifier could differentiate a sniff from a regular\n    inhalation based on PCx activity in both groups, its accuracy was notably reduced\n    post-bulbectomy (Figure 4G).\n  depends_on:\n  - inhalation-sorting\n  criterion: Per STAR Methods, Inhalation speed decoding, and decoding_of_inh_type_control.m and\n    decoding_of_inh_type_bulbectomized.m. Pseudo-population of each group, odorless\n    inhalations, 180 ms spike counts, 400 inhalations balanced slow and fast (readings as in\n    figs1b-speed-decoding-single-mice), linear SVM, 10-fold CV, training-set z-scoring; neuron\n    counts 5, 15, ... up to 175 (bulbectomy) and 195 (control), neurons drawn with\n    replacement, 100 resamples by 100 inhalation draws. Reproduced when at every neuron count\n    the control mean accuracy exceeds the bulbectomy mean, and in both groups the mean minus\n    one SD at the largest count exceeds 50%.\n- id: fig4d-pre-sniff-rise\n  statement: In bulbectomized mice the sniff-induced activity starts rising several tens of\n    milliseconds before the nominal sniff onset.\n  source: Results, A top-down input may supply behavioral state information during a sniff,\n    paragraph 2; Figure 4D\n  quote: Remarkably, the sniff-induced activity observed in the bulbectomized mice seemed to start\n    rising several tens of milliseconds before the nominal onset of the sniff.\n  depends_on:\n  - fig4-sniff-preferring-fraction\n  criterion: As fig4_C-E_bulbectomy_responses_firstsniff.m and the Figure 4D legend. For each\n    sniff-preferring neuron, PETHs (1 ms, -0.6 to 0.6 s) for first sniffs and slow inhalations,\n    averaged in 10 ms bins; per bin a one-sided paired t test (sniff greater) across neurons;\n    Benjamini-Hochberg at 0.05 over bins. Reproduced when the run of significant bins that\n    contains the post-onset response begins at or before -20 ms (several tens of ms read as at\n    least 20 ms); partially reproduced when it begins between -20 and 0 ms.\n- id: figs4-motor-cortex-sniff\n  statement: A similar peri-sniff increase occurs in motor cortex, where a slow inhalation\n    modulates 5.8% of neurons but 17.1% show a significant peri-sniff increase.\n  source: Results, A top-down input may supply behavioral state information during a sniff,\n    paragraph 3; Figure S4C\n  quote: Here, a slow inhalation modulated the activity of 5.8% of neurons (see STAR Methods). In\n    contrast, 17.1% of MCx neurons showed a significant peri-sniff increase in spiking activity\n  depends_on:\n  - fig4-sniff-preferring-fraction\n  expected:\n  - quantity: MCx neurons modulated by slow inhalation\n    value: 5.8\n    tolerance: 0.58\n    unit: percent\n  - quantity: MCx neurons preferring a sniff\n    value: 17.1\n    tolerance: 1.71\n    unit: percent\n  - quantity: sniff-preferring MCx neurons (94 of 548, Figure S4C)\n    value: 94\n    tolerance: 9.4\n    unit: neurons\n  criterion: Sniff preference as in fig4-sniff-preferring-fraction (t test, p < 0.01). Inhalation\n    modulation per STAR Methods, Analysis of sniff-by-sniff responses - spikes from -300 to +400\n    ms around onsets of odorless slow inhalations, adaptive bins of at least five spikes, a\n    chi-square test against a homogeneous Poisson process at the neuron's mean rate. The\n    chi-square threshold is not given; readings p < 0.05 and p < 0.01. Which mice hold MCx\n    neurons (the code takes them from both control and bulbectomized mice) is open; readings\n    (a) control mice only, as the legend says \"mice with intact OBs\"; (b) all mice with MCx\n    units. Reproduced when a reading gives values within tolerance.\n- id: fig5b-pc1-speed-pc23-concentration\n  statement: Inhalation speed is decoded with high accuracy from the first PC of the population\n    odor response but concentration is not; concentration (and odor identity) are decoded from\n    the second and third PCs, from which speed is not.\n  source: Results, Odor information and inhalation information are independent, paragraphs 2\n    and 3; Figures 5B, S5C and S5E\n  quote: Linear decoders—namely, linear support vector machine (lSVM) classifiers—could\n    discriminate the inhalation speed with high accuracy using the projection of neural activity\n    onto the first PC. In contrast, decoders could not classify an odor concentration using only\n    the activity explained by the first PC.\n  depends_on:\n  - inhalation-sorting\n  criterion: As fig5_Decoding_of_conc_and_type_in_each_PC.m (and the odor-identity version).\n    Pseudo-population of the four mice, odor inhalations of both odors at three concentrations,\n    balanced per speed and concentration, 180 ms counts; PCA on z-scored responses; for each of\n    the first 15 PCs, linear SVM (10-fold CV, 100 resamples, 100 draws) per odor for speed and\n    concentration. Read from mean and SD as the figure shows - \"high accuracy\" or \"decoded\" as\n    mean minus one SD above chance (50% speed, 33.3% concentration, 25% identity of four\n    odors), \"could not\" as chance within mean plus or minus one SD. Reproduced when, for both\n    odors, speed is decoded from PC1 and not from PC2 or PC3, and concentration is decoded from\n    PC2 or PC3 and not from PC1. Identity (four-odor experiment, Figure S5E) is reported the\n    same way.\n- id: fig5c-encoding-angles\n  statement: The population directions that separate concentrations during slow and during fast\n    inhalation differ but are more similar to each other than to the direction that separates\n    inhalation speeds.\n  source: Results, Odor information and inhalation information are independent, paragraph 4;\n    Figure 5C\n  quote: We found that, even though these two directions were different (as expected, given the\n    high dimensionality of the population response), they were more similar than the directions\n    that tell how fast a mouse breathes in apart from how concentrated the odor is (Figure 5C).\n  depends_on:\n  - inhalation-sorting\n  criterion: As STAR Methods, Angle between encoding axes, and fig5_encoding_angle_full.ipynb.\n    Per odor and for 100 pseudo-population samples, LDA (eigen solver, Ledoit-Wolf shrinkage)\n    on spike counts for concentration within fast, within slow, and for speed; first column of\n    the scalings; angles transformed to 90 - |90 - Q| (the notebook takes |90 - angle|, the\n    complement; the Methods form is used and the notebook's shown as a variant). Reproduced\n    when the mean slow-fast concentration angle is below the mean concentration-speed angle\n    for both odors. The number of neurons per sample is not given; readings (a) all 464\n    neurons with inhalations resampled, as the notebook's input file name suggests; (b) 143\n    neurons drawn at random, the size used elsewhere in Figure 5.\n- id: fig5d-sniff-invariant-decoding\n  statement: Concentration decoders trained on one inhalation speed generalize to the other\n    (trans-decoding) with performance similar to cis-decoding, both on PCs 2 and 3 and on the\n    full population, so the PCx representation of concentration is sniff invariant.\n  source: Results, The distributed representation of odor concentration is sniff invariant,\n    paragraph 1; Figures 5D and S5F\n  quote: A decoder using PCx response projections on the second and third PCs exhibited similar\n    cis- and trans-decoding performances, suggesting that PCx has sniffinvariant representations\n    of odor concentration (Figure 5D; Figures S5F and S5G).\n  depends_on:\n  - inhalation-sorting\n  criterion: As fig5_cis_and_trans_decoding_of_conc.m. Per odor and for 100 pseudo-population\n    samples, linear SVM of concentration (three classes) trained on slow or fast inhalations,\n    tested on held-out inhalations of the same speed (cis, 10-fold CV) or of the other (trans),\n    on PCs 2 and 3 of the z-scored pseudo-population and on the full population. Reproduced\n    when in both spaces trans accuracy minus one SD exceeds 33.3%, and for PCs 2 and 3 the\n    mean trans accuracy lies within one SD of the mean cis accuracy (\"similar\", read from the\n    mean and SD the panel shows). The gap between cis and trans is reported.\n- id: figs5gh-other-windows-and-codes\n  statement: Cis- and trans-decoding results are similar with spike counts over 70 ms or 180 ms\n    windows and with population vectors of 10 ms bins or phase bins over a respiratory cycle.\n  source: Results, The distributed representation of odor concentration is sniff invariant,\n    paragraph 1; Figures S5G and S5H\n  quote: We observed similar results when the decoders used spike counts summed over 70 or 180 ms\n    windows and spike counts for concatenated 10 ms or 10\n  depends_on:\n  - fig5d-sniff-invariant-decoding\n  criterion: Feature vectors per STAR Methods, Concentration decoding (one bin of 180 ms; 18\n    bins of 10 ms; 50 time bins over the cycle zero-padded to 500 ms; 36 phase bins from the\n    Hilbert phase), per mouse (four mice, Figure S5H), inhalations resampled 100 times, SVC\n    with linear kernel, C 1, 10-fold. The 70 ms window (Figure S5G) as fig5d with 70 ms counts.\n    Reproduced when the full-space condition of fig5d-sniff-invariant-decoding (trans above\n    chance by one SD) holds for every scheme and the 70 ms window.\n- id: fig5ef-correlated-subpopulations\n  statement: Trans-decoding of concentration falls to chance with sub-populations whose\n    inhalation and concentration sensitivities are correlated (positively or negatively), but\n    stays above chance with an uncorrelated sub-population.\n  source: Results, The distributed representation of odor concentration is sniff invariant,\n    paragraph 2; Figures 5E and 5F\n  quote: Thus, a trans-decoder performed at the chancelevel if it could use only the activity of\n    a neural population with correlated sensitivity for non-olfactory and olfactory inputs (Figure\n    5F).\n  depends_on:\n  - fig5d-sniff-invariant-decoding\n  expected:\n    quantity: neurons per sub-population\n    value: 143\n    tolerance: 14.3\n    unit: neurons\n  criterion: Weights a (speed) and b (concentration) from the linear model of STAR Methods,\n    Encoding models, as linear_model.m (z-scored 180 ms response, regressors I and C,\n    inhalations balanced by resampling 100 times, coefficients averaged). Selection per STAR\n    Methods, |b| between |a*tan(pi/12)| and |a*tan(5*pi/12)|, positive when a and b share sign,\n    negative otherwise, uncorrelated as their union; the code\n    (fig5_H_I_high_correlated_sub_units.m) uses a lower bound |a|*(pi/4 - pi/6), close to\n    tan(pi/12), shown as a variant. Equal random draws from the three groups (the smaller\n    group's size); cis and trans decoding as fig5d-sniff-invariant-decoding on the full space.\n    Reproduced when for both odors trans accuracy is within one SD of 33.3% for both correlated\n    groups and minus one SD above it for the uncorrelated group.\n- id: fig5gh-mechanosensitive-as-good\n  statement: A population of mechanosensitive neurons carries at least as much sniff-invariant\n    concentration information as a population of sniff-insensitive neurons.\n  source: Results, The distributed representation of odor concentration is sniff invariant,\n    paragraph 3; Figures 5G and 5H\n  quote: This analysis revealed that a population of mechanosensitive neurons carries at least as\n    much sniff-invariant information as a population of only sniff-insensitive neurons (Figure\n    5H).\n  depends_on:\n  - fig5ef-correlated-subpopulations\n  expected:\n    quantity: neurons per population\n    value: 143\n    tolerance: 14.3\n    unit: neurons\n  criterion: Speed coefficients from the linear model of fig5ef-correlated-subpopulations.\n    Sniff-invariant neurons have a coefficient within 0 +/- 0.75 SD, mechanosensitive neurons\n    beyond +/- 1.5 SD, equal numbers drawn (Results, paragraph 3); the code does not hold this\n    step. Open readings (a) SD of the coefficients over all neurons, per odor; (b) over all\n    neuron-odor pairs pooled. Trans-decoding as fig5d-sniff-invariant-decoding. \"At least as\n    much\" read as the mean mechanosensitive trans accuracy not lower than the sniff-invariant\n    mean by more than one SD. Reproduced when this holds for both odors under a reading.\n- id: fig5i-time-course-similar\n  statement: Over 20 consecutive 10 ms bins of an inhalation, concentration decoding within and\n    across inhalation speeds is similar for mechanosensitive and sniff-insensitive neurons.\n  source: Results, The distributed representation of odor concentration is sniff invariant,\n    paragraph 4; Figure 5I\n  quote: Linear decoders using only mechanosensitive or sniff-insensitive neurons performed\n    similarly throughout this inhalation window (Figure 5I).\n  statistics:\n  - test: two-way ANOVA\n    p: 0.05\n    p_relation: '>'\n    n: 143 neurons per sub-population\n  depends_on:\n  - fig5gh-mechanosensitive-as-good\n  criterion: A claim of absence. Populations of fig5gh-mechanosensitive-as-good; cis and trans\n    decoding as fig5d-sniff-invariant-decoding in each of 20 bins of 10 ms tiling 0 to 200 ms.\n    The paper's test is a two-way ANOVA at 0.05; its factors and units are not given. Readings\n    (a) population by time bin on trans accuracies of the resamples; (b) population by time bin\n    on cis and trans accuracies pooled. Reproduced when the population effect has p > 0.05;\n    not reproduced when p <= 0.05; the effect size is reported. If the readings differ the\n    claim is blocked as methods_underspecified.\n- id: figs5i-coefficients-similar\n  statement: Mechanosensitive and sniff-invariant neurons have similar distributions of\n    concentration coefficients.\n  source: Results, The distributed representation of odor concentration is sniff invariant,\n    paragraph 3; Figure S5I\n  quote: Cumulative distribution of concentration regressor coefficients for mechano-sensitive\n    and sniff-invariant neurons (Kolmogorov-Smirnov test, P-value = 0.4793).\n  statistics:\n  - test: Kolmogorov-Smirnov test\n    p: 0.4793\n  depends_on:\n  - fig5gh-mechanosensitive-as-good\n  criterion: A claim of absence. Concentration coefficients of the two populations of\n    fig5gh-mechanosensitive-as-good (all neurons meeting each rule); two-sample\n    Kolmogorov-Smirnov test; reproduced when p >= 0.05, not reproduced otherwise.\n- id: fig6-simulation-mechanosensory-rescues\n  statement: In a population simulated from the fitted coefficients, an inhalation-driven\n    concentration change makes concentration decoding across inhalation speeds worse than within\n    speed as the change grows, and adding the mechanosensory input restores decoding of the true\n    concentration for any change.\n  source: Results, Airflow information affords tolerance to flow-dependent concentration\n    fluctuations, paragraph 1; Figures 6B and 6C; STAR Methods, Simulation of sniff-induced\n    concentration changes\n  quote: Consistently, decoders trained on the responses during slow and fast inhalations\n    classified the odor concentration worse than decoders trained using only one inhalation speed\n    as the simulated influence of the airflow on the concentration increased (Figure 6C).\n    However, supplementing this population with mechanosensory responses was sufficient to reduce\n    ambiguity and retrieve the actual concentration for any DIC (Figures 6B and 6C).\n  depends_on:\n  - fig5ef-correlated-subpopulations\n  criterion: Simulated per STAR Methods, R = Poisson(a I + b Cn) with Cn = log(Ce + k I Ce), Ce\n    0.01, 0.1, 1%, k from 0 to 1, a and b the linear-model coefficients of\n    fig5ef-correlated-subpopulations, a set to 0 for the population without mechanosensory\n    input. The Methods do not say how negative rates are handled or how many events are drawn;\n    the code (simulation_effect_of_inh_on_con_lrModel_exponential.ipynb) shifts rates to be\n    positive (+0.025), uses 20 k values, 500 simulations and a 10-fold linear SVC, and adds the\n    change as k*b*C*I on the 0.33/0.66/1 scale; the code's model is a variant. Reproduced when,\n    without mechanosensory input, the mixed-speed decoder's accuracy falls below the\n    within-speed decoders' as k grows (lower at k = 0.7 by more than one SD), and with it the\n    mixed-speed accuracy stays within one SD of within-speed accuracy at every k.\n- id: figs6h-waveforms-homogeneous\n  statement: Classifiers cannot decode the experimental condition from the spike waveform\n    features of the recorded units, suggesting homogeneous sampling of cell types across\n    conditions.\n  source: Results, Sniffing causes unstable odor responses in the PCx, paragraph 2; Figures S6G\n    and S6H\n  quote: The distributions of the waveform features were comparable across experiments, and\n    neither crossvalidated linear nor non-linear classifiers could discriminate an experimental\n    condition based on the spike waveforms of the units recorded (see STAR Methods).\n  criterion: Per STAR Methods, Spike sorting and inclusion criteria, trough-to-peak latency and\n    asymmetry index of each unit; cross-validated Naive Bayes and linear SVM for each pair of\n    experimental conditions (AUC and accuracy). Neither the folds nor the threshold for\n    \"could not\" is given; 10-fold CV, a standard choice, and readings (a) mean AUC minus one SD\n    at or below 0.5; (b) mean AUC below 0.6 for every pair. Reproduced when a reading holds for\n    every pair and both classifiers.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000931/10.1016-j.celrep.2024.114013.yaml paper/10.1016-j.celrep.2024.114013.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes: 37 claims, 37 quotes, 0 problems. Now the style rules: em dashes outside quotes, the word "rather", and ": " in plain scalars.

**Agent calls Bash**

```bash
f=claims/000931/10.1016-j.celrep.2024.114013.yaml; grep -n "—" $f | grep -v "quote:" ; grep -ni "rather" $f; python3 - <<'EOF'
import yaml
f='claims/000931/10.1016-j.celrep.2024.114013.yaml'
d=yaml.safe_load(open(f))
for c in d['claims']:
    for k in ('statement','criterion','source','inferred'):
        v=c.get(k)
        if v and ': ' in v: print(c['id'],k)
    for e in (c.get('expected') or []) if isinstance(c.get('expected'),list) else [c.get('expected')] if c.get('expected') else []:
        if ': ' in e['quantity']: print(c['id'],'quantity')
print(len(d['claims']), sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']), sum('expected' in c for c in d['claims']))
EOF
```

```
37 6 37 16
```

**Agent**

I've written `claims/000931/10.1016-j.celrep.2024.114013.yaml`. The quote checker reports 37 claims, 37 quotes, 8 statistical values and 0 problems. The style rules (no em dashes outside quotes, no "rather", no ": " in plain scalars) also check out. Nothing was committed.

**Text read**
- The version of record, as text extracted from a publisher PDF that a person supplied. It includes the main text, figure legends, STAR Methods and the supplement (legends of Figures S1 to S6). The paper has no supplementary tables, and I didn't need to open the PDF.
- The code: `iurillilab/mechano-olfactory_code` v1.1, commit 3bec502, from the Zenodo deposit doi:10.5281/zenodo.10381293. It holds MATLAB scripts and Python notebooks for each figure panel. Its panel letters follow the bioRxiv preprint, not the published figures.
- The code leaves some steps uncovered. It loads preprocessed files and helper functions that aren't in the repository. It has nothing for:
  - the inhalation clustering;
  - the phase decoding;
  - Figure 5G to 5I;
  - Figure S2C;
  - Figure S6H.

**Claims**
- 37 claims, all with quotes and criteria. 16 have expected values and 6 have statistics.
- They cover inhalation sorting, phase and speed decoding, odor responsiveness, sniff effects on responses (Figure 1H to 1L, S1), the GLM (Figure 2, S2), and airflow tuning under anesthesia, awake and after nerve section (Figure 3, S3).
- They also cover bulbectomy and motor cortex (Figure 4, S4), population decoding and encoding angles (Figure 5, S5), the simulation (Figure 6) and the waveform check (S6H).

**Where the code settles or disagrees with the Methods**
- **Odor-inhalation window:** the Methods say 0 to 5 s after odor onset; the code uses 0.4 to 5 s. The Methods window is the main reading and the code's is a variant.
- **GLM:** the code fixes the concentration coding (0, 0.33, 0.66, 1) and the penalty (lambda_1se).
- **Tests the code ran differently from the legends:** the legends name signed-rank tests for Fig 1J and 1L, but the code runs rank-sum and Kolmogorov-Smirnov tests. The legends' tests are used, with the code's as variants.
- **Fig 5C angle transform:** the Methods give 90 − |90 − Q|; the notebook computes |90 − angle|. The Methods form is used.
- **Fig 5E/F selection bound:** the code's lower bound differs slightly from the Methods' tan(π/12). The code's is a variant.
- **Fig 6 simulation:** the code models the inhalation-driven concentration change differently from the Methods. The code's model is a variant.

**Details left open, with the readings named**
- **Odor-responsiveness test (Fig 1H):** what the signed-rank test compares isn't stated. Readings: whole 5 s odor period against the preceding period, one-sided or two-sided; or the per-trial inhalation response against odorless inhalations.
- **CDI (Fig 1L):** the sample size per draw and how the mixed sample is made up. Three readings.
- **GLM "91.9% of variance":** pooled R² of condition means, per-pair R², or deviance explained.
- **Speed decoding:** whether "400 inhalations" is the total or per class.
- **Bulbectomy fraction:** the text says 15.7%, but 23 of 153 is 15.0%. Readings: pooled over neurons, or the mean of per-mouse fractions.
- **Motor cortex:** which mice hold the neurons (the code takes them from both groups), and the chi-square threshold (0.05 or 0.01).
- **Number of neurons in the angle analysis:** all 464, or 143.
- **SD for the sniff-invariant and mechanosensitive selection (Fig 5G to 5I):** per odor, or over pooled pairs.
- **Fig 5I two-way ANOVA:** its factors aren't given. Two readings.
- **Fig S2C:** which weights are used (GLM or linear model) and what makes an R² "significant".
- **Inhalation clustering:** how the dendrogram is cut when it gives three clusters.
- **Words like "similar", "monotonic", "several tens of ms" and "could not decode":** the paper reports no test for them, mostly for Fig 3B, S1D, S3E, S6H and the Fig 5 panels shown as mean ± SD. Each criterion names readings. Where a figure shows mean ± SD, decoders are judged against chance by one SD.

**Missing from the paper**
- Nothing a claim needed is missing.
- The Methods list the odor panel inconsistently: three odors at "0.01 and 1%" against the four-odor, two-concentration experiment. The author has to take odors and concentrations from the files.
- Fig 3 and the Methods disagree on the artificial airflow pulse rate (1 Hz against 750 ms intervals). It doesn't affect any criterion.

## End of run

30 turns, 7 minutes, result: success.
