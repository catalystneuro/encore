# 001773 · author-revise-1 · run 41680765759

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/001773/verifier-1-report.md; ls entries/001773-fujimoto-2026 entries/001773-fujimoto-2026/*; ls questions | head
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -80
```

```
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
53:### 2. Read the paper's code
63:### 3. Write the claims file
148:### 4. Data from outside the paper's own recordings
156:### 5. Check
169:### 6. Answer questions
182:## Author
198:### 1. Establish what can be tested
325:### 2. Check the data against its description
340:### 3. Write the entry
398:### 4. Lock, check and run
409:### 5. Record the attempt
460:### 6. Hand over for verification
498:## Repeat attempts
540:## Local and remote datasets
563:## Verifier
567:### Round 1: without the author's conclusions
592:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

```
Tue Nov  3 17:11:40 UTC 2026
**A. Outcomes** (32 claims in the claims file, 32 judged)

| Claim | Outcome | Reason |
|---|---|---|
| ed1-behavior-increase | reproduced | Cell 18: movement F(1,236)=34.61, ηp²=0.128; foraging F=17.35, ηp²=0.068, all within tolerance. Reading (b) is also P<0.05. Post is higher than pre in both monkeys for both behaviors. |
| ed1-monkey-d-no-change | not_reproduced | Cell 20: foraging drops from 0.183 to 0.050, F(1,118)=5.32, P=0.023 (Fisher variant P=0.043). Movement does not differ (P=0.18). The criterion fails when either behavior differs. |
| fig2a-cb-fa-increase | reproduced | Cell 22: PrePost×side F=4.64, P=0.031, ηp²=0.00146, within tolerance; type II gives P=0.012. Stimulated CB Tukey P=0.022 with post higher. Voxel counts match the legend (cell 7). |
| fig2a-no-change-other-tracts | reproduced | Cell 24: none of the 5 comparisons has P<0.05 (smallest P=0.86). |
| ed2-cb-both-monkeys | reproduced | Cell 26: stimulated CB post−pre is +0.019 in N and +0.079 in T. |
| fig2b-mcc-cb-fa-increase | reproduced | Cell 28: F=5.42, P=0.020, ηp²=0.0040 (type II P=0.045). Stimulated MCC P=0.0018 with post higher; no other cell has a significant increase. MCC change is +0.081 in N and +0.205 in T. |
| fig3c-cc1-dapi-ratio | reproduced | Cell 30: F(1,108)=9.00, P=0.0034, ηp²=0.077; reading (b) and the ratio recomputed from counts agree. Stimulated side is higher in both monkeys (+5.5 and +5.0). |
| ed5-cc1-count-dapi-unchanged | reproduced | Cell 32: CC1 F=6.22, P=0.014, ηp²=0.054, stimulated side higher. DAPI P=0.46. Both readings agree. |
| ed6-dacc-ufm-no-oligodendrocyte-change | reproduced | Cell 34: 0 of 6 reading (a) tests have P<0.05, and reading (b) agrees. UF/FM DAPI gives P=0.951 against the paper's printed 0.9611; the paper's own ηp² (4.97e-5) implies 0.951, so the printed value is a typo. |
| fig3f-g-ratio-decrease | reproduced | Cell 36: F(1,696)=58.98, P=5.4e-14, ηp²=0.078. Stimulated side is lower in N (−0.084) and T (−0.023). 7
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 182,200p docs/protocol.md; sed -n 290,330p docs/protocol.md; sed -n 398,500p docs/protocol.md
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).

**Time.** An author run is stopped five hours after it starts, and whatever
is not recorded by then is lost. The prompt says when the run started and the
time by which to finish. Check the clock (`date -u`) between steps. When that
time comes, stop analysing and finish: record each claim not yet tested as
blocked, `too_large` where the computation is what stopped it, saying how far
it got, then write the attempt record and run the entry's checks. A record
with some claims blocked for time is worth more than a run that is cut off.

### 1. Establish what can be tested

Do this before any analysis.
   it links. Search all of them, and where they disagree, follow the order of
[... 143 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep 001773; ls transcripts/001773; cat questions/001773.yaml 2>/dev/null | head -50; wc -l entries/001773-fujimoto-2026/dbs.py
```

```
001773-fujimoto-2026-01.yaml
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
dandiset: "001773"
paper: doi:10.1038/s41593-026-02301-4
questions:
- claim: fig4b-roi-changes-counts
  asked: 2026-11-03
  question: The paper's Fig. 4 script in the dandiset (code/Fig4 Fujimoto_NatNeuro_2026_FCmatrix.m)
    counts an ROI as changed when `ranksum(sbj_data_mean, zeros(length(sbj_data_mean),1))` is below
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001773-fujimoto-2026-01.yaml
```

```
schema_version: 2
id: 001773-fujimoto-2026-01
dataset:
  archive: dandi
  id: "001773"
  version: 0.260416.1939
  doi: 10.48324/dandi.001773/0.260416.1939
paper: doi:10.1038/s41593-026-02301-4
date: 2026-11-03
entry: 001773-fujimoto-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
    platform: GitHub Actions
[... 397 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; cat README.md | head -40; sed -n 1,80p dbs.py; python - <<'E'
import json
nb=json.load(open('reproduce_fujimoto_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(i,c['cell_type'],c.get('metadata',{}).get('tags'),repr(s[:150]))
E
```

```
# Fujimoto, Fujimoto, Elorette et al. (2026) from dandiset 001773

Tests the findings of [Fujimoto et al. (2026)](https://doi.org/10.1038/s41593-026-02301-4) that can
be tested on [DANDI:001773](https://dandiarchive.org/dandiset/001773/0.260416.1939). The dandiset
holds the paper's derived values (voxel FA, voxel seed connectivity in 17 target ROIs, group
connectomes, CC1 and DAPI counts, EM g-ratios, home-cage behavior bins) and its MATLAB scripts.
No images are in it.

| Claims | Outcome |
|---|---|
| DWI, histology, EM and behavior of the stimulated monkeys N and T (9 claims) | Reproduced |
| Connectome patterns and per-ROI counts, DBS group and nonsurgical controls (3 claims) | Reproduced |
| Fig. 4c network sorting | Blocked: the connectome ROIs have no names |
| Seed connectivity of the SCC, ROIs and networks, N and T (10 claims) | Reproduced |
| Voxelwise maps of the nonsurgical controls and of monkey D (2 claims) | Blocked: data missing |
| Monkey D, FA, CC1, connectome and seed ROIs (5 claims) | Reproduced |
| Monkey D, behavior unchanged | Not reproduced (foraging falls, P = 0.023) |
| Monkey D, no network reduction | Blocked: the readings disagree |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
[... 196 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import dbs
for p in sorted(dbs.asset_ids()): print(p)
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import dbs
  File "entries/001773-fujimoto-2026/dbs.py", line 41, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls ../../.venv* ../../envs 2>/dev/null; sed -n 1,60p ../../tools/entry.py | grep -n -i "venv\|env"
```

```
3:    python tools/entry.py lock  entries/<name>   # pin the environment
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
25:`run` builds a fresh virtual environment from the lock file and executes each
26:notebook through a Jupyter kernel installed in that environment, in the entry
```

**Agent calls Bash**

```bash
grep -n "venv\|tempfile\|mkdtemp" ../../tools/entry.py | head -20
```

```
345:    venv = (output_dir / ".venv").resolve()
346:    python = venv / "bin" / "python"
350:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
353:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
367:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
```

**Agent calls Bash**

```bash
ls -a ../../executed/001773-fujimoto-2026/ 2>/dev/null; ls ../../executed/001773-fujimoto-2026/.venv/bin/python 2>/dev/null
```

```
Exit code 2
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.12 v && uv pip install -q --python v/bin/python -r entries/001773-fujimoto-2026/requirements.lock.txt 2>&1 | tail -3; ls v/bin/python
```

```
v/bin/python
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026 && $TMPDIR/v/bin/python -c "
import dbs
for p in sorted(dbs.asset_ids()): print(p)
"
```

```
README.md
code/Fig2A_dbs_FA_wholetract_analysisscript_a.m
code/Fig2B_dbs_FA_CB_part_analysisscript_a.m
code/Fig3CandE5_dbs_IF_CC1_MCC_CB_analysisscript_a.m
code/Fig3F_dbs_EMgratio_analysisscript_a.m
code/Fig4 Fujimoto_NatNeuro_2026_FCmatrix.m
code/Fig4andE10C_Fujimoto_NatNeuro_2026_FCmatrix.m
code/Fig5BCandE9_dbs_FC_25norm_mkNT_analysisscript_a.m
code/Fig6A_dbs_FA_wholetract_mkD_analysisscript_a.m
code/Fig6B_dbs_FA_CB_part_mkD_analysisscript_a.m
code/Fig6C_dbs_IF_CC1_mkD_MCC_CB_analysisscript_a.m
code/Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m
code/Fig6DandE10Ddbs_FC_25norm_mkD_analysisscript_a.m
code/FigE1_dbs_behavior_analysisscript_a.m
code/FigE4A_dbs_fine_grained_FA_CB_a.m
code/FigE4B_dbs_fine_grained_FA_UF_a.m
code/FigE4C_dbs_fine_grained_FA_FM_a.m
code/FigE6A_dbs_IF_CC1_dACC_CB_analysisscript_a.m
code/FigE6B_dbs_IF_CC1_UF_FMoverlap_analysisscript_a.m
dataset_description.json
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026 2>/dev/null; mkdir -p $TMPDIR/code; $TMPDIR/v/bin/python -c "
import dbs,os
for p in dbs.asset_ids():
    if p.startswith('code/'): open(os.path.join('$TMPDIR/code',p[5:]),'wb').write(dbs.fetch(p))
"; cd $TMPDIR/code; cat FigE1_dbs_behavior_analysisscript_a.m
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

[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims 2>/dev/null | grep 1773; f=$(ls claims/*1773* 2>/dev/null | head -1); echo $f; grep -n "ed1-monkey-d-no-change" -A40 $f | head -60
```

```
001773
10.1038-s41593-026-02301-4.yaml
grep: 10.1038-s41593-026-02301-4.yaml: No such file or directory
```

**Agent calls Bash**

```bash
ls claims/001773; f=claims/001773/10.1038-s41593-026-02301-4.yaml; grep -n "id: ed1-monkey-d-no-change" -A40 $f | head -50; grep -n "fig4c-network" -A40 $f | head -50
```

```
10.1038-s41593-026-02301-4.yaml
160:- id: ed1-monkey-d-no-change
161-  statement: In the unstimulated lead-implanted monkey D, the amount of movement and foraging
162-    did not change between before and 6 weeks after implantation.
163-  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain
164-    networks, paragraph 2; Extended Data Fig. 1 (monkey D)
165-  quote: First, there was no change in the amount of movement or foraging in naturalistic
166-    behavior
167-  criterion: A claim of absence. The paper shows monkey D's probabilities (Extended Data Fig. 1)
168-    but reports no test for monkey D; the legend says only N and T were analysed. The test the
169-    Methods describe for this measure, applied to one monkey, is a one-way ANOVA of the 120
170-    binary bins on condition (pre, post), at the Methods' P < 0.05. Reproduced when neither
171-    movement nor foraging differs at P < 0.05; not reproduced when either does. The pre and post
172-    probabilities and their difference are given either way.
173-- id: fig2a-cb-fa-increase
174-  statement: After 6 weeks of SCC-DBS, fractional anisotropy (FA) increased in the cingulum
175-    bundle of the stimulated hemisphere, with a significant PrePost x side interaction and a
176-    significant pre against post difference in the stimulated CB.
177-  source: Results, SCC-DBS induces selective macroscale remodeling in the CB, paragraph 3; Fig.
178-    2a and legend
[... 72 more lines not kept]
```

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
cd $TMPDIR/code; head -60 Fig5BCandE9_dbs_FC_25norm_mkNT_analysisscript_a.m; echo =====; grep -n -i "concat\|run\|importdata\|xlsread\|readtable" *.m | grep -v "^Fig4" | head -30; echo ====; head -40 Fig6C_dbs_IF_CC1_mkD_MCC_CB_analysisscript_a.m
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
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; sed -n 80,303p dbs.py | grep -n "def \|read_excel\|sheet" ; $TMPDIR/v/bin/python - <<'E'
import dbs, pandas as pd, io
x=pd.read_excel(io.BytesIO(dbs.fetch("source_data/CC1_mkD_MCC_CB_data_a.xlsx")),sheet_name=None,header=None)
for k,v in x.items(): print(k,v.shape); print(v.head(6).to_string())
x=pd.read_excel(io.BytesIO(dbs.fetch("source_data/dbs_FC25norm_mkNT_concatenated_all_data_a.xlsx")),sheet_name=None,header=None)
for k,v in x.items(): print(k,v.shape); print(v.head(4).to_string()); print(v.iloc[:,:3].nunique())
E
```

```
4:def sheet(path: str, sheet_name=0, header=None) -> pd.DataFrame:
5:    return pd.read_excel(io.BytesIO(fetch(path)), sheet_name=sheet_name, header=header)
8:def text(path: str) -> str:
14:def behavior() -> pd.DataFrame:
15:    d = sheet("source_data/dbs_behavior_data_a.xlsx", header=0).iloc[:, :6].dropna()
19:def fa_wholetract() -> pd.DataFrame:
20:    d = sheet("source_data/dbs_FA_wholetract_data_a.xlsx", header=0).iloc[:, :5].dropna()
24:def fa_subpart() -> pd.DataFrame:
25:    d = sheet("source_data/dbs_FA_CB_subpart_data_a.xlsx", header=0).iloc[:, :5].dropna()
30:def _mkD(path: str, last: str) -> pd.DataFrame:
31:    # These sheets have no header row; the legend (columns O onwards) names columns A to D.
32:    d = sheet(path).iloc[:, :4].dropna()
37:def fa_wholetract_mkD() -> pd.DataFrame:
41:def fa_subpart_mkD() -> pd.DataFrame:
45:def cc1(region: str) -> pd.DataFrame:
47:    d = sheet(f"source_data/CC1_{region}_data_a.xlsx", header=0).iloc[:, :7].dropna(subset=["CC1"])
52:def cc1_mkD() -> pd.DataFrame:
53:    return sheet("source_data/CC1_mkD_MCC_CB_data_a.xlsx", header=0).iloc[:, :8].dropna(subset=["CC1_leadside"])
56:def gratio() -> pd.DataFrame:
57:    d = sheet("source_data/dbs_EMgratio_MCC_CB_data_a.xlsx").iloc[2:, :15]
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; $TMPDIR/v/bin/python - <<'E'
import dbs
for w in ["mkNT","mkD"]:
    d=dbs.seed_fc(w)
    print(w, d.groupby(["subject","time_condition","date"]).size().unstack(fill_value=0))
    # voxel duplicates within a subject/time/side/roi?
    k=d.groupby(["subject","time_condition","side","roi","x","y","z"]).size()
    print("max rows per voxel:",k.max())
E
```

```
/bin/bash: line 1: cd: entries/001773-fujimoto-2026: No such file or directory
mkNT date                       1     2     3     4
subject time_condition                        
1       1               5087     0     0     0
        2                  0  5087     0     0
2       1                  0     0  5087     0
        2                  0     0     0  5087
max rows per voxel: 1
mkD date                       1     2
subject time_condition            
3       1               5087     0
        2                  0  5087
max rows per voxel: 1
```

**Agent calls Bash**

```bash
cd  ls paper; grep -rn -i "concatenat\|each run\|per run" paper/*.md 2>/dev/null | head; grep -rln -i "concatenat" paper | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "concatenat\|runs\b\|run was\|each run\|seed" paper/*.txt | head -30; grep -n "fig5a-pre-scc" -A30 claims/001773/*.yaml | grep -i -n "run\|concat"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i ".\{250\}concatenat.\{250\}" paper/*.txt | head; echo ===; grep -o -i ".\{200\}each run.\{200\}" paper/*.txt | head -5; echo; grep -n "fig5a-pre-scc" -A30 claims/001773/*.yaml | grep -i "run\|concat"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 468,480p claims/001773/*.yaml; grep -o -i ".\{300\}seed-based.\{400\}" paper/*.txt | head -4
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; $TMPDIR/v/bin/python - <<'E'
import dbs, pandas as pd, numpy as np
x=dbs.sheet("source_data/Source Data FC matrix.xlsx", sheet_name=None)
for k,v in x.items():
    nn=[(i,j,c) for (i,j),c in np.ndenumerate(v.values) if isinstance(c,str)]
    print(k, v.shape, "non-numeric cells:", len(nn), nn[:20])
E
which pdftotext
```

```
Exit code 1
Average FC matrix DBS (374, 123) non-numeric cells: 3 [(0, 0, 'DBS group Pre'), (125, 0, 'DBS group post'), (250, 0, 'DBS group Post-Pre')]
Average FC matrix CTRL (374, 123) non-numeric cells: 3 [(0, 0, 'Control gropu Pre'), (125, 0, 'Control group Post'), (250, 0, 'Control group Post-Pre')]
Circular plot (111, 54) non-numeric cells: 2 [(0, 0, 'DBS group FC average'), (56, 0, 'Control group FC average')]
Sham animal FC matrix (374, 123) non-numeric cells: 3 [(0, 0, 'Sham animal Pre'), (125, 0, 'Sham animal Post'), (250, 0, 'Sham animal Post-Pre')]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "import pypdf" 2>&1; python3 -c "import fitz" 2>&1; python3 -c "import pypdf; r=pypdf.PdfReader('paper/10.1038-s41593-026-02301-4.supp.pdf'); print(len(r.pages)); [print(i, r.pages[i].extract_text()[:300].replace(chr(10),' | ')) for i in range(len(r.pages))]" 2>&1 | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; uv pip install -q --python v/bin/python pypdf 2>&1|tail -1; v/bin/python -c "
import pypdf; r=pypdf.PdfReader('paper/10.1038-s41593-026-02301-4.supp.pdf'); print(len(r.pages))
t=[p.extract_text() for p in r.pages]
import re
for i,s in enumerate(t):
    if re.search('Supplementary Table 3|network',s,re.I): print(i, [m.start() for m in re.finditer('network',s,re.I)][:5], s[:200].replace(chr(10),' | '))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; $TMPDIR/v/bin/python - <<'E'
import dbs
for w in ["mkD","mkNT"]:
    d=dbs.seed_fc(w); d=d[d.time_condition==1]
    c=d.groupby(["side","roi"]).size().unstack(0)
    if w=="mkNT": c=c  # both subjects pooled
    for side in c.columns:
        lim=[1,5,8,9,10,11,12]
        print(w,"side",side,"LIM with 25:",c.loc[lim,side].sum(),"without:",c.loc[[r for r in lim if r!=8],side].sum())
E
grep -o -i ".\{100\}LIM.\{0,40\}n = .\{200\}" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i ".\{10\}438.\{200\}" paper/*.txt | head -3; grep -o -i "limbic network.\{300\}" paper/*.txt | head -5; grep -n "fig6e-monkey-d" -A30 claims/001773/*.yaml | sed -n 1,35p
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 885,900p claims/001773/*.yaml; grep -n "id: fig5c-dmn-lim-cen-decrease" -A35 claims/001773/*.yaml | grep -i -A6 "LIM\b\|area 25" | head -30
```

```
at P < 0.05, with the LIM readings. What "not observed" covers is open, (a) the sham
    side, (b) both sides; the paper's own legend lists significant control-side DMN and CEN
    differences without their direction. Reproduced when no DMN, LIM or CEN comparison of the
    sides the reading covers is a significant decrease; not reproduced when one is. If the
    readings disagree, blocked as methods_underspecified with both shown.
- id: ed10d-monkey-d-roi-changes
  statement: Among vmFC, PCC, anterior-dorsal insula and dACC, monkey D showed a significant
    pre against post difference in SCC connectivity only for the sham-side vmFC and the
    control-side anterior-dorsal insula.
  source: Extended Data Fig. 10d legend
  quote: A significant pre–post difference was observed in the sham side vmFC ( P = 7.83e-04)
    and control side anterior-dorsal insula
  statistics:
  - about: PrePost x side interaction, 17 target ROIs
    test: three-way ANOVA (DBS x side x target ROI)
    statistic: F(1,10106) = 4.58
638:- id: fig5c-dmn-lim-cen-decrease
639-  statement: After SCC-DBS, functional connectivity of the stimulated SCC with the hubs of the
640-    default mode, limbic and central executive networks decreased, with a significant PrePost x
641-    side interaction.
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o -i ".\{400\}SCC, dACC and PCC were counted as hubs.\{100\}" paper/*.txt | head -2; grep -o -i "Fig. 5c legend.\{0\}\|DMN, n = .\{300\}" paper/*.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd entries/001773-fujimoto-2026; sed -n 85,95p dbs.py; $TMPDIR/v/bin/python - <<'E'
import json
nb=json.load(open('reproduce_fujimoto_2026.ipynb'))
for i in [3,4,11,12,13,14,20,21,22,93,94,95,99,100,101]:
    print(i,'-----'); print(''.join(nb['cells'][i]['source']))
E
```

```
Tue Nov  3 17:14:00 UTC 2026


def text(path: str) -> str:
    return fetch(path).decode("utf-8", errors="replace")


# ---------------------------------------------------------------- loaders

def behavior() -> pd.DataFrame:
    d = sheet("source_data/dbs_behavior_data_a.xlsx", header=0).iloc[:, :6].dropna()
    return d.astype({"sec": int, "movement": int, "foraging": int, "mk": int, "stim": int, "group": int})
3 -----
ids = dbs.asset_ids()
import requests
latest = requests.get(f"{dbs.API}/dandisets/{dbs.DANDISET_ID}/", timeout=60).json()["most_recent_published_version"]["version"]
url = f"{dbs.API}/dandisets/{dbs.DANDISET_ID}/versions/{latest}/assets/?page_size=200"
ids_latest = {a["path"]: a["asset_id"] for a in requests.get(url, timeout=60).json()["results"]}
print(f"{len(ids)} assets at {dbs.DANDISET_VERSION}; {len(ids_latest)} at the latest published version {latest}")
print("same paths and asset ids in both versions:", ids == ids_latest)
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; sed -n 236,292p dbs.py
```

```
/bin/bash: line 1: cd: entries/001773-fujimoto-2026: No such file or directory


def tukey_kramer(fit: dict, dims: list, only_vary: str | None = None) -> pd.DataFrame:
    """Pairwise comparisons of population marginal means over `dims` (multcompare).

    The family is all pairs of the cells of `dims`, which sets the studentized range's number
    of means; `only_vary` returns only the pairs that differ in that factor alone (the pre
    against post pairs), which is faster and gives the same P values for those pairs.
    """
    levels, terms = fit["levels"], fit["terms"]
    combos = list(itertools.product(*[levels[f] for f in dims]))
    L = []
    for combo in combos:
        setting = dict(zip(dims, combo))
        row = [1.0]
        for t in terms:
            if all(f in setting for f in t):
                vecs = []
                for f in t:
[... 38 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001773-fujimoto-2026/dbs.py",
 "old_string": "    against post pairs), which is faster and gives the same P values for those pairs.\n    \"\"\"",
 "new_string": "    against post pairs), which is faster and gives the same P values for those pairs.\n    SciPy's studentized range tail loses accuracy below about 1e-7 and stops near 1e-11 (or\n    returns 0), so P values that small are only read as far below 0.05.\n    \"\"\""
}
```

```
The file entries/001773-fujimoto-2026/dbs.py has been updated successfully.
```

**Agent calls Bash**

```bash
$TMPDIR/v/bin/python - <<'E'
import json
fn='reproduce_fujimoto_2026.ipynb'
nb=json.load(open(fn))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def code(s,tag): return {"cell_type":"code","execution_count":None,"metadata":{"tags":[tag]} if tag else {},"outputs":[],"source":s.splitlines(keepends=True)}
def md(s): return {"cell_type":"markdown","metadata":{},"source":s.splitlines(keepends=True)}

# seed sheet: sessions and the script's loading lines
s=src(11)
s+='''
print("rows per voxel and session (N and T, D):",
      int(fcNT.groupby(["subject", "time_condition", "side", "roi", "x", "y", "z"]).size().max()),
      int(fcD.groupby(["time_condition", "side", "roi", "x", "y", "z"]).size().max()))
fig5_script = codes["code/Fig5BCandE9_dbs_FC_25norm_mkNT_analysisscript_a.m"].splitlines()
print("\\nFig5BCandE9 script, loading the sheet:")
print("\\n".join(f"{i:4d}: {l}" for i, l in enumerate(fig5_script, 1) if 7 <= i <= 15))'''
setsrc(11,s)
s=src(12)
old='''The file names say "concatenated":
the deposited seed maps were computed on concatenated runs, so the per-run reading in the claims
file cannot be run and is not needed (see deviations).'''
assert old in s
s=s.replace(old,'''Each voxel has one
value per session (the `date` column numbers the sessions, four for N and T and two for D), and the
script analyses the sheet as it is, with no run index. The deposited maps are therefore one per
session. The file names say "concatenated", which may refer to runs or to the subjects and ROIs
combined in one sheet, and the paper does not say whether runs were concatenated or their maps
averaged. Only this one version can be run (see deviations); its interaction F values are the
paper's.''')
setsrc(12,s)

# ed1 monkey D: the FigE1 script's selection
s=src(20)+'''

The FigE1 script's lines that select the rows of its ANOVA are printed first.'''
setsrc(20,s)
setsrc(21,'''fige1 = codes["code/FigE1_dbs_behavior_analysisscript_a.m"].splitlines()
print("FigE1 script, the ANOVA's rows (column 6 is group, column 4 monkey):")
print("\\n".join(f"{i:4d}: {l}" for i, l in enumerate(fige1, 1) if 10 <= i <= 20))
print("groups per monkey:", b.groupby("mk").group.unique().to_dict(), "\\n")
'''+src(21))
s=src(22)+''' The FigE1 script fits its ANOVA
only to the rows of group 1, monkeys N and T; monkey D's rows (group 2) enter only the plotted
means. The paper therefore ran no test for monkey D, and the test here is the criterion's.'''
setsrc(22,s)

# fig6c: rows pair a section and field
s=src(94)+'''
print("columns:", list(ccD.columns))
print("fields per section (each row is one section and field, both hemispheres):",
      ccD.groupby("slide").location.apply(list).to_dict(), "; distinct section and field pairs:",
      len(ccD[["slide", "location"]].drop_duplicates()))
fig6c = codes["code/Fig6C_dbs_IF_CC1_mkD_MCC_CB_analysisscript_a.m"].splitlines()
print("Fig6C script:"); print("\\n".join(f"{i:4d}: {l}" for i, l in enumerate(fig6c, 1) if 9 <= i <= 15))'''
setsrc(94,s)

# fig6e: LIM voxel counts against the legend
s=src(100)+'''
lim = dbs.NETWORKS["LIM"]
for side, n_legend in [(1, 438), (2, 383)]:
    v = fcD[(fcD.time_condition == 1) & (fcD.side == side)].groupby("roi").size()
    print(f"side {side}: LIM voxels with area 25 {v[lim].sum()}, without {v[[r for r in lim if r != dbs.AREA25]].sum()}; Fig. 6e legend {n_legend}")'''
setsrc(100,s)

# fig4c section after fig4b result (cell 53)
assert src(53).startswith("**Result: reproduced.** Under the amended")
new=[md('''## fig4c-network-sorted-reduction

> Sorted by cortical network membership, functional connectivity within and across networks was
> reduced after SCC-DBS.

The criterion needs the paper's code to assign the connectome's ROIs to networks. The Fig. 4
script's lines that name ROIs or draw the circular plot, and every text cell of the connectome
workbook, are printed.'''),
code('''fig4_script = codes["code/Fig4 Fujimoto_NatNeuro_2026_FCmatrix.m"].splitlines()
for i, line in enumerate(fig4_script, 1):
    if any(k in line.lower() for k in ("key", "reorder", "label_names", "circulargraph", "mycolormap", "network")):
        print(f"{i:4d}: {line.strip()}")
book = dbs.sheet("source_data/Source Data FC matrix.xlsx", sheet_name=None)
for name, d in book.items():
    print(f"sheet {name!r}, {d.shape}: text cells", [(r, c, v) for (r, c), v in np.ndenumerate(d.values) if isinstance(v, str)])''','claim:fig4c-network-sorted-reduction'),
md('''**Result: blocked (methods_underspecified).** The script reads the ROI names from atlas key
files and an order file (CHARM_key_4.txt, SARM_key_4.txt, reorder_rois.txt) that are not
deposited, draws the circular plot of the first 54 ROIs with one colour for decreases and one for
increases, and assigns no ROI to a network. The workbook's only text cells are block titles.
Supplementary Tables 3 and 4 name the ROIs but give no network. Without an assignment the
criterion blocks the claim.''')]
C[54:54]=new
json.dump(nb,open(fn,'w'),indent=1,ensure_ascii=False); open(fn,'a').write('\n')
E
git diff --stat
```

```
entries/001773-fujimoto-2026/dbs.py                |  2 +
 .../reproduce_fujimoto_2026.ipynb                  | 89 ++++++++++++++++++++--
 2 files changed, 83 insertions(+), 8 deletions(-)
```

**Agent calls Bash**

```bash
$TMPDIR/v/bin/python - <<'E'
import json
fn='reproduce_fujimoto_2026.ipynb'
nb=json.load(open(fn)); C=nb['cells']
for i,c in enumerate(C):
    s=''.join(c['source'])
    if s.startswith("**Result: blocked, the readings disagree."):
        s+=''' The legend's LIM voxel counts (438 sham, 383 control) are those with area 25 (428 and 375
without), as are the Fig. 5c counts (821, against 803), so the paper's n support reading (a); a
reader is asked whether reading (b) should stay. Under reading (a) alone the sham-side and
both-sides readings still disagree, so the block does not depend on it.'''
        c['source']=s.splitlines(keepends=True); print(i)
    if s.startswith("## Summary"): print(s)
json.dump(nb,open(fn,'w'),indent=1,ensure_ascii=False); open(fn,'a').write('\n')
E
git diff reproduce_fujimoto_2026.ipynb | head -30
```

```
104
## Summary

| Claim | Outcome |
|---|---|
| ed1-behavior-increase | reproduced |
| ed1-monkey-d-no-change | not reproduced |
| fig2a-cb-fa-increase | reproduced |
| fig2a-no-change-other-tracts | reproduced |
| ed2-cb-both-monkeys | reproduced |
| fig2b-mcc-cb-fa-increase | reproduced |
| fig3c-cc1-dapi-ratio | reproduced |
| ed5-cc1-count-dapi-unchanged | reproduced |
| ed6-dacc-ufm-no-oligodendrocyte-change | reproduced |
| fig3f-g-ratio-decrease | reproduced |
| fig4a-cortical-down-subcortical-up | reproduced |
| fig4b-roi-changes-counts | reproduced |
| fig4c-network-sorted-reduction | blocked (methods underspecified) |
| fig4-nonsurgical-no-pattern | reproduced |
| fig5a-pre-scc-connectivity | reproduced |
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/v/bin/python - <<'E'
import json
fn='reproduce_fujimoto_2026.ipynb'
nb=json.load(open(fn)); C=nb['cells']
for c in C:
    s=''.join(c['source'])
    if s.startswith("## Summary"):
        a='''The Tukey-Kramer P values agree with
the reported ones to about the second digit, and SciPy does not resolve P values below about
1e-11, which the paper prints as 0. The deposited seed maps come from concatenated runs, so the
claims file's per-run reading cannot be run.'''
        assert a in s
        s=s.replace(a,'''The Tukey-Kramer P values agree with
the reported ones to about the second digit down to about 1e-6. Below that SciPy's studentized
range tail is inexact (1.1 to 3 times the reported value between 1e-8 and 1e-11) and stops near
1e-11 or at 0, where the paper prints 0; no such P is near 0.05. The deposited seed maps are one
per session, and the paper does not say whether its runs were concatenated or averaged, so only
one of the claims file's two run readings can be run.''')
        c['source']=s.splitlines(keepends=True)
json.dump(nb,open(fn,'w'),indent=1,ensure_ascii=False); open(fn,'a').write('\n')
E
git diff --stat; grep -n -i "concatenat" README.md
```

```
entries/001773-fujimoto-2026/dbs.py                |   2 +
 .../reproduce_fujimoto_2026.ipynb                  | 102 ++++++++++++++++++---
 2 files changed, 92 insertions(+), 12 deletions(-)
```

**Agent calls Bash**

```bash
$TMPDIR/v/bin/python - <<'E'
import json
nb=json.load(open('reproduce_fujimoto_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    for k in ['oncatenat','floor','1.4e-11','1.7e-11']:
        if k in s: print(i,c['cell_type'],k,'|',[l for l in s.splitlines() if k in l][:3])
E
```

```
12 markdown oncatenat | ['session. The file names say "concatenated", which may refer to runs or to the subjects and ROIs', 'combined in one sheet, and the paper does not say whether runs were concatenated or their maps']
60 markdown oncatenat | ['stimulated hemisphere; (b) both hemispheres pooled. Only concatenated-run seed maps are deposited.']
63 markdown floor | ['at that floor.']
65 markdown floor | ['8.8e-06 (7.70e-06), PCC 4.5e-11, and vmFC, STG and DLPFC at the floor of the computation']
65 markdown 1.4e-11 | ['(1.4e-11; printed as 0 in the paper).']
68 markdown floor | ['floor, 1.4e-11; printed as 0).']
68 markdown 1.4e-11 | ['floor, 1.4e-11; printed as 0).']
80 markdown floor | ['0.035) at the floor of the computation (P below 1.7e-11).']
80 markdown 1.7e-11 | ['0.035) at the floor of the computation (P below 1.7e-11).']
83 markdown 1.7e-11 | ['**Result: reproduced.** The stimulated-side SMN rises from -0.017 to +0.003 with P below 1.7e-11']
108 markdown oncatenat | ['per session, and the paper does not say whether its runs were concatenated or averaged, so only']
```

**Agent calls Bash**

```bash
$TMPDIR/v/bin/python - <<'E'
import json
nb=json.load(open('reproduce_fujimoto_2026.ipynb'))
for i in [60,63]: print(i,''.join(nb['cells'][i]['source'])); print('---')
E
```

```
60 ## fig5a-pre-scc-connectivity

> Before stimulation, the SCC was positively connected with vmFC, dACC, PCC, STG, hippocampus,
> amygdala and DLPFC, and negatively with the insula and somatosensory cortex.

Pre-DBS normalized seed connectivity, mean over the ROI's voxels pooled over N and T: (a) in the
stimulated hemisphere; (b) both hemispheres pooled. Only concatenated-run seed maps are deposited.
---
63 ## fig5b-scc-decreases

> After SCC-DBS, functional connectivity of the stimulated SCC decreased with vmFC, PCC, STG,
> hippocampus, amygdala, DLPFC and dACC in the stimulated hemisphere, with a significant PrePost x
> side interaction.

Model of the Fig5BCandE9 script on the 17 target ROIs: subject, PrePost, side, ROI, and all
interactions of PrePost, side and ROI. Tukey-Kramer over the 68 cells. SciPy's studentized range
tail does not resolve P values below about 1e-11 (MATLAB prints them as 0); such P values are shown
at that floor.
---
```

**Agent calls Bash**

```bash
$TMPDIR/v/bin/python - <<'E'
import json
fn='reproduce_fujimoto_2026.ipynb'
nb=json.load(open(fn)); C=nb['cells']
def rep(i,a,b):
    s=''.join(C[i]['source']); assert a in s,(i,a); C[i]['source']=s.replace(a,b).splitlines(keepends=True)
rep(60,"Only concatenated-run seed maps are deposited.","Only one seed map per session is deposited\n(see the data check), so the run readings cannot both be run.")
rep(63,"""tail does not resolve P values below about 1e-11 (MATLAB prints them as 0); such P values are shown
at that floor.""","""tail loses accuracy below about 1e-7 (values there run up to three times the reported ones) and
does not resolve P values below about 1e-11 (MATLAB prints them as 0); such P values are shown at
that floor.""")
json.dump(nb,open(fn,'w'),indent=1,ensure_ascii=False); open(fn,'a').write('\n')
E
```

```
(Bash completed with no output)
```

**Agent**

Now run the entry (the README says it takes under a minute).

**Agent calls Bash**

```bash
cd  date -u; timeout 3000 python tools/entry.py all entries/001773-fujimoto-2026 2>&1 | tail -20; date -u
```

```
Tue Nov  3 17:15:05 UTC 2026
/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-001773-fujimoto-2026 in executed/001773-fujimoto-2026/.venv/share/jupyter/kernels/registry-001773-fujimoto-2026
0 error(s)
pass  reproduce_fujimoto_2026.ipynb  (41 s)
Tue Nov  3 17:15:54 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; $TMPDIR/v/bin/python - <<'E'
import json,uuid
fn='reproduce_fujimoto_2026.ipynb'
nb=json.load(open(fn)); print(nb['nbformat'],nb['nbformat_minor'], sum('id' in c for c in nb['cells']), len(nb['cells']))
for c in nb['cells']:
    if 'id' not in c: c['id']=uuid.uuid4().hex[:8]
json.dump(nb,open(fn,'w'),indent=1,ensure_ascii=False); open(fn,'a').write('\n')
E
git diff --stat
```

```
4 5 107 110
 entries/001773-fujimoto-2026/dbs.py                |   2 +
 .../reproduce_fujimoto_2026.ipynb                  | 113 ++++++++++++++++++---
 2 files changed, 100 insertions(+), 15 deletions(-)
```

**Agent**

Now read the new outputs in the executed copy.

**Agent calls Bash**

```bash
cd  ls executed/001773-fujimoto-2026/; $TMPDIR/v/bin/python - <<'E'
import json
nb=json.load(open('executed/001773-fujimoto-2026/reproduce_fujimoto_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    tags=c.get('metadata',{}).get('tags',[])
    if i in (11,) or any(t in tags for t in ['claim:ed1-monkey-d-no-change','claim:fig4c-network-sorted-reduction','claim:fig6c-monkey-d-cc1-no-change','claim:fig6e-monkey-d-no-network-reduction']):
        print('=====',i,tags)
        for o in c.get('outputs',[]): print(o.get('text','') if 'text' in o else o)
E
```

```
reproduce_fujimoto_2026.ipynb
result.json
===== 11 ['sanity']
['Seed connectivity voxels per target ROI (pre; post has the same counts):\n', '                          stim_N  stim_T  control_N  control_T  stim_pooled  D_side1_left  D_side2_right\n', '1 PCC                        138     111        111        138          249           138            111\n', '2 vmFC                        66      43         43         66          109            66             43\n', '3 STG                        249     250        250        249          499           249            250\n', '4 Anterior-dorsal Insula      49      51         51         49          100            49             51\n', '5 dACC                        88      74         74         88          162            88             74\n', '6 DLPFC                      387     379        379        387          766           387            379\n', '7 PPC                        165     171        171        165          336           165            171\n', '8 Area 25                     10       8          8         10           18            10              8\n', '9 Area 32                     30      18         18         30           48            30             18\n', '10 MCC                        56      45         45         56          101            56             45\n', '11 HIP                        59      73         73         59          132            59             73\n', '12 AMY                        57      54         54         57          111            57             54\n', '13 Sensory Cx                346     346        346        346          692           346            346\n', '14 Motor Cx                  231     215        215        231          446           231            215\n', '15 SMA                        60      41         41         60          101            60             41\n', '16 Visual Cx                 574     587        587        574         1161           574         
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l "^verifications:" attempts/*.yaml | head -3; f=$(grep -l "^verifications:" attempts/*.yaml | head -1); sed -n '/^verifications:/,$p' $f | head -50; ls schemas 2>/dev/null; grep -rn "verifications" docs/*.md | head
```

```
attempts/000003-senzai-2017-01.yaml
attempts/000004-chandravadia-2020-01.yaml
attempts/000005-yu-2016-01.yaml
verifications:
- date: '2026-10-16'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
    helper module and the claims file, with the paper. The verifier queried the archive metadata and tested
    helper functions on synthetic inputs. Its report had no attempt record and gave its own outcome for
    each claim; all 31 agree with the record.
  results:
  - claim: unit-counts
    agrees: true
    outcome: partially_reproduced
    reason: GC 609 is inside 527 to 645, but MC 568 is outside 450 to 550.
    response: No change needed.
  - claim: first-stage-labels
    agrees: true
    outcome: partially_reproduced
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties']['verifications'],indent=1)[:3000])
print(json.dumps(s['properties'].get('provenance'),indent=0)[:600])"; grep -n "author-answers\|answers" attempts/001773-fujimoto-2026-01.yaml | head
```

```
{
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "date",
   "kind",
   "by",
   "results"
  ],
  "properties": {
   "date": {
    "type": "string",
    "format": "date"
   },
   "kind": {
    "enum": [
     "agent",
     "person",
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> questions/001773.yaml <<'E'
- claim: fig6e-monkey-d-no-network-reduction
  asked: 2026-11-03
  question: The criteria of fig6e-monkey-d-no-network-reduction and fig5c-dmn-lim-cen-decrease
    run LIM with area 25 (reading a) and without it (reading b). The voxel counts the legends
    give fit only reading (a). In monkey D's seed table the LIM hubs sum to 438 voxels on the sham
    side and 383 on the control side with area 25, and 428 and 375 without it; the Fig. 6e legend
    gives 438 and 383. For N and T the sums are 821 with area 25 and 803 without, and the Fig. 5c
    legend gives 821. The Fig5BCandE9 script also lists ROI 8 (area 25) in LIM. Should reading (b)
    be dropped from both criteria, so that LIM is judged with area 25 only?
  passage: LIM, n = 438 (pre), 438 (post) ... control side ... LIM, n = 383 (Fig. 6e legend);
    LIM 821 per side (Fig. 5c legend, as the claims file's n for fig5c-dmn-lim-cen-decrease);
    SCC, dACC and PCC were counted as hubs for the LIM (blue hubs) as well (Fig. 5c legend).
  why: For fig5c-dmn-lim-cen-decrease both readings give the same outcome, reproduced. For
    fig6e-monkey-d-no-network-reduction reading (b) adds a sham-side LIM decrease (P = 6.9e-04).
    Under reading (a) alone the claim is still blocked, because the sham-side scope (0 of 3
    decreases) and the both-sides scope (control-side CEN decrease, P = 0.0089) disagree, so
    dropping (b) does not change an outcome in this attempt but removes one of the readings
    behind the block. The verifier of round 1 reported this.
E
$TMPDIR/v/bin/python -c "import yaml;d=yaml.safe_load(open('questions/001773.yaml'));print(len(d['questions']))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
cd  grep -o "LIM, n = 821.\{0,40\}" paper/*.txt | head -2; python3 -c "import yaml;d=yaml.safe_load(open('questions/001773.yaml'));print(len(d['questions']))"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o ".\{60\}821.\{60\}" paper/*.txt | head -4
```

Result: not kept, because it reads the paper's text.

**Agent**

Fix the passage to quote the legend exactly.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='questions/001773.yaml'; s=open(p).read()
a='''    LIM 821 per side (Fig. 5c legend, as the claims file's n for fig5c-dmn-lim-cen-decrease);
    SCC, dACC and PCC were counted as hubs for the LIM (blue hubs) as well (Fig. 5c legend).'''
assert a in s
s=s.replace(a,'''    stimulation side ... LIM, n = 821 (pre), 821 (post) ... control side ... LIM, n = 821 (Fig. 5c
    legend); SCC, dACC and PCC were counted as hubs for the LIM (blue hubs) as well (Fig. 5c
    legend, where SCC is area 25 and area 32).''')
open(p,'w').write(s)
import yaml; yaml.safe_load(open(p))
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='attempts/001773-fujimoto-2026-01.yaml'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,a
    s=s.replace(a,b)
rep('''    N and T), so the test is the claims file's reading of the Methods applied to one animal. The
    change in monkey D is a decrease, opposite to the increase of the DBS animals.''',
'''    N and T), so the test is the claims file's reading of the Methods applied to one animal. The
    deposited FigE1 script fits its ANOVA only to the rows of group 1 (N and T); monkey D's rows
    (group 2) enter only its plotted means, so the paper ran no test for monkey D. The change in
    monkey D is a decrease, opposite to the increase of the DBS animals.''')
rep('''- claim: fig4c-network-sorted-reduction
  outcome: blocked
  blocked_by: methods_underspecified
  notes:''','''- claim: fig4c-network-sorted-reduction
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_fujimoto_2026.ipynb
  output: claim:fig4c-network-sorted-reduction
  notes:''')
rep('''    The deposited circular plot sheet holds the 54 x 54 cortical block of each group's difference
    without network labels.''','''    The deposited circular plot sheet holds the 54 x 54 cortical block of each group's difference
    without network labels. The notebook prints the script's lines that read labels or draw the
    circular plot (one colour for decreases, one for increases, no grouping) and every text cell of
    the workbook (block titles only). Supplementary Tables 3 and 4 name the ROIs but give no
    network.''')
rep('''  deviations:
  - Only seed maps from concatenated runs are deposited (the files are named "concatenated"), so
    the per-run reading of the criterion cannot be run; the deposited maps are those the paper's
    scripts analyse.''','''  deviations:
  - The deposited seed tables hold one value per voxel and session (column date), and the paper's
    scripts analyse them as they are. The paper does not say whether a session's map comes from
    concatenated runs or from per-run maps averaged; the file name's "concatenated" may refer to
    runs or to subjects and ROIs combined in one sheet. Only this one version is deposited, so only
    one of the criterion's two run readings is run.''')
rep('''  - Concatenated-run seed maps only, as for fig5a-pre-scc-connectivity.
  - SciPy's studentized range tail does not resolve P below about 1e-11, so the smallest P values
    are shown at that floor; this cannot change an outcome at P < 0.05.''','''  - One seed map per session as deposited, as for fig5a-pre-scc-connectivity.
  - SciPy's studentized range tail loses accuracy below about 1e-7 (values there are 1.1 to 3
    times the reported ones, for example PCC 4.5e-11 against 8.22e-12) and does not resolve P
    below about 1e-11, where it prints a floor or 0; this cannot change an outcome at P < 0.05.''')
rep('''    and in T (7 of 7, -0.024 to -0.103). Concatenated-run maps only.''','''    and in T (7 of 7, -0.024 to -0.103). One seed map per session, as deposited.''')
rep('''  notes: Paired t(27) = -0.9888, P = 0.332, Cohen's dz -0.19 (the reported values); lead side 58.0 %
    against control 59.9 % (mean difference -1.86). The unpaired variant gives P = 0.47.''','''  notes: Paired t(27) = -0.9888, P = 0.332, Cohen's dz -0.19 (the reported values); lead side 58.0 %
    against control 59.9 % (mean difference -1.86). The unpaired variant gives P = 0.47. Each of the
    28 rows carries one section (slide D284, D294, D304, D314) and field (location 1 to 7), with
    the lead-side and control-side counts in the same row; the 28 section and field pairs are
    distinct.''')
rep('''    script settles LIM as including area 25.
  deviations:''','''    script settles LIM as including area 25. The Fig. 6e legend's LIM voxel counts (438 sham, 383
    control) are those with area 25 (428 and 375 without), so the paper's n support reading (a);
    a reader is asked whether reading (b) should stay (questions/001773.yaml). Under reading (a)
    alone the sham-side and both-sides scopes still disagree, so the block does not rest on (b).
  deviations:''')
rep('''  - Network membership is the script's (DMN PCC, vmFC, STG; SAN insula, dACC; CEN DLPFC, PPC; LIM
    PCC, dACC, area 25, area 32, MCC, HIP, AMY; SMN; VIS). The script settles LIM as reading (a);
    reading (b) is run as the criterion asks.''','''  - Network membership is the script's (DMN PCC, vmFC, STG; SAN insula, dACC; CEN DLPFC, PPC; LIM
    PCC, dACC, area 25, area 32, MCC, HIP, AMY; SMN; VIS). The script and the legend's LIM n (821
    with area 25, 803 without) settle LIM as reading (a); reading (b) is run as the criterion asks,
    and a reader is asked whether it should stay (questions/001773.yaml).''')
rep('''    decrease (P = 0.0089), and the Methods list LIM without area 25 while the script includes it.
    The authors could say which hemisphere and which LIM the sentence refers to.''','''    decrease (P = 0.0089). The Methods list LIM without area 25, while the script and the legend's
    voxel counts include it. The authors could say which hemisphere the sentence refers to.''')
rep('''- kind: other
  statement: Two scripts are deposited twice''','''- kind: methods_unavailable
  statement: The seed connectivity tables hold one value per voxel and session, and the file
    names say "concatenated". The paper does not say whether a session's seed map was computed on
    concatenated runs or averaged over per-run maps, and no per-run maps are deposited.
- kind: other
  statement: Two scripts are deposited twice''')
open(p,'w').write(s)
E
grep -n "Methods list LIM\|LIM without area" paper/*.txt | head -2; grep -o -i "limbic network (LIM).\{0,300\}hubs" paper/*.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; v/bin/python -c "
import pypdf,re; r=pypdf.PdfReader('paper/10.1038-s41593-026-02301-4.supp.pdf')
t=' '.join(p.extract_text() for p in r.pages[3:6]).replace(chr(10),' ')
for m in re.finditer('LIM|[Ll]imbic',t): print(t[max(0,m.start()-200):m.start()+300]); print('---')
" | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; v/bin/python -c "
import pypdf,re; r=pypdf.PdfReader('paper/10.1038-s41593-026-02301-4.supp.pdf')
t=' '.join(p.extract_text() for p in r.pages).replace(chr(10),' ')
for m in re.finditer('LIM|imbic|network hub',t): print(t[max(0,m.start()-200):m.start()+300]); print('---')
" | head -30; grep -o -i ".\{300\}hubs of.\{300\}" paper/*.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; v/bin/python -c "
import pypdf,re; r=pypdf.PdfReader('paper/10.1038-s41593-026-02301-4.supp.pdf')
t=' '.join(p.extract_text() for p in r.pages).replace(chr(10),' ')
i=t.find('4. ROI definitions'); print(t[i:i+1500])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i ".\{200\}(LIM.\{400\}" paper/*.txt | grep -v "blue for the" | head -3; grep -n "LIM" claims/001773/*.yaml | head -12
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 80,95p claims/001773/*.yaml
```

```
#   side" pools each monkey's own stimulated hemisphere. The voxel counts confirm this: the
#   pooled N and T count per side (e.g. DMN 857) equals monkey D's left plus right count
#   (453 + 404). Target ROIs are those of Supplementary Methods 4 with the voxel counts of
#   Supplementary Table 8; where an atlas label is ambiguous (STG, dorsal insula, HIP, AMY, V1,
#   MT), the definition whose pooled voxel count matches Table 8 is the one meant.
# - Network hubs (Methods): DMN = PCC, vmFC, STG; SAN = anterior-dorsal insula, dACC; CEN =
#   DLPFC, PPC; LIM = area 32, dACC, MCC, PCC, HIP, AMY; SMN = motor cortex, somatosensory
#   cortex, SMA; VIS = V1, MT. Voxels of a hub ROI used in two networks are counted in both.
#   The LIM count in Fig. 5c (821) equals the Methods list (803) plus area 25 (18), and the
#   Extended Data Fig. 9 legend counts SCC as a LIM hub; so LIM is open, (a) with area 25 (the
#   reported n) and (b) without (the Methods).
# - Whole-brain connectome (Fig. 4): AFNI 3dNetCorr on CHARM and SARM level 4 ROIs, 123 ROIs as
#   listed in Supplementary Tables 3 and 4, each with 122 values, the legends' n = 122
#   (hemispheres not separated in those lists; whether left and right ROIs are merged is not
#   stated), Fisher Z per run, averaged per condition, post
#   minus pre per subject, averaged across subjects.
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='questions/001773.yaml'; s=open(p).read()
a='''    legend gives 821. The Fig5BCandE9 script also lists ROI 8 (area 25) in LIM. Should reading (b)'''
assert a in s
s=s.replace(a,'''    legend gives 821. The claims file's header notes the Fig. 5c count and keeps (b) for the
    Methods' hub list; the Fig. 6e counts are a second legend that fits (a) only, and the
    Fig5BCandE9 script also lists ROI 8 (area 25) in LIM. Should reading (b)''')
open(p,'w').write(s)
import yaml; yaml.safe_load(open(p))
E
date -u
```

```
Tue Nov  3 17:17:16 UTC 2026
```

**Agent calls Bash**

```bash
cd  tail -5 attempts/001773-fujimoto-2026-01.yaml; grep -n "^verifications" attempts/001773-fujimoto-2026-01.yaml; sed -n '/^verifications:/,/^  results/p' attempts/000005-yu-2016-01.yaml | head -12
```

```
- kind: other
  statement: Two scripts are deposited twice under two names with identical text
    (`Fig4 Fujimoto_NatNeuro_2026_FCmatrix.m` and `Fig4andE10C_Fujimoto_NatNeuro_2026_FCmatrix.m`;
    `Fig6DandE10D_dbs_FC_25norm_mkD_analysisscript_a.m` and
    `Fig6DandE10Ddbs_FC_25norm_mkD_analysisscript_a.m`).
verifications:
- date: 2026-10-19
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook)
  reviewed: The handover of the first run, the executed notebook with the conclusions and summary
    removed, the helper module and the claims file. The verifier also read the paper's public page,
    with the supplementary legends.
  results:
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/ver.py <<'E'
import yaml
R = [
("ed1-behavior-increase","reproduced","Cell 18: movement F(1,236)=34.61, ηp²=0.128; foraging F=17.35, ηp²=0.068, all within tolerance. Reading (b) is also P<0.05. Post is higher than pre in both monkeys for both behaviors. Problem 5: the behavior sheet's legend codes foraging as 2/1, but the values are 0/1, and monkey D's rows are labeled group 2; the exact match of F confirms reading foraging as 1 = yes.",
 "No change needed. The legend coding is already recorded as a metadata_error finding and a deviation."),
("ed1-monkey-d-no-change","not_reproduced","Cell 20: foraging drops from 0.183 to 0.050, F(1,118)=5.32, P=0.023 (Fisher variant P=0.043). Movement does not differ (P=0.18). The criterion fails when either behavior differs. Problem 6 (affects a conclusion): this is the only claim that fails, and it rests on a test the paper never reports for monkey D, a one-way ANOVA treating the 120 bins as independent; the claims file fixes this test. The notebook does not show whether the deposited FigE1 script tests monkey D.",
 "Added to the claim's cell the FigE1 script's lines that select the ANOVA's rows (column 6, group, equal to 1) and the group of each monkey (N and T 1, D 2). The script tests only N and T; monkey D enters only its plotted means, so the paper ran no test for monkey D. Outcome kept, as the claims file fixes the test and its own header lists this reading as open; the notes say so."),
("fig2a-cb-fa-increase","reproduced","Cell 22: PrePost×side F=4.64, P=0.031, ηp²=0.00146, within tolerance; type II gives P=0.012. Stimulated CB Tukey P=0.022 with post higher. Voxel counts match the legend (cell 7).","No change needed."),
("fig2a-no-change-other-tracts","reproduced","Cell 24: none of the 5 comparisons has P<0.05 (smallest P=0.86).","No change needed."),
("ed2-cb-both-monkeys","reproduced","Cell 26: stimulated CB post−pre is +0.019 in N and +0.079 in T.","No change needed."),
("fig2b-mcc-cb-fa-increase","reproduced","Cell 28: F=5.42, P=0.020, ηp²=0.0040 (type II P=0.045). Stimulated MCC P=0.0018 with post higher; no other cell has a significant increase. MCC change is +0.081 in N and +0.205 in T.","No change needed."),
("fig3c-cc1-dapi-ratio","reproduced","Cell 30: F(1,108)=9.00, P=0.0034, ηp²=0.077; reading (b) and the ratio recomputed from counts agree. Stimulated side is higher in both monkeys (+5.5 and +5.0). Problem 4: the MCC-CB sheet has data errors; the ratio column is wrong for T423 fields 3 and 4, two fields have more CC1 than DAPI cells, and the variant using ratios recomputed from counts gives the same outcome.",
 "No change needed. The sheet errors are already recorded as a finding and the recomputed-ratio variant is shown."),
("ed5-cc1-count-dapi-unchanged","reproduced","Cell 32: CC1 F=6.22, P=0.014, ηp²=0.054, stimulated side higher. DAPI P=0.46. Both readings agree.","No change needed."),
("ed6-dacc-ufm-no-oligodendrocyte-change","reproduced","Cell 34: 0 of 6 reading (a) tests have P<0.05, and reading (b) agrees. UF/FM DAPI gives P=0.951 against the paper's printed 0.9611; the paper's own ηp² (4.97e-5) implies 0.951, so the printed value is a typo.","No change needed."),
("fig3f-g-ratio-decrease","reproduced","Cell 36: F(1,696)=58.98, P=5.4e-14, ηp²=0.078. Stimulated side is lower in N (−0.084) and T (−0.023). 700 axons, all with aspect ratio <2.","No change needed."),
("fig4a-cortical-down-subcortical-up","reproduced","Cell 38, DBS group: cortical −0.096 and subcortical +0.012 under (a); −0.052 and +0.006 under (b). The 54-ROI cortical split is confirmed from the order of Supplementary Table 3.","No change needed."),
("fig4b-roi-changes-counts","reproduced","Cells 40–41: with the script's rank-sum against zeros at 0.05/123, the counts are exactly 69 (DBS) and 44 (controls). The largest significant P is 3.88e-4, which matches the tables.","No change needed."),
("fig4c-network-sorted-reduction","blocked","No ROI-to-network assignment appears in the outputs. The criterion says to block in that case. Whether the Fig4 script or the \"Circular plot\" sheet assigns the 123 ROIs to networks was not checked; printing the script lines that build the circular plot's groups and colours, and the sheet's non-numeric cells, would settle it.",
 "Added a cell for the claim that prints the Fig. 4 script's lines that read labels, reorder ROIs or draw the circular plot, and every text cell of the connectome workbook. The script reads names from undeposited key files, draws the circular plot with one colour for decreases and one for increases, and assigns no network; the workbook's only text cells are block titles. Outcome kept, blocked."),
("fig4-nonsurgical-no-pattern","reproduced","Cell 43, controls: cortical +0.001 and subcortical −0.004 under (a); +0.001 and −0.001 under (b). The DBS pattern is absent under both readings.","No change needed."),
("fig5a-pre-scc-connectivity","reproduced","Cell 45: 9 of 9 signs match under (a) and (b). Only the deposited seed maps exist. Problem 3: the claims file asks for both per-run and concatenated seed maps; only one version is deposited. The notebook infers from the file name (\"concatenated_all_data\") that runs were concatenated; that name could equally mean all subjects and ROIs concatenated into one sheet, so the inference is unchecked. It does not matter here: the interaction F values match the paper exactly.",
 "Removed the inference. The data check now prints that each voxel has one value per session (column date) and the Fig5BCandE9 script's loading lines, which read the sheet with no run index. The notebook, the deviations and a new methods_unavailable finding now say the deposited maps are one per session and the paper does not say whether runs were concatenated or averaged. Outcome kept."),
("fig5b-scc-decreases","reproduced","Cell 47: interaction F=186.48, ηp²=0.0091, exactly the paper's values (type II F=56.2, also significant). All 7 stimulated-side ROIs decrease with P<0.05. Problem 2: SciPy's studentized_range.sf breaks down in the far tail; it prints a floor of about 1.4e-11 or 1.7e-11, or 0, and values just above the floor run 1.1 to 3× the paper's (8.4e-9 vs 5.07e-9, 3.6e-8 vs 1.3e-8, 4.5e-11 vs 8.2e-12). Every such P is orders of magnitude below 0.05.",
 "The helper's docstring, the notebook's text and summary, and the deviation now say the tail loses accuracy below about 1e-7 (1.1 to 3 times the reported values) as well as stopping near 1e-11 or 0. No outcome depends on such a P. Outcome kept."),
("fig5b-scc-increases","reproduced","Cell 49: insula +0.039 (P=6.8e-8) and somatosensory cortex +0.032 (P at the numerical floor).","No change needed."),
("ed9-control-hemisphere-changes","reproduced","Cell 51: 4 of 4 named ROIs are significant. 11 control-side ROIs are significant, the same list as Supplementary Table 9.","No change needed."),
("ed9-no-change-motor-mcc","reproduced","Cell 53: P=0.99992 (motor), 1.0 (SMA), 0.9918 (MCC), matching the paper's values.","No change needed."),
("ed7-decreases-both-monkeys","reproduced","Cell 55: all 7 are negative in both monkeys. N's AMY change is very small (−0.0006).","No change needed; the notes now say one seed map per session in place of concatenated runs."),
("fig5a-nonsurgical-no-reduction","blocked","The archive holds seed tables only for N+T and D. There are no seed maps for B, W or H and no voxelwise whole-brain maps, confirmed from the asset list. The control connectome includes an area 25 ROI row, but it is a 123-ROI measure, not the paper's voxelwise test.","No change needed."),
("fig5c-dmn-lim-cen-decrease","reproduced","Cell 57: F=51.09, ηp²=0.0023, exact. DMN, LIM and CEN decrease on the stimulated side under both LIM readings; type II is also significant. Voxel counts (857/821/…) match. Problem 1: the \"LIM without area 25\" reading is ruled out by the paper itself; the Fig. 6e legend counts for monkey D (sham LIM 438, control 383) equal the hub sums with area 25, and the helper says the script includes ROI 8. The claims file keeps reading (b) open, which misreads the reported n.",
 "Added a question for a reader (questions/001773.yaml) on whether reading (b) should be dropped from this criterion and that of fig6e-monkey-d-no-network-reduction; the claim is unchanged and both readings are still run. The deviation now says the legend's n settle LIM as reading (a). Outcome kept; it is the same under both readings."),
("fig5c-smn-increase","reproduced","Cell 59: stimulated-side SMN +0.020, P at the numerical floor, under both readings.","No change needed."),
("fig5c-vis-no-change","reproduced","Cell 61: VIS P=1.0 (stimulated) and 0.65/0.23 (control). Stimulated-side V1 P=1.0 and MT P=0.999.","No change needed."),
("fig5c-san-rebalanced","reproduced","Cells 63/49: stimulated-side SAN P=1.0. Insula increases (P=6.8e-8) and dACC decreases (P=4.9e-4).","No change needed."),
("fig6a-monkey-d-cb-fa-decrease","reproduced","Cell 65: three-way interaction F(2,1238)=6.02, P=0.0025, ηp²=0.0096. Sham CB decreases (P=8.4e-9); none of the other 5 comparisons has P<0.05.","No change needed."),
("fig6b-monkey-d-dacc-cb-decrease","reproduced","Cell 67: F=24.55, ηp²=0.0475. Sham dACC decreases (P=3.6e-8). Sham MCC goes down, not up (P=0.44).","No change needed."),
("fig6c-monkey-d-cc1-no-change","reproduced","Cell 69: t(27)=−0.9888, P=0.3316, dz=−0.19, identical to the paper. That rows pair the same section and field across hemispheres was not checked; printing the cc1_mkD() columns would show it. The exact t match makes this low-risk.",
 "Added to the claim's cell the sheet's columns, the fields of each section and the count of distinct section and field pairs (28), and the Fig6C script's ttest lines. Each row carries one slide and location with both hemispheres' counts. Outcome kept."),
("ed10c-monkey-d-subcortical-decrease","reproduced","Cell 71: subcortical −0.035 under (a) and −0.022 under (b).","No change needed."),
("fig6d-monkey-d-scc-local-increase","blocked","The archive has no voxelwise whole-brain map for D and no lead coordinates; D's seed table covers only 17 target ROIs. Monkey D's sham-side area 25 rises (0.55 to 0.74, P=4e-12), but sham vmFC and HIP decrease significantly, so an ROI-level reading would fail the \"no decrease\" half anyway.","No change needed."),
("fig6e-monkey-d-no-network-reduction","blocked","Cell 73: under the LIM-with-area-25 reading, the sham side shows 0 significant decreases (reproduced), but both sides together show the control-side CEN decrease (P=0.0089, not reproduced). The claims file's rule blocks when readings disagree. Problem 1: the Fig. 6e legend counts (sham LIM 438, control 383) equal the hub sums with area 25, so the reading without area 25 is ruled out by the paper; fig6e stays blocked because the sham-side and both-sides readings still disagree under reading (a).",
 "Added to the claim's cell the LIM voxel counts with and without area 25 against the legend (438 and 383 with, 428 and 375 without), and a question for a reader on dropping reading (b). The notes, the conclusion and the methods_unavailable finding now say the block does not rest on reading (b). Outcome kept, blocked."),
("ed10d-monkey-d-roi-changes","reproduced","Cell 75: interaction F=4.58, P=0.032. Of the 8 comparisons, exactly sham vmFC (P=8.0e-4) and control insula are significant.","No change needed."),
]
results=[{"claim":c,"agrees":True,"outcome":o,"reason":r,"response":p} for c,o,r,p in R]
v=[{"date":"2026-11-03","kind":"agent",
 "by":"Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)",
 "reviewed":"Round 1. The handover of the run after the reader's answer on fig4b-roi-changes-counts, the executed notebook with the conclusion cells and the summary removed, the helper module and the claims file, with the paper. The verifier queried the archive's asset list and tested the helper's anova and tukey_kramer on synthetic data against statsmodels and scipy.stats.tukey_hsd. It gave its own outcome for each claim; all 32 agree with the record.",
 "results":results}]
txt=yaml.safe_dump({"verifications":v},sort_keys=False,allow_unicode=True,width=100,default_flow_style=False)
p='attempts/001773-fujimoto-2026-01.yaml'
s=open(p).read()
assert 'verifications:' not in s
open(p,'a').write(txt)
E
$TMPDIR/v/bin/python -c "import yaml" 2>/dev/null || uv pip install -q --python $TMPDIR/v/bin/python pyyaml; $TMPDIR/v/bin/python $TMPDIR/ver.py && tail -30 attempts/001773-fujimoto-2026-01.yaml
```

```
agrees: true
    outcome: reproduced
    reason: 'Cell 71: subcortical −0.035 under (a) and −0.022 under (b).'
    response: No change needed.
  - claim: fig6d-monkey-d-scc-local-increase
    agrees: true
    outcome: blocked
    reason: The archive has no voxelwise whole-brain map for D and no lead coordinates; D's seed table
      covers only 17 target ROIs. Monkey D's sham-side area 25 rises (0.55 to 0.74, P=4e-12), but sham
      vmFC and HIP decrease significantly, so an ROI-level reading would fail the "no decrease" half anyway.
    response: No change needed.
  - claim: fig6e-monkey-d-no-network-reduction
    agrees: true
    outcome: blocked
    reason: 'Cell 73: under the LIM-with-area-25 reading, the sham side shows 0 significant decreases
      (reproduced), but both sides together show the control-side CEN decrease (P=0.0089, not reproduced).
      The claims file''s rule blocks when readings disagree. Problem 1: the Fig. 6e legend counts (sham
      LIM 438, control 383) equal the hub sums with area 25, so the reading without area 25 is ruled out
      by the paper; fig6e stays blocked because the sham-side and both-sides readings still disagree under
      reading (a).'
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/001773-fujimoto-2026 2>&1 | tail -5; python tools/entry.py check entries/001773-fujimoto-2026 2>&1 | tail -5; git status --short
```

```
Installed kernelspec registry-001773-fujimoto-2026 in executed/001773-fujimoto-2026/.venv/share/jupyter/kernels/registry-001773-fujimoto-2026
0 error(s)
pass  reproduce_fujimoto_2026.ipynb  (41 s)
0 error(s)
 M attempts/001773-fujimoto-2026-01.yaml
 M entries/001773-fujimoto-2026/dbs.py
 M entries/001773-fujimoto-2026/reproduce_fujimoto_2026.ipynb
 M questions/001773.yaml
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
?? scripts
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('entries/001773-fujimoto-2026/reproduce_fujimoto_2026.ipynb'));print(sum(len(c.get('outputs',[])) for c in nb['cells']))"; git diff | grep "^+" | grep -n -i "—\|rather" | head
```

```
0
```

**Agent**

No outcome changed. The round-1 verifier agreed with all 32 outcomes: 27 reproduced, 1 not reproduced (`ed1-monkey-d-no-change`) and 4 blocked. I re-ran the entry with `python tools/entry.py all entries/001773-fujimoto-2026`: it passed in 41 s, `check` reports 0 errors, and every number in the conclusions is the same as before.

**Outputs the verifier asked for, now in the notebook:**
- **`ed1-monkey-d-no-change`:** the notebook now prints the FigE1 script's row selection. Its ANOVA uses only group 1 (monkeys N and T); monkey D's rows (group 2) appear only in the plotted means. So the paper never tested monkey D, and the outcome stays not reproduced under the claims file's test. The notes say this.
- **`fig4c-network-sorted-reduction`:** a new section prints the Fig. 4 script's label, reordering and circular-plot lines, and every text cell of the connectome workbook. None of them assigns ROIs to networks: the only text cells are block titles, and the plot uses one colour for decreases and one for increases. The claim stays blocked (`methods_underspecified`), and the record now points to this cell.
- **`fig6c-monkey-d-cc1-no-change`:** the notebook prints the sheet's columns and the Fig6C `ttest` lines. Each of the 28 rows holds a distinct section and field, with both hemispheres' counts.
- **Seed maps (problem 3):** the data check shows one value per voxel per session (the `date` column) and prints the Fig5BCandE9 lines that load the sheet.

**Corrections:**
- **"Concatenated runs":** I removed the inference that the seed maps come from concatenated runs. The notebook, its summary, the deviations for `fig5a-pre-scc-connectivity`, `fig5b-scc-decreases` and `ed7-decreases-both-monkeys`, and a new `methods_unavailable` finding now say the maps are one per session. The paper does not say whether runs were concatenated or averaged.
- **Tukey-Kramer far tail (problem 2):** the helper's docstring, the notebook text and summary, and the `fig5b` deviation now say SciPy's P values lose accuracy below about 1e-7 (1.1 to 3 times the paper's values), not only below the 1e-11 floor. No outcome depends on such a P.
- **LIM with or without area 25 (problem 1):** I added a question to `questions/001773.yaml` asking whether the reading without area 25 should be dropped from the criteria of `fig5c-dmn-lim-cen-decrease` and `fig6e-monkey-d-no-network-reduction`. The Fig. 6e voxel counts (438 and 383) and the Fig. 5c count (821) fit only the reading with area 25. The `fig6e` cell now prints these counts. The claim is unchanged and both readings are still run. `fig6e` stays blocked either way, because with area 25 the sham-side and both-sides scopes still disagree. I also updated the `fig6e` notes and its `methods_unavailable` finding.
- **Round 1 in the record:** it is under `verifications`, with the verifier's reasons in its own words and my response for each claim.

**Not done:**
- Problems 4 and 5 (the CC1 sheet errors and the behavior legend coding) were already recorded as findings, so nothing new was needed.
- `fig5a-nonsurgical-no-reduction` and `fig6d-monkey-d-scc-local-increase` stay blocked for missing data. The ROI-level look the verifier mentions is not the criterion's test, and it would fail `fig6d` anyway.

Nothing is committed, as instructed.

## End of run

60 turns, 8 minutes, $2.56 at API prices, result: success.
