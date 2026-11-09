# 001773 · author · run 41671057318

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls docs claims/001773 paper entries attempts | head -80; wc -l docs/*.md README.md
```

```
Tue Nov  3 16:13:54 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
[... 97 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
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
[... 593 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "README.md"
}
```

```
1	# Encore Science: the registry
2	
3	Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).
4	
5	Agents, and people, try to reproduce the key findings of papers from the open
6	data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
7	here: the notebooks when it works, and the reason when it does not.
8	
9	- **For the archive:** evidence of whether each dandiset is complete and
10	  accurate enough to support the findings of its paper.
11	- **For analysts:** working notebooks to build new analyses on.
12	
13	Status: pilot. All eight pilot targets have been attempted and checked by an
14	independent agent.
15	
16	**Dashboard:** <https://encorescience.org/>
17	
18	## Reading the outcomes
19	
20	An outcome says what one attempt could recover from the data in a dandiset,
[... 120 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/design.md"
}
```

```
1	# Reproduction registry: design
2	
3	Status: draft for discussion. "Reproduction registry" is a working name.
4	
5	## Goal
6	
7	Agents work through the dandisets on the DANDI Archive that have an associated
8	paper. For each one, an agent tries to reproduce the paper's key findings and
9	figures from the open data, writes the analysis as a notebook, and registers it
10	here. People can deposit too, but most deposits are expected to come from
11	agents.
12	
13	This serves two purposes:
14	
15	1. **Check the data.** A finding that can be reproduced shows the dandiset is
16	   complete and accurate enough to support it. A finding that cannot be
17	   reproduced, with the reason, tells the data owner and the archive what is
18	   missing.
19	2. **Give analysts a starting point.** Someone who wants to test a new
20	   hypothesis on a dandiset starts from notebooks that already load the data
[... 252 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la claims/001773 paper entries/001453-fouke-2025 claims/001453; cat attempts/001453-fouke-2025-01.yaml; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; ls questions | head; sed -n 1,80p docs/archives.md
```

```
<persisted-output>
Output too large (41.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f29fdf87-f731-49ab-9e78-2627f4f5ea55/tool-results/bkq3yu0yp.txt

Preview (first 2KB):
claims/001453:
total 28
drwxr-xr-x   2 runner runner  4096 Nov  3 16:09 .
drwxr-xr-x 235 runner runner  4096 Nov  3 16:09 ..
-rw-r--r--   1 runner runner 17825 Nov  3 16:09 10.1016-j.cub.2025.04.027.yaml

claims/001773:
total 64
drwxr-xr-x   2 runner runner  4096 Nov  3 16:09 .
drwxr-xr-x 235 runner runner  4096 Nov  3 16:09 ..
-rw-r--r--   1 runner runner 56816 Nov  3 16:09 10.1038-s41593-026-02301-4.yaml

entries/001453-fouke-2025:
total 132
drwxr-xr-x   2 runner runner  4096 Nov  3 16:09 .
drwxr-xr-x 187 runner runner 12288 Nov  3 16:09 ..
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001453-fouke-2025-01.yaml | head -150
```

```
schema_version: 2
id: 001453-fouke-2025-01
dataset:
  archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: 001453-fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
    platform: GitHub Actions
[... 130 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001773/10.1038-s41593-026-02301-4.yaml"
}
```

```
1	# Claims for Fujimoto, Fujimoto, Elorette et al. (2026), "Deep brain stimulation induces white
2	# matter remodeling and functional changes to brain-wide networks", Nature Neuroscience,
3	# doi:10.1038/s41593-026-02301-4, on dandiset 001773.
4	#
5	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, as
6	# the reader of docs/protocol.md (version pilot-10).
7	#
8	# Text read: the version of record (open access, PMC13337501, as served by Europe PMC), main
9	# text, figure legends, Methods and Extended Data legends 1 to 10, together with the
10	# Supplementary Information PDF (Supplementary Methods 1 to 7 and Supplementary Tables 1 to 11),
11	# all in paper/10.1038-s41593-026-02301-4.txt. No PDF of the main article was available; no
12	# figure needed to be read from one. The Nature "Source Data" files (statistical source data for
13	# Figs. 2 to 6 and Extended Data Figs. 1, 4, 5, 6, 9 and 10) are cited by the paper but were not
14	# under paper/ and no claim relies on them.
15	#
16	# Code: the paper says its custom MATLAB scripts for the functional MRI analysis are deposited in
17	# the dandiset itself (Code availability, doi 10.48324/dandi.001773/0.260416.1939). A reader may
18	# not open the dataset's files, so this code was NOT read. Every criterion below rests on the
19	# Methods, legends and supplement. Where a detail is named open, the author should check whether
20	# that code settles it and ask a reader (protocol, author step 6).
[... 918 more lines not kept]
```

**Agent**

The claims file has 30 claims. Next I'll look at the dataset (54 files, about 3.2 MB, BIDS).

**Agent calls Bash**

```bash
cd  grep -n "DANDI" -A60 docs/archives.md | head -120
```

```
4:the DANDI Archive. The protocol is written for any archive. What is particular
5-to an archive (how its datasets are named, versioned and read) is here, and an
6-agent is pointed to its archive's section.
7-
8-A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
9:`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
10-`transcripts/`, the `attempt/` branch, the paper store) are under its folder
11:name: the identifier alone for DANDI, which the registry began with, and
12-`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
13-below), and `tools/datasets.py` turns one form of a dataset's name into another.
14-The workflows take a dataset in any of these forms.
15-
16:## DANDI
17-
18-- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
19-  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
20:  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
21-- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
22-  `10.48324/dandi.<id>/<version>`. The draft can change. Pin the version the
23-  paper cites, or the latest published one. For a draft, record its
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001773/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001773/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent**

The paper cites version 0.260416.1939, so I'll pin that one. Listing its assets:

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001773/versions/0.260416.1939/assets/?page_size=200" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['size'], a['path'])
"; echo; curl -s "https://api.dandiarchive.org/api/dandisets/001773/versions/0.260615.1838/assets/?page_size=200" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['size'], a['path'])
" > v2.txt; curl -s "https://api.dandiarchive.org/api/dandisets/001773/versions/0.260416.1939/assets/?page_size=200" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['size'], a['path'])
" > v1.txt; diff v1.txt v2.txt && echo same
```

Result: the fetched text is not kept.

**Agent**

The dataset holds no NWB: 23 MATLAB scripts and 31 Excel source-data sheets, identical between 0.260416.1939 (the version the paper cites) and 0.260615.1838. Reading the README and the code next.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import requests, json
V="0.260416.1939"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/001773/versions/{V}/assets/?page_size=200").json()
ids={a['path']:a['asset_id'] for a in r['results']}
for p in ['README.md','dataset_description.json']:
    print('=====',p); print(requests.get(f"https://api.dandiarchive.org/api/assets/{ids[p]}/download/").text)
m=requests.get(f"https://api.dandiarchive.org/api/dandisets/001773/versions/{V}/").json()
print(json.dumps({k:m.get(k) for k in ['description','relatedResource','assetsSummary','citation']},indent=1)[:4000])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'
```

**Agent calls Bash**

```bash
cd $TMPDIR; uv venv -q expl && . expl/bin/activate && uv pip install -q requests pandas openpyxl statsmodels scipy numpy 2>&1 | tail -2; python -c "import pandas, statsmodels; print(pandas.__version__, statsmodels.__version__)"
```

```
3.1.0 0.15.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . expl/bin/activate; mkdir -p code; python - <<'EOF'
import requests, json
V="0.260416.1939"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/001773/versions/{V}/assets/?page_size=200").json()
ids={a['path']:a['asset_id'] for a in r['results']}
json.dump(ids,open('ids.json','w'))
for p in ['README.md','dataset_description.json']:
    print('=====',p); print(requests.get(f"https://api.dandiarchive.org/api/assets/{ids[p]}/download/").text)
m=requests.get(f"https://api.dandiarchive.org/api/dandisets/001773/versions/{V}/").json()
print(json.dumps({k:m.get(k) for k in ['description','relatedResource','assetsSummary']},indent=1)[:3000])
# code into memory, print to file in TMPDIR for reading (scratch only)
for p in ids:
    if p.endswith('.m'):
        open('code/'+p.split('/')[-1],'w').write(requests.get(f"https://api.dandiarchive.org/api/assets/{ids[p]}/download/").text)
EOF
ls code; md5sum code/*FCmatrix* code/Fig6D*
```

```
===== README.md
This dataset contains source data and analysis scripts associated with the study:

"Deep brain stimulation induces white matter remodeling and functional changes to brain-wide networks"

Contents:
- source_data/: Excel files containing processed data used for statistical analysis and figure generation
- code/: MATLAB scripts used to generate figures and perform analyses

Description:
The Excel files contain tract-specific fractional anisotropy (FA) measurements, functional connectivity values, immunofluorescence quantification data, g-ratio measurements derived from electron microscopy, and behavioral metrics. MATLAB scripts are organized by figure number and reproduce the analyses and plots presented in the manuscript.

Notes:
- Scripts are designed to directly load the corresponding Excel files

Author: Satoka Fujimoto


===== dataset_description.json
{
[... 55 more lines not kept]
```

**Agent**

Two scripts are deposited twice under different names (identical MD5). Reading the analysis code:

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat FigE1_dbs_behavior_analysisscript_a.m Fig2A_dbs_FA_wholetract_analysisscript_a.m
```

```
clear all;
close all;

maindir = char('C:\MATLAB_analy\DBS\data\'); 
cd(maindir);

% load list
list = importdata('dbs_behavior_data_a.xlsx');

%ANOVA and posthoc for mk N & T
y = list.data(list.data(:,6) == 1, 2); %movement
y2 = list.data(list.data(:,6) == 1, 3); %foraging
g1 = list.data(list.data(:,6) == 1, 4); %mk
g2 = list.data(list.data(:,6) == 1, 5); %stim
g3 = list.data(list.data(:,6) == 1, 6); %group

% anova 
[p,tbl,stats] = anovan(y,{g1,g2},"Model", "full", "Varnames",["monkey","stim"]);
[p2,tbl2,stats2] = anovan(y2,{g1,g2},"Model", "full", "Varnames",["monkey","stim"]);

[... 354 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; grep -v "^\s*$" Fig2B_dbs_FA_CB_part_analysisscript_a.m | grep -v -i "text(\|errorbar\|plot(\|ylim\|xlim\|xticks\|ylabel\|title\|subplot\|figure\|hold on\|FontSize\|HorizontalAlignment" | head -120; echo =====; cat Fig3CandE5_dbs_IF_CC1_MCC_CB_analysisscript_a.m Fig3F_dbs_EMgratio_analysisscript_a.m Fig6C_dbs_IF_CC1_mkD_MCC_CB_analysisscript_a.m | grep -v -i "errorbar\|plot(\|ylim\|xlim\|xticks\|ylabel\|title\|subplot\|figure\|hold on"
```

```
clear all;
close all;
maindir = char('C:\MATLAB_analy\DBS\data\'); 
cd(maindir);
% load list
list = importdata('dbs_FA_CB_subpart_data_a.xlsx');
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
    0 1 1 0;
    0 1 0 1;
    0 0 1 1;
    0 1 1 1;];
[... 279 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; grep -v "^\s*$" Fig5BCandE9_dbs_FC_25norm_mkNT_analysisscript_a.m | grep -v -i "text(\|errorbar\|plot(\|ylim\|xlim\|xticks\|ylabel\|title\|subplot\|figure\|hold on\|FontSize\|HorizontalAlignment\|scatter\|boxplot\|xticklabels\|legend\|set(gca"
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
    0 1 1 0;
    0 1 0 1;
    0 0 1 1;
    0 1 1 1;];
[... 315 more lines not kept]
```

**Agent**

The seed connectivity file is named "concatenated", which settles the run handling, and the code gives the network membership as ROI index lists. Now the connectome script:

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat "Fig4 Fujimoto_NatNeuro_2026_FCmatrix.m"
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
cd $TMPDIR; . expl/bin/activate; python - <<'EOF'
import requests, json, io, pandas as pd
ids=json.load(open('ids.json'))
for p in sorted(ids):
    if not p.endswith('.xlsx'): continue
    b=requests.get(f"https://api.dandiarchive.org/api/assets/{ids[p]}/download/").content
    open('x_'+p.split('/')[-1],'wb').write(b)  # scratch cache for exploration only
    x=pd.ExcelFile(io.BytesIO(b))
    for s in x.sheet_names:
        df=x.parse(s,header=None)
        print('==',p,'|',s,df.shape)
        print(df.head(3).to_string(max_colwidth=18)[:900])
EOF
```

```
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
<stdin>:9: Pandas4Warning: ExcelFile.parse is deprecated. Use pd.read_excel instead.
[... 196 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . expl/bin/activate; python - <<'EOF' 2>/dev/null
import pandas as pd, numpy as np
pd.set_option('display.width',250)
def rd(f): return pd.read_excel('x_'+f,header=None)
for f in ['dbs_behavior_data_a.xlsx','dbs_FA_wholetract_data_a.xlsx','dbs_FA_CB_subpart_data_a.xlsx','dbs_FA_wholetract_mkD_data_a.xlsx','dbs_FA_CB_subpart_mkD_data_a.xlsx','CC1_MCC_CB_data_a.xlsx']:
    d=rd(f); 
    leg=d.iloc[:,6:].dropna(how='all').dropna(axis=1,how='all')
    print('=====',f); print(leg.to_string()[:1500])
d=rd('dbs_behavior_data_a.xlsx'); print(d.iloc[:,:6].iloc[1:].astype(float).groupby([3,4,5]).agg(['count','mean'])[[1,2]])
EOF
```

```
===== dbs_behavior_data_a.xlsx
         9           10   11                       12   13    14   15
1  movement         yes  1.0                       no  0.0   NaN  NaN
2  foraging         yes  2.0                       no  1.0   NaN  NaN
3        mk        mk N  1.0                     mk T  2.0  mk D  3.0
4      stim    pre stim  0.0                 stim 6w   1.0   NaN  NaN
5     group  sDBS group  1.0  non-stimulation control  0.0   NaN  NaN
===== dbs_FA_wholetract_data_a.xlsx
        16         17   18            19   20    21   22
1       mk       mk N  1.0          mk T  2.0   NaN  NaN
2  prepost        pre  1.0          post  2.0   NaN  NaN
3     side  stim side  1.0  control side  2.0   NaN  NaN
4    tract         CB  1.0            UF  2.0  Fmin  3.0
===== dbs_FA_CB_subpart_data_a.xlsx
        11          12   13            14   15   16   17   18   19
1       mk        mk N  1.0          mk T  2.0  NaN  NaN  NaN  NaN
2  prepost         Pre  1.0          Post  2.0  NaN  NaN  NaN  NaN
3     hemi  Stim side   1.0  Control side  2.0  NaN  NaN  NaN  NaN
4     part         SCC  1.0          dACC  2.0  MCC  3.0  PCC  4.0
===== dbs_FA_wholetract_mkD_data_a.xlsx
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . expl/bin/activate; python - <<'EOF' 2>/dev/null
import pandas as pd, numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
for f in ['dbs_FC25norm_mkNT_concatenated_all_data_a.xlsx','dbs_FC25norm_mkD_concatenated_all_data_a.xlsx']:
    d=pd.read_excel('x_'+f)
    print(f,d.shape); print(d.describe().T)
    print(d.groupby(['subject','time_condition','date']).size())
    print(d.groupby(['roi','side','subject','time_condition']).size().unstack([2,3]))
print(pd.read_excel('x_FC_ROI_label.xlsx'))
EOF
```

```
dbs_FC25norm_mkNT_concatenated_all_data_a.xlsx (24424, 9)
                  count       mean  ...        75%        max
x               20348.0   0.303420  ...  12.000000  28.500000
y               20348.0  -7.964444  ...   4.625000  25.625000
z               20348.0  22.982332  ...  30.375000  37.875000
fc              20348.0   0.019878  ...   0.040792   1.379922
subject         20348.0   1.500000  ...   2.000000   2.000000
roi             20348.0   9.981325  ...  15.000000  17.000000
time_condition  20348.0   1.500000  ...   2.000000   2.000000
side            20348.0   1.500000  ...   2.000000   2.000000
date            20348.0   2.500000  ...   3.250000   4.000000

[9 rows x 8 columns]
subject  time_condition  date
1.0      1.0             1.0     5087
         2.0             2.0     5087
2.0      1.0             3.0     5087
         2.0             4.0     5087
dtype: int64
subject         1.0       2.0     
[... 109 more lines not kept]
```

**Agent**

The seed-FC tables match the paper's counts exactly (20,348 voxel values for N and T, 10,174 for D), and the code's LIM list includes area 25. Next, the connectome workbook:

**Agent calls Bash**

```bash
cd $TMPDIR; . expl/bin/activate; python - <<'EOF' 2>/dev/null
import pandas as pd, numpy as np
x=pd.ExcelFile('x_Source Data FC matrix.xlsx')
for s in x.sheet_names:
    d=pd.read_excel(x,s,header=None)
    print('=====',s,d.shape)
    c0=d.iloc[:,0].astype(str)
    for i,v in enumerate(c0):
        if not v.replace('.','').replace('-','').strip().isdigit() and i<400:
            pass
    # rows where col1 is NaN = section headers
    hdr=[(i,d.iloc[i,0]) for i in range(len(d)) if pd.isna(d.iloc[i,1]) or isinstance(d.iloc[i,1],str)]
    print(hdr[:20])
    print(d.iloc[:3,:5])
d=pd.read_excel(x,'Average FC matrix DBS',header=None)
print(list(d.iloc[1,:10])); print(list(d.iloc[1:126,0])[:5], list(d.iloc[1:126,0])[50:60], list(d.iloc[1:126,0])[118:126])
EOF
```

```
Exit code 1
===== Average FC matrix DBS (374, 123)
```

**Agent calls Bash**

```bash
cd $TMPDIR; . expl/bin/activate; python - <<'EOF' 2>&1 | grep -v Warn
import pandas as pd, numpy as np
x=pd.ExcelFile('x_Source Data FC matrix.xlsx')
for s in x.sheet_names:
    d=pd.read_excel(x,s,header=None)
    print('=====',s,d.shape)
    for i in range(len(d)):
        v=d.iloc[i,0]
        if isinstance(v,str): print(i, repr(v[:80]), '| next:', [str(t)[:12] for t in d.iloc[i,1:4]])
EOF
```

```
===== Average FC matrix DBS (374, 123)
0 'DBS group Pre' | next: ['nan', 'nan', 'nan']
125 'DBS group post' | next: ['nan', 'nan', 'nan']
250 'DBS group Post-Pre' | next: ['nan', 'nan', 'nan']
===== Average FC matrix CTRL (374, 123)
0 'Control gropu Pre' | next: ['nan', 'nan', 'nan']
125 'Control group Post' | next: ['nan', 'nan', 'nan']
250 'Control group Post-Pre' | next: ['nan', 'nan', 'nan']
===== Circular plot (111, 54)
0 'DBS group FC average' | next: ['nan', 'nan', 'nan']
56 'Control group FC average' | next: ['nan', 'nan', 'nan']
===== Sham animal FC matrix (374, 123)
0 'Sham animal Pre' | next: ['nan', 'nan', 'nan']
125 'Sham animal Post' | next: ['nan', 'nan', 'nan']
250 'Sham animal Post-Pre' | next: ['nan', 'nan', 'nan']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . expl/bin/activate; python - <<'EOF' 2>&1 | grep -v Warn
import pandas as pd, numpy as np
x=pd.ExcelFile('x_Source Data FC matrix.xlsx')
d=pd.read_excel(x,'Average FC matrix DBS',header=None)
print(d.iloc[0:4,0:6]); print(d.iloc[120:128,0:5]); print(d.iloc[1,118:123].tolist())
lab_row=d.iloc[1,1:].tolist(); lab_col=d.iloc[2:124,0].tolist()
print(len(lab_row), lab_row[:5], lab_row[50:58], lab_row[-3:])
print(lab_col==lab_row)
pre=d.iloc[2:124,1:123].astype(float).values; post=d.iloc[127:249,1:123].astype(float).values; diff=d.iloc[252:374,1:123].astype(float).values
print(np.diag(pre)[:5], np.diag(diff)[:5], np.nanmax(abs(post-pre-diff)), np.allclose(pre,pre.T,equal_nan=True))
print(d.iloc[125:128,0:4], d.iloc[250:253,0:4])
c=pd.read_excel(x,'Circular plot',header=None); print(c.iloc[0:3,0:5]); print(c.iloc[55:58,0:5])
EOF
```

```
0        1        2        3        4        5
0  DBS group Pre      NaN      NaN      NaN      NaN      NaN
1              1  0.22765  0.17945  0.51025  0.38535  0.27810
2        0.22765  1.00000  0.56575  0.36490  0.32735  0.51355
3        0.17945  0.56575  1.00000  0.29150  0.27255  0.29205
                  0        1        2        3        4
120        -0.02385 -0.01900 -0.01640 -0.06125 -0.06085
121         -0.0076 -0.01030  0.02065  0.01385 -0.00945
122         0.00155  0.01665 -0.00660 -0.02180 -0.01190
123         -0.0105 -0.00210 -0.00085 -0.01910 -0.04030
124             NaN      NaN      NaN      NaN      NaN
125  DBS group post      NaN      NaN      NaN      NaN
126               1  0.03580  0.04020  0.20920  0.04155
127          0.0358  1.00000  0.26340  0.15595  0.10420
[-0.01425, -0.02385, -0.0076, 0.00155, -0.0105]
122 [0.22765, 0.17945, 0.51025, 0.38535, 0.2781] [0.1964, 0.1246, 0.1203, 0.07955, 0.03255, -0.01245, 0.226, 0.0253] [-0.0076, 0.00155, -0.0105]
True
[1. 1. 1. 1. 1.] [0. 0. 0. 0. 0.] 1.1102230246251565e-16 True
                  0       1       2        3
125  DBS group post     NaN     NaN      NaN
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . expl/bin/activate; python - <<'EOF' 2>&1 | grep -v Warn
import pandas as pd, numpy as np
x=pd.ExcelFile('x_Source Data FC matrix.xlsx')
for s in ['Average FC matrix DBS','Average FC matrix CTRL','Sham animal FC matrix']:
    d=pd.read_excel(x,s,header=None)
    M=[d.iloc[a:a+123,0:123].astype(float).values for a in (1,126,251)]
    for m in M: print(s, m.shape, np.isnan(m).sum(), np.diag(m)[:3], np.allclose(m,m.T))
    print('post-pre-diff', np.abs(M[1]-M[0]-M[2]).max())
    nanrows=[i for i in range(123) if np.isnan(M[0][i]).all()]
    print('nan rows',nanrows)
c=pd.read_excel(x,'Circular plot',header=None)
A=c.iloc[1:55,0:54].astype(float).values; B=c.iloc[57:111,0:54].astype(float).values
d=pd.read_excel(x,'Average FC matrix DBS',header=None); D=d.iloc[251:374,0:123].astype(float).values
dc=pd.read_excel(x,'Average FC matrix CTRL',header=None); DC=dc.iloc[251:374,0:123].astype(float).values
print(A.shape, np.abs(A-D[:54,:54]).max(), np.abs(B-DC[:54,:54]).max())
EOF
```

```
Average FC matrix DBS (123, 123) 0 [1. 1. 1.] True
Average FC matrix DBS (123, 123) 0 [1. 1. 1.] True
Average FC matrix DBS (123, 123) 0 [0. 0. 0.] True
post-pre-diff 1.1102230246251565e-16
nan rows []
Average FC matrix CTRL (123, 123) 0 [1. 1. 1.] True
Average FC matrix CTRL (123, 123) 0 [1. 1. 1.] True
Average FC matrix CTRL (123, 123) 0 [0. 0. 0.] True
post-pre-diff 3.1086244689504383e-15
nan rows []
Sham animal FC matrix (123, 123) 0 [1. 1. 1.] True
Sham animal FC matrix (123, 123) 0 [1. 1. 1.] True
Sham animal FC matrix (123, 123) 0 [0. 0. 0.] True
post-pre-diff 1.6653345369377348e-16
nan rows []
(54, 54) 0.0 0.0
Shell cwd was reset to
```

**Agent**

The connectome matrices are 123 x 123 with no ROI labels, where the paper says 122 ROIs. Checking the paper's text on this and on the per-ROI test:

**Agent calls Bash**

```bash
cd paper; grep -n -i "122\|123 \|rank-sum\|ranksum\|Bonferroni\|3dNetCorr\|CHARM" 10.1038-s41593-026-02301-4.txt | cut -c1-400 | head -40
```

```
7:pmc Nat Neurosci Nat Neurosci 981 npgopen 9809671 Nature Neuroscience 1097-6256 1546-1726 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC13337501 PMC13337501.1 13337501 13337501 42225897 10.1038/s41593-026-02301-4 2301 1 Article Deep brain stimulation induces white matter remodeling and functional changes to brain-wide networks http://orcid.org/0000-0003-2374-3002 Fujimoto
817:0.122951
1078:0.122951
2255:0.122951
```

**Agent calls Bash**

```bash
cd paper; wc -c *.txt; grep -o -i ".\{300\}wilcoxon.\{300\}" 10.1038-s41593-026-02301-4.txt | head; grep -o -i ".\{200\}bonferroni.\{200\}" 10.1038-s41593-026-02301-4.txt | head -5; grep -o -i ".\{300\}3dnetcorr.\{400\}" 10.1038-s41593-026-02301-4.txt | head -3
```

```
186673 10.1038-s41593-026-02301-4.txt
Each data point represents measurements from individual ROI (pre, n = 122; post, n = 122), pooled across two monkeys. Rank-sum test was conducted to determine statistical significance ( P < 0.01 with Bonferroni correction). Statistical comparisons assessed differences between pre and post conditions. All tests were two-sided. P values are provided in Supplementary Table 1 (DBS group) and Supplementary Table
raged to investigate the regional effects caused by SCC-DBS or nonsurgical control. A rank-sum test was conducted to determine statistical significance between pre and post conditions ( P < 0.01 with Bonferroni correction). Functional connectivity changes were further visualized as circular plots using the circular Graph toolbox run in MATLAB. For targeted seed-based analyses, the seed ROI was defined as th
I (pre, n = 122; post, n = 122), collected from one monkey. Colors represent significant negative (blue) and positive changes (orange) of functional connectivity from zero in each ROI ( P < 0.01 with Bonferroni correction, rank-sum test). Statistical comparisons assessed differences between pre and post conditions. All tests were two-sided. Exact P values are shown in Supplementary Table 10 . Effect sizes (
d converted to percent signal change. Finally, the motion derivatives from each scan along with cerebrospinal fluid and white matter signal were regressed out. The residuals from this analysis were then used to compute functional connectivity. The full connectome analyses were computed using ANFI’s 3dNetCorr function 51 , 71 , 76 . The correlations between regions of interest (ROIs) were computed at the fourth level of the cortical (Cortical Hierarchy Atlas of the Rhesus Macaque (CHARM atlas) 72 ) and subcortical (Subcortical Atlas of the Rhesus Macaque (SARM atlas) 77 ) hierarchical atlas. For each run, the functional connectomes were Fisher’s Z -transformed and then averaged within condition to cre
```

**Agent**

The paper's "n = 122" per ROI equals 123 ROIs minus the ROI itself, so the 123 x 123 matrices fit the legend. Checking the EM g-ratio sheet columns:

**Agent calls Bash**

```bash
cd $TMPDIR; . expl/bin/activate; python - <<'EOF' 2>&1 | grep -v Warn
import pandas as pd, numpy as np
pd.set_option('display.width',250)
d=pd.read_excel('x_dbs_EMgratio_MCC_CB_data_a.xlsx',header=None)
print(d.iloc[:4].to_string()); print(d.iloc[-3:].to_string())
b=d.iloc[2:,[3,4,5,6,7,8,9,10,11,12,13,14]].astype(float); b.columns=['long','short','thick','thin','diam','myel','g','circ','flag','mk','side','diam_nm']
print(b.describe().T)
print(b.groupby(['mk','side']).g.agg(['count','mean']))
g2=b.diam/(b.diam+2*b.myel); print('g check',np.abs(g2-b.g).max(), np.abs((b.long+b.short)/2-b.diam).max(), np.abs((b.thick+b.thin)/2-b.myel).max(), np.abs(b.long/b.short-b.circ).max())
print(d.iloc[2:,15:].dropna(how='all').head())
print(d.iloc[2:,1].str[:2].value_counts())
EOF
```

```
0       1    2         3      4                5      6                        7                  8         9            10               11   12    13                    14  15   16   17  18   19
0  NaN     NaN  NaN  Diameter    NaN  myelin thikness    NaN                      NaN                NaN       NaN          NaN              NaN  NaN   NaN                   NaN NaN  NaN  NaN NaN  NaN
1  NaN    Left  NaN      long  short            thick   thin  diameter of axon(pixel)  myeline thickness   g ratio  circularity  circularity>=2)   mk  side  diameter of axon(nm) NaN  NaN  NaN NaN  NaN
2  1.0  TL-1-1  1.0     0.752  0.665            0.517  0.391                  0.35425              0.454  0.438293     1.130827                1    2     2            356.030151 NaN  NaN  NaN NaN  NaN
3  2.0     NaN  2.0       0.3  0.248            0.186  0.165                    0.137             0.1755    0.4384     1.209677                1    2     2            137.688442 NaN  NaN  NaN NaN  NaN
        0    1    2      3      4      5      6      7       8         9         10 11 12 13          14  15   16   17  18   19
699  179.0  NaN  3.0  0.255  0.245  0.119  0.102  0.125  0.1105  0.530786  1.040816  1  1  1  125.628141 NaN  NaN  NaN NaN  NaN
700  180.0  NaN  4.0  0.694  0.486  0.134  0.102  0.295   0.118  0.714286  1.427984  1  1  1  296.482412 NaN  NaN  NaN NaN  NaN
701  181.0  NaN  5.0  0.865  0.531  0.127  0.108  0.349  0.1175  0.748124  1.629002  1  1  1  350.753769 NaN  NaN  NaN NaN  NaN
         count        mean  ...         75%          max
long     700.0    0.744281  ...    0.876000     2.640000
short    700.0    0.518881  ...    0.613000     1.850000
thick    700.0    0.189680  ...    0.212250     0.813000
thin     700.0    0.163214  ...    0.183250     0.880000
diam     700.0    0.315791  ...    0.371750     1.111000
myel     700.0    0.176447  ...    0.199750     0.608500
g        700.0    0.636123  ...    0.702110     0.857693
circ     700.0    1.453324  ...
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p entries/001453-fouke-2025/omr.py; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in entries/001453-fouke-2025/README.md; python - <<'EOF'
import json;nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:600]); print('---')
EOF
```

```
"""Loading and measures for the freely swimming optomotor data of dandiset 001453.

Fouke, He, Loring & Naumann (2025), Current Biology, doi:10.1016/j.cub.2025.04.027.

Each NWB file holds one fish: x and y position (pixels), heading (`f0_theta`, radians), its
change per frame (`f0_vtheta`; the file says radians/s, the data show radians per frame),
velocity estimates, and per frame the stimulus code and trial number (`stim_index`). Files are
streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Trial processing follows the paper's analysis notebook, Fig1-S1.ipynb, in
  https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit
  33a5c297ff4ab6ff49f6bdd96139e9fdd867025c (the Methods give none of these): Savitzky-Golay
  smoothing of positions (21 frames, order 2); rejection of trials whose absolute cumulative
  heading change exceeds 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or
  whose mean speed exceeds 100 mm/s; measures from 3 s to 35 s after the first tracked frame;
  10 pixels per mm (the code divides pixels per second by 10 to give mm/s); per fish the median
  over trials. The 3 s stationary phase and the 32 s of motion are in the Methods.
- The names of the stimulus codes combine the protocol file sevenrep_twentyonestim.hdf of the
[... 166 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/001773-fujimoto-2026/dbs.py",
 "content": "\"\"\"Loading and statistics for the source data of dandiset 001773.\n\nFujimoto, Fujimoto, Elorette et al. (2026), Nature Neuroscience, doi:10.1038/s41593-026-02301-4.\n\nThe dandiset holds no NWB files: Excel sheets of derived values (voxel FA, voxel seed\nconnectivity, ROI-by-ROI connectomes, cell counts, g-ratios, behavior bins) and the paper's\nMATLAB scripts under `code/`. Each sheet is read from the archive into memory at the pinned\nversion; nothing is written to disk.\n\nWhere the parameters come from:\n\n- The ANOVAs follow the paper's scripts in the dandiset. FA (Fig2A, Fig2B, Fig6A, Fig6B\n  scripts) and seed connectivity (Fig5BCandE9, Fig6DandE10D scripts) use MATLAB `anovan` with\n  the model matrix `model_mat2`: main effects of monkey, PrePost, side and tract (or subregion,\n  ROI, network) and every interaction of the last three, but none with monkey. Behavior,\n  CC1/DAPI and g-ratio (FigE1, Fig3CandE5, Fig3F, FigE6A, FigE6B scripts) use `anovan` with\n  `\"Model\",\"full\"` on monkey and condition, that is condition, monkey and their interaction.\n  `anovan` uses type III sums of squares and sum-to-zero constraints by default; `anova` does\n  the same, and type II is available as the variant the claims file asks for.\n- The post hoc tests are MATLAB `multcompare` on the `anovan` statistics, whose default is the\n  Tukey-Kramer method on the population marginal means, over the cells of the dimensions the\n  scripts name (`\"Dimension\",[2 3 4]`, PrePost x side x tract). `tukey_kramer` computes the same:\n  each mean is the model's prediction with the other factors averaged over their levels, its\n  covariance comes from the model, and P is the studentized range tail for the number of means\n  and the error df.\n- Monkey D's CC1/DAPI test is MATLAB `ttest(x1, x2)` on the row-paired lead-side and control-side\n  columns (Fig6C script).\n- The network hubs are the ROI lists of the Fig5BCandE9 script: DMN 1 2 3, SAN 4 5, CEN 6 7,\n  LIM 1 5 8 9 10 11 12, SMN 13 14 15, VIS 16 17 (ROI numbers of FC_ROI_label.xlsx).\n- The per-ROI connectome test of the Fig4 script is `ranksum` of each ROI's off-diagonal changes\n  against a vector of zeros at 0.05 / nrois; the cortical block is the first 54 ROIs (its\n  `plot([54 54], ...)` and the circular plot's `1:54`).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport itertools\nfrom functools import lru_cache\n\nimport numpy as np\nimport pandas as pd\nimport requests\nfrom scipy import stats\n\nDANDISET_ID = \"001773\"\nDANDISET_VERSION = \"0.260416.1939\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nN_CORTICAL = 54   # Fig4 script: cortical (CHARM) ROIs come first, then SARM\nNETWORKS = {      # Fig5BCandE9 script\n    \"DMN\": [1, 2, 3],\n    \"SAN\": [4, 5],\n    \"CEN\": [6, 7],\n    \"LIM\": [1, 5, 8, 9, 10, 11, 12],\n    \"SMN\": [13, 14, 15],\n    \"VIS\": [16, 17],\n}\nAREA25 = 8\n\n\n@lru_cache(maxsize=None)\ndef asset_ids() -> dict:\n    url = f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200\"\n    out = {}\n    while url:\n        r = requests.get(url, timeout=60)\n        r.raise_for_status()\n        j = r.json()\n        out.update({a[\"path\"]: a[\"asset_id\"] for a in j[\"results\"]})\n        url = j[\"next\"]\n    return out\n\n\n@lru_cache(maxsize=None)\ndef fetch(path: str) -> bytes:\n    \"\"\"The bytes of one asset, read into memory.\"\"\"\n    r = requests.get(f\"{API}/assets/{asset_ids()[path]}/download/\", timeout=120)\n    r.raise_for_status()\n    return r.content\n\n\ndef sheet(path: str, sheet_name=0, header=None) -> pd.DataFrame:\n    return pd.read_excel(io.BytesIO(fetch(path)), sheet_name=sheet_name, header=header)\n\n\ndef text(path: str) -> str:\n    return fetch(path).decode(\"utf-8\", errors=\"replace\")\n\n\n# ---------------------------------------------------------------- loaders\n\ndef behavior() -> pd.DataFrame:\n    d = sheet(\"source_data/dbs_behavior_data_a.xlsx\", header=0).iloc[:, :6].dropna()\n    return d.astype({\"sec\": int, \"movement\": int, \"foraging\": int, \"mk\": int, \"stim\": int, \"group\": int})\n\n\ndef fa_wholetract() -> pd.DataFrame:\n    d = sheet(\"source_data/dbs_FA_wholetract_data_a.xlsx\", header=0).iloc[:, :5].dropna()\n    return d.astype({\"mk\": int, \"prepost\": int, \"side\": int, \"tract\": int})\n\n\ndef fa_subpart() -> pd.DataFrame:\n    d = sheet(\"source_data/dbs_FA_CB_subpart_data_a.xlsx\", header=0).iloc[:, :5].dropna()\n    d = d.rename(columns={\"hemi\": \"side\"})\n    return d.astype({\"mk\": int, \"prepost\": int, \"side\": int, \"part\": int})\n\n\ndef _mkD(path: str, last: str) -> pd.DataFrame:\n    # These sheets have no header row; the legend (columns O onwards) names columns A to D.\n    d = sheet(path).iloc[:, :4].dropna()\n    d.columns = [\"FA\", \"prepost\", \"side\", last]\n    return d.astype({\"prepost\": int, \"side\": int, last: int})\n\n\ndef fa_wholetract_mkD() -> pd.DataFrame:\n    return _mkD(\"source_data/dbs_FA_wholetract_mkD_data_a.xlsx\", \"tract\")\n\n\ndef fa_subpart_mkD() -> pd.DataFrame:\n    return _mkD(\"source_data/dbs_FA_CB_subpart_mkD_data_a.xlsx\", \"part\")\n\n\ndef cc1(region: str) -> pd.DataFrame:\n    \"\"\"region: 'MCC_CB', 'dACC_CB' or 'UF-FMoverlap'.\"\"\"\n    d = sheet(f\"source_data/CC1_{region}_data_a.xlsx\", header=0).iloc[:, :7].dropna(subset=[\"CC1\"])\n    d.columns = [\"CC1\", \"DAPI\", \"ratio\", \"mk\", \"side\", \"section\", \"location\"]\n    return d.astype({\"CC1\": float, \"DAPI\": float, \"ratio\": float, \"mk\": int, \"side\": int, \"location\": int})\n\n\ndef cc1_mkD() -> pd.DataFrame:\n    return sheet(\"source_data/CC1_mkD_MCC_CB_data_a.xlsx\", header=0).iloc[:, :8].dropna(subset=[\"CC1_leadside\"])\n\n\ndef gratio() -> pd.DataFrame:\n    d = sheet(\"source_data/dbs_EMgratio_MCC_CB_data_a.xlsx\").iloc[2:, :15]\n    d.columns = [\"n\", \"label\", \"n_in_image\", \"d_long\", \"d_short\", \"m_thick\", \"m_thin\", \"radius\",\n                 \"myelin\", \"g\", \"aspect\", \"aspect_ok\", \"mk\", \"side\", \"diameter_nm\"]\n    d[\"label\"] = d[\"label\"].ffill()\n    num = [c for c in d.columns if c != \"label\"]\n    d[num] = d[num].astype(float)\n    return d.astype({\"mk\": int, \"side\": int})\n\n\ndef seed_fc(which: str = \"mkNT\") -> pd.DataFrame:\n    d = sheet(f\"source_data/dbs_FC25norm_{which}_concatenated_all_data_a.xlsx\", header=0).dropna(subset=[\"fc\"])\n    return d.astype({\"subject\": int, \"roi\": int, \"time_condition\": int, \"side\": int, \"date\": int})\n\n\ndef roi_labels() -> dict:\n    d = sheet(\"source_data/FC_ROI_label.xlsx\", header=0)\n    return dict(zip(d.ROI_Number.astype(int), d.ROI_Name))\n\n\ndef network_data(fc: pd.DataFrame, lim_with_area25: bool = True) -> pd.DataFrame:\n    \"\"\"Voxels of each network's hubs, with repeats (Fig5BCandE9 script).\"\"\"\n    parts = []\n    for i, (name, rois) in enumerate(NETWORKS.items(), start=1):\n        if name == \"LIM\" and not lim_with_area25:\n            rois = [r for r in rois if r != AREA25]\n        p = fc[fc.roi.isin(rois)].copy()\n        p[\"network\"] = i\n        parts.append(p)\n    return pd.concat(parts, ignore_index=True)\n\n\ndef connectomes(sheet_name: str) -> dict:\n    \"\"\"Pre, post and post-minus-pre ROI x ROI matrices from 'Source Data FC matrix.xlsx'.\"\"\"\n    d = sheet(\"source_data/Source Data FC matrix.xlsx\", sheet_name=sheet_name)\n    n = d.shape[1]\n    out = {}\n    for key, start in zip([\"pre\", \"post\", \"diff\"], [1, 1 + n + 2, 1 + 2 * (n + 2)]):\n        out[key] = d.iloc[start:start + n, :n].astype(float).values\n    out[\"titles\"] = [d.iloc[0, 0], d.iloc[n + 2, 0], d.iloc[2 * (n + 2), 0]]\n    return out\n\n\ndef offdiag(m: np.ndarray, i: int, keep_diag: bool = False) -> np.ndarray:\n    return m[:, i] if keep_diag else np.delete(m[:, i], i)\n\n\n# ---------------------------------------------------------------- ANOVA as MATLAB anovan\n\ndef _sum_coding(x: np.ndarray, levels) -> np.ndarray:\n    cols = np.zeros((len(x), len(levels) - 1))\n    for j, lev in enumerate(levels[:-1]):\n        cols[:, j] = (x == lev).astype(float)\n    cols[x == levels[-1], :] = -1.0\n    return cols\n\n\ndef _term_columns(codes: dict, term: tuple) -> np.ndarray:\n    blocks = [codes[f] for f in term]\n    out = blocks[0]\n    for b in blocks[1:]:\n        out = np.einsum(\"ni,nj->nij\", out, b).reshape(len(out), -1)\n    return out\n\n\ndef anova(df: pd.DataFrame, y: str, factors: list, terms: list, sstype: int = 3) -> dict:\n    \"\"\"N-way ANOVA with sum-to-zero coding, as MATLAB anovan.\n\n    terms: tuples of factor names, e.g. [(\"mk\",), (\"prepost\",), (\"prepost\", \"side\")].\n    Returns the table (SS, df, F, P, partial eta squared) and what `tukey_kramer` needs.\n    \"\"\"\n    yv = df[y].to_numpy(float)\n    levels = {f: sorted(df[f].unique()) for f in factors}\n    codes = {f: _sum_coding(df[f].to_numpy(), levels[f]) for f in factors}\n    blocks = {t: _term_columns(codes, t) for t in terms}\n\n    def fit(ts):\n        X = np.column_stack([np.ones(len(yv))] + [blocks[t] for t in ts])\n        beta, *_ = np.linalg.lstsq(X, yv, rcond=None)\n        r = yv - X @ beta\n        return float(r @ r), X, beta\n\n    sse, X, beta = fit(terms)\n    dfe = len(yv) - np.linalg.matrix_rank(X)\n    mse = sse / dfe\n    rows = []\n    for t in terms:\n        if sstype == 3:\n            reduced = [u for u in terms if u != t]\n            full_ss = sse\n        else:  # type II: the term against the terms that do not contain it\n            reduced = [u for u in terms if not set(t) <= set(u)]\n            full_ss = fit(reduced + [t])[0]\n        ss = fit(reduced)[0] - full_ss\n        dft = blocks[t].shape[1]\n        F = (ss / dft) / mse\n        rows.append({\"term\": \" x \".join(t), \"SS\": ss, \"df\": dft, \"F\": F,\n                     \"P\": stats.f.sf(F, dft, dfe), \"eta_p2\": ss / (ss + sse)})\n    table = pd.DataFrame(rows).set_index(\"term\")\n    return {\"table\": table, \"dfe\": int(dfe), \"mse\": mse, \"beta\": beta, \"X\": X, \"terms\": terms,\n            \"levels\": levels, \"factors\": factors, \"n\": len(yv)}\n\n\ndef tukey_kramer(fit: dict, dims: list) -> pd.DataFrame:\n    \"\"\"All pairwise comparisons of population marginal means over `dims` (multcompare).\"\"\"\n    levels, terms = fit[\"levels\"], fit[\"terms\"]\n    combos = list(itertools.product(*[levels[f] for f in dims]))\n    L = []\n    for combo in combos:\n        setting = dict(zip(dims, combo))\n        row = [1.0]\n        for t in terms:\n            if all(f in setting for f in t):\n                vecs = []\n                for f in t:\n                    lv = levels[f]\n                    v = np.zeros(len(lv) - 1)\n                    k = lv.index(setting[f])\n                    if k < len(lv) - 1:\n                        v[k] = 1.0\n                    else:\n                        v[:] = -1.0\n                    vecs.append(v)\n                out = vecs[0]\n                for v in vecs[1:]:\n                    out = np.outer(out, v).ravel()\n                row.extend(out)\n            else:\n                row.extend(np.zeros(np.prod([len(levels[f]) - 1 for f in t])))\n        L.append(row)\n    L = np.array(L)\n    XtX_inv = np.linalg.pinv(fit[\"X\"].T @ fit[\"X\"])\n    means = L @ fit[\"beta\"]\n    cov = L @ XtX_inv @ L.T * fit[\"mse\"]\n    k = len(combos)\n    out = []\n    for i, j in itertools.combinations(range(k), 2):\n        d = means[i] - means[j]\n        se = np.sqrt(cov[i, i] + cov[j, j] - 2 * cov[i, j])\n        q = abs(d) / se * np.sqrt(2)\n        p = stats.studentized_range.sf(q, k, fit[\"dfe\"])\n        out.append({**{f\"A_{f}\": a for f, a in zip(dims, combos[i])},\n                    **{f\"B_{f}\": b for f, b in zip(dims, combos[j])},\n                    \"A_mean\": means[i], \"B_mean\": means[j], \"A_minus_B\": d, \"P\": p})\n    return pd.DataFrame(out)\n\n\ndef prepost_pairs(tk: pd.DataFrame, by: str, prepost: str = \"prepost\") -> pd.DataFrame:\n    \"\"\"The pre against post comparison of each side and `by` level from `tukey_kramer`.\"\"\"\n    m = tk[(tk[f\"A_{prepost}\"] == 1) & (tk[f\"B_{prepost}\"] == 2)\n           & (tk[\"A_side\"] == tk[\"B_side\"]) & (tk[f\"A_{by}\"] == tk[f\"B_{by}\"])]\n    m = m.rename(columns={\"A_side\": \"side\", f\"A_{by}\": by, \"A_mean\": \"pre\", \"B_mean\": \"post\"})\n    m[\"post_minus_pre\"] = -m[\"A_minus_B\"]\n    return m[[\"side\", by, \"pre\", \"post\", \"post_minus_pre\", \"P\"]].reset_index(drop=True)\n\n\ndef three_way_terms(mk: str | None, a: str, b: str, c: str, full_monkey: bool = False) -> list:\n    \"\"\"`model_mat2` of the scripts: monkey main effect plus a full factorial of a, b, c.\"\"\"\n    t = [(a,), (b,), (c,), (a, b), (a, c), (b, c), (a, b, c)]\n    return ([(mk,)] if mk else []) + t\n"
}
```

```
File created successfully at: entries/001773-fujimoto-2026/dbs.py (file state is current in your context — no need to Read it back)
```

**Agent**

Testing the helper on the whole-tract FA model (expected F(1,3187) = 4.64, stimulated CB Tukey P = 0.022):

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; sed -i 's/def three_way_terms(mk: str | None, a: str, b: str, c: str, full_monkey: bool = False) -> list:/def three_way_terms(mk: str | None, a: str, b: str, c: str) -> list:/' dbs.py; . $TMPDIR/expl/bin/activate; time python - <<'EOF' 2>&1 | grep -v Warn
import dbs, pandas as pd
pd.set_option('display.width',200)
d=dbs.fa_wholetract(); print(d.shape)
f=dbs.anova(d,'FA',['mk','prepost','side','tract'],dbs.three_way_terms('mk','prepost','side','tract'))
print(f['table'], f['dfe'])
tk=dbs.tukey_kramer(f,['prepost','side','tract']); print(len(tk)); print(dbs.prepost_pairs(tk,'tract'))
f2=dbs.anova(d,'FA',['mk','prepost','side','tract'],dbs.three_way_terms('mk','prepost','side','tract'),sstype=2); print(f2['table'])
EOF
```

```
(3200, 5)
                              SS  df          F             P    eta_p2
term                                                                   
mk                      0.671915   1  21.871392  3.036638e-06  0.006816
prepost                 0.001113   1   0.036213  8.490884e-01  0.000011
side                    0.100366   1   3.266991  7.078141e-02  0.001024
tract                   1.737620   2  28.280487  6.693532e-13  0.017438
prepost x side          0.142697   1   4.644908  3.122047e-02  0.001455
prepost x tract         0.320381   2   5.214335  5.484539e-03  0.003262
side x tract            0.477398   2   7.769846  4.303271e-04  0.004852
prepost x side x tract  0.002994   2   0.048724  9.524447e-01  0.000031 3187
66
   side  tract       pre      post  post_minus_pre         P
0     1      1  0.323969  0.368725        0.044755  0.022273
1     1      2  0.376612  0.382406        0.005794  1.000000
2     1      3  0.373378  0.364386       -0.008991  1.000000
3     2      1  0.299812  0.308977        0.009164  0.999919
4     2      2  0.362961  0.340986       -0.021975  0.869329
5     2      3  0.418483  0.381686       -0.036797  0.863025
                              SS  df          F             P    eta_p2
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; . $TMPDIR/expl/bin/activate; time python - <<'EOF' 2>&1 | grep -v Warn
import dbs, pandas as pd, numpy as np
from scipy import stats
pd.set_option('display.width',200)
T=dbs.three_way_terms
# behavior
b=dbs.behavior(); nt=b[b.mk<3]
for y in ['movement','foraging']:
    for terms in ([('mk',),('stim',),('mk','stim')],[('mk',),('stim',)]):
        f=dbs.anova(nt,y,['mk','stim'],terms); print(y, f['table'].loc['stim'].round(5).to_dict(), f['dfe'])
    D=b[b.mk==3]; f=dbs.anova(D,y,['stim'],[('stim',)]); print('D',y,f['table'].round(4).to_dict('records'), D.groupby('stim')[y].mean().tolist())
# subpart
s=dbs.fa_subpart(); f=dbs.anova(s,'FA',['mk','prepost','side','part'],T('mk','prepost','side','part')); print(f['table'].loc['prepost x side'].round(5).to_dict(), f['dfe'])
print(dbs.prepost_pairs(dbs.tukey_kramer(f,['prepost','side','part']),'part'))
print(s.groupby(['side','part','mk','prepost']).size().unstack([2,3]))
# mk D
w=dbs.fa_wholetract_mkD(); f=dbs.anova(w,'FA',['prepost','side','tract'],T(None,'prepost','side','tract')); print(f['table'].round(5), f['dfe'])
print(dbs.prepost_pairs(dbs.tukey_kramer(f,['prepost','side','tract']),'tract'))
s=dbs.fa_subpart_mkD(); f=dbs.anova(s,'FA',['prepost','side','part'],T(None,'prepost','side','part')); print(f['table'].round(5), f['dfe'])
print(dbs.prepost_pairs(dbs.tukey_kramer(f,['prepost','side','part']),'part'))
# CC1
for r in ['MCC_CB','dACC_CB','UF-FMoverlap']:
    c=dbs.cc1(r)
    for y in ['ratio','CC1','DAPI']:
        f=dbs.anova(c,y,['mk','side'],[('mk',),('side',),('mk','side')]); print(r,y,f['table'].loc['side'].round(4).to_dict(), f['dfe'], c.groupby(['mk','side'])[y].mean().round(2).tolist())
g=dbs.gratio(); f=dbs.anova(g,'g',['mk','side'],[('mk',),('side',),('mk','side')]); print('g',f['table'].loc['side'].round(5).to_dict(),f['dfe'])
dd=dbs.cc1_mkD(); print(stats.ttest_rel(dd.ratio_leadside, dd.ratio_controlside))
EOF
```

```
warn(msg)
  warn(msg)
movement {'SS': 6.3375, 'df': 1.0, 'F': 34.60818, 'P': 0.0, 'eta_p2': 0.12789} 236
movement {'SS': 6.3375, 'df': 1.0, 'F': 33.81268, 'P': 0.0, 'eta_p2': 0.12486} 237
D movement [{'SS': 0.4083, 'df': 1, 'F': 1.8592, 'P': 0.1753, 'eta_p2': 0.0155}] [0.38333333333333336, 0.26666666666666666]
foraging {'SS': 1.35, 'df': 1.0, 'F': 17.34664, 'P': 4e-05, 'eta_p2': 0.06847} 236
foraging {'SS': 1.35, 'df': 1.0, 'F': 16.46398, 'P': 7e-05, 'eta_p2': 0.06496} 237
D foraging [{'SS': 0.5333, 'df': 1, 'F': 5.3183, 'P': 0.0228, 'eta_p2': 0.0431}] [0.18333333333333332, 0.05]
{'SS': 0.14562, 'df': 1.0, 'F': 5.42303, 'P': 0.02002, 'eta_p2': 0.00398} 1357
   side  part       pre      post  post_minus_pre         P
0     1     1  0.264653  0.308867        0.044214  0.991016
1     1     2  0.321540  0.336122        0.014582  0.999996
2     1     3  0.415549  0.550632        0.135083  0.001766
3     1     4  0.416931  0.464063        0.047133  0.909483
4     2     1  0.256226  0.256025       -0.000201  1.000000
5     2     2  0.278932  0.277981       -0.000951  1.000000
6     2     3  0.346387  0.396499        0.050112  0.979118
7     2     4  0.354363  0.368194        0.013831  1.000000
mk          1        2     
prepost     1   2    1    2
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; . $TMPDIR/expl/bin/activate; time python - <<'EOF' 2>&1 | grep -v -i Warn
import dbs, pandas as pd, numpy as np
pd.set_option('display.width',200); pd.set_option('display.max_rows',100)
T=dbs.three_way_terms; lab=dbs.roi_labels()
fc=dbs.seed_fc('mkNT')
f=dbs.anova(fc,'fc',['subject','time_condition','side','roi'],T('subject','time_condition','side','roi')); print(f['table'].round(6), f['dfe'])
import time; t=time.time()
tk=dbs.tukey_kramer(f,['time_condition','side','roi']); print('tk s',time.time()-t, len(tk))
pp=dbs.prepost_pairs(tk,'roi','time_condition'); pp['name']=pp.roi.map(lab); print(pp)
for lim in (True,False):
    nd=dbs.network_data(fc,lim)
    f=dbs.anova(nd,'fc',['subject','time_condition','side','network'],T('subject','time_condition','side','network')); print(f['table'].loc['time_condition x side'].to_dict(), f['dfe'])
    print(dbs.prepost_pairs(dbs.tukey_kramer(f,['time_condition','side','network']),'network','time_condition'))
EOF
```

```
quad_r = quad(f, low, high, args=args, full_output=self.full_output,
  quad_r = quad(f, low, high, args=args, full_output=self.full_output,
  quad_r = quad(f, low, high, args=args, full_output=self.full_output,
                                    SS  df            F    P    eta_p2
term                                                                  
subject                       0.049789   1    28.581087  0.0  0.001407
time_condition                0.990841   1   568.781187  0.0  0.027283
side                          1.823925   1  1047.002935  0.0  0.049095
roi                          24.161931  16   866.867465  0.0  0.406159
time_condition x side         0.324849   1   186.475926  0.0  0.009112
time_condition x roi          6.855998  16   245.975431  0.0  0.162530
side x roi                    4.993525  16   179.154723  0.0  0.123846
time_condition x side x roi   0.649625  16    23.306868  0.0  0.018057 20279
tk s 26.118038654327393 2278
    side  roi  ...             P                    name
0      1    1  ...  4.497591e-11                     PCC
1      1    2  ...  1.356515e-11                    vmFC
2      1    3  ...  1.356515e-11                     STG
3      1    4  ...  6.790466e-08  Anterior-dorsal Insula
4      1    5  ...  4.877844e-04                    dACC
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; python - <<'EOF'
s=open('dbs.py').read()
s=s.replace('''def tukey_kramer(fit: dict, dims: list) -> pd.DataFrame:
    """All pairwise comparisons of population marginal means over `dims` (multcompare)."""''','''def tukey_kramer(fit: dict, dims: list, only_vary: str | None = None) -> pd.DataFrame:
    """Pairwise comparisons of population marginal means over `dims` (multcompare).

    The family is all pairs of the cells of `dims`, which sets the studentized range's number
    of means; `only_vary` returns only the pairs that differ in that factor alone (the pre
    against post pairs), which is faster and gives the same P values for those pairs.
    """''')
s=s.replace('''    for i, j in itertools.combinations(range(k), 2):
        d = means[i] - means[j]''','''    for i, j in itertools.combinations(range(k), 2):
        if only_vary is not None:
            diff = [f for f, a, b in zip(dims, combos[i], combos[j]) if a != b]
            if diff != [only_vary]:
                continue
        d = means[i] - means[j]''')
open('dbs.py','w').write(s)
EOF
. $TMPDIR/expl/bin/activate; time python - <<'EOF' 2>&1 | grep -v -i "Warn\|quad"
import dbs, pandas as pd, numpy as np
from scipy import stats
pd.set_option('display.width',200); pd.set_option('display.max_rows',100)
T=dbs.three_way_terms; lab=dbs.roi_labels()
fc=dbs.seed_fc('mkD')
f=dbs.anova(fc,'fc',['time_condition','side','roi'],T(None,'time_condition','side','roi')); print(f['table'].loc['time_condition x side'].to_dict(), f['dfe'])
pp=dbs.prepost_pairs(dbs.tukey_kramer(f,['time_condition','side','roi'],'time_condition'),'roi','time_condition'); pp['name']=pp.roi.map(lab); print(pp.iloc[:,[0,1,4,5,6]])
nd=dbs.network_data(fc,True); f=dbs.anova(nd,'fc',['time_condition','side','network'],T(None,'time_condition','side','network')); print(f['table'].loc['time_condition x side'].to_dict(), f['dfe'])
print(dbs.prepost_pairs(dbs.tukey_kramer(nd and f,['time_condition','side','network'],'time_condition'),'network','time_condition'))
EOF
```

```
{'SS': 0.003081507690519736, 'df': 1.0, 'F': 4.584833449006978, 'P': 0.03227995250011409, 'eta_p2': 0.00045346866917518966} 10106
    side  roi  post_minus_pre             P                    name
0      1    1       -0.006204  9.999611e-01                     PCC
1      1    2       -0.022895  8.044435e-04                    vmFC
2      1    3       -0.001756  1.000000e+00                     STG
3      1    4        0.018548  3.085560e-01  Anterior-dorsal Insula
4      1    5       -0.000396  1.000000e+00                    dACC
5      1    6        0.001483  1.000000e+00                   DLPFC
6      1    7        0.014921  3.635041e-04                     PPC
7      1    8        0.183515  4.291012e-12                 Area 25
8      1    9       -0.032409  2.500284e-03                 Area 32
9      1   10        0.013082  9.514671e-01                     MCC
10     1   11       -0.026323  7.700240e-05                     HIP
11     1   12       -0.015999  5.171842e-01                     AMY
12     1   13        0.005848  8.002763e-01              Sensory Cx
13     1   14        0.013851  2.112366e-05                Motor Cx
14     1   15        0.027259  1.912535e-05                     SMA
15     1   16       -0.008749  2.441896e-05               Visual Cx
16     1   17        0.030886  1.397047e-02                      MT
17     2    1       -0.003129  1.000000e+00                     PCC
[... 28 more lines not kept]
```

**Agent**

Monkey D matches as well (ROI interaction F = 4.58; sham vmFC P = 8.0e-4 against the paper's 7.83e-4). Now the connectome claims:

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; . $TMPDIR/expl/bin/activate; time python - <<'EOF' 2>&1 | grep -v -i "Warn\|quad"
import dbs, pandas as pd, numpy as np
from scipy import stats
for s in ['Average FC matrix DBS','Average FC matrix CTRL','Sham animal FC matrix']:
    c=dbs.connectomes(s); D=c['diff']; n=len(D); nc=54
    iu=np.triu_indices(nc,1); cort=D[:nc,:nc][iu].mean()
    sub=D[nc:,nc:][np.triu_indices(n-nc,1)].mean()
    roi=np.array([dbs.offdiag(D,i).mean() for i in range(n)])
    print(s, c['titles'], n, 'block cort %.4f sub %.4f | roi-median cort %.4f sub %.4f | frac neg cort %.2f'%(cort,sub,np.median(roi[:nc]),np.median(roi[nc:]), (D[:nc,:nc][iu]<0).mean()))
    for kd in (False,True):
        res={}
        pa=np.array([stats.ranksums(dbs.offdiag(c['pre'],i,kd),dbs.offdiag(c['post'],i,kd)).pvalue for i in range(n)])
        pb=np.array([stats.wilcoxon(dbs.offdiag(D,i,kd)[dbs.offdiag(D,i,kd)!=0] if kd else dbs.offdiag(D,i,kd)).pvalue for i in range(n)])
        pc=np.array([stats.ranksums(dbs.offdiag(D,i,kd),np.zeros(n-1+kd)).pvalue for i in range(n)])
        for nm,p in [('a rank-sum pre/post',pa),('b signed-rank',pb),('code ranksum vs 0',pc)]:
            print('  diag' if kd else '  off', nm, [(p<t).sum() for t in (0.01/122,0.01/123,0.01,0.05/123)])
EOF
```

```
Average FC matrix DBS ['DBS group Pre', 'DBS group post', 'DBS group Post-Pre'] 123 block cort -0.0955 sub 0.0123 | roi-median cort -0.0517 sub 0.0063 | frac neg cort 0.78
  off a rank-sum pre/post [np.int64(11), np.int64(11), np.int64(44), np.int64(18)]
  off b signed-rank [np.int64(60), np.int64(60), np.int64(85), np.int64(68)]
  off code ranksum vs 0 [np.int64(61), np.int64(61), np.int64(78), np.int64(66)]
  diag a rank-sum pre/post [np.int64(10), np.int64(10), np.int64(43), np.int64(17)]
  diag b signed-rank [np.int64(60), np.int64(60), np.int64(85), np.int64(68)]
  diag code ranksum vs 0 [np.int64(61), np.int64(61), np.int64(78), np.int64(62)]
Average FC matrix CTRL ['Control gropu Pre', 'Control group Post', 'Control group Post-Pre'] 123 block cort 0.0012 sub -0.0041 | roi-median cort 0.0010 sub -0.0010 | frac neg cort 0.49
  off a rank-sum pre/post [np.int64(4), np.int64(4), np.int64(15), np.int64(5)]
  off b signed-rank [np.int64(27), np.int64(27), np.int64(49), np.int64(35)]
  off code ranksum vs 0 [np.int64(34), np.int64(34), np.int64(54), np.int64(39)]
  diag a rank-sum pre/post [np.int64(4), np.int64(4), np.int64(15), np.int64(5)]
  diag b signed-rank [np.int64(27), np.int64(27), np.int64(49), np.int64(35)]
  diag code ranksum vs 0 [np.int64(34), np.int64(34), np.int64(54), np.int64(36)]
Sham animal FC matrix ['Sham animal Pre', 'Sham animal Post', 'Sham animal Post-Pre'] 123 block cort -0.0137 sub -0.0354 | roi-median cort -0.0049 sub -0.0216 | frac neg cort 0.51
  off a rank-sum pre/post [np.int64(35), np.int64(35), np.int64(60), np.int64(40)]
  off b signed-rank [np.int64(48), np.int64(48), np.int64(73), np.int64(53)]
  off code ranksum vs 0 [np.int64(54), np.int64(54), np.int64(79), np.int64(61)]
  diag a rank-sum pre/post [np.int64(35), np.int64(35), np.int64(60), np.int64(40)]
  diag b signed-rank [np.int64(48), np.int64(48), np.int64(73), np.int64(53)]
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; . $TMPDIR/expl/bin/activate; python - <<'EOF' 2>&1 | grep -v -i "Warn\|quad"
import dbs, numpy as np
from scipy import stats
mw=lambda a,b: stats.mannwhitneyu(a,b,alternative='two-sided',method='asymptotic',use_continuity=True).pvalue
for s in ['Average FC matrix DBS','Average FC matrix CTRL','Sham animal FC matrix']:
    c=dbs.connectomes(s); D=c['diff']; n=len(D)
    for kd in (False,True):
        pa=np.array([mw(dbs.offdiag(c['pre'],i,kd),dbs.offdiag(c['post'],i,kd)) for i in range(n)])
        pc=np.array([mw(dbs.offdiag(D,i,kd),np.zeros(n-1+kd)) for i in range(n)])
        print(s,kd,'a',[(pa<t).sum() for t in (0.01/122,0.01/123,0.01,0.05/123)],'code',[(pc<t).sum() for t in (0.01/122,0.01/123,0.01,0.05/123)], np.sort(pc)[[60,65,70]] if s.startswith('Av') else '')
EOF
```

```
Average FC matrix DBS False a [np.int64(11), np.int64(11), np.int64(44), np.int64(18)] code [np.int64(62), np.int64(62), np.int64(81), np.int64(69)] [2.06535929e-05 1.54005448e-04 9.28523440e-04]
Average FC matrix DBS True a [np.int64(10), np.int64(10), np.int64(43), np.int64(17)] code [np.int64(62), np.int64(62), np.int64(81), np.int64(69)] [2.15775903e-05 1.59486910e-04 9.54124271e-04]
Average FC matrix CTRL False a [np.int64(4), np.int64(4), np.int64(15), np.int64(5)] code [np.int64(36), np.int64(36), np.int64(56), np.int64(44)] [0.01803195 0.0333066  0.05852093]
Average FC matrix CTRL True a [np.int64(4), np.int64(4), np.int64(15), np.int64(5)] code [np.int64(36), np.int64(36), np.int64(56), np.int64(44)] [0.01829845 0.03371413 0.05910298]
Sham animal FC matrix False a [np.int64(35), np.int64(35), np.int64(60), np.int64(40)] code [np.int64(58), np.int64(58), np.int64(81), np.int64(69)] 
Sham animal FC matrix True a [np.int64(35), np.int64(35), np.int64(60), np.int64(40)] code [np.int64(58), np.int64(58), np.int64(81), np.int64(69)]
```

**Agent calls Bash**

```bash
cd  date -u; grep -n "def check\|error(\|errors.append\|fail(" tools/entry.py | head -80; ls schemas; ls questions | head -3; cat questions/$(ls questions | head -1) | head -30
```

```
Tue Nov  3 16:21:00 UTC 2026
73:    def error(self, where, message: str) -> None:
74:        self.errors.append(f"{where}: {message}")
112:        report.error(path.relative_to(ROOT), problem)
121:        report.error(path.relative_to(ROOT), message)
143:def check(entry_dir: Path) -> Report:
150:        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")
155:        report.error(rel / name, "notebook is not listed in entry.yaml")
157:        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
161:            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")
165:        report.error(rel, "no requirements.in")
167:        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
174:                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")
185:            report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dataset")
188:                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
195:            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
197:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
201:                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
204:                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
224:                    report.error(path.relative_to(ROOT), f"claim {c['id']!r} depends on {other!r}, which is not in the file")
[... 61 more lines not kept]
```

**Agent**

It is 16:21 UTC, so there is plenty of time. Checking the literal-size and path rules:

**Agent calls Bash**

```bash
cd  sed -n 20,70p tools/entry.py; sed -n 312,335p tools/entry.py; python -c "import json;print(json.dumps(json.load(open('schemas/attempt.schema.json'))['properties']['findings'],indent=0)[:1500])"
```

```
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
- no notebook or helper embeds a large literal array or an encoded image, or
  reads a figure from somewhere else.

`run` builds a fresh virtual environment from the lock file and executes each
notebook through a Jupyter kernel installed in that environment, in the entry
directory. The executed copies
go to --output-dir (default: executed/<name>/, which git ignores). A notebook
that takes longer than --max-minutes fails, even if it ran without error.

`handover` builds what a verifier is given in its first round
(docs/protocol.md): the executed notebooks with the conclusions removed (every
markdown cell that begins "**Result:" and everything from the "## Summary"
heading on), the helper modules and the claims files, in
executed/<name>/handover/. Run the entry first.

Requires `uv` on PATH, and `pyyaml`, `jsonschema` and `nbformat` to run this
script itself. The entry's own dependencies come only from its lock file.
"""
[... 93 more lines not kept]
```

**Agent**

Now the notebook. I'll build it with nbformat from a generator script in `$TMPDIR`, run it once, and then write the conclusions against the printed numbers.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\nimport sys\n\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nconclusions = {}\nif len(sys.argv) > 2:\n    import yaml\n    conclusions = yaml.safe_load(open(sys.argv[2]))\n\n\ndef result(cid):\n    if cid in conclusions:\n        md(conclusions[cid])\n\n\nmd(open(\"/tmp/claude-1001/header.md\").read())\n\ncode('''\nimport time\nimport warnings\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport dbs\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)       # openpyxl: unsupported Excel extensions\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)    # scipy quadrature at extreme tails\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_rows\", 200)\npd.set_option(\"display.max_columns\", 30)\nstarted = time.time()\nT = dbs.three_way_terms\nLAB = dbs.roi_labels()\nSIDE = {1: \"stim\", 2: \"control\"}\nprint(f\"dandiset {dbs.DANDISET_ID}, version {dbs.DANDISET_VERSION}\")\n''')\n\nmd('''\n## Data check\n\nThe dandiset holds Excel sheets of derived values and the paper's MATLAB scripts; no images or\ntime series. Each check of the metadata against the values is stated under its output.\n''')\n\ncode('''\nids = dbs.asset_ids()\nimport requests\nlatest = requests.get(f\"{dbs.API}/dandisets/{dbs.DANDISET_ID}/\", timeout=60).json()[\"most_recent_published_version\"][\"version\"]\nurl = f\"{dbs.API}/dandisets/{dbs.DANDISET_ID}/versions/{latest}/assets/?page_size=200\"\nids_latest = {a[\"path\"]: a[\"asset_id\"] for a in requests.get(url, timeout=60).json()[\"results\"]}\nprint(f\"{len(ids)} assets at {dbs.DANDISET_VERSION}; {len(ids_latest)} at the latest published version {latest}\")\nprint(\"same paths and asset ids in both versions:\", ids == ids_latest)\nprint(pd.Series([p.split(\"/\")[0] for p in ids]).value_counts().to_string())\ncodes = {p: dbs.text(p) for p in ids if p.endswith(\".m\")}\nseen = {}\nfor p, t in sorted(codes.items()):\n    seen.setdefault(t, []).append(p.split(\"/\")[-1])\nprint(\"\\\\nScripts deposited more than once (identical text):\")\nfor names in seen.values():\n    if len(names) > 1:\n        print(\"  \", names)\n''', tags=[\"sanity\"])\n\nmd('''\nThe two published versions hold the same 54 assets (same asset ids), so the choice of version\ndoes not change the data. Two scripts are deposited twice under two names, with identical text;\neach is counted once.\n''')\n\ncode('''\nb = dbs.behavior()\nprint(\"Behavior: 10-s bins per monkey (1 N, 2 T, 3 D), condition (stim 0 pre, 1 post) and group:\")\nprint(b.groupby([\"mk\", \"stim\", \"group\"]).agg(bins=(\"sec\", \"size\"), sec_min=(\"sec\", \"min\"), sec_max=(\"sec\", \"max\"),\n      movement=(\"movement\", \"mean\"), foraging=(\"foraging\", \"mean\")).round(3).to_string())\nprint(\"values of movement:\", sorted(b.movement.unique()), \" foraging:\", sorted(b.foraging.unique()))\nlegend = dbs.sheet(\"source_data/dbs_behavior_data_a.xlsx\").iloc[1:6, 9:16]\nprint(\"\\\\nThe sheet's own legend (columns J to P):\")\nprint(legend.to_string(header=False, index=False))\n''', tags=[\"sanity\"])\n\nmd('''\nEach monkey has 60 bins of 10 s (10 to 600 s) per session, as the Methods say. Every value of\nboth behaviors is 0 or 1. The sheet's legend codes foraging as yes 2 and no 1, which no value\nuses; the values are read as for movement (1 yes, 0 no), which gives the Extended Data Fig. 1\nstatistics below. The legend gives group 1 for the DBS group and 0 for a non-stimulation control,\nwhile monkey D's rows carry group 2. Both are recorded as metadata errors.\n''')\n\ncode('''\nfa = dbs.fa_wholetract()\nprint(\"FA whole tract, voxels per monkey (1 N, 2 T), side (1 stim, 2 control), tract (1 CB, 2 UF, 3 FM), pre and post:\")\nprint(fa.groupby([\"side\", \"tract\", \"mk\", \"prepost\"]).size().unstack([2, 3]).to_string())\nprint(\"pooled per side and tract (pre):\", fa[fa.prepost == 1].groupby([\"side\", \"tract\"]).size().to_dict())\nprint(f\"FA range {fa.FA.min():.4f} to {fa.FA.max():.4f}; rows {len(fa)}\")\nsp = dbs.fa_subpart()\nprint(\"\\\\nCB subregions (1 SCC, 2 dACC, 3 MCC, 4 PCC), pooled per side and part (pre):\",\n      sp[sp.prepost == 1].groupby([\"side\", \"part\"]).size().to_dict(), f\"rows {len(sp)}, FA {sp.FA.min():.3f} to {sp.FA.max():.3f}\")\nfaD, spD = dbs.fa_wholetract_mkD(), dbs.fa_subpart_mkD()\nprint(\"monkey D tracts (pre):\", faD[faD.prepost == 1].groupby([\"side\", \"tract\"]).size().to_dict(), f\"rows {len(faD)}\")\nprint(\"monkey D CB subregions (pre):\", spD[spD.prepost == 1].groupby([\"side\", \"part\"]).size().to_dict(), f\"rows {len(spD)}\")\n''', tags=[\"sanity\"])\n\nmd('''\nThe voxel counts match the legends of Fig. 2a (stimulated CB 380, UF 252, FM 105; control 363,\n367, 133), Fig. 2b (stimulated SCC 54, dACC 137, MCC 55, PCC 80; control 81, 158, 50, 72), Fig. 6a\n(sham CB 162, UF 120, FM 64; control 148, 74, 57) and Fig. 6b (sham 44, 58, 23, 16; control 28, 53,\n13, 19), and the rows give the error df of the paper's models (3200, 1374, 1250, 508 values). The\npre and post values of a voxel are paired row by row (the same number of each per cell).\n''')\n\ncode('''\n# Which hemisphere is \"side 1\"? The per-tract voxel sheets (x, y, z, preFA, postFA) name the\n# hemisphere; match their pre FA values with the whole-tract table.\nrows = []\nfor mk, mkname in [(1, \"N\"), (2, \"T\")]:\n    for tract, tname in [(1, \"CB\"), (3, \"FM\")]:\n        for hemi in [\"L\", \"R\"]:\n            v = dbs.sheet(f\"source_data/FA_{tname}_{hemi}_mk{mkname}.xlsx\", header=0)\n            pre = np.round(v.iloc[:, 3].astype(float).values, 6)\n            for side in (1, 2):\n                w = np.round(fa[(fa.mk == mk) & (fa.tract == tract) & (fa.side == side) & (fa.prepost == 1)].FA.values, 6)\n                rows.append({\"monkey\": mkname, \"tract\": tname, \"sheet_hemisphere\": hemi, \"side\": SIDE[side],\n                             \"sheet_voxels\": len(pre), \"table_voxels\": len(w),\n                             \"same_values\": len(pre) == len(w) and bool(np.allclose(np.sort(pre), np.sort(w)))})\nprint(pd.DataFrame(rows).to_string(index=False))\n''', tags=[\"sanity\"])\n\nmd('''\nThe whole-tract table repeats the per-tract voxel sheets; the CB and FM rows above show which\nhemisphere each side is. The paper puts the lead in the left hemisphere of N and the right of T;\na sheet whose values equal the stimulated side should be L for N and R for T.\n''')\n\ncode('''\nfcNT, fcD = dbs.seed_fc(\"mkNT\"), dbs.seed_fc(\"mkD\")\ncnt = fcNT[fcNT.time_condition == 1].groupby([\"roi\", \"side\", \"subject\"]).size().unstack([1, 2])\ncnt.columns = [f\"{SIDE[s]}_{'N' if m == 1 else 'T'}\" for s, m in cnt.columns]\ncnt[\"stim_pooled\"] = cnt.stim_N + cnt.stim_T\ncntD = fcD[fcD.time_condition == 1].groupby([\"roi\", \"side\"]).size().unstack()\ncnt[\"D_side1_left\"], cnt[\"D_side2_right\"] = cntD[1], cntD[2]\ncnt.index = [f\"{r} {LAB[r]}\" for r in cnt.index]\nprint(\"Seed connectivity voxels per target ROI (pre; post has the same counts):\")\nprint(cnt.to_string())\nprint(f\"\\\\nN and T rows {len(fcNT)}, monkey D rows {len(fcD)}; sessions (subject, time, date):\",\n      fcNT.groupby([\"subject\", \"time_condition\", \"date\"]).size().to_dict(), fcD.groupby([\"subject\", \"time_condition\", \"date\"]).size().to_dict())\nfor name, d in [(\"N and T\", fcNT), (\"D\", fcD)]:\n    print(f\"{name}: normalized connectivity {d.fc.min():.4f} to {d.fc.max():.4f}, median {d.fc.median():.4f}\")\nprint(\"voxel coordinates identical between the N and T table and the D table:\",\n      bool(np.allclose(fcNT[[\"x\", \"y\", \"z\"]].values[:len(fcD)], fcD[[\"x\", \"y\", \"z\"]].values)) if len(fcNT) >= len(fcD) else None)\n''', tags=[\"sanity\"])\n\nmd('''\nThe voxel counts per side are the NMT-space left and right counts swapped between N and T, so\nside 1 is each monkey's stimulated hemisphere, as the claims file reads it; pooled over N and T\nthey match the Supplementary Table 8 sums used in the claims (for example DMN below 857 per side),\nand monkey D's left plus right count equals the pooled count of each side. The rows give the error\ndf of the paper's models (20,348 and 10,174 values). The values are all Fisher Z divided by each\nsession's maximum, so most lie near 0 and the largest near 1. The file names say \"concatenated\":\nthe deposited seed maps were computed on concatenated runs, so the per-run reading in the claims\nfile cannot be run and is not needed (see deviations). There are no seed values for the\nnonsurgical controls B, W and H.\n''')\n\ncode('''\nconn = {k: dbs.connectomes(s) for k, s in [(\"DBS\", \"Average FC matrix DBS\"), (\"CTRL\", \"Average FC matrix CTRL\"),\n                                           (\"D\", \"Sham animal FC matrix\")]}\nfor k, c in conn.items():\n    n = len(c[\"pre\"])\n    print(f\"{k}: sheets {c['titles']}, {n} x {n} ROIs; symmetric {all(np.allclose(m, m.T) for m in (c['pre'], c['post'], c['diff']))}; \"\n          f\"diagonal pre {np.unique(np.diag(c['pre']))}, diff {np.unique(np.diag(c['diff']))}; \"\n          f\"max |post - pre - diff| {np.abs(c['post'] - c['pre'] - c['diff']).max():.1e}; \"\n          f\"off-diagonal Z pre {np.min(c['pre'][~np.eye(n, dtype=bool)]):.3f} to {np.max(c['pre'][~np.eye(n, dtype=bool)]):.3f}, \"\n          f\"diff {c['diff'].min():.3f} to {c['diff'].max():.3f}\")\ncirc = dbs.sheet(\"source_data/Source Data FC matrix.xlsx\", sheet_name=\"Circular plot\")\nprint(\"Circular plot sheet: DBS block equals the first 54 x 54 of the DBS difference:\",\n      bool(np.allclose(circ.iloc[1:55, 0:54].astype(float).values, conn[\"DBS\"][\"diff\"][:54, :54])),\n      \"; control block equals the control difference:\",\n      bool(np.allclose(circ.iloc[57:111, 0:54].astype(float).values, conn[\"CTRL\"][\"diff\"][:54, :54])))\n''', tags=[\"sanity\"])\n\nmd('''\nThe connectomes are group averages (DBS: N and T; controls: B, W and H; monkey D alone) of 123\nROIs with no ROI names. The paper's per-ROI legend gives n = 122 values per ROI, which is the\nnumber of other ROIs in a 123-ROI matrix. The circular plot uses the first 54 ROIs, which the\nFig. 4 script takes as the cortical (CHARM) block. No per-monkey connectome is deposited.\n''')\n\ncode('''\ncc = {r: dbs.cc1(r) for r in [\"MCC_CB\", \"dACC_CB\", \"UF-FMoverlap\"]}\nfor r, d in cc.items():\n    g = d.groupby([\"mk\", \"side\"])\n    print(f\"{r}: fields per monkey and side {g.size().to_dict()}; sections per monkey and side {g.section.nunique().to_dict()}; \"\n          f\"ratio {d.ratio.min():.1f} to {d.ratio.max():.1f} %; max |100 CC1/DAPI - ratio| {np.abs(100 * d.CC1 / d.DAPI - d.ratio).max():.2e}\")\nccD = dbs.cc1_mkD()\nprint(f\"monkey D MCC-CB: {len(ccD)} rows, sections {ccD.slide.nunique()}, fields per section {ccD.groupby('slide').size().to_dict()}; \"\n      f\"lead-side ratio {ccD.ratio_leadside.min():.1f} to {ccD.ratio_leadside.max():.1f}, control {ccD.ratio_controlside.min():.1f} to {ccD.ratio_controlside.max():.1f}\")\ngr = dbs.gratio()\nprint(f\"\\\\nEM: {len(gr)} axons; per monkey and side {gr.groupby(['mk', 'side']).size().to_dict()}\")\nprint(\"image labels by monkey and side:\", gr.groupby([\"mk\", \"side\"]).label.agg(lambda s: sorted(set(x[:2] for x in s))).to_dict())\nprint(f\"aspect ratio (long / short diameter) {gr.aspect.min():.3f} to {gr.aspect.max():.3f}; \"\n      f\"max |d_long / d_short - aspect| {np.abs(gr.d_long / gr.d_short - gr.aspect).max():.1e}\")\nd_mean = (gr.d_long + gr.d_short) / 2\nm_mean = (gr.m_thick + gr.m_thin) / 2\nprint(f\"column 'diameter of axon' / mean diameter: {np.median(gr.radius / d_mean):.3f}; \"\n      f\"max |g - d / (d + 2 m)| {np.abs(gr.g - d_mean / (d_mean + 2 * m_mean)).max():.1e}; g {gr.g.min():.3f} to {gr.g.max():.3f}\")\n''', tags=[\"sanity\"])\n\nmd('''\nThe fields match the Methods: 7 fields in each of 4 sections per hemisphere and monkey for the\nMCC-CB and dACC-CB (28, 112 in all), 5 x 4 for the UF/FM overlap (20, 80 in all), and 28 for\nmonkey D, and the ratio column is 100 x CC1 / DAPI. The EM sheet holds 700 axons (181 per side\nin N, 169 in T; the Methods say about 175 per hemisphere and animal), all with aspect ratio below\n2, so the exclusion is already applied. Its column headed \"diameter of axon\" holds half the mean\nof the long and short diameters, and the g-ratio column equals d / (d + 2m) with d the mean\ndiameter and m the mean myelin width, the Methods' definition.\n''')\n\n# ------------------------------------------------------------------ claims\nmd('''\n## ed1-behavior-increase\n\n> After 6 weeks of SCC-DBS, monkeys N and T spent more time moving and more time foraging in the\n> home cage than before, in the same direction in both animals.\n\nANOVA of the binary bins on condition with monkey, as in the FigE1 script (`anovan`, model\n\"full\": monkey, condition and their interaction; reading (a)), and with monkey and condition only\n(reading (b)).\n''')\n\ncode('''\nnt = b[b.mk < 3]\nrows = []\nfor y in [\"movement\", \"foraging\"]:\n    for reading, terms in [(\"a\", [(\"mk\",), (\"stim\",), (\"mk\", \"stim\")]), (\"b\", [(\"mk\",), (\"stim\",)])]:\n        f = dbs.anova(nt, y, [\"mk\", \"stim\"], terms)\n        r = f[\"table\"].loc[\"stim\"]\n        rows.append({\"behavior\": y, \"reading\": reading, \"F\": r.F, \"df\": f\"1,{f['dfe']}\", \"P\": r.P, \"eta_p2\": r.eta_p2})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\\\nProbability per monkey (1 N, 2 T) and condition (0 pre, 1 post):\")\nprint(nt.groupby([\"mk\", \"stim\"])[[\"movement\", \"foraging\"]].mean().unstack().round(3).to_string())\n''', tags=[\"claim:ed1-behavior-increase\"])\nresult(\"ed1-behavior-increase\")\n\nmd('''\n## ed1-monkey-d-no-change\n\n> In the unstimulated lead-implanted monkey D, the amount of movement and foraging did not change\n> between before and 6 weeks after implantation.\n\nThe criterion's test: a one-way ANOVA of monkey D's 120 bins on condition, at P < 0.05. A\ntwo-sided Fisher exact test of the same counts is shown as a variant.\n''')\n\ncode('''\nD = b[b.mk == 3]\nrows = []\nfor y in [\"movement\", \"foraging\"]:\n    f = dbs.anova(D, y, [\"stim\"], [(\"stim\",)])\n    r = f[\"table\"].loc[\"stim\"]\n    tab = pd.crosstab(D.stim, D[y]).reindex(columns=[0, 1], fill_value=0).values\n    rows.append({\"behavior\": y, \"pre\": D[D.stim == 0][y].mean(), \"post\": D[D.stim == 1][y].mean(),\n                 \"post_minus_pre\": D[D.stim == 1][y].mean() - D[D.stim == 0][y].mean(),\n                 \"F\": r.F, \"df\": f\"1,{f['dfe']}\", \"P\": r.P, \"eta_p2\": r.eta_p2, \"fisher_P\": stats.fisher_exact(tab)[1],\n                 \"bins_pre\": int(tab[0, 1]), \"bins_post\": int(tab[1, 1])})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\n''', tags=[\"claim:ed1-monkey-d-no-change\"])\nresult(\"ed1-monkey-d-no-change\")\n\nmd('''\n## fig2a-cb-fa-increase\n\n> After 6 weeks of SCC-DBS, fractional anisotropy (FA) increased in the cingulum bundle of the\n> stimulated hemisphere, with a significant PrePost x side interaction and a significant pre\n> against post difference in the stimulated CB.\n\nModel of the Fig2A script: monkey, PrePost, side, tract, and all interactions of PrePost, side and\ntract; type III sums of squares (`anovan` default), type II as a variant. Tukey-Kramer over the 12\nPrePost x side x tract cells (`multcompare`, Dimension [2 3 4]).\n''')\n\ncode('''\nTRACT = {1: \"CB\", 2: \"UF\", 3: \"FM\"}\nfit_fa = {ss: dbs.anova(fa, \"FA\", [\"mk\", \"prepost\", \"side\", \"tract\"], T(\"mk\", \"prepost\", \"side\", \"tract\"), sstype=ss) for ss in (3, 2)}\nfor ss, f in fit_fa.items():\n    print(f\"type {ss} sums of squares, error df {f['dfe']}:\")\n    print(f[\"table\"].round(5).to_string())\npp_fa = dbs.prepost_pairs(dbs.tukey_kramer(fit_fa[3], [\"prepost\", \"side\", \"tract\"], only_vary=\"prepost\"), \"tract\")\npp_fa[\"side\"], pp_fa[\"tract\"] = pp_fa.side.map(SIDE), pp_fa.tract.map(TRACT)\nprint(\"\\\\nTukey-Kramer, pre against post (population marginal means):\")\nprint(pp_fa.to_string(index=False))\n''', tags=[\"claim:fig2a-cb-fa-increase\"])\nresult(\"fig2a-cb-fa-increase\")\n\nmd('''\n## fig2a-no-change-other-tracts\n\n> FA did not change in the stimulated UF or FM, nor in any of the three tracts of the control\n> hemisphere.\n''')\n\ncode('''\nothers = pp_fa[~((pp_fa.side == \"stim\") & (pp_fa.tract == \"CB\"))]\nprint(others.to_string(index=False))\nprint(\"comparisons with P < 0.05:\", int((others.P < 0.05).sum()), \"of\", len(others))\n''', tags=[\"claim:fig2a-no-change-other-tracts\"])\nresult(\"fig2a-no-change-other-tracts\")\n\nmd('''\n## ed2-cb-both-monkeys\n\n> The FA increase in the stimulated CB was in the same direction in both monkeys.\n''')\n\ncode('''\ncb = fa[(fa.tract == 1)]\nper = cb.groupby([\"side\", \"mk\", \"prepost\"]).FA.mean().unstack()\nper[\"post_minus_pre\"] = per[2] - per[1]\nper[\"voxels\"] = cb[cb.prepost == 1].groupby([\"side\", \"mk\"]).size()\nper.index = [f\"{SIDE[s]} {'N' if m == 1 else 'T'}\" for s, m in per.index]\nprint(per.rename(columns={1: \"pre\", 2: \"post\"}).round(4).to_string())\n''', tags=[\"claim:ed2-cb-both-monkeys\"])\nresult(\"ed2-cb-both-monkeys\")\n\nmd('''\n## fig2b-mcc-cb-fa-increase\n\n> Of the four CB subregions, only the mid-cingulate portion (MCC-CB) of the stimulated hemisphere\n> showed an FA increase, and it did so in both animals.\n\nThe subregion labels are the dataset's (column `part`), and the voxel counts match the legend\n(data check). Model of the Fig2B script, Tukey-Kramer over the 16 cells.\n''')\n\ncode('''\nPART = {1: \"SCC\", 2: \"dACC\", 3: \"MCC\", 4: \"PCC\"}\nfit_sp = {ss: dbs.anova(sp, \"FA\", [\"mk\", \"prepost\", \"side\", \"part\"], T(\"mk\", \"prepost\", \"side\", \"part\"), sstype=ss) for ss in (3, 2)}\nfor ss, f in fit_sp.items():\n    print(f\"type {ss}, error df {f['dfe']}:\", f[\"table\"].loc[\"prepost x side\"].round(5).to_dict())\npp_sp = dbs.prepost_pairs(dbs.tukey_kramer(fit_sp[3], [\"prepost\", \"side\", \"part\"], only_vary=\"prepost\"), \"part\")\npp_sp[\"side\"], pp_sp[\"part\"] = pp_sp.side.map(SIDE), pp_sp.part.map(PART)\nprint(pp_sp.to_string(index=False))\nper = sp.groupby([\"side\", \"part\", \"mk\", \"prepost\"]).FA.mean().unstack()\nper = (per[2] - per[1]).unstack(\"mk\").rename(columns={1: \"N post-pre\", 2: \"T post-pre\"})\nper.index = [f\"{SIDE[s]} {PART[p]}\" for s, p in per.index]\nprint(\"\\\\nMean post minus pre FA per monkey:\")\nprint(per.round(4).to_string())\n''', tags=[\"claim:fig2b-mcc-cb-fa-increase\"])\nresult(\"fig2b-mcc-cb-fa-increase\")\n\nmd('''\n## fig3c-cc1-dapi-ratio\n\n> The proportion of CC1-positive (myelinating oligodendrocyte) cells among DAPI-positive cells in\n> the MCC-CB was higher in the stimulated than in the control hemisphere, in both animals.\n\nFig3CandE5 script: `anovan` model \"full\" on monkey and side (reading (a)); reading (b) without the\ninteraction.\n''')\n\ncode('''\ndef side_anova(d, y):\n    rows = []\n    for reading, terms in [(\"a\", [(\"mk\",), (\"side\",), (\"mk\", \"side\")]), (\"b\", [(\"mk\",), (\"side\",)])]:\n        f = dbs.anova(d, y, [\"mk\", \"side\"], terms)\n        r = f[\"table\"].loc[\"side\"]\n        rows.append({\"measure\": y, \"reading\": reading, \"F\": r.F, \"df\": f\"1,{f['dfe']}\", \"P\": r.P, \"eta_p2\": r.eta_p2})\n    return rows\n\ndef per_monkey(d, y):\n    m = d.groupby([\"mk\", \"side\"])[y].mean().unstack().rename(columns={1: \"stim\", 2: \"control\"})\n    m[\"stim_minus_control\"] = m.stim - m.control\n    m.index = [\"N\" if i == 1 else \"T\" for i in m.index]\n    return m\n\nprint(pd.DataFrame(side_anova(cc[\"MCC_CB\"], \"ratio\")).to_string(index=False))\nprint(per_monkey(cc[\"MCC_CB\"], \"ratio\").round(3).to_string())\n''', tags=[\"claim:fig3c-cc1-dapi-ratio\"])\nresult(\"fig3c-cc1-dapi-ratio\")\n\nmd('''\n## ed5-cc1-count-dapi-unchanged\n\n> In the MCC-CB the number of CC1-positive cells was higher on the stimulated side, while the\n> number of DAPI-positive cells did not differ between hemispheres.\n''')\n\ncode('''\nprint(pd.DataFrame(side_anova(cc[\"MCC_CB\"], \"CC1\") + side_anova(cc[\"MCC_CB\"], \"DAPI\")).to_string(index=False))\nprint(\"CC1:\"); print(per_monkey(cc[\"MCC_CB\"], \"CC1\").round(2).to_string())\nprint(\"DAPI:\"); print(per_monkey(cc[\"MCC_CB\"], \"DAPI\").round(2).to_string())\n''', tags=[\"claim:ed5-cc1-count-dapi-unchanged\"])\nresult(\"ed5-cc1-count-dapi-unchanged\")\n\nmd('''\n## ed6-dacc-ufm-no-oligodendrocyte-change\n\n> Neither the CC1/DAPI ratio nor the numbers of CC1-positive and DAPI-positive cells differed\n> between hemispheres in the anterior (dACC) portion of the CB, nor in the region where the FM and\n> UF overlap.\n''')\n\ncode('''\nrows = []\nfor r in [\"dACC_CB\", \"UF-FMoverlap\"]:\n    for y in [\"ratio\", \"CC1\", \"DAPI\"]:\n        for row in side_anova(cc[r], y):\n            m = per_monkey(cc[r], y)\n            rows.append({\"region\": r, **row, \"N_stim_minus_control\": m.stim_minus_control[\"N\"],\n                         \"T_stim_minus_control\": m.stim_minus_control[\"T\"]})\nres = pd.DataFrame(rows)\nprint(res.round(4).to_string(index=False))\nprint(\"reading (a) comparisons with P < 0.05:\", int((res[res.reading == \"a\"].P < 0.05).sum()), \"of 6\")\n''', tags=[\"claim:ed6-dacc-ufm-no-oligodendrocyte-change\"])\nresult(\"ed6-dacc-ufm-no-oligodendrocyte-change\")\n\nmd('''\n## fig3f-g-ratio-decrease\n\n> The g-ratio of myelinated axons in the MCC-CB was lower in the stimulated than in the control\n> hemisphere, in both animals, meaning thicker myelin.\n\nFig3F script: `anovan` model \"full\" on monkey and side, one g-ratio per axon (the sheet's g-ratio\ncolumn, checked against the Methods' formula in the data check).\n''')\n\ncode('''\nprint(pd.DataFrame(side_anova(gr, \"g\")).to_string(index=False))\nprint(per_monkey(gr, \"g\").round(4).to_string())\nprint(\"axons:\", gr.groupby([\"mk\", \"side\"]).size().to_dict())\n''', tags=[\"claim:fig3f-g-ratio-decrease\"])\nresult(\"fig3f-g-ratio-decrease\")\n\nmd('''\n## fig4a-cortical-down-subcortical-up\n\n> After SCC-DBS, whole-brain functional connectivity between cortical areas decreased and\n> connectivity between subcortical areas increased.\n\nThe deposited DBS group difference connectome (post minus pre, mean of N and T). Cortical ROIs are\nthe first 54 (Fig. 4 script), subcortical the other 69. Reading (a): mean of the off-diagonal\nentries within each block; reading (b): each ROI's mean change to all other ROIs, median over the\nROIs of each block.\n''')\n\ncode('''\ndef blocks(m, nc=dbs.N_CORTICAL):\n    n = len(m)\n    cort = m[:nc, :nc][np.triu_indices(nc, 1)]\n    sub = m[nc:, nc:][np.triu_indices(n - nc, 1)]\n    roi = np.array([dbs.offdiag(m, i).mean() for i in range(n)])\n    return {\"a_cortical_block_mean\": cort.mean(), \"a_subcortical_block_mean\": sub.mean(),\n            \"b_cortical_roi_median\": np.median(roi[:nc]), \"b_subcortical_roi_median\": np.median(roi[nc:]),\n            \"cortical_entries_negative\": (cort < 0).mean(), \"subcortical_entries_negative\": (sub < 0).mean(),\n            \"cortico_subcortical_mean\": m[:nc, nc:].mean(), \"diff_min\": m.min(), \"diff_max\": m.max()}\n\nblock_table = pd.DataFrame({k: blocks(c[\"diff\"]) for k, c in conn.items()})\nprint(block_table.round(4).to_string())\n''', tags=[\"claim:fig4a-cortical-down-subcortical-up\"])\nresult(\"fig4a-cortical-down-subcortical-up\")\n\nmd('''\n## fig4b-roi-changes-counts\n\n> Per ROI, functional connectivity changed significantly between pre and post scans in 69 of the\n> 122 CHARM and SARM ROIs in the DBS group and in 44 of 122 in the nonsurgical control group.\n\nThe criterion's readings: (a) rank-sum of the ROI's pre values against its post values; (b)\nsigned-rank of its changes against zero; thresholds P < 0.01/122 (the same as adjusted P < 0.01)\nand P < 0.01 uncorrected; with and without the ROI's own diagonal. The rank-sum is computed as\nMATLAB `ranksum` does for these sample sizes (normal approximation with tie correction and\ncontinuity correction, `scipy.stats.mannwhitneyu`, method \"asymptotic\"). The Fig. 4 script's own\ntest, `ranksum(changes, zeros(n,1)) < 0.05/nrois` with nrois = 123, is shown as the code's reading;\nwith 0.01/123 too. The tolerance is 62.1 to 75.9 (DBS) and 39.6 to 48.4 (controls).\n''')\n\ncode('''\ndef mw(a, b):\n    return stats.mannwhitneyu(a, b, alternative=\"two-sided\", method=\"asymptotic\", use_continuity=True).pvalue\n\ndef roi_pvalues(c, keep_diag):\n    n = len(c[\"pre\"])\n    out = {}\n    out[\"a rank-sum pre vs post\"] = np.array([mw(dbs.offdiag(c[\"pre\"], i, keep_diag), dbs.offdiag(c[\"post\"], i, keep_diag)) for i in range(n)])\n    out[\"b signed-rank change vs 0\"] = np.array([stats.wilcoxon(dbs.offdiag(c[\"diff\"], i, keep_diag), zero_method=\"wilcox\").pvalue for i in range(n)])\n    out[\"code rank-sum change vs zeros\"] = np.array([mw(dbs.offdiag(c[\"diff\"], i, keep_diag), np.zeros(n - 1 + keep_diag)) for i in range(n)])\n    return out\n\npvals = {}\nrows = []\nfor grp in [\"DBS\", \"CTRL\"]:\n    n = len(conn[grp][\"pre\"])\n    for keep_diag in (False, True):\n        pv = roi_pvalues(conn[grp], keep_diag)\n        pvals[(grp, keep_diag)] = pv\n        for test, p in pv.items():\n            for thr_name, thr in [(\"0.01/122\", 0.01 / 122), (\"0.01 uncorrected\", 0.01), (\"0.01/123\", 0.01 / n), (\"0.05/123 (code)\", 0.05 / n)]:\n                rows.append({\"group\": grp, \"values\": f\"{n - 1 + keep_diag}\" + (\" with diagonal\" if keep_diag else \" off-diagonal\"),\n                             \"test\": test, \"threshold\": thr_name, \"significant\": int((p < thr).sum())})\ncounts = pd.DataFrame(rows).pivot_table(index=[\"values\", \"test\", \"threshold\"], columns=\"group\", values=\"significant\").astype(int)\ncounts[\"DBS_in_tol\"] = counts.DBS.between(62.1, 75.9)\ncounts[\"CTRL_in_tol\"] = counts.CTRL.between(39.6, 48.4)\nprint(counts.to_string())\n''', tags=[\"claim:fig4b-roi-changes-counts\"])\n\ncode('''\np_code = pvals[(\"DBS\", False)][\"code rank-sum change vs zeros\"]\nsig = p_code < 0.05 / 123\nprint(f\"code's reading, DBS: largest P among the significant ROIs {p_code[sig].max():.2e}; smallest P among the others {p_code[~sig].min():.2e}\")\nprint(f\"DBS significant ROIs, cortical {int(sig[:54].sum())} of 54, subcortical {int(sig[54:].sum())} of 69; \"\n      f\"of them with negative mean change {int((sig & (np.array([dbs.offdiag(conn['DBS']['diff'], i).mean() for i in range(123)]) < 0)).sum())}\")\npc = pvals[(\"CTRL\", False)][\"code rank-sum change vs zeros\"]\nprint(f\"code's reading, controls: largest significant P {pc[pc < 0.05 / 123].max():.2e}; smallest P among the others {pc[pc >= 0.05 / 123].min():.2e}\")\n''', tags=[\"claim:fig4b-roi-changes-counts\"])\nresult(\"fig4b-roi-changes-counts\")\n\nmd('''\n## fig4-nonsurgical-no-pattern\n\n> In the nonsurgical control animals, scans 6 to 7 weeks apart showed no systematic pattern of\n> functional connectivity change.\n\nThe measure of fig4a-cortical-down-subcortical-up on the control group's difference connectome\n(column CTRL of the table above).\n''')\n\ncode('''\nprint(block_table[[\"DBS\", \"CTRL\"]].round(4).to_string())\nctrl = block_table.CTRL\nfor r in [\"a\", \"b\"]:\n    k = [\"a_cortical_block_mean\", \"a_subcortical_block_mean\"] if r == \"a\" else [\"b_cortical_roi_median\", \"b_subcortical_roi_median\"]\n    print(f\"reading ({r}): DBS pattern (cortical < 0 and subcortical > 0) present in the controls: {bool(ctrl[k[0]] < 0 and ctrl[k[1]] > 0)}\")\nprint(\"significant ROIs in the controls under the code's reading:\", int((pvals[(\"CTRL\", False)][\"code rank-sum change vs zeros\"] < 0.05 / 123).sum()))\n''', tags=[\"claim:fig4-nonsurgical-no-pattern\"])\nresult(\"fig4-nonsurgical-no-pattern\")\n\nmd('''\n## fig5a-pre-scc-connectivity\n\n> Before stimulation, the SCC was positively connected with vmFC, dACC, PCC, STG, hippocampus,\n> amygdala and DLPFC, and negatively with the insula and somatosensory cortex.\n\nPre-DBS normalized seed connectivity, mean over the ROI's voxels pooled over N and T: (a) in the\nstimulated hemisphere; (b) both hemispheres pooled. Only concatenated-run seed maps are deposited.\n''')\n\ncode('''\nwant = {\"vmFC\": 1, \"dACC\": 1, \"PCC\": 1, \"STG\": 1, \"HIP\": 1, \"AMY\": 1, \"DLPFC\": 1, \"Anterior-dorsal Insula\": -1, \"Sensory Cx\": -1}\nnum = {v: k for k, v in LAB.items()}\npre = fcNT[fcNT.time_condition == 1]\nrows = []\nfor name, sign in want.items():\n    r = num[name]\n    a = pre[(pre.roi == r) & (pre.side == 1)].fc\n    bb = pre[pre.roi == r].fc\n    rows.append({\"roi\": name, \"expected_sign\": sign, \"a_stim_side_mean\": a.mean(), \"b_both_sides_mean\": bb.mean(),\n                 \"N_stim\": pre[(pre.roi == r) & (pre.side == 1) & (pre.subject == 1)].fc.mean(),\n                 \"T_stim\": pre[(pre.roi == r) & (pre.side == 1) & (pre.subject == 2)].fc.mean(),\n                 \"a_match\": np.sign(a.mean()) == sign, \"b_match\": np.sign(bb.mean()) == sign})\nres = pd.DataFrame(rows)\nprint(res.round(4).to_string(index=False))\nprint(\"signs matching: reading (a)\", int(res.a_match.sum()), \"of 9; reading (b)\", int(res.b_match.sum()), \"of 9\")\n''', tags=[\"claim:fig5a-pre-scc-connectivity\"])\nresult(\"fig5a-pre-scc-connectivity\")\n\nmd('''\n## fig5b-scc-decreases\n\n> After SCC-DBS, functional connectivity of the stimulated SCC decreased with vmFC, PCC, STG,\n> hippocampus, amygdala, DLPFC and dACC in the stimulated hemisphere, with a significant PrePost x\n> side interaction.\n\nModel of the Fig5BCandE9 script on the 17 target ROIs: subject, PrePost, side, ROI, and all\ninteractions of PrePost, side and ROI. Tukey-Kramer over the 68 cells. SciPy's studentized range\ntail does not resolve P values below about 1e-11 (MATLAB prints them as 0); such P values are shown\nat that floor.\n''')\n\ncode('''\nfit_roi = {ss: dbs.anova(fcNT, \"fc\", [\"subject\", \"time_condition\", \"side\", \"roi\"], T(\"subject\", \"time_condition\", \"side\", \"roi\"), sstype=ss) for ss in (3, 2)}\nfor ss, f in fit_roi.items():\n    print(f\"type {ss}, error df {f['dfe']}:\")\n    print(f[\"table\"].to_string())\npp_roi = dbs.prepost_pairs(dbs.tukey_kramer(fit_roi[3], [\"time_condition\", \"side\", \"roi\"], only_vary=\"time_condition\"), \"roi\", \"time_condition\")\npp_roi[\"name\"] = pp_roi.roi.map(LAB)\npp_roi[\"side\"] = pp_roi.side.map(SIDE)\nprint(\"\\\\nTukey-Kramer pre against post, 68 cells:\")\nprint(pp_roi.to_string(index=False))\nseven = [\"vmFC\", \"PCC\", \"STG\", \"HIP\", \"AMY\", \"DLPFC\", \"dACC\"]\ns7 = pp_roi[(pp_roi.side == \"stim\") & pp_roi.name.isin(seven)]\nprint(\"\\\\nstimulated side, the seven ROIs: decreases with P < 0.05:\", int(((s7.P < 0.05) & (s7.post_minus_pre < 0)).sum()), \"of 7\")\n''', tags=[\"claim:fig5b-scc-decreases\"])\nresult(\"fig5b-scc-decreases\")\n\nmd('''\n## fig5b-scc-increases\n\n> After SCC-DBS, functional connectivity of the stimulated SCC increased with the anterior-dorsal\n> insula and the somatosensory cortex.\n''')\n\ncode('''\nprint(pp_roi[(pp_roi.side == \"stim\") & pp_roi.name.isin([\"Anterior-dorsal Insula\", \"Sensory Cx\"])].to_string(index=False))\n''', tags=[\"claim:fig5b-scc-increases\"])\nresult(\"fig5b-scc-increases\")\n\nmd('''\n## ed9-control-hemisphere-changes\n\n> Although stimulation was unilateral, SCC functional connectivity also changed in the\n> unstimulated control hemisphere, including vmFC, PCC, anterior-dorsal insula and dACC.\n''')\n\ncode('''\nctl = pp_roi[pp_roi.side == \"control\"]\nprint(ctl.to_string(index=False))\nprint(\"\\\\ncontrol-side ROIs with P < 0.05:\", int((ctl.P < 0.05).sum()), \"of 17:\", ctl[ctl.P < 0.05].name.tolist())\nprint(\"of vmFC, PCC, insula and dACC:\", int((ctl[ctl.name.isin([\"vmFC\", \"PCC\", \"Anterior-dorsal Insula\", \"dACC\"])].P < 0.05).sum()), \"of 4\")\n''', tags=[\"claim:ed9-control-hemisphere-changes\"])\nresult(\"ed9-control-hemisphere-changes\")\n\nmd('''\n## ed9-no-change-motor-mcc\n\n> Connectivity between the stimulated SCC and motor-related regions (primary motor cortex, SMA)\n> and the MCC did not change.\n''')\n\ncode('''\nprint(pp_roi[(pp_roi.side == \"stim\") & pp_roi.name.isin([\"Motor Cx\", \"SMA\", \"MCC\"])].to_string(index=False))\n''', tags=[\"claim:ed9-no-change-motor-mcc\"])\nresult(\"ed9-no-change-motor-mcc\")\n\nmd('''\n## ed7-decreases-both-monkeys\n\n> The reductions in SCC functional connectivity after DBS were consistent across both monkeys.\n''')\n\ncode('''\ns = fcNT[(fcNT.side == 1) & fcNT.roi.isin([num[n] for n in seven])]\nper = s.groupby([\"roi\", \"subject\", \"time_condition\"]).fc.mean().unstack()\nper = (per[2] - per[1]).unstack(\"subject\").rename(columns={1: \"N post-pre\", 2: \"T post-pre\"})\nper.index = [LAB[r] for r in per.index]\nprint(per.round(4).to_string())\nprint(\"negative: N\", int((per[\"N post-pre\"] < 0).sum()), \"of 7; T\", int((per[\"T post-pre\"] < 0).sum()), \"of 7\")\n''', tags=[\"claim:ed7-decreases-both-monkeys\"])\nresult(\"ed7-decreases-both-monkeys\")\n\nmd('''\n## fig5c-dmn-lim-cen-decrease\n\n> After SCC-DBS, functional connectivity of the stimulated SCC with the hubs of the default mode,\n> limbic and central executive networks decreased, with a significant PrePost x side interaction.\n\nNetwork voxels are the hub ROIs' voxels with repeats (Fig5BCandE9 script). LIM under (a) with area\n25 (the script's list and the Fig. 5c n) and (b) without. Tukey-Kramer over the 24 cells.\n''')\n\ncode('''\nNET = {i: k for i, k in enumerate(dbs.NETWORKS, start=1)}\npp_net, fit_net = {}, {}\nfor reading, lim25 in [(\"a\", True), (\"b\", False)]:\n    nd = dbs.network_data(fcNT, lim_with_area25=lim25)\n    for ss in (3, 2):\n        f = dbs.anova(nd, \"fc\", [\"subject\", \"time_condition\", \"side\", \"network\"], T(\"subject\", \"time_condition\", \"side\", \"network\"), sstype=ss)\n        fit_net[(reading, ss)] = f\n        print(f\"LIM reading ({reading}), type {ss}, error df {f['dfe']}:\", f[\"table\"].loc[\"time_condition x side\"].to_dict())\n    p = dbs.prepost_pairs(dbs.tukey_kramer(fit_net[(reading, 3)], [\"time_condition\", \"side\", \"network\"], only_vary=\"time_condition\"), \"network\", \"time_condition\")\n    p[\"side\"], p[\"network\"] = p.side.map(SIDE), p.network.map(NET)\n    p[\"voxels_per_side_pre\"] = [int(((nd.network == list(NET.values()).index(n) + 1) & (nd.side == (1 if s == \"stim\" else 2)) & (nd.time_condition == 1)).sum()) for s, n in zip(p.side, p.network)]\n    pp_net[reading] = p\n    print(p.to_string(index=False))\n''', tags=[\"claim:fig5c-dmn-lim-cen-decrease\"])\nresult(\"fig5c-dmn-lim-cen-decrease\")\n\nmd('''\n## fig5c-smn-increase\n\n> SCC connectivity with the sensorimotor network increased after SCC-DBS, although that network\n> has few direct CB connections.\n''')\n\ncode('''\nfor r, p in pp_net.items():\n    print(f\"LIM reading ({r}):\"); print(p[p.network == \"SMN\"].to_string(index=False))\n''', tags=[\"claim:fig5c-smn-increase\"])\nresult(\"fig5c-smn-increase\")\n\nmd('''\n## fig5c-vis-no-change\n\n> SCC connectivity with the visual network, and with the areas within it, did not change after\n> SCC-DBS.\n''')\n\ncode('''\nfor r, p in pp_net.items():\n    print(f\"LIM reading ({r}), VIS:\"); print(p[p.network == \"VIS\"].to_string(index=False))\nprint(\"\\\\nareas (17-ROI model):\")\nprint(pp_roi[pp_roi.name.isin([\"Visual Cx\", \"MT\"])].to_string(index=False))\n''', tags=[\"claim:fig5c-vis-no-change\"])\nresult(\"fig5c-vis-no-change\")\n\nmd('''\n## fig5c-san-rebalanced\n\n> In the stimulated hemisphere, the salience network as a whole showed no change in connectivity\n> with the stimulated SCC, because its anterior-dorsal insula node increased and its dACC node\n> decreased.\n''')\n\ncode('''\nfor r, p in pp_net.items():\n    print(f\"LIM reading ({r}), SAN:\"); print(p[p.network == \"SAN\"].to_string(index=False))\nprint(\"\\\\nnodes, stimulated side (17-ROI model):\")\nprint(pp_roi[(pp_roi.side == \"stim\") & pp_roi.name.isin([\"Anterior-dorsal Insula\", \"dACC\"])].to_string(index=False))\n''', tags=[\"claim:fig5c-san-rebalanced\"])\nresult(\"fig5c-san-rebalanced\")\n\nmd('''\n## fig6a-monkey-d-cb-fa-decrease\n\n> In the unstimulated lead-implanted monkey D, FA decreased in the CB of the implanted hemisphere\n> and did not change in the other tracts.\n\nFig6A script: the model of fig2a-cb-fa-increase without the monkey term. Side 1 is the lead\n(sham) side, the left hemisphere, as the sheet's legend says.\n''')\n\ncode('''\nfit_faD = {ss: dbs.anova(faD, \"FA\", [\"prepost\", \"side\", \"tract\"], T(None, \"prepost\", \"side\", \"tract\"), sstype=ss) for ss in (3, 2)}\nfor ss, f in fit_faD.items():\n    print(f\"type {ss}, error df {f['dfe']}:\"); print(f[\"table\"].round(5).to_string())\npp_faD = dbs.prepost_pairs(dbs.tukey_kramer(fit_faD[3], [\"prepost\", \"side\", \"tract\"], only_vary=\"prepost\"), \"tract\")\npp_faD[\"side\"], pp_faD[\"tract\"] = pp_faD.side.map({1: \"sham\", 2: \"control\"}), pp_faD.tract.map(TRACT)\nprint(pp_faD.to_string(index=False))\n''', tags=[\"claim:fig6a-monkey-d-cb-fa-decrease\"])\nresult(\"fig6a-monkey-d-cb-fa-decrease\")\n\nmd('''\n## fig6b-monkey-d-dacc-cb-decrease\n\n> In monkey D the CB FA decrease was significant in the dACC portion of the implanted hemisphere,\n> more anterior than and opposite in direction to the MCC-CB increase after stimulation, although\n> reductions were diffuse across the CB.\n''')\n\ncode('''\nfit_spD = {ss: dbs.anova(spD, \"FA\", [\"prepost\", \"side\", \"part\"], T(None, \"prepost\", \"side\", \"part\"), sstype=ss) for ss in (3, 2)}\nfor ss, f in fit_spD.items():\n    print(f\"type {ss}, error df {f['dfe']}:\", f[\"table\"].loc[\"prepost x side\"].round(6).to_dict())\npp_spD = dbs.prepost_pairs(dbs.tukey_kramer(fit_spD[3], [\"prepost\", \"side\", \"part\"], only_vary=\"prepost\"), \"part\")\npp_spD[\"side\"], pp_spD[\"part\"] = pp_spD.side.map({1: \"sham\", 2: \"control\"}), pp_spD.part.map(PART)\nprint(pp_spD.to_string(index=False))\n''', tags=[\"claim:fig6b-monkey-d-dacc-cb-decrease\"])\nresult(\"fig6b-monkey-d-dacc-cb-decrease\")\n\nmd('''\n## fig6c-monkey-d-cc1-no-change\n\n> In monkey D, the CC1/DAPI ratio in the MCC-CB did not differ between the implanted and control\n> hemispheres.\n\nFig6C script: `ttest` of the lead-side against the control-side column, paired by row. Each row\ncarries one section and field number (reading (a)).\n''')\n\ncode('''\nt = stats.ttest_rel(ccD.ratio_leadside, ccD.ratio_controlside)\ndlt = ccD.ratio_leadside - ccD.ratio_controlside\nprint(f\"paired t({t.df}) = {t.statistic:.4f}, P = {t.pvalue:.4f}; mean difference {dlt.mean():.3f} %, Cohen's dz {dlt.mean() / dlt.std(ddof=1):.3f}\")\nu = stats.ttest_ind(ccD.ratio_leadside, ccD.ratio_controlside)\nprint(f\"unpaired variant: t = {u.statistic:.4f}, P = {u.pvalue:.4f}\")\nprint(f\"means: lead side {ccD.ratio_leadside.mean():.2f} %, control {ccD.ratio_controlside.mean():.2f} %; pairs {len(ccD)}\")\n''', tags=[\"claim:fig6c-monkey-d-cc1-no-change\"])\nresult(\"fig6c-monkey-d-cc1-no-change\")\n\nmd('''\n## ed10c-monkey-d-subcortical-decrease\n\n> In monkey D, whole-brain connectivity changes after implantation were less coherent than after\n> SCC-DBS, cortico-cortical changes were mixed, and subcortico-subcortical connectivity decreased,\n> the opposite of the SCC-DBS group.\n''')\n\ncode('''\nprint(block_table[[\"DBS\", \"D\"]].round(4).to_string())\n''', tags=[\"claim:ed10c-monkey-d-subcortical-decrease\"])\nresult(\"ed10c-monkey-d-subcortical-decrease\")\n\nmd('''\n## fig6e-monkey-d-no-network-reduction\n\n> In monkey D the reductions in SCC connectivity with the DMN, LIM and CEN seen after SCC-DBS were\n> not observed.\n\nThe model of fig5c-dmn-lim-cen-decrease on monkey D without the subject term, LIM readings (a) and\n(b); \"not observed\" read as (a) the sham side and (b) both sides.\n''')\n\ncode('''\npp_netD = {}\nfor reading, lim25 in [(\"a\", True), (\"b\", False)]:\n    nd = dbs.network_data(fcD, lim_with_area25=lim25)\n    f = dbs.anova(nd, \"fc\", [\"time_condition\", \"side\", \"network\"], T(None, \"time_condition\", \"side\", \"network\"))\n    print(f\"LIM reading ({reading}), error df {f['dfe']}:\", f[\"table\"].loc[\"time_condition x side\"].to_dict())\n    p = dbs.prepost_pairs(dbs.tukey_kramer(f, [\"time_condition\", \"side\", \"network\"], only_vary=\"time_condition\"), \"network\", \"time_condition\")\n    p[\"side\"], p[\"network\"] = p.side.map({1: \"sham\", 2: \"control\"}), p.network.map(NET)\n    pp_netD[reading] = p\n    print(p.to_string(index=False))\n    for scope, sides in [(\"sham side\", [\"sham\"]), (\"both sides\", [\"sham\", \"control\"])]:\n        q = p[p.network.isin([\"DMN\", \"LIM\", \"CEN\"]) & p.side.isin(sides)]\n        print(f\"  {scope}: significant decreases in DMN, LIM, CEN: {int(((q.P < 0.05) & (q.post_minus_pre < 0)).sum())} of {len(q)}\")\n''', tags=[\"claim:fig6e-monkey-d-no-network-reduction\"])\nresult(\"fig6e-monkey-d-no-network-reduction\")\n\nmd('''\n## ed10d-monkey-d-roi-changes\n\n> Among vmFC, PCC, anterior-dorsal insula and dACC, monkey D showed a significant pre against\n> post difference in SCC connectivity only for the sham-side vmFC and the control-side\n> anterior-dorsal insula.\n''')\n\ncode('''\nfit_roiD = dbs.anova(fcD, \"fc\", [\"time_condition\", \"side\", \"roi\"], T(None, \"time_condition\", \"side\", \"roi\"))\nprint(f\"error df {fit_roiD['dfe']}:\", fit_roiD[\"table\"].loc[\"time_condition x side\"].to_dict())\npp_roiD = dbs.prepost_pairs(dbs.tukey_kramer(fit_roiD, [\"time_condition\", \"side\", \"roi\"], only_vary=\"time_condition\"), \"roi\", \"time_condition\")\npp_roiD[\"name\"], pp_roiD[\"side\"] = pp_roiD.roi.map(LAB), pp_roiD.side.map({1: \"sham\", 2: \"control\"})\nfour = pp_roiD[pp_roiD.name.isin([\"vmFC\", \"PCC\", \"Anterior-dorsal Insula\", \"dACC\"])]\nprint(four.to_string(index=False))\nprint(\"significant (P < 0.05):\", [f\"{s} {n}\" for s, n in zip(four[four.P < 0.05].side, four[four.P < 0.05].name)])\n''', tags=[\"claim:ed10d-monkey-d-roi-changes\"])\nresult(\"ed10d-monkey-d-roi-changes\")\n\nmd(open(\"/tmp/claude-1001/summary.md\").read() if len(sys.argv) > 2 else \"## Summary\\n\\n(to be written)\")\n\ncode('''\nprint(f\"notebook ran in {(time.time() - started) / 60:.1f} min\")\n''')\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, sys.argv[1])\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR; echo "# Reproducing Fujimoto et al. (2026) from dandiset 001773 (draft header)" > header.md; . expl/bin/activate; uv pip install -q nbconvert ipykernel nbformat pyyaml 2>&1|tail -1; cd entries/001773-fujimoto-2026 && python $TMPDIR/build_nb.py $TMPDIR/draft.ipynb && cp $TMPDIR/draft.ipynb ./draft_tmp.ipynb && time jupyter nbconvert --to notebook --execute draft_tmp.ipynb --output $TMPDIR/draft_out.ipynb --ExecutePreprocessor.timeout=1200 2>&1 | tail -3; rm -f draft_tmp.ipynb
```

```
[NbConvertApp] Converting notebook draft_tmp.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 113759 bytes to /tmp/claude-1001/draft_out.ipynb

real	0m30.223s
user	0m15.531s
sys	0m0.494s
```

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import json
nb=json.load(open('draft_out.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='markdown':
        s=''.join(c['source']); 
        if s.startswith('##'): print('\n#####', s.split('\n')[0])
        continue
    for o in c.get('outputs',[]):
        t=''.join(o.get('text','')) or ''.join(o.get('data',{}).get('text/plain',''))
        if o.get('output_type')=='error': t='ERROR '+o['ename']+o['evalue']
        print(t[:6000])
EOF
```

```
<persisted-output>
Output too large (39.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f29fdf87-f731-49ab-9e78-2627f4f5ea55/tool-results/bxjr25nj0.txt

Preview (first 2KB):
dandiset 001773, version 0.260416.1939


##### ## Data check
54 assets at 0.260416.1939; 54 at the latest published version 0.260615.1838
same paths and asset ids in both versions: True
source_data                 34
code                        18
README.md                    1
dataset_description.json     1


Scripts deposited more than once (identical text):
   ['Fig4 Fujimoto_NatNeuro_2026_FCmatrix.m', 'Fig4andE10C_Fujimoto_NatNeuro_2026_FCmatrix.m']
   ['Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m', 'Fig6DandE10Ddbs_FC_25norm_mkD_analysisscript_a.m']

[... 32 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/f29fdf87-f731-49ab-9e78-2627f4f5ea55/tool-results/bxjr25nj0.txt",
 "offset": 40
}
```

```
40	     2      176  176   76   76
41	     3       51   51   54   54
42	2    1      150  150  213  213
43	     2      242  242  125  125
44	     3       67   67   66   66
45	pooled per side and tract (pre): {(1, 1): 380, (1, 2): 252, (1, 3): 105, (2, 1): 363, (2, 2): 367, (2, 3): 133}
46	FA range 0.0000 to 1.0359; rows 3200
47	
48	
49	CB subregions (1 SCC, 2 dACC, 3 MCC, 4 PCC), pooled per side and part (pre): {(1, 1): 54, (1, 2): 137, (1, 3): 55, (1, 4): 80, (2, 1): 81, (2, 2): 158, (2, 3): 50, (2, 4): 72} rows 1374, FA 0.000 to 0.932
50	
51	monkey D tracts (pre): {(1, 1): 162, (1, 2): 120, (1, 3): 64, (2, 1): 148, (2, 2): 74, (2, 3): 57} rows 1250
52	monkey D CB subregions (pre): {(1, 1): 44, (1, 2): 58, (1, 3): 23, (1, 4): 16, (2, 1): 28, (2, 2): 53, (2, 3): 13, (2, 4): 19} rows 508
53	
54	monkey tract sheet_hemisphere    side  sheet_voxels  table_voxels  same_values
55	     N    CB                L    stim           158           218        False
56	     N    CB                L control           158           150        False
57	     N    CB                R    stim            84           218        False
58	     N    CB                R control            84           150        False
59	     N    FM                L    stim            53            51        False
[... 597 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; . $TMPDIR/expl/bin/activate; python - <<'EOF' 2>&1 | grep -v -i warn
import dbs, numpy as np, pandas as pd
d=dbs.cc1('MCC_CB'); d['calc']=100*d.CC1/d.DAPI; d['dev']=d.ratio-d.calc
print(d[np.abs(d.dev)>1e-6].to_string()); print((d.CC1>d.DAPI).sum())
for y in ['ratio','calc']:
    f=dbs.anova(d,y,['mk','side'],[('mk',),('side',),('mk','side')]); print(y, f['table'].loc['side'].round(4).to_dict())
EOF
```

```
CC1   DAPI      ratio  mk  side section  location       calc       dev
86  125.0  353.0  44.918033   2     2    T423         3  35.410765  9.507268
87  138.0  312.0  35.410765   2     2    T423         4  44.230769 -8.820004
2
ratio {'SS': 780.0089, 'df': 1.0, 'F': 8.9964, 'P': 0.0034, 'eta_p2': 0.0769}
calc {'SS': 783.6405, 'df': 1.0, 'F': 9.031, 'P': 0.0033, 'eta_p2': 0.0772}
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; python - <<'EOF'
s=open('build_nb.py').read()
old_md=s[s.index("md('''\nThe whole-tract table repeats"):s.index("code('''\nfcNT, fcD")]
s=s.replace(old_md,"""md('''
The Extended Data Fig. 4 voxel sheets (with coordinates) hold other voxel sets than the whole-tract
table for the CB (158 and 84 voxels in N against 218 and 150), so they do not show the hemisphere
of each side there. The FM sheets do: the control-side FM values of the table are the right FM of N
and the left FM of T, so side 1 is the left hemisphere in N and the right in T, the hemispheres the
paper gives for the leads. This is consistent with side 1 being the stimulated side throughout.
''')

""")
s=s.replace('''print(f"monkey D MCC-CB: {len(ccD)} rows''','''mcc = cc["MCC_CB"]
bad = mcc[np.abs(100 * mcc.CC1 / mcc.DAPI - mcc.ratio) > 1e-6]
print("MCC-CB fields whose ratio is not 100 x CC1 / DAPI:")
print(bad.assign(ratio_from_counts=100 * bad.CC1 / bad.DAPI).to_string())
print("fields with more CC1 than DAPI cells:", {r: int((d.CC1 > d.DAPI).sum()) for r, d in cc.items()})
print(f"monkey D MCC-CB: {len(ccD)} rows''')
s=s.replace('''monkey D, and the ratio column is 100 x CC1 / DAPI.''','''monkey D. The ratio column is 100 x CC1 / DAPI except in two MCC-CB fields of monkey T's control
side (section T423, fields 3 and 4): the ratio of field 4 is the ratio computed from field 3's
counts, and field 3's ratio fits neither. Two MCC-CB fields have more CC1-positive than
DAPI-positive cells, which a ratio of CC1-positive cells among DAPI-positive cells cannot have.
The analyses use the ratio column as the paper's script does; the ratio from the counts is shown
as a variant.''')
s=s.replace('''print(pd.DataFrame(side_anova(cc["MCC_CB"], "ratio")).to_string(index=False))
print(per_monkey(cc["MCC_CB"], "ratio").round(3).to_string())''','''print(pd.DataFrame(side_anova(cc["MCC_CB"], "ratio")).to_string(index=False))
print(per_monkey(cc["MCC_CB"], "ratio").round(3).to_string())
recomputed = cc["MCC_CB"].assign(ratio_from_counts=100 * cc["MCC_CB"].CC1 / cc["MCC_CB"].DAPI)
print("\\nvariant, ratio computed from the counts:")
print(pd.DataFrame(side_anova(recomputed, "ratio_from_counts")).to_string(index=False))''')
open('build_nb.py','w').write(s)
EOF
grep -n "Extended Data Fig. 4 voxel" build_nb.py | head -2
```

```
Tue Nov  3 16:25:06 UTC 2026
147:The Extended Data Fig. 4 voxel sheets (with coordinates) hold other voxel sets than the whole-tract
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/header.md",
 "content": "# Reproducing Fujimoto et al. (2026) from dandiset 001773\n\n**Paper.** Fujimoto S, Fujimoto A, Elorette C, et al. (2026). Deep brain stimulation induces white\nmatter remodeling and functional changes to brain-wide networks. *Nature Neuroscience*.\n[doi:10.1038/s41593-026-02301-4](https://doi.org/10.1038/s41593-026-02301-4). The claims file was\nwritten from the version of record (open access, PMC13337501), with its Methods, Extended Data\nlegends and Supplementary Information.\n\n**Dandiset.** [DANDI:001773](https://dandiarchive.org/dandiset/001773/0.260416.1939), version\n0.260416.1939. This is the version the paper cites in its Code availability statement\n(doi:10.48324/dandi.001773/0.260416.1939), as the claims file gives it. A later version,\n0.260615.1838, holds the same 54 assets with the same asset ids (shown in the data check), so the\nchoice does not change the data.\n\nThe dandiset holds the paper's derived values as Excel sheets (voxel FA, voxel seed connectivity,\ngroup connectomes, cell counts, g-ratios, behavior bins) and its MATLAB analysis scripts. The\nsheets are read into memory from the archive; the analyses follow the scripts (see `dbs.py`). No\nrandom numbers are used anywhere.\n\n| Claim | Tested |\n|---|---|\n| ed1-behavior-increase | tested |\n| ed1-monkey-d-no-change | tested |\n| fig2a-cb-fa-increase | tested |\n| fig2a-no-change-other-tracts | tested |\n| ed2-cb-both-monkeys | tested |\n| fig2b-mcc-cb-fa-increase | tested |\n| fig3c-cc1-dapi-ratio | tested |\n| ed5-cc1-count-dapi-unchanged | tested |\n| ed6-dacc-ufm-no-oligodendrocyte-change | tested |\n| fig3f-g-ratio-decrease | tested |\n| fig4a-cortical-down-subcortical-up | tested |\n| fig4b-roi-changes-counts | tested |\n| fig4c-network-sorted-reduction | blocked: the connectome's 123 ROIs carry no names and no network assignment |\n| fig4-nonsurgical-no-pattern | tested |\n| fig5a-pre-scc-connectivity | tested |\n| fig5b-scc-decreases | tested |\n| fig5b-scc-increases | tested |\n| ed9-control-hemisphere-changes | tested |\n| ed9-no-change-motor-mcc | tested |\n| ed7-decreases-both-monkeys | tested |\n| fig5a-nonsurgical-no-reduction | blocked: no seed maps of the nonsurgical controls and no whole-brain voxel maps |\n| fig5c-dmn-lim-cen-decrease | tested |\n| fig5c-smn-increase | tested |\n| fig5c-vis-no-change | tested |\n| fig5c-san-rebalanced | tested |\n| fig6a-monkey-d-cb-fa-decrease | tested |\n| fig6b-monkey-d-dacc-cb-decrease | tested |\n| fig6c-monkey-d-cc1-no-change | tested |\n| ed10c-monkey-d-subcortical-decrease | tested |\n| fig6d-monkey-d-scc-local-increase | blocked: no whole-brain voxel map of monkey D and no lead location |\n| fig6e-monkey-d-no-network-reduction | tested; blocked because its readings disagree |\n| ed10d-monkey-d-roi-changes | tested |\n"
}
```

```
<tool_use_error>File has not been read yet. Read it first before writing to it.</tool_use_error>
```

**Agent calls Bash**

```bash
rm /tmp/claude-1001/header.md
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/header.md",
 "content": "# Reproducing Fujimoto et al. (2026) from dandiset 001773\n\n**Paper.** Fujimoto S, Fujimoto A, Elorette C, et al. (2026). Deep brain stimulation induces white\nmatter remodeling and functional changes to brain-wide networks. *Nature Neuroscience*.\n[doi:10.1038/s41593-026-02301-4](https://doi.org/10.1038/s41593-026-02301-4). The claims file was\nwritten from the version of record (open access, PMC13337501), with its Methods, Extended Data\nlegends and Supplementary Information.\n\n**Dandiset.** [DANDI:001773](https://dandiarchive.org/dandiset/001773/0.260416.1939), version\n0.260416.1939. This is the version the paper cites in its Code availability statement\n(doi:10.48324/dandi.001773/0.260416.1939), as the claims file gives it. A later version,\n0.260615.1838, holds the same 54 assets with the same asset ids (shown in the data check), so the\nchoice does not change the data.\n\nThe dandiset holds the paper's derived values as Excel sheets (voxel FA, voxel seed connectivity,\ngroup connectomes, cell counts, g-ratios, behavior bins) and its MATLAB analysis scripts. The\nsheets are read into memory from the archive; the analyses follow the scripts (see `dbs.py`). No\nrandom numbers are used anywhere.\n\n| Claim | Tested |\n|---|---|\n| ed1-behavior-increase | tested |\n| ed1-monkey-d-no-change | tested |\n| fig2a-cb-fa-increase | tested |\n| fig2a-no-change-other-tracts | tested |\n| ed2-cb-both-monkeys | tested |\n| fig2b-mcc-cb-fa-increase | tested |\n| fig3c-cc1-dapi-ratio | tested |\n| ed5-cc1-count-dapi-unchanged | tested |\n| ed6-dacc-ufm-no-oligodendrocyte-change | tested |\n| fig3f-g-ratio-decrease | tested |\n| fig4a-cortical-down-subcortical-up | tested |\n| fig4b-roi-changes-counts | tested |\n| fig4c-network-sorted-reduction | blocked: the connectome's 123 ROIs carry no names and no network assignment |\n| fig4-nonsurgical-no-pattern | tested |\n| fig5a-pre-scc-connectivity | tested |\n| fig5b-scc-decreases | tested |\n| fig5b-scc-increases | tested |\n| ed9-control-hemisphere-changes | tested |\n| ed9-no-change-motor-mcc | tested |\n| ed7-decreases-both-monkeys | tested |\n| fig5a-nonsurgical-no-reduction | blocked: no seed maps of the nonsurgical controls and no whole-brain voxel maps |\n| fig5c-dmn-lim-cen-decrease | tested |\n| fig5c-smn-increase | tested |\n| fig5c-vis-no-change | tested |\n| fig5c-san-rebalanced | tested |\n| fig6a-monkey-d-cb-fa-decrease | tested |\n| fig6b-monkey-d-dacc-cb-decrease | tested |\n| fig6c-monkey-d-cc1-no-change | tested |\n| ed10c-monkey-d-subcortical-decrease | tested |\n| fig6d-monkey-d-scc-local-increase | blocked: no whole-brain voxel map of monkey D and no lead location |\n| fig6e-monkey-d-no-network-reduction | tested, and blocked because its readings disagree |\n| ed10d-monkey-d-roi-changes | tested |\n"
}
```

```
File created successfully at: /tmp/claude-1001/header.md (file state is current in your context — no need to Read it back)
```

**Agent**

Now the conclusions, each backed by printed numbers:

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/conclusions.yaml",
 "content": "ed1-behavior-increase: |\n  **Result: reproduced.** Under reading (a), the paper's model, condition gives F(1,236) = 34.61\n  (P = 1.4e-08, partial eta squared 0.128) for movement and F(1,236) = 17.35 (P = 4.4e-05, 0.068)\n  for foraging, the reported values. Under reading (b) both stay significant (F 33.81 and 16.46).\n  The post probability is higher in both monkeys for both behaviors: movement 0.083 to 0.550 (N)\n  and 0.200 to 0.383 (T), foraging 0.033 to 0.050 (N) and 0.017 to 0.300 (T).\ned1-monkey-d-no-change: |\n  **Result: not reproduced.** Movement does not differ (0.383 pre, 0.267 post, F(1,118) = 1.86,\n  P = 0.175), but foraging does: 11 of 60 bins before and 3 of 60 after (0.183 to 0.050,\n  F(1,118) = 5.32, P = 0.023; Fisher exact P = 0.043). The paper reports no test for monkey D, and\n  the change is a decrease, the opposite of the DBS animals.\nfig2a-cb-fa-increase: |\n  **Result: reproduced.** The PrePost x side interaction is F(1,3187) = 4.64, P = 0.031, partial\n  eta squared 0.0015, the reported values (type II: F = 6.34, P = 0.012). The stimulated CB rises\n  from 0.324 to 0.369 (Tukey-Kramer P = 0.022, the reported P).\nfig2a-no-change-other-tracts: |\n  **Result: reproduced.** None of the five other pre against post comparisons has P < 0.05; the\n  smallest is control FM (change -0.037, P = 0.86), and the stimulated UF and FM have P = 1.00.\ned2-cb-both-monkeys: |\n  **Result: reproduced.** Mean stimulated-CB FA rises by 0.019 in N (218 voxels) and 0.079 in T\n  (162 voxels).\nfig2b-mcc-cb-fa-increase: |\n  **Result: reproduced.** PrePost x side F(1,1357) = 5.42, P = 0.020, partial eta squared 0.0040,\n  the reported values (type II: F = 4.03, P = 0.045). The stimulated MCC-CB rises from 0.416 to\n  0.551 (Tukey-Kramer P = 0.0018, the reported 0.0017); no other subregion and side has P < 0.05\n  (smallest 0.91). The MCC-CB change is positive in N (0.081) and T (0.205).\nfig3c-cc1-dapi-ratio: |\n  **Result: reproduced.** Side gives F(1,108) = 9.00, P = 0.0034, partial eta squared 0.077 (the\n  reported values) under reading (a) and F(1,109) = 9.08, P = 0.0032 under (b). The stimulated\n  side is higher in N (80.6 against 75.0 %) and T (55.1 against 50.1 %). With the ratio computed\n  from the counts, F = 9.03, P = 0.0033.\ned5-cc1-count-dapi-unchanged: |\n  **Result: reproduced.** The CC1 count has a side effect, F(1,108) = 6.22, P = 0.014, partial\n  eta squared 0.054 (reading (b): F = 6.17, P = 0.014), higher on the stimulated side in N (306.1\n  against 281.0) and T (186.5 against 178.8). The DAPI count has none (F = 0.55, P = 0.46; (b)\n  P = 0.47).\ned6-dacc-ufm-no-oligodendrocyte-change: |\n  **Result: reproduced.** None of the six reading (a) tests has P < 0.05: dACC-CB ratio P = 0.090,\n  CC1 P = 0.997, DAPI P = 0.27; UF/FM overlap ratio P = 0.23, CC1 P = 0.38, DAPI P = 0.95.\n  Reading (b) gives the same P values to two digits. The F values match the Extended Data Fig. 6\n  legend; the UF/FM DAPI P is 0.9511 here against the legend's 0.9611, with F = 0 in both.\nfig3f-g-ratio-decrease: |\n  **Result: reproduced.** Side gives F(1,696) = 58.98, P = 5.4e-14, partial eta squared 0.078\n  (the reported values); reading (b) F(1,697) = 59.83. The g-ratio is lower on the stimulated\n  side in N (0.600 against 0.684) and T (0.618 against 0.642).\nfig4a-cortical-down-subcortical-up: |\n  **Result: reproduced.** In the DBS group difference connectome the cortical block mean is\n  -0.096 and the subcortical block mean +0.012 (reading (a)); the median ROI change is -0.052 over\n  cortical ROIs and +0.006 over subcortical ROIs (reading (b)). 78% of cortical entries are\n  negative, 40% of subcortical entries.\nfig4b-roi-changes-counts: |\n  **Result: reproduced, resting on an assumption.** The test and threshold of the paper's Fig. 4\n  script, a rank-sum of each ROI's 122 changes against zeros at P < 0.05/123, give 69 ROIs in the\n  DBS group and 44 in the controls, the reported counts (with the diagonal, 69 and 44 as well).\n  None of the readings the criterion names puts both counts in the tolerance: the pre against\n  post rank-sum gives 4 to 44 (DBS) and 4 to 15 (controls), and the signed-rank test 60 to 85 and\n  27 to 49. The code's test at the text's threshold, 0.01/122, gives 62 and 36. The largest P\n  counted as significant is 3.88e-04 in both groups, the largest value in the paper's\n  Supplementary Tables 1 and 2 (3.9e-4), which only the code's threshold (4.07e-04) admits.\nfig4-nonsurgical-no-pattern: |\n  **Result: reproduced.** In the controls the cortical block mean is +0.001 and the subcortical\n  -0.004 (reading (a)), the ROI medians +0.001 and -0.001 (reading (b)); the DBS pattern (cortical\n  negative, subcortical positive) is absent under both. 49% of the controls' cortical entries are\n  negative, against 78% in the DBS group. The code's per-ROI test counts 44 significant ROIs in\n  the controls.\nfig5a-pre-scc-connectivity: |\n  **Result: reproduced.** Before DBS the seven ROIs are positive (vmFC 0.123, STG 0.099, DLPFC\n  0.066, dACC 0.064, AMY 0.042, HIP 0.038, PCC 0.038 in the stimulated hemisphere) and the\n  anterior-dorsal insula (-0.013) and somatosensory cortex (-0.026) negative; 9 of 9 signs match\n  in the stimulated hemisphere and 9 of 9 with both hemispheres pooled.\nfig5b-scc-decreases: |\n  **Result: reproduced.** PrePost x side F(1,20279) = 186.48, P = 2.9e-42, partial eta squared\n  0.0091, the reported values (type II: F = 56.2, P = 6.7e-14). All seven stimulated-side ROIs\n  decrease with P < 0.001: dACC P = 4.9e-04 (reported 4.75e-04), HIP 1.3e-05 (1.19e-05), AMY\n  8.8e-06 (7.70e-06), PCC 4.5e-11, and vmFC, STG and DLPFC at the floor of the computation\n  (1.4e-11; printed as 0 in the paper).\nfig5b-scc-increases: |\n  **Result: reproduced.** The stimulated-side anterior-dorsal insula rises from -0.013 to +0.026\n  (P = 6.8e-08, reported 4.42e-08) and the somatosensory cortex from -0.026 to +0.006 (P at the\n  floor, 1.4e-11; printed as 0).\ned9-control-hemisphere-changes: |\n  **Result: reproduced.** On the control side vmFC, PCC, dACC (decreases) and the anterior-dorsal\n  insula (increase, P = 0.029, reported 0.0293) all have P < 0.05, and 11 of 17 control-side ROIs\n  do, the same 11 ROIs as Supplementary Table 9.\ned9-no-change-motor-mcc: |\n  **Result: reproduced.** Stimulated-side motor cortex P = 0.99992, SMA P = 1.00000 and MCC\n  P = 0.99180 (reported 0.99991, 0.99999 and 0.99183); changes +0.006, -0.002 and -0.014.\ned7-decreases-both-monkeys: |\n  **Result: reproduced.** All seven stimulated-side ROIs decrease in N and in T (7 of 7 each); the\n  smallest decrease is AMY in N (-0.0006).\nfig5c-dmn-lim-cen-decrease: |\n  **Result: reproduced.** With LIM as the script and the Fig. 5c n have it (reading (a), 821\n  voxels), PrePost x side F(1,21967) = 51.09, P = 9.1e-13, partial eta squared 0.0023, the\n  reported values (type II: F = 40.5). Without area 25 (reading (b), 803 voxels) F(1,21895) =\n  61.60. Under both, the stimulated-side DMN, LIM and CEN decrease (by 0.064, 0.025 to 0.029, and\n  0.035) at the floor of the computation (P below 1.7e-11).\nfig5c-smn-increase: |\n  **Result: reproduced.** The stimulated-side SMN rises from -0.017 to +0.003 with P below 1.7e-11\n  under both LIM readings (the control side too, +0.017).\nfig5c-vis-no-change: |\n  **Result: reproduced.** VIS does not change on either side (stimulated P = 1.00; control\n  P = 0.65 with LIM reading (a), 0.23 with (b)), nor do the stimulated-side visual cortex\n  (P = 1.00) and MT (P = 0.999). The control-side MT decreases (P = 1.0e-06, reported 7.85e-7).\nfig5c-san-rebalanced: |\n  **Result: reproduced.** The stimulated-side SAN does not change (+0.0002, P = 1.00 under both\n  LIM readings), while its anterior-dorsal insula node increases (P = 6.8e-08) and its dACC node\n  decreases (P = 4.9e-04). The control-side SAN decreases (P = 6.9e-07, reported 6.20e-07).\nfig6a-monkey-d-cb-fa-decrease: |\n  **Result: reproduced.** The PrePost x side x tract interaction is F(2,1238) = 6.02, P = 0.0025,\n  partial eta squared 0.0096; the F, P and effect size are the reported ones, with 2 numerator df\n  (the legend prints 1). The sham-side CB falls from 0.362 to 0.245 (P = 8.4e-09, reported\n  5.07e-09); none of the five other comparisons has P < 0.05 (smallest control FM, P = 0.088).\nfig6b-monkey-d-dacc-cb-decrease: |\n  **Result: reproduced.** PrePost x side F(1,492) = 24.55, P = 1.0e-06, partial eta squared 0.048,\n  the reported values. The sham-side dACC-CB falls from 0.413 to 0.230 (P = 3.6e-08, reported\n  1.30e-08); the sham-side MCC-CB falls too (-0.115, P = 0.44), so it shows no increase. All four\n  sham-side subregions decrease (by 0.080 to 0.184), the diffuse reduction the statement\n  describes; only the dACC-CB reaches P < 0.05.\nfig6c-monkey-d-cc1-no-change: |\n  **Result: reproduced.** Paired t(27) = -0.9888, P = 0.332, Cohen's dz -0.19, the reported values;\n  the lead side is 58.0 % and the control side 59.9 %. The unpaired variant gives P = 0.47.\ned10c-monkey-d-subcortical-decrease: |\n  **Result: reproduced.** In monkey D's difference connectome the subcortical block mean is\n  -0.035 (reading (a)) and the median subcortical ROI change -0.022 (reading (b)), with 76% of\n  subcortical entries negative, against +0.012 and 40% in the DBS group. Cortical changes are\n  mixed: block mean -0.014, 51% of entries negative (DBS group 78%).\nfig6e-monkey-d-no-network-reduction: |\n  **Result: blocked, the readings disagree.** With LIM as the script has it (with area 25), no\n  sham-side DMN, LIM or CEN comparison is a significant decrease (0 of 3), but on both sides one\n  is: the control-side CEN (-0.009, P = 0.0089, the reported 0.0088). Without area 25 the\n  sham-side LIM decreases (P = 6.9e-04), so the sham-side reading fails too (1 of 3), and on both\n  sides 2 of 6 are decreases. The interaction is F(1,10972) = 7.36, P = 0.0067 (reported). The\n  criterion blocks the claim when its readings disagree.\ned10d-monkey-d-roi-changes: |\n  **Result: reproduced.** PrePost x side F(1,10106) = 4.58, P = 0.032 (reported). Of the eight\n  comparisons, exactly the sham-side vmFC (decrease, P = 8.0e-04, reported 7.83e-04) and the\n  control-side anterior-dorsal insula (increase, P = 1.1e-11) have P < 0.05; the others have\n  P = 0.31 or more.\n"
}
```

```
File created successfully at: /tmp/claude-1001/conclusions.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "Supplementary Table 1\b\|Supplementary Table 2\b" *.txt | cut -c1-200 | head; grep -o "3\.9[0-9]*[eE]-0\?4\|3\.8[0-9]*[eE]-0\?4\|3\.9[0-9]* *[x×] *10 *-4" *.txt | head
```

```
7:pmc Nat Neurosci Nat Neurosci 981 npgopen 9809671 Nature Neuroscience 1097-6256 1546-1726 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC13337501 PMC13337501.1 13337501 133375
421:Supplementary Table 1 
569:Supplementary Table 2
```

**Agent calls Bash**

```bash
cd paper; sed -n 421,440p *.txt | cut -c1-300; sed -n 421,720p *.txt | grep -E "^[0-9.]+E-0?[0-9]+$|^[0-9.]+e-0?[0-9]+$" | sort -g | tail -5
```

```
Supplementary Table 1 
P value for Fig. 4B, DBS group 
 
 
 
Area
p value
area_25
3.7 ×10^-14
PCC
2.2 ×10^-06
RSC
6.8 ×10^-07
area_10
7.0 ×10^-06
STGr
2.2 ×10^-13
STGc
3.3 ×10^-09
area_32
```

**Agent calls Bash**

```bash
cd paper; sed -n 421,720p *.txt | grep -n "×10^-0[45]" | sed 's/ //g' | awk -F'×10\\^' '{print $2, $1}' | sort -k1,1r -k2,2gr | head -8; sed -n 421,720p *.txt | grep -c "×10^"
```

```
-05 240:2.1
-05 236:2.1
-05 226:2.1
-05 218:2.1
-05 200:2.1
-05 180:5.8
-05 164:2.1
-05 162:5.8
113
```

**Agent calls Bash**

```bash
cd paper; sed -n 421,720p *.txt | grep "×10^-04"
```

```
1.5 ×10^-04
1.5 ×10^-04
1.5 ×10^-04
3.9 ×10^-04
3.9 ×10^-04
3.9 ×10^-04
1.5 ×10^-04
3.9 ×10^-04
3.9 ×10^-04
1.5 ×10^-04
3.9 ×10^-04
3.9 ×10^-04
1.5 ×10^-04
3.9 ×10^-04
1.5 ×10^-04
```

**Agent**

The Supplementary Tables list 113 P values (69 + 44) with a largest of 3.9e-4, which matches the code's procedure. Fixing one range in the fig4b conclusion and writing the summary:

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
s=open('conclusions.yaml').read()
s=s.replace("""  post rank-sum gives 4 to 44 (DBS) and 4 to 15 (controls), and the signed-rank test 60 to 85 and
  27 to 49.""","""  post rank-sum gives 10 to 44 (DBS) and 4 to 15 (controls), and the signed-rank test 60 to 85 and
  27 to 49.""")
open('conclusions.yaml','w').write(s)
EOF
grep -n "10 to 44" conclusions.yaml
```

```
56:  post rank-sum gives 10 to 44 (DBS) and 4 to 15 (controls), and the signed-rank test 60 to 85 and
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/summary.md",
 "content": "## Summary\n\n| Claim | Outcome |\n|---|---|\n| ed1-behavior-increase | reproduced |\n| ed1-monkey-d-no-change | not reproduced |\n| fig2a-cb-fa-increase | reproduced |\n| fig2a-no-change-other-tracts | reproduced |\n| ed2-cb-both-monkeys | reproduced |\n| fig2b-mcc-cb-fa-increase | reproduced |\n| fig3c-cc1-dapi-ratio | reproduced |\n| ed5-cc1-count-dapi-unchanged | reproduced |\n| ed6-dacc-ufm-no-oligodendrocyte-change | reproduced |\n| fig3f-g-ratio-decrease | reproduced |\n| fig4a-cortical-down-subcortical-up | reproduced |\n| fig4b-roi-changes-counts | reproduced, resting on an assumption |\n| fig4c-network-sorted-reduction | blocked (methods underspecified) |\n| fig4-nonsurgical-no-pattern | reproduced |\n| fig5a-pre-scc-connectivity | reproduced |\n| fig5b-scc-decreases | reproduced |\n| fig5b-scc-increases | reproduced |\n| ed9-control-hemisphere-changes | reproduced |\n| ed9-no-change-motor-mcc | reproduced |\n| ed7-decreases-both-monkeys | reproduced |\n| fig5a-nonsurgical-no-reduction | blocked (data missing) |\n| fig5c-dmn-lim-cen-decrease | reproduced |\n| fig5c-smn-increase | reproduced |\n| fig5c-vis-no-change | reproduced |\n| fig5c-san-rebalanced | reproduced |\n| fig6a-monkey-d-cb-fa-decrease | reproduced |\n| fig6b-monkey-d-dacc-cb-decrease | reproduced |\n| fig6c-monkey-d-cc1-no-change | reproduced |\n| ed10c-monkey-d-subcortical-decrease | reproduced |\n| fig6d-monkey-d-scc-local-increase | blocked (data missing) |\n| fig6e-monkey-d-no-network-reduction | blocked (methods underspecified) |\n| ed10d-monkey-d-roi-changes | reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\n**How the analysis differs from the paper's.** The tests are those of the paper's MATLAB scripts\nin the dandiset, reimplemented in Python: type III ANOVA with sum-to-zero coding and the scripts'\nmodel terms, Tukey-Kramer on population marginal means, MATLAB's tie-corrected rank-sum. The\nANOVAs give the reported F values to two decimals throughout. The Tukey-Kramer P values agree with\nthe reported ones to about the second digit, and SciPy does not resolve P values below about\n1e-11, which the paper prints as 0. The deposited seed maps come from concatenated runs, so the\nclaims file's per-run reading cannot be run. The per-ROI connectome counts rest on the test and\nthreshold of the paper's Fig. 4 script (rank-sum of the changes against zeros, P < 0.05/123),\nwhich differ from the Methods' \"P < 0.01 with Bonferroni correction\".\n\n**What was found about the dataset.** It holds derived values, not images, and with the paper's\nscripts it supports almost every statistic of the DWI, histology, EM, behavior and seed\nconnectivity analyses. Missing: the nonsurgical controls' seed connectivity, all whole-brain\nvoxel maps, per-monkey connectomes, ROI names for the 123 x 123 connectomes, and the lead\nlocation. Errors: the behavior legend codes foraging as yes 2 and no 1 while the values are 0 and\n1, and gives no group code for monkey D (its rows carry 2); two MCC-CB fields of monkey T carry\nratios that do not match their counts, and two MCC-CB fields have more CC1-positive than\nDAPI-positive cells; the EM column headed \"diameter of axon\" holds half the mean diameter; two\nscripts are deposited twice under different names. The connectomes have 123 ROIs where the paper\nsays 122.\n"
}
```

```
File created successfully at: /tmp/claude-1001/summary.md (file state is current in your context — no need to Read it back)
```

**Agent**

Checking whether the paper lists 122 or 123 ROIs in Supplementary Table 3:

**Agent calls Bash**

```bash
cd paper; grep -n "Supplementary Table [34]" *.txt | head; awk 'NR>=720 && NR<=1400' *.txt | grep -n "Supplementary Table" | head
```

```
<persisted-output>
Output too large (138.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f29fdf87-f731-49ab-9e78-2627f4f5ea55/tool-results/b0ol6x1hs.txt

Preview (first 2KB):
7:pmc Nat Neurosci Nat Neurosci 981 npgopen 9809671 Nature Neuroscience 1097-6256 1546-1726 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC13337501 PMC13337501.1 13337501 13337501 42225897 10.1038/s41593-026-02301-4 2301 1 Article Deep brain stimulation induces white matter remodeling and functional changes to brain-wide networks http://orcid.org/0000-0003-2374-3002 Fujimoto Satoka H. [removed: an e-mail address] 1 2 7 http://orcid.org/0000-0002-1621-2003 Fujimoto Atsushi 1 2 7 http://orcid.org/0000-0001-5735-4369 Elorette Catherine 1 2 Seltzer Adela 1 2 Andraka Emma 1 2 http://orcid.org/0009-0006-4539-9301 Herbert Keondre 1 2 Verma Gaurav 3 4 Janssen William G. M. 1 Fleysher Lazar 4 Folloni Davide 1 2 http://orcid.org/0000-0002-6446-0677 Choi Ki Sueng 3 4 Russ Brian E. 1 5 6 http://orcid.org/0000-0002-1672-2716 Mayberg Helen S. 1 3 http://orcid.org/0000-0002-1411-7555 Rudebeck Peter H. [removed: an e-mail address] 1 2 1 https://ror.org/04a9tmd77 grid.59734.3c 0000 0001 0670 2351 Nash Family Department of Neuroscience and Friedman Brain Institute, Icahn School of Medicine at Mount Sinai, New York, NY USA 2 https://ror.org/04a9tmd77 grid.59734.3c 0000 0001 0670 2351 Lipschultz Center for Cognitive Neuroscience, Icahn School of Medicine at Mount Sinai, New York, NY USA 3 https://ror.org/031e8jz65 grid.430600.1 0000 0004 0431 8956 Nash Family Center for Advanced Circuit Therapeutics, Mount Sinai West Hospital, New York, NY USA 4 https://ror.org/04a9tmd77 grid.59734.3c 0000 0001 0670 2351 BioMedical Engineering and Imaging Institute, Icahn School of Medicine at Mount Sinai, New York, NY USA 5 https://ror.org/01s434164 grid.250263.0 0000 0001 2189 4777 Center for Biomedical Imaging and Neuromodulation, Nathan Kline Institute, Orangeburg, NY USA 6 https
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "^Supplementary Table" *.txt | cut -c1-80;
```

```
421:Supplementary Table 1 
569:Supplementary Table 2 
666:Supplementary Table 3 
927:Supplementary Table 4 
1188:Supplementary Table 5 
1500:Supplementary Table 6 
1704:Supplementary Table 7 
1828:Supplementary Table 8 
1928:Supplementary Table 9 
1989:Supplementary Table 10 
2105:Supplementary Table 11
```

**Agent calls Bash**

```bash
cd paper; sed -n 666,680p *.txt; sed -n 666,926p *.txt | grep -c -E "^-?0\.[0-9]+ *$|^-?[0-9]\.[0-9]+ *$"; sed -n 666,926p *.txt | grep -v -E "^-?[0-9.]+ *$|^ *$" | wc -l
```

```
Supplementary Table 3 
Effect size (rank-biserial correlation, r_rb) for Fig. 4B, DBS group 
 
 
ROI
r_rb
ROI
r_rb
ROI
r_rb
area_25
-0.16393
area_12m/o
-0.10656
MLThal
121
135
```

**Agent**

The extracted table is too garbled to count reliably, so I'll avoid claiming the paper says 122 ROIs and phrase it from the legend's n instead.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
s=open('summary.md').read()
s=s.replace("""scripts are deposited twice under different names. The connectomes have 123 ROIs where the paper
says 122.""","""scripts are deposited twice under different names. The connectomes have 123 ROIs, so each ROI has
122 values, the n of the Fig. 4b legend; the claims file reads that n as the number of ROIs.""")
open('summary.md','w').write(s)
EOF
cd entries/001773-fujimoto-2026 && . $TMPDIR/expl/bin/activate && python $TMPDIR/build_nb.py reproduce_fujimoto_2026.ipynb $TMPDIR/conclusions.yaml && ls
```

```
__pycache__
dbs.py
reproduce_fujimoto_2026.ipynb
```

**Agent**

Adding a note on the protocol's clock check, which has no counterpart in a dataset without time series, then writing entry.yaml, requirements and README:

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
s=open('build_nb.py').read()
s=s.replace("""The dandiset holds Excel sheets of derived values and the paper's MATLAB scripts; no images or
time series. Each check of the metadata against the values is stated under its output.""","""The dandiset holds Excel sheets of derived values and the paper's MATLAB scripts; no images or
time series. Each check of the metadata against the values is stated under its output. With no
time series there is no clock to align; the corresponding check is that the condition labels mean
what the legends say. Side is checked against the hemispheres (voxel sheets with coordinates, the
NMT-space voxel counts, the EM image labels), and pre and post against the session dates of the
seed tables; pre and post cannot be told apart from the values themselves, so those labels are
taken as the sheets give them, which the reproduced statistics are consistent with.""")
open('build_nb.py','w').write(s)
EOF
cd entries/001773-fujimoto-2026; rm -rf __pycache__; . $TMPDIR/expl/bin/activate && python $TMPDIR/build_nb.py reproduce_fujimoto_2026.ipynb $TMPDIR/conclusions.yaml
cat > requirements.in <<'EOF'
numpy
openpyxl
pandas
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 001773-fujimoto-2026
type: reproduction
title: White matter remodeling and network changes after SCC-DBS in macaques (Fujimoto et al. 2026)
description: Tests the findings of Fujimoto, Fujimoto, Elorette et al. (2026) on dandiset 001773, which
  holds the paper's derived values (voxel FA, voxel seed connectivity, group connectomes, CC1 and DAPI
  counts, EM g-ratios, home-cage behavior bins) and its MATLAB scripts. It repeats the paper's ANOVAs,
  Tukey-Kramer tests and rank-sum tests for the stimulated monkeys N and T, the lead-implanted monkey D
  and the nonsurgical controls. The whole-brain voxel maps and the controls' seed connectivity are not
  in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_fujimoto_2026.ipynb
  title: Reproducing Fujimoto et al. (2026) from dandiset 001773
  runtime_minutes: 2
helpers:
- dbs.py
related:
- id: dandi:001773/0.260416.1939
  relation: uses_data
- id: doi:10.1038/s41593-026-02301-4
  relation: reproduces
EOF
python -c "import json;print(json.load(open('schemas/entry.schema.json'))['properties'].keys())"
```

```
dict_keys(['schema_version', 'name', 'type', 'title', 'description', 'license', 'notebooks', 'helpers', 'related'])
```

**Agent calls Bash**

```bash
cd  date -u; . $TMPDIR/expl/bin/activate; uv pip install -q pyyaml jsonschema nbformat 2>&1 | tail -1; python tools/entry.py lock entries/001773-fujimoto-2026 && python tools/entry.py check entries/001773-fujimoto-2026
```

```
Tue Nov  3 16:27:23 UTC 2026
wrote entries/001773-fujimoto-2026/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/expl/bin/activate; time python tools/entry.py all entries/001773-fujimoto-2026 2>&1 | tail -15
```

```
print("
variant, ratio computed from the counts:")
print(pd.DataFrame(side_anova(recomputed, "ratio_from_counts")).to_string(index=False))
------------------


  [36mCell[39m[36m [39m[32mIn[15][39m[32m, line 18[39m
[31m    [39m[31mprint("[39m
          ^
[31mSyntaxError[39m[31m:[39m unterminated string literal (detected at line 18)



0 error(s)
FAIL  reproduce_fujimoto_2026.ipynb  (29 s)

real	0m35.793s
user	0m12.711s
sys	0m2.150s
```

**Agent**

A string escape broke during my edit. Fixing it:

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
s=open('build_nb.py').read()
s=s.replace('print("\nvariant, ratio computed from the counts:")','print()\nprint("variant, ratio computed from the counts:")')
open('build_nb.py','w').write(s)
EOF
grep -n "variant, ratio computed" build_nb.py; cd entries/001773-fujimoto-2026 && . $TMPDIR/expl/bin/activate && python $TMPDIR/build_nb.py reproduce_fujimoto_2026.ipynb $TMPDIR/conclusions.yaml && cd ../.. && time python tools/entry.py all entries/001773-fujimoto-2026 2>&1 | tail -4
```

```
413:print("\nvariant, ratio computed from the counts:")


0 error(s)
FAIL  reproduce_fujimoto_2026.ipynb  (28 s)

real	0m35.115s
user	0m12.580s
sys	0m2.564s
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 408,418p build_nb.py | cat -A | cut -c1-120
```

```
return m$
$
print(pd.DataFrame(side_anova(cc["MCC_CB"], "ratio")).to_string(index=False))$
print(per_monkey(cc["MCC_CB"], "ratio").round(3).to_string())$
recomputed = cc["MCC_CB"].assign(ratio_from_counts=100 * cc["MCC_CB"].CC1 / cc["MCC_CB"].DAPI)$
print("\nvariant, ratio computed from the counts:")$
print(pd.DataFrame(side_anova(recomputed, "ratio_from_counts")).to_string(index=False))$
''', tags=["claim:fig3c-cc1-dapi-ratio"])$
result("fig3c-cc1-dapi-ratio")$
$
md('''$
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -i '413s/print("\\nvariant/print("\\\\nvariant/' build_nb.py; sed -n 413p build_nb.py; cd entries/001773-fujimoto-2026 && . $TMPDIR/expl/bin/activate && python $TMPDIR/build_nb.py reproduce_fujimoto_2026.ipynb $TMPDIR/conclusions.yaml && cd ../.. && time python tools/entry.py all entries/001773-fujimoto-2026 2>&1 | tail -4
```

```
print("\\nvariant, ratio computed from the counts:")
Installed kernelspec registry-001773-fujimoto-2026 in executed/001773-fujimoto-2026/.venv/share/jupyter/kernels/registry-001773-fujimoto-2026
0 error(s)
pass  reproduce_fujimoto_2026.ipynb  (32 s)

real	0m40.086s
user	0m20.978s
sys	0m2.605s
```

**Agent**

The entry passes in 32 s from a clean environment. Confirming the conclusions against the executed copy:

**Agent calls Bash**

```bash
cd  ls executed/001773-fujimoto-2026/; python - <<'EOF'
import json
nb=json.load(open('executed/001773-fujimoto-2026/reproduce_fujimoto_2026.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    out=''.join(''.join(o.get('text','')) or ''.join(o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]))
    if any(t in str(tags) for t in ['fig3c','ed1-monkey','fig4b','fig6e']) or 'MCC-CB fields' in out:
        print(tags, out[:2500]); print('----')
print(''.join(nb['cells'][-1]['outputs'][0]['text']))
EOF
```

```
reproduce_fujimoto_2026.ipynb
result.json
['sanity'] MCC_CB: fields per monkey and side {(1, 1): 28, (1, 2): 28, (2, 1): 28, (2, 2): 28}; sections per monkey and side {(1, 1): 4, (1, 2): 4, (2, 1): 4, (2, 2): 4}; ratio 33.0 to 101.5 %; max |100 CC1/DAPI - ratio| 9.51e+00
dACC_CB: fields per monkey and side {(1, 1): 28, (1, 2): 28, (2, 1): 28, (2, 2): 28}; sections per monkey and side {(1, 1): 4, (1, 2): 4, (2, 1): 4, (2, 2): 4}; ratio 48.9 to 90.7 %; max |100 CC1/DAPI - ratio| 1.42e-14
UF-FMoverlap: fields per monkey and side {(1, 1): 20, (1, 2): 20, (2, 1): 20, (2, 2): 20}; sections per monkey and side {(1, 1): 4, (1, 2): 4, (2, 1): 4, (2, 2): 4}; ratio 51.8 to 90.7 %; max |100 CC1/DAPI - ratio| 1.42e-14
MCC-CB fields whose ratio is not 100 x CC1 / DAPI:
      CC1   DAPI      ratio  mk  side section  location  ratio_from_counts
86  125.0  353.0  44.918033   2     2    T423         3          35.410765
87  138.0  312.0  35.410765   2     2    T423         4          44.230769
fields with more CC1 than DAPI cells: {'MCC_CB': 2, 'dACC_CB': 0, 'UF-FMoverlap': 0}
monkey D MCC-CB: 28 rows, sections 4, fields per section {'D284': 7, 'D294': 7, 'D304': 7, 'D314': 7}; lead-side ratio 37.8 to 74.8, control 42.2 to 78.2

EM: 700 axons; per monkey and side {(1, 1): 181, (1, 2): 181, (2, 1): 169, (2, 2): 169}
image labels by monkey and side: {(1, 1): ['NI'], (1, 2): ['NI'], (2, 1): ['TR'], (2, 2): ['TL']}
aspect ratio (long / short diameter) 0.878 to 1.998; max |d_long / d_short - aspect| 0.0e+00
column 'diameter of axon' / mean diameter: 0.500; max |g - d / (d + 2 m)| 0.0e+00; g 0.277 to 0.858

----
['claim:ed1-monkey-d-no-change'] behavior    pre   post  post_minus_pre      F    df      P  eta_p2  fisher_P  bins_pre  bins_post
movement 0.3833 0.2667         -0.1167 1.8592 1,118 0.1753  0.0155    0.2421        23         16
[... 82 more lines not kept]
```

**Agent**

Outputs match the conclusions. Checking the paper's Data availability statement before recording what is missing:

**Agent calls Bash**

```bash
cd paper; grep -o -i "data availability.\{700\}" *.txt | head -2; grep -o -i "code availability.\{400\}" *.txt | head -2
```

```
Data availability The functional MRI data generated in this study have been deposited in the DANDI database (10.48324/dandi.001773/0.260416.1939). Openly available resources used in this study, such as the NMT atlas, are accessible through the Primate Data and Resource Exchange (PRIME-DRE; https://prime-re.github.io/ ). Source data are provided with this paper. Code availability The custom MATLAB scripts used to analyze the functional MRI data are available in the DANDI database (10.48324/dandi.001773/0.260416.1939). Competing interests H.S.M. and K.S.C. receive consulting fees from Abbott Neuromodulation. S.H.F., A.F., C.E., A.S., E.A., K.H., G.V., W.G.M.J., L.F., D.F., B.E.R. and P.H.R. declare no competin
code availability are available at 10.1038/s41593-026-02301-4. Supplementary information Supplementary Information Supplementary Methods and Tables 1–11. Reporting Summary Source data Source Data Fig. 2 Statistical source data. Source Data Fig. 3 Statistical source data. Source Data Fig. 4 Statistical source data. Source Data Fig. 5 Statistical source data. Source Data Fig. 6 Statistical source data. Source Data E
Code availability The custom MATLAB scripts used to analyze the functional MRI data are available in the DANDI database (10.48324/dandi.001773/0.260416.1939). Competing interests H.S.M. and K.S.C. receive consulting fees from Abbott Neuromodulation. S.H.F., A.F., C.E., A.S., E.A., K.H., G.V., W.G.M.J., L.F., D.F., B.E.R. and P.H.R. declare no competing interests. S.H.F. is also affiliated with the Department of Ne
```

**Agent**

The Data availability statement says the fMRI data are deposited, but the dandiset holds only derived ROI values; I'll record that as missing data. Checking the attempt schema fields:

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required'), list(s['properties']))
o=s['properties']['outcomes']['items']; print(o.get('required'), json.dumps({k:v.get('enum',v.get('type')) for k,v in o['properties'].items()}))
print(json.dumps(s['properties']['provenance'])[:1500]); print(json.dumps(s['properties']['inputs'])[:600])
EOF
sed -n 150,175p attempts/001453-fouke-2025-01.yaml; grep -n "^findings" -A12 attempts/001453-fouke-2025-01.yaml | head -20
```

```
['schema_version', 'id', 'dataset', 'paper', 'date', 'provenance', 'outcomes'] ['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
['claim', 'outcome'] {"claim": "string", "outcome": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "blocked_by": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "too_large", "not_runnable", "other"], "notes": "string", "notebook": "string", "output": "string", "measured": null, "deviations": "array", "assumed": "boolean", "proposed": "object"}
{"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.", "type": "object", "additionalProperties": false, "required": ["platform"], "properties": {"platform": {"description": "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.", "type": "string", "minLength": 1}, "url": {"description": "The run that wrote the record, e.g. https://github.com/<owner>/<repo>/actions/runs/<id>.", "type": "string",
[... 40 more lines not kept]
```

**Agent**

Writing the attempt record:

**Agent calls Write**

```json
{
 "file_path": "attempts/001773-fujimoto-2026-01.yaml",
 "content": "schema_version: 2\nid: 001773-fujimoto-2026-01\ndataset:\n  archive: dandi\n  id: \"001773\"\n  version: 0.260416.1939\n  doi: 10.48324/dandi.001773/0.260416.1939\npaper: doi:10.1038/s41593-026-02301-4\ndate: 2026-11-03\nentry: 001773-fujimoto-2026\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/41671057318\noutcomes:\n- claim: ed1-behavior-increase\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:ed1-behavior-increase\n  measured:\n  - 34.61\n  - 17.35\n  - 0.128\n  - 0.068\n  notes: Under reading (a), the FigE1 script's model (monkey, condition and their interaction),\n    condition gives F(1,236) = 34.61, P = 1.4e-08, partial eta squared 0.128 for movement and\n    F(1,236) = 17.35, P = 4.4e-05, 0.068 for foraging. Reading (b) gives F 33.81 and 16.46, both\n    P below 1e-04. The post probability is higher in N (movement 0.083 to 0.550, foraging 0.033 to\n    0.050) and in T (0.200 to 0.383, 0.017 to 0.300).\n  deviations:\n  - The foraging values are read as 1 yes and 0 no, as for movement; the sheet's legend says yes 2\n    and no 1, which no value uses.\n- claim: ed1-monkey-d-no-change\n  outcome: not_reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:ed1-monkey-d-no-change\n  notes: By the criterion's test, a one-way ANOVA of monkey D's 120 bins on condition, movement\n    does not differ (0.383 pre, 0.267 post, F(1,118) = 1.86, P = 0.175) but foraging does (11 of 60\n    bins before, 3 of 60 after, 0.183 to 0.050, F(1,118) = 5.32, P = 0.023; Fisher exact P =\n    0.043). The paper reports no test for monkey D (its Extended Data Fig. 1 legend analyses only\n    N and T), so the test is the claims file's reading of the Methods applied to one animal. The\n    change in monkey D is a decrease, opposite to the increase of the DBS animals.\n  deviations:\n  - The paper reports no test for monkey D; the criterion applies the Methods' ANOVA to its bins.\n- claim: fig2a-cb-fa-increase\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig2a-cb-fa-increase\n  measured:\n  - 4.64\n  - 0.0015\n  notes: With the Fig2A script's model (monkey, and PrePost, side and tract with all their\n    interactions; type III), PrePost x side F(1,3187) = 4.64, P = 0.031, partial eta squared 0.0015.\n    Type II gives F = 6.34, P = 0.012. The stimulated CB rises from 0.324 to 0.369 (Tukey-Kramer P =\n    0.022, as reported). The voxel counts match the legend exactly.\n  deviations:\n  - The model terms and the Tukey-Kramer family (the 12 PrePost x side x tract cells) are those\n    of the paper's Fig2A script in the dandiset (`anovan` with `model_mat2`, `multcompare` with\n    Dimension [2 3 4]), which the claims file left to the code. Monkey enters as a main effect\n    only, which the claims file's reading also has.\n- claim: fig2a-no-change-other-tracts\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig2a-no-change-other-tracts\n  notes: None of the five comparisons has P < 0.05. Stimulated UF +0.006 (P = 1.00), stimulated FM\n    -0.009 (P = 1.00), control CB +0.009 (P = 1.00), control UF -0.022 (P = 0.87), control FM -0.037\n    (P = 0.86).\n- claim: ed2-cb-both-monkeys\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:ed2-cb-both-monkeys\n  notes: Mean post minus pre FA in the stimulated CB is +0.019 in N (218 voxels) and +0.079 in T\n    (162 voxels). On the control side it is -0.020 in N and +0.030 in T.\n- claim: fig2b-mcc-cb-fa-increase\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig2b-mcc-cb-fa-increase\n  measured:\n  - 5.42\n  - 0.0040\n  notes: PrePost x side F(1,1357) = 5.42, P = 0.020, partial eta squared 0.0040 (type II F = 4.03,\n    P = 0.045). The stimulated MCC-CB rises from 0.416 to 0.551 (Tukey-Kramer P = 0.0018, reported\n    0.0017). No other subregion and side has P < 0.05 (smallest 0.91). The MCC-CB change is\n    positive in N (+0.081) and T (+0.205). The subregions are the dataset's labels, and their voxel\n    counts match the legend.\n  deviations:\n  - Subregions are the labels in the dataset (column `part`), which the criterion says to use; the\n    model is that of the Fig2B script.\n- claim: fig3c-cc1-dapi-ratio\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig3c-cc1-dapi-ratio\n  measured:\n  - 9.00\n  - 0.077\n  notes: Side gives F(1,108) = 9.00, P = 0.0034, partial eta squared 0.077 under reading (a), the\n    Fig3CandE5 script's full model, and F(1,109) = 9.08, P = 0.0032 under (b). The stimulated side is\n    higher in N (80.6 against 75.0 %) and T (55.1 against 50.1 %). Two fields of T's control side\n    carry ratios that do not match their counts; with the ratio computed from the counts F = 9.03,\n    P = 0.0033.\n- claim: ed5-cc1-count-dapi-unchanged\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:ed5-cc1-count-dapi-unchanged\n  measured:\n  - 6.22\n  - 0.054\n  notes: CC1 count side effect F(1,108) = 6.22, P = 0.014, partial eta squared 0.054 (reading (b)\n    F = 6.17, P = 0.014), higher on the stimulated side in N (306.1 against 281.0) and T (186.5\n    against 178.8). DAPI count F(1,108) = 0.55, P = 0.46 (reading (b) P = 0.47).\n- claim: ed6-dacc-ufm-no-oligodendrocyte-change\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:ed6-dacc-ufm-no-oligodendrocyte-change\n  notes: Under reading (a) none of the six tests has P < 0.05. dACC-CB ratio F = 2.93, P = 0.090;\n    CC1 F = 0.00, P = 0.997; DAPI F = 1.22, P = 0.27. UF/FM overlap ratio F = 1.45, P = 0.23; CC1\n    F = 0.79, P = 0.38; DAPI F = 0.00, P = 0.951. Partial eta squared at most 0.026. Reading (b)\n    gives the same P values to two digits. All F values and P values are the legend's, except the\n    UF/FM DAPI P, 0.9511 here and 0.9611 in the legend.\n- claim: fig3f-g-ratio-decrease\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig3f-g-ratio-decrease\n  measured:\n  - 58.98\n  - 0.078\n  notes: Side gives F(1,696) = 58.98, P = 5.4e-14, partial eta squared 0.078 under reading (a), and\n    F(1,697) = 59.83 under (b). The g-ratio is lower on the stimulated side in N (0.600 against\n    0.684, 181 axons per side) and T (0.618 against 0.642, 169 per side). All 700 axons have\n    aspect ratio below 2, and the sheet's g-ratio equals the Methods' formula.\n- claim: fig4a-cortical-down-subcortical-up\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig4a-cortical-down-subcortical-up\n  notes: In the deposited DBS group difference connectome (123 ROIs, cortical the first 54 as in\n    the Fig. 4 script) the cortical block mean is -0.096 and the subcortical block mean +0.012\n    (reading (a)); the median ROI change is -0.052 over cortical ROIs and +0.006 over subcortical\n    ROIs (reading (b)). 78% of cortical and 40% of subcortical entries are negative.\n  deviations:\n  - The connectome is the group average the dandiset holds, not recomputed from runs; its ROIs\n    have no names, and the cortical block is taken from the Fig. 4 script (first 54 ROIs).\n- claim: fig4b-roi-changes-counts\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig4b-roi-changes-counts\n  measured:\n  - 69\n  - 44\n  notes: The paper's Fig. 4 script tests each ROI with `ranksum` of its off-diagonal changes against\n    a vector of zeros, significant at P < 0.05/nrois, with nrois = 123. Computed as MATLAB's\n    ranksum (tie and continuity corrected), this gives 69 ROIs for the DBS group (41 of 54\n    cortical, 28 of 69 subcortical) and 44 for the controls, the reported counts, with or without\n    the diagonal. The largest P counted is 3.88e-04 in both groups, the largest value listed in\n    Supplementary Tables 1 and 2 (3.9e-4), which the text's threshold (0.01/122 = 8.2e-05) would\n    exclude. None of the readings the criterion names puts both counts in tolerance (62.1 to 75.9\n    and 39.6 to 48.4). Pre against post rank-sum gives 10 to 44 (DBS) and 4 to 15 (controls);\n    signed-rank of the changes 60 to 85 and 27 to 49; both over the thresholds 0.01/122 and 0.01\n    uncorrected and with or without the diagonal. The script's test at the text's threshold gives\n    62 and 36. The outcome rests on taking the test and threshold from the script, which a question\n    to a reader asks about (questions/001773.yaml).\n  deviations:\n  - Assumption. The per-ROI test and threshold are those of the paper's Fig. 4 script in the\n    dandiset (rank-sum of the changes against zeros, P < 0.05/123). The Methods and the Fig. 4b\n    legend say \"Rank-sum test ... (P < 0.01 with Bonferroni correction)\" and \"changes ... from\n    zero\"; the script and the paper's Supplementary Tables 1 and 2 agree with each other and\n    not with the 0.01 of the text. The readings the criterion names were all run and none\n    matches.\n  - The matrices have 123 ROIs, so each ROI has 122 values, the n of the legend; the threshold\n    uses 123 as the script does (0.01/122 is also shown).\n- claim: fig4c-network-sorted-reduction\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: The criterion blocks the claim without an assignment of the connectome's ROIs to\n    networks. The dandiset's connectomes (123 x 123) have no ROI names, the Fig. 4 script reads the\n    names from atlas key files that are not deposited (CHARM_key_4.txt, SARM_key_4.txt,\n    reorder_rois.txt), and neither the script nor the paper assigns ROIs to the networks of Fig. 4c.\n    The deposited circular plot sheet holds the 54 x 54 cortical block of each group's difference\n    without network labels.\n- claim: fig4-nonsurgical-no-pattern\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig4-nonsurgical-no-pattern\n  notes: In the controls' difference connectome the cortical block mean is +0.001 and the\n    subcortical -0.004 (reading (a)), the ROI medians +0.001 and -0.001 (reading (b)), so the DBS\n    pattern is absent under both; against DBS values -0.096, +0.012, -0.052 and +0.006. 49% of the\n    controls' cortical entries are negative (DBS 78%). Under the script's per-ROI test the controls\n    have 44 significant ROIs, as the paper lists.\n- claim: fig5a-pre-scc-connectivity\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig5a-pre-scc-connectivity\n  notes: Before DBS, in the stimulated hemisphere, vmFC 0.123, STG 0.099, DLPFC 0.066, dACC 0.064,\n    AMY 0.042, HIP 0.038 and PCC 0.038 are positive, the anterior-dorsal insula -0.013 and the\n    somatosensory cortex -0.026 negative; 9 of 9 signs match, and 9 of 9 with both hemispheres\n    pooled. Each sign is the same in N and T separately.\n  deviations:\n  - Only seed maps from concatenated runs are deposited (the files are named \"concatenated\"), so\n    the per-run reading of the criterion cannot be run; the deposited maps are those the paper's\n    scripts analyse.\n- claim: fig5b-scc-decreases\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig5b-scc-decreases\n  measured:\n  - 186.48\n  - 0.0091\n  notes: With the Fig5BCandE9 script's model, PrePost x side F(1,20279) = 186.48, P = 2.9e-42,\n    partial eta squared 0.0091 (type II F = 56.2, P = 6.7e-14). All seven stimulated-side ROIs\n    decrease with Tukey-Kramer P < 0.001, dACC 4.9e-04 (reported 4.75e-04), HIP 1.3e-05 (1.19e-05),\n    AMY 8.8e-06 (7.70e-06), PCC 4.5e-11 (8.22e-12), vmFC, STG and DLPFC at the floor of SciPy's\n    studentized range (1.4e-11; reported as 0).\n  deviations:\n  - Concatenated-run seed maps only, as for fig5a-pre-scc-connectivity.\n  - SciPy's studentized range tail does not resolve P below about 1e-11, so the smallest P values\n    are shown at that floor; this cannot change an outcome at P < 0.05.\n- claim: fig5b-scc-increases\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig5b-scc-increases\n  notes: The stimulated-side anterior-dorsal insula rises from -0.013 to +0.026 (P = 6.8e-08,\n    reported 4.42e-08), the somatosensory cortex from -0.026 to +0.006 (P at the floor, reported 0).\n- claim: ed9-control-hemisphere-changes\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:ed9-control-hemisphere-changes\n  measured: 11\n  notes: On the control side vmFC (-0.112), PCC (-0.024, P = 5.3e-07), dACC (-0.059) and the\n    anterior-dorsal insula (+0.025, P = 0.029) all have P < 0.05. 11 of 17 control-side ROIs have\n    P < 0.05, the 11 the criterion lists from Supplementary Table 9.\n- claim: ed9-no-change-motor-mcc\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:ed9-no-change-motor-mcc\n  notes: Stimulated-side motor cortex +0.006 (P = 0.99992), SMA -0.002 (P = 1.00000), MCC -0.014\n    (P = 0.99180); the reported P values are 0.99991, 0.99999 and 0.99183.\n- claim: ed7-decreases-both-monkeys\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:ed7-decreases-both-monkeys\n  notes: All seven stimulated-side ROIs decrease in N (7 of 7, -0.0006 for AMY to -0.082 for STG)\n    and in T (7 of 7, -0.024 to -0.103). Concatenated-run maps only.\n- claim: fig5a-nonsurgical-no-reduction\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The test needs the voxelwise seed maps of the nonsurgical controls B, W and H over the\n    whole brain. The dandiset holds seed connectivity only for N, T and D, and only for the voxels\n    of the 17 target ROIs; it has no whole-brain voxel maps, no control seed values and no fMRI\n    images, so neither the cluster test nor the ROI-level variant can be run. The paper's Data\n    availability statement names only this dandiset for the fMRI data.\n- claim: fig5c-dmn-lim-cen-decrease\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig5c-dmn-lim-cen-decrease\n  measured:\n  - 51.09\n  - 0.0023\n  notes: With LIM as the Fig5BCandE9 script has it (with area 25, 821 voxels per side, reading\n    (a)), PrePost x side F(1,21967) = 51.09, P = 9.1e-13, partial eta squared 0.0023 (type II F =\n    40.5). Without area 25 (reading (b), 803 voxels) F(1,21895) = 61.60. Under both, the\n    stimulated-side DMN (-0.064), LIM (-0.025, (b) -0.029) and CEN (-0.035) decrease with P below\n    1.7e-11. The network voxel counts match the legend.\n  deviations:\n  - Network membership is the script's (DMN PCC, vmFC, STG; SAN insula, dACC; CEN DLPFC, PPC; LIM\n    PCC, dACC, area 25, area 32, MCC, HIP, AMY; SMN; VIS). The script settles LIM as reading (a);\n    reading (b) is run as the criterion asks.\n- claim: fig5c-smn-increase\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig5c-smn-increase\n  notes: The stimulated-side SMN rises from -0.017 to +0.003 (P below 1.7e-11 under both LIM\n    readings); the control side rises too (+0.017).\n- claim: fig5c-vis-no-change\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig5c-vis-no-change\n  notes: VIS stimulated side +0.001 (P = 1.00), control side -0.005 (P = 0.65 with LIM reading (a),\n    0.23 with (b)); stimulated-side visual cortex P = 1.00 and MT P = 0.999. The control-side MT\n    decreases (-0.049, P = 1.0e-06, reported 7.85e-07), and the control-side visual cortex does not\n    (P = 1.00).\n- claim: fig5c-san-rebalanced\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig5c-san-rebalanced\n  notes: The stimulated-side SAN changes by +0.0002 (P = 1.00 under both LIM readings), while its\n    anterior-dorsal insula node increases (+0.039, P = 6.8e-08) and its dACC node decreases (-0.024,\n    P = 4.9e-04). The control-side SAN decreases (P = 6.9e-07, reported 6.20e-07).\n- claim: fig6a-monkey-d-cb-fa-decrease\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig6a-monkey-d-cb-fa-decrease\n  measured:\n  - 6.02\n  - 0.0096\n  notes: With the Fig6A script's model, the PrePost x side x tract interaction is F(2,1238) = 6.02,\n    P = 0.0025, partial eta squared 0.0096 (type II the same). The sham-side CB falls from 0.362 to\n    0.245 (P = 8.4e-09, reported 5.07e-09); none of the other five comparisons has P < 0.05\n    (sham UF P = 0.22, sham FM 0.97, control CB 1.00, UF 1.00, FM 0.088).\n  deviations:\n  - The interaction has 2 numerator df, as the claims file reads it; the legend prints 1.\n- claim: fig6b-monkey-d-dacc-cb-decrease\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig6b-monkey-d-dacc-cb-decrease\n  measured:\n  - 24.55\n  - 0.048\n  notes: PrePost x side F(1,492) = 24.55, P = 1.0e-06, partial eta squared 0.048 (type II F =\n    34.3). The sham-side dACC-CB falls from 0.413 to 0.230 (P = 3.6e-08, reported 1.30e-08). The\n    sham-side MCC-CB falls (-0.115, P = 0.44), so shows no increase. All four sham-side subregions\n    decrease (-0.080 to -0.184), and only the dACC-CB reaches P < 0.05; the statement's further\n    comparison marked in the legend is not found at P < 0.05 on either side.\n- claim: fig6c-monkey-d-cc1-no-change\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig6c-monkey-d-cc1-no-change\n  notes: Paired t(27) = -0.9888, P = 0.332, Cohen's dz -0.19 (the reported values); lead side 58.0 %\n    against control 59.9 % (mean difference -1.86). The unpaired variant gives P = 0.47.\n  deviations:\n  - Fields are paired by row, as the Fig6C script does; each row holds one section and field of\n    both hemispheres (reading (a)).\n- claim: ed10c-monkey-d-subcortical-decrease\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:ed10c-monkey-d-subcortical-decrease\n  notes: In monkey D's difference connectome the subcortical block mean is -0.035 (reading (a)) and\n    the median subcortical ROI change -0.022 (reading (b)); 76% of subcortical entries are\n    negative, against +0.012 and 40% in the DBS group. Cortical block mean -0.014, 51% of cortical\n    entries negative (DBS group 78%).\n- claim: fig6d-monkey-d-scc-local-increase\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig5a-nonsurgical-no-reduction, blocked for missing data. The claim also needs\n    monkey D's whole-brain voxelwise map and the location of the lead track; the dandiset holds\n    only the voxels of the 17 target ROIs and gives no lead location. In those ROIs, area 25 on the\n    sham side, next to the lead, has the largest increase (+0.18, P = 4.3e-12 in the 17-ROI model),\n    which the notebook prints under ed10d-monkey-d-roi-changes but which is not the claim's test.\n- claim: fig6e-monkey-d-no-network-reduction\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:fig6e-monkey-d-no-network-reduction\n  notes: The interaction is F(1,10972) = 7.36, P = 0.0067, as reported. With LIM as the script has\n    it (with area 25), no sham-side DMN, LIM or CEN comparison is a significant decrease (0 of 3;\n    sham DMN -0.006, P = 0.73), but over both sides the control-side CEN decreases (-0.009, P =\n    0.0089, the legend's 0.0088), 1 of 6. Without area 25, the sham-side LIM decreases (-0.008, P =\n    6.9e-04), 1 of 3 on the sham side and 2 of 6 on both. The readings disagree (reproduced only\n    for the sham side with the script's LIM), and the criterion blocks the claim when they do. The\n    question for the paper's authors is whether \"not observed\" covers the control hemisphere,\n    where their own legend lists a significant CEN difference (the data show a decrease), and the\n    script settles LIM as including area 25.\n  deviations:\n  - The LIM membership of the script (with area 25) and of the Methods (without) are both run, as\n    the criterion asks.\n- claim: ed10d-monkey-d-roi-changes\n  outcome: reproduced\n  notebook: reproduce_fujimoto_2026.ipynb\n  output: claim:ed10d-monkey-d-roi-changes\n  notes: PrePost x side F(1,10106) = 4.58, P = 0.032 (reported). Of the eight comparisons exactly\n    the sham-side vmFC (-0.023, P = 8.0e-04, reported 7.83e-04) and the control-side\n    anterior-dorsal insula (+0.041, P = 1.1e-11, reported 1.37e-12) have P < 0.05; the others have\n    P = 0.31 or more.\nfindings:\n- kind: data_missing\n  statement: The Data availability statement says the functional MRI data are deposited in this\n    dandiset, but it holds only derived values (seed connectivity of the voxels of 17 target ROIs\n    for monkeys N, T and D, and three group-average connectomes). There are no fMRI or DWI images,\n    no whole-brain seed maps, no seed connectivity for the nonsurgical controls B, W and H, and no\n    per-monkey connectomes, so the voxelwise cluster maps of Fig. 5a, Fig. 6d and Extended Data\n    Figs. 7, 8 and 10d cannot be tested.\n- kind: metadata_insufficient\n  statement: The connectomes in \"Source Data FC matrix.xlsx\" (123 x 123) carry no ROI names. The\n    Fig. 4 script reads them from atlas key and reorder files (CHARM_key_4.txt, SARM_key_4.txt,\n    reorder_rois.txt) that are not deposited, so no ROI can be named and the network sorting of\n    Fig. 4c cannot be repeated.\n- kind: metadata_error\n  statement: The legend in dbs_behavior_data_a.xlsx codes foraging as yes 2 and no 1, but every\n    foraging value is 0 or 1; read as 1 yes, the values give the paper's statistics. The same\n    legend gives group codes 1 (DBS) and 0 (non-stimulation control), while monkey D's rows carry\n    group 2.\n- kind: other\n  statement: In CC1_MCC_CB_data_a.xlsx two fields of monkey T's control side (section T423, fields 3\n    and 4) carry CC1/DAPI ratios that do not match their counts (44.9 and 35.4 % against 35.4 and\n    44.2 % from the counts); field 4's ratio is field 3's. Two MCC-CB fields have more CC1-positive\n    than DAPI-positive cells (ratio above 100 %). The paper's script uses the ratio column; with the\n    ratio from the counts the side effect changes from F = 9.00 to 9.03.\n- kind: metadata_error\n  statement: In dbs_EMgratio_MCC_CB_data_a.xlsx the column headed \"diameter of axon(pixel)\" holds\n    half the mean of the long and short diameters (a radius), and \"diameter of axon(nm)\" the same\n    in nm. The g-ratio column is consistent with the Methods' definition.\n- kind: code_mismatch\n  statement: The Fig. 4 script counts an ROI as changed when `ranksum` of its changes against a\n    vector of zeros gives P < 0.05/nrois (nrois = 123), while the Methods and the Fig. 4b legend\n    give a rank-sum test at \"P < 0.01 with Bonferroni correction\". The script's threshold\n    reproduces the 69 and 44 ROIs of Supplementary Tables 1 and 2, whose largest listed P is 3.9e-4,\n    above 0.01/122.\n- kind: paper_inconsistency\n  statement: The Fig. 6a legend gives the PrePost x side x tract interaction as F(1,1238) = 6.02,\n    P = 0.0025. The data give F = 6.02 and P = 0.0025 with 2 numerator df, as three tracts imply.\n- kind: methods_unavailable\n  statement: For fig6e-monkey-d-no-network-reduction, the paper does not say whether \"the\n    widespread reductions ... were not observed\" in monkey D covers the control hemisphere. Its own\n    Fig. 6e legend lists a significant control-side CEN difference, which the data show to be a\n    decrease (P = 0.0089), and the Methods list LIM without area 25 while the script includes it.\n    The authors could say which hemisphere and which LIM the sentence refers to.\n- kind: metadata_insufficient\n  statement: The dandiset's metadata names the paper only in its title, with no related resource,\n    and gives no species, approach, measurement technique or variables measured. The sheets have\n    no data dictionary beyond the legends inside some of them.\n- kind: other\n  statement: Two scripts are deposited twice under two names with identical text\n    (`Fig4 Fujimoto_NatNeuro_2026_FCmatrix.m` and `Fig4andE10C_Fujimoto_NatNeuro_2026_FCmatrix.m`;\n    `Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m` and\n    `Fig6DandE10Ddbs_FC_25norm_mkD_analysisscript_a.m`).\n"
}
```

```
File created successfully at: attempts/001773-fujimoto-2026-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

A note in the record cites monkey D's area-25 change, which the notebook does not print yet. Adding that table to the ed10d cell, then checking the YAML for colon-space in plain scalars:

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
s=open('build_nb.py').read()
old='''print("significant (P < 0.05):", [f"{s} {n}" for s, n in zip(four[four.P < 0.05].side, four[four.P < 0.05].name)])'''
assert old in s
s=s.replace(old, old+'''
print("\\\\nall 17 ROIs, monkey D:")
print(pp_roiD.to_string(index=False))''')
open('build_nb.py','w').write(s)
EOF
grep -n 'all 17 ROIs' build_nb.py; cd  python - <<'EOF'
import re,yaml
p='attempts/001773-fujimoto-2026-01.yaml'
yaml.safe_load(open(p))
for i,l in enumerate(open(p),1):
    t=l.strip()
    if t.startswith('- '): t=t[2:]
    m=re.match(r'^[A-Za-z_]+:\s?',t)
    rest=t[m.end():] if m else t
    if ': ' in rest: print(i,l.rstrip())
print('ok')
EOF
```

```
871:print("\\nall 17 ROIs, monkey D:")
ok
```

**Agent**

Now the question for a reader on fig4b, the README, and a rerun:

**Agent calls Bash**

```bash
cd  ls schemas; grep -rn "questions" tools/entry.py | head -5; cat > questions/001773.yaml <<'EOF'
dandiset: "001773"
paper: doi:10.1038/s41593-026-02301-4
questions:
- claim: fig4b-roi-changes-counts
  asked: 2026-11-03
  question: The paper's Fig. 4 script in the dandiset (code/Fig4 Fujimoto_NatNeuro_2026_FCmatrix.m)
    counts an ROI as changed when `ranksum(sbj_data_mean, zeros(length(sbj_data_mean),1))` is below
    0.05/nrois, that is a rank-sum of the ROI's changes against zeros at 0.05 over the number of
    ROIs (123 in the deposited matrices). The criterion lists a pre against post rank-sum, a
    signed-rank of the changes, and thresholds 0.01/122 and 0.01, but not this test or threshold.
    Should the criterion include the script's test and threshold as a reading? And is "of the 122
    ROIs" right, when the deposited connectomes have 123 ROIs and the legend's n = 122 is the
    number of values per ROI?
  passage: Rank-sum test was conducted to determine statistical significance ( P < 0.01 with
    Bonferroni correction). (Fig. 4b legend) Colors represent significant negative (blue) and
    positive changes (orange) of functional connectivity from zero in each ROI ( P < 0.01 with
    Bonferroni correction, rank-sum test). (Extended Data Fig. 10c legend) The claims file's own
    header notes that Supplementary Tables 1 and 2 list P values up to 3.9e-4 as significant.
  why: Under the criterion's readings the counts are 10 to 85 (DBS) and 4 to 56 (controls), never
    both in tolerance, so the claim would be not reproduced. The script's test and threshold give
    69 and 44, the reported counts, with a largest significant P of 3.88e-04 in both groups, which
    matches the 3.9e-4 of the Supplementary Tables. The attempt recorded the claim as reproduced,
    resting on the assumption that the script's procedure is the paper's.
EOF
python -c "import yaml;yaml.safe_load(open('questions/001773.yaml'));print('ok')"
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
ok
```

**Agent calls Bash**

```bash
cd  sed -i 's/counts are 10 to 85 (DBS) and 4 to 56 (controls), never/counts are 10 to 85 (DBS) and 4 to 49 (controls), never/' questions/001773.yaml; grep -n "4 to 49" questions/001773.yaml; cat > entries/001773-fujimoto-2026/README.md <<'EOF'
# Fujimoto, Fujimoto, Elorette et al. (2026) from dandiset 001773

Tests the findings of [Fujimoto et al. (2026)](https://doi.org/10.1038/s41593-026-02301-4) that can
be tested on [DANDI:001773](https://dandiarchive.org/dandiset/001773/0.260416.1939). The dandiset
holds the paper's derived values (voxel FA, voxel seed connectivity in 17 target ROIs, group
connectomes, CC1 and DAPI counts, EM g-ratios, home-cage behavior bins) and its MATLAB scripts.
No images are in it.

| Claims | Outcome |
|---|---|
| DWI, histology, EM and behavior of the stimulated monkeys N and T (10 claims) | Reproduced |
| Connectome patterns and per-ROI counts, DBS group and nonsurgical controls (3 claims) | Reproduced (the counts rest on the test of the paper's script) |
| Fig. 4c network sorting | Blocked: the connectome ROIs have no names |
| Seed connectivity of the SCC, ROIs and networks, N and T (11 claims) | Reproduced |
| Voxelwise maps of the nonsurgical controls and of monkey D (2 claims) | Blocked: data missing |
| Monkey D, FA, CC1, connectome and seed ROIs (5 claims) | Reproduced |
| Monkey D, behavior unchanged | Not reproduced (foraging falls, P = 0.023) |
| Monkey D, no network reduction | Blocked: the readings disagree |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001773-fujimoto-2026-01.yaml`](../../attempts/001773-fujimoto-2026-01.yaml).

- `reproduce_fujimoto_2026.ipynb`: the analysis. It takes under a minute.
- `dbs.py`: reading the sheets from the archive, and the paper's statistics as its MATLAB scripts
  compute them (`anovan` type III with the scripts' model terms, `multcompare` Tukey-Kramer on
  population marginal means). Other notebooks on this dandiset can import it.
EOF
cd entries/001773-fujimoto-2026 && . $TMPDIR/expl/bin/activate && python $TMPDIR/build_nb.py reproduce_fujimoto_2026.ipynb $TMPDIR/conclusions.yaml && cd ../.. && python tools/entry.py all entries/001773-fujimoto-2026 2>&1 | tail -3
```

```
19:  why: Under the criterion's readings the counts are 10 to 85 (DBS) and 4 to 49 (controls), never
Installed kernelspec registry-001773-fujimoto-2026 in executed/001773-fujimoto-2026/.venv/share/jupyter/kernels/registry-001773-fujimoto-2026
0 error(s)
pass  reproduce_fujimoto_2026.ipynb  (32 s)
```

**Agent**

The README group counts are off by one (9 and 10, not 10 and 11). Fixing them and confirming the new monkey D table in the executed copy:

**Agent calls Bash**

```bash
cd  sed -i 's/behavior of the stimulated monkeys N and T (10 claims)/behavior of the stimulated monkeys N and T (9 claims)/; s/ROIs and networks, N and T (11 claims)/ROIs and networks, N and T (10 claims)/' entries/001773-fujimoto-2026/README.md; grep -n "claims)" entries/001773-fujimoto-2026/README.md; python - <<'EOF'
import json
nb=json.load(open('executed/001773-fujimoto-2026/reproduce_fujimoto_2026.ipynb'))
for c in nb['cells']:
    if 'claim:ed10d-monkey-d-roi-changes' in str(c['metadata']):
        print(''.join(o.get('text','') for o in c['outputs'])[-1200:])
EOF
```

```
Exit code 1
11:| DWI, histology, EM and behavior of the stimulated monkeys N and T (9 claims) | Reproduced |
12:| Connectome patterns and per-ROI counts, DBS group and nonsurgical controls (3 claims) | Reproduced (the counts rest on the test of the paper's script) |
14:| Seed connectivity of the SCC, ROIs and networks, N and T (10 claims) | Reproduced |
15:| Voxelwise maps of the nonsurgical controls and of monkey D (2 claims) | Blocked: data missing |
16:| Monkey D, FA, CC1, connectome and seed ROIs (5 claims) | Reproduced |
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
TypeError: sequence item 0: expected str instance, list found
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/001773-fujimoto-2026/reproduce_fujimoto_2026.ipynb'))
for c in nb['cells']:
    if 'claim:ed10d-monkey-d-roi-changes' in str(c['metadata']):
        print(''.join(''.join(o.get('text',[])) for o in c['outputs'])[-1500:])
EOF
```

```
58        0.030886 1.397047e-02                     MT
control    1  0.016865  0.013736       -0.003129 1.000000e+00                    PCC
control    2  0.039579  0.029462       -0.010118 9.999985e-01                   vmFC
control    3  0.015081  0.045549        0.030469 4.291012e-12                    STG
control    4  0.017008  0.057560        0.040551 1.137601e-11 Anterior-dorsal Insula
control    5  0.023517  0.037047        0.013529 6.274835e-01                   dACC
control    6  0.027179  0.014466       -0.012713 3.520376e-08                  DLPFC
control    7  0.011466  0.009103       -0.002363 1.000000e+00                    PPC
control    8  0.119994  0.179493        0.059499 7.907795e-03                Area 25
control    9  0.047140  0.037204       -0.009937 1.000000e+00                Area 32
control   10  0.004304  0.011102        0.006799 1.000000e+00                    MCC
control   11  0.006732  0.016958        0.010225 9.945599e-01                    HIP
control   12  0.012019  0.015630        0.003612 1.000000e+00                    AMY
control   13  0.006049 -0.000224       -0.006273 6.198986e-01             Sensory Cx
control   14 -0.005631  0.007632        0.013263 2.425492e-04               Motor Cx
control   15  0.004219  0.004415        0.000196 1.000000e+00                    SMA
control   16  0.006080 -0.000099       -0.006180 5.997303e-02              Visual Cx
control   17 -0.006408 -0.004673        0.001735 1.000000e+00                     MT
```

**Agent**

Everything matches. Running the final check and the handover:

**Agent calls Bash**

```bash
cd  rm -rf entries/001773-fujimoto-2026/__pycache__; . $TMPDIR/expl/bin/activate; python tools/entry.py check entries/001773-fujimoto-2026 && python tools/entry.py handover entries/001773-fujimoto-2026 && ls -R executed/001773-fujimoto-2026/handover | head; git status --short; date -u
```

```
0 error(s)
wrote executed/001773-fujimoto-2026/handover
executed/001773-fujimoto-2026/handover:
10.1038-s41593-026-02301-4.yaml
dbs.py
reproduce_fujimoto_2026.ipynb
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
?? attempts/001773-fujimoto-2026-01.yaml
?? entries/001773-fujimoto-2026/
?? questions/001773.yaml
?? scripts
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "Result:" executed/001773-fujimoto-2026/handover/reproduce_fujimoto_2026.ipynb; grep -c "## Summary" executed/001773-fujimoto-2026/handover/reproduce_fujimoto_2026.ipynb; ls -la .bashrc scripts | head -3; git log --oneline -1 -- scripts 2>/dev/null | head -1
```

```
0
0
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  3 16:08 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  3 16:08 scripts
```

**Agent**

I've finished steps 1 to 6 for DANDI:001773: the entry `entries/001773-fujimoto-2026/`, the record `attempts/001773-fujimoto-2026-01.yaml`, one reader question in `questions/001773.yaml`, and the handover package. Lock, check and run all pass, and the notebook runs in 32 s from a clean environment. Nothing is committed.

**(1) Outcome per claim** (32 claims)

| Outcome | Claims |
|---|---|
| reproduced (27) | ed1-behavior-increase, fig2a-cb-fa-increase, fig2a-no-change-other-tracts, ed2-cb-both-monkeys, fig2b-mcc-cb-fa-increase, fig3c-cc1-dapi-ratio, ed5-cc1-count-dapi-unchanged, ed6-dacc-ufm-no-oligodendrocyte-change, fig3f-g-ratio-decrease, fig4a-cortical-down-subcortical-up, fig4b-roi-changes-counts (rests on an assumption), fig4-nonsurgical-no-pattern, fig5a-pre-scc-connectivity, fig5b-scc-decreases, fig5b-scc-increases, ed9-control-hemisphere-changes, ed9-no-change-motor-mcc, ed7-decreases-both-monkeys, fig5c-dmn-lim-cen-decrease, fig5c-smn-increase, fig5c-vis-no-change, fig5c-san-rebalanced, fig6a-monkey-d-cb-fa-decrease, fig6b-monkey-d-dacc-cb-decrease, fig6c-monkey-d-cc1-no-change, ed10c-monkey-d-subcortical-decrease, ed10d-monkey-d-roi-changes |
| not reproduced (1) | ed1-monkey-d-no-change: monkey D's foraging falls from 0.183 to 0.050, P = 0.023 |
| blocked (4) | fig4c-network-sorted-reduction (methods_underspecified: the connectome ROIs have no names or network assignment); fig5a-nonsurgical-no-reduction and fig6d-monkey-d-scc-local-increase (data_missing); fig6e-monkey-d-no-network-reduction (methods_underspecified: it was run, its readings disagree, and the criterion says to block in that case) |

**(2) The dataset**
- **Contents:** no NWB. It holds 34 Excel sheets of derived values and 18 MATLAB scripts. I pinned 0.260416.1939, the version the paper cites; the latest version, 0.260615.1838, has identical asset ids.
- **Match to the paper:** with the scripts' models, almost every F value, partial eta squared and voxel or field count matches the paper to the printed digits.
- **Missing:** fMRI and DWI images, whole-brain seed maps, the nonsurgical controls' seed data, per-monkey connectomes, ROI names for the 123 x 123 connectomes, and the lead location.
- **Errors:**
  - The behavior legend codes foraging as yes 2 / no 1, but the values are 0/1. Monkey D's group code (2) is not in the legend.
  - Two MCC-CB fields have ratios that don't match their counts, and two have more CC1 than DAPI cells.
  - The EM "diameter" column holds a radius.
  - Two scripts are deposited twice under different names.
  - The dandiset metadata does not link the paper.
  - The Fig. 6a legend's interaction df is printed as 1; the data give 2.
- **Assumption (fig4b):** I took the per-ROI test and threshold from the paper's Fig. 4 script: a rank-sum of each ROI's changes against zeros at P < 0.05/123. That gives exactly 69 and 44 ROIs, and the largest P counted (3.88e-4) matches the Supplementary Tables. The Methods say P < 0.01 with Bonferroni correction, and none of the criterion's readings gets both counts within tolerance. I recorded this as a `code_mismatch` finding.
- **Question for the paper's authors (fig6e):** does "not observed" cover the control hemisphere, and which LIM membership is meant?
- **Question to a reader (fig4b):** should the criterion include the script's test and threshold? I also asked whether "122 ROIs" is right, since the matrices have 123 and 122 is the number of values per ROI.

**(3) Where the protocol was unclear or did not fit**
1. The DANDI reading rules assume NWB read with remfile and h5py. I fetched each xlsx asset into memory through the API's download endpoint.
2. The step 2 clock and stream-alignment check has nothing to act on in derived tables. I checked that the side labels match the hemispheres (coordinates, voxel counts, EM image labels) and recorded pre/post as consistent with the data but not shown.
3. The paper's code sits inside the dataset, so the readers, who may not open dataset files, never saw it. Code-settled details fell to me, and for fig4b the code's procedure is not among the criterion's readings. The rule "Methods first, code as variant" conflicts with the fact that the paper's own tables follow the code. I adopted the code's procedure as an assumption and asked a reader.
4. A criterion reading the data cannot support: only concatenated-run seed maps are deposited, so the per-run reading could not be run. I recorded it as a deviation.
5. For absence claims, the protocol says the several-readings rule does not apply, but the fig6e criterion says to block when its readings disagree. I followed the criterion.
6. SciPy's studentized-range tail stops at about 1e-11, where MATLAB prints 0. I stated this; it cannot change an outcome at P < 0.05.

**(4) Runtime and failures**
The run took about 25 minutes (16:09 to 16:33 UTC), and the notebook itself takes 32 s. The only failure was one notebook run that broke on a string escape in my generator; I fixed it and the rerun passed. The working tree also shows untracked dotfiles and a `scripts` entry; these are sandbox device placeholders created before the run, and I left them alone.

## End of run

75 turns, 20 minutes, $6.51 at API prices, result: success.
