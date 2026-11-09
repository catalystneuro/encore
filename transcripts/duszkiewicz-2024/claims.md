# 000939 · claims · run 39879051896

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/; ls claims/000939 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md | sed -n '40,400p'
```

```
reader check the statement against the paper without opening it. For a
     finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
     states it (numbers only in a table, a result spread over several
     legends), a short note under `inferred` saying so. The statement is
     then a reading of the paper, and the note says what it was
     read from.
   - `statistics`: the statistical support the paper reports for the
     finding, one entry per test or interval: what it compares (`about`,
     when there is more than one), the `test` and `statistic` as named, the
     `p`-value as a number (a bound such as "p < 0.05" is `p: 0.05` with
     `p_relation: "<"`; a printed "P = 0" is recorded as 0), any `corrected`
     for multiple comparisons, a confidence interval (`ci`), and `n` in
     words. It records the paper; the
     numbers the attempt must match, with tolerances, stay in `expected`.
     Record only tests whose result is the finding. A significance threshold
     used to select or count units, cells or pairs ("238 of 288 neurons were
     better fit, p < 0.05") is a method, not a result, and is left out.
     Leave the field out when the paper reports no test or interval for the
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la claims/001453/ paper/; ls claims/000939 2>&1
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

**Agent calls Bash**

```bash
wc -l paper/*.txt; head -c 3000 paper/*.txt; pdftotext -v 2>&1 | head -1
```

Result: not kept, because it reads the paper's text.

**Agent**

Let me read the full text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-024-01588-5.txt",
 "offset": 7,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)}' *.txt | sort -t: -k2 -n -r | head -20
```

```
7: 58973
34: 56119
16: 11456
46: 1077
92: 319
102: 309
174: 302
106: 260
122: 257
136: 250
168: 247
142: 246
118: 239
54: 232
120: 227
170: 226
110: 226
138: 224
132: 224
90: 222
```

**Agent calls Bash**

```bash
cd paper; sed -n 7p *.txt | fold -s -w 4000 | sed -n '1,8p'
```

```
<persisted-output>
Output too large (31.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5decd2e7-46f5-4ec3-80a2-3a72d97be870/tool-results/bc112y8p6.txt

Preview (first 2KB):
pmc Nat Neurosci Nat Neurosci 981 npgopen 9809671 Nature Neuroscience 1097-6256 1546-1726 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC11001581 PMC11001581.1 11001581 11001581 38491324 10.1038/s41593-024-01588-5 1588 1 Article Local origin of excitatory–inhibitory tuning equivalence in a cortical network Duszkiewicz Adrian J. [removed: an e-mail address] 1 2 3 http://orcid.org/0000-0003-1094-266X Orhan Pierre 1 4 Skromne Carrasco Sofia 1 http://orcid.org/0000-0001-9564-9213 Brown Eleanor H. 1 Owczarek Eliott 1 Vite Gilberto R. 1 Wood Emma R. 2 5 http://orcid.org/0000-0001-9708-309X Peyrache Adrien [removed: an e-mail address] 1 1 https://ror.org/01pxwe438 grid.14709.3b 0000 0004 1936 8649 Montreal Neurological Institute and Hospital, McGill University, Montreal, Quebec Canada 2 https://ror.org/01nrxwf90 grid.4305.2 0000 0004 1936 7988 Centre for Discovery Brain Sciences, University of Edinburgh, Edinburgh, UK 3 https://ror.org/045wgfr59 grid.11918.30 0000 0001 2248 4331 Department of Psychology, University of Stirling, Stirling, UK 4 https://ror.org/013cjyk83 grid.440907.e 0000 0004 1784 3645 Ecole normale supérieure, PSL University, CNRS, Paris, France 5 https://ror.org/01nrxwf90 grid.4305.2 0000 0004 1936 7988 Simons Initiative for the Developing Brain, University of Edinburgh, Edinburgh, UK 15 3 2024 2024 27 4 459642 782 792 12 12 2022 24 1 2024 15 03 2024 10 04 2024 14 03 2026 © The Author(s) 2024 2024 https://creativecommons.org/licenses/by/4.0/ Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; fold -s -w 250 *.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

```
1528 /tmp/claude-1001/p.txt
/tmp/claude-1001
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 1,
 "limit": 260
}
```

```
1	DOI: 10.1038/s41593-024-01588-5
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 2 supplement file(s) from the PMC Open Access cloud data (PMC11001581), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	pmc Nat Neurosci Nat Neurosci 981 npgopen 9809671 Nature Neuroscience 1097-6256 1546-1726 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC11001581 PMC11001581.1 11001581 11001581 38491324 10.1038/s41593-024-01588-5 1588 1 
8	Article Local origin of excitatory–inhibitory tuning equivalence in a cortical network Duszkiewicz Adrian J. [removed: an e-mail address] 1 2 3 http://orcid.org/0000-0003-1094-266X Orhan Pierre 1 4 Skromne Carrasco Sofia 1 http://orcid.org/0000-0001-9564-9213 
9	Brown Eleanor H. 1 Owczarek Eliott 1 Vite Gilberto R. 1 Wood Emma R. 2 5 http://orcid.org/0000-0001-9708-309X Peyrache Adrien [removed: an e-mail address] 1 1 https://ror.org/01pxwe438 grid.14709.3b 0000 0004 1936 8649 Montreal Neurological Institute 
10	and Hospital, McGill University, Montreal, Quebec Canada 2 https://ror.org/01nrxwf90 grid.4305.2 0000 0004 1936 7988 Centre for Discovery Brain Sciences, University of Edinburgh, Edinburgh, UK 3 https://ror.org/045wgfr59 grid.11918.30 0000 0001 2248 
11	4331 Department of Psychology, University of Stirling, Stirling, UK 4 https://ror.org/013cjyk83 grid.440907.e 0000 0004 1784 3645 Ecole normale supérieure, PSL University, CNRS, Paris, France 5 https://ror.org/01nrxwf90 grid.4305.2 0000 0004 1936 
12	7988 Simons Initiative for the Developing Brain, University of Edinburgh, Edinburgh, UK 15 3 2024 2024 27 4 459642 782 792 12 12 2022 24 1 2024 15 03 2024 10 04 2024 14 03 2026 © The Author(s) 2024 2024 https://creativecommons.org/licenses/by/4.0/ 
13	Open Access This article is licensed under a Creative Commons Attribution 4.0 International Licen
[... 247 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 260,
 "limit": 260
}
```

```
260	Cross-validated HD tuning curve auto-correlograms and cross-correlograms We obtained HD tuning curve auto-correlogram and cross-correlogram by computing Pearson’s correlation coefficients between the reference tuning curve vector and the second 
261	tuning curve vector (from either the same or another cell), which was circularly shifted by 0–359 bins. To minimize the effect of non-HD factors on tuning curves computed from the same epoch, we used a cross-validation procedure whereby the two 
262	tuning curves were computed from separate halves of the epoch. When computing HD tuning curves during the exploration of the triangular open field, we noticed that sometimes the cells’ receptive fields were rotated with respect to the prior square 
263	open-field exploration. To correct for this, we first calculated for each HD cell the degree of tuning curve rotation between the two environments via cross-correlation. We then used the average rotation per recording session to circularly shift all 
264	triangular open-field tuning curves in the opposite direction by the equivalent amount. This allowed us to compute the true tuning curve correlation between the two environments. Detection of monosynaptic connections Spike train cross-correlograms 
265	of ±50 ms binned in 0.2-ms windows were convolved with a Gaussian kernel of 4 ms s.d, resulting in a predictor of the baseline rate. At each time bin, the 99th percentile of the cumulative Poisson distribution (at the predicted rate) was used at the 
266	statistical threshold for significant detection of outliers from baseline. A putative connection was considered significant when at least two consecutive bins in the cross-correlograms passed the statistical test. Analysis of HD cell realignment 
267	after cue rotation To estimate the degree of realignment of the HD system following cue rotation, HD cell spike times were binned into population vectors (50 ms window, smoothed in 100 ms s.d. Gaussian windows). Based on cells’ t
[... 252 more lines not kept]
```

**Agent**

Main text and Methods read. Now locating the supplement text.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "supplement|^=+|----" $TMPDIR/p.txt | awk -F: '$1>519' | head -20; awk 'NR>7{print NR": "substr($0,1,300)}' *.txt | grep -v '^\s*$' | awk 'length>8' | head -40
```

```
704:##### Supplement: 41593_2024_1588_MOESM1_ESM.pdf
706:=== page 1 ===
715:=== page 2 ===
716:Supplementary Methods 
777:=== page 3 ===
799:=(w;, −μ;)-w;( −μ;.
852:=== page 4 ===
921:=== page 5 ===
931:=  
988:=== page 6 ===
1030:= 0 
1040:=== page 7 ===
1091:= =(u,C −1)-
1094:= n−2 T= u,C
1102:= ε,C(n)-
1105:= n− 2 T= u,C
1117:= O(1) 
1124:= ε,C(n)-
1127:= n+ O(1). 
1129:=== page 8 ===
[... 40 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 700,
 "limit": 160
}
```

```
700	[66] Levenstein, D., Buzsáki, G. & Rinzel, J. NREM sleep in the rodent neocortex and hippocampus reflects excitable dynamics. Nat. Commun. 10, 2478 (2019). 10.1038/s41467-019-10327-5
701	
702	[67] Berens, P. CircStat: a MATLAB toolbox for circular statistics. J. Stat. Softw. 31, 1–21 (2009). 10.18637/jss.v031.i10
703	
704	##### Supplement: 41593_2024_1588_MOESM1_ESM.pdf
705	
706	=== page 1 ===
707	nature neuroscience
708	https://doi.org/10.1038/s41593-024-01588-5
709	Article
710	Local origin of excitatory–inhibitory tuning 
711	equivalence in a cortical network
712	In the format provided by the 
713	authors and unedited
714	
715	=== page 2 ===
716	Supplementary Methods 
717	 
718	Fourier spectrum simulations – Model fitting 
719	We aim to derive network parameters based on the statistics of observed tuning curves in FS cells. 
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "##### Supplement" $TMPDIR/p.txt; sed -n '1180,1528p' $TMPDIR/p.txt | grep -v '^\s*$' | cut -c1-200 | head -150
```

```
704:##### Supplement: 41593_2024_1588_MOESM1_ESM.pdf
1320:##### Supplement: 41593_2024_1588_MOESM2_ESM.pdf
0
T.HU(0):
-HI
∑
ε,C(n)-HI
.
,/0
→.→D 0 i.e   ∑
ε,C(n)-HI
.
,/0
= o7n0H,
-: 
Note: Let us show that assumption 2 holds for von Mises tuning curve: 
ε,C(n) = 1 −cos 1
-X,
. l2  
The sum 
[... 132 more lines not kept]
```

**Agent**

The full text, Methods, Extended Data legends, Supplementary Methods and reporting summary are all present. Next, the code (figshare 10.6084/m9.figshare.24921252) and the dataset's description.

**Agent calls Bash**

```bash
cd  curl -s -m 30 https://api.figshare.com/v2/articles/24921252 | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('title'),d.get('version'),d.get('published_date'));print(d.get('description')[:3000]);[print(f['name'],f['size'],f['download_url']) for f in d['files']]"; curl -s -m 30 https://api.dandiarchive.org/api/dandisets/000939/ | python -c "import json,sys;d=json.load(sys.stdin);print(d)"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  curl -s -m 30 https://api.figshare.com/v2/articles/24921252 | python -c "import json,sys,re;d=json.load(sys.stdin);print(re.sub('<[^>]+>',' ',d.get('description'))[2500:])"; curl -s -m 30 https://api.dandiarchive.org/api/dandisets/000939/versions/0.261016.2310/info/ | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('description'));print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/code && cd $TMPDIR/code && curl -sL -m 120 -o code.zip https://ndownloader.figshare.com/files/43857246 && curl -sL -m 60 -o sl.zip https://ndownloader.figshare.com/files/43857237 && unzip -q -o code.zip && unzip -q -o sl.zip && find . -type f | grep -v -i '__MACOSX' | head -200; md5sum code.zip sl.zip
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code; find . -type f -name '*.m' ! -name '._*' | grep -v Dependencies | sort; for f in ListFiles/*.list; do echo "$f $(wc -l <$f)"; done; head -40 ListFiles/dataset_All.list
```

```
./Code/Analysis/Duszkiewicz2024_Figure_AnticipatoryFiring.m
./Code/Analysis/Duszkiewicz2024_Figure_BasicProperties.m
./Code/Analysis/Duszkiewicz2024_Figure_CueRotation.m
./Code/Analysis/Duszkiewicz2024_Figure_Fourier.m
./Code/Analysis/Duszkiewicz2024_Figure_GLMRemWake.m
./Code/Analysis/Duszkiewicz2024_Figure_GainSimulation.m
./Code/Analysis/Duszkiewicz2024_Figure_IsomapREM.m
./Code/Analysis/Duszkiewicz2024_Figure_IsomapWake.m
./Code/Analysis/Duszkiewicz2024_Figure_Optogenetics.m
./Code/Analysis/Duszkiewicz2024_Figure_SingleRec_Angled.m
./Code/Analysis/Duszkiewicz2024_Figure_SingleRec_CueRotation.m
./Code/Analysis/Duszkiewicz2024_Figure_SingleRec_Decoding.m
./Code/Analysis/Duszkiewicz2024_Figure_SingleRec_IsomapREM.m
./Code/Analysis/Duszkiewicz2024_Figure_SingleRec_IsomapRaster.m
./Code/Analysis/Duszkiewicz2024_Figure_SingleRec_IsomapWake.m
./Code/Analysis/Duszkiewicz2024_Figure_SingleRec_LFP.m
./Code/Analysis/Duszkiewicz2024_Figure_SingleRec_NPX.m
./Code/Analysis/Duszkiewicz2024_Figure_SingleRec_Vertical.m
./Code/Analysis/Duszkiewicz2024_Figure_Stability.m
./Code/Analysis/Duszkiewicz2024_Figure_SynapticConnections.m
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; wc -l [!.]*.m | sort -n | tail -50; cat Duszkiewicz2024_GetCellTypes_PoSub.m
```

```
12 Duszkiewicz2024_GetClusterQualityScore.m
    15 Duszkiewicz2024_GetSynapticPairs.m
    28 Duszkiewicz2024_GetCueEpochs_CueRotation.m
    28 Duszkiewicz2024_GetSpikeAutocorrs.m
    28 Duszkiewicz2024_GetTuningCurveCrosscorrs.m
    29 Duszkiewicz2024_GetMeanRates.m
    30 Duszkiewicz2024_GetCellTypes_ADN.m
    37 Duszkiewicz2024_GetSpikeCrosscorrs.m
    38 Duszkiewicz2024_GetCellTypes_PoSub.m
    45 Duszkiewicz2024_GetTuningAutocorr_xval.m
    61 Duszkiewicz2024_GetBayesianDecoding_CueRotation.m
    90 Duszkiewicz2024_GetAnticipatoryTuning.m
    98 Duszkiewicz2024_GetBayesianDecoding.m
   124 Duszkiewicz2024_GetHdTuning_xval.m
   145 Duszkiewicz2024_GetWaveformFeatures.m
   160 Duszkiewicz2024_Figure_SingleRec_Decoding.m
   162 Duszkiewicz2024_GetHdTuning.m
   227 Duszkiewicz2024_Figure_SingleRec_LFP.m
   262 Duszkiewicz2024_Figure_SingleRec_NPX.m
   271 Duszkiewicz2024_Figure_AnticipatoryFiring.m
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; cat Duszkiewicz2024_GetMeanRates.m Duszkiewicz2024_GetHdTuning.m; sed -n 1,145p Duszkiewicz2024_GetWaveformFeatures.m | grep -n -i -E "tr2pk|neg|nan|max|min" | head -30
```

```
getREM = 0;

load(fullfile('Data','BehavEpochs'));
load(fullfile('Data','SpikeData'),'S');
[~, foldername, ~] = fileparts(pwd);

if getREM == 1    
    load(fullfile('Sleep',[foldername '.SleepState.states.mat'] ));
    % get REM episodes
    rem = SleepState.ints.REMstate;
    remDur = sum(rem(:,2) - rem(:,1));
    epRem = intervalSet(rem(:,1),rem(:,2));
    rateREM = Rate(S,epRem); 
else
    rateREM = nan(length(S),1);
end
% calculate mean wake FR

% rate in square 
epS = wake1Ep;
[... 200 more lines not kept]
```

**Agent**

Code read so far: cell typing uses trough-to-peak 0.35 ms where the Methods say 0.4 ms (a variant to record). Now the figure scripts' statistics.

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; grep -n -E "signrank|ranksum|anova|corr\(|ttest|kruskal|multcompare|bonf|prctile|isomap|compute_mapping" Duszkiewicz2024_Figure_BasicProperties.m Duszkiewicz2024_Figure_Stability.m | head -60; sed -n 1,80p Duszkiewicz2024_Figure_BasicProperties.m
```

```
Duszkiewicz2024_Figure_BasicProperties.m:311:    [p,h,stats] = signrank(vbl1,vbl2);
Duszkiewicz2024_Figure_BasicProperties.m:359:    [p,h,stats] = signrank(vbl1,vbl2);
Duszkiewicz2024_Figure_BasicProperties.m:418:    [r,p] = corr(vbl1,vbl2,'type','Pearson');
Duszkiewicz2024_Figure_BasicProperties.m:494:    [r,p] = corr(vbl1,vbl2,'type','Spearman');
Duszkiewicz2024_Figure_Stability.m:119:    cc = TCcrosscorr(tc1,tc2); 
Duszkiewicz2024_Figure_Stability.m:127:    cc = TCcrosscorr(tc1,tc2); 
Duszkiewicz2024_Figure_Stability.m:142:    cc = TCcrosscorr(tc1,tc2); 
Duszkiewicz2024_Figure_Stability.m:150:    cc = TCcrosscorr(tc1,tc2); 
Duszkiewicz2024_Figure_Stability.m:210:        cc = TCcrosscorr(tc1,tc2); 
Duszkiewicz2024_Figure_Stability.m:215:        cc = TCcrosscorr(tc1,tc2); 
Duszkiewicz2024_Figure_Stability.m:285:% via https://uk.mathworks.com/matlabcentral/answers/124353-does-fitrm-ranova-support-within-subject-models-without-between-subject-factors
Duszkiewicz2024_Figure_Stability.m:296:    anTbl12 = ranova(rm,'WithinModel','a*b-1');
Duszkiewicz2024_Figure_Stability.m:307:    anTblST = ranova(rm,'WithinModel','a*b-1');
Duszkiewicz2024_Figure_Stability.m:369:    [p,h,stats] = signrank(vbl1,vbl2);
Duszkiewicz2024_Figure_Stability.m:417:    [p,h,stats] = signrank(vbl1,vbl2);
Duszkiewicz2024_Figure_Stability.m:449:    cc = TCcrosscorr(tc1,tc2);
Duszkiewicz2024_Figure_Stability.m:510:    [p,h,stats] = signrank(vbl1,vbl2);
Duszkiewicz2024_Figure_Stability.m:556:    [p,h,stats] = signrank(vbl1,vbl2);
Duszkiewicz2024_Figure_Stability.m:588:    cc = TCcrosscorr(tc1,tc2);
function Duszkiewicz2024_Figure_BasicProperties
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; sed -n 80,523p Duszkiewicz2024_Figure_BasicProperties.m | grep -v '^\s*$' | grep -v -E "^\s*(set|xlabel|ylabel|title|box|axis|xlim|ylim|hold|plot|subplot|figure|colormap|caxis|xticks|yticks|xticklabels|yticklabels|line|text|legend|bar|histogram|scatter|errorbar|fill|area|patch|%)" | head -200
```

```
medianErrFS = [medianErrFS; medianErrorFS];
    medianErrFS_sh = [medianErrFS_sh; medianErrorFS_sh];
    totHD = [totHD; sum(hd)];
    totFS = [totFS; sum(fs)];
    edges = -180:5:180;
    bins = edges(1:end-1)+median(diff(edges))/2;
    counts = histcounts(rad2deg(Data(decErr_HD)),edges); %
    errHistHD = [errHistHD counts'];    
    counts = histcounts(rad2deg(Data(decErr_FS)),edges); %
    errHistFS = [errHistFS counts'];    
end
totC = length(isFs); % total cells
ixGd = find(isGd == 1);
ixHd = find(isHd == 1 & isGd == 1);
ixFs = find(isFs == 1 & isGd == 1);
ixEx = find(isEx == 1 & isGd == 1);
vbl_ex = sort(hdi_sh(ixEx));
thr_ex = round(0.99*length(vbl_ex));
thr_ex = vbl_ex(thr_ex+1);
thr_ex = log10(round(thr_ex,1));
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; sed -n 370,523p Duszkiewicz2024_Figure_BasicProperties.m | grep -n -E "vbl|corr|median|mean|errHist|modIndex" | head -40; grep -v '^\s*%' Duszkiewicz2024_GetBayesianDecoding.m | grep -v '^\s*$' | head -100
```

```
28:    vbl1 = totHD;
29:    vbl2 = medianErrHD;
30:    ax = scatter(vbl1,vbl2);
35:    vbl1 = totFS;
36:    vbl2 = medianErrFS;
37:    ax = scatter(vbl1,vbl2);
42:    vbl = mean(medianErrFS_sh);
43:    ax = plot([0 120],[vbl vbl],':');
49:    [r,p] = corr(vbl1,vbl2,'type','Pearson');
64:    vbl1 = modIndex(ixFs)*100;
65:    m1 = median(vbl1);
66:    h1 = histogram(vbl1);
92:    vbl1 = totFS;
93:    vbl2 = medianErrFS;
94:    ax = scatter(vbl1,vbl2);
99:    vbl = mean(medianErrFS_sh);
100:    ax = plot([0 120],[vbl vbl],':');
104:    vbl = mean(medianErrHD);
105:    ax = plot([0 120],[vbl vbl],':');
109:    Fit = polyfit(vbl1,vbl2,1);
[... 73 more lines not kept]
```

**Agent**

Decoding method is fixed only by the code (train on first half of the square epoch, test on second, 100 ms bins). Now the Fourier script, the core of the paper.

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; grep -v '^\s*$' Duszkiewicz2024_Figure_Fourier.m | grep -v -E "^\s*(set|xlabel|ylabel|title|box|axis|xlim|ylim|hold|plot|subplot|figure|colormap|caxis|xticks|yticks|xticklabels|yticklabels|line|text|legend|bar|histogram|scatter|errorbar|fill|area|patch|ax\.|h[0-9]\.|ax =|nexttile|tiledlayout)" | sed -n 1,260p
```

```
function Duszkiewicz2024_Figure_Fourier
% This script reporoduces panels from:
% Figure 3, Extended Data Figures 3 and 4
% Dependencies: 
% TStoolbox
% CircStat
% Matlab Toolbox for DImensionality Reduction 
%TODO: script dependencies, links to external functions
% Copyright (C) 2023 by Adrian Duszkiewicz and Adrien Peyrache
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 2 of the License, or
% (at your option) any later version.
%% Parameters
clear all 
smoothTC = 3; % smoothing of tuning curves (3 used in Duszkiewicz et al., 2024)
noComps = 10; % total number of Fourier components used
saveTC = 0; % 1 to save tuning curves
onlyGoodClusters = 0; % 1 to limit to good clusters
[... 241 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; grep -n -E "offFR|cqSc|ranksum|signrank|KLDiv|circ_corrcc|compute_mapping|isomap|ftDist|velTh|highComp" Duszkiewicz2024_Figure_Fourier.m | sed -n 1,200p; find $TMPDIR/code -name 'KLDiv*' ! -name '._*'; grep -c . $TMPDIR/code/ListFiles/dataset_All_FT.list; sed -n 30,50p $TMPDIR/code/ListFiles/dataset_All_FT.list
```

```
56:cqSc = [];
80:    cqSc = [cqSc; cqs];
119:offFR = nan(totC,1);
124:        offFR(nC) = mean(tcAllN(tcWidth(nC):end-tcWidth(nC),nC),1);
133:    isHd = isHd & cqSc < 0.2;
134:    isFs = isFs & cqSc < 0.2;
135:    isGd = isGd & cqSc < 0.2;
139:isHd =  isHd & offFR < 0.05;
185:[~,highComp] = max(ftN(1:3,:)',[],2);
188:ftDistFS = nan(totC,1);
198:    ftDistFS(nC) = sqrt(ftd);
203:ftDist = nan(totC,1); 
211:    ftDist(ix(nC)) = sqrt(ftd);
220:    ftDist(ix(nC)) = sqrt(ftd);
229:    ftDist(ix(nC)) = sqrt(ftd);
235:ftDistFsKL = nan(totC,1);
237:ftDistFsKL(ixHd) = KLDiv(repmat(meanFtFS',length(ixHd),1),ftN(:,ixHd)');
239:ftDistKL = nan(totC,1);
240:ftDistKL(ixFs) = KLDiv(repmat(meanFtFS',length(ixFs),1),ftN(:,ixFs)');
241:ftDistKL(find(isHd & isPos)) = KLDiv(repmat(meanFtPos',length(find(isHd & isPos)),1),ftN(:,find(isHd & isPos))');
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code; grep -v '^\s*%' Dependencies/TSToolbox_Utils/Stats/KLDiv.m | grep -v '^\s*$'; sed -n 455,530p Analysis/Duszkiewicz2024_Figure_Fourier.m | grep -v -E "^\s*(ax|h[0-9])"; sed -n 1395,1410p Analysis/Duszkiewicz2024_Figure_Fourier.m; head -30 $TMPDIR/code/ListFiles/dataset_All_FT.list | tr '\n' ' '
```

```
function dist=KLDiv(P,Q)
if size(P,2)~=size(Q,2)
    error('the number of columns in P and Q should be the same');
end
if sum(~isfinite(P(:))) + sum(~isfinite(Q(:)))
   error('the inputs contain non-finite values!') 
end
if size(Q,1)==1
    Q = Q ./sum(Q);
    P = P ./repmat(sum(P,2),[1 size(P,2)]);
    temp =  P.*log(P./repmat(Q,[size(P,1) 1]));
    temp(isnan(temp))=0;% resolving the case when P(i)==0
    dist = sum(temp,2);
elseif size(Q,1)==size(P,1)
    Q = Q ./repmat(sum(Q,2),[1 size(Q,2)]);
    P = P ./repmat(sum(P,2),[1 size(P,2)]);
    temp =  P.*log(P./Q);
    temp(isnan(temp))=0; % resolving the case when P(i)==0
    dist = sum(temp,2);
end
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; grep -v '^\s*%' Duszkiewicz2024_GetTuningAutocorr_xval.m | grep -v '^\s*$'; sed -n 1,60p Duszkiewicz2024_GetHdTuning_xval.m | grep -v '^\s*%' | grep -v '^\s*$' | head -50
```

```
load(fullfile('Analysis','HDtuning_xval_moveEp'));
hAllA = hAll1;
hAllB = hAll2;
hAllA_sh = hAll1_sh;
hAllB_sh = hAll2_sh;
[totBins,totC,totTh] = size(hAllA);
ac = nan(size(hAllA));
for nTh = 1:totTh 
    h1 = zscore(hAllA(:,:,nTh));
    h2 = zscore(hAllB(:,:,nTh));
    for n = 0:size(ac,1)-1
        hs = circshift(h2,n);
        ac(n+1,:,nTh) = diag(h1' * hs);
    end
end
acAll = ac / (size(ac,1)-1);
ac_sh = nan(size(hAllA));
for nTh = 1:totTh 
    h1 = zscore(hAllA_sh(:,:,nTh));
    h2 = zscore(hAllB_sh(:,:,nTh));
[... 35 more lines not kept]
```

**Agent**

Found a second code/Methods disagreement: the code's KL divergence runs D_KL(S‖σ_i), the reverse of the direction the Methods give. Now the Stability, GLM, Isomap, opto and synaptic scripts.

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; f=Duszkiewicz2024_Figure_Stability.m; grep -v '^\s*$' $f | grep -v -E "^\s*(%|set|xlabel|ylabel|title|box|axis|xlim|ylim|hold|plot|subplot|figure|colormap|xticks|yticks|line|text|legend|bar|histogram|scatter|ax\.|h[0-9]\.|ax =|nexttile|tiledlayout|mx[0-9]|m[0-9] =)" | sed -n 1,140p
```

```
function Duszkiewicz2024_Figure_Stability
clear all
goodSpk = [];
spw = [];
tpk = [];
hpw = [];
frateS = [];
frateT = [];
hdi = [];
hdi1 = [];
hdi2 = [];
hdiT = [];
isHd = [];
isFs = [];
isGd = [];
isTri = [];
isTriRec = [];
whichRec = [];
tcAll1 = [];
tcAll2 = [];
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; f=Duszkiewicz2024_Figure_Stability.m; sed -n 300,600p $f | grep -n -E "vbl[0-9]? =|signrank|ranova|cc[A-Za-z_]*\(|max\(" | head -50; grep -v '^\s*%' TCcrosscorr.m 2>/dev/null || find $TMPDIR/code -name 'TCcrosscorr.m' ! -name '._*' -exec cat {} \;
```

```
8:    anTblST = ranova(rm,'WithinModel','a*b-1');
34:    vbl1 = corrST(ix); 
35:    vbl2 = zeroST_rev(ix); 
70:    [p,h,stats] = signrank(vbl1,vbl2);
78:    vbl1 = corrST(ix); 
79:    vbl2 = zeroST_rev(ix); 
118:    [p,h,stats] = signrank(vbl1,vbl2);
155:    [~,maxIx] = max(cc);
174:    vbl1 = corrHH(ixHd); 
175:    vbl2 = zeroHH_rev(ixHd);
211:    [p,h,stats] = signrank(vbl1,vbl2);
217:    vbl1 = corrHH(ixFs); 
218:    vbl2 = zeroHH_rev(ixFs); 
257:    [p,h,stats] = signrank(vbl1,vbl2);
294:    [~,maxIx] = max(cc);
function ac = TCcrosscorr(h1,h2)

if rem(h1,2) == 1 % if odd number of bins then make even
    h1 = h1(1:end-1);
end
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; f=Duszkiewicz2024_Figure_Stability.m; grep -n -E "corrST|zeroST_rev|corrHH|zeroHH_rev|ix = " $f | head -30
```

```
175:        ix = ixC(ismember(ixC,ixR)); 
188:        ix = ixC(ismember(ixC,ixR));        
230:corrHH = ccHH(1,:);
231:corrST = ccST(1,:);
233:zeroHH_rev = ccHH_sh(1,:);
234:zeroST_rev = ccST_sh(1,:);
332:    ix = ixHdT;
333:    vbl1 = corrST(ix); 
334:    vbl2 = zeroST_rev(ix); 
376:    ix = ixFsT;
377:    vbl1 = corrST(ix); 
378:    vbl2 = zeroST_rev(ix); 
422:    ix = ixFsT;
473:    vbl1 = corrHH(ixHd); 
474:    vbl2 = zeroHH_rev(ixHd);
516:    vbl1 = corrHH(ixFs); 
517:    vbl2 = zeroHH_rev(ixFs); 
561:    ix = ixFsT;
612:    ix = find(isFs);
638:    ix = ixFsT;
[... 1 more lines not kept]
```

**Agent**

Stability tests are settled: zero-lag tuning correlation against the time-reversed control, Wilcoxon signed-rank. Now GLM (Fig. 6).

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; f=Duszkiewicz2024_Figure_GLMRemWake.m; grep -v '^\s*$' $f | grep -v -E "^\s*(%|set|xlabel|ylabel|title|box|axis|xlim|ylim|hold|plot|subplot|figure|colormap|caxis|xticks|yticks|line|text|legend|bar|histogram|scatter|imagesc|ax\.|h[0-9]\.|ax =|nexttile|tiledlayout|mx[0-9]|m[0-9] =)" | sed -n 1,200p
```

```
function Duszkiewicz2024_Figure_GLMRemWake
clear all 
smoothTC = 3; % smoothing of tuning curves (3 used in Duszkiewicz et al., 2024)
isHd = [];
isFs = [];
isGd = [];
isEx = [];
tcAll = [];
ccAll = [];
pairsTc = [];
pairsGlm = [];
rateWk = [];
rateRem = [];
betaRem = [];
betaWake = [];
warnRem = [];
warnWake = [];
remDur = [];
pairsGlm_rev = [];
betaRem_rev = [];
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; f=Duszkiewicz2024_Figure_GLMRemWake.m; grep -n -E "corr\(|signrank|ranksum|mid|polyfit" $f | head -30; grep -v '^\s*%' Duszkiewicz2024_GetGLM_Forward.m | grep -v '^\s*$' | sed -n 1,90p
```

```
200:    mid = round(size(betaWake,1)./2);
503:    mid = round(size(betaWake,1)./2);
504:    vbl1 = betaWake(mid,ix);       
505:    vbl2 = betaRem(mid,ix);          
510:    Fit = polyfit(vbl1,vbl2,1);
524:    [r,p] = corr(vbl1',vbl2','type','Pearson');
536:    mid = round(size(betaWake,1)./2);
537:    vbl1 = betaWake(mid,ix);       
538:    vbl2 = betaRem(mid,ix);          
543:    Fit = polyfit(vbl1,vbl2,1);
561:    [r,p] = corr(vbl1',vbl2','type','Pearson');
568:    mid = round(size(betaWake,1)./2);
569:    vbl1 = betaWake(mid,ix);       
570:    vbl2 = betaRem(mid,ix);          
575:    Fit = polyfit(vbl1,vbl2,1);
588:    [r,p] = corr(vbl1',vbl2','type','Pearson');
612:    mid = round(size(betaWake,1)./2);
613:    vbl2 = betaWake(mid,ix);
619:    Fit = polyfit(vbl1,vbl2,1);
635:    [r,p] = corr(vbl1',vbl2','type','Pearson');
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/ListFiles; for f in *.list; do echo "$f $(grep -c . $f)"; done; cd ../Code/Analysis; for f in Duszkiewicz2024_Figure_IsomapWake.m Duszkiewicz2024_Figure_IsomapREM.m; do echo "== $f"; grep -n -E "List2Cell|signrank|ranksum|corr\(|ix[A-Za-z]* = find|rate|remDur|>= *100|TCcrosscorr|smoothTC|ccg|\(1,:\)" $f | head -40; done
```

```
dataset_All.list 32
dataset_All_FT.list 51
dataset_All_Rem.list 28
dataset_Opto.list 21
dataset_Stability.list 19
dataset_cuerot.list 7
== Duszkiewicz2024_Figure_IsomapWake.m
36:dataset = List2Cell('dataset_All.list');
89:ixGd = find(isGd == 1);
92:ixEx = find(isEx == 1);
95:ixHd = find(isHd == 1);
98:ixFs = find(isFs == 1);
107:    ixR = find(whichRec == nR); 
113:        cc = TCcrosscorr(tcReal(:,ix(nC)),tcWake(:,ix(nC))); % xcorr between two tuning curves
116:        cc = TCcrosscorr(tcReal(:,ix(nC)),tcRv(:,ix(nC))); % xcorr between two tuning curves
127:    ixR = find(whichRec == nR); 
133:        cc = TCcrosscorr(tcRealSh(:,ix(nC)),tcWakeSh(:,ix(nC))); % xcorr between two tuning curves
136:        cc = TCcrosscorr(tcRealSh(:,ix(nC)),tcRvSh(:,ix(nC))); % xcorr between two tuning curves
152:    cc_RlWk(:,nC) = TCcrosscorr(tcReal(:,nC),tcWake(:,nC)); 
153:    cc_RlRv(:,nC) = TCcrosscorr(tcReal(:,nC),tcRv(:,nC)); 
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; sed -n 100,200p Duszkiewicz2024_Figure_IsomapREM.m | grep -v -E "^\s*$"; grep -n -B3 "signrank" Duszkiewicz2024_Figure_IsomapREM.m | grep vbl; grep -n -B3 "signrank" Duszkiewicz2024_Figure_IsomapWake.m | grep -E "vbl|ix ="
```

```
% Calculate offset of each Isomap and correct tuning curves
recs = unique(whichRec);
totR = length(recs);
for nR = 1:totR    
    ixR = find(whichRec == nR); 
    ix = ixHd(find(ismember(ixHd,ixR)));
    tC = length(ix);
    ofW = nan(tC,1);
    ofWsh = nan(tC,1);
    for nC = 1:tC        
        cc = TCcrosscorr(tcReal(:,ix(nC)),tcWake(:,ix(nC))); % xcorr between two tuning curves
        [~,mx] = max(cc); % max point on the xcorr is the offset
        ofW(nC) = mx;
        cc = TCcrosscorr(tcRealSh(:,ix(nC)),tcWakeSh(:,ix(nC))); % xcorr between two tuning curves
        [~,mx] = max(cc); % max point on the xcorr is the offset
        ofWsh(nC) = mx;
    end
    meanOf = round(mean(ofW),0);
    tcWake(:,ixR) = circshift(tcWake(:,ixR),meanOf);
    tcRem(:,ixR) = circshift(tcRem(:,ixR),meanOf);
[... 75 more lines not kept]
```

**Agent**

Isomap tests are clear. Now the optogenetics and synaptic-connection scripts.

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat ListFiles/dataset_Opto.list; echo; cd Code/Analysis; f=Duszkiewicz2024_Figure_Optogenetics.m; grep -n -E "List2Cell|ranksum|signrank|polyfit|corr\(|ix[A-Za-z0-9_]* = find|isArch|isCtrl|tcWidth|smooth|nbins|binSize|= 6|pval|0\.05|excl|Wilcoxon" $f | head -80
```

```
A1106-180418
A1106-180419
A1110-180612
A1110-180613
A1110-180617
A1110-180619
A1110-180621
A1110-180626
A1113-180813
A1113-180816
A1801-181004
A1801-181015
A1804-181225
A1804-190104
A1806-190307
A1806-190314
A1808-190807
A1813-190408
A1815-190523
A1821-190910
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; f=Duszkiewicz2024_Figure_Optogenetics.m; sed -n 59,320p $f | grep -v -E "^\s*$|^\s*%"
```

```
dataset = List2Cell('dataset_Opto.list');
idRec = [];
for ii = 1:length(dataset)
    d = cell2mat(dataset(ii));
    idRec = [idRec; str2num(d(2:5))];
end
for ii = 1:length(dataset)
    fprintf(['Uploading recording ', dataset{ii},'\n'])
    load(fullfile(dataset{ii},'Analysis','BehavEpochs'));
    load(fullfile(dataset{ii},'Analysis','CellTypes'));
    load(fullfile(dataset{ii},'Analysis','SpikeData'));
    load(fullfile(dataset{ii},'Analysis','BrainArea'));
    load(fullfile(dataset{ii},'Analysis','Angle'));
    load(fullfile(dataset{ii},'Analysis','Groups'));
    load(fullfile(dataset{ii},'Analysis','Velocity'));
    optoEp = csvread(fullfile(dataset{ii},'Analysis','Opto_TS.csv'));     
    isHd = [isHd; hd];
    isNhd = [isNhd; nhd];
    isFs = [isFs; fs];
    isGd = [isGd; gd];
[... 157 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; f=Duszkiewicz2024_Figure_Optogenetics.m; sed -n 1,58p $f | grep -E "offStart|offEnd|=" | grep -v "\[\]"; sed -n 920,965p $f | grep -v -E "^\s*(ax|h[0-9])" | grep -v '^\s*$'; grep -n "isGdGain\|signrank" $f | head
```

```
offStart = 4; % start of OFF epoch (from beginning of light pulse)
offEnd = 0; % start of ON epoch (from beginning of light pulse)
smoothTC = 3; % smoothing of tuning curves for half-width (3 used in Duszkiewicz et al., 2024)
smoothFactors = 0; % smoothing of tuning curves for factor analysis (0 used in Duszkiewicz et al., 2024)
subplot(3,4,4)
hold on
    ix1 = isHd == 1 & group == 1 & isPos & isGdGain;
    vbl1 = factorMult_opto;
    vbl2 = factorAdd_opto;
    [r,p] = corr(vbl1,vbl2,'type','Pearson');
    ix2 = isFs == 1 & group == 1 & isPos & isGdGain;
    [r,p] = corr(vbl1,vbl2,'type','Pearson');
    xlabel({'Multiplicative factor'})
    ylabel('Additive factor')
    xlim([0 3])
    ylim([-0.5 1])
    [p,h,stats] = ranksum(vbl1(ix1),vbl1(ix2));
    [p,h,stats] = ranksum(vbl2(ix1),vbl2(ix2))
% 2nd row
subplot(3,4,5)
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; cat Duszkiewicz2024_GetSynapticPairs.m; grep -v '^\s*%' Duszkiewicz2024_GetSpikeCrosscorrs.m | grep -v '^\s*$'; f=Duszkiewicz2024_Figure_SynapticConnections.m; grep -v '^\s*$' $f | grep -v -E "^\s*(%|set|xlabel|ylabel|title|box|axis|xlim|ylim|hold|plot|subplot|figure|colormap|xticks|yticks|line|text|legend|bar|histogram|scatter|imagesc|ax\.|h[0-9]\.|ax =|nexttile|tiledlayout|mx[0-9]|m[0-9] =)" | sed -n 1,150p
```

```
load(fullfile('Analysis','SynCrossCorrs'));
binsize = median(diff(bins));

fprintf('Finding synaptic connections \n');
[synLat,synStrZ,synStrR,bounds,ccg_conv] = FindSynapse_Exc(ccg,'synWin',[0 2],'alpha',0.01,'bins',binsize,'convwin',41,'excSigWin',0.4);

    

SaveAnalysis(pwd,'SynPairs_P01',{pairs, ccg, bins, synLat,synStrZ,synStrR,bounds,ccg_conv},{'pairs', 'ccg', 'bins', 'lat', 'strZ', 'strR','bounds','ccg_conv'});


binsize = 0.2;
nbins = 250;
load(fullfile('Data','SpikeData'),'S');
fprintf('Computing spike train CCGs \n');
totC = length(S);
allCCG = nan(nbins+1,nchoosek(totC,2)*2);
allPairs = [];
noCCG = 1;
for nC1 = 1:totC   
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code; f=$(find . -name 'FindSynapse_Exc.m' ! -name '._*'); grep -v '^\s*%' $f | grep -v '^\s*$' | head -90; f2=$(find . -name 'cch_conv.m' ! -name '._*'); grep -v '^\s*%' $f2 | grep -v '^\s*$' | head -40
```

```
function [synLat,synStrZ,synStrR,sigBounds,pred] = FindSynapse(cch,varargin)
bins = 0.5; %in ms
window = 21; %number of bins
alpha = 0.001;
synWin = [0 10]; %window for synaptic connection in ms
excSigWin = 1; %in ms
inhSigWin = 2; %in ms
if nargin < 1 | mod(length(varargin),2) ~= 0,
  error('Incorrect number of parameters (type ''help FindSynapse'' for details).');
end
for i = 1:2:length(varargin),
  if ~isa(varargin{i},'char'),
    error(['Parameter ' num2str(i) ' is not a property (type ''help FindSynapse'' for details).']);
  end
  switch(lower(varargin{i})),
    case 'bins',
      bins = varargin{i+1};
      if ~isa(bins,'numeric') | length(bins) ~= 1 | bins <= 0
           error('Incorrect value for property ''bins'' (type ''help FindSynapse'' for details).');
      end
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code; f=$(find . -name 'FindSynapse_Exc.m' ! -name '._*'); grep -v '^\s*%' $f | grep -v '^\s*$' | sed -n 90,140p
```

```
ix = find(bbs>0);
            signBins(ix(2):end) = [];
        end
        for jj=1:length(signBins);
            [pkVal,pkT] = max(diffBins(signBins(jj):signBins(jj)+nbExcShifts-1,ii));
            predPk = predRest(pkT+signBins(jj)-1,excPairs(ii));
            confInt = sqrt(predPk); %Assuming a Poisson process
            strZ = (pkVal-predPk)/confInt;
            strR = pkVal/predPk;
            pkT = bb(signBins(jj)+pkT-1);
            if pkT>0 %reference cell is presynaptic;
                pkTimes(ii,2) = pkT;
                pkStrZ(ii,2) = strZ;
                pkStrR(ii,2) = strR;
            else %reference cell is postsynaptic
                pkTimes(ii,1) = -pkT;
                pkStrZ(ii,1) = strZ;
                pkStrR(ii,1) = strR;
            end
        end
[... 15 more lines not kept]
```

**Agent**

Optogenetics and synaptic code read. The opto exclusion rule in the code differs from the Methods. Checking the Stability ANOVA and the phase-correlation code before writing.

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; sed -n 236,330p Duszkiewicz2024_Figure_Stability.m | grep -v '^\s*$'; sed -n 540,600p Duszkiewicz2024_Figure_Fourier.m | grep -E "vbl|ix =|circ_corrcc"
```

```
t = deg2rad([0:1:nbins-1]);
maxBasis = 180;
maxComp = 10;
maxComp_score = 3;
% Fourier basis
basis = [];
for n = 1:maxBasis
    basis = [basis;cos(n*t) + 1i*sin(n*t)];
end    
vblFT = tcAll1; 
    % FFT code
    ft   = basis * vblFT/length(t); %complex Fourier components
    ftN  = ft .* conj(ft);% ./ repmat(var(vblFT)/2,[size(ft,1) 1]);
    ftN = abs(ftN);
    % cut FT to N first components and normalize
    ftN = ftN(1:maxComp,:)./repmat(sum(ftN(1:maxComp,:),1),maxComp,1); 
    ft1 = ftN;
vblFT = tcAll2; 
    % FFT code
    ft   = basis * vblFT/length(t); %complex Fourier components
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; sed -n 600,740p Duszkiewicz2024_Figure_Fourier.m | grep -E "vbl[12] =|ix =|circ_corrcc|signrank"
```

```
ix = ixFs;
    vbl1 = mod(phFt(1,:)',pi)*2;
    vbl2 = mod(phFt(2,:)',2*pi);
    [c,p] = circ_corrcc(vbl1(ix),vbl2(ix));
    ix = find(isFs);
    ix = find(isFs);
    [p1,~,stats1] = signrank(ftN(1,ix),ftN_sh(1,ix));
    [p2,~,stats2] = signrank(ftN(2,ix),ftN_sh(2,ix));
    [p3,~,stats3] = signrank(ftN(3,ix),ftN_sh(3,ix));
    [p4,~,stats4] = signrank(ftN(4,ix),ftN_sh(4,ix));
    ix = find(isHd & isPos);
    vbl1 = mod(phFt(1,:)',2/3*pi)*3;
    vbl2 = mod(phFt(3,:)',2*pi);
    [c,p] = circ_corrcc(vbl1(ix),vbl2(ix));
    ix = find(isHd & isAdn);
    vbl1 = mod(phFt(1,:)',2/3*pi)*3;
    vbl2 = mod(phFt(3,:)',2*pi);
    [c,p] = circ_corrcc(vbl1(ix),vbl2(ix));
    ix = ixFs;
    vbl1 = mod(phFt(1,:)',2/3*pi)*3;
[... 3 more lines not kept]
```

**Agent**

I have what I need from the code. Checking the claims schema and checker before writing.

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/claims_check.py; ls docs; grep -rn "kind:" claims/*/*.yaml | awk '{print $NF}' | sort | uniq -c; grep -rn "^  data:" claims/*/*.yaml | awk '{print $NF}' | sort | uniq -c
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

[... 58 more lines not kept]
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
cd  python -c "
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

**Agent**

The schema requires a p or CI per statistic, but most of this paper's tests print only z. Checking how earlier claims files handled that.

**Agent calls Bash**

```bash
cd  grep -rn -i -E "no p-value|without a p|p is not (printed|reported)|prints no p|no p value" claims/ | head -8
```

```
claims/001276/10.1016-j.bioelechem.2025.109016.yaml:535:  - Open, not settled. fig4b-center-no-rate-effect records p > 0.05 from "no significant effect"; the paper prints no p-value, and which rates were compared is not stated (each rate against 1 Hz is read from the Fig. 4C legend).
claims/000061/10.1038-nn.4637.yaml:254:    Bonferroni-corrected post hoc tests are shown but give no P values to match.
claims/001260/10.1038-s41593-025-02190-z.yaml:190:    pairwise contrast). The VoR text gives no p-value; the figure marks are not in the text.
claims/001863/10.1101-2025.07.09.663970.yaml:696:  - Open, fig1c-accuracy-time-bins, the statement's wording covers the 25 to 30 min bin, but the text gives no p-value for it (the code's bin labels make "10 to 25 min" the bins 10-15, 15-20 and 20-25); it is reported and not judged.
claims/001525/10.1016-j.bioelechem.2026.109283.yaml:34:# 100, the first 40 without a pulse (baseline) and the next 60 with a pulse of one amplitude;
claims/000059/10.1016-j.neuron.2020.05.023.yaml:22:# window were found to mark pairs without a peak inside it, so lags are taken at local
claims/001350/10.1073-pnas.2307250121.yaml:306:    unpaired t test (n = 6 mice per genotype); no p-value is printed.
claims/001350/10.1073-pnas.2307250121.yaml:532:    and S3G print no p-value. The checker's VALUE NOT FOUND lines for these are values printed only
```

**Agent calls Bash**

```bash
cd  sed -n 1,40p claims/001350/10.1073-pnas.2307250121.yaml; grep -n "^[a-z#]" claims/001276/10.1016-j.bioelechem.2025.109016.yaml | head; sed -n 520,540p claims/001276/10.1016-j.bioelechem.2025.109016.yaml
```

```
# Claims for Iram, Garcia et al. (2024), PNAS 121(12) e2307250121, on dandiset 001350.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record as served by Europe PMC (PMC10962977), main text, figure
# legends and Methods, with the SI Appendix (pnas.2307250121.sapp.pdf: Figs. S1 to S5, their
# legends, Supplementary Materials and Methods). Datasets S1 to S3 (XLSX) were not read. The
# main article's PDF was not supplied; values and p-values printed only on the panels of
# Figures 2 and 5 were read from the figure images of the PMC article (pnas.2307250121fig02.jpg,
# fig05.jpg), and those of Figs. S2 and S3 from the SI Appendix PDF. Figure 4's image could not
# be fetched, so the values of Fig. 4C to 4F are not recorded. Numbers read off a bar plot
# are marked as such and are good to about one tick of the axis's finest gridline.
#
# Code. The paper links no analysis code. Its Data availability names only NCBI GEO GSE241561
# (ChIP-seq, bulk RNA-seq, snRNA-seq). TEM was quantified by hand in Fiji/ImageJ and the
# statistics run in GraphPad Prism 9. The dandiset's description points to a segmentation
# model (github.com/axondeepseg/model_seg_unmyelinated_tem) trained later on these images.
# It is not the paper's code and was not read.
#
# The dandiset ("TEM Images of Corpus Callosum in Flox/SRF-cKO Mice") holds, by its
[... 47 more lines not kept]
```

**Agent**

I'll check one more detail in the opto script (the firing-rate modulation measure), then write the file.

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; f=Duszkiewicz2024_Figure_Optogenetics.m; sed -n 530,700p $f | grep -E "vbl[12]? =|ix[12]? =|ranksum|signrank"; sed -n 760,830p $f | grep -E "vbl[12]? =|ix[12]? =|ranksum|signrank"; grep -n "hwTc\|signrank" $f | sed -n 1,40p | grep -E "signrank|vbl"
```

```
ix1 = find(isHd & isAdn);
    ix2 = find(isNhd & isAdn);
    vbl1 = optoRes(ix1); 
    vbl2 = optoRes(ix2); 
    [p,h,stats] = ranksum(vbl1,vbl2);
    vbl = optoRes;
    ix1 = find(isHd == 1 & group == 1 & isPos);
    ix2 = find(isHd == 1 & group == 2 & isPos);
    vbl1 = vbl(ix1); 
    vbl2 = vbl(ix2); 
    [p,h,stats] = ranksum(vbl1,vbl2);
    vbl = optoRes;
    ix1 = find(isFs == 1 & group == 1 & isPos);
    ix2 = find(isFs == 1 & group == 2 & isPos);
    vbl1 = vbl(ix1); 
    vbl2 = vbl(ix2); 
    [p,h,stats] = ranksum(vbl1,vbl2);
    ix = find(isHd & isAdn);
    vbl1 = hwTc_off(ix);
    vbl2 = hwTc_on(ix);
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/Code/Analysis; grep -n -E "vel|Ep\b|wake1Ep|binsize|smooth|sqrt|compute_mapping|knn|k =|nbins|ix = |hd ==|find\(hd" Duszkiewicz2024_GetIsomap_WAKE.m | head -30; grep -n -E "vel|wake1Ep|rem|binsize|smooth|sqrt|compute_mapping|nbins|randperm|randsample|find\(hd" Duszkiewicz2024_GetIsomap_WAKEvsREM.m | head -30
```

```
6:binsize = 0.2; % bin size for population vectors, needs to be large
7:thSmooth = 2; % smoothing factor of population vectors
10:velTh = 2; % velocity threshold (2 = default)
21:ep = wake1Ep;
26:ixHd = find(hd == 1);
37:    Q = MakeQfromS(S,binsize); 
43:    frate = frate ./ binsize;
47:    dQ = sqrt(dQ);
52:    mapping = compute_mapping(dq_iso, 'Isomap',3); % run the Isomap script
62:% r = r - binsize/2; % move the angle values to the beginning of Q bins, otherwise first half of the bin will have a wrong ang
73:ix = find(isnan(dr));
104:tcWk = nan(nBins,totC);
108:h0_wk = hist(mod(Data(isoAng),2*pi),B); % histograms of angle distribution
119:        dt = 1./binsize;
138:        dt = 1./binsize;
157:        dt = 1./binsize;
251:ix = ixHd;
302:    ix = ixCells;
6:binsize = 0.2; % bin size for population vectors, needs to be large
7:thSmooth = 2; % smoothing factor of population vectors
[... 29 more lines not kept]
```

**Agent**

I've read the text, supplement and code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000939/10.1038-s41593-024-01588-5.yaml",
 "content": "# Claims for Duszkiewicz, Orhan, Skromne Carrasco, Brown, Owczarek, Vite, Wood & Peyrache (2024),\n# Nature Neuroscience 27, 782-792, on dandiset 000939.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record as served by Europe PMC (PMC11001581), main text, figure\n# legends, Methods and Extended Data figure legends, with both supplements: the Supplementary\n# Information (41593_2024_1588_MOESM1_ESM.pdf, Supplementary Methods on model fitting and theory)\n# and the Reporting Summary (MOESM2). The main article's PDF was not supplied, so the figures\n# were not seen. Values printed only on figure panels (the r values of Fig. 6c and Extended Data\n# Fig. 9, the CV of Fig. 4f, medians in Fig. 2 and 3, most p-values) are not recorded. Most\n# legends give a z statistic and no p-value; those z values are given in the criteria, as the\n# claims schema records a statistic only with a p-value.\n#\n# Code read: the paper's Code availability, figshare doi:10.6084/m9.figshare.24921252 (version 3,\n# published 2025-12-11), files MatlabCode_Duszkiewicz2024.zip (md5 8f391dec0d3fa120ef58f3158443f5df)\n# and SessionLists_ForAnalysis.zip (md5 5653a94673ce2db0da9ac38a38800413). It holds the MATLAB\n# scripts that compute every analysis but the simulations (Duszkiewicz2024_Get*.m per session,\n# Duszkiewicz2024_Figure_*.m per figure), their dependencies (TStoolbox, CircStat, the\n# Dimensionality Reduction Toolbox, FindSynapse_Exc and cch_conv) and the session lists\n# (dataset_All.list, 32 PoSub sessions; dataset_All_FT.list, the 32 plus 19 ADN sessions;\n# dataset_All_Rem.list, 28; dataset_Stability.list, 19; dataset_Opto.list, 21; dataset_cuerot.list,\n# 7). The Python code of the simulations and model fit (Fig. 4, Extended Data Fig. 5,\n# Supplementary Methods) is not deposited there. The data files of the figshare item were not\n# opened.\n#\n# Where the code settles what the Methods leave open, the criteria follow it and say so. Where\n# they disagree the Methods are followed and the code's choice is named as a variant. The\n# disagreements found are these. (1) Cell classes. Methods give a trough-to-peak cut of 0.4 ms;\n# Duszkiewicz2024_GetCellTypes_PoSub.m uses 0.35 ms (FS at or below 0.35 ms and at least 10 Hz,\n# excitatory above 0.35 ms and at most 10 Hz). (2) Fourier power. Methods call the power \"the root\n# mean square of the projection values onto the sine and cosine basis\"; the code takes the\n# squared modulus of the complex coefficient (ft .* conj(ft)), which is what makes the Parseval\n# check of Extended Data Fig. 3e hold. Both are named as readings, as the Methods' own text\n# allows both. (3) KL divergence. Methods give D_KL(sigma_i || S); the code's KLDiv(S, sigma_i)\n# computes D_KL(S || sigma_i). (4) The as-shipped Figure_Fourier.m keeps only PoSub-HD cells with\n# a multipeak score below 0.05 for every Fourier analysis, which is the Extended Data Fig. 3k\n# control; the legends' n = 1,602 shows that Fig. 3 used all PoSub-HD cells. (5) Stability\n# analyses (Figure_Stability.m) take the tuning curves smoothed at 2 degrees (index smoothTC, not\n# smoothTC+1); Methods give 3 degrees throughout. (6) Widths before and during light (Extended\n# Data Fig. 7d, i) are tested with the Wilcoxon signed-rank test in the legends and with ranksum\n# in the code. (7) The opto exclusion rule (below).\n#\n# The data the paper used. Electrophysiology in 43 adult male mice (VGAT-IRES-Cre, PV-IRES-Cre or\n# SST-IRES-Cre crossed with C57BL/6J; one C57BL/6J x FVB mouse with a Neuropixel 1.0 probe for\n# Fig. 1a-c). PoSub was recorded with 64-channel H5 linear probes, vertically (931 units, 14\n# mice) or parallel to the cell layers (1,999 units, 18 mice), one session per mouse; ADN with\n# four-shank Buzsaki32 probes, several sessions per mouse (97 ADN-HD cells, 8 mice). Each session\n# is a home-cage sleep epoch, square open-field exploration (80 cm walls), a second sleep epoch,\n# and in a subset a triangular open field, a cue rotation session (6 sessions) or, in\n# VGAT-Cre mice with ArchT or control virus in TRN and optic fibres over ADN, a second\n# exploration with 240 one-second 520 nm light pulses (PoSub ArchT 83 HD and 47 FS cells from 5\n# mice; control 89 HD and 38 FS cells from 3 mice; ADN 127 thalamic cells including 52 HD cells\n# from 3 mice). Signals at 20 kHz, spikes sorted with Kilosort 2.0 and curated; head direction\n# (yaw of the Optitrack headcap) at 100 Hz; sleep scored with SleepScoreMaster (REM, NREM, WAKE).\n# Measured variables are spike times, mean waveforms (trough-to-peak), head direction, position\n# and speed, sleep states, light pulse times, and probe channel positions.\n#\n# The dandiset (\"Large-scale recordings of head direction cells in mouse postsubiculum\"), by its\n# description, holds the PoSub H5-probe recordings, one session per mouse, 31 mice, 42 to 185\n# units per recording, each with a square open field and two sleep epochs and some with a\n# triangle or an optogenetic stimulation epoch, with spike times, waveforms, position, head\n# direction, sleep scoring and raw data. These are the figshare Datasets 1 (17 parallel) and 2\n# (14 vertical). The paper's PoSub list has 32 sessions, so counts over the dandiset may fall a\n# little short of the paper's. The ADN recordings (figshare Dataset_5), the cue rotation sessions\n# (Dataset_3), the Neuropixel session (Dataset_4) and the ADN and other opto sessions (Dataset_6)\n# are on figshare only; the claims that need them have data elsewhere. Whether the dandiset\n# holds the control-virus PoSub opto sessions is for the author to find.\n#\n# Method fixed for every PoSub claim, from the Methods and the code. Units with mean rate at\n# least 0.5 Hz over the square open-field epoch and a negative-going waveform (the code's\n# waveform features are NaN for positive spikes). FS cells, trough-to-peak below 0.4 ms and rate\n# above 10 Hz; excitatory, trough-to-peak above 0.4 ms and rate below 10 Hz (code variant 0.35\n# ms). HD cells, excitatory cells with HD information above 0.2 bits per spike, the 99th\n# percentile of the time-reversed control (the computed percentile is a second reading). Tuning\n# curves, spike count over occupancy in 1 degree bins, smoothed with a Gaussian of 3 degrees s.d.,\n# from times in the square epoch (first to last tracked sample) with speed above 2 cm/s. HD\n# information as the Methods' formula, in bits per spike, from the smoothed curve. Time-reversed\n# control, the HD series reversed in time within the epoch. Tuning curve width, from the code\n# (Figure_Fourier.m), the full width at half maximum of the peak-aligned, max-normalized curve\n# averaged over its two sides. Fourier signature, the projection of the 360-bin curve on the\n# harmonics 1 to 180, power per harmonic, the first ten normalized to their sum. All tests\n# two-tailed (Methods).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000939\"\npaper: doi:10.1038/s41593-024-01588-5\nclaims:\n- id: cell-classes-counts\n  statement: PoSub units split into 1,835 putative excitatory cells and 427 putative FS cells by\n    firing rate and waveform, and 1,602 excitatory cells (87%) were HD cells with HD information\n    above 0.2 bits per spike; the vertical recordings gave 931 units from 14 mice and the parallel\n    ones 1,999 units from 18 mice.\n  source: Results, High-density recordings in the PoSub of freely moving mice, paragraph 1;\n    Methods, Spike sorting and unit classification, and HD tuning curves and tuning metrics\n  quote: The probe was implanted either vertically ( n = 931 units from 14 mice, range ... or\n    parallel to PoSub cell layers ( n = 1,999 units from 18 mice ... PoSub units were subdivided\n    into putative excitatory cells ( n = 1,835) and putative PoSub-FS cells ( n = 427) based on\n    mean firing rate and waveform shape ... were classified as PoSub-HD cells (>0.2 bits per\n    spike, n = 1602, 87% of excitatory cells\n  expected:\n  - quantity: putative excitatory cells\n    value: 1835\n    tolerance: 184\n  - quantity: putative FS cells\n    value: 427\n    tolerance: 43\n  - quantity: PoSub-HD cells\n    value: 1602\n    tolerance: 160\n  - quantity: fraction of excitatory cells that are HD cells\n    value: 0.87\n    tolerance: 0.087\n  - quantity: units in vertical recordings\n    value: 931\n    tolerance: 93\n  - quantity: units in parallel recordings\n    value: 1999\n    tolerance: 200\n  criterion: Classification as fixed in the opening comment (Methods). The 0.4 ms trough-to-peak\n    cut is the main reading and the code's 0.35 ms a variant; the HD threshold is read as 0.2\n    bits per spike (Results, Methods and code) and as the 99th percentile of the excitatory\n    cells' time-reversed HD information (Methods' definition). The fraction can be 87% (Results)\n    or 85% (Methods, \"85% of putative excitatory cells\"); either value within tolerance counts.\n    Unit counts are over all units of each probe orientation as the dandiset's metadata gives it.\n    The dandiset holds 31 of the 32 sessions, so a count below the paper's by one session's\n    cells is reported as such. If the dandiset carries its own cell-type labels, they are\n    compared with the recomputed classes and both counts are shown.\n- id: ed2b-excitatory-hd-information\n  statement: Putative excitatory PoSub cells carry more HD information than their time-reversed\n    controls, and HD information across all PoSub cells is bimodal.\n  source: Extended Data Fig. 2b,c\n  quote: Distribution of HD information carried by tuning curves of putative excitatory cells in\n    PoSub ( n = 1835; Wilcoxon signed rank test vs time-reversed control, z = 37.1\n  criterion: As in Duszkiewicz2024_Figure_BasicProperties.m, log10 HD information of each\n    excitatory cell against that of its time-reversed control, Wilcoxon signed-rank test, paired\n    by cell. The paper reports z = 37.1 and no p-value. Reproduced when p < 0.05 with the real\n    median above the control median. The bimodality of Extended Data Fig. 2c is shown, not judged.\n- id: fig2a-fs-hd-information\n  statement: The HD information carried by PoSub-FS cell tuning curves is higher than that of\n    their time-reversed controls.\n  source: Results, Tuning of PoSub-FS cells is stable and anchored to landmarks, paragraph 1;\n    Figure 2a\n  quote: at the population level, the quantity of HD information conveyed by PoSub-FS cells was\n    significantly higher than that of the time-reversed control\n  depends_on:\n  - cell-classes-counts\n  criterion: As in Duszkiewicz2024_Figure_BasicProperties.m, log10 HD information of each FS cell\n    against its time-reversed control, Wilcoxon signed-rank test (Fig. 2a legend, n = 427, z =\n    17.9, no p-value printed). Reproduced when p < 0.05 and the median of the real values is above\n    that of the controls. The median HD information of PoSub-HD cells (the dashed line of Fig. 2a)\n    is reported alongside.\n- id: fig2b-decoding-from-fs\n  statement: The animal's HD can be decoded accurately from PoSub-FS cell spiking with a Bayesian\n    decoder built on their tuning curves, and decoding error falls as more FS cells are used.\n  source: Results, Tuning of PoSub-FS cells is stable and anchored to landmarks, paragraph 1;\n    Figure 2b; Extended Data Fig. 2e\n  quote: The information contained in PoSub-FS cell tuning curves was sufficient to accurately\n    decode the animal's HD from PoSub-FS cell spiking activity\n  depends_on:\n  - cell-classes-counts\n  criterion: The Methods do not describe this decoder; Duszkiewicz2024_GetBayesianDecoding.m\n    settles it. Tuning curves (360 bins, 3 degree smoothing) from the first half of the square\n    epoch at speed above 2 cm/s; spike counts in 100 ms bins smoothed with a Gaussian of 2 bins\n    s.d.; one-dimensional Bayesian decoding (Poisson) over the second half of the epoch, all\n    times; error as the absolute angular difference from the real HD, median per session; the\n    same with time-reversed tuning curves gives the chance level. Reproduced when the mean over\n    the sessions (32 in the paper) of the FS decoder's median error is below the chance level\n    (the mean of the control medians, as Extended Data Fig. 2e draws it) and the Pearson\n    correlation across sessions between the number of FS cells and the median error is negative\n    with p < 0.05 (Extended Data Fig. 2e, Pearson, n = 32). The HD-cell decoder's error is shown\n    for comparison.\n- id: fig2c-geometry-independent\n  statement: The tuning of PoSub-FS cells is preserved between the square and triangular arenas,\n    as it is for PoSub-HD cells.\n  source: Results, Tuning of PoSub-FS cells is stable and anchored to landmarks, paragraph 2;\n    Figure 2c; Extended Data Fig. 2j\n  quote: the tuning of PoSub-FS cells was stable within a single exploration epoch (Extended Data\n    Fig. 2h ) and independent of the enclosure geometry (Fig. 2c ), reflecting the properties of\n    canonical PoSub-HD cells\n  depends_on:\n  - cell-classes-counts\n  criterion: Sessions with a triangle epoch. Selection from Figure_Stability.m, FS cells with rate\n    above 10 Hz and HD cells with rate above 0.5 Hz in both arenas. The triangle tuning curves of\n    each session are shifted back by the circular mean rotation of its HD cells (the lag of\n    maximum square-triangle cross-correlation), as the Methods say; then the Pearson correlation\n    at zero lag of each cell's square and triangle curves, against the same for time-reversed\n    curves, Wilcoxon signed-rank (Fig. 2c, n = 264 FS cells, z = 14.0; Extended Data Fig. 2j,\n    n = 1,013 HD cells, z = 27.6; no p-values printed). Reproduced when both tests give p < 0.05\n    with real correlations above the controls. Curves smoothed at 3 degrees (Methods); the code's\n    2 degrees is a variant.\n- id: ed2hi-within-epoch-stability\n  statement: Tuning curves of PoSub-FS and PoSub-HD cells computed from the two halves of the\n    square-arena epoch are correlated above their time-reversed controls.\n  source: Extended Data Fig. 2h,i\n  quote: PoSub-FS cell tuning curve correlation across two halves of the square arena epoch\n  depends_on:\n  - cell-classes-counts\n  criterion: As in Figure_Stability.m and GetHdTuning_xval.m, tuning curves from the two halves\n    of the movement epoch, zero-lag Pearson correlation per cell against the time-reversed halves,\n    Wilcoxon signed-rank (FS n = 427, z = 17.8; HD n = 1,602, z = 34.7; no p-values printed).\n    Reproduced when both give p < 0.05 with real correlations higher. Smoothing at 3 degrees\n    (Methods), 2 degrees (code) as a variant.\n- id: fig2f-cue-rotation\n  statement: In a cue rotation task PoSub-FS cell tuning curves follow the rotated distal landmark\n    together with PoSub-HD cells.\n  source: Results, Tuning of PoSub-FS cells is stable and anchored to landmarks, paragraph 2;\n    Figure 2d-f\n  quote: PoSub-FS cell tuning curves followed the rotated distal landmark in concert with PoSub-HD\n    cells\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.24921252 version 3, Dataset_3.tar.gz (cue rotation, 6\n    sessions)\n  criterion: Per the Methods (Analysis of HD cell realignment after cue rotation) and\n    Figure_CueRotation.m. Rotation epochs kept when the decoder error over the next 200 s exceeds\n    45 degrees and the animal moved (mean speed at least 2 cm/s) in the preceding epoch;\n    realignment ends at 0.99 of a fitted sigmoid; per FS cell the mean absolute difference between\n    its rotation and the mean rotation of the session's HD cells, against the time-reversed\n    control, Wilcoxon signed-rank (n = 99 FS cells, z = 8.25, no p-value printed). Reproduced when\n    p < 0.05 with real differences smaller than control. The Methods' exclusion reads \"(1) ... and\n    (2)\"; it is read as excluding epochs that fail either condition and, as a second reading,\n    both.\n- id: fig3c-adn-broader\n  statement: ADN-HD cells have broader tuning curves than PoSub-HD cells.\n  source: Results, Equivalence of PoSub-HD and FS cell tuning in Fourier space, paragraph 1;\n    Figure 3c\n  quote: In mice, ADN-HD cells tend to have broader HD tuning curves than PoSub-HD cells\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.24921252 version 3, Dataset_5.tar.gz (ADN recordings)\n  depends_on:\n  - cell-classes-counts\n  criterion: Width as in the opening comment (code). Mann-Whitney U test of PoSub-HD against\n    ADN-HD widths (n = 1,602 and 97, z = 11.4, no p-value printed). Reproduced when p < 0.05 with\n    the ADN median wider. ADN-HD cells are classified by Duszkiewicz2024_GetCellTypes_ADN.m.\n- id: fig3-ten-components-power\n  statement: Fourier power of tuning curves decays quickly with frequency, and the first ten\n    components hold on average 98% of the total power.\n  source: Results, Equivalence of PoSub-HD and FS cell tuning in Fourier space, paragraph 2\n  quote: Across the cell population, the Fourier power decayed rapidly as a function of\n    frequency. Hence, for clarity, we focused our analysis on the relative power of the first ten\n    Fourier components that contained, on average, 98% of the total power\n  expected:\n    quantity: mean fraction of power (harmonics 1 to 180) in harmonics 1 to 10\n    value: 0.98\n    tolerance: 0.02\n  depends_on:\n  - cell-classes-counts\n  criterion: The tolerance is 0.02 because a fraction cannot exceed 1, so 10% of the value would\n    not test it. \"The cell population\" is read as (a) PoSub-HD and PoSub-FS cells pooled (the\n    dandiset) and (b) each of the two separately; ADN-HD cells, when available, as a variant. Power\n    is read as (a) the squared modulus of the complex coefficient (code, and the Parseval check of\n    Extended Data Fig. 3e) and (b) the root mean square of the sine and cosine projections\n    (Methods' words). Reproduced when one population reading under each power reading is within\n    tolerance.\n- id: fig3e-fourier-signatures-differ\n  statement: The average Fourier signatures of PoSub-FS, PoSub-HD and ADN-HD populations differ,\n    with ADN-HD cells having more power at low and less at high components than PoSub-HD and\n    PoSub-FS cells, which are alike.\n  source: Results, Equivalence of PoSub-HD and FS cell tuning in Fourier space, paragraph 3;\n    Figure 3e; Extended Data Fig. 3f\n  quote: the Fourier signature of ADN-HD cells was different from both PoSub-HD and PoSub-FS\n    cells, with higher power at low frequencies and lower power at higher frequencies\n  statistics:\n  - test: two-way ANOVA, Fourier component by cell type interaction\n    statistic: F (9,19116) = 2.76\n    p: 0.003\n    n: 427 PoSub-FS, 1,602 PoSub-HD and 97 ADN-HD cells\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.24921252 version 3, Dataset_5.tar.gz (ADN recordings)\n  depends_on:\n  - cell-classes-counts\n  criterion: As in Figure_Fourier.m, a repeated-measures ANOVA (fitrm and ranova) of the ten\n    normalized powers with cell type as between factor; the component by cell type interaction.\n    Reproduced when p < 0.05 and the ADN-HD mean signature is above both PoSub means at component\n    1 and below both summed over components 3 to 10. Both power readings (squared modulus, code;\n    root mean square, Methods) are run. The same ANOVA on PoSub-FS and PoSub-HD only, which the\n    dandiset alone allows, is shown as a variant and not judged.\n- id: fig3f-posub-hd-closer-to-fs\n  statement: Individual PoSub-HD cell Fourier spectra are closer to the average PoSub-FS signature\n    than ADN-HD cell spectra are.\n  source: Results, Equivalence of PoSub-HD and FS cell tuning in Fourier space, paragraph 3;\n    Figure 3f\n  quote: we found that the average Fourier signature of the PoSub-FS cell population was often\n    indistinguishable from the Fourier signatures of individual PoSub-HD cells\n  statistics:\n  - test: Mann-Whitney U test\n    p: 1.0e-9\n    p_relation: \"<\"\n    n: 1,602 PoSub-HD and 97 ADN-HD cells\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.24921252 version 3, Dataset_5.tar.gz (ADN recordings)\n  depends_on:\n  - cell-classes-counts\n  criterion: KL divergence between each HD cell's ten-component spectrum and the mean PoSub-FS\n    spectrum, Mann-Whitney U of PoSub-HD against ADN-HD. Readings, all run, for what the paper\n    leaves open or states against its code. Divergence direction, D_KL(sigma_i || S) (Methods)\n    and D_KL(S || sigma_i) (code). Power, squared modulus (code) and root mean square (Methods).\n    Reproduced when p < 1e-9 with the PoSub-HD median smaller under every reading; partially\n    reproduced when p < 0.05 with PoSub-HD smaller under every reading but p is not below 1e-9 in\n    all. PoSub-HD cells are all HD cells (n = 1,602); the shipped code's multipeak filter is the\n    Extended Data Fig. 3k control.\n- id: ed3k-robust-to-controls\n  statement: The smaller distance of PoSub-HD than ADN-HD spectra from the PoSub-FS signature holds\n    after excluding multipeaked HD cells, after excluding noisy clusters, and with a 10 cm/s speed\n    threshold; ADN-HD cells have higher multipeak scores than PoSub-HD cells.\n  source: Results, Equivalence of PoSub-HD and FS cell tuning in Fourier space, paragraph 3;\n    Extended Data Fig. 3j,k\n  quote: the similarity between PoSub-HD and PoSub-FS cell Fourier signatures on a population level\n    was preserved when the analysis was limited to HD cells with a single receptive field.\n    Additionally, it was preserved when a threshold was applied to keep only the best isolated\n    unit clusters or when a higher velocity threshold was used to compute tuning curves\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.24921252 version 3, Dataset_5.tar.gz (ADN recordings)\n  depends_on:\n  - fig3f-posub-hd-closer-to-fs\n  criterion: The Fig. 3f test under each control, with the readings of fig3f-posub-hd-closer-to-fs.\n    Multipeak score as the Methods define it, the mean of the normalized curve outside its peak\n    (plus or minus the width from the maximum), cells kept below 0.05 (code, Figure_Fourier.m);\n    expected n = 789 and 69, z = 10.4. Contamination score, spike autocorrelogram at plus or minus\n    100 ms in 1 ms bins, value at 0.1 ms over the highest value, clusters kept at or below 0.2;\n    n = 1,472 and 83, z = 5.91. Speed above 10 cm/s; n = 1,602 and 97, z = 6.46. Multipeak scores,\n    Mann-Whitney U, n = 1,602 and 97, z = 4.25. No p-values are printed. Reproduced when all four\n    tests give p < 0.05 in the paper's direction under every reading.\n- id: fig3g-first-three-components\n  statement: Compared with time-reversed controls, the PoSub-FS spectrum has higher power for the\n    first three Fourier components only.\n  source: Results, Equivalence of PoSub-HD and FS cell tuning in Fourier space, paragraph 4;\n    Figure 3g\n  quote: Compared to controls, the spectrum of PoSub-FS cells showed higher power for the first\n    three Fourier components only\n  statistics:\n  - about: component by condition interaction, FS against time-reversed control\n    test: two-way ANOVA, Fourier component by cell type interaction\n    statistic: F (9,3834) = 64.1\n    p: 4.0e-110\n    n: 427 PoSub-FS cells\n  - about: first component, FS against control\n    test: Wilcoxon signed-rank test\n    statistic: z = 0.65\n    p: 8.0e-10\n    corrected: Bonferroni\n    n: 427 PoSub-FS cells\n  - about: second component, FS against control\n    test: Wilcoxon signed-rank test\n    statistic: z = 0.85\n    p: 3.0e-16\n    corrected: Bonferroni\n    n: 427 PoSub-FS cells\n  - about: third component, FS against control\n    test: Wilcoxon signed-rank test\n    statistic: z = 0.46\n    p: 4.0e-5\n    corrected: Bonferroni\n    n: 427 PoSub-FS cells\n  depends_on:\n  - cell-classes-counts\n  criterion: As in Figure_Fourier.m, ten normalized powers of each FS cell and of its time-reversed\n    curve; repeated-measures ANOVA with condition and component as within factors (the\n    interaction); then a Wilcoxon signed-rank test per component with p multiplied by 10. The code\n    divides the printed z by 10, which is why the legend's z values are small; the test's own z is\n    reported too. Reproduced when the interaction has p < 0.05 and components 1, 2 and 3, and no\n    other, are significantly higher than control after correction. Both power readings are run.\n- id: fig3h-dominant-component\n  statement: Of the 427 PoSub-FS cells, 231, 141 and 55 have their highest power in the first,\n    second and third Fourier component, proportions similar to the relative mean power of those\n    components.\n  source: Results, Equivalence of PoSub-HD and FS cell tuning in Fourier space, paragraph 4; Figure\n    3h; Extended Data Fig. 4a legend\n  quote: The proportions of recorded PoSub-FS cells with the highest relative power in each of the\n    first three Fourier components were similar to the relative mean power for the population\n  expected:\n  - quantity: FS cells with highest power in component 1\n    value: 231\n    tolerance: 23\n  - quantity: FS cells with highest power in component 2\n    value: 141\n    tolerance: 14\n  - quantity: FS cells with highest power in component 3\n    value: 55\n    tolerance: 6\n  depends_on:\n  - cell-classes-counts\n  criterion: The counts are those of Extended Data Fig. 4a (n = (231, 141, 55)), each cell assigned\n    to the largest of its first three powers (code, highComp; the power reading does not change\n    the assignment). \"Similar\" is not defined; the readings are (a) the three proportions are in\n    the same order as the mean relative powers of components 1 to 3 renormalized over those three,\n    and (b) each proportion is within 10% of its renormalized mean power. Reproduced when the\n    counts are within tolerance and both readings hold under both power readings; partially\n    reproduced when the counts hold and only one reading does.\n- id: ed3g-fs-spectra-heterogeneous\n  statement: Fourier signatures are far more variable among PoSub-FS cells than among HD cells of\n    the same region, so individual FS cells are narrowly tuned in Fourier space.\n  source: Results, Equivalence of PoSub-HD and FS cell tuning in Fourier space, paragraph 5;\n    Extended Data Fig. 3g\n  quote: while the shape of Fourier signatures was largely uniform among HD cells from the same\n    brain region, it was highly variable among PoSub-FS cells\n  statistics:\n  - about: cell type effect on distance from own population mean\n    test: one-way ANOVA\n    statistic: F (2,2123) = 169\n    p: 5.0e-69\n    n: 427 PoSub-FS, 1,602 PoSub-HD and 97 ADN-HD cells\n  depends_on:\n  - cell-classes-counts\n  criterion: Distance of each cell's spectrum from its own population's mean spectrum. The legend\n    says \"statistical distance\" and its abbreviations name D_KL; the code (Figure_Fourier.m,\n    ftDist) uses the Euclidean distance over the ten components for the ANOVA and the tests. Both\n    are run, with both power readings. The part the dandiset holds is FS against PoSub-HD,\n    Mann-Whitney U, p multiplied by 3 (legend z = 5.71, a third of the test's z as the code\n    divides it; no p printed). Reproduced when that test gives p < 0.05 with FS distances larger\n    under every reading. The ANOVA and the comparisons with ADN-HD (z = 3.40 and 0.45) are run\n    when the figshare ADN data are used and are reported.\n- id: ed3l-fs-phases-independent\n  statement: Phases of the Fourier components are correlated with each other in individual HD\n    cells but random relative to each other in PoSub-FS cells.\n  source: Results, Equivalence of PoSub-HD and FS cell tuning in Fourier space, paragraph 5;\n    Extended Data Fig. 3l\n  quote: In contrast, the Fourier components of individual PoSub-FS cells had random phases\n    relative to each other\n  depends_on:\n  - cell-classes-counts\n  criterion: As in Figure_Fourier.m, phase of each component as the angle of the complex\n    coefficient; circular correlation (circ_corrcc) between twice the first phase (mod 2 pi) and\n    the second phase, and between three times the first phase and the third phase, across cells\n    (Extended Data Fig. 3l, 1,602 PoSub-HD and 427 PoSub-FS cells). The FS part is a claim of\n    absence judged on that test at p < 0.05. Reproduced when both PoSub-HD correlations are\n    significant and neither FS correlation is; the coefficients are reported either way. ADN-HD\n    cells are a variant when their data are used.\n- id: ed4a-autocorrelogram-symmetries\n  statement: Tuning curve auto-correlograms of FS cells with the highest power in the second\n    component peak at 180 degrees, and those with the highest power in the third at 120 and 240\n    degrees, above controls.\n  source: Results, Equivalence of PoSub-HD and FS cell tuning in Fourier space, paragraph 6;\n    Extended Data Fig. 4a\n  quote: Auto-correlograms of tuning curves for cells with maximum power for the second component\n    showed a second maximum at 180°, reflecting their twofold radial symmetry. For cells with\n    maximum power in the third component, auto-correlograms peaked at 120° and 240°\n  depends_on:\n  - fig3h-dominant-component\n  criterion: Cross-validated auto-correlograms as the Methods and GetTuningAutocorr_xval.m give\n    them (z-scored curves from the two halves of the movement epoch, Pearson correlation at each\n    circular shift). For twofold cells the value at 180 degrees, for threefold cells the mean of\n    the values at 120 and 240 degrees, each against the same from time-reversed curves, Wilcoxon\n    signed-rank (n = 141 and 55; no statistic printed). Reproduced when both give p < 0.05 with\n    real values higher.\n- id: ed4cd-isomap-posub-central\n  statement: In a joint Isomap embedding of tuning curve auto-correlograms, PoSub-HD cells lie\n    nearer the centre of the PoSub-FS distribution than ADN-HD cells.\n  source: Results, Equivalence of PoSub-HD and FS cell tuning in Fourier space, paragraph 6;\n    Extended Data Fig. 4c,d\n  quote: The distribution of PoSub-HD cells occupied the center of the PoSub-FS cell distribution\n    while that of ADN-HD cells was closer to the periphery\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.24921252 version 3, Dataset_5.tar.gz (ADN recordings)\n  depends_on:\n  - cell-classes-counts\n  criterion: As in the Methods and Figure_Fourier.m, Isomap (12 neighbours, 2 dimensions) on the\n    cross-validated auto-correlograms of all FS, PoSub-HD and ADN-HD cells together; Euclidean\n    distance of each HD cell to the mean FS position; Mann-Whitney U of PoSub-HD against ADN-HD\n    (n = 1,602 and 97, z = 4.26, no p printed). Reproduced when p < 0.05 with PoSub-HD distances\n    smaller.\n- id: fig4-random-connectivity-simulation\n  statement: In simulation, random linear combinations of HD-tuned inputs preserve the input\n    population's average Fourier spectrum, and the proportions of outputs dominated by the first\n    three components converge to those of PoSub-FS cells when the s.d. of the weights exceeds\n    their mean.\n  source: Results, PoSub-FS cell tuning reveals key circuit properties, paragraphs 1 and 2; Figure\n    4a-d,g; Extended Data Fig. 5\n  quote: random connectivity preserved the Fourier spectrum of the input population ... This\n    convergence emerged for weight distributions in which the standard deviation (s.d.) exceeded\n    the mean of the weights\n  data: elsewhere\n  where: none deposited; the simulation code (Python, Methods, Data analysis and statistics) is not\n    in figshare doi:10.6084/m9.figshare.24921252 version 3\n  criterion: A result of simulation, not of the recordings. It can be tested only by rerunning a\n    simulation the paper does not fully specify (input tuning widths, number of inputs, the\n    log-normal weight parameters, 30 simulations per point); the author reports it as not testable\n    from the dataset unless the simulation code is found.\n- id: fig4f-synaptic-weights-dispersed\n  statement: Putative synaptic weights from PoSub-HD to PoSub-FS cells, estimated from spike train\n    cross-correlograms, are heavy-tailed with an s.d. larger than their mean, in the range where\n    simulations predict the radial symmetries of FS tuning.\n  source: Results, PoSub-FS cell tuning reveals key circuit properties, paragraph 2; Figure 4e,f;\n    Extended Data Fig. 2f,g\n  quote: The distribution was heavy-tailed (Fig. 4f ), with the ratio of s.d. and mean input weight\n    (i.e. coefficient of variation), in the range where in silico simulation predicted the\n    emergence of radial symmetries\n  depends_on:\n  - cell-classes-counts\n  criterion: Detection from the Methods (Detection of monosynaptic connections) with details from\n    GetSpikeCrosscorrs.m, GetSynapticPairs.m and Figure_SynapticConnections.m. Cross-correlograms\n    in 0.2 ms bins over plus or minus 50 ms (Methods; the code's plus or minus 25 ms is a\n    variant), baseline from convolution with a partially hollowed Gaussian of about 4 ms s.d.\n    (cch_conv, window 41 bins), upper bound the 99th percentile of the Poisson distribution at the\n    largest predicted count within 0 to 2 ms, at least two consecutive bins above it; HD cell as\n    reference with the peak at positive lag, latency above 0.5 ms, no peak at negative lag. Weight\n    as the code's strZ, peak minus prediction over the square root of the prediction (the ratio\n    strR is a variant). The paper prints no CV in the text; Figure 4g and the sentence above make\n    the threshold s.d. greater than the mean. Reproduced when the CV of the weights over all\n    putative HD-to-FS connections exceeds 1 and their skewness is positive.\n- id: fig4h-model-fit\n  statement: A model fit to the PoSub-FS tuning statistics gives near-Gaussian weights from ADN-HD\n    inputs and heavy-tailed weights from PoSub-HD inputs, so that FS tuning is best explained by\n    flat, high-rate ADN input and HD-modulated, low-rate PoSub input.\n  source: Results, PoSub-FS cell tuning reveals key circuit properties, paragraph 3; Figure 4h;\n    Supplementary Methods, Fourier spectrum simulations, Model fitting\n  quote: established that PoSub-FS cell-like outputs are best explained by flat, high firing rate\n    inputs from ADN-HD cells and low firing rate, HD-modulated inputs from PoSub-HD cells\n  data: elsewhere\n  where: none deposited; the fitting code (PyTorch, Supplementary Methods) is not in figshare\n    doi:10.6084/m9.figshare.24921252 version 3\n  criterion: The fit uses the recorded FS, PoSub-HD and ADN-HD tuning curves (the ADN curves only on\n    figshare) and three losses minimized with Adam (learning rate 0.0001, 200,000 steps), the\n    first two scaled by 0.25 of their left-hand side, ADN inputs expanded tenfold by circular\n    shifts (Supplementary Methods). The input numbers and initial values are not given. The author\n    reports it as not testable unless the fitting code is found; a reimplementation would rest on\n    the author's choices.\n- id: ed7-adn-disinhibition\n  statement: Light over ADN in VGAT-Cre mice with ArchT in TRN raises the firing of ADN-HD cells but\n    not of non-HD thalamic cells, without broadening ADN-HD tuning curves.\n  source: Results, PoSub-FS cells receive directionally uniform thalamic input, paragraph 2;\n    Extended Data Fig. 7b-d\n  quote: Targeted illumination of ADN (inactivating the inhibitory presynaptic terminals of the TRN\n    neurons) resulted in a net increase of the firing rates of ADN-HD cells but not of untuned\n    neurons (non-HD cells) recorded in the same sessions\n  statistics:\n  - about: width of ADN-HD tuning curves, baseline against high gain\n    test: Wilcoxon signed rank test\n    statistic: z = 0.67\n    p: 0.5\n    n: 52 ADN-HD cells\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.24921252 version 3, Dataset_6.tar.gz (optogenetics)\n  criterion: Light ON, the 240 one-second pulses; OFF, the 4 s before each pulse onset (Methods;\n    offStart = 4 in Figure_Optogenetics.m). Cells with rate above 0.5 Hz in ON, OFF and baseline\n    (code). Modulation as the ON over OFF rate (code, optoRes); ADN-HD against non-HD,\n    Mann-Whitney U (n = 52 and 75, z = 6.57, no p printed), reproduced when p < 0.05 with ADN-HD\n    higher and ADN-HD median above 1. Width (1 degree bins, 3 degree smoothing) before and during\n    light is a claim of absence judged on the legend's Wilcoxon signed-rank test at p < 0.05; the\n    code's rank-sum test is a variant.\n- id: fig5b-posub-rates-increase\n  statement: Thalamic disinhibition raises the firing rates of PoSub-FS cells, and of PoSub-HD\n    cells, in ArchT mice compared with control-virus mice.\n  source: Results, PoSub-FS cells receive directionally uniform thalamic input, paragraph 3;\n    Figure 5b; Extended Data Fig. 7e,f\n  quote: Similarly to the upstream ADN-HD cells, PoSub-HD and PoSub-FS cells increased their firing\n    rates\n  depends_on:\n  - cell-classes-counts\n  criterion: Opto sessions of PoSub, cells and ON and OFF epochs as in ed7-adn-disinhibition;\n    modulation as the ON over OFF rate (code); ArchT against control, Mann-Whitney U (Extended\n    Data Fig. 7f; PoSub-FS n = 47 and 38, z = 4.99; PoSub-HD n = 83 and 89, z = 1.69; no p\n    printed). The paper's z for PoSub-HD corresponds to a two-tailed p of about 0.09. Reproduced\n    when the FS test gives p < 0.05 with ArchT higher and the ArchT medians of both FS and HD\n    cells exceed 1 and exceed the control medians. If the dandiset lacks the control sessions,\n    only the ArchT medians and a Wilcoxon signed-rank of per-pulse ON against OFF rates (the\n    Methods' light-modulation test) can be shown, and the claim is partially testable.\n- id: ed7gj-tuning-preserved\n  statement: Thalamic disinhibition preserves the HD tuning of PoSub-HD and PoSub-FS cells.\n  source: Results, PoSub-FS cells receive directionally uniform thalamic input, paragraph 3;\n    Extended Data Fig. 7g-j\n  quote: increased their firing rates (Fig. 5b and Extended Data Fig. 7e,f ) while preserving their\n    HD tuning\n  depends_on:\n  - fig5b-posub-rates-increase\n  criterion: Two claims of absence judged on the legends' tests at p < 0.05. PoSub-HD tuning curve\n    width, baseline against high gain, Wilcoxon signed-rank (Extended Data Fig. 7i, z = 0.30; the\n    legend's n = 52 is read as the ArchT PoSub-HD cells, 83 in Fig. 5, and the count found is\n    reported). PoSub-FS baseline against high-gain tuning curve correlation (6 degree bins, no\n    smoothing, as for the gain factors), ArchT against control, Mann-Whitney U (Extended Data\n    Fig. 7j, n = 47 and 38, z = 1.14). Reproduced when neither test finds a difference; the\n    effect sizes are reported.\n- id: fig5e-hd-multiplicative-fs-additive\n  statement: Thalamic gain modulates PoSub-HD cell tuning multiplicatively and PoSub-FS cell tuning\n    additively, so that FS cells receive thalamic input that is uniform across directions.\n  source: Results, PoSub-FS cells receive directionally uniform thalamic input, paragraph 4;\n    Figure 5c-e; Extended Data Fig. 8a,b\n  quote: The modulation of PoSub-HD cells was purely multiplicative ... In contrast, modulation of\n    PoSub-FS cell tuning was exclusively additive\n  depends_on:\n  - fig5b-posub-rates-increase\n  criterion: Per the Methods (Gain modulation analysis, experiment) and Figure_Optogenetics.m. ON\n    and OFF tuning curves in 6 degree bins, unsmoothed, without speed threshold, both divided by\n    the maximum of the OFF curve; linear fit of ON on OFF (polyfit), slope the multiplicative and\n    intercept the additive factor. ArchT cells excluded, by the Methods, when they show neither a\n    significant light modulation (Wilcoxon signed-rank of per-pulse ON against preceding OFF\n    rates, p < 0.05) nor a significant ON-OFF tuning correlation (Pearson, p < 0.05). The sentence\n    reads \"did not show ... and did not show\", so the readings are (a) exclusion when both fail\n    and (b) when either fails; the code (c) excludes on the correlation alone. The paper excluded\n    1 of 47 FS cells and no other cells. Tests, Mann-Whitney U, ArchT PoSub-HD against PoSub-FS\n    (Fig. 5e, additive z = 7.72, multiplicative z = 5.99; legend n = (83, 52), read as 83 and 46);\n    each against control (Extended Data Fig. 8a, HD additive z = 1.57, multiplicative z = 6.80;\n    8b, FS additive z = 4.16, multiplicative z = 0.36; no p printed). Reproduced when, under every\n    reading, HD multiplicative factors exceed FS ones and FS additive factors exceed HD ones (p <\n    0.05), HD multiplicative and FS additive factors exceed control (p < 0.05), and HD additive and\n    FS multiplicative factors do not differ from control (p of 0.05 or more). Partially\n    reproduced when the HD against FS comparisons hold and the control comparisons cannot be run\n    or do not all hold.\n- id: ed8cd-multiplicative-detectable\n  statement: Simulations of noisy gain on real FS tuning curves show that multiplicative gain would\n    be detectable at the FS cells' tuning correlations, and the FS data are best explained by\n    additive gain.\n  source: Results, PoSub-FS cells receive directionally uniform thalamic input, paragraph 4;\n    Methods, Gain modulation analysis, simulations; Extended Data Fig. 8c,d\n  quote: These simulations allowed us to establish that multiplicative gain is indeed detectable in\n    tuning curves with correlation values similar to those observed experimentally in PoSub-FS\n    cells and that our experimental results in PoSub-FS cells are best explained by significant\n    additive gain\n  depends_on:\n  - fig5e-hd-multiplicative-fs-additive\n  criterion: Per the Methods and Duszkiewicz2024_Figure_GainSimulation.m. ArchT FS baseline curves;\n    simulated high-gain curves with no gain, with multiplicative gain (times 1.2) or additive gain\n    (plus 20% of the curve's maximum) before Gaussian noise titrated to the observed distribution\n    of baseline-high-gain correlations; factors computed as for the data; each simulation's factor\n    distributions against the control group's, Mann-Whitney U (n = 46 and 38). Reproduced when the\n    multiplicative simulation's multiplicative factors differ from control (p < 0.05) and the\n    additive simulation's factors match the data's pattern (additive differs, multiplicative does\n    not). The noise seed is a standard choice.\n- id: ed8e-adn-mixed-gain\n  statement: ADN-HD cells show multiplicative factors like those of PoSub-HD cells and larger\n    additive factors.\n  source: Results, PoSub-FS cells receive directionally uniform thalamic input, paragraph 4;\n    Extended Data Fig. 8e,f\n  quote: this high degree of multiplicative modulation largely reflected the modulation of the\n    upstream ADN-HD cells\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.24921252 version 3, Dataset_6.tar.gz (optogenetics)\n  depends_on:\n  - fig5e-hd-multiplicative-fs-additive\n  criterion: Factors as in fig5e-hd-multiplicative-fs-additive. ADN-HD against PoSub-HD,\n    Mann-Whitney U (multiplicative z = 0.55, additive z = 5.07; no p printed). Reproduced when\n    the multiplicative factors do not differ (p of 0.05 or more, a claim of absence on the\n    paper's test) and the additive factors do (p < 0.05, ADN higher, as the Extended Data Fig. 8\n    title says ADN-HD cells show a mixture of both).\n- id: fig6c-coupling-preserved-wake-rem\n  statement: GLM cross-coupling of PoSub-HD pairs, PoSub-FS pairs and PoSub-HD to PoSub-FS pairs is\n    preserved between wakefulness and REM sleep, less for FS pairs than for HD pairs.\n  source: Results, PoSub-FS cells are coupled to the PoSub-HD ring manifold, paragraph 2; Figure\n    6a-c\n  quote: Similarly, PoSub-FS cell pairs also preserved their coupling across WAKE and REM, albeit to\n    a smaller degree than PoSub-HD cell pairs (Fig. 6a-c , middle). Notably, the coupling of the\n    two cell populations to each other was also preserved across WAKE and REM\n  depends_on:\n  - cell-classes-counts\n  criterion: Sessions with at least 100 s of REM (Methods). GLM per the Methods and\n    GetGLM_Forward.m and GetGLM_Reverse.m. Spike counts in 100 ms bins smoothed with a 100 ms s.d.\n    Gaussian; the population rate (all units) smoothed alike and z-scored; cell B's train z-scored;\n    Poisson GLM (log link) of cell A on population rate and cell B within WAKE (the square epoch)\n    or REM; the coefficient at lag 0 averaged with the reversed pair's; pairs with fit warnings\n    removed. Pearson correlation across pairs of WAKE against REM coefficients for HD-HD, FS-FS and\n    HD-FS pairs (n = 34,270, 2,492 and 8,992; no r or p in the text). Reproduced when all three\n    correlations are positive with p < 0.05 and the FS-FS r is below the HD-HD r. The HD-FS count\n    is read as either ordering of the pair (code, both ordered sets) or one per pair; Extended\n    Data Fig. 9d gives 18,992, so both counts are shown.\n- id: ed9d-coupling-follows-tuning\n  statement: The polarity of the GLM coupling within a pair depends on the similarity of the two\n    cells' HD tuning, during both WAKE and REM.\n  source: Results, PoSub-FS cells are coupled to the PoSub-HD ring manifold, paragraph 2; Extended\n    Data Fig. 9d\n  quote: Predictably, the polarity of the cross-coupling coefficient depended on the HD tuning\n    relationship within each cell pair during both WAKE and REM\n  depends_on:\n  - fig6c-coupling-preserved-wake-rem\n  criterion: As in Figure_GLMRemWake.m, Pearson correlation across pairs between the zero-lag\n    tuning curve correlation and the lag-0 coupling coefficient, for HD-FS and FS-FS pairs, in\n    WAKE and in REM (n = 18,992 and 2,492). Reproduced when all four correlations are positive\n    with p < 0.05.\n- id: fig7b-wake-isomap-tuning\n  statement: HD tuning curves of PoSub-HD and PoSub-FS cells computed from the virtual HD of the\n    WAKE ring manifold are equivalent to those computed from the real HD.\n  source: Results, PoSub-FS cells are coupled to the PoSub-HD ring manifold, paragraph 3; Figure\n    7a,b; Extended Data Fig. 10e\n  quote: The HD tuning curves of both PoSub-HD and PoSub-FS cells computed using virtual HD values\n    during WAKE were equivalent to those computed using real HD values\n  depends_on:\n  - cell-classes-counts\n  criterion: Per the Methods (Visualization and analysis of the ring manifold). HD cell spikes over\n    the whole square epoch in 200 ms bins, smoothed with a 400 ms s.d. Gaussian, square root;\n    Isomap with 12 neighbours and 3 dimensions; virtual HD the four-quadrant arctangent of the\n    first two dimensions, its direction chosen by the smaller circular variance of the difference\n    from real HD, its origin by the mean offset of maximum cross-correlation over HD cells; real\n    and virtual tuning curves in 1 degree bins, 3 degree smoothing, real HD downsampled to 200 ms.\n    Zero-lag Pearson correlation of each cell's real and virtual curves against the time-reversed\n    Isomap angle control, Wilcoxon signed-rank (HD n = 1,602, z = 34.7; FS n = 427, z = 17.9; no p\n    printed). Reproduced when both give p < 0.05 with real correlations higher.\n- id: ed10b-ring-topology\n  statement: Population vectors of PoSub-HD cells lie on a ring during WAKE, farther from the\n    centre of the manifold than shuffled vectors, and the ring has the same radius during REM.\n  source: Extended Data Fig. 10b,d; Figure 7c legend\n  quote: Distance of population vectors to the center of the manifold ( d ) is the same during WAKE\n    and REM\n  depends_on:\n  - fig7b-wake-isomap-tuning\n  criterion: Per the Methods and the Isomap scripts, distance of each point to the manifold centre,\n    normalized to the mean distance of the real projection; shuffles by shifting each cell's\n    binned train by a random number of bins. Mean distance real against shuffled, Wilcoxon\n    signed-rank across sessions (n = 32, z = 4.79), reproduced when p < 0.05 with real larger.\n    REM against subsampled WAKE in the joint embedding is a claim of absence on the legend's\n    Wilcoxon signed-rank (n = 26, z = 0.17), reproduced when p is 0.05 or more. The shuffle and\n    subsampling seeds are standard choices.\n- id: fig7d-rem-isomap-tuning\n  statement: During REM sleep the HD tuning of PoSub-HD and PoSub-FS cells can be estimated from\n    the virtual HD of the ring manifold alone and matches their WAKE tuning.\n  source: Results, PoSub-FS cells are coupled to the PoSub-HD ring manifold, paragraph 4; Figure\n    7c,d; Extended Data Fig. 10f\n  quote: Notably, HD tuning of PoSub-FS cells could also be accurately estimated during REM based\n    solely on the virtual HD obtained from the HD ring attractor manifold\n  depends_on:\n  - fig7b-wake-isomap-tuning\n  criterion: Sessions with at least 100 s of REM. WAKE population vectors randomly subsampled to the\n    number of REM vectors, Isomap on both together, virtual HD as in fig7b-wake-isomap-tuning;\n    tuning curves in 6 degree bins with 6 degree smoothing. Cells with REM rate above 0.5 Hz (HD)\n    or above 10 Hz (FS), as Figure_IsomapREM.m selects them (expected n = 1,148 and 317). Zero-lag\n    Pearson correlation of WAKE and REM curves against the time-reversed control, Wilcoxon\n    signed-rank (HD z = 29.2, FS z = 10.4; no p printed). The WAKE curve is read as the WAKE\n    Isomap curve (legend) and as the real-HD WAKE curve (the code's cc_WkRem); both are run.\n    Reproduced when, under both readings, both tests give p < 0.05 with real correlations higher.\n- id: fig1ac-posub-border\n  statement: Along a Neuropixel probe crossing pRSC and PoSub, HD tuning of excitatory cells rises\n    in a step at the functional border between the two regions.\n  source: Results, High-density recordings in the PoSub of freely moving mice, paragraph 1; Figure\n    1a-c\n  quote: We first established the functional border between PoSub and posterior retrosplenial\n    cortex (pRSC) using a Neuropixel linear electrode array\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.24921252 version 3, Dataset_4.tar.gz (Neuropixel session)\n  criterion: The paper reports no measure or test of the step. HD information of excitatory cells\n    against probe position, with a running average, as Duszkiewicz2024_Figure_SingleRec_NPX.m\n    plots it. Reproduced when the running average of HD information is higher on the PoSub side\n    of the border than on the pRSC side by a Mann-Whitney U test at p < 0.05, the border placed\n    where the code places it.\n- id: ed6-trn-innervates-adn\n  statement: TRN sends denser inhibitory projections to ADN than to the other rostral thalamic\n    nuclei.\n  source: Results, PoSub-FS cells receive directionally uniform thalamic input, paragraph 2;\n    Extended Data Fig. 6\n  quote: The ADN is strongly innervated by inhibitory afferents from the thalamic reticular nucleus\n  statistics:\n  - test: repeated measures ANOVA\n    statistic: F (2,9) = 44.9\n    p: 1.0e-4\n    p_relation: \"<\"\n    n: 4 mice\n  data: elsewhere\n  where: none deposited; anatomical images are not in the dandiset or the figshare item\n  criterion: Anatomy (ImageJ intensity of GFP in ROIs per nucleus) on images the paper does not\n    deposit. Not testable from the dataset.\n"
}
```

```
File created successfully at: claims/000939/10.1038-s41593-024-01588-5.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000939/10.1038-s41593-024-01588-5.yaml paper/10.1038-s41593-024-01588-5.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Every quote and value passed. Checking the prose rules (no em dashes, no "rather").

**Agent calls Bash**

```bash
cd  grep -n -E "—|rather" claims/000939/*.yaml; grep -c "^- id:" claims/000939/*.yaml; grep -c "  statistics:" claims/000939/*.yaml; grep -c "  criterion:" claims/000939/*.yaml; grep -c "data: elsewhere" claims/000939/*.yaml; git status --short
```

```
34
6
34
12
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
?? claims/000939/
?? scripts
```

**Agent**

I wrote `claims/000939/10.1038-s41593-024-01588-5.yaml`. The quote checker passes it with no problems: 34 claims, 34 quotes, 9 statistical values found in the text. Nothing is committed.

**Text read.** The version of record from Europe PMC (PMC11001581): main text, figure legends, Methods and Extended Data legends. Both supplements were there: the Supplementary Methods on model fitting and theory, and the Reporting Summary. The main article's PDF was not supplied, so I never saw the figures. Values printed only on figure panels are not recorded, for example the r values of Fig. 6c, the CV of Fig. 4f and most p-values.

**Code read.** figshare doi:10.6084/m9.figshare.24921252, version 3: `MatlabCode_Duszkiewicz2024.zip` (md5 8f391dec…) and `SessionLists_ForAnalysis.zip`. It has the MATLAB code for every analysis except the simulations. The Python code for the simulations and the model fit (Fig. 4, Extended Data Fig. 5) is not deposited.

**Claims.**
- **Counts:** all 34 have quotes, none is `inferred`, and all 34 have criteria.
- **Statistics:** only 6 claims have a statistics entry. Most legends print a z value and no p-value, and the schema needs a p or an interval, so those z values are written into the criteria.
- **Data:** 22 claims use the dataset. 12 use data held elsewhere: ADN, cue rotation, Neuropixel and ADN opto data on figshare, plus the simulations, the model fit and the anatomy, which are not deposited anywhere.

**Where the Methods and code disagree.** The Methods are followed and the code's choice is named as a variant:
- **Cell classes:** the trough-to-peak cut is 0.4 ms in the Methods and 0.35 ms in the code.
- **KL divergence direction:** the Methods give D_KL(σ_i‖S); the code computes D_KL(S‖σ_i).
- **Smoothing in the stability analyses:** 3° in the Methods, 2° in the code.
- **Width tests (ED Fig. 7d,i):** the legends say Wilcoxon signed-rank; the code uses a rank-sum test.
- **Cross-correlogram window:** ±50 ms in the Methods, ±25 ms in the code.
- **Multipeak filter:** the code as shipped drops multipeaked HD cells from every Fourier analysis. The legends' n = 1,602 shows Fig. 3 used all HD cells, so the filter is treated as the ED Fig. 3k control only.

**Details left open, with the readings named for each:**
- **Fourier power:** the squared modulus (what the code computes, and what the Parseval check needs) or the root mean square (the Methods' wording).
- **HD threshold:** a fixed 0.2 bits per spike, or the 99th percentile computed from the time-reversed controls. The HD fraction is 87% in the Results and 85% in the Methods.
- **Opto exclusion:** the Methods' sentence allows excluding cells that fail both tests or either test; the code uses the correlation test alone.
- **Cue rotation exclusion:** an epoch is dropped if it fails either condition, or both.
- **ED Fig. 3g distance:** the KL divergence the legend names, or the Euclidean distance the code uses.
- **"Similar" proportions (Fig. 3h):** the same rank order, or each within 10%.
- **"The cell population" for the 98% power figure:** FS and HD cells pooled, or each separately.
- **REM comparison (Fig. 7d):** the WAKE Isomap curve (legend) or the real-HD WAKE curve (code).
- **HD-FS pair count:** 8,992 in Fig. 6c against 18,992 in ED Fig. 9d.
- **Legend n values that look like slips:** n = 52 in ED Fig. 7i and n = (83, 52) in Fig. 5e, read as 83 and 46.
- **Decoding:** the Methods give no decoder; the code settles it.

**Missing from the paper.**
- **Simulation and model-fit code:** not deposited. The two claims built on them (Fig. 4a–d,g and Fig. 4h) can't be tested from the recordings.
- **Anatomy images (ED Fig. 6):** not deposited.
- **Session coverage:** the dandiset holds 31 of the paper's 32 PoSub sessions. Whether it has the control-virus opto sessions is for the author to find.

## End of run

53 turns, 9 minutes, result: success.
