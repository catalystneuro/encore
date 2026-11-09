# openneuro-ds004752 · claims · run 40657958012

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453 claims/openneuro-ds004752 paper 2>&1; ls tools
```

```
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
53:### 2. Read the paper's code
63:### 3. Write the claims file
148:### 4. Data from outside the paper's own recordings
156:### 5. Check
169:### 6. Answer questions
182:## Author
198:### 1. Establish what can be tested
325:### 2. Check the data against its description
340:### 3. Write the entry
398:### 4. Lock, check and run
409:### 5. Record the attempt
460:### 6. Hand over for verification
498:## Repeat attempts
540:## Local and remote datasets
563:## Verifier
567:### Round 1: without the author's conclusions
592:### Round 2: with the author's conclusions
[... 33 more lines not kept]
```

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
3	Version: `pilot-12`. Record this version in the attempt's provenance.
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
cd  wc -l paper/*.txt; ls paper; head -30 paper/*.txt; python tools/claims_check.py --help 2>&1 | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.78677.txt",
 "offset": 30
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/vdimakopoulos/verbal_working_memory && cd verbal_working_memory && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100 && find . -type f -not -path './.git/*' | wc -l
```

```
395ae136372be9772cdbeb09bccd677fda01b5d6 Thu Apr 28 22:44:22 2022 +0200
./Synchronize NLX-EDF/Main_Synchronize_NLX_EDF.m
./Subfunctions/tight_subplot.m
./Subfunctions/stdshade.m
./Subfunctions/shadedErrorBar.m
./Subfunctions/resetVertex.m
./Subfunctions/reref_toSeparate_Chan.m
./Subfunctions/redblue.m
./Subfunctions/plot_areaerrorbar.m
./Subfunctions/plotSpread/plotSpread/repeatEntries.m
./Subfunctions/plotSpread/plotSpread/plotSpread.m
./Subfunctions/plotSpread/plotSpread/myErrorbar.m
./Subfunctions/plotSpread/plotSpread/isEven.m
./Subfunctions/plotSpread/plotSpread/distinguishable_colors.m
./Subfunctions/plotSpread/license.txt
./Subfunctions/getTFR_granger_all_hippGridPairs.m
./Subfunctions/demo_shadedErrorBar.m
./Subfunctions/custom_blue_white_map.m
./Subfunctions/compute_Connectivity_metrics.m
./Subfunctions/bluewhitered_pos.m
[... 83 more lines not kept]
```

**Agent**

The paper's full text (version of record, Europe PMC) has Methods and figure legends. I cloned the linked code (commit 395ae13) and am reading its Granger, behavior and statistics scripts.

**Agent calls Bash**

```bash
cd $TMPDIR/verbal_working_memory && find . -type f -not -path './.git/*' | tail -33; cat README.md; wc -l Subfunctions/Granger_causality.m "Source Localization/"*.m "Publication Ready Figures/210122_Figures/DeltaGranger_EEG.m" "Publication Ready Figures/210122_Figures/Delta_Granger_EEG_incorrectTrials.m" Statistics/permutest.m Subfunctions/BehaviourAnalysis.m
```

```
./Phase Coherence Patients/Phase_Coherence_Patient_6.m
./Phase Coherence Patients/Phase_Coherence_Patient_5.m
./Phase Coherence Patients/Phase_Coherence_Patient_4.m
./Phase Coherence Patients/Phase_Coherence_Patient_3.m
./Phase Coherence Patients/Phase_Coherence_Patient_2.m
./Phase Coherence Patients/Phase_Coherence_Patient_1.m
./Load Human MTL dataset scripts/subfunctions/get_TFR_Granger.m
./Load Human MTL dataset scripts/subfunctions/getPower_trialWise.m
./Load Human MTL dataset scripts/subfunctions/getGranger_session_Wise.m
./Load Human MTL dataset scripts/subfunctions/getDataInSessions.m
./Load Human MTL dataset scripts/subfunctions/Plot_Power_correlation_all_subj_Correct_vs_Incorrect.m
./Load Human MTL dataset scripts/subfunctions/Plot_PowerCorrelation.m
./Load Human MTL dataset scripts/subfunctions/Plot_Granger_sessionWise.m
./Load Human MTL dataset scripts/subfunctions/PlotGranger_sessionWise_all_subjects.m
./Load Human MTL dataset scripts/subfunctions/Mean_granger_for_subjects_from_human_MTL_dataset.m
./Load Human MTL dataset scripts/subfunctions/MaxGranger_AnatLocationsFigure.m
./Load Human MTL dataset scripts/subfunctions/Granger_spectra_stats_Corr_vs_Incorr.m
./Load Human MTL dataset scripts/subfunctions/Granger_spectra_stats_211105.m
./Load Human MTL dataset scripts/subfunctions/Granger_spectra_stats.m
./Load Human MTL dataset scripts/subfunctions/Get_Only_Incorrect_Trials_FieldTrip.m
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory/Publication Ready Figures/210122_Figures" && cat DeltaGranger_EEG.m; echo =====; sed -n 1,177p Delta_Granger_EEG_incorrectTrials.m
```

```
%% Paths
strPaths.Main = 'F:\Vasileios\';
strPaths.Project = [strPaths.Main, 'Task Analysis\'];
strPaths.GeneralFunctions = 'F:\Vasileios\Task Analysis\Code\';
strPaths.Data = [strPaths.Main, 'Task Analysis\Data\'];
strPaths.ExtractedData = [strPaths.Main, 'Task Analysis\Extracted_Data Sternberg\'];
strPaths.Statistics = [strPaths.Main, 'Task Analysis\Code\Statistics\'];
strPaths.ChanLoc = [strPaths.Main, 'Task Analysis\Code\Channel Localization\'];
strPaths.EEGLAB_Subfunctions = [strPaths.Main,'Task Analysis\Code\Subfunctions\EEGLAB Subfunctions\'];
strPaths.Subfunctions = [strPaths.Main,'Task Analysis\Code\Subfunctions\']
strPaths.FigureData = [strPaths.Data,'Analysis Data\Figure Data\'];
% Results
strPaths.Results = [strPaths.Main,'Task Analysis\Analysis Results\'];

% FieldTrip toolbox
% strPaths.Toolboxes.FieldTrip            = 'F:\Vasileios\Toolboxes\fieldtrip-20191126\';
strPaths.Toolboxes.FieldTrip            = 'F:\Vasileios\Toolboxes\fieldtrip-20200315\';

% EEGLAB toolbox
strPaths.Toolboxes.EEGLAB               = 'F:\Vasileios\Toolboxes\eeglab14_1_1b\';
[... 313 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory" && grep -n -i "resample\|foilim\|foi\b\|cfg.foi\|tapsmofrq\|taper\|pad\b\|cfg.pad\|toilim\|latency\|granger\|ft_freqanalysis\|ft_connectivity\|channelcmb\|Heschl\|Frontal\|SetSize\|set size\|correct" "Source Localization/MainSourceAnalysisConnectivity.m" | head -120
```

```
34:[dataScalp,TrialInformationTable,dataScalp_Task_SS] = LoadEEGData(pID,Drive_Letter,'incorrect trials')
317:temp_idx = strmatch('Frontal_Inf_Oper_L', atlas.tissuelabel);
387:cfg.correctm         = 'cluster';
480:strParcels = {'Frontal','central','Temporal','Occipital'};
481:clear gdata Granger_random_trial_sampling;
484:    sprintf('\n\n\nCalculating Granger between hippocampus and %s regions\n\n\n', strParcels{iG})
492:    x = find(contains(atlas.tissuelabel,strParcels{iG}));%find(ismember(atlas.tissuelabel,'Frontal_Inf_Tri_L'));
649:    %% Granger
651:    analysis_type = 'correct trials'; %'incorrect trials'; %or 'correct trials'
652:    % Granger Causality calculation between a hippocampal contact of a depth
704:    cfg.resamplefs = 40;%200;
705:    dataBipolarResampled = ft_resampledata(cfg,dataBip);
706:    combineddata = ft_resampledata(cfg,virtsensparcel);
707:    combineddata2 = ft_resampledata(cfg,virtsensparcel2);
709:    % Select only correct trials
711:        case 'correct trials'
712:            [dataBipolar_SS,TrialInformationTableCorrect] = Get_Only_Correct_Trials_FieldTrip(dataBipolarResampled,TrialInformationTable_iEEG_clean);
713:        case 'incorrect trials'
714:            [dataBipolar_SS, TrialInformationTableCorrect] = Get_Only_Incorrect_Trials_FieldTrip(dataBipolarResampled, TrialInformationTable_iEEG_clean )
717:    %% Divide data into set sizes
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory" && sed -n 470,520p "Source Localization/MainSourceAnalysisConnectivity.m"; echo ....; sed -n 640,770p "Source Localization/MainSourceAnalysisConnectivity.m"; echo ====; cat "Source Localization/calculateGranger_random_trial_sampling.m"
```

```
cfg.funcolormap    = 'bluewhitered_pos(128)';
cfg.maskparameter = 'mask';
cfg.renderer = 'zbuffer';
cfg.funcolorlim   = [0 10];
cfg.atlas = atlas;
ft_sourceplot(cfg,statint);

%% ----------------------
%% Connectivity analysis
%First, we interpolate the statistical result and the atlas.
strParcels = {'Frontal','central','Temporal','Occipital'};
clear gdata Granger_random_trial_sampling;
visualFlag = 0;
for iG = 1:length(strParcels)
    sprintf('\n\n\nCalculating Granger between hippocampus and %s regions\n\n\n', strParcels{iG})
    clear indxtempSupL;
    cfg = [];
    cfg.interpmethod = 'nearest';
    cfg.parameter = 'tissue';
    stat_atlas = ft_sourceinterpolate(cfg, atlas, stat);
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory" && cat "Load Human MTL dataset scripts/subfunctions/Extract_task_period_Data.m"; sed -n 520,640p "Source Localization/MainSourceAnalysisConnectivity.m"
```

```
function [dataBipolar_Ret_SS] = Extract_task_period_Data(TaskPeriod,dataBipolar_SS)
nSet_Size = size(dataBipolar_SS,2);
if strcmp(TaskPeriod,'fix') %Fixation
    %% Extract 1 seconds of fixation latency
    dataBipolar_Ret_SS = {};
    fsample = dataBipolar_SS{1}.fsample;
    for iSS = 1:nSet_Size
        if ~isempty(dataBipolar_SS{iSS}.time)
            
            cfg = [];
            cfg.latency = [dataBipolar_SS{iSS}.time{1}(1) dataBipolar_SS{iSS}.time{1}(fsample)]%
            dataBipolar_Ret_SS{iSS} = ft_selectdata(cfg,dataBipolar_SS{iSS});
            
            cfg =[];
            cfg.resamplefs = 1000;
            dataBipolar_Ret_SS{iSS} = ft_resampledata(cfg,dataBipolar_Ret_SS{iSS})
        else
            dataBipolar_Ret_SS{iSS} = dataBipolar_SS{iSS};
        end
        
[... 164 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory" && grep -n "grngChan1\s*=\|grngChan2\s*=\|channelPair\s*=" -r . | head; echo ===; grep -n -i "kruskal\|multcompare\|dunn\|permut\|freq_wnd\|median(\|\[4 8\]\|4:8\|find(.*freq" "Source Localization/MeanSourceGranger.m" | head -60
```

```
./Subfunctions/Granger_random_trial_sampling_convergence.m:59:    grngChan1 = strChannelNameList{hipp_chanPairs(iPair,1)};
./Subfunctions/Granger_random_trial_sampling_convergence.m:60:    grngChan2 = strChannelNameList{hipp_chanPairs(iPair,2)};
./Source Localization/calculateGranger_random_trial_sampling.m:29:    grngChan1 = channelPair{1};
./Source Localization/calculateGranger_random_trial_sampling.m:30:    grngChan2 = channelPair{2};
./Source Localization/MainSourceAnalysisConnectivity.m:759:    % grngChan1 = 'PHL1-PHL3';
./Source Localization/MainSourceAnalysisConnectivity.m:760:    % grngChan2 = 'TSL';
./Source Localization/MainSourceAnalysisConnectivity.m:789:    channelPair = {grngChan1,grngChan2}
./Load Human MTL dataset scripts/subfunctions/getGranger_session_Wise.m:28:        grngChan1                           = strChannelNameList{hipp_chanPairs(iPair,1)};
./Load Human MTL dataset scripts/subfunctions/getGranger_session_Wise.m:29:        grngChan2                           = strChannelNameList{hipp_chanPairs(iPair,2)};
./Load Human MTL dataset scripts/Main_Granger_calculation_for_humanMTL_dataset.m:350:        grngChan1 = strChannelNameList{hipp_chanPairs(iPair,1)};
===
197:    median_CH_enc(j) = median(tempMedian_CH_enc{j});
198:    median_HC_enc(j) = median(tempMedian_HC_enc{j});
199:    median_HC_maint(j) = median(tempMedian_HC_maint{j});
200:    median_CH_maint(j) = median(tempMedian_CH_maint{j});
364:freq_wnd_a = find(freq == freq_start);
365:freq_wnd_b = find(freq == freq_end);
368:DGranger_enc(i) = min(sourceGrangerEnc_group{2,i}(freq_wnd_a:freq_wnd_b) - sourceGrangerEnc_group{1,i}(freq_wnd_a:freq_wnd_b))*100;
369:DGranger_maint(i) = max(sourceGrangerMaint_group{1,i}(freq_wnd_a:freq_wnd_b) - sourceGrangerMaint_group{2,i}(freq_wnd_a:freq_wnd_b))*100;
403:freq_wnd_a = find(freq == freq_start);
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory" && sed -n 340,470p "Source Localization/MeanSourceGranger.m"; sed -n 640,760p "Source Localization/MeanSourceGranger.m" | grep -n -i "kruskal\|ranksum\|signrank\|permut\|multcompare\|p =\|pval\|stats"
```

```
material dull

cfg = [];
cfg.method         = 'surface';
cfg.funparameter   = 'parcel';
cfg.funcolorlim    = [0 10];
cfg.funcolormap    = 'jet';
cfg.projmethod     = 'nearest';
cfg.surfinflated   = 'surface_inflated_both_caret.mat';
cfg.projthresh     = 0.8;
cfg.camlight       = 'no';
ft_sourceplot(cfg, mean_stat_maint);
view ([-70 20 50])
light ('Position',[-70 20 50])
material dull

%% DGranger across subjects
nSubjects = 15;
nSubjs =nSubjects;
x_enc = 1;
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory" && grep -rn "permutationTest(\|permutest(\|kruskalwallis\|multcompare\|signrank\|ttest" --include=*.m . | grep -v "^./Statistics/permut" | head -30; sed -n 1,60p Statistics/permutationTest.m | grep -n "%" | head -40
```

```
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:389:[h,p] = ttest(Accuracy_PatientSubject_MM(:,1),Accuracy_PatientSubject_MM(:,2))
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:395:[h,p] = ttest(Accuracy_PatientSubject_MM(:,1),Accuracy_PatientSubject_MM(:,2))
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:403:[h,p] = ttest(ResponseTime_Mean_PatientSubject_CI_MM(:,1,1),ResponseTime_Mean_PatientSubject_CI_MM(:,1,2))
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:410:[h,p] = ttest(temp(:,1),temp(:,2));        
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:508:[h,p] = ttest2(ReactionTime_TrialLevel_Corr_MM{1},ReactionTime_TrialLevel_Corr_MM{2})
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:509:fprintf('\nttest2 t-value %.2f; p = %.4f\n',0,p)
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:523:[h,p] = ttest2(ReactionTime_TrialLevel_Corr_MM{1},ReactionTime_TrialLevel_Corr_MM{2})
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:524:fprintf('\nttest2 t-value %.2f; p = %.4f\n',stats,p)
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:537:[h,p] = ttest2(ReactionTime_TrialLevel_CI{1},ReactionTime_TrialLevel_CI{2})
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:538:fprintf('\nttest2 t-value %.2f; p = %.4f\n',stats,p)
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:927:[h,p] = ttest(MedianResponseTime_Patients(:,1),MedianResponseTime_Patients(:,2));
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:942:[h,p] = ttest(MedianResponseTime_Sessions(:,1),MedianResponseTime_Sessions(:,2))
./Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory" && sed -n 1,40p Statistics/permutest.m; grep -n "Correct\|SetSize\|Setsize" Subfunctions/Get_Only_Correct_Trials_FieldTrip.m Subfunctions/Get_Separated_Set_Size_Datasets_FieldTrip.m | head; grep -n "Artifact\|Clean" "Load Human MTL dataset scripts/subfunctions/Get_Only_Clean_Trials_FieldTrip.m" | head
```

```
function [clusters, p_values, t_sums, permutation_distribution ] = permutest( trial_group_1, trial_group_2, dependent_samples, ...
    p_threshold, num_permutations, two_sided, num_clusters )
% Permutation test for dependent or independent measures of 1-D or 2-D data. 
% Based on Maris & Oostenveld 2007 for 1-D and 2-D vectors. The test 
% statistic is T-Sum - the total of t-values within a cluster of contingent
% above-threshold data points. 
% See: Maris, E., & Oostenveld, R. (2007). Nonparametric statistical 
% testing of EEG-and MEG-data. Journal of Neuroscience Methods, 164(1), 
% 177�190. https://doi.org/10.1016/j.jneumeth.2007.03.024
% 
% Important notes: 
% * Make sure you understand whether you should be using a test of
% dependent or independent samples (a within or between subjects test,
% respectively). Also make sure you know if you want a one-sided or
% two-sided test. 
% * The number of permutation sets a minimal boundary for the resulting
% p-value. This boundary is 1/(nP+1). If a very low p-value is needed, e.g.
% to survive a multiple-comparisons correction, use a sufficiently high
% number of permutations (this is also necessary in order to estimate the
% p-value with sufficient accuracy unless there is a very small number of
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory" && cat "Source Localization/getSignificant_bandsGranger_groupStats.m"; grep -n "cfg\.\|Granger_spectra_stats" "Load Human MTL dataset scripts/subfunctions/Granger_spectra_stats_211105.m" | head -40
```

```
function [sgnf_bands_enc sgnf_bands_maint stat_maint_freq stat_enc_freq] = getSignificant_bandsGranger_groupStats()
load('F:\Vasileios\Task Analysis\Analysis Results\Granger_source_level\variables\groupStats_vars\sourceGrangerEnc_group.mat')
load('F:\Vasileios\Task Analysis\Analysis Results\Granger_source_level\variables\groupStats_vars\sourceGrangerMaint_group.mat')
load('F:\Vasileios\Task Analysis\Analysis Results\Granger_source_level\variables\groupStats_vars\freq.mat')
clear dataMaint dataEnc
dataMaint{1}.label = 'Hipp - Temporal Superior Lobe';
dataMaint{2}.label = 'Temporal Superior Lobe - Hipp';
dataMaint{1}.dimord = 'subj_freq';
dataMaint{2}.dimord = 'subj_freq';
dataMaint{1}.freq = freq;
dataMaint{2}.freq = freq;

dataEnc{1}.label = 'Hipp - Temporal Superior Lobe';
dataEnc{2}.label = 'Temporal Superior Lobe - Hipp';
dataEnc{1}.dimord = 'subj_freq';
dataEnc{2}.dimord = 'subj_freq';
dataEnc{1}.freq = freq;
dataEnc{2}.freq = freq;


[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory" && grep -n "cfg\.\|ft_freqstatistics" "Statistics/permutation test FieldTrip/statistics_fr.m" | head -40
```

```
6:%   cfg.event_comparisons = a cell array containing the events numbers for
9:% cfg can contain anything that ft_freqstatistics recognizes
11:event_comparisons = cfg.event_comparisons;
19:    cfg.method           = 'montecarlo'; % use the Monte Carlo Method to calculate the significance probability
20:    cfg.statistic        = 'indepsamplesT'; % use the independent samples T-statistic as a measure to
22:    cfg.correctm         = 'fdr';
24:    cfg.tail             = 0;          % -1, 1 or 0 (default = 0); one-sided or two-sided test
25:    cfg.alpha            = 0.05;      % alpha level of the permutation test
26:    cfg.numrandomization = 2500;
27:%     cfg.neighbours = [1 1];
28:    cfg.minnbchan        = 2;          % minimum number of neighborhood channels that is
40:    cfg.design = design;
41:    cfg.ivar = [2];
42:%     cfg.uvar = 1;
43:    this_stat = ft_freqstatistics(cfg, data_comparison{1},data_comparison{2});
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory" && grep -n -i "cowan\|polyfit\|ms/item\|slope\|mean(\|median(" Subfunctions/BehaviourAnalysis.m "Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m" | head -40
```

```
Subfunctions/BehaviourAnalysis.m:42:Cowan_K = ((Performance_IN/100 + Performance_Out/100) -1)*[4 6 8];
Subfunctions/BehaviourAnalysis.m:43:sprintf('Across all sessions the capacity averaged %.2f which indicates that \nthe subject was able to maintain at least %d letters in memory.',Cowan_K(3), floor(Cowan_K(3)))
Subfunctions/BehaviourAnalysis.m:60:%% Cowan K capacity per set size
Subfunctions/BehaviourAnalysis.m:71:Cowan_K_SS = {}
Subfunctions/BehaviourAnalysis.m:72:Cowan_K_SS{1} = (Correct_SS_IN_rate{1}+Correct_SS_Out_rate{1} - 1)*4 % set size 4
Subfunctions/BehaviourAnalysis.m:73:Cowan_K_SS{2} = (Correct_SS_IN_rate{2}+Correct_SS_Out_rate{2} - 1)*6 % set size 6
Subfunctions/BehaviourAnalysis.m:74:Cowan_K_SS{3} = (Correct_SS_IN_rate{3}+Correct_SS_Out_rate{3} - 1)*8 % set size 8
Subfunctions/BehaviourAnalysis.m:86:    median(CorrectTrialsTime)/1000,std(CorrectTrialsTime)/1000, median(SS4_corr_time),std(SS4_corr_time), median(SS6_corr_time), ...
Subfunctions/BehaviourAnalysis.m:87:    std(SS6_corr_time),median(SS8_corr_time),std(SS8_corr_time))
Subfunctions/BehaviourAnalysis.m:89:%% Slope for reaction time per item
Subfunctions/BehaviourAnalysis.m:100:slope = LM.Coefficients.Estimate(2)*1000
Subfunctions/BehaviourAnalysis.m:106:MeanCorrectIN_time = mean(CorrectIN_time);
Subfunctions/BehaviourAnalysis.m:108:MeanIncorrectIN_time = mean(IncorrectIN_time);
Subfunctions/BehaviourAnalysis.m:113:MeanCorrectOut_time = mean(CorrectOut_time);
Subfunctions/BehaviourAnalysis.m:115:MeanIncorrectOut_time = mean(IncorrectOut_time);
Subfunctions/BehaviourAnalysis.m:124:    median(CorrectResponse_Time)/1000,std(CorrectResponse_Time)/1000, median(IncorrectResponse_Time)/1000,...
Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:217:        ResponseTime_Mean_PatientSubject_SS(nPatientSubject,iSS) = mean(ResponseTime_PatientSubject_SS{nPatientSubject}{iSS});
Subfunctions/Behavioural_Analysis_Sternberg Subjects/Extened_Behavior_Analysis.m:218:        Respons
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/verbal_working_memory" && sed -n 1,45p Subfunctions/BehaviourAnalysis.m; sed -n 76,100p Subfunctions/BehaviourAnalysis.m
```

```
addpath(genpath('F:\Vasileios\Toolboxes\eeglab14_1_1b\functions'))

Path = 'F:\Vasileios\Task Analysis\Data\Analysis Data\Performance Data\42 DS\';

strFilename_Session1 = [Path,'gelflog 1.txt']
strFilename_Session2 = [Path,'gelflog 2.txt']

Behav_res_s1 = readtable(strFilename_Session1,'Format','auto');
Behav_res_s2 = readtable(strFilename_Session2,'Format','auto');
%Remove the column with the boolean flag of response
Behav_res_s2 = removevars(Behav_res_s2,8);
Behav_res_s2.Properties.VariableNames{8} = 'Var8';
%Fix trial numbers
Behav_res_s2.Var1 = Behav_res_s2.Var1+50; 
Behav_res_Merged = [Behav_res_s1; Behav_res_s2]

%Assign the correct names on the vars
Behav_res_Merged.Properties.VariableNames = {'Trial Number', 'Set Size', 'Sequence', 'In', 'Out',...
    'Probed Letter','Response','Time'}

[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s -m 30 https://openneuro.org/crn/graphql -H 'Content-Type: application/json' -d '{"query":"{ dataset(id: \"ds004752\") { latestSnapshot { tag description { Name DatasetDOI } readme } } }"}' | head -c 5000
```

Result: the fetched text is not kept.

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

Read the paper, the code, and the dataset's archive description. Now writing the claims file (about 20 claims).

**Agent calls Bash**

```bash
python3 - <<'EOF'
enc=[-0.036,-0.017,-0.060,-0.006,-0.003,-0.049,-0.059,-0.040,-0.051,-0.070,-0.052,-0.022,-0.018,-0.053,-0.061]
mai=[0.025,0.093,0.065,0.035,0.021,0.039,0.042,0.017,0.050,0.018,0.020,0.012,0.020,0.085,0.069]
ienc=[0.087,0.016,-0.013,0.003,-0.002,0.025,0.042,0.013,0.012,-0.016,-0.011,0.000,0.019,0.022,-0.005]
imai=[-0.037,0.002,0.005,-0.002,0.048,-0.024,-0.036,-0.031,-0.015,-0.081,-0.062,0.003,-0.022,-0.089,-0.004]
import statistics as s
print(s.median(enc),s.median(mai),s.median(ienc),s.median(imai))
def blk(name,vals):
  for i,v in enumerate(vals,1):
    t=max(round(abs(v)*0.1,4),0.001)
    print(f"  - {{quantity: 'Participant {i}, {name}', value: {v}, tolerance: {t}}}")
blk('encoding ΔGranger, correct trials',enc); blk('maintenance ΔGranger, correct trials',mai)
EOF
```

```
-0.049 0.035 0.012 -0.022
  - {quantity: 'Participant 1, encoding ΔGranger, correct trials', value: -0.036, tolerance: 0.0036}
  - {quantity: 'Participant 2, encoding ΔGranger, correct trials', value: -0.017, tolerance: 0.0017}
  - {quantity: 'Participant 3, encoding ΔGranger, correct trials', value: -0.06, tolerance: 0.006}
  - {quantity: 'Participant 4, encoding ΔGranger, correct trials', value: -0.006, tolerance: 0.001}
  - {quantity: 'Participant 5, encoding ΔGranger, correct trials', value: -0.003, tolerance: 0.001}
  - {quantity: 'Participant 6, encoding ΔGranger, correct trials', value: -0.049, tolerance: 0.0049}
  - {quantity: 'Participant 7, encoding ΔGranger, correct trials', value: -0.059, tolerance: 0.0059}
  - {quantity: 'Participant 8, encoding ΔGranger, correct trials', value: -0.04, tolerance: 0.004}
  - {quantity: 'Participant 9, encoding ΔGranger, correct trials', value: -0.051, tolerance: 0.0051}
  - {quantity: 'Participant 10, encoding ΔGranger, correct trials', value: -0.07, tolerance: 0.007}
  - {quantity: 'Participant 11, encoding ΔGranger, correct trials', value: -0.052, tolerance: 0.0052}
  - {quantity: 'Participant 12, encoding ΔGranger, correct trials', value: -0.022, tolerance: 0.0022}
  - {quantity: 'Participant 13, encoding ΔGranger, correct trials', value: -0.018, tolerance: 0.0018}
  - {quantity: 'Participant 14, encoding ΔGranger, correct trials', value: -0.053, tolerance: 0.0053}
  - {quantity: 'Participant 15, encoding ΔGranger, correct trials', value: -0.061, tolerance: 0.0061}
  - {quantity: 'Participant 1, maintenance ΔGranger, correct trials', value: 0.025, tolerance: 0.0025}
  - {quantity: 'Participant 2, maintenance ΔGranger, correct trials', value: 0.093, tolerance: 0.0093}
  - {quantity: 'Participant 3, maintenance ΔGranger, correct trials', value: 0.065, tolerance: 0.0065}
  - {quantity: 'Participant 4, maintenance ΔGranger, correct trials', value: 0.035, tolerance: 0.0035}
[... 11 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/openneuro-ds004752/10.7554-elife.78677.yaml",
 "content": "# Claims for Dimakopoulos, Megevand, Stieglitz, Imbach & Sarnthein (2022), eLife 11:e78677,\n# on OpenNeuro ds004752.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-10-28, protocol pilot-12 as stated in docs/protocol.md.\n#\n# Text read: the version of record, full text from Europe PMC (PMC9374435, full-text XML converted\n# to text): main text, figure legends, Table 1 and Materials and methods. The supplement is\n# given by its descriptions only: Supplementary file 1 (coordinates of the hippocampal electrode\n# tips, and the ECoG locations of Participants 1 to 4) and the legends of Figure 1, figure\n# supplement 1 and Figure 4, figure supplement 1 are not in the text. No claim below rests on\n# their content beyond what the main text states.\n#\n# Code read: https://github.com/vdimakopoulos/verbal_working_memory at commit 395ae13 (MATLAB,\n# FieldTrip). It holds the preprocessing helpers (trial selection, bipolar montage, task-period\n# windows), the beamforming and Granger script (Source Localization/MainSourceAnalysisConnectivity.m),\n# the 10% trial subsampling (calculateGranger_random_trial_sampling.m), the per-participant\n# ΔGranger and figure scripts (MeanSourceGranger.m, DeltaGranger_EEG.m,\n# Delta_Granger_EEG_incorrectTrials.m), the group spectrum statistics (statistics_fr.m) and a\n# single-participant behaviour script (BehaviourAnalysis.m). It does not hold the calls of the\n# paired permutation test of Figure 4d to 4f, nor of the Kruskal-Wallis and Dunn's tests of\n# Figure 4b and 4c. Its README describes GC over [4 30] Hz at 60 Hz; the script and the Methods\n# use 40 Hz and [4 20] Hz, which are followed here.\n#\n# Data the paper used: 15 participants with drug-resistant focal epilepsy (numbered 1 to 15 in\n# Table 1, with pathology), 71 sessions of 50 trials of a modified Sternberg task. Each trial:\n# fixation [-6 -5] s, encoding (8 letters on screen, the middle 4, 6 or 8 being the items, heard\n# at the same time) [-5 -3] s, maintenance [-3 0] s, probe at 0 s; the response is IN or OUT and\n# correct or incorrect, with a response time. Recordings: hippocampal depth LFP in all 15\n# (re-referenced to a white matter contact), scalp EEG of the 10-20 system (median 17 sites,\n# re-referenced to the averaged mastoids), and in Participants 1 to 4 subdural ECoG grids or\n# strips (Participant 1 a grid of columns A to H and rows 1 to 8 over left temporal and parietal\n# cortex; Participants 2 and 3 left strips; Participant 4 right parietal). Neuralynx ATLAS at\n# 4000 Hz, downsampled to 500 Hz. LCMV beamforming sources of the scalp EEG on AAL parcels, of\n# which the dataset description says derivative virtual sensors are deposited (DLPFC, OFC, PPC,\n# AC, V1). Nine participants (5 to 14) were in Boran et al. (2019). The paper does not give the\n# mapping of its participant numbers to the dataset's subject labels; Table 1 (pathology) and\n# the ECoG participants are the only keys.\n#\n# Method fixed here for every Granger causality (GC) criterion, from the Methods and the code,\n# referred to below as \"the GC method\":\n# - Trials: correct trials of set sizes 6 and 8, without scalp EEG artifacts (Methods, Recording\n#   setup, paragraph 1; code Get_Only_Correct_Trials_FieldTrip, Set_Sizes {[6 8]},\n#   Get_Only_Clean_Trials_FieldTrip). Incorrect trials where a claim says so.\n# - Windows: encoding [-5 -3) s and maintenance [-2 0) s (Methods, Task; Figure 2h legend; code\n#   Extract_task_period_Data.m).\n# - Signals downsampled to 40 Hz (\"the Nyquist frequency=40 Hz\" in the Methods, read with the\n#   code's resamplefs = 40, so that GC is resolved over [4 20] Hz).\n# - Fourier transform by FieldTrip mtmfft with a Hann taper and 20 s padding (Methods, Spectral\n#   Granger causality; code calculateGranger_random_trial_sampling.m). The Methods say \"two Hann\n#   tapers\", which mtmfft does not produce; the code's main script uses dpss tapers with 1 Hz\n#   smoothing, run as a variant.\n# - Nonparametric spectral factorization, bivariate, unconditional (code grangercfg in\n#   MainSourceAnalysisConnectivity.m), between one hippocampal channel and one cortical channel.\n# - ΔGranger = GC hippocampus to cortex minus GC cortex to hippocampus; negative means flow from\n#   cortex to hippocampus (Results, Directed functional coupling between hippocampus and ECoG,\n#   paragraph 1; Figure 2 legend). Values are fractions (the code multiplies by 100 for plots).\n# - EEG sources: LCMV beamformer on the scalp EEG, fixed orientation, 5% regularisation, the\n#   parcel's virtual channels averaged (code MainSourceAnalysisConnectivity.m). The dataset's\n#   derivative virtual sensors are described as these sources and are used when present;\n#   recomputing them needs a head model template the paper does not name.\n# Open in the GC method, with the readings the paper allows, each run:\n# - Hippocampal channel: the paper does not say which contact. Readings (h1) the most distal\n#   hippocampal contact, the one Figure 1d localises, re-referenced to a white matter contact\n#   (Methods, Electrode localization and Recording setup); (h2) the bipolar derivation of\n#   adjacent hippocampal contacts, as the code's GetDataInBipolar does; (h3) the mean of the GC\n#   spectra over all hippocampal channels.\n# - Auditory cortex source: the Results name the \"auditory cortex\", Table 1 \"Heschl\", Figure 4b\n#   the \"temporal superior gyrus\", and the code averages the left parcels whose AAL label holds\n#   \"Temporal\". Readings (a1) the dataset's AC virtual sensor; (a2) left Heschl gyrus; (a3) left\n#   superior temporal gyrus.\n# - Per-participant ΔGranger in [4 8] Hz: (d1) the mean over the 4 to 8 Hz bins (\"We averaged\n#   ΔGranger for each participant\", Results, Directed functional coupling and the participants'\n#   performance, paragraph 1); (d2) the extreme value over 4 to 8 Hz, the minimum in encoding\n#   and the maximum in maintenance (\"maximal ΔGranger\", Figure 4d legend; code MeanSourceGranger.m\n#   and DeltaGranger_EEG.m). The code uses (d2) for correct trials and (d1) for incorrect ones.\n# - Trials entering the per-participant value of Figure 4d: (t1) all correct trials; (t2) 10% of\n#   the correct trials drawn at random, repeated 200 times (Methods, Statistics, paragraph 4),\n#   the mean (Methods) or the median (Results; code, which draws 20 times) over draws.\nschema_version: 2\ndataset:\n  archive: openneuro\n  id: ds004752\n  doi: 10.18112/openneuro.ds004752.v1.0.1\npaper: doi:10.7554/elife.78677\nclaims:\n- id: cohort-sessions\n  statement: Fifteen participants (median age 29 years, range 18 to 56, 7 male) performed the\n    modified Sternberg task in 71 sessions of 50 trials each.\n  source: Results, Task and behavior, paragraph 1; Table 1\n  quote: Fifteen participants (median age 29 years, range [18–56], 7 male, Table 1) performed a\n    modified Sternberg WM task (71 sessions in total, 50 trials each)\n  expected:\n  - quantity: participants\n    value: 15\n    tolerance: 0\n  - quantity: sessions\n    value: 71\n    tolerance: 0\n  - quantity: trials per session\n    value: 50\n    tolerance: 0\n  - quantity: median age\n    value: 29\n    tolerance: 2.9\n    unit: years\n  - quantity: male participants\n    value: 7\n    tolerance: 0\n  criterion: Counts of participants, sessions, trials and sexes are exact (tolerance 0, as a\n    count either matches or not); the differences are reported. The age range 18 to 56 is\n    checked as well.\n- id: fig1b-accuracy\n  statement: The mean correct response rate was 91% (for both IN and OUT trials) and decreased\n    with set size, from 97% at set size 4 to 89% at 6 and 83% at 8.\n  source: Results, Task and behavior, paragraph 2; Figure 1b\n  quote: The mean correct response rate was 91% (both for IN and OUT trials). The rate of correct\n    responses decreased with set size from a set size of 4 (97% correct responses) to set sizes of\n    6 (89%) and 8 (83%) (Figure 1b)\n  expected:\n  - quantity: correct response rate, all trials\n    value: 91\n    tolerance: 9.1\n    unit: '%'\n  - quantity: correct response rate, set size 4\n    value: 97\n    tolerance: 9.7\n    unit: '%'\n  - quantity: correct response rate, set size 6\n    value: 89\n    tolerance: 8.9\n    unit: '%'\n  - quantity: correct response rate, set size 8\n    value: 83\n    tolerance: 8.3\n    unit: '%'\n  criterion: The paper does not say over what the mean is taken. Readings (a) pooled over all\n    trials; (b) the mean of the 71 session rates (Figure 1b is drawn over 71 sessions); (c) the\n    mean of the 15 participant rates. All trials, before artifact rejection. Reproduced when,\n    under one reading, all four values are within tolerance and the rate falls from set size 4\n    to 6 to 8; the IN and OUT rates are reported.\n- id: capacity-cowan-k\n  statement: Across participants the memory capacity (Cowan's K) averaged 6.1.\n  source: Results, Task and behavior, paragraph 2\n  quote: Across the participants, the memory capacity averaged 6.1 (Cowan’s K, [correct IN rate\n    +correct OUT rate –1]×set size), which indicates that the participants were able to maintain\n    at least six letters in memory\n  expected:\n    quantity: Cowan's K\n    value: 6.1\n    tolerance: 0.61\n  criterion: K = (correct IN rate + correct OUT rate - 1) x set size, as the Results define it.\n    The set size and the averaging are open. Readings (a) per participant, rates over all trials\n    and set size 8, as BehaviourAnalysis.m computes it (Cowan_K(3)), then the mean over\n    participants; (b) as (a) with the median over participants (the Discussion says \"The median\n    Cowan's K=6.1\"); (c) per participant, K at set size 8 from the set size 8 rates, mean or\n    median over participants; (d) as (a) to (c) over sessions. Reproduced when one reading is\n    within tolerance.\n- id: fig1c-response-time\n  statement: The response time of correct trials (3045 trials) was 1.1 +- 0.5 s and grew with\n    set size (1.1, 1.2 and 1.3 s for 4, 6 and 8 letters, 53 ms per item); correct decisions were\n    faster than incorrect ones (1.1 against 1.3 s).\n  source: Results, Task and behavior, paragraph 2; Figure 1c\n  quote: The mean response time (RT) for correct trials (3045 trials) was 1.1±0.5 s and increased\n    with workload from set size 4 (1.1±0.5 s) to 6 (1.2±0.5 s) and 8 (1.3±0.6 s), 53 ms/item\n    (Figure 1c). Correct IN/OUT decisions were made more rapidly than incorrect decisions\n    (1.1±0.5 s vs 1.3±0.6 s)\n  expected:\n  - quantity: correct trials with a response time\n    value: 3045\n    tolerance: 304.5\n  - quantity: response time, correct trials\n    value: 1.1\n    tolerance: 0.11\n    unit: s\n  - quantity: response time, correct, set size 4\n    value: 1.1\n    tolerance: 0.11\n    unit: s\n  - quantity: response time, correct, set size 6\n    value: 1.2\n    tolerance: 0.12\n    unit: s\n  - quantity: response time, correct, set size 8\n    value: 1.3\n    tolerance: 0.13\n    unit: s\n  - quantity: slope of response time on set size\n    value: 53\n    tolerance: 5.3\n    unit: ms/item\n  - quantity: response time, incorrect trials\n    value: 1.3\n    tolerance: 0.13\n    unit: s\n  criterion: Trials pooled across participants. The slope is the linear regression of response\n    time on set size over correct trials (BehaviourAnalysis.m, fitlm). The central value is\n    called a mean in the Results, and the code prints a median under that sentence; readings\n    (a) mean and (b) median, with the standard deviation. The 3045 trials are fewer than the\n    correct trials of 71 x 50 at 91%; readings for the pool are (p1) all correct trials and\n    (p2) correct trials kept after artifact rejection. Reproduced when, under one reading, the\n    response times and the slope are within tolerance and correct trials are faster than\n    incorrect ones; the trial count is reported.\n- id: fig2bc-gamma-encoding-p1\n  statement: In Participant 1, gamma power (above 40 Hz) rose by more than 100% over fixation\n    during encoding in an occipital contact (H3) and a temporal contact over auditory cortex\n    (C2), and gamma increased significantly only in temporal and occipital-parietal contacts.\n  source: Results, Power spectral density in cortical and hippocampal recordings, paragraph 1;\n    Figure 2a to 2c\n  quote: In an occipital recording of Participant 1 (grid contact H3), strong gamma activity (>40\n    Hz) in the relative PSD occurred while the participant viewed the letters during encoding\n    (increase >100% with respect to fixation, Figure 2b). Similarly, encoding elicited gamma\n    activity in a temporal recording over auditory cortex (increase >100%, grid contact C2, Figure\n    2c)\n  statistics:\n  - about: gamma increase on grid contacts during encoding\n    test: permutation test\n    statistic: z-score > 1.96\n    p: 0.05\n    p_relation: <\n  criterion: Relative PSD as the Methods give it (Power spectral density) - multitaper\n    time-frequency analysis with 3 tapers, windows of 10 cycles, smoothing 0.2 x frequency,\n    4 to 100 Hz, 0.1 s steps, all trials averaged, baseline (PSD - PSD fixation) / PSD fixation\n    with fixation [-6 -5] s. Gamma is [60 80] Hz and encoding [-3.5 -3] s for the grid map\n    (Figure 2a legend); for C2 the last second of encoding [-4 -3] s (Figure 2c legend). The\n    trials are those of the GC method; whether the PSD used correct trials only is open, and\n    readings (a) correct trials and (b) all trials of set sizes 6 and 8 are both run. The z-score\n    test is a permutation of trials between fixation and encoding (Methods, Statistics,\n    paragraph 2 describes this null for the spatial test; the PSD test is not described\n    further). Reproduced when the relative gamma increase exceeds 100% in H3 and C2 and the\n    contacts with z > 1.96 lie in the temporal and occipital-parietal parts of the grid only.\n    Needs the ECoG grid of Participant 1.\n- id: fig2d-cortical-beta-maintenance-p1\n  statement: In Participant 1, high alpha to low beta activity ([11 14] Hz) appeared toward the\n    end of maintenance in temporal and occipital contacts.\n  source: Results, Power spectral density in cortical and hippocampal recordings, paragraph 2;\n    Figure 2b and 2d\n  quote: After the letters disappeared from the screen, activity occurred in the [11 14] Hz range\n    (high alpha/low beta, Figure 2b) toward the end of the maintenance period in temporal and\n    occipital contacts (permutation test p<0.05, Figure 2d)\n  statistics:\n  - test: permutation test\n    p: 0.05\n    p_relation: <\n  criterion: Relative PSD as in fig2bc-gamma-encoding-p1, averaged over [11 14] Hz and the\n    maintenance window [-2 0] s (Figure 2d legend). Reproduced when the contacts with a\n    significant increase over fixation (permutation of trials, p < 0.05) include temporal and\n    occipital contacts and the largest values lie there. Needs the ECoG grid of Participant 1.\n- id: hipp-beta-maintenance\n  statement: In the hippocampus of all four participants with ECoG, beta activity ([12 24] Hz)\n    rose by more than 100% toward the end of maintenance.\n  source: Results, Power spectral density in cortical and hippocampal recordings, paragraph 4;\n    Figure 2e, Figure 3c, 3h and 3m\n  quote: In the hippocampus of all four participants, we found elevated activity in the beta range\n    ([12 24] Hz) toward the end of the maintenance period (increase >100%, Figure 2e, Figure 3c, h\n    and m)\n  criterion: Relative PSD of the hippocampal channel as in fig2bc-gamma-encoding-p1, over the\n    beta band [12 24] Hz (Methods, Phase-locking value, paragraph 3). The hippocampal channel\n    follows readings h1 to h3 of the GC method. \"Toward the end\" is not timed; readings (w1)\n    [-1 0] s and (w2) [-2 0] s. The paper does not say whether \">100%\" is the band average or\n    its peak; readings (m1) the mean over the band and window and (m2) the maximum over its\n    time-frequency points. Reproduced when, under one reading, the increase exceeds 100% in all\n    four of Participants 1 to 4; partially reproduced for three.\n- id: fig2fg-plv-theta-p1\n  statement: In Participant 1, phase locking between hippocampus and auditory cortex was enhanced\n    in the theta range during maintenance (PLV 0.4 at contact C3), and theta PLV in maintenance\n    was highest to contacts over auditory cortex.\n  source: Results, Functional coupling between hippocampus and cortex, paragraph 1; Figure 2f and\n    2g\n  quote: Compared to encoding, maintenance showed enhanced PLV in the theta range between\n    hippocampal LFP and cortical ECoG (PLV=0.4 in contact C3, permutation test p<0.05, Figure\n    2f). PLV in the [4 8] Hz theta range increased significantly with several contacts over\n    auditory cortex (permutation test p<0.05, Figure 2g)\n  statistics:\n  - about: PLV maintenance against the reference period, contact C3\n    test: cluster-based non-parametric permutation test\n    p: 0.05\n    p_relation: <\n  - about: theta PLV over grid contacts\n    test: permutation test\n    p: 0.05\n    p_relation: <\n  expected:\n    quantity: theta PLV, contact C3, maintenance\n    value: 0.4\n    tolerance: 0.04\n  criterion: PLV as in the Methods (Phase-locking value) - multitaper Fourier transform with two\n    tapers, 4 to 100 Hz at 1 Hz resolution, on 2 s epochs, across trials; theta [4 8] Hz,\n    maintenance [-2 0] s (Figure 2g legend). Trials of the GC method; hippocampal channel by\n    readings h1 to h3. The comparison period is open; the Results compare with encoding and the\n    Figure 2f legend with fixation (\"against a null distribution with scrambled trials during\n    fixation and maintenance\"); readings (r1) fixation [-6 -5] s and (r2) encoding. Reproduced\n    when theta PLV at C3 in maintenance is within tolerance and exceeds the reference period by\n    the permutation test (200 trial permutations, Methods, Statistics) at p < 0.05 under one\n    reading, and the contacts with the highest maintenance theta PLV lie over auditory cortex.\n    Needs the ECoG grid of Participant 1.\n- id: fig2h-gc-reversal-p1\n  statement: In Participant 1, information flowed from auditory cortex to hippocampus during\n    encoding (net flow significant in [6 8] Hz) and reversed, from hippocampus to auditory cortex,\n    during maintenance (significant in [5 8] Hz).\n  source: Results, Directed functional coupling between hippocampus and ECoG, paragraph 1;\n    Figure 2h and 2l\n  quote: The net information flow ΔGranger (GC hipp→cortex – GC cortex→hipp) during encoding was\n    significant in the [6 8] Hz range (blue bar in Figure 2h, p<0.05 permutation test against a\n    null distribution). During maintenance, the information flow in the theta frequency range was\n    reversed\n  statistics:\n  - about: ΔGranger, encoding, [6 8] Hz\n    test: permutation test against a null distribution\n    p: 0.05\n    p_relation: <\n  - about: ΔGranger, maintenance, [5 8] Hz\n    test: permutation test against a null distribution\n    p: 0.05\n    p_relation: <\n  criterion: The GC method, between the hippocampal channel (readings h1 to h3) and grid contact\n    C2. Significance as the Methods give it (Statistics, paragraph 1) - GC recomputed 200 times\n    with the direction switched at random across trials, the true ΔGranger compared with the 5th\n    and 95th percentiles of the null distribution at each frequency. Reproduced when, under one\n    reading, ΔGranger is significantly negative in encoding and significantly positive in\n    maintenance at frequencies within [4 10] Hz; the significant bands are reported against\n    [6 8] and [5 8] Hz. Needs the ECoG grid of Participant 1.\n- id: fig2ijk-spatial-spread-p1\n  statement: In Participant 1, the strongest net flow in theta during encoding was from auditory\n    cortex contacts to hippocampus; during maintenance theta flow from hippocampus was significant\n    to auditory and occipital cortex, and this spatial pattern was significant against a null\n    distribution.\n  source: Results, Directed functional coupling between hippocampus and ECoG, paragraphs 1 and 2;\n    Figure 2i to 2k\n  quote: the maximal net information flow ΔGranger (GC hipp→cortex – GC cortex→hipp) during\n    encoding occurred from auditory cortex to hippocampus (p<0.05, permutation test, Figure 2i).\n    During maintenance, the theta ΔGranger was significant from hippocampus to both auditory\n    cortex and occipital cortex (permutation test p<0.05, Figure 2j)\n  statistics:\n  - about: encoding ΔGranger map\n    test: permutation test\n    p: 0.05\n    p_relation: <\n  - about: maintenance ΔGranger map\n    test: permutation test\n    p: 0.05\n    p_relation: <\n  criterion: ΔGranger by the GC method, averaged over [4 8] Hz (reading d1, with d2 shown), for\n    each grid contact, encoding [-5 -3] s and maintenance [-2 0] s. Per contact, the direction\n    permutation test of fig2h-gc-reversal-p1. The spatial test as in the Methods (Statistics,\n    paragraph 2) - 200 iterations, each splitting the trials into two halves and taking the\n    scalar product of the two grid vectors; the null mixes trials of fixation and the task\n    period; significant when the true distribution exceeds the 95th percentile of the null.\n    How \"exceeds\" is judged between two distributions is open; readings (s1) the median of the\n    true distribution above the null 95th percentile and (s2) at least 95% of true values above\n    it. Reproduced when the most negative encoding contact is over auditory cortex (columns A to\n    D, rows 1 to 4, the temporal part of the grid as Figure 2a shows it is read from the\n    legend's naming; the contact labels are taken from the dataset), the significant maintenance\n    contacts include auditory and occipital contacts, and the spatial test is significant.\n    Needs the ECoG grid of Participant 1.\n- id: fig3-gc-reversal-p2-p3\n  statement: The same reversal appeared in Participant 2 between auditory cortex and hippocampus\n    (encoding [6 8] Hz, maintenance [6 10] Hz) and in Participant 3 between visual cortex and the\n    right hippocampus (encoding 6 to 9 Hz, maintenance [6 8] Hz).\n  source: Results, Directed functional coupling between hippocampus and ECoG, paragraph 4;\n    Figure 3d, 3e, 3i and 3j\n  quote: Similarly in Participant 2, the time course of GC followed the same pattern between\n    auditory cortex (anterior strip electrode contact in Figure 3a) and hippocampus (Figure 3d\n    and e). ... The time course of information flow between visual cortex and hippocampus\n    (Figure 3i and j) followed the same pattern as described for the auditory cortex above\n  statistics:\n  - test: cluster-based non-parametric permutation test against a null distribution with\n      scrambled trials\n    p: 0.05\n    p_relation: <\n  criterion: As fig2h-gc-reversal-p1, with the most anterior strip contact in Participant 2 and\n    the most posterior strip contact in Participant 3 (Figure 3a and 3f legends); in\n    Participant 3 the hippocampal LFP is from the right hippocampus (Results, same paragraph).\n    Reproduced when both participants show significant negative ΔGranger in encoding and\n    significant positive ΔGranger in maintenance within [4 10] Hz; partially reproduced for one.\n- id: fig3no-p4-right-no-gc\n  statement: In Participant 4, recordings from right parietal cortex showed no significant GC\n    with the hippocampus during the task.\n  source: Results, Directed functional coupling between hippocampus and ECoG, paragraph 4; Figure\n    3n and 3o\n  quote: However, in Participant 4, the recordings from the right cortical hemisphere (Figure 3k)\n    did not show significant GC between LFP and ECoG during task performance (Figure 3n and o)\n  criterion: A claim of absence, judged on the paper's test, the direction permutation test of\n    fig2h-gc-reversal-p1 (200 permutations, p < 0.05) on the right parietal contacts of\n    Participant 4, in encoding and maintenance over [4 20] Hz. Reproduced when no contact shows\n    significant ΔGranger in theta [4 8] Hz in either period; the largest ΔGranger and the\n    contacts tested are reported.\n- id: table1-left-hemisphere-sources\n  statement: In each participant, more than 80% of the EEG sources that differed significantly\n    from fixation lay in the left hemisphere, in encoding and in maintenance.\n  source: Results, Source reconstruction of the scalp EEG, paragraph 1; Table 1\n  quote: In each participant, the proportion of significant sources in the left hemisphere\n    exceeded 80% of all significant sources\n  statistics:\n  - test: non-parametric cluster-based permutation test\n    p: 0.05\n    p_relation: <\n  data: with_inputs\n  criterion: LCMV beamforming of the scalp EEG on a grid at the AAL parcels (Methods, Source\n    reconstruction), sources of encoding and maintenance tested against fixation with\n    FieldTrip's ft_sourcestatistics, cluster-based permutation (Methods, Statistics, paragraph\n    3), p < 0.05. Needs a head model template and the AAL atlas, which the paper names only as\n    \"a precomputed head model template\" (the code's README says a 3-compartment BEM); FieldTrip's\n    standard BEM is the standard choice. Reproduced when the left share exceeds 80% in all 15\n    participants in both periods; partially reproduced when it does in at least 12. The Table 1\n    shares (81% to 100%) are compared per participant.\n- id: fig4a-group-gc-reversal\n  statement: Across the 15 participants, GC between hippocampal LFP and auditory cortex EEG\n    sources showed net flow from auditory cortex to hippocampus during encoding ([6 10] Hz) and\n    from hippocampus to auditory cortex during maintenance ([6 9] Hz and [13 15] Hz).\n  source: Results, Directed functional coupling between hippocampus and averaged EEG sources,\n    paragraph 1; Figure 4a\n  quote: During encoding, the net information flow was from auditory cortex to hippocampus (light\n    blue curve – dark blue curve, blue bar, p<0.05, group cluster-based permutation test). During\n    maintenance, the net information flow was reversed (dark red curve – light red curve, red bar,\n    p<0.05, group cluster-based permutation test), i.e., from hippocampus to auditory cortex\n  statistics:\n  - about: encoding, [6 10] Hz\n    test: group cluster-based permutation t-test\n    p: 0.05\n    p_relation: <\n    corrected: FDR\n    n: 15 participants\n  - about: maintenance, [6 9] Hz and [13 15] Hz\n    test: group cluster-based permutation t-test\n    p: 0.05\n    p_relation: <\n    corrected: FDR\n    n: 15 participants\n  criterion: The GC method between the hippocampal channel (h1 to h3) and the auditory cortex\n    source (a1 to a3), per participant, all correct trials. Group test as the Methods give it\n    (Statistics, paragraph 6) and the code runs it (statistics_fr.m) - FieldTrip\n    ft_freqstatistics, Monte Carlo, t-statistic, FDR correction, two-sided, alpha 0.05, comparing\n    the two directions' spectra across the 15 participants. The code uses independent samples\n    t with 2500 randomisations; a dependent samples t is run as a variant. Reproduced when,\n    under one reading, encoding shows significant frequencies where cortex to hippocampus\n    exceeds the reverse that overlap [6 10] Hz, and maintenance shows significant frequencies\n    where hippocampus to cortex exceeds the reverse that overlap [6 9] Hz; the bands found are\n    reported against [6 10], [6 9] and [13 15] Hz.\n- id: scalp-temporal-laplacian\n  statement: A similar GC pattern appeared with the signals of left temporal scalp electrodes,\n    and it disappeared with a Laplacian derivation.\n  source: Results, Directed functional coupling between hippocampus and averaged EEG sources,\n    paragraph 1\n  quote: A similar GC pattern emerged when using the signals from left temporal scalp electrodes\n    but was eliminated when using a Laplacian derivation\n  criterion: The GC method between the hippocampal channel (h1 to h3) and left temporal scalp\n    electrodes, re-referenced to the averaged mastoids (Methods, Recording setup). The paper does\n    not name the electrodes or the Laplacian; readings (e1) T3, (e2) T5, (e3) the mean of their\n    spectra; the Laplacian by FieldTrip ft_scalpcurrentdensity (spline method), the standard\n    choice, with the nearest-neighbour Hjorth derivation as a variant. Per participant\n    ΔGranger in [4 8] Hz (d1 and d2). Reproduced when, under one electrode reading, encoding\n    ΔGranger is below maintenance ΔGranger by the paired permutation test of fig4d-reversal-all\n    at p < 0.05 with the mastoid reference, and the same test is not significant after the\n    Laplacian.\n- id: fig4bc-auditory-strongest\n  statement: Theta net flow was strongest between hippocampus and auditory cortex, toward the\n    hippocampus during encoding (ΔGranger -0.049, p = 0.0009) and toward the cortex during\n    maintenance (ΔGranger 0.034, p = 0.001); other areas showed weaker flow in the same\n    directions.\n  source: Results, Directed functional coupling between hippocampus and averaged EEG sources,\n    paragraph 2; Figure 4b and 4c\n  quote: During encoding, the mean information flow was strongest from auditory cortex to\n    hippocampus (ΔGranger=−0.049, p=0.0009, Kruskal-Wallis test, Figure 4b). ... the strongest\n    flow appeared from hippocampus to auditory cortex (ΔGranger=0.034, p=0.001, Kruskal-Wallis\n    test)\n  statistics:\n  - about: encoding, across cortical areas\n    test: Kruskal-Wallis test, Dunn's test\n    p: 0.0009\n    corrected: Bonferroni\n    n: 15 participants\n  - about: maintenance, across cortical areas\n    test: Kruskal-Wallis test, Dunn's test\n    p: 0.001\n    corrected: Bonferroni\n    n: 15 participants\n  expected:\n  - quantity: auditory cortex ΔGranger [4 8] Hz, encoding\n    value: -0.049\n    tolerance: 0.0049\n  - quantity: auditory cortex ΔGranger [4 8] Hz, maintenance\n    value: 0.034\n    tolerance: 0.0034\n  criterion: Per participant and area, ΔGranger in [4 8] Hz by the GC method with the readings\n    h, d and t of the opening comment. The group value is called a mean in the Results and a\n    median in the Figure 4b legend; readings (g1) mean and (g2) median over the 15 participants.\n    Areas are the left-hemisphere sources the dataset holds as virtual sensors (AC, DLPFC, OFC,\n    PPC, V1); the code's set is AC, LPFC, PPC, V1 and Broca. A Kruskal-Wallis test across areas\n    of the participant values, followed by Dunn's test with Bonferroni correction. Reproduced\n    when, under one reading, both values are within tolerance, the Kruskal-Wallis test has\n    p < 0.05 in each period, and auditory cortex has the most negative value in encoding and\n    the most positive in maintenance; the values of other areas are reported against [-0.03 0]\n    in encoding and below 0.02 in maintenance.\n- id: fig4d-reversal-all\n  statement: The reversal of theta net flow between hippocampus and auditory cortex appeared in\n    each of the 15 participants, negative in encoding (median -0.049) and positive in\n    maintenance (median 0.034), p = 4.1e-10 by a paired permutation test, correct trials only.\n  source: Results, Directed functional coupling and the participants' performance, paragraph 1;\n    Figure 4d\n  quote: The reversal of ΔGranger appeared in all 15 participants individually (Figure 4d). We\n    averaged ΔGranger for each participant in the [4 8] Hz theta frequency range. The ΔGranger\n    between hippocampus and auditory cortex, was negative during encoding and was positive during\n    maintenance in the theta frequency range (p=4.1e-10, paired permutation test)\n  statistics:\n  - test: paired permutation test\n    p: 4.1e-10\n    n: 15 participants\n  expected:\n  - quantity: median ΔGranger [4 8] Hz, encoding\n    value: -0.049\n    tolerance: 0.0049\n  - quantity: median ΔGranger [4 8] Hz, maintenance\n    value: 0.034\n    tolerance: 0.0034\n  criterion: Per participant ΔGranger between the hippocampal channel and the auditory cortex\n    source by the GC method, readings h, a, d and t of the opening comment. The median is over\n    the 15 participants; the figure code also pools the three ECoG values (DeltaGranger_EEG.m),\n    shown as a variant. Paired permutation test of encoding against maintenance values (Methods,\n    Statistics, paragraph 5, N = 200 permutations). A p of 4.1e-10 cannot come from 200\n    permutations, nor from the 32768 sign flips of 15 pairs, so the p is judged at 0.05 and the\n    smallest p the test can give is reported with the exact sign-flip p. Reproduced when, under\n    one reading, encoding ΔGranger is negative and maintenance ΔGranger positive in all 15\n    participants, both medians are within tolerance, and the paired test has p < 0.05;\n    partially reproduced when the test and the medians hold and the sign pattern holds in 12 to\n    14 participants.\n- id: table1-heschl-dgranger-correct\n  statement: Table 1 reports, for each participant, a negative ΔGranger to Heschl gyrus in\n    encoding and a positive one in maintenance on correct trials.\n  source: Table 1, columns Heschl ΔGranger correct trials\n  inferred: The per-participant values are in Table 1 only; its legend names them and the\n    Results state the sign pattern (fig4d-reversal-all).\n  depends_on:\n  - fig4d-reversal-all\n  expected:\n  - {quantity: 'Participant 1, encoding', value: -0.036, tolerance: 0.0036}\n  - {quantity: 'Participant 2, encoding', value: -0.017, tolerance: 0.0017}\n  - {quantity: 'Participant 3, encoding', value: -0.060, tolerance: 0.006}\n  - {quantity: 'Participant 4, encoding', value: -0.006, tolerance: 0.001}\n  - {quantity: 'Participant 5, encoding', value: -0.003, tolerance: 0.001}\n  - {quantity: 'Participant 6, encoding', value: -0.049, tolerance: 0.0049}\n  - {quantity: 'Participant 7, encoding', value: -0.059, tolerance: 0.0059}\n  - {quantity: 'Participant 8, encoding', value: -0.040, tolerance: 0.004}\n  - {quantity: 'Participant 9, encoding', value: -0.051, tolerance: 0.0051}\n  - {quantity: 'Participant 10, encoding', value: -0.070, tolerance: 0.007}\n  - {quantity: 'Participant 11, encoding', value: -0.052, tolerance: 0.0052}\n  - {quantity: 'Participant 12, encoding', value: -0.022, tolerance: 0.0022}\n  - {quantity: 'Participant 13, encoding', value: -0.018, tolerance: 0.0018}\n  - {quantity: 'Participant 14, encoding', value: -0.053, tolerance: 0.0053}\n  - {quantity: 'Participant 15, encoding', value: -0.061, tolerance: 0.0061}\n  - {quantity: 'Participant 1, maintenance', value: 0.025, tolerance: 0.0025}\n  - {quantity: 'Participant 2, maintenance', value: 0.093, tolerance: 0.0093}\n  - {quantity: 'Participant 3, maintenance', value: 0.065, tolerance: 0.0065}\n  - {quantity: 'Participant 4, maintenance', value: 0.035, tolerance: 0.0035}\n  - {quantity: 'Participant 5, maintenance', value: 0.021, tolerance: 0.0021}\n  - {quantity: 'Participant 6, maintenance', value: 0.039, tolerance: 0.0039}\n  - {quantity: 'Participant 7, maintenance', value: 0.042, tolerance: 0.0042}\n  - {quantity: 'Participant 8, maintenance', value: 0.017, tolerance: 0.0017}\n  - {quantity: 'Participant 9, maintenance', value: 0.050, tolerance: 0.005}\n  - {quantity: 'Participant 10, maintenance', value: 0.018, tolerance: 0.0018}\n  - {quantity: 'Participant 11, maintenance', value: 0.020, tolerance: 0.002}\n  - {quantity: 'Participant 12, maintenance', value: 0.012, tolerance: 0.0012}\n  - {quantity: 'Participant 13, maintenance', value: 0.020, tolerance: 0.002}\n  - {quantity: 'Participant 14, maintenance', value: 0.085, tolerance: 0.0085}\n  - {quantity: 'Participant 15, maintenance', value: 0.069, tolerance: 0.0069}\n  criterion: Values computed as in fig4d-reversal-all, with the same readings. Tolerance 10% of\n    each value, and at least 0.001, the precision at which Table 1 prints them. The paper's\n    participant numbers must be matched to the dataset's subjects by Table 1's pathology and\n    the ECoG participants; where the match is not unique, the match is reported as an\n    assumption. Reproduced when, under one reading, the sign matches the table in all 30\n    cells and at least half of the values are within tolerance; partially reproduced when the\n    signs match in at least 26 cells. The number within tolerance is reported.\n- id: fig4e-lpfc-no-reversal\n  statement: The directionality and its reversal were absent for other areas such as lateral\n    prefrontal cortex, whose net flow had a lower median and higher variability (p = 0.16,\n    paired permutation test, correct trials).\n  source: Results, Directed functional coupling and the participants' performance, paragraph 1;\n    Figure 4e\n  quote: The directionality and its reversal was missing for all other areas, e.g., lateral\n    prefrontal cortex (p=0.16, paired permutation test, Figure 4e)\n  statistics:\n  - test: paired permutation test\n    p: 0.16\n    n: 15 participants\n  criterion: A claim of absence, judged on the paper's test. Per participant ΔGranger in [4 8]\n    Hz between the hippocampal channel and the lateral prefrontal source (the dataset's DLPFC\n    virtual sensor; the code's LPFC parcel uses the mean over 4 to 8 Hz, reading d1), correct\n    trials, then the paired permutation test of encoding against maintenance values (200\n    permutations). Reproduced when p >= 0.05; not reproduced when p < 0.05 with maintenance\n    above encoding. The median difference is reported. The same test on the other areas\n    (OFC, PPC, V1) is shown as a variant, since the Results say \"all other areas\".\n- id: fig4f-incorrect-no-reversal\n  statement: On incorrect trials, the net flow between auditory cortex and hippocampus did not\n    have the same direction in all participants and did not reverse (p = 0.37, paired\n    permutation test).\n  source: Results, Directed functional coupling and the participants' performance, paragraph 2;\n    Figure 4f; Table 1, columns Heschl ΔGranger incorrect trials\n  quote: For incorrect trials, the net information flow ΔGranger from auditory cortex to\n    hippocampus did not show the same directionality in all participants and did not reverse in\n    direction (p=0.37, paired permutation test, Figure 4f)\n  statistics:\n  - test: paired permutation test\n    p: 0.37\n    n: 15 participants\n  criterion: A claim of absence, judged on the paper's test. Per participant ΔGranger in [4 8]\n    Hz between the hippocampal channel and the auditory cortex source on incorrect trials of\n    set sizes 6 and 8, by the GC method (the code uses the mean over 4 to 8 Hz for incorrect\n    trials, reading d1, with d2 shown); the paired permutation test of encoding against\n    maintenance values (200 permutations). Reproduced when p >= 0.05; not reproduced when\n    p < 0.05 with maintenance above encoding. The signs per participant are compared with\n    Table 1 (encoding 0.087, 0.016, -0.013, 0.003, -0.002, 0.025, 0.042, 0.013, 0.012, -0.016,\n    -0.011, 0.000, 0.019, 0.022, -0.005; maintenance -0.037, 0.002, 0.005, -0.002, 0.048,\n    -0.024, -0.036, -0.031, -0.015, -0.081, -0.062, 0.003, -0.022, -0.089, -0.004, for\n    Participants 1 to 15) and the effect size is reported.\n- id: balanced-correct-subset\n  statement: With correct trials subsampled to the number of incorrect trials (10%), the reversal\n    was equally present (p < 0.0005).\n  source: Results, Directed functional coupling and the participants' performance, paragraph 2;\n    Figure 4d legend\n  quote: We calculated the GC in a subset of correct trials (median of 200 permutations of a\n    number of correct trials that equals the mean percentage of incorrect trials=10%); the effect\n    was equally present for the subset of correct trials (p<0.0005)\n  statistics:\n  - test: paired permutation test\n    p: 0.0005\n    p_relation: <\n    n: 15 participants\n  depends_on:\n  - fig4d-reversal-all\n  criterion: As fig4d-reversal-all with reading t2 - per participant, 10% of the correct trials\n    drawn at random, GC recomputed, 200 draws (Methods, Statistics, paragraph 4), the median\n    over draws (Results) with the mean (Methods) as a variant. Reproduced when the paired\n    permutation test of encoding against maintenance has p < 0.05 and encoding ΔGranger is\n    negative and maintenance ΔGranger positive in at least 13 of 15 participants. The paper's\n    p < 0.0005 is below what 200 permutations resolve, so the smallest attainable p and the\n    exact sign-flip p are reported.\n"
}
```

```
File created successfully at: claims/openneuro-ds004752/10.7554-elife.78677.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/openneuro-ds004752/10.7554-elife.78677.yaml",
 "old_string": "it. Reproduced when the most negative encoding contact is over auditory cortex (columns A to\n    D, rows 1 to 4, the temporal part of the grid as Figure 2a shows it is read from the\n    legend's naming; the contact labels are taken from the dataset), the significant maintenance",
 "new_string": "it. Auditory cortex contacts are C2, C3 and the contacts around C2, as the paper names them\n    (Figure 2c, 2f and 2j legends); occipital is H3 (Figure 2b legend). Reproduced when the most\n    negative encoding contact is an auditory cortex contact, the significant maintenance"
}
```

```
The file claims/openneuro-ds004752/10.7554-elife.78677.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/openneuro-ds004752/10.7554-elife.78677.yaml paper/10.7554-elife.78677.txt; grep -n "—\| rather " claims/openneuro-ds004752/10.7554-elife.78677.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import yaml;d=yaml.safe_load(open('claims/openneuro-ds004752/10.7554-elife.78677.yaml'))
def w(o,p=''):
  if isinstance(o,dict): [w(v,p+'.'+str(k)) for k,v in o.items()]
  elif isinstance(o,list): [w(v,p+str(i)) for i,v in enumerate(o)]
  elif isinstance(o,str) and ': ' in o: print(p,o[:80])
w(d)
print(sum('criterion' in c for c in d['claims']))"
```

```
21
```

**Agent**

I wrote `claims/openneuro-ds004752/10.7554-elife.78677.yaml`. The quote checker reports 21 claims, 20 quotes, 18 statistical values and 0 problems.

**Text read:** the version of record from Europe PMC (PMC9374435): main text, figure legends, Table 1 and Methods. Of the supplement, the text gives only descriptions: Supplementary file 1 (electrode coordinates) and the legends of the two figure supplements are absent. No claim rests on them.

**Code read:** `vdimakopoulos/verbal_working_memory` at commit 395ae13. It settles the 40 Hz downsampling, the trial selection (correct trials, set sizes 6 and 8, artifact-free), the time windows, the Granger settings, the min/max reduction for each participant, the group statistic, and how Cowan's K and the response-time slope are computed. The calls for the paired permutation test and for the Kruskal-Wallis and Dunn's tests are not in the repository.

**Claims:**
- 21 in all: 20 with quotes, and one, `table1-heschl-dgranger-correct`, marked `inferred` because its per-participant values appear only in Table 1.
- 17 carry statistics and all 21 have criteria.
- They cover behaviour (cohort, accuracy, Cowan's K, response time), ECoG in Participants 1 to 4 (power, phase locking, Granger reversal, spatial spread, no effect in Participant 4), and the EEG-source results across all 15 participants (left-hemisphere sources, group Granger, the left temporal scalp electrodes with and without a Laplacian, auditory cortex strongest, reversal in every participant, Table 1 values, no reversal in prefrontal cortex or on incorrect trials, the balanced 10% subset).

**Details the paper leaves open, with the readings named:**
- **Hippocampal channel:** the most distal contact, a bipolar pair as in the code, or the mean over contacts.
- **Auditory cortex source:** the dataset's AC sensor, Heschl gyrus, or superior temporal gyrus.
- **Theta ΔGranger per participant:** the mean over 4 to 8 Hz (Results) or the extreme value (legend "maximal", and the code).
- **Trials for each participant's value:** all correct trials, or 10% of them redrawn 200 times, taking the mean (Methods) or the median (Results).
- **Taper:** Hann (Methods). The code's dpss is run as a variant.
- **Group value:** mean or median, and whether the three ECoG values are pooled in, as the figure code does.
- **Behaviour:** whether averages are over trials, sessions or participants; mean or median response time; which trials make up the 3045.
- **Power analysis:** how the window "toward the end" of maintenance is read, and whether ">100%" is the band average or its peak.
- **Phase locking:** the comparison period, fixation (legend) or encoding (Results).
- **Spatial test:** how "exceeds the 95th percentile" is judged.
- **Scalp result:** which left temporal electrodes, and which Laplacian.
- **Areas in Figure 4b and 4c:** which areas enter the Kruskal-Wallis test.
- **Group test variant:** dependent against independent samples t.

**Missing or inconsistent in the paper:**
- **Participant numbers:** the paper never maps them to subjects; only Table 1's pathology and the ECoG participants can match them to the dataset.
- **p-values below what the test resolves:** p = 4.1e-10 and p < 0.0005 are below what 200 permutations, or exact sign flips over 15 pairs, can give. These claims are judged at 0.05 and the smallest attainable p is reported.
- **Head model:** it is not named, so the left-hemisphere source claim needs outside data (`with_inputs`).
- **ECoG:** the dataset description mentions only depth iEEG, so the ECoG claims may not be testable on this dataset.

## End of run

28 turns, 5 minutes, result: success.
