# kim-2025 · claims · run 44960584529

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/; wc -c paper/*
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
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.06.30.662469.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.06.30.662469.txt",
 "offset": 311,
 "limit": 420
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Text is the bioRxiv preprint (posted July 4, 2025, under an earlier title), with Methods and the supplementary figures inline; equations are not in the text. Next: datasets file and the paper's code.

**Agent calls Bash**

```bash
cat papers/datasets/kim-2025.yaml 2>/dev/null; grep -n "kim-2025" -r papers/keys.yaml | head; cat tools/claims_check.py | head -40; cd $TMPDIR && git clone -q https://github.com/jhk4839/Neural_variability_robustness && cd Neural_variability_robustness && git log -1 --format='%H %cd' && find . -type f | grep -v .git/ | head -100
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1101/2025.06.30.662469
title: Intrinsic geometry of trial-to-trial variability in primary visual cortex is optimal for robust
  representation of visual similarity
datasets:
- archive: dandi
  id: 000248
  relation: reuses
226:  10.1101/2025.06.30.662469: kim-2025
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && cat README.md; ls; grep -l -i -E "ICwcfg1|openscope|illusion|000248|400 ?ms|0\.4" --include=*.py --include=*.ipynb --include=*.m -r . | grep -v matnwb
```

````
## 1. File description

This repository contains the source code for the manuscript "Intrinsic geometry of trial-to-trial variability in primary visual cortex is optimal for robust representation of visual similarity" (Kim and Shin, 2026). We have 3 types of files:

- Jupyter Notebook files (`.ipynb`)  
- Python scripts (`.py`)  
- MATLAB scripts (`.m`)  

## 2. How to run the code
### 2-1. Minimal information to reproduce figures
**To generate the figures, you only need the Jupyter Notebooks, and pickle.gz files which can be downloaded from https://figshare.com/s/64957e60fe943cb732a7. Those pickle.gz files contain all the variables needed to run the Jupyter Notebooks, so save them in the same directory as the Jupyter Notebooks and run each Jupyter Notebook.**

First, install the packages listed in `requirements.txt` in a Python 3.11.10 Conda environment.
```cmd
python -m pip install pip==24.2
python -m pip install -r "your_path\requirements.txt"
```
Second, run each Jupyter Notebook file using Visual Studio Code in the envrionment. You should first run the helper codes at the top of the Notebook. Then, you can independently run specific cells for figures you want (If there are multiple cells for a figure panel, you should run them in order). In each Notebook, figure citations are at the top and immediately before each figure-generating cell. In summary:

- **decode_noise_corr.ipynb** → Figure 3b, Supplementary Figure 6a, 10a, b, e, 12b, 15b
[... 102 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && git log --format='%h %cd %s' --date=short | head -40; git log --format='%h' | wc -l
```

```
6eb0aac 2026-05-15 2026.5.15.
29af1a4 2026-05-15 2026.5.15.
74f9137 2026-05-15 2026.5.15.
a1890a1 2026-05-15 2026.5.15.
0262a66 2026-05-15 2026.5.15.
51f7c88 2026-05-15 2026.5.15.
0ce620c 2026-05-15 2026.5.15.
8906c34 2026-05-15 2026.5.15.
c74f07d 2026-05-15 2026.5.15.
a73c2a7 2026-05-15 2026.5.15.
f4e0ef2 2026-05-15 2026.5.15.
d66b4a1 2026-05-15 2026.5.15.
88b82b8 2026-05-14 2026.5.14.
013d8fb 2026-05-14 2026.5.14.
83688ab 2026-05-14 2026.5.14.
a0ee6f7 2026-05-14 2026.5.14.
58ee794 2026-05-14 2026.5.14.
a73d264 2026-05-14 2026.5.14.
554472a 2026-05-14 2026.5.14.
6782468 2026-05-06 2026.5.6.
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && git log --format='%h %cd %s' --date=short | tail -42;
```

```
2ab4e1e 2025-11-11 2025.11.11.
721c324 2025-11-06 2025.11.6.
1982b08 2025-11-05 2025.11.5.
22b9d8b 2025-11-04 2025.11.4.
b4bb567 2025-10-31 2025.10.31.
eae8e05 2025-10-28 2025.10.28.
254844f 2025-10-26 2025.10.26.
78b40bb 2025-10-22 2025.10.22.
18ae0a0 2025-10-20 2025.10.20.
676333e 2025-10-19 2025.10.19.
2118d3e 2025-10-19 2025.10.19.
929df9f 2025-10-14 2025.10.14.
32e9a23 2025-09-10 2025.9.10.
9fcfd19 2025-07-26 2025.7.26.
5a1b5b0 2025-07-26 2025.7.26.
63e65fa 2025-07-24 2025.7.24.
f2c2bde 2025-07-17 2025.7.17.
1539aa7 2025-07-16 2025.7.16.
3db1396 2025-07-16 2025.7.16.
b97caf2 2025-07-11 Create LICENSE
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && git checkout -q ac3300b && git log -1 --format='%H' && ls && cat README.md | head -60
```

```
ac3300b007c2348ccda73c0c87fb02f557791089
README.md
RSA_decoding.py
RSA_overlap_SCC.ipynb
box_and_overlap.py
box_counting_analysis.ipynb
compute_geo_ortho.py
decode_noise_corr.ipynb
dimensionality_tangent.ipynb
extract_natural_movie_neuropixels.m
extract_natural_scenes_neuropixels.m
fit_slope_histogram.ipynb
fit_slope_openscope.ipynb
local_global_alignment.ipynb
local_global_alignment.py
ortho_variance.ipynb
poisson_multi_rs.py
requirements.txt
tangent_angle.py
visualize_manifold.ipynb
[... 35 more lines not kept]
```

**Agent**

Code at commit ac3300b (2025-07-03) matches this preprint's figure numbering. Reading the notebooks that touch the OpenScope data.

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && for nb in fit_slope_openscope visualize_manifold; do echo "=== $nb"; python -c "
import json,sys
nb=json.load(open('$nb.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f'--- [{i}] {c[\"cell_type\"]}'); print(src[:3000])
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=''.join(o.get('text',[])) or ''.join(o.get('data',{}).get('text/plain',[]))
            if t: print('>>OUT:', t[:800])
"; done
```

```
<persisted-output>
Output too large (33.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/177398ff-912a-4e19-84e8-71526625feb1/tool-results/beqmneowu.txt

Preview (first 2KB):
=== fit_slope_openscope
--- [0] code
from scipy.io import savemat, loadmat
import mat73
import hdf5storage as st
import pickle
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.sparse.linalg import eigsh
from sklearn.decomposition import PCA
from scipy.stats import wilcoxon
from scipy.optimize import curve_fit
[... 42 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/177398ff-912a-4e19-84e8-71526625feb1/tool-results/beqmneowu.txt"
}
```

```
1	=== fit_slope_openscope
2	--- [0] code
3	from scipy.io import savemat, loadmat
4	import mat73
5	import hdf5storage as st
6	import pickle
7	import os
8	
9	import numpy as np
10	import pandas as pd
11	import matplotlib.pyplot as plt
12	
13	from scipy.sparse.linalg import eigsh
14	from sklearn.decomposition import PCA
15	from scipy.stats import wilcoxon
16	from scipy.optimize import curve_fit
17	import seaborn as sns
18	from copy import deepcopy as dc
19	from statsmodels.stats.multitest import multipletests
20	
[... 767 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && python -c "
import json
nb=json.load(open('visualize_manifold.ipynb')); print(''.join(nb['cells'][8]['source']))
print('=========== fit_slope_openscope cell5')
nb=json.load(open('fit_slope_openscope.ipynb')); print(''.join(nb['cells'][5]['source'])[2000:]); print('---6'); print(''.join(nb['cells'][6]['source'])[3000:])
"
```

```
# wcfg1 Ic, Lc, Tre isomap (RRneuron) 
    
print(f'wcfg1 Ic, Lc, Tre isomap (RRneuron)\n')

num_trial_types = 12
num_trials = 400 
list_target_slopes = [0, 1, 2]

# Iterate over all sessions

for sess_ind, (rate_all, stm, neu_loc, wfdur) in enumerate(zip(list_rate_w1, list_stm_w1, list_neu_loc, list_wfdur)):
    
    if sess_ind == 6:
    
        print(f'session index: {sess_ind}')

        # rate_all transposition
        rate_all = rate_all.T.copy()

        # Extract V1 neurons
[... 271 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && python -c "
import json
for f in ['ortho_variance.ipynb','local_global_alignment.ipynb']:
    nb=json.load(open(f))
    print('=====',f)
    for i,c in enumerate(nb['cells']):
        s=''.join(c['source'])
        if c['cell_type']=='markdown': print(f'[{i}] MD:', s)
        elif 'list_rate_w1' in s and 'pickle.load' not in s:
            print(f'[{i}] CODE:'); print(s[:6000])
"
```

```
===== ortho_variance.ipynb
[0] MD: ## Figure 3A-D
[8] MD: ## Figure 3A
[9] CODE:
# wcfg1 isomap (RRneuron) (orthogonal variance figure)
    
num_trials = 400 

# Iterate over all sessions

for sess_ind, (rate_all, stm, neu_loc, wfdur) in enumerate(zip(list_rate_w1, list_stm_w1, list_neu_loc, list_wfdur)):
    
    if sess_ind == 6:
    
        print(f'session index: {sess_ind}')

        # rate_all transposition
        rate_all = rate_all.T.copy()

        # Extract V1 neurons
[... 352 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; grep -l "elsewhere" claims/*.yaml | head -3
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
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:])"; grep -n -B2 -A3 "where:" claims/andrews-2024.yaml | head -30
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
head -60 claims/hiraoka-2025.yaml; grep -n "where:" claims/*.yaml | grep -i -E "allen|000021|brain-map" | head
```

```
# Claims for Hiraoka & Jo (2025), "Hierarchical organization of bursty trains in event
# sequences", doi:10.1063/5.0296506, on dandiset 000044.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: paper/10.1063-5.0296506.txt. Its header says "version of record", but only its
# first part (abstract and a 54-item reference list) is from the version of record. The body
# that follows is the arXiv preprint (stamp arXiv:2508.18281v1, dated September 22, 2025, 50
# references), and its abstract is worded differently. Every claim and quote below comes from
# that preprint body: Sections I to V, Algorithms 1 and 2, and the legends of Figures 1 to 4.
# The paper has no supplement. No PDF was supplied, so the figure panels were read only from
# the labels the text extraction keeps (the delta values in the legends, n, tau_min, tau_max).
# The paper links no analysis code. Its fits use the maximum likelihood estimator and the
# likelihood ratio test of Clauset et al. (ref. 36), citing the Python package powerlaw
# (Alstott et al., ref. 37). No version of that package is given. No code was read.
#
# Data the paper used. Three kinds of event sequence. (1) Neuronal spikes (refs. 38 and 39,
# Grosmark & Buzsaki 2016, DANDI 000044 version 0.210812.1516). These are electrophysiological
# recordings of pyramidal cells in rat hippocampus. Each session is two four-hour rest and sleep
# periods with a 45-minute exploration of a novel maze between them. The spike train of each
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && cat box_and_overlap.py | head -120; echo ======; grep -n -E "wilcoxon\(|multipletests\(|spearmanr\(|combinations\(|strongly|connected_components" RSA_decoding.py box_and_overlap.py local_global_alignment.py compute_geo_ortho.py tangent_angle.py | head -40
```

```
# %%
import mat73
import h5py
import hdf5storage as st
# from pymatreader import read_mat
import pickle
import os

import multiprocessing as mp

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.cm import get_cmap

from scipy.stats import wilcoxon, norm, kruskal, tukey_hsd, mannwhitneyu, sem
from scipy.optimize import curve_fit
from scipy.io import loadmat
from scipy.linalg import null_space
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && python - <<'EOF'
import json,re
for f in ['RSA_overlap_SCC.ipynb','decode_noise_corr.ipynb','dimensionality_tangent.ipynb','ortho_variance.ipynb','local_global_alignment.ipynb','fit_slope_histogram.ipynb','box_counting_analysis.ipynb']:
    nb=json.load(open(f))
    for i,c in enumerate(nb['cells']):
        s=''.join(c['source'])
        for line in s.split('\n'):
            if re.search(r'wilcoxon\(|multipletests\(|ranksums|kruskal\(|mannwhitneyu\(|^## ',line) and not line.strip().startswith('#  '):
                print(f,i,line.strip()[:200])
        if c['cell_type']=='code':
            for o in c.get('outputs',[]):
                t=''.join(o.get('text',[]))
                if re.search(r'mean|slope|p ?=|pval|median',t): print('   OUT',f,i,t[:400].replace('\n',' | '))
EOF
```

```
RSA_overlap_SCC.ipynb 0 ## Figure 2A, 2C, 4
RSA_overlap_SCC.ipynb 0 ## Figure S4C, S6B, S6C
RSA_overlap_SCC.ipynb 12 ## Figure 4A
RSA_overlap_SCC.ipynb 13 list_pvals_overlap_consis = np.array([list(wilcoxon(list_overlap_consis_asis, list_overlap_consis_RRneuron2[:, slope_ind], nan_policy='omit'))[1]
RSA_overlap_SCC.ipynb 15 ## Figure 2A, 4D
RSA_overlap_SCC.ipynb 16 list_pvals_overlap_consis = np.array([list(wilcoxon(list_overlap_consis_asis, list_overlap_consis_RRneuron2[:, slope_ind], nan_policy='omit'))[1]
RSA_overlap_SCC.ipynb 16 list_pvals_overlap = np.array([list(wilcoxon(list_overlap_asis2.mean(axis=(1, 2)), list_overlap_RRneuron3[:, slope_ind].mean(axis=(1, 2)), nan_policy='omit'))[1]
RSA_overlap_SCC.ipynb 17 ## Figure 2C
RSA_overlap_SCC.ipynb 18 list_pvals_size_cc_ABO[0, slope_ind] = list(wilcoxon(list_size_cc_asis[:, 0], list_size_cc_RRneuron2[:, slope_ind, 0], nan_policy='omit'))[1]
RSA_overlap_SCC.ipynb 18 list_pvals_size_cc_ABO[1, slope_ind] = list(wilcoxon(list_size_cc_asis[:, 1], list_size_cc_RRneuron2[:, slope_ind, 1], nan_policy='omit'))[1]
RSA_overlap_SCC.ipynb 20 ## Figure 4C
RSA_overlap_SCC.ipynb 21 list_pvals_corr_withinsess_ABO = np.array([[list(wilcoxon(list_corr_withinsess_asis2[:, :, corr_ind].mean(axis=1), list_corr_withinsess3[slope_ind, :, :, corr_ind].mean(axis=1)))[1] \
RSA_overlap_SCC.ipynb 22 ## Figure S4C middle
RSA_overlap_SCC.ipynb 23 list_pvals_corr_withinsess_ABO = np.array([[list(wilcoxon(list_corr_withinsess_asis2[:, :, corr_ind].mean(axis=1), list_corr_withinsess3[slope_ind, :, :, corr_ind].mean(axis=1)))[1] \
RSA_overlap_SCC.ipynb 23 list_pvals_corr_withinsess_ABO_shuf = np.array([[list(wilcoxon(list_corr_withinsess_asis2_shuf[:, :, corr_ind].mean(axis=1), list_corr_withinsess3_shuf[slope_ind, :, :, corr_ind].mean(axis=1)))[1] \
RSA_overlap_SCC.ipynb 23 list_pvals_corr_withinsess_ABO_toshuf = np.array([[list(wilcoxon(list_corr_withinsess3[slope_ind, :, :, corr_ind].mean(axis=1), list_corr_withinsess3_shuf[slope_ind, :, :, corr
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && python - <<'EOF'
import json
nb=json.load(open('RSA_overlap_SCC.ipynb'))
for i in [13,18,21]:
    s=''.join(nb['cells'][i]['source'])
    print('=== cell',i); print(s[:2500])
EOF
grep -n "def \|percentile\|5)" box_and_overlap.py | sed -n 1,60p | grep -v "^.*#" | head -30
```

```
=== cell 13
# overlap consistency

save_file_name = 'overlap_nbr_stimpairs_consis_ABO_all3.pickle' # num_trial_types x num_trial_types, overlap (minimum distance) & gap (minimum distance), with diagonal, slope 0-2
# save_file_name = os.path.join('..', 'data', save_file_name)
with open(save_file_name, 'rb') as f:
    overlap_stimpairs_ABO_all = pickle.load(f)
    
    list_overlap_asis3 = dc(overlap_stimpairs_ABO_all['list_overlap_asis3'])
    list_overlap_RRneuron4 = dc(overlap_stimpairs_ABO_all['list_overlap_RRneuron4'])
    list_gap_asis3 = dc(overlap_stimpairs_ABO_all['list_gap_asis3'])
    list_gap_RRneuron4 = dc(overlap_stimpairs_ABO_all['list_gap_RRneuron4'])

list_target_slopes = np.linspace(0, 2, 21, endpoint=True)
num_sess = 32
num_trial_types = 119
num_sampling = 10

# num_trial_types x num_trial_types
list_overlap_consis_asis = np.full((num_sess, num_sampling), np.nan) # correlation between 2 neuronal subset
[... 153 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && grep -n -E "SVC\(|StratifiedKFold\(|KFold\(|Isomap\(|n_neighbors|PCA\(" RSA_decoding.py compute_geo_ortho.py local_global_alignment.py tangent_angle.py box_and_overlap.py | head -30; python - <<'EOF'
import json
for f in ['decode_noise_corr.ipynb','dimensionality_tangent.ipynb']:
    nb=json.load(open(f))
    for i,c in enumerate(nb['cells']):
        s=''.join(c['source'])
        for l in s.split('\n'):
            if any(k in l for k in ['SVC(','StratifiedKFold(','KFold(','def compute_dim','participation','eigvals','np.sum(eig']) : print(f,i,l.strip()[:200])
EOF
```

```
RSA_decoding.py:982:        kfold = KFold(n_splits=n_splits)
RSA_decoding.py:983:        stkfold = StratifiedKFold(n_splits=n_splits)
RSA_decoding.py:990:        kfold = KFold(n_splits=n_splits)
RSA_decoding.py:991:        stkfold = StratifiedKFold(n_splits=n_splits)
RSA_decoding.py:1007:                    clf = svm.SVC(kernel='linear')
RSA_decoding.py:1013:                    clf = KNeighborsClassifier(n_neighbors=30)  
RSA_decoding.py:1084:            kfold = KFold(n_splits=n_splits)
RSA_decoding.py:1085:            stkfold = StratifiedKFold(n_splits=n_splits)
RSA_decoding.py:1101:                        clf = svm.SVC(kernel='linear')
RSA_decoding.py:1107:                        clf = KNeighborsClassifier(n_neighbors=30) 
RSA_decoding.py:1220:                kfold = KFold(n_splits=n_splits)
RSA_decoding.py:1221:                stkfold = StratifiedKFold(n_splits=n_splits)
RSA_decoding.py:1230:                    kfold = KFold(n_splits=n_splits)
RSA_decoding.py:1231:                    stkfold = StratifiedKFold(n_splits=n_splits)
RSA_decoding.py:1245:                            clf_SVC = svm.SVC(kernel='linear')
RSA_decoding.py:1246:                            # clf_SVC = svm.SVC(kernel='poly', degree=3)
RSA_decoding.py:1247:                            # clf_SVC = svm.SVC(kernel='rbf')
RSA_decoding.py:1315:                kfold = KFold(n_splits=n_splits)
RSA_decoding.py:1316:                stkfold = StratifiedKFold(n_splits=n_splits)
RSA_decoding.py:1330:                        clf_SVC = svm.SVC(kernel='linear')
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && sed -n 180,215p compute_geo_ortho.py; grep -n -E "ortho|var\(|dist_matrix|spearmanr" compute_geo_ortho.py | head -30; sed -n 130,175p local_global_alignment.py
```

```
# Compute mean and variance of slope-changed data
        rate_mean_RRneuron_coll, rate_var_RRneuron_coll = \
            compute_mean_var_trial_collapse(stm_cnt_dict, rate_RRneuron_dr)
        # FF_RRneuron = rate_var_RRneuron_dr.div(rate_mean_RRneuron_dr)
        # print(FF_RRneuron)
        # print(rate_var_RRneuron_dr)

        # concatenate centroids of all stimuli
        rate_plus_mean = pd.concat([rate_RRneuron_dr, rate_mean_RRneuron_coll], axis=1)

        # Compute geodesic distance matrix
        n_components = 1 # target number of dimensions
        # n_components = rate_RRneuron_dr.shape[0] # target number of dimensions
        n_neighbors = 5 # number of neighbors

        isomap = Isomap(n_neighbors=n_neighbors, n_components=n_components)
        
        isomap.fit(rate_plus_mean.T)
        mean_dist_mat_RRneuron = isomap.dist_matrix_[rate_RRneuron_dr.shape[1]:, rate_RRneuron_dr.shape[1]:].copy() # inter-centroid geodesic distance matrix
                        
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neural_variability_robustness && python - <<'EOF'
import json
nb=json.load(open('ortho_variance.ipynb'))
s=''.join(nb['cells'][9]['source']); i=s.find('# against Tre2'); print(s[i:i+1500])
for o in nb['cells'][9].get('outputs',[]): print(''.join(o.get('text',[]))[:500])
EOF
```

```
# against Tre2
        slope_mean = (rate_plus_mean_isomap.loc[1, 'Tre2']-rate_plus_mean_isomap.loc[1, 'Lc1']) / (rate_plus_mean_isomap.loc[0, 'Tre2']-rate_plus_mean_isomap.loc[0, 'Lc1'])
        scaling_c = 22
        Lc1_mean = rate_plus_mean_isomap.loc[:, 'Lc1'].copy()

        start_Tre2 = (Lc1_mean[0] - scaling_c, Lc1_mean[1] - scaling_c*slope_mean)
        end_Tre2 = (Lc1_mean[0] + scaling_c, Lc1_mean[1] + scaling_c*slope_mean)
        arrow_Tre2 = patches.FancyArrowPatch(start_Tre2, end_Tre2, arrowstyle="<->",
                                            mutation_scale=15,  # Size of arrowheads
                                            color='darkviolet', linewidth=2.5, zorder=2, label='orthogonal variance')
        ax.add_patch(arrow_Tre2)

        ax.annotate(f'Orthogonal variance', xy=(0.03, 0.88), xycoords='axes fraction', fontsize=20, color='k')
        ax.annotate(f'Faraway stimulus,\nlarger variance', xy=(0.52, 0.7), xycoords='axes fraction', fontsize=14, color='green')
        ax.annotate(f'Nearby stimulus,\nsmaller variance', xy=(0.47, 0.15), xycoords='axes fraction', fontsize=14, color='darkviolet')

        # ax.set_title('as-is', fontsize=20)
        ax.tick_params('both', labelsize=18)

        ax.set_xlim([-130, 130]) # with rest points
[... 8 more lines not kept]
```

**Agent**

I have what I need from the code. Writing the claims file now: most claims are on the Allen Visual Coding data (`elsewhere`), plus a link claim and three claims that DANDI:000248 can test.

**Agent calls Write**

```json
{
 "file_path": "claims/kim-2025.yaml",
 "content": "# Claims for Kim & Shin (2025), doi:10.1101/2025.06.30.662469, read for dandiset 000248.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-21,\n# protocol as stated in docs/protocol.md (Reader).\n#\n# Text read: paper/10.1101-2025.06.30.662469.txt, the bioRxiv full text of the preprint posted\n# July 04, 2025, under the title \"Neural variability structure in primary visual cortex is optimal\n# for robust representation of visual similarity\". The registry lists the paper under a later\n# title (\"Intrinsic geometry of trial-to-trial variability in primary visual cortex is optimal for\n# robust representation of visual similarity\"); that later version was not supplied, and every\n# claim here is from the July 2025 text. That text holds the Results, Discussion, Methods and the\n# legends of Figures 1 to 4 and S1 to S6; the supplementary figures are part of it, and there is\n# no separate supplement. The equations of the Methods (slope manipulation, effective\n# dimensionality, orthogonal component, number of RSA trial pairs, modulated Poisson model) are\n# lost in the extraction, and the legends of Figures 2 and 3 are cut after \"(Wilcoxon signed-rank\n# test\". No PDF was supplied, so figure panels could not be read. Where the equations are needed\n# they are taken from the code below.\n#\n# Code read: GitHub jhk4839/Neural_variability_robustness at commit\n# ac3300b007c2348ccda73c0c87fb02f557791089 (2025-07-03), the last commit before the preprint was\n# posted; its README names the July 2025 title and maps the notebooks to this text's figure\n# numbers (fit_slope_histogram for 1B, 1C, S1 to S3, S5A; dimensionality_tangent for 1D, 2D;\n# box_counting_analysis for S5C; decode_noise_corr for 2B, S4, S6A; RSA_overlap_SCC for 2A, 2C,\n# 4, S4C, S6B, S6C; ortho_variance for 3A to 3D; local_global_alignment for 3E, 3F;\n# visualize_manifold for 1C, S5B, S5D; fit_slope_openscope fits slopes to the Illusion data and\n# makes no figure). The notebooks load pickles that are not in the repository. The head of the\n# repository (2026) belongs to the later version and uses other figure numbers; it was not used.\n#\n# Data the paper used.\n# (1) Main dataset, not in dandiset 000248. Allen Brain Observatory Visual Coding Neuropixels,\n#     \"Brain Observatory 1.1\" sessions, \"natural scenes\" block, read through AllenSDK. 32\n#     sessions, one mouse each; 2 excluded for V1 (more than 10% of natural scenes trials with no\n#     spikes in any unit), leaving 30 (the code drops session indices 0 and 6). 119 stimuli (118\n#     natural scenes and a gray image), 250 ms each, no interval, 50 repeats in random order (one\n#     session 47 to 50 repeats, subsampled to 47 for decoding and RSA). Spike counts in the 250 ms\n#     from onset. Units kept when isi_violations < 0.5, amplitude_cutoff < 0.1 and presence_ratio\n#     > 0.9. V1 has 64 +- 25 units per session (14 to 110). Higher visual areas LM, RL, AL, PM, AM\n#     (one RL session also excluded). Running speed (moving when the trial mean speed is >= 1\n#     cm/s) and pupil area (tertiles of the trial mean) for Figure S2. Natural movie one (30 s,\n#     60 repeats) from 23 of 26 \"Functional Connectivity\" sessions, in 12-frame (400 ms) bins, 75\n#     bins, for Figure S5A and S5B.\n# (2) Allen Institute OpenScope Illusion dataset, dandiset 000248, used only for the Isomap\n#     pictures of Figures 1C (bottom), 3A, 3E (left) and 3F (left). V1 spike counts in the 400\n#     ms from stimulus onset, all stimuli with 400 repeats in the \"ICwcfg1\" block of one example\n#     session. In the paper's code the data come from a post-processed MATLAB copy (folder\n#     \"OpenScopeData_00248_v240130_postprocessed\") with 11 subjects, sub_619296, sub_620333,\n#     sub_620334, sub_625545, sub_625554, sub_625555, sub_630506, sub_631510, sub_631570,\n#     sub_633229 and sub_637484; the example is index 6, sub_630506. V1 units are those whose\n#     location contains \"VISp\" and not \"VISpm\"; spike counts are the stored rate times 0.4 s; no\n#     unit quality filter is applied in the code (a waveform-duration filter is commented out).\n#     Stimulus codes are named by the code's map 0 Blank, 1 X, 2 Tc1, 3 Ic1, 4 Lc1, 5 Tc2, 6 Lc2,\n#     7 Ic2, 8 Ire1, 9 Ire2, 10 Tre1, 11 Tre2, 12 Xre1, 13 Xre2, 14 BR_in, 15 BL_in, 16 TL_in, 17\n#     TR_in, 18 BR_out, 19 BL_out, 20 TL_out, 21 TR_out. The code expects 12 stimuli with 400\n#     repeats. Figure 1C shows Ic1, Lc1 and Tre1; Figure 3A shows Ic1, Lc1 and Tre2; Figures 3E\n#     and 3F left show Lc1 and Tre2 against the rest.\n# Only the claims marked data dataset (illusion-*) can be tested on dandiset 000248. Every other\n# claim is on the Allen Visual Coding Neuropixels data (data elsewhere).\n#\n# Shared method, from the Methods unless stated.\n# - M1 slope fit. Per session and stimulus, across-trial mean and variance (ddof 1, code) of each\n#   neuron's spike count; neurons with zero count on all trials of the stimulus excluded; OLS of\n#   log10 variance on log10 mean across neurons (np.polyfit, code) gives slope s and intercept i.\n# - M2 slope manipulation (Methods, \"Manipulation of slope by residual rescaling\"; the equations\n#   are lost in the text and taken from the code). Target slopes s' from 0 to 2 in steps of 0.1.\n#   For each neuron, log10 var' = (s'/s)(log10 var - i) + (s - s') mean_n(log10 mean) + i, which\n#   keeps the mean log variance across neurons; each trial's residual (count minus the stimulus\n#   mean) is multiplied by sqrt(var'/var) and added back to the mean; neurons with zero mean stay\n#   0. Means, pairwise noise correlations and the summed log variance are unchanged.\n# - M3 overlap percentage of manifold A relative to B. The fraction of A's trials whose nearest\n#   trial of B is closer than the 5th percentile of the pairwise distances within B (Euclidean,\n#   in the N-neuron space; box_and_overlap.py uses np.percentile(..., 5)).\n# - M4 statistics on curves. Each slope-changed value is compared with the as-is value by a\n#   Wilcoxon signed-rank test across sessions (or session pairs), p < 0.05, uncorrected (the\n#   notebooks call scipy wilcoxon per slope with no correction). n is 30 sessions or 435 session\n#   pairs for V1.\n# - M5 geodesic distances between centroids. Isomap (n_neighbors 5) fitted on all trials with the\n#   stimulus centroids appended; the geodesic distance matrix among the centroids\n#   (compute_geo_ortho.py, local_global_alignment.py).\n#\n# Details the paper leaves open, used by several criteria.\n# - O1 \"peaks near (around) slope 1\". The paper fixes no window. Readings, (a) the slope with the\n#   largest across-session mean lies in 0.8 to 1.2, (b) in 0.7 to 1.3; in both, the values at\n#   slopes 0 and 2 are lower than as-is and differ from it by the M4 test. Reproduced under\n#   either reading; both are reported.\n# - O2 \"increases (decreases) with slope\". Read as the across-session mean at slope 2 above (below)\n#   the mean at slope 1, which is above (below) the mean at slope 0, with slopes 0 and 2 both\n#   differing from as-is by the M4 test. \"Monotonically\" (Figure 2B) is read strictly, a change\n#   in the stated direction at every 0.1 step.\n# - O3 Illusion units. The paper states no unit filter for dandiset 000248. Readings, (a) all\n#   units located in VISp (not VISpm), as the code, (b) the same units restricted by the Allen\n#   quality criteria the Methods give for the main dataset. The code's post-processed input may\n#   already have been filtered; that cannot be checked. Both readings are run.\n# - O4 Illusion example session. The text says \"one example session\"; the code uses sub_630506.\n#   That session is the main reading; the other sessions with an ICwcfg1 block are a variant.\nschema_version: 2\npaper: doi:10.1101/2025.06.30.662469\nclaims:\n- id: illusion-data-link\n  kind: link\n  statement: Dandiset 000248 holds the OpenScope Illusion recordings the paper used for its\n    Isomap pictures, an ICwcfg1 block in which stimuli are repeated 400 times, with V1 units, in\n    the example session the paper's code uses.\n  source: Methods, Visualization of stimulus manifold geometry, paragraph 2; Data and code\n    availability; visualize_manifold.ipynb cell 8 at commit ac3300b\n  data: with_labels\n  criterion: Reproduced when (i) sub_630506 is in the dandiset with an ICwcfg1 presentations block\n    whose 400-repeat stimuli number 12, as the code expects (num_trial_types 12), (ii) the stimuli\n    Ic1, Lc1, Tre1 and Tre2 can be identified in it, by the names the dandiset gives or through\n    the code's map of codes 0 to 21 (header), and (iii) the session has units located in VISp\n    (not VISpm). Partially reproduced when the block and units exist but the repeat count or the\n    number of 400-repeat stimuli differs. The presence of the code's other 10 subjects and their\n    ICwcfg1 blocks is reported.\n- id: illusion-fig1c-isomap-geometry\n  statement: In an example session of the Illusion data, three stimulus manifolds of V1 activity\n    appear continuous with little overlap in the as-is data, discontinuous at slope 0 and heavily\n    overlapping at slope 2.\n  source: Figure 1C bottom; Results, Neural variability structure is highly consistent across\n    visual stimuli and mice, paragraph 6\n  quote: As the slope increases from 0 to 2, the stimulus manifolds become increasingly\n    overlapping. At slope 0, the stimulus manifolds appear discontinuous with one another,\n    hindering smooth transitions between stimuli. At slope 2, the stimulus manifolds are hard to\n    discriminate due to the large overlap.\n  depends_on:\n  - illusion-data-link\n  criterion: Session sub_630506 (O4), V1 units (O3), spike counts in the 400 ms from onset, the 12\n    stimuli with 400 repeats. Slope manipulation M2 at target slopes 0, 1 and 2 with M1 fits on\n    these stimuli (fit_slope_openscope.ipynb). The Isomap pictures (n_neighbors 5, 2 components,\n    fitted on all trials of the 12 stimuli, visualize_manifold.ipynb cell 8) are drawn for Ic1,\n    Lc1 and Tre1 and shown, but the claim is judged on the measures the paper uses to formalize\n    this picture (Results, Neural variability structure enables maximal discriminability,\n    paragraph 1), computed in the full N-neuron space. Among Ic1, Lc1 and Tre1, with the M3\n    overlap percentages and a directed edge wherever one is above zero, (i) at slope 0 the three\n    do not form one strongly connected component, (ii) in the as-is data they do, (iii) the mean\n    of the six directed overlap percentages is larger at slope 2 than as-is and larger as-is than\n    at slope 0. Reproduced when all three hold, partially when two hold. The same measures over\n    all 12 stimuli (the size of the largest strongly connected component, the mean overlap) and\n    the other sessions are shown as variants.\n- id: illusion-fig3a-orthogonal-variance-example\n  statement: In the example session of the Illusion data, the Lc1 manifold has larger orthogonal\n    variance toward the faraway Ic1 manifold than toward the nearby Tre2 manifold.\n  source: Figure 3A (legend; the labels \"Faraway stimulus, larger variance\" on Ic1 and \"Nearby\n    stimulus, smaller variance\" on Tre2 are from ortho_variance.ipynb cell 9 at commit ac3300b)\n  quote: Purple and green arrows indicate the orthogonal variances of the orange manifold\n    relative to the purple and green manifolds, respectively.\n  depends_on:\n  - illusion-data-link\n  criterion: The arrows of Figure 3A are drawn in the 2D Isomap with lengths set by hand in the\n    code (60 toward Ic1, 22 toward Tre2), so the claim is tested with the paper's measures in the\n    N-neuron space. As-is data of sub_630506 (O4), V1 units (O3), the 12 stimuli with 400\n    repeats. Geodesic distance between centroids by M5. Orthogonal variance as the Methods define\n    it, the variance (ddof 1, code) across Lc1 trials of the norm of the component of each\n    trial's deviation from the Lc1 centroid along the line joining the two centroids, divided by\n    the summed per-neuron variance of Lc1. Reproduced when Ic1 is geodesically farther from Lc1\n    than Tre2 is and Lc1's orthogonal variance toward Ic1 is larger than toward Tre2; partially\n    reproduced when only the variance order holds. The Spearman correlation between geodesic\n    distance and orthogonal variance over all 132 ordered pairs of the 12 stimuli is shown as a\n    variant.\n- id: illusion-geometry-similar-across-datasets\n  statement: The changes in manifold geometry that come with changing the slope are qualitatively\n    the same in the Illusion data as in the natural scenes data.\n  source: Methods, Visualization of stimulus manifold geometry, paragraph 3\n  quote: The geometric changes accompanying log-mean vs. log-variance slope changes are\n    qualitatively similar across datasets, as well as across Isomap and UMAP.\n  depends_on:\n  - illusion-data-link\n  criterion: The paper does not say which geometric changes it compared. Read as the two changes\n    it reports for the main data, effective dimensionality falling with slope (Figure 1D) and\n    overlap rising with slope (Figure 2A). Every session of dandiset 000248 with an ICwcfg1\n    block, V1 units (O3), 400 ms counts, the stimuli with 400 repeats, M2 at slopes 0 to 2.\n    Effective dimensionality per stimulus as the Methods define it, the participation ratio of\n    the covariance eigenvalues divided by the number of neurons, averaged over stimuli; overlap\n    by M3, averaged over ordered stimulus pairs. Reproduced when, across sessions, the mean\n    dimensionality decreases and the mean overlap increases by the O2 reading (with the M4 test\n    across these sessions); partially reproduced when the direction holds for both but the tests\n    do not. The example session alone is shown as a variant.\n- id: data-v1-units\n  statement: The main analysis uses V1 units from 30 sessions of 30 mice, 64 +- 25 units per\n    session (14 to 110), 1920 units in all, with 119 stimuli per session (3570 stimulus fits).\n  source: Methods, Main dataset and visual stimuli, paragraph 4; Results, first section,\n    paragraph 1; Figure 1B legend\n  quote: The number of V1 neurons analyzed in the 30 sessions was 64 ± 25 (mean ± standard\n    deviation).\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, Brain Observatory 1.1 sessions\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels), read with AllenSDK;\n    the paper gives no release\n  expected:\n  - quantity: V1 sessions analyzed\n    value: 30\n    tolerance: 0\n  - quantity: mean V1 units per session\n    value: 64\n    tolerance: 6.4\n  - quantity: SD of V1 units per session\n    value: 25\n    tolerance: 2.5\n  - quantity: total V1 units (across-stimulus fits)\n    value: 1920\n    tolerance: 192\n  criterion: Session count is exact (tolerance 0) because the exclusion rule is stated (more than\n    10% of natural scenes trials with no spike in any V1 unit, from 32 sessions). Units by the\n    Allen quality criteria of the Methods. The range 14 to 110 is checked within the 10% rule\n    (minimum 12.6 to 15.4, maximum 99 to 121).\n- id: fig1b-across-neuron-slope-near-1\n  statement: Across simultaneously recorded V1 neurons, the log-mean against log-variance relation\n    for each stimulus is fit by a line with slope near 1 (mean 1.048, SEM 0.001; SD 0.07 over 3570\n    session-stimulus fits).\n  source: Results, Neural variability structure is highly consistent across visual stimuli and\n    mice, paragraph 1; Figure 1B\n  quote: we found a highly consistent relationship across mice and stimuli that was well-fit by a\n    linear regression with a slope near 1 (mean ± standard error of the mean, or SEM, 1.048 ±\n    0.001\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, Brain Observatory 1.1 sessions,\n    natural scenes block (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  depends_on:\n  - data-v1-units\n  expected:\n  - quantity: mean across-neuron slope\n    value: 1.048\n    tolerance: 0.001\n  - quantity: SD of across-neuron slopes\n    value: 0.07\n    tolerance: 0.007\n  - quantity: number of across-neuron fits\n    value: 3570\n    tolerance: 0\n  criterion: M1 for every V1 session and stimulus, all fits pooled. The mean's tolerance is the\n    paper's SEM. The count is exact (30 sessions times 119 stimuli).\n- id: fig1b-across-stimulus-slope\n  statement: Fit across stimuli for each neuron, the log-mean against log-variance slope is larger\n    and more spread (1.13 +- 0.21 over 1920 neurons) than the across-neuron slope (1.05 +- 0.07).\n  source: Figure 1B legend; Figure S1A, S1E; Results, first section, paragraph 2\n  quote: Mean ± standard deviation was 1.13 ± 0.21 for across-stimulus fits (n = 1920, i.e.,\n    cumulative number of neurons across sessions), and 1.05 ± 0.07 for across-neuron fits\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n    n: 1920 across-stimulus fits and 3570 across-neuron fits\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  depends_on:\n  - data-v1-units\n  expected:\n  - quantity: mean across-stimulus slope\n    value: 1.13\n    tolerance: 0.21\n  - quantity: SD of across-stimulus slopes\n    value: 0.21\n    tolerance: 0.021\n  criterion: Across-stimulus fit per neuron as in M1 with stimuli as points (Methods,\n    Log-mean vs. log-variance relationship across stimuli). The mean's tolerance is the paper's\n    stated SD, as no SEM is given. Reproduced when both values are within tolerance and a\n    two-sided Wilcoxon rank-sum test (Mann-Whitney U, as fit_slope_histogram.ipynb cell 25)\n    between the two sets of slopes gives p < 0.001.\n- id: figs1-gain-variance\n  statement: The gain variance of the modulated Poisson model is larger and more spread across\n    stimuli (0.78 +- 0.92, n 1519) than across neurons (0.26 +- 0.15, n 3535), after excluding\n    401 of 1920 neurons and 35 of 3570 stimuli that are not supralinear.\n  source: Figure S1B, S1F\n  quote: Mean ± standard deviation was 0.78 ± 0.92 for across-stimulus fits (n = 1519), and 0.26 ±\n    0.15 for across-neuron fits (n = 3535)\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n    n: 1519 across-stimulus and 3535 across-neuron fits\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  depends_on:\n  - data-v1-units\n  expected:\n  - quantity: mean across-stimulus gain variance\n    value: 0.78\n    tolerance: 0.078\n  - quantity: mean across-neuron gain variance\n    value: 0.26\n    tolerance: 0.026\n  - quantity: neurons excluded from across-stimulus fits\n    value: 401\n    tolerance: 40\n  - quantity: stimuli excluded from across-neuron fits\n    value: 35\n    tolerance: 3.5\n  criterion: Negative binomial fit by maximum likelihood with Nelder-Mead for each neuron and\n    stimulus, gain variance from k as in the Methods (the formulas are lost in the text and are\n    taken from fit_slope_histogram.ipynb), fits kept only for neurons (stimuli) with more than\n    50% supralinear stimuli (neurons), median across stimuli (neurons). Reproduced when the means\n    are within tolerance and the two-sided rank-sum test gives p < 0.001.\n- id: figs2-behavioral-state\n  statement: The across-neuron slope is slightly but significantly modulated by behavioral state,\n    smallest when the mouse runs and when its pupils are dilated, while staying near 1.\n  source: Results, first section, paragraph 2; Figure S2A, S2C\n  quote: The slope was smallest when the mouse was running (Figure S2A) and had dilated pupils\n    (Figure S2C).\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block with running\n    speed and pupil tracking (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  depends_on:\n  - data-v1-units\n  criterion: Trials split into moving (trial mean speed >= 1 cm/s) and stationary, and into pupil\n    area tertiles (0-33, 33-67, 67-100 percentiles of trial mean area); M1 fit per session,\n    stimulus and state, all pooled. The legend names a Wilcoxon rank-sum test for locomotion and\n    a Kruskal-Wallis test for pupil, without printing p in the text; the code runs a two-sided\n    Mann-Whitney U test and scipy kruskal. Reproduced when moving slopes are lower than\n    stationary slopes at p < 0.05, the largest pupil tertile has the lowest median slope with\n    Kruskal-Wallis p < 0.05, and every state's median slope lies in 0.9 to 1.1 (\"near 1\" read as\n    within 10% of 1, the protocol default, as the paper gives no bound).\n- id: figs3-higher-visual-areas\n  statement: The across-neuron slope is concentrated around 1 in the five higher visual areas as\n    in V1.\n  source: Results, first section, paragraph 2; Figure S3\n  quote: Higher visual areas showed a similar mean-variance relationship as V1 (Figure S3;\n    lateromedial area LM, rostrolateral area RL, anterolateral area AL, posteromedial area PM, and\n    anteromedial area AM).\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  expected:\n  - quantity: sessions with LM neurons\n    value: 24\n    tolerance: 2.4\n  - quantity: sessions with RL neurons\n    value: 27\n    tolerance: 2.7\n  - quantity: sessions with AL neurons\n    value: 24\n    tolerance: 2.4\n  - quantity: sessions with PM neurons\n    value: 20\n    tolerance: 2\n  - quantity: sessions with AM neurons\n    value: 26\n    tolerance: 2.6\n  criterion: M1 per area, sessions without neurons in the area excluded, all sessions and stimuli\n    pooled. The paper gives no bound for \"around 1\"; read as each area's median slope within 0.9\n    to 1.1 (10% of 1, the protocol default). Reproduced when all five areas meet it, partially\n    when three or four do.\n- id: figs4ab-noise-correlation-under-manipulation\n  statement: Rescaling residuals to change the slope leaves pairwise noise correlations unchanged\n    but changes population-wise noise correlation.\n  source: Figure S4A, S4B; Discussion, paragraph 5\n  quote: Notably, this manipulation does affect the population-wise noise correlation, defined as\n    the fraction of variance explained by the first principal component of the population\n    activity (Figure S4B)\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: M2 in each V1 session at slopes 0, 1 and 2. Reproduced when every neuron pair's noise\n    correlation per stimulus equals the as-is value to within 1e-6 (it must, by construction),\n    and the fraction of variance on the first PC of each stimulus manifold differs from as-is for\n    most stimuli at slopes 0 and 2. The example in the figure is session index 7\n    (decode_noise_corr.ipynb cell 18); all sessions are reported.\n- id: fig1d-dimensionality-falls-with-slope\n  statement: The effective dimensionality of individual stimulus manifolds falls as the slope\n    rises from 0 to 2.\n  source: Figure 1D; Results, first section, paragraph 5\n  quote: When the slope is 0, the stimulus manifold has the same variance across all axes,\n    resulting in a spherical shape and a higher effective dimension. Conversely, when the slope\n    increases to 2, variance becomes even larger in the axes with larger means, resulting in a\n    more elliptical shape and a lower effective dimension.\n  statistics:\n  - test: Wilcoxon signed-rank test across sessions, slope-changed against as-is\n    p: 0.05\n    p_relation: \"<\"\n    n: 30 sessions\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: Effective dimensionality per stimulus as the Methods define it, (sum of eigenvalues)\n    squared over the sum of squared eigenvalues of the covariance, divided by N; averaged over\n    stimuli per session; M2 slopes 0 to 2. Judged by O2 (decreasing) with M4.\n- id: figs5a-movie-slope-near-1\n  statement: In the natural movie data the across-neuron log-mean against log-variance relation\n    is also linear with slope near 1.\n  source: Figure S5A; Results, first section, paragraph 8\n  quote: The log-mean vs. log-variance of spike counts during a designated movie segment showed a\n    linear relationship across neurons with slope near 1, as in the natural scenes data\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, Functional Connectivity sessions,\n    natural movie one (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  expected:\n  - quantity: sessions analyzed\n    value: 23\n    tolerance: 0\n  - quantity: movie bins per session\n    value: 75\n    tolerance: 0\n  criterion: 12-frame (400 ms) bins treated as stimuli, M1 per bin and session, all pooled (23 of\n    26 sessions; 3 excluded for truncated movies or no V1 units). Counts are exact by\n    construction. The paper gives no bound for \"near 1\"; read as the median of the pooled slopes\n    within 0.9 to 1.1 (protocol default), with 0.85 to 1.15 as a second reading because the\n    paper's code printed a median of 1.11 for this panel (fit_slope_histogram.ipynb cell 46).\n    Reproduced under either reading; both are reported.\n- id: figs5c-space-occupancy-peak\n  statement: The fraction of the neural state space occupied by the 119 stimulus manifolds is\n    maximal when the slope is around 1.\n  source: Figure S5C; Results, first section, paragraph 9\n  quote: This analysis confirms that the neural state space occupancy (i.e., packing efficiency)\n    is maximal when slope is around 1.\n  statistics:\n  - test: Wilcoxon signed-rank test across sessions, slope-changed against as-is\n    p: 0.05\n    p_relation: \"<\"\n    n: 30 sessions\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: Bounding box per neuron from the as-is data (minimum minus 1 to maximum plus 1), the\n    same box for the slope-changed data, count of occupied unit voxels (edge 1 spike) as in the\n    Methods and compute_percent_filled in box_and_overlap.py. Judged by O1.\n- id: fig2a-overlap-rises-with-slope\n  statement: The overlap percentage between stimulus manifolds increases with the slope.\n  source: Figure 2A; Results, Neural variability structure enables maximal discriminability,\n    paragraph 1\n  quote: We found that overlap percentage increases with slope, in good agreement with our\n    observations of the dimensionality reduced visual representation space.\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: M3 for every ordered pair of the 119 stimuli, averaged per session (diagonal set to\n    0 as in RSA_overlap_SCC.ipynb). Judged by O2 (increasing) with M4. The legend's test is\n    Wilcoxon signed-rank; its threshold is cut from the text and taken from the code (0.05).\n- id: fig2b-decoding-falls-with-slope\n  statement: Linear SVM decoding accuracy of image identity decreases monotonically as the slope\n    increases, above the chance level of 1/119.\n  source: Figure 2B; Results, Neural variability structure enables maximal discriminability,\n    paragraph 2\n  quote: As expected, cross-validation accuracy decreases monotonically as a function of log-mean\n    vs. log-variance slope.\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: sklearn SVC with a linear kernel and default C (RSA_decoding.py), 10-fold stratified\n    cross-validation, counts centered by the training mean per fold, mean accuracy per session;\n    the 47-to-50-repeat session subsampled to 47. Judged by O2 in its strict reading (a decrease\n    at every 0.1 step of the across-session mean) with M4; partially reproduced when slopes 0 and\n    2 differ from as-is in the stated direction but the decrease is not strict. Accuracy above\n    1/119 at every slope is reported.\n- id: fig2c-continuity-from-slope-1\n  statement: The largest strongly connected component of the stimulus manifold network covers all\n    stimuli only from a slope of about 1 upward, so the representation space is discontinuous\n    below 1.\n  source: Figure 2C; Results, Neural variability structure enables maximal discriminability,\n    paragraph 4\n  quote: This analysis revealed that indeed, the visual representation space became continuous\n    starting around log-mean vs. log-variance slope of 1 (Figure 2C).\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  depends_on:\n  - fig2a-overlap-rises-with-slope\n  criterion: Directed edge from A to B when the M3 overlap of A relative to B is above zero;\n    largest strongly connected component per session and slope (networkx, RSA_overlap_SCC.ipynb\n    cell 18). \"Starting around 1\" is open; readings, the smallest slope at which the\n    across-session mean size reaches 119 lies in (a) 0.8 to 1.2, (b) 0.7 to 1.3. Reproduced when,\n    under one reading, that holds and the mean size at slope 0 is below 119 and differs from\n    as-is by M4.\n- id: fig2d-tangent-angle-rises-below-1\n  statement: The tangent space angle between adjacent stimulus manifolds increases as the slope\n    decreases.\n  source: Figure 2D; Results, Neural variability structure enables maximal discriminability,\n    paragraph 5\n  quote: As predicted, the tangent space angle increased as the slope decreased (Figure 2D right).\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: Nearest neighbor stimulus by M5; points of tangency, local PCA on k = 5 neighbors,\n    weighted angle, and the 25%, 50% and 90% cut-offs as in the Methods (Tangent space angle) and\n    tangent_angle.py. Averaged over stimuli per session. Judged by O2 (decreasing with slope)\n    with M4.\n- id: fig3bc-geodesic-orthogonal-correlation\n  statement: Across stimulus pairs, the geodesic distance between manifold centroids correlates\n    positively with orthogonal variance, so variance is small toward nearby stimuli and large\n    toward faraway ones.\n  source: Figure 3B, 3C; Results, Neural variability structure of individual visual stimuli,\n    paragraph 2\n  quote: We found that the geodesic distance between the centroids of a pair of stimulus manifolds\n    has a positive correlation with the orthogonal variance (Figures 3B and 3C).\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: As-is data. Geodesic distance by M5, orthogonal variance as in\n    illusion-fig3a-orthogonal-variance-example, Spearman correlation over the 14042 ordered pairs\n    per session. The text reports no test; the code tests the session correlations against 0 by\n    a one-sided Wilcoxon signed-rank test (ortho_variance.ipynb cell 13). Reproduced when the\n    mean session correlation is positive and that test gives p < 0.05.\n- id: fig3d-correlation-peaks-near-1\n  statement: The correlation between geodesic distance and orthogonal variance is highest near a\n    slope of 1.\n  source: Figure 3D; Results, Neural variability structure of individual visual stimuli,\n    paragraph 2\n  quote: When varying the log-mean vs. log-variance slope, the correlation between geodesic\n    distance and orthogonal variance was highest near the slope of 1 (Figure 3D).\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  depends_on:\n  - fig3bc-geodesic-orthogonal-correlation\n  criterion: As fig3bc at each M2 slope, geodesic distances recomputed on the slope-changed data\n    (compute_geo_ortho.py). Judged by O1.\n- id: fig3e-local-alignment-peaks-near-1\n  statement: The alignment of each stimulus manifold's first principal component with that of its\n    nearest neighbor manifold is highest around a slope of 1.\n  source: Figure 3E right; Results, Neural variability structure of individual visual stimuli,\n    paragraph 4\n  quote: As predicted, the local alignment was highest when the log- mean vs. log-variance slope\n    was around 1 (Figures 3E right).\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: Absolute cosine similarity between PC1 of each manifold and PC1 of its nearest\n    neighbor by M5, in the N-neuron space, averaged over the 119 stimuli per session\n    (local_global_alignment.py). Judged by O1.\n- id: fig3f-global-alignment-peaks-near-1\n  statement: The alignment of each stimulus manifold's first principal component with that of the\n    rest of the global manifold is highest around a slope of 1.\n  source: Figure 3F right; Results, Neural variability structure of individual visual stimuli,\n    paragraph 5\n  quote: Global alignment was also highest when the log-mean vs. log-variance slope was around 1\n    (Figure 3F right).\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: Absolute cosine similarity between PC1 of each manifold and PC1 of all trials of the\n    other 118 stimuli, averaged per session (local_global_alignment.py). Judged by O1.\n- id: fig4a-overlap-consistency-within-mice\n  statement: The consistency of overlap percentages between two random halves of the V1 neurons\n    of a session peaks near a slope of 1.\n  source: Figure 4A; Results, Neural variability structure is optimal for coding consistency,\n    paragraph 3\n  quote: The overlap consistency peaked near slope 1 (Figure 4A).\n  statistics:\n  - test: Wilcoxon signed-rank test across sessions, slope-changed against as-is\n    p: 0.05\n    p_relation: \"<\"\n    n: 30 sessions\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: Neurons split at random into two equal halves, M3 overlap matrix (119 by 119) per\n    half, Spearman correlation of the two matrices, averaged over 10 partitions per session.\n    Whether the slope fit and manipulation are done on all neurons before splitting or on each\n    half is not stated; the code fits on all neurons and splits after (RSA_overlap_SCC.ipynb,\n    box_and_overlap.py compute_overlap_stimpairs_consis), which is followed. Judged by O1.\n- id: fig4c-rsm-similarity-within-mice\n  statement: Representational similarity matrices from two halves of the V1 neurons of a session\n    are most similar around a slope of 1.\n  source: Figure 4C; Results, Neural variability structure is optimal for coding consistency,\n    paragraph 4\n  quote: we found that the RSMs in distinct neuronal subsets within V1 were most consistent with\n    each other around slope 1 (Figure 4C).\n  statistics:\n  - test: Wilcoxon signed-rank test across sessions, slope-changed against as-is\n    p: 0.05\n    p_relation: \"<\"\n    n: 30 sessions\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: Trial order randomized within each stimulus; for every unordered pair of trial\n    indices (r choose 2, itertools combinations in RSA_decoding.py), cosine similarity between\n    the population vectors of all stimulus pairs; the matrices averaged to an RSM per half;\n    Spearman correlation of the two flattened RSMs, averaged over 10 partitions. Judged by O1.\n- id: fig4d-overlap-consistency-across-mice\n  statement: The consistency of overlap percentages between pairs of mice peaks around a slope of\n    1.\n  source: Figure 4D; Results, Neural variability structure is optimal for representational\n    similarity robustness across different mice, paragraph 2\n  quote: We found that both overlap consistency and the similarity of RSMs peaked around log-mean\n    vs. log-variance slope of 1 (Figures 4D and 4E).\n  statistics:\n  - test: Wilcoxon signed-rank test across session pairs, slope-changed against as-is\n    p: 0.05\n    p_relation: \"<\"\n    n: 435 session pairs\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: M3 overlap matrix per session with all its V1 neurons, Spearman correlation between\n    the matrices of every pair of sessions. Judged by O1 over session pairs.\n- id: fig4e-rsm-similarity-across-mice\n  statement: Representational similarity matrices of pairs of mice are most similar around a\n    slope of 1.\n  source: Figure 4E; Results, Neural variability structure is optimal for representational\n    similarity robustness across different mice, paragraph 2\n  quote: We found that both overlap consistency and the similarity of RSMs peaked around log-mean\n    vs. log-variance slope of 1 (Figures 4D and 4E).\n  statistics:\n  - test: Wilcoxon signed-rank test across session pairs, slope-changed against as-is\n    p: 0.05\n    p_relation: \"<\"\n    n: 435 session pairs\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: RSM per session as in fig4c with all its V1 neurons, Spearman correlation between\n    the RSMs of every pair of sessions (RSA_decoding.py). Judged by O1 over session pairs.\n- id: figs6-higher-areas-consistency\n  statement: Several higher visual areas, including LM and PM, have near maximal representational\n    consistency at a slope of 1, within and across mice.\n  source: Figure S6B, S6C; Results, Neural variability structure is optimal for representational\n    similarity robustness across different mice, paragraph 3\n  quote: In addition, several higher visual areas, including LM and PM, had near maximal\n    consistency at slope 1 (Figure S6B and S6C).\n  statistics:\n  - test: Wilcoxon signed-rank test across sessions or session pairs, slope-changed against as-is\n    p: 0.05\n    p_relation: \"<\"\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  criterion: Analyses of fig4c and fig4e for LM and PM, sessions without neurons in the area\n    excluded. \"Near maximal\" is open; read as the value at slope 1 within one SEM (across\n    sessions or pairs) of the curve's maximum and not differing from the maximum slope's value by\n    the M4 test. Reproduced when this holds for LM and PM in both S6B and S6C, partially when it\n    holds in two or three of the four panels. The other areas are reported.\n- id: figs4c-shuffling-alters-dependence\n  statement: Destroying pairwise noise correlations by shuffling trials within stimulus for each\n    neuron changes how decoding accuracy and RSM similarity depend on the slope.\n  source: Figure S4C; Discussion, paragraph 5\n  quote: When we destroyed the pairwise noise correlation structure by shuffling the trial order\n    for each neuron within each trial type, both the decoder accuracy and the representation\n    similarity analysis showed an altered dependence on the log-mean vs. log-variance slope\n    (Figure S4C).\n  statistics:\n  - test: Wilcoxon signed-rank test across sessions or session pairs, original against shuffled\n    p: 0.05\n    p_relation: \"<\"\n  data: elsewhere\n  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block\n    (https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels)\n  depends_on:\n  - fig2b-decoding-falls-with-slope\n  - fig4c-rsm-similarity-within-mice\n  - fig4e-rsm-similarity-across-mice\n  criterion: The analyses of Figures 2B, 4C and 4E repeated on data shuffled within stimulus for\n    each neuron before slope manipulation. Reproduced when, for each of the three analyses, the\n    original and shuffled curves differ by the Wilcoxon signed-rank test at p < 0.05 at one or\n    more slopes (the green lines of the legend), partially when this holds for one or two.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/kim-2025.yaml paper/10.1101-2025.06.30.662469.txt; python - <<'EOF'
import yaml,re
t=open('claims/kim-2025.yaml').read()
d=yaml.safe_load(t)
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str):
        if ': ' in x: print('colon-space', p)
        if '—' in x or 'rather' in x: print('style', p)
walk(d)
print(len(d['claims']), sum('quote' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']))
EOF
grep -n -i "rather\|—" claims/kim-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/kim-2025.yaml`, and the quote checker passes: 28 claims, 27 quotes, 0 problems. Nothing is committed.

**Text read.** The file under `paper/` is the bioRxiv preprint posted July 4, 2025, under an earlier title: "Neural variability structure in primary visual cortex is optimal for robust representation of visual similarity". The registry's title ("Intrinsic geometry of trial-to-trial variability…") belongs to a later version, which was not supplied. Every claim comes from the July 2025 text. That text includes the Results, Discussion, Methods and the legends of Figures 1–4 and S1–S6. The supplementary figures are part of it, so there is no separate supplement. There was no PDF.

**Code read.** The linked repository is jhk4839/Neural_variability_robustness. I read it at commit ac3300b (2025-07-03), the last commit before the preprint was posted; its figure numbers match this text. The head of the repository belongs to the 2026 version and was not used.

**What DANDI:000248 holds for this paper.** It is the OpenScope Illusion dataset, and the paper uses it only for the Isomap pictures in Figures 1C (bottom), 3A, 3E (left) and 3F (left). All the quantitative results are on the Allen Visual Coding Neuropixels data, which is not in this dandiset. So 24 claims are `data: elsewhere`. The four claims this dandiset can test are:
- a link claim: the ICwcfg1 block, its 12 stimuli with 400 repeats, the example session sub_630506 named in the code, and V1 units;
- the Figure 1C geometry: continuous with little overlap as-is, discontinuous at slope 0, heavily overlapping at slope 2;
- the Figure 3A example: orthogonal variance larger toward the faraway stimulus than the nearby one;
- the Methods sentence saying the geometric changes are "qualitatively similar across datasets".

**Counts.**

| | Number |
|---|---|
| Claims | 28 (27 findings, 1 link) |
| With a quote | 27 (all but the link claim) |
| With statistics | 10 |
| With a criterion | 28 |
| With expected values | 6 |

**Details the paper leaves open, and the readings named:**
- **O1, "peaks near slope 1".** No window is given. Readings: the slope with the highest across-session mean lies in (a) 0.8–1.2 or (b) 0.7–1.3. In both, slopes 0 and 2 must be lower than as-is and differ from it by a Wilcoxon signed-rank test, uncorrected, as in the code.
- **O2, "increases or decreases with slope".** Read as slope 0, 1 and 2 in that order, with the ends differing from as-is. "Monotonically" in Figure 2B is read strictly: a change in the stated direction at every 0.1 step.
- **O3, which Illusion units.** Readings: (a) all units located in VISp (not VISpm), as the code does, with no quality filter; (b) the same units with the Allen quality criteria from the Methods.
- **O4, the example session.** The text says only "one example session". The code uses sub_630506; the other sessions are a variant.
- **Figure 2C, "continuous starting around 1".** Same two windows as O1.
- **"Near 1" for the behavioural-state, higher-area and movie slopes.** No bound is given, so I used 0.9–1.1 (the protocol's 10% default). For the movie I added 0.85–1.15, because the paper's own code printed a median of 1.11.
- **Figure S6, "near maximal".** Read as the value at slope 1 within one SEM of the curve's maximum and not differing from it by the test.
- **Which "geometric changes" were compared across datasets.** Read as falling effective dimensionality and rising overlap.
- **Figures 1C and 3A.** These are pictures, and the 3A arrow lengths are set by hand in the code. They are judged with the paper's own overlap, connected-component and orthogonal-variance measures, computed in the full neuron space.

**Missing from the paper:**
- The Methods equations (slope manipulation, effective dimensionality, orthogonal component, number of trial pairs in the similarity analysis, the modulated Poisson model) are lost in the text. They were taken from the code.
- The legends of Figures 2 and 3 are cut before the p threshold. It was taken from the code, so no statistics are recorded for those claims.
- No p-values are printed for Figure S2 or for the positive correlation in Figure 3B and 3C.
- The paper gives no AllenSDK or data release.
- The code reads the Illusion data from a post-processed MATLAB copy that is not in the repository, so it cannot be checked whether its units were already filtered.

## End of run

27 turns, 6 minutes, $2.60 at API prices, result: success.
