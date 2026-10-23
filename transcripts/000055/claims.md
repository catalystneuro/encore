# 000055 · claims · run 39977828885

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/000055 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ paper/ claims/000055 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  for f in paper/*.txt; do echo "== $f"; head -15 $f; wc -w $f; done; cat claims/001453/*.yaml | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  head -12 paper/10.1523-eneuro.0007-21.2021.txt; wc -l paper/10.1523-eneuro.0007-21.2021.txt; grep -n "^=== \|^#\|github\|Figure [0-9]\b" paper/10.1523-eneuro.0007-21.2021.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -lw paper/10.1523-eneuro.0007-21.2021.txt; fold -s -w 250 paper/10.1523-eneuro.0007-21.2021.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt"
}
```

```
1	DOI: 10.1523/eneuro.0007-21.2021
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	2821 eneuro eNeuro eNeuro Society for Neuroscience PMC8225404 8225404 8225404 34031100 10.1523/ENEURO.0007-21.2021 Behavioral and Neural Variability of Naturalistic Arm Movements Peterson Steven M 1 2 ✉ Singh Satpreet H 3 Wang Nancy X R 4 5 Rao 
8	Rajesh P N 3 5 6 Brunton Bingni W 1 2 1 Department of Biology, University of Washington, Seattle, Washington 98195 2 eScience Institute, University of Washington, Seattle, Washington 98195 3 Department of Electrical & Computer Engineering, 
9	University of Washington, Seattle, Washington 98195 4 IBM Research, San Jose, California 95120 5 Paul G. Allen School of Computer Science and Engineering, University of Washington, Seattle, Washington 98195 6 Center for Neurotechnology, University 
10	of Washington, Seattle, Washington 98195 The authors declare no competing financial interests. Author contributions: N.X.R.W., R.P.N.R., and B.W.B. designed research; S.M.P. and S.H.S. performed research; S.M.P. and S.H.S. contributed unpublished 
11	reagents/analytic tools; S.M.P., S.H.S., R.P.N.R., and B.W.B. analyzed data; S.M.P. and B.W.B. wrote the paper. This research was supported by Defense Advanced Research Projects Agency Grant FA8750-18-2-0259, National Science Foundation Grants 
12	1630178 and EEC-1028725, the Sloan Foundation, the Washington Research Foundation, and the Weill Neurohub. * S.M.P. and S.H.S. contributed equally to this work. ✉ Correspondence should be addressed to Steven M. Peterson at [removed: an e-mail address] . ✉ 
13	Corresponding author. 19 6 2021 8 3 ENEURO.0007-21.2021 ENEURO.0007-21.2021 25 6 2021 Copyright © 2021 Peterson et al. This is an open-access article distributed under the terms of the Creative Commons Attribution 4.0 International license , which 
14	permits unrestri
[... 180 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 195,
 "limit": 120
}
```

```
195	plots of the seven other regions of interest, see Extended Data Figures 4-1 , 4-2 , 4-3 , 4-4 , 4-5 , 4-6 , 4-7 . In addition to intersubject neural variability, we also identified notable changes in movement-related neural activity across recording 
196	days for several subjects ( Fig. 5 ). We analyzed spectral power in the precentral region averaged over the 0.5 s following movement onset and split into LFBs (8–32 Hz) and HFBs (76–100 Hz) bands, similar to previous research ( Miller et al., 2007 
197	). Statistical significance for each subject was computed by pooling over all electrodes for that subject (Extended Data Fig. 1-1 ). For both frequency bands, spectral power significantly differed across subjects ( p < 0.001 for both bands, one-way 
198	Kruskal–Wallis test). For further statistical details, see Table 1 . We also found a significant effect of recording day in LFBs for subjects 03 ( p < 0.001, Kruskal–Wallis test), 05 ( p = 0.013), 06 ( p < 0.001), 07 ( p = 0.041), 08 ( p = 0.013), 
199	and 11 ( p < 0.001), as well as in HFBs for subjects 03 ( p = 0.002), 04 ( p < 0.001), 07 ( p < 0.001), 08 ( p = 0.004), and 10 ( p = 0.006). For further statistical details, see Table 2 . Surprisingly, these significant recording day effects appear 
200	for several subjects despite baseline-subtracting spectral power features. Yet, baseline subtraction does substantially reduce neural variability across recording days (Extended Data Fig. 5-1 ), as expected. Figure 5. Precentral banded spectral 
201	power varies considerably across subjects and recording days. a , b , LFB (8–32 Hz; a ) and HFB (76–100 Hz; b ) spectral power in the precentral region was averaged over the first 0.5 s after movement onset. Boxplots show spectral power variability 
202	across events for every subject, separated by recording day. For each subject, a significant recording day effect on spectral power is denoted by an asterisk ( p < 0.05, Kruskal–Wallis test). Despite the reduction in neura
[... 112 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 315,
 "limit": 90
}
```

```
315	human behavior, these movements are still unconstrained, unstructured, and spontaneous. Therefore, we feel that “naturalistic” most appropriately describes these types of movements and would like to keep this wording in our title. Reviewer 2 The 
316	manuscript addresses the considerable challenge of explaining the neural basis of movement by analyzing ECoG recordings during naturalistic movement performance. Unlike most common experiments where the results are performed in the controlled 
317	conditions of numerous repetitions of the same movement under the same precise conditions, here the authors carried out a series of experiments aimed at recording and analyzing thousands of natural arm movements, together with ECoG recordings from 
318	epilepsy patients. I believe that the manuscript addresses two of the major problems of the study of motor control: the lack of natural conditions and the necessity of providing movement correlates in humans. Towards this end, the authors perform a 
319	careful study addressing two of the hard points in these kinds of problems: identifying relevant features both of behavior and of neural data. One of the major challenges of analyzing unconstrained movements is their intrinsic variability. 
320	Amplitudes, orientations and targets are not defined, which turns movement characterization into a formidable task. The authors characterized thousands of spontaneous movements enabling scalable analysis of video that was acquired simultaneously 
321	with the intracranial recordings. We characterized the variability of both naturalistic upper-limb reaching movements and the corresponding changes in cortical spectral power. Their hypothesis is that naturalistic reaches would be associated with 
322	transient low- frequency power decreases and high-frequency power increases, localized from fronto- parietal sources. They also assessed the variability of these event-related spectral power fluctuations and performed regression to partially 
[... 82 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "000055",
 "path": "
 "glob": "!paper/**",
 "output_mode": "content",
 "head_limit": 20
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 210,240p papers/manifest.yaml; sed -n 735,790p targets/dandisets.json
```

```
supplements: 3
  '000054':
  - doi: 10.1038/s41593-021-00816-6
    status: stored
    version: as served by ncbi_pmc
    source: ncbi_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 1
  '000055':
  - doi: 10.1523/eneuro.0007-21.2021
    status: stored
    version: as served by europe_pmc
    source: europe_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 0
  - doi: 10.1016/j.jneumeth.2021.109199
    status: stored
    version: version of record
    source: PDF supplied by a person
    pdf: true
[... 67 more lines not kept]
```

**Agent**

Full text of the eNeuro paper is present (Europe PMC version; the Extended Data figures exist only as EPS links, not in the text). Now reading the linked code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/BruntonUWBio/naturalistic_arm_movements_ecog code 2>&1 | tail -3; cd code && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | head -50
```

```
04c6faf2f219586fa834d10c614ef48a694cec55 2021-03-17 09:23:58 -0700
./upload_figshare.py
./project_data_rois_matlab/set_environment_paths.m
./project_data_rois_matlab/project_ecog_to_rois.m
./compute_power_gen_figs_python/tfr_utils.py
./compute_power_gen_figs_python/regression_utils.py
./compute_power_gen_figs_python/fit_regression_models.py
./compute_power_gen_figs_python/feat_plot_utils.py
./compute_power_gen_figs_python/config.py
./compute_power_gen_figs_python/compute_spectral_power.py
./compute_power_gen_figs_python/archived_code/Regression_results_Figs7_8.ipynb
./compute_power_gen_figs_python/archived_code/Plot_movement_variability_Fig2.ipynb
./compute_power_gen_figs_python/archived_code/Comparison_reaches_handclench_Fig5.ipynb
./compute_power_gen_figs_python/archived_code/.ipynb_checkpoints/Regression_results_Figs7_8-checkpoint.ipynb
./compute_power_gen_figs_python/archived_code/.ipynb_checkpoints/Plot_movement_variability_Fig2-checkpoint.ipynb
./compute_power_gen_figs_python/archived_code/.ipynb_checkpoints/Comparison_reaches_handclench_Fig5-checkpoint.ipynb
./compute_power_gen_figs_python/__pycache__/tfr_utils.cpython-36.pyc
./compute_power_gen_figs_python/__pycache__/regression_utils.cpython-36.pyc
./compute_power_gen_figs_python/__pycache__/feat_plot_utils.cpython-36.pyc
./compute_power_gen_figs_python/__pycache__/config.cpython-36.pyc
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat README.md; cat compute_power_gen_figs_python/config.py; wc -l compute_power_gen_figs_python/*.py
```

```
# Behavioral and neural variability of naturalistic arm movements

This repository contains scripts used to analyze the behavioral and neural variability of 12 human subjects as they performed spontaneous arm movements across multiple days. Neural data was monitored intracranially using electrocorticography (ECoG); wrist trajectories extracted from simultaneously recorded video was used to generate behavioral data. This repository is meant to be used with our [published dataset](https://figshare.com/projects/Behavioral_and_neural_variability_of_naturalistic_arm_movements/78666) to replicate our analysis and generate most of the figures from our [preprint](https://doi.org/10.1101/2020.04.17.047357). Such analyses include ECoG spectral power computation and projection to pre-defined regions of interest, comparison of naturalistic reach data to cued hand clench data, and regression of spectral power on behavioral and environmental features.

## Getting started

This code was primarily run using Python 3.6.8, with one optional part requiring Matlab 2018b. Note that Matlab and Python code are separated into separate folders. Analysis is heavily reliant on [MNE](https://mne.tools/stable/index.html) for data analysis and saving. Some specific package versions used:

-  Python: Matplotlib 3.0.2, MNE 0.19.0, Nilearn 0.5.0, Numpy 1.15.4, Pandas 0.25.3

-  Matlab: EEGLAB 13.5.4b, Measure Projection Toolbox 1.661

## Analysis steps

All Python scripts can be found in *compute_power_gen_figs_python*. This folder includes Jupyter notebooks to generate plots, scripts to perform longer analyses such as computing spectral power and fitting regression models, and utility scripts. There is also a config file that contains many parameters that may be shared by multiple scripts or do not need to be changed.

### Step 1: Computing spectral power (*compute_spectral_power.py*)

This script will compute spectral power via Morlet wavelet transform for ECoG segments aligned to movement onset 
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/compute_power_gen_figs_python; cat compute_spectral_power.py fit_regression_models.py; cat regression_utils.py
```

```
<persisted-output>
Output too large (35.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5ff93f43-1501-470e-9e5d-93960d399ca7/tool-results/bqhbnbt84.txt

Preview (first 2KB):
import os, mne, sys, pdb, argparse, h5py, glob, natsort
os.environ["OMP_NUM_THREADS"] = "1" #avoid multithreading if have Anaconda numpy
import numpy as np
import pandas as pd
from datetime import datetime as dt
import scipy.io as sio

#Import custom scripts
import config
from tfr_utils import compute_tfr,tfr_subtract_baseline,tfr_boot_sig_mask,str2bool

#Set parameters
def main(ecog_lp,savefolder,averagePower,stat_method): 
    '''
    Use MNE to compute spectrograms from ECoG trials (with false positive trials removed, if desired).
    '''
[... 35 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/5ff93f43-1501-470e-9e5d-93960d399ca7/tool-results/bqhbnbt84.txt"
}
```

```
1	import os, mne, sys, pdb, argparse, h5py, glob, natsort
2	os.environ["OMP_NUM_THREADS"] = "1" #avoid multithreading if have Anaconda numpy
3	import numpy as np
4	import pandas as pd
5	from datetime import datetime as dt
6	import scipy.io as sio
7	
8	#Import custom scripts
9	import config
10	from tfr_utils import compute_tfr,tfr_subtract_baseline,tfr_boot_sig_mask,str2bool
11	
12	#Set parameters
13	def main(ecog_lp,savefolder,averagePower,stat_method): 
14	    '''
15	    Use MNE to compute spectrograms from ECoG trials (with false positive trials removed, if desired).
16	    '''
17	    
18	    #Load parameters
19	    alpha = config.constants_compute_tfr['alpha']
20	    n_perms = config.constants_compute_tfr['n_perms']
[... 740 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/compute_power_gen_figs_python; grep -n "def \|morlet\|n_cycles\|log\|median\|bootstrap\|multipletests\|percentile" tfr_utils.py | head -80
```

```
5:from mne.time_frequency import tfr_morlet
8:from scipy.stats import percentileofscore
25:def compute_tfr(epochsAllMove,epoch_times,freqs = np.arange(6, 123, 3),crop_val=0.5,decim=30):
27:    n_cycles = freqs / 4.  # different number of cycle per frequency
31:    power = tfr_morlet(epochsAllMove, freqs=freqs, n_cycles=n_cycles, use_fft=False,
35:    power.data = 10*np.log10(power.data) #convert to log scale
39:def tfr_subtract_baseline(power,chan_ind,baseidx,compute_mean=False):
49:            baseline = np.median(input_power[:,baseidx,:],axis=1)
56:            baseline = np.median(input_power[:,baseidx],axis=1)
60:def tfr_boot_sig_mask(curr_power,baseidx,n_perms=2000,alpha=0.05,method='fdr_bh',averagePower=True,useMedian=True):
67:            curr_power_ave = np.median(curr_power,axis=2)
71:        #Create bootstrap distribution (based on EEGLAB's bootstat function)
87:            #Take median across trials
88:            boot_dist[:,:,n] = np.median(curr_power_tmp,2)
98:                percentile_temp = percentileofscore(boot_dist[:,j],curr_power_ave[j,k])/100
99:                if percentile_temp>0.5:
100:                    p_raw[j,k] = 2*(1-percentile_temp)
102:                    p_raw[j,k] = 2*(percentile_temp)
106:            rej, pval_corr = smm.multipletests(p_raw.flatten(), alpha=alpha, method=method)[:2]
117:                curr_power = np.median(curr_power,axis=2) 
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/compute_power_gen_figs_python; for nb in Behavioral_features_Fig2 Plot_banded_power_Fig5 Projected_spectral_power_Figs3_4 Regression_results_Fig6; do echo "=== $nb"; python3 -c "
import json,sys
nb=json.load(open('$nb.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        print('--- cell',i); print(''.join(c['source']))
    else:
        print('--- md',i); print(''.join(c['source']))
" > $TMPDIR/$nb.txt; wc -l $TMPDIR/$nb.txt; done
```

```
=== Behavioral_features_Fig2
52 /tmp/claude-1001/Behavioral_features_Fig2.txt
=== Plot_banded_power_Fig5
187 /tmp/claude-1001/Plot_banded_power_Fig5.txt
=== Projected_spectral_power_Figs3_4
73 /tmp/claude-1001/Projected_spectral_power_Figs3_4.txt
=== Regression_results_Fig6
213 /tmp/claude-1001/Regression_results_Fig6.txt
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat Behavioral_features_Fig2.txt Plot_banded_power_Fig5.txt
```

```
--- md 0
# Large inter-subject variability in extracted behavioral features
--- md 1
Takes in 10 behavioral and environmental metadata measures and plots their distributions for every subject. This will generate Fig. 2 from the paper.
--- cell 2
%matplotlib inline
import glob, natsort, mne, sys, pdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import seaborn as sns
from mne.time_frequency import read_tfrs
import config
from feat_plot_utils import update_behavioral_features,feat_plot_unit_conversions,feat_plot,plot_feature_scattermatrix
--- md 3
### Set parameters
--- cell 4
tfr_lp = '.../naturalistic_reaches/tfr/'
n_subjs = 12
[... 219 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/compute_power_gen_figs_python; sed -n 20,205p tfr_utils.py; sed -n 280,330p tfr_utils.py; sed -n 650,700p tfr_utils.py
```

```
'''
Utility functions for computing and plotting spectral power.
'''

def compute_tfr(epochsAllMove,epoch_times,freqs = np.arange(6, 123, 3),crop_val=0.5,decim=30):
    #Time-frequency analysis (from https://plot.ly/ipython-notebooks/mne-tutorial/ -> Time-frequency analysis)
    n_cycles = freqs / 4.  # different number of cycle per frequency

    #Compute power for move trials
    print('Computing power...')
    power = tfr_morlet(epochsAllMove, freqs=freqs, n_cycles=n_cycles, use_fft=False,
                       return_itc=False, decim=decim, n_jobs=1,average=False)
    print('Power computation complete!')
    power.crop(epoch_times[0]+crop_val, epoch_times[1]-crop_val) #trim epoch to avoid edge effects
    power.data = 10*np.log10(power.data) #convert to log scale
    power.data[np.isinf(power.data)]=0 #set infinite values to 0
    return power

def tfr_subtract_baseline(power,chan_ind,baseidx,compute_mean=False):
    """
[... 268 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat Projected_spectral_power_Figs3_4.txt; cat Regression_results_Fig6.txt
```

```
--- md 0
# Plot cortical spectral power at regions of interest
--- md 1
The spectral power in the TFR files is calculated across electrodes, whose locations vary by subject. To look at average activity across subjects, we project electrode-level power onto common regions of interest. The weighting matrices needed for this are computed in project_data_rois_matlab directory. This notebook will generate Figs. 3 and 4 from the paper.
--- cell 2
%matplotlib notebook
import os,mne,glob,natsort
os.environ["OMP_NUM_THREADS"] = "1" #avoid multithreading if have Anaconda numpy
import numpy as np
import pandas as pd
from tqdm import tqdm_notebook as tqdm #useful for seeing progress
from matplotlib import gridspec
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import config
from tfr_utils import load_project_spectral_power,plot_specs_group,plot_specs_single_region
--- md 3
### Set parameters
--- cell 4
[... 266 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; grep -rn "kruskal\|bootstrap\|pearson\|corr(" --include=*.py --include=*.ipynb . | grep -v checkpoint | grep -v archived | head; sed -n 1,80p compute_power_gen_figs_python/feat_plot_utils.py
```

```
./compute_power_gen_figs_python/tfr_utils.py:71:        #Create bootstrap distribution (based on EEGLAB's bootstat function)
./compute_power_gen_figs_python/feat_plot_utils.py:224:    corr = df_scm.corr().values
./compute_power_gen_figs_python/Plot_banded_power_Fig5.ipynb:313:    "    stats = pg.kruskal(data=df_pat_sbj.loc[df_pat_sbj['Frequencies']==freq_dict[i]],\n",
./compute_power_gen_figs_python/Plot_banded_power_Fig5.ipynb:322:    "        stats = pg.kruskal(data=df_freq_band.loc[df_freq_band['Subjects']==curr_sbj],\n",
./compute_power_gen_figs_python/Plot_banded_power_Fig5.ipynb:446:    "    stats = pg.kruskal(data=df_pat_sbj.loc[df_pat_sbj['Frequencies']==freq_dict[i]],\n",
./compute_power_gen_figs_python/Plot_banded_power_Fig5.ipynb:457:    "        stats = pg.kruskal(data=df_freq_band.loc[df_freq_band['Subjects']==curr_sbj],\n",
import os,pdb
os.environ["OMP_NUM_THREADS"] = "1" #avoid multithreading if have Anaconda numpy
import numpy as np
import pandas as pd
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
import config
from pandas.plotting import scatter_matrix
import matplotlib.patches as patches
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import gridspec

def update_behavioral_features(df_metadata):
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; sed -n 200,240p compute_power_gen_figs_python/feat_plot_utils.py
```

```
def plot_feature_scattermatrix(df_metadata_plot):
    '''
    Plots scatter matrix of behavioral/environmental features to match supplemental figure.
    '''
    df_scm = df_metadata_plot.copy()
    df_scm = df_scm.iloc[:,:-1]

    #Change column names
    titles_dict = {'day':'Recording\nday','tod':'Time of\nday','run_1':'Reach\nduration',
                   'reach_r':'Reach\nmagnitude','reach_a':'Reach\nangle',
                   'onset_velocity':'Onset\nspeed','audio_ratio':'Audio\nratio',
                   'C_over_I_ratio':'Bimanual\nratio','other_lag_overlap':'Bimanual\noverlap',
                   'bimanual':'Bimanual\nclass','I_over_C_ratio':'Bimanual\nratio',
                   'other_reach_overlap':'Bimanual\noverlap',
                   'reach_duration':'Reach\nduration'
                  }
    df_cols = df_scm.columns
    df_cols2 = [titles_dict[val] for val in df_cols]
    df_scm.columns = df_cols2

[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,400p claims/001453/*.yaml; sed -n 1,80p tools/claims_check.py
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
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json | head -200; ls claims | head; ls claims/*/ | head -30
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
[... 219 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,320p schemas/claims.schema.json
```

```
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
          "date": {
            "type": "string",
            "format": "date"
          },
          "kind": {
            "enum": [
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/000447 claims/000404; head -60 claims/000447/*.yaml
```

```
claims/000404:
10.1016-j.cub.2023.06.027.yaml

claims/000447:
10.1016-j.celrep.2023.112246.yaml
# Claims for Tang, Shin & Jadhav (2023), Cell Reports 42, 112246, on dandiset 000447.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read. The NIH author manuscript in PubMed Central (PMC10124109, NIHMS1887302) as served by
# Europe PMC, with its STAR Methods and figure legends, and the supplement
# (NIHMS1887302-supplement-1.pdf, Figures S1 to S7 and their legends), all from
# paper/10.1016-j.celrep.2023.112246.txt. The version of record was not read. The PDF of the
# supplement was not opened; its text was enough. One value of the Methods is garbled in the
# text. The 1D Gaussian that smooths the linearized rate maps reads "(s = σ cm" with the
# number lost (Methods, Spatial fields and linearization). Criteria that use it name it as open.
#
# Code read. github.com/JadhavLab/GeometricTransformation at commit
# 5e55e69f2f089adcfd65bbfae42ec80e60e9903d (16 March 2023), MATLAB. It holds the scripts behind
# Figures 1 to 4 and S3, S5, S6, S7C-D. They are the behavioural summary, PV similarity, Bayesian
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o -i ".\{200\}\(speech ratio\|audio_ratio\|reach_a\|figshare\|events table\|metadata\).\{200\}" paper/10.1038-s41597-022-01280-y.txt | head -12
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/code; sed -n 80,200p compute_power_gen_figs_python/feat_plot_utils.py; grep -n "fwhm\|FWHM\|gauss\|Gauss\|dipole\|density\|aal" -i project_data_rois_matlab/project_ecog_to_rois.m | head -30
```

```
ax[s] = fig.add_subplot(gs[s, p])
            if (feat=='day'):
                bar_width = .6
                bins_use = []
                for k in [3,4,5,6,7]:
                    bins_use.append(k-bar_width/2)
                    bins_use.append(k+bar_width/2)
                sns.distplot(df_metadata_plot.loc[df_metadata_plot['patient_id']==patient,feat],
                             bins=np.asarray(bins_use), kde=False,color=colors_out[s],ax=ax[s],norm_hist=normalize_dists,hist_kws=dict(alpha=1))
                ax[s].set_xlabel('')
                ax[s].axhline(0,color=colors_out[s])
            elif (feat=='bimanual'):
                bar_width = .35
                bins_use = []
                for k in range(2):
                    bins_use.append(k-bar_width/2)
                    bins_use.append(k+bar_width/2)
                sns.distplot(df_metadata_plot.loc[df_metadata_plot['patient_id']==patient,feat],
                             bins=np.asarray(bins_use), kde=False,color=colors_out[s],ax=ax[s],norm_hist=normalize_dists,hist_kws=dict(alpha=1))
                ax[s].set_xlabel('')
[... 131 more lines not kept]
```

**Agent**

I have the paper's methods and the code (commit 04c6faf). Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000055/10.1523-eneuro.0007-21.2021.yaml",
 "content": "# Claims for Peterson, Singh, Wang, Rao & Brunton (2021), eNeuro 8(3), ENEURO.0007-21.2021,\n# \"Behavioral and Neural Variability of Naturalistic Arm Movements\", on dandiset 000055.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read. The version of record as served by Europe PMC (PMC8225404), from\n# paper/10.1523-eneuro.0007-21.2021.txt: main text, Materials and Methods, figure legends,\n# Tables 1 and 2, the legends of the Extended Data figures, and the review history. No PDF was\n# supplied. The Extended Data figures (1-1, 2-1 to 2-4, 3-1, 4-1 to 4-7, 5-1, 6-1, 6-2) are\n# EPS downloads and are not in the text; only their legends are. Claims that rest on them are\n# taken from their legends and from the Results sentences that cite them. The per-subject\n# electrode table (Extended Data Figure 1-1) and the per-subject feature confidence intervals\n# (Extended Data Figures 2-3 and 2-4) could not be read.\n#\n# Code read. github.com/BruntonUWBio/naturalistic_arm_movements_ecog at commit\n# 04c6faf2f219586fa834d10c614ef48a694cec55 (17 March 2021), Python 3.6 (MNE 0.19) and MATLAB.\n# It holds compute_spectral_power.py and tfr_utils.py (Morlet power, baseline, bootstrap\n# masking, projection to regions), the MATLAB projection of electrodes onto AAL regions\n# (project_ecog_to_rois.m, EEGLAB 13.5.4b, Measure Projection Toolbox 1.661),\n# fit_regression_models.py and regression_utils.py (regression), and notebooks for Figures 2,\n# 3 and 4, 5 and 6. It does not hold the ECoG preprocessing, the pose estimation, the event\n# detection, the behavioural feature extraction, the Kruskal-Wallis tests of Figure 2, the\n# bootstrap confidence intervals of Tables 1 and 2, or the code of Extended Data Figures 5-1\n# and 6-2. It starts from the curated epochs and spectral power deposited on Figshare.\n#\n# Spectral method fixed here (Methods, with the code where the Methods are silent). Segments\n# of 10 s centred on each movement onset; segments with power below 0 dB or with power at\n# 115-125 Hz more than 3 SD above all segments are dropped (Methods), and so are events marked\n# false positive (code). Morlet wavelet power at 1 to 121 Hz in 5 Hz steps (1, 6, ..., 121) with\n# n_cycles = frequency/4, decimated by 50 (10 Hz time bins at 500 Hz), converted to\n# 10*log10 (code). Each event's power has its own mean over -1.5 to -1 s subtracted, per\n# electrode and frequency (Methods give the window; code takes the mean). Projection onto\n# regions (Methods and code): electrodes in MNI space, right-hemisphere ones mirrored to the\n# left; a 3D Gaussian of 20 mm FWHM, truncated at 10 SD, at each electrode, summed over AAL\n# regions; regions kept when the electrode density averaged over the 12 subjects exceeds 3\n# (the eight regions middle frontal, precentral, postcentral, inferior parietal,\n# supramarginal, superior temporal, middle temporal, inferior temporal); bad electrodes get\n# weight 0 and each region's weights are renormalised to sum to 1 per subject (code); region\n# power is the weighted sum of electrode power. Banded power (Methods and Figure 5 legend) is\n# power over the first 0.5 s after onset (0 to 0.5 s) in the LFB 8-32 Hz (bins 11 to 31 Hz) and\n# HFB 76-100 Hz (bins 76 to 96 Hz). The Methods say this power is \"averaged\"; the code takes the\n# median over time bins and then over frequency bins. The mean is the main result, the code's\n# median a variant shown beside it.\n#\n# Regression method fixed here (Methods, with the code where the Methods are silent). One model\n# per subject, good electrode and band (LFB, HFB), over all of the subject's analysed events.\n# Ten features. Day of recording is one-hot by day; time of day is one-hot in three bins (0-8,\n# 8-16, 16-24 h). Reach duration, reach magnitude, reach angle, onset speed, speech ratio,\n# bimanual ratio, bimanual overlap and bimanual class are standardised (z-score over the\n# subject's events). Reach duration and reach magnitude are log transformed (Methods); the code\n# uses log(duration), log(magnitude + 1) and also log(onset speed + 1), shown as a variant.\n# Reach angle is folded to -90 (down) to +90 degrees (up) (Methods; code negates the image angle\n# and folds 90-270 degrees). Missing bimanual ratios are set to 0.5 and bimanual class is 1 when\n# the ipsilateral lead/lag value exists (code). Forward selection by OLS adjusted R2 (code\n# _forward_selected_new, run on all of the subject's events, as the code does where the\n# Methods do not say); unselected features are set to 0. Huber-loss linear regression\n# (sklearn HuberRegressor defaults, code). 200 random train/test splits per subject with days\n# balanced in the test set (equal numbers of test events from each day). The Methods give 90%\n# training and 10% test; the code uses 80/20 (train_test_split_day_balance, per_train=.8). The\n# Methods' 90/10 is the main result and the code's 80/20 a variant. Full-model R2 is the\n# coefficient of determination on the test events, averaged over splits. The Delta R2 of a\n# feature is the full-model test R2 minus the test R2 of a model refit with that feature\n# shuffled (all day columns shuffled together, and all time-of-day columns together, code),\n# averaged over splits. Features dropped by forward selection get Delta R2 0 (code). The\n# Methods score the shuffled model on the unshuffled withheld data, and the Results say the\n# training labels were shuffled. The code shuffles the column in training and test events and\n# scores on the shuffled test events. The Methods' version is the main result, the code's a\n# variant. Coefficients are averaged over splits. Recording day and time of day are\n# summarised by the SD of their one-hot coefficients (Figure 6 legend, code). Figure 6b-d\n# show only models with withheld R2 > 0.05 (legend), judged per band; the code selects\n# electrodes for both bands by the LFB R2, shown as a variant.\n#\n# Data the paper used. 12 subjects (8 male, 4 female, 29.4 +- 7.9 years) in clinical epilepsy\n# monitoring at the University of Washington, with ECoG grids over motor cortex (87.0 +- 12.9\n# surface electrodes; 5 subjects also had 23.2 +- 12.1 depth electrodes), seven implanted in the\n# left and five in the right hemisphere. Days 3 to 7 after implantation, 3 to 5 days per subject\n# (days per subject are listed in Table 2; 55 subject-days in all). ECoG at 1000 Hz, preprocessed\n# (median removed, high-amplitude artifacts zeroed with 2 s margins, 1-200 Hz bandpass, 60 Hz\n# notches, resampled to 500 Hz, common median reference per electrode group, bad electrodes by\n# SD or kurtosis) and video at 30 fps. Measured variables are the pose (DeepLabCut, nine key\n# points), contralateral wrist movement onset events (151 to 947 per subject, median 640), ten\n# behavioural and environmental features per event (day of recording, time of day, reach\n# duration, magnitude, angle, onset speed, speech ratio from the audio, bimanual ratio, overlap\n# and class), electrode MNI positions and bad-electrode labels. The paper deposited its curated\n# epochs, spectral power, event features and projection matrices on Figshare\n# (figshare.com/projects/Behavioral_and_neural_variability_of_naturalistic_arm_movements/78666).\n# The dandiset (AJILE12) describes ECoG at 500 Hz and pose for the same 12 participants over 55\n# days, with the wrist movement events and their features. Outside data the paper uses: the AAL\n# atlas (Tzourio-Mazoyer et al., 2002) through the Measure Projection Toolbox, for every claim on\n# regions of interest. The Figshare projection matrices (roi_proj_matlab/aal_XX_elecs2ROI.csv)\n# are the paper's own output of that step.\n#\n# Subjects S01 to S12 are assumed to be the dataset's subjects 01 to 12 in order; claim\n# subject-days checks this.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000055\"\npaper: doi:10.1523/eneuro.0007-21.2021\nclaims:\n- id: subject-days\n  kind: link\n  statement: The dataset's subjects and recording days are the paper's subjects S01 to S12 and\n    the recording days the paper lists for each.\n  source: Table 2; Methods, Data collection\n  criterion: The days per subject in Table 2 are S01 days 3, 4, 5 and 7; S02 and S03 days 3 to\n    6; S05 days 3, 4 and 7; S04 and S06 to S12 days 3 to 7 (55 subject-days). The link holds\n    (reproduced) when the dataset's subjects 01 to 12 have exactly these days in order. When it\n    does not, the subjects are matched by their day sets where these are unique, and the\n    mapping and any mismatch are reported; subjects whose day sets are identical cannot be told\n    apart this way, so the event counts per subject (claim fig2-event-counts) are reported\n    beside them.\n- id: cohort\n  statement: Twelve subjects (8 male, 4 female, 29.4 +- 7.9 years) had on average 87.0 +- 12.9\n    surface electrodes; five also had 23.2 +- 12.1 depth electrodes; five were implanted in the\n    right hemisphere and seven in the left.\n  source: Methods, Subject information, paragraph 1\n  quote: We analyzed opportunistic clinical recordings from 12 subjects (8 males, 4 females)\n    during their clinical epilepsy monitoring. Subjects were (mean ± SD) 29.4 ± 7.9 years old ...\n    resulting in 87.0 ± 12.9 total surface electrodes per subject (mean ± SD). In addition, five\n    subjects had 23.2 ± 12.1 intracortical depth electrodes (mean ± SD). Electrodes were\n    implanted primarily within one hemisphere for each subject (five right hemisphere, seven\n    left hemisphere)\n  expected:\n  - quantity: subjects\n    value: 12\n    tolerance: 0\n  - quantity: male subjects\n    value: 8\n    tolerance: 0\n  - quantity: mean age\n    value: 29.4\n    tolerance: 7.9\n    unit: years\n  - quantity: mean surface electrodes per subject\n    value: 87.0\n    tolerance: 12.9\n  - quantity: subjects with depth electrodes\n    value: 5\n    tolerance: 0\n  - quantity: mean depth electrodes in those subjects\n    value: 23.2\n    tolerance: 12.1\n  - quantity: subjects implanted in the right hemisphere\n    value: 5\n    tolerance: 0\n  criterion: Tolerances on the means are the SDs the paper states, as the protocol allows; the\n    counts are exact. Surface electrodes are grid and strip electrodes, depth electrodes the\n    rest (Extended Data Figure 1-1 legend). Values the dataset does not hold are reported as\n    not testable.\n- id: fig2-event-counts\n  statement: Each subject contributed between 151 and 947 movement events (median 640 across\n    subjects).\n  source: Figure 2 legend\n  quote: The total number of events for each subject was between 151 and 947 (median, 640\n    across subjects).\n  expected:\n  - quantity: fewest events in a subject\n    value: 151\n    tolerance: 15.1\n  - quantity: most events in a subject\n    value: 947\n    tolerance: 94.7\n  - quantity: median events per subject\n    value: 640\n    tolerance: 64\n  criterion: Which events are counted is not fixed by the text. Readings are (a) all\n    contralateral wrist movement events the dataset holds for a subject; (b) those left after\n    dropping events marked false positive and ECoG segments with power below 0 dB or with\n    115-125 Hz power more than 3 SD above all segments (Methods, ECoG-event synchronization;\n    the Figure 2 code reads its events from the spectral power files, which have these removed).\n    Reproduced when all three values are within tolerance under one reading.\n- id: fig2-features-differ-across-subjects\n  statement: All ten behavioural and environmental features differ significantly across\n    subjects.\n  source: Results, Behavior during naturalistic movements, paragraph 3; Figure 2\n  quote: All 10 metadata features significantly differed across subjects ( p < 0.001 for every\n    feature, one-way Kruskal–Wallis test).\n  statistics:\n  - test: one-way Kruskal-Wallis test, one per feature\n    p: 0.001\n    p_relation: \"<\"\n    n: 12 subjects, events pooled within subject\n  criterion: For each of the ten features, a one-way Kruskal-Wallis test of the event values\n    grouped by subject, on the events of claim fig2-event-counts (reading b, with reading a as\n    a variant), reach angle folded as in the opening comment and day of recording as a number.\n    Reproduced when p < 0.001 for all ten features; not reproduced otherwise, with every p\n    reported.\n- id: fig2-reach-shape\n  statement: Most reaches last under 2 s and cover under 200 pixels, and reach angle\n    distributions tend to be bimodal with peaks near +90 and -90 degrees, with few side-to-side\n    reaches.\n  source: Results, Behavior during naturalistic movements, paragraph 3; Figure 2\n  quote: Reach duration and reach magnitude show minimal intersubject variability, with most\n    reaches lasting <2 s and covering <200 pixels ... For reach angle, the distributions tend to\n    be bimodal, with peaks at ±90\n  criterion: The paper gives no measure for these words, so they are read as follows. \"Most\"\n    is more than half of the events, judged in every subject and in the events pooled over\n    subjects; reach duration in seconds and reach magnitude in pixels. Reach angle (folded to\n    -90 to 90 degrees) is judged on a Gaussian kernel density with Scott's bandwidth, the\n    seaborn kdeplot default the Figure 2 code uses, evaluated on -90 to 90; a subject is bimodal\n    with peaks at +-90 when the density's two highest local maxima lie within 15 degrees of -90\n    and of +90 and the density at 0 degrees is below both. Reproduced when the duration and\n    magnitude parts hold pooled and in at least 10 of 12 subjects, and the angle part holds\n    pooled and in more than half of the subjects (\"tend to\"). Partially reproduced when one of\n    the two parts holds.\n- id: fig2-bimanual-skew\n  statement: Bimanual ratio and bimanual overlap are skewed toward unimanual movement of the\n    contralateral arm, less so for subjects 02, 04 and 05, while the bimanual class is mostly\n    bimanual.\n  source: Results, Behavior during naturalistic movements, paragraph 4; Figure 2\n  quote: For bimanual ratio and overlap features, the distributions are skewed toward unimanual\n    movements of the contralateral limb, as expected from Extended Data Fig. 2-1 c , with less\n    skew for subjects 02, 04, and 05. In contrast, the bimanual class categorical feature is\n    primarily skewed toward bimanual movements\n  criterion: The paper gives no measure, so it is read as follows. Bimanual ratio (missing\n    values 0.5, code) skewed toward unimanual when its median is below 0.5; bimanual overlap\n    (seconds) skewed toward unimanual when its sample skewness (Fisher-Pearson) is positive;\n    bimanual class mostly bimanual when more than half the events are bimanual. \"Less skew\" for\n    S02, S04 and S05 when each is among the five subjects with the highest median bimanual\n    ratio. Reproduced when the ratio and overlap parts hold pooled and in at least 9 of 12\n    subjects, the class part holds pooled and in more than half the subjects, and the S02, S04,\n    S05 part holds; partially reproduced when some but not all of these hold.\n- id: extfig2-2-feature-correlations\n  statement: Over all events, reach magnitude correlates with reach duration (r = 0.26) and\n    onset speed (r = 0.56), reach duration with bimanual overlap (r = 0.48), and the bimanual\n    features with one another (overlap and ratio 0.51, class and ratio 0.50, overlap and class\n    0.61).\n  source: Results, Behavior during naturalistic movements, paragraph 5; Extended Data Figure\n    2-2\n  quote: Reach magnitude positively correlates with reach duration ( r = 0.26) and onset speed (\n    r = 0.56) ... Reach duration is also positively correlated with bimanual overlap ( r = 0.48)\n    ... overlap vs ratio, r = 0.51; class vs ratio, r = 0.50; and overlap vs class, r = 0.61\n  expected:\n  - quantity: r, reach magnitude and reach duration\n    value: 0.26\n    tolerance: 0.026\n  - quantity: r, reach magnitude and onset speed\n    value: 0.56\n    tolerance: 0.056\n  - quantity: r, reach duration and bimanual overlap\n    value: 0.48\n    tolerance: 0.048\n  - quantity: r, bimanual overlap and bimanual ratio\n    value: 0.51\n    tolerance: 0.051\n  - quantity: r, bimanual class and bimanual ratio\n    value: 0.5\n    tolerance: 0.05\n  - quantity: r, bimanual overlap and bimanual class\n    value: 0.61\n    tolerance: 0.061\n  criterion: Pearson correlation over the events of all 12 subjects pooled (\"group-level\"),\n    on untransformed features in the units of Figure 2 (duration and overlap in seconds,\n    magnitude in pixels, speed in pixels per second, missing bimanual ratios 0.5), as\n    plot_feature_scattermatrix in the code computes it (pandas DataFrame.corr). Event set as in\n    fig2-event-counts reading b, reading a shown as a variant. Reproduced when all six are within\n    tolerance; partially when four or five are.\n- id: fig2-days-and-waking\n  statement: Reach counts were fairly even across recording days except for subjects 04, 05 and\n    09, each with one day holding most events, and events occurred mostly during waking hours.\n  source: Results, Behavior during naturalistic movements, paragraph 3; Figure 2\n  quote: The number of reaches detected across days of recording was fairly consistent, with the\n    exceptions of subjects 04, 05, and 09, who each had 1 d representing most of the total\n    events. As expected, detected movement events often occurred mostly during waking hours.\n  criterion: '\"Most of the total events\" is read as more than half. Reproduced when the\n    subject''s busiest day holds more than half of its events for S04, S05 and S09 and for none\n    of the other nine subjects. Waking hours are not defined; they are read as 08:00 to 24:00,\n    the two daytime bins of the paper''s time-of-day feature, and the part holds when more than\n    half of each subject''s events fall in them. Partially reproduced when the day part holds for\n    the three named subjects but also for one or two others, or when only one of the two parts\n    holds. Event set as in fig2-event-counts reading b.'\n- id: fig3-group-lfb-decrease-hfb-increase\n  statement: At the group level, low-frequency power decreases and high-frequency power increases\n    at movement initiation in several cortical regions, as in controlled movement experiments.\n  source: Figure 3; Results, Intracortical spectral power during naturalistic movements,\n    paragraph 1\n  quote: Generally, we find the expected pattern of low-frequency (∼4–30 Hz) spectral power\n    decrease and high-frequency (∼50–120 Hz) power increases during movement initiation across\n    multiple cortices ( Fig.\n  statistics:\n  - test: two-sided bootstrap against baseline time points, 2000 permutations\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR (Benjamini-Hochberg)\n    n: 12 subjects\n  data: with_inputs\n  criterion: Group spectrogram per region as the Methods and the code (plot_specs_group) make\n    it. Per subject, the median over events of region power (spectral method of the opening\n    comment); the mean over the 12 subjects; the group median over -1.5 to -1 s subtracted\n    again (code). Masking as in the code (tfr_boot_sig_mask). Each subject's baseline time bins\n    are shuffled within frequency, the median over subjects is taken, repeated to about 2000\n    values per frequency, two-sided percentile p, Benjamini-Hochberg over all frequency and time\n    bins of the region at 0.05; non-significant values set to 0. \"At movement initiation\" is\n    read two ways. (a) The mean of the masked values over 0 to 0.5 s, the window of the paper's\n    banded analyses. (b) The time bin nearest 0 s. Reproduced when, under both readings, the\n    masked mean over the 4-30 Hz bins is below 0 and over the 50-120 Hz bins above 0 in each of\n    precentral, postcentral and inferior parietal. Partially reproduced when this holds in one\n    or two of them. Blocked as methods_underspecified when the readings disagree.\n- id: fig3-sensorimotor-largest\n  statement: Spectral power changes are largest in precentral, postcentral and inferior parietal\n    regions, and the three temporal regions show minimal movement-related changes.\n  source: Results, Intracortical spectral power during naturalistic movements, paragraph 2;\n    Figure 3\n  quote: Spectral power deviations are largest in magnitude in precentral, postcentral, and\n    inferior parietal regions, which are located in sensorimotor areas of the brain ... As\n    expected, all three temporal cortical regions contain minimal movement-related spectral power\n    fluctuations.\n  data: with_inputs\n  depends_on:\n  - fig3-group-lfb-decrease-hfb-increase\n  criterion: On the masked group spectrograms of claim fig3-group-lfb-decrease-hfb-increase. The\n    paper does not say how magnitude is measured. Readings are (a) the mean absolute masked\n    value over all frequency bins and 0 to 0.5 s; (b) the same over the 4-30 Hz bins and,\n    separately, over the 50-120 Hz bins, a region ranking high when it does in both; (c) as (a)\n    over -0.5 to 0.5 s. Reproduced when, under every reading, precentral, postcentral and\n    inferior parietal are the three largest of the eight regions and each temporal region is\n    below all three. Partially reproduced when two of the three named regions are in the top\n    three and the temporal part holds. Blocked as methods_underspecified when the readings give\n    different outcomes.\n- id: fig3-lfb-more-widespread\n  statement: Low-frequency power decreases are more spatially widespread than high-frequency\n    increases and are also present in supramarginal and superior temporal regions.\n  source: Results, Intracortical spectral power during naturalistic movements, paragraph 2;\n    Figure 3\n  quote: In addition, low-frequency power decreases appear more spatially widespread than\n    high-frequency power increases and are also present in supramarginal and superior temporal\n    regions.\n  data: with_inputs\n  depends_on:\n  - fig3-group-lfb-decrease-hfb-increase\n  criterion: On the masked group spectrograms, over 0 to 0.5 s. Readings for \"widespread\" are (a)\n    the number of regions with any significant negative bin in 4-30 Hz against the number with\n    any significant positive bin in 50-120 Hz; (b) the count of significant negative 4-30 Hz bins\n    against significant positive 50-120 Hz bins, summed over the eight regions and divided by\n    the number of frequency bins in each range. Reproduced when, under both readings, the\n    low-frequency count is larger, and supramarginal and superior temporal each have\n    significant negative 4-30 Hz bins. Blocked as methods_underspecified when the readings\n    disagree.\n- id: fig4-precentral-subject-variability\n  statement: In the precentral region every subject shows the low/high-frequency pattern, but\n    amplitudes and frequency bands vary; subjects 03, 06, 07, 08 and 11 have increases up to\n    120 Hz, subjects 09 and 12 mainly at 60-80 Hz, and subjects 04 and 08 have narrower\n    low-frequency decreases.\n  source: Results, Intracortical spectral power during naturalistic movements, paragraph 3;\n    Figure 4\n  quote: For instance, the precentral region shows the same low/high-frequency power pattern for\n    each subject ( Fig. 4 ), but the amplitudes and frequency bands of maximal power deviation\n    differ widely across subjects. Subjects 03, 06, 07, 08, and 11 show increased power at high\n    frequencies up to 120 Hz, while subjects 09 and 12 have increased power primarily between 60\n    and 80 Hz. For subjects 04 and 08, low-frequency power decreases occur across narrower\n    frequency bands compared with the other subjects.\n  data: with_inputs\n  criterion: Per subject, the unmasked median over events of precentral power (Figure 4 legend,\n    no statistical masking), averaged over 0 to 0.5 s to give a spectrum. The paper gives no\n    measure, so the parts are read as follows. (1) Every subject has a negative mean over 8-32\n    Hz and a positive mean over 76-100 Hz. (2) For S03, S06, S07, S08 and S11 the 116 and 121\n    Hz bins are positive. (3) For S09 and S12 the largest value among the 56-121 Hz bins is at\n    61 to 76 Hz (bins within 60-80 Hz), and the mean over 101-121 Hz is below half of it. (4)\n    The width of the decrease is the number of 1-46 Hz bins below half of the subject's most\n    negative value; S04 and S08 are among the three subjects with the fewest. Reproduced when\n    all four hold; partially when two or three hold. Part (1) failing in a subject is reported\n    by subject.\n- id: fig5-band-power-differs-across-subjects\n  statement: Precentral LFB and HFB power in the 0.5 s after movement onset differs\n    significantly across subjects.\n  source: Results, Intracortical spectral power during naturalistic movements, paragraph 4;\n    Figure 5; Table 1\n  quote: For both frequency bands, spectral power significantly differed across subjects ( p <\n    0.001 for both bands, one-way Kruskal–Wallis test).\n  statistics:\n  - test: one-way Kruskal-Wallis test, one per band\n    p: 0.001\n    p_relation: \"<\"\n    n: 12 subjects, events pooled within subject\n  data: with_inputs\n  criterion: Banded precentral power per event (opening comment; band mean as the main result,\n    the code's median as a variant), all days pooled per subject. One-way Kruskal-Wallis test\n    across the 12 subjects per band, as the Figure 5 notebook (pingouin kruskal). \"Pooling over\n    all electrodes\" (Results) is the projection of all the subject's good electrodes onto the\n    precentral region, as the code does. Reproduced when p < 0.001 in both bands.\n- id: table1-subject-band-power-ci\n  statement: Each subject's precentral band power lies in the 95% bootstrap interval Table 1\n    gives; LFB power is below baseline and HFB power above it for most subjects.\n  source: Table 1\n  inferred: Values read from Table 1; no sentence states them. The statement is a reading of the\n    table.\n  data: with_inputs\n  criterion: 'Table 1 intervals (dB), LFB then HFB. S01 -1.87 to -1.29, 0.03 to 0.23; S02 -1.12\n    to -0.31, 0.07 to 0.64; S03 -2.11 to -1.73, 1.39 to 1.67; S04 -0.17 to 0.01, 0.32 to 0.52;\n    S05 -0.7 to -0.38, 0.2 to 0.48; S06 -1.63 to -1.11, 2.02 to 2.37; S07 -0.84 to -0.51, 1.14\n    to 1.34; S08 -0.3 to 0.04, 0.36 to 0.63; S09 -0.57 to -0.08, -0.11 to 0.23; S10 -0.87 to\n    -0.35, 0.01 to 0.3; S11 -2.3 to -1.86, 0.09 to 0.34; S12 -0.66 to -0.44, 0.06 to 0.2. The\n    table does not say which statistic the interval is for. Readings are (a) the mean and (b)\n    the median over the subject''s events of banded precentral power. Band power is taken as\n    the band mean (Methods) or the band median (code), giving four readings in all. Reproduced\n    when, under one reading, the point estimate lies inside the paper''s interval for all 24\n    subject and band pairs. Partially reproduced when it does for at least 18. The attempt''s own\n    5000-replicate bootstrap intervals are shown beside the paper''s.'\n- id: fig5-recording-day-effects\n  statement: Precentral band power differs significantly across recording days in LFB for\n    subjects 03, 05, 06, 07, 08 and 11, and in HFB for subjects 03, 04, 07, 08 and 10, despite\n    baseline subtraction.\n  source: Results, Intracortical spectral power during naturalistic movements, paragraph 4;\n    Figure 5; Table 2\n  quote: We also found a significant effect of recording day in LFBs for subjects 03 ( p <\n    0.001, Kruskal–Wallis test), 05 ( p = 0.013), 06 ( p < 0.001), 07 ( p = 0.041), 08 ( p =\n    0.013), and 11 ( p < 0.001), as well as in HFBs for subjects 03 ( p = 0.002), 04 ( p <\n    0.001), 07 ( p < 0.001), 08 ( p = 0.004), and 10 ( p = 0.006).\n  statistics:\n  - about: LFB, S03\n    test: Kruskal-Wallis test\n    p: 0.001\n    p_relation: \"<\"\n  - about: LFB, S05\n    test: Kruskal-Wallis test\n    p: 0.013\n  - about: LFB, S06\n    test: Kruskal-Wallis test\n    p: 0.001\n    p_relation: \"<\"\n  - about: LFB, S07\n    test: Kruskal-Wallis test\n    p: 0.041\n  - about: LFB, S08\n    test: Kruskal-Wallis test\n    p: 0.013\n  - about: LFB, S11\n    test: Kruskal-Wallis test\n    p: 0.001\n    p_relation: \"<\"\n  - about: HFB, S03\n    test: Kruskal-Wallis test\n    p: 0.002\n  - about: HFB, S04\n    test: Kruskal-Wallis test\n    p: 0.001\n    p_relation: \"<\"\n  - about: HFB, S07\n    test: Kruskal-Wallis test\n    p: 0.001\n    p_relation: \"<\"\n  - about: HFB, S08\n    test: Kruskal-Wallis test\n    p: 0.004\n  - about: HFB, S10\n    test: Kruskal-Wallis test\n    p: 0.006\n  data: with_inputs\n  criterion: Per subject and band, a one-way Kruskal-Wallis test of banded precentral power\n    across the subject's recording days, uncorrected, at p < 0.05 (Figure 5 legend; the notebook\n    uses pingouin's uncorrected p). Band mean as the main result, band median (code) as a\n    variant. The paper's pattern is the 11 significant pairs above and the 13 other subject and\n    band pairs not significant. Reproduced when all 24 pairs agree; partially reproduced when at\n    least 20 agree. Each p is reported, with the per-day 95% intervals of Table 2 for\n    comparison.\n- id: extfig5-1-baseline-reduces-day-variability\n  statement: Subtracting the -1.5 to -1 s baseline reduces the variability of band power across\n    recording days, though clear variability remains.\n  source: Results, Intracortical spectral power during naturalistic movements, paragraph 4;\n    Extended Data Figure 5-1 legend\n  quote: Baseline subtraction reduces the variation across recording days, as expected, but clear\n    variability remains.\n  data: with_inputs\n  criterion: The legend gives the measure, the SD across recording days of the average LFB\n    (8-32 Hz) and HFB (76-100 Hz) power, with and without baseline subtraction. The figure could\n    not be read and no code for it is in the repository, so what is averaged is open. Readings\n    are (a) precentral region power, per subject, the SD across days of the day means of event\n    band power; (b) the same per good electrode, pooled over electrodes and subjects. Without\n    baseline means the 10*log10 band power with no subtraction. Reproduced when, under both\n    readings and in both bands, the SD with baseline is below the SD without it for more than\n    half of the units (subjects or electrodes) and the median SD with baseline is above 0.\n    Blocked as methods_underspecified when the readings disagree.\n- id: discussion-day-changes-small\n  statement: Day-to-day changes in baseline-subtracted spectral power are small (about 1-2 dB)\n    compared with spectral power without baseline subtraction (about 10-50 dB).\n  source: Discussion, paragraph 3\n  quote: It is also worth noting that these day-to-day changes in ECoG spectral power are small\n    in magnitude (±1–2 dB) relative to spectral power without any baseline values subtracted\n  data: with_inputs\n  criterion: On precentral banded power, per subject and band, the day means of the event\n    values. The day-to-day change is the largest absolute difference between a day mean and the\n    subject's overall mean. It holds when every such change is at most 2.2 dB (2 dB widened by\n    10%). The level without baseline is the mean 10*log10 band power without subtraction. It\n    depends on the voltage unit, which the paper does not state; readings are microvolts and\n    volts. That part holds when the levels lie in 9 to 55 dB (10-50 dB widened by 10% of each\n    bound) under one unit reading. Reproduced when both parts hold; partially when only the\n    first does.\n- id: fig6b-best-models-sensorimotor\n  statement: Regression models with the highest withheld R2 are mainly at electrodes over\n    frontoparietal sensorimotor areas, for both bands.\n  source: Figure 6b; Results, Modeling single-event spectral power with behavioral features,\n    paragraph 2; Extended Data Figure 6-1\n  quote: For both frequency bands, intracortical activity variability is best explained by the\n    fit of our models to electrodes located in frontoparietal sensorimotor areas ( Fig. 6 b ,\n    Extended Data Fig. 6-1 ).\n  data: with_inputs\n  criterion: Full-model withheld R2 per electrode and band (regression method of the opening\n    comment). The paper shows this on brain maps and gives no measure. Each electrode is assigned\n    to an area in one of two ways, (a) to the region of the eight with its largest projection\n    weight, or (b) by projecting the electrode R2 values onto the eight regions with the\n    projection weights, as for power, and averaging over subjects. Frontoparietal sensorimotor\n    regions are precentral, postcentral and inferior parietal (the regions the Results call\n    sensorimotor) with middle frontal and supramarginal. Under (a), the part holds when more\n    than half of the electrodes with R2 > 0.05 are in these five regions and the median R2 of\n    precentral, postcentral and inferior parietal electrodes exceeds that of temporal ones.\n    Under (b), it holds when the three regions with the highest projected R2 are among the five\n    frontoparietal ones. Reproduced when this holds in both bands under both readings. Blocked\n    as methods_underspecified when the readings disagree.\n- id: fig6-r2-at-most-025\n  statement: All regression models explain at most 25% of the variance of withheld single-event\n    power.\n  source: Results, Modeling single-event spectral power with behavioral features, paragraph 2\n  quote: However, all R 2 scores are at most 0.25, indicating that even the best models cannot\n    explain >75% of the variance in the withheld data.\n  expected:\n  - quantity: largest full-model withheld R2 over electrodes, subjects and bands\n    value: 0.25\n    tolerance: 0.025\n  criterion: The largest split-averaged full-model withheld R2 over all good electrodes of all\n    subjects in both bands (regression method of the opening comment). Reproduced when it is at\n    most 0.275 (0.25 plus 10%). The value is also reported for the code's 80/20 split and\n    median band power.\n- id: fig6c-angle-and-day-most-informative\n  statement: Reach angle and day of recording are the most informative features for single-event\n    power, especially for low-frequency power.\n  source: Figure 6c and legend; Results, Modeling single-event spectral power with behavioral\n    features, paragraph 2\n  quote: Among individual features, we find that reach angle and day of recording are the most\n    informative ( Fig. 6 c ).\n  criterion: Delta R2 per feature, electrode and band (opening comment), over electrodes with\n    withheld R2 > 0.05 in that band, across all subjects. The summary across electrodes is the\n    median, as the box plots of Figure 6c show (code). Reproduced when reach angle and recording\n    day have the two largest median Delta R2 of the ten features in the LFB. The HFB ranking is\n    reported, and the claim is partially reproduced when only one of the two is in the LFB top\n    two. Shown as variants are the code's Delta R2 (shuffling test events too), the code's\n    selection by LFB R2, and the code's 80/20 split.\n- id: extfig6-2-angle-most-retained\n  statement: Reach angle is the feature most often retained by forward selection in sensorimotor\n    regions, followed by reach duration, reach magnitude, bimanual ratio and bimanual overlap.\n  source: Extended Data Figure 6-2 legend; Results, Modeling single-event spectral power with\n    behavioral features, paragraph 2\n  quote: Reach angle is the feature most often retained, followed by reach duration, reach\n    magnitude, bimanual ratio, and bimanual overlap.\n  data: with_inputs\n  criterion: Per electrode and band, whether each feature is kept by forward selection (code\n    feat_select_prob; a day or time-of-day one-hot column counts as 1/number of columns of that\n    feature). The legend projects the retention probability onto the eight regions and averages\n    across subjects; the code of this step is not in the repository. It is read as the\n    projection-weighted mean over the subject's good electrodes, then the mean over subjects, as\n    for power. Reproduced when reach angle has the highest retention probability among the ten\n    features in precentral, postcentral and inferior parietal for both bands. The order of the\n    next four features is reported and compared with the legend's.\n- id: fig6d-upward-reaches-enhance-pattern\n  statement: Upward reaches are associated with lower low-frequency power and higher\n    high-frequency power, that is, a larger version of the average movement response.\n  source: Figure 6d and legend; Results, Modeling single-event spectral power with behavioral\n    features, paragraph 2\n  quote: The coefficients for reach angle indicate that upward reaches are associated with\n    decreased low-frequency power and increased high-frequency power compared with the average\n    response.\n  criterion: Reach angle coefficient (positive angle is upward, standardised feature), averaged\n    over splits, over electrodes with withheld R2 > 0.05 in that band. Reproduced when the median\n    coefficient is below 0 for LFB and above 0 for HFB; partially when it holds in one band. The\n    code's selection by LFB R2 is shown as a variant.\n- id: fig6d-angle-and-day-largest-coefficients\n  statement: Reach angle and day of recording have the largest coefficient magnitudes among the\n    features, and the SD of the recording-day coefficients is large.\n  source: Figure 6d and legend; Results, Modeling single-event spectral power with behavioral\n    features, paragraph 2\n  quote: In addition, both reach angle and day of recording have the largest coefficient\n    magnitudes among behavioral features in the regression models ( Fig. 6 c ).\n  criterion: Per electrode with withheld R2 > 0.05 in the band, the absolute split-averaged\n    coefficient of each continuous or binary feature, and for day and time of day the SD of\n    their one-hot coefficients (Figure 6 legend, code). The summary across electrodes is the\n    median, as in the box plots. Reproduced when reach angle and recording day have the two\n    largest medians in both bands; partially when in one band. Variants as for\n    fig6c-angle-and-day-most-informative.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000055/10.1523-eneuro.0007-21.2021.yaml paper/10.1523-eneuro.0007-21.2021.txt; grep -n " — \|rather\|—" claims/000055/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml
d=yaml.safe_load(open('claims/000055/10.1523-eneuro.0007-21.2021.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print(p, x[:80])
walk(d)
print(sum(1 for c in d['claims'] if 'criterion' in c), sum(1 for c in d['claims'] if 'statistics' in c), sum(1 for c in d['claims'] if c.get('kind')=='link'))
"
```

```
23 4 1
```

**Agent**

I wrote `claims/000055/10.1523-eneuro.0007-21.2021.yaml`. The quote checker reports 0 problems: 23 claims, 21 quotes, 14 statistical values.

**Text read.** The version of record as served by Europe PMC (PMC8225404): main text, Methods, figure legends, Tables 1 and 2, and the review history. There was no PDF. The Extended Data figures are EPS downloads, so only their legends are in the text.

**Code read.** `BruntonUWBio/naturalistic_arm_movements_ecog` at commit 04c6faf2 (17 March 2021). It covers spectral power, the bootstrap masking, the projection onto brain regions, the regression, and the notebooks for Figures 2 to 6. It does not cover preprocessing, pose estimation, event detection, feature extraction, the Kruskal–Wallis tests of Figure 2, the confidence intervals of Tables 1 and 2, or Extended Data Figures 5-1 and 6-2.

**Claims.**
- **Count:** 23 claims. One is a link check (`subject-days`); 22 are findings.
- **Quotes:** 21 claims have a quote. The Table 1 claim is marked `inferred`, and the link check has neither.
- **Statistics:** 4 claims carry them, 14 values in all: Kruskal–Wallis tests across subjects, the 11 per-subject recording-day tests, and the bootstrap with FDR correction for Figure 3.
- **Criteria:** all 23 have one.
- **Data:** 12 claims are marked `with_inputs` because they need the AAL atlas to place electrodes in brain regions.

**Where the Methods and the code disagree.** The Methods are the main result and the code's choice is shown as a variant:
- Band power: the Methods say "averaged" (mean); the code takes the median.
- Train/test split: 90/10 in the Methods; 80/20 with days balanced in the code.
- ΔR²: the Methods score the shuffled model on unshuffled withheld data; the code shuffles the test events too.
- Log transform: the code also log-transforms onset speed.
- Electrode selection for Figure 6b–d: the legend's R² > 0.05 is applied per band; the code selects by the low-frequency R² for both bands.

**Details the paper leaves open, and the readings named for each:**
- **Events counted:** all events in the dataset, or only those left after removing false positives and artifact segments.
- **"At movement initiation" in Figure 3:** the mean over 0 to 0.5 s, or the time bin nearest 0 s.
- **"Largest in magnitude" in Figure 3:** mean absolute power over all frequencies, per band, or over −0.5 to 0.5 s.
- **"More widespread" for low frequencies:** a count of regions, or a count of significant bins.
- **Tables 1 and 2 intervals:** whether they are for the mean or the median, crossed with mean or median band power (four readings).
- **Extended Data Figure 5-1 SD across days:** per subject in the precentral region, or per electrode.
- **Unit for the absolute 10–50 dB level:** microvolts or volts.
- **Figure 6b area assignment:** each electrode goes to the region with its largest weight, or R² is projected onto the regions.
- **Extended Data Figure 6-2 projection:** the paper gives no method; I used a weighted mean projection, as for power.
- **Words the paper gives no measure for:** "most", "bimodal", "skewed", "waking hours" and the per-subject features of Figure 4. Each criterion says how I read them, as the reader's reading and not the paper's.

**Missing from the paper.** The Extended Data figures themselves (1-1, 2-1 to 2-4, 3-1, 4-1 to 4-7, 5-1, 6-1, 6-2):
- The per-subject electrode counts (1-1) and the per-subject confidence intervals for the features (2-3, 2-4) could not be read.
- The claims on 2-2, 5-1 and 6-2 rest on their legends and on the Results sentences that cite them.

The paper's curated data, including the projection matrices, are on Figshare and are named in the opening comment. Subjects S01 to S12 are assumed to match the dataset's subjects 01 to 12 in order; the `subject-days` link checks this against the days listed in Table 2.

## End of run

31 turns, 6 minutes, result: success.
