# 000055 · author · run 38870441263

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls entries claims attempts | head -50
```

```
# Protocol for an attempt

Version: `pilot-7`. Record this version in the attempt's provenance.

This is what an agent, or a person, does to attempt a target and deposit the
result. It is written from the eight pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

There are two roles. The **author** makes the attempt. The **verifier** checks
it and must not be the author: for agents, a separate run with a separate
context that has not seen the author's reasoning.

Agent runs are made with the [Agent run](../.github/workflows/attempt.yml)
workflow, one role at a time: `author`, `verifier-1`, `author-revise-1`,
`verifier-2`, `author-revise-2`, and, when the last of these proposes changes
of outcome, `verifier-3` and `author-revise-3`. Each run's transcript and final report are
kept in [`transcripts/<dandiset>/`](../transcripts).

## Author

[... 408 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md | head -400; ls entries/001453-fouke-2025 claims/001453; cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (55.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e4dcc5c4-cdf8-4de0-938c-c8b39ed4937d/tool-results/bq6i7h37p.txt

Preview (first 2KB):
# Reproduction registry (working name)

Agents, and people, try to reproduce the key findings of papers from the open
data on the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>

## Reading the outcomes
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e4dcc5c4-cdf8-4de0-938c-c8b39ed4937d/tool-results/bq6i7h37p.txt"
}
```

```
1	# Reproduction registry (working name)
2	
3	Agents, and people, try to reproduce the key findings of papers from the open
4	data on the [DANDI Archive](https://dandiarchive.org), and register the result
5	here: the notebooks when it works, and the reason when it does not.
6	
7	- **For the archive:** evidence of whether each dandiset is complete and
8	  accurate enough to support the findings of its paper.
9	- **For analysts:** working notebooks to build new analyses on.
10	
11	Status: pilot. All eight pilot targets have been attempted and checked by an
12	independent agent.
13	
14	**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>
15	
16	## Reading the outcomes
17	
18	An outcome says what one attempt could recover from the data in a dandiset,
19	with the methods available to it. **A "not reproduced" or "partially
20	reproduced" outcome is not a finding that the paper is wrong.** It can come
[... 993 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 ../../claims/001453/*.yaml; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:2500]); print('-----')
print(len(nb['cells']))
for c in nb['cells']: print(c['cell_type'], c.get('metadata',{}).get('tags'), ''.join(c['source'])[:100].replace('\n',' | '))
"
```

```
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
- id: dandi:001453/0.250518.1950
  relation: uses_data
- id: doi:10.1016/j.cub.2025.04.027
[... 271 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,120p entries/001453-fouke-2025/omr.py; ls schemas tools; sed -n 1,80p schemas/claims*.json 2>/dev/null | head -120
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
[... 196 more lines not kept]
```

**Agent**

Now the target: the paper and the dandiset.

**Agent calls Bash**

```bash
cd  sed -n 80,200p schemas/claims.schema.json; mkdir -p paper; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1523/eneuro.0007-21.2021&format=json&resultType=core" | python -c "import json,sys;d=json.load(sys.stdin);r=d['resultList']['result'][0];print(r.get('pmcid'),r.get('isOpenAccess'),r.get('title'),r.get('license'))"; curl -s https://api.dandiarchive.org/api/dandisets/000055/versions/ | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent**

The paper is open access (PMC8225404, CC BY); the dandiset is AJILE12, 845 GB in 55 files with one published version. Fetching the full text.

**Agent calls Bash**

```bash
cd  curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8225404/fullTextXML" -o paper/peterson2021.xml; ls -la paper; python - <<'EOF'
import re
x=open('paper/peterson2021.xml').read()
t=re.sub(r'<xref[^>]*>(.*?)</xref>',r'\1',x)
t=re.sub(r'</(p|title|caption|label)>','\n',t)
t=re.sub(r'<[^>]+>','',t)
t=re.sub(r'\n\s*\n+','\n\n',t)
open('paper/peterson2021.txt','w').write(t)
print(len(t))
EOF
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "paper/peterson2021.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Paper full text (CC BY, PMC8225404) saved. Now listing the dandiset assets and metadata.

**Agent calls Bash**

```bash
cd  python -c "import dandi, pynwb, h5py, remfile; print(dandi.__version__, pynwb.__version__)" ; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/assets/?page_size=100" | python -c "
import json,sys;d=json.load(sys.stdin)
for a in d['results']: print(a['path'], round(a['size']/1e9,2), a['asset_id'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q expl && . expl/bin/activate && uv pip install -q dandi h5py remfile numpy pandas scipy pynwb matplotlib statsmodels 2>&1 | tail -2; python -c "import dandi,pynwb;print(dandi.__version__,pynwb.__version__)"
```

```
0.81.0 4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && cat > list1.py <<'EOF'
import h5py, remfile, numpy as np, time
from dandi.dandiapi import DandiAPIClient
t0=time.time()
with DandiAPIClient() as c:
    ds=c.get_dandiset("000055","0.220127.0436")
    meta=ds.get_raw_metadata()
    a=ds.get_asset_by_path("sub-01/sub-01_ses-3_behavior+ecephys.nwb")
    url=a.get_content_url(follow_redirects=1, strip_query=True)
import json
print(json.dumps({k:meta.get(k) for k in ['name','description','relatedResource','assetsSummary','citation','license','wasGeneratedBy']},indent=1)[:5000])
f=h5py.File(remfile.File(url),'r')
def visit(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype, dict((k,(v if not isinstance(v,bytes) else v.decode())) for k,v in obj.attrs.items() if k in('unit','conversion','rate','description','starting_time','resolution','offset')))
    else:
        a=dict(obj.attrs)
        print(name+'/', {k:str(v)[:200] for k,v in a.items() if k in ('neurodata_type','description','colnames','rate')})
f.visititems(visit)
print(time.time()-t0)
EOF
python list1.py
```

```
{
 "name": "AJILE12: Long-term naturalistic human intracranial neural recordings and pose",
 "description": "Understanding the neural basis of human movement in naturalistic scenarios is critical for expanding neuroscience research beyond constrained laboratory paradigms. The neural correlates of unstructured, spontaneous movements in completely naturalistic settings have rarely been studied, due in large part to a lack of available data. Here, we present our Annotated Joints in Long-term Electrocorticography for 12 human participants (AJILE12) dataset, the largest human neurobehavioral dataset that is publicly available; the dataset was recorded opportunistically during passive clinical epilepsy monitoring. AJILE12 includes synchronized intracranial neural recordings and upper body pose trajectories across 55 semi-continuous days of naturalistic movements, along with relevant metadata, including thousands of wrist movement events and annotated behavioral states. Neural recordings are available at 500 Hz from at least 64 electrodes per participant, for a total of 1280 hours. Pose trajectories at 9 upper-body keypoints, including wrist, elbow, and shoulder joints, were sampled at 30 frames per second and estimated from 118 million video frames. In adherence with the FAIR data principles, we have shared AJILE12 on The Dandi Archive in the Neurodata Without Borders (NWB) data standard and developed a browser-based dashboard to facilitate data exploration and reuse.",
 "relatedResource": [
  {
   "url": "https://doi.org/10.1523/ENEURO.0007-21.2021",
   "name": "Behavioral and Neural Variability of Naturalistic Arm Movements",
   "relation": "dcite:IsDescribedBy",
   "schemaKey": "Resource",
   "identifier": "DOI:10.1523/ENEURO.0007-21.2021"
  },
  {
   "url": "https://doi.org/10.1016/j.jneumeth.2021.109199",
   "name": "Mining naturalistic human behaviors in long-term video and neural recordings",
   "relation": "dcite:IsDescribedBy",
   "schemaKey": "Resource",
   "ide
[... 225 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && cat > list2.py <<'EOF'
import h5py, remfile, numpy as np, time, pandas as pd
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("000055","0.220127.0436")
    url=ds.get_asset_by_path("sub-01/sub-01_ses-3_behavior+ecephys.nwb").get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
d=f['acquisition/ElectricalSeries/data']
print('chunks',d.chunks,d.compression,d.compression_opts)
print(f['processing/behavior/Position/R_Wrist/data'].chunks)
for k in ['session_description','session_start_time','timestamps_reference_time','identifier','general/session_id','general/subject/species','general/subject/subject_id']:
    print(k, f[k][()])
print([k for k in f['general'].keys()])
print('ref frame', f['processing/behavior/Position/R_Wrist/reference_frame'][()])
print('ReachEvents desc', dict(f['processing/behavior/ReachEvents'].attrs))
e=f['general/extracellular_ephys/electrodes']
df=pd.DataFrame({k:e[k][:] for k in ['x','y','z','imp','location','group_name','good','standard_deviation','kurtosis','median_deviation','low_freq_R2','high_freq_R2']})
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
print(df.to_string())
ep=f['intervals/epochs']
lab=pd.Series([x.decode() if isinstance(x,bytes) else x for x in ep['labels'][:]])
print(lab.value_counts().head(40))
st,sp=ep['start_time'][:],ep['stop_time'][:]
print(st[:5],sp[:5], st.min(), sp.max())
r=f['intervals/reaches']
rd=pd.DataFrame({k:r[k][:] for k in ['start_time','stop_time','Reach_magnitude_px','Reach_angle_degrees','Onset_speed_px_per_sec','Speech_ratio','Bimanual_ratio','Bimanual_overlap','Bimanual_class']})
print(rd.describe().T)
print(rd.head(10))
ev=f['processing/behavior/ReachEvents/timestamps'][:]
print(ev[:10], np.abs(ev-rd.start_time.values).max())
t0=time.time(); x=d[1000000:1005000,:]; print('read 10s', time.time()-t0, x.shape, np.nanpercentile(x,[1,50,99]), np.isnan(x).mean())
t0=time.time(); w=f['processing/behavior/Position/R_Wrist/data'][:]; print('wrist read',time.time()-t0, np.nanpercentile(w,[1,50,99],axis=0), np.isnan(w).mean())
EOF
python list2.py
```

```
chunks (84375, 1) gzip 4
(5063, 1)
session_description b'no description'
session_start_time b'2000-01-02T19:00:00-05:00'
timestamps_reference_time b'2000-01-02T19:00:00-05:00'
identifier b'4c571b6c-1028-476f-b0e1-e34aa27b3206'
general/session_id b'3'
general/subject/species b'Homo sapiens'
general/subject/subject_id b'01'
['devices', 'extracellular_ephys', 'session_id', 'subject']
ref frame b'unknown'
ReachEvents desc {'description': 'r_wrist', 'namespace': 'ndx-events', 'neurodata_type': 'Events', 'object_id': '4139bd10-e36b-4de7-830c-fef06010d3ca'}
            x          y          z  imp    location group_name   good  standard_deviation    kurtosis  median_deviation  low_freq_R2  high_freq_R2
0  -45.648495  38.560372  36.187962  NaN  b'unknown'    b'GRID'  False           35.398535    6.154781         28.978650     0.013106     -0.001107
1  -47.347152  31.182861  41.176799  NaN  b'unknown'    b'GRID'   True           55.518727    1.309332         48.247142    -0.004729     -0.019041
2  -50.291409  22.157208  45.191885  NaN  b'unknown'    b'GRID'   True           33.992008    1.585154         31.077800    -0.003226     -0.003235
3  -51.358961  11.787268  48.726509  NaN  b'unknown'    b'GRID'   True           33.701261    2.652564         28.651509     0.036002     -0.013343
4  -51.219818   1.713889  53.000981  NaN  b'unknown'    b'GRID'   True           59.648470    2.626867         51.301159     0.096380     -0.014212
5  -51.215001  -6.680892  57.994505  NaN  b'unknown'    b'GRID'   True           76.684587    5.448267         58.777123     0.134391     -0.009448
6  -52.291020 -18.127226  61.412827  NaN  b'unknown'    b'GRID'   True           52.276869    0.546240         51.063440     0.149291      0.004633
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/BruntonUWBio/naturalistic_arm_movements_ecog nam && cd nam && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | head -100 && cat README.md | head -80
```

```
04c6faf2f219586fa834d10c614ef48a694cec55 Wed Mar 17 09:23:58 2021 -0700
./project_data_rois_matlab/set_environment_paths.m
./project_data_rois_matlab/project_ecog_to_rois.m
./upload_figshare.py
./LICENSE
./README.md
./compute_power_gen_figs_python/regression_utils.py
./compute_power_gen_figs_python/feat_plot_utils.py
./compute_power_gen_figs_python/tfr_utils.py
./compute_power_gen_figs_python/.ipynb_checkpoints/Projected_spectral_power_Figs3_4-checkpoint.ipynb
./compute_power_gen_figs_python/.ipynb_checkpoints/Behavioral_features_Fig2-checkpoint.ipynb
./compute_power_gen_figs_python/__pycache__/tfr_utils.cpython-36.pyc
./compute_power_gen_figs_python/__pycache__/regression_utils.cpython-36.pyc
./compute_power_gen_figs_python/__pycache__/feat_plot_utils.cpython-36.pyc
./compute_power_gen_figs_python/__pycache__/config.cpython-36.pyc
./compute_power_gen_figs_python/fit_regression_models.py
./compute_power_gen_figs_python/Regression_results_Fig6.ipynb
./compute_power_gen_figs_python/compute_spectral_power.py
./compute_power_gen_figs_python/config.py
./compute_power_gen_figs_python/Plot_banded_power_Fig5.ipynb
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nam/compute_power_gen_figs_python && cat config.py compute_spectral_power.py && sed -n 1,400p tfr_utils.py
```

```
import numpy as np

root_dir = '.../data_release_scripts/'

constants_compute_tfr = {'pad_val' : 0.5,
                         'alpha' : 0.05,
                         'n_perms' : 2000,
                         'freqs' : np.arange(1, 124, 5),
                         'decim' : 50,
                         'baseline_vals' : [-1.5,-1]
                        } #units: pad_val (sec), freqs (Hz), baseline_vals (sec)

constants_plot_tfr = {'epoch_times' : [-1.5,1.51],
                      'vscale_val' : 1,
                      'atlas' : 'aal',
                      'alpha' : 0.05,
                      'n_perms' : 2000,
                      'stat_method' : 'fdr_bh',
                      'baseline_vals' : [-1.5,-1],
                      'epoch_times_plot' : [-1.5,1.51],
[... 541 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nam/compute_power_gen_figs_python && for nb in Plot_banded_power_Fig5.ipynb Behavioral_features_Fig2.ipynb; do echo "=== $nb"; python -c "
import json,sys;nb=json.load(open('$nb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        print(''.join(c['source'])); 
        for o in c.get('outputs',[]):
            if 'text' in o: print('OUT>', ''.join(o['text'])[:1500])
            elif 'data' in o and 'text/plain' in o['data']: print('OUT>', ''.join(o['data']['text/plain'])[:1500])
        print('-----')
"; done
```

```
=== Plot_banded_power_Fig5.ipynb
%matplotlib inline
import numpy as np
import pdb, sys, natsort
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg
from matplotlib import rcParams
rcParams['font.family'] = 'Times New Roman'

from tfr_utils import load_project_spectral_power
-----
tfr_lp = '.../data_release/naturalistic_reaches/tfr/'
roi_proj_loadpath = '.../data_release/roi_proj_matlab/'
n_subjs = 12

rem_bad_chans = True #don't use bad channels for ROI projection
elec_dens_thresh = 3 #threshold for dipole density

[... 294 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nam/compute_power_gen_figs_python && sed -n 1,200p feat_plot_utils.py; cat ../project_data_rois_matlab/project_ecog_to_rois.m
```

```
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
    '''
    Transforms behavioral/environmental features
    '''
    #Set reach angle to range from -90 to 90
    df_metadata['reach_a'] = -df_metadata['reach_a'] # Correct angle for upper half
    df_metadata['reach_a'] = df_metadata['reach_a'].map(lambda x: x if x <= 90 else 180-x)
[... 421 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.figshare.com/v2/projects/78666/articles?page_size=100" | python -c "
import json,sys;d=json.load(sys.stdin)
for a in d: print(a['id'], a['title'], a.get('doi'), a.get('defined_type_name'))"; cat nam/upload_figshare.py | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for id in 12114408 12115728; do curl -s "https://api.figshare.com/v2/articles/$id" | python -c "
import json,sys;d=json.load(sys.stdin)
print(d['title'], d['doi'], d.get('version'), d.get('published_date'))
fs=d['files']; print(len(fs), sum(f['size'] for f in fs)/1e9,'GB')
for f in fs[:40]: print(' ',f['name'], f['size'], f['download_url'])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/nam/compute_power_gen_figs_python && cat fit_regression_models.py; sed -n 1,400p regression_utils.py
```

```
import os,pdb,argparse
os.environ["OMP_NUM_THREADS"] = "1" #avoid multithreading if have Anaconda numpy
import numpy as np

#Packages for multiprocessing
from multiprocessing import Pool
from functools import partial

#Custom packages
import config
from regression_utils import single_subj_regression
from tfr_utils import str2bool


def main(tfr_lp,save_folder,feats2use,n_perms,n_subjs,n_proc,model_type,add_interactions=False):
    '''
    Perform robust linear regression between behavioral features and spectral power.
    Allows for running subjects in parallel to speed up computation time (see n_proc variable).
    The only required inputs are the load/save pathnames and directory pathname for the projection matrices.
    '''
[... 460 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && cat > meta_all.py <<'EOF'
import h5py, remfile, numpy as np, time, pandas as pd, pickle
from concurrent.futures import ProcessPoolExecutor
from dandi.dandiapi import DandiAPIClient
def txt(v):
    v=v[()]; return v.decode() if isinstance(v,bytes) else str(v)
def load(pu):
    path,url=pu
    t0=time.time()
    with h5py.File(remfile.File(url),'r') as f:
        r=f['intervals/reaches']
        rd=pd.DataFrame({k:r[k][:] for k in r['colnames'] if False} if False else {k:r[k][:] for k in ['start_time','stop_time','Reach_magnitude_px','Reach_angle_degrees','Onset_speed_px_per_sec','Speech_ratio','Bimanual_ratio','Bimanual_overlap','Bimanual_class']})
        e=f['general/extracellular_ephys/electrodes']
        el=pd.DataFrame({k:e[k][:] for k in ['x','y','z','location','group_name','good','low_freq_R2','high_freq_R2']})
        el['group_name']=el.group_name.str.decode('utf8')
        groups={g:txt(f['general/extracellular_ephys/'+g].attrs['description']) if isinstance(f['general/extracellular_ephys/'+g].attrs['description'],(bytes,str)) else '' for g in f['general/extracellular_ephys'] if g!='electrodes'}
        groups={g: (f['general/extracellular_ephys/'+g].attrs['description']) for g in f['general/extracellular_ephys'] if g!='electrodes'}
        ep=f['intervals/epochs']
        epd=pd.DataFrame({'start':ep['start_time'][:],'stop':ep['stop_time'][:],'label':[x.decode() if isinstance(x,bytes) else x for x in ep['labels'][:]]})
        info=dict(path=path, subject=txt(f['general/subject/subject_id']), session=txt(f['general/session_id']),
             start=txt(f['session_start_time']), ref=txt(f['timestamps_reference_time']),
             n_samples=f['acquisition/ElectricalSeries/data'].shape[0], n_ch=f['acquisition/ElectricalSeries/data'].shape[1],
             rate=float(f['acquisition/ElectricalSeries/starting_time'].attrs['rate']), t_start=float(f['acquisition/ElectricalSeries/starting_time'][()]),
             pose_n=f['processing/behavior/Position/R_Wrist/data'].shape[0],
             ev_desc=txt(f['processing/behavior/ReachEvents/description']) if 'description' in f['processing/behavior/ReachEvents'] else f['processing/behavior/ReachEvents'].attrs.get('description'),
             ev_ts=f['processing/behavior/ReachEvents/timestamps'][:],
             subj_keys=list(f['general/subject'].keys()), shuffle=f['acquisition/ElectricalSeries/data'].shuffle,
             acq=list(f['acquisition'].keys()), elec_ref=f['acquisition/ElectricalSeries/electrodes'][:])
    return info, rd, el, groups, epd, time.time()-t0
if __name__=='__main__':
    with DandiAPIClient() as c:
        ds=c.get_dandiset("000055","0.220127.0436")
        pus=sorted((a.path,a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets())
    t0=time.time()
    with ProcessPoolExecutor(12) as ex: res=list(ex.map(load,pus))
    print('total',time.time()-t0, [round(r[-1]) for r in res])
    pickle.dump(res,open('meta_all.pkl','wb'))
EOF
python meta_all.py
```

```
Exit code 1
concurrent.futures.process._RemoteTraceback: 
"""
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/process.py", line 255, in _process_worker
    r = call_item.fn(*call_item.args, **call_item.kwargs)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/process.py", line 204, in _process_chunk
    return [fn(*args) for args in chunk]
            ~~^^^^^^^
  File "/tmp/claude-1001/meta_all.py", line 15, in load
    groups={g:txt(f['general/extracellular_ephys/'+g].attrs['description']) if isinstance(f['general/extracellular_ephys/'+g].attrs['description'],(bytes,str)) else '' for g in f['general/extracellular_ephys'] if g!='electrodes'}
              ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/meta_all.py", line 5, in txt
    v=v[()]; return v.decode() if isinstance(v,bytes) else str(v)
      ~^^^^
TypeError: string indices must be integers, not 'tuple'
"""

The above exception was the direct cause of the following exception:

[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && python - <<'EOF'
import re
s=open('meta_all.py').read()
s=s.replace("""        groups={g:txt(f['general/extracellular_ephys/'+g].attrs['description']) if isinstance(f['general/extracellular_ephys/'+g].attrs['description'],(bytes,str)) else '' for g in f['general/extracellular_ephys'] if g!='electrodes'}\n""","")
s=s.replace("ev_desc=txt(f['processing/behavior/ReachEvents/description']) if 'description' in f['processing/behavior/ReachEvents'] else f['processing/behavior/ReachEvents'].attrs.get('description')","ev_desc=f['processing/behavior/ReachEvents'].attrs.get('description')")
open('meta_all.py','w').write(s)
EOF
python meta_all.py
```

```
total 8.260326147079468 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && python - <<'EOF'
import pickle, pandas as pd, numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_rows',300); pd.set_option('display.max_columns',30)
res=pickle.load(open('meta_all.pkl','rb'))
rows=[]
for info,rd,el,groups,epd,_ in res:
    rows.append(dict(path=info['path'],subj=info['subject'],ses=info['session'],start=info['start'],ref=info['ref'],ns=info['n_samples'],nch=info['n_ch'],rate=info['rate'],t0=info['t_start'],pose=info['pose_n'],ev=len(rd),evts=len(info['ev_ts']),desc=info['ev_desc'],keys=info['subj_keys'],shuffle=info['shuffle'],acq=len(info['acq']),
    ngood=int(el.good.sum()), nR2=np.isfinite(el.low_freq_R2).sum(), maxR2lo=el.low_freq_R2.max(), maxR2hi=el.high_freq_R2.max(), xmean=el.x.mean(), groups=','.join(sorted(groups))))
df=pd.DataFrame(rows); print(df.drop(columns=['path']).to_string())
print(df.groupby('subj').ev.agg(['sum','count']))
s=df.groupby('subj').ev.sum(); print('median',s.median(),'min',s.min(),'max',s.max())
EOF
```

```
subj ses                             start                               ref        ns  nch   rate   t0     pose   ev  evts     desc                   keys  shuffle  acq  ngood  nR2   maxR2lo   maxR2hi      xmean                                             groups
0    01   3         2000-01-02T19:00:00-05:00         2000-01-02T19:00:00-05:00  43200000   94  500.0  0.0  2592000  156   156  r_wrist  [species, subject_id]    False    5     85   94  0.149291  0.055118 -53.675056                   ECG,EOG,GRID,LAT,LID,LMT,LPT,LTO
1    01   4         2000-01-03T19:00:00-05:00         2000-01-03T19:00:00-05:00  43200000   94  500.0  0.0  2592000  196   196  r_wrist  [species, subject_id]    False    5     91   94  0.149291  0.055118 -53.675056                   ECG,EOG,GRID,LAT,LID,LMT,LPT,LTO
2    01   5         2000-01-04T19:00:00-05:00         2000-01-04T19:00:00-05:00  43200000   94  500.0  0.0  2592000  199   199  r_wrist  [species, subject_id]    False    5     91   94  0.149291  0.055118 -53.675056                   ECG,EOG,GRID,LAT,LID,LMT,LPT,LTO
3    01   7  2000-01-07T03:31:22.414000-05:00  2000-01-07T03:31:22.414000-05:00  27858793   94  500.0  0.0  2592000  190   190  r_wrist  [species, subject_id]    False    5     91   94  0.149291  0.055118 -53.675056                   ECG,EOG,GRID,LAT,LID,LMT,LPT,LTO
4    02   3         2000-01-02T19:00:00-05:00         2000-01-02T19:00:00-05:00  43200000   86  500.0  0.0  2592000   51    51  l_wrist  [species, subject_id]    False    1     85   86  0.016180  0.031845  54.465985                                   GRID,RDA,RDP,RST
5    02   4         2000-01-03T19:00:00-05:00         2000-01-03T19:00:00-05:00  43200000   86  500.0  0.0  2592000   94    94  l_wrist  [species, subject_id]    False    1     85   86  0.016180  0.031845  54.465985                                   GRID,RDA,RDP,RST
6    02   5         2000-01-04T19:00:00-05:00         2000-01-04T19:00:00-05:00  43200000   86  500.0  0.0  2592000   82    82  l_wris
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && cat > tput.py <<'EOF'
import h5py, remfile, numpy as np, time, zlib, requests
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("000055","0.220127.0436")
    url=ds.get_asset_by_path("sub-01/sub-01_ses-4_behavior+ecephys.nwb").get_content_url(follow_redirects=1, strip_query=True)
print(url)
t0=time.time()
f=h5py.File(remfile.File(url),'r')
d=f['acquisition/ElectricalSeries/data']
print(d.chunks, d.compression, d.shuffle, d.fletcher32, d.scaleoffset)
ev=f['intervals/reaches/start_time'][:]
dsid=d.id
CH=d.chunks[0]
rows=sorted(set(int(t*500)//CH for t in ev[:60]) | set(int(t*500+1500)//CH for t in ev[:60]) | set(max(0,int(t*500-1500))//CH for t in ev[:60]))
t1=time.time()
info={}
for r in rows:
    for ch in range(d.shape[1]):
        ci=dsid.get_chunk_info_by_coord((r*CH,ch))
        info[(r,ch)]=(ci.byte_offset,ci.size)
print('index',len(info),time.time()-t1)
sizes=np.array([v[1] for v in info.values()]); print('chunk size MB',sizes.mean()/1e6)
sess=requests.Session()
adapter=requests.adapters.HTTPAdapter(pool_connections=64,pool_maxsize=64); sess.mount('https://',adapter)
def fetch(k):
    off,sz=info[k]
    b=sess.get(url,headers={'Range':f'bytes={off}-{off+sz-1}'}).content
    return k,np.frombuffer(zlib.decompress(b),dtype='<f4')
t1=time.time()
with ThreadPoolExecutor(32) as ex: out=dict(ex.map(fetch,list(info)))
dt=time.time()-t1; print('fetched',len(out),'in',dt,'MB/s',sizes.sum()/1e6/dt)
r,ch=list(info)[5]
print(np.allclose(out[(r,ch)], d[r*CH:(r+1)*CH,ch]))
EOF
python tput.py
```

```
https://dandiarchive.s3.amazonaws.com/blobs/1aa/f5a/1aaf5acb-f8b9-4479-b12d-e4ef554fc3bc
(84375, 1) gzip False False None
index 3572 69.53840112686157
chunk size MB 0.3131194633258678
fetched 3572 in 15.507222175598145 MB/s 72.12527881105558
True
Shell cwd was reset to
```

**Agent**

Direct range requests give 72 MB/s with 32 threads. Looking up chunk offsets one by one is slow (70 s for 3572), so I'll try `chunk_iter` and work out the total volume all events would need.

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && python - <<'EOF'
import pickle, numpy as np
res=pickle.load(open('meta_all.pkl','rb'))
CH=84375; tot=0; totch=0
for info,rd,el,groups,epd,_ in res:
    t=rd.start_time.values
    rows=set()
    for a in t:
        for s in (a-2.5,a+2.0):
            rows.add(int(s*500)//CH)
    tot+=len(rows); totch+=len(rows)*len(el)
print('unique rows',tot,'chunks all ch',totch,'GB',totch*0.313/1e3)
EOF
mkdir -p proj && cd proj && for i in 01 02 03 04 05 06 07 08 09 10 11 12; do :; done; curl -s "https://api.figshare.com/v2/articles/12114408" | python -c "
import json,sys
for f in json.load(sys.stdin)['files']: print(f['name'], f['download_url'], f['computed_md5'])" > files.txt; while read n u m; do curl -sL -o $n $u; done < files.txt; ls | head; head -c 600 aal_01_elecs2ROI.csv; echo; python -c "
import pandas as pd
df=pd.read_csv('aal_01_elecs2ROI.csv'); print(df.shape); print(df.columns[:10].tolist()); print(df.iloc[:3,:6])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && python - <<'EOF'
import pickle, numpy as np, pandas as pd
res=pickle.load(open('meta_all.pkl','rb'))
first={}
for info,rd,el,groups,epd,_ in res:
    first.setdefault(info['subject'],(el,info))
rois=['Precentral_L','Frontal_Mid_L','Postcentral_L','Parietal_Inf_L','SupraMarginal_L','Temporal_Sup_L','Temporal_Mid_L','Temporal_Inf_L']
dens=0
for s in sorted(first):
    el,info=first[s]
    df=pd.read_csv(f'proj/aal_{s}_elecs2ROI.csv')
    W=df.iloc[1:]
    nz=np.nonzero(df.transpose().mean().values!=0)[0][1:]
    zero_rows=[i for i in range(len(W)) if (W.iloc[i]==0).all()]
    dens=dens+df.iloc[0]
    # weighted centroid check
    xyz=el[['x','y','z']].values.copy(); xyz[:,0]=-np.abs(xyz[:,0])
    cen=pd.read_csv(f'proj/aal_{s}_ROIcentroids_Lside.csv')
    print(s,'csv rows',len(W),'nonzero rows',len(nz),'dandiset n',len(el),'zero rows idx',zero_rows[:10], 'acq',info['acq'])
print((dens/12)[rois].round(2).to_dict())
print(sorted(((dens/12)>3).pipe(lambda x:x[x]).index))
print(cen.head())
EOF
```

```
01 csv rows 98 nonzero rows 94 dandiset n 94 zero rows idx [94, 95, 96, 97] acq ['ECGL', 'ECGR', 'EOGL', 'EOGR', 'ElectricalSeries']
02 csv rows 86 nonzero rows 86 dandiset n 86 zero rows idx [] acq ['ElectricalSeries']
03 csv rows 96 nonzero rows 80 dandiset n 96 zero rows idx [80, 81, 82, 83, 84, 85, 86, 87, 88, 89] acq ['ElectricalSeries']
04 csv rows 84 nonzero rows 84 dandiset n 84 zero rows idx [] acq ['ElectricalSeries']
05 csv rows 106 nonzero rows 106 dandiset n 106 zero rows idx [] acq ['ElectricalSeries']
06 csv rows 80 nonzero rows 80 dandiset n 80 zero rows idx [] acq ['ElectricalSeries']
07 csv rows 64 nonzero rows 64 dandiset n 64 zero rows idx [] acq ['ElectricalSeries']
08 csv rows 92 nonzero rows 92 dandiset n 92 zero rows idx [] acq ['ElectricalSeries']
09 csv rows 126 nonzero rows 126 dandiset n 126 zero rows idx [] acq ['ElectricalSeries']
10 csv rows 126 nonzero rows 126 dandiset n 126 zero rows idx [] acq ['ElectricalSeries']
11 csv rows 106 nonzero rows 106 dandiset n 106 zero rows idx [] acq ['ElectricalSeries']
12 csv rows 124 nonzero rows 116 dandiset n 124 zero rows idx [72, 73, 74, 75, 76, 77, 78, 79] acq ['ElectricalSeries']
{'Precentral_L': 5.15, 'Frontal_Mid_L': 4.42, 'Postcentral_L': 8.27, 'Parietal_Inf_L': 4.14, 'SupraMarginal_L': 4.28, 'Temporal_Sup_L': 4.45, 'Temporal_Mid_L': 9.23, 'Temporal_Inf_L': 5.33}
['Frontal_Mid_L', 'Parietal_Inf_L', 'Postcentral_L', 'Precentral_L', 'SupraMarginal_L', 'Temporal_Inf_L', 'Temporal_Mid_L', 'Temporal_Sup_L']
        x       y       z
0 -39.200  -6.920  50.360
1   0.000   0.000   0.000
2 -19.448  32.793  42.172
3   0.000   0.000   0.000
4 -19.733  44.333 -13.533
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && python - <<'EOF'
import pickle, numpy as np, pandas as pd
res=pickle.load(open('meta_all.pkl','rb'))
CH=84375
rois=['Precentral_L','Frontal_Mid_L','Postcentral_L','Parietal_Inf_L','SupraMarginal_L','Temporal_Sup_L','Temporal_Mid_L','Temporal_Inf_L']
tot={0.99:0,0.95:0,'pre99':0}
for info,rd,el,groups,epd,_ in res:
    s=info['subject']
    W=pd.read_csv(f'proj/aal_{s}_elecs2ROI.csv').iloc[1:len(el)+1][rois].values
    good=el.good.values
    W=W*good[:,None]; W=W/W.sum(0)
    rows=set()
    for a in rd.start_time.values:
        for t in (a-2.5,a+2.0): rows.add(int(t*500)//CH)
    for thr in (0.99,0.95):
        keep=set()
        for j in range(8):
            o=np.argsort(-W[:,j]); c=np.cumsum(W[o,j]); keep|=set(o[:np.searchsorted(c,thr)+1])
        tot[thr]+=len(rows)*len(keep)
        if info['session']=='3' or (s=='04' and info['session']=='3'): print(s,thr,len(keep),'of',good.sum())
    o=np.argsort(-W[:,0]); c=np.cumsum(W[o,0]); k=np.searchsorted(c,0.99)+1
    tot['pre99']+=len(rows)*k
    if info['session']=='3': print(s,'precentral99',k)
print({k:(v, v*0.313/1e3) for k,v in tot.items()})
EOF
```

```
01 0.99 77 of 85
01 0.95 68 of 85
01 precentral99 23
02 0.99 76 of 85
02 0.95 70 of 85
02 precentral99 9
03 0.99 74 of 79
03 0.95 67 of 79
03 precentral99 15
04 0.99 61 of 67
04 0.95 55 of 67
04 precentral99 25
05 0.99 95 of 104
05 0.95 84 of 104
05 precentral99 17
06 0.99 52 of 70
06 0.95 44 of 70
06 precentral99 10
07 0.99 63 of 63
07 0.95 63 of 63
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && python - <<'EOF'
import pickle, numpy as np, pandas as pd
res=pickle.load(open('meta_all.pkl','rb'))
seen=set()
for info,rd,el,groups,epd,_ in res:
    s=info['subject']
    if s in seen: continue
    seen.add(s)
    g={k:(v.decode() if isinstance(v,bytes) else v) for k,v in groups.items()}
    cnt=el.group_name.value_counts().to_dict()
    print(s, {k:(g.get(k),cnt.get(k,0)) for k in g}, 'loc',el.location.unique()[:5], 'nan xyz',int(el.x.isna().sum()), 'nan R2',int(el.low_freq_R2.isna().sum()))
    if s in('03','12'): print(el[el.low_freq_R2.isna()][['x','y','z','group_name','good']].head(20).to_string())
EOF
```

```
01 {'ECG': ('electrocardiogram', 0), 'EOG': ('electrooculogram', 0), 'GRID': ('ECoG grid', 64), 'LAT': ('left anterior temporal', 6), 'LID': ('left insular depth', 8), 'LMT': ('left medial temporal', 4), 'LPT': ('left posterior temporal', 6), 'LTO': ('left temporal occipital', 6)} loc [b'unknown'] nan xyz 0 nan R2 0
02 {'GRID': ('ECoG grid', 64), 'RDA': ('right depth anterior', 8), 'RDP': ('right depth posterior', 8), 'RST': ('right temporal', 6)} loc [b'unknown'] nan xyz 0 nan R2 0
03 {'GRID': ('ECoG grid', 64), 'LAD': ('left anterior depth', 8), 'LAT': ('left anterior temporal', 8), 'LMT': ('left medial temporal', 8), 'LPD': ('left posterior depth', 8)} loc [b'unknown'] nan xyz 16 nan R2 16
     x   y   z group_name   good
80 NaN NaN NaN        LAD  False
81 NaN NaN NaN        LAD  False
82 NaN NaN NaN        LAD  False
83 NaN NaN NaN        LAD  False
84 NaN NaN NaN        LAD  False
85 NaN NaN NaN        LAD  False
86 NaN NaN NaN        LAD  False
87 NaN NaN NaN        LAD  False
88 NaN NaN NaN        LPD  False
89 NaN NaN NaN        LPD  False
90 NaN NaN NaN        LPD  False
91 NaN NaN NaN        LPD  False
92 NaN NaN NaN        LPD  False
93 NaN NaN NaN        LPD  False
94 NaN NaN NaN        LPD  False
95 NaN NaN NaN        LPD  False
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && python - <<'EOF'
import pickle, numpy as np, pandas as pd
from scipy.stats import spearmanr
res=pickle.load(open('meta_all.pkl','rb'))
rois=['Precentral_L','Frontal_Mid_L','Postcentral_L','Parietal_Inf_L','SupraMarginal_L','Temporal_Sup_L','Temporal_Mid_L','Temporal_Inf_L']
seen=set()
def score(xyz,W,cen):
    rs=[]
    for j,r in enumerate(rois):
        c=cen.loc[r].values
        d=np.linalg.norm(xyz-c,axis=1)
        ok=np.isfinite(d)&(W[:,j]>0)
        rs.append(spearmanr(-d[ok],W[ok,j])[0])
    return np.median(rs)
rng=np.random.default_rng(0)
for info,rd,el,groups,epd,_ in res:
    s=info['subject']
    if s in seen: continue
    seen.add(s)
    df=pd.read_csv(f'proj/aal_{s}_elecs2ROI.csv')
    allcols=df.columns
    cen=pd.read_csv(f'proj/aal_{s}_ROIcentroids_Lside.csv'); cen.index=allcols
    W=df.iloc[1:len(el)+1][rois].values
    xyz=el[['x','y','z']].values.copy(); xyz[:,0]=-np.abs(xyz[:,0])
    sc=score(xyz,W,cen)
    null=[score(xyz[rng.permutation(len(xyz))],W,cen) for _ in range(20)]
    print(s, round(sc,3), 'null max', round(max(null),3))
    if s=='12':
        print(list(enumerate(el.group_name))[60:124:4])
        # alternative: move dandiset rows 116-123 to 72-79
        idx=list(range(72))+list(range(116,124))+list(range(72,116))
        print('alt', round(score(xyz[idx],W,cen),3))
        # per-row diagnostics: for each csv row, which ROI gets max raw weight
EOF
```

```
01 0.952 null max 0.155
02 0.917 null max 0.124
03 0.932 null max 0.119
04 0.944 null max 0.135
05 0.932 null max 0.119
06 0.967 null max 0.169
07 0.952 null max 0.075
08 0.957 null max 0.13
09 0.939 null max 0.123
10 0.938 null max 0.101
11 0.929 null max 0.113
12 0.931 null max 0.119
[(60, 'GRID'), (64, 'LOF'), (68, 'LOF'), (72, 'AID'), (76, 'AID'), (80, 'PID'), (84, 'PID'), (88, 'LTP'), (92, 'LTP'), (96, 'LAT'), (100, 'LMT'), (104, 'LPT'), (108, 'AHD'), (112, 'AHD'), (116, 'PHD'), (120, 'PHD')]
alt 0.737
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nam/compute_power_gen_figs_python && sed -n 400,520p regression_utils.py; grep -n "def plot_feature_scattermatrix" -A40 feat_plot_utils.py | head -50; python -c "
import json;nb=json.load(open('Regression_results_Fig6.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        print(''.join(c['source'])[:3000]);
        for o in c.get('outputs',[]):
            if 'text' in o: print('OUT>', ''.join(o['text'])[:800])
        print('-----')
" | head -300
```

```
r2_test_full = clf.score(X[val_inds,...],y[val_inds,...])
                r2_test_full_pats[elec_ind,freq_i] = r2_test_full
                if model_type=='rf':
                    coefs_pats[elec_ind,:,freq_i] = 0
                else:
                    day_std = np.std(np.asarray(clf.coef_[coef_inds_keep:-3]))
                    tod_std = np.std(np.asarray(clf.coef_[-3:]))
                    coefs_np = np.asarray([clf.intercept_]+clf.coef_.tolist()[:coef_inds_keep]+[day_std]+[tod_std])
                    coefs_pats[elec_ind,:,freq_i] = coefs_np
                
                #Reduced models for change in R2
                del_r2_test_reduced,del_r2_train_reduced = [],[]
                for j in range(coef_inds_keep+2):
                    if len(np.nonzero(X[:,j])[0])>0:
                        if j<coef_inds_keep:
                            #Shuffle ind var
                            X_shuffled = X.copy()
                            X_col = X_shuffled[:,j]
                            np.random.shuffle(X_col)
                            X_shuffled[:,j] = X_col
[... 303 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && cat > ci.py <<'EOF'
import h5py, remfile, numpy as np, time, pandas as pd
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("000055","0.220127.0436")
    url=ds.get_asset_by_path("sub-01/sub-01_ses-4_behavior+ecephys.nwb").get_content_url(follow_redirects=1, strip_query=True)
t0=time.time()
f=h5py.File(remfile.File(url),'r')
d=f['acquisition/ElectricalSeries/data']
idx={}
def cb(info):
    idx[(info.chunk_offset[0]//84375, info.chunk_offset[1])]=(info.byte_offset,info.size)
d.id.chunk_iter(cb)
print('chunk_iter',len(idx),time.time()-t0)
# pose and reaches
r=f['intervals/reaches']
rd=pd.DataFrame({k:r[k][:] for k in ['start_time','stop_time','Reach_magnitude_px','Reach_angle_degrees','Onset_speed_px_per_sec','Speech_ratio','Bimanual_ratio','Bimanual_overlap','Bimanual_class']})
w=f['processing/behavior/Position/R_Wrist/data'][:]
lw=f['processing/behavior/Position/L_Wrist/data'][:]
rd['dur']=rd.stop_time-rd.start_time
print(rd.describe().T.to_string())
print('overlap>dur',(rd.Bimanual_overlap>rd.dur+1e-6).mean(), 'overlap/dur max',(rd.Bimanual_overlap/rd.dur).max())
print('nan ratio',rd.Bimanual_ratio.isna().sum())
# angle check: displacement at max radial displacement during move
rows=[]
for _,e in rd.iterrows():
    i0=int(round(e.start_time*30)); i1=int(round(e.stop_time*30))
    seg=w[i0:i1+1]-w[i0]
    rr=np.hypot(seg[:,0],seg[:,1]); k=np.nanargmax(rr)
    rows.append((np.degrees(np.arctan2(seg[k,1],seg[k,0])), rr[k], e.Reach_angle_degrees, e.Reach_magnitude_px,
                 np.nanmax(np.hypot(*(w[i0:i0+16]-w[i0]).T)), np.nanmax(np.hypot(*(w[i0-30:i0+1]-w[i0]).T))))
a=pd.DataFrame(rows,columns=['ang_img','mag','ang','magst','move_after','move_before'])
print(a.head(15).round(1).to_string())
print('corr mag',a[['mag','magst']].corr().iloc[0,1])
EOF
python ci.py
```

```
chunk_iter 48128 125.47409152984619
                        count          mean           std          min           25%           50%           75%           max
start_time              196.0  53001.262393  15221.973083  1547.936000  46087.690000  54799.218000  62264.733000  84793.565000
stop_time               196.0  53002.528209  15221.909231  1550.736000  46089.315000  54800.318000  62266.124667  84794.898333
Reach_magnitude_px      196.0    118.857442     75.309440     6.746733     63.508866    106.335410    160.987975    435.492189
Reach_angle_degrees     196.0    -27.484147    101.508137  -179.221339    -96.740556    -64.352949     58.131316    179.798287
Onset_speed_px_per_sec  196.0    146.745018    145.417261     8.370473     48.319754    102.475949    192.481651    970.659974
Speech_ratio            196.0      0.373070      0.109278     0.030339      0.296097      0.386208      0.452751      0.560355
Bimanual_ratio          196.0      0.281805      0.297469     0.000000      0.025098      0.128415      0.566006      0.993131
Bimanual_overlap        196.0      0.690136      0.733958     0.000000      0.000000      0.533333      1.075000      3.833333
Bimanual_class          196.0      0.765306      0.424893     0.000000      1.000000      1.000000      1.000000      1.000000
dur                     196.0      1.265816      0.665139     0.333333      0.766667      1.116667      1.600000      3.933333
overlap>dur 0.0 overlap/dur max 1.0000000000056175
nan ratio 0
    ang_img    mag    ang  magst  move_after  move_before
0     166.2  228.5  162.3  230.8       187.8          5.8
1      71.1   44.2   69.8   43.9        14.7          3.9
2     -93.5   81.7  -94.5   82.1        13.0          6.0
3      15.2  109.6    8.2  100.1       109.6          1.5
4     -64.0   76.1  -64.6   75.7        21.0          3.1
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && python -c "import remfile,inspect;print(inspect.signature(remfile.File.__init__))"; cat > ci2.py <<'EOF'
import h5py, remfile, numpy as np, time, sys
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("000055","0.220127.0436")
    url=ds.get_asset_by_path("sub-01/sub-01_ses-5_behavior+ecephys.nwb").get_content_url(follow_redirects=1, strip_query=True)
for mcs in [int(sys.argv[1])]:
    t0=time.time()
    rf=remfile.File(url, _min_chunk_size=mcs) if mcs else remfile.File(url)
    f=h5py.File(rf,'r')
    d=f['acquisition/ElectricalSeries/data']
    offs=[]
    d.id.chunk_iter(lambda i: offs.append((i.chunk_offset, i.byte_offset, i.size)))
    print(mcs,'chunk_iter',len(offs),time.time()-t0)
    o=np.array([x[1] for x in offs]); 
    print('first offsets', [(x[0],x[1]) for x in offs[:3]], [(x[0],x[1]) for x in offs[94:97]])
EOF
python ci2.py 1000000
```

```
(self, url: Union[str, Any], *, verbose: bool = False, disk_cache: Optional[remfile.DiskCache.DiskCache] = None, _min_chunk_size: int = 102400, _max_cache_size: int = 1000000000.0, _chunk_increment_factor: int = 1.7, _bytes_per_thread: int = 4194304, _max_threads: int = 1, _max_chunk_size: int = 104857600, _impose_request_failures_for_testing: bool = False, _size: Optional[int] = None, _use_session: bool = True)
1000000 chunk_iter 48128 139.57469940185547
first offsets [((0, 0), 691221376), ((0, 1), 691534605), ((0, 2), 691847810)] [((84375, 0), 720685835), ((84375, 1), 720998780), ((84375, 2), 721311757)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . expl/bin/activate && python - <<'EOF'
import pickle, numpy as np, pandas as pd
res=pickle.load(open('meta_all.pkl','rb'))
CH=84375
rois=['Precentral_L','Frontal_Mid_L','Postcentral_L','Parietal_Inf_L','SupraMarginal_L','Temporal_Sup_L','Temporal_Mid_L','Temporal_Inf_L']
first={}
for info,rd,el,groups,epd,_ in res:
    first.setdefault(info['subject'], el.good.values)
def need(times, nch):
    d={}
    for a in times:
        s0=int(round((a-2.0)*500)); s1=int(round((a+2.0)*500))
        for r in range(s0//CH, s1//CH+1):
            end=min(s1, (r+1)*CH-1)-r*CH
            d[r]=max(d.get(r,0), end+1)
    return sum(v*4*0.93 for v in d.values())*nch, len(d)
rng=np.random.default_rng(0)
for thr in (0.9,0.95,0.99):
    totP=0; rowsP=0
    for info,rd,el,groups,epd,_ in res:
        s=info['subject']; good=first[s]
        W=pd.read_csv(f'proj/aal_{s}_elecs2ROI.csv').iloc[1:len(el)+1]['Precentral_L'].values*good
        W=W/W.sum(); o=np.argsort(-W); k=np.searchsorted(np.cumsum(W[o]),thr)+1
        b,nr=need(rd.start_time.values,k); totP+=b; rowsP+=nr
    print('P',thr,round(totP/1e9,1),'GB rows',rowsP)
totA=0
for info,rd,el,groups,epd,_ in res:
    s=info['subject']; good=first[s]
    W=pd.read_csv(f'proj/aal_{s}_elecs2ROI.csv').iloc[1:len(el)+1][rois].values*good[:,None]
    W=W/W.sum(0); keep=set()
    for j in range(8):
        o=np.argsort(-W[:,j]); keep|=set(o[:np.searchsorted(np.cumsum(W[o,j]),0.99)+1])
    n=min(len(rd),5)
    b,_=need(rng.choice(rd.start_time.values,n,replace=False),len(keep)); totA+=b
print('A 5/session',round(totA/1e9,1))
EOF
```

```
P 0.9 13.5 GB rows 4980
P 0.95 16.1 GB rows 4980
P 0.99 22.4 GB rows 4980
A 5/session 3.7
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/entry.py && grep -n "def \|python_version\|--python\|timeout\|EMBED\|max_\|literal" tools/entry.py | head -80
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
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
- each notebook, or a helper it imports, names the dandiset the entry uses;
- each notebook has a cell tagged `sanity` that prints what was loaded;
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/000055-peterson-2021; cat attempts/001453-fouke-2025-01.yaml | head -5 >/dev/null; sed -n 1,60p schemas/attempt.schema.json | head -80; grep -n '"enum"' -A12 schemas/attempt.schema.json | head -60
```

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "One attempt at reproducing the claims of a target",
  "description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "id",
    "dandiset",
    "paper",
    "date",
    "provenance",
    "outcomes"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "id": {
[... 100 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "content": "\"\"\"Loading and measures for AJILE12, dandiset 000055, as used by Peterson, Singh et al. (2021).\n\nPeterson SM, Singh SH, Wang NXR, Rao RPN, Brunton BW (2021). Behavioral and neural variability\nof naturalistic arm movements. eNeuro 8(3), doi:10.1523/ENEURO.0007-21.2021.\n\nEach NWB file holds one subject and one recording day: ECoG at 500 Hz (`ElectricalSeries`, data\ntimes 1e-6 volts), pose of nine keypoints at 30 Hz (in pixels, though the files say meters),\ncoarse behavioural labels (`epochs`), and the wrist movement events with their features\n(`intervals/reaches`). Files are streamed from the archive at the pinned version; nothing is\nwritten to disk.\n\nECoG is stored in gzip chunks of 84375 samples x 1 channel. A window around an event costs one\nchunk per channel, so `fetch_windows` reads, for each chunk it needs, only the compressed bytes\nup to the end of the window (gzip streams decompress from the start), with HTTP range requests\nin parallel threads.\n\nWhere the parameters come from:\n\n- From the paper's Methods: LFB 8 to 32 Hz and HFB 76 to 100 Hz; power over the first 0.5 s after\n  movement onset; baseline 1.5 to 1 s before onset; Morlet wavelets; the eight AAL regions;\n  time of day in three 8 h bins from midnight; reach angle folded to -90 (down) to 90 (up).\n- From the paper's code (github.com/BruntonUWBio/naturalistic_arm_movements_ecog, commit\n  04c6faf2f219586fa834d10c614ef48a694cec55, `config.py`, `tfr_utils.py`, `regression_utils.py`,\n  `Plot_banded_power_Fig5.ipynb`), where the Methods leave them open: frequencies 1 to 121 Hz in\n  5 Hz steps with n_cycles = f / 4 (MNE `tfr_morlet`), power in dB, decimation by 50 (10 Hz time\n  bins); baseline as the mean over its bins, subtracted per event, frequency and channel; band\n  power as the median over the bins from 0 to 0.5 s and then over the band's frequencies; the\n  projection of baseline-subtracted electrode power onto regions with the paper's projection\n  matrices, with the weights of bad electrodes set to 0 and renormalised (bad electrodes are\n  those of the subject's first file, as the code takes them); the folding of the reach angle\n  (negate, then fold); NaN bimanual ratios set to 0.5; features in seconds, px and px/s.\n- The projection matrices (electrode to AAL region weights) are the paper's, from Figshare,\n  doi:10.6084/m9.figshare.12114408.v1; they are not in the dandiset.\n- Common choices here: the window read around each event (-2 to 2 s; the wavelets are at most\n  0.4 s long, as n_cycles = f / 4 gives a Gaussian of SD 1/(8 pi) s at every frequency).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport multiprocessing as mp\nimport zlib\nfrom concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy.signal import fftconvolve\n\nDANDISET_ID = \"000055\"\nDANDISET_VERSION = \"0.220127.0436\"\n\nFS = 500.0                 # ECoG sampling rate, Hz (stated in the files; checked in the notebook)\nFS_VIDEO = 30.0            # pose rate, Hz\nCHUNK = 84375              # ECoG samples per stored chunk\nFREQS = np.arange(1, 124, 5).astype(float)   # code: config.constants_compute_tfr['freqs']\nN_CYCLES = FREQS / 4.0                        # code: tfr_utils.compute_tfr\nDECIM = 50                                     # code: config, 10 Hz time bins\nTIMES = np.round(np.arange(-15, 16) / 10.0, 1)  # TFR bins kept, -1.5 to 1.5 s\nBASELINE = (-1.5, -1.0)\nT_AVE = (0.0, 0.5)\nLFB = (8, 32)\nHFB = (76, 100)\nWINDOW = (-2.0, 2.0)       # seconds of ECoG read around each event\n\nROIS = [\"Precentral_L\", \"Frontal_Mid_L\", \"Postcentral_L\", \"Parietal_Inf_L\", \"SupraMarginal_L\",\n        \"Temporal_Sup_L\", \"Temporal_Mid_L\", \"Temporal_Inf_L\"]\nROI_NAMES = {\"Precentral_L\": \"precentral\", \"Frontal_Mid_L\": \"middle frontal\",\n             \"Postcentral_L\": \"postcentral\", \"Parietal_Inf_L\": \"inferior parietal\",\n             \"SupraMarginal_L\": \"supramarginal\", \"Temporal_Sup_L\": \"superior temporal\",\n             \"Temporal_Mid_L\": \"middle temporal\", \"Temporal_Inf_L\": \"inferior temporal\"}\nFIGSHARE_ARTICLE = 12114408   # \"ROI projection matrices and labels\", version 1\nFIGSHARE_DOI = \"10.6084/m9.figshare.12114408.v1\"\n\nREACH_COLUMNS = [\"start_time\", \"stop_time\", \"Reach_magnitude_px\", \"Reach_angle_degrees\",\n                 \"Onset_speed_px_per_sec\", \"Speech_ratio\", \"Bimanual_ratio\", \"Bimanual_overlap\",\n                 \"Bimanual_class\"]\nFEATURES = [\"day\", \"time_of_day\", \"duration\", \"magnitude\", \"angle\", \"onset_speed\", \"speech_ratio\",\n            \"bimanual_ratio\", \"bimanual_overlap\", \"bimanual_class\"]\n\n\ndef asset_urls() -> list[tuple[str, str]]:\n    \"\"\"(path, streaming URL) of every NWB file at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))\n                      for a in dandiset.get_assets() if a.path.endswith(\".nwb\"))\n\n\ndef dandiset_metadata() -> dict:\n    with DandiAPIClient() as client:\n        return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_raw_metadata()\n\n\ndef _text(value) -> str:\n    value = value[()] if hasattr(value, \"shape\") else value\n    return value.decode() if isinstance(value, bytes) else str(value)\n\n\ndef _strings(values) -> list[str]:\n    return [v.decode() if isinstance(v, bytes) else str(v) for v in values]\n\n\ndef load_session(path_url: tuple[str, str]) -> dict:\n    \"\"\"Everything but the ECoG and pose samples of one file.\"\"\"\n    path, url = path_url\n    with h5py.File(remfile.File(url), \"r\") as f:\n        ecog = f[\"acquisition/ElectricalSeries\"]\n        el = f[\"general/extracellular_ephys/electrodes\"]\n        electrodes = pd.DataFrame({k: el[k][:] for k in [\"x\", \"y\", \"z\", \"imp\", \"good\", \"low_freq_R2\",\n                                                         \"high_freq_R2\", \"standard_deviation\",\n                                                         \"kurtosis\", \"median_deviation\"]})\n        electrodes[\"location\"] = _strings(el[\"location\"][:])\n        electrodes[\"group_name\"] = _strings(el[\"group_name\"][:])\n        groups = {g: _text(f[\"general/extracellular_ephys\"][g].attrs[\"description\"])\n                  for g in f[\"general/extracellular_ephys\"] if g != \"electrodes\"}\n        r = f[\"intervals/reaches\"]\n        reaches = pd.DataFrame({k: r[k][:] for k in REACH_COLUMNS})\n        ep = f[\"intervals/epochs\"]\n        epochs = pd.DataFrame({\"start\": ep[\"start_time\"][:], \"stop\": ep[\"stop_time\"][:],\n                               \"label\": _strings(ep[\"labels\"][:])})\n        pose = f[\"processing/behavior/Position\"]\n        session = {\n            \"path\": path, \"url\": url,\n            \"subject\": _text(f[\"general/subject/subject_id\"]),\n            \"species\": _text(f[\"general/subject/species\"]),\n            \"subject_fields\": sorted(f[\"general/subject\"].keys()),\n            \"day\": int(_text(f[\"general/session_id\"])),\n            \"session_start\": _text(f[\"session_start_time\"]),\n            \"ecog_shape\": ecog[\"data\"].shape,\n            \"ecog_chunks\": ecog[\"data\"].chunks,\n            \"ecog_rate\": float(ecog[\"starting_time\"].attrs[\"rate\"]),\n            \"ecog_start\": float(ecog[\"starting_time\"][()]),\n            \"ecog_unit\": _text(ecog[\"data\"].attrs[\"unit\"]),\n            \"ecog_conversion\": float(ecog[\"data\"].attrs[\"conversion\"]),\n            \"ecog_electrodes\": ecog[\"electrodes\"][:],\n            \"acquisition\": {k: _text(f[\"acquisition\"][k].attrs.get(\"description\", \"\"))\n                            for k in f[\"acquisition\"]},\n            \"pose_keys\": sorted(pose.keys()),\n            \"pose_n\": pose[\"R_Wrist/data\"].shape[0],\n            \"pose_rate\": float(pose[\"R_Wrist/starting_time\"].attrs[\"rate\"]),\n            \"pose_unit\": _text(pose[\"R_Wrist/data\"].attrs[\"unit\"]),\n            \"pose_conversion\": float(pose[\"R_Wrist/data\"].attrs[\"conversion\"]),\n            \"event_wrist\": _text(f[\"processing/behavior/ReachEvents\"].attrs[\"description\"]),\n            \"event_times\": f[\"processing/behavior/ReachEvents/timestamps\"][:],\n            \"reach_descriptions\": {k: _text(r[k].attrs.get(\"description\", \"\")) for k in REACH_COLUMNS},\n            \"electrodes\": electrodes, \"groups\": groups, \"reaches\": reaches, \"epochs\": epochs,\n        }\n    session[\"hemisphere\"] = \"R\" if np.nanmean(electrodes.x) > 0 else \"L\"\n    return session\n\n\ndef _pool(workers: int) -> ProcessPoolExecutor:\n    return ProcessPoolExecutor(workers, mp_context=mp.get_context(\"spawn\"))\n\n\ndef load_all(workers: int = 12) -> list[dict]:\n    \"\"\"Every file's tables, ordered by subject and day.\"\"\"\n    with _pool(workers) as ex:\n        sessions = list(ex.map(load_session, asset_urls()))\n    return sorted(sessions, key=lambda s: (s[\"subject\"], s[\"day\"]))\n\n\ndef fold_angle(angle_deg):\n    \"\"\"The code's folding (regression_utils, feat_plot_utils): negate the image-coordinate angle so\n    that up is positive, then fold 90 to 270 degrees onto 90 to -90.\"\"\"\n    a = -np.asarray(angle_deg, dtype=float)\n    a = np.where(a <= 90, a, 180 - a)\n    return np.where(a >= -90, a, -180 - a)\n\n\ndef reach_features(sessions: list[dict]) -> pd.DataFrame:\n    \"\"\"The paper's ten features for every event, with subject, day and event time.\n\n    Time of day is the event's clock time from the file's session_start_time, in hours.\n    Duration is stop_time - start_time. Bimanual overlap is kept as stored (seconds; see the\n    notebook's data check).\"\"\"\n    rows = []\n    for s in sessions:\n        r = s[\"reaches\"]\n        start = pd.Timestamp(s[\"session_start\"])\n        clock = (start.hour + start.minute / 60 + start.second / 3600 + r.start_time / 3600) % 24\n        rows.append(pd.DataFrame({\n            \"subject\": s[\"subject\"], \"day\": s[\"day\"], \"event\": np.arange(len(r)),\n            \"t\": r.start_time, \"time_of_day\": clock, \"duration\": r.stop_time - r.start_time,\n            \"magnitude\": r.Reach_magnitude_px, \"angle\": fold_angle(r.Reach_angle_degrees),\n            \"angle_stored\": r.Reach_angle_degrees, \"onset_speed\": r.Onset_speed_px_per_sec,\n            \"speech_ratio\": r.Speech_ratio, \"bimanual_ratio\": r.Bimanual_ratio.fillna(0.5),\n            \"bimanual_ratio_nan\": r.Bimanual_ratio.isna(),\n            \"bimanual_overlap\": r.Bimanual_overlap, \"bimanual_class\": r.Bimanual_class}))\n    return pd.concat(rows, ignore_index=True)\n\n\ndef pose_windows(path_url: tuple[str, str], times: np.ndarray, keypoint: str,\n                 before: float = 1.5, after: float = 3.0) -> np.ndarray:\n    \"\"\"x, y of one keypoint (pixels) from `before` s before to `after` s after each time;\n    events x frames x 2.\"\"\"\n    path, url = path_url\n    n0, n1 = int(round(before * FS_VIDEO)), int(round(after * FS_VIDEO))\n    with h5py.File(remfile.File(url), \"r\") as f:\n        data = f[f\"processing/behavior/Position/{keypoint}/data\"]\n        idx = np.round(np.asarray(times) * FS_VIDEO).astype(int)\n        lo, hi = max(idx.min() - n0, 0), min(idx.max() + n1 + 1, data.shape[0])\n        block = data[lo:hi]\n    out = np.full((len(idx), n0 + n1 + 1, 2), np.nan)\n    for k, i in enumerate(idx):\n        a, b = i - n0 - lo, i + n1 + 1 - lo\n        if a >= 0 and b <= len(block):\n            out[k] = block[a:b]\n    return out\n\n\n# ---------------------------------------------------------------- projection weights (Figshare)\n\ndef projection_matrices() -> dict[str, pd.DataFrame]:\n    \"\"\"The paper's electrode-to-AAL weights per subject, read into memory from Figshare.\n\n    Row 0 is the electrode density of each region; the other rows are the electrodes, each region's\n    column normalised to sum to 1 (project_ecog_to_rois.m).\"\"\"\n    meta = requests.get(f\"https://api.figshare.com/v2/articles/{FIGSHARE_ARTICLE}/versions/1\",\n                        timeout=60)\n    meta.raise_for_status()\n    out = {}\n    for item in meta.json()[\"files\"]:\n        name = item[\"name\"]\n        if name.endswith(\"_elecs2ROI.csv\"):\n            r = requests.get(item[\"download_url\"], timeout=120)\n            r.raise_for_status()\n            out[name.split(\"_\")[1]] = pd.read_csv(io.BytesIO(r.content))\n    return out\n\n\ndef roi_weights(matrix: pd.DataFrame, n_electrodes: int, good: np.ndarray,\n                rois: list[str] = ROIS) -> np.ndarray:\n    \"\"\"electrodes x regions weights, with bad electrodes set to 0 and each region renormalised\n    (tfr_utils.load_project_spectral_power with rem_bad_chans=True).\"\"\"\n    w = matrix.iloc[1:n_electrodes + 1][rois].to_numpy(float) * np.asarray(good, float)[:, None]\n    return w / w.sum(axis=0, keepdims=True)\n\n\ndef covering(weights: np.ndarray, fraction: float) -> np.ndarray:\n    \"\"\"Indices of the fewest electrodes whose weights sum to `fraction` of each region's weight.\"\"\"\n    keep = set()\n    for j in range(weights.shape[1]):\n        order = np.argsort(-weights[:, j])\n        n = int(np.searchsorted(np.cumsum(weights[order, j]), fraction) + 1)\n        keep |= set(order[:n].tolist())\n    return np.array(sorted(keep))\n\n\n# ---------------------------------------------------------------- ECoG windows\n\ndef _morlet_bank():\n    \"\"\"MNE's morlet(): Gaussian of SD n_cycles / (2 pi f), cut at 5 SD, normalised.\"\"\"\n    bank = []\n    for f, n in zip(FREQS, N_CYCLES):\n        sigma = n / (2 * np.pi * f)\n        t = np.arange(0, 5 * sigma, 1 / FS)\n        t = np.r_[-t[::-1], t[1:]]\n        w = np.exp(2j * np.pi * f * t) * np.exp(-t ** 2 / (2 * sigma ** 2))\n        bank.append(w / (np.sqrt(0.5) * np.linalg.norm(w)))\n    return bank\n\n\n_BANK = _morlet_bank()\n\n\ndef log_power(x: np.ndarray) -> np.ndarray:\n    \"\"\"dB power of windows (..., samples) at FREQS and TIMES: (..., freqs, times).\"\"\"\n    n0 = int(round(-WINDOW[0] * FS))\n    idx = n0 + np.round(TIMES * FS).astype(int)\n    out = np.empty(x.shape[:-1] + (len(FREQS), len(TIMES)))\n    for k, w in enumerate(_BANK):\n        c = fftconvolve(x, w.reshape((1,) * (x.ndim - 1) + (-1,)), mode=\"same\", axes=-1)\n        out[..., k, :] = np.abs(c[..., idx]) ** 2\n    with np.errstate(divide=\"ignore\"):\n        out = 10 * np.log10(out)\n    out[np.isinf(out)] = 0    # tfr_utils.compute_tfr sets infinite values to 0\n    return out\n\n\ndef subtract_baseline(p: np.ndarray) -> np.ndarray:\n    base = (TIMES >= BASELINE[0]) & (TIMES <= BASELINE[1])\n    return p - p[..., base].mean(axis=-1, keepdims=True)\n\n\ndef band_values(p: np.ndarray) -> np.ndarray:\n    \"\"\"(..., freqs, times) -> (..., 2): median over 0 to 0.5 s, then over LFB and HFB frequencies.\"\"\"\n    t = (TIMES >= T_AVE[0]) & (TIMES <= T_AVE[1])\n    m = np.median(p[..., t], axis=-1)\n    lo = (FREQS >= LFB[0]) & (FREQS <= LFB[1])\n    hi = (FREQS >= HFB[0]) & (FREQS <= HFB[1])\n    return np.stack([np.median(m[..., lo], axis=-1), np.median(m[..., hi], axis=-1)], axis=-1)\n\n\ndef fetch_windows(url: str, n_samples: int, times: np.ndarray, channels: np.ndarray,\n                  threads: int = 24) -> np.ndarray:\n    \"\"\"ECoG in microvolts around each time: events x channels x samples (WINDOW, at FS).\n\n    Windows that run past the recording are NaN.\"\"\"\n    n0, n1 = int(round(-WINDOW[0] * FS)), int(round(WINDOW[1] * FS))\n    starts = np.round(np.asarray(times) * FS).astype(int) - n0\n    length = n0 + n1\n    need = {}                                  # chunk row -> samples needed from its start\n    for s in starts:\n        if s < 0 or s + length > n_samples:\n            continue\n        for row in range(s // CHUNK, (s + length - 1) // CHUNK + 1):\n            need[row] = max(need.get(row, 0), min(s + length, (row + 1) * CHUNK) - row * CHUNK)\n    with h5py.File(remfile.File(url), \"r\") as f:\n        dsid = f[\"acquisition/ElectricalSeries/data\"].id\n        info = {(row, ch): dsid.get_chunk_info_by_coord((row * CHUNK, int(ch)))\n                for row in sorted(need) for ch in channels}\n    session = requests.Session()\n    session.mount(\"https://\", requests.adapters.HTTPAdapter(pool_connections=threads,\n                                                            pool_maxsize=threads))\n\n    def get(key):\n        row, ch = key\n        ci = info[key]\n        want = need[row] * 4\n        # gzip of these float32 samples barely compresses; ask for the bytes the samples need\n        # plus a margin, and fetch the rest of the chunk if that was not enough.\n        n_bytes = min(ci.size, int(want * 1.02) + 65536)\n        for attempt in range(2):\n            r = session.get(url, headers={\"Range\": f\"bytes={ci.byte_offset}-{ci.byte_offset + n_bytes - 1}\"},\n                            timeout=120)\n            r.raise_for_status()\n            raw = zlib.decompressobj().decompress(r.content)\n            if len(raw) >= want or n_bytes == ci.size:\n                break\n            n_bytes = ci.size\n        if len(raw) < want:\n            raise OSError(f\"chunk {key} decompressed to {len(raw)} bytes, {want} needed\")\n        return key, np.frombuffer(raw[:want], dtype=\"<f4\")\n\n    with ThreadPoolExecutor(threads) as ex:\n        chunks = dict(ex.map(get, list(info)))\n    out = np.full((len(starts), len(channels), length), np.nan, dtype=np.float32)\n    for k, s in enumerate(starts):\n        if s < 0 or s + length > n_samples:\n            continue\n        for j, ch in enumerate(channels):\n            parts = []\n            for row in range(s // CHUNK, (s + length - 1) // CHUNK + 1):\n                a = max(s, row * CHUNK) - row * CHUNK\n                b = min(s + length, (row + 1) * CHUNK) - row * CHUNK\n                parts.append(chunks[(row, ch)][a:b])\n            out[k, j] = np.concatenate(parts)\n    return out\n\n\ndef session_power(task: dict) -> dict:\n    \"\"\"For one file: fetch the windows of the requested events and channels and return\n\n    - `bands`: events x channels x 2, baseline-subtracted LFB and HFB power (dB);\n    - `bands_raw`: the same without baseline subtraction;\n    - `roi_tfr`: events x regions x freqs x times, baseline-subtracted power projected with\n      `task['weights']` (channels x regions, rows in the order of `task['channels']`);\n    - `roi_tfr_raw`: the same, projected before baseline subtraction;\n    - `hf_noise`: events, mean dB power at 116 and 121 Hz over channels and times;\n    - `bad_window`: events, True where the window has NaN or is outside the recording, or where a\n      channel is flat (all zeros; the preprocessing set artefacts to 0).\n    \"\"\"\n    x = fetch_windows(task[\"url\"], task[\"n_samples\"], task[\"times\"], task[\"channels\"])\n    bad = np.isnan(x).any(axis=(1, 2)) | (np.abs(x).max(axis=2) == 0).any(axis=1)\n    x = np.nan_to_num(x).astype(float)\n    p = log_power(x)                                    # events x channels x freqs x times\n    pb = subtract_baseline(p)\n    w = np.asarray(task[\"weights\"])\n    hf = (FREQS >= 115) & (FREQS <= 125)\n    return {\n        \"bands\": band_values(pb), \"bands_raw\": band_values(p),\n        \"roi_tfr\": np.einsum(\"ecft,cr->erft\", pb, w).astype(np.float32),\n        \"roi_tfr_raw\": np.einsum(\"ecft,cr->erft\", p, w).astype(np.float32),\n        \"hf_noise\": p[:, :, hf, :].mean(axis=(1, 2, 3)),\n        \"bad_window\": bad,\n    }\n\n\ndef run_power(tasks: list[dict], workers: int = 12) -> list[dict]:\n    with _pool(workers) as ex:\n        return list(ex.map(session_power, tasks))\n"
}
```

```
File created successfully at: entries/000055-peterson-2021/ajile.py (file state is current in your context — no need to Read it back)
```

**Agent**

Testing the pipeline on three files, to time it:

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && . $TMPDIR/expl/bin/activate && cat > $TMPDIR/t1.py <<'EOF'
import time, numpy as np, sys
sys.path.insert(0,'.')
import ajile
if __name__=='__main__':
    t0=time.time()
    sessions=ajile.load_all()
    print('meta',time.time()-t0)
    P=ajile.projection_matrices(); print('proj',time.time()-t0, sorted(P))
    first_good={}
    for s in sessions: first_good.setdefault(s['subject'], s['electrodes'].good.values)
    tasks=[]
    for s in sessions[:3]:
        n=len(s['electrodes'])
        w=ajile.roi_weights(P[s['subject']], n, first_good[s['subject']])
        ch=ajile.covering(w[:,:1],0.95)
        wp=w[ch,:1]/w[ch,:1].sum(0)
        tasks.append(dict(url=s['url'],n_samples=s['ecog_shape'][0],times=s['reaches'].start_time.values,channels=ch,weights=wp))
        print(s['path'],len(ch),len(s['reaches']))
    t1=time.time()
    out=ajile.run_power(tasks,workers=3)
    print('power',time.time()-t1)
    for o in out:
        print(o['bands'].shape, np.median(o['bands'],axis=(0,1)), o['bad_window'].sum(), np.median(ajile.band_values(o['roi_tfr'])[:,0,:],axis=0))
EOF
python $TMPDIR/t1.py
```

```
meta 25.318729162216187
proj 40.70561361312866 ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
sub-01/sub-01_ses-3_behavior+ecephys.nwb 16 156
sub-01/sub-01_ses-4_behavior+ecephys.nwb 16 196
sub-01/sub-01_ses-5_behavior+ecephys.nwb 16 199
power 139.1700839996338
(156, 16, 2) [-0.13824014  0.70931437] 1 [-1.3083386  -0.00800284]
(196, 16, 2) [-0.41143046  0.78820615] 1 [-1.6620541   0.12119055]
(199, 16, 2) [-0.46536979  0.8908792 ] 1 [-1.7196577   0.22896574]
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && cat > $TMPDIR/t2.py <<'EOF'
import time, numpy as np, h5py, remfile, sys
sys.path.insert(0,'.')
import ajile
urls=dict(ajile.asset_urls())
url=urls['sub-01/sub-01_ses-4_behavior+ecephys.nwb']
f=h5py.File(remfile.File(url),'r')
d=f['acquisition/ElectricalSeries/data']; ev=f['intervals/reaches/start_time'][:]
rows=sorted(set(int((t-2)*500)//84375 for t in ev)|set(int((t+2)*500)//84375 for t in ev))
print(len(rows))
t0=time.time()
for r in rows[:40]:
    for ch in range(16): d.id.get_chunk_info_by_coord((r*84375,ch))
print('16ch x 40 rows',time.time()-t0)
t0=time.time()
for r in rows[40:80]:
    d.id.get_chunk_info_by_coord((r*84375,0))
print('1ch x 40 rows',time.time()-t0)
EOF
python $TMPDIR/t2.py
```

```
117
16ch x 40 rows 67.95824813842773
1ch x 40 rows 15.17003607749939
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && cat > $TMPDIR/t3.py <<'EOF'
import time, numpy as np, h5py, remfile, sys, struct, requests
sys.path.insert(0,'.')
import ajile
urls=dict(ajile.asset_urls())
url=urls['sub-01/sub-01_ses-4_behavior+ecephys.nwb']
f=h5py.File(remfile.File(url),'r')
d=f['acquisition/ElectricalSeries/data']
try:
    print('h5o addr', h5py.h5o.get_info(d.id).addr)
except Exception as e: print('h5o err',e)
oi=h5py.h5g.get_objinfo(f['acquisition/ElectricalSeries'].id, b'data'); print('objno',oi.objno)
addr=oi.objno[0]
hdr=requests.get(url,headers={'Range':f'bytes={addr}-{addr+4095}'}).content
print(hdr[:16])
EOF
python $TMPDIR/t3.py
```

```
h5o addr 691217920
objno (691217920, 0)
b'\x01\x00\x0c\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00'
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && cat > $TMPDIR/t4.py <<'EOF'
import time, numpy as np, h5py, remfile, sys, struct, requests
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,'.')
import ajile
urls=dict(ajile.asset_urls())
url=urls['sub-01/sub-01_ses-4_behavior+ecephys.nwb']
S=requests.Session()
def rng(a,n): 
    r=S.get(url,headers={'Range':f'bytes={a}-{a+n-1}'}); r.raise_for_status(); return r.content
f=h5py.File(remfile.File(url),'r')
d=f['acquisition/ElectricalSeries/data']
addr=h5py.h5o.get_info(d.id).addr
t0=time.time()
def messages(block, start, end):
    p=start
    while p+8<=end:
        typ,size,flags=struct.unpack_from('<HHB',block,p)
        yield typ, block[p+8:p+8+size]
        p+=8+size
hdr=rng(addr,4096)
nmsg,=struct.unpack_from('<H',hdr,2); hsize,=struct.unpack_from('<I',hdr,8)
queue=[(hdr,16,16+hsize)]; layout=None
while queue:
    blk,a,b=queue.pop()
    for typ,data in messages(blk,a,b):
        if typ==0x10:
            off,ln=struct.unpack_from('<QQ',data,0); queue.append((rng(off,ln),0,ln))
        if typ==8: layout=data
print('layout',layout[:40], len(layout))
ver,cls=layout[0],layout[1]
ndim=layout[2]; broot,=struct.unpack_from('<Q',layout,3)
dims=struct.unpack_from('<'+'I'*ndim,layout,11)
print(ver,cls,ndim,broot,dims)
keysize=8+8*ndim
def parse(node):
    assert node[:4]==b'TREE',node[:4]
    typ,level,used=struct.unpack_from('<BBH',node,4)
    p=24; out=[]
    for i in range(used):
        csize,mask=struct.unpack_from('<II',node,p); offs=struct.unpack_from('<'+'Q'*ndim,node,p+8)
        child,=struct.unpack_from('<Q',node,p+keysize)
        out.append((offs,csize,child)); p+=keysize+8
    return level,out
NODE=24+65*keysize+64*8+1024
level,ents=parse(rng(broot,NODE))
print('root level',level,len(ents))
while level>0:
    with ThreadPoolExecutor(32) as ex: nodes=list(ex.map(lambda e: parse(rng(e[2],NODE)), ents))
    level=nodes[0][0]; ents=[e for n in nodes for e in n[1]]
print('leaves entries',len(ents),time.time()-t0)
idx={(e[0][0]//84375,e[0][1]):(e[2],e[1]) for e in ents}
for k in [(0,0),(5,7),(300,93)]:
    ci=d.id.get_chunk_info_by_coord((k[0]*84375,k[1])); print(k, idx[k], (ci.byte_offset,ci.size))
EOF
python $TMPDIR/t4.py
```

```
layout b'\x03\x02\x03H)3)\x00\x00\x00\x00\x97I\x01\x00\x01\x00\x00\x00\x04\x00\x00\x00\x00' 24
3 2 3 691218760 (84375, 1, 4)
root level 2 15
leaves entries 48128 5.2767345905303955
(0, 0) (691221376, 313670) (691221376, 313670)
(5, 7) (840657805, 313611) (840657805, 313611)
(300, 93) (9520343622, 313776) (9520343622, 313776)
```

**Agent**

Parsing the B-tree directly gives the full index in 5.3 s, and the offsets match h5py's. Adding it to the helper:

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "old_string": "    with h5py.File(remfile.File(url), \"r\") as f:\n        dsid = f[\"acquisition/ElectricalSeries/data\"].id\n        info = {(row, ch): dsid.get_chunk_info_by_coord((row * CHUNK, int(ch)))\n                for row in sorted(need) for ch in channels}\n    session = requests.Session()\n    session.mount(\"https://\", requests.adapters.HTTPAdapter(pool_connections=threads,\n                                                            pool_maxsize=threads))\n\n    def get(key):\n        row, ch = key\n        ci = info[key]\n        want = need[row] * 4\n        # gzip of these float32 samples barely compresses; ask for the bytes the samples need\n        # plus a margin, and fetch the rest of the chunk if that was not enough.\n        n_bytes = min(ci.size, int(want * 1.02) + 65536)\n        for attempt in range(2):\n            r = session.get(url, headers={\"Range\": f\"bytes={ci.byte_offset}-{ci.byte_offset + n_bytes - 1}\"},\n                            timeout=120)\n            r.raise_for_status()\n            raw = zlib.decompressobj().decompress(r.content)\n            if len(raw) >= want or n_bytes == ci.size:\n                break\n            n_bytes = ci.size",
 "new_string": "    session = requests.Session()\n    session.mount(\"https://\", requests.adapters.HTTPAdapter(pool_connections=threads,\n                                                            pool_maxsize=threads))\n    index = chunk_index(url, session, threads)\n\n    def get(key):\n        row, ch = key\n        offset, size = index[key]\n        want = need[row] * 4\n        # gzip of these float32 samples barely compresses; ask for the bytes the samples need\n        # plus a margin, and fetch the rest of the chunk if that was not enough.\n        n_bytes = min(size, int(want * 1.02) + 65536)\n        for attempt in range(2):\n            r = session.get(url, headers={\"Range\": f\"bytes={offset}-{offset + n_bytes - 1}\"},\n                            timeout=120)\n            r.raise_for_status()\n            raw = zlib.decompressobj().decompress(r.content)\n            if len(raw) >= want or n_bytes == size:\n                break\n            n_bytes = size"
}
```

```
The file entries/000055-peterson-2021/ajile.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "old_string": "    with ThreadPoolExecutor(threads) as ex:\n        chunks = dict(ex.map(get, list(info)))",
 "new_string": "    with ThreadPoolExecutor(threads) as ex:\n        chunks = dict(ex.map(get, [(row, int(ch)) for row in sorted(need) for ch in channels]))"
}
```

```
The file entries/000055-peterson-2021/ajile.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "old_string": "def fetch_windows(url: str,",
 "new_string": "def _range(session, url: str, offset: int, n: int) -> bytes:\n    r = session.get(url, headers={\"Range\": f\"bytes={offset}-{offset + n - 1}\"}, timeout=120)\n    r.raise_for_status()\n    return r.content\n\n\ndef chunk_index(url: str, session=None, threads: int = 24) -> dict:\n    \"\"\"(chunk row, channel) -> (byte offset, compressed size) of every ECoG chunk.\n\n    h5py looks chunks up one at a time, and over the network each lookup of a B-tree node is a\n    request (about 0.4 s per chunk row here). This reads the dataset's version 1 chunk B-tree\n    directly, one level at a time with parallel requests: the object header gives the layout\n    message (type 8, version 3, chunked) and the B-tree root; each node is \"TREE\", type, level,\n    entries used, two sibling addresses, then keys (chunk size, filter mask, one 8-byte offset\n    per dimension plus one) alternating with child addresses (HDF5 file format specification,\n    sections III.A.1 and IV.A.2.i). The notebook checks it against h5py on sample chunks.\"\"\"\n    session = session or requests.Session()\n    with h5py.File(remfile.File(url), \"r\") as f:\n        header_address = h5py.h5o.get_info(f[\"acquisition/ElectricalSeries/data\"].id).addr\n    header = _range(session, url, header_address, 4096)\n    if header[0] != 1:\n        raise ValueError(\"expected a version 1 object header\")\n    size = struct.unpack_from(\"<I\", header, 8)[0]\n    blocks, layout = [(header, 16, 16 + size)], None\n    while blocks:\n        block, p, end = blocks.pop()\n        while p + 8 <= end:\n            kind, n = struct.unpack_from(\"<HH\", block, p)\n            body = block[p + 8:p + 8 + n]\n            if kind == 0x10:                         # continuation\n                offset, length = struct.unpack_from(\"<QQ\", body)\n                blocks.append((_range(session, url, offset, length), 0, length))\n            elif kind == 0x08:\n                layout = body\n            p += 8 + n\n    if layout is None or layout[0] != 3 or layout[1] != 2:\n        raise ValueError(\"expected a version 3 chunked layout message\")\n    ndim = layout[2]\n    root = struct.unpack_from(\"<Q\", layout, 3)[0]\n    key_size = 8 + 8 * ndim\n    node_size = 24 + 129 * (key_size + 8)            # room for up to 128 entries\n\n    def parse(address):\n        node = _range(session, url, address, node_size)\n        if node[:4] != b\"TREE\":\n            raise ValueError(f\"no B-tree node at {address}\")\n        level, used = struct.unpack_from(\"<BH\", node, 5)\n        p, entries = 24, []\n        for _ in range(used):\n            chunk_size = struct.unpack_from(\"<I\", node, p)[0]\n            offsets = struct.unpack_from(\"<\" + \"Q\" * ndim, node, p + 8)\n            child = struct.unpack_from(\"<Q\", node, p + key_size)[0]\n            entries.append((offsets, chunk_size, child))\n            p += key_size + 8\n        return level, entries\n\n    level, entries = parse(root)\n    with ThreadPoolExecutor(threads) as ex:\n        while level > 0:\n            nodes = list(ex.map(parse, [e[2] for e in entries]))\n            level = nodes[0][0]\n            entries = [e for _, node in nodes for e in node]\n    return {(e[0][0] // CHUNK, e[0][1]): (e[2], e[1]) for e in entries}\n\n\ndef fetch_windows(url: str,"
}
```

```
The file entries/000055-peterson-2021/ajile.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "old_string": "import io\nimport multiprocessing as mp\nimport zlib",
 "new_string": "import io\nimport multiprocessing as mp\nimport struct\nimport zlib"
}
```

```
The file entries/000055-peterson-2021/ajile.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && cat > $TMPDIR/t5.py <<'EOF'
import time, numpy as np, sys, pickle
sys.path.insert(0,'.')
import ajile
if __name__=='__main__':
    t0=time.time()
    sessions=ajile.load_all()
    P=ajile.projection_matrices()
    print('meta+proj',time.time()-t0)
    first_good={}
    for s in sessions: first_good.setdefault(s['subject'], s['electrodes'].good.values)
    tasks=[]
    for s in sessions:
        n=len(s['electrodes'])
        w=ajile.roi_weights(P[s['subject']], n, first_good[s['subject']])
        ch=ajile.covering(w[:,:1],0.95)
        tasks.append(dict(url=s['url'],n_samples=s['ecog_shape'][0],times=s['reaches'].start_time.values,channels=ch,weights=w[ch,:1]/w[ch,:1].sum(0)))
    t1=time.time()
    out=ajile.run_power(tasks,workers=int(sys.argv[1]))
    print('power',time.time()-t1)
    pickle.dump((tasks,out),open(sys.argv[2],'wb'))
EOF
python $TMPDIR/t5.py 12 $TMPDIR/p95.pkl
```

```
Exit code 1
meta+proj 44.66757845878601
concurrent.futures.process._RemoteTraceback: 
"""
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/process.py", line 255, in _process_worker
    r = call_item.fn(*call_item.args, **call_item.kwargs)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/process.py", line 204, in _process_chunk
    return [fn(*args) for args in chunk]
            ~~^^^^^^^
  File "entries/000055-peterson-2021/ajile.py", line 431, in session_power
    x = fetch_windows(task["url"], task["n_samples"], task["times"], task["channels"])
  File "entries/000055-peterson-2021/ajile.py", line 404, in fetch_windows
    chunks = dict(ex.map(get, [(row, int(ch)) for row in sorted(need) for ch in channels]))
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
[... 34 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "old_string": "        n_bytes = min(size, int(want * 1.02) + 65536)\n        for attempt in range(2):\n            r = session.get(url, headers={\"Range\": f\"bytes={offset}-{offset + n_bytes - 1}\"},\n                            timeout=120)\n            r.raise_for_status()\n            raw = zlib.decompressobj().decompress(r.content)\n            if len(raw) >= want or n_bytes == size:\n                break\n            n_bytes = size",
 "new_string": "        n_bytes = min(size, int(want * 1.02) + 65536)\n        for attempt in range(4):\n            content = _range(session, url, offset, n_bytes)\n            if len(content) != n_bytes:              # a short read; ask again\n                continue\n            raw = zlib.decompressobj().decompress(content)\n            if len(raw) >= want:\n                break\n            n_bytes = size"
}
```

```
The file entries/000055-peterson-2021/ajile.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && python $TMPDIR/t5.py 12 $TMPDIR/p95.pkl
```

```
Exit code 1
meta+proj 43.966482400894165
concurrent.futures.process._RemoteTraceback: 
"""
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/process.py", line 255, in _process_worker
    r = call_item.fn(*call_item.args, **call_item.kwargs)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/process.py", line 204, in _process_chunk
    return [fn(*args) for args in chunk]
            ~~^^^^^^^
  File "entries/000055-peterson-2021/ajile.py", line 431, in session_power
    x = fetch_windows(task["url"], task["n_samples"], task["times"], task["channels"])
  File "entries/000055-peterson-2021/ajile.py", line 404, in fetch_windows
    chunks = dict(ex.map(get, [(row, int(ch)) for row in sorted(need) for ch in channels]))
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ajile.py').read()
s=s.replace('''            chunk_size = struct.unpack_from("<I", node, p)[0]
            offsets = struct.unpack_from("<" + "Q" * ndim, node, p + 8)
            child = struct.unpack_from("<Q", node, p + key_size)[0]
            entries.append((offsets, chunk_size, child))''','''            chunk_size, mask = struct.unpack_from("<II", node, p)
            offsets = struct.unpack_from("<" + "Q" * ndim, node, p + 8)
            child = struct.unpack_from("<Q", node, p + key_size)[0]
            entries.append((offsets, chunk_size, child, mask))''')
s=s.replace('''    return {(e[0][0] // CHUNK, e[0][1]): (e[2], e[1]) for e in entries}''','''    return {(e[0][0] // CHUNK, e[0][1]): (e[2], e[1], e[3]) for e in entries}''')
s=s.replace('''    """(chunk row, channel) -> (byte offset, compressed size) of every ECoG chunk.''','''    """(chunk row, channel) -> (byte offset, stored size, filter mask) of every ECoG chunk.

    A filter mask of 1 means gzip was skipped for that chunk (HDF5 stores a chunk uncompressed
    when compression would not shrink it).''')
s=s.replace('''        offset, size = index[key]
        want = need[row] * 4''','''        offset, size, mask = index[key]
        want = need[row] * 4
        if mask & 1:                                 # stored without gzip
            return key, np.frombuffer(_range(session, url, offset, want), dtype="<f4")''')
open('ajile.py','w').write(s)
EOF
grep -n "mask" ajile.py; . $TMPDIR/expl/bin/activate && python $TMPDIR/t5.py 12 $TMPDIR/p95.pkl
```

```
Exit code 1
307:    """(chunk row, channel) -> (byte offset, stored size, filter mask) of every ECoG chunk.
309:    A filter mask of 1 means gzip was skipped for that chunk (HDF5 stores a chunk uncompressed
316:    entries used, two sibling addresses, then keys (chunk size, filter mask, one 8-byte offset
352:            chunk_size, mask = struct.unpack_from("<II", node, p)
355:            entries.append((offsets, chunk_size, child, mask))
389:        offset, size, mask = index[key]
391:        if mask & 1:                                 # stored without gzip
meta+proj 42.90670680999756
concurrent.futures.process._RemoteTraceback: 
"""
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/process.py", line 255, in _process_worker
    r = call_item.fn(*call_item.args, **call_item.kwargs)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/process.py", line 204, in _process_chunk
    return [fn(*args) for args in chunk]
            ~~^^^^^^^
  File "entries/000055-peterson-2021/ajile.py", line 436, in session_power
    x = fetch_windows(task["url"], task["n_samples"], task["times"], task["channels"])
  File "entries/000055-peterson-2021/ajile.py", line 409, in fetch_windows
[... 41 more lines not kept]
```

**Agent**

Still failing on the same chunk. Looking at it directly:

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && cat > $TMPDIR/t6.py <<'EOF'
import sys, numpy as np, zlib, requests, h5py, remfile, pickle
sys.path.insert(0,'.')
import ajile
tasks,_=None,None
urls=ajile.asset_urls()
import pickle
res=pickle.load(open(sys.argv[1],'rb'))
for (path,url),(info,rd,*_ ) in zip(urls,res):
    assert path==info['path']
    rows=set()
    for a in rd.start_time.values:
        s=int(round((a-2)*500)); rows|={s//84375,(s+1999)//84375}
    if 195 in rows:
        print(path)
        S=requests.Session()
        idx=ajile.chunk_index(url,S)
        off,size,mask=idx[(195,2)]
        c=ajile._range(S,url,off,size)
        print(size,len(c),mask)
        d=zlib.decompressobj(); raw=d.decompress(c); print(len(raw), d.eof, len(d.unused_data))
        f=h5py.File(remfile.File(url),'r'); x=f['acquisition/ElectricalSeries/data'][195*84375:196*84375,2]
        print(np.allclose(np.frombuffer(raw,'<f4'), x[:len(raw)//4]), np.abs(x[len(raw)//4:]).max(), x[len(raw)//4-3:len(raw)//4+3])
        break
EOF
python $TMPDIR/t6.py $TMPDIR/meta_all.pkl
```

```
sub-01/sub-01_ses-7_behavior+ecephys.nwb
201962 201962 0
217648 True 0
False 186.18811 [-14.028666   -5.2793145   3.63898     5.5821977  15.3550625  17.771975 ]
```

**Agent**

Subject 01 day 7 is stored with a different chunk length (54412 samples). I'll take the chunk shape from each file's layout message.

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ajile.py').read()
s=s.replace('''    ndim = layout[2]
    root = struct.unpack_from("<Q", layout, 3)[0]''','''    ndim = layout[2]
    root = struct.unpack_from("<Q", layout, 3)[0]
    chunk_rows = struct.unpack_from("<I", layout, 11)[0]''')
s=s.replace('''    return {(e[0][0] // CHUNK, e[0][1]): (e[2], e[1], e[3]) for e in entries}''','''    return chunk_rows, {(e[0][0] // chunk_rows, e[0][1]): (e[2], e[1], e[3]) for e in entries}''')
s=s.replace('''    """(chunk row, channel) -> (byte offset, stored size, filter mask) of every ECoG chunk.''','''    """Samples per chunk, and (chunk row, channel) -> (byte offset, stored size, filter mask) of
    every ECoG chunk.''')
open('ajile.py','w').write(s)
EOF
grep -n "CHUNK" ajile.py
```

```
59:CHUNK = 84375              # ECoG samples per stored chunk
382:        for row in range(s // CHUNK, (s + length - 1) // CHUNK + 1):
383:            need[row] = max(need.get(row, 0), min(s + length, (row + 1) * CHUNK) - row * CHUNK)
418:            for row in range(s // CHUNK, (s + length - 1) // CHUNK + 1):
419:                a = max(s, row * CHUNK) - row * CHUNK
420:                b = min(s + length, (row + 1) * CHUNK) - row * CHUNK
```

**Agent calls Read**

```json
{
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "offset": 370,
 "limit": 55
}
```

```
370	def fetch_windows(url: str, n_samples: int, times: np.ndarray, channels: np.ndarray,
371	                  threads: int = 24) -> np.ndarray:
372	    """ECoG in microvolts around each time: events x channels x samples (WINDOW, at FS).
373	
374	    Windows that run past the recording are NaN."""
375	    n0, n1 = int(round(-WINDOW[0] * FS)), int(round(WINDOW[1] * FS))
376	    starts = np.round(np.asarray(times) * FS).astype(int) - n0
377	    length = n0 + n1
378	    need = {}                                  # chunk row -> samples needed from its start
379	    for s in starts:
380	        if s < 0 or s + length > n_samples:
381	            continue
382	        for row in range(s // CHUNK, (s + length - 1) // CHUNK + 1):
383	            need[row] = max(need.get(row, 0), min(s + length, (row + 1) * CHUNK) - row * CHUNK)
384	    session = requests.Session()
385	    session.mount("https://", requests.adapters.HTTPAdapter(pool_connections=threads,
386	                                                            pool_maxsize=threads))
387	    index = chunk_index(url, session, threads)
388	
389	    def get(key):
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ajile.py').read()
old=s[s.index('    n0, n1 = int(round(-WINDOW[0] * FS)), int(round(WINDOW[1] * FS))\n    starts'):s.index('    return out\n\n\ndef session_power')]
new='''    n0, n1 = int(round(-WINDOW[0] * FS)), int(round(WINDOW[1] * FS))
    starts = np.round(np.asarray(times) * FS).astype(int) - n0
    length = n0 + n1
    session = requests.Session()
    session.mount("https://", requests.adapters.HTTPAdapter(pool_connections=threads,
                                                            pool_maxsize=threads))
    rows_per, index = chunk_index(url, session, threads)   # chunk length differs between files

    def rows(s):
        return range(s // rows_per, (s + length - 1) // rows_per + 1)

    inside = [(k, s) for k, s in enumerate(starts) if s >= 0 and s + length <= n_samples]
    need = {}                                  # chunk row -> samples needed from its start
    for _, s in inside:
        for row in rows(s):
            need[row] = max(need.get(row, 0), min(s + length, (row + 1) * rows_per) - row * rows_per)

    def get(key):
        row, ch = key
        offset, size, mask = index[key]
        want = need[row] * 4
        if mask & 1:                                 # stored without gzip
            return key, np.frombuffer(_range(session, url, offset, want), dtype="<f4")
        # gzip of these float32 samples barely compresses; ask for the bytes the samples need
        # plus a margin, and fetch the rest of the chunk if that was not enough.
        n_bytes, raw = min(size, int(want * 1.02) + 65536), b""
        for attempt in range(4):
            content = _range(session, url, offset, n_bytes)
            if len(content) != n_bytes:              # a short read; ask again
                continue
            raw = zlib.decompressobj().decompress(content)
            if len(raw) >= want:
                break
            n_bytes = size
        if len(raw) < want:
            raise OSError(f"{url}: chunk {key} gave {len(raw)} bytes, {want} needed")
        return key, np.frombuffer(raw[:want], dtype="<f4")

    with ThreadPoolExecutor(threads) as ex:
        chunks = dict(ex.map(get, [(row, int(ch)) for row in sorted(need) for ch in channels]))
    out = np.full((len(starts), len(channels), length), np.nan, dtype=np.float32)
    for k, s in inside:
        for j, ch in enumerate(channels):
            parts = []
            for row in rows(s):
                a = max(s, row * rows_per) - row * rows_per
                b = min(s + length, (row + 1) * rows_per) - row * rows_per
                parts.append(chunks[(row, int(ch))][a:b])
            out[k, j] = np.concatenate(parts)
'''
s=s.replace(old,new)
s=s.replace('CHUNK = 84375              # ECoG samples per stored chunk\n','')
open('ajile.py','w').write(s)
EOF
grep -n "CHUNK" ajile.py; . $TMPDIR/expl/bin/activate && python $TMPDIR/t5.py 12 $TMPDIR/p95.pkl
```

```
meta+proj 38.93971562385559
power 768.5625441074371
```

**Agent**

The full precentral run works but takes 12.8 min, only 21 MB/s. Checking whether it is CPU-bound or network-bound:

**Agent calls Bash**

```bash
nproc; free -g | head -2; . $TMPDIR/expl/bin/activate && cat > $TMPDIR/t7.py <<'EOF'
import sys,time,pickle,numpy as np
sys.path.insert(0,'.')
import ajile
tasks,out=pickle.load(open(sys.argv[1],'rb'))
t=tasks[30]; print(len(t['times']),len(t['channels']))
t0=time.time(); x=ajile.fetch_windows(t['url'],t['n_samples'],t['times'],t['channels']); t1=time.time()
p=ajile.log_power(np.nan_to_num(x).astype(float)); t2=time.time()
print('fetch',t1-t0,'tfr',t2-t1)
EOF
python $TMPDIR/t7.py $TMPDIR/p95.pkl
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
197 15
fetch 129.22297620773315 tfr 2.6579606533050537
```

**Agent**

Fetching dominates: 129 s for one file against 2.7 s of TFR, whereas the earlier raw test moved 3572 chunks in 15 s. Instrumenting the request path:

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && cat > $TMPDIR/t8.py <<'EOF'
import sys,time,pickle,numpy as np,requests,zlib
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,'.')
import ajile
tasks,out=pickle.load(open(sys.argv[1],'rb'))
t=tasks[30]; url=t['url']
S=requests.Session(); S.mount("https://", requests.adapters.HTTPAdapter(pool_connections=32,pool_maxsize=32))
t0=time.time(); rp,idx=ajile.chunk_index(url,S); print('index',time.time()-t0, rp)
keys=[(r,int(c)) for r in sorted({k[0] for k in idx})[100:160] for c in t['channels']]
def g(k):
    o,s,m=idx[k]; a=time.time(); c=ajile._range(S,url,o,s); b=time.time(); zlib.decompressobj().decompress(c); return b-a, time.time()-b
for th in (24,):
    t0=time.time()
    with ThreadPoolExecutor(th) as ex: r=np.array(list(ex.map(g,keys)))
    print(th,len(keys),'wall',time.time()-t0,'req mean',r[:,0].mean(),'dec mean',r[:,1].mean())
# plain requests.get without session
def g2(k):
    o,s,m=idx[k]; a=time.time(); c=requests.get(url,headers={'Range':f'bytes={o}-{o+s-1}'}).content; return time.time()-a
t0=time.time()
with ThreadPoolExecutor(24) as ex: r=np.array(list(ex.map(g2,keys[:300])))
print('nosession 300',time.time()-t0,r.mean())
EOF
python $TMPDIR/t8.py $TMPDIR/p95.pkl
```

```
index 119.45057582855225 84375
24 900 wall 4.893319368362427 req mean 0.1240740081999037 dec mean 0.003181665208604601
nosession 300 5.264651536941528 0.40664791663487754
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && cat > $TMPDIR/t9.py <<'EOF'
import sys,time,pickle,numpy as np,requests,h5py,remfile,struct
sys.path.insert(0,'.')
import ajile
tasks,out=pickle.load(open(sys.argv[1],'rb'))
url=tasks[30]['url']; print(url)
t0=time.time()
with h5py.File(remfile.File(url), "r") as f:
    t1=time.time(); print('open',t1-t0)
    a=h5py.h5o.get_info(f["acquisition/ElectricalSeries/data"].id).addr
    print('get_info',time.time()-t1)
    t2=time.time(); oi=h5py.h5g.get_objinfo(f['acquisition/ElectricalSeries'].id, b'data'); print('objinfo',time.time()-t2, oi.objno, a)
EOF
python $TMPDIR/t9.py $TMPDIR/p95.pkl
```

```
https://dandiarchive.s3.amazonaws.com/blobs/f30/ba3/f30ba333-ef76-4a3d-a185-c8d934e5f52e
open 0.84474778175354
get_info 111.33367204666138
objinfo 0.000186920166015625 (2864, 0) 2864
```

**Agent**

`h5o.get_info` is the slow part, 111 s, probably because it computes storage information. `h5g.get_objinfo` returns the same header address instantly, so I'll switch to it.

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ajile.py').read()
s=s.replace('''        header_address = h5py.h5o.get_info(f["acquisition/ElectricalSeries/data"].id).addr''','''        # h5g.get_objinfo gives the object header address at once; h5o.get_info takes minutes
        header_address = h5py.h5g.get_objinfo(f["acquisition/ElectricalSeries"].id, b"data").objno[0]''')
open('ajile.py','w').write(s)
EOF
. $TMPDIR/expl/bin/activate && python $TMPDIR/t5.py 12 $TMPDIR/p95.pkl
```

```
meta+proj 42.96074390411377
power 245.5435287952423
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && python - <<'EOF'
import pickle,numpy as np
tasks,out=pickle.load(open('/tmp/claude-1001/p95.pkl','rb'))
res=pickle.load(open('/tmp/claude-1001/meta_all.pkl','rb'))
for (info,*_),o in zip(res,out):
    hf=o['hf_noise']
    print(info['subject'],info['session'],len(hf),'bad',int(o['bad_window'].sum()), 'hf mean',round(hf.mean(),1),'sd',round(hf.std(),1),'max',round(hf.max(),1))
EOF
```

```
01 3 156 bad 1 hf mean 9.6 sd 23.3 max 14.5
01 4 196 bad 1 hf mean 10.7 sd 15.2 max 14.4
01 5 199 bad 1 hf mean 10.7 sd 21.0 max 14.5
01 7 190 bad 132 hf mean 3.3 sd 5.0 max 12.4
02 3 51 bad 0 hf mean 14.4 sd 0.7 max 15.6
02 4 94 bad 1 hf mean 13.0 sd 4.1 max 15.2
02 5 82 bad 1 hf mean 10.7 sd 22.2 max 15.7
02 6 78 bad 0 hf mean 13.4 sd 0.8 max 16.0
03 3 198 bad 0 hf mean 13.3 sd 0.6 max 15.6
03 4 193 bad 0 hf mean 13.9 sd 0.7 max 15.7
03 5 137 bad 0 hf mean 14.1 sd 0.7 max 15.9
03 6 114 bad 0 hf mean 13.8 sd 1.6 max 23.4
04 3 35 bad 22 hf mean 4.5 sd 5.8 max 12.8
04 4 98 bad 0 hf mean 11.8 sd 0.4 max 12.7
04 5 43 bad 0 hf mean 12.3 sd 0.5 max 13.4
04 6 82 bad 1 hf mean 11.9 sd 8.9 max 13.7
04 7 159 bad 3 hf mean 9.9 sd 30.5 max 14.6
05 3 56 bad 0 hf mean 14.5 sd 0.6 max 15.7
05 4 48 bad 0 hf mean 14.9 sd 0.6 max 16.3
05 7 163 bad 0 hf mean 15.1 sd 0.7 max 17.6
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && python - <<'EOF'
import pickle,numpy as np
tasks,out=pickle.load(open('/tmp/claude-1001/p95.pkl','rb'))
res=pickle.load(open('/tmp/claude-1001/meta_all.pkl','rb'))
for (info,rd,el,g,epd,_),o in zip(res,out):
    if info['n_samples']<43200000:
        dur=info['n_samples']/500
        t=rd.start_time.values
        print(info['subject'],info['session'],info['start'],'dur h',round(dur/3600,2),'events min/max h',round(t.min()/3600,2),round(t.max()/3600,2),'n beyond',(t+2>dur).sum(),'bad',o['bad_window'].sum(),'epochs max h',round(epd.stop.max()/3600,2))
        bad=o['bad_window']; print('  bad event times h', np.round(t[bad][:8]/3600,2), ' good', np.round(t[~bad][:5]/3600,2))
EOF
```

```
01 7 2000-01-07T03:31:22.414000-05:00 dur h 15.48 events min/max h 8.98 23.83 n beyond 132 bad 132 epochs max h 24.0
  bad event times h [15.5  15.61 15.62 15.67 15.74 15.76 15.77 15.94]  good [8.98 8.98 9.11 9.18 9.2 ]
04 3 2000-01-03T03:20:48.322000-05:00 dur h 15.65 events min/max h 13.7 23.98 n beyond 22 bad 22 epochs max h 24.0
  bad event times h [15.89 15.89 15.94 16.42 16.68 16.77 17.11 17.35]  good [13.7  14.07 14.08 14.19 14.48]
06 3 2000-01-03T03:07:20.566000-05:00 dur h 15.88 events min/max h 8.27 22.12 n beyond 83 bad 83 epochs max h 24.0
  bad event times h [15.91 15.93 15.99 16.03 16.05 16.08 16.12 16.13]  good [8.27 8.27 8.75 8.76 8.82]
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && cat > $TMPDIR/t10.py <<'EOF'
import sys,pickle,numpy as np, pandas as pd
sys.path.insert(0,'.')
import ajile
tasks,out=pickle.load(open(sys.argv[1],'rb'))
res=pickle.load(open(sys.argv[2],'rb'))
for k,((info,rd,*_),t) in enumerate(zip(res,tasks)):
    if info['n_samples']<43200000:
        st=pd.Timestamp(info['start']).tz_convert('UTC')
        off=(st-st.normalize()).total_seconds()
        rng=np.random.default_rng(0)
        times=rd.start_time.values
        res_={}
        for name,tt in [('stored',times),('minus offset',times-off),('stored+30s',times+30),('minus offset+30s',times-off+30)]:
            ok=(tt>3)&(tt<info['n_samples']/500-3)
            sel=np.flatnonzero(ok)[:40]
            x=ajile.fetch_windows(t['url'],info['n_samples'],tt[sel],t['channels'][:6])
            b=ajile.band_values(ajile.subtract_baseline(ajile.log_power(np.nan_to_num(x).astype(float))))
            res_[name]=(len(sel), np.round(np.median(b,axis=(0,1)),2))
        print(info['subject'],info['session'],'offset h',round(off/3600,3),res_)
EOF
python $TMPDIR/t10.py $TMPDIR/p95.pkl $TMPDIR/meta_all.pkl
```

```
01 7 offset h 8.523 {'stored': (40, array([0.97, 0.61])), 'minus offset': (40, array([-1.32,  1.11])), 'stored+30s': (40, array([0.5 , 0.69])), 'minus offset+30s': (40, array([0.01, 0.56]))}
04 3 offset h 8.347 {'stored': (13, array([0.23, 0.39])), 'minus offset': (35, array([0.24, 0.57])), 'stored+30s': (13, array([0.21, 1.06])), 'minus offset+30s': (35, array([0.33, 0.6 ]))}
06 3 offset h 8.122 {'stored': (40, array([0.59, 0.98])), 'minus offset': (40, array([-1.24,  3.19])), 'stored+30s': (40, array([0.64, 0.51])), 'minus offset+30s': (40, array([0.36, 0.43]))}
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && python - <<'EOF'
import pickle,numpy as np,pandas as pd
res=pickle.load(open('/tmp/claude-1001/meta_all.pkl','rb'))
sl=np.zeros(24); ev=np.zeros(24); br=[]
for info,rd,el,g,epd,_ in res:
    e=epd[epd.label.str.contains('Sleep')]
    for a,b in zip(e.start,e.stop):
        for h in range(24):
            sl[h]+=max(0,min(b,(h+1)*3600)-max(a,h*3600))
    ev+=np.histogram(rd.start_time/3600,bins=np.arange(25))[0]
    if info['n_samples']<43200000: print(info['subject'],info['session'],epd.head(3).to_string())
print('sleep hours by hour since file start (h of label)'); print(np.round(sl/3600,1))
print('events by hour since file start'); print(ev.astype(int))
EOF
```

```
01 7           start          stop                   label
0      0.000000  30694.366667  Blocklist (Data break)
1  30694.366667  30815.533333                     Eat
2  30815.533333  30937.733333               Eat, Talk
04 3           start          stop                         label
0      0.000000  49079.800000        Blocklist (Data break)
1  49079.800000  49201.233333  Blocklist (Camera move/zoom)
2  49201.233333  49222.266667        Blocklist (Data break)
06 3         start        stop                   label
0    0.000000   96.566667  Blocklist (Data break)
1   96.566667  217.500000              Sleep/rest
2  217.500000  217.566667  Blocklist (Data break)
sleep hours by hour since file start (h of label)
[33.4 39.5 40.4 44.4 42.2 35.8 28.2 21.4 15.5 13.3 11.4 12.  11.  10.4
 13.2 12.7 10.5  8.6 11.4  9.3  8.9 18.1 31.4 36.3]
events by hour since file start
[153 118 106  44  64 126 207 377 432 462 405 349 535 462 479 525 394 555
 547 552 482 370 208 135]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ajile.py').read()
s=s.replace('''    session["hemisphere"] = "R" if np.nanmean(electrodes.x) > 0 else "L"
    return session''','''    session["hemisphere"] = "R" if np.nanmean(electrodes.x) > 0 else "L"
    start = pd.Timestamp(session["session_start"]).tz_convert("UTC")
    # Seconds from the file's midnight (UTC) to session_start_time. The event, epoch and pose
    # times count from that midnight; the ECoG starts at session_start_time (starting_time 0).
    # The two agree in full-day files (offset 0); in three files that start later they do not,
    # and the notebook shows that subtracting the offset aligns the events with the ECoG.
    session["ecog_offset"] = (start - start.normalize()).total_seconds()
    return session''')
s=s.replace('''    Time of day is the event's clock time from the file's session_start_time, in hours.
    Duration''','''    Time of day is the event time from the start of the file's day, in hours: the files start at
    local midnight as far as the sleep labels show, not at the 19:00 their session_start_time
    states (see the notebook's data check). Duration''')
s=s.replace('''        start = pd.Timestamp(s["session_start"])
        clock = (start.hour + start.minute / 60 + start.second / 3600 + r.start_time / 3600) % 24
''','''        clock = (r.start_time / 3600) % 24
''')
s=s.replace('''    - `hf_noise`: events, mean dB power at 116 and 121 Hz over channels and times;''','''    - `hf_noise`: events, mean dB power at 116 and 121 Hz over channels and times;
    - `seg_power`: events, mean dB power over all frequencies, channels and times (microvolts^2);''')
s=s.replace('''        "hf_noise": p[:, :, hf, :].mean(axis=(1, 2, 3)),''','''        "hf_noise": p[:, :, hf, :].mean(axis=(1, 2, 3)),
        "seg_power": p.mean(axis=(1, 2, 3)),''')
open('ajile.py','w').write(s)
EOF
grep -n "ecog_offset\|seg_power\|clock" ajile.py
```

```
158:    session["ecog_offset"] = (start - start.normalize()).total_seconds()
191:        clock = (r.start_time / 3600) % 24
194:            "t": r.start_time, "time_of_day": clock, "duration": r.stop_time - r.start_time,
442:    - `seg_power`: events, mean dB power over all frequencies, channels and times (microvolts^2);
458:        "seg_power": p.mean(axis=(1, 2, 3)),
```

**Agent**

Writing the claims file:

**Agent calls Write**

```json
{
 "file_path": "claims/000055/10.1523-eneuro.0007-21.2021.yaml",
 "content": "# Claims for Peterson, Singh, Wang, Rao & Brunton (2021), eNeuro, on dandiset 000055 (AJILE12).\n# Source: the full text in PubMed Central (PMC8225404, CC BY 4.0), read from its Methods, Results,\n# figure legends and Tables 1 and 2. The Extended Data figures are EPS files that were not read;\n# claims on them rest on their legends and the Results.\n#\n# When these criteria were written, the author had seen the data check only: the file list and\n# metadata of every file, the number of events per subject and day, the electrode tables\n# (groups, coordinates, `good` flags, and the maximum of the stored R2 columns per subject), the\n# summary of the reach features of two files, the link between the paper's projection matrices\n# and the electrode tables, the event-time offset in three files, the noise measures of the\n# event windows, and, from a trial run of the loading code, the median precentral LFB and HFB\n# power of subject 01 on days 3 to 5. No other claim's analysis had been run. The author had also\n# read the paper's code (GitHub BruntonUWBio/naturalistic_arm_movements_ecog, commit 04c6faf),\n# including the outputs printed in Plot_banded_power_Fig5.ipynb.\n#\n# Method choices fixed here, from the paper's code where the Methods are silent: Morlet power at\n# 1 to 121 Hz in 5 Hz steps with n_cycles = f / 4, in dB, in 0.1 s bins; the baseline (-1.5 to\n# -1 s) is the mean over its bins, subtracted per event, channel and frequency; band power is the\n# median over the bins from 0 to 0.5 s and then over the band's frequencies (LFB 8 to 32 Hz, HFB\n# 76 to 100 Hz); regional power is the projection of baseline-subtracted electrode power with the\n# paper's projection matrices, bad electrodes (those of the subject's first file) set to 0 and the\n# weights renormalised; the reach angle is folded as in the code (negated, then 90 to 270 degrees\n# mapped onto 90 to -90). Choices made here: events are those of the dandiset's reaches tables;\n# an event is dropped when its ECoG window holds missing or flat data, when its mean power is below\n# 0 dB (in microvolts squared), or when its power at 116 and 121 Hz is more than 3 SD above the\n# subject's mean (the Methods' segment rejection, as far as it can be read). Regional power for\n# the precentral claims uses, per subject, the electrodes that carry 95% of the precentral weight,\n# with the weights renormalised over them; the eight-region analysis uses a seeded subsample of\n# five events per file and the electrodes that carry 99% of every region's weight.\nschema_version: 1\ndandiset: \"000055\"\npaper: doi:10.1523/eneuro.0007-21.2021\nclaims:\n- id: subjects-days-hemispheres\n  statement: The data come from 12 subjects, each recorded for 3 to 5 days within days 3 to 7\n    after implantation, with electrodes in the right hemisphere in five subjects and in the left\n    in seven; events are movements of the wrist contralateral to the implant.\n  source: Methods (Subject information, Data collection); Results; Figure 1h; Extended Data\n    Figure 1-1\n  expected:\n  - quantity: number of subjects\n    value: 12\n    tolerance: 0\n  - quantity: subjects implanted in the right hemisphere\n    value: 5\n    tolerance: 0\n  criterion: Reproduced when the dandiset holds 12 subjects, every subject has 3 to 5 files whose\n    days lie within 3 to 7, five subjects have electrodes in the right hemisphere (sign of the\n    mean electrode x coordinate) and seven in the left, and every file's event wrist is the one\n    contralateral to its hemisphere. Counts are exact, so the tolerance is 0.\n- id: demographics\n  statement: The subjects were 8 males and 4 females, aged 29.4 +/- 7.9 years (mean +/- SD).\n  source: Methods (Subject information)\n  expected:\n  - quantity: males\n    value: 8\n    tolerance: 0\n  - quantity: mean age (years)\n    value: 29.4\n    tolerance: 2.94\n- id: electrode-counts\n  statement: Subjects had 87.0 +/- 12.9 surface electrodes (mean +/- SD), and five subjects also\n    had 23.2 +/- 12.1 depth electrodes.\n  source: Methods (Subject information)\n  expected:\n  - quantity: mean surface electrodes per subject\n    value: 87.0\n    tolerance: 8.7\n  - quantity: subjects with depth electrodes\n    value: 5\n    tolerance: 0\n  - quantity: mean depth electrodes in those subjects\n    value: 23.2\n    tolerance: 2.32\n  criterion: Electrodes are counted from the electrode tables, in a subject's first file. Two\n    readings are allowed. (a) Depth electrodes are those of every group whose description\n    contains \"depth\"; the others are surface electrodes. (b) As (a), but electrodes without\n    coordinates are left out, as they could not have been localised. The claim is reproduced\n    when all three values are within tolerance under a reading, partially reproduced when the\n    surface count is within tolerance but a depth value is not, and not reproduced otherwise.\n- id: bad-electrodes\n  statement: Removing electrodes with abnormal SD or kurtosis left out 4.9 +/- 4.9 surface\n    electrodes per subject, and 1.0 +/- 1.4 depth electrodes in each of the five subjects with\n    depth electrodes.\n  source: Methods (ECoG data processing)\n  expected:\n  - quantity: mean surface electrodes removed per subject\n    value: 4.9\n    tolerance: 0.49\n  - quantity: mean depth electrodes removed per subject with depth electrodes\n    value: 1.0\n    tolerance: 0.1\n  criterion: A removed electrode is one whose `good` flag is false. Three readings are allowed,\n    as the flag differs between a subject's files. (a) The subject's first file, as the paper's\n    code takes it. (b) Bad in any file. (c) The mean over the subject's files. Depth and surface\n    are as in electrode-counts, reading (a). Reproduced when both values are within tolerance\n    under a reading; partially reproduced when one is; not reproduced otherwise.\n  depends_on:\n  - electrode-counts\n- id: event-counts\n  statement: The total number of movement events per subject was between 151 and 947, with a\n    median of 640 across subjects.\n  source: Figure 2 legend\n  expected:\n  - quantity: fewest events in a subject\n    value: 151\n    tolerance: 15.1\n  - quantity: most events in a subject\n    value: 947\n    tolerance: 94.7\n  - quantity: median events per subject\n    value: 640\n    tolerance: 64\n  criterion: Two readings. (a) Every event in the dandiset's reaches tables. (b) The events left\n    after this attempt's segment rejection. Reproduced when all three values are within\n    tolerance under a reading; partially reproduced when one or two are; not reproduced when\n    none is.\n- id: features-differ-subjects\n  statement: All ten behavioural and environmental features differ across subjects (one-way\n    Kruskal-Wallis test, p < 0.001 for every feature).\n  source: Results (Behavior during naturalistic movements); Figure 2\n  criterion: A Kruskal-Wallis test across the 12 subjects on every event of the reaches tables,\n    for each of day, time of day, duration, magnitude, folded angle, onset speed, speech ratio,\n    bimanual ratio, bimanual overlap and bimanual class. Reproduced when p < 0.001 for all ten;\n    partially reproduced when for 7 to 9; not reproduced otherwise.\n- id: days-one-dominant\n  statement: The number of events was fairly consistent across recording days, except in\n    subjects 04, 05 and 09, who each had one day representing most of their events.\n  source: Results (Behavior during naturalistic movements); Figure 2\n  criterion: Two readings of \"most\". (a) In each of subjects 04, 05 and 09 one day holds more\n    than half of the subject's events, and in no other subject. (b) Subjects 04, 05 and 09 are\n    the three subjects with the largest share of their events on one day. Reproduced when either\n    holds; partially reproduced when two of the three subjects meet reading (b); not reproduced\n    otherwise.\n- id: duration-magnitude-small\n  statement: Most reaches last less than 2 s and cover less than 200 pixels, with minimal\n    variability across subjects.\n  source: Results (Behavior during naturalistic movements); Figure 2\n  criterion: Reproduced when, over all events, more than half last less than 2 s and more than\n    half cover less than 200 pixels, and both hold in at least 10 of the 12 subjects. Partially\n    reproduced when it holds over all events but in fewer subjects. Not reproduced otherwise.\n- id: angle-bimodal\n  statement: Reach angle distributions tend to be bimodal, with peaks at +/-90 degrees (upward and\n    downward reaches) and few side-to-side reaches.\n  source: Results (Behavior during naturalistic movements); Figure 2\n  criterion: On the folded angle (-90 down to 90 up). Over all events, the two most populated of\n    the twelve 15-degree bins from -90 to 90 are the two outer ones, and in at least 8 of the 12\n    subjects more events have |angle| above 60 degrees than below 30. Reproduced when both hold;\n    partially reproduced when only the pooled part holds; not reproduced otherwise.\n- id: feature-correlations\n  statement: Over all subjects, reach magnitude correlates with reach duration (r = 0.26) and\n    onset speed (r = 0.56), reach duration with bimanual overlap (r = 0.48), and the bimanual\n    features with each other (overlap and ratio r = 0.51, class and ratio r = 0.50, overlap and\n    class r = 0.61).\n  source: Results (Behavior during naturalistic movements); Extended Data Figure 2-2\n  expected:\n  - quantity: r magnitude and duration\n    value: 0.26\n    tolerance: 0.026\n  - quantity: r magnitude and onset speed\n    value: 0.56\n    tolerance: 0.056\n  - quantity: r duration and bimanual overlap\n    value: 0.48\n    tolerance: 0.048\n  - quantity: r bimanual overlap and bimanual ratio\n    value: 0.51\n    tolerance: 0.051\n  - quantity: r bimanual class and bimanual ratio\n    value: 0.5\n    tolerance: 0.05\n  - quantity: r bimanual overlap and bimanual class\n    value: 0.61\n    tolerance: 0.061\n  criterion: Pearson correlation over all events of all subjects, on the features in the code's\n    units (seconds, pixels, pixels per second; bimanual ratio with missing values set to 0.5).\n    Reproduced when all six are within tolerance; partially reproduced when all six are positive\n    and at least three are within tolerance; not reproduced otherwise.\n- id: bimanual-skew\n  statement: Bimanual ratio and overlap are skewed toward unimanual movements, less so in\n    subjects 02, 04 and 05, while the bimanual class is mostly bimanual.\n  source: Results (Behavior during naturalistic movements); Figure 2\n  criterion: Over all events, the median bimanual ratio is below 0.5, the median bimanual overlap\n    is below half the median reach duration, and more than half the events are of class\n    bimanual. Reproduced when these hold and subjects 02, 04 and 05 are among the four subjects\n    with the highest median bimanual ratio; partially reproduced when only the pooled part\n    holds; not reproduced otherwise.\n- id: projection-link\n  statement: The paper's projection matrices from electrodes to AAL regions can be matched to the\n    dandiset's electrodes, and selecting regions with an average electrode density above 3 gives\n    the paper's eight regions.\n  source: Methods (Projecting power into regions of interest); Data availability; Figshare\n    doi:10.6084/m9.figshare.12114408.v1\n  data: with_inputs\n  criterion: Electrodes are matched by their row order, as there is no identifier. The link holds\n    (reproduced) when, in every subject, the matrix has one row per electrode of the dandiset's\n    table (apart from rows of zeros past the end of the table), the eight regions with average\n    density above 3 are the paper's eight, and the rank correlation between an electrode's weight\n    for a region and its closeness to that region's centroid (median over the eight regions) is\n    above 0.5 and above every value from 20 shuffles of the row order. Partially reproduced when\n    this holds in 9 to 11 subjects; not reproduced otherwise.\n- id: group-pattern-rois\n  statement: At movement onset, low-frequency power decreases and high-frequency power increases\n    across subjects, with the largest changes in the precentral, postcentral and inferior\n    parietal regions and minimal changes in the three temporal regions.\n  source: Results (Intracortical spectral power during naturalistic movements); Figure 3\n  data: with_inputs\n  criterion: Projected power, median over events per subject and mean over subjects, from 0 to\n    0.5 s. Reproduced when LFB power is below 0 and HFB power above 0 in the precentral,\n    postcentral and inferior parietal regions, and in each of these three regions the sum of the\n    absolute LFB and HFB changes is larger than in each of the three temporal regions. Partially\n    reproduced when the signs hold but not the ranking. Not reproduced otherwise.\n  depends_on:\n  - projection-link\n- id: precentral-subject-ci\n  statement: Precentral LFB and HFB power from 0 to 0.5 s after movement onset differ between\n    subjects as given by their 95% confidence intervals in Table 1.\n  source: Table 1; Figure 5\n  data: with_inputs\n  expected:\n  - quantity: S01 LFB (dB), CI -1.87 to -1.29\n    value: -1.58\n    tolerance: 0.29\n  - quantity: S02 LFB (dB), CI -1.12 to -0.31\n    value: -0.715\n    tolerance: 0.405\n  - quantity: S03 LFB (dB), CI -2.11 to -1.73\n    value: -1.92\n    tolerance: 0.19\n  - quantity: S04 LFB (dB), CI -0.17 to 0.01\n    value: -0.08\n    tolerance: 0.09\n  - quantity: S05 LFB (dB), CI -0.7 to -0.38\n    value: -0.54\n    tolerance: 0.16\n  - quantity: S06 LFB (dB), CI -1.63 to -1.11\n    value: -1.37\n    tolerance: 0.26\n  - quantity: S07 LFB (dB), CI -0.84 to -0.51\n    value: -0.675\n    tolerance: 0.165\n  - quantity: S08 LFB (dB), CI -0.3 to 0.04\n    value: -0.13\n    tolerance: 0.17\n  - quantity: S09 LFB (dB), CI -0.57 to -0.08\n    value: -0.325\n    tolerance: 0.245\n  - quantity: S10 LFB (dB), CI -0.87 to -0.35\n    value: -0.61\n    tolerance: 0.26\n  - quantity: S11 LFB (dB), CI -2.3 to -1.86\n    value: -2.08\n    tolerance: 0.22\n  - quantity: S12 LFB (dB), CI -0.66 to -0.44\n    value: -0.55\n    tolerance: 0.11\n  - quantity: S01 HFB (dB), CI 0.03 to 0.23\n    value: 0.13\n    tolerance: 0.1\n  - quantity: S02 HFB (dB), CI 0.07 to 0.64\n    value: 0.355\n    tolerance: 0.285\n  - quantity: S03 HFB (dB), CI 1.39 to 1.67\n    value: 1.53\n    tolerance: 0.14\n  - quantity: S04 HFB (dB), CI 0.32 to 0.52\n    value: 0.42\n    tolerance: 0.1\n  - quantity: S05 HFB (dB), CI 0.2 to 0.48\n    value: 0.34\n    tolerance: 0.14\n  - quantity: S06 HFB (dB), CI 2.02 to 2.37\n    value: 2.195\n    tolerance: 0.175\n  - quantity: S07 HFB (dB), CI 1.14 to 1.34\n    value: 1.24\n    tolerance: 0.1\n  - quantity: S08 HFB (dB), CI 0.36 to 0.63\n    value: 0.495\n    tolerance: 0.135\n  - quantity: S09 HFB (dB), CI -0.11 to 0.23\n    value: 0.06\n    tolerance: 0.17\n  - quantity: S10 HFB (dB), CI 0.01 to 0.3\n    value: 0.155\n    tolerance: 0.145\n  - quantity: S11 HFB (dB), CI 0.09 to 0.34\n    value: 0.215\n    tolerance: 0.125\n  - quantity: S12 HFB (dB), CI 0.06 to 0.2\n    value: 0.13\n    tolerance: 0.07\n  criterion: Each expected value is the centre of the paper's 95% confidence interval and its\n    tolerance the half-width, so a value matches when it lies inside the interval. The table\n    does not say whether the interval is of the mean or the median over events; both readings\n    are computed. Reproduced when at least 20 of the 24 values match under a reading; partially\n    reproduced when 12 to 19 do; not reproduced when fewer do.\n  depends_on:\n  - projection-link\n- id: precentral-subjects-differ\n  statement: Precentral LFB and HFB power from 0 to 0.5 s differ significantly across subjects\n    (one-way Kruskal-Wallis test, p < 0.001 for both bands).\n  source: Results (Intracortical spectral power); Figure 5; Table 1\n  data: with_inputs\n  criterion: Kruskal-Wallis test across the 12 subjects on the events' precentral band power.\n    Reproduced when p < 0.001 in both bands; partially reproduced when in one; not reproduced\n    otherwise.\n  depends_on:\n  - projection-link\n- id: precentral-day-effects\n  statement: Precentral power depends on the recording day in several subjects; the effect is\n    significant (Kruskal-Wallis, p < 0.05) in LFB for subjects 03, 05, 06, 07, 08 and 11, and in\n    HFB for subjects 03, 04, 07, 08 and 10.\n  source: Results (Intracortical spectral power); Figure 5; Table 2\n  data: with_inputs\n  criterion: Kruskal-Wallis test across days within each subject and band, p < 0.05. Of the 24\n    subject and band calls, count those that agree with the paper (significant where it is, not\n    where it is not). Reproduced when at least 20 agree; partially reproduced when 14 to 19\n    agree and at least three subjects are significant in each band; not reproduced otherwise.\n  depends_on:\n  - projection-link\n- id: baseline-reduces-day-variability\n  statement: Baseline subtraction reduces the variability of LFB and HFB power across recording\n    days, but clear variability remains.\n  source: Extended Data Figure 5-1 (legend); Results\n  data: with_inputs\n  criterion: The legend does not name the region; the precentral region of Figure 5 is used. Per\n    subject and band, the SD across days of the day means of power from 0 to 0.5 s, with and\n    without baseline subtraction. Reproduced when the SD with subtraction is lower in at least 9\n    of 12 subjects in both bands and above 0 in all; partially reproduced when this holds in one\n    band; not reproduced otherwise.\n  depends_on:\n  - projection-link\n- id: regression-r2-max\n  statement: Regression models of single-event power on the behavioural features explain at\n    most 25% of the variance of withheld events (R2 at most 0.25).\n  source: Results (Modeling single-event spectral power); Figure 6b; Discussion\n  data: with_inputs\n  expected:\n    quantity: largest test R2 of any model\n    value: 0.25\n    tolerance: 0.025\n  criterion: Recomputed for the tested electrodes (the eight good electrodes per subject with the\n    largest precentral weight), LFB and HFB, as the mean test R2 over train and test splits. The\n    claim is an upper bound, so it is reproduced when the largest mean R2 is at most 0.275 and\n    not reproduced when it is above. The R2 values stored in the dandiset's electrode tables are\n    shown as reference.\n  depends_on:\n  - projection-link\n- id: regression-r2-sensorimotor\n  statement: The models with the largest R2 on withheld data are in frontoparietal sensorimotor\n    areas.\n  source: Results (Modeling single-event spectral power); Figure 6b; Extended Data Figure 6-1\n  data: with_inputs\n  criterion: Tested on the R2 values stored in the dandiset's electrode tables (low_freq_R2,\n    high_freq_R2), which cover every electrode; the recomputation covers precentral electrodes\n    only. Per subject, the stored R2 of good electrodes is projected onto the eight regions; the\n    regional values are averaged over subjects. Reproduced when, in both bands, the region with\n    the highest value is one of the five frontoparietal regions (precentral, postcentral, middle\n    frontal, inferior parietal, supramarginal) and the mean over these five is higher than the\n    mean over the three temporal regions; partially reproduced when this holds in one band; not\n    reproduced otherwise.\n  depends_on:\n  - projection-link\n- id: regression-angle-day-top\n  statement: Reach angle and recording day are the most explanatory features of single-event\n    power, especially of low-frequency power.\n  source: Results (Modeling single-event spectral power); Figure 6c\n  data: with_inputs\n  criterion: On the tested electrodes whose mean LFB test R2 is above 0.05 (the code selects\n    models on LFB R2 for both bands), the mean Delta R2 of each of the ten features. Following the\n    Methods, Delta R2 is the full model's test R2 minus that of a model fit with the feature\n    shuffled, scored on the unshuffled withheld events. Reproduced when reach angle and day have\n    the two largest mean Delta R2 in LFB; partially reproduced when one of them is among the two\n    largest; not reproduced otherwise. Blocked (other) if fewer than five electrodes pass the R2\n    threshold.\n  depends_on:\n  - regression-r2-max\n- id: regression-angle-coefficient\n  statement: Upward reaches are associated with decreased low-frequency power and increased\n    high-frequency power, enhancing the average pattern.\n  source: Results (Modeling single-event spectral power); Figure 6d\n  data: with_inputs\n  criterion: On the electrodes selected as in regression-angle-day-top, the mean over electrodes\n    of the reach angle coefficient (mean over splits, standardised features). Reproduced when it\n    is negative for LFB and positive for HFB; partially reproduced when one sign holds; not\n    reproduced otherwise.\n  depends_on:\n  - regression-angle-day-top\n- id: regression-angle-retained\n  statement: Reach angle is the feature most often retained by forward selection in sensorimotor\n    areas.\n  source: Results (Modeling single-event spectral power); Extended Data Figure 6-2 (legend)\n  data: with_inputs\n  criterion: On all tested electrodes (both bands), the fraction of models in which forward\n    selection retains each feature (day and time of day counted per one-hot column, as the code\n    does). Reproduced when reach angle has the highest fraction; partially reproduced when it is\n    second; not reproduced otherwise.\n  depends_on:\n  - regression-r2-max\n"
}
```

```
File created successfully at: claims/000055/10.1523-eneuro.0007-21.2021.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Next I'll add the regression to the helper, following the code's design matrix, forward selection and ΔR² but with the Methods' 90/10 split and unshuffled test scoring. First, timing a Huber fit:

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && uv pip install -q scikit-learn 2>&1|tail -1; python -c "
import numpy as np,time
from sklearn.linear_model import HuberRegressor
rng=np.random.default_rng(0); X=rng.normal(size=(630,16)); y=X[:,0]+rng.standard_t(3,630)
t=time.time()
for i in range(100): HuberRegressor().fit(X,y)
print((time.time()-t)/100)"
```

```
0.0035294365882873537
```

**Agent**

About 3.5 ms per fit, so 40 splits on 8 electrodes per subject is affordable.

**Agent calls Bash**

```bash
cat >> ajile.py <<'EOF'


# ---------------------------------------------------------------- regression (Figure 6)

REG_FEATURES = ["duration", "magnitude", "angle", "onset_speed", "speech_ratio", "bimanual_ratio",
                "bimanual_overlap", "bimanual_class", "day", "time_of_day"]


def design(events: pd.DataFrame) -> tuple[np.ndarray, list[str], dict[str, list[int]]]:
    """The code's design matrix for one subject (regression_utils.single_subj_regression).

    Duration is log-transformed, magnitude and onset speed log(x + 1); the eight continuous
    features are standardised (mean 0, SD 1); day is one-hot by recording day and time of day
    one-hot in three 8 h bins (0 to 8, 8 to 16, 16 to 24, ends included as in the code); the
    one-hot columns are not standardised."""
    cont = pd.DataFrame({
        "duration": np.log(events.duration), "magnitude": np.log(events.magnitude + 1),
        "angle": events.angle, "onset_speed": np.log(events.onset_speed + 1),
        "speech_ratio": events.speech_ratio, "bimanual_ratio": events.bimanual_ratio,
        "bimanual_overlap": events.bimanual_overlap, "bimanual_class": events.bimanual_class})
    cont = (cont - cont.mean()) / cont.std()
    days = pd.get_dummies(events.day.to_numpy(), prefix="day").astype(float)
    tod = events.time_of_day.to_numpy()
    tods = pd.DataFrame({"tod_0_8": ((tod >= 0) & (tod <= 8)).astype(float),
                         "tod_8_16": ((tod >= 8) & (tod <= 16)).astype(float),
                         "tod_16_24": ((tod >= 16) & (tod <= 24)).astype(float)})
    x = pd.concat([cont.reset_index(drop=True), days.reset_index(drop=True), tods], axis=1)
    names = list(x.columns)
    groups = {f: [names.index(f)] for f in REG_FEATURES[:8]}
    groups["day"] = [i for i, n in enumerate(names) if n.startswith("day_")]
    groups["time_of_day"] = [i for i, n in enumerate(names) if n.startswith("tod_")]
    return x.to_numpy(float), names, groups


def _adj_r2(x: np.ndarray, y: np.ndarray) -> float:
    a = np.column_stack([np.ones(len(y)), x])
    beta = np.linalg.lstsq(a, y, rcond=None)[0]
    r2 = 1 - np.sum((y - a @ beta) ** 2) / np.sum((y - y.mean()) ** 2)
    n, p = len(y), x.shape[1]
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)


def forward_select(x: np.ndarray, y: np.ndarray) -> list[int]:
    """Columns kept by forward selection on adjusted R2 of an OLS fit (the code's
    _forward_selected_new): add the best column while adjusted R2 rises above the current score,
    which starts at 0."""
    remaining, selected, current = list(range(x.shape[1])), [], 0.0
    while remaining:
        scores = [(_adj_r2(x[:, selected + [c]], y), c) for c in remaining]
        best, column = max(scores)
        if best <= current:
            break
        remaining.remove(column)
        selected.append(column)
        current = best
    return selected


def day_balanced_split(days: np.ndarray, per_train: float, rng: np.random.Generator):
    """The code's train_test_split_day_balance: the same number of test events from each day."""
    uniq = np.unique(days)
    n_test = int(((1 - per_train) * len(days)) // len(uniq))
    train, test = [], []
    for d in uniq:
        idx = np.flatnonzero(days == d)
        idx = idx[rng.permutation(len(idx))]
        train.extend(idx[:len(idx) - n_test])
        test.extend(idx[len(idx) - n_test:])
    return np.array(train), np.array(test)


def regression_model(task: dict) -> dict:
    """Huber regression of one electrode's band power on the features, over random day-balanced
    splits (`task`: x, y, groups, days, per_train, n_splits, seed).

    As in the code, forward selection runs once on all events and the columns it leaves out are
    set to 0. For each feature, Delta R2 is the full model's test R2 minus that of a model fit with
    the feature's columns shuffled across events; `delta_methods` scores the shuffled model on the
    unshuffled test events (the Methods), `delta_code` on the shuffled ones (the code). A feature
    with no column selected has Delta R2 0."""
    import warnings
    from sklearn.exceptions import ConvergenceWarning
    from sklearn.linear_model import HuberRegressor
    from sklearn.metrics import r2_score

    x, y, groups = task["x"], task["y"], task["groups"]
    rng = np.random.default_rng(task["seed"])
    selected = forward_select(x, y)
    xs = np.zeros_like(x)
    xs[:, selected] = x[:, selected]
    retained = {f: (len(set(c) & set(selected)) / len(c) if f in ("day", "time_of_day")
                    else float(c[0] in selected)) for f, c in groups.items()}
    r2_test, r2_train, coef_angle, unconverged = [], [], [], 0
    delta_methods = {f: [] for f in groups}
    delta_code = {f: [] for f in groups}
    for _ in range(task["n_splits"]):
        train, test = day_balanced_split(task["days"], task["per_train"], rng)
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always", ConvergenceWarning)
            model = HuberRegressor().fit(xs[train], y[train])
            full = r2_score(y[test], model.predict(xs[test]))
            r2_test.append(full)
            r2_train.append(r2_score(y[train], model.predict(xs[train])))
            coef_angle.append(model.coef_[groups["angle"][0]])
            for f, cols in groups.items():
                if not np.any(xs[:, cols]):
                    delta_methods[f].append(0.0)
                    delta_code[f].append(0.0)
                    continue
                shuffled = xs.copy()
                shuffled[:, cols] = xs[rng.permutation(len(y))][:, cols]
                m = HuberRegressor().fit(shuffled[train], y[train])
                delta_methods[f].append(full - r2_score(y[test], m.predict(xs[test])))
                delta_code[f].append(full - r2_score(y[test], m.predict(shuffled[test])))
        unconverged += sum(issubclass(w.category, ConvergenceWarning) for w in caught)
    return {"r2_test": float(np.mean(r2_test)), "r2_train": float(np.mean(r2_train)),
            "coef_angle": float(np.mean(coef_angle)), "retained": retained,
            "delta_methods": {f: float(np.mean(v)) for f, v in delta_methods.items()},
            "delta_code": {f: float(np.mean(v)) for f, v in delta_code.items()},
            "n_fits": task["n_splits"] * (1 + len(groups)), "unconverged": unconverged}


def run_regressions(tasks: list[dict], workers: int = 4) -> list[dict]:
    with _pool(workers) as ex:
        return list(ex.map(regression_model, tasks, chunksize=4))
EOF
echo ok
```

```
ok
```

**Agent**

The regression code is in place. Next: make the pose reads per event, fetch the Figshare files in parallel, and include the centroids for the link claim.

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ajile.py').read()
a=s.index('def pose_windows(')
b=s.index('# ---------------------------------------------------------------- projection weights')
s=s[:a]+'''def wrist_windows(task: dict) -> np.ndarray:
    """x, y (pixels) of one keypoint from 1.5 s before to 4.5 s after each time in
    `task['times']` (seconds on the pose clock): events x frames x 2. Each window is read on its
    own, as the pose arrays hold a whole day."""
    n0, n1 = int(round(1.5 * FS_VIDEO)), int(round(4.5 * FS_VIDEO))
    with h5py.File(remfile.File(task["url"]), "r") as f:
        data = f[f"processing/behavior/Position/{task['keypoint']}/data"]
        out = np.full((len(task["times"]), n0 + n1 + 1, 2), np.nan)
        for k, t in enumerate(task["times"]):
            i = int(round(t * FS_VIDEO))
            if i - n0 >= 0 and i + n1 + 1 <= data.shape[0]:
                out[k] = data[i - n0:i + n1 + 1]
    return out


def run_wrist(tasks: list[dict], workers: int = 12) -> list[np.ndarray]:
    with _pool(workers) as ex:
        return list(ex.map(wrist_windows, tasks))


'''+s[b:]
a=s.index('def projection_matrices()')
b=s.index('def roi_weights(')
s=s[:a]+'''def projection_matrices() -> tuple[dict[str, pd.DataFrame], dict[str, pd.DataFrame]]:
    """The paper's electrode-to-AAL weights and region centroids per subject, read into memory
    from Figshare.

    In the weights, row 0 is the electrode density of each region and the other rows are the
    electrodes, each region's column normalised to sum to 1 (project_ecog_to_rois.m). The
    centroids are those of the left-hemisphere part of each region, in MNI coordinates."""
    meta = requests.get(f"https://api.figshare.com/v2/articles/{FIGSHARE_ARTICLE}/versions/1",
                        timeout=60)
    meta.raise_for_status()

    def get(item):
        r = requests.get(item["download_url"], timeout=120)
        r.raise_for_status()
        return item["name"], pd.read_csv(io.BytesIO(r.content))

    with ThreadPoolExecutor(8) as ex:
        tables = dict(ex.map(get, meta.json()["files"]))
    weights = {n.split("_")[1]: t for n, t in tables.items() if n.endswith("_elecs2ROI.csv")}
    centroids = {}
    for n, t in tables.items():
        if n.endswith("_ROIcentroids_Lside.csv"):
            s = n.split("_")[1]
            centroids[s] = t.set_axis(weights[s].columns, axis=0)
    return weights, centroids


'''+s[b:]
open('ajile.py','w').write(s)
EOF
grep -n "^def \|^FIG" ajile.py
```

```
75:FIGSHARE_ARTICLE = 12114408   # "ROI projection matrices and labels", version 1
76:FIGSHARE_DOI = "10.6084/m9.figshare.12114408.v1"
85:def asset_urls() -> list[tuple[str, str]]:
93:def dandiset_metadata() -> dict:
98:def _text(value) -> str:
103:def _strings(values) -> list[str]:
107:def load_session(path_url: tuple[str, str]) -> dict:
162:def _pool(workers: int) -> ProcessPoolExecutor:
166:def load_all(workers: int = 12) -> list[dict]:
173:def fold_angle(angle_deg):
181:def reach_features(sessions: list[dict]) -> pd.DataFrame:
203:def wrist_windows(task: dict) -> np.ndarray:
218:def run_wrist(tasks: list[dict], workers: int = 12) -> list[np.ndarray]:
225:def projection_matrices() -> tuple[dict[str, pd.DataFrame], dict[str, pd.DataFrame]]:
252:def roi_weights(matrix: pd.DataFrame, n_electrodes: int, good: np.ndarray,
260:def covering(weights: np.ndarray, fraction: float) -> np.ndarray:
272:def _morlet_bank():
287:def log_power(x: np.ndarray) -> np.ndarray:
301:def subtract_baseline(p: np.ndarray) -> np.ndarray:
306:def band_values(p: np.ndarray) -> np.ndarray:
[... 11 more lines not kept]
```

**Agent**

Now the notebook. I'll write it as a cell-marked script and convert it with nbformat.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_src.py",
 "content": "# %% [markdown]\n# # Reproducing Peterson, Singh et al. (2021) from dandiset 000055 (AJILE12)\n#\n# **Paper.** Peterson SM, Singh SH, Wang NXR, Rao RPN, Brunton BW (2021). Behavioral and neural\n# variability of naturalistic arm movements. *eNeuro* 8(3).\n# [doi:10.1523/ENEURO.0007-21.2021](https://doi.org/10.1523/ENEURO.0007-21.2021). This attempt\n# used the full text (open access, PubMed Central PMC8225404). The Extended Data figures are EPS\n# files and were not read; claims on them rest on their legends and the Results.\n#\n# **Dandiset.** [DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436), \"AJILE12\",\n# version 0.220127.0436. The paper cites no DANDI version: it points to a curated dataset on\n# Figshare, and the dandiset was published later and names the paper as describing it. This is\n# the only published version. The draft has the same 55 assets and size; its modification date\n# is later, and the analysis does not depend on anything it could have changed.\n#\n# **What the dandiset holds.** One NWB file per subject and recording day (12 subjects, days 3 to\n# 7 after implantation, 55 files): ECoG at 500 Hz, pose of nine upper-body keypoints at 30 Hz,\n# coarse behavioural labels, and the wrist movement events with nine stored features. It holds\n# the whole recordings, not the paper's curated 10 s segments.\n#\n# **Outside input.** The paper's projection matrices from electrodes to AAL regions and the\n# regions' centroids, from Figshare\n# ([doi:10.6084/m9.figshare.12114408.v1](https://doi.org/10.6084/m9.figshare.12114408.v1)),\n# read into memory. Claims marked \"with inputs\" use them and depend on `projection-link`.\n#\n# **Code read.** The paper's analysis code, GitHub `BruntonUWBio/naturalistic_arm_movements_ecog`\n# at commit 04c6faf2f219586fa834d10c614ef48a694cec55: spectral power (`compute_spectral_power.py`,\n# `tfr_utils.py`, `config.py`), projection (`project_ecog_to_rois.m`), Figure 2 features\n# (`feat_plot_utils.py`), Figure 5 (`Plot_banded_power_Fig5.ipynb`) and the regression\n# (`regression_utils.py`). Choices it settles are listed in the helper's docstring.\n#\n# **Random numbers.** Each section that draws them has its own seeded generator.\n#\n# | Claim | Data | Status |\n# |---|---|---|\n# | subjects-days-hemispheres | dandiset | tested |\n# | demographics | dandiset | blocked: no sex or age in the dandiset |\n# | electrode-counts | dandiset | tested |\n# | bad-electrodes | dandiset | tested |\n# | event-counts | dandiset | tested |\n# | features-differ-subjects | dandiset | tested |\n# | days-one-dominant | dandiset | tested |\n# | duration-magnitude-small | dandiset | tested |\n# | angle-bimodal | dandiset | tested |\n# | feature-correlations | dandiset | tested |\n# | bimanual-skew | dandiset | tested |\n# | projection-link | with inputs | tested |\n# | group-pattern-rois | with inputs | tested |\n# | precentral-subject-ci | with inputs | tested |\n# | precentral-subjects-differ | with inputs | tested |\n# | precentral-day-effects | with inputs | tested |\n# | baseline-reduces-day-variability | with inputs | tested |\n# | regression-r2-max | with inputs | tested |\n# | regression-r2-sensorimotor | with inputs | tested |\n# | regression-angle-day-top | with inputs | tested |\n# | regression-angle-coefficient | with inputs | tested |\n# | regression-angle-retained | with inputs | tested |\n\n# %%\nimport os\nimport time\nimport warnings\n\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport ajile\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nsessions = ajile.load_all()\ndandiset_meta = ajile.dandiset_metadata()\nproj, centroids = ajile.projection_matrices()\nev = ajile.reach_features(sessions)\nsubjects = sorted({s[\"subject\"] for s in sessions})\nfirst = {}\nfor s in sessions:\n    first.setdefault(s[\"subject\"], s)\nprint(f\"loaded {len(sessions)} files of dandiset {ajile.DANDISET_ID} version {ajile.DANDISET_VERSION}, \"\n      f\"{len(ev)} events, projection matrices for {len(proj)} subjects, in {time.time() - started:.0f} s\")\n\n# %% [markdown]\n# ## Data check\n#\n# Each check of the metadata against the values is stated under its output.\n\n# %% tags=[\"sanity\"]\nfiles = pd.DataFrame([{\n    \"subject\": s[\"subject\"], \"day\": s[\"day\"], \"session_start\": s[\"session_start\"],\n    \"ecog_hours\": round(s[\"ecog_shape\"][0] / s[\"ecog_rate\"] / 3600, 2), \"channels\": s[\"ecog_shape\"][1],\n    \"ecog_rate\": s[\"ecog_rate\"], \"chunk\": s[\"ecog_chunks\"], \"pose_hours\": round(s[\"pose_n\"] / s[\"pose_rate\"] / 3600, 2),\n    \"events\": len(s[\"reaches\"]), \"event_wrist\": s[\"event_wrist\"], \"hemisphere\": s[\"hemisphere\"],\n    \"offset_h\": round(s[\"ecog_offset\"] / 3600, 3)} for s in sessions])\nprint(files.to_string(index=False))\nprint(\"\\nArchive summary:\", {k: dandiset_meta[\"assetsSummary\"][k] for k in (\"numberOfSubjects\", \"numberOfFiles\", \"numberOfBytes\")},\n      \"species:\", [x[\"name\"] for x in dandiset_meta[\"assetsSummary\"][\"species\"]])\nprint(\"Subject fields in the files:\", sorted({tuple(s[\"subject_fields\"]) for s in sessions}))\nprint(\"Species in the files:\", sorted({s[\"species\"] for s in sessions}))\nprint(\"Dandiset metadata mentions sex or age:\", any(k in str(dandiset_meta).lower() for k in (\"sex\", \"\\\"age\\\"\", \"agereference\")))\nprint(\"ECoG unit, conversion:\", sorted({(s[\"ecog_unit\"], s[\"ecog_conversion\"]) for s in sessions}),\n      \"; pose unit, conversion:\", sorted({(s[\"pose_unit\"], str(s[\"pose_conversion\"])) for s in sessions}))\nprint(\"ECoG starting_time:\", sorted({s[\"ecog_start\"] for s in sessions}), \"; pose rate:\", sorted({s[\"pose_rate\"] for s in sessions}))\nprint(\"Other acquisition series and their descriptions:\", sorted({(k, v) for s in sessions for k, v in s[\"acquisition\"].items() if k != \"ElectricalSeries\"}))\nprint(\"Event timestamps equal reaches start_time (max difference, s):\",\n      max(float(np.max(np.abs(s[\"event_times\"] - s[\"reaches\"].start_time.to_numpy()))) for s in sessions))\n\n# %% [markdown]\n# The archive summary lists 12 subjects, all *Homo sapiens*. The files give only species and\n# subject id: no sex or age, so the paper's demographics cannot be checked. Every file holds\n# 24 h of pose and 15.5 to 24 h of ECoG. ECoG data are stated in volts with a conversion of 1e-6,\n# so the stored values are microvolts. The pose is stated in meters with a conversion of NaN, but\n# its values are image pixels (0 to about 640; the reach features are in pixels). The ECG\n# channels (`ECGL`, `ECGR`, subject 01 only) carry the description of the EOG channels\n# (\"Electrooculography for tracking saccades\"). The chunk length of the ECoG differs between\n# files (84375 samples in most; see the table).\n\n# %% tags=[\"sanity\"]\nel_rows = []\nfor s in sessions:\n    e = s[\"electrodes\"]\n    depth = e.group_name.map(lambda g: \"depth\" in s[\"groups\"].get(g, \"\").lower())\n    el_rows.append({\"subject\": s[\"subject\"], \"day\": s[\"day\"], \"electrodes\": len(e),\n                    \"ecog_channels\": s[\"ecog_shape\"][1], \"depth\": int(depth.sum()),\n                    \"no_xyz\": int(e.x.isna().sum()), \"bad\": int((~e.good).sum()),\n                    \"bad_depth\": int((~e.good & depth).sum()),\n                    \"locations\": \",\".join(sorted(set(e.location))), \"imp_nan\": bool(e.imp.isna().all()),\n                    \"R2_lo_max\": round(float(e.low_freq_R2.max()), 3), \"R2_hi_max\": round(float(e.high_freq_R2.max()), 3),\n                    \"R2_nan\": int(e.low_freq_R2.isna().sum())})\nel_tab = pd.DataFrame(el_rows)\nprint(el_tab.to_string(index=False))\nprint(\"\\nGroups and their descriptions, per subject (first file):\")\nfor sub in subjects:\n    s = first[sub]\n    counts = s[\"electrodes\"].group_name.value_counts().to_dict()\n    print(sub, {g: (d, counts.get(g, 0)) for g, d in s[\"groups\"].items()})\nsame_r2 = all(np.allclose(s[\"electrodes\"].low_freq_R2.fillna(9), first[s[\"subject\"]][\"electrodes\"].low_freq_R2.fillna(9))\n              for s in sessions)\nprint(\"\\nStored R2 columns identical across a subject's files:\", same_r2)\nprint(\"Electrode coordinates identical across a subject's files:\",\n      all(np.allclose(s[\"electrodes\"][[\"x\", \"y\", \"z\"]].fillna(0), first[s[\"subject\"]][\"electrodes\"][[\"x\", \"y\", \"z\"]].fillna(0)) for s in sessions))\n\n# %% [markdown]\n# Electrode `location` is \"unknown\" and impedance is missing for every electrode. Subject 03 has\n# 16 depth electrodes (groups LAD, LPD) without coordinates, and these have no stored R2. In\n# subject 12 the 8 electrodes without stored R2 (rows 116 to 123, group PHD) do have coordinates.\n# The stored R2 columns, the coordinates and the electrode list are the same in every file of a\n# subject; the `good` flags differ between days.\n\n# %% tags=[\"sanity\"]\nreach_desc = first[\"01\"][\"reach_descriptions\"]\nfor k, v in reach_desc.items():\n    print(f\"{k}: {v!r}\")\nprint()\nsummary = ev[[\"duration\", \"magnitude\", \"angle_stored\", \"onset_speed\", \"speech_ratio\", \"bimanual_ratio\",\n              \"bimanual_overlap\", \"bimanual_class\", \"time_of_day\"]].describe(percentiles=[0.01, 0.5, 0.99]).T\nprint(summary.round(3).to_string())\nprint(\"\\nBimanual ratio missing (set to 0.5 as the code does):\", int(ev.bimanual_ratio_nan.sum()))\nprint(\"Events with duration below 0.5 s:\", int((ev.duration < 0.5).sum()), \"; above 4 s:\", int((ev.duration > 4).sum()),\n      \"(Methods keep 0.5 to 4 s)\")\nprint(\"Bimanual overlap above the reach duration:\", int((ev.bimanual_overlap > ev.duration + 1e-6).sum()),\n      \"; overlap above 1:\", int((ev.bimanual_overlap > 1).sum()),\n      \"; median overlap / duration where overlap > 0:\", round(float((ev.bimanual_overlap / ev.duration)[ev.bimanual_overlap > 0].median()), 3))\nprint(\"Bimanual class values:\", sorted(ev.bimanual_class.unique()))\nprint(\"Largest number of events in one file:\", int(files.events.max()), \"(Methods: up to 200 per day)\")\n\n# %% [markdown]\n# Speech ratio lies within 0 to 1, as described. `Bimanual_overlap` is described as a fraction of\n# the movement duration, but reaches 3.8 and is never above the reach duration: it is in seconds,\n# as in the paper's code (overlap in frames divided by 30). The stored reach angle covers -180 to\n# 180 degrees; its convention is checked against the pose below. Some durations\n# (`stop_time - start_time`) fall below the 0.5 s the Methods keep. No file has more than 200\n# events, the Methods' cap per day.\n\n# %% tags=[\"sanity\"]\n# Pose clock and reach angle convention: contralateral wrist around 20 events per file\n# (seeded), at the stored event times and 30 s later.\nrng_pose = np.random.default_rng(55002)\npose_tasks, pose_events = [], []\nfor s in sessions:\n    r = s[\"reaches\"]\n    idx = np.sort(rng_pose.choice(len(r), min(20, len(r)), replace=False))\n    kp = \"R_Wrist\" if s[\"event_wrist\"] == \"r_wrist\" else \"L_Wrist\"\n    t = r.start_time.to_numpy()[idx]\n    pose_tasks.append({\"url\": s[\"url\"], \"keypoint\": kp, \"times\": np.r_[t, t + 30.0]})\n    pose_events.append((s, idx))\nstarted = time.time()\nwrist = ajile.run_wrist(pose_tasks)\nn0 = int(1.5 * ajile.FS_VIDEO)\nrows = []\nfor (s, idx), w in zip(pose_events, wrist):\n    n = len(idx)\n    speed = np.hypot(*np.diff(w, axis=1).transpose(2, 0, 1)) * ajile.FS_VIDEO   # px/s\n    resp = np.nanmean(speed[:, n0:n0 + 15], axis=1) - np.nanmean(speed[:, 0:15], axis=1)\n    r = s[\"reaches\"].iloc[idx]\n    for k in range(n):\n        seg = w[k, n0:n0 + int(round(r.stop_time.iloc[k] * 30)) - int(round(r.start_time.iloc[k] * 30)) + 1] - w[k, n0]\n        rad = np.hypot(seg[:, 0], seg[:, 1])\n        j = np.nanargmax(rad) if np.isfinite(rad).any() else 0\n        ang = np.degrees(np.arctan2(seg[j, 1], seg[j, 0]))\n        rows.append({\"subject\": s[\"subject\"], \"day\": s[\"day\"], \"resp_true\": resp[k], \"resp_shift\": resp[n + k],\n                     \"angle_pose\": ang, \"angle_stored\": r.Reach_angle_degrees.iloc[k],\n                     \"mag_pose\": rad[j], \"mag_stored\": r.Reach_magnitude_px.iloc[k]})\npose_chk = pd.DataFrame(rows)\nd_ang = (pose_chk.angle_pose - pose_chk.angle_stored + 180) % 360 - 180\nprint(f\"wrist windows read in {time.time() - started:.0f} s\")\nprint(\"Wrist speed 0 to 0.5 s minus -1.5 to -1 s (px/s), median over events, per subject:\")\nprint(pose_chk.groupby(\"subject\")[[\"resp_true\", \"resp_shift\"]].median().round(1).T.to_string())\nprint(\"Events with a higher speed after the event time than before: true\",\n      round(float((pose_chk.resp_true > 0).mean()), 3), \"; shifted by 30 s\", round(float((pose_chk.resp_shift > 0).mean()), 3))\nprint(\"Median |stored angle - pose angle| (image coordinates, y down):\", round(float(np.nanmedian(np.abs(d_ang))), 1),\n      \"deg; within 20 deg:\", round(float(np.nanmean(np.abs(d_ang) < 20)), 3))\nprint(\"Same with the pose angle taken with y up:\",\n      round(float(np.nanmedian(np.abs((-pose_chk.angle_pose - pose_chk.angle_stored + 180) % 360 - 180))), 1), \"deg\")\nprint(\"Spearman r, pose and stored magnitude:\", round(stats.spearmanr(pose_chk.mag_pose, pose_chk.mag_stored, nan_policy=\"omit\")[0], 3))\nprint(\"Pose x, y ranges (px), over these windows:\", np.round(np.nanpercentile(np.concatenate(wrist).reshape(-1, 2), [0, 100], axis=0), 1).tolist())\n\n# %% [markdown]\n# The wrist speeds up after the stored event times in every subject and not 30 s later, so the\n# pose and the event tables share a clock, in all files including the three that start later in\n# the day. The stored reach angle is the angle of the wrist's largest displacement in image\n# coordinates, with y pointing down: a positive stored angle is a downward reach. The paper's\n# code negates it before folding, so that upward reaches are positive; the description of the\n# column does not give the convention.\n\n# %% tags=[\"sanity\"]\nsleep = np.zeros(24)\nev_hours = np.histogram(ev.t / 3600, bins=np.arange(25))[0]\nfor s in sessions:\n    e = s[\"epochs\"][s[\"epochs\"].label.str.contains(\"Sleep\")]\n    for a, b in zip(e.start, e.stop):\n        for h in range(24):\n            sleep[h] += max(0.0, min(b, (h + 1) * 3600) - max(a, h * 3600)) / 3600\nprint(\"Hours labelled Sleep/rest, by hour after the start of the file's day:\")\nprint(np.round(sleep, 1).tolist())\nprint(\"Events by hour after the start of the file's day:\")\nprint(ev_hours.tolist())\nprint(\"Epoch labels:\", sorted({l for s in sessions for l in s[\"epochs\"].label.unique()}))\nprint(\"Last epoch stop (h), per file:\", sorted({round(s[\"epochs\"].stop.max() / 3600, 2) for s in sessions}))\n\n# %% [markdown]\n# Sleep labels peak in the first six hours after the start of the file's day and events are\n# fewest from 2 to 5 h. This is consistent with each file's day starting at local midnight. The\n# `session_start_time` of the full-day files is 19:00 at UTC-05:00, which would put sleep at\n# 19:00 to 01:00; the stated time zone does not fit the labels (consistent with the data, not\n# shown). Time of day is therefore taken as hours from the start of the file's day.\n#\n# The epochs and the events of every file run to 24 h, also in the three files whose ECoG covers\n# only 15.5 to 15.9 h and whose `session_start_time` is 8.1 to 8.5 h after the day's start\n# (subject 01 day 7, 04 day 3, 06 day 3). The ECoG `starting_time` is 0 in every file, so the\n# files place the ECoG at the day's start. The ECoG check below shows that in these files the\n# ECoG starts at `session_start_time` and the event times count from the day's start.\n\n# %% tags=[\"sanity\"]\n# Recordings deposited twice: compare per-electrode SD and kurtosis (computed over the whole\n# recording and stored per file), the event tables and the event counts between files.\ndups = []\nfor i, a in enumerate(sessions):\n    for b in sessions[i + 1:]:\n        same_sd = (len(a[\"electrodes\"]) == len(b[\"electrodes\"]) and\n                   np.allclose(a[\"electrodes\"].standard_deviation, b[\"electrodes\"].standard_deviation))\n        same_ev = (len(a[\"reaches\"]) == len(b[\"reaches\"]) and\n                   np.allclose(a[\"reaches\"].to_numpy(float), b[\"reaches\"].to_numpy(float), equal_nan=True))\n        if same_sd or same_ev:\n            dups.append((a[\"path\"], b[\"path\"], same_sd, same_ev))\nprint(\"File pairs with identical electrode SDs or identical event tables:\", dups if dups else \"none\")\n\n# %% [markdown]\n# No two files share their per-electrode statistics or their event tables, so no recording is\n# deposited twice.\n\n# %% [markdown]\n# ## ECoG around the events\n#\n# For every event, ECoG from 2 s before to 2 s after the event is streamed for the electrodes\n# that carry 95% of the subject's precentral weight (set P), and for a seeded subsample of five\n# events per file, at the event and 30 s later, for the electrodes that carry 99% of every\n# region's weight (set A). In the three files above, the event times are moved onto the ECoG\n# clock by subtracting the offset of `session_start_time` from the day's start; the check after\n# the loading cell shows this is needed.\n\n# %%\nrng_sub = np.random.default_rng(55001)\nw_all, tasks_p, tasks_a, sub_idx = {}, [], [], []\nfor s in sessions:\n    sub = s[\"subject\"]\n    n_el = len(s[\"electrodes\"])\n    w = ajile.roi_weights(proj[sub], n_el, first[sub][\"electrodes\"].good.to_numpy())\n    w_all[sub] = w\n    t = s[\"reaches\"].start_time.to_numpy() - s[\"ecog_offset\"]\n    ch_p = ajile.covering(w[:, :1], 0.95)\n    tasks_p.append({\"url\": s[\"url\"], \"n_samples\": s[\"ecog_shape\"][0], \"times\": t, \"channels\": ch_p,\n                    \"weights\": w[ch_p, :1] / w[ch_p, :1].sum(axis=0)})\n    ch_a = ajile.covering(w, 0.99)\n    k = np.sort(rng_sub.choice(len(t), min(5, len(t)), replace=False))\n    sub_idx.append(k)\n    trunc = np.zeros((len(ch_a), 1))\n    trunc[np.isin(ch_a, ch_p), 0] = w[ch_p, 0] / w[ch_p, 0].sum()\n    tasks_a.append({\"url\": s[\"url\"], \"n_samples\": s[\"ecog_shape\"][0], \"times\": np.r_[t[k], t[k] + 30.0],\n                    \"channels\": ch_a, \"weights\": np.c_[w[ch_a] / w[ch_a].sum(axis=0), trunc]})\nstarted = time.time()\nout_p = ajile.run_power(tasks_p)\nprint(f\"set P: {sum(len(t['times']) for t in tasks_p)} events x {sum(len(t['channels']) for t in tasks_p) / len(tasks_p):.1f} \"\n      f\"electrodes on average, in {time.time() - started:.0f} s\")\nstarted = time.time()\nout_a = ajile.run_power(tasks_a)\nprint(f\"set A: {sum(len(k) for k in sub_idx)} events (and as many shifted windows) x \"\n      f\"{sum(len(t['channels']) for t in tasks_a) / len(tasks_a):.1f} electrodes on average, in {time.time() - started:.0f} s\")\n\n# %%\n# One row per event with its precentral band power (set P) and the rejection flags.\npieces = []\nfor s, task, o in zip(sessions, tasks_p, out_p):\n    b = ajile.band_values(o[\"roi_tfr\"][:, 0])\n    braw = ajile.band_values(o[\"roi_tfr_raw\"][:, 0])\n    pieces.append(pd.DataFrame({\"subject\": s[\"subject\"], \"day\": s[\"day\"], \"event\": np.arange(len(task[\"times\"])),\n                                \"lfb\": b[:, 0], \"hfb\": b[:, 1], \"lfb_raw\": braw[:, 0], \"hfb_raw\": braw[:, 1],\n                                \"bad_window\": o[\"bad_window\"], \"seg_power\": o[\"seg_power\"], \"hf_noise\": o[\"hf_noise\"]}))\npw = pd.concat(pieces, ignore_index=True)\nassert len(pw) == len(ev) and (pw[[\"subject\", \"day\", \"event\"]].to_numpy() == ev[[\"subject\", \"day\", \"event\"]].to_numpy()).all()\npw[\"low_power\"] = ~pw.bad_window & (pw.seg_power < 0)\nok = ~pw.bad_window & ~pw.low_power\nmu = pw[ok].groupby(\"subject\").hf_noise.mean()\nsd = pw[ok].groupby(\"subject\").hf_noise.std()\npw[\"hf_outlier\"] = ok & (pw.hf_noise > pw.subject.map(mu) + 3 * pw.subject.map(sd))\npw[\"keep\"] = ok & ~pw.hf_outlier\n\n# %% tags=[\"sanity\"]\nprint(\"Events dropped per subject: missing or flat data, mean power below 0 dB, 115-125 Hz outlier; kept\")\ndrop = pw.groupby(\"subject\").agg(events=(\"keep\", \"size\"), missing_or_flat=(\"bad_window\", \"sum\"),\n                                 below_0dB=(\"low_power\", \"sum\"), hf_outlier=(\"hf_outlier\", \"sum\"), kept=(\"keep\", \"sum\"))\nprint(drop.to_string())\nprint(\"Total kept:\", int(pw.keep.sum()), \"of\", len(pw))\nprint(\"Electrodes in set P per subject:\", {s[\"subject\"]: len(t[\"channels\"]) for s, t in zip(sessions, tasks_p)})\nprint(\"Mean dB power (microvolts^2) of kept windows, 1st to 99th percentile:\", np.round(np.percentile(pw.seg_power[pw.keep], [1, 99]), 1).tolist())\nprint(\"Precentral LFB and HFB of kept events (dB), 1st to 99th percentile:\",\n      np.round(np.percentile(pw.lfb[pw.keep], [1, 99]), 2).tolist(), np.round(np.percentile(pw.hfb[pw.keep], [1, 99]), 2).tolist())\n\n# %% [markdown]\n# Before the offset was applied, the three late-starting files had most of their windows past\n# the end of their ECoG. The windows dropped as missing or flat are those that reach into\n# stretches of zeros or past the end of the recording.\n\n# %% tags=[\"sanity\"]\n# Clock check. (1) The three late-starting files: precentral response at the corrected times,\n# at the stored times, and 30 s after each. (2) Every subject: response at the event times\n# against 30 s later (set A subsample, precentral projection), as a contrast between true and\n# shifted labels.\nlate = [i for i, s in enumerate(sessions) if s[\"ecog_offset\"] > 0]\nrows = []\nfor i in late:\n    s = sessions[i]\n    t = s[\"reaches\"].start_time.to_numpy()\n    for name, tt in ((\"stored times\", t), (\"corrected times\", t - s[\"ecog_offset\"]),\n                     (\"stored + 30 s\", t + 30), (\"corrected + 30 s\", t - s[\"ecog_offset\"] + 30)):\n        inside = np.flatnonzero((tt > 3) & (tt < s[\"ecog_shape\"][0] / ajile.FS - 3))[:40]\n        x = ajile.fetch_windows(s[\"url\"], s[\"ecog_shape\"][0], tt[inside], tasks_p[i][\"channels\"])\n        p = ajile.subtract_baseline(ajile.log_power(np.nan_to_num(x).astype(float)))\n        b = ajile.band_values(np.einsum(\"ecft,cr->erft\", p, tasks_p[i][\"weights\"]))[:, 0]\n        rows.append({\"file\": f\"{s['subject']} day {s['day']}\", \"times\": name, \"events\": len(inside),\n                     \"LFB\": np.median(b[:, 0]), \"HFB\": np.median(b[:, 1])})\nprint(pd.DataFrame(rows).round(2).to_string(index=False))\n\nrows = []\nfor s, k, o in zip(sessions, sub_idx, out_a):\n    b = ajile.band_values(o[\"roi_tfr\"][:, 0])\n    n = len(k)\n    good = ~o[\"bad_window\"][:n] & ~o[\"bad_window\"][n:]\n    rows.append(pd.DataFrame({\"subject\": s[\"subject\"], \"lfb_true\": b[:n, 0], \"lfb_shift\": b[n:, 0],\n                              \"hfb_true\": b[:n, 1], \"hfb_shift\": b[n:, 1]})[good])\nshift = pd.concat(rows)\nshift[\"contrast_true\"] = shift.hfb_true - shift.lfb_true\nshift[\"contrast_shift\"] = shift.hfb_shift - shift.lfb_shift\ntab = shift.groupby(\"subject\")[[\"contrast_true\", \"contrast_shift\"]].median()\ntab[\"events\"] = shift.groupby(\"subject\").size()\ntab[\"wilcoxon_p\"] = [stats.wilcoxon(g.contrast_true, g.contrast_shift)[1] for _, g in shift.groupby(\"subject\")]\nprint(\"\\nPrecentral HFB minus LFB (dB), median over subsampled events, at the event and 30 s later:\")\nprint(tab.round(3).to_string())\n\n# %% [markdown]\n# In subject 01 day 7 and subject 06 day 3, the stored times give no movement response: LFB is\n# not below 0. The corrected times give the decrease in LFB and increase in HFB seen in the\n# other files. So in these files the ECoG starts at `session_start_time` and the events count\n# from the day's start, and the corrected times are used throughout. In subject 04 day 3 neither\n# timing shows a clear response (this subject's LFB response is small on every day), so its\n# alignment could not be established; the same correction is applied. Across subjects, HFB minus\n# LFB is larger at the event times than 30 s later in most subjects (table above), which supports\n# a shared clock between ECoG and events. Where a subject shows no contrast, the response itself\n# is small (subjects 04, 08 and 09 have the smallest precentral responses in Table 1), so the\n# check cannot tell an offset from a weak response there.\n\n# %% [markdown]\n# ## subjects-days-hemispheres\n#\n# > The data come from 12 subjects, each recorded for 3 to 5 days within days 3 to 7 after\n# > implantation, with electrodes in the right hemisphere in five subjects and in the left in\n# > seven; events are movements of the wrist contralateral to the implant.\n\n# %% tags=[\"claim:subjects-days-hemispheres\"]\nper_sub = files.groupby(\"subject\").agg(days=(\"day\", lambda d: sorted(d)), n_days=(\"day\", \"size\"),\n                                       hemisphere=(\"hemisphere\", \"first\"), wrist=(\"event_wrist\", lambda w: sorted(set(w))))\nper_sub[\"contralateral\"] = [(h == \"L\" and w == [\"r_wrist\"]) or (h == \"R\" and w == [\"l_wrist\"])\n                            for h, w in zip(per_sub.hemisphere, per_sub.wrist)]\nprint(per_sub.to_string())\nprint(\"\\nSubjects:\", len(per_sub), \"; days per subject:\", sorted(per_sub.n_days.unique()),\n      \"; all days within 3 to 7:\", bool(files.day.between(3, 7).all()))\nprint(\"Right hemisphere:\", int((per_sub.hemisphere == \"R\").sum()), \"; left:\", int((per_sub.hemisphere == \"L\").sum()),\n      \"; event wrist contralateral in every subject:\", bool(per_sub.contralateral.all()))\n\n# %% [markdown]\n# **Result: reproduced.** The dandiset holds 12 subjects with 3 to 5 days each, all within days\n# 3 to 7. Five subjects have electrodes in the right hemisphere and seven in the left, and every\n# file's events are of the contralateral wrist.\n\n# %% [markdown]\n# ## demographics\n#\n# > The subjects were 8 males and 4 females, aged 29.4 +/- 7.9 years.\n#\n# Blocked: the files hold only species and subject id, and the dandiset metadata has no sex or\n# age (data check).\n\n# %% [markdown]\n# ## electrode-counts\n#\n# > Subjects had 87.0 +/- 12.9 surface electrodes, and five subjects also had 23.2 +/- 12.1 depth\n# > electrodes.\n\n# %% tags=[\"claim:electrode-counts\"]\ndef electrode_counts(drop_no_xyz):\n    rows = []\n    for sub in subjects:\n        s = first[sub]\n        e = s[\"electrodes\"]\n        depth = e.group_name.map(lambda g: \"depth\" in s[\"groups\"].get(g, \"\").lower()).to_numpy()\n        keep = e.x.notna().to_numpy() if drop_no_xyz else np.ones(len(e), bool)\n        rows.append({\"subject\": sub, \"surface\": int((~depth & keep).sum()), \"depth\": int((depth & keep).sum())})\n    return pd.DataFrame(rows).set_index(\"subject\")\n\nfor label, drop_no_xyz in ((\"(a) all electrodes\", False), (\"(b) electrodes with coordinates\", True)):\n    c = electrode_counts(drop_no_xyz)\n    d = c.depth[c.depth > 0]\n    print(f\"{label}: surface {c.surface.mean():.1f} +/- {c.surface.std():.1f}; subjects with depth {len(d)} \"\n          f\"({', '.join(d.index)}); depth {d.mean():.1f} +/- {d.std():.1f}\")\n    print(\"   per subject:\", c.T.to_dict())\nprint(\"Paper: surface 87.0 +/- 12.9; 5 subjects with depth 23.2 +/- 12.1\")\n\n# %% [markdown]\n# **Result: partially reproduced.** Under both readings the mean number of surface electrodes is\n# within tolerance of 87.0 (85.5 and 85.5), but six or seven subjects have depth electrodes, not\n# five, and their mean count (24.6 and 25.8) does not match 23.2 within 10%.\n\n# %% [markdown]\n# ## bad-electrodes\n#\n# > Removing electrodes with abnormal SD or kurtosis left out 4.9 +/- 4.9 surface electrodes per\n# > subject, and 1.0 +/- 1.4 depth electrodes in each of the five subjects with depth electrodes.\n\n# %% tags=[\"claim:bad-electrodes\"]\nrows = []\nfor sub in subjects:\n    ss = [s for s in sessions if s[\"subject\"] == sub]\n    s0 = ss[0]\n    depth = s0[\"electrodes\"].group_name.map(lambda g: \"depth\" in s0[\"groups\"].get(g, \"\").lower()).to_numpy()\n    bad = np.array([~s[\"electrodes\"].good.to_numpy() for s in ss])\n    for reading, b in ((\"(a) first file\", bad[0].astype(float)), (\"(b) any file\", bad.any(axis=0).astype(float)),\n                       (\"(c) mean over files\", bad.mean(axis=0))):\n        rows.append({\"subject\": sub, \"reading\": reading, \"surface\": float(b[~depth].sum()),\n                     \"depth\": float(b[depth].sum()) if depth.any() else np.nan})\nbad_tab = pd.DataFrame(rows)\nprint(bad_tab.pivot(index=\"subject\", columns=\"reading\", values=[\"surface\", \"depth\"]).round(2).to_string())\nfor reading, g in bad_tab.groupby(\"reading\"):\n    print(f\"{reading}: surface {g.surface.mean():.2f} +/- {g.surface.std():.2f}; \"\n          f\"depth {g.depth.mean():.2f} +/- {g.depth.std():.2f} over {g.depth.notna().sum()} subjects\")\nprint(\"Paper: surface 4.9 +/- 4.9; depth 1.0 +/- 1.4 over 5 subjects\")\n\n# %% [markdown]\n# **Result: not reproduced.** Under the reading of the paper's code (first file) 5.42 surface\n# electrodes per subject are flagged, outside 4.9 +/- 0.49, and 2.29 depth electrodes per subject\n# with depth electrodes, against 1.0. The other readings are further away. The surface count is\n# close, but the depth count is more than twice the paper's under every reading.\n\n# %% [markdown]\n# ## event-counts\n#\n# > The total number of movement events per subject was between 151 and 947, with a median of\n# > 640 across subjects.\n\n# %% tags=[\"claim:event-counts\"]\ncounts = pd.DataFrame({\"all_events\": ev.groupby(\"subject\").size(), \"after_rejection\": pw[pw.keep].groupby(\"subject\").size()})\nprint(counts.T.to_string())\nfor c in counts:\n    print(f\"{c}: min {counts[c].min()}, max {counts[c].max()}, median {counts[c].median():.1f}\")\nprint(\"Paper: min 151, max 947, median 640\")\nprint(\"Events per file at the Methods' cap of 200 or one below:\", int((files.events >= 199).sum()), \"of\", len(files))\n\n# %% [markdown]\n# **Result: not reproduced.** The reaches tables hold 211 to 996 events per subject (median\n# 770.5), and 205 to 986 (median 762) remain after the segment rejection: the maximum is within\n# tolerance of 947 under both readings, but the minimum and the median are 15 to 40% above the\n# paper's. Many files hold exactly the cap of up to 200 events per day, which the Methods apply\n# before the visual inspection that removed 17.8 +/- 9.9% of events as false positives. The\n# dandiset keeps no mark of those false positives.\n\n# %% [markdown]\n# ## features-differ-subjects\n#\n# > All ten behavioural and environmental features differ across subjects (Kruskal-Wallis,\n# > p < 0.001 for every feature).\n\n# %% tags=[\"claim:features-differ-subjects\"]\nrows = []\nfor f in ajile.FEATURES:\n    groups = [g[f].to_numpy() for _, g in ev.groupby(\"subject\")]\n    h, p = stats.kruskal(*groups)\n    rows.append({\"feature\": f, \"H\": h, \"p\": p, \"eta2_H\": (h - len(groups) + 1) / (len(ev) - len(groups))})\nkw = pd.DataFrame(rows)\nprint(kw.to_string(index=False, formatters={\"p\": \"{:.2e}\".format, \"H\": \"{:.1f}\".format, \"eta2_H\": \"{:.3f}\".format}))\nprint(\"Features with p < 0.001:\", int((kw.p < 0.001).sum()), \"of 10\")\n\n# %% [markdown]\n# **Result: reproduced.** All ten features differ across subjects with p < 0.001; the smallest\n# effect is for reach duration (eta squared 0.023) and the largest for day of recording.\n\n# %% [markdown]\n# ## days-one-dominant\n#\n# > The number of events was fairly consistent across days, except in subjects 04, 05 and 09,\n# > who each had one day representing most of their events.\n\n# %% tags=[\"claim:days-one-dominant\"]\nshare = ev.groupby([\"subject\", \"day\"]).size().unstack()\ntop = (share.max(axis=1) / share.sum(axis=1)).rename(\"largest_day_share\")\nprint(share.fillna(0).astype(int).assign(largest_day_share=top.round(3)).to_string())\nover_half = sorted(top[top > 0.5].index)\ntop3 = sorted(top.sort_values(ascending=False).index[:3])\nprint(\"\\n(a) subjects with one day above half their events:\", over_half)\nprint(\"(b) the three subjects with the largest one-day share:\", top3)\n\n# %% [markdown]\n# **Result: reproduced.** Under reading (b) subjects 04, 05 and 09 are the three with the largest\n# share of their events on one day (38%, 61% and 52%; the next is 31%). Under reading (a) only\n# subjects 05 and 09 have more than half on one day.\n\n# %% [markdown]\n# ## duration-magnitude-small\n#\n# > Most reaches last less than 2 s and cover less than 200 pixels.\n\n# %% tags=[\"claim:duration-magnitude-small\"]\nfrac = ev.groupby(\"subject\").agg(dur_below_2s=(\"duration\", lambda d: (d < 2).mean()),\n                                 mag_below_200px=(\"magnitude\", lambda m: (m < 200).mean()),\n                                 median_duration=(\"duration\", \"median\"), median_magnitude=(\"magnitude\", \"median\"))\nprint(frac.round(3).to_string())\nprint(\"\\nAll events: below 2 s\", round(float((ev.duration < 2).mean()), 3), \"; below 200 px\", round(float((ev.magnitude < 200).mean()), 3))\nprint(\"Subjects where both are above half:\", int(((frac.dur_below_2s > 0.5) & (frac.mag_below_200px > 0.5)).sum()), \"of 12\")\n\n# %% [markdown]\n# **Result: reproduced.** Over all events, 90% last less than 2 s and 93% cover less than 200\n# pixels, and both hold in all 12 subjects.\n\n# %% [markdown]\n# ## angle-bimodal\n#\n# > Reach angle distributions tend to be bimodal, with peaks at +/-90 degrees and few\n# > side-to-side reaches.\n\n# %% tags=[\"claim:angle-bimodal\"]\nbins = np.arange(-90, 91, 15)\nhist = np.histogram(ev.angle, bins=bins)[0]\nprint(\"Folded angle, events per 15-degree bin from -90 (down) to 90 (up):\", hist.tolist())\nprint(\"Two most populated bins:\", sorted(np.argsort(hist)[-2:].tolist()), \"(outer bins are 0 and 11)\")\nper = ev.groupby(\"subject\").angle.agg(steep=lambda a: (np.abs(a) > 60).mean(), flat=lambda a: (np.abs(a) < 30).mean(),\n                                       up=lambda a: (a > 60).mean(), down=lambda a: (a < -60).mean())\nprint(per.round(3).to_string())\nprint(\"Subjects with more events above |60| than below |30| degrees:\", int((per.steep > per.flat).sum()), \"of 12\")\nfig, ax = plt.subplots(figsize=(5, 2.5))\nax.hist(ev.angle, bins=bins, color=\"0.4\")\nax.set_xlabel(\"folded reach angle (deg, up positive)\")\nax.set_ylabel(\"events\")\nplt.tight_layout()\nplt.show()\nprint(\"Plotted range:\", round(float(ev.angle.min()), 1), \"to\", round(float(ev.angle.max()), 1), \"deg; none outside the axes\")\n\n# %% [markdown]\n# **Result: reproduced.** Over all events the two most populated bins are the outer ones (-90 to\n# -75 and 75 to 90), and 11 of 12 subjects have more steep reaches (|angle| above 60 degrees)\n# than flat ones (below 30).\n\n# %% [markdown]\n# ## feature-correlations\n#\n# > Reach magnitude correlates with duration (r = 0.26) and onset speed (r = 0.56), duration with\n# > bimanual overlap (r = 0.48), and the bimanual features with each other (0.51, 0.50, 0.61).\n\n# %% tags=[\"claim:feature-correlations\"]\npairs = [(\"magnitude\", \"duration\", 0.26), (\"magnitude\", \"onset_speed\", 0.56), (\"duration\", \"bimanual_overlap\", 0.48),\n         (\"bimanual_overlap\", \"bimanual_ratio\", 0.51), (\"bimanual_class\", \"bimanual_ratio\", 0.50),\n         (\"bimanual_overlap\", \"bimanual_class\", 0.61)]\nrows = []\nfor a, b, paper in pairs:\n    r_all = ev[a].corr(ev[b])\n    r_keep = ev[pw.keep.to_numpy()][a].corr(ev[pw.keep.to_numpy()][b])\n    rows.append({\"pair\": f\"{a} / {b}\", \"paper\": paper, \"r\": r_all, \"within_10pct\": abs(r_all - paper) <= 0.1 * paper,\n                 \"r_kept_events\": r_keep, \"spearman\": stats.spearmanr(ev[a], ev[b])[0]})\ncorr = pd.DataFrame(rows)\nprint(corr.round(3).to_string(index=False))\nprint(\"Within tolerance:\", int(corr.within_10pct.sum()), \"of 6; all positive:\", bool((corr.r > 0).all()))\n\n# %% [markdown]\n# **Result: partially reproduced.** All six correlations are positive and three are within 10% of\n# the paper's (magnitude and onset speed 0.555, duration and overlap 0.459, class and ratio\n# 0.476). Magnitude and duration correlate more weakly than reported (0.137 against 0.26), and\n# overlap with ratio (0.383) and with class (0.536) are below the paper's. The events left after\n# segment rejection give the same values to two decimals.\n\n# %% [markdown]\n# ## bimanual-skew\n#\n# > Bimanual ratio and overlap are skewed toward unimanual movements, less so in subjects 02, 04\n# > and 05, while the bimanual class is mostly bimanual.\n\n# %% tags=[\"claim:bimanual-skew\"]\nprint(\"All events: median bimanual ratio\", round(float(ev.bimanual_ratio.median()), 3),\n      \"; median overlap\", round(float(ev.bimanual_overlap.median()), 3), \"s against median duration\",\n      round(float(ev.duration.median()), 3), \"s; fraction bimanual class\", round(float(ev.bimanual_class.mean()), 3))\nbs = ev.groupby(\"subject\").agg(median_ratio=(\"bimanual_ratio\", \"median\"), median_overlap=(\"bimanual_overlap\", \"median\"),\n                               bimanual_class=(\"bimanual_class\", \"mean\")).sort_values(\"median_ratio\", ascending=False)\nprint(bs.round(3).to_string())\nprint(\"Four subjects with the highest median ratio:\", sorted(bs.index[:4]))\n\n# %% [markdown]\n# **Result: partially reproduced.** Over all events the median bimanual ratio is 0.12, the median\n# overlap 0.37 s against a median duration of 1.1 s, and 67% of events are of class bimanual, as\n# stated. The four subjects with the highest median ratio are 02, 04, 05 and 06, but the claim\n# was judged on subjects 02, 04 and 05 being among them... see the output: the pooled part holds\n# and the subject part is shown above.\n\n# %% [markdown]\n# ## projection-link\n#\n# > The paper's projection matrices can be matched to the dandiset's electrodes, and regions\n# > with an average electrode density above 3 are the paper's eight.\n\n# %% tags=[\"claim:projection-link\"]\nrng_link = np.random.default_rng(55005)\n\n\ndef closeness_score(xyz, w, cen):\n    rs = []\n    for j, roi in enumerate(ajile.ROIS):\n        d = np.linalg.norm(xyz - cen.loc[roi].to_numpy(float), axis=1)\n        ok = np.isfinite(d) & (w[:, j] > 0)\n        rs.append(stats.spearmanr(-d[ok], w[ok, j])[0])\n    return float(np.median(rs))\n\n\ndensity = sum(proj[s].iloc[0] for s in subjects) / len(subjects)\nchosen = sorted(density[density > 3].index)\nprint(\"Regions with average density above 3:\", chosen)\nprint(\"Same as the paper's eight:\", chosen == sorted(ajile.ROIS))\nrows = []\nfor sub in subjects:\n    e = first[sub][\"electrodes\"]\n    m = proj[sub]\n    w = m.iloc[1:][ajile.ROIS].to_numpy(float)\n    extra = w[len(e):]\n    xyz = e[[\"x\", \"y\", \"z\"]].to_numpy(float).copy()\n    xyz[:, 0] = -np.abs(xyz[:, 0])                 # all electrodes mirrored to the left, as in the code\n    w = w[:len(e)]\n    score = closeness_score(xyz, w, centroids[sub])\n    null = [closeness_score(xyz[rng_link.permutation(len(xyz))], w, centroids[sub]) for _ in range(20)]\n    zero_rows = np.flatnonzero((m.iloc[1:len(e) + 1] == 0).all(axis=1).to_numpy())\n    rows.append({\"subject\": sub, \"matrix_rows\": len(m) - 1, \"electrodes\": len(e), \"extra_rows_all_zero\": bool((extra == 0).all()),\n                 \"score\": score, \"shuffled_max\": max(null), \"zero_weight_rows\": f\"{zero_rows.min()}-{zero_rows.max()}\" if len(zero_rows) else \"\",\n                 \"rows_without_xyz\": \",\".join(map(str, np.flatnonzero(e.x.isna().to_numpy())[[0, -1]])) if e.x.isna().any() else \"\",\n                 \"rows_without_R2\": \",\".join(map(str, np.flatnonzero(e.low_freq_R2.isna().to_numpy())[[0, -1]])) if e.low_freq_R2.isna().any() else \"\"})\nlink = pd.DataFrame(rows)\nprint(link.round(3).to_string(index=False))\nlink_ok = (link.extra_rows_all_zero & (link.score > 0.5) & (link.score > link.shuffled_max))\nprint(\"Subjects where the link holds:\", int(link_ok.sum()), \"of 12\")\n\n# %% [markdown]\n# **Result: reproduced.** In every subject the matrix has one row per electrode of the dandiset's\n# table (subject 01's four extra rows, past the table, are all zero), the eight regions selected\n# by density are the paper's, and an electrode's weight for a region follows its closeness to the\n# region's centroid (median rank correlation 0.92 to 0.97 against at most 0.17 with shuffled rows).\n# In subject 12 the electrodes with zero weight (rows 72 to 79, group AID) are not those without\n# stored R2 (rows 116 to 123, group PHD), and all have coordinates in the dandiset.\n\n# %% [markdown]\n# ## group-pattern-rois\n#\n# > At movement onset, low-frequency power decreases and high-frequency power increases, with the\n# > largest changes in the precentral, postcentral and inferior parietal regions and minimal\n# > changes in the three temporal regions.\n#\n# Set A: five events per file (seeded), all electrodes carrying 99% of every region's weight.\n# Events dropped by the segment rejection of set P are left out.\n\n# %% tags=[\"claim:group-pattern-rois\"]\nkeep_key = set(map(tuple, pw[pw.keep][[\"subject\", \"day\", \"event\"]].to_numpy()))\nsub_tfr = {}\nn_used = {}\nfor s, k, o in zip(sessions, sub_idx, out_a):\n    n = len(k)\n    good = np.array([(s[\"subject\"], s[\"day\"], int(e)) in keep_key for e in k]) & ~o[\"bad_window\"][:n]\n    sub_tfr.setdefault(s[\"subject\"], []).append(o[\"roi_tfr\"][:n][good][:, :8])\n    n_used[s[\"subject\"]] = n_used.get(s[\"subject\"], 0) + int(good.sum())\nper_subject_tfr = np.array([np.median(np.concatenate(sub_tfr[sub]), axis=0) for sub in subjects])   # subjects x regions x f x t\ngroup_tfr = per_subject_tfr.mean(axis=0)\nbands_sub = ajile.band_values(per_subject_tfr)          # subjects x regions x 2\nbands_grp = ajile.band_values(group_tfr[None])[0]\nprint(\"Events used per subject:\", n_used)\ng = pd.DataFrame(bands_grp, index=[ajile.ROI_NAMES[r] for r in ajile.ROIS], columns=[\"LFB\", \"HFB\"])\ng[\"abs_sum\"] = g.LFB.abs() + g.HFB.abs()\ng[\"subjects_LFB_below_0\"] = (bands_sub[:, :, 0] < 0).sum(axis=0)\ng[\"subjects_HFB_above_0\"] = (bands_sub[:, :, 1] > 0).sum(axis=0)\nprint(g.round(3).to_string())\nsm = [\"precentral\", \"postcentral\", \"inferior parietal\"]\ntm = [\"superior temporal\", \"middle temporal\", \"inferior temporal\"]\nsigns = bool((g.loc[sm, \"LFB\"] < 0).all() and (g.loc[sm, \"HFB\"] > 0).all())\nranking = bool(g.loc[sm, \"abs_sum\"].min() > g.loc[tm, \"abs_sum\"].max())\nprint(\"LFB < 0 and HFB > 0 in the three sensorimotor regions:\", signs,\n      \"; each larger than every temporal region:\", ranking)\n\nfig, axes = plt.subplots(2, 4, figsize=(11, 4.5), sharex=True, sharey=True)\nfor j, ax in enumerate(axes.flat):\n    im = ax.pcolormesh(ajile.TIMES, ajile.FREQS, group_tfr[j], cmap=\"RdBu_r\", vmin=-1, vmax=1, shading=\"nearest\")\n    ax.set_title(ajile.ROI_NAMES[ajile.ROIS[j]], fontsize=9)\n    ax.axvline(0, color=\"k\", lw=0.8, ls=\"--\")\nfor ax in axes[:, 0]:\n    ax.set_ylabel(\"Hz\")\nfor ax in axes[1]:\n    ax.set_xlabel(\"s from movement onset\")\nfig.colorbar(im, ax=axes, label=\"dB from baseline\", shrink=0.8)\nplt.show()\nprint(\"Plotted values range from\", round(float(group_tfr.min()), 2), \"to\", round(float(group_tfr.max()), 2),\n      \"dB; the colour scale saturates at +/-1 dB for\",\n      int((np.abs(group_tfr) > 1).sum()), \"of\", group_tfr.size, \"bins\")\n\n# %% tags=[\"claim:group-pattern-rois\"]\n# Variant: precentral value with the full projection (set A) against the 95% electrode set of\n# set P, on the same events; and the set P precentral result for those events.\nrows = []\nfor s, k, o in zip(sessions, sub_idx, out_a):\n    n = len(k)\n    full = ajile.band_values(o[\"roi_tfr\"][:n, 0])\n    trunc = ajile.band_values(o[\"roi_tfr\"][:n, 8])\n    rows.append(pd.DataFrame({\"lfb_full\": full[:, 0], \"lfb_95\": trunc[:, 0], \"hfb_full\": full[:, 1], \"hfb_95\": trunc[:, 1]}))\ntv = pd.concat(rows)\nprint(\"Precentral, full weights against the 95% electrode set, same events (n = %d):\" % len(tv))\nprint(\"  LFB r = %.3f, median difference %.3f dB; HFB r = %.3f, median difference %.3f dB\" % (\n    tv.lfb_full.corr(tv.lfb_95), (tv.lfb_full - tv.lfb_95).median(), tv.hfb_full.corr(tv.hfb_95), (tv.hfb_full - tv.hfb_95).median()))\n\n# %% [markdown]\n# **Result: reproduced.** Averaged over subjects, LFB power falls and HFB power rises from 0 to\n# 0.5 s in the precentral, postcentral and inferior parietal regions, and each of these changes\n# more than any temporal region. The pattern rests on five events per file, about 23 per subject.\n\n# %% [markdown]\n# ## precentral-subject-ci\n#\n# > Precentral LFB and HFB power from 0 to 0.5 s differ between subjects as given by their 95%\n# > confidence intervals in Table 1.\n\n# %% tags=[\"claim:precentral-subject-ci\"]\nTABLE1 = {  # subject: (LFB low, LFB high, HFB low, HFB high), Table 1\n    \"01\": (-1.87, -1.29, 0.03, 0.23), \"02\": (-1.12, -0.31, 0.07, 0.64), \"03\": (-2.11, -1.73, 1.39, 1.67),\n    \"04\": (-0.17, 0.01, 0.32, 0.52), \"05\": (-0.7, -0.38, 0.2, 0.48), \"06\": (-1.63, -1.11, 2.02, 2.37),\n    \"07\": (-0.84, -0.51, 1.14, 1.34), \"08\": (-0.3, 0.04, 0.36, 0.63), \"09\": (-0.57, -0.08, -0.11, 0.23),\n    \"10\": (-0.87, -0.35, 0.01, 0.3), \"11\": (-2.3, -1.86, 0.09, 0.34), \"12\": (-0.66, -0.44, 0.06, 0.2)}\nrng_boot = np.random.default_rng(55004)\nkept = pw[pw.keep]\nrows = []\nfor sub in subjects:\n    g = kept[kept.subject == sub]\n    for band, col, lo, hi in ((\"LFB\", \"lfb\", TABLE1[sub][0], TABLE1[sub][1]), (\"HFB\", \"hfb\", TABLE1[sub][2], TABLE1[sub][3])):\n        x = g[col].to_numpy()\n        boot = rng_boot.choice(x, (2000, len(x)))\n        rows.append({\"subject\": sub, \"band\": band, \"n\": len(x), \"paper_lo\": lo, \"paper_hi\": hi,\n                     \"mean\": x.mean(), \"median\": np.median(x),\n                     \"mean_ci\": f\"{np.percentile(boot.mean(1), 2.5):.2f} to {np.percentile(boot.mean(1), 97.5):.2f}\",\n                     \"median_ci\": f\"{np.percentile(np.median(boot, 1), 2.5):.2f} to {np.percentile(np.median(boot, 1), 97.5):.2f}\",\n                     \"mean_in\": lo <= x.mean() <= hi, \"median_in\": lo <= np.median(x) <= hi})\nci = pd.DataFrame(rows)\nprint(ci.round(2).to_string(index=False))\nprint(\"Inside the paper's interval: mean\", int(ci.mean_in.sum()), \"of 24; median\", int(ci.median_in.sum()), \"of 24\")\nfor band in (\"LFB\", \"HFB\"):\n    c = ci[ci.band == band]\n    centre = (c.paper_lo + c.paper_hi) / 2\n    print(f\"{band}: Spearman r across subjects, median against interval centre {stats.spearmanr(c['median'], centre)[0]:.3f}, \"\n          f\"mean against centre {stats.spearmanr(c['mean'], centre)[0]:.3f}\")\n\n# %% tags=[\"claim:precentral-subject-ci\"]\n# Variants: without the segment rejection; without the three late-starting files.\nfor label, mask in ((\"no segment rejection\", ~pw.bad_window),\n                    (\"without the three late-starting files\", pw.keep & ~pw.set_index([\"subject\", \"day\"]).index.isin(\n                        [(s[\"subject\"], s[\"day\"]) for s in sessions if s[\"ecog_offset\"] > 0]))):\n    g = pw[mask].groupby(\"subject\")[[\"lfb\", \"hfb\"]].median()\n    inside = sum(TABLE1[s][0] <= g.loc[s, \"lfb\"] <= TABLE1[s][1]) + sum(TABLE1[s][2] <= g.loc[s, \"hfb\"] <= TABLE1[s][3]) for s in subjects)\n    print(f\"{label}: medians inside the paper's interval for {inside} of 24\")\n\n# %% [markdown]\n# **Result: partially reproduced.** Of the 24 subject and band values, 14 medians and 14 means\n# fall inside the paper's 95% intervals. The values follow the paper's ordering of subjects\n# closely (Spearman r of the medians against the interval centres in the output above), but\n# several subjects fall outside their narrow intervals.\n\n# %% [markdown]\n# ## precentral-subjects-differ\n#\n# > Precentral LFB and HFB power from 0 to 0.5 s differ across subjects (Kruskal-Wallis,\n# > p < 0.001 for both bands).\n\n# %% tags=[\"claim:precentral-subjects-differ\"]\nfor band in (\"lfb\", \"hfb\"):\n    groups = [g[band].to_numpy() for _, g in kept.groupby(\"subject\")]\n    h, p = stats.kruskal(*groups)\n    print(f\"{band.upper()}: H = {h:.1f}, p = {p:.2e}, eta2_H = {(h - 11) / (len(kept) - 12):.3f}, n = {len(kept)}\")\nprint(\"Paper's code printed p = 2.1e-159 (LFB) and 2.4e-278 (HFB).\")\n\n# %% [markdown]\n# **Result: reproduced.** Precentral power differs across subjects in both bands with p far below\n# 0.001.\n\n# %% [markdown]\n# ## precentral-day-effects\n#\n# > Precentral power depends on the recording day in several subjects; significant in LFB for\n# > 03, 05, 06, 07, 08 and 11, and in HFB for 03, 04, 07, 08 and 10.\n\n# %% tags=[\"claim:precentral-day-effects\"]\nPAPER_DAY_SIG = {\"lfb\": {\"03\", \"05\", \"06\", \"07\", \"08\", \"11\"}, \"hfb\": {\"03\", \"04\", \"07\", \"08\", \"10\"}}\n\n\ndef day_tests(frame):\n    rows = []\n    for sub in subjects:\n        g = frame[frame.subject == sub]\n        for band in (\"lfb\", \"hfb\"):\n            p = stats.kruskal(*[d[band].to_numpy() for _, d in g.groupby(\"day\")])[1]\n            rows.append({\"subject\": sub, \"band\": band, \"p\": p, \"significant\": p < 0.05,\n                         \"paper\": sub in PAPER_DAY_SIG[band]})\n    t = pd.DataFrame(rows)\n    t[\"agree\"] = t.significant == t.paper\n    return t\n\n\ndt = day_tests(kept)\nprint(dt.pivot(index=\"subject\", columns=\"band\", values=[\"p\", \"significant\", \"paper\"]).to_string(\n    formatters={(\"p\", \"lfb\"): \"{:.2e}\".format, (\"p\", \"hfb\"): \"{:.2e}\".format}))\nprint(\"Calls that agree with the paper:\", int(dt.agree.sum()), \"of 24; significant subjects, LFB\",\n      int(dt[dt.band == \"lfb\"].significant.sum()), \", HFB\", int(dt[dt.band == \"hfb\"].significant.sum()))\nfor label, mask in ((\"no segment rejection\", ~pw.bad_window), ):\n    v = day_tests(pw[mask])\n    print(f\"Variant, {label}: {int(v.agree.sum())} of 24 agree\")\nday_means = kept.groupby([\"subject\", \"day\"])[[\"lfb\", \"hfb\"]].median().round(2)\nprint(\"\\nMedian per subject and day (dB):\")\nprint(day_means.unstack(\"day\").to_string())\n\n# %% [markdown]\n# **Result: partially reproduced.** Recording day has a significant effect in several subjects in\n# both bands, and 16 of the 24 subject and band calls agree with the paper's.\n\n# %% [markdown]\n# ## baseline-reduces-day-variability\n#\n# > Baseline subtraction reduces the variability of LFB and HFB power across recording days, but\n# > clear variability remains.\n\n# %% tags=[\"claim:baseline-reduces-day-variability\"]\nrows = []\nfor sub in subjects:\n    g = kept[kept.subject == sub].groupby(\"day\")\n    rows.append({\"subject\": sub,\n                 \"lfb_sd_subtracted\": g.lfb.mean().std(), \"lfb_sd_raw\": g.lfb_raw.mean().std(),\n                 \"hfb_sd_subtracted\": g.hfb.mean().std(), \"hfb_sd_raw\": g.hfb_raw.mean().std()})\nbv = pd.DataFrame(rows).set_index(\"subject\")\nprint(bv.round(3).to_string())\nfor band in (\"lfb\", \"hfb\"):\n    lower = (bv[f\"{band}_sd_subtracted\"] < bv[f\"{band}_sd_raw\"]).sum()\n    print(f\"{band.upper()}: lower with subtraction in {lower} of 12 subjects; median ratio \"\n          f\"{(bv[f'{band}_sd_subtracted'] / bv[f'{band}_sd_raw']).median():.3f}; all above 0: {bool((bv[f'{band}_sd_subtracted'] > 0).all())}\")\n\n# %% [markdown]\n# **Result: reproduced.** In both bands the SD across days is lower with baseline subtraction in\n# most subjects, and it stays above 0 in every subject.\n\n# %% [markdown]\n# ## Regression (Figure 6)\n#\n# For each subject, the up to eight good electrodes of set P with the largest precentral weight;\n# LFB and HFB power of each electrode (baseline-subtracted, median over 0 to 0.5 s and the band)\n# for the kept events; the code's design matrix and forward selection; Huber regression over 40\n# random day-balanced splits with 90% of events for training (the Methods; the code uses 80%, shown\n# as a variant with 10 splits). The paper uses 200 splits.\n\n# %%\nreg_tasks, reg_keys = [], []\nfor sub in subjects:\n    ss = [(s, t, o) for s, t, o in zip(sessions, tasks_p, out_p) if s[\"subject\"] == sub]\n    ch = ss[0][1][\"channels\"]\n    good0 = first[sub][\"electrodes\"].good.to_numpy()\n    order = [c for c in ch[np.argsort(-w_all[sub][ch, 0])] if good0[c]][:8]\n    bands = np.concatenate([o[\"bands\"] for _, _, o in ss])           # events x channels x 2\n    mask = pw[pw.subject == sub].keep.to_numpy()\n    evs = ev[ev.subject == sub][mask].reset_index(drop=True)\n    x, names, groups = ajile.design(evs)\n    for c in order:\n        j = int(np.flatnonzero(ch == c)[0])\n        for b, band in enumerate((\"LFB\", \"HFB\")):\n            for per_train, n_splits, label in ((0.9, 40, \"methods\"), (0.8, 10, \"code\")):\n                reg_tasks.append({\"x\": x, \"y\": bands[mask, j, b], \"groups\": groups, \"days\": evs.day.to_numpy(),\n                                  \"per_train\": per_train, \"n_splits\": n_splits,\n                                  \"seed\": 55003 + len(reg_tasks)})\n                reg_keys.append((sub, int(c), band, label))\nstarted = time.time()\nreg_out = ajile.run_regressions(reg_tasks)\nprint(f\"{len(reg_tasks)} models, {sum(r['n_fits'] for r in reg_out)} Huber fits in {time.time() - started:.0f} s; \"\n      f\"fits that did not converge: {sum(r['unconverged'] for r in reg_out)}\")\nreg = pd.DataFrame([{\"subject\": k[0], \"electrode\": k[1], \"band\": k[2], \"split\": k[3], \"r2_test\": r[\"r2_test\"],\n                     \"r2_train\": r[\"r2_train\"], \"coef_angle\": r[\"coef_angle\"],\n                     **{f\"dm_{f}\": v for f, v in r[\"delta_methods\"].items()},\n                     **{f\"dc_{f}\": v for f, v in r[\"delta_code\"].items()},\n                     **{f\"ret_{f}\": v for f, v in r[\"retained\"].items()}} for k, r in zip(reg_keys, reg_out)])\nmain = reg[reg.split == \"methods\"]\nprint(\"Electrodes tested per subject:\", main[main.band == \"LFB\"].groupby(\"subject\").size().to_dict())\n\n# %% [markdown]\n# ## regression-r2-max\n#\n# > Regression models explain at most 25% of the variance of withheld events.\n\n# %% tags=[\"claim:regression-r2-max\"]\nprint(\"Mean test R2 over splits, tested electrodes:\")\nprint(main.groupby(\"band\").r2_test.describe().round(3).to_string())\nprint(\"Largest:\", round(float(main.r2_test.max()), 3), \"at\", main.loc[main.r2_test.idxmax(), [\"subject\", \"electrode\", \"band\"]].to_dict())\nprint(\"Code's split (80/20, 10 splits): largest\", round(float(reg[reg.split == \"code\"].r2_test.max()), 3))\nstored = []\nfor _, r in main.iterrows():\n    e = first[r.subject][\"electrodes\"]\n    stored.append(e.low_freq_R2.iloc[r.electrode] if r.band == \"LFB\" else e.high_freq_R2.iloc[r.electrode])\nmain = main.assign(stored_r2=stored)\nfor band in (\"LFB\", \"HFB\"):\n    m = main[main.band == band]\n    print(f\"{band}: recomputed against stored R2 on the same electrodes, Pearson r = {m.r2_test.corr(m.stored_r2):.3f}, \"\n          f\"median recomputed {m.r2_test.median():.3f}, median stored {m.stored_r2.median():.3f}\")\nall_stored = pd.concat([first[s][\"electrodes\"][[\"low_freq_R2\", \"high_freq_R2\"]] for s in subjects])\nprint(\"Stored R2 over all electrodes: largest LFB\", round(float(all_stored.low_freq_R2.max()), 3),\n      \", HFB\", round(float(all_stored.high_freq_R2.max()), 3))\n\n# %% [markdown]\n# **Result: reproduced.** The largest recomputed mean test R2 is below 0.275 in both bands. The\n# stored R2 values, which cover every electrode, reach 0.255 (HFB, subject 04).\n\n# %% [markdown]\n# ## regression-r2-sensorimotor\n#\n# > The models with the largest R2 on withheld data are in frontoparietal sensorimotor areas.\n#\n# On the R2 values stored in the dandiset for every electrode, projected onto the regions.\n\n# %% tags=[\"claim:regression-r2-sensorimotor\"]\nrows = []\nfor sub in subjects:\n    e = first[sub][\"electrodes\"]\n    for band, col in ((\"LFB\", \"low_freq_R2\"), (\"HFB\", \"high_freq_R2\")):\n        r2 = e[col].to_numpy(float)\n        good = e.good.to_numpy() & np.isfinite(r2)\n        w = ajile.roi_weights(proj[sub], len(e), good)\n        rows.append({\"subject\": sub, \"band\": band, **dict(zip([ajile.ROI_NAMES[r] for r in ajile.ROIS], np.nan_to_num(r2) @ w))})\npr = pd.DataFrame(rows)\nreg_roi = pr.groupby(\"band\")[[ajile.ROI_NAMES[r] for r in ajile.ROIS]].mean().T\nprint(reg_roi.round(4).to_string())\nfp = [\"precentral\", \"postcentral\", \"middle frontal\", \"inferior parietal\", \"supramarginal\"]\nfor band in (\"LFB\", \"HFB\"):\n    top = reg_roi[band].idxmax()\n    print(f\"{band}: highest region {top}; frontoparietal mean {reg_roi.loc[fp, band].mean():.4f}, \"\n          f\"temporal mean {reg_roi.loc[tm, band].mean():.4f}\")\nprint(\"Electrodes with stored R2 > 0.05: LFB\", int((all_stored.low_freq_R2 > 0.05).sum()), \", HFB\", int((all_stored.high_freq_R2 > 0.05).sum()))\n\n# %% [markdown]\n# **Result: reproduced.** In both bands the projected stored R2 is highest in a frontoparietal\n# region and the frontoparietal mean exceeds the temporal mean. This uses the stored R2 values,\n# not a recomputation.\n\n# %% [markdown]\n# ## regression-angle-day-top\n#\n# > Reach angle and recording day are the most explanatory features, especially for\n# > low-frequency power.\n\n# %% tags=[\"claim:regression-angle-day-top\"]\nwell = main[main.band == \"LFB\"].set_index([\"subject\", \"electrode\"]).r2_test > 0.05\nwell_keys = set(well[well].index)\nsel = main[[(s, e) in well_keys for s, e in zip(main.subject, main.electrode)]]\nprint(\"Electrodes with mean LFB test R2 > 0.05:\", len(well_keys), \"of\", len(well), \"; by subject:\",\n      pd.Series([k[0] for k in well_keys]).value_counts().sort_index().to_dict())\nfeats = ajile.REG_FEATURES\nfor prefix, label in ((\"dm_\", \"Methods (unshuffled test events)\"), (\"dc_\", \"code (shuffled test events)\")):\n    t = sel.groupby(\"band\")[[prefix + f for f in feats]].mean().T\n    t.index = feats\n    print(f\"\\nMean Delta R2, {label}:\")\n    print(t.round(4).to_string())\n    print(\"Two largest in LFB:\", list(t[\"LFB\"].sort_values(ascending=False).index[:2]),\n          \"; in HFB:\", list(t[\"HFB\"].sort_values(ascending=False).index[:2]))\nt_all = main.groupby(\"band\")[[\"dm_\" + f for f in feats]].mean().T\nt_all.index = feats\nprint(\"\\nVariant, all tested electrodes (Methods):\", \"LFB top two\", list(t_all[\"LFB\"].sort_values(ascending=False).index[:2]))\nt_code = reg[(reg.split == \"code\")].groupby(\"band\")[[\"dc_\" + f for f in feats]].mean().T\nt_code.index = feats\nprint(\"Variant, code's split and scoring, all tested electrodes: LFB top two\", list(t_code[\"LFB\"].sort_values(ascending=False).index[:2]))\n\n# %% [markdown]\n# **Result: partially reproduced.** On the well-fit electrodes, recording day is among the two\n# features with the largest mean Delta R2 for LFB, and reach angle is not.\n\n# %% [markdown]\n# ## regression-angle-coefficient\n#\n# > Upward reaches are associated with decreased low-frequency and increased high-frequency\n# > power.\n\n# %% tags=[\"claim:regression-angle-coefficient\"]\nc = sel.groupby(\"band\").coef_angle.agg([\"mean\", \"median\", \"count\", lambda x: (x < 0).mean()])\nc.columns = [\"mean\", \"median\", \"n\", \"fraction_negative\"]\nprint(c.round(4).to_string())\nfor band in (\"LFB\", \"HFB\"):\n    x = sel[sel.band == band].coef_angle\n    print(f\"{band}: Wilcoxon against 0, p = {stats.wilcoxon(x)[1]:.3g}\")\nprint(\"All tested electrodes:\", main.groupby(\"band\").coef_angle.mean().round(4).to_dict())\n\n# %% [markdown]\n# **Result: reproduced.** On the well-fit electrodes the mean reach angle coefficient is negative\n# for LFB and positive for HFB: upward reaches deepen the LFB decrease and raise the HFB increase.\n\n# %% [markdown]\n# ## regression-angle-retained\n#\n# > Reach angle is the feature most often retained by forward selection in sensorimotor areas.\n\n# %% tags=[\"claim:regression-angle-retained\"]\nret = main[[\"ret_\" + f for f in feats]].mean()\nret.index = feats\nprint(\"Fraction of models (tested electrodes, both bands) retaining each feature:\")\nprint(ret.sort_values(ascending=False).round(3).to_string())\nprint(\"\\nBy band:\")\nrb = main.groupby(\"band\")[[\"ret_\" + f for f in feats]].mean().T\nrb.index = feats\nprint(rb.round(3).to_string())\n\n# %% [markdown]\n# **Result: reproduced.** Reach angle is the feature most often retained by forward selection.\n\n# %% [markdown]\n# ## Summary\n\n# %%\nprint(f\"Notebook ran in {(time.time() - started) / 60:.1f} min since the last timer; total cells above.\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('''    inside = sum(TABLE1[s][0] <= g.loc[s, "lfb"] <= TABLE1[s][1]) + sum(TABLE1[s][2] <= g.loc[s, "hfb"] <= TABLE1[s][3]) for s in subjects)''','''    inside = sum(int(TABLE1[s][0] <= g.loc[s, "lfb"] <= TABLE1[s][1]) + int(TABLE1[s][2] <= g.loc[s, "hfb"] <= TABLE1[s][3])
                 for s in subjects)''')
s=s.replace('''started = time.time()
sessions = ajile.load_all()''','''nb_started = started = time.time()
sessions = ajile.load_all()''')
s=s.replace('''print(f"Notebook ran in {(time.time() - started) / 60:.1f} min since the last timer; total cells above.")''','''print(f"Notebook ran in {(time.time() - nb_started) / 60:.1f} min.")''')
old=s[s.index('late = [i for i, s in enumerate(sessions) if s["ecog_offset"] > 0]'):s.index('print(pd.DataFrame(rows).round(2).to_string(index=False))')]
new='''late = [i for i, s in enumerate(sessions) if s["ecog_offset"] > 0]
clock_tasks, clock_rows = [], []
for i in late:
    s = sessions[i]
    t = s["reaches"].start_time.to_numpy()
    for name, tt in (("stored times", t), ("corrected times", t - s["ecog_offset"]),
                     ("stored + 30 s", t + 30), ("corrected + 30 s", t - s["ecog_offset"] + 30)):
        inside = np.flatnonzero((tt > 3) & (tt < s["ecog_shape"][0] / ajile.FS - 3))[:40]
        clock_tasks.append({**tasks_p[i], "times": tt[inside]})
        clock_rows.append({"file": f"{s['subject']} day {s['day']}", "times": name, "events": len(inside)})
rows = []
for r, o in zip(clock_rows, ajile.run_power(clock_tasks)):
    b = ajile.band_values(o["roi_tfr"][:, 0])
    rows.append({**r, "LFB": np.median(b[:, 0]), "HFB": np.median(b[:, 1])})
'''
s=s.replace(old,new)
import re
# placeholder conclusions
parts=s.split('\n# %% [markdown]\n')
out=[parts[0]]
for p in parts[1:]:
    if p.startswith('# **Result:'):
        p='# **Result: TBD.**\n'
    out.append(p)
s='\n# %% [markdown]\n'.join(out)
open('nb_src.py','w').write(s)
print(s.count('Result: TBD'))
EOF
cat > $TMPDIR/py2nb.py <<'EOF'
import sys, re, nbformat
src=open(sys.argv[1]).read()
cells=[]
blocks=re.split(r'^# %%(.*)$', src, flags=re.M)
# blocks: [pre, header1, body1, header2, body2...]
for h,b in zip(blocks[1::2], blocks[2::2]):
    b=b.strip('\n')
    if '[markdown]' in h:
        text='\n'.join(l[2:] if l.startswith('# ') else l[1:] if l.startswith('#') else l for l in b.split('\n'))
        cells.append(nbformat.v4.new_markdown_cell(text))
    else:
        m=re.search(r'tags=(\[.*\])',h)
        c=nbformat.v4.new_code_cell(b)
        if m: c.metadata['tags']=eval(m.group(1))
        cells.append(c)
nb=nbformat.v4.new_notebook(); nb.cells=cells
nb.metadata['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
nbformat.write(nb,sys.argv[2])
print(len(cells))
EOF
python3 -c "import nbformat" 2>/dev/null || pip install -q nbformat pyyaml jsonschema; python3 $TMPDIR/py2nb.py $TMPDIR/nb_src.py entries/000055-peterson-2021/reproduce_peterson_2021.ipynb
```

```
21
92
Shell cwd was reset to
```

**Agent**

Now `entry.yaml` and `requirements.in`, then lock and run:

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && cat > requirements.in <<'EOF'
dandi
h5py
matplotlib
numpy
pandas
remfile
requests
scikit-learn
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000055-peterson-2021
type: reproduction
title: Behavioral and neural variability of naturalistic arm movements (Peterson, Singh et al. 2021)
description: Tests the findings of Peterson, Singh, Wang, Rao and Brunton (2021) on dandiset 000055
  (AJILE12), which holds the long-term ECoG, upper-body pose and wrist movement events of 12
  subjects during clinical epilepsy monitoring. It checks the subjects, electrodes and events, the
  distributions and correlations of the behavioural features, the movement-related spectral power
  in eight cortical regions and in the precentral region per subject and day, and the regression of
  single-event power on the behavioural features.
license: Apache-2.0
notebooks:
- path: reproduce_peterson_2021.ipynb
  title: Reproducing Peterson, Singh et al. (2021) from dandiset 000055
  runtime_minutes: 12
helpers:
- ajile.py
related:
- id: dandi:000055/0.220127.0436
  relation: uses_data
- id: doi:10.1523/eneuro.0007-21.2021
  relation: reproduces
EOF
cd ../.. && python -c "import yaml,jsonschema,nbformat" && python tools/entry.py lock entries/000055-peterson-2021 && python tools/entry.py check entries/000055-peterson-2021
```

```
wrote entries/000055-peterson-2021/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py run entries/000055-peterson-2021 2>&1 | tail -30
```

```
# Variant: precentral value with the full projection (set A) against the 95% electrode set of
# set P, on the same events; and the set P precentral result for those events.
rows = []
for s, k, o in zip(sessions, sub_idx, out_a):
    n = len(k)
    full = ajile.band_values(o["roi_tfr"][:n, 0])
    trunc = ajile.band_values(o["roi_tfr"][:n, 8])
    rows.append(pd.DataFrame({"lfb_full": full[:, 0], "lfb_95": trunc[:, 0], "hfb_full": full[:, 1], "hfb_95": trunc[:, 1]}))
tv = pd.concat(rows)
print("Precentral, full weights against the 95% electrode set, same events (n = %d):" % len(tv))
print("  LFB r = %.3f, median difference %.3f dB; HFB r = %.3f, median difference %.3f dB" % (
    tv.lfb_full.corr(tv.lfb_95), (tv.lfb_full - tv.lfb_95).median(), tv.hfb_full.corr(tv.hfb_95), (tv.hfb_full - tv.hfb_95).median()))
------------------


[31m---------------------------------------------------------------------------[39m
[31mTypeError[39m                                 Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[24][39m[32m, line 10[39m
[32m      6[39m     full = ajile.band_values(o[[33m"roi_tfr"[39m][:n, [32m0[39m])
[32m      7[39m     trunc = ajile.band_values(o[[33m"roi_tfr"[39m][:n, [32m8[39m])
[... 14 more lines not kept]
```

**Agent**

A format-string bug (`%` inside the text). To find any remaining errors in one pass, I'll run the notebook with errors allowed in my exploration environment.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('''print("Precentral, full weights against the 95% electrode set, same events (n = %d):" % len(tv))
print("  LFB r = %.3f, median difference %.3f dB; HFB r = %.3f, median difference %.3f dB" % (
    tv.lfb_full.corr(tv.lfb_95), (tv.lfb_full - tv.lfb_95).median(), tv.hfb_full.corr(tv.hfb_95), (tv.hfb_full - tv.hfb_95).median()))''','''print(f"Precentral, full weights against the 95% electrode set, same events (n = {len(tv)}):")
print(f"  LFB r = {tv.lfb_full.corr(tv.lfb_95):.3f}, median difference {(tv.lfb_full - tv.lfb_95).median():.3f} dB; "
      f"HFB r = {tv.hfb_full.corr(tv.hfb_95):.3f}, median difference {(tv.hfb_full - tv.hfb_95).median():.3f} dB")''')
open('nb_src.py','w').write(s)
EOF
python3 py2nb.py nb_src.py entries/000055-peterson-2021/reproduce_peterson_2021.ipynb && . expl/bin/activate && uv pip install -q nbconvert ipykernel 2>&1 | tail -1; cd entries/000055-peterson-2021 && time jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3600 --output-dir $TMPDIR/exec reproduce_peterson_2021.ipynb 2>&1 | tail -3
```

```
92
[NbConvertApp] Converting notebook reproduce_peterson_2021.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 264301 bytes to /tmp/claude-1001/exec/reproduce_peterson_2021.ipynb

real	8m55.927s
user	27m54.749s
sys	3m44.977s
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/exec/reproduce_peterson_2021.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': 
        continue
    print(f'===== [{i}] {c.metadata.get("tags","")} {c.source[:70]!r}')
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[:6000])
        elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
        elif 'text/plain' in o.get('data',{}): print(o['data']['text/plain'][:500])
EOF
```

```
<persisted-output>
Output too large (45KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e4dcc5c4-cdf8-4de0-938c-c8b39ed4937d/tool-results/bnudotir6.txt

Preview (first 2KB):
===== [1]  'import os\nimport time\nimport warnings\n\nos.environ.setdefault("OMP_NUM_'
loaded 55 files of dandiset 000055 version 0.220127.0436, 8088 events, projection matrices for 12 subjects, in 29 s

===== [3] ['sanity'] 'files = pd.DataFrame([{\n    "subject": s["subject"], "day": s["day"], '
subject  day                    session_start  ecog_hours  channels  ecog_rate      chunk  pose_hours  events event_wrist hemisphere  offset_h
     01    3        2000-01-02T19:00:00-05:00       24.00        94      500.0 (84375, 1)        24.0     156     r_wrist          L     0.000
     01    4        2000-01-03T19:00:00-05:00       24.00        94      500.0 (84375, 1)        24.0     196     r_wrist          L     0.000
     01    5        2000-01-04T19:00:00-05:00       24.00        94      500.0 (84375, 1)        24.0     199     r_wrist          L     0.000
     01    7 2000-01-07T03:31:22.414000-05:00       15.48        94      500.0 (54412, 1)        24.0     190     r_wrist          L     8.523
     02    3        2000-01-02T19:00:00-05:00       24.00        86      500.0 (84375, 1)        24.0      51     l_wrist          R     0.000
     02    4        2000-01-03T19:00:00-05:00       24.00        86      500.0 (84375, 1)        24.0      94     l_wrist          R     0.000
     02    5        2000-01-04T19:00:00-05:00       24.00        86      500.0 (84375, 1)        24.0      82     l_wrist          R     0.000
     02    6        2000-01-05T19:00:00-05:00       24.00        86      500.0 (84375, 1)        24.0      78     l_wrist          R     0.000
     03    3        2000-01-02T19:00:00-05:00       24.00        96      500.0 (84375, 1)        24.0     198     r_wrist          L     0.000
     03    4        2000-0
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e4dcc5c4-cdf8-4de0-938c-c8b39ed4937d/tool-results/bnudotir6.txt",
 "offset": 60,
 "limit": 700
}
```

```
60	     03    6          96             96     16      16   17         16   unknown     True      0.146      0.140      16
61	     04    3          84             84      0       0   17          0   unknown     True      0.037      0.255       0
62	     04    4          84             84      0       0    4          0   unknown     True      0.037      0.255       0
63	     04    5          84             84      0       0    3          0   unknown     True      0.037      0.255       0
64	     04    6          84             84      0       0    2          0   unknown     True      0.037      0.255       0
65	     04    7          84             84      0       0    7          0   unknown     True      0.037      0.255       0
66	     05    3         106            106      0       0    2          0   unknown     True      0.059      0.064       0
67	     05    4         106            106      0       0    2          0   unknown     True      0.059      0.064       0
68	     05    7         106            106      0       0    6          0   unknown     True      0.059      0.064       0
69	     06    3          80             80      0       0   10          0   unknown     True      0.039      0.055       0
70	     06    4          80             80      0       0   10          0   unknown     True      0.039      0.055       0
71	     06    5          80             80      0       0    4          0   unknown     True      0.039      0.055       0
72	     06    6          80             80      0       0    6          0   unknown     True      0.039      0.055       0
73	     06    7          80             80      0       0    1          0   unknown     True      0.039      0.055       0
74	     07    3          64             64      0       0    1          0   unknown     True      0.032      0.095       0
75	     07    4          64             64      0       0    1          0   unknown     True      0.032      0.095       0
76	     07    5          64     
[... 526 more lines not kept]
```

**Agent**

Everything ran in 8.8 min with no errors. Reading the first part of the outputs to check the data-check text against them:

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e4dcc5c4-cdf8-4de0-938c-c8b39ed4937d/tool-results/bnudotir6.txt",
 "offset": 55,
 "limit": 5
}
```

```
55	     02    5          86             86     16       0    5          1   unknown     True      0.016      0.032       0
56	     02    6          86             86     16       0    6          1   unknown     True      0.016      0.032       0
57	     03    3          96             96     16      16   17         16   unknown     True      0.146      0.140      16
58	     03    4          96             96     16      16   25         16   unknown     True      0.146      0.140      16
59	     03    5          96             96     16      16   20         16   unknown     True      0.146      0.140      16
```

**Agent calls Bash**

```bash
sed -n 1,50p /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e4dcc5c4-cdf8-4de0-938c-c8b39ed4937d/tool-results/bnudotir6.txt | cut -c1-400 | sed -n '1,4p;56,200p'; grep -n "Archive summary\|Subject fields\|Species in\|Dandiset metadata\|ECoG unit\|ECoG starting\|Other acquisition\|Event timestamps\|Groups and\|identical\|^01 {\|^03 {\|^12 {" /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e4dcc5c4-cdf8-4de0-938c-c8b39ed4937d/tool-results/bnudotir6.txt | cut -c1-700
```

```
===== [1]  'import os\nimport time\nimport warnings\n\nos.environ.setdefault("OMP_NUM_'
loaded 55 files of dandiset 000055 version 0.220127.0436, 8088 events, projection matrices for 12 subjects, in 29 s

===== [3] ['sanity'] 'files = pd.DataFrame([{\n    "subject": s["subject"], "day": s["day"], '
148:File pairs with identical electrode SDs or identical event tables: none
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/exec/reproduce_peterson_2021.ipynb',4)
for i in (3,5):
    t=''.join(o.text for o in nb.cells[i].outputs if o.output_type=='stream')
    print(t[-3500:] if i==3 else t[-2600:])
EOF
```

```
_wrist          L     0.000
     09    4        2000-01-03T19:00:00-05:00       24.00       126      500.0 (84375, 1)        24.0      18     r_wrist          L     0.000
     09    5        2000-01-04T19:00:00-05:00       24.00       126      500.0 (84375, 1)        24.0     109     r_wrist          L     0.000
     09    6        2000-01-05T19:00:00-05:00       24.00       126      500.0 (84375, 1)        24.0      38     r_wrist          L     0.000
     09    7        2000-01-06T19:00:00-05:00       24.00       126      500.0 (84375, 1)        24.0      31     r_wrist          L     0.000
     10    3        2000-01-02T19:00:00-05:00       24.00       126      500.0 (84375, 1)        24.0     184     r_wrist          L     0.000
     10    4        2000-01-03T19:00:00-05:00       24.00       126      500.0 (84375, 1)        24.0     154     r_wrist          L     0.000
     10    5        2000-01-04T19:00:00-05:00       24.00       126      500.0 (84375, 1)        24.0     112     r_wrist          L     0.000
     10    6        2000-01-05T19:00:00-05:00       24.00       126      500.0 (84375, 1)        24.0     157     r_wrist          L     0.000
     10    7        2000-01-06T19:00:00-05:00       24.00       126      500.0 (84375, 1)        24.0     199     r_wrist          L     0.000
     11    3        2000-01-02T19:00:00-05:00       24.00       106      500.0 (84375, 1)        24.0     199     r_wrist          L     0.000
     11    4        2000-01-03T19:00:00-05:00       24.00       106      500.0 (84375, 1)        24.0     194     r_wrist          L     0.000
     11    5        2000-01-04T19:00:00-05:00       24.00       106      500.0 (84375, 1)        24.0     195     r_wrist          L     0.000
     11    6        2000-01-05T19:00:00-05:00       24.00       106      500.0 (84375, 1)        24.0     198     r_wrist          L     0.000
     11    7        2000-01-06T19:00:00-05:00       24.00       106      500.0 (84375, 1)        24.0     196    
[... 29 more lines not kept]
```

**Agent**

One surprise: in some file the `ReachEvents` timestamps differ from the reaches `start_time` by exactly 86400 s. Finding which:

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && python - <<'EOF'
import pickle,numpy as np
res=pickle.load(open('/tmp/claude-1001/meta_all.pkl','rb'))
for info,rd,*_ in res:
    d=info['ev_ts']-rd.start_time.values
    if np.abs(d).max()>0.01:
        bad=np.flatnonzero(np.abs(d)>0.01)
        print(info['subject'],info['session'],len(bad),'of',len(d), d[bad][:5], rd.start_time.values[bad][:5], info['ev_ts'][bad][:5])
EOF
```

```
01 7 190 of 190 [-30682.415 -30682.414 -30682.415 -30682.414 -30682.414] [32313.385 32323.618 32800.671 33043.112 33113.332] [1630.97  1641.204 2118.256 2360.698 2430.918]
04 3 35 of 35 [-30048.322 -30048.323 -30048.323 -30048.322 -30048.322] [49319.452 50646.161 50689.061 51076.188 52141.924] [19271.13  20597.838 20640.738 21027.866 22093.602]
06 3 166 of 166 [-29240.567 -29240.567 -29240.567 -29240.566 -29240.566] [29754.283 29785.583 31504.309 31518.476 31736.916] [ 513.716  545.016 2263.742 2277.91  2496.35 ]
08 4 1 of 197 [-86400.] [86440.332] [40.332]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_src.py').read()
def rep(a,b):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b)
rep('''print("Other acquisition series and their descriptions:", sorted({(k, v) for s in sessions for k, v in s["acquisition"].items() if k != "ElectricalSeries"}))
print("Event timestamps equal reaches start_time (max difference, s):",
      max(float(np.max(np.abs(s["event_times"] - s["reaches"].start_time.to_numpy()))) for s in sessions))''','''print("Other acquisition series, by subject:", {s["subject"]: sorted(k for k in s["acquisition"] if k != "ElectricalSeries")
                                                for s in sessions if len(s["acquisition"]) > 1})
print("Their descriptions:", sorted({(k, v) for s in sessions for k, v in s["acquisition"].items() if k != "ElectricalSeries"}))
mismatch = []
for s in sessions:
    d = s["event_times"] - s["reaches"].start_time.to_numpy()
    off = np.abs(d) > 0.01
    if off.any():
        mismatch.append({"file": f"{s['subject']} day {s['day']}", "events": len(d), "differing": int(off.sum()),
                         "difference_s": np.unique(np.round(d[off], 1)).tolist()[:3], "ecog_offset_s": round(s["ecog_offset"], 1),
                         "start_time_of_differing": np.round(s["reaches"].start_time.to_numpy()[off][:3], 1).tolist()})
print("Files where ReachEvents timestamps differ from the reaches table's start_time by more than 0.01 s:")
print(pd.DataFrame(mismatch).to_string(index=False))''')
rep('''# The archive summary lists 12 subjects, all *Homo sapiens*. The files give only species and
# subject id: no sex or age, so the paper's demographics cannot be checked. Every file holds
# 24 h of pose and 15.5 to 24 h of ECoG. ECoG data are stated in volts with a conversion of 1e-6,
# so the stored values are microvolts. The pose is stated in meters with a conversion of NaN, but
# its values are image pixels (0 to about 640; the reach features are in pixels). The ECG
# channels (`ECGL`, `ECGR`, subject 01 only) carry the description of the EOG channels
# ("Electrooculography for tracking saccades"). The chunk length of the ECoG differs between
# files (84375 samples in most; see the table).''','''# The archive summary lists 12 subjects, all human. The files give only species and subject id:
# no sex or age, so the paper's demographics cannot be checked. Every file holds 24 h of pose and
# 15.5 to 24 h of ECoG. ECoG data are stated in volts with a conversion of 1e-6, so the stored
# values are microvolts. The pose is stated in meters with a conversion of NaN, but its values are
# image pixels (up to about 1233 by 708 in the windows read below; the reach features are in
# pixels). The ECG series (`ECGL`, `ECGR`, subject 01 only) carry the description of the EOG
# series ("Electrooculography for tracking saccades"). The ECoG chunk length is 54412 samples in
# subject 01 day 7 and 84375 in the other files.
#
# The `ReachEvents` timestamps equal the reaches table's `start_time` except in four files. In the
# three files whose ECoG starts later in the day, every timestamp is earlier by the file's offset
# of `session_start_time` from the start of its day (8.1 to 8.5 h). In subject 08 day 4, one
# event's `start_time` is 86440.3 s, past the end of the 24 h file, where its timestamp is 40.3 s.''')
rep('''# event-time offset''','''# event-time offset''') if False else None
rep('''# Speech ratio lies within 0 to 1, as described. `Bimanual_overlap` is described as a fraction of
# the movement duration, but reaches 3.8 and is never above the reach duration: it is in seconds,
# as in the paper's code (overlap in frames divided by 30). The stored reach angle covers -180 to
# 180 degrees; its convention is checked against the pose below. Some durations
# (`stop_time - start_time`) fall below the 0.5 s the Methods keep. No file has more than 200
# events, the Methods' cap per day.''','''# Speech ratio lies within 0 to 1, as described. `Bimanual_overlap` is described as a fraction of
# the movement duration, but reaches 3.83 (1708 events above 1) and is never above the reach
# duration: it is in seconds, as in the paper's code (overlap in frames divided by 30). The stored
# reach angle covers -180 to 180 degrees; its convention is checked against the pose below. 328
# durations (`stop_time - start_time`) are below the 0.5 s the Methods keep (the shortest is
# 0.23 s). No file has more than 200 events, the Methods' cap per day.''')
rep('''print("Pose x, y ranges (px), over these windows:",''','''late_files = [f"{s['subject']} day {s['day']}" for s in sessions if s["ecog_offset"] > 0]
pose_chk["file"] = pose_chk.subject + " day " + pose_chk.day.astype(str)
print("Late-starting files:", pose_chk[pose_chk.file.isin(late_files)].groupby("file")[["resp_true", "resp_shift"]].median().round(1).to_dict("index"))
print("Pose x, y ranges (px), over these windows:",''')
rep('''# The wrist speeds up after the stored event times in every subject and not 30 s later, so the
# pose and the event tables share a clock, in all files including the three that start later in
# the day.''','''# The wrist speeds up after the stored event times (median 27.8 to 206.9 px/s per subject) and
# not 30 s later (-2.0 to 1.8 px/s), and in 94% of events against 49%, so the pose and the event
# table share a clock, also in the three files that start later in the day.''')
rep('''# The epochs and the events of every file run to 24 h, also in the three files whose ECoG covers
# only 15.5 to 15.9 h and whose `session_start_time` is 8.1 to 8.5 h after the day's start
# (subject 01 day 7, 04 day 3, 06 day 3). The ECoG `starting_time` is 0 in every file, so the
# files place the ECoG at the day's start. The ECoG check below shows that in these files the
# ECoG starts at `session_start_time` and the event times count from the day's start.''','''# The epochs of every file run to 24 h, also in the three files whose ECoG covers only 15.5 to
# 15.9 h and whose `session_start_time` is 8.1 to 8.5 h after the day's start (subject 01 day 7,
# 04 day 3, 06 day 3). The ECoG `starting_time` is 0 in every file, so the files place the ECoG
# at the start of the day, as the pose and the reaches table. The `ReachEvents` timestamps of
# these files, and the ECoG check below, show that the ECoG starts at `session_start_time`.''')
rep('''# %% [markdown]
# Before the offset was applied, the three late-starting files had most of their windows past
# the end of their ECoG. The windows dropped as missing or flat are those that reach into
# stretches of zeros or past the end of the recording.
''','''# %% [markdown]
# 124 of 8088 events (1.5%) are dropped: 89 whose window holds missing data, lies outside the
# recording or has a channel of zeros, and 35 with outlying power at 115 to 125 Hz. No window has
# a mean power below 0 dB.
''')
rep('''# In subject 01 day 7 and subject 06 day 3, the stored times give no movement response: LFB is
# not below 0. The corrected times give the decrease in LFB and increase in HFB seen in the
# other files. So in these files the ECoG starts at `session_start_time` and the events count
# from the day's start, and the corrected times are used throughout. In subject 04 day 3 neither
# timing shows a clear response (this subject's LFB response is small on every day), so its
# alignment could not be established; the same correction is applied. Across subjects, HFB minus
# LFB is larger at the event times than 30 s later in most subjects (table above), which supports
# a shared clock between ECoG and events. Where a subject shows no contrast, the response itself
# is small (subjects 04, 08 and 09 have the smallest precentral responses in Table 1), so the
# check cannot tell an offset from a weak response there.''','''# In subject 01 day 7 and subject 06 day 3, the stored times give an LFB increase (0.61 and
# 0.70 dB), and the corrected times the LFB decrease with HFB increase seen in the other files
# (-1.40 and 0.12 dB; -1.47 and 2.77 dB). With the `ReachEvents` timestamps, which equal the
# corrected times, this shows that in these files the ECoG starts at `session_start_time` while
# the reaches table counts from the day's start; the corrected times are used throughout. In
# subject 04 day 3 neither timing gives a clear response (corrected -0.29 and -0.10 dB, from 35
# events; stored 0.40 and -0.14 dB, from 13), so its alignment could not be established from the
# ECoG; the same correction is applied, as its `ReachEvents` timestamps also support.
#
# Across subjects, precentral HFB minus LFB is larger at the event times than 30 s later in 10
# of 12 subjects, significantly in 5 (05, 06, 07, 08, 11; Wilcoxon p below 0.05) on 15 to 25
# events each. In subjects 01 and 02 it is not larger, so this subsample does not establish the
# ECoG clock for them; it is consistent with a shared clock elsewhere.''')
rep('''print("Paper: surface 4.9 +/- 4.9; depth 1.0 +/- 1.4 over 5 subjects")''','''print("Paper: surface 4.9 +/- 4.9; depth 1.0 +/- 1.4 over 5 subjects")
a = bad_tab[(bad_tab.reading == "(a) first file") & (bad_tab.subject != "03")]
print(f"Reading (a) without subject 03 (whose 16 depth electrodes have no coordinates): depth {a.depth.mean():.2f} over {a.depth.notna().sum()} subjects")''')
rep('''print("Events per file at the Methods' cap of 200 or one below:", int((files.events >= 199).sum()), "of", len(files))''','''print("Events per file at the Methods' cap of 200 or one below:", int((files.events >= 199).sum()), "of", len(files))
c = counts.all_events * (1 - 0.178)
print(f"Variant, all events less the Methods' mean 17.8% of false positives: min {c.min():.0f}, max {c.max():.0f}, median {c.median():.0f}")''')
open('nb_src.py','w').write(s)
EOF
grep -c "Result: TBD" $TMPDIR/nb_src.py
```

```
21
Shell cwd was reset to
```

**Agent**

Writing the 21 conclusions from the outputs:

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_src.py').read()
R=[
"""**Result: reproduced.** The dandiset holds 12 subjects with 3 to 5 files each, all on days 3 to
# 7. Five subjects have electrodes in the right hemisphere and seven in the left, and in every
# subject the events are of the contralateral wrist.""",
"""**Result: partially reproduced.** Under both readings the mean number of surface electrodes,
# 84.8, is within tolerance of 87.0, and the mean number of depth electrodes, 23.7, within
# tolerance of 23.2. But 7 subjects (reading a) or 6 (reading b) have depth electrodes, not 5.""",
"""**Result: partially reproduced.** Under reading (a), the paper's code's choice, 4.83 +/- 4.99
# surface electrodes per subject are flagged bad, matching 4.9 +/- 4.9, but 4.29 depth electrodes
# per subject with depth electrodes, against 1.0. Without subject 03, whose 16 depth electrodes
# have no coordinates and are all flagged, the depth mean is 2.33. Readings (b) and (c) match
# neither value.""",
"""**Result: partially reproduced.** The reaches tables hold 211 to 996 events per subject
# (median 770.5), and 208 to 986 (median 748) remain after segment rejection. Under both readings
# the largest count is within tolerance of 947, but the smallest and the median are above the
# paper's 151 and 640. Twelve of 55 files hold 199 or 200 events, the Methods' cap per day before
# visual inspection removed 17.8 +/- 9.9% of events as false positives; taking 17.8% off every
# subject gives 173 to 819 (median 633). The dandiset marks no events as false positives.""",
"""**Result: reproduced.** All ten features differ across subjects with p < 0.001 (the largest p
# is 1.2e-34, for duration). The effect sizes range from 0.022 (duration) to 0.250 (onset speed).""",
"""**Result: reproduced.** Under reading (b), subjects 04, 05 and 09 have the three largest shares
# of their events on one day (0.381, 0.610 and 0.517; the next is 0.308). Under reading (a) only
# subjects 05 and 09 have more than half on one day.""",
"""**Result: reproduced.** Over all events, 91.7% last less than 2 s and 91.5% cover less than
# 200 pixels, and both fractions are above half in all 12 subjects (the lowest is 0.590, for
# magnitude in subject 08).""",
"""**Result: not reproduced.** Over all events the two most populated bins are 60 to 75 and 75 to
# 90 degrees (1304 and 1605 events): upward reaches dominate. The downward outer bin holds 514
# events, more than its neighbour (487) but fewer than eight of the twelve bins, so the pooled
# part of the criterion fails. In 11 of 12 subjects steep reaches (|angle| above 60 degrees)
# outnumber flat ones (below 30), and in every subject upward steep reaches outnumber downward
# ones.""",
"""**Result: partially reproduced.** All six correlations are positive and five are within 10% of
# the paper's values. Magnitude and duration correlate at 0.231, just outside 0.26 +/- 0.026. The
# events left after segment rejection give the same values within 0.004.""",
"""**Result: reproduced.** Over all events the median bimanual ratio is 0.137, the median overlap
# 0.467 s against a median duration of 1.1 s, and 72.6% of events are of class bimanual.
# Subjects 04, 05 and 02 are among the four with the highest median ratio (with 07).""",
"""**Result: reproduced.** In all 12 subjects the matrix has a row for each electrode of the
# dandiset's table (subject 01's four extra rows, past the table, are zeros), the eight regions
# with density above 3 are the paper's, and an electrode's weight for a region follows its
# closeness to the region's centroid (median rank correlation 0.917 to 0.967, against at most
# 0.143 with shuffled rows). Rows of zero weight are electrodes without coordinates in subject 03
# (rows 80 to 95), but in subject 12 (rows 72 to 79) they have coordinates in the dandiset, and
# that subject's electrodes without stored R2 are others (rows 116 to 123).""",
"""**Result: reproduced.** Averaged over subjects, LFB power falls and HFB power rises from 0 to
# 0.5 s in the precentral (-0.549 and 0.487 dB), postcentral (-0.793 and 0.596 dB) and inferior
# parietal (-0.879 and 0.280 dB) regions, and the summed change in each (1.036 to 1.389 dB) is
# larger than in any temporal region (at most 0.337 dB). This rests on 15 to 25 events per
# subject. Restricting the precentral projection to the electrodes of set P changes it little
# (r = 0.999 in both bands).""",
"""**Result: reproduced.** The subject means fall inside the paper's 95% intervals for 22 of the
# 24 subject and band values (medians for 20). The two means outside are subject 06 HFB (1.99
# against 2.02 to 2.37 dB) and subject 10 LFB (-0.30 against -0.87 to -0.35 dB). Across subjects
# the values follow the interval centres (Spearman r 0.846 to 0.974). Without segment rejection
# 21 medians fall inside, and without the three late-starting files 19.""",
"""**Result: reproduced.** Precentral power differs across subjects in both bands (H = 802.1 for
# LFB and 1243.5 for HFB over 7964 events; p is below the smallest number printed, so below
# 0.001).""",
"""**Result: reproduced.** 23 of the 24 subject and band calls agree with the paper's: 5 subjects
# have a significant day effect in each band. The one difference is subject 05 in LFB (p =
# 0.054, where the paper reports 0.013). The same 23 agree without segment rejection.""",
"""**Result: reproduced.** The SD across days is lower with baseline subtraction in 9 of 12
# subjects for LFB and in 12 of 12 for HFB (median ratios 0.216 and 0.291), and it stays above 0
# in every subject (smallest 0.066 dB for LFB and 0.032 dB for HFB).""",
"""**Result: reproduced.** The largest recomputed mean test R2 is 0.141 (subject 03, LFB), within
# the bound of 0.25. The R2 values stored in the dandiset, which cover every electrode, reach
# 0.255 (HFB); on the tested electrodes they correlate with the recomputed ones (r = 0.865 for
# LFB and 0.776 for HFB).""",
"""**Result: reproduced.** On the stored R2 values, the region with the highest projected R2 is
# the precentral for LFB and the postcentral for HFB, and the frontoparietal mean is higher than
# the temporal mean in both bands. The projected values are all near or below 0 (-0.0192 to
# 0.0008), as only 24 (LFB) and 25 (HFB) electrodes have a stored R2 above 0.05.""",
"""**Result: reproduced.** On the 12 tested electrodes with mean LFB test R2 above 0.05 (6 in
# subject 01, 4 in 03, 2 in 11), reach angle (0.0645) and day (0.0280) have the largest mean
# Delta R2 for LFB, and also for HFB. The same holds with the code's split and scoring, and over
# all tested electrodes. The well-fit electrodes come from three subjects only.""",
"""**Result: reproduced.** On the same 12 electrodes the mean reach angle coefficient is -1.065
# for LFB (negative on all 12, Wilcoxon p = 0.00049) and 0.2145 for HFB (positive on 11 of 12,
# p = 0.012): upward reaches go with a deeper LFB decrease and a larger HFB increase.""",
"""**Result: reproduced.** Forward selection retains reach angle in 64.1% of the models on the
# tested electrodes, more than any other feature (next, onset speed at 38.6%), and in both
# bands.""",
]
for r in R:
    s=s.replace('# **Result: TBD.**', '# '+r, 1)
assert 'TBD' not in s
summary='''# %% [markdown]
# ## Summary
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# | Claim | Data | Outcome |
# |---|---|---|
# | subjects-days-hemispheres | dandiset | reproduced |
# | demographics | dandiset | blocked: data missing |
# | electrode-counts | dandiset | partially reproduced |
# | bad-electrodes | dandiset | partially reproduced |
# | event-counts | dandiset | partially reproduced |
# | features-differ-subjects | dandiset | reproduced |
# | days-one-dominant | dandiset | reproduced |
# | duration-magnitude-small | dandiset | reproduced |
# | angle-bimodal | dandiset | not reproduced |
# | feature-correlations | dandiset | partially reproduced |
# | bimanual-skew | dandiset | reproduced |
# | projection-link | with inputs | reproduced |
# | group-pattern-rois | with inputs | reproduced |
# | precentral-subject-ci | with inputs | reproduced |
# | precentral-subjects-differ | with inputs | reproduced |
# | precentral-day-effects | with inputs | reproduced |
# | baseline-reduces-day-variability | with inputs | reproduced |
# | regression-r2-max | with inputs | reproduced |
# | regression-r2-sensorimotor | with inputs | reproduced |
# | regression-angle-day-top | with inputs | reproduced |
# | regression-angle-coefficient | with inputs | reproduced |
# | regression-angle-retained | with inputs | reproduced |
#
# **How the analysis differs from the paper's.**
#
# - Events are those of the dandiset's reaches tables. The paper's visual removal of false
#   positives cannot be repeated, and the dandiset does not mark them; the segment rejection
#   follows the Methods as far as they can be read (missing or flat data, mean power below 0 dB in
#   microvolts squared, power at 116 and 121 Hz more than 3 SD above the subject's mean).
# - In three files the event times are moved onto the ECoG clock (see the data check).
# - Spectral power is computed here with the code's Morlet parameters, not with MNE, on 4 s
#   windows read from the continuous ECoG, not on the paper's 10 s segments.
# - Precentral power uses the electrodes that carry 95% of the precentral weight; the
#   eight-region pattern uses five events per file. The regression uses up to eight electrodes per
#   subject, 40 splits in place of 200, and the Methods' 90/10 split and Delta R2 scoring, with
#   the code's 80/20 split and scoring as a variant; forward selection runs on all events, as in
#   the code.
# - The sensorimotor location of the best regression models is judged on the R2 stored in the
#   dandiset, not on a recomputation.
#
# **What was found about the dandiset.**
#
# - In three files (subject 01 day 7, 04 day 3, 06 day 3) the ECoG starts at
#   `session_start_time`, 8.1 to 8.5 h after the start of the day, but its `starting_time` is 0,
#   while the reaches table, the epochs and the pose count from the start of the day. The
#   `ReachEvents` timestamps of these files are on the ECoG clock and disagree with the reaches
#   table.
# - `session_start_time` gives 19:00 at UTC-05:00 for the full-day files, while the sleep labels
#   place the start of the file at local midnight.
# - The events are those before the paper's visual removal of false positives, with no mark of
#   which were removed; per subject counts are 211 to 996 against the paper's 151 to 947.
# - Subject sex and age are not in the dandiset.
# - `Bimanual_overlap` is in seconds, though described as a fraction; the reach angle's convention
#   (image coordinates, y down) is not stated; pose is stated in meters with a NaN conversion but
#   is in pixels; the ECG series carry the EOG description; electrode location is "unknown" and
#   impedance missing for every electrode.
# - Electrode groups described as depth occur in seven subjects, where the paper reports five;
#   subject 03's 16 depth electrodes have no coordinates; in subject 12 the electrodes without
#   stored R2 are not those without projection weight.
# - One event (subject 08 day 4) has a `start_time` past the end of its 24 h file.
# - The ECoG chunk length differs between files, and over the network h5py takes about 0.4 s per
#   chunk row to look chunks up; the notebook reads the chunk index directly.

# %%
print(f"Notebook ran in {(time.time() - nb_started) / 60:.1f} min.")
'''
a=s.index('# %% [markdown]\n# ## Summary')
s=s[:a]+summary
open('nb_src.py','w').write(s)
EOF
python3 $TMPDIR/py2nb.py $TMPDIR/nb_src.py entries/000055-peterson-2021/reproduce_peterson_2021.ipynb && python tools/entry.py check entries/000055-peterson-2021
```

```
Exit code 1
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 204, in write
    fp.write(s)
    ^^^^^^^^
AttributeError: 'str' object has no attribute 'write'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/claude-1001/py2nb.py", line 18, in <module>
    nbformat.write(nb,sys.argv[2])
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 208, in write
    with Path(fp).open("w", encoding="utf8") as f:
         ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/pathlib/_local.py", line 537, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'entries/000055-peterson-2021/reproduce_peterson_2021.ipynb'
```

**Agent calls Bash**

```bash
pwd && python3 $TMPDIR/py2nb.py $TMPDIR/nb_src.py entries/000055-peterson-2021/reproduce_peterson_2021.ipynb && python tools/entry.py check entries/000055-peterson-2021
```

```
92
0 error(s)
```

**Agent**

The check passes. Running the official lock and check-then-run:

**Agent calls Bash**

```bash
python tools/entry.py lock entries/000055-peterson-2021 && time python tools/entry.py all entries/000055-peterson-2021 2>&1 | tail -5
```

```
wrote entries/000055-peterson-2021/requirements.lock.txt
Installed kernelspec registry-000055-peterson-2021 in executed/000055-peterson-2021/.venv/share/jupyter/kernels/registry-000055-peterson-2021
0 error(s)
pass  reproduce_peterson_2021.ipynb  (554 s)

real	9m25.359s
user	28m16.943s
sys	3m55.492s
```

**Agent**

The run passes (554 s). Now confirming that every number in the conclusions matches the executed copy:

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && python - <<'EOF' > $TMPDIR/out2.txt
import nbformat
nb=nbformat.read('executed/000055-peterson-2021/reproduce_peterson_2021.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f'===== [{i}] {c.metadata.get("tags","")}')
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[-4000:])
        elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
diff <(grep -v "in [0-9]* s\|ran in" $TMPDIR/out2.txt) <(. $TMPDIR/expl/bin/activate; python - <<'EOF' | grep -v "in [0-9]* s\|ran in"
import nbformat
nb=nbformat.read('/tmp/claude-1001/exec/reproduce_peterson_2021.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f'===== [{i}] {c.metadata.get("tags","")}')
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[-4000:])
        elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
) | head -80
```

```
4c4,7
<  r_wrist          L     0.000
---
> 0       24.00        92      500.0 (84375, 1)        24.0     173     l_wrist          R     0.000
>      08    6        2000-01-05T19:00:00-05:00       24.00        92      500.0 (84375, 1)        24.0     198     l_wrist          R     0.000
>      08    7        2000-01-06T19:00:00-05:00       24.00        92      500.0 (84375, 1)        24.0     200     l_wrist          R     0.000
>      09    3        2000-01-02T19:00:00-05:00       24.00       126      500.0 (84375, 1)        24.0      15     r_wrist          L     0.000
31,38c34,35
< Other acquisition series, by subject: {'01': ['ECGL', 'ECGR', 'EOGL', 'EOGR']}
< Their descriptions: [('ECGL', 'Electrooculography for tracking saccades - left'), ('ECGR', 'Electrooculography for tracking saccades - right'), ('EOGL', 'Electrooculography for tracking saccades - left'), ('EOGR', 'Electrooculography for tracking saccades - right')]
< Files where ReachEvents timestamps differ from the reaches table's start_time by more than 0.01 s:
<     file  events  differing difference_s  ecog_offset_s     start_time_of_differing
< 01 day 7     190        190   [-30682.4]        30682.4 [32313.4, 32323.6, 32800.7]
< 04 day 3      35         35   [-30048.3]        30048.3 [49319.5, 50646.2, 50689.1]
< 06 day 3     166        166   [-29240.6]        29240.6 [29754.3, 29785.6, 31504.3]
< 08 day 4     197          1   [-86400.0]            0.0                   [86440.3]
---
> Other acquisition series and their descriptions: [('ECGL', 'Electrooculography for tracking saccades - left'), ('ECGR', 'Electrooculography for tracking saccades - right'), ('EOGL', 'Electrooculography for tracking saccades - left'), ('EOGR', 'Electrooculography for tracking saccades - right')]
> Event timestamps equal reaches start_time (max difference, s): 86400.0
105d101
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/expl/bin/activate && python - <<'EOF'
import nbformat
old="# events, more than its neighbour (487) but fewer than eight of the twelve bins, so the pooled"
new="# events, more than its neighbour (487) but fewer than six other bins, so the pooled"
p='/tmp/claude-1001/nb_src.py'; s=open(p).read(); assert old in s; s=s.replace(old,new); open(p,'w').write(s)
o2=old[2:]; n2=new[2:]
for f in ['entries/000055-peterson-2021/reproduce_peterson_2021.ipynb','executed/000055-peterson-2021/reproduce_peterson_2021.ipynb']:
    nb=nbformat.read(f,4); k=0
    for c in nb.cells:
        if c.cell_type=='markdown' and o2 in c.source: c.source=c.source.replace(o2,n2); k+=1
    nbformat.write(nb,f); print(f,k)
EOF
python tools/entry.py check entries/000055-peterson-2021
```

```
entries/000055-peterson-2021/reproduce_peterson_2021.ipynb 1
executed/000055-peterson-2021/reproduce_peterson_2021.ipynb 1
0 error(s)
```

**Agent**

Next, the entry README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/000055-peterson-2021/README.md",
 "content": "# Peterson, Singh, Wang, Rao & Brunton (2021) from dandiset 000055\n\nTests the findings of [Peterson et al. (2021)](https://doi.org/10.1523/ENEURO.0007-21.2021) on\n[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12), which holds the\nlong-term ECoG, upper-body pose and wrist movement events of 12 subjects during clinical epilepsy\nmonitoring.\n\n| Claim | Outcome |\n|---|---|\n| 12 subjects, 3 to 5 days each, five implanted on the right | Reproduced |\n| Sex and age of the subjects | Blocked: data missing |\n| Surface and depth electrode counts | Partially reproduced |\n| Electrodes removed as bad | Partially reproduced |\n| 151 to 947 events per subject, median 640 | Partially reproduced |\n| All ten features differ across subjects | Reproduced |\n| Subjects 04, 05 and 09 have one dominant day | Reproduced |\n| Most reaches last under 2 s and cover under 200 px | Reproduced |\n| Reach angles bimodal at +/-90 degrees | Not reproduced |\n| Correlations between features | Partially reproduced |\n| Bimanual features skewed toward unimanual | Reproduced |\n| The paper's projection matrices link to the electrodes | Reproduced |\n| LFB decrease and HFB increase, largest in sensorimotor regions | Reproduced |\n| Precentral power per subject (Table 1) | Reproduced |\n| Precentral power differs across subjects | Reproduced |\n| Recording-day effects per subject (Table 2) | Reproduced |\n| Baseline subtraction reduces variability across days | Reproduced |\n| Regression R2 at most 0.25 | Reproduced |\n| Best regression models in sensorimotor areas | Reproduced |\n| Reach angle and day are the most explanatory features | Reproduced |\n| Upward reaches enhance the power pattern | Reproduced |\n| Reach angle most often retained | Reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe regional analyses use the paper's projection matrices from Figshare\n(doi:10.6084/m9.figshare.12114408.v1), which the dandiset does not hold. In three files the ECoG\nand the event table are on different clocks; the notebook shows this and corrects the event times.\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/000055-peterson-2021-01.yaml`](../../attempts/000055-peterson-2021-01.yaml).\n\n- `reproduce_peterson_2021.ipynb`: the analysis. It takes about ten minutes, most of it streaming\n  ECoG windows around 8088 events.\n- `ajile.py`: loading the files, the reach features, a direct reader of the ECoG chunk index with\n  parallel range requests, Morlet power with the paper's parameters, the projection onto regions,\n  and the regression of the paper's code. Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/000055-peterson-2021/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']
print(o.get('required'), list(o['properties']))
print(s['properties']['inputs'])
print(s['properties']['findings']['items'].get('required'), s['properties']['findings']['items']['properties'].keys())
print(s['properties']['provenance']['properties']['agent'])
EOF
```

```
['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'proposed']
{'description': 'Everything the attempt used that is not in the dandiset.', 'type': 'array', 'items': {'type': 'object', 'additionalProperties': False, 'required': ['what', 'source'], 'properties': {'what': {'type': 'string', 'minLength': 1}, 'source': {'description': 'A DOI, or a repository URL with the commit read.', 'type': 'string', 'minLength': 1}}}}
['kind', 'statement'] dict_keys(['kind', 'statement'])
{'description': 'Required when kind is agent.', 'type': 'object', 'additionalProperties': False, 'required': ['harness', 'model', 'protocol'], 'properties': {'harness': {'type': 'string'}, 'model': {'type': 'string'}, 'protocol': {'description': 'Version of the reproduction protocol the agent followed.', 'type': 'string'}}}
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000055-peterson-2021-01.yaml",
 "content": "schema_version: 1\nid: 000055-peterson-2021-01\ndandiset: \"000055\"\ndandiset_version: 0.220127.0436\npaper: doi:10.1523/eneuro.0007-21.2021\ndate: 2026-10-16\nentry: 000055-peterson-2021\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-7\ninputs:\n- what: The paper's projection matrices from electrodes to AAL regions (aal_<subject>_elecs2ROI.csv)\n    and the regions' left-hemisphere centroids (aal_<subject>_ROIcentroids_Lside.csv), Figshare item\n    \"ROI projection matrices and labels\", version 1. Used for every regional measure and for the\n    choice of electrodes in the regression.\n  source: doi:10.6084/m9.figshare.12114408.v1\n- what: The paper's analysis code, read for the method choices the Methods leave open (Morlet\n    parameters, baseline, band medians, projection, folding of the reach angle, regression design,\n    forward selection, splits and Delta R2). The Kruskal-Wallis p-values printed by\n    Plot_banded_power_Fig5.ipynb are shown as reference only.\n  source: https://github.com/BruntonUWBio/naturalistic_arm_movements_ecog at commit\n    04c6faf2f219586fa834d10c614ef48a694cec55\noutcomes:\n- claim: subjects-days-hemispheres\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:subjects-days-hemispheres\n  measured:\n  - 12\n  - 5\n  notes: 12 subjects with 3 to 5 files each, all on days 3 to 7 (subject 01 days 3, 4, 5 and 7;\n    subjects 02 and 03 days 3 to 6; subject 05 days 3, 4 and 7; the others days 3 to 7). Five\n    subjects (02, 04, 05, 07, 08) have electrodes in the right hemisphere by the sign of the mean x\n    coordinate, and every file's events are of the contralateral wrist.\n- claim: demographics\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The files' subject objects hold only species and subject_id, and the dandiset metadata has\n    no sex or age. The paper gives the values only in aggregate.\n- claim: electrode-counts\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:electrode-counts\n  measured:\n  - 84.8\n  - 7\n  - 23.7\n  notes: Under reading (a) the mean number of surface electrodes is 84.8 +/- 11.6 (paper 87.0 +/-\n    12.9) and seven subjects (01, 02, 03, 09, 10, 11, 12) have electrodes in groups described as\n    depth, 23.7 +/- 13.4 on average (paper five subjects, 23.2 +/- 12.1). Under reading (b), which\n    leaves out subject 03's 16 depth electrodes without coordinates, six subjects have depth\n    electrodes, 23.7 +/- 13.8. The surface count and the mean depth count match; the number of\n    subjects with depth electrodes does not under either reading.\n  deviations:\n  - Depth electrodes are identified by their group description, as the files have no other label.\n- claim: bad-electrodes\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:bad-electrodes\n  measured:\n  - 4.83\n  - 4.29\n  notes: Under reading (a), the `good` flags of each subject's first file as the paper's code takes\n    them, 4.83 +/- 4.99 surface electrodes per subject are bad (paper 4.9 +/- 4.9) and 4.29 +/-\n    5.85 depth electrodes per subject with depth electrodes, over seven subjects (paper 1.0 +/- 1.4\n    over five). Subject 03's 16 depth electrodes, which have no coordinates, are all flagged;\n    without that subject the depth mean is 2.33. Reading (b), bad in any file, gives 12.58 and 8.14;\n    reading (c), the mean over files, 4.17 and 4.71.\n  deviations:\n  - The `good` flag is taken as the paper's bad-electrode selection; the files do not say how it was\n    set, and it differs between a subject's files.\n- claim: event-counts\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:event-counts\n  measured:\n  - 211\n  - 996\n  - 770.5\n  notes: Reading (a), the reaches tables, gives 211 to 996 events per subject with a median of\n    770.5; reading (b), after segment rejection, 208 to 986 with a median of 748. The largest count\n    is within tolerance of 947 under both readings, the smallest and the median are not. 12 of 55\n    files hold 199 or 200 events, the Methods' cap per day, which comes before the visual removal\n    of 17.8 +/- 9.9% of events as false positives; taking 17.8% off every subject gives 173 to 819\n    with a median of 633. The dandiset appears to hold the events before that removal and does not\n    mark which were removed.\n- claim: features-differ-subjects\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:features-differ-subjects\n  notes: Kruskal-Wallis across the 12 subjects gives p < 0.001 for all ten features over 8088\n    events; the largest p is 1.2e-34 (duration). Effect sizes (eta squared from H) range from 0.022\n    (duration) to 0.250 (onset speed).\n  deviations:\n  - Includes the events the paper removed as false positives, which the dandiset does not mark.\n  - Time of day is taken from the start of each file's day, which the sleep labels place at local\n    midnight; the files' session_start_time states 19:00 at UTC-05:00.\n- claim: days-one-dominant\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:days-one-dominant\n  notes: Under reading (b) subjects 04, 05 and 09 have the largest share of their events on one day\n    (0.381, 0.610 and 0.517; next 0.308 in subjects 02 and 03). Under reading (a) only subjects 05\n    and 09 have more than half their events on one day.\n  deviations:\n  - The paper's word \"most\" is read two ways; the claim holds under reading (b).\n- claim: duration-magnitude-small\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:duration-magnitude-small\n  notes: 91.7% of events last less than 2 s and 91.5% cover less than 200 pixels; both fractions are\n    above half in all 12 subjects, the lowest being 0.590 for magnitude in subject 08 (median 172\n    pixels). 328 events last less than the 0.5 s the Methods keep.\n- claim: angle-bimodal\n  outcome: not_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:angle-bimodal\n  notes: Over all events the folded angle has its two most populated 15-degree bins at 60 to 75 and\n    75 to 90 degrees (1304 and 1605 of 8088 events). The downward outer bin holds 514, more than its\n    neighbour (487) but fewer than six other bins, so the pooled part of the criterion fails. In 11\n    of 12 subjects steep reaches (|angle| above 60) outnumber flat ones (below 30), and in every\n    subject upward steep reaches outnumber downward ones. The distribution has a strong upward peak\n    and a weak downward one. The stored angle is in image coordinates with y down (checked against\n    the pose, median difference 1.5 degrees), and the code's negation makes upward positive.\n  deviations:\n  - Includes the events the paper removed as false positives.\n- claim: feature-correlations\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:feature-correlations\n  measured:\n  - 0.231\n  - 0.609\n  - 0.505\n  - 0.501\n  - 0.494\n  - 0.598\n  notes: Five of six Pearson correlations are within 10% of the paper's; magnitude and duration is\n    0.231 against 0.26 +/- 0.026. All six are positive. The events left after segment rejection give\n    values within 0.004 of these.\n  deviations:\n  - Includes the events the paper removed as false positives.\n- claim: bimanual-skew\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:bimanual-skew\n  notes: Median bimanual ratio 0.137, median overlap 0.467 s against a median duration of 1.1 s, and\n    72.6% of events of class bimanual. The four subjects with the highest median ratio are 04, 07,\n    05 and 02.\n  deviations:\n  - Bimanual overlap is used as stored, in seconds; the file's description calls it a fraction of\n    the movement duration.\n- claim: projection-link\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:projection-link\n  notes: Matched by row order. In all 12 subjects the matrix has one row per electrode of the\n    dandiset's table (subject 01's four extra rows past the table are all zero), the regions with\n    average density above 3 are the paper's eight, and the median rank correlation between an\n    electrode's weight and its closeness to the region's centroid is 0.917 to 0.967, against at most\n    0.143 with shuffled rows. Zero-weight rows are subject 03's electrodes without coordinates (rows\n    80 to 95) and subject 12's rows 72 to 79 (group AID), which have coordinates in the dandiset;\n    subject 12's electrodes without stored R2 are rows 116 to 123 (group PHD).\n- claim: group-pattern-rois\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:group-pattern-rois\n  notes: Mean over subjects of the subject medians, 0 to 0.5 s. LFB and HFB change by -0.549 and\n    0.487 dB in the precentral, -0.793 and 0.596 dB in the postcentral and -0.879 and 0.280 dB in\n    the inferior parietal region; the summed absolute change in these (1.036 to 1.389 dB) exceeds\n    every temporal region (at most 0.337 dB). LFB is below 0 in 12, 10 and 12 of the 12 subjects in\n    these regions. The paper's statistical masking was not applied. The projection matrices match\n    the electrodes (projection-link), so the regional values rest on the dandiset's ECoG.\n  deviations:\n  - Five events per file (seeded subsample, 15 to 25 per subject after rejection) in place of all\n    events, for runtime.\n  - Electrodes carrying 99% of every region's weight; the rest of the weight is left out and the\n    weights renormalised.\n  - No bootstrap masking of non-significant bins; the criterion uses signs and magnitudes.\n  - Spectral power from 4 s windows of the continuous ECoG with the code's Morlet parameters, not\n    MNE on the paper's 10 s segments.\n- claim: precentral-subject-ci\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:precentral-subject-ci\n  measured:\n  - -1.46\n  - -0.45\n  - -1.8\n  - -0.1\n  - -0.45\n  - -1.2\n  - -0.73\n  - -0.03\n  - -0.33\n  - -0.3\n  - -2.05\n  - -0.48\n  - 0.11\n  - 0.52\n  - 1.5\n  - 0.5\n  - 0.35\n  - 1.99\n  - 1.16\n  - 0.52\n  - 0.11\n  - 0.19\n  - 0.18\n  - 0.16\n  notes: Under the first reading, the subject mean over events, 22 of 24 values fall inside the\n    paper's 95% intervals; under the second, the median, 20 of 24. The means outside are subject 06\n    HFB (1.99 against 2.02 to 2.37 dB) and subject 10 LFB (-0.30 against -0.87 to -0.35 dB). Spearman\n    r between these values and the interval centres is 0.846 to 0.974. Without segment rejection 21\n    medians are inside; without the three late-starting files, 19. The paper's intervals are of\n    events after false-positive removal, which cannot be repeated here.\n  deviations:\n  - Table 1 does not say whether its intervals are of the mean or the median; both readings are\n    computed and both match.\n  - Precentral power uses the electrodes that carry 95% of the precentral weight (5 to 32 per\n    subject), weights renormalised; on a subsample the full projection agrees (r = 0.999).\n  - Includes the events the paper removed as false positives; segment rejection as described in\n    the claims file.\n  - In three files the event times are moved onto the ECoG clock (see the findings).\n- claim: precentral-subjects-differ\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:precentral-subjects-differ\n  notes: Kruskal-Wallis across subjects over 7964 events gives H = 802.1 for LFB and 1243.5 for HFB,\n    with p below the smallest printed number (paper's code printed 2.1e-159 and 2.4e-278).\n  deviations:\n  - As for precentral-subject-ci.\n- claim: precentral-day-effects\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:precentral-day-effects\n  notes: 23 of 24 subject and band calls agree with the paper's; five subjects are significant in\n    each band. The difference is subject 05 in LFB, p = 0.054 here against 0.013 in the paper. The\n    same 23 agree without segment rejection.\n  deviations:\n  - As for precentral-subject-ci.\n- claim: baseline-reduces-day-variability\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:baseline-reduces-day-variability\n  notes: The SD across days of the day means is lower with baseline subtraction in 9 of 12 subjects\n    for LFB (not in 03, 06 and 11) and 12 of 12 for HFB, with median ratios 0.216 and 0.291, and it\n    stays above 0 in all (smallest 0.066 and 0.032 dB).\n  deviations:\n  - The legend of Extended Data Figure 5-1 does not name the region or the statistic; the precentral\n    region and the SD of day means were chosen.\n- claim: regression-r2-max\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:regression-r2-max\n  measured: 0.141\n  notes: The largest mean test R2 over 40 splits on the 92 tested electrodes is 0.141 (subject 03,\n    LFB); 0.137 with the code's 80/20 split. The R2 values stored in the dandiset reach 0.149 (LFB)\n    and 0.255 (HFB, subject 04) over all electrodes; on the tested electrodes they correlate with\n    the recomputed ones (r = 0.865 for LFB and 0.776 for HFB). All 101200 Huber fits converged.\n  deviations:\n  - Up to eight electrodes per subject (the good electrodes with the largest precentral weight, 92\n    in all), not every electrode, for runtime.\n  - 40 random day-balanced splits with 90% training (the Methods) in place of 200; the code's 80%\n    split with 10 splits is shown as a variant.\n  - Forward selection on all events, as in the code; the Methods do not say whether it used the\n    training events only.\n- claim: regression-r2-sensorimotor\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:regression-r2-sensorimotor\n  notes: On the stored R2 projected onto the regions and averaged over subjects, the highest region\n    is the precentral for LFB and the postcentral for HFB, and the frontoparietal mean exceeds the\n    temporal mean in both bands (LFB -0.0061 against -0.0182; HFB -0.0084 against -0.0171). The\n    projected values are all near or below 0, as only 24 (LFB) and 25 (HFB) electrodes have a stored\n    R2 above 0.05.\n  deviations:\n  - Judged on the R2 values stored in the dandiset, whose computation the files do not describe, not\n    on a recomputation; the recomputation covers precentral electrodes only and agrees with the\n    stored values there (regression-r2-max).\n  - The paper shows electrodes on a brain; here the stored R2 is projected onto the eight regions.\n- claim: regression-angle-day-top\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:regression-angle-day-top\n  notes: 12 of 92 tested electrodes have mean LFB test R2 above 0.05 (6 in subject 01, 4 in 03, 2 in\n    11). On them, reach angle (0.0645) and day (0.0280) have the largest mean Delta R2 for LFB, and\n    also for HFB (0.0108 and 0.0051). The same two lead with the code's split and scoring and over\n    all tested electrodes. The well-fit electrodes come from three subjects.\n  deviations:\n  - As for regression-r2-max.\n  - Delta R2 is scored on unshuffled test events, as the Methods say; the code scores the shuffled\n    model on shuffled test events (shown as a variant, same result).\n- claim: regression-angle-coefficient\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:regression-angle-coefficient\n  notes: On the 12 well-fit electrodes the mean reach angle coefficient is -1.065 for LFB (negative\n    on all 12, Wilcoxon p = 0.00049) and 0.2145 for HFB (positive on 11 of 12, p = 0.012). Over all\n    92 tested electrodes the means are -0.277 and 0.160.\n  deviations:\n  - As for regression-r2-max.\n- claim: regression-angle-retained\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:regression-angle-retained\n  notes: Forward selection retains reach angle in 64.1% of the 184 models on the tested electrodes,\n    ahead of onset speed (38.6%) and duration (34.8%); it leads in both bands (67.4% LFB, 60.9% HFB).\n    The paper's order after angle (duration, magnitude, bimanual ratio, overlap) is not reproduced\n    on these electrodes, which the criterion does not test.\n  deviations:\n  - As for regression-r2-max; the paper's figure averages over regions, here over precentral\n    electrodes.\nfindings:\n- kind: metadata_error\n  statement: In three files (sub-01 ses-7, sub-04 ses-3, sub-06 ses-3) the ECoG ElectricalSeries has\n    starting_time 0 but starts at session_start_time, 8.1 to 8.5 h after the start of the day, while\n    the reaches table, the epochs and the pose count from the start of the day. Event-locked ECoG with\n    the stored reach times shows no movement response in sub-01 ses-7 and sub-06 ses-3; with the\n    offset subtracted it shows the usual one. The ReachEvents timestamps of these files are on the\n    ECoG clock, so the two event series of a file disagree by the offset.\n- kind: metadata_error\n  statement: The full-day files give session_start_time as 19:00 at UTC-05:00, but the sleep labels\n    peak in the first six hours of each file and events are fewest 2 to 5 h in, which places the\n    start at local midnight. Consistent with the data, not shown.\n- kind: selection_undocumented\n  statement: The reaches tables hold 211 to 996 events per subject (median 770.5) where the paper\n    analysed 151 to 947 (median 640). Many days hold exactly the cap of 200 events, which the Methods\n    apply before removing 17.8 +/- 9.9% of events as false positives by visual inspection. The\n    dandiset does not say that it holds the events before that removal, nor mark the false\n    positives, so the paper's event set cannot be recovered.\n- kind: data_missing\n  statement: The subjects' sex and age are not in the files or the dandiset metadata.\n- kind: metadata_error\n  statement: Bimanual_overlap is described as a fraction of the contralateral movement duration, but\n    its values (up to 3.83, never above the duration) are in seconds.\n- kind: metadata_insufficient\n  statement: The reach angle's convention is not described; the values are the angle of the largest\n    wrist displacement in image coordinates with y pointing down, so positive angles are downward\n    reaches, the reverse of the paper's Figure 2.\n- kind: metadata_error\n  statement: The pose SpatialSeries are stated in meters with a conversion of NaN, but hold image\n    pixels. The ECGL and ECGR series of sub-01 carry the description of the EOG series\n    (\"Electrooculography for tracking saccades\").\n- kind: metadata_insufficient\n  statement: Electrode location is \"unknown\" and impedance missing for every electrode, so regions\n    can be assigned only with the paper's projection matrices on Figshare. The stored low_freq_R2 and\n    high_freq_R2 columns do not say how they were computed (they agree with a recomputation of the\n    paper's regression, r = 0.78 to 0.87).\n- kind: other\n  statement: Electrode groups described as depth occur in seven subjects, where the paper reports\n    five; sub-03's 16 depth electrodes have no coordinates and are all flagged bad. In sub-12 the\n    electrodes with zero projection weight in the paper's matrices (rows 72 to 79) have coordinates,\n    and the electrodes without stored R2 are others (rows 116 to 123).\n- kind: other\n  statement: In sub-08 ses-4 one reach has a start_time of 86440.3 s, past the end of its 24 h file,\n    where its ReachEvents timestamp is 40.3 s. 328 reaches last less than the 0.5 s the Methods keep.\n- kind: other\n  statement: The ECoG is stored in chunks of one channel, 84375 samples long (54412 in sub-01 ses-7),\n    and its chunk B-tree is spread through each file. Streamed with h5py, looking up the chunks of one\n    window costs about 0.4 s per chunk row over the network; the entry reads the chunk index directly.\n- kind: code_mismatch\n  statement: The paper's regression code splits 80/20 where the Methods say 90/10, scores Delta R2 on\n    shuffled test events where the Methods say unshuffled, and runs forward selection on all events,\n    including the test events. Here the choices make no difference to the outcomes.\n"
}
```

```
File created successfully at: attempts/000055-peterson-2021-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
for f in ['attempts/000055-peterson-2021-01.yaml','claims/000055/10.1523-eneuro.0007-21.2021.yaml']:
    d=yaml.safe_load(open(f))
    def walk(x,path=''):
        if isinstance(x,dict):
            for k,v in x.items(): walk(v,path+'/'+str(k))
        elif isinstance(x,list):
            for i,v in enumerate(x): walk(v,path+f'[{i}]')
        elif isinstance(x,str) and ': ' in x: print('COLON',f,path,x[:80])
    walk(d)
    print(f,'ok')
a=yaml.safe_load(open('attempts/000055-peterson-2021-01.yaml'))
c=yaml.safe_load(open('claims/000055/10.1523-eneuro.0007-21.2021.yaml'))
ids=[x['id'] for x in c['claims']]; oc=[x['claim'] for x in a['outcomes']]
print(ids==oc, len(ids))
for x,o in zip(c['claims'],a['outcomes']):
    e=x.get('expected'); m=o.get('measured')
    if e is not None:
        ne=len(e) if isinstance(e,list) else 1; nm=len(m) if isinstance(m,list) else (1 if m is not None else 0)
        if ne!=nm: print('measured mismatch',x['id'],ne,nm)
EOF
python tools/entry.py check entries/000055-peterson-2021
```

```
attempts/000055-peterson-2021-01.yaml ok
claims/000055/10.1523-eneuro.0007-21.2021.yaml ok
True 22
measured mismatch demographics 2 0
0 error(s)
```

**Agent**

Both files are valid. Building the verifier's handover package (step 6):

**Agent calls Bash**

```bash
python tools/entry.py handover entries/000055-peterson-2021 && ls -la executed/000055-peterson-2021/handover/ && git status --short
```

```
wrote executed/000055-peterson-2021/handover
total 324
drwxr-xr-x 2 runner runner   4096 Oct 16 10:04 .
drwxr-xr-x 4 runner runner   4096 Oct 16 10:04 ..
-rw-r--r-- 1 runner runner  21387 Oct 16 10:04 10.1523-eneuro.0007-21.2021.yaml
-rw-r--r-- 1 runner runner  30322 Oct 16 10:04 ajile.py
-rw-r--r-- 1 runner runner 264438 Oct 16 10:04 reproduce_peterson_2021.ipynb
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
?? attempts/000055-peterson-2021-01.yaml
?? claims/000055/
?? entries/000055-peterson-2021/
[... 1 more lines not kept]
```

**Agent**

The handover is built. Several untracked dotfiles have appeared in the repository root. Checking what they are before the workflow commits:

**Agent calls Bash**

```bash
ls -la --time-style=full-iso .bash_profile .bashrc .gitconfig .mcp.json .profile .ripgreprc .zprofile .zshrc .idea .vscode scripts | head -30; cat .gitignore | head -20
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-16 07:56:33.371649687 +0000 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-16 07:56:33.371649687 +0000 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-16 07:56:33.371649687 +0000 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-16 07:56:33.371649687 +0000 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-16 07:56:33.371649687 +0000 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-16 07:56:33.371649687 +0000 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-16 07:56:33.371649687 +0000 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-16 07:56:33.371649687 +0000 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-16 07:56:33.371649687 +0000 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-16 07:56:33.371649687 +0000 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-16 07:56:33.371649687 +0000 scripts
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
.DS_Store
executed/
site/
paper/
```

**Agent**

I made the attempt on dandiset 000055 for Peterson et al. 2021 (eNeuro) and ran steps 1 to 6. The final run passes check and run in a clean environment in 554 s (9.2 min). I did not verify my own work, and nothing is committed.

I used the paper's full text (open access, CC BY, PMC8225404), saved under `paper/`. I did not read the Extended Data figures, which are EPS files; claims about them rest on their legends and the Results. The pinned version is 0.220127.0436, the only published one. The paper cites only its own Figshare dataset, not a DANDI version.

**1. Outcomes per claim**

| Claim | Outcome |
|---|---|
| subjects-days-hemispheres | reproduced |
| demographics | blocked (data_missing: no sex or age anywhere) |
| electrode-counts | partially reproduced (7 subjects have depth electrodes, paper says 5) |
| bad-electrodes | partially reproduced (surface 4.83 matches; depth 4.29 against 1.0) |
| event-counts | partially reproduced (211 to 996, median 770.5, against 151 to 947, median 640) |
| features-differ-subjects | reproduced |
| days-one-dominant | reproduced |
| duration-magnitude-small | reproduced |
| angle-bimodal | not reproduced (strong upward peak, weak downward one) |
| feature-correlations | partially reproduced (5 of 6 within 10%) |
| bimanual-skew | reproduced |
| projection-link (with inputs) | reproduced |
| group-pattern-rois (with inputs) | reproduced |
| precentral-subject-ci (with inputs) | reproduced (22 of 24 inside Table 1's intervals) |
| precentral-subjects-differ (with inputs) | reproduced |
| precentral-day-effects (with inputs) | reproduced (23 of 24 calls agree) |
| baseline-reduces-day-variability (with inputs) | reproduced |
| regression-r2-max, -r2-sensorimotor, -angle-day-top, -angle-coefficient, -angle-retained (with inputs) | reproduced |

The "with inputs" claims use the paper's electrode-to-region projection matrices from Figshare (doi:10.6084/m9.figshare.12114408.v1). They match the dandiset's electrodes in all 12 subjects.

**2. What was found about the dandiset**
- **Clock error:** in three files (sub-01 ses-7, sub-04 ses-3, sub-06 ses-3) the ECoG starts at `session_start_time`, 8.1 to 8.5 h after the day's start, but its `starting_time` is 0. The reaches table, epochs and pose count from the day's start, while the `ReachEvents` timestamps follow the ECoG clock. The stored times give no movement response; subtracting the offset brings it back. The notebook applies this correction.
- **Time of day:** the full-day files state 19:00 at UTC-05:00, but the sleep labels place the file start at local midnight.
- **Events:** the dandiset appears to hold the events before the paper's visual removal of false positives, with no flag marking them.
- **Metadata errors and gaps:**
  - `Bimanual_overlap` is in seconds, though described as a fraction.
  - The reach-angle convention (image coordinates, y down) is not stated.
  - Pose is stated in meters with a NaN conversion but holds pixels.
  - The ECG series carry the EOG description.
  - Electrode location is "unknown" for every electrode.
  - Subject 03's 16 depth electrodes have no coordinates.
  - In subject 12, the electrodes without stored R² are not the ones with zero projection weight.
  - One event (sub-08 ses-4) starts past the end of its file.
- **Code against Methods:** the regression code uses an 80/20 split and shuffled-test ΔR² where the Methods say 90/10 and unshuffled. Here the outcome is the same either way.

**3. Where the protocol was unclear, wrong or missing something**
1. **Version to pin:** the paper cites Figshare, not DANDI. I pinned the only published version and said why in the header.
2. **Clock check:** the suggested contrasts don't fit ECoG with an event table. I used the event-locked response at the true times against 30 s later, plus wrist speed from the pose. The protocol also doesn't cover two event series in one file that disagree; I recorded it as a finding.
3. **Stored derived results:** the files store the paper's regression R² per electrode, and it is unclear whether a claim may be judged on them. I judged one claim (regression-r2-sensorimotor) on them, said so, and showed they agree with my recomputation (r = 0.78 to 0.87).
4. **Code under `inputs`:** the protocol does not say whether code read for method choices belongs there. I listed the code repository and commit, as the example attempt did.
5. **Size against runtime:** the dandiset is 845 GB, and the protocol has no rule for subsampling within the 30 min limit. I used:
   - electrodes carrying 95% of the precentral weight, for all events;
   - five events per file for the eight-region pattern;
   - up to eight electrodes per subject and 40 splits (paper: 200) for the regression.

   All are recorded as deviations.
6. **Many expected values in one claim:** there is no rule for turning 24 confidence intervals into one outcome. I set the threshold (20 of 24) in the criterion before the analysis.
7. **Data check before criteria:** a trial run of the loader showed me subject 01's precentral values before I wrote that criterion. I said so in the claims file's opening comment.
8. **Duplicate check:** comparing raw traces was not feasible at this size. I compared the stored per-electrode SDs and the event tables between files instead; no recording is deposited twice.

**4. Runtime and failures**
- The final notebook runs in 554 s and nothing failed.
- Problems found and fixed during development:
  - h5py chunk lookups over the network took about 0.4 s per chunk row. I replaced them with a direct reader of the chunk index, checked against h5py.
  - `h5o.get_info` took about 2 minutes per file; `h5g.get_objinfo` returns the same address at once.
  - Chunk length differs in one file (54412 samples, not 84375).
- My first conclusion cells were drafted before the run. I replaced them with placeholders and wrote all conclusions from the executed outputs.
- Untracked character-device dotfiles (`.bashrc`, `.gitconfig`, `scripts` and others) in the repository root come from the sandbox, not from this attempt. I left them alone; they should not be committed.

Files are in `claims/000055/`, `attempts/`, and `entries/000055-peterson-2021`:
- 10.1523-eneuro.0007-21.2021.yaml
- 000055-peterson-2021-01.yaml
- reproduce_peterson_2021.ipynb

## End of run

88 turns, 128 minutes, result: success.
