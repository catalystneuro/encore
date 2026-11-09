# 000678 · author · run 41188142719

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls claims/000678 paper entries | head -50
```

**Agent calls Bash**

```bash
cat README.md docs/design.md docs/archives.md | head -400
```

```
<persisted-output>
Output too large (36.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f1445809-fc2d-4a04-a125-d63cfd1285d0/tool-results/brmgh8yxa.txt

Preview (first 2KB):
Sat Oct 31 09:20:30 UTC 2026
# Protocol for an attempt

Version: `pilot-12`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 20 more lines not kept]
```

```
Exit code 1
bwrap: Can't get type of source .git/config.worktree.lock: No such file or directory
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
3	Version: `pilot-12`. Record this version in the attempt's provenance.
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

**Agent calls Bash**

```bash
cat README.md; cat docs/design.md | head -200
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://encorescience.org/>

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 319 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p docs/design.md; grep -n -A60 "^## DANDI" docs/archives.md | head -120
```

````
dataset:
  archive: dandi          # dandi, ebrains, openneuro, dryad, zenodo, ...
  id: "001754"            # the dataset's identifier in that archive
  version: 0.260728.1352  # attempts only: the version read, or draft
  doi: 10.48324/dandi.001754/0.260728.1352   # when the version has one
  modified: 2026-10-14T21:55:09Z             # for a draft, which can change
```

A published version is fixed and usually has a DOI; a draft has neither, so
it is pinned by its modification time. The archive and identifier are what
the registry keys on, so a dataset without a DOI can still be recorded. The
tools, the workflows and the site still work only on DANDI, and directories
are named by the DANDI identifier.

## What is reused from the example-notebooks registry

That work (in the CatalystNeuro fork of `dandi/example-notebooks`) stays as it
is. The parts that carry over, adapted:

- the notebook test harness and the locked-environment tooling;
[... 113 more lines not kept]
````

**Agent calls Bash**

```bash
ls claims/000678 paper entries/001453-fouke-2025 claims/001453 questions | head; cat claims/000678/*.yaml
```

```
<persisted-output>
Output too large (53.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f1445809-fc2d-4a04-a125-d63cfd1285d0/tool-results/bz6i9gasp.txt

Preview (first 2KB):
claims/000678:
10.1016-j.celrep.2024.113709.yaml

claims/001453:
10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
# Claims for Hulsey, Zumwalt, Mazzucato, McCormick & Jaramillo (2024), "Decision-making dynamics
# are predicted by arousal and uninstructed movements", Cell Reports 43(1), 113709, on dandiset
# 000678.
#
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000678/10.1016-j.celrep.2024.113709.yaml"
}
```

```
1	# Claims for Hulsey, Zumwalt, Mazzucato, McCormick & Jaramillo (2024), "Decision-making dynamics
2	# are predicted by arousal and uninstructed movements", Cell Reports 43(1), 113709, on dandiset
3	# 000678.
4	#
5	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
6	# protocol pilot-10 as stated in docs/protocol.md.
7	#
8	# Text read: the accepted author manuscript of the version of record in PubMed Central
9	# (PMC11016285, NIHMS1970871), as served by ncbi_pmc, full text with Results, Discussion, STAR
10	# Methods and figure legends, and its supplement (NIHMS1970871-supplement-1.pdf, the legends of
11	# Figures S1 to S8, read as extracted text). The bioRxiv preprint (10.1101/2023.03.02.530651 v2)
12	# is also under paper/ and was not used for claims. The main-text PDF is not under paper/, so the
13	# main figures were not seen; where a significance mark appears only in a figure, it is taken from
14	# the figure code below, which draws it.
15	#
16	# Code read: the analysis code the paper links, Zenodo doi:10.5281/zenodo.10306018
17	# (hulsey2023.zip, folders hulsey2023_analysis, a minimal uobrainflex and the fork of ssm with
18	# categorical emissions). The hulsey2023 scripts are also in github.com/sjara/uobrainflex at
19	# commit ef48985192e4af332c64f9d2e70ddcfc78659040 (folder hulsey2023/), except FigureS7.py and
20	# FigureS8.py, which are only in the Zenodo archive. The scripts are
[... 885 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/README.md; ls entries/001453-fouke-2025; cat attempts/001453-fouke-2025-01.yaml | head -150
```

```
10.1016-j.celrep.2024.113709.supp.pdf
10.1016-j.celrep.2024.113709.txt
10.1101-2023.03.02.530651.txt
schema_version: 1
name: 001453-fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
helpers:
- omr.py
related:
[... 194 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/001453-fouke-2025-01.yaml | grep -n -B2 -A30 "^findings\|^verifications\|blocked_by" | head -120; cat entries/001453-fouke-2025/requirements.in; ls schemas
```

```
48-- claim: fig1cef-representative-values
49-  outcome: blocked
50:  blocked_by: metadata_insufficient
51-  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
52-    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
53-    dandiset gives no mapping from those folders to its subjects, nor the original file names.
54-- claim: fig2d-shared-architecture
55-  outcome: blocked
56:  blocked_by: data_missing
57-  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
58-    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
59-    notebooks only, and no other dandiset of this lab or paper was found on the archive.
60-- claim: fig2g-dsi-similar
61-  outcome: blocked
62:  blocked_by: data_missing
63-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
64-- claim: fig2h-fewer-motion-responsive
65-  outcome: blocked
66:  blocked_by: data_missing
67-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000678/versions/ | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -n -i "dandi\|000678\|zenodo\|github" paper/10.1016-j.celrep.2024.113709.txt | head; cd $TMPDIR; for v in 0.231004.2146 0.261020.0029; do curl -s https://api.dandiarchive.org/api/dandisets/000678/versions/$v/ > meta_$v.json; done; diff <(python -m json.tool meta_0.231004.2146.json) <(python -m json.tool meta_0.261020.0029.json) | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -o -i ".\{150\}\(dandi\|000678\|zenodo\.\)[^ ]*.\{150\}" paper/10.1016-j.celrep.2024.113709.txt | head; cd $TMPDIR; diff <(python -m json.tool meta_0.231004.2146.json) <(python -m json.tool meta_0.261020.0029.json) | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; for v in 0.231004.2146 0.261020.0029; do python - <<EOF
import requests, json
url="https://api.dandiarchive.org/api/dandisets/000678/versions/$v/assets/?page_size=1000"
out=[]
while url:
    r=requests.get(url).json(); out+=r['results']; url=r['next']
json.dump(out,open('assets_$v.json','w'))
print(len(out), sum(a['size'] for a in out))
EOF
done; python -c "
import json
a=json.load(open('assets_0.231004.2146.json'));b=json.load(open('assets_0.261020.0029.json'))
A={x['path']:(x['size'],x['blob'] if 'blob' in x else None) for x in a};B={x['path']:(x['size'],x.get('blob')) for x in b}
print(A==B, len(set(A)^set(B)))
print(list(a[0].keys()))
for x in sorted(A)[:10]: print(x, A[x])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    a=json.load(open('assets_0.231004.2146.json'));b=json.load(open('assets_0.261020.0029.json'))
                ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'assets_0.231004.2146.json'
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q requests pynwb remfile h5py numpy pandas scipy scikit-learn matplotlib dandi 2>&1 | tail -3; python -V
```

```
Python 3.13.17
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; for v in 0.231004.2146 0.261020.0029; do python - <<EOF
import requests, json
url="https://api.dandiarchive.org/api/dandisets/000678/versions/$v/assets/?page_size=1000"
out=[]
while url:
    r=requests.get(url).json(); out+=r['results']; url=r['next']
json.dump(out,open('assets_$v.json','w'))
print(len(out), sum(a['size'] for a in out))
EOF
done; python -c "
import json
a=json.load(open('assets_0.231004.2146.json'));b=json.load(open('assets_0.261020.0029.json'))
A={x['path']:(x['size'],x['asset_id']) for x in a};B={x['path']:(x['size'],x['asset_id']) for x in b}
print(A==B, len(set(A)^set(B)))
print(a[0])
for x in sorted(A)[:5]: print(x, A[x])
import collections
print(collections.Counter(p.split('/')[0] for p in A))
"
```

```
391 8108311416
391 8108311416
True 0
{'asset_id': '4a81e0b6-6a51-453a-925f-e6084910ae54', 'blob': '6a8e60ed-37b2-4779-9fa6-0dea5d56b84e', 'zarr': None, 'path': 'sub-BW041/sub-BW041_ses-20210830T130549.nwb', 'size': 28417584, 'created': '2023-10-04T00:35:29.363393Z', 'modified': '2023-10-04T21:46:13.252607Z'}
sub-BW041/sub-BW041_ses-20210830T130549.nwb (28417584, '4a81e0b6-6a51-453a-925f-e6084910ae54')
sub-BW041/sub-BW041_ses-20210831T133632.nwb (18886188, 'f7fd0c8c-2cc1-49e3-99e5-3e1324b8e304')
sub-BW041/sub-BW041_ses-20210901T122327.nwb (17367064, 'e8906288-9c1f-489b-b0f6-dd14a1fccd6f')
sub-BW041/sub-BW041_ses-20210902T131253.nwb (21054184, '94e8791a-f8ce-4940-a838-13b1b8df5f02')
sub-BW041/sub-BW041_ses-20210903T135324.nwb (20791004, '4780b7dc-3341-46f3-80e0-6689759a2bfa')
Counter({'sub-BW045': 84, 'sub-BW048': 35, 'sub-BW051': 35, 'sub-BW046': 34, 'sub-BW053': 32, 'sub-BW041': 25, 'sub-BW059': 25, 'sub-BW071': 25, 'sub-BW061': 23, 'sub-BW067': 23, 'sub-BW064': 21, 'sub-BW062': 17, 'sub-BW058': 12})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; cat > open1.py <<'EOF'
import remfile, h5py, pynwb, requests, sys
aid=sys.argv[1]
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
s3=requests.head(url,allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset): print(name, obj.shape, obj.dtype, dict((k,v) for k,v in obj.attrs.items() if k in ('unit','description','conversion','rate')))
    else: print(name, {k:v for k,v in obj.attrs.items() if k in ('neurodata_type','description','colnames')})
f.visititems(show)
EOF
time python open1.py 4a81e0b6-6a51-453a-925f-e6084910ae54
```

```
acquisition {}
acquisition/face_energy {'description': 'Pixel intensity time differential within face ROI.', 'neurodata_type': 'TimeSeries'}
acquisition/face_energy/data (213620,) float64 {'conversion': np.float64(1.0), 'unit': 'a.u.'}
acquisition/face_energy/timestamps (213620,) float64 {'unit': 'seconds'}
acquisition/licks_left {'description': 'Time of each left-port lick.', 'neurodata_type': 'TimeSeries'}
acquisition/licks_left/data (1649,) int32 {'conversion': np.float64(1.0), 'unit': 's'}
acquisition/licks_left/timestamps (1649,) float64 {'unit': 'seconds'}
acquisition/licks_right {'description': 'Time of each right-port lick.', 'neurodata_type': 'TimeSeries'}
acquisition/licks_right/data (2028,) int32 {'conversion': np.float64(1.0), 'unit': 's'}
acquisition/licks_right/timestamps (2028,) float64 {'unit': 'seconds'}
acquisition/post_hoc_pupil_diameter {'description': 'Pixel length of the long axis of the pupil per frame calculated post-hoc.', 'neurodata_type': 'TimeSeries'}
acquisition/post_hoc_pupil_diameter/data (213620,) float64 {'conversion': np.float64(1.0), 'unit': 'pixels'}
acquisition/post_hoc_pupil_diameter/timestamps (213620,) float64 {'unit': 'seconds'}
acquisition/pupil_area {'description': 'The pixel area of the pupil per frame calculated online during behavioral performance.', 'neurodata_type': 'TimeSeries'}
acquisition/pupil_area/data (213620,) float64 {'conversion': np.float64(1.0), 'unit': 'sq_pixels'}
acquisition/pupil_area/timestamps (213620,) float64 {'unit': 'seconds'}
acquisition/pupil_diameter {'description': 'Pixel length of the long axis of the pupil per frame calculated online during behavioral performance.', 'neurodata_type': 'TimeSeries'}
acquisition/pupil_diameter/data (213620,) float64 {'conversion': np.float64(1.0), 'unit': 'pixels'}
acquisition/pupil_diameter/timestamps (213620,) float64 {'unit': 'seconds'}
acquisition/reward_left {'description': 'Time of each left-port reward.', 'neurodata_type': 'TimeSeries'}
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
nproc; free -g | head -2; cd $TMPDIR; curl -sL -o uob.zip https://github.com/sjara/uobrainflex/archive/ef48985192e4af332c64f9d2e70ddcfc78659040.zip; ls -la uob.zip; unzip -q -o uob.zip && ls uobrainflex-*/ uobrainflex-*/hulsey2023 2>/dev/null | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040; wc -l hulsey2023/*/*.py uobrainflex/nwb/loadbehavior.py uobrainflex/behavioranalysis/flex_hmm.py; ls hulsey2023/ssm_changes; cat hulsey2023/data_processing_code/1_compile_data.py
```

```
14 hulsey2023/data_processing_code/1_compile_data.py
   141 hulsey2023/data_processing_code/2_n_states.py
    72 hulsey2023/data_processing_code/3_generate_hmms.py
   255 hulsey2023/data_processing_code/4_optimal_pupils.py
   150 hulsey2023/data_processing_code/5_decoding.py
   153 hulsey2023/data_processing_code/6_predictive_accuracy.py
   169 hulsey2023/data_processing_code/7_example_mouse_decoding.py
   561 hulsey2023/figure_generation_code/Figure1.py
   443 hulsey2023/figure_generation_code/Figure2.py
   518 hulsey2023/figure_generation_code/Figure3.py
   459 hulsey2023/figure_generation_code/Figure4.py
   273 hulsey2023/figure_generation_code/Figure5.py
   357 hulsey2023/figure_generation_code/FigureS1.py
   124 hulsey2023/figure_generation_code/FigureS2.py
   688 hulsey2023/figure_generation_code/FigureS3_S4.py
   340 hulsey2023/figure_generation_code/FigureS5.py
   399 hulsey2023/figure_generation_code/FigureS6.py
   821 hulsey2023/ssm_changes/hmm.py
  1948 hulsey2023/ssm_changes/observations.py
   499 uobrainflex/nwb/loadbehavior.py
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040; grep -n "^def " uobrainflex/behavioranalysis/flex_hmm.py; grep -n "^def " uobrainflex/nwb/loadbehavior.py
```

```
33:def format_choice_behavior_hmm(trial_data, trial_labels, drop_no_response=False, drop_distractor_trials=True):
145:def compile_choice_hmm_data(sessions, get_behavior_measures=False, verbose=True):
187:def choice_hmm_sate_fit(subject, inpts, true_choices, max_states=4, save_folder=''):
294:def choice_hmm_fit(subject, num_states, inpts, true_choices):
314:def generate_n_states_hmms(max_states, inpts, true_choices):  
321:def hmm_state_testing(max_states,train_inpts,train_choices,test_inpts,test_choices):
333:def get_posterior_probs(hmm, hmm_trials, occ_thresh = .8):
367:def get_posterior_probs_from_hmm_trials(hmm_trials):   
382:def get_inpts_from_hmm_trials(hmm_trials):
390:def get_pupils_from_hmm_trials(hmm_trials):
397:def get_true_choices_from_hmm_trials(hmm_trials):
405:def set_hmm_trials_choices(hmm_trials):
428:def get_true_choices_from_outcomes_hmm_trials(hmm_trials):
448:def get_psychos(hmm_trials):  
464:def get_trials_psychos(all_trials):
482:def compare_psychos(psycho1,psycho2):
500:def hmm_trials_to_all_trials(hmm_trials):
507:def hmm_trials_to_p_state(hmm_trials):
525:def get_optimal_pupil(hmm_trials):
559:def permute_hmm(hmm, hmm_trials):
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040; sed -n 1,190p uobrainflex/behavioranalysis/flex_hmm.py; sed -n 330,600p uobrainflex/behavioranalysis/flex_hmm.py; sed -n 786,830p uobrainflex/behavioranalysis/flex_hmm.py
```

```
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:49:15 2021 by Daniel Hulsey

Functions for formatting task performance data and fitting models with the SSM package 
"""

from uobrainflex.nwb import loadbehavior as load
import ssm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle
import matplotlib.gridspec as gridspec
import scipy
from PIL import Image
import glob
import os 
from scipy.stats import mannwhitneyu #non parametric distribution test
from scipy.stats import levene   #levene tests for differences in the variance of data of non normal distributions
[... 487 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040; sed -n 57,135p uobrainflex/nwb/loadbehavior.py; sed -n 210,282p uobrainflex/nwb/loadbehavior.py; sed -n 379,473p uobrainflex/nwb/loadbehavior.py
```

```
def load_nwb_file(nwbfilepath):
    ioObj = pynwb.NWBHDF5IO(nwbfilepath, 'r', load_namespaces=True)
    nwbFileObj = ioObj.read()
    return nwbFileObj


def get_stim_vals(trial_data,trial_dict):
    aud_stim_direction = trial_data['auditory_stim_id'].values
    aud_stim_direction[np.where(aud_stim_direction==trial_dict['auditory_stim_id']['left'])[0]]=-1
    aud_stim_direction[np.where(aud_stim_direction==trial_dict['auditory_stim_id']['right'])[0]]=1
    aud_stim_direction[np.where(aud_stim_direction==trial_dict['auditory_stim_id']['no stim'])[0]]=np.nan
    aud_stim_value = trial_data['auditory_stim_difficulty'].values
    aud_stim_value = aud_stim_value-(1-aud_stim_value)/2
    aud_stim = aud_stim_direction*aud_stim_value

    vis_stim_direction =  trial_data['visual_stim_id'].values
    vis_stim_direction[np.where(vis_stim_direction==trial_dict['visual_stim_id']['left'])[0]]=-1
    vis_stim_direction[np.where(vis_stim_direction==trial_dict['visual_stim_id']['right'])[0]]=1
    vis_stim_direction[np.where(vis_stim_direction==trial_dict['visual_stim_id']['no stim'])[0]]=np.nan
    if any(trial_data.columns == 'visual_stim_difficulty'):
[... 228 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040/hulsey2023/data_processing_code; cat 2_n_states.py 3_generate_hmms.py | grep -v "^\s*#" | grep -v "^\s*$"
```

```
import os
import numpy as np
import glob
from uobrainflex.behavioranalysis import flex_hmm
from sklearn.model_selection import KFold
import time
import ssm
import ray
@ray.remote
def MAP_hmm_fit(subject, num_states, training_inpts, training_choices, test_inpts, test_choices):
    obs_dim = training_choices[0].shape[1]          # number of observed dimensions
    num_categories = len(np.unique(np.concatenate(training_choices)))    # number of categories for output
    input_dim = inpts[0].shape[1]                                    # input dimensions
    TOL = 10**-4
    N_iters = 1000
    prior_sigma = 2
    prior_alpha = 2
    hmm = ssm.HMM(num_states, obs_dim, input_dim, observations="input_driven_obs", 
                         observation_kwargs=dict(C=num_categories,prior_sigma=prior_sigma),
                         transitions="sticky", transition_kwargs=dict(alpha=prior_alpha,kappa=0))
[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040/hulsey2023/ssm_changes; grep -n "class InputDrivenObservations" -A 140 observations.py | grep -v '^\S*\s*$' | head -150
```

```
629:class InputDrivenObservations(Observations):
631-    def __init__(self, K, D, M=0, C=2, prior_mean = 0, prior_sigma=1000):
632-        """
633-        @param K: number of states
634-        @param D: dimensionality of output
635-        @param C: number of distinct classes for each dimension of output
636-        @param prior_sigma: parameter governing strength of prior. Prior on GLM weights is multivariate
637-        normal distribution with mean 'prior_mean' and diagonal covariance matrix (prior_sigma is on diagonal)
638-        """
639-        super(InputDrivenObservations, self).__init__(K, D, M)
640-        self.C = C
641-        self.M = M
642-        self.D = D
643-        self.K = K
644-        self.prior_mean = prior_mean
645-        self.prior_sigma = prior_sigma
646-        # Parameters linking input to distribution over output classes
647-        self.Wk = npr.randn(K, C - 1, M)
649-    @property
650-    def params(self):
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; cat > t2.py <<'EOF'
import remfile, h5py, requests, time, numpy as np
aid="4a81e0b6-6a51-453a-925f-e6084910ae54"
t=time.time()
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
for k in ['face_energy','post_hoc_pupil_diameter','running_speed']:
    d=f['acquisition'][k]['data']; print(k, d.chunks, d.compression)
    x=d[:]; ts=f['acquisition'][k]['timestamps'][:]
    print(k, x[:3], np.nanmin(x), np.nanmax(x), ts[:3], ts[-1], np.median(np.diff(ts)), time.time()-t)
m=f['general/metadata']
print(list(m.keys()), {k:m[k][()] for k in m.keys()}, dict(m.attrs))
print({k:f['general/subject'][k][()] for k in f['general/subject']}, f['session_start_time'][()], f['session_description'][()])
EOF
python t2.py
```

```
face_energy None None
face_energy [0.35208792 0.36311447 0.42195751] 0.26671625588034253 0.621083564526289 [32.020686 32.053597 32.125405] 7232.39336 0.03390899999976682 0.8864414691925049
post_hoc_pupil_diameter None None
post_hoc_pupil_diameter [29.64373767 29.6769057  29.69193166] 19.99567705790202 39.81097157796225 [32.020686 32.053597 32.125405] 7232.39336 0.03390899999976682 0.9948782920837402
running_speed None None
running_speed [4.414418 0.068033 0.075093] -0.085099 4.414418 [32.398187 32.40816  32.418134] 7139.974262 0.009973999999601801 1.1995384693145752
[] {} {'auditory_stim_association': 'low_band_left', 'behavior_version': 'multimodal_behavior_v20210816', 'namespace': 'uobrainflex_metadata', 'neurodata_type': 'LabMetaData_ext', 'object_id': '9cc9e457-0462-4b47-b809-d38a86dec78d', 'rig': 'Box 1', 'session_type': 'visual', 'training_stage': 'S5', 'visual_stim_association': 'horz_gabor_left'}
{'date_of_birth': b'2021-03-04T00:00:00-08:00', 'sex': b'F', 'species': b'Mus musculus', 'subject_id': b'BW041'} b'2021-08-30T13:05:49.532000-07:00' b'Behavior data. Two-alternative choice visual/auditory discrimination.'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040; sed -n 135,209p uobrainflex/nwb/loadbehavior.py | grep -v '^\s*$' | tail -25; grep -n "pupil_trace\|evoked\|kruskal\|iti\|ITI" hulsey2023/figure_generation_code/FigureS1.py | head -40
```

```
W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery
       Cambridge University Press ISBN-13: 9780521880688
    """
    import numpy as np
    from math import factorial
    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040/hulsey2023/figure_generation_code; sed -n 28,125p FigureS1.py; grep -n "kruskal" -B3 -A3 FigureS1.py
```

```
#step through data for each mouse
for m,hmm_trials_path in enumerate(list(folder.joinpath('hmm_trials').rglob('*hmm_trials*'))):
    hmm_trials_path = list(folder.joinpath('hmm_trials').rglob('*hmm_trials*'))[m]
    hmm_trials = np.load(hmm_trials_path, allow_pickle = True)
    if np.isnan(hmm_trials[0]['visual_stim_id'].iloc[0]):
        modality[m]=0
        
    start=[]
    evoked_up = []
    evoked_down = []
    hmm_state=[]
    iti=[]
    loc=[]
    face=[]
    # gather data on behavioral measures and ITI
    for trials in hmm_trials:
        for t, pupil in enumerate(trials['pupil_trace']):
            if len(pupil)>1000:
                start.append(pupil[1000])
                evoked_up.append(np.max(pupil[1000:1000+evoked_time_lim] - pupil[1000]))
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040/hulsey2023/data_processing_code; grep -v "^\s*#" 6_predictive_accuracy.py | grep -v "^\s*$" | head -120
```

```
Sat Oct 31 09:23:14 UTC 2026
import glob
import numpy as np
from sklearn.model_selection import StratifiedKFold
from uobrainflex.behavioranalysis import flex_hmm
import matplotlib.pyplot as plt
import ray
from sklearn import svm
base_folder = input("Enter the main directory path") + '\\'
hmm_trials_paths = glob.glob(base_folder + 'hmm_trials\\*hmm_trials.npy')
hmm_paths = glob.glob(base_folder + 'hmms\\*hmm.npy')
SVM = svm.SVC(probability = True)
all_measures = ['post_hoc_pupil_diameter','post_hoc_pupil_std10','face_energy','face_std_10','running_speed','running_std10']
def stratified_kFold_random_order(class_index,nKfold):
    n_class = len(np.unique(class_index))
    fold_index = np.full([n_class,nKfold],int)
    for i in range(n_class):
        fold_index[i,:]=np.random.permutation(range(nKfold))
    skf = StratifiedKFold(n_splits=nKfold)
    train_idx=[]
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040; sed -n 294,330p uobrainflex/behavioranalysis/flex_hmm.py; cd hulsey2023/data_processing_code; grep -v "^\s*#" 5_decoding.py | grep -v "^\s*$" | head -150
```

```
def choice_hmm_fit(subject, num_states, inpts, true_choices):
    ## Fit GLM-HMM with MAP estimation:
    # Set the parameters of the GLM-HMM
    obs_dim = true_choices[0].shape[1]          # number of observed dimensions
    num_categories = len(np.unique(np.concatenate(true_choices)))    # number of categories for output
    input_dim = inpts[0].shape[1]                                    # input dimensions

    # Instantiate GLM-HMM and set prior hyperparameters (MAP version)
    prior_sigma = 2
    prior_alpha = 2
    
    hmm = ssm.HMM(num_states, obs_dim, input_dim, observations="input_driven_obs", 
                         observation_kwargs=dict(C=num_categories,prior_sigma=prior_sigma),
                         transitions="sticky", transition_kwargs=dict(alpha=prior_alpha,kappa=0))
    
    N_iters = 1000
    fit_map_ll = hmm.fit(true_choices, inputs=inpts, method="em", num_iters=N_iters,
                                tolerance=10**-4)
    return hmm

[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/000678-hulsey-2024; cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040; sed -n 282,320p uobrainflex/nwb/loadbehavior.py | head -5; grep -n "behavior_events_keylist" -A3 uobrainflex/nwb/loadbehavior.py | head
```

```
def read_behavior_events(nwbFileObj, speriod=0.001, events=[]):
    """
    return behavioral events at input sampling precision from open nwb file.
    Args:
        nwbFileObj (object): an open nwbfile object.
13:behavior_events_keylist = ['reward_right','reward_left','licks_left','licks_right']
14-# ophys_acquisition_keylist = ['OnePhotonSeries_external']
15-
16-def get_file_path(subject, fileID):
--
233:        measures = list(set(keys).symmetric_difference(set(behavior_events_keylist)))        
234:        # measures = list(set(keys).symmetric_difference(set(behavior_events_keylist)).symmetric_difference(set(ophys_acquisition_keylist)))        
235-    
236-    # calculate number of periods to index with based on sample rate and length of longest measures data set
237-    max_time=np.full(len(measures),np.NaN)
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/000678-hulsey-2024/hulsey.py",
 "content": "\"\"\"Loading and measures for Hulsey et al. (2024) on dandiset 000678.\n\nHulsey, Zumwalt, Mazzucato, McCormick & Jaramillo (2024), \"Decision-making dynamics are\npredicted by arousal and uninstructed movements\", Cell Reports 43(1), 113709.\n\nWhere each parameter comes from:\n\n- Trial inputs and choices: the paper's code, uobrainflex at commit ef48985 (the claims file,\n  M1): ``loadbehavior.get_stim_vals`` for the stimulus value, and\n  ``flex_hmm.format_choice_behavior_hmm`` for the choice (left, right, none) and the removal of\n  distractor trials.\n- Measures at stimulus onset: ``loadbehavior.read_behavior_measures`` and\n  ``fetch_trial_beh_measures`` (claims file, M4; STAR Methods, \"Pupillometry, face motion energy\n  and locomotion\"): each series is put on a 1 ms grid at the rounded sample times, linearly\n  interpolated over gaps of up to 100 samples, filtered with a second-order Savitzky-Golay filter\n  of 201 samples (face, locomotion) or 501 samples (pupil) with the code's mirrored padding; face\n  motion energy is shifted to a minimum of 0 and divided by its maximum, pupil divided by its\n  maximum, locomotion kept raw and sign-flipped when its median is negative. The value of a trial\n  is the grid sample at round(stimulus_time / 1 ms). The 10-trial variability is\n  pandas ``rolling(10).std()`` over the session's target trials.\n- Evoked pupil response: FigureS1.py (claims file, figs1-iti-independence): from the pupil trace\n  at stimulus onset (the code's trace starts 999 samples before onset, so its sample 1000 is\n  onset + 1 ms) over 2500 samples, the larger in size of the largest rise and the largest fall.\n- Session inclusion: STAR Methods, \"Training and inclusion criteria\" (claims file,\n  cohort-inclusion).\n- GLM-HMM: ``fit_glmhmm`` reimplements the expectation-maximisation of the paper's ssm fork\n  (``hulsey2023/ssm_changes``) for the input-driven categorical observations: weights of shape\n  (K, C-1, M) with the last category (\"no response\") as reference, random normal initial\n  weights, transitions initialised at 0.95 I + 0.05 U(0, 1) normalised, uniform initial state\n  distribution, M-step of the weights by Newton's method on the expected log joint with the\n  Gaussian prior of standard deviation ``prior_sigma`` (1000 for MLE, 2 for MAP: ssm uses\n  ``prior_sigma ** 2`` as the variance), \"standard\" transitions (expected counts) or \"sticky\"\n  transitions with Dirichlet alpha 2 and kappa 0 (expected counts + alpha - 1), and stopping\n  when the log joint (log likelihood plus log prior, as ssm computes it) changes by less than\n  1e-4 or after 1000 iterations (2_n_states.py, 3_generate_hmms.py). A test log likelihood per\n  trial is ssm's ``log_probability``, which adds the log prior.\n\"\"\"\n\nfrom concurrent.futures import ThreadPoolExecutor\nimport json\nimport math\nimport urllib.request\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom numba import njit\n\nDANDISET = \"000678\"\nVERSION = \"0.231004.2146\"  # the version the paper cites (Key resources table)\nAPI = \"https://api.dandiarchive.org/api\"\n\nMEASURES = [\"post_hoc_pupil_diameter\", \"face_energy\", \"running_speed\"]\n# Savitzky-Golay windows in 1 ms samples, normalisation and zeroing (loadbehavior.read_behavior_measures)\nFILT = {\"face_energy\": 201, \"running_speed\": 201, \"post_hoc_pupil_diameter\": 501}\nNORM = {\"face_energy\": True, \"running_speed\": False, \"post_hoc_pupil_diameter\": True}\nZERO = {\"face_energy\": True, \"running_speed\": False, \"post_hoc_pupil_diameter\": False}\nEVOKED_SAMPLES = 2500  # FigureS1.py evoked_time_lim\n\n\ndef _get_json(url):\n    with urllib.request.urlopen(url) as r:\n        return json.load(r)\n\n\ndef list_assets(version=VERSION):\n    \"\"\"All assets of the pinned version, as a DataFrame with path, size, asset_id, subject.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000\"\n    rows = []\n    while url:\n        page = _get_json(url)\n        rows += page[\"results\"]\n        url = page[\"next\"]\n    df = pd.DataFrame(rows)[[\"path\", \"size\", \"asset_id\"]]\n    df[\"subject\"] = df[\"path\"].str.split(\"/\").str[0].str.replace(\"sub-\", \"\")\n    return df.sort_values(\"path\").reset_index(drop=True)\n\n\ndef version_metadata(version=VERSION):\n    return _get_json(f\"{API}/dandisets/{DANDISET}/versions/{version}/\")\n\n\ndef s3_url(asset_id):\n    req = urllib.request.Request(f\"{API}/assets/{asset_id}/download/\", method=\"HEAD\")\n    with urllib.request.urlopen(req) as r:\n        return r.url\n\n\ndef _maps(trials_group):\n    \"\"\"Code maps stored in the column descriptions ('... MAP:{...}'), as the code reads them.\"\"\"\n    maps = {}\n    for key in trials_group.attrs[\"colnames\"]:\n        desc = trials_group[key].attrs.get(\"description\", \"\")\n        if isinstance(desc, bytes):\n            desc = desc.decode()\n        if \"{\" in desc:\n            maps[key] = eval(desc[desc.find(\"{\"):])\n    return maps\n\n\ndef _savgol_code(y, window, order=2):\n    \"\"\"loadbehavior.savitzky_golay: convolution with mirrored-difference padding at the ends.\"\"\"\n    half = (window - 1) // 2\n    b = np.array([[k ** i for i in range(order + 1)] for k in range(-half, half + 1)], float)\n    m = np.linalg.pinv(b)[0]\n    first = y[0] - np.abs(y[1:half + 1][::-1] - y[0])\n    last = y[-1] + np.abs(y[-half - 1:-1][::-1] - y[-1])\n    return np.convolve(m[::-1], np.concatenate((first, y, last)), mode=\"valid\")\n\n\ndef _to_grid(ts, data, n):\n    \"\"\"Samples at round(t / 1 ms), linear interpolation, at most 100 consecutive filled samples\n    (pandas interpolate(limit=100), forward only).\"\"\"\n    grid = np.full(n, np.nan)\n    idx = np.round(ts / 0.001).astype(int)\n    keep = idx < n\n    grid[idx[keep]] = data[: len(idx)][keep]\n    valid = np.flatnonzero(~np.isnan(grid))\n    if len(valid) < 2:\n        return grid\n    out = np.interp(np.arange(n), valid, grid[valid])\n    # samples before the first valid one stay NaN; in gaps, only the first 100 are filled\n    out[: valid[0]] = np.nan\n    gaps = np.diff(valid) - 1\n    for g in np.flatnonzero(gaps > 100):\n        out[valid[g] + 101: valid[g + 1]] = np.nan\n    out[valid[-1] + 1:] = np.nan\n    return out\n\n\ndef load_session(asset_id, path):\n    \"\"\"One session: its target trials with inputs, choices and measures, plus session facts.\"\"\"\n    f = h5py.File(remfile.File(s3_url(asset_id)), \"r\")\n    meta = dict(f[\"general/metadata\"].attrs)\n    tg = f[\"intervals/trials\"]\n    maps = _maps(tg)\n    cols = [c for c in tg.attrs[\"colnames\"]]\n    tr = pd.DataFrame({c: tg[c][:] for c in cols})\n    acq = f[\"acquisition\"]\n    series = {}\n    for k in MEASURES:\n        if k in acq:\n            series[k] = (acq[k][\"timestamps\"][:], acq[k][\"data\"][:])\n    n_rew = {k: (acq[k][\"data\"].shape[0] if k in acq else 0) for k in [\"reward_left\", \"reward_right\"]}\n    subj = f[\"general/subject/subject_id\"][()].decode()\n    start = f[\"session_start_time\"][()].decode()\n    f.close()\n\n    # stimulus values (loadbehavior.get_stim_vals)\n    a_dir = tr[\"auditory_stim_id\"].map({maps[\"auditory_stim_id\"][\"left\"]: -1.0,\n                                        maps[\"auditory_stim_id\"][\"right\"]: 1.0}).astype(float)\n    a_val = tr[\"auditory_stim_difficulty\"].values\n    aud = a_dir.values * (a_val - (1 - a_val) / 2)\n    v_dir = tr[\"visual_stim_id\"].map({maps[\"visual_stim_id\"][\"left\"]: -1.0,\n                                      maps[\"visual_stim_id\"][\"right\"]: 1.0}).astype(float)\n    v_val = tr[\"visual_stim_difficulty\"].values\n    v_id = np.zeros(len(tr))\n    v_id[v_val == 1] = 0.8\n    v_id[v_val == 2] = 0.6\n    v_id[v_val == 0] = 1\n    vis = v_dir.values * v_id\n    tr[\"aud_stim\"], tr[\"vis_stim\"] = aud, vis\n    tr[\"stage\"] = meta.get(\"training_stage\")\n    distractor = maps[\"stimulus_type\"][\"distractor\"]\n    all_trials = tr.copy()\n\n    # target trials and choices (flex_hmm.format_choice_behavior_hmm)\n    t = tr[tr[\"stimulus_type\"] != distractor].copy()\n    modality = t[\"target_modality\"].iloc[0]\n    t[\"inpt\"] = t[\"aud_stim\"] if modality == maps[\"target_modality\"][\"auditory\"] else t[\"vis_stim\"]\n    hit, err, nores = (maps[\"outcome\"][k] for k in [\"hit\", \"miss\", \"incorrect_reject\"])\n    left, right = maps[\"target_port\"][\"left\"], maps[\"target_port\"][\"right\"]\n    ch = np.full(len(t), 2)\n    o, p = t[\"outcome\"].values, t[\"target_port\"].values\n    ch[(o == hit) & (p == left)] = 0\n    ch[(o == err) & (p == right)] = 0\n    ch[(o == hit) & (p == right)] = 1\n    ch[(o == err) & (p == left)] = 1\n    ch[o == nores] = 2\n    t[\"hmm_choice\"] = ch\n\n    # measures on the 1 ms grid (loadbehavior.read_behavior_measures, fetch_trial_beh_measures)\n    n = int(max(np.round(ts[-1] / 0.001) for ts, _ in series.values())) if series else 0\n    samp = np.round(t[\"stimulus_time\"].values / 0.001).astype(int)\n    for k in MEASURES:\n        if k not in series:\n            t[k] = np.nan\n            continue\n        g = _savgol_code(_to_grid(*series[k], n), FILT[k])\n        if NORM[k]:\n            if ZERO[k]:\n                g = g - np.nanmin(g)\n            g = g / np.nanmax(g)\n        if k == \"running_speed\" and np.nanmedian(g) < 0:\n            g = -g\n        ok = samp <= n - 1\n        vals = np.full(len(t), np.nan)\n        vals[ok] = g[samp[ok]]\n        t[k] = vals\n        if k == \"post_hoc_pupil_diameter\":\n            ev = np.full(len(t), np.nan)\n            for i, s in enumerate(samp):\n                seg = g[s + 1: s + 1 + EVOKED_SAMPLES]\n                if len(seg) == EVOKED_SAMPLES:\n                    up, down = np.max(seg - seg[0]), np.min(seg - seg[0])\n                    ev[i] = up if abs(up) >= abs(down) else down\n            t[\"evoked_pupil\"] = ev\n    t[\"post_hoc_pupil_std10\"] = t[\"post_hoc_pupil_diameter\"].rolling(10).std()\n    t[\"face_std_10\"] = t[\"face_energy\"].rolling(10).std()\n    t[\"running_std10\"] = t[\"running_speed\"].rolling(10).std()\n    t[\"trial_in_session\"] = np.arange(len(t))\n    info = dict(path=path, asset_id=asset_id, subject=subj, session_start=start,\n                stage=meta.get(\"training_stage\"), session_type=meta.get(\"session_type\"),\n                rig=meta.get(\"rig\"), behavior_version=meta.get(\"behavior_version\"),\n                modality=int(modality), n_trials_file=len(all_trials), n_target=len(t),\n                n_distractor=int((all_trials[\"stimulus_type\"] == distractor).sum()),\n                reward_left=n_rew[\"reward_left\"], reward_right=n_rew[\"reward_right\"],\n                has_pupil=(\"post_hoc_pupil_diameter\" in series),\n                pupil_n=len(series[\"post_hoc_pupil_diameter\"][0]) if \"post_hoc_pupil_diameter\" in series else 0,\n                face_n=len(series[\"face_energy\"][0]) if \"face_energy\" in series else 0,\n                run_n=len(series[\"running_speed\"][0]) if \"running_speed\" in series else 0,\n                run_raw_median=float(np.nanmedian(series[\"running_speed\"][1])) if \"running_speed\" in series else np.nan,\n                run_raw_p99=float(np.nanpercentile(series[\"running_speed\"][1], 99)) if \"running_speed\" in series else np.nan,\n                pupil_raw_median=float(np.nanmedian(series[\"post_hoc_pupil_diameter\"][1])) if \"post_hoc_pupil_diameter\" in series else np.nan,\n                face_rate=1 / np.median(np.diff(series[\"face_energy\"][0])) if \"face_energy\" in series else np.nan,\n                run_rate=1 / np.median(np.diff(series[\"running_speed\"][0])) if \"running_speed\" in series else np.nan,\n                last_sample_s=n / 1000)\n    all_trials[\"path\"] = path\n    t[\"path\"] = path\n    t[\"subject\"] = subj\n    return t, all_trials, info\n\n\ndef load_all(assets, workers=8):\n    \"\"\"Stream every session in parallel. Returns (target trials, all trials, sessions).\"\"\"\n    with ThreadPoolExecutor(workers) as ex:\n        res = list(ex.map(lambda r: load_session(r.asset_id, r.path), assets.itertuples()))\n    trials = pd.concat([r[0] for r in res], ignore_index=True)\n    alltr = pd.concat([r[1] for r in res], ignore_index=True)\n    sessions = pd.DataFrame([r[2] for r in res])\n    return trials, alltr, sessions\n"
}
```

```
File created successfully at: entries/000678-hulsey-2024/hulsey.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; uv pip install -q numba pyarrow 2>&1|tail -1; cd entries/000678-hulsey-2024; python -c "
import hulsey, time
t=time.time()
a=hulsey.list_assets(); print(len(a), time.time()-t)
tr,al,info=hulsey.load_session(a.asset_id[0],a.path[0]); print(time.time()-t)
print(info); print(tr.describe().T.to_string())
print(al.outcome.value_counts(), al.stimulus_type.value_counts(), al.visual_stim_difficulty.value_counts())
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    tr,al,info=hulsey.load_session(a.asset_id[0],a.path[0]); print(time.time()-t)
               ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/000678-hulsey-2024/hulsey.py", line 134, in load_session
    f = h5py.File(remfile.File(s3_url(asset_id)), "r")
                               ~~~~~~^^^^^^^^^^
  File "entries/000678-hulsey-2024/hulsey.py", line 86, in s3_url
    with urllib.request.urlopen(req) as r:
         ~~~~~~~~~~~~~~~~~~~~~~^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/urllib/request.py", line 189, in urlopen
    return opener.open(url, data, timeout)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/urllib/request.py", line 495, in open
    response = meth(req, response)
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/urllib/request.py", line 604, in http_response
    response = self.parent.error(
        'http', request, response, code, msg, hdrs)
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/urllib/request.py", line 527, in error
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; python - <<'EOF'
import re
s=open('hulsey.py').read()
s=s.replace('''def s3_url(asset_id):
    req = urllib.request.Request(f"{API}/assets/{asset_id}/download/", method="HEAD")
    with urllib.request.urlopen(req) as r:
        return r.url''','''def s3_url(asset_id):
    """The asset's S3 address, from its metadata (contentUrl)."""
    meta = _get_json(f"{API}/assets/{asset_id}/")
    return next(u for u in meta["contentUrl"] if "s3" in u)''')
open('hulsey.py','w').write(s)
EOF
cd $TMPDIR; . env/bin/activate; cd -; python -c "
import hulsey, time
t=time.time()
a=hulsey.list_assets(); print(len(a), time.time()-t)
tr,al,info=hulsey.load_session(a.asset_id[0],a.path[0]); print(time.time()-t)
print(info); print(tr.describe().T.to_string())
print(al.outcome.value_counts(), al.stimulus_type.value_counts(), al.visual_stim_difficulty.value_counts())
"
```

```
entries/000678-hulsey-2024
391 0.11256790161132812
2.6762595176696777
{'path': 'sub-BW041/sub-BW041_ses-20210830T130549.nwb', 'asset_id': '4a81e0b6-6a51-453a-925f-e6084910ae54', 'subject': 'BW041', 'session_start': '2021-08-30T13:05:49.532000-07:00', 'stage': 'S5', 'session_type': 'visual', 'rig': 'Box 1', 'behavior_version': 'multimodal_behavior_v20210816', 'modality': 1, 'n_trials_file': 885, 'n_target': 885, 'n_distractor': 0, 'reward_left': 68, 'reward_right': 138, 'has_pupil': True, 'pupil_n': 213620, 'face_n': 213620, 'run_n': 684228, 'run_raw_median': 0.0, 'run_raw_p99': 0.17019672999999996, 'pupil_raw_median': 29.23593209584554, 'face_rate': np.float64(29.49069568571402), 'run_rate': np.float64(100.26067776618444), 'last_sample_s': 7232.393}
                          count         mean          std          min          25%          50%          75%          max
start_time                885.0  3752.840658  2003.379025    44.304777  2089.994208  3806.887480  5471.677240  7135.192845
stop_time                 885.0  3754.981431  2003.526616    46.533989  2092.232410  3809.226271  5473.972308  7137.442830
target_modality           885.0     1.000000     0.000000     1.000000     1.000000     1.000000     1.000000     1.000000
cue_time                  885.0  3752.840658  2003.379025    44.304777  2089.994208  3806.887480  5471.677240  7135.192845
cue_ID                    885.0     0.000000     0.000000     0.000000     0.000000     0.000000     0.000000     0.000000
cue_duration              885.0     0.000000     0.000000     0.000000     0.000000     0.000000     0.000000     0.000000
stimulus_type             885.0     0.000000     0.000000     0.000000     0.000000     0.000000     0.000000     0.000000
stimulus_time             885.0  3752.841232  2003.379179    44.304777  2089.995208  3806.887480  5471.678237  7135.193842
stimulus_duration         885.0  1200.000000     0.000000  1200.000000  1200.000000  1200.000000  1200.000000  1200.000000
target_por
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; time python -c "
import hulsey, time
a=hulsey.list_assets()
tr,al,ss=hulsey.load_all(a, workers=12)
import os; d=os.environ['TMPDIR']
tr.to_pickle(d+'/tr.pkl'); al.to_pickle(d+'/al.pkl'); ss.to_pickle(d+'/ss.pkl')
print(len(tr), len(al), len(ss))
"
```

```
entries/000678-hulsey-2024/hulsey.py:194: RuntimeWarning: All-NaN slice encountered
  g = g / np.nanmax(g)
entries/000678-hulsey-2024/hulsey.py:225: RuntimeWarning: All-NaN slice encountered
  pupil_raw_median=float(np.nanmedian(series["post_hoc_pupil_diameter"][1])) if "post_hoc_pupil_diameter" in series else np.nan,
entries/000678-hulsey-2024/hulsey.py:194: RuntimeWarning: All-NaN slice encountered
  g = g / np.nanmax(g)
entries/000678-hulsey-2024/hulsey.py:225: RuntimeWarning: All-NaN slice encountered
  pupil_raw_median=float(np.nanmedian(series["post_hoc_pupil_diameter"][1])) if "post_hoc_pupil_diameter" in series else np.nan,
entries/000678-hulsey-2024/hulsey.py:194: RuntimeWarning: All-NaN slice encountered
  g = g / np.nanmax(g)
entries/000678-hulsey-2024/hulsey.py:225: RuntimeWarning: All-NaN slice encountered
  pupil_raw_median=float(np.nanmedian(series["post_hoc_pupil_diameter"][1])) if "post_hoc_pupil_diameter" in series else np.nan,
entries/000678-hulsey-2024/hulsey.py:194: RuntimeWarning: All-NaN slice encountered
  g = g / np.nanmax(g)
entries/000678-hulsey-2024/hulsey.py:225: RuntimeWarning: All-NaN slice encountered
  pupil_raw_median=float(np.nanmedian(series["post_hoc_pupil_diameter"][1])) if "post_hoc_pupil_diameter" in series else np.nan,
entries/000678-hulsey-2024/hulsey.py:194: RuntimeWarning: All-NaN slice encountered
  g = g / np.nanmax(g)
entries/000678-hulsey-2024/hulsey.py:194: RuntimeWarning: All-NaN slice encountered
  g = g / np.nanmax(g)
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python -c "
import pandas as pd, os, numpy as np
d=os.environ['TMPDIR']; ss=pd.read_pickle(d+'/ss.pkl'); al=pd.read_pickle(d+'/al.pkl'); tr=pd.read_pickle(d+'/tr.pkl')
pd.set_option('display.width',250)
print(ss.groupby('subject').agg(n=('path','size'),mod=('modality','first'),stages=('stage',lambda x: dict(x.value_counts())),stype=('session_type',lambda x: dict(x.value_counts())),pup=('has_pupil','sum'),pupnan=('pupil_raw_median',lambda x: x.isna().sum()), rew=('reward_left',lambda x:(x).min())).to_string())
ss['rew']=ss.reward_left+ss.reward_right; ss['minfrac']=np.minimum(ss.reward_left,ss.reward_right)/ss.rew
print(((ss.rew>=100)&(ss.minfrac>=0.2)).sum(), (ss.rew<100).sum(), (ss.minfrac<0.2).sum())
print(ss.run_raw_median.describe(), ss.run_raw_p99.describe(), ss.face_rate.describe(), ss.run_rate.describe())
print(ss.behavior_version.value_counts())
"
```

```
n  mod                stages             stype  pup  pupnan  rew
subject                                                                   
BW041    25    1  {'S5': 15, 'S6': 10}    {'visual': 25}   25       0   37
BW045    84    0  {'S6': 74, 'S5': 10}  {'auditory': 84}   84       1   35
BW046    34    1  {'S5': 18, 'S6': 16}    {'visual': 34}   34      14   35
BW048    35    1  {'S5': 20, 'S6': 15}    {'visual': 35}   35       0   36
BW051    35    1  {'S5': 25, 'S6': 10}    {'visual': 35}   35       4   58
BW053    32    0   {'S5': 23, 'S6': 9}  {'auditory': 32}   32       3   38
BW058    12    1            {'S5': 12}    {'visual': 12}   12       2  112
BW059    25    0   {'S5': 18, 'S6': 7}  {'auditory': 25}   25       5   44
BW061    23    0            {'S5': 23}  {'auditory': 23}   23       1   54
BW062    17    0            {'S5': 17}  {'auditory': 17}   17       4   27
BW064    21    0   {'S5': 12, 'S6': 9}  {'auditory': 21}   21       2   21
BW067    23    0            {'S5': 23}  {'auditory': 23}   23       0  105
BW071    25    0            {'S5': 25}  {'auditory': 25}   25       2   49
376 13 2
count    391.000000
mean       0.102143
std        0.110481
min       -0.244551
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; cat >> hulsey.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# GLM-HMM (reimplementation of the ssm fork's input-driven categorical HMM, fit by EM)
# ---------------------------------------------------------------------------------------------

@njit(cache=True)
def _forward_backward(log_pi0, P, loglik):
    """Scaled forward-backward for one sequence. Returns (gamma, xi_sum, marginal log lik)."""
    T, K = loglik.shape
    alpha = np.zeros((T, K))
    c = np.zeros(T)
    m = np.zeros(T)
    lik = np.zeros((T, K))
    for t in range(T):
        mx = loglik[t, 0]
        for k in range(1, K):
            if loglik[t, k] > mx:
                mx = loglik[t, k]
        m[t] = mx
        for k in range(K):
            lik[t, k] = math.exp(loglik[t, k] - mx)
    pi0 = np.exp(log_pi0 - np.max(log_pi0))
    pi0 = pi0 / pi0.sum()
    s = 0.0
    for k in range(K):
        alpha[0, k] = pi0[k] * lik[0, k]
        s += alpha[0, k]
    c[0] = s
    for k in range(K):
        alpha[0, k] /= s
    for t in range(1, T):
        s = 0.0
        for j in range(K):
            a = 0.0
            for i in range(K):
                a += alpha[t - 1, i] * P[i, j]
            alpha[t, j] = a * lik[t, j]
            s += alpha[t, j]
        c[t] = s
        for j in range(K):
            alpha[t, j] /= s
    beta = np.ones((T, K))
    xi = np.zeros((K, K))
    for t in range(T - 2, -1, -1):
        for i in range(K):
            b = 0.0
            for j in range(K):
                b += P[i, j] * lik[t + 1, j] * beta[t + 1, j]
            beta[t, i] = b / c[t + 1]
        for i in range(K):
            for j in range(K):
                xi[i, j] += alpha[t, i] * P[i, j] * lik[t + 1, j] * beta[t + 1, j] / c[t + 1]
    gamma = alpha * beta
    ll = 0.0
    for t in range(T):
        ll += math.log(c[t]) + m[t]
    return gamma, xi, ll


@njit(cache=True)
def _filter(log_pi0, P, loglik):
    """Filtered state probabilities p(z_t | y_1..t) for one sequence."""
    T, K = loglik.shape
    alpha = np.zeros((T, K))
    pi0 = np.exp(log_pi0 - np.max(log_pi0))
    pi0 = pi0 / pi0.sum()
    for t in range(T):
        lik = np.exp(loglik[t] - np.max(loglik[t]))
        if t == 0:
            a = pi0 * lik
        else:
            a = (alpha[t - 1] @ P) * lik
        alpha[t] = a / a.sum()
    return alpha


def _logits(W, X):
    """log p(y = c | z = k, x) for all trials: array (T, K, C). W is (K, C-1, M)."""
    eta = np.einsum("kcm,tm->tkc", W, X)
    eta = np.concatenate([eta, np.zeros(eta.shape[:2] + (1,))], axis=2)
    return eta - np.logaddexp.reduce(eta, axis=2, keepdims=True)


def _loglik(W, X, y):
    lg = _logits(W, X)
    return lg[np.arange(len(y)), :, y]


def _log_prior_obs(W, sigma):
    K, C1, M = W.shape
    return float(-0.5 * M * np.log(2 * np.pi) * K * C1 - M * np.log(sigma) * K * C1
                 - 0.5 * np.sum(W ** 2) / sigma ** 2)


def _log_prior_trans(P, sticky, alpha=2.0):
    return float(np.sum((alpha - 1) * np.log(P))) if sticky else 0.0


def _mstep_W(W, X, y, gamma, sigma, n_newton=20):
    """Maximise sum_t gamma_tk log p(y_t | z=k, x_t) + log N(W_k; 0, sigma^2) for each state."""
    K, C1, M = W.shape
    Y = np.zeros((len(y), C1 + 1))
    Y[np.arange(len(y)), y] = 1
    Y = Y[:, :C1]
    W = W.copy()
    for k in range(K):
        g = gamma[:, k]
        w = W[k].reshape(-1)
        for _ in range(n_newton):
            eta = X @ W[k].T  # (T, C1)
            eta = np.concatenate([eta, np.zeros((len(y), 1))], axis=1)
            p = np.exp(eta - np.logaddexp.reduce(eta, axis=1, keepdims=True))[:, :C1]
            r = (Y - p) * g[:, None]
            grad = (r.T @ X).reshape(-1) - w / sigma ** 2
            H = np.zeros((C1 * M, C1 * M))
            for a in range(C1):
                for b in range(C1):
                    wab = g * p[:, a] * ((a == b) - p[:, b])
                    H[a * M:(a + 1) * M, b * M:(b + 1) * M] = -(X * wab[:, None]).T @ X
            H -= np.eye(C1 * M) / sigma ** 2
            step = np.linalg.solve(H, grad)
            w = w - step
            W[k] = w.reshape(C1, M)
            if np.max(np.abs(step)) < 1e-8:
                break
    return W


class GLMHMM:
    """K-state GLM-HMM with categorical (C classes) emissions and inputs of dimension M."""

    def __init__(self, K, M=2, C=3, prior_sigma=1000.0, sticky=False, rng=None):
        rng = np.random.default_rng(rng)
        self.K, self.M, self.C = K, M, C
        self.prior_sigma, self.sticky = prior_sigma, sticky
        self.W = rng.standard_normal((K, C - 1, M))
        P = 0.95 * np.eye(K) + 0.05 * rng.random((K, K))
        self.P = P / P.sum(1, keepdims=True)
        self.log_pi0 = -np.log(K) * np.ones(K)

    def log_prior(self):
        return _log_prior_obs(self.W, self.prior_sigma) + _log_prior_trans(self.P, self.sticky)

    def _estep(self, Xs, ys):
        X = np.concatenate(Xs)
        ll_all = _loglik(self.W, X, np.concatenate(ys))
        out, start = [], 0
        for x in Xs:
            out.append(_forward_backward(self.log_pi0, self.P, ll_all[start:start + len(x)]))
            start += len(x)
        return out

    def log_likelihood(self, Xs, ys):
        X = np.concatenate(Xs)
        ll_all = _loglik(self.W, X, np.concatenate(ys))
        tot, start = 0.0, 0
        for x in Xs:
            tot += _forward_backward(self.log_pi0, self.P, ll_all[start:start + len(x)])[2]
            start += len(x)
        return tot

    def log_probability(self, Xs, ys):
        """ssm's HMM.log_probability: log likelihood plus log prior."""
        return self.log_likelihood(Xs, ys) + self.log_prior()

    def fit(self, Xs, ys, num_iters=1000, tolerance=1e-4):
        X, y = np.concatenate(Xs), np.concatenate(ys)
        lps = []
        for it in range(num_iters):
            ex = self._estep(Xs, ys)
            lp = sum(e[2] for e in ex) + self.log_prior()
            lps.append(lp)
            if it > 0 and abs(lps[-1] - lps[-2]) < tolerance:
                break
            # M-step
            pi0 = sum(e[0][0] for e in ex) + 1e-8
            self.log_pi0 = np.log(pi0 / pi0.sum())
            xi = sum(e[1] for e in ex)
            xi = xi + (1.0 if self.sticky else 1e-32)  # Dirichlet alpha 2 (sticky) adds alpha - 1
            self.P = xi / xi.sum(1, keepdims=True)
            gamma = np.concatenate([e[0] for e in ex])
            self.W = _mstep_W(self.W, X, y, gamma, self.prior_sigma)
        self.n_iter = it + 1
        self.lps = lps
        return lps

    def posteriors(self, Xs, ys):
        return [e[0] for e in self._estep(Xs, ys)]

    def permute(self, perm):
        perm = np.asarray(perm)
        self.W = self.W[perm]
        self.P = self.P[np.ix_(perm, perm)]
        self.log_pi0 = self.log_pi0[perm]


def fit_one(args):
    """Fit one GLM-HMM; args = (K, Xs_train, ys_train, Xs_test, ys_test, map, seed).
    Returns (model, train log prob per trial, test log prob per trial or nan)."""
    K, Xtr, ytr, Xte, yte, use_map, seed = args
    m = GLMHMM(K, prior_sigma=2.0 if use_map else 1000.0, sticky=use_map, rng=seed)
    lps = m.fit(Xtr, ytr)
    ntr = sum(len(x) for x in Xtr)
    test = np.nan
    if Xte is not None:
        test = m.log_probability(Xte, yte) / sum(len(x) for x in Xte)
    return m, lps[-1] / ntr, test


def plateau(ll, threshold=0.001):
    """3_generate_hmms.plateu: among state counts whose step raises the test log likelihood by
    more than the threshold, the one with the highest log likelihood. Returns the number of states."""
    ind = np.where(np.diff(ll) > threshold)[0]
    if len(ind) == 0:
        return 1
    return int(ind[np.argmax(ll[ind + 1])] + 1) + 1
EOF
python - <<'EOF'
import sys; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd, os, time
tr=pd.read_pickle(os.environ['TMPDIR']+'/tr.pkl')
m=tr[tr.subject=='BW046']
Xs=[np.c_[g.inpt.values, np.ones(len(g))] for _,g in m.groupby('path')]
ys=[g.hmm_choice.values.astype(int) for _,g in m.groupby('path')]
print(sum(len(x) for x in Xs), len(Xs))
for K in [1,2,4]:
    t=time.time(); mod,tr_ll,_=hulsey.fit_one((K,Xs,ys,None,None,False,0)); print(K, mod.n_iter, tr_ll, time.time()-t)
    t=time.time(); mod,tr_ll,_=hulsey.fit_one((K,Xs,ys,None,None,True,0)); print('map',K, mod.n_iter, tr_ll, time.time()-t)
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "entries/000678-hulsey-2024/hulsey.py", line 44, in <module>
    import h5py
ModuleNotFoundError: No module named 'h5py'
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import sys; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd, os, time
tr=pd.read_pickle(os.environ['TMPDIR']+'/tr.pkl')
m=tr[tr.subject=='BW046']
Xs=[np.c_[g.inpt.values, np.ones(len(g))] for _,g in m.groupby('path')]
ys=[g.hmm_choice.values.astype(int) for _,g in m.groupby('path')]
print(sum(len(x) for x in Xs), len(Xs))
for K in [1,2,4]:
    t=time.time(); mod,tr_ll,_=hulsey.fit_one((K,Xs,ys,None,None,False,0)); print(K, mod.n_iter, tr_ll, time.time()-t)
    t=time.time(); mod,tr_ll,_=hulsey.fit_one((K,Xs,ys,None,None,True,0)); print('map',K, mod.n_iter, tr_ll, time.time()-t)
EOF
```

```
14077 34
1 3 -0.7794469897438162 2.6012187004089355
map 1 3 -0.7777251018267629 0.02909255027770996
2 14 -0.5789403550927951 0.36428380012512207
map 2 14 -0.5765265270037891 0.370560884475708
4 106 -0.5011541231219826 4.722240209579468
map 4 107 -0.499687071793749 4.671206951141357
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
s=open('hulsey.py').read()
old_start=s.index('def _mstep_W(')
old_end=s.index('class GLMHMM:')
new_m='''def _mstep_W(W, U, counts, sigma, n_newton=50):
    """Maximise sum_t gamma_tk log p(y_t | z=k, x_t) + log N(W_k; 0, sigma^2 I) for each state
    by Newton's method. The inputs take few distinct values, so the expected counts
    counts[u, k, c] (summed posterior of state k over trials with input row U[u] and choice c)
    are sufficient."""
    K, C1, M = W.shape
    W = W.copy()
    for k in range(K):
        n = counts[:, k, :]  # (n_u, C)
        tot = n.sum(1)
        w = W[k].reshape(-1)
        for _ in range(n_newton):
            eta = U @ W[k].T
            eta = np.concatenate([eta, np.zeros((len(U), 1))], axis=1)
            p = np.exp(eta - np.logaddexp.reduce(eta, axis=1, keepdims=True))[:, :C1]
            r = n[:, :C1] - p * tot[:, None]
            grad = (r.T @ U).reshape(-1) - w / sigma ** 2
            H = np.zeros((C1 * M, C1 * M))
            for a in range(C1):
                for b in range(C1):
                    wab = tot * p[:, a] * ((a == b) - p[:, b])
                    H[a * M:(a + 1) * M, b * M:(b + 1) * M] = -(U * wab[:, None]).T @ U
            H -= np.eye(C1 * M) / sigma ** 2
            step = np.linalg.solve(H, grad)
            w = w - step
            W[k] = w.reshape(C1, M)
            if np.max(np.abs(step)) < 1e-10:
                break
    return W


'''
s=s[:old_start]+new_m+s[old_end:]
s=s.replace('''    def _estep(self, Xs, ys):
        X = np.concatenate(Xs)
        ll_all = _loglik(self.W, X, np.concatenate(ys))
        out, start = [], 0''','''    def _estep(self, Xs, ys, cache=None):
        if cache is None:
            cache = _unique_inputs(Xs, ys)
        U, ux, y = cache
        ll_all = _logits(self.W, U)[ux, :, y]
        out, start = [], 0''')
s=s.replace('''    def log_likelihood(self, Xs, ys):
        X = np.concatenate(Xs)
        ll_all = _loglik(self.W, X, np.concatenate(ys))''','''    def log_likelihood(self, Xs, ys):
        U, ux, y = _unique_inputs(Xs, ys)
        ll_all = _logits(self.W, U)[ux, :, y]''')
s=s.replace('''        X, y = np.concatenate(Xs), np.concatenate(ys)
        lps = []
        for it in range(num_iters):
            ex = self._estep(Xs, ys)''','''        cache = _unique_inputs(Xs, ys)
        U, ux, y = cache
        idx = ux * self.C + y
        lps = []
        for it in range(num_iters):
            ex = self._estep(Xs, ys, cache)''')
s=s.replace('''            gamma = np.concatenate([e[0] for e in ex])
            self.W = _mstep_W(self.W, X, y, gamma, self.prior_sigma)''','''            gamma = np.concatenate([e[0] for e in ex])
            counts = np.stack([np.bincount(idx, weights=gamma[:, k], minlength=len(U) * self.C)
                               for k in range(self.K)], axis=1).reshape(len(U), self.C, self.K)
            self.W = _mstep_W(self.W, U, counts.transpose(0, 2, 1), self.prior_sigma)''')
s=s.replace('''def _loglik(W, X, y):
    lg = _logits(W, X)
    return lg[np.arange(len(y)), :, y]''','''def _unique_inputs(Xs, ys):
    X = np.concatenate(Xs)
    U, ux = np.unique(X, axis=0, return_inverse=True)
    return U, ux.ravel(), np.concatenate(ys).astype(int).ravel()''')
open('hulsey.py','w').write(s)
EOF
python - <<'EOF'
import sys; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd, os, time
tr=pd.read_pickle(os.environ['TMPDIR']+'/tr.pkl')
m=tr[tr.subject=='BW046']
Xs=[np.c_[g.inpt.values, np.ones(len(g))] for _,g in m.groupby('path')]
ys=[g.hmm_choice.values.astype(int) for _,g in m.groupby('path')]
print(sum(len(x) for x in Xs), len(Xs))
for K in [1,2,4,7]:
    t=time.time(); mod,tr_ll,_=hulsey.fit_one((K,Xs,ys,None,None,False,0)); print(K, mod.n_iter, tr_ll, time.time()-t)
    t=time.time(); mod,tr_ll,_=hulsey.fit_one((K,Xs,ys,None,None,True,0)); print('map',K, mod.n_iter, tr_ll, time.time()-t)
print(np.round(mod.W,2), np.round(mod.P,3))
EOF
```

```
14077 34
1 3 -0.7794469897438164 2.185302495956421
map 1 3 -0.7777251018267629 0.012828826904296875
2 14 -0.5789403550927951 0.03986358642578125
map 2 14 -0.5765265270037893 0.0419466495513916
4 106 -0.5011541231219824 0.39144110679626465
map 4 107 -0.499687071793749 0.40280818939208984
7 116 -0.48925240727330455 1.0611672401428223
map 7 195 -0.492573514646563 1.2227256298065186
[[[-1.28  0.75]
  [ 0.44  3.84]]

 [[-2.56  5.2 ]
  [ 0.42  4.32]]

 [[-1.35 -2.83]
  [-0.23 -4.08]]

 [[-2.74  1.53]
  [-1.69 -2.34]]
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
s=open('hulsey.py').read()
s=s.replace('''    first = y[0] - np.abs(y[1:half + 1][::-1] - y[0])
    last = y[-1] + np.abs(y[-half - 1:-1][::-1] - y[-1])
    return np.convolve(m[::-1], np.concatenate((first, y, last)), mode="valid")''','''    first = y[0] - np.abs(y[1:half + 1][::-1] - y[0])
    last = y[-1] + np.abs(y[-half - 1:-1][::-1] - y[-1])
    z = np.concatenate((first, y, last))
    # np.convolve(m[::-1], z, "valid") computed by overlap-add; a NaN anywhere in the window
    # makes the output NaN, as np.convolve does
    bad = np.isnan(z)
    out = oaconvolve(np.where(bad, 0.0, z), m[::-1], mode="valid")
    out[oaconvolve(bad.astype(float), np.ones(window), mode="valid") > 0.5] = np.nan
    return out''')
s=s.replace("from numba import njit","from numba import njit\nfrom scipy.signal import oaconvolve\nimport hashlib")
s=s.replace('''    subj = f["general/subject/subject_id"][()].decode()''','''    subj = f["general/subject/subject_id"][()].decode()
    # fingerprints to find recordings deposited twice
    fp_face = hashlib.md5(series["face_energy"][1].tobytes()).hexdigest() if "face_energy" in series else ""
    fp_trials = hashlib.md5(tr[["stimulus_time", "outcome"]].values.tobytes()).hexdigest()''')
s=s.replace('''                last_sample_s=n / 1000)''','''                last_sample_s=n / 1000, fp_face=fp_face, fp_trials=fp_trials)''')
open('hulsey.py','w').write(s)
EOF
python - <<'EOF'
import sys,time; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd, os
a=hulsey.list_assets()
old=pd.read_pickle(os.environ['TMPDIR']+'/tr.pkl')
t=time.time()
tr,al,ss=hulsey.load_all(a.iloc[:16], workers=16)
print(time.time()-t)
o=old[old.path.isin(tr.path)]
for c in ['post_hoc_pupil_diameter','face_energy','running_speed','evoked_pupil','running_std10']:
    print(c, np.nanmax(np.abs(o[c].values-tr[c].values)), np.isnan(o[c].values).sum(), np.isnan(tr[c].values).sum())
EOF
```

```
22.47600269317627
post_hoc_pupil_diameter 1.3322676295501878e-15 7 7
face_energy 3.1086244689504383e-15 2 2
running_speed 1.6653345369377348e-16 5 5
evoked_pupil 1.3322676295501878e-15 25 25
running_std10 4.530397273964e-09 194 194
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import sys,time; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd, os
from concurrent.futures import ProcessPoolExecutor
a=hulsey.list_assets().iloc[16:48]
t=time.time()
with ProcessPoolExecutor(16) as ex:
    res=list(ex.map(hulsey.load_session, a.asset_id, a.path))
print(time.time()-t)
EOF
```

```
entries/000678-hulsey-2024/hulsey.py:205: RuntimeWarning: All-NaN slice encountered
  g = g / np.nanmax(g)
entries/000678-hulsey-2024/hulsey.py:236: RuntimeWarning: All-NaN slice encountered
  pupil_raw_median=float(np.nanmedian(series["post_hoc_pupil_diameter"][1])) if "post_hoc_pupil_diameter" in series else np.nan,
17.943523645401
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
s=open('hulsey.py').read()
s=s.replace('''def load_all(assets, workers=8):
    """Stream every session in parallel. Returns (target trials, all trials, sessions)."""
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(lambda r: load_session(r.asset_id, r.path), assets.itertuples()))''','''def load_all(assets, workers=16):
    """Stream every session in parallel. Returns (target trials, all trials, sessions)."""
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        with ProcessPoolExecutor(workers) as ex:
            res = list(ex.map(load_session, assets["asset_id"], assets["path"]))''')
s=s.replace("from concurrent.futures import ThreadPoolExecutor","from concurrent.futures import ProcessPoolExecutor")
s=s.replace('''        g = _savgol_code(_to_grid(*series[k], n), FILT[k])
        if NORM[k]:
            if ZERO[k]:
                g = g - np.nanmin(g)
            g = g / np.nanmax(g)''','''        g = _savgol_code(_to_grid(*series[k], n), FILT[k])
        if NORM[k] and np.isfinite(g).any():
            if ZERO[k]:
                g = g - np.nanmin(g)
            g = g / np.nanmax(g)''')
s=s.replace('''pupil_raw_median=float(np.nanmedian(series["post_hoc_pupil_diameter"][1])) if "post_hoc_pupil_diameter" in series else np.nan,''','''pupil_raw_median=float(np.nanmedian(series["post_hoc_pupil_diameter"][1])) if np.isfinite(series.get("post_hoc_pupil_diameter", (0, [np.nan]))[1]).any() else np.nan,''')
open('hulsey.py','w').write(s)
EOF
time python -c "
import sys; sys.path.insert(0,'.')
import hulsey, os
a=hulsey.list_assets()
tr,al,ss=hulsey.load_all(a)
d=os.environ['TMPDIR']
tr.to_pickle(d+'/tr.pkl'); al.to_pickle(d+'/al.pkl'); ss.to_pickle(d+'/ss.pkl')
print(len(tr), len(al), len(ss), ss.fp_face.duplicated().sum(), ss.fp_trials.duplicated().sum())
"; date -u
```

```
167948 214985 391 0 0

real	3m47.252s
user	10m43.908s
sys	3m57.950s
Sat Oct 31 09:37:45 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import pandas as pd, numpy as np, os
d=os.environ['TMPDIR']; ss=pd.read_pickle(d+'/ss.pkl'); al=pd.read_pickle(d+'/al.pkl'); tr=pd.read_pickle(d+'/tr.pkl')
ss['rew']=ss.reward_left+ss.reward_right; ss['minfrac']=np.minimum(ss.reward_left,ss.reward_right)/ss.rew
h=al[al.outcome==1].groupby('path').target_port.agg(hits='size', hl=lambda x:(x==0).sum())
ss=ss.merge(h,left_on='path',right_index=True,how='left')
ss['hfrac']=np.minimum(ss.hl,ss.hits-ss.hl)/ss.hits
a=(ss.rew>=100)&(ss.minfrac>=0.2); b=(ss.hits>=100)&(ss.hfrac>=0.2)
print(a.sum(), b.sum(), (a|b).sum(), (a&b).sum())
print(ss.loc[~a|~b, ['path','rew','minfrac','hits','hfrac','stage']].to_string())
print((ss.rew-ss.hits).describe())
print(al.groupby('stimulus_type').outcome.value_counts())
EOF
```

```
376 375 377 374
                                            path  rew   minfrac  hits     hfrac stage
6    sub-BW041/sub-BW041_ses-20210905T142058.nwb  341  0.108504   340  0.105882    S5
68   sub-BW045/sub-BW045_ses-20211108T091227.nwb   92  0.402174    93  0.397849    S6
78   sub-BW045/sub-BW045_ses-20211116T093954.nwb   99  0.383838    99  0.383838    S6
79   sub-BW045/sub-BW045_ses-20211117T085905.nwb   93  0.419355    93  0.419355    S6
81   sub-BW045/sub-BW045_ses-20211118T084349.nwb   98  0.459184    98  0.459184    S6
97   sub-BW045/sub-BW045_ses-20211211T141311.nwb   99  0.404040    99  0.404040    S6
129  sub-BW046/sub-BW046_ses-20211116T093954.nwb   87  0.402299    87  0.402299    S6
134  sub-BW046/sub-BW046_ses-20211122T113133.nwb   99  0.393939    99  0.393939    S6
223  sub-BW053/sub-BW053_ses-20211228T140451.nwb  220  0.195455   222  0.202703    S5
225  sub-BW053/sub-BW053_ses-20211231T155717.nwb   97  0.453608    97  0.453608    S5
238  sub-BW053/sub-BW053_ses-20220121T144423.nwb   97  0.391753    97  0.391753    S6
262  sub-BW059/sub-BW059_ses-20220220T101110.nwb  102  0.431373    97  0.402062    S5
315  sub-BW062/sub-BW062_ses-20220802T094351.nwb   66  0.409091    66  0.409091    S5
328  sub-BW064/sub-BW064_ses-20220714T114217.nwb   78  0.217949    78  0.217949    S5
341  sub-BW064/sub-BW064_ses-20220815T094736.nwb   86  0.302326    86  0.302326    S6
342  sub-BW064/sub-BW064_ses-20220816T102856.nwb   76  0.276316    76  0.276316    S6
373  sub-BW071/sub-BW071_ses-20220710T124035.nwb  150  0.486667    79  0.481013    S5
count    391.000000
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; cat >> hulsey.py <<'EOF'


def sequences(trials):
    """Per session (in session order): inputs [stimulus value, 1] and choices (0 left, 1 right,
    2 none), as flex_hmm.get_inpts_from_hmm_trials and get_true_choices_from_hmm_trials."""
    Xs, ys = [], []
    for _, g in trials.groupby("path", sort=True):
        Xs.append(np.c_[g["inpt"].values, np.ones(len(g))])
        ys.append(g["hmm_choice"].values.astype(int))
    return Xs, ys


def run_parallel(func, tasks, workers=None):
    import os
    workers = workers or os.cpu_count()
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(func, tasks, chunksize=1))


def cv_tasks(Xs, ys, n_init, seed, max_states=7, n_folds=5):
    """2_n_states.py: KFold over sessions (shuffled), states 1 to max_states, n_init random
    initialisations, MLE and MAP fits. Returns task list and their (fold, K, init, map) keys."""
    from sklearn.model_selection import KFold
    rng = np.random.default_rng(seed)
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=int(rng.integers(2**31)))
    tasks, keys = [], []
    for f, (tr_i, te_i) in enumerate(kf.split(np.arange(len(Xs)))):
        Xtr, ytr = [Xs[i] for i in tr_i], [ys[i] for i in tr_i]
        Xte, yte = [Xs[i] for i in te_i], [ys[i] for i in te_i]
        for K in range(1, max_states + 1):
            for z in range(n_init):
                for use_map in (False, True):
                    tasks.append((K, Xtr, ytr, Xte, yte, use_map, int(rng.integers(2**31))))
                    keys.append((f, K, z, use_map))
    return tasks, keys


def cv_test_ll(task):
    """Only the per-trial test log probability of one fit (keeps results small across processes)."""
    m, tr_ll, te_ll = fit_one(task)
    return tr_ll, te_ll, m.n_iter
EOF
cat > $TMPDIR/cv1.py <<'EOF'
import sys,time,os; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd
tr=pd.read_pickle(os.environ['TMPDIR']+'/tr.pkl')
m=tr[tr.subject==sys.argv[1]]
Xs,ys=hulsey.sequences(m)
t=time.time()
tasks,keys=hulsey.cv_tasks(Xs,ys,int(sys.argv[2]),0)
res=hulsey.run_parallel(hulsey.cv_test_ll,tasks)
print(len(m), len(tasks), time.time()-t, max(r[2] for r in res))
EOF
python $TMPDIR/cv1.py BW046 1
```

```
14077 70 42.79350924491882 1000
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF' 2>&1 | head -30
import sys,time,os; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd, cProfile, pstats
tr=pd.read_pickle(os.environ['TMPDIR']+'/tr.pkl')
m=tr[tr.subject=='BW046']
Xs,ys=hulsey.sequences(m)
hulsey.fit_one((2,Xs,ys,None,None,False,0))
cProfile.run("r=hulsey.fit_one((7,Xs,ys,None,None,False,3))",'/tmp/claude/prof' if False else os.environ['TMPDIR']+'/prof')
print(r[0].n_iter)
pstats.Stats(os.environ['TMPDIR']+'/prof').sort_stats('tottime').print_stats(12)
EOF
```

```
1000
Sat Oct 31 09:39:20 2026    /tmp/claude-1001/prof

         1379760 function calls in 6.621 seconds

   Ordered by: internal time
   List reduced from 101 to 12 due to restriction <12>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    3.576    0.004    3.647    0.004 entries/000678-hulsey-2024/hulsey.py:403(_estep)
     1000    1.491    0.001    2.358    0.002 entries/000678-hulsey-2024/hulsey.py:357(_mstep_W)
        1    0.462    0.462    6.620    6.620 entries/000678-hulsey-2024/hulsey.py:427(fit)
    21969    0.209    0.000    0.469    0.000 /tmp/claude-1001/env/lib/python3.13/site-packages/numpy/linalg/_linalg.py:374(solve)
    54940    0.152    0.000    0.152    0.000 {method 'reduce' of 'numpy.ufunc' objects}
    21970    0.069    0.000    0.093    0.000 /tmp/claude-1001/env/lib/python3.13/site-packages/numpy/lib/_twodim_base_impl.py:178(eye)
     3001    0.067    0.000    0.083    0.000 {built-in method builtins.sum}
    22970    0.049    0.000    0.097    0.000 /tmp/claude-1001/env/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:66(_wrapreduction)
    21969    0.046    0.000    0.094    0.000 /tmp/claude-1001/env/lib/python3.13/site-packages/numpy/linalg/_linalg.py:201(_commonType)
    66908    0.044    0.000    0.044    0.000 {built-in method numpy.zeros}
    51940    0.040    0.000    0.040    0.000 {method 'reshape' of 'numpy.ndarray' objects}
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; cat >> hulsey.py <<'EOF'


@njit(cache=True)
def _table(W, U):
    """log p(c | k, U[u]) as (n_u, K, C), the last class the reference."""
    K, C1, M = W.shape
    n_u = U.shape[0]
    out = np.zeros((n_u, K, C1 + 1))
    for u in range(n_u):
        for k in range(K):
            mx = 0.0
            for c in range(C1):
                e = 0.0
                for d in range(M):
                    e += W[k, c, d] * U[u, d]
                out[u, k, c] = e
                if e > mx:
                    mx = e
            s = math.exp(-mx)
            for c in range(C1):
                s += math.exp(out[u, k, c] - mx)
            lse = mx + math.log(s)
            for c in range(C1 + 1):
                out[u, k, c] -= lse
    return out


@njit(cache=True)
def _em(W, P, log_pi0, U, ux, y, starts, sigma, sticky, num_iters, tol):
    """EM as ssm's HMM.fit(method="em"): E-step, then M-step of the initial distribution,
    transitions and weights; stops when the log joint changes by less than tol."""
    K, C1, M = W.shape
    C = C1 + 1
    n_u = U.shape[0]
    n_seq = len(starts) - 1
    lps = np.zeros(num_iters)
    it_done = 0
    for it in range(num_iters):
        tab = _table(W, U)
        counts = np.zeros((n_u, K, C))
        xi_tot = np.zeros((K, K))
        pi_acc = np.zeros(K)
        ll_tot = 0.0
        for s in range(n_seq):
            a, b = starts[s], starts[s + 1]
            T = b - a
            lik = np.zeros((T, K))
            mloc = np.zeros(T)
            for t in range(T):
                mx = -1e300
                for k in range(K):
                    v = tab[ux[a + t], k, y[a + t]]
                    if v > mx:
                        mx = v
                mloc[t] = mx
                for k in range(K):
                    lik[t, k] = math.exp(tab[ux[a + t], k, y[a + t]] - mx)
            pi0 = np.exp(log_pi0 - np.max(log_pi0))
            pi0 /= pi0.sum()
            alpha = np.zeros((T, K))
            cs = np.zeros(T)
            ssum = 0.0
            for k in range(K):
                alpha[0, k] = pi0[k] * lik[0, k]
                ssum += alpha[0, k]
            cs[0] = ssum
            for k in range(K):
                alpha[0, k] /= ssum
            for t in range(1, T):
                ssum = 0.0
                for j in range(K):
                    acc = 0.0
                    for i in range(K):
                        acc += alpha[t - 1, i] * P[i, j]
                    alpha[t, j] = acc * lik[t, j]
                    ssum += alpha[t, j]
                cs[t] = ssum
                for j in range(K):
                    alpha[t, j] /= ssum
            beta = np.ones(K)
            nb = np.zeros(K)
            # gamma at T-1
            for k in range(K):
                g = alpha[T - 1, k]
                counts[ux[a + T - 1], k, y[a + T - 1]] += g
            if T == 1:
                for k in range(K):
                    pi_acc[k] += alpha[0, k]
            for t in range(T - 2, -1, -1):
                for i in range(K):
                    acc = 0.0
                    for j in range(K):
                        q = P[i, j] * lik[t + 1, j] * beta[j] / cs[t + 1]
                        xi_tot[i, j] += alpha[t, i] * q
                        acc += q
                    nb[i] = acc
                for k in range(K):
                    beta[k] = nb[k]
                    g = alpha[t, k] * beta[k]
                    counts[ux[a + t], k, y[a + t]] += g
                    if t == 0:
                        pi_acc[k] += g
            for t in range(T):
                ll_tot += math.log(cs[t]) + mloc[t]
        # log prior (ssm: Gaussian on each weight vector; Dirichlet on sticky transitions)
        lp = 0.0
        for k in range(K):
            for c in range(C1):
                sq = 0.0
                for d in range(M):
                    sq += W[k, c, d] ** 2
                lp += -0.5 * M * math.log(2 * math.pi) - M * math.log(sigma) - 0.5 * sq / sigma ** 2
        if sticky:
            for i in range(K):
                for j in range(K):
                    lp += math.log(P[i, j])
        lps[it] = ll_tot + lp
        it_done = it + 1
        if it > 0 and abs(lps[it] - lps[it - 1]) < tol:
            break
        # M-step
        pi_acc += 1e-8
        log_pi0 = np.log(pi_acc / pi_acc.sum())
        add = 1.0 if sticky else 1e-32
        for i in range(K):
            rs = 0.0
            for j in range(K):
                rs += xi_tot[i, j] + add
            for j in range(K):
                P[i, j] = (xi_tot[i, j] + add) / rs
        nprm = C1 * M
        for k in range(K):
            for newton in range(50):
                tabk = _table(W[k:k + 1], U)
                grad = np.zeros(nprm)
                H = np.zeros((nprm, nprm))
                for u in range(n_u):
                    tot = 0.0
                    for c in range(C):
                        tot += counts[u, k, c]
                    for c1 in range(C1):
                        p1 = math.exp(tabk[u, 0, c1])
                        r = counts[u, k, c1] - p1 * tot
                        for d in range(M):
                            grad[c1 * M + d] += r * U[u, d]
                        for c2 in range(C1):
                            p2 = math.exp(tabk[u, 0, c2])
                            wab = tot * p1 * ((1.0 if c1 == c2 else 0.0) - p2)
                            for d1 in range(M):
                                for d2 in range(M):
                                    H[c1 * M + d1, c2 * M + d2] -= wab * U[u, d1] * U[u, d2]
                for c1 in range(C1):
                    for d in range(M):
                        grad[c1 * M + d] -= W[k, c1, d] / sigma ** 2
                        H[c1 * M + d, c1 * M + d] -= 1.0 / sigma ** 2
                step = np.linalg.solve(H, grad)
                mstep = 0.0
                for c1 in range(C1):
                    for d in range(M):
                        W[k, c1, d] -= step[c1 * M + d]
                        if abs(step[c1 * M + d]) > mstep:
                            mstep = abs(step[c1 * M + d])
                if mstep < 1e-10:
                    break
    return W, P, log_pi0, lps[:it_done]


def _fit_fast(self, Xs, ys, num_iters=1000, tolerance=1e-4):
    U, ux, y = _unique_inputs(Xs, ys)
    starts = np.r_[0, np.cumsum([len(x) for x in Xs])].astype(np.int64)
    W, P, lp0, lps = _em(self.W.copy(), self.P.copy(), self.log_pi0.copy(), U.astype(float),
                         ux.astype(np.int64), y.astype(np.int64), starts, float(self.prior_sigma),
                         bool(self.sticky), num_iters, tolerance)
    self.W, self.P, self.log_pi0 = W, P, lp0
    self.n_iter = len(lps)
    self.lps = list(lps)
    return self.lps


GLMHMM.fit_slow = GLMHMM.fit
GLMHMM.fit = _fit_fast
EOF
python - <<'EOF'
import sys,time,os; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd
tr=pd.read_pickle(os.environ['TMPDIR']+'/tr.pkl')
m=tr[tr.subject=='BW046']
Xs,ys=hulsey.sequences(m)
hulsey.fit_one((2,Xs,ys,None,None,False,0))
for K,mp in [(4,False),(7,False),(4,True)]:
    a=hulsey.GLMHMM(K,prior_sigma=2.0 if mp else 1000.,sticky=mp,rng=3); b=hulsey.GLMHMM(K,prior_sigma=2.0 if mp else 1000.,sticky=mp,rng=3)
    t=time.time(); la=a.fit(Xs,ys); t1=time.time()-t; t=time.time(); lb=b.fit_slow(Xs,ys); t2=time.time()-t
    print(K, len(la), len(lb), la[-1], lb[-1], t1, t2, np.abs(a.W-b.W).max(), a.log_probability(Xs,ys))
EOF
```

```
4 123 123 -7054.746568622452 -7054.746568622446 0.19761896133422852 1.457646131515503 6.600497926001481e-12 -7054.746568622444
7 1000 1000 -6821.986401423908 -6821.986401423912 2.9559216499328613 6.0921361446380615 9.228973141262031e-11 -6821.966556560519
4 34 34 -6956.912370999867 -6956.91237099988 0.06006145477294922 0.14753293991088867 6.31494856406789e-13 -6956.912370999877
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
s=open('hulsey.py').read()
s=s.replace('''            for t in range(T - 2, -1, -1):
                for i in range(K):
                    acc = 0.0
                    for j in range(K):
                        q = P[i, j] * lik[t + 1, j] * beta[j] / cs[t + 1]''','''            v = np.zeros(K)
            for t in range(T - 2, -1, -1):
                for j in range(K):
                    v[j] = lik[t + 1, j] * beta[j] / cs[t + 1]
                for i in range(K):
                    acc = 0.0
                    for j in range(K):
                        q = P[i, j] * v[j]''')
open('hulsey.py','w').write(s)
EOF
python $TMPDIR/cv1.py BW046 1
```

```
14077 70 21.249181747436523 1000
```

**Agent calls Bash**

```bash
cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040/hulsey2023/figure_generation_code; sed -n 1,140p Figure2.py | grep -v "^\s*#" | grep -v "^\s*$"
```

```
import os
import numpy as np
import glob
import pandas as pd
from matplotlib.patches import Polygon
from scipy.stats import sem
from uobrainflex.behavioranalysis import flex_hmm
from matplotlib.patches import Rectangle
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Tahoma']
rcParams['font.size']= 15
rcParams['font.weight']= 'normal'
rcParams['axes.titlesize']= 15
rcParams['ytick.labelsize']= 15
rcParams['xtick.labelsize']= 15
import matplotlib.pyplot as plt
def pdur(val,dur):
     return (1-val)*val**(dur-1)    
def get_psychos(hmm_trials):  
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/uobrainflex-ef48985192e4af332c64f9d2e70ddcfc78659040/hulsey2023/figure_generation_code; sed -n 140,300p Figure2.py | grep -v "^\s*#" | grep -v "^\s*$" | grep -v "plt\.\|ax\.\|ax[0-9]\|set_\|fig\."
```

```
print('fixed with ' + str(state_similarity))
    all_state_similarity.append(state_similarity)
    for state in range(6):
        if len(all_trials.query('hmm_state==@state'))>0:
            if len(all_trials.query('hmm_state==@state'))>20:             
                lft_h = len(all_trials.query('hmm_state==@state and inpt<0 and choice==0'))/len(all_trials.query('hmm_state==@state and inpt<0'))
                lft_e = len(all_trials.query('hmm_state==@state and inpt<0 and choice==1'))/len(all_trials.query('hmm_state==@state and inpt<0'))
                lft_m = len(all_trials.query('hmm_state==@state and inpt<0 and choice==2'))/len(all_trials.query('hmm_state==@state and inpt<0'))
                rt_h = len(all_trials.query('hmm_state==@state and inpt>0 and choice==1'))/len(all_trials.query('hmm_state==@state and inpt>0'))
                rt_e = len(all_trials.query('hmm_state==@state and inpt>0 and choice==0'))/len(all_trials.query('hmm_state==@state and inpt>0'))
                rt_m = len(all_trials.query('hmm_state==@state and inpt>0 and choice==2'))/len(all_trials.query('hmm_state==@state and inpt>0'))
                lh[m,state_similarity[state]]=lft_h
                le[m,state_similarity[state]]=lft_e
                lm[m,state_similarity[state]]=lft_m
                rh[m,state_similarity[state]]=rt_h
                re[m,state_similarity[state]]=rt_e
                rm[m,state_similarity[state]]=rt_m
    occupancy=[]
    occupancy.append(len(np.where(all_trials['hmm_state']==0)[0])/len(all_trials))
    occupancy.append(len(np.where(all_trials['hmm_state']==1)[0])/len(all_trials))
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; cat >> hulsey.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# State selection, final model, state labels (2_n_states.py, 3_generate_hmms.py, flex_hmm,
# Figure2.py)
# ---------------------------------------------------------------------------------------------

def select_states(test_ll):
    """test_ll: (init, K, fold) per-trial test log probabilities. As 3_generate_hmms.py: mean over
    folds, best initialisation, then the plateau rule."""
    curve = np.nanmax(np.nanmean(test_ll, axis=2), axis=0)
    return plateau(curve), curve


def final_tasks(Xs, ys, K, n_init, seed):
    rng = np.random.default_rng(seed)
    return [(K, Xs, ys, None, None, False, int(rng.integers(2**31))) for _ in range(n_init)]


def posterior_states(model, trials, occ_thresh=0.8):
    """flex_hmm.get_posterior_probs: posterior of each state per trial, and the state when its
    posterior is at least occ_thresh (NaN, indeterminate, otherwise)."""
    Xs, ys = sequences(trials)
    post = np.concatenate(model.posteriors(Xs, ys))
    order = trials.sort_values(["path", "trial_in_session"]).index
    out = pd.DataFrame(index=order)
    st = np.argmax(post, axis=1).astype(float)
    st[np.max(post, axis=1) < occ_thresh] = np.nan
    out["hmm_state"] = st
    for k in range(post.shape[1]):
        out[f"state_{k + 1}_prob"] = post[:, k]
    return out.loc[trials.index]


def psychos(trials, states):
    """flex_hmm.get_psychos: P(choice | state, input) for discrete states (state, choice, input)."""
    inp = np.unique(trials["inpt"])
    K = int(np.nanmax(states)) + 1
    ps = np.full((K, 3, len(inp)), np.nan)
    for k in range(K):
        sel = states == k
        for j, x in enumerate(inp):
            n = np.sum(sel & (trials["inpt"].values == x))
            if n > 0:
                for c in range(3):
                    ps[k, c, j] = np.sum(sel & (trials["inpt"].values == x) & (trials["hmm_choice"].values == c)) / n
    return ps, inp


def permutation_optimal_disengaged(ps):
    """flex_hmm.permute_hmm: state nearest a perfect psychometric first, nearest all no-response
    second (sum of absolute differences over inputs without missing values), others after."""
    perfect = np.zeros((2, ps.shape[1], ps.shape[2]))
    perfect[0, 0, : int(ps.shape[2] / 2)] = 1
    perfect[0, 1, int(ps.shape[2] / 2):] = 1
    perfect[1, 2, :] = 1
    miss = np.unique(np.where(ps != ps)[2])
    p1, p2 = np.delete(perfect, miss, axis=2), np.delete(ps, miss, axis=2)
    sim = np.array([[np.sum(np.abs(s - t)) for t in p1] for s in p2])
    perm = np.nanargmin(sim, axis=0)
    if len(perm) < ps.shape[0]:
        perm = np.append(perm, np.delete(np.arange(ps.shape[0]), perm))
    if len(np.unique(perm)) != len(perm):
        best = np.nanargmin(sim[:, 0])
        perm = np.concatenate(([best], np.delete(np.arange(sim.shape[0]), best)))
    return perm


STATE_NAMES = ["optimal", "disengaged", "bias left", "avoid right", "bias right", "avoid left"]


def sort_templates():
    """Figure2.py sort_psychos: (template, choice, 6 inputs)."""
    s = np.zeros([6, 3, 6])
    s[0, 0, :3] = 1
    s[0, 1, 3:] = 1
    s[1, 2, :] = 1
    s[2, 0, :] = 1
    s[3, 0, :3] = 1
    s[3, 2, 3:] = 1
    s[4, 1, :] = 1
    s[5, 1, 3:] = 1
    s[5, 2, :3] = 1
    return s


def state_types(ps):
    """Figure2.py: each state's nearest template (nansum of absolute differences), with the
    code's loop resolving states assigned the same template. ps must have 6 inputs."""
    if ps.shape[2] == 8:
        bad = np.unique(np.where(ps != ps)[-1])
        ps = np.delete(ps, bad, axis=2)
    if ps.shape[2] == 8:
        ps = np.delete(ps, [1, 6], axis=2)
    tmpl = sort_templates()
    sim = np.array([[np.nansum(np.abs(s - t)) for t in tmpl] for s in ps])
    lab = np.nanargmin(sim, axis=1)
    guard = 0
    while len(np.unique(lab)) != len(lab) and guard < 100:
        vals, counts = np.unique(lab, return_counts=True)
        for v in vals[counts > 1]:
            idx = np.where(lab == v)[0]
            worst = idx[np.argmax(sim[idx, v])]
            lab[worst] = np.argsort(sim[worst])[1]
        guard += 1
    return lab, sim
EOF
cat > $TMPDIR/cvall.py <<'EOF'
import sys,time,os; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd, pickle
d=os.environ['TMPDIR']
tr=pd.read_pickle(d+'/tr.pkl'); ss=pd.read_pickle(d+'/ss.pkl')
ss['rew']=ss.reward_left+ss.reward_right
inc=ss[(ss.rew>=100)&(np.minimum(ss.reward_left,ss.reward_right)/ss.rew>=0.2)&ss.stage.isin(['S5','S6'])]
tr=tr[tr.path.isin(inc.path)]
out={}
t0=time.time()
tasks_all=[];keys_all=[]
for i,(subj,g) in enumerate(sorted(tr.groupby('subject'))):
    Xs,ys=hulsey.sequences(g)
    tasks,keys=hulsey.cv_tasks(Xs,ys,2,1000+i)
    tasks_all+=tasks; keys_all+=[(subj,)+k for k in keys]
# biggest first
order=np.argsort([-sum(len(x) for x in t[1])*t[0] for t in tasks_all])
res=hulsey.run_parallel(hulsey.cv_test_ll,[tasks_all[j] for j in order])
resd={keys_all[j]:r for j,r in zip(order,res)}
pickle.dump(resd,open(d+'/cv.pkl','wb'))
print(time.time()-t0)
EOF
time python $TMPDIR/cvall.py; date -u
```

```
184.15264773368835

real	3m6.291s
user	12m6.569s
sys	0m2.207s
Sat Oct 31 09:44:24 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import sys,os,pickle; sys.path.insert(0,'.')
import hulsey, numpy as np
d=os.environ['TMPDIR']; r=pickle.load(open(d+'/cv.pkl','rb'))
subs=sorted(set(k[0] for k in r))
for s in subs:
    row=[]
    for mp in (False,True):
        a=np.full((2,7,5),np.nan)
        for (sb,f,K,z,m),v in r.items():
            if sb==s and m==mp: a[z,K-1,f]=v[1]
        n,curve=hulsey.select_states(a)
        row.append((n,np.round(curve,4)))
    iters=[v[2] for k,v in r.items() if k[0]==s]
    print(s, row[0][0], row[1][0], row[0][1], row[1][1], np.mean(np.array(iters)==1000))
EOF
```

```
BW041 4 3 [-6.30155278e+09 -4.86700000e-01 -4.81000000e-01 -4.36100000e-01
 -4.45300000e-01 -4.56100000e-01 -4.69300000e-01] [-1.4379856e+04 -4.7120000e-01 -4.0970000e-01 -4.2280000e-01
 -4.4030000e-01 -4.6260000e-01 -4.8920000e-01] 0.02142857142857143
BW045 4 4 [-6.28511003e+09 -6.41300000e-01 -6.11000000e-01 -5.93700000e-01
 -5.92900000e-01 -5.97100000e-01 -6.01100000e-01] [-5.11653183e+04 -6.33500000e-01 -6.01800000e-01 -5.87200000e-01
 -5.89900000e-01 -5.99400000e-01 -6.14200000e-01] 0.014285714285714285
BW046 4 4 [-5.11040121e+09 -6.00500000e-01 -5.66300000e-01 -5.40500000e-01
 -5.44100000e-01 -5.57100000e-01 -5.64600000e-01] [-3.4356929e+03 -7.4106717e+03 -5.5320000e-01 -5.3070000e-01
 -5.4510000e-01 -5.6300000e-01 -5.8920000e-01] 0.02857142857142857
BW048 5 5 [-6.38324738e+09 -6.13600000e-01 -5.56400000e-01 -5.40500000e-01
 -5.34200000e-01 -5.40800000e-01 -5.47200000e-01] [-2.46349446e+04 -5.90800000e-01 -5.52300000e-01 -5.29200000e-01
 -5.27900000e-01 -5.45000000e-01 -5.66100000e-01] 0.007142857142857143
BW051 4 3 [-5.45037494e+09 -5.52200000e-01 -5.40500000e-01 -5.34000000e-01
 -5.44800000e-01 -5.53700000e-01 -5.61100000e-01] [-1.23131542e+04 -5.38800000e-01 -5.26600000e-01 -5.27600000e-01
 -5.40300000e-01 -5.61400000e-01 -5.82500000e-01] 0.02857142857142857
BW053 3 4 [-5.42274413e+09 -6.98000000e-01 -6.86000000e-01 -6.87500000e-01
 -6.92900000e-01 -7.00400000e-01 -7.13000000e-01] [-2.16915204e+04 -6.82300000e-01 -1.54779620e+03 -6.74100000e-01
 -6.81800000e-01 -7.07500000e-01 -7.36700000e-01] 0.04285714285714286
BW058 4 3 [-2.21660673e+09 -6.56800000e-01 -6.54300000e-01 -6.36500000e-01
 -6.64300000e-01 -6.90600000e-01 -7.20400000e-01] [-4.5346876e+03 -6.2430000e-01 -6.0950000e-01 -6.1080000e-01
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import sys,time,os; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd
tr=pd.read_pickle(os.environ['TMPDIR']+'/tr.pkl')
m=tr[tr.subject=='BW046']
Xs,ys=hulsey.sequences(m)
for seed in range(3):
    a=hulsey.GLMHMM(1,rng=seed); l=a.fit(Xs,ys); print(l, a.W, a.P, a.log_pi0, a.log_likelihood(Xs,ys), a.log_prior())
EOF
```

```
[np.float64(-14813.289970540845), np.float64(-10972.275274622643), np.float64(-10972.275274622643)] [[[-1.42078506  1.33984948]
  [ 0.37572109  1.00117543]]] [[1.]] [0.] -10940.968496896285 -31.306777727419938
[np.float64(-19403.945943855364), np.float64(-149222644620031.3), np.float64(-149222644620031.3)] [[[-3.3294e+09  7.0440e+09]
  [ 2.7384e+09 -8.7120e+09]]] [[1.]] [0.] -77172335160000.0 -72050309460031.31
[np.float64(-26005.617852723095), np.float64(-149222644620031.3), np.float64(-149222644620031.3)] [[[-3.3294e+09  7.0440e+09]
  [ 2.7384e+09 -8.7120e+09]]] [[1.]] [0.] -77172335160000.0 -72050309460031.31
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
s=open('hulsey.py').read()
s=s.replace('''@njit(cache=True)
def _em(''','''@njit(cache=True)
def _obj_k(Wk, U, cnt, sigma):
    """Expected complete-data log likelihood of one state's weights plus its log prior."""
    tab = _table(Wk, U)
    f = 0.0
    for u in range(U.shape[0]):
        for c in range(cnt.shape[1]):
            if cnt[u, c] > 0:
                f += cnt[u, c] * tab[u, 0, c]
    f -= 0.5 * np.sum(Wk ** 2) / sigma ** 2
    return f


@njit(cache=True)
def _em(''')
s=s.replace('''                step = np.linalg.solve(H, grad)
                mstep = 0.0
                for c1 in range(C1):
                    for d in range(M):
                        W[k, c1, d] -= step[c1 * M + d]
                        if abs(step[c1 * M + d]) > mstep:
                            mstep = abs(step[c1 * M + d])
                if mstep < 1e-10:
                    break''','''                step = np.linalg.solve(H, grad)
                # Newton step, halved until the objective does not decrease (damped Newton)
                Wk = W[k:k + 1].copy()
                f0 = _obj_k(Wk, U, counts[:, k, :], sigma)
                scale = 1.0
                for _ in range(60):
                    Wn = Wk.copy()
                    for c1 in range(C1):
                        for d in range(M):
                            Wn[0, c1, d] -= scale * step[c1 * M + d]
                    if _obj_k(Wn, U, counts[:, k, :], sigma) >= f0 - 1e-12:
                        break
                    scale *= 0.5
                W[k] = Wn[0]
                mstep = scale * np.max(np.abs(step))
                if mstep < 1e-10:
                    break''')
open('hulsey.py','w').write(s)
EOF
python - <<'EOF'
import sys,time,os; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd
tr=pd.read_pickle(os.environ['TMPDIR']+'/tr.pkl')
m=tr[tr.subject=='BW046']
Xs,ys=hulsey.sequences(m)
for seed in range(3):
    a=hulsey.GLMHMM(1,rng=seed); l=a.fit(Xs,ys); print(l[-1], a.W.ravel())
for K in (4,7):
  for seed in range(3):
    a=hulsey.GLMHMM(K,rng=seed); t=time.time(); l=a.fit(Xs,ys); print(K,l[-1], len(l), time.time()-t)
EOF
```

```
-10972.275274622643 [-1.42078506  1.33984948  0.37572109  1.00117543]
-10972.275274622643 [-1.42078506  1.33984948  0.37572109  1.00117543]
-10972.275274622643 [-1.42078506  1.33984948  0.37572109  1.00117543]
4 -7054.746591187938 106 0.1700730323791504
4 -6979.392114068811 58 0.0964815616607666
4 -6979.384138164381 46 0.07816243171691895
7 -6887.2061371848295 116 0.32081127166748047
7 -6805.426872023966 394 1.049687385559082
7 -6802.604463916352 565 1.5270001888275146
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; sed -i 's/hulsey.cv_tasks(Xs,ys,2,1000+i)/hulsey.cv_tasks(Xs,ys,3,1000+i)/' $TMPDIR/cvall.py; time python $TMPDIR/cvall.py; python - <<'EOF'
import sys,os,pickle; sys.path.insert(0,'.')
import hulsey, numpy as np
d=os.environ['TMPDIR']; r=pickle.load(open(d+'/cv.pkl','rb'))
subs=sorted(set(k[0] for k in r))
for s in subs:
    row=[]
    for mp in (False,True):
        a=np.full((3,7,5),np.nan)
        for (sb,f,K,z,m),v in r.items():
            if sb==s and m==mp: a[z,K-1,f]=v[1]
        n,curve=hulsey.select_states(a)
        row.append((n,np.round(curve,4)))
    iters=[v[2] for k,v in r.items() if k[0]==s]
    print(s, row[0][0], row[1][0], row[0][1], row[1][1], np.mean(np.array(iters)==1000))
EOF
date -u
```

```
234.93692421913147

real	3m57.019s
user	15m28.487s
sys	0m1.635s
BW041 3 3 [-0.7073 -0.4867 -0.4242 -0.4327 -0.4442 -0.4553 -0.4686] [-0.6968 -0.4712 -0.4097 -0.4221 -0.4404 -0.4632 -0.4896] 0.0
BW045 4 4 [-0.8578 -0.6413 -0.611  -0.5937 -0.5935 -0.5963 -0.6014] [-0.8525 -0.6335 -0.6018 -0.5908 -0.5899 -0.5999 -0.6145] 0.004761904761904762
BW046 4 4 [-0.7908 -0.6005 -0.5691 -0.5402 -0.5467 -0.554  -0.5639] [-0.782  -0.588  -0.5553 -0.5307 -0.5437 -0.5645 -0.5869] 0.01904761904761905
BW048 5 4 [-0.7076 -0.6036 -0.559  -0.5389 -0.5328 -0.5395 -0.5477] [-0.6989 -0.5908 -0.5431 -0.5268 -0.5269 -0.5429 -0.5653] 0.0
BW051 3 3 [-0.6512 -0.5522 -0.5334 -0.5348 -0.543  -0.5518 -0.5621] [-0.6425 -0.5388 -0.5221 -0.5274 -0.5412 -0.5605 -0.5811] 0.009523809523809525
BW053 4 3 [-0.908  -0.698  -0.6889 -0.6854 -0.6873 -0.6974 -0.7122] [-0.8973 -0.6823 -0.6676 -0.674  -0.681  -0.7047 -0.737 ] 0.004761904761904762
BW058 4 4 [-0.8038 -0.6568 -0.6392 -0.636  -0.6618 -0.6868 -0.7192] [-0.7803 -0.6243 -0.6164 -0.6108 -0.656  -0.7045 -0.7566] 0.009523809523809525
BW059 4 3 [-0.7503 -0.6729 -0.6472 -0.6446 -0.6517 -0.6531 -0.6626] [-0.7409 -0.6579 -0.6295 -0.6321 -0.6439 -0.6632 -0.6882] 0.004761904761904762
BW061 3 3 [-1.0153 -0.7655 -0.6686 -0.6723 -0.676  -0.6832 -0.6854] [-1.0063 -0.7524 -0.6554 -0.6571 -0.68   -0.6999 -0.7263] 0.0
BW062 3 3 [-0.8491 -0.7061 -0.6694 -0.6747 -0.6816 -0.69   -0.7038] [-0.8381 -0.691  -0.6553 -0.6642 -0.6815 -0.7046 -0.7332] 0.009523809523809525
BW064 3 3 [-0.98   -0.9033 -0.8807 -0.892  -0.913  -0.932  -0.9563] [-0.9612 -0.8711 -0.8422 -0.8553 -0.887  -0.9272 -0.9691] 0.004761904761904762
BW067 4 3 [-0.95   -0.7672 -0.6886 -0.6846 -0.6859 -0.6903 -0.6983] [-0.9408 -0.7521 -0.672  -0.6735 -0.6799 -0.6979 -0.7208] 0.009523809523809525
BW071 4 3 [-0.8312 -0.553  -0.5342 -0.5307 -0.5304 -0.5405 -0.5518] [-0.8207 -0.5381 -0.5205 -0.5232 -0.5315 -0.5556 -0.584 ] 0.0
Sat Oct 31 09:49:09 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; cat > $TMPDIR/final.py <<'EOF'
import sys,time,os,pickle; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd
d=os.environ['TMPDIR']
tr=pd.read_pickle(d+'/tr.pkl'); ss=pd.read_pickle(d+'/ss.pkl')
ss['rew']=ss.reward_left+ss.reward_right
inc=ss[(ss.rew>=100)&(np.minimum(ss.reward_left,ss.reward_right)/ss.rew>=0.2)&ss.stage.isin(['S5','S6'])]
tr=tr[tr.path.isin(inc.path)].copy()
r=pickle.load(open(d+'/cv.pkl','rb'))
subs=sorted(tr.subject.unique())
nst={}
for s in subs:
    a=np.full((3,7,5),np.nan)
    for (sb,f,K,z,m),v in r.items():
        if sb==s and not m: a[z,K-1,f]=v[1]
    nst[s]=hulsey.select_states(a)[0]
t0=time.time()
tasks=[];own=[]
for i,s in enumerate(subs):
    Xs,ys=hulsey.sequences(tr[tr.subject==s])
    tt=hulsey.final_tasks(Xs,ys,nst[s],10,2000+i); tasks+=tt; own+=[s]*len(tt)
res=hulsey.run_parallel(hulsey.fit_one,tasks)
print(time.time()-t0)
models={}
for s in subs:
    rr=[res[j] for j in range(len(res)) if own[j]==s]
    models[s]=rr[int(np.argmax([x[1] for x in rr]))][0]
pickle.dump((nst,models),open(d+'/final.pkl','wb'))
EOF
python $TMPDIR/final.py
```

```
6.477055788040161
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -o z.json https://zenodo.org/api/records/10306018; python -c "
import json; r=json.load(open('z.json')); print([ (f['key'],f['size'],f['links']['self']) for f in r['files']])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -o hz.zip https://zenodo.org/api/records/10306018/files/hulsey2023.zip/content; mkdir -p hz; cd hz; unzip -q -o ../hz.zip; find . -name "*.py" | grep -i "figure\|_" | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/hz/hulsey2023/hulsey2023_analysis; grep -v "^\s*#" data_processing_code/4_optimal_pupils.py | grep -v "^\s*$" | grep -v "plt\.\|ax\.\|set_\|fig\." | head -150
```

```
import numpy as np
import glob
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import KFold
import math
a = '#679292'
b ='#c41111'
c ='#ffc589'
d ='#ffa51e'
e ='#f26c2a'
f = '#ec410d'
cols = [a,b,c,d,e,f]
base_folder = input("Enter the main directory path") + '\\'
hmm_trials_paths = glob.glob(base_folder + 'hmm_trials\\*hmm_trials.npy')
max_degree = 7
nKfold = 5
rsqs= np.full([len(hmm_trials_paths),max_degree,nKfold],np.nan)
step = .02
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hz/hulsey2023/hulsey2023_analysis/figure_generation_code; grep -v "^\s*#" Figure3.py | grep -v "^\s*$" | grep -v "plt\.\|ax\.\|ax[0-9]*\[\|set_\|fig\.\|rcParams\|^[a-f] =" | sed -n 1,260p
```

```
import os
import numpy as np
import glob
import pandas as pd
from matplotlib.patches import Polygon
from scipy.stats import sem
from uobrainflex.nwb import loadbehavior as load
from uobrainflex.behavioranalysis import flex_hmm
import scipy
from matplotlib.patches import Rectangle
from scipy import stats 
cols = [a,b,c,d,e,f,'k','k','k','k','k','k','k','k']
import matplotlib.pyplot as plt
base_folder = input("Enter the main directory path") + '\\'
hmm_trials_paths = glob.glob(base_folder + 'hmm_trials\\*hmm_trials.npy')
ax=[]
face_file = base_folder +'images\\mouse_face_annotated.png'
m=6
subject = os.path.basename(hmm_trials_paths[m])[:5]
hmm_trials = np.load(hmm_trials_paths[m],allow_pickle=True)
[... 238 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hz/hulsey2023/hulsey2023_analysis/figure_generation_code; grep -v "^\s*#" Figure4.py | grep -v "^\s*$" | grep -v "plt\.\|ax\.\|ax[0-9]*\[\|set_\|fig\.\|rcParams\|^[a-f] =\|spine\|tick\|label" | sed -n 1,200p
```

```
import os
import numpy as np
import glob
import pandas as pd
from scipy import stats
from uobrainflex.behavioranalysis import flex_hmm
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.patches import Polygon
from matplotlib.patches import Rectangle
cols = [a,b,c,[.6,.6,.6]]
base_folder = input("Enter the main directory path") + '\\'
hmm_trials_paths = glob.glob(base_folder + 'hmm_trials\\*hmm_trials.npy')
hmm_paths = glob.glob(base_folder + 'hmms\\*hmm.npy')
mean_measure = np.full([len(hmm_trials_paths),6,3],np.nan) #[mouse,state,measure]
subjects=[]
all_r = np.full([len(hmm_trials_paths),4],np.nan)
all_mouse_state_enter_means_no_opt=[]
all_mouse_state_exit_means_no_opt=[]
for m in range(len(hmm_trials_paths)):
[... 172 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hz/hulsey2023/hulsey2023_analysis/figure_generation_code; grep -n "wilcoxon\|ranksums\|stats\.\(w\|r\|k\)" Figure4.py FigureS6.py FigureS8.py Figure5.py FigureS7.py FigureS3_S4.py FigureS5.py | head -40
```

```
Figure4.py:168:    # print(stats.wilcoxon(data[0],data[1]))
Figure4.py:170:    # print(stats.wilcoxon(data[1],data[2]))
Figure4.py:172:    # print(stats.wilcoxon(data[0],data[2]))
Figure4.py:286:    # print(stats.wilcoxon(this_enter[:,9],this_enter[:,19]))
Figure4.py:288:    # print(stats.wilcoxon(this_exit[:,9],this_exit[:,19]))
FigureS6.py:191:            p=stats.wilcoxon(all_r[:,zz,these_states[0]],all_r[:,zz,these_states[1]])[1]
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hz/hulsey2023/hulsey2023_analysis/figure_generation_code; grep -v "^\s*#" FigureS8.py | grep -v "^\s*$" | grep -v "plt\.\|ax\.\|ax[0-9]*\[\|set_\|fig\.\|rcParams\|^[a-f] =\|spine\|tick\|label" | sed -n 1,140p
```

```
"""
Created on Mon Nov 13 11:47:42 2023
@author: admin
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 
import glob
import os
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm
base_folder = input("Enter the main directory path") + '\\'
hmm_trials_paths = glob.glob(base_folder + 'hmm_trials\\*hmm_trials.npy')
measures = ['post_hoc_pupil_diameter','post_hoc_pupil_std10','face_energy','face_std_10','running_speed','running_std10']
subjects=[]
all_models=[]
all_models2=[]
for m in range(len(hmm_trials_paths)):
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hz/hulsey2023/hulsey2023_analysis/figure_generation_code; grep -n "bin_size\|step\s*=\|arange(\|rsq\|r2_score\|KFold\|polyfit\|zscore\|query(" FigureS3_S4.py | head -60
```

```
40:                state_trials=len(all_trials.query("hmm_state==@state and inpt==@this_inpt"))
42:                    psycho[int(state),ind,ind2]=len(all_trials.query("choice==@choice and hmm_state==@state and inpt==@this_inpt"))/state_trials
123:        if all([len(trials.query('hmm_state==0'))>10,np.isin('post_hoc_pupil_diameter',trials.columns)]):
129:        all_trials=all_trials.query(measure+'=='+measure)
131:    face_z = scipy.stats.zscore(all_trials['face_energy'])
132:    run_z = scipy.stats.zscore(all_trials['running_speed'])
135:    state_trials = all_trials.query('hmm_state==hmm_state')
138:    bin_size=.02
139:    p_state=np.full([int(1/bin_size),6],np.nan)
140:    for k,p in enumerate(np.arange(0,1,bin_size)):
141:        p2 = p+bin_size
142:        p_trials = state_trials.query(pupil_measure+'>=@p and '+pupil_measure+'<@p2')
153:    p2=(k+1)*bin_size
155:    p_trials = state_trials.query(pupil_measure+'>=@p and '+pupil_measure+'<@p2')
171:    bin_size=.05
172:    p_state=np.full([int(1/bin_size),6],np.nan)
173:    for k,p in enumerate(np.arange(0,1,bin_size)):
174:        p2 = p+bin_size
175:        p_trials = state_trials.query('face_energy>=@p and face_energy<@p2')
188:    p2=(k+1)*bin_size
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json; nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:600]); print('----')
print(nb['metadata'])
"; grep -n "def check" -A5 tools/entry.py | head -40; grep -n "install\|pip\|tags\|sanity\|claim:" tools/entry.py | head -40
```

```
markdown {} # Reproducing Fouke et al. (2025) from dandiset 001453

**Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent
visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*.
[doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04.027). This attempt used the
full text of the accepted author manuscript in PubMed Central (PMC12218792); the version of record
is not open access.

**Dandiset.** [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), version
0.250518.1950. The paper cites no DANDI version (its data
----
code {} import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.formula.api import ols
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,40p tools/entry.py; sed -n 150,330p tools/entry.py
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
[... 200 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "max.minutes\|max_minutes\|PYTHON_VERSION =" tools/entry.py | head
```

```
29:that takes longer than --max-minutes fails, even if it ran without error.
59:PYTHON_VERSION = "3.13"
342:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
371:        if ok and seconds > max_minutes * 60:
373:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
433:    parser.add_argument("--max-minutes", type=float, default=30,
469:    return run(entry_dir, output_dir, args.timeout, args.max_minutes)
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
s=open('hulsey.py').read()
old='''        if k == "post_hoc_pupil_diameter":
            ev = np.full(len(t), np.nan)'''
new='''        # clock check: change of the measure over 1.5 s from stimulus onset, and the same change
        # 4 s later (between trials)
        for name, off in (("d0", 0), ("d4", 4000)):
            a_, b_ = samp + off, samp + off + 1500
            okd = b_ <= n - 1
            dv = np.full(len(t), np.nan)
            dv[okd] = g[b_[okd]] - g[a_[okd]]
            t[f"{k}_{name}"] = dv
        if k == "post_hoc_pupil_diameter":
            ev = np.full(len(t), np.nan)'''
assert old in s
s=s.replace(old,new)
open('hulsey.py','w').write(s)
EOF
time python -c "
import sys; sys.path.insert(0,'.')
import hulsey, os
a=hulsey.list_assets()
tr,al,ss=hulsey.load_all(a)
d=os.environ['TMPDIR']
tr.to_pickle(d+'/tr.pkl'); al.to_pickle(d+'/al.pkl'); ss.to_pickle(d+'/ss.pkl')
print(len(tr))
"; date -u
```

```
167948

real	3m9.902s
user	9m7.204s
sys	3m9.895s
Sat Oct 31 09:53:48 UTC 2026
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev; cat > $TMPDIR/dev/run.py <<'EOF'
"""Dev runner: exec cells of nb.py from cell A to B, snapshotting the namespace."""
import sys, os, pickle, re, time
sys.path.insert(0, 'entries/000678-hulsey-2024')
os.chdir('entries/000678-hulsey-2024')
src = open(os.environ['TMPDIR'] + '/dev/nb.py').read()
cells = re.split(r'^#%% ', src, flags=re.M)[1:]
a, b = int(sys.argv[1]), int(sys.argv[2])
snap = os.environ['TMPDIR'] + f'/dev/snap_{a}.pkl'
ns = {}
if a > 0:
    ns = pickle.load(open(snap, 'rb'))
for i in range(a, b):
    head, _, body = cells[i].partition('\n')
    if head.startswith('md'):
        continue
    if 'devload' in head:
        body = open(os.environ['TMPDIR'] + '/dev/devload.py').read()
    print(f'===== cell {i} [{head}]', flush=True)
    t = time.time()
    exec(compile(body, f'cell{i}', 'exec'), ns)
    print(f'----- {time.time()-t:.1f}s', flush=True)
import types
keep = {k: v for k, v in ns.items() if not k.startswith('__') and not isinstance(v, types.ModuleType)}
ok = {}
for k, v in keep.items():
    try:
        pickle.dumps(v); ok[k] = v
    except Exception:
        pass
pickle.dump(ok, open(os.environ['TMPDIR'] + f'/dev/snap_{b}.pkl', 'wb'))
EOF
cat > $TMPDIR/dev/devload.py <<'EOF'
import time, warnings, os
import numpy as np, pandas as pd
from scipy import stats
import hulsey
pd.set_option("display.width", 220); pd.set_option("display.max_columns", 40); pd.set_option("display.max_rows", 200)
warnings.filterwarnings("ignore", category=RuntimeWarning)
started = time.time()
assets = hulsey.list_assets()
d = os.environ['TMPDIR']
trials_all = pd.read_pickle(d + '/tr.pkl'); alltrials = pd.read_pickle(d + '/al.pkl'); sessions = pd.read_pickle(d + '/ss.pkl')
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/nb.py <<'EOF'
#%% md
HEADER
#%% code devload
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

import hulsey

pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_rows", 200)
warnings.filterwarnings("ignore", category=RuntimeWarning)

started = time.time()
assets = hulsey.list_assets()
print(f"dandiset {hulsey.DANDISET} version {hulsey.VERSION}: {len(assets)} assets, "
      f"{assets['size'].sum() / 1e9:.2f} GB")
trials_all, alltrials, sessions = hulsey.load_all(assets)
print(f"streamed {len(sessions)} files in {(time.time() - started) / 60:.1f} min")
#%% md
## Data check

Each file holds one session: a trials table, the measures of the face camera (online and post hoc pupil, face and whisker motion energy, sampled at about 29.5 Hz), wheel speed (about 100 Hz), and lick and reward times. The checks of the metadata against the values are stated under each output.
#%% code tags=sanity
meta = hulsey.version_metadata()
print("Archive metadata: name:", meta["name"])
print("  numberOfSubjects:", meta.get("assetsSummary", {}).get("numberOfSubjects"),
      "| numberOfFiles:", meta.get("assetsSummary", {}).get("numberOfFiles"))
print("\nSessions by subject, task (session_type), training stage:")
by = sessions.assign(task=sessions.session_type).groupby(["subject", "task"]).agg(
    sessions=("path", "size"), S5=("stage", lambda x: int((x == "S5").sum())),
    S6=("stage", lambda x: int((x == "S6").sum())),
    no_post_hoc_pupil=("pupil_raw_median", lambda x: int(x.isna().sum())))
print(by.to_string())
print("\nTask per subject from session_type agrees with target_modality of the trials (0 auditory, 1 visual):",
      bool((sessions.groupby("subject").modality.nunique() == 1).all()
           and ((sessions.session_type == "visual") == (sessions.modality == 1)).all()))
print("Training stages present:", sorted(sessions.stage.unique()))
print("Rigs:", sessions.rig.value_counts().to_dict())
print("\nTrials in the files:", len(alltrials), "| target trials:", len(trials_all),
      "| distractor trials:", int(sessions.n_distractor.sum()))
print("Outcome codes by stimulus type (0 target, 1 distractor):")
print(pd.crosstab(alltrials.stimulus_type, alltrials.outcome).to_string())
print("\nStimulus values (code's inpt) per task:")
print(trials_all.assign(task=np.where(trials_all.target_modality == 0, "auditory", "visual"))
      .groupby("task").inpt.apply(lambda x: sorted(np.round(x.unique(), 3))).to_string())
print("Visual difficulty codes present:", sorted(alltrials.visual_stim_difficulty.dropna().unique()),
      "| auditory difficulty values:", sorted(np.round(alltrials.auditory_stim_difficulty.dropna().unique(), 2)))
print("Stimulus duration (ms):", alltrials.stimulus_duration.unique())
iti = alltrials.groupby("path").start_time.diff().dropna()
print(f"Start-to-start interval (s): median {iti.median():.2f}, 5-95% {iti.quantile(.05):.2f} to {iti.quantile(.95):.2f}")
print("\nSampling: face camera", sessions.face_rate.round(2).value_counts().to_dict(),
      "Hz; wheel", sessions.run_rate.round(1).value_counts().to_dict(), "Hz")
print("Raw running_speed per session (unit stated 'cm/s'): median of session medians "
      f"{sessions.run_raw_median.median():.3f}, median of session 99th percentiles {sessions.run_raw_p99.median():.3f}, "
      f"largest 99th percentile {sessions.run_raw_p99.max():.3f}")
print("Raw post hoc pupil diameter (pixels): session medians from "
      f"{sessions.pupil_raw_median.min():.1f} to {sessions.pupil_raw_median.max():.1f}")
cols = ["post_hoc_pupil_diameter", "face_energy", "running_speed", "post_hoc_pupil_std10", "face_std_10", "running_std10"]
print("\nMeasures at stimulus onset after the code's filtering and normalisation (target trials):")
print(trials_all[cols].describe().T[["count", "mean", "min", "50%", "max"]].round(3).to_string())
print("\nDuplicate recordings: identical face motion energy arrays", int(sessions.fp_face.duplicated(keep=False).sum()),
      "| identical trial tables (stimulus times and outcomes)", int(sessions.fp_trials.duplicated(keep=False).sum()))
#%% md
The archive gives 13 subjects and 391 files; the files hold 13 mice, 8 on the auditory task and 5 on the visual task, all in training stages 5 and 6. No recording is deposited twice. `running_speed` is labelled cm/s, but its values (session medians around 0.07, 99th percentiles up to about 0.67) fit m/s, the unit of the paper (locomotion speed around 0.14 m/s) and of its code, which uses the values as they are; the values are taken as m/s and the label is recorded as a metadata error. Some sessions have a post hoc pupil series that is all missing; the paper's analyses that need pupil drop those trials, as here. The visual difficulty column is described as five angles, but only codes 0 to 2 occur, which the code maps to stimulus values 1, 0.8 and 0.6.

The next cell checks that the measures share the clock of the trial table. If they do, licking after the stimulus moves the face, so face motion energy rises over the 1.5 s after stimulus onset more on trials with a response than on trials without; 4 s later, between trials, the difference should vanish.
#%% code tags=sanity
resp = trials_all.hmm_choice != 2
clock = []
for subj, g in trials_all.groupby("subject"):
    r = g.hmm_choice != 2
    row = {"subject": subj}
    for k in ["face_energy", "running_speed", "post_hoc_pupil_diameter"]:
        for w in ["d0", "d4"]:
            row[f"{k[:4]}_{w}"] = g.loc[r, f"{k}_{w}"].mean() - g.loc[~r, f"{k}_{w}"].mean()
    clock.append(row)
clock = pd.DataFrame(clock).set_index("subject")
print("Response minus no-response trials: change of each measure from stimulus onset to 1.5 s after (d0),")
print("and over the same 1.5 s starting 4 s after onset (d4). Face and pupil normalised units, running m/s.")
print(clock.round(4).to_string())
print("\nMice with a larger face rise on response trials at onset than 4 s later:",
      int((clock.face_d0 > clock.face_d4.abs()).sum()), "of", len(clock))
#%% md
## Sessions and trials (claim `cohort-inclusion`)

> Of 31 mice, 13 met the inclusion criteria (8 auditory, 5 visual task), with 381 of their 500 stage 5 and 6 sessions included.

The criterion is the STAR Methods' (Training and inclusion criteria): stage 5 or 6, at least 100 rewards with at least 20% at each port, and at least 10 such sessions per mouse. Rewards are counted from the `reward_left` and `reward_right` series; the hits of the trial table are shown as a second count. The sessions that pass are the sessions of every later analysis.
#%% code tags=claim:cohort-inclusion
s = sessions.copy()
s["rewards"] = s.reward_left + s.reward_right
s["min_port_frac"] = np.minimum(s.reward_left, s.reward_right) / s.rewards
hits = alltrials[alltrials.outcome == 1].groupby("path").target_port.agg(hits="size", hits_left=lambda x: int((x == 0).sum()))
s = s.merge(hits, left_on="path", right_index=True, how="left")
s["hit_min_frac"] = np.minimum(s.hits_left, s.hits - s.hits_left) / s.hits
s["pass_rewards"] = s.stage.isin(["S5", "S6"]) & (s.rewards >= 100) & (s.min_port_frac >= 0.2)
s["pass_hits"] = s.stage.isin(["S5", "S6"]) & (s.hits >= 100) & (s.hit_min_frac >= 0.2)
per_mouse = s.groupby("subject").pass_rewards.sum()
s["included"] = s.pass_rewards & s.subject.map(per_mouse >= 10)
print("Sessions in the dandiset:", len(s))
print("Pass by rewards:", int(s.pass_rewards.sum()), "| pass by hits:", int(s.pass_hits.sum()),
      "| either:", int((s.pass_rewards | s.pass_hits).sum()))
print("Mice with at least 10 passing sessions:", int((per_mouse >= 10).sum()), "of", len(per_mouse))
mods = s.groupby("subject").session_type.first()
print("Mice by task:", mods.value_counts().to_dict())
print("Included sessions (rewards):", int(s.included.sum()))
print("\nSessions that fail either count:")
print(s.loc[~s.pass_rewards | ~s.pass_hits, ["path", "stage", "rewards", "min_port_frac", "hits", "hit_min_frac"]]
      .round(3).to_string(index=False))
print("\nIncluded sessions per mouse:", s[s.included].groupby("subject").size().to_dict())
included = s[s.included]
trials = trials_all[trials_all.path.isin(included.path)].copy()
print("Target trials in included sessions:", len(trials))
#%% md
**Result: COHORT**
#%% md
## Training before stage 5 (claim `training-duration`)

> Mice that reached proficiency took 21 +/- 8 training sessions to reach stage 5.

The dandiset holds only stage 5 and 6 sessions (data check), so the sessions before stage 5 cannot be counted. Blocked: data missing.
#%% md
## Distractor responses (claim `distractor-response-rate`)

> In stage 6, responses to distractors of the untrained modality were below 10%, with no discernible change in task performance.

Distractor trials have outcome 4 (`false_alarm`, a lick) or 8 (`correct_reject`, no lick); the rate is the fraction with a lick. All stage 6 sessions in the dandiset are used, and the included ones are shown too.
#%% code tags=claim:distractor-response-rate
d = alltrials[(alltrials.stimulus_type == 1)].merge(s[["path", "subject", "stage", "included"]], on="path")
d = d[d.stage == "S6"]
d["lick"] = (d.outcome == 4).astype(float)
for label, dd in [("all stage 6 sessions", d), ("included stage 6 sessions", d[d.included])]:
    pooled = dd.groupby("subject").lick.mean()
    per_sess = dd.groupby(["subject", "path"]).lick.mean().groupby("subject").mean()
    tab = pd.DataFrame({"sessions": dd.groupby("subject").path.nunique(), "distractor trials": dd.groupby("subject").size(),
                        "(a) pooled": pooled.round(4), "(b) mean over sessions": per_sess.round(4),
                        "max session": dd.groupby(["subject", "path"]).lick.mean().groupby("subject").max().round(4)})
    print(label)
    print(tab.to_string())
    print(f"(c) pooled over all mice: {dd.lick.mean():.4f} over {len(dd)} trials; mice below 0.10 under (a): "
          f"{int((pooled < 0.1).sum())} of {len(pooled)}, under (b): {int((per_sess < 0.1).sum())} of {len(per_sess)}\n")
st6 = trials_all.merge(s[["path", "stage", "included"]], on="path")
perf = st6[st6.hmm_choice != 2].assign(correct=lambda x: x.outcome == 1).groupby(["subject", "stage"]).correct.mean().unstack()
print("Not tested, for reference: fraction correct of responded target trials by stage")
print(perf.round(3).to_string())
#%% md
**Result: DISTRACTOR**
EOF
cd $TMPDIR/dev && python run.py 0 12 2>&1 | tail -150
```

```
===== cell 1 [code devload]
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run.py", line 20, in <module>
    exec(compile(body, f'cell{i}', 'exec'), ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell1", line 2, in <module>
ModuleNotFoundError: No module named 'numpy'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd $TMPDIR/dev && python run.py 0 12 2>&1 | tail -150
```

```
===== cell 1 [code devload]
----- 1.7s
===== cell 3 [code tags=sanity]
Archive metadata: name: Pupil and movement measurements during mouse auditory and visual discrimination
  numberOfSubjects: 13 | numberOfFiles: 391

Sessions by subject, task (session_type), training stage:
                  sessions  S5  S6  no_post_hoc_pupil
subject task                                         
BW041   visual          25  15  10                  0
BW045   auditory        84  10  74                  1
BW046   visual          34  18  16                 14
BW048   visual          35  20  15                  0
BW051   visual          35  25  10                  4
BW053   auditory        32  23   9                  3
BW058   visual          12  12   0                  2
BW059   auditory        25  18   7                  5
BW061   auditory        23  23   0                  1
BW062   auditory        17  17   0                  4
BW064   auditory        21  12   9                  2
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python - <<'EOF'
s=open('nb.py').read()
s=s.replace('''d = alltrials[(alltrials.stimulus_type == 1)].merge(s[["path", "subject", "stage", "included"]], on="path")''','''d = alltrials[(alltrials.stimulus_type == 1)].merge(s[["path", "subject", "included"]], on="path")''')
s=s.replace('''st6 = trials_all.merge(s[["path", "stage", "included"]], on="path")''','''st6 = trials_all.merge(s[["path", "included"]], on="path")''')
s=s.replace('''The next cell checks that the measures share the clock of the trial table. If they do, licking after the stimulus moves the face, so face motion energy rises over the 1.5 s after stimulus onset more on trials with a response than on trials without; 4 s later, between trials, the difference should vanish.''','''The next cell checks that the measures share the clock of the trial table, with a contrast between conditions: if they do, the measures change after stimulus onset differently on trials with a response (a lick) than on trials without, and the difference shrinks when the same window is taken 4 s later, between trials.''')
s=s.replace('''print("\\nMice with a larger face rise on response trials at onset than 4 s later:",
      int((clock.face_d0 > clock.face_d4.abs()).sum()), "of", len(clock))''','''for k in ["face", "runn", "post"]:
    print(f"{k}: mice with a larger response contrast at onset than 4 s later (absolute values): "
          f"{int((clock[k + '_d0'].abs() > clock[k + '_d4'].abs()).sum())} of {len(clock)}; "
          f"median d0 {clock[k + '_d0'].median():.4f}, d4 {clock[k + '_d4'].median():.4f}")''')
open('nb.py','w').write(s)
EOF
. $TMPDIR/env/bin/activate; python run.py 0 12 2>&1 | sed -n '/cell 5/,/-----/p;/cell 11/,$p'
```

```
===== cell 5 [code tags=sanity]
Response minus no-response trials: change of each measure from stimulus onset to 1.5 s after (d0),
and over the same 1.5 s starting 4 s after onset (d4). Face and pupil normalised units, running m/s.
         face_d0  face_d4  runn_d0  runn_d4  post_d0  post_d4
subject                                                      
BW041     0.0056  -0.0227  -0.0233   0.0090  -0.0033   0.0074
BW045     0.0588   0.0122  -0.0296   0.0040   0.0075  -0.0032
BW046     0.0252  -0.0095  -0.1593   0.0242  -0.0520   0.0148
BW048     0.0352  -0.0082  -0.1329   0.0807  -0.0395   0.0129
BW051    -0.0714   0.0108  -0.1641   0.0509  -0.0287   0.0195
BW053     0.0815  -0.0180  -0.0026   0.0025   0.0461   0.0007
BW058     0.0153   0.0063  -0.1134   0.0416  -0.0157   0.0061
BW059     0.0515  -0.0086  -0.3026   0.0868  -0.0261  -0.0050
BW061    -0.0791  -0.0013  -0.1167  -0.0223  -0.0200  -0.0003
BW062    -0.1024  -0.0052  -0.1024   0.0050   0.0118  -0.0194
BW064     0.0584  -0.0285  -0.1068   0.0082  -0.0040  -0.0062
BW067    -0.0423   0.0233  -0.1305   0.0829  -0.0084   0.0062
BW071    -0.0043   0.0010  -0.1426   0.0118  -0.0183   0.0014
face: mice with a larger response contrast at onset than 4 s later (absolute values): 12 of 13; median d0 0.0153, d4 -0.0052
runn: mice with a larger response contrast at onset than 4 s later (absolute values): 13 of 13; median d0 -0.1167, d4 0.0118
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
#%% md
## GLM-HMM: number of states (claim `figs2-n-states`)

> Cross-validated GLM-HMMs fit separately to each of the 13 mice gave between 3 and 5 states per mouse.

Per mouse, the target trials of the included sessions (distractor trials dropped, no-response trials kept) with inputs [stimulus value, 1] and choices left, right or none (claims file, M1 and M2). The GLM-HMM is the paper's ssm model, reimplemented in `hulsey.py` (its docstring gives the source of each part). 5-fold cross-validation over sessions, 1 to 7 states, MLE and MAP fits (2_n_states.py). The paper runs 10 random initialisations per fold and number of states; this notebook runs 3 to fit the time limit (see the deviations). The number of states is the plateau rule of 3_generate_hmms.py on the test log likelihood per trial (mean over folds, best initialisation): reading (b) on the MLE curve alone, the code's; reading (a) the larger of the MLE and MAP plateaus.
#%% code tags=claim:figs2-n-states
N_INIT_CV = 3
t0 = time.time()
subjects = sorted(trials.subject.unique())
seqs = {subj: hulsey.sequences(trials[trials.subject == subj]) for subj in subjects}
tasks, keys = [], []
for i, subj in enumerate(subjects):
    Xs, ys = seqs[subj]
    tt, kk = hulsey.cv_tasks(Xs, ys, N_INIT_CV, seed=1000 + i)
    tasks += tt
    keys += [(subj,) + k for k in kk]
order = np.argsort([-sum(len(x) for x in t[1]) * t[0] for t in tasks])  # largest fits first
res = hulsey.run_parallel(hulsey.cv_test_ll, [tasks[j] for j in order])
cv = {keys[j]: r for j, r in zip(order, res)}
print(f"{len(tasks)} cross-validation fits in {(time.time() - t0) / 60:.1f} min; "
      f"{sum(r[2] == 1000 for r in res)} stopped at 1000 iterations")
n_states, curves = {}, {}
rows = []
for subj in subjects:
    row = {"subject": subj, "task": mods[subj], "trials": sum(len(x) for x in seqs[subj][0]),
           "sessions": len(seqs[subj][0])}
    for use_map, name in [(False, "MLE"), (True, "MAP")]:
        a = np.full((N_INIT_CV, 7, 5), np.nan)
        for (sb, f, K, z, m), v in cv.items():
            if sb == subj and m == use_map:
                a[z, K - 1, f] = v[1]
        n, curve = hulsey.select_states(a)
        curves[(subj, name)] = curve
        row[name] = n
    row["(a) max"] = max(row["MLE"], row["MAP"])
    row["(b) MLE"] = row["MLE"]
    rows.append(row)
nst = pd.DataFrame(rows).set_index("subject")
print(nst.to_string())
for r in ["(a) max", "(b) MLE"]:
    print(f"reading {r}: range {nst[r].min()} to {nst[r].max()}; counts {nst[r].value_counts().sort_index().to_dict()}")
print("\nTest log likelihood per trial (MLE, mean over folds, best initialisation), 1 to 7 states:")
print(pd.DataFrame({subj: curves[(subj, 'MLE')] for subj in subjects}, index=range(1, 8)).T.round(4).to_string())
print("\nThe same for MAP:")
print(pd.DataFrame({subj: curves[(subj, 'MAP')] for subj in subjects}, index=range(1, 8)).T.round(4).to_string())
n_states = nst["(b) MLE"].to_dict()
#%% md
**Result: NSTATES**
#%% md
### Final models and state labels

As 3_generate_hmms.py: per mouse, 10 MLE fits on all sessions with the selected number of states (reading (b), which is also reading (a) when they agree), the one with the highest log likelihood kept; trials in a state when its posterior is at least 0.8 (flex_hmm.get_posterior_probs); states ordered optimal, disengaged, others (flex_hmm.permute_hmm). Sub-optimal states are then matched to the four templates of Figure2.py, on the sessions in which the optimal state occurs.
#%% code
t0 = time.time()
tasks, owner = [], []
for i, subj in enumerate(subjects):
    Xs, ys = seqs[subj]
    tt = hulsey.final_tasks(Xs, ys, n_states[subj], 10, seed=2000 + i)
    tasks += tt
    owner += [subj] * len(tt)
res = hulsey.run_parallel(hulsey.fit_one, tasks)
models = {}
for subj in subjects:
    rr = [res[j] for j in range(len(res)) if owner[j] == subj]
    models[subj] = rr[int(np.argmax([r[1] for r in rr]))][0]
print(f"final fits in {(time.time() - t0) / 60:.1f} min")
post_cols = []
parts = []
for subj in subjects:
    g = trials[trials.subject == subj]
    m = models[subj]
    p0 = hulsey.posterior_states(m, g)
    ps, _ = hulsey.psychos(g, p0.hmm_state.values)
    perm = hulsey.permutation_optimal_disengaged(ps)
    m.permute(perm)
    parts.append(hulsey.posterior_states(m, g))
post = pd.concat(parts)
trials = trials.drop(columns=[c for c in trials.columns if c.startswith("state_") or c == "hmm_state"], errors="ignore")
trials = trials.join(post)
# sessions in which the optimal state occurs (Figure2.py) and with more than 10 optimal trials (Figure3.py etc.)
opt_n = trials.groupby("path").hmm_state.apply(lambda x: int((x == 0).sum()))
trials["sess_has_opt"] = trials.path.map(opt_n > 0)
trials["sess_opt10"] = trials.path.map(opt_n > 10) & trials.path.map(included.set_index("path").pupil_raw_median.notna())
types = {}
rows = []
for subj in subjects:
    g = trials[(trials.subject == subj) & trials.sess_has_opt]
    ps, inp = hulsey.psychos(g, g.hmm_state.values)
    lab, sim = hulsey.state_types(ps)
    types[subj] = lab
    occ = g.hmm_state.value_counts(normalize=True).sort_index()
    rows.append({"subject": subj, "states": n_states[subj], "inputs": len(inp),
                 "labels": [hulsey.STATE_NAMES[k] for k in lab],
                 "occupancy": [round(occ.get(k, 0), 3) for k in range(n_states[subj])],
                 "indeterminate": round(g.hmm_state.isna().mean(), 3)})
print(pd.DataFrame(rows).set_index("subject").to_string())
trials["state_type"] = np.nan
for subj in subjects:
    sel = trials.subject == subj
    st = trials.loc[sel, "hmm_state"]
    trials.loc[sel, "state_type"] = st.map(lambda k: types[subj][int(k)] if k == k else np.nan)
print("\nTrials by state (0 optimal, 1 disengaged, 2 or more other; NaN indeterminate):",
      trials.hmm_state.value_counts(dropna=False).sort_index().to_dict())
EOF
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python run.py 12 17 2>&1 | grep -v Warning | tail -80; date -u
```

```
===== cell 14 [code tags=claim:figs2-n-states]
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run.py", line 20, in <module>
    exec(compile(body, f'cell{i}', 'exec'), ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell14", line 2, in <module>
NameError: name 'time' is not defined. Did you forget to import 'time'?
Sat Oct 31 09:55:25 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; sed -i 's/^    ns = pickle.load(open(snap, .rb.))/    ns = pickle.load(open(snap, "rb")); exec("import time, warnings\\nimport numpy as np, pandas as pd\\nfrom scipy import stats\\nimport hulsey\\nimport matplotlib\\nmatplotlib.use(\\"Agg\\")\\nimport matplotlib.pyplot as plt\\nwarnings.filterwarnings(\\"ignore\\")", ns)/' run.py; grep -n "ns = pickle" run.py; . $TMPDIR/env/bin/activate; python run.py 12 17 2>&1 | grep -v Warning | tail -80; date -u
```

```
11:    ns = pickle.load(open(snap, "rb")); exec("import time, warnings\nimport numpy as np, pandas as pd\nfrom scipy import stats\nimport hulsey\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nwarnings.filterwarnings(\"ignore\")", ns)
===== cell 14 [code tags=claim:figs2-n-states]
2730 cross-validation fits in 4.2 min; 16 stopped at 1000 iterations
             task  trials  sessions  MLE  MAP  (a) max  (b) MLE
subject                                                        
BW041      visual   11542        24    3    3        3        3
BW045    auditory   23179        79    4    4        4        4
BW046      visual   13795        32    4    4        4        4
BW048      visual   14109        35    5    4        5        5
BW051      visual   13935        35    3    3        3        3
BW053    auditory   11858        29    4    3        4        4
BW058      visual    5623        12    4    4        4        4
BW059    auditory   13184        25    4    3        4        4
BW061    auditory   13793        23    3    3        3        3
BW062    auditory   11142        16    3    3        3        3
BW064    auditory    7034        18    3    3        3        3
BW067    auditory   13603        23    4    3        4        4
BW071    auditory   11706        25    4    3        4        4
reading (a) max: range 3 to 5; counts {3: 5, 4: 7, 5: 1}
reading (b) MLE: range 3 to 5; counts {3: 5, 4: 7, 5: 1}
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python run.py 17 18 2>&1 | grep -v Warning | tail -40
```

```
===== cell 17 [code]
final fits in 0.1 min
         states  inputs                                                   labels                         occupancy  indeterminate
subject                                                                                                                          
BW041         3       6                        [optimal, disengaged, avoid left]             [0.678, 0.129, 0.192]          0.071
BW045         4       6           [optimal, disengaged, bias right, avoid right]      [0.422, 0.173, 0.319, 0.086]          0.238
BW046         4       6             [optimal, disengaged, bias right, bias left]        [0.61, 0.082, 0.11, 0.198]          0.103
BW048         5       6  [optimal, disengaged, bias left, bias left, avoid left]  [0.33, 0.062, 0.353, 0.156, 0.1]          0.334
BW051         3       6                       [optimal, disengaged, avoid right]             [0.626, 0.069, 0.305]          0.149
BW053         4       6             [optimal, disengaged, bias left, bias right]      [0.546, 0.224, 0.114, 0.116]          0.129
BW058         4       6           [optimal, disengaged, avoid right, bias right]        [0.672, 0.1, 0.164, 0.064]          0.086
BW059         4       6            [bias right, disengaged, optimal, avoid left]           [0.703, 0.076, 0, 0.22]          0.171
BW061         3       6                        [bias right, disengaged, optimal]             [0.651, 0.275, 0.074]          0.042
BW062         3       6                        [optimal, disengaged, avoid left]             [0.539, 0.112, 0.348]          0.172
BW064         3       6                       [optimal, disengaged, avoid right]              [0.43, 0.331, 0.239]          0.223
BW067         4       6             [optimal, disengaged, bias left, bias right]       [0.491, 0.142, 0.33, 0.037]          0.104
BW071         4       6             [optimal, disengaged, bias left, bias right]      [0.611, 0.174, 0.091, 0.125]          0.102

Trials
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python - <<'EOF' 2>&1 | grep -v Warn
import pickle,os,sys
sys.path.insert(0,'entries/000678-hulsey-2024')
import hulsey, numpy as np
ns=pickle.load(open(os.environ['TMPDIR']+'/dev/snap_18.pkl','rb'))
tr=ns['trials']
for s in ['BW059','BW061','BW048']:
    g=tr[(tr.subject==s)]
    ps,inp=hulsey.psychos(g,g.hmm_state.values)
    print(s, inp, g.hmm_state.value_counts(dropna=False).to_dict())
    print(np.round(ps,2))
    print(np.round(ns['models'][s].W,2))
EOF
```

```
BW059 [-0.97  -0.625 -0.43   0.43   0.625  0.97 ] {0.0: 7420, 3.0: 2327, nan: 2185, 1.0: 820, 2.0: 432}
[[[0.95 0.78 0.64 0.12 0.08 0.04]
  [0.03 0.2  0.34 0.87 0.91 0.95]
  [0.02 0.02 0.02 0.   0.   0.  ]]

 [[0.01 0.   0.   0.01 0.03 0.01]
  [0.03 0.05 0.04 0.13 0.05 0.08]
  [0.96 0.95 0.96 0.86 0.92 0.91]]

 [[0.95 0.8  0.77 0.33 0.18 0.06]
  [0.   0.04 0.06 0.24 0.19 0.29]
  [0.05 0.16 0.17 0.43 0.63 0.65]]

 [[0.06 0.07 0.06 0.   0.01 0.  ]
  [0.15 0.42 0.58 0.98 0.99 1.  ]
  [0.79 0.5  0.36 0.02 0.01 0.  ]]]
[[[ 0.16  3.1 ]
  [ 3.26  3.77]]

 [[ 1.29 -4.72]
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
s=open('hulsey.py').read()
old=s[s.index('def state_types(ps):'):]
new='''def state_types(ps, fixed_first_two=True):
    """Figure2.py: each state's nearest template (nansum of absolute differences), with the
    code's loop resolving states assigned the same template. ps must have 6 inputs.

    With fixed_first_two (claims file, M3), states 0 and 1 are optimal and disengaged as
    flex_hmm.permute_hmm ordered them, and only the others are matched, to the four sub-optimal
    templates. A state with no trial in a discrete state has an all-missing psychometric, which
    the code's nansum would score 0 against every template; such a state is labelled -1 (no
    trials) and left out of the matching (a guard added here)."""
    if ps.shape[2] == 8:
        bad = np.unique(np.where(ps != ps)[-1])
        ps = np.delete(ps, bad, axis=2)
    if ps.shape[2] == 8:
        ps = np.delete(ps, [1, 6], axis=2)
    tmpl = sort_templates()
    sim = np.array([[np.nansum(np.abs(s - t)) for t in tmpl] for s in ps])
    empty = np.array([np.all(np.isnan(s)) for s in ps])
    sim[empty] = np.inf
    lab = np.full(len(ps), -1)
    if fixed_first_two:
        lab[0], lab[1] = 0, 1
        rows = [i for i in range(2, len(ps)) if not empty[i]]
        allowed = [2, 3, 4, 5]
    else:
        rows = [i for i in range(len(ps)) if not empty[i]]
        allowed = list(range(6))
    sub = sim[np.ix_(rows, allowed)]
    if len(rows):
        cur = np.argmin(sub, axis=1)
        guard = 0
        while len(np.unique(cur)) != len(cur) and guard < 100:
            vals, counts = np.unique(cur, return_counts=True)
            for v in vals[counts > 1]:
                idx = np.where(cur == v)[0]
                worst = idx[np.argmax(sub[idx, v])]
                cur[worst] = np.argsort(sub[worst])[1]
            guard += 1
        lab[rows] = np.array(allowed)[cur]
    return lab, sim
'''
s=s.replace(old,new)
s=s.replace('STATE_NAMES = ["optimal", "disengaged", "bias left", "avoid right", "bias right", "avoid left"]','STATE_NAMES = ["optimal", "disengaged", "bias left", "avoid right", "bias right", "avoid left", "no trials"]')
open('hulsey.py','w').write(s)
EOF
cd $TMPDIR/dev; python - <<'EOF'
s=open('nb.py').read()
s=s.replace('''    lab, sim = hulsey.state_types(ps)
    types[subj] = lab
    occ = g.hmm_state.value_counts(normalize=True).sort_index()
    rows.append({"subject": subj, "states": n_states[subj], "inputs": len(inp),
                 "labels": [hulsey.STATE_NAMES[k] for k in lab],''','''    lab, sim = hulsey.state_types(ps)
    lab_all, _ = hulsey.state_types(ps, fixed_first_two=False)
    types[subj] = lab
    occ = g.hmm_state.value_counts(normalize=True).sort_index()
    rows.append({"subject": subj, "states": n_states[subj], "inputs": len(inp),
                 "labels": [hulsey.STATE_NAMES[k] for k in lab],
                 "nearest of all six templates": [hulsey.STATE_NAMES[k] for k in lab_all],''')
open('nb.py','w').write(s)
EOF
python run.py 17 18 2>&1 | grep -v Warning | tail -40
```

```
===== cell 17 [code]
final fits in 0.4 min
         states  inputs                                                     labels                             nearest of all six templates                         occupancy  indeterminate
subject                                                                                                                                                                                     
BW041         3       6                          [optimal, disengaged, avoid left]                        [optimal, disengaged, avoid left]             [0.678, 0.129, 0.192]          0.071
BW045         4       6             [optimal, disengaged, bias right, avoid right]           [optimal, disengaged, bias right, avoid right]      [0.422, 0.173, 0.319, 0.086]          0.238
BW046         4       6               [optimal, disengaged, bias right, bias left]             [optimal, disengaged, bias right, bias left]        [0.61, 0.082, 0.11, 0.198]          0.103
BW048         5       6  [optimal, disengaged, avoid right, bias left, avoid left]  [optimal, disengaged, bias left, bias left, avoid left]  [0.33, 0.062, 0.353, 0.156, 0.1]          0.334
BW051         3       6                         [optimal, disengaged, avoid right]                       [optimal, disengaged, avoid right]             [0.626, 0.069, 0.305]          0.149
BW053         4       6               [optimal, disengaged, bias left, bias right]             [optimal, disengaged, bias left, bias right]      [0.546, 0.224, 0.114, 0.116]          0.129
BW058         4       6             [optimal, disengaged, avoid right, bias right]           [optimal, disengaged, avoid right, bias right]        [0.672, 0.1, 0.164, 0.064]          0.086
BW059         4       6               [optimal, disengaged, no trials, avoid left]             [optimal, disengaged, no trials, avoid left]           [0.703, 0.076, 0, 0.22]          0.171
BW061         3       6                           [optimal, disenga
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; cat >> hulsey.py <<'EOF'


def dwell_table(states):
    """flex_hmm.get_dwell_times for one session, line by line. A dwell is recorded as the run
    length plus one for every epoch ended inside the loop, and the final record uses the state of
    the second-to-last trial; last_trial is the index of the first trial after the epoch.
    'run' is the run length itself."""
    ts = np.asarray(states, float)
    rows = []
    n, state_start = 0, 0
    this_state = np.nan
    while n < len(ts) - 1:
        this_state, next_state = ts[n], ts[n + 1]
        if not (this_state == next_state):
            state_end = n + 1
            if not np.isnan(this_state):
                rows.append((this_state, state_end - state_start + 1, state_start, state_end, state_end - state_start))
            state_start = n + 1
        n += 1
    state_end = n
    if not np.isnan(this_state):
        rows.append((this_state, state_end - state_start, state_start, state_end, state_end - state_start + 1))
    return pd.DataFrame(rows, columns=["state", "dwell", "first_trial", "last_trial", "run"])


def stratified_kfold_random_order(class_index, n_folds, rng):
    """6_predictive_accuracy.stratified_kFold_random_order: StratifiedKFold on the session index
    (contiguous blocks of each session), with the order of the folds permuted per session."""
    from sklearn.model_selection import StratifiedKFold
    classes = np.unique(class_index)
    fold_index = np.array([rng.permutation(n_folds) for _ in classes])
    skf = StratifiedKFold(n_splits=n_folds)
    tr_idx, te_idx = [], []
    for a, b in skf.split(np.arange(len(class_index)), class_index):
        tr_idx.append(a)
        te_idx.append(b)
    new_tr, new_te = [], []
    for i in range(n_folds):
        t1, t2 = [], []
        for j, c in enumerate(classes):
            this = np.where(class_index == c)[0]
            a, b = tr_idx[fold_index[j, i]], te_idx[fold_index[j, i]]
            t1.append(a[np.isin(a, this)])
            t2.append(b[np.isin(b, this)])
        new_tr.append(np.concatenate(t1))
        new_te.append(np.concatenate(t2))
    return new_tr, new_te


def fit_map_one(args):
    """flex_hmm.choice_hmm_fit (MAP: prior_sigma 2, sticky transitions alpha 2, kappa 0) on one
    concatenated sequence; returns the model and its test log probability per trial."""
    K, Xtr, ytr, Xte, yte, seed = args
    m = GLMHMM(K, prior_sigma=2.0, sticky=True, rng=seed)
    m.fit([Xtr], [ytr])
    return m, m.log_probability([Xte], [yte]) / len(Xte)


def predict_choices(m, X, y):
    """6_predictive_accuracy.py: the first trial's state is the most likely initial state; later,
    the most likely next state from the transition matrix given the most likely filtered state of
    the preceding test trials; the choice is the most likely choice of that state's GLM."""
    U, ux, yy = _unique_inputs([X], [y])
    ll = _logits(m.W, U)[ux, :, yy]
    filt = _filter(m.log_pi0, m.P, ll)
    states = np.empty(len(X), int)
    states[0] = np.argmax(m.log_pi0)
    states[1:] = np.argmax(m.P[np.argmax(filt[:-1], axis=1)], axis=1)
    lg = _logits(m.W, X)  # (T, K, C)
    return np.argmax(lg[np.arange(len(X)), states], axis=1)
EOF
cat >> $TMPDIR/dev/nb.py <<'EOF'
#%% code
# a state with no discrete trial in the sessions where the optimal state occurs is typed on all sessions
for subj in subjects:
    if (types[subj] == -1).any():
        g = trials[trials.subject == subj]
        ps, _ = hulsey.psychos(g, g.hmm_state.values)
        lab_all_sess, _ = hulsey.state_types(ps)
        print(f"{subj}: states with no discrete trial in sessions with the optimal state:",
              list(np.where(types[subj] == -1)[0]), "| typed on all sessions:",
              [hulsey.STATE_NAMES[k] for k in lab_all_sess],
              "| trials per state over all sessions:", g.hmm_state.value_counts().sort_index().to_dict())
        types[subj] = np.where(types[subj] == -1, lab_all_sess, types[subj])
        sel = trials.subject == subj
        trials.loc[sel, "state_type"] = trials.loc[sel, "hmm_state"].map(lambda k: types[subj][int(k)] if k == k else np.nan)
#%% md
## State types (claim `fig2a-state-types`)

> Six stereotyped performance states emerged across mice. Every mouse had an optimal and a disengaged state and at least one sub-optimal state (bias left or right, avoid left or right).
#%% code tags=claim:fig2a-state-types
rows = []
for subj in subjects:
    lab = types[subj]
    rows.append({"subject": subj, "states": len(lab), "optimal": int((lab == 0).sum()), "disengaged": int((lab == 1).sum()),
                 "other states": int((lab >= 2).sum()),
                 "other states matched to a sub-optimal template": int(((lab >= 2) & (lab <= 5)).sum())})
ft = pd.DataFrame(rows).set_index("subject")
print(ft.to_string())
ok = (ft.optimal == 1) & (ft.disengaged == 1) & (ft["other states"] >= 1) & (ft["other states"] == ft["other states matched to a sub-optimal template"])
print("\nMice with an optimal, a disengaged and at least one other state, each other state typed:", int(ok.sum()), "of", len(ft))
counts = {hulsey.STATE_NAMES[k]: int(sum((types[s] == k).any() for s in subjects)) for k in range(2, 6)}
print("Mice with each sub-optimal type:", counts, "(Figure 2A: bias left 6, avoid right 4, bias right 5, avoid left 5)")
print("Sub-optimal states in all:", int(sum((types[s] >= 2).sum() for s in subjects)))
#%% md
**Result: STATETYPES**
#%% md
## Occupancy (claim `fig2b-optimal-occupancy`)

> Mice spent the largest proportion of trials in the optimal state (around half), more than in the disengaged, sub-optimal or indeterminate states; 13.1% +/- 1.6% of trials were indeterminate.

Per mouse, trials of the sessions in which the optimal state occurs, pooled (Figure2.py).
#%% code tags=claim:fig2b-optimal-occupancy
occ = []
for subj in subjects:
    g = trials[(trials.subject == subj) & trials.sess_has_opt]
    h = g.hmm_state
    occ.append({"subject": subj, "optimal": (h == 0).mean(), "disengaged": (h == 1).mean(),
                "sub-optimal": (h > 1).mean(), "indeterminate": h.isna().mean(), "trials": len(g)})
occ = pd.DataFrame(occ).set_index("subject")
print((occ.drop(columns="trials") * 100).round(1).assign(trials=occ.trials).to_string())
m_ = occ.drop(columns="trials").mean() * 100
se_ = occ.drop(columns="trials").sem() * 100
print("\nmean +/- SEM over mice (%):", {k: f"{m_[k]:.1f} +/- {se_[k]:.1f}" for k in m_.index})
for other in ["disengaged", "sub-optimal", "indeterminate"]:
    w = stats.wilcoxon(occ.optimal, occ[other])
    print(f"optimal vs {other}: optimal larger in {int((occ.optimal > occ[other]).sum())} of 13 mice, "
          f"Wilcoxon signed-rank p = {w.pvalue:.2g}")
#%% md
**Result: OCCUPANCY**
#%% md
## Dwell times (claim `fig2c-dwell-times`)

> Epochs of the optimal state lasted longer than disengaged and sub-optimal epochs (about 37 against about 15 trials), and the median transition between discrete states took 3.4 +/- 0.3 trials.

Epochs from flex_hmm.get_dwell_times on the sessions in which the optimal state occurs (Figure2.py), with (y) the code's dwell and (x) the run length. A disengaged epoch longer than 40 trials (code's dwell) that ends a session is left out (Figure2.py). The per-mouse median is the first length at which the cumulative distribution exceeds 0.499.
#%% code tags=claim:fig2c-dwell-times
def cdf_median(v):
    v = np.asarray(v)
    for i in range(500):
        if np.mean(v <= i) > 0.499:
            return i
    return np.nan

ep_rows, ind_rows = [], []
for subj in subjects:
    g = trials[(trials.subject == subj) & trials.sess_has_opt].sort_values(["path", "trial_in_session"])
    for path, sg in g.groupby("path"):
        dt = hulsey.dwell_table(sg.hmm_state.values)
        if len(dt) == 0:
            continue
        gap = dt.first_trial.values - np.r_[0, dt.last_trial.values[:-1]]
        ind_rows += [{"subject": subj, "gap": x} for x in gap]
        drop_last = dt.state.iloc[-1] == 1 and dt.dwell.iloc[-1] > 40
        dt = dt.iloc[:-1] if drop_last else dt
        ep_rows.append(dt.assign(subject=subj, path=path))
ep = pd.concat(ep_rows, ignore_index=True)
ep["group"] = np.where(ep.state == 0, "optimal", np.where(ep.state == 1, "disengaged", "sub-optimal"))
ind = pd.DataFrame(ind_rows)
res_dw = {}
for col, cname in [("dwell", "(y) code dwell"), ("run", "(x) run length")]:
    med = ep.groupby(["subject", "group"])[col].apply(cdf_median).unstack()
    mean = ep.groupby(["subject", "group"])[col].mean().unstack()
    pooled = ep.groupby("group")[col].mean()
    res_dw[cname] = (med, mean, pooled)
    print(cname)
    print("  (a) mean over mice of per-mouse median:", med.mean().round(1).to_dict())
    print("  (b) mean over mice of per-mouse mean:  ", mean.mean().round(1).to_dict())
    print("  (c) mean over all epochs pooled:       ", pooled.round(1).to_dict())
    for other in ["disengaged", "sub-optimal"]:
        for nm, tab in [("medians", med), ("means", mean)]:
            w = stats.wilcoxon(tab.optimal, tab[other])
            print(f"  optimal vs {other} ({nm}): optimal longer in {int((tab.optimal > tab[other]).sum())} of 13, p = {w.pvalue:.2g}")
ind_med = ind.groupby("subject").gap.apply(cdf_median)
print("\nMedian indeterminate dwell per mouse:", ind_med.to_dict())
print(f"mean +/- SEM over mice: {ind_med.mean():.2f} +/- {ind_med.sem():.2f} trials")
print("Per-mouse medians (code dwell):")
print(res_dw["(y) code dwell"][0].assign(indeterminate=ind_med).to_string())
print("Epochs per group:", ep.group.value_counts().to_dict())
#%% md
**Result: DWELL**
EOF
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python run.py 17 26 2>&1 | grep -v Warning | sed -n '/cell 18/,$p'
```

```
===== cell 18 [code]
BW059: states with no discrete trial in sessions with the optimal state: [np.int64(2)] | typed on all sessions: ['optimal', 'disengaged', 'avoid right', 'avoid left'] | trials per state over all sessions: {0.0: 7420, 1.0: 820, 2.0: 432, 3.0: 2327}
----- 0.0s
===== cell 20 [code tags=claim:fig2a-state-types]
         states  optimal  disengaged  other states  other states matched to a sub-optimal template
subject                                                                                           
BW041         3        1           1             1                                               1
BW045         4        1           1             2                                               2
BW046         4        1           1             2                                               2
BW048         5        1           1             3                                               3
BW051         3        1           1             1                                               1
BW053         4        1           1             2                                               2
BW058         4        1           1             2                                               2
BW059         4        1           1             2                                               2
BW061         3        1           1             1                                               1
BW062         3        1           1             1                                               1
BW064         3        1           1             1                                               1
BW067         4        1           1             2                                               2
BW071         4        1           1             2                                               2

[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
#%% md
## Choice prediction (claims `fig2d-prediction-accuracy` and `fig1g-example-mouse-prediction`)

> The best-fit GLM-HMM predicted 75.7% +/- 1.7% of choices, a 10.8% +/- 1.3% improvement over a one-state (static performance) model.

As 6_predictive_accuracy.py: per mouse, 5 folds, each holding out a contiguous block of 20% of every session's trials, the order of the blocks permuted per session; on the training trials, concatenated as one sequence, a one-state model and a model with the mouse's number of states are fit (flex_hmm.choice_hmm_fit, MAP), 5 initialisations each, the best by test log likelihood kept; each test trial's choice is predicted from the state the transition matrix makes most likely after the filtered state of the preceding test trials.
#%% code tags=claim:fig2d-prediction-accuracy
rng_pred = np.random.default_rng(6)
t0 = time.time()
tasks, meta = [], []
folds = {}
for subj in subjects:
    g = trials[trials.subject == subj].sort_values(["path", "trial_in_session"])
    X = np.c_[g.inpt.values, np.ones(len(g))]
    y = g.hmm_choice.values.astype(int)
    sess_idx = pd.factorize(g.path)[0]
    tr_i, te_i = hulsey.stratified_kfold_random_order(sess_idx, 5, rng_pred)
    folds[subj] = (X, y, tr_i, te_i)
    for f in range(5):
        for K in (1, n_states[subj]):
            for z in range(5):
                tasks.append((K, X[tr_i[f]], y[tr_i[f]], X[te_i[f]], y[te_i[f]], int(rng_pred.integers(2**31))))
                meta.append((subj, f, K))
res = hulsey.run_parallel(hulsey.fit_map_one, tasks)
print(f"{len(tasks)} fits in {(time.time() - t0) / 60:.1f} min")
acc = {}
for subj in subjects:
    X, y, tr_i, te_i = folds[subj]
    for K in (1, n_states[subj]):
        a = []
        for f in range(5):
            cand = [res[j] for j in range(len(res)) if meta[j] == (subj, f, K)]
            best = cand[int(np.argmax([c[1] for c in cand]))][0]
            pred = hulsey.predict_choices(best, X[te_i[f]], y[te_i[f]])
            a.append(np.mean(pred == y[te_i[f]]))
        acc[(subj, "one state" if K == 1 else "best")] = np.mean(a) * 100
acc = pd.Series(acc).unstack()
acc["states"] = pd.Series(n_states)
acc["gain (points)"] = acc.best - acc["one state"]
acc["gain (relative %)"] = (acc.best / acc["one state"] - 1) * 100
print(acc.round(2).to_string())
print(f"\nbest model: {acc.best.mean():.1f} +/- {acc.best.sem():.1f}%; one state: {acc['one state'].mean():.1f} +/- {acc['one state'].sem():.1f}%")
print(f"(a) gain in points: {acc['gain (points)'].mean():.1f} +/- {acc['gain (points)'].sem():.1f}; "
      f"(b) relative gain: {acc['gain (relative %)'].mean():.1f} +/- {acc['gain (relative %)'].sem():.1f}%")
print(f"best better in {int((acc['gain (points)'] > 0).sum())} of 13; Wilcoxon signed-rank p = {stats.wilcoxon(acc.best, acc['one state']).pvalue:.2g}; "
      f"rank-sum (variant, O4) p = {stats.ranksums(acc.best, acc['one state']).pvalue:.2g}")
#%% md
**Result: PREDICT**
#%% md
> For the example mouse, a 4-state GLM-HMM was selected; it predicted 78% of choices against 70% for a one-state model.

The example mouse is BW046 (Figure1.py, 7_example_mouse_decoding.py).
#%% code tags=claim:fig1g-example-mouse-prediction
print("BW046: states selected", n_states["BW046"], "(reading (a):", nst.loc["BW046", "(a) max"], ")")
print(f"BW046: one state {acc.loc['BW046', 'one state']:.1f}%, best model {acc.loc['BW046', 'best']:.1f}%")
#%% md
**Result: EXAMPLE**
EOF
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python run.py 26 33 2>&1 | grep -v Warning | sed -n '/cell 26/,$p'; date -u
```

```
===== cell 26 [code tags=claim:fig2c-dwell-times]
(y) code dwell
  (a) mean over mice of per-mouse median: {'disengaged': 11.9, 'optimal': 39.5, 'sub-optimal': 13.8}
  (b) mean over mice of per-mouse mean:   {'disengaged': 17.5, 'optimal': 70.6, 'sub-optimal': 23.5}
  (c) mean over all epochs pooled:        {'disengaged': 13.6, 'optimal': 46.1, 'sub-optimal': 19.6}
  optimal vs disengaged (medians): optimal longer in 12 of 13, p = 0.00049
  optimal vs disengaged (means): optimal longer in 13 of 13, p = 0.00024
  optimal vs sub-optimal (medians): optimal longer in 12 of 13, p = 0.00073
  optimal vs sub-optimal (means): optimal longer in 12 of 13, p = 0.00073
(x) run length
  (a) mean over mice of per-mouse median: {'disengaged': 11.4, 'optimal': 38.5, 'sub-optimal': 12.8}
  (b) mean over mice of per-mouse mean:   {'disengaged': 17.0, 'optimal': 69.6, 'sub-optimal': 22.5}
  (c) mean over all epochs pooled:        {'disengaged': 13.0, 'optimal': 45.2, 'sub-optimal': 18.6}
  optimal vs disengaged (medians): optimal longer in 12 of 13, p = 0.00073
  optimal vs disengaged (means): optimal longer in 13 of 13, p = 0.00024
  optimal vs sub-optimal (medians): optimal longer in 12 of 13, p = 0.00073
  optimal vs sub-optimal (means): optimal longer in 12 of 13, p = 0.00073

Median indeterminate dwell per mouse: {'BW041': 2, 'BW045': 4, 'BW046': 2, 'BW048': 5, 'BW051': 3, 'BW053': 4, 'BW058': 2, 'BW059': 4, 'BW061': 2, 'BW062': 3, 'BW064': 3, 'BW067': 1, 'BW071': 4}
mean +/- SEM over mice: 3.00 +/- 0.32 trials
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
#%% md
## Pupil diameter and the optimal state (claims `fig3c-inverted-u-pupil`, `fig3d-optimal-pupil-modality`, `fig3e-u-disengaged-pupil`)

> The probability of being in the optimal state follows an inverted-U function of pupil diameter, highest at intermediate diameters, in nearly all mice.

Sessions with more than 10 optimal-state trials and a post hoc pupil (claims file, M5). As 4_optimal_pupils.py: discrete-state trials with a pupil value are binned by pupil diameter in 0.02 bins (lower, upper]; per fold of a shuffled 5-fold split, P(optimal) per bin with more than 2 training or 3 test trials, polynomials of degree 1 to 7 fit to the training bins and scored by r2 on the test bins; the degree is the elbow of the mean r2 (largest height above the line from degree 1 to degree 7). As Figure3.py: P(state) per 0.02 bin [lower, upper) over trials with all six measures, for bins with more than 5 trials (a state absent from a bin is left missing, as the code does), the bins below the first one with a value merged into it; the polynomial of the selected degree is fit to P(optimal) and the optimal pupil is its maximum on a 0.001 grid within the range of the bins.
#%% code tags=claim:fig3c-inverted-u-pupil
MEAS6 = ["post_hoc_pupil_diameter", "post_hoc_pupil_std10", "face_energy", "face_std_10", "running_speed", "running_std10"]

def fig3_set(subj, sess_col="sess_opt10"):
    """Figure3.py / FigureS3_S4.py / FigureS8.py trials: the mouse's sessions in the set, all six
    measures present, the movement index z-scored over these trials."""
    g = trials[(trials.subject == subj) & trials[sess_col]].dropna(subset=MEAS6).copy()
    g["movement"] = stats.zscore(g.face_energy) + stats.zscore(g.running_speed)
    g["movement_std"] = stats.zscore(g.face_std_10) + stats.zscore(g.running_std10)
    return g

def p_state_bins(values, state, lo, hi, step, min_n=5, merge_low=True):
    """Figure3.py: P(optimal), P(disengaged), P(other) per bin [p, p + step) with more than min_n
    trials; a state absent from a bin stays NaN; bins below the first with an optimal value are merged into it."""
    st = np.where(state > 2, 2, state)
    edges = np.arange(lo, hi, step)
    out = np.full((len(edges), 3), np.nan)
    for k, p in enumerate(edges):
        sel = (values >= p) & (values < p + step)
        n = sel.sum()
        if n > min_n:
            for s_ in np.unique(st[sel]):
                out[k, int(s_)] = np.mean(st[sel] == s_)
    if merge_low and np.isfinite(out[:, 0]).any():
        k = np.where(np.isfinite(out[:, 0]))[0][0]
        sel = (values >= lo) & (values < lo + (k + 1) * step)
        if sel.sum() > min_n:
            for s_ in np.unique(st[sel]):
                out[k, int(s_)] = np.mean(st[sel] == s_)
    return edges, out

def cv_r2(values, opt, edges_lower, step, rng, degrees=range(1, 8)):
    """4_optimal_pupils.py: 5-fold shuffled split of trials; binned P(optimal) in (lower, upper]
    with more than 2 training and 3 test trials per bin; test r2 of polynomial fits per degree."""
    from sklearn.model_selection import KFold
    from sklearn.metrics import r2_score
    kf = KFold(n_splits=5, shuffle=True, random_state=int(rng.integers(2**31)))
    r2 = np.full((len(degrees), 5), np.nan)
    def binp(v, o, mn):
        y = np.full(len(edges_lower), np.nan)
        for i, lo in enumerate(edges_lower):
            sel = (v > lo) & (v <= lo + step)
            if sel.sum() > mn:
                y[i] = o[sel].mean()
        return y
    for f, (a, b) in enumerate(kf.split(values)):
        ytr, yte = binp(values[a], opt[a], 2), binp(values[b], opt[b], 3)
        x = np.asarray(edges_lower, dtype=np.float32)
        xtr, ytr2 = x[np.isfinite(ytr)], ytr[np.isfinite(ytr)]
        xte, yte2 = x[np.isfinite(yte)], yte[np.isfinite(yte)]
        for j, d in enumerate(degrees):
            c = np.polyfit(xtr, ytr2, d)
            r2[j, f] = r2_score(yte2, np.poly1d(c)(xte))
    return r2.mean(axis=1)

def elbow_degree(mean_r2):
    """4_optimal_pupils.py: the degree (2 to 6) whose mean r2 lies furthest above the line from degree 1 to 7."""
    x1, y1, x2, y2 = 0, mean_r2[0], 6, mean_r2[6]
    b = (x1 * y2 - x2 * y1) / (x1 - x2)
    m = (y1 - y2) / (x1 - x2)
    signs = [mean_r2[ii] - (m * ii + b) for ii in range(1, 6)]
    return int(np.argmax(signs) + 2)

rng3 = np.random.default_rng(3)
pupil_rows, curves_pupil = [], {}
for subj in subjects:
    g4 = trials[(trials.subject == subj) & trials.sess_opt10].dropna(subset=["post_hoc_pupil_diameter", "hmm_state"])
    r2 = cv_r2(g4.post_hoc_pupil_diameter.values, (g4.hmm_state.values == 0).astype(float), np.arange(0, 1, .02), .02, rng3)
    deg = elbow_degree(r2)
    g = fig3_set(subj).dropna(subset=["hmm_state"])
    edges, ps3 = p_state_bins(g.post_hoc_pupil_diameter.values, g.hmm_state.values, 0, 1, .02)
    curves_pupil[subj] = (edges, ps3)
    y = ps3[:, 0]
    x2, y2 = edges[np.isfinite(y)], y[np.isfinite(y)]
    xs = np.arange(x2[0], x2[-1], .001)
    fit = np.poly1d(np.polyfit(x2.astype(np.float32), y2.astype(np.float32), deg))(xs)
    opt_pupil = xs[np.argmax(fit)]
    c2 = np.polyfit(x2, y2, 2)
    pupil_rows.append({"subject": subj, "task": mods[subj], "trials": len(g), "bins": len(x2),
                       "range": f"{x2[0]:.2f}-{x2[-1]:.2f}", "degree": deg, "r2 deg2": r2[1],
                       "optimal pupil": opt_pupil, "fit at max": fit.max(), "fit at low end": fit[0], "fit at high end": fit[-1],
                       "(i) interior max, lower ends": bool(0 < np.argmax(fit) < len(fit) - 1 and fit[0] < fit.max() and fit[-1] < fit.max()),
                       "(ii) quad coef": c2[0]})
pupil_tab = pd.DataFrame(pupil_rows).set_index("subject")
print(pupil_tab.round(3).to_string())
n_i = int(pupil_tab["(i) interior max, lower ends"].sum())
n_ii = int((pupil_tab["(ii) quad coef"] < 0).sum())
print(f"\n(i) maximum inside the range with lower values at both ends: {n_i} of 13; (ii) negative quadratic term: {n_ii} of 13")
print("Readings of 'nearly all': (a) at least 12 of 13, (b) at least 11 of 13:",
      {"(i)": (n_i >= 12, n_i >= 11), "(ii)": (n_ii >= 12, n_ii >= 11)})
optimal_pupil = pupil_tab["optimal pupil"]
#%% code tags=claim:fig3c-inverted-u-pupil
fig, axes = plt.subplots(2, 7, figsize=(18, 5), sharey=True)
for ax, subj in zip(axes.ravel(), subjects):
    edges, ps3 = curves_pupil[subj]
    for k, c in zip(range(3), ["teal", "firebrick", "orange"]):
        ax.plot(edges, ps3[:, k], ".-", color=c, lw=1)
    ax.axvline(optimal_pupil[subj], color="k", ls=":")
    ax.set_title(subj, fontsize=9)
    ax.set_xlim(0, 1)
axes.ravel()[-1].axis("off")
fig.supxlabel("pupil diameter (fraction of session maximum)")
fig.supylabel("P(state): optimal teal, disengaged red, other orange")
plt.tight_layout()
plt.show()
print("All plotted values lie in [0, 1] on both axes; dotted line: optimal pupil.")
#%% md
**Result: INVU**
#%% md
> The optimal pupil diameter is smaller in mice performing the auditory task than in those performing the visual task.
#%% code tags=claim:fig3d-optimal-pupil-modality
aud = optimal_pupil[pupil_tab.task == "auditory"]
vis = optimal_pupil[pupil_tab.task == "visual"]
rs = stats.ranksums(aud, vis)
print("auditory:", aud.round(3).to_dict())
print("visual:", vis.round(3).to_dict())
print(f"median auditory {aud.median():.3f}, visual {vis.median():.3f}; Wilcoxon rank-sum p = {rs.pvalue:.3g}; "
      f"Mann-Whitney U exact p = {stats.mannwhitneyu(aud, vis).pvalue:.3g}")
#%% md
**Result: MODALITY**
#%% md
> Across mice, aligned to each mouse's optimal pupil, the probability of the optimal state is an inverted U and the probability of the disengaged state a U of pupil diameter; this holds also on trials when the mice were stationary.

As Figure3.py: each mouse's P(state) per 0.02 bin shifted so that the bin nearest its optimal pupil is at 0, and averaged over mice. The shape test is the claims file's: on bins with data from at least 7 of 13 mice, a second-order fit with a negative (optimal) or positive (disengaged) quadratic term and its vertex inside the range. Stationary trials, readings (a) locomotion speed exactly 0 and (b) below 0.02 m/s, with the same optimal pupils.
#%% code tags=claim:fig3e-u-disengaged-pupil
def shifted_mean(sel_fn):
    shifted = np.full((len(subjects), 3, 50), np.nan)
    x = np.arange(0, 1, .02)
    for i, subj in enumerate(subjects):
        g = fig3_set(subj).dropna(subset=["hmm_state"])
        g = g[sel_fn(g)]
        if len(g) == 0:
            continue
        _, ps3 = p_state_bins(g.post_hoc_pupil_diameter.values, g.hmm_state.values, 0, 1, .02)
        ob = np.argmin(np.abs(x - optimal_pupil[subj]))
        for j, b in enumerate(range(ob - 25, ob + 25)):
            if 0 <= b < 50:
                shifted[i, :, j] = ps3[b]
    return shifted

def shape(curve_by_mouse, k, sign):
    n = np.sum(np.isfinite(curve_by_mouse[:, k, :]), axis=0)
    mean = np.nanmean(curve_by_mouse[:, k, :], axis=0)
    keep = n >= 7
    xb = np.arange(-50, 50, 2)[keep]
    if keep.sum() < 3:
        return dict(bins=int(keep.sum()), quad=np.nan, vertex=np.nan, holds=False)
    c = np.polyfit(xb, mean[keep], 2)
    vx = -c[1] / (2 * c[0])
    return dict(bins=int(keep.sum()), range=f"{xb[0]} to {xb[-1]}", quad=c[0], vertex=round(vx, 1),
                holds=bool(np.sign(c[0]) == sign and xb[0] < vx < xb[-1]))

shift_res = {}
for name, fn in [("all trials", lambda g: np.ones(len(g), bool)),
                 ("(a) stationary, speed == 0", lambda g: g.running_speed.values == 0),
                 ("(b) stationary, speed < 0.02 m/s", lambda g: g.running_speed.values < 0.02)]:
    sh = shifted_mean(fn)
    shift_res[name] = sh
    o, d = shape(sh, 0, -1), shape(sh, 1, +1)
    nt = sum(int(fn(fig3_set(s_).dropna(subset=["hmm_state"])).sum()) for s_ in subjects)
    print(f"{name} ({nt} trials): optimal {o}\n    disengaged {d}")
fig, ax = plt.subplots(1, 3, figsize=(14, 3.5), sharey=True)
for a, (name, sh) in zip(ax, shift_res.items()):
    for k, c in zip(range(3), ["teal", "firebrick", "orange"]):
        a.plot(np.arange(-50, 50, 2), np.nanmean(sh[:, k, :], axis=0), color=c)
    a.set_title(name, fontsize=9)
    a.set_xlabel("pupil minus optimal pupil (% of max)")
ax[0].set_ylabel("mean P(state) over mice")
plt.tight_layout()
plt.show()
print("x from -50 to 48 % of max; y in [0, 1].")
#%% md
**Result: SHIFT**
EOF
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python run.py 33 42 2>&1 | grep -v Warning | sed -n '/cell 3[3-9]/,$p'; date -u
```

```
===== cell 35 [code tags=claim:fig3c-inverted-u-pupil]
             task  trials  bins      range  degree  r2 deg2  optimal pupil  fit at max  fit at low end  fit at high end  (i) interior max, lower ends  (ii) quad coef
subject                                                                                                                                                              
BW041      visual   10456    24  0.50-0.96       2    0.762          0.698       0.752           0.380            0.111                          True          -9.442
BW045    auditory   14768    30  0.38-0.96       3    0.712          0.562       0.569           0.161            0.120                          True          -4.043
BW046      visual    7513    19  0.60-0.98       2    0.727          0.807       0.682          -0.008            0.203                          True         -16.147
BW048      visual    8081    22  0.54-0.96       3    0.562          0.662       0.448           0.285            0.057                          True          -4.940
BW051      visual    9366    22  0.56-0.98       2    0.086          0.798       0.763           0.244            0.463                          True          -9.170
BW053    auditory    8148    33  0.02-0.94       2    0.751          0.385       0.681           0.340           -0.103                          True          -2.558
BW058      visual    4411    21  0.52-0.94       3    0.422          0.682       0.757          -0.057            0.400                          True         -11.846
BW059    auditory    8520    22  0.54-0.96       2    0.788          0.689       0.752           0.475           -0.156                          True         -12.472
BW061    auditory    8790    29  0.42-0.98       3    0.549          0.420       1.015           1.015           -0.040                         False          -4.500
BW062    auditory    6224    24  0.50-0.96       2    0.871          0.710       0.753           0.192           -0.042
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
#%% md
## Movement measures and the optimal state (claims `figs4-r2-individual-movement`, `fig3f-movement-index-inverted-u`, `fig3f-movement-index-u-disengaged`, `figs5-movement-index-correlations`)

> Second-order cross-validated regression fits of optimal-state probability are poorer for face motion energy (r2 0.49 +/- 0.08) and locomotion speed (0.44 +/- 0.07) than for pupil diameter (0.72 +/- 0.03).

The cross-validated r2 of a degree-2 fit as 4_optimal_pupils.py computes it (above), for pupil on its own trial set, and for face motion energy, locomotion speed and the movement index on the Figure3.py trial set (sessions of M5, six measures present). Bins, O5: (a) the plotting bins of FigureS3_S4.py and Figure3.py (face 0.05 from 0 to 1, locomotion 0.02 m/s from -0.02 to 0.30, movement index 0.25 from -5 to 5); (b) 50 equal-width bins over each mouse's range.
#%% code tags=claim:figs4-r2-individual-movement
rng4 = np.random.default_rng(4)
BINS_A = {"face_energy": (0, 1, .05), "running_speed": (-.02, .301, .02), "movement": (-5, 5, .25)}
r2rows = []
for subj in subjects:
    g = fig3_set(subj).dropna(subset=["hmm_state"])
    opt = (g.hmm_state.values == 0).astype(float)
    row = {"subject": subj, "pupil": pupil_tab.loc[subj, "r2 deg2"]}
    for meas, (lo, hi, step) in BINS_A.items():
        v = g[meas].values
        row[f"{meas} (a)"] = cv_r2(v, opt, np.arange(lo, hi, step), step, rng4, degrees=[1, 2])[1]
        stepb = (v.max() - v.min()) / 50
        row[f"{meas} (b)"] = cv_r2(v, opt, v.min() - 1e-9 + np.arange(50) * stepb, stepb, rng4, degrees=[1, 2])[1]
    r2rows.append(row)
r2tab = pd.DataFrame(r2rows).set_index("subject")
print(r2tab.round(3).to_string())
print("\nmean +/- SEM over mice:", {c: f"{r2tab[c].mean():.2f} +/- {r2tab[c].sem():.2f}" for c in r2tab.columns})
for c in r2tab.columns[1:]:
    w = stats.wilcoxon(r2tab[c], r2tab.pupil)
    print(f"{c} vs pupil: difference {np.mean(r2tab[c] - r2tab.pupil):+.2f}, lower in {int((r2tab[c] < r2tab.pupil).sum())} of 13, p = {w.pvalue:.3g}")
#%% md
**Result: R2MOVE**
#%% md
> Optimal-state probability peaks at intermediate values of the movement index, an inverted U similar to pupil diameter (cross-validated r2 0.63 +/- 0.06, not different from pupil).

The movement index is the sum of the z-scored face motion energy and locomotion speed over the trials of the Figure3.py set (M4). Its r2 and the test against pupil are in the table above (rows `movement`). The shape is tested on the mean P(optimal) curve over the 0.25 bins of Figure3.py, as for pupil.
#%% code tags=claim:fig3f-movement-index-inverted-u
mv = np.full((len(subjects), 3, 40), np.nan)
for i, subj in enumerate(subjects):
    g = fig3_set(subj).dropna(subset=["hmm_state"])
    _, ps3 = p_state_bins(g.movement.values, g.hmm_state.values, -5, 5, .25, merge_low=False)
    mv[i] = ps3.T

def shape_x(curves, k, sign, xb_all):
    n = np.sum(np.isfinite(curves[:, k, :]), axis=0)
    mean = np.nanmean(curves[:, k, :], axis=0)
    keep = n >= 7
    xb = xb_all[keep]
    c = np.polyfit(xb, mean[keep], 2)
    vx = -c[1] / (2 * c[0])
    return dict(bins=int(keep.sum()), range=f"{xb[0]} to {xb[-1]}", quad=round(c[0], 4), vertex=round(vx, 2),
                peak_bin_of_mean=float(xb[np.argmax(mean[keep])] if sign < 0 else xb[np.argmin(mean[keep])]),
                holds=bool(np.sign(c[0]) == sign and xb[0] < vx < xb[-1]))

xmv = np.arange(-5, 5, .25)
print("optimal:", shape_x(mv, 0, -1, xmv))
for c in ["movement (a)", "movement (b)"]:
    print(f"{c}: r2 {r2tab[c].mean():.2f} +/- {r2tab[c].sem():.2f}; vs pupil difference {np.mean(r2tab[c] - r2tab.pupil):+.2f}, "
          f"p = {stats.wilcoxon(r2tab[c], r2tab.pupil).pvalue:.3g}")
fig, ax = plt.subplots(figsize=(5, 3.5))
for k, c in zip(range(3), ["teal", "firebrick", "orange"]):
    ax.plot(xmv, np.nanmean(mv[:, k, :], axis=0), color=c)
ax.set_xlabel("movement index (bins of 0.25)")
ax.set_ylabel("mean P(state) over mice")
plt.tight_layout()
plt.show()
print("x from -5 to 4.75; y in [0, 1]; bins with fewer than 7 mice are included in the plot but not in the fit.")
#%% md
**Result: MOVEINVU**
#%% md
> The probability of the disengaged state is a U-shaped function of the movement index.
#%% code tags=claim:fig3f-movement-index-u-disengaged
print("disengaged:", shape_x(mv, 1, +1, xmv))
#%% md
**Result: MOVEU**
#%% md
> The movement index is equally correlated with face motion energy and with locomotion speed, and highly correlated with both in each mouse.
#%% code tags=claim:figs5-movement-index-correlations
cr = []
for subj in subjects:
    g = fig3_set(subj)
    cr.append({"subject": subj, "r face": stats.pearsonr(g.movement, g.face_energy)[0],
               "r locomotion": stats.pearsonr(g.movement, g.running_speed)[0]})
cr = pd.DataFrame(cr).set_index("subject")
cr["difference"] = cr["r face"] - cr["r locomotion"]
print(cr.round(4).to_string())
print(f"\nlargest |difference| {cr.difference.abs().max():.4f}; smallest r {cr[['r face', 'r locomotion']].min().min():.3f}; "
      f"(a) both above 0.7 in every mouse: {bool((cr[['r face', 'r locomotion']] > .7).all().all())}; "
      f"(b) above 0.5: {bool((cr[['r face', 'r locomotion']] > .5).all().all())}")
#%% md
**Result: S5CORR**
#%% md
## Raw measures by state (claims `fig3-distance-from-optimal-pupil`, `fig3-raw-face-energy-trend`, `fig3-raw-locomotion-no-difference`)

Per mouse, the mean at stimulus onset over the trials of each state, sub-optimal states pooled; sessions read both ways of O3: (a) sessions with more than 10 optimal-state trials and a post hoc pupil (Figure3.py), (b) all included sessions. Each measure's trials are those where it is present.
#%% code tags=claim:fig3-distance-from-optimal-pupil
def by_state(col, sess_col, fn=lambda g, c: g[c]):
    rows = []
    for subj in subjects:
        g = trials[(trials.subject == subj)]
        if sess_col:
            g = g[g[sess_col]]
        v = fn(g, col)
        st = g.hmm_state
        rows.append({"subject": subj, "optimal": v[st == 0].mean(), "disengaged": v[st == 1].mean(), "sub-optimal": v[st > 1].mean()})
    return pd.DataFrame(rows).set_index("subject")

def report(tab, scale, larger=None):
    m_, se_ = tab.mean() * scale, tab.sem() * scale
    print("   mean +/- SEM:", {k: f"{m_[k]:.3f} +/- {se_[k]:.3f}" for k in tab.columns})
    for other in ["disengaged", "sub-optimal"]:
        w = stats.wilcoxon(tab.optimal, tab[other])
        print(f"   optimal vs {other}: difference {np.mean(tab.optimal - tab[other]) * scale:+.3f}, "
              f"optimal lower in {int((tab.optimal < tab[other]).sum())} of 13, p = {w.pvalue:.2g}")

dist = lambda g, c: (g[c] - g.subject.map(optimal_pupil)).abs()
for label, sc in [("(a) sessions with >10 optimal trials and pupil", "sess_opt10"), ("(b) all included sessions", None)]:
    print("Absolute difference from the optimal pupil (% of session maximum),", label)
    report(by_state("post_hoc_pupil_diameter", sc, dist), 100)
#%% md
**Result: DIST**
#%% code tags=claim:fig3-raw-face-energy-trend
for label, sc in [("(a)", "sess_opt10"), ("(b)", None)]:
    print("Face motion energy (a.u.)", label)
    report(by_state("face_energy", sc), 1)
#%% md
**Result: FACE**
#%% code tags=claim:fig3-raw-locomotion-no-difference
for label, sc in [("(a)", "sess_opt10"), ("(b)", None)]:
    print("Locomotion speed (m/s)", label)
    report(by_state("running_speed", sc), 1)
#%% md
**Result: LOCO**
EOF
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python run.py 42 64 2>&1 | grep -v Warning | sed -n '/cell 42/,$p'; date -u
```

```
===== cell 42 [code tags=claim:fig3e-u-disengaged-pupil]
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run.py", line 20, in <module>
    exec(compile(body, f'cell{i}', 'exec'), ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell42", line 32, in <module>
  File "cell42", line 5, in shifted_mean
NameError: name 'fig3_set' is not defined
Sat Oct 31 10:04:36 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python run.py 33 64 2>&1 | grep -v Warning | sed -n '/cell 42/,$p'; date -u
```

```
===== cell 42 [code tags=claim:fig3e-u-disengaged-pupil]
all trials (109646 trials): optimal {'bins': 22, 'range': '-12 to 30', 'quad': np.float64(-0.0005728624597519658), 'vertex': np.float64(0.1), 'holds': True}
    disengaged {'bins': 22, 'range': '-12 to 30', 'quad': np.float64(0.0004688296525358962), 'vertex': np.float64(0.5), 'holds': True}
(a) stationary, speed == 0 (1881 trials): optimal {'bins': 0, 'quad': nan, 'vertex': nan, 'holds': False}
    disengaged {'bins': 1, 'quad': nan, 'vertex': nan, 'holds': False}
(b) stationary, speed < 0.02 m/s (32648 trials): optimal {'bins': 20, 'range': '-12 to 26', 'quad': np.float64(-0.00033753462670574444), 'vertex': np.float64(-0.7), 'holds': True}
    disengaged {'bins': 20, 'range': '-12 to 26', 'quad': np.float64(0.00029574372883412674), 'vertex': np.float64(-3.4), 'holds': True}
x from -50 to 48 % of max; y in [0, 1].
----- 0.9s
===== cell 45 [code tags=claim:figs4-r2-individual-movement]
         pupil  face_energy (a)  face_energy (b)  running_speed (a)  running_speed (b)  movement (a)  movement (b)
subject                                                                                                           
BW041    0.762            0.559            0.652             -0.076              0.220         0.692         0.542
BW045    0.712            0.628            0.355              0.797              0.681         0.480         0.375
BW046    0.727            0.494            0.225              0.518              0.094         0.237         0.179
BW048    0.562            0.464            0.376              0.545              0.117         0.339         0.336
BW051    0.086            0.756            0.689              0.776              0.543         0.826         0.769
BW053    0.751            0.234            0.351              0.408             -0.090         0.393         0.458
BW058    0.422            0.869            0.852              0.565              0.200         0.759         0.763
BW059    0
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hz/hulsey2023/hulsey2023_analysis/figure_generation_code; grep -n "these_states\|all_r\[\|corrcoef\|pearsonr\|query" FigureS6.py | head -30
```

```
51:        if all([len(trials.query('hmm_state==0'))>10,np.isin('post_hoc_pupil_diameter',trials.columns)]):
56:        all_trials=all_trials.query(measure+'=='+measure) 
59:        state_trials = all_trials.query('hmm_state==@state')
64:        r = round(np.corrcoef(fme,pup)[0,1],3)        
65:        all_r[m,0,state] = r
66:        r = round(np.corrcoef(loc,pup)[0,1],3)        
67:        all_r[m,1,state] = r
68:        r = round(np.corrcoef(loc,fme)[0,1],3)        
69:        all_r[m,2,state] = r
71:    state_trials = all_trials.query('hmm_state>1')
75:    r = round(np.corrcoef(fme,pup)[0,1],3)        
76:    all_r[m,0,2] = r
77:    r = round(np.corrcoef(loc,pup)[0,1],3)        
78:    all_r[m,1,2] = r
79:    r = round(np.corrcoef(loc,fme)[0,1],3)        
80:    all_r[m,2,2] = r
83:    state_trials = all_trials.query('hmm_state!=hmm_state')
87:    r = round(np.corrcoef(fme,pup)[0,1],3)        
88:    all_r[m,0,3] = r
89:    r = round(np.corrcoef(loc,pup)[0,1],3)        
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
#%% md
## Variability of the measures (claims `fig4a-lower-variability`, `fig4b-variability-at-transitions`)

> The 10-trial variability of pupil diameter, face motion energy and locomotion speed is lower in the optimal state than in the disengaged and sub-optimal states.

As Figure4.py: all included sessions, trials with the three 10-trial standard deviations and the pupil present; per mouse the mean of each standard deviation over the trials of each state, sub-optimal states pooled.
#%% code tags=claim:fig4a-lower-variability
STD3 = ["post_hoc_pupil_std10", "face_std_10", "running_std10"]
fig4 = {}
for subj in subjects:
    g = trials[trials.subject == subj].dropna(subset=STD3 + ["post_hoc_pupil_diameter"]).copy()
    g["movement"] = stats.zscore(g.face_energy) + stats.zscore(g.running_speed)
    fig4[subj] = g
n_tests = 0
for meas in STD3:
    tab = pd.DataFrame({subj: {"optimal": g.loc[g.hmm_state == 0, meas].mean(), "disengaged": g.loc[g.hmm_state == 1, meas].mean(),
                               "sub-optimal": g.loc[g.hmm_state > 1, meas].mean()} for subj, g in fig4.items()}).T
    print(meas, "mean over mice:", tab.mean().round(4).to_dict())
    for other in ["disengaged", "sub-optimal"]:
        w = stats.wilcoxon(tab.optimal, tab[other])
        n_tests += (w.pvalue < 0.05) and (tab.optimal.mean() < tab[other].mean())
        print(f"   optimal vs {other}: difference {np.mean(tab.optimal - tab[other]):+.4f}, optimal lower in "
              f"{int((tab.optimal < tab[other]).sum())} of 13, p = {w.pvalue:.2g}")
print("tests with the optimal state lower at p < 0.05:", int(n_tests), "of 6")
#%% md
**Result: VAR**
#%% md
> Variability of the measures decreases on entering the optimal state and increases on leaving it.

As Figure4.py: optimal epochs from flex_hmm.get_dwell_times on all included sessions with a code dwell above 9; entries from a discrete non-optimal epoch and exits to one; the 10-trial standard deviation over the 10 trials before and the 10 after the boundary, averaged per mouse; the test compares position 10 (the last trial before the entry, or the last optimal trial) with position 20.
#%% code tags=claim:fig4b-variability-at-transitions
enter_means, exit_means = {m: [] for m in STD3}, {m: [] for m in STD3}
n_trans = {}
for subj in subjects:
    g = trials[trials.subject == subj].sort_values(["path", "trial_in_session"])
    E = {m: [] for m in STD3}
    X_ = {m: [] for m in STD3}
    ne = nx = 0
    for path, sg in g.groupby("path"):
        dt = hulsey.dwell_table(sg.hmm_state.values)
        for SI in np.where(dt.state.values == 0)[0]:
            if dt.dwell.iloc[SI] <= 9:
                continue
            start, end = dt.first_trial.iloc[SI], dt.last_trial.iloc[SI]
            prior = dt.state.iloc[SI - 1] if SI > 0 else np.nan
            nxt = dt.state.iloc[SI + 1] if SI < len(dt) - 1 else np.nan
            for m in STD3:
                v = sg[m].values
                a, b = v[start - 10:start + 10], v[end - 10:end + 10]
                if prior > 0 and len(a) == 20:
                    E[m].append(a)
                if nxt > 0 and len(b) == 20:
                    X_[m].append(b)
            ne += prior > 0
            nx += nxt > 0
    for m in STD3:
        enter_means[m].append(np.nanmean(E[m], axis=0))
        exit_means[m].append(np.nanmean(X_[m], axis=0))
    n_trans[subj] = (ne, nx)
print("transitions per mouse (entries, exits):", n_trans)
fig, ax = plt.subplots(1, 3, figsize=(13, 3))
for i, m in enumerate(STD3):
    en, ex = np.array(enter_means[m]), np.array(exit_means[m])
    we, wx = stats.wilcoxon(en[:, 9], en[:, 19]), stats.wilcoxon(ex[:, 9], ex[:, 19])
    print(f"{m}: entry {np.mean(en[:, 9]):.4f} -> {np.mean(en[:, 19]):.4f} (lower after in {int((en[:, 19] < en[:, 9]).sum())} of 13, p = {we.pvalue:.2g}); "
          f"exit {np.mean(ex[:, 9]):.4f} -> {np.mean(ex[:, 19]):.4f} (higher after in {int((ex[:, 19] > ex[:, 9]).sum())} of 13, p = {wx.pvalue:.2g})")
    ax[i].plot(np.arange(-10, 10), (en - en.mean(1, keepdims=True)).mean(0), label="entry")
    ax[i].plot(np.arange(-10, 10), (ex - ex.mean(1, keepdims=True)).mean(0), label="exit")
    ax[i].axvline(0, color="k", lw=.5)
    ax[i].set_title(m, fontsize=9)
ax[0].legend()
ax[0].set_ylabel("mean-subtracted 10-trial SD")
ax[1].set_xlabel("trials from the boundary")
plt.tight_layout()
plt.show()
#%% md
**Result: TRANS**
#%% md
## Coupling of pupil and movement (claims `fig4d-pupil-movement-decoupling`, `figs6-individual-measure-decoupling`)

> The correlation between pupil diameter and the movement index is lower during the optimal state than during the disengaged and sub-optimal states.

As Figure4.py: the trial set of `fig4a`, per mouse and state the Pearson r between movement index and pupil diameter.
#%% code tags=claim:fig4d-pupil-movement-decoupling
rr = pd.DataFrame({subj: {"optimal": np.corrcoef(g.loc[g.hmm_state == 0, "movement"], g.loc[g.hmm_state == 0, "post_hoc_pupil_diameter"])[0, 1],
                          "disengaged": np.corrcoef(g.loc[g.hmm_state == 1, "movement"], g.loc[g.hmm_state == 1, "post_hoc_pupil_diameter"])[0, 1],
                          "sub-optimal": np.corrcoef(g.loc[g.hmm_state > 1, "movement"], g.loc[g.hmm_state > 1, "post_hoc_pupil_diameter"])[0, 1]}
                   for subj, g in fig4.items()}).T
print(rr.round(3).to_string())
print("mean:", rr.mean().round(3).to_dict())
for a_, b_ in [("optimal", "disengaged"), ("optimal", "sub-optimal"), ("disengaged", "sub-optimal")]:
    print(f"{a_} vs {b_}: difference {np.mean(rr[a_] - rr[b_]):+.3f}, first lower in {int((rr[a_] < rr[b_]).sum())} of 13, "
          f"p = {stats.wilcoxon(rr[a_], rr[b_]).pvalue:.2g}")
#%% md
**Result: DECOUPLE**
#%% md
> The correlations of pupil diameter with face motion energy and with locomotion speed are also reduced during the optimal state.

As FigureS6.py: sessions of M5 with the six measures present; per mouse and state the Pearson r.
#%% code tags=claim:figs6-individual-measure-decoupling
for a_m, b_m in [("face_energy", "post_hoc_pupil_diameter"), ("running_speed", "post_hoc_pupil_diameter"), ("running_speed", "face_energy")]:
    tab = {}
    for subj in subjects:
        g = fig3_set(subj)
        tab[subj] = {nm: np.corrcoef(g.loc[sel, a_m], g.loc[sel, b_m])[0, 1]
                     for nm, sel in [("optimal", g.hmm_state == 0), ("disengaged", g.hmm_state == 1), ("sub-optimal", g.hmm_state > 1)]}
    tab = pd.DataFrame(tab).T
    print(f"r({a_m}, {b_m}) mean over mice:", tab.mean().round(3).to_dict())
    for other in ["disengaged", "sub-optimal"]:
        print(f"   optimal vs {other}: difference {np.mean(tab.optimal - tab[other]):+.3f}, optimal lower in "
              f"{int((tab.optimal < tab[other]).sum())} of 13, p = {stats.wilcoxon(tab.optimal, tab[other]).pvalue:.2g}")
#%% md
**Result: S6**
#%% md
## Trial history and evoked pupil (claim `figs1-iti-independence`)

> The inter-trial interval is long enough that trial-evoked responses do not carry over; correlations of the measures at trial start with the prior ITI are weak and centered on zero, and evoked pupil responses do not differ across performance states.

As FigureS1.py on all included sessions: the ITI is the difference between consecutive trial start times within a session; per mouse, Pearson r of each measure at stimulus onset with the preceding ITI (the pupil value at onset is used for the code's trace sample 1 ms later); the evoked response is the signed larger of the largest rise and fall of pupil within 2.5 s of onset; per mouse the median per group, and a Kruskal-Wallis test over mice.
#%% code tags=claim:figs1-iti-independence
itr, ev = [], []
for subj in subjects:
    g = trials[trials.subject == subj].sort_values(["path", "trial_in_session"]).copy()
    g["iti"] = g.groupby("path").start_time.diff()
    g = g.dropna(subset=["evoked_pupil", "post_hoc_pupil_diameter", "iti", "running_speed", "face_energy"])
    itr.append({"subject": subj, **{m: stats.pearsonr(g.iti, g[m])[0] for m in ["post_hoc_pupil_diameter", "running_speed", "face_energy"]}})
    ev.append({"subject": subj, "optimal": g.loc[g.hmm_state == 0, "evoked_pupil"].median() * 100,
               "disengaged": g.loc[g.hmm_state == 1, "evoked_pupil"].median() * 100,
               "sub-optimal": g.loc[g.hmm_state > 1, "evoked_pupil"].median() * 100,
               "indeterminate": g.loc[g.hmm_state.isna(), "evoked_pupil"].median() * 100})
itr = pd.DataFrame(itr).set_index("subject")
ev = pd.DataFrame(ev).set_index("subject")
print("r with the preceding ITI:")
print(itr.round(3).to_string())
for m in itr.columns:
    print(f"{m}: median r {itr[m].median():+.3f}, Wilcoxon against 0 p = {stats.wilcoxon(itr[m]).pvalue:.2g}; "
          f"(a) |median| < 0.1: {abs(itr[m].median()) < .1}, (b) < 0.2: {abs(itr[m].median()) < .2}")
print("\nmedian evoked pupil response per mouse (% of max):")
print(ev.round(2).to_string())
kw4 = stats.kruskal(*[ev[c] for c in ev.columns])
kw3 = stats.kruskal(*[ev[c] for c in ["optimal", "disengaged", "sub-optimal"]])
print(f"Kruskal-Wallis, four groups: H = {kw4.statistic:.2f}, p = {kw4.pvalue:.2g}; three discrete states (variant): p = {kw3.pvalue:.2g}")
print("group means:", ev.mean().round(2).to_dict())
#%% md
**Result: S1**
#%% md
## Regression of state probabilities on the measures (claims `figs8a-regression-weights`, `figs8b-pupil-movement-interaction`)

> In linear regressions of state probability on the measures, the quadratic weights of pupil diameter and of locomotion speed are negative for the optimal state and positive for the disengaged state, as are the weights of their 10-trial SDs, while face motion energy weights center on zero.

As FigureS8.py: sessions of M5 with the six measures; per mouse, OLS of each state's posterior on the min-max scaled design (constant, pupil P, face F, locomotion L, their squares and products, their 10-trial SDs, and P*F*L; the design scaled again); second model on pupil, movement index M, their squares and product, the pupil SD and the movement SD index.
#%% code tags=claim:figs8a-regression-weights
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
names1 = ["1", "P", "F", "L", "P*P", "P*F", "P*L", "F*F", "F*L", "L*L", "Pstd", "Fstd", "Lstd", "P*F*L"]
names2 = ["1", "P", "M", "P*P", "P*M", "M*M", "Pstd", "Mstd"]
W1, W2 = [], []
for subj in subjects:
    g = fig3_set(subj)
    mm = MinMaxScaler()
    X = mm.fit_transform(g[["post_hoc_pupil_diameter", "face_energy", "running_speed"]].values)
    S = mm.fit_transform(g[["post_hoc_pupil_std10", "face_std_10", "running_std10"]].values)
    X2 = mm.fit_transform(np.c_[g.post_hoc_pupil_diameter.values, g.movement.values])
    pf = PolynomialFeatures(degree=2)
    A1 = mm.fit_transform(np.c_[pf.fit_transform(X), S, X[:, 0] * X[:, 1] * X[:, 2]])
    A1[:, 0] = 1
    A2 = mm.fit_transform(np.c_[pf.fit_transform(X2), g.post_hoc_pupil_std10.values, g.movement_std.values])
    A2[:, 0] = 1
    for k in range(n_states[subj]):
        yk = g[f"state_{k + 1}_prob"].values
        grp = "optimal" if k == 0 else "disengaged" if k == 1 else "sub-optimal"
        W1.append({"subject": subj, "state": grp, **dict(zip(names1, sm.OLS(yk, A1).fit().params))})
        W2.append({"subject": subj, "state": grp, **dict(zip(names2, sm.OLS(yk, A2).fit().params))})
W1, W2 = pd.DataFrame(W1), pd.DataFrame(W2)
rows = []
for grp in ["optimal", "disengaged"]:
    w = W1[W1.state == grp]
    for term in ["P*P", "L*L", "F*F", "Pstd", "Lstd", "Fstd"]:
        rows.append({"state": grp, "term": term, "median": w[term].median(), "mean": w[term].mean(),
                     "positive": int((w[term] > 0).sum()), "p (vs 0)": stats.wilcoxon(w[term]).pvalue})
s8 = pd.DataFrame(rows)
print(s8.round(3).to_string(index=False))
#%% md
**Result: S8A**
#%% md
> With the movement index, the quadratic movement weight is negative for the optimal state, and the pupil-by-movement interaction is the only consistent weight for sub-optimal states (0.42 +/- 0.11), differing from its weight for the optimal state (-0.95 +/- 0.21).
#%% code tags=claim:figs8b-pupil-movement-interaction
for grp in ["optimal", "disengaged", "sub-optimal"]:
    w = W2[W2.state == grp]
    print(grp, f"({len(w)} fits): mean +/- SEM", {t: f"{w[t].mean():.2f} +/- {w[t].sem():.2f}" for t in names2[1:]})
    print("   Wilcoxon vs 0 p:", {t: round(stats.wilcoxon(w[t]).pvalue, 3) for t in names2[1:]})
pm_s, pm_o = W2[W2.state == "sub-optimal"]["P*M"], W2[W2.state == "optimal"]["P*M"]
print(f"P*M sub-optimal {pm_s.mean():.2f} +/- {pm_s.sem():.2f} vs optimal {pm_o.mean():.2f} +/- {pm_o.sem():.2f}; "
      f"rank-sum p = {stats.ranksums(pm_s, pm_o).pvalue:.2g}")
print(f"M*M optimal mean {W2[W2.state == 'optimal']['M*M'].mean():.2f}")
#%% md
**Result: S8B**
EOF
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python run.py 33 90 2>&1 | grep -v Warning | sed -n '/cell 6[4-9]/,$p'; date -u
```

```
===== cell 64 [code tags=claim:fig4a-lower-variability]
post_hoc_pupil_std10 mean over mice: {'optimal': 0.027, 'disengaged': 0.0452, 'sub-optimal': 0.0333}
   optimal vs disengaged: difference -0.0182, optimal lower in 13 of 13, p = 0.00024
   optimal vs sub-optimal: difference -0.0063, optimal lower in 11 of 13, p = 0.01
face_std_10 mean over mice: {'optimal': 0.0667, 'disengaged': 0.0911, 'sub-optimal': 0.0745}
   optimal vs disengaged: difference -0.0244, optimal lower in 11 of 13, p = 0.0024
   optimal vs sub-optimal: difference -0.0078, optimal lower in 10 of 13, p = 0.08
running_std10 mean over mice: {'optimal': 0.053, 'disengaged': 0.0796, 'sub-optimal': 0.0597}
   optimal vs disengaged: difference -0.0266, optimal lower in 11 of 13, p = 0.0012
   optimal vs sub-optimal: difference -0.0067, optimal lower in 10 of 13, p = 0.033
tests with the optimal state lower at p < 0.05: 5 of 6
----- 0.2s
===== cell 67 [code tags=claim:fig4b-variability-at-transitions]
transitions per mouse (entries, exits): {'BW041': (np.int64(52), np.int64(49)), 'BW045': (np.int64(85), np.int64(125)), 'BW046': (np.int64(49), np.int64(65)), 'BW048': (np.int64(55), np.int64(51)), 'BW051': (np.int64(61), np.int64(71)), 'BW053': (np.int64(16), np.int64(32)), 'BW058': (np.int64(20), np.int64(28)), 'BW059': (np.int64(74), np.int64(79)), 'BW061': (np.int64(17), np.int64(22)), 'BW062': (np.int64(65), np.int64(67)), 'BW064': (np.int64(39), np.int64(43)), 'BW067': (np.int64(29), np.int64(46)), 'BW071': (np.int64(15), np.int64(31))}
post_hoc_pupil_std10: entry 0.0316 -> 0.0289 (lower after in 8 of 13, p = 0.24); exit 0.0298 -> 0.0337 (higher after in 11 of 13, p = 0.0012)
face_std_10: entry 0.0750 -> 0.0715 (lower after in 8 of 13, p = 0.15); exit 0.0716 -> 0.0780 (higher after in 9 of 13, p = 0.057)
running_std10: entry 0.0582 -> 0.0540 (lower after in 7 of 13, p = 0.24); exit 0.0551 -> 0.0626 (higher after in 11 of 13, p = 0.0024)
----- 0.7s
===== cell 70 [code tags=claim:fig4d-pupil-movement-de
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; uv pip install -q statsmodels; cd $TMPDIR/dev; python run.py 33 90 2>&1 | grep -v Warning | sed -n '/cell 79/,$p'; date -u
```

```
===== cell 79 [code tags=claim:figs8a-regression-weights]
     state term  median   mean  positive  p (vs 0)
   optimal  P*P  -1.131 -1.412         1     0.001
   optimal  L*L  -1.066 -1.194         0     0.000
   optimal  F*F  -0.302 -0.246         5     0.376
   optimal Pstd  -0.295 -0.383         2     0.008
   optimal Lstd  -0.354 -0.267         4     0.027
   optimal Fstd  -0.035 -0.056         6     0.497
disengaged  P*P   1.113  0.975        12     0.000
disengaged  L*L   0.644  0.804        13     0.000
disengaged  F*F   0.223  0.141         9     0.497
disengaged Pstd   0.193  0.306        10     0.013
disengaged Lstd   0.187  0.213        11     0.008
disengaged Fstd   0.130  0.122         9     0.127
----- 2.1s
===== cell 82 [code tags=claim:figs8b-pupil-movement-interaction]
optimal (13 fits): mean +/- SEM {'P': '1.46 +/- 0.42', 'M': '2.16 +/- 0.33', 'P*P': '-1.40 +/- 0.36', 'P*M': '-0.82 +/- 0.23', 'M*M': '-1.52 +/- 0.29', 'Pstd': '-0.35 +/- 0.16', 'Mstd': '-0.29 +/- 0.12'}
   Wilcoxon vs 0 p: {'P': np.float64(0.002), 'M': np.float64(0.0), 'P*P': np.float64(0.0), 'P*M': np.float64(0.002), 'M*M': np.float64(0.0), 'Pstd': np.float64(0.04), 'Mstd': np.float64(0.048)}
disengaged (13 fits): mean +/- SEM {'P': '-0.88 +/- 0.26', 'M': '-1.46 +/- 0.25', 'P*P': '0.99 +/- 0.21', 'P*M': '0.25 +/- 0.19', 'M*M': '1.31 +/- 0.24', 'Pstd': '0.30 +/- 0.15', 'Mstd': '0.29 +/- 0.10'}
   Wilcoxon vs 0 p: {'P': np.float64(0.001), 'M': np.float64(0.0), 'P*P': np.float64(0.0), 'P*M': np.float64(0.244), 'M*M': np.float64(0.0), 'Pstd': np.float64(0.033), 'Mstd': np.float64(0.013)}
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python - <<'EOF'
import numpy as np, time
from sklearn import svm
rng=np.random.default_rng(0)
X=rng.random((2400,8)); y=(rng.random(2400)>0.5).astype(int); X[:,0]+=y*0.3
Xt=rng.random((600,8)); yt=(rng.random(600)>0.5).astype(int); Xt[:,0]+=yt*0.3
t=time.time()
for i in range(10): s=svm.SVC().fit(X,y); s.score(Xt,yt)
print((time.time()-t)/10)
Xs=X.copy(); Xs[:,0]=X[rng.permutation(2400),0]
t=time.time()
for i in range(10): s=svm.SVC().fit(Xs,y); s.score(Xt,yt)
print((time.time()-t)/10)
EOF
```

```
0.16243386268615723
0.2014392375946045
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; cat >> hulsey.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# State decoding (5_decoding.py)
# ---------------------------------------------------------------------------------------------

DECODE_MEASURES = ['post_hoc_pupil_diameter', 'post_hoc_pupil_std10', 'face_energy', 'face_std_10',
                   'running_speed', 'running_std10', 'movement', 'movement_std']
# columns shuffled in the training set, by condition (5_decoding.py shuffle_schedule, by index),
# plus "M only" (keep the movement index value and SD, shuffle all others; Figure 5C legend)
SHUFFLE = {0: [6, 7], 1: [2, 3, 4, 5], 2: [2, 3, 4, 5, 6, 7], 3: [0, 1, 4, 5, 6, 7], 4: [0, 1, 2, 3, 6, 7],
           5: [1, 2, 3, 4, 5], 6: [0, 1, 6, 7], 7: [2, 3, 6, 7], 8: [4, 5, 6, 7], 13: [],
           14: [0, 1, 2, 3, 4, 5, 6, 7], "M only": [0, 1, 2, 3, 4, 5]}


def svm_task(args):
    """Fit an RBF SVC (scikit-learn defaults) on the training fold with the condition's columns
    permuted across training trials (one permutation per run, shared by the columns, as the code)
    and return the test accuracy."""
    from sklearn import svm
    Xtr, ytr, Xte, yte, cols, seed = args
    Xtr = Xtr.copy()
    if cols:
        perm = np.random.default_rng(seed).permutation(len(Xtr))
        Xtr[:, cols] = Xtr[perm][:, cols]
    return svm.SVC(kernel="rbf").fit(Xtr, ytr).score(Xte, yte)
EOF
cat >> $TMPDIR/dev/nb.py <<'EOF'
#%% md
## Decoding the state from the measures (claims `fig5c-state-classification`, `figs7-pupil-best-raw-measure`, `fig5c-movement-index-best`)

> For every mouse, support vector machines on the value and 10-trial variability of the measures predict the performance state above chance, with 88.2% +/- 1.8% accuracy for optimal against disengaged and 77.7% +/- 2% for optimal against sub-optimal states.

As 5_decoding.py: sessions of M5; discrete-state trials with the six measures; the movement index and its SD z-scored over these trials; for each mouse, optimal against each other state when the two classes give more than 30 trials; at most 1500 trials per class, balanced, sampled at random; features min-max scaled; RBF SVC; 5-fold shuffled KFold; accuracy is the mean over folds and runs. In a run, the condition's columns are permuted across the training trials. The paper runs 1000 runs per condition; here the unshuffled condition needs one run (it does not vary), the shuffled conditions 3 runs, and the null (all columns shuffled) 20 runs, to fit the time limit (see the deviations). z = (accuracy - null mean) / null SD.
#%% code tags=claim:fig5c-state-classification
N_RUN_COND, N_RUN_NULL = 3, 20
rng5 = np.random.default_rng(5)
t0 = time.time()
clf = []
tasks, tmeta = [], []
for subj in subjects:
    g = trials[(trials.subject == subj) & trials.sess_opt10].dropna(subset=["hmm_state"] + MEAS6).copy()
    g["movement"] = stats.zscore(g.face_energy) + stats.zscore(g.running_speed)
    g["movement_std"] = stats.zscore(g.face_std_10) + stats.zscore(g.running_std10)
    for st in sorted(g.hmm_state.unique())[1:]:
        o = g[g.hmm_state == 0].sample(frac=1, random_state=int(rng5.integers(2**31)))
        t_ = g[g.hmm_state == st].sample(frac=1, random_state=int(rng5.integers(2**31)))
        n = min(len(o), len(t_), 1500)
        o, t_ = o.iloc[:n], t_.iloc[:n]
        y = np.r_[np.zeros(n), np.ones(n)]
        if len(y) <= 30:
            continue
        X = MinMaxScaler().fit_transform(np.r_[o[hulsey.DECODE_MEASURES].values, t_[hulsey.DECODE_MEASURES].values])
        cid = len(clf)
        clf.append({"subject": subj, "state": int(st), "type": "disengaged" if st == 1 else "sub-optimal",
                    "template": hulsey.STATE_NAMES[types[subj][int(st)]], "trials per class": n})
        from sklearn.model_selection import KFold
        for f, (a, b) in enumerate(KFold(5, shuffle=True, random_state=int(rng5.integers(2**31))).split(y)):
            for cond, cols in hulsey.SHUFFLE.items():
                nr = 1 if cond == 13 else N_RUN_NULL if cond == 14 else N_RUN_COND
                for r in range(nr):
                    tasks.append((X[a], y[a], X[b], y[b], cols, int(rng5.integers(2**31))))
                    tmeta.append((cid, cond, r, f))
res = hulsey.run_parallel(hulsey.svm_task, tasks)
print(f"{len(clf)} classifications, {len(tasks)} SVM fits in {(time.time() - t0) / 60:.1f} min")
acc5 = pd.DataFrame(tmeta, columns=["cid", "cond", "run", "fold"]).assign(acc=res)
per_run = acc5.groupby(["cid", "cond", "run"]).acc.mean()           # mean over folds
null = per_run.xs(14, level="cond").groupby("cid").agg(["mean", "std", lambda x: np.percentile(x, 95)])
null.columns = ["null mean", "null sd", "null p95"]
cond_acc = per_run.groupby(["cid", "cond"]).mean().unstack()
clf = pd.DataFrame(clf).join(null)
for cond in cond_acc.columns:
    clf[f"acc {cond}"] = cond_acc[cond] * 100
    clf[f"z {cond}"] = (cond_acc[cond] - clf["null mean"]) / clf["null sd"]
show = clf[["subject", "state", "type", "template", "trials per class", "acc 13", "acc 0", "null mean", "null sd", "z 13", "z 0"]].copy()
show["null mean"] *= 100
show["null sd"] *= 100
print(show.round(2).to_string(index=False))
for cond, label in [(13, "eight features unshuffled (condition 13)"), (0, "'All measures' of Figure5.py (condition 0)")]:
    for tp in ["disengaged", "sub-optimal"]:
        c = clf[clf.type == tp][f"acc {cond}"]
        print(f"{label}, optimal vs {tp}: {c.mean():.1f} +/- {c.sem():.1f}% over {len(c)} classifications")
    z = clf[f"z {cond}"]
    above95 = (clf[f"acc {cond}"] / 100 > clf["null p95"])
    print(f"   significant: (a) z > 1.98 {int((z > 1.98).sum())} of {len(z)}, (b) z > 1.645 {int((z > 1.645).sum())}, "
          f"(c) above the null's 95th percentile {int(above95.sum())}")
#%% md
**Result: DECODE**
#%% md
> Pupil diameter (value and variability) is the best single raw measure for state classification, better than face motion energy and only slightly better than locomotion speed.

Readings (a), Figure S7A: keep one measure's value and SD, shuffle all others (conditions 2 pupil, 3 face, 4 locomotion); (b), Figure S7B: shuffle one measure's value and SD with the movement index (conditions 6, 7, 8), comparing the drop from condition 13. Quantity (i) accuracy, (ii) z.
#%% code tags=claim:figs7-pupil-best-raw-measure
for reading, (cp, cf, cl), drop in [("(a) keep one", (2, 3, 4), False), ("(b) shuffle one", (6, 7, 8), True)]:
    for q in ["acc", "z"]:
        P, F, L = (clf[f"{q} {c}"] for c in (cp, cf, cl))
        if drop:
            base = clf[f"{q} 13"]
            P, F, L = base - P, base - F, base - L   # a larger drop means more information
        wf, wl = stats.wilcoxon(P, F), stats.wilcoxon(P, L)
        print(f"{reading}, {q}{' drop' if drop else ''}: pupil {P.mean():.2f}, face {F.mean():.2f}, locomotion {L.mean():.2f}; "
              f"pupil > face in {int((P > F).sum())} of {len(P)}, p = {wf.pvalue:.2g}; pupil > locomotion in {int((P > L).sum())}, p = {wl.pvalue:.2g}")
#%% md
**Result: S7**
#%% md
> The movement index is the best predictor of performance state, encoding more information about states than pupil diameter.

Main reading (Figure 5C legend): keep the movement index value and SD, shuffle all others ("M only"), against keeping only the pupil value and SD (condition 2). Variants: condition 5 of 5_decoding.py (movement index kept with the pupil value) and condition 1 (face and locomotion shuffled), the label "Movement index" of the final Figure5.py.
#%% code tags=claim:fig5c-movement-index-best
for label, cm in [("main: M only", "M only"), ("variant: condition 5", 5), ("variant: condition 1", 1)]:
    for q in ["acc", "z"]:
        M, P = clf[f"{q} {cm}"], clf[f"{q} 2"]
        w = stats.wilcoxon(M, P)
        print(f"{label}, {q}: movement {M.mean():.2f} vs pupil {P.mean():.2f}; movement higher in {int((M > P).sum())} of {len(M)}, p = {w.pvalue:.2g}")
#%% md
**Result: MOVEBEST**
EOF
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python run.py 33 99 2>&1 | grep -v Warning | sed -n '/cell 8[5-9]/,$p'; date -u
```

```
===== cell 85 [code tags=claim:fig5c-state-classification]
34 classifications, 8670 SVM fits in 5.7 min
subject  state        type    template  trials per class  acc 13  acc 0  null mean  null sd  z 13   z 0
  BW041      1  disengaged  disengaged              1366   87.74  87.21      50.23     4.90  7.66  7.55
  BW041      2 sub-optimal  avoid left              1500   75.50  74.87      50.16     3.66  6.93  6.75
  BW045      1  disengaged  disengaged              1500   82.73  82.14      50.26     3.82  8.49  8.34
  BW045      2 sub-optimal  bias right              1500   59.53  58.39      49.57     1.41  7.08  6.27
  BW045      3 sub-optimal avoid right              1296   86.65  86.25      49.39     7.02  5.31  5.25
  BW046      1  disengaged  disengaged               628   76.83  75.93      49.45     4.13  6.64  6.42
  BW046      2 sub-optimal  bias right               862   76.91  76.68      50.17     2.65 10.10 10.02
  BW046      3 sub-optimal   bias left              1301   69.49  68.22      49.62     2.15  9.24  8.65
  BW048      1  disengaged  disengaged               475   90.42  90.35      50.48     6.77  5.90  5.89
  BW048      2 sub-optimal avoid right              1500   75.00  74.12      50.22     2.69  9.22  8.90
  BW048      3 sub-optimal   bias left              1171   81.17  79.33      50.91     3.16  9.57  8.99
  BW048      4 sub-optimal  avoid left               648   78.63  77.57      49.28     2.96  9.93  9.57
  BW051      1  disengaged  disengaged               550   90.27  89.82      47.60     5.48  7.78  7.70
  BW051      2 sub-optimal avoid right              1500   75.30  74.36      50.25     3.81  6.57  6.32
  BW053      1  disengaged  disengaged              1500   89.67  89.28      50.01     3.80 10.42 10.32
  BW053      2 sub-optimal   bias left               925   82.22  81.39      49.46     3.34  9.80  9.55
  BW053      3 sub-optimal  bias right               972   68.72  67.87      48.98     2.65  7.44  7.11
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python - <<'EOF'
s=open('nb.py').read()
s=s.replace('''    print(f"{c}: r2 {r2tab[c].mean():.2f} +/- {r2tab[c].sem():.2f}; vs pupil difference {np.mean(r2tab[c] - r2tab.pupil):+.2f}, "''','''    print(f"{c}: r2 {r2tab[c].mean():.3f} +/- {r2tab[c].sem():.3f}; vs pupil difference {np.mean(r2tab[c] - r2tab.pupil):+.3f}, "''')
s=s.replace('''print("\\nmean +/- SEM over mice:", {c: f"{r2tab[c].mean():.2f} +/- {r2tab[c].sem():.2f}" for c in r2tab.columns})''','''print("\\nmean +/- SEM over mice:", {c: f"{r2tab[c].mean():.3f} +/- {r2tab[c].sem():.3f}" for c in r2tab.columns})''')
open('nb.py','w').write(s)
EOF
grep -n "r2tab\[c\].mean():.3f" nb.py | head; . $TMPDIR/env/bin/activate; python run.py 33 50 2>&1 | grep -A3 "mean +/- SEM over mice\|movement (a): r2"
```

```
629:print("\nmean +/- SEM over mice:", {c: f"{r2tab[c].mean():.3f} +/- {r2tab[c].sem():.3f}" for c in r2tab.columns})
660:    print(f"{c}: r2 {r2tab[c].mean():.3f} +/- {r2tab[c].sem():.3f}; vs pupil difference {np.mean(r2tab[c] - r2tab.pupil):+.3f}, "
mean +/- SEM over mice: {'pupil': '0.647 +/- 0.060', 'face_energy (a)': '0.486 +/- 0.083', 'face_energy (b)': '0.432 +/- 0.084', 'running_speed (a)': '0.564 +/- 0.082', 'running_speed (b)': '0.392 +/- 0.080', 'movement (a)': '0.567 +/- 0.062', 'movement (b)': '0.554 +/- 0.058'}
face_energy (a) vs pupil: difference -0.16, lower in 9 of 13, p = 0.244
face_energy (b) vs pupil: difference -0.22, lower in 9 of 13, p = 0.146
running_speed (a) vs pupil: difference -0.08, lower in 8 of 13, p = 0.542
--
movement (a): r2 0.567 +/- 0.062; vs pupil difference -0.081, p = 0.34
movement (b): r2 0.554 +/- 0.058; vs pupil difference -0.093, p = 0.34
x from -5 to 4.75; y in [0, 1]; bins with fewer than 7 mice are included in the plot but not in the fit.
----- 0.2s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; cat > results.py <<'EOF'
R = {
"COHORT": "Partially reproduced. The dandiset holds 13 mice, 8 on the auditory and 5 on the visual task, all of which have at least 10 passing sessions, as the paper reports. Of its 391 sessions, 376 pass the criteria counted from the reward series (375 from the hits), not 381; the paper's 500 stage 5 and 6 sessions and its 18 excluded mice are not in the dandiset, so which 381 sessions were analysed cannot be told. The 376 sessions are used below.",
"DISTRACTOR": "Reproduced under reading (c): 5.2% of the 47,037 stage 6 distractor trials had a lick (5.2% on the included sessions). Per mouse, 7 of the 8 mice with stage 6 sessions are below 10% under readings (a) and (b); BW053 is at 16.2% pooled (15.3% over sessions). The fraction correct of responded target trials changes between stages by at most 5 points (BW053, 0.760 to 0.709), shown but not tested.",
"NSTATES": "Reproduced. Under both readings the number of states per mouse is 3 to 5 (five mice with 3, seven with 4, one with 5); the MLE and MAP plateaus give the same count under reading (a) as the MLE alone. This rests on 3 initialisations per fold, where the paper runs 10.",
"STATETYPES": "Reproduced. All 13 mice have an optimal state, a disengaged state and at least one other state, and every other state matches a sub-optimal template (22 sub-optimal states). The mice per sub-optimal type are bias left 6, avoid right 6, bias right 6 and avoid left 4, against 6, 4, 5 and 5 in Figure 2A; these counts do not decide the claim. In BW059 one state has no trial with a posterior of at least 0.8 in the sessions where the optimal state occurs; it is typed on all sessions (avoid right), an assumption.",
"OCCUPANCY": "Partially reproduced. The optimal state holds the largest share of trials (48.6% +/- 3.6%), more than the disengaged (12.9%), sub-optimal (23.7%) and indeterminate (14.8%) states by Wilcoxon signed-rank tests (p = 0.00024, 0.0024 and 0.0012). The indeterminate share, 14.8% +/- 2.2%, is just outside the expected 13.1% +/- 1.6% (11.5 to 14.7).",
"DWELL": "Partially reproduced. Optimal epochs last longer than disengaged and sub-optimal epochs in 12 or 13 of 13 mice under every reading (p from 0.00024 to 0.00073). The mean of the per-mouse median optimal dwell is 39.5 trials (code dwell; 38.5 as run length), within 37 +/- 3.7; the sub-optimal 13.8 (12.8) is within 15 +/- 1.5 for the code dwell, but the disengaged 11.9 (11.4) is not, and readings (b) and (c) put the optimal dwell at 45 to 71 trials. The median indeterminate dwell is 3.00 +/- 0.32 trials, outside 3.4 +/- 0.3.",
"PREDICT": "Reproduced. The selected GLM-HMM predicts 76.0% +/- 1.7% of choices against 65.0% for one state, a gain of 10.9 +/- 1.2 points (17.6% relative), better in 13 of 13 mice (signed-rank p = 0.00024; rank-sum p = 0.00025).",
"EXAMPLE": "Reproduced. BW046 has 4 states under both readings, and its choices are predicted at 78.3% by the 4-state model against 70.2% by the one-state model.",
"INVU": "Reproduced. In 12 of 13 mice the fit of P(optimal) on pupil diameter has its maximum inside the data range with lower values at both ends (BW061's fit is highest at its smallest pupil bin), and in 13 of 13 a second-order fit has a negative quadratic term, so reading (b), at least 11 of 13, holds under (i) and (ii), and reading (a) does too.",
"MODALITY": "Reproduced. The optimal pupil is smaller in auditory-task mice (median 0.627 of the session maximum) than in visual-task mice (0.698); Wilcoxon rank-sum p = 0.034.",
"SHIFT": "Reproduced. Aligned to each mouse's optimal pupil and averaged, P(optimal) has a negative and P(disengaged) a positive quadratic term with the vertex inside the range (22 bins with at least 7 mice), and both shapes hold on stationary trials below 0.02 m/s (reading (b), 32,648 trials). Reading (a), speed exactly 0, leaves 1,881 trials and no bin with 7 mice, so the shapes cannot be tested under it.",
"R2MOVE": "Partially reproduced. Face motion energy (0.486 +/- 0.083 with the plotting bins) and locomotion speed (0.392 +/- 0.080 with 50 bins; 0.564 with the plotting bins) are below pupil diameter on average, but pupil gives 0.647 +/- 0.060, outside 0.72 +/- 0.03, and only locomotion with 50 bins is lower than pupil at p < 0.05 (p = 0.048; face p = 0.24 and 0.15).",
"MOVEINVU": "Partially reproduced. The mean P(optimal) over movement-index bins is an inverted U (negative quadratic term, vertex at 0.23, inside -4.25 to 3.75), and its r2 does not differ from pupil's (p = 0.34 under both bin readings, as in the paper). The r2, 0.567 +/- 0.062 (plotting bins) or 0.554 (50 bins), is just below the expected 0.63 +/- 0.06.",
"MOVEU": "Reproduced. The mean P(disengaged) over movement-index bins has a positive quadratic term with its vertex (0.0) inside the range of bins with at least 7 mice.",
"S5CORR": "Reproduced. In every mouse the movement index correlates equally with face motion energy and with locomotion speed (difference below 0.0001), with r from 0.674 to 0.855, so reading (b), both above 0.5, holds; reading (a), above 0.7, fails in one mouse (BW071, 0.674).",
"DIST": "Partially reproduced. The distance from the optimal pupil is smallest in the optimal state and lower than in the disengaged (13 of 13 mice, p = 0.00024) and sub-optimal states (12 of 13, p = 0.021 and 0.017) under both session readings, but the values are larger than the paper's: 10.7%, 18.0% and 13.0% of the session maximum against 7%, 12.6% and 9%.",
"FACE": "Reproduced. Under reading (a), face motion energy is 0.487 +/- 0.025 a.u. in the optimal state, 0.443 in the disengaged and 0.442 in the sub-optimal states, all within tolerance; the optimal mean is the largest, above sub-optimal with p = 0.00049, and above disengaged with p = 0.068 (paper 0.06). Under reading (b) the values are 0.489, 0.439 and 0.453.",
"LOCO": "Reproduced. Locomotion speed is 0.136, 0.135 and 0.134 m/s in the optimal, disengaged and sub-optimal states (reading (a)), and neither test finds a difference (p = 0.74 and 0.68; reading (b) p = 0.54 and 1).",
"VAR": "Partially reproduced. All six differences have the stated sign, and five of the six tests give p < 0.05; face motion energy variability in the optimal state against the sub-optimal states does not (p = 0.08).",
"TRANS": "Partially reproduced. All three measures' variability falls on entering the optimal state and rises on leaving it on average, but of the four comparisons the figure marks, only pupil and locomotion exits give p < 0.05 (0.0012 and 0.0024); face entry (p = 0.15) and locomotion entry (p = 0.24) do not.",
"DECOUPLE": "Reproduced. The pupil-movement correlation is 0.104 in the optimal state against 0.438 in the disengaged and 0.257 in the sub-optimal states, lower in 13 and 10 of 13 mice (p = 0.00024 and 0.0081).",
"S6": "Reproduced. The correlation of pupil with face motion energy is lower in the optimal state than in the disengaged (p = 0.0046) and sub-optimal states (p = 0.033); with locomotion speed it is lower than in the disengaged state (p = 0.0046) and not significantly lower than in the sub-optimal states (p = 0.08).",
"S1": "Reproduced. The median correlations of pupil, locomotion and face motion energy with the preceding ITI are -0.044, -0.007 and -0.044, none different from zero (p = 0.13, 0.89, 0.27), within reading (a). The median evoked pupil responses do not differ across the four groups (Kruskal-Wallis p = 0.23; three discrete states p = 0.15).",
"S8A": "Reproduced. For the optimal state, the quadratic and SD weights of pupil and locomotion are negative (Wilcoxon against zero p from 0.0002 to 0.027) and positive for the disengaged state (p from 0.0002 to 0.013), while the face weights do not differ from zero (p from 0.13 to 0.50), under reading (a) and so under (b).",
"S8B": "Reproduced. The pupil-by-movement weight is 0.34 +/- 0.11 over the 22 sub-optimal fits (expected 0.42 +/- 0.11) and -0.82 +/- 0.23 over the optimal fits (expected -0.95 +/- 0.21), different by a rank-sum test (p = 5.6e-05), and the mean quadratic movement weight of the optimal fits is negative (-1.52). It is the only sub-optimal weight that differs from zero (p = 0.005).",
"DECODE": "Reproduced. With the eight features unshuffled, accuracy is 88.5% +/- 1.7% for optimal against disengaged (13 classifications) and 77.2% +/- 1.6% against sub-optimal states (21), within tolerance; the 'All measures' condition gives 88.2% and 76.4%. All 34 classifications are significant under every reading. Here 21 sub-optimal classifications are possible against 19 in the paper.",
"S7": "Reproduced under reading (a). Keeping one measure, pupil gives 71.1% against 65.7% for face motion energy (pupil higher in 23 of 34, p = 0.00046) and 67.7% for locomotion speed (p = 0.034); reading (b) agrees for face (p = 0.00018).",
"MOVEBEST": "Not reproduced under the claim's main reading: keeping only the movement index and its SD gives 67.7% against 71.1% for the pupil alone, lower in 21 of 34 classifications (p = 0.017). Under the code's conditions shown as variants, the movement index is better (condition 5: 74.5%, p = 7.4e-05; condition 1: 76.7%, p = 2.3e-10).",
}
EOF
python - <<'EOF'
import re
exec(open('results.py').read())
s=open('nb.py').read()
for k,v in R.items():
    tag=f"**Result: {k}**"
    assert tag in s, k
    s=s.replace(tag, "**Result: "+v[0].lower()+v[1:]+"**" if False else f"**Result: {v.split('. ')[0]}.** " + '. '.join(v.split('. ')[1:]))
open('nb.py','w').write(s)
print(re.findall(r'\*\*Result: [A-Z]+\*\*', s))
EOF
grep -c "Result:" nb.py
```

```
[]
28
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; cat > header.md <<'EOF'
# Reproducing Hulsey et al. (2024) from dandiset 000678

**Paper.** Hulsey D, Zumwalt K, Mazzucato L, McCormick DA, Jaramillo S (2024). Decision-making dynamics are predicted by arousal and uninstructed movements. *Cell Reports* 43(1), 113709. [doi:10.1016/j.celrep.2024.113709](https://doi.org/10.1016/j.celrep.2024.113709). The claims file was written from the accepted author manuscript in PubMed Central (PMC11016285) with its supplement; this attempt read the same text and the paper's analysis code (Zenodo [10.5281/zenodo.10306018](https://doi.org/10.5281/zenodo.10306018), and github.com/sjara/uobrainflex at commit ef48985192e4af332c64f9d2e70ddcfc78659040).

**Dandiset.** [DANDI:000678](https://dandiarchive.org/dandiset/000678/0.231004.2146), version 0.231004.2146, streamed from the archive. This is the version the paper cites (Data and code availability, and the Key resources table). A later version, 0.261020.0029, has the same 391 assets with the same asset identifiers and sizes; it differs only in the archive metadata (keywords, affiliations, ORCIDs), so the choice does not change the data.

**Claims.** `claims/000678/10.1016-j.celrep.2024.113709.yaml` (29 claims). The GLM-HMM and the analyses after it follow the paper's code, reimplemented in `hulsey.py`; where the claims file leaves a detail open, the passage used is cited in the section or in the helper's docstring.

| Claim | Tested here |
|---|---|
| cohort-inclusion | tested |
| training-duration | blocked: data missing (no sessions before stage 5) |
| distractor-response-rate | tested |
| figs2-n-states | tested (3 initialisations per fold in place of 10) |
| fig1g-example-mouse-prediction | tested |
| fig2a-state-types | tested |
| fig2b-optimal-occupancy | tested |
| fig2c-dwell-times | tested |
| fig2d-prediction-accuracy | tested |
| fig3c-inverted-u-pupil | tested |
| fig3d-optimal-pupil-modality | tested |
| fig3e-u-disengaged-pupil | tested |
| figs4-r2-individual-movement | tested |
| fig3f-movement-index-inverted-u | tested |
| fig3f-movement-index-u-disengaged | tested |
| figs5-movement-index-correlations | tested |
| fig3-distance-from-optimal-pupil | tested |
| fig3-raw-face-energy-trend | tested |
| fig3-raw-locomotion-no-difference | tested |
| fig4a-lower-variability | tested |
| fig4b-variability-at-transitions | tested |
| fig4d-pupil-movement-decoupling | tested |
| figs6-individual-measure-decoupling | tested |
| fig5c-state-classification | tested (fewer shuffle runs) |
| figs7-pupil-best-raw-measure | tested (fewer shuffle runs) |
| fig5c-movement-index-best | tested (fewer shuffle runs) |
| figs8a-regression-weights | tested |
| figs8b-pupil-movement-interaction | tested |
| figs1-iti-independence | tested |

The notebook takes about 15 minutes on 4 cores: about 4 to stream the 391 files, 4 for the cross-validated GLM-HMM fits and 6 for the state decoders. Random seeds are fixed, and each claim's section has its own generator.
EOF
cat > summary.md <<'EOF'
## Summary

| Claim | Outcome |
|---|---|
| cohort-inclusion | partially reproduced (13 mice, 8 and 5 by task; 376 sessions pass, not 381) |
| training-duration | blocked: data missing |
| distractor-response-rate | reproduced (5.2% overall; one mouse at 16%) |
| figs2-n-states | reproduced (3 to 5 states) |
| fig1g-example-mouse-prediction | reproduced (4 states; 70.2% and 78.3%) |
| fig2a-state-types | reproduced, resting on an assumption for one state of BW059 |
| fig2b-optimal-occupancy | partially reproduced (indeterminate 14.8%, expected 13.1 +/- 1.6) |
| fig2c-dwell-times | partially reproduced (indeterminate dwell 3.0, disengaged 11.9) |
| fig2d-prediction-accuracy | reproduced (76.0%, gain 10.9 points) |
| fig3c-inverted-u-pupil | reproduced |
| fig3d-optimal-pupil-modality | reproduced (p = 0.034) |
| fig3e-u-disengaged-pupil | reproduced |
| figs4-r2-individual-movement | partially reproduced (pupil r2 0.65; tests not significant) |
| fig3f-movement-index-inverted-u | partially reproduced (r2 0.567, expected 0.63 +/- 0.06) |
| fig3f-movement-index-u-disengaged | reproduced |
| figs5-movement-index-correlations | reproduced |
| fig3-distance-from-optimal-pupil | partially reproduced (order and tests hold; values larger) |
| fig3-raw-face-energy-trend | reproduced |
| fig3-raw-locomotion-no-difference | reproduced |
| fig4a-lower-variability | partially reproduced (5 of 6 tests) |
| fig4b-variability-at-transitions | partially reproduced (signs hold; 2 of 4 marked tests) |
| fig4d-pupil-movement-decoupling | reproduced |
| figs6-individual-measure-decoupling | reproduced |
| fig5c-state-classification | reproduced (88.5% and 77.2%) |
| figs7-pupil-best-raw-measure | reproduced |
| fig5c-movement-index-best | not reproduced under the main reading; reproduced under the code's conditions |
| figs8a-regression-weights | reproduced |
| figs8b-pupil-movement-interaction | reproduced |
| figs1-iti-independence | reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** The GLM-HMM of the paper's ssm fork is reimplemented (`hulsey.py`), fit by the same EM with the same priors, initialisation and stopping rule; its random initial values differ from ssm's. The cross-validation that selects the number of states uses 3 random initialisations per fold and number of states, not 10, and the decoders use 3 shuffle runs per shuffled condition and 20 null runs, not 1000, to keep the notebook within its time limit. The sessions are the 376 that pass the paper's inclusion criteria, where the paper reports 381. Where the paper's state-typing code would score a state with no discrete trials as equal to every template, that state is typed on all sessions (one state of BW059).

**What was found about the dataset.** The dandiset holds the 13 included mice and 391 sessions of stages 5 and 6, more than the 381 the paper analysed, with no way to tell which were left out; the excluded mice, the other stage 5 and 6 sessions and the training sessions before stage 5 are not in it. `running_speed` is labelled cm/s but holds m/s. 40 sessions have a post hoc pupil series that is entirely missing. The rig names are spelled several ways ('Box 1', 'Box1', 'Boox1'). No recording is deposited twice, and the measures share the clock of the trial table (data check).
EOF
python - <<'EOF'
s=open('nb.py').read()
s=s.replace('#%% md\nHEADER\n','#%% md\n'+open('header.md').read())
s=s.rstrip('\n')+'\n#%% md\n'+open('summary.md').read()
open('nb.py','w').write(s)
EOF
grep -c "^#%%" nb.py
```

```
94
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; sed -i 's/40 sessions have a post hoc pupil series that is entirely missing/38 of the 391 sessions have a post hoc pupil series that is entirely missing/' nb.py; cat > build.py <<'EOF'
import re, os, nbformat
src = open(os.environ['TMPDIR'] + '/dev/nb.py').read()
cells = re.split(r'^#%% ', src, flags=re.M)[1:]
nb = nbformat.v4.new_notebook()
for c in cells:
    head, _, body = c.partition('\n')
    body = body.rstrip('\n')
    if head.startswith('md'):
        nb.cells.append(nbformat.v4.new_markdown_cell(body))
    else:
        cell = nbformat.v4.new_code_cell(body)
        m = re.search(r'tags=(\S+)', head)
        if m:
            cell.metadata['tags'] = m.group(1).split(',')
        nb.cells.append(cell)
nb.metadata['kernelspec'] = {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}
nbformat.write(nb, 'entries/000678-hulsey-2024/reproduce_hulsey_2024.ipynb')
print(len(nb.cells))
EOF
. $TMPDIR/env/bin/activate; uv pip install -q nbformat 2>/dev/null; python build.py
cd entries/000678-hulsey-2024
cat > requirements.in <<'EOF'
h5py
matplotlib
numba
numpy
pandas
remfile
scikit-learn
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000678-hulsey-2024
type: reproduction
title: Arousal, uninstructed movements and decision-making states in mice (Hulsey et al. 2024)
description: Tests the findings of Hulsey, Zumwalt, Mazzucato, McCormick and Jaramillo (2024) on
  dandiset 000678, which holds the stage 5 and 6 behavioral sessions of 13 mice performing auditory
  or visual discrimination, with pupil diameter, face motion energy and locomotion speed. It fits the
  paper's GLM-HMM to each mouse's choices, labels the performance states, and relates the states to
  the arousal and movement measures, including the support vector machine decoding of the states.
license: Apache-2.0
notebooks:
- path: reproduce_hulsey_2024.ipynb
  title: Reproducing Hulsey et al. (2024) from dandiset 000678
  runtime_minutes: 15
helpers:
- hulsey.py
related:
- id: dandi:000678/0.231004.2146
  relation: uses_data
- id: doi:10.1016/j.celrep.2024.113709
  relation: reproduces
EOF
cat ../001453-fouke-2025/requirements.lock.txt | head -5; cd  python tools/entry.py lock entries/000678-hulsey-2024 2>&1 | tail -3; date -u
```

```
94
# This file was autogenerated by uv via the following command:
#    uv pip compile --python-version 3.13 requirements.in -o requirements.lock.txt
acres==0.5.0
    # via bidsschematools
aiohappyeyeballs==2.7.1
wrote entries/000678-hulsey-2024/requirements.lock.txt
Sat Oct 31 10:15:03 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; grep -n "^def \|^class \|^    def \|^GLMHMM\|^@njit" hulsey.py
```

```
64:def _get_json(url):
69:def list_assets(version=VERSION):
82:def version_metadata(version=VERSION):
86:def s3_url(asset_id):
92:def _maps(trials_group):
104:def _savgol_code(y, window, order=2):
120:def _to_grid(ts, data, n):
140:def load_session(asset_id, path):
254:def load_all(assets, workers=16):
271:@njit(cache=True)
272:def _forward_backward(log_pi0, P, loglik):
325:@njit(cache=True)
326:def _filter(log_pi0, P, loglik):
342:def _logits(W, X):
349:def _unique_inputs(Xs, ys):
355:def _log_prior_obs(W, sigma):
361:def _log_prior_trans(P, sticky, alpha=2.0):
365:def _mstep_W(W, U, counts, sigma, n_newton=50):
396:class GLMHMM:
399:    def __init__(self, K, M=2, C=3, prior_sigma=1000.0, sticky=False, rng=None):
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000678-hulsey-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
s=open('hulsey.py').read()
lines=s.split('\n')
def block(start_pat, end_pat):
    a=s.index(start_pat); b=s.index(end_pat, a); return a,b
# extract numba EM block (from '@njit(cache=True)\ndef _table' to 'def _fit_fast')
a=s.index('@njit(cache=True)\ndef _table'); b=s.index('def _fit_fast')
em_block=s[a:b]
# remove fit_fast & assignments
c=s.index('GLMHMM.fit = _fit_fast\n')+len('GLMHMM.fit = _fit_fast\n')
fast=s[b:c]
s=s[:a]+s[c:]
# remove _mstep_W
a=s.index('def _mstep_W('); b=s.index('class GLMHMM:')
s=s[:a]+em_block+'\n'+s[b:]
# replace class fit method
a=s.index('    def fit(self, Xs, ys, num_iters=1000, tolerance=1e-4):'); b=s.index('    def posteriors(self')
newfit='''    def fit(self, Xs, ys, num_iters=1000, tolerance=1e-4):
        """EM (ssm's HMM.fit with method="em"); returns the log joint at each iteration."""
        U, ux, y = _unique_inputs(Xs, ys)
        starts = np.r_[0, np.cumsum([len(x) for x in Xs])].astype(np.int64)
        W, P, lp0, lps = _em(self.W.copy(), self.P.copy(), self.log_pi0.copy(), U.astype(float),
                             ux.astype(np.int64), y.astype(np.int64), starts, float(self.prior_sigma),
                             bool(self.sticky), num_iters, tolerance)
        self.W, self.P, self.log_pi0 = W, P, lp0
        self.n_iter = len(lps)
        self.lps = list(lps)
        return self.lps

'''
s=s[:a]+newfit+s[b:]
s=s.replace("from concurrent.futures import ProcessPoolExecutor\n","from concurrent.futures import ProcessPoolExecutor\n")
open('hulsey.py','w').write(s)
EOF
grep -n "^def \|^class \|^    def \|^GLMHMM\|_fit_fast\|fit_slow\|ThreadPool" hulsey.py | head -60; python -c "
import sys; sys.path.insert(0,'.')
import hulsey, numpy as np, pandas as pd, os
tr=pd.read_pickle(os.environ['TMPDIR']+'/tr.pkl')
m=tr[tr.subject=='BW046']
Xs,ys=hulsey.sequences(m)
r=hulsey.fit_one((4,Xs,ys,None,None,False,3)); print(r[1], r[0].n_iter)
"
```

```
64:def _get_json(url):
69:def list_assets(version=VERSION):
82:def version_metadata(version=VERSION):
86:def s3_url(asset_id):
92:def _maps(trials_group):
104:def _savgol_code(y, window, order=2):
120:def _to_grid(ts, data, n):
140:def load_session(asset_id, path):
254:def load_all(assets, workers=16):
272:def _forward_backward(log_pi0, P, loglik):
326:def _filter(log_pi0, P, loglik):
342:def _logits(W, X):
349:def _unique_inputs(Xs, ys):
355:def _log_prior_obs(W, sigma):
361:def _log_prior_trans(P, sticky, alpha=2.0):
366:def _table(W, U):
391:def _obj_k(Wk, U, cnt, sigma):
404:def _em(W, P, log_pi0, U, ux, y, starts, sigma, sticky, num_iters, tol):
555:class GLMHMM:
558:    def __init__(self, K, M=2, C=3, prior_sigma=1000.0, sticky=False, rng=None):
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python - <<'EOF'
s=open('nb.py').read()
s=s.replace('''#%% code devload
import time
import warnings
''','''#%% code devload
import os
for _v in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[_v] = "1"  # many small fits run in parallel processes; one linear-algebra thread each
import time
import warnings
''')
open('nb.py','w').write(s)
EOF
sed -i "s/M-step of the weights by Newton's method on the expected log joint/M-step of the weights by damped Newton steps on the expected log joint (computed from the expected counts of each choice at each distinct input)/" entries/000678-hulsey-2024/hulsey.py
. $TMPDIR/env/bin/activate; python build.py; cd  python tools/entry.py check entries/000678-hulsey-2024 2>&1 | tail -20
```

```
94
0 error(s)
```

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/000678-hulsey-2024 2>&1 | tail -30; date -u
```

```
Sat Oct 31 10:15:43 UTC 2026
Installed kernelspec registry-000678-hulsey-2024 in executed/000678-hulsey-2024/.venv/share/jupyter/kernels/registry-000678-hulsey-2024
0 error(s)
pass  reproduce_hulsey_2024.ipynb  (842 s)

real	14m8.964s
user	49m52.076s
sys	3m58.509s
Sat Oct 31 10:29:52 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls executed/000678-hulsey-2024/; python3 - <<'EOF' > $TMPDIR/exec_out.txt
import json
nb=json.load(open('executed/000678-hulsey-2024/reproduce_hulsey_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print(f"=== cell {i} {c['metadata'].get('tags')}")
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text']))
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
EOF
wc -l $TMPDIR/exec_out.txt; grep -n "ERROR\|streamed\|fits in\|reading (\|mean +/- SEM\|best model\|BW046:\|(i) maximum\|median auditory\|holds\|r2 0.5\|largest |diff\|tests with\|entry \|optimal vs\|Kruskal\|classifications\|keep one, acc\|main: M only\|P\*M sub\|significant" $TMPDIR/exec_out.txt | head -120
```

```
reproduce_hulsey_2024.ipynb
result.json
644 /tmp/claude-1001/exec_out.txt
4:streamed 391 files in 3.1 min
162:2730 cross-validation fits in 4.2 min; 16 stopped at 1000 iterations
178:reading (a) max: range 3 to 5; counts {3: 5, 4: 7, 5: 1}
179:reading (b) MLE: range 3 to 5; counts {3: 5, 4: 7, 5: 1}
214:final fits in 0.1 min
275:mean +/- SEM over mice (%): {'optimal': '48.6 +/- 3.6', 'disengaged': '12.9 +/- 2.0', 'sub-optimal': '23.7 +/- 2.4', 'indeterminate': '14.8 +/- 2.2'}
276:optimal vs disengaged: optimal larger in 13 of 13 mice, Wilcoxon signed-rank p = 0.00024
277:optimal vs sub-optimal: optimal larger in 12 of 13 mice, Wilcoxon signed-rank p = 0.0024
278:optimal vs indeterminate: optimal larger in 12 of 13 mice, Wilcoxon signed-rank p = 0.0012
285:  optimal vs disengaged (medians): optimal longer in 12 of 13, p = 0.00049
286:  optimal vs disengaged (means): optimal longer in 13 of 13, p = 0.00024
287:  optimal vs sub-optimal (medians): optimal longer in 12 of 13, p = 0.00073
288:  optimal vs sub-optimal (means): optimal longer in 12 of 13, p = 0.00073
293:  optimal vs disengaged (medians): optimal longer in 12 of 13, p = 0.00073
294:  optimal vs disengaged (means): optimal longer in 13 of 13, p = 0.00024
295:  optimal vs sub-optimal (medians): optimal longer in 12 of 13, p = 0.00073
296:  optimal vs sub-optimal (means): optimal longer in 12 of 13, p = 0.00073
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 520,590p $TMPDIR/exec_out.txt; sed -n 630,644p $TMPDIR/exec_out.txt
```

```
optimal vs sub-optimal: difference -0.131, optimal lower in 12 of 13, p = 0.00073

=== cell 76 ['claim:figs1-iti-independence']
r with the preceding ITI:
         post_hoc_pupil_diameter  running_speed  face_energy
subject                                                     
BW041                     -0.150          0.058       -0.070
BW045                     -0.031         -0.011       -0.123
BW046                      0.079          0.058       -0.081
BW048                      0.081          0.134       -0.026
BW051                     -0.044         -0.007        0.138
BW053                     -0.276         -0.085       -0.070
BW058                     -0.063         -0.056        0.123
BW059                      0.036         -0.009        0.020
BW061                      0.012          0.006        0.006
BW062                     -0.002         -0.036       -0.065
BW064                     -0.229          0.142       -0.119
BW067                     -0.089         -0.153       -0.003
BW071                     -0.058          0.074       -0.044
post_hoc_pupil_diameter: median r -0.044, Wilcoxon against 0 p = 0.13; (a) |median| < 0.1: True, (b) < 0.2: True
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['required'])); print(list(s['properties'].keys()))
o=s['properties']['outcomes']['items']; print(o.get('required'), list(o['properties'].keys()))
print(json.dumps(s['properties']['findings'],indent=0)[:1500])
print(json.dumps(s['properties']['provenance'],indent=0)[:1500])
print(json.dumps(s['properties'].get('inputs'),indent=0)[:800])
"
```

```
["schema_version", "id", "dataset", "paper", "date", "provenance", "outcomes"]
['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
{
"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.",
"type": "array",
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"kind",
"statement"
],
"properties": {
"kind": {
"enum": [
"metadata_error",
"data_missing",
"identifier_missing",
"metadata_insufficient",
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python - <<'EOF'
s=open('nb.py').read()
reps=[("are negative (Wilcoxon against zero p from 0.0002 to 0.027) and positive for the disengaged state (p from 0.0002 to 0.013), while the face weights do not differ from zero (p from 0.13 to 0.50)","are negative (Wilcoxon against zero p at most 0.027) and positive for the disengaged state (p at most 0.013), while the face weights do not differ from zero (p from 0.127 to 0.497)"),
("gives 67.7% against 71.1% for the pupil alone, lower in 21 of 34 classifications (p = 0.017)","gives 67.7% against 71.1% for the pupil alone, higher in only 13 of 34 classifications (p = 0.017)"),
("Reading (a), speed exactly 0, leaves 1,881 trials and no bin with 7 mice, so the shapes cannot be tested under it.","Reading (a), speed exactly 0, leaves 1,881 trials and at most one bin with 7 mice, so the shapes cannot be tested under it.")]
for a,b in reps:
    assert a in s, a[:40]
    s=s.replace(a,b)
open('nb.py','w').write(s)
EOF
grep -n "Result:" nb.py | cut -c1-200
```

```
166:**Result: Partially reproduced.** The dandiset holds 13 mice, 8 on the auditory and 5 on the visual task, all of which have at least 10 passing sessions, as the paper reports. Of its 391 sessions,
198:**Result: Reproduced under reading (c): 5.2% of the 47,037 stage 6 distractor trials had a lick (5.2% on the included sessions).** Per mouse, 7 of the 8 mice with stage 6 sessions are below 10% un
247:**Result: Reproduced.** Under both readings the number of states per mouse is 3 to 5 (five mice with 3, seven with 4, one with 5); the MLE and MAP plateaus give the same count under reading (a) as
338:**Result: Reproduced.** All 13 mice have an optimal state, a disengaged state and at least one other state, and every other state matches a sub-optimal template (22 sub-optimal states). The mice p
362:**Result: Partially reproduced.** The optimal state holds the largest share of trials (48.6% +/- 3.6%), more than the disengaged (12.9%), sub-optimal (23.7%) and indeterminate (14.8%) states by Wi
413:**Result: Partially reproduced.** Optimal epochs last longer than disengaged and sub-optimal epochs in 12 or 13 of 13 mice under every reading (p from 0.00024 to 0.00073). The mean of the per-mous
461:**Result: Reproduced.** The selected GLM-HMM predicts 76.0% +/- 1.7% of choices against 65.0% for one state, a gain of 10.9 +/- 1.2 points (17.6% relative), better in 13 of 13 mice (signed-rank p 
470:**Result: Reproduced.** BW046 has 4 states under both readings, and its choices are predicted at 78.3% by the 4-state model against 70.2% by the one-state model.
584:**Result: Reproduced.** In 12 of 13 mice the fit of P(optimal) on pupil diameter has its maximum inside the data range with lower values at both ends (BW061's fit is highest at its smallest pupil 
596:**Result: Reproduced.** The optimal pupil is smaller in auditory-task mice (median 0.627 of the session maximum) than in visual-task mice (0.698); Wilcoxon rank-sum p = 0.034.
649:**Result: Reproduced.** Aligned to each mo
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python - <<'EOF'
s=open('nb.py').read()
reps=[("**Result: Reproduced under reading (c): 5.2% of the 47,037 stage 6 distractor trials had a lick (5.2% on the included sessions).**","**Result: Reproduced.** Under reading (c), 5.2% of the 47,037 stage 6 distractor trials had a lick (5.2% on the included sessions)."),
("changes between stages by at most 5 points (BW053, 0.760 to 0.709)","changes between stages by at most 5.4 points (BW064, 0.816 to 0.762)"),
("**Result: Not reproduced under the claim's main reading: keeping only the movement index and its SD gives 67.7% against 71.1% for the pupil alone, higher in only 13 of 34 classifications (p = 0.017).**","**Result: Not reproduced.** Under the claim's main reading, keeping only the movement index and its SD gives 67.7% against 71.1% for the pupil alone, higher in only 13 of 34 classifications (p = 0.017).")]
for a,b in reps:
    assert a in s, a[:50]
    s=s.replace(a,b)
open('nb.py','w').write(s)
EOF
grep -n "Result: Not\|Result: Reproduced.\*\* Under" nb.py | cut -c1-150; date -u
```

```
198:**Result: Reproduced.** Under reading (c), 5.2% of the 47,037 stage 6 distractor trials had a lick (5.2% on the included sessions). Per mouse, 7 o
247:**Result: Reproduced.** Under both readings the number of states per mouse is 3 to 5 (five mice with 3, seven with 4, one with 5); the MLE and MAP
772:**Result: Reproduced.** Under reading (a), face motion energy is 0.487 +/- 0.025 a.u. in the optimal state, 0.443 in the disengaged and 0.442 in t
1063:**Result: Not reproduced.** Under the claim's main reading, keeping only the movement index and its SD gives 67.7% against 71.1% for the pupil al
Sat Oct 31 10:30:24 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  cat > attempts/000678-hulsey-2024-01.yaml <<'EOF'
schema_version: 2
id: 000678-hulsey-2024-01
dataset:
  archive: dandi
  id: "000678"
  version: 0.231004.2146
  doi: 10.48324/dandi.000678/0.231004.2146
paper: doi:10.1016/j.celrep.2024.113709
date: 2026-10-31
entry: 000678-hulsey-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-12
  runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/41188142719
outcomes:
- claim: cohort-inclusion
  outcome: partially_reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:cohort-inclusion
  measured:
  - 13
  - 8
  - 5
  - 376
  notes: The dandiset holds 13 mice, 8 on the auditory and 5 on the visual task, each with at least
    10 passing sessions. Of its 391 stage 5 and 6 sessions, 376 pass the STAR Methods criteria
    counted from the reward series and 375 counted from the hits, against 381 in the paper. The
    sessions failing either count are listed in the notebook (13 with fewer than 100 rewards, 2 with
    less than 20% at one port, and 2 that fail one count only). The paper's 500 stage 5 and 6
    sessions and its 18 excluded mice are not in the dandiset.
  deviations:
  - The sessions of every later analysis are the 376 that pass the criteria by the reward count; the
    paper analysed 381, and the dandiset does not say which.
- claim: training-duration
  outcome: blocked
  blocked_by: data_missing
  notes: Every session in the dandiset is stage 5 or 6 (metadata training_stage), so the training
    sessions before stage 5 cannot be counted. They are not public elsewhere as far as the paper and
    the dandiset say.
- claim: distractor-response-rate
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:distractor-response-rate
  measured: 0.052
  notes: Distractor trials have outcome 4 (false alarm, a lick) or 8 (correct reject). Under reading
    (c), 2,446 of 47,037 stage 6 distractor trials had a lick, 5.2%. Under readings (a) and (b), 7 of
    the 8 mice with stage 6 sessions are below 10%; BW053 is at 16.2% pooled and 15.3% over sessions.
    "No discriminable change in performance" is not tested; the fraction correct of responded target
    trials differs between stages by at most 5.4 points.
- claim: figs2-n-states
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:figs2-n-states
  measured:
  - 3
  - 5
  notes: Under both readings of O1 the counts are 3 states in five mice, 4 in seven and 5 in one
    (BW048); the MAP plateau is never larger than the MLE plateau. 16 of the 2,730 cross-validation
    fits stopped at 1,000 iterations.
  deviations:
  - The GLM-HMM of the paper's ssm fork is reimplemented (hulsey.py) with the same model, priors,
    initialisation scheme, EM updates and stopping rule; its random initial values differ from
    ssm's. The test log probability includes the log prior, as ssm's log_probability does.
  - 3 random initialisations per fold and number of states in place of the paper's 10, to fit the
    notebook's time limit; with fewer initialisations the best test log likelihood of larger models
    may be lower, which would favour fewer states.
  - Fit on the 376 sessions that pass the inclusion criteria (see cohort-inclusion).
- claim: fig1g-example-mouse-prediction
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig1g-example-mouse-prediction
  measured:
  - 70.2
  - 78.3
  - 4
  notes: BW046 gets 4 states under both readings of O1; one-state accuracy 70.2%, 4-state accuracy
    78.3%, computed as in fig2d-prediction-accuracy.
  deviations:
  - As for figs2-n-states and fig2d-prediction-accuracy.
- claim: fig2a-state-types
  outcome: reproduced
  assumed: true
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig2a-state-types
  notes: All 13 mice have an optimal, a disengaged and at least one other state, and each of the 22
    other states is matched to a sub-optimal template. Mice per type are bias left 6, avoid right 6,
    bias right 6 and avoid left 4 (Figure 2A gives 6, 4, 5 and 5; not deciding). For BW061 the state
    that flex_hmm.permute_hmm puts first (the one nearest a perfect psychometric) is nearer the bias
    right template than the optimal one when all six templates are compared; under M3 it is the
    optimal state. In BW059 one state has no trial with a posterior of at least 0.8 in the sessions
    where the optimal state occurs, so its psychometric is all missing; Figure2.py's nansum would
    score it 0 against every template and mislabel the mouse's optimal state. That state (432 trials
    over all sessions) is typed on all sessions, as avoid right. The question is asked of the paper's
    authors (findings).
  deviations:
  - Assumption. A state with no discrete-state trial in the sessions where the optimal state occurs
    is typed on all of the mouse's sessions; Figure2.py has no rule for it (it would score the state
    as equal to every template). Affects one state of BW059.
  - As for figs2-n-states.
- claim: fig2b-optimal-occupancy
  outcome: partially_reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig2b-optimal-occupancy
  measured: 14.8
  notes: On sessions in which the optimal state occurs, the optimal state holds 48.6% +/- 3.6% of
    trials, disengaged 12.9%, sub-optimal 23.7% and indeterminate 14.8% +/- 2.2%. The optimal share
    is larger than each other share by Wilcoxon signed-rank tests (p = 0.00024, 0.0024, 0.0012). The
    indeterminate share is just above the expected 13.1 +/- 1.6 (upper bound 14.7).
  deviations:
  - As for figs2-n-states.
- claim: fig2c-dwell-times
  outcome: partially_reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig2c-dwell-times
  measured:
  - 3.0
  - 39.5
  - 11.9
  notes: Optimal epochs are longer than disengaged and sub-optimal epochs in 12 or 13 of 13 mice under
    every reading (p from 0.00024 to 0.00073). The median indeterminate dwell is 3.00 +/- 0.32 trials,
    outside 3.4 +/- 0.3. Under reading (a) with the code's dwell (y), the optimal dwell is 39.5 trials
    (within 37 +/- 3.7), the sub-optimal 13.8 (within 15 +/- 1.5) and the disengaged 11.9 (outside);
    with the run length (x), 38.5, 12.8 and 11.4. Readings (b) and (c) give optimal dwells of 69.6 to
    70.6 and 45.2 to 46.1. The measured values are the indeterminate dwell, the optimal and the
    disengaged dwell under (a) and (y).
  deviations:
  - As for figs2-n-states.
- claim: fig2d-prediction-accuracy
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig2d-prediction-accuracy
  measured:
  - 76.0
  - 10.9
  notes: Best model 76.0% +/- 1.7%, one state 65.0% +/- 2.2%, gain 10.9 +/- 1.2 points under reading
    (a) (17.6% +/- 2.4% relative under (b), outside). Better in 13 of 13 mice, Wilcoxon signed-rank
    p = 0.00024 (rank-sum p = 0.00025).
  deviations:
  - The paper's code computes the filtered posterior of the preceding test trials by re-running
    expected_states on each prefix; here one forward pass gives the same filtered probabilities.
  - As for figs2-n-states.
- claim: fig3c-inverted-u-pupil
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig3c-inverted-u-pupil
  measured: 12
  notes: Reading (i) holds in 12 of 13 mice (BW061's fit is highest at its lowest pupil bin) and
    reading (ii) in 13 of 13, so "nearly all" holds under (a) and (b). Polynomial degrees 2 to 6 were
    selected by the elbow rule.
  deviations:
  - As Figure3.py, a state absent from a bin with more than 5 trials leaves that bin missing, so a
    bin with no optimal trial is not a zero; this follows the code.
- claim: fig3d-optimal-pupil-modality
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig3d-optimal-pupil-modality
  measured: 0.034
  notes: Median optimal pupil 0.627 of the session maximum for the 8 auditory mice and 0.698 for the 5
    visual mice; Wilcoxon rank-sum p = 0.034 (paper 0.008).
- claim: fig3e-u-disengaged-pupil
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig3e-u-disengaged-pupil
  notes: On all trials, over 22 bins with at least 7 mice, the second-order fit to mean P(optimal) has
    a negative quadratic term (vertex 0.1% from the optimal pupil) and to P(disengaged) a positive one
    (vertex 0.5%). On stationary trials under reading (b), below 0.02 m/s (32,648 trials, 20 bins),
    both hold (vertices -0.7 and -3.4). Reading (a), speed exactly 0, leaves 1,881 trials and at most
    one bin with 7 mice, so it cannot be tested.
- claim: figs4-r2-individual-movement
  outcome: partially_reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:figs4-r2-individual-movement
  measured:
  - 0.647
  - 0.486
  - 0.564
  notes: Pupil r2 0.647 +/- 0.060 (outside 0.72 +/- 0.03). Face 0.486 +/- 0.083 with plotting bins
    (a) and 0.432 with 50 bins (b), within tolerance under (a). Locomotion 0.564 (a), outside, and
    0.392 (b), within. Both are lower than pupil on average under both readings (by 0.08 to 0.25),
    but by Wilcoxon only locomotion under (b) is lower at p < 0.05 (p = 0.048); face p = 0.24 and
    0.15. One mouse, BW051, has a pupil r2 of 0.086. The measured values are pupil, face (a) and
    locomotion (a).
- claim: fig3f-movement-index-inverted-u
  outcome: partially_reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig3f-movement-index-inverted-u
  measured: 0.567
  notes: The mean P(optimal) over the 0.25 movement-index bins with at least 7 mice has a negative
    quadratic term with its vertex at 0.23, inside -4.25 to 3.75. Its r2 does not differ from pupil's
    (difference -0.08, p = 0.34 under both bin readings, the paper's p). The r2 is 0.567 +/- 0.062
    under (a) and 0.554 under (b), just below the expected range 0.57 to 0.69.
- claim: fig3f-movement-index-u-disengaged
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig3f-movement-index-u-disengaged
  notes: The mean P(disengaged) over 33 movement-index bins with at least 7 mice has a positive
    quadratic term (0.026) with its vertex at 0.0, inside -4.25 to 3.75.
- claim: figs5-movement-index-correlations
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:figs5-movement-index-correlations
  notes: The two correlations agree to better than 0.0001 in every mouse (as they must by
    construction), with r from 0.674 to 0.855; reading (b), above 0.5, holds, and reading (a), above
    0.7, fails in BW071 (0.674).
- claim: fig3-distance-from-optimal-pupil
  outcome: partially_reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig3-distance-from-optimal-pupil
  measured:
  - 10.7
  - 18.0
  - 13.0
  notes: Under reading (a) of O3 the absolute distance is 10.7% +/- 2.3% in the optimal state, 18.0%
    in the disengaged and 13.0% in the sub-optimal states, lower in the optimal state than in the
    disengaged (13 of 13, p = 0.00024) and sub-optimal states (12 of 13, p = 0.021); reading (b) gives
    10.7, 17.9 and 13.1 (p = 0.00024 and 0.017). The order and the tests hold; all three values are
    larger than the paper's 7, 12.6 and 9.
  deviations:
  - Rests on the optimal pupils of fig3c-inverted-u-pupil, from this attempt's state fits.
- claim: fig3-raw-face-energy-trend
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig3-raw-face-energy-trend
  measured:
  - 0.487
  - 0.443
  - 0.442
  notes: Reading (a) of O3 gives 0.487, 0.443 and 0.442 a.u., all within tolerance; optimal is the
    largest, above sub-optimal with p = 0.00049 and above disengaged with p = 0.068 (paper 0.06).
    Reading (b) gives 0.489, 0.439 and 0.453 (p = 0.04 and 0.0046).
- claim: fig3-raw-locomotion-no-difference
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig3-raw-locomotion-no-difference
  measured:
  - 0.136
  - 0.135
  - 0.134
  notes: Optimal 0.136, disengaged 0.135, sub-optimal 0.134 m/s under reading (a), differences of
    0.002 m/s, p = 0.74 and 0.68; reading (b) 0.138, 0.132 and 0.139 m/s, p = 0.54 and 1. Speeds are
    read as m/s although the file labels them cm/s (findings).
- claim: fig4a-lower-variability
  outcome: partially_reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig4a-lower-variability
  notes: All six differences have the stated sign. Pupil, optimal against disengaged p = 0.00024 and
    against sub-optimal p = 0.01; face p = 0.0024 and 0.08; locomotion p = 0.0012 and 0.033. Five of
    six tests pass.
- claim: fig4b-variability-at-transitions
  outcome: partially_reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig4b-variability-at-transitions
  notes: All six changes have the stated sign on average over mice (entry, pupil 0.0316 to 0.0289,
    face 0.0750 to 0.0715, locomotion 0.0582 to 0.0540; exit, 0.0298 to 0.0337, 0.0716 to 0.0780,
    0.0551 to 0.0626). Of the four comparisons the figure marks, pupil exit (p = 0.0012) and
    locomotion exit (p = 0.0024) pass, face entry (p = 0.15) and locomotion entry (p = 0.24) do not.
    15 to 85 entries and 22 to 125 exits per mouse.
- claim: fig4d-pupil-movement-decoupling
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig4d-pupil-movement-decoupling
  notes: Mean r 0.104 (optimal), 0.438 (disengaged), 0.257 (sub-optimal); optimal lower than
    disengaged in 13 of 13 (p = 0.00024) and than sub-optimal in 10 of 13 (p = 0.0081). Disengaged is
    higher than sub-optimal (p = 0.0046), as the figure marks.
- claim: figs6-individual-measure-decoupling
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:figs6-individual-measure-decoupling
  notes: Pupil with face, optimal lower than disengaged (p = 0.0046) and sub-optimal (p = 0.033).
    Pupil with locomotion, lower than disengaged (p = 0.0046), not significantly lower than
    sub-optimal (p = 0.08). The face with locomotion correlation is also lower in the optimal state
    (p = 0.00049 and 0.00073).
- claim: figs1-iti-independence
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:figs1-iti-independence
  measured: 0.23
  notes: Median r with the preceding ITI, pupil -0.044, locomotion -0.007, face -0.044, none different
    from zero (p = 0.13, 0.89, 0.27), so the ITI part holds under readings (a) and (b). The
    Kruskal-Wallis test of the per-mouse median evoked pupil response over the four groups gives
    H = 4.32, p = 0.23 (three discrete states, p = 0.15); group means -1.1, 1.57, 0.04 and -0.6% of
    the maximum.
  deviations:
  - The pupil at onset is the filtered value at the stimulus sample; FigureS1.py takes it from the
    trial's pupil trace, 1 ms later. A standard choice that cannot change the result.
- claim: figs8a-regression-weights
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:figs8a-regression-weights
  notes: Optimal fits, pupil squared, locomotion squared, pupil SD and locomotion SD weights negative
    (medians -1.13, -1.07, -0.30, -0.35; Wilcoxon against zero p = 0.001, below 0.001, 0.008, 0.027).
    Disengaged fits, the same weights positive (1.11, 0.64, 0.19, 0.19; p below 0.001, below 0.001,
    0.013, 0.008). Face squared and face SD weights do not differ from zero (p 0.13 to 0.50). Reading
    (a) holds, and so does (b).
- claim: figs8b-pupil-movement-interaction
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:figs8b-pupil-movement-interaction
  measured:
  - 0.34
  - -0.82
  notes: Pupil-by-movement weight 0.34 +/- 0.11 over 22 sub-optimal fits and -0.82 +/- 0.23 over 13
    optimal fits, rank-sum p = 5.6e-05; quadratic movement weight of the optimal fits -1.52. Among the
    sub-optimal weights only the interaction differs from zero (p = 0.005).
- claim: fig5c-state-classification
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig5c-state-classification
  measured:
  - 88.5
  - 77.2
  notes: Eight features unshuffled (condition 13), 88.5% +/- 1.7% over 13 optimal against disengaged
    classifications and 77.2% +/- 1.6% over 21 optimal against sub-optimal classifications; the
    "All measures" condition 0 gives 88.2% and 76.4%. All 34 classifications are significant under
    readings (a), (b) and (c), with z from 4.98 to 11.16. The paper has 19 sub-optimal
    classifications; this attempt's fits give 22 sub-optimal states, 21 with enough trials.
  deviations:
  - 3 runs per shuffled condition and 20 null runs, in place of 1000, to fit the time limit. The
    unshuffled condition does not vary between runs. With 20 null runs the null SD and its 95th
    percentile are estimated less precisely.
  - Rests on this attempt's state fits (figs2-n-states).
- claim: figs7-pupil-best-raw-measure
  outcome: reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:figs7-pupil-best-raw-measure
  notes: Reading (a), accuracy, pupil 71.1%, face 65.7%, locomotion 67.7%; pupil above face in 23 of
    34 (p = 0.00046) and above locomotion on average (p = 0.034). The z-scores and reading (b) agree
    for face (p from 0.00018 to 0.00046); under (b) pupil is above locomotion on average (p = 0.059
    and 0.064).
  deviations:
  - As for fig5c-state-classification.
- claim: fig5c-movement-index-best
  outcome: not_reproduced
  notebook: reproduce_hulsey_2024.ipynb
  output: claim:fig5c-movement-index-best
  notes: Main reading (movement index value and SD kept, all else shuffled) gives 67.7% against 71.1%
    for pupil alone, movement higher in 13 of 34 (p = 0.017, the other way); z 4.42 against 5.29
    (p = 0.033). The code's conditions shown as variants make the movement index better than pupil,
    condition 5 (movement index kept with the pupil value) 74.5% (p = 7.4e-05) and condition 1 (face
    and locomotion shuffled) 76.7% (p = 2.3e-10); both keep pupil information in the movement-index
    classifier.
  deviations:
  - As for fig5c-state-classification.
findings:
- kind: metadata_error
  statement: The running_speed series of every file is labelled cm/s, but its values (session medians
    around 0.07, 99th percentiles up to 0.67) are in m/s, the unit of the paper and of its code.
- kind: selection_undocumented
  statement: The dandiset holds 391 stage 5 and 6 sessions of the 13 included mice, where the paper
    analysed 381. The paper's inclusion criteria select 376 of them counted from the reward series and
    375 counted from the hits, and nothing in the dandiset marks which sessions the paper used.
- kind: data_missing
  statement: The training sessions before stage 5, the other stage 5 and 6 sessions of the 500 the
    paper names, and the 18 mice that did not meet the inclusion criteria are not in the dandiset, so
    the training duration (21 +/- 8 sessions) cannot be tested.
- kind: other
  statement: In 38 of the 391 sessions the post hoc pupil diameter series is present but entirely
    missing values (14 of BW046's 34 sessions), so those sessions have no pupil measure.
- kind: metadata_error
  statement: The rig names in the session metadata are spelled several ways for what appear to be the
    same rigs (Box 1, Box1, Boox1).
- kind: methods_unavailable
  statement: Question for the paper's authors. Figure2.py types each state by its nearest template
    with nansum, so a state with no trial of posterior 0.8 or more in the sessions where the optimal
    state occurs scores 0 against every template and displaces the optimal label. In this attempt's
    fits one state of BW059 is such a state; it was typed on all sessions. How were such states
    handled, and which 381 sessions were analysed?
EOF
python tools/entry.py check entries/000678-hulsey-2024 2>&1 | tail -5
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  sed -i 's/    sessions failing either count are listed in the notebook (13 with fewer than 100 rewards, 2 with\n//' attempts/000678-hulsey-2024-01.yaml; python3 - <<'EOF'
p='attempts/000678-hulsey-2024-01.yaml'
s=open(p).read()
a="""The
    sessions failing either count are listed in the notebook (13 with fewer than 100 rewards, 2 with
    less than 20% at one port, and 2 that fail one count only)."""
assert a in s
s=s.replace(a,"""The
    sessions failing either count are listed in the notebook; 14 fail both (13 with fewer than 100
    rewards, 1 with less than 20% at one port) and 3 fail one count only.""")
open(p,'w').write(s)
EOF
cat > entries/000678-hulsey-2024/README.md <<'EOF'
# Hulsey, Zumwalt, Mazzucato, McCormick & Jaramillo (2024) from dandiset 000678

Tests the findings of [Hulsey et al. (2024)](https://doi.org/10.1016/j.celrep.2024.113709) on
[DANDI:000678](https://dandiarchive.org/dandiset/000678/0.231004.2146), which holds the stage 5 and 6
sessions of the 13 mice the paper analysed, with pupil diameter, face motion energy and locomotion
speed. The notebook fits the paper's GLM-HMM to each mouse's choices, labels the performance states,
and relates them to the arousal and movement measures.

| Claim | Outcome |
|---|---|
| 13 mice included, 8 auditory and 5 visual, 381 sessions | Partially reproduced (376 sessions) |
| 21 +/- 8 training sessions to reach stage 5 | Blocked: data missing |
| Distractor responses below 10% | Reproduced |
| 3 to 5 GLM-HMM states per mouse | Reproduced |
| Example mouse: 4 states, 78% against 70% of choices predicted | Reproduced |
| Every mouse has optimal, disengaged and sub-optimal states | Reproduced (one assumption) |
| Optimal state most occupied; 13.1% indeterminate | Partially reproduced |
| Optimal epochs longer; 3.4-trial transitions | Partially reproduced |
| GLM-HMM predicts 75.7% of choices, 10.8% better than one state | Reproduced |
| Inverted U of optimal state on pupil diameter | Reproduced |
| Smaller optimal pupil in the auditory task | Reproduced |
| Inverted U (optimal) and U (disengaged) aligned to the optimal pupil | Reproduced |
| Face and locomotion r2 below pupil's | Partially reproduced |
| Inverted U on the movement index, r2 like pupil's | Partially reproduced |
| U of the disengaged state on the movement index | Reproduced |
| Movement index equally correlated with face and locomotion | Reproduced |
| Pupil closest to optimal in the optimal state | Partially reproduced |
| Face motion energy larger in the optimal state | Reproduced |
| No difference in locomotion speed between states | Reproduced |
| Lower variability of the measures in the optimal state | Partially reproduced |
| Variability falls on entering and rises on leaving the optimal state | Partially reproduced |
| Pupil and movement decoupled in the optimal state | Reproduced |
| Pupil decoupled from face and locomotion in the optimal state | Reproduced |
| SVM decoding of states: 88.2% and 77.7% | Reproduced |
| Pupil the best single raw measure for decoding | Reproduced |
| Movement index the best predictor of state | Not reproduced |
| Regression weights of pupil and locomotion terms | Reproduced |
| Pupil-by-movement interaction for sub-optimal states | Reproduced |
| ITI does not carry over; evoked pupil equal across states | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The GLM-HMM of the paper's ssm fork is reimplemented in `hulsey.py`; the cross-validation runs 3
random initialisations per fold, not 10, and the decoders fewer shuffle runs, to keep the notebook
near 15 minutes on 4 cores. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/000678-hulsey-2024-01.yaml`](../../attempts/000678-hulsey-2024-01.yaml).

- `reproduce_hulsey_2024.ipynb`: the analysis.
- `hulsey.py`: streaming and preprocessing the files as the paper's code does, the GLM-HMM, state
  labels, dwell times, choice prediction and the decoders. Other notebooks on this dandiset can
  import it.
EOF
cd $TMPDIR/dev; . $TMPDIR/env/bin/activate; python build.py; cd  python tools/entry.py check entries/000678-hulsey-2024 2>&1 | tail -3; date -u
```

```
94
0 error(s)
Sat Oct 31 10:32:05 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python - <<'EOF'
s=open('nb.py').read()
a='''    print(meas, "mean over mice:", tab.mean().round(4).to_dict())'''
assert a in s
s=s.replace(a,'''    print(meas, "per mouse:")
    print(tab.round(4).T.to_string())
    print(meas, "mean over mice:", tab.mean().round(4).to_dict())''')
a='''    print(f"r({a_m}, {b_m}) mean over mice:", tab.mean().round(3).to_dict())'''
assert a in s
s=s.replace(a,'''    print(f"r({a_m}, {b_m}) per mouse:", {k: list(v.round(2).values) for k, v in tab.T.iterrows()})
    print(f"r({a_m}, {b_m}) mean over mice:", tab.mean().round(3).to_dict())''')
a='''print("\\nTrials by state (0 optimal, 1 disengaged, 2 or more other; NaN indeterminate):",'''
assert a in s
s=s.replace(a,'''print("\\nSessions with the optimal state:", int(trials.groupby("path").sess_has_opt.first().sum()),
      "| with more than 10 optimal trials and a post hoc pupil (M5):", int(trials.groupby("path").sess_opt10.first().sum()),
      "of", trials.path.nunique())
m5 = trials[trials.sess_opt10]
print("Trials in the M5 sessions:", len(m5), "| with all six measures:", len(m5.dropna(subset=["post_hoc_pupil_diameter",
      "post_hoc_pupil_std10", "face_energy", "face_std_10", "running_speed", "running_std10"])),
      "| of these in a discrete state:", int(m5.dropna(subset=["post_hoc_pupil_diameter", "post_hoc_pupil_std10", "face_energy",
      "face_std_10", "running_speed", "running_std10"]).hmm_state.notna().sum()))
print("\\nTrials by state (0 optimal, 1 disengaged, 2 or more other; NaN indeterminate):",''')
open('nb.py','w').write(s)
EOF
. $TMPDIR/env/bin/activate; python build.py; cd  date -u; python tools/entry.py all entries/000678-hulsey-2024 2>&1 | tail -3; date -u
```

```
94
Sat Oct 31 10:32:17 UTC 2026
Installed kernelspec registry-000678-hulsey-2024 in executed/000678-hulsey-2024/.venv/share/jupyter/kernels/registry-000678-hulsey-2024
0 error(s)
pass  reproduce_hulsey_2024.ipynb  (822 s)
Sat Oct 31 10:46:08 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/exec_out2.txt
import json
nb=json.load(open('executed/000678-hulsey-2024/reproduce_hulsey_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print(f"=== cell {i} {c['metadata'].get('tags')}")
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text']))
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
EOF
diff <(grep -v "fits in\|streamed\|min$" $TMPDIR/exec_out.txt) <(grep -v "fits in\|streamed\|min$" $TMPDIR/exec_out2.txt) | head -80
```

```
85c85,86
< Sessions in the dandiset: 391
---
> Sessions in the dandiset:
>  391
228a230,233
> 
> Sessions with the optimal state: 356 | with more than 10 optimal trials and a post hoc pupil (M5): 310 of 376
> Trials in the M5 sessions: 136950 | with all six measures: 129876 | of these in a discrete state: 109646
> 
432d436
< 
468a473,477
> post_hoc_pupil_std10 per mouse:
>               BW041   BW045   BW046   BW048   BW051   BW053   BW058   BW059   BW061   BW062   BW064   BW067   BW071
> optimal      0.0302  0.0462  0.0215  0.0207  0.0285  0.0482  0.0232  0.0177  0.0245  0.0281  0.0275  0.0161  0.0186
> disengaged   0.0558  0.0501  0.0306  0.0510  0.0431  0.0953  0.0707  0.0308  0.0289  0.0288  0.0317  0.0256  0.0457
> sub-optimal  0.0422  0.0468  0.0236  0.0272  0.0361  0.0622  0.0564  0.0205  0.0184  0.0267  0.0283  0.0189  0.0259
470a480
> 
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python - <<'EOF'
s=open('nb.py').read()
a='''    print(f"r({a_m}, {b_m}) per mouse:", {k: list(v.round(2).values) for k, v in tab.T.iterrows()})'''
assert a in s
s=s.replace(a,'''    print(f"r({a_m}, {b_m}) per mouse:")
    print(tab.round(3).T.to_string())''')
open('nb.py','w').write(s)
EOF
. $TMPDIR/env/bin/activate; python build.py; cd  python tools/entry.py all entries/000678-hulsey-2024 2>&1 | tail -2; date -u
```

```
94
0 error(s)
pass  reproduce_hulsey_2024.ipynb  (793 s)
Sat Oct 31 10:59:38 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/exec_out3.txt
import json
nb=json.load(open('executed/000678-hulsey-2024/reproduce_hulsey_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print(f"=== cell {i} {c['metadata'].get('tags')}")
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text']))
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
EOF
diff <(grep -v "fits in\|streamed\|min$" $TMPDIR/exec_out2.txt) <(grep -v "fits in\|streamed\|min$" $TMPDIR/exec_out3.txt) | head -30; grep "streamed\|fits in" $TMPDIR/exec_out3.txt; python tools/entry.py handover entries/000678-hulsey-2024 2>&1 | tail -3; ls executed/000678-hulsey-2024/handover; git status --short
```

```
43d42
< 
85,86c84
< Sessions in the dandiset:
<  391
---
> Sessions in the dandiset: 391
130d127
< 
143a141
> 
230d227
< 
231a229
> 
440a439
> 
451a451
> 
462a463
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la .bash_profile .bashrc .gitconfig .idea .mcp.json .profile .ripgreprc .vscode .zprofile .zshrc scripts 2>&1 | head -20; ls entries/000678-hulsey-2024
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 09:18 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 09:18 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 09:18 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 09:18 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 09:18 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 09:18 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 09:18 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 09:18 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 09:18 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 09:18 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 09:18 scripts
README.md
__pycache__
entry.yaml
hulsey.py
reproduce_hulsey_2024.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
cd  rm -rf entries/000678-hulsey-2024/__pycache__; python tools/entry.py check entries/000678-hulsey-2024 2>&1 | tail -2; git status --short entries attempts; date -u
```

```
0 error(s)
?? attempts/000678-hulsey-2024-01.yaml
?? entries/000678-hulsey-2024/
Sat Oct 31 11:00:07 UTC 2026
```

**Agent**

I did steps 1 to 5 of the Author protocol and ran the handover. The entry is `entries/000678-hulsey-2024/`, the record is `attempts/000678-hulsey-2024-01.yaml`, and the handover package is in `executed/000678-hulsey-2024/handover/`. `tools/entry.py all` passed with 0 errors, and the notebook ran in 13 to 14 minutes. Nothing is committed.

**1. Outcomes per claim**

| Claim | Outcome |
|---|---|
| cohort-inclusion | partially reproduced: 13 mice (8 auditory, 5 visual) match; 376 sessions pass the criteria, not 381 |
| training-duration | blocked, `data_missing` (only stage 5 and 6 sessions are in the dataset) |
| distractor-response-rate | reproduced: 5.2% overall; one mouse, BW053, at 16% |
| figs2-n-states | reproduced: 3 to 5 states per mouse under both readings |
| fig1g-example-mouse-prediction | reproduced: BW046 has 4 states; 70.2% against 78.3% |
| fig2a-state-types | reproduced, resting on one assumption (`assumed: true`) |
| fig2b-optimal-occupancy | partially reproduced: all tests pass; indeterminate share 14.8%, just outside 13.1 ± 1.6 |
| fig2c-dwell-times | partially reproduced: tests pass and the optimal dwell (39.5) matches; indeterminate 3.0 and disengaged 11.9 are outside tolerance |
| fig2d-prediction-accuracy | reproduced: 76.0%, a gain of 10.9 points |
| fig3c-inverted-u-pupil, fig3d-optimal-pupil-modality, fig3e-u-disengaged-pupil | reproduced |
| figs4-r2-individual-movement | partially reproduced: pupil r2 is 0.65; face and locomotion are lower on average but mostly not significantly |
| fig3f-movement-index-inverted-u | partially reproduced: shape holds and p = 0.34 as in the paper; r2 is 0.567 against 0.63 ± 0.06 |
| fig3f-movement-index-u-disengaged, figs5-movement-index-correlations | reproduced |
| fig3-distance-from-optimal-pupil | partially reproduced: the order and tests hold, but the values are larger than the paper's |
| fig3-raw-face-energy-trend, fig3-raw-locomotion-no-difference | reproduced |
| fig4a-lower-variability | partially reproduced: 5 of 6 tests pass |
| fig4b-variability-at-transitions | partially reproduced: all signs hold; 2 of the 4 marked tests pass |
| fig4d-pupil-movement-decoupling, figs6-individual-measure-decoupling | reproduced |
| fig5c-state-classification | reproduced: 88.5% and 77.2% |
| figs7-pupil-best-raw-measure | reproduced |
| fig5c-movement-index-best | not reproduced under the claim's main reading; the paper code's conditions 5 and 1 reproduce it |
| figs8a-regression-weights, figs8b-pupil-movement-interaction, figs1-iti-independence | reproduced |

**2. What was found about the dataset**
- I pinned version 0.231004.2146 because the paper cites it. The later 0.261020.0029 has identical assets and differs only in archive metadata; the notebook header says this.
- The dataset holds 391 sessions from stages 5 and 6, against 381 in the paper. Nothing marks which sessions the paper used.
- The excluded mice, the other stage 5 and 6 sessions, and all training before stage 5 are absent. That is why training-duration is blocked.
- `running_speed` is labelled cm/s but the values are m/s.
- 38 sessions have a post hoc pupil series that is entirely missing values.
- Rig names are spelled several ways ("Box 1", "Box1", "Boox1").
- No recording is deposited twice. A response against no-response contrast is consistent with the measures sharing the trial clock.

**Assumption:** one state of mouse BW059 has no trials confidently in that state (posterior ≥ 0.8) in the sessions where the optimal state occurs. The paper's state-typing code (Figure2.py) would score such a state as matching every template, so I typed it on all of the mouse's sessions. The question to the paper's authors (how such states were handled, and which 381 sessions were analysed) is recorded as a `methods_unavailable` finding.

I asked no reader questions.

**3. Where the protocol was unclear or did not fit**
1. The paper's method cannot run in full within the 30-minute notebook limit: 10 initialisations per fold for choosing the number of states, and 1000 shuffle runs for the decoders. I reduced these to 3 initialisations, and to 3 runs per shuffled condition plus 20 null runs. I recorded this as a deviation, not as `too_large`, because blocking it would have blocked almost every claim that depends on the state fits.
2. The paper's model library (its fork of ssm) is not a locked dependency, so I reimplemented the model in `hulsey.py` with the same EM, priors and stopping rule. The protocol says nothing about reimplementing a method versus installing the original; I recorded it as a deviation.
3. The protocol does not say what to do when the paper's own code has a latent bug that the data trigger (the empty-state typing above). I treated my fix as an assumption and asked the authors.
4. The protocol has no rule for a session set that the dataset cannot reconstruct (381 reported, 376 passing the criteria). I used the paper's criteria and recorded a `selection_undocumented` finding.

**4. Runtime and failures**
The run started at 09:19 and finished at 11:00 UTC. The notebook takes about 13.5 minutes on 4 cores: about 3 to stream the files, 4 for the cross-validation fits and 6 for the decoders. The last three full runs gave identical numbers. During development a first version of the model fitting diverged; I fixed it with damped Newton steps before any reported fit. Nothing failed in the final runs.

## End of run

106 turns, 100 minutes, result: success.
