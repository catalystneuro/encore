# 001785 · claims · run 39630543925

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/Reader/,$p' | head -300; ls claims/001785 claims/001453 paper/ 2>&1; git show --stat HEAD HEAD~1 | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat transcripts/001785/claims-report.md transcripts/001785/claims-check-report.md; head -60 paper/*.txt; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat transcripts/001785/claims-check-report.md; head -c 3000 paper/*.txt; echo; wc -c paper/*; grep -n "001785" papers/manifest.yaml -A15 | head -40
```

Result: not kept, because it reads the paper's text.

**Agent**

Supplement now present. Reading the full text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02301-4.txt",
 "offset": 7
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l paper/*.txt; awk '{print NR": "length($0)}' paper/*.txt | sort -t: -k2 -n -r | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 7p paper/*.txt | fold -s -w 2000 > $TMPDIR/main.txt; wc -l $TMPDIR/main.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "limit": 24
}
```

```
1	pmc Nat Neurosci Nat Neurosci 981 npgopen 9809671 Nature Neuroscience 1097-6256 1546-1726 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC13337501 PMC13337501.1 13337501 13337501 42225897 10.1038/s41593-026-02301-4 2301 1 Article Deep brain stimulation induces white matter remodeling and functional changes to brain-wide networks http://orcid.org/0000-0003-2374-3002 Fujimoto Satoka H. [removed: an e-mail address] 1 2 7 http://orcid.org/0000-0002-1621-2003 Fujimoto Atsushi 1 2 7 http://orcid.org/0000-0001-5735-4369 Elorette Catherine 1 2 Seltzer Adela 1 2 Andraka Emma 1 2 http://orcid.org/0009-0006-4539-9301 Herbert Keondre 1 2 Verma Gaurav 3 4 Janssen William G. M. 1 Fleysher Lazar 4 Folloni Davide 1 2 http://orcid.org/0000-0002-6446-0677 Choi Ki Sueng 3 4 Russ Brian E. 1 5 6 http://orcid.org/0000-0002-1672-2716 Mayberg Helen S. 1 3 http://orcid.org/0000-0002-1411-7555 Rudebeck Peter H. [removed: an e-mail address] 1 2 1 https://ror.org/04a9tmd77 grid.59734.3c 0000 0001 0670 2351 Nash Family Department of Neuroscience and Friedman Brain Institute, Icahn School of Medicine at Mount Sinai, New York, NY USA 2 https://ror.org/04a9tmd77 grid.59734.3c 0000 0001 0670 2351 Lipschultz Center for Cognitive Neuroscience, Icahn School of Medicine at Mount Sinai, New York, NY USA 3 https://ror.org/031e8jz65 grid.430600.1 0000 0004 0431 8956 Nash Family Center for Advanced Circuit Therapeutics, Mount Sinai West Hospital, New York, NY USA 4 https://ror.org/04a9tmd77 grid.59734.3c 0000 0001 0670 2351 BioMedical Engineering and Imaging Institute, Icahn School of Medicine at Mount Sinai, New York, NY USA 5 https://ror.org/01s434164 grid.250263.0 0000 0001 2189 4777 Center for Biomedical Imaging and Neuromodulation, Nathan Kline Institute, Orangeburg, NY USA 6 https://ror.org/0190ak572 grid.137628.9 0000 0004 1936 8753 Department of Psychiatry, New York University at Langone, New York, NY USA 7 https://ror.org/017zqws13 grid.17635.36 0000 0004 1936 8657 Present Address: 
2	Depar
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 25
}
```

```
File content (36839 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02301-4.txt",
 "offset": 8
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 25,
 "limit": 23
}
```

```
25	Discussion The present results indicate that SCC-DBS is associated with focal white matter structural remodeling in the MCC-CB (Figs. 2 and 3 ) as well as a brain-wide shift in the functional connectivity patterns across multiple networks (Figs. 4 and 5 ). These stimulation-induced changes could not be explained by the alterations associated with implantation of the DBS lead alone (Fig. 6 ). Our results highlight the potential role of white matter plasticity in the efficacy of DBS therapies for psychiatric and neurological disorders. DBS induced changes in white matter macro- and microstructure Prior work has shown that white matter remodeling can be induced by electrical, optogenetic or chemogenomic stimulation of neurons in gray matter 28 – 30 . Our data reveal that DBS targeted to white matter induces both macro- and micro-structual changes in white matter in the CB distal to the site of stimulation. This pattern of results complements prior studies that have pointed to a role for white matter dysfunction as contributing to the pathophysiology of depression 31 – 33 . Notably, abnormal white matter integrity in the CB was recently found to be positively correlated with symptom severity in patients with treatment-resistant depression 13 . In this context, our observation that SCC-DBS selectively induces white matter remodeling in the CB provides additional evidence that inducing structural plasticity in this tract may be a key mechanism through which DBS for depression mediates its therapeutic effects and results in sustained recovery over years with ongoing stimulation 8 . Surprisingly, only the CB exhibited a change in white matter integrity following SCC-DBS, despite chronic stimulation of the three targeted tracts, as used with clinical DBS, all of which have been shown to be necessary for clinical response 7 . Several mechanisms could account for this selective effect. First, unlike the FM or the UF, the CB uniquely contains long-range dopaminergic and 
26	
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 48
}
```

```
48	of UF and FM. Symbols indicate average values for individual animals (circles: monkey N; triangles: monkey T). Box represents the interquartile range (IQR; 25 th –75 th percentile). Green line is the median. Whiskers extend to 1.5 × IQR. Outliers are not displayed. For three box plots, each data point represents measurements from individual fields (5 fields per hemisphere per section) across four coronal sections, collected from two monkeys. The number of field-wise measurements (n) used for statistical analysis was as follows: stimulated hemisphere, n = 40 (5 fields × 4 sections × 2 subject); control hemisphere, n = 40. CC1/DAPI ratio, number of CC1 positive cells and number of DAPI positive cells were compared between hemispheres using 1-way ANOVA. Statistical comparisons assessed differences between stimulation side and control side. All tests were two-sided. The main effect of side were not significant (CC1/DAPI ratio, F 1,76 = 1.45, P = 0.2319, ηp 2 = 0.019, #CC1, F 1,76 = 0.79, P = 0.3778, ηp 2 = 0.010, #DAPI, F 1,76 = 0, P = 0.9611, ηp 2 = 4.97e-05). Source data Extended Data Fig. 7 Functional connectivity with SCC is altered consistently across individual subjects by SCC-DBS. The left and middle columns show functional connectivity maps with the stimulated SCC for each monkey at the pre-DBS (top row) and post-DBS (second row) time points (left column: monkey N; middle column: monkey T). The third row presents the difference maps (post-DBS functional connectivity – pre-DBS functional connectivity) for each monkey. The sagittal slices show the stimulated hemisphere. For axial images of monkey N, the left and right sides were flipped to display the stimulated hemisphere on the right side of the image. Green circles indicate the location of the stimulated contact of the SCC-DBS lead. The right column displays averaged functional connectivity changes with right SCC in non-surgical control group, shown in sagittal (left, right hemisphere is shown) and axial 
49
[... 23 more lines not kept]
```

**Agent**

The full text now includes the supplement (Supplementary Methods 1–7 and Tables 1–11), so the earlier block is lifted. Next: the format example and the checker.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -250; wc -l claims/001453/*.yaml; sed -n 1,60p tools/claims_check.py
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 291 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 250,321p claims/001453/*.yaml; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | head -250
```

```
- id: fig2k-more-monocular
  statement: DC have a higher proportion of purely monocular neurons than ZF (0.37 against 0.16,
    p < 0.05).
  source: Figure 2K
  quote: DC show a higher proportion of purely monocular neurons (ZF = 0.16, DC = 0.37
  statistics:
  - test: Student's t-test
    p: 0.05
    p_relation: "<"
    n: 5 ZF and 5 DC fish
- id: fig2l-bi-ratio
  statement: The binocularity index ratio is higher in ZF than in DC (0.72 against 0.24, p =
    0.010).
  source: Figure 2L
  quote: BI ratios show a higher fraction of binocular neurons in ZF compared to DC (ZF = 0.72, DC =
    0.24
  statistics:
  - test: Student's t-test
    p: 0.01
    n: 5 ZF and 5 DC fish
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"; grep -n "001785\|001773" -r docs papers/*.yaml 2>/dev/null | head; ls papers
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
[... 86 more lines not kept]
```

**Agent**

Now the dataset's archive title and description, and the code the paper links to (in DANDI:001773).

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001785/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/001785/versions/draft/" | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'));print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/001773/versions/0.260416.1939/" | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'))"; curl -s "https://api.dandiarchive.org/api/dandisets/001773/versions/0.260416.1939/assets/?page_size=1000" | python -c "
import json,sys;d=json.load(sys.stdin);print(d['count'])
for a in d['results']:
  p=a['path']
  if not p.endswith(('.nii.gz','.nii','.json','.tsv')) or 'code' in p.lower(): print(p, a['size'], a['asset_id'])
" | head -80
```

Result: the fetched text is not kept.

**Agent**

The paper's code is in DANDI:001773 (17 MATLAB scripts plus source-data tables). Downloading the scripts only.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/code && cd $TMPDIR/code && curl -s "https://api.dandiarchive.org/api/dandisets/001773/versions/0.260416.1939/assets/?page_size=1000" | python -c "
import json,sys;d=json.load(sys.stdin)
for a in d['results']:
  p=a['path']
  if p.endswith('.m') or p.endswith('.md'): print(a['asset_id']+'\t'+p.split('/')[-1])
" | while IFS=$'\t' read id name; do curl -sL "https://api.dandiarchive.org/api/assets/$id/download/" -o "$name"; done; ls -la; cat README.md; md5sum *FCmatrix.m *mkD_analysis*FC*
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat Fig2A_dbs_FA_wholetract_analysisscript_a.m Fig2B_dbs_FA_CB_part_analysisscript_a.m
```

```
clear all;
close all;

maindir = char('C:\MATLAB_analy\DBS\data\');
cd(maindir);

% load list
list = importdata('dbs_FA_wholetract_data_a.xlsx');

%% ANOVA
y = list.data(:,1);
g1 = list.data(:,2);
g2 = list.data(:,3);
g3 = list.data(:,4);
g4 = list.data(:,5);

model_mat2=[1 0 0 0;
    0 1 0 0;
    0 0 1 0;
    0 0 0 1;
[... 444 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat Fig3CandE5_dbs_IF_CC1_MCC_CB_analysisscript_a.m Fig3F_dbs_EMgratio_analysisscript_a.m Fig6C_dbs_IF_CC1_mkD_MCC_CB_analysisscript_a.m; diff Fig3CandE5_dbs_IF_CC1_MCC_CB_analysisscript_a.m FigE6A_dbs_IF_CC1_dACC_CB_analysisscript_a.m; diff FigE6A_dbs_IF_CC1_dACC_CB_analysisscript_a.m FigE6B_dbs_IF_CC1_UF_FMoverlap_analysisscript_a.m
```

```
clear all;
close all;

maindir = char('C:\MATLAB_analy\DBS\data\'); 
cd(maindir);

% load list
% MCC-CB
list = importdata('CC1_MCC_CB_data_a.xlsx');

%ANOVA
y1 = list.data(2:end,1);
y2 = list.data(2:end,2);
y3 = list.data(2:end,3);
g1 = list.data(2:end,4);
g2 = list.data(2:end,5);

% CC1/DAPI ratio
[p,tbl,stats] = anovan(y3,{g1,g2},'model','full','varnames',{'monkey','side'});
% number of CC1 positive cell
[... 249 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat "Fig4andE10C_Fujimoto_NatNeuro_2026_FCmatrix.m"
```

```
%-------------------------------------------------------------------
% Functional connectome analysis for Fujimoto SH et al., (2026)
%-------------------------------------------------------------------
clear all; close all;

% set data directory
datadir = char('/Data');
analydir = char('/Codes');
cd(analydir);

% specify ROI mask (use mask after 3dresample)
MASK = "SCHARM"; % atlas (CHARM & SARM)
LEVEL = "4"; % Lv 4

MASKL = strcat(MASK,LEVEL);
MASKROIS = sprintf("SCHARM_in_NMT_15mm.nii.gz'[%s]'",string(str2num(LEVEL)-1));
tmp_label_table_CHARM = importdata(sprintf('CHARM_key_%s.txt',LEVEL),'\t');
tmp_label_table2_CHARM = string(tmp_label_table_CHARM.textdata);
label_table_CHARM = tmp_label_table2_CHARM(2:end,1:2);
tmp_label_table_SARM = importdata(sprintf('SARM_key_%s.txt',LEVEL),'\t');
[... 317 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat Fig5BCandE9_dbs_FC_25norm_mkNT_analysisscript_a.m | head -150
```

```
clear all;
close all;

maindir = char('C:\MATLAB_analy\DBS\data\');
cd(maindir);

% load list
list = importdata('dbs_FC25norm_mkNT_concatenated_all_data_a.xlsx');

%% ROI analysis - ANOVA
fc_25_roi = list.data(:,4);
mk_25_roi = list.data(:,5);
stim_25_roi = list.data(:,7);
side_25_roi = list.data(:,8);
roi_25_roi = list.data(:,6);

model_mat=[1 0 0 0;
    0 1 0 0;
    0 0 1 0;
    0 0 0 1;
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; sed -n 150,400p Fig5BCandE9_dbs_FC_25norm_mkNT_analysisscript_a.m | grep -n -i "anovan\|network\|hub\|model\|roi ==\|ismember\|net\b\|multcompare\|%" | head -60
```

```
15:    % overlay mean for subjects
42:        cond1 = (A == sprintf('PrePost=1,side=1,roi=%d',roi) && ...
43:            B == sprintf('PrePost=2,side=1,roi=%d',roi));
44:        cond2 = (A == sprintf('PrePost=2,side=1,roi=%d',roi) && ...
45:            B == sprintf('PrePost=1,side=1,roi=%d',roi));
65:        cond1 = (A == sprintf('PrePost=1,side=2,roi=%d',roi) && ...
66:            B == sprintf('PrePost=2,side=2,roi=%d',roi));
67:        cond2 = (A == sprintf('PrePost=2,side=2,roi=%d',roi) && ...
68:            B == sprintf('PrePost=1,side=2,roi=%d',roi));
85:%% Network analysis - data reorganization for nw
86:% DMN
87:DMN = list.data(ismember(list.data(:,6), [1,2,3]), :);
90:% SAN
91:SAN = list.data(ismember(list.data(:,6), [4,5]), :);
94:% CEN
95:CEN = list.data(ismember(list.data(:,6), [6,7]), :);
98:% LIM
99:LIM = list.data(ismember(list.data(:,6), [1,5,8,9,10,11,12]), :);
102:% SMN
103:SMN = list.data(ismember(list.data(:,6), [13,14,15]), :);
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; grep -n "anovan\|model_mat\|^    [01] [01]\|multcompare\|importdata\|ismember\|ttest\|ranksum" Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m Fig6B_dbs_FA_CB_part_mkD_analysisscript_a.m Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m; diff Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m Fig6DandE10Ddbs_FC_25norm_mkD_analysisscript_a.m && echo same; sed -n 1,60p FigE1_dbs_behavior_analysisscript_a.m
```

```
Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m:8:list = importdata('dbs_FA_wholetract_mkD_data_a.xlsx');
Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m:16:model_mat=[1 0 0;
Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m:17:    0 1 0;
Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m:18:    0 0 1;
Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m:19:    1 1 0;
Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m:20:    1 0 1;
Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m:21:    0 1 1;
Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m:22:    1 1 1;];
Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m:23:[p,tbl,stats] = anovan(y,{g1,g2,g3},"Model",model_mat,"Varnames",["PrePost","side","tract"]);
Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m:26:[c,m,h] = multcompare(stats);
Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m:27:[results,~,~,gnames] = multcompare(stats,"Dimension",[1 2 3]);
Fig6B_dbs_FA_CB_part_mkD_analysisscript_a.m:8:list = importdata('dbs_FA_CB_subpart_mkD_data_a.xlsx');
Fig6B_dbs_FA_CB_part_mkD_analysisscript_a.m:16:model_mat=[1 0 0;
Fig6B_dbs_FA_CB_part_mkD_analysisscript_a.m:23:[p,tbl,stats] = anovan(y,{g1,g2,g3},"Model",model_mat,"Varnames",["PrePost","side","part"]);
Fig6B_dbs_FA_CB_part_mkD_analysisscript_a.m:26:[c,m,h] = multcompare(stats);
Fig6B_dbs_FA_CB_part_mkD_analysisscript_a.m:27:[results,~,~,gnames] = multcompare(stats,"Dimension",[1 2 3]);
Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m:8:list = importdata('dbs_FC25norm_mkD_concatenated_all_data_a.xlsx');
Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m:16:model_mat=[1 0 0;
Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m:17:    0 1 0;
Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m:18:    0 0 1;
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python - <<'E'
import re
L=open('10.1038-s41593-026-02301-4.txt').read().split('\n')
def tab(a,b):
    seg=L[a-1:b]
    out=[]
    for i in range(len(seg)-1):
        m=re.match(r'^([\d.]+) ×10\^-(\d+)$',seg[i+1].strip())
        if m: out.append((seg[i].strip(), float(m.group(1))*10**-int(m.group(2))))
    return out
from scipy.stats import f
for name,(a,b) in {'T1':(426,566),'T2':(573,663),'T10':(1994,2102)}.items():
    t=tab(a,b); ps=[p for _,p in t]
    print(name,len(t),'max p',max(ps),'n<0.01/122',sum(p<0.01/122 for p in ps),'n<0.05/122',sum(p<0.05/122 for p in ps))
print(f.sf(6.02,1,1238),f.sf(6.02,2,1238),f.sf(4.64,1,3187),f.sf(5.42,1,1357),f.sf(9,1,108),f.sf(58.98,1,696),f.sf(186.48,1,20279),f.sf(51.09,1,21967),f.sf(7.36,1,10972),f.sf(24.55,1,492),f.sf(4.58,1,10106))
from scipy.stats import t
print(2*t.sf(0.9888,27))
E
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
cd paper; python - <<'E'
import re
L=open('10.1038-s41593-026-02301-4.txt').read().split('\n')
def tab(a,b):
    seg=L[a-1:b]
    out=[]
    for i in range(len(seg)-1):
        m=re.match(r'^([\d.]+) ×10\^-(\d+)$',seg[i+1].strip())
        if m: out.append((seg[i].strip(), float(m.group(1))*10**-int(m.group(2))))
    return out
for name,(a,b) in {'T1':(426,566),'T2':(573,663),'T10':(1994,2102)}.items():
    t=tab(a,b); ps=[p for _,p in t]
    print(name,len(t),'max p',max(ps),'n<0.01/122',sum(p<0.01/122 for p in ps),'n<0.05/122',sum(p<0.05/122 for p in ps))
    print([n for n,_ in t])
E
python -c "import statsmodels" 2>&1; pip list 2>/dev/null | grep -i -E "numpy|mpmath|sympy"
```

```
T1 69 max p 0.00039 n<0.01/122 62 n<0.05/122 69
['area_25', 'PCC', 'RSC', 'area_10', 'STGr', 'STGc', 'area_32', 'area_24', 'paraHipp', 'ERh', 'area_8A', 'area_8B', 'rostral_dlPFC', 'rostral_vlPFC', 'SI', 'MT', 'V4', 'V3', 'TGa', 'TEO', 'gyral_TE', 'TE_in_STSv', 'STSf', 'STSd', 'lat_belt', 'med_belt', 'RTp', 'core', 'area_14', 'areas_11/13', 'OLF', 'cl_OFC', 'caudal_vlPFC', 'V6', 'V6A', 'area_5', 'vm_IPS', 'lat_IPS', 'MST', 'area_7_in_IPL', 'area_7m', 'Cl', 'Pir', 'HF', 'stAmy', 'mAmy', 'pdAmy', 'VStr', 'Pd', 'BR', 'opt', 'VTHy', 'DTHy', 'ZI-H', 'Rt', 'A+', 'MLThal', 'SpThal', 'DLG', 'MG', 'Pi', 'Hb', 'OC+', 'R+', 'Pn+', 'DCb', 'VCC', 'MedRaphe', 'PreCbMed']
T2 44 max p 0.00039 n<0.01/122 36 n<0.05/122 44
['STGr', 'STGc', 'ERh', 'PRh', 'area_8B', 'Ri', 'SI', 'PM', 'MT', 'V1', 'gyral_TE', 'TE_in_STSv', 'STSd', 'lat_belt', 'med_belt', 'area_14', 'area_12m/o', 'V6', 'En', 'Pir', 'stAmy', 'mAmy', 'DStr', 'opt', 'POR', 'MTHy', 'VTHy', 'DTHy', 'VPHy', 'A+', 'MD', 'MLThal', 'CbThal', 'LD', 'Pul', 'DLG', 'PrT', 'Co', 'raphe_Mid', 'wmCB', 'Fl-PFl', 'ICbCx', 'LCbCx', 'MedMC']
T10 53 max p 0.00039 n<0.01/122 46 n<0.05/122 53
['area_25', 'PCC', 'RSC', 'area_10', 'STGr', 'STGc', 'ERh', 'PRh', 'area_8B', 'rostral_dlPFC', 'SII', 'V3', 'TGa', 'TGg/TGd', 'gyral_TE', 'TE_in_STSv', 'STSf', 'STSd', 'lat_belt', 'med_belt', 'RTp', 'core', 'area_14', 'areas_11/13', 'OLF', 'cl_OFC', 'V6', 'MST', 'area_7m', 'Cl', 'HF', 'mAmy', 'DStr', 'ST', 'SDBR', 'opt', 'POR', 'MTHy', 'DTHy', 'Rt', 'A+', 'ILThal', 'MLThal', 'PNThal', 'LD', 'Hb', 'OC+', 'DA_Mid', 'Pn+', 'Fl-PFl', 'ICbCx', 'LCbCx', 'VCC']
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import statsmodels
ModuleNotFoundError: No module named 'statsmodels'
```

**Agent calls Write**

```json
{
 "file_path": "claims/001785/10.1038-s41593-026-02301-4.yaml",
 "content": "# Claims for Fujimoto, Fujimoto, Elorette et al. (2026), Nature Neuroscience,\n# doi:10.1038/s41593-026-02301-4, on dandiset 001785.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol as stated in docs/protocol.md.\n#\n# Text read: the version of record as served by Europe PMC (PMC13337501), with main text,\n# Methods, figure legends and Extended Data legends, and the Supplementary Information PDF\n# (41593_2026_2301_MOESM1_ESM.pdf; Supplementary Methods 1 to 7 and Supplementary Tables 1 to\n# 11), extracted as text into paper/10.1038-s41593-026-02301-4.txt. The PDF of the article was\n# not available; no figure had to be read from it.\n#\n# Code read: the paper's Code availability points to DANDI:001773 version 0.260416.1939\n# (doi:10.48324/dandi.001773/0.260416.1939). It holds a README, 17 MATLAB scripts under code/\n# (one per figure; two pairs are duplicates under two names) and the paper's source-data\n# spreadsheets under source_data/. The scripts start from the spreadsheets (voxel-wise FA,\n# voxel-wise normalized seed FC, per-field CC1 and DAPI counts, per-axon g-ratios, behavior\n# bins), not from images; the FC matrix script starts from AFNI residual files. Read:\n# Fig2A_dbs_FA_wholetract_analysisscript_a.m, Fig2B_dbs_FA_CB_part_analysisscript_a.m,\n# Fig3CandE5_dbs_IF_CC1_MCC_CB_analysisscript_a.m, FigE6A_..., FigE6B_...,\n# Fig3F_dbs_EMgratio_analysisscript_a.m, Fig4andE10C_Fujimoto_NatNeuro_2026_FCmatrix.m,\n# Fig5BCandE9_dbs_FC_25norm_mkNT_analysisscript_a.m, Fig6A_..., Fig6B_..., Fig6C_...,\n# Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m, FigE1_dbs_behavior_analysisscript_a.m.\n#\n# Data the paper used (Methods, Subjects; Acquisition and processing of neuroimaging data):\n# - Monkeys N and T (male rhesus, 7 to 9 years), SCC-DBS lead implanted unilaterally (left in\n#   N, right in T), 4 weeks of recovery, then 6 weeks of chronic stimulation (130 Hz, 90 us,\n#   5 mA) through the contact nearest the confluence of CB, UF and FM.\n# - Monkey D, nonstimulation control: lead implanted on the left, no stimulation.\n# - Monkeys B, W and H, nonsurgical controls: rs-fMRI and T1w only, two sessions 6 to 7 weeks\n#   apart.\n# - MRI (3 T Siemens Skyra, isoflurane anesthesia), one session before implantation and one\n#   after the 6 weeks (lead removed about 20 min before): T1w (0.5 mm); DWI (b = 1000, 72\n#   directions, 1.5 mm, six runs, three AP and three PA); rs-fMRI (MION contrast, 1.6 mm, TR\n#   2.12 s, six runs of 300 volumes).\n# - Histology after the post scan: CC1 and DAPI immunofluorescence, four coronal sections per\n#   animal and region, 7 fields per hemisphere per section (MCC-CB, dACC-CB) or 5 (UF and FM\n#   overlap); electron microscopy of the MCC-CB in N and T, about 175 axons per hemisphere per\n#   animal, four measurements per axon.\n# - Home-cage behavior videos, 10 min, 60 bins of 10 s binarized for movement and foraging,\n#   before implantation and after 6 weeks of stimulation (N, T, D).\n# The archive's description of 001785 lists DWI (FA) and T1w for N, T, D; EPI for N, T, D and\n# B, W, H; CC1 immunofluorescence (MCC-CB, dACC-CB, UF-FM overlap for N and T, MCC-CB for D);\n# and EM for N and T. It does not list behavior.\n#\n# Outside data (Reader, step 4):\n# - DANDI:001773 version 0.260416.1939, the paper's own deposit: source-data spreadsheets and\n#   the scripts. The behavior bins are there (source_data/dbs_behavior_data_a.xlsx), so the\n#   behavior claims are data elsewhere. The other spreadsheets hold the paper's per-voxel,\n#   per-field and per-axon values; an author may use them to link the dataset to the paper's\n#   values (kind link), not to replace the dataset's measurements.\n# - Atlases in NMT v2.0 space (Methods, EPI data analysis and FA analysis): the NMT v2.0\n#   template, the D99 atlas, CHARM and SARM, distributed with AFNI and listed on PRIME-DRE\n#   (https://prime-re.github.io/). The paper gives no version beyond NMT 2.0. Claims whose ROIs\n#   or CB subregions come from these atlases are data with_inputs.\n#\n# Shared methods, from the Methods, the Supplementary Methods and the code. Each criterion\n# below refers to these blocks by name.\n#\n# [FA] FA from DTIFIT after the preprocessing of Supplementary Methods 1 (MP-PCA denoising,\n#   AP/PA merge, susceptibility, eddy and bias correction, b0 brain extraction, linear\n#   alignment to the session T1w). Each session's FA map registered to its own T1w with\n#   epi_reg; post-DBS T1w registered nonlinearly to pre-DBS T1w with ANTs; post FA brought to\n#   pre-DBS T1w space. FA taken voxel-wise (1.5 mm) inside each tract mask, each hemisphere\n#   apart; voxels on the DBS lead track excluded. Tract masks (Methods, Identification of white\n#   matter tracts; Supplementary Methods 2): ProbtrackX in native diffusion space (3200 steps,\n#   10000 samples, step 0.1 mm, curvature 0.2) from seed, waypoint and exclusion masks drawn by\n#   hand; each tract log-transformed, divided by its maximum and thresholded at 0.7 to 1. The\n#   seed masks were drawn by hand and are not given; a mask drawn by an agent would be an\n#   agent's choice, so these claims need the paper's masks (or tracts) from the dataset. The\n#   reported voxel counts check them. Open, how lead-track voxels were found; readings (a)\n#   voxels on the CT-defined lead location aligned to pre-DBS T1w (Methods, SCC-DBS\n#   implantation surgery), (b) voxels on the visible track in the post-DBS images.\n#   \"Stimulated side\" is the left hemisphere for N and D and the right for T; n pools the two\n#   animals' voxels.\n# [FA-ANOVA] As the code does it (anovan, MATLAB default type III sums of squares): for N and T,\n#   FA on monkey (main effect only), PrePost, side and tract (or CB subregion), with the\n#   PrePost x side, PrePost x tract, side x tract and PrePost x side x tract terms; the\n#   resulting error df match the paper's (3187, 1357). Post hoc, multcompare with\n#   Tukey-Kramer (MATLAB's default) over all pairs of the PrePost x side x tract cells, on\n#   population marginal means; the pre-post pair of each side and tract is read. For monkey D,\n#   the full three-way factorial without a monkey term (error df 1238 and 492, as reported).\n# [CB-PARTS] CB subregions from D99 (Methods, FA analysis): SCC part next to areas 25 and 32,\n#   dACC part next to area 24, MCC part next to area 24', PCC part next to area 23. Open, how\n#   \"adjacent\" assigns a CB voxel; readings (a) the D99 label nearest to the voxel, (b) the\n#   anterior-posterior extent of each area applied to the CB mask. The voxel counts in the\n#   Fig. 2b legend check the reading.\n# [IF] Per field (x20, nonoverlapping), CC1-positive and DAPI-positive counts and their ratio in\n#   percent. Counts were made in FIJI with section-specific intensity thresholds, checked\n#   against manual counts; the thresholds are not reported. If the dataset holds counts they\n#   are used; if it holds images only, the threshold is open, readings (a) an automatic\n#   per-section, per-channel threshold (FIJI default IsoData), (b) Otsu. For N and T, anovan\n#   with the full model monkey x side (the code; error df 108 or 76 as reported), the side main\n#   effect read. For D, a two-sided paired t-test of sham against control fields, pairs as\n#   rows of the paper's sheet (field order within section); open if the dataset does not give\n#   field order, readings (a) pair by section and field index, (b) pair by section and sorted\n#   field value is not a reading the paper allows, so only (a).\n# [EM] Per axon, longest and shortest axon diameters and myelin widths; g-ratio = mean axon\n#   diameter / (mean axon diameter + 2 x mean myelin width); axons with aspect ratio above 2\n#   excluded, regions with fixation artifacts or noncompaction excluded. anovan full model\n#   monkey x side (the code; error df 696), the side main effect read.\n# [EPI] Custom AFNI pipeline (Methods, EPI data analysis): slice-timing correction, first three\n#   TRs removed, motion correction, alignment to the session T1w and warp to NMT v2.0, 3 mm\n#   FWHM blur, percent signal change, regression of motion derivatives and CSF and white\n#   matter signals (the code reads errts.<subject>.fanaticor files, AFNI's fast ANATICOR).\n# [MATRIX] 3dNetCorr Fisher z between ROIs of CHARM and SARM level 4 (122 ROIs in the Fig. 4b\n#   legend). The Methods compute one matrix per run, Fisher z, averaged within condition; the\n#   code runs 3dNetCorr once per session on the residual file (all runs together), kept as a\n#   variant. Difference post minus pre per subject, then the mean over subjects of the group\n#   (N and T; B, W and H; D alone). Cortical ROIs are the CHARM ones (54, the first 54 in the\n#   code's order), subcortical the SARM ones. Per ROI, the post minus pre changes from that ROI\n#   to the 121 others (group mean). Test (code and legend, \"changes ... from zero\") is a\n#   Wilcoxon rank-sum test of these 121 values against 121 zeros; the Methods' wording \"between\n#   pre and post conditions\" also allows a rank-sum of the ROI's 121 pre values against its 121\n#   post values, a second reading. Threshold, open between the Methods and legend (\"P < 0.01\n#   with Bonferroni correction\", read as p < 0.01/122) and the code (p < 0.05/122); the ROIs of\n#   Supplementary Tables 1, 2 and 10 all have p below 0.05/122 and include seven, eight and\n#   seven ROIs above 0.01/122, so the tables follow the code. Circular plots draw pairs with a\n#   change beyond 0.1 (legend); the code uses 0.15, a variant.\n# [SEED] Seed is D99 area 25 in the stimulated (for D, implanted) hemisphere; for the\n#   nonsurgical controls the right area 25 (Fig. 5a legend). Fisher z of the Pearson\n#   correlation between the seed's mean time series and every voxel (3dTcorr1D); each voxel's\n#   z divided by the session's maximum z. Open, two details. Runs, readings (a) per run then\n#   averaged, as the Methods do for the matrix, (b) the session's residual series. Maximum,\n#   readings (a) over all brain voxels, the seed included, (b) over voxels outside the seed.\n#   Target ROIs from Supplementary Methods 4, in the order and with the voxel counts of\n#   Supplementary Table 8 (1 PCC, 2 vmFC, 3 STG, 4 anterior-dorsal insula, 5 dACC, 6 DLPFC,\n#   7 PPC, 8 area 25 of the other hemisphere, 9 area 32, 10 MCC, 11 HIP, 12 AMY, 13 sensory\n#   cortex, 14 motor cortex, 15 SMA, 16 visual cortex V1, 17 MT), each taken in the stimulated\n#   and in the control hemisphere. Each monkey contributes the voxels of the ROI in the\n#   hemisphere concerned, which is why the stimulated and control n are equal. Open, the voxel\n#   grid; readings 1.5 mm (the atlas file name in the matrix code) and 1.6 mm (EPI); the\n#   Supplementary Table 8 counts decide.\n# [SEED-ANOVA] As the code does it: normalized z on monkey (main effect), PrePost, side and\n#   ROI with the same terms as [FA-ANOVA] (error df 20279, as reported); multcompare\n#   Tukey-Kramer over the PrePost x side x ROI cells. Networks (code; Methods, EPI data\n#   analysis; Extended Data Fig. 9a): DMN = PCC, vmFC, STG; SAN = anterior-dorsal insula,\n#   dACC; CEN = DLPFC, PPC; LIM = PCC, dACC, area 25, area 32, MCC, HIP, AMY; SMN = sensory\n#   cortex, motor cortex, SMA; VIS = V1, MT. Voxels of shared ROIs are counted in each network.\n#   The Methods' LIM list leaves out area 25; the code, Extended Data Fig. 9a (\"SCC, dACC and\n#   PCC were counted as hubs for the LIM\") and the reported n (821 = 249 + 162 + 18 + 48 + 101\n#   + 132 + 111) include it, so it is included. The same model on network in place of ROI\n#   (error df 21967). For D, the full three-way factorial without monkey (error df 10106 and\n#   10972).\n#\n# Discrepancies in the text, recorded for the author: Fig. 6a prints \"F 1,1238 = 6.02,\n# P = 0.0025\" for the PrePost x side x tract interaction; F(1, 1238) = 6.02 gives P near 0.014\n# and F(2, 1238) gives 0.0025, and the three-way term has 2 df, so the 1 is taken as a misprint.\n# Supplementary Tables 3, 4 and 11 (effect sizes) hold identical values, so they are not used.\n# Extended Data Fig. 10d calls the post scan of D \"10 weeks after implantation\"; the Methods say\n# 6 weeks of implantation without stimulation (after the 4-week recovery, 10 weeks in all).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001785\"\npaper: doi:10.1038/s41593-026-02301-4\nclaims:\n- id: ed1-behavior-increase\n  statement: In monkeys N and T, time spent moving and foraging in the home cage increased after 6\n    weeks of SCC-DBS (one-way ANOVA, movement F(1,236) = 34.61, foraging F(1,236) = 17.35).\n  source: Results, SCC-DBS induces selective macroscale remodeling in the CB, paragraph 2; Extended\n    Data Fig. 1\n  quote: Time spent moving and foraging both increased after SCC-DBS, with concordant effects\n    observed across subjects\n  statistics:\n  - about: movement, pre against post\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,236) = 34.61\n    p: 1.37e-08\n    n: 120 bins pre and 120 post (60 per animal per session)\n  - about: foraging, pre against post\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,236) = 17.35\n    p: 4.37e-05\n    n: 120 bins pre and 120 post\n  data: elsewhere\n  where: DANDI:001773 version 0.260416.1939, source_data/dbs_behavior_data_a.xlsx\n  criterion: Bins of 10 s, 60 per 10-min video, 1 when movement (or foraging) occurs (Methods,\n    Behavior analysis). anovan with the full model monkey x stim on the bins of N and T, as in\n    FigE1_dbs_behavior_analysisscript_a.m (error df 236). Reproduced when the stim effect has p <\n    0.05 with the post proportion higher, for both movement and foraging, and each animal's post\n    proportion exceeds its pre proportion; partially reproduced when this holds for one of the two\n    behaviors.\n- id: ed1-sham-no-behavior-change\n  statement: The nonstimulation control animal (monkey D) showed no change in movement or foraging.\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain networks,\n    paragraph 2; Extended Data Fig. 1\n  quote: First, there was no change in the amount of movement or foraging in naturalistic behavior\n  data: elsewhere\n  where: DANDI:001773 version 0.260416.1939, source_data/dbs_behavior_data_a.xlsx\n  criterion: A claim of absence for which the paper reports no test; the test it used for N and T\n    (one-way ANOVA of the binarized bins, pre against post, p < 0.05) is applied to the 60 pre and\n    60 post bins of D. Reproduced when neither movement nor foraging differs at p < 0.05; not\n    reproduced when either does. The pre and post proportions are reported.\n- id: fig2a-cb-fa-increase\n  statement: After 6 weeks of SCC-DBS, FA increased in the cingulum bundle of the stimulated\n    hemisphere (PrePost x side interaction F(1,3187) = 4.64, p = 0.0312; Tukey-Kramer pre against\n    post in the stimulated CB, p = 0.022).\n  source: Results, SCC-DBS induces selective macroscale remodeling in the CB, paragraph 3; Fig. 2a\n  quote: We found there was a selective increase in FA in the CB in the stimulated hemisphere,\n    particularly the mid-cingulate portion, after 6 weeks of SCC-DBS\n  statistics:\n  - about: PrePost x side interaction\n    test: three-way ANOVA (DBS x side x tract, monkey as a fixed effect)\n    statistic: F(1,3187) = 4.64, partial eta squared 0.0015\n    p: 0.0312\n  - about: stimulated CB, pre against post\n    test: Tukey-Kramer post hoc\n    p: 0.022\n    corrected: Tukey-Kramer\n    n: 380 voxels pre and 380 post, pooled over monkeys N and T\n  expected:\n  - quantity: stimulated-side CB voxels (N and T pooled)\n    value: 380\n    tolerance: 38\n  - quantity: control-side CB voxels\n    value: 363\n    tolerance: 36.3\n  - quantity: stimulated-side UF voxels\n    value: 252\n    tolerance: 25.2\n  - quantity: control-side UF voxels\n    value: 367\n    tolerance: 36.7\n  - quantity: stimulated-side FM voxels\n    value: 105\n    tolerance: 10.5\n  - quantity: control-side FM voxels\n    value: 133\n    tolerance: 13.3\n  criterion: FA as in [FA] of the header, model and post hoc as in [FA-ANOVA]\n    (Fig2A_dbs_FA_wholetract_analysisscript_a.m). Reproduced when the PrePost x side interaction\n    has p < 0.05 and the Tukey-Kramer pre-post comparison in the stimulated CB has p < 0.05 with\n    post FA higher, under one reading of the lead-track exclusion. The voxel counts are checked\n    against the expected values as a check on the masks.\n- id: fig2a-no-other-tract-change\n  statement: FA did not change consistently in the stimulated UF or FM, nor in any of the three\n    tracts in the control hemisphere.\n  source: Results, SCC-DBS induces selective macroscale remodeling in the CB, paragraph 3; Fig. 2a\n    bottom; Extended Data Figs. 2 to 4\n  quote: No consistent changes were apparent in either the stimulated UF or the FM ... or in the same\n    tracts within the control hemisphere\n  depends_on:\n  - fig2a-cb-fa-increase\n  criterion: A claim of absence, judged on the paper's test, the Tukey-Kramer post hoc of\n    [FA-ANOVA] at p < 0.05. Reproduced when none of the five pre-post comparisons (stimulated UF,\n    stimulated FM, control CB, control UF, control FM) has p < 0.05; not reproduced when any does.\n    The mean change and p of each are reported.\n- id: ed2-cb-both-monkeys\n  statement: Both stimulated monkeys showed an FA change in the same direction in the stimulated\n    CB.\n  source: Results, SCC-DBS induces selective macroscale remodeling in the CB, paragraph 3; Extended\n    Data Fig. 2\n  quote: Importantly, both monkeys exhibited changes in the same direction\n  depends_on:\n  - fig2a-cb-fa-increase\n  criterion: The paper shows this with per-monkey maps and symbols, without a test. Per monkey, the\n    mean over the stimulated CB voxels of post FA minus the mean of pre FA ([FA]). Reproduced when\n    it is positive in both N and T.\n- id: fig2b-mcc-cb-increase\n  statement: Of four CB subregions, only the mid-cingulate part on the stimulated side showed an FA\n    increase, in both animals (PrePost x side interaction F(1,1357) = 5.42, p = 0.020; Tukey-Kramer\n    for the stimulated MCC-CB, p = 0.0017).\n  source: Results, SCC-DBS induces selective macroscale remodeling in the CB, paragraph 4; Fig. 2b\n  quote: Comparing the FA values before and after 6 weeks of DBS in four CB subregions revealed that\n    only the mid-cingulate region on the stimulated side showed an increase in FA in both animals\n  statistics:\n  - about: PrePost x side interaction\n    test: three-way ANOVA (DBS x side x subregion, monkey as a fixed effect)\n    statistic: F(1,1357) = 5.42, partial eta squared 0.0040\n    p: 0.02\n  - about: stimulated MCC-CB, pre against post\n    test: Tukey-Kramer post hoc\n    p: 0.0017\n    corrected: Tukey-Kramer\n    n: 55 voxels pre and 55 post, pooled over N and T\n  expected:\n  - quantity: stimulated-side MCC-CB voxels\n    value: 55\n    tolerance: 5.5\n  - quantity: stimulated-side SCC, dACC and PCC CB voxels\n    value: 271\n    tolerance: 27.1\n  - quantity: control-side CB subregion voxels (SCC, dACC, MCC, PCC)\n    value: 361\n    tolerance: 36.1\n  data: with_inputs\n  depends_on:\n  - fig2a-cb-fa-increase\n  criterion: FA as in [FA], subregions as in [CB-PARTS], model and post hoc as in [FA-ANOVA]\n    (Fig2B_dbs_FA_CB_part_analysisscript_a.m). Reproduced, under one reading of [CB-PARTS] and of\n    the lead-track exclusion, when the PrePost x side interaction has p < 0.05, the stimulated\n    MCC-CB pre-post comparison has Tukey-Kramer p < 0.05 with post higher, none of the other seven\n    pre-post comparisons shows a significant increase, and each monkey's mean MCC-CB FA rises on\n    the stimulated side. Partially reproduced when the stimulated MCC-CB increase holds but another\n    subregion also increases significantly or one monkey does not rise.\n- id: fig3c-cc1-dapi-ratio-mcc\n  statement: The proportion of CC1-positive cells among DAPI-stained cells was higher in the MCC-CB\n    of the stimulated hemisphere than in the control hemisphere, in both animals (F(1,108) = 9, p =\n    0.0034).\n  source: Results, SCC-DBS induces increased myelinating oligodendrocytes and the degree of\n    myelination, paragraph 1; Fig. 3b,c\n  quote: The proportion of CC1 positive cells in the whole DAPI stained population was higher in the\n    mid-cingulate portion of the CB on the stimulated side compared to the control side in both\n    animals\n  statistics:\n  - about: side main effect on the CC1/DAPI ratio\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,108) = 9, partial eta squared 0.077\n    p: 0.0034\n    n: 56 fields per hemisphere (7 fields x 4 sections x 2 monkeys)\n  expected:\n  - quantity: fields per hemisphere, N and T pooled\n    value: 56\n    tolerance: 0\n  criterion: Counts and test as in [IF], on the MCC-CB fields of N and T\n    (Fig3CandE5_dbs_IF_CC1_MCC_CB_analysisscript_a.m). The tolerance on the field count is 0 as it\n    is the design (7 fields x 4 sections x 2 animals). Reproduced when the side effect has p < 0.05\n    with the stimulated side higher and each animal's mean ratio is higher on the stimulated side.\n- id: ed5-cc1-count-dapi\n  statement: In the MCC-CB the number of CC1-positive cells was higher on the stimulated side\n    (F(1,108) = 6.22, p = 0.0142), while the number of DAPI-positive cells did not differ (F(1,108)\n    = 0.55, p = 0.4617).\n  source: Extended Data Fig. 5 legend\n  quote: The main effect of side for the number of CC1 positive cells was significant ... while no\n    significant difference was observed for the number of DAPI positive cells\n  statistics:\n  - about: CC1-positive count, side main effect\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,108) = 6.22, partial eta squared 0.054\n    p: 0.0142\n    n: 56 fields per hemisphere\n  - about: DAPI-positive count, side main effect\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,108) = 0.55, partial eta squared 0.0050\n    p: 0.4617\n    n: 56 fields per hemisphere\n  depends_on:\n  - fig3c-cc1-dapi-ratio-mcc\n  criterion: As in [IF]. Reproduced when the side effect on CC1 counts has p < 0.05 with the\n    stimulated side higher and the side effect on DAPI counts has p >= 0.05 (the paper's test for\n    the absence); partially reproduced when only one of the two holds.\n- id: ed6a-dacc-cb-no-change\n  statement: In the dACC portion of the CB, neither the CC1/DAPI ratio nor the CC1 or DAPI counts\n    differed between hemispheres (ratio F(1,108) = 2.93, p = 0.0899).\n  source: Results, SCC-DBS induces increased myelinating oligodendrocytes and the degree of\n    myelination, paragraph 1; Extended Data Fig. 6a\n  quote: No changes were observed in the anterior portion of CB, consistent with the lack of FA\n    alterations there\n  statistics:\n  - about: CC1/DAPI ratio\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,108) = 2.93\n    p: 0.0899\n    n: 56 fields per hemisphere\n  - about: CC1-positive count\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,108) = 0\n    p: 0.9974\n  - about: DAPI-positive count\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,108) = 1.22\n    p: 0.2718\n  criterion: A claim of absence, judged on the paper's test, [IF] on the dACC-CB fields of N and T\n    (FigE6A_dbs_IF_CC1_dACC_CB_analysisscript_a.m) at p < 0.05. Reproduced when the side effect is\n    not significant for the ratio, the CC1 count or the DAPI count; not reproduced when any is.\n    Effect sizes are reported.\n- id: ed6b-uf-fm-no-change\n  statement: In the region where the UF and FM overlap, oligodendrocyte measures did not differ\n    between hemispheres (CC1/DAPI ratio F(1,76) = 1.45, p = 0.2319).\n  source: Results, SCC-DBS induces increased myelinating oligodendrocytes and the degree of\n    myelination, paragraph 1; Extended Data Fig. 6b\n  quote: Similarly, the region where the FM and UF overlap showed no oligodendrocyte changes\n  statistics:\n  - about: CC1/DAPI ratio\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,76) = 1.45\n    p: 0.2319\n    n: 40 fields per hemisphere (5 fields x 4 sections x 2 monkeys)\n  - about: CC1-positive count\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,76) = 0.79\n    p: 0.3778\n  - about: DAPI-positive count\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,76) = 0\n    p: 0.9611\n  criterion: A claim of absence, judged on the paper's test, [IF] on the UF-FM overlap fields of N\n    and T (FigE6B_dbs_IF_CC1_UF_FMoverlap_analysisscript_a.m) at p < 0.05. Reproduced when the side\n    effect is not significant for the ratio, the CC1 count or the DAPI count; not reproduced when\n    any is.\n- id: fig3f-gratio-decrease\n  statement: The g-ratio of myelinated axons in the MCC-CB was lower in the stimulated than in the\n    control hemisphere in both animals, meaning thicker myelin (F(1,696) = 58.98, p = 5.42e-14).\n  source: Results, SCC-DBS induces increased myelinating oligodendrocytes and the degree of\n    myelination, paragraph 2; Fig. 3d-f\n  quote: the MCC-CB g -ratio was decreased compared to the control hemisphere in both animals\n  statistics:\n  - about: side main effect on the g-ratio\n    test: one-way ANOVA with monkey as a fixed effect\n    statistic: F(1,696) = 58.98, partial eta squared 0.078\n    p: 5.42e-14\n    n: 350 axons per hemisphere, pooled over N and T\n  expected:\n  - quantity: axons per hemisphere, N and T pooled\n    value: 350\n    tolerance: 35\n  criterion: Measures, exclusions and test as in [EM] (Fig3F_dbs_EMgratio_analysisscript_a.m).\n    Reproduced when the side effect has p < 0.05 with the stimulated side lower and each animal's\n    mean g-ratio is lower on the stimulated side.\n- id: fig4a-cortical-decrease-subcortical-increase\n  statement: After SCC-DBS, cortico-cortical functional connectivity was broadly reduced and\n    subcortico-subcortical connectivity increased.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 1; Fig.\n    4a,b\n  quote: Broadly, we observed a reduction in cortico–cortical functional connectivity and a\n    concurrent increase in subcortico–subcortical functional connectivity\n  data: with_inputs\n  criterion: Matrices as in [EPI] and [MATRIX], mean post minus pre over N and T. The paper shows\n    this in the difference matrix without a test. Readings for the summary, (a) the mean and (b)\n    the median of the change over all cortico-cortical pairs and over all subcortico-subcortical\n    pairs. Reproduced when, under one reading and one run reading of [MATRIX], the\n    cortico-cortical value is below 0 and the subcortico-subcortical value above 0.\n- id: fig4b-dbs-widespread-roi-changes\n  statement: SCC-DBS induced widespread changes in functional connectivity, with many CHARM and SARM\n    ROIs showing a significant change from zero in their connectivity to the rest of the brain\n    (Supplementary Table 1 lists 69 ROIs).\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 1; Fig.\n    4b; Supplementary Table 1\n  quote: In contrast to the localized structural alterations observed in white matter, SCC-DBS\n    induced widespread functional changes\n  statistics:\n  - test: rank-sum test per ROI\n    p: 0.01\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 122 ROIs, changes averaged over monkeys N and T\n  expected:\n  - quantity: ROIs with a significant change, threshold p < 0.05/122 (code; the ROIs of\n      Supplementary Table 1)\n    value: 69\n    tolerance: 6.9\n  - quantity: ROIs with a significant change, threshold p < 0.01/122 (Methods and legend; ROIs of\n      Supplementary Table 1 under it)\n    value: 62\n    tolerance: 6.2\n  data: with_inputs\n  criterion: Per-ROI test as in [MATRIX] for the DBS group. Readings, the test (rank-sum against\n    zeros, or pre against post values) and the threshold (0.01/122 or 0.05/122), each paired with\n    its own expected count. Reproduced when the count is within tolerance under one reading and\n    the significant ROIs overlap those of Supplementary Table 1 by at least 80%; partially\n    reproduced when the count is within tolerance but the overlap is lower. The signs of the\n    significant ROIs (cortical against subcortical) are reported.\n- id: fig4c-cortical-network-reduction\n  statement: Sorted by cortical network membership, connectivity within and across cortical\n    networks was reduced after SCC-DBS.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 1; Fig.\n    4c left\n  quote: When the functional connectivity was sorted based on cortical networks membership, it was\n    clear that connectivity within and across networks was reduced\n  data: with_inputs\n  depends_on:\n  - fig4a-cortical-decrease-subcortical-increase\n  criterion: Circular plot of Fig. 4c, pairs of the 54 cortical ROIs with a group-mean change\n    beyond 0.1 in absolute value (legend; the code's 0.15 is a variant). The network assignment of\n    the ROIs is not given, so the claim is judged over all cortical pairs. Reproduced when pairs\n    with a change below -0.1 outnumber pairs with a change above 0.1.\n- id: fig4-control-no-systematic-pattern\n  statement: In the nonsurgical control group, scans 6 to 7 weeks apart showed no systematic pattern\n    of functional connectivity change like that after SCC-DBS.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 2; Fig.\n    4a-c bottom and right; Supplementary Table 2\n  quote: In these control animals, a comparison conducted between scans acquired 6–7 weeks apart did\n    not reveal a systematic pattern of functional changes\n  expected:\n  - quantity: ROIs with a significant change in the control group, threshold p < 0.05/122 (ROIs of\n      Supplementary Table 2)\n    value: 44\n    tolerance: 4.4\n  data: with_inputs\n  depends_on:\n  - fig4a-cortical-decrease-subcortical-increase\n  criterion: The paper judges this by eye; its own Supplementary Table 2 lists 44 ROIs significant\n    by the per-ROI test, so a systematic pattern is read as the DBS group's pattern. Matrices as\n    in [MATRIX], mean over B, W and H. Reproduced when the control group does not show both a\n    cortico-cortical decrease and a subcortico-subcortical increase (as in\n    fig4a-cortical-decrease-subcortical-increase, same readings), and in the circular plot pairs\n    beyond 0.1 are fewer than in the DBS group. The count of significant ROIs is compared with the\n    expected value and reported.\n- id: fig5a-pre-scc-connectivity\n  statement: Before stimulation, the SCC had positive connectivity with vmFC, dACC, PCC, STG,\n    hippocampus, amygdala and DLPFC, and negative connectivity with the insula and somatosensory\n    cortex.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 3; Fig.\n    5a top row; Extended Data Fig. 7 top row\n  quote: Before stimulation, the SCC showed positive connectivity to the ventromedial frontal cortex\n    (vmFC), dorsal anterior cingulate cortex (dACC), posterior cingulate cortex (PCC), superior\n    temporal gyrus (STG), hippocampus (HIP), amygdala (AMY) and dorsolateral prefrontal cortex\n    (DLPFC), as well as negative connectivity to the insula and somatosensory cortex\n  data: with_inputs\n  criterion: Seed maps as in [EPI] and [SEED], pre-DBS sessions of N and T. The paper shows maps\n    without an ROI test. Per target ROI, the mean normalized z over its voxels pooled across the\n    two animals. Readings, ROIs (a) in the stimulated hemisphere, (b) in both hemispheres pooled.\n    Reproduced when, under one reading, the seven ROIs named are above 0 and the anterior-dorsal\n    insula and sensory cortex below 0; partially reproduced when at least seven of the nine signs\n    hold.\n- id: fig5b-scc-decreases\n  statement: After SCC-DBS, connectivity of the stimulated SCC fell with PCC, vmFC, STG,\n    hippocampus, amygdala, DLPFC and dACC (PrePost x side interaction F(1,20279) = 186.48, p =\n    2.87e-42; Tukey-Kramer p < 0.001 in the stimulated hemisphere).\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 4; Fig.\n    5b; Extended Data Fig. 9; Supplementary Table 9\n  quote: Following 6 weeks of SCC-DBS, there was a marked reduction in functional connectivity\n    between the SCC and the PCC as well as the vmFC. Reductions were also apparent between the SCC\n    and HIP, AMY and DLPFC\n  statistics:\n  - about: PrePost x side interaction\n    test: three-way ANOVA (DBS x side x target ROI, monkey as a fixed effect)\n    statistic: F(1,20279) = 186.48, partial eta squared 0.0091\n    p: 2.87e-42\n  - about: stimulated-side PCC, pre against post\n    test: Tukey-Kramer post hoc\n    p: 8.22e-12\n    corrected: Tukey-Kramer\n    n: 249 voxels pre and 249 post\n  - about: stimulated-side vmFC\n    test: Tukey-Kramer post hoc\n    p: 1.0e-300\n    p_relation: \"<\"\n    corrected: Tukey-Kramer\n    n: 109 voxels\n  - about: stimulated-side dACC\n    test: Tukey-Kramer post hoc\n    p: 0.000475\n    corrected: Tukey-Kramer\n    n: 162 voxels\n  - about: stimulated-side HIP\n    test: Tukey-Kramer post hoc\n    p: 1.19e-05\n    corrected: Tukey-Kramer\n    n: 132 voxels\n  - about: stimulated-side AMY\n    test: Tukey-Kramer post hoc\n    p: 7.7e-06\n    corrected: Tukey-Kramer\n    n: 111 voxels\n  - about: stimulated-side STG and DLPFC\n    test: Tukey-Kramer post hoc (printed as 0 in Supplementary Table 9)\n    p: 0\n    corrected: Tukey-Kramer\n    n: 499 and 766 voxels\n  expected:\n  - quantity: PCC voxels per side (N and T pooled)\n    value: 249\n    tolerance: 24.9\n  - quantity: vmFC voxels per side\n    value: 109\n    tolerance: 10.9\n  - quantity: STG voxels per side\n    value: 499\n    tolerance: 49.9\n  - quantity: DLPFC voxels per side\n    value: 766\n    tolerance: 76.6\n  data: with_inputs\n  criterion: Seed maps as in [EPI] and [SEED], model and post hoc as in [SEED-ANOVA]\n    (Fig5BCandE9_dbs_FC_25norm_mkNT_analysisscript_a.m). Reproduced when, under one reading of\n    [SEED], the PrePost x side interaction has p < 0.05 and each of the seven ROIs in the\n    stimulated hemisphere has Tukey-Kramer p < 0.05 with post below pre; partially reproduced\n    when PCC and vmFC hold but fewer than all seven do. The voxel counts of all 17 ROIs are\n    compared with Supplementary Table 8.\n- id: fig5b-scc-increases\n  statement: Connectivity of the stimulated SCC with the anterior-dorsal insula and somatosensory\n    cortex increased after SCC-DBS (Tukey-Kramer p < 0.001).\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 5; Fig.\n    5a,b; Extended Data Fig. 9; Supplementary Table 9\n  quote: The insula and somatosensory cortex exhibited increases in functional connectivity with the\n    SCC following DBS\n  statistics:\n  - about: stimulated-side anterior-dorsal insula\n    test: Tukey-Kramer post hoc\n    p: 4.42e-08\n    corrected: Tukey-Kramer\n    n: 100 voxels\n  - about: stimulated-side sensory cortex\n    test: Tukey-Kramer post hoc (printed as 0 in Supplementary Table 9)\n    p: 0\n    corrected: Tukey-Kramer\n    n: 692 voxels\n  data: with_inputs\n  depends_on:\n  - fig5b-scc-decreases\n  criterion: As in fig5b-scc-decreases. Reproduced when both ROIs in the stimulated hemisphere have\n    Tukey-Kramer p < 0.05 with post above pre; partially reproduced when one does.\n- id: ed7-decreases-both-monkeys\n  statement: The reductions in connectivity from the SCC were consistent across both stimulated\n    monkeys.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 4;\n    Extended Data Figs. 7 and 8\n  quote: These reductions in functional connectivity from SCC were consistent across both monkeys\n  data: with_inputs\n  depends_on:\n  - fig5b-scc-decreases\n  criterion: Shown in per-monkey maps without a test. Per monkey, the mean over the ROI's voxels of\n    post minus pre normalized z ([SEED]), stimulated hemisphere, for the seven ROIs of\n    fig5b-scc-decreases. Reproduced when all seven are below 0 in both N and T; partially\n    reproduced when PCC and vmFC are below 0 in both but not all seven.\n- id: fig5-bilateral-changes\n  statement: Although stimulation was unilateral, connectivity changes with the stimulated SCC were\n    also present in the unstimulated control hemisphere.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 5; Fig.\n    5b,c; Extended Data Figs. 8 and 9; Supplementary Table 9\n  quote: Despite DBS being delivered unilaterally and white matter remodeling being confined to the\n    stimulated hemisphere ... functional connectivity changes were also apparent in the\n    unstimulated control hemisphere\n  statistics:\n  - about: control-side PCC\n    test: Tukey-Kramer post hoc\n    p: 4.03e-07\n    corrected: Tukey-Kramer\n  - about: control-side anterior-dorsal insula\n    test: Tukey-Kramer post hoc\n    p: 0.0293\n    corrected: Tukey-Kramer\n  - about: control-side vmFC, STG, dACC, DLPFC, area 25, area 32, sensory cortex\n    test: Tukey-Kramer post hoc (printed as 0 in Supplementary Table 9)\n    p: 0\n    corrected: Tukey-Kramer\n  data: with_inputs\n  depends_on:\n  - fig5b-scc-decreases\n  criterion: As in fig5b-scc-decreases, the control-hemisphere pre-post comparisons. Supplementary\n    Table 9 has 12 of 17 control-side ROIs at p < 0.05 (PCC, vmFC, STG, anterior-dorsal insula,\n    dACC, DLPFC, area 25, area 32, HIP, sensory cortex, MT). Reproduced when PCC, vmFC and dACC on\n    the control side each have Tukey-Kramer p < 0.05, the three DMN and SAN hubs of Fig. 5b with\n    the largest effects; partially reproduced when at least one does. The number of significant\n    control-side ROIs is reported against the table.\n- id: fig5a-control-group-no-reduction\n  statement: The reductions in SCC connectivity, and bilateral changes, were absent in the\n    nonsurgical control group over a comparable interval.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraphs 4 and\n    5; Fig. 5a bottom row; Extended Data Fig. 7 right column; Extended Data Fig. 8 bottom row\n  quote: Notably, such reductions in connectivity were absent in the nonsurgical control group\n  data: with_inputs\n  criterion: A claim of absence, judged on the paper's test, the thresholded seed map (voxel P <\n    0.01, cluster above 20 voxels, cluster-level corrected P < 0.01, two-sided; Fig. 5a legend) of\n    the change with the right area 25 in B, W and H ([SEED]). The paper does not say what voxel\n    test gives P; readings (a) a two-sample t-test per voxel of post against pre normalized z\n    across runs pooled over animals, (b) a one-sample t-test of the per-animal change; cluster\n    correction (a) AFNI 3dClustSim at the stated thresholds. Reproduced when no significant\n    negative cluster covers PCC or vmFC under the readings; not reproduced when one does. If the\n    readings disagree, the claim is blocked as methods_underspecified with both shown.\n- id: fig5c-network-decreases\n  statement: After SCC-DBS, connectivity between the stimulated SCC and the DMN, LIM and CEN hubs\n    decreased significantly (PrePost x side interaction F(1,21967) = 51.09, p = 9.10e-13;\n    Tukey-Kramer p < 0.001).\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 6; Fig.\n    5c\n  quote: After chronic stimulation, the DMN, LIM and CEN showed significantly decreased functional\n    connectivity with SCC\n  statistics:\n  - about: PrePost x side interaction\n    test: three-way ANOVA (DBS x side x network, monkey as a fixed effect)\n    statistic: F(1,21967) = 51.09, partial eta squared 0.0023\n    p: 9.1e-13\n  - about: stimulated-side DMN, LIM and CEN, pre against post\n    test: Tukey-Kramer post hoc\n    p: 1.0e-300\n    p_relation: \"<\"\n    corrected: Tukey-Kramer\n    n: DMN 857, LIM 821, CEN 1102 voxels per side\n  expected:\n  - quantity: DMN voxels per side\n    value: 857\n    tolerance: 85.7\n  - quantity: LIM voxels per side\n    value: 821\n    tolerance: 82.1\n  - quantity: CEN voxels per side\n    value: 1102\n    tolerance: 110.2\n  data: with_inputs\n  depends_on:\n  - fig5b-scc-decreases\n  criterion: Networks and model as in [SEED-ANOVA]. Reproduced when the interaction has p < 0.05\n    and the stimulated-side DMN, LIM and CEN each have Tukey-Kramer p < 0.05 with post below pre;\n    partially reproduced when one or two do. The Methods' LIM without area 25 is shown as a\n    variant.\n- id: fig5c-smn-increase\n  statement: Connectivity between the SCC and the sensorimotor network also changed after SCC-DBS,\n    as an increase, though the SMN has limited direct CB connections.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 6; Fig.\n    5c; Discussion, Effect of SCC-DBS on functional networks, paragraph 2\n  quote: There were, however, also changes in networks with limited direct CB connections, such as\n    the SMN\n  statistics:\n  - about: stimulated-side SMN\n    test: Tukey-Kramer post hoc\n    p: 2.83e-20\n    corrected: Tukey-Kramer\n    n: 1239 voxels per side\n  - about: control-side SMN\n    test: Tukey-Kramer post hoc\n    p: 1.21e-14\n    corrected: Tukey-Kramer\n  data: with_inputs\n  depends_on:\n  - fig5c-network-decreases\n  criterion: As in fig5c-network-decreases. The direction comes from the Discussion (\"an increase\n    in connectivity between the SCC and the SMN\"). Reproduced when the stimulated-side SMN has\n    Tukey-Kramer p < 0.05 with post above pre.\n- id: fig5c-vis-no-change\n  statement: Connectivity between the SCC and the visual network, or areas within it, did not\n    change.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 6; Fig.\n    5c; Extended Data Fig. 9; Supplementary Table 9\n  quote: In comparison, there was no change in relation to the VIS or areas within the VIS\n  statistics:\n  - about: stimulated-side visual cortex (V1)\n    test: Tukey-Kramer post hoc\n    p: 0.999989453\n    corrected: Tukey-Kramer\n  - about: stimulated-side MT\n    test: Tukey-Kramer post hoc\n    p: 0.998895555\n    corrected: Tukey-Kramer\n  data: with_inputs\n  depends_on:\n  - fig5c-network-decreases\n  criterion: A claim of absence, judged on the paper's test, the Tukey-Kramer post hoc of\n    [SEED-ANOVA] at p < 0.05, stimulated hemisphere. Reproduced when VIS (network model) and V1\n    and MT (ROI model) all have p >= 0.05; not reproduced when any is significant. The control\n    side is reported (Supplementary Table 9 has control-side MT significant, p = 7.85e-07).\n- id: fig5bc-san-no-net-change\n  statement: The salience network as a whole did not change its connectivity with the SCC, because\n    its nodes changed in opposite directions, the anterior-dorsal insula increasing and the dACC\n    decreasing.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 6; Fig.\n    5b,c; Extended Data Fig. 9\n  quote: Specifically, the anterior-dorsal insula exhibited increased connectivity with the SCC,\n    whereas the dACC showed decreased connectivity following 6 weeks of DBS\n  statistics:\n  - about: stimulated-side SAN network\n    test: Tukey-Kramer post hoc\n    p: 1.0\n    corrected: Tukey-Kramer\n    n: 262 voxels per side\n  - about: control-side SAN network\n    test: Tukey-Kramer post hoc\n    p: 6.2e-07\n    corrected: Tukey-Kramer\n  data: with_inputs\n  depends_on:\n  - fig5b-scc-decreases\n  - fig5c-network-decreases\n  criterion: Model as in [SEED-ANOVA]. Reproduced when the stimulated-side SAN pre-post comparison\n    has Tukey-Kramer p >= 0.05 (the paper's test for the absence), the stimulated-side\n    anterior-dorsal insula rises and the dACC falls, each at p < 0.05.\n- id: fig6a-sham-cb-fa-decrease\n  statement: In the nonstimulation control animal (lead implanted, no stimulation), FA decreased in\n    the CB of the implanted hemisphere (Tukey-Kramer p = 5.07e-09), with no change in the other\n    tracts.\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain networks,\n    paragraph 2; Fig. 6a; Extended Data Fig. 10a\n  quote: Second, in direct contrast to the SCC-DBS animals, we saw a significant decrease in FA in\n    the CB of the implanted hemisphere and no changes in any of our other target tracts\n  statistics:\n  - about: PrePost x side x tract interaction (printed as F 1,1238; the term has 2 df)\n    test: three-way ANOVA\n    statistic: F = 6.02, partial eta squared 0.0096\n    p: 0.0025\n  - about: sham-side CB, pre against post\n    test: Tukey-Kramer post hoc\n    p: 5.07e-09\n    corrected: Tukey-Kramer\n    n: 162 voxels pre and 162 post\n  expected:\n  - quantity: sham-side CB voxels (monkey D)\n    value: 162\n    tolerance: 16.2\n  - quantity: control-side CB voxels (monkey D)\n    value: 148\n    tolerance: 14.8\n  criterion: FA as in [FA], model as in [FA-ANOVA] for monkey D\n    (Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m). Reproduced when the sham-side CB pre-post\n    comparison has Tukey-Kramer p < 0.05 with post below pre, and none of the other five pre-post\n    comparisons has p < 0.05 (the paper's test for the absence); partially reproduced when the CB\n    decrease holds and another tract also changes.\n- id: fig6b-sham-dacc-cb-decrease\n  statement: In the nonstimulation control animal, the FA decrease lay in the dACC portion of the\n    CB, more anterior than and opposite to the increase after stimulation (PrePost x side F(1,492)\n    = 24.55, p = 9.97e-07; dACC-CB Tukey-Kramer p = 1.30e-08).\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain networks,\n    paragraph 2; Fig. 6b\n  quote: This decrease in FA is more anterior and the opposite direction of that observed in the\n    stimulation group, although diffuse reductions were seen across the CB\n  statistics:\n  - about: PrePost x side interaction\n    test: three-way ANOVA (DBS x side x subregion)\n    statistic: F(1,492) = 24.55, partial eta squared 0.048\n    p: 9.97e-07\n  - about: sham-side dACC-CB, pre against post\n    test: Tukey-Kramer post hoc\n    p: 1.3e-08\n    corrected: Tukey-Kramer\n    n: 58 voxels pre and 58 post\n  data: with_inputs\n  depends_on:\n  - fig6a-sham-cb-fa-decrease\n  criterion: FA as in [FA], subregions as in [CB-PARTS], model as in [FA-ANOVA] for monkey D\n    (Fig6B_dbs_FA_CB_part_mkD_analysisscript_a.m). Reproduced when the interaction has p < 0.05\n    and the sham-side dACC-CB has Tukey-Kramer p < 0.05 with post below pre, and the sham-side\n    MCC-CB shows no significant increase.\n- id: fig6c-sham-cc1-no-change\n  statement: In the nonstimulation control animal, the CC1/DAPI ratio in the MCC-CB did not differ\n    between the implanted and control hemispheres (paired t-test, t(27) = -0.99, p = 0.33).\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain networks,\n    paragraph 2; Fig. 6c; Extended Data Fig. 10b\n  quote: the ratio of myelinated oligodendrocytes (CC1/DAPI) in the MCC-CB did not differ between\n    the implanted and control hemispheres\n  statistics:\n  - test: two-sided paired t-test\n    statistic: t(27) = -0.9888, Cohen's dz = -0.19\n    p: 0.3316\n    n: 28 fields per hemisphere (7 fields x 4 sections)\n  criterion: A claim of absence, judged on the paper's test, the paired t-test of [IF]\n    (Fig6C_dbs_IF_CC1_mkD_MCC_CB_analysisscript_a.m) at p < 0.05. Reproduced when p >= 0.05; not\n    reproduced when p < 0.05. The mean difference and dz are reported.\n- id: ed10c-sham-subcortical-decrease\n  statement: After lead implantation alone, whole-brain connectivity changes were less coherent;\n    cortico-cortical changes looked random and subcortico-subcortical connectivity decreased, the\n    opposite of SCC-DBS.\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain networks,\n    paragraph 3; Extended Data Fig. 10c; Supplementary Table 10\n  quote: Cortical-to-cortical connections showed more random connectivity changes, and\n    subcortical-to-subcortical connections showed a consistent negative change, which is the\n    opposite direction of what we saw after SCC-DBS\n  expected:\n  - quantity: ROIs with a significant change in monkey D, threshold p < 0.05/122 (ROIs of\n      Supplementary Table 10)\n    value: 53\n    tolerance: 5.3\n  data: with_inputs\n  criterion: Matrices as in [MATRIX] for monkey D alone. Readings for the summary, (a) the mean and\n    (b) the median change over pairs, as in fig4a-cortical-decrease-subcortical-increase.\n    Reproduced when, under one reading, the subcortico-subcortical value is below 0 and the\n    fraction of cortico-cortical pairs with a negative change is closer to one half than in the DBS\n    group. The count of significant ROIs is compared with the expected value and reported.\n- id: fig6d-sham-scc-little-change\n  statement: After lead implantation without stimulation, connectivity of the SCC changed little,\n    apart from a local increase at the implantation site; among the DMN and SAN hubs only the\n    sham-side vmFC and control-side anterior-dorsal insula changed (PrePost x side F(1,10106) =\n    4.58, p = 0.0323).\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain networks,\n    paragraph 3; Fig. 6d; Extended Data Fig. 10d\n  quote: Additionally, there was very little alteration in the functional connectivity associated\n    with the SCC, except for a localized increase in connectivity at the site of implantation\n  statistics:\n  - about: PrePost x side interaction\n    test: three-way ANOVA (DBS x side x target ROI)\n    statistic: F(1,10106) = 4.58, partial eta squared 0.00045\n    p: 0.0323\n  - about: sham-side vmFC\n    test: Tukey-Kramer post hoc\n    p: 0.000783\n    corrected: Tukey-Kramer\n    n: 66 voxels\n  - about: control-side anterior-dorsal insula\n    test: Tukey-Kramer post hoc\n    p: 1.37e-12\n    corrected: Tukey-Kramer\n    n: 51 voxels\n  data: with_inputs\n  criterion: Seed maps as in [SEED] for monkey D (seed in the implanted hemisphere), model as in\n    [SEED-ANOVA] for D (Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m), on the four hubs of\n    Extended Data Fig. 10d (vmFC, PCC, anterior-dorsal insula, dACC). Reproduced when PCC and\n    dACC on the sham side show no significant decrease (Tukey-Kramer p < 0.05) and at most two of\n    the eight pre-post comparisons are significant. The local increase at the lead site is read\n    from the map thresholded as in fig5a-control-group-no-reduction and reported, not judged.\n- id: fig6e-sham-no-network-reduction\n  statement: After lead implantation without stimulation, the reductions in connectivity between the\n    SCC and the DMN, LIM and CEN seen after SCC-DBS did not appear (PrePost x side F(1,10972) =\n    7.36, p = 0.0067).\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain networks,\n    paragraph 3; Fig. 6e\n  quote: Notably, the widespread reductions in connectivity that we saw in the DMN, LIM and CEN\n    after SCC-DBS were not observed\n  statistics:\n  - about: PrePost x side interaction\n    test: three-way ANOVA (DBS x side x network)\n    statistic: F(1,10972) = 7.36, partial eta squared 0.00067\n    p: 0.0067\n  - about: control-side DMN\n    test: Tukey-Kramer post hoc\n    p: 8.2e-08\n    corrected: Tukey-Kramer\n  - about: control-side CEN\n    test: Tukey-Kramer post hoc\n    p: 0.0088\n    corrected: Tukey-Kramer\n  - about: sham-side SMN\n    test: Tukey-Kramer post hoc\n    p: 0.000138\n    corrected: Tukey-Kramer\n  - about: control-side SAN\n    test: Tukey-Kramer post hoc\n    p: 0.000106\n    corrected: Tukey-Kramer\n  expected:\n  - quantity: sham-side DMN voxels (monkey D)\n    value: 453\n    tolerance: 45.3\n  - quantity: control-side DMN voxels (monkey D)\n    value: 404\n    tolerance: 40.4\n  data: with_inputs\n  depends_on:\n  - fig5c-network-decreases\n  criterion: A claim of absence, judged on the paper's test, the Tukey-Kramer post hoc of\n    [SEED-ANOVA] for D at p < 0.05. The paper lists significant changes in control-side DMN and\n    CEN (direction not stated), so the claim is read on the implanted (sham) side, where the\n    seed and the lead are. Reproduced when none of sham-side DMN, LIM and CEN has a significant\n    decrease; not reproduced when any does. The control-side results and their directions are\n    reported.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001785/10.1038-s41593-026-02301-4.yaml",
 "old_string": "#   rows of the paper's sheet (field order within section); open if the dataset does not give\n#   field order, readings (a) pair by section and field index, (b) pair by section and sorted\n#   field value is not a reading the paper allows, so only (a).",
 "new_string": "#   rows of the paper's sheet (Fig6C_dbs_IF_CC1_mkD_MCC_CB_analysisscript_a.m). The Methods do\n#   not say how fields are paired; the reading the text allows is by section and field index\n#   within section, the order in which the fields were taken."
}
```

```
The file claims/001785/10.1038-s41593-026-02301-4.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001785/10.1038-s41593-026-02301-4.yaml",
 "old_string": "  criterion: As in fig5b-scc-decreases, the control-hemisphere pre-post comparisons. Supplementary\n    Table 9 has 12 of 17 control-side ROIs at p < 0.05 (PCC, vmFC, STG, anterior-dorsal insula,\n    dACC, DLPFC, area 25, area 32, HIP, sensory cortex, MT). Reproduced when PCC, vmFC and dACC on\n    the control side each have Tukey-Kramer p < 0.05, the three DMN and SAN hubs of Fig. 5b with\n    the largest effects; partially reproduced when at least one does. The number of significant\n    control-side ROIs is reported against the table.",
 "new_string": "  criterion: As in fig5b-scc-decreases, the control-hemisphere pre-post comparisons. Supplementary\n    Table 9 has 11 of 17 control-side ROIs at p < 0.05 (PCC, vmFC, STG, anterior-dorsal insula,\n    dACC, DLPFC, area 25, area 32, HIP, sensory cortex, MT). Reproduced when the four hubs of Fig.\n    5b (vmFC, PCC, anterior-dorsal insula, dACC), all reported significant on the control side in\n    its legend, each have Tukey-Kramer p < 0.05 on the control side; partially reproduced when two\n    or three do. The number of significant control-side ROIs is reported against the table."
}
```

```
The file claims/001785/10.1038-s41593-026-02301-4.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001785/10.1038-s41593-026-02301-4.yaml paper/10.1038-s41593-026-02301-4.txt; grep -nE "^\s+[a-z_]+: [^\"'|>].*: " claims/001785/*.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('claims/001785/10.1038-s41593-026-02301-4.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))
from collections import Counter;print(Counter(x.get('data','dataset') for x in c))"; git status --short
```

```
31 31 21 31 11
Counter({'with_inputs': 19, 'dataset': 10, 'elsewhere': 2})
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
?? claims/001785/
?? scripts
```

**Agent**

I wrote `claims/001785/10.1038-s41593-026-02301-4.yaml`. The earlier reader run stopped because the supplement was missing; it is now in `paper/`, so nothing a claim needs is missing.

**Text read:** the version of record from Europe PMC (PMC13337501): main text, Methods, figure and Extended Data legends, plus the Supplementary Information PDF (Supplementary Methods 1–7, Supplementary Tables 1–11), all in the `.txt`. There was no article PDF, and I didn't need one.

**Code read:** the paper's code is in DANDI:001773 version 0.260416.1939: 17 MATLAB scripts and the source-data spreadsheets. I took from it the ANOVA models (monkey as a main effect, MATLAB's default type III sums of squares), the Tukey–Kramer comparisons over the PrePost × side × tract (or ROI) cells, the paired t-test for monkey D, and the network membership. The reported error df all match these models.

**Counts:** 31 claims, all with quotes and criteria; 21 have statistics and 11 have expected values. Data: 10 `dataset`, 19 `with_inputs` (they need the D99, CHARM and SARM atlases in NMT v2.0, distributed with AFNI and listed on PRIME-DRE), and 2 `elsewhere` (the behavior bins, which are only in 001773, `source_data/dbs_behavior_data_a.xlsx`). The quote checker found every quote. It flagged 7 p-values it couldn't match because of how they are printed; I checked each against the text and they are correct.

**Details the paper leaves open, with the readings named:**
- **Tract masks:** the seed masks were drawn by hand and are not given. The FA claims need the paper's masks from the dataset; the reported voxel counts check them.
- **Lead-track voxels excluded from FA:** found (a) from the CT-defined lead location, or (b) from the visible track in the post-DBS images.
- **CB subregions "adjacent to" D99 areas:** (a) the nearest D99 label, or (b) each area's front-to-back extent.
- **CC1/DAPI counting thresholds:** not reported. If the dataset holds images only: (a) FIJI IsoData or (b) Otsu, per section and channel.
- **Pairing of fields in monkey D's paired t-test:** by section and field index, the only reading the text allows.
- **FC matrix:** one matrix per run, then averaged (Methods), or one per session on all runs together (code, kept as a variant).
- **Per-ROI test in Fig. 4b:** rank-sum of the ROI's changes against zeros (code and legend), or of pre against post values (Methods wording). The threshold is open between p < 0.01/122 (Methods) and p < 0.05/122 (code). Supplementary Tables 1, 2 and 10 follow the code.
- **Circular-plot threshold:** 0.1 in the legend, 0.15 in the code (variant).
- **Seed connectivity:**
  - Runs: per run then averaged, or the session's full series.
  - Normalizing maximum: over all brain voxels, or outside the seed.
  - Voxel grid: 1.5 or 1.6 mm. Supplementary Table 8's counts decide.
- **Voxel test behind the thresholded seed maps:** not stated. Named readings are a per-voxel two-sample test across runs, or a one-sample test of each animal's change.
- **Summaries the paper judges by eye** ("broad reduction", "no systematic pattern"): the mean or the median over ROI pairs.

**Settled by the code where the Methods disagree:** the limbic network includes the contralateral area 25. The code and Extended Data Fig. 9a include it, and so does the reported n = 821; the Methods list leaves it out.

**Errors in the paper, noted in the file:**
- Fig. 6a prints "F 1,1238 = 6.02, P = 0.0025", but P = 0.0025 needs 2 df, which the three-way term has, so the 1 is taken as a misprint.
- Supplementary Tables 3, 4 and 11 (effect sizes) are identical, so I didn't use them.
- Extended Data Fig. 10d says monkey D's post scan was "10 weeks" after implantation; the Methods say 6 weeks without stimulation after the 4-week recovery.

Nothing is committed; the other untracked files in the working tree aren't mine.

## End of run

31 turns, 9 minutes, result: success.
