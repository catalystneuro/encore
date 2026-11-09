# 000623 · claims · run 39922410203

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000623 paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md
```

**Agent calls Bash**

```bash
ls claims/001453/ claims/000623 paper/ ; wc -c paper/*
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

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150
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
[... 130 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41597-024-03029-1.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
s=open('paper/10.1038-s41597-024-03029-1.txt').read()
i=s.find('Fig. 7 Example event selective')
print(s[i:i+12000])"
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text is there (Data Descriptor, no supplement). Now the code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/rutishauserlab/bmovie-release-NWB-BIDS && cd bmovie-release-NWB-BIDS && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | head -100
```

```
8c35290b74a9522bf27cbcae44dcb88ff2a1d58f 2024-02-27 15:16:43 -0500
./make_env.yml
./code/inlab_src/sudata.py
./code/inlab_src/helpers_inlab.py
./code/inlab_src/generate_movieNWBs.py
./code/inlab_src/README.md
./code/inlab_src/BDmovie_sessions.ini
./code/gen_table1_subj_info.py
./code/fmri_qc/prepdata-isc-fsaverage.py
./code/fmri_qc/gen_figure5_isc-fsaverage.py
./code/fmri_qc/gen_figure4c_tsnr-fsaverage.py
./code/fmri_qc/gen_figure4b_tsnr-nativeviolin.py
./code/fmri_qc/gen_figure4a_framewisedisp.py
./code/fmri_qc/compute-tsnr-volume.py
./code/fmri_qc/compute-tsnr-fsaverage.py
./code/fmri_qc/compute-isc-fsaverage.py
./code/fmri_qc/budapestcode/utils.py
./code/fmri_qc/budapestcode/__pycache__/utils.cpython-39.pyc
./code/fmri_qc/budapestcode/__pycache__/utils.cpython-311.pyc
./code/fmri_qc/budapestcode/README.md
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS && wc -l code/ephys_qc/*.py code/ephys_qc/*/*.py README.md && cat README.md
```

```
440 code/ephys_qc/ephys_utills.py
   140 code/ephys_qc/gen_figure1d_electrodelocs.py
   238 code/ephys_qc/gen_figure2ah_singleunitQC.py
   174 code/ephys_qc/gen_figure2i_recordinglocs.py
   238 code/ephys_qc/gen_figure3_eyetracking.py
   216 code/ephys_qc/gen_figure3_recogtask_roc.py
   347 code/ephys_qc/ieeg/examine_channels_recognitiontask.py
   336 code/ephys_qc/ieeg/examine_channels_scenecuts.py
   172 code/ephys_qc/ieeg/prep_filterLFP.py
   176 code/ephys_qc/ieeg/vizutils_channel.py
   276 code/ephys_qc/singleneuron/examine_neurons_recognitiontask.py
   277 code/ephys_qc/singleneuron/examine_neurons_scenecuts.py
   206 code/ephys_qc/singleneuron/vizutils_neuron.py
   199 README.md
  3435 total
# Multimodal single-neuron, intracranial EEG, and fMRI brain responses during movie watching in human patients

This repository contains Python scripts to accompany our data descriptor paper titled "Multimodal single-neuron, intracranial EEG, and fMRI brain responses during movie watching in human patients". The code includes functionalities to read and plot data from NWB and BIDS files and perform various data validation analyses.

## Table of Contents
[... 194 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS/code/ephys_qc && cat ephys_utills.py singleneuron/examine_neurons_recognitiontask.py
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import numpy as np


# Function to assign colors based on channel names (brain areas)
from matplotlib.colors import to_rgb
def get_color(ch_name, xrgb=True):
    ch_name_u = ch_name.lower()
    
    if 'amy' in ch_name_u:
        return to_rgb('C1') if xrgb else 'C1'
    elif 'acc' in ch_name_u:
        return to_rgb('C0') if xrgb else 'C0'
    elif 'hip' in ch_name_u:
        return to_rgb('C3') if xrgb else 'C3'
[... 697 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS/code/ephys_qc && grep -n "def get_bootstrappval" -A25 singleneuron/vizutils_neuron.py; grep -n "def get_NulltestPvals_cols" -A25 singleneuron/vizutils_neuron.py; diff singleneuron/examine_neurons_recognitiontask.py singleneuron/examine_neurons_scenecuts.py
```

```
14:def get_bootstrappval(x, alternative='two-sided'):
15-    ''' Calculate bootstrap p-value
16-    the null hypothesis is that the mean of the distribution 
17-    from which x is sampled is zero. '''
18-
19-    x = np.array(x)
20-    assert x.ndim == 1
21-    assert alternative in ['two-sided', 'one-sided']
22-    
23-    if np.mean(x) > 0:
24-        p_1 = (np.sum(x<=0)+1.)/(x.size+1.)
25-        p_2 = (np.sum(x>0)+1.)/(x.size+1.)
26-    elif np.mean(x) < 0:
27-        p_1 = (np.sum(x<0)+1.)/(x.size+1.)
28-        p_2 = (np.sum(x>=0)+1.)/(x.size+1.)
29-    else: # rare but happens in this electrophys data 
30-        p_1 = (np.sum(x<=0)+1.)/(x.size+1.)
31-        p_2 = (np.sum(x>=0)+1.)/(x.size+1.)
32-
33-    # Return the appropriate p-value based on the 'alternative' parameter
[... 306 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS && grep -rn "def get_NulltestPvals_cols" -A20 code/; head -5 assets/annotations/scenecut_info.csv; python3 -c "
import pandas as pd,numpy as np
d=pd.read_csv('assets/annotations/scenecut_info.csv');print(len(d), d.columns.tolist()); print(len(np.where(np.diff(d['scene_id']))[0])+1)"
```

```
Exit code 1
scene_id,shot_start_fr,shot_start_t,shot_dur_t,location,cut_type,cut_dur_t,cut_dur_fr
1.0,1.0,0.0,4.72,backyard,cut,0.0,0
1.0,119.0,4.72,10.28,backyard,cut,0.0,0
1.0,376.0,15.0,1.72,backyard,cut,0.0,0
1.0,419.0,16.72,2.36,backyard,cut,0.0,0
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import pandas as pd,numpy as np
ModuleNotFoundError: No module named 'pandas'
```

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS && grep -rn "NulltestPvals" code/ | head; python3 -c "
import csv
r=list(csv.DictReader(open('assets/annotations/scenecut_info.csv')));print(len(r)); s=[x['scene_id'] for x in r]; print(sum(1 for a,b in zip(s,s[1:]) if a!=b)+1)"
```

```
code/ephys_qc/singleneuron/vizutils_neuron.py:40:get_NulltestPvals_cols = lambda x, x_pmean: [ (np.sum(x[:,p_ii]>=x_pmean[p_ii])+1.)/float(x.shape[0]+1.) if x_pmean[p_ii] > 0 else
code/ephys_qc/singleneuron/examine_neurons_scenecuts.py:22:from vizutils_neuron import plot_cellraster, get_bootstrappval, get_NulltestPvals_cols
code/ephys_qc/singleneuron/examine_neurons_scenecuts.py:233:    pval_nulltest = get_NulltestPvals_cols(area_counts_null_dist, cell_significant)
code/ephys_qc/singleneuron/examine_neurons_recognitiontask.py:21:from vizutils_neuron import plot_cellraster, get_bootstrappval, get_NulltestPvals_cols
code/ephys_qc/singleneuron/examine_neurons_recognitiontask.py:233:    pval_nulltest = get_NulltestPvals_cols(area_counts_null_dist, cell_significant)
code/ephys_qc/ieeg/vizutils_channel.py:40:get_NulltestPvals_cols = lambda x, x_pmean: [ (np.sum(x[:,p_ii]>=x_pmean[p_ii])+1.)/float(x.shape[0]+1.) if x_pmean[p_ii] > 0 else
code/ephys_qc/ieeg/examine_channels_scenecuts.py:26:from vizutils_channel import get_bootstrappval, get_NulltestPvals_cols
code/ephys_qc/ieeg/examine_channels_scenecuts.py:236:        pval_nulltest = get_NulltestPvals_cols(area_counts_null_dist, chs_significant)
code/ephys_qc/ieeg/examine_channels_recognitiontask.py:25:from vizutils_channel import get_bootstrappval, get_NulltestPvals_cols
code/ephys_qc/ieeg/examine_channels_recognitiontask.py:250:        pval_nulltest = get_NulltestPvals_cols(area_counts_null_dist, chs_significant)
93
13
Shell cwd was reset to
```

**Agent**

Code repo read (commit 8c35290). Now the channel-level scripts.

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS/code/ephys_qc/ieeg && sed -n 1,172p prep_filterLFP.py && sed -n 30,60p vizutils_channel.py
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Load NWB files to extract and preprocess iEGG signals, both micros and macros, to 
obtain the high-frequency broadband (HFB) time-course per channel.
"""


import os
import numpy as np
from glob import glob

from pynwb import NWBHDF5IO

import mne
from scipy.stats import zscore
import argparse

# note that in micros and macros data, 
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS/code/ephys_qc/ieeg && cat examine_channels_recognitiontask.py; diff examine_channels_recognitiontask.py examine_channels_scenecuts.py
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Load NWB files and preprocessed HFB signals to calculate the ratio of event selective channels 
and plot Figure 6 c,d. 

"""


import os
import numpy as np

from pynwb import NWBHDF5IO
from scipy.stats import mode

from glob import glob
from tqdm import tqdm
import mne
import argparse
[... 686 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS/code/ephys_qc && cat gen_figure2ah_singleunitQC.py | sed -n 1,238p
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Plots SU QC metrics as shown in Figure 2 a-h. 

"""

# Required Libraries
import os
import numpy as np
from pynwb import NWBHDF5IO
from ephys_utills import get_color
import matplotlib.pyplot as plt
from glob import glob
import argparse

# Set SVG font type for Matplotlib
plt.rcParams['svg.fonttype'] = 'none'

[... 220 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS/code/ephys_qc && sed -n 1,238p gen_figure3_eyetracking.py
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Assess and plot eye tracking data quality recorded during the EMU sessions

"""

import os
import numpy as np
import pandas as pd
from pynwb import NWBHDF5IO
from tqdm import tqdm
from glob import glob

from ephys_utills import get_et_timebins, compute_pixelperDVA, et_heatmap

import matplotlib.pyplot as plt
import argparse

[... 220 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS/code/ephys_qc && sed -n 1,216p gen_figure3_recogtask_roc.py
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Assess and plot behavioral ROC curves for recognition task for the EMU sessions

This code and used helper functions are adapted from:
https://github.com/rutishauserlab/recogmem-release-NWB/tree/master/RutishauserLabtoNWB/events/newolddelay/python/analysis

"""

import os
import numpy as np
from glob import glob

from pynwb import NWBHDF5IO
from ephys_utills import cal_d_prime, cal_auc, check_inclusion, dynamic_split

import matplotlib.pyplot as plt
import argparse
[... 197 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS/code && grep -v "^\s*#" fmri_qc/gen_figure4a_framewisedisp.py | sed -n 1,200p | grep -v "^\s*$" | head -90; grep -v "^\s*$" gen_table1_subj_info.py | head -80
```

```
'''
Framewise displacement in mm for each participant across all runs as shown in Fig. 4a.
---------------------------------------------------------------------------------
This code is adapted from:
https://github.com/mvdoc/budapest-fmri-data/tree/master/scripts/quality-assurance
Copyright 2020 Matteo Visconti di Oleggio Castello and Jiahui Guo
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS/code/fmri_qc && grep -n "mask\|mean\|std\|tsnr\|clean" compute-tsnr-volume.py gen_figure4b_tsnr-nativeviolin.py | head -40; grep -n "corr\|mean\|arctanh\|tanh" compute-isc-fsaverage.py | head -30; grep -n "median\|outlier" gen_figure4a_framewisedisp.py | head
```

```
compute-tsnr-volume.py:6:(as implemented in budapestcode.utils.clean_data)
compute-tsnr-volume.py:8:The tSNR values in native space are plotted in a violin plot across subjects in plot-tsnr-group.py. 
compute-tsnr-volume.py:45:from budapestcode.utils import compute_tsnr
compute-tsnr-volume.py:68:        tsnr_runs = []
compute-tsnr-volume.py:75:            tsnr_runs.append(compute_tsnr(data, conf))
compute-tsnr-volume.py:77:        # compute mean tsnr
compute-tsnr-volume.py:78:        tsnr_mean = np.mean(tsnr_runs, 0)
compute-tsnr-volume.py:81:        tsnr_tosave = tsnr_runs + [tsnr_mean]
compute-tsnr-volume.py:82:        run_types = [f'{i:02d}' for i in range(1, 3)] + ['mean']
compute-tsnr-volume.py:84:        tsnr_outdir = f'{output_dir}/{subject}'
compute-tsnr-volume.py:85:        os.makedirs(tsnr_outdir, exist_ok=True)
compute-tsnr-volume.py:87:        for run, t in zip(run_types, tsnr_tosave):
compute-tsnr-volume.py:89:            fnout = f'{subject}_task-movie_run-{run}_space-T1w_desc-tsnr.nii.gz'
compute-tsnr-volume.py:91:            fnout = f"{tsnr_outdir}/{fnout}"
compute-tsnr-volume.py:105:python compute-tsnr-volume.py --fmriprep_dir /path/to/fmriprep_directory/ --output_dir /path/to/tsnr_prep_dir
gen_figure4b_tsnr-nativeviolin.py:7:The tSNR values were computed in compute-tsnr-volume.py script.
gen_figure4b_tsnr-nativeviolin.py:53:def make_conjuction_mask(subject, fmriprep_dir):
gen_figure4b_tsnr-nativeviolin.py:54:    mask_fns = glob(os.path.join(fmriprep_dir,
gen_figure4b_tsnr-nativeviolin.py:55:                 f'{subject}/ses-001/func/*space-T1w_desc-brain_mask.nii.gz'))
gen_figure4b_tsnr-nativeviolin.py:56:    brainmask = 1.
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p claims/001453/*.yaml; ls tools; ls docs
```

```
data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: For each fish, the mean of its median angular velocities for the rightward
    stimuli (right, forward right, backward right) minus the mean for the leftward stimuli
    (left, forward left, backward left). Reproduced when this difference is greater than zero
    in each species by a one-sided Wilcoxon signed-rank test at p < 0.05; partially reproduced
    when it holds in one species only. The per-stimulus species medians are reported as well.
- id: fig1h-zf-higher-angular-acceleration
  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the
    distributions of the two species differ for every stimulus.
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
    (Kruskal-Wallis test with Bonferroni correction)
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
  data: with_labels
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/000630 claims/000631; head -60 claims/000630/*.yaml; grep -h "^  [a-z_]*:" claims/000*/*.yaml | sort | uniq -c | sort -rn | head -30
```

```
claims/000630:
10.1126-science.adf0805.yaml

claims/000631:
10.3390-ijms241310921.yaml
# Claims for Chartrand et al. (2023), Science 382, eadf0805, on dandiset 000630.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read. The author manuscript of the version of record in PubMed Central (PMC11864503,
# NIHMS2048794), as text (paper/10.1126-science.adf0805.txt). It has the main text, the legends
# of Figures 1 to 6, and the supplementary PDF (NIHMS2048794-supplement-5.pdf) extracted as text:
# the Materials and Methods, the legends of figs. S1 to S9, and Tables S1 and S2. The four
# supplementary data tables (Data S1 donors, Data S2 subclass statistics, Data S3 metadata
# statistics, Data S4 cross-species statistics, all .xlsx) are not under paper/, so no per-feature
# statistic from them is used here; each claim rests on the sentence or legend it quotes. The
# code that wrote Data S2 and S4 was read instead (below). No figure was opened. The bioRxiv
# preprint (doi:10.1101/2022.10.24.511199) is under paper/ but was not used.
#
# Code read. github.com/AllenInstitute/patchseq_human_L1 at commit 7777857 (2025-05-13), linked
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "elsewhere" -B3 -A6 claims/000630/*.yaml | head -60; grep -n "^[a-z_]*:" claims/000630/*.yaml; sed -n '/Open details/,/^[a-z]/p' claims/000630/*.yaml | head -40
```

```
65-# link claim that matches the dandiset's files to that table (protocol, author step 4).
66-# Mouse electrophysiology (DANDI 000020) is an outside input (`with_inputs`). Morphologies
67-# (BIL doi:10.35077/g.606), transcriptomes (NeMO; processed data in the Zenodo archive) and
68:# cytoarchitecture images are not in the dandiset (`elsewhere`).
69-#
70-# Sets used below, from the code.
71-#  - Strict L1 set: cells listed in human_l1_dataset_strict.csv, soma in L1 or in L2 within
72-#    40 um of the L1/L2 border (Methods, "border cells"; l1_cross_species.ipynb cell 5).
73-#  - Primary set P: strict L1 set, collaborator AIBS (Seattle) and failed_fx_long_squares
74-#    False (l1_load.py, primary_ephys). Table S2 gives 194 such cells among those of the ten L1
--
145-  source: Results, L1 patch-seq pipeline and transcriptomic references, paragraph 1; Figure 1A
146-  quote: many human t-types formed separated clusters, with others clustered in groups of related
147-    t-types, whereas mouse L1 t-types showed more continuous variability
148:  data: elsewhere
149-  where: Allen Brain Map RNA-seq portal (human MTG snRNA-seq of Hodge et al. 2019, mouse VISp
150-    scRNA-seq of Tasic et al. 2018), as the Methods cite them
151-  criterion: The paper shows this with UMAP projections and reports no test or measure for the
152-    contrast. A reading named here, not the paper's test, uses the paper's transcriptomic d'
153-    (Methods, Discriminant analysis, NB d' on the reference data, as used for Fig. 1B); reproduced
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "ALLOWED\|allowed\|fields\|keys" tools/claims_check.py | head -20
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

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));
def walk(d,p=''):
  if isinstance(d,dict):
    if 'properties' in d: print(p, list(d['properties'].keys()), d.get('required'))
    for k,v in d.items(): walk(v,p+'/'+k)
  elif isinstance(d,list):
    for x in d: walk(x,p)
walk(s)"; grep -n "enum" -A3 schemas/claims.schema.json | head -40
```

```
['schema_version', 'dataset', 'paper', 'claims', 'checks'] ['schema_version', 'dataset', 'paper', 'claims']
/properties/dataset ['archive', 'id', 'doi'] ['archive', 'id']
/properties/dataset/if ['archive'] None
/properties/dataset/then ['id'] None
/properties/claims/items ['id', 'statement', 'source', 'kind', 'quote', 'inferred', 'expected', 'statistics', 'criterion', 'depends_on', 'data', 'where'] ['id', 'statement', 'source']
/properties/claims/items/allOf/if ['kind'] ['kind']
/properties/claims/items/allOf/if ['data'] ['data']
/properties/checks/items ['date', 'kind', 'model', 'by', 'ready', 'changes'] ['date', 'kind', 'ready']
/$defs/expected ['quantity', 'value', 'tolerance', 'unit'] ['quantity', 'value']
/$defs/statistic ['about', 'test', 'statistic', 'p', 'p_relation', 'corrected', 'ci', 'n'] None
/$defs/statistic/properties/ci ['level', 'low', 'high', 'unit'] ['low', 'high']
89:            "enum": [
90-              "finding",
91-              "link"
92-            ]
--
141:            "enum": [
142-              "dataset",
143-              "with_labels",
144-              "with_inputs",
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn -i "s\.d\.\|standard deviation\|± \|+/-" claims/*/*.yaml | grep -i toler | head -10; grep -rn -B2 -A2 "tolerance:.*" claims/000939/*.yaml | grep -i "reason\|#" | head
```

```
claims/000005/10.1038-nn.4412.yaml:114:# Tolerances. Where the paper gives mean +- s.e.m., the s.e.m. Where it gives mean +- s.d. over n
claims/000005/10.1038-nn.4412.yaml:1114:  - Open, not settled. Tolerances for mean +- s.d. use the larger of 10% and s.d./sqrt(n), not the s.d. itself. The header gives the reason; the protocol's "stated spread" could also be read as the s.d.
claims/000006/10.1038-s41586-018-0642-9.yaml:669:    the mean + 1 s.d. from the rectified accuracies. Reproduced when all numbers are within tolerance and
claims/000013/10.7554-elife.06619.yaml:65:# Tolerances. Where the paper gives mean +- s.d., the tolerance is the s.d., the paper's stated
claims/000017/10.1038-s41586-019-1787-x.yaml:128:    recorded response, NoGo); the mean over the 39 sessions. Tolerances are the paper's s.d. over
claims/000017/10.1038-s41586-019-1787-x.yaml:131:    are within tolerance under one reading; the s.d. over sessions is reported as well.
claims/000017/10.1038-s41586-019-1787-x.yaml:226:    by findWheelMoves3, its direction that of the movement. Tolerances are the paper's s.d. over
claims/000017/10.1038-s41586-019-1787-x.yaml:472:    4,240). The tolerance is two Poisson s.d. of a count of 14 (7.5 neurons), since 10% (1.4
claims/000017/10.1038-s41586-019-1787-x.yaml:932:    values are within tolerance (the tolerances of the last two are the paper's s.d.).
claims/000045/10.7554-elife.63711.yaml:106:# Tolerances. Where the paper gives mean +- s.d. over mice, the s.d. describes the spread across
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000623/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['most_recent_published_version'] if 'most_recent_published_version' in d else '', d.get('draft_version',{}).get('name'))"; curl -s https://api.dandiarchive.org/api/dandisets/000623/versions/draft/info/ | python3 -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m['name']);print(m.get('description'))"; cat $TMPDIR/bmovie-release-NWB-BIDS/make_env.yml
```

Result: the fetched text is not kept.

**Agent**

Code read. Now writing the claims file.

**Agent calls Bash**

```bash
cd $TMPDIR/bmovie-release-NWB-BIDS && git log -1 --format='%h %cs' && grep -n "def compute_tsnr" -A15 code/fmri_qc/budapestcode/utils.py | head -20; head -3 assets/annotations/scanner_questionnaire.csv
```

```
8c35290 2024-02-27
35:def compute_tsnr(data, confounds):
36-    """Compute tSNR on data by first regressing out the following nuisance
37-    regressors:
38-
39-    - six motion parameters and their derivatives
40-    - global signal
41-    - framewise displacement
42-    - six aCompCor components
43-    - polynomial regressors up to second order
44-
45-    Parameters
46-    ----------
47-    data : array of shape (dim1, dim2, dim3, n_volumes)
48-        EPI data
49-    confounds : pandas Dataframe
50-        dataframe containing confounds generated by fmriprepp
ID,R1 (corrects),R2 (corrects),R1_Q1,R1_Q2,R1_Q3,R1_Q4,R1_Q5,R1_Q6,R1_Q7,R2_Q1,R2_Q2,R2_Q3,R2_Q4,R2_Q5,R2_Q6,R2_Q7
P41CS,5,7,1,1,1,1,0,1,0,1,1,1,1,1,1,1
P42CS,7,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1
[... 1 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/000623/10.1038-s41597-024-03029-1.yaml",
 "content": "# Claims for Keles et al. (2024), Sci Data 11, 214, \"Multimodal single-neuron, intracranial EEG,\n# and fMRI brain responses during movie watching in human patients\", on dandiset 000623.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md (Reader).\n#\n# Text read. The version of record (open access, CC BY 4.0) as served by Europe PMC\n# (paper/10.1038-s41597-024-03029-1.txt): Background and Summary, Methods, Data Records,\n# Technical Validation, Usage Notes, Code availability, Table 1 and the legends of Figures 1 to 7.\n# The paper is a Data Descriptor and has no supplement. No PDF was available and no figure was\n# opened; numbers shown only in figures (the per-area neuron counts of Fig. 2h) are read from the\n# text as noted under `inferred`.\n#\n# Code read. github.com/rutishauserlab/bmovie-release-NWB-BIDS at commit 8c35290 (2024-02-27),\n# linked under Code availability. It holds: gen_table1_subj_info.py (Table 1, with the ages and\n# sexes of the four fMRI-only participants entered by hand); ephys_qc/gen_figure2ah_singleunitQC.py\n# (spike-sorting metrics, Fig. 2a-h); gen_figure3_eyetracking.py (gaze heatmap correlations and\n# missing gaze, Fig. 3a); gen_figure3_recogtask_roc.py (ROC, AUC and the confidence-accuracy\n# t-test, Fig. 3b,c); ephys_utills.py (AUC, d', confidence split, inclusion rule, gaze binning and\n# heatmaps); singleneuron/examine_neurons_recognitiontask.py and examine_neurons_scenecuts.py\n# (memory- and event-selective cells, permutation tests, Fig. 6a,b and 7a,b); ieeg/prep_filterLFP.py\n# (HFB preprocessing) and ieeg/examine_channels_recognitiontask.py and examine_channels_scenecuts.py\n# (selective LFP and iEEG channels, Fig. 6c,d and 7c,d); fmri_qc/ (framewise displacement, tSNR,\n# ISC, adapted from github.com/mvdoc/budapest-fmri-data); and assets/annotations/ (scenecut_info.csv,\n# the 93 annotated cuts with scene_id and shot_start_fr; short_faceannots.pkl, face annotations;\n# scanner_questionnaire.csv, the in-scanner question answers). The code prints the per-area counts\n# and permutation p-values but not the means and s.d. of the quality metrics, nor the run 1 against\n# run 2 AUC test, which is not in the code. The environment file pins no versions (python 3.11,\n# mne-base, numpy, scipy, pynwb).\n#\n# Data the paper used. 20 patients with intractable epilepsy (Table 1; 11 female; age 37.75 +-\n# 13.86, mean (SD)). 16 were recorded in the epilepsy monitoring unit (EMU) with hybrid\n# Behnke-Fried depth electrodes, 29 sessions (\"runs\") in all (two runs for 13 participants, one for\n# P44CS, P58CS and P60CS); 15 were scanned with fMRI (two runs each, 30 runs); 11 did both. Each\n# EMU run is an 8-min edited excerpt of \"Bang! You're Dead\" (25 Hz, 11971 frames), then a\n# recognition test of 40 frames (20 novel, 20 familiar), rated on a 1 to 6 confidence scale (1 to 3\n# novel, 4 to 6 familiar). Recorded variables: spike-sorted single units (OSort, 1450 units) from\n# microwires in amygdala, hippocampus, ACC, preSMA and vmPFC, with per-unit quality metrics; LFP\n# from the microwires and iEEG from the macro contacts, both at 1000 Hz (band 0.1 to 500 Hz), from\n# 10 s before movie start; monocular gaze (EyeLink 1000, 500 Hz) with fixations, saccades, blinks\n# and pupil size; frame times of the movie (NWBFile.stimulus[\"movieframe_time\"]); the trials table\n# (one encoding row for the movie, then one row per recognition trial with stimulus_file,\n# actual_response and response_correct); electrode locations in native and MNI152 space. Spike\n# times are referenced to movie start.\n#\n# Where the data are. The dandiset (\"Data for: Multimodal single-neuron, intracranial EEG, and\n# fMRI brain responses during movie watching in human patients\", 29 NWB assets) holds the EMU\n# data only. The fMRI data (BIDS) are on OpenNeuro, ds004798; the movie annotations and the\n# in-scanner answers are on Figshare (doi:10.6084/m9.figshare.25037045.v4) and in the code\n# repository's assets/annotations at commit 8c35290. Claims on fMRI are `elsewhere`; claims on\n# scene cuts use the annotation file as labels (`with_labels`, through claim scenecut-labels).\n#\n# Shared methods, from the code (cited by name in the criteria).\n#  - Movie window: the trials-table row with stim_phase \"encoding\", start_time to stop_time.\n#  - Unit set U: every unit with at least one spike in the movie window (gen_figure2ah,\n#    examine_neurons_*: \"no spike during encoding\" units are skipped). Brain area is the\n#    electrode's location with \"Left \" or \"Right \" removed.\n#  - Recognition trials: rows with stim_phase \"recognition\"; truth \"new\" or \"old\" from the first\n#    three characters of stimulus_file; response \"new\" when actual_response <= 3. Correct trials\n#    are true positives (old, old) and true negatives (new, new).\n#  - Session rule R (memory analyses): a session is skipped when it has fewer than 10 correct\n#    new or fewer than 10 correct old trials (examine_*_recognitiontask.py).\n#  - Bootstrap selection B: per cell or channel, 10,000 resamples with replacement (numpy\n#    default_rng seed 13) of the two groups' trial responses, the difference of group means per\n#    resample, and the two-sided bootstrap p = 2 x min(p1, p2) with +1 correction (get_bootstrappval);\n#    selective when p < 0.05. Recognition, novel minus familiar, both groups resampled to the\n#    smaller group's size; responses in 0.2 to 1.7 s after trial start_time. Scene cuts, scene\n#    change minus continuity cut, each group resampled to its own size; responses in 0 to 1.0 s\n#    after cut onset; counted only when the difference is positive (see Open details 6).\n#  - Permutation test P: 2,000 shuffles; in each, per cell or channel, n_new + n_old (or n_change\n#    + n_cont) responses drawn without replacement from all of its events (for recognition, all\n#    40 trials including incorrect ones), split into two pseudo-groups, tested by B with 5,000\n#    resamples (unseeded); the null count of selective units per area; area p = (number of null\n#    counts >= observed + 1) / 2001 (get_NulltestPvals_cols). For scene cuts a null unit counts\n#    only when its pseudo-difference is positive, as for the observed count.\n#  - HFB pipeline H (prep_filterLFP.py): per session and per electrode type (LFP_micro, LFP_macro\n#    in processing[\"ecephys\"]), channels whose origchannel_name characters 2 to 4 are AMY, HIP, ACC,\n#    SMA (preSMA) or OFC (vmPFC); time shifted by the 10 s LFP pad so that the movie starts at 0;\n#    the movie window and the recognition block (first trial start to last trial stop), each\n#    padded by 10 s, processed separately; MNE notch filter at 60 Hz and harmonics (zero-double\n#    phase), high-pass 0.1 Hz, common average reference over the kept channels, Morlet power with\n#    5 cycles at 70, 80, ..., 170 Hz, z-scored across time per frequency, averaged across\n#    frequencies, resampled to 500 Hz. Channel area is the channel name without its first and\n#    last character (examine_channels_*).\n#  - Scene cuts S: the 93 rows of scenecut_info.csv; a cut is a scene change when its scene_id\n#    differs from the previous row's, and the first cut is a scene change; onset is the\n#    movieframe_time timestamp of frame shot_start_fr (1-based) in each session.\n#\n# Tolerances. Counts of deposited records (sessions, participants, units, cuts) have tolerance 0:\n# the dataset fixes them. Other values use 10% of the reported value. Where the paper gives mean\n# +- s.d. over units, sessions or pairs, the s.d. describes the spread of the population, not the\n# uncertainty of the mean of a fixed deposited set; the means and the s.d. are each held to 10%.\n#\n# Open details (none of paper, legends or code fixes them; each is named again in its claim).\n#  1. The mean ISI percentage: over all units of U, or over the units with less than 3% plotted\n#     in Fig. 2c (the code plots only these).\n#  2. The degrees of freedom of every s.d. the paper gives (not computed in the code except for\n#     the gaze s.d. and Table 1, both numpy ddof 0). Standard choice ddof 0, ddof 1 shown; it\n#     cannot change an outcome at these n.\n#  3. The missing-gaze mean (7% +- 8%): over the 27 sessions left after P53CS is excluded, or\n#     over all 29.\n#  4. The mean AUC (0.79 +- 0.19): over the 29 sessions (Fig. 3b legend, \"all sessions\"), or over\n#     the 16 participants after averaging their runs (\"across participants\").\n#  5. Sessions in the memory analyses: rule R (the code), or the five runs the text lists as\n#     excluded (P44CS run 1, P51CS run 2, P56CS run 2, P57CS runs 1 and 2). The text's first\n#     criterion, \"behavioral AUC > 0.6\", is read as AUC below 0.6 (excluding sessions above 0.6\n#     would leave almost none); the code applies no AUC rule here.\n#  6. Scene-cut selectivity: the text says the response \"differed significantly\"; the code counts\n#     only cells and channels with scene change > continuity cut (and builds its null the same\n#     way). The text does not say either direction, and the code settles it, so the code's\n#     reading is followed; the count in either direction is shown as a variant.\n#  7. Run 1 against run 2 AUC: not in the code. AUC by cal_auc per run; paired t-test across the\n#     13 participants with two runs, two-sided (scipy ttest_rel default).\n#  8. The permutation test is unseeded; its Monte Carlo standard error (about 0.005 at p = 0.05\n#     with 2,000 shuffles) is reported with each area p. Seed 0 is used as a standard choice.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000623\"\npaper: doi:10.1038/s41597-024-03029-1\nclaims:\n- id: cohort-emu-sessions\n  statement: >-\n    The electrophysiology data come from 16 participants and 29 EMU sessions (runs); 13\n    participants performed two runs and P44CS, P58CS and P60CS one, as Table 1 lists.\n  source: Table 1; Technical Validation, Number of neurons isolated and spike-sorting quality metrics\n  quote: >-\n    We recorded 1450 neurons in total from the amygdala, hippocampus, vmPFC, ACC, and preSMA\n    across 29 sessions involving 16 subjects\n  expected:\n  - quantity: EMU sessions\n    value: 29\n    tolerance: 0\n  - quantity: EMU participants\n    value: 16\n    tolerance: 0\n  - quantity: participants with two EMU runs\n    value: 13\n    tolerance: 0\n  criterion: >-\n    Sessions are NWB files, participants their subject identifiers. Reproduced when the counts\n    match and each participant's number of runs matches its Table 1 row (P41CS, P42CS, P43CS,\n    P47CS, P48CS, P49CS, P51CS, P53CS, P54CS, P55CS, P56CS, P57CS, P62CS two; P44CS, P58CS,\n    P60CS one).\n- id: table1-demographics\n  statement: >-\n    Of the 20 participants 11 are female, and their mean age is 37.75 years (SD 13.86); the age,\n    sex and epilepsy diagnosis of each participant are as in Table 1.\n  source: Table 1\n  inferred: >-\n    Read from Table 1, whose last row gives the totals; no sentence states the ages of the\n    individual participants.\n  expected:\n  - quantity: mean age, 20 participants\n    value: 37.75\n    tolerance: 3.775\n    unit: years\n  - quantity: SD of age, 20 participants\n    value: 13.86\n    tolerance: 1.386\n    unit: years\n  - quantity: female participants\n    value: 11\n    tolerance: 0\n  data: with_inputs\n  where: >-\n    The four fMRI-only participants (P45CS, P46CS, P50CS, P59CS) are not in the dandiset; their\n    age and sex are in Table 1 and entered by hand in gen_table1_subj_info.py (commit 8c35290)\n  criterion: >-\n    As gen_table1_subj_info.py does. For the 16 EMU participants, age (subject.age, \"P..Y\"), sex\n    and diagnosis (subject.description) from the NWB files; for the four fMRI-only participants\n    the Table 1 values. Mean and SD (numpy ddof 0, as the code) over the 20. Reproduced when every\n    EMU participant's age, sex and diagnosis match Table 1 and the totals are within tolerance.\n- id: neurons-total-and-areas\n  statement: >-\n    The dataset holds 1450 single units from amygdala (479), hippocampus (261), ACC (236), preSMA\n    (299) and vmPFC (175).\n  source: >-\n    Technical Validation, Number of neurons isolated and spike-sorting quality metrics; Fig. 2h;\n    Technical Validation, Neuronal responses (movie watching phase), paragraph 1\n  quote: >-\n    We recorded 1450 neurons in total from the amygdala, hippocampus, vmPFC, ACC, and preSMA\n    across 29 sessions involving 16 subjects (Fig. 2h )\n  inferred: >-\n    The per-area counts are shown only in Fig. 2h; they are read from the denominators of the\n    scene-cut analysis, which included every unit (479 + 261 + 236 + 299 + 175 = 1450).\n  expected:\n  - quantity: units\n    value: 1450\n    tolerance: 0\n  - quantity: amygdala units\n    value: 479\n    tolerance: 0\n  - quantity: hippocampus units\n    value: 261\n    tolerance: 0\n  - quantity: ACC units\n    value: 236\n    tolerance: 0\n  - quantity: preSMA units\n    value: 299\n    tolerance: 0\n  - quantity: vmPFC units\n    value: 175\n    tolerance: 0\n  criterion: >-\n    Units of set U (at least one spike in the movie window), as in gen_figure2ah_singleunitQC.py,\n    by electrode location without hemisphere. The count of all units in the files, with no spike\n    rule, is shown as a variant.\n- id: units-per-wire\n  statement: There were on average 1.99 units per wire, counting only wires with at least one unit.\n  source: Technical Validation, Number of neurons isolated and spike-sorting quality metrics; Fig. 2a\n  quote: >-\n    There were on average 1.99 units per wire (only counting wires with at least one isolated\n    neuron)\n  expected:\n  - quantity: mean units per active wire\n    value: 1.99\n    tolerance: 0.199\n  criterion: >-\n    As gen_figure2ah_singleunitQC.py. Per session, the number of units (all units in the file)\n    on each electrode_id; the mean over all session and wire pairs.\n- id: firing-rate\n  statement: The mean firing rate of the neurons was 2.47 +- 3.32 spikes/s (mean +- s.d.).\n  source: Technical Validation, Number of neurons isolated and spike-sorting quality metrics; Fig. 2b\n  quote: the mean firing rate of neurons was 2.47 ± 3.32 (mean ± standard deviation, s.d.; Fig. 2a,b )\n  expected:\n  - quantity: mean firing rate\n    value: 2.47\n    tolerance: 0.247\n    unit: spikes/s\n  - quantity: s.d. of firing rate\n    value: 3.32\n    tolerance: 0.332\n    unit: spikes/s\n  criterion: >-\n    As gen_figure2ah_singleunitQC.py. For each unit of U, the spike count in the movie window\n    divided by its duration; mean and s.d. over units (ddof 0, ddof 1 shown; open detail 2).\n    The paper gives no unit; spikes/s is the axis of Fig. 2b in the code.\n- id: isi-violations\n  statement: The percentage of interspike intervals below 3 ms was 0.40% +- 0.53%.\n  source: Technical Validation, Number of neurons isolated and spike-sorting quality metrics; Fig. 2c\n  quote: the percentage of interspike intervals (ISIs) below 3 ms was 0.40% ± 0.53% (Fig. 2c )\n  expected:\n  - quantity: mean percentage of ISI < 3 ms\n    value: 0.40\n    tolerance: 0.04\n    unit: \"%\"\n  - quantity: s.d. of percentage of ISI < 3 ms\n    value: 0.53\n    tolerance: 0.053\n    unit: \"%\"\n  criterion: >-\n    The units table's isibelow column for the units of U (gen_figure2ah_singleunitQC.py). Open\n    detail 1, two readings: (a) all units of U; (b) units of U with isibelow < 3, the set plotted\n    in Fig. 2c. Reproduced when both values are within tolerance under one reading.\n- id: waveform-snr\n  statement: >-\n    The peak SNR of the mean waveform was 5.95 +- 3.48 and the mean SNR of the whole waveform 2.07\n    +- 1.13.\n  source: Technical Validation, Number of neurons isolated and spike-sorting quality metrics; Fig. 2d,e\n  quote: >-\n    the ratio between peak amplitude of the mean waveform of each cluster and the standard\n    deviation of the noise was 5.95 ± 3.48 (Fig. 2d ; peak SNR) and the mean SNR was 2.07 ± 1.13\n  expected:\n  - quantity: mean peak SNR\n    value: 5.95\n    tolerance: 0.595\n  - quantity: s.d. of peak SNR\n    value: 3.48\n    tolerance: 0.348\n  - quantity: mean of mean SNR\n    value: 2.07\n    tolerance: 0.207\n  - quantity: s.d. of mean SNR\n    value: 1.13\n    tolerance: 0.113\n  criterion: >-\n    The units table's peakSNR and meanSNR columns for the units of U (gen_figure2ah_singleunitQC.py);\n    mean and s.d. over units (open detail 2).\n- id: projection-distance\n  statement: >-\n    The pairwise projection distance between neurons isolated on the same wire was 11.98 +- 8.93\n    s.d. units.\n  source: Technical Validation, Number of neurons isolated and spike-sorting quality metrics; Fig. 2f\n  quote: >-\n    the pairwise projection distance in clustering space between all neurons isolated on the same\n    wire was 11.98 ± 8.93 (Fig. 2f , projection test; in units of s.d. of the signal)\n  expected:\n  - quantity: mean projection distance\n    value: 11.98\n    tolerance: 1.198\n  - quantity: s.d. of projection distance\n    value: 8.93\n    tolerance: 0.893\n  criterion: >-\n    As gen_figure2ah_singleunitQC.py. The electrodes table's pairwise_distances column, entries\n    \"NA\" and empty skipped, each entry split on \"_\" into numbers; all pairs of all sessions pooled;\n    mean and s.d. (open detail 2).\n- id: isolation-distance\n  statement: The median isolation distance of the units was 24.90.\n  source: Technical Validation, Number of neurons isolated and spike-sorting quality metrics; Fig. 2g\n  quote: the median isolation distance was 24.90 (Fig. 2g )\n  expected:\n  - quantity: median isolation distance\n    value: 24.90\n    tolerance: 2.49\n  criterion: >-\n    As gen_figure2ah_singleunitQC.py. The isolationdist column for the units of U, NaN values and\n    values of 1e18 or more removed (the code's outlier rule); the median.\n- id: gaze-missing-p53cs\n  statement: >-\n    Gaze data were missing for more than half of the movie only for P53CS (74% in run 1, 84% in\n    run 2), whose gaze was excluded from the eye-tracking analysis.\n  source: Technical Validation, Eye tracking data quality (behavior), paragraph 1\n  quote: >-\n    The gaze data was missing at more than half of the movie watching duration only for one\n    participant (P53CS, the percentage of missing data was 74% in the first run and 84% in the\n    second run of the movie watching phase)\n  expected:\n  - quantity: P53CS run 1 missing gaze\n    value: 74\n    tolerance: 7.4\n    unit: \"%\"\n  - quantity: P53CS run 2 missing gaze\n    value: 84\n    tolerance: 8.4\n    unit: \"%\"\n  criterion: >-\n    As gen_figure3_eyetracking.py. Gaze samples (processing[\"behavior\"][\"EyeTracking\"]\n    [\"SpatialSeries\"]) in the movie window, mapped to the 640 x 480 movie frame with the display\n    geometry in the series' comments; samples outside the frame set missing; samples grouped in\n    1-s bins over the 479 s of the movie (11971 frames at 25 Hz), empty bins filled as missing;\n    missing fraction = missing samples over all samples. Reproduced when P53CS's two runs are\n    within tolerance and are the only sessions at or above 50%.\n- id: gaze-similarity\n  statement: >-\n    Each participant's gaze was highly correlated with the reference heatmap of the other\n    participants (Pearson's r = 0.75 +- 0.12) and little gaze was missing (7% +- 8%).\n  source: Technical Validation, Eye tracking data quality (behavior), paragraph 1; Fig. 3a\n  quote: >-\n    We found that the individual participant's gaze patterns were highly correlated with the\n    reference visual salience (Pearson's r = 0.75 ± 0.12, mean ± s.d., across participants and\n    runs ... while having low percentages of missing gaze data (7% ± 8%) (Fig. 3a )\n  expected:\n  - quantity: mean gaze heatmap correlation\n    value: 0.75\n    tolerance: 0.075\n  - quantity: s.d. of gaze heatmap correlation\n    value: 0.12\n    tolerance: 0.012\n  - quantity: mean missing gaze\n    value: 7\n    tolerance: 0.7\n    unit: \"%\"\n  - quantity: s.d. of missing gaze\n    value: 8\n    tolerance: 0.8\n    unit: \"%\"\n  depends_on:\n  - gaze-missing-p53cs\n  criterion: >-\n    As gen_figure3_eyetracking.py, after the sessions of claim gaze-missing-p53cs at or above 50%\n    missing are removed. Per 1-s bin, a reference heatmap from the pooled samples of all other\n    participants' sessions (both runs of the same participant left out) and the session's own\n    heatmap, each a 2-D histogram on the 640 x 480 frame downsampled by 5 and Gaussian-smoothed\n    with sigma = the mean over sessions of pixels per degree (compute_pixelperDVA, 40 x 30 cm\n    screen at 60 cm, divided by 5); the session's heatmap is skipped when half or more of the bin's\n    samples are missing; Pearson r of the flattened maps. Per session, the tanh of the mean\n    Fisher z over bins; the reported mean is tanh of the mean of these session z-means and the\n    s.d. tanh of their s.d. (ddof 0), as the code prints. Missing gaze as in gaze-missing-p53cs;\n    open detail 3, mean and s.d. over (a) the remaining sessions or (b) all 29. Reproduced when\n    the correlation values are within tolerance and the missing-gaze values are within tolerance\n    under one reading.\n- id: recognition-auc\n  statement: >-\n    Participants remembered the movie well; their recognition accuracy across confidence levels\n    was 0.79 +- 0.19 AUC.\n  source: Technical Validation, New-old task performance (behavior) in EMU, paragraph 1; Fig. 3b\n  quote: >-\n    Participants had excellent memory: their average accuracy across all confidence levels was\n    0.79 ± 0.19 AUC (Fig. 3b )\n  expected:\n  - quantity: mean AUC\n    value: 0.79\n    tolerance: 0.079\n  - quantity: s.d. of AUC\n    value: 0.19\n    tolerance: 0.019\n  criterion: >-\n    As gen_figure3_recogtask_roc.py. Per session, the recognition trials (trials table after the\n    encoding row); cumulative hit and false-alarm rates from confidence 6 down to 1, adjusted for\n    0 and 1 (adjustHF), and the AUC by the trapezoid rule (cal_auc). Open detail 4, mean and s.d.\n    over (a) the 29 sessions or (b) the 16 participants after averaging their runs; ddof as open\n    detail 2. Reproduced when both values are within tolerance under one reading.\n- id: auc-run1-vs-run2\n  statement: >-\n    Memory accuracy did not differ between the first and second run for the 13 participants with\n    two runs (0.79 +- 0.14 against 0.79 +- 0.24 AUC, p = 0.960, paired t-test).\n  source: Technical Validation, New-old task performance (behavior) in EMU, paragraph 1\n  quote: >-\n    there was no significant difference in memory accuracy between the first and second run for\n    the 13 participants who performed the two runs of movie watching and recognition memory tasks\n    (run #1: 0.79 ± 0.14; run #2: 0.79 ± 0.24 AUC; p = 0.960, paired t-test)\n  statistics:\n  - test: paired t-test\n    p: 0.96\n    n: 13 participants\n  expected:\n  - quantity: mean AUC, run 1\n    value: 0.79\n    tolerance: 0.079\n  - quantity: s.d. of AUC, run 1\n    value: 0.14\n    tolerance: 0.014\n  - quantity: mean AUC, run 2\n    value: 0.79\n    tolerance: 0.079\n  - quantity: s.d. of AUC, run 2\n    value: 0.24\n    tolerance: 0.024\n  depends_on:\n  - recognition-auc\n  criterion: >-\n    A claim of absence. Per-session AUC as in recognition-auc; run number from the session\n    identifier; the 13 participants with two runs. The paper's test, a paired t-test, two-sided\n    (open detail 7). Reproduced when p >= 0.05, not reproduced when p < 0.05; the mean difference\n    and the values against tolerance are reported either way.\n- id: confidence-accuracy\n  statement: >-\n    Recognition accuracy was significantly higher for high-confidence than for low-confidence\n    judgments (p < 0.001, paired t-test).\n  source: Technical Validation, New-old task performance (behavior) in EMU, paragraph 1; Fig. 3c legend\n  quote: >-\n    Accuracy was significantly different between high- versus low-confidence trials (p < 0.001,\n    paired t-test)\n  statistics:\n  - test: paired t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: sessions passing the inclusion rule\n  depends_on:\n  - recognition-auc\n  criterion: >-\n    As gen_figure3_recogtask_roc.py. Sessions included by check_inclusion (AUC >= 0.6, and no\n    more than one unused confidence level among 1 to 3 or among 4 to 6); high and low confidence\n    split per session by dynamic_split (either 1 and 6 high, or 1, 2, 5 and 6 high, whichever\n    split is more balanced, with its fallbacks); accuracy = correct over all trials of each\n    confidence class; scipy ttest_rel of high against low. Reproduced when p < 0.001 with high\n    above low.\n- id: memory-sessions-included\n  statement: >-\n    Of the 1450 neurons, 1266 entered the memory analysis; the rest came from runs excluded for\n    poor behavior (P44CS run 1, P51CS run 2, P56CS run 2, P57CS runs 1 and 2).\n  source: Technical Validation, Neuronal responses (recognition memory phase), paragraph 1\n  quote: >-\n    Of the overall 1450 recorded neurons, 1266 were included in this analysis. The remainder was\n    excluded based on these behavioral criteria ... Excluded patients and runs were P44CS run 1,\n    P51CS run 2, P56CS run 2, P57CS runs 1 and 2\n  expected:\n  - quantity: units in the memory analysis\n    value: 1266\n    tolerance: 0\n  depends_on:\n  - neurons-total-and-areas\n  criterion: >-\n    Units of U in the sessions kept. Open detail 5, (a) rule R (the code) and (b) the five listed\n    runs removed. Reproduced when the count is 1266 under one reading; the sessions each reading\n    removes, and whether they are the five listed, are reported.\n- id: memory-cells-significant\n  statement: >-\n    Significant proportions of cells were memory selective in the amygdala (32/436, p = 0.015),\n    ACC (22/186, p = 0.002) and vmPFC (14/150, p = 0.016).\n  source: Technical Validation, Neuronal responses (recognition memory phase), paragraph 1\n  quote: >-\n    Significant proportions of cells were memory selective in the amygdala (32/436, p = 0.015,\n    permutation test with 2,000 shuffling of average firing rates across trials for each cell),\n    ACC (22/186, p = 0.002), and vmPFC (14/150, p = 0.016)\n  statistics:\n  - about: amygdala\n    test: permutation test, 2,000 shuffles\n    p: 0.015\n    n: 436 cells\n  - about: ACC\n    test: permutation test, 2,000 shuffles\n    p: 0.002\n    n: 186 cells\n  - about: vmPFC\n    test: permutation test, 2,000 shuffles\n    p: 0.016\n    n: 150 cells\n  expected:\n  - quantity: amygdala memory-selective cells\n    value: 32\n    tolerance: 3.2\n  - quantity: amygdala cells analysed\n    value: 436\n    tolerance: 0\n  - quantity: ACC memory-selective cells\n    value: 22\n    tolerance: 2.2\n  - quantity: ACC cells analysed\n    value: 186\n    tolerance: 0\n  - quantity: vmPFC memory-selective cells\n    value: 14\n    tolerance: 1.4\n  - quantity: vmPFC cells analysed\n    value: 150\n    tolerance: 0\n  depends_on:\n  - memory-sessions-included\n  criterion: >-\n    As examine_neurons_recognitiontask.py. Units of U in the sessions of memory-sessions-included;\n    firing rate in 0.2 to 1.7 s after each recognition trial's start_time; correct trials only;\n    selection by bootstrap B (novel against familiar, balanced); area p by permutation test P.\n    Reproduced when each of the three areas has p < 0.05 and its counts are within tolerance;\n    partially reproduced when all three have p < 0.05 but a count is outside tolerance.\n- id: memory-cells-not-significant\n  statement: >-\n    The proportions of memory-selective cells in the hippocampus (14/238, p = 0.30) and preSMA\n    (17/256, p = 0.17) were not significant.\n  source: Technical Validation, Neuronal responses (recognition memory phase), paragraph 1\n  quote: but not the hippocampus (14/238, p = 0.30) and preSMA (17/256, p = 0.17)\n  statistics:\n  - about: hippocampus\n    test: permutation test, 2,000 shuffles\n    p: 0.3\n    n: 238 cells\n  - about: preSMA\n    test: permutation test, 2,000 shuffles\n    p: 0.17\n    n: 256 cells\n  expected:\n  - quantity: hippocampus memory-selective cells\n    value: 14\n    tolerance: 1.4\n  - quantity: hippocampus cells analysed\n    value: 238\n    tolerance: 0\n  - quantity: preSMA memory-selective cells\n    value: 17\n    tolerance: 1.7\n  - quantity: preSMA cells analysed\n    value: 256\n    tolerance: 0\n  depends_on:\n  - memory-sessions-included\n  criterion: >-\n    A claim of absence, on the paper's test as in memory-cells-significant. Reproduced when both\n    areas have permutation p >= 0.05; not reproduced when either has p < 0.05. Counts and p are\n    reported either way.\n- id: memory-lfp\n  statement: >-\n    For microwire LFP HFB power, significant proportions of channels were memory selective in the\n    amygdala (37/368, p = 0.002), ACC (33/368, p = 0.028) and preSMA (40/368, p = 0.001), but not\n    in the hippocampus (17/368, p = 0.90) or vmPFC (28/336, p = 0.05).\n  source: Technical Validation, Neuronal responses (recognition memory phase), paragraph 2\n  quote: >-\n    For the LFP, significant proportions of channels were memory selective in the amygdala\n    (37/368, p = 0.002, permutation test with 2,000 shuffling of average HBF power across trials\n    for each channel), ACC (33/368, p = 0.028), and preSMA (40/368, p = 0.001) but not hippocampus\n    (17/368, p = 0.90) and vmPFC (28/336, p = 0.05)\n  statistics:\n  - about: amygdala\n    test: permutation test, 2,000 shuffles\n    p: 0.002\n    n: 368 channels\n  - about: ACC\n    test: permutation test, 2,000 shuffles\n    p: 0.028\n    n: 368 channels\n  - about: preSMA\n    test: permutation test, 2,000 shuffles\n    p: 0.001\n    n: 368 channels\n  - about: hippocampus\n    test: permutation test, 2,000 shuffles\n    p: 0.9\n    n: 368 channels\n  - about: vmPFC\n    test: permutation test, 2,000 shuffles\n    p: 0.05\n    n: 336 channels\n  expected:\n  - quantity: amygdala selective LFP channels\n    value: 37\n    tolerance: 3.7\n  - quantity: ACC selective LFP channels\n    value: 33\n    tolerance: 3.3\n  - quantity: preSMA selective LFP channels\n    value: 40\n    tolerance: 4\n  - quantity: hippocampus selective LFP channels\n    value: 17\n    tolerance: 1.7\n  - quantity: vmPFC selective LFP channels\n    value: 28\n    tolerance: 2.8\n  - quantity: LFP channels analysed per area (amygdala, hippocampus, ACC, preSMA)\n    value: 368\n    tolerance: 0\n  - quantity: vmPFC LFP channels analysed\n    value: 336\n    tolerance: 0\n  criterion: >-\n    As examine_channels_recognitiontask.py on the micro channels. HFB by pipeline H on the\n    recognition block; mean HFB in 0.2 to 1.7 s after each trial's start_time; sessions by rule R\n    (open detail 5 readings shown); correct trials; selection by bootstrap B and area p by\n    permutation test P, areas AMY, HIP, ACC, SMA, OFC. Reproduced when amygdala, ACC and preSMA\n    have p < 0.05 and hippocampus and vmPFC have p >= 0.05 (the absence half judged on the\n    paper's test; the paper's vmPFC p of 0.05 sits at the threshold, so its p is reported with\n    its Monte Carlo error, open detail 8), with counts within tolerance; partially reproduced\n    when the significance pattern holds but a count is outside tolerance, or when only the\n    vmPFC decision differs.\n- id: memory-ieeg\n  statement: >-\n    For macroelectrode iEEG HFB power, significant proportions of channels were memory selective\n    in the ACC (41/368, p < 0.001), vmPFC (34/368, p = 0.012) and preSMA (45/368, p < 0.001), but\n    not in the amygdala (25/368, p = 0.47) or hippocampus (32/368, p = 0.067).\n  source: Technical Validation, Neuronal responses (recognition memory phase), paragraph 2\n  quote: >-\n    At the iEEG level (macro channels), significant proportion of channels in the ACC (41/368,\n    p < 0.001), vmPFC (34/368, p = 0.012), and preSMA (45/368, p < 0.001) but not the amygdala\n    (25/368, p = 0.47) and hippocampus (32/368, p = 0.067) were memory selective for HFB power\n  statistics:\n  - about: ACC\n    test: permutation test, 2,000 shuffles\n    p: 0.001\n    p_relation: \"<\"\n    n: 368 channels\n  - about: vmPFC\n    test: permutation test, 2,000 shuffles\n    p: 0.012\n    n: 368 channels\n  - about: preSMA\n    test: permutation test, 2,000 shuffles\n    p: 0.001\n    p_relation: \"<\"\n    n: 368 channels\n  - about: amygdala\n    test: permutation test, 2,000 shuffles\n    p: 0.47\n    n: 368 channels\n  - about: hippocampus\n    test: permutation test, 2,000 shuffles\n    p: 0.067\n    n: 368 channels\n  expected:\n  - quantity: ACC selective iEEG channels\n    value: 41\n    tolerance: 4.1\n  - quantity: vmPFC selective iEEG channels\n    value: 34\n    tolerance: 3.4\n  - quantity: preSMA selective iEEG channels\n    value: 45\n    tolerance: 4.5\n  - quantity: amygdala selective iEEG channels\n    value: 25\n    tolerance: 2.5\n  - quantity: hippocampus selective iEEG channels\n    value: 32\n    tolerance: 3.2\n  - quantity: iEEG channels analysed per area\n    value: 368\n    tolerance: 0\n  criterion: >-\n    As memory-lfp, on the macro channels (LFP_macro). Reproduced when ACC, vmPFC and preSMA have\n    p < 0.05 and amygdala and hippocampus have p >= 0.05 (absence on the paper's test), with\n    counts within tolerance; partially reproduced when the significance pattern holds but a count\n    is outside tolerance.\n- id: memory-modalities-differ\n  statement: >-\n    The areas with memory selectivity differ by modality; the ACC is selective in all three\n    (cells, LFP, iEEG), the hippocampus in none, and the amygdala in cells and LFP but not iEEG.\n  source: Technical Validation, Neuronal responses (recognition memory phase), paragraph 3\n  quote: >-\n    For example, the ACC showed memory selectivity in all three modalities, the hippocampus showed\n    selectivity in none of them, and the amygdala showed selectivity at the single-cell and LFP but\n    not iEEG level\n  depends_on:\n  - memory-cells-significant\n  - memory-cells-not-significant\n  - memory-lfp\n  - memory-ieeg\n  criterion: >-\n    Read from the area p-values of the four claims it depends on, at p < 0.05. Reproduced when\n    the ACC is significant in all three modalities, the hippocampus in none, and the amygdala in\n    cells and LFP but not iEEG.\n- id: fig6-examples\n  statement: >-\n    Example memory-selective units and channels; a preSMA neuron firing more to familiar images\n    (p = 0.003), an ACC neuron firing more to novel images (p < 0.001), and a preSMA macro channel\n    and an ACC microwire channel with higher HFB to novel images (both p < 0.001).\n  source: Fig. 6 legend\n  quote: >-\n    Significance of selection criteria (bootstrap test, novel versus familiar) was p = 0.003 ( a ),\n    p < 0.001( b ), p < 0.001 ( c ), p < 0.001 ( d )\n  statistics:\n  - about: Fig. 6a, preSMA neuron\n    test: bootstrap test\n    p: 0.003\n  - about: Fig. 6b, ACC neuron\n    test: bootstrap test\n    p: 0.001\n    p_relation: \"<\"\n  - about: Fig. 6c, preSMA macro channel\n    test: bootstrap test\n    p: 0.001\n    p_relation: \"<\"\n  - about: Fig. 6d, ACC micro channel\n    test: bootstrap test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - memory-cells-significant\n  - memory-lfp\n  - memory-ieeg\n  criterion: >-\n    The examples are the code's plot lists. Cells P53CS_R1_11_1_3077 and P58CS_R1_34_2_3239\n    (unit_id_session; the code does not say which is panel a, so each is matched to the panel\n    whose area and direction it shows), macro channel P42CS_R2_RSMA3 (6c) and micro channel\n    P58CS_R1_RACC2 (6d). Bootstrap B as in the memory claims. Reproduced when each has the\n    legend's area, the stated direction (familiar above novel for 6a, novel above familiar for\n    the others) and a p-value matching the legend (0.003 within 10%, the others below 0.001).\n- id: scenecut-labels\n  kind: link\n  statement: >-\n    The movie has 80 continuity cuts and 13 scene changes, and the annotation file's cuts can be\n    placed in each session through the frame times in the NWB files.\n  source: Methods, Movie annotations, paragraph 2; Usage Notes, paragraph 1\n  quote: The movie contained 80 continuity cuts and 13 scene changes\n  expected:\n  - quantity: continuity cuts\n    value: 80\n    tolerance: 0\n  - quantity: scene changes\n    value: 13\n    tolerance: 0\n  data: with_labels\n  criterion: >-\n    Labels from scenecut_info.csv in the code repository at commit 8c35290 (the paper's Figshare\n    annotations, doi:10.6084/m9.figshare.25037045.v4, are the other copy), classified by rule S.\n    Reproduced when the counts match and every cut's shot_start_fr has a movieframe_time entry in\n    every session, so that onsets fall inside the movie window.\n- id: event-cells\n  statement: >-\n    Significant proportions of cells were event selective (scene change against continuity cut) in\n    the vmPFC (10/175, p = 0.005) and preSMA (20/299, p < 0.001), but not in the amygdala (15/479,\n    p = 0.081), ACC (7/236, p = 0.224) or hippocampus (8/261, p = 0.199).\n  source: Technical Validation, Neuronal responses (movie watching phase), paragraph 1\n  quote: >-\n    Significant proportions of cells were event selective in the vmPFC (10/175, p = 0.005,\n    permutation test) and preSMA (20/299, p < 0.001) but not in the amygdala (15/479, p = 0.081),\n    ACC (7/236, p = 0.224), and hippocampus (8/261, p = 0.199\n  statistics:\n  - about: vmPFC\n    test: permutation test\n    p: 0.005\n    n: 175 cells\n  - about: preSMA\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: 299 cells\n  - about: amygdala\n    test: permutation test\n    p: 0.081\n    n: 479 cells\n  - about: ACC\n    test: permutation test\n    p: 0.224\n    n: 236 cells\n  - about: hippocampus\n    test: permutation test\n    p: 0.199\n    n: 261 cells\n  expected:\n  - quantity: vmPFC event-selective cells\n    value: 10\n    tolerance: 1\n  - quantity: preSMA event-selective cells\n    value: 20\n    tolerance: 2\n  - quantity: amygdala event-selective cells\n    value: 15\n    tolerance: 1.5\n  - quantity: ACC event-selective cells\n    value: 7\n    tolerance: 0.7\n  - quantity: hippocampus event-selective cells\n    value: 8\n    tolerance: 0.8\n  data: with_labels\n  depends_on:\n  - scenecut-labels\n  - neurons-total-and-areas\n  criterion: >-\n    As examine_neurons_scenecuts.py. All units of U in all 29 sessions; firing rate in 0 to 1.0 s\n    after each cut onset (rule S); selection by bootstrap B (scene change minus continuity cut,\n    unbalanced, counted when the difference is positive and p < 0.05); area p by permutation\n    test P with the same positive-difference rule. Open detail 6, the count in either direction\n    is shown as a variant. Reproduced when vmPFC and preSMA have p < 0.05 and amygdala, ACC and\n    hippocampus p >= 0.05 (absence on the paper's test), with counts within tolerance; partially\n    reproduced when the significance pattern holds but a count is outside tolerance.\n- id: event-lfp\n  statement: >-\n    For microwire LFP HFB power, significant proportions of channels were event selective in all\n    five areas; amygdala 20/448 (p = 0.005), hippocampus 40/448 (p < 0.001), ACC 33/448\n    (p < 0.001), vmPFC 15/400 (p = 0.015), preSMA 22/448 (p = 0.001).\n  source: Technical Validation, Neuronal responses (movie watching phase), paragraph 2\n  quote: >-\n    For the LFP, significant proportions of channels were event selective in the amygdala (20/448,\n    p = 0.005, permutation test), hippocampus (40/448, p < 0.001), ACC (33/448, p < 0.001), vmPFC\n    (15/400, p = 0.015), and preSMA (22/448, p = 0.001)\n  statistics:\n  - about: amygdala\n    test: permutation test\n    p: 0.005\n    n: 448 channels\n  - about: hippocampus\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: 448 channels\n  - about: ACC\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: 448 channels\n  - about: vmPFC\n    test: permutation test\n    p: 0.015\n    n: 400 channels\n  - about: preSMA\n    test: permutation test\n    p: 0.001\n    n: 448 channels\n  expected:\n  - quantity: amygdala event-selective LFP channels\n    value: 20\n    tolerance: 2\n  - quantity: hippocampus event-selective LFP channels\n    value: 40\n    tolerance: 4\n  - quantity: ACC event-selective LFP channels\n    value: 33\n    tolerance: 3.3\n  - quantity: vmPFC event-selective LFP channels\n    value: 15\n    tolerance: 1.5\n  - quantity: preSMA event-selective LFP channels\n    value: 22\n    tolerance: 2.2\n  - quantity: LFP channels analysed per area (amygdala, hippocampus, ACC, preSMA)\n    value: 448\n    tolerance: 0\n  - quantity: vmPFC LFP channels analysed\n    value: 400\n    tolerance: 0\n  data: with_labels\n  depends_on:\n  - scenecut-labels\n  criterion: >-\n    As examine_channels_scenecuts.py on the micro channels. HFB by pipeline H on the movie window;\n    mean HFB in 0 to 1.0 s after each cut onset (rule S); all sessions; bootstrap B and\n    permutation test P with the positive-difference rule (open detail 6, either direction shown\n    as a variant). Reproduced when all five areas have p < 0.05 with counts within tolerance;\n    partially reproduced when four of five have p < 0.05, or all five do but a count is outside\n    tolerance.\n- id: event-ieeg\n  statement: >-\n    For macroelectrode iEEG HFB power, significant proportions of channels were event selective in\n    all five areas; amygdala 67/448, hippocampus 41/448, ACC 25/448, vmPFC 33/449 (all\n    p < 0.001) and preSMA 21/448 (p = 0.002).\n  source: Technical Validation, Neuronal responses (movie watching phase), paragraph 2\n  quote: >-\n    At the iEEG level (macro channels), significant proportion of channels in the amygdala (67/448,\n    p < 0.001), hippocampus (41/448, p < 0.001), ACC (25/448, p < 0.001), vmPFC (33/449,\n    p < 0.001), and preSMA (21/448, p = 0.002) were event selective\n  statistics:\n  - about: amygdala\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: 448 channels\n  - about: hippocampus\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: 448 channels\n  - about: ACC\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: 448 channels\n  - about: vmPFC\n    test: permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: 449 channels\n  - about: preSMA\n    test: permutation test\n    p: 0.002\n    n: 448 channels\n  expected:\n  - quantity: amygdala event-selective iEEG channels\n    value: 67\n    tolerance: 6.7\n  - quantity: hippocampus event-selective iEEG channels\n    value: 41\n    tolerance: 4.1\n  - quantity: ACC event-selective iEEG channels\n    value: 25\n    tolerance: 2.5\n  - quantity: vmPFC event-selective iEEG channels\n    value: 33\n    tolerance: 3.3\n  - quantity: preSMA event-selective iEEG channels\n    value: 21\n    tolerance: 2.1\n  - quantity: iEEG channels analysed per area (amygdala, hippocampus, ACC, preSMA)\n    value: 448\n    tolerance: 0\n  - quantity: vmPFC iEEG channels analysed\n    value: 449\n    tolerance: 0\n  data: with_labels\n  depends_on:\n  - scenecut-labels\n  criterion: >-\n    As event-lfp, on the macro channels (LFP_macro). The vmPFC denominator of 449 is printed as\n    in the text and may be a misprint of 448; the count found is reported. Reproduced when all\n    five areas have p < 0.05 with counts within tolerance; partially reproduced when four of five\n    have p < 0.05, or all five do but a count is outside tolerance.\n- id: fig7-examples\n  statement: >-\n    Example event-selective units and channels; a preSMA neuron (p = 0.024) and a vmPFC neuron\n    (p = 0.030), a hippocampal macro channel (p = 0.026) and a preSMA microwire channel\n    (p < 0.001), each responding differently to scene changes than to continuity cuts.\n  source: Fig. 7 legend\n  quote: >-\n    Significance of selection criteria (bootstrap test, scene change versus continuity cut) was\n    p = 0.024 ( a ), p = 0.030 ( b ), p = 0.026 ( c ), p < 0.001 ( d )\n  statistics:\n  - about: Fig. 7a, preSMA neuron\n    test: bootstrap test\n    p: 0.024\n  - about: Fig. 7b, vmPFC neuron\n    test: bootstrap test\n    p: 0.03\n  - about: Fig. 7c, hippocampus macro channel\n    test: bootstrap test\n    p: 0.026\n  - about: Fig. 7d, preSMA micro channel\n    test: bootstrap test\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: Fig. 7a bootstrap p\n    value: 0.024\n    tolerance: 0.0024\n  - quantity: Fig. 7b bootstrap p\n    value: 0.030\n    tolerance: 0.003\n  - quantity: Fig. 7c bootstrap p\n    value: 0.026\n    tolerance: 0.0026\n  data: with_labels\n  depends_on:\n  - event-cells\n  - event-lfp\n  - event-ieeg\n  criterion: >-\n    The examples are the code's plot lists. Cells P42CS_R1_47_2_1347 and P47CS_R1_78_1_2233\n    (matched to panels a and b by area), macro channel P62CS_R2_RHIP6 (7c) and micro channel\n    P51CS_R2_RSMA8 (7d). Bootstrap B as in the event claims (seed 13). Reproduced when each has\n    the legend's area, scene change above continuity cut, and a p-value within tolerance (7d\n    below 0.001).\n- id: nwb-contents\n  statement: >-\n    Each NWB file holds spike times of all sorted neurons, LFP from all microwires and field\n    potentials from all macro contacts downsampled to 1000 Hz, behavior, electrode locations,\n    spike-sorting quality metrics and eye-tracking data; spike times are referenced to movie\n    start and the LFP starts 10 s before it.\n  source: Data Records, Electrophysiology; Usage Notes, paragraph 1\n  quote: >-\n    Each NWB file includes various types of data: (1) spike times of all sorted neurons; (2) the\n    LFP from all microwires, which were downsampled to 1000 Hz ... (3) the field potentials from\n    all iEEG macroelectrodes, similarly downsampled to 1000 Hz; (4) behavior; (5) electrode\n    locations; (6) spike sorting quality metrics; and (7) eye tracking data\n  criterion: >-\n    Checked in each of the 29 files. Reproduced when every file has units with spike times and\n    electrode ids; LFP_micro and LFP_macro electrical series at 1000 Hz (rate, or timestamps 1 ms\n    apart) whose first sample lies 10 s before movie start (Usage Notes); behavior in the trials\n    table; an electrodes table with locations; the per-unit metrics used above (isibelow, peakSNR,\n    meanSNR, isolationdist) and pairwise_distances; gaze in processing[\"behavior\"]; and\n    movieframe_time; and when the movie window starts at time 0 within 1 frame (40 ms). A file\n    lacking macro channels (the code allows for it) is reported, not counted against the claim.\n- id: scanner-questions\n  statement: >-\n    In the scanner, participants answered on average 5.97 +- 0.98 of seven questions on the movie\n    correctly (across participants and runs).\n  source: Methods, Task, paragraph 3\n  quote: >-\n    Participants answered on average 5.97 ± 0.98 (mean ± s.d., across participants and runs)\n    questions correctly\n  expected:\n  - quantity: mean correct answers\n    value: 5.97\n    tolerance: 0.597\n  - quantity: s.d. of correct answers\n    value: 0.98\n    tolerance: 0.098\n  data: elsewhere\n  where: >-\n    Figshare doi:10.6084/m9.figshare.25037045.v4 and the code repository's\n    assets/annotations/scanner_questionnaire.csv at commit 8c35290\n  criterion: Not tested on the dandiset.\n- id: fmri-motion\n  statement: >-\n    Participants moved little in the scanner; median framewise displacement 0.15 mm (per-participant\n    medians 0.09 to 0.38 mm), with a median of 1.8% of volumes (0.2% to 14.8%) marked as motion\n    outliers.\n  source: Technical Validation, Imaging data quality, paragraph 1; Fig. 4a\n  quote: >-\n    participants exhibited minimal motion, with a low median framewise displacement of 0.15 mm\n    (minimum median across participants was 0.09 mm, maximum was 0.38 mm, see Fig. 4a ), and a\n    small percentage of volumes (median = 1.8%; min 0.2%, max 14.8%) marked as motion outliers by\n    fMRIprep\n  expected:\n  - quantity: median framewise displacement\n    value: 0.15\n    tolerance: 0.015\n    unit: mm\n  - quantity: median percentage of motion-outlier volumes\n    value: 1.8\n    tolerance: 0.18\n    unit: \"%\"\n  data: elsewhere\n  where: OpenNeuro ds004798 (BIDS), after fMRIPrep 23.1.3 as the Methods describe\n  criterion: Not tested on the dandiset.\n- id: fmri-tsnr\n  statement: >-\n    The mean whole-brain tSNR across participants was 67.56 +- 8.29, higher in dorsal areas and\n    lower in anterior temporal, orbitofrontal and subcortical regions.\n  source: Technical Validation, Imaging data quality, paragraph 2; Fig. 4b,c\n  quote: >-\n    The mean whole-brain tSNR across participants was 67.56 ± 8.29, mean ± s.d., consistent with\n    previous datasets\n  expected:\n  - quantity: mean whole-brain tSNR\n    value: 67.56\n    tolerance: 6.756\n  - quantity: s.d. of whole-brain tSNR\n    value: 8.29\n    tolerance: 0.829\n  data: elsewhere\n  where: OpenNeuro ds004798 (BIDS), after fMRIPrep 23.1.3 as the Methods describe\n  criterion: Not tested on the dandiset.\n- id: fmri-isc\n  statement: >-\n    Inter-subject correlation of BOLD responses to the movie was high in visual and auditory\n    areas and elevated in social regions (precuneus, TPJ, MPFC).\n  source: Technical Validation, Imaging data quality, paragraph 3; Fig. 5\n  quote: >-\n    The ISC analysis confirmed that the stimulus elicited comparable brain responses among\n    participants, showing high ISC values in visual and auditory areas as expected for an\n    audio-visual movie stimulus\n  data: elsewhere\n  where: OpenNeuro ds004798 (BIDS), after fMRIPrep 23.1.3 as the Methods describe\n  criterion: Not tested on the dandiset.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000623/10.1038-s41597-024-03029-1.yaml paper/10.1038-s41597-024-03029-1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000623/10.1038-s41597-024-03029-1.yaml",
 "old_string": "  inferred: >-\n    The per-area counts are shown only in Fig. 2h; they are read from the denominators of the\n    scene-cut analysis, which included every unit (479 + 261 + 236 + 299 + 175 = 1450).\n  expected:\n  - quantity: units\n    value: 1450",
 "new_string": "  expected:\n  - quantity: units\n    value: 1450"
}
```

```
The file claims/000623/10.1038-s41597-024-03029-1.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000623/10.1038-s41597-024-03029-1.yaml",
 "old_string": "  criterion: >-\n    Units of set U (at least one spike in the movie window), as in gen_figure2ah_singleunitQC.py,",
 "new_string": "  criterion: >-\n    The per-area counts are shown only in Fig. 2h; they are taken from the denominators of the\n    scene-cut analysis (Neuronal responses (movie watching phase), paragraph 1), which included\n    every unit (479 + 261 + 236 + 299 + 175 = 1450).\n    Units of set U (at least one spike in the movie window), as in gen_figure2ah_singleunitQC.py,"
}
```

```
The file claims/000623/10.1038-s41597-024-03029-1.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000623/10.1038-s41597-024-03029-1.yaml paper/10.1038-s41597-024-03029-1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "—\|rather" claims/000623/*.yaml; python3 -c "
import yaml;d=yaml.safe_load(open('claims/000623/10.1038-s41597-024-03029-1.yaml'));c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('inferred' in x for x in c))"
```

```
31 30 11 31 1
```

**Agent**

I've written `claims/000623/10.1038-s41597-024-03029-1.yaml`. The quote checker passes with 0 problems. Nothing is committed.

**Text read.** The version of record (Sci Data 11, 214, open access), as Europe PMC serves it. It has the full main text, Methods, Data Records, Technical Validation, Usage Notes, Table 1 and the legends of Figures 1 to 7. The paper is a Data Descriptor and has no supplement. There was no PDF and I opened no figure.

**Code read.** github.com/rutishauserlab/bmovie-release-NWB-BIDS at commit 8c35290. The criteria take from it the unit and session selection, the bootstrap and permutation tests, the HFB (high-frequency broadband power) pipeline, the scene-cut labels, the gaze heatmaps, AUC and the confidence split. The code doesn't hold the run 1 against run 2 test, and it doesn't print the means and s.d. of the quality metrics.

**Claims.** 31 in all: 30 have quotes and 1 has an `inferred` note (Table 1 demographics). 11 have statistics (40 values), and all 31 have criteria.
- **Tested on the dandiset (25):** cohort and sessions, unit counts, spike-sorting quality metrics, eye tracking, recognition AUC, memory-selective cells, LFP and iEEG channels, event-selective cells and channels, the example units in Figs 6 and 7, and NWB contents. Of these, 6 use the code repository's scene-cut annotation file as labels, through a link claim.
- **Outside data (1):** Table 1 demographics, because the four fMRI-only participants' ages are in Table 1 and the code, not the dandiset.
- **Data elsewhere (4):** the fMRI motion, tSNR and inter-subject correlation results are on OpenNeuro ds004798. The in-scanner answers are on Figshare and in the code repository.

**Tolerances.** Counts of deposited records have tolerance 0, and everything else uses 10%. I didn't use the s.d. as a tolerance, because it describes the spread of units or sessions, not the uncertainty of a mean over a fixed deposited set.

**Details the paper leaves open, with the readings named:**
1. **Mean ISI below 3 ms:** over all units, or only the units under 3% that the code plots in Fig. 2c.
2. **s.d. degrees of freedom:** ddof 0 is used as a standard choice and ddof 1 is shown; it can't change an outcome at these sample sizes.
3. **Missing-gaze mean (7% ± 8%):** over the 27 sessions left after P53CS is excluded, or over all 29.
4. **Mean AUC (0.79 ± 0.19):** over the 29 sessions, or over the 16 participants after averaging their runs.
5. **Sessions in the memory analyses:** the code's rule (fewer than 10 correct trials per condition), or the five runs the text lists. The text's "behavioral AUC > 0.6" is read as AUC below 0.6, and the code applies no AUC rule.
6. **Direction of scene-cut selectivity:** the text says "differed significantly"; the code counts only scene change above continuity cut. The code's reading is followed and the either-direction count is a variant.
7. **Run 1 against run 2 AUC test:** not in the code, so it is set as a two-sided paired t-test on per-run AUC.
8. **Unseeded permutation test:** seed 0 is used as a standard choice and the Monte Carlo error is reported. This matters for the vmPFC LFP memory result, whose p of 0.05 sits at the threshold, so its criterion allows a partial result there.

**Missing from the paper.**
- The firing rate (2.47 ± 3.32) is printed without a unit; spikes/s is taken from the code's Fig. 2b axis.
- The per-area neuron counts appear only in Fig. 2h, so they are taken from the scene-cut denominators, which add up to 1450.
- The paper doesn't say which example neuron is Fig. 6a or 6b, or 7a or 7b; units are matched to panels by area and direction.
- The iEEG vmPFC denominator is printed as 449 where every other area is 448. It may be a misprint, and the claim reports the count found.
- No claim was blocked for lack of a method.

## End of run

34 turns, 6 minutes, result: success.
