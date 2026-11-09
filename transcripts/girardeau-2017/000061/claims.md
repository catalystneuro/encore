# 000061 · claims · run 39470180222

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls claims/001453/ claims/000061/ paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 170
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-10`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. It is written from the pilot attempts
7	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
8	
9	An attempt has three roles, each a separate run with a separate context:
10	
11	- The **reader** reads the paper and writes the claims file: every finding,
12	  and how each is to be tested, taken from the paper. A second reader checks
13	  it against the paper. Readers never see the dandiset's data.
14	- The **author** tests the claims on the dandiset. It reads the paper to
15	  understand the claims, but the claims file binds it: it cannot change a
16	  claim, and it asks a reader for any method detail the file lacks.
17	- The **verifier** checks the author's work and must not be the author.
18	
19	So every claim and its method are fixed from the paper before anyone analyses
20	the data, and no method is chosen by the agent that runs the analysis.
[... 150 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000061/10.1038-nn.4637.yaml"
}
```

```
1	# Claims for Girardeau, Inema & Buzsaki (2017) on dandiset 000061.
2	# Source: the abstract only (PubMed 28892057). The article is not open access: it is not in
3	# PubMed Central, Europe PMC lists no full text, and the HAL record (hal-03963137) holds metadata
4	# only. So every claim is at the level of a sentence of the abstract, no claim has a reported
5	# number, and every method choice below is fixed here, as a common choice, before the analysis.
6	# Quotes from the abstract added 2026-10-19 where it states the finding; the rest are marked
7	# inferred (no open full text).
8	#
9	# When these criteria were written, the author had seen the data check only: the file list, the
10	# metadata, the units' location labels and counts per session, which files lack units, sleep
11	# states or ripple events, the epoch tables, and the reward and air-puff events, including the
12	# laps built from alternating rewards, which direction holds the puffs, and the median lap
13	# durations per direction in the pre-run, run and post-run epochs. No reactivation, ripple
14	# modulation or pattern weight had been computed.
15	#
16	# Method choices fixed here (the Methods were not available):
17	# - Units. Hippocampus is the label `hpc` or `HIP`; BLA is the label `bla` or `BLA` (case is
18	#   ignored). A session is used when it has sleep states, ripple events, a sleep epoch before and
19	#   one after the run, and at least 5 hippocampal and 5 BLA units that fire at 0.1 Hz or more in
20	#   the run epoch. Units are not matched across sessions.
[... 186 more lines not kept]
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
wc -l paper/10.1038-nn.4637.txt; head -c 3000 paper/10.1038-nn.4637.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4637.txt",
 "offset": 50,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4637.txt",
 "offset": 750,
 "limit": 1080
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, Online Methods and supplement are all present. Next I'll read the code the paper links.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone --depth 1 --filter=blob:none --sparse https://github.com/buzsakilab/papers.git 2>&1 | tail -2; cd papers && git sparse-checkout set GGirardeauBLAHpcInteractions-Package 2>&1|tail -2; git log -1 --format=%H; find GGirardeauBLAHpcInteractions-Package -type f | head -100
```

```
Cloning into 'papers'...
cdcec89f8d1f5cf11f407f82827f9af44405c5b7
find: ‘GGirardeauBLAHpcInteractions-Package’: No such file or directory
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers && git ls-tree -d --name-only HEAD | head -50
```

```
GGirardeau-BLAHpcInteractions-Package
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers && git sparse-checkout set GGirardeau-BLAHpcInteractions-Package && find GGirardeau-BLAHpcInteractions-Package -type f | sed 's/^/  /' | head -200; find GGirardeau-BLAHpcInteractions-Package -type f | wc -l
```

```
GGirardeau-BLAHpcInteractions-Package/Reactivations/ReplayInTime_Plot.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ReplayInTime_LapTypes_Plot.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ReplayInTime_LapTypes_All.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ReplayInTime_LapTypes.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ReplayInTime_All.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ReplayInTime.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ExplainedVariance_Ultimate_IntraStruct.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ExplainedVariance_Ultimate.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ExplainedVariance_PrePostCorr_Ultimate.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ExplainedVariance_PooledCorr_Groups.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ExplainedVariance_PooledCorr.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ExplainedVarianceMean_Ultimate.m
  GGirardeau-BLAHpcInteractions-Package/Reactivations/ExplainedVarianceMean_CrossStructureStats.m
  GGirardeau-BLAHpcInteractions-Package/Physiology/StatesFiringRates.m
  GGirardeau-BLAHpcInteractions-Package/Physiology/RippleRatePrePost_All.m
  GGirardeau-BLAHpcInteractions-Package/Physiology/RippleRatePrePost.m
  GGirardeau-BLAHpcInteractions-Package/Physiology/RippleMod_PrePost.m
  GGirardeau-BLAHpcInteractions-Package/Physiology/PrePostFiringRates_Plot.m
  GGirardeau-BLAHpcInteractions-Package/Physiology/PrePostFiringRates_All.m
  GGirardeau-BLAHpcInteractions-Package/Physiology/PrePostFiringRates.m
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package && wc -l */*.m | sort -n | tail -65
```

```
8 Miscellaneous/QuantileGroups.m
    14 Miscellaneous/GetAmygdalaRatioforStateEditor.m
    15 Behavior/RunIntervals.m
    19 Miscellaneous/AxesInsetBars.m
    21 Miscellaneous/GetCleanPositions.m
    23 Reactivations/ExplainedVarianceMean_CrossStructureStats.m
    24 Miscellaneous/SaveAirpuffEvents.m
    30 Miscellaneous/CreateCellIndex.m
    31 Behavior/PlotLaps.m
    32 CellClassification/FinalType.m
    37 Behavior/CheckLaps.m
    38 Physiology/PoissonRippleModAll.m
    40 Behavior/LapType.m
    40 Behavior/Performance.m
    42 Miscellaneous/FindRunEpochs.m
    42 Physiology/PrePostFiringRates_All.m
    44 Behavior/Performance_All.m
    45 Physiology/RippleRatePrePost_All.m
    51 Behavior/BehavioralMeasuresAll.m
    56 Miscellaneous/SaveRewardEvents.m
[... 43 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations/ReplayInTime_LapTypes.m"
}
```

```
1	function [HPtrains,STtrains,R,meanR,tb] = ReplayInTime_LapTypes (session,structure,pre,post,varargin)
2	
3	%ReplayInTime_LapTypes - Calculates reactivation strength of the airpuff vs the safe trajectory correlation matrices in time during pre and post-sleep epochs for each session.
4	%
5	%  USAGE
6	%
7	%    [[HPtrains,STtrains,R,meanR,tb] = ReplayInTime (session,structure, pre, post, <options>)
8	%
9	%    session		path to session
10	%    structure          structure name (ex : 'BLA')
11	%    pre                subsession number for presleep
12	%    post               subsession number for postsleep
13	%    <options>          list of property-value pairs, see below
14	%
15	%    =========================================================================
16	%     Properties            Values
17	%    -------------------------------------------------------------------------
18	%     'binsize'	        binsize for spike trains
19	%     'savefig'     	save figure : 'on','off'(default)
20	%     'savevar'		save variable
[... 238 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations/ReplayInTime_LapTypes_Plot.m"
}
```

```
1	function ReplayInTime_LapTypes_Plot (struc,binsize,zsc,window,ctype,varargin)
2	
3	%ReplayInTime_LapTypes_Plot - PLots Peri-ripple reactivation strength for airpuff and safe RUN trajectories.
4	%
5	%  USAGE
6	%
7	%    ReplayInTime_Plot (struc,binsize,zsc,window,ctype,varargin)
8	%
9	%    struc              structure name (ex : 'BLA')
10	%    binsize            binsize
11	%    zsc                zscore 'on'/'off'
12	%    window             periripple window
13	%    ctype              cell type 'pyr', 'all'
14	%
15	%    =========================================================================
16	%     Properties            Values
17	%    -------------------------------------------------------------------------
18	%     'stattype'	'mean' (default) or 'median'
19	%    =========================================================================
20	%
[... 148 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations/ReplayInTime_LapTypes_All.m"
}
```

```
1	function [PeriRippleReplay,Mean,Sem,tb,centermeans,ratsess] = ReplayInTime_LapTypes_All(struc,binsize,zsc,window,ctype,varargin)
2	
3	%ReplayInTime_LapTypes_All - Reactivation strength of the safe vs airpuff RUNS in time during pre and post-sleep epochs across rats and sessions
4	%
5	%  USAGE
6	%
7	%   [PeriRippleReplay,Ratios,Mean,Sem,tb,centermeans,ratsess] = ReplayInTime_All(struc,binsize,zsc,window,ctype,varargin)
8	%
9	%    struc              structure name (ex : 'BLA')
10	%    binsize            binsize
11	%    zsc                zscore 'on'/'off'
12	%    window             periripple window
13	%    ctype              cell type 'pyr', 'all'
14	%    <options>
15	%
16	%    =========================================================================
17	%     Properties            Values
18	%    -------------------------------------------------------------------------
19	%     'stattype'	'mean'(default), 'median'
20	%    =========================================================================
[... 125 more lines not kept]
```

**Agent**

The paper's code (buzsakilab/papers, commit cdcec89) holds the per-session reactivation scripts. I'm reading the whole-run version and the ripple-modulation code next.

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && sed -n 90,470p ReplayInTime.m | grep -v "^\s*%" | grep -v "^\s*$"
```

```
end
end
load('/media/Data-01/All-Rats/sessionindexing.mat');
load('/media/Data-01/All-Rats/AllRats-FinalType.mat');
ratsess=ratsessionindex(strcmp([session '/'],xmlpath),1:2); %[rat session]
cd(session);
xml=session(end-13:end);
SetCurrentSession('filename',[session '/' xml]);
load('States.mat');
load('runintervals.mat');
load(['/media/Data-01/All-Rats/Structures/' structure '.mat']);
load(['/media/Data-01/All-Rats/Structures/Hpc.mat']);
struc=eval(structure);
presleep=RunIntervals(pre);
postsleep=RunIntervals(post);
run=runintervals(2,:);
endlimit=runintervals(end,end);
limits=[0 endlimit];
rip=GetRippleEvents;
rip=rip(:,2);
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && sed -n 70,230p ReplayInTime_All.m | grep -v "^\s*$"; echo ----; sed -n 60,184p ReplayInTime_Plot.m | grep -v "^\s*$" | grep -iE "signrank|wind|tail|ranksum|size|>="
```

```
end
load('/media/Data-01/All-Rats/sessionindexing.mat');
PeriRippleReplay.pre.cross=[];
PeriRippleReplay.post.cross=[];
PeriRippleReplay.pre.hpc=[];
PeriRippleReplay.post.hpc=[];
PeriRippleReplay.pre.struc=[];
PeriRippleReplay.post.struc=[];
Ratios.Pre=[];
Ratios.Post=[];
ratsess=[];
for i=1:size(ratsessionindex)
  currentsession=xmlpath{i}
  cd(currentsession);
  xml=currentsession(end-14:end-1);
  if exist ([xml '-ReplayInTime-' struc '-binsize' num2str(binsize) '-zsc' zsc '-window' int2str(window) '-ctype-' ctype '.mat'])==2;
    load([xml '-ReplayInTime-' struc '-binsize' num2str(binsize) '-zsc' zsc '-window' int2str(window) '-ctype-' ctype '.mat']);
    load([xml '-ExplainedVariance-' struc '.mat'],'CorrMatrix');
    if exist ('BehavioralMeasures.mat')==2;
      load('BehavioralMeasures.mat');
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && sed -n 1,646p ExplainedVariance_Ultimate.m | grep -v "^\s*$" | grep -v "^\s*%" | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|f[0-9]=|ylim|xlim|set\()" | head -330
```

```
<persisted-output>
Output too large (33.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/405da440-72bd-4540-addf-b94971f65d09/tool-results/bp2552259.txt

Preview (first 2KB):
function [EV,REV,CorrMatrix] = ExplainedVariance_Ultimate(session,structure,pre,post,varargin)
binsize = 0.05;
savefig = 'off';
savevar = 'off';
if nargin < 4,
  error('Incorrect number of parameters (type ''help <a href="matlab:help FunctionName">FunctionName</a>'' for details).');
end
if mod(length(varargin),2) ~= 0,
  error('Incorrect number of parameters  (type ''help <a href="matlab:help FunctionName">FunctionName</a>'' for details).');
end
for i = 1:2:length(varargin),
	if ~ischar(varargin{i}),
		error(['Parameter ' num2str(i) ' is not a property (type ''help <a href="matlab:help FunctionName">FunctionName</a>'' for details).']);
	end
	switch(lower(varargin{i})),
		case 'type',
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && grep -nE "corrcoef|EV\.|REV\.|1200|3600|>=|nancorr|corr\(|Restrict\(bins|InIntervals|zscore|isnan|ripplemod|sws|rem\b|REM" ExplainedVariance_Ultimate.m | grep -v "^\S*\s*%" | head -120
```

```
75:		case 'ripplemod',
76:			ripplemod = (varargin{i+1});
104:swsripples=Restrict(ripples,sws);
105:swsrippleintervals=[swsripples(:,1) swsripples(:,2)];
107:swsrippleintervals_pre=Restrict(swsrippleintervals,presleep);
108:swsrippleintervals_post=Restrict(swsrippleintervals,postsleep);
142:HPspikes(HPspikes(:,1)>=limits(2),:)=[];
143:STspikes(STspikes(:,1)>=limits(2),:)=[];
149:nbins20min=1200/binsize;
151:is.pre.sws=InIntervals(bins,presleep)&InIntervals(bins,sws);
152:is.post.sws=InIntervals(bins,postsleep)&InIntervals(bins,sws);
153:is.pre.rem=InIntervals(bins,presleep)&InIntervals(bins,Rem);
154:is.post.rem=InIntervals(bins,postsleep)&InIntervals(bins,Rem);
161:duration.pre.sws=sum(is.pre.sws)*binsize;
162:duration.post.sws=sum(is.post.sws)*binsize;
163:postswsHPtrains=HPtrains(is.post.sws,:);
164:postswsSTtrains=STtrains(is.post.sws,:);
167:    [CorrMatrix.pre.sws.all.Rall, PvalMatrix.pre.sws.all.Rall]=corr(HPtrains(is.pre.sws,:),STtrains(is.pre.sws,:));
168:    [CorrMatrix.post.sws.all.Rall, PvalMatrix.post.sws.all.Rall]=corr(HPtrains(is.post.sws,:),STtrains(is.post.sws,:));
169:    [CorrMatrix.post_1.sws.all.Rall, PvalMatrix.post_1.sws.all.Rall]=corr(postswsHPtrains(1:nbins20min,:),postswsSTtrains(1:nbins20min,:));
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && sed -n 109,160p ExplainedVariance_Ultimate.m; grep -nE "is\.mod|run\.(all|pyr)\.Rall\b.*=corr|EV\.sws|REV\.sws|function|\^2|sqrt" ExplainedVariance_Ultimate.m | head -40
```

```
% Get hippocampal cells (pyr/all) + index
HPshanks=Hpc(ismember(Hpc(:,1:2),ratsess,'rows'),3);
HPcells=finalType(ismember(finalType(:,1:2),ratsess,'rows')&ismember(finalType(:,3),HPshanks),3:4);
HPspikes=GetSpikeTimes(HPcells,'output','total');
HPindex=unique(HPspikes(:,2:4),'rows');
HPtype=finalType(ismember(finalType(:,1:2),ratsess,'rows')&ismember(finalType(:,3),HPshanks),5); % cell type 1/2
HPispyr=HPtype==1;

% Get all structure spikes + index + finaltype and modulation
STshanks=struc(ismember(struc(:,1:2),ratsess,'rows'),3);
STcells=finalType(ismember(finalType(:,1:2),ratsess,'rows')&ismember(finalType(:,3),STshanks),3:4); %finaltype jsut used as index here
STtype=finalType(ismember(finalType(:,1:2),ratsess,'rows')&ismember(finalType(:,3),STshanks),5);% FinalType for structure cells
STispyr=STtype==1;

if ~isempty(STcells)
  STspikes=GetSpikeTimes(STcells,'output','total');
  STindex=unique(STspikes(:,2:4),'rows');
else
  warning('No cells in target structure : exit function')
  return
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && sed -n 330,646p ExplainedVariance_Ultimate.m | grep -v "^\s*$" | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|f[0-9]+=|ylim|xlim|set\(|bar|suptitle)" | grep -vE "Rnomod|Rmod" | head -120
```

```
% Ripple mod vs Non ripplemod
  %%%%%% Pyramidals Only
    % All Ripple mod
    [CorrMatrix.run.pyr.Rall, PvalMatrix.run.pyr.Rall]=corr(HPtrains(is.run,HPispyr),STtrains(is.run,STispyr));   
    % Ripple mod vs Non ripplemod
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Correlation Coeffs.
%%%%%%%%%%%%% REM %%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  %%%% All cell types
    %%%% All Ripple modulation types
    r_runpost.rem.all.Rall=corrcoef(CorrMatrix.post.rem.all.Rall,CorrMatrix.run.all.Rall,'rows','complete');r_runpost.rem.all.Rall=r_runpost.rem.all.Rall(1,2);
    r_runpre.rem.all.Rall=corrcoef(CorrMatrix.pre.rem.all.Rall,CorrMatrix.run.all.Rall,'rows','complete');r_runpre.rem.all.Rall=r_runpre.rem.all.Rall(1,2);
    r_prepost.rem.all.Rall=corrcoef(CorrMatrix.pre.rem.all.Rall,CorrMatrix.post.rem.all.Rall,'rows','complete');r_prepost.rem.all.Rall=r_prepost.rem.all.Rall(1,2);
    EV.rem.all.Rall=((r_runpost.rem.all.Rall-r_runpre.rem.all.Rall*r_prepost.rem.all.Rall)/sqrt((1-r_runpre.rem.all.Rall^2)*(1-r_prepost.rem.all.Rall^2)))^2;
    REV.rem.all.Rall=((r_runpre.rem.all.Rall-r_runpost.rem.all.Rall*r_prepost.rem.all.Rall)/sqrt((1-r_runpost.rem.all.Rall^2)*(1-r_prepost.rem.all.Rall^2)))^2;
    %%%% Ripple mod vs nonripple mod
      %%% Ripple mod all
      %%% Ripple No mod
  %%%% Pyr Only
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && grep -n "is.run" ExplainedVariance_Ultimate.m | head -5; echo ---; grep -v "^\s*$" ExplainedVarianceMean_Ultimate.m | grep -nE "signrank|ranksum|>=|kruskal|size\(|numel|length\(|EV\.sws|post1|isnan|nshank|shank|exclude" | head -60
```

```
326:is.run=InIntervals(bins,runintervals(2,:));
329:    [CorrMatrix.run.all.Rall, PvalMatrix.run.all.Rall]=corr(HPtrains(is.run,:),STtrains(is.run,:));   
331:    [CorrMatrix.run.all.Rmod, PvalMatrix.run.all.Rmod]=corr(HPtrains(is.run,:),STtrains(is.run,is.mod));   
332:    [CorrMatrix.run.all.Rnomod, PvalMatrix.run.all.Rnomod]=corr(HPtrains(is.run,:),STtrains(is.run,~is.mod)); 
336:    [CorrMatrix.run.pyr.Rall, PvalMatrix.run.pyr.Rall]=corr(HPtrains(is.run,HPispyr),STtrains(is.run,STispyr));   
---
46:if mod(length(varargin),2) ~= 0,
50:for i = 1:2:length(varargin),
66:EVREV.sws.all.Rall=[];
67:EVREV.sws.all.Rmod=[];
68:EVREV.sws.all.Rnomod=[];
78:EVREV.sws.pyr.Rall=[];
79:EVREV.sws.pyr.Rmod=[];
80:EVREV.sws.pyr.Rnomod=[];
112:for i=1:length(xmlpath)
144:  enough.all.Rall=size(CorrMatrix.pre.sws.all.Rall,1)>5&size(CorrMatrix.pre.sws.all.Rall,2)>5;
146:    enough.all.Rmod=size(CorrMatrix.pre.sws.all.Rmod,1)>5&size(CorrMatrix.pre.sws.all.Rmod,2)>5;
151:    enough.pyr.Rall=size(CorrMatrix.pre.sws.pyr.Rall,1)>5&size(CorrMatrix.pre.sws.pyr.Rall,2)>5;
153:      enough.pyr.Rmod=size(CorrMatrix.pre.sws.pyr.Rmod,1)>5&size(CorrMatrix.pre.sws.pyr.Rmod,2)>5;
166:      EVREV.sws.all.Rall=[EVREV.sws.all.Rall; EV.sws.all.Rall REV.sws.all.Rall EV.post1.sws.all.Rall REV.post1.sws.all.Rall EV.post2.sws.all.Rall REV.post2.sws.all.Rall EV.post3.sws.all.Rall REV.post3.sws.all.Rall];    
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && sed -n 112,165p ExplainedVarianceMean_Ultimate.m; grep -n "180\|duration" ExplainedVarianceMean_Ultimate.m | head
```

```
sess.sws.all.Rall=[];
sess.rem.all.Rall=[];
sess.rem.all.Rmod=[];
sess.sws.all.Rmod=[];
sess.rip.all.Rall=[];
sess.rip.all.Rmod=[];
sess.sws.pyr.Rall=[];
sess.rem.pyr.Rall=[];
sess.rem.pyr.Rmod=[];
sess.sws.pyr.Rmod=[];
sess.rip.pyr.Rall=[];
sess.rip.pyr.Rmod=[];

sess.run.all.Rall=[];
sess.run.all.Rmod=[];
sess.run.pyr.Rall=[];
sess.run.pyr.Rmod=[];


for i=1:length(xmlpath)
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Physiology && grep -v "^\s*$" PoissonRippleMod.m | grep -v "^\s*%" | sed -n 30,200p | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|ylim|xlim|set\()"
```

```
pval = varargin{i+1};
		case 'duration'
		      duration = varargin{i+1};
		case 'smooth'
		      smooth = varargin{i+1};
		case 'binSize'
		      binSize = varargin{i+1};
		case 'savepng'
		      savepng = varargin{i+1};
		otherwise,
			error(['Unknown property ''' num2str(varargin{i})]);
	end
end
cd(session);
xml=session(end-13:end);
SetCurrentSession(xml);
ripples=GetRippleEvents;
channel=GetRippleChannel;
spikes1=GetSpikeTimes('output','numbered');
spikes2=GetSpikeTimes('output','full');
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && grep -nE "anova|multcompare|0\.01|0\.001|Pval|signrank|ranksum|>5|>=6|is\.up|is\.down|ctype|pyr" ExplainedVariance_PooledCorr_Groups.m | head -60
```

```
36:bothpyr=sum(Index.Type,2)==2;
42:run.sigup=Allpval.run(:,2)<0.01&Allcorr.run(:,2)>0;
43:run.sigdown=Allpval.run(:,2)<0.01&Allcorr.run(:,2)<0;
44:run.signot=Allpval.run(:,2)>=0.01&Allcorr.run(:,2)<0;
48:ripup.runup=bothpyr&ripple.up&run.sigup;
49:ripup.rundown=bothpyr&ripple.up&run.sigdown;
50:ripup.runnot=bothpyr&ripple.up&run.signot;
51:ripup.all=bothpyr&ripple.up;
53:ripdown.runup=bothpyr&ripple.down&run.sigup;
54:ripdown.rundown=bothpyr&ripple.down&run.sigdown;
55:ripdown.runnot=bothpyr&ripple.down&run.signot;
56:ripdown.all=bothpyr&ripple.down;
58:ripnone.runup=bothpyr&ripple.none&run.sigup;
59:ripnone.rundown=bothpyr&ripple.none&run.sigdown;
60:ripnone.runnot=bothpyr&ripple.none&run.signot;
61:ripnone.all=bothpyr&ripple.none;
160:xlabel('EV for ripple modulation groups, all pyr')
176:PyrMeanFR=MeanPairFR(bothpyr);
181:PyrBLAFR=Index.FR(bothpyr,2);
182:%  PyrBLAFR=unique(Index.FR(bothpyr,2));
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && sed -n 1,160p ExplainedVariance_PooledCorr_Groups.m | grep -v "^\s*$" | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|ylim|xlim|set\(|bar)"
```

```
function [EV,REV] = ExplainedVariance_PooledCorr_Groups
% Explained Variance_PooledCorr_Groups - Calculates and plots EV and REVs for different groups of Hpc-BLA pairs (based on ripple-modulation of BLA cell, RUN correlation and firing rates) 
%  
%  USAGE
%
%    [EV, REV] = ExplainedVariance_PooledCorr_Groups
%
%    struct		structure name (ex : 'BLA')
%    threshold		threshold for contributing and anticontributing cells
%    <options>      	optional list of property-value pairs (see table below)
%
%    =========================================================================
%     Properties            Values
%    -------------------------------------------------------------------------
%    EVtype		'cross' (cross-structure : default), 'intra' (intrastructure) 
%    =========================================================================
%
%  OUTPUT
%
%  NOTE
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package && grep -rnE "anova|multcompare|kruskal" --include=*.m . | head; grep -rn "RippleMod==\|Index.RippleMod\s*=\|RippleMod(" --include=*.m . | head
```

```
./Reactivations/ExplainedVariance_PrePostCorr_Ultimate.m:322:anovadiff=[prepostDiff.isup;prepostDiff.nomod;prepostDiff.isdown];
./Reactivations/ExplainedVariance_PrePostCorr_Ultimate.m:334:anovagr=zeros(length(runpval),1);
./Reactivations/ExplainedVariance_PrePostCorr_Ultimate.m:336:anovagr(ripplegr==1&issigplus)=1;
./Reactivations/ExplainedVariance_PrePostCorr_Ultimate.m:337:mean(anovadiff(ripplegr==1))
./Reactivations/ExplainedVariance_PrePostCorr_Ultimate.m:338:anovagr(ripplegr==1&isnosig)=2;
./Reactivations/ExplainedVariance_PrePostCorr_Ultimate.m:339:anovagr(ripplegr==1&issigneg)=3;
./Reactivations/ExplainedVariance_PrePostCorr_Ultimate.m:340:anovagr(ripplegr==2&issigplus)=4;
./Reactivations/ExplainedVariance_PrePostCorr_Ultimate.m:341:anovagr(ripplegr==2&isnosig)=5;
./Reactivations/ExplainedVariance_PrePostCorr_Ultimate.m:342:anovagr(ripplegr==2&issigneg)=6;
./Reactivations/ExplainedVariance_PrePostCorr_Ultimate.m:343:anovagr(ripplegr==3&issigplus)=7;
./Reactivations/ExplainedVariance_PooledCorr_Groups.m:38:ripple.up=Index.RippleMod==1;
./Reactivations/ExplainedVariance_PooledCorr_Groups.m:39:ripple.down=Index.RippleMod==2;
./Reactivations/ExplainedVariance_PooledCorr_Groups.m:40:ripple.none=Index.RippleMod==0;
./Reactivations/ExplainedVariance_PooledCorr.m:91:Index.RippleMod=[];
./Reactivations/ExplainedVariance_PooledCorr.m:136:    Index.RippleMod=[Index.RippleMod; reshape(repmat(STripplemod',size(HPindex,1),1),[],1)];
./Physiology/PoissonRippleMod.m:1:function poissonripplemod = PoissonRippleMod(session,varargin)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && sed -n 1,400p ExplainedVariance_PrePostCorr_Ultimate.m | grep -v "^\s*$" | grep -v "^\s*%" | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|ylim|xlim|set\(|bar|error)" | sed -n 25,260p
```

```
sess=[];
Allcorr.pre.isup=[];
Allcorr.pre.isdown=[];
Allcorr.pre.nomod=[];
Allcorr.pre.all=[];
Allcorr.run.isup=[];
Allcorr.run.isdown=[];
Allcorr.run.nomod=[];
Allcorr.run.all=[];
Allcorr.post.isup=[];
Allcorr.post.isdown=[];
Allcorr.post.nomod=[];
Allcorr.post.all=[];
AllpVal.pre.isup=[];
AllpVal.pre.isdown=[];
AllpVal.pre.nomod=[];
AllpVal.pre.all=[];
AllpVal.run.isup=[];
AllpVal.run.isdown=[];
AllpVal.run.nomod=[];
[... 217 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Reactivations && sed -n 345,420p ExplainedVariance_PrePostCorr_Ultimate.m | grep -v "^\s*$"; sed -n 1,25p ExplainedVariance_PrePostCorr_Ultimate.m | grep -iE "celltype|sleep|default|="
```

```
anovagr(ripplegr==3&issigneg)=9;
anovadiff(anovagr==0)=[];
anovagr(anovagr==0)=[];
[p,anovatab,stats]=anova1(anovadiff,anovagr,'Alpha',0.001);
%  [p,anovatab,stats]=kruskalwallis(anovadiff,anovagr);
[comp,means]=multcompare(stats,'Alpha',0.01);
%Equality of variance test
p=vartestn(anovadiff,anovagr);
%%%%%%%%%%%%
if strcmp(celltype,'all')
  celltypetitle='Pyr+Int';
elseif strcmp(celltype,'pyr')
  celltypetitle='PyrOnly';
end
if strcmp(EVtype,'cross')
  evtypetitle='Cross-Structure';
elseif strcmp(EVtype,'intra')
  evtypetitle='Intra-Structure';
end
anovagr=[];
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000061/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['draft_version']['name']); v=d.get('most_recent_published_version') or d['draft_version']; print(v['version'])"; curl -s https://api.dandiarchive.org/api/dandisets/000061/versions/draft/info/ | python3 -c "import json,sys; d=json.load(sys.stdin)['metadata']; print(d.get('description')); print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package && for f in Behavior/LapType.m Behavior/ClassifyLaps.m Miscellaneous/SaveAirpuffEvents.m Behavior/RunIntervals.m; do echo "=== $f"; grep -v "^\s*$" $f | grep -v "^\s*%" | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|ylim|xlim|set\(|bar|error)"; done
```

```
=== Behavior/LapType.m
function [safelaps,aplaps]=LapType(session)
cd(session);
xml=session(end-13:end);
load([xml '-Laps.mat']);
load('States.mat');
load('runintervals.mat');
load('airpuff.mat')
git st
if size(runintervals,1)<3
  warning('Should be 3 runintervals : wrong size')
end
if strcmp(airpuff.dir,'LtoR')
  aplaps.all = LtoRlaps ;
  aplaps.prerun = Restrict(LtoRlaps,runintervals(1,:));
  aplaps.run = Restrict (LtoRlaps,runintervals(2,:));
  aplaps.postrun = Restrict (LtoRlaps,runintervals(3,:));
  safelaps.all = RtoLlaps ;
  safelaps.prerun = Restrict(RtoLlaps,runintervals(1,:));
  safelaps.run = Restrict (RtoLlaps,runintervals(2,:));
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Behavior && grep -v "^\s*$" BehavioralMeasures.m | grep -v "^\s*%" | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|ylim|xlim|set\(|bar|error|Plot)" | sed -n 20,200p
```

```
xml=session(end-13:end)
  SetCurrentSession(xml,'spikes','off')
end
load('airpuff.mat');
if exist('airpuffPrevious.mat')==2
  Y=load('airpuffPrevious.mat');
else
  Y=[];
end
pos=GetPositions('coordinates','real','pixel',0.43,'discard','none');
CleanPos(pos);
pos(:,2:3)=[];
pos=InterpolateNaNPos(pos);
if exist('runintervals.mat')==2
  load('runintervals.mat');
  runint=runintervals;
end
prerun=runint(1,:);
run=runint(2,:);
postrun=runint(3,:);
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Behavior && grep -v "^\s*$" BehavioralMeasures_Stats.m | grep -v "^\s*%" | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|ylim|xlim|set\(|bar|error|Plot|boxplot)" | sed -n 1,140p; grep -v "^\s*%" BehavioralMeasuresAll.m | grep -nE "overlap|exist|isnan|ratsess"
```

```
function stats = BehavioralMeasures_Stats(varargin)
ratnum='all';
if mod(length(varargin),2) ~= 0,
end
for i = 1:2:length(varargin),
  if ~ischar(varargin{i}),
  end
  switch(lower(varargin{i})),
    case 'ratnum',
	ratnum = varargin{i+1};
  otherwise,
  end
end
load('/media/Data-01/All-Rats/BehavioralMeasures/BehavioralMeasures.mat')
Rats=rats(:);
if strcmp(ratnum,'all')
  sesstotal=55;
  for i=1:55
    prerun.currentvel(i)=PrePmeanVAll{i}.prerun;
    prerun.previousvel(i)=YPrePmeanVAll{i}.prerun;
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Physiology && grep -nE "0\.001|pval|isnan|sum\(|Type|==1|==2|load\(" PoissonRippleModPercent.m | head -50; echo; grep -v "^\s*%" PoissonRippleModAll.m | grep -v "^\s*$" | sed -n 1,40p
```

```
1:function [bla,hpc] = PoissonRippleModPercent(pval)
6:%    [bla,hpc] = PoissonRippleModPercent (pval)
8:%    pval       pvalue under which a cell is considered modulated.
29:load('/media/Data-01/All-Rats/PoissonRippleMod.mat');
30:load('/media/Data-01/All-Rats/AllRats-FinalType.mat');
31:load('/media/Data-01/All-Rats/SpikeParameters.mat');
32:load('/media/Data-01/All-Rats/Structures/structures.mat');
34:%  pval=0.001;
35:finaltype=finalType(ismember(finalType(:,1:4),poissonripplemod(:,1:4),'rows'),5);
44:%  pval=0.05/size(bla.stats,1);
48:bla.nall.ccg=sum(bla.ccgtype~=0);
49:bla.nint.final=sum(bla.finaltype==2);
50:bla.nint.ccg=sum(bla.ccgtype==2);
51:bla.npyr.final=sum(bla.finaltype==1);
52:bla.npyr.ccg=sum(bla.ccgtype==1);
54:bla.allsig=sum(bla.stats(:,6)<pval/2|bla.stats(:,7)<pval/2);
55:bla.allsigup=sum(bla.stats(:,6)<pval/2);
56:bla.allsigdown=sum(bla.stats(:,7)<pval/2);
59:bla.intsig.final=sum((bla.stats(:,6)<pval/2|bla.stats(:,7)<pval/2)&bla.finaltype==2);
60:bla.intsigup.final=sum(bla.stats(:,6)<pval/2&bla.finaltype==2);
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Physiology && grep -v "^\s*$" RippleMod_PrePost.m | grep -v "^\s*%" | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|ylim|xlim|set\(|bar|error|Plot|imagesc|colorbar|caxis)" | sed -n 1,150p
```

```
function RippleMod_PrePost_2(pval,varargin)
CellList=[];
savefig='off';
if nargin < 1,
end
if mod(length(varargin),2) ~= 0,
end
for i = 1:2:length(varargin),
  if ~ischar(varargin{i}),
  end
  switch(lower(varargin{i})),
    case 'celllist',
      CellList = varargin{i+1};	
    case 'savefig'
      savefig = varargin{i+1};
    otherwise,
  end
end
load('/media/Data-01/All-Rats/SpikeParameters.mat');
load('/media/Data-01/All-Rats/PoissonRippleMod.mat');
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package && grep -v "^\s*%" Reactivations/ExplainedVariance_PooledCorr.m | grep -v "^\s*$" | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|ylim|xlim|set\(|bar|error|Plot)" | sed -n 60,260p
```

```
Allpval.run=[Allpval.run;NaN(length(PvalMatrix.pre.sws.all.Rall(:)),3)];
    end
    Allpval.sws=[Allpval.sws;PvalMatrix.pre.sws.all.Rall(:) PvalMatrix.run.all.Rall(:) PvalMatrix.post.sws.all.Rall(:)];
    Allpval.rem=[Allpval.rem;PvalMatrix.pre.rem.all.Rall(:) PvalMatrix.run.all.Rall(:) PvalMatrix.post.rem.all.Rall(:)];
    Allpval.rip=[Allpval.rip;PvalMatrix.pre.rip_in.all.Rall(:) PvalMatrix.run.all.Rall(:) PvalMatrix.post.rip_in.all.Rall(:)];
    STindex=STindex(:,1:2);
    HPindex=HPindex(:,1:2);
    Index.Cells=[Index.Cells;[repmat(ratsess,length(CorrMatrix.pre.sws.all.Rall(:)),1) repmat(HPindex(:,1:2),size(STindex,1),1) reshape(repmat(STindex(:)',size(HPindex,1),1),[],2)]];
    Index.Type=[Index.Type;[repmat(HPtype,size(STindex,1),1) reshape(repmat(STtype',size(HPindex,1),1),[],1)]];
    STripplemod=zeros(size(STindex,1),1);
    STripplemod(is.up)=1;
    STripplemod(is.down)=2;    
    Index.RippleMod=[Index.RippleMod; reshape(repmat(STripplemod',size(HPindex,1),1),[],1)];
    STfiringrate=StatesFR(ismember(StatesFR(:,1:4),[repmat(ratsess,size(STindex,1),1) STindex],'rows'),10);
    HPfiringrate=StatesFR(ismember(StatesFR(:,1:4),[repmat(ratsess,size(HPindex,1),1) HPindex],'rows'),10);
    Index.FR=[Index.FR;[repmat(HPfiringrate,size(STindex,1),1) reshape(repmat(STfiringrate',size(HPindex,1),1),[],1)]];    
  end
end
bothpyr=sum(Index.Type,2)==2;
nonan.rem=sum(isnan(Allcorr.rem),2)==0;
[... 173 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package && grep -v "^\s*%" Reactivations/ExplainedVariance_PooledCorr.m | grep -v "^\s*$" | sed -n 1,60p | grep -vE "error\("; echo ====; grep -v "^\s*%" Physiology/AllRippleCCGs_2.m | grep -v "^\s*$" | grep -nE "CCG|gain|binSize|duration|baseline|Restrict|presleep|postsleep|sws|smooth|0\.1" | head -40
```

```
function [Allcorr,Allpval,Index,EV,REV,PairContrib,Minusindex,BLA,HPC,CorrDiff] = ExplainedVariance_PooledCorr(struct,threshold,varargin)
EVtype='cross';
thresh2=0.000003;
if nargin < 1,
end
if mod(length(varargin),2) ~= 0,
end
for i = 1:2:length(varargin),
  if ~ischar(varargin{i}),
  end
  switch(varargin{i}),
    case 'EVtype',
      EVtype = lower(varargin{i+1});
    otherwise,
  end
end
load('/media/Data-01/All-Rats/sessionindexing.mat');
load('/media/Data-01/All-Rats/AllRats-FinalType.mat');
load('/media/Data-01/All-Rats/PoissonRippleMod.mat');
load('/media/Data-01/All-Rats/AllRats-StatesFR.mat');
[... 78 more lines not kept]
```

**Agent**

I have the main method details from the code. One external detail remains: how FMAToolbox's `SyncHist` bins the peri-ripple curve. I'll check that toolbox's source.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone --depth 1 https://github.com/michael-zugaro/FMAToolbox.git 2>&1 | tail -1; cd FMAToolbox && git log -1 --format=%H; f=$(find . -name SyncHist.m); grep -nE "nBins|smooth|Smooth|durations|mean" $f | head -40
```

```
Cloning into 'FMAToolbox'...
6bbb3662f7ed1ccf09c5ff4b4d233e27e17c71a6
18:%    [mean,error,timeBins] = SyncHist(synchronized,indices,'mode','mean',<options>)
31:%     'mode'        type of histogram: 'sum' (default), 'mean' or 'dist'
32:%     'durations'   durations before and after synchronizing events for each
34:%     'nBins'       total number of time bins (default 100)
37:%     'smooth'      standard deviation for Gaussian kernel (default 0, no
38:%                   smoothing)
42:%                   'sem' to compute standard error of the mean, or '95%' to
43:%                   compute 95% confidence intervals (only in 'mean' mode)
79:durations = [-0.5 0.5];
80:nBins = 100;
81:smooth = 0;
113:			if ~isastring(mode,'sum','mean','dist'),
117:		case 'durations',
118:			durations = varargin{i+1};
119:			if ~isdvector(durations,'#2','<'),
120:				error('Incorrect value for property ''durations'' (type ''help <a href="matlab:help SyncHist">SyncHist</a>'' for details).');
124:			nBins = varargin{i+1};
125:			if ~isdscalar(nBins,'>0'),
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/FMAToolbox && f=$(find . -name SyncHist.m); sed -n 214,230p $f; grep -n "timeBins\s*=" $f
```

```
case 'mean',
		if pointProcess,
			% Smoothed mean
			for j = 2:size(synchronized,2),
				a(:,j-1) = Smooth(Accumulate(binnedTime,synchronized(:,j),nBins),smooth)/(nTrials*timeBinSize);
			end
			b = []; % Not yet implemented
		else
			% Number of values in each time bin
			n = Smooth(Accumulate(binnedTime,1,nBins),smooth);
			% Smoothed mean
			for j = 2:size(synchronized,2),
				a(:,j-1) = Smooth(Accumulate(binnedTime,synchronized(:,j),nBins),smooth)./n;
			end
			if strcmp(type,'circular'),
				b = []; % Error not computed for circular data
			else
195:timeBins = (start:timeBinSize:stop-timeBinSize)+timeBinSize/2;
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; ls docs; grep -rn "inferred\|open:" docs/*.md | head -20
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

[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
c=s['\$defs'] if '\$defs' in s else s.get('definitions')
print(json.dumps(s,indent=1)[:6000])"
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
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s['\$defs'],indent=1)[:4000])"
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

Plan settled: about 25 claims, keeping the six old ids where the finding is the same. Before writing, I'll check the last few scripts: state firing rates, ripple rate, and safe vs air-puff firing.

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Physiology && for f in StatesFiringRates.m RippleRatePrePost.m RippleRatePrePost_All.m; do echo "=== $f"; grep -v "^\s*$" $f | grep -v "^\s*%" | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|ylim|xlim|set\(|bar|error|Plot|case|switch|end$|if mod|for i = 1:2)" | sed -n 1,70p; done
```

```
=== StatesFiringRates.m
function StatesFR = StatesFiringRates (session)
StatesFR=[];
cd(session);
xml=session(end-13:end);
SetCurrentSession(xml);
load('/media/Data-01/All-Rats/sessionindexing.mat');
ratsess = ratsessionindex(strcmp(xmlpath,[session '/']),:)
spikes1=GetSpikeTimes('output','numbered');
spikes2=GetSpikeTimes('output','full');
spikes=[spikes2 spikes1(:,2)];
spikes(spikes(:,3)==0,:)=[];
spikes(spikes(:,3)==1,:)=[];
ids=unique(spikes(:,4));
for ii=1:length(ids)
  spikes(spikes(:,4)==ids(ii),4)=ii;
idx=unique(spikes(:,2:4),'rows'); % shank / cell/ ID
if min(idx(:,3))==1 & sum(diff(idx(:,3))-1)==0
  disp('Renumbering OK')
else
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package && grep -rln "safelaps\|aplaps" --include=*.m . ; grep -n "safe\|signrank\|ap\b" Physiology/PrePostFiringRates_Plot.m | head -20
```

```
./Reactivations/ReplayInTime_LapTypes.m
./Physiology/PlotAirpuffRewardMod_SingleCells.m
./Physiology/AirpuffRewardMod_Structures_2.m
./Physiology/AirpuffRewardMod_Structures.m
./Behavior/VelocityMaps.m
./Behavior/LapType.m
81:  [prun,~]=signrank(CellFR(:,prerun),CellFR(:,postrun))
82:  [psws,~]=signrank(CellFR(:,presws),CellFR(:,postsws))
83:  [prem,~]=signrank(CellFR(:,prerem),CellFR(:,postrem))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Physiology && grep -nE "safelaps|aplaps|signrank|FR|rate|Restrict|pyr|type" AirpuffRewardMod_Structures_2.m | head -40
```

```
1:function [AllCurves,CompleteCurves,CellIndex,x,FRIndex,AllAPpeth,AllRWpeth] = AirpuffRewardMod_Structures_2(structure,varargin)
5:ctype = 'pyr';
10:  error('Incorrect number of parameters (type ''help <a href="matlab:help FunctionName">FunctionName</a>'' for details).');
15:  error('Incorrect number of parameters  (type ''help <a href="matlab:help FunctionName">FunctionName</a>'' for details).');
21:    error(['Parameter ' num2str(i) ' is not a property (type ''help <a href="matlab:help FunctionName">FunctionName</a>'' for details).']);
24:    case 'ctype',
25:      ctype = varargin{i+1};
29:      error(['Unknown property ''' num2str(varargin{i}) ''' (type ''help <a href="matlab:help FunctionName">FunctionName</a>'' for details).']);
62:FRIndex=[];
76:    sessiontypes=finalType(ismember(finalType(:,1:2),ratsess,'rows'),3:5);	% shank/cell/type for all session cells
77:    sessionFR=SpikeParameters(ismember(SpikeParameters(:,1:2),ratsess,'rows'),[3 4 10]);
80:    structureFR=sessionFR(ismember(sessionFR(:,1),structureshanks,'rows'),3);
82:    structuretypes=sessiontypes(ismember(sessiontypes(:,1),structureshanks,'rows'),3);
84:    if strcmp(ctype,'all')
86:      cellFR=structureFR;
87:    elseif strcmp(ctype,'pyr')
88:      cells=structurecellsID(structuretypes==1);
89:      cellFR=structureFR(structuretypes==1);
99:	airpuffcurve.all=MazeCurve{cells(j)}.run.curve.rate(APzone);
100:	airpuffcurve.airpuff=MazeCurve{cells(j)}.run.airpufflapscurve.rate(APzone);
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Behavior && grep -nE "corr|regress|signrank|ttest|Habit|habit|laps|/" AirpuffPositionDistribution_Plot.m Performance.m Performance_All.m | grep -v "^\S*:\s*%" | head -40
```

```
AirpuffPositionDistribution_Plot.m:31:cd('/media/Data-01/All-Rats/BehavioralMeasures');
AirpuffPositionDistribution_Plot.m:106:[r1,p1]=corrcoef(flippedNormAP,PrerunVel)
AirpuffPositionDistribution_Plot.m:107:[r2,p2]=corrcoef(flippedNormAP,RunVel)
AirpuffPositionDistribution_Plot.m:108:[r3,p3]=corrcoef(flippedNormAP(~isnan(PostrunVel)),PostrunVel(~isnan(PostrunVel)))
AirpuffPositionDistribution_Plot.m:141:[r1,p1]=corrcoef(CenterDist,PrerunVel)
AirpuffPositionDistribution_Plot.m:142:[r2,p2]=corrcoef(CenterDist,RunVel)
AirpuffPositionDistribution_Plot.m:143:[r3,p3]=corrcoef(CenterDist(~isnan(PostrunVel)),PostrunVel(~isnan(PostrunVel)))
Performance.m:1:function [laps,runtime,perf,xml] = Performance(session,run)
Performance.m:35:runlrw=Restrict(LtoRlaps(:,1),runInterval);
Performance.m:37:laps=size(runlrw,1);
Performance.m:39:perf=(laps/runtime)*100;
Performance.m:41:save('Perf.mat','perf','laps','runtime');
Performance_All.m:24:load('/media/Data-01/All-Rats/TrainingSessionsForPerf.mat');
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Behavior && sed -n 60,145p AirpuffPositionDistribution_Plot.m | grep -v "^\s*$" | grep -vE "^\s*(subplot|plot|xlabel|ylabel|title|figure|hold|ylim|xlim|set\(|bar|Plot|scatter|lsline)"; sed -n 20,40p Performance.m
```

```
%  plot(NormAP(fullsess(:,1)==8),PostrunVel(fullsess(:,1)==8),'b.');
%  ylim([0 90])
%  xlim([0 1])
%  subplot(2,2,2);hold on;
%  plot(NormAP(fullsess(:,1)==9),RunVel(fullsess(:,1)==9),'r.');
%  plot(NormAP(fullsess(:,1)==9),PrerunVel(fullsess(:,1)==9),'g.');
%  plot(NormAP(fullsess(:,1)==9),PostrunVel(fullsess(:,1)==9),'b.');
%  ylim([0 90])
%  xlim([0 1])
%  subplot(2,2,3);hold on;
%  plot(NormAP(fullsess(:,1)==10),RunVel(fullsess(:,1)==10),'r.');
%  plot(NormAP(fullsess(:,1)==10),PrerunVel(fullsess(:,1)==10),'g.');
%  plot(NormAP(fullsess(:,1)==10),PostrunVel(fullsess(:,1)==10),'b.');
%  ylim([0 90])
%  xlim([0 1])
%  subplot(2,2,4);hold on;
%  xlim([0 1])
%  plot(NormAP(fullsess(:,1)==11),RunVel(fullsess(:,1)==11),'r.');
%  plot(NormAP(fullsess(:,1)==11),PrerunVel(fullsess(:,1)==11),'g.');
%  plot(NormAP(fullsess(:,1)==11),PostrunVel(fullsess(:,1)==11),'b.');
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers/GGirardeau-BLAHpcInteractions-Package/Behavior && sed -n 30,59p AirpuffPositionDistribution_Plot.m | grep -v "^\s*$" | grep -v "^\s*%"; grep -n "NormAP\|loc" AirpuffPositionDistribution.m | head
```

```
cd('/media/Data-01/All-Rats/BehavioralMeasures');
load('BehavioralMeasures.mat');
load('NormAPpos.mat');
fullsess=ratsession(ismember(ratsession,ratsess,'rows'),:);
is.rat55=ismember(ratsession,fullsess,'rows');
is.rat53=ismember(ratsess,fullsess,'rows');
for i=1:length(PrePmeanVAll)
    RunVel(i)=PrePmeanVAll{i}.run;
    PrerunVel(i)=PrePmeanVAll{i}.prerun;
    PostrunVel(i)=PrePmeanVAll{i}.postrun;
end
RunVel=RunVel(is.rat55)';
PrerunVel=PrerunVel(is.rat55)';
PostrunVel=PostrunVel(is.rat55)';
NormAP=NormalizedAPpos(is.rat53);
dirs=directions(is.rat53);
flippedNormAP=NormAP;
flippedNormAP(dirs==1)=abs(flippedNormAP(dirs==1)-1)
43:    ap=airpuff.loc*0.43;
58:save('NormAPpos.mat','NormalizedAPpos','xmlIndex','directions','ratsess');
[... 1 more lines not kept]
```

**Agent**

I've finished reading the code. Now I'm writing the claims file: 31 claims, with shared methods and open details set out in the opening comment.

**Agent calls Write**

```json
{
 "file_path": "claims/000061/10.1038-nn.4637.yaml",
 "content": "# Claims for Girardeau, Inema & Buzsaki (2017), Nat. Neurosci. 20, 1634-1642, on dandiset 000061.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-20, protocol\n# pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4). The reader did not look at the\n# dandiset's data or files; only its archive title and description, which name this paper.\n#\n# Why this file was rewritten. The earlier file was written from the abstract alone (the full text\n# was not open then) and its methods were fixed by an agent. Read against the full text and the\n# supplement on 2026-10-20, two of its claims were tested with measures the paper does not use:\n# aversive-direction-stronger (the paper compares peri-ripple reactivation strength R of a run\n# correlation template, Fig. 6b, not singular-vector patterns over all sleep bins) and\n# reactivation-involves-ripple-up-cells (the paper compares post-NREM minus pre-NREM pair\n# correlations across nine pair groups with a one-way ANOVA, Fig. 5a, not BLA pattern weights). The\n# other claims of that file also used agent-chosen methods (SVD patterns, shuffled ripple windows)\n# in place of the paper's EV/REV, Poisson ripple-modulation test and reactivation strength R, and\n# many findings had no claim. Every criterion is now taken from the Online Methods, the legends,\n# the supplement and the paper's code. Ids are kept where the finding is the same:\n# hpc-bla-reactivation-post-sleep (EV against REV, Fig. 3c), reactivation-peaks-at-ripples\n# (Supplementary Fig. 11a), bla-ripple-up-subgroup (Fig. 4), reactivation-involves-ripple-up-cells\n# (Fig. 5a), aversive-direction-stronger (Fig. 6b) and rats-learn-puff-location (Fig. 1b). The\n# other 25 claims are new.\n#\n# Text read. The version of record (PDF supplied by a person, text extracted 2026-10-20), with the\n# main text, figure legends, Online Methods, Life Sciences Reporting Summary, and the\n# Supplementary Information PDF (41593_2017_BFnn4637_MOESM1_ESM.pdf; Supplementary Figs. 1 to 11\n# and Supplementary Tables 1 and 2). Supplementary Table 1 is an image whose numbers the text\n# does not carry.\n#\n# Code read. The code the paper links (Code availability), github.com/buzsakilab/papers, folder\n# GGirardeau-BLAHpcInteractions-Package, commit cdcec89f8d1f5cf11f407f82827f9af44405c5b7: Matlab\n# scripts for behavior (BehavioralMeasures, ClassifyLaps, LapType, Performance,\n# AirpuffPositionDistribution), cell classification (MonoSynConvClick, CellClassifkmeans,\n# FinalType), physiology (PoissonRippleMod, PoissonRippleModPercent, StatesFiringRates,\n# AllRippleCCGs_2, RippleMod_PrePost, RippleRatePrePost, AirpuffRewardMod_Structures_2) and\n# reactivations (ExplainedVariance_Ultimate, ExplainedVarianceMean_Ultimate,\n# ExplainedVariance_PrePostCorr_Ultimate, ExplainedVariance_PooledCorr,\n# ExplainedVariance_PooledCorr_Groups, ReplayInTime, ReplayInTime_LapTypes and their _All and\n# _Plot scripts). They call FMAToolbox (fmatoolbox.sourceforge.net, read at\n# github.com/michael-zugaro/FMAToolbox commit 6bbb3662f7ed1ccf09c5ff4b4d233e27e17c71a6 for\n# SyncHist) and a poissonTest function that is not in the repository.\n#\n# The data the paper used. Four male Long-Evans rats (rats 1 to 4), 61 sessions, 7,390 units.\n# Silicon probes in both amygdalae (two 8-shank probes, lowered 140 um after each session) and in\n# dorsal CA1 (one 4-shank probe); the hippocampal probe of one rat (rat 2) failed, so\n# hippocampus-BLA analyses use 3 rats (29 sessions with simultaneous BLA and hippocampus units).\n# Each daily session is pre-sleep, pre-run (track, no air puff), run (training; air puff at one\n# location in one running direction, location changed daily, water rewards at both ends),\n# post-sleep, post-run (no air puff). Measured variables used here: sorted spike times with unit\n# location (BLA, central nuclei, piriform cortex, hippocampus, from histology maps) and putative\n# type (pyramidal or interneuron); the epochs; scored brain states (wake, NREM, REM); hippocampal\n# ripple events (start, peak, stop); head position on the track; air puff times and locations, and\n# the previous day's air puff location and direction (for the danger zones); reward times. 55\n# sessions in 4 rats enter the behavioral analysis. Data were to be deposited at CRCNS; the\n# dandiset is described as this paper's data.\n#\n# Methods shared by the criteria (each from the paper or its code, as cited):\n# M1 Units. Hippocampal units are those on hippocampal CA1 shanks; BLA units those the paper's\n#   histology maps place in the BLA (Online Methods, Histology; Supplementary Fig. 2). Putative\n#   pyramidal cells and interneurons are the paper's types (monosynaptic identification, then\n#   k-means on spike width and peak-to-trough for the rest; Online Methods, Preprocessing;\n#   FinalType.m, type 1 pyramidal, type 2 interneuron). \"Pyramidal pairs\" means both cells\n#   pyramidal.\n# M2 Epochs. Pre-sleep and post-sleep are the sleep epochs before and after the run (training)\n#   epoch; pre-NREM and post-NREM are the scored NREM intervals inside them; the template epoch\n#   is the whole run epoch, including reward platforms (Supplementary Fig. 11a legend;\n#   ExplainedVariance_Ultimate.m and ReplayInTime.m use the second run interval whole).\n# M3 Binning. Spike counts in 50-ms bins (Online Methods), spikes after the end of the last run\n#   epoch dropped (ReplayInTime.m).\n# M4 EV and REV. For each hippocampus-BLA pair, the Pearson correlation of binned counts in the\n#   pre-NREM bins, the run bins and the post-NREM bins; the three pair-correlation matrices are\n#   correlated with one another over pairs, pairs with an undefined correlation left out\n#   (corrcoef with 'rows','complete'), giving r(run,post), r(run,pre), r(pre,post).\n#   EV = ((r(run,post) - r(run,pre) r(pre,post)) / sqrt((1 - r(run,pre)^2)(1 - r(pre,post)^2)))^2,\n#   REV the same with pre and post swapped (Online Methods; ExplainedVariance_Ultimate.m). Shown\n#   as percent. A session enters when it has at least 6 hippocampal and 6 BLA cells of the cell\n#   type used (Online Methods says \"a minimum of 1 shank and 6 cells in each structure\";\n#   ExplainedVarianceMean_Ultimate.m tests more than 5 cells in each structure).\n#   For REM, sessions need more than 3 min (180 s) of REM in both pre- and post-sleep.\n# M5 Ripples. The paper's ripple events (detection in Online Methods), kept when inside NREM.\n# M6 Ripple modulation of a unit (Online Methods; PoissonRippleMod.m; ExplainedVariance_Ultimate.m).\n#   Over all NREM of the session: baseline is NREM minus every ripple widened by 100 ms on each\n#   side; the unit's spike count inside ripples (start to stop) is compared with a Poisson\n#   distribution of mean (baseline rate x total ripple time). Upmodulated when the upper tail\n#   probability is below 0.0005, downmodulated when the lower tail probability is below 0.0005\n#   (the code's 0.001/2, the Methods' \"P < 0.001\"); units with no spike in ripples or in baseline\n#   are untested. Otherwise not modulated.\n# M7 Reactivation strength R (Online Methods; Supplementary Fig. 10; ReplayInTime.m,\n#   ReplayInTime_LapTypes.m). Binned counts of the pyramidal cells (or all cells, where stated)\n#   are z-scored per cell within the template bins, and within the NREM bins of each sleep epoch.\n#   Template C = Z_hpc' Z_bla / nBins over the template bins. R(t) = z_hpc(t) C z_bla(t)' for each\n#   NREM bin t of pre- and post-sleep; R is z-scored over the NREM bins of each epoch. Around each\n#   ripple peak of that epoch's NREM, R is averaged in 100 bins of 40 ms over -2 to +2 s\n#   (FMAToolbox SyncHist, mode mean, its default 100 bins) with Gaussian smoothing of SD 2 bins\n#   ('smooth', 2), giving one peri-ripple curve per session and epoch. The ripple-peak value of a\n#   session is the mean of that curve over bin centres strictly between -0.25 and +0.25 s (12\n#   bins; ReplayInTime_All.m). A session enters with at least 6 hippocampal and 6 BLA cells of\n#   the type used (ReplayInTime_All.m, ReplayInTime_LapTypes_All.m).\n# M8 Air puff and safe laps (ClassifyLaps.m, LapType.m). In the run epoch, laps are the intervals\n#   during which position stays inside a 150-cm window of the track; a lap goes left to right or\n#   right to left when its end lies more than 10 cm from its start in that direction. Air puff\n#   laps are those in the air puff direction of the day, safe laps the others.\n#\n# Details the paper and its code leave open, with the readings the text allows (each criterion\n# that uses one says so; the notebook runs every reading):\n# O1 The 150-cm lap window of M8 starts at a left limit picked by hand on a plot (ClassifyLaps.m).\n#   Readings (a) lap intervals the dataset holds, if any; (b) the M8 rule with the window's left\n#   edge at the smallest run-epoch position; (c) laps as the intervals between consecutive\n#   rewards at opposite ends of the track.\n# O2 poissonTest (M6) is not in the repository. Readings (a) upper tail P(X >= n) and lower tail\n#   P(X <= n); (b) upper tail P(X > n) and lower tail P(X < n).\n# O3 Bin time stamps (bin start or centre) when aligning R to ripple peaks. A standard choice (bin\n#   centre); it cannot change an outcome at 40-ms resolution.\n# O4 Fig. 2c uses monosynaptically identified pyramidal cells and interneurons (675 and 175). If\n#   the dataset does not mark which cells were identified monosynaptically, the readings are\n#   (a) the identified cells where marked; (b) all putative cells of each type.\n# O5 The family size of the Bonferroni corrections in Fig. 1b is not given. Readings (a) all post\n#   hoc tests of the panel (four for speeds, three for ratios); (b) uncorrected 0.05.\n# O6 The post hoc correction of Fig. 5a. The Online Methods say Bonferroni; the legend says\n#   Tukey-Kramer, as the code does (multcompare default, alpha 0.01). Main reading Bonferroni\n#   (Methods first, protocol step 2), variant Tukey-Kramer.\n# O7 How the BLA firing rate of safe and air puff trajectories is taken is not in the text or the\n#   code read. Readings (a) spike count over time on safe laps and on air puff laps of the run;\n#   (b) the mean of the cell's position firing-rate curve on each lap type.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000061\"\npaper: doi:10.1038/nn.4637\nclaims:\n- id: unit-counts\n  statement: Over 61 sessions in 4 rats, 7,390 well-isolated units were recorded (rat 1, 2,444;\n    rat 2, 1,294; rat 3, 1,138; rat 4, 2,514), of which 2,038 were in the BLA, 782 in the central\n    nuclei, 1,560 in the piriform cortex and 1,210 in the hippocampus.\n  source: Results, BLA recordings and sleep physiology, paragraph 1; Supplementary Table 1\n  quote: Over the course of a total of 61 sessions, we recorded 7,390 well-isolated units (rat 1,\n    2,444; rat 2, 1,294; rat ... 3, 1,138; rat 4, 2,514). On the basis of histological\n    reconstruction of probe placement and probe movement record, 2,038 of these were in the BLA,\n    782 in the central nuclei, 1,560 in the piriform cortex and 1,210 in the hippocampus\n  expected:\n  - quantity: sessions\n    value: 61\n    tolerance: 6.1\n  - quantity: units, all rats\n    value: 7390\n    tolerance: 739\n  - quantity: units, rat 1\n    value: 2444\n    tolerance: 244.4\n  - quantity: units, rat 2\n    value: 1294\n    tolerance: 129.4\n  - quantity: units, rat 3\n    value: 1138\n    tolerance: 113.8\n  - quantity: units, rat 4\n    value: 2514\n    tolerance: 251.4\n  - quantity: BLA units\n    value: 2038\n    tolerance: 203.8\n  - quantity: central nuclei units\n    value: 782\n    tolerance: 78.2\n  - quantity: piriform cortex units\n    value: 1560\n    tolerance: 156\n  - quantity: hippocampal units\n    value: 1210\n    tolerance: 121\n  criterion: Counts of distinct sorted units and sessions, per rat and per location label (M1).\n    Reproduced when every count is within its tolerance; partially reproduced when the totals\n    are and some location counts are not.\n- id: rats-learn-puff-location\n  statement: Rats learned the daily location of the air puff. The speed ratio between the previous\n    and the current danger zone rises from pre-run to run and post-run, reversing between pre-run\n    and post-run.\n  source: Results, Rats learn the daily location of an aversive air puff on a linear track,\n    paragraph 1; Figure 1b, right; Supplementary Fig. 1b\n  quote: Therefore, the systematic reversal in the speed ratio (previous/current danger zone)\n    between pre- and ... post-run indicates learning of the new air puff location (Fig. 1b and\n    Supplementary Fig. 1b).\n  statistics:\n  - about: speed ratio over pre-run, run and post-run\n    test: one-way repeated measure ANOVA\n    statistic: F = 40.48, d.f. = 2\n    p: 1.31e-13\n    n: 55 sessions in 4 animals\n  - about: speed ratio, pre-run against run\n    test: post hoc t-test\n    statistic: t(51) = -8.49\n    p: 2.5e-11\n    corrected: Bonferroni (on the significance thresholds; the P shown is uncorrected)\n  - about: speed ratio, pre-run against post-run\n    test: post hoc t-test\n    statistic: t(51) = -5.08\n    p: 5.3e-6\n    corrected: Bonferroni (on the significance thresholds; the P shown is uncorrected)\n  - about: speed ratio, run against post-run\n    test: post hoc t-test\n    statistic: t(50) = 4.43\n    p: 5.1e-5\n    corrected: Bonferroni (on the significance thresholds; the P shown is uncorrected)\n  criterion: Per session and run epoch (pre-run, run, post-run), the mean speed in the current\n    danger zone (the 20 cm before the day's air puff location, on laps of the day's air puff\n    direction) and in the previous danger zone (the 20 cm before the previous day's location, on\n    laps of the previous day's direction); speed from positions smoothed over 5 samples\n    (LinearVelocity(pos,5)); ratio = (previous - current)/(previous + current) (Online Methods;\n    BehavioralMeasures.m). Laps per M8 under each reading of O1. Sessions with all three ratios\n    defined enter (the first session of a rat has no previous day). A one-way repeated-measures\n    ANOVA over the three epochs, then paired t-tests (BehavioralMeasures_Stats.m). Reproduced\n    when the ANOVA has p < 0.05 and the post-run ratio exceeds the pre-run ratio by paired t-test\n    at p < 0.05/3 (O5 reading a) or p < 0.05 (reading b); the run against pre-run and run against\n    post-run tests are reported.\n- id: dz-speed-slower-post-run\n  statement: Speed in the current danger zone is lower in post-run than in pre-run, and in run and\n    post-run rats run slower in the current than in the previous danger zone.\n  source: Results, Rats learn the daily location of an aversive air puff on a linear track,\n    paragraph 2; Figure 1b, left; Figure 1c\n  quote: This was quantitatively reflected by the significantly slower speed in the current\n    danger zone in post-run compared to pre-run (Fig. 1b,c).\n  statistics:\n  - about: speed over epochs (pre-run, run, post-run)\n    test: two-way repeated measures ANOVA, session effect\n    statistic: F = 41.51, d.f. = 2\n    p: 7.48e-14\n    n: 55 sessions in 4 animals\n  - about: speed, current against previous danger zone\n    test: two-way repeated measures ANOVA, air puff location effect\n    statistic: F = 11.81, d.f. = 1\n    p: 0.0012\n  - about: epoch by danger zone\n    test: two-way repeated measures ANOVA, interaction\n    statistic: F = 30.53, d.f. = 2\n    p: 4.46e-11\n  - about: previous against current danger zone speed, pre-run\n    test: post hoc paired t-test\n    statistic: t(52) = 3.45\n    p: 0.0011\n    corrected: Bonferroni\n  - about: previous against current danger zone speed, run\n    test: post hoc paired t-test\n    statistic: t(51) = -6.84\n    p: 9.70e-9\n    corrected: Bonferroni\n  - about: previous against current danger zone speed, post-run\n    test: post hoc paired t-test\n    statistic: t(51) = -3.10\n    p: 0.00307\n    corrected: Bonferroni\n  - about: current danger zone speed, pre-run against post-run\n    test: post hoc paired t-test\n    statistic: t(53) = 5.47\n    p: 1.21e-6\n    corrected: Bonferroni\n  depends_on:\n  - rats-learn-puff-location\n  criterion: The danger-zone speeds of rats-learn-puff-location. A two-way repeated-measures\n    ANOVA (epoch by danger zone) over sessions with all six speeds, then paired t-tests\n    (BehavioralMeasures_Stats.m). Reproduced when current-zone speed is lower in post-run than in\n    pre-run and current-zone speed is lower than previous-zone speed in run and in post-run, each\n    by paired t-test at p < 0.05/4 (O5 reading a) or p < 0.05 (reading b); partially reproduced\n    when the post-run against pre-run test holds and one of the other two does not.\n- id: puff-location-no-speed-bias\n  statement: The location of the air puff on the track does not correlate with the speed in the\n    current danger zone in pre-run, run or post-run.\n  source: Results, Rats learn the daily location of an aversive air puff on a linear track,\n    paragraph 2\n  quote: The location of the air puff on the track did not correlate with the speed in the\n    current danger zone in pre-run, training or post-run\n  depends_on:\n  - rats-learn-puff-location\n  criterion: A claim of absence. The text names no test; the code computes Pearson correlations\n    (corrcoef) across sessions between the air puff location normalised to the track (0 to 1,\n    flipped for right-to-left days so that 0 is the start of the air puff run) and the\n    current-zone speed of each epoch (AirpuffPositionDistribution_Plot.m). Reproduced when none of\n    the three correlations has p < 0.05; not reproduced when any does. The code's second measure,\n    the distance of the location from the track centre, is shown as a variant. r is reported.\n- id: habituation-over-days\n  statement: The aversive valence of the air puff diminishes over training days; rats run more laps\n    per unit time as they habituate.\n  source: Results, Rats learn the daily location of an aversive air puff on a linear track,\n    paragraph 2; Supplementary Fig. 1c\n  quote: The aversive valence of the air puff gradually diminished with training days\n    (Supplementary Fig. 1c).\n  criterion: Habituation index per training session = laps / time on the track x 100 (Online\n    Methods; Performance.m counts left-to-right laps over the run epoch duration). The laps\n    counted are open between the Methods (\"back-and-forth laps\"), the Supplementary Fig. 1c\n    legend (\"airpuff laps\") and the code (left-to-right laps); all three are run. The paper shows\n    the index per day for each rat and gives no test. Readings of \"gradually diminished\" (a) a\n    Spearman correlation between the training day rank within the rat and the index, sessions of\n    all rats pooled, positive with p < 0.05; (b) a positive Spearman correlation in at least 3 of\n    the 4 rats. Reproduced when the outcome holds under every reading; otherwise reported as\n    methods_underspecified with all results.\n- id: bla-pyr-sleep-firing-increase\n  statement: BLA pyramidal cells fire faster in REM sleep and, to a lesser extent, in NREM sleep\n    than in wakefulness.\n  source: Results, BLA recordings and sleep physiology, paragraph 1; Figure 2c\n  quote: we found a specific increase in the firing rate of BLA pyramidal cells, but not\n    interneurons, during REM sleep and, to a lesser extent, NREM sleep relative to wakefulness\n  statistics:\n  - about: NREM/wake firing rate ratio of BLA pyramidal cells\n    test: Wilcoxon signed rank test\n    statistic: z = 14.25\n    p: 4.07e-46\n    n: 675 monosynaptically identified pyramidal cells\n  - about: REM/wake firing rate ratio of BLA pyramidal cells\n    test: Wilcoxon signed rank test\n    statistic: z = 13.54\n    p: 8e-42\n    n: 675 monosynaptically identified pyramidal cells\n  criterion: Per BLA pyramidal cell, firing rates over all REM, all NREM and all wake intervals of\n    the session (StatesFiringRates.m); ratios (REM - wake)/(REM + wake) and (NREM - wake)/(NREM +\n    wake) (Online Methods). A two-sided Wilcoxon signed rank test of each ratio against 0. Cells\n    per O4. Reproduced when both ratios have a positive median with p < 0.05 and the REM median\n    exceeds the NREM median; partially reproduced when both are positive and significant but the\n    REM median does not exceed the NREM median.\n- id: bla-int-sleep-firing\n  statement: BLA interneurons do not change their firing rate between REM sleep and wake, and fire\n    slightly less in NREM sleep than in wake.\n  source: Figure 2c legend\n  quote: Interneurons do not change firing rates between REM and wake ... and slightly decrease\n    firing rates during NREM compared to wake\n  statistics:\n  - about: REM/wake firing rate ratio of BLA interneurons\n    test: Wilcoxon signed rank test\n    statistic: z = 1.25\n    p: 0.21\n    n: 175 monosynaptically identified interneurons\n  - about: NREM/wake firing rate ratio of BLA interneurons\n    test: Wilcoxon signed rank test\n    statistic: z = -6.00\n    p: 1.97e-9\n    n: 175 monosynaptically identified interneurons\n  criterion: As bla-pyr-sleep-firing-increase, for BLA interneurons (cells per O4). The REM part\n    is a claim of absence judged on the paper's test, a two-sided Wilcoxon signed rank test of the\n    REM/wake ratio against 0 at p < 0.05. Reproduced when that test does not reach p < 0.05 and\n    the NREM/wake ratio has a negative median with p < 0.05; partially reproduced when only one\n    of the two holds.\n- id: hpc-bla-reactivation-post-sleep\n  statement: Hippocampus-BLA pyramidal cell pair correlations of the run are reinstated in\n    post-sleep NREM, measured as explained variance (EV) exceeding the reverse explained variance\n    (REV) across sessions.\n  source: Results, BLA-hippocampus coordinated reactivations during NREM sleep, paragraph 1;\n    Figure 3a-c\n  quote: The EV and REV, calculated using hippocampus–BLA pyramidal cell pairs, showed significant\n    reactivations between the hippocampus and BLA during post-NREM (Fig. 3c).\n  statistics:\n  - about: EV against REV, NREM, pyramidal pairs\n    test: Wilcoxon signed rank test\n    statistic: z = 3.72\n    p: 0.00019\n    n: 25 sessions in 3 rats\n  expected:\n  - quantity: mean EV - REV over sessions, hippocampus-BLA pyramidal pairs, NREM\n    value: 3.13\n    tolerance: 0.73\n    unit: percent\n  - quantity: sessions entering\n    value: 25\n    tolerance: 2.5\n  criterion: EV and REV per session (M4) over hippocampal and BLA pyramidal cells, NREM bins of\n    pre- and post-sleep (M2, M3). A two-sided Wilcoxon signed rank test of EV against REV across\n    sessions (Online Methods, Statistical analysis; ExplainedVarianceMean_Ultimate.m). Reproduced\n    when EV exceeds REV with p < 0.05 and the expected values hold (the mean EV - REV of 3.13 +-\n    0.73% s.e.m. is from Results, A subset of BLA cells, paragraph 1, Fig. 3d test); partially\n    reproduced when the test holds and an expected value does not.\n- id: reactivation-all-cell-pairs\n  statement: Hippocampus-BLA NREM reactivation holds when pyramidal cells and interneurons are both\n    included.\n  source: Results, BLA-hippocampus coordinated reactivations during NREM sleep, paragraph 1;\n    Supplementary Fig. 5a\n  quote: Reactivations were maintained when both pyramidal cells and interneurons were included in\n    the EV calculation (Supplementary Fig. 5).\n  statistics:\n  - about: EV against REV, NREM, all cell pairs\n    test: Wilcoxon signed rank test\n    statistic: z = 3.79\n    p: 0.00014\n    n: 27 sessions in 3 rats\n  - about: EV against REV over the first, second and third 20 min of NREM, all cell pairs\n    test: Wilcoxon signed rank tests\n    statistic: z = 3.91; z = 2.98; z = -0.71\n    p: 8.85e-5\n    n: 17 sessions in 3 rats\n  criterion: As hpc-bla-reactivation-post-sleep with all hippocampal and BLA units. Reproduced when\n    EV exceeds REV with two-sided Wilcoxon signed rank p < 0.05 across sessions. The 20-min\n    epochs are reported as in reactivation-decay.\n- id: reactivation-decay\n  statement: Hippocampus-BLA reactivation decays over the first hour of post-sleep NREM (mean EV -\n    REV 2.89, 1.72 and 1.31% in successive 20-min NREM periods).\n  source: Results, BLA-hippocampus coordinated reactivations during NREM sleep, paragraph 1;\n    Figure 3c, right\n  quote: The gradual decay in reactivations over the first hour of NREM sleep ... paralleled the\n    previously described decay for pairs of hippocampal neurons\n  statistics:\n  - about: EV - REV across the three 20-min NREM periods\n    test: Kruskal-Wallis test\n    statistic: chi2 = 8.53, d.f. = 2\n    p: 0.014\n    n: 19 sessions\n  - about: EV against REV, 0-20 min of post-NREM\n    test: Wilcoxon signed rank test\n    statistic: z = 0.38 (as printed)\n    p: 0.00013\n    n: 19 sessions in 3 rats\n  - about: EV against REV, 20-40 min\n    test: Wilcoxon signed rank test\n    statistic: z = 3.5\n    p: 0.00046\n    n: 19 sessions in 3 rats\n  - about: EV against REV, 40-60 min\n    test: Wilcoxon signed rank test\n    statistic: z = 2.15\n    p: 0.0312\n    n: 19 sessions in 3 rats\n  expected:\n  - quantity: mean EV - REV, 0-20 min of post-NREM\n    value: 2.89\n    tolerance: 0.47\n    unit: percent\n  - quantity: mean EV - REV, 20-40 min\n    value: 1.72\n    tolerance: 0.44\n    unit: percent\n  - quantity: mean EV - REV, 40-60 min\n    value: 1.31\n    tolerance: 0.60\n    unit: percent\n  - quantity: sessions with EV > REV in the first 20 min\n    value: 19\n    tolerance: 1.9\n  depends_on:\n  - hpc-bla-reactivation-post-sleep\n  criterion: Pyramidal pairs, sessions of hpc-bla-reactivation-post-sleep. The post-NREM bins are\n    concatenated in time order and cut into the first 24,000 bins (20 min), the next 24,000, and\n    the next 24,000 or what remains when fewer; each period's EV and REV use the whole pre-NREM\n    and the run (ExplainedVariance_Ultimate.m). Only sessions with EV > REV in the first period\n    enter (Online Methods). A Kruskal-Wallis test of EV - REV across the three periods (Results)\n    and two-sided Wilcoxon signed rank tests of EV against REV in each period. Reproduced when the\n    Kruskal-Wallis p < 0.05 with the means falling from the first to the third period and the\n    expected values hold; partially reproduced when the means fall and the test or an expected\n    value fails.\n- id: no-rem-reactivation\n  statement: Hippocampus-BLA reactivations are not significant in REM sleep.\n  source: Results, BLA-hippocampus coordinated reactivations during NREM sleep, paragraph 2;\n    Figure 3c, left\n  quote: Reactivations during REM sleep ... were not significant in any structure\n  statistics:\n  - about: EV against REV, REM, pyramidal pairs\n    test: Wilcoxon signed rank test\n    statistic: z = 0.88\n    p: 0.377\n    n: 23 sessions in 3 rats\n  - about: EV against REV, REM, all cell pairs (Supplementary Fig. 5a)\n    test: Wilcoxon signed rank test\n    statistic: z = -0.71\n    p: 0.47583\n    n: 25 sessions in 3 rats\n  criterion: A claim of absence, judged on the paper's test. EV and REV (M4) from the REM bins of\n    pre- and post-sleep, sessions with more than 180 s of REM in each, pyramidal pairs; two-sided\n    Wilcoxon signed rank test of EV against REV. Reproduced when p >= 0.05, not reproduced when\n    p < 0.05; the median EV - REV is reported. All cell pairs shown as a variant.\n- id: piriform-weaker-reactivation\n  statement: Piriform cortex neurons show weaker reactivation with hippocampal CA1 neurons than BLA\n    neurons do, though still significant in NREM.\n  source: Results, BLA-hippocampus coordinated reactivations during NREM sleep, paragraph 2;\n    Figure 3d\n  quote: Neurons in the piriform cortex showed weaker experience-induced ... reactivation with\n    their CA1 partner neurons (Fig. 3d\n  statistics:\n  - about: EV - REV, hippocampus-BLA against hippocampus-piriform\n    test: Wilcoxon one-tailed rank sum test\n    statistic: z = 2.38\n    p: 0.0092\n    n: 25 hippocampus-BLA and 14 hippocampus-piriform sessions\n  - about: EV against REV, hippocampus-piriform, NREM, pyramidal pairs\n    test: Wilcoxon signed rank test\n    p: 0.0052\n    n: 17 sessions\n  expected:\n  - quantity: mean EV - REV, hippocampus-piriform\n    value: 0.85\n    tolerance: 0.34\n    unit: percent\n  depends_on:\n  - hpc-bla-reactivation-post-sleep\n  criterion: EV and REV (M4) for hippocampus-piriform pyramidal pairs, piriform units as the\n    paper's maps label them (M1). Reproduced when EV - REV of hippocampus-BLA sessions exceeds that\n    of hippocampus-piriform sessions by one-tailed Wilcoxon rank sum p < 0.05, the\n    hippocampus-piriform EV exceeds REV by two-sided signed rank p < 0.05, and the expected value\n    holds. Partially reproduced when the comparison holds and one of the others does not. The\n    paper gives 14 sessions for the comparison and 17 for Fig. 3d; both session sets are shown.\n- id: cen-no-reactivation\n  statement: There are no reactivations between the central amygdala nuclei and the hippocampus.\n  source: Results, BLA-hippocampus coordinated reactivations during NREM sleep, paragraph 2;\n    Figure 3e\n  quote: while there were no reactivations at all between the central nuclei and the hippocampus\n    (Fig. 3e)\n  statistics:\n  - about: EV against REV, NREM, all cell pairs\n    test: Wilcoxon signed rank test\n    statistic: z = 0.36\n    p: 0.717\n    n: 19 sessions in 3 rats\n  - about: EV against REV, REM, all cell pairs\n    test: Wilcoxon signed rank test\n    statistic: z = -0.40\n    p: 0.687\n    n: 19 sessions in 3 rats\n  criterion: A claim of absence, judged on the paper's test. EV and REV (M4) for all\n    hippocampus-central nuclei cell pairs; two-sided Wilcoxon signed rank of EV against REV in NREM\n    and in REM. Reproduced when neither has p < 0.05 with EV above REV; not reproduced when either\n    does. Medians reported.\n- id: intra-structure-reactivation\n  statement: Within the hippocampus and within the BLA, pair correlations are reactivated in NREM\n    but not in REM sleep.\n  source: Supplementary Fig. 4; Results, BLA-hippocampus coordinated reactivations during NREM\n    sleep, paragraph 1\n  quote: Intra-structure reactivations for hippocampus and BLA.\n  statistics:\n  - about: hippocampus, all pairs, NREM\n    test: Wilcoxon signed rank test\n    statistic: z = 3.95\n    p: 7.75e-5\n    n: 38 sessions in 3 rats\n  - about: hippocampus, pyramidal pairs, NREM\n    test: Wilcoxon signed rank test\n    statistic: z = 3.99\n    p: 6.45e-5\n    n: 38 sessions in 3 rats\n  - about: BLA, all pairs, NREM\n    test: Wilcoxon signed rank test\n    statistic: z = 2.74\n    p: 0.00606\n    n: 34 sessions in 4 rats\n  - about: BLA, pyramidal pairs, NREM\n    test: Wilcoxon signed rank test\n    statistic: z = 3.16\n    p: 0.00157\n    n: 32 sessions in 4 rats\n  - about: hippocampus, all pairs, REM\n    test: Wilcoxon signed rank test\n    statistic: z = 0.04\n    p: 0.965\n    n: 34 sessions in 3 rats\n  - about: hippocampus, pyramidal pairs, REM\n    test: Wilcoxon signed rank test\n    statistic: z = -0.67\n    p: 0.499\n    n: 34 sessions in 3 rats\n  - about: BLA, all pairs, REM\n    test: Wilcoxon signed rank test\n    statistic: z = 0.84\n    p: 0.39948\n    n: 28 sessions in 4 rats\n  - about: BLA, pyramidal pairs, REM\n    test: Wilcoxon signed rank test\n    statistic: z = 1.40\n    p: 0.158\n    n: 26 sessions in 4 rats\n  criterion: EV and REV (M4) over the distinct pairs within one structure (upper triangle of the\n    correlation matrix, ExplainedVariance_Ultimate_IntraStruct.m), for all cells and for pyramidal\n    cells, NREM and REM (REM sessions per M4). Two-sided Wilcoxon signed rank of EV against REV.\n    Reproduced when all four NREM tests have EV above REV at p < 0.05 and none of the four REM\n    tests reaches p < 0.05 (absence on the paper's test); partially reproduced when the NREM tests\n    hold and a REM test does not, or three of four NREM tests hold.\n- id: bla-ripple-up-subgroup\n  statement: A subset of BLA neurons is positively modulated during hippocampal SPW-Rs, 25.8% of\n    interneurons (42 of 163) and 11.1% of pyramidal cells (137 of 1,233).\n  source: Results, A subset of BLA cells are modulated during hippocampal SPW-Rs, paragraph 1;\n    Figure 4a\n  quote: A fraction of BLA neurons were significantly and positively modulated (‘upmodulation’; 42\n    of 163 interneurons (25.8%), 137 of 1,233 pyramidal cells (11.1%)) ... during hippocampal\n    SPW-Rs (Fig. 4).\n  expected:\n  - quantity: upmodulated BLA interneurons\n    value: 25.8\n    tolerance: 2.58\n    unit: percent\n  - quantity: upmodulated BLA pyramidal cells\n    value: 11.1\n    tolerance: 1.11\n    unit: percent\n  - quantity: BLA interneurons tested\n    value: 163\n    tolerance: 16.3\n  - quantity: BLA pyramidal cells tested\n    value: 1233\n    tolerance: 123.3\n  criterion: M6 for every BLA unit of the sessions with ripple events (29 sessions, 3 rats, Fig. 4a\n    legend), under both readings of O2; denominators are the BLA pyramidal cells and interneurons\n    of those sessions (PoissonRippleModPercent.m counts all typed BLA cells in the table). An\n    untested unit (no spikes in ripples or baseline) counts in the denominator as not modulated;\n    the fractions excluding untested units are shown as a variant. Reproduced when both fractions\n    are within tolerance; partially reproduced when both are above 0 and one is outside it.\n- id: bla-ripple-down-subgroup\n  statement: Another subset of BLA neurons is negatively modulated during hippocampal SPW-Rs, 14.7%\n    of interneurons (24 of 163) and 8.3% of pyramidal cells (102 of 1,233).\n  source: Results, A subset of BLA cells are modulated during hippocampal SPW-Rs, paragraph 1;\n    Figure 4a\n  quote: or negatively modulated (‘downmodulation’; 24 of 163 interneurons (14.7%), 102 of 1,233\n    pyramidal cells (8.3%)) during hippocampal SPW-Rs (Fig. 4)\n  expected:\n  - quantity: downmodulated BLA interneurons\n    value: 14.7\n    tolerance: 1.47\n    unit: percent\n  - quantity: downmodulated BLA pyramidal cells\n    value: 8.3\n    tolerance: 0.83\n    unit: percent\n  depends_on:\n  - bla-ripple-up-subgroup\n  criterion: As bla-ripple-up-subgroup, for the lower tail. Reproduced when both fractions are\n    within tolerance; partially reproduced when both are above 0 and one is outside it.\n- id: ripple-modulated-cells-larger-reactivation\n  statement: Reactivation (EV - REV) is larger for hippocampus-BLA pairs whose BLA cell is\n    ripple-modulated than for pairs with a non-modulated BLA cell.\n  source: Results, A subset of BLA cells are modulated during hippocampal SPW-Rs, paragraph 1;\n    Supplementary Fig. 5b\n  quote: Moreover, reactivations calculated using SPW-R-modulated BLA cells were larger than for\n    nonmodulated pairs (Supplementary Fig. 5b).\n  statistics:\n  - about: EV - REV, ripple-modulated against non-modulated BLA partners, all cells\n    test: Wilcoxon ranksum test\n    statistic: z = 2.71\n    p: 0.00662\n    n: 19 sessions in 3 rats\n  - about: EV - REV, ripple-modulated against non-modulated BLA partners, pyramidal pairs\n    test: Wilcoxon ranksum test\n    statistic: z = 2.57\n    p: 0.00992\n    n: 18 sessions in 3 rats\n  expected:\n  - quantity: mean EV - REV, ripple-modulated BLA partner, all cells\n    value: 6.07\n    tolerance: 1.3\n    unit: percent\n  - quantity: mean EV - REV, non-modulated BLA partner, all cells\n    value: 1.76\n    tolerance: 0.56\n    unit: percent\n  - quantity: mean EV - REV, ripple-modulated BLA partner, pyramidal pairs\n    value: 7.16\n    tolerance: 2.19\n    unit: percent\n  - quantity: mean EV - REV, non-modulated BLA partner, pyramidal pairs\n    value: 1.90\n    tolerance: 0.71\n    unit: percent\n  depends_on:\n  - bla-ripple-up-subgroup\n  - hpc-bla-reactivation-post-sleep\n  criterion: Per session, EV and REV (M4) computed twice, with the BLA cells that are up- or\n    downmodulated (M6) and with the non-modulated BLA cells; a session enters when it has more\n    than 5 hippocampal and more than 5 modulated BLA cells of the type used\n    (ExplainedVarianceMean_Ultimate.m). A two-sided Wilcoxon rank sum test on EV - REV of the two\n    sets, as the paper names it (Supplementary Fig. 5b legend); the signed rank test on the same\n    sessions is shown as a variant. Reproduced when, for all cells and for pyramidal pairs,\n    modulated exceeds non-modulated with p < 0.05; partially reproduced when one of the two holds.\n- id: run-correlated-pair-fractions\n  statement: During run, 6.69% of hippocampus-BLA pyramidal pairs (2,521 of 37,660) are\n    significantly positively correlated, 3.34% (1,258) negatively, and 89.96% (33,881) not\n    reliably correlated.\n  source: Results, Ripple-modulated BLA cells are preferentially involved in reactivations,\n    paragraph 1; Supplementary Table 2\n  quote: During run, a fraction of hippocampal–BLA pyramidal neuron pairs showed significantly\n    positively correlated spike trains (2,521 of 37,660; 6.69%). Another small percentage (1,258\n    of 37,660; 3.34%) was negatively correlated, while the remaining majority (33,881 of 37,660;\n    89.96%) was not reliably correlated\n  expected:\n  - quantity: hippocampus-BLA pyramidal pairs, all sessions pooled\n    value: 37660\n    tolerance: 3766\n  - quantity: pairs, rat 1\n    value: 16056\n    tolerance: 1605.6\n  - quantity: pairs, rat 3\n    value: 3836\n    tolerance: 383.6\n  - quantity: pairs, rat 4\n    value: 17768\n    tolerance: 1776.8\n  - quantity: positively correlated pairs\n    value: 6.69\n    tolerance: 0.669\n    unit: percent\n  - quantity: negatively correlated pairs\n    value: 3.34\n    tolerance: 0.334\n    unit: percent\n  - quantity: not reliably correlated pairs\n    value: 89.96\n    tolerance: 8.996\n    unit: percent\n  criterion: All hippocampus-BLA pyramidal pairs of the 29 sessions with simultaneous recordings\n    and ripple events (Supplementary Fig. 6a legend; ExplainedVariance_PrePostCorr_Ultimate.m has\n    no cell minimum), pooled. Run correlation is the Pearson correlation of 50-ms binned counts\n    over the whole run epoch; positive when p < 0.01 and r > 0, negative when p < 0.01 and r < 0,\n    otherwise not reliably correlated (Online Methods; the code's isnosig is p >= 0.01). Pairs\n    with an undefined correlation (a silent cell) are left out of the fractions. Reproduced when\n    every expected value holds; partially reproduced when the three fractions hold and a pair\n    count does not.\n- id: reactivation-involves-ripple-up-cells\n  statement: Among nine groups of hippocampus-BLA pyramidal pairs formed by run correlation and BLA\n    ripple modulation, the pairs with a significant positive run correlation and an upmodulated BLA\n    partner show the largest pre-NREM to post-NREM increase in correlation, and differ from every\n    other group.\n  source: Results, Ripple-modulated BLA cells are preferentially involved in reactivations,\n    paragraph 1; Figure 5a; Supplementary Fig. 6a; Supplementary Table 2\n  quote: Hippocampus–BLA pairs with significant, positive run correlations and SPW-R upmodulation\n    of the BLA partner showed the largest pre-NREM to post-NREM change\n  statistics:\n  - about: the nine groups of pairs by run correlation and BLA ripple modulation\n    test: one-way ANOVA\n    statistic: F = 29.09, d.f. = 8\n    p: 1.1e-45\n    n: 37,660 pairs in 3 rats\n  - about: the upmodulated, positively correlated group against the other groups\n    test: post hoc comparisons\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Tukey-Kramer (Fig. 5a legend, which gives P < 0.01; the Online Methods say Bonferroni)\n  expected:\n  - quantity: pairs, upmodulated BLA partner and positive run correlation\n    value: 595\n    tolerance: 59.5\n  - quantity: pairs, upmodulated and non-significant\n    value: 3686\n    tolerance: 368.6\n  - quantity: pairs, upmodulated and negative\n    value: 334\n    tolerance: 33.4\n  - quantity: pairs, non-modulated and positive\n    value: 1774\n    tolerance: 177.4\n  - quantity: pairs, non-modulated and non-significant\n    value: 28087\n    tolerance: 2808.7\n  - quantity: pairs, non-modulated and negative\n    value: 801\n    tolerance: 80.1\n  - quantity: pairs, downmodulated and positive\n    value: 152\n    tolerance: 15.2\n  - quantity: pairs, downmodulated and non-significant\n    value: 2108\n    tolerance: 210.8\n  - quantity: pairs, downmodulated and negative\n    value: 123\n    tolerance: 12.3\n  depends_on:\n  - bla-ripple-up-subgroup\n  - run-correlated-pair-fractions\n  criterion: The pairs and run-correlation classes of run-correlated-pair-fractions, crossed with\n    the BLA partner's ripple modulation (M6, both O2 readings). Per pair, post-NREM correlation\n    minus pre-NREM correlation (Pearson, 50-ms bins, M2). A one-way ANOVA across the nine groups,\n    then post hoc comparisons (ExplainedVariance_PrePostCorr_Ultimate.m, anova1 and multcompare).\n    Post hoc correction per O6, Bonferroni over the 36 pairwise comparisons (main) and\n    Tukey-Kramer (variant). Reproduced when the ANOVA has p < 0.05, the upmodulated positive group\n    has the largest mean, and it differs from each of the other eight groups at p < 0.01 after\n    correction; partially reproduced when it has the largest mean and differs from at least five.\n    The group counts are reported against Supplementary Table 2.\n- id: pair-group-ev\n  statement: EV computed within each of the nine pair groups confirms the dominant contribution of\n    the pairs with positive run correlation and an upmodulated BLA partner.\n  source: Results, Ripple-modulated BLA cells are preferentially involved in reactivations,\n    paragraph 1; Supplementary Fig. 6b\n  quote: The dominant contribution of this specific subgroup of cell pairs to reactivations was\n    confirmed by calculating the EVs across the nine subgroups\n  depends_on:\n  - reactivation-involves-ripple-up-cells\n  criterion: For each group of reactivation-involves-ripple-up-cells, EV and REV (M4 formula) over\n    the pooled pairs of the group, with pre-NREM, run and post-NREM correlations\n    (ExplainedVariance_PooledCorr_Groups.m). The paper gives no test. Reproduced when the\n    upmodulated positive group has the largest EV - REV of the nine. In the code the\n    non-significant group is restricted to negative run correlations (run.signot); the Methods\n    define it by p > 0.01 alone, so the Methods' groups are the main reading and the code's the\n    variant.\n- id: contributing-up-cells-gain-increase\n  statement: Upmodulated BLA cells in the quartile contributing most to the reactivation increase\n    their SPW-R gain from pre-NREM to post-NREM, while upmodulated cells of the other three\n    quartiles do not.\n  source: Results, Ripple-modulated BLA cells are preferentially involved in reactivations,\n    paragraph 2; Figure 5b; Supplementary Fig. 8a\n  quote: We found that upmodulated BLA neurons in the most strongly contributing quartile showed a\n    specific increase in SPW-R gain (that is, firing rate during versus outside SPW-R) from\n    pre-NREM to post-NREM compared to the upmodulated cells of the remaining three,\n    low-contribution quartiles\n  statistics:\n  - about: post-NREM against pre-NREM gain, upmodulated cells of the highest-contribution quartile\n    test: Wilcoxon one-tail signed rank test\n    statistic: z = -3.913\n    p: 4.57e-5\n    n: 63 cells in 3 rats\n  - about: the same, upmodulated cells of the remaining three quartiles\n    test: Wilcoxon one-tail signed rank test\n    statistic: z = 2.408\n    p: 0.992\n    n: 73 cells in 3 rats\n  - about: second, third and fourth quartiles separately (Supplementary Fig. 8a)\n    test: Wilcoxon signed rank one-tailed tests\n    statistic: z = 0.7839; z = 1.8873; z = 1.5420\n    p: 0.7834\n    n: 18, 16 and 39 cells\n  depends_on:\n  - bla-ripple-up-subgroup\n  - run-correlated-pair-fractions\n  expected:\n  - quantity: upmodulated BLA cells, highest-contribution quartile\n    value: 63\n    tolerance: 6.3\n  - quantity: upmodulated BLA cells, remaining quartiles\n    value: 73\n    tolerance: 7.3\n  criterion: Contribution of a pair (Online Methods; ExplainedVariance_PooledCorr.m). Over all\n    pooled pyramidal pairs with defined pre-NREM, run and post-NREM correlations, the global EV\n    (M4 formula on pooled pairs) and, for each pair, the EV with that pair removed; contribution =\n    EV without the pair minus global EV (negative is a positive contribution). A BLA cell's\n    contribution is the mean over its pairs; BLA cells are split at the quartiles, the highest\n    contribution quartile being the most negative. Gain (AllRippleCCGs_2.m, RippleMod_PrePost.m)\n    is the cell's peri-ripple firing in 10-ms bins over -2 to +2 s around ripple peaks of\n    pre-NREM, and of post-NREM, divided by the baseline rate of the same sleep epoch (NREM minus\n    ripples widened by 100 ms); cells with an all-zero or undefined gain in either epoch are\n    dropped; each curve is smoothed over 2 bins (the Methods' 20-ms Gaussian) and averaged over\n    -250 to +250 ms. A one-tailed Wilcoxon signed rank test (post greater than pre) in the\n    upmodulated cells (M6, both O2 readings) of the highest quartile and in those of the other\n    three. Reproduced when the highest quartile has p < 0.05 and the other three do not;\n    partially reproduced when the highest quartile has p < 0.05 and the other quartiles do too.\n- id: ev-independent-of-firing-rate\n  statement: Hippocampus-BLA EV does not depend on firing rates; EV exceeds REV across firing-rate\n    octiles of the pairs, of the BLA cells and of the hippocampal cells.\n  source: Results, Ripple-modulated BLA cells are preferentially involved in reactivations,\n    paragraph 2; Supplementary Fig. 9\n  quote: This control showed that EV did not depend on firing rates (Supplementary Fig. 9).\n  depends_on:\n  - run-correlated-pair-fractions\n  criterion: The pooled pyramidal pairs of run-correlated-pair-fractions, split into octiles of\n    (a) the mean of the two cells' rates, (b) the BLA cell's rate, (c) the hippocampal cell's\n    rate, rate being the spike count over the whole recording span of the scored states\n    (StatesFiringRates.m, all-states rate, used by ExplainedVariance_PooledCorr_Groups.m); EV and\n    REV (M4 formula) over the pairs of each octile. The paper gives no test. Readings of \"did not\n    depend\" (a) EV exceeds REV in all eight octiles of each of the three splits; (b) the Spearman\n    correlation between octile rank and EV - REV has p >= 0.05 in each split. Reproduced when\n    the outcome holds under both readings; otherwise reported as methods_underspecified with all\n    results.\n- id: reactivation-peaks-at-ripples\n  statement: Reactivation strength of the whole-run template around hippocampal ripple peaks is\n    higher in post-NREM than in pre-NREM, for pyramidal pairs and for all cell pairs.\n  source: Supplementary Fig. 11a\n  quote: Mean z-scored peri-ripple reactivation strength of the whole training session ...\n    reactivation strength in a 500ms window around ripple peaks (grey bar in a) was significantly\n    higher in post-NREM\n  statistics:\n  - about: post-NREM against pre-NREM ripple-peak reactivation strength, whole training session,\n      pyramidal cell pairs\n    test: Wilcoxon one-tailed signed rank test\n    statistic: z = -3.175\n    p: 7.49e-4\n    n: 25 sessions in 3 rats\n  - about: the same, all cell pairs\n    test: Wilcoxon one-tailed signed rank test\n    statistic: z = -2.895\n    p: 0.00189\n    n: 27 sessions in 3 rats\n  depends_on:\n  - hpc-bla-reactivation-post-sleep\n  criterion: R per M7 with the whole run epoch as template, pyramidal cells (and all cells as the\n    second test). Per session, the ripple-peak value in pre-NREM and in post-NREM; a one-tailed\n    Wilcoxon signed rank test, post greater than pre (ReplayInTime_All.m, tail left on pre\n    against post). Reproduced when both tests have p < 0.05; partially reproduced when one does.\n- id: airpuff-trajectory-ripple-reactivation\n  statement: The hippocampus-BLA correlation pattern of the air puff trajectory is reactivated more\n    around post-NREM ripples than around pre-NREM ripples.\n  source: Figure 6a, top; Results, The aversive trajectory is reactivated during SPW-Rs, paragraph 1\n  quote: reactivation strength in a 500-ms window around ripple peaks (gray bars) was significantly\n    higher in post-NREM compared to pre-NREM for air puff trajectory\n  statistics:\n  - about: post-NREM against pre-NREM ripple-peak reactivation strength, air puff trajectory,\n      pyramidal pairs\n    test: Wilcoxon one-tail signed rank test\n    statistic: z = -3.793\n    p: 7.42e-5\n    n: 25 sessions in 3 rats\n  depends_on:\n  - reactivation-peaks-at-ripples\n  criterion: R per M7, pyramidal cells, with the template built only from run bins inside air puff\n    laps (M8, each O1 reading), the run counts z-scored within those bins\n    (ReplayInTime_LapTypes.m). Per session, ripple-peak values in pre- and post-NREM; one-tailed\n    Wilcoxon signed rank test, post greater than pre (ReplayInTime_LapTypes_All.m). Reproduced\n    when p < 0.05 under every O1 reading; methods_underspecified when the readings disagree.\n- id: safe-trajectory-no-ripple-reactivation\n  statement: The hippocampus-BLA correlation pattern of the safe trajectory is not significantly\n    more reactivated around post-NREM ripples than around pre-NREM ripples (pyramidal pairs).\n  source: Figure 6a, bottom; Results, The aversive trajectory is reactivated during SPW-Rs,\n    paragraph 1\n  quote: significantly higher in post-NREM compared to pre-NREM for air puff trajectory ... but not\n    for safe trajectory\n  statistics:\n  - about: post-NREM against pre-NREM ripple-peak reactivation strength, safe trajectory,\n      pyramidal pairs\n    test: Wilcoxon one-tail signed rank test\n    statistic: z = -0.780\n    p: 0.217\n    n: 25 sessions in 3 rats\n  depends_on:\n  - airpuff-trajectory-ripple-reactivation\n  criterion: A claim of absence, judged on the paper's test. As\n    airpuff-trajectory-ripple-reactivation with the template built from run bins inside safe laps.\n    Reproduced when the one-tailed Wilcoxon signed rank test (post greater than pre) has\n    p >= 0.05; not reproduced when p < 0.05. The median post minus pre difference is reported. The\n    O1 readings are each run and reported; absence is judged on each.\n- id: aversive-direction-stronger\n  statement: The post-NREM minus pre-NREM change in reactivation strength at the ripple peak is\n    larger for the air puff trajectory than for the safe trajectory (pyramidal pairs).\n  source: Figure 6b; Results, The aversive trajectory is reactivated during SPW-Rs, paragraph 1\n  quote: The pre-NREM vs. post-NREM difference in reactivation strength (RS) at the ripple peak is\n    significantly higher for the air puff trajectory compared to safe trajectory\n  statistics:\n  - about: post-NREM minus pre-NREM ripple-peak reactivation strength, air puff against safe\n      trajectory\n    test: Wilcoxon one-tail signed rank-test\n    statistic: z = -2.798\n    p: 0.00257\n    n: 25 sessions\n  depends_on:\n  - airpuff-trajectory-ripple-reactivation\n  - safe-trajectory-no-ripple-reactivation\n  criterion: Per session, the post-NREM minus pre-NREM ripple-peak value (M7) for the air puff\n    template and for the safe template of the two claims above. One-tailed Wilcoxon signed rank\n    test across sessions, air puff greater than safe (ReplayInTime_LapTypes_Plot.m, signrank of\n    safe against air puff, tail left). Reproduced when p < 0.05 under every O1 reading;\n    methods_underspecified when the readings disagree.\n- id: direction-all-cell-pairs\n  statement: With all cell types included, both the air puff and the safe trajectory patterns are\n    more reactivated around post-NREM than pre-NREM ripples, and the post minus pre difference does\n    not differ significantly between the two trajectories.\n  source: Supplementary Fig. 11b,c\n  quote: Reactivation strength in a 500ms window around ripple peaks (grey bar in a) was\n    significantly higher in post-NREM compared to pre-NREM for airpuff ... and safe trajectories\n    ... Pre/Post peak differences (postNREM - preNREM; see methods) in reactivation strength are\n    not significantly different for safe and airpuff trajectories when all cell types are included\n  statistics:\n  - about: post-NREM against pre-NREM, air puff trajectory, all cell pairs\n    test: Wilcoxon one-tail signed rank test\n    statistic: z = -3.327\n    p: 4.38e-4\n    n: 27 sessions in 3 rats\n  - about: post-NREM against pre-NREM, safe trajectory, all cell pairs\n    test: Wilcoxon one-tail signed rank test\n    statistic: z = -1.789\n    p: 0.036\n    n: 27 sessions in 3 rats\n  - about: post minus pre difference, air puff against safe, all cell pairs\n    test: Wilcoxon one-tailed signed rank test\n    statistic: z = -1.333\n    p: 0.0912\n    n: 27 sessions in 3 rats\n  depends_on:\n  - aversive-direction-stronger\n  criterion: The three tests of airpuff-trajectory-ripple-reactivation,\n    safe-trajectory-no-ripple-reactivation and aversive-direction-stronger with all cells (ctype\n    all). Reproduced when both within-trajectory tests have p < 0.05 and the between-trajectory\n    test has p >= 0.05 (absence on the paper's one-tailed test); partially reproduced when two of\n    the three hold.\n- id: bla-rate-same-across-directions\n  statement: Firing rates of BLA cells do not differ significantly between the safe and the air\n    puff trajectories.\n  source: Results, The aversive trajectory is reactivated during SPW-Rs, paragraph 1\n  quote: Because the firing rates of BLA cells did not significantly differ between safe and air\n    puff trajectories\n  statistics:\n  - about: BLA pyramidal cells\n    test: Wilcoxon signed rank test\n    statistic: z = 1.101\n    p: 0.270\n  - about: all BLA cells\n    test: Wilcoxon signed rank test\n    statistic: z = 0.302\n    p: 0.763\n  criterion: A claim of absence, judged on the paper's test, a two-sided Wilcoxon signed rank test\n    across BLA cells of the sessions entering aversive-direction-stronger, safe against air puff\n    rate in the run epoch, for pyramidal cells and for all cells. The rate per O7, both readings,\n    laps per O1. Reproduced when neither test has p < 0.05; not reproduced when either does under\n    every reading. Median differences reported.\n- id: ripple-rate-unchanged\n  statement: The occurrence rate of SPW-Rs does not differ between pre-NREM and post-NREM.\n  source: Results, The aversive trajectory is reactivated during SPW-Rs, paragraph 1;\n    Supplementary Fig. 11d\n  quote: The occurrence rate of SPW-R was also not significantly different between the pre-NREM\n    and postNREM epochs\n  statistics:\n  - test: Wilcoxon signed rank test\n    statistic: z = -1.289\n    p: 0.192\n    n: 41 sessions in 3 rats\n  criterion: A claim of absence, judged on the paper's test. Per session with ripple events, the\n    number of ripple peaks in pre-NREM over pre-NREM duration and the same in post-NREM\n    (RippleRatePrePost.m). A two-sided Wilcoxon signed rank test (Online Methods default; the\n    printed P of 0.192 for z = -1.289 is two-sided, while RippleRatePrePost_All.m calls tail\n    right). Reproduced when p >= 0.05; not reproduced when p < 0.05. Median difference reported.\n- id: contributing-pairs-run-sleep-coupling\n  statement: For the 2.5% most strongly contributing hippocampus-BLA pairs, the pre-run to post-run\n    change in correlation correlates with the pre-NREM to post-NREM change (r = 0.27), but not for\n    the 2.5% least contributing pairs.\n  source: Results, NREM contributes to reinstatement of new place-threat representations,\n    paragraph 1; Figure 7b; Supplementary Fig. 7c\n  quote: We found that for strongly contributing, but not for weakly contributing, pairs the\n    increase between pre-run and post-run coactivity was significantly correlated with the\n    increase in coactivity between pre-NREM and post-NREM (Fig. 7b).\n  statistics:\n  - about: strongly contributing pairs (2.5% highest contributions)\n    test: Pearson correlation\n    statistic: r = 0.27\n    p: 2.11e-16\n    n: 866 pairs, 3 rats\n  - about: weakly contributing pairs (2.5% lowest contributions)\n    test: Pearson correlation\n    statistic: r = 0.03\n    p: 0.305\n    n: 845 pairs, 3 rats\n  expected:\n  - quantity: Pearson r, strongly contributing pairs\n    value: 0.27\n    tolerance: 0.027\n  - quantity: strongly contributing pairs with defined run changes\n    value: 866\n    tolerance: 86.6\n  - quantity: weakly contributing pairs with defined run changes\n    value: 845\n    tolerance: 84.5\n  depends_on:\n  - contributing-up-cells-gain-increase\n  criterion: Pair contributions as in contributing-up-cells-gain-increase. Strongly contributing\n    pairs are those below the 2.5th percentile of contribution (most negative), weakly\n    contributing those above the 97.5th (ExplainedVariance_PooledCorr.m, prctile 2.5 and 97.5).\n    Per pair, post-NREM minus pre-NREM correlation, and post-run minus pre-run correlation\n    (Pearson, 50-ms bins over the pre-run and post-run test epochs); pairs with an undefined run\n    change left out. Pearson correlation of the two changes in each group. Reproduced when the\n    strong group has r > 0 with p < 0.05 and r within tolerance, and the weak group has p >= 0.05;\n    partially reproduced when the strong group's r is positive and significant but outside\n    tolerance, or the weak group's p < 0.05.\n- id: contributing-quartiles-run-sleep-coupling\n  statement: The coupling between run and sleep correlation changes holds when the most and least\n    contributing quartiles of pairs are compared (r = 0.13 against r = 0.013).\n  source: Results, NREM contributes to reinstatement of new place-threat representations,\n    paragraph 1; Figure 7c; Supplementary Fig. 7b\n  quote: This result was maintained when the most strongly and the most weakly contributing\n    quartiles (instead of 2.5th percentiles) of the distribution were compared (Fig. 7c).\n  statistics:\n  - about: most strongly contributing quartile\n    test: Pearson correlation\n    statistic: r = 0.13\n    p: 1.07e-32\n    n: 9,415 pairs, 3 rats\n  - about: least contributing quartile\n    test: Pearson correlation\n    statistic: r = 0.013\n    p: 0.22\n    n: 9,415 pairs, 3 rats\n  expected:\n  - quantity: Pearson r, strongest quartile\n    value: 0.13\n    tolerance: 0.013\n  - quantity: pairs per quartile\n    value: 9415\n    tolerance: 941.5\n  depends_on:\n  - contributing-pairs-run-sleep-coupling\n  criterion: As contributing-pairs-run-sleep-coupling with the pairs split at the 25th and 75th\n    percentiles of contribution (quantile), strongest quartile below the 25th. Reproduced when the\n    strongest quartile has r > 0 with p < 0.05 and r within tolerance, and the weakest has\n    p >= 0.05; partially reproduced when only the strongest quartile's test holds.\n"
}
```

```
The file claims/000061/10.1038-nn.4637.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000061/10.1038-nn.4637.yaml paper/10.1038-nn.4637.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/^    p: 8e-42$/    p: 8.0e-42/' claims/000061/10.1038-nn.4637.yaml && python tools/claims_check.py claims/000061/10.1038-nn.4637.yaml paper/10.1038-nn.4637.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/000061/10.1038-nn.4637.yaml; grep -n "—\|rather" $f; python3 - <<'E'
import yaml,re
t=open('claims/000061/10.1038-nn.4637.yaml').read()
d=yaml.safe_load(t)
bad=[]
def walk(x,path):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+[k])
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+[i])
    elif isinstance(x,str) and ': ' in x: bad.append((path,x[:80]))
walk(d,[])
print(bad)
print(len(d['claims']), sum('quote' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']), sum('expected' in c for c in d['claims']))
E
```

```
[]
31 31 23 31 12
```

**Agent**

I rewrote `claims/000061/10.1038-nn.4637.yaml` from the full text, and every quote passes the checker. The checker still exits non-zero on four p-values: the text prints them as "9.70 × 10−9", "8.85x10-05", "7.75x10-05" and "6.45x10-05", forms it doesn't recognise. I checked each against the text by hand and left the checker unchanged.

**Text read.** The version of record (supplied PDF, extracted text): main text, figure legends, Online Methods and reporting summary, plus the Supplementary Information PDF (Supplementary Figs. 1–11, Tables 1–2). Nothing the claims need is missing. The one gap is Supplementary Table 1, which is an image with no numbers in the text, but the counts the claims use are also stated in the Results.

**Code read.** The code the paper links, `buzsakilab/papers`, folder `GGirardeau-BLAHpcInteractions-Package`, commit cdcec89f8d1f. For `SyncHist` I also read FMAToolbox at commit 6bbb3662f7ed.

**Claims.** There are 31 claims: all 31 have quotes, 23 have statistics, all 31 have criteria and 12 have expected values. Six ids are kept because the finding is the same: `hpc-bla-reactivation-post-sleep`, `reactivation-peaks-at-ripples`, `bla-ripple-up-subgroup`, `reactivation-involves-ripple-up-cells`, `aversive-direction-stronger` and `rats-learn-puff-location`. The other 25 are new, covering behaviour, unit counts, sleep firing rates, reactivation decay, the absence of REM reactivation, piriform cortex and central nuclei, within-structure reactivation, downmodulation, pair contributions and gain, the safe trajectory, all cell types, ripple rate, and Fig. 7. The opening comment says what changed and why: the two flagged claims and the other old criteria used agent-chosen measures in place of the paper's own (EV/REV, the Poisson ripple-modulation test and reactivation strength R).

**Details the paper and code leave open, with the readings named:**
- **O1, lap window:** the code picks the track's left limit by hand. Readings: (a) laps the dataset holds; (b) a 150-cm window starting at the smallest run-epoch position; (c) laps between rewards at opposite ends.
- **O2, `poissonTest`:** not in the repository. Readings: tails P(X ≥ n) / P(X ≤ n), or strict tails.
- **O3, bin timestamps:** bin start or centre. I used the standard choice (centre); it can't change an outcome.
- **O4, Fig. 2c cells:** (a) the monosynaptically identified cells, if the dataset marks them; (b) all putative cells of each type.
- **O5, Fig. 1b Bonferroni family size:** (a) all post hoc tests in the panel; (b) uncorrected.
- **O6, Fig. 5a post hoc test:** the Methods say Bonferroni; the legend and the code say Tukey–Kramer. Bonferroni is the main reading (Methods first) and Tukey–Kramer the variant.
- **O7, BLA rate on safe vs air-puff laps:** (a) spike count over lap time; (b) the mean of the position rate curve.
- **Claim-level details:**
  - Habituation: which laps are counted (the Methods, the legend and the code differ). The paper gives no test, so I named readings for "gradually diminished".
  - Supplementary Fig. 9: no test is given; two readings of "did not depend".
  - Fig. 3d comparison: 14 vs 17 piriform sessions; both are shown.
  - Supplementary Fig. 6b: the code's non-significant group is restricted to negative correlations, so it is a variant.

**Paper inconsistencies, recorded in the claims:**
- Fig. 3c prints "z = 0.38" with P = 0.00013 (recorded as printed).
- The text and legend give opposite z signs for the Fig. 5b test (legend z = −3.913 recorded).
- The ripple-rate script calls a right-tailed test, but the printed P is two-sided; the criterion follows the paper.

**Missing for any claim.** Nothing the claims need is missing from the paper.

## End of run

52 turns, 9 minutes, result: success.
