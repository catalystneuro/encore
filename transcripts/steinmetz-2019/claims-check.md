# 000017 · claims-check · run 39661631609

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000017/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; python tools/claims_check.py claims/000017/10.1038-s41586-019-1787-x.yaml paper/10.1038-s41586-019-1787-x.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000017/10.1038-s41586-019-1787-x.yaml"
}
```

```
1	# Claims for Steinmetz, Zatka-Haas, Carandini & Harris (2019), Nature 576, 266-273, "Distributed
2	# coding of choice, action and engagement across the mouse brain", on dandiset 000017.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
4	# pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the accepted author manuscript as served by Europe PMC (PMC6913580, UKPMC Funders
7	# Author Manuscripts), with the main text, Methods, Extended Data figure legends, Extended Data
8	# Table 1 and the figure legends. Both supplement files from the PMC Open Access data were read:
9	# supplement 1 (Supplementary Information guide, Supplementary Tables 1 and 2, legends of
10	# Supplementary Figs. 1 to 4) and supplement 2 (Supplementary Discussion and the same tables and
11	# legends). The "±" of the Supplementary Fig. 2 legend is lost in the text ("d'=0.350.04"); the
12	# Word file holds a Symbol-font "±" there (0.35 ± 0.04 and 0.10 ± 0.02). Supplementary Table 3 is
13	# only an image and was not read. No PDF was opened. In Extended Data Table 1 the text prints VISl
14	# and VISrl as "VISI" and "VISrI".
15	#
16	# Code read: github.com/nsteinme/steinmetz-et-al-2019 at commit 9a0bea8 (2021-08-09, head of
17	# master). It holds the reduced-rank kernel regression (reducedRankRegression/: kernelFitBasic.m,
18	# regFullPipeline.m, determineResidualsWithout.m, predictResidualsWith.m, CanonCor2all.m,
19	# KernelModel.m, KernelEventSeries.m), the trial movement classification (behavior/findMoveTimes.m),
20	# jPECC (jPECC/jPECC.m), the ccCP shuffle (ccCP/choiceProbShuf.m, mannWhitneyUshuf.m), data browsers
[... 898 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-019-1787-x.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41586-019-1787-x.txt').read()
print(t[57200:100000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/cc4a23bf-9314-424b-82cc-718beb769a03/tool-results/bky9naep4.txt"
}
```

```
1	 to stimulus onset for Vision decoding, and the period -0.05 to 0 s relative to movement onset for Action or Choice decoding. We then predicted the binary category of test data by projecting firing rates from test set trials, from each time point during the trial, onto the weight vector of the logistic regression. (Although it is in principle possible that these signals are encoded in a nonlinearly separable way, the robust predictions obtained suggest information can be read out linearly.) The population decoding was taken as the difference between projections between test set trials of each binary category. For Action decoding, where trials with Left or Right choices were compared to those with neither, a “movement onset time” was chosen for trials without a movement randomly from the distribution of movement onset times on Left and Right choice trials. To statistically compare decoding time course across areas, we took the population decoding score from each key area in each recording (n=29 populations from frontal cortex including MOs, PL, and MOp; n=29 populations from midbrain including SCm, MRN, SNr, ZI; n = 5 striatum, CP), and normalized each so the mean across recordings within an area was 1 at choice time. We then performed a two-way ANOVA, with factors time relative to movement onset and area (frontal, midbrain, striatum). We found a significant effect of time (50 d.f., F = 10.43, p<10 -71 ) but no significant effect of area (2 d.f., F = 0.28, p<0.05) and no significant interaction between time and area (100 d.f., F = 0.12, p>0.05). Joint Peri-event Canonical Correlation (jPECC) analysis To perform jPECC analysis ( Figure 4d , Extended Data Fig. 8 ), we took spike counts of individual neurons from simultaneously recorded regions, combining neurons from all regions within a group (“VIS”: VISp, VISpm, VISl, VISrl, VISa, VISam; “Midbrain”: SCm, MRN, ZI, SNr; “Frontal”: MOs, MOp, PL). Thus, only one jPECC per pair of region groups could be computed per rec
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41586-019-1787-x.txt').read()
i=t.find('Author contributions N.A.S.')
print(t[i:i+40000])" > $TMPDIR/rest.txt; wc -c $TMPDIR/rest.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/rest.txt"
}
```

```
1	Author contributions N.A.S., M.C., and K.D.H. conceived and designed the study. N.A.S. collected data. N.A.S., P.Z-H., and K.D.H. analyzed data. N.A.S., M.C., and K.D.H. wrote the manuscript. Reprints and permissions information is available at www.nature.com/reprints . The authors declare no competing interests. Data and code availability statement The behavioral and neural datasets generated and analyzed in this study are available on figshare with the identifier doi:10.6084/m9.figshare.9598406. The code used to analyze the data is available at https://github.com/nsteinme/steinmetz-et-al-2019 . 1 Jun J Fully Integrated Silicon Probes for High-Density Recording of Neural Activity Nature 2017 551 232 236 29120427 10.1038/nature24636 PMC5955206 2 Steinmetz NA Koch C Harris KD Carandini M Challenges and opportunities for large-scale electrophysiology with Neuropixels probes Curr Opin Neurobiol 2018 50 92 100 29444488 10.1016/j.conb.2018.01.009 PMC5999351 3 Burgess CP High-Yield Methods for Accurate Two-Alternative Visual Psychophysics in Head-Fixed Mice Cell Rep 2017 20 2513 2524 28877482 10.1016/j.celrep.2017.08.047 PMC5603732 4 Cisek P Kalaska JF Neural Mechanisms for Interacting with a World Full of Action Choices Annu Rev Neurosci 2010 33 269 298 20345247 10.1146/annurev.neuro.051508.135409 5 Romo R De Lafuente V Conversion of sensory signals into perceptual decisions Prog Neurobiol 2013 103 41 75 22472964 10.1016/j.pneurobio.2012.03.007 6 Ding L Gold JI The basal ganglia’s contributions to perceptual decision making Neuron 2013 79 640 649 23972593 10.1016/j.neuron.2013.07.042 PMC3771079 7 Hikosaka O Takikawa Y Kawagoe R Role of the basal ganglia in the control of purposive saccadic eye movements Physiol Rev 2000 80 953 10893428 10.1152/physrev.2000.80.3.953 8 Felsen G Mainen ZF Midbrain contributions to sensorimotor decision making J Neurophysiol 2012 108 135 147 22496524 10.1152/jn.01181.2011 PMC3434602 9 Gao Z A cortico-cerebellar loop for motor planning Natu
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41586-019-1787-x.txt').read()
i=t.find('Supplementary Table 1',t.find('##### Supplement: EMS84617-supplement-2'))
print(len(t)-i); print(t[i:])" | head -c 20000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41586-019-1787-x.txt').read()
a=t.find('##### Supplement: EMS84617-supplement-1'); b=t.find('##### Supplement: EMS84617-supplement-2')
print(t[a:b])
import re
for m in re.finditer('Supplementary Table',t): print(m.start(), t[m.start():m.start()+120].replace('\n',' '))
"
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passed with no problems. Now I'm verifying the supplement tables, since the text holds only the session table.

**Agent calls Bash**

```bash
cd $TMPDIR && rm -rf s1 && mkdir s1 && cd s1 && unzip -q -o paper/10.1038-s41586-019-1787-x.supp1.docx && python3 -c "
import re;x=open('word/document.xml').read();t=re.sub(r'</w:p>','\n',x);t=re.sub(r'<w:tab/>',' | ',t);t=re.sub(r'<[^>]+>','',t);print(t[:6000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && rm -rf s2 && mkdir s2 && cd s2 && unzip -q -o paper/10.1038-s41586-019-1787-x.supp2.docx && ls -R word | head -30 && python3 -c "
import re;x=open('word/document.xml').read()
i=x.find('Supplementary Table 1');j=x.find('Supplementary Table 2 |') if 'Supplementary Table 2 |' in x else x.find('Recording sessions')
t=x[i-3000:i+600];t=re.sub(r'</w:p>','\n',t);t=re.sub(r'<[^>]+>','',t);print(t)
print('sex' in x.lower(), 'female' in x.lower(), 'genotype' in x.lower())
k=x.find('0.35');print(x[k-300:k+600])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/s2 && python3 -c "
import re;x=open('word/document.xml').read()
t=re.sub(r'</w:tc>',' | ',x);t=re.sub(r'</w:p>','\n',t);t=re.sub(r'<[^>]+>','',t)
i=t.find('Supplementary Table 1 |');print(t[i-1500:i+300])
j=t.find('Supplementary Table 2 |');print('----');print(t[j-300:j+200])"
```

```
contralateral interconnectivity in the thalamus of rats. J Comp Neurol 436:52–63. 
Roseberry TK, Lee AM, Lalive AL, Wilbrecht L, Bonci A, Kreitzer AC (2016) Cell-Type-Specific Control of Brainstem Locomotor Circuits by Basal Ganglia. Cell 164:526–537 
Sachidhanandam S, Sreenivasan V, Kyriakatos A, Kremer Y, Petersen CCH (2013) Membrane potential correlates of sensory perception in mouse barrel cortex. Nat Neurosci 16:1671–1677 
Tonelli L, Chiaraviglio E (1993) Enhancement of water intake in rats after lidocaine injection in the zona incerta. Brain Res Bull 31:1–5. 
Tonelli L, Chiaraviglio E (1995) Dopaminergic neurons in the zona incerta modulates ingestive behavior in rats. Physiol Behav 58:725–729. 
Trageser JC, Burke KA, Masri R, Li Y, Sellers L, Keller A (2006) State-Dependent Gating of Sensory Inputs by Zona Incerta. J Neurophysiol 96:1456–1463 
Wang X-J (2008) Decision Making in Recurrent Neuronal Circuits. Neuron 60:215–234 
Zatka-Haas P, Steinmetz NA, Carandini M, Harris KD (2018) Distinct contributions of mouse cortical areas to visual discrimination. bioRxiv:501627. 



Subject ID
 | Sex
 | Genotype
 | Cori
 | F
 | tetO-G6s x CaMK-tTA
 | Forssmann
 | M
 | C57BL/6J
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import re
t=open('paper/10.1038-s41586-019-1787-x.txt').read()
i=t.find('Extended Data Table 1 Brain regions recorded');s=t[i:t.find('Supplementary Material',i)]
rows=re.findall(r'(\d+) (\d+) (\d+) (\d+) (\d+\.\d)',s)
print(len(rows),sum(int(r[2]) for r in rows),sum(int(r[3]) for r in rows))
"; ls; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -rn -A12 "^checks:" claims/*/*.yaml | head -40
```

```
claims/000005/10.1038-nn.4412.yaml:1092:checks:
claims/000005/10.1038-nn.4412.yaml-1093-- date: 2026-10-20
claims/000005/10.1038-nn.4412.yaml-1094-  kind: agent
claims/000005/10.1038-nn.4412.yaml-1095-  model: claude-opus-5-5
claims/000005/10.1038-nn.4412.yaml-1096-  ready: true
claims/000005/10.1038-nn.4412.yaml-1097-  changes:
claims/000005/10.1038-nn.4412.yaml-1098-  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
claims/000005/10.1038-nn.4412.yaml-1099-  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
claims/000005/10.1038-nn.4412.yaml-1100-  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
claims/000005/10.1038-nn.4412.yaml-1101-  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
claims/000005/10.1038-nn.4412.yaml-1102-  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
claims/000005/10.1038-nn.4412.yaml-1103-  - exc-thalamus-photoinhibition. Removed latency reading (b), a 3 s.d. threshold on Vm that appears nowhere in the paper. The Methods' touch-latency rule is applied to laser onset, and the criterion says this is an assumption.
claims/000005/10.1038-nn.4412.yaml-1104-  - pv-enphr-suppression. Same change for its latencies; the Methods' dPSTH/dt rule is applied to the laser-onset PSTH, as an assumptio
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://github.com/nsteinme/steinmetz-et-al-2019 code 2>&1 | tail -2; cd code 2>/dev/null && git log -1 --format='%h %ad' && grep -rn -i "ranksum\|signrank" --include=*.m . | head -20
```

```
9a0bea8 Mon Aug 9 16:38:34 2021 -0700
./reducedRankRegression/kernelFitBasic.m:134:        pvals(q,1) = signrank(xx); 
./reducedRankRegression/kernelFitBasic.m:138:        pvals(q,2) = signrank(xx); 
./reducedRankRegression/kernelFitBasic.m:142:        pvals(q,3) = signrank(xx);
./reducedRankRegression/kernelFitBasic.m:145:        [pvals(q,4),~,stat] = ranksum(mvRates(hasR(mTr),q), mvRates(hasL(mTr),q));
./reducedRankRegression/kernelFitBasic.m:147:        effectSizes(q,4) = stat.ranksum-nullRank; %positive value means that hasR is greater
./reducedRankRegression/kernelFitBasic.m:153:        pvals(q,5) = signrank(xx);
./reducedRankRegression/kernelFitBasic.m:156:        [pvals(q,6),~,stat] = ranksum(rewRates(:,q), bslRates(:,q));
./reducedRankRegression/kernelFitBasic.m:158:        effectSizes(q,6) = stat.ranksum-nullRank;
./reducedRankRegression/kernelFitBasic.m:161:            % the pval will be 'nan' from ranksum if all entries are zero
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent**

I could clone the paper's code (same commit, 9a0bea8). Now checking the code details the criteria cite.

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 100,200p reducedRankRegression/kernelFitBasic.m; ls; grep -rln "effectSizes" . | head
```

```
trRates = squeeze(mean(trRates,2));

trMeans = squeeze(mean(trRates))';

inclU = trMeans>0.1 & sp.cgs>1;

bslTimes = stimOn(inclT)+[-0.2:timeBinSize:0]; 
bslRates = interp1(tN, binnedSpikes, bslTimes);
bslRates = squeeze(mean(bslRates,2));

stimTimes = stimOn(inclT)+[0.05:timeBinSize:0.15]; 
stimRates = interp1(tN, binnedSpikes, stimTimes);
stimRates = squeeze(mean(stimRates,2));

mvTimes = moveTimeAbs(inclT&(hasLeftMove|hasRightMove))+[-0.1:timeBinSize:0.05]; 
mvRates = interp1(tN, binnedSpikes, mvTimes);
mvRates = squeeze(mean(mvRates,2));
mTr = (hasLeftMove|hasRightMove); mTr = mTr(inclT);
hasR = hasRightMove(inclT); hasL = hasLeftMove(inclT); 

[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -rn -i "increas\|decreas\|d'\|dprime" --include=*.m . | head -20; ls plotting behavior utils jPECC ccCP
```

```
./utils/iff.m:3:%   v = IFF(cond, evalTrue, evalFalse) returns 'evalTrue' if 'cond' is true,
./utils/brainRegionGroups.m:54:groups(g).acr = {'LP', 'LD', 'RT', 'MD', 'MG', 'LGd', 'VPM', 'VPL', 'PO', 'POL'};
./utils/brainRegionGroups.m:115:            g = g+1; groups(g).acr = {'LGd'}; groups(g).color = co(coIdx,:); coIdx = coIdx+1;
./utils/brainRegionGroups.m:117:            g = g+1; groups(g).acr = {'LD'}; groups(g).color = co(coIdx,:); coIdx = coIdx+1;
./utils/brainRegionGroups.m:119:            g = g+1; groups(g).acr = {'MD'}; groups(g).color = co(coIdx,:); coIdx = coIdx+1;
./utils/brainRegionGroups.m:252:            g = g+1; groups(g).acr = {'LGd'}; groups(g).color = co(coIdx,:); 
./utils/brainRegionGroups.m:254:            g = g+1; groups(g).acr = {'LD'}; groups(g).color = co(coIdx,:); %coIdx = coIdx+1;
./utils/brainRegionGroups.m:256:            g = g+1; groups(g).acr = {'MD'}; groups(g).color = co(coIdx,:); %coIdx = coIdx+1;
./utils/areaOrdering.m:9:            'VISa', 'LD','CP',      ...
./utils/areaOrdering.m:13:            'VPL', 'LGd', 'MD', 'PO', 'POL', 'MG', 'RT','VPM',  ...
./utils/areaOrdering.m:22:            'LD', 'POL', 'MD', 'VPL','PO', 'VPM', 'RT','MG', ...
./utils/areaOrdering.m:24:            'ZI', 'OLF', 'LS', 'BLA', 'LGd'}'; % non-responsive/other
./utils/areaOrdering.m:33:            'LGd', 'LP', 'LD', 'POL', 'MD', 'VPL', 'PO', 'VPM', 'RT', 'MG', ... thalamus
./reducedRankRegression/regFullPipeline.m:98:      cvp = cvpartition(max(trNum),'KFold',nfold);
./reducedRankRegression/regFullPipeline.m:200:    'allAcr', 'allCID', 'allPrbIdx', 'allR', '-v7.3');
./reducedRankRegression/regFullPipeline.m:283:[~, ii] = sort(ExKFitMx, 'descend');
./reducedRankRegression/regFullPipeline.m:313:    [mxSort, ii] = sort(ExKFitMx, 'descend');
./reducedRankRegression/predictResidualsWith.m:39:    r(n).cvp5 = cvpartition(max(r(n).trNum),'KFold',5);
./reducedRankRegression/predictResidualsWith.m:40:    r(n).cvp10 = cvpartition(max(r(n).trNum),'KFold',10);
./reduced
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 1,110p utils/brainRegionGroups.m
```

```
function groups = brainRegionGroups(style)

% co = get(gca, 'ColorOrder');
co = [         0    0.4470    0.7410;...
    0.8500    0.3250    0.0980;...
    0.9290    0.6940    0.1250;...
    0.4940    0.1840    0.5560;...
    0.4660    0.6740    0.1880;...
    0.3010    0.7450    0.9330;...
    0.6350    0.0780    0.1840;...
    [255 158 253]/255;... %pink
    0 0 0;...
    0.5*[1 1 1]];

% co = [55,126,184;...
%     228,26,28;...
%     77,175,74;...
%     152,78,163;...
%     0 0 0;...
%     0 0 0;...
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n -i "pca\|nPC\|lambda\|eye\|min(" jPECC/jPECC.m | head -20; grep -n "evalWin\|nComp\|1:50\|18\|75" reducedRankRegression/regFullPipeline.m | head -30
```

```
3:function [jPECC_val, jPECC_p] = jPECC(sp1, sp2, kfold, lambda, maxNpc)
4:% function [jPECC_val, jPECC_p] = jPECC(sp1, sp2, kfold, lambda)
12:% - lambda is a regularization parameter. Can leave it out and just use
14:% - maxNpc is the number of dimensions to keep from PCA analysis. Will keep
22:doPCA = true; % if false, just use what you're given
25:    maxNpc = 10; 
28:    lambda = [];     
39:nd = min([maxNpc size(sp1,3) size(sp2,3)]);
40:% nd = min([size(sp1,3) size(sp2,3)]);
45:    if doPCA        
46:        [~,Xs] = pca(X);
57:        if doPCA
58:            [~,Ys] = pca(Y);           
80:            if isempty(lambda)
87:                    [Xs(cvp.training(k),:); lambda*eye(nd); zeros(nd)],...
88:                    [Ys(cvp.training(k),:); zeros(nd); lambda*eye(nd)]);
82:nComp = 50;
101:    cvBS = zeros(size(bs,1), nComp);
120:            for nc = 1:nComp
144:    explVarAll = zeros(nComp,1); corrAll = zeros(nComp,1);
[... 5 more lines not kept]
```

**Agent**

Spot checks against the code mostly hold. I'm now applying the corrections.

**Agent calls Bash**

```bash
cd claims/000017 && python3 - <<'EOF'
p='10.1038-s41586-019-1787-x.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a,s.count(a))
    s=s.replace(a,b)
rep("""Table 1 and the figure legends. Both supplement files from the PMC Open Access data were read:
# supplement 1 (Supplementary Information guide, Supplementary Tables 1 and 2, legends of
# Supplementary Figs. 1 to 4) and supplement 2 (Supplementary Discussion and the same tables and
# legends).""","""Table 1 and the figure legends. Both supplement files from the PMC Open Access data were read:
# supplement 1 (the Supplementary Information guide only) and supplement 2 (Supplementary
# Discussion, Supplementary Tables 1 and 2, legends of Supplementary Figs. 1 to 4). The text file
# lacks Supplementary Table 1 (sex and genotype); it is read from the supplement 2 Word file, where
# each caption follows its table.""")
rep("""ANOVA nor the trials. Readings of the factors (F1) condition class (high-contrast single,
    low-contrast single, competing similar contrasts) and session; (F2) condition class and
    subject;""","""ANOVA nor the trials. Readings of the factors (F1) condition class (high-contrast single,
    low-contrast single, competing similar contrasts) and session; (F2) condition class and
    subject; (F3) contrast and presence of a competing stimulus (the variables of the Fig. 1d
    legend) and session, the condition effect being that of either factor;""")
rep("""  criterion: Per session, of trials whose recorded response is Left or Right, the percentage with
    the onset of a turn reaching 90 d.v.a. within 0.4 s of stimulus onset, and of those the
    percentage whose turn direction equals the recorded response; mean over the 39 sessions.
    Tolerances are the paper's s.d. over sessions. Reproduced when both are within tolerance.""","""  criterion: Per session, of trials whose recorded response is Left or Right, the percentage with
    a turn within 0.4 s of stimulus onset, and of those the percentage whose turn direction equals
    the recorded response; mean over the 39 sessions. The paper does not say what counts as
    "turning the wheel" here. Readings (a) the onset of a turn reaching 90 d.v.a. (the Left and
    Right Choice definition of the next sentence of the Methods); (b) any movement onset detected
    by findWheelMoves3, its direction that of the movement. Tolerances are the paper's s.d. over
    sessions. Reproduced when both are within tolerance under one reading.""")
rep("""is 60.0%, and Extended Data Table 1 sums to these). The direction of a significant test against
    baseline is the sign of the count of positive minus negative differences (code effectSizes).
    The paper does not define "consistently". Readings (a) every significant test against
    baseline (tests 1, 2, 3, 5, 6) has the same sign, test 4 being left out; (b) as (a) with test 6
    taken as a rank-sum, as the code does. Reproduced when all four values are within tolerance
    under one reading.""","""is 60.0%, and Extended Data Table 1 sums to these). The direction of a test against baseline is
    the sign of the code's effectSizes (kernelFitBasic.m); for the signrank tests 1, 2, 3 and 5 the
    count of positive minus negative trial differences, for the ranksum test 6 the rank sum of the
    post-reward rates minus its null value. Supplementary Fig. 1b counts a decrease as a higher
    baseline rate. The paper does not define "consistently". Readings (a) every test against
    baseline (1, 2, 3, 5, 6) with p below 0.05/6 has the same sign, test 4 being left out; (b) as
    (a) over the tests with p below 0.05. Reproduced when all four values are within tolerance
    under one reading.""")
rep("""being a bootstrap s.e. over neurons; (b) the mean ± s.e. of the six per-test d' values. d' is
    the difference of means over the root mean of the two variances.""","""being a bootstrap s.e. over neurons; (b) the mean ± s.e. of the six per-test d' values. d' is
    the difference of means over the root mean of the two variances, a standard choice; the paper
    does not define it.""")
rep("""sp/s). Responsive is open; readings (a) active during the task (definition N); (b) the Figs. 3
    to 5 set. The paper defines no latency.""","""sp/s). Responsive is open; readings (a) the display selection of the same Methods paragraph, a
    ranksum p < 0.0001 in at least three consecutive 0.1 s windows stepped by 0.005 s between task
    trials with stimuli and movements and those without both; (b) active during the task
    (definition N); (c) the Figs. 3 to 5 set. The paper defines no latency.""")
rep("""    SCs fall in the earliest quarter of regions, and on ipsilateral trials both fall in the latest
    third.""","""    SCs fall in the earliest quarter of regions, and on ipsilateral trials both fall in the latest
    third. The quarter and the third are this file's reading of "first" and "amongst the last".""")
rep("""    contralateral Miss trials. The thresholds are this file's reading of "failed to propagate
    globally" and "essentially no activity".
  depends_on:
  - fig5b-miss-more-than-passive
""","""    contralateral Miss trials. The thresholds are this file's reading of "failed to propagate
    globally" and "essentially no activity".
""")
rep("""    SNr, SCm, MRN, APN and ZI that is analysed has at least one such neuron. Partially reproduced
    when the first two hold only.""","""    SNr, SCm, MRN, APN and ZI that is analysed has at least one such neuron. The half and the five
    regions are this file's reading of "primarily" and "common". Partially reproduced when the
    first two hold only.""")
rep("""  criterion: F = sum of p_a squared over the square of the sum of p_a, p_a the fraction of neurons
    in region a requiring the kernel (kernel test K; Methods).""","""  criterion: F = sum of p_a squared over the square of the sum of p_a, p_a the fraction of neurons
    in region a requiring the kernel (kernel test K; Methods), over the 42 regions (the legend's
    floor of 0.0238 is 1/42).""")
rep("""  criterion: Kernel test K for the Choice kernel, as in fig3d-vision-localized. Higher-order
    thalamus is the thalamic regions other than LGd, VPL, VPM and MG.""","""  criterion: Kernel test K for the Choice kernel, as in fig3d-vision-localized. The paper does not
    define higher-order thalamus; this file reads it as the thalamic regions other than the
    first-order relays LGd, VPL, VPM and MG.""")
rep("""    ZI and one higher-order thalamic region has at least one, and the overall fraction of analysed
    neurons that are choice-selective is below 5%.""","""    ZI and one higher-order thalamic region has at least one, and the overall fraction of analysed
    neurons that are choice-selective is below 5% (this file's reading of "rare").""")
rep("""baseline + 1 sp/s; per group and time bin PCA to 10 dimensions (fewer if the group has fewer
    neurons);""","""baseline + 1 sp/s; per group and time bin PCA to 10 dimensions (fewer when either group has
    fewer neurons, the same number for both, jPECC.m);""")
rep("""  statement: Before the stimulus, neocortex and sensory thalamus were less active in the task than
    in the passive context, while basal ganglia and other subcortical choice areas were more
    active; VISp was lower and CP higher in the task.""","""  statement: Before the stimulus, neocortex and sensory thalamus were less active in the task than
    in the passive context, while basal ganglia and other subcortical choice areas were more
    active; VISp was lower and CP higher on Miss trials than on passive trials.""")
rep("""    0.0012 (0.05 over 42 regions). Reproduced when, under one reading, every differing neocortical
    region is lower in the task, every differing non-neocortical region other than visual thalamus
    (LGd, LP, LD) is higher, VISp differs and is lower, and CP differs and is higher.""","""    0.0012 (0.05 over 42 regions). VISp and CP are compared as in Fig. 5a, the mean pre-stimulus
    rate over neurons on contrast-matched (M) Miss trials against passive trials, windows as the
    readings of ed6b-prestimulus-order; the paper gives no test for them. Reproduced when, under
    one reading, every differing neocortical region is lower in the task, every differing
    non-neocortical region other than visual thalamus (LGd, LP, LD) is higher, VISp is lower on
    Miss than on passive trials, and CP is higher.""")
rep("""contralateral contrast > 0, (b) every contralateral contrast with a stimulus present.""","""contralateral contrast > 0 (as definition M), (b) all four contralateral contrast levels, zero
    included.""")
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  && cat >> claims/000017/10.1038-s41586-019-1787-x.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Opening comment. Said supplement 1 holds Supplementary Tables 1 and 2 and the legends; it holds only the Supplementary Information guide. Both tables and the legends are in supplement 2, and the sex and genotype table is only in its Word file.
  - fig1d-reaction-time-difficulty. Added factor reading F3, contrast and presence of a competing stimulus, the variables the Fig. 1d legend names.
  - early-response-fraction. The criterion took "turning the wheel within 400 ms" as the onset of a 90 d.v.a. turn; the paper does not say so. Named it open, with readings (a) that and (b) any detected movement onset.
  - task-modulated-fraction. The direction rule (count of positive minus negative differences) holds only for the signrank tests; for ranksum test 6 the code's effectSizes is the rank sum minus its null. Reading (b) ("test 6 taken as a rank-sum, as the code does") was the same as the Methods, which already make test 6 a ranksum; replaced by a reading at p < 0.05.
  - suppfig2-rate-amplitude. Said the d' formula is a standard choice; the paper does not define d'.
  - fig2de-activity-order. The Methods give a display selection of responsive neurons (ranksum p < 0.0001 in three consecutive sliding windows) in the paragraph that defines the normalization the criterion uses; added it as reading (a). Said the quarter and third thresholds are this file's reading.
  - fig2fg-miss-restricted. Removed depends_on fig5b-miss-more-than-passive; the criterion uses no result of that claim, only definitions M and R.
  - fig3d-vision-localized. Said the half and five-region thresholds are this file's reading of "primarily" and "common".
  - ed4f-focality. Said the index is taken over the 42 regions, as the legend's floor of 0.0238 (1/42) shows.
  - fig4b-choice-regions. Said the definition of higher-order thalamus and the 5% bound for "rare" are this file's readings; the paper gives neither.
  - fig4d-jpecc-vis-leads. jPECC.m keeps the same number of PCs for both groups, 10 or the smaller neuron count of the two; the criterion said per group.
  - fig5c-prestimulus-task-vs-passive. The criterion required VISp and CP to differ in the nested ANOVA; the paper states their difference for Miss against passive trials (Fig. 5a) with no test. Statement and criterion now compare contrast-matched Miss and passive means for these two regions.
  - fig5f-engagement-index. Contrast reading (b) ("every contralateral contrast with a stimulus present") did not differ from (a); now all four contralateral levels, zero included.
  - Open. fig4d-jpecc-vis-leads does not test the ~40 ms lag the Fig. 4d legend gives, and "at time points between -0.2 and -0.05 s" does not say how many points must be significant.
  - Open. fig4d-jpecc-no-lag-frontal-midbrain judges absence over -0.25 to 0 s from movement onset with an uncorrected t-test at each time point; the window is this file's choice and many uncorrected tests make a false positive likely.
  - Open. fig5d-go-miss-matches-task-passive uses a Pearson correlation across regions as its test; the paper gives none for Fig. 5d.
  - Open. No claim covers Extended Data Fig. 4c-e (activity detectable before movement onset in most regions, widespread activity after reward), a secondary finding.
EOF
python tools/claims_check.py claims/000017/10.1038-s41586-019-1787-x.yaml paper/10.1038-s41586-019-1787-x.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^checks:/,$p' claims/000017/10.1038-s41586-019-1787-x.yaml | grep -n '^  - .*: ' ; grep -c '—' claims/000017/10.1038-s41586-019-1787-x.yaml; grep -ci 'rather' claims/000017/10.1038-s41586-019-1787-x.yaml
```

```
0
0
```

**Agent**

**Checker result:** `claims/000017/10.1038-s41586-019-1787-x.yaml: 40 claims, 38 quotes, 11 statistical values, 0 problems`. I ran it before and after my edits and got the same result both times.

I checked the file against the paper text, the supplement 2 Word file (the subject table is only there) and the paper's code at commit 9a0bea8.

**Changes, by claim**
- **Opening comment:** it said supplement 1 holds Supplementary Tables 1 and 2 and the legends. It holds only the guide; the tables and legends are in supplement 2.
- **fig1d-reaction-time-difficulty:** added a third reading of the ANOVA factors: contrast and presence of a competing stimulus, the variables the Fig. 1d legend names.
- **early-response-fraction:** the paper does not say what counts as "turning the wheel within 400 ms". Named it open, with two readings: a 90 d.v.a. turn, or any detected movement onset.
- **task-modulated-fraction:** the rule for a test's direction was wrong for the ranksum test 6; it now follows the code. Reading (b) said "test 6 as a rank-sum, as the code does", but the Methods already make it a ranksum, so it was the same as (a). Replaced it with a reading at p < 0.05.
- **suppfig2-rate-amplitude:** said the d' formula is a standard choice; the paper does not define it.
- **fig2de-activity-order:** added the Methods' own rule for selecting responsive neurons for display as reading (a); the criterion had missed it. Said the quarter and third thresholds are the file's own reading.
- **fig2fg-miss-restricted:** removed `depends_on` fig5b-miss-more-than-passive; the criterion does not use that claim's result.
- **fig3d-vision-localized, fig4b-choice-regions:** said which thresholds and definitions (the half of neurons, the five top regions, "higher-order thalamus", the 5% bound for "rare") are the file's readings and not the paper's.
- **ed4f-focality:** said the index is taken over the 42 regions; the legend's floor of 0.0238 is 1/42.
- **fig4d-jpecc-vis-leads:** the number of principal components is the same for both groups (jPECC.m), not set per group.
- **fig5c-prestimulus-task-vs-passive:** the criterion required VISp and CP to pass the nested ANOVA. The paper only states their difference for Miss against passive trials (Fig. 5a), with no test. The statement and criterion now compare those means.
- **fig5f-engagement-index:** contrast reading (b) did not differ from (a); it now includes all four contralateral contrast levels, zero included.

**Still open** (recorded under `checks`)
- fig4d-jpecc-vis-leads does not test the ~40 ms lag, and does not say how many time points must be significant.
- fig4d-jpecc-no-lag-frontal-midbrain uses a time window the file chose, with uncorrected t-tests at each time point, so a false positive is likely.
- fig5d-go-miss-matches-task-passive uses a Pearson correlation as its test; the paper gives no test for Fig. 5d.
- No claim covers Extended Data Fig. 4c-e (activity before movement onset in most regions, activity after reward), a secondary finding.

**Ready:** yes (`ready: true`). Every main finding has a claim and every claim comes from this paper. Nothing was committed.

## End of run

25 turns, 3 minutes, result: success.
