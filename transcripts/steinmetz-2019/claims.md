# 000017 · claims · run 39659654318

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/000017 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -c paper/*; head -30 paper/*.txt; grep -n "supp\|Supplementary" paper/*.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001453; f=$(ls); sed -n 25,140p $f; grep -n "^checks\|^- id\|^  [a-z_]*:" $f | awk -F: '{print $2}' | sort | uniq -c
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
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -c 3000 paper/*.txt; grep -n "^#\|^==\|Methods\|Supplementary\|github\|Data availability\|Code availability" paper/*.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '{print NR": "length($0)}' paper/*.txt | sort -t: -k2 -n -r | head; grep -n "SUPPLEMENT\|supp1\|supp2\|^---" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I'm reading the paper now; the main text sits on one 118 KB line, so I'm wrapping it into a temp copy to read.

**Agent calls Bash**

```bash
cd  fold -s -w 400 paper/*.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 160
}
```

```
1	DOI: 10.1038/s41586-019-1787-x
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 2 supplement file(s) from the PMC Open Access cloud data (PMC6913580), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	Nature Nature 358 wtpa 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title UKPMC Funders Author Manuscripts PMC6913580 PMC6913580.1 6913580 6913580 EMS84617 31776518 10.1038/s41586-019-1787-x EMS84617 WTPA84617 WTMS84617 UKMS84617 1 Article Distributed coding of choice, action, and engagement across the mouse brain Steinmetz Nicholas A. 1 3 * Zatka-Haas Peter 2 
8	Carandini Matteo 1 4 Harris Kenneth D. 2 4 1 Institute of Ophthalmology, University College London, London, UK 2 Institute of Neurology, University College London, London, UK * Correspondence and requests for materials should be addressed to [removed: an e-mail address] 3 Present address: Department of Biological Structure, University of Washington, Seattle, WA. 4 These authors jointly supervised 
9	this work: Matteo Carandini, Kenneth D. Harris 27 11 2019 12 2019 576 7786 347872 266 273 12 10 2019 27 05 2020 27 05 2020 17 12 2019 16 06 2024 Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use: http://www.nature.com/authors/editorial_policies/license.html#terms Vision, 
10	choice, action, and behavioral engagement arise from neuronal activity that may be distributed across brain regions. Here we delineate the spatial distribution of neurons underlying these processes. We used Neuropixels probes 1 , 2 to record from ~30,000 neurons in 42 brain regions of mice performing a visual discrimination task 3 . Neurons in nearly all regions responded non-specifically when 
11	the m
[... 149 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 160,
 "limit": 170
}
```

```
160	Extended Data Fig. 9a ), we performed a nested multiple ANOVA test, in order to account for correlated variability between neurons within recording sessions. Each observation was a neuron’s average measured pre-trial firing rate in the window between 250 and 50ms prior to stimulus onset, log transformed (log 10 (x + 1 sp/s)) to make distributions approximately normal. Any trials with detectable 
161	wheel movement in this interval were excluded. The ANOVA had three factors: active/passive condition, recording session, and neuron identity (nested within recording session). The null hypothesis of no difference between baseline rates in active and passive conditions for neurons from a given brain region was rejected if the p-value for the active/passive condition factor was less than 0.0012, 
162	i.e. less than 0.05 after applying a Bonferroni correction for the 42 brain regions tested. To compute the trial-by-trial ‘engagement index’, we took the difference in pre-stimulus firing between the average of all task (‘active’) trials a and of all passive trials p, over the 200 ms period prior to stimulus onset: x n = f n a ¯ ( − 0.2 < t < 0 ) − f n p ¯ ( − 0.2 < t < 0 ) This quantity was 
163	computed for each neuron in one of the areas with significant differences between task and passive determined by nested ANOVA analysis (319 ± 32.5 mean ± s.e. neurons included per session, n=34 sessions), accumulated into a vector x and normalized to unit L2 magnitude for each session. To compute the engagement index for each trial i we computed the dot product x · f i , where f i is the vector 
164	of pre-stimulus firing rates for each trial i . We then computed the mean across Go and the mean across Miss trials, and took the difference of the two. The Go and Miss trials included in this analysis were matched for contrast so that difference in visual drive could not influence the difference between trial types. To do this, N trials were selected from each contralateral contrast c
[... 165 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 330
}
```

```
330	
331	[2] Steinmetz, N. A., Koch, C., Harris, K. D. & Carandini, M. Challenges and opportunities for large-scale electrophysiology with Neuropixels probes. Curr. Opin. Neurobiol. 50, 92–100 (2018). 10.1016/j.conb.2018.01.009
332	
333	[3] Burgess, C. P. et al. High-yield methods for accurate two-alternative visual psychophysics in head-fixed mice. Cell Rep. 20, 2513–2524 (2017). 10.1016/j.celrep.2017.08.047
334	
335	[4] Cisek, P. & Kalaska, J. F. Neural mechanisms for interacting with a world full of action choices. Annu. Rev. Neurosci. 33, 269–298 (2010). 10.1146/annurev.neuro.051508.135409
336	
337	[5] Romo, R. & de Lafuente, V. Conversion of sensory signals into perceptual decisions. Prog. Neurobiol. 103, 41–75 (2013). 10.1016/j.pneurobio.2012.03.007
338	
339	[6] Ding, L. & Gold, J. I. The basal ganglia’s contributions to perceptual decision making. Neuron 79, 640–649 (2013). 10.1016/j.neuron.2013.07.042
340	
341	[7] Hikosaka, O., Takikawa, Y. & Kawagoe, R. Role of the basal ganglia in the control of purposive saccadic eye movements. Physiol. Rev. 80, 953–978 (2000). 10.1152/physrev.2000.80.3.953
342	
343	[8] Felsen, G. & Mainen, Z. F. Midbrain contributions to sensorimotor decision making. J. Neurophysiol. 108, 135–147 (2012). 10.1152/jn.01181.2011
344	
345	[9] Gao, Z. et al. A cortico-cerebellar loop for motor planning. Nature 563, 113–116 (2018). 10.1038/s41586-018-0633-x
346	
347	[10] Chabrol, F. P., Blot, A. & Mrsic-Flogel, T. D. Cerebellar contribution to preparatory activity in motor neocortex. Neuron 103, 506–519.e4 (2019). 10.1016/j.neuron.2019.05.022
348	
349	[11] Shadlen, M. N. & Newsome, W. T. Neural basis of a perceptual decision in the parietal cortex (area LIP) of the rhesus monkey. J. Neurophysiol. 86, 1916–1936 (2001). 10.1152/jn.2001.86.4.1916
[... 399 more lines not kept]
```

**Agent**

The full text is all there: main text, Methods, Extended Data legends and both supplement files. Next I'll read the paper's code repository and look at the dataset's archive description.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/nsteinme/steinmetz-et-al-2019 code 2>&1 | tail -2; cd code && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | head -100
```

```
9a0bea8f33e4f43b4881c5e5756aad21cdbb9920 Mon Aug 9 16:38:34 2021 -0700
./utils/roc.m
./utils/loadSession.m
./utils/iff.m
./utils/brainRegionGroups.m
./utils/binAndNorm.m
./utils/avgAndNorm.m
./utils/areaOrdering.m
./reducedRankRegression/regFullPipeline.m
./reducedRankRegression/predictResidualsWith.m
./reducedRankRegression/makeCosReg.m
./reducedRankRegression/kmDummy.m
./reducedRankRegression/kernelRegPredict.m
./reducedRankRegression/kernelRegFitOne.m
./reducedRankRegression/kernelRegFit.m
./reducedRankRegression/kernelRegEval.m
./reducedRankRegression/kernelFitBasic.m
./reducedRankRegression/determineResidualsWithout.m
./reducedRankRegression/computeRegTraces.m
./reducedRankRegression/KernelModelToeplitz.m
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000017/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/000017/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m.get('name'));print(m.get('description'));print(m.get('relatedResource'));print(m.get('assetsSummary',{}).get('numberOfFiles'))"
```

Result: the fetched text is not kept.

**Agent**

The dataset holds 39 assets, which matches the paper's 39 sessions. The code repo was cloned at commit 9a0bea8. Now reading what it holds.

**Agent calls Bash**

```bash
cd $TMPDIR/code; find . -type f -not -path './.git/*' -not -path './behavior/inclusionData/trials/*' -not -path './images/*'; cat README.md 2>/dev/null | head -80; ls behavior behavior/inclusionData
```

```
./utils/roc.m
./utils/loadSession.m
./utils/iff.m
./utils/brainRegionGroups.m
./utils/binAndNorm.m
./utils/avgAndNorm.m
./utils/areaOrdering.m
./reducedRankRegression/regFullPipeline.m
./reducedRankRegression/predictResidualsWith.m
./reducedRankRegression/makeCosReg.m
./reducedRankRegression/kmDummy.m
./reducedRankRegression/kernelRegPredict.m
./reducedRankRegression/kernelRegFitOne.m
./reducedRankRegression/kernelRegFit.m
./reducedRankRegression/kernelRegEval.m
./reducedRankRegression/kernelFitBasic.m
./reducedRankRegression/determineResidualsWithout.m
./reducedRankRegression/computeRegTraces.m
./reducedRankRegression/KernelModelToeplitz.m
./reducedRankRegression/KernelModel.m
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; for f in behavior/findMoveTimes.m behavior/inclusionData/*.m reducedRankRegression/regFullPipeline.m reducedRankRegression/kernelRegFit.m reducedRankRegression/kernelRegFitOne.m reducedRankRegression/determineResidualsWithout.m reducedRankRegression/predictResidualsWith.m reducedRankRegression/kernelRegEval.m; do echo "=== $f"; cat $f; done
```

```
=== behavior/findMoveTimes.m

function [moveTimeUse, firstMoveType, firstMoveTime, hasNoMoveInWin] = ...
    findMoveTimes(...
    cweA, cwtA, moveData, win, winNoMove)
% determine the movement times to use, including choosing a suitable null 

if nargin<4
    win = [0.075 0.4];
    winNoMove = [-0.1 0.4];
elseif nargin<5
    winNoMove = [-0.1 0.4];
end


inclTrials = cweA.inclTrials;
nT = numel(inclTrials);

firstMoveTime = NaN(nT,1);
firstMoveType = NaN(nT,1);
[... 838 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; for f in reducedRankRegression/kernelFitBasic.m reducedRankRegression/KernelModel.m reducedRankRegression/KernelEventSeries.m reducedRankRegression/CanonCor2all.m ccCP/*.m utils/roc.m utils/brainRegionGroups.m; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (33.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/6f727277-45ea-4a61-8b1e-1e607e3b262a/tool-results/bhzengayh.txt

Preview (first 2KB):
=== reducedRankRegression/kernelFitBasic.m



function [km, binnedSpikes, inclU, inclTimes, trNum, cweA, cwtA, pvals, bslMeans, effectSizes] = ...
    kernelFitBasic(sp, cweA, cwtA, moveData)






%% load some data
% r = listInclRecs();
% n = 9; 
% mouseName = r(n).mouseName; thisDate = r(n).thisDate; 
[... 59 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/6f727277-45ea-4a61-8b1e-1e607e3b262a/tool-results/bhzengayh.txt",
 "offset": 60
}
```

```
60	
61	maxT = cwtA.feedbackTime(end)+5;
62	
63	
64	theseST = sp.st;
65	clu = sp.clu;
66	
67	cids = unique(clu);
68	if numel(cids)==1
69	    
70	    binBorders = 0:timeBinSize:maxT;
71	    tN = binBorders(1:end-1)+timeBinSize/2;
72	    
73	    binnedSpikes = histc(theseST, binBorders)./timeBinSize; % dividing here converts to Hz;
74	    binnedSpikes = binnedSpikes(1:end-1);
75	    binnedSpikes = binnedSpikes(:);
76	else
77	    
78	    theseClu = double(clu(theseST<maxT & theseST>0));
79	    theseST = theseST(theseST<maxT & theseST>0);    
[... 826 more lines not kept]
```

**Agent**

The repo also ships per-session lists of the paper's included trials and neurons (`behavior/inclusionData`). Those pin the paper's own selection, so I'm checking their shape.

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat jPECC/jPECC.m utils/loadSession.m utils/binAndNorm.m | head -250; python -c "
import numpy as np,glob
for s in ['Cori_2016-12-14','Lederberg_2017-12-05']:
  for k in ['hasLeft','hasRight','hasNone']:
    a=np.load(f'behavior/inclusionData/trials/{s}_{k}.npy'); print(s,k,a.shape,a.dtype,a.sum())
  a=np.load(f'behavior/inclusionData/neurons/{s}_inclNeurons.npy'); print(s,'incl',a.shape,a.dtype,a.sum())
tot=0;n=0
for f in glob.glob('behavior/inclusionData/neurons/*.npy'):
  a=np.load(f); tot+=a.sum(); n+=a.size
print('neurons incl total',tot,'of',n)
L=R=N=0
for f in glob.glob('behavior/inclusionData/trials/*_hasLeft.npy'):
  L+=np.load(f).sum(); R+=np.load(f.replace('Left','Right')).sum(); N+=np.load(f.replace('Left','None')).sum()
print('trials L R None',L,R,N, L+R+N)
"
```

```
Exit code 1


function [jPECC_val, jPECC_p] = jPECC(sp1, sp2, kfold, lambda, maxNpc)
% function [jPECC_val, jPECC_p] = jPECC(sp1, sp2, kfold, lambda)
%
% Inputs: 
% - sp1 and sp2 are size [trials, timebins, neurons] and contain spike counts
% aligned to an event, from neurons in area 1 and area 2. The third
% dimension (number of neurons) can be different between sp1 and sp2, but
% the other two should match. 
% - kfold sets cross-validation number of folds
% - lambda is a regularization parameter. Can leave it out and just use
% three input arguments for un-regularized version. 
% - maxNpc is the number of dimensions to keep from PCA analysis. Will keep
% fewer if there aren't enough neurons in the population. Default is 10. 
%
% Outputs: 
% - jPECC_val is size [timebins, timebins] containing the first canonical
% correlation value
[... 170 more lines not kept]
```

**Agent**

numpy isn't installed, so I'll read the `.npy` headers and values with the standard library.

**Agent calls Bash**

```bash
cd $TMPDIR/code; python3 - <<'EOF'
import glob,ast,struct
def load(f):
    b=open(f,'rb').read()
    hl=struct.unpack('<H',b[8:10])[0]; h=ast.literal_eval(b[10:10+hl].decode()); d=b[10+hl:]
    return h,d
for f in ['behavior/inclusionData/trials/Cori_2016-12-14_hasLeft.npy','behavior/inclusionData/neurons/Cori_2016-12-14_inclNeurons.npy']:
    h,d=load(f); print(f,h,len(d))
def bools(f):
    h,d=load(f); assert h['descr'] in ('|b1','|u1'),h; return list(d)
tot=n=0
for f in sorted(glob.glob('behavior/inclusionData/neurons/*.npy')):
    a=bools(f); tot+=sum(a); n+=len(a)
print('neurons',tot,n,len(glob.glob('behavior/inclusionData/neurons/*.npy')))
L=R=N=0;T=0
for f in sorted(glob.glob('behavior/inclusionData/trials/*_hasLeft.npy')):
    l=bools(f); r=bools(f.replace('Left','Right')); no=bools(f.replace('hasLeft','hasNone'))
    L+=sum(l);R+=sum(r);N+=sum(no);T+=len(l)
print('trials L R None total',L,R,N,T)
EOF
```

```
Exit code 1
behavior/inclusionData/trials/Cori_2016-12-14_hasLeft.npy {'descr': '<b1', 'fortran_order': True, 'shape': (214, 1)} 214
behavior/inclusionData/neurons/Cori_2016-12-14_inclNeurons.npy {'descr': '<b1', 'fortran_order': True, 'shape': (1085, 1)} 1085
Traceback (most recent call last):
  File "<stdin>", line 12, in <module>
  File "<stdin>", line 9, in bools
AssertionError: {'descr': '<b1', 'fortran_order': True, 'shape': (1085, 1)}
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; python3 - <<'EOF'
import glob,ast,struct
def bools(f):
    b=open(f,'rb').read()
    hl=struct.unpack('<H',b[8:10])[0]; return list(b[10+hl:])
tot=n=0
for f in sorted(glob.glob('behavior/inclusionData/neurons/*.npy')):
    a=bools(f); tot+=sum(a); n+=len(a)
print('neurons',tot,n,len(glob.glob('behavior/inclusionData/neurons/*.npy')))
L=R=N=0;T=0
for f in sorted(glob.glob('behavior/inclusionData/trials/*_hasLeft.npy')):
    l=bools(f); r=bools(f.replace('Left','Right')); no=bools(f.replace('hasLeft','hasNone'))
    L+=sum(l);R+=sum(r);N+=sum(no);T+=len(l)
print('trials L R None total',L,R,N,T)
EOF
git -C $TMPDIR/code log --format='%h %ad %s' | head
```

```
neurons 18248 48661 39
trials L R None total 1971 1729 2869 10050
9a0bea8 Mon Aug 9 16:38:34 2021 -0700 Update README.md
6ca6017 Thu Sep 24 09:19:32 2020 -0700 Update choiceProbShuf.m
3f720db Thu Sep 24 09:17:42 2020 -0700 Update mannWhitneyUshuf.m
acdfea8 Fri Aug 14 14:55:35 2020 -0700 fix setLambda
d40f312 Mon Mar 9 17:52:55 2020 -0700 add some utils and update loadSession
ea37f7d Mon Mar 2 10:15:34 2020 -0700 add ccCP functions
9211d43 Wed Jan 22 18:40:52 2020 -0800 add nPC as a parameter, update doc
e9ab655 Wed Jan 22 18:32:36 2020 -0800 add jPECC core function
c3af80e Mon Oct 14 17:17:01 2019 -0700 Merge branch 'master' of https://github.com/nsteinme/steinmetz-et-al-2019
e499d40 Mon Oct 14 17:16:57 2019 -0700 add guis, add inclusion data and functions
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; grep -il "passive\|engage\|focal\|anova\|fisher" -r --include=*.m . ; grep -n "passive\|winNoMove\|0.4\]" -r --include=*.m . | head -30; cat utils/avgAndNorm.m
```

```
./reducedRankRegression/regFullPipeline.m:236:    {[0.05 0.4], [-0.2 0]}, ...
./reducedRankRegression/regFullPipeline.m:237:    {[0.05 0.4], [-0.2 0]}, ...
./reducedRankRegression/regFullPipeline.m:238:    {[0.05 0.4], [-0.2 0]}, ...
./reducedRankRegression/regFullPipeline.m:239:    {[0.05 0.4], [-0.2 0]} ...
./reducedRankRegression/kernelFitBasic.m:21:winCountMove = [0.125 0.4];
./reducedRankRegression/kernelFitBasic.m:22:winNoMove = [-0.05 0.4];
./reducedRankRegression/kernelFitBasic.m:42:                findMoveTimes(cweA, cwtA, moveData, winCountMove, winNoMove);
./reducedRankRegression/kernelFitBasic.m:98:trTimes = stimOn(inclT)+[0:timeBinSize:winNoMove(end)]; 
./reducedRankRegression/kernelFitBasic.m:197:stimWin = [-0.05 0.4];
./behavior/findMoveTimes.m:4:    cweA, cwtA, moveData, win, winNoMove)
./behavior/findMoveTimes.m:8:    win = [0.075 0.4];
./behavior/findMoveTimes.m:9:    winNoMove = [-0.1 0.4];
./behavior/findMoveTimes.m:11:    winNoMove = [-0.1 0.4];
./behavior/findMoveTimes.m:38:        if firstMoveTime(t)<winNoMove(1) || firstMoveTime(t)>winNoMove(2)
function [mnNorm, mn, stderr] = avgAndNorm(allba, bsl, mgw, trAvg)

mgw3 = zeros(1,1,numel(mgw)); mgw3(1,1,:) = mgw; 
allbaSmooth = convn(allba, mgw3, 'same');

mn = squeeze(mean(allbaSmooth(:,trAvg,:),2));
[... 6 more lines not kept]
```

**Agent**

The code has no engagement, passive, focality or Fisher-test analyses, so the Methods alone fix those. Next I'm checking what the quote checker and claims schema expect.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; ls docs; grep -rn "schema_version\|p_relation\|corrected" docs/*.md | head -20
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

[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | head -200
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1)); print([k for k in d['properties']])"
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
[... 83 more lines not kept]
```

**Agent**

Now a recent claims file, to see how the opening comment records provenance and the code read.

**Agent calls Bash**

```bash
ls claims/001444/; head -60 claims/001444/*.yaml
```

```
10.1038-s41531-025-01070-4.yaml
# Claims for Doherty, Chen, Smith, Wichmann, Chu & Lytton (2025), npj Parkinson's Disease 11, 230,
# "Enhanced beta power emerges from simulated parkinsonian primary motor cortex", on dandiset 001444.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
# pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record as served by Europe PMC (PMC12325672), main text, figure legends
# and Methods. The supplement (Supplementary Tables 1 to 3, Supplementary Figs. 1 to 5) was not in
# the text supplied and was not read. The main text reports every result below from one set of
# simulations; the supplement holds the analyses of the three other sets (Supplementary Table 2),
# the PT5B current-frequency curves (Supplementary Fig. 1) and the conductance changes
# (Supplementary Table 3). The bioRxiv preprint (doi:10.1101/2024.05.23.595566) was also supplied;
# it is an earlier version with another title and was not used for claims.
#
# Code read: github.com/suny-downstate-medical-center/pd_m1_6ohda at commit 0a1f0e8 (2025-08-20, the
# head of main; the paper cites Zenodo 10.5281/zenodo.12399983). It holds the NetPyNE simulation
# (sim/cfg.py, sim/netParams.py, cells, mechanisms) and four notebooks that stream one file each
# from dandiset 001444 and plot the LFP, a raster and five PT5B voltage traces. It holds no code for
# rates, statistics, CV, duty cycle, spectrograms, coincidences or unitary events. The README gives
# the four parameter settings (control or parkinsonian PT5B BK and NaT conductances; rest or
[... 41 more lines not kept]
```

**Agent**

I have enough to plan the claims. First I'll check the supplement docx for the "±" that the text extraction dropped in Supplementary Fig. 2.

**Agent calls Bash**

```bash
cd paper; python3 - <<'EOF'
import zipfile,re
for f in ['10.1038-s41586-019-1787-x.supp1.docx','10.1038-s41586-019-1787-x.supp2.docx']:
    x=zipfile.ZipFile(f).read('word/document.xml').decode()
    t=re.sub(r'<[^>]+>','',x)
    i=t.find("d’=0.35")
    if i<0: i=t.find("d'=0.35")
    print(f,i,repr(t[i-80:i+80]) if i>=0 else '')
    j=x.find('0.35'); print(repr(x[j-300:j+400]) if j>=0 else '')
EOF
```

```
10.1038-s41586-019-1787-x.supp1.docx -1 

10.1038-s41586-019-1787-x.supp2.docx 15045 'ance in each test. Significant cells tend to have higher baseline firing rates (d’=0.350.04), while differences in spike amplitude are much smaller (d’=0.100.02'
'l:space="preserve"> scatter plots with one point per cell, showing mean pre-stimulus baseline firing rate (x-axis) and mean spike waveform amplitude (y-axis), color coded according to whether that cell showed significance in each test. Significant cells tend to have higher baseline firing rates (d’=0.35</w:t></w:r><w:r w:rsidRPr="00124522"><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:sym w:font="Symbol" w:char="F0B1"/></w:r><w:r w:rsidRPr="00124522"><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:t>0.04), while differences in spike amplitude are much smaller (d’='
```

**Agent**

The supplement docx has the ± sign as a Symbol-font glyph, so the values are 0.35 ± 0.04 and 0.10 ± 0.02. Next I'll sum the columns of Extended Data Table 1 to see which totals they match.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import re
t=open('paper/10.1038-s41586-019-1787-x.txt').read()
i=t.find('Extended Data Table 1 Brain regions recorded'); j=t.find('Supplementary Material',i)
s=t[i:j]
rows=re.findall(r'([A-Za-z]+) ([A-Z][A-Za-z ,\-]+?) (\d+) (\d+) (\d+) (\d+) ([\d.]+)',s)
print(len(rows))
print(sum(int(r[4]) for r in rows), sum(int(r[5]) for r in rows), sum(int(r[2]) for r in rows))
for r in rows: print(r[0],r[2:])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/000017/10.1038-s41586-019-1787-x.yaml",
 "content": "# Claims for Steinmetz, Zatka-Haas, Carandini & Harris (2019), Nature 576, 266-273, \"Distributed\n# coding of choice, action and engagement across the mouse brain\", on dandiset 000017.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, protocol\n# pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the accepted author manuscript as served by Europe PMC (PMC6913580, UKPMC Funders\n# Author Manuscripts), with the main text, Methods, Extended Data figure legends, Extended Data\n# Table 1 and the figure legends. Both supplement files from the PMC Open Access data were read:\n# supplement 1 (Supplementary Information guide, Supplementary Tables 1 and 2, legends of\n# Supplementary Figs. 1 to 4) and supplement 2 (Supplementary Discussion and the same tables and\n# legends). The \"±\" of the Supplementary Fig. 2 legend is lost in the text (\"d'=0.350.04\"); the\n# Word file holds a Symbol-font \"±\" there (0.35 ± 0.04 and 0.10 ± 0.02). Supplementary Table 3 is\n# only an image and was not read. No PDF was opened. In Extended Data Table 1 the text prints VISl\n# and VISrl as \"VISI\" and \"VISrI\".\n#\n# Code read: github.com/nsteinme/steinmetz-et-al-2019 at commit 9a0bea8 (2021-08-09, head of\n# master). It holds the reduced-rank kernel regression (reducedRankRegression/: kernelFitBasic.m,\n# regFullPipeline.m, determineResidualsWithout.m, predictResidualsWith.m, CanonCor2all.m,\n# KernelModel.m, KernelEventSeries.m), the trial movement classification (behavior/findMoveTimes.m),\n# jPECC (jPECC/jPECC.m), the ccCP shuffle (ccCP/choiceProbShuf.m, mannWhitneyUshuf.m), data browsers\n# and plotting, and per-session arrays of included trials (behavior/inclusionData/trials,\n# hasLeft/hasRight/hasNone, 39 sessions, 1,971 + 1,729 + 2,869 of 10,050 trials) and included units\n# (behavior/inclusionData/neurons, 18,248 of 48,661 units). The paper does not say which selection\n# these arrays hold; an author may compare its selections with them, through a link claim. The code\n# holds nothing for the passive-context, engagement index, nested ANOVA, GLM, Focality index,\n# Fisher tests or population decoding. regFullPipeline.m opens with a note by its author that the\n# evaluation window should be fixed and the script re-run; it is the only pipeline given. The wheel\n# movement detector is cortex-lab/wheelAnalysis +wheel/findWheelMoves3.m (Methods link), not read.\n# The data were also deposited on figshare, doi:10.6084/m9.figshare.9598406 (Data availability).\n#\n# The data the paper used. 10 mice (6 female, 4 male; Supplementary Table 1 names Cori, Forssmann,\n# Hench, Lederberg, Moniz, Muller, Radnitz, Richards, Tatum, Theiler), 11 to 46 weeks old, 39\n# sessions (Supplementary Table 2 gives date, age and areas of each), 92 Neuropixels insertions,\n# all in the left hemisphere, 2 or 3 probes at a time. 29,134 neurons, 22,458 of them in 42 brain\n# regions (Extended Data Table 1). Task (Methods, Two-alternative unforced choice task) with left and\n# right Gabor stimuli of zero or one of three contrasts (low, medium, high); wheel turns left or\n# right, or no turn (NoGo); a go cue tone 0.5 to 1.2 s after stimulus onset; water reward or white\n# noise feedback. After each session a passive replay of the task stimuli (visual stimuli, beeps,\n# noise bursts, valve clicks) and sparse noise receptive field mapping. Measured variables. Spike\n# times and clusters with curation labels, channel brain locations, wheel position (rotary encoder),\n# lick piezo, eye video (pupil area by DeepLabCut), face/body video (motion energy), trial events\n# (stimulus onset, contrasts, go cue, response, feedback), passive stimulus events. Histology of the\n# DiI tracks.\n#\n# Definitions used by several criteria, each from the paper or its code as cited.\n# - Contralateral. All recordings are in the left hemisphere (Methods, Neuronal recordings), so the\n#   contralateral stimulus is the right one and a contralateral choice is a Right choice (the turn\n#   that brings the right stimulus to the centre).\n# - Trials T. Left and Right choice trials have the onset of a turn reaching 90 d.v.a. between 125\n#   and 400 ms after stimulus onset; NoGo trials have no movement from -50 to 400 ms; trials with\n#   other movements are dropped (Methods, Training protocol). Movement onsets by the findWheelMoves3\n#   algorithm (Methods). Disengaged trials are dropped (a Miss preceded by two or more Misses, and\n#   the run of NoGo trials at the end of the session). Sessions need at least 12 trials of each of\n#   Left, Right and NoGo. The code (kernelFitBasic.m, findMoveTimes.m) takes the first movement after\n#   stimulus onset minus 0.1 s and before feedback, and counts a trial as NoGo only when such a\n#   movement exists outside -0.05 to 0.4 s; a trial with no movement at all before feedback is then\n#   dropped. This differs from the Methods; the Methods rule is used, the code rule is a variant.\n#   For NoGo trials a movement time is drawn at random from the Left and Right trials' movement\n#   times when one is needed (Methods, Population decoding; findMoveTimes.m).\n# - Neurons N. Units curated as single units (not multi-unit; code sp.cgs > 1), trial firing rate\n#   (stimulus onset to 0.4 s) at least 0.1 Hz, at least 13 such neurons in the same region in the\n#   same session, regions recorded in at least two subjects (Methods, Data analysis). The set for\n#   Figs. 3 to 5 also needs p < 0.05 on any of tests 1 to 4 of the six responsiveness tests (Methods,\n#   which define the tests and windows). \"Active during the task\" is any of the six tests below\n#   0.05/6. The code keeps a neuron when a test returns NaN (comment \"this is a BUG\", kernelFitBasic.m,\n#   about 1000 neurons); that is a variant.\n# - Kernel test K (Methods, Kernel regression and Determining individual neuron selectivity; code as\n#   named). Spikes in 5 ms bins, smoothed with a causal half-Gaussian of s.d. 25 ms; each neuron's\n#   mean rate from -0.2 to 0 s before stimulus onset is subtracted (code). Six Vision kernels (left\n#   and right, low, medium, high contrast), -0.05 to 0.4 s from stimulus onset (90 bins); an Action\n#   kernel and a Choice kernel (event value +1 Left, -1 Right, code) at every Left or Right\n#   movement onset, -0.25 to 0.025 s (55 bins); Toeplitz predictors and an intercept. Samples from\n#   0.05 s before stimulus onset to the earlier of 0.4 s after it and 0.025 s after movement onset\n#   (code). Reduced-rank regression basis from all neurons of all sessions together\n#   (CanonCor2all.m), first 200 columns kept. Full model per neuron: elastic net, alpha 0.5, lambda\n#   0.5 fixed (Methods; code calls glmnet with its default options, useCVG false), 5-fold\n#   cross-validation over trials, 1 to 50 components, the best cross-validated variance explained\n#   (VE) kept, VE taken over samples from stimulus onset to the earlier of movement onset and 0.4 s\n#   (code). Neurons with full-model VE < 2% are dropped. Nested test for kernel K: a new basis from\n#   the model without K over the kept neurons, each neuron fit with 75 components on all its data,\n#   residuals taken; a new basis for K alone on the residuals; 10-fold cross-validation over trials,\n#   1 to 18 components, best VE, over samples 0.05 to 0.4 s after stimulus onset (ending at movement\n#   onset) and -0.2 to 0 s from movement onset (code evalWins). The neuron requires K when VE > 2%.\n#   Contralateral Vision is the three right-stimulus kernels.\n# - Matched contrast M (Methods, Training protocol). Trials with contralateral contrast > 0, split\n#   by contralateral contrast; at each level the smallest of the counts of Go (Left or Right), NoGo\n#   and passive trials is drawn at random from each; sessions with fewer than 10 such trials are\n#   dropped (34 of 39 kept). The Methods do not say whether \"fewer than 10\" counts the trials of one\n#   group or all three.\n# - Responsive in a condition R (Methods, Data analysis, paragraph on Fig. 2d-h and Fig. 5b). The\n#   mean rate 0 to 0.25 s after stimulus onset over the condition's trials, z-scored against the\n#   trial-by-trial baseline (-0.1 to 0 s); significant when z > 4 or z < -4, \"equivalent to a\n#   two-sided t-test at p<10-4\". Open is the z denominator. Readings Z1, the standard error of the\n#   baseline mean (s.d. over trials divided by the square root of the trial count), which matches the\n#   t-test the Methods name; Z2, the s.d. of the trial baselines.\n# - Region groups (code utils/brainRegionGroups.m and Methods). Frontal for choice timing and jPECC\n#   MOs, MOp, PL; midbrain MRN, SCm, SNr, ZI; striatum CP; VIS VISp, VISpm, VISl, VISrl, VISa, VISam.\n#   Neocortex is the Allen isocortex areas recorded (ACA, ILA, MOp, MOs, ORB, PL, RSP, SSp and the VIS\n#   areas). Visual thalamus is LGd, LP, LD (Extended Data Fig. 6b legend).\n# - Random draws (folds, matched-contrast subsets, shuffles) take a fixed seed, a standard choice.\n# Where the readings of a claim give different outcomes, the claim is blocked as\n# methods_underspecified with every result shown.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000017\"\npaper: doi:10.1038/s41586-019-1787-x\nclaims:\n- id: fig1c-easy-performance\n  statement: On high-contrast single-stimulus trials mice made 1.7 ± 2.5% incorrect choices and\n    10.1 ± 8.3% Misses (mean ± s.d. over 39 sessions of 10 mice).\n  source: Results, Brain-wide recording in visual behavior, paragraph 1; Fig. 1c,d\n  quote: Their choices were most accurate for high-contrast single stimuli (i.e. when the other\n    stimulus was absent; 1.7 ± 2.5% incorrect choices, i.e. turns in the wrong direction; 10.1 ±\n    8.3% Misses, i.e. failures to turn; mean ± s.d., n = 39 sessions, 10 mice)\n  expected:\n  - quantity: incorrect choices, high-contrast single stimulus, mean over sessions\n    value: 1.7\n    tolerance: 2.5\n    unit: percent of trials\n  - quantity: Misses, high-contrast single stimulus, mean over sessions\n    value: 10.1\n    tolerance: 8.3\n    unit: percent of trials\n  criterion: Trials with the high contrast on one side and zero on the other. Per session, the\n    percentage of such trials with a turn to the wrong side, and with no turn (the task's\n    recorded response, NoGo); the mean over the 39 sessions. Tolerances are the paper's s.d. over\n    sessions. The paper does not say which trials enter. Readings (a) all trials of the session;\n    (b) trials after dropping disengaged trials as in definition T. Reproduced when both values\n    are within tolerance under one reading; the s.d. over sessions is reported as well.\n- id: fig1c-low-contrast-performance\n  statement: With low-contrast single stimuli mice made 5.1 ± 6.4% incorrect choices and 29.8 ±\n    19.8% Misses.\n  source: Results, Brain-wide recording in visual behavior, paragraph 1\n  quote: with low-contrast single stimuli (5.1 ± 6.4% incorrect choices; 29.8 ± 19.8% Misses)\n  expected:\n  - quantity: incorrect choices, low-contrast single stimulus, mean over sessions\n    value: 5.1\n    tolerance: 6.4\n    unit: percent of trials\n  - quantity: Misses, low-contrast single stimulus, mean over sessions\n    value: 29.8\n    tolerance: 19.8\n    unit: percent of trials\n  criterion: As fig1c-easy-performance, for trials with the low contrast on one side and zero on\n    the other, under the same readings.\n- id: fig1c-competing-performance\n  statement: With competing stimuli of similar but unequal contrast (high against medium, medium\n    against low) mice made 20.0 ± 7.9% incorrect choices and 13.9 ± 11.7% Misses.\n  source: Results, Brain-wide recording in visual behavior, paragraph 1\n  quote: or with competing stimuli of similar but unequal contrast (20.0 ± 7.9% incorrect choices;\n    13.9 ± 11.7% Misses, on trials with high vs. medium or medium vs. low contrast)\n  expected:\n  - quantity: incorrect choices, high vs medium and medium vs low trials, mean over sessions\n    value: 20.0\n    tolerance: 7.9\n    unit: percent of trials\n  - quantity: Misses, high vs medium and medium vs low trials, mean over sessions\n    value: 13.9\n    tolerance: 11.7\n    unit: percent of trials\n  criterion: As fig1c-easy-performance, for trials with high against medium or medium against low\n    contrast (either side), an incorrect choice being a turn towards the lower contrast, under the\n    same readings.\n- id: fig1d-reaction-time-difficulty\n  statement: Reaction times were longer in the harder conditions (low-contrast single stimuli and\n    competing stimuli of similar contrast) than for high-contrast single stimuli.\n  source: Results, Brain-wide recording in visual behavior, paragraph 1; Fig. 1d\n  quote: As expected, in these more challenging cases reaction times were longer ... multi-way ANOVA\n  statistics:\n  - test: multi-way ANOVA\n    p: 0.0001\n    p_relation: \"<\"\n    n: 39 sessions, 10 mice\n  criterion: Reaction time is the movement onset (definition T, findWheelMoves3) minus stimulus\n    onset on Left and Right choice trials. The paper names neither the factors of its multi-way\n    ANOVA nor the trials. Readings of the factors (F1) condition class (high-contrast single,\n    low-contrast single, competing similar contrasts) and session; (F2) condition class and\n    subject; readings of the trials (a) all Left and Right choice trials; (b) those of definition\n    T (onset 125 to 400 ms). Reproduced when, under one reading, the condition factor has p < 1e-4\n    and the mean reaction time of the high-contrast single class is the shortest of the three.\n- id: ed1q-wheel-choice-decoding\n  statement: Choice decoded from instantaneous wheel velocity is at chance (47.7%) 50 ms before\n    detected movement onset and near perfect (94.6%) 50 ms after it.\n  source: Methods, Training protocol, paragraph 3; Extended Data Fig. 1q\n  quote: The decoder performed essentially at chance 50 ms prior to movement onset (47.7%) compared\n    to near perfect performance 50 ms after movement onset (94.6%)\n  expected:\n  - quantity: decoding accuracy 50 ms before movement onset\n    value: 47.7\n    tolerance: 4.77\n    unit: percent\n  - quantity: decoding accuracy 50 ms after movement onset\n    value: 94.6\n    tolerance: 9.46\n    unit: percent\n  criterion: Velocity is the wheel position at t minus that at t - 10 ms (Methods), at times\n    relative to the detected onset of Left and Right choice movements. The paper does not name the\n    decoder. Readings (a) the sign of the velocity, a zero velocity counting as a guess (50%);\n    (b) a logistic regression on velocity with 10-fold cross-validation over trials, per\n    session. Accuracy is the mean over the 39 sessions (Extended Data Fig. 1q, s.d. across\n    sessions). Reproduced when both values are within tolerance under one reading.\n- id: early-response-fraction\n  statement: On trials that ended in a Left or Right choice, mice turned the wheel within 400 ms of\n    stimulus onset on 64.9 ± 14.0% (s.d.) of trials, nearly always (96.6 ± 3.4%) in the direction\n    of their final choice.\n  source: Methods, Training protocol, paragraph 1\n  quote: turning the wheel within 400 ms of stimulus appearance (64.9 ± 14.0% s.d., n=39 sessions),\n    nearly always in the same direction as their final choice (96.6 ± 3.4%)\n  expected:\n  - quantity: trials with a turn within 400 ms, of trials ending in a Left or Right choice\n    value: 64.9\n    tolerance: 14.0\n    unit: percent, mean over sessions\n  - quantity: of those, turns in the direction of the final choice\n    value: 96.6\n    tolerance: 3.4\n    unit: percent, mean over sessions\n  criterion: Per session, of trials whose recorded response is Left or Right, the percentage with\n    the onset of a turn reaching 90 d.v.a. within 0.4 s of stimulus onset, and of those the\n    percentage whose turn direction equals the recorded response; mean over the 39 sessions.\n    Tolerances are the paper's s.d. over sessions. Reproduced when both are within tolerance.\n- id: passive-no-movement\n  statement: In the passive replay mice hardly ever turned the wheel; 94.1% ± 0.6% of passive\n    trials with high-contrast stimuli had no movement.\n  source: Results, Propagation of activity during the task, paragraph 3\n  quote: In these passive trials the mice hardly ever turned the wheel (94.1% ± 0.6% of trials with\n    high contrast stimuli had no movement)\n  expected:\n    quantity: passive high-contrast trials with no wheel movement\n    value: 94.1\n    tolerance: 0.6\n    unit: percent\n  criterion: Passive replay presentations of a visual stimulus at the high contrast (on either\n    side). The paper does not give the window or the spread. Readings of the window (a) -0.05 to\n    0.4 s from stimulus onset, the NoGo window of definition T; (b) 0 to 0.4 s; of the value (i)\n    the mean over sessions; (ii) the pooled fraction. No movement is no detected wheel movement\n    onset and no movement in progress in the window. The tolerance is the paper's stated spread.\n    Reproduced when one reading is within tolerance.\n- id: recording-counts\n  statement: Across 39 sessions in 10 mice with 92 probe insertions, 29,134 neurons were recorded\n    (747 ± 38 per session, mean ± s.e.), 22,458 of them localized to one of 42 brain regions; the\n    behaviour comprised 9,538 trials.\n  source: Results, Brain-wide recording in visual behavior, paragraphs 2 and 3; Fig. 1c legend\n  quote: Across all sessions we recorded from 29,134 neurons (n=747 ± 38 neurons per session, mean\n    ± s.e.), of which 22,458 were localizable to one of 42 brain regions\n  expected:\n  - quantity: neurons recorded\n    value: 29134\n    tolerance: 2913\n  - quantity: neurons per session, mean\n    value: 747\n    tolerance: 38\n  - quantity: neurons localized to one of the 42 regions\n    value: 22458\n    tolerance: 2246\n  - quantity: sessions\n    value: 39\n    tolerance: 0\n  - quantity: mice\n    value: 10\n    tolerance: 0\n  - quantity: probe insertions\n    value: 92\n    tolerance: 0\n  - quantity: trials in Fig. 1c\n    value: 9538\n    tolerance: 954\n  criterion: Counts of sessions, subjects and probes are exact. Neurons are units curated as single\n    units. Readings of \"neurons\" (a) all such units; (b) those also with a trial firing rate of at\n    least 0.1 Hz. Readings of \"localizable\" (i) neurons whose channel lies in one of the 42 regions\n    of Extended Data Table 1; (ii) neurons of definition N. Readings of the trials (a) all trials;\n    (b) trials kept after definition T. Reproduced when every count is within tolerance under one\n    reading of each; partially reproduced when the exact counts hold and one other count does not.\n- id: edtable1-region-counts\n  statement: Extended Data Table 1 gives, for each of the 42 regions, the number of recordings,\n    mice, task-responsive neurons and neurons (for example MOs 19 recordings, 9 mice, 993 of\n    1,534 neurons responsive; MRN 11, 7, 722 of 857).\n  source: Extended Data Table 1\n  inferred: Numbers only in Extended Data Table 1; no sentence states them. The table's neuron\n    column sums to 22,458 and its responsive column to 13,467, against 13,466 in the Results.\n  criterion: For each region of the table, the number of sessions with neurons of the region\n    (definition N), the number of mice, the number of neurons and the number active during the\n    task (definition N). Reproduced when the recordings and mice match exactly and the neuron\n    counts are within 10% in at least 38 of the 42 regions; partially reproduced in 30 to 37\n    regions. The regions that differ are listed.\n- id: supptable2-sessions\n  statement: The 39 sessions are those of Supplementary Table 2, each with its subject, date, age\n    and recorded areas (for example Cori 2016-12-14, 11 weeks, ACA, CA3, DG, LS, MOs, SUB, VISp),\n    from the 10 subjects of Supplementary Table 1 with their sex and genotype.\n  source: Supplementary Tables 1 and 2\n  inferred: Numbers only in Supplementary Tables 1 and 2; no sentence states them.\n  criterion: Each session of the table matched by subject and date. Reproduced when all 39 sessions\n    are present, their subjects' sex and genotype match Supplementary Table 1, and the set of\n    areas with neurons in each session matches the table in at least 35 sessions; partially\n    reproduced when all sessions are present but the areas match in fewer.\n- id: task-modulated-fraction\n  statement: 60.0% of neurons (13,466) were significantly modulated during the task; of these 74.3%\n    consistently increased and 20.2% consistently decreased their activity.\n  source: Results, Propagation of activity during the task, paragraph 1; Supplementary Figs. 1 and 2\n  quote: A sizeable fraction of all neurons (60.0%, 13,466 neurons) had significant modulation of\n    firing rate during the task. Most of these neurons (74.3%) consistently increased their\n    activity during the task, but a sizeable minority (20.2%) consistently decreased\n  expected:\n  - quantity: neurons active during the task\n    value: 13466\n    tolerance: 1347\n  - quantity: fraction active\n    value: 60.0\n    tolerance: 6.0\n    unit: percent of localized neurons\n  - quantity: active neurons consistently increasing\n    value: 74.3\n    tolerance: 7.4\n    unit: percent of active neurons\n  - quantity: active neurons consistently decreasing\n    value: 20.2\n    tolerance: 2.0\n    unit: percent of active neurons\n  criterion: Active during the task is any of the six tests of the Methods below 0.05/6, on trials\n    T of the neurons localized to the 42 regions with a rate of at least 0.1 Hz (13,466 of 22,458\n    is 60.0%, and Extended Data Table 1 sums to these). The direction of a significant test against\n    baseline is the sign of the count of positive minus negative differences (code effectSizes).\n    The paper does not define \"consistently\". Readings (a) every significant test against\n    baseline (tests 1, 2, 3, 5, 6) has the same sign, test 4 being left out; (b) as (a) with test 6\n    taken as a rank-sum, as the code does. Reproduced when all four values are within tolerance\n    under one reading.\n- id: suppfig2-rate-amplitude\n  statement: Statistically responsive neurons have higher baseline firing rates than other neurons\n    (d' = 0.35 ± 0.04), while their spike amplitudes differ much less (d' = 0.10 ± 0.02).\n  source: Supplementary Fig. 2 legend\n  quote: Significant cells tend to have higher baseline firing rates ... while differences in spike\n    amplitude are much smaller\n  expected:\n  - quantity: d' of baseline firing rate, significant against other cells\n    value: 0.35\n    tolerance: 0.04\n  - quantity: d' of spike waveform amplitude, significant against other cells\n    value: 0.10\n    tolerance: 0.02\n  criterion: Values read from the supplement's Word file (the \"±\" is lost in the text). Baseline is\n    the mean rate -0.2 to 0 s before stimulus onset; amplitude the mean spike waveform amplitude.\n    The legend shows the cells per test (b to g) and gives one d' each; the paper does not say over\n    what the ± is taken. Readings (a) significant on any of the six tests against the rest, the ±\n    being a bootstrap s.e. over neurons; (b) the mean ± s.e. of the six per-test d' values. d' is\n    the difference of means over the root mean of the two variances. Reproduced when both are\n    within tolerance under one reading.\n- id: fig2de-activity-order\n  statement: When the mouse chose a contralateral stimulus, activity arose first in visual cortex\n    and superficial superior colliculus and then spread to most regions; when it chose an\n    ipsilateral stimulus, VIS and SCs were among the last areas to respond.\n  source: Results, Propagation of activity during the task, paragraph 2; Fig. 2d,e\n  quote: When a mouse successfully selected a visual stimulus contralateral to the recorded\n    hemisphere, activity emerged first in classical visual regions such as visual cortex (VIS) and\n    superficial superior colliculus (SCs), and soon spread to most of the remaining recorded\n    regions ... VIS and SCs were now amongst the last areas to respond\n  criterion: Correct contralateral (Right choice on a right stimulus alone) and correct ipsilateral\n    trials (T, matched in contrast for d as in definition M). Per region the mean over responsive\n    neurons of the normalized rate of the Methods (5 ms bins, causal half-Gaussian 0.02 s, trial\n    mean, causal half-Gaussian 0.03 s, minus the baseline -0.02 to 0 s, divided by baseline + 0.5\n    sp/s). Responsive is open; readings (a) active during the task (definition N); (b) the Figs. 3\n    to 5 set. The paper defines no latency. Readings (L1) the first time after stimulus onset the\n    region's trace reaches half its maximum in 0 to 0.4 s; (L2) the time of that maximum.\n    Reproduced when, under one reading, on contralateral trials VISp (and the VIS group mean) and\n    SCs fall in the earliest quarter of regions, and on ipsilateral trials both fall in the latest\n    third.\n- id: fig2fg-miss-restricted\n  statement: On Miss trials with a contralateral stimulus, activity appeared in a visual pathway of\n    visual areas, basal ganglia and several midbrain structures but did not spread to the whole\n    brain; on Miss trials with an ipsilateral stimulus there was essentially no activity.\n  source: Results, Propagation of activity during the task, paragraph 2; Fig. 2f,g\n  quote: activity was found in a “visual pathway” consisting of classical visual areas, basal\n    ganglia, and several midbrain structures ... but failed to propagate globally. When the mouse\n    missed an ipsilateral stimulus, essentially no activity was seen in the recorded hemisphere\n  criterion: Fraction of neurons per region significantly activated (definition R, z > 4; readings\n    Z1, Z2) on contrast-matched (M) correct contralateral Go trials and contralateral Miss trials,\n    and on ipsilateral Miss trials. The visual pathway set is the VIS areas, LGd, LP, LD, SCs, CP,\n    GPe, SNr, SCm, MRN, APN and ZI (the areas Fig. 3d and the Results name for vision); the rest are\n    other regions. Reproduced when, under one reading, (i) on contralateral Miss trials the mean\n    fraction over visual pathway regions exceeds that over other regions, (ii) the mean fraction\n    over other regions is at least twice as large on contralateral Go as on contralateral Miss\n    trials, and (iii) the pooled fraction on ipsilateral Miss trials is below half that on\n    contralateral Miss trials. The thresholds are this file's reading of \"failed to propagate\n    globally\" and \"essentially no activity\".\n  depends_on:\n  - fig5b-miss-more-than-passive\n- id: fig3d-vision-localized\n  statement: Neurons encoding the contralateral visual stimulus were found mainly in classical\n    visual areas, common in visual cortex, thalamus and SCs, and occasionally in frontal cortex\n    (MOs, ACA, PL), basal ganglia (CP, GPe, SNr) and midbrain nuclei (SCm, MRN, APN, ZI).\n  source: Results, Globally distributed action coding, paragraph 3; Fig. 3d,f\n  quote: Neurons encoding vision (i.e. requiring Vision kernels) were found in a pathway comprising\n    primarily classical visual areas ... They were common in visual cortex (VIS) and thalamus, and\n    superficial superior colliculus (SCs), but also were found occasionally in other structures\n    such as frontal cortex (MOs, ACA, PL), basal ganglia (CP, GPe, SNr), and several midbrain\n    nuclei (SCm, MRN, APN, ZI\n  criterion: Kernel test K for the Contralateral Vision kernels, on neurons N (Figs. 3 to 5 set) and\n    trials T; fraction per region of neurons passing analysis criteria, regions with fewer than 5\n    such neurons left out (Fig. 3d legend). Reproduced when more than half of all neurons\n    requiring Contralateral Vision lie in the VIS areas, visual thalamus (LGd, LP, LD) and SCs; the\n    regions with the five highest fractions are among these; and each of MOs, ACA, PL, CP, GPe,\n    SNr, SCm, MRN, APN and ZI that is analysed has at least one such neuron. Partially reproduced\n    when the first two hold only.\n- id: fig3e-action-global\n  statement: Neurons encoding action (requiring the Action kernel) were found in all recorded\n    regions, and most did not require a Choice kernel.\n  source: Results, Globally distributed action coding, paragraph 3; Fig. 3e,g\n  quote: In contrast, neurons encoding action (requiring an Action kernel) were spread throughout\n    all recorded regions ... The great majority of neurons encoding action did not require an\n    additional Choice kernel\n  criterion: Kernel test K for the Action and the Choice kernels, as in fig3d-vision-localized.\n    Reproduced when every analysed region (at least 5 neurons) has Action-requiring neurons and\n    more than half of Action-requiring neurons do not require the Choice kernel; partially\n    reproduced when at least 90% of regions have them.\n- id: ed4f-focality\n  statement: The Focality index was 0.079 for choice, 0.069 for contralateral vision and 0.040 for\n    action, with choice and vision each significantly more focal than action.\n  source: Extended Data Fig. 4f legend; Methods, Focality Index\n  quote: This focality index was 0.079 for choice, 0.069 for visual kernels and 0.040 for action\n    kernels; the differences between Choice and Move, as well as Contralateral Vision and Action,\n    were statistically significant (p<0.05; bias-corrected bootstrap)\n  statistics:\n  - about: Choice against Action, and Contralateral Vision against Action\n    test: bias-corrected bootstrap\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: Focality index, Choice\n    value: 0.079\n    tolerance: 0.0079\n  - quantity: Focality index, Contralateral Vision\n    value: 0.069\n    tolerance: 0.0069\n  - quantity: Focality index, Action\n    value: 0.040\n    tolerance: 0.0040\n  criterion: F = sum of p_a squared over the square of the sum of p_a, p_a the fraction of neurons\n    in region a requiring the kernel (kernel test K; Methods). Intervals are 95% bootstrap\n    intervals, normal approximation with bootstrap bias and s.e. (MATLAB bootci \"norm\"); 2,000\n    resamples, a standard choice. The paper does not say what is resampled or how the difference\n    is tested. Readings (B1) neurons resampled within each region; (B2) sessions resampled;\n    (S1) the bootstrap interval of the difference (same resamples) excludes 0; (S2) the two\n    intervals do not overlap. Reproduced when the three values are within tolerance and both\n    differences are significant under one reading.\n  depends_on:\n  - fig3d-vision-localized\n  - fig3e-action-global\n  - fig4b-choice-regions\n- id: ed5h-choice-shuffle-fpr\n  statement: With Left and Right choice labels shuffled, 14 neurons (0.33%) passed the Choice kernel\n    test, the false-positive rate of the test.\n  source: Extended Data Fig. 5h legend; Methods, Estimation of false positive rate\n  quote: A small number (14, 0.33%) of neurons are false positives in this shuffle test\n  expected:\n    quantity: false-positive rate of the Choice kernel test on shuffled labels\n    value: 0.33\n    tolerance: 0.17\n    unit: percent\n  criterion: Each Left or Right choice trial gets the choice of another Left or Right trial drawn\n    without replacement, and the whole kernel test K for Choice is rerun from the start (Methods).\n    The fraction is of neurons entering the nested test (full-model VE at least 2%; 14 of about\n    4,240). The tolerance is two Poisson s.d. of a count of 14 (7.5 neurons), since 10% (1.4\n    neurons) is below the spread of one shuffle. Reproduced when the fraction is within tolerance.\n  depends_on:\n  - fig4b-choice-regions\n- id: fig4b-choice-regions\n  statement: Choice-selective neurons were rare and found in frontal cortex (MOs, PL, MOp), basal\n    ganglia (CP, SNr), higher-order thalamus, SCm, MRN and ZI, but not in VISp; 54 were in the\n    midbrain (MRN, SCm, SNr, ZI) and 48 in the forebrain (MOs, PL, MOp, CP).\n  source: Results, Forebrain and midbrain choice coding, paragraphs 1 and 3; Fig. 4b\n  quote: These neurons were rare, and were found in frontal cortex (MOs, PL, and MOp), basal ganglia\n    (CP, SNr), higher-order thalamus, motor-related superior colliculus (SCm), as well as two\n    subcortical nuclei which unexpectedly contained neurons selective for choice (MRN and ZI ...\n    but choice-selective neurons were not found in VISp\n  expected:\n  - quantity: choice-selective neurons in midbrain (MRN, SCm, SNr, ZI)\n    value: 54\n    tolerance: 5.4\n  - quantity: choice-selective neurons in forebrain (MOs, PL, MOp, CP)\n    value: 48\n    tolerance: 4.8\n  criterion: Kernel test K for the Choice kernel, as in fig3d-vision-localized. Higher-order\n    thalamus is the thalamic regions other than LGd, VPL, VPM and MG. Reproduced when both counts are\n    within tolerance, VISp has no choice-selective neuron, each of MOs, PL, MOp, CP, SNr, SCm, MRN,\n    ZI and one higher-order thalamic region has at least one, and the overall fraction of analysed\n    neurons that are choice-selective is below 5%. Partially reproduced when the regions hold but\n    a count does not. The VISp count is reported with the count the 0.33% false-positive rate\n    predicts.\n- id: fig4c-choice-timing\n  statement: The time course of choice decoding did not differ between frontal cortex, striatum and\n    midbrain (two-way ANOVA on area and time, no effect of area and no interaction).\n  source: Results, Forebrain and midbrain choice coding, paragraph 2; Fig. 4c; Methods, Population\n    decoding\n  quote: the time course of choice decoding could not be statistically distinguished between\n    choice-selective regions in frontal cortex, striatum, and midbrain (two-way ANOVA on brain\n    region and time, interaction p > 0.05\n  statistics:\n  - about: time\n    test: two-way ANOVA\n    statistic: F = 10.43, 50 d.f.\n    p: 1.0e-71\n    p_relation: \"<\"\n  - about: area; the Methods print \"p<0.05\" while calling the effect not significant, the Fig. 4c\n      legend gives p>0.05\n    test: two-way ANOVA\n    statistic: F = 0.28, 2 d.f.\n    p: 0.05\n    p_relation: \"<\"\n  - about: interaction of time and area\n    test: two-way ANOVA\n    statistic: F = 0.12, 100 d.f.\n    p: 0.05\n    p_relation: \">\"\n    n: 29 frontal (MOs, PL, MOp), 29 midbrain (SCm, MRN, SNr, ZI) and 5 striatum (CP) populations\n  expected:\n  - quantity: frontal populations\n    value: 29\n    tolerance: 2.9\n  - quantity: midbrain populations\n    value: 29\n    tolerance: 2.9\n  - quantity: striatum populations\n    value: 5\n    tolerance: 0.5\n  criterion: Residual rates from the model without the Choice kernel (kernel test K, code\n    determineResidualsWithout \"moveLR\"), Left against Right choice trials; an L1-regularized\n    logistic regression on the residuals -0.05 to 0 s from movement onset of training trials; test\n    trials' residuals at each time projected on its weights; the score is the mean projection on\n    Left minus Right test trials (Methods). One population per area per recording; each score is\n    divided by its area's mean across recordings at choice time (movement onset). A claim of\n    absence, judged on the paper's test, a two-way ANOVA with factors time and area group (frontal,\n    midbrain, striatum), at alpha 0.05. Time has 51 levels (50 d.f.). Open details, each a reading\n    the notebook runs; (a) times -0.25 to 0 s from movement onset in 5 ms steps (the Choice kernel\n    support and bin) or (b) -0.2 to 0.05 s; folds (a) 5-fold or (b) 10-fold over trials; L1\n    strength (a) chosen by inner cross-validation or (b) the library default. Reproduced when the\n    interaction and area effects both have p > 0.05; not reproduced when either has p < 0.05. The\n    F values and the effect sizes are reported.\n  depends_on:\n  - fig4b-choice-regions\n- id: fig4d-jpecc-vis-leads\n  statement: In jPECC, visual cortex activity leads frontal cortex activity by about 40 ms in the\n    period about 200 ms before movement, and visual cortex leads frontal cortex and midbrain at about\n    100 ms after stimulus onset.\n  source: Fig. 4d legend; Extended Data Fig. 8d legend; Methods, jPECC analysis\n  quote: population activity in visual cortex predicts that in frontal cortex following a ~40 ms\n    lag, but only in the period ~200ms prior to movement\n  criterion: jPECC as in the Methods and jPECC.m. Recordings with neurons of both groups (VIS,\n    Frontal, Midbrain); spike counts in 10 ms bins, causal half-Gaussian of s.d. 25 ms, divided by\n    baseline + 1 sp/s; per group and time bin PCA to 10 dimensions (fewer if the group has fewer\n    neurons); 10-fold over trials; CCA on training PCs with L2 regularization lambda 0.5 (rows\n    lambda times identity appended, as jPECC.m); Pearson r of test projections on the first\n    canonical pair, for each pair of time bins. Asymmetry index at t, the mean r along the slice\n    from (t, t) to 50 ms of lead of the first group minus the mean along 50 ms of lead of the\n    second; across recordings a t-test against 0 at each t, alpha 0.05 (the paper names no\n    correction). Open; the baseline window, readings (a) -0.2 to 0 s and (b) -0.1 to 0 s before\n    stimulus onset; the trials, readings (a) all trials T for stimulus alignment and Left and Right\n    choice trials for movement alignment, (b) Left and Right choice trials for both. Reproduced\n    when, under one reading, VIS leads Frontal at time points between -0.2 and -0.05 s from\n    movement onset and VIS leads Frontal and Midbrain near 0.1 s after stimulus onset.\n- id: fig4d-jpecc-no-lag-frontal-midbrain\n  statement: Population activity in midbrain and frontal cortex shows no consistent lead or lag.\n  source: Results, Forebrain and midbrain choice coding, paragraph 2; Fig. 4d; Extended Data Fig. 8\n  quote: it revealed no lag for activity correlations between frontal and midbrain areas\n  criterion: A claim of absence, judged on the paper's test, the t-test across recordings of the\n    Frontal-Midbrain asymmetry index against 0 at each time point (as fig4d-jpecc-vis-leads, same\n    readings of the open details), alpha 0.05 uncorrected as the paper gives it. Reproduced when no\n    time point from -0.25 to 0 s from movement onset is significant; not reproduced when any is.\n    The mean index and the count of significant points are reported, with a Bonferroni variant.\n- id: fig4f-contralateral-preference\n  statement: Nearly all midbrain choice-selective neurons (53/54, 98%) preferred contralateral\n    choices, while 19/48 (40%) forebrain ones preferred ipsilateral choices, significantly more\n    than in the midbrain.\n  source: Results, Forebrain and midbrain choice coding, paragraph 3; Fig. 4e-g\n  quote: In midbrain (MRN, SCm, SNr, and ZI) nearly all choice-selective neurons (53/54, 98%)\n    preferred contralateral choices ... with a sizeable proportion preferring ipsilateral choices\n    (19/48, 40%, significantly more than in the midbrain\n  statistics:\n  - test: Fisher's exact test\n    p: 1.0e-5\n    p_relation: \"<\"\n    n: 54 midbrain and 48 forebrain choice-selective neurons\n  expected:\n  - quantity: midbrain choice-selective neurons preferring contralateral choices\n    value: 98\n    tolerance: 9.8\n    unit: percent\n  - quantity: forebrain choice-selective neurons preferring ipsilateral choices\n    value: 40\n    tolerance: 4.0\n    unit: percent\n  criterion: Choice-selective neurons of fig4b-choice-regions. Preference is the choice with the\n    higher model activity at movement onset relative to baseline (Fig. 4f,g legend, \"estimated\n    from the kernel model\"). Open is the model activity. Readings (a) the Action kernel plus or\n    minus the Choice kernel at lag 0 (kernels on baseline-subtracted rates); (b) the full model's\n    prediction at movement onset averaged over Left and over Right choice trials. Reproduced when\n    both percentages are within tolerance and a two-sided Fisher's exact test of the 2 by 2 table\n    has p < 1e-5, under one reading.\n  depends_on:\n  - fig4b-choice-regions\n- id: fig4fg-opposed-activity\n  statement: Many midbrain choice-selective neurons (29/54, 54%) increased before one choice and\n    were suppressed below baseline before the other, against 10/48 (21%) in the forebrain.\n  source: Results, Forebrain and midbrain choice coding, paragraph 3; Fig. 4f,g\n  quote: Many midbrain choice-selective neurons, moreover, exhibited directionally-opposed activity\n    ... (10/48, 21% suppressed for non-preferred choice, significantly less than in the midbrain\n  statistics:\n  - test: Fisher's exact test\n    p: 0.001\n    p_relation: \"<\"\n    n: 54 midbrain and 48 forebrain choice-selective neurons\n  expected:\n  - quantity: midbrain choice-selective neurons suppressed for the non-preferred choice\n    value: 54\n    tolerance: 5.4\n    unit: percent\n  - quantity: forebrain choice-selective neurons suppressed for the non-preferred choice\n    value: 21\n    tolerance: 2.1\n    unit: percent\n  criterion: As fig4f-contralateral-preference, a neuron being suppressed when its model activity\n    for the non-preferred choice at movement onset is below baseline (below 0 after the baseline\n    subtraction), under readings (a) and (b). Reproduced when both are within tolerance and the\n    two-sided Fisher's exact test has p < 1e-3, under one reading.\n  depends_on:\n  - fig4b-choice-regions\n- id: ed7b-detect-probability-widespread\n  statement: Neurons with significant detect probability (Go against NoGo for the same stimulus)\n    around movement onset are found widely across regions, replicating the global action signal.\n  source: Extended Data Fig. 7b legend; Methods, ccCP and Detect Probability analysis\n  quote: Percentage of neurons in each area with significant Detect Probability measured around\n    movement onset, replicating the finding from Fig 2d,e and Fig 3e that non-selective action\n    signals are distributed widely\n  criterion: ccCP algorithm of the Methods and choiceProbShuf.m, Go (Left or Right) against NoGo\n    trials (T) within each of the 16 stimulus conditions, 2,000 within-condition label shuffles; a\n    neuron is significant when its rank among shuffles puts it below 0.025 or above 0.975 (chance\n    5%, the dashed line of the legend). Sessions with fewer than 10 includable trials left out. NoGo\n    trials take a movement time drawn from the Go trials (definition T). The window \"around\n    movement onset\" is open; readings (a) -0.1 to 0.05 s (the pre-movement window of test 3);\n    (b) -0.05 to 0 s (the choice decoding window). Regions are marked when the 95% binomial\n    interval of the fraction (Clopper-Pearson, a standard choice) excludes 5%. Reproduced when at\n    least three quarters of regions are marked above chance under one reading.\n- id: ed7c-choice-probability-restricted\n  statement: Neurons with significant choice probability around movement onset are restricted to\n    frontal cortex, basal ganglia, midbrain and certain thalamic nuclei; six sessions were\n    excluded for too few trials, holding 20.8% of the MOs choice-selective neurons of the kernel\n    analysis.\n  source: Extended Data Fig. 7c legend; Methods, ccCP and Detect Probability analysis\n  quote: this analysis broadly replicates the finding from Fig 4b that choice selective neurons,\n    around the time of movement onset, are restricted to frontal cortex, basal ganglia, midbrain,\n    and certain thalamic nuclei\n  expected:\n  - quantity: sessions excluded from ccCP for fewer than 10 includable trials\n    value: 6\n    tolerance: 0\n  - quantity: MOs choice-selective neurons (kernel test) in the excluded sessions\n    value: 20.8\n    tolerance: 2.1\n    unit: percent\n  criterion: As ed7b-detect-probability-widespread, for Left against Right choice trials within\n    stimulus conditions; only conditions with both choices contribute. Reproduced when, under one\n    reading, no VIS area and no hippocampal region (CA1, CA3, DG, SUB, POST) is marked above chance,\n    at least one frontal, one basal ganglia (CP, GPe, SNr, ACB, LS) and one midbrain region is, and\n    six sessions are excluded. Partially reproduced when the regional pattern holds and the\n    session count does not.\n  depends_on:\n  - fig4b-choice-regions\n- id: ed5g-ipsilateral-vision-rare\n  statement: Ipsilateral visual stimuli are hardly encoded, unlike contralateral ones.\n  source: Methods, Determining individual neuron selectivity, paragraph 2; Extended Data Fig. 5g\n  quote: since the same argument should apply to Ipsilateral Vision correlates, and we found very\n    little of such correlates\n  criterion: Population decoding of the Methods (as fig4c-choice-timing) of contralateral against\n    no contralateral stimulus, and ipsilateral against no ipsilateral stimulus, on residuals from\n    the model without the tested Vision kernels, logistic regression on 0.05 to 0.15 s after\n    stimulus onset; mean score per area. Same open readings as fig4c-choice-timing. Reproduced when\n    the largest area mean for ipsilateral decoding is below a quarter of the largest for\n    contralateral decoding under every reading. The counts of neurons requiring each kernel (test\n    K) are shown as a variant.\n- id: fig3c-variance-explained\n  statement: The kernels often explained a small fraction of cross-validated variance, even for\n    neurons whose mean rates they predicted well (50.2% for the Fig. 3a neuron, 13.6% for the Fig.\n    3b neuron).\n  source: Results, Globally distributed action coding, paragraph 2; Fig. 3c\n  quote: The fraction of cross-validated variance the kernels explained was frequently small ...\n    (50.2% for the neuron in Fig. 3a and 13.6% for the neuron in Fig. 3b\n  expected:\n  - quantity: full-model VE, Fig. 3a VISpm neuron\n    value: 50.2\n    tolerance: 5.0\n    unit: percent\n  - quantity: full-model VE, Fig. 3b SUB neuron\n    value: 13.6\n    tolerance: 1.4\n    unit: percent\n  criterion: Full-model cross-validated VE (kernel test K). Reproduced when the median VE over all\n    analysed neurons is below 10% (this file's reading of \"frequently small\") and, if the two\n    example neurons can be identified (the paper gives only their regions and rasters, Figs. 2a,b\n    and 3a,b), their VE is within tolerance. When they cannot be identified the claim is judged on\n    the median alone and the examples are reported as not identifiable.\n- id: fig5b-miss-more-than-passive\n  statement: More neurons were significantly activated by contralateral visual stimuli on Miss\n    trials in the task than on passive trials with the same contrasts, and passive responses were\n    weaker than those on Miss trials.\n  source: Results, Distributed coding of task engagement, paragraph 1; Fig. 5b; Fig. 2h\n  quote: more neurons were significantly activated by visual stimuli during the task (Miss trials),\n    than in the passive trials\n  expected:\n    quantity: sessions with enough contrast-matched trials\n    value: 34\n    tolerance: 0\n  criterion: Contrast-matched (M) Miss and passive trials; per region the fraction of neurons\n    significantly activated (definition R, z > 4; readings Z1, Z2). Neurons are open; readings\n    (a) neurons N of the Figs. 3 to 5 set; (b) all neurons of the 42 regions with a rate of at least\n    0.1 Hz. Passive trials with a wheel movement in -0.05 to 0.4 s are kept (the Methods drop none).\n    Reproduced when, under one reading, the pooled fraction is larger on Miss than on passive\n    trials, the excess (Miss minus passive) is positive in more than half the regions, and 34\n    sessions are kept.\n- id: fig5c-prestimulus-task-vs-passive\n  statement: Before the stimulus, neocortex and sensory thalamus were less active in the task than\n    in the passive context, while basal ganglia and other subcortical choice areas were more\n    active; VISp was lower and CP higher in the task.\n  source: Results, Distributed coding of task engagement, paragraph 1; Fig. 5a,c; Extended Data Fig.\n    9a; Methods, Engagement Index and pre-stimulus analyses\n  quote: While neocortex and sensory thalamus showed a net decrease in pre-stimulus activity during\n    task context, other regions ... showed a consistent increase\n  criterion: Per region a nested ANOVA (Methods) on each neuron's mean rate 250 to 50 ms before\n    stimulus onset, log10(x + 1 sp/s), trials with wheel movement in that window dropped. The\n    factors are open, as the Methods and the Extended Data Fig. 9a legend disagree; readings (a)\n    condition, session and neuron nested in session (Methods); (b) condition, session and subject\n    (legend). Task trials are trials T; passive trials are open, readings (a) all passive replay\n    events; (b) passive visual stimulus presentations. A region differs when the condition p <\n    0.0012 (0.05 over 42 regions). Reproduced when, under one reading, every differing neocortical\n    region is lower in the task, every differing non-neocortical region other than visual thalamus\n    (LGd, LP, LD) is higher, VISp differs and is lower, and CP differs and is higher.\n- id: ed6b-prestimulus-order\n  statement: Pre-stimulus firing in midbrain, basal ganglia and hippocampal regions is ordered\n    Passive < Miss < Go, while in neocortical areas it is higher in Passive than in Miss and Go.\n  source: Extended Data Fig. 6b legend\n  quote: the pre-stimulus firing rate of midbrain, basal ganglia, and hippocampal regions is in the\n    order Passive < Miss < Go; whereas pre-stimulus activity in neocortical areas instead is\n    arranged as Passive > Miss and Go\n  criterion: Per region the mean over neurons (N, Figs. 3 to 5 set) of the mean pre-stimulus rate\n    on contrast-matched (M) Go, Miss and passive trials. The window is open; readings (a) -0.2 to 0\n    s (the engagement index window); (b) -0.25 to -0.05 s (the nested ANOVA window). Groups from\n    utils/brainRegionGroups.m (midbrain MRN, SCm, SCs, APN, PAG; basal ganglia CP, GPe, SNr, ACB,\n    LS; hippocampus POST, SUB, DG, CA1, CA3); neocortex as defined above. Reproduced when, under one\n    reading, more than half the midbrain, basal ganglia and hippocampal regions show Passive < Miss\n    < Go and more than half the neocortical regions show Passive above both Miss and Go.\n- id: fig5d-go-miss-matches-task-passive\n  statement: Regions whose pre-stimulus rate differed between task and passive contexts showed\n    similar differences between Go and Miss trials.\n  source: Results, Distributed coding of task engagement, paragraph 2; Fig. 5d\n  quote: Areas that showed differences in pre-stimulus firing rate between task and passive contexts\n    also showed similar differences between Go and Miss trials\n  criterion: Per region the mean over neurons of task minus passive and of Go minus Miss\n    pre-stimulus rates (as ed6b-prestimulus-order, same readings), contrast-matched. The paper gives\n    no test for Fig. 5d; the test used is the Pearson correlation across regions, the measure the\n    paper reports for the companion comparison of Extended Data Fig. 7f. Reproduced when r > 0 with\n    p < 0.05 under one reading.\n- id: ed7f-detect-probability-engagement\n  statement: The pre-stimulus detect probability of each area correlated with its task minus\n    passive difference (r = 0.48, p = 0.001), as the Go minus Miss difference does.\n  source: Extended Data Fig. 7f legend\n  quote: The pre-stimulus Detect Probability was correlated with the Engagement Index (i.e.\n    Task-Passive difference) similarly to the Go-Miss difference (with r = 0.48, p=0.001; not shown)\n  statistics:\n  - test: correlation\n    statistic: r = 0.48\n    p: 0.001\n  expected:\n    quantity: correlation across areas of pre-stimulus DP minus 0.5 and task minus passive rate\n    value: 0.48\n    tolerance: 0.048\n  criterion: Per neuron the pre-stimulus DP (ccCP of Go against NoGo within stimulus conditions,\n    minus 0.5); per area the mean over neurons; Pearson r across areas with the area's mean task\n    minus passive pre-stimulus rate (as fig5d-go-miss-matches-task-passive). Windows as in\n    ed6b-prestimulus-order, readings (a) and (b). Reproduced when r is within tolerance and p <\n    0.05 under one reading.\n- id: fig5f-engagement-index\n  statement: An engagement index, the projection of pre-stimulus population activity onto the task\n    minus passive difference vector, was higher on Go than on Miss trials consistently across\n    recordings (mean difference 8.42 a.u., paired t-test p < 1e-4).\n  source: Results, Distributed coding of task engagement, paragraph 2; Fig. 5f; Methods, Engagement\n    Index and pre-stimulus analyses\n  quote: This engagement index differed between Go and Miss trials consistently across recordings\n    ... paired t-test\n  statistics:\n  - test: paired t-test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 34 sessions\n  expected:\n  - quantity: mean over recordings of the Go minus Miss engagement index\n    value: 8.42\n    tolerance: 0.84\n    unit: a.u. (sp/s projected on a unit vector)\n  - quantity: neurons in the index per session, mean\n    value: 319\n    tolerance: 32.5\n  - quantity: sessions\n    value: 34\n    tolerance: 0\n  criterion: Neurons of the regions that differ in fig5c-prestimulus-task-vs-passive, x_n the mean\n    rate -0.2 to 0 s before stimulus onset on all task trials minus that on all passive trials,\n    normalized to unit L2 norm per session; the index of trial i is x times the trial's\n    pre-stimulus rate vector; per session the mean on Go minus the mean on Miss trials, with N\n    trials per contralateral contrast, N the smaller of the Go and NoGo counts (Methods). Open;\n    readings of task trials (a) trials T, (b) all task trials; of the contrast conditions (a)\n    contralateral contrast > 0, (b) every contralateral contrast with a stimulus present. The\n    tolerance of the neuron count is the paper's s.e. Reproduced when the paired t-test across\n    sessions has p < 1e-4 with Go higher and the mean is within tolerance, under one reading;\n    partially reproduced when the test holds and the mean does not.\n  depends_on:\n  - fig5c-prestimulus-task-vs-passive\n- id: fig5e-engagement-predicts-go\n  statement: The probability of a Go response rises with the engagement index on single trials.\n  source: Results, Distributed coding of task engagement, paragraph 2; Fig. 5e\n  quote: it was possible to predict whether an animal would respond to the stimulus on a given trial\n    within the task context, by projecting pre-stimulus population activity onto a weight vector\n    given by the difference of pre-stimulus activity in passive and task contexts\n  criterion: Engagement index as in fig5f-engagement-index, z-scored; contrast-matched Go and Miss\n    trials pooled over sessions; logistic regression of Go on the index (Fig. 5e legend). Open is\n    the z-scoring, readings (a) within session, (b) over all trials. Reproduced when the slope is\n    positive and its 95% interval excludes 0 under one reading.\n  depends_on:\n  - fig5f-engagement-index\n- id: ed9i-engagement-beyond-arousal\n  statement: The engagement index improves the prediction of Go responses beyond inter-trial\n    interval, previous reward, pupil area and motion energy (deviance test, p = 1.5e-8).\n  source: Extended Data Fig. 9i legend; Methods, GLM prediction of P(Go) from pre-stimulus variables\n  quote: The null hypothesis that engagement index had no additional effect on Go probability over\n    all other variables was rejected using a deviance test (p=1.5e-8)\n  statistics:\n  - test: deviance test\n    p: 1.5e-8\n  criterion: Binomial GLM of Go against Miss on inter-trial interval, previous reward (0 or 1),\n    pre-stimulus pupil area and motion energy (z-scored) and their squares, against the same model\n    plus the engagement index, contrast-matched trials (Methods). Sessions with usable pupil video\n    only (34 of 39 in the Methods). Open; the pre-stimulus window, readings (a) -0.2 to 0 s, (b)\n    -0.25 to -0.05 s; pooling, readings (a) all sessions in one GLM, (b) one GLM per session with the\n    deviances summed. Reproduced when the deviance test has p < 0.05 under one reading; p is\n    reported against 1.5e-8.\n  depends_on:\n  - fig5f-engagement-index\n- id: ed9cf-engagement-controls\n  statement: The Go against Miss difference in engagement index persists on trials after rewards,\n    after regressing out previous reward, and on trials after short and after long inter-trial\n    intervals.\n  source: Extended Data Fig. 9c-f legend\n  quote: c-f, Same plot after restricting to contrast-matched trials following rewards ... The\n    effect persists in each case\n  criterion: The index of fig5f-engagement-index on four trial sets; trials after a rewarded trial;\n    all trials with each previous-reward group's mean subtracted; trials after short and after long\n    inter-trial intervals. Open; the interval split, readings (a) median per session, (b) median\n    over all trials; the test (Extended Data Fig. 9b says t-test), readings (a) paired t-test across\n    sessions, (b) two-sample t-test over pooled Go and Miss trials. Reproduced when all four sets\n    give Go higher with p < 0.05 under one reading.\n  depends_on:\n  - fig5f-engagement-index\n- id: ed9k-engagement-vector-specific\n  statement: The engagement vector correlates better with the Go minus Miss vector than with the\n    vectors of other behavioural variables, though not significantly for previous reward (p =\n    0.096).\n  source: Extended Data Fig. 9k legend\n  quote: In each case we find that the correlation is greater for the Go-Miss vector (not reaching\n    significance at alpha=0.05 level, however, for the comparison with the previous reward vector,\n    p=0.096)\n  statistics:\n  - about: Go-Miss against previous reward correlations\n    p: 0.096\n  criterion: Per recording, the Pearson correlation over neurons between the engagement vector\n    (task minus passive pre-stimulus rate) and the Go minus Miss vector, and between the engagement\n    vector and each other variable's vector. Open; each variable's vector, readings (a) the\n    difference of pre-stimulus rates between trials above and below the variable's median (for\n    previous reward, rewarded minus not); (b) each neuron's regression slope on the variable; the\n    test across recordings, readings (a) paired t-test, (b) Wilcoxon signed-rank. Variables are\n    pupil area, motion energy, inter-trial interval and previous reward. Reproduced when, under one\n    reading, the Go-Miss correlation is larger on average for all four and the difference has p <\n    0.05 for pupil, motion energy and inter-trial interval.\n  depends_on:\n  - fig5f-engagement-index\n- id: suppfig3-nonresponsive-neurons\n  statement: The engagement index differs between Go and Miss trials even when computed from\n    neurons that are otherwise not responsive in the task.\n  source: Results, Distributed coding of task engagement, paragraph 1; Supplementary Fig. 3 legend\n  quote: All neurons show a significant difference in Engagement Index between Go and Miss trials\n  criterion: As fig5f-engagement-index, computed separately from all neurons, from task-responsive\n    neurons (the Figs. 3 to 5 set) and from the others of the same regions. The p-values are only\n    in the figure. Reproduced when the paired t-test gives Go higher with p < 0.05 for each set.\n  depends_on:\n  - fig5f-engagement-index\n- id: histology-alignment-error\n  statement: Probe tracks were localized with a lateral error of 39.3 um (median distance of DiI\n    spots from the fitted track) and a longitudinal error of 88.7 um (median absolute deviation of\n    held-out landmarks), with 15.1 ± 6.9 DiI spots per probe and a scaling of 1.08 ± 0.02.\n  source: Methods, Anatomical targeting and probe localization, paragraphs 2 and 3\n  quote: We quantified the lateral localization error by the median distance of the DiI spots from\n    this common trajectory (39.3 μm)\n  expected:\n  - quantity: median distance of DiI spots from the fitted trajectory\n    value: 39.3\n    tolerance: 3.9\n    unit: um\n  - quantity: median absolute deviation of held-out landmark errors\n    value: 88.7\n    tolerance: 8.9\n    unit: um\n  - quantity: DiI spots per probe, mean\n    value: 15.1\n    tolerance: 6.9\n  - quantity: scaling factor, mean\n    value: 1.08\n    tolerance: 0.02\n  criterion: Needs the DiI spot coordinates in the atlas and the electrophysiological landmarks per\n    probe (Methods); the trajectory by total least squares (Extended Data Fig. 2b), the longitudinal\n    map by linear regression of landmarks, leave-one-landmark-out errors. Reproduced when all four\n    values are within tolerance (the tolerances of the last two are the paper's s.d.).\n"
}
```

```
File created successfully at: claims/000017/10.1038-s41586-019-1787-x.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000017/10.1038-s41586-019-1787-x.yaml paper/10.1038-s41586-019-1787-x.txt; grep -n " — \|—\|rather\|Rather" claims/000017/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes with no problems: 40 claims, 38 quotes, 11 statistical values. One more check: whether any loaded string contains ": ".

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml
d=yaml.safe_load(open('claims/000017/10.1038-s41586-019-1787-x.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print(p, x[:80])
walk(d)
c=d['claims']; print(len(c), sum('quote' in x for x in c), sum('statistics' in x for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c))
"; git status --short
```

```
40 38 9 40 21
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
?? claims/000017/
?? scripts
```

**Agent**

I've written the claims file for DANDI:000017 at `claims/000017/10.1038-s41586-019-1787-x.yaml`. The quote checker passes with no problems, nothing was committed, and the dataset's data were not opened.

**Text read**
- The accepted author manuscript from Europe PMC (PMC6913580): main text, Methods, figure and Extended Data legends, and Extended Data Table 1.
- Both supplement Word files: the Supplementary Discussion, Supplementary Tables 1 and 2, and the legends of Supplementary Figs. 1 to 4.
- One value comes from the Word file itself: the "±" in the Supplementary Fig. 2 legend is lost in the text, and the Word file shows it (0.35 ± 0.04 and 0.10 ± 0.02).
- No PDF was opened. Supplementary Table 3 is only an image and was not read; no claim needs it.

**Code read**
- github.com/nsteinme/steinmetz-et-al-2019 at commit 9a0bea8. It holds the kernel regression, the trial movement classification, jPECC, the combined-conditions choice probability (ccCP) shuffle, and per-session arrays of included trials and units.
- It has no code for the passive-context, engagement-index, nested ANOVA, GLM, focality, Fisher-test or decoding analyses, so the Methods alone fix those.
- The code fixes several kernel details the Methods leave open: baseline subtraction, a basis shared by all sessions, a fixed penalty of 0.5, 5-fold cross-validation with up to 50 components for the full model, 75 components for the residual fit, 18 components and 10-fold cross-validation for the test kernel, and the scoring windows.

**Claims**: 40 in all. 38 have quotes; 2 are read from tables (Extended Data Table 1, Supplementary Tables 1 and 2). 9 carry statistics (11 values), 21 have expected values, and all 40 have criteria.

**Details the paper leaves open, with the readings named**
- **Trial selection:** the Methods rule against the code rule. The code drops NoGo trials with no movement before feedback, which the Methods do not; it is kept as a variant.
- **Neuron selection:** the code keeps about 1,000 neurons whose test returned NaN (its own comment calls this a bug); kept as a variant.
- **Which trials enter the behaviour figures:** all trials, or trials after dropping disengaged ones.
- **Reaction-time ANOVA:** its factors are not named. Readings: condition class with session, or with subject.
- **Wheel choice decoder:** not named. Readings: the sign of the velocity, or a cross-validated logistic regression.
- **Passive no-movement:** the window (−0.05 to 0.4 s or 0 to 0.4 s) and whether the value is a session mean or pooled.
- **"Consistently increased":** which responsiveness tests set the direction.
- **Supplementary Fig. 2:** what the d′ spread is taken over.
- **Significance z-score:** standard error or s.d. as the denominator.
- **Fig. 2 activity order:** which neurons count as responsive, and the latency measure (half-maximum or peak).
- **Focality bootstrap:** what is resampled (neurons within regions, or sessions) and how the difference is tested (its interval excludes 0, or the two intervals don't overlap).
- **Choice-timing decoding:** the time range (−0.25 to 0 s or −0.2 to 0.05 s), 5- or 10-fold, and the L1 strength.
- **jPECC:** the baseline window and which trials enter.
- **Contralateral preference and suppression:** model activity as the kernels at lag 0, or the full-model prediction.
- **ccCP:** the window around movement onset (−0.1 to 0.05 s or −0.05 to 0 s).
- **Nested ANOVA:** its factors (the Methods and the Extended Data Fig. 9a legend disagree) and which passive trials enter.
- **Pre-stimulus window:** −0.2 to 0 s or −0.25 to −0.05 s.
- **Engagement index:** which task trials and contrast conditions enter, z-scoring within session or pooled, pooling of the GLM, the inter-trial-interval split, the t-test form, and how each other variable's vector is defined.

**Problems in the paper itself**
- The Methods print p<0.05 for the area effect in the choice-timing ANOVA while calling it not significant; the Fig. 4c legend gives p>0.05.
- Extended Data Table 1's responsive column sums to 13,467, against 13,466 in the Results.

**What claims need that the paper lacks**
- **Fig. 5d:** the paper gives no test. I used a Pearson correlation across regions, the measure it reports for the matching Extended Data Fig. 7f comparison.
- **Vague wording:** where the paper says "widely", "frequently small" or "essentially no", the criterion sets the thresholds, and each says so.
- **Example neurons (Figs. 2 and 3):** the paper does not identify them beyond their region.
- **Repo's inclusion arrays:** the paper never says which selection they hold. They contain 18,248 of 48,661 units and 6,569 of 10,050 trials.
- **Histology:** the alignment-error claim needs DiI-spot and landmark data that may not be in the dataset.

Nothing the claims rest on is missing from the text.

## End of run

29 turns, 10 minutes, result: success.
