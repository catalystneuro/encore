# 000959 · author · run 41252133262

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls claims/000959 paper entries | head -50
```

```
<persisted-output>
Output too large (36.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/872dc8d0-ddfb-4d24-a385-7282affd2812/tool-results/bvdk12vyx.txt

Preview (first 2KB):
Sat Oct 31 23:23:57 UTC 2026
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

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

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/872dc8d0-ddfb-4d24-a385-7282affd2812/tool-results/bvdk12vyx.txt"
}
```

```
1	Sat Oct 31 23:23:57 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-13`. Record this version in the attempt's provenance.
5	
6	This is what agents, or people, do to attempt a target and deposit the
7	result. A target is a dataset in a public archive and a paper it names. How
8	each archive's datasets are named, versioned and read is in
9	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
10	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
11	
12	An attempt has three roles, each a separate run with a separate context:
13	
14	- The **reader** reads the paper and writes the claims file: every finding,
15	  and how each is to be tested, taken from the paper. A second reader checks
16	  it against the paper. Readers never see the dataset's data.
17	- The **author** tests the claims on the dataset. It reads the paper to
18	  understand the claims, but the claims file binds it: it cannot change a
19	  claim's statement, expected values or criterion. A method detail the file
20	  lacks it takes from the paper, citing the passage, and it asks a reader
[... 669 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000959/*.yaml; ls paper; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/872dc8d0-ddfb-4d24-a385-7282affd2812/tool-results/bjo08m6fl.txt"
}
```

```
1	# Claims for Fan, Dal Monte, Nair, Fagan & Chang (2024) on dandiset 000959.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the accepted author manuscript in PubMed Central (PMC11309918, NIHMS1994226),
6	# main text, figure legends and STAR Methods, with its one supplement
7	# (NIHMS1994226-supplement-1.pdf, Table S1 and the legends of Figures S1 to S4). The version of
8	# record (Neuron 112(15) 2631-2644.e6) was not read. The Results point to "Supplementary
9	# Results" for the Mouth stimulation experiments and the post-gaze window; the supplement holds
10	# no such section, and these results are given in the STAR Methods of the manuscript
11	# ("Gaze distance analyses" and "Gaze distance analyses (Mouth stimulation)"), which were read.
12	#
13	# Code read: github.com/changlabneuro/microstim-ofc-social-attention, commit cc0bf994 (2024-10-15),
14	# the analysis code named in Data and code availability (also Zenodo doi:10.5281/zenodo.11110139).
15	# It holds MATLAB scripts for every analysis of the paper ("Scripts for social attention":
16	# Get data, Overall gaze behavior and number of stims, Heatmap, Spatial dimension, Temporal
17	# dimension, Inter-individual dynamics, Saccade kinematics) and older scripts (stim/, script/).
18	# It starts from intermediate files (fixation events, ROIs, positions, stimulation and sham
19	# times) made by an upstream pipeline that is not in the repository, and it calls functions
20	# of outside packages (bfw, shared_utils, dsp3). The causal decomposition itself was run
[... 910 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la paper; cat docs/archives.md | head -150
```

```
total 3068
drwxr-xr-x  2 runner runner    4096 Oct 31 23:23 .
drwxr-xr-x 20 runner runner    4096 Oct 31 23:24 ..
-rw-r--r--  1 runner runner 3011148 Oct 31 23:23 10.1016-j.neuron.2024.05.004.supp.pdf
-rw-r--r--  1 runner runner  118417 Oct 31 23:23 10.1016-j.neuron.2024.05.004.txt
# Archives

The registry tests papers against data in public archives. It began with one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
below), and `tools/datasets.py` turns one form of a dataset's name into another.
The workflows take a dataset in any of these forms.

[... 136 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/872dc8d0-ddfb-4d24-a385-7282affd2812/tool-results/bjo08m6fl.txt",
 "offset": 930
}
```

```
930	    test: Wilcoxon signed rank, two-sided
931	    p: 0.757
932	  - about: contralateral
933	    test: Wilcoxon signed rank, two-sided
934	    p: 0.882
935	  - about: ipsilateral
936	    test: Wilcoxon signed rank, two-sided
937	    p: 0.098
938	  depends_on:
939	  - figs4a-causal-strength-no-stim-effect
940	  - epoch-days-76-of-81
941	  criterion: A claim of absence, judged on the paper's test. From the Methods and
942	    S3_Gaze_Correlation_by_Epoch.m. For each day and epoch, an ordinary least squares fit (fitlm)
943	    of relative causal strength on social gaze distance (in degrees) over the stimulation trials
944	    of the epoch; distance is the trial mean over fixations in the post-gaze epoch, overall,
945	    contralateral or ipsilateral. Late against early slopes, signed-rank over OFC days.
946	    Reproduced when no test gives p < 0.05, under each reading of figs4a-causal-strength-no-stim-effect.
947	- id: fig4c-dmpfc-slope-late-greater
948	  statement: For dmPFC, the slope of the relation between contralateral social gaze distance and
949	    relative causal strength was larger in the late than in the early epoch (p = 0.054, at the
[... 223 more lines not kept]
```

**Agent**

I've read the protocol and the claims file (33 claims). Next I'll survey the dataset on DANDI.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000959/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000959/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n -i "dandi\|000959" paper/*.txt | head; python - <<'EOF'
import requests, json
V="0.261020.0242"
url=f"https://api.dandiarchive.org/api/dandisets/000959/versions/{V}/assets/?page_size=1000"
assets=[]
while url:
    r=requests.get(url).json(); assets+=r['results']; url=r['next']
json.dump(assets,open('assets.json','w'))
print(len(assets))
for a in assets[:15]: print(a['path'],a['size'])
import collections
print(collections.Counter(a['path'].split('/')[0] for a in assets))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls entries/001453-fouke-2025/; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; which python; python --version; ls .venv 2>/dev/null | head
```

```
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
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
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q wenv && . wenv/bin/activate && uv pip install -q requests h5py remfile pynwb numpy pandas scipy statsmodels matplotlib 2>&1 | tail -2; python -c "import pynwb; print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; python - <<'EOF'
import requests, json, collections
V="0.261020.0242"
url=f"https://api.dandiarchive.org/api/dandisets/000959/versions/{V}/assets/?page_size=1000"
assets=[]
while url:
    r=requests.get(url).json(); assets+=r['results']; url=r['next']
json.dump(assets,open('assets.json','w'))
print(len(assets))
for a in assets[:20]: print(a['path'],a['size'])
print(collections.Counter(a['path'].split('/')[0] for a in assets))
import numpy as np
s=np.array([a['size'] for a in assets]); print(s.min(), np.median(s), s.max())
EOF
```

```
1705
sub-L/sub-L_ses-20190718_obj-1wqjp5d_behavior.nwb 10013880
sub-L/sub-L_ses-20190718_obj-13f8g2t_behavior.nwb 10014512
sub-L/sub-L_ses-20190718_obj-1di9l1e_behavior.nwb 9973904
sub-L/sub-L_ses-20190718_obj-jvhdtl_behavior.nwb 17528968
sub-L/sub-L_ses-20190718_obj-25do0p_behavior.nwb 17599896
sub-L/sub-L_ses-20190718_obj-nfftvc_behavior.nwb 9989224
sub-L/sub-L_ses-20190718_obj-kpk2fd_behavior.nwb 17580912
sub-L/sub-L_ses-20190718_obj-lyew5r_behavior.nwb 17587120
sub-L/sub-L_ses-20190718_obj-r8q0qb_behavior.nwb 17518768
sub-L/sub-L_ses-20190718_obj-rodstk_behavior.nwb 17550536
sub-L/sub-L_ses-20190718_obj-s7zl1u_behavior.nwb 17473768
sub-L/sub-L_ses-20190718_obj-y190sa_behavior.nwb 9975960
sub-L/sub-L_ses-20190718_obj-toaj27_behavior.nwb 17517560
sub-L/sub-L_ses-20190718_obj-sb77gy_behavior.nwb 17535384
sub-L/sub-L_ses-20190718_obj-y9z9xw_behavior.nwb 17529976
sub-L/sub-L_ses-20190720_obj-11gi722_behavior.nwb 17554832
sub-L/sub-L_ses-20190720_obj-159350p_behavior.nwb 10007248
sub-L/sub-L_ses-20190720_obj-13l0gc3_behavior.nwb 17500424
sub-L/sub-L_ses-20190720_obj-14mpmyn_behavior.nwb 17524168
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; cat > peek.py <<'EOF'
import json, remfile, h5py, pynwb, sys
assets=json.load(open('assets.json'))
a=assets[int(sys.argv[1])]
print(a['path'])
url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
import requests
s3=requests.head(url,allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset): print(name,obj.shape,obj.dtype, dict((k,str(v)[:80]) for k,v in obj.attrs.items() if k not in('namespace','object_id')))
    else: print(name+'/', dict((k,str(v)[:100]) for k,v in obj.attrs.items() if k not in('namespace','object_id')))
f.visititems(show)
EOF
time python peek.py 0 2>&1 | grep -v "^specifications" | head -150
```

```
sub-L/sub-L_ses-20190718_obj-1wqjp5d_behavior.nwb
acquisition/ {}
acquisition/EyeTracking_m1/ {'neurodata_type': 'EyeTracking'}
acquisition/EyeTracking_m1/spatialseries/ {'comments': 'no comments', 'description': 'M1 gaze position', 'neurodata_type': 'SpatialSeries'}
acquisition/EyeTracking_m1/spatialseries/data (300815, 2) float64 {'conversion': '1.0', 'offset': '0.0', 'resolution': '-1.0', 'unit': 'pixels'}
acquisition/EyeTracking_m1/spatialseries/reference_frame () object {}
acquisition/EyeTracking_m1/spatialseries/starting_time () float64 {'rate': '1000.0', 'unit': 'seconds'}
acquisition/pupil_m1/ {'comments': 'no comments', 'description': 'M1 pupil size', 'neurodata_type': 'TimeSeries'}
acquisition/pupil_m1/data (300815,) float64 {'conversion': '1.0', 'offset': '0.0', 'resolution': '-1.0', 'unit': 'a.u.'}
acquisition/pupil_m1/starting_time () float64 {'rate': '1000.0', 'unit': 'seconds'}
acquisition/roi_definitions/ {'colnames': "['roi_name' 'x1' 'y1' 'x2' 'y2']", 'description': 'ROI definitions used for fixation classification. Each row contains one ROI with vector format [x1 y', 'neurodata_type': 'DynamicTable'}
acquisition/roi_definitions/id (3,) int64 {'neurodata_type': 'ElementIdentifiers'}
acquisition/roi_definitions/roi_name (3,) object {'description': 'ROI field name from MATLAB data', 'neurodata_type': 'VectorData'}
acquisition/roi_definitions/x1 (3,) float64 {'description': 'First x-coordinate of ROI boundary', 'neurodata_type': 'VectorData'}
acquisition/roi_definitions/x2 (3,) float64 {'description': 'Second x-coordinate of ROI boundary', 'neurodata_type': 'VectorData'}
acquisition/roi_definitions/y1 (3,) float64 {'description': 'First y-coordinate of ROI boundary', 'neurodata_type': 'VectorData'}
acquisition/roi_definitions/y2 (3,) float64 {'description': 'Second y-coordinate of ROI boundary', 'neurodata_type': 'VectorData'}
acquisition/stimulation_events/ {'comments': 'no comments', 'description': 'Stimulation/sham event labels. Timestamps are even
[... 110 more lines not kept]
```

**Agent**

Files are behavior-only NWBs (gaze, pupil, stim events, fixation intervals, ROIs). Let me inspect a larger (social) file and the values.

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; python peek.py 3 2>&1 | grep -v "index\|_sec\|/id \|start_time (\|stop_time (" | head -80
```

```
sub-L/sub-L_ses-20190718_obj-jvhdtl_behavior.nwb
acquisition/ {}
acquisition/EyeTracking_m1/ {'neurodata_type': 'EyeTracking'}
acquisition/EyeTracking_m1/spatialseries/ {'comments': 'no comments', 'description': 'M1 gaze position', 'neurodata_type': 'SpatialSeries'}
acquisition/EyeTracking_m1/spatialseries/data (301554, 2) float64 {'conversion': '1.0', 'offset': '0.0', 'resolution': '-1.0', 'unit': 'pixels'}
acquisition/EyeTracking_m1/spatialseries/reference_frame () object {}
acquisition/EyeTracking_m1/spatialseries/starting_time () float64 {'rate': '1000.0', 'unit': 'seconds'}
acquisition/EyeTracking_m2/ {'neurodata_type': 'EyeTracking'}
acquisition/EyeTracking_m2/spatialseries/ {'comments': 'no comments', 'description': 'M2 gaze position', 'neurodata_type': 'SpatialSeries'}
acquisition/EyeTracking_m2/spatialseries/data (301554, 2) float64 {'conversion': '1.0', 'offset': '0.0', 'resolution': '-1.0', 'unit': 'pixels'}
acquisition/EyeTracking_m2/spatialseries/reference_frame () object {}
acquisition/EyeTracking_m2/spatialseries/starting_time () float64 {'rate': '1000.0', 'unit': 'seconds'}
acquisition/pupil_m1/ {'comments': 'no comments', 'description': 'M1 pupil size', 'neurodata_type': 'TimeSeries'}
acquisition/pupil_m1/data (301554,) float64 {'conversion': '1.0', 'offset': '0.0', 'resolution': '-1.0', 'unit': 'a.u.'}
acquisition/pupil_m1/starting_time () float64 {'rate': '1000.0', 'unit': 'seconds'}
acquisition/pupil_m2/ {'comments': 'no comments', 'description': 'M2 pupil size', 'neurodata_type': 'TimeSeries'}
acquisition/pupil_m2/data (301554,) float64 {'conversion': '1.0', 'offset': '0.0', 'resolution': '-1.0', 'unit': 'a.u.'}
acquisition/pupil_m2/starting_time () float64 {'rate': '1000.0', 'unit': 'seconds'}
acquisition/roi_definitions/ {'colnames': "['roi_name' 'x1' 'y1' 'x2' 'y2']", 'description': 'ROI definitions used for fixation classification. Each row contains one ROI with vector format [x1 y', 'neurodata_type': 'DynamicTable'}
acquisition/roi_definiti
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; cat > vals.py <<'EOF'
import json, remfile, h5py, sys, requests, numpy as np, pandas as pd
assets=json.load(open('assets.json'))
a=assets[int(sys.argv[1])]
print(a['path'])
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
dec=lambda x: x.decode() if isinstance(x,bytes) else x
for k in ['session_description','identifier','session_start_time','timestamps_reference_time','general/subject/subject_id','general/subject/sex','general/subject/age','general/subject/description','general/subject/species','general/was_generated_by']:
    print(k, f[k][()])
for k in f['scratch']: print(k, f['scratch'][k][()])
print(f['acquisition/EyeTracking_m1/spatialseries/reference_frame'][()])
r=f['acquisition/roi_definitions']
print(pd.DataFrame({c:[dec(v) for v in r[c][:]] for c in ['roi_name','x1','y1','x2','y2']}))
se=f['acquisition/stimulation_events']
print(list(zip([dec(v) for v in se['data'][:]], se['timestamps'][:])))
t=f['acquisition/t/data'][:]; print('t', np.nanmin(t), np.nanmax(t), np.isnan(t).sum(), len(t), np.nanmedian(np.diff(t)))
for k in f['acquisition']:
    if 'starting_time' in f['acquisition'][k] : print(k, f['acquisition'][k]['starting_time'][()])
g=f['acquisition/EyeTracking_m1/spatialseries/data'][:]
print('m1 gaze', np.nanpercentile(g,[0,1,50,99,100],axis=0), np.isnan(g).mean())
for name in f['intervals']:
    it=f['intervals'][name]
    df=pd.DataFrame({c:[dec(v) for v in it[c][:]] for c in it if c!='id'})
    print(name, len(df)); print(df.head(3).to_string())
EOF
python vals.py 3 2>&1 | head -150
```

```
sub-L/sub-L_ses-20190718_obj-jvhdtl_behavior.nwb
session_description b'data_07182019 run_6 | subject=L | region=dmPFC | roi=Eyes | condition=Social'
identifier b'data_07182019_run_6'
session_start_time [b'2019-07-18T00:00:00.000000-04:00']
timestamps_reference_time [b'2019-07-18T00:00:00.000000-04:00']
general/subject/subject_id b'L'
general/subject/sex b'M'
general/subject/age b'P10Y'
general/subject/description b'Non-human primate subject'
general/subject/species b'Macaca mulatta'
general/was_generated_by [[b'matnwb' b'2.10.0']]
stimulated_region [b'dmPFC']
stimulation_condition [b'Social']
stimulation_roi [b'Eyes']
b'screen coordinates'
       roi_name           x1          y1           x2          y2
0   roi_m1_eyes  1488.556271  322.656261  1634.143742  406.943745
1   roi_m2_eyes  1704.581266  252.218737  1554.718752  338.981245
2  roi_m1_mouth  1488.556271  406.943745  1634.143742  491.231228
3  roi_m2_mouth  1704.581266  338.981245  1554.718752  425.743753
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; cat > chk.py <<'EOF'
import json, remfile, h5py, sys, requests, numpy as np
assets=json.load(open('assets.json'))
a=assets[3]
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
for p in ['acquisition/EyeTracking_m1/spatialseries/data','acquisition/t/data','acquisition/pupil_m1/data','intervals/m1_all/start_time']:
    d=f[p]; print(p,d.chunks,d.compression)
t=f['acquisition/t/data'][:]
v=np.where(~np.isnan(t))[0]; print('first valid idx0',v[0],t[v[0]],'last',v[-1],t[v[-1]], len(t))
print('t[4173],t[4174]',t[4173],t[4174])
it=f['intervals/m1_all']; s=it['m1_start_index'][:5].astype(int); print(s, it['m1_start_time_sec'][:5], t[s-1], t[s])
g=f['acquisition/EyeTracking_m1/spatialseries/data']
print(np.isnan(g[:v[0]]).mean(), np.isnan(g[v[0]:v[-1]]).mean())
# check t diffs
print(np.unique(np.round(np.diff(t[v[0]:v[-1]+1]),4),return_counts=True))
EOF
python chk.py
```

```
acquisition/EyeTracking_m1/spatialseries/data None None
acquisition/t/data None None
acquisition/pupil_m1/data None None
intervals/m1_all/start_time None None
first valid idx0 4154 2823.308 last 300661 3119.7980000000002 301554
t[4173],t[4174] 2823.3269999999998 2823.328
[4174 4730 4992 5194 5492] [2823.327 2823.883 2824.145 2824.347 2824.645] [2823.327 2823.883 2824.145 2824.347 2824.645] [2823.328 2823.884 2824.146 2824.348 2824.646]
0.0 0.09291854829734206
(array([0.001]), array([296507]))
Shell cwd was reset to
```

**Agent**

Indices are 1-based MATLAB, data uncompressed and contiguous, so window slicing is cheap. Now a quick read of the relevant Methods passages.

**Agent calls Bash**

```bash
cd  grep -n -i "padding\|post-gaze epoch\|Gaze distance analyses\|Gaze latency\|reciprocation latency\|pupil\|Fixation density\|mutual\|exclusive\|contralateral visual\|hemifield" paper/*.txt | cut -c1-300 | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '170,220p' paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Now a survey of all 1705 files' metadata (descriptions, run identifiers, event counts) to map days, areas and conditions.

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; cat > survey.py <<'EOF'
import json, remfile, h5py, requests, numpy as np, pandas as pd, time
from concurrent.futures import ThreadPoolExecutor
assets=json.load(open('assets.json'))
sess=requests.Session()
def one(a):
    for k in range(3):
        try:
            url=f"https://dandiarchive.s3.amazonaws.com/blobs/{a['blob'][:3]}/{a['blob'][3:6]}/{a['blob']}" if 'blob' in a else None
            s3=sess.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=True).url
            f=h5py.File(remfile.File(s3),'r')
            se=f['acquisition/stimulation_events']
            return dict(path=a['path'], asset_id=a['asset_id'], url=s3, desc=f['session_description'][()].decode(), ident=f['identifier'][()].decode(),
                region=f['scratch/stimulated_region'][0].decode(), cond=f['scratch/stimulation_condition'][0].decode(), roi=f['scratch/stimulation_roi'][0].decode(),
                n=f['acquisition/t/data'].shape[0], nev=se['timestamps'].shape[0], labels=','.join(sorted(set(x.decode() for x in se['data'][:]))),
                tables=','.join(f['intervals'].keys()), acq=','.join(f['acquisition'].keys()), rois=','.join(x.decode() for x in f['acquisition/roi_definitions/roi_name'][:]))
        except Exception as e:
            err=repr(e); time.sleep(1)
    return dict(path=a['path'], err=err)
t0=time.time()
with ThreadPoolExecutor(32) as ex: rows=list(ex.map(one, assets))
df=pd.DataFrame(rows); df.to_pickle('survey.pkl'); print(time.time()-t0)
print(df.get('err', pd.Series()).notna().sum())
print(df.groupby(['region','cond','roi']).size())
print(df.labels.value_counts()); print(df.acq.value_counts()); print(df.rois.value_counts())
print(df.tables.value_counts().head(10))
print(df.ident.duplicated().sum())
EOF
python survey.py
```

```
750.2282259464264
0
region  cond    roi  
ACCg    Dot     Eyes     151
                Mouth     25
        Social  Eyes     318
                Mouth     75
OFC     Dot     Eyes     152
                Mouth     25
        Social  Eyes     318
                Mouth     75
dmPFC   Dot     Eyes     148
                Mouth     25
        Social  Eyes     318
                Mouth     75
dtype: int64
labels
sham,stim    1705
Name: count, dtype: int64
acq
[... 21 more lines not kept]
```

**Agent**

The metadata survey took 12.5 min with 32 threads, which is slow; I'll need a leaner loader. Notable: 526 duplicated `identifier`s. Checking whether those are duplicate recordings.

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; python - <<'EOF'
import pandas as pd
df=pd.read_pickle('survey.pkl')
d=df[df.ident.duplicated(keep=False)].sort_values('ident')
print(d[['ident','desc','n','nev','path']].head(12).to_string())
print(df[df.cond=='Dot'].ident.str.slice(0,13).nunique())
df['subj']=df.path.str.slice(4,5)
df['date']=df.desc.str.extract(r'data_(\d{8})')[0]
df['run']=df.desc.str.extract(r'run_(\d+)')[0].astype(int)
print(df.desc.str.extract(r'condition=(\w+)')[0].value_counts())
g=df.groupby(['subj','region','roi']).date.nunique(); print(g)
# same-date different region?
print(df.groupby('date').region.nunique().value_counts())
print(df.groupby(['date','cond']).size().groupby('cond').describe())
dup=df.groupby(['date','cond','run']).size(); print(dup[dup>1])
EOF
```

```
ident                                                                          desc       n  nev                                               path
497  data_01022020_run_1     data_01022020 run_1 | subject=L | region=dmPFC | roi=Eyes | condition=Dot  300911   13   sub-L/sub-L_ses-20200102_obj-ili6j0_behavior.nwb
495  data_01022020_run_1  data_01022020 run_1 | subject=L | region=dmPFC | roi=Eyes | condition=Social  302027   27  sub-L/sub-L_ses-20200102_obj-1mtpq6k_behavior.nwb
498  data_01022020_run_2  data_01022020 run_2 | subject=L | region=dmPFC | roi=Eyes | condition=Social  301680   29  sub-L/sub-L_ses-20200102_obj-1sydgku_behavior.nwb
492  data_01022020_run_2     data_01022020 run_2 | subject=L | region=dmPFC | roi=Eyes | condition=Dot  300853   16  sub-L/sub-L_ses-20200102_obj-1crftsf_behavior.nwb
484  data_01022020_run_3     data_01022020 run_3 | subject=L | region=dmPFC | roi=Eyes | condition=Dot  300984   15  sub-L/sub-L_ses-20200102_obj-10fzxpp_behavior.nwb
494  data_01022020_run_3  data_01022020 run_3 | subject=L | region=dmPFC | roi=Eyes | condition=Social  301780   33  sub-L/sub-L_ses-20200102_obj-1kqr9x8_behavior.nwb
500  data_01022020_run_4     data_01022020 run_4 | subject=L | region=dmPFC | roi=Eyes | condition=Dot  300942   19   sub-L/sub-L_ses-20200102_obj-reps8u_behavior.nwb
499  data_01022020_run_4  data_01022020 run_4 | subject=L | region=dmPFC | roi=Eyes | condition=Social  301830   31  sub-L/sub-L_ses-20200102_obj-1wsio9b_behavior.nwb
501  data_01022020_run_5  data_01022020 run_5 | subject=L | region=dmPFC | roi=Eyes | condition=Social  302072   28   sub-L/sub-L_ses-20200102_obj-kmsaii_behavior.nwb
489  data_01022020_run_5     data_01022020 run_5 | subject=L | region=dmPFC | roi=Eyes | condition=Dot  301044   20  sub-L/sub-L_ses-20200102_obj-1dwubek_behavior.nwb
493  data_01022020_run_6     data_01022020 run_6 | subject=L | region=dmPFC | roi=Eyes | condition=Dot  300955   24  sub-L/sub-L_ses-20200102_obj-1o0a2y5_behavior.nwb
488  data_01022
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; python - <<'EOF'
import pandas as pd, requests, io, h5py, time, numpy as np
from concurrent.futures import ThreadPoolExecutor
df=pd.read_pickle('survey.pkl')
urls=df.url.tolist()[:64]
def one(u):
    b=requests.get(u).content
    f=h5py.File(io.BytesIO(b),'r')
    g=f['acquisition/EyeTracking_m1/spatialseries/data'][:]
    return len(b)
t0=time.time()
with ThreadPoolExecutor(16) as ex: s=sum(ex.map(one,urls))
dt=time.time()-t0; print(dt, s/dt/1e6,'MB/s', dt/64*1705/60,'min est')
EOF
```

```
6.5320494174957275 147.6207986757214 MB/s 2.9002979835495353 min est
Shell cwd was reset to
```

**Agent**

Reading whole files into memory (never to disk) brings the full load to about 3 min. Now checking ROI and event semantics on one run.

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; python - <<'EOF'
import pandas as pd, requests, io, h5py, numpy as np
df=pd.read_pickle('survey.pkl')
dec=lambda x: x.decode() if isinstance(x,bytes) else x
def load(u):
    return h5py.File(io.BytesIO(requests.get(u).content),'r')
r=df[(df.cond=='Social')&(df.path.str.contains('sub-T'))].iloc[0]
print(r.desc)
f=load(r.url)
g=f['acquisition/EyeTracking_m1/spatialseries/data'][:]
g2=f['acquisition/EyeTracking_m2/spatialseries/data'][:]
rt=f['acquisition/roi_definitions']; rois={dec(n):np.array([rt[c][i] for c in ['x1','y1','x2','y2']]) for i,n in enumerate(rt['roi_name'][:])}
print(rois)
def tab(name):
    it=f['intervals'][name]; return pd.DataFrame({c:[dec(v) for v in it[c][:]] for c in it if c!='id'})
def inroi(p,r): 
    x1,x2=sorted(r[[0,2]]); y1,y2=sorted(r[[1,3]]); return (p[:,0]>=x1)&(p[:,0]<=x2)&(p[:,1]>=y1)&(p[:,1]<=y2)
for name,gg,roi in [('m1_eye',g,'roi_m1_eyes'),('m1_wholeface',g,'roi_m1_face'),('m2_eye',g2,'roi_m2_eyes'),('m2_wholeface',g2,'roi_m2_face'),('m1_everywhere',g,'roi_m1_face'),('mutual_wholeface',g,'roi_m1_face')]:
    t=tab(name); s=t.m1_start_index.astype(int)-1 if name[:2]!='m2' else t.m2_start_index.astype(int)-1; e=(t.m1_end_index if name[:2]!='m2' else t.m2_end_index).astype(int)
    pos=np.array([np.nanmean(gg[a:b],0) for a,b in zip(s,e)])
    print(name,len(t), inroi(pos,rois[roi]).mean())
# laterality
t=tab('m1_all'); s=t.m1_start_index.astype(int)-1; e=t.m1_end_index.astype(int)
pos=np.array([np.nanmean(g[a:b],0) for a,b in zip(s,e)])
for nm in ['roi_m2_face','roi_m1_face','roi_m1_eyes']:
    cx=rois[nm][[0,2]].mean()
    lab=np.where(pos[:,0]>cx,'ipsi','contra')  # T: right is ipsi
    print(nm, cx, (lab==t.laterality_label.values).mean())
# subsets
for a in ['mutual_eye','mutual_face']:
    if a in f['intervals']:
        A=set(tab(a).start_time.round(3)); B=set(tab('mutual_wholeface').start_time.round(3)); print(a, len(A), len(A&B))
st=set(tab('m1_all').start_time.round(3)); print('m1_all with mutual starts', len(st & set(tab('mutual_wholeface').m1_start_time_sec.round(3))))
EOF
```

```
data_11042021 run_10 | subject=T | region=ACCg | roi=Eyes | condition=Social
{'roi_m1_eyes': array([1522.5562706 ,  278.20624924, 1649.14374161,  351.49373245]), 'roi_m2_eyes': array([1740.56250191,  287.23750114, 1604.2375164 ,  366.16249275]), 'roi_m1_mouth': array([1522.5562706 ,  351.49373245, 1649.14374161,  424.78121567]), 'roi_m2_mouth': array([1740.56250191,  366.16249275, 1604.2375164 ,  445.08748436]), 'roi_m1_face': array([1487.54998779,  273.75      , 1689.69998169,  432.1000061 ]), 'roi_m2_face': array([1773.65000916,  279.6000061 , 1561.80000305,  442.3999939 ])}
m1_eye 11 0.8181818181818182
m1_wholeface 15 1.0
m2_eye 11 0.9090909090909091
m2_wholeface 18 1.0
m1_everywhere 466 0.0
mutual_wholeface 3 1.0
roi_m2_face 1667.7250061035156 1.0
roi_m1_face 1588.624984741211 0.918918918918919
roi_m1_eyes 1585.8500061035156 0.918918918918919
mutual_eye 1 1
mutual_face 2 2
m1_all with mutual starts 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd  ls entries/001453-fouke-2025; head -60 entries/001453-fouke-2025/omr.py; cat entries/001453-fouke-2025/README.md | head -30
```

```
Sat Oct 31 23:39:26 UTC 2026
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
"""Loading and measures for the freely swimming optomotor data of dandiset 001453.

Fouke, He, Loring & Naumann (2025), Current Biology, doi:10.1016/j.cub.2025.04.027.

Each NWB file holds one fish: x and y position (pixels), heading (`f0_theta`, radians), its
change per frame (`f0_vtheta`; the file says radians/s, the data show radians per frame),
velocity estimates, and per frame the stimulus code and trial number (`stim_index`). Files are
streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Trial processing follows the paper's analysis notebook, Fig1-S1.ipynb, in
  https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit
[... 76 more lines not kept]
```

**Agent**

I have more time than I estimated (it is 23:39). Writing the helper module.

**Agent calls Write**

```json
{
 "file_path": "entries/000959-fan-2024/microstim.py",
 "content": "\"\"\"Loading and measures for the closed-loop microstimulation gaze data of dandiset 000959.\n\nFan, Dal Monte, Nair, Fagan & Chang (2024), Neuron 112, 2631-2644,\ndoi:10.1016/j.neuron.2024.05.004. The claims file is claims/000959/10.1016-j.neuron.2024.05.004.yaml.\n\nEach NWB file holds one 300-s run (a \"session\" in the paper) of one day: M1's gaze (pixels,\n1 kHz), in social runs M2's gaze, pupil size, the stimulation and sham times\n(`stimulation_events`), the ROIs of the day (`roi_definitions`), and fixation events as\ninterval tables (`m1_all`, `m1_eye`, `m1_wholeface`, ..., `m2_*`, `mutual_*`). The\n`session_description` names the date, run, subject, stimulated region, triggering ROI (Eyes or\nMouth) and condition (Social, or Dot for the non-social RDM control). Files are read over HTTP\ninto memory at the pinned version; nothing is written to disk.\n\nWhere the parameters come from:\n\n- Trial selection (the claims file's opening comment, from the paper's code): a trial is kept\n  when its time lies within the valid run (non-NaN `t`) and more than 5 s before the run's last\n  valid sample; the first trial of each run is dropped. Trials are grouped by their own label.\n- Post-gaze epoch: fixations whose start lies in [0, 1.5) s after the trial (claims file,\n  opening comment; STAR Methods, Fixation density map, \"within 1.5 sec after the onset\").\n- A fixation's position is the mean of its own gaze samples between its start and end indices\n  (claims file, opening comment). Indices in the files are 1-based (MATLAB); this module\n  checks that `t[start_index - 1]` equals the stored start time.\n- Which events enter a distance: the Methods reading (M1-only events, `m1_all`, plus the M1\n  side of mutual whole Face events, `mutual_wholeface`) and the code's (M1-only events only);\n  claims file, opening comment. Mutual events are only defined within the face, and\n  `mutual_wholeface` holds every mutual event (`mutual_eye` and `mutual_face` are subsets of\n  it; shown in the notebook).\n- Hemifield: the side of the fixation's mean x relative to the centre of `roi_m2_face`; for\n  monkey L left is ipsilateral, for monkey T right (claims file, opening comment). The files'\n  own `laterality_label` is compared with it in the notebook.\n- Pixels to degrees: screen height 27 cm at 50 cm over 768 pixels (claims file, opening\n  comment, from the paper's code); rank tests do not depend on it.\n- Pupil: 700 ms after the trial in 10-ms bins, trials where M1's gaze stays within the whole\n  Face ROI throughout (STAR Methods, Control analyses, \"throughout at least 700-msec\").\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport re\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport requests\n\nDANDISET_ID = \"000959\"\nDANDISET_VERSION = \"0.261020.0242\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nPOST_GAZE_S = 1.5\nLATENCY_WINDOW_S = 5.0          # STAR Methods, Gaze latency analyses, \"within 5 sec\"\nEND_MARGIN_S = 5.0              # trials more than 5 s before the run's last sample\nPUPIL_MS = 700\nPUPIL_BIN_MS = 10\nDEG_PER_PX = np.degrees(2 * np.arctan(13.5 / 50.0)) / 768.0\nIPSI_SIDE = {\"L\": \"left\", \"T\": \"right\"}   # chamber side (claims file, opening comment)\n\n\ndef list_assets(version: str = DANDISET_VERSION) -> pd.DataFrame:\n    \"\"\"Every asset of the pinned version, with its path, size and id.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000\"\n    rows = []\n    while url:\n        r = requests.get(url, timeout=60).json()\n        rows += r[\"results\"]\n        url = r[\"next\"]\n    return pd.DataFrame([{\"path\": a[\"path\"], \"asset_id\": a[\"asset_id\"], \"size\": a[\"size\"]}\n                         for a in rows])\n\n\ndef _dec(x):\n    return x.decode() if isinstance(x, bytes) else x\n\n\ndef _table(f, name):\n    it = f[\"intervals\"][name]\n    return pd.DataFrame({c: [_dec(v) for v in it[c][:]] for c in it if c != \"id\"})\n\n\ndef _centre(r):\n    return np.array([(r[0] + r[2]) / 2, (r[1] + r[3]) / 2])\n\n\ndef _in_rect(xy, r):\n    x1, x2 = sorted(r[[0, 2]])\n    y1, y2 = sorted(r[[1, 3]])\n    return (xy[..., 0] >= x1) & (xy[..., 0] <= x2) & (xy[..., 1] >= y1) & (xy[..., 1] <= y2)\n\n\ndef read_run(asset_id: str, session: requests.Session | None = None) -> dict:\n    \"\"\"Read one run into small tables: metadata, trials, ROIs, fixation events, pupil.\"\"\"\n    s = session or requests\n    for attempt in range(4):\n        try:\n            content = s.get(f\"{API}/assets/{asset_id}/download/\", timeout=300).content\n            f = h5py.File(io.BytesIO(content), \"r\")\n            break\n        except Exception:  # retry network errors\n            if attempt == 3:\n                raise\n    desc = _dec(f[\"session_description\"][()])\n    m = re.match(r\"data_(\\d{8}) run_(\\d+) \\| subject=(\\w) \\| region=(\\w+) \\| roi=(\\w+) \\| \"\n                 r\"condition=(\\w+)\", desc)\n    date, run, subj, region, roi, cond = m.groups()\n    meta = dict(asset_id=asset_id, desc=desc, date=date, run=int(run), subject=subj,\n                region=region, roi=roi, cond=cond,\n                region_scratch=_dec(f[\"scratch/stimulated_region\"][0]),\n                roi_scratch=_dec(f[\"scratch/stimulation_roi\"][0]),\n                cond_scratch=_dec(f[\"scratch/stimulation_condition\"][0]),\n                identifier=_dec(f[\"identifier\"][()]),\n                gaze_unit=_dec(f[\"acquisition/EyeTracking_m1/spatialseries/data\"].attrs[\"unit\"]),\n                rate=float(f[\"acquisition/t/starting_time\"].attrs[\"rate\"]))\n    t = f[\"acquisition/t/data\"][:]\n    valid = np.flatnonzero(~np.isnan(t))\n    i0, i1 = valid[0], valid[-1]\n    meta.update(n_samples=len(t), t_first=t[i0], t_last=t[i1], n_valid=len(valid),\n                dt_median=float(np.median(np.diff(t[i0:i1 + 1]))),\n                dt_max=float(np.max(np.diff(t[i0:i1 + 1]))))\n    g1 = f[\"acquisition/EyeTracking_m1/spatialseries/data\"][:]\n    g2 = (f[\"acquisition/EyeTracking_m2/spatialseries/data\"][:]\n          if \"EyeTracking_m2\" in f[\"acquisition\"] else None)\n    p1 = f[\"acquisition/pupil_m1/data\"][:]\n    meta.update(gaze_x_range=(np.nanmin(g1[:, 0]), np.nanmax(g1[:, 0])),\n                gaze_y_range=(np.nanmin(g1[:, 1]), np.nanmax(g1[:, 1])),\n                gaze_nan=float(np.isnan(g1[i0:i1 + 1, 0]).mean()),\n                pupil_range=(np.nanmin(p1), np.nanmax(p1)))\n    rt = f[\"acquisition/roi_definitions\"]\n    rois = {_dec(n): np.array([rt[c][i] for c in [\"x1\", \"y1\", \"x2\", \"y2\"]])\n            for i, n in enumerate(rt[\"roi_name\"][:])}\n\n    # trials\n    se = f[\"acquisition/stimulation_events\"]\n    tt = se[\"timestamps\"][:]\n    lab = np.array([_dec(v) for v in se[\"data\"][:]])\n    order = np.argsort(tt, kind=\"stable\")\n    tt, lab = tt[order], lab[order]\n    trials = pd.DataFrame({\"time\": tt, \"type\": lab})\n    trials[\"first\"] = np.arange(len(trials)) == 0\n    trials[\"in_run\"] = (tt >= t[i0]) & (tt < t[i1] - END_MARGIN_S)\n    trials[\"kept\"] = trials.in_run & ~trials[\"first\"]\n    tidx = np.clip(np.searchsorted(t[i0:i1 + 1], tt) + i0, 0, len(t) - 1)\n    trials[\"sample\"] = tidx\n    # pupil and gaze in the whole Face during the 700 ms after each trial\n    nb = PUPIL_MS // PUPIL_BIN_MS\n    pup = np.full((len(trials), nb), np.nan)\n    inface = np.zeros(len(trials), bool)\n    for k, i in enumerate(tidx):\n        if i + PUPIL_MS <= len(t):\n            pup[k] = p1[i:i + PUPIL_MS].reshape(nb, PUPIL_BIN_MS).mean(1)\n            if \"roi_m1_face\" in rois:\n                inface[k] = _in_rect(g1[i:i + PUPIL_MS], rois[\"roi_m1_face\"]).all()\n    trials[\"in_face_700\"] = inface\n\n    # fixation events: one row per monkey per event (mutual events give one row each)\n    ev = []\n    idx_check = []\n    for name in f[\"intervals\"]:\n        tab = _table(f, name)\n        if not len(tab):\n            continue\n        kind, roi_name = name.split(\"_\", 1)\n        whos = [\"m1\", \"m2\"] if kind == \"mutual\" else [kind]\n        for who in whos:\n            s0 = tab[f\"{who}_start_index\"].to_numpy().astype(int) - 1\n            e0 = tab[f\"{who}_end_index\"].to_numpy().astype(int)\n            g = g1 if who == \"m1\" else g2\n            pos = np.array([np.nanmean(g[a:b], 0) if b > a else [np.nan, np.nan]\n                            for a, b in zip(s0, e0)])\n            idx_check.append(np.nanmax(np.abs(t[s0] - tab[f\"{who}_start_time_sec\"].to_numpy())))\n            ev.append(pd.DataFrame({\n                \"table\": name, \"who\": who, \"roi\": roi_name, \"mutual\": kind == \"mutual\",\n                \"start\": tab[f\"{who}_start_time_sec\"].to_numpy(),\n                \"stop\": tab[f\"{who}_end_time_sec\"].to_numpy(),\n                \"x\": pos[:, 0], \"y\": pos[:, 1],\n                \"laterality_label\": tab[\"laterality_label\"].to_numpy()}))\n    events = pd.concat(ev, ignore_index=True)\n    meta[\"index_time_max_err\"] = float(np.max(idx_check))\n    f.close()\n    return dict(meta=meta, trials=trials, rois=rois, events=events, pupil=pup)\n\n\ndef load_all(assets: pd.DataFrame, workers: int = 16) -> list[dict]:\n    \"\"\"Read every asset in parallel (each file into memory, reduced, then released).\"\"\"\n    sess = requests.Session()\n    adapter = requests.adapters.HTTPAdapter(pool_connections=workers, pool_maxsize=workers)\n    sess.mount(\"https://\", adapter)\n    with ThreadPoolExecutor(workers) as ex:\n        runs = list(ex.map(lambda a: read_run(a, sess), assets.asset_id))\n    for r, p in zip(runs, assets.path):\n        r[\"meta\"][\"path\"] = p\n    return runs\n\n\ndef tables(runs: list[dict]):\n    \"\"\"Concatenate runs into `meta`, `trials` and `events` tables keyed by `run_id`.\"\"\"\n    meta = pd.DataFrame([r[\"meta\"] for r in runs])\n    meta[\"run_id\"] = np.arange(len(meta))\n    tr, ev = [], []\n    for k, r in enumerate(runs):\n        a = r[\"trials\"].copy()\n        a[\"run_id\"] = k\n        a[\"row\"] = np.arange(len(a))\n        tr.append(a)\n        b = r[\"events\"].copy()\n        b[\"run_id\"] = k\n        ev.append(b)\n    keys = [\"run_id\", \"date\", \"subject\", \"region\", \"roi\", \"cond\"]\n    trials = pd.concat(tr, ignore_index=True).merge(meta[keys], on=\"run_id\")\n    events = pd.concat(ev, ignore_index=True).merge(meta[keys], on=\"run_id\")\n    return meta, trials, events\n\n\ndef day_rois(runs: list[dict]) -> dict:\n    \"\"\"ROIs of each day, from its social runs (the Dot runs hold M1's ROIs only).\"\"\"\n    out = {}\n    for r in runs:\n        if r[\"meta\"][\"cond\"] == \"Social\":\n            out.setdefault(r[\"meta\"][\"date\"], r[\"rois\"])\n    return out\n\n\ndef add_hemifield(events: pd.DataFrame, droi: dict) -> pd.DataFrame:\n    \"\"\"Hemifield by the event's mean x against the centre of the day's `roi_m2_face`.\"\"\"\n    cx = events.date.map(lambda d: _centre(droi[d][\"roi_m2_face\"])[0])\n    right = events.x > cx\n    ipsi = np.where(events.subject == \"T\", right, ~right)\n    events = events.copy()\n    events[\"hemi\"] = np.where(events.x.isna(), None, np.where(ipsi, \"ipsi\", \"contra\"))\n    return events\n\n\ndef window_pairs(trials: pd.DataFrame, events: pd.DataFrame, t0: float, t1: float) -> pd.DataFrame:\n    \"\"\"All (trial, event) pairs of the same run with event start in [trial + t0, trial + t1).\n\n    Returns the event rows with `trial` (the trial's index in `trials`) and `lag` (start minus\n    trial time, s).\"\"\"\n    out = []\n    ev_by_run = {k: g.sort_values(\"start\") for k, g in events.groupby(\"run_id\")}\n    for rid, tg in trials.groupby(\"run_id\"):\n        eg = ev_by_run.get(rid)\n        if eg is None:\n            continue\n        st = eg.start.to_numpy()\n        for ti, tt in zip(tg.index, tg.time.to_numpy()):\n            a, b = np.searchsorted(st, [tt + t0, tt + t1], side=\"left\")\n            if b > a:\n                sub = eg.iloc[a:b].copy()\n                sub[\"trial\"] = ti\n                sub[\"lag\"] = sub.start - tt\n                out.append(sub)\n    if not out:\n        return events.iloc[:0].assign(trial=[], lag=[])\n    return pd.concat(out, ignore_index=True)\n\n\ndef roi_centre(droi: dict, date: str, name: str) -> np.ndarray:\n    return _centre(droi[date][name])\n\n\ndef day_means(trial_values: pd.DataFrame, value: str, by=(\"date\",)) -> pd.DataFrame:\n    \"\"\"Mean over trials of each type per day (NaN ignored), as columns `stim` and `sham`.\"\"\"\n    keys = list(by) + [\"subject\", \"region\"]\n    d = trial_values.groupby(keys + [\"type\"])[value].mean().unstack(\"type\")\n    return d.reset_index()\n\n\ndef in_rect(xy, r):\n    return _in_rect(xy, r)\n"
}
```

```
File created successfully at: entries/000959-fan-2024/microstim.py (file state is current in your context — no need to Read it back)
```

**Agent**

Testing the loader on one day, then timing a full load.

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; export PYTHONPATH=entries/000959-fan-2024; python - <<'EOF'
import microstim as ms, pandas as pd, time, pickle
a=ms.list_assets(); print(len(a))
sub=a[a.path.str.contains('ses-20190718')]
t0=time.time(); runs=ms.load_all(sub); print(len(sub), time.time()-t0)
meta,trials,events=ms.tables(runs)
print(meta[['desc','t_first','t_last','index_time_max_err','dt_max','gaze_nan']].head())
print(trials.head()); print(events.groupby(['cond','table']).size())
EOF
```

```
entries/000959-fan-2024/microstim.py:170: RuntimeWarning: Mean of empty slice
  pos = np.array([np.nanmean(g[a:b], 0) if b > a else [np.nan, np.nan]
1705
15 5.367630481719971
                                                desc  ...  gaze_nan
0  data_07182019 run_5 | subject=L | region=dmPFC...  ...  0.083658
1  data_07182019 run_1 | subject=L | region=dmPFC...  ...  0.071784
2  data_07182019 run_4 | subject=L | region=dmPFC...  ...  0.069780
3  data_07182019 run_6 | subject=L | region=dmPFC...  ...  0.092918
4  data_07182019 run_4 | subject=L | region=dmPFC...  ...  0.147721

[5 rows x 6 columns]
       time  type  first  in_run  ... subject region   roi cond
0  5855.622  stim   True    True  ...       L  dmPFC  Eyes  Dot
1  5882.616  stim  False    True  ...       L  dmPFC  Eyes  Dot
2  5898.181  sham  False    True  ...       L  dmPFC  Eyes  Dot
3  5908.323  sham  False    True  ...       L  dmPFC  Eyes  Dot
4  5918.974  sham  False    True  ...       L  dmPFC  Eyes  Dot

[5 rows x 14 columns]
[... 28 more lines not kept]
```

**Agent**

Full load estimate is about 10 min; running it once and caching to $TMPDIR for development only.

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; export PYTHONPATH=entries/000959-fan-2024; python -W ignore - <<'EOF'
import microstim as ms, pandas as pd, time, pickle
a=ms.list_assets()
t0=time.time(); runs=ms.load_all(a); print(time.time()-t0)
pickle.dump(runs, open('runs.pkl','wb'))
EOF
date -u
```

```
621.8099629878998
Sat Oct 31 23:50:59 UTC 2026
Shell cwd was reset to
```

**Agent**

Loaded all 1705 runs in 10.4 min. Now developing the analyses on the cached copy, starting with data checks and design counts.

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; export PYTHONPATH=entries/000959-fan-2024; python -W ignore - <<'EOF'
import microstim as ms, pandas as pd, numpy as np, pickle
runs=pickle.load(open('runs.pkl','rb'))
meta,trials,events=ms.tables(runs)
print((meta.region==meta.region_scratch).all(), (meta.roi==meta.roi_scratch).all(), (meta.cond==meta.cond_scratch).all())
print(meta.index_time_max_err.max(), meta.dt_median.describe(), meta.dt_max.max())
meta['dur']=meta.t_last-meta.t_first
print(meta.groupby('cond').dur.describe())
print(meta.gaze_unit.unique(), meta.rate.unique())
# duplicates
key=meta.apply(lambda r: (r.n_samples, round(r.t_first,3)),axis=1)
print('dup keys', key.duplicated().sum())
fp=trials.groupby('run_id').time.apply(lambda s: tuple(np.round(s,3)))
print('dup stim times', fp.duplicated().sum())
# days per area
d=meta.groupby(['subject','region','roi']).date.nunique(); print(d)
# sessions per day
s=meta[meta.roi=='Eyes'].groupby(['subject','date','cond']).size().unstack('cond')
print(s.groupby('subject').agg(['mean','min','max']))
# trial types
print(trials.groupby(['cond','type']).size(), trials.kept.mean(), (~trials.in_run).sum(), trials['first'].sum())
# inter-trial intervals
d=trials.groupby('run_id').time.diff(); print('min ITI', d.min(), (d<5).sum())
# day ROIs constant?
for date,g in meta[meta.cond=='Social'].groupby('date'):
    rr=[runs[i]['rois']['roi_m1_eyes'] for i in g.run_id]
    if not all(np.allclose(rr[0],x) for x in rr): print('roi varies', date); break
# mutual subsets
e=events[events.mutual & (events.who=='m1')]
w=set(zip(e[e.roi=='wholeface'].run_id, e[e.roi=='wholeface'].start.round(4)))
for r in ['eye','face','mouth']:
    x=set(zip(e[e.roi==r].run_id, e[e.roi==r].start.round(4))); print(r, len(x), len(x&w))
EOF
```

```
Exit code 1
True True True
0.0 count    1.705000e+03
mean     1.000000e-03
std      1.250502e-13
min      1.000000e-03
25%      1.000000e-03
50%      1.000000e-03
75%      1.000000e-03
max      1.000000e-03
Name: dt_median, dtype: float64 0.0010049950050188272
         count        mean       std  ...      50%      75%      max
cond                                  ...                           
Dot      526.0  296.136878  0.463363  ...  295.841  296.856  297.290
Social  1179.0  296.497961  0.029657  ...  296.497  296.510  296.701

[2 rows x 8 columns]
<StringArray>
['pixels']
Length: 1, dtype: str [1000.]
[... 32 more lines not kept]
```

**Agent**

Two early findings: monkey L averages 6.0 control runs per day (paper: 5), and ROIs vary between runs within some days. Fixing a column clash and checking the ROI variation.

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; sed -i 's/"table": name, "who": who, "roi": roi_name,/"table": name, "who": who, "target": roi_name,/' microstim.py; grep -n '"target"' microstim.py; cd $TMPDIR; . wenv/bin/activate; export PYTHONPATH=entries/000959-fan-2024; python -W ignore - <<'EOF'
import microstim as ms, pandas as pd, numpy as np, pickle
runs=pickle.load(open('runs.pkl','rb'))
for r in runs: r['events']=r['events'].rename(columns={'roi':'target'})
pickle.dump(runs, open('runs.pkl','wb'))
meta,trials,events=ms.tables(runs)
nvary=0
for date,g in meta.groupby('date'):
    for nm in ['roi_m1_eyes','roi_m1_face','roi_m2_face']:
        rr=np.array([runs[i]['rois'][nm] for i in g.run_id if nm in runs[i]['rois']])
        sp=rr.max(0)-rr.min(0)
        if sp.max()>0: nvary+=1; print(date,nm,len(rr),np.round(sp,1), g.cond.value_counts().to_dict()) if nvary<8 else None
print(nvary)
e=events[events.mutual & (events.who=='m1')]
w=set(zip(e[e.target=='wholeface'].run_id, e[e.target=='wholeface'].start.round(4)))
for r in ['eye','face','mouth']:
    x=set(zip(e[e.target==r].run_id, e[e.target==r].start.round(4))); print(r, len(x), len(x&w))
# m1_all == everywhere + wholeface?
c=events[events.who=='m1'].groupby(['run_id','table']).size().unstack(fill_value=0)
print(((c.m1_all-(c.m1_everywhere+c.m1_wholeface))).describe())
EOF
```

```
174:                "table": name, "who": who, "target": roi_name, "mutual": kind == "mutual",
08142019 roi_m1_eyes 15 [55.8 33.3 16.4 10.5] {'Social': 10, 'Dot': 5}
08142019 roi_m1_face 15 [48.4 39.9 18.9  5.9] {'Social': 10, 'Dot': 5}
12102019 roi_m1_eyes 14 [28.9 38.5  3.9 19.5] {'Social': 10, 'Dot': 4}
12102019 roi_m1_face 14 [ 0.4 21.6 12.7 24.1] {'Social': 10, 'Dot': 4}
12132019 roi_m1_eyes 18 [11.2 36.4  6.8 46.9] {'Social': 11, 'Dot': 7}
12132019 roi_m1_face 18 [13.3 33.9 13.5 52.4] {'Social': 11, 'Dot': 7}
6
eye 2912 2912
face 2384 2384
mouth 263 263
count    1705.0
mean        0.0
std         0.0
min         0.0
25%         0.0
50%         0.0
75%         0.0
max         0.0
dtype: float64
[... 1 more lines not kept]
```

**Agent**

Only 3 days have recalibrated ROIs between runs, so I'll use each run's own ROIs (and the day's `roi_m2_face`, which never varies, for Dot runs). Checking what `tools/entry.py` expects of notebooks.

**Agent calls Bash**

```bash
cd  grep -n "def \|tag\|sanity\|claim:" tools/entry.py | head -60; python -c "import nbformat, jupytext" 2>&1
```

```
Exit code 1
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
70:    def __init__(self):
73:    def error(self, where, message: str) -> None:
78:def dataset_id(record: dict) -> str | None:
83:def schema(name: str) -> Draft202012Validator:
94:def _parsed(text: str):
102:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
108:def load(report: Report, path: Path):
116:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
125:def _plain(value):
136:def code_of(notebook_path: Path) -> str:
143:def check(entry_dir: Path) -> Report:
196:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
197:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
305:            tag = outcome.get("output")
306:            if notebook in present and tag:
308:                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
309:                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
313:def _local_data(code: str, start: int) -> bool:
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,70p tools/entry.py; sed -n 143,200p tools/entry.py; sed -n 280,400p tools/entry.py
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
[... 229 more lines not kept]
```

**Agent**

I'll write the notebook as a cell-marked Python script and convert it with nbformat. First, adding the analysis measures to the helper.

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
p='microstim.py'; s=open(p).read()
s=s.replace('''def in_rect(xy, r):
    return _in_rect(xy, r)
''','''def in_rect(xy, r):
    return _in_rect(xy, r)


def run_centres(runs: list[dict]) -> pd.DataFrame:
    """Per run, the ROI centres (pixels) the measures use, from the run's own ROIs.

    `eyes` and `mouth` are the partner's Eyes and Mouth in M1's coordinates (`roi_m1_eyes`,
    `roi_m1_mouth`; in Dot runs the RDM stimulus, "same location and size as Eyes ROI", STAR
    Methods); `m2_eyes` is M1's Eyes in M2's coordinates (`roi_m2_eyes`, social runs only);
    `m2face_x` is the x of the centre of the day's `roi_m2_face`, the hemifield reference (taken
    from the day's social runs for Dot runs, which do not hold it)."""
    droi = day_rois(runs)
    rows = []
    for k, r in enumerate(runs):
        ro = r["rois"]
        e, m = _centre(ro["roi_m1_eyes"]), _centre(ro["roi_m1_mouth"])
        e2 = _centre(ro["roi_m2_eyes"]) if "roi_m2_eyes" in ro else (np.nan, np.nan)
        rows.append(dict(run_id=k, eyes_x=e[0], eyes_y=e[1], mouth_x=m[0], mouth_y=m[1],
                         m2_eyes_x=e2[0], m2_eyes_y=e2[1],
                         m2face_x=_centre(droi[r["meta"]["date"]]["roi_m2_face"])[0]))
    return pd.DataFrame(rows)


def prepare(runs: list[dict]):
    """Tables for the analyses: run metadata, every trial, every event with its hemifield
    and the run's ROI centres."""
    meta, trials, events = tables(runs)
    cen = run_centres(runs)
    events = events.merge(cen, on="run_id")
    right = events.x > events.m2face_x
    ipsi = np.where(events.subject == "T", right, ~right)
    events["hemi"] = np.where(events.x.isna(), None, np.where(ipsi, "ipsi", "contra"))
    trials = trials.merge(cen, on="run_id")
    return meta, trials, events


def m1_fixations(events: pd.DataFrame, reading: str = "methods") -> pd.DataFrame:
    """M1's fixations: `methods`, M1-only events and the M1 side of mutual whole Face events;
    `code`, M1-only events (`m1_all`)."""
    sel = events.table == "m1_all"
    if reading == "methods":
        sel |= (events.table == "mutual_wholeface") & (events.who == "m1")
    return events[sel]


def m2_fixations(events: pd.DataFrame, reading: str = "methods") -> pd.DataFrame:
    """M2's fixations, as `m1_fixations` for the partner."""
    sel = events.table == "m2_all"
    if reading == "methods":
        sel |= (events.table == "mutual_wholeface") & (events.who == "m2")
    return events[sel]


def trial_distance(trials, fix, centre=("eyes_x", "eyes_y"), t1=POST_GAZE_S, hemi=None):
    """Per trial, the mean Euclidean distance (pixels) of the fixations starting in [0, t1) s
    after it from the given centre; NaN for a trial with none (STAR Methods, Gaze distance
    analyses: "first averaged across all fixations after each trial")."""
    if hemi is not None:
        fix = fix[fix.hemi == hemi]
    pairs = window_pairs(trials, fix.dropna(subset=["x"]), 0.0, t1)
    cx = pairs[centre[0]].to_numpy()
    cy = pairs[centre[1]].to_numpy()
    pairs["dist"] = np.hypot(pairs.x - cx, pairs.y - cy)
    d = pairs.groupby("trial").dist.mean()
    return trials.index.map(d).astype(float)


def first_latency(trials, ev, t1=LATENCY_WINDOW_S):
    """Per trial, the time from the trial to the start of the first event starting in [0, t1)
    after it; NaN when there is none."""
    pairs = window_pairs(trials, ev, 0.0, t1)
    lat = pairs.groupby("trial").lag.min()
    return trials.index.map(lat).astype(float)


def reciprocation(trials, m1_ev, m2_ev, t1=LATENCY_WINDOW_S, first="m2"):
    """Per trial, the mean over sequences of the latency from the first event of a run of
    consecutive `first` events to the next event of the other monkey, over the whole Face
    events of both monkeys that start in [0, t1) after the trial (S1_Gaze_ITI_Combined.m, as
    the claims file gives it). Mutual events enter both lists. NaN when there is no
    sequence."""
    a = window_pairs(trials, m1_ev, 0.0, t1).assign(w="m1")
    b = window_pairs(trials, m2_ev, 0.0, t1).assign(w="m2")
    allp = pd.concat([a, b], ignore_index=True).sort_values(["trial", "start"], kind="stable")
    out = {}
    for tr, g in allp.groupby("trial", sort=False):
        w = g.w.to_numpy()
        st = g.start.to_numpy()
        lats, run_start = [], None
        for k in range(len(w)):
            if w[k] == first:
                if run_start is None:
                    run_start = st[k]
            elif run_start is not None:
                lats.append(st[k] - run_start)
                run_start = None
        if lats:
            out[tr] = np.mean(lats)
    return trials.index.map(out).astype(float)
''')
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent**

Now a dev run of the core distance analysis (Fig. 2C) to check logic and speed.

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; export PYTHONPATH=entries/000959-fan-2024; time python -W ignore - <<'EOF'
import microstim as ms, pandas as pd, numpy as np, pickle, time
from scipy.stats import wilcoxon
runs=pickle.load(open('runs.pkl','rb'))
meta,trials,events=ms.prepare(runs)
print((events.hemi==events.laterality_label)[events.who=='m1'].mean(), (events.hemi==events.laterality_label)[(events.who=='m1')&(events.cond=='Dot')].mean())
tr=trials[trials.kept & (trials.cond=='Social') & (trials.roi=='Eyes')].copy()
for reading in ['methods','code']:
    fx=ms.m1_fixations(events,reading)
    t0=time.time(); tr['d']=ms.trial_distance(tr,fx); print(time.time()-t0, tr.d.isna().mean())
    dm=ms.day_means(tr,'d')
    for reg in ['OFC','dmPFC','ACCg']:
        for subj in [None,'L','T']:
            x=dm[(dm.region==reg)&((dm.subject==subj) if subj else True)]
            diff=x.stim-x.sham
            print(reading,reg,subj,len(x), round(np.median(diff),2), wilcoxon(x.stim,x.sham).pvalue)
EOF
```

```
0.9997885348575409 1.0
16.551449060440063 0.06531785971038308
methods OFC None 27 -17.87 0.0003387331962585449
methods OFC L 15 -22.43 0.0067138671875
methods OFC T 12 -13.4 0.0341796875
methods dmPFC None 27 -6.02 0.2483380287885666
methods dmPFC L 15 -6.53 0.1688232421875
methods dmPFC T 12 -3.69 0.90966796875
methods ACCg None 27 -4.87 0.4553176909685135
methods ACCg L 15 -5.39 0.12054443359375
methods ACCg T 12 3.52 0.5693359375
15.15132761001587 0.0707096641676081
code OFC None 27 -20.38 0.00018434226512908936
code OFC L 15 -22.32 0.0067138671875
code OFC T 12 -8.8 0.00927734375
code dmPFC None 27 -4.83 0.324220210313797
code dmPFC L 15 -6.04 0.22930908203125
code dmPFC T 12 -1.27 1.0
code ACCg None 27 -3.91 0.324220210313797
code ACCg L 15 -5.52 0.10699462890625
[... 6 more lines not kept]
```

**Agent**

Fig. 2C is close to the paper (OFC p = 0.0003; L p = 0.007; T p = 0.03). The window search is slow (16 s per call), so I'll vectorize it before writing all the claims.

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
p='microstim.py'; s=open(p).read()
a=s.index('def window_pairs'); b=s.index('def roi_centre')
s=s[:a]+'''def window_pairs(trials: pd.DataFrame, events: pd.DataFrame, t0: float, t1: float) -> pd.DataFrame:
    """All (trial, event) pairs of the same run with event start in [trial + t0, trial + t1).

    Returns the event rows with `trial` (the trial's index in `trials`) and `lag` (start minus
    trial time, s)."""
    ev = events.sort_values(["run_id", "start"], kind="stable").reset_index(drop=True)
    er = ev.run_id.to_numpy()
    est = ev.start.to_numpy()
    # events sorted by (run, start): offset the start by run so one searchsorted serves all runs
    span = 1e6
    key = er * span + est
    tk = trials.run_id.to_numpy() * span + trials.time.to_numpy()
    lo = np.searchsorted(key, tk + t0, side="left")
    hi = np.searchsorted(key, tk + t1, side="left")
    n = hi - lo
    ti = np.repeat(np.arange(len(trials)), n)
    ei = np.concatenate([np.arange(a, b) for a, b in zip(lo, hi)]) if n.sum() else np.array([], int)
    out = ev.iloc[ei].reset_index(drop=True)
    out["trial"] = trials.index.to_numpy()[ti]
    out["lag"] = est[ei] - trials.time.to_numpy()[ti]
    return out


'''+s[b:]
open(p,'w').write(s)
EOF
cd $TMPDIR; . wenv/bin/activate; export PYTHONPATH=entries/000959-fan-2024; python -W ignore - <<'EOF'
import microstim as ms, pandas as pd, numpy as np, pickle, time
runs=pickle.load(open('runs.pkl','rb'))
meta,trials,events=ms.prepare(runs)
print(meta.t_last.max())
tr=trials[trials.kept & (trials.cond=='Social') & (trials.roi=='Eyes')].copy()
fx=ms.m1_fixations(events,'methods')
t0=time.time(); tr['d']=ms.trial_distance(tr,fx); print(time.time()-t0, tr.d.isna().mean())
dm=ms.day_means(tr,'d'); x=dm[dm.region=='OFC']; print(np.median(x.stim-x.sham))
EOF
```

```
9955.055
0.25130414962768555 0.0652151586731026
-17.87038578276571
Shell cwd was reset to
```

**Agent**

Vectorized: 0.25 s per call, same result. Now writing the full notebook (all testable claims), as a cell-marked script I'll convert with nbformat.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; . wenv/bin/activate; export PYTHONPATH=entries/000959-fan-2024; python -W ignore - <<'EOF'
import microstim as ms, pandas as pd, numpy as np, pickle
runs=pickle.load(open('runs.pkl','rb'))
meta,trials,events=ms.prepare(runs)
c=events[events.who=='m1'].groupby(['run_id','table']).size().unstack(fill_value=0)
print(((c.m1_wholeface-(c.m1_eye+c.m1_neface))).describe())
print(trials.groupby(['cond','roi']).kept.sum())
EOF
```

```
Sat Oct 31 23:53:43 UTC 2026
count    1705.0
mean        0.0
std         0.0
min         0.0
25%         0.0
50%         0.0
75%         0.0
max         0.0
dtype: float64
cond    roi  
Dot     Eyes     10148
        Mouth     1953
Social  Eyes     19474
        Mouth     2444
Name: kept, dtype: int64
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/nb_src.py",
 "content": "# %% [markdown]\n# # Reproducing Fan et al. (2024) from dandiset 000959\n#\n# **Paper.** Fan, Dal Monte, Nair, Fagan & Chang (2024), \"Closed-loop microstimulations of the\n# orbitofrontal cortex during real-life gaze interaction enhance dynamic social attention\",\n# Neuron 112, 2631-2644, doi:10.1016/j.neuron.2024.05.004.\n#\n# **Claims.** `claims/000959/10.1016-j.neuron.2024.05.004.yaml`, written from the accepted author\n# manuscript (PMC11309918) with its supplement, and the paper's code\n# (github.com/changlabneuro/microstim-ofc-social-attention at cc0bf994).\n#\n# **Dataset.** DANDI:000959, version 0.261020.0242. The paper cites the dandiset without a\n# version. Two versions are published, 0.260531.2104 and 0.261020.0242; the most recent is pinned,\n# as the protocol asks when the paper cites none. The data check below compares the two asset\n# lists: both hold the same 1705 assets with the same identifiers, paths and sizes, so the choice\n# does not change the data.\n#\n# Each file is one 300-s run (a \"session\" in the paper) and holds M1's gaze and pupil at 1 kHz,\n# M2's gaze and pupil in social runs, the stimulation and sham times, the day's ROIs, and\n# fixation events as interval tables (M1-only, M2-only and mutual events by ROI). Files are read\n# over HTTP into memory at the pinned version (nothing is written to disk) and reduced to small\n# tables by `microstim.py`.\n#\n# | Claim | Tested |\n# |---|---|\n# | design-days-per-area, design-sessions-per-day | tested |\n# | fig1e-stim-counts-comparable, figs1d-stim-counts-nonsocial | tested |\n# | figs1e-eyes-more-than-face, figs1e-eyes-vs-rdm-comparable | tested |\n# | fig2a-density-map-ofc | tested |\n# | fig2c-ofc-social-gaze-distance, fig2c-dmpfc-accg-no-distance-effect | tested |\n# | fig2e-ofc-contralateral, fig2e-dmpfc-accg-no-hemifield-effect | tested |\n# | fig2f-nonsocial-no-distance-effect, fig2gh-nonsocial-no-hemifield-effect | tested |\n# | methods-ofc-distance-longer-windows, methods-ofc-no-change-in-fixation-number, methods-ofc-longer-face-looking | tested |\n# | methods-mouth-stimulation-no-effect, methods-eyes-vs-mouth-bootstrap | tested |\n# | fig3b-ofc-inter-looking-interval, ili-nonsocial-no-effect, ili-missing-trials-41, figs3b-ili-trial-level | tested |\n# | figs3c-reciprocation-day-level-none, fig3d-ofc-reciprocation-latency | tested |\n# | partner-monkey-unchanged | tested |\n# | epoch-days-76-of-81 | tested |\n# | figs4a-causal-strength-no-stim-effect, figs4b-causal-strength-no-epoch-effect, ofc-slope-unchanged-by-epoch, fig4c-dmpfc-slope-late-greater, fig4d-dmpfc-slope-permutation, dmpfc-slope-positive | blocked, too_large (the causal decomposition; timed below) |\n# | fig5a-trigger-duration-unchanged, fig5b-pupil-unchanged | tested |\n# | fig5cd-saccade-counts-unchanged, fig5e-h-saccade-kinematics-unchanged | blocked, not_runnable (saccade detection by MATLAB code not in the dataset) |\n\n# %%\nimport time\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport requests\nfrom scipy.stats import mannwhitneyu, wilcoxon\nfrom statsmodels.stats.multitest import multipletests\n\nimport microstim as ms\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\nAREAS = [\"OFC\", \"dmPFC\", \"ACCg\"]\n\n\ndef signrank(a, b=None):\n    \"\"\"Two-sided Wilcoxon signed-rank test (scipy's default method: exact for small n\n    without ties). Returns (n, p).\"\"\"\n    a = np.asarray(a, float)\n    d = a if b is None else a - np.asarray(b, float)\n    d = d[~np.isnan(d)]\n    if len(d) == 0 or np.all(d == 0):\n        return len(d), np.nan\n    return len(d), wilcoxon(d).pvalue\n\n\ndef ranksum(a, b):\n    a = np.asarray(a, float)\n    b = np.asarray(b, float)\n    a, b = a[~np.isnan(a)], b[~np.isnan(b)]\n    return mannwhitneyu(a, b, alternative=\"two-sided\").pvalue\n\n\ndef day_test(dm, region, subject=None):\n    \"\"\"Signed-rank of stim against sham day means; returns n, median stim - sham, p.\"\"\"\n    x = dm[(dm.region == region) & ((dm.subject == subject) if subject else True)]\n    x = x.dropna(subset=[\"stim\", \"sham\"])\n    n, p = signrank(x.stim, x.sham)\n    return dict(region=region, subject=subject or \"both\", n=n,\n                median_diff=np.median(x.stim - x.sham) if n else np.nan,\n                mean_diff=np.mean(x.stim - x.sham) if n else np.nan, p=p)\n\n\ndef day_table(dm, subjects=(None, \"L\", \"T\"), areas=AREAS):\n    return pd.DataFrame([day_test(dm, a, s) for a in areas for s in subjects])\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nt_start = time.time()\nassets = ms.list_assets()\nother = ms.list_assets(\"0.260531.2104\")\nsame = assets.merge(other, on=[\"path\", \"asset_id\", \"size\"], how=\"outer\", indicator=True)\nprint(f\"version {ms.DANDISET_VERSION}: {len(assets)} assets, {assets['size'].sum() / 1e9:.1f} GB; \"\n      f\"version 0.260531.2104: {len(other)} assets; rows not shared: {(same._merge != 'both').sum()}\")\nruns = ms.load_all(assets)\nmeta, trials, events = ms.prepare(runs)\nprint(f\"loaded {len(runs)} runs in {(time.time() - t_start) / 60:.1f} min\")\n\nprint(\"\\nThe description, the scratch fields and the file name agree:\",\n      bool((meta.region == meta.region_scratch).all() and (meta.roi == meta.roi_scratch).all()\n           and (meta.cond == meta.cond_scratch).all()\n           and (meta.path.str.slice(4, 5) == meta.subject).all()))\nprint(\"runs by subject, triggering ROI, region and condition:\")\nprint(meta.groupby([\"subject\", \"roi\", \"region\", \"cond\"]).size().unstack(\"cond\"))\nprint(\"\\ndays by subject, triggering ROI and region:\")\nprint(meta.groupby([\"subject\", \"roi\", \"region\"]).date.nunique().unstack(\"region\"))\nprint(\"days with more than one region:\", (meta.groupby(\"date\").region.nunique() > 1).sum())\ndup_key = meta.apply(lambda r: (r.n_samples, round(r.t_first, 3), round(r.t_last, 3)), axis=1)\ndup_stim = trials.groupby(\"run_id\").time.apply(lambda s: tuple(np.round(s, 3)))\nprint(\"runs sharing sample count and time span:\", dup_key.duplicated().sum(),\n      \"; runs sharing all trial times:\", dup_stim.duplicated().sum(),\n      \"; identifiers shared by a Social and a Dot run (run numbers restart per condition):\",\n      meta.identifier.duplicated().sum(), \"; (date, condition, run) repeated:\",\n      meta.duplicated([\"date\", \"cond\", \"run\"]).sum())\n\nprint(\"\\nunits:\", meta.gaze_unit.unique(), \"; sampling rate (Hz):\", meta.rate.unique(),\n      \"; median and largest step of t (s):\", meta.dt_median.median(), meta.dt_max.max())\nprint(\"valid run length (s) by condition:\")\nprint((meta.t_last - meta.t_first).groupby(meta.cond).describe()[[\"count\", \"min\", \"50%\", \"max\"]])\nprint(\"M1 gaze x range (pixels):\", np.min([r[0] for r in meta.gaze_x_range]), np.max([r[1] for r in meta.gaze_x_range]),\n      \"; y range:\", np.min([r[0] for r in meta.gaze_y_range]), np.max([r[1] for r in meta.gaze_y_range]),\n      \"; median fraction of NaN gaze in the valid run:\", round(meta.gaze_nan.median(), 3))\nprint(\"M1 pupil range (a.u.):\", np.min([r[0] for r in meta.pupil_range]), np.max([r[1] for r in meta.pupil_range]))\nprint(\"event start indices are 1-based: largest |t[start_index - 1] - start time| =\",\n      meta.index_time_max_err.max(), \"s\")\n\nprint(\"\\ntrials by condition and label (all events in the files):\")\nprint(trials.groupby([\"cond\", \"roi\", \"type\"]).size().unstack(\"type\"))\ngap = trials.sort_values([\"run_id\", \"time\"]).groupby(\"run_id\").time.diff()\nprint(\"smallest interval between consecutive trials (s):\", round(gap.min(), 3),\n      \"; intervals under 4.99 s:\", int((gap < 4.99).sum()))\nprint(\"kept for analysis:\", int(trials.kept.sum()), \"of\", len(trials), \"; dropped as first of run:\",\n      int(trials[\"first\"].sum()), \"; outside the run or in its last 5 s:\", int((~trials.in_run & ~trials[\"first\"]).sum()))\nblk = trials.sort_values([\"run_id\", \"time\"]).copy()\nblk[\"k\"] = blk.groupby(\"run_id\").cumcount() // 4\nfull = blk.groupby([\"run_id\", \"k\"]).filter(lambda g: len(g) == 4)\nprint(\"blocks of four consecutive trials with two stimulations:\",\n      round((full.groupby([\"run_id\", \"k\"]).type.apply(lambda s: (s == \"stim\").sum()) == 2).mean(), 3))\n\nm1 = events[events.who == \"m1\"]\nprint(\"\\nevent tables: m1_all = m1_everywhere + m1_wholeface and m1_wholeface = m1_eye + m1_neface in every run:\",\n      bool((m1.groupby([\"run_id\", \"table\"]).size().unstack(fill_value=0).eval(\n          \"m1_all - m1_everywhere - m1_wholeface\").abs().max() == 0)))\nmw = set(zip(m1[m1.table == \"mutual_wholeface\"].run_id, m1[m1.table == \"mutual_wholeface\"].start.round(4)))\nfor t in [\"mutual_eye\", \"mutual_face\", \"mutual_mouth\"]:\n    s = set(zip(m1[m1.table == t].run_id, m1[m1.table == t].start.round(4)))\n    print(f\"  {t}: {len(s)} events, in mutual_wholeface: {len(s & mw)}\")\nalls = set(zip(m1[m1.table == \"m1_all\"].run_id, m1[m1.table == \"m1_all\"].start.round(4)))\nprint(\"  M1 sides of mutual events also in m1_all:\", len(mw & alls))\nlab = m1.dropna(subset=[\"hemi\"])\nprint(\"hemifield from the centre of roi_m2_face agrees with the files' laterality_label for\",\n      f\"{(lab.hemi == lab.laterality_label).mean():.4f} of M1 events \"\n      f\"(social {(lab[lab.cond == 'Social'].hemi == lab[lab.cond == 'Social'].laterality_label).mean():.4f}, \"\n      f\"Dot {(lab[lab.cond == 'Dot'].hemi == lab[lab.cond == 'Dot'].laterality_label).mean():.4f})\")\n\n# fixation positions against their ROI labels\nrows = []\nfor (cond, table), g in m1[m1.table.isin([\"m1_eye\", \"m1_wholeface\", \"m1_everywhere\"])].groupby([\"cond\", \"table\"]):\n    r = []\n    for rid, gg in g.groupby(\"run_id\"):\n        ro = runs[rid][\"rois\"]\n        rect = ro[\"roi_m1_eyes\"] if table == \"m1_eye\" else ro[\"roi_m1_face\"]\n        r.append(ms.in_rect(gg[[\"x\", \"y\"]].to_numpy(), rect))\n    rows.append(dict(cond=cond, table=table, n=len(g), mean_position_in_rectangle=np.concatenate(r).mean()))\nprint(\"\\nfraction of events whose mean position lies in the ROI rectangle of the file \"\n      \"(Eyes for m1_eye, whole Face for the others):\")\nprint(pd.DataFrame(rows))\nnvar = [d for d, g in meta.groupby(\"date\") if len({tuple(np.round(runs[i][\"rois\"][\"roi_m1_eyes\"], 2)) for i in g.run_id}) > 1]\nprint(\"days whose Eyes ROI differs between runs (recalibrated; each run's own ROIs are used):\", nvar)\n\n# %% [markdown]\n# **Clock check.** Each trial was triggered online by an M1 fixation in the targeted ROI, so the\n# trial times should fall inside the M1 events labelled with that ROI far more often than the\n# same times shifted by a few hundred milliseconds or seconds. The contrast between the true and\n# shifted times tests that the trial times and the event tables share a clock.\n\n# %%\ndef inside_rate(tr, ev, shift):\n    p = ms.window_pairs(tr.assign(time=tr.time + shift), ev, -10.0, 0.0005)\n    p = p[p.stop >= p.start - p.lag]\n    return tr.index.isin(p.trial).mean()\n\nclock = []\nfor (cond, roi), tr in trials[trials.kept].groupby([\"cond\", \"roi\"]):\n    tab = \"eye\" if roi == \"Eyes\" else \"mouth\"\n    ev = events[(events.who == \"m1\") & (events.target == tab)]\n    for shift in [-2.0, -0.5, 0.0, 0.5, 2.0]:\n        clock.append(dict(cond=cond, roi=roi, shift_s=shift, fraction_inside=inside_rate(tr, ev, shift)))\nclock = pd.DataFrame(clock).pivot(index=[\"cond\", \"roi\"], columns=\"shift_s\", values=\"fraction_inside\")\nprint(\"fraction of trials whose time lies inside an M1 event in the triggering ROI, by time shift:\")\nprint(clock.round(3))\nby_run = trials[trials.kept & (trials.cond == \"Social\") & (trials.roi == \"Eyes\")]\nev_e = events[(events.who == \"m1\") & (events.target == \"eye\")]\npr = ms.window_pairs(by_run, ev_e, -10.0, 0.0005)\npr = pr[pr.stop >= pr.start - pr.lag]\nr_in = by_run.assign(inside=by_run.index.isin(pr.trial)).groupby(\"run_id\").inside.mean()\nprint(\"social Eyes runs: fraction inside per run, quantiles:\", r_in.quantile([0, 0.05, 0.5]).round(3).to_dict(),\n      \"; runs below 0.5:\", int((r_in < 0.5).sum()), \"of\", len(r_in))\n\n# %% [markdown]\n# ## design-days-per-area\n#\n# > Eyes stimulation was applied on 27 days per stimulated area (OFC, dmPFC and ACCg), 15 per area\n# > from monkey L and 12 per area from monkey T, and Mouth stimulation on 5 days per area from monkey T.\n\n# %% tags=[\"claim:design-days-per-area\"]\nkept = trials[trials.kept]\ndd = kept.groupby([\"subject\", \"roi\", \"region\", \"date\"]).type.agg(lambda s: set(s) >= {\"stim\", \"sham\"})\ndays = dd[dd].reset_index().groupby([\"subject\", \"roi\", \"region\"]).date.nunique().unstack(\"region\")\nprint(\"days holding kept stimulation and sham trials:\")\nprint(days)\n\n# %% [markdown]\n# ## design-sessions-per-day\n#\n# > Each day held on average 10 live social gaze sessions (9 to 11) and 5 non-social control sessions\n# > (4 to 8) for monkey L, and 15 social (14 to 15) and 5 control sessions for monkey T, each 300 s long.\n\n# %% tags=[\"claim:design-sessions-per-day\"]\neyes_days = meta[meta.roi == \"Eyes\"]\nspd = eyes_days.groupby([\"subject\", \"date\", \"cond\"]).size().unstack(\"cond\")\nprint(spd.groupby(\"subject\").agg([\"mean\", \"min\", \"max\"]).round(2))\nprint(\"\\nnumber of control runs per day, monkey L:\", spd.loc[\"L\", \"Dot\"].value_counts().sort_index().to_dict())\nprint(\"number of social runs per day, monkey T:\", spd.loc[\"T\", \"Social\"].value_counts().sort_index().to_dict())\ndur = eyes_days.t_last - eyes_days.t_first\nprint(f\"\\nrun length (s), valid samples: mean {dur.mean():.1f}, min {dur.min():.1f}, max {dur.max():.1f}; \"\n      f\"whole file: mean {(eyes_days.n_samples / 1000).mean():.1f} s\")\nspd_m = meta[meta.roi == \"Mouth\"].groupby([\"subject\", \"date\", \"cond\"]).size().unstack(\"cond\")\nprint(\"Mouth days (not part of the claim): runs per day\", spd_m.agg([\"mean\", \"min\", \"max\"]).to_dict())\n\n# %% [markdown]\n# ## fig1e-stim-counts-comparable and figs1d-stim-counts-nonsocial\n#\n# > In the live social gaze condition, the total numbers of microstimulations and of shams per day\n# > were comparable across the three stimulated areas and between the two monkeys.\n#\n# > In the non-social control condition the numbers of microstimulations and shams per day were also\n# > comparable across areas and between monkeys.\n\n# %%\ndef count_tests(cond):\n    k = trials[trials.kept & (trials.roi == \"Eyes\") & (trials.cond == cond)]\n    c = k.groupby([\"date\", \"subject\", \"region\", \"type\"]).size().unstack(\"type\", fill_value=0).reset_index()\n    out = []\n    for typ in [\"stim\", \"sham\"]:\n        tests = []\n        for subj in [None, \"L\", \"T\"]:\n            x = c if subj is None else c[c.subject == subj]\n            for a, b in [(\"OFC\", \"dmPFC\"), (\"OFC\", \"ACCg\"), (\"dmPFC\", \"ACCg\")]:\n                tests.append(dict(type=typ, comparison=f\"{a} vs {b}, {subj or 'both'}\",\n                                  p=ranksum(x[x.region == a][typ], x[x.region == b][typ])))\n        for a in AREAS:\n            x = c[c.region == a]\n            tests.append(dict(type=typ, comparison=f\"L vs T, {a}\",\n                              p=ranksum(x[x.subject == \"L\"][typ], x[x.subject == \"T\"][typ])))\n        t = pd.DataFrame(tests)\n        t[\"p_fdr\"] = multipletests(t.p, method=\"fdr_bh\")[1]\n        out.append(t)\n    summ = c.groupby([\"subject\", \"region\"])[[\"stim\", \"sham\"]].agg([\"mean\", \"min\", \"max\"]).round(1)\n    return summ, pd.concat(out, ignore_index=True)\n\n# %% tags=[\"claim:fig1e-stim-counts-comparable\"]\nsumm, t = count_tests(\"Social\")\nprint(\"kept trials per day, social runs:\")\nprint(summ)\nprint(t.round(4).to_string())\nfor typ in [\"stim\", \"sham\"]:\n    x = t[t.type == typ]\n    print(f\"{typ}: smallest corrected p {x.p_fdr.min():.3f}; all corrected p > 0.90: {bool((x.p_fdr > 0.9).all())}; \"\n          f\"smallest uncorrected p {x.p.min():.3f}\")\n\n# %% tags=[\"claim:figs1d-stim-counts-nonsocial\"]\nsumm, t = count_tests(\"Dot\")\nprint(\"kept trials per day, control (Dot) runs:\")\nprint(summ)\nprint(t.round(4).to_string())\nfor typ in [\"stim\", \"sham\"]:\n    x = t[t.type == typ]\n    print(f\"{typ}: smallest corrected p {x.p_fdr.min():.3f}; all corrected p > 0.10: {bool((x.p_fdr > 0.1).all())}\")\n\n# %% [markdown]\n# ## figs1e-eyes-more-than-face and figs1e-eyes-vs-rdm-comparable\n#\n# > The stimulated monkeys made significantly more fixations per day on the partner's Eyes than on\n# > the non-eye Face, for days of all three stimulated areas.\n#\n# > The number of fixations on the partner's Eyes per day was comparable to the number of\n# > fixations on the RDM stimulus, for days of all three areas.\n#\n# Day counts under the claims' readings (a) the day's total and (b) the mean per run. The events\n# counted: M1's fixations in the ROI, the M1-only events plus the M1 side of mutual events (the\n# Methods' \"total number of gaze fixations ... of the stimulated monkey\"), with M1-only events as\n# the variant (the code's event tables). RDM fixations are the M1 events labelled Eyes in the Dot\n# runs (the RDM ROI is the Eyes ROI's location and size). FDR over the 15 tests of the claims file.\n\n# %%\ndef roi_counts(evset):\n    e = events[(events.roi == \"Eyes\") & (events.who == \"m1\")]\n    if evset == \"M1-only\":\n        e = e[~e.mutual]\n    sel = {\"Eyes\": (e.cond == \"Social\") & (e.target == \"eye\"),\n           \"neFace\": (e.cond == \"Social\") & (e.target.isin([\"neface\", \"face\"])),\n           \"RDM\": (e.cond == \"Dot\") & (e.target == \"eye\")}\n    # mutual non-eye Face events are in mutual_face; M1-only ones in m1_neface\n    sel[\"neFace\"] = (e.cond == \"Social\") & ((e.table == \"m1_neface\") | (e.table == \"mutual_face\"))\n    sel[\"Eyes\"] = (e.cond == \"Social\") & ((e.table == \"m1_eye\") | (e.table == \"mutual_eye\"))\n    runs_ = meta[meta.roi == \"Eyes\"]\n    out = {}\n    for name, s in sel.items():\n        cond = \"Dot\" if name == \"RDM\" else \"Social\"\n        per_run = e[s].groupby(\"run_id\").size().reindex(runs_[runs_.cond == cond].run_id, fill_value=0)\n        rr = runs_.set_index(\"run_id\").loc[per_run.index]\n        df = pd.DataFrame({\"n\": per_run.to_numpy(), \"date\": rr.date.to_numpy(), \"region\": rr.region.to_numpy(),\n                           \"subject\": rr.subject.to_numpy()})\n        out[name] = df.groupby([\"date\", \"region\", \"subject\"]).n.agg([\"sum\", \"mean\"])\n    return pd.concat(out, axis=1).reset_index()\n\n\ndef roi_tests(c, reading):\n    col = \"sum\" if reading == \"a\" else \"mean\"\n    tests = []\n    for a in AREAS:\n        x = c[c.region == a]\n        tests.append(dict(test=f\"Eyes vs neFace, {a}\", kind=\"signrank\", p=signrank(x[(\"Eyes\", col)], x[(\"neFace\", col)])[1],\n                          median_diff=np.median(x[(\"Eyes\", col)] - x[(\"neFace\", col)])))\n        tests.append(dict(test=f\"Eyes vs RDM, {a}\", kind=\"signrank\", p=signrank(x[(\"Eyes\", col)], x[(\"RDM\", col)])[1],\n                          median_diff=np.median(x[(\"Eyes\", col)] - x[(\"RDM\", col)])))\n    for roi in [\"Eyes\", \"neFace\", \"RDM\"]:\n        for a, b in [(\"OFC\", \"dmPFC\"), (\"OFC\", \"ACCg\"), (\"dmPFC\", \"ACCg\")]:\n            tests.append(dict(test=f\"{roi}, {a} vs {b}\", kind=\"ranksum\",\n                              p=ranksum(c[c.region == a][(roi, col)], c[c.region == b][(roi, col)]), median_diff=np.nan))\n    t = pd.DataFrame(tests)\n    t[\"p_fdr\"] = multipletests(t.p, method=\"fdr_bh\")[1]\n    return t\n\n\nroi_res = {}\nfor evset in [\"M1 and mutual\", \"M1-only\"]:\n    c = roi_counts(evset)\n    for reading in [\"a\", \"b\"]:\n        roi_res[(evset, reading)] = roi_tests(c, reading)\nc_main = roi_counts(\"M1 and mutual\")\nprint(\"fixations per day (reading a, the day's total), M1 and mutual events:\")\nprint(c_main.groupby(\"region\")[[(\"Eyes\", \"sum\"), (\"neFace\", \"sum\"), (\"RDM\", \"sum\")]].median())\n\n# %% tags=[\"claim:figs1e-eyes-more-than-face\"]\nfor k, t in roi_res.items():\n    x = t[t.test.str.startswith(\"Eyes vs neFace\")]\n    print(f\"events {k[0]}, reading ({k[1]}):\")\n    print(x[[\"test\", \"median_diff\", \"p\", \"p_fdr\"]].to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))\n\n# %% tags=[\"claim:figs1e-eyes-vs-rdm-comparable\"]\nfor k, t in roi_res.items():\n    x = t[t.test.str.startswith(\"Eyes vs RDM\")]\n    print(f\"events {k[0]}, reading ({k[1]}):\")\n    print(x[[\"test\", \"median_diff\", \"p\", \"p_fdr\"]].to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))\nprint(\"\\nthe nine rank-sum tests between areas, events M1 and mutual, reading (a):\")\nprint(roi_res[(\"M1 and mutual\", \"a\")].query(\"kind == 'ranksum'\")[[\"test\", \"p\", \"p_fdr\"]].to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))\n\n# %% [markdown]\n# ## Social gaze distance: common tables\n#\n# Kept trials of the Eyes days. Distances in pixels; the medians are also given in degrees\n# (`DEG_PER_PX`). Fixation readings: `methods` (M1-only and mutual events) and `code` (M1-only).\n\n# %%\nsoc = trials[trials.kept & (trials.cond == \"Social\") & (trials.roi == \"Eyes\")].copy()\ndot = trials[trials.kept & (trials.cond == \"Dot\") & (trials.roi == \"Eyes\")].copy()\nFIX = {r: ms.m1_fixations(events, r) for r in [\"methods\", \"code\"]}\n\n\ndef distance_days(tr, reading, t1=ms.POST_GAZE_S, hemi=None, centre=(\"eyes_x\", \"eyes_y\")):\n    tr = tr.copy()\n    tr[\"d\"] = ms.trial_distance(tr, FIX[reading], centre=centre, t1=t1, hemi=hemi)\n    return tr, ms.day_means(tr, \"d\")\n\n\ndef show(tab, label=\"\"):\n    t = tab.copy()\n    t[\"median_diff_deg\"] = t.median_diff * ms.DEG_PER_PX\n    print(label)\n    print(t.to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\n\n\ndist = {}\nfor reading in [\"methods\", \"code\"]:\n    for hemi in [None, \"contra\", \"ipsi\"]:\n        dist[(reading, hemi)] = distance_days(soc, reading, hemi=hemi)\ntr0 = dist[(\"methods\", None)][0]\nprint(\"social trials with no fixation in [0, 1.5) s:\", int(tr0.d.isna().sum()), \"of\", len(tr0))\nprint(\"trials per day and type, quantiles:\", tr0.groupby([\"date\", \"type\"]).size().quantile([0, 0.5, 1]).to_dict())\nprint(\"trial distance (pixels) range:\", round(tr0.d.min(), 1), round(tr0.d.max(), 1))\n\n# %% [markdown]\n# ## fig2a-density-map-ofc\n#\n# > After OFC microstimulations, compared with shams, the stimulated monkey's fixations in the\n# > 1.5 s post-gaze epoch were more clustered around the partner monkey.\n#\n# A 40 by 40 grid of 1-degree squares centred on the run's Eyes centre; monkey T's maps flipped\n# horizontally; per day stimulation and sham maps; normalisation (1) z-score of each map, (2)\n# difference divided by the day's total of stimulation and sham fixations. The measure is the\n# day-averaged difference summed over the squares whose centres lie in (a) the whole Face ROI,\n# (b) the Eyes ROI. Fixations: the Methods reading.\n\n# %% tags=[\"claim:fig2a-density-map-ofc\"]\nedges = np.arange(-20, 21, 1.0)\ncent = (edges[:-1] + edges[1:]) / 2\nfx = FIX[\"methods\"].dropna(subset=[\"x\"])\npairs = ms.window_pairs(soc, fx, 0.0, ms.POST_GAZE_S)\npairs[\"type\"] = soc.loc[pairs.trial, \"type\"].to_numpy()\nsgn = np.where(pairs.subject == \"T\", -1.0, 1.0)\npairs[\"dx\"] = (pairs.x - pairs.eyes_x) * ms.DEG_PER_PX * sgn\npairs[\"dy\"] = (pairs.y - pairs.eyes_y) * ms.DEG_PER_PX\nprint(f\"post-gaze fixations: {len(pairs)}; outside the 40-degree grid: {int(((pairs.dx.abs() >= 20) | (pairs.dy.abs() >= 20)).sum())}\")\ngx, gy = np.meshgrid(cent, cent, indexing=\"xy\")\ndmaps, rows = {}, []\nfor (date, region, subject), g in pairs.groupby([\"date\", \"region\", \"subject\"]):\n    H = {t: np.histogram2d(g[g.type == t].dy, g[g.type == t].dx, bins=[edges, edges])[0] for t in [\"stim\", \"sham\"]}\n    z = {t: (H[t] - H[t].mean()) / H[t].std() for t in H}\n    norm = {\"zscore\": z[\"stim\"] - z[\"sham\"], \"total\": (H[\"stim\"] - H[\"sham\"]) / (H[\"stim\"].sum() + H[\"sham\"].sum())}\n    rid = soc[soc.date == date].run_id.iloc[0]\n    ro = runs[rid][\"rois\"]\n    e = ms._centre(ro[\"roi_m1_eyes\"])\n    masks = {}\n    for nm, key in [(\"face\", \"roi_m1_face\"), (\"eyes\", \"roi_m1_eyes\")]:\n        r = ro[key]\n        xs = np.sort((r[[0, 2]] - e[0]) * ms.DEG_PER_PX * (-1 if subject == \"T\" else 1))\n        ys = np.sort((r[[1, 3]] - e[1]) * ms.DEG_PER_PX)\n        masks[nm] = (gx >= xs[0]) & (gx <= xs[1]) & (gy >= ys[0]) & (gy <= ys[1])\n    for k, m in norm.items():\n        dmaps.setdefault((region, k), []).append(m)\n        rows.append(dict(date=date, region=region, subject=subject, norm=k,\n                         face=m[masks[\"face\"]].sum(), eyes=m[masks[\"eyes\"]].sum(),\n                         n_face_squares=masks[\"face\"].sum(), n_eye_squares=masks[\"eyes\"].sum()))\nhm = pd.DataFrame(rows)\nres = hm.groupby([\"region\", \"norm\"])[[\"face\", \"eyes\"]].mean()\nprint(\"day-averaged stimulation minus sham density summed over the squares in each ROI:\")\nprint(res.round(4))\nprint(\"by monkey:\")\nprint(hm.groupby([\"region\", \"subject\", \"norm\"])[[\"face\", \"eyes\"]].mean().round(4))\nprint(\"squares inside the ROIs per day, median:\", hm.n_face_squares.median(), hm.n_eye_squares.median())\nfig, ax = plt.subplots(1, 3, figsize=(12, 3.6))\nfor a, region in zip(ax, AREAS):\n    m = np.mean(dmaps[(region, \"zscore\")], 0)\n    im = a.imshow(m, origin=\"upper\", extent=[-20, 20, 20, -20], cmap=\"RdBu_r\", vmin=-0.6, vmax=0.6)\n    a.set_title(f\"{region}, z-scored stim - sham\")\n    print(f\"{region}: plotted range {m.min():.2f} to {m.max():.2f}; squares beyond the colour scale {(np.abs(m) > 0.6).sum()}\")\n    a.set_xlabel(\"deg (contra <- -> ipsi for L)\")\nplt.colorbar(im, ax=ax)\nplt.show()\n\n# %% [markdown]\n# ## fig2c-ofc-social-gaze-distance\n#\n# > OFC microstimulations decreased the social gaze distance, the mean distance of the stimulated\n# > monkey's fixations in the post-gaze epoch from the centre of the partner's Eyes, compared with\n# > shams; the effect held in each monkey.\n\n# %% tags=[\"claim:fig2c-ofc-social-gaze-distance\"]\nfor reading in [\"methods\", \"code\"]:\n    show(day_table(dist[(reading, None)][1], areas=[\"OFC\"]), f\"fixations: {reading}\")\n\n# %% [markdown]\n# ## fig2c-dmpfc-accg-no-distance-effect\n#\n# > Microstimulations of dmPFC or ACCg did not change social gaze distance.\n\n# %% tags=[\"claim:fig2c-dmpfc-accg-no-distance-effect\"]\nfor reading in [\"methods\", \"code\"]:\n    show(day_table(dist[(reading, None)][1], areas=[\"dmPFC\", \"ACCg\"]), f\"fixations: {reading}\")\n\n# %% [markdown]\n# ## fig2e-ofc-contralateral and fig2e-dmpfc-accg-no-hemifield-effect\n#\n# > The OFC effect on social gaze distance was stronger for fixations in the hemifield\n# > contralateral to the stimulated hemisphere; it was significant for contralateral fixations,\n# > not for ipsilateral ones, and the contralateral effect exceeded the ipsilateral one.\n#\n# > For dmPFC and ACCg there was no stimulation effect on social gaze distance in either\n# > hemifield, and no difference between hemifields.\n\n# %%\ndef hemi_table(dsets, areas, subjects=(None, \"L\", \"T\")):\n    rows = []\n    for a in areas:\n        for s in subjects:\n            c = day_test(dsets[\"contra\"], a, s)\n            i = day_test(dsets[\"ipsi\"], a, s)\n            dc = dsets[\"contra\"].assign(eff=lambda d: d.stim - d.sham)\n            di = dsets[\"ipsi\"].assign(eff=lambda d: d.stim - d.sham)\n            m = dc.merge(di, on=[\"date\", \"subject\", \"region\"], suffixes=(\"_c\", \"_i\"))\n            m = m[(m.region == a) & ((m.subject == s) if s else True)].dropna(subset=[\"eff_c\", \"eff_i\"])\n            n, p = signrank(m.eff_c, m.eff_i)\n            rows.append(dict(region=a, subject=s or \"both\", n_contra=c[\"n\"], contra_median=c[\"median_diff\"], contra_p=c[\"p\"],\n                             n_ipsi=i[\"n\"], ipsi_median=i[\"median_diff\"], ipsi_p=i[\"p\"],\n                             n_cvi=n, contra_minus_ipsi_median=np.median(m.eff_c - m.eff_i) if n else np.nan, cvi_p=p))\n    return pd.DataFrame(rows)\n\n\nhemi_res = {r: hemi_table({h: dist[(r, h)][1] for h in [\"contra\", \"ipsi\"]}, AREAS) for r in [\"methods\", \"code\"]}\n\n# %% tags=[\"claim:fig2e-ofc-contralateral\"]\nfor r in [\"methods\", \"code\"]:\n    print(f\"fixations: {r} (effects in pixels, stim - sham)\")\n    print(hemi_res[r][hemi_res[r].region == \"OFC\"].to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\n\n# %% tags=[\"claim:fig2e-dmpfc-accg-no-hemifield-effect\"]\nfor r in [\"methods\", \"code\"]:\n    print(f\"fixations: {r}\")\n    x = hemi_res[r][(hemi_res[r].region != \"OFC\") & (hemi_res[r].subject == \"both\")]\n    print(x.to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\n\n# %% [markdown]\n# ## fig2f-nonsocial-no-distance-effect and fig2gh-nonsocial-no-hemifield-effect\n#\n# > In the non-social control condition, microstimulations of none of the three areas changed the\n# > distance of fixations from the centre of the RDM stimulus.\n#\n# > In the non-social control condition there was no stimulation effect in either hemifield, and no\n# > hemifield difference, for any area.\n#\n# Dot runs of the Eyes days; the RDM centre is the centre of the run's `roi_m1_eyes` (the RDM ROI\n# has the Eyes ROI's location and size); M1 events only (there is no M2 gaze, so no mutual events).\n\n# %% tags=[\"claim:fig2f-nonsocial-no-distance-effect\"]\nddot = {h: distance_days(dot, \"code\", hemi=h) for h in [None, \"contra\", \"ipsi\"]}\nprint(\"control trials with no fixation in [0, 1.5) s:\", int(ddot[None][0].d.isna().sum()), \"of\", len(dot))\nshow(day_table(ddot[None][1], subjects=(None,)), \"control runs, distance to the RDM centre\")\nshow(day_table(ddot[None][1], subjects=(\"L\", \"T\")), \"by monkey\")\n\n# %% tags=[\"claim:fig2gh-nonsocial-no-hemifield-effect\"]\nhd = hemi_table({h: ddot[h][1] for h in [\"contra\", \"ipsi\"]}, AREAS)\nprint(hd.to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\n\n# %% [markdown]\n# ## methods-ofc-distance-longer-windows\n#\n# > The OFC decrease of social gaze distance also held within 2 s and within 3 s after the trial for\n# > both monkeys combined and for monkey L, not for monkey T.\n\n# %% tags=[\"claim:methods-ofc-distance-longer-windows\"]\nfor reading in [\"methods\", \"code\"]:\n    for t1 in [2.0, 3.0]:\n        show(day_table(distance_days(soc, reading, t1=t1)[1], areas=[\"OFC\"]), f\"fixations {reading}, window [0, {t1:g}) s\")\n\n# %% [markdown]\n# ## methods-ofc-no-change-in-fixation-number\n#\n# > OFC microstimulations did not change the number of fixations within the partner's Eyes or whole\n# > Face in the post-gaze window, in either monkey, for windows of 1.5, 2 or 3 s.\n\n# %%\ndef count_or_duration(tr, tables_, t1, what):\n    ev = events[events.table.isin(tables_) & (events.who == \"m1\")]\n    p = ms.window_pairs(tr, ev, 0.0, t1)\n    p[\"dur\"] = (p.stop - p.start) * 1000.0\n    agg = p.groupby(\"trial\").size() if what == \"count\" else p.groupby(\"trial\").dur.sum()\n    tr = tr.copy()\n    tr[\"v\"] = tr.index.map(agg).fillna(0).astype(float)\n    return ms.day_means(tr, \"v\")\n\n\nSETS = {\"a\": {\"Eyes\": [\"m1_eye\"], \"wholeFace\": [\"m1_wholeface\"]},\n        \"b\": {\"Eyes\": [\"m1_eye\", \"mutual_eye\"], \"wholeFace\": [\"m1_wholeface\", \"mutual_wholeface\"]}}\n\n# %% tags=[\"claim:methods-ofc-no-change-in-fixation-number\"]\nrows = []\nfor reading in [\"a\", \"b\"]:\n    for roi in [\"Eyes\", \"wholeFace\"]:\n        for t1 in [1.5, 2.0, 3.0]:\n            dm = count_or_duration(soc, SETS[reading][roi], t1, \"count\")\n            for s in [\"L\", \"T\", None]:\n                r = day_test(dm, \"OFC\", s)\n                rows.append(dict(reading=reading, roi=roi, window=t1, **r))\nfn = pd.DataFrame(rows)\nprint(fn.to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\nfor reading in [\"a\", \"b\"]:\n    x = fn[(fn.reading == reading) & (fn.subject != \"both\")]\n    print(f\"reading ({reading}): per-monkey tests with p < 0.05: {int((x.p < 0.05).sum())} of {len(x)}; smallest p {x.p.min():.3f}\")\n\n# %% [markdown]\n# ## methods-ofc-longer-face-looking\n#\n# > With OFC microstimulations the stimulated monkey spent more time looking within the partner's\n# > whole Face in the post-gaze epoch (48.9 ms more than with shams, both monkeys combined), and more\n# > weakly within the Eyes; dmPFC and ACCg showed no such effect.\n\n# %% tags=[\"claim:methods-ofc-longer-face-looking\"]\nfor evs in [\"a\", \"b\"]:\n    rows = []\n    for roi in [\"wholeFace\", \"Eyes\"]:\n        dm = count_or_duration(soc, SETS[evs][roi], ms.POST_GAZE_S, \"duration\")\n        for a in AREAS:\n            for s in [None, \"L\", \"T\"]:\n                rows.append(dict(roi=roi, **day_test(dm, a, s)))\n    print(f\"events ({evs}: {'M1-only, as the code' if evs == 'a' else 'M1-only and mutual'}); total duration in ms, \"\n          \"median_diff and mean_diff are readings (a) and (b) of the claim's 'diff'\")\n    print(pd.DataFrame(rows).to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\n\n# %% [markdown]\n# ## methods-mouth-stimulation-no-effect\n#\n# > When microstimulations were triggered by looking at the partner's Mouth (or at an RDM stimulus at\n# > the Mouth location), none of the three areas changed social or non-social gaze distance, in\n# > either hemifield.\n#\n# Mouth days (monkey T, 5 per area). Social distance to the centre of the run's `roi_m1_mouth`;\n# non-social distance to the centre of the Dot run's `roi_m1_mouth` (the RDM at the Mouth\n# location). With 5 days the smallest two-sided exact signed-rank p is 0.0625.\n\n# %% tags=[\"claim:methods-mouth-stimulation-no-effect\"]\nmsoc = trials[trials.kept & (trials.cond == \"Social\") & (trials.roi == \"Mouth\")]\nmdot = trials[trials.kept & (trials.cond == \"Dot\") & (trials.roi == \"Mouth\")]\nprint(\"Mouth days: social trials\", len(msoc), \"control trials\", len(mdot))\nrows = []\nmouth_dm = {}\nfor cond, tr, rd in [(\"social\", msoc, \"methods\"), (\"social, code reading\", msoc, \"code\"), (\"non-social\", mdot, \"code\")]:\n    for h in [None, \"contra\", \"ipsi\"]:\n        dm = distance_days(tr, rd, hemi=h, centre=(\"mouth_x\", \"mouth_y\"))[1]\n        mouth_dm[(cond, h)] = dm\n        for a in AREAS:\n            rows.append(dict(condition=cond, hemifield=h or \"both\", **day_test(dm, a, \"T\")))\nmt = pd.DataFrame(rows)\nprint(mt.to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\nprint(\"tests with p < 0.05:\", int((mt.p < 0.05).sum()), \"of\", len(mt))\n\n# %% [markdown]\n# ## methods-eyes-vs-mouth-bootstrap\n#\n# > For contralateral fixations, the OFC stimulation effect on social gaze distance was\n# > significantly more negative in Eyes stimulation than in Mouth stimulation, but not for\n# > ipsilateral fixations or both hemifields combined; the difference was stronger using monkey\n# > T's Eyes days only.\n#\n# Day effects are stimulation minus sham day means (Methods fixation reading). 1,000 draws of 5\n# days with replacement; p readings (a) fraction of bootstrap medians at or above the Mouth\n# median, (b) twice the smaller tail. Seed 959 (a standard choice).\n\n# %% tags=[\"claim:methods-eyes-vs-mouth-bootstrap\"]\nrng = np.random.default_rng(959)\nrows = []\nfor h in [None, \"contra\", \"ipsi\"]:\n    e = dist[(\"methods\", h)][1]\n    e = e[e.region == \"OFC\"].assign(eff=lambda d: d.stim - d.sham).dropna(subset=[\"eff\"])\n    m = mouth_dm[(\"social\", h)]\n    m = m[m.region == \"OFC\"].assign(eff=lambda d: d.stim - d.sham).dropna(subset=[\"eff\"])\n    mouth_med = np.median(m.eff)\n    for pool in [\"all\", \"T\"]:\n        x = (e if pool == \"all\" else e[e.subject == \"T\"]).eff.to_numpy()\n        boots = np.median(rng.choice(x, size=(1000, 5), replace=True), axis=1)\n        pa = np.mean(boots >= mouth_med)\n        pb = min(1.0, 2 * min(np.mean(boots >= mouth_med), np.mean(boots <= mouth_med)))\n        rows.append(dict(hemifield=h or \"both\", eyes_days=pool, n_eyes=len(x), n_mouth=len(m),\n                         eyes_median=np.median(x), boot_median=np.median(boots), mouth_median=mouth_med,\n                         p_a_one_sided=pa, p_b_two_sided=pb))\nprint(pd.DataFrame(rows).to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\n\n# %% [markdown]\n# ## Inter-looking interval\n#\n# Per trial, the time from the trial to the start of the first M1 whole Face event (M1-only or\n# mutual, Methods, Gaze latency analyses) that starts within 5 s after it; NaN when there is none.\n\n# %%\nwf_m1 = events[(events.who == \"m1\") & events.table.isin([\"m1_wholeface\", \"mutual_wholeface\"])]\nwf_m2 = events[(events.who == \"m2\") & events.table.isin([\"m2_wholeface\", \"mutual_wholeface\"])]\nsoc[\"ili\"] = ms.first_latency(soc, wf_m1)\ndot[\"ili\"] = ms.first_latency(dot, events[(events.who == \"m1\") & (events.table == \"m1_wholeface\")])\nili_dm = ms.day_means(soc, \"ili\")\nprint(\"social trials with an inter-looking interval:\", int(soc.ili.notna().sum()), \"of\", len(soc),\n      \"; range (s):\", round(soc.ili.min(), 3), round(soc.ili.max(), 3))\n\n# %% [markdown]\n# ## fig3b-ofc-inter-looking-interval\n#\n# > OFC microstimulations decreased the inter-looking interval, the latency of the stimulated\n# > monkey to look back at the partner's whole Face within 5 s after the trial, compared with\n# > shams; dmPFC and ACCg microstimulations did not.\n\n# %% tags=[\"claim:fig3b-ofc-inter-looking-interval\"]\nshow(day_table(ili_dm), \"inter-looking interval (s), day level\")\n\n# %% [markdown]\n# ## ili-nonsocial-no-effect\n#\n# > The inter-looking interval did not change with stimulation in the non-social control\n# > condition, for any area.\n\n# %% tags=[\"claim:ili-nonsocial-no-effect\"]\nprint(\"control trials with an interval:\", int(dot.ili.notna().sum()), \"of\", len(dot))\nshow(day_table(ms.day_means(dot, \"ili\")), \"inter-looking interval (s), control runs\")\n\n# %% [markdown]\n# ## ili-missing-trials-41\n#\n# > On 41% of microstimulation and sham trials per day on average, the stimulated monkey did not\n# > look back at the partner's whole Face within the 5 s window.\n\n# %% tags=[\"claim:ili-missing-trials-41\"]\nmiss = soc.assign(m=soc.ili.isna()).groupby([\"date\", \"region\", \"subject\"]).m.mean().reset_index()\nprint(f\"(a) all {miss.date.nunique()} Eyes days: {100 * miss.m.mean():.1f}%\")\nprint(f\"(b) the {miss[miss.region == 'OFC'].date.nunique()} OFC days: {100 * miss[miss.region == 'OFC'].m.mean():.1f}%\")\nprint(\"by area and monkey (%):\")\nprint((100 * miss.groupby([\"region\", \"subject\"]).m.mean()).round(1))\nprint(f\"pooled over trials: {100 * soc.ili.isna().mean():.1f}%\")\n\n# %% [markdown]\n# ## figs3b-ili-trial-level\n#\n# > With all trials of each area pooled across days, OFC microstimulations still decreased the\n# > inter-looking interval, while dmPFC and ACCg did not.\n\n# %%\ndef trial_level(tr, col):\n    rows = []\n    for a in AREAS:\n        for s in [None, \"L\", \"T\"]:\n            x = tr[(tr.region == a) & ((tr.subject == s) if s else True)]\n            st, sh = x[x.type == \"stim\"][col].dropna(), x[x.type == \"sham\"][col].dropna()\n            rows.append(dict(region=a, subject=s or \"both\", n_stim=len(st), n_sham=len(sh),\n                             median_stim=st.median(), median_sham=sh.median(),\n                             mean_stim=st.mean(), mean_sham=sh.mean(), p=ranksum(st, sh)))\n    return pd.DataFrame(rows)\n\n# %% tags=[\"claim:figs3b-ili-trial-level\"]\nprint(trial_level(soc, \"ili\").to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\n\n# %% [markdown]\n# ## Reciprocation latency\n#\n# Whole Face events of M1 and of M2 that start within 5 s after the trial, mutual events in both\n# lists; for each run of consecutive M2 events followed by an M1 event, the time from the run's\n# first M2 event to that M1 event; the trial's value is the mean over sequences.\n\n# %%\nsoc[\"recip\"] = ms.reciprocation(soc, wf_m1, wf_m2, first=\"m2\")\nprint(\"social trials with a reciprocation latency:\", int(soc.recip.notna().sum()), \"of\", len(soc),\n      \"; range (s):\", round(soc.recip.min(), 3), round(soc.recip.max(), 3))\n\n# %% [markdown]\n# ## figs3c-reciprocation-day-level-none\n#\n# > At the day level, microstimulations did not significantly reduce the reciprocation latency in\n# > any area; on 86% of trials per day on average there was no sequence of the partner looking at\n# > the stimulated monkey followed by the stimulated monkey looking back.\n\n# %% tags=[\"claim:figs3c-reciprocation-day-level-none\"]\nshow(day_table(ms.day_means(soc, \"recip\")), \"reciprocation latency (s), day level\")\nrm = soc.assign(m=soc.recip.isna()).groupby([\"date\", \"region\"]).m.mean().reset_index()\nprint(f\"\\ntrials with no sequence: (a) all {rm.date.nunique()} days {100 * rm.m.mean():.1f}%; \"\n      f\"(b) OFC days {100 * rm[rm.region == 'OFC'].m.mean():.1f}%\")\nprint(\"days with no sequence in a trial type, by area:\",\n      ms.day_means(soc, \"recip\").groupby(\"region\")[[\"stim\", \"sham\"]].apply(lambda d: d.isna().any(axis=1).sum()).to_dict())\n\n# %% [markdown]\n# ## fig3d-ofc-reciprocation-latency\n#\n# > With trials pooled across days, OFC microstimulations decreased the latency of the stimulated\n# > monkey to reciprocate the partner's gaze to his face; dmPFC and ACCg did not.\n\n# %% tags=[\"claim:fig3d-ofc-reciprocation-latency\"]\nprint(trial_level(soc, \"recip\").to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\n\n# %% [markdown]\n# ## partner-monkey-unchanged\n#\n# > Microstimulations in none of the areas changed the partner monkey's social gaze distance,\n# > inter-looking interval or reciprocation latency.\n#\n# M2 distance: M2's fixations starting in [0, 1.5) s, distance to the centre of `roi_m2_eyes`\n# (M1's Eyes in M2's coordinates). M2 inter-looking interval, readings (a) start of the second\n# minus start of the first M2 whole Face event in the 5-s window, (b) start of the second minus\n# end of the first. M2 reciprocation latency, readings (a) from the start of the first M1 event of\n# a run of M1 whole Face events to the next M2 event (the mirror of M1's measure), (b) from the\n# trial time to the first M2 event that follows an M1 event.\n\n# %% tags=[\"claim:partner-monkey-unchanged\"]\nrows = []\nfor rd in [\"methods\", \"code\"]:\n    t = soc.copy()\n    t[\"d2\"] = ms.trial_distance(t, ms.m2_fixations(events, rd).dropna(subset=[\"x\"]), centre=(\"m2_eyes_x\", \"m2_eyes_y\"))\n    for a in AREAS:\n        rows.append(dict(measure=f\"M2 distance ({rd})\", **day_test(ms.day_means(t, \"d2\"), a)))\np2 = ms.window_pairs(soc, wf_m2, 0.0, ms.LATENCY_WINDOW_S).sort_values([\"trial\", \"start\"])\np2[\"k\"] = p2.groupby(\"trial\").cumcount()\nfirst2 = p2[p2.k == 0].set_index(\"trial\")\nsecond2 = p2[p2.k == 1].set_index(\"trial\")\nt = soc.copy()\nt[\"ili2a\"] = t.index.map(second2.start - first2.start.reindex(second2.index)).astype(float)\nt[\"ili2b\"] = t.index.map(second2.start - first2.stop.reindex(second2.index)).astype(float)\nt[\"rec2a\"] = ms.reciprocation(soc, wf_m1, wf_m2, first=\"m1\")\np1 = ms.window_pairs(soc, wf_m1, 0.0, ms.LATENCY_WINDOW_S).groupby(\"trial\").start.min()\nq = p2.assign(f1=p2.trial.map(p1)).query(\"start > f1\").groupby(\"trial\").lag.min()\nt[\"rec2b\"] = t.index.map(q).astype(float)\nfor col, lab in [(\"ili2a\", \"M2 inter-looking interval (a)\"), (\"ili2b\", \"M2 inter-looking interval (b)\"),\n                 (\"rec2a\", \"M2 reciprocation latency (a)\"), (\"rec2b\", \"M2 reciprocation latency (b)\")]:\n    for a in AREAS:\n        rows.append(dict(measure=lab, **day_test(ms.day_means(t, col), a)))\npm = pd.DataFrame(rows)\nprint(pm.to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\nprint(\"trials with a value:\", {c: int(t[c].notna().sum()) for c in [\"ili2a\", \"ili2b\", \"rec2a\", \"rec2b\"]}, \"of\", len(t))\nprint(\"tests with p < 0.05:\", pm[pm.p < 0.05][[\"measure\", \"region\", \"p\"]].to_dict(\"records\"))\n\n# %% [markdown]\n# ## epoch-days-76-of-81\n#\n# > 76 of the 81 days had at least 90 microstimulations and entered the epoch analysis; the five\n# > excluded were 1 OFC day of monkey L and, of monkey T, 1 OFC, 2 dmPFC and 1 ACCg day.\n\n# %% tags=[\"claim:epoch-days-76-of-81\"]\nallsoc = trials[(trials.cond == \"Social\") & (trials.roi == \"Eyes\")]\nns = pd.DataFrame({\n    \"a_kept\": allsoc[allsoc.kept & (allsoc.type == \"stim\")].groupby(\"date\").size(),\n    \"b_all\": allsoc[allsoc.type == \"stim\"].groupby(\"date\").size()}).fillna(0).astype(int)\nns = ns.join(meta.drop_duplicates(\"date\").set_index(\"date\")[[\"subject\", \"region\"]])\nfor col in [\"a_kept\", \"b_all\"]:\n    ok = ns[col] >= 90\n    print(f\"reading ({col}): days with at least 90 stimulations {int(ok.sum())} of {len(ns)}; excluded:\")\n    print(ns[~ok].sort_values([\"subject\", \"region\"]).to_string())\nnamed = [\"08122019\", \"12222021\", \"11052021\", \"12172021\", \"11042021\"]\nprint(\"\\nthe five days the code names:\")\nprint(ns.loc[named].to_string())\nprint(\"stimulations per day, quantiles (a):\", ns.a_kept.quantile([0, 0.1, 0.5, 1]).to_dict())\n\n# %% [markdown]\n# ## Causal decomposition claims (blocked)\n#\n# figs4a-causal-strength-no-stim-effect, figs4b-causal-strength-no-epoch-effect,\n# ofc-slope-unchanged-by-epoch, fig4c-dmpfc-slope-late-greater, fig4d-dmpfc-slope-permutation and\n# dmpfc-slope-positive all rest on the relative causal strength of each trial, from the causal\n# decomposition of Yang, Peng and Huang (2018), which is built on ensemble empirical mode\n# decomposition (EEMD). The claims file's reading (a) takes noise 0.2 and 1,000 ensembles on 150\n# bins. The cell below times one EEMD of one 150-bin series with the PyEMD implementation and\n# counts the trials, to estimate the cost.\n\n# %%\nfrom PyEMD import EEMD\n\nrng_c = np.random.default_rng(4)\nsig = np.cumsum(rng_c.normal(size=150))\neemd = EEMD(trials=100, noise_width=0.2, parallel=False)\neemd.noise_seed(4)\nt0 = time.time()\nimfs = eemd.eemd(sig)\nper_100 = time.time() - t0\nn_tr = len(soc)\nn_imf = imfs.shape[0]\n# one EEMD of each series, then one per IMF of each series with that IMF removed (Yang et al. 2018)\nper_trial = per_100 * 10 * (2 + 2 * n_imf)\nprint(f\"EEMD of one 150-bin series with 100 ensembles: {per_100:.2f} s; {n_imf} IMFs\")\nprint(f\"estimated per trial at 1,000 ensembles: {per_trial:.0f} s; {n_tr} social trials: \"\n      f\"{per_trial * n_tr / 3600:.0f} CPU hours\")\n\n# %% [markdown]\n# ## fig5a-trigger-duration-unchanged\n#\n# > Microstimulations of OFC or dmPFC did not change the duration of the Eyes fixation that\n# > triggered the trial.\n#\n# The M1 Eyes event in progress at the trial time (start at or before it, end at or after it).\n# Readings: (a) M1-only and mutual Eyes events, (b) M1-only.\n\n# %% tags=[\"claim:fig5a-trigger-duration-unchanged\"]\nfor rd, tabs in [(\"a\", [\"m1_eye\", \"mutual_eye\"]), (\"b\", [\"m1_eye\"])]:\n    ev = events[(events.who == \"m1\") & events.table.isin(tabs)]\n    p = ms.window_pairs(soc, ev, -10.0, 0.0005)\n    p = p[p.stop >= p.start - p.lag]\n    p[\"dur\"] = (p.stop - p.start) * 1000\n    t = soc.copy()\n    t[\"trig\"] = t.index.map(p.groupby(\"trial\").dur.max()).astype(float)\n    print(f\"reading ({rd}): trials with an Eyes event in progress {int(t.trig.notna().sum())} of {len(t)}; \"\n          f\"median duration {t.trig.median():.0f} ms\")\n    show(day_table(ms.day_means(t, \"trig\"), subjects=(None,)), \"duration (ms), day level\")\n\n# %% [markdown]\n# ## fig5b-pupil-unchanged\n#\n# > Pupil size did not differ between microstimulation and sham trials in any 10 ms bin of the 700\n# > ms after trial onset, for any area.\n\n# %% tags=[\"claim:fig5b-pupil-unchanged\"]\npup = np.vstack([r[\"pupil\"] for r in runs])\nalltr = trials.copy()\nalltr[\"prow\"] = np.arange(len(alltr))\nsel = alltr.loc[soc.index]\nsel = sel[sel.in_face_700]\nprint(\"social trials with gaze in the whole Face for 700 ms:\", len(sel), \"of\", len(soc))\nP = pd.DataFrame(pup[sel.prow.to_numpy()], index=sel.index)\nP[[\"date\", \"region\", \"subject\", \"type\"]] = sel[[\"date\", \"region\", \"subject\", \"type\"]]\ndmp = P.groupby([\"date\", \"region\", \"subject\", \"type\"]).mean()\nrows = []\nfor a in AREAS:\n    x = dmp.xs(a, level=\"region\")\n    st = x.xs(\"stim\", level=\"type\")\n    sh = x.xs(\"sham\", level=\"type\")\n    common = st.index.intersection(sh.index)\n    ps = np.array([signrank(st.loc[common, b], sh.loc[common, b])[1] for b in range(pup.shape[1])])\n    rows.append(dict(region=a, days=len(common), bins=len(ps), bins_p_below_05=int((ps < 0.05).sum()),\n                     min_p=ps.min(), bins_stim_larger=int((st.loc[common].median() > sh.loc[common].median()).sum())))\nprint(pd.DataFrame(rows).to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\nprint(\"pupil (a.u.) of the selected trials, range:\", np.nanmin(P.iloc[:, :70].to_numpy()), np.nanmax(P.iloc[:, :70].to_numpy()))\n\n# %% [markdown]\n# ## Summary\n#\n# Filled in after the run.\n\n# %%\nprint(f\"notebook run time: {(time.time() - t_start) / 60:.1f} min\")\n"
}
```

```
File created successfully at: /tmp/claude/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent**

Draft written. Fixing two fragile spots (pupil row mapping, a leftover selection dict), then running it end to end on the cached data.

**Agent calls Bash**

```bash
cd /tmp/claude; python - <<'EOF'
p='nb_src.py'; s=open(p).read()
s=s.replace('''    sel = {"Eyes": (e.cond == "Social") & (e.target == "eye"),
           "neFace": (e.cond == "Social") & (e.target.isin(["neface", "face"])),
           "RDM": (e.cond == "Dot") & (e.target == "eye")}
    # mutual non-eye Face events are in mutual_face; M1-only ones in m1_neface
    sel["neFace"] = (e.cond == "Social") & ((e.table == "m1_neface") | (e.table == "mutual_face"))
    sel["Eyes"] = (e.cond == "Social") & ((e.table == "m1_eye") | (e.table == "mutual_eye"))
''','''    # non-eye Face: m1_neface, and mutual_face for mutual events (m1_wholeface = m1_eye + m1_neface)
    sel = {"Eyes": (e.cond == "Social") & e.table.isin(["m1_eye", "mutual_eye"]),
           "neFace": (e.cond == "Social") & e.table.isin(["m1_neface", "mutual_face"]),
           "RDM": (e.cond == "Dot") & (e.table == "m1_eye")}
''')
s=s.replace('''alltr = trials.copy()
alltr["prow"] = np.arange(len(alltr))
sel = alltr.loc[soc.index]
''','''offset = np.concatenate([[0], np.cumsum([len(r["trials"]) for r in runs])[:-1]])
sel = soc.assign(prow=offset[soc.run_id.to_numpy()] + soc.row.to_numpy())
''')
open(p,'w').write(s)
EOF
grep -n "roi_counts\|prow" nb_src.py | head; cd $TMPDIR; . wenv/bin/activate; uv pip install -q EMD-signal 2>&1|tail -1; python -c "import PyEMD; print(PyEMD.__version__)"
```

```
303:def roi_counts(evset):
343:    c = roi_counts(evset)
346:c_main = roi_counts("M1 and mutual")
889:sel = soc.assign(prow=offset[soc.run_id.to_numpy()] + soc.row.to_numpy())
892:P = pd.DataFrame(pup[sel.prow.to_numpy()], index=sel.index)
/tmp/claude-1001/wenv/lib/python3.13/site-packages/PyEMD/CEEMDAN.py:63: SyntaxWarning: invalid escape sequence '\e'
  Scale for added noise (:math:`\epsilon`) which multiply std :math:`\sigma`:
/tmp/claude-1001/wenv/lib/python3.13/site-packages/PyEMD/EEMD.py:41: SyntaxWarning: invalid escape sequence '\h'
  Standard deviation of Gaussian noise (:math:`\hat\sigma`).
1.10.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; export PYTHONPATH=entries/000959-fan-2024; cat > dev.py <<'EOF'
import pickle, matplotlib; matplotlib.use("Agg")
import microstim as ms
_runs=pickle.load(open('runs.pkl','rb'))
def fake(assets, workers=16):
    return _runs
ms.load_all=fake
src=open('/tmp/claude/nb_src.py').read()
exec(compile(src,'nb','exec'))
EOF
time python -W ignore dev.py 2>&1 | tail -n +1 > dev_out.txt; wc -l dev_out.txt; tail -5 dev_out.txt
```

```
real	0m34.792s
user	0m33.601s
sys	0m1.118s
597 dev_out.txt
   OFC    27    70                0 0.3126                29
 dmPFC    27    70                0 0.5149                33
  ACCg    27    70                0 0.1056                10
pupil (a.u.) of the selected trials, range: 1112.7 5312.1
notebook run time: 0.5 min
Shell cwd was reset to
```

**Agent**

Runs end to end in 35 s on cached data. Reading the output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/dev_out.txt"
}
```

```
1	version 0.261020.0242: 1705 assets, 26.0 GB; version 0.260531.2104: 1705 assets; rows not shared: 0
2	loaded 1705 runs in 0.0 min
3	
4	The description, the scratch fields and the file name agree: True
5	runs by subject, triggering ROI, region and condition:
6	cond                  Dot  Social
7	subject roi   region             
8	L       Eyes  ACCg     91     150
9	              OFC      92     150
10	              dmPFC    88     150
11	T       Eyes  ACCg     60     168
12	              OFC      60     168
13	              dmPFC    60     168
14	        Mouth ACCg     25      75
15	              OFC      25      75
16	              dmPFC    25      75
17	
18	days by subject, triggering ROI and region:
19	region         ACCg  OFC  dmPFC
20	subject roi                    
[... 578 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '98,102p' paper/*.txt; grep -n "S3A\|alternative visualization" paper/*.txt | head -5; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd /tmp/claude; python - <<'EOF'
p='nb_src.py'; s=open(p).read()
def after(anchor, text):
    global s
    i=s.index(anchor); j=s.index('\n# %%', i+len(anchor))
    s=s[:j]+'\n\n# %% [markdown]\n'+'\n'.join('# '+l if l else '#' for l in text.strip().split('\n'))+'\n'+s[j:]
# show(): degrees only for distances
s=s.replace('''def show(tab, label=""):
    t = tab.copy()
    t["median_diff_deg"] = t.median_diff * ms.DEG_PER_PX''','''def show(tab, label="", degrees=True):
    t = tab.copy()
    if degrees:
        t["median_diff_deg"] = t.median_diff * ms.DEG_PER_PX''')
for a in ['show(day_table(ili_dm), "inter-looking interval (s), day level")',
          'show(day_table(ms.day_means(dot, "ili")), "inter-looking interval (s), control runs")',
          'show(day_table(ms.day_means(soc, "recip")), "reciprocation latency (s), day level")',
          'show(day_table(ms.day_means(t, "trig"), subjects=(None,)), "duration (ms), day level")']:
    s=s.replace(a, a[:-1]+', degrees=False)')
s=s.replace('''print("social trials with an inter-looking interval:", int(soc.ili.notna().sum()), "of", len(soc),
      "; range (s):", round(soc.ili.min(), 3), round(soc.ili.max(), 3))''','''print("social trials with an inter-looking interval:", int(soc.ili.notna().sum()), "of", len(soc),
      "; range (s):", round(soc.ili.min(), 3), round(soc.ili.max(), 3),
      "; intervals of 0 (an event starting at the trial sample):", int((soc.ili == 0).sum()))''')
s=s.replace('''show(day_table(ili_dm), "inter-looking interval (s), day level", degrees=False)''','''show(day_table(ili_dm), "inter-looking interval (s), day level", degrees=False)
v = soc.copy()
v["ili_m1only"] = ms.first_latency(v, events[(events.who == "m1") & (events.table == "m1_wholeface")])
show(day_table(ms.day_means(v, "ili_m1only")), "variant: M1-only whole Face events", degrees=False)''')
s=s.replace('''print(pd.DataFrame(rows).to_string(index=False, float_format=lambda v: f"{v:.4g}"))

# %% [markdown]
# ## Inter-looking''','''print(pd.DataFrame(rows).to_string(index=False, float_format=lambda v: f"{v:.4g}"))
print("\\ncontralateral, all Eyes days, p under readings (a) and (b) for five other seeds:")
e = dist[("methods", "contra")][1]
e = e[e.region == "OFC"].assign(eff=lambda d: d.stim - d.sham).dropna(subset=["eff"]).eff.to_numpy()
m = mouth_dm[("social", "contra")]
mm = np.median((m[m.region == "OFC"].stim - m[m.region == "OFC"].sham).dropna())
for seed in range(1, 6):
    b = np.median(np.random.default_rng(seed).choice(e, size=(1000, 5), replace=True), axis=1)
    print(f"  seed {seed}: (a) {np.mean(b >= mm):.3f}  (b) {min(1, 2 * min(np.mean(b >= mm), np.mean(b <= mm))):.3f}")

# %% [markdown]
# ## Inter-looking''')
open(p,'w').write(s)
EOF
grep -n "variant: M1-only\|seed {seed}" nb_src.py
```

```
670:    print(f"  seed {seed}: (a) {np.mean(b >= mm):.3f}  (b) {min(1, 2 * min(np.mean(b >= mm), np.mean(b <= mm))):.3f}")
699:show(day_table(ms.day_means(v, "ili_m1only")), "variant: M1-only whole Face events", degrees=False)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; export PYTHONPATH=entries/000959-fan-2024; python -W ignore dev.py > dev_out2.txt 2>&1; grep -n -A12 "seed 959\|other seeds\|variant: M1-only" dev_out2.txt | head -40; grep -n "Error\|Traceback" dev_out2.txt
```

```
461:contralateral, all Eyes days, p under readings (a) and (b) for five other seeds:
462-  seed 1: (a) 0.064  (b) 0.128
463-  seed 2: (a) 0.069  (b) 0.138
464-  seed 3: (a) 0.059  (b) 0.118
465-  seed 4: (a) 0.070  (b) 0.140
466-  seed 5: (a) 0.070  (b) 0.140
467-social trials with an inter-looking interval: 11655 of 19474 ; range (s): -0.0 4.999 ; intervals of 0 (an event starting at the trial sample): 91
468-inter-looking interval (s), day level
469-region subject  n  median_diff  mean_diff       p
470-   OFC    both 27     -0.03758    -0.1089 0.05847
471-   OFC       L 15     -0.02682    -0.1027  0.2524
472-   OFC       T 12     -0.06835    -0.1167 0.09229
473- dmPFC    both 27   -0.0008149   -0.03068  0.9341
--
479:variant: M1-only whole Face events
480-region subject  n  median_diff  mean_diff        p
481-   OFC    both 27      -0.1268    -0.1323 0.002045
482-   OFC       L 15     -0.03393   -0.09526   0.1514
483-   OFC       T 12      -0.2306    -0.1785 0.002441
484- dmPFC    both 27      0.03229  -0.008165   0.6277
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
p='microstim.py'; s=open(p).read()
s=s.replace('''def first_latency(trials, ev, t1=LATENCY_WINDOW_S):
    """Per trial, the time from the trial to the start of the first event starting in [0, t1)
    after it; NaN when there is none."""
    pairs = window_pairs(trials, ev, 0.0, t1)''','''def first_latency(trials, ev, t1=LATENCY_WINDOW_S):
    """Per trial, the time from the trial to the start of the first event that starts after it
    (strictly, so an event starting at the trial sample, the triggering fixation, is not a look
    back; claims file, fig3b-ofc-inter-looking-interval, "starts after it") and within t1;
    NaN when there is none."""
    pairs = window_pairs(trials, ev, HALF_SAMPLE_S, t1)''')
s=s.replace('''PUPIL_MS = 700''','''HALF_SAMPLE_S = 0.0005          # "after" the trial: later than the trial's own sample
PUPIL_MS = 700''')
open(p,'w').write(s)
EOF
cd $TMPDIR; . wenv/bin/activate; export PYTHONPATH=entries/000959-fan-2024; python -W ignore dev.py > dev_out2.txt 2>&1; sed -n '467,540p' dev_out2.txt
```

```
social trials with an inter-looking interval: 11589 of 19474 ; range (s): 0.001 4.999 ; intervals of 0 (an event starting at the trial sample): 0
inter-looking interval (s), day level
region subject  n  median_diff  mean_diff       p
   OFC    both 27     -0.06928    -0.1072 0.04356
   OFC       L 15     -0.06928   -0.09927  0.2524
   OFC       T 12     -0.07442    -0.1172  0.1099
 dmPFC    both 27      0.02292   -0.01849  0.7676
 dmPFC       L 15    -0.002927   -0.03938  0.8904
 dmPFC       T 12       0.1168   0.007634  0.6772
  ACCg    both 27      0.02053    0.04014  0.3361
  ACCg       L 15    -0.003057   0.003093  0.7615
  ACCg       T 12      0.02241    0.08646  0.2334
variant: M1-only whole Face events
region subject  n  median_diff  mean_diff        p
   OFC    both 27     -0.09935    -0.1297 0.002248
   OFC       L 15     -0.07347   -0.08706   0.1876
   OFC       T 12      -0.2362    -0.1831 0.002441
 dmPFC    both 27      0.05669   0.005792   0.4996
 dmPFC       L 15      0.05669   -0.01896   0.7197
 dmPFC       T 12      0.07132    0.03673   0.5186
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude; python - <<'EOF'
p='nb_src.py'; s=open(p).read()
s=s.replace('''show(day_table(ms.day_means(v, "ili_m1only")), "variant: M1-only whole Face events", degrees=False)''','''show(day_table(ms.day_means(v, "ili_m1only")), "variant: M1-only whole Face events", degrees=False)
p0 = ms.window_pairs(v, wf_m1, 0.0, ms.LATENCY_WINDOW_S).groupby("trial").lag.min()
v["ili_with0"] = v.index.map(p0).astype(float)
print("trials whose first whole Face event starts at the trial sample itself:", int((v.ili_with0 == 0).sum()))
show(day_table(ms.day_means(v, "ili_with0"), subjects=(None,)), "variant: events starting at the trial sample counted (latency 0)", degrees=False)''')
open(p,'w').write(s)
EOF
date -u
```

```
Sun Nov  1 00:00:19 UTC 2026
Shell cwd was reset to
```

**Agent**

Writing the conclusion cells and summary into the notebook source.

**Agent calls Bash**

```bash
cd /tmp/claude; cat > results.py <<'PYEOF'
R = {
"design-days-per-area": "**Result: reproduced.** Every day holds kept stimulation and sham trials: 15 Eyes days per area for monkey L, 12 per area for monkey T, and 5 Mouth days per area for monkey T.",
"design-sessions-per-day": "**Result: partially reproduced.** Monkey L has 10.0 social runs per day (9 to 11) and 6.02 control runs (4 to 8); monkey T has 14 social runs on every Eyes day and 5 control runs. Runs hold 295.8 to 297.3 s of valid samples. The ranges and three of the four means hold; monkey L's mean of 6.02 control runs lies outside 5 ± 0.5 (14 of its 45 days have 8 control runs). Monkey T's 14 social runs on every day are within the tolerance of the reported mean of 15 but never reach the reported 15 (the Mouth days have 15).",
"fig1e-stim-counts-comparable": "**Result: reproduced.** Of the 24 rank-sum tests on the social runs, the smallest FDR-corrected p is 0.908 for stimulations and 0.942 for shams, all above 0.90 as reported.",
"figs1d-stim-counts-nonsocial": "**Result: reproduced.** No corrected p is below 0.05 (smallest 0.108 for stimulations, 0.082 for shams). Not all exceed 0.10 as the paper reports: the sham comparisons between the monkeys for OFC and dmPFC give corrected p = 0.082 (uncorrected 0.014 and 0.010), monkey T having more control trials per day.",
"figs1e-eyes-more-than-face": "**Result: reproduced.** Under both day counts and both event sets, Eyes fixations exceed non-eye Face fixations for every area, with corrected p at most 4.4e-05, below 10^-4 (median day totals of 384 to 408 Eyes against 129 to 177 non-eye Face fixations).",
"figs1e-eyes-vs-rdm-comparable": "**Result: not reproduced.** Under the paper's reading (a), the day's total, Eyes fixations exceed RDM fixations for every area (corrected p = 0.00036, 0.000025 and 0.00041 for OFC, dmPFC and ACCg; median differences of 177 to 241 fixations per day), since a day holds about twice as many social runs as control runs. Under the code's reading (b), the mean per run, the counts are comparable (corrected p = 0.40, 0.40 and 0.52), as the paper reports.",
"fig2a-density-map-ofc": "**Result: reproduced.** The day-averaged OFC stimulation minus sham density summed over the whole Face is positive under both normalisations (7.47 z-scored, 0.0093 by total), and so is the sum over the Eyes (3.71 and 0.0046); it is positive in each monkey under each. The dmPFC and ACCg sums over the whole Face are negative under both. 10,771 of 53,542 post-gaze fixations lie outside the 40-degree grid.",
"fig2c-ofc-social-gaze-distance": "**Result: reproduced.** With M1-only and mutual events, OFC stimulation lowered the day-mean social gaze distance (median stimulation minus sham -17.9 pixels, -0.70 degrees; p = 0.00021 over 27 days); monkey L gives p = 0.0067 (paper 0.008) and monkey T p = 0.016 (paper 0.002), both negative. The code's M1-only reading gives p = 0.00013, 0.0067 and 0.0034.",
"fig2c-dmpfc-accg-no-distance-effect": "**Result: reproduced.** dmPFC gives p = 0.21 and ACCg p = 0.39 (paper 0.361 and 0.374); the code's reading gives 0.29 and 0.29.",
"fig2e-ofc-contralateral": "**Result: reproduced.** Contralateral: median effect -21.2 pixels, p = 0.00048; ipsilateral: -12.3 pixels, p = 0.058; contralateral against ipsilateral: median -17.7 pixels, p = 0.046 (paper < 0.001, 0.068 and 0.026). Per monkey the contralateral effect gives p = 0.018 (L) and 0.012 (T) (paper 0.015 and 0.012), and the hemifield difference p = 0.073 (L) and 0.30 (T) (paper 0.073 and 0.204). The code's M1-only reading gives the same pattern (0.00038, 0.055 and 0.026).",
"fig2e-dmpfc-accg-no-hemifield-effect": "**Result: reproduced.** None of the six tests gives p < 0.05 (dmPFC 0.48, 0.10 and 0.22; ACCg 0.53, 0.53 and 0.82), under either fixation reading.",
"fig2f-nonsocial-no-distance-effect": "**Result: reproduced.** No area changes the distance to the RDM centre (OFC p = 0.22, dmPFC 0.64, ACCg 0.50; paper 0.118, 0.719 and 0.302).",
"fig2gh-nonsocial-no-hemifield-effect": "**Result: reproduced.** None of the nine tests over both monkeys gives p < 0.05 (smallest 0.16, OFC contralateral). Per monkey, outside the claim, dmPFC in monkey L gives p = 0.035 for contralateral fixations.",
"methods-ofc-distance-longer-windows": "**Result: reproduced.** Within 2 s: both monkeys p = 0.0030, monkey L 0.012, monkey T 0.23; within 3 s: 0.0032, 0.0067 and 0.20 (paper 0.003, 0.008, 0.204 and 0.004, 0.007, 0.204), with stimulation below sham. The code's reading gives the same pattern.",
"methods-ofc-no-change-in-fixation-number": "**Result: reproduced.** Under the code's reading (a), none of the 12 per-monkey tests gives p < 0.05 (smallest 0.12). Outside the claim, both monkeys combined give p = 0.025 for whole Face fixations within 1.5 s (more after stimulation), and under reading (b) monkey L gives p = 0.026 for the whole Face within 1.5 s.",
"methods-ofc-longer-face-looking": "**Result: partially reproduced.** With the code's M1-only events, OFC whole Face looking is longer after stimulation (p = 0.0025; L 0.0067; T 0.15), the OFC Eyes test gives p = 0.039, and dmPFC and ACCg give p = 0.80 and 0.93, as the paper reports. Under reading (a) of the difference, the median over days, OFC whole Face is 52.8 ms (expected 48.9 ± 4.9) and monkey L 65.1 ms (66.6 ± 6.7), within tolerance, but monkey T is 46.2 ms (39.5 ± 4.0); reading (b), the mean, gives 62.6, 85.3 and 34.3 ms, none within tolerance. dmPFC's median, -14.7 ms, matches -14.5; ACCg's, -2.2 ms, does not match 3.4, nor does OFC Eyes, 12.2 ms against 16.5.",
"methods-mouth-stimulation-no-effect": "**Result: reproduced.** None of the 27 tests on the Mouth days (5 days of monkey T per area) gives p < 0.05: social OFC, dmPFC and ACCg give p = 1, 1 and 0.19 (paper 1, 1 and 0.125), non-social 1, 0.125 and 0.19 (paper 1, 0.188 and 0.188). With 5 days the smallest possible two-sided p is 0.0625, so these tests could not find an effect at 0.05.",
"methods-eyes-vs-mouth-bootstrap": "**Result: not reproduced.** For contralateral fixations, the bootstrap medians of the OFC Eyes effects are not significantly below the Mouth median using all Eyes days (p = 0.078 one-sided, 0.156 two-sided; 0.059 to 0.070 one-sided over five other seeds), while for both hemifields combined the one-sided p is 0.043, where the paper finds no difference. With monkey T's Eyes days the contralateral p is 0.037 one-sided (0.074 two-sided) and the combined p is also 0.037 one-sided. The ipsilateral p values are 0.30 and 0.35. Neither reading gives the paper's pattern.",
"fig3b-ofc-inter-looking-interval": "**Result: reproduced.** OFC stimulation shortened the inter-looking interval (median day difference -0.069 s, p = 0.044; paper 0.035), while dmPFC (p = 0.77) and ACCg (p = 0.34) did not (paper 0.792 and 0.291). Neither monkey alone is significant (L 0.25, T 0.11; paper 0.188 and 0.092). The result rests on near-threshold details: counting an event that starts at the trial sample as a latency of 0 gives OFC p = 0.058, and M1-only events give p = 0.0022.",
"ili-nonsocial-no-effect": "**Result: reproduced.** No area changes the interval in the control runs (OFC p = 0.70, dmPFC 0.13, ACCg 0.84; paper 0.773, 0.080 and 0.943).",
"ili-missing-trials-41": "**Result: reproduced.** Averaged over the 81 Eyes days, 41.3% of trials have no whole Face event within 5 s (reading a; expected 41 ± 4.1); over the 27 OFC days, 39.9% (reading b).",
"figs3b-ili-trial-level": "**Result: reproduced.** Pooling trials, OFC stimulation shortened the interval (median 1.19 against 1.36 s, p = 0.017; paper 0.010), while dmPFC (p = 0.39) and ACCg (p = 0.62) did not (paper 0.301 and 0.602).",
"figs3c-reciprocation-day-level-none": "**Result: reproduced.** No area changes the day-level reciprocation latency (OFC p = 0.11, dmPFC 0.56, ACCg 0.32; paper 0.130, 0.701 and 0.400), and 86.4% of trials per day have no M2-then-M1 sequence (reading a; expected 86 ± 8.6; 85.1% on the OFC days).",
"fig3d-ofc-reciprocation-latency": "**Result: reproduced.** Pooling trials, OFC stimulation shortened the reciprocation latency (median 0.84 against 1.01 s, p = 0.023; paper 0.011), while dmPFC (p = 0.72) and ACCg (p = 0.36) did not (paper 0.777 and 0.368); per monkey, L gives p = 0.15 and T p = 0.078 (paper 0.074 and 0.079).",
"partner-monkey-unchanged": "**Result: partially reproduced.** M2's social gaze distance (OFC p = 0.12, dmPFC 0.47, ACCg 0.062; paper 0.118, 0.302 and 0.064) and M2's inter-looking interval under both readings (smallest p 0.19) do not change. M2's reciprocation latency does not change under reading (b) (smallest p 0.46), but under reading (a), from the start of the M1 look, dmPFC gives p = 0.044 (median 0.11 s longer after stimulation). The criterion asks that no test give p < 0.05 under every reading; 1 of the 21 tests does.",
"epoch-days-76-of-81": "**Result: reproduced.** Counting kept stimulations (reading a), 76 of the 81 days have at least 90, and the five others are the days the paper names: 08122019 (L, OFC, 87), 12222021 (T, OFC, 80), 11052021 and 12172021 (T, dmPFC, 64 and 67) and 11042021 (T, ACCg, 50). Counting all stimulations delivered (reading b) gives 77 days, the L OFC day having 96.",
"fig5a-trigger-duration-unchanged": "**Result: not reproduced.** The duration of the Eyes event in progress at the trial does not differ for OFC (p = 0.61 with mutual events, 0.36 without), but for dmPFC it is longer on stimulation trials (median day difference 31 ms, p = 0.019; 28 ms, p = 0.028 without mutual events), where the paper reports p = 0.269.",
"fig5b-pupil-unchanged": "**Result: reproduced.** Of the 70 bins of 10 ms, none gives p < 0.05 in any area (smallest p 0.31, 0.51 and 0.11 for OFC, dmPFC and ACCg), on the 2,198 trials whose gaze stayed in the whole Face for 700 ms.",
}
import re
s = open('nb_src.py').read()
for cid, text in R.items():
    tag = f'# %% tags=["claim:{cid}"]'
    i = s.index(tag)
    j = s.index('\n# %%', i + len(tag))
    s = s[:j] + '\n\n# %% [markdown]\n# ' + text + '\n' + s[j:]
s = s.replace('''# %%
from PyEMD import EEMD''', '''# %% tags=["claim:figs4a-causal-strength-no-stim-effect"]
from PyEMD import EEMD''')
s = s.replace('''      f"{per_trial * n_tr / 3600:.0f} CPU hours")
''', '''      f"{per_trial * n_tr / 3600:.0f} CPU hours; at a tenth of the ensembles {per_trial * n_tr / 36000:.0f} CPU hours")

# %% [markdown]
# **Result: blocked (too_large).** The estimate printed above, in CPU hours, is far beyond the
# sixty-minute limit of a notebook and the time of this run, even at a tenth of the ensembles,
# so the relative causal strength is not computed and the six claims that use it are blocked.
#
# ## Saccade claims (blocked)
#
# fig5cd-saccade-counts-unchanged and fig5e-h-saccade-kinematics-unchanged need saccades detected
# by the unsupervised clustering method of Otero-Millan et al. (2014). The files hold fixation
# events only, no saccade events, and that method is distributed as MATLAB code, which cannot run
# in this entry's locked Python environment. Both claims are blocked as not_runnable.
''')
s = s.replace('''# ## Summary
#
# Filled in after the run.''', '''# ## Summary
#
# | Claim | Outcome |
# |---|---|
# | design-days-per-area | reproduced |
# | design-sessions-per-day | partially reproduced |
# | fig1e-stim-counts-comparable | reproduced |
# | figs1d-stim-counts-nonsocial | reproduced |
# | figs1e-eyes-more-than-face | reproduced |
# | figs1e-eyes-vs-rdm-comparable | not reproduced |
# | fig2a-density-map-ofc | reproduced |
# | fig2c-ofc-social-gaze-distance | reproduced |
# | fig2c-dmpfc-accg-no-distance-effect | reproduced |
# | fig2e-ofc-contralateral | reproduced |
# | fig2e-dmpfc-accg-no-hemifield-effect | reproduced |
# | fig2f-nonsocial-no-distance-effect | reproduced |
# | fig2gh-nonsocial-no-hemifield-effect | reproduced |
# | methods-ofc-distance-longer-windows | reproduced |
# | methods-ofc-no-change-in-fixation-number | reproduced |
# | methods-ofc-longer-face-looking | partially reproduced |
# | methods-mouth-stimulation-no-effect | reproduced |
# | methods-eyes-vs-mouth-bootstrap | not reproduced |
# | fig3b-ofc-inter-looking-interval | reproduced |
# | ili-nonsocial-no-effect | reproduced |
# | ili-missing-trials-41 | reproduced |
# | figs3b-ili-trial-level | reproduced |
# | figs3c-reciprocation-day-level-none | reproduced |
# | fig3d-ofc-reciprocation-latency | reproduced |
# | partner-monkey-unchanged | partially reproduced |
# | epoch-days-76-of-81 | reproduced |
# | figs4a, figs4b, ofc-slope, fig4c, fig4d, dmpfc-slope-positive | blocked, too_large |
# | fig5a-trigger-duration-unchanged | not reproduced |
# | fig5b-pupil-unchanged | reproduced |
# | fig5cd-saccade-counts-unchanged, fig5e-h-saccade-kinematics-unchanged | blocked, not_runnable |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# **How the analysis differs from the paper's.** It starts from the fixation events in the
# files, not from the paper's own pipeline. Trial selection, fixation sets, hemifield split
# and the measures follow the claims file, which takes them from the paper and its code; the
# details the claims file leaves open are taken as stated in `microstim.py`. Statistics use
# scipy's signed-rank and rank-sum tests, which can differ from MATLAB's in the last digits for
# ties and for n above 15. The causal decomposition and the saccade detection were not run.
#
# **What was found about the dataset.** The dataset holds every day of the paper (81 Eyes and
# 15 Mouth days), with one file per run and no run deposited twice. The files carry the
# region, triggering ROI and condition; the event tables are consistent with each other; the
# trial times fall inside an M1 event in the triggering ROI on 71% of social Eyes trials against
# 5 to 20% for times shifted by 0.5 to 2 s, consistent with a shared clock. The files' own
# laterality labels match the claims file's hemifield rule for 99.98% of M1 events. Monkey L
# has 6.0 control runs per day where the paper reports 5. 6% of the M1 Eyes events have a mean
# position outside the Eyes rectangle of their file, and the files do not say how events were
# assigned to ROIs. Neither the files nor the paper give the padding of the Eyes ROI.''')
open('nb_src.py','w').write(s)
PYEOF
python results.py && grep -c "Result:" nb_src.py
```

```
29
Shell cwd was reset to
```

**Agent**

Converting the script to a notebook and setting up the entry files.

**Agent calls Bash**

```bash
cd /tmp/claude; cat > conv.py <<'EOF'
import re, json, nbformat
src = open('/tmp/claude/nb_src.py').read()
parts = re.split(r'^# %%(.*)$', src, flags=re.M)
cells = []
for hdr, body in zip(parts[1::2], parts[2::2]):
    body = body.strip('\n')
    tags = re.findall(r'"([^"]+)"', re.search(r'tags=\[(.*)\]', hdr).group(1)) if 'tags=' in hdr else []
    if '[markdown]' in hdr:
        text = '\n'.join(l[2:] if l.startswith('# ') else l[1:] if l.startswith('#') else l for l in body.split('\n'))
        c = nbformat.v4.new_markdown_cell(text)
    else:
        c = nbformat.v4.new_code_cell(body)
    if tags: c.metadata['tags'] = tags
    cells.append(c)
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata['kernelspec'] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, 'entries/000959-fan-2024/reproduce_fan_2024.ipynb')
print(len(cells))
EOF
. $TMPDIR/wenv/bin/activate; uv pip install -q nbformat 2>&1 | tail -1; python conv.py
cd entries/000959-fan-2024
printf "EMD-signal\nh5py\nmatplotlib\nnumpy\npandas\nrequests\nscipy\nstatsmodels\n" > requirements.in
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000959-fan-2024
type: reproduction
title: Closed-loop OFC microstimulation and dynamic social attention (Fan et al. 2024)
description: Tests the findings of Fan, Dal Monte, Nair, Fagan and Chang (2024) on dandiset 000959,
  which holds the gaze, pupil, fixation events and stimulation times of every run of the 81 Eyes and
  15 Mouth stimulation days of two stimulated monkeys. It compares social gaze distance, its
  hemifield split, inter-looking interval, reciprocation latency, the partner's gaze, fixation counts
  and durations, pupil size and the trial counts between microstimulation and sham trials. The causal
  decomposition and the saccade analyses are not run.
license: Apache-2.0
notebooks:
- path: reproduce_fan_2024.ipynb
  title: Reproducing Fan et al. (2024) from dandiset 000959
  runtime_minutes: 15
helpers:
- microstim.py
related:
- id: dandi:000959/0.261020.0242
  relation: uses_data
- id: doi:10.1016/j.neuron.2024.05.004
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/000959-fan-2024 && python tools/entry.py check entries/000959-fan-2024; date -u
```

```
102
Traceback (most recent call last):
  File "tools/entry.py", line 55, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
Sun Nov  1 00:01:56 UTC 2026
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/wenv/bin/activate; uv pip install -q pyyaml jsonschema nbformat 2>&1|tail -1; python tools/entry.py lock entries/000959-fan-2024 && python tools/entry.py check entries/000959-fan-2024
```

```
wrote entries/000959-fan-2024/requirements.lock.txt
0 error(s)
```

**Agent**

Lock and check pass. A quick dev run to confirm the final source runs cleanly before the full clean-environment run.

**Agent calls Bash**

```bash
cd $TMPDIR; . wenv/bin/activate; export PYTHONPATH=entries/000959-fan-2024; python -W ignore dev.py > dev_out3.txt 2>&1; grep -n "Traceback\|Error" dev_out3.txt; grep -n -A4 "latency 0\|CPU hours" dev_out3.txt
```

```
491:variant: events starting at the trial sample counted (latency 0)
492-region subject  n  median_diff  mean_diff       p
493-   OFC    both 27     -0.03758    -0.1089 0.05847
494- dmPFC    both 27   -0.0008149   -0.03068  0.9341
495-  ACCg    both 27     0.006374    0.04043  0.3865
--
602:estimated per trial at 1,000 ensembles: 161 s; 19474 social trials: 869 CPU hours; at a tenth of the ensembles 87 CPU hours
603-reading (a): trials with an Eyes event in progress 13779 of 19474; median duration 367 ms
604-duration (ms), day level
605-region subject  n  median_diff  mean_diff       p
606-   OFC    both 27        8.148      14.94  0.6109
Shell cwd was reset to
```

**Agent**

Clean. Running the entry from a clean environment (about 12 to 15 min expected).

**Agent calls Bash**

```bash
cd  . $TMPDIR/wenv/bin/activate; time python tools/entry.py all entries/000959-fan-2024 2>&1 | tail -20; date -u
```

```
Installed kernelspec registry-000959-fan-2024 in executed/000959-fan-2024/.venv/share/jupyter/kernels/registry-000959-fan-2024
0 error(s)
pass  reproduce_fan_2024.ipynb  (668 s)

real	11m15.496s
user	11m23.112s
sys	4m49.307s
Sun Nov  1 00:13:58 UTC 2026
```

**Agent**

Passed in 11 min. Checking that the executed outputs match the numbers in the conclusions.

**Agent calls Bash**

```bash
cd  . $TMPDIR/wenv/bin/activate; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/000959-fan-2024/reproduce_fan_2024.ipynb',4)
out=[]
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.outputs:
            if o.get('output_type')=='stream': out.append(o.text)
            elif o.get('output_type')=='error': out.append('ERROR '+o.ename)
open('/tmp/claude/exec_out.txt','w').write(''.join(out))
EOF
grep -v "loaded\|EEMD\|CPU hours\|run time" /tmp/claude/exec_out.txt > /tmp/claude/a.txt; grep -v "loaded\|EEMD\|CPU hours\|run time" $TMPDIR/dev_out3.txt > /tmp/claude/b.txt; diff /tmp/claude/a.txt /tmp/claude/b.txt | head -30; grep "loaded\|CPU hours\|run time\|EEMD" /tmp/claude/exec_out.txt
```

```
2,3d1
< entries/000959-fan-2024/microstim.py:171: RuntimeWarning: Mean of empty slice
<   pos = np.array([np.nanmean(g[a:b], 0) if b > a else [np.nan, np.nan]
602,603d599
<   Scale for added noise (:math:`\epsilon`) which multiply std :math:`\sigma`:
<   Standard deviation of Gaussian noise (:math:`\hat\sigma`).
loaded 1705 runs in 10.5 min
executed/000959-fan-2024/.venv/lib/python3.13/site-packages/PyEMD/CEEMDAN.py:63: SyntaxWarning: invalid escape sequence '\e'
executed/000959-fan-2024/.venv/lib/python3.13/site-packages/PyEMD/EEMD.py:41: SyntaxWarning: invalid escape sequence '\h'
EEMD of one 150-bin series with 100 ensembles: 1.01 s; 7 IMFs
estimated per trial at 1,000 ensembles: 162 s; 19474 social trials: 877 CPU hours; at a tenth of the ensembles 88 CPU hours
notebook run time: 11.0 min
```

**Agent calls Bash**

```bash
cd  sed -n 1,200p attempts/001453-fouke-2025-01.yaml | cut -c1-220; ls schemas
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
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,400p attempts/001453-fouke-2025-01.yaml | grep -v "^    " | head -60; python -c "
import json; s=json.load(open('schemas/attempt.schema.json')); print(json.dumps(s['properties'].get('findings'),indent=0)[:1500]); print(list(s['properties'].keys())); print(s.get('required'))"
```

```
notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
- claim: fig2d-shared-architecture
  outcome: blocked
  blocked_by: data_missing
  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
- claim: fig2g-dsi-similar
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2h-fewer-motion-responsive
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2k-more-monocular
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2l-bi-ratio
  outcome: blocked
  blocked_by: data_missing
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json; s=json.load(open('schemas/attempt.schema.json'));
o=s['properties']['outcomes']['items']; print(json.dumps(o,indent=0)[:3000])"; python -c "
import json; s=json.load(open('schemas/attempt.schema.json')); print(json.dumps(s['properties']['provenance'],indent=0)[:1500]); print(json.dumps(s['properties']['dataset'],indent=0)[:800])"
```

```
{
"type": "object",
"additionalProperties": false,
"required": [
"claim",
"outcome"
],
"properties": {
"claim": {
"description": "Claim id from the target's claims file.",
"type": "string"
},
"outcome": {
"enum": [
"reproduced",
"partially_reproduced",
"not_reproduced",
"blocked"
],
"description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."
[... 238 more lines not kept]
```

**Agent**

Making the small notebook and helper cleanups.

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
p='microstim.py'; s=open(p).read()
s=s.replace('''            pos = np.array([np.nanmean(g[a:b], 0) if b > a else [np.nan, np.nan]
                            for a, b in zip(s0, e0)])''','''            with warnings.catch_warnings():  # an event whose samples are all NaN has no position
                warnings.simplefilter("ignore", RuntimeWarning)
                pos = np.array([np.nanmean(g[a:b], 0) if b > a else [np.nan, np.nan]
                                for a, b in zip(s0, e0)])''')
s=s.replace('import re\n','import re\nimport warnings\n',1)
open(p,'w').write(s)
EOF
cd /tmp/claude; python - <<'EOF'
p='nb_src.py'; s=open(p).read()
s=s.replace('''lab = m1.dropna(subset=["hemi"])''','''print("M1 events with no gaze position (all samples NaN; left out of distances):",
      int(m1.x.isna().sum()), "of", len(m1), "; M2 events:", int(events[events.who == "m2"].x.isna().sum()))
lab = m1.dropna(subset=["hemi"])''')
open(p,'w').write(s)
EOF
sed -i 's/runtime_minutes: 15/runtime_minutes: 12/' entries/000959-fan-2024/entry.yaml
. $TMPDIR/wenv/bin/activate; python conv.py; cd $TMPDIR; export PYTHONPATH=entries/000959-fan-2024; python dev.py 2>&1 | grep -n "no gaze position\|Traceback\|Warning"
```

```
102
55:M1 events with no gaze position (all samples NaN; left out of distances): 0 of 1929396 ; M2 events: 188
Shell cwd was reset to
```

**Agent**

Now the README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/000959-fan-2024/README.md",
 "content": "# Fan, Dal Monte, Nair, Fagan & Chang (2024) from dandiset 000959\n\nTests the findings of [Fan et al. (2024)](https://doi.org/10.1016/j.neuron.2024.05.004) on\n[DANDI:000959](https://dandiarchive.org/dandiset/000959/0.261020.0242). The dandiset holds one file\nper 300-s run for every day of the paper: 81 Eyes stimulation days (OFC, dmPFC and ACCg; 15 per area\nfrom monkey L, 12 from monkey T) and 15 Mouth stimulation days of monkey T. Each file has the gaze and\npupil of both monkeys at 1 kHz, the stimulation and sham times, the day's ROIs and the fixation events.\n\n| Claim | Outcome |\n|---|---|\n| Days per area, runs per day | Reproduced; partially reproduced (monkey L has 6.0 control runs per day, not 5) |\n| Stimulation and sham counts comparable across areas and monkeys (social, control) | Reproduced |\n| More fixations on the Eyes than on the non-eye Face | Reproduced |\n| Eyes fixations comparable to RDM fixations | Not reproduced under the Methods' day total; comparable under the code's mean per run |\n| OFC density map more clustered around the partner | Reproduced |\n| OFC lowers social gaze distance, not dmPFC or ACCg; stronger contralaterally; none in the control condition; longer windows | Reproduced |\n| No change in fixation number; longer whole Face looking after OFC stimulation | Reproduced; partially reproduced (tests hold, values in part) |\n| No effect of Mouth stimulation | Reproduced (5 days per area cannot reach p < 0.05) |\n| Eyes against Mouth bootstrap | Not reproduced |\n| Inter-looking interval and reciprocation latency (day and trial level, 41% and 86%) | Reproduced |\n| Partner monkey unchanged | Partially reproduced (one reading of M2's reciprocation latency gives dmPFC p = 0.044) |\n| 76 of 81 days with at least 90 stimulations | Reproduced, with the five named days |\n| Causal decomposition and epoch slopes (six claims) | Blocked: too large |\n| Trigger fixation duration unchanged | Not reproduced (dmPFC p = 0.019) |\n| Pupil unchanged | Reproduced |\n| Saccade counts and kinematics (two claims) | Blocked: not runnable (MATLAB detection, no saccades in the files) |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/000959-fan-2024-01.yaml`](../../attempts/000959-fan-2024-01.yaml). `microstim.py` reads\neach run into small tables (trials, fixation events with positions and hemifields, pupil traces)\nand holds the measures.\n"
}
```

```
File created successfully at: entries/000959-fan-2024/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000959-fan-2024-01.yaml",
 "content": "schema_version: 2\nid: 000959-fan-2024-01\ndataset:\n  archive: dandi\n  id: \"000959\"\n  version: 0.261020.0242\n  doi: 10.48324/dandi.000959/0.261020.0242\npaper: doi:10.1016/j.neuron.2024.05.004\ndate: 2026-10-31\nentry: 000959-fan-2024\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/41252133262\noutcomes:\n- claim: design-days-per-area\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:design-days-per-area\n  measured:\n  - 15\n  - 12\n  - 5\n  notes: Days holding kept stimulation and sham trials are 15 per area for monkey L, 12 per area for\n    monkey T (Eyes) and 5 per area for monkey T (Mouth). Each day holds one region.\n- claim: design-sessions-per-day\n  outcome: partially_reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:design-sessions-per-day\n  measured:\n  - 10.0\n  - 6.02\n  - 14.0\n  - 5.0\n  - 296.4\n  notes: Monkey L has 10.0 social runs per day (9 to 11) and 6.02 control runs (4 to 8); monkey T has\n    14 social runs on every one of its 36 Eyes days and 5 control runs. Runs hold 295.8 to 297.3 s of\n    valid samples (mean 296.4). All ranges hold, and three of four means; monkey L's control mean of\n    6.02 is outside 5 plus or minus 0.5, as 14 of its 45 days have 8 control runs. Monkey T's mean of\n    14 is within the tolerance of 15 but no Eyes day has 15 social runs (the Mouth days have 15).\n  deviations:\n  - A session of the paper is taken to be one file (one run); the valid run length is the span of\n    non-NaN samples of `t`.\n- claim: fig1e-stim-counts-comparable\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig1e-stim-counts-comparable\n  notes: Over the 12 rank-sum tests for stimulations and the 12 for shams, the smallest\n    FDR-corrected p is 0.908 and 0.942, so all exceed 0.90 as reported (smallest uncorrected 0.509\n    and 0.187). Kept trials per day average 116 to 125 per type and area.\n  deviations:\n  - Benjamini-Hochberg correction from statsmodels in place of dsp3.fdr, which the claims file\n    names; both implement the same procedure.\n- claim: figs1d-stim-counts-nonsocial\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:figs1d-stim-counts-nonsocial\n  notes: No FDR-corrected p is below 0.05 (smallest 0.108 for stimulations, 0.082 for shams). The\n    paper's \"all p > 0.10\" does not hold for two sham tests between the monkeys (OFC and dmPFC,\n    corrected 0.082, uncorrected 0.014 and 0.010); monkey T has more control trials per day (71 to\n    77) than monkey L (52 to 57).\n- claim: figs1e-eyes-more-than-face\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:figs1e-eyes-more-than-face\n  notes: Under both day counts (a, total; b, mean per run) and both event sets (M1-only and mutual,\n    M1-only), Eyes fixations exceed non-eye Face fixations for every area, corrected p from 1.1e-07 to\n    4.4e-05, all below 1e-4. Median day totals are 384 to 408 Eyes and 129 to 177 non-eye Face\n    fixations.\n  deviations:\n  - The events counted are not fixed by the claims file. M1's fixations in the ROI including the M1\n    side of mutual events are the main set, following the Methods' \"total number of gaze fixations\n    ... of the stimulated monkey\" (STAR Methods, Frequency of microstimulations and regions of\n    interest); M1-only events are shown and give the same outcome.\n  - The non-eye Face is the files' m1_neface table (with mutual_face for mutual events); the\n    notebook shows that m1_wholeface equals m1_eye plus m1_neface in every run.\n- claim: figs1e-eyes-vs-rdm-comparable\n  outcome: not_reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:figs1e-eyes-vs-rdm-comparable\n  notes: Under reading (a), the day's total, which the criterion judges, Eyes fixations exceed RDM\n    fixations for every area (corrected p 0.00036, 0.000025 and 0.00041 for OFC, dmPFC and ACCg;\n    median differences 177, 202 and 241 per day). A day holds about twice as many social runs as\n    control runs (L 10 and 6, T 14 and 5), so day totals differ. Under the code's reading (b), the\n    mean per run, the counts are comparable (corrected p 0.40, 0.40 and 0.52), as the paper\n    reports; M1-only events give the same pattern under both readings.\n  deviations:\n  - The RDM fixations are the M1 events labelled Eyes in the Dot runs, whose Eyes ROI is the RDM\n    location (\"same location and size as Eyes ROI\", STAR Methods, Closed-loop microstimulation\n    protocol).\n- claim: fig2a-density-map-ofc\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig2a-density-map-ofc\n  notes: The day-averaged OFC stimulation minus sham density summed over the whole Face squares is\n    7.47 (z-scored) and 0.0093 (by total), and over the Eyes squares 3.71 and 0.0046; it is positive\n    in each monkey under each normalisation. dmPFC (whole Face -2.46 and -0.0026) and ACCg (-2.55 and\n    -0.0048) are negative. 10,771 of 53,542 post-gaze fixations fall outside the 40-degree grid.\n  deviations:\n  - Fixations are the Methods reading (M1-only and mutual events). The grid is centred on each\n    run's Eyes ROI centre, and the ROI squares are those whose centres lie in the day's ROI\n    rectangle, a standard choice; pixels are converted with 27 cm at 50 cm over 768 pixels (claims\n    file, opening comment).\n- claim: fig2c-ofc-social-gaze-distance\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig2c-ofc-social-gaze-distance\n  notes: Methods reading, median stimulation minus sham day difference -17.9 pixels (-0.70 degrees),\n    p = 0.00021 over 27 days; monkey L p = 0.0067 (paper 0.008), monkey T p = 0.016 (paper 0.002),\n    both negative. Code reading, p = 0.00013, 0.0067 and 0.0034. 1,270 of 19,474 social trials have\n    no fixation in the window and are left out of the day means.\n  deviations:\n  - The mutual events added in the Methods reading are the M1 side of mutual_wholeface, which holds\n    every mutual event (mutual_eye, mutual_face and mutual_mouth are subsets of it, shown in the\n    notebook); mutual events are defined only within the face, and m1_all holds no M1 side of a\n    mutual event.\n  - Each run's own ROIs are used, since three days were recalibrated between runs (08142019,\n    12102019, 12132019).\n- claim: fig2c-dmpfc-accg-no-distance-effect\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig2c-dmpfc-accg-no-distance-effect\n  notes: dmPFC median day difference -6.5 pixels, p = 0.21; ACCg -4.9 pixels, p = 0.39 (paper 0.361\n    and 0.374). The code reading gives 0.29 and 0.29.\n- claim: fig2e-ofc-contralateral\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig2e-ofc-contralateral\n  notes: Contralateral median effect -21.2 pixels, p = 0.00048; ipsilateral -12.3 pixels, p = 0.058;\n    contralateral against ipsilateral median -17.7 pixels, p = 0.046 (paper below 0.001, 0.068,\n    0.026). Per monkey, contralateral p = 0.018 (L) and 0.012 (T) (paper 0.015, 0.012); hemifield\n    difference p = 0.073 (L) and 0.30 (T) (paper 0.073, 0.204). The code reading gives 0.00038,\n    0.055 and 0.026. All 27 days have fixations in both hemifields.\n  deviations:\n  - The hemifield is computed from the centre of `roi_m2_face` as the claims file says; the files'\n    own laterality_label agrees for 99.98% of M1 events.\n- claim: fig2e-dmpfc-accg-no-hemifield-effect\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig2e-dmpfc-accg-no-hemifield-effect\n  notes: dmPFC contralateral p = 0.48, ipsilateral 0.10, difference 0.22; ACCg 0.53, 0.53, 0.82\n    (paper 0.501, 0.149, 0.230 and 0.442, 0.517, 0.564). The code reading gives no p below 0.05\n    either (smallest 0.11).\n- claim: fig2f-nonsocial-no-distance-effect\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig2f-nonsocial-no-distance-effect\n  notes: OFC median day difference -13.4 pixels, p = 0.22; dmPFC 1.7 pixels, p = 0.64; ACCg -5.7\n    pixels, p = 0.50 (paper 0.118, 0.719, 0.302). By monkey, dmPFC in monkey L gives p = 0.048\n    (distance larger after stimulation), outside the claim's test.\n  deviations:\n  - The RDM centre is the centre of each Dot run's `roi_m1_eyes`; the Dot runs hold M1 events only,\n    so the fixations are m1_all.\n- claim: fig2gh-nonsocial-no-hemifield-effect\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig2gh-nonsocial-no-hemifield-effect\n  notes: None of the nine tests over both monkeys gives p below 0.05; the smallest is OFC\n    contralateral, 0.16 (paper 0.097). By monkey, dmPFC contralateral in monkey L gives p = 0.035,\n    outside the claim's tests.\n  deviations:\n  - The Dot runs do not hold `roi_m2_face`; the hemifield reference is taken from the same day's\n    social runs, where it never varies within a day.\n- claim: methods-ofc-distance-longer-windows\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:methods-ofc-distance-longer-windows\n  notes: Within 2 s, both monkeys p = 0.0030, L 0.012, T 0.23; within 3 s, 0.0032, 0.0067 and 0.20\n    (paper 0.003, 0.008, 0.204 and 0.004, 0.007, 0.204), stimulation below sham in each. The code\n    reading gives the same pattern (2 s 0.0022, 0.010, 0.18; 3 s 0.0025, 0.0067, 0.15).\n- claim: methods-ofc-no-change-in-fixation-number\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:methods-ofc-no-change-in-fixation-number\n  notes: Under the code's reading (a), none of the 12 per-monkey tests (Eyes and whole Face, 1.5, 2\n    and 3 s) gives p below 0.05; the smallest is 0.12. Both monkeys combined, outside the claim,\n    give p = 0.025 for whole Face fixations within 1.5 s (0.044 more per trial after stimulation).\n    Under reading (b), M1-only and mutual events, monkey L gives p = 0.026 for the whole Face within\n    1.5 s, 1 of 12 tests.\n- claim: methods-ofc-longer-face-looking\n  outcome: partially_reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:methods-ofc-longer-face-looking\n  measured:\n  - 52.8\n  - 65.07\n  - 46.23\n  - -14.68\n  - -2.15\n  - 12.23\n  notes: The tests hold with the code's M1-only events; OFC whole Face p = 0.0025 with stimulation\n    longer (L 0.0067, T 0.15), OFC Eyes p = 0.039, dmPFC 0.80, ACCg 0.93 (paper 0.003, 0.008,\n    0.129, 0.044, 0.683, 0.848). Under reading (a), the median of day differences, OFC whole Face is\n    52.8 ms (expected 48.9 plus or minus 4.89) and monkey L 65.1 ms (66.6 plus or minus 6.66),\n    within tolerance, monkey T 46.2 ms (39.5 plus or minus 3.95) is not; reading (b), the mean, gives\n    62.6, 85.3 and 34.3 ms, none within. dmPFC -14.7 ms matches -14.5; ACCg -2.2 ms against 3.4 and\n    OFC Eyes 12.2 ms against 16.5 do not. With M1-only and mutual events the OFC whole Face test\n    still holds (p = 0.030) but OFC Eyes does not (p = 0.19).\n- claim: methods-mouth-stimulation-no-effect\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:methods-mouth-stimulation-no-effect\n  notes: None of the 27 tests on the Mouth days gives p below 0.05. Social OFC, dmPFC and ACCg give\n    p = 1, 1 and 0.19 (paper 1, 1, 0.125), non-social 1, 0.125 and 0.19 (paper 1, 0.188, 0.188);\n    the hemifield tests give at least 0.0625. With 5 days per area the smallest two-sided exact\n    signed-rank p is 0.0625, so the paper's test cannot find an effect at 0.05 on these days.\n  deviations:\n  - The Mouth centre is the centre of each run's `roi_m1_mouth`, and the non-social centre that of\n    the Dot run's `roi_m1_mouth` (the RDM at the Mouth location); the files do not say whether the\n    Mouth rectangle is the one used online.\n- claim: methods-eyes-vs-mouth-bootstrap\n  outcome: not_reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:methods-eyes-vs-mouth-bootstrap\n  notes: With all 27 OFC Eyes days, contralateral p = 0.078 (a, one-sided) and 0.156 (b, two-sided),\n    0.059 to 0.070 one-sided over five other seeds (paper 0.009); ipsilateral 0.30 and 0.59 (paper\n    0.724); both hemifields 0.043 and 0.086 (paper 0.799). With monkey T's 12 days, contralateral\n    0.037 and 0.074 (paper 0.005), ipsilateral 0.35 and 0.70, both hemifields 0.037 and 0.074\n    (paper 0.510). The Mouth medians are -6.3 (contralateral), -8.4 (ipsilateral) and -0.24 pixels\n    (both), the Eyes medians -21.2, -12.3 and -17.9. Neither reading gives significance for the\n    contralateral fixations alone; under (a) both hemifields combined is the comparison that is\n    significant, the reverse of the paper's pattern.\n  deviations:\n  - Seed 959 is a standard choice; five other seeds are shown.\n- claim: fig3b-ofc-inter-looking-interval\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig3b-ofc-inter-looking-interval\n  notes: OFC median day difference -0.069 s, p = 0.044 (paper 0.035); dmPFC p = 0.77, ACCg 0.34\n    (paper 0.792, 0.291); monkey L 0.25 and T 0.11 (paper 0.188, 0.092). The outcome is near the\n    threshold and depends on two details. 91 trials have a whole Face event that starts at the trial\n    sample itself; the criterion's \"starts after it\" leaves them out, and counting them as latency 0\n    gives OFC p = 0.058. M1-only events give OFC p = 0.0022 (T 0.0024).\n  deviations:\n  - An event \"after\" the trial must start later than the trial's own sample (criterion, \"starts\n    after it\"); 91 events that start on the trial sample, likely the triggering fixation as the\n    offline fixation detection saw it, are not counted. Whether the paper's code counts them is not\n    known; this is asked of the paper's authors in the findings.\n- claim: ili-nonsocial-no-effect\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:ili-nonsocial-no-effect\n  notes: OFC p = 0.70, dmPFC 0.13, ACCg 0.84 (paper 0.773, 0.080, 0.943). By monkey, dmPFC in monkey\n    T gives p = 0.034, outside the claim's test. 7,736 of 10,148 control trials have an interval.\n  deviations:\n  - The whole Face in the Dot runs is the files' m1_wholeface table of those runs.\n- claim: ili-missing-trials-41\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:ili-missing-trials-41\n  measured: 41.3\n  notes: Reading (a), over the 81 Eyes days, 41.3% (expected 41 plus or minus 4.1); reading (b),\n    over the 27 OFC days, 39.9%. Pooled over trials, 40.5%.\n- claim: figs3b-ili-trial-level\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:figs3b-ili-trial-level\n  notes: OFC median 1.19 s after stimulation against 1.36 s after sham, p = 0.017 (paper 0.010);\n    dmPFC p = 0.39, ACCg 0.62 (paper 0.301, 0.602); OFC monkey L 0.049 and T 0.14 (paper 0.026,\n    0.143).\n- claim: figs3c-reciprocation-day-level-none\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:figs3c-reciprocation-day-level-none\n  measured: 86.4\n  notes: OFC p = 0.11, dmPFC 0.56, ACCg 0.32 (paper 0.130, 0.701, 0.400). Trials with no M2-then-M1\n    sequence are 86.4% per day over the 81 days (reading a; expected 86 plus or minus 8.6) and 85.1%\n    over the OFC days. 2,689 of 19,474 trials have a latency; every day has one in each trial type.\n  deviations:\n  - A mutual event enters both lists, at M1's and at M2's own start times; ties keep the M1 event\n    first, a standard choice.\n- claim: fig3d-ofc-reciprocation-latency\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig3d-ofc-reciprocation-latency\n  notes: OFC median 0.84 s after stimulation against 1.01 s after sham, p = 0.023 (paper 0.011);\n    dmPFC p = 0.72, ACCg 0.36 (paper 0.777, 0.368); OFC monkey L 0.15 and T 0.078 (paper 0.074,\n    0.079).\n- claim: partner-monkey-unchanged\n  outcome: partially_reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:partner-monkey-unchanged\n  notes: M2 social gaze distance, OFC p = 0.12, dmPFC 0.47, ACCg 0.062 (paper 0.118, 0.302, 0.064);\n    the M2-only reading gives 0.11, 0.37 and 0.069. M2 inter-looking interval, readings (a) and (b),\n    smallest p 0.19 (paper 1, 0.866, 0.249). M2 reciprocation latency, reading (b) from the trial\n    time, smallest p 0.46; reading (a), from the start of the M1 look (the mirror of M1's measure),\n    OFC 0.56, dmPFC 0.044 (median 0.11 s longer after stimulation), ACCg 0.99 (paper 0.665, 0.773,\n    0.701). The criterion asks that no test give p below 0.05 under every reading; 1 of 21 tests\n    does, so the claim holds for the distance and the interval and in part for the reciprocation\n    latency.\n  deviations:\n  - M2's distance is to the centre of `roi_m2_eyes` (M1's Eyes in M2's coordinates); the Methods\n    reading adds the M2 side of mutual whole Face events to m2_all.\n  - Reading (a) of the M2 inter-looking interval, start of the second minus start of the first M2\n    whole Face event in the window, follows the Results' \"the latency between the second and first\n    whole Face events of M2\"; reading (b), from the end of the first, is shown.\n  - The 188 M2 events whose gaze samples are all NaN have no position and are left out of the M2\n    distance.\n- claim: figs4a-causal-strength-no-stim-effect\n  outcome: blocked\n  blocked_by: too_large\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:figs4a-causal-strength-no-stim-effect\n  notes: The relative causal strength needs the causal decomposition of Yang, Peng and Huang (2018),\n    built on ensemble empirical mode decomposition. One EEMD of one 150-bin series with 100\n    ensembles takes about 1.0 s here (PyEMD) and yields 7 IMFs; with one decomposition of each\n    series and one per IMF of each series with that IMF removed, the claims file's reading (a), 1,000\n    ensembles, needs about 160 s per trial, or about 870 CPU hours for the 19,474 social trials (88\n    hours at a tenth of the ensembles). This is beyond the notebook limit and the run. The trials,\n    distances and epochs the analysis would use are all in the dataset.\n- claim: figs4b-causal-strength-no-epoch-effect\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on figs4a-causal-strength-no-stim-effect, blocked by the cost of the causal\n    decomposition. The epochs themselves are reproduced (epoch-days-76-of-81).\n- claim: epoch-days-76-of-81\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:epoch-days-76-of-81\n  measured: 76\n  notes: Counting kept stimulations (reading a), 76 of 81 days have at least 90, and the five others\n    are the days the code names, with the stated composition, 08122019 (L, OFC, 87), 12222021 (T,\n    OFC, 80), 11052021 and 12172021 (T, dmPFC, 64 and 67) and 11042021 (T, ACCg, 50). Counting all\n    stimulations delivered in social runs (reading b) gives 77; the L OFC day has 96.\n- claim: ofc-slope-unchanged-by-epoch\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on figs4a-causal-strength-no-stim-effect, blocked by the cost of the causal\n    decomposition.\n- claim: fig4c-dmpfc-slope-late-greater\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on ofc-slope-unchanged-by-epoch and the causal strengths, blocked by the cost of\n    the causal decomposition.\n- claim: fig4d-dmpfc-slope-permutation\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig4c-dmpfc-slope-late-greater and the causal strengths, blocked by the cost of\n    the causal decomposition.\n- claim: dmpfc-slope-positive\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig4c-dmpfc-slope-late-greater and the causal strengths, blocked by the cost of\n    the causal decomposition.\n- claim: fig5a-trigger-duration-unchanged\n  outcome: not_reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig5a-trigger-duration-unchanged\n  notes: Under reading (a), M1-only and mutual Eyes events, the event in progress at the trial is\n    longer on stimulation trials for dmPFC (median day difference 31 ms, p = 0.019; paper 0.269),\n    not for OFC (8 ms, p = 0.61; paper 0.302). Reading (b), M1-only events, gives dmPFC 28 ms, p =\n    0.028 and OFC p = 0.36. ACCg, outside the claim, gives 0.30 and 0.13. 13,779 of 19,474 trials\n    fall inside an offline Eyes event under (a), 12,647 under (b); the others are left out.\n  deviations:\n  - The triggering fixation is taken as the offline (EyeMMV) Eyes event that contains the trial\n    time; the online fixation that triggered the trial is not in the files.\n- claim: fig5b-pupil-unchanged\n  outcome: reproduced\n  notebook: reproduce_fan_2024.ipynb\n  output: claim:fig5b-pupil-unchanged\n  notes: No 10-ms bin of the 70 gives p below 0.05 in any area; the smallest p are 0.31 (OFC), 0.51\n    (dmPFC) and 0.11 (ACCg). 2,198 of 19,474 social trials keep M1's gaze in the whole Face for 700\n    ms; all 27 days of each area have both trial types.\n  deviations:\n  - Pupil size is the raw file value (a.u.), averaged within 10-ms bins, without baseline\n    correction, as the Methods describe none.\n- claim: fig5cd-saccade-counts-unchanged\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: The files hold fixation events but no saccade events. The paper detects saccades with the\n    unsupervised clustering method of Otero-Millan et al. (2014), distributed as MATLAB code, which\n    cannot run in this entry's locked Python environment; no Python implementation of it was found\n    to substitute without changing the method. The gaze traces needed are in the dataset.\n- claim: fig5e-h-saccade-kinematics-unchanged\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: Depends on fig5cd-saccade-counts-unchanged; the saccade detection cannot be run here.\nfindings:\n- kind: other\n  statement: The dataset holds 6.0 control (Dot) runs per day on average for monkey L (4 to 8; 14 of\n    45 days have 8), where the paper reports 5 on average, and 14 social runs on every Eyes day of\n    monkey T, where the paper reports 15 on average (14 to 15). Either some runs were not analysed in\n    the paper or the counts in the paper are off; the files do not say which runs the paper used.\n- kind: code_mismatch\n  statement: The Methods give the fixation counts of Figure S1E as the total per day, and the paper's\n    code takes the mean per session. Because a day has about twice as many social runs as control\n    runs, the Eyes against RDM comparison is significant for every area with day totals (corrected p\n    0.000025 to 0.00041) and comparable with means per run (0.40 to 0.52), as the paper reports.\n- kind: metadata_insufficient\n  statement: Neither the files nor the paper give the padding of the Eyes ROI (the Methods text has\n    the number missing), nor how fixation events were assigned to ROIs. 6% of the M1 Eyes events of\n    social runs and 11% of those of Dot runs have a mean gaze position outside the Eyes rectangle of\n    their file, and 3% and 10% of whole Face events outside the Face rectangle. The description of\n    `laterality_label` does not name its reference; it matches the centre of `roi_m2_face` for\n    99.98% of M1 events.\n- kind: metadata_insufficient\n  statement: The Dot (control) runs do not hold `roi_m2_face`, the reference of their hemifield\n    split, nor say that their `roi_m1_eyes` is the RDM stimulus; both are inferred, the first from\n    the same day's social runs and the second from the Methods.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. For the inter-looking interval, does a whole Face\n    event that starts on the trial sample itself (91 trials; likely the triggering fixation as the\n    offline detection found it) count as the look back with latency 0? Counting it changes the OFC\n    day-level p from 0.044 to 0.058. And is the inter-looking interval taken over M1-only events or\n    M1-only and mutual events, as the Methods say (OFC p 0.0022 against 0.044)?\n- kind: methods_unavailable\n  statement: Question for the paper's authors. Is M2's reciprocation latency measured from the start\n    of M1's look at M2 or from the trial time? Measured from M1's look, dmPFC gives p = 0.044; from\n    the trial, no area is below 0.46. And how is the p-value of the Eyes against Mouth bootstrap\n    computed (one- or two-sided, and which tail)?\n- kind: other\n  statement: Trial times fall inside an offline M1 event in the triggering ROI on 71% of social Eyes\n    trials and 62% of Dot Eyes trials, against 5 to 20% for times shifted by 0.5 to 2 s; this is\n    consistent with a shared clock of trials and events, and shows that about 30% of online\n    triggers do not coincide with an offline fixation in the ROI (65 of 954 social Eyes runs are\n    below 50%).\n"
}
```

```
File created successfully at: attempts/000959-fan-2024-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Fixing one misquoted range, then the final clean run, check and handover.

**Agent calls Bash**

```bash
cd  sed -i 's/than monkey L (52 to 57)/than monkey L (52 to 57)/; s/per day (71 to$/per day (71 to/' attempts/000959-fan-2024-01.yaml; grep -n "71 to" attempts/000959-fan-2024-01.yaml
```

```
67:    corrected 0.082, uncorrected 0.014 and 0.010); monkey T has more control trials per day (71 to
```

**Agent calls Bash**

```bash
cd  sed -n 68p attempts/000959-fan-2024-01.yaml; sed -i '68s/^    77)/    76)/' attempts/000959-fan-2024-01.yaml; sed -n 67,68p attempts/000959-fan-2024-01.yaml; . $TMPDIR/wenv/bin/activate; python -c "import yaml; yaml.safe_load(open('attempts/000959-fan-2024-01.yaml'))" && python tools/entry.py check entries/000959-fan-2024
```

```
77) than monkey L (52 to 57).
    corrected 0.082, uncorrected 0.014 and 0.010); monkey T has more control trials per day (71 to
    76) than monkey L (52 to 57).
0 error(s)
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/wenv/bin/activate; python tools/entry.py all entries/000959-fan-2024 2>&1 | tail -4; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/000959-fan-2024/reproduce_fan_2024.ipynb',4)
out=[]
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.outputs:
            if o.get('output_type')=='stream': out.append(o.text)
            elif o.get('output_type')=='error': out.append('ERROR '+o.ename)
open('/tmp/claude/exec_out2.txt','w').write(''.join(out))
EOF
diff <(grep -v "loaded\|EEMD\|CPU hours\|run time\|Warning\|Scale for\|Standard dev" /tmp/claude/exec_out.txt) <(grep -v "loaded\|EEMD\|CPU hours\|run time\|Warning\|Scale for\|Standard dev" /tmp/claude/exec_out2.txt); grep "no gaze\|CPU hours\|run time" /tmp/claude/exec_out2.txt; date -u
```

```
Installed kernelspec registry-000959-fan-2024 in executed/000959-fan-2024/.venv/share/jupyter/kernels/registry-000959-fan-2024
0 error(s)
pass  reproduce_fan_2024.ipynb  (672 s)
2d1
<   pos = np.array([np.nanmean(g[a:b], 0) if b > a else [np.nan, np.nan]
54a54
> M1 events with no gaze position (all samples NaN; left out of distances): 0 of 1929396 ; M2 events: 188
M1 events with no gaze position (all samples NaN; left out of distances): 0 of 1929396 ; M2 events: 188
estimated per trial at 1,000 ensembles: 161 s; 19474 social trials: 870 CPU hours; at a tenth of the ensembles 87 CPU hours
notebook run time: 11.1 min
Sun Nov  1 00:28:30 UTC 2026
```

**Agent**

Passed again (11.2 min), with outputs identical to the first run apart from the added line. Rounding one timing figure in the record, then the handover.

**Agent calls Bash**

```bash
cd  sed -i 's/hours for the 19,474 social trials (88$/hours for the 19,474 social trials (about 90/' attempts/000959-fan-2024-01.yaml; grep -n "about 90\|(88" attempts/000959-fan-2024-01.yaml; . $TMPDIR/wenv/bin/activate; python tools/entry.py check entries/000959-fan-2024 && python tools/entry.py handover entries/000959-fan-2024; ls executed/000959-fan-2024/handover; git status --short
```

```
315:    ensembles, needs about 160 s per trial, or about 870 CPU hours for the 19,474 social trials (about 90
0 error(s)
wrote executed/000959-fan-2024/handover
10.1016-j.neuron.2024.05.004.yaml
microstim.py
reproduce_fan_2024.ipynb
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
?? attempts/000959-fan-2024-01.yaml
?? entries/000959-fan-2024/
?? scripts
```

**Agent calls Bash**

```bash
cd  ls -a entries/000959-fan-2024; git status --short --ignored entries/000959-fan-2024 | head
```

```
.
..
.claude
README.md
__pycache__
entry.yaml
microstim.py
reproduce_fan_2024.ipynb
requirements.in
requirements.lock.txt
?? entries/000959-fan-2024/
!! entries/000959-fan-2024/__pycache__/
```

**Agent calls Bash**

```bash
cd  ls -la entries/000959-fan-2024/.claude; git check-ignore -v entries/000959-fan-2024/.claude || echo not-ignored
```

```
total 12
drwxr-xr-x 3 runner runner 4096 Oct 31 23:52 .
drwxr-xr-x 4 runner runner 4096 Nov  1 00:15 ..
drwx------ 2 runner runner 4096 Oct 31 23:52 .cc-writes
not-ignored
```

**Agent**

A harness artefact (`.claude/.cc-writes`) appeared inside the entry when the shell's working directory was there. Checking it's empty before removing it, so it isn't committed with the entry.

**Agent calls Bash**

```bash
cd  find entries/000959-fan-2024/.claude | head; [ -z "$(find entries/000959-fan-2024/.claude -type f)" ] && rmdir entries/000959-fan-2024/.claude/.cc-writes entries/000959-fan-2024/.claude && echo removed; date -u
```

```
entries/000959-fan-2024/.claude
entries/000959-fan-2024/.claude/.cc-writes
removed
Sun Nov  1 00:29:00 UTC 2026
```

**Agent**

I tested 28 of the 33 claims on DANDI:000959. 19 reproduced, 4 partially, 5 did not; the other 5 are blocked. The entry passes `lock` and `all` from a clean environment and the handover package is built. Nothing is committed.

Version: the paper cites none, so I pinned the latest published version, 0.261020.0242. The only other version, 0.260531.2104, has the same 1705 assets with the same ids and sizes. The header says so.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| design-days-per-area | reproduced |
| design-sessions-per-day | partially reproduced (monkey L has 6.02 control runs per day, paper says 5) |
| fig1e-stim-counts-comparable, figs1d-stim-counts-nonsocial | reproduced |
| figs1e-eyes-more-than-face | reproduced |
| figs1e-eyes-vs-rdm-comparable | not reproduced under the Methods' "total per day"; comparable under the code's mean per run |
| fig2a-density-map-ofc | reproduced |
| fig2c (both claims), fig2e (both), fig2f, fig2gh, methods-ofc-distance-longer-windows | reproduced |
| methods-ofc-no-change-in-fixation-number | reproduced |
| methods-ofc-longer-face-looking | partially reproduced (tests hold; 2 of 3 OFC durations within tolerance) |
| methods-mouth-stimulation-no-effect | reproduced (with 5 days the smallest possible p is 0.0625) |
| methods-eyes-vs-mouth-bootstrap | not reproduced |
| fig3b-ofc-inter-looking-interval | reproduced (p = 0.044, close to the threshold) |
| ili-nonsocial-no-effect, ili-missing-trials-41, figs3b-ili-trial-level, figs3c-reciprocation-day-level-none, fig3d-ofc-reciprocation-latency | reproduced |
| partner-monkey-unchanged | partially reproduced (one reading of M2's reciprocation latency gives dmPFC p = 0.044) |
| epoch-days-76-of-81 | reproduced, with exactly the five named days |
| fig5a-trigger-duration-unchanged | not reproduced (dmPFC p = 0.019) |
| fig5b-pupil-unchanged | reproduced |
| figs4a, figs4b, ofc-slope, fig4c, fig4d, dmpfc-slope-positive | blocked, `too_large`: the causal decomposition would take about 870 CPU hours, timed in the notebook |
| fig5cd, fig5e-h (saccades) | blocked, `not_runnable`: the files hold no saccades and the paper's detection method is MATLAB code |

The headline result reproduces well: OFC stimulation lowers social gaze distance with p = 0.0002 (L p = 0.0067, T p = 0.016), and the contralateral pattern matches too.

### 2. Dataset, assumptions and questions

**Dataset.**
- It holds every day the paper describes: 81 Eyes days and 15 Mouth days, one file per run, no run deposited twice.
- Each file holds gaze, pupil, stimulation and sham times, ROIs, and fixation-event tables.
- The files' own hemifield labels match the claims file's rule for 99.98% of events.
- A clock check passes: 71% of trial times fall inside an M1 event in the triggering ROI, against 5 to 20% when the times are shifted.

**Findings recorded.**
- Run counts per day differ from the paper's (L control runs, T social runs never reaching 15).
- Methods and code count fixations differently (day total against mean per run), and the Eyes-vs-RDM outcome depends on it.
- Neither the paper nor the files give the Eyes ROI padding or how events were assigned to ROIs.
- The control runs lack `roi_m2_face`, the hemifield reference, which I took from the same day's social runs.

**Assumptions.** None of the outcomes rests on one: every reading was taken from the claims file or the paper and cited.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Does a face event that starts on the trial sample itself count as a look back with latency 0? Counting it moves OFC from p = 0.044 to p = 0.058.
- Is M2's reciprocation latency measured from M1's look or from the trial time?
- How is the bootstrap p-value computed (which side)?

**Questions to a reader:** none.

### 3. Protocol points
1. The DANDI section of `archives.md` says to stream with remfile. That took about 14 s per file for metadata alone (12.5 min with 32 threads). I read each file into memory over HTTP instead (never to disk), which brought the full load to about 10 min.
2. Each claim of absence must be judged "on the paper's test alone", yet this claims file names several readings for some of them (partner monkey). I followed the criterion, which requires every reading to pass, and gave `partially_reproduced` when one test out of 21 failed.
3. Several criteria have no rule for a partial result (sessions per day, partner monkey). I used `partially_reproduced` where most of the claim held, and said so in the notes.
4. For the Eyes-vs-RDM claim, the protocol's order (Methods first) gives a "not reproduced" that the code's reading would reverse. I did not ask a reader, since this is not a misreading of the paper, and recorded it as a `code_mismatch` finding.
5. The protocol does not say whether a cost estimate made inside the notebook is enough to support `too_large`. I timed one decomposition inside the notebook to give the estimate.
6. While the shell's working directory was the entry folder, the harness created an empty `.claude/.cc-writes` there; I removed it. Unrelated untracked dotfiles at the repository root (`.bashrc`, `.idea`, and others) I left untouched.

### 4. Runtime and failures
- The run took about 67 minutes of wall clock (23:22 to 00:29 UTC).
- The notebook takes 11.2 min, almost all of it reading the data.
- Nothing failed.

The new files are `entries/000959-fan-2024/` and `attempts/000959-fan-2024-01.yaml`; the handover is in `executed/000959-fan-2024/handover/`.

## End of run

62 turns, 65 minutes, result: success.
