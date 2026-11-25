# mah-2023 · claims · run 42769463961

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ | grep -i mah; ls claims | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,198p docs/protocol.md; ls paper/ | head; ls paper | grep -i -e mah -e 43250
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -60 claims/fouke-2025.yaml; cat papers/datasets/mah-2023.yaml; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-023-43250-x.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-023-43250-x.txt",
 "offset": 90,
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, Methods and supplement are all present. Next I'm reading the supplementary figure legends and the paper's code.

**Agent calls Bash**

```bash
cd  awk 'NR>489' paper/*.txt | grep -n -A12 "^Supplementary Fig\|^#####" | grep -v "^[0-9]*-[-0-9.x× ]*$" | head -300
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone --depth 1 --filter=blob:none --sparse https://github.com/constantinoplelab/published.git pub 2>&1 | tail -2; cd pub && git sparse-checkout set rat_behavior 2>&1|tail -1; git log -1 --format='%H %cd'; find rat_behavior -type f | head -100; find rat_behavior -type f | wc -l
```

```
Cloning into 'pub'...
b7b68ca8c107d8ce4a061e16da214307f175c3e5 Fri Sep 25 05:57:44 2026 -0400
rat_behavior/BehavioralModel/WaitTimeModels/GenerateSynthData_Bayes.m
rat_behavior/BehavioralModel/WaitTimeModels/GenerateSynthData_Bayes_BeliefState.m
rat_behavior/BehavioralModel/WaitTimeModels/GenerateSynthData_Bayes_subopt_onlylambda_flat.m
rat_behavior/BehavioralModel/WaitTimeModels/GenerateSynthData_AlphaPHModel.m
rat_behavior/BehavioralModel/utils/generate_wts.m
rat_behavior/BehavioralModel/TrialInitiationTimeModels/GenerateLatencyData_VanillaAlpha.m
rat_behavior/BehavioralModel/TrialInitiationTimeModels/GenerateLatencyData_RPEAlpha.m
rat_behavior/BehavioralModel/TrialInitiationTimeModels/GenerateLatencyData_DivNormModel.asv
rat_behavior/BehavioralModel/TrialInitiationTimeModels/GenerateLatencyData_Bayes_subopt_onlylambda.m
rat_behavior/BehavioralModel/TrialInitiationTimeModels/GenerateLatencyData_DivNormModel.m
rat_behavior/BehavioralModel/TrialInitiationTimeModels/GenerateLatencyData_AlphaPHModel.m
rat_behavior/BehavioralModel/TrialInitiationTimeModels/GenerateLatencyData_BayesModel.m
rat_behavior/BehavioralModel/.DS_Store
rat_behavior/Analysis/wtByPCatch.m
rat_behavior/Analysis/wtcurves.m
rat_behavior/Analysis/getITI.m
rat_behavior/Analysis/ratAndMdlWTCurves.m
rat_behavior/Analysis/myLambdaShuffleTest.m
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; cat README.md; wc -l Analysis/*.m Figures/Figure[1-5].m utils/*.m | sort -n | tail -40
```

```
# rat_behavior: analysis of rat behavior in a temporal wagering task

This is the code used in [Mah, A., Schiereck, S.S., Bossio, V., Constantinople, C.M. (2023). Distinct value computations support rapid sequential decisions. Nature Communications, 2023](https://www.nature.com/articles/s41467-023-43250-x)

The analyses are broken to two primary sets:
1. Analysis of rat's behavior during the task
2. Analysis of behavioral models fit to the rat's behavior
	
## Data
The data associated with this work can be found on Zenodo at LINK TO COME

## Demos
Figures directory contains code to generate every figure in the paper

## Code dependencies
This project was developed with Matlab 2019a, and uses the following toolboxes
  Curve Fitter
	Optimization
	Signal Analyzer

[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; cat Figures/Figure1.m Analysis/wtcurves.m Analysis/getITI.m Analysis/iticurves.m
```

```
function [WT, Lat] = Figure1(datadir, codedir)
%Figure1 - Wait time and trial initiation time were modulated by the value 
% of the environment
%   datadir = directory of dataset
%   codedir = director of code

%% Set up paths
s = pathsep;
pathStr = [s, path, s];
onPath  = contains(pathStr,...
    codedir, 'IgnoreCase', ispc);

if ~onPath % only add code dir to path if it already isn't
    addpath(genpath(codedir))
end

%% Load data

a = load([datadir filesep 'ratList.mat']);
ratList = a.ratList; % list of rats
[... 426 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; sed -n 1,200p Figures/Figure2.m; cat Analysis/waittime_20ul_by_previous_vol.m Analysis/latency_post20ul_by_previous_vol.m
```

```
function [WT, Lat] = Figure2(datadir, codedir)
%Figure2 - Wait and trial initiation times use distinct estimates of the 
% value of the environment. 
%   datadir = directory of dataset
%   codedir = director of code

%% Set up paths
s = pathsep;
pathStr = [s, path, s];
onPath  = contains(pathStr,...
    codedir, 'IgnoreCase', ispc);

if ~onPath % only add code dir to path if it already isn't
    addpath(genpath(codedir))
end

%% Load data

a = load([datadir filesep 'ratList.mat']);
ratList = a.ratList; % list of rats
[... 273 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; cat Analysis/regress_wt_vs_rew.m Analysis/regress_latency_vs_rew.m utils/fit_exp_decay.m utils/get_tau.m Analysis/myTauShuffleTest.m
```

```
function [b, tau, er] = regress_wt_vs_rew(A, nback, plotarg, cond)
%regress waittime against rewards, a la Wang/Uchida 2013.
%also fits exponential. Adapted from regress_latency_vs_rew
%inputs: A struct. If you give it the S struct, will convert it to A struct.
%nback specifies number of previous trials to regress.
%avm 11/22/21
% avm 23 Nov 21 - edit to only use rewards and wait times from mixed blocks

if nargin == 2
    plotarg = false;
    cond = true(size(A.optout));
elseif nargin == 3
    cond = true(size(A.optout));
end

if isfield(A, 'pd') %if it's an S struct.
    [A, ~, ~] = parse_data_from_mysql(A);
end

% A.block == 1
[... 267 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; sed -n 200,422p Figures/Figure2.m | grep -v "^\s*$" | grep -iv "xlim\|ylim\|xlabel\|ylabel\|xticks\|set(gca\|linewidth=\|title" | head -150
```

```
%--------------------------------------------------------------------------
% Tau histo
%--------------------------------------------------------------------------
subplot(ht, wd, 5); hold on
h = histogram(tau.latency, FaceColor=lat_color,...
    binedges=linspace(0, 5, 25));
histogram(tau.wt, FaceColor=wt_color, binedges=h.BinEdges);
xline(mean(tau.wt, 'omitnan'),...
xline(mean(tau.latency, 'omitnan'),...
%--------------------------------------------------------------------------
% WT vs. TI time taus
%--------------------------------------------------------------------------
subplot(ht, wd, 6); hold on
plot(tau.latency, tau.wt, 'k.', markersize=10)
l1 = refline(1, 0);
%--------------------------------------------------------------------------
% Latency Tau Percentiles - Latency
%--------------------------------------------------------------------------
subplot(ht, wd, 7); hold on
plot(1:9,  betas.latency(first_q, 2:end-1),...
[... 91 more lines not kept]
```

**Agent**

Main text, Methods and supplement are complete. I've read the Figure 1 and 2 code; next come the block-transition, Figure 4 and Figure 5 code.

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; cat Analysis/block_dynamics_wt.m | grep -v "^\s*%" ; cat Analysis/block_dynamics_latency.m | grep -v "^\s*%" | head -120
```

```
function [ltom, htom, mtol, mtoh, ltom_incong, htom_incong, sems] =...
    block_dynamics_wt(A, twin, smoothfactor, varargin)
  
if isfield(A, 'pd') %just in case the input is an S struct.
    [A, ~, ~] = parse_data_from_mysql(A);
end
[~, A.reward] = convertreward(A.reward);

A.wait_time(logical(A.catch)) = (A.wait_time(logical(A.catch))-...
    mean(A.wait_time(logical(A.catch)), 'omitnan'))./...
    std(A.wait_time(logical(A.catch)), 'omitnan');

A = deltawt(A); 

if isempty(varargin)
    dropthese = true(size(A.wait_time));
else
    dropthese = varargin{1};
end
A.wait_time(~dropthese) = nan;
[... 250 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; grep -n "signrank\|ranksum\|prctile\|Shuffle\|corr(\|load(\|BIC\|N = \|= [0-9]*;" Figures/Figure3.m Figures/Figure4.m Figures/Figure5.m Figures/FigureS9.m Figures/FigureS12.m Figures/FigureS2.m Figures/FigureS8.m | head -100; cat Analysis/myLambdaShuffleTest.m
```

```
Figures/Figure3.m:29:A = load([datadir 'ModelFits' filesep...
Figures/Figure3.m:31:B = load([datadir 'ModelFits' filesep...
Figures/Figure3.m:33:C = load([datadir 'ModelFits' filesep...
Figures/Figure3.m:40:a = load([datadir filesep 'ratList.mat']);
Figures/Figure3.m:53:D = 1; % Scale parameter (hand-chosen)
Figures/Figure3.m:67:    a = load([datadir 'A_Structs_Final' filesep...
Figures/Figure3.m:113:% model comparison (BIC = Bayes Information Criteria)
Figures/Figure3.m:114:[~, ~, deltaBIC, pvals] =...
Figures/Figure3.m:122:twin1 = 20; % number of trials around each block to pull
Figures/Figure3.m:123:smoothfactor1 = 10; % size of smoothing window
Figures/Figure3.m:126:twin2 = 20; % number of trials around each block to pull
Figures/Figure3.m:127:smoothfactor2 = 15; % size of smoothing window
Figures/Figure3.m:130:Nsims = 50;
Figures/Figure3.m:229:% Shuffle test parameters
Figures/Figure3.m:230:N = 60; % Percentile to split high/low lambda
Figures/Figure3.m:231:Nshuffle = 500; % Number of shuffles to perform
Figures/Figure3.m:234:twin3 = 30; % number of trials around each block to pull
Figures/Figure3.m:235:smoothfactor = 10; % size of smoothing window
Figures/Figure3.m:261:hiLambda = lambda > prctile(lambda, N); % high lambdas (good inference)
Figures/Figure3.m:262:loLambda = lambda < prctile(lambda, 100-N); % low lambdas (poor inference)
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001169/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps({k:d['draft_version'].get(k) for k in ['name','status']},indent=1))"; curl -s https://api.dandiarchive.org/api/dandisets/001169/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d['name']);print(d.get('description'));print(d.get('assetsSummary',{}).get('numberOfSubjects'), d.get('assetsSummary',{}).get('variableMeasured'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; sed -n 20,160p Figures/Figure4.m | grep -v "^\s*$";
```

```
% block transition dynamic parameters
twin = 20; % number of trials around each block to pull
smoothfactor = 10; % size of smoothing window
% Parameter for example sessions for high to mixed transition
nsess = 10; % Pull first nsess and last nsess to average across rats
chunkSize = 5; % Number of sessions to combine
% Preallcate matricies
[htom_iti_early, ltom_iti_early, mtol_iti_early, mtoh_iti_early,...
    htom_iti_late, ltom_iti_late, mtol_iti_late, mtoh_iti_late,...
    htom_wt_early, ltom_wt_early, mtol_wt_early, mtoh_wt_early,...
    htom_wt_late, ltom_wt_late, mtol_wt_late, mtoh_wt_late] =...
    deal(nan(length(ratList), 2*twin+1));
[data_early, data_late] = deal(cell(1, length(ratList)));
[ltomChunk, htomChunk,...
    mtolChunk, mtohChunk] = deal(cell(1, length(ratList)));
% Loop over rats
for rr = 1:length(ratList)    
    % Load S Struct- has data over training that gets removed in A struct
    s = load([datadir filesep 'S_Structs' filesep...
        'SStruct_' ratList{rr} '.mat']);
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; sed -n 15,150p Figures/Figure5.m | grep -v "^\s*$"
```

```
end
%%
nback = 10;
twin = 20;
smoothfactor = 10;
ratListAll = {'M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047',...
    'M048', 'G070', 'E005', 'E008', 'G078', 'G076','G069', 'S042', 'S050'};
startDates = datetime({'2022-10-04', '2022-10-04', '2022-10-04',...
    '2022-10-04', '2022-12-13', '2022-12-13', '2022-12-13',...
    '2022-12-13', '2022-10-24', '2022-10-24', '2022-10-24',...
    '2022-11-07', '2022-11-14', '2022-11-14', '2022-12-21',...
    '2022-12-22', '2023-01-03', '2023-01-03', '2023-01-23', '2023-01-25'});
secondGroup = {'M045', 'M046', 'M047', 'M048'};
groupOne = ~ismember(ratListAll, secondGroup);
groupTwo = ismember(ratListAll, secondGroup);
[S, sDates,...
    sensitivityProcessed,...
    sensitivityAligned] = deal(cell(size(ratListAll)));
for rr = 1:length(ratListAll)
    ratname = ratListAll{rr};
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; sed -n 25,120p Figures/Figure3.m | grep -v "^\s*$"; sed -n 225,290p Figures/Figure3.m | grep -v "^\s*$"; grep -n "signrank\|BIC\|AIC\|log(" Analysis/model_comparison.m | head
```

```
mdl3 = 'BayesSubOpt_OnlyLambda_flat';
mdl3_projectname = 'FitAll_WT_BayesSubOpt_24July23_Final';
A = load([datadir 'ModelFits' filesep...
    mdl1_projectname filesep 'BestFit.mat']);
B = load([datadir 'ModelFits' filesep...
    mdl2_projectname filesep 'BestFit.mat']);
C = load([datadir 'ModelFits' filesep...
    mdl3_projectname filesep 'BestFit.mat']);
BestFit_mf = A.BestFit;
BestFit_mb = B.BestFit;
BestFit_mb_lambda = C.BestFit;
a = load([datadir filesep 'ratList.mat']);
ratList = a.ratList; % list of rats
%% Generate example kappas from each model
% generate example kappas with handchosen parameters
[Kappa_MF, Kappa_MB] = generateExampleKappas(A);
%% Wait time by catch probability
probCatchVec = [0.1, 0.15, 0.2, 0.25, 0.35]; % Possible catch probabilities
% Model simulation parameters
tau = 2.5; % exponential distribution mean
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; cat utils/convertreward.m; grep -rn "std\|thresh" utils/parse_data_from_mysql.m | head; cat utils/iti_by_reward.m
```

```
function [converted, standard] = convertreward(rewardvector)
%converts all reward volumes to reward levels
%CG moved here 11/5/21

converted = rewardvector;

converted(converted==4) = 1;
converted(converted==5) = 1;
converted(converted==8) = 2;
converted(converted==10) = 2;
converted(converted==16) = 3;
converted(converted==20) = 3;
converted(converted==32) = 4;
converted(converted==40) = 4;
converted(converted==64) = 5;
converted(converted==80) = 5;

standard = converted;
standard(converted==1) = 5;
standard(converted==2) = 10;
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls docs tools; grep -n "expected" -A8 claims/fouke-2025.yaml | head -40; grep -l "elsewhere" claims/*.yaml | head -3
```

```
docs:
agents
archives.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
paper-first.md
pilot-notes
pilot-notes.md
pipeline.md
protocol.md
queue.md

tools:
__pycache__
agent_run.py
archive_transcripts.sh
archives
backfill_summaries.py
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; grep -n "elsewhere" -B3 -A6 claims/berg-2020.yaml | head -40; grep -rn "corrected\|  n:" claims/*.yaml | head -5
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

[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
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
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print(json.dumps(s['properties'].get('checks'),indent=1)[:500])"
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
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -30 claims/kussovska-2025.yaml
```

```
# Claims for Kussovska, Kim & Rungratsameetaweemana (2025), "Neural heterogeneity shapes the
# temporal structure of human working memory", bioRxiv, doi:10.1101/2025.10.31.684900, tested on
# DANDI:000469 (reused; the paper analyses the dataset of Kyzar et al. 2024, ref. 59).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read. paper/10.1101-2025.10.31.684900.txt, the bioRxiv full-text page of the preprint
# posted 1 November 2025 (its header says "version of record"; the page says "New Results" and
# offers a "current version", so a later version may exist; it was not read). It holds the
# abstract, Introduction, Results, legends of Figures 1 to 6, Discussion, Methods, Data and Code
# availability and references. No PDF was supplied. The Extended Data figures (Extended Data
# Figs 1 to 5, behind "Supplementary Material") and their legends are not in the text read; the
# Source Data are not either. The main findings are all stated in the main text and legends, so
# claims were written; claims on Extended Data panels rest on the main-text sentences that cite
# them, and their sources say "(not in the text read)". Several equations of the Methods (the GLM
# link, the local-peak and prominence formulas of Burst detection) were lost in extraction.
#
# Code read. github.com/dariakussovska/heterogeneitywm at commit 5144fe8 (2025-10-26), the last
# commit before the preprint was posted. Later commits (REVISIONS/ and R2_REVISIONS/, 2026) are
# for a revised version and were not used. The repository holds Python scripts named by figure
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://api.github.com/repos/constantinoplelab/published/commits?path=rat_behavior&per_page=10" | python -c "import json,sys;[print(c['sha'][:10],c['commit']['author']['date'],c['commit']['message'][:60].replace('\n',' ')) for c in json.load(sys.stdin)]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/pub/rat_behavior; sed -n 150,207p utils/parse_data_from_mysql.m; cat utils/screen_perf.m | head -49
```

```
end
                    end
                    usethese = find(S.peh{j}(mm).Events.RightIn>...
                        S.peh{j}(mm).Events.CenterOut(1));
                    data.rpokedur = [data.rpokedur; ...
                        sum(S.peh{j}(mm).Events.RightOut(usethese) -...
                        S.peh{j}(mm).Events.RightIn(usethese))];
                    data.rpoke = [data.rpoke;...
                        length(S.peh{j}(mm).Events.RightOut(usethese))];
                    
                else
                    data.rpokedur = [data.rpokedur; nan];
                    data.rpoke = [data.rpoke; nan];
                    
                end
            else
                data.cpokedur = [data.cpokedur; nan];
                data.cpoke = [data.cpoke; nan];
                data.lpokedur = [data.lpokedur; nan];
                data.lpoke = [data.lpoke; nan];
[... 88 more lines not kept]
```

**Agent**

I have what I need from the paper and the code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/mah-2023.yaml",
 "content": "# Claims for Mah, Schiereck, Bossio & Constantinople (2023), \"Distinct value computations support\n# rapid sequential decisions\", Nature Communications 14, 7573, doi:10.1038/s41467-023-43250-x,\n# tested on DANDI:001169 (primary; the dandiset's title is the paper's and its description is the\n# paper's abstract, so it is meant to hold the behavioral data of the 291 rats).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read. paper/10.1038-s41467-023-43250-x.txt, the version of record as served by Europe PMC\n# (PMC10663503), with the main text, figure legends, Methods, Data and Code availability, and three\n# supplement files extracted from their PDFs. Supplement 1 (MOESM1) is the Supplementary\n# Information, Supplementary Figs 1 to 14 with legends; supplement 2 is the peer review file;\n# supplement 3 is the reporting summary. No PDF of the main article was supplied; none was needed,\n# as the text of every legend and table was legible. Source Data are not in the text read.\n#\n# Code read. github.com/constantinoplelab/published, folder rat_behavior, at commit b7b68ca8c107\n# (HEAD, 2026-09-25; the folder was last changed in commit 87fd4a40b3, 2024-09-20, and its files\n# were uploaded in f3cb954ef7, 2023-10-22). It holds MATLAB scripts that redraw each figure\n# (Figures/Figure1.m to Figure5.m, FigureS1.m to FigureS14.m), the analyses they call (Analysis/:\n# wtcurves, iticurves, waittime_20ul_by_previous_vol, latency_post20ul_by_previous_vol,\n# regress_wt_vs_rew, regress_latency_vs_rew, block_dynamics_wt, block_dynamics_latency,\n# myTauShuffleTest, myLambdaShuffleTest, model_comparison, macro_regress_overtraining_V2), the\n# trial parser (utils/parse_data_from_mysql.m, getITI.m, screen_perf.m) and the generative models\n# (BehavioralModel/). It does not hold the model-fitting code: Figure3.m and FigureS8.m load fitted\n# parameters from ModelFits/<project>/BestFit.mat. The paper deposits \"The rat behavioral data and\n# model fits\" on Zenodo, doi:10.5281/zenodo.10031483 (Data availability); those fits are outside\n# data for the model claims (step 4).\n#\n# Data the paper used. 291 Long-Evans rats (184 male, 107 female, Methods, Subjects; the Methods\n# section \"Training for male and female rats\" says 160 male and 114 female, and Supplementary Fig.\n# 12 uses 184 and 107), 6 to 24 months old, trained in a temporal wagering task in stage 8 of\n# shaping (the code codes the final stage as 9, Figure4.m). Median 33,493 trials and 71 sessions per\n# rat. Each trial has an offered reward (5, 10, 20, 40, 80 uL for males; 4, 8, 16, 32, 64 uL for\n# most females, treated as the male volumes, utils/convertreward.m), a cue tone (1 to 16 kHz), a\n# block (mixed, high, low; the code codes 1 = mixed, 2 = high, 3 = low), whether it was a catch\n# trial (15 to 25% of trials; RewardDelay 100 in the code), whether the rat opted out, whether it\n# broke fixation (violation), whether it was rewarded (hit), the wait time (time before opting out)\n# and the trial initiation time (time from opting out or consuming reward to the next center poke;\n# getITI.m measures it from the last exit from the previous rewarded port, or from trial start,\n# to CenterIn). Blocks of 40 completed trials; sessions start with a mixed block; high and low\n# alternate around mixed blocks. Catch probability cohorts (Fig. 3c) of N = 3, 183, 61, 151 and 39\n# rats for 0.1, 0.15, 0.2, 0.25 and 0.35. A further 16 rats ran a pre-initiation cue task (Fig. 5;\n# 12 switched from the standard task, 4 trained only on it). Fig. 4 uses all stage 8 sessions,\n# including sessions that fail the inclusion criterion. Whether the dandiset holds the pre-cue rats,\n# the excluded sessions and the catch probabilities is the author's to find.\n#\n# Common method, used by every criterion unless it says otherwise (Methods, Criteria for including\n# behavioral data and Statistical analyses, and the code).\n# - Sessions. Stage 8 sessions that pass the inclusion criterion (regression of catch-trial wait\n#   time on offered reward, after removing wait times above mean + 2 SD in that session, with a\n#   positive slope on a session followed by another positive session; utils/screen_perf.m also\n#   requires a 7-session moving mean of the slope at or above 0, more than 100 trials and at least\n#   5 catch trials). If the dandiset holds only included sessions, they are used as given.\n# - Wait times. Opt-out wait times on catch trials; wait times more than 1 SD above the mean\n#   catch-trial wait time pooled over the rat's sessions are removed (Methods, Statistical\n#   analyses; parse_data_from_mysql.m:204). Timed-out catch trials (no opt-out within 100 s) are not\n#   catch trials (parse_data_from_mysql.m).\n# - Trial initiation times. All trials; values above the 99th percentile of the rat's pooled\n#   distribution are removed (Methods, Criteria for including behavioral data; iticurves.m).\n# - z-scoring is within rat, over the trials each analysis names.\n# - Volumes are the male volumes; female volumes map 4, 8, 16, 32, 64 to 5, 10, 20, 40, 80.\n#\n# Disagreements between the Methods and the code, and between the text and the legends, are named\n# in the criteria they touch; the Methods come first, the code's choice is a variant.\nschema_version: 2\npaper: doi:10.1038/s41467-023-43250-x\nclaims:\n- id: cohort-size\n  statement: The dataset comes from 291 rats, with a median of 33,493 behavioral trials and 71\n    sessions per rat.\n  source: Results, Rats' deliberative and motivational decisions are sensitive to the value of the\n    environment, paragraph 2\n  quote: We used a high-throughput facility to train 291 rats using computerized, semi-automated\n    procedures. The facility generated statistically powerful datasets (median = 33,493 behavioral\n    trials, 71 sessions).\n  expected:\n  - quantity: rats\n    value: 291\n    tolerance: 0\n  - quantity: median trials per rat\n    value: 33493\n    tolerance: 3349\n  - quantity: median sessions per rat\n    value: 71\n    tolerance: 7\n  criterion: Rats, sessions and trials counted in the data used for Figs 1 to 3 (included stage 8\n    sessions; Figure1.m counts sessions as length(A.date) and trials as length(A.reward) per rat).\n    The rat count must be exact; the medians within 10%. Rats of the pre-initiation cue task are not\n    counted unless they are among the 291.\n\n- id: fig1e-wait-time-increases-with-reward\n  statement: In mixed blocks, rats wait longer for larger offered rewards; mean wait time on catch\n    trials rises with offer across 5, 10, 20, 40 and 80 uL.\n  source: Figure 1d,e; Results, Computational modeling reveals distinct value computations,\n    paragraph 1 (Fig. 3b)\n  quote: This model captured key features of the rats' behavior, including the monotonic\n    relationship between wait time and reward offer in mixed blocks (Fig. 3b )\n  criterion: Per rat, mean wait time on catch trials in mixed blocks for each offer (wtcurves.m);\n    then the mean over the 291 rats. Reproduced when the population mean increases at each step from\n    5 to 80 uL. The paper reports no test.\n\n- id: fig1f-wait-time-block-effect\n  statement: Rats wait about 10% less for 20 uL in high blocks than in low blocks, across the\n    population.\n  source: Figure 1d-f; Results, Rats' deliberative and motivational decisions are sensitive to the\n    value of the environment, paragraph 3\n  quote: rats adjusted how long they were willing to wait for rewards in each block, and on average\n    waited ~10 percent less time for 20 μL in high blocks, when the opportunity cost was high,\n    compared to in low blocks ( p ≪ 0.001, Wilcoxon signed-rank test, N = 291; Fig. 1d–f ).\n  statistics:\n  - test: two-tailed Wilcoxon signed-rank test\n    p: 8.26e-49\n    n: 291 rats\n  expected:\n  - quantity: population mean wait time ratio, 20 uL high block over low block\n    value: 0.90\n    tolerance: 0.025\n  criterion: Per rat, mean wait time on 20 uL catch trials in high and in low blocks; the wait time\n    ratio is high over low (Methods, Statistical analyses; Figure1.m). Reproduced when the mean\n    ratio over rats is within tolerance and the signed-rank test across rats of high against low\n    has p < 0.001. The tolerance is wider than 10% of the reduction because the paper gives the\n    value as \"~10 percent\". Open detail with two readings for the population test, both run - (a)\n    the Methods compare each rat's mean z-scored wait time (z-scored over all its catch trials);\n    (b) Figure1.m compares the raw means in seconds. The per-rat one-tailed rank-sum test (high\n    shorter than low, wtcurves.m) is reported as the count of rats with p < 0.05; the paper gives no\n    count.\n\n- id: fig1i-initiation-block-effect\n  statement: Rats initiate trials more quickly in high blocks than in low blocks, across the\n    population.\n  source: Figure 1g-i; Supplementary Fig. 1; Results, Rats' deliberative and motivational decisions\n    are sensitive to the value of the environment, paragraph 4\n  quote: trial initiation times were modulated by blocks in a similar pattern as the wait times, with\n    rats initiating trials more quickly in high compared to low blocks ( p ≪ 0.001, Wilcoxon\n    signed-rank test, N = 291; Fig. 1g–i ; Supplementary Fig. 1 ).\n  statistics:\n  - test: two-tailed Wilcoxon signed-rank test\n    p: 1.82e-49\n    n: 291 rats\n  criterion: Per rat, mean trial initiation time over all trials in high and in low blocks\n    (iticurves.m). Reproduced when the signed-rank test across rats has p < 0.001 and the mean of\n    the per-rat ratio (high over low) is below 1. Open detail with two readings, both run - (a) the\n    Methods compare mean z-scored initiation times; (b) Figure1.m and Supplementary Fig. 1b\n    compare raw means in seconds (the same p is printed for both).\n\n- id: suppfig2-initiation-block-effect-after-unrewarded\n  statement: The block sensitivity of trial initiation times comes from trials after unrewarded\n    trials; after rewarded trials initiation times do not differ between high and low blocks in the\n    same direction.\n  source: Supplementary Fig. 2b; Results, Rats' deliberative and motivational decisions are\n    sensitive to the value of the environment, paragraph 5; Methods, Statistical analyses,\n    paragraph 3\n  quote: sensitivity to the reward blocks was largely driven by initiation times following\n    unrewarded trials (Supplementary Fig. 2 , Methods), which accounted for more variance in\n    initiation times.\n  statistics:\n  - about: post-rewarded trials, high against low block\n    test: Wilcoxon signed-rank test (two-tailed in the legend)\n    p: 1\n    n: 291 rats\n  - about: post-unrewarded trials, high against low block\n    test: Wilcoxon signed-rank test (two-tailed in the legend)\n    p: 9.07e-50\n    n: 291 rats\n  - about: all trials, high against low block\n    test: Wilcoxon signed-rank test (two-tailed in the legend)\n    p: 9.17e-50\n    n: 291 rats\n  criterion: Per rat, mean z-scored trial initiation time in high and low blocks, split by whether\n    the previous trial was rewarded (unrewarded includes opt-outs and violations; Methods,\n    Statistical analyses, paragraph 3). Reproduced when the post-unrewarded test has p < 0.001 with\n    shorter times in high blocks and the post-rewarded test does not reach p < 0.05 in that\n    direction. Open detail - the legend says two-tailed, FigureS2.m runs one-tailed tests\n    (tail 'right', low longer than high); both are run. The legend prints \"Post-rewarded\" twice; the\n    third value is read as all trials.\n\n- id: suppfig3-wait-time-not-affected-by-previous-outcome\n  statement: Wait times show no major differences after rewarded and after unrewarded trials.\n  source: Supplementary Fig. 3; Results, Rats' deliberative and motivational decisions are sensitive\n    to the value of the environment, paragraph 5\n  quote: There were no major differences in wait times following rewarded or unrewarded trials\n    (Supplementary Fig. 3 ).\n  criterion: Per rat, wait time ratio (20 uL high over low) computed separately for catch trials\n    after rewarded and after unrewarded trials (Supplementary Fig. 3b). The paper reports no test.\n    Reproduced when the population mean ratio is below 1 in both subsets. The size of the\n    difference between subsets (and a signed-rank test of it, a variant) is reported.\n\n- id: fig2a-wait-time-converges-in-mixed-blocks\n  statement: After a transition into a mixed block, wait times converge to a common value whether\n    the previous block was high or low, while trial initiation times in mixed blocks keep depending\n    on the previous block (slower after high blocks, faster after low blocks).\n  source: Figure 2a,b; Supplementary Figs 4 and 5; Results, Trial initiation and wait times\n    exhibited distinct temporal dynamics, paragraph 1\n  quote: In mixed blocks, the wait times following high and low blocks converged to a common value,\n    regardless of the previous block type ... Trial initiation times, however, showed longer\n    timescale effects such that initiation times in mixed blocks strongly depended on the previous\n    block identity (Fig. 2b ; Supplementary Fig. 4 ).\n  criterion: Block transition curves as in the Methods (Block transition dynamics) and the code\n    (block_dynamics_wt.m, block_dynamics_latency.m, 20 trials either side, 10-point moving\n    average per rat, then the mean over rats). Wait times are z-scored over catch trials, then\n    z-scored again within each volume, non-violation catch trials only. Initiation times are\n    z-scored and detrended against trial number (the Methods fit each session; the code fits one\n    line over pooled sessions; both readings run). The paper gives no test. Reproduced when (1)\n    the gap between the high-to-mixed and low-to-mixed wait time curves over trials 1 to 20 of the\n    mixed block is smaller than the same gap for initiation times, relative to each measure's gap\n    over trials -20 to -1, and (2) mean z-scored initiation time over the whole mixed block is\n    higher after high blocks than after low blocks across rats (Supplementary Fig. 4) by a\n    two-tailed signed-rank test at p < 0.05, the paper's population test for block effects\n    (Methods, Statistical analyses). The window for (1) is open; trials 1 to 20 and trials 10 to\n    20 are both run.\n\n- id: suppfig5-mixed-to-adaptation-transitions\n  statement: Longer timescale contrast effects also appear at transitions from mixed into high or\n    low blocks for trial initiation times, but not for wait times.\n  source: Supplementary Fig. 5; Results, Trial initiation and wait times exhibited distinct temporal\n    dynamics, paragraph 1\n  quote: These longer timescale dynamics, which are reminiscent of incentive contrast effects 29 ,\n    were also evident in the transitions from mixed blocks into high/low blocks for trial initiation\n    times, but not wait times (Supplementary Fig. 5 )\n  depends_on:\n  - fig2a-wait-time-converges-in-mixed-blocks\n  criterion: Curves for mixed-to-high and mixed-to-low transitions computed as in\n    fig2a-wait-time-converges-in-mixed-blocks. The mixed block before a low block follows a high\n    block and vice versa (Supplementary Fig. 5 legend). Reproduced when, over trials -20 to -1\n    (the mixed block), the initiation time curve before a low block lies above the one before a high\n    block (the previous high block still slowing initiation), and the wait time curves differ by\n    less than the initiation time curves in that window, as a fraction of their gap over trials 1 to\n    20. The paper reports no test.\n\n- id: fig2c-d-regression-on-previous-rewards\n  statement: In mixed blocks, wait times are explained by the current offer and barely by previous\n    offers, while trial initiation times reflect an exponentially decaying effect of previous\n    rewards (larger recent rewards, faster initiation).\n  source: Figure 2c,d; Results, Trial initiation and wait times exhibited distinct temporal\n    dynamics, paragraph 2\n  quote: Examination of the regression coefficients revealed qualitatively different dynamics, in\n    which the wait times were explained by the reward offered on the current trial, but the trial\n    initiation times reflected an exponentially weighted effect of previous rewards\n  criterion: Regressions as in the Methods (Trial history effects) and the code\n    (regress_wt_vs_rew.m, regress_latency_vs_rew.m), mixed blocks only, log2 rewards, rewards from\n    another block set to NaN, ordinary least squares with a constant. Wait time - z-scored catch\n    trial wait times on the current offer and 9 previous offers, violation trials included.\n    Initiation time - z-scored initiation times on previous rewards, with unrewarded trials set to\n    0 (the Methods say violation and catch trials; the code multiplies by hits, so all unrewarded\n    trials). Open detail - the Methods give 9 previous rewards for initiation times, the code\n    (nback = 10) uses 10; both are run. Reproduced when, in the mean over rats, the current offer\n    coefficient for wait time is positive with a 95% interval across rats excluding 0 and larger in\n    size than every previous trial coefficient, and the initiation time coefficients for 1, 2 and 3\n    trials back are negative and decrease in size with lag.\n\n- id: fig2e-tau-differ\n  statement: The time constants of exponential fits to the previous trial coefficients differ\n    between trial initiation times and wait times, with longer time constants for initiation times\n    (wait time time constants are mostly 0).\n  source: Figure 2e; Results, Trial initiation and wait times exhibited distinct temporal dynamics,\n    paragraph 2; Methods, Trial history effects\n  quote: We fit exponential curves to the previous trial coefficients for each rat, and found that\n    the distributions of exponential decay time constant parameters ( τ ) were significantly\n    different for the trial initiation and wait times ( p ≪ 0.01, Wilcoxon sign-rank test, N = 291;\n    Fig. 2e ).\n  statistics:\n  - test: two-tailed Wilcoxon signed-rank test\n    p: 1.3e-49\n    n: 291 rats\n  depends_on:\n  - fig2c-d-regression-on-previous-rewards\n  criterion: Per rat, from the regressions of fig2c-d-regression-on-previous-rewards, the first\n    coefficient whose 95% interval contains 0 and all after it are set to 0; y = D exp(-x/tau) is\n    fitted to the previous trial coefficients by least squares (fit_exp_decay.m, fmincon, 10\n    random starts; bounds D in [-10, 10], tau in [0, 10] for wait time with coefficients scaled by\n    10, D in [-10, 0], tau in [0, 10] for initiation time); tau is 0 when all previous coefficients\n    are 0. Reproduced when the signed-rank test of the two taus across rats has p < 0.01 and the\n    mean initiation time tau exceeds the mean wait time tau. The random starts are a standard\n    choice (the seed cannot change the outcome beyond fit noise).\n\n- id: fig2f-tau-uncorrelated\n  statement: Across rats, the time constants for wait times and trial initiation times are not\n    correlated.\n  source: Figure 2f; Results, Trial initiation and wait times exhibited distinct temporal dynamics,\n    paragraph 2\n  quote: Moreover, τ parameters were not correlated across models ( r = 0.08, p = 0.18, Pearson\n    linear correlation, N = 291, Fig. 2f ).\n  statistics:\n  - about: as printed in the Results\n    test: Pearson linear correlation\n    statistic: r = 0.08\n    p: 0.18\n    n: 291 rats\n  - about: as printed in the Figure 2f legend\n    test: Pearson linear correlation\n    statistic: r = -0.03\n    p: 0.53\n    n: 291 rats\n  depends_on:\n  - fig2e-tau-differ\n  criterion: Pearson correlation of the per-rat taus of fig2e-tau-differ (Methods, corr.m;\n    Figure2.m, rows 'complete'). A claim of absence, judged on the paper's test - reproduced when\n    p >= 0.05, not reproduced when p < 0.05. The r and p are reported against both printed pairs\n    (the Results and the legend disagree).\n\n- id: fig2g-h-fast-slow-tau-groups\n  statement: Rats split by fast or slow temporal integration of initiation times (tau below the\n    20th or above the 80th percentile) differ in their initiation time regression coefficients but\n    not in their wait time coefficients.\n  source: Figure 2g,h; Results, Trial initiation and wait times exhibited distinct temporal\n    dynamics, paragraph 3\n  quote: There were differences in temporal integration for trial initiation times, but not wait\n    times, for these groups (Fig. 2g, h trial initiation time p < 0.05, wait time p = 0.1,\n    permutation test, N = 116).\n  statistics:\n  - about: initiation time coefficients, fast against slow group\n    test: one-tailed permutation test\n    p: 0.02\n    n: 116 rats\n  - about: wait time coefficients, fast against slow group\n    test: one-tailed permutation test\n    p: 0.1\n    n: 116 rats\n  depends_on:\n  - fig2e-tau-differ\n  criterion: Groups from the initiation time taus of fig2e-tau-differ, below the 20th and above\n    the 80th percentile (Figure2.m, N = 80). Test as myTauShuffleTest.m - the group labels are\n    shuffled 500 times, the mean coefficients of each shuffled half are refitted with an\n    exponential (coefficients times 10, D in [-3, 1], tau in [0, 50]), and p is the share of\n    shuffles whose absolute tau difference exceeds the observed one, divided by 2 (the observed\n    fits use D in [-10, 1], tau in [0, 10]). Reproduced when initiation time p < 0.05 and wait\n    time p >= 0.05; the wait time part is a claim of absence judged on this test.\n\n- id: fig2j-wait-time-not-sensitive-to-previous-offer\n  statement: In mixed blocks, wait times for 20 uL do not depend on whether the previous offer was\n    smaller or larger than 20 uL, for 87% of rats (253 of 291) and for the population.\n  source: Figure 2j; Results, Trial initiation and wait times exhibited distinct temporal dynamics,\n    paragraph 3\n  quote: Indeed, for almost all rats (87%), wait times for 20 μL offers in mixed blocks were not\n    significantly different if they were preceded by rewards that were smaller or larger than 20 μL\n    ( p > 0.05, Wilcoxon rank-sum test, N = 253/291).\n  statistics:\n  - about: population\n    test: two-tailed Wilcoxon rank-sum test (legend)\n    p: 0.8\n    n: 291 rats\n  expected:\n  - quantity: rats with p < 0.05 (per-rat rank-sum test)\n    value: 38\n    tolerance: 4\n  criterion: Per rat, 20 uL catch trials in mixed blocks (not the first trial), wait times z-scored\n    over these trials, split by previous offer below or above 20 uL (Methods, Trial history\n    effects; waittime_20ul_by_previous_vol.m), compared with a two-tailed rank-sum test. The\n    count of rats with p < 0.05 must be within tolerance. The population part is a claim of absence\n    - per-rat means for the two conditions, compared across rats by the legend's two-tailed\n    rank-sum test; reproduced when p >= 0.05. Figure2.m runs a paired signed-rank test; it is shown\n    as a variant.\n\n- id: fig2k-initiation-sensitive-to-previous-offer\n  statement: In mixed blocks, trial initiation times are slower after offers smaller than 20 uL\n    than after offers larger than 20 uL, significantly so for 89% of rats (256 of 291) and for the\n    population.\n  source: Figure 2k; Results, Trial initiation and wait times exhibited distinct temporal dynamics,\n    paragraph 3\n  quote: However, for 89% of rats, trial initiation times were significantly modulated by previous\n    rewards, suggesting fixed and incrementally updated estimates of the value of the environment,\n    respectively ( p < 0.05, Wilcoxon rank-sum test, N = 256/291, Fig. 2i–l ).\n  statistics:\n  - about: population\n    test: two-tailed Wilcoxon rank-sum test (legend)\n    p: 1.84e-49\n    n: 291 rats\n  expected:\n  - quantity: rats with p < 0.05 (per-rat rank-sum test)\n    value: 256\n    tolerance: 26\n  criterion: Per rat, z-scored initiation times in mixed blocks split by previous offer below or\n    above 20 uL, compared with a two-tailed rank-sum test; the count with p < 0.05 within\n    tolerance; population p < 0.001 with slower initiation after smaller offers. Open details, all\n    readings run - which trials (the Methods use 20 uL trials in mixed blocks; the code,\n    latency_post20ul_by_previous_vol.m, uses all mixed-block trials, z-scored over all the rat's\n    trials); the population test (the legend's rank-sum on per-rat means, or Figure2.m's paired\n    signed-rank).\n\n- id: fig2l-sensitivity-greater-for-initiation\n  statement: Sensitivity to the previous offer is larger for trial initiation times than for wait\n    times across rats.\n  source: Figure 2l; Methods, Trial history effects\n  quote: We compared wait time and trial initiation time sensitivity to previous offers across rats\n    using a paired Wilcoxon signed-rank test.\n  statistics:\n  - test: two-tailed Wilcoxon signed-rank test\n    p: 6.21e-38\n    n: 291 rats\n  depends_on:\n  - fig2j-wait-time-not-sensitive-to-previous-offer\n  - fig2k-initiation-sensitive-to-previous-offer\n  criterion: Sensitivity is the mean for previous offer below 20 uL minus the mean for previous offer\n    above 20 uL, per rat and measure, from fig2j and fig2k (Methods, Trial history effects;\n    Figure2.m). Reproduced when the paired signed-rank test has p < 0.001 and the mean initiation\n    time sensitivity exceeds the mean wait time sensitivity. Run under each reading of fig2k.\n\n- id: suppfig6-results-without-detrending\n  statement: Satiety effects on trial initiation times are modest, and the results, including the\n    dynamics at block transitions, do not change qualitatively without detrending.\n  source: Supplementary Fig. 6; Results, Trial initiation and wait times exhibited distinct temporal\n    dynamics, paragraph 4\n  quote: However, there was no qualitative change in any of our results, including the dynamics at\n    block transitions, if we did not detrend (Supplementary Fig. 6 ).\n  depends_on:\n  - fig2a-wait-time-converges-in-mixed-blocks\n  criterion: The initiation time transition curves of fig2a-wait-time-converges-in-mixed-blocks\n    recomputed without the trial number regression (block_dynamics_latency.m with detrending off).\n    Reproduced when part (2) of that criterion and the ordering of the curves (above after high\n    blocks, below after low blocks) still hold.\n\n- id: fig3c-wait-time-by-catch-probability\n  statement: Rats' wait times in mixed blocks depend in a graded way on the catch probability, as\n    the wait time model predicts (shorter waits at higher catch probability).\n  source: Figure 3c; Results, Computational modeling reveals distinct value computations,\n    paragraph 1; Methods, Statistical analyses, paragraph 5\n  quote: as well as a graded dependence of wait times on the catch probability (Fig. 3c )\n  expected:\n  - quantity: rats at catch probability 0.1\n    value: 3\n    tolerance: 0\n  - quantity: rats at catch probability 0.15\n    value: 183\n    tolerance: 18\n  - quantity: rats at catch probability 0.2\n    value: 61\n    tolerance: 6\n  - quantity: rats at catch probability 0.25\n    value: 151\n    tolerance: 15\n  - quantity: rats at catch probability 0.35\n    value: 39\n    tolerance: 4\n  criterion: The direction is read from Equation 1 (wait time grows with C/(1-C), C = 1 - catch\n    probability), which the figure compares with the rats. Per rat and catch probability, mean wait\n    time on mixed block catch trials by offer, leaving out each rat's first 1000 stage 8 trials\n    (Figure3.m, which drops them because the first trials of stage 8 have catch probability 0.35\n    while rats learn); then the mean over rats with data at that probability. Reproduced when, for\n    at least 4 of the 5 offers, the population mean wait time decreases from 0.15 to 0.2 to 0.25\n    (the cohorts large enough to compare), with the 0.1 and 0.35 cohorts reported. Rats per cohort\n    within 10% (exact for 3 rats). The ordering rule is a reading; the paper gives no test.\n\n- id: fig3j-inferential-beats-retrospective-for-wait-times\n  statement: Wait times are better fit by the inferential model, which uses hidden state inference to\n    choose a block-specific value of the environment, than by the retrospective model, by BIC, AIC\n    and cross-validated negative log-likelihood.\n  source: Figure 3j; Supplementary Fig. 8a,c,e; Results, Computational modeling reveals distinct\n    value computations, paragraph 5\n  quote: By several model comparison metrics, wait times were better fit by the inferential model\n    that used hidden state inference to select block-specific estimates of the value of the\n    environment ( p ≪ 0.001, Wilcoxon signed-rank test, N = 291; Fig. 3j , Supplementary Fig. 8 )\n  statistics:\n  - about: delta BIC\n    test: two-tailed Wilcoxon signed-rank test\n    p: 1.07e-37\n    n: 291 rats\n  - about: cross-validated negative log-likelihood\n    test: two-tailed Wilcoxon signed-rank test\n    p: 6.58e-40\n    n: 291 rats\n  - about: AIC\n    test: two-tailed Wilcoxon signed-rank test\n    p: 1.89e-39\n    n: 291 rats\n  criterion: Both models fitted to each rat's wait times (Methods, Behavioral models, Inferential\n    model, Retrospective model, Fitting and evaluating models) - wait time by Equation 1 with tau =\n    2.5 s, C = 1 - catch probability, log-normal noise of variance 8; inferential kappa from the\n    most likely block under Equations 3 to 6 with H0 = 1/40; retrospective kappa by Equation 9\n    with the dynamic gain of Equation 10; fmincon, 100 random starts; BIC = log(n) k + 2 nLL on all\n    data, AIC = 2k + 2 nLL, and 5-fold cross-validated nLL. Reproduced when all three signed-rank\n    tests have p < 0.001 with the inferential model better on average. Open details - the paper's\n    fitting code is not in the repository, so the free parameters of each model, their bounds and\n    the folds are not fixed (the Methods name kappa_low, kappa_mixed, kappa_high and D for the\n    inferential model, and alpha_0 and D with an initial kappa for the retrospective one; other sets\n    may be named, with the parameter count k following them). The paper's fits are deposited on\n    Zenodo (doi:10.5281/zenodo.10031483); using them in place of a refit is an input from outside\n    the dataset.\n\n- id: suppfig8-belief-state-not-distinguished\n  statement: Model comparison does not distinguish the inferential model from the belief state model\n    for wait times.\n  source: Supplementary Fig. 8b,d,f; Results, Computational modeling reveals distinct value\n    computations, paragraph 6\n  quote: In fact, when the posterior beliefs are stable, which is often the case, the belief state\n    and inferential models are identical, and model comparison did not favor one model over the\n    other (Supplementary Fig. 8 ).\n  statistics:\n  - about: cross-validated negative log-likelihood\n    test: two-tailed Wilcoxon signed-rank test\n    p: 1\n    n: 291 rats\n  - about: AIC\n    test: two-tailed Wilcoxon signed-rank test\n    p: 1\n    n: 291 rats\n  - about: BIC\n    test: two-tailed Wilcoxon signed-rank test\n    p: 1\n    n: 291 rats\n  depends_on:\n  - fig3j-inferential-beats-retrospective-for-wait-times\n  criterion: The belief state model (Equation 7) fitted as in\n    fig3j-inferential-beats-retrospective-for-wait-times, with the same open details. A claim of\n    absence - reproduced when none of the three signed-rank tests reaches p < 0.05.\n\n- id: suppfig9-wait-times-reflect-misinferences\n  statement: Within mixed blocks, wait times for 20 uL differ between trials the inferential model\n    labels as high and as low blocks, so wait times reflect mistaken inferences.\n  source: Supplementary Fig. 9; Results, Computational modeling reveals distinct value computations,\n    paragraph 5\n  quote: The rats' wait times reflected these mistaken inferences, further indicating that their wait\n    times were well-described by the inferential model ( p ≪ 0.001, Wilcoxon signed-rank test\n    comparing wait times for 20μL in misinferred high vs. low blocks, N = 291; Supplementary Fig. 9\n    ).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 291 rats\n  depends_on:\n  - fig3j-inferential-beats-retrospective-for-wait-times\n  criterion: The inferential model, fitted per rat, labels each mixed block trial with its most\n    likely block; per rat, mean wait time on 20 uL catch trials labeled high and labeled low, in\n    held-out test sets (Supplementary Fig. 9 legend; FigureS9.m compares column 3, 20 uL, with\n    signrank). Reproduced when p < 0.001 with shorter waits on trials labeled high.\n\n- id: fig3l-lambda-groups-wait-time-dynamics\n  statement: Rats with optimal and poor inference (high or low lambda of the sub-optimal inferential\n    model) differ in their wait time dynamics at transitions from mixed into low or high blocks, but\n    not in their trial initiation time dynamics.\n  source: Figure 3l; Supplementary Figs 10 and 11; Results, Computational modeling reveals distinct\n    value computations, paragraph 7\n  quote: Rats with optimal and poor inference exhibited significantly different dynamics at\n    transitions from mixed into low or high blocks, indicated by different inverse temperature\n    parameters (mix to low/high, p < 0.05, one-tailed permutation test, N = 180 Fig. 3l ). There was\n    no difference in the dynamics of trial initiation times for those same groups of rats (mixed to\n    low... p = 0.3, mixed to high... p = 0.2, one-tailed permutation test, N = 180; Fig. 3l ).\n  statistics:\n  - about: wait time, mixed to low, slope (legend)\n    test: one-tailed non-parametric shuffle test\n    p: 0.02\n    n: 116 rats (legend; 180 in the Results)\n  - about: wait time, mixed to high, right asymptote (legend)\n    test: one-tailed non-parametric shuffle test\n    p: 0.003\n    n: 116 rats (legend; 180 in the Results)\n  - about: trial initiation time, mixed to low, slope (legend; p = 0.3 in the Results)\n    test: one-tailed non-parametric shuffle test\n    p: 0.15\n    n: 116 rats (legend; 180 in the Results)\n  - about: trial initiation time, mixed to high, right asymptote (legend; p = 0.2 in the Results)\n    test: one-tailed non-parametric shuffle test\n    p: 0.21\n    n: 116 rats (legend; 180 in the Results)\n  criterion: Lambda per rat from the sub-optimal inferential model (Equation 8) fitted to wait times\n    as in fig3j-inferential-beats-retrospective-for-wait-times. Mixed-to-low and mixed-to-high\n    curves (block_dynamics_wt.m, block_dynamics_latency.m with 30 trials either side, trials -20\n    to 20 kept) averaged per group; the 4-parameter logistic of Equation 11 fitted to each group\n    mean (my_fit_sigmoid.m, 10 starts); 500 label shuffles; p is the share of shuffles whose\n    absolute parameter difference exceeds the observed one, divided by 2 (myLambdaShuffleTest.m).\n    Reproduced when the wait time test has p < 0.05 for the slope C at mixed to low and for at\n    least one parameter at mixed to high (the right asymptote D per the legend, C per the Results),\n    and the initiation time tests do not reach p < 0.05 for those same parameters (absence, judged\n    on this test). Open detail - the groups are below the 20th and above the 80th percentile of\n    lambda in the Methods and the Results (N = 116 in the legend fits this), while Figure3.m splits\n    at the 40th and 60th (N = 60); both are run, the Methods' split first.\n\n- id: fig3i-retrospective-model-captures-initiation\n  statement: A retrospective model with a learning rate scaled by changes in the inferred block\n    posterior captures the slow and fast dynamics of trial initiation times at block transitions and\n    their dependence on previous rewards, while a static learning rate or an unsigned prediction\n    error gain does not.\n  source: Figure 3g-i; Supplementary Fig. 7; Results, Computational modeling reveals distinct value\n    computations, paragraphs 3 and 4\n  quote: We explored versions of the dynamic learning rate that did not reflect inference, including\n    using the unsigned reward prediction error or a running average of reward prediction errors 38 .\n    However, these models could not capture both short and long timescale dynamics at block\n    transitions (Supplementary Fig. 7 ).\n  criterion: Simulated initiation times TI = D/kappa (Equation 2) on the rats' reward sequences, with\n    kappa from Equation 9 under three gains - G from Equation 10, G = 1, and G = |delta| (Methods,\n    Retrospective model; GenerateLatencyData_AlphaPHModel.m, _VanillaAlpha.m, _RPEAlpha.m), alpha_0\n    below 0.1 (Results, paragraph 4), log-normal noise of variance 4, 50 simulations (Supplementary\n    Fig. 7 legend), curves as in fig2a-wait-time-converges-in-mixed-blocks. Reproduced when the\n    Equation 10 model shows both an overshoot after the high-to-mixed transition (maximum within\n    20 trials above the value at trial 20) and a persistent post-high above post-low gap in the\n    mixed block, while each alternative lacks one of the two. The paper fits no initiation time\n    model; the parameter values beyond alpha_0 below 0.1 are open and the ones set in the code's\n    scripts are used.\n\n- id: bayes-observer-offer-reduces-uncertainty\n  statement: In simulations of a Bayes optimal observer, hearing the reward offer reduces the\n    uncertainty of beliefs about the hidden block (posterior variance below prior variance).\n  source: Results, Reducing state uncertainty did not change trial initiation times, paragraph 2\n  quote: Model simulations of a Bayes' optimal observer did show that the reward offer reduced the\n    uncertainty of subjective beliefs about the hidden state (comparing variance of prior to\n    variance of posterior, p ≪ 0.001, Wilcoxon sign-rank test).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Prior (Equation 5) and posterior (Equation 3) of the inferential model on the rats'\n    reward sequences, with H0 = 1/40. Open details - \"variance\" of a distribution over three blocks\n    is not defined, nor the unit of the test (trials or rats); readings run - the variance of the\n    block probabilities, and the variance of block value with blocks coded 1 to 3 (low, mixed,\n    high), tested over trials and over per-rat means. Reproduced when the posterior is less\n    uncertain with p < 0.001 under the readings run.\n\n- id: fig4a-wait-time-block-sensitivity-emerges\n  statement: When the hidden blocks are introduced, wait times for 20 uL become sensitive to the\n    block only gradually over training, while trial initiation times are block sensitive from the\n    first session.\n  source: Figure 4a,b; Results, Block sensitivity for wait times requires structure learning,\n    paragraph 2\n  quote: In the final stage of training, when rats were introduced to the hidden states, their wait\n    times for 20μL gradually became sensitive to the reward block (Fig. 4a ) ... In contrast, trial\n    initiation times exhibited block sensitivity on the first session in the final training stage\n    (Fig. 4a ).\n  criterion: All stage 8 sessions, including those that fail the inclusion criterion, grouped in\n    consecutive pairs; per pair, wait time and initiation time ratios (high over low) as in\n    fig1f-wait-time-block-effect and fig1i-initiation-block-effect; per session, wait time\n    regressed on current reward and block (1 low, 2 mixed, 3 high), smoothed with a 5-session moving\n    average, outliers 3 scaled MADs from a 5-point moving median set to NaN, then averaged over\n    rats (Methods, Learning dynamics; macro_regress_overtraining_V2.m, first 50 sessions in\n    Figure4.m). Reproduced when the mean initiation time ratio of the first session pair is below\n    1 (signed-rank against 1, p < 0.05, a reading), the mean wait time ratio of the first pair is\n    closer to 1 than its mean over the last 10 pairs of the first 50 sessions, and the block\n    coefficient grows in size from the first to the last 10 sessions. The windows are readings;\n    the paper gives no test.\n\n- id: fig4c-initiation-previous-reward-stable\n  statement: The effect of the previous reward on trial initiation times is comparable early and\n    late in training.\n  source: Figure 4c; Results, Block sensitivity for wait times requires structure learning,\n    paragraph 2\n  quote: This sensitivity was comparable early and late in training, consistent with animals using\n    previous rewards to a similar extent at these timepoints (Fig. 4c ).\n  depends_on:\n  - fig4a-wait-time-block-sensitivity-emerges\n  criterion: Per session, initiation time regressed on the previous reward, smoothed and cleaned as\n    in fig4a-wait-time-block-sensitivity-emerges, averaged over rats over the first 50 sessions.\n    The paper reports no test. Reproduced when the mean coefficient over the first 10 sessions has\n    the same sign as over sessions 41 to 50 and differs from it by less than the change in the wait\n    time block coefficient over the same sessions, in proportion to each coefficient's late value\n    (a reading).\n\n- id: fig4d-overshoot-grows-with-training\n  statement: The overshoot of trial initiation times after transitions from high to mixed blocks\n    becomes more prominent with training, on a timescale like that of block sensitivity for wait\n    times.\n  source: Figure 4d,e; Results, Block sensitivity for wait times requires structure learning,\n    paragraph 3\n  quote: The overshoot became more prominent with training (Fig. 4d ), on a similar timescale as\n    block sensitivity for wait times (Fig. 4e ), suggesting a shared mechanism.\n  depends_on:\n  - fig4a-wait-time-block-sensitivity-emerges\n  criterion: Overshoot is the maximum z-scored initiation time after a high-to-mixed transition\n    minus its value 20 trials after the transition (Fig. 4d legend; Figure4.m), on the high-to-mixed\n    curves of block_dynamics_latency.m averaged over rats. Reproduced when the overshoot of the\n    last 10 stage 8 sessions exceeds that of the first 10 (Figure4.m, nsess = 10). For Fig. 4e, the\n    overshoot per chunk of 5 sessions (Figure4.m), smoothed with a 10-point moving average, is\n    reported beside the wait time ratio over sessions; it is shown, not judged, as the paper gives\n    no measure of \"similar timescale\".\n\n- id: fig5b-pre-cue-initiation-sensitive-to-offer\n  statement: With the reward cue played before trial initiation, trial initiation times become\n    sensitive to the offered reward.\n  source: Figure 5b; Results, Reducing state uncertainty did not change trial initiation times,\n    paragraph 3; Methods, Pre-initiation cue task\n  quote: Their trial initiation times became sensitive to the offered reward (Fig. 5b ).\n  criterion: The 16 pre-cue rats (Figure5.m names them); for the 12 that switched, sessions after 30\n    pre-cue sessions (Methods; Figure5.m starts at a dated switch per rat and the 30-session offset\n    is not visible in it, so both are run) and their original-task sessions; for the 4 others all\n    stage 8 sessions; no session exclusion by the wait time criterion. Per rat, mean z-scored\n    initiation time by offer in mixed blocks, leaving out trials after violations\n    (iti_by_reward.m), with the code's one-way ANOVA over offers. Reproduced when the population\n    mean on the pre-cue task decreases from 5 to 80 uL and more rats reach ANOVA p < 0.05 on the\n    pre-cue task than on the original task (a reading; the paper gives no test).\n\n- id: fig5c-pre-cue-initiation-still-sensitive-to-previous-reward\n  statement: On the pre-initiation cue task, trial initiation times for 20 uL in mixed blocks are\n    still modulated by the previous reward, for 13 of 16 rats and for the population.\n  source: Figure 5c; Results, Reducing state uncertainty did not change trial initiation times,\n    paragraph 3\n  quote: However, trial initiation times for 20μL in mixed blocks were still modulated by the\n    previous reward, consistent with the use of incrementally updated estimates of the value of the\n    environment within a block ( p < 0.05 for 13/16 rats; Fig. 5c ).\n  statistics:\n  - about: population\n    test: two-tailed Wilcoxon rank-sum test\n    p: 1.03e-4\n    n: 16 rats\n  expected:\n  - quantity: rats with p < 0.05\n    value: 13\n    tolerance: 1\n  depends_on:\n  - fig2k-initiation-sensitive-to-previous-offer\n  - fig5b-pre-cue-initiation-sensitive-to-offer\n  criterion: Pre-cue sessions as in fig5b-pre-cue-initiation-sensitive-to-offer; per rat and at\n    population, the test of fig2k-initiation-sensitive-to-previous-offer under each of its\n    readings. Reproduced when the count is within tolerance and the population p < 0.001 with\n    slower initiation after smaller offers.\n\n- id: fig5d-pre-cue-initiation-depends-on-previous-block\n  statement: On the pre-initiation cue task, how quickly rats initiate trials in mixed blocks still\n    depends on the previous block.\n  source: Figure 5d; Results, Reducing state uncertainty did not change trial initiation times,\n    paragraph 3\n  quote: Moreover, how quickly they initiated trials in mixed blocks continued to depend on the\n    previous block identity (Fig. 5d ).\n  depends_on:\n  - fig2a-wait-time-converges-in-mixed-blocks\n  - fig5b-pre-cue-initiation-sensitive-to-offer\n  criterion: Pre-cue sessions as in fig5b-pre-cue-initiation-sensitive-to-offer; initiation time\n    transition curves as in fig2a-wait-time-converges-in-mixed-blocks. Reproduced when the\n    population mean z-scored initiation time over trials 1 to 20 of mixed blocks is higher after\n    high blocks than after low blocks, with a two-tailed signed-rank test across the 16 rats at\n    p < 0.05 (a reading; the paper gives no test).\n\n- id: suppfig12-no-sex-differences\n  statement: Male and female rats do not differ in their wait time ratios or trial initiation time\n    ratios.\n  source: Supplementary Fig. 12; Methods, Training for male and female rats\n  quote: We did not observe any significant differences between the male and female rats, in terms\n    of contextual effects, or behavioral dynamics at block transitions (Supplementary Fig. 12 ).\n  statistics:\n  - about: wait time ratio\n    test: Wilcoxon rank-sum test\n    p: 0.23\n    n: 184 males and 107 females\n  - about: trial initiation time ratio\n    test: Wilcoxon rank-sum test\n    p: 0.59\n    n: 184 males and 107 females\n  depends_on:\n  - fig1f-wait-time-block-effect\n  - fig1i-initiation-block-effect\n  criterion: Per-rat wait time and initiation time ratios of fig1f and fig1i compared between sexes\n    with a rank-sum test (FigureS12.m). A claim of absence - reproduced when both p >= 0.05. Sex is\n    taken from the subject metadata; the group sizes are reported against 184 and 107 (the Methods\n    also print 160 and 114). The transition dynamics by sex are shown, not judged (no test).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/mah-2023.yaml paper/10.1038-s41467-023-43250-x.txt; grep -nP "[^\"'] [a-z_]*: .*[^ ]: " claims/mah-2023.yaml | grep -v "^\S*#" | head; grep -n "—\|rather" claims/mah-2023.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml
d=yaml.safe_load(open('claims/mah-2023.yaml'))
def walk(x):
    if isinstance(x,dict): [walk(v) for v in x.values()]
    elif isinstance(x,list): [walk(v) for v in x]
    elif isinstance(x,str) and ': ' in x: print(repr(x[:80]))
walk(d)
c=d['claims'];print(len(c), sum('statistics' in k for k in c), sum('criterion' in k for k in c), sum(len(k.get('statistics',[])) for k in c))"
```

```
30 16 30 28
```

**Agent**

I've written `claims/mah-2023.yaml`. The quote checker passes: 30 claims, 30 quotes, 28 statistical values, 0 problems.

**Text read**
- The version of record (Nat Commun 14:7573) as served by Europe PMC (PMC10663503): main text, legends and Methods.
- Three supplement files: the Supplementary Information (Supplementary Figs 1–14 with legends), the peer review file and the reporting summary.
- There was no main-article PDF, and none was needed. Source Data are not in the text.

**Code read**
- github.com/constantinoplelab/published, folder `rat_behavior`, at commit b7b68ca8.
- It has figure scripts, analysis functions, the trial parser and the generative models. It does not have the model-fitting code.
- The fitted models are on Zenodo (doi:10.5281/zenodo.10031483). The claims file names them as outside data.

**Claims:** 30, all with quotes. 16 claims carry statistics (28 entries in total), and all 30 have criteria. 6 are claims of absence, each judged on the paper's own test. All are `data: dataset`.

**Details left open, and the readings named for each**
- **Population block tests (Fig. 1f, 1i):** the Methods compare z-scored means; the code compares raw means.
- **Supplementary Fig. 2b:** the legend says two-tailed; the code runs one-tailed tests.
- **Fig. 2k, which trials:** the Methods use 20 μL mixed-block trials; the code uses all mixed-block trials. For the population test, the legend says rank-sum; the code runs a signed-rank test.
- **Fig. 2j population test:** the legend's rank-sum is primary; the code's signed-rank is a variant.
- **Previous rewards in the initiation-time regression:** 9 in the Methods, 10 in the code.
- **Detrending:** the Methods fit each session; the code fits one line over pooled sessions.
- **Fig. 3l lambda groups:** split at the 20th/80th percentile in the Methods and legend, at 40th/60th in the code. The legend and Results also disagree on which logistic parameter differs, the p-values and N (116 vs 180).
- **Fig. 2f:** the Results print r = 0.08, p = 0.18; the legend prints r = −0.03, p = 0.53. Both are recorded.
- **Bayes observer "variance":** undefined, and so is the unit of the test. I named two variance readings, each tested over trials and over per-rat means.
- **Pre-cue sessions (Fig. 5):** the Methods start after 30 pre-cue sessions; this offset is not visible in the code.
- **Model fitting (Fig. 3j, Supplementary Figs 8 and 9, Fig. 3l):** the free parameters, bounds and folds are not fixed, because the fitting code is missing.
- **Qualitative claims with no test in the paper** (Fig. 2a–b, Supplementary Fig. 5, Fig. 3c, Fig. 4a/c/d, Fig. 5b/d): the windows and ordering rules are stated as readings.

**Missing from the paper**
- No fitting code for the wait-time models.
- No reported test for the transition-dynamics, training and catch-probability claims.
- The sex counts disagree within the Methods (184/107 vs 160/114).
- Whether the dandiset holds the 16 pre-cue rats, the sessions that failed inclusion (needed for Fig. 4) and the catch probabilities is left for the author to check.

## End of run

30 turns, 6 minutes, $2.26 at API prices, result: success.
