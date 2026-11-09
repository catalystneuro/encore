# crcns-apl-1 · claims-check · run 42477647120

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/crcns-apl-1/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 100,220p docs/protocol.md; cat claims/crcns-apl-1/*.yaml; python tools/claims_check.py claims/crcns-apl-1/10.7554-elife.27342.yaml paper/10.7554-elife.27342.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 120,200p docs/protocol.md; echo ======; python tools/claims_check.py claims/crcns-apl-1/10.7554-elife.27342.yaml paper/10.7554-elife.27342.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-apl-1/10.7554-elife.27342.yaml"
}
```

```
1	# Claims for Bruno, Frost & Humphries (2017), eLife 6:e27342, "A spiral attractor network drives
2	# rhythmic locomotion", doi:10.7554/elife.27342, on CRCNS data set apl-1 (doi:10.6080/K0SN074B).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
4	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
5	#
6	# Text read: the version of record (PMC5546814, open access), as JATS XML flattened to text under
7	# paper/: main text, Materials and methods, and the legends of Figures 1 to 8 and of all twelve
8	# figure supplements. The paper has no other supplementary file. No PDF of the paper was supplied,
9	# and none was needed: no claim rests on a number shown only in a figure. The extraction garbles
10	# some formulas: the Gaussian width reads "σ = {median ISI in population}/12" (a square root may be
11	# lost) and the rotation period reads "ω = 2πbΔt"; the code settles the second (see below).
12	# The data set's description (paper/apl-1.data-description.txt) was read only to know what it
13	# holds; no claim comes from it.
14	#
15	# Code read: https://github.com/mdhumphries/AplysiaAttractorAnalysis, commit e5f28e98 (2018-07-11),
16	# MATLAB, linked from the paper's Data and code availability. Analysis/DataSet_Properties.m builds
17	# the spike-density functions and the PCA; Analysis/Classify_attractors/ holds the recurrence
18	# analysis (Analyse_by_Recurrence_Points.m, LocalLinearDynamics.m, recurrence_point_results_Viz.m),
19	# manifold comparisons (Are_sequential_attractors_the_same.m and _CommonAxes.m,
20	# Initial_Conditions.m), perturbations (Are_jumps_perturbations_or_transitions2.m), period change
[... 623 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/10.7554-elife.27342.txt; ls  ls ~ 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes with 0 problems. Now reading the paper to check each claim.

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
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.27342.txt",
 "offset": 249,
 "limit": 170
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/mdhumphries/AplysiaAttractorAnalysis && cd AplysiaAttractorAnalysis && git log -1 --format='%h %ad' && find . -name "*.m" | wc -l
```

```
e5f28e9 Wed Jul 11 09:57:57 2018 +0100
99
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && find . -name "*.m" | sort && echo ---- && grep -n "sigma\|median\|princomp\|mtspectrumpt\|fpass\|params\|2\*std\|SD\b" Analysis/DataSet_Properties.m | head -60
```

```
./Analysis/Classify_attractors/Analyse_by_Recurrence_Points.m
./Analysis/Classify_attractors/Are_jumps_perturbations_or_transitions2.m
./Analysis/Classify_attractors/Are_sequential_attractors_the_same.m
./Analysis/Classify_attractors/Are_sequential_attractors_the_same_CommonAxes.m
./Analysis/Classify_attractors/CatalogueAttractors_by_recurrence.m
./Analysis/Classify_attractors/Check_All_Real_Eigenvalues.m
./Analysis/Classify_attractors/Dimensionality_of_Projections.m
./Analysis/Classify_attractors/Does_Oscillation_Period_Change.m
./Analysis/Classify_attractors/Initial_Conditions.m
./Analysis/Classify_attractors/LocalLinearDynamics.m
./Analysis/Classify_attractors/Quantify_attractors_by_recurrence_plot_lines.m
./Analysis/Classify_attractors/Quantifying_Participation_by_PCA_Contribution.m
./Analysis/Classify_attractors/RecurrencePlot_LineCounting.m
./Analysis/Classify_attractors/RobustnessOfAttractor_to_single_neuron_variability.m
./Analysis/Classify_attractors/Toy3DOscillator.m
./Analysis/Classify_attractors/What_is_Participation.m
./Analysis/Classify_attractors/recurrence_point_results_Viz.m
./Analysis/DataSet_Properties.m
./Analysis/Ensembles/Analyse_Spike_Train_Properties.m
./Analysis/Ensembles/Change_of_Firing_Rates_StaticEnsembles.m
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && sed -n 105,200p Analysis/DataSet_Properties.m
```

```
%% loop and analyse data
dirP = dir(spikepath); dirP = dirP(3:end);   % discard top two entries: always cd/ commands

nfiles = numel(dirP);
Dctr = 0;
DataTable = []; allrates = []; allisis = [];
for loop = 1:nfiles
    SpkData = struct([]);  % need spike-times in struct to pass to Chronux functions
    if any(strfind(dirP(loop).name,'.mat')) && any(strfind(dirP(loop).name,stimset)) 
        Dctr = Dctr + 1; % number of recordings in data-set
        load([spikepath '/' dirP(loop).name]);
        if ~exist('spks','var') error(['Data-file ' dirP(loop).name ' does not contain spks variable']); end

        % T_start_recording = min(spks(:,2));
        T_start_recording = stimstart;  % start from 30 s in
        T_end_recording = max(spks(:,2));
        
        FileTable{Dctr} = dirP(loop).name;  % keep list of filenames
        
        % remove spontaneous period from this analysis
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && sed -n 80,100p Analysis/DataSet_Properties.m; sed -n 200,215p Analysis/DataSet_Properties.m; echo ----; grep -n "prctVar\|0\.8\|prctile\|theta\|tmin\|minpts\|bins\|winsize\|step\|35\|10 s\|2.5\|nneigh\|100" Analysis/Classify_attractors/Analyse_by_Recurrence_Points.m | head -60
```

```
% data-set parameters
stimstart = 30; % 30 s into recording
stimoff = 32.5; % 2.5 s stimulation


%% Analysis parameters
% Gaussian convolution
Qt = 0.01;

% PCA
VarExplained = 0.95;  % 95%

% MT spectrum properties - spikes
params.Fs = 1000; % sampling time-step is 1 ms
params.trialave = 1; % average over all spike-trains
params.fpass = [0 1];
params.err = [2 0.05];

% MT spectrum properties - PC1
paramsPC.Fs = 1/Qt; % sampling time-step is 10 ms for convolved functions
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && grep -n "0.0001\|0.0005\|2\*pi\|exp(\|patch\|fill(" Figures/Figure_LinearDynamics.m | head; echo ---; grep -n "theta\|blnSame" Analysis/Classify_attractors/Are_jumps_perturbations_or_transitions2.m | head -20; echo ---; grep -n "nperm\|Nperm\|perm\|tail\|sign" Analysis/Classify_attractors/Does_Oscillation_Period_Change.m | head; echo ---; grep -n "dRate\|dPart\|delta\|pairs\|\[1 2\]\|corr" Analysis/Classify_attractors/What_is_Participation.m | head -40
```

```
96:ptch = fill([0 2.5 2.5 0],[0.02 0.02 0 0],stimcolor);
98:set(gca,'Layer','top') % esnure that the axes are on top, so the patch objects don't overlap
114:ptch = fill([0 2.5 2.5 0],[0.005 0.005 -0.02 -0.02],stimcolor);
116:set(gca,'Layer','top') % esnure that the axes are on top, so the patch objects don't overlap
140:xmin = -0.0005; 
145:xmax = 0.01*2*pi/1; % max imaginary eigenvalue: fastest possible rotation we can detect
153:% do patches
154:patchinfo.Vertices = [xmin ymin; abs(xmin) ymin; abs(xmin) ymax; xmin ymax];
155:patchinfo.Faces = [1 2 3 4];
156:patchinfo.FaceColor = [0.7 0.7 0.7];
---
16:jumppars.theta = 0.2;  % threshold for a different attractor
24:Summary.blnSame = [];   % same or different attractor?
88:               Summary.blnSame = [Summary.blnSame; Summary.pAfter(end) > jumppars.theta];
129:            Summary.blnSame = [Summary.blnSame; nan];
---
---
14:% correlation between participation and firing rate
19:        [PartContribution(iPrep).rRatePart(iProg),PartContribution(iPrep).pRatePart(iProg)] = corr(Coeffs(iPrep).normWMax(iProg,:)',PartContribution(iPrep).rates(iProg,:)'); 
23: % correlation between change in participation and change in firing rate
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && sed -n 120,175p Figures/Figure_LinearDynamics.m; grep -n "2\*pi\|exp" Figures/Figure_LinearDynamics.m; echo ---; grep -n "WeightedCorr\|1e\|0000" Analysis/Classify_attractors/Does_Oscillation_Period_Change.m; grep -n "nargin\|for\|perm\|tail\|>=\|<=" Functions/WeightedCorrelation.m | head -20
```

```
set(hE,'Markersize',2,'Color',prep_Cmap(ixExample,:));
axis([0 90 -0.02 0.005])
xlabel('Time (s)','FontSize',fontsize)
ylabel('Real Eig.','FontSize',fontsize)
set(gca,'FontName','Helvetica','FontSize',fontsize);
set(gca,'TickDir','out','LineWidth',axlinewidth,'Box','off');

print -depsc FigLinDyn_EigR_timeseries
% exportPPTfig(gcf,'EigR_timeseries',[10 15 6 3])

%% b: summary panel: plot just eigenvalues on plane
load([filepath '/Classify attractors/RecurrenceStats_FilterPts'])

npreps = size(RcrStats,1);
nstims = size(RcrStats,2);

Msize = [2 4 6];  % stim order
sym = 'o';


[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && sed -n 60,125p Analysis/Classify_attractors/Does_Oscillation_Period_Change.m; sed -n 14,30p Functions/WeightedCorrelation.m
```

```
%        actualTime = Data(iPrep).stimbins(RcrPtData(iPrep).ix0 + Ts);   % conversion to time
%     
%        figure
%        plot(actualTime,Egs,'ko')
       
       PeriodChange(iPrep,iProg).blnJump = any(Summary.JumpList(:,1) == iPrep & Summary.JumpList(:,2) == iProg);
       
       % get recurrence density
       tsDensity = RcrPtData(iPrep).Orbit(oscpars.ixT).AllRecurrentPoint.pRecur;

       % get time windows
       ixW = RcrPtData(iPrep).winmids;
       tsW = Data(iPrep).stimbins(ixW);
       
       % find admissible windows
       ixwins = 1:numel(ixW);
       ixWinStrt = 1; ixWinEnd = numel(ixwins);
       if oscpars.blnCoalesce  % then only check after coalescence
            ixC = find(Data(iPrep).stimbins == RcrStats(iPrep,iProg).firstW);
            ixWinStrt = find(ixW == ixC);
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && grep -rn "PeriodChange\|rhoRecur\|Wrho\|Wpval" Figures/*.m | head -30
```

```
Figures/Figure_LinearDynamics.m:295:load([filepath '/Classify attractors/PeriodChange'])
Figures/Figure_LinearDynamics.m:354:%r = [PeriodChange.rho]; p =[PeriodChange.pval];
Figures/Figure_LinearDynamics.m:355:r = [PeriodChange.WrhoRecurAll]; p =[PeriodChange.WpvalRecurAll];  % weighted Spearman's rank
Figures/Figure_LinearDynamics.m:383:r = [PeriodChange.WrhoRecurAll];
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && sed -n 295,420p Figures/Figure_LinearDynamics.m
```

```
load([filepath '/Classify attractors/PeriodChange'])

ixExample = 3;
% get recurrence density
tsDensity = RcrPtData(ixExample).Orbit(statpars.ixT).AllRecurrentPoint.pRecur;

% get time windows
ixW = RcrPtData(ixExample).winmids;
tsW = Data(ixExample).stimbins(ixW);

% find admissible windows
ixwins = 1:numel(ixW);
ixWinStrt = 1; ixWinEnd = numel(ixwins);
if oscpars.blnCoalesce  % then only check after coalescence
    ixC = find(Data(ixExample).stimbins == RcrStats(ixExample,3).firstW);
    ixWinStrt = find(ixW == ixC);
end
if oscpars.blnOff
    ixWinEnd = find(tsDensity > oscpars.pDensity,1,'last');  % final window with P% density of recurrence
end
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && grep -n "shuffle\|randperm\|Hausdorff\|hausdorff\|nShuffle\|max(\|min(\|mean(" Analysis/Classify_attractors/Are_sequential_attractors_the_same.m | head -50
```

```
18:spars.nShuffles = 100;  % 100!
28:% uses Parallel Computing Toolbox do 100 shuffled repeats
85:            ixR = randperm(All(iF).n);
89:                All(iF).ControlSponOnda01(:,iP) = sum(bsxfun(@times,SDF(iR).spkfcn(All(iF).ixts,ixR),All(1).PCAdata.coeffs(:,iP)'),2); % shuffle neuron indices, and project onto da01 axes
90:                All(iF).ControlStimOnda01(:,iP) = sum(bsxfun(@times,SDF(iR).spkfcn(All(iF).ixStim,ixR),All(1).PCAdata.coeffs(:,iP)'),2); % shuffle neuron indices, and project onto da01 axes
96:            ixR = randperm(All(iF).n);
105:   maxD = min([Prep(iR).Prog(:).nPCsVAF80]);  % max comparable dimensions across all three programs
146:    % attractor; compare to min distance to shuffle control
154:        DminCtrl = zeros(numel(fnames),numel(fnames),spars.nShuffles,tmax) + nan; 
177:                cmnStrt = max(srcts(1),targetts(1));
190:                    ix(iN) = find(All(j).Data.stimbins == ptts);  % store index for use in shuffled batch
191:                    Prep(iR).Dmin(i,j,ix(iN)) = min(D); % above diagonal: source -> target
195:                Dalltemp = zeros(spars.nShuffles,numel(srcts));
196:                parfor iB = 1:spars.nShuffles
198:                    % get shuffled target
199:                    ixR = randperm(All(i).n);
202:                        ControlStimOnda01(:,iP) = sum(bsxfun(@times,All(i).SDF.spkfcn(All(i).ixStim,ixR),All(1).PCAdata.coeffs(:,iP)'),2); % shuffle neuron indices, and project onto da01 axes
204:                    ctrltargetPCs = ControlStimOnda01(All(i).ixAdPts,1:Prep(iR).Prog(1).nPCsVAF80); % control source: itself, shuffled
211:                        % DminCtrl(i,j,iB,ix(iN)) = min(Dctrl); % below diagonal: source -> target*
212:                        Dtemp(iN) = min(Dctrl); % below diagonal: source -> target*    
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && grep -n "max\|min\|pdist\|Onset\|onset\|Coal\|firstW" Analysis/Classify_attractors/Initial_Conditions.m | head -40
```

```
1:%% check initial conditions at stimulation onset
86:    TimeToCoalesce = [RcrStats(iPrep,:).firstW] - pars.stimstart;  % seconds to reach coalscence compared to min possible time we can measure
89:        ixP = Prep(iPrep).PIdx(iStim).ts; ixP = ixP(1:round(TimeToCoalesce(iStim)/dt));  % set of admissible points within projection
93:            ixP = Prep(iPrep).PIdx(j).ts;  ixP = ixP(1:round(TimeToCoalesce(j)/dt));
95:            IC(iPrep).sponD(j,iStim) = sqrt(sum((srcPCs(1,:) - targetPCs(1,:)).^2));  % distance at onset of stim
99:                D = sqrt(sum(bsxfun(@minus,targetPCs,pt0).^2,2)); % Euclidean distance to all points within time radius
100:                Dmax(iStim,j,iN) = max(D); % max distance from this point to the other trajectory
102:            IC(iPrep).stimDmax(j,iStim) = max(squeeze(Dmax(iStim,j,:))); % max of all max distnaces
108:% correlate spontaneous distance and max evoked distance
112:allDmax = [];
115:    Dmax = IC(iPrep).stimDmax(IC(iPrep).stimDmax > 0);
116:    plot(Dspon,Dmax,'o','MarkerFaceColor',cmap(iPrep,:),'MarkerEdgeColor','none','MarkerSize',5);
119:    allDmax = [allDmax; Dmax];
140:allDistances = [allSpon allDmax allHdist];
142:LinkedUnivariateScatterPlots(gca,1:3,[allSpon allDmax allHdist],[0.7 0.7 0.7]);
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && sed -n 1,90p Analysis/Classify_attractors/Initial_Conditions.m | grep -n "load\|coeff\|Common\|PCA\|nPC\|Hauss"
```

```
19:%% load and get rates
22:% for each program: find its spike file (loop over da01 etc) - load
31:    load(['../' fnames{iStim} '_DataProperties_FunctionAndWindowSize.mat'],'FileTable')
35:        load([spikepath FileTable{iPrep}]);
79:%% load common-axes PCA, and get distances
80:load('RecurrenceManifoldStats_CommonAxes_AllPreps','Prep','spars') 
81:load('RecurrenceStats_FilterPts')
90:        targetPCs = Prep(iPrep).PCprojU(ixP,1:Prep(iPrep).PCA.nPCs);
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && grep -n "iterateoutliers\|3\*\|nSD\|thresh\|maxDMaxP\|dMaxP\|> \|>=\|VarExplained\|prctVar" Analysis/Classify_attractors/Quantifying_Participation_by_PCA_Contribution.m | head -40
```

```
10:spars.VarExplained = 0.8;  % just get it to work....
42:    conSDF = []; pre = 0;
47:       All(iF).ixStim = find(Data(iR).bins >= spars.stimstart);
50:       conSDF = [conSDF; SDF(iR).spkfcn(All(iF).ixStim,:)];
59:       % Coeffs(iR).nPCs(iF) = find(cumsum(PCAdata(iR).eigvalues./sum(PCAdata(iR).eigvalues)) >= spars.VarExplained,1,'first');
83:%     mS = round(max(max(conSDF)))+1;
85:%     subplot(nfiles,1,iR),plot(conSDF(:,Coeffs(iR).Rank(1:2))); hold on
89:%     % subplot(nfiles,2,iR+nfiles),plot(conSDF(:,ix(3:10)))
92:%     subplot(nfiles,1,iR),plot(conSDF(:,Coeffs(iR).Rank(end-1:end))); hold on
122:    Coeffs(iR).dMaxP = [(Coeffs(iR).normWMax(1,:) - Coeffs(iR).normWMax(2,:))' (Coeffs(iR).normWMax(2,:) - Coeffs(iR).normWMax(3,:))' (Coeffs(iR).normWMax(1,:) - Coeffs(iR).normWMax(3,:))']; 
123:    Coeffs(iR).maxDMaxP = max(abs(Coeffs(iR).dMaxP(:,1:2)),[],2);  % largest jump of each neuron between consecutive programs
126:    Coeffs(iR).NmaxDmaxP = Coeffs(iR).maxDMaxP ./ Coeffs(iR).HighMaxP; % scale of change compared to maximum...
129:    tbl = table(Coeffs(iR).HighMaxP,Coeffs(iR).maxDMaxP ,'VariableNames',{'Max_Pi','Max_DPi'});
139:    plot(Coeffs(iR).HighMaxP,Coeffs(iR).maxDMaxP,'k.')
154:    [Varsrt,Varrnk] = sort(Coeffs(iR).maxDMaxP,'descend'); % from most to least variable
155:    mS = round(max(max(conSDF)))+1;
157:    subplot(nfiles,1,iR),plot(conSDF(:,Varrnk(1:2))); hold on
161:    subplot(nfiles,1,iR),plot(conSDF(:,Varrnk(end-1:end))); hold on
166:%     plot(conSDF(:,20)); hold on
172:%             %H1 = hilbert(conSDF(Prep(iR).PIdx(iF).ts,Coeffs(iR).Rank(iM)) - mean(conSDF(Prep(iR).PIdx(iF).ts,Coeffs(iR).Rank(iM))));
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && grep -n "HaussD\|dMaxP\|Hellinger\|hell\|fitlm\|< 1\|bins\|robust" Analysis/Classify_attractors/RobustnessOfAttractor_to_single_neuron_variability.m | head -30
```

```
22:Robust.allH = []; Robust.allDpart = []; Robust.allHaussD = []; Robust.allHraw = []; Robust.allPchange = []; Robust.allMDensity = []; Robust.allHD_Diff = [];
25:pbins = 0:0.05:1; % bins for histogram
27:ixpairs = [1,2; 2,3; 1,3];  % pairs stored sequentially in e.g. Coeffs.dMaxP field
35:        pbinsRaw = 0:0.05:max(max(Coeffs(iPrep).sumWProg));
40:                p1 = hist(Coeffs(iPrep).normWMax(i,:),pbins); p1 = p1 ./sum(p1);
41:                p2 = hist(Coeffs(iPrep).normWMax(j,:),pbins); p2 = p2 ./sum(p2);               
45:                p1 = hist(Coeffs(iPrep).sumWProg(i,:),pbinsRaw); p1 = p1 ./sum(p1);
46:                p2 = hist(Coeffs(iPrep).sumWProg(j,:),pbinsRaw); p2 = p2 ./sum(p2);               
56:            Pchange(ixpairs(i,1),ixpairs(i,2)) = sum(Coeffs(iPrep).dMaxP(:,i) >= Coeffs(iPrep).MinVarPart) ./ numel(Coeffs(iPrep).Rank); 
65:        Robust.allHaussD = [Robust.allHaussD; nonzeros(Prep(iPrep).HaussD)];
67:        ctrl = mean(Prep(iPrep).HaussDCtrl,3);
68:        Robust.allHD_Diff = [Robust.allHD_Diff; nonzeros(Prep(iPrep).HaussD) - nonzeros(ctrl)];  % difference between (mean) control and data distance
69:        Robust.allHD_MagCtrl = [Robust.allHD_MagCtrl; nonzeros(Prep(iPrep).HaussD) ./nonzeros(ctrl)];  % expressed as magnitude
76:tbl = table(Robust.allH,Robust.allHaussD,'VariableNames',{'NormDist','HaussD'});
77:Robust.lm_NormDist =fitlm(tbl,'linear');  % normalised participation distribution
79:tbl = table(Robust.allHraw,Robust.allHaussD,'VariableNames',{'RawDist','HaussD'});
80:Robust.lm_RawDist =fitlm(tbl,'linear');
82:tbl = table(Robust.allDpart,Robust.allHaussD,'VariableNames',{'ChangePart','HaussD'});
83:Robust.lm_ChangePart =fitlm(tbl,'linear');
84:Robust.lm_ChangePartRob =fitlm(tbl,'linear','RobustOpts','bisquare');
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; grep -n "expected" -A40 schemas/claims*.json 2>/dev/null | grep -n "properties\|\"[a-z_]*\": {" | head -30
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
1:104:          "expected": {
10:113-                "items": {
16:119-          "statistics": {
20:123-            "items": {
24:127-          "criterion": {
28:131-          "depends_on": {
31:134-            "items": {
36:139-          "data": {
45:148-          "where": {
53:156-            "not": {
59:245:    "expected": {
66:252-      "properties": {
67:253-        "quantity": {
70:256-        "value": {
73:259-        "tolerance": {
77:263-        "unit": {
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 240,330p schemas/claims.schema.json
```

```
}
      }
    }
  },
  "$defs": {
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
[... 71 more lines not kept]
```

**Agent**

Checker passes. My review of the claims against the paper and code (cloned at e5f28e9) found a few concrete problems. Applying fixes now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-apl-1/10.7554-elife.27342.yaml",
 "old_string": "    quantity: frequency of the dominant peak of the mean post-stimulation spectrum\n    value: 0.1",
 "new_string": "    quantity: upper bound on the frequency of the dominant peak of the mean post-stimulation\n      spectrum (the paper gives a bound, at or below 0.1 Hz, not a point value)\n    value: 0.1"
}
```

```
The file claims/crcns-apl-1/10.7554-elife.27342.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-apl-1/10.7554-elife.27342.yaml",
 "old_string": "    reading, more than half of the 30 dominant periods lie in 9 to 16.5 s and at least one does\n    not (\"not all\").",
 "new_string": "    reading, more than half of the 30 dominant periods lie in 9 to 16.5 s and at least one does\n    not (\"not all\"; the paper does not count \"many\", so more than half is a rule fixed here)."
}
```

```
The file claims/crcns-apl-1/10.7554-elife.27342.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-apl-1/10.7554-elife.27342.yaml",
 "old_string": "    between the pair's point sets; control, the Hausdorff distance after shuffling the neurons of\n    one program, 100 shuffles, mean taken. The point sets are (a) the recurrent points (Methods)\n    or (b) all points of runs of 5 s windows with at least 90% recurrence, from the later of the\n    two programs' first such point (the code). Reproduced when, under a reading, at least 25 of\n    the 30 pairs have a distance below their control mean; the pairs that fail are named against\n    those of preparation 4.",
 "new_string": "    between the pair's point sets; control, as the Methods, max{min d(A,B*), min d(B,A*)}, with\n    A* and B* the programs after shuffling the assignment of time series to neurons and projecting\n    onto the same axes, 100 shuffles, mean taken. The point sets are (a) the recurrent points\n    (Methods) or (b) all points of runs of 5 s windows with at least 90% recurrence, from the\n    later of the two programs' first such point (the code). Reproduced when, under a reading, at\n    least 26 of the 30 pairs (28 less its tolerance of 2.8) have a distance below their control\n    mean; the pairs that fail are named against those of preparation 4."
}
```

```
The file claims/crcns-apl-1/10.7554-elife.27342.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-apl-1/10.7554-elife.27342.yaml",
 "old_string": "    which keeps the PCs whose cumulative variance is at most 80%). Reproduced when at least 25 of\n    the 30 pairs have a distance below their control mean.",
 "new_string": "    which keeps the PCs whose cumulative variance is at most 80%). The legend says the results\n    are the same as Figure 3C, where 28 of 30 pairs pass, so reproduced when at least 26 of the 30\n    pairs have a distance below their control mean, as claim fig3c-same-manifold."
}
```

```
The file claims/crcns-apl-1/10.7554-elife.27342.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-apl-1/10.7554-elife.27342.yaml",
 "old_string": "    that of its first program, or the larger of its two programs' controls. Reproduced when, under\n    a reading, at least 25 of the 30 pairs have a data correlation above their control.",
 "new_string": "    that of its first program, or the larger of its two programs' controls. Reproduced when, under\n    a reading, at least 26 of the 30 pairs (28 less its tolerance of 2.8) have a data correlation\n    above their control."
}
```

```
The file claims/crcns-apl-1/10.7554-elife.27342.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-apl-1/10.7554-elife.27342.yaml",
 "old_string": "    is a stable spiral and each of the 10 preparations has at least two of its three responses in\n    the stable spiral region; partially",
 "new_string": "    is a stable spiral and each of the 10 preparations has at least two of its three responses in\n    the stable spiral region (the paper does not count responses per preparation; this rule is\n    fixed here); partially"
}
```

```
The file claims/crcns-apl-1/10.7554-elife.27342.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-apl-1/10.7554-elife.27342.yaml",
 "old_string": "  statistics:\n  - test: weighted Spearman's rank correlation, permutation test\n    p: 0.01\n    p_relation: \"<\"\n    n: 30 responses, 31 to 72 local estimates each\n  expected:",
 "new_string": "  expected:"
}
```

```
The file claims/crcns-apl-1/10.7554-elife.27342.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-apl-1/10.7554-elife.27342.yaml",
 "old_string": "    250 ms) is a variant. The paper's 173",
 "new_string": "    250 ms) is a variant, and so are histories up to 100 ms, as the Results say (\"recent history\n    (up to 100 ms)\"), against the Methods' 50 to 200 ms. The paper's 173"
}
```

```
The file claims/crcns-apl-1/10.7554-elife.27342.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-apl-1/10.7554-elife.27342.yaml",
 "old_string": "    \"close to 1\"; 0.9 is taken here. Reproduced when no neuron has a maximum of 0.9 or more in two\n    programs of its preparation; the largest values are reported.",
 "new_string": "    \"close to 1\"; 0.9 is taken here. Reproduced when no neuron has a maximum of 0.9 or more in any\n    program (no neuron close to 1 at any delay) and hence none in two programs of its preparation\n    (no consistent locking); the largest values, and how many neurons reach 0.9 in one program\n    and in two, are reported."
}
```

```
The file claims/crcns-apl-1/10.7554-elife.27342.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n '"checks"' -A30 schemas/claims.schema.json | head -45
```

```
202:    "checks": {
203-      "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
204-      "type": "array",
205-      "items": {
206-        "type": "object",
207-        "additionalProperties": false,
208-        "required": [
209-          "date",
210-          "kind",
211-          "ready"
212-        ],
213-        "properties": {
214-          "date": {
215-            "type": "string",
216-            "format": "date"
217-          },
218-          "kind": {
219-            "enum": [
220-              "agent",
221-              "person"
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> claims/crcns-apl-1/10.7554-elife.27342.yaml <<'EOF'
checks:
- date: '2026-11-08'
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig5b-period-changes, removed the statistics entry (permutation test, p < 0.01); in the Figure 5B legend p < 0.01 only marks which responses count as changing, a threshold used to count responses, not a result. The criterion keeps it.
  - fig1d-slow-oscillation, the expected quantity now says 0.1 Hz is an upper bound (the paper's "≤ 0.1 Hz"), not a point value, so it agrees with the criterion.
  - fig3c-same-manifold, the control described as "shuffling the neurons of one program" now follows the Methods, max{min d(A,B*), min d(B,A*)} with both programs shuffled in turn, as Are_sequential_attractors_the_same.m also does.
  - fig3c-same-manifold and fig3f-pairwise-similarity, the count required went from 25 to 26 of 30, so the criterion matches the expected 28 with tolerance 2.8 (25 lies outside it).
  - fig3s1a-common-axes, the count required went from 25 to 26 of 30, as the legend says the results are the same as Figure 3C.
  - fig2ef-periodic-recurrence and fig4bc-stable-spiral, the criteria now say their counting rules ("more than half" for "many"; two of three responses per preparation) are fixed here, as the paper does not count them.
  - fig6d-decode-p10, added histories up to 100 ms as a variant; the Results say "recent history (up to 100 ms)", the Methods 50 to 200 ms.
  - fig6s1-no-p10-motorneurons, the criterion tested only consistent locking in two programs; the statement and legend also say no neuron comes close to 1 at any delay, so it now requires no neuron at 0.9 or more in any program.
  - Open, fig2b-dimensions and fig6s2-dimensions-p10, the paper gives 4 to 8 dimensions for all 30 responses but 3 to 5 for the nine P10 recordings; the two cannot both hold for every response, which "generally" allows. Both claims stand as written.
  - Open, the Gaussian SD; the extracted text reads median ISI / 12, and no PDF of the paper was supplied to check for a lost square root. The criteria name both readings and the code's.
EOF
python tools/claims_check.py claims/crcns-apl-1/10.7554-elife.27342.yaml paper/10.7554-elife.27342.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file is ready for an attempt. I made eight changes and left two points open, and a `checks` entry at the end of the file records all of them.

**Checker result** (after my changes): `30 claims, 30 quotes, 0 statistical values, 0 problems`. Before my changes it read the same, except for 1 statistical value, which I removed (see fig5b below).

I checked the claims against the full text and against the paper's code (mdhumphries/AplysiaAttractorAnalysis, commit e5f28e9, cloned to a temporary folder). Most of the code details the claims cite are accurate: the kernel and PCA settings, the recurrence parameters, the eigenvalue bands and period formula, the permutation and weighting code, the 0.2 threshold for returning to the same manifold, the noise-model threshold, and the mismatched pairs in the rate-change analysis.

**Changes, by claim**
- **fig5b-period-changes**: removed the statistics entry (p < 0.01). In the Figure 5B legend that p-value only marks which responses count as changing, so it is a counting threshold, not a result. The criterion still uses it.
- **fig1d-slow-oscillation**: the expected quantity now says 0.1 Hz is an upper bound (the paper says "≤ 0.1 Hz"). It was written as a point value, which disagreed with the criterion.
- **fig3c-same-manifold**: the control now follows the Methods formula, max{min d(A,B*), min d(B,A*)}, which shuffles both programs in turn, as the code does. The file had said only one program is shuffled.
- **fig3c-same-manifold, fig3f-pairwise-similarity**: the required count went from 25 to 26 of 30. The expected value is 28 with a tolerance of 2.8, so 25 fell outside it.
- **fig3s1a-common-axes**: also 26 of 30, since the legend says the results are the same as Figure 3C.
- **fig2ef-periodic-recurrence, fig4bc-stable-spiral**: the criteria now say their counting rules are set by the claims file, not the paper ("more than half" for "many"; two of three responses per preparation).
- **fig6d-decode-p10**: added histories up to 100 ms as a variant. The Results say "up to 100 ms", while the Methods say 50 to 200 ms.
- **fig6s1-no-p10-motorneurons**: the criterion only tested consistent locking across two programs. The paper also says no neuron comes close to 1 at any delay, so it now requires that no neuron reaches 0.9 in any program.

**Open**
- **fig2b-dimensions and fig6s2-dimensions-p10**: the paper gives 4 to 8 dimensions for all 30 responses, but 3 to 5 for the nine recordings with P10 activity. The paper's "generally" allows this, so both claims stand as written.
- **Gaussian width**: the extracted text reads median ISI / 12, and with no PDF of the paper I could not check whether a square root was lost. The criteria already list both readings and the code's choice (the median ISI itself).

Nothing was committed or pushed, and only the claims file changed.

## End of run

36 turns, 3 minutes, $1.69 at API prices, result: success.
