# okuno-2025 · claims · run 42756915076

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ | grep -i okuno; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ | grep -i okuno; wc -l claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper/ | grep -i -E "okuno|107990"; ls paper | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml; wc -c paper/*; cat papers/datasets/okuno-2025.yaml 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.107990.1.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 400,592p paper/10.7554-elife.107990.1.txt | grep -v "^\[" | grep -v "Google Scholar" | grep -v "^$" | head -50; ls tools/; git log --oneline -3 -- claims/ | head; ls claims | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/takuto-okuno-riken/flywalk && cd flywalk && git log -1 --format="%H %ci" && ls && find . -type f | grep -v .git/ | wc -l
```

```
29c4e32d18d355d3d76e6a14aed8c113bf70989b 2026-06-12 17:29:25 +0900
LICENSE
README.md
analyzeFuncConnectivity.m
analyzeFuncConnectivityFixNc.m
analyzeNeuralFC.m
analyzeStructConnectivity.m
atlas
checkBehavior.m
checkHistogram.m
data
extractNeuralTimeseries.m
extractROItimeseries.m
getSCconfig.m
glmFlyMB1st.m
glmFlyMB2nd.m
hemi1_2matToFlywireCompatible.m
lib
makeAtlasNiftiFiles.m
makeNeuralSC.m
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && cat README.md && git log --format="%h %ci %s" | head -40 && ls lib data results template atlas | head -80
```

```
[![License: MIT](https://img.shields.io/badge/License-MIT-success.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15532271.svg)](https://doi.org/10.5281/zenodo.15532271)

# Fly FC-SC analysis scripts
Scripts for a manuscipt of ["Functional connectivity, structural connectivity, and inter-individual variability in Drosophila melanogaster,"](https://elifesciences.org/reviewed-preprints/107990v1)
Takuto Okuno, Alexander Woodward, Hideyuki Okano, Junichi Hata (2025) eLife

<div align="center">
<img src="data/img/fig1.jpg" width="70%">
</div>

## Requirements: Software
* MATLAB R2021b or later
* Parallel Computing Toolbox ver7.1 or later


## Installation
1. Download this code zip file.
2. Extract zip file under your working directory <work_path>.
3. Run the MATLAB software, and "Add Path" extracted directories (i.e. <work_path>/flywalk-main).
[... 212 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && git log --format="%h %ci %s" --before=2025-10-10 | head -5; git log --format="%h %ci %s" --before=2025-07-05 | head -3; git log --format=%h | wc -l
```

```
4b92add 2025-08-11 15:48:53 +0900 fixed default clustering edge.
6e51c95 2025-06-27 15:03:27 +0900 Update README.md
1227dc1 2025-05-28 15:16:49 +0900 Update README.md
49b6038 2025-05-09 13:57:45 +0900 Update README.md
9f86c67 2025-05-08 20:32:58 +0900 fixed comments.
6e51c95 2025-06-27 15:03:27 +0900 Update README.md
1227dc1 2025-05-28 15:16:49 +0900 Update README.md
49b6038 2025-05-09 13:57:45 +0900 Update README.md
367
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && git checkout -q 4b92add && wc -l *.m lib/*.m | sort -n | tail -50
```

```
21 lib/getNuisanceRegressionOut.m
    24 lib/colormapGen.m
    24 lib/plotSwc.m
    30 makeSCweightMatrixLarge.m
    34 lib/getNuisanceMeanTimeSeries.m
    36 lib/calcGlobalClusteringCoeff.m
    36 lib/regressPrepare.m
    38 lib/calcGlmContrastImage.m
    39 lib/generateCFGgraph.m
    40 makeAtlasNiftiFiles.m
    41 lib/calcGlmMixedTukey.m
    43 lib/calcShowGroupROCcurve.m
    43 lib/getNuisancetCompCor.m
    48 checkHistogram.m
    55 lib/getNuisanceaCompCor.m
    58 getSCconfig.m
    62 checkBehavior.m
    75 lib/regressLinear.m
    77 lib/estimateSmoothFWHM.m
    84 lib/plotNifti3DZSlice.m
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && cat glmFlyMB1st.m checkBehavior.m lib/getGlmCRF.m
```

```
% GLM for drosophila movement behavior
% single session. with Tukey 8 window
function glmFlyMB1st
    %%%%%%%%%%%%%% set parameters %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % pre-process
    preproc = 'ar'; % for move correct, slice time correct
%    preproc = 'r'; % for move correct only

    % output time-series (smoothing, highpass filter, nuisance removal)
    hpfTh = 0; % high-pass filter threshold
    smooth = 's80';
    nuisance = 'poltcomp';

    TR = 1 / 1.879714;
    tuM = 8; % tukey window size
    %%%%%%%%%%%%%% set parameters %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    hpfstr = '';
    if hpfTh > 0, hpfstr = ['hf' num2str(round(1/hpfTh))]; end

[... 251 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && cat glmFlyMB2nd.m; sed -n 1,140p extractROItimeseries.m
```

```
% GLM for drosophila movement behavior
% multi-subject. mixed-effects with Tukey-Taper.
function glmFlyMB2nd
    %%%%%%%%%%%%%% set parameters %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % pre-process
    preproc = 'ar'; % for move correct, slice time correct
%    preproc = 'r'; % for move correct only

    % output time-series (smoothing, highpass filter, nuisance removal)
    hpfTh = 0; % high-pass filter threshold
    smooth = 's80';
    nuisance = 'poltcomp'; % ''; %

    tuM = 8; % tukey window size
    %%%%%%%%%%%%%% set parameters %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    hpfstr = '';
    if hpfTh > 0, hpfstr = ['hf' num2str(round(1/hpfTh))]; end

    path = 'results/glm/';
[... 247 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 140,331p extractROItimeseries.m; cat lib/getNuisancePolynomial.m lib/getNuisancetCompCor.m lib/getNuisanceRegressionOut.m
```

```
for h=1:length(hpfTh)
                hpfstr = '';
                if hpfTh(h) > 0, hpfstr = ['hf' num2str(round(1/hpfTh(h)))]; end
        
                for k=1:length(smooth)
                    for n=1:length(nuisance)
                        CX = {}; CXm = {};
                        % load file
                        outfname = ['results/ts/' smooth{k} hpfstr nuisance{n} preproc roitypes{ii} '-ts.mat'];
                        if exist(outfname,'file')
                            load(outfname);
                        end
                        if length(CX) < i
                            % smoothing
                            Vk = V;
                            if ~isempty(smooth{k}) > 0 && (strcmp(smooth{k}(1),'s') || strcmp(smooth{k}(1),'m'))
                                % gaussian filter
                                sz = str2double(smooth{k}(2:end));
                                FWHM = [(sz/10)/(2.45/2.28) sz/10 (sz/10)/(3.715/2.28)]; % voxel size;
                                sigma = FWHM / sqrt(8*log(2));
[... 251 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && grep -n -i -E "atanh|corr\(|score|auc|perfcurve|ranksum|log10|log\(|Inf|prctile|normcdf|bonf|ttest" analyzeFuncConnectivity.m | head -80
```

```
119:    %to check scatter and AUC graph (need to comment out plot lines)
135:    AUCVER = 3;
172:            r = corr(W2b(:),C2b(:));    % corr between neurons v. synapse weight
176:        r = corr(Sb(:),C2b(:));    % corr between neurons v. synapse weight
184:    lC2 = log10(C2); lC2(lC2<0) = 0;
185:    lS = log10(S); lS(lS<0) = 0;
186:    lW2 = log10(W2); lW2(lW2<0) = 0;
187:    lC2b = log10(C2b); lC2b(lC2b<0) = 0;
188:    lSb = log10(Sb); lSb(lSb<0) = 0;
189:    lW2b = log10(W2b); lW2b(lW2b<0) = 0;
193:    if ~exist('results/auc','dir'), mkdir('results/auc'); end
198:    AUC = [];
214:                    CM{i} = single(corr(CX{sbjids(i)})); %calcPartialCorrelation_(CX{i}',[],[],[],false,1e-3);
234:                F3z = atanh(F3); % z transformed (better FC-SC corr).
239:                mFz(isinf(mFz)) = max(mFz(~isinf(mFz)));
243:                T3(isinf(T3)) = max(T3(~isinf(T3)));
245:                lT3 = log(T3); lT3(lT3<0) = 0;
247:                % each flys [log10(neurons) vs. m-FCz]
250:                    Dz(isinf(Dz)) = max(Dz(~isinf(Dz)));
251:                    sbjR(k,i) = corr(lC2(:),abs(Dz(:)));
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 130,250p analyzeFuncConnectivity.m; sed -n 354,524p analyzeFuncConnectivity.m
```

```
end
    end
end

function analyzeFcROItype(roitype, preproc, hpfTh, smooth, nuisance, sbjids, isplot)
    AUCVER = 3;

    % load structural connectivity matrix (from makeStructConnectivity.m)
    switch(roitype)
    case 'hemiroif'
        load('results/sc/hemiroi_connectlist.mat');
        ids = 1:roiNum;
    otherwise
        roitype = lower(roitype);
        load(['results/sc/' roitype '_connectlist.mat']);
        ids = primaryIds;
    end

    nweightMat(isnan(nweightMat)) = 0;
    isw2 = ~isempty(nweightMat);
[... 273 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && grep -n -i -E "score|ranksum|bonf|normcdf|norminv|1.67|fitdist|ttest|perm|null|rand" plotFuncConnectivity.m | head -80
```

```
33:    % roitype: FlyEM,FlyEMFw,Branson,BransonFw,Cm,CmFw,CmR1w1,Dist,Rand,Vrand
37:    % roitype: Branson,Cm,CmR1w1,Dist,Rand,Vand
42:    % roitype: FlyEM,FlyEmFw,Branson,Cm,CmR1w1,Dist,Rand,Vrand
46:    % roitype: Branson,Cm,CmR1w1,Dist,Rand,Vand
97:%    checkReciprocalDistanceRandByHemiroi(vslabels);
101:%    checkSeparationRandByHemiroi(vslabels);
103:%    checkRandSubsampleByHemiroi(vslabels); % find good rand param of permutation test of separation index & reciprocal
105:    checkRandSubsampleRankTestByHemiroi(vslabels); % show permutation test results (figure.4)
109:%    checkReciprocalDistanceRandByDistKm(vslabels);
119:    roitypes = {{'hemiBranson7065km',''},{'hemiCmkm',''},{'hemiCmkm','r1w1'},{'hemiDistKm',''},{'hemiRand',''},{'hemiVrand',''}};
120:    roitypelabels = {'Branson','Cm','CmR1w1','Dist','Rand','Vand'};
189:    roitypes = {'hemiroi','hemiroi_fw0sr50','hemiBranson7065km50','hemiCmkm50','hemiCmkm50r1w1','hemiDistKm50','hemiRand50','hemiVrand50'};
190:    roitypelabels = {'FlyEM','FlyEMFw','Branson','Cm','CmR1w1','Dist','Rand','Vrand'};
412:function checkReciprocalDistanceRandByHemiroi(vslabels)
422:%        {'hemiroi','_hb0sr80_rc10000'},{'hemiroi','_hb0sr80_rc10000_rand1'},{'hemiroi','_hb0sr80_rc10000_rand2'},{'hemiroi','_hb0sr80_rc10000_rand3'}, ...
423:%        {'hemiroi','_hb0sr80_rc10000_xrand1'},{'hemiroi','_hb0sr80_rc10000_xrand2'},{'hemiroi','_hb0sr80_rc10000_xrand3'}, ...
424:%        {'hemiroi','_hb0sr80fw_rc20_xorand1'},{'hemiroi','_hb0sr80fw_rc20_xorand2'},{'hemiroi','_hb0sr80fw_rc20_xorand3'}, ...
425:%        {'hemiroi','_hb0sr80_rc20_xorand1'},{'hemiroi','_hb0sr80_rc20_xorand2'},{'hemiroi','_hb0sr80_rc20_xorand3'}, ...
426:%        {'hemiroi','_hb0sr80_rc10000_xorand1'},{'hemiroi','_hb0sr80_rc10000_xorand2'},{'hemiroi','_hb0sr80_rc10000_xorand3'}, ...
427:%        {'hemiroi','_fw0sr140_rc10000'},{'hemiroi','_fw0sr140_rc10000_rand1'},{'hemiroi','_fw0sr140_rc10000_rand2'},{'hemiroi','_fw0sr140_rc10000_rand3'}, ...
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 1180,1260p plotFuncConnectivity.m; grep -n -E "\- ?0\.5|\(AA|R\(.*\+.*A|nanmean\(.*AUC" plotFuncConnectivity.m | head -30
```

```
aucmat = ['results/auc/' pftype '-fcauc.mat'];
                        if exist(aucmat,'file')
                            load(aucmat);
                        else
                            A = nan(size(Am,1),100);
                            R = nan(1,size(Rm,1));
                            SR = nan(1,size(SRm,1));
                        end
                        AA = cat(3,AA,A);
                        Am = [Am,nanmean(A,2)];
                        Am2 = [Am2,nanmean(A(I,:),2)];
                        Rm = [Rm,R(:)];
                        Rm2 = [Rm2,R(I)'];
                        SRm = [SRm,SR(:)];
                        SRm2 = [SRm2,SR(I)'];
                    end
                    R3r = [R3r;Rm2]; SR3r = [SR3r;SRm2]; A3r = [A3r;Am2];
                end
            end
        end
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && grep -n "sbjids\s*=" *.m | head; grep -n -B3 -A30 "^function analyzeFuncConnectivity" analyzeFuncConnectivity.m | head -80
```

```
analyzeFuncConnectivity.m:37:    sbjids = [1 2 3 4 5 6 8 9];
analyzeFuncConnectivityFixNc.m:28:    sbjids = [1 2 3 4 5 6 8 9];
analyzeNeuralFC.m:16:    sbjids = [1 2 3 4 5 6 8 9];
1-% analyze functional connectivity matrix (1st and 2nd level analysis).
2-% this script should run after makeVoxelROIatlas.m, makeStructConnectivity.m, extractROItimeseries.m first.
3-
4:function analyzeFuncConnectivity
5-    %%%%%%%%%%%%%% set parameters %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
6-    % pre-process
7-    preproc = 'ar'; % for move correct, slice time correct
8-%    preproc = 'r'; % for move correct only
9-
10-    % output time-series (smoothing, highpass filter, nuisance removal)
11-    hpfTh = [0]; % high-pass filter threshold
12-%    hpfTh = [0, 0.1, 0.05, 0.025, 0.02, 0.01, 0.009, 0.008, 0.005, 0.001]; % high-pass filter threshold
13-%    smooth = {'', 's10', 's20', 's30', 's40', 's50', 's60', 's70', 's80'};
14-    smooth = {'', 's10', 's20', 's30', 's40', 's50', 's60', 's70', 's80', 's90', 's100', 's110', 's120', 's130', 's140', 's150', 's160', 's170', 's180', 's190', 's200', 's210', 's220', 's230', 's240', 's250', 's260', 's270', 's280', 's290', 's300'};
15-%    smooth = {'', 's30', 's80'}; %, 's150','s230','s300'};
16-%    smooth = {'', 's30', 's40', 's60', 's80', 's100', 's150'};
17-%    smooth = {'s230'}; % DistKm
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -E "with_labels|with_inputs|elsewhere" docs/protocol.md docs/*.md | head -30
```

```
docs/protocol.md:149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:156:     rests on it. A claim on data in none of them is `data: elsewhere`, or
docs/protocol.md:161:     recordings of its own, or on other data, are `data: elsewhere` when they
docs/protocol.md:233:4. Decide what comes from outside the dataset. Data from elsewhere may be
docs/protocol.md:242:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:243:     `with_inputs` and `elsewhere` claims are counted apart, each group on
docs/protocol.md:245:   - `with_labels` is for outside sources that only name or map codes the
docs/protocol.md:267:   - `elsewhere` is for a claim whose data the dataset does not hold at
docs/protocol.md:276:   - The notes of a `with_inputs` claim say which side a difference comes
docs/protocol.md:287:     `data: elsewhere` instead (step 4).
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
docs/pilot-notes.md:95:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:107:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:123:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:162:adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
docs/pilot-notes.md:166:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/pipeline.md:49:`other_data` (a research paper whose data are elsewhere; `data_in` says where),
docs/pipeline.md:68:aside, are mostly on data elsewhere stops the chain before its checkpoint.
docs/protocol.md:149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:156:     rests on it. A claim on data in none of them is `data: elsewhere`, or
[... 8 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 230,
 "limit": 60
}
```

```
230	   unless an earlier one matches the claims file's description better. Say
231	   why in the notebook's header. If versions differ in content the analysis
232	   uses, show the difference.
233	4. Decide what comes from outside the dataset. Data from elsewhere may be
234	   used only when the claims file says the paper relies on it, it is public,
235	   and it is pinned: a DOI, or a repository at a commit. Record each under
236	   `inputs` in the attempt. A claim whose outside input is not public is
237	   blocked with `data_missing`, and its notes say where you looked.
238	
239	   The registry judges the dataset, so claims that use outside data are
240	   kept apart:
241	   - Each claim says what its test uses: `data: dataset` (the default),
242	     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
243	     `with_inputs` and `elsewhere` claims are counted apart, each group on
244	     its own; the others count towards what is said about the dataset.
245	   - `with_labels` is for outside sources that only name or map codes the
246	     dataset already holds, such as stimulus names for its stimulus codes.
247	     They bring in no measurements. A link claim must confirm the names, and
248	     the missing names are recorded as a finding (`metadata_insufficient`).
249	   - When outside data has to be matched to the dataset's cells, sessions
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "with_inputs" claims/*.yaml | head -3; grep -n -A4 "data: elsewhere" claims/*.yaml | head -30; grep -rn "inputs:" claims/*.yaml | head -5
```

```
claims/alasfour-2024.yaml
claims/amjad-2025.yaml
claims/bellvila-2026.yaml
claims/azcorra-2023.yaml:729:  data: elsewhere
claims/azcorra-2023.yaml-730-  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
claims/azcorra-2023.yaml-731-  expected:
claims/azcorra-2023.yaml-732-  - quantity: Nuclei after quality control
claims/azcorra-2023.yaml-733-    value: 12065
--
claims/azcorra-2023.yaml:750:  data: elsewhere
claims/azcorra-2023.yaml-751-  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
claims/azcorra-2023.yaml-752-  depends_on:
claims/azcorra-2023.yaml-753-  - snrna-nuclei-qc
claims/azcorra-2023.yaml-754-  criterion: Without clustering, from raw counts of the nuclei that pass quality control, a
--
claims/azcorra-2023.yaml:774:  data: elsewhere
claims/azcorra-2023.yaml-775-  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
claims/azcorra-2023.yaml-776-- id: scrna-meta-integration
claims/azcorra-2023.yaml-777-  statement: Integrating four published single-cell datasets gives eight clusters, one of them
claims/azcorra-2023.yaml-778-    defined by co-expression of Aldh1a1 and Anxa1.
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B2 -A12 "data: with_inputs" claims/alasfour-2024.yaml | head -60; head -40 claims/alasfour-2024.yaml
```

```
251-  quote: we observe that the highest classification performance is 69% for the high γ band in the
252-    inferior temporal lobe
253:  data: with_inputs
254-  expected:
255-  - quantity: participant-wide accuracy, high gamma, inferior temporal
256-    value: 69
257-    tolerance: 6.9
258-    unit: '%'
259-  criterion: Accuracy of a feature is the mean of its 35 fold accuracies (M5, M6), under the
260-    readings of O5, O6, O7. Reproduced when, under one reading, high gamma in the inferior
261-    temporal lobe has the highest mean of the 40 features and its value is within tolerance;
262-    partially reproduced when the value is within tolerance but another feature is higher.
263-- id: fig2-rois-three-bands
264-  statement: The postcentral gyrus, supramarginal gyrus and superior, middle and inferior
265-    temporal lobes each have three or more bands with accuracy significantly above chance.
--
268-    lobes have 3 or more frequency bands where the LDA classification performance is
269-    significantly above chance.
270:  data: with_inputs
271-  criterion: Significance per M6, with the chance level and test under O9, folds under O7, ROI
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && grep -n -i -E "ppssi|dbscan|syMIXscore|sepscore|mixscore" makeNeuralSC.m plotNeuralFC.m | head -40
```

```
makeNeuralSC.m:4:    % DBscan param
makeNeuralSC.m:20:        checkNeuralDBScanFw(conf, epsilon*i, minpts);
makeNeuralSC.m:99:        checkNeuralDBScanFw(conf, epsilon*i, minpts);
makeNeuralSC.m:397:function checkNeuralDBScanFw(conf, epsilon, minpts)
makeNeuralSC.m:400:    fname = ['results/neuralsc/' conf.scname num2str(synTh) 'sr' num2str(scoreTh) '_neuralDBScan' num2str(epsilon) 'mi' num2str(minpts) '.mat'];
makeNeuralSC.m:433:        dbidx = int32(dbscan(X,epsilon,minpts)); % nanometer
makeNeuralSC.m:454:        disp(['dbscan ' conf.scname num2str(synTh) 'sr' num2str(scoreTh) ' : process (' num2str(i) ') nid=' num2str(Nid(i)) ', clsz=' num2str(clsz) ' (' num2str(inOnly) ', ' num2str(outOnly) ')']);
makeNeuralSC.m:482:    load(['results/neuralsc/' conf.scname num2str(synTh) 'sr' num2str(scoreTh) '_neuralDBScan' num2str(epsilon) 'mi' num2str(minpts) '.mat']);
makeNeuralSC.m:488:    NsywSepScore = nan(nlen,1,'half');
makeNeuralSC.m:489:    NsywMixScore = nan(nlen,1,'half');
makeNeuralSC.m:497:        % pre-post-synapse separation index based on DBscan clustering
makeNeuralSC.m:515:        NsywMixScore(i) = half(msco);
makeNeuralSC.m:516:        NsywSepScore(i) = half(ssco);
makeNeuralSC.m:540:    save(fname, 'Nspidx', 'NsywMixScore', 'NsywSepScore');
makeNeuralSC.m:558:function checkNeuralDBScanVoxelFw(conf, epsilon, minpts)
makeNeuralSC.m:561:    fname = ['results/neuralsc/' conf.scname num2str(synTh) 'sr' num2str(scoreTh) '_neuralDBScanVox' num2str(epsilon) 'mi' num2str(minpts) '.mat'];
makeNeuralSC.m:596:        dbidx = int16(dbscan(X,epsilon,minpts));
makeNeuralSC.m:617:        disp(['dbscan ' conf.scname num2str(synTh) 'sr' num2str(scoreTh) ' : process (' num2str(i) ') nid=' num2str(Nid(i)) ' cls=' num2str(length(cls(cls>0))) ' invox=' num2str(scinlen) ' outvox=' num2str(scoutlen)]);
plotNeuralFC.m:5:    % DBscan param
plotNeuralFC.m:16:%    showNeuralDBScanFw(conf, epsilon, minpts); % ext figure.4-1
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 1,30p makeNeuralSC.m; sed -n 480,540p makeNeuralSC.m; sed -n 255,330p plotNeuralFC.m
```

```
% make neural Struct Connectivity data.

function makeNeuralSC
    % DBscan param
    epsilon = 1000; % nano meter
    minpts = 1; % set 1, includes isolated synapse

    % check neural input & output voxels (FlyEM)
    scTh = 80; synTh = 0; % FlyEM synapse confidence & synapse count at one neuron threshold
%    scTh = 60; synTh = 5; % almost flywire codex compatible setting
%    scTh = 80; synTh = 5; % high confidence & connection setting.
%    scTh = 0; synTh = 0; % for cheking neuPRINT+ compatible
    conf = getSCconfig('hemi', synTh, scTh);

%    checkNeuralInputOutputVoxelsFw(conf); % no use

%    checkNeuralInputOutputDistance(conf); % no use

    for i=1:5
        checkNeuralDBScanFw(conf, epsilon*i, minpts);
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && grep -n -E "out-neuron|roiR|corr\(|fw0sr140|hemiroi" plotStructConnectivity.m | head -40
```

```
6:    % roitype: hemiroi52, CmKm50, DistKm50 (figure.1)
11:    % roitype: hemiroi primary, hemiDistKm500
16:    % roitype: hemiroi primary, hemiDistKm500
20:    % roitype: hemiroi primary, hemiDistKm500
24:    % roitype: hemiroi primary, hemiDistKm500
36:    load('data/hemiroi.mat');
40:    checkOtherPieceSynapse('results/sc/hemiroi_connectlist.mat', ids, labelNames); % hemibrain ROI
50:%    roitypes = {'hemiroi','hemiCmkm50','hemiDistKm50'};
63:        case 'hemiroi'
64:            [roiIdxs, sz] = getHemiroiRoiIdxs();
96:function [roiIdxs, sz] = getHemiroiRoiIdxs()
98:    listing = dir(['atlas/hemiroi/*.nii.gz']);
100:        V = niftiread(['atlas/hemiroi/roi' num2str(i) '.nii.gz']); % ROI mask should have same transform with 4D nifti data
109:    load('data/hemiroi.mat');
112:    roitypes = {'hemiroi'}; %, 'hemidistkm500'};
155:        case 'hemiroi'
171:            r1 = corr(Y(:,p{1}(1)),Y(:,p{1}(2)));
172:            r2 = corr(log10(Y(:,p{1}(1))),log10(Y(:,p{1}(2))));
173:            r3 = corr(Y(:,p{1}(1)),Y(:,p{1}(2)),'type','Spearman');
193:    roitypes = {'hemiroi'}; %, 'hemidistkm500'};
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 1,35p plotStructConnectivity.m; sed -n 320,435p plotStructConnectivity.m; grep -n "corr(" plotStructConnectivity.m | sed -n 5,30p
```

```
% analyze and plot SC and FC relation.
% this script can run after analyzeStructConnectivity.m

function plotStructConnectivity
    % check ROI volume 
    % roitype: hemiroi52, CmKm50, DistKm50 (figure.1)
    % roitype: CmKm & DistKm 20 to 10000 (figure.2)
%    showSCroiVolume();
    
    % check SC post synapse cloud (figure.3)
    % roitype: hemiroi primary, hemiDistKm500
    showSCpostSynapse();

    % check SC matrix connection similarity FlyEM vs. FlyWire
    % matrix diff is used ext fig.3-1
    % roitype: hemiroi primary, hemiDistKm500
%    showSCmatrixSimilarity();

    % check SC vs. FC matrix connection FlyEM vs. FlyWire (figure.3)
    % roitype: hemiroi primary, hemiDistKm500
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 300,320p plotStructConnectivity.m; sed -n 470,530p plotStructConnectivity.m
```

```
figure; scatter(S1(:),S2(:)); ylim([0 m]); xlim([0 m]); daspect([1 1 1]); set(gca,'xscale','log'); set(gca,'yscale','log');
                    hold on; plot([0 m], [0 m],':','Color',[0.5 0.5 0.5]); hold off; xlabel('connected synapse count (FlyEM)'); ylabel('connected synapse count (FlyWire)');
                    title([labels{j} '-' labels{k} ' ' roitype ' r=' num2str(Sr(j,k))]);

                    figure; scatter(Sw1(:),Sw2(:)); ylim([0 1]); xlim([0 1]); daspect([1 1 1]);
                    hold on; plot([0 1], [0 1],':','Color',[0.5 0.5 0.5]); hold off; xlabel('connected synapse weight (FlyEM)'); ylabel('connected synapse weight (FlyWire)');
                    title([labels{j} '-' labels{k} ' ' roitype ' r=' num2str(Swr(j,k))]);
                end
            end
        end
        figure; imagescLabel(Nr,labels,[0.8 1],'neuron count matrix similarity');
        figure; imagescLabel(Sr,labels,[0.8 1],'synapse count matrix similarity');
        figure; imagescLabel(Nwr,labels,[0.8 1],'neuron weight matrix similarity');
        figure; imagescLabel(Swr,labels,[0.8 1],'synapse weight matrix similarity');
    end
end

function showSCFCmatrixSimilarity()
    preproc = 'ar'; % for move correct, slice time correct
    smoothSet = {{'', 's30', 's80'},{'', 's30', 's80','s150','s230','s300'}};
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 455,470p plotStructConnectivity.m; sed -n 250,272p analyzeFuncConnectivity.m; sed -n 36,118p analyzeFuncConnectivity.m | grep -v "^%" | grep -v "^\s*%"
```

```
function showNeuralTransmitter()
    llabels = {'Unknown','DA','SER','GABA','GLUT','ACH','OCT'};
    rateThs = [140]; %50 70 100  140 150];
    synThs = [0];
    roitypes = {'hemiroi'}; %, 'hemidistkm500'};

    % use appropriate smooth and nuisance
    preproc = 'ar';
    smooth = {'','s230'};
    nuisance = {'poltcomp','poltcomp'};

    for n = 1:length(roitypes)
        roitype = roitypes{n};
        for rt=1:length(rateThs)
            rth = rateThs(rt);
                    Dz(isinf(Dz)) = max(Dz(~isinf(Dz)));
                    sbjR(k,i) = corr(lC2(:),abs(Dz(:)));
                end

                % each ROIs (Traced vs. m-FCz and only)
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 576,710p plotFuncConnectivity.m
```

```
function checkRandSubsampleRankTestByHemiroi(vslabels)
    preproc = 'ar'; % for move correct, slice time correct
    hpfTh = [0]; % high-pass filter threshold
    smooth = {''};
    nuisance = {'poltcomp'};
%    roitypes = {{'hemiroi','_hb0sr80fw_rd140-15'},{'hemiroi','_hb0sr80fw_rd705-40'},{'hemiroi','_hb0sr80fw_rd67-12'}, ...
%       {'hemiroi','_fw0sr140_rd185-20'},{'hemiroi','_fw0sr140_rd1560-80'},{'hemiroi','_fw0sr140_rd140-15'},};
    roitypes = {{'hemiroi','_fw0sr140_rd185-20'},{'hemiroi','_fw0sr140_rd1560-80'},{'hemiroi','_fw0sr140_rd140-15'},};
%    targets = {{'hemiroi','_hb0sr80_sp10db3000mi1_only1'},{'hemiroi','_hb0sr80_sp90db3000mi1'},{'hemiroi','_hb0sr80_rc20_only1'}, ...
%        {'hemiroi','_fw0sr140_sp10db3000mi1_only1'},{'hemiroi','_fw0sr140_sp90db3000mi1'},{'hemiroi','_fw0sr140_rc20_only1'},};
    targets = {{'hemiroi','_fw0sr140_sp10db3000mi1_only1'},{'hemiroi','_fw0sr140_sp90db3000mi1'},{'hemiroi','_fw0sr140_rc20_only1'},};
    rNums = 1:99; % for random subsampling number
    pval = 0.05 / 6; % bonferroni correction

    for r = 1:length(roitypes)
        Am = []; Rm = []; tAm = []; tRm = []; ncounts = []; sycounts = [];
        for h=1:length(hpfTh)
            hpfstr = '';
            if hpfTh(h) > 0, hpfstr = ['hf' num2str(round(1/hpfTh(h)))]; end
            for k=1:length(smooth)
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && grep -rn -i -l "nwb\|antsRegistration\|spm_realign\|slice" --include=*.m . | head; grep -rn -i "zenodo" --include=*.m . | head -5; ls atlas/hemiroi | wc -l
```

```
./lib/plotNifti3DZSlice.m
./lib/plotGlmContrastImage.m
./plotNeuralFC.m
./analyzeNeuralFC.m
./plotFuncConnectivity.m
./extractNeuralTimeseries.m
./glmFlyMB2nd.m
./analyzeFuncConnectivity.m
./analyzeFuncConnectivityFixNc.m
./extractROItimeseries.m
114
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -rl "000727" --include=*.yaml --include=*.json --include=*.md . 2>/dev/null | grep -v "^./transcripts" | head
```

```
./attempts/brezovec-2022-01.yaml
./docs/pilot-notes.md
./docs/conversion-tracker.md
./docs/pilot-notes/brezovec-2022-01.md
./papers/triage.yaml
./papers/manifest.yaml
./papers/datasets/okuno-2025.yaml
./papers/datasets/brezovec-2022.yaml
./papers/renamed.yaml
./targets/reuse.yaml
```

**Agent calls Bash**

```bash
grep -n -B3 -A15 "000727" targets/reuse.yaml | head -60; cat papers/datasets/brezovec-2022.yaml
```

```
49-  source: find_reuse
50-- key: okuno-2025
51-  doi: 10.7554/elife.107990.1
52:  dataset: dandi:000727
53-  reuse_type: NOVEL_ANALYSIS
54-  evidence: Whole-brain calcium imaging data of D. melanogaster were acquired by Brezovec et al. [14] and downloaded
55:    from DANDI (https://dandiarchive.org/dandiset/000727/0.240106.0043). 4D NIfTI image data (256×128×49 voxels,
56-    3384 frames) were extracted from a NWB file by an in-house MATLAB script.
57:  reasoning: The authors explicitly downloaded dataset 000727 from DANDI and extracted and preprocessed its whole-brain
58-    calcium-imaging recordings. They also extracted movement-velocity data and analyzed the walking task with a
59-    whole-brain GLM. The author lists do not overlap with the Brezovec et al. dataset paper, indicating reuse by
60-    a different lab.
61-  source: find_reuse
62-- key: wakhloo-2026
63-  doi: 10.1038/s41593-025-02183-y
64-  dataset: dandi:000978
65-  reuse_type: NOVEL_ANALYSIS
66-  evidence: Shin, J. & Jadhav, S. Single day W-track learning (Version 0.240511.0307) [Data set]. DANDI https://doi.org/10.48324/dandi.000978/0.240511.0307
67-    (2024).
68-  reasoning: Added by hand. find_reuse paired the paper with DANDI:000447, another W-track dataset of the same lab;
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn -A6 "'000727'\|\"000727\"\|id: 000727" targets/*.yaml | head -30
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -rn "000727" targets/ papers/manifest.yaml papers/triage.yaml | head
```

```
targets/reuse.yaml:52:  dataset: dandi:000727
targets/reuse.yaml:55:    from DANDI (https://dandiarchive.org/dandiset/000727/0.240106.0043). 4D NIfTI image data (256×128×49 voxels,
targets/reuse.yaml:57:  reasoning: The authors explicitly downloaded dataset 000727 from DANDI and extracted and preprocessed its whole-brain
targets/dandisets.json:3536:   "dandiset": "000727",
papers/manifest.yaml:1037:  '000727':
papers/triage.yaml:163:  "000727":
```

**Agent calls Bash**

```bash
sed -n 3530,3560p targets/dandisets.json
```

```
],
   "catalystneuro": [
    "conversion code at https://github.com/catalystneuro/cai-lab-to-nwb"
   ]
  },
  {
   "dandiset": "000727",
   "name": "Mapping the Neural Dynamics of Locomotion across the Drosophila Brain",
   "published_version": "0.240106.0043",
   "asset_count": 18,
   "size_gb": 609.57,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Drosophila melanogaster - Fruit fly"
   ],
   "approaches": [
    "behavioral approach",
    "microscopy approach; cell population imaging"
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && grep -n -A8 "glmFlyMB2nd" README.md | head -14; git diff --stat 4b92add 29c4e32 -- glmFlyMB1st.m glmFlyMB2nd.m checkBehavior.m extractROItimeseries.m analyzeFuncConnectivity.m lib/ plotStructConnectivity.m | tail -3; ls atlas/hemiroi | head -3; grep -n "WED\|AVLP\|LAL\|GNG\|IPS" data/*.xlsx 2>/dev/null | head -2; grep -n -i "jrc2018f_2010roi\|2010roi" *.m | head
```

```
120:>>  glmFlyMB2nd
121-Height threshold: P-value=0.001, T-value=3.2423
122-Extent threshold: k=167.936 voxels, P-value=0.0051641 (0.015373)
123-Expected cluster list (num=3), degree of freedom=56, FWHM={7.5373 7.8173 5.5143} voxels
124-1) k=416801 voxels, P uncorr=0, P fwe-corr=0, peak (102,83,40)=14.7075
125-2) k=406 voxels, P uncorr=7.5926e-05, P fwe-corr=0.00022775, peak (82,78,12)=-6.1411
126-3) k=260 voxels, P uncorr=0.00086956, P fwe-corr=0.0026053, peak (174,80,15)=-5.6522
127-Tmax of s80poltcomparfly-all-Tukey8 : movement tmax=14.7075, tcnt=416809
128-~~~
 analyzeFuncConnectivity.m | 82 ++++++++++++++++++++++++++++++++++++-----------
 lib/loadSwc.m             |  5 +++
 2 files changed, 68 insertions(+), 19 deletions(-)
roi1.nii.gz
roi10.nii.gz
roi100.nii.gz
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && grep -n -E "rd185|rd1560|rd140|'_rd|_rd'|randSubsample|normrnd|randn" *.m | head -20
```

```
analyzeFuncConnectivity.m:116:%    roitypes = {'hemiroi_hb0sr80fw_rd67-12','hemiroi_hb0sr80fw_rd140-15','hemiroi_hb0sr80fw_rd705-40', ...
analyzeFuncConnectivity.m:117:%            'hemiroi_fw0sr140_rd140-15','hemiroi_fw0sr140_rd185-20','hemiroi_fw0sr140_rd1560-80'};  % for s0, poltcomp, rNums
makeSCcountMatrix.m:50:                [ssspidx, splogi] = randSubsample((Spidx >= 0 & Spidx < spiTh), rtype, StoS, Sid, ssrate, sstraced, 0); % -1 should be ignored
makeSCcountMatrix.m:55:                [ssrcdist, rclogi] = randSubsample((SrcCloseDist < rcdistTh), rtype, StoS, Sid, ssrate, sstraced, 0); % nan should be ignored by <.
makeSCcountMatrix.m:59:                [sssubsamp, sublogi] = randSubsample(sublogi, rtype, StoS, Sid, ssrate, sstraced, rnum);
makeSCcountMatrix.m:315:function [ssrslogi, rslogi] = randSubsample(rslogi, rtype, StoS, Sid, ssrate, sstraced, rnum)
makeSCcountMatrixFw.m:39:                spidx = randSubsampleFw(((postSpidx>=0 & postSpidx<spiTh) & (preSpidx>=0 & preSpidx<spiTh)), rtype, valid, score, 0);
makeSCcountMatrixFw.m:43:                rcdist = randSubsampleFw((SrcpreCloseDist<rcdistTh & SrcpostCloseDist<rcdistTh), rtype, valid, score, 0); % nan should be ignored by <.
makeSCcountMatrixFw.m:46:                subsamp = randSubsampleFw(subsamp, rtype, valid, score, rnum);
makeSCcountMatrixFw.m:267:function [rslogi] = randSubsampleFw(rslogi, rtype, valid, score, rnum)
makeStructConnectivity.m:304:            idstr = ['hemiroi_hb'  num2str(synTh) 'sr' num2str(hbSth) functype '_rd' num2str(param(1)/10000) '-' num2str(param(2)/10000) '-' num2str(k)];
makeStructConnectivity.m:309:                rnum = param(1) + randn() * param(2);
makeStructConnectivity.m:332:            idstr = ['hemiroi_fw'  num2str(synTh) 'sr' num2str(fwSth) '_rd' num2str(param(1)/10000) '-' num2str(param(2)/10000) '-' num2str(k)];
makeStructConnectivity.m:337:                rnum = param(1) + randn() * param(2);
plotFuncConnectivity.m:581:%    roitypes = {{'hemiroi','_hb0sr
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py
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

[... 61 more lines not kept]
```

**Agent**

Code read. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/okuno-2025.yaml",
 "content": "# Claims for Okuno, Woodward, Okano & Hata (2025), eLife reviewed preprint 107990 v1,\n# \"Functional connectivity, structural connectivity, and inter-individual variability in\n# Drosophila melanogaster\", on dandiset 000727 (reused; the data are those of Brezovec et al.).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read. The eLife Reviewed Preprint version 1 (October 9, 2025, \"Not revised\"), the version\n# the DOI 10.7554/elife.107990.1 names, from the publisher's HTML, in\n# paper/10.7554-elife.107990.1.txt: abstract, Introduction, Results, figure legends (Figures 1\n# to 5), Discussion, Materials and methods, Data availability, and the legends of the Extended\n# Data figures (1-1, 1-2, 2-1, 3-1, 3-2, 4-1 to 4-4, 5-1), which are the paper's only\n# supplement. No PDF was supplied, so no figure could be read; values shown only in figures are\n# not known here. The text lost the displayed equations of the Methods (the FC-SC detection and\n# correlation score, cPPSSI, PPSSI and the two ranking scores); they are taken from the code\n# (M4, M7).\n#\n# Code read. github.com/takuto-okuno-riken/flywalk (MATLAB), linked under Code Availability, at\n# commit 4b92add (2025-08-11), the last commit before v1 was posted. Later commits\n# (2025-11 to 2026-06) answer the reviewers and change the DBSCAN distance to a morphological\n# one; they are not this version's method. The repository holds the ROI time-series\n# extraction with smoothing and nuisance regression (extractROItimeseries.m, lib/getNuisance*),\n# FC and FC-SC analysis (analyzeFuncConnectivity.m), the plotting and tests of Figures 2 to 4\n# (plotFuncConnectivity.m, plotStructConnectivity.m, plotNeuralFC.m), SC construction and the\n# random synapse subsampling (makeStructConnectivity.m, makeSCcountMatrix*.m), PPSSI\n# (makeNeuralSC.m), the walking regressor (checkBehavior.m) and the GLM (glmFlyMB1st.m,\n# glmFlyMB2nd.m, lib/calcGlmTukey.m), with the resized FDA template, the fibre mask, the brain\n# mask and the hemibrain neuropil atlas (atlas/hemiroi, 114 ROIs) already transformed to the\n# template. It does not hold the NWB-to-NIfTI extraction or the SPM12 and ANTs registration\n# steps. Its README points to Zenodo 10.5281/zenodo.15532271 for the preprocessed connection\n# lists and ROI atlases (SCKm, DistKm) the scripts load.\n#\n# Data the paper used. From dandiset 000727, version 0.240106.0043 (Methods), the whole-brain\n# two-photon calcium imaging of Brezovec et al. in 9 head-fixed flies walking on a ball:\n# 256 x 128 x 49 voxels, 3384 volumes per fly; the code uses a volume rate of 1.879714 Hz, the\n# GCaMP (green) channel, and the movement speed sampled at 50 Hz with the imaging starting\n# 104.654892 ms after it (checkBehavior.m). Eight flies are used for every ROI-based analysis\n# (\"because of missing time-series in some ROIs in one fly\"); the code's subject list is\n# [1 2 3 4 5 6 8 9] of the registered files in name order, so the seventh fly is left out.\n# All nine are used in the GLM. The dandiset's title, \"Mapping the Neural Dynamics of\n# Locomotion across the Drosophila Brain\", names these data.\n#\n# Outside data. Every finding on structural connectivity (SC) uses EM connectomes the paper\n# downloaded: FlyEM hemibrain v1.2 synapses from Janelia's DVID (dvid.io/blog/release-v1.2/),\n# and FlyWire from codex.flywire.ai and Zenodo 10676866, with neurotransmitter predictions;\n# synapses moved to the resized FDA template through JRC2018F with navis-flybrains and ANTs.\n# Claims that compare the dandiset's FC with these SC matrices are data with_inputs; claims on\n# the connectomes alone are data elsewhere. The neuropil atlas and the template come from the\n# code repository (pinned above), the SCKm and DistKm ROI atlases from Zenodo 15532271 (or are\n# rebuilt with makeVoxelROIatlas.m, by k-means, so not identically).\n#\n# Methods shared by the criteria (M) and details the paper leaves open (O).\n# M1 Preprocessing (Methods, Preprocessing). SPM12 motion and slice-timing correction (code\n#    prefix \"ar\"), the mean image registered by ANTs to the resized FDA template\n#    (template/thresholded_FDACal.nii.gz, 2.45 x 2.28 x 3.72 um voxels) and the 4D data\n#    transformed with it.\n# M2 Smoothing. A Gaussian kernel whose width the paper gives in voxels (\"FWHM from 1 voxel\n#    (2.28 um) to 30 voxels\"; Results and the GLM Methods call it \"kernel radius\"). The code\n#    sets FWHM = n voxels along y (2.28 um) and the same physical width along x and z, sigma =\n#    FWHM / sqrt(8 ln 2), filter size 2*ceil(2*sigma)+1, applied to each volume\n#    (extractROItimeseries.m; code names s10 to s300 for 1 to 30 voxels).\n# M3 Nuisance removal and FC (Methods, Generation of ROIs; code). Poly-tCompCor is 7 polynomial\n#    regressors (two linear ramps, four quadratic terms and a constant,\n#    lib/getNuisancePolynomial.m) plus 6 principal components of the 1000 voxels with the\n#    highest temporal SD after polynomial detrending (lib/getNuisancetCompCor.m). Each voxel of\n#    an ROI is mean-centred and regressed on these by OLS; the ROI time series is the mean of\n#    the residuals; FC is the Pearson correlation between ROI time series per fly,\n#    Fisher-z-transformed (atanh) and averaged over the 8 flies; infinite values (the diagonal)\n#    are set to the largest finite value.\n# M4 FC-SC correlation and detection (Methods, FC-SC detection and correlation;\n#    analyzeFuncConnectivity.m). SC (neuron) is the count of neurons with post-synapses in one ROI\n#    and pre-synapses in the other, SC (synapse) the count of their synapses (FlyEM confidence\n#    0.8, FlyWire cleft score 140 unless stated). FC-SC correlation is the Pearson r between\n#    log10(SC), with log of zero set to 0, and the code's |mean z-FC|, over every element of the\n#    n x n matrices including the diagonal. FC-SC detection is the mean over 100 thresholds (the\n#    0th to 99th percentiles of the nonzero SC values) of the ROC AUC of |mean z-FC| against SC\n#    at or above the threshold. The score is |r| + 2|AUC - 0.5| (the code's B, range 0 to 2).\n# M5 ROI types. Hemibrain primary neuropils (63 ROIs, Figures 3 and 4), the 52 of Figure 1, and\n#    SCKm and DistKm, k-means parcellations of the 146,604 hemibrain voxels into 20 to 1000 (and\n#    up to 10,000 or 20,000 in the code) ROIs.\n# M6 Permutation test (Methods, Statistical Analysis; plotFuncConnectivity.m\n#    checkRandSubsampleRankTestByHemiroi). On the 63 hemibrain primary ROIs, no smoothing,\n#    Poly-tCompCor, FlyWire sc140: the SC matrix of the selected synapses against 99 null SC\n#    matrices of randomly sampled synapses whose number is drawn from a normal distribution\n#    around the selected total (makeStructConnectivity.m). A normal distribution is fitted to\n#    the 99 null values and the two-tailed p is 2*Phi(-|x - mu| / sigma); significance at\n#    0.05/6 (Bonferroni, as the code sets it).\n# M7 PPSSI (Methods, PPSSI; makeNeuralSC.m). DBSCAN on each neuron's synapse positions with\n#    radius 3 um and minimum 1 point; for each cluster cPPSSI = ((pre - post) / (pre + post))^2;\n#    PPSSI = sum over clusters of cPPSSI times the cluster's share of the neuron's synapses.\n#    Unsegregated ranking score (1 - PPSSI) * log10(W), segregated ranking score PPSSI *\n#    log10(W), W the neuron's synapse count.\n# M8 GLM (Methods, GLM Analysis; checkBehavior.m, glmFlyMB1st.m, glmFlyMB2nd.m). The speed is\n#    averaged per imaging volume; the code clips it at th, the mean over flies of each fly's SD\n#    of speed, subtracts b, the mean over flies of each fly's 10th percentile, sets negatives\n#    to 0 and scales to [0 1]; it is convolved with a gamma CRF (shape 1.7, scale 0.25 s, 5 s\n#    kernel, at 25 times the volume rate). First level per fly, on brain-mask voxels smoothed with\n#    FWHM 8 voxels (M2), mean-centred, with the regressor, the 7 polynomial terms and 6\n#    tCompCor components scaled by their SD; pre-whitening by Tukey taper of size 8\n#    (lib/calcGlmTukey.m). Second level is the code's mixed-effects OLS with Tukey taper on the\n#    nine flies' betas of the regressor and the tCompCor terms (glmFlyMB2nd.m); height threshold\n#    p < 0.001, cluster extent as plotGlmContrastImage.m computes it.\n# O1 The Methods say \"Walking was defined as 1σ (34%) or more of the movement velocity and\n#    divided into walking and other. Less than 10% of movement velocity was zero cut.\" The code\n#    builds the graded regressor of M8, saturating at 1 SD; this is followed. A binary\n#    regressor (1 for volumes at or above b + th, else 0) is the reading the words \"divided into\n#    walking and other\" allow, and is run as a variant.\n# O2 The SPM12 and ANTs settings of M1 are not given in the paper or the code. The author uses\n#    SPM12 defaults (realign to the mean, slice timing to the middle slice) and ANTs SyN with\n#    default parameters, as a standard choice; a rigid plus affine registration is a variant.\n#    Registration can change ROI time series, so outcomes resting on it are marked so.\n# O3 The paper's FC matrix is signed; the code correlates SC with |mean z-FC| (M4). The code is\n#    followed; signed FC is shown as a variant.\n# O4 Which neuropil atlas names the GLM regions. Readings (a) the hemibrain atlas of the\n#    Methods (atlas/hemiroi, names in data/hemiroi.mat), (b) the JFRC2010 whole-brain atlas\n#    the repository also holds (atlas/jrc2018f_2010roiCal_invFDACal.nii.gz with\n#    jfrc2010-roi-itksnap.txt).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000727\"\npaper: doi:10.7554/elife.107990.1\nclaims:\n- id: fig1-poltcomp-optimal\n  statement: Among the nuisance removal methods tested, polynomial detrending combined with\n    tCompCor gives the best FC-SC correlation and detection for the three ROI types.\n  source: Results, Investigation of the optimal nuisance factor removal method, paragraph 1;\n    Figure 1d to 1f\n  quote: After the comparison of the raw (leftmost) and removal methods for various ROI types, the\n    combination of polynomial detrending [41] & tCompCor [42] was found to yield the optimal\n    results.\n  data: with_inputs\n  criterion: For hemibrain 52, SCKm 50 and DistKm 50 ROIs (M5), FlyEM SC, no smoothing (Figure 1\n    names none, and the code's hemibrain runs use none), the score of M4 for every method in the\n    code's list of 37 combinations (extractROItimeseries.m; global mean, global signal, white\n    matter, 6 and 24 head motion, aCompCor, tCompCor, polynomial). Readings for \"optimal\"; (a)\n    Poly-tCompCor has the highest score with SC (neuron) in each ROI type; (b) it has the\n    highest score averaged over the three ROI types and both SC kinds. Reproduced when (a) or\n    (b) holds; partially reproduced when Poly-tCompCor is within the top three under (b) but\n    neither holds. Rests on O2 and O3.\n- id: fig2b-distkm-smoothing-optimum\n  statement: For DistKm ROIs spatial smoothing raises FC-SC agreement strongly, and the best\n    kernel is about 23 voxels (52.44 um) across ROI counts.\n  source: Results, Comparison of the FC-SC correlation between humans and flies, paragraph 1;\n    Figure 2b\n  quote: In DistKm, smoothing was highly effective, and the optimal kernel radius of the Gaussian\n    filter was around 23 voxels (52.44 μm) for various ROI counts (Fig. 2b).\n  data: with_inputs\n  expected:\n  - quantity: optimal smoothing size for DistKm\n    value: 23\n    tolerance: 2.3\n    unit: voxels\n  criterion: DistKm at 20, 30, 50, 100, 200, 300, 500 and 1000 ROIs, Poly-tCompCor (the code's\n    Figure 2 setting, README demo 2), FlyEM SC, smoothing 0 to 30 voxels by 1 (M2). For each\n    count, the size that maximizes the score of M4 with SC (neuron), as the code's \"find best\n    smooth size\" does. Reproduced when the median of the eight optimal sizes is within\n    tolerance and the score at the optimum exceeds the unsmoothed score at every count;\n    partially reproduced when smoothing raises the score at every count but the median optimum\n    falls outside tolerance. The optima with SC (synapse) are shown. Rests on O2 and O3.\n- id: figs2-1b-sckm-smoothing\n  statement: For SCKm ROIs, smoothing does not help below 100 ROIs, while kernels above 16\n    voxels (36.48 um) help above 100 ROIs.\n  source: Results, Comparison of the FC-SC correlation between humans and flies, paragraph 1;\n    Extended Data Figure 2-1b\n  quote: In SCKm, smoothing was ineffective for ROI count below 100, while the kernel radius above\n    16 voxels (36.48 μm) was effective for ROI count above 100 (Ext.Data.Fig.2-1b).\n  data: with_inputs\n  criterion: As fig2b-distkm-smoothing-optimum, on SCKm. Reproduced when, for 20, 30 and 50 ROIs,\n    no smoothing size raises the score of M4 (SC neuron) by more than 0.05 over no smoothing,\n    and for 200 to 1000 ROIs every size from 17 to 30 voxels gives a higher score than no\n    smoothing. The 0.05 margin for \"ineffective\" is not from the paper; the curves are shown so\n    that a reader can judge them. Partially reproduced when one of the two halves holds. Rests\n    on O2 and O3.\n- id: fig2c-smoothing-plus-poltcomp\n  statement: Smoothing combined with Poly-tCompCor gives significantly higher FC-SC scores than\n    smoothing alone, for SCKm and DistKm.\n  source: Results, Comparison of the FC-SC correlation between humans and flies, paragraph 1;\n    Figure 2c\n  quote: We found that this combination was significantly more effective than smoothing alone for\n    SCKm and DistKm (Fig. 2c, Mann–Whitney U test p<1.67e-4 Bonferroni corrected).\n  statistics:\n  - test: Mann-Whitney U test\n    p: 0.000167\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: scores over smoothing sizes 0 to 30 voxels at each ROI count\n  data: with_inputs\n  criterion: As the Figure 2c legend and the code's ranksum block (plotFuncConnectivity.m) have\n    it, at each ROI count of SCKm and DistKm (20 to 1000), the scores of M4 over the 31\n    smoothing sizes 0 to 30 with no nuisance removal against those with Poly-tCompCor, by a\n    two-sided Mann-Whitney U test at p < 1.67e-4. Reproduced when Poly-tCompCor is higher and\n    significant at every count of both ROI types with SC (neuron); partially reproduced when\n    that holds at more than half of the 16 type and count pairs. SC (synapse) is shown. Rests\n    on O2 and O3.\n- id: figs2-1d-highpass-degrades\n  statement: Adding a temporal high-pass filter to nuisance removal degrades FC-SC agreement.\n  source: Results, Comparison of the FC-SC correlation between humans and flies, paragraph 1;\n    Extended Data Figure 2-1d\n  quote: the combination of a high-pass filter and nuisance factor removal overlapped for the\n    purpose of noise removal, and the effect was degraded (Ext.Data.Fig.2-1d)\n  data: with_inputs\n  criterion: DistKm ROIs (legend), Poly-tCompCor, no smoothing, FlyEM SC, with high-pass cut-offs\n    0.1, 0.05, 0.025, 0.02, 0.01, 0.009, 0.008, 0.005 and 0.001 Hz (the code's list; Methods\n    \"from 0.1 Hz to 0.001 Hz\") applied after the regression, as extractROItimeseries.m does\n    (MATLAB highpass). Reproduced when the score of M4 with any cut-off is below the score\n    without the filter at most ROI counts tested (20 to 1000). Rests on O2 and O3.\n- id: fig2d-log-decline\n  statement: The best FC-SC correlation falls linearly with the logarithm of the ROI count.\n  source: Results, Comparison of the FC-SC correlation between humans and flies, paragraph 2;\n    Figure 2d\n  quote: Results showed that the correlation decreased proportionally to the logarithm of the ROI\n    count (Fig. 2d).\n  data: with_inputs\n  criterion: For SCKm and DistKm, the FC-SC correlation (SC neuron, FlyEM) at the score-optimal\n    smoothing of each ROI count (as in fig2b-distkm-smoothing-optimum), over the counts 20 to\n    1000 and, where the atlases exist, 5000 and 10,000. Reproduced when, for each ROI type, the\n    slope of r on log10(ROI count) is negative and the Pearson correlation of r with log10(count)\n    is -0.9 or lower (a standard bar for \"linear\", not the paper's). Partially reproduced when\n    it holds for one type. Rests on O2 and O3.\n- id: fig2d-fly-values\n  statement: The fly FC-SC correlation is 0.71 to 0.81 at about 50 ROIs and 0.6 to 0.67 at about\n    1000 ROIs (SCKm and DistKm), against 0.66 and 0.54 in humans.\n  source: Results, Comparison of the FC-SC correlation between humans and flies, paragraph 2;\n    Figure 2d\n  quote: At approximately 50 ROIs, the difference was nearly 1.08-fold to 1.22-fold (r=0.66 for\n    humans and r=0.71-0.81 for flies [SCKm, DistKm]); by contrast, at approximately 1,000 ROIs,\n    the difference was roughly 1.12-fold to 1.24-fold (r=0.54 for humans and r=0.6-0.67 for flies)\n  data: with_inputs\n  expected:\n  - quantity: fly FC-SC correlation at 50 ROIs, range over SCKm and DistKm\n    value: [0.71, 0.81]\n    tolerance: range widened by 10% of each bound, 0.639 to 0.891\n  - quantity: fly FC-SC correlation at 1000 ROIs, range over SCKm and DistKm\n    value: [0.6, 0.67]\n    tolerance: range widened by 10% of each bound, 0.54 to 0.737\n  criterion: FC-SC correlation as in fig2d-log-decline at 50 and at 1000 ROIs. The human values\n    are from the literature and are not tested. Which values span each range is open; readings\n    (a) SCKm and DistKm with SC (neuron) only, (b) both SC kinds. Reproduced when, under one\n    reading, every value at 50 ROIs and every value at 1000 ROIs lies in its widened range.\n    Rests on O2 and O3.\n- id: fig2d-ten-thousand-rois\n  statement: At about 10,000 ROIs the fly FC-SC correlation is 0.46 to 0.57.\n  source: Results, Comparison of the FC-SC correlation between humans and flies, paragraph 2;\n    Discussion, paragraph 3\n  quote: The difference was slightly larger (1.21 to 1.5-fold: r=0.378 for marmosets and\n    r=0.46-0.57 for flies) than the marmoset results at around 10,000 ROIs\n  data: with_inputs\n  expected:\n  - quantity: fly FC-SC correlation at 10,000 ROIs, range over SCKm and DistKm\n    value: [0.46, 0.57]\n    tolerance: range widened by 10% of each bound, 0.414 to 0.627\n  criterion: As fig2d-fly-values, at 10,000 ROIs (code atlases hemiCmkm10000 and\n    hemiDistKm10000). Reproduced when, under one reading of fig2d-fly-values, every value lies\n    in the widened range. Rests on O2 and O3.\n- id: discussion-twenty-rois\n  statement: With optimal nuisance removal and smoothing the FC-SC correlation reaches 0.87 at\n    20 ROIs, and 0.928 with Spearman correlation.\n  source: Discussion, paragraph 3\n  quote: Through optimal nuisance factor removal and smoothing, we achieved r=0.87 at 20 ROIs.\n    Furthermore, by applying Spearman correlation instead of Pearson, we obtained r=0.928.\n  data: with_inputs\n  expected:\n  - quantity: Pearson FC-SC correlation at 20 ROIs\n    value: 0.87\n    tolerance: 0.087\n  - quantity: Spearman FC-SC correlation at 20 ROIs\n    value: 0.928\n    tolerance: 0.0928\n  criterion: The paper does not name the ROI type or SC kind. Readings; SCKm or DistKm at 20 ROIs,\n    SC (neuron) or (synapse), Poly-tCompCor, the score-optimal smoothing (M4, and the code's\n    Spearman SR on the same elements). Reproduced when, under one reading, both values are within\n    tolerance. Rests on O2 and O3.\n- id: fig3d-confidence-threshold\n  statement: Raising the FlyEM synapse confidence threshold to 0.8 increases the FC-SC\n    correlation.\n  source: Results, Comparison between FlyEM and FlyWire connectome data, paragraph 1; Figure 3d;\n    Extended Data Figure 3-1b\n  quote: we set the confidence threshold of 0.8 as high as possible, thereby increasing the FC-SC\n    correlation (Fig. 3d, ExtFig.3-1b)\n  data: with_inputs\n  criterion: 63 hemibrain primary ROIs, no smoothing, Poly-tCompCor (the code's combination index\n    4 in plotStructConnectivity.m), SC (neuron) from FlyEM at confidence 0.5, 0.6, 0.7, 0.8 and\n    0.9. Reproduced when the FC-SC correlation at 0.8 exceeds that at 0.5, 0.6 and 0.7. Rests\n    on O2 and O3.\n- id: fig3d-flyem-vs-flywire\n  statement: Against the same FC, FlyEM gives a higher matrix-level FC-SC correlation than\n    FlyWire (0.73 against 0.68).\n  source: Results, Comparison between FlyEM and FlyWire connectome data, paragraph 1; Figure 3d\n  quote: As a result, FlyEM r=0.73 differed from FlyWire r=0.68 at the matrix level (Fig. 3d).\n  data: with_inputs\n  expected:\n  - quantity: FC-SC correlation, FlyEM cf0.8\n    value: 0.73\n    tolerance: 0.073\n  - quantity: FC-SC correlation, FlyWire sc140\n    value: 0.68\n    tolerance: 0.068\n  criterion: 63 hemibrain primary ROIs, no smoothing, Poly-tCompCor (the code's combination index\n    4), SC (neuron), FlyEM confidence 0.8 and FlyWire cleft score 140 (M4). Reproduced when both\n    values are within tolerance and FlyEM is higher; partially reproduced when FlyEM is higher\n    but a value is outside tolerance. Rests on O2 and O3.\n- id: fig3e-flyem-higher-most-regions\n  statement: Per region, FlyEM gives the higher FC-SC correlation in 58 of the 63 primary\n    neuropils, FlyWire in 5.\n  source: Results, Comparison between FlyEM and FlyWire connectome data, paragraph 1; Figure 3e\n  quote: In the FC-SC correlation of each region, FlyEM had higher values in most regions at 58:5\n    (Fig. 3e, ExtFig.3-1a).\n  data: with_inputs\n  depends_on:\n  - fig3d-flyem-vs-flywire\n  expected:\n  - quantity: regions where FlyEM is higher\n    value: 58\n    tolerance: 5.8\n    unit: of 63 regions\n  criterion: The code's per-region FC-SC correlation (analyzeFuncConnectivity.m, roiR column 7);\n    for region i, the Pearson r between log10(SC neuron) of row i and column i stacked and |mean\n    z-FC| of row i and column i stacked, with the settings of fig3d-flyem-vs-flywire. Reproduced\n    when the count is within tolerance. Rests on O2 and O3.\n- id: fig3g-transmitter-correlation\n  statement: Across regions, the FC-SC correlation rises with the share of cholinergic output\n    neurons (r = 0.39, p = 0.0013) and falls with the share of GABAergic ones (r = -0.25, p =\n    0.046).\n  source: Results, Comparison between FlyEM and FlyWire connectome data, paragraph 1; Figure 3g\n  quote: The analysis of the relationship between this ratio and FC-SC correlation in each\n    neurotransmitter revealed significant correlations for acetylcholine (r=0.39, p=0.0013) and\n    GABA (r=-0.25, p=0.046).\n  statistics:\n  - about: acetylcholine\n    test: Pearson correlation\n    statistic: r = 0.39\n    p: 0.0013\n    n: 63 hemibrain primary ROIs\n  - about: GABA\n    test: Pearson correlation\n    statistic: r = -0.25\n    p: 0.046\n    n: 63 hemibrain primary ROIs\n  data: with_inputs\n  depends_on:\n  - fig3e-flyem-higher-most-regions\n  expected:\n  - quantity: r, acetylcholine output share against regional FC-SC correlation\n    value: 0.39\n    tolerance: 0.039\n  - quantity: r, GABA output share against regional FC-SC correlation\n    value: -0.25\n    tolerance: 0.025\n  criterion: As plotStructConnectivity.m showNeuralTransmitter, the per-region FC-SC correlation\n    of fig3e-flyem-higher-most-regions with FlyWire sc140 SC (no smoothing, Poly-tCompCor),\n    against each region's share of output neurons of each predicted transmitter (FlyWire),\n    Pearson r and its p over the 63 regions. Reproduced when both r are within tolerance and\n    both p < 0.05; partially reproduced when the signs hold and p < 0.05 for one. The other four\n    transmitters are shown. Rests on O2 and O3.\n- id: fig3a-postsynapse-counts\n  statement: In the hemibrain region FlyEM has 21.4 million post-synapses at confidence 0 and\n    FlyWire 18.8 million at cleft score 50; FlyWire at cleft score 140 has about 11.4 million,\n    matched to FlyEM at confidence 0.8.\n  source: Results, Comparison between FlyEM and FlyWire connectome data, paragraph 1; Figure 3a\n  quote: FlyEM has a synaptic “confidence” threshold and contains 21.4 million post-synapses in\n    the hemibrain region at its initial value of 0. ... FlyWire has a ‘CleftScore’ [17]\n    threshold and 18.8 million post-synapses at its initial value of 50. ... Then we adjusted\n    the CleftScore to 140, which has a post-synapse number of approximately 11.4 million\n  data: elsewhere\n  where: FlyEM hemibrain v1.2 synapses (dvid.io/blog/release-v1.2/); FlyWire synapses (Zenodo\n    10676866, codex.flywire.ai)\n  expected:\n  - quantity: FlyEM post-synapses in hemibrain, confidence 0\n    value: 21.4\n    tolerance: 2.14\n    unit: million\n  - quantity: FlyWire post-synapses in hemibrain, cleft score 50\n    value: 18.8\n    tolerance: 1.88\n    unit: million\n  - quantity: FlyWire post-synapses in hemibrain, cleft score 140\n    value: 11.4\n    tolerance: 1.14\n    unit: million\n- id: fig3c-regional-detection\n  statement: FlyEM detects more synapses in the mushroom bodies and the central complex (EB, FB,\n    NO, PB), FlyWire more in the optic lobe (LO, ME) and the periesophageal neuropils (CAN, FLA).\n  source: Results, Comparison between FlyEM and FlyWire connectome data, paragraph 1; Figure 3c\n  quote: FlyEM had more synapses in the mushroom bodies (aL, bL, etc.) and in the major neuropils\n    of the central nervous system (CNS; EB, FB, NO, and PB). In comparison, FlyWire had more\n    synapses in the visual system (LO and ME) and in the periesophageal neuropils (CAN and FLA;\n    Fig. 3c)\n  data: elsewhere\n  where: FlyEM hemibrain v1.2 (DVID) and FlyWire (Zenodo 10676866), with the hemibrain atlas of\n    the code repository\n- id: figs3-1a-regional-count-similarity\n  statement: Regional post-synapse counts of FlyEM and FlyWire over the 63 primary ROIs correlate\n    with Pearson r = 0.778, Spearman r = 0.9, and Pearson r = 0.919 on log10 counts.\n  source: Extended Data Figure 3-1a\n  quote: The Pearson correlation is not so similar, r=0.778, but the Spearman correlation is much\n    more similar, r=0.9. ... Pearson correlation shows r=0.919, a higher similarity.\n  data: elsewhere\n  where: FlyEM hemibrain v1.2 (DVID) and FlyWire (Zenodo 10676866)\n  expected:\n  - quantity: Pearson r of regional counts\n    value: 0.778\n    tolerance: 0.0778\n  - quantity: Spearman r of regional counts\n    value: 0.9\n    tolerance: 0.09\n  - quantity: Pearson r of log10 regional counts\n    value: 0.919\n    tolerance: 0.0919\n- id: fig3f-output-transmitters\n  statement: Across the primary ROIs, output neurons are mostly cholinergic (62.8% +- 14.2%),\n    then glutamatergic (15.5% +- 9.2%) and GABAergic (11.4% +- 8.2%).\n  source: Results, Comparison between FlyEM and FlyWire connectome data, paragraph 1; Figure 3f\n  quote: The highest percentage was acetylcholine (62.8%±14.2%), followed by glutamine\n    (15.5%±9.2%), then GABA (11.4%±8.2%) in neurotransmitter output.\n  data: elsewhere\n  where: FlyWire sc140 connectome and neurotransmitter predictions (Zenodo 10676866)\n  expected:\n  - quantity: acetylcholine share of output neurons, mean over regions\n    value: 62.8\n    tolerance: 6.28\n    unit: '%'\n  - quantity: glutamate share of output neurons, mean over regions\n    value: 15.5\n    tolerance: 1.55\n    unit: '%'\n  - quantity: GABA share of output neurons, mean over regions\n    value: 11.4\n    tolerance: 1.14\n    unit: '%'\n- id: figs3-2cd-apl-similarity\n  statement: The APL right neuron occupies a similar volume in FlyEM and FlyWire (Dice 0.716),\n    but its voxelwise post-synapse counts correlate weakly (r = 0.104), more after smoothing\n    (0.379 at 2 voxels, 0.66 at 8 voxels).\n  source: Extended Data Figure 3-2c and 3-2d\n  quote: Sørensen-Dice index (0.716) shows similarity ... Pearson correlation shows r=0.104, so\n    not similar at all. ... Similarity was increased (r=0.379). ... Similarity was increased\n    (r=0.66).\n  data: elsewhere\n  where: FlyEM hemibrain v1.2 (DVID) and FlyWire (Zenodo 10676866)\n  expected:\n  - quantity: Dice index of APL-R masks\n    value: 0.716\n    tolerance: 0.0716\n  - quantity: r of voxel post-synapse counts, unsmoothed\n    value: 0.104\n    tolerance: 0.0104\n  - quantity: r after 2-voxel smoothing\n    value: 0.379\n    tolerance: 0.0379\n  - quantity: r after 8-voxel smoothing\n    value: 0.66\n    tolerance: 0.066\n- id: fig4b-ppssi-distribution\n  statement: Over the 139,255 FlyWire neurons the PPSSI histogram resembles a normal distribution\n    with a mean near 0.5, so many neurons have unsegregated synapses.\n  source: Results, Unsegregated synapses contribute considerably to functional connectivity,\n    paragraph 1; Figure 4b; Methods, PPSSI\n  quote: Fig. 4b shows the result of applying PPSSI to 139,255 whole-brain neurons of FlyWire. The\n    result showed a histogram resembling a normal distribution.\n  data: elsewhere\n  where: FlyWire sc140 synapses (Zenodo 10676866)\n  expected:\n  - quantity: neurons with a PPSSI\n    value: 139255\n    tolerance: 0\n  criterion: PPSSI as M7. Reproduced when the neuron count matches and the mean PPSSI is within\n    0.4 to 0.6 (the Methods' \"its mean is close to 0.5\", read with a 0.1 margin, a choice made\n    here).\n- id: fig4a-unsegregated-ranking\n  statement: The unsegregated ranking puts APL and CT1 cells in the top four places in FlyWire,\n    and APL first in FlyEM.\n  source: Results, Unsegregated synapses contribute considerably to functional connectivity,\n    paragraph 1; Figure 4a; Extended Data Figure 4-1a\n  quote: APL and CT1 cells occupied the top 1–4 positions, indicating that we efficiently extracted\n    unsegregated neurons (Fig. 4a, Ext.Data.Fig.4-3a). APL was also at the top for FlyEM\n  data: elsewhere\n  where: FlyWire sc140 (Zenodo 10676866) and FlyEM cf0.8 (DVID v1.2)\n  criterion: Ranking by (1 - PPSSI) log10(W) (M7). Reproduced when ranks 1 to 4 in FlyWire are all\n    APL or CT1 cells and rank 1 in FlyEM is APL.\n- id: fig4c-segregated-ranking\n  statement: The segregated ranking puts two OA-AL2b2 cells first in FlyWire, and AOTU019_R and\n    DNa02_R first in FlyEM.\n  source: Figure 4c; Extended Data Figure 4-1c\n  quote: Segregated first (OA-AL2b2 cell) and second (OA-AL2b2 cell) ranking in FlyWire (sc140)\n    connectome data.\n  data: elsewhere\n  where: FlyWire sc140 (Zenodo 10676866) and FlyEM cf0.8 (DVID v1.2)\n  criterion: Ranking by PPSSI log10(W) (M7). Reproduced when the two top FlyWire cells are\n    OA-AL2b2 and the two top FlyEM cells are AOTU019_R and DNa02_R.\n- id: figs4-1ij-segregation-index-biased\n  statement: The segregation index of Schneider-Mizell et al. is heavily biased toward 0, with a\n    mean much closer to 0 than to 0.5, in both connectomes.\n  source: Methods, PPSSI, last paragraph; Extended Data Figure 4-1i and 4-1j\n  quote: Despite the [0 1] range of indices, the histogram is heavily biased toward 0 because of\n    the use of the logarithm, and the mean is much closer to 0 than 0.5 (Ext.Data.Fig.4-1i, j).\n  data: elsewhere\n  where: FlyWire sc140 (Zenodo 10676866) and FlyEM cf0.8 (DVID v1.2)\n  criterion: Segregation index on the DBSCAN clusters as plotNeuralFC.m computes it (1 - S/Snorm,\n    with entropy terms; 1 for neurons with only inputs or only outputs). Reproduced when the\n    mean is below 0.25 in both connectomes and below the PPSSI mean of fig4b-ppssi-distribution.\n    The 0.25 bound for \"much closer to 0\" is a choice made here.\n- id: fig4e-unsegregated-higher\n  statement: The SC matrix of unsegregated synapses (cPPSSI 0 to 0.1) has a significantly higher\n    FC-SC correlation than 99 random synapse samples of matched size, for both neuron and synapse\n    SC.\n  source: Results, Unsegregated synapses contribute considerably to functional connectivity,\n    paragraph 2; Figure 4e\n  quote: The FC-SC correlations of the SC matrices (unsegregated synapses) of neurons and synapses\n    were significantly higher than those of the randomly extracted samples (Fig. 4e, p=0, 6.5e-43\n  statistics:\n  - about: SC (neuron)\n    test: permutation test against 99 null SC matrices, normal approximation\n    p: 0\n    corrected: Bonferroni\n  - about: SC (synapse)\n    test: permutation test against 99 null SC matrices, normal approximation\n    p: 6.5e-43\n    corrected: Bonferroni\n  - about: null matrices' total connections against the unsegregated matrix (2,373,100)\n    test: normal approximation\n    p: 0.832\n  data: with_inputs\n  expected:\n  - quantity: total connections of the unsegregated SC matrix\n    value: 2373100\n    tolerance: 237310\n  criterion: M6 with the synapses of FlyWire sc140 whose cluster has cPPSSI below 0.1 (M7). For\n    neuron and synapse SC, reproduced when the unsegregated FC-SC correlation is above the null\n    mean with p < 0.05/6 for both; partially reproduced for one. Not reproduced when the null\n    totals differ from the selected total at p < 0.05. Rests on O2 and O3.\n- id: fig4f-segregated-lower\n  statement: The SC matrix of highly segregated synapses (cPPSSI 0.9 to 1) has a significantly\n    lower FC-SC correlation than random synapse samples.\n  source: Results, Unsegregated synapses contribute considerably to functional connectivity,\n    paragraph 2; Figure 4f\n  quote: A similar analysis was performed on synapses with a cPPSSI of 0.9–1, which surprisingly\n    showed a significantly lower FC-SC correlation (Fig. 4f, p=9.2e-14, 0\n  statistics:\n  - about: SC (neuron)\n    test: permutation test against 99 null SC matrices, normal approximation\n    p: 9.2e-14\n    corrected: Bonferroni\n  - about: SC (synapse)\n    test: permutation test against 99 null SC matrices, normal approximation\n    p: 0\n    corrected: Bonferroni\n  data: with_inputs\n  criterion: As fig4e-unsegregated-higher, with the synapses of clusters with cPPSSI 0.9 or more\n    (code target sp90). Reproduced when the FC-SC correlation is below the null mean with p <\n    0.05/6 for neuron and synapse SC; partially reproduced for one. Rests on O2 and O3.\n- id: fig4i-reciprocal-higher\n  statement: The SC matrix of reciprocal synapses within 2 um has a significantly higher FC-SC\n    correlation than random synapse samples.\n  source: Results, Unsegregated synapses contribute considerably to functional connectivity,\n    paragraph 3; Figure 4i\n  quote: The comparison of the SC matrix based on reciprocal synapses (<2 μm) with the null SC\n    matrices showed that the FC-SC correlation was significantly higher (Fig. 4I, p=0, 2.7e-32\n  statistics:\n  - about: SC (neuron)\n    test: permutation test against 99 null SC matrices, normal approximation\n    p: 0\n    corrected: Bonferroni\n  - about: SC (synapse)\n    test: permutation test against 99 null SC matrices, normal approximation\n    p: 2.7e-32\n    corrected: Bonferroni\n  data: with_inputs\n  criterion: As fig4e-unsegregated-higher, with the reciprocal synapses whose shortest\n    pre-to-post distance within the neuron is 2 um or less (code target rc20, makeSCcountMatrixFw.m).\n    Reproduced when the FC-SC correlation is above the null mean with p < 0.05/6 for neuron and\n    synapse SC; partially reproduced for one. Rests on O2 and O3.\n- id: figs4-1-flyem-permutation\n  statement: The same three results hold with the FlyEM connectome, unsegregated and reciprocal\n    synapses higher and segregated synapses lower than random samples.\n  source: Results, Unsegregated synapses contribute considerably to functional connectivity,\n    paragraphs 2 and 3; Extended Data Figure 4-1d, 4-1e and 4-1h\n  inferred: The text cites the FlyEM panels beside each FlyWire result without stating their\n    values; read from the citations \"Ext.Data.Fig.4-1d for FlyEM\", \"4-1e\" and \"4-1h\".\n  data: with_inputs\n  criterion: M6 with FlyEM cf0.8 synapses (the code's commented hb0sr80 targets and nulls in\n    plotFuncConnectivity.m). Reproduced when all three directions hold at p < 0.05/6 for SC\n    (neuron); partially reproduced when two do. Rests on O2 and O3.\n- id: fig4h-reciprocal-distances\n  statement: Reciprocal synapses are particularly abundant within 2 um, and most are\n    cholinergic or GABAergic.\n  source: Results, Unsegregated synapses contribute considerably to functional connectivity,\n    paragraph 3; Figure 4h\n  quote: They are particularly abundant within 2 μm (Ext.Data.Fig.4-2a,c for CT1 and APL cells),\n    and acetylcholine and GABA constitute the majority (Fig. 4h).\n  data: elsewhere\n  where: FlyWire sc140 (Zenodo 10676866)\n  criterion: Histogram of each reciprocal pair's shortest distance (code\n    checkReciprocalSynapseDistanceFw). Reproduced when the histogram's mode lies at or below 2\n    um and acetylcholine plus GABA make up more than half of the pairs.\n- id: fig5b-walking-activation\n  statement: In the group GLM of walking, the LAL, FB, IPS and GNG neuropils show strong\n    activity.\n  source: Results, Region suppression analysis during fly walking, paragraph 1; Figure 5b\n  quote: Similar to the results of Brezovec et al., our findings revealed that LAL, FB, and IPS\n    neuropils showed strong activity; the GNG neuropil, which is highly connected to leg\n    neuropils in the ventral nerve code [51], also exhibited strong activity.\n  data: with_inputs\n  criterion: Second-level t map of the walking regressor over the nine flies (M8, O1), height p <\n    0.001 and the code's cluster extent. Neuropils by O4. \"Strong\" is not defined; readings (a)\n    each of the four neuropils holds voxels of a surviving positive cluster with a peak t at\n    least half the brain-wide maximum, (b) each neuropil's mean t ranks in the top third of\n    neuropils. Reproduced when all four hold under one reading and one atlas; partially\n    reproduced when three do. The code's README prints one positive cluster of 416,801 voxels\n    with peak t = 14.7, to compare with. Rests on O1, O2 and O4.\n- id: fig5b-walking-suppression\n  statement: The Wedge and AVLP neuropils are inactive or strongly suppressed during walking.\n  source: Results, Region suppression analysis during fly walking, paragraph 1; Figure 5b\n  quote: Conversely, we found inactivity or strong suppression in the Wedge and AVLP neuropils.\n  data: with_inputs\n  criterion: As fig5b-walking-activation, the negative contrast. Reproduced when a surviving\n    negative cluster (t below the negative height threshold) lies mainly in WED or AVLP under one\n    atlas (O4), and neither neuropil holds surviving positive voxels covering more than half its\n    volume. The code's README prints two negative clusters (406 voxels, peak t = -6.14 at\n    voxel (82,78,12), and 260 voxels, peak t = -5.65 at (174,80,15)), to compare with.\n    Partially reproduced when one of the two neuropils meets this. Rests on O1, O2 and O4.\n- id: fig5-wagn\n  statement: The left Wedge-AVLP GABA neuron has unsegregated synapses (PPSSI 0.133), receives\n    212 synapses from 22 ascending neurons and sends 65 to WPNb, and its closest WPNb output to\n    AN input distance is 852.3 nm.\n  source: Results, Region suppression analysis during fly walking, paragraphs 1 and 2; Figure 5d\n    to 5g\n  quote: the left WAGN was strongly interconnected with WPNb tier 2/3 [54] and received input from\n    22 ascending neurons (ANs; Fig. 5d) ... it has highly unsegregated synapses (PPSSI=0.133). ...\n    It received input from ANs (212 synapses) mainly on the ventral side, and outputs to WPNb (65\n    synapses) ... the closest distance was 852.3 nm (Fig. 5g)\n  data: elsewhere\n  where: FlyWire (codex.flywire.ai at sc50 with connection threshold above 5 for the network;\n    sc140 for PPSSI; Zenodo 10676866); the neuron is FlyWire id 720575940644632087 in\n    plotNeuralFC.m\n  expected:\n  - quantity: PPSSI of the left WAGN\n    value: 0.133\n    tolerance: 0.0133\n  - quantity: ascending neurons giving input\n    value: 22\n    tolerance: 2.2\n  - quantity: synapses from ANs\n    value: 212\n    tolerance: 21.2\n  - quantity: synapses to WPNb\n    value: 65\n    tolerance: 6.5\n  - quantity: closest WPNb-output to AN-input distance\n    value: 852.3\n    tolerance: 85.23\n    unit: nm\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/okuno-2025.yaml paper/10.7554-elife.107990.1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n ": .*: " claims/okuno-2025.yaml | grep -v "^[0-9]*:#" | head
```

```
245:  quote: The difference was slightly larger (1.21 to 1.5-fold: r=0.378 for marmosets and
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/okuno-2025.yaml",
 "old_string": "  quote: The difference was slightly larger (1.21 to 1.5-fold: r=0.378 for marmosets and\n    r=0.46-0.57 for flies)",
 "new_string": "  quote: The difference was slightly larger (1.21 to 1.5-fold ... r=0.378 for marmosets and\n    r=0.46-0.57 for flies)"
}
```

```
The file claims/okuno-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n -E "^\s+[a-z_]+: [^\"'\[].*: " claims/okuno-2025.yaml; grep -n -E "^    [^-#].*: " claims/okuno-2025.yaml | grep -v -E "^\S+\s+(- )?[a-z_]+: " | head; python tools/claims_check.py claims/okuno-2025.yaml paper/10.7554-elife.107990.1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
import pprint
d=s.get('\$defs',s.get('definitions',{}))
for k,v in d.items():
  if 'xpect' in k or 'range' in k.lower(): print(k); pprint.pprint(v)
" | head -80; grep -rn -B1 -A4 "range:" claims/*.yaml | head -20
```

```
expected
{'additionalProperties': False,
 'properties': {'quantity': {'type': 'string'},
                'tolerance': {'minimum': 0, 'type': 'number'},
                'unit': {'type': 'string'},
                'value': {'type': 'number'}},
 'required': ['quantity', 'value'],
 'type': 'object'}
claims/economo-2018.yaml-75-#   rejected, 130 kept). The code (loadAndProcessData.m) counts per unit over the trials in its
claims/economo-2018.yaml:76:#   range: more than 50 correct trials of each type (strictly more; the Methods keep 50), more
claims/economo-2018.yaml-77-#   than 3.2 spikes per trial (spikes over the range of trials with spikes; the Methods do not
claims/economo-2018.yaml-78-#   name this rule, the code settles it), more than 65% correct for each type, and unit quality
claims/economo-2018.yaml-79-#   Excellent, Good or single. Readings: (a) the code's per-unit rule, (b) the Methods' session
claims/economo-2018.yaml-80-#   rule with at least 50 trials. The selection is checked by pt-tagged-units (61 and 69).
--
claims/kaku-2025.yaml-193-  source: Results, Coordination of breathing, licking, and swallowing, paragraph 2; Figure 1d
claims/kaku-2025.yaml:194:  quote: "Licking occurred at 6.23 ± 2 Hz (mean ± std, 95% range: 3.59 - 8.91 Hz) while breathing
claims/kaku-2025.yaml:195:    occurred at lower frequencies (4.02 ± 1.24 Hz, 95% range: 2.12 - 7.17 Hz; Figure 1d)"
claims/kaku-2025.yaml-196-  expected:
claims/kaku-2025.yaml-197-  - quantity: mean licking frequency
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/okuno-2025.yaml'
s=open(p).read()
rep={
"""  - quantity: fly FC-SC correlation at 50 ROIs, range over SCKm and DistKm
    value: [0.71, 0.81]
    tolerance: range widened by 10% of each bound, 0.639 to 0.891
  - quantity: fly FC-SC correlation at 1000 ROIs, range over SCKm and DistKm
    value: [0.6, 0.67]
    tolerance: range widened by 10% of each bound, 0.54 to 0.737
""":"""  - quantity: lowest fly FC-SC correlation at 50 ROIs (range 0.71 to 0.81)
    value: 0.71
    tolerance: 0.071
  - quantity: highest fly FC-SC correlation at 50 ROIs
    value: 0.81
    tolerance: 0.081
  - quantity: lowest fly FC-SC correlation at 1000 ROIs (range 0.6 to 0.67)
    value: 0.6
    tolerance: 0.06
  - quantity: highest fly FC-SC correlation at 1000 ROIs
    value: 0.67
    tolerance: 0.067
""",
"""  - quantity: fly FC-SC correlation at 10,000 ROIs, range over SCKm and DistKm
    value: [0.46, 0.57]
    tolerance: range widened by 10% of each bound, 0.414 to 0.627
""":"""  - quantity: lowest fly FC-SC correlation at 10,000 ROIs (range 0.46 to 0.57)
    value: 0.46
    tolerance: 0.046
  - quantity: highest fly FC-SC correlation at 10,000 ROIs
    value: 0.57
    tolerance: 0.057
""",
"""Reproduced when, under one
    reading, every value at 50 ROIs and every value at 1000 ROIs lies in its widened range.""":
"""A reported range holds inside
    the range widened by 10% of each bound (0.639 to 0.891 at 50 ROIs, 0.54 to 0.737 at 1000).
    Reproduced when, under one reading, every value at 50 ROIs and every value at 1000 ROIs
    lies in its widened range.""",
"""Reproduced when, under one reading of fig2d-fly-values, every value lies
    in the widened range.""":"""Reproduced when, under one reading of fig2d-fly-values, every value lies
    in the range widened by 10% of each bound, 0.414 to 0.627.""",
}
for a,b in rep.items():
    assert a in s, a[:40]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/okuno-2025.yaml paper/10.7554-elife.107990.1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -c "—" claims/okuno-2025.yaml; grep -n -i "rather" claims/okuno-2025.yaml; grep -c "criterion:" claims/okuno-2025.yaml; grep -c "data: with_inputs" claims/okuno-2025.yaml; grep -c "data: elsewhere" claims/okuno-2025.yaml; git status --short
```

```
0
24
19
11
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
?? claims/okuno-2025.yaml
?? scripts
```

**Agent**

I wrote `claims/okuno-2025.yaml` and the quote checker passes it with no problems. Nothing is committed.

**Text read.** The eLife Reviewed Preprint v1 (9 October 2025, not revised), from the publisher's HTML. It has the main text, figure legends, Methods, Data availability and the Extended Data figure legends, which are the paper's only supplement. There was no PDF, so I could not read any figure. The text lost the Methods' displayed equations (the FC-SC detection and correlation score, cPPSSI, PPSSI and the two ranking scores); I took them from the code. I read the code at github.com/takuto-okuno-riken/flywalk, commit 4b92add (11 August 2025), the last commit before v1. Later commits answer the reviewers and change the method, so they are not this version's.

**Claims.**
- **Count:** 30 claims. 29 have quotes; one is `inferred` (the FlyEM permutation panels, which the text only cites).
- **Statistics:** 10 values: Mann-Whitney p<1.67e-4; acetylcholine r=0.39, p=0.0013 and GABA r=-0.25, p=0.046; the permutation p-values of Fig. 4e, f and i.
- **Criteria:** 24 claims have one.
- **Data:** 19 are `with_inputs`, because they set the dataset's FC against EM connectome SC or use the template and neuropil atlas from the code repository. 11 are `elsewhere`, on the FlyEM and FlyWire connectomes alone. None runs on the dandiset alone: even the walking GLM needs the repository's template and atlas.

**Details left open, and the readings named:**
- **O1, walking regressor:** the Methods say "1σ … divided into walking and other". The code builds a graded regressor (clipped at 1 SD, 10th-percentile floor). I followed the code and named a binary regressor as a variant.
- **O2, registration:** neither the paper nor the code gives the SPM12 or ANTs settings. Standard choice: SPM12 defaults with ANTs SyN; variant: rigid plus affine. Outcomes are marked as resting on it.
- **O3, sign of FC:** the code correlates SC with |mean z-FC|, the Methods just say "FC". I followed the code; signed FC is a variant.
- **O4, atlas for the GLM regions:** (a) the hemibrain atlas, (b) the JFRC2010 atlas also in the repository.
- **Per claim:** how "optimal" is judged in Fig. 1 (best in each ROI type, or best on average); which ROI type and SC kind give the 50, 1000 and 10,000 ROI ranges and the 20 ROI values; what "strong" activity means in Fig. 5b (peak t, or neuropil rank).
- **Thresholds I set myself:** some bars are mine, not the paper's, and each criterion says so. They are r ≤ -0.9 for "linear", a 0.05 margin for "ineffective", 0.4 to 0.6 for "mean close to 0.5", and below 0.25 for "biased toward 0".

**Missing from the paper:**
- **Values only in figures:** these cannot be known without the figures, mainly the per-method scores of Fig. 1 and the curves of Fig. 2b and 2c.
- **Number of Bonferroni comparisons:** not stated for Fig. 2c, so the criterion uses the printed threshold.
- **Steps missing from the code:** the NWB-to-NIfTI extraction and the registration scripts.
- **ROI atlases and connection lists:** the SCKm and DistKm atlases and the preprocessed connection lists are not in the repository. They are on Zenodo 10.5281/zenodo.15532271, and the claims file names that record.

## End of run

48 turns, 7 minutes, $2.96 at API prices, result: success.
