# 001187 · claims-check · run 39824598267

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001187/ paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; cat claims/001187/*.yaml
```

```
<persisted-output>
Output too large (56.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7ae2d244-6900-4406-b5ab-7e4818c9ea15/tool-results/bfauz0mff.txt

Preview (first 2KB):
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001187/10.1016-j.neuron.2024.09.013.yaml paper/10.1016-j.neuron.2024.09.013.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001187/10.1016-j.neuron.2024.09.013.yaml"
}
```

```
1	# Claims for Daume, Kaminski, Salimpour, Gomez Palacio Schjetnan, Anderson, Valiante, Mamelak and
2	# Rutishauser (2024), Neuron 112, 3957-3968, on dandiset 001187.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
4	# docs/protocol.md, version pilot-10.
5	#
6	# Text read. The accepted author manuscript in PubMed Central (PMC11624075, NIHMS2025394), full text
7	# with Results, figure legends and STAR Methods (paper/10.1016-j.neuron.2024.09.013.txt), and its
8	# supplement (NIHMS2025394-supplement-1.pdf, extracted into the same file: Figures S1 to S4 and Table
9	# S1). The bioRxiv preprint (10.1101/2024.07.15.603630 v1) was searched for method details only; it
10	# adds none. The main-text figures were not viewed (no main-text PDF was supplied), so numbers printed
11	# only inside panels are not used, and units of axes the text does not name are left open.
12	#
13	# Code read. https://github.com/rutishauserlab/SBCAT-NO-release-NWB, commit 6d07204 (2024-09-04,
14	# "final main"), the repository the paper links (also Zenodo 10.5281/zenodo.13621888). It holds a
15	# MATLAB script (NWB_SBCAT_NO_analysis_main.m) that loads the dandiset and computes the behaviour
16	# plots of Fig. 1c-g (plot_behavior.m, no statistics), the 0.1 Hz rate filter (rateFilter_units.m),
17	# the category-neuron selection (NWB_calcCatSelective_SB.m), the memory-selective selection
18	# (NWB_calcMemSelective_SB.m), the mixed-effects GLM of Fig. 3a (NWB_computeGLM.m), and the example
19	# neurons of Fig. 2a and 4a. It has no code for Fig. 2b,c,e,f, 3b-h or Fig. 4b-g; those analyses
20	# rest on the Methods and legends alone, with the Fig. 3a code as the nearest implementation where
[... 749 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n "" paper/10.1016-j.neuron.2024.09.013.txt | awk -F: 'length($0)>0' | head -400
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.09.013.txt",
 "offset": 33,
 "limit": 150
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "Experimental model\|Method details\|Quantification\|Spike sorting\|Selection of neurons\|Single-neuron AUC\|Interaction between\|Statistics\|Relating WM\|Table S1\|Supplement" paper/10.1016-j.neuron.2024.09.013.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.09.013.txt",
 "offset": 230,
 "limit": 45
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.09.013.txt",
 "offset": 611,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.09.013.txt",
 "offset": 730,
 "limit": 130
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes (0 problems). Now checking Table S1's column definitions, which several claims rest on.

**Agent calls Bash**

```bash
sed -n 1080,1110p paper/10.1016-j.neuron.2024.09.013.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 735,1090p paper/10.1016-j.neuron.2024.09.013.txt | python3 -c "
import sys,re
lines=[l.strip() for l in sys.stdin]
rows=[];cur=None;trip=[]
for l in lines:
    if re.match(r'^P\d+\w*',l) and '/' not in l: cur=l;trip=[];continue
    m=re.match(r'^(\d+)/(\d+)/(\d+)\s*\*?$',l)
    if m and cur:
        trip.append(tuple(map(int,m.groups())))
        if len(trip)==2: rows.append((cur,trip));cur=None
    if cur and re.match(r'^[\d.]+ / [\d.]+',l): pass
print(len(rows))
s=[0]*6
for r,t in rows:
    for i in range(3): s[i]+=t[0][i]; s[3+i]+=t[1][i]
print(s)
for r,t in rows: print(r,t)
" | head -60; sed -n 735,1090p paper/10.1016-j.neuron.2024.09.013.txt | grep -n '\*'
```

Result: not kept, because it reads the paper's text.

**Agent**

Table S1 sums match the file's comment (104/53/386 hippocampus, 220/68/587 amygdala). Next I'll try to check the code claims against the linked repository.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://github.com/rutishauserlab/SBCAT-NO-release-NWB.git sb 2>&1 | tail -2; cd sb 2>/dev/null && git log --oneline -1 && git ls-files | head -50
```

```
6d07204 final main
.gitignore
LICENSE
NWB_SBCAT_NO_analysis/NWB_SBCAT_NO_analysis_main.m
NWB_SBCAT_NO_analysis/helpers/3rdParty/permutationTest/LICENSE.txt
NWB_SBCAT_NO_analysis/helpers/3rdParty/permutationTest/README.md
NWB_SBCAT_NO_analysis/helpers/3rdParty/permutationTest/permutationTest.m
NWB_SBCAT_NO_analysis/helpers/3rdParty/permutationTest/permutationTest.png
NWB_SBCAT_NO_analysis/helpers/3rdParty/randanova1/license.txt
NWB_SBCAT_NO_analysis/helpers/3rdParty/randanova1/randanova1.m
NWB_SBCAT_NO_analysis/helpers/3rdParty/sort_nat/license.txt
NWB_SBCAT_NO_analysis/helpers/3rdParty/sort_nat/sort_nat.m
NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/anova1_cell.m
NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/anova1rm_cell.m
NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/anova2_cell.m
NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/anova2rm_cell.m
NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/concatdata.m
NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/finputcheck.m
NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/stat_surrogate_pvals.m
NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/statcond.m
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sb/NWB_SBCAT_NO_analysis/helpers && cat custom/NWB_computeGLM.m; grep -n "statcond\|0.1\|<\|perm\|anova\|0.2\|1.2" custom/NWB_calcCatSelective_SB.m custom/NWB_calcMemSelective_SB.m | head -40
```

```
function m = NWB_computeGLM(nwbAll, all_units, cat_cells_all, params)
%NWB_computeGLM Takes the output of NWB_SB_extractUnits and runs
% a mixed-effects GLM across all category neurons

if isfield(params,'rateFilter') && ~isempty(params.rateFilter) && params.rateFilter > 0
    rateFilter = params.rateFilter;
else
    rateFilter = [];
end

whichWindow = [0 2.5]; % maintenance
whichWindow_bsl = [-.9 -.3]; % baseline

% Filtering for Global Rate (rateFilter should be a nonzero float)
if ~isempty(rateFilter)
    aboveRate = rateFilter_units(nwbAll,all_units,rateFilter);
else
    aboveRate = ones(length(all_units),1);
end
all_units = all_units(logical(aboveRate));
[... 155 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sb/NWB_SBCAT_NO_analysis && grep -n "alphaLim\|rateFilter\|nonPar_method\|vary\|run" helpers/custom/NWB_calcCatSelective_SB.m NWB_SBCAT_NO_analysis_main.m | head -20; sed -n 100,150p helpers/custom/NWB_calcCatSelective_SB.m; grep -n "5\b\|> *5\|RT\|conf" helpers/internal/plotting/plot_behavior.m | head -40
```

```
helpers/custom/NWB_calcCatSelective_SB.m:2:%NWB_CALCSELECTIVE Takes the output of NWB_SB_extractUnits and runs
helpers/custom/NWB_calcCatSelective_SB.m:6:if isfield(params,'rateFilter') && ~isempty(params.rateFilter) && params.rateFilter > 0
helpers/custom/NWB_calcCatSelective_SB.m:7:    rateFilter = params.rateFilter;
helpers/custom/NWB_calcCatSelective_SB.m:9:    rateFilter = [];
helpers/custom/NWB_calcCatSelective_SB.m:12:% Filtering for Global Rate (rateFilter should be a nonzero float)
helpers/custom/NWB_calcCatSelective_SB.m:13:if ~isempty(rateFilter)
helpers/custom/NWB_calcCatSelective_SB.m:14:    aboveRate = rateFilter_units(nwbAll,all_units,rateFilter);
helpers/custom/NWB_calcCatSelective_SB.m:119:    alphaLim = 0.05;
helpers/custom/NWB_calcCatSelective_SB.m:122:%     nonPar_method = 'other'; % Prior selectivity method. Not same used in Daume et al
helpers/custom/NWB_calcCatSelective_SB.m:123:    nonPar_method = 'statcond';
helpers/custom/NWB_calcCatSelective_SB.m:126:        p_ANOVA = anovan(Hz_allTrials,{string(CAT_allTrials)}, 'display','off','model', 'linear','alpha',alphaLim,'varnames','picID');
helpers/custom/NWB_calcCatSelective_SB.m:127:        if p_ANOVA < alphaLim % First test: 1-way ANOVA
helpers/custom/NWB_calcCatSelective_SB.m:128:            p_bANOVA = anovan(Hz_allTrials,{string(id_Trial_maxOnly)}, 'display','off','model', 'linear','alpha',alphaLim,'varnames','picID');
helpers/custom/NWB_calcCatSelective_SB.m:129:            if p_bANOVA < alphaLim % Second Test: Binarized 1-way ANOVA (simplifies to t-test)
helpers/custom/NWB_calcCatSelective_SB.m:137:        if strcmp(nonPar_method,'statcond') % Statcond version (From Daume et al)
helpers/custom/NWB_calcCatSelective_SB.m:144:        elseif strcmp(nonPar_method,'other') % Non-statcond version
helpers/custom/NWB_calcCatSelective_SB.m:151:        if p_ANOVA < alphaLim && ~isnan(F_ANOVA)  % First test: 1-way ANOVA            
helpers/custom/NWB_calcCatSelective_SB.m:153:            if strcmp(nonP
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sb/NWB_SBCAT_NO_analysis && sed -n 1,30p helpers/internal/plotting/plot_behavior.m; sed -n 52,70p helpers/internal/plotting/plot_behavior.m; sed -n 84,135p helpers/internal/plotting/plot_behavior.m; grep -n "statcond" helpers/custom/NWB_calcMemSelective_SB.m
```

```
function plot_behavior(nwbAll)
%% This script analyses behavior of all sessions in SternbergCAT_NO
% JD 2024

nsubjects = length(nwbAll);

LTM_values = 1;
WM_values = 2;

%% Test acc and RT between WM load
clear RT_load1 RT_load3 acc_load1 acc_load3 acc_all

for isubj = 1:nsubjects
    clear RT acc
    
    RT = double(nwbAll{isubj}.intervals.values{WM_values}.vectordata.get('response_time').data.load());
    acc = double(nwbAll{isubj}.intervals.values{WM_values}.vectordata.get('response_accuracy').data.load());
    WM_load = double(nwbAll{isubj}.intervals.values{WM_values}.vectordata.get('loads').data.load());
    
    RT(RT>5) = nan;
[... 83 more lines not kept]
```

**Agent**

The code checks out: the 0.1 two-sided threshold, the RT > 5 s exclusion, the confidence recoding, and the O-C outlier rule all match the file. Now applying corrections.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001187/10.1016-j.neuron.2024.09.013.yaml",
 "old_string": "  source: Results, Persistent activity of category neurons in the hippocampus, paragraph 4; Figure 3h;\n    STAR Methods, Relating WM maintenance activity to LTM formation, paragraph 2\n  quote: To test whether category-selective activity predicted LTM formation during the encoding window,\n    we based our GLM analysis on firing rates determined during the picture 1 window of preferred\n    images (0–2 s).",
 "new_string": "  source: Results, Persistent activity of category neurons in the hippocampus, paragraph 4; Figure 3h;\n    STAR Methods, Relating WM maintenance activity to LTM formation, paragraph 2\n  quote: or for the visually evoked response of category neurons when images were shown on the screen\n    during encoding (Fig. 3h; encoding 1; 0 – 2s after picture onset; preferred trials only). None of\n    the main effects nor interactions in either of the mixed-effects GLMs showed any significant\n    relationship between FR and the factors tested (all p > 0.06)"
}
```

```
The file claims/001187/10.1016-j.neuron.2024.09.013.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001187/10.1016-j.neuron.2024.09.013.yaml",
 "old_string": "  statement: In a GLM over category neurons of both areas, no main effect of LTM accuracy, confidence\n    or area is significant, but every interaction with area is,",
 "new_string": "  statement: In a GLM over category neurons of both areas, no main effect of LTM accuracy, confidence\n    or area is significant, nor the LTM accuracy by confidence interaction, but every interaction with\n    area is,"
}
```

```
The file claims/001187/10.1016-j.neuron.2024.09.013.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001187/10.1016-j.neuron.2024.09.013.yaml",
 "old_string": "    after the rate filter of U) against the table's recorded count. Reproduced when every one of the\n    46 sessions matches under one of the two counts; partially reproduced when at least 41 (90%) do.",
 "new_string": "    after the rate filter of U) against the table's recorded count. Reproduced when every one of the\n    46 sessions matches under one of the two counts; partially reproduced when some do and others do\n    not, the sessions that differ being listed."
}
```

```
The file claims/001187/10.1016-j.neuron.2024.09.013.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001187/10.1016-j.neuron.2024.09.013.yaml",
 "old_string": "    only baseline the paper defines. Reproduced when no GLM effect and not the t-test reach p < 0.05",
 "new_string": "    only baseline the paper defines; (D3) the trials of the t-test, (a) correct LTM trials only, as\n    for the GLM in the sentence before, or (b) all trials of preferred old and new pictures, the\n    sentence on the t-test not restricting them. Reproduced when no GLM effect and not the t-test reach p < 0.05"
}
```

```
The file claims/001187/10.1016-j.neuron.2024.09.013.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -rn -A8 "^checks:" claims/*/*.yaml | head -30
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
--
claims/000006/10.1038-s41586-018-0642-9.yaml:841:checks:
claims/000006/10.1038-s41586-018-0642-9.yaml-842-- date: "2026-10-20"
claims/000006/10.1038-s41586-018-0642-9.yaml-843-  kind: agent
claims/000006/10.1038-s41586-018-0642-9.yaml-844-  model: claude-opus-5-5
claims/000006/10.1038-s41586-018-0642-9.yaml-845-  ready: true
claims/000006/10.1038-s41586-018-0642-9.yaml-846-  changes:
claims/000006/10.1038-s41586-018-0642-9.yaml-847-  - Opening comment. Added two code details read in Ephys.zip Code/ (Figshare doi:10.25378/janelia.7007846 v1),
claims/000006/10.1038-s41586-018-0642-9.yaml-848-    the zero weight of a neuron with rank-sum p of 1 in DirectionVector, and the epoch means taking time > start
claims/000006/10.1038-s41586-018-0642-9.yaml-849-    and <= end, unlike the CD windows.
--
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> claims/001187/10.1016-j.neuron.2024.09.013.yaml <<'EOF'
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig3h-encoding-no-effect. The quote was a Methods sentence describing the analysis, which states no finding; replaced it with the Results sentences of paragraph 4 that cite Fig. 3h and give the result (all p > 0.06).
  - fig3a-area-interactions. The statement left out that the LTM accuracy by confidence interaction was also not significant, which the quote and the criterion include; added it.
  - table-s1-counts. The partial grade at 41 of 46 sessions (90%) is a threshold from no source; replaced it by a partial grade when some sessions match and others do not, with the differing sessions listed.
  - fig4d-category-no-memory-signal. The Results sentence on the t-test (preferred old against new) does not say whether only correct LTM trials are used, as for the GLM before it; named this open as D3, with both readings.
  - Checked against the linked code (SBCAT-NO-release-NWB, commit 6d07204) the details the file attributes to it (two-sided statcond p < 0.1 for the right-sided category test, response times above 5 s set to missing, the confidence recoding and the O-C outlier rule of NWB_computeGLM.m, high confidence as ratings 1 and 6 in plot_behavior.m); all match. Table S1 sums (104, 53, 386 hippocampus; 220, 68, 587 amygdala) match the opening comment.
  - Open, fig3e-early-delay-cluster and fig3f-amygdala-no-cluster. The cluster-forming threshold is given in no source; the file takes FieldTrip's default 0.05 as a standard choice though it can change the cluster's extent. Not settled from the paper.
  - Open, behaviour-overall-accuracy and ltm-rt-confidence. Tolerances are the SEM derived from the stated SD and n, with a reason given, where the protocol names the stated spread; kept, since these are means of the same sessions, but a reviewer may prefer the SD.
  - Open, fig3g-nonpreferred-no-effect. The Fig. 3g legend does not say whether area is a fixed effect of that GLM; the file follows the Methods model with area, which the legend allows but does not state.
EOF
python tools/claims_check.py claims/001187/10.1016-j.neuron.2024.09.013.yaml paper/10.1016-j.neuron.2024.09.013.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file for DANDI:001187 is ready for an attempt. I made four corrections and left three points open. Nothing is committed.

**Checker result** (the same before and after my edits): `29 claims, 28 quotes, 43 statistical values, 0 problems`

I also cloned the linked code (SBCAT-NO-release-NWB, commit 6d07204) and checked every detail the file attributes to it. All of them match: the category-neuron test, the 5 s response-time cutoff, the confidence recoding, the outlier rule in the GLM code and the high-confidence definition. The neuron counts in Table S1 add up to the totals in the file's opening comment.

**Changes, by claim**
- **fig3h-encoding-no-effect:** the quote was a Methods sentence that describes the analysis but states no result. I replaced it with the Results sentences that cite Fig. 3h and give the result ("all p > 0.06").
- **fig3a-area-interactions:** the statement left out that the LTM accuracy × confidence interaction was also not significant. The quote and the criterion already include it, so I added it.
- **table-s1-counts:** the "partially reproduced" grade at 41 of 46 sessions (90%) had no source. It now applies when some sessions match and others don't, with the mismatched sessions listed.
- **fig4d-category-no-memory-signal:** the paper doesn't say whether the old-vs-new t-test uses only correct LTM trials, as the GLM before it does. I added this as an open detail (D3) with both readings.

**Still open** (recorded under `checks`)
- **fig3e and fig3f (cluster tests):** no source gives the threshold that forms the clusters. The file uses FieldTrip's default of 0.05, which could change how far the cluster extends.
- **behaviour-overall-accuracy and ltm-rt-confidence:** the tolerances are standard errors worked out from the paper's SD and session count, with a reason given. The protocol names the stated spread (the SD itself), which would be much looser.
- **fig3g-nonpreferred-no-effect:** the figure legend doesn't say whether brain area is a factor in that model. The file follows the Methods model, which includes area.

**Ready:** yes.

## End of run

24 turns, 2 minutes, result: success.
