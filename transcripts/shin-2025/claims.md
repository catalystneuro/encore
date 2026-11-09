# 000248 · claims · run 39999757269

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/000248 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md; echo ----; ls claims/001453/ paper/ claims/000248 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -c paper/*; head -20 paper/*.txt; cat claims/001453/*.yaml | head -150
```

Result: not kept, because it reads the paper's text.

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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-025-02055-5.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1038-s41593-025-02055-5.txt').read(); print(s[54000:100000])"
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the protocol and the main Results; now reading the Methods in chunks.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1038-s41593-025-02055-5.txt').read(); print(s[56000:76000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1038-s41593-025-02055-5.txt').read(); print(s[76000:98000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1038-s41593-025-02055-5.txt').read(); print(s[98000:122000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1038-s41593-025-02055-5.txt').read(); print(s[-3000:])"; head -c 3000 paper/10.1101-2023.06.05.543698.txt; ls paper; grep -o "Supplementary Fig[^,;)]*" paper/10.1038-s41593-025-02055-5.txt | sort | uniq -c
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -rn "elsewhere" claims | head; grep -rln "data_source\|outside:" claims | head; ls claims | head -50; awk '/^## Author/,0' docs/protocol.md | grep -n -i -B2 -A12 "step 4\|### 4"
```

```
claims/000294/10.1162-neco_a_01672.yaml:43:# data elsewhere. The experimental model fits (Figures 7, 8, 10) use the dataset's recordings
claims/000294/10.1162-neco_a_01672.yaml:192:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml:203:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml:218:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml:234:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml:247:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml:273:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml:285:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml:305:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml:318:  data: elsewhere
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p claims/000294/10.1162-neco_a_01672.yaml; sed -n 185,210p claims/000294/10.1162-neco_a_01672.yaml; grep -n "allowed\|KEYS\|keys\|'data'\|elsewhere\|with_labels" tools/claims_check.py | head -40
```

```
# Claims for Buccino, Damart, Bartram, ... Hierlemann & Van Geit (2024) on dandiset 000294.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (Neural Computation 36, 1286-1331, 2024, CC BY 4.0), from the
# PDF supplied to paper/ and its text extraction: main text, Methods (section 5), Tables 1 to 5
# and the appendix (Figures 9 and 10). The paper has no separate supplement.
#
# Code read: github.com/alejoe91/multimodalfitting at commit 24e8e6168b2d5be45c551bcc08b62fde187d01c7
# (2025-04-12), the repository the Data and Code Availability section names. It holds the package
# (ecode protocols, feature extraction, the patch and HD-MEA sync and patch-triggered average in
# mea_patch/mea_patch.py, model and evaluator construction), the optimization script
# (scripts/run_optimizations.py, 20 offspring and 600 generations by default), the notebooks that
# make the figures (notebooks/ground-truth and notebooks/experimental/cell1, cell2, notebook
# outputs stripped), and cell_models/ with the ground-truth model (hay_ais) and the two
# experimental models: morphology_corrected.swc, mechanisms, parameters, and fitting/efeatures with
# the extracted feature and protocol files, the thresholded probe and the template_BPO.npy
# template of each cell. No optimization results (checkpoints, runs.pkl) are in the repository.
# The BluePyOpt extensions are in BluePyOpt pull request 385, release 1.13.88 (not read).
# In the code, cell 1 is "cell1_211006_3148" and cell 2 is "cell1_211011_3436" (the cell1 and
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -m 30 https://api.dandiarchive.org/api/dandisets/000248/ | head -c 1500; echo; curl -sL -m 30 "https://api.dandiarchive.org/api/dandisets/000248/versions/draft/info/" | python3 -c "import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m.get('name')); print(m.get('description')); print(d.get('version'))"; curl -sIL -m 30 https://doi.org/10.24433/CO.6659254.v2 | grep -i "^location\|^HTTP"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for u in "https://codeocean.com/capsule/2540707/tree/v2" "https://codeocean.com/api/capsules/2540707" "https://api.github.com/search/repositories?q=illusory+contours+pattern+completion" "https://api.github.com/users/hs13/repos"; do echo "== $u"; curl -sL -m 30 -A "Mozilla/5.0" "$u" | head -c 1500; echo; done
```

```
== https://codeocean.com/capsule/2540707/tree/v2
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<HTML><HEAD><META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=iso-8859-1">
<TITLE>ERROR: The request could not be satisfied</TITLE>
</HEAD><BODY>
<H1>403 ERROR</H1>
<H2>The request could not be satisfied.</H2>
<HR noshade size="1px">
Request blocked.
We can't connect to the server for this app or website at this time. There might be too much traffic or a configuration error. Try again later, or contact the app or website owner.
<BR clear="all">
If you provide content to customers through CloudFront, you can find steps to troubleshoot and help prevent this error by reviewing the CloudFront documentation.
<BR clear="all">
<HR noshade size="1px">
<PRE>
Generated by cloudfront (CloudFront)
Request ID: OEbgYBbSnA_wJ3OeLv_syfXaKo61l23gFRw69Dbs_G2Z6k3dD9mU-A==
</PRE>
<ADDRESS>
</ADDRESS>
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
curl -sL -m 30 "https://api.github.com/users/hs13/repos?per_page=100" | python3 -c "import json,sys; [print(r['name'], r['fork'], r['pushed_at'], r['description']) for r in json.load(sys.stdin)]"; curl -sL -m 30 "https://api.github.com/users/hs13" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('name'), d.get('company'), d.get('bio'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/hs13/IC_paper_code.git && git clone -q https://github.com/hs13/Analyze_IC_OpenScope_v240130.git && cd IC_paper_code && git log -3 --format="%H %ad %s" && find . -type f -not -path "./.git/*" | head -100 && find . -type f -not -path "./.git/*" | wc -l; cd ../Analyze_IC_OpenScope_v240130 && git log -1 --format="%H %ad %s" && find . -type f -not -path "./.git/*" | wc -l
```

```
50e04eaf7c9192a067c129f3c1f174a27f10c406 Sun Oct 27 22:04:51 2024 +0900 Initial commit
./postprocessnwb_v240130.m
./postprocess_optotagging.m
./plot_SVM_trainREx_areas.m
./plot_SVM_trainICRC_areas.m
./plot_MouseEye.m
./merge_postprocessed.m
./computeCCGpeaktroughs.m
./check_CCF.m
./analyzesizeCI.m
./analyze_CCGfftlong.m
./analyzeStaticICtxi.m
./analyzeRFCIspin.m
./analyzeRFCI.m
./analyzeMouseEye.m
./analyzeICtxi_SVM_subsets.m
./analyzeICtxi_SVM_areas.m
./aggregate_psth.m
./aggregate_fixedgaze.m
./aggregateMouseEye.m
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code && wc -l *.m
```

```
197 aggregateICtxi_SVM_trainICRC_areas.m
   192 aggregateICtxi_SVM_trainREx_areas.m
   125 aggregateMouseEye.m
   624 aggregate_fixedgaze.m
   593 aggregate_psth.m
   477 analyzeICtxi_SVM_areas.m
   442 analyzeICtxi_SVM_subsets.m
   599 analyzeMouseEye.m
   127 analyzeRFCI.m
   181 analyzeRFCIspin.m
   469 analyzeStaticICtxi.m
   306 analyze_CCGfftlong.m
   340 analyzesizeCI.m
   220 check_CCF.m
    82 computeCCGpeaktroughs.m
   416 merge_postprocessed.m
   579 plot_MouseEye.m
   553 plot_SVM_trainICRC_areas.m
   604 plot_SVM_trainREx_areas.m
   431 postprocess_optotagging.m
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/IC_paper_code/analyzeStaticICtxi.m"
}
```

```
1	function ICsig = analyzeStaticICtxi(R, trialorder)
2	
3	Nneurons = size(R, 1);
4	if size(R,2)~=length(trialorder)
5	    error('check R dimensions')
6	end
7	
8	Palpha = 0.05;
9	correctmultcomp = true;
10	verbosity = false;
11	
12	%% Kruskalwallis statistics
13	% perhaps do ranksum tests instead of
14	clk = tic;
15	tic
16	% PkwBKI and PmcBKI can be skipped if time is scarce (will save ~15 seconds)
17	BKtt = [0 106 107 110 111]; % Blank and Kanizsa trial type
18	% BKItt = [0 106 107 110 111 1301:1308]; % Blank, Kanizsa and Inducer trial type
19	BItt = [0 1301:1308]; % Blank and Inducer trial type
20	BICREltt = [0 106 506 111 511]; % Blank, IC and REl trial type
[... 450 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/IC_paper_code/postprocessnwb_v240130.m"
}
```

```
1	% check here for camstim orientation: clockwise, i.e., 30deg is 1o'clock
2	% http://observatory.brain-map.org/visualcoding/stimulus/static_gratings
3	
4	clear all
5	
6	addpath(genpath('d:\Users\USER\Documents\MATLAB\matnwb'))
7	addpath('C:\Users\USER\GitHub\Analyze_IC_OpenScope_v240130')
8	addpath(genpath('C:\Users\USER\GitHub\helperfunctions'))
9	
10	datadir = 'S:\OpenScopeData\00248_v240130\';
11	nwbdir = dir(datadir);
12	nwbsessions = {nwbdir.name};
13	nwbsessions = nwbsessions( contains(nwbsessions, 'sub-') | contains(nwbsessions, 'sub_') );
14	
15	%%
16	for ises = 1:numel(nwbsessions)
17	    clearvars -except ises nwbsessions datadir
18	    sesclk = tic;
19	
20	    nwbfiles = cat(1, dir([datadir nwbsessions{ises} filesep '*.nwb']), dir([datadir nwbsessions{ises} filesep '*' filesep '*.nwb']));
[... 379 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/IC_paper_code/analyzeRFCI.m"
}
```

```
1	% THIS CODE TREATS THE ENTIRE SPINNING GRATING AS ONE TRIAL, CONSISTENT
2	% WITH THE ANALYSIS DONE WITH 2P DATASET
3	
4	% % 10000s: which type (classic 0 vs inverse 1), 1000s which ctrsizes, 
5	% % 10-100s: which RFcenter, 1s: which direction
6	% RFCI = struct();
7	% tloi = psthtli>0 & psthtli<=1000;
8	% tempR = squeeze(1000*mean(psth.RFCI(tloi,:,:), 1))';
9	% temptrialorder = vis.RFCI_presentations.trialorder(1:4:end);
10	% RFCI.(visblocknames{b}) = analyzeRFCI(tempR, temptrialorder);
11	
12	% 'RFcentersrel', 'cRFsigneurons', 'cRFind', 'iRFsigneurons', 'iRFind', ...
13	% 'RFcentersrel9', 'RFcenterinds9', 'cRFind9', 'pRFclassic9', 'cRFsigexcl9', ...
14	% 'iRFind9', 'pRFinverse9', 'iRFsigexcl9')
15	
16	function RFCI = analyzeRFCI(R, trialorder, sponFR)
17	
18	Nneurons = size(R,1);
19	if numel(sponFR) ~= Nneurons
20	    error('check sponFR')
[... 108 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/IC_paper_code/analyzeICtxi_SVM_areas.m"
}
```

```
1	% 0. score needs to be reordered?
2	% is there bias if I don't mask the order of Ylabs?
3	% 1. predict returns [label, NegLoss, PBScore] when there are >2 classes,
4	% but retnuns [label, score] when there are only two classes
5	% 2. before, trials2anal (balanced trials if trial repeat is different amongst train trial types) was ignored after being computed -- now train and test trials are only being drawn from trials2anal
6	clear all; close all; clc
7	
8	datadir = 'S:\OpenScopeData\00248_v240130\';
9	nwbdir = dir(datadir);
10	nwbsessions = {nwbdir.name};
11	nwbsessions = nwbsessions( contains(nwbsessions, 'sub-') | contains(nwbsessions, 'sub_') );
12	Nsessions = numel(nwbsessions);
13	
14	svmdesc = 'trainICRC';
15	preproc = 'zscore'; % zscore or minmax or meancenter
16	whichSVMkernel = 'Linear';
17	neuopt = '';
18	
19	% takes ~50hrs per session...
20	rng('shuffle')
[... 458 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code; grep -n "neuopt\|Rall\.\|Rall =\|tloi\|>=50\|>= 50\|Nneu.*50\|signrank\|ranksum\|kruskal\|friedman\|0\.4\|neuRS\|wfdur" plot_SVM_trainICRC_areas.m aggregateICtxi_SVM_trainICRC_areas.m merge_postprocessed.m | head -80
```

```
plot_SVM_trainICRC_areas.m:1:discardbelowNneurons = 50;
plot_SVM_trainICRC_areas.m:245:        p = signrank(testaccuracy(a,:), testaccuracy(b,:));
plot_SVM_trainICRC_areas.m:310:ptestpred=signrank(reshape(nanmean(testpredmatchnull(a,b,:,:),3),[],1), reshape(testpredmatch(a,b,:),[],1));
plot_SVM_trainICRC_areas.m:351:        p = signrank(testaccuracy(a,:), testaccuracy(b,:));
plot_SVM_trainICRC_areas.m:410:        p = signrank(AIC_BLC, ALC_BIC);
plot_SVM_trainICRC_areas.m:500:p=signrank(xvec(~isnan(xvec) & ~isnan(yvec)), yvec(~isnan(xvec) & ~isnan(yvec)));
plot_SVM_trainICRC_areas.m:502:p=signrank(reshape(nanmean(TREpredmatchnull{ii},3),[],1), reshape(TREpredmatch{ii},[],1));
plot_SVM_trainICRC_areas.m:515:p = signrank(reshape(nanmean(TREasICmatchnull{ii},3),[],1), reshape(TREasICmatch{ii},[],1));
plot_SVM_trainICRC_areas.m:526:pTREpred=signrank(reshape(nanmean(TREpredmatchnull{ii}(a,b,:,:),3),[],1), reshape(TREpredmatch{ii}(a,b,:),[],1));
plot_SVM_trainICRC_areas.m:527:pTREasIC=signrank(reshape(nanmean(TREasICmatchnull{ii}(a,b,:,:),3),[],1), reshape(TREasICmatch{ii}(a,b,:),[],1));
plot_SVM_trainICRC_areas.m:533:pTREpred=signrank(reshape(nanmean(TREpredmatchnull{ii}(a,b,:,:),3),[],1), reshape(TREpredmatch{ii}(a,b,:),[],1));
plot_SVM_trainICRC_areas.m:534:pTREasIC=signrank(reshape(nanmean(TREasICmatchnull{ii}(a,b,:,:),3),[],1), reshape(TREasICmatch{ii}(a,b,:),[],1));
plot_SVM_trainICRC_areas.m:543:% V1 & AM match N=11 TRE p=0.7646 TRE as IC p=0.4131
plot_SVM_trainICRC_areas.m:546:% LM & PM match N=8 TRE p=0.1484 TRE as IC p=0.4609
aggregateICtxi_SVM_trainICRC_areas.m:8:neuopt = 'RS';
aggregateICtxi_SVM_trainICRC_areas.m:29:svmfn = strcat(pathsvm, 'SVM_', svmdesc, '_', whichvisarea, neuopt, '_', whichSVMkernel, '_', preproc, '_', whichICblock, '.mat');
aggregateICtxi_SVM_trainICRC_areas.m:81:            svmfn = strcat(pathsvm, 'SVM_', svmdesc, '_', whichvisarea, neuopt, '_', whichSVMkernel, '_', preproc, '_', whichICblock, '.mat');
aggregateICtxi_SVM_trainICRC_areas.m:
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/IC_paper_code/aggregateICtxi_SVM_trainICRC_areas.m"
}
```

```
1	addpath(genpath('C:\Users\USER\GitHub\helperfunctions'))
2	datadir = 'S:\OpenScopeData\00248_v240130\';
3	nwbdir = dir(datadir);
4	nwbsessions = {nwbdir.name};
5	nwbsessions = nwbsessions( contains(nwbsessions, 'sub-') | contains(nwbsessions, 'sub_') );
6	Nsessions = numel(nwbsessions);
7	
8	neuopt = 'RS';
9	svmdesc = 'trainICRC';
10	preproc = 'zscore'; % '' is z-score train trials, '_zscoreall', or '_meancenter'
11	whichSVMkernel = 'Linear';
12	
13	pathsv = [datadir 'SVM_' svmdesc '_selectareas' filesep];
14	loadallsvm = true;
15	allblocks = true;
16	
17	visareas = {'VISp', 'VISl', 'VISrl', 'VISal', 'VISpm', 'VISam'};
18	visarealabels = {'V1', 'LM', 'RL', 'AL', 'PM', 'AM'};
19	if allblocks
20	    ICblocknames = {'ICkcfg0','ICkcfg1','ICwcfg0','ICwcfg1'};
[... 178 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code; sed -n 300,335p merge_postprocessed.m; grep -n "neuallloc\|ICsigall\|RFCIall" merge_postprocessed.m | head -20
```

```
neucheck = false(Nneuronsall,1);
    
    for iprobe = 1:numel(probes)
        if nnz(floor(unit_peakch/1000)==iprobe-1)==0
            continue
        end
        
        load(sprintf('%spostprocessed_probe%s.mat', pathpp, probes{iprobe}))
        load(sprintf('%svisresponses_probe%s.mat', pathpp, probes{iprobe}))
        if validfixgaze
            load(sprintf('%svisresponses_fixedgaze%dpix_probe%s.mat', pathpp, gazedistthresh, probes{iprobe}))
        end
        
        if any(neucheck(neuoind))
            error('some of the neurons seem to already have been accounted for, check')
        end
        neucheck(neuoind)=true;
        
        meanFRall(neuoind) = meanFRvec;
        sponFRall(neuoind) = sponFRvec;
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code; sed -n 1,60p plot_SVM_trainICRC_areas.m; echo ....; sed -n 440,553p plot_SVM_trainICRC_areas.m
```

```
discardbelowNneurons = 50;
whichICblock = 'ICwcfg1';
SVMall = SVMtrainICRCagg.(whichICblock);
Nsessions = numel(SVMall);

visareas = {'VISp', 'VISl', 'VISrl', 'VISal', 'VISpm', 'VISam'};
visarealabels = {'V1', 'LM', 'RL', 'AL', 'PM', 'AM'};
traintrialtypes = SVMall(1).VISp.trialtypes;

%% test trials: check that there is correlation between area decoders
% this correlation must exceed null distribution, where null distribution
% is obtained by shuffling within trial types

% perhaps train and test trial divide should have been the same between all
% areas...
Nshuf = 1000;

testaccuracy = NaN(numel(visareas), Nsessions);
for ises = 1:Nsessions
for a = 1:numel(visareas)
[... 156 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code; cat computeCCGpeaktroughs.m; grep -n "ICwcfg1\|smooth\|25\|flank\|7\*\|thresh\|wfdur\|ranksum\|RS" analyze_CCGfftlong.m | head -40
```

```
function [hpk, tpk, htr, ttr] = computeCCGpeaktroughs(CCG, CCGtli)
% CCG format: Nneurons * Nneurons * Ntimepoints
% CCGplus: take >=0 timepoints, and rearrange so that the first axis is timepont

flanktli = abs(CCGtli)>50 & abs(CCGtli)<=100;
CCGflankstd = squeeze( std(CCG(:,:,flanktli),0,3) );
CCGflankmean = squeeze( mean(CCG(:,:,flanktli),3) );

Nneu = size(CCG,2);
CCGtlirs = CCGtli(CCGtli>=0);
CCGrs = permute(CCG(:,:,CCGtli>=0), [3 1 2]);
dCCGrs = diff(CCGrs);

% t0ind = find(CCGtli>=0, 1,'first');
% if ~isequaln( squeeze(dCCGrs(1,:,:)), squeeze(CCG(:,:,t0ind+1)-CCG(:,:,t0ind)) )
%     error('sanity check failed')
% end

dCCGrssign = dCCGrs;
dCCGrssign(dCCGrs>0) = 1;
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code; sed -n 60,180p analyze_CCGfftlong.m
```

```
nwbspikefile = fullfile([nwbfiles(fileind).folder filesep nwbfiles(fileind).name]);
    nwb = nwbRead(nwbspikefile); %, 'ignorecache');
    unit_times_data = nwb.units.spike_times.data.load();
    
    recarealabels = {'VISp', 'VISl', 'VISrl', 'VISal', 'VISpm', 'VISam'};
    visarealabels = zeros(Nneuctx,1);
    for a = 1:numel(recarealabels)
        if strcmp(recarealabels{a}, 'VISp')
            neuinarea = contains(neulocctx, 'VISp') & ~contains(neulocctx, 'VISpm');
        else
            neuinarea = contains(neulocctx, recarealabels{a});
        end
        visarealabels(neuinarea) = a;
    end
    
    ststartend = [floor(min(unit_times_data)/Tres)+1 floor(max(unit_times_data)/Tres)+1];
    ICblockstartend = [vis.ICwcfg1_presentations.start_time(1) vis.ICwcfg1_presentations.stop_time(end)];
    ICblockstartend = floor(ICblockstartend/Tres)+1;
    
    Nneurons = length(unit_ids);
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Analyze_IC_OpenScope_v240130; ls | head -300 | tr '\n' ' '; echo; grep -l "CCG" *.m | head -30
```

```
100000.tif LICENSE MouseEye20pix_ICwcfg1.jpg MouseEye20pix_validRFCI.jpg README.md UMAP_KNN_decoder.ipynb aggregateICtxi_SVM_invcv_trainICRC_lmlv.m aggregateICtxi_SVM_sponreactivation.m aggregateICtxi_SVM_trainICRC_areas.m aggregateICtxi_SVM_trainICRC_cumPSTH.m aggregateICtxi_SVM_trainICRC_lmlv.m aggregateICtxi_SVM_trainICRC_lmlv_consistency.m aggregateICtxi_SVM_trainREx_areas.m aggregateICtxi_SVM_trainREx_cumPSTH.m aggregateICwcfg1_spikecount.m aggregateMouseEye.m aggregateSVM_trainICRC_lmlv.m aggregate_Trise.m aggregate_ctxqcCCGfftlong.m aggregate_fixedgaze.m aggregate_latency.m aggregate_psth.m aggregate_rate_EPS.m aggregate_rate_celltype.m aggregate_spectraleventtriggered_spiking.m aggregate_spiketriggered_LFP_CSD_TFR.m aggregate_stpsth_LFP_CSD_TFR.m aggregate_time_time_cossim.m analyzeICtxi_SVM_PSTH.m analyzeICtxi_SVM_areas.m analyzeICtxi_SVM_cumPSTH.m analyzeICtxi_SVM_invcv_trainICRC_lmlv.m analyzeICtxi_SVM_sponreactivation.m analyzeICtxi_SVM_subsets.m analyzeICtxi_SVM_trainICRC_lmlv.m analyzeICtxi_SVM_trainICRC_lmlv_consistency.m analyzeICtxi_SVM_trainICRC_lmlv_scoreconsistency.m analyzeICtxi_SVM_trainICRC_lmlv_scoresimilarity.m analyzeICwcfg1_gaborfiltbank_SVM_trainICRC.m analyzeMouseEye.m analyzeRFCI.m analyzeRFCIspin.m analyzeStaticICtxi.m analyze_CCGfftlong.m analyze_ICwcfg1_hireptt_UMAP.ipynb analyze_Trise.m analyze_UMAP_KNN_sponreactivation.ipynb analyze_cossim.m analyze_ephys_properties.m analyze_latency.m analyze_logmean_logvar_Xneurons.m analyze_neuronclusters.m analyze_spectraleventtriggered_spiking.m analyze_spikecount_ConwayMaxwellPoisson.exe analyze_spikecount_ConwayMaxwellPoisson.m analyze_spiketriggered_LFP_CSD_TFR.m analyze_stpsth_LFP_CSD_TFR.m analyze_time_time_cossim.m analyzesizeCI.m check_CCF.m check_nwb.m check_nwb_vis.m check_sanity.m clusterNeurons.m compare_latency_smoothVShistogram.m computeBayesianInferenceDecoding.m computeCCGpeaktroughs.m computeICtxi_SVM.m computeSVM_trainICRC_lmlv.m compute_spkcnt_lmlv_UMAP_KNN.m find_localmax_me
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Analyze_IC_OpenScope_v240130; wc -l aggregate_ctxqcCCGfftlong.m; grep -n "smooth\|movmean\|25\|flank\|7\*\|\*7\|thresh\|ranksum\|ICencoder\|indin\|1:10\|<=10\|wfdur\|0.4\|neufilt\|qc" aggregate_ctxqcCCGfftlong.m | head -80
```

```
548 aggregate_ctxqcCCGfftlong.m
3:datadir = 'S:\OpenScopeData\00248_v240130\';
8:    'sub-625545', 'sub-625554', 'sub-625555', 'sub-630506', 'sub-631510', ...
14:ccgpath = 'S:\OpenScopeData\00248_v240130\CCG\';
22:    tli25 = CCGtli_fft>=-12 & CCGtli_fft<=12;
23:    CCGtli = CCGtli_fft(tli25);
24:    ctxCCG = ctxCCGfftnew(:,:,tli25);
38:% standard deviation of the CCG flanks (between ±50–100 ms from zero). 
41:ccgpath = 'S:\OpenScopeData\00248_v240130\CCG\';
53:ctxCCGflankstdagg = cell(Nsessions,1);
76:    flanktli = abs(CCGtli_fft)>=50;
77:    ctxCCGflankstdagg{ises} = std(ctxCCGfftnew(:,:,flanktli),0,3);
84:    'ctxCCGjcpostpkagg', 'ctxCCGjcpostTpkagg', 'ctxCCGjcprepkagg', 'ctxCCGjcpreTpkagg', 'ctxCCGflankstdagg', '-v7.3')
87:ccgpath = 'S:\OpenScopeData\00248_v240130\CCG\';
118:ctxCCGflankstd = std(ctxCCGfftnew(:,:,abs(CCGtli_fft)>=50),0,3);
119:ctxCCGflankstdpost = std(ctxCCGfftnew(:,:,CCGtli_fft>=50),0,3);
120:ctxCCGflankstdpre = std(ctxCCGfftnew(:,:,CCGtli_fft<=-50),0,3);
126:            tempy = ctxCCGflankstdpost;
129:            tempy = ctxCCGflankstdpost;
132:            tempy = ctxCCGflankstd;
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Analyze_IC_OpenScope_v240130; sed -n 1,40p aggregate_ctxqcCCGfftlong.m; sed -n 150,215p aggregate_ctxqcCCGfftlong.m; sed -n 325,400p aggregate_ctxqcCCGfftlong.m; git log -1 --format=%H -- aggregate_ctxqcCCGfftlong.m
```

```
addpath(genpath('C:\Users\USER\GitHub\helperfunctions'))

datadir = 'S:\OpenScopeData\00248_v240130\';
% nwbdir = dir(datadir);
% nwbsessions = {nwbdir.name};
% nwbsessions = nwbsessions(( contains(nwbsessions, 'sub-') | contains(nwbsessions, 'sub_') ));
nwbsessions = {'sub-619293', 'sub-619296', 'sub-620333', 'sub-620334', ...
    'sub-625545', 'sub-625554', 'sub-625555', 'sub-630506', 'sub-631510', ...
    'sub-631570', 'sub-633229', 'sub-637484'};
Nsessions = numel(nwbsessions);
ses2anal = 1:Nsessions;

%{
ccgpath = 'S:\OpenScopeData\00248_v240130\CCG\';
for ises = ses2anal
    fprintf('%d/%d %s\n', ises, Nsessions, nwbsessions{ises})
    clearvars -except ises ses2anal Nsessions nwbsessions ccgpath
    % pathpp = [datadir 'postprocessed' filesep nwbsessions{ises} filesep];
    pathccg = [ccgpath nwbsessions{ises} filesep];
    load([pathccg 'ctxCCGfftnew.mat'])
[... 164 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code; grep -n "RFexcl\|RFsigexcl\|exclctr\|ICresp\|RElresp\|prefIRE\|match\|ICwcfg\|neuRS\|signrank\|ranksum\|0\.05" aggregate_psth.m | head -60
```

```
1:% IMPORTANT VERSION UPDATE ON 231010 : aggregate to match the original order
90:ICblocks = {'ICkcfg0_presentations','ICkcfg1_presentations','ICwcfg0_presentations','ICwcfg1_presentations'};
92:allfields = fieldnames(ICsig.ICwcfg1_presentations);
95:    validfields(f) = size(ICsig.ICwcfg1_presentations.(allfields{f}),1)==Nneurons;
105:%     'ICresp1','RCresp1','RCresp2','ICresp2','ICtuned1','RCtuned1','RCtuned2','ICtuned2'};
362:visblocks = {'ICkcfg0_presentations','ICkcfg1_presentations','ICwcfg0_presentations','ICwcfg1_presentations', ...
364:ICblocks = {'ICkcfg0_presentations','ICkcfg1_presentations','ICwcfg0_presentations','ICwcfg1_presentations'};
443:        % visblocks = {'ICkcfg0_presentations','ICkcfg1_presentations','ICwcfg0_presentations','ICwcfg1_presentations', ...
557:        error('mismatch between uniquecnt and strcmp -- check')
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/Analyze_IC_OpenScope_v240130; grep -ln "RFexclsigclassic\|RFsigexclclassic" *.m; grep -rn "RFsigexclclassic\|RFexclsigclassic" --include=*.m . | grep -v "analyzeRFCI\|RFCIfields" | head -20
```

```
analyzeMouseEye.m
analyzeRFCI.m
analyzeRFCIspin.m
rerun_analyzeRFCI.m
./analyzeMouseEye.m:333:fprintf('ctrCRF: pRFclassic* %d Pkw_rfclassic* %d sigmc_rfclassic %d RFsigexclclassic %d RFexclsigclassic %d\n', ...
./analyzeMouseEye.m:337:    nnz(RFCI.RFindclassic==1 & RFCI.RFsigexclclassic), ...
./analyzeMouseEye.m:338:    nnz(RFCI.RFindclassic==1 & RFCI.RFexclsigclassic) )
./analyzeMouseEye.m:367:fprintf('spin ctrCRF: pRFclassic* %d Pfried_rfclassic* %d RFsigexclclassic %d RFexclsigclassic %d\n', ...
./analyzeMouseEye.m:370:    nnz(RFCIspin.RFindclassic==1 & RFCIspin.RFsigexclclassic), ...
./analyzeMouseEye.m:371:    nnz(RFCIspin.RFindclassic==1 & RFCIspin.RFexclsigclassic) )
./analyzeMouseEye.m:427:            fprintf('fixed gaze ctrCRF: pRFclassic* %d Pkw_rfclassic* %d sigmc_rfclassic %d RFsigexclclassic %d RFexclsigclassic %d\n', ...
./analyzeMouseEye.m:431:                nnz(RFCI_fixedgaze.RFindclassic==1 & RFCI_fixedgaze.RFsigexclclassic), ...
./analyzeMouseEye.m:432:                nnz(RFCI_fixedgaze.RFindclassic==1 & RFCI_fixedgaze.RFexclsigclassic) )
./analyzeMouseEye.m:447:            fprintf('fixed gaze spin ctrCRF: pRFclassic* %d Pfried_rfclassic* %d RFsigexclclassic %d RFexclsigclassic %d\n', ...
./analyzeMouseEye.m:450:                nnz(RFCIspin_fixedgaze.RFindclassic==1 & RFCIspin_fixedgaze.RFsigexclclassic), ...
./analyzeMouseEye.m:451:                nnz(RFCIspin_fixedgaze.RFindclassic==1 & RFCIspin_fixedgaze.RFexclsigclassic) )
./analyzeMouseEye.m:495:    fprintf('ctrCRF: pRFclassic* %d Pkw_rfclassic* %d sigmc_rfclassic %d RFsigexclclassic %d RFexclsigclassic %d\n', ...
./analyzeMouseEye.m:499:        nnz(RFCI.RFindclassic==1 & RFCI.RFsigexclclassic), ...
./analyzeMouseEye.m:500:        nnz(RFCI.RFindclassic==1 & RFCI.RFexclsigclassic) )
./analyzeMouseEye.m:502:    fprintf('spin ctrCRF: pRFclassic* %d Pfried_rfclassic* %d RFsigexclclassic %d RFexclsigclassic %d\n', ...
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; grep -n "def \|KNOWN\|FIELDS\|fields" tools/claims_check.py | head -40
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

[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
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
cd  python3 -c "
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
cd $TMPDIR/IC_paper_code; sed -n 225,260p plot_SVM_trainICRC_areas.m; sed -n 380,420p plot_SVM_trainICRC_areas.m; grep -n "kruskal\|friedman" *.m | head
```

```
end
end
toc
end

%% plot test trial prediction match between pairs of areas
figure
for a = 1:numel(visareas)
    whichvisareaA = visareas{a};
    for b = a+1:numel(visareas)
        whichvisareaB = visareas{b};
        subplot(numel(visareas), numel(visareas), (a-1)*numel(visareas)+b)
        hold all
        plot(testaccuracy(a,:), testaccuracy(b,:), 'o')
        xl = xlim;
        plot(xl,xl,'r-')
        % xlabel([whichvisareaA ' test accuracy'])
        % ylabel([whichvisareaB ' test accuracy'])
        xlabel(whichvisareaA)
        ylabel(whichvisareaB)
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code; sed -n 1,125p aggregateMouseEye.m | grep -v "^\s*%" | head -120
```

```
datadir = 'S:\OpenScopeData\00248_v230821\';
nwbdir = dir(datadir);
nwbsessions = {nwbdir.name};
nwbsessions = nwbsessions(~contains(nwbsessions, 'Placeholder') & ...
    ( contains(nwbsessions, 'sub-') | contains(nwbsessions, 'sub_') ));
Nsessions = numel(nwbsessions);

whichblock = 'ICwcfg1_presentations';

    pathpp = [datadir 'postprocessed' filesep nwbsessions{ises} filesep];
load([pathpp 'trackmouseeye.mat'])


trackeyetli = trialdistmodecom.(whichblock).trackeyetli;
trackeyetrialinds = trialdistmodecom.(whichblock).psthtrialinds;

figure; hold all
plot(vis.(whichblock).trialstart, TrackEyeTimestamps(trackeyetrialinds(:, trackeyetli==0)), 'o')
plot(vis.(whichblock).trialstart, vis.(whichblock).trialstart, '-')

[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Analyze_IC_OpenScope_v240130; cat pix8visdeg.m | head -60; grep -n "gazedistthresh\s*=\|mode(" ../IC_paper_code/analyzeMouseEye.m | head
```

```
230:gazedistthresh = 20;
295:    gazedistthresh = 20;
483:    gazedistthresh = 20;
541:    gazedistthresh = 20;
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code; sed -n 1,60p analyzeMouseEye.m | grep -v "^\s*%$"; sed -n 220,300p analyzeMouseEye.m; wc -c ../Analyze_IC_OpenScope_v240130/pix8visdeg.m
```

```
addpath(genpath('d:\Users\USER\Documents\MATLAB\matnwb'))
addpath(genpath('C:\Users\USER\GitHub\Analize_IC_OpenScope_v240130'))
addpath(genpath('C:\Users\USER\GitHub\helperfunctions'))

datadir = 'S:\OpenScopeData\00248_v240130\';
nwbdir = dir(datadir);
nwbsessions = {nwbdir.name};
nwbsessions = nwbsessions( contains(nwbsessions, 'sub-') | contains(nwbsessions, 'sub_') );
Nsessions = numel(nwbsessions);

% Skipping session1 sub-619293 -- EyeTracking error in nwb
% Skipping session12 sub-637484 -- EyeTracking error in nwb

%%
for ises = 1:Nsessions
    clearvars -except ises Nsessions nwbsessions datadir
    sesclk = tic;
    
    visblocks = {'ICkcfg0_presentations','ICkcfg1_presentations','ICwcfg0_presentations','ICwcfg1_presentations', ...
        'RFCI_presentations','sizeCI_presentations'}; %,'spontaneous_presentations'};
[... 123 more lines not kept]
```

**Agent**

I've read enough code to write the criteria. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000248/10.1038-s41593-025-02055-5.yaml",
 "content": "# Claims for Shin, Ogando, Abdeladim, ... Lecoq & Adesnik (2025), \"Recurrent pattern completion\n# drives the neocortical representation of sensory inference\", Nature Neuroscience 28, 2319-2329,\n# on dandiset 000248 (\"Allen Institute Openscope - Illusion project\").\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (CC BY 4.0), full text from Europe PMC in\n# paper/10.1038-s41593-025-02055-5.txt: main text, figure legends, Methods and the Extended Data\n# figure legends (Extended Data Figs. 1 to 10). The Supplementary Information (Supplementary\n# Results, Supplementary Discussion, Supplementary Figs. 1 to 8) is not in paper/ and was not\n# read. The main findings are shown in the main and Extended Data figures; the Supplementary\n# Figures are cited for support only (Supp. Fig. 1 heatmaps of the subsets, Supp. Fig. 2 mesoscope\n# area borders, Supp. Fig. 3 other decoders, Supp. Fig. 4, Supp. Fig. 6). The claim that rests on\n# a Supplementary Figure (supp3-decoder-types) says so. The bioRxiv preprint (10.1101/2023.06.05.543698,\n# version 1) is also in paper/; it was not used. No PDF was supplied, so no figure was read.\n#\n# Code. The paper's Code availability names a Code Ocean capsule, 10.24433/CO.6659254.v2\n# (codeocean.com/capsule/2540707); it returned HTTP 403 from this run and was not read. Read in\n# its place, as the first author's public code for this dataset (its data path is\n# 'S:\\OpenScopeData\\00248_v240130\\'): github.com/hs13/IC_paper_code at commit\n# 50e04eaf7c9192a067c129f3c1f174a27f10c406 (2024-10-27, \"Initial commit\"), cited below as \"the\n# code\". It holds the Neuropixels analysis only, in MATLAB: postprocessnwb_v240130.m (reads the\n# NWB files, trial parsing, response windows), analyzeStaticICtxi.m (IC-encoder, LC-encoder and\n# segment responder definitions), analyzeRFCI.m (receptive fields), merge_postprocessed.m,\n# analyzeICtxi_SVM_areas.m and aggregateICtxi_SVM_trainICRC_areas.m / _trainREx_areas.m (decoding),\n# plot_SVM_*.m, analyze_CCGfftlong.m and computeCCGpeaktroughs.m (raw cross-correlograms),\n# analyzeMouseEye.m, aggregateMouseEye.m and aggregate_fixedgaze.m (eye tracking). The\n# cross-correlogram correction and the Fig. 2d count are not in it; they were read in the same\n# author's larger repository github.com/hs13/Analyze_IC_OpenScope_v240130 at commit\n# 4ee15852ca19bf32ff876ede0598f3099f2e4208 (aggregate_ctxqcCCGfftlong.m), which the paper does not\n# link and which is cited as \"the larger repository\", a lower source than the Methods and the code.\n# No code for the 2p analyses or for the Figure 1 percentages was found.\n#\n# Data the paper describes. Three kinds of experiment.\n# (1) Neuropixels (this dandiset; Data availability gives dandiset 000248): 12 sessions from 12\n# mice, six probes targeted to V1, LM, RL, AL, PM and AM, Allen Brain Observatory pipeline,\n# Kilosort2, spike times per unit. The Methods' Animals list Sst-IRES-Cre;Ai32 (n = 10) and\n# PV-IRES-Cre;Ai32 (n = 4) mice, 14 in all, against 12 elsewhere; the code's CCG script names 12\n# subjects (sub-619293, 619296, 620333, 620334, 625545, 625554, 625555, 630506, 631510, 631570,\n# 633229, 637484). Analyzed units are regular-spiking (RS) units, trough-to-peak width >= 0.4 ms\n# (the code uses the NWB units column waveform_duration > 0.4). A unit's area is the location\n# label of its peak channel (code; 'VISp' and not 'VISpm' for V1). Stimuli, monocular on a monitor\n# 15 cm from the right eye. IC blocks (Extended Data Fig. 1b) ICwcfg1 (default, white circles on\n# black), ICwcfg0 (rotated 315 degrees), ICkcfg1 and ICkcfg0 (black-white inverted); each image\n# 0.4 s with 0.4 s ITI; in ICwcfg1 the IC and LC images 400 times and the others at least 50; in\n# configuration 0 each image 30 times. Images per IC block (code trial codes): blank 0, X 101,\n# TC1 105, IC1 106, LC1 107, TC2 109, LC2 110, IC2 111, IRE1 506, IRE2 511, TRE1 1105, TRE2 1109,\n# XRE1 1201, XRE2 1299, In BR/BL/TL/TR 1301 to 1304, Out BR/BL/TL/TR 1305 to 1308. In the NWB\n# stimulus table of an IC block the code takes every second row from the first non-zero frame\n# (image rows alternate with ITI rows) and maps the frame value to these codes. Receptive field\n# block (RFCI) 16-degree drifting grating patches at 9 positions (center and 8 at 16 degrees), each\n# presentation 4 directions of 0.25 s, 10 repeats; size tuning block (sizeCI) 0 to 64 degrees.\n# Eye tracking video at 30 Hz with pupil ellipse fits in the NWB (EyeTracking); running wheel.\n# (2) 2p calcium imaging (not in this dandiset): V1L2/3 (CaMKII-tTA;tetO-GCaMP6s, 11 sessions from 5\n# mice for decoding; 29 sessions from 5 mice for Fig. 1), V1L4 (Scnn1a-Tg3-Cre;Ai162, 8 sessions\n# from 2 mice), 2p mesoscope (19 sessions from 5 mice); z-scored neuropil-corrected fluorescence.\n# (3) 2p holographic optogenetics (24 sessions from 4 mice, GCaMP6m-ChRmine) and the 2p holographic\n# mesoscope (11 sessions from 2 Vglut1-Cre;Ai203 mice). Not in this dandiset.\n# Outside data. The paper deposits \"Additional postprocessed data\" in the same Code Ocean capsule\n# and does not say what they are; it does not say where the 2p and holography recordings are. The\n# 2p and holography claims are marked data dataset (the paper's own recordings); the author is to\n# find whether any public copy exists.\n#\n# Shared methods, cited below by name.\n# \"IC response\": per trial, the mean spike rate from 0 to 400 ms after image onset (code,\n# postprocessnwb_v240130.m and merge_postprocessed.m, 1 ms bins).\n# \"IC-encoder\" (Methods, Definition of functional subsets; code analyzeStaticICtxi.m): in one IC\n# block, Kruskal-Wallis across blank, IC1, LC1, LC2 and IC2 trials at p < 0.05, then Tukey-Kramer\n# comparisons (MATLAB multcompare default); IC1-encoder when IC1 differs from blank at p < 0.05 with\n# AUROC against blank > 0.5 and neither LC1 nor LC2 differs from blank; IC2 likewise. LC-encoders\n# (Extended Data Fig. 10a) the same with IC and LC exchanged.\n# \"segment responder\" (Methods; code): BR-segment responder when Kruskal-Wallis across blank and\n# the 8 segment images is p < 0.05, a rank-sum test of In BR against Out BR trials is p < 0.05 with\n# AUROC > 0.5, and the unit is neither IC- nor LC-encoder; likewise BL, TL, TR. The Methods name\n# only the rank-sum test; the Kruskal-Wallis gate is the code's.\n# \"decoder\" (Methods, Decoding analysis; code analyzeICtxi_SVM_areas.m): block ICwcfg1; units of\n# one area (RS units for Neuropixels; code aggregate scripts load the 'RS' files); response as the\n# IC response; training classes IC1, LC1, LC2, IC2, trials balanced to the smallest class by taking\n# its first trials; tenfold stratified partition (cvpartition), test sets not overlapping; each\n# fold z-scores every unit by the training trials' mean and SD (NaN set to 0); linear SVM in\n# MATLAB fitcecoc (default one-vs-one coding, templateSVM with Standardize true). Cross-validation\n# accuracy is the mean over the four classes of the fraction of test trials decoded correctly,\n# averaged over folds. Probe trials are decoded by each of the ten fold models and the fractions\n# averaged. Neuropixels areas are kept in a session when it has >= 50 RS units there; 2p areas\n# when >= 100 neurons. Open detail, could change the outcome: the code calls fitcecoc with\n# OptimizeHyperparameters 'auto' (MATLAB Bayesian optimization of the coding and SVM\n# hyperparameters, its default settings), which the Methods do not mention. Readings, run both:\n# (a) fixed defaults, linear SVM with C = 1, one-vs-one; (b) C chosen by an inner cross-validation\n# on the training folds, the Python counterpart of the code's search.\n# \"inference score\" (Results; code aggregateICtxi_SVM_trainICRC_areas.m line 171): with P(x -> y)\n# the fraction of x trials decoded as y, ((P(TRE1->IC1) - P(TRE1->LC1)) + (P(TRE2->IC2) -\n# P(TRE2->LC2)))/2 per session; tested against 0 across sessions with a two-sided Wilcoxon\n# signed-rank test (the same test as IC against LC fractions paired by session).\n# The Statistics section says tests are nonparametric and two-sided unless noted.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000248\"\npaper: doi:10.1038/s41593-025-02055-5\nclaims:\n- id: fig1e-npx-exclusive-center\n  statement: In the Neuropixels data, 18 of 1,804 V1 RS units respond exclusively to the grating\n    patch at the center position (the illusory gap region) of the receptive field mapping block.\n  source: Methods, Definition of functional subsets of neurons, paragraph 1; Figure 1e legend\n  quote: In the Neuropixels data, there were n = 18 exclusively center-responsive neurons of 1,804\n    V1 RS units\n  expected:\n  - quantity: exclusively center-responsive V1 RS units\n    value: 18\n    tolerance: 1.8\n    unit: units\n  - quantity: V1 RS units, all 12 sessions\n    value: 1804\n    tolerance: 180.4\n    unit: units\n  criterion: V1 RS units as in the opening comment. Per RF trial (one presentation of the four\n    directions, 1 s), the mean rate from 0 to 1000 ms after onset (code, postprocessnwb_v240130.m,\n    every fourth row of the RFCI table), standard (not inverse) patches only. The Methods test\n    each position against gray-screen trials with a Wilcoxon rank-sum test, Bonferroni-Holm\n    corrected, and keep units significant at the center only. The RF block has no gray-screen\n    trials (0 s ITI), so what forms the gray-screen sample is open. Readings, (a) the code\n    (analyzeRFCI.m, RFsigexclclassic with RFindclassic = center), a Wilcoxon signed-rank test of\n    each position's trial rates against the unit's mean rate in the longest spontaneous block,\n    the position of largest mean response being the center and the only one significant after the\n    Holm step; (b) the Methods, a rank-sum test of each position's trial rates against rates in\n    1 s windows tiled over the longest spontaneous (gray screen) block, Holm corrected over the 9\n    positions, center the only significant position. Reproduced when, under one reading, both\n    counts are within tolerance.\n- id: fig1f-npx-ic-ire-responsive\n  statement: Of the exclusively center-responsive V1 RS units, 66.7% respond substantially to the\n    IC image and 77.8% to the real-edge (IRE) image of their preferred IRE orientation, although\n    the IC image has no contrast in their receptive field.\n  source: Figure 1f legend; Results, Mouse V1 neurons respond to ICs despite the absence of contrast\n    within their receptive fields, paragraph 2\n  quote: Bottom, individual neurons with substantially I C -responsive (left; 66.7%) and I RE\n    -responsive (right; 77.8%) neurons marked in magenta on the y axis\n  depends_on:\n  - fig1e-npx-exclusive-center\n  expected:\n  - quantity: IC-responsive fraction of exclusively center-responsive units\n    value: 66.7\n    tolerance: 6.67\n    unit: percent\n  - quantity: IRE-responsive fraction of exclusively center-responsive units\n    value: 77.8\n    tolerance: 7.78\n    unit: percent\n  criterion: Units of fig1e-npx-exclusive-center. Preferred IRE orientation is the IRE image with\n    the strongest mean IC response (Results, paragraph 2); the IC image is the one with the illusory\n    bar of that orientation. Neither the Methods nor the code read fixes the test for\n    \"substantially responsive\" or the block. Readings, test (a) the code's analyzeStaticICtxi.m,\n    Kruskal-Wallis across blank, IC and IRE of that orientation at p < 0.05 with Tukey-Kramer\n    comparison against blank at p < 0.05 and mean above blank (sigmcBICREl1/2); (b) a rank-sum test\n    of those trials against blank trials at p < 0.05 with AUROC > 0.5. Block (i) ICwcfg1 only, two\n    orientations (135 and 45 degrees); (ii) ICwcfg1 and ICwcfg0 together, four orientations.\n    Reproduced when, under one combination, both fractions are within tolerance.\n- id: fig1g-npx-orientation-match\n  statement: For IRE-responsive exclusively center-responsive V1 RS units, the preferred\n    orientation of the illusory bar matches that of the real bar in 78.6% of units.\n  source: Figure 1g legend; Results, Mouse V1 neurons respond to ICs despite the absence of contrast\n    within their receptive fields, paragraph 2\n  quote: Comparison of the preferred orientation between illusory bars (I C stimuli) and real bars\n    (I RE stimuli) for I RE -responsive and exclusively center-responsive V1 RS units, showing a\n    78.6% match\n  depends_on:\n  - fig1f-npx-ic-ire-responsive\n  expected:\n    quantity: units whose preferred IC and IRE orientations match\n    value: 78.6\n    tolerance: 7.86\n    unit: percent\n  criterion: Preferred IC (IRE) orientation is that of the IC (IRE) image with the strongest mean\n    IC response (Results, paragraph 2), among the IRE-responsive units of fig1f under the same\n    readings. Reproduced when, under the reading that reproduces fig1f, the match is within\n    tolerance; the fraction is reported for every reading.\n- id: results-npx-units-per-session\n  statement: The Neuropixels sessions hold 150 +/- 20 V1 RS units and 597 +/- 46 higher visual area\n    RS units per session (mean +/- s.e.m., 12 sessions).\n  source: Results, A subpopulation of V1 neurons respond to ICs but not to its inducing segments,\n    paragraph 4\n  quote: 12 sessions from 12 mice; mean ± s.e.m. = 150 ± 20 V1 RS units and 597 ± 46 higher visual\n    area RS units across sessions\n  expected:\n  - quantity: V1 RS units per session, mean\n    value: 150\n    tolerance: 20\n    unit: units\n  - quantity: higher visual area (LM, RL, AL, PM, AM) RS units per session, mean\n    value: 597\n    tolerance: 46\n    unit: units\n  criterion: RS units and areas as in the opening comment, with no further quality filter (the\n    code computes an ISI, amplitude cutoff and presence ratio filter and does not apply it).\n    Tolerances are the paper's s.e.m.\n- id: methods-npx-ic-encoder-count\n  statement: Across the ICwcfg0 and ICwcfg1 blocks, 159 of 1,804 V1 RS units are IC-encoders.\n  source: Methods, Definition of functional subsets of neurons, paragraph 2\n  quote: Across ICwcfg0 and ICwcfg1, 159 of 1,804 V1 RS units were identified as IC-encoders in the\n    Neuropixels dataset\n  expected:\n    quantity: V1 RS IC-encoders across ICwcfg0 and ICwcfg1\n    value: 159\n    tolerance: 15.9\n    unit: units\n  criterion: IC-encoder and IC response as in the opening comment, in each block separately with\n    that block's IC1 and IC2 images. \"Across\" is open. Readings, (a) units that are IC-encoders in\n    at least one of the two blocks; (b) the sum of the two blocks' counts. Reproduced when the count\n    is within tolerance under one reading.\n- id: ed6b-npx-v1-group-counts\n  statement: The Neuropixels data hold 87 V1 IC-encoders and 636 V1 segment responders (the sets\n    whose layer distribution Extended Data Fig. 6b shows).\n  source: Extended Data Fig. 6b legend\n  quote: For the Neuropixels dataset, proportion of V1 IC-encoders (left, n = 87) and V1 segment\n    responders (right, n = 636) in each layer\n  expected:\n  - quantity: V1 IC-encoders\n    value: 87\n    tolerance: 8.7\n    unit: units\n  - quantity: V1 segment responders\n    value: 636\n    tolerance: 63.6\n    unit: units\n  criterion: IC-encoder and segment responder as in the opening comment (segment responders the\n    union over BR, BL, TL, TR). Which units and block are open (Fig. 2d gives 79 and 526, the\n    Methods 159 across two blocks). Readings, (a) RS units, block ICwcfg1; (b) all units not\n    classified as noise, block ICwcfg1; (c) RS units, union of ICwcfg1 and ICwcfg0. Reproduced when\n    both counts are within tolerance under one reading. The layer proportions are shown, with no\n    value to match.\n- id: fig2d-npx-ccg-hva-input\n  statement: V1 IC-encoders (n = 79) are more likely than V1 segment responders (n = 526) to receive\n    putative excitatory connections from higher visual areas, by cross-correlogram analysis.\n  source: Figure 2d legend; Results, A subpopulation of V1 neurons respond to ICs but not to its\n    inducing segments, paragraph 4\n  quote: V1 IC-encoders ( n = 79) are substantially more likely than V1 segment responders ( n =\n    526) to receive putative excitatory connections from higher visual areas (LM, RL, AL, PM and AM)\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 7.0e-6\n    n: 79 V1 IC-encoders and 526 V1 segment responders, 12 sessions from 12 mice\n  expected:\n  - quantity: V1 IC-encoders in the analysis\n    value: 79\n    tolerance: 7.9\n    unit: units\n  - quantity: V1 segment responders in the analysis\n    value: 526\n    tolerance: 52.6\n    unit: units\n  criterion: Methods, Cross-correlogram analysis. Spike trains of cortical RS units over the\n    ICwcfg1 block in 1 ms bins; CCG(tau) = sum over t of x1(t) x2(t + tau) divided by the square\n    root of the two spike counts, tau up to +/- 100 ms (code analyze_CCGfftlong.m); the CCG of the\n    same trains smoothed with a 25 ms window is subtracted; a putative excitatory connection from an\n    HVA unit to a V1 unit when the corrected CCG peak in the 1 to 10 ms window with the HVA unit\n    leading exceeds 7 times the SD of the CCG flank (50 to 100 ms from zero). Groups as in the\n    opening comment, in ICwcfg1 (larger repository, aggregate_ctxqcCCGfftlong.m lines 285 to 287).\n    Open details, each could change the outcome. Smoothing window shape, (a) a 25-bin boxcar, (b) a\n    Gaussian kernel 25 ms long. Flank SD taken from (i) the uncorrected CCG (larger repository,\n    line 77), (ii) the corrected CCG. Per V1 unit measure, (x) the fraction of the session's HVA RS\n    units with a connection to it (larger repository, Pin_flank.HVA), (y) the number of such units.\n    Reproduced when, under every combination, IC-encoders have the higher median and a two-sided\n    rank-sum test gives p < 0.05; not reproduced when none does; when the readings differ the\n    claim is blocked as methods_underspecified with all results shown. Group sizes are compared\n    with the expected counts.\n- id: fig3a-npx-v1-decoding\n  statement: A linear SVM decodes the four images IC1, LC1, LC2 and IC2 from V1 activity in the\n    Neuropixels data with tenfold cross-validation accuracy above the chance of 0.25.\n  source: Figure 3a; Results, Representation of IC inference across the mouse visual cortical\n    hierarchy, paragraph 3\n  quote: The tenfold cross-validation performance was substantially above chance, indicating that\n    neural activity patterns evoked by these four images were highly distinct at the multivariate\n    level\n  criterion: The decoder of the opening comment on V1 RS units, sessions with >= 50 of them. The\n    paper reports no test for Fig. 3a; the code tests the per-session accuracy against 0.25 with a\n    Wilcoxon signed-rank test (aggregateICtxi_SVM_trainICRC_areas.m line 147). Reproduced when the\n    mean accuracy exceeds 0.25 with that test at p < 0.05 under both decoder readings. Accuracy for\n    the other five areas is reported.\n- id: fig3c-npx-v1-inference\n  statement: In Neuropixels V1, TRE trials are decoded as the matching IC image more often than as\n    the matching LC image (0.51 against 0.22), so IC inference is represented in V1.\n  source: Figure 3c; Results, Representation of IC inference across the mouse visual cortical\n    hierarchy, paragraph 4\n  quote: Applying inference decoding to Neuropixels V1 recordings revealed that T RE was\n    substantially more likely to be decoded as I C than as L C (Fig. 3c ; decoding probability for I\n    C vs. L C was 0.51 vs. 0.22, P < 0.05 Wilcoxon signed-rank test)\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.05\n    p_relation: \"<\"\n    n: 12 sessions from 12 mice\n  expected:\n  - quantity: probability TRE decoded as the corresponding IC, V1, mean over sessions\n    value: 0.51\n    tolerance: 0.051\n  - quantity: probability TRE decoded as the corresponding LC, V1, mean over sessions\n    value: 0.22\n    tolerance: 0.022\n  depends_on:\n  - fig3a-npx-v1-decoding\n  criterion: The decoder and inference score of the opening comment on V1 RS units. The IC value\n    is the mean of P(TRE1->IC1) and P(TRE2->IC2), the LC value the mean of P(TRE1->LC1) and\n    P(TRE2->LC2), each averaged over sessions. Reproduced when, under a decoder reading, both values\n    are within tolerance and the signed-rank test of IC against LC gives p < 0.05 with IC higher;\n    partially reproduced when the test holds and a value is outside tolerance.\n- id: fig3d-npx-areas-inference\n  statement: In the Neuropixels data almost every visual area decodes TRE as IC more than as LC,\n    significantly in V1, LM, RL, AL and PM and not in AM, with V1, LM and AL the strongest.\n  source: Figure 3d legend; Results, Representation of IC inference across the mouse visual cortical\n    hierarchy, paragraph 5\n  quote: In the Neuropixels dataset, almost every visual area was substantially biased toward\n    decoding T RE as I C than L C , with V1, LM and AL showing the strongest representations of the\n    IC\n  statistics:\n  - about: V1, 12 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.0132\n  - about: LM, 8 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.0156\n  - about: RL, 11 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.0244\n  - about: AL, 10 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.0039\n  - about: PM, 12 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.0342\n  - about: AM, 11 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.1748\n  criterion: The decoder and inference score of the opening comment per area, sessions with >= 50\n    RS units in the area (the paper keeps 12, 8, 11, 10, 12, 11 sessions for V1, LM, RL, AL, PM,\n    AM; the counts found are reported). \"Strongest\" is open, readings (a) the three largest mean\n    inference scores, (b) the three smallest p-values. Reproduced when at least five areas give p <\n    0.05 with IC above LC and V1, LM and AL are the strongest three under reading (a) or (b);\n    partially reproduced when three or four areas are significant, or when five are and the\n    ranking fails under both readings; not reproduced otherwise.\n- id: ed7a-npx-no-area-above-v1\n  statement: No higher visual area shows a substantially larger inference performance than V1,\n    although decoding accuracy and inference scores differ across areas.\n  source: Results, Representation of IC inference across the mouse visual cortical hierarchy,\n    paragraph 9; Extended Data Fig. 7a and 7c legends\n  quote: Notably, none of the higher visual areas showed a substantially larger inference\n    performance compared to V1 (Extended Data Fig. 7a,c )\n  statistics:\n  - about: cross-validation accuracy across the six areas, Neuropixels (Extended Data Fig. 7a)\n    test: Kruskal-Wallis test\n    p: 0.0019\n  - about: TRE inference score across the six areas, Neuropixels (Extended Data Fig. 7a)\n    test: Kruskal-Wallis test\n    p: 0.0249\n  - about: cross-validation accuracy across areas, XRE decoders (Extended Data Fig. 7c)\n    test: Kruskal-Wallis test\n    p: 0.0005\n  - about: XRE inference score across areas (Extended Data Fig. 7c)\n    test: Kruskal-Wallis test\n    p: 0.0022\n  depends_on:\n  - fig3d-npx-areas-inference\n  - ed7b-npx-xre-inference\n  criterion: A claim of absence. Per-session TRE inference scores (fig3d) and XRE inference scores\n    (ed7b) per area. The paper's test is a Kruskal-Wallis across areas followed by pairwise\n    comparisons it does not name. Readings, (a) two-sided Wilcoxon signed-rank of V1 against each\n    HVA over sessions with both, the pairwise test the code uses between areas\n    (plot_SVM_trainICRC_areas.m line 245); (b) Tukey-Kramer comparisons after the Kruskal-Wallis\n    (MATLAB multcompare default). Reproduced when no HVA has a significantly larger score than V1\n    (p < 0.05) for either score; not reproduced when one does. Extended Data Fig. 7c is said to show\n    the data of panel b, which mixes the Neuropixels and 2p areas; its Kruskal-Wallis values are\n    compared on the six Neuropixels areas and the reading is a deviation. The Kruskal-Wallis\n    p-values found are reported against the paper's.\n- id: ed7b-npx-xre-inference\n  statement: Decoders trained on the XRE real-bar images classify IC1 and IC2 trials as the XRE\n    image whose real bar matches the illusory bar, above chance in all six Neuropixels areas.\n  source: Extended Data Fig. 7b legend; Results, Representation of IC inference across the mouse\n    visual cortical hierarchy, paragraph 7\n  quote: As with T RE inference decoding (Fig. 2 ), layer 2/3 of V1 and LM consistently show high\n    inference scores (*p < 0.05, Wilcoxon signed-rank test compared to chance of 0.5\n  statistics:\n  - about: V1, 12 sessions\n    test: Wilcoxon signed-rank test against 0.5\n    p: 0.0005\n  - about: LM, 8 sessions\n    test: Wilcoxon signed-rank test against 0.5\n    p: 0.0078\n  - about: RL, 11 sessions\n    test: Wilcoxon signed-rank test against 0.5\n    p: 0.0049\n  - about: AL, 10 sessions\n    test: Wilcoxon signed-rank test against 0.5\n    p: 0.0020\n  - about: PM, 12 sessions\n    test: Wilcoxon signed-rank test against 0.5\n    p: 0.0005\n  - about: AM, 11 sessions\n    test: Wilcoxon signed-rank test against 0.5\n    p: 0.0137\n  criterion: The decoder of the opening comment trained on XRE1 against XRE2 trials (codes 1201,\n    1299) of ICwcfg1, probed with IC1 and IC2 trials (code svmdesc trainREx); XRE inference score\n    (P(IC1->XRE1) + P(IC2->XRE2))/2 (Extended Data Fig. 7b legend) per session and area, sessions\n    with >= 50 RS units. Reproduced when the score is above 0.5 with a signed-rank p < 0.05 in all\n    six areas; partially reproduced in four or five; not reproduced otherwise.\n- id: ed6ef-npx-ic-not-greater\n  statement: In the Neuropixels data, IC images do not evoke larger population average responses\n    than LC images in any area, averaged over all units or over visually responsive units.\n  source: Extended Data Fig. 6e and 6f legends\n  quote: I C images do not evoke greater responses than L C images (*p < 0.05 one-tailed Wilcoxon\n    signed-rank test for testing I C > L C ; note that none of the visual areas showed significance)\n  statistics:\n  - about: all units, V1\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.9614\n  - about: all units, LM\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.9805\n  - about: all units, RL\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.7676\n  - about: all units, AL\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.7217\n  - about: all units, PM\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.9895\n  - about: all units, AM\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.8398\n  - about: visually responsive units, V1\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.9788\n  - about: visually responsive units, LM\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.9805\n  - about: visually responsive units, RL\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.7114\n  - about: visually responsive units, AL\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.7842\n  - about: visually responsive units, PM\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.9866\n  - about: visually responsive units, AM\n    test: one-tailed Wilcoxon signed-rank test, IC > LC\n    p: 0.6499\n  criterion: A claim of absence, on the paper's test. Same sessions as fig3d (>= 50 RS units in the\n    area); ICwcfg1; per session, the IC response averaged over (e) all RS units of the area, (f)\n    visually responsive RS units (Kruskal-Wallis across blank, IC1, LC1, LC2, IC2 at p < 0.05,\n    Extended Data Fig. 6d legend), on IC trials (IC1 and IC2 pooled) and on LC trials (LC1 and LC2\n    pooled); one-tailed signed-rank test of IC > LC across sessions. Reproduced when no area gives p\n    < 0.05 in either panel; not reproduced when any does. The mean IC minus LC difference per area\n    is reported.\n- id: ed2b-npx-fixed-gaze\n  statement: Limiting the Neuropixels analysis to fixed-gaze trials (pupil within 8 degrees of its\n    modal position) leaves 11 exclusively center-responsive V1 RS units, and their responses to ICs\n    and orientation match do not change the conclusion.\n  source: Extended Data Fig. 2b to 2e legends; Results, Mouse V1 neurons respond to ICs despite the\n    absence of contrast within their receptive fields, paragraph 3\n  quote: When analyzing only fixed-gaze trials, there were n = 11 exclusively center-responsive V1\n    RS units; 10 sessions had eye tracking data and of these, 9 sessions had a valid receptive field\n    mapping block where the fixed-gaze constraint left at least one trial in each position\n  depends_on:\n  - fig1e-npx-exclusive-center\n  - fig1g-npx-orientation-match\n  expected:\n  - quantity: exclusively center-responsive V1 RS units, fixed-gaze trials\n    value: 11\n    tolerance: 1.1\n    unit: units\n  - quantity: sessions with eye tracking data\n    value: 10\n    tolerance: 0\n    unit: sessions\n  - quantity: sessions with a valid fixed-gaze receptive field block\n    value: 9\n    tolerance: 0\n    unit: sessions\n  criterion: Fixed-gaze trials per the Methods (Eye tracking analysis), pupil position within 8\n    visual degrees of the modal pupil position throughout the trial. The code (analyzeMouseEye.m)\n    uses the NWB EyeTracking pupil fits, a threshold of 20 camera pixels (its stand-in for 8\n    degrees) on the maximum distance from the mode during the trial, and drops likely blinks; the\n    pixel threshold is run as a variant, as the Methods give degrees and no conversion is in the\n    paper. Then fig1e, fig1f and fig1g are repeated on fixed-gaze trials only, in the sessions whose\n    fixed-gaze RF trials cover all 9 positions. Session counts must match exactly. Reproduced when\n    the unit count is within tolerance and the IC-IRE orientation match exceeds the 95th percentile\n    of 1,000 shuffles of the preferred IC orientations among those units (the null of Extended Data\n    Fig. 2e; the shuffle count is a standard choice); partially reproduced when one holds.\n- id: ed2f-npx-rf-match\n  statement: Receptive field positions mapped with fixed-gaze trials match those mapped with all\n    trials for 81% of the 398 V1 RS units with significant receptive fields.\n  source: Extended Data Fig. 2f legend\n  quote: Match proportion is 0.81 among 398 V1 RS units with significant receptive fields (p < 0.05\n    Kruskal-Wallis test across responses to 9 positions in the receptive field mapping block)\n  expected:\n  - quantity: fraction of units with the same RF position under fixed-gaze and all trials\n    value: 0.81\n    tolerance: 0.081\n  - quantity: V1 RS units with significant receptive fields\n    value: 398\n    tolerance: 39.8\n    unit: units\n  criterion: RF position is the position of largest mean RF-trial response (code analyzeRFCI.m,\n    RFindclassic); significant receptive field when the Kruskal-Wallis across the 9 positions gives\n    p < 0.05 (legend). Fixed-gaze trials as in ed2b, sessions with eye tracking. Open, which mapping\n    must be significant. Readings, (a) significant with all trials; (b) significant with\n    fixed-gaze trials; (c) both. Reproduced when both values are within tolerance under one reading.\n- id: ed2g-npx-pupil-area\n  statement: Pupil area during the presentation does not differ across the images of the IC block.\n  source: Extended Data Fig. 2g legend\n  quote: Pupil area, z-scored across each recording session, during visual presentation of various\n    images in the IC block (n = 10 sessions with eye tracking data; p = 0.7220 Friedman test)\n  statistics:\n  - test: Friedman test\n    p: 0.722\n    n: 10 sessions with eye tracking data\n  criterion: A claim of absence, on the paper's test. Pupil area from the NWB pupil fits, z-scored\n    over the session; per trial its mean over the 0 to 0.4 s presentation (the code's\n    aggregateMouseEye.m also computes the end and maximum value; the mean is used, the others\n    shown); per session and image the mean over trials; a Friedman test with sessions as blocks.\n    Open, which images. Readings, (a) IC1, LC1, LC2, IC2 of ICwcfg1, the images the code compares;\n    (b) all 22 images of ICwcfg1. Reproduced when p >= 0.05 under the readings; when they differ,\n    blocked as methods_underspecified.\n- id: ed2a-npx-gaze-confined\n  statement: Eye gaze is confined to a small region that fits within the illusory gap, with no\n    systematic difference in pupil position among IC1, LC1, LC2 and IC2 presentations.\n  source: Extended Data Fig. 2a legend; Results, A subpopulation of V1 neurons respond to ICs but\n    not to its inducing segments, paragraph 3\n  quote: Mouse eye gaze is confined to a small region that fits within the illusory gap region.\n    There are no systematic differences in pupil position among I C1 vs. L C1 vs. L C2 vs. I C2\n    presentations\n  criterion: The paper names no test and gives no pixel to degree conversion. Pupil center from the\n    NWB pupil fits during the 0 to 0.4 s presentation of IC1, LC1, LC2, IC2 trials in ICwcfg1. A\n    claim of absence with no test in the paper, so the test is open. Readings, (a) per session, a\n    Kruskal-Wallis across the four images of the trial mean pupil x and of y; (b) across sessions,\n    a Friedman test of the per-session image means of x and of y. Reproduced when no test gives p <\n    0.05 after Bonferroni over x and y under both readings, and blocked as methods_underspecified\n    when the readings differ. The confinement part is reported as the extent of the 0.01 isoline of\n    each session's 2D density in camera pixels, with no conversion to degrees.\n- id: supp3-decoder-types\n  statement: Decoders of other kinds (quadratic and radial basis function SVMs, a fully connected\n    neural network) give results highly consistent with the linear SVM.\n  source: Results, Representation of IC inference across the mouse visual cortical hierarchy,\n    paragraph 8; Supplementary Fig. 3 (not read); Methods, Decoding analysis, paragraph 3\n  quote: In addition, different types of decoders yielded highly consistent results (Supplementary\n    Fig. 3 )\n  criterion: Supplementary Fig. 3 was not available, so which dataset and areas it shows is not\n    known. Methods, SVMs with linear, quadratic polynomial and RBF kernels, and an ANN (input layer\n    of one node per unit, two hidden layers of 100 nodes, four softmax outputs, Adam, cross-entropy\n    loss, 50,000 epochs), all with tenfold cross-validation. Tested on the Neuropixels areas, a\n    reading recorded as a deviation. Reproduced when each decoder gives the same sign and\n    significance (signed-rank p < 0.05) as the linear SVM for the TRE inference score in V1, LM and\n    AL; partially reproduced when two of three agree.\n- id: fig1ik-2p-exclusive-center\n  statement: In the 2p data, 310 of 18,576 V1L2/3 neurons are exclusively center-responsive; 21.3%\n    of them respond to the IC and 43.2% to the IRE image, and preferred IC and IRE orientations\n    match in 54.5%.\n  source: Figure 1i to 1k legend; Methods, Definition of functional subsets of neurons, paragraph 1\n  quote: Bottom, individual neurons with substantially I C -responsive (left; 21.3%) and I RE\n    -responsive (right; 43.2%) neurons marked in magenta on the y axis. There was a 54.5% match\n  data: dataset\n  expected:\n  - quantity: exclusively center-responsive V1L2/3 neurons\n    value: 310\n    tolerance: 31\n    unit: neurons\n  - quantity: V1L2/3 neurons\n    value: 18576\n    tolerance: 1857.6\n    unit: neurons\n  - quantity: IC-responsive fraction\n    value: 21.3\n    tolerance: 2.13\n    unit: percent\n  - quantity: IRE-responsive fraction\n    value: 43.2\n    tolerance: 4.32\n    unit: percent\n  - quantity: IC-IRE orientation match\n    value: 54.5\n    tolerance: 5.45\n    unit: percent\n  criterion: 2p imaging, 29 sessions from five mice, not in this dandiset. Methods as in fig1e to\n    fig1g on z-scored fluorescence averaged over the 1 s presentation, with the same open details.\n- id: fig2b-2p-ic-encoder-fraction\n  statement: About 4.3% of V1L2/3 neurons are IC-encoders (selective for one of the two IC images\n    with no substantial response to either LC image), 8.5% over both white-circle configurations.\n  source: Results, A subpopulation of V1 neurons respond to ICs but not to its inducing segments,\n    paragraph 3; Methods, Definition of functional subsets of neurons, paragraph 2\n  quote: Using these stimuli, we identified approximately 4.3% of neurons in V1L2/3 with\n    selectivity for one of the two I C images, and no substantial responses to either L C image\n  expected:\n  - quantity: IC-encoder fraction in V1L2/3, one configuration\n    value: 4.3\n    tolerance: 0.43\n    unit: percent\n  - quantity: IC-encoder fraction in V1L2/3, both white-circle configurations\n    value: 8.5\n    tolerance: 0.85\n    unit: percent\n  - quantity: V1L2/3 IC-encoders across ICwcfg0 and ICwcfg1 (Methods, 1,569 of 18,576)\n    value: 1569\n    tolerance: 156.9\n    unit: neurons\n  criterion: 2p imaging, not in this dandiset. IC-encoder as in the opening comment on z-scored\n    fluorescence over the 1 s presentation.\n- id: fig2c-2p-orientation-tuning\n  statement: V1L2/3 IC-encoders are tuned to the orientation of the illusory bar of their IC image,\n    measured with single long bars, for white-circle and black-circle blocks alike.\n  source: Figure 2c legend; Extended Data Fig. 5b legend\n  quote: Indeed, IC-encoders in V1L2/3 were tuned to the orientation of the illusory bar in the I C\n    image (I C1 -encoders were tuned to 135°, and I C2 -encoders were tuned to 45°)\n  statistics:\n  - about: illusory bar against orthogonal orientation, Fig. 2c\n    test: Wilcoxon signed-rank test\n    p: 1.8e-5\n    n: 11 sessions from five mice\n  - about: white-circles block, Extended Data Fig. 5b\n    test: Wilcoxon signed-rank test\n    p: 0.0017\n    n: 93 IC1-encoders and 159 IC2-encoders\n  - about: black-circles block, Extended Data Fig. 5b\n    test: Wilcoxon signed-rank test\n    p: 2.6e-8\n    n: 409 IC1-encoders and 482 IC2-encoders\n  criterion: 2p imaging, not in this dandiset. Reproduced when the response to the single bar at the\n    illusory bar's orientation exceeds that at the orthogonal orientation by a signed-rank test at\n    p < 0.05 over IC-encoders.\n- id: ed4c-2p-ic-encoder-rf-anywhere\n  statement: IC-encoders' receptive fields are not biased toward the illusory gap region, while\n    segment responders' receptive fields are biased toward the segments that define them.\n  source: Extended Data Fig. 4c legend; Results, A subpopulation of V1 neurons respond to ICs but\n    not to its inducing segments, paragraph 6\n  quote: IC-encoders’ receptive fields are not biased toward the illusory gap region (n = 367/386 I\n    C1 /I C2 -encoders in 24 sessions from 4 mice). On the contrary, segment responders’ receptive\n    fields are biased toward the image segments that are used to define them\n  criterion: 2p imaging, not in this dandiset. The paper names no test for panel c; Extended Data\n    Fig. 4g compares with 95% bootstrapped confidence intervals of IC-responsive and LC-responsive\n    neurons, the comparison used. Reproduced when the IC-encoders' fraction with RF at the center is\n    inside that interval and each segment responder group's most common RF position is its segment.\n- id: ed5cd-2p-rf-size\n  statement: IC-encoders do not have larger receptive fields than other V1L2/3 neurons, by size\n    tuning and by the number of grating patches they respond to.\n  source: Results, A subpopulation of V1 neurons respond to ICs but not to its inducing segments,\n    paragraph 6; Extended Data Fig. 5c and 5d legends\n  quote: Furthermore, IC-encoders did not have substantially larger receptive fields compared to\n    other neurons in V1L2/3\n  criterion: 2p imaging, not in this dandiset. A claim of absence; the paper's comparison is the 95%\n    bootstrapped confidence interval of the number of patches IC-encoders respond to against that\n    of IC-responsive neurons (Extended Data Fig. 5d). Reproduced when the intervals overlap.\n- id: fig3e-2p-l23-not-l4\n  statement: Inference decoding is significant in V1L2/3 and not in V1L4, so V1L2/3 is the lowest\n    region of the visual hierarchy where IC inference is represented.\n  source: Results, Representation of IC inference across the mouse visual cortical hierarchy,\n    paragraph 4; Figure 3e legend\n  quote: Whereas V1L2/3 showed substantial inference decoding performance, V1L4 did not (Fig. 3e )\n  statistics:\n  - about: V1L4, 8 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.3125\n  - about: V1L2/3, 11 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.0049\n  criterion: 2p imaging, not in this dandiset. Decoder and inference score of the opening comment on\n    z-scored fluorescence over the 1 s presentation. Reproduced when V1L2/3 gives p < 0.05 with IC\n    above LC and V1L4 does not.\n- id: fig3e-2p-mesoscope-areas\n  statement: In the 2p mesoscope data, V1 and LM show significant IC inference, and RL, AL, PM and\n    AM do not.\n  source: Results, Representation of IC inference across the mouse visual cortical hierarchy,\n    paragraph 5; Figure 3e legend\n  quote: Similarly, L2/3 of V1 and LM showed the strongest IC representation in the 2p mesoscope\n    dataset (Fig. 3e )\n  statistics:\n  - about: mesoscope V1, 19 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.0196\n  - about: LM, 8 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.0391\n  - about: RL, 15 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.2293\n  - about: AL, 2 sessions\n    test: Wilcoxon signed-rank test\n    p: 1.0\n  - about: PM, 6 sessions\n    test: Wilcoxon signed-rank test\n    p: 0.4375\n  - about: AM, 1 session\n    test: Wilcoxon signed-rank test\n    p: 1.0\n  criterion: 2p mesoscope, not in this dandiset. As fig3e-2p-l23-not-l4, areas with >= 100 neurons.\n    Reproduced when V1 and LM give p < 0.05 with IC above LC.\n- id: ed7b-2p-xre-inference\n  statement: XRE inference decoding gives results consistent with TRE inference decoding in the 2p\n    data, significant in V1L2/3, mesoscope V1, LM and RL and not in V1L4.\n  source: Extended Data Fig. 7b legend; Results, Representation of IC inference across the mouse\n    visual cortical hierarchy, paragraph 7\n  quote: When applying X RE inference decoding to different visual areas, we found consistent\n    results as T RE inference decoding\n  statistics:\n  - about: V1L4\n    test: Wilcoxon signed-rank test against 0.5\n    p: 0.4609\n  - about: V1L2/3\n    test: Wilcoxon signed-rank test against 0.5\n    p: 0.0020\n  - about: mesoscope V1\n    test: Wilcoxon signed-rank test against 0.5\n    p: 0.0007\n  - about: LM\n    test: Wilcoxon signed-rank test against 0.5\n    p: 0.0078\n  - about: RL\n    test: Wilcoxon signed-rank test against 0.5\n    p: 0.0054\n  criterion: 2p imaging, not in this dandiset. As ed7b-npx-xre-inference on the 2p sessions.\n- id: ed5e-2p-inverted\n  statement: Inference decoding indicates IC inference in V1L2/3 for white-circle and for\n    black-circle (inverted) blocks alike.\n  source: Extended Data Fig. 5e legend; Results, Representation of IC inference across the mouse\n    visual cortical hierarchy, paragraph 8\n  quote: We found that inference decoding indicated the representation of IC inference in V1L2/3\n    regardless of black–white inversion (Extended Data Fig. 5e )\n  statistics:\n  - about: white-circles blocks\n    test: Wilcoxon signed-rank test\n    p: 0.0020\n    n: 11 sessions\n  - about: black-circles blocks\n    test: Wilcoxon signed-rank test\n    p: 0.0273\n    n: 9 sessions\n  criterion: 2p imaging, not in this dandiset. Reproduced when both block types give p < 0.05 with\n    IC above LC.\n- id: ed4hi-2p-scaled-images\n  statement: With IC block images scaled up 1.5 times, decoding accuracy is above chance and the\n    TRE inference score above zero in V1L2/3.\n  source: Extended Data Fig. 4h and 4i legend\n  quote: Decoder performance for images scaled up by 1.5× (n = 10 sessions from 5 mice)\n  statistics:\n  - about: cross-validation accuracy against 0.25\n    test: Wilcoxon signed-rank test\n    p: 0.002\n  - about: TRE inference score against 0\n    test: Wilcoxon signed-rank test\n    p: 0.002\n  criterion: 2p imaging, not in this dandiset. Reproduced when both tests give p < 0.05 in the\n    stated direction.\n- id: ed3-2p-robust-gap-mapping-contrast\n  statement: V1L2/3 neurons with receptive fields in the gap respond to illusory bars with the\n    orientation selectivity of real bars also with larger gaps, dense receptive field mapping and\n    contrast bars.\n  source: Results, Mouse V1 neurons respond to ICs despite the absence of contrast within their\n    receptive fields, paragraph 3; Extended Data Fig. 3 legend\n  quote: We further verified the illusory bar responsiveness and orientation selectivity for\n    exclusively center-responsive V1 neurons using larger illusory gap sizes (Extended Data Fig.\n    3a–d ), denser receptive field mappings (Extended Data Fig. 3e–h ) and contrast bars instead of\n    outline bars\n  expected:\n  - quantity: exclusively center-responsive neurons, 24-degree gap sessions\n    value: 32\n    tolerance: 3.2\n    unit: neurons\n  - quantity: center-RF neurons, dense mapping sessions\n    value: 71\n    tolerance: 7.1\n    unit: neurons\n  - quantity: exclusively center-responsive neurons, 50% contrast sessions\n    value: 38\n    tolerance: 3.8\n    unit: neurons\n  criterion: 2p imaging, not in this dandiset. Reproduced when in each variant the IC-IRE\n    orientation match exceeds the 95th percentile of shuffled matches (the null the legends show).\n- id: fig4a-2p-zeroing-ic-encoders\n  statement: Zeroing out IC-encoders in the input of a trained V1L2/3 decoder abolishes the TRE\n    inference performance, while zeroing out segment responders does not.\n  source: Figure 4a legend; Results, Neurons that respond emergently to ICs mediate the\n    representation of inference in V1, paragraphs 2 and 4\n  quote: Indeed, this abolished the IC inference performance; T RE -responses were no longer biased\n    toward being classified as I C compared to L C (Fig. 4a , right)\n  statistics:\n  - about: cross-validation accuracy across subsets\n    test: Friedman test\n    p: 1.1e-5\n    n: 24 sessions from four mice\n  - about: TRE inference performance across subsets\n    test: Friedman test\n    p: 0.0019\n    n: 24 sessions from four mice\n  - about: TRE inference, first subset of the figure\n    test: Wilcoxon signed-rank test\n    p: 0.0177\n  - about: TRE inference, second subset of the figure\n    test: Wilcoxon signed-rank test\n    p: 0.1228\n  - about: TRE inference, third subset of the figure\n    test: Wilcoxon signed-rank test\n    p: 0.0089\n  criterion: 2p holography sessions (visual block), not in this dandiset. The legend gives the\n    per-subset p-values in the figure's order without naming the subsets in text; read from the\n    Results, the non-significant one (0.1228) is the IC-encoders-zeroed decoder. Reproduced when\n    zeroing IC-encoders gives a TRE inference test p >= 0.05 and zeroing segment responders gives p\n    < 0.05 with IC above LC.\n- id: fig4b-2p-ic-encoders-only\n  statement: A decoder trained only on IC-encoders (30 +/- 4 per session) shows high TRE inference\n    performance, while one trained only on segment responders (69 +/- 8) does not, though both\n    discriminate IC from LC images.\n  source: Figure 4b legend; Results, Neurons that respond emergently to ICs mediate the\n    representation of inference in V1, paragraphs 3 and 4\n  quote: Despite training this decoder on the activity of drastically fewer cells, it showed high\n    levels of IC inference performance (Fig. 4b , right)\n  statistics:\n  - about: cross-validation accuracy across subsets\n    test: Friedman test\n    p: 0.0025\n  - about: TRE inference score across subsets\n    test: Friedman test\n    p: 0.0208\n  - about: TRE inference, first subset of the figure\n    test: Wilcoxon signed-rank test\n    p: 0.0177\n  - about: TRE inference, second subset of the figure\n    test: Wilcoxon signed-rank test\n    p: 0.0004\n  - about: TRE inference, third subset of the figure\n    test: Wilcoxon signed-rank test\n    p: 0.2472\n  expected:\n  - quantity: IC-encoders per session\n    value: 30\n    tolerance: 4\n    unit: neurons\n  - quantity: segment responders per session\n    value: 69\n    tolerance: 8\n    unit: neurons\n  criterion: 2p holography sessions, not in this dandiset. Reproduced when the IC-encoder-only\n    decoder's TRE inference test gives p < 0.05 with IC above LC and the segment-responder-only\n    decoder's does not.\n- id: fig5c-2p-holo-ic-responsive\n  statement: Photoactivating IC-encoders evokes larger activity in nonphotoactivated IC-responsive\n    neurons than in non-IC-responsive neurons, while photoactivating segment responders does not.\n  source: Results, Neurons that encode IC inference drive neural pattern completion within V1,\n    paragraph 4; Figure 5c; Extended Data Fig. 8b legend\n  quote: Despite this heterogeneity, targeting IC-encoders evoked substantially larger activity in I\n    C -responsive neurons compared to non-I C -responsive neurons during the photoactivation window\n  statistics:\n  - about: IC-encoder ensembles\n    test: one-tailed Wilcoxon signed-rank test\n    p: 0.0023\n    n: 32 holographic ensembles\n  - about: segment responder ensembles\n    test: one-tailed Wilcoxon signed-rank test\n    p: 0.966\n    n: 37 holographic ensembles\n  criterion: 2p holography, not in this dandiset. Reproduced when the IC-encoder test gives p < 0.05\n    and the segment responder test does not.\n- id: fig5-2p-holo-suppression\n  statement: Photoactivating a sparse ensemble of V1L2/3 excitatory neurons leads on average to a\n    prolonged suppression of the nonphotoactivated population.\n  source: Results, Neurons that encode IC inference drive neural pattern completion within V1,\n    paragraph 4; Figure 5c\n  quote: Consistent with prior reports, photoactivating a sparse ensemble of excitatory neurons in\n    V1L2/3 led to a prolonged suppression of the nonphotoactivated population on average\n  criterion: 2p holography, not in this dandiset. No test is reported; reproduced when the mean\n    baseline-subtracted response of nonphotoactivated neurons after the photoactivation window is\n    below zero.\n- id: fig5d-2p-ic-encoder-pattern-completion\n  statement: Holographic activation of IC-encoders is decoded as the corresponding IC image, both\n    from all neurons and from nonphotoactivated neurons only (median 0.372), in the absence of any\n    visual stimulus.\n  source: Figure 5d legend; Results, Neurons that encode IC inference drive neural pattern\n    completion within V1, paragraph 6\n  quote: Indeed, the decoder constructed with nonphotoactivated neurons was able to classify\n    IC-encoder photoactivation trials as the corresponding I C image\n  statistics:\n  - about: all imaged neurons\n    test: one-tailed Wilcoxon signed-rank test against chance\n    p: 7.9e-7\n    n: 32 IC-encoder ensembles\n  - about: nonphotoactivated neurons\n    test: one-tailed Wilcoxon signed-rank test against chance\n    p: 4.3e-5\n    n: 32 IC-encoder ensembles\n  expected:\n    quantity: median decoding performance, nonphotoactivated neurons\n    value: 0.372\n    tolerance: 0.0372\n  criterion: 2p holography, not in this dandiset. Reproduced when both tests give p < 0.05 above\n    chance (0.25).\n- id: fig5e-2p-segment-no-completion\n  statement: Holographic activation of segment responders is decoded as the corresponding IC image\n    from all neurons, but not from nonphotoactivated neurons (median 0.228).\n  source: Figure 5e legend; Results, Neurons that encode IC inference drive neural pattern\n    completion within V1, paragraph 6\n  quote: In contrast, photoactivating a similar number of segment responders did not evoke\n    decodable activity patterns (Fig. 5e , right, and Extended Data Fig. 9c,d,g,h )\n  statistics:\n  - about: all imaged neurons\n    test: one-tailed Wilcoxon signed-rank test against chance\n    p: 0.0029\n    n: 37 segment responder ensembles\n  - about: nonphotoactivated neurons\n    test: one-tailed Wilcoxon signed-rank test against chance\n    p: 0.3254\n    n: 37 segment responder ensembles\n  expected:\n    quantity: median decoding performance, nonphotoactivated neurons\n    value: 0.228\n    tolerance: 0.0228\n  criterion: 2p holography, not in this dandiset. Reproduced when the all-neuron test gives p < 0.05\n    and the nonphotoactivated test does not.\n- id: ed9b-2p-holo-near-visual\n  statement: Decoding IC-encoder holography trials with a decoder trained on visual trials\n    approaches the cross-validation accuracy on held-out visual trials (0.4029 against 0.4818), and\n    the effect correlates with the number of targets.\n  source: Results, Neurons that encode IC inference drive neural pattern completion within V1,\n    paragraphs 6 and 7; Extended Data Fig. 9b\n  quote: mean ± s.e.m. performance for decoding holography trials as visual image labels was 0.4029\n    ± 0.0296, whereas cross-validation accuracy was 0.4818 ± 0.0165\n  expected:\n  - quantity: holography trials decoded as the expected visual label, mean\n    value: 0.4029\n    tolerance: 0.0296\n  - quantity: cross-validation accuracy of the same decoders, mean\n    value: 0.4818\n    tolerance: 0.0165\n  criterion: 2p holography, not in this dandiset. Tolerances are the paper's s.e.m.; the Spearman\n    correlation with target number is reproduced when positive at p < 0.05.\n- id: ed10-2p-lc-encoders-weaker\n  statement: LC-encoders are less potent than IC-encoders at driving pattern completion, even when\n    matched in visual information.\n  source: Results, Neurons that encode IC inference drive neural pattern completion within V1,\n    paragraph 8; Extended Data Fig. 10e and 10g legends\n  quote: LC-encoders were substantially less potent at driving pattern completion of L C\n    representations compared to IC-encoders\n  statistics:\n  - about: nonphotoactivated decoding across LC-encoder, IC-encoder and segment responder ensembles\n    test: Kruskal-Wallis test, then Bonferroni-Holm corrected Wilcoxon rank-sum tests\n    p: 0.0012\n    n: 35, 32 and 37 ensembles\n  - about: same, bootstrapped groups matched in visual information\n    test: Kruskal-Wallis test, then Bonferroni-Holm corrected Wilcoxon rank-sum tests\n    p: 0.0022\n    n: 48 ensembles per group\n  criterion: 2p holography, not in this dandiset. Reproduced when both Kruskal-Wallis tests give p\n    < 0.05 and IC-encoders exceed LC-encoders in the corrected rank-sum test.\n- id: fig6d-meso-ic-encoders-local\n  statement: On the 2p holographic mesoscope, photoactivating V1 IC-encoders is decoded as the\n    corresponding image from all neurons, but not from nonphotoactivated neurons in higher visual\n    areas.\n  source: Figure 6d legend; Results, IC encoding is mediated by a looped circuit in the visual\n    cortical hierarchy, paragraph 4\n  quote: In stark contrast to pattern completion effects within V1L2/3 (Fig. 5d,e , right), V1\n    segment responders, but not V1 IC-encoders, drove IC representation in higher visual areas\n  statistics:\n  - about: all neurons\n    test: one-tailed Wilcoxon signed-rank test against chance\n    p: 0.001\n    n: 11 IC-encoder ensembles\n  - about: nonphotoactivated neurons in higher visual areas\n    test: one-tailed Wilcoxon signed-rank test against chance\n    p: 0.3501\n    n: 11 IC-encoder ensembles\n  criterion: 2p holographic mesoscope, not in this dandiset. Reproduced when the all-neuron test\n    gives p < 0.05 and the higher visual area test does not.\n- id: fig6e-meso-segment-feedforward\n  statement: On the 2p holographic mesoscope, photoactivating V1 segment responders drives IC\n    representations in nonphotoactivated neurons of higher visual areas.\n  source: Figure 6e legend; Results, IC encoding is mediated by a looped circuit in the visual\n    cortical hierarchy, paragraph 4\n  quote: These data demonstrate that V1 segment responders drive feedforward communication of the\n    bottom-up sensory information to higher visual areas\n  statistics:\n  - about: all neurons\n    test: one-tailed Wilcoxon signed-rank test against chance\n    p: 0.0047\n    n: 22 segment responder ensembles\n  - about: nonphotoactivated neurons in higher visual areas\n    test: one-tailed Wilcoxon signed-rank test against chance\n    p: 0.0457\n    n: 22 segment responder ensembles\n  expected:\n    quantity: median decoding performance, nonphotoactivated higher visual area neurons\n    value: 0.278\n    tolerance: 0.0278\n  criterion: 2p holographic mesoscope, not in this dandiset. Reproduced when both tests give p <\n    0.05 above chance.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000248/10.1038-s41593-025-02055-5.yaml paper/10.1038-s41593-025-02055-5.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The one flag is Fig. 2d's p printed as "7.0 × 10 −6"; I confirmed it in the legend, and the checker's printed forms just don't include "7.0". Now checking the style rules.

**Agent calls Bash**

```bash
cd  f=claims/000248/10.1038-s41593-025-02055-5.yaml; grep -n "—\|rather" $f; python3 - <<'E'
import yaml
f='claims/000248/10.1038-s41593-025-02055-5.yaml'
ev=yaml.compose(open(f).read())
def walk(n):
    if isinstance(n,yaml.ScalarNode):
        if n.style is None and ': ' in n.value: print('colon', n.start_mark.line+1, n.value[:60])
    elif isinstance(n,yaml.MappingNode):
        for k,v in n.value: walk(k); walk(v)
    elif isinstance(n,yaml.SequenceNode):
        for v in n.value: walk(v)
walk(ev)
d=yaml.safe_load(open(f)); print(len(d['claims']), sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']))
E
```

```
39 21 39
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000248/10.1038-s41593-025-02055-5.yaml",
 "old_string": "    -responsive (right; 43.2%) neurons marked in magenta on the y axis. There was a 54.5% match\n  data: dataset\n",
 "new_string": "    -responsive (right; 43.2%) neurons marked in magenta on the y axis. There was a 54.5% match\n"
}
```

```
The file claims/000248/10.1038-s41593-025-02055-5.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000248/10.1038-s41593-025-02055-5.yaml paper/10.1038-s41593-025-02055-5.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/000248/10.1038-s41593-025-02055-5.yaml`. It has 39 claims, every one with a quote and a criterion, and 21 with statistics (73 values in all). The checker passes all quotes and the schema, with one flag left: Fig. 2d's p, which the paper prints as "7.0 × 10 −6". I confirmed it by reading the legend; the checker only looks for the form "7 × 10-6". Nothing was committed.

**Text read**
- I used the version of record (Nature Neuroscience 28, 2319–2329, from Europe PMC): main text, figure legends, Methods and all ten Extended Data legends.
- The Supplementary Information (Supplementary Results and Supp. Figs 1–8) is not in `paper/` and was not read. The main findings rest on the main and Extended Data figures; the supplement is cited only in support. The one claim that rests on it (`supp3-decoder-types`) says so.
- There was no PDF. I did not use the preprint.

**Code**
- The paper's Code Ocean capsule (10.24433/CO.6659254.v2) returned HTTP 403 from here, so I could not read it.
- In its place I read the first author's GitHub repo `hs13/IC_paper_code` at commit 50e04ea. It is MATLAB and covers only the Neuropixels analysis: unit and area selection, response windows, the IC-encoder and segment responder tests, decoding, raw cross-correlograms and eye tracking.
- The cross-correlogram correction and the Fig. 2d measure come from the same author's larger repo, `hs13/Analyze_IC_OpenScope_v240130` at 4ee1585. The paper does not link it, and the file cites it as a lower source.
- I found no code for the 2p analyses or for the Fig. 1 percentages.

**Claims**
- **Neuropixels, in this dandiset (18):** Fig. 1e–g; unit counts per session; IC-encoder and segment responder counts; Fig. 2d cross-correlograms; Fig. 3a, c, d decoding; Extended Data Figs 7a–c, 6e/f and 2a/b/f/g; and the other decoder types.
- **2p imaging, holography and mesoscope (21):** Figs 1i–k, 2b/c, 3e, 4a/b, 5c–e and 6d/e, plus Extended Data Figs 3, 4, 5, 9 and 10. These are the paper's own recordings but not in this dandiset. The paper does not say where they are; its only other deposit is unnamed "additional postprocessed data" in the same Code Ocean capsule.

**Details left open, with the readings named**
- **Decoder tuning:** the code runs MATLAB's automatic hyperparameter search, which the Methods don't mention. Readings: (a) fixed defaults, linear SVM with C = 1; (b) C chosen by inner cross-validation.
- **Exclusively center-responsive units:** the Methods test each position against gray-screen trials, but the mapping block has none. Readings: (a) the code's signed-rank test against the spontaneous rate, Holm-corrected; (b) a rank-sum test against 1 s windows cut from the spontaneous block.
- **"Substantially IC/IRE-responsive" and orientation match (Fig. 1f, g):**
  - Test: (a) Kruskal–Wallis with Tukey–Kramer against blank; (b) rank-sum against blank.
  - Block: (i) ICwcfg1 only, two orientations; (ii) ICwcfg1 and ICwcfg0, four orientations.
- **"Across ICwcfg0 and ICwcfg1" (159 IC-encoders):** units that are IC-encoders in either block, or the sum of the two blocks' counts.
- **Extended Data Fig. 6b counts (87 and 636):**
  - (a) RS units in ICwcfg1;
  - (b) all units in ICwcfg1;
  - (c) RS units in the union of both blocks.
  - Fig. 2d's 79 and 526 differ from these.
- **Fig. 2d cross-correlograms:**
  - Smoothing window: 25-bin boxcar or 25 ms Gaussian.
  - Flank SD: from the raw or the corrected correlogram.
  - Per-unit measure: fraction or count of connected higher-area units.
- **"Strongest" areas (Fig. 3d):** the largest mean scores or the smallest p-values.
- **Post hoc test after Kruskal–Wallis (Extended Data Fig. 7a, c):**
  - Readings: signed-rank V1 against each area, or Tukey–Kramer.
  - Panel 7c's dataset is ambiguous (Neuropixels or 2p); this is recorded as a deviation.
- **Eye tracking:**
  - The fixed-gaze threshold is 8 degrees in the Methods and 20 camera pixels in the code; the pixel threshold is run as a variant.
  - The images in the pupil-area Friedman test: the four IC/LC images or all 22.
  - Gaze confinement has no test in the paper, so two tests are named and no pixel-to-degree conversion is applied.
- **Fig. 4a/b:** the per-subset p-values are given in figure order, so which value belongs to which subset is read from the Results text.

**Missing from the paper**
- The Supplementary Information.
- An accessible copy of the linked code.
- Any location for the 2p data.
- The figure code for the Fig. 1 percentages.
- A pixel-to-degree conversion for eye position.

The Methods also list 14 Neuropixels mice (10 Sst, 4 PV) against 12 sessions from 12 mice elsewhere in the paper; the file notes this.

## End of run

45 turns, 9 minutes, result: success.
