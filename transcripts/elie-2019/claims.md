# elie-2019 · claims · run 42947709232

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; ls claims | head; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml
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
[... 301 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat paper/aa-4.data-description.txt | head -60; cat papers/datasets/elie-2019.yaml; grep -n elie claims/*.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1006698.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1006698.txt",
 "offset": 152,
 "limit": 170
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1006698.txt",
 "offset": 322,
 "limit": 320
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/julieelie/PoissonTimeVaryingInfo && cd PoissonTimeVaryingInfo && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | head -100
```

```
978020328321c7ed83be12c0152bed85ec77e218 Mon Apr 1 13:49:30 2019 -0700
./info_model_Calculus_wrapper.m
./cuminfo_callsemantic.m
./selVoc.m
./info_cumulative_wrapper.m
./Tutorial_TimeVarying_Information.mlx
./slurm_savio_RunCumInfo_SemanticCells.m
./PoissonGaussianNeuralResponses.m
./insideMultiMat_Dim.m
./organiz_data4coherence.m
./slurm_script_AN_CumInfo_patchcorrection.m
./cumulative_info_poisson_model_calculus_MCJK.m
./info_callsemantic.m
./updatePath.m
./stimulusCorrelations.m
./cumulative_info_poisson_model_MCJK_wrapper.m
./info_model_Calculus_wrapper2.m
./README.md
./organiz_SpikeArray4coherence.m
./ScriptPlotInfoSemanticCells.m
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/PoissonTimeVaryingInfo && wc -l *.m README.md && cat README.md
```

```
81 Cumulative_Info_AN.m
   114 Markov_entropy.m
   150 PoissonGaussianNeuralResponses.m
   254 PoissonTestNeuralResponses.m
   139 ScriptPlotInfoSemanticCells.m
   462 Semantic_NeuroInfo_Poisson_savio.m
    58 cumInfo_4AN.m
    30 cumInfo_MC_4AN.m
   684 cuminfo_callsemantic.m
    73 cumulative_info_poisson_model_MCJK_wrapper.m
   342 cumulative_info_poisson_model_calculus_MCJK.m
   441 info_callsemantic.m
   836 info_cuminfo_callsemantic.m
   406 info_cumulative_model_Calculus.m
   183 info_cumulative_wrapper.m
    77 info_model_Calculus_wrapper.m
   117 info_model_Calculus_wrapper2.m
   144 info_poisson_model_calculus.m
    56 insideMultiMat.m
    81 insideMultiMat_Dim.m
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/PoissonTimeVaryingInfo && cat ScriptPlotInfoSemanticCells.m
```

```
%load('[removed: a home directory path]/Documents/CODE/data/matfile/ModMatInfo/Models_InfoPoisson_Site4_L1500R1900_e23_s0_ss2_win16_exactCumInfo.mat')
DataMkv1=load('[removed: a home directory path]/Documents/CODE/data/matfile/ModMatInfo/Models_InfoPoisson_Site4_L1500R1900_e23_s0_ss2_MarkovHistory1_1.mat','Data');
%R=load('Models_GLMPoisson_Site4_L1500R1900_e23_s0_ss2.mat')
load('[removed: a home directory path]/Documents/CODE/data/matfile/ModMatInfo/Models_GLMPoisson_Site4_L1500R1900_e23_s0_ss2_InfoOnly_ExactCumInfo.mat')
% Find the number of windows that run
WinMax=sum(~isnan(Model.Ceiling.info));
%WinFirsts=[1 6 11];
% Calculate the mean spike rate
Mean_SR = nan(19,1);
for ww=1:19
    Mean_SR(ww)=mean(DataMkv1.Data.y_wholeset{ww}*50);%data are the number of spike in 20ms windows so *50 to obtain nb spikes per s
end

figure(1)
% Information
subplot(1,3,1)
Info_MatrixPlot_y_left = [Model.Ceiling.info(1:WinMax), Model.Semantic.info(1:WinMax), Model.Floor.info(1:WinMax)];
Info_MatrixPlot_x_left = repmat((1:WinMax)',1,3);
SPA_Plot_y_right = Mean_SR(1:WinMax);
SPA_Plot_x_right = 1:WinMax;
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/PoissonTimeVaryingInfo && grep -n -i -E "CII|k300|tau|fitnlm|lsqcurvefit|ttest|fitlm|anova|fano|fdr|benjamini|sskernel|ssvkernel|KDE|Floor|Ceil|Exp\b|expected|ResponseDelay|Win\s*=|Bin_ms|0\.6|threshold|3\*|ErrorCum|NB|Nb_Boot|5000000|100000|0\.2\b" *.m | grep -v "^ScriptPlot" | cut -c1-220 | head -150
```

```
Cumulative_Info_AN.m:27:Nb_Kth = min([length(DataCell.Kth_Neigh_JK) length(DataCell.Kth_Neigh)]);
Cumulative_Info_AN.m:35:ConvThresh = 0.2;
Cumulative_Info_AN.m:38:Nb_Win = length(P_YgivenS);
Cumulative_Info_AN.m:39:Icum_EstMonteCarloOpt = nan(1,Nb_Win);
Cumulative_Info_AN.m:40:Icum_EstMonteCarloOpt_err = nan(1,Nb_Win);
Cumulative_Info_AN.m:41:Icum_EstMonteCarloOpt_bcorr = nan(1,Nb_Win);
Cumulative_Info_AN.m:47:MC_Samp = nan(1,Nb_Win);
Cumulative_Info_AN.m:49:fprintf('**** Monte Carlo with optimal # samples and Jackknife kk=%d/%d *****\n', kk, Nb_Kth);
Cumulative_Info_AN.m:50:for tt=2:Nb_Win
Cumulative_Info_AN.m:52:    fprintf('Time point %d/%d\n', tt, Nb_Win);
Cumulative_Info_AN.m:61:    if Icum_EstMonteCarloOpt_err(tt)>(3*ConvThresh)
Cumulative_Info_AN.m:65:    DataCell.(sprintf('Kth%d',kk)).Nb_Win = Nb_Win;
PoissonGaussianNeuralResponses.m:1:function [PG_Index, FanoFactor_Index, Wins, Ymean, Yvar] = PoissonGaussianNeuralResponses(Trials,ParamModel,SWITCH, Cellname, Spectro)
PoissonGaussianNeuralResponses.m:7:    ParamModel.MinWin = 10; % end point of the first analysis window (spectrogram and neural response)
PoissonGaussianNeuralResponses.m:10:    ParamModel.MaxWin = 600; %end point of the last anaysis window for...
PoissonGaussianNeuralResponses.m:54:NbStim = length(Trials);
PoissonGaussianNeuralResponses.m:58:FanoFactor_Index = nan(WinNum,1);
PoissonGaussianNeuralResponses.m:59:Ymean = nan(WinNum,NbStim);
PoissonGaussianNeuralResponses.m:60:Yvar = nan(WinNum,NbStim);
PoissonGaussianNeuralResponses.m:65:    Win = Wins(ww);
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/PoissonTimeVaryingInfo && grep -n -i -E "exponential|expfit|fit\(|CCI|semantic index|confusion|mi2p|fzero|fminsearch|Rand|random" *.m | cut -c1-200 | head -40; echo ----; cat selVoc.m; sed -n 60,240p Semantic_NeuroInfo_Poisson_savio.m
```

```
PoissonTestNeuralResponses.m:59:    yBootLast = zeros(length(trial), nBoot);            % to store the values of the last random data
cuminfo_callsemantic.m:235:if strcmp(ParamModel.CIType, 'CICRand')
cuminfo_callsemantic.m:236:    fprintf(1,'Cumulative information for random categories\n')
cuminfo_callsemantic.m:238:    Data.cum_info_catRand = struct();
cuminfo_callsemantic.m:245:        Keep = find(strcmp(FNames, 'cum_info_catRand'));
cuminfo_callsemantic.m:248:        Old_Stop = find(isnan(Old.Data.cum_info_catRand.MonteCarloOpt_bcorr),1) -1;
cuminfo_callsemantic.m:250:        if isempty(Old_Stop) && length(Old.Data.cum_info_catRand.MonteCarloOpt_bcorr)==(ParamModel.MaxWin_cumInfo/ParamModel.Increment) && isreal(Old.Data.cum_info_catRand.M
cuminfo_callsemantic.m:251:            Old_Stop = length(Old.Data.cum_info_catRand.MonteCarloOpt_bcorr);
cuminfo_callsemantic.m:252:            Data.cum_info_catRand.MonteCarloOpt_raw = Old.Data.cum_info_catRand.MonteCarloOpt_raw;
cuminfo_callsemantic.m:253:            Data.cum_info_catRand.MonteCarloOpt_bcorr = Old.Data.cum_info_catRand.MonteCarloOpt_bcorr;
cuminfo_callsemantic.m:254:            Data.cum_info_catRand.MonteCarloOpt_err = Old.Data.cum_info_catRand.MonteCarloOpt_err;
cuminfo_callsemantic.m:255:            Data.cum_info_catRand.MonteCarloOpt_Samples  = Old.Data.cum_info_catRand.MonteCarloOpt_Samples;
cuminfo_callsemantic.m:257:        elseif isempty(Old_Stop) && isreal(Old.Data.cum_info_catRand.MonteCarloOpt_bcorr(end)) %The code already run but need to run further
cuminfo_callsemantic.m:259:            Old_Stop = length(Old.Data.cum_info_catRand.MonteCarloOpt_bcorr);
cuminfo_callsemantic.m:261:            [Data.cum_info_catRand.MonteCarloOpt_raw, Data.cum_info_catRand.MonteCarloOpt_bcorr, Data.cum_info_catRand.MonteCarloOpt_err, Data.cum_info_catRand.MonteCarloOpt
cuminfo_callsemantic.m:264:            Data.cum_info_catRand.MonteCarloOpt_raw(1:Old_Stop) = Old.Data.cum_info_catRand.MonteCarloOpt_raw(1:Old_Stop);
c
[... 247 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/PoissonTimeVaryingInfo && sed -n 1,140p info_callsemantic.m
```

```
function [ParamModel, Data, InputData, Wins]=info_callsemantic(PSTH,JackKnifeTrials,VocType, ParamModel,  Calfilename)
FIG=0;

%% Deals with input parameters
if nargin<4
    ParamModel = struct();
end
if  ~isfield(ParamModel,'MinWin') || isempty(ParamModel.MinWin)
    ParamModel.MinWin = 10; % end point of the first analysis window (spectrogram and neural response)
end
if ~isfield(ParamModel,'MaxWin') || isempty(ParamModel.MaxWin)
    ParamModel.MaxWin = 1000; %end point of the last anaysis window for...
    ... neural response and end point of the largest analysis window for...
        ... spectrogram
end

if ~isfield(ParamModel,'Increment') || isempty(ParamModel.Increment)
    ParamModel.Increment = 10; %increase the size of the spectro window with a Xms pace
end
if ~isfield(ParamModel,'NeuroBin') || isempty(ParamModel.NeuroBin)
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/PoissonTimeVaryingInfo && cat info_model_Calculus_wrapper2.m | sed -n 1,117p; sed -n 1,60p info_poisson_model_calculus.m
```

```
function [Info]=info_model_Calculus_wrapper2(PSTH, FirstTimePoint, LastTimePoint, CatList, CatListRand, Response_samprate)


NbStim = size(PSTH,1);
% Change the grouping parameter to a vector if not a vector
if nargin<4
    fprintf(1,'No input for categories\nNo information about category is calculated\n');
    CatList_in = [];
    NbCat = 1;
elseif iscell(CatList) && ischar(CatList{1})
    CatList_in = nan(1,NbStim);
    % Number of categories of stims
    IdCats = unique(CatList);
    NbCat = length(IdCats);
    for ss =1:NbCat
        CatList_in(find(strcmp(CatList, IdCats(ss))))=ss;
    end
elseif iscell(CatList) && isnumeric(CatList{1})
    CatList_in = cell2mat(CatList);
     % Number of categories of stims
[... 158 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/PoissonTimeVaryingInfo && sed -n 1,80p cumulative_info_poisson_model_calculus_MCJK.m | grep -v "^\s*$"; grep -n -E "N_MC|MaxMC|Nb_MC|ConvThresh|5\*10|5e6|10\^5|100000" cumulative_info_poisson_model_MCJK_wrapper.m cuminfo_callsemantic.m cumulative_info_poisson_model_calculus_MCJK.m | head -30
```

```
function [Icum, HY, HYgivenS, Icum_corr_mean, Icum_corr_std, N_MC_tot]=cumulative_info_poisson_model_calculus_MCJK(P_YgivenS_Full,P_YgivenS_JK, NTrials, varargin)
%% Calculates the cumulative information in a neural response given conditional probability distribution of responses given stims
% at each time point.  Although it is assumed that this stimulus conditional probability is time
% independent (i.e know that stim identity and the rate at a previous time does not tell you 
% about the rate at the current time - as in a poisson distribution), the joint probability
% distribution is not making the cumulative information calculation
% difficult.
    % To calculate the cumulative information at a given time bin T, one
    % needs to estimate the distribution of joint probabilities of reponse
    % sequences. This distribution can be very very large as the number of
    % time bins in the neural response sequence increases. This algorithm
    % uses a Monte Carlo approximation to estimate
    % this joint distribution and calculate the entropy of the response and the
    % conditional entropy (entropy of the response given the event
    % (stimulus)), and finally the cumulative mutual information. The
    % number of samples used in the Monte Carlo is upper bounded by
    % MaxMCParameter.
    % The algorithm expects as input two cell arrays (1 x T) of T matrices
    % (c x N) containing the conditional probability of observing a reponse
    % c given the stimulus N at time t.
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/PoissonTimeVaryingInfo && sed -n 1,48p PoissonTestNeuralResponses.m; sed -n 60,100p PoissonTestNeuralResponses.m; sed -n 140,220p PoissonTestNeuralResponses.m; sed -n 60,116p PoissonGaussianNeuralResponses.m
```

```
function [Poisson_P, noiseCC, noiseCC_P, noiseCCA, noiseCCA_P, noiseCCC, noiseCCC_P, noiseCCCA, noiseCCCA_P] = PoissonTestNeuralResponses(Res,ParamModel)

% Global argurments
figFlg=0;     % Flag for plotting - 1 summary plots, 2 debugging plots + summary plots
nBoot = 1000; % Number of boot points

% Arguments that are passed.
if nargin<2
    ParamModel = struct();
end
if  ~isfield(ParamModel,'MinTime') || isempty(ParamModel.MinTime)
    ParamModel.MinTime = 10; % beginning point of analysis
end
if ~isfield(ParamModel,'MaxTime') || isempty(ParamModel.MaxTime)
    ParamModel.MaxTime = 600; %end point of analysis
end
if ~isfield(ParamModel,'Increment') || isempty(ParamModel.Increment)
    ParamModel.Increment = 10; %increase the size of the spectro window with a Xms pace
end

[... 209 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,128p paper/aa-4.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && mkdir -p mlx && cd mlx && unzip -o -q ../PoissonTimeVaryingInfo/Tutorial_TimeVarying_Information.mlx && ls -R | head; grep -o -i -E "exponential|CII|semantic index|fit[a-z]*|tau|k300" matlab/document.xml | sort | uniq -c
```

```
.:
[Content_Types].xml
_rels
matlab
metadata

./_rels:

./matlab:
document.xml
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/PoissonTimeVaryingInfo && sed -n 240,352p Semantic_NeuroInfo_Poisson_savio.m
```

```
%% Compute coherence and or the spectrum of the KDE of PSTH to determine the optimal window size, the scale at which neural response information is maximized
if SWITCH.BestBin
    ParamModel.Response_samprate = Res.Response_samprate;
    
    % COHERENCE on RAW spike trains
    %Data processing group spike trains in two sets containing all stims
    %but half of the trials each
    [HalfTrain1, HalfTrain2, ResponseDuration]=organiz_SpikeArray4coherence(Res.Spike_array(DataSel),ParamModel);
    
    % Compute coherence
    [CoherenceStruct]=compute_coherence_mean(HalfTrain1, HalfTrain2,Res.Response_samprate);
    CoherenceStruct.ResponseDuration = ResponseDuration;
    OptimalFreqCutOff.CoherenceStruct = CoherenceStruct;
    
    
    % Power spectrum density of KDE of spike rates
    % First retrieve the KDE of the spike patterns
    SignalTot_local = nan(nvoc,ParamModel.MaxWin);
    for vv=1:nvoc
        SignalTot_local(vv,:) = Res.PSTH_KDE_Filtered{DataSel(vv)}(1:ParamModel.MaxWin) .* hann(ParamModel.MaxWin)';
[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -t claims | head -5; f=claims/$(ls -t claims | head -1); grep -E "^[a-z_]+:|^  [a-z_]+:|^- [a-z_]+:" $f | sort | uniq -c | sort -rn | head -30; sed -n 1,60p $f; ls tools; python tools/claims_check.py --help 2>&1 | head -20
```

```
zhu-2022.yaml
zhuang-2025.yaml
zhong-2026.yaml
zandvakili-2015.yaml
zhang-2021.yaml
     15   expected:
     13   depends_on:
      4   statistics:
      2   source: Results, paragraph 5; Figure 2b
      1 schema_version: 2
      1 paper: doi:10.1038/s41562-022-01334-6
      1 dataset:
      1 claims:
      1 checks:
      1 - id: task-structure
      1 - id: suppfig9-predict-from-corr
      1 - id: suppfig8b-individual-no-separation
      1 - id: suppfig7b-not-nonlinguistic
      1 - id: suppfig7a-com-overlap
      1 - id: suppfig6b-duration-metric
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; grep -l "archive: crcns" claims/*.yaml | head -3
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
   "required": [
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:])"; sed -n 1,15p claims/bruno-2017.yaml; grep -n "^dataset\|archive:" claims/bruno-2017.yaml
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 150 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/elie-2019.yaml",
 "content": "# Claims for Elie & Theunissen (2019), PLoS Computational Biology 15(9):e1006698, \"Invariant neural\n# responses for sensory categories revealed by the time-varying information for communication calls\",\n# doi:10.1371/journal.pcbi.1006698, on CRCNS data set aa-4 (doi:10.6080/K00C4T06).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-11,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record (PMC6762074, open access), as JATS XML flattened to text under\n# paper/: main text, Methods, Table 1, and the legends of Figures 1 to 10 and of S1 to S7 Fig. The\n# supplement is the seven figures whose legends are in the text; it has no other file. No PDF was\n# supplied. The extraction drops every displayed equation: the information formulas, the\n# coherence-based information (Methods, Time-varying spike rate estimation), the exponential model\n# of the cumulative information (Results, Time-varying Information for 3 example neurons), the\n# definition of the CII (Methods, Calculation of the expected value of categorical information) and\n# the confusion-matrix information. Where the words around an equation or the code fix it, the\n# criteria say so; where not, the equation is named as open and the reading the text allows is given.\n# The author may read those equations in the published article (they are not figures). The data\n# set's description (paper/aa-4.data-description.txt) was read only to know what it holds; no claim\n# comes from it.\n#\n# Code read: https://github.com/julieelie/PoissonTimeVaryingInfo, commit 97802032 (2019-04-01), the\n# repository the Methods and Data Availability link. It holds the per-unit calculations. The stimulus\n# selection selVoc.m keeps the call types Ag (the Wsst call, Ws), Be, DC, Di, LT, Ne, Te, Th and song\n# (whines and noise are dropped). info_callsemantic.m and info_model_Calculus_wrapper2.m compute the\n# instantaneous information in 10 ms bins ending at 10, 20, ..., 600 ms after stimulus onset\n# (MinWin 10, Increment 10, NeuroBin 10, ResDelay 0); the Poisson mean of a bin is the sum of the\n# KDE rate (sampled at 1 kHz) over the bin; spike counts are summed from 0 to MaxY = 20; the lower\n# bound on the mean is 1/20 (MuLims default, info_poisson_model_calculus.m); p(y|c) is the mean of\n# p(y|s) over the stimuli of the category and categories are weighted equally; the random-category\n# floor permutes the call-type labels once per unit (randperm in info_callsemantic.m); the fixed\n# rate code uses each stimulus's KDE rate averaged over 0 to 600 ms. cumulative_info_poisson_model_\n# calculus_MCJK.m and its wrapper do the Monte Carlo with importance sampling, 10^5 samples per chunk,\n# up to 5x10^6, target error 0.2 bits, and stop at the first bin whose error exceeds 0.6 bits; the\n# bootstrap of the jackknife uses NbBoot_CumInfo = 20. PoissonTestNeuralResponses.m holds the Poisson\n# log-likelihood test (1000 simulated sets) and the noise correlation; PoissonGaussianNeuralResponses.m\n# the Fano factor. The repository does not hold the locally adaptive KDE that makes the rates\n# (PSTH_KDE_Filtered and JackKnife_KDE_Filtered are loaded already made), the coherence function\n# (compute_coherence_mean, called but not present), the Benjamini-Hochberg step, the selection of the\n# 404 and the 337 units, the exponential fits, the expected categorical information and the CII, or\n# any population statistic, regression or anatomical analysis. Those come from the paper alone.\n#\n# Data the paper used (Results, opening paragraph; Methods, Animals and stimuli, Neurophysiological\n# and histological procedures, Table 1).\n# - Subjects. Six adult zebra finches (Taeniopygia guttata), 4 males and 2 females, urethane\n#   anesthetized, head fixed. Table 1 names five of them (BlaBro09xxF, GreBlu9508M, LblBlu2028M,\n#   WhiWhi4522M, YelBlu6903F); the sixth bird's electrode tracks were not recovered and it is left out\n#   of the anatomy.\n# - Recordings. One (1 bird) or two (5 birds) arrays of 16 tungsten electrodes (2 rows of 8), one per\n#   hemisphere, at several sites per penetration (4.2 +- 2 sites per bird and hemisphere, 400 to\n#   2550 um deep), in Field L (L1, L2, L3), CLM, CMM and NCM. Spikes by voltage threshold, sorted\n#   offline into 914 single auditory units (SNR > 5); spike times aligned to stimulus onset.\n# - Stimuli. At each site a new random subset of a bank of 486 vocalizations of 15 adults and 8\n#   chicks, 9 call types (So, DC, Te, Ne, Ws, Di, Th for adults; Be, LT for chicks), up to 3 bouts per\n#   call type from each of 10 callers (3 adult females, 3 adult males, 2 female and 2 male chicks), up\n#   to 141 stimuli, 114 on average per unit (sd 22, 34 to 123), 10 trials each (9 to 11), random order,\n#   75 dB SPL. The search stimuli (song, white noise, distance call, modulation-limited noise) are not\n#   analysed (S4 Fig legend).\n# - Units analysed. 404 of the 914 units, those from which call type could be decoded above chance in\n#   Elie & Theunissen 2015 (Eur J Neurosci 41:546-567, the paper's reference 40); 337 of them with\n#   significant stimulus cumulative information; 303 of the 337 with an anatomical location (Table 1).\n# - Measured variables. Spike arrival times per trial over the first 600 ms after stimulus onset; the\n#   call type and caller of each stimulus; the anatomical area and x, y, z coordinates of each site\n#   (relative to the midline, the rostro-caudal position of the LPS peak, and the brain surface).\n#\n# Shared method. Criteria refer to these by letter.\n# R, rates. For each unit and stimulus, the 9 to 11 trials of 600 ms are combined into a time-varying\n#   rate at 1 kHz by the locally adaptive kernel bandwidth optimisation of Shimazaki and Shinomoto\n#   (the paper's reference 42, ssvkernel) (Methods, Time-varying spike rate estimation, paragraph 2).\n#   A stimulus with no spike in any trial gets the constant rate 1/(2*Ntrials*600) per ms, one with a\n#   single spike 1/(Ntrials*600) (same paragraph). Jackknife rates are the same estimate on each set\n#   of Ntrials-1 trials (Methods, Bias correction). Open, whether the rates are low-pass filtered\n#   before binning (the code's inputs are named KDE_Filtered, the filter is not in the code; the text\n#   says the rates \"were sampled at 10ms (Nyquist limit frequency of 50Hz)\"); readings (a) bin the KDE\n#   rate as it is, (b) low-pass it at 50 Hz first. Either is expected to give the same outcome.\n# B, bins. 60 bins of 10 ms, [0,10) to [590,600) ms after onset; the Poisson mean of a bin is the KDE\n#   rate summed over the bin, bounded below by 1/20 (code, info_callsemantic.m and\n#   info_poisson_model_calculus.m; Methods, The instantaneous information). Stimuli are the nine call\n#   types of selVoc.m.\n# I, information. Instantaneous stimulus and category information per bin, and cumulative stimulus\n#   and category information from 0 ms to each bin by Monte Carlo with importance sampling, as the\n#   Methods (Information theoretic calculations to Bias correction) and the code above give them,\n#   bias-corrected by the jackknife and with errors from 20 bootstraps of the jackknife. A unit's\n#   cumulative curve ends at the first bin whose error exceeds 0.6 bits (Methods, The cumulative\n#   information, last paragraph). The paper's code is in MATLAB; a port is acceptable when it follows\n#   the code.\n# F, exponential fit. The equation is lost from the text read. Its words fix three parameters, a\n#   latency dt, a time constant tau and a saturation k as a fraction of I_Max, with I_Max = log2(n_stim)\n#   for stimuli and log2(n_cat) for categories (Fig 3D and Fig 7 legends). Reading, unless the printed\n#   equation says otherwise, I(t) = k*I_Max*(1 - exp(-(t - dt)/tau)) for t > dt and 0 before, fitted by\n#   least squares to each unit's bias-corrected cumulative curve over the bins it has. k300 is the\n#   model's value at 300 ms divided by I_Max (Results, paragraph after the model equation). Open, what\n#   \"well fitted\" means for the 214 units kept (Fig 7 legend); the paper gives no rule. Readings (a) the\n#   fits of both curves converge with tau > 0, dt >= 0 and 0 < k <= 1; (b) as (a), and the 214 units\n#   whose summed MSE of the two fits is lowest.\n# C, CII. Per unit and bin, from the cumulative category information CCI and three references (Methods,\n#   Calculation of the expected value of categorical information). Floor, the cumulative information\n#   for categories formed by one random permutation of the call-type labels (code, info_callsemantic.m\n#   and cuminfo_callsemantic.m, CICRand). Ceiling, the stimulus cumulative information capped at\n#   log2(n_c), n_c = 9 (Results, Analysis of the categorical information, paragraph 1). Expected value,\n#   by the three steps of the Methods: invert mi = log2 n + p log2 p + (1-p) log2((1-p)/(n-1)) for the\n#   probability p of correct decoding of the n stimuli (the information of a confusion matrix with p on\n#   the diagonal and (1-p)/(n-1) elsewhere, equal stimulus probabilities), group the joint\n#   probabilities (p/n on the diagonal, (1-p)/(n(n-1)) elsewhere) by the unit's own call types, and\n#   take the information of the grouped matrix. The CII formula is lost from the text read; the text\n#   fixes CII = 0 at the floor, 1 at the expected value and 2 at the ceiling and says it lies between 0\n#   and 2. Reading, unless the printed equation says otherwise, the piecewise linear map\n#   CII = (CCI - Floor)/(Exp - Floor) when CCI <= Exp, and 1 + (CCI - Exp)/(Ceil - Exp) above it. A\n#   unit's time-averaged CII is its mean CII from 50 to 300 ms (Fig 9A legend).\n# P, population. Population analyses use the 337 units (claim units-337), the Poisson checks the 404\n#   (Methods, Information theoretic calculations, paragraph 2). Open, how a unit whose cumulative curve\n#   ended early enters a population average at later bins; readings (a) it is left out of the average\n#   from the bin where it ends, (b) its last value is carried forward. Averages are means over units\n#   with 2 SEM bands, as in the Fig 6 and Fig 9 legends.\n# A, anatomy. The 303 units with a location (Table 1). Open, the distance to the L2 axis; the paper\n#   says the sites were aligned on the oblique rostro-caudal long axis of L2 (Fig 10 legend) and that\n#   values rise \"as one moved rostrally or caudally\" from it. Readings (a) the absolute perpendicular\n#   distance, in the parasagittal plane, from each site to the line of the L2 axis, (b) the absolute\n#   rostro-caudal distance from the L2 axis at the site's depth. The regressions report F(2,195) or\n#   F(1,195) degrees of freedom; the printed p-values (0.0042, 0.00258, 0.0047) match F(1,195) and not\n#   F(2,195), so the regression is read as one predictor (the distance) on about 197 units (the units\n#   with a location among the well-fitted units, for the tau and k300 regressions), and the printed\n#   p-values are the targets.\n#\n# Outside data. The 404-unit selection rests on the decoding analysis of Elie & Theunissen 2015\n# (reference 40); this paper does not describe its method beyond \"call-types could be decoded above\n# chance level\". The vocalization bank is at http://bit.do/ZebeVocBank (Data Availability); no claim\n# needs it. The model neurons of Fig 1 are simulations; the code repository holds the tutorial's\n# model cell data (ModelCell_InfoCumInfo_Tutorial.mat).\nschema_version: 2\npaper: doi:10.1371/journal.pcbi.1006698\nclaims:\n- id: units-404\n  statement: The analysis uses 404 of the 914 isolated single units, those from which call type\n    could be decoded above chance in the authors' earlier study.\n  source: Methods, Neurophysiological and histological procedures, last paragraph\n  quote: The data of neural responses from 404 out of 914 isolated single units were used in this\n    study. The 404 neurons were selected based on a prior analysis that showed that this subset of\n    units were not only auditory but also contained information about call-types\n  data: with_inputs\n  expected:\n  - quantity: single units in the data set\n    value: 914\n    tolerance: 0\n  - quantity: units selected\n    value: 404\n    tolerance: 40\n  criterion: The selection is the decoding analysis of Elie & Theunissen 2015 (Eur J Neurosci\n    41:546-567, reference 40), which this paper does not describe. Readings (a) a list of the 404\n    units from the data set's documentation or the 2015 paper, (b) the 2015 decoding selection redone\n    as that paper describes it. Reproduced when the data set holds 914 single units and a selection\n    of 404 +- 40 units can be made under one reading; the units, not only the count, are carried to\n    later claims. Blocked as methods_underspecified when neither reading can be carried out.\n- id: units-337\n  statement: Of the 404 units, 337 have at least one time point with significant stimulus\n    cumulative information, and these 337 form the population analysed.\n  source: Methods, Information theoretic calculations, paragraph 2\n  quote: categorical instantaneous and cumulative information were calculated on a restricted set of\n    337 neurons that presented at least one time point with a significant value of stimulus\n    cumulative information (significant threshold set as 3 times the local error\n  depends_on:\n  - units-404\n  expected:\n    quantity: units with significant stimulus cumulative information\n    value: 337\n    tolerance: 34\n  criterion: Methods R, B and I on the 404 units. A unit is kept when, in at least one bin, its\n    bias-corrected stimulus cumulative information exceeds 3 times its error (the bootstrap\n    standard error of Methods, Bias correction). Open, whether the first bin (where the cumulative\n    information equals the instantaneous information) counts; readings (a) all bins, (b) bins from\n    20 ms. Reproduced when the count is within tolerance under one reading.\n- id: s1-temporal-resolution\n  statement: Low-pass filtering at 50 Hz (10 ms bins) keeps 96.7% +- 6.9% of the coherence-based\n    information of the spike trains, only 88 of 404 units lose more than 5%, and 98.8% +- 1.6% of\n    the power of the KDE rates lies below 50 Hz.\n  source: Methods, Time-varying spike rate estimation, paragraph 4; S1 Fig\n  quote: Over all units, 96.7% ±6.9% (mean ± SD) of information was conserved by a lowpass filtering\n    at 50Hz and only 88 out of 404 cells had information losses greater than 5%. ... On average\n    across units, the cumulative power reached 98.8%±1.6% (mean ± SD) at 50Hz\n  depends_on:\n  - units-404\n  expected:\n  - quantity: mean percentage of coherence information below 50 Hz\n    value: 96.7\n    tolerance: 6.9\n    unit: percent\n  - quantity: units losing more than 5% of the information\n    value: 88\n    tolerance: 8.8\n  - quantity: mean percentage of KDE rate power below 50 Hz\n    value: 98.8\n    tolerance: 1.6\n    unit: percent\n  criterion: Tolerances on the two percentages are the stated SDs (protocol). Coherence, per unit\n    the coherence between the PSTHs of two halves of the trials over all stimuli, converted to the\n    coherence between one spike train and the mean response by the formula of the Methods (lost\n    from the text read; reference 99, Hsu, Borst and Theunissen 2004), and I_AR = -integral of\n    log2(1 - coherence) over frequency, from 0 to 50 Hz against 0 to 500 Hz (S1 Fig legend). Spike\n    trains at 10 kHz as the Methods say (code, organiz_SpikeArray4coherence.m; the coherence function\n    is not in the repository). Power, per unit, the KDE rates of all stimuli, each Hanning-windowed\n    over 600 ms and concatenated, Welch periodogram in 200 ms windows at 1 kHz, cumulative power\n    normalised to the total, read at 50 Hz (Methods; code, Semantic_NeuroInfo_Poisson_savio.m).\n    Reproduced when all three values are within tolerance; partially when one or two are.\n- id: fig1-model-neurons\n  statement: For simulated Poisson neurons (rate, onset and temporal codes, 4 stimuli, 10 trials),\n    the KDE recovers the model rates with an average error below 0.02 spikes/ms, the cumulative\n    information approaches the 2-bit maximum, and the temporal neuron's peak instantaneous\n    information is 0.5 bits.\n  source: Results, Time-varying information for model neurons, paragraphs 2 and 3; Figure 1\n  quote: over all stimuli and model neurons, the average error was less than 0.02 spikes/ms ... in\n    the Temporal neuron ( Fig 1C & 1F ) a peak instantaneous information of 0.5 bits is expected as\n    1 out 4 stimuli will be almost perfectly discriminated\n  data: elsewhere\n  where: GitHub julieelie/PoissonTimeVaryingInfo, commit 97802032, ModelCell_InfoCumInfo_Tutorial.mat\n    and Tutorial_TimeVarying_Information.mlx\n  expected:\n  - quantity: average KDE error, all model neurons and stimuli\n    value: 0.02\n    unit: spikes/ms\n  - quantity: peak instantaneous information, temporal neuron\n    value: 0.5\n    tolerance: 0.05\n    unit: bits\n  criterion: A simulation, not the recordings. The model rates are not given numerically in the\n    paper; the tutorial's model cells are used. Reproduced when the mean absolute difference between\n    KDE and model rates is below 0.02 spikes/ms, the cumulative information of each model neuron\n    reaches at least 1.8 bits (90% of 2 bits) before it ends, and the temporal neuron's peak\n    instantaneous information is within tolerance.\n- id: fig2a-poisson-test\n  statement: For most units (240 of 404) the spike counts in 10 ms bins cannot be told from a\n    Poisson distribution in 90% of the bins, only 5 of 404 deviate in 40% of the bins, and on\n    average 10.5% of bins are rejected.\n  source: Results, Avian auditory neurons have approximate Poisson statistics, paragraph 2; Figure 2A\n  quote: For the large majority of cells (240/404), the empirical spike count could not be\n    distinguished from a Poisson distribution for 90% of the time bins. For a small number of\n    neurons (5/404) non-Poisson spike count statistics could be observed in 40% of the time bins.\n    The mean number of rejected time bins was 10.5%.\n  depends_on:\n  - units-404\n  expected:\n  - quantity: units with Poisson not rejected in 90% of bins\n    value: 240\n    tolerance: 24\n  - quantity: units with Poisson rejected in 40% of bins\n    value: 5\n    tolerance: 0.5\n  - quantity: mean percentage of rejected bins\n    value: 10.5\n    tolerance: 1.05\n    unit: percent\n  criterion: Per unit, stimulus and 10 ms bin, the Poisson log-likelihood of the trial counts with\n    the delete-one (jackknife) KDE mean of each trial, against 1000 log-likelihoods of 10 Poisson\n    samples with the full KDE mean; two-tailed p; Benjamini-Hochberg at 0.05 within each unit over\n    all its stimulus-bin tests (Methods, Testing the poisson assumptions). The code\n    (PoissonTestNeuralResponses.m) takes a one-tailed p, 1 minus the fraction of simulated\n    log-likelihoods above the data's, has no FDR step, and uses bins from 10 to 610 ms; the Methods\n    are followed and the code's p is a variant. Open, the cut-offs; readings (a) rejected in at most\n    10% of bins and in at least 40%, (b) rejected in under 10% and over 40%. Reproduced when the\n    three values are within tolerance under one reading; the count of 5 is held to +- 1 unit, as 10%\n    of 5 is below one unit. Partially reproduced when the mean is within tolerance and one count is.\n- id: fig2cd-fano-factor\n  statement: The time-averaged Fano factor of the population is 1.04 (SEM 0.04) and is not\n    significantly different from 1.\n  source: Results, Avian auditory neurons have approximate Poisson statistics, paragraph 2; Figure\n    2C and 2D\n  quote: The mean Fano factor for the population was 1.04 with SEM of 0.04 ( Fig 2D )\n  depends_on:\n  - units-404\n  expected:\n    quantity: mean time-averaged Fano factor over units\n    value: 1.04\n    tolerance: 0.04\n  criterion: Per unit, 10 ms bin and stimulus, the variance over the mean of the trial spike counts,\n    averaged over stimuli (Fig 2C legend), then over the 60 bins (Fig 2D). The code\n    (PoissonGaussianNeuralResponses.m) sets the ratio to 1 where variance equals mean, which covers\n    stimuli with no spike in the bin; open, readings (a) as the code, (b) such stimuli left out. A\n    claim of absence. The legend says \"Fano Factors are not significantly different from 1\" and\n    names no test; readings (i) a two-sided one-sample t-test of the 404 time-averaged values against\n    1, (ii) a two-sided Wilcoxon signed-rank test against 1, both at 0.05. Reproduced when the mean is\n    within tolerance and neither test finds a difference; not reproduced when a test finds one. The\n    mean and its SEM are reported either way.\n- id: fig2b-noise-correlations\n  statement: Noise correlations between successive 10 ms bins are small, centred near zero with a\n    slight positive skew, while stimulus correlations between consecutive bins are high, centred\n    around 0.4.\n  source: Results, Avian auditory neurons have approximate Poisson statistics, paragraphs 3 and 5;\n    Figure 2B\n  quote: Significant noise correlations were observed (red bars versus non-significant values shown\n    in blue), but they were small, centered around zero and their distribution showed a slight\n    positive skew. ... the distribution of stimulus correlation (correlation of mean rate between\n    pairs of consecutive time bins in the trial average response of each stimulus) across the neural\n    population show high positive values centered around 0.4\n  depends_on:\n  - units-404\n  expected:\n    quantity: centre of the distribution of stimulus correlations over units\n    value: 0.4\n    tolerance: 0.04\n  criterion: Noise correlation, per unit, the Pearson correlation of the trial deviations from the\n    delete-one KDE mean in successive bins, pooled over pairs of bins and stimuli (Methods, Testing\n    the poisson assumptions, paragraph 3; the code pools the sums of products and of squares,\n    PoissonTestNeuralResponses.m); significance per unit against the 1000 simulated Poisson sets,\n    two-tailed, as the code does. Stimulus correlation, per unit, the Pearson correlation over\n    stimuli of the mean counts in consecutive bins, averaged over bin pairs; the text does not say\n    whether the correlation runs over stimuli at each bin pair or over bins within each stimulus, and\n    both are readings. The paper gives no number for \"small\". Reproduced when the median of the\n    noise correlations is within +- 0.05 of zero and their skewness is positive (a fixed choice, the\n    paper giving no threshold), and the median stimulus correlation is within tolerance under one\n    reading.\n- id: fig3-5-example-neurons\n  statement: Three example units show distinct codes, a high-rate unit responding to all calls with\n    high cumulative information, a low-rate unit selective for distance calls with a selective onset,\n    and a unit selective for Wsst calls with a long latency (100 to 300 ms).\n  source: Results, Time-varying Information for 3 example neurons, paragraph 1; Figures 3 to 5\n  quote: The neurons in Figs 4 and 5 have much lower firing rates and exhibit selectivity for a\n    call-type, the Distance Call (DC) and the Wsst Call (Ws) respectively.\n  criterion: The paper does not name the three units, so they cannot be found in the data set unless\n    the rasters of S4 to S6 Fig identify them. If they cannot be identified, the claim is blocked as\n    methods_underspecified. If they can, reproduced when the category-averaged rate of unit 2 is\n    highest for DC and that of unit 3 for Ws, and unit 1's stimulus cumulative information exceeds\n    that of the other two at 300 ms.\n- id: fig6a-onset-sustained-information\n  statement: Across the population the firing rate shows an onset followed by a lower sustained\n    response, while the instantaneous information about stimuli and about categories stays almost\n    constant, so the onset and sustained responses are equally informative in bits/s.\n  source: Results, Rate and time-varying information, Population analysis, paragraph 1; Figure 6A\n  quote: On average, avian cortical auditory neurons show an onset response followed by a sustained\n    response ... The instantaneous information, however, remains almost constant during the entire\n    time. This is true both for the information about individual stimuli or the information about\n    categories.\n  depends_on:\n  - units-337\n  criterion: Methods R, B, I and P. Population mean over the 337 units of the mean rate over stimuli\n    and of the bias-corrected instantaneous stimulus and category information, per bin. The paper\n    gives no rule for \"almost constant\"; this one is fixed here. The onset peak is the maximum\n    population rate within 0 to 100 ms and the sustained level the mean rate over 150 to 600 ms.\n    Reproduced when the onset peak exceeds the sustained level by at least 50%, and for both kinds of\n    information the mean over 150 to 600 ms is within 20% of the mean over the bins from 20 ms to the\n    rate peak plus 30 ms. Not reproduced otherwise.\n- id: fig6c-new-information\n  statement: The new information acquired per bin (the slope of the cumulative information) about\n    categories stays roughly constant while the rate falls between 50 and 150 ms, whereas the new\n    information about stimuli decreases and is correlated with the spike rate.\n  source: Results, Rate and time-varying information, Population analysis, paragraph 1; Figure 6C\n  quote: The new information for categories is relatively constant (red line Fig 6C ) and similar to\n    the instantaneous information about category (yellow line Fig 6A ), while the spike rate is\n    drastically decreasing between 50 and 150ms. ... In contrast, the new information for individual\n    stimuli decreases and is, on average, remarkably correlated with spike rate ( Fig 6C ).\n  depends_on:\n  - units-337\n  criterion: Methods R, B, I and P. Per bin, the population mean of the difference between successive\n    bias-corrected cumulative values (Fig 6C legend), for stimuli and categories, and the population\n    mean rate. The paper names no test; this rule is fixed here. Reproduced when (1) the Pearson\n    correlation over bins from 20 to 600 ms between the stimulus slope and the rate is positive with\n    p < 0.05, (2) the stimulus slope over 150 to 600 ms is lower than over 20 to 100 ms, and (3) the\n    category slope averaged over 150 to 200 ms is at least 80% of its average over 50 to 100 ms while\n    the rate drops by more than that over the same spans. Partially reproduced when (1) and (2) hold\n    and (3) does not.\n- id: fig6b-fixed-rate-fraction\n  statement: A fixed rate code captures only 24% of the stimulus cumulative information of the\n    time-varying rates at 100 ms and 21% at 300 ms, and 50% and 41% of the categorical cumulative\n    information.\n  source: Results, Rate and time-varying information, Population analysis, paragraph 2; Figure 6B\n  quote: a fixed rate code (or assumption) captures only 24% of the information at 100 ms and 21% at\n    300 ms. ... for categorical information, a fixed rate code captures 50% of the information at 100\n    ms and 41% at 300 ms.\n  depends_on:\n  - units-337\n  expected:\n  - quantity: fixed over time-varying stimulus cumulative information, 100 ms\n    value: 24\n    tolerance: 2.4\n    unit: percent\n  - quantity: fixed over time-varying stimulus cumulative information, 300 ms\n    value: 21\n    tolerance: 2.1\n    unit: percent\n  - quantity: fixed over time-varying category cumulative information, 100 ms\n    value: 50\n    tolerance: 5\n    unit: percent\n  - quantity: fixed over time-varying category cumulative information, 300 ms\n    value: 41\n    tolerance: 4.1\n    unit: percent\n  criterion: Methods R, B, I and P. The fixed rate code gives each stimulus, in every bin, its KDE\n    rate averaged over 0 to 600 ms (Fig 6B legend; code, CsteRate in info_callsemantic.m), and its\n    cumulative information is computed as for the time-varying rates. Open, the ratio; readings (a)\n    the population mean of the fixed-rate curve over the population mean of the time-varying curve,\n    as Fig 6B plots them, (b) the mean over units of each unit's ratio. With P's two readings of\n    units that end early, four readings. Reproduced when all four values are within tolerance under\n    one reading; partially when the two stimulus values or the two category values are.\n- id: fig7a-time-constants\n  statement: For the 214 of 337 units well fitted by exponentials, the time constants range from 100\n    to 600 ms, with a mean of 459 ms for stimulus and 372 ms for categorical cumulative information,\n    a significant difference.\n  source: Results, Rate and time-varying information, Population analysis, paragraph 3; Figure 7A\n  quote: The range of time constants observed across the population of neurons was large (100 ms-600\n    ms) with average time constants of 459 ms for cumulative stimulus information and 372 ms for\n    cumulative categorical information. This difference in means of time constants is statistically\n    significant (Paired t-test t(214) = 3.49, p = 0.00058)\n  statistics:\n  - about: stimulus against category time constants\n    test: paired t-test\n    statistic: t(214) = 3.49\n    p: 0.00058\n    n: 214 units (215 by the degrees of freedom)\n  depends_on:\n  - units-337\n  expected:\n  - quantity: units well fitted\n    value: 214\n    tolerance: 21\n  - quantity: mean tau, stimulus cumulative information\n    value: 459\n    tolerance: 45.9\n    unit: ms\n  - quantity: mean tau, category cumulative information\n    value: 372\n    tolerance: 37.2\n    unit: ms\n  criterion: Methods F on the 337 units' curves (Methods I). The text says 214 units while the t and\n    F statistics imply 215; both counts are within tolerance. Reproduced when, under one reading of\n    F, the count and both means are within tolerance and a two-sided paired t-test of stimulus\n    against category tau gives p < 0.05 with the stimulus mean higher. Partially reproduced when the\n    test holds and one mean is outside tolerance.\n- id: fig7b-k300\n  statement: The relative cumulative information at 300 ms (k300) ranges from near zero to 0.6, with\n    means of 0.2 for stimuli and 0.15 for categories.\n  source: Results, Rate and time-varying information, Population analysis, paragraph 3; Figure 7B\n  quote: There is also a wide distribution of relative cumulative information values ( k 300 ranging\n    from close to zero to 0.6). On average across neurons, the k 300 was 0.2 (or 20%) for stimuli and\n    0.15 (or 15%) for categories.\n  depends_on:\n  - fig7a-time-constants\n  expected:\n  - quantity: mean k300, stimuli\n    value: 0.2\n    tolerance: 0.02\n  - quantity: mean k300, categories\n    value: 0.15\n    tolerance: 0.015\n  - quantity: largest k300\n    value: 0.6\n    tolerance: 0.06\n  criterion: Methods F on the well-fitted units. The paper calls the difference highly significant\n    but reports no test and says a direct comparison is not warranted, so no test is part of the\n    claim. Reproduced when the three values are within tolerance under one reading of F.\n- id: k300-rate-regression\n  statement: k300 rises with the unit's average firing rate, by 1% per spike/s for stimuli (adjusted\n    R2 0.36) and 0.8% per spike/s for categories (adjusted R2 0.34).\n  source: Results, Rate and time-varying information, Population analysis, paragraph 3\n  quote: For cumulative stimulus information, one finds an increase in k 300 of 1% per spike/s (Adj R\n    2 = 0.36, F(1,213) = 120, p = 1.82 10 −22 ) and, for cumulative categorical information, an\n    increase in k 300 of 0.8% per spike/s (Adj R 2 = 0.34, F(1,213) = 112, p = 2.26 10 −21 )\n  statistics:\n  - about: k300 for stimuli on average firing rate\n    test: linear regression\n    statistic: F(1,213) = 120\n    p: 1.82e-22\n  - about: k300 for categories on average firing rate\n    test: linear regression\n    statistic: F(1,213) = 112\n    p: 2.26e-21\n  depends_on:\n  - fig7a-time-constants\n  expected:\n  - quantity: slope, stimulus k300 on rate\n    value: 0.01\n    tolerance: 0.001\n    unit: per spike/s\n  - quantity: adjusted R2, stimulus\n    value: 0.36\n    tolerance: 0.036\n  - quantity: slope, category k300 on rate\n    value: 0.008\n    tolerance: 0.0008\n    unit: per spike/s\n  - quantity: adjusted R2, category\n    value: 0.34\n    tolerance: 0.034\n  criterion: Ordinary least squares of k300 on the unit's average firing rate over the well-fitted\n    units. Open, the average firing rate; readings (a) the mean KDE rate over all stimuli and 0 to\n    600 ms, (b) the mean spike count rate over all trials and 0 to 600 ms, (c) as (a) over 0 to 300 ms.\n    Reproduced when both slopes are positive with p < 0.05 and the slopes and adjusted R2 are within\n    tolerance under one reading; partially when the regressions hold but a value is outside\n    tolerance.\n- id: fig9a-mean-cii\n  statement: The population average CII is close to the shared value of 1, and slightly but\n    significantly above 1 between 120 and 260 ms.\n  source: Results, Analysis of the categorical information, paragraph 2; Figure 9A\n  quote: The average CII over neurons (bold black line) is very close to the shared value of 1 ... the\n    average CII is also slightly (and significantly) above 1 between 120 and 260 ms\n  depends_on:\n  - units-337\n  expected:\n  - quantity: start of the span with mean CII above 1\n    value: 120\n    tolerance: 12\n    unit: ms\n  - quantity: end of the span with mean CII above 1\n    value: 260\n    tolerance: 26\n    unit: ms\n  criterion: Methods C and P on the 337 units. The test is not named; the figure shows 2 SEM error\n    bars. Readings (a) bins where the mean minus 2 SEM exceeds 1, (b) bins where a two-sided\n    one-sample t-test against 1 gives p < 0.05. Reproduced when, under one reading, the significant\n    bins form one span whose ends are within tolerance and the mean CII over 50 to 600 ms is within\n    0.9 to 1.1 (a fixed reading of \"very close\"). Partially reproduced when a significant span above 1\n    exists inside 100 to 300 ms but its ends are outside tolerance.\n- id: fig9a-top-quartile\n  statement: The CII distribution at 150 ms is skewed toward values above 1, and the quarter of units\n    with the highest CII reach their maximum CII at 175 ms.\n  source: Results, Analysis of the categorical information, paragraph 2; Figure 9A\n  quote: this distribution is positively skewed towards values higher than 1 as exemplified by the\n    density plots calculated at 150ms. ... Focusing on these 25% of neurons with the highest CII, we\n    found a maximum value of CII at 175 ms\n  depends_on:\n  - units-337\n  expected:\n    quantity: time of the top quartile's maximum mean CII\n    value: 175\n    tolerance: 17.5\n    unit: ms\n  criterion: Methods C and P. The top quartile is the 25% of units with the highest time-averaged\n    CII (50 to 300 ms; Fig 9A legend). Bins end at multiples of 10 ms; 175 ms is read as the bin\n    [170,180), within tolerance. Reproduced when the skewness of the CII over units at 150 ms is\n    positive and the top quartile's mean CII peaks within tolerance.\n- id: s7-invariant-information\n  statement: In absolute terms, the top quartile of units by CII reaches a maximum of 0.16 bits of\n    categorical cumulative information above the shared value, at 320 ms.\n  source: Results, Analysis of the categorical information, paragraph 2; S7 Fig\n  quote: these same neurons reach a maximum of 0.16 bits at 320 ms ( S7 Fig )\n  depends_on:\n  - fig9a-top-quartile\n  expected:\n  - quantity: maximum of the mean of CCI minus CCI_Exp, top quartile\n    value: 0.16\n    tolerance: 0.016\n    unit: bits\n  - quantity: time of that maximum\n    value: 320\n    tolerance: 32\n    unit: ms\n  criterion: Methods C and P; the quantity is CCI - CCI_Exp per unit and bin, averaged over the top\n    quartile of fig9a-top-quartile. Reproduced when both values are within tolerance.\n- id: fig9b-cii-tau-ratio\n  statement: Units with high CII have long stimulus time constants relative to their categorical time\n    constants; across the population CII is explained by tau_cat/tau_stim (adjusted R2 0.11).\n  source: Results, Analysis of the categorical information, paragraph 3; Figure 9B\n  quote: neurons with high CII have relatively long stimulus time constants in comparison to their\n    corresponding time constant observed for categorical information. This relationship is also\n    significant for the entire population of neurons (Linear Regression explaining CII from τ cat / τ\n    stim : Adj R 2 = 0.11, F(1,213) = 28.5, p = 2.37 10 −7 )\n  statistics:\n  - test: linear regression\n    statistic: F(1,213) = 28.5\n    p: 2.37e-7\n  depends_on:\n  - fig7a-time-constants\n  expected:\n    quantity: adjusted R2\n    value: 0.11\n    tolerance: 0.011\n  criterion: Ordinary least squares of the time-averaged CII (50 to 300 ms, Methods C) on tau_cat\n    over tau_stim (Methods F), over the well-fitted units. Reproduced when the slope is negative with\n    p < 0.05 and the adjusted R2 is within tolerance under one reading; partially when the slope is\n    negative and significant but R2 is outside tolerance.\n- id: fig9c-cii-k300\n  statement: CII is strongly explained by the difference k300,cat - k300,stim (adjusted R2 0.76),\n    an expected consequence of its definition, and units with high CII have low stimulus k300\n    (adjusted R2 0.28).\n  source: Results, Analysis of the categorical information, paragraph 3; Figure 9C\n  quote: (Linear Regression explaining CII from k 300,cat —k 300,stim : Adj R 2 = 0.76, F(1,213) =\n    675, p = 5.5 10 −68 ). Finally, one can also notice that neurons with high CII have low values of\n    relative stimulus cumulative information (Linear Regression explaining CII from k stim (300): Adj\n    R 2 = 0.28, F(1,213) = 84, p = 3.96 10 −17 )\n  statistics:\n  - about: CII on k300,cat - k300,stim\n    test: linear regression\n    statistic: F(1,213) = 675\n    p: 5.5e-68\n  - about: CII on k300,stim\n    test: linear regression\n    statistic: F(1,213) = 84\n    p: 3.96e-17\n  depends_on:\n  - fig7a-time-constants\n  expected:\n  - quantity: adjusted R2, CII on k300 difference\n    value: 0.76\n    tolerance: 0.076\n  - quantity: adjusted R2, CII on stimulus k300\n    value: 0.28\n    tolerance: 0.028\n  criterion: Ordinary least squares of the time-averaged CII on each predictor over the well-fitted\n    units. Reproduced when the first slope is positive and the second negative, both with p < 0.05,\n    and both adjusted R2 are within tolerance; partially when the signs and significance hold and an\n    R2 is outside tolerance.\n- id: table1-anatomy-counts\n  statement: 303 of the 337 units have an anatomical location, in five birds, 109 in NCM, 29 in CMM,\n    20 in CLM, 46 in L2, 87 in L1/L3 and 12 unclassified.\n  source: Methods, Neurophysiological and histological procedures, paragraph 2; Table 1\n  quote: Table 1 shows the number of units from each bird for which we had an anatomical location and\n    that had significant stimulus cumulative information (303/337 neurons; see below).\n  depends_on:\n  - units-337\n  expected:\n  - quantity: units with anatomical location\n    value: 303\n    tolerance: 30\n  - quantity: NCM\n    value: 109\n    tolerance: 10.9\n  - quantity: CMM\n    value: 29\n    tolerance: 2.9\n  - quantity: CLM\n    value: 20\n    tolerance: 2\n  - quantity: L2\n    value: 46\n    tolerance: 4.6\n  - quantity: L1/L3\n    value: 87\n    tolerance: 8.7\n  - quantity: unclassified\n    value: 12\n    tolerance: 1.2\n  criterion: From the anatomical labels of the units of units-337, if the data set holds them.\n    Reproduced when the total and the six area counts are within tolerance; partially when the total\n    is and some area counts are not. The per-bird counts of Table 1 are compared and reported.\n- id: fig10-cii-distance\n  statement: CII is slightly higher farther from the L2 axis, rostrally or caudally, toward higher\n    auditory areas (adjusted R2 0.036).\n  source: Results, Anatomical organization, paragraph 2; Figure 10B\n  quote: Using the L2 dorsal-ventral oblique axis as reference point, CII was slightly higher as one\n    moved rostrally or caudally to higher regions of auditory processing (Linear regression: Adj R 2\n    = 0.036, F(2,195) = 8.39, p = 0.0042)\n  statistics:\n  - test: linear regression\n    statistic: F(2,195) = 8.39\n    p: 0.0042\n  depends_on:\n  - table1-anatomy-counts\n  - fig7a-time-constants\n  expected:\n    quantity: adjusted R2\n    value: 0.036\n    tolerance: 0.0036\n  criterion: Ordinary least squares of the time-averaged CII on the distance from the L2 axis\n    (Methods A). Open, the units; readings (a) the units with a location among the well-fitted units\n    (about 197, matching the degrees of freedom), (b) all 303 units with a location. Reproduced when\n    the slope is positive with p < 0.05 under one reading of A and of the units; partially when the\n    slope is positive and significant and R2 is outside tolerance. The p-value as printed is reported\n    beside the p of the regression run.\n- id: fig10-cii-area-anova\n  statement: An ANOVA across areas suggests that NCM and L2 have slightly higher mean CII (adjusted R2\n    0.027).\n  source: Results, Anatomical organization, paragraph 2\n  quote: an ANOVA also suggested that both regions NCM and L2 had slightly higher mean CII (Adj R 2 =\n    0.027, F(4,185) = 2.77, p = 0.042)\n  statistics:\n  - test: ANOVA\n    statistic: F(4,185) = 2.77\n    p: 0.042\n  depends_on:\n  - table1-anatomy-counts\n  criterion: One-way ANOVA of the time-averaged CII on area, five groups (NCM, CMM, CLM, L2, L1/L3;\n    unclassified units left out, as the degrees of freedom imply). Open, the units (190 by the degrees\n    of freedom); readings (a) the well-fitted units with an area, (b) all classified units with a\n    location. Reproduced when the area effect has p < 0.05 and NCM and L2 have the two highest group\n    means under one reading; partially when the effect holds and only one of them is among the two\n    highest.\n- id: fig10-tau-k300-distance\n  statement: Farther from the L2 axis the time constant of the stimulus cumulative information is\n    longer (adjusted R2 0.04) and the stimulus k300 smaller (adjusted R2 0.035), with very small\n    effects.\n  source: Results, Anatomical organization, paragraph 2; Figure 10B\n  quote: We also observed an increase in the time constant ( τ ) for the stimulus cumulative\n    information that parallel the increase in CII as one moved away from the L2 axis (Linear\n    regression: Ajd R 2 = 0.04, F(2,195) = 9.32, p = 0.00258). The saturation constant at 300 ms (κ\n    300 ) for stimulus information was also higher in the central auditory region and smaller as one\n    moved away from the L2 axis (Linear Regression: Ajd R 2 = 0.035, F(2,195) = 8.18, p = 0.0047).\n  statistics:\n  - about: stimulus tau on distance from the L2 axis\n    test: linear regression\n    statistic: F(2,195) = 9.32\n    p: 0.00258\n  - about: stimulus k300 on distance from the L2 axis\n    test: linear regression\n    statistic: F(2,195) = 8.18\n    p: 0.0047\n  depends_on:\n  - table1-anatomy-counts\n  - fig7a-time-constants\n  expected:\n  - quantity: adjusted R2, tau\n    value: 0.04\n    tolerance: 0.004\n  - quantity: adjusted R2, k300\n    value: 0.035\n    tolerance: 0.0035\n  criterion: Ordinary least squares of stimulus tau and of stimulus k300 on the distance from the L2\n    axis (Methods A), over the well-fitted units with a location. Reproduced when the tau slope is\n    positive and the k300 slope negative, both with p < 0.05, under one reading of A; partially when\n    one of the two holds. R2 values are compared with their tolerances and reported.\n- id: fig10-no-anatomy-categorical\n  statement: Anatomy has no effect on the time constant or the k300 of the categorical cumulative\n    information.\n  source: Results, Anatomical organization, paragraph 2\n  quote: We did not find, however, any effects of anatomy on the time constant, ( τ ), or saturation\n    constants (κ 300 ) for the cumulative categorical information\n  depends_on:\n  - table1-anatomy-counts\n  - fig7a-time-constants\n  criterion: A claim of absence. The paper's test for the stimulus measures is the linear regression\n    on the distance from the L2 axis; the same regressions of category tau and category k300, over\n    the well-fitted units with a location, at p < 0.05. Reproduced when neither is significant under\n    the reading of A used for fig10-tau-k300-distance; not reproduced when one is. The slopes and R2\n    are reported either way, and the area ANOVA of fig10-cii-area-anova is shown as a variant.\n- id: cii-unimodal\n  statement: The distribution of the categorical information index across units is unimodal, with no\n    separate population of invariant units.\n  source: Discussion, paragraph 7\n  quote: we did not find a separate population of invariant neurons across all of our recordings of\n    neurons informative for categories: the distribution of our categorical index was unimodal\n  depends_on:\n  - units-337\n  criterion: The paper names no test and shows the distribution at 150 ms (Fig 9A, right panel).\n    Readings of the distribution, (a) the CII at 150 ms, (b) the time-averaged CII (50 to 300 ms).\n    Hartigan's dip test at p < 0.05 is fixed here as the test, the paper naming none. A claim of\n    absence of a second mode; reproduced when the dip test does not reject unimodality under either\n    reading, not reproduced when it does.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import re
p='claims/elie-2019.yaml'
s=open(p).read()
rep={
"""  quote: we did not find a separate population of invariant neurons across all of our recordings of
    neurons informative for categories: the distribution of our categorical index was unimodal""":
"""  quote: the distribution of our categorical index was unimodal""",
"""moved rostrally or caudally to higher regions of auditory processing (Linear regression: Adj R 2
    = 0.036, F(2,195) = 8.39, p = 0.0042)""":
"""moved rostrally or caudally to higher regions of auditory processing ... Adj R 2 = 0.036, F(2,195)
    = 8.39, p = 0.0042""",
"""  quote: neurons with high CII have relatively long stimulus time constants in comparison to their
    corresponding time constant observed for categorical information. This relationship is also
    significant for the entire population of neurons (Linear Regression explaining CII from τ cat / τ
    stim : Adj R 2 = 0.11, F(1,213) = 28.5, p = 2.37 10 −7 )""":
"""  quote: neurons with high CII have relatively long stimulus time constants in comparison to their
    corresponding time constant observed for categorical information. This relationship is also
    significant for the entire population of neurons ... Adj R 2 = 0.11, F(1,213) = 28.5, p = 2.37 10
    −7""",
"""  quote: (Linear Regression explaining CII from k 300,cat —k 300,stim : Adj R 2 = 0.76, F(1,213) =
    675, p = 5.5 10 −68 ). Finally, one can also notice that neurons with high CII have low values of
    relative stimulus cumulative information (Linear Regression explaining CII from k stim (300): Adj
    R 2 = 0.28, F(1,213) = 84, p = 3.96 10 −17 )""":
"""  quote: neurons with high CII also have higher relative levels of categorical information in
    comparison to their relative values for stimulus information although this result is expected
    given our definition of CII ... Adj R 2 = 0.76, F(1,213) = 675, p = 5.5 10 −68 ). Finally, one
    can also notice that neurons with high CII have low values of relative stimulus cumulative
    information ... Adj R 2 = 0.28, F(1,213) = 84, p = 3.96 10 −17""",
"""information that parallel the increase in CII as one moved away from the L2 axis (Linear
    regression: Ajd R 2 = 0.04, F(2,195) = 9.32, p = 0.00258). The saturation constant at 300 ms (κ
    300 ) for stimulus information was also higher in the central auditory region and smaller as one
    moved away from the L2 axis (Linear Regression: Ajd R 2 = 0.035, F(2,195) = 8.18, p = 0.0047).""":
"""information that parallel the increase in CII as one moved away from the L2 axis ... Ajd R 2 =
    0.04, F(2,195) = 9.32, p = 0.00258). The saturation constant at 300 ms (κ 300 ) for stimulus
    information was also higher in the central auditory region and smaller as one moved away from the
    L2 axis ... Ajd R 2 = 0.035, F(2,195) = 8.18, p = 0.0047""",
}
for a,b in rep.items():
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n ": .*: \|—\|rather" claims/elie-2019.yaml | grep -v "^[0-9]*:#" ; python tools/claims_check.py claims/elie-2019.yaml paper/10.1371-journal.pcbi.1006698.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "10 \|e-\|exponent\|sci" tools/claims_check.py | head -30
```

```
7:confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
28:INLINE = (r"</?(italic|bold|sup|sub|sc|underline|xref|ext-link|named-content|inline-formula|mml:[a-z]+"
64:    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
```

**Agent calls Bash**

```bash
cd  sed -n 60,110p tools/claims_check.py
```

```
return False


def printed_forms(v: float) -> set[str]:
    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
    out = {f"{v:g}", f"{v:g}".lstrip("0") if abs(v) < 1 else f"{v:g}"}
    if 0 < abs(v) < 1:
        m, e = f"{v:.3e}".split("e")
        m, e = f"{float(m):g}", str(int(e))
        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
        if m == "1":
            out.add(f"10{e}")
    if 0 < abs(v) < 0.001:
        plain = f"{v:.12f}".rstrip("0")
        out |= {plain, plain.lstrip("0")}
    return {f.lower() for f in out}


def check(claims_path: Path, paper_paths: list[Path]) -> int:
    doc = yaml.safe_load(claims_path.read_text())
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "—" claims/elie-2019.yaml; grep -ci "rather" claims/elie-2019.yaml; grep -n "[^#].*[a-z)]: " claims/elie-2019.yaml | grep -v "^\S*\s*[a-z_]*: \|^[0-9]*:#\|^[0-9]*:  *[a-z_]*: \|^[0-9]*:- [a-z_]*: \|^[0-9]*:  - [a-z_]*: " | head; git status --short
```

```
0
0
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
?? claims/elie-2019.yaml
?? scripts
```

**Agent**

I wrote `claims/elie-2019.yaml`, uncommitted as asked. It has 25 claims, every one with a quote. The checker passes the schema and all 25 quotes. It flags one p-value, `fig9b-cii-tau-ratio` 2.37e-7, which the paper prints as "p = 2.37 10 −7" (Results, Analysis of the categorical information, paragraph 3); the checker does not recognise that format. I confirmed the value by reading and left the checker alone, but its exit code is still non-zero.

**Text read.** The version of record, PMC6762074 (open access), from the publisher's XML: main text, Methods, Table 1, and the legends of Figs 1 to 10 and S1 to S7. The supplement is only those seven figures. No PDF was supplied. The data description was read only to see what the dataset holds.

**Code read.** github.com/julieelie/PoissonTimeVaryingInfo at commit 97802032 (2019-04-01). It settles:
- which nine call types are used;
- the 10 ms bins and the Monte Carlo settings;
- how categories are weighted;
- the random-category floor (one shuffle of the call-type labels per unit);
- the fixed-rate control.

It does not contain the rate estimate (KDE) itself, the coherence function, the multiple-comparison (FDR) step, the selection of the 404 and 337 units, the exponential fits, the expected categorical information or the categorical index (CII), or any population or anatomical statistics.

**Content.**
- **Claims:** 25 findings and no link claims. One, the model neurons of Fig 1, is a simulation (`data: elsewhere`, using the tutorial file in the code repository). One, the 404-unit selection, needs outside information (`with_inputs`).
- **Statistics:** 10 tests recorded, across 8 claims.
- **Criteria:** every claim has one, and 22 have expected values.

**Open details and the readings named:**
- **Rates:** used as estimated, or low-pass filtered at 50 Hz first.
- **Exponential fit:** the equation is lost from the text. The reading given is I(t) = k·I_Max·(1 − exp(−(t−dt)/τ)). "Well fitted" is not defined; readings are (a) fits converge with parameters in range, or (b) the 214 lowest-error fits.
- **CII:** the formula is lost. The reading given is a piecewise linear map through 0 (floor), 1 (expected) and 2 (ceiling).
- **Population averages for units whose cumulative curve ends early:** leave them out from that point, or carry the last value forward.
- **Poisson test:** the Methods say two-tailed; the code is one-tailed and has no FDR step. The Methods are followed and the code is a variant. Cut-offs read as "at most 10% / at least 40%" or "under 10% / over 40%".
- **Fano factor:**
  - Stimuli with no spikes in a bin are set to 1 (as the code does) or left out.
  - No test is named; readings are a t-test or a Wilcoxon test against 1.
- **Stimulus correlation:** computed across stimuli at each pair of bins, or across bins within each stimulus.
- **Fixed-rate fraction:** a ratio of population means, or the mean of each unit's ratio.
- **Average firing rate in the k300 regression:** KDE rate over 0 to 600 ms, spike-count rate over 0 to 600 ms, or KDE rate over 0 to 300 ms.
- **Significance of the mean CII:** the 2-SEM band, or a t-test in each bin.
- **Distance to the L2 axis:** perpendicular distance, or rostro-caudal distance. Which units enter the regressions and the ANOVA is also open.
- **Degrees of freedom:** the text gives 214 units but t(214) and F(1,213) imply 215. The printed F(2,195) values match their p-values only as F(1,195).
- **Thresholds I fixed myself:** for "small", "almost constant", "relatively constant" and "unimodal" (Hartigan's dip test), the paper gives no rule, so each criterion says the threshold is my choice.
- **Example neurons (Figs 3 to 5):** the paper does not identify these units in the data. The claim is blocked unless the rasters in S4 to S6 Fig identify them.

**Missing from what was supplied:**
- **Equations:** all the displayed equations were lost in extraction, and no PDF was supplied. Those that matter are the exponential model, the CII formula, the coherence formula and the bias correction. The author can read them in the published article.
- **404-unit selection:** this rests on the decoding analysis of Elie & Theunissen 2015 (Eur J Neurosci 41:546), which this paper does not describe.
- **Anatomy:** the anatomical claims need area labels and coordinates for each unit. The data description does not mention them.

## End of run

28 turns, 6 minutes, $2.47 at API prices, result: success.
