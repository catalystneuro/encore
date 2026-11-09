# crcns-apl-1 · claims · run 42476827269

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/001453/ claims/crcns-apl-1/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,185p docs/protocol.md; cat claims/001453/*.yaml
```

```
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

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
[... 486 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; cat paper/10.7554-elife.27342.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.27342.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.27342.txt",
 "offset": 129,
 "limit": 130
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.27342.txt",
 "offset": 259,
 "limit": 160
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  head -c 4000 paper/apl-1.data-description.txt; echo; cd $TMPDIR && git clone -q https://github.com/mdhumphries/AplysiaAttractorAnalysis.git && cd AplysiaAttractorAnalysis && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis; cat README.md; wc -l Analysis/*.m Analysis/*/*.m Functions/convolve_spiketrains.m Functions/WeightedCorrelation.m Functions/iterateoutliers.m; cat Analysis/DataSet_Properties.m Analysis/Classify_attractors/Dimensionality_of_Projections.m
```

```
Aplysia Attractor Analysis
============================

Suite of MATLAB code for the eLife paper
"A spiral attractor drives rhythmic locomotion"
Angela Bruno, Bill Frost & Mark Humphries

Angela M Bruno, William N Frost & Mark D Humphries (2017) A spiral attractor network drives rhythmic locomotion. eLife, 6:e27342. 
https://elifesciences.org/articles/27342

All experimental data is available at the CRCNS repository: https://crcns.org/data-sets/aplysia/apl-1/about-apl-1

---
### Summary

We provide here all the code we used:

Figures/

All code to produce all panels of main text and supplemental figures
[... 502 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis/Analysis/Classify_attractors; cat Analyse_by_Recurrence_Points.m LocalLinearDynamics.m
```

```
<persisted-output>
Output too large (33.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9ec795df-db2a-406a-8193-73ed83546f9c/tool-results/bqdirlxqn.txt

Preview (first 2KB):
% script to classify projections
% does periodic orbit recurrence ~ Lathrop & Kostelich (1989)
% ADD osc and burst to this: 
% 
% NB: for a given point in PC projection, computes its recurrence time for
% a given threshold; first discards all time-points less then threshold
% that are contiguous in future time with the given point - i.e. removes
% the local tangent
% 
% pars.X
%   struct of analysis parameters:
%         stimstart: time of stimulation onset (s)
%                T0: initial time of recurrence checking (s)
%         maxWindow: time before end of time-series to stop checking for recurrence (s)
%      VarExplained: target proportion of variance explained by chosen set of PC dimensions
%         prctTheta: vector (Nx1): percentages of recurrence distance
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/9ec795df-db2a-406a-8193-73ed83546f9c/tool-results/bqdirlxqn.txt"
}
```

```
1	% script to classify projections
2	% does periodic orbit recurrence ~ Lathrop & Kostelich (1989)
3	% ADD osc and burst to this: 
4	% 
5	% NB: for a given point in PC projection, computes its recurrence time for
6	% a given threshold; first discards all time-points less then threshold
7	% that are contiguous in future time with the given point - i.e. removes
8	% the local tangent
9	% 
10	% pars.X
11	%   struct of analysis parameters:
12	%         stimstart: time of stimulation onset (s)
13	%                T0: initial time of recurrence checking (s)
14	%         maxWindow: time before end of time-series to stop checking for recurrence (s)
15	%      VarExplained: target proportion of variance explained by chosen set of PC dimensions
16	%         prctTheta: vector (Nx1): percentages of recurrence distance
17	%                           distribution to use as recurrence threshold
18	%             bstep: step-size for recurrence point histogram (s)
19	%              bins: vector of bins for recurrence point histogram (s)
20	%              tmin: smallest recurrence time to count as a histogram peak (s)
[... 618 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis; grep -v '^\s*%' Analysis/Classify_attractors/recurrence_point_results_Viz.m | grep -v '^\s*$' | head -300
```

```
clear all; close all
addpath ../../Functions/
statpars.ixT = 3; % threshold of 10%
statpars.pDensity = 90; % min point density to count as "coalescence time"
statpars.Tperturb = 50; % falling below threshold of point density indicates non-recurrent period
load da01_RecurrencePointsData_FilterPts RcrPtData
fname_Pre = '';
fnames = {'da01','da02','da03'};
nfiles = numel(RcrPtData);
PerColor = [0.4 0.4 0.4]; % dominant period
AllColor = [1 0 0];  % all recurrence points 
NoPerColor = [0.6 0.6 0.9];  % no period at all, but recurrent
for iR = 1:nfiles
   for iF = 1:numel(fnames) 
       load([fname_Pre fnames{iF} '_RecurrencePointsData_FilterPts'],'RcrPtData','pars');
       load(['../' fname_Pre  fnames{iF} '_DataProperties_FunctionAndWindowSize'],'Data','FileTable')
       nPoints = [RcrPtData(iR).Orbit(statpars.ixT).Period(:).nPoints];
       ixPrd = find(nPoints == max(nPoints));  
       usedPts = RcrPtData(iR).Orbit(statpars.ixT).Period(ixPrd).Npts >= pars.minNeighbours;
       RcrStats(iR,iF).nUsedPts = numel(usedPts); % points used to compute each mean etc!
[... 214 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis; for f in Figures/Figure_LinearDynamics.m Analysis/Classify_attractors/Does_Oscillation_Period_Change.m Functions/WeightedCorrelation.m; do echo "=== $f"; grep -v '^\s*%' $f | grep -v '^\s*$' | grep -v -i 'set(gca\|xlabel\|ylabel\|exportPPT\|figure\b\|FontSize\|axis\|text(' ; done | head -400
```

```
=== Figures/Figure_LinearDynamics.m
clear all; close all
if ismac
    filepath = '[removed: a home directory path]/Dropbox/Analyses/My modularity based methods/Collaborations using my methods/AB - Aplysia motor program dynamics/';
    spikepath = '[removed: a home directory path]/Dropbox/paper2/datasets/deconcatenated_spks/experimental/';
else
    filepath = 'C:\Users\mqbssmhg.DS\Dropbox\Analyses\My modularity based methods\Collaborations using my methods\AB - Aplysia motor program dynamics\';
    spikepath = 'C:\Users\mqbssmhg.DS\Dropbox\paper2\datasets\deconcatenated_spks\experimental\';
end
run figure_properties
M = 4; % need bigger markers here 
ixExample = 5; % prep #5, stims 2 and 3
ixT = 3;  % which threshold? s
load([filepath '/Classify attractors/RecurrenceStats_FilterPts'])
npreps = size(RcrStats,1);
nstims = size(RcrStats,2);
ixExample = 9;
load([filepath 'da03_DataProperties_FunctionAndWindowSize'],'Data')
load([filepath '/Classify attractors/da03_RecurrencePointsData_FilterPts'])
nPoints = [RcrPtData(ixExample).Orbit(statpars.ixT).Period(:).nPoints];
[... 287 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis/Analysis/Classify_attractors; for f in Are_sequential_attractors_the_same.m Initial_Conditions.m; do echo "=== $f"; grep -v '^\s*%' $f | grep -v '^\s*$' | grep -v -i 'set(gca\|xlabel\|ylabel\|exportPPT\|^\s*figure\|FontSize\|^\s*axis\|text(\|title(\|plot(\|line(' ; done | head -400
```

```
=== Are_sequential_attractors_the_same.m
clear all; close all
addpath ../../Functions/
spars.stimstart = 30;  % stimulation time
spars.VmaxD = 3;  % number of dimensions to visualise
spars.minDens = 0; % min proportion of recurrence points with period
spars.ixT = 3; % which threshold to use
spars.minRecur = 90; % minimum percentage of recurrence points per time-window
spars.manifoldT = 5; % distance to be on same manifold
spars.divPeriod = 0;  % radius on checking min distance as division of oscillation period (0 = no radius; 1 = period; 2 = half period etc)
spars.nShuffles = 100;  % 100!
fname_Pre = '';
load ../da01_DataProperties_FunctionAndWindowSize FileTable
nfiles = numel(FileTable);
load RecurrenceStats RcrStats
fnames = {'da01','da02','da03'};
ixExample = 1;
feature('numCores');
if isempty(gcp('nocreate'))
    parpool('local',10);
[... 317 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis/Analysis; for f in Classify_attractors/Are_jumps_perturbations_or_transitions2.m Classify_attractors/Quantifying_Participation_by_PCA_Contribution.m Classify_attractors/RobustnessOfAttractor_to_single_neuron_variability.m ../Functions/iterateoutliers.m; do echo "=== $f"; grep -v '^\s*%' $f | grep -v '^\s*$' | grep -v -i 'set(gca\|xlabel\|ylabel\|exportPPT\|^\s*figure\|FontSize\|^\s*axis\|text(\|title(\|plot(\|line(\|print -' ; done | head -400
```

```
=== Classify_attractors/Are_jumps_perturbations_or_transitions2.m
clear all; close all
fname_Pre = '';
fnames = {'da01','da02','da03'};
load([fname_Pre 'RecurrenceStats_FilterPts'])  % use recurrence point statistics based on using more robust model fits - min 1s and contiguous points
npreps = size(RcrStats,1);
jumppars.theta = 0.2;  % threshold for a different attractor
jumppars.cycles = 2;  % how many cycles before end...
ctr = 1;
Summary.allJumps = 0;
Summary.JumpList = [];  % list of all jumps (Prep,Program,Jump Number)
Summary.blnReturned = []; % returned to attractor?
Summary.blnSame = [];   % same or different attractor?
Summary.pAfter = [];
Summary.pAfterEnd = [];
PropPeriodLocal = zeros(npreps,numel(fnames));
PropPeriodHist = zeros(npreps,numel(fnames));
for iPrep = 1:npreps
    iPrep
   for iProg = 1:numel(fnames)
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis/Analysis; grep -n "pars\.\w* *=\|glmfit\|median(abs\|corr(\|VarExplained\|nPCs *=" P10_analysis/DecodeP10_statespace.m P10_analysis/Best_P10_StateSpace_GLMmodels.m Classify_attractors/Are_sequential_attractors_the_same_CommonAxes.m | head -60; grep -n "Cxy\|corr\|SDF\|Gauss" Ensembles/StaticEnsembles.m | head -30
```

```
P10_analysis/DecodeP10_statespace.m:17:pars.VarIx = 3;  % 2= 80%, 3 = 90%
P10_analysis/DecodeP10_statespace.m:18:pars.Stim = str2double(fname(end)); % column index
P10_analysis/DecodeP10_statespace.m:21:pars.stimstart = 30;
P10_analysis/DecodeP10_statespace.m:22:pars.endwin = 123;  % allow for overrun of recording
P10_analysis/DecodeP10_statespace.m:23:pars.strtMatch = 33;
P10_analysis/DecodeP10_statespace.m:27:pars.Hstep = 100; % number of bins of spike history per second
P10_analysis/DecodeP10_statespace.m:28:pars.Hmax = 0.05:0.05:0.25;   % length of history (in s) 
P10_analysis/DecodeP10_statespace.m:29:% pars.Hstep = 5; % number of bins of spike history per second
P10_analysis/DecodeP10_statespace.m:30:% pars.Hmax = 1:1:4;   % length of history (in s) 
P10_analysis/DecodeP10_statespace.m:32:pars.Wstep = 20;  % number of bins to advance the forecasting window (1=10ms)
P10_analysis/DecodeP10_statespace.m:37:pars.prctTrain = 0.5;  % min. proportion of time-series on which to train model
P10_analysis/DecodeP10_statespace.m:38:pars.kstep = 1:1:10; % forecast this many seconds ahead
P10_analysis/DecodeP10_statespace.m:133:%             [thetaF,dev,stats] = glmfit(Xflat,P10data(iF).spkfcn(Nt),'poisson','link','log','constant','off');
P10_analysis/DecodeP10_statespace.m:135:%             [thetaF,dev,stats] = glmfit(Xflat,P10data(iF).spkfcn(Nt),'poisson','link','log','constant','on'); % 'estdisp','on');
P10_analysis/DecodeP10_statespace.m:147:            P10data(iF).Hist(iH).R_train(iN) = corr(P10data(iF).spkfcn(Nt),modelP10F);
P10_analysis/DecodeP10_statespace.m:149:            P10data(iF).Hist(iH).mae_train(iN) = median(abs(P10data(iF).spkfcn(Nt) - modelP10F));
P10_analysis/DecodeP10_statespace.m:172:            P10data(iF).Hist(iH).R_forecast(iN) = corr(P10data(iF).spkfcn(forecastNt),modelP10forecast(numel(Nt)+1:end));
P10_analysis/DecodeP10_statespace.m:173:            P10data(iF).Hist(iH).mae_forecast(iN) = median(abs(P10data(iF).spkfcn(forecastNt) - modelP10forecas
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis/Analysis; sed -n 1,130p P10_analysis/DecodeP10_statespace.m | grep -v '^\s*$'; sed -n 40,80p Ensembles/StaticEnsembles.m
```

```
%%% script to decode P10 from state-space using GLM
clear all; close all
datapath = '../../Data/P10/';
addpath ../../Functions/
fname = 'da03';
prefix = [];
% get PCA projections
load(['../' prefix fname '_DataProperties_FunctionAndWindowSize'],'FileTable','Data')  % filenames and 
% get PCA projections - has every recording in its matrix (10x3)
load(['../Classify attractors/Projects_For_VAF.mat'])
pars.VarIx = 3;  % 2= 80%, 3 = 90%
pars.Stim = str2double(fname(end)); % column index
% analysis parameters
pars.stimstart = 30;
pars.endwin = 123;  % allow for overrun of recording
pars.strtMatch = 33;
Bsize = 0.02;  % binsize in s  (for histogram - not used at present)
pars.Hstep = 100; % number of bins of spike history per second
pars.Hmax = 0.05:0.05:0.25;   % length of history (in s) 
% pars.Hstep = 5; % number of bins of spike history per second
[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis; grep -n "clstrstart *=" -r Analysis; grep -n "Hellinger\|lm_\|disp\|Rsquared\|pValue" Figures/Figure_NeuronvsProgramVariation.m | head; grep -n "prctVar\|nPCs\|80\|hist" Figures/Figure_Recurrence.m | head -20
```

```
Analysis/Ensembles/StaticEnsembles.m:29:clstrstart = stimstart; % + 6; % 7 seconds after stimulation: mean time to recover phase-locking... (cf ComparePLandR)
25:Robust.lm_NormDist_M
43:Robust.lm_ChangePart_M
63:Robust.lm_Pchange_M
102:    PCA(i,1).prctVar = PCAdata(i).prctVar;
104:    PCA(i,2).prctVar = PCAdata(i).prctVar;
106:    PCA(i,3).prctVar = PCAdata(i).prctVar;
111:line([0.75 200],[80 80],'Linewidth',axlinewidth,'Color',[0.8 0.3 0.3])
114:        nPC = numel(PCA(iP,iS).prctVar);
115:        semilogx(1:nPC,100*PCA(iP,iS).prctVar,'.-','Linewidth',0.25,'Color',stim_set(iS,:));
128:%% panel b inset: histogram of number PCs
131:da01_nPCs = [RcrPtData(:).maxD];
134:da02_nPCs = [RcrPtData(:).maxD];
137:da03_nPCs = [RcrPtData(:).maxD];
140:hPCs = hist([da01_nPCs da02_nPCs da03_nPCs],bins);
154:print -depsc Fig2b_histogram
156:%exportPPTfig(gcf,'Fig2s_histogram')
171:set(gca,'XTick',[0 40 80 120],'YTick',[0 40 80 120])
184:%% panel X: theta histogram example: robustness to threshold
186:% all Theta histograms
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; ls schemas 2>/dev/null; grep -rn "kind" docs/*.md | head -10; ls claims | head; ls claims/*/ | head -30
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

[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; ls claims | grep -i crcns | head;
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
[... 195 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"; head -30 claims/crcns-alm-1/*.yaml
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
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis/Figures; grep -n "mTime\|mean(\|median(\|2f\|2F\|Fig2f" Figure_Recurrence.m | head -30; grep -n "mean\|R2\|corr\|rsq\|\^2" ExtendedFig_Participation.m | head -20; grep -n "Ntests\|173\|mean(\|R_forecast\|mae" ../Figures/Figure_OutputDecoding.m | head -20
```

```
232:        allMtime(ctr) =  RcrPtData(iF).Orbit(ixT).Period(ixPrd).mTime;
243:        allMtime(ctr) =  RcrPtData(iF).Orbit(ixT).Period(ixPrd).mTime;
254:        allMtime(ctr) =  RcrPtData(iF).Orbit(ixT).Period(ixPrd).mTime;
315:    % line([0.9 1.1],[mean(D_pre_postN),mean(D_pre_postN)],'Color','k','Linewidth',errorlinewidth)
316:    % line([1 1],[mean(D_pre_postN)-2*std(D_pre_postN)/sqrt(n),mean(D_pre_postN)+2*std(D_pre_postN)/sqrt(n)],'Color','k','Linewidth',errorlinewidth)
27:%% does participation mean just rate?
38:text(0.5,95,sprintf('R^2=%.2g',PartContribution(iPrep).rRatePart(iProg)^2),'Fontsize',fontsize-1)
50:%% histogram of all R^2 for rate vs participation
54:        allR2(iPrep,iProg) = PartContribution(iPrep).rRatePart(iProg)^2;
58:binsR2 = 0:binstep:1;
59:hR2 = hist(allR2(:),binsR2);
61:mAllR2 = mean(allR2(:));
63:bar(binsR2+binstep/2,hR2,1,'FaceColor',[1 1 1],'LineWidth',axlinewidth)
64:line([mAllR2 mAllR2],[0 7],'Color',[0.8 0.3 0.3],'Linewidth',axlinewidth)
68:% xlabel('R^2: participation','FontSize',fontsize)
70:xlabel('R^2: rate','FontSize',fontsize)
72:text(mAllR2+0.02,7.2,sprintf('%.2g',mAllR2),'Color',[0.8 0.3 0.3],'FontSize',fontsize-1);
78:print -depsc ExtFigPart_rateR2Histogram
91:text(1,-25,sprintf('R^2=%.2g',PartContribution(iPrep).rDrateDpart(iChange)^2),'Fontsize',fontsize-1)
102:%% histogram of all R^2 for change in rate vs change in participation
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis/Analysis/Classify_attractors; grep -v '^\s*%' What_is_Participation.m | grep -v '^\s*$'
```

```
clear all; close all
fnames = {'da01','da02','da03'};
fname_Pre = [];
load([fname_Pre 'ParticipationChanges_SamePCs'],'Coeffs');  % load Pariticpation scores
npreps = size(Coeffs,2);
nprogs = numel(fnames);
 for iProg = 1:numel(fnames)
    for iPrep = 1:npreps
        load(['../' fname_Pre fnames{iProg} '_DataProperties_FunctionAndWindowSize'],'Data') % to get density functions and basic data
        PartContribution(iPrep).rates(iProg,:) = Data(iPrep).rates;
        [PartContribution(iPrep).rRatePart(iProg),PartContribution(iPrep).pRatePart(iProg)] = corr(Coeffs(iPrep).normWMax(iProg,:)',PartContribution(iPrep).rates(iProg,:)'); 
    end
 end
 for iPrep = 1:npreps
    PartContribution(iPrep).dRates = [PartContribution(iPrep).rates(1,:)' - PartContribution(iPrep).rates(2,:)' PartContribution(iPrep).rates(1,:)' - PartContribution(iPrep).rates(3,:)' PartContribution(iPrep).rates(2,:)' - PartContribution(iPrep).rates(3,:)'];
    for iChange = 1:numel(fnames)  % for each change, correlate the change in rate and the change in participation (normalised)
         [PartContribution(iPrep).rDrateDpart(iChange),PartContribution(iPrep).pDrateDpart(iChange)] = corr(PartContribution(iPrep).dRates(:,iChange),Coeffs(iPrep).dMaxP(:,iChange));
    end
    PartContribution(iPrep).maxDrates = max(abs(PartContribution(iPrep).dRates(:,1:2)),[],2);
    [PartContribution(iPrep).rDrateDpartMax,PartContribution(iPrep).pDrateDpartMax] = corr(PartContribution(iPrep).maxDrates, Coeffs(iPrep).maxDMaxP);
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis/Analysis; for f in Classify_attractors/Check_All_Real_Eigenvalues.m P10_analysis/P10_ID_motorneurons.m Mapping/ParticipationMapsSummary.m; do echo "=== $f"; grep -v '^\s*%' $f | grep -v '^\s*$' | grep -v -i 'set(gca\|xlabel\|ylabel\|exportPPT\|^\s*figure\|FontSize\|^\s*axis\|text(\|title(\|line(\|print -' ; done | head -250
```

```
=== Classify_attractors/Check_All_Real_Eigenvalues.m
clear all; close all;
addpath ../../Functions/
Eigpars.ixT = 3; % threshold of 10%
Eigpars.Same = 1e-7;
load da01_RecurrencePointsData_FilterPts RcrPtData
fname_Pre = '';
fnames = {'da01','da02','da03'};
nPreps = numel(RcrPtData);
cmap = brewermap(10,'Paired'); 
Msize = [3 9 5];   % for 5HT & washout: pick out the 5HT prep
Msize = [4 4 4];
for iPrep = 1:nPreps
   for iStim = 1:numel(fnames) 
       load([fname_Pre fnames{iStim} '_RecurrencePointsData_FilterPts'],'RcrPtData','pars');
       load(['../' fname_Pre  fnames{iStim} '_DataProperties_FunctionAndWindowSize'],'Data','FileTable')
       nPoints = [RcrPtData(iPrep).Orbit(Eigpars.ixT).Period(:).nPoints];
       ixPrd = find(nPoints == max(nPoints));  
       usedPts = RcrPtData(iPrep).Orbit(Eigpars.ixT).Period(ixPrd).Npts >= pars.minNeighbours;
       AllEigs(iPrep,iStim).nUsedPts = numel(usedPts); % points used to compute each mean etc!
[... 215 more lines not kept]
```

**Agent**

Full text is complete: version of record PMC5546814, with all figure supplements, Methods and code link. I've read the code at commit e5f28e9. Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-apl-1/10.7554-elife.27342.yaml",
 "content": "# Claims for Bruno, Frost & Humphries (2017), eLife 6:e27342, \"A spiral attractor network drives\n# rhythmic locomotion\", doi:10.7554/elife.27342, on CRCNS data set apl-1 (doi:10.6080/K0SN074B).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-08,\n# protocol as stated in docs/protocol.md (Reader), version pilot-13.\n#\n# Text read: the version of record (PMC5546814, open access), as JATS XML flattened to text under\n# paper/: main text, Materials and methods, and the legends of Figures 1 to 8 and of all twelve\n# figure supplements. The paper has no other supplementary file. No PDF of the paper was supplied,\n# and none was needed: no claim rests on a number shown only in a figure. The extraction garbles\n# some formulas: the Gaussian width reads \"σ = {median ISI in population}/12\" (a square root may be\n# lost) and the rotation period reads \"ω = 2πbΔt\"; the code settles the second (see below).\n# The data set's description (paper/apl-1.data-description.txt) was read only to know what it\n# holds; no claim comes from it.\n#\n# Code read: https://github.com/mdhumphries/AplysiaAttractorAnalysis, commit e5f28e98 (2018-07-11),\n# MATLAB, linked from the paper's Data and code availability. Analysis/DataSet_Properties.m builds\n# the spike-density functions and the PCA; Analysis/Classify_attractors/ holds the recurrence\n# analysis (Analyse_by_Recurrence_Points.m, LocalLinearDynamics.m, recurrence_point_results_Viz.m),\n# manifold comparisons (Are_sequential_attractors_the_same.m and _CommonAxes.m,\n# Initial_Conditions.m), perturbations (Are_jumps_perturbations_or_transitions2.m), period change\n# (Does_Oscillation_Period_Change.m, Functions/WeightedCorrelation.m), eigenvalues\n# (Check_All_Real_Eigenvalues.m), participation (Quantifying_Participation_by_PCA_Contribution.m,\n# Functions/iterateoutliers.m, What_is_Participation.m,\n# RobustnessOfAttractor_to_single_neuron_variability.m); Analysis/P10_analysis/ the P10 decoding\n# and motorneuron test; Analysis/Mapping/ the participation maps; Figures/ the figure scripts.\n#\n# Method choices the code settles where the Methods are silent, used in the criteria below:\n# spike-density functions on a 10 ms grid, Gaussian kernel to +/-5 SD with unit area; PCA\n# (princomp, mean-centred) on the spike-density functions from stimulation onset (30 s) to the end\n# of the recording; the recurrence threshold theta is the 10th percentile of all pairwise Euclidean\n# distances among the post-onset points; recurrence is checked from 35 s (5 s after onset) to\n# 10 s before the end; the first contiguous run of points within theta after the checked point is\n# dropped and the earliest later point within theta gives the recurrence time; histogram bins\n# 0:1:50 s, peaks are runs of non-empty bins at 5 s or more holding at least 100 points;\n# sliding windows 5 s, step 1 s; a window's recurrence density counts any recurrent point; local\n# linear models are fitted to the contiguous run of points within 2.5 theta, by least squares of\n# the first difference on the points (no intercept), and only points with at least 100 neighbours\n# are averaged; rotation period = 2*pi / b * 0.01 s and contraction = (exp(100 a) - 1) * 100 %/s\n# (Figures/Figure_LinearDynamics.m), with a and b the real and imaginary parts of the maximum\n# eigenvalue.\n#\n# Places where the code and the Methods differ, each named again in the claims it touches:\n# (1) the Gaussian SD: the Methods give the median ISI divided by 12 (or its square root, if the\n# extraction lost it); the code uses the median ISI itself, and computes it from the post-onset\n# ISIs of all recordings of the same stimulation number read so far, not of the recording alone;\n# (2) the number of PCs: the Methods say at least 80% of variance; the recurrence code keeps the\n# PCs whose cumulative variance is at most 80% (sum(prctVar <= 0.8)), the manifold code the\n# smallest number reaching at least 80%; (3) the dominant period: the Methods and Figure 2F say\n# the mean recurrence time of the dominant peak, the code stores and plots the median;\n# (4) P10 decoding: the Methods fit 40 s windows stepped by 1 s with histories 50 to 200 ms; the\n# code trains on 50% of the post-33 s series, steps 0.2 s, and tries histories 50 to 250 ms;\n# (5) the period-change permutation test: 10000 permutations in the Methods, 100000 in the code,\n# which permutes the pooled time and period values and is one-sided in the direction of rho.\n# Following the protocol, the Methods are the main reading and the code's choice is a variant.\n#\n# Data the paper used. Aplysia californica, isolated cerebral, pleural and pedal ganglia (15 to\n# 17 C). Voltage-sensitive dye RH-155 imaged with a 464-element photodiode array at 1600 Hz over\n# the dorsal pedal ganglion, bandpassed 5 to 100 Hz and spike-sorted by independent component\n# analysis. 10 preparations, three evoked bouts of fictive locomotion each (30 evoked population\n# responses, \"programs\"), each evoked by 8 V, 5 ms pulses at 20 Hz for 2.5 s to pedal nerve 9 at\n# 30 s into a recording of about 125 s (30 s spontaneous, about 95 s evoked); stimulation\n# intervals of 15 and 60 min. The same neurons were tracked across the three bouts of a\n# preparation; the paper gives 120 to 180 neurons per recording and 1131 neurons in all\n# (Figure 7B). Extracellular P10 nerve recordings for all three bouts in 3 preparations (nine\n# responses). Neuron (x, y) positions on the array, reconstructed for 8 preparations (4 left,\n# 4 right ganglia). The data set's description says it holds spike times of the 30 recordings,\n# the P10 channel where recorded, and neuron location maps; so all claims use the data set.\n# The data set's description gives 75 to 160 neurons per preparation, against the paper's 120 to\n# 180 (claim dataset-size).\n#\n# Not made into claims: the three-neuron model of Figure 1—figure supplement 1 (a simulation, no\n# data), and Figure 2—figure supplement 1, which describes the range of dynamics without a finding\n# beyond the claims below.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: apl-1\n  doi: 10.6080/K0SN074B\npaper: doi:10.7554/elife.27342\nclaims:\n- id: dataset-size\n  statement: Three bouts of fictive locomotion were evoked in each of 10 isolated preparations\n    (30 population responses); each recorded population held 120 to 180 neurons, 1131 neurons in\n    all.\n  source: Results, paragraph 1; Figure 7B legend\n  quote: We sequentially evoked three bouts of fictive locomotion in each of 10 isolated central\n    nervous system preparations ... Recorded populations from the pedal ganglion comprised 120–180\n    neurons each\n  expected:\n  - quantity: preparations\n    value: 10\n    tolerance: 0\n  - quantity: evoked population responses\n    value: 30\n    tolerance: 0\n  - quantity: neurons over all preparations (Figure 7B)\n    value: 1131\n    tolerance: 0\n  criterion: Counts of preparations, recordings and spike-sorted neurons, with zero tolerance as\n    they are counts of what was deposited. The range of neurons per recording is reproduced when\n    every recording holds between 108 and 198 neurons (120 to 180 widened by 10% of each bound).\n    Neurons are counted as the distinct units of a recording (as DataSet_Properties.m counts\n    them); the count of units that spike after stimulation onset is shown as a variant.\n- id: fig1d-slow-oscillation\n  statement: After stimulation the spike-train power spectra of the populations are dominated by a\n    slow oscillation at or below 0.1 Hz.\n  source: Results, paragraph 1; Figure 1D\n  quote: A dominant, slow ( ≤ 0.1 Hz) oscillation in neural firing ( Figure 1D ) is consistent with\n    the periodic activity necessary to generate rhythmic locomotion\n  expected:\n    quantity: frequency of the dominant peak of the mean post-stimulation spectrum\n    value: 0.1\n    tolerance: 0.01\n    unit: Hz\n  criterion: As the Methods (Spike-train analysis) and DataSet_Properties.m, a multitaper\n    spectrum (Chronux mtspectrumpt, spike times at 1 ms, averaged over the neurons of a\n    recording, fpass 0 to 1 Hz, default tapers) of each neuron's spikes after stimulation onset;\n    the mean over neurons for each recording, then the mean over the 30 recordings. The peak\n    frequency is the code's, the power-weighted mean frequency of the region more than 2 SD above\n    the spectrum's mean. Reproduced when the peak of the grand mean spectrum, and the peaks of a\n    majority of the 30 recordings, lie above 0 and at or below 0.11 Hz. The frequency of maximum\n    power above 0 Hz is shown as a variant.\n- id: fig1e-decaying-rate\n  statement: The population firing rate decays slowly after the stimulus, decreasing in most\n    evoked responses.\n  source: Results, paragraph 1; Figure 1E (cited as Figure 1F in the text); Results, Heterogenous\n    population activity arises from a common attractor, paragraph 5\n  quote: the slowly decaying population firing rate ( Figure 1F ) post-stimulus ... corresponding to\n    the decreasing population spike rate in most evoked responses ( Figure 1E )\n  criterion: The network firing rate in 1 s bins, as the Figure 1E legend gives. The paper fixes no\n    measure of decay, so two readings, one from the Methods' own test of rate change for\n    ensembles. (a) The Methods' ensemble rule applied to the whole population: spike counts in\n    20 s windows advanced by 5 s from stimulation onset, Pearson R of window time against count,\n    decreasing when R < -0.2. (b) The slope of a least-squares line of the 1 s binned rate on time\n    from stimulation offset (32.5 s) to the end, decreasing when negative. Reproduced when, under a\n    reading, more than half of the 30 responses are decreasing.\n- id: fig2b-dimensions\n  statement: Capturing 80% of the population variance needs 4 to 8 embedding dimensions in the\n    evoked responses, a reduction by more than a factor of 10 from the number of neurons.\n  source: Results, Joint population activity forms a low-dimensional periodic orbit, paragraph 1;\n    Figure 2B and inset\n  quote: Capturing a significant proportion (80%) of the population variance generally required 4–8\n    embedding dimensions ( Figure 2B ), representing a dimension reduction by more than a factor of\n    10 compared to the number of neurons\n  expected:\n  - quantity: smallest number of dimensions for 80% variance\n    value: 4\n    tolerance: 0.4\n  - quantity: largest number of dimensions for 80% variance\n    value: 8\n    tolerance: 0.8\n  criterion: PCA on the covariance of the spike-density functions from stimulation onset to the end\n    (Methods, Recurrence analysis; DataSet_Properties.m). Two details are open. The Gaussian SD\n    (a) median ISI / sqrt(12), (b) median ISI / 12, as printed, (c) the median ISI, as the code;\n    each with the median of the recording's own post-onset ISIs, and for (c) also the code's\n    pooled running median. The count (i) the smallest number of PCs reaching at least 80% (the\n    Methods), (ii) the number whose cumulative variance is at most 80% (the code that makes the\n    Figure 2B inset). Reproduced when, under a reading, at least 27 of the 30 counts lie in 3.6 to\n    8.8 (the paper says \"generally\"; the rule of 27 is fixed here) and the number of neurons\n    divided by the count exceeds 10 in every response.\n- id: fig2ef-periodic-recurrence\n  statement: The evoked low-dimensional activity recurs with a regular period; strongly periodic\n    recurrence on the scale of 10 to 15 s is found in many but not all of the 30 responses.\n  source: Results, Joint population activity forms a low-dimensional periodic orbit, paragraph 3;\n    Figure 2D to 2F\n  quote: We found strongly periodic recurrence on the scale of 10–15 s in many but not all of the 30\n    evoked population responses ( Figure 2E,F )\n  expected:\n  - quantity: lower end of the dominant recurrence period\n    value: 10\n    tolerance: 1\n    unit: s\n  - quantity: upper end of the dominant recurrence period\n    value: 15\n    tolerance: 1.5\n    unit: s\n  criterion: Dominant period per response as the Methods (Recurrence analysis) with the code's\n    settings in the opening comment, theta at the 10th percentile, in the dimensions of claim\n    fig2b-dimensions. The period of the dominant peak is (a) the mean of its recurrence times (the\n    Methods and Figure 2F legend) or (b) their median (the code). Reproduced when, under a\n    reading, more than half of the 30 dominant periods lie in 9 to 16.5 s and at least one does\n    not (\"not all\"). The SD and the readings of claim fig2b-dimensions are carried over; the\n    author reports each.\n  depends_on:\n  - fig2b-dimensions\n- id: fig2e-single-dominant-orbit\n  statement: Almost all populations are dominated by a single periodic orbit; the majority of\n    programs have more than 50% of their recurrent points in the dominant peak.\n  source: Results, Joint population activity forms a low-dimensional periodic orbit, paragraph 3;\n    Materials and methods, Recurrence analysis, paragraph 3; Figure 2E\n  quote: the majority of programs had more than 50% of their recurrent points in this peak\n    (blue-scale vectors in Figure 2E )\n  criterion: Per response, the proportion of recurrent points (delays of 5 s or more, as the\n    histogram counts them, and, as a variant, all recurrent points as propInMaxPeriod in\n    recurrence_point_results_Viz.m) falling in the dominant peak. Reproduced when more than 15 of\n    the 30 responses exceed 50%. The number of peaks per response is reported against the\n    Methods' \"between one and four\".\n  depends_on:\n  - fig2ef-periodic-recurrence\n- id: fig2s2-threshold-robust\n  statement: The periodic orbits are robust to the threshold for recurrence, with similar\n    periodicity at thresholds of 10%, 5% and 2%.\n  source: Figure 2—figure supplement 2; Materials and methods, Recurrence analysis, paragraph 2\n  quote: similar periodicity of recurrence was maintained at all tested thresholds from 2% upwards\n  criterion: Dominant periods per response at theta of the 2nd, 5th and 10th percentiles, as the\n    code computes all three. The paper gives no measure of similarity, so two readings. (a) Across\n    the responses with a dominant peak at both thresholds, the period at 5% and at 2% correlates\n    positively with that at 10% (Spearman, p < 0.05). (b) The median absolute difference from the\n    10% period is under 10% of the median 10% period. Reproduced when one reading holds for both\n    lower thresholds.\n  depends_on:\n  - fig2ef-periodic-recurrence\n- id: fig3a-coalescence\n  statement: Almost all evoked responses reach a state of high recurrence within one oscillation\n    period of stimulation and are thereafter dominated by recurrence.\n  source: Results, Joint population activity meets the conditions for a periodic attractor,\n    paragraph 2; Figure 3A\n  quote: We found that almost all evoked population responses quickly reached a state of high\n    recurrence, within one oscillation period ( Figure 3A ), and were thereafter dominated by\n    recurrence\n  criterion: Coalescence time as the Methods and the Figure 3A legend, the mid-point of the first\n    5 s window (step 1 s) in which at least 90% of the points recur, measured from stimulation\n    onset; stability as the proportion of recurrent points after it. Reproduced when the\n    coalescence time is no longer than the response's dominant period (claim\n    fig2ef-periodic-recurrence) in at least 27 of the 30 responses and the proportion of recurrent\n    points exceeds 50% in at least 27 (\"almost all\" is not counted by the paper; the rule of 27\n    is fixed here). The coalescence time is also reported from stimulation offset.\n  depends_on:\n  - fig2ef-periodic-recurrence\n- id: fig3c-same-manifold\n  statement: Sequentially evoked responses of a preparation fall on the same manifold; their\n    distance is below that of random projections for all pairs except two, pairs (1,2) and (1,3)\n    of preparation 4.\n  source: Results, Joint population activity meets the conditions for a periodic attractor,\n    paragraph 4; Figure 3C legend\n  quote: pairs of evoked population responses from the same preparation fell close to each other\n    throughout ( Figure 3C ), well in excess of the expected agreement between random projections of\n    the data onto the same embedding dimensions\n  expected:\n    quantity: pairs of responses closer than their random-projection control, of 30\n    value: 28\n    tolerance: 2.8\n  criterion: As the Methods (Testing convergence to the same manifold) and\n    Are_sequential_attractors_the_same.m. All three programs of a preparation projected onto the\n    PCA axes of program 1 (code; raw spike-density functions times the eigenvectors, not\n    mean-centred), in the smallest number of program 1's PCs reaching 80%. Hausdorff distance\n    between the pair's point sets; control, the Hausdorff distance after shuffling the neurons of\n    one program, 100 shuffles, mean taken. The point sets are (a) the recurrent points (Methods)\n    or (b) all points of runs of 5 s windows with at least 90% recurrence, from the later of the\n    two programs' first such point (the code). Reproduced when, under a reading, at least 25 of\n    the 30 pairs have a distance below their control mean; the pairs that fail are named against\n    those of preparation 4.\n  depends_on:\n  - fig3a-coalescence\n- id: fig3s1a-common-axes\n  statement: The convergence of sequential responses to the same manifold holds when the three\n    programs are projected onto common axes from a PCA of their concatenated activity.\n  source: Figure 3—figure supplement 1A\n  quote: We obtain the same results: sequentially-evoked programs converge to the same manifold\n  criterion: As claim fig3c-same-manifold, with the axes from a PCA of the three programs'\n    concatenated post-onset spike-density functions (Methods; Are_sequential_attractors_the_same_CommonAxes.m,\n    which keeps the PCs whose cumulative variance is at most 80%). Reproduced when at least 25 of\n    the 30 pairs have a distance below their control mean.\n  depends_on:\n  - fig3c-same-manifold\n- id: fig3d-initial-conditions\n  statement: Stimulation drives responses of the same preparation far apart before coalescence,\n    more than at stimulus onset or after both have coalesced, so the same manifold is reached from\n    different initial conditions.\n  source: Results, Joint population activity meets the conditions for a periodic attractor,\n    paragraph 5; Figure 3D\n  quote: We found that the stimulation caused population responses within the same preparation to\n    diverge far more than in either the spontaneous activity or after coalescing to the manifold (\n    Figure 3D )\n  criterion: Three distances per pair, as the Figure 3D legend and Initial_Conditions.m, in the\n    common axes of claim fig3s1a-common-axes. Onset, the distance between the two programs' points\n    at stimulation onset; transient, the maximum over points between onset and coalescence of the\n    maximum distance to the other program's points in that span; coalesced, the Hausdorff distance\n    of claim fig3s1a-common-axes. The paper reports no test. Reproduced when the transient\n    distance exceeds both other distances in more than half of the 30 pairs and its median exceeds\n    both medians (a rule fixed here).\n  depends_on:\n  - fig3s1a-common-axes\n- id: fig3f-pairwise-similarity\n  statement: Pairwise similarity between neurons is preserved across responses of the same\n    preparation, above a null model, except for pairs (1,3) and (2,3) of preparation 7.\n  source: Results, Joint population activity meets the conditions for a periodic attractor,\n    paragraph 6; Figure 3F legend\n  quote: We found that pair-wise similarity is indeed well-preserved across population responses in\n    the same preparation ( Figure 3F )\n  expected:\n    quantity: pairs of responses whose similarity matrices correlate above the control, of 30\n    value: 28\n    tolerance: 2.8\n  criterion: Similarity S as the correlation coefficient between neurons' post-onset\n    spike-density functions, negative values set to zero and the diagonal to zero (StaticEnsembles.m,\n    Are_sequential_attractors_the_same.m); data, the correlation of S(A) with S(B); control, the\n    correlation of S(A) with the null model E_ij = s_i s_j / T (Methods). Open details, all run:\n    the correlation is Spearman (the code that is plotted) or Pearson; the control for a pair is\n    that of its first program, or the larger of its two programs' controls. Reproduced when, under\n    a reading, at least 25 of the 30 pairs have a data correlation above their control.\n- id: fig3h-perturbations-return\n  statement: Of 19 spontaneous divergences from the trajectory, 17 (90%) returned to a recurrent\n    state; the two that did not were consistent with the end of the evoked locomotion.\n  source: Results, Joint population activity meets the conditions for a periodic attractor,\n    paragraph 7; Materials and methods, Testing return to the same manifold after perturbation;\n    Figure 3H\n  quote: For the remaining 19 divergent periods, we then determined if the population activity\n    returned to a recurrent state after the divergent point; that is, whether the density of\n    recurrence returned above 90% or not. The majority (17/19) did\n  expected:\n  - quantity: divergent periods\n    value: 19\n    tolerance: 1.9\n  - quantity: divergent periods that returned to above 90% recurrence\n    value: 17\n    tolerance: 1.7\n  criterion: As the Methods and recurrence_point_results_Viz.m with\n    Are_jumps_perturbations_or_transitions2.m. After coalescence, a divergent period is a run of\n    5 s windows with recurrence density below 90% that falls below 50% at least once; its\n    divergent point is the window of lowest density; periods whose divergent point lies within two\n    cycles (dominant period) of the recording's end are removed. Reproduced when both counts are\n    within tolerance and the returned fraction is at least 80%.\n  depends_on:\n  - fig3a-coalescence\n- id: fig3i-same-manifold-after\n  statement: Of the 17 divergences that returned to a recurrent state, all but three returned to\n    the same manifold; the three appeared to move to a different periodic attractor.\n  source: Results, Joint population activity meets the conditions for a periodic attractor,\n    paragraph 7; Figure 3I\n  quote: Of those that returned, all but three clearly returned to the same manifold ( Figure 3I )\n  expected:\n    quantity: returned divergences that came back to the same manifold\n    value: 14\n    tolerance: 1.4\n  criterion: As the Methods, the final window before the divergent period, and the proportion of\n    its recurrent points whose recurrence falls after (a) the end of the divergent period, as the\n    Methods say, or (b) the divergent point, as the code's blnSame uses; same manifold when that\n    proportion exceeds 0.2 (the code's jumppars.theta; the Methods give no value). Reproduced when,\n    under a reading, the count is within tolerance.\n  depends_on:\n  - fig3h-perturbations-return\n- id: fig4bc-stable-spiral\n  statement: The evoked responses have highly clustered maximum eigenvalues of the local linear\n    dynamics, dominated by negative complex values, so the pedal ganglion implements a contracting\n    periodic orbit, a stable spiral attractor, found in every preparation.\n  source: Results, Heterogenous population activity arises from a common attractor, paragraph 2;\n    Introduction, last paragraph; Figure 4B\n  quote: Doing so, we found that the evoked population responses had highly clustered maximum\n    eigenvalues ( Figure 4B,C ), and thus highly similar underlying dynamics ... The dominance of\n    negative complex eigenvalues implies the pedal ganglion network implements a contracting\n    periodic orbit - it is a stable spiral attractor\n  criterion: As the Methods (Statistical estimation of the attractor's parameters) with the code's\n    settings in the opening comment; per response, the means of the real (a) and imaginary (b)\n    parts of the maximum eigenvalue over the recurrent points of the dominant orbit with at least\n    100 neighbours. Stable spiral when a < -0.0001 and b > 0.0005, the edges of the grey bands\n    drawn in Figure 4B by Figure_LinearDynamics.m. Reproduced when the mean over the 30 responses\n    is a stable spiral and each of the 10 preparations has at least two of its three responses in\n    the stable spiral region; partially reproduced when the grand mean holds but fewer\n    preparations do. The spread (SD over responses of a and b) is reported.\n  depends_on:\n  - fig2ef-periodic-recurrence\n- id: fig4c-orbital-period\n  statement: The linear model estimates a mean orbital period of about 10 s, consistent with the\n    period from the recurrent points.\n  source: Results, Heterogenous population activity arises from a common attractor, paragraph 5;\n    Figure 4C\n  quote: The linear model estimated a mean orbital period of around 10 s ( Figure 4C ), consistent\n    with the directly-derived estimate from the recurrent points ( Figure 2F )\n  expected:\n    quantity: mean over responses of the linear-model orbital period\n    value: 10\n    tolerance: 1\n    unit: s\n  criterion: Per response, the period 2 pi / b times 0.01 s from the mean imaginary part b of claim\n    fig4bc-stable-spiral (Figure_LinearDynamics.m; the Methods' printed formula is garbled), then\n    the mean over the 30 responses. The mean over responses of the per-point rotation periods\n    (RcrStats.mRot) is shown as a variant. Consistency is reported as the Pearson correlation of\n    the 30 linear-model periods with the 30 recurrence periods.\n  depends_on:\n  - fig4bc-stable-spiral\n- id: fig4s1a-contracting-dimensions\n  statement: In most responses the trajectory contracts in all embedding dimensions; a few\n    responses have a positive real eigenvalue in one low-variance dimension, a minor expansion.\n  source: Results, Heterogenous population activity arises from a common attractor, paragraph 3;\n    Figure 4—figure supplement 1A\n  quote: In most population responses, the low-dimensional trajectory had negative, complex\n    eigenvalues in all embedding dimensions ... Intriguingly, a few population responses had a\n    positive real eigenvalue in one low-variance dimension\n  criterion: As Check_All_Real_Eigenvalues.m, per response the mean real part of each unique\n    eigenvalue dimension (conjugate pairs counted once) over the points of claim\n    fig4bc-stable-spiral. Reproduced when more than 15 of the 30 responses have all means negative\n    and at least one response, but fewer than half, has one positive mean in a dimension other\n    than the first.\n  depends_on:\n  - fig4bc-stable-spiral\n- id: fig4s1b-rotation-dominant\n  statement: Local trajectories were dominated by rotation throughout; in every preparation most\n    local models have a complex eigenvalue among their top two.\n  source: Figure 4—figure supplement 1B\n  quote: Population responses were dominated by rotation throughout\n  criterion: As Check_All_Real_Eigenvalues.m (Pcomplex12), per response the proportion of local\n    models in which either of the two largest eigenvalues is complex. Reproduced when the\n    proportion exceeds 0.5 in every response; partially reproduced when it does so in a majority\n    of responses of every preparation.\n  depends_on:\n  - fig4bc-stable-spiral\n- id: fig5b-period-changes\n  statement: Over a response the orbital period may slow, speed up or not change; all three occur\n    among the 30 responses.\n  source: Results, Heterogenous population activity arises from a common attractor, paragraph 5;\n    Figure 5B\n  quote: We found that the population responses included all possible changes in periodic orbit:\n    slowing, speeding up, and not changing ( Figure 5B )\n  statistics:\n  - test: weighted Spearman's rank correlation, permutation test\n    p: 0.01\n    p_relation: \"<\"\n    n: 30 responses, 31 to 72 local estimates each\n  expected:\n  - quantity: fewest local estimates per response\n    value: 31\n    tolerance: 3.1\n  - quantity: most local estimates per response\n    value: 72\n    tolerance: 7.2\n  criterion: As the Methods (Tracking changes in periodicity) and Does_Oscillation_Period_Change.m,\n    the mean recurrence time of all recurrent points in each 5 s window, from coalescence to the\n    final window with at least 90% recurrent points; weighted Spearman correlation of window time\n    and mean recurrence time, weights 1/SD of recurrence times times the proportion of recurrent\n    points (windows with zero or undefined SD weighted 0, as the code); permutation p-value with\n    10000 permutations (Methods; the code's 100000 permutations of pooled values is a variant).\n    Reproduced when at least one response has rho > 0 with p < 0.01, at least one rho < 0 with\n    p < 0.01, and at least one p of 0.01 or more, and the number of windows per response lies in\n    27.9 to 79.2.\n  depends_on:\n  - fig3a-coalescence\n- id: fig5c-no-relation-contraction\n  statement: There is no relationship between the change in orbital period over a response and its\n    rate of contraction, as a stable spiral predicts.\n  source: Results, Heterogenous population activity arises from a common attractor, paragraph 5;\n    Figure 5C legend\n  quote: As predicted there was no relationship between the contraction of the periodic orbit and\n    its change in period ( Figure 5C )\n  statistics:\n  - test: Pearson's R\n    p: 0.05\n    p_relation: \">\"\n    n: 30 responses\n  criterion: A claim of absence, judged on the paper's test, Pearson's R across the 30 responses\n    between the weighted rho of claim fig5b-period-changes and the mean real part of the maximum\n    eigenvalue of claim fig4bc-stable-spiral (Figure_LinearDynamics.m). The paper prints no\n    threshold; p < 0.05, the conventional level, is taken here and the statistics entry records it\n    as that reading. Reproduced when p is 0.05 or more; R and p are reported either way, and with\n    the contraction in %/s as a variant.\n  depends_on:\n  - fig5b-period-changes\n  - fig4bc-stable-spiral\n- id: fig6d-decode-p10\n  statement: P10 nerve activity can be fitted and forecast from the low-dimensional trajectory in\n    all nine responses with P10 recordings, so the trajectory encodes muscle commands.\n  source: Results, The locomotion motor program can be decoded from the low-dimensional orbit,\n    paragraphs 2 and 3; Figure 6B to 6D\n  quote: The model could accurately fit and forecast P10 activity from the low-dimensional\n    trajectory in all nine population responses ( Figure 6D )\n  criterion: As the Methods (Decoding motor output). P10 spikes convolved with a Gaussian of the\n    program's width; a Poisson GLM with log link of the P10 rate on the past history of the PCs\n    (80% variance, as claim fig2b-dimensions), histories 50 to 200 ms in 10 ms steps, the history\n    with the smallest median absolute error of forecast kept per program; fit on a 40 s window and\n    forecast the next 10 s, windows stepped by 1 s from 33 s (after the stimulus, as the code) to\n    the end. Forecast R (correlation coefficient) and MAE (median absolute error) per window.\n    Reproduced when in each of the nine responses the mean forecast R minus 2 s.e.m. over its\n    windows is above 0 (Figure 6D shows means plus or minus 2 s.e.m.; \"accurately\" is otherwise\n    unquantified). The code's windowing (training on 50% of the series, 0.2 s steps, histories to\n    250 ms) is a variant. The paper's 173 forecast windows are reported against the count each\n    windowing gives, not judged.\n  depends_on:\n  - fig6s1-no-p10-motorneurons\n- id: fig6s1-no-p10-motorneurons\n  statement: No recorded neuron is a P10 motorneuron; no neuron comes close to one-to-one locking\n    of its spikes with P10 spikes at any delay, nor locks consistently across programs.\n  source: Figure 6—figure supplement 1; Materials and methods, Decoding motor output, paragraph 1\n  quote: We see that no neuron in our dataset comes close to P ( s p i k e 10 | s p i k e ) ≈ 1 at\n    any delay, and there are no neurons with consistently high locking between programs\n  criterion: As the legend and P10_ID_motorneurons.m, for each neuron and each program with P10,\n    spikes after 33 s, the proportion of its spikes followed by a P10 spike at delays 0 to 25 ms\n    (1 ms steps) within plus or minus 2 ms, maximum over delays. The paper gives no cut-off for\n    \"close to 1\"; 0.9 is taken here. Reproduced when no neuron has a maximum of 0.9 or more in two\n    programs of its preparation; the largest values are reported.\n- id: fig6s2-dimensions-p10\n  statement: The nine recordings with P10 activity need only 3 to 5 embedding dimensions for 80%\n    variance, and at least double that for 90%; using the 90% dimensions does not improve the P10\n    forecasts.\n  source: Results, The locomotion motor program can be decoded from the low-dimensional orbit,\n    paragraph 4; Figure 6—figure supplement 2\n  quote: The successful decoding of future P10 activity was achieved despite needing only 3–5\n    embedding dimensions to account for 80% variance ... Increasing the number of embedding\n    dimensions to account for 90% variance, at least doubling the number of embedding dimensions,\n    did not improve the forecasts of P10 activity\n  expected:\n  - quantity: fewest dimensions for 80% variance, P10 recordings\n    value: 3\n    tolerance: 0.3\n  - quantity: most dimensions for 80% variance, P10 recordings\n    value: 5\n    tolerance: 0.5\n  criterion: Dimension counts as claim fig2b-dimensions, under its readings, for the nine\n    responses; reproduced in part when all nine lie in 2.7 to 5.5 and the 90% count is at least\n    twice the 80% count in each. The forecasts of claim fig6d-decode-p10 repeated with the 90%\n    dimensions; the paper reports no test, so a two-sided Wilcoxon signed-rank test over the nine\n    paired mean MAEs and mean forecast R-squared values is fixed here. The absence holds when\n    neither test finds the 90% models better at p < 0.05. Reproduced when the counts and the\n    absence both hold.\n  depends_on:\n  - fig2b-dimensions\n  - fig6d-decode-p10\n- id: fig7a-long-tailed-participation\n  statement: Every response has a long-tailed distribution of single-neuron participation, a\n    minority of neurons dominating its dynamics.\n  source: Results, Variable neuron participation in stable motor programs, paragraph 2; Figure 7A\n  quote: Every population response had a long-tailed distribution of participation ( Figure 7A ),\n    indicating that a minority of neurons dominated the dynamics of any given response\n  criterion: Participation as the Methods (Single neuron participation), the sum over the d\n    principal axes of the program of the absolute eigenvalue-weighted eigenvector weights,\n    normalised to the program's maximum. d is (a) the program's own count for 80% (Methods) or (b)\n    the count from the PCA of the three programs concatenated, cumulative variance at most 80%,\n    used for all three (Quantifying_Participation_by_PCA_Contribution.m). The paper does not\n    quantify \"long-tailed\"; fixed here, reproduced when, under a reading, in every response the\n    skewness of participation is positive and fewer than half of the neurons exceed 50% of the\n    maximum.\n  depends_on:\n  - fig2b-dimensions\n- id: fig7f-strongly-variable-neurons\n  statement: Neurons with high participation in one response often have low participation in\n    another; every preparation contains neurons whose change in participation well exceeds that\n    predicted by a noise model.\n  source: Results, Variable neuron participation in stable motor programs, paragraph 2; Figure 7B\n    to 7F\n  quote: Every preparation’s pedal ganglion contained neurons whose change in participation between\n    responses well-exceeded that predicted by the noise model ( Figure 7F )\n  criterion: Participation as claim fig7a-long-tailed-participation. Per preparation, the changes\n    in participation of each neuron between programs, pooled over (a) all three pairs (Methods,\n    \"all pairs\") or (b) the consecutive pairs (1,2) and (2,3) (the code); a Gaussian fitted by the\n    Methods' iterative maximum likelihood (iterateoutliers.m: drop the point furthest from the\n    mean, refit, stop when the log likelihood falls); a neuron is strongly variable when its\n    maximum absolute change between consecutive programs is at least the larger of\n    |mean - 3 SD| and |mean + 3 SD|. Reproduced when, under a reading, each of the 10 preparations\n    has at least one strongly variable neuron. The proportion per preparation (Figure 7F) is\n    reported.\n  depends_on:\n  - fig7a-long-tailed-participation\n- id: halving-participation\n  statement: Even the most strongly participating neurons in a response could more than halve their\n    participation in other evoked responses.\n  source: Discussion, Insights and challenges of variable neuron participation, paragraph 1\n  quote: Even the most strongly participating neurons in a given population response could more\n    than halve their participation in other evoked responses\n  criterion: Participation as claim fig7a-long-tailed-participation, normalised to each program's\n    maximum. The most strongly participating neurons are read as (a) the neuron at 100% in a\n    program, or (b) the top 10% of a program's neurons. Reproduced when, under a reading, such a\n    neuron has under half its participation in another program of its preparation in more than one\n    preparation; the count of preparations is reported.\n  depends_on:\n  - fig7a-long-tailed-participation\n- id: fig7s1-rate-synchrony\n  statement: A neuron's participation reflects both its firing rate and its synchrony; firing rate\n    explains on average 50% of the variation in participation within a response, and rate changes\n    23% of the change in participation between responses.\n  source: Figure 7—figure supplement 1B and 1D\n  quote: Firing rate explains on average (R 2 , red line) 50% of the variation in participation\n    within an evoked response ... Firing rate changes explain on average 23% of the variation in the\n    change of participation\n  expected:\n  - quantity: mean R-squared, rate against participation, 30 programs\n    value: 0.5\n    tolerance: 0.05\n  - quantity: mean R-squared, change in rate against change in participation, 30 pairs\n    value: 0.23\n    tolerance: 0.023\n  criterion: As What_is_Participation.m, Pearson correlation per program of normalised\n    participation with the firing rate, squared, and the mean over the 30 programs; and per pair\n    (1,2), (1,3), (2,3) of a preparation, of the change in rate with the change in participation,\n    mean of R-squared over the 30 pairs. The rate is the spike count divided by duration from (a)\n    stimulation offset to the end (the legend) or (b) stimulation onset (the code). In the code the\n    rate changes are ordered (1,2), (1,3), (2,3) and the participation changes (1,2), (2,3),\n    (1,3), so two of the three pairs are mismatched; the matched pairs are the main reading and\n    the code's pairing a variant.\n  depends_on:\n  - fig7a-long-tailed-participation\n- id: fig7s2-no-invariant-core\n  statement: No small invariant core of strongly participating, phasically active neurons, such as\n    a classic central pattern generator, is found across preparations.\n  source: Results, Variable neuron participation in stable motor programs, paragraph 3; Figure\n    7—figure supplement 2\n  quote: in our observed portion of the ganglion we found no evidence for a core of strongly\n    participating, invariant, and phasically active neurons across the preparations\n  criterion: Ensembles and their types (tonic, oscillator, burster, pauser) as the Methods and\n    Bruno et al. (2015), with the code's toolbox (consensus_cluster_spike_data_binless.m and\n    Analyse_Spike_Train_Properties.m), from stimulation onset. Neurons typed oscillator in all\n    three programs; the top 10% of them by maximum participation per preparation, and the median\n    of their maximum change in participation between consecutive programs (panel C). The paper\n    gives no cut-off; fixed here, an invariant core is a preparation whose top 10% have a median\n    maximum change under 10% of the program maximum. Reproduced when fewer than half of the\n    preparations have one (\"most preparations showed high variation\"). The legend's statement that\n    only the oscillator class had a consistently typed neuron in all ten preparations is\n    reported.\n  depends_on:\n  - fig7f-strongly-variable-neurons\n- id: fig7gh-robust-to-participation\n  statement: The distance between a pair of responses does not correlate with the total change in\n    neuron participation between them nor with the distance between their participation\n    distributions; the program is robust to the participation of single neurons.\n  source: Results, Variable neuron participation in stable motor programs, paragraph 4; Figure 7G\n    and 7H\n  quote: We found that the distance between a pair of population responses did not correlate with\n    either the total change in neuron participation between the two responses ( Figure 7G ) or the\n    distance between their participation distributions ( Figure 7H )\n  criterion: A claim of absence. Distance, the Hausdorff distance of claim fig3c-same-manifold\n    divided by its control mean; total change, the sum over neurons of the absolute change in\n    normalised participation; distribution distance, the Hellinger distance between histograms of\n    normalised participation in bins of 0.05 on 0 to 1 (Methods;\n    RobustnessOfAttractor_to_single_neuron_variability.m). The pairs containing response 1 of\n    preparation 4 are excluded as the legend says (the code keeps pairs with normalised distance\n    below 1). The paper names no test; the code fits a linear regression (fitlm), so the test is\n    the slope's p-value at the conventional p < 0.05. Reproduced when neither slope is\n    significant; slopes and R-squared are reported, and the robust (bisquare) fit as a variant.\n  depends_on:\n  - fig3c-same-manifold\n  - fig7a-long-tailed-participation\n- id: fig8-caudolateral\n  statement: Neurons with strong participation across the three responses, and those with highly\n    variable participation, lie mainly in the caudo-lateral quadrant of the ganglion.\n  source: Results, Participation maps identify potential locations of the pattern generator\n    network, paragraph 1; Figure 8\n  quote: We found that neurons with strong participation across the three evoked population\n    responses were robustly located in the caudo-lateral quadrant of the ganglion ( Figure 8A,B )\n  criterion: Neuron positions from the data set's maps, 4 left and 4 right preparations (the code's\n    LEFT and RIGHT lists in ParticipationMapsSummary.m), each preparation's maximum (A,B) and\n    range (C,D) of normalised participation over the three programs; the top fifth by the code's\n    equal-width division of the range of values into five (\"quintile\" in the legend; true\n    quintiles are a variant). The orientation of the array (which quadrant is caudo-lateral) is\n    not stated in the paper or the code, and must come from the data set's documentation or map\n    files; if it cannot be found the claim is blocked. Reproduced when, for both sides, the\n    caudo-lateral quadrant holds more of the top-fifth neurons than any other quadrant, for\n    maximum and for range. The right ganglia's rostro-medial strength, which the paper leaves\n    unresolved, is reported.\n  depends_on:\n  - fig7a-long-tailed-participation\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/crcns-apl-1; f=10.7554-elife.27342.yaml; grep -n "—" $f; grep -n -i "rather" $f; grep -nE "^\s+(- )?[a-z_]+: .*: |^\s{4,}[^#-].*: " $f | grep -v "^\S*#"
```

```
71:# Not made into claims: the three-neuron model of Figure 1—figure supplement 1 (a simulation, no
72:# data), and Figure 2—figure supplement 1, which describes the range of dynamics without a finding
203:  source: Figure 2—figure supplement 2; Materials and methods, Recurrence analysis, paragraph 2
258:  source: Figure 3—figure supplement 1A
386:    Figure 4—figure supplement 1A
400:  source: Figure 4—figure supplement 1B
482:  source: Figure 6—figure supplement 1; Materials and methods, Decoding motor output, paragraph 1
495:    paragraph 4; Figure 6—figure supplement 2
569:  source: Figure 7—figure supplement 1B and 1D
594:    7—figure supplement 2
91:    value: 10
92:    tolerance: 0
94:    value: 30
95:    tolerance: 0
97:    value: 1131
98:    tolerance: 0
111:    quantity: frequency of the dominant peak of the mean post-stimulation spectrum
112:    value: 0.1
113:    tolerance: 0.01
114:    unit: Hz
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims/crcns-apl-1; f=10.7554-elife.27342.yaml; python3 - <<'EOF'
p='10.7554-elife.27342.yaml'
s=open(p).read()
s=s.replace('—figure supplement',', figure supplement')
s=s.replace("ensembles. (a) The Methods' ensemble rule applied to the whole population: spike counts in","ensembles. (a) The Methods' ensemble rule applied to the whole population, spike counts in")
s=s.replace("  quote: We obtain the same results: sequentially-evoked programs converge to the same manifold","  quote: \"We obtain the same results: sequentially-evoked programs converge to the same manifold\"")
s=s.replace("Methods' iterative maximum likelihood (iterateoutliers.m: drop the point","Methods' iterative maximum likelihood (iterateoutliers.m, drop the point")
s=s.replace("""  quote: We found that the population responses included all possible changes in periodic orbit:
    slowing, speeding up, and not changing ( Figure 5B )""","""  quote: "We found that the population responses included all possible changes in periodic orbit:
    slowing, speeding up, and not changing ( Figure 5B )\"""")
s=s.replace("""  statistics:
  - test: Pearson's R
    p: 0.05
    p_relation: ">"
    n: 30 responses
""","")
s=s.replace("threshold; p < 0.05, the conventional level, is taken here and the statistics entry records it\n    as that reading.","threshold and no R or p; p < 0.05, the conventional level, is taken here.")
open(p,'w').write(s)
EOF
grep -n "—\|7, figure supplement 2$" $f | head; cd  python tools/claims_check.py claims/crcns-apl-1/10.7554-elife.27342.yaml paper/10.7554-elife.27342.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-apl-1/10.7554-elife.27342.yaml; sed -i 's/(Methods). Open details, all run:$/(Methods). Open details, all run,/' $f; grep -nE "[^ ]: |:$" $f | grep -vE "^[0-9]+:\s*#|^[0-9]+:\s*(- )?[a-z_]+:( |$)" ; python tools/claims_check.py $f paper/10.7554-elife.27342.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -c "—" claims/crcns-apl-1/*.yaml; grep -ci "rather" claims/crcns-apl-1/*.yaml; git status --short
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
?? claims/crcns-apl-1/
?? scripts
```

**Agent**

I wrote the claims file at `claims/crcns-apl-1/10.7554-elife.27342.yaml`. It has 30 claims, and the quote checker passes: 30 quotes, 0 problems. Nothing was committed.

**Text read.** I read the version of record (PMC5546814), flattened from its JATS XML: main text, Methods, and the legends of Figures 1 to 8 and all twelve figure supplements. The paper has no other supplementary file, and no PDF of it was supplied; no claim needed one. I read the data descriptor only to see what the dataset holds.

**Code read.** github.com/mdhumphries/AplysiaAttractorAnalysis at commit e5f28e98. It holds the MATLAB scripts for every analysis and figure. Where the Methods are silent, the code settles: the recurrence settings, the local linear fits, how rotation period and contraction rate are computed, the cut-offs for the Figure 4B regions, the 0.2 cut-off for "same manifold", the ensemble and similarity measures, and the left and right preparation lists for the maps.

**Claims.**
- 30 claims, all with a quote and none `inferred`. All use the dataset itself.
- 29 have criteria; 16 have expected values.
- One statistics entry: Figure 5B, weighted Spearman with a permutation test, P < 0.01. The paper prints no other test result.
- I made no claim for the three-neuron model (Figure 1, figure supplement 1), which is a simulation, or for Figure 2, figure supplement 1, which is descriptive.

**Where the code differs from the Methods.** Following the protocol, the Methods are the main reading and the code's choice is a variant:
- **Gaussian width:** the Methods print median ISI/12, which may be a square root lost in extraction. The code uses the median ISI itself, pooled over all recordings of that stimulation number read so far.
- **Number of PCs:** the Methods say "at least 80%" of variance. The recurrence code keeps the PCs whose cumulative variance is at most 80%; the manifold code uses at least 80%.
- **Dominant period:** the Methods say the mean recurrence time of the dominant peak; the code uses the median.
- **P10 decoding windows:** the Methods use a 40 s fit stepped by 1 s with 50 to 200 ms histories. The code trains on 50% of the series, steps 0.2 s, and tries histories up to 250 ms.
- **Permutation test:** 10,000 permutations in the Methods; 100,000 in the code, which permutes the pooled values and is one-sided.
- **Point sets for the Hausdorff distance:** recurrent points in the Methods; windows with at least 90% recurrence in the code.
- **Noise model for participation:** all pairs of programs in the Methods; consecutive pairs only in the code.
- **Participation dimensions:** each program's own count, or the count from the PCA of the three programs together (the code).
- **Return after a perturbation:** recurrences counted after the end of the divergent period (Methods) or after its divergent point (code).
- **Rate behind participation (Fig. 7, figure supplement 1):** spikes counted from stimulus offset (legend) or onset (code). The code also mismatches two of the three pairs when it compares changes in rate with changes in participation.

**Open details and the readings named.**
- Decay of the population rate: the Methods' 20 s window R < -0.2 rule, or a negative regression slope.
- Robustness to the recurrence threshold: Spearman agreement, or the median difference.
- Similarity correlation: Spearman or Pearson, and which program's control a pair is compared with.
- "Most strongly participating" neurons: the top neuron or the top 10%.
- "Quintile" in Figure 8: the code's equal-width bins or true quintiles.

**Rules I fixed because the paper gives none, each stated as such in the criterion:**
- the counts behind "generally" and "almost all" (27 of 30);
- the comparison for initial conditions;
- "accurately" for P10 decoding (mean forecast R minus 2 s.e.m. above 0);
- "close to 1" for motorneuron locking (0.9);
- what counts as long-tailed;
- the invariant-core cut-off;
- the Wilcoxon test for "no improvement at 90%";
- p < 0.05 for the claims of absence in Figures 5C and 7G/H, where the paper prints neither a threshold nor a statistic.

**Missing from the paper, or not reconcilable:**
- **Figure 8 orientation:** neither the paper nor the code says which quadrant of the array is caudo-lateral. It has to come from the dataset's map files, or that claim is blocked.
- **Neuron counts:** the paper gives 120 to 180 neurons per recording; the dataset description gives 75 to 160. The 1131 total matches.
- **Forecast windows:** the paper's 173 forecast windows match neither the Methods' windowing nor the code's, so it is reported and not judged.

## End of run

29 turns, 6 minutes, $3.02 at API prices, result: success.
