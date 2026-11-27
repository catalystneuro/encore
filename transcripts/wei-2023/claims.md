# wei-2023 · claims · run 44934410023

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls; ls paper claims | head -50; grep -n "^#" docs/protocol.md
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,198p docs/protocol.md; ls paper | grep -i wei;
```

```
# Protocol for an attempt

Version: `pilot-18`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 177 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la paper; cat papers/datasets/wei-2023.yaml 2>/dev/null; head -80 claims/fouke-2025.yaml; wc -l claims/fouke-2025.yaml
```

```
total 2084
drwxr-xr-x  2 runner runner    4096 Nov 21 18:21 .
drwxr-xr-x 21 runner runner    4096 Nov 21 18:21 ..
-rw-r--r--  1 runner runner 1496326 Nov 21 18:21 10.1038-s41467-023-37844-8.supp-41467_2023_37844_MOESM1_ESM.pdf
-rw-r--r--  1 runner runner  420642 Nov 21 18:21 10.1038-s41467-023-37844-8.supp-41467_2023_37844_MOESM3_ESM.xlsx
-rw-r--r--  1 runner runner  204482 Nov 21 18:21 10.1038-s41467-023-37844-8.txt
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1038/s41467-023-37844-8
title: Associations between in vitro, in vivo and in silico cell classes in mouse primary visual cortex.
datasets:
- archive: dandi
  id: '000021'
  relation: reuses
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 80,321p claims/fouke-2025.yaml | grep -n -E "^- id|^  [a-z_]+:|^checks|^[a-z]" | head -80; head -30 paper/*.txt; grep -n -i -E "^(supplement|methods|results|discussion|references|data availability|code availability)" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1038-s41467-023-37844-8.txt; wc -l -c $f; awk '{print NR": "length($0)}' $f | sort -t: -k2 -n -r | head -5; head -c 1500 $f
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper text is there; a supplement PDF and a source-data spreadsheet are with it. Reading the text now.

**Agent calls Bash**

```bash
cd  f=paper/10.1038-s41467-023-37844-8.txt; fold -s -w 200 $f > $TMPDIR/wei.txt; wc -l $TMPDIR/wei.txt; grep -n -i -E "supplementary (note|information|fig)" $TMPDIR/wei.txt | head -20; tail -c 3000 $f
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/wei.txt",
 "limit": 330
}
```

```
1	DOI: 10.1038/s41467-023-37844-8
2	Version: version of record
3	Source: find_reuse cache
4	Stored: 2026-11-10
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	pmc Nat Commun Nat Commun Nature Communications 2041-1723 Nature Publishing Group UK London 10126114 37095130 37844 10.1038/s41467-023-37844-8 Article Associations between in vitro, in vivo and in 
8	silico cell classes in mouse primary visual cortex Wei Yina [removed: an e-mail address] 1 2 Nandi Anirban 2 Jia Xiaoxuan 2 3 http://orcid.org/0000-0002-7736-4844 Siegle Joshua H. 2 Denman Daniel 4 
9	http://orcid.org/0000-0001-8224-0144 Lee Soo Yeun 2 Buchin Anatoly 2 5 http://orcid.org/0000-0002-2915-720X Van Geit Werner 6 Mosher Clayton P. 7 http://orcid.org/0000-0002-9568-7057 Olsen Shawn 2 
10	http://orcid.org/0000-0002-6793-0611 Anastassiou Costas A. [removed: an e-mail address] 7 8 9 10 1 grid.510538.a 0000 0004 8156 0818 Zhejiang Lab, Hangzhou, 311100 China 2 grid.417881.3 0000 0001 2298 
11	2461 Allen Institute for Brain Science, Seattle, WA 98109 USA 3 grid.12527.33 0000 0001 0662 3178 School of Life Sciences/McGovern Institute for Brain Research, Tsinghua University, 100084 Beijing, 
12	China 4 grid.266239.a 0000 0001 2165 7675 University of Denver, Denver, CO 80208 USA 5 grid.511032.4 Cajal Neuroscience Inc, Seattle, WA 98102 USA 6 Blue Brain Project, École Polytechnique Fédérale 
13	de Lausanne (EPFL) Campus Biotech, Geneva, 1202 Switzerland 7 grid.50956.3f 0000 0001 2152 9905 Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA 90048 USA 8 grid.50956.3f 0000 
14	0001 2152 9905 Department of Neurology, Cedars-Sinai Medical Center, Los Angeles, CA 90048 USA 9 grid.50956.3f 0000 0001 2152 9905 Board of Governors Regenerative Medicine Institute, Cedars-Sinai 
15	Medical Center, Los Angeles, CA 90048 USA 10 grid.50956.3f 0000 0001 2152 9905 Center for Neural Science and Medicine, Department of Biomedical Sciences, Cedars-Sinai Medical C
[... 315 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/wei.txt",
 "offset": 330,
 "limit": 250
}
```

```
330	drifting gratings in head-fixed animals) and differential coupling to ongoing LFP oscillations. Looking at the properties of these finer clusters with the cortical depth, we found increased diversity 
331	in their spike-LFP coupling. RS3, for example, exhibits almost double the coupling strength of RS1 in the supragranular region for beta and low gamma (RS2 is an intermediate case). On the other hand, 
332	in the infragranular region and for low gamma, RS3 and RS1 spike phase is similar, while RS2 comes earlier (the same happens for high gamma). The differences in RS1-3 are consistent with classes of 
333	neurons that possess different biophysical setups as well as a divergence in connectivity patterns. It is known, for example, that the biophysical properties of excitatory V1 neurons vary and depend 
334	on cortical depth, which, in turn, is expected to have an impact on their firing properties and burstiness 1 , 34 , 46 , 47 . In addition, their intricate connectivity and projections along the 
335	anatomical hierarchy can result in a spectrum of functional clusters among excitatory V1 cells that reflect upstream input segregation from earlier brain regions (e.g., various thalamic areas 34 , 48 
336	, 49 ). The combination of diverging biophysical properties of V1 excitatory cells combined with localized and class-specific connectivity gives rise to functionally distinct and input-specific RS1–3 
337	clusters. Furthermore, behavior and brain state can further modulate the response properties of excitatory clusters along V1 34 . The aforementioned points to a network consisting of clusters of 
338	distinct biophysical properties and functional in vivo responses that, nevertheless, can be organized and reconfigured in multiple ways, depending on the external input and internal state. While 
339	excitatory cells exhibit differences in visual responses (though with varying degrees of sensitivity and selectivity), inhibitory neurons do not show strong or selective 
[... 240 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 579,600p $TMPDIR/wei.txt | grep -n -i -E "code|data availability|github" ; grep -n -o -i -E ".{200}(code availability|data availability).{600}" $TMPDIR/wei.txt | head
```

```
3:models. Y.W. wrote the analysis codes. X.J., J.H.S, D.D., and S.O. contributed the Neuropixels data. Y.W., A.N., and C.A.A. wrote the paper with input from all of the other authors (A.B., C.P.M., 
5:Data availability The in vivo Neuropixels Dataset is available for download in Neurodata Without Borders (NWB) format via the AllenSDK 23 : 
9:https://allensdk.readthedocs.io/en/latest/_static/examples/nb/ecephys_optotagging.html . Source data are provided in this paper (see Source data set). Source data are provided in this paper. Code 
10:availability The codes for calculating EAP features and clustering cell classes were custom written in Python and are made available on GitHub ( https://github.com/yinawei/Mouse_V1_EAP_Analysis ) 
11:with DOI (10.5281/zenodo.7679748). The all-active mouse single-neuron models were generated using a Python pipeline and are also available on GitHub ( 
12:https://github.com/yinawei/Mouse-all-active-models-EAP ) with DOI (10.5281/zenodo.7679762). Competing interests The authors declare no competing interests. References 1. Gouwens NW Classification of
```

**Agent calls Bash**

```bash
cd  sed -n 580,592p $TMPDIR/wei.txt; sed -n 1060,1200p $TMPDIR/wei.txt
```

```
Institute founder, Paul G. Allen. Author contributions C.A.A. conceptualized this work. Y.W. and C.A.A. performed the research. A.N., W.V.G., and C.A.A. wrote the software to develop the all-active 
models. Y.W. wrote the analysis codes. X.J., J.H.S, D.D., and S.O. contributed the Neuropixels data. Y.W., A.N., and C.A.A. wrote the paper with input from all of the other authors (A.B., C.P.M., 
S.Y.L., X.J., and J.H.S.). Peer review Peer review information Nature Communications thanks Dirk Feldmeyer and the other anonymous reviewer(s) for their contribution to the peer review of this work. 
Data availability The in vivo Neuropixels Dataset is available for download in Neurodata Without Borders (NWB) format via the AllenSDK 23 : 
https://allensdk.readthedocs.io/en/latest/visual_coding_neuropixels.html . The Neurodata Without Borders files is also available on the DANDI Archive 23 : 
https://gui.dandiarchive.org/#/dandiset/000021 . The in vitro electrophysiology data and the reconstructed morphology used to generate single-cell models are available at: 
https://celltypes.brain-map.org . The cell ID used in the paper is listed in Table S1 . The optotagging experimental data set with Pvalb and Sst neurons is available at: 
https://allensdk.readthedocs.io/en/latest/_static/examples/nb/ecephys_optotagging.html . Source data are provided in this paper (see Source data set). Source data are provided in this paper. Code 
availability The codes for calculating EAP features and clustering cell classes were custom written in Python and are made available on GitHub ( https://github.com/yinawei/Mouse_V1_EAP_Analysis ) 
with DOI (10.5281/zenodo.7679748). The all-active mouse single-neuron models were generated using a Python pipeline and are also available on GitHub ( 
https://github.com/yinawei/Mouse-all-active-models-EAP ) with DOI (10.5281/zenodo.7679762). Competing interests The authors declare no competing interests. References 1. Gouwens NW Classification of 
electrophysiologi
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1200,1300p $TMPDIR/wei.txt | cut -c1-400; grep -n -i "Source Data\|Sheet\|^Fig" $TMPDIR/wei.txt | sed -n 1,60p | cut -c1-200
```

```
Table S1.  Metadata about origin of experimental in vitro data used to generate singlecell models. In vitro electrophysiology data and the reconstructed morphology are generated 
for each whole-cell patched neuron from mouse primary visual cortex. Data for each 
experiment available online (https://celltypes.brain-map.org). 
 
Cell ID 
Cre lines 
Layer 
Dendrite type 
1 
395830185 
Scnn1a 
L4 
spiny 
2 
476218657 
Scnn1a 
L4 
spiny 
3 
320207387 
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1300,1380p $TMPDIR/wei.txt | cut -c1-300; grep -n "^### Sheet" $TMPDIR/wei.txt
```

```
469801569 
Pvalb 
L5 
aspiny 
20 
469610831 
Pvalb 
L5 
aspiny 
21 
396608557 
Pvalb 
L5 
aspiny 
22 
333604946 
Pvalb 
L2/3 
aspiny 
23 
[... 64 more lines not kept]
```

**Agent**

The text, Methods, supplementary figures S1 to S8 and Table S1 are all present. Next I'll list the source-data sheets and clone the analysis code.

**Agent calls Bash**

```bash
cd  grep -n "Table S2" $TMPDIR/wei.txt | head; python3 -c "
import openpyxl
wb=openpyxl.load_workbook('paper/10.1038-s41467-023-37844-8.supp-41467_2023_37844_MOESM3_ESM.xlsx',read_only=True)
for ws in wb.worksheets: print(ws.title, ws.max_row, ws.max_column)
" 2>&1 | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls .venv 2>/dev/null | head -2; uv run --no-sync python -c "import openpyxl" 2>&1 | tail -1; cd $TMPDIR && git clone -q https://github.com/yinawei/Mouse_V1_EAP_Analysis && cd Mouse_V1_EAP_Analysis && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -80
```

```
ModuleNotFoundError: No module named 'openpyxl'
1e35126f1e521b4c98e9ba5fd6a4a8abce70530a Tue Aug 10 11:11:02 2021 +0800
./LICENSE.txt
./README.md
./Examples/ecp_func.py
./Examples/Exp_Model_Classifier.ipynb
./Examples/data/model_features.csv
./Examples/data/wt_EAP_data_info/771160300unitinfo.csv
./Examples/data/wt_EAP_data_info/757216464unitinfo.csv
./Examples/data/wt_EAP_data_info/754312389unitinfo.csv
./Examples/data/wt_EAP_data_info/766640955unitinfo.csv
./Examples/data/wt_EAP_data_info/761418226unitinfo.csv
./Examples/data/wt_EAP_data_info/797828357.npy
./Examples/data/wt_EAP_data_info/774875821.npy
./Examples/data/wt_EAP_data_info/757970808unitinfo.csv
./Examples/data/wt_EAP_data_info/761418226.npy
./Examples/data/wt_EAP_data_info/778240327unitinfo.csv
./Examples/data/wt_EAP_data_info/750332458unitinfo.csv
./Examples/data/wt_EAP_data_info/821695405.npy
./Examples/data/wt_EAP_data_info/760345702.npy
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Mouse_V1_EAP_Analysis; find . -type f -not -path './.git/*' -not -path '*/wt_EAP_data_info/*'; cat README.md; ls Examples/data/wt_EAP_data_info | grep -c unitinfo; head -3 Examples/data/wt_EAP_data_info/771160300unitinfo.csv | cut -c1-600; head -3 Examples/data/exp_features.csv | cut -c1-400
```

```
./LICENSE.txt
./README.md
./Examples/ecp_func.py
./Examples/Exp_Model_Classifier.ipynb
./Examples/data/model_features.csv
./Examples/data/exp_features.csv
./Examples/data/.DS_Store
./Examples/.DS_Store
./Examples/sankey.py
./Examples/NP_EAP_FeatureAnalysis.ipynb
Associations between in vitro, in vivo and in silico cell classes in mouse primary visual cortex (Wei et al, 2021)

Code base for mouse V1 Neurpixels EAP data analysis

* Method is presented in Wei et al. (2021): 

## Dependencies
 * Python 3.6+
 * AllenSDK
 * pandas
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Mouse_V1_EAP_Analysis/Examples; python3 - <<'E'
import json
for nb in ['NP_EAP_FeatureAnalysis.ipynb','Exp_Model_Classifier.ipynb']:
    d=json.load(open(nb))
    print('=====',nb)
    for i,c in enumerate(d['cells']):
        src=''.join(c['source'])
        if c['cell_type']=='markdown': print(f'--- md {i}\n{src}')
        else:
            print(f'--- code {i}\n{src}')
            for o in c.get('outputs',[]):
                t=o.get('text') or o.get('data',{}).get('text/plain')
                if t: print('>>OUT', ''.join(t)[:600])
E
```

```
===== NP_EAP_FeatureAnalysis.ipynb
--- code 0
# ==================================================================================
# Function: Read EAP matrix, extract EAP features and run EAP feature clusters
# The code reproduces Fig.2d
# @Author: Yina Wei, 2021
#==================================================================================
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from time import time
from scipy import stats
import ecp_func as ef # import self-written sub functions  

plt.rcParams.update({'font.size': 9})
sns.set_style("whitegrid", {'axes.grid' : False})
my_pal_FSRS = {0:[5/255.0,23/255.0,182/255.0],1:[23/255.0,163/255.0,95/255.0],2:[213/255.0,9/255.0,21/255.0],3:[254/255.0,200/255.0,46/255.0]}
[... 727 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Mouse_V1_EAP_Analysis/Examples; wc -l ecp_func.py; cat ecp_func.py
```

```
613 ecp_func.py
# ==================================================================================
# It icludes all the subfunctions
# @Author: Yina Wei, 2021
#==================================================================================
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy import signal
from scipy.ndimage.filters import gaussian_filter
from sklearn import linear_model
from scipy.stats import shapiro  # Shapiro-Wilk Test
from scipy.stats import mannwhitneyu,ttest_ind # Mann-Whitney U test
from sklearn import preprocessing
import scikit_posthocs as sp
from scipy.interpolate import make_interp_spline
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
import scikit_posthocs as sp
[... 590 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -o -i -E ".{150}(isolat|quality|snr|isi_viol|amplitude cutoff|presence ratio).{150}" $TMPDIR/wei.txt | head; grep -n -o -E ".{100}(drifting gratings|spontaneous).{100}" $TMPDIR/wei.txt | head -30
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  f=paper/10.1038-s41467-023-37844-8.txt; head -c 120000 $f | grep -o -i -E ".{150}(isolat|quality|snr|violation|cutoff|presence).{150}" | head; head -c 120000 $f | grep -o -E ".{80}spontaneous.{80}" | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000021/versions/draft/info/ | python3 -c "import json,sys; d=json.load(sys.stdin); m=d.get('metadata',d); print(m.get('name')); print(m.get('description')); print(d.get('version'))" 2>&1 | head -30; ls paper | grep -i desc
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  uv run --no-project --with openpyxl python -c "
import openpyxl
wb=openpyxl.load_workbook('paper/10.1038-s41467-023-37844-8.supp-41467_2023_37844_MOESM3_ESM.xlsx',read_only=True)
for ws in wb.worksheets:
    rows=list(ws.iter_rows(values_only=True))
    print('##',ws.title,len(rows))
    for r in rows[:4]: print('  ',[c for c in r if c is not None][:14])
" 2>&1 | tail -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  uv run --no-project --with openpyxl --with pandas python -c "
import pandas as pd
x=pd.read_excel('paper/10.1038-s41467-023-37844-8.supp-41467_2023_37844_MOESM3_ESM.xlsx',sheet_name=None)
for s in ['Fig 1d','Fig1g','Fig3c','FigS7','Fig3de','FigS6']:
    print('##',s); print(x[s].to_string())
d=x['Fig2d']; print(d.columns.tolist()); print(d.iloc[:,2].value_counts())
for s in ['Fig3a_rate_cv_lv','Fig3a_stimulus_metrics']:
    d=x[s]; print(s, d.groupby('cell_type_str').median(numeric_only=True).to_string())
d=x['FigS3ab']; print(d.groupby(d.columns[4])['Spike rate'].describe())
d=x['Fig7deg']; print(d.groupby('cell_type').median().to_string()); print(d.cell_type.value_counts())
d=x['Fig7h']; print(d.groupby('cell_type').median(numeric_only=True))
d=x['Fig6a']; print(d.groupby('str_label').describe().to_string())
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=/home/runner/.claude/projects/-home-runner-work-encore-encore/33d582f7-b09a-49a3-a041-ac47ed0e0125/tool-results/bmpbvuwc8.txt; sed -n 30,1000p $f | cut -c1-250 | grep -v "^ *[0-9]* *NaN *NaN" | head -150
```

```
22          16.0     771990200                  40               NaN
23          17.0     774875821                  50               NaN
24          18.0     778240327                  63               NaN
25          19.0     778998620                  44               NaN
26          20.0     779839471                  86               NaN
27          21.0     781842082                  54               NaN
28          22.0     793224716                  47               NaN
29          23.0     799864342                  49               NaN
30          24.0     847657808                  30               NaN
33           NaN       unit_id  Cortical depth(um)               NaN
34           0.0     915960297                -280               NaN
35           1.0     915960294                -280               NaN
36           2.0     915960283                -280               NaN
37           3.0     915960275                -280               NaN
38           4.0     915960317                -260               NaN
39           5.0     915960312                -260               NaN
40           6.0     915960300                -260               NaN
41           7.0     915960337                -240               NaN
42           8.0     915960356                -220               NaN
43           9.0     915960392                -180               NaN
[... 130 more lines not kept]
```

**Agent**

The source data has unit IDs, cluster labels and per-unit values for most panels. I'll pull just the summaries I need.

**Agent calls Bash**

```bash
cd  uv run --no-project --with openpyxl --with pandas python -c "
import pandas as pd
x=pd.read_excel('paper/10.1038-s41467-023-37844-8.supp-41467_2023_37844_MOESM3_ESM.xlsx',sheet_name=None)
d=x['Fig 1d']; print(d.iloc[6:31,2].astype(int).sum())
for s in ['Fig1g','Fig3c','FigS7','Fig3de','FigS6']:
    print('##',s); print(x[s].to_string())
d=x['Fig2d']; print(d.iloc[:,2].value_counts().to_dict())
for s in ['Fig3a_rate_cv_lv','Fig3a_stimulus_metrics']:
    d=x[s]; print(s, d.cell_type_str.value_counts().to_dict()); print(d.groupby('cell_type_str').median(numeric_only=True).to_string())
d=x['FigS3ab']; print(d.columns.tolist()); print(d.groupby(d.columns[4])['Spike rate'].describe())
d=x['Fig7deg']; print(d.groupby('cell_type').median().to_string()); print(d.cell_type.value_counts())
d=x['Fig7h']; print(d.groupby('cell_type').median(numeric_only=True))
d=x['Fig6a']; print(d.groupby('str_label')['Symmetry index'].describe().to_string())
d=x['Fig6b']; print(d.groupby('cre_lines').describe().to_string())
d=x['FigS4ab']; print(d.groupby('cell_type')[['Spread','1/V_below','1/V_above']].median().to_string())
"
```

Result: not kept, because it reads the paper's text.

**Agent**

I have what I need from the paper, its code and the source data. Before writing the claims file I'll check the claims schema and the quote checker.

**Agent calls Bash**

```bash
cd  ls schemas; python3 -c "
import json,glob
for f in glob.glob('schemas/*claim*'):
    print(f); print(open(f).read()[:6000])
"; sed -n 1,60p tools/claims_check.py
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
schemas/claims.schema.json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Claims proposed for one target (a dataset and one of its papers)",
  "description": "Draft. To be revised after the pilot.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "paper",
    "claims"
  ],
  "properties": {
    "schema_version": {
      "const": 2
    },
[... 198 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
s=json.load(open('schemas/claims.schema.json'))
p=s['properties']['claims']['items']['properties']
for k in list(p)[list(p).index('datasets'):]: print(k, json.dumps(p[k])[:400])
print(json.dumps(s['\$defs'])[:3000])
print([k for k in s['properties']])
"; grep -l "readings" claims/*.yaml | head -3
```

```
datasets {"description": "Only when the paper is tested on more than one dataset: the folder names of those this claim rests on.", "type": "array", "items": {"type": "string"}, "minItems": 1}
{"expected": {"type": "object", "additionalProperties": false, "required": ["quantity", "value"], "properties": {"quantity": {"type": "string"}, "value": {"type": "number"}, "tolerance": {"type": "number", "minimum": 0}, "unit": {"type": "string"}}}, "statistic": {"type": "object", "additionalProperties": false, "anyOf": [{"required": ["p"]}, {"required": ["ci"]}], "properties": {"about": {"description": "What the test compares or the interval bounds, when the claim has more than one, e.g. 'GPi against VLa onset times'.", "type": "string"}, "test": {"description": "The test as the paper names it, e.g. 'Wilcoxon rank-sum', 'two-tailed t-test'.", "type": "string"}, "statistic": {"description": "The test statistic as reported, e.g. 't(14) = 3.2', 'F(2, 40) = 5.1', 'r = 0.38'.", "type": "string"}, "p": {"description": "The reported p-value as printed, or its bound when the paper gives one ('p < 0.05' is p 0.05 with p_relation '<'). A paper that prints 'P = 0' (below the precision it reports) is recorded as 0.", "type": "number", "minimum": 0, "maximum": 1}, "p_relation": {"description": "How p was reported: exactly (the default) or as a bound.", "enum": ["=", "<", ">"]}, "corrected": {"description": "The correction for multiple comparisons the paper applied, e.g. 'Bonferroni', 'FDR'.", "type": "string"}, "ci": {"type": "object", "additionalProperties": false, "required": ["low", "high"], "properties": {"level": {"description": "The confidence level, e.g. 0.95.", "type": "number", "exclusiveMinimum": 0, "exclusiveMaximum": 1}, "low": {"type": "number"}, "high": {"type": "number"}, "unit": {"type": "string"}}}, "n": {"description": "The sample the test was run on, in words, e.g. '206 GPi and 179 VLa units'.", "type": "string"}}}}
['schema_version', 'dataset', 'paper', 'claims', 'chec
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -t claims | head -5; f=$(grep -l "Provenance\|written by an agent" claims/*.yaml | head -1); echo $f; sed -n 1,40p $f
```

```
zheng-2024.yaml
zhong-2026.yaml
zhuang-2025.yaml
zhang-2021.yaml
zheng-2022.yaml
claims/dijk-2018.yaml
# Claims for van Dijk & Fenton (2018), "On How the Dentate Gyrus Contributes to Memory
# Discrimination", Neuron 98, 832-845, on CRCNS hc-17.
#
# Provenance: written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
# Actions"), 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read: the version of record (paper/10.1016-j.neuron.2018.04.018.txt, supplied by a
# person, extracted from the PDF), the main text, figure legends, STAR Methods (e1 to e5) and
# the Supplemental Information (Figures S1 and S2 with legends, Tables S1 and S2). No figure
# was read from a PDF page. The CRCNS data descriptor (hc-17.data-description.txt) was read
# only to know which experiments the dataset holds; no claim comes from it.
#
# Code read: the Data and Software Availability section links
# https://github.com/FentonLab/Mcode_DG-MemoryDiscrimination-NeuronMS. At commit
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q --depth 1 https://github.com/yinawei/Mouse-all-active-models-EAP && cd Mouse-all-active-models-EAP && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | sed 's|/[^/]*$||' | sort | uniq -c | head -30; cat README.md | head -40
```

```
f1a426867032527e1ed5cbdf87eb56e9f7fa65ef Tue Aug 10 16:29:19 2021 +0800
      2 .
      1 ./examples
      4 ./examples/395830185
      2 ./examples/NWB_files
      1 ./examples/biophys_components
      1 ./examples/biophys_components/biophysical_neuron_templates
     23 ./examples/biophys_components/mechanisms/modfiles
     51 ./examples/biophys_components/mechanisms/x86_64
      1 ./examples/biophys_components/mechanisms/x86_64/.libs
      1 ./examples/biophys_components/morphologies
      2 ./examples/biophys_components/point_neuron_templates
      1 ./examples/biophys_components/recXelectrodes
      2 ./examples/biophys_components/stimulations
      6 ./examples/biophys_components/synaptic_models
Associations between in vitro, in vivo and in silico cell classes in mouse primary visual cortex (Wei et al, 2021)

## Instructions

* 1)  Create a virtual environment
[... 36 more lines not kept]
```

**Agent**

Now writing the claims file: about 48 claims covering the in vivo clustering, function, phase-locking, optotagging, and the model and in vitro findings (the last marked as data held elsewhere).

**Agent calls Write**

```json
{
 "file_path": "claims/wei-2023.yaml",
 "content": "# Claims for Wei, Nandi, Jia, Siegle, Denman, Lee, Buchin, Van Geit, Mosher, Olsen & Anastassiou\n# (2023), \"Associations between in vitro, in vivo and in silico cell classes in mouse primary\n# visual cortex\", Nature Communications 14, 2344, on DANDI:000021.\n#\n# Provenance: written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub\n# Actions\"), 2026-11-21, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read: the version of record (paper/10.1038-s41467-023-37844-8.txt, from PubMed Central),\n# its main text, figure legends and Methods; the Supplementary Information (Figures S1 to S8\n# with legends, Table S1), which the same text file holds; and the Source Data workbook\n# (41467_2023_37844_MOESM3_ESM.xlsx, read from the copy under paper/). The supplement PDF\n# (MOESM1) was not opened, as its text was legible. Table S2, cited for the visual stimulus\n# metrics, is not in the supplement text; Table 2 of the Methods names the same three metrics.\n# Fig 3d, 3e, S6 and the opto kappa and phase are given in the Source Data only as pickle files\n# (wt_phase_locking_df2.pickle, Fig7h_opto_kappa_phase.pickle) that are not supplied, and the\n# main-figure PDF is not supplied, so the significance stars of the main figures could not be\n# read. Statistics are recorded as the text and legends give them.\n#\n# Code read (Code availability). https://github.com/yinawei/Mouse_V1_EAP_Analysis at commit\n# 1e35126f1e521b4c98e9ba5fd6a4a8abce70530a (2021-08-10; Zenodo doi:10.5281/zenodo.7679748).\n# It holds Examples/NP_EAP_FeatureAnalysis.ipynb (EAP features and K-means clusters, Fig 2d),\n# Examples/Exp_Model_Classifier.ipynb (the FS/RS and AP/SP classifiers, Fig 4f to h; the\n# README calls them Fig 3c,f,g,h, from an earlier figure numbering), Examples/ecp_func.py (the\n# helper functions) and data: per-session mean waveforms (Examples/data/wt_EAP_data_info/\n# <session>.npy, units x 82 samples x 40 channels) with unit tables (<session>unitinfo.csv:\n# good flag, unit id, fr_5min, fr, depth relative to layer 4), exp_features.csv (features and\n# cluster labels of the 1204 units) and model_features.csv (features of the 33 models). The\n# code starts from these prepared files; how waveforms, the good flag, fr_5min and depth were\n# taken from the NWB files is not in it. No code for Fig 3, Fig 5 to 7, the phase-locking or\n# the optotagging is in it. https://github.com/yinawei/Mouse-all-active-models-EAP at commit\n# f1a426867032527e1ed5cbdf87eb56e9f7fa65ef (2021-08-10; Zenodo doi:10.5281/zenodo.7679762)\n# holds the BMTK/NEURON set-up to simulate one example model (cell 395830185).\n#\n# Method details the code fixes (NP_EAP_FeatureAnalysis.ipynb, ecp_func.py), followed below:\n# - Sessions: the 25 wild-type session ids listed in the notebook (732592105, 739448407,\n#   744228101, 750332458, 750749662, 754312389, 754829445, 757216464, 757970808, 759883607,\n#   761418226, 763673393, 766640955, 767871931, 768515987, 771160300, 771990200, 774875821,\n#   778240327, 778998620, 779839471, 781842082, 793224716, 799864342, 847657808); the Source\n#   Data (sheet Fig 1d) lists the same ids with unit counts summing to 1204.\n# - Waveforms: 40 channels around the peak channel; every second channel (one per 20 um row,\n#   the two columns on one side) gives 20 sites, the peak at index 10; each trace high-passed\n#   at 300 Hz (5th-order Butterworth, filtfilt) at 30 kHz; time axis sample*1/30 ms - 0.6 ms;\n#   cubic spline to 10000 points for feature timing.\n# - Features: TPW from the trough (minimum between -1 and 2.5 ms) to the following maximum;\n#   REP from that peak to the half-peak after it; 1/V below and above as the slope (times\n#   1000, ms/mm) of trough time against distance over sites within 100 um whose amplitude is at\n#   least max(0.5% of the peak amplitude, 5); spread from the 12% amplitude points of a spline\n#   of amplitude against distance; symmetry index |1/V below + 1/V above| / sqrt(2).\n# - Exclusions after the good flag and a hard-coded list of 38 unit ids: peak channel not at\n#   the centre, values beyond 3 SD of the mean in half width, TPW, REP, the two W slopes or the\n#   two 1/V features, trough time more than 0.1 ms from 0, amplitude below 15 or above 300.\n#   1287 good units became 1204.\n# - Clustering: features median-imputed and z-scored; K-means (k-means++, 1000 initialisations)\n#   for K = 1 to 9; the elbow is the largest ratio of successive WCSS differences, f(K) as in\n#   Methods eq. 5-6, the optimum its minimum. Two clusters on TPW and REP; then each of FS and\n#   RS clustered on 1/V below and 1/V above (z-scored over all units) with K from f(K).\n# - Classifiers (ecp_func.classifier): features z-scored, minority class upsampled with\n#   replacement to balance; 100 stratified 75/25 splits for each of 100 resamplings; linear SVC\n#   (C = 1, balanced weights) for two classes, random forest (20 trees, gini) for more; label\n#   by most frequent prediction.\n# - Two- and three-group tests (two_sample_test, three_sample_test): Shapiro-Wilk on each group\n#   at 0.05; t-test or Mann-Whitney U for two groups; one-way ANOVA with Holm-corrected t-tests,\n#   or Kruskal-Wallis with Holm-corrected Mann-Whitney tests (scikit_posthocs), for three.\n#\n# Data the paper used (Results; Methods, In vivo neuropixels recordings; Source Data).\n# - The Allen Brain Observatory Visual Coding Neuropixels dataset, via the AllenSDK and DANDI\n#   000021. Awake head-fixed mice on a running disc; V1 recorded with Neuropixels probes (384\n#   sites, 30 kHz, KiloSort2 spike sorting); stimuli named are flashes, drifting gratings and a\n#   mean-luminance gray screen (spontaneous). 25 wild-type C57BL/6J mice (24 male, 1 female),\n#   8 Pvalb-IRES-Cre x Ai32 (6 male, 2 female), 12 Sst-IRES-Cre x Ai32 (8 male, 4 female).\n#   The paper does not say which of the Visual Coding stimulus sets each session belongs to;\n#   the dandiset's title names the Brain Observatory 1.1 stimulus set only, so the author\n#   finds which of the 25 sessions, and which opto-tagging mice, it holds.\n# - Units: 1204 V1 units from the 25 wild-type mice (Source Data Fig2d gives each unit id and\n#   its cluster label, TPW, REP and 1/V features). Fig 3 uses units with EAP amplitude above\n#   50 uV and at least 100 spikes (745 RS for rate, CV and LV; 768 RS for the grating metrics;\n#   203 FS and 745 RS for phase-locking). Depth relative to the layer 4 centre found from the\n#   first CSD sink to flashes (Fig S1). LFP bands theta 3-8, alpha 8-12.5, beta 12.5-30, low\n#   gamma 30-50, high gamma 50-90 Hz (Results) or 8-12 and 12-30 Hz for alpha and beta\n#   (Methods). Optotagging with 10 ms square light pulses.\n# - Outside the dataset: 33 all-active single-cell models (15 spiny, Cre lines 5 Nr5a1, 4\n#   Scnn1a, 6 Rorb; 18 aspiny, 9 Pvalb, 9 Sst) fitted to cells of the Allen Cell Types Database\n#   (celltypes.brain-map.org, cell ids in Table S1), with their in vitro electrophysiology and\n#   reconstructed morphologies. The models are in the second repository (Zenodo\n#   doi:10.5281/zenodo.7679762); their simulated EAP features are in model_features.csv of the\n#   first (Zenodo doi:10.5281/zenodo.7679748) and in the Source Data.\n#\n# Details the paper and code leave open, with the readings named in the criteria:\n# - unit isolation (\"well-isolated\", \"see Methods\", but the Methods give no criteria);\n# - which recording period gives fr_5min, the FS/RS firing rate (Fig S3b);\n# - the drifting-grating period and spike sets for Fig 3 and how ISIs are pooled;\n# - the method of the ISI-median confidence interval;\n# - the LFP channel (\"different neighboring electrodes\"), the band filter, which spikes form\n#   the 10,000-spike cap, the alpha and beta band edges, and what \"kappa\" is (the text says it\n#   ranges from 0 to 1, which a von Mises concentration does not);\n# - the boundaries of the supragranular, granular and infragranular regions;\n# - the opto-tagging baseline window and unit selection.\nschema_version: 2\npaper: doi:10.1038/s41467-023-37844-8\nclaims:\n- id: source-data-units-link\n  kind: link\n  statement: The 1204 unit ids of the paper's Source Data, with their one- and multi-channel\n    cluster labels, are units of the dataset's wild-type V1 recordings.\n  source: Source Data, sheets Fig 1d and Fig2d; NP_EAP_FeatureAnalysis.ipynb session list\n  data: with_labels\n  criterion: Each unit id of Source Data sheet Fig2d is looked up in the units tables of the\n    dataset's sessions among the 25 the code lists. The link holds (reproduced) when the\n    dataset holds all 25 sessions and every one of the 1204 ids is found, with the per-session\n    counts of sheet Fig 1d, in the VISp structure. It is partially reproduced when the dataset\n    holds only some of the 25 sessions and every id of those sessions is found; the number of\n    sessions and units held is then reported, and every claim judged on the dataset is judged\n    on that subset, as a deviation. It is not reproduced when ids of sessions the dataset holds\n    are missing or lie outside V1.\n- id: fig1d-unit-count\n  statement: The analysis rests on 1204 well-isolated V1 units from 25 wild-type mice, an\n    average of 48 units per mouse.\n  source: Results, EAP recordings from in vivo experiments and biophysical models of cell\n    types, paragraph 1; Figure 1d\n  quote: We only analyzed units located in V1 with an average of 48 units per wild-type mouse\n    being well-isolated (unit isolation criteria... the total number of units = 1204) during\n    spontaneous activity\n  expected:\n  - quantity: well-isolated V1 units from wild-type mice\n    value: 1204\n    tolerance: 120.4\n  - quantity: mean units per wild-type mouse\n    value: 48\n    tolerance: 4.8\n  depends_on:\n  - source-data-units-link\n  criterion: Units in VISp of the 25 sessions the code lists, then the code's exclusions (the\n    hard-coded list of 38 ids, peak channel off centre, 3 SD outliers in the seven features,\n    trough time beyond 0.1 ms, amplitude outside 15 to 300). The isolation step that sets the\n    code's good flag is not stated in the paper or code; two readings are run, (a) the\n    AllenSDK default unit filter the paper's stated access route applies (isi_violations <\n    0.5, amplitude_cutoff < 0.1, presence_ratio > 0.9), (b) every VISp unit the NWB units\n    table lists. The claim is reproduced when either reading gives counts within the\n    tolerances. Figure 1d's legend gives 24 wild-type mice and \"204\" units; the text and\n    Source Data give 25 and 1204, used here.\n- id: fig2-one-channel-two-clusters\n  statement: K-means clustering of the one-channel features TPW and REP gives two clusters as\n    the optimum by both the elbow method and the density function, a narrow-waveform cluster\n    with short REP and a wide-waveform cluster with long REP.\n  source: Results, The standard waveform features reveal two clusters, paragraph 1; Figure 2c,d\n  quote: Both the elbow method and density method of unsupervised K -means clustering 22\n    independently confirmed the optimal number of clusters is two.\n  depends_on:\n  - fig1d-unit-count\n  criterion: TPW and REP of each unit as the code computes them; median-imputed and z-scored;\n    K-means (k-means++, 1000 initialisations) for K = 1 to 9; elbow and f(K) as in\n    ecp_func.selectionK_kmeans and findElbow. Reproduced when both select K = 2 and the\n    cluster with the lower median TPW also has the lower median REP; partially when only one\n    method selects 2.\n- id: fig2-fs-rs-counts\n  statement: Of the 1204 units, 281 (23.3%) fall in the narrow-waveform (FS) cluster and 923\n    (76.7%) in the wide-waveform (RS) cluster.\n  source: Results, The standard waveform features reveal two clusters, paragraph 1; Figure 2d\n  quote: narrow waveform units ( n = 281, 23.3%) exhibit elevated spike frequency vs. wide\n    waveform ones ( n = 923, 76.7%)\n  expected:\n  - quantity: FS units\n    value: 281\n    tolerance: 28.1\n  - quantity: RS units\n    value: 923\n    tolerance: 92.3\n  - quantity: FS fraction\n    value: 23.3\n    tolerance: 2.33\n    unit: percent\n  depends_on:\n  - fig2-one-channel-two-clusters\n  criterion: Counts of the two clusters of fig2-one-channel-two-clusters. When the unit set\n    differs from the 1204 of the Source Data, the fraction is the measure; the agreement of\n    the cluster labels with the Source Data labels on the shared units is also reported.\n- id: figs3b-fs-faster\n  statement: FS units fire faster than RS units, at a median of 4.85 Hz (IQR 1.93 to 10.79\n    Hz) against 2.05 Hz (IQR 0.84 to 5.00 Hz).\n  source: Results, The standard waveform features reveal two clusters, paragraph 1; Figure S3b\n  quote: narrow waveform units spike at a median firing rate of 4.85 Hz (interquartile range,\n    IQR... 1.93-10.79 Hz) while wide waveform units fire at a median of 2.05 Hz (IQR... 0.84-5.00\n    Hz). Thus, narrow waveform units spike significantly faster than their wide waveform\n    counterparts (Mann-Whitney U test, p = 3.5 x 10 -18\n  statistics:\n  - test: Mann-Whitney U test, two-sided\n    p: 3.5e-18\n    n: 281 FS and 923 RS units\n  expected:\n  - quantity: FS median firing rate\n    value: 4.85\n    tolerance: 0.485\n    unit: Hz\n  - quantity: RS median firing rate\n    value: 2.05\n    tolerance: 0.205\n    unit: Hz\n  depends_on:\n  - fig2-fs-rs-counts\n  criterion: Rate as N / T (Methods, Single unit firing properties). The code uses a column\n    fr_5min whose period is not stated; the text ties the 1204 units to spontaneous activity.\n    Readings, (a) the spontaneous (gray screen) block of the session, (b) the first 5 minutes\n    of the recording, (c) the whole session (Methods, N / T during the recording session).\n    Reproduced when, under a reading, both medians fall within tolerance and the two-sided\n    Mann-Whitney U test gives p < 0.001 with FS higher.\n- id: fig2-rs-more-asymmetric\n  statement: RS units have more asymmetric EAP propagation below against above the soma than\n    FS units.\n  source: Results, Spatial features reveal six distinct sub-clusters, paragraph 1; Figure 2c,d;\n    Figure S3c,d\n  quote: Looking at the multi-channel EAP features of FS vs. RS, RS generally exhibits a more\n    asymmetric EAP propagation below vs. above the putative soma location than FS\n  depends_on:\n  - fig2-fs-rs-counts\n  criterion: The paper reports no test. The symmetry index of Methods (distance of (1/V below,\n    1/V above) from the line y = -x) per unit. Reproduced when the RS median exceeds the FS\n    median and the paper's two-sample procedure (Shapiro-Wilk, then t-test or Mann-Whitney U,\n    Methods, Statistical analysis; ecp_func.two_sample_test) gives p < 0.05.\n- id: fig2d-three-subclusters-each\n  statement: Clustering FS and RS separately on the multi-channel features 1/V below and 1/V\n    above gives three clusters in each, FS1 to FS3 (130, 82 and 69 units) and RS1 to RS3 (479,\n    235 and 209 units).\n  source: Results, Spatial features reveal six distinct sub-clusters, paragraph 2; Figure 2d\n  quote: Unsupervised clustering ( K -means) indicated that the optimal number of\n    multi-channel clusters within FS and RS is three for each\n  expected:\n  - quantity: FS1 units\n    value: 130\n    tolerance: 13\n  - quantity: FS2 units\n    value: 82\n    tolerance: 8.2\n  - quantity: FS3 units\n    value: 69\n    tolerance: 6.9\n  - quantity: RS1 units\n    value: 479\n    tolerance: 47.9\n  - quantity: RS2 units\n    value: 235\n    tolerance: 23.5\n  - quantity: RS3 units\n    value: 209\n    tolerance: 20.9\n  depends_on:\n  - fig2-fs-rs-counts\n  - source-data-units-link\n  criterion: As the code, 1/V below and 1/V above z-scored over all units, then K-means within\n    each of FS and RS with K from f(K) (the code takes nc = argmin f(K) + 1), the elbow also\n    reported. Clusters are named by greatest overlap with the Source Data labels on shared\n    units. Reproduced when both methods give K = 3 in FS and in RS and the six counts are\n    within tolerance; partially when K = 3 in both but counts are off. Label agreement with\n    the Source Data is reported.\n- id: figs4-rs1-faster-above\n  statement: RS1 and RS2 both propagate asymmetrically and differ mainly in supragranular\n    propagation velocity, faster in RS1 than in RS2.\n  source: Results, Spatial features reveal six distinct sub-clusters, paragraph 2; Figure S4b\n  quote: For the RS group, RS1 and RS2 show mostly asymmetric propagation, with their main\n    difference being the supragranular propagation velocity, i.e., V above (RS1) > V above (RS2)\n  depends_on:\n  - fig2d-three-subclusters-each\n  criterion: Reproduced when the RS1 median of 1/V above is below the RS2 median (faster\n    V above) and the paper's three-group procedure (ecp_func.three_sample_test) gives a\n    Holm-corrected RS1 against RS2 p < 0.05 for 1/V above.\n- id: figs4-rs-spread\n  statement: RS1 to RS3 differ in spatial spread, RS3 being the most spatially confined.\n  source: Results, Spatial features reveal six distinct sub-clusters, paragraph 2; Figure S4b\n    legend\n  quote: Comparison of spread among RS1-3, Kruskal-Wallis Htest, F=48.2, p = 3.34*10-11\n  statistics:\n  - test: Kruskal-Wallis H-test, Holm-Bonferroni corrected post hoc\n    statistic: F = 48.2\n    p: 3.34e-11\n    corrected: Holm-Bonferroni\n    n: 479 RS1, 235 RS2, 209 RS3\n  depends_on:\n  - fig2d-three-subclusters-each\n  criterion: Spread as the code (extent above 12% of the peak amplitude along the probe).\n    Reproduced when the Kruskal-Wallis test gives p < 0.05 and the RS3 median spread is the\n    smallest of the three. The text also says RS3 has a faster infragranular velocity; its\n    sign convention for 1/V below is not stated, so it is reported, not judged.\n- id: figs4-fs-spread-absent\n  statement: FS1 to FS3 show no significant difference in spatial spread.\n  source: Results, Spatial features reveal six distinct sub-clusters, paragraph 2; Figure S4a\n    legend\n  quote: Comparison of spread among FS1-3, Kruskal-Wallis Htest, F=0.457, p=0.795\n  statistics:\n  - test: Kruskal-Wallis H-test\n    statistic: F = 0.457\n    p: 0.795\n    n: 130 FS1, 82 FS2, 69 FS3\n  depends_on:\n  - fig2d-three-subclusters-each\n  criterion: A claim of absence, judged on the paper's test. Kruskal-Wallis H-test of spread\n    across FS1 to FS3. Reproduced when p >= 0.05, not reproduced when p < 0.05; the medians\n    are reported either way.\n- id: figs5-depth-distribution\n  statement: The six multi-channel clusters are distributed differently along the V1 depth\n    axis.\n  source: Results, Spatial features reveal six distinct sub-clusters, paragraph 2; Figure S5\n  quote: Looking at the distribution of the cortical depth, the six clusters are distributed\n    differently across V1 layers\n  depends_on:\n  - fig2d-three-subclusters-each\n  criterion: The paper reports no test. Depth relative to the layer 4 centre, taken at the\n    first CSD sink after flash onset (Fig S1). How the CSD is computed and the sink located is\n    not stated, and the code starts from a precomputed depth; readings, (a) the standard\n    second spatial derivative of the flash-averaged LFP with the earliest sink in V1 as the\n    centre, (b) the CCF layer 4 midpoint of the probe in the session's channel table. The\n    paper's multi-group procedure (Methods, Statistical analysis; Kruskal-Wallis or one-way\n    ANOVA) across the six clusters. Reproduced when it gives p < 0.05 under a reading.\n- id: fig3a-isi-fs-rs\n  statement: During drifting gratings the ISI median of FS units is 19.63 ms (95% CI 19.60 to\n    19.67) and that of RS units 53.37 ms (95% CI 53.30 to 53.43), a significant difference.\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 1;\n    Figure 3a\n  quote: the ISI median of FS is 19.63 ms with a 95% confidence interval (CI) at [19.60-19.67]\n    ms, while the ISI median of RS is 53.37 ms with 95% CI at [53.30-53.43] ms (Fig. 3a ,\n    Mann-Whitney U test, p = 0.0)\n  statistics:\n  - about: FS ISI median\n    ci:\n      level: 0.95\n      low: 19.6\n      high: 19.67\n      unit: ms\n  - about: RS ISI median\n    ci:\n      level: 0.95\n      low: 53.3\n      high: 53.43\n      unit: ms\n  - about: FS against RS ISI distributions\n    test: Mann-Whitney U test, two-sided\n    p: 0\n    n: 2,900,284 FS and 4,586,637 RS spikes\n  expected:\n  - quantity: FS ISI median\n    value: 19.63\n    tolerance: 0.04\n    unit: ms\n  - quantity: RS ISI median\n    value: 53.37\n    tolerance: 0.07\n    unit: ms\n  - quantity: FS spikes\n    value: 2900284\n    tolerance: 290028\n  - quantity: RS spikes\n    value: 4586637\n    tolerance: 458664\n  depends_on:\n  - fig2-fs-rs-counts\n  criterion: Units with EAP amplitude above 50 uV and at least 100 spikes (Methods). The\n    tolerances of the medians are the paper's confidence intervals, which reflect spike\n    sampling only; a median within 10% is reported as a variant. Open, the drifting-grating\n    period and the ISI pool; readings, (a) ISIs within each drifting-grating presentation,\n    pooled over all units of a cluster, (b) ISIs over the whole drifting-grating blocks,\n    pooled. The CI method is not stated; a bootstrap of the median over ISIs (as Fig 6a uses\n    for its intervals) is used. Reproduced when both medians fall in tolerance under a\n    reading and the Mann-Whitney test gives p < 0.001; partially when only the 10% variant\n    holds with the same direction and test.\n- id: fig3a-rs1-excitability\n  statement: RS1 units fire faster and with less variable spiking (lower CV and LV) than RS2\n    and RS3 units during drifting gratings.\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 1;\n    Figure 3a\n  quote: Specifically, RS1 units exhibit faster, more stereotyped, and less variable spiking\n    than RS2-3 units.\n  statistics:\n  - test: Kruskal-Wallis H-test, Holm-Bonferroni corrected\n    p: 0.05\n    p_relation: <\n    corrected: Holm-Bonferroni\n    n: 419 RS1, 173 RS2, 153 RS3\n  expected:\n  - quantity: RS1 units\n    value: 419\n    tolerance: 41.9\n  - quantity: RS2 units\n    value: 173\n    tolerance: 17.3\n  - quantity: RS3 units\n    value: 153\n    tolerance: 15.3\n  depends_on:\n  - fig2d-three-subclusters-each\n  criterion: Units with EAP amplitude above 50 uV and at least 100 spikes during drifting\n    gratings; rate N / T, CV and LV as Methods eqs. 7 and 8, over the drifting-grating spikes\n    (the period is open as in fig3a-isi-fs-rs). The paper's three-group procedure\n    (ecp_func.three_sample_test). Reproduced when for each of rate, CV and LV the omnibus test\n    and both Holm-corrected RS1 against RS2 and RS1 against RS3 tests give p < 0.05, with RS1\n    rate higher and RS1 CV and LV lower; partially when this holds for one or two of the three\n    measures. Rate, CV and LV are also tested on the Source Data labels (with_labels).\n- id: fig3a-rs23-visual-responses\n  statement: RS2 and RS3 have higher f1/f0, modulation index and lifetime sparseness to\n    drifting gratings than RS1.\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 1;\n    Figure 3a\n  quote: Statistically significant differences emerge between RS1 vs. RS2-3 in terms of the\n    response metrics with RS2-3 exhibiting higher response sensitivity and selectivity over RS1\n  statistics:\n  - test: Kruskal-Wallis H-test, Holm-Bonferroni corrected\n    p: 0.05\n    p_relation: <\n    corrected: Holm-Bonferroni\n    n: 430 RS1, 182 RS2, 156 RS3\n  depends_on:\n  - fig2d-three-subclusters-each\n  criterion: The three drifting-grating metrics as the AllenSDK defines them (Methods, Visual\n    stimulus metrics, which point to the AllenSDK documentation; the Source Data columns are\n    f1_f0_dg, mod_idx_dg and lifetime_sparseness_dg). The paper's three-group procedure.\n    Reproduced when for each metric the omnibus test and the Holm-corrected RS1 against RS2\n    and RS1 against RS3 tests give p < 0.05 with RS1 lowest; partially for one or two metrics.\n- id: fig3a-fs-visual-absent\n  statement: FS1 to FS3 do not differ significantly in their visual responses to drifting\n    gratings.\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 1\n  quote: No significant difference in terms of visual responses was observed between FS1-3.\n  depends_on:\n  - fig2d-three-subclusters-each\n  criterion: A claim of absence, judged on the paper's test. For f1/f0, modulation index and\n    lifetime sparseness, the paper's three-group procedure across FS1 to FS3 (units as in\n    fig3a-rs23-visual-responses). Reproduced when no omnibus test gives p < 0.05; not\n    reproduced when any does. Medians are reported either way.\n- id: fig3c-fs-more-phase-locked\n  statement: During drifting gratings a larger share of FS than RS units is phase-locked to\n    the LFP in every band (theta 96.6% against 86.7%, alpha 86.7% against 63.9%, beta 88.2%\n    against 67.7%, low gamma 83.3% against 58.1%, high gamma 91.1% against 68.5%).\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 2;\n    Figure 3c, left; Source Data sheet Fig3c\n  quote: with FS containing a significantly higher percentage of phase-locked units than RS\n    across frequency bands (Fig. 3c , left)\n  statistics:\n  - test: two sample z test for proportions, Holm-Bonferroni corrected over bands\n    p: 0.05\n    p_relation: <\n    corrected: Holm-Bonferroni\n    n: 203 FS and 745 RS units\n  expected:\n  - quantity: FS phase-locked, theta\n    value: 96.6\n    tolerance: 9.66\n    unit: percent\n  - quantity: RS phase-locked, theta\n    value: 86.7\n    tolerance: 8.67\n    unit: percent\n  - quantity: FS phase-locked, alpha\n    value: 86.7\n    tolerance: 8.67\n    unit: percent\n  - quantity: RS phase-locked, alpha\n    value: 63.9\n    tolerance: 6.39\n    unit: percent\n  - quantity: FS phase-locked, beta\n    value: 88.2\n    tolerance: 8.82\n    unit: percent\n  - quantity: RS phase-locked, beta\n    value: 67.7\n    tolerance: 6.77\n    unit: percent\n  - quantity: FS phase-locked, low gamma\n    value: 83.3\n    tolerance: 8.33\n    unit: percent\n  - quantity: RS phase-locked, low gamma\n    value: 58.1\n    tolerance: 5.81\n    unit: percent\n  - quantity: FS phase-locked, high gamma\n    value: 91.1\n    tolerance: 9.11\n    unit: percent\n  - quantity: RS phase-locked, high gamma\n    value: 68.5\n    tolerance: 6.85\n    unit: percent\n  depends_on:\n  - fig2-fs-rs-counts\n  criterion: The percentages are counts of Source Data sheet Fig3c (196, 176, 179, 169 and\n    185 of 203 FS; 646, 476, 504, 433 and 510 of 745 RS). Methods, Phase-locking analysis,\n    units with EAP amplitude above 50 uV and at least 100 spikes, at most 10,000 spikes,\n    Hilbert phase of the band-passed LFP, phase-locked when the Rayleigh test gives p < 0.001.\n    Open, (1) the LFP channel, read as (a) the LFP channel nearest the unit's peak channel\n    other than that channel, (b) the channels two rows above and below averaged; (2) the band\n    filter, read as the 5th-order Butterworth zero-phase band-pass of ecp_func; (3) the\n    10,000-spike cap, read as (a) the first 10,000, (b) a random 10,000; (4) alpha and beta\n    edges, 8-12.5 and 12.5-30 Hz (Results) or 8-12 and 12-30 Hz (Methods). Reproduced when,\n    under a combination of readings, FS exceeds RS in all five bands with Holm-corrected\n    z-test p < 0.05 and the percentages fall within tolerance; partially when FS exceeds RS\n    significantly in three or four bands.\n  inferred: The percentages are computed from the counts of Source Data sheet Fig3c; the text\n    states only the direction.\n- id: fig3c-rs-prefers-theta\n  statement: RS phase-locking is most common for theta and less common at higher frequencies\n    (beta, low and high gamma), while the share of phase-locked FS units stays high across\n    bands.\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 2;\n    Figure 3c, left\n  quote: In general, the percentage of significantly entrained FS units was high and remained\n    broadly unaffected by the specific LFP bands. In contrast, RS couples preferentially to slow\n    LFP oscillations (theta), with the percentage decreasing for higher frequencies (beta,\n    gamma, and high gamma).\n  depends_on:\n  - fig3c-fs-more-phase-locked\n  criterion: Percentages of fig3c-fs-more-phase-locked. Reproduced when the RS theta\n    percentage is the highest of the five bands and exceeds each of beta, low gamma and high\n    gamma, and the range of FS percentages over the five bands is smaller than the range of\n    RS percentages (in the Source Data, 13.3 against 28.6 points).\n- id: figs7-spontaneous-less-locked\n  statement: Far fewer FS and RS units are phase-locked during spontaneous activity than\n    during drifting gratings, in every band.\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 2;\n    Figure S7; Source Data sheet FigS7\n  quote: Notably, FS and RS coupling to in vivo oscillations is input- and behavior-dependent,\n    with a much lower percentage of phase-locked neurons detected during spontaneous activity\n    (Fig. S7 ) than during drifting gratings (Fig. 3c , left) across frequency bands\n  expected:\n  - quantity: FS phase-locked during spontaneous activity, theta\n    value: 19.5\n    tolerance: 1.95\n    unit: percent\n  - quantity: RS phase-locked during spontaneous activity, theta\n    value: 4.7\n    tolerance: 0.47\n    unit: percent\n  depends_on:\n  - fig3c-fs-more-phase-locked\n  criterion: The same phase-locking method on spikes and LFP of the spontaneous (gray screen)\n    period, for units active in both periods (Fig S7 legend; 203 FS and 750 RS in the legend,\n    210 and 766 in Source Data sheet FigS7, whose theta counts are 41 of 210 FS and 36 of 766\n    RS). Reproduced when, for FS and for RS, the spontaneous percentage is below the\n    drifting-grating percentage in all five bands and the theta percentages fall within\n    tolerance; partially when only the direction holds.\n  inferred: The theta percentages are computed from Source Data sheet FigS7; no sentence\n    gives them.\n- id: fig3c-fs-stronger-earlier\n  statement: FS units phase-lock more strongly (higher kappa) than RS units across bands and\n    spike earlier in the cycle than RS units in beta and low gamma.\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 2;\n    Figure 3c, right\n  quote: The pairwise comparison revealed that FS has stronger phase-locking across frequency\n    bands and spikes earlier in the cycle than RS for beta and low gamma\n  statistics:\n  - test: Mann-Whitney U test, two-sided, Holm-Bonferroni corrected\n    p: 0.05\n    p_relation: <\n    corrected: Holm-Bonferroni\n    n: 203 FS and 745 RS units\n  depends_on:\n  - fig3c-fs-more-phase-locked\n  criterion: Kappa and preferred phase from pycircstat for each phase-locked unit and band\n    (Methods). What kappa is, is open; readings, (a) pycircstat.kappa of the spike phases (the\n    von Mises concentration estimate), (b) the mean resultant length (pycircstat.resultant_\n    vector_length), which ranges from 0 to 1 as the Methods say kappa does. The text cites\n    \"Fig. 2f, g\" for this, which do not exist; Fig 3c is meant. Reproduced when under a\n    reading kappa is higher for FS in all five bands and the FS preferred phase is earlier in\n    beta and low gamma, with Holm-corrected two-sided Mann-Whitney p < 0.05; partially when\n    kappa holds in three or four bands or only one of the two phase results holds.\n- id: fig3d-rs2-gamma-locking\n  statement: Among RS clusters, RS2 phase-locks more strongly to low and high gamma than RS1,\n    while the preferred phase of RS1 to RS3 stays at about 180 to 200 degrees.\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 3;\n    Figure 3d\n  quote: We found significant differences in LFP coupling for RS1-3 in the low and high gamma\n    bands, with RS2 exhibiting stronger phase locking to low and high gamma than RS1 (Fig. 3d ).\n    The preferred phase of RS1-3 remains similar at 180-200 degrees\n  statistics:\n  - test: Kruskal-Wallis H-test, Holm-Bonferroni corrected\n    p: 0.05\n    p_relation: <\n    corrected: Holm-Bonferroni\n    n: 419 RS1, 173 RS2, 153 RS3\n  expected:\n  - quantity: preferred phase range of RS1 to RS3, all bands\n    value: 190\n    tolerance: 28\n    unit: degrees\n  depends_on:\n  - fig3c-fs-stronger-earlier\n  - fig2d-three-subclusters-each\n  criterion: Kappa and phase as fig3c-fs-stronger-earlier, per RS cluster. Reproduced when in\n    low and high gamma the omnibus test gives p < 0.05 and the Holm-corrected RS2 against RS1\n    test gives p < 0.05 with RS2 higher, and the cluster mean phases lie within the reported\n    range of 180 to 200 degrees widened by 10% of each bound (162 to 220); partially when\n    only one gamma band holds.\n- id: fig3e-fs-cluster-locking\n  statement: FS3 phase-locks more strongly to high gamma than FS2, and FS1 to FS3 have\n    distinct preferred phases in alpha, beta and low gamma.\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 3;\n    Figure 3e\n  quote: Specifically, FS3 exhibit stronger phase locking to high gamma than FS2, with\n    distinct preferred phases among the three clusters in alpha, beta, and low gamma\n  statistics:\n  - test: Kruskal-Wallis H-test, Holm-Bonferroni corrected\n    p: 0.05\n    p_relation: <\n    corrected: Holm-Bonferroni\n    n: 100 FS1, 54 FS2, 49 FS3\n  expected:\n  - quantity: FS1 units\n    value: 100\n    tolerance: 10\n  - quantity: FS2 units\n    value: 54\n    tolerance: 5.4\n  - quantity: FS3 units\n    value: 49\n    tolerance: 4.9\n  depends_on:\n  - fig3c-fs-stronger-earlier\n  - fig2d-three-subclusters-each\n  criterion: Kappa and phase as fig3c-fs-stronger-earlier, per FS cluster. Reproduced when\n    the Holm-corrected FS3 against FS2 kappa test in high gamma gives p < 0.05 with FS3\n    higher, and the omnibus phase test gives p < 0.05 in each of alpha, beta and low gamma;\n    partially when the kappa result or only some phase results hold.\n- id: figs6c-fs-stronger-across-depth\n  statement: FS units phase-lock more strongly than RS units in the supragranular, granular\n    and infragranular regions in all LFP bands.\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 4;\n    Figure S6c\n  quote: Looking at one-channel clusters, FS shows consistently stronger phase-coupling than RS\n    across the cortical depth for all LFP bands (Fig. S6c ).\n  statistics:\n  - test: Mann-Whitney U test, two-sided\n    p: 0.05\n    p_relation: <\n    n: supragranular 37 FS and 107 RS, granular 54 FS and 185 RS, infragranular 112 FS and\n      453 RS\n  depends_on:\n  - fig3c-fs-stronger-earlier\n  criterion: Regions by distance from pia, supragranular (broadly layers 2-3), granular\n    (layer 4), infragranular (layers 5-6); the boundaries are not given. Readings, (a) the CCF\n    layer of the unit's peak channel in the session's channel table, (b) depth relative to\n    the CSD layer 4 centre, with layer 4 as the depths within 100 um of the centre. The\n    reading whose region counts come closer to the legend's is preferred. Kappa as\n    fig3c-fs-stronger-earlier. Reproduced when FS mean kappa exceeds RS in all 15 region and\n    band cells with p < 0.05 in at least 12; partially when FS exceeds RS in at least 12.\n- id: figs6d-rs3-supragranular-beta\n  statement: In the supragranular region the beta-band coupling strength (kappa) of RS3 is\n    almost double that of RS1.\n  source: Results, Distinct functional properties of the in vivo clusters, paragraph 4;\n    Figure S6d; Discussion, paragraph 2\n  quote: we found the most significant differences in the coupling strength of RS1-3 in\n    supragranular beta and low gamma, with kappa almost doubling between supragranular RS3 and\n    RS1 in beta\n  statistics:\n  - test: Mann-Whitney U test, two-sided\n    p: 0.05\n    p_relation: <\n  expected:\n  - quantity: ratio of RS3 to RS1 mean kappa, supragranular beta\n    value: 2\n    tolerance: 0.2\n  depends_on:\n  - figs6c-fs-stronger-across-depth\n  criterion: Regions and kappa as figs6c-fs-stronger-across-depth. Reproduced when the RS3 to\n    RS1 ratio of mean kappa in supragranular beta is within tolerance (\"almost doubling\" read\n    as 2, 10%) and the two-sided Mann-Whitney test gives p < 0.05; partially when RS3 exceeds\n    RS1 significantly but the ratio is outside tolerance.\n- id: fig4g-experiment-classifier-fs-rs\n  statement: A linear SVM trained on TPW and REP of in vivo units discriminates FS from RS with\n    a validation accuracy above 99%.\n  source: Results, Multimodal mapping between electrophysiology-, morphology-, and\n    Cre-reporter-based classes, paragraph 3; Figure 4g\n  quote: In the experiment-based classifier, we trained on one-channel EAP features (TPW, REP)\n    of in vivo units to discriminate between FS and RS clusters (training/validation set,\n    75%/25%), and classification accuracy on the validation data set exceeded 99%\n  expected:\n    quantity: validation accuracy, FS against RS\n    value: 99\n    unit: percent\n  depends_on:\n  - fig2-fs-rs-counts\n  criterion: As Exp_Model_Classifier.ipynb, which printed 99.62% (FS upsampled to balance,\n    z-scored TPW and REP, 100 resamplings each of 100 stratified 75/25 splits, linear SVC C =\n    1). Reproduced when the mean validation accuracy exceeds 99%; partially when it exceeds\n    95%.\n- id: fig5d-experiment-classifier-rs\n  statement: A classifier trained on the multi-channel in vivo features discriminates RS1 to\n    RS3 with accuracy above 99%.\n  source: Results, Composition and properties of multi-channel RS clusters, paragraph 2;\n    Figure 5d\n  quote: We also pursued the opposite direction by building the experiment-based classifier\n    trained on multi-channel in vivo EAP features to discriminate among RS1-3 and saw very high\n    classification accuracy (>99%; Fig. 5d ).\n  expected:\n    quantity: validation accuracy, RS1 to RS3\n    value: 99\n    unit: percent\n  depends_on:\n  - fig2d-three-subclusters-each\n  criterion: Random forest for more than two classes (Methods; ecp_func.classifier, 20 trees,\n    gini), on z-scored 1/V below and 1/V above of RS units, classes upsampled to the largest\n    (ecp_func.upsampling_data), 100 stratified 75/25 splits. The notebook for this panel is\n    not in the repository; the 100 resamplings of the FS/RS notebook are followed. Reproduced\n    when mean validation accuracy exceeds 99%; partially when it exceeds 95%.\n- id: fig6a-fs1-symmetric\n  statement: The spike propagation symmetry index separates FS1 (symmetric propagation) from\n    FS2 and FS3 (asymmetric propagation).\n  source: Results, Multi-channel features separate inhibitory Pvalb and Sst, paragraph 1;\n    Figure 6a\n  quote: The spike propagation symmetry index separates FS1 from FS2-3 ... Kruskal-Wallis H\n    -test, F = 111.41, p -values corrected using the Holm-Bonferroni method for multiple\n    tests, *** p < 0.001\n  statistics:\n  - test: Kruskal-Wallis H-test, Holm-Bonferroni corrected\n    statistic: F = 111.41\n    p: 0.001\n    p_relation: <\n    corrected: Holm-Bonferroni\n    n: 130 FS1, 82 FS2, 69 FS3\n  depends_on:\n  - fig2d-three-subclusters-each\n  criterion: Symmetry index as Methods eq. 1 (the Source Data values are z-scored, which does\n    not change the ranks). Reproduced when the omnibus test and the Holm-corrected FS1 against\n    FS2 and FS1 against FS3 tests give p < 0.001 with FS1 lowest; partially at p < 0.05.\n- id: fig7-opto-unit-counts\n  statement: Opto-tagging found 25 well-isolated Pvalb units in 8 Pvalb-Cre mice and 18 Sst\n    units in 12 Sst-Cre mice.\n  source: Results, Comparisons with ground-truth channelrhodopsin-tagged Pvalb and Sst units in\n    vivo, paragraph 1; Figure 7c,d\n  quote: Extracellular recordings with Neuropixels in these animals detected 25 well-isolated\n    Pvalb units in 8 Pvalb-Cre mice and 18 Sst units in 12 Sst-Cre mice\n  expected:\n  - quantity: opto-tagged Pvalb units\n    value: 25\n    tolerance: 2.5\n  - quantity: opto-tagged Sst units\n    value: 18\n    tolerance: 1.8\n  criterion: Methods, Detection of opto-tagged neurons, 1 ms PSTH bins over the 10 ms square\n    pulses, spikes counted 2 to 8 ms after onset, tagged when the trial-averaged rate there\n    exceeds 25 Hz and 2.5 times the rate in the window just before onset; V1 units of the\n    Pvalb-IRES-Cre and Sst-IRES-Cre x Ai32 sessions. Open, (1) the baseline window, read as\n    (a) the 6 ms from -6 to 0 ms, (b) the 10 ms before onset; (2) isolation, the two readings\n    of fig1d-unit-count. Figure 7 legends and the Source Data give 24 Pvalb units; 24 is\n    taken as a second reading of the Pvalb count. Reproduced when under a reading both counts\n    fall within tolerance of either reported Pvalb count; the numbers of mice are reported.\n    When the dataset holds only some of these mice, the claim is judged on the counts per\n    mouse, as a deviation.\n- id: fig7d-pvalb-fs-sst-diffuse\n  statement: In one-channel feature space opto-tagged Pvalb units overlap the wild-type FS\n    cluster, while Sst units are more diffuse and span FS and RS.\n  source: Results, Comparisons with ground-truth channelrhodopsin-tagged Pvalb and Sst units in\n    vivo, paragraph 2; Figure 7d\n  quote: For one-channel EAP features (TPW, REP), the opto-tagged Pvalb units exhibit clear\n    overlap with FS from experiments with wild-type animals. Sst units are much more diffuse,\n    spanning across the FS/RS-space\n  depends_on:\n  - fig7-opto-unit-counts\n  - fig4g-experiment-classifier-fs-rs\n  criterion: Opto-tagged units placed in FS or RS by the experiment-based classifier of\n    fig4g-experiment-classifier-fs-rs (the paper's way of assigning new units to FS/RS).\n    Reproduced when more than half of the Pvalb units are FS, Sst units fall in both FS and\n    RS, and the share of Sst units in RS exceeds that of Pvalb units.\n- id: fig7e-pvalb-sst-one-channel\n  statement: Opto-tagged Pvalb and Sst units differ in TPW, REP and spike rate, Pvalb units\n    having narrower waveforms, shorter REP and higher rates.\n  source: Results, Comparisons with ground-truth channelrhodopsin-tagged Pvalb and Sst units in\n    vivo, paragraph 2; Figure 7e; Source Data sheet Fig7deg\n  quote: Direct comparison of one-channel features (TPW, REP) and in vivo activity metrics like\n    spike frequency show that Pvalb is well-separated from Sst (Fig. 7e , top).\n  statistics:\n  - test: Mann-Whitney U test, two-sided\n    p: 0.01\n    p_relation: <\n    n: 24 Pvalb and 18 Sst units\n  depends_on:\n  - fig7-opto-unit-counts\n  criterion: The legend marks the one-channel comparisons with ** or ***, so p < 0.01 is\n    recorded; which star goes with which panel could not be read. Reproduced when each of\n    TPW, REP and rate gives a two-sided Mann-Whitney p < 0.01 with Pvalb lower in TPW and REP\n    and higher in rate; partially when two of three do.\n  inferred: The direction of each difference is read from the medians of Source Data sheet\n    Fig7deg (TPW 0.23 against 0.35 ms, REP 0.22 against 0.28 ms, rate 11.5 against 5.3 Hz);\n    the text says only that they are well separated.\n- id: fig7g-pvalb-more-symmetric\n  statement: Opto-tagged Pvalb units have more symmetric EAP propagation (a lower symmetry\n    index) than Sst units, as the models predict.\n  source: Results, Comparisons with ground-truth channelrhodopsin-tagged Pvalb and Sst units in\n    vivo, paragraph 2; Figure 7g\n  quote: A pairwise comparison of the symmetry index for the Pvalb and Sst optotagged units\n    confirms that Pvalb shows more symmetric EAP propagation compared to Sst (Fig. 7g )\n  statistics:\n  - test: two-sample t-test, two-sided\n    p: 0.012\n    n: 24 Pvalb and 18 Sst units\n  depends_on:\n  - fig7-opto-unit-counts\n  criterion: Symmetry index as Methods eq. 1 from each unit's 1/V below and 1/V above.\n    Reproduced when Pvalb mean is lower and the paper's two-sample procedure gives p < 0.05.\n- id: fig7h-pvalb-higher-cv\n  statement: During drifting gratings opto-tagged Pvalb units have higher spike time\n    variability (CV) than Sst units.\n  source: Results, Comparisons with ground-truth channelrhodopsin-tagged Pvalb and Sst units in\n    vivo, paragraph 3; Figure 7h, left\n  quote: First, we found that Pvalb exhibits higher spike time variability than Sst (Fig. 7h ,\n    left).\n  statistics:\n  - test: Mann-Whitney U test, two-sided\n    p: 0.0076\n    n: 24 Pvalb and 18 Sst units\n  depends_on:\n  - fig7-opto-unit-counts\n  criterion: CV of ISIs during drifting gratings (Methods eq. 7; the period read as in\n    fig3a-isi-fs-rs). Reproduced when the Pvalb median is higher and the two-sided\n    Mann-Whitney test gives p < 0.05.\n- id: fig7h-pvalb-theta-sst-later\n  statement: Opto-tagged Pvalb units phase-lock more strongly than Sst units to theta, and Sst\n    units spike about 40 to 50 degrees later than Pvalb units in beta, low gamma and high\n    gamma.\n  source: Results, Comparisons with ground-truth channelrhodopsin-tagged Pvalb and Sst units in\n    vivo, paragraph 3; Figure 7h, right\n  quote: Specifically, we found that Pvalb exhibits stronger phase coupling than Sst for slower\n    (theta) oscillations. Furthermore, Pvalb has a significantly different spike phase,\n    especially for faster oscillations (beta, low-, and high-gamma) than Sst, with Sst units\n    spiking in a later phase by about 40-50 degrees\n  statistics:\n  - test: Mann-Whitney U test, two-sided\n    p: 0.05\n    p_relation: <\n    n: 24 Pvalb and 18 Sst units\n  expected:\n  - quantity: Sst minus Pvalb mean preferred phase, beta, low gamma and high gamma\n    value: 45.5\n    tolerance: 9.5\n    unit: degrees\n  depends_on:\n  - fig7-opto-unit-counts\n  - fig3c-fs-stronger-earlier\n  criterion: Kappa and phase as fig3c-fs-stronger-earlier, during drifting gratings. The range\n    40 to 50 degrees widened by 10% of each bound is 36 to 55. Reproduced when theta kappa is\n    higher for Pvalb with p < 0.05 and, in each of beta, low and high gamma, the phase differs\n    with p < 0.05 and the Sst minus Pvalb difference of mean phases lies in 36 to 55 degrees;\n    partially when the theta result and some of the phase results hold.\n- id: fig4d-ap-sp-models-tpw-rep\n  statement: Simulated EAPs of aspiny (AP) models have significantly lower TPW and REP than\n    those of spiny (SP) models, as in vivo FS against RS.\n  source: Results, Multimodal mapping between electrophysiology-, morphology-, and\n    Cre-reporter-based classes, paragraph 1; Figure 4d\n  quote: simulated AP cells exhibit significantly lower TPW (two-sample t test, p = 0.00025) and\n    REP (Mann-Whitney U test, p = 0.00024) than SP ones\n  statistics:\n  - about: TPW, AP against SP models\n    test: two-sample t-test, two-sided\n    p: 0.00025\n    n: 18 AP and 15 SP models\n  - about: REP, AP against SP models\n    test: Mann-Whitney U test, two-sided\n    p: 0.00024\n    n: 18 AP and 15 SP models\n  data: elsewhere\n  where: GitHub yinawei/Mouse-all-active-models-EAP (Zenodo doi:10.5281/zenodo.7679762);\n    model features in yinawei/Mouse_V1_EAP_Analysis Examples/data/model_features.csv (Zenodo\n    doi:10.5281/zenodo.7679748); Source Data sheet Fig4cd\n  criterion: Tests on the model features. Reproduced when both tests give p < 0.001 with AP\n    lower.\n- id: fig4e-in-vitro-ap-sp\n  statement: The in vitro cells behind the AP and SP models differ significantly in spike\n    width, adaptation, spike rate and f-I slope.\n  source: Results, Multimodal mapping between electrophysiology-, morphology-, and\n    Cre-reporter-based classes, paragraph 1; Figure 4e\n  quote: show statistically significant differences in intrinsic properties known to\n    differentiate between major excitatory and inhibitory classes (spike width, adaptation,\n    spike rate, and f-I slope; Fig. 4e )\n  statistics:\n  - test: Mann-Whitney U test or two-sample t-test, two-sided\n    p: 0.001\n    p_relation: <\n    n: 18 AP and 15 SP neurons\n  data: elsewhere\n  where: Allen Cell Types Database (celltypes.brain-map.org), cell ids of Table S1; Source Data\n    sheet Fig4e\n  criterion: The tests the Fig 4e legend assigns (Mann-Whitney for width, adaptation and f-I\n    slope; t-test for spike rate). Reproduced when all four give p < 0.001; partially at p <\n    0.05.\n- id: fig4f-model-classifier\n  statement: A linear SVM trained on TPW and REP of the models separates AP from SP with 82.5%\n    validation accuracy, and applied to in vivo units labels most FS units AP and most RS units\n    SP.\n  source: Results, Multimodal mapping between electrophysiology-, morphology-, and\n    Cre-reporter-based classes, paragraph 2; Figure 4f\n  quote: This process yielded 82.5% classification accuracy on the validation data set ...\n    Most FS units are labeled as AP neurons, while the majority of RS is SP\n  expected:\n    quantity: validation accuracy, AP against SP models\n    value: 82.5\n    tolerance: 8.25\n    unit: percent\n  data: with_inputs\n  depends_on:\n  - fig2-fs-rs-counts\n  criterion: As Exp_Model_Classifier.ipynb (printed 81.67%), model features from\n    model_features.csv, z-scored together with the upsampled set, applied to the z-scored in\n    vivo TPW and REP. Reproduced when accuracy is within tolerance and more than half of FS\n    are labelled AP and more than half of RS SP.\n- id: fig4g-models-map-to-fs-rs\n  statement: The experiment-based classifier labels most AP models FS and most SP models RS.\n  source: Results, Multimodal mapping between electrophysiology-, morphology-, and\n    Cre-reporter-based classes, paragraph 3; Figure 4g\n  quote: When applying the classifier on the test datasets, i.e., model-labeled AP and SP\n    neurons, most AP neurons were labeled as FS and most SP neurons as RS units\n  data: with_inputs\n  depends_on:\n  - fig4g-experiment-classifier-fs-rs\n  criterion: The classifier of fig4g-experiment-classifier-fs-rs applied to the model features\n    of model_features.csv, each model labelled by its most frequent prediction. Reproduced\n    when more than half of the 18 AP models are FS and more than half of the 15 SP models RS.\n- id: fig4h-cre-lines-map\n  statement: Models of excitatory Cre lines (Scnn1a, Rorb, Nr5a1) are mainly classified RS and\n    models of inhibitory lines (Pvalb, Sst) mainly FS.\n  source: Results, Multimodal mapping between electrophysiology-, morphology-, and\n    Cre-reporter-based classes, paragraph 3; Figure 4h\n  quote: The excitatory classes (Scnn1a, Rorb, and Nr5a1) are mainly classified as RS, whereas\n    inhibitory classes (Pvalb and Sst) are mainly classified as FS\n  data: with_inputs\n  depends_on:\n  - fig4g-models-map-to-fs-rs\n  criterion: Labels of fig4g-models-map-to-fs-rs grouped by the cre_lines column of\n    model_features.csv. Reproduced when more than half of each excitatory line is RS and more\n    than half of each inhibitory line FS; partially when this holds pooled over excitatory\n    and over inhibitory lines.\n- id: fig5a-sp-models-three-clusters\n  statement: K-means on the simulated multi-channel features of the 15 SP models gives three\n    clusters (SP1 to SP3, with 5, 7 and 3 models), as many as the RS clusters in vivo.\n  source: Results, Composition and properties of multi-channel RS clusters, paragraph 1;\n    Figure 5a,b\n  quote: Two separate clustering analyses (elbow method and the density function) determined\n    the number of SP clusters in our simulated data to be three, i.e., SP1-3.\n  expected:\n  - quantity: SP1 models\n    value: 5\n    tolerance: 0.5\n  - quantity: SP2 models\n    value: 7\n    tolerance: 0.7\n  - quantity: SP3 models\n    value: 3\n    tolerance: 0.3\n  data: elsewhere\n  where: model_features.csv in yinawei/Mouse_V1_EAP_Analysis (Zenodo doi:10.5281/zenodo.\n    7679748); Source Data sheet Fig5a\n  criterion: The clustering of fig2-one-channel-two-clusters on the SP models' 1/V below and\n    1/V above. Reproduced when both methods give K = 3 and the counts are 5, 7 and 3.\n- id: fig5c-sp-rs-two-way-mapping\n  statement: A random forest trained on the SP models' multi-channel features identifies SP1 to\n    SP3 with more than 94% accuracy and maps RS1 to SP1, RS2 to SP2 and RS3 to SP3; the\n    experiment-based classifier maps SP1 to SP3 back to RS1 to RS3.\n  source: Results, Composition and properties of multi-channel RS clusters, paragraph 2;\n    Figure 5c,d\n  quote: we applied the model-based classifier on the test experimental data sets (in vivo\n    clustered RS1-3) and found that, indeed, RS1 units are mapped to SP1, RS2 to SP2, and RS3\n    to SP3 with high fidelity (performance... >94%; Fig. 5c )\n  expected:\n    quantity: model-based classifier accuracy\n    value: 94\n    unit: percent\n  data: with_inputs\n  depends_on:\n  - fig5a-sp-models-three-clusters\n  - fig5d-experiment-classifier-rs\n  criterion: Random forest as fig5d-experiment-classifier-rs, trained on SP1 to SP3 and\n    applied to RS1 to RS3, and the reverse. Reproduced when the model-based validation\n    accuracy exceeds 94%, the most frequent SP label of each RS cluster is the matching one,\n    and each SP cluster's models are labelled the matching RS cluster by majority.\n- id: fig5e-ca-lva\n  statement: Axonal low-voltage-activated Ca conductance is higher in SP1 and SP3 models than\n    in SP2 models, with a large effect size.\n  source: Results, Composition and properties of multi-channel RS clusters, paragraph 3;\n    Figure 5e\n  quote: Pairwise comparison between SP1 and 3 model conductances indicates that the axonal\n    low-voltage activated Ca-conductance is increased for SP1 and SP3 vs. SP2 (Cohen's d effect\n    size > 0.8; Fig. 5e )\n  data: elsewhere\n  where: GitHub yinawei/Mouse-all-active-models-EAP (Zenodo doi:10.5281/zenodo.7679762);\n    Source Data sheet Fig5e\n  criterion: Cohen's d of axonal gbar_Ca_LVA. Reproduced when d > 0.8 for SP1 against SP2 and\n    SP3 against SP2, with SP2 lower.\n- id: fig5g-bifurcation-velocity-sp\n  statement: Across SP models the morphological bifurcation distance is linearly related to the\n    inverse spike propagation velocity (slope 2.7, r = 0.8).\n  source: Results, Composition and properties of multi-channel RS clusters, paragraph 3;\n    Figure 5g, right\n  quote: the morphology bifurcation distance exhibits a strong linear relationship with the\n    spike propagation speed across SP1-3 (Fig. 5g right, slope = 2.7, the correlation\n    coefficient r = 0.8, p = 1.02 x 10 -7 )\n  statistics:\n  - test: linear regression\n    statistic: r = 0.8, slope = 2.7\n    p: 1.02e-07\n    n: 15 SP models, above and below soma\n  expected:\n  - quantity: slope\n    value: 2.7\n    tolerance: 0.27\n  - quantity: correlation coefficient\n    value: 0.8\n    tolerance: 0.08\n  data: elsewhere\n  where: Allen Cell Types Database reconstructions (cell ids of Table S1); Source Data sheet\n    Fig5g\n  criterion: Bifurcation distance as Methods eq. 2 (normalised, nodes beyond 200 um excluded,\n    summed above and below soma) against 1/V above and 1/V below. Reproduced when slope and r\n    fall within tolerance with p < 0.001.\n- id: fig5j-sp1-rate-tau\n  statement: In vitro, SP1 neurons reach a higher maximum spike rate than SP2 neurons and are\n    more electrotonically compact (differing cellular time constant).\n  source: Results, Composition and properties of multi-channel RS clusters, paragraph 4;\n    Figure 5j\n  quote: Specifically, SP1 neurons achieve a higher spike rate especially compared to SP2 ...\n    Moreover, SP1 is more electrotonically compact than SP2 (Fig. 5j ).\n  data: elsewhere\n  where: Allen Cell Types Database (cell ids of Table S1); Source Data sheet Fig5j\n  criterion: Cohen's d (the legend marks d > 0.8). Reproduced when SP1 against SP2 gives d >\n    0.8 for maximum spike rate, SP1 higher, and for tau.\n- id: fig6b-pvalb-sst-models-symmetry\n  statement: The symmetry index separates Pvalb from Sst models, Pvalb models being more\n    symmetric.\n  source: Results, Multi-channel features separate inhibitory Pvalb and Sst, paragraph 1;\n    Figure 6b, right\n  quote: Notably, a clearer separation between Pvalb and Sst models was achieved based on the\n    symmetry index\n  statistics:\n  - test: two-sample t-test, two-sided\n    p: 0.000998\n    n: 9 Pvalb and 9 Sst models\n  data: elsewhere\n  where: model_features.csv in yinawei/Mouse_V1_EAP_Analysis (Zenodo doi:10.5281/zenodo.\n    7679748); Source Data sheet Fig6b\n  criterion: Symmetry index of the models. Reproduced when Pvalb mean is lower with p < 0.01.\n- id: fig6cf-kv31\n  statement: Pvalb and Sst models differ significantly in three conductances, the largest\n    effect being dendritic Kv3.1.\n  source: Results, Multi-channel features separate inhibitory Pvalb and Sst, paragraph 2;\n    Figure 6c,f\n  quote: Pairwise comparison between Pvalb and Sst models at the level of ionic conductances\n    reveals statistically significant differences in three conductances, with the effect size\n    being largest for Kv3.1\n  statistics:\n  - test: Mann-Whitney U test, two-sided\n    p: 0.05\n    p_relation: <\n    n: 9 Pvalb and 9 Sst models\n  data: elsewhere\n  where: GitHub yinawei/Mouse-all-active-models-EAP (Zenodo doi:10.5281/zenodo.7679762);\n    Source Data sheet Fig6cf\n  criterion: Mann-Whitney tests of every conductance. Reproduced when exactly three give p <\n    0.05 and dendritic Kv3.1 has the largest |d| among them.\n- id: fig6d-sst-asymmetric-morphology\n  statement: Sst morphologies are asymmetric, with bifurcation distance above the soma longer\n    than below, while Pvalb morphologies are symmetric; Pvalb and Sst differ below the soma\n    (p = 0.03) but not above (p = 0.45).\n  source: Results, Multi-channel features separate inhibitory Pvalb and Sst, paragraph 2;\n    Figure 6d\n  quote: Specifically, while Pvalb morphologies are symmetric (i.e., above vs. below bifurcation\n    distance remains similar), Sst possesses a more asymmetric morphology with the bifurcation\n    distance above being longer than below their soma\n  statistics:\n  - about: above soma, Pvalb against Sst\n    test: two-sample t-test, two-sided\n    p: 0.45\n    n: 9 Pvalb and 9 Sst\n  - about: below soma, Pvalb against Sst\n    test: two-sample t-test, two-sided\n    p: 0.03\n    n: 9 Pvalb and 9 Sst\n  data: elsewhere\n  where: Allen Cell Types Database reconstructions (cell ids of Table S1); Source Data sheet\n    Fig6d\n  criterion: Bifurcation distances as fig5g-bifurcation-velocity-sp. Reproduced when the below\n    comparison gives p < 0.05, the above one p >= 0.05, and Sst |above| exceeds |below|.\n- id: fig6e-bifurcation-velocity-inhibitory\n  statement: Across Pvalb and Sst models the bifurcation distance above and below the soma is\n    linearly related to the inverse EAP propagation velocity (slope 2.67, r = 0.8).\n  source: Results, Multi-channel features separate inhibitory Pvalb and Sst, paragraph 2;\n    Figure 6e\n  quote: We found that the bifurcation distance above and below the soma is robustly related to\n    the inverse of the EAP propagation velocity (Fig. 6e , right, slope = 2.67, the correlation\n    coefficient r = 0.8, p -value = 5.12 x 10 -9 )\n  statistics:\n  - test: linear regression\n    statistic: r = 0.8, slope = 2.67\n    p: 5.12e-09\n    n: 9 Pvalb and 9 Sst models, above and below soma\n  expected:\n  - quantity: slope\n    value: 2.67\n    tolerance: 0.267\n  - quantity: correlation coefficient\n    value: 0.8\n    tolerance: 0.08\n  data: elsewhere\n  where: Allen Cell Types Database reconstructions (cell ids of Table S1); Source Data sheet\n    Fig6d\n  criterion: As fig5g-bifurcation-velocity-sp, on the 18 inhibitory models.\n- id: fig6g-pvalb-sst-in-vitro\n  statement: In vitro, Pvalb and Sst neurons differ in maximum spike rate, rheobase and resting\n    potential among other properties.\n  source: Results, Multi-channel features separate inhibitory Pvalb and Sst, paragraph 3;\n    Figure 6g\n  quote: Maximum spike rate to dc current injections separates between Pvalb and Sst neurons.\n    Mann-Whitney U test, two-sided, p = 0.0067\n  statistics:\n  - about: maximum spike rate\n    test: Mann-Whitney U test, two-sided\n    p: 0.0067\n    n: 9 Pvalb and 9 Sst neurons\n  data: elsewhere\n  where: Allen Cell Types Database (cell ids of Table S1); Source Data sheet Fig6g\n  criterion: Reproduced when maximum spike rate gives p < 0.01 and rheobase and resting\n    potential each p < 0.05.\n- id: figs8-rotation-symmetry\n  statement: The angle between the probe and the morphology changes multi-channel EAP metrics,\n    including the symmetry index, of Pvalb and Sst models, with some angles enlarging and some\n    hiding the Pvalb against Sst difference.\n  source: Results, Multi-channel features separate inhibitory Pvalb and Sst, paragraph 4;\n    Figure S8\n  quote: we varied the angle between the extracellular probe and morphology across Pvalb and Sst\n    models and found that, indeed, certain EAP multi-channel metrics, including the symmetry\n    index, are affected by this parameter\n  data: elsewhere\n  where: GitHub yinawei/Mouse-all-active-models-EAP (Zenodo doi:10.5281/zenodo.7679762)\n  criterion: Simulation of rotated morphologies; the angles are shown only in Fig S8a, which\n    was not read. Reproduced when the Pvalb against Sst symmetry-index test is significant at\n    some angles and not at others.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  uv run --no-sync python tools/claims_check.py claims/wei-2023.yaml paper/10.1038-s41467-023-37844-8.txt 2>&1 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  (uv run python tools/claims_check.py claims/wei-2023.yaml paper/10.1038-s41467-023-37844-8.txt || python tools/claims_check.py claims/wei-2023.yaml paper/10.1038-s41467-023-37844-8.txt) 2>&1 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent**

Three claims had both a quote and an inferred note, which the schema forbids, and six quotes were not found (degree signs, the × sign, "H-test"). Fixing those.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import re
p='claims/wei-2023.yaml'; s=open(p).read()
rep=[
("""    Hz). Thus, narrow waveform units spike significantly faster than their wide waveform
    counterparts (Mann-Whitney U test, p = 3.5 x 10 -18
""","""    Hz). Thus, narrow waveform units spike significantly faster than their wide waveform
    counterparts
"""),
("quote: Comparison of spread among RS1-3, Kruskal-Wallis Htest, F=48.2, p = 3.34*10-11","quote: Comparison of spread among RS1-3, Kruskal-Wallis H-test, F=48.2, p = 3.34*10-11"),
("""    The preferred phase of RS1-3 remains similar at 180-200 degrees
""","""    The preferred phase of RS1-3 remains similar at 180
"""),
("""    spiking in a later phase by about 40-50 degrees
""","""    spiking in a later phase by about 40-50
"""),
("""    coefficient r = 0.8, p = 1.02 x 10 -7 )
""","""    coefficient r = 0.8
"""),
("""    coefficient r = 0.8, p -value = 5.12 x 10 -9 )
""","""    coefficient r = 0.8
"""),
("""    significantly in three or four bands.
  inferred: The percentages are computed from the counts of Source Data sheet Fig3c; the text
    states only the direction.
""","""    significantly in three or four bands. The percentages are computed from the Source Data
    counts; the text states only the direction.
"""),
("""    tolerance; partially when only the direction holds.
  inferred: The theta percentages are computed from Source Data sheet FigS7; no sentence
    gives them.
""","""    tolerance; partially when only the direction holds. The theta percentages are computed
    from the Source Data counts; no sentence gives them.
"""),
("""    and higher in rate; partially when two of three do.
  inferred: The direction of each difference is read from the medians of Source Data sheet
    Fig7deg (TPW 0.23 against 0.35 ms, REP 0.22 against 0.28 ms, rate 11.5 against 5.3 Hz);
    the text says only that they are well separated.
""","""    and higher in rate; partially when two of three do. The direction of each difference is
    read from the medians of Source Data sheet Fig7deg (TPW 0.23 against 0.35 ms, REP 0.22
    against 0.28 ms, rate 11.5 against 5.3 Hz); the text says only that they are well
    separated.
"""),
]
for a,b in rep:
    assert s.count(a)==1,a[:60]; s=s.replace(a,b)
open(p,'w').write(s)
E
uv run python tools/claims_check.py claims/wei-2023.yaml paper/10.1038-s41467-023-37844-8.txt 2>&1 | tail -8
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -E "—|rather" claims/wei-2023.yaml; uv run python -c "
import yaml;d=yaml.safe_load(open('claims/wei-2023.yaml'));c=d['claims']
from collections import Counter
print(len(c), sum('quote' in x for x in c), sum('statistics' in x for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c), Counter(x.get('data','dataset') for x in c))"; git status --short
```

```
48 47 25 48 20 Counter({'dataset': 31, 'elsewhere': 12, 'with_inputs': 4, 'with_labels': 1})
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
?? claims/wei-2023.yaml
?? scripts
```

**Agent**

I wrote `claims/wei-2023.yaml` with 48 claims, and it passes the quote checker. The one item the checker flags is a p-value the supplement prints as "3.34*10-11"; I confirmed it against the Fig. S4 legend by eye. Nothing is committed.

**Text read.** I used the version of record from PubMed Central: main text, figure legends, Methods, Supplementary Figs. S1 to S8 with their legends, and Table S1. I also read the Source Data workbook. I didn't need to open the supplement PDF. I read both linked repositories:
- **`yinawei/Mouse_V1_EAP_Analysis` @1e35126:** waveform feature extraction, K-means clustering, the FS/RS classifiers and the helper functions. It starts from waveform arrays already extracted per session.
- **`yinawei/Mouse-all-active-models-EAP` @f1a4268:** the simulation set-up for one example model.

**Claims.**

| | Count |
|---|---|
| Claims | 48 (1 link claim, 47 findings) |
| With quotes | 47 (all findings; the link claim has none) |
| With `statistics` | 25 |
| With `expected` | 20 |
| With a criterion | 48 |

- **Data needed:** 31 use the dataset alone, 1 the dataset plus the Source Data labels, 4 the dataset plus the code's model features, and 12 data held elsewhere (the models, and the Allen Cell Types in vitro data and morphologies).
- **Main findings covered:** the FS/RS split and the six sub-clusters, firing and visual-response differences, phase-locking (including by depth), the optotagged Pvalb against Sst units, the classifiers, and the model and in vitro comparisons.
- **Code settings followed where the Methods are silent:** the 25 session IDs, waveform channels and filtering, feature definitions, unit exclusions, the clustering and K selection, the classifier set-up, and the test-choice rules.

**Details left open, and the readings named:**
- **Unit isolation:** the text says "see Methods", but the Methods give no criteria. Readings: (a) the AllenSDK default quality filter, (b) every V1 unit in the NWB units table.
- **FS/RS firing rate period** (the code's `fr_5min` column): (a) the spontaneous block, (b) the first 5 minutes, (c) the whole session.
- **ISI pooling:** (a) within each drifting-grating presentation, (b) across the whole grating blocks. The confidence-interval method isn't stated, so a bootstrap is used.
- **Phase-locking:**
  - LFP channel: the nearest other channel, or an average of neighbouring channels.
  - 10,000-spike cap: the first or a random 10,000.
  - Band edges: the Results (8–12.5 and 12.5–30 Hz) against the Methods (8–12 and 12–30 Hz).
  - "Kappa": the von Mises concentration, or the mean resultant length (the text says kappa ranges from 0 to 1, which only the second does).
- **Supragranular, granular and infragranular boundaries:** (a) the atlas layer of each unit's channel, (b) within 100 µm of the layer 4 centre found from the current source density.
- **Layer 4 centre from the current source density:** standard computation, or the atlas layer 4 midpoint.
- **Opto-tagging baseline window:** (a) the 6 ms before onset, (b) the 10 ms before onset.
- **Inconsistencies in the paper:**
  - Mice: the Fig. 1d legend says 24 wild-type mice; the text and Source Data say 25.
  - Pvalb units: the text says 25; the Fig. 7 legends and Source Data say 24. Both are accepted as readings.
  - The text cites "Fig. 2f, g" where it means Fig. 3c.
- The sign convention for 1/V below is unclear, so the claim that RS3 propagates faster below the soma is reported but not judged.

**Missing from the paper:**
- The main-figure PDF isn't supplied, so the significance stars of the main figures couldn't be read; those p-values are recorded as bounds.
- Figs. 3d, 3e and S6 and the optotagging kappa and phase exist only as pickle files that aren't supplied.
- Table S2 isn't in the supplement text; Methods Table 2 names the same three metrics.
- The code has no notebooks for Fig. 3 or Figs. 5 to 7, phase-locking or optotagging, and doesn't show how waveforms, the unit quality flag or depth were taken from the NWB files.

**For the author:** the dandiset's title names only the Brain Observatory 1.1 stimulus set, and the paper doesn't say which set its 25 wild-type sessions or its optotagging mice come from. So the author has to check how many are in DANDI:000021. The link claim makes that the first check, and any claim tested on a subset of sessions counts as a deviation.

## End of run

34 turns, 8 minutes, $2.97 at API prices, result: success.
