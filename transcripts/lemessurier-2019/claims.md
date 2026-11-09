# crcns-ssc-10 · claims · run 42475975709

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453/ claims/crcns-ssc-10/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,185p docs/protocol.md; cat claims/001453/*.yaml; wc paper/*.txt; head -30 paper/10.7554-elife.46321.txt; head -40 paper/ssc-10.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/69d6615e-8d15-4c68-835d-6a6759b9191d/tool-results/bc3b1piyf.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 560 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.46321.txt",
 "offset": 30
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.46321.txt",
 "offset": 30,
 "limit": 90
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.46321.txt",
 "offset": 120,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.46321.txt",
 "offset": 320
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text with Methods and figure supplement legends is present. Next I'll read the linked code and the data descriptor's summary.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/alemessurier/imaging_analysis_pipeline 2>&1 | tail -3; cd imaging_analysis_pipeline && git log -1 --format='%H %cd' && find . -type f | grep -v '^./.git/' | wc -l && find . -type d | grep -v .git
```

```
5a21c9fef839fbc8eb79fa24f16662426e36904f Wed Jul 10 12:27:39 2019 -0700
67
.
./rawDataPipeline
./plotting_2017
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "paper/ssc-10.data-description.txt",
 "offset": 40,
 "limit": 330
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/imaging_analysis_pipeline && find . -type f -not -path './.git/*' | xargs wc -l | sort -k2; cat README* 2>/dev/null | head -50
```

```
674 ./LICENSE
    35 ./README.md
   156 ./plotting_2017/compare_SCvNC_inBarr.m
   224 ./plotting_2017/compare_npCorrection_20171327.m
   268 ./plotting_2017/make_CorrAnalysisPlots.m
   546 ./plotting_2017/make_CorrAnalysisPlots_L4.m
   192 ./plotting_2017/make_CorrAnalysisPlots_NPsubCompare.m
   502 ./plotting_2017/make_CorrAnalysisPlots_NPsubCompare_old.m
   671 ./plotting_2017/make_CorrAnalysisPlots_SWvCW.m
   232 ./plotting_2017/make_CorrAnalysisPlots_eqSamp.m
   125 ./plotting_2017/make_CorrAnalysisPlots_eqSamp_L4.m
   612 ./plotting_2017/make_CorrAnalysisPlots_old.m
   409 ./plotting_2017/make_CorrAnalysisPlots_surround.m
   450 ./plotting_2017/make_responseDistPlots.m
   311 ./plotting_2017/make_responseDistPlots_BarrVSept.m
   306 ./plotting_2017/make_responseDistPlots_eqSamp.m
   262 ./plotting_2017/make_responseDistPlots_npSubCompare.m
   110 ./plotting_2017/make_responseDists_eqSamp.m
   101 ./plotting_2017/plot_CWtunedInBarr_byRad.m
   116 ./plotting_2017/plot_CWtunedInD2_byRad.m
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/imaging_analysis_pipeline && cat rawDataPipeline/permutationTest.m rawDataPipeline/permutationTest_median.m rawDataPipeline/permuteTest_whisk_2016.m rawDataPipeline/analysisTemplate.m; grep -n "framesEvoked\|timeEvoked\|bl_length\|mafdr\|fdr" -r rawDataPipeline | head -30
```

```
function [ P ] = permutationTest(stimLocked,spont,numReps )
%Permutation test for difference in means between two distributionss

T=abs(nanmean(stimLocked)-nanmean(spont));
dim1=find(size(stimLocked)>1);
pooled=cat(dim1,stimLocked,spont);

for t=1:numReps
    indsA=randsample(1:length(pooled),length(stimLocked));
    A=pooled(indsA);
    indsB=ones(length(pooled),1);
    indsB(indsA)=0;
    indsB=logical(indsB);
    B=pooled(indsB);
    PT(t)=abs(nanmean(A)-nanmean(B));
end
PT(t+1)=T;
P=sum(PT>=T)/length(PT);


[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/imaging_analysis_pipeline && grep -n -i "eqbw\|equal\|eBW\|bestwhisk\|BW_\|tuned\|ranksum\|ttest\|fishertest\|fexact\|anova\|permutationTest\|kmeans\|bins\s*=\|binEdges\|edges" plotting_2017/somatotopy_plots_2018_eqSamp.m | head -80
```

```
1:function [pvals,CWtuned_byRad,CWtuned_byRad_num,CWresp_byDist]=somatotopy_plots_2018_eqSamp( paths_NH,paths_EN,npSub,rval,ROIs_EN,ROIs_NH )
29:%% plot percent of cells tuned to CW by radius (EBW)
31:[mean_dist_NH,mean_percMatch_NH,sem_percMatch_NH,percMatch_byBarr_NH,percMatch_NH,num_ROIs_NH,CWtunedInds_binned_NH,binEdges]=plot_CWtunedByRad(paths_NH,npSub,rval,15,ROIs_NH);
32:[mean_dist_EN,mean_percMatch_EN,sem_percMatch_EN,percMatch_byBarr_EN, percMatch_EN,num_ROIs_EN,CWtunedInds_binned_EN]=plot_CWtunedByRad(paths_EN,npSub,rval,binEdges,ROIs_EN);
34:CWtuned_byRad.binEdges=binEdges;
35:CWtuned_byRad.percMatch_NH=percMatch_NH;
36:CWtuned_byRad.percMatch_EN=percMatch_EN;
60:for i=1:numel(CWtunedInds_binned_NH)
61:    P(i)=permutationTest(CWtunedInds_binned_NH{i},CWtunedInds_binned_EN{i},10000);
64:CWtuned_byRad.pvals=P;
87:ylabel('% tuned to CW (EBW)')
114:% ylabel('mean % of cells tuned to CW (EBW)')
122:% %     [~,pval]=ttest2(percMatch_byBarr_NH{i},percMatch_byBarr_EN{i});
130:%% plot percent of cells tuned to CW by radius (absolute BW)
131:[mean_dist_num_NH,mean_percMatch_num_NH,sem_percMatch_num_NH,percMatch_byBarr_num_NH,percMatch_num_NH,num_ROIs_num_NH,CWtunedInds_binned_NH,binEdges]=plot_CWtunedByRad_num(paths_NH,npSub,rval,15,ROIs_NH);
132:[mean_dist_num_EN,mean_percMatch_num_EN,sem_percMatch_num_EN,percMatch_byBarr_num_EN, percMatch_num_EN,num_ROIs_num_EN,CWtunedInds_binned_EN]=plot_CWtunedByRad_num(paths_EN,npSub,rval,binEdges,ROIs_EN);
134:P=zeros(1,numel(CWtunedInds_binned_EN));
136:    P(j)=permutationTest(CWtunedInds_binned_NH{j},CWtunedInds_binned_EN{j},10000);
138:CWtuned_byRad_num.binEdges=binEdges;
139:CWtuned_byRad_num.percMatch_NH=percMatch_num_NH;
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/imaging_analysis_pipeline && grep -rn "whiskPref\s*=\|function.*whiskPref\|eqBW\|findEBW\|find_CWtuned_byRad\b\|function.*find_CWtuned\|corrPairs\|function .*sigCorr\|noiseCorr\s*=\|function.*decod" --include=*.m . | head -30; echo ---; grep -rhn "^\s*function" --include=*.m . | sed 's/.*=\s*//;s/(.*//' | sort -u | head -100
```

```
./plotting_2017/make_CorrAnalysisPlots_NPsubCompare.m:175:function h=sigCorrByDist_rval(group,binEdges)
./plotting_2017/somatotopy_plots_2017_L4.m:516:                    %                     whiskPref=whiskPref(2);
./plotting_2017/somatotopy_plots_2017_L4.m:570:                    %                     whiskPref=whiskPref(2);
./plotting_2017/somatotopy_plots_2017_L4.m:618:                    %                     whiskPref=whiskPref(2);
./plotting_2017/somatotopy_plots_2017_L4.m:621:            results=find_CWtuned_byRad( traceByStim, sigROIs,whiskPref,ROItoBarrel);
./plotting_2017/somatotopy_plots_2017_L4.m:664:                    %                     whiskPref=whiskPref(2);
./plotting_2017/somatotopy_plots__NPsubCompare_2017.m:314:            whiskPref=whiskPref(rval);
./plotting_2017/somatotopy_plots__NPsubCompare_2017.m:315:            results=find_CWtuned_byRad( traceByStim, permTestResults,whiskPref,ROItoBarrel);
./plotting_2017/voronoi_decode_detect.m:1:function voronoi_decode_detect(paths_EN,paths_NH)
./plotting_2017/plot_CWtunedInBarr_byRad.m:53:    function [mean_dist,percMatch,num_ROIs,percentCWtuned,num_ROIs_inc]=find_CWtuned_inBarr(pathNames,npSub)
./plotting_2017/plot_CWtunedInBarr_byRad.m:67:            results=find_CWtuned_byRad( traceByStim, permTestResults,whiskPref,ROItoBarrel);
./plotting_2017/plot_CWtunedInD2_byRad.m:68:    function [mean_dist,percMatch,num_ROIs,percentCWtuned,num_ROIs_inc]=find_CWtuned_inBarr(pathNames,npSub)
./plotting_2017/somatotopy_plots_2018_eqSamp.m:407:%                     whiskPref=whiskPref(2);
./plotting_2017/somatotopy_plots_2018_eqSamp.m:437:%                     whiskPref=whiskPref(2);
./plotting_2017/somatotopy_plots_2018_eqSamp.m:630:%                     whiskPref=whiskPref(2);
./plotting_2017/somatotopy_plots_2018_eqSamp.m:704:%                     whiskPref=whiskPref(2);
./plotting_2017/somatotopy_plots_2018_eqSamp.m:767:%                     whiskPref=whiskPref(2);
./plotting_2017/somatotopy_plots_2018_eq
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/imaging_analysis_pipeline && grep -rn "whiskPref" --include=*.m . | grep -v "^\S*:\s*%" | grep -v "whiskPref=whiskPref(2)" | head -20; grep -rn "load(" plotting_2017/somatotopy_plots_2018_eqSamp.m | head; grep -rn "sigROIs\s*=\|mafdr\|fdr" --include=*.m plotting_2017 | head
```

```
./plotting_2017/somatotopy_plots_2017_L4.m:279:                ~,~,~,~,~,~,~,whiskPref ] = load_nonNPsub_data( paths_EN{K});
./plotting_2017/somatotopy_plots_2017_L4.m:282:                ~,~,~,~,~,~,~,whiskPref ] = load_NPsub_data_L4( paths_EN{K},2 );
./plotting_2017/somatotopy_plots_2017_L4.m:285:    numBW_EN{K}=cellfun(@(x)length(whiskPref.(x){1}),cellNames,'Uni',1);
./plotting_2017/somatotopy_plots_2017_L4.m:297:                ~,~,~,~,~,~,~,whiskPref ] = load_nonNPsub_data( paths_NH{K} );
./plotting_2017/somatotopy_plots_2017_L4.m:300:                ~,~,~,~,~,~,~,whiskPref ] = load_NPsub_data_L4( paths_NH{K},2 );
./plotting_2017/somatotopy_plots_2017_L4.m:303:    numBW_NH{K}=cellfun(@(x)length(whiskPref.(x){1}),cellNames,'Uni',1);
./plotting_2017/somatotopy_plots_2017_L4.m:508:                        deltaF,sampRate,whiskPref ] = load_nonNPsub_data( pathNames{J} );
./plotting_2017/somatotopy_plots_2017_L4.m:512:                        deltaF,sampRate,whiskPref ] = load_NPsub_data_L4( pathNames{J},2 );
./plotting_2017/somatotopy_plots_2017_L4.m:562:                        deltaF,sampRate,whiskPref ] = load_nonNPsub_data( pathNames{J} );
./plotting_2017/somatotopy_plots_2017_L4.m:566:                        deltaF,sampRate,whiskPref ] = load_NPsub_data_L4( pathNames{J},2 );
./plotting_2017/somatotopy_plots_2017_L4.m:610:                        deltaF,sampRate,whiskPref ] = load_nonNPsub_data( pathNames{J} );
./plotting_2017/somatotopy_plots_2017_L4.m:614:                        deltaF,sampRate,whiskPref ] = load_NPsub_data_L4( pathNames{J},2 );
./plotting_2017/somatotopy_plots_2017_L4.m:621:            results=find_CWtuned_byRad( traceByStim, sigROIs,whiskPref,ROItoBarrel);
./plotting_2017/somatotopy_plots_2017_L4.m:656:                        deltaF,sampRate,whiskPref ] = load_nonNPsub_data( pathNames{J} );
./plotting_2017/somatotopy_plots_2017_L4.m:660:                        deltaF,sampRate,whiskPref ] = load_NPsub_data_L4( pathNames{J},2 );
./plotting_2017/s
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/imaging_analysis_pipeline && defs=$(grep -rhoE "^\s*function\s+(\[[^]]*\]\s*=\s*|\w+\s*=\s*)?\w+" --include=*.m . | sed -E 's/.*[= ]//' | sort -u); calls=$(grep -rhv "^\s*%" --include=*.m plotting_2017 | grep -oE "\b[a-z][A-Za-z0-9_]*_[A-Za-z0-9_]*\(" | tr -d '(' | sort -u); comm -23 <(echo "$calls") <(echo "$defs") | tr '\n' ' '
```

```
ax_L23 ax_L4 cShuff_clust_EN cShuff_clust_NH cVar_clust_EN cVar_clust_NH cellsToPlot_EN cellsToPlot_NH chisquare_binned colorCodeByWhiskResponse_norm colorCodeByWhiskResponse_norm_MW colorCodeByWhiskResponse_norm_SWorCW colorCodeROIs_byWhiskPref compare_4means_bar decoder_PandPos dist_EN dist_NH fano_all_EN fano_all_NH find_BWmatchCW find_CWresponse_byRad find_CWtuned_byRad find_CWtuned_byRad_num find_D2tuned_byRad find_SWtunedCells find_corrInBarrel find_corrInBarrelvsAcross find_corrToSWs find_corr_sameBW find_corr_simple find_percent_responsive find_rankedRFs find_response_dists find_septalVbarrel find_sigROIs fname_s1 fullfield_EN fullfield_NH h_EN h_NH hp_info hp_ingo inArcNC_byROI_EN inArcNC_byROI_NH inArcSC_byROI_EN inArcSC_byROI_NH inBarr_EN inBarr_NH inColNC_byROI_EN inColNC_byROI_NH inColSC_byROI_EN inColSC_byROI_NH inRowNC_byROI_EN inRowNC_byROI_NH inRowSC_byROI_EN inRowSC_byROI_NH inds_whisk_EN inds_whisk_NH load_NPsub_data load_NPsub_data_L23 load_NPsub_data_L4 load_nonNPsub_data make_tunedInColPlots meanCorr_EN meanCorr_NH meanDist_EN_inBarr meanDist_EN_xBarr meanDist_NH_inBarr meanDist_NH_xBarr mean_EN_inBarr mean_EN_xBarr mean_NH_inBarr mean_NH_xBarr mean_dist mean_dist_EN mean_dist_NH mean_percMatch mean_responseDF mean_responseDF_EN mean_responseZ mean_responseZ_EN notBoxPlot_ENvNH numBins_EN numBins_EN_CW numBins_EN_xBarr numBins_NH numBins_NH_CW numBins_NH_xBarr numROIsBin_EN numROIsBin_NH num_ROIs num_ROIs_EN num_ROIs_inc p_EN p_NH paths_EN paths_NH paths_to_include percMatch_all perfByWhisk_EN perfByWhisk_NH permutationTest_mean plot_2cdfs plot_4cdfs plot_CWresponseByRad plot_CWvsSWtunedDists plot_CWvsSWtunedDists_NPsubCompare plot_MWtunedDists plot_allROI_positions plot_scatterRLine r2_EN r2_NH rankedRFs_EN rankedRFs_NH rankedRFs_sponNorm_EN rankedRFs_sponNorm_NH resample_equalPos response_Z_all response_dF_all responses_plot_EN responses_plot_NH results_CW_EN results_CW_NH results_EN results_NH results_SW_EN results_SW_NH results_all results_
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/imaging_analysis_pipeline && for f in make_CorrAnalysisPlots.m make_responseDistPlots.m plot_ENvsNH_CWvsSW.m voronoi_decode_detect.m; do echo "=== $f"; grep -n -v "^\s*%" plotting_2017/$f | grep -n -i "binEdges\s*=\|edges\|0:75\|75\|150\|anova\|permutationTest\|ttest\|ranksum\|kstest\|multcompare\|numel(.*)>=\|>=3\|>2\|find_\|decoder\|zscore" | head -25; done
```

```
=== make_CorrAnalysisPlots.m
15:18:        sigROIs=find_sigROIs(permTestResults,traceByStim);
19:22:    [ results ] = find_corr_sameBW( traceByStim,sponTrace,sigROIs,framesEvoked,ROI_positions,mag);
39:43:        sigROIs=find_sigROIs(permTestResults,traceByStim);
44:48:    [ results ] = find_corr_sameBW( traceByStim,sponTrace,sigROIs,framesEvoked,ROI_positions,mag);
69:75:shuffNC_EN_all=cat(1,results_EN(:).shuffNC);
94:109:            sigROIs=find_sigROIs(permTestResults,traceByStim);
99:114:    [ results ] = find_corrInBarrelvsAcross( sigROIs,traceByStim,framesEvoked,ROIsInBarrel,sponTrace,ROI_positions,mag);
119:134:            sigROIs=find_sigROIs(permTestResults,traceByStim);
124:139:    [ results ] = find_corrInBarrelvsAcross( sigROIs,traceByStim,framesEvoked,ROIsInBarrel,sponTrace,ROI_positions,mag);
134:150:NC_EN_inBarr=cat(1,results_EN(:).NC_inBarr);
155:172:    function [numBins,binEdges,meanDist,meanNC,semNC,meanSC,semSC,allNC,allSC,shuff_meanNC,...
156:173:            shuff_semNC,shuff_meanSC,shuff_semSC]=binCorrByDist(NC,shuffNC,SC,shuffSC,ROIdist,binEdges)
158:175:        
166:183:        [numBins,binEdges,binInds]=histcounts(ROIdist,binEdges);
246:263:        pval=permutationTest(NH,EN,10000);
=== make_responseDistPlots.m
5:7:    medianRs_EN,fano_CW_EN]=find_response_dists(paths_EN,npSub,rval,cellsToPlot_EN);
9:11:    medianRs_NH,fano_CW_NH]=find_response_dists(paths_NH,npSub,rval,cellsToPlot_NH);
18:24:[EN,~,binEdgesX,binEdgesY] = scatterPlot_marginals( worstSWs_rawDF_EN,bestSWs_rawDF_EN,[],[] );
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims | head -50; grep -rn -i "sem\b\|± " claims/*/*.yaml | grep -i "toleran\|sem" | head -15; sed -n 1,80p tools/claims_check.py | head -80
```

```
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
000016
000017
000019
000023
000034
000035
000036
000037
000041
000044
[... 125 more lines not kept]
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
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"; ls claims | grep -i crcns | head;
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
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/crcns-hc-10; head -60 claims/crcns-hc-10/*.yaml
```

```
10.1016-j.neuron.2014.03.034.yaml
# Claims for Lee, Marchionni, Bezaire, Varga, Danielson, Lovett-Barron, Losonczy & Soltesz (2014),
# Neuron 82:1129-1144, on CRCNS data set hc-10 (doi:10.6080/K00P0WXQ).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: the version of record with its Supplemental Information, as supplied under paper/
# (PyMuPDF text of the journal PDF): Results, Discussion, Experimental Procedures, the legends
# of Figures 1 to 6 and S1 to S5, Table S1 and the Supplemental Experimental Procedures. The
# extracted text prints micrometres as "mm" and some minus signs as a replacement character.
# Values shown only in Figures S1E to S1H and S3F were read from the PDF pages (rendered here)
# and are marked as read from a figure.
#
# Code read: the model code the paper links, ModelDB accession 153280 ("superdeep", NEURON),
# downloaded from modeldb.science/download/153280 on 2026-11-06 (zip sha256 333fd221...fe405,
# README "Last updated on May 15, 2014"). It holds the cell templates, connectivity, stimulation
# and job scripts of the network model of Figures 4C to 4F and S3. It holds no analysis of the
# experimental recordings, so it fixes none of the criteria for the intrinsic properties. The
# lab page the paper also links (ivansolteszlab.org/models/superdeep.html, said to hold the
# simulation results and analysis procedures) is now a parked domain, and the Open Source
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/imaging_analysis_pipeline && sed -n 100,118p rawDataPipeline/rawDataPipeline_shared.m; cat rawDataPipeline/slidingAvg_rawF.m rawDataPipeline/deltaF_simple.m rawDataPipeline/npSubtract_preDF.m | grep -v "^\s*%" | head -60; git remote -v | head -1
```

```
Stimuli = make_Stimuli( dir_reduced,fns,StimISI,Metadata );

%% make traceByStim

% generate vector of frames for measuring evoked activity post-stimulus
framesEvoked=(ceil(bl_length*sampRate(1))+1):(ceil(bl_length*sampRate(1))+ceil(timeEvoked*sampRate(1))); 

% make structure collecting dF/F in time window before and after each stim iteration by ROI and by whisker identity
[ traceByStim, stimFramesAll ] = make_traceByStim( whisk,Stimuli,Metadata,deltaF,bl_length,timePostStim );

%% find spontaneous activity
[ sponTrace ] = make_sponTrace( Stimuli,sampRate(1),deltaF,bl_length,timePostStim );

%% permutation test for whisker responsiveness

%for each ROI, tests for difference in means between spontaeous dF/F and
%dF/F evoked by each whisker. Returns p-value for each whisker. For further analysis must be corrected for 9 comparisons using FDR. 
[ permTestResults ] = permuteTest_whisk_2016( sponTrace,traceByStim,numBoots,framesEvoked,permTestType );

function [ filtTrace ] = slidingAvg_rawF( rawTrace,ptsToAvg,type )
[... 56 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-ssc-10/10.7554-elife.46321.yaml",
 "content": "# Claims for LeMessurier, Laboy-Juarez, McLain, Chen, Nguyen & Feldman (2019), eLife 8:e46321,\n# \"Enrichment drives emergence of functional columns and improves sensory coding in the whisker\n# map in L2/3 of mouse S1\", on CRCNS data set ssc-10 (doi:10.6080/K0DB801M).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-08,\n# protocol as stated in docs/protocol.md (Reader), version pilot-13.\n#\n# Text read: the version of record, PMC6697414 (Europe PMC JATS XML, flattened), as supplied\n# under paper/: Results, Discussion, Materials and methods, Table 1, and the legends of Figures 1\n# to 7 and their figure supplements (Figure 1 S1, Figure 2 S1 and S2, Figure 3 S1, Figure 4 S1\n# and S2, Figure 5 S1 and S2). The paper has no other supplementary text. Table 1 is flattened\n# to one cell per line and was read in that form. No PDF of the paper was supplied; no figure\n# was read.\n#\n# Code read: github.com/alemessurier/imaging_analysis_pipeline, commit 5a21c9fef839fbc8eb79fa24f16662426e36904f\n# (2019-07-10), the repository the paper links. rawDataPipeline/ holds the reduction from movies\n# to ROI time series, dF/F, trial-aligned traces (traceByStim, sponTrace) and the responsiveness\n# test (permuteTest_whisk_2016.m). plotting_2017/ holds the figure scripts. Many functions those\n# scripts call are not in the repository, among them find_sigROIs, the computation of whiskPref\n# (the equivalent best whiskers), find_CWtuned_byRad, find_rankedRFs, find_corr_simple,\n# find_corrInBarrelvsAcross, decoder_PandPos and permutationTest_mean. What the code fixes:\n#   - Evoked window: frames ceil(0.5*fs)+1 to ceil(0.5*fs)+ceil(1*fs) of each trial-aligned\n#     trace, i.e. the 1 s after onset, with traces baseline-corrected to the 0.5 s before onset\n#     (rawDataPipeline_shared.m, analysisTemplate.m), as the Methods say.\n#   - EN against NH comparisons of means: permutationTest.m, 10,000 label shuffles of the pooled\n#     units, statistic the absolute difference of means (two-sided), p the fraction of shuffles\n#     (the observed value included) at least as large. Used in the figure scripts for responses\n#     by distance, receptive fields, correlations and spontaneous activity.\n#   - Fractions tuned by distance bin: the figure script somatotopy_plots_2018_eqSamp.m compares\n#     EN with NH by permutationTest on the 0/1 tuned indicators, where the legend of Figure 3A\n#     names Fisher's exact test. The legend is followed; the code's test is a variant.\n# Where the code and the Methods differ, the Methods are followed and the code's choice is a\n# variant: the responsiveness test is one-sided on means in the Methods (\"greater than the 95th\n# percentile\"), two-sided in permuteTest_whisk_2016.m, with mean or median set per field\n# (permTestType, 'median' in analysisTemplate.m); the temporal filter is a four-frame moving\n# median in the Methods, a five-frame window (ptsToAvg = 2) in the code; F0 is the 20th percentile\n# of the 80 s movie in the Methods, the 5th percentile in deltaF_simple.m.\n#\n# Data the paper used. Mice raised from weaning (P20-21) either enriched (EN, 2-3 littermates,\n# tactile toys changed every 2-4 days) or normally housed (NH, one littermate, no toys), for\n# 25-50 days. Drd3-Cre mice (L2/3 pyramidal cells; NH 7 mice, 11 fields; EN 7 mice, 11 fields)\n# and Scnn1a-Tg3-Cre mice (L4 excitatory cells; NH 5 mice, 6 fields; EN 6 mice, 8 fields), with\n# Cre-dependent GCaMP6s, imaged under isoflurane and chlorprothixene at 30 Hz through a cranial\n# window, fields ~400 x 400 um (L2/3, 100-250 um deep) or ~300 x 300 um (L4). Nine whiskers in a\n# 3 x 3 array centred on D2 (C1-C3, D1-D3, E1-E3) deflected one at a time with trains of five\n# 300 um deflections 100 ms apart, interleaved with blank trials, 5 s apart in random order,\n# 60 +/- 10 repetitions per whisker, ~40 movies of 80 s per field. Manually drawn soma ROIs; no\n# neuropil subtraction for L2/3 in the main analysis, neuropil weight r = 0.3 for L4. ROI\n# positions relative to the nine barrel centroids from cytochrome oxidase histology, barrel\n# radii, and whether each ROI lies over a barrel or a septum. Measured variables: the evoked\n# dF/F per trial, its median per whisker (the receptive field), responses z-scored to blank\n# trials, best and equivalent best whiskers, signal and noise correlations of pairs, and\n# logistic-regression decoders of single trials. Units of most tests are ROIs or ROI pairs\n# pooled across fields and mice. Separately, juxtacellular recordings with GCaMP6s imaging of 10\n# L2/3 cells in 5 C57BL/6 mice (Figure 1F) and a behavioural cohort of 6 NH and 6 EN mice\n# (data not shown).\n#\n# The CRCNS data set, by its title and description, holds the population imaging of the four\n# groups (raw and neuropil time series, dF/F, stimuli, trial-aligned traces, responsiveness\n# p-values, ROI positions relative to each barrel). Whether it holds the juxtacellular recordings,\n# or the barrel radii, is the author's to find.\n#\n# Methods common to the criteria below, from the Methods unless said otherwise:\n#   - Evoked response of a trial: mean dF/F in the 1 s after train onset minus mean dF/F in the\n#     0.5 s before (Methods, Quantification of whisker responses).\n#   - Responsive ROI: for some whisker, the per-trial evoked responses exceed those of blank\n#     trials by a permutation test of the difference in means (10,000 shuffles, one-sided at the\n#     95th percentile), p-values Benjamini-Hochberg corrected over the nine whiskers at 0.05.\n#     Variant: the p-values stored per ROI by the pipeline (two-sided, mean or median per the\n#     field's permTestType), BH corrected. ROIs with nuclear GCaMP were excluded by the authors.\n#   - Which responsive ROIs enter. Methods: for L2/3 \"all whisker-responsive ROIs located within\n#     any of the nine columns\"; for L4 only responsive ROIs in columns C1, C2 and C3. Open for\n#     L2/3: whether ROIs over septa enter the point representation and tuning-by-distance\n#     analyses. Readings (A) all responsive ROIs of the field; (B) only ROIs over one of the nine\n#     barrels. The counts favour (A) for Figures 2 and 3 (475 NH responsive cells, of which 344 lie\n#     within a column). Correlations use only ROIs over (L2/3) or in (L4) a barrel (Methods).\n#   - Receptive field: the median evoked response to each whisker over its trials (Methods).\n#     Response normalised to spontaneous activity: that median z-scored to the distribution of\n#     evoked-window responses on blank trials, read as (median - mean of blank) / SD of blank,\n#     the standard z-score; centring on the blank median is a variant (Methods, Quantification).\n#   - Best whisker (BW): the whisker with the largest mean evoked dF/F (Results, Whisker map\n#     topography, paragraph 2). The median (the receptive field of the Methods) is a variant.\n#   - Equivalent best whiskers (eBWs): whiskers whose response is \"statistically\n#     indistinguishable from the BW (see Materials and methods)\". Neither the Methods nor the code\n#     (whiskPref is loaded precomputed) say how. OPEN. Readings (E1) the paper's own permutation\n#     test of the difference in means (10,000 shuffles, two-sided as in permutationTest.m) between\n#     the BW's per-trial evoked responses and each other whisker's, p >= 0.05 uncorrected meaning\n#     equivalent; (E2) as E1 with Benjamini-Hochberg correction over the eight comparisons, as the\n#     Methods correct the responsiveness test; (E3) as E1 on medians (permutationTest_median.m).\n#   - Distance to a column: Euclidean distance in um from the ROI to the centroid of the\n#     reference whisker's barrel (Methods, 2-photon imaging, paragraph 4). In by-distance\n#     analyses each responsive ROI enters once for each of the nine reference whiskers, at its\n#     distance to that whisker's column; the bin counts the paper prints (406 and 419 NH cells at\n#     225-300 and 525-600 um, from 475 responsive cells) require this.\n#   - Columnar whisker (CW): the whisker of the barrel an ROI lies over (Results). Rows C, D, E run\n#     dorsal to ventral and arcs 1, 2, 3 caudal to rostral, so for D2 the within-arc -1 and +1\n#     row whiskers are C2 and E2 and the within-row -1 and +1 arc whiskers are D1 and D3\n#     (Results, Enrichment sharpens whisker receptive fields, paragraph 3).\n#   - EN against NH tests on means: the permutation test of the difference in means named in the\n#     Results, as in permutationTest.m (two-sided, 10,000 shuffles), with ROIs or pairs pooled\n#     across fields and mice as the units. Values reported as mean +/- SEM have the SEM as\n#     tolerance; other values have 10% of the value.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: ssc-10\n  doi: 10.6080/K0DB801M\npaper: doi:10.7554/elife.46321\nclaims:\n- id: table1-mice-and-fields\n  statement: The population imaging used 7 NH and 7 EN Drd3-Cre mice with 11 imaging fields each,\n    and 5 NH and 6 EN Scnn1a-Tg3-Cre mice with 6 and 8 imaging fields.\n  source: Table 1\n  inferred: The counts are in the columns N mice and N imaging fields of Table 1; no sentence lists\n    all four groups. Materials and methods, Animals, gives 14 Drd3-Cre and 11 Scnn1a-Tg3-Cre mice.\n  expected:\n  - quantity: Drd3-Cre NH mice\n    value: 7\n    tolerance: 0\n  - quantity: Drd3-Cre NH imaging fields\n    value: 11\n    tolerance: 0\n  - quantity: Drd3-Cre EN mice\n    value: 7\n    tolerance: 0\n  - quantity: Drd3-Cre EN imaging fields\n    value: 11\n    tolerance: 0\n  - quantity: Scnn1a-Tg3-Cre NH mice\n    value: 5\n    tolerance: 0\n  - quantity: Scnn1a-Tg3-Cre NH imaging fields\n    value: 6\n    tolerance: 0\n  - quantity: Scnn1a-Tg3-Cre EN mice\n    value: 6\n    tolerance: 0\n  - quantity: Scnn1a-Tg3-Cre EN imaging fields\n    value: 8\n    tolerance: 0\n  criterion: Counts are exact. A tolerance of zero is used because these are counts of animals and\n    fields, which are either present or not.\n- id: l23-cell-counts\n  statement: In L2/3 of Drd3-Cre mice, NH fields held 998 cells of which 475 were whisker-responsive,\n    and EN fields 1257 cells of which 874 were responsive.\n  source: Results, Enrichment sharpens the point representation of a single whisker in L2/3,\n    paragraph 2\n  quote: For L2/3 cells in normally-housed (NH) mice (11 imaging fields, seven mice, 998 total\n    cells, 475 responsive cells ... Enriched (EN) mice (11 imaging fields, seven mice, 1257 total\n    cells, 874 responsive cells\n  expected:\n  - quantity: NH L2/3 total cells\n    value: 998\n    tolerance: 99.8\n  - quantity: NH L2/3 responsive cells\n    value: 475\n    tolerance: 47.5\n  - quantity: EN L2/3 total cells\n    value: 1257\n    tolerance: 125.7\n  - quantity: EN L2/3 responsive cells\n    value: 874\n    tolerance: 87.4\n  criterion: Responsive as defined in the opening comment (Methods test; the pipeline's stored\n    p-values as a variant). Readings for which responsive ROIs are counted are (A) all of the\n    field and (B) only those over one of the nine barrels. Reproduced when all four counts are\n    within tolerance under one reading. The fraction responsive in EN higher than in NH is\n    reported either way.\n- id: l4-cell-counts\n  statement: In L4 of Scnn1a-Cre mice, NH fields held 322 cells of which 107 were responsive, and EN\n    fields 586 cells of which 181 were responsive.\n  source: Results, Enrichment sharpens the point representation of a single whisker in L2/3,\n    paragraph 3\n  quote: We imaged from 107 responsive cells in L4 of NH mice (six imaging fields, five mice, 322\n    total cells ... In EN mice, we imaged from 181 responsive cells in L4 (eight imaging fields, six\n    mice, 586 total cells\n  expected:\n  - quantity: NH L4 total cells\n    value: 322\n    tolerance: 32.2\n  - quantity: NH L4 responsive cells\n    value: 107\n    tolerance: 10.7\n  - quantity: EN L4 total cells\n    value: 586\n    tolerance: 58.6\n  - quantity: EN L4 responsive cells\n    value: 181\n    tolerance: 18.1\n  criterion: Responsive as in the opening comment. The Methods restrict L4 analysis to responsive\n    ROIs in columns C1, C2 and C3; readings are (A) responsive ROIs counted over the whole field\n    and (B) only those in C1, C2 or C3. Reproduced when all four counts are within tolerance under\n    one reading.\n- id: fig1f-gcamp-matches-spikes\n  statement: Whisker receptive fields measured from GCaMP6s dF/F were highly similar to those from\n    simultaneously recorded spikes in 9 of 10 L2/3 neurons.\n  source: Results, Whisker receptive fields measured by calcium imaging, paragraph 1; Figure 1F\n  quote: Receptive fields from spike counts were highly similar to those from ΔF/F in 9/10 cells\n  criterion: Spikes 0 to 100 ms after each deflection count as evoked (Methods, Cell-attached\n    recording); the imaging receptive field as in the opening comment. The paper does not say how\n    \"highly similar\" was judged. Readings are (a) the same best whisker from spikes and from dF/F;\n    (b) a Pearson correlation of the two nine-whisker receptive fields with p < 0.05. Reproduced\n    when 9 of 10 cells (8 to 10 accepted) meet one reading.\n- id: fig2a-l23-point-representation-stronger\n  statement: In L2/3, EN raised the mean response to a reference whisker in and just around its\n    column, at 0-75 um (NH 0.59, EN 0.77), 150-225 um (0.53, 0.60) and 225-300 um (0.41, 0.51)\n    from the column centre.\n  source: Results, Enrichment sharpens the point representation of a single whisker in L2/3,\n    paragraph 2; Figure 2A\n  quote: >-\n    This was observed in the central bin (0–75 μm from column center; NH: 0.59 ± 0.06, EN: 0.77 ±\n    0.04; p=0.0098, permutation test for difference in means) as well as at 150–225 µm (NH: 0.53 ±\n    0.02, EN: 0.60 ± 0.02; p=0.0028) and 225–300 µm (NH: 0.41 ± 0.02, EN: 0.51 ± 0.01; p=0.0001)\n  statistics:\n  - about: 0-75 um bin\n    test: permutation test for difference in means\n    p: 0.0098\n  - about: 150-225 um bin\n    test: permutation test for difference in means\n    p: 0.0028\n  - about: 225-300 um bin\n    test: permutation test for difference in means\n    p: 0.0001\n  expected:\n  - quantity: NH mean z-scored response, 0-75 um\n    value: 0.59\n    tolerance: 0.06\n  - quantity: EN mean z-scored response, 0-75 um\n    value: 0.77\n    tolerance: 0.04\n  - quantity: NH mean z-scored response, 150-225 um\n    value: 0.53\n    tolerance: 0.02\n  - quantity: EN mean z-scored response, 150-225 um\n    value: 0.60\n    tolerance: 0.02\n  - quantity: NH mean z-scored response, 225-300 um\n    value: 0.41\n    tolerance: 0.02\n  - quantity: EN mean z-scored response, 225-300 um\n    value: 0.51\n    tolerance: 0.01\n  criterion: Per responsive L2/3 ROI and reference whisker, the median evoked dF/F z-scored to blank\n    trials (Methods; Figure 2A legend), binned by distance to the reference column centre in 75 um\n    bins (Figure 2A legend), averaged over ROI-whisker pairs. EN against NH per bin by the\n    permutation test of the difference in means (permutationTest.m). ROI readings (A) and (B) of\n    the opening comment; z-score centred on the blank mean, the blank median as a variant.\n    Reproduced when, under one reading, EN is higher in all three bins with p < 0.05 each and the\n    six values are within tolerance; partially reproduced when the three tests hold but some\n    values fall outside tolerance.\n- id: fig2a-l23-flanks-suppressed\n  statement: In L2/3, EN lowered mean responses to the reference whisker at the flanks of the point\n    representation, 375 to 750 um from the column centre.\n  source: Results, Enrichment sharpens the point representation of a single whisker in L2/3,\n    paragraph 2; Figure 2A\n  quote: But EN suppressed mean responses at the flanks of the point representation (375–750 μm,\n    p<0.05 for all bins\n  statistics:\n  - test: permutation test for difference in means\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - fig2a-l23-point-representation-stronger\n  criterion: As fig2a-l23-point-representation-stronger, for the five 75 um bins from 375 to 750\n    um. Reproduced when, under one reading, EN is lower with p < 0.05 in all five bins; partially\n    reproduced for three or four bins.\n- id: fig2b-2d-point-representation\n  statement: Two-dimensional maps of the L2/3 point representation, with fields rotated to align the\n    arc axis, show the same EN enhancement in the home column and reduction some distance away.\n  source: Results, Enrichment sharpens the point representation of a single whisker in L2/3,\n    paragraph 2; Figure 2B\n  quote: This enhancement of responses in the home column and reduced responses some distance away\n    was also apparent in 2D maps\n  depends_on:\n  - fig2a-l23-point-representation-stronger\n  criterion: Responsive ROIs within 750 um of each reference column, coordinates centred on the\n    column and rotated so the within-row axis is horizontal (Figure 2B legend; Methods, Normalized\n    anatomical reference frame), binned by k-means into bins of similar ROI count (Methods; the\n    number of bins is not given, a plotting choice, 30 used). Reproduced when the EN minus NH mean\n    response is positive over ROIs inside the average barrel radius of the centre and negative over\n    ROIs beyond 375 um, on the same ROI-whisker pairs as Figure 2A.\n- id: fig2c-l4-point-representation-weaker\n  statement: In L4, EN reduced mean whisker-evoked responses in most bins within 375 um of the\n    reference column centre, including 0-75 um (NH 1.11, EN 0.86).\n  source: Results, Enrichment sharpens the point representation of a single whisker in L2/3,\n    paragraph 3; Figure 2C\n  quote: >-\n    We found that EN reduced mean whisker-evoked responses for cells in most bins <375 μm from the\n    reference whisker’s column center (p<0.05 for each bin), including at 0–75 μm (NH: 1.11 ±\n    0.13, EN: 0.86 ± 0.06, p=0.034)\n  statistics:\n  - about: 0-75 um bin\n    test: permutation test for difference in means\n    p: 0.034\n  - about: each bin below 375 um where EN is lower\n    test: permutation test for difference in means\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: NH L4 mean z-scored response, 0-75 um\n    value: 1.11\n    tolerance: 0.13\n  - quantity: EN L4 mean z-scored response, 0-75 um\n    value: 0.86\n    tolerance: 0.06\n  criterion: As fig2a-l23-point-representation-stronger, for L4 ROIs (responsive, in columns C1, C2\n    or C3, per the Methods; all responsive L4 ROIs as a variant). \"Most bins\" read as at least three\n    of the five 75 um bins below 375 um. Reproduced when EN is lower with p < 0.05 in at least three\n    of them, the 0-75 um bin among them, and both 0-75 um values are within tolerance.\n- id: fig2c-l4-sharper-than-l23\n  statement: In NH mice the point representation was sharper in L4 than in L2/3.\n  source: Results, Enrichment sharpens the point representation of a single whisker in L2/3,\n    paragraph 3; Figure 2C\n  quote: We found that the point representation was sharper in L4 than L2/3\n  depends_on:\n  - fig2a-l23-point-representation-stronger\n  - fig2c-l4-point-representation-weaker\n  criterion: The paper gives no measure of sharpness. OPEN; readings are (a) the mean response at\n    225-300 um as a fraction of that at 0-75 um, and (b) the distance at which the binned mean\n    first falls below half the 0-75 um value, each computed on NH profiles of Figure 2A and 2C.\n    Reproduced when both readings are smaller in L4 than in L2/3. No test is reported.\n- id: figs2-1-column-frame\n  statement: In a column-based reference frame, EN raised the mean L2/3 response to a reference\n    whisker in its home column and sharpened the point representation mainly across rows; in L4\n    EN weakened home-column responses.\n  source: Results, Enrichment sharpens the point representation of a single whisker in L2/3,\n    paragraph 4; Figure 2 figure supplement 1\n  quote: In L2/3, this confirmed that EN increased the mean response to a reference whisker in its\n    home column, and revealed that EN sharpened the point representation primarily across whisker\n    rows, not across arcs ... In L4, this confirmed that EN weakened home-column responses\n  criterion: Positions in units of the reference column radius along the ROI's direction (Figure 2\n    S1 legend; ROI_pos_barrel_norm), ROIs within 5 radii. Home column is distance < 1. Home-column\n    test, EN against NH by the permutation test of the difference in means. Across-row sharpening\n    has no measure in the paper; it is read as the EN minus NH difference in mean response for ROIs\n    at 1 to 2 radii lying within 45 degrees of the arc axis (across rows) being more negative than\n    for those within 45 degrees of the row axis (across arcs). Reproduced when the L2/3 home-column\n    response is higher in EN (p < 0.05), the L4 home-column response lower in EN (p < 0.05), and\n    the across-row reading holds; partially reproduced when the two home-column tests hold alone.\n- id: figs2-2-barrel-size-unchanged\n  statement: Enrichment did not change the radius of L4 barrels, in Drd3-Cre mice (NH 151 um, EN 145\n    um) or in Scnn1a-Cre mice (NH 118 um, EN 124 um).\n  source: Results, Enrichment sharpens the point representation of a single whisker in L2/3,\n    paragraph 5; Figure 2 figure supplement 2\n  quote: Enrichment did not alter mean barrel radius (NH ... 151 ± 7.2 μm, n = 6 mice, EN ... 145 ±\n    4.6 μm [mean ± SEM], n = 7 mice (2-way ANOVA, factors ... enrichment and barrel identity, p=0.7\n    for enrichment factor) ... There was also no change in barrel radius in Scnn1a-Cre mice, which\n    have a slightly smaller barrels (NH ... 118 ± 6.6 μm, n = 5 mice, EN ... 124 ± 6.9 μm, n = 6\n    mice, p=0.01 for enrichment factor\n  statistics:\n  - about: Drd3-Cre, enrichment factor\n    test: 2-way ANOVA, factors enrichment and barrel identity\n    p: 0.7\n    n: 6 NH and 7 EN mice\n  - about: Scnn1a-Cre, enrichment factor (printed so, while the text and legend call it not\n      significant)\n    test: 2-way ANOVA, factors enrichment and barrel identity\n    p: 0.01\n    n: 5 NH and 6 EN mice\n  expected:\n  - quantity: Drd3-Cre NH mean barrel radius\n    value: 151\n    tolerance: 7.2\n    unit: um\n  - quantity: Drd3-Cre EN mean barrel radius\n    value: 145\n    tolerance: 4.6\n    unit: um\n  - quantity: Scnn1a-Cre NH mean barrel radius\n    value: 118\n    tolerance: 6.6\n    unit: um\n  - quantity: Scnn1a-Cre EN mean barrel radius\n    value: 124\n    tolerance: 6.9\n    unit: um\n  criterion: Radius from each barrel's area assuming a circle, nine barrels per mouse, the mouse mean\n    over them (Methods, Quantification of L4 barrel size). A claim of absence judged on the paper's\n    test, a two-way ANOVA with factors enrichment and barrel identity on per-barrel radii, for each\n    genotype. Reproduced when the enrichment factor has p >= 0.05 in both genotypes and the means\n    are within tolerance. The printed p = 0.01 for Scnn1a-Cre conflicts with the sentence and with\n    the legend (\"no significant enrichment effect for either genotype\"); the legend's reading is\n    used. Radii derived from the data set's normalised positions measure the radius along each\n    ROI's direction, not from area, and if used are a stated approximation.\n- id: figs3-1-l23-salt-and-pepper\n  statement: In L2/3 of NH mice, tuning is intermixed within columns; 53% of responsive cells within\n    75 um of a column centre had the CW as best whisker, falling to 16% at 225-300 um and 1% at\n    525-600 um, and by equivalent best whiskers 67%, 43% and 10%.\n  source: Results, Whisker map topography in L2/3 and L4 in normally housed mice, paragraph 2;\n    Figure 3 figure supplement 1B and 1D\n  quote: 53% (31/58) of responsive cells within 0–75 µm of a column center had a BW that matched the\n    column’s anatomically-mapped whisker ... to 16% (66/406 cells) at 225–300 µm and 1% (6/419\n    cells) at 525–600 µm ... By this measure, 67% (39/58) of L2/3 PYR cells within 0–75 µm of the\n    column center were tuned to the CW. This fraction fell off gradually with cortical distance, to\n    43% at 225–300 µm (174/406 cells) and 10% at 525–600 µm (41/419 cells\n  expected:\n  - quantity: NH L2/3 fraction BW equals reference whisker, 0-75 um\n    value: 53\n    tolerance: 5.3\n    unit: percent\n  - quantity: NH L2/3 fraction BW equals reference whisker, 225-300 um\n    value: 16\n    tolerance: 1.6\n    unit: percent\n  - quantity: NH L2/3 fraction BW equals reference whisker, 525-600 um\n    value: 1\n    tolerance: 0.1\n    unit: percent\n  - quantity: NH L2/3 fraction eBW includes reference whisker, 0-75 um\n    value: 67\n    tolerance: 6.7\n    unit: percent\n  - quantity: NH L2/3 fraction eBW includes reference whisker, 225-300 um\n    value: 43\n    tolerance: 4.3\n    unit: percent\n  - quantity: NH L2/3 fraction eBW includes reference whisker, 525-600 um\n    value: 10\n    tolerance: 1\n    unit: percent\n  - quantity: NH L2/3 ROI count, 0-75 um bin\n    value: 58\n    tolerance: 5.8\n  - quantity: NH L2/3 ROI-whisker count, 225-300 um bin\n    value: 406\n    tolerance: 40.6\n  criterion: Responsive NH L2/3 ROIs; each ROI enters each reference whisker's 75 um distance bins\n    (opening comment); fraction of entries whose BW (or eBW set) contains the reference whisker.\n    BW by mean, median as a variant; eBW readings E1, E2, E3; ROI readings (A), (B). The 1% value\n    is 6 of 419 cells; a count of 2 to 10 of about 419 is accepted, as 10% of 1% is below one\n    cell. Reproduced when the BW values and the bin counts are within tolerance under one reading\n    and the eBW values under one eBW reading; partially reproduced when only the BW values hold.\n    Fractions falling with distance is required in either case.\n- id: discussion-l23-nh-in-column-tuning\n  statement: In NH L2/3, about 48% of cells located in a column responded maximally to the CW and\n    65% had the CW among their equivalent best whiskers.\n  source: Discussion, Whisker map structure in L2/3 and L4 of normally housed mice, paragraph 1;\n    Results, Enrichment decreases tuning heterogeneity in the salt-and-pepper map, paragraph 1\n  quote: only 48% of PYR cells in each column responded maximally to the CW, and only 65% had the CW\n    among statistically equal best whiskers\n  expected:\n  - quantity: NH L2/3 in-column fraction with BW equal to CW\n    value: 48\n    tolerance: 4.8\n    unit: percent\n  - quantity: NH L2/3 in-column fraction with CW among eBWs\n    value: 65\n    tolerance: 6.5\n    unit: percent\n  criterion: Responsive NH L2/3 ROIs over one of the nine barrels, each against its own CW, pooled\n    over fields. The 65% matches 224 of 344 (65.1%) in the Results. The 48% is not given elsewhere;\n    readings are (a) the pooled fraction and (b) the mean over columns of the per-column fraction\n    (\"in each column\"). Reproduced when both values are within tolerance under one BW, eBW and\n    pooling reading.\n- id: figs3-1-l4-nh-tuning\n  statement: In NH L4, 63% (30/48) of cells within 75 um of a column centre had the CW as BW and 73%\n    (35/48) had it among eBWs, not different from L2/3; but the fraction tuned to a whisker fell off\n    more sharply with distance in L4, significantly at 150-375 um.\n  source: Results, Whisker map topography in L2/3 and L4 in normally housed mice, paragraph 3;\n    Figure 3 figure supplement 1B and 1D\n  quote: 63% of L4 excitatory cells (30/48) had a BW that matched the CW, and 73% (35/48) had the CW\n    among the eBWs. These values are not different from L2/3 (p=0.43 and p=0.67 respectively,\n    Fisher’s Exact Test). However, the fraction of cells tuned to a given whisker fell off ~30% more\n    sharply with distance in L4 than in L2/3, using either tuning measure. This difference was\n    significant at distance bins from 150 to 375 µm from the column center (p<0.05, Fisher’s Exact\n    Test\n  statistics:\n  - about: BW fraction at 0-75 um, L4 against L2/3\n    test: Fisher's exact test\n    p: 0.43\n  - about: eBW fraction at 0-75 um, L4 against L2/3\n    test: Fisher's exact test\n    p: 0.67\n  - about: fraction tuned, L4 against L2/3, bins from 150 to 375 um\n    test: Fisher's exact test\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: NH L4 fraction BW equals CW, 0-75 um\n    value: 63\n    tolerance: 6.3\n    unit: percent\n  - quantity: NH L4 fraction CW among eBWs, 0-75 um\n    value: 73\n    tolerance: 7.3\n    unit: percent\n  depends_on:\n  - figs3-1-l23-salt-and-pepper\n  criterion: As figs3-1-l23-salt-and-pepper for NH L4 ROIs (C1 to C3 per the Methods, all responsive\n    L4 ROIs as a variant). The 0-75 um equality is a claim of absence judged by Fisher's exact test\n    at 0.05, L4 against L2/3, for both measures. Reproduced when both 0-75 um values are within\n    tolerance, neither 0-75 um test is significant, and L4 is lower than L2/3 with p < 0.05\n    (Fisher) in at least two of the three bins 150-225, 225-300 and 300-375 um for one tuning\n    measure; partially reproduced when the values and absence hold but not the fall-off.\n- id: fig3a-l23-enrichment-more-cw-tuned\n  statement: In L2/3, EN raised the fraction of cells tuned to the CW at column centres (82%, 111/135,\n    against 67% in NH) and in every bin below 300 um, not beyond; over all cells within column\n    boundaries 77.1% (468/607) against 65.1% (224/344).\n  source: Results, Enrichment decreases tuning heterogeneity in the salt-and-pepper map, paragraph 1;\n    Figure 3A\n  quote: In EN mice, 82% (111/135) of cells located 0–75 μm from a column center were tuned to the\n    CW, which is greater than NH mice (67%, p=0.025, Fisher’s Exact Test). This was true for all\n    bins < 300 μm from the column center, but not further away ... 77.1% (468/607) of\n    whisker-responsive cells in EN mice were tuned to the CW, compared to 65.1% (224/344) in NH\n    (p=0.00008\n  statistics:\n  - about: 0-75 um bin\n    test: Fisher's exact test\n    p: 0.025\n  - about: all cells within column boundaries\n    test: Fisher's exact test\n    p: 0.00008\n  expected:\n  - quantity: EN L2/3 fraction CW among eBWs, 0-75 um\n    value: 82\n    tolerance: 8.2\n    unit: percent\n  - quantity: NH L2/3 fraction CW among eBWs, 0-75 um\n    value: 67\n    tolerance: 6.7\n    unit: percent\n  - quantity: EN L2/3 fraction CW among eBWs, within columns\n    value: 77.1\n    tolerance: 7.71\n    unit: percent\n  - quantity: NH L2/3 fraction CW among eBWs, within columns\n    value: 65.1\n    tolerance: 6.51\n    unit: percent\n  - quantity: EN L2/3 cells within columns\n    value: 607\n    tolerance: 60.7\n  - quantity: NH L2/3 cells within columns\n    value: 344\n    tolerance: 34.4\n  depends_on:\n  - figs3-1-l23-salt-and-pepper\n  criterion: Tuned means the reference whisker is among the eBWs (Figure 3A legend), eBW readings E1,\n    E2, E3. Per 75 um bin, EN against NH by Fisher's exact test (legend); the code's permutation\n    test on 0/1 indicators is a variant. Within columns, responsive ROIs over one of the nine\n    barrels against their CW. Reproduced when, under one eBW reading, the values are within\n    tolerance, EN is higher with p < 0.05 at 0-75 um and within columns, and EN is higher with p\n    < 0.05 in every bin below 300 um and in no bin from 300 um on; partially reproduced when the\n    0-75 um and within-column tests hold but the bin pattern does not.\n- id: fig3c-l4-enrichment-more-cw-tuned\n  statement: In L4, EN also raised the fraction of CW-tuned cells, at column centres (90%, 57/63,\n    against 73%) and over all cells within columns (89.3%, 133/149, against 75.6%, 65/86).\n  source: Results, Enrichment decreases tuning heterogeneity in the salt-and-pepper map, paragraph 2;\n    Figure 3C\n  quote: In EN mice, 90% (57/63) of cells at column centers (0–75 μm) were tuned to the CW, which is\n    greater than the 73% in NH mice (p=0.021) ... In EN mice, 89.3% (133/149) of all cells within a\n    column boundary were CW-tuned, compared to 75.6% (65/86) in NH mice (p=0.0086\n  statistics:\n  - about: 0-75 um bin\n    test: Fisher's exact test\n    p: 0.021\n  - about: all cells within column boundaries\n    test: Fisher's exact test\n    p: 0.0086\n  expected:\n  - quantity: EN L4 fraction CW among eBWs, 0-75 um\n    value: 90\n    tolerance: 9\n    unit: percent\n  - quantity: NH L4 fraction CW among eBWs, 0-75 um\n    value: 73\n    tolerance: 7.3\n    unit: percent\n  - quantity: EN L4 fraction CW among eBWs, within columns\n    value: 89.3\n    tolerance: 8.93\n    unit: percent\n  - quantity: NH L4 fraction CW among eBWs, within columns\n    value: 75.6\n    tolerance: 7.56\n    unit: percent\n  depends_on:\n  - fig3a-l23-enrichment-more-cw-tuned\n  criterion: As fig3a-l23-enrichment-more-cw-tuned for L4 ROIs. The test is not named in this\n    paragraph; Fisher's exact test is read from the Figure 3 legend (\"C-D, As in A and B\").\n    Reproduced when the four values are within tolerance and both tests give p < 0.05 with EN\n    higher, under one eBW reading.\n- id: fig4a-l23-ranked-rf-sharper\n  statement: In L2/3, EN increased responses to the strongest three whiskers and decreased responses\n    to the weakest three in rank-ordered receptive fields normalised to spontaneous activity, so\n    receptive fields were sharper.\n  source: Results, Enrichment sharpens whisker receptive fields, paragraph 1; Figure 4A\n  quote: In L2/3, EN increased responses to the strongest three whiskers, and decreased responses to\n    the weakest three whiskers, relative to NH cells\n  statistics:\n  - test: permutation test, per whisker rank\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Per responsive L2/3 ROI, the nine z-scored median responses (opening comment) sorted\n    from strongest to weakest, averaged over ROIs; EN against NH per rank by the permutation test of\n    the difference in means (Figure 4A legend; permutationTest.m). ROI readings (A), (B).\n    Reproduced when EN is higher with p < 0.05 at ranks 1 to 3 and lower with p < 0.05 at ranks 7\n    to 9; partially reproduced when the direction holds at all six ranks but some tests do not.\n- id: fig4b-l23-cw-and-best-sw-stronger\n  statement: In L2/3, EN increased the signal-to-noise of the CW response and of the two best\n    surround whisker responses.\n  source: Results, Enrichment sharpens whisker receptive fields, paragraph 1; Figure 4B\n  quote: EN specifically increased the signal-to-noise of both CW response and the best 2 SW\n    responses\n  statistics:\n  - test: permutation test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Responsive L2/3 ROIs over a barrel, z-scored median responses to the CW and to the\n    surround whiskers ranked by strength (Figure 4B legend). EN against NH by the permutation test\n    of the difference in means. Reproduced when EN is higher with p < 0.05 for the CW and for SW\n    ranks 1 and 2.\n- id: fig4c-spontaneous-activity\n  statement: EN decreased spontaneous (blank trial) activity in L2/3, while L4 spontaneous activity\n    was unaffected.\n  source: Results, Enrichment sharpens whisker receptive fields, paragraphs 1 and 4; Figure 4C\n  quote: In addition to these changes in tuning shape, EN also decreased spontaneous (blank trial)\n    activity relative to NH ... spontaneous activity was unaffected\n  statistics:\n  - test: permutation test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Spontaneous activity of an ROI is the median dF/F during blank trials (Figure 4C\n    legend), read as the median over blank trials of the evoked-window response (baseline\n    subtracted, as for whisker trials); the median raw evoked-window dF/F without baseline\n    subtraction is a variant. EN against NH by the permutation test of the difference in means\n    (legend), responsive ROIs. Reproduced when L2/3 EN is lower with p < 0.05 and L4 shows no\n    difference at p < 0.05 (absence judged on the same test).\n- id: figs4-1-absolute-dff\n  statement: Without normalisation to spontaneous activity, L2/3 cells in EN had greater mean evoked\n    dF/F than NH, and the regression of weakest-four on strongest-four whisker responses had a\n    different slope in EN, showing sharper tuning.\n  source: Figure 4 figure supplement 1; Results, Enrichment sharpens whisker receptive fields,\n    paragraph 1\n  quote: ** denotes greater mean response for EN than NH (p=0.0002, permutation test) ... Regression\n    slope was different between NH and EN (p=1.2e-9, t-test for difference in slopes\n  statistics:\n  - about: mean response, EN against NH\n    test: permutation test\n    p: 0.0002\n  - about: regression slope, EN against NH\n    test: t-test for difference in slopes\n    p: 1.2e-9\n  criterion: Per responsive L2/3 ROI, the mean dF/F evoked by its four strongest and by its four\n    weakest whiskers; a linear regression of weakest on strongest in each group, slopes compared by\n    a t-test on the interaction term. Which response the p = 0.0002 compares is open; readings are\n    (a) the mean over the four strongest whiskers (the figure script make_responseDistPlots.m\n    tests bestSWs and worstSWs), (b) the mean over all nine whiskers. Reproduced when, under one\n    reading, EN is higher with p < 0.05, and the EN slope is lower than the NH slope with p < 0.05.\n- id: figs4-2-barrel-vs-septal\n  statement: Sharpening of L2/3 tuning by EN was more prominent for ROIs over L4 barrels than for ROIs\n    over septa.\n  source: Results, Enrichment sharpens whisker receptive fields, paragraph 1; Figure 4 figure\n    supplement 2A and 2B\n  quote: Sharpening of tuning was more prominent for L2/3 cells located over L4 barrels than for\n    those located over septa\n  depends_on:\n  - fig4a-l23-ranked-rf-sharper\n  criterion: Ranked receptive fields as in fig4a-l23-ranked-rf-sharper, separately for ROIs over a\n    barrel and over septa. The paper gives no measure. Read as more ranks with a significant EN\n    against NH difference (p < 0.05, permutation test) in the barrel group than in the septal\n    group; reproduced when that holds. The septal group is smaller, which alone lowers its count;\n    the absolute EN minus NH differences at ranks 1-3 and 7-9 are reported as well.\n- id: fig4d-l23-cw-stronger\n  statement: In L2/3, CW responses were higher in EN than NH (0.71 against 0.64).\n  source: Results, Enrichment sharpens whisker receptive fields, paragraph 3; Figure 4D\n  quote: >-\n    CW responses were higher in EN than NH (NH: 0.64 ± 0.03, EN: 0.71 ± 0.02; p=0.01, permutation\n    test for difference in means)\n  statistics:\n  - test: permutation test for difference in means\n    p: 0.01\n  expected:\n  - quantity: NH L2/3 mean CW response\n    value: 0.64\n    tolerance: 0.03\n  - quantity: EN L2/3 mean CW response\n    value: 0.71\n    tolerance: 0.02\n  criterion: Responsive L2/3 ROIs over a barrel, the z-scored median response to the CW, averaged\n    over ROIs; columns with at least 3 ROIs (Figure 4 legend, stated for E; applying it to D as\n    well is a reading, all columns the other). EN against NH by the permutation test of the\n    difference in means. Reproduced when both values are within tolerance and p < 0.05 with EN\n    higher, under one reading.\n- id: fig4d-l23-across-row-sharpening\n  statement: In L2/3, EN reduced responses to the surround whiskers one row dorsal and one row ventral\n    to the CW (from 68% and 62% of the CW response in NH to 49% and 41% in EN), sharpening receptive\n    fields across rows.\n  source: Results, Enrichment sharpens whisker receptive fields, paragraph 3; Figure 4D\n  quote: >-\n    In NH, the SW one row dorsal to the CW (within-arc, −1 row) and one row ventral to the CW\n    (within-arc, +one row) were 68% and 62% of the CW response, respectively. EN reduced responses\n    to both these SWs (within-arc, −1 row: NH: 0.44 ± 0.02, EN 0.35 ± 0.02, p=0.001; within-arc,\n    +one row: NH: 0.39 ± 0.02, EN: 0.29 ± 0.01, p=0.0001). As a result, these whiskers evoked only\n    49% and 41% of the CW response\n  statistics:\n  - about: within-arc, -1 row\n    test: permutation test for difference in means\n    p: 0.001\n  - about: within-arc, +1 row\n    test: permutation test for difference in means\n    p: 0.0001\n  expected:\n  - quantity: NH response, within-arc -1 row\n    value: 0.44\n    tolerance: 0.02\n  - quantity: EN response, within-arc -1 row\n    value: 0.35\n    tolerance: 0.02\n  - quantity: NH response, within-arc +1 row\n    value: 0.39\n    tolerance: 0.02\n  - quantity: EN response, within-arc +1 row\n    value: 0.29\n    tolerance: 0.01\n  - quantity: NH -1 row response as fraction of CW\n    value: 68\n    tolerance: 6.8\n    unit: percent\n  - quantity: NH +1 row response as fraction of CW\n    value: 62\n    tolerance: 6.2\n    unit: percent\n  - quantity: EN -1 row response as fraction of CW\n    value: 49\n    tolerance: 4.9\n    unit: percent\n  - quantity: EN +1 row response as fraction of CW\n    value: 41\n    tolerance: 4.1\n    unit: percent\n  depends_on:\n  - fig4d-l23-cw-stronger\n  criterion: As fig4d-l23-cw-stronger, for the whisker in the same arc one row dorsal (-1) or ventral\n    (+1) of the CW, for ROIs whose CW has that neighbour among the nine. Fractions are the group\n    mean SW response over the group mean CW response (the printed values match this, e.g. 0.44 /\n    0.64 = 69%). Reproduced when both tests give p < 0.05 with EN lower and the four response\n    values are within tolerance; partially reproduced when the tests hold but values fall outside.\n- id: fig4d-l23-within-row-broadening\n  statement: In the within-row dimension, EN increased L2/3 responses to the surround whisker one arc\n    rostral of the CW (0.34 to 0.53) and did not alter responses to the one arc caudal (0.57 and\n    0.55), broadening receptive fields along rows.\n  source: Results, Enrichment sharpens whisker receptive fields, paragraph 3; Figure 4D\n  quote: >-\n    In the within-row dimension, EN increased responses to the SW one arc rostral of the CW\n    (within-row, +one arc: NH: 0.34 ± 0.01, EN: 0.53 ± 0.02, p=0.0001), and did not alter responses\n    to the SW one arc caudal of the CW (within-row, −1 arc: NH: 0.57 ± 0.04, EN 0.55 ± 0.04,\n    p=0.40)\n  statistics:\n  - about: within-row, +1 arc\n    test: permutation test for difference in means\n    p: 0.0001\n  - about: within-row, -1 arc\n    test: permutation test for difference in means\n    p: 0.4\n  expected:\n  - quantity: NH response, within-row +1 arc\n    value: 0.34\n    tolerance: 0.01\n  - quantity: EN response, within-row +1 arc\n    value: 0.53\n    tolerance: 0.02\n  - quantity: NH response, within-row -1 arc\n    value: 0.57\n    tolerance: 0.04\n  - quantity: EN response, within-row -1 arc\n    value: 0.55\n    tolerance: 0.04\n  depends_on:\n  - fig4d-l23-cw-stronger\n  criterion: As fig4d-l23-cw-stronger, for the whisker in the same row one arc rostral (+1, higher arc\n    number) or caudal (-1). The -1 arc part is a claim of absence judged on the same permutation\n    test at 0.05. Reproduced when +1 arc is higher in EN with p < 0.05, -1 arc shows no difference\n    at p < 0.05, and the four values are within tolerance.\n- id: fig4ae-l4-weaker-responses\n  statement: In L4, EN reduced responses to most whiskers in ranked receptive fields and, in\n    somatotopic space, to the CW (0.98 to 0.81) and to the +1 arc (0.54 to 0.17), -1 arc (0.67 to\n    0.33) and +1 row (0.23 to 0.11) surround whiskers, sharpening receptive fields by global\n    weakening.\n  source: Results, Enrichment sharpens whisker receptive fields, paragraph 4; Figure 4A, 4B and 4E\n  quote: >-\n    In L4, EN reduced responses to most whiskers in rank-ordered receptive fields ... CW responses\n    were weaker in EN than NH (NH: 0.98 ± 0.09, EN: 0.81 ± 0.04, p=0.02), as were responses to the\n    within-row, +one arc SW (NH: 0.54 ± 0.08, EN: 0.17 ± 0.02, p=0.0001), the within-row, −1 arc SW\n    (NH: 0.67 ± 0.13, EN 0.33 ± 0.04, p=0.003), and the within-arc, +one row SW (NH: 0.23 ± 0.03,\n    EN 0.11 ± 0.02, p=0.0007)\n  statistics:\n  - about: CW\n    test: permutation test for difference in means\n    p: 0.02\n  - about: within-row, +1 arc\n    test: permutation test for difference in means\n    p: 0.0001\n  - about: within-row, -1 arc\n    test: permutation test for difference in means\n    p: 0.003\n  - about: within-arc, +1 row\n    test: permutation test for difference in means\n    p: 0.0007\n  expected:\n  - quantity: NH L4 CW response\n    value: 0.98\n    tolerance: 0.09\n  - quantity: EN L4 CW response\n    value: 0.81\n    tolerance: 0.04\n  - quantity: NH L4 +1 arc response\n    value: 0.54\n    tolerance: 0.08\n  - quantity: EN L4 +1 arc response\n    value: 0.17\n    tolerance: 0.02\n  - quantity: NH L4 -1 arc response\n    value: 0.67\n    tolerance: 0.13\n  - quantity: EN L4 -1 arc response\n    value: 0.33\n    tolerance: 0.04\n  - quantity: NH L4 +1 row response\n    value: 0.23\n    tolerance: 0.03\n  - quantity: EN L4 +1 row response\n    value: 0.11\n    tolerance: 0.02\n  depends_on:\n  - fig4d-l23-cw-stronger\n  criterion: As fig4d-l23-cw-stronger for L4 ROIs in C1 to C3, columns with at least 3 ROIs (Figure 4E\n    legend). Ranked receptive fields as in fig4a-l23-ranked-rf-sharper; \"most whiskers\" read as at\n    least five of nine ranks lower in EN with p < 0.05. Reproduced when the four somatotopic tests\n    give p < 0.05 with EN lower, the eight values are within tolerance, and the ranked reading\n    holds; partially reproduced when the four tests hold alone.\n- id: fig5a-l23-signal-correlation-boundary\n  statement: In L2/3, EN modestly raised signal correlation for within-column pairs (0.637 to 0.659)\n    and greatly reduced it for across-column pairs (0.541 to 0.425); in EN, closely spaced pairs\n    (under 150 um) had much lower signal correlation across than within columns (0.529 against\n    0.674), where in NH the difference was modest (0.611 against 0.652).\n  source: Results, Enrichment strengthens functional column boundaries in L2/3, paragraph 1; Figure\n    5A and 5C\n  quote: >-\n    For closely spaced pairs (<150 μm apart) signal correlation was only modestly higher for\n    within-column pairs than across-column pairs (0.652 ± 0.005 vs. 0.611 ± 0.007, p<0.0001,\n    permutation test of difference in means) ... In EN mice, mean signal correlation for\n    within-column pairs was modestly increased (NH: 0.637 ± 0.004, EN: 0.659 ± 0.002; includes\n    pairs at all distances; p<0.0001, permutation test), while signal correlation for across-column\n    pairs was greatly reduced (NH: 0.541 ± 0.004, EN: 0.425 ± 0.004; p<0.0001) ... signal\n    correlation for closely spaced cross-column pairs (<150 μm apart) was much lower than for\n    similarly spaced within-column pairs (0.674 ± 0.003 vs. 0.529 ± 0.006, p<0.0001\n  statistics:\n  - about: NH pairs under 150 um, within against across columns\n    test: permutation test of difference in means\n    p: 0.0001\n    p_relation: \"<\"\n  - about: within-column pairs, EN against NH\n    test: permutation test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: across-column pairs, EN against NH\n    test: permutation test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: EN pairs under 150 um, within against across columns\n    test: permutation test\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: NH within-column signal correlation, pairs under 150 um\n    value: 0.652\n    tolerance: 0.005\n  - quantity: NH across-column signal correlation, pairs under 150 um\n    value: 0.611\n    tolerance: 0.007\n  - quantity: NH within-column signal correlation, all pairs\n    value: 0.637\n    tolerance: 0.004\n  - quantity: EN within-column signal correlation, all pairs\n    value: 0.659\n    tolerance: 0.002\n  - quantity: NH across-column signal correlation, all pairs\n    value: 0.541\n    tolerance: 0.004\n  - quantity: EN across-column signal correlation, all pairs\n    value: 0.425\n    tolerance: 0.004\n  - quantity: EN within-column signal correlation, pairs under 150 um\n    value: 0.674\n    tolerance: 0.003\n  - quantity: EN across-column signal correlation, pairs under 150 um\n    value: 0.529\n    tolerance: 0.006\n  criterion: All pairs of simultaneously imaged responsive L2/3 ROIs that both lie over a barrel\n    (septal ROIs left out); within-column when over the same barrel, across-column otherwise\n    (Methods, Signal and noise correlation analysis). Signal correlation is the Pearson\n    correlation of the two ROIs' nine-element vectors of mean evoked response per whisker, each\n    z-scored. Distance is Euclidean in um between ROI positions (from the positions relative to a\n    common barrel). Tests are permutation tests of the difference in means with pairs as units.\n    Reproduced when all four tests give p < 0.05 in the stated direction and at least six of the\n    eight values are within tolerance; partially reproduced when the four tests hold with fewer\n    values within tolerance.\n- id: fig5b-l23-noise-correlation-boundary\n  statement: In L2/3 of NH mice, noise correlations were similar within (0.334) and across (0.327)\n    columns; EN modestly reduced them within columns (0.307) and greatly reduced them across columns\n    (0.255), even for pairs about 100 um apart.\n  source: Results, Enrichment strengthens functional column boundaries in L2/3, paragraph 2; Figure\n    5B and 5D\n  quote: In NH mice, noise correlations for L2/3 neuron pairs decreased with distance, and were\n    similar within columns (0.334 ± 0.002) and across columns (0.327 ± 0.002). EN modestly reduced\n    noise correlations for within-column pairs (to 0.307 ± 0.001; p<0.0001, permutation test vs.\n    NH), but greatly reduced noise correlations for cross-column pairs (to 0.255 ± 0.001; p<0.0001,\n    permutation test vs. NH\n  statistics:\n  - about: within-column pairs, EN against NH\n    test: permutation test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: across-column pairs, EN against NH\n    test: permutation test\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: NH within-column noise correlation\n    value: 0.334\n    tolerance: 0.002\n  - quantity: NH across-column noise correlation\n    value: 0.327\n    tolerance: 0.002\n  - quantity: EN within-column noise correlation\n    value: 0.307\n    tolerance: 0.001\n  - quantity: EN across-column noise correlation\n    value: 0.255\n    tolerance: 0.001\n  depends_on:\n  - fig5a-l23-signal-correlation-boundary\n  criterion: Pairs as in fig5a-l23-signal-correlation-boundary. Noise correlation per pair is the\n    mean over the nine whiskers of the Pearson correlation of the two ROIs' per-trial evoked\n    responses to that whisker, each whisker's vector z-scored (Methods). EN against NH by the\n    permutation test of the difference in means. Reproduced when both tests give p < 0.05 with EN\n    lower, the EN reduction across columns is larger than within, and at least three of the four\n    values are within tolerance. The NH within against across difference is reported; the paper\n    reports no test of it.\n- id: fig5eh-l23-correlation-gradient-at-edge\n  statement: EN substantially reduced the signal and noise correlations of neurons outside a\n    reference column to neurons inside it, while preserving signal correlation and modestly\n    reducing noise correlation within the column, giving a steeper gradient at the column edge.\n  source: Results, Enrichment strengthens functional column boundaries in L2/3, paragraph 3; Figure\n    5E to 5H\n  quote: EN substantially reduced these signal and noise correlations for neurons outside the\n    column, while preserving signal correlation and only modestly reducing noise correlation among\n    neurons within the reference column ( Figure 5E–F ). This generated a stronger gradient of\n    signal- and noise-correlation in L2/3 at the reference column edge\n  depends_on:\n  - fig5a-l23-signal-correlation-boundary\n  - fig5b-l23-noise-correlation-boundary\n  criterion: For each responsive L2/3 ROI over a barrel and each reference column, its mean signal\n    (and noise) correlation to the other ROIs in that column (Figure 5E legend), against its\n    distance from the column centre. The legend gives no bins for G-H; 75 um bins as in Figure 2A, a\n    plotting choice. Reproduced when, for both correlations, the EN minus NH difference averaged\n    over ROIs outside the column is more negative than over ROIs inside it, each by a permutation\n    test of the difference in means at p < 0.05 for the outside difference.\n- id: figs5-1-row-and-arc-boundaries\n  statement: The reduction of signal and noise correlations across column boundaries appeared for\n    both within-row and within-arc column boundaries.\n  source: Results, Enrichment strengthens functional column boundaries in L2/3, paragraph 2; Figure\n    5 figure supplement 1\n  quote: The reduction of signal and noise correlations across column boundaries was apparent across\n    both within-row and within-arc column boundaries\n  depends_on:\n  - fig5b-l23-noise-correlation-boundary\n  criterion: Across-column pairs split into pairs whose barrels share a row and pairs whose barrels\n    share an arc (Figure 5 S1 legend). Reproduced when, in both groups, EN mean signal and noise\n    correlations are lower than NH by the permutation test of the difference in means at p < 0.05.\n- id: fig6-l4-within-column-correlations\n  statement: In L4, EN increased both signal (0.681 to 0.774) and noise (0.241 to 0.356) correlations\n    between co-columnar neurons.\n  source: Results, Enrichment strengthens functional column boundaries in L2/3, paragraph 4; Figure 6\n  quote: >-\n    This was true for both signal correlations (NH: 0.681 ± 0.011; EN: 0.774 ± 0.005; p<0.0001) and\n    noise correlations (NH: 0.241 ± 0.006; EN: 0.356 ± 0.002; p<0.0001)\n  statistics:\n  - about: signal correlation\n    test: permutation test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: noise correlation\n    test: permutation test\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: NH L4 within-column signal correlation\n    value: 0.681\n    tolerance: 0.011\n  - quantity: EN L4 within-column signal correlation\n    value: 0.774\n    tolerance: 0.005\n  - quantity: NH L4 within-column noise correlation\n    value: 0.241\n    tolerance: 0.006\n  - quantity: EN L4 within-column noise correlation\n    value: 0.356\n    tolerance: 0.002\n  depends_on:\n  - fig5b-l23-noise-correlation-boundary\n  criterion: As the L2/3 correlation claims, for responsive L4 ROIs in the same barrel. The test is\n    not named in this paragraph and is read as the permutation test of the preceding paragraphs.\n    Readings (A) responsive ROIs in any barrel, (B) only in C1 to C3 (Methods). Reproduced when\n    both tests give p < 0.05 with EN higher and at least three of the four values are within\n    tolerance under one reading.\n- id: figs5-2-neuropil-robustness\n  statement: The enrichment effects on tuning heterogeneity and point representation were\n    qualitatively unchanged with neuropil subtraction at r = 0, 0.3 and 0.7 in L2/3 and L4; effects\n    on signal correlations held at r = 0 and 0.3 but were lost at 0.7, and effects on noise\n    correlations held at all levels.\n  source: Results, Robustness to neuropil contamination, paragraph 1; Figure 5 figure supplement 2\n  quote: Enrichment effects on tuning heterogeneity ( Figure 3 ) and point representation ( Figure 5\n    ) were qualitatively unchanged across these levels of neuropil subtraction in both L2/3 and L4\n    ... Effects of enrichment on signal correlations were conserved for r = 0 and r = 0.3, but were\n    lost for r = 0.7 ... Effects of enrichment on noise correlations persisted across all neuropil\n    subtraction levels\n  depends_on:\n  - fig2a-l23-point-representation-stronger\n  - fig2c-l4-point-representation-weaker\n  - fig3a-l23-enrichment-more-cw-tuned\n  - fig3c-l4-enrichment-more-cw-tuned\n  - fig5a-l23-signal-correlation-boundary\n  - fig5b-l23-noise-correlation-boundary\n  criterion: Raw ROI fluorescence minus r times the neuropil-mask fluorescence before dF/F (Figure 5\n    S2 legend; npSubtract_preDF.m), at r = 0, 0.3, 0.7, then the whole pipeline including the\n    responsiveness test. (\"Figure 5\" in the quote is read as Figure 2, the point representation.)\n    Qualitatively unchanged is read as the same direction of the EN against NH difference at 0-75\n    um for the fraction CW-tuned (L2/3 and L4) and the mean response (L2/3 higher, L4 lower). For\n    correlations, EN against NH within and across columns by the permutation test at p < 0.05.\n    Reproduced when the four directions hold at all three weights, the across-column signal\n    correlation reduction is significant at r = 0 and 0.3 and not at 0.7, and both noise\n    correlation reductions are significant at all three; partially reproduced when all but the r =\n    0.7 signal correlation pattern hold.\n- id: fig7b-single-roi-decoder\n  statement: Single-ROI decoders detected CW deflection against blank above chance, slightly better\n    for EN cells than NH cells (fraction correct 0.65 against 0.63).\n  source: Results, Enrichment improves population coding of columnar whisker deflections, paragraph\n    1; Figure 7B\n  quote: Single-ROI decoders performed above chance, with slightly better performance by EN cells\n    than NH cells (fraction correct for NH ... 0.63 ± 0.005, for EN ... 0.65 ± 0.004, p=0.004,\n    permutation test for difference in means\n  statistics:\n  - test: permutation test for difference in means\n    p: 0.004\n  expected:\n  - quantity: NH single-ROI fraction correct\n    value: 0.63\n    tolerance: 0.005\n  - quantity: EN single-ROI fraction correct\n    value: 0.65\n    tolerance: 0.004\n  criterion: Responsive L2/3 ROIs of Drd3-Cre mice; for each, a logistic regression of stimulus\n    against blank on the single-trial evoked response (the 1 s window, Results), fit on 80% of the\n    CW and blank trials and tested on the other 20%, 500 repetitions, fraction correct averaged\n    (Methods, Neural decoder). Predicted class is the more probable of stimulus and blank. Open,\n    and named as readings, (i) the splits, as (a) 500 random 80/20 splits or (b) 5-fold\n    cross-validation repeated 100 times (the Methods say both \"K-fold\" and \"repeated 500 times\");\n    (ii) class balance, as (a) all trials of both classes or (b) blank trials subsampled to the\n    number of CW trials; (iii) the ROIs, as (a) those over a barrel, tested on its CW, or (b) all\n    responsive ROIs, tested on the whisker of the nearest column centre. Reproduced when, under\n    one combination, EN is higher with p < 0.05 by the permutation test, both means exceed 0.5, and\n    both values are within tolerance; partially reproduced when the test holds but values do not.\n    The tolerances are the SEMs and tight; every combination's values are shown.\n- id: fig7c-population-decoder\n  statement: Detection by population decoders of randomly chosen, simultaneously imaged ROIs improved\n    with ensemble size and was better for EN than NH for ensembles of 3 or more neurons.\n  source: Results, Enrichment improves population coding of columnar whisker deflections, paragraph\n    1; Figure 7C\n  quote: Detection performance increased with population size, and was greater for EN than NH for\n    populations containing ≥3 neurons (p<0.001; permutation test of difference in means\n  statistics:\n  - test: permutation test of difference in means\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig7b-single-roi-decoder\n  criterion: Ensembles of 1, 2, 3, 5, 10, 15, 20, 25 and 30 responsive ROIs from one field, the lesser\n    of 500 or N-choose-K random ensembles per field and size; each ROI classifier's output\n    normalised so units weigh equally, class probabilities summed over the ensemble and the larger\n    class chosen (Methods). Tested whisker, open, (a) the whisker of the column closest to the\n    ensemble centroid (Figure 7C legend), (b) performance averaged over the CWs of the ensemble's\n    columns (Results). Normalisation, open, (a) each ROI's probabilities used as they are (they sum\n    to one per trial), (b) each ROI's probability z-scored over test trials. Unit of the\n    permutation test, open, (a) ensembles pooled, (b) per-field means. Reproduced when, under one\n    combination, mean performance rises with size and EN exceeds NH with p < 0.001 at every size\n    from 3 on; partially reproduced when p < 0.05 at every such size.\n- id: fig7d-clustered-ensemble-topography\n  statement: Spatially clustered ensembles detected the reference whisker best near its column\n    centre; EN decoders outperformed NH decoders for ensembles centred 0-77 and 77-154 um from the\n    column centre, and EN performed worse than NH farther away (e.g. 308-385 um).\n  source: Results, Enrichment improves population coding of columnar whisker deflections, paragraph\n    2; Figure 7D\n  quote: Mean detection performance (on average across the population sizes) was greatest for\n    ensembles centered near the whisker column center, and fell off with distance. EN decoders\n    outperformed NH decoders for ensembles centered at 0-77 µm and 77-154 µm from a column center\n    ... This effect disappeared and even reversed for more distant ensembles, where EN performed\n    worse than NH (e.g., 308-385 µm bin\n  statistics:\n  - about: EN against NH, 0-77 and 77-154 um bins\n    test: 2-way ANOVA\n    p: 2.0e-6\n  - about: EN against NH, 308-385 um bin\n    test: 2-way ANOVA\n    p: 2.0e-6\n  depends_on:\n  - fig7b-single-roi-decoder\n  criterion: Ensembles from k-means clustering of responsive ROI positions in each field, relative\n    to each reference whisker, for every k from 2 to the number of responsive ROIs (Methods),\n    sizes 2 to 42; each tested on detecting the reference whisker against blank as in\n    fig7c-population-decoder; ensembles binned by the distance of their centroid to the reference\n    column centre in 77 um bins (the bins the Results name). The factors of the 2-way ANOVA are\n    not given; readings (a) enrichment and ensemble size within each distance bin, (b) enrichment\n    and distance bin with per-bin comparisons. Reproduced when, under one reading, performance\n    is highest in the 0-77 um bin, EN exceeds NH with p < 0.05 in the 0-77 and 77-154 um bins, and\n    NH exceeds EN with p < 0.05 in the 308-385 um bin; partially reproduced when the near bins hold\n    but not the reversal.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-ssc-10/10.7554-elife.46321.yaml paper/10.7554-elife.46321.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ssc-10/10.7554-elife.46321.yaml",
 "old_string": "  quote: ** denotes greater mean response for EN than NH (p=0.0002, permutation test) ... Regression",
 "new_string": "  quote: denotes greater mean response for EN than NH (p=0.0002, permutation test) ... Regression"
}
```

```
The file claims/crcns-ssc-10/10.7554-elife.46321.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-ssc-10/10.7554-elife.46321.yaml paper/10.7554-elife.46321.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The only remaining checker reports are the two Figure 7D p-values, which the text prints garbled as "p= 2 * 10 - 6" (line 285); I confirmed them by reading. Checking for banned characters and words:

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" claims/crcns-ssc-10/*.yaml; git status --short
```

```
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
?? claims/crcns-ssc-10/
?? scripts
```

**Agent**

I wrote `claims/crcns-ssc-10/10.7554-elife.46321.yaml`. The quote checker passes except for two Figure 7D p-values: the text prints them as "p= 2 * 10 - 6", so the checker can't match them, and I confirmed them by reading the text.

**Text read:** the version of record (PMC6697414, Europe PMC full text), with Results, Discussion, Methods, Table 1 and all figure and figure-supplement legends. The paper has no separate supplementary text and no PDF was supplied, so no figure was read. I also read the linked code, github.com/alemessurier/imaging_analysis_pipeline at commit 5a21c9f. It is incomplete: many functions the figure scripts call are missing, including the one computing equivalent best whiskers (eBWs), the responsive-cell selection, the correlation functions and the decoder.

**Claims:** 34. 33 have quotes; one (Table 1 counts) is marked inferred. 31 claims carry 41 statistical values: mostly permutation tests, plus Fisher's exact tests, 2-way ANOVAs and a slope t-test. 29 claims have expected values. Where the paper gives ± SEM, the SEM is the tolerance; elsewhere it is 10% of the value. Every claim has a criterion except the bare Table 1 counts. Three claims have no reported test: the L4-sharper claim, the barrel-versus-septum sharpening, and the correlation gradient at column edges.

**Details the paper leaves open, with the readings named:**
- **eBW test:** the Results say "see Materials and methods", but neither the Methods nor the code define it. Readings: the paper's two-sided permutation test, uncorrected (E1), with FDR over 8 comparisons (E2), or on medians (E3).
- **Which L2/3 cells enter:** all responsive ROIs, or only those over the nine barrels. For L4, all responsive ROIs or only those in C1 to C3.
- **Z-score centre:** the blank mean, or the blank median as a variant.
- **Best whisker:** by mean (as the Results say) or by median.
- **Methods against code**, where I followed the Methods and named the code as a variant: the responsiveness test (one-sided on means in the Methods, two-sided and mean or median per field in the code), the filter width, and F0 (20th against 5th percentile).
- **Per-claim gaps:**
  - The measure for "sharper in L4": a 225-300 µm to 0-75 µm ratio, or the half-max distance.
  - "Highly similar" in Figure 1F: same best whisker, or a significant correlation.
  - Which response the p = 0.0002 in Figure 4 supplement 1 compares: the four strongest whiskers or all nine.
  - Whether the "columns with at least 3 ROIs" rule applies to Figure 4D.
  - The 48% in the Discussion: pooled, or the mean over columns.
- **Decoder:** 80/20 splits against K-fold, class balance, which ROIs and which whisker are tested, how outputs are normalised, and the unit of the test (ensembles or per-field means).
- **Figure 7D:** the factors of the 2-way ANOVA (enrichment by ensemble size within each distance bin, or enrichment by distance bin).

**Inconsistencies in the paper:**
- The Scnn1a-Cre barrel-radius test prints p = 0.01, but the text and legend say there is no significant effect. I recorded it as printed and judge the claim on the legend's reading.
- The neuropil paragraph cites "Figure 5" for the point representation; I read it as Figure 2.

**Missing from the paper:** nothing that stops claims from being written. The eBW method is the one detail a whole group of claims (Figures 3A, 3C and the Figure 3 supplement) depends on, and it is handled through readings E1 to E3. Whether the dataset holds the juxtacellular recordings (Figure 1F) and the barrel radii is for the author to find.

## End of run

27 turns, 7 minutes, $2.35 at API prices, result: success.
