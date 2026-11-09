# crcns-fcx-2 · author · run 42521152357

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8eb7e607-aa9b-4fd6-8803-473fa4a165f3/tool-results/b0jywu24d.txt

Preview (first 2KB):
Sun Nov  8 20:41:56 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8eb7e607-aa9b-4fd6-8803-473fa4a165f3/tool-results/b0jywu24d.txt"
}
```

```
1	Sun Nov  8 20:41:56 UTC 2026
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
[... 633 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; wc -l docs/design.md docs/archives.md
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
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/crcns-fcx-2/ paper/ entries/001453-fouke-2025/ claims/001453/; cat claims/crcns-fcx-2/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-fcx-2/10.1371-journal.pbio.2004274.yaml"
}
```

```
1	# Claims for Johnson, Adams, Solbakk, Endestad, Larsson, Ivanovic, Meling, Lin & Knight (2018),
2	# PLoS Biology 16, e2004274, "Dynamic frontotemporal systems process space and time in working
3	# memory", doi:10.1371/journal.pbio.2004274, on CRCNS data set fcx-2 (doi:10.6080/K0VX0DQD).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
6	#
7	# Text read: the version of record, open access, PMC5895055, as supplied under paper/ (Europe PMC
8	# full-text XML, flattened): Introduction, Results, Discussion, Materials and methods, the legends
9	# of Figures 1 to 8 and the captions of the supporting information. No PDF was supplied. The
10	# supporting information is S1 and S2 Fig (legends read) and S1 to S4 Table (DOCX files: group
11	# mixed-effects model outputs with degrees of freedom). Only the captions of the four tables were
12	# supplied; their contents were not read. Every claim below rests on a p-value the main text
13	# prints, so no claim needs the tables, but the full model outputs (degrees of freedom, F values
14	# of the PAC models) they hold were not available. Values shown only in figures (the percentages
15	# of Fig 4B, the grand means of Fig 8A, the per-subject PSI of Fig 3B) were not read.
16	#
17	# Code. The Data Availability statement says the "custom-built MATLAB codes" are deposited with
18	# the data on CRCNS (doi:10.6080/K0VX0DQD). The data descriptor says they are in the data set's
19	# analysis_scripts directory (one <metric>_compute script per analysis, with subfunctions, using
20	# FieldTrip). Being among the data set's files, they were not read in this run. Where a criterion
[... 838 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/fcx-2.data-description.txt; grep -n -A60 "## CRCNS" docs/archives.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=fcx-2/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s,lm in re.findall(r'<Key>(.*?)</Key><LastModified>(.*?)</LastModified>.*?<Size>(\d+)</Size>',t): print(k,lm,s)
print(t[-300:])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live; for f in checksums.md5 filelist.txt docs/summary_file.csv docs/summary_channel_analysis.csv; do echo "== $f"; curl -s $B/$f; echo; done; curl -s $B/analysis_scripts.tar.gz | tar tzvf -
```

```
== checksums.md5
8b5b07094a3a31e8bb4828afcdffd2f2  analysis_scripts.tar.gz
5eb078815470c8d1b70b06d8f2be5300  data_indiv/s10.tar.gz
0bbbcce3cc2738bc7ce5545b27843d4c  data_indiv/s1.tar.gz
5ead31d89d1ae4a50adae20054bb6572  data_indiv/s2.tar.gz
740991d34257dabc1fdd8a467f1e80a2  data_indiv/s3.tar.gz
306d554f9e9ec77a35b68879f301f6b1  data_indiv/s4.tar.gz
66673b1504648aff5ea1f2e0bea6fcdd  data_indiv/s5.tar.gz
68608a2237469bc285b928298b1e8f3f  data_indiv/s6.tar.gz
639d8e97e026f9b8dea08610c51af00e  data_indiv/s7.tar.gz
6aa467667c0fec9566f49fd19c8461e8  data_indiv/s8.tar.gz
bfd6d72c7663db18db4f0fe90cea63c7  data_indiv/s9.tar.gz
05de3d369c076737b8554a80fda2c992  docs/crcns_fcx-2_data_description.docx
d1072c4bd9daa9dcbee22e4a2f31a6dc  docs/crcns_fcx-2_data_description.pdf
79adb25db44e195ad952359ed43d9a3a  docs/summary_channel_analysis.csv
6d214de444bf222cee1c3291b6191a6f  docs/summary_file.csv
310fdc4b0696e05b772f11dad39acd3a  filelist.txt

== filelist.txt
# CRCNS.org 'fcx-2' dataset files
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/analysis_scripts.tar.gz | tar xzf - && cd analysis_scripts && for f in *.m subfunctions/*.m; do echo "=== $f"; cat $f; done
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8eb7e607-aa9b-4fd6-8803-473fa4a165f3/tool-results/bg92nngdj.txt"
}
```

```
1	=== cspsi_compute.m
2	% Compute cross-spectral phase slope index. Requires fieldtrip toolbox.
3	%
4	% Key:
5	% subid = 's1' (required)
6	% elecs = {'LOF1','LOF2','LHH1'} (optional)
7	%
8	% E. L. Johnson, PhD
9	% Copyright (c) 2017
10	% UC Berkeley
11	% [removed: an e-mail address]
12	
13	function [] = cspsi_compute(subid, elecs)
14	% plv_compute('s1', {'LOF1','LOF2','LHH1'});
15	
16	% INPUT PATH TO DATA DIRECTORY
17	path = %%INSERT%%
18	
19	dataDir = [path '/Johnson_PB_2018/data_indiv/'];
20	saveDir = [path '/Johnson_PB_2018/cspsi/'];
[... 1215 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "import fsspec,scipy,h5py,numpy,statsmodels;print(scipy.__version__)" ; time python3 - <<'EOF'
import fsspec, tarfile, time
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/data_indiv/s8.tar.gz"
t=time.time()
with fsspec.open(url, block_size=2**22) as f:
    tf=tarfile.open(fileobj=f, mode="r|gz")
    for m in tf:
        print(m.name, m.size, round(time.time()-t,1), flush=True)
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec,scipy,h5py,numpy,statsmodels;print(scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'fsspec'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'fsspec'

real	0m0.034s
user	0m0.028s
sys	0m0.005s
```

**Agent calls Bash**

```bash
cat entries/001453-fouke-2025/requirements.in entries/001453-fouke-2025/entry.yaml; cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests scipy h5py numpy statsmodels pandas matplotlib && python -c "import fsspec; print('ok')"
```

```
dandi
h5py
matplotlib
numpy
pandas
remfile
scipy
statsmodels
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
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && timeout 900 python - <<'EOF'
import fsspec, tarfile, time
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/data_indiv/s8.tar.gz"
t=time.time()
with fsspec.open(url, block_size=2**22) as f:
    tf=tarfile.open(fileobj=f, mode="r|gz")
    for m in tf:
        print(m.name, m.size, round(time.time()-t,1), flush=True)
EOF
```

```
s8 0 1.4
s8/s8_MNI_grid.csv 49364 1.4
s8/data_primary.mat 347028413 1.4
s8/data_derived.mat 210369492 34.0
s8/summary_file_trial.csv 4730 53.5
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && timeout 900 python - <<'EOF'
import requests, tarfile, time
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/data_indiv/s8.tar.gz"
t=time.time()
r=requests.get(url, stream=True); r.raw.decode_content=False
tf=tarfile.open(fileobj=r.raw, mode="r|gz", bufsize=2**20)
for m in tf:
    print(m.name, m.size, round(time.time()-t,1), flush=True)
EOF
```

```
s8 0 0.8
s8/s8_MNI_grid.csv 49364 0.8
s8/data_primary.mat 347028413 0.8
s8/data_derived.mat 210369492 7.8
s8/summary_file_trial.csv 4730 12.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && timeout 900 python - <<'EOF'
import requests, tarfile, time, io, resource
import scipy.io as sio, numpy as np, h5py
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/data_indiv/s8.tar.gz"
r=requests.get(url, stream=True)
tf=tarfile.open(fileobj=r.raw, mode="r|gz", bufsize=2**20)
for m in tf:
    if m.name.endswith('data_derived.mat'):
        b=tf.extractfile(m).read(); print(b[:120])
    if m.name.endswith('.csv'):
        txt=tf.extractfile(m).read().decode(); print(m.name, txt[:600])
bio=io.BytesIO(b)
try:
    d=sio.loadmat(bio, squeeze_me=True, struct_as_record=False)
    for k,v in d.items():
        if k.startswith('__'): continue
        print(k, type(v), v._fieldnames if hasattr(v,'_fieldnames') else '')
        print(' label', v.label[:5], len(v.label), 'fs', v.fsample, 'ntr', len(v.trial), v.trial[0].shape, v.time[0][[0,-1]], v.trialinfo[:3])
        print(' hdr', v.hdr._fieldnames if hasattr(v.hdr,'_fieldnames') else v.hdr)
        for fn in v._fieldnames: print('  field',fn)
except NotImplementedError as e:
    print('v73'); f=h5py.File(bio); print(list(f.keys()))
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
```

```
s8/s8_MNI_grid.csv #vtkpxElectrodeMultiGridSource File
#Description
patient
#Comment
no additional comment
#Number of Grids
 12 
#- - - - - - - - - - - - - - - - - - -
# Electrode Grid 0
- - - - - - - - - - - - - - - - - - -
#vtkpxElectrodeGridSource File v2
#Description
CR
#Dimensions
 1 10
#Electrode Spacing
 10.0000 10.0000
#Electrode Type
0
#Radius 
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && timeout 900 python - <<'EOF'
import requests, tarfile, io, h5py, numpy as np
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/data_indiv/s8.tar.gz"
r=requests.get(url, stream=True)
tf=tarfile.open(fileobj=r.raw, mode="r|gz", bufsize=2**20)
for m in tf:
    if m.name.endswith('data_derived.mat'):
        b=tf.extractfile(m).read(); break
open('s8_derived.mat','wb').write(b)  # dev only, scratch
EOF
python - <<'EOF'
import h5py, numpy as np
f=h5py.File('/tmp/claude-1001/s8_derived.mat' if False else __import__('os').environ['TMPDIR']+'/s8_derived.mat')
def s(ref): return ''.join(map(chr, f[ref][()].ravel()))
for k in ['data_pre','data_encmain','data_proc']:
    g=f[k]; print(k, list(g.keys()))
    for fn in g.keys():
        print('  ',fn, g[fn].shape, g[fn].dtype)
    lab=[s(r) for r in g['label'][()].ravel()]; print(lab)
    tr=g['trial'][()].ravel(); tm=g['time'][()].ravel()
    print(len(tr), f[tr[0]].shape, f[tm[0]][()].ravel()[[0,1,-1]], f[tm[0]].shape)
    print(g['trialinfo'][()].T[:4], g['fsample'][()])
    print('hdr', list(g['hdr'].keys()) if isinstance(g['hdr'],h5py.Group) else g['hdr'])
    if 'cfg' in g: print(list(g['cfg'].keys())[:50])
EOF
```

```
Exit code 1
data_pre ['cfg', 'fsample', 'hdr', 'label', 'sampleinfo', 'time', 'trial', 'trialinfo']
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
AttributeError: 'Group' object has no attribute 'shape'
```

**Agent calls Bash**

```bash
rm -f $TMPDIR/s8_derived.mat; cd $TMPDIR && . dev/bin/activate && timeout 900 python - <<'EOF'
import requests, tarfile, io, h5py, numpy as np
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/data_indiv/s8.tar.gz"
r=requests.get(url, stream=True)
tf=tarfile.open(fileobj=r.raw, mode="r|gz", bufsize=2**20)
for m in tf:
    if m.name.endswith('data_derived.mat'):
        b=tf.extractfile(m).read(); break
f=h5py.File(io.BytesIO(b))
def s(ref): return ''.join(map(chr, f[ref][()].ravel()))
def walk(g,ind=''):
    for k in g.keys():
        o=g[k]
        if isinstance(o,h5py.Group): print(ind+k,'/'); walk(o,ind+'  ') if ind.count(' ')<4 else None
        else: print(ind+k, o.shape, o.dtype, o.attrs.get('MATLAB_class'))
for k in ['data_pre','data_encmain','data_proc']:
    g=f[k]; print('=====',k)
    for fn in ['fsample','label','sampleinfo','time','trial','trialinfo']:
        print('  ',fn, g[fn].shape, g[fn].dtype)
    walk(g['hdr'],'   hdr.')
    lab=[s(r) for r in g['label'][()].ravel()]; print(lab)
    tr=g['trial'][()].ravel(); tm=g['time'][()].ravel()
    print(len(tr), f[tr[0]].shape, f[tm[0]][()].ravel()[[0,1,-1]], f[tm[0]].shape, f[tm[5]].shape)
    print(g['trialinfo'][()].T[:4], g['fsample'][()], g['sampleinfo'][()].T[:3])
    print('cfg keys', list(g['cfg'].keys()))
EOF
```

```
===== data_pre
   fsample (1, 1) float64
   label (1, 43) object
   sampleinfo (2, 90) float64
   time (90, 1) object
   trial (90, 1) object
   trialinfo (6, 90) float64
   hdr.Fs (1, 1) float64 b'double'
   hdr.label (1, 43) object b'cell'
   hdr.nChans (1, 1) float64 b'double'
   hdr.nSamples (1, 1) float64 b'double'
   hdr.nSamplesPre (1, 1) float64 b'double'
   hdr.nTrials (1, 1) float64 b'double'
['TOL_02', 'TOL_03', 'TOL_04', 'TOL_05', 'AL_09', 'AL_10', 'AL_11', 'AL_12', 'CL_02', 'CL_03', 'CL_04', 'CL_10', 'CL_11', 'CL_12', 'BL_10', 'BL_11', 'BL_12', 'FOAL_04', 'FOAL_05', 'FOPL_04', 'FOPL_05', 'POAL_06', 'POAL_07', 'POPL_02', 'POPL_03', 'POPL_04', 'POPL_05', 'WL_03', 'WL_04', 'WL_05', 'AR_01', 'AR_09', 'AR_10', 'AR_11', 'AR_12', 'CR_09', 'CR_10', 'BR_03', 'BR_04', 'BR_05', 'BR_06', 'BR_09', 'BR_10']
90 (2305, 43) [-1.5        -1.49804688  3.        ] (2305, 1) (2305, 1)
[[1.000e+00 1.000e+00 1.000e+00 1.000e+00 9.000e+02 9.060e+02]
 [2.000e+00 1.000e+00 2.000e+00 3.000e+00 1.150e+03 7.240e+02]
 [3.000e+00 1.000e+00 2.000e+00 3.000e+00 1.150e+03 2.052e+03]
 [4.000e+00 1.000e+00 2.000e+00 3.000e+00 1.150e+03 7.370e+02]] [[512.]] [[ 4873.  7177.]
 [ 8468. 10772.]
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; wc -c paper/10.1371-journal.pbio.2004274.txt; grep -n "Materials and methods" paper/10.1371-journal.pbio.2004274.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '119,200p' paper/10.1371-journal.pbio.2004274.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pandas as pd, io, requests
t=requests.get("https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/docs/summary_channel_analysis.csv").text
df=pd.read_csv(io.StringIO(t),header=None,skiprows=2)
df[0]=df[0].ffill()
cols={1:('MTL','L'),2:('MTL','R'),3:('PFC','L'),4:('PFC','R'),5:('OFC','L'),6:('OFC','R')}
rows=[]
for _,r in df.iterrows():
    for c,(reg,h) in cols.items():
        if isinstance(r[c],str) and r[c].strip(): rows.append((r[0],reg,h,r[c].strip()))
ch=pd.DataFrame(rows,columns=['sub','region','hemi','label'])
print(ch.groupby('region').size(), len(ch))
print(ch.groupby(['sub','region','hemi']).size().unstack([1,2]).fillna(0).astype(int))
EOF
```

```
Sun Nov  8 20:48:17 UTC 2026
region
MTL     36
OFC    102
PFC    116
dtype: int64 254
region MTL OFC PFC MTL OFC PFC
hemi     R   R   R   L   L   L
sub                           
S1       2   5   8   0   0   0
S10      0   2   0   5  45   0
S2       0   3  11   7   0   4
S3       2   0   2   0   1   2
S4       1   2   7   4   0   5
S5       0   0   0   2  16  10
S6       0   0   0   1  19  28
S7       0   4   6   2   1  11
S8       4   0   0   1   0   4
S9       0   0  12   5   4   6
Shell cwd was reset to
```

**Agent calls Bash**

```bash
ls entries/001453-fouke-2025/; head -c 3000 entries/001453-fouke-2025/omr.py; python3 -c "
import json;nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:1500]); print('----')
"
```

```
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
  33a5c297ff4ab6ff49f6bdd96139e9fdd867025c (the Methods give none of these): Savitzky-Golay
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && timeout 900 python - <<'EOF'
import requests, tarfile, io, h5py, numpy as np
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/data_indiv/s2.tar.gz"
r=requests.get(url, stream=True)
tf=tarfile.open(fileobj=r.raw, mode="r|gz", bufsize=2**20)
for m in tf:
    print(m.name, m.size)
    if m.name.endswith('data_derived.mat'):
        b=tf.extractfile(m).read()
f=h5py.File(io.BytesIO(b))
def s(ref): return ''.join(map(chr, f[ref][()].ravel()))
g=f['data_encmain']
print([s(r) for r in g['label'][()].ravel()])
print(g['fsample'][()], g['trialinfo'].shape, f[g['trial'][0,0]].shape, f[g['trial'][0,0]].dtype)
print(np.unique(g['trialinfo'][()][1],return_counts=True))
x=f[g['trial'][0,0]][()]; print(x[:5,:3], np.abs(x[:20]).max(), np.abs(x).max())
EOF
```

```
Sun Nov  8 20:49:43 UTC 2026
s2 0
s2/data_primary.mat 490708543
s2/data_derived.mat 371704202
s2/summary_file_trial.csv 4777
s2/s2_MNI_grid.csv 37858
['RAH14', 'RAH15', 'RAH16', 'RC2', 'RC3', 'RC4', 'RC8', 'RC9', 'RC10', 'RC11', 'RC12', 'ROF2', 'ROF3', 'ROF4', 'ROF11', 'ROF12', 'ROF13', 'ROF14', 'ROF15', 'ROF16', 'LAH5', 'LAH6', 'LAH7', 'LAH8', 'LAH9', 'LAH10', 'LAH11', 'LIN10', 'LIN14', 'LIN15', 'LIN16']
[[1000.]] (6, 113) (4503, 31) float64
(array([0., 1.]), array([  4, 109]))
[[ 3.68206449e+00 -2.34315794e+01  5.84429586e-01]
 [ 2.17457409e+00 -2.40356471e+01  3.47444596e-01]
 [ 5.52006206e-01 -2.60804622e+01  3.21789015e-01]
 [-6.24781543e-01 -2.89313745e+01  2.91510254e-01]
 [-1.32161930e+00 -3.13848463e+01 -1.12008867e-02]] 48.74521022997197 88.68146225099387
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "content": "\"\"\"Loading and measures for CRCNS fcx-2 (Johnson et al. 2018, PLoS Biology 16, e2004274).\n\nThe data set holds, per subject, a tar.gz with the filtered continuous data (data_primary.mat),\nthe preprocessed bipolar data (data_derived.mat, MATLAB 7.3, FieldTrip structures data_pre,\ndata_encmain and data_proc), a per-trial table (summary_file_trial.csv) and electrode\ncoordinates. The tar files are streamed from the public S3 bucket and read member by member in\nmemory; nothing is written to disk. Only the derived data of the analysed channels\n(docs/summary_channel_analysis.csv) are kept.\n\nWhere the parameters come from. \"Code\" is the analysis code deposited with the data\n(analysis_scripts.tar.gz in the data set, scripts dated 2018-02-22 to 2018-04-03); \"Methods\" is\nthe paper's Materials and methods; M1 to M10 are the shared method details of the claims file.\n\n- Segment windows (M1): encoding and precue [0, 1.5] s of data_encmain, precue delay\n  [0.6, 1.5] s of data_encmain, postcue delay [0.3, 1.2] s of data_proc, baseline [0.65, 0.85] s\n  of data_pre. Code: power_compute.m, psi_compute.m, cspsi_compute.m (\"cfgt.latency\"). The\n  precue delay is M1 reading (a), which the code settles.\n- Filter bank (M2): the 24 band edges of power_compute.m (`BANDS`), the last band dropped for the\n  512 Hz subjects s8 and s9 (code). Two-pass FIR filters designed as FieldTrip's default for\n  `bpfilttype = 'fir'` (fir1 with a Hamming window, order 3 * fix(fs / low edge), capped at a\n  third of the padded length); this design is FieldTrip's, which the code calls. Segments are zero\n  padded to 7.5 s (Methods, Spectral decomposition; code `padding = 7.5`). Analytic amplitude by\n  the Hilbert transform; power is its square (Methods).\n- Baseline z (M3): bootstrap of the pooled baseline power, r = number of correct trials, 1000\n  draws without replacement (code zbaseline.m, `randsample`), z = (power - mean) / SD of the\n  bootstrap means. The z is affine in power per channel and frequency, so the trial mean of z\n  equals the z of the trial mean (M3 readings (a) and (b) give the same number).\n- Down-sampling to 50 ms: polyphase resampling with a Kaiser window (beta 5, 100 * max(p, q)\n  taps each side), which is what MATLAB's resample(x, p, q, 100) in resamplemtx.m does.\n- Cluster permutation (M4): FieldTrip's montecarlo cluster test as configured in\n  erp_compute.m and power_compute.m: independent-samples t (two-tailed, cluster threshold at\n  t for p = 0.025 each tail) or F (one-tailed, threshold at p = 0.05), cluster statistic the sum\n  of t or F, 1000 permutations of the condition labels, cluster p doubled for the two-tailed t\n  test (`correcttail = 'prob'`), significant at p < 0.05. Clusters never join electrodes\n  (`neighbours = []`). The null is the maximum cluster sum per permutation either over all of a\n  subject's electrodes tested together (what the code does, as it passes all channels at once)\n  or per electrode (Methods, \"clustered per electrode\"); both are returned.\n- ERPs: 30 Hz low-pass two-pass FIR, order 3 * fix(fs / 30), segments zero padded to 7.5 s\n  (Methods, ERPs; code erp_compute.m).\n- ERP subtraction for phase measures: the mean over correct trials is subtracted from each\n  correct trial (code subtracterp.m with ncond = 1; for PAC per condition, ncond = 3, Methods,\n  PAC paragraph 2).\n- Theta spectra for PSI (M5): the code (psi_compute.m) runs FieldTrip mtmfft with a Hanning\n  taper over the whole 900 ms window, zero padded to 4 s, at 3 to 7 Hz; FieldTrip ignores\n  `t_ftimwin` for mtmfft. The Methods describe sliding 3-cycle windows, which cannot be placed\n  inside a 900 ms segment at 3 Hz (a 1 s window), so the code's single window is the main\n  reading and sliding windows that run into the zero padding are a variant (`theta_fourier`).\n- PSI (Nolte et al. 2008, ref. 30 of the paper): coherency from the cross-spectrum averaged over\n  trials (and windows), PSI = Im(sum_f conj(C_f) C_(f+1)), positive when the first signal leads.\n  Null: the frequencies of the second signal shuffled, 1000 times; z = (PSI - mean) / SD\n  (Methods, PSI paragraph 2). The code's own form (`psianalysis.m`: the trial mean of per-trial\n  PSI, z-scored against frequency-shuffled trial-mean coherency) is a variant (`psi_code`).\n- Cross-spectral PSI (M6): theta Fourier coefficients of the amplitude envelopes of the 17 bands\n  centred at 9.5 to 152.5 Hz (16 for s8 and s9) of the code (cspsi_compute.m), z per band, then\n  averaged over bands.\n- PAC (M9): circular-linear correlation (code circ_corrcl.m) across the trials of a condition at\n  each time point and amplitude band, 100 surrogates, z = (PAC - mean) / SD. Surrogate reading\n  (a): the amplitudes permuted across trials, a new permutation per band (code pacanalysis.m,\n  `ampvec(randperm(...), :)`); reading (b): the amplitude bands shuffled within each trial.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport tarfile\nimport time\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport requests\nfrom scipy import ndimage, signal, stats\n\nBASE = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live\"\nSUBJECTS = [f\"s{i}\" for i in range(1, 11)]\n\nBANDS = np.array([[1, 3], [1.5, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 10], [7, 12], [9, 14],\n                  [10, 17], [12, 20], [15, 24], [17, 28], [20, 33], [24, 40], [29, 48], [34, 57],\n                  [40, 67], [47, 81], [57, 96], [67, 114], [80, 135], [94, 162], [113, 192]])\nCENTRES = BANDS.mean(axis=1)\nAMP_BANDS = np.arange(7, 24)        # 7-12 ... 113-192 Hz, centres 9.5 to 152.5 Hz\nPLV_BANDS = np.arange(0, 11)        # 1-3 ... 12-20 Hz (code plv_compute.m)\nPEAK_BANDS = np.arange(1, 7)        # 1.5-4 ... 6-10 Hz, the 6 ranges of M8\nTHETA_FREQS = np.arange(3, 8)       # 3 to 7 Hz (M5)\n\nWIN = {\"enc\": (\"encmain\", 0.0, 1.5), \"pre\": (\"encmain\", 0.6, 1.5), \"post\": (\"proc\", 0.3, 1.2),\n       \"base\": (\"pre\", 0.65, 0.85)}\nPAD_S = 7.5\n\n\n# ---------------------------------------------------------------- loading\n\ndef read_channel_table():\n    \"\"\"docs/summary_channel_analysis.csv as one row per analysed channel.\"\"\"\n    text = requests.get(f\"{BASE}/docs/summary_channel_analysis.csv\", timeout=60).text\n    df = pd.read_csv(io.StringIO(text), header=None, skiprows=2)\n    df[0] = df[0].ffill()\n    cols = {1: (\"MTL\", \"L\"), 2: (\"MTL\", \"R\"), 3: (\"PFC\", \"L\"), 4: (\"PFC\", \"R\"),\n            5: (\"OFC\", \"L\"), 6: (\"OFC\", \"R\")}\n    rows = []\n    for _, r in df.iterrows():\n        for c, (reg, hemi) in cols.items():\n            if isinstance(r[c], str) and r[c].strip():\n                rows.append({\"subject\": r[0].lower(), \"region\": reg, \"hemi\": hemi, \"label\": r[c].strip()})\n    return pd.DataFrame(rows)\n\n\ndef read_summary_file():\n    text = requests.get(f\"{BASE}/docs/summary_file.csv\", timeout=60).text\n    names = [\"subject\", \"age\", \"sex\", \"acc_identity\", \"acc_spatial\", \"acc_temporal\",\n             \"rt_identity\", \"rt_spatial\", \"rt_temporal\"]\n    df = pd.read_csv(io.StringIO(text), header=None, names=names)\n    df[\"subject\"] = df.subject.str.lower()\n    return df\n\n\nTRIAL_COLS = [\"trial\", \"accuracy\", \"trial_type\", \"condition\", \"jitter\", \"rt\",\n              \"pre_start\", \"enc_start\", \"post_start\"]\n\n\ndef _h5str(f, ref):\n    return \"\".join(map(chr, f[ref][()].ravel()))\n\n\ndef load_subject(sid, channels):\n    \"\"\"Stream one subject's tar.gz and return its trial table and the analysed channels' data.\n\n    `channels` is the list of analysed labels for this subject. Returns a dict with the trial\n    table, the derived structures' labels, fsample, trialinfo, sampleinfo and time axes, and per\n    segment an array (trials, channels, samples) in float32.\n    \"\"\"\n    t0 = time.time()\n    url = f\"{BASE}/data_indiv/{sid}.tar.gz\"\n    out = {\"subject\": sid, \"members\": {}}\n    with requests.get(url, stream=True, timeout=120) as resp:\n        resp.raise_for_status()\n        tf = tarfile.open(fileobj=resp.raw, mode=\"r|gz\", bufsize=2 ** 20)\n        for m in tf:\n            if not m.isfile():\n                continue\n            out[\"members\"][m.name] = m.size\n            if m.name.endswith(\"summary_file_trial.csv\"):\n                out[\"trials\"] = pd.read_csv(tf.extractfile(m), header=None, names=TRIAL_COLS)\n            elif m.name.endswith(\"data_derived.mat\"):\n                raw = tf.extractfile(m).read()\n                out.update(_read_derived(raw, channels))\n                del raw\n    out[\"load_s\"] = time.time() - t0\n    return out\n\n\ndef _read_derived(raw, channels):\n    res = {}\n    with h5py.File(io.BytesIO(raw), \"r\") as f:\n        for seg in [\"pre\", \"encmain\", \"proc\"]:\n            g = f[f\"data_{seg}\"]\n            labels = [_h5str(f, r) for r in g[\"label\"][()].ravel()]\n            idx = [labels.index(c) for c in channels]\n            trefs = g[\"trial\"][()].ravel()\n            tm = f[g[\"time\"][()].ravel()[0]][()].ravel()\n            x = np.stack([f[r][()][:, idx].T for r in trefs]).astype(np.float32)\n            res[seg] = {\n                \"labels\": labels, \"fs\": float(g[\"fsample\"][()].ravel()[0]),\n                \"trialinfo\": g[\"trialinfo\"][()].T, \"sampleinfo\": g[\"sampleinfo\"][()].T,\n                \"time\": tm, \"x\": x,\n                \"hdr_fs\": float(g[\"hdr\"][\"Fs\"][()].ravel()[0]),\n                \"same_time\": all(np.array_equal(f[r][()].ravel(), tm) for r in g[\"time\"][()].ravel()),\n            }\n            # clock check: absolute sample of time 0, assuming sampleinfo[0] is time 0\n            res[seg][\"first_rows\"] = {i: f[trefs[i]][()][:, idx].T.astype(np.float32) for i in range(min(3, len(trefs)))}\n    return {\"seg\": res}\n\n\n# ---------------------------------------------------------------- spectral tools\n\ndef fir_order(fs, low, npad):\n    n = 3 * int(np.fix(fs / low))\n    return int(min(n, np.floor((npad - 1) / 3)))\n\n\ndef _twopass_gain(b, nfft):\n    h = np.fft.fft(b, nfft)\n    return np.abs(h) ** 2\n\n\ndef bandpass_gain(lo, hi, fs, nfft, npad):\n    n = fir_order(fs, lo, npad)\n    b = signal.firwin(n + 1, [lo, hi], pass_zero=False, fs=fs)\n    return _twopass_gain(b, nfft)\n\n\ndef lowpass_gain(hi, fs, nfft, npad):\n    n = 3 * int(np.fix(fs / hi))\n    n = int(min(n, np.floor((npad - 1) / 3)))\n    b = signal.firwin(n + 1, hi, fs=fs)\n    return _twopass_gain(b, nfft)\n\n\nclass Padder:\n    \"\"\"Zero pad a segment (..., T) to `PAD_S` s, centred, and FFT it.\"\"\"\n\n    def __init__(self, T, fs, pad_s=PAD_S):\n        self.T, self.fs = T, fs\n        self.npad = max(int(round(pad_s * fs)), T)\n        self.left = (self.npad - T) // 2\n        self.nfft = signal.next_fast_len(self.npad + 2 * 3 * int(fs) + 2)\n        f = np.fft.fftfreq(self.nfft, 1 / fs)\n        self.hil = np.where(f > 0, 2.0, 0.0)\n        self.hil[0] = 1.0\n        if self.nfft % 2 == 0:\n            self.hil[self.nfft // 2] = 1.0\n\n    def fft(self, x):\n        buf = np.zeros(x.shape[:-1] + (self.nfft,), dtype=np.float64)\n        buf[..., self.left:self.left + self.T] = x\n        return np.fft.fft(buf, axis=-1)\n\n    def back(self, X, analytic):\n        y = np.fft.ifft(X * self.hil if analytic else X, axis=-1)\n        y = y[..., self.left:self.left + self.T]\n        return y if analytic else y.real\n\n\ndef window_index(time_axis, t0, t1):\n    \"\"\"Samples of `time_axis` from t0 to t1, as ft_selectdata picks them (nearest samples).\"\"\"\n    i0 = int(np.argmin(np.abs(time_axis - t0)))\n    i1 = int(np.argmin(np.abs(time_axis - t1)))\n    return np.arange(i0, i1 + 1)\n\n\ndef hilbert_bands(x, fs, bands, sel, analytic=True, pad=None):\n    \"\"\"Analytic signal of x (trials, ch, T) in each band, kept at samples `sel`.\n\n    Returns complex64 (trials, ch, nband, len(sel)).\n    \"\"\"\n    pad = pad or Padder(x.shape[-1], fs)\n    X = pad.fft(x)\n    out = np.empty(x.shape[:2] + (len(bands), len(sel)), dtype=np.complex64)\n    for k, (lo, hi) in enumerate(bands):\n        g = bandpass_gain(lo, hi, fs, pad.nfft, pad.npad)\n        y = pad.back(X * g, analytic=True)\n        out[:, :, k, :] = y[..., sel]\n    return out\n\n\ndef resample_20hz(x, fs):\n    \"\"\"Down-sample the last axis to 20 Hz as MATLAB resample(x, p, q, 100) (resamplemtx.m).\"\"\"\n    from fractions import Fraction\n    fr = Fraction(20, int(round(fs))).limit_denominator(1000)\n    p, q = fr.numerator, fr.denominator\n    m = max(p, q)\n    h = signal.firwin(2 * 100 * m + 1, 1.0 / m, window=(\"kaiser\", 5.0)) * p\n    n_new = int(np.floor((x.shape[-1] - 1) / fs * 20)) + 1\n    if n_new % 2 == 0:\n        n_new += 1\n    y = signal.resample_poly(x, p, q, axis=-1, window=h)\n    return y[..., :n_new]\n\n\ndef baseline_bootstrap(base_pow, ntrials, rng, nperm=1000):\n    \"\"\"Mean and SD of the bootstrap distribution of baseline means (zbaseline.m).\n\n    base_pow: (trials, ch, band, T). Returns two arrays (ch, band).\n    \"\"\"\n    _, nch, nb, _ = base_pow.shape\n    pool = base_pow.transpose(1, 2, 0, 3).reshape(nch, nb, -1)\n    npool = pool.shape[-1]\n    dist = np.empty((nch, nb, nperm))\n    for z in range(nperm):\n        pick = rng.choice(npool, size=ntrials, replace=False)\n        dist[:, :, z] = pool[:, :, pick].mean(axis=-1)\n    return dist.mean(axis=-1), dist.std(axis=-1, ddof=1)\n\n\n# ---------------------------------------------------------------- cluster permutation test\n\ndef _stat(X, groups, kind):\n    \"\"\"t (two groups) or F (k groups) for each column of X (n, M); groups is (P, n) int labels.\"\"\"\n    P = groups.shape[0]\n    labels = np.unique(groups[0])\n    sums, sq, ns = [], [], []\n    X2 = X * X\n    for g in labels:\n        G = (groups == g).astype(X.dtype)\n        sums.append(G @ X)\n        sq.append(G @ X2)\n        ns.append(G.sum(axis=1)[:, None])\n    if kind == \"t\":\n        m1, m2 = sums[0] / ns[0], sums[1] / ns[1]\n        v1 = (sq[0] - ns[0] * m1 ** 2) / (ns[0] - 1)\n        v2 = (sq[1] - ns[1] * m2 ** 2) / (ns[1] - 1)\n        sp = ((ns[0] - 1) * v1 + (ns[1] - 1) * v2) / (ns[0] + ns[1] - 2)\n        return (m1 - m2) / np.sqrt(sp * (1 / ns[0] + 1 / ns[1]))\n    n = X.shape[0]\n    grand = X.sum(axis=0) / n\n    ssb = sum(ns[k] * (sums[k] / ns[k] - grand) ** 2 for k in range(len(labels)))\n    ssw = sum(sq[k] - sums[k] ** 2 / ns[k] for k in range(len(labels)))\n    k = len(labels)\n    return (ssb / (k - 1)) / (ssw / (n - k))\n\n\n_STRUCT = None\n\n\ndef _cluster_sums(stat, thr, sign, shape):\n    \"\"\"Cluster sums per electrode for one map. stat: (ch, *dims). Returns list per channel of sums.\"\"\"\n    mask = (stat * sign) > thr\n    nd = len(shape)\n    struct = np.zeros((3,) * (nd + 1), dtype=bool)\n    c = (1,) * (nd + 1)\n    struct[c] = True\n    for ax in range(1, nd + 1):\n        for d in (0, 2):\n            idx = list(c)\n            idx[ax] = d\n            struct[tuple(idx)] = True\n    lab, nlab = ndimage.label(mask, structure=struct)\n    if nlab == 0:\n        return np.zeros(0), np.zeros(0, dtype=int)\n    sums = np.bincount(lab.ravel(), weights=(stat * sign).ravel(), minlength=nlab + 1)[1:]\n    chan_of = ndimage.labeled_comprehension(np.broadcast_to(np.arange(stat.shape[0]).reshape((-1,) + (1,) * nd), stat.shape),\n                                            lab, np.arange(1, nlab + 1), np.min, int, -1)\n    return sums, chan_of\n\n\ndef cluster_test(data, labels, kind, rng, nperm=1000, chunk=50):\n    \"\"\"FieldTrip-style cluster permutation test, independently per electrode (no neighbours).\n\n    data: (trials, ch, *dims). labels: (trials,) condition codes.\n    Returns a DataFrame with, per electrode, the smallest cluster p under the subject-wide max\n    null (`p_subject`, what the code does) and under the per-electrode max null (`p_electrode`),\n    and the number of observed clusters.\n    \"\"\"\n    n, nch = data.shape[:2]\n    dims = data.shape[2:]\n    X = data.reshape(n, -1).astype(np.float64)\n    lab = np.asarray(labels)\n    ulab = np.unique(lab)\n    codes = np.searchsorted(ulab, lab)\n    if kind == \"t\":\n        df = n - 2\n        thr = stats.t.ppf(1 - 0.025, df)\n        signs = (1, -1)\n    else:\n        thr = stats.f.ppf(1 - 0.05, len(ulab) - 1, n - len(ulab))\n        signs = (1,)\n    obs = _stat(X, codes[None, :], kind)[0].reshape((nch,) + dims)\n    null_subj = {s: np.zeros(nperm) for s in signs}\n    null_chan = {s: np.zeros((nperm, nch)) for s in signs}\n    done = 0\n    while done < nperm:\n        P = min(chunk, nperm - done)\n        perms = np.stack([rng.permutation(codes) for _ in range(P)])\n        st = _stat(X, perms, kind).reshape((P, nch) + dims)\n        for i in range(P):\n            for s in signs:\n                sums, chan = _cluster_sums(st[i], thr, s, dims)\n                if len(sums):\n                    null_subj[s][done + i] = sums.max()\n                    mx = np.zeros(nch)\n                    np.maximum.at(mx, chan, sums)\n                    null_chan[s][done + i] = mx\n        done += P\n    rows = []\n    factor = 2.0 if kind == \"t\" else 1.0\n    for c in range(nch):\n        best_s, best_e, ncl = 1.0, 1.0, 0\n        for s in signs:\n            sums, chan = _cluster_sums(obs, thr, s, dims)\n            for v in sums[chan == c]:\n                ncl += 1\n                ps = (np.sum(null_subj[s] >= v) + 1) / (nperm + 1) * factor\n                pe = (np.sum(null_chan[s][:, c] >= v) + 1) / (nperm + 1) * factor\n                best_s, best_e = min(best_s, ps), min(best_e, pe)\n        rows.append({\"ch\": c, \"p_subject\": min(best_s, 1.0), \"p_electrode\": min(best_e, 1.0), \"n_clusters\": ncl})\n    return pd.DataFrame(rows)\n\n\n# ---------------------------------------------------------------- theta Fourier and PSI\n\ndef hanning_matlab(n):\n    k = np.arange(1, n + 1)\n    return 0.5 * (1 - np.cos(2 * np.pi * k / (n + 1)))\n\n\ndef theta_fourier(x, fs, mode=\"mtmfft\", step_s=0.05):\n    \"\"\"Fourier coefficients at 3 to 7 Hz of x (trials, ch, T), demeaned per trial.\n\n    mode \"mtmfft\": one Hanning window over the segment, zero padded to 4 s (code).\n    mode \"sliding\": 3-cycle Hanning windows centred every `step_s` over the segment, the data\n    zero padded to 4 s so that a window may run into the padding (Methods' sliding windows).\n    Returns complex (trials, ch, 5, nwin).\n    \"\"\"\n    x = x - x.mean(axis=-1, keepdims=True)\n    T = x.shape[-1]\n    if mode == \"mtmfft\":\n        nfft = int(round(4 * fs))\n        tap = hanning_matlab(T)\n        X = np.fft.rfft(x * tap, n=nfft, axis=-1)\n        fr = np.fft.rfftfreq(nfft, 1 / fs)\n        idx = [int(np.argmin(np.abs(fr - f))) for f in THETA_FREQS]\n        return X[..., idx][..., None]\n    npad = int(round(4 * fs))\n    left = (npad - T) // 2\n    buf = np.zeros(x.shape[:-1] + (npad,))\n    buf[..., left:left + T] = x\n    centres = left + np.arange(0, T, int(round(step_s * fs)))\n    out = []\n    for f in THETA_FREQS:\n        L = int(round(3 / f * fs))\n        tap = hanning_matlab(L)\n        kern = tap * np.exp(-2j * np.pi * f * np.arange(L) / fs)\n        cols = []\n        for c in centres:\n            a = c - L // 2\n            cols.append(buf[..., a:a + L] @ kern)\n        out.append(np.stack(cols, axis=-1))\n    return np.stack(out, axis=-2)\n\n\ndef cross_spectra(A, B):\n    \"\"\"Trial- and window-averaged cross-spectra between frequencies.\n\n    A: (trials, na, 5, w), B: (trials, nb, 5, w). Returns S (na, nb, 5, 5) with\n    S[a, b, f, g] = mean over trials and windows of A[a, f] conj(B[b, g]), and the powers\n    PA (na, 5), PB (nb, 5).\n    \"\"\"\n    S = np.einsum(\"rafw,rbgw->abfg\", A, np.conj(B)) / (A.shape[0] * A.shape[-1])\n    PA = (np.abs(A) ** 2).mean(axis=(0, 3))\n    PB = (np.abs(B) ** 2).mean(axis=(0, 3))\n    return S, PA, PB\n\n\ndef psi_z(S, PA, PB, rng, nperm=1000):\n    \"\"\"Nolte PSI and its z against shuffles of the second signal's frequencies.\n\n    S: (..., 5, 5) cross-spectra between frequencies; PA (..., 5), PB (..., 5).\n    Returns raw PSI (...) and z (...).\n    \"\"\"\n    nf = S.shape[-1]\n    diag = np.arange(nf)\n\n    def psi_for(perm):\n        C = S[..., diag, perm] / np.sqrt(PA * PB[..., perm])\n        return np.imag(np.conj(C[..., :-1]) * C[..., 1:]).sum(axis=-1)\n\n    raw = psi_for(diag)\n    null = np.stack([psi_for(rng.permutation(nf)) for _ in range(nperm)], axis=-1)\n    return raw, (raw - null.mean(axis=-1)) / null.std(axis=-1, ddof=1)\n\n\ndef psi_code(A, B, rng, nperm=1000):\n    \"\"\"The deposited code's form of PSI (psianalysis.m), with the cross-spectrum conjugated.\n\n    Observed: the trial mean of per-trial PSI from per-trial normalised cross-spectra. Null:\n    trial-mean normalised cross-spectra with both frequency axes shuffled independently. A and B\n    are (trials, n, 5, 1) for the pairs to compute (A[:, i] with B[:, i]).\n    \"\"\"\n    cs = A[..., 0] * np.conj(B[..., 0])                      # (trials, n, 5)\n    pp = cs / np.abs(cs)\n    per_trial = np.imag(np.conj(pp[..., :-1]) * pp[..., 1:]).sum(axis=-1)\n    obs = per_trial.mean(axis=0)\n    ppm = pp.mean(axis=0)                                    # (n, 5)\n    nf = ppm.shape[-1]\n    null = np.stack([np.imag(np.conj(ppm[:, rng.permutation(nf)]) * ppm[:, rng.permutation(nf)]).sum(axis=-1)\n                     for _ in range(nperm)], axis=-1)\n    return obs, (obs - null.mean(axis=-1)) / null.std(axis=-1, ddof=1)\n\n\n# ---------------------------------------------------------------- PAC\n\ndef circ_corrcl_trials(phase, amp):\n    \"\"\"Circular-linear correlation across trials (axis 0), as circ_corrcl.m.\n\n    phase: (trials, T); amp: (P, trials, F, T). Returns (P, F, T).\n    \"\"\"\n    n = phase.shape[0]\n\n    def zs(v, axis):\n        v = v - v.mean(axis=axis, keepdims=True)\n        return v / np.sqrt((v * v).sum(axis=axis, keepdims=True))\n\n    s, c = zs(np.sin(phase), 0), zs(np.cos(phase), 0)\n    rcs = (s * c).sum(axis=0)                               # (T,)\n    za = zs(amp, 1)\n    rxs = np.einsum(\"prft,rt->pft\", za, s)\n    rxc = np.einsum(\"prft,rt->pft\", za, c)\n    rho2 = (rxc ** 2 + rxs ** 2 - 2 * rxc * rxs * rcs) / (1 - rcs ** 2)\n    return np.sqrt(np.clip(rho2, 0, None))\n\n\ndef pac_z(phase, amp, rng, reading=\"a\", nsurr=100, chunk=25):\n    \"\"\"PAC z per amplitude band and time. phase (trials, T); amp (trials, F, T).\"\"\"\n    n, F, T = amp.shape\n    obs = circ_corrcl_trials(phase, amp[None])[0]\n    surr = np.empty((nsurr, F, T), dtype=np.float32)\n    for a in range(0, nsurr, chunk):\n        P = min(chunk, nsurr - a)\n        if reading == \"a\":\n            # one trial permutation per surrogate and band\n            perm = np.stack([np.stack([rng.permutation(n) for _ in range(F)], axis=1) for _ in range(P)])  # (P, n, F)\n            sh = amp[perm, np.arange(F)[None, None, :], :]\n        else:\n            # the amplitude bands shuffled within each trial\n            perm = np.stack([np.stack([rng.permutation(F) for _ in range(n)]) for _ in range(P)])  # (P, n, F)\n            sh = amp[np.arange(n)[None, :, None], perm, :]\n        surr[a:a + P] = circ_corrcl_trials(phase, sh)\n    return (obs - surr.mean(axis=0)) / surr.std(axis=0, ddof=1)\n\n\n# ---------------------------------------------------------------- balanced split-plot F tests\n\ndef within_unit_anova(Y, groups=None):\n    \"\"\"F tests of the within-unit effects of a balanced factorial table, per unit.\n\n    Y: (units, a, b, c) with factors in that order (condition, frequency, time). With random\n    intercepts for unit (and subject) and a balanced design, a linear mixed model's F tests of\n    the within-unit effects equal these (the unit intercepts absorb all between-unit variance).\n    `groups` (units,) of 0/1 adds a between-unit factor (direction): its interactions with the\n    within effects are tested here (sum-to-zero coding, type III), its main effect separately.\n    Returns a DataFrame of effect, df, F, p, and the residual df.\n    \"\"\"\n    U = Y.shape[0]\n    dims = Y.shape[1:]\n    letters = \"abc\"[: len(dims)]\n    Yc = Y - Y.mean(axis=tuple(range(1, Y.ndim)), keepdims=True)\n    # projections onto effect subspaces by inclusion-exclusion of marginal means\n    from itertools import combinations\n    effects = []\n    for k in range(1, len(dims) + 1):\n        effects += list(combinations(range(len(dims)), k))\n\n    def marg(Z, keep):\n        axes = tuple(i + 1 for i in range(len(dims)) if i not in keep)\n        return Z.mean(axis=axes, keepdims=True) if axes else Z\n\n    proj = {}\n    for e in effects:\n        p = np.zeros_like(Yc)\n        for k in range(0, len(e) + 1):\n            for sub in combinations(e, k):\n                sgn = (-1) ** (len(e) - k)\n                p = p + sgn * np.broadcast_to(marg(Yc, sub), Yc.shape)\n        proj[e] = p\n    ncell = int(np.prod(dims))\n    rows = []\n    if groups is None:\n        res_ss, res_df = 0.0, 0\n        for e in effects:\n            m = proj[e].mean(axis=0)\n            res_ss += ((proj[e] - m) ** 2).sum()\n            res_df += (U - 1) * int(np.prod([dims[i] - 1 for i in e]))\n        for e in effects:\n            df = int(np.prod([dims[i] - 1 for i in e]))\n            ss = U * (proj[e].mean(axis=0) ** 2).sum()\n            F = (ss / df) / (res_ss / res_df)\n            rows.append({\"effect\": e, \"df\": df, \"F\": F, \"p\": stats.f.sf(F, df, res_df)})\n        return pd.DataFrame(rows), res_df\n    g = np.asarray(groups)\n    n1, n2 = (g == 0).sum(), (g == 1).sum()\n    vf = (1 / n1 + 1 / n2) / 4\n    res_ss, res_df = 0.0, 0\n    for e in effects:\n        m1, m2 = proj[e][g == 0].mean(axis=0), proj[e][g == 1].mean(axis=0)\n        res_ss += ((proj[e][g == 0] - m1) ** 2).sum() + ((proj[e][g == 1] - m2) ** 2).sum()\n        res_df += (U - 2) * int(np.prod([dims[i] - 1 for i in e]))\n    for e in effects:\n        df = int(np.prod([dims[i] - 1 for i in e]))\n        m1, m2 = proj[e][g == 0].mean(axis=0), proj[e][g == 1].mean(axis=0)\n        for name, c in [(e, (m1 + m2) / 2), ((\"D\",) + e, (m1 - m2) / 2)]:\n            ss = (c ** 2).sum() / vf\n            F = (ss / df) / (res_ss / res_df)\n            rows.append({\"effect\": name, \"df\": df, \"F\": F, \"p\": stats.f.sf(F, df, res_df)})\n    return pd.DataFrame(rows), res_df\n"
}
```

```
File created successfully at: entries/crcns-fcx-2-johnson-2018/fcx2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-2-johnson-2018 && python3 - <<'EOF'
p='fcx2.py'; s=open(p).read()
old=s[s.index('    lab, nlab = ndimage.label(mask, structure=struct)'):s.index('    return sums, chan_of\n')]
new='''    lab, nlab = ndimage.label(mask, structure=struct)
    if nlab == 0:
        return np.zeros(0), np.zeros(0, dtype=int)
    sums = np.bincount(lab.ravel(), weights=(stat * sign).ravel(), minlength=nlab + 1)[1:]
    chan_of = np.array([sl[0].start for sl in ndimage.find_objects(lab)])
'''
s=s.replace(old,new)
s=s.replace('''            # clock check: absolute sample of time 0, assuming sampleinfo[0] is time 0
            res[seg]["first_rows"] = {i: f[trefs[i]][()][:, idx].T.astype(np.float32) for i in range(min(3, len(trefs)))}
''','')
old2=s[s.index('    rows = []\n    factor = 2.0'):s.index('    return pd.DataFrame(rows)\n\n\n# ----')]
new2='''    rows = []
    factor = 2.0 if kind == "t" else 1.0
    best_s, best_e, ncl = np.ones(nch), np.ones(nch), np.zeros(nch, dtype=int)
    for s in signs:
        sums, chan = _cluster_sums(obs, thr, s, dims)
        for v, c in zip(sums, chan):
            ncl[c] += 1
            ps = (np.sum(null_subj[s] >= v) + 1) / (nperm + 1) * factor
            pe = (np.sum(null_chan[s][:, c] >= v) + 1) / (nperm + 1) * factor
            best_s[c], best_e[c] = min(best_s[c], ps), min(best_e[c], pe)
    for c in range(nch):
        rows.append({"ch": c, "p_subject": min(best_s[c], 1.0), "p_electrode": min(best_e[c], 1.0),
                     "n_clusters": int(ncl[c])})
'''
s=s.replace(old2,new2)
open(p,'w').write(s)
EOF
grep -n "first_rows\|labeled_comprehension" fcx2.py
```

```
(Bash completed with no output)
```

**Agent**

Now a dev test on s8: loading, clock check, power, cluster test timing.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cd entries/crcns-fcx-2-johnson-2018 && timeout 1200 python - <<'EOF'
import time, resource, numpy as np, pandas as pd
import fcx2
ch=fcx2.read_channel_table()
t=time.time()
sub=fcx2.load_subject('s8', ch[ch.subject=='s8'].label.tolist())
print('load', time.time()-t, sub['members'])
tr=sub['trials']; print(tr.head(3)); print(len(tr))
for seg,d in sub['seg'].items():
    print(seg, d['fs'], d['hdr_fs'], d['x'].shape, d['time'][[0,-1]], len(d['time']), d['same_time'], d['sampleinfo'][:2])
    print('  labels in derived', len(d['labels']))
# clock: compare overlap of pre and encmain using sampleinfo[0] as time 0 vs time -1.5
pre, enc, proc = sub['seg']['pre'], sub['seg']['encmain'], sub['seg']['proc']
fs=pre['fs']
for hyp in ['t0','tstart']:
    diffs=[]
    for i in range(5):
        def absidx(d):
            s0=d['sampleinfo'][i,0]
            return s0 + (np.round(d['time']*fs).astype(int) if hyp=='t0' else np.arange(len(d['time'])))
        a, b = absidx(pre), absidx(enc)
        common, ia, ib = np.intersect1d(a, b, return_indices=True)
        diffs.append((len(common), float(np.max(np.abs(pre['x'][i][:, ia]-enc['x'][i][:, ib]))) if len(common) else None))
    print(hyp, diffs)
ti=sub['seg']['pre']['trialinfo'][:,0].astype(int)
T=tr.set_index('trial').loc[ti]
print('pre s0 - pre_start', np.unique(pre['sampleinfo'][:,0]-T.pre_start.values))
print('enc s0 - enc_start', np.unique(enc['sampleinfo'][:,0]-T.enc_start.values))
print('proc s0 - post_start', np.unique(proc['sampleinfo'][:,0]-T.post_start.values))
print('trialinfo matches table', np.array_equal(pre['trialinfo'][:,1:6], T[['accuracy','trial_type','condition','jitter','rt']].values))
print('mem GB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
Sun Nov  8 20:52:03 UTC 2026
load 14.044270753860474 {'s8/s8_MNI_grid.csv': 49364, 's8/data_primary.mat': 347028413, 's8/data_derived.mat': 210369492, 's8/summary_file_trial.csv': 4730}
   trial  accuracy  trial_type  ...  pre_start  enc_start  post_start
0      1         1           1  ...       4822       5796        6973
1      2         1           2  ...       8417       9396       10701
2      3         1           2  ...      11672      12647       13952

[3 rows x 9 columns]
120
pre 512.0 512.0 (90, 9, 2305) [-1.5  3. ] 2305 True [[ 4873.  7177.]
 [ 8468. 10772.]]
  labels in derived 43
encmain 512.0 512.0 (90, 9, 2304) [-1.5         2.99804688] 2304 True [[ 5796.  8099.]
 [ 9396. 11699.]]
  labels in derived 43
proc 512.0 512.0 (90, 9, 2305) [-1.5  3. ] 2305 True [[ 6819.  9123.]
 [10547. 12851.]]
  labels in derived 43
t0 [(1382, 0.0), (1377, 0.0), (1381, 0.0), (1390, 0.0), (1398, 0.0)]
tstart [(1382, 0.0), (1377, 0.0), (1381, 0.0), (1390, 0.0), (1398, 0.0)]
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> fcx2.py <<'EOF'


# ---------------------------------------------------------------- per-subject analysis

def seed_for(name, sid):
    """A fixed seed per analysis and subject, so each claim's numbers have their own generator."""
    return int.from_bytes(f"{name}|{sid}".encode(), "little") % (2 ** 32)


def _filter_chunks(x, fs, sel, bands, out_kind, chunk=6):
    """Band-filtered Hilbert outputs of x (trials, ch, T) at samples `sel`, channel chunks.

    out_kind: "power" (amplitude squared), "abs", "angle" or "complex". Returns float32 or
    complex64 (trials, ch, nband, len(sel)).
    """
    pad = Padder(x.shape[-1], fs)
    dtype = np.complex64 if out_kind == "complex" else np.float32
    out = np.empty(x.shape[:2] + (len(bands), len(sel)), dtype=dtype)
    gains = [bandpass_gain(lo, hi, fs, pad.nfft, pad.npad) for lo, hi in bands]
    for c0 in range(0, x.shape[1], chunk):
        X = pad.fft(x[:, c0:c0 + chunk].astype(np.float64))
        for k, g in enumerate(gains):
            y = pad.back(X * g, analytic=True)[..., sel]
            if out_kind == "power":
                y = np.abs(y) ** 2
            elif out_kind == "abs":
                y = np.abs(y)
            elif out_kind == "angle":
                y = np.angle(y)
            out[:, c0:c0 + chunk, k, :] = y
    return out


def lowpass_erp(x, fs, sel, hi=30.0, chunk=8):
    pad = Padder(x.shape[-1], fs)
    g = lowpass_gain(hi, fs, pad.nfft, pad.npad)
    out = np.empty(x.shape[:2] + (len(sel),), dtype=np.float32)
    for c0 in range(0, x.shape[1], chunk):
        X = pad.fft(x[:, c0:c0 + chunk].astype(np.float64))
        out[:, c0:c0 + chunk] = pad.back(X * g, analytic=False)[..., sel]
    return out


def segment(sub, name):
    segname, t0, t1 = WIN[name]
    d = sub["seg"][segname]
    return d, window_index(d["time"], t0, t1)


def n_amp_bands(fs):
    return len(AMP_BANDS) - (1 if fs < 600 else 0)
EOF
date -u
```

```
Sun Nov  8 20:53:27 UTC 2026
```

**Agent calls Bash**

```bash
cat >> fcx2.py <<'EOF'


def analyse_subject(sub, chans, nperm_cluster=1000, pac=True, pac_readings=("a", "b"), log=print):
    """Every per-subject measure the claims use, from one subject's loaded data.

    chans: the subject's rows of the channel table (region, hemi, label), in the order of the
    loaded arrays. Returns a dict of compact results; the raw arrays are not kept.
    """
    sid = sub["subject"]
    res = {"subject": sid, "timing": {}}
    T0 = time.time()
    pre, enc, proc = (sub["seg"][k] for k in ("pre", "encmain", "proc"))
    fs = enc["fs"]
    ti = enc["trialinfo"]
    correct = ti[:, 1] == 1
    res["trialinfo"] = ti
    regions = chans.region.to_numpy()
    hemis = chans.hemi.to_numpy()
    labels = chans.label.tolist()
    nb_all = len(BANDS) - (1 if fs < 600 else 0)
    bands = BANDS[:nb_all]

    xs = {k: sub["seg"][s]["x"][correct] for k, s in (("pre", "pre"), ("enc", "encmain"), ("proc", "proc"))}
    tic = ti[correct]

    # ---- ERPs (erp_compute.m): 30 Hz low-pass, baseline from the trial mean of [0.65, 0.85] s
    _, bsel = segment(sub, "base")
    _, esel = segment(sub, "enc")
    _, psel = segment(sub, "post")
    base = lowpass_erp(xs["pre"], fs, bsel).mean(axis=(0, 2))
    erp_enc = lowpass_erp(xs["enc"], fs, esel) - base[None, :, None]
    erp_post = lowpass_erp(xs["proc"], fs, psel) - base[None, :, None]
    rng = np.random.default_rng(seed_for("erp-no-condition-difference", sid))
    res["erp_enc"] = cluster_test(erp_enc[:, :, None, :], tic[:, 2], "t", rng, nperm_cluster)
    res["erp_post"] = cluster_test(erp_post[:, :, None, :], tic[:, 3], "F", rng, nperm_cluster)
    res["erp_mean"] = {"enc": erp_enc.mean(axis=0), "post": erp_post.mean(axis=0)}
    del erp_enc, erp_post
    res["timing"]["erp"] = time.time() - T0

    # ---- power (power_compute.m): Hilbert power, bootstrap baseline z, 50 ms
    rng = np.random.default_rng(seed_for("power", sid))
    bpow = _filter_chunks(xs["pre"], fs, bsel, bands, "power")
    bmean, bsd = baseline_bootstrap(bpow, int(correct.sum()), rng)
    del bpow
    zs = {}
    for name, x, sel in (("enc", xs["enc"], esel), ("post", xs["proc"], psel)):
        p = _filter_chunks(x, fs, sel, bands, "power")
        z = (p - bmean[None, :, :, None]) / bsd[None, :, :, None]
        del p
        zs[name] = resample_20hz(z, fs).astype(np.float32)
        if name == "enc":
            res["enc_time_mean_z"] = z.mean(axis=(0, 3))          # (ch, band), trials and time
        del z
    res["power_z_mean"] = {k: v.mean(axis=0) for k, v in zs.items()}  # (ch, band, t20)
    res["timing"]["power"] = time.time() - T0
    rng = np.random.default_rng(seed_for("power-condition-exclusions", sid))
    res["pow_enc"] = cluster_test(zs["enc"], tic[:, 2], "t", rng, nperm_cluster)
    res["pow_post"] = cluster_test(zs["post"], tic[:, 3], "F", rng, nperm_cluster)
    del zs
    res["timing"]["power_test"] = time.time() - T0
    excl = (np.minimum(res["pow_enc"].p_subject, res["pow_post"].p_subject) < 0.05).to_numpy()
    res["excluded"] = excl
    keep = ~excl

    # ---- individual theta peak (M8), reading (a): all kept analysed electrodes
    pk = res["enc_time_mean_z"][keep][:, PEAK_BANDS].mean(axis=0)
    res["peak_curve_all"] = pk
    res["peak_band_all"] = int(PEAK_BANDS[np.argmax(pk)])

    # ---- phase measures on ERP-subtracted delay data (subtracterp.m, ncond = 1)
    xe = {k: v - v.mean(axis=0, keepdims=True) for k, v in (("enc", xs["enc"]), ("proc", xs["proc"]))}
    _, pre_sel = segment(sub, "pre")
    wins = {"pre": (xe["enc"], pre_sel), "post": (xe["proc"], psel)}

    mtl = np.where((regions == "MTL") & keep)[0]
    pairs = {"MTL-MTL": [], "MTL-PFC": [], "MTL-OFC": []}
    for a in mtl:
        for b in np.where(keep & (hemis == hemis[a]))[0]:
            if regions[b] == "MTL" and b > a:
                pairs["MTL-MTL"].append((a, b))
            elif regions[b] in ("PFC", "OFC"):
                pairs[f"MTL-{regions[b]}"].append((a, b))
    res["pairs"] = pairs

    # PLV (plv_compute.m bands 1-3 ... 12-20 Hz)
    plv = {}
    for w, (x, sel) in wins.items():
        A = _filter_chunks(x, fs, sel, BANDS[PLV_BANDS], "complex")
        U = A / np.abs(A)
        out = {}
        for g, pl in pairs.items():
            vals = {"implv": [], "pli": [], "code": []}
            for a, b in pl:
                d = U[:, a] * np.conj(U[:, b])                   # (trials, band, T)
                vals["implv"].append(np.abs(np.imag(d.mean(axis=0))).mean(axis=-1))
                vals["pli"].append(np.abs(np.sign(np.imag(d)).mean(axis=0)).mean(axis=-1))
                dd = np.exp(1j * (np.imag(A[:, a]) - np.imag(A[:, b])))
                vals["code"].append(np.abs(dd.mean(axis=0)).mean(axis=-1))
            out[g] = {k: np.array(v) for k, v in vals.items()}
        plv[w] = out
        del A, U
    res["plv"] = plv
    res["timing"]["plv"] = time.time() - T0

    # PSI (M5) between MTL and frontal electrodes, and cross-spectral PSI (M6)
    nab = n_amp_bands(fs)
    amp_bands = BANDS[AMP_BANDS[:nab]]
    psi, cs = {}, {}
    for w, (x, sel) in wins.items():
        env = _filter_chunks(x, fs, np.arange(x.shape[-1]), amp_bands, "abs")   # full segment
        for mode in ("mtmfft", "sliding"):
            rng = np.random.default_rng(seed_for(f"psi|{w}|{mode}", sid))
            th = theta_fourier(x[..., sel].astype(np.float64), fs, mode)          # (n, ch, 5, w)
            S, PA, PB = cross_spectra(th, th)
            raw, z = psi_z(S, PA[:, None, :], PB[None, :, :], rng)              # (ch, ch)
            psi[(w, mode)] = {"raw": raw, "z": z}
            if mode == "mtmfft":
                code_raw = np.full(raw.shape, np.nan)
                code_z = np.full(raw.shape, np.nan)
                ij = [(a, b) for g in ("MTL-PFC", "MTL-OFC") for a, b in pairs[g]]
                if ij:
                    ia, ib = np.array(ij).T
                    o, zc = psi_code(th[:, ia], th[:, ib], rng)
                    code_raw[ia, ib], code_z[ia, ib] = o, zc
                psi[(w, "code")] = {"raw": code_raw, "z": code_z}
            # cross-spectral: theta of each amplitude envelope
            rng = np.random.default_rng(seed_for(f"cspsi|{w}|{mode}", sid))
            ea = env[..., sel]
            n, nch, nbb, T = ea.shape
            the = theta_fourier(ea.reshape(n, nch * nbb, T).astype(np.float64), fs, mode)
            the = the.reshape(n, nch, nbb, 5, the.shape[-1])
            Sx = np.einsum("rafw,rbcgw->abcfg", th, np.conj(the)) / (n * th.shape[-1])
            PBx = (np.abs(the) ** 2).mean(axis=(0, 4))                          # (ch, nbb, 5)
            rawx, zx = psi_z(Sx, PA[:, None, None, :], PBx[None, :, :, :], rng)  # (ch, ch, nbb)
            cs[(w, mode)] = {"raw": rawx, "z": zx}
        del env
    res["psi"], res["cspsi"] = psi, cs
    res["timing"]["psi"] = time.time() - T0

    # units for cross-spectral directionality and PAC
    units = []
    for e in np.where(keep)[0]:
        units.append({"system": regions[e], "ph": e, "amp": e})
    for g in ("MTL-PFC", "MTL-OFC"):
        fr = g.split("-")[1]
        for a, b in pairs[g]:
            units.append({"system": f"MTL->{fr}", "ph": a, "amp": b})
            units.append({"system": f"{fr}->MTL", "ph": b, "amp": a})
    for u in units:
        for (w, mode), d in cs.items():
            u[f"z_{w}_{mode}"] = float(d["z"][u["ph"], u["amp"], :].mean())
            u[f"raw_{w}_{mode}"] = float(d["raw"][u["ph"], u["amp"], :].mean())
        u["zf_post_mtmfft"] = cs[("post", "mtmfft")]["z"][u["ph"], u["amp"], :16].copy()
        u["ph_label"], u["amp_label"] = labels[u["ph"]], labels[u["amp"]]
        u["hemi"] = hemis[u["ph"]]
    res["units"] = units

    # theta peak reading (b): phase-directing electrodes only (any electrode in a directing unit)
    pdir = sorted({i for u in units if u["z_post_mtmfft"] > 1.96 for i in (u["ph"], u["amp"])})
    if pdir:
        pkb = res["enc_time_mean_z"][pdir][:, PEAK_BANDS].mean(axis=0)
        res["peak_curve_dir"], res["peak_band_dir"] = pkb, int(PEAK_BANDS[np.argmax(pkb)])
    else:
        res["peak_curve_dir"], res["peak_band_dir"] = None, None

    # ---- PAC (M9) on the phase-directing units, postcue, per condition
    res["pac"] = []
    if pac:
        pb = res["peak_band_all"]
        if pb == 1:      # 1.5-4 Hz maximum: the nearest 3 Hz wide band, 2-5 Hz
            pb = 2
        if pb == 6:      # 6-10 Hz maximum: the nearest 3 Hz wide band, 5-8 Hz
            pb = 5
        res["theta_band_used"] = BANDS[pb].tolist()
        dir_units = [i for i, u in enumerate(units) if u["z_post_mtmfft"] > 1.96]
        need = sorted({units[i][k] for i in dir_units for k in ("ph", "amp")})
        xp = xs["proc"]
        for cond in (1, 2, 3):
            m = tic[:, 3] == cond
            xc = xp[m] - xp[m].mean(axis=0, keepdims=True)
            sub_idx = np.array(need, dtype=int)
            if len(sub_idx) == 0:
                continue
            ph = _filter_chunks(xc[:, sub_idx], fs, psel, BANDS[[pb]], "angle")[:, :, 0]   # (n, k, T)
            am = _filter_chunks(xc[:, sub_idx], fs, psel, amp_bands, "abs")                # (n, k, F, T)
            pos = {c: i for i, c in enumerate(need)}
            for i in dir_units:
                u = units[i]
                for rd in pac_readings:
                    rng = np.random.default_rng(seed_for(f"pac|{rd}|{cond}|{u['ph']}|{u['amp']}", sid))
                    z = pac_z(ph[:, pos[u["ph"]]].astype(np.float64), am[:, pos[u["amp"]]], rng, rd)
                    z20 = resample_20hz(z, fs)[:, :19]
                    res["pac"].append({"unit": i, "system": u["system"], "cond": cond, "reading": rd,
                                       "z": z20.astype(np.float32), "n_trials": int(m.sum())})
            del ph, am
    res["timing"]["pac"] = time.time() - T0
    log(f"{sid}: analysed in {time.time() - T0:.0f} s; " + ", ".join(f"{k} {v:.0f}" for k, v in res["timing"].items()))
    return res
EOF
date -u
```

```
Sun Nov  8 20:54:05 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='fcx2.py'; s=open(p).read()
s=s.replace('env = _filter_chunks(x, fs, np.arange(x.shape[-1]), amp_bands, "abs")   # full segment','env = _filter_chunks(x, fs, sel, amp_bands, "abs")   # filtered on the full segment')
s=s.replace('            ea = env[..., sel]\n','            ea = env\n')
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && timeout 1800 python - <<'EOF'
import time, resource, numpy as np, pandas as pd, pickle, os
import fcx2
ch=fcx2.read_channel_table()
c=ch[ch.subject=='s8'].reset_index(drop=True)
sub=fcx2.load_subject('s8', c.label.tolist())
r=fcx2.analyse_subject(sub, c, nperm_cluster=200)
print('mem GB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
print(r['pow_enc'], r['pow_post'], r['erp_enc'], r['erp_post'], sep='\n')
print('peak', r['peak_curve_all'], r['peak_band_all'], r['peak_band_dir'])
for w in ['pre','post']:
    for g,v in r['plv'][w].items():
        if len(v['implv']): print(w,g,{k:np.round(x.mean(0),3) for k,x in v.items()})
print(pd.DataFrame([{k:v for k,v in u.items() if not k.startswith('zf')} for u in r['units']]).round(2).to_string())
print(len(r['pac']))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
  File "entries/crcns-fcx-2-johnson-2018/fcx2.py", line 653, in analyse_subject
    base = lowpass_erp(xs["pre"], fs, bsel).mean(axis=(0, 2))
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "entries/crcns-fcx-2-johnson-2018/fcx2.py", line 607, in lowpass_erp
    pad = Padder(x.shape[-1], fs)
  File "entries/crcns-fcx-2-johnson-2018/fcx2.py", line 204, in __init__
    self.nfft = signal.next_fast_len(self.npad + 2 * 3 * int(fs) + 2)
                ^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'scipy.signal' has no attribute 'next_fast_len'
```

**Agent calls Bash**

```bash
sed -i 's/signal.next_fast_len/sfft.next_fast_len/; s/^from scipy import ndimage, signal, stats/from scipy import fft as sfft\nfrom scipy import ndimage, signal, stats/' fcx2.py && cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && timeout 1800 python - <<'EOF'
import time, resource, numpy as np, pandas as pd, pickle, os
import fcx2
ch=fcx2.read_channel_table()
c=ch[ch.subject=='s8'].reset_index(drop=True)
sub=fcx2.load_subject('s8', c.label.tolist())
r=fcx2.analyse_subject(sub, c, nperm_cluster=200)
print('mem GB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
print(r['pow_enc'], r['pow_post'], r['erp_enc'], r['erp_post'], sep='\n')
print('peak', r['peak_curve_all'], r['peak_band_all'], r['peak_band_dir'])
for w in ['pre','post']:
    for g,v in r['plv'][w].items():
        if len(v['implv']): print(w,g,{k:np.round(x.mean(0),3) for k,x in v.items()})
print(pd.DataFrame([{k:v for k,v in u.items() if not k.startswith('zf')} for u in r['units']]).round(2).to_string())
print(len(r['pac']))
EOF
```

```
s8: analysed in 88 s; erp 1, power 80, power_test 80, plv 82, psi 88, pac 88
mem GB 0.72336
   ch  p_subject  p_electrode  n_clusters
0   0   1.000000     0.407960          21
1   1   0.845771     0.089552          24
2   2   1.000000     1.000000          15
3   3   1.000000     0.417910          22
4   4   1.000000     0.606965          24
5   5   1.000000     0.338308          19
6   6   0.766169     0.218905          24
7   7   0.009950     0.009950          17
8   8   0.049751     0.009950          18
   ch  p_subject  p_electrode  n_clusters
0   0   1.000000     0.980100           9
1   1   1.000000     0.597015           7
2   2   0.766169     0.159204           8
3   3   0.711443     0.144279          10
4   4   1.000000     0.845771           9
5   5   0.701493     0.134328          12
6   6   1.000000     0.542289           7
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && timeout 600 python - <<'EOF'
import time, numpy as np, fcx2
fs=1000.; x=np.random.randn(100,8,4503).astype(np.float32)
sel=np.arange(1500,3001)
t=time.time(); p=fcx2._filter_chunks(x,fs,sel,fcx2.BANDS,"power"); print('filter',time.time()-t, p.shape)
t=time.time(); z=fcx2.resample_20hz(p,fs); print('resample',time.time()-t, z.shape)
rng=np.random.default_rng(0)
bp=p[...,:200]
t=time.time(); fcx2.baseline_bootstrap(bp,100,rng); print('boot',time.time()-t)
t=time.time(); r=fcx2.cluster_test(z[:,:,:,:], (np.arange(100)%2)+1, 't', rng, 100); print('cluster 100',time.time()-t)
EOF
```

```
filter 3.8965742588043213 (100, 8, 24, 1501)
resample 76.71560573577881 (100, 8, 24, 31)
boot 0.08694124221801758
cluster 100 0.07147002220153809
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='fcx2.py'; s=open(p).read()
old=s[s.index('def resample_20hz(x, fs):'):s.index('def baseline_bootstrap')]
new='''_RESAMPLE_CACHE = {}


def resample_20hz(x, fs):
    """Down-sample the last axis to 20 Hz as MATLAB resample(x, p, q, 100) (resamplemtx.m).

    The resampler is linear, so it is applied as a matrix built once per length and rate.
    """
    T = x.shape[-1]
    key = (T, fs)
    if key not in _RESAMPLE_CACHE:
        from fractions import Fraction
        fr = Fraction(20, int(round(fs))).limit_denominator(1000)
        p, q = fr.numerator, fr.denominator
        m = max(p, q)
        h = signal.firwin(2 * 100 * m + 1, 1.0 / m, window=("kaiser", 5.0)) * p
        n_new = int(np.floor((T - 1) / fs * 20)) + 1
        if n_new % 2 == 0:
            n_new += 1
        R = signal.resample_poly(np.eye(T), p, q, axis=-1, window=h)[:, :n_new]
        _RESAMPLE_CACHE[key] = R
    R = _RESAMPLE_CACHE[key]
    return x @ R.astype(x.dtype if x.dtype in (np.float32, np.float64) else np.float64)


'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && timeout 600 python - <<'EOF'
import time, numpy as np, fcx2
from scipy import signal
fs=1000.; x=np.random.randn(100,8,24,1501).astype(np.float32)
t=time.time(); z=fcx2.resample_20hz(x,fs); print('resample',time.time()-t, z.shape)
t=time.time(); z=fcx2.resample_20hz(x,fs); print('resample2',time.time()-t, z.shape)
y=np.sin(np.arange(1501)/1000*2*np.pi*2)+3; print(np.round(fcx2.resample_20hz(y,fs),2))
print(fcx2.resample_20hz(np.ones(461),512.).round(2), fcx2.resample_20hz(np.ones(901),1000.).shape)
EOF
```

```
resample 6.04853081703186 (100, 8, 24, 31)
resample2 0.038355112075805664 (100, 8, 24, 31)
[1.59 3.86 3.8  4.06 3.5  3.07 2.35 2.1  2.   2.46 2.96 3.63 3.91 3.99
 3.55 3.04 2.37 2.09 2.01 2.45 2.96 3.63 3.9  4.01 3.53 3.07 2.33 2.16
 1.89 2.7  1.46]
[2.57 5.48 4.73 5.2  4.84 5.14 4.88 5.12 4.89 5.11 4.89 5.12 4.88 5.14
 4.84 5.2  4.73 5.48 2.42] (19,)
```

**Agent calls Bash**

```bash
sed -i 's/        h = signal.firwin(2 \* 100 \* m + 1, 1.0 \/ m, window=("kaiser", 5.0)) \* p/        h = signal.firwin(2 * 100 * m + 1, 1.0 \/ m, window=("kaiser", 5.0))  # resample_poly scales by p/' fcx2.py && grep -n "kaiser" fcx2.py && cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && python -c "
import fcx2,numpy as np
print(fcx2.resample_20hz(np.ones(461),512.).round(2)); print(fcx2.resample_20hz(np.ones(901),1000.).round(2))"
```

```
260:        h = signal.firwin(2 * 100 * m + 1, 1.0 / m, window=("kaiser", 5.0))  # resample_poly scales by p
[0.51 1.1  0.95 1.04 0.97 1.03 0.98 1.02 0.98 1.02 0.98 1.02 0.98 1.03
 0.97 1.04 0.95 1.1  0.48]
[0.5  1.1  0.95 1.04 0.97 1.03 0.98 1.02 0.98 1.02 0.98 1.02 0.98 1.03
 0.97 1.04 0.95 1.1  0.5 ]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='fcx2.py'; s=open(p).read()
s=s.replace('''            cs[(w, mode)] = {"raw": rawx, "z": zx}
''','''            cs[(w, mode)] = {"raw": rawx, "z": zx}
            if mode == "mtmfft":
                keep_th[w] = (th, the)
''')
s=s.replace('''    psi, cs = {}, {}
    for w, (x, sel) in wins.items():''','''    psi, cs, keep_th = {}, {}, {}
    for w, (x, sel) in wins.items():''')
s=s.replace('''        u["zf_post_mtmfft"] = cs[("post", "mtmfft")]["z"][u["ph"], u["amp"], :16].copy()
''','''        u["zf_post_mtmfft"] = cs[("post", "mtmfft")]["z"][u["ph"], u["amp"], :16].copy()
        for w, (th, the) in keep_th.items():
            rng = np.random.default_rng(seed_for(f"cspsi-code|{w}|{u['ph']}|{u['amp']}", sid))
            nbb = the.shape[2]
            A = np.repeat(th[:, [u["ph"]]], nbb, axis=1)
            o, zc = psi_code(A, the[:, u["amp"]], rng)
            u[f"z_{w}_code"], u[f"raw_{w}_code"] = float(zc.mean()), float(o.mean())
''')
open(p,'w').write(s)
EOF
date -u; cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && timeout 1800 python - <<'EOF'
import time, resource, numpy as np, pandas as pd
import fcx2
ch=fcx2.read_channel_table()
for sid in ['s8','s2']:
    c=ch[ch.subject==sid].reset_index(drop=True)
    sub=fcx2.load_subject(sid, c.label.tolist())
    print(sid,'load',round(sub['load_s']), {k:v['x'].shape for k,v in sub['seg'].items()})
    r=fcx2.analyse_subject(sub, c, nperm_cluster=1000)
    print('mem GB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
    print('excl', r['excluded'].sum(), 'erp sig', (r['erp_enc'].p_subject<.05).sum(), (r['erp_post'].p_subject<.05).sum(), (r['erp_enc'].p_electrode<.05).sum(), (r['erp_post'].p_electrode<.05).sum())
    print('peak', r['peak_curve_all'].round(2), r['peak_band_all'], r['peak_band_dir'])
    U=pd.DataFrame([{k:v for k,v in u.items() if not k.startswith('zf')} for u in r['units']])
    print(U.groupby('system')[[c for c in U.columns if c.startswith('z_')]].agg(lambda v: f"{np.mean(v):.2f}/{(v>1.96).sum()}/{len(v)}").to_string())
    print('pac n', len(r['pac']))
    del sub
EOF
```

```
Exit code 1
Sun Nov  8 20:58:53 UTC 2026
s8 load 14 {'pre': (90, 9, 2305), 'encmain': (90, 9, 2304), 'proc': (90, 9, 2305)}
s8: analysed in 18 s; erp 1, power 9, power_test 10, plv 12, psi 17, pac 18
mem GB 0.727252
excl 2 erp sig 0 0 0 0
peak [ 0.43  0.49 -0.34 -0.46  0.5   0.07] 5 None
         z_pre_mtmfft z_pre_sliding z_post_mtmfft z_post_sliding z_pre_code z_post_code
system                                                                                 
MTL         -0.46/0/4     -0.37/0/4     -0.47/0/4      -0.45/0/4  14.37/3/4  -10.30/1/4
MTL->PFC    -0.06/0/3     -0.14/0/3     -0.29/0/3      -1.06/0/3  -6.12/0/3  -14.80/0/3
PFC         -0.04/0/3     -0.37/0/3     -0.56/0/3      -1.09/0/3  27.54/2/3   11.87/2/3
PFC->MTL    -0.20/0/3     -0.48/0/3     -0.14/0/3      -0.57/0/3  28.14/3/3    4.88/1/3
pac n 0
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
  File "entries/crcns-fcx-2-johnson-2018/fcx2.py", line 147, in load_subject
    out.update(_read_derived(raw, channels))
               ~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "entries/crcns-fcx-2-johnson-2018/fcx2.py", line 162, in _read_derived
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='fcx2.py'; s=open(p).read()
old='''            trefs = g["trial"][()].ravel()
            tm = f[g["time"][()].ravel()[0]][()].ravel()
            x = np.stack([f[r][()][:, idx].T for r in trefs]).astype(np.float32)
'''
new='''            trefs = g["trial"][()].ravel()
            tms = [f[r][()].ravel() for r in g["time"][()].ravel()]
            # trials can differ in length by a few samples; keep the samples all trials share,
            # from the common first time
            starts = np.array([t[0] for t in tms])
            nmin = min(len(t) for t in tms)
            tm = tms[0][:nmin]
            x = np.stack([f[r][()][:nmin, idx].T for r in trefs]).astype(np.float32)
'''
s=s.replace(old,new)
s=s.replace('''                "same_time": all(np.array_equal(f[r][()].ravel(), tm) for r in g["time"][()].ravel()),''','''                "same_start": bool(np.allclose(starts, starts[0])),
                "n_samples": np.array([len(t) for t in tms]),''')
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && timeout 1800 python - <<'EOF'
import time, resource, numpy as np, pandas as pd
import fcx2
ch=fcx2.read_channel_table()
for sid in ['s2']:
    c=ch[ch.subject==sid].reset_index(drop=True)
    sub=fcx2.load_subject(sid, c.label.tolist())
    print(sid,'load',round(sub['load_s']), {k:(v['x'].shape, v['same_start'], np.unique(v['n_samples'],return_counts=True), v['time'][[0,-1]]) for k,v in sub['seg'].items()})
    r=fcx2.analyse_subject(sub, c, nperm_cluster=1000)
    print('mem GB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
    print('excl', r['excluded'].sum(), 'erp sig', (r['erp_enc'].p_subject<.05).sum(), (r['erp_post'].p_subject<.05).sum(), (r['erp_enc'].p_electrode<.05).sum(), (r['erp_post'].p_electrode<.05).sum())
    print('peak', r['peak_curve_all'].round(2), r['peak_band_all'], r['peak_band_dir'])
    U=pd.DataFrame([{k:v for k,v in u.items() if not k.startswith('zf')} for u in r['units']])
    print(U.groupby('system')[[c for c in U.columns if c.startswith('z_')]].agg(lambda v: f"{np.mean(v):.2f}/{(v>1.96).sum()}/{len(v)}").to_string())
    print('pac n', len(r['pac']))
    for w in ['pre','post']:
        for g,v in r['plv'][w].items():
            if len(v['implv']): print(w,g,{k:np.round(x.mean(0),3) for k,x in v.items()})
    del sub
EOF
```

```
s2 load 21 {'pre': ((113, 25, 4501), True, (array([4501]), array([113])), array([-1.5,  3. ])), 'encmain': ((113, 25, 4502), True, (array([4502, 4503]), array([85, 28])), array([-1.5  ,  3.001])), 'proc': ((113, 25, 4501), True, (array([4501]), array([113])), array([-1.5,  3. ]))}
s2: analysed in 116 s; erp 6, power 54, power_test 56, plv 73, psi 114, pac 116
mem GB 3.469192
excl 0 erp sig 0 0 0 0
peak [ 0.04  0.51  0.29 -0.1  -0.02  0.34] 2 None
         z_pre_mtmfft z_pre_sliding z_post_mtmfft z_post_sliding   z_pre_code  z_post_code
system                                                                                    
MTL          0.13/0/7      0.31/0/7     -0.06/0/7      -0.09/0/7     1.88/3/7    12.39/6/7
MTL->PFC   -0.06/0/28    -0.07/0/28    -0.02/0/28     -0.03/0/28   2.61/12/28  13.76/25/28
OFC         -0.68/0/3     -1.84/0/3     -0.65/0/3      -1.31/0/3     4.09/2/3   -13.27/0/3
PFC        -0.05/0/15    -0.06/0/15    -0.08/0/15      0.17/0/15    7.91/9/15    4.75/7/15
PFC->MTL   -0.21/0/28     0.06/0/28    -0.17/0/28      0.07/0/28  -2.38/10/28   2.37/14/28
pac n 0
pre MTL-MTL {'implv': array([0.06 , 0.089, 0.102, 0.087, 0.083, 0.08 , 0.068, 0.058, 0.06 ,
       0.065, 0.071], dtype=float32), 'pli': array([0.09 , 0.128, 0.144, 0.124, 0.12 , 0.114, 0.098, 0.085, 0.09 ,
       0.094, 0.098], dtype=float32), 'code': array([0.087, 0.089, 0.092, 0.103, 0.109, 0.115, 0.118, 0.119, 0.118,
       0.11 , 0.109], dtype=float32)}
pre MTL-PFC {'implv': array([0.062, 0.061, 0.057, 0.064, 0.06 , 0.05 , 0.045, 0.054, 0.054,
       0.056, 0.052], dtype=float32), 'pli': array([0.084, 0.085, 0.08 , 0.087, 0.087, 0.073, 0.063, 0.078, 0.077,
       0.078, 0.075], dtype=float32), 'code': array([0.082, 0.085, 0.085, 0.084, 0.084, 0.086, 0.086, 0.091, 0.095,
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && timeout 600 python - <<'EOF'
import time, numpy as np, fcx2
rng=np.random.default_rng(0)
ph=rng.uniform(-np.pi,np.pi,(35,901)); am=rng.random((35,17,901)).astype(np.float32)
for rd in 'ab':
    t=time.time(); z=fcx2.pac_z(ph,am,rng,rd); print(rd,time.time()-t, z.shape, z.mean(), z.std())
EOF
```

```
a 0.26836633682250977 (17, 901) 0.011842534684864993 1.0213170812960528
b 0.2696409225463867 (17, 901) 0.009759955986467068 1.0242008397381974
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='fcx2.py'; s=open(p).read()
# chunk sliding mode
old='''    x = x - x.mean(axis=-1, keepdims=True)
    T = x.shape[-1]
    if mode == "mtmfft":'''
new='''    if mode != "mtmfft" and x.shape[1] > 32:
        return np.concatenate([theta_fourier(x[:, i:i + 32], fs, mode, step_s)
                               for i in range(0, x.shape[1], 32)], axis=1)
    x = x - x.mean(axis=-1, keepdims=True)
    T = x.shape[-1]
    if mode == "mtmfft":'''
s=s.replace(old,new)
# cross-spectral only mtmfft
s=s.replace('''            # cross-spectral: theta of each amplitude envelope
            rng = np.random.default_rng''','''            if mode != "mtmfft":
                continue
            # cross-spectral: theta of each amplitude envelope (code's single window)
            rng = np.random.default_rng''')
# PAC selection: union of main and code readings
s=s.replace('''        dir_units = [i for i, u in enumerate(units) if u["z_post_mtmfft"] > 1.96]''','''        for u in units:
            u["dir_main"] = u["z_post_mtmfft"] > 1.96
            u["dir_code"] = u["z_post_code"] > 1.96
        dir_units = [i for i, u in enumerate(units) if u["dir_main"] or u["dir_code"]]''')
open(p,'w').write(s)
EOF
grep -n "z_{w}_{mode}\|for (w, mode), d in cs" fcx2.py
```

```
798:        for (w, mode), d in cs.items():
799:            u[f"z_{w}_{mode}"] = float(d["z"][u["ph"], u["amp"], :].mean())
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='fcx2.py'; s=open(p).read()
s=s.replace('''    if pdir:
        pkb = res["enc_time_mean_z"][pdir][:, PEAK_BANDS].mean(axis=0)
        res["peak_curve_dir"], res["peak_band_dir"] = pkb, int(PEAK_BANDS[np.argmax(pkb)])
    else:
        res["peak_curve_dir"], res["peak_band_dir"] = None, None
''','''    if pdir:
        pkb = res["enc_time_mean_z"][pdir][:, PEAK_BANDS].mean(axis=0)
        res["peak_curve_dir"], res["peak_band_dir"] = pkb, int(PEAK_BANDS[np.argmax(pkb)])
    else:
        res["peak_curve_dir"], res["peak_band_dir"] = None, None
    pdir = sorted({i for u in units if u["z_post_code"] > 1.96 for i in (u["ph"], u["amp"])})
    if pdir:
        pkb = res["enc_time_mean_z"][pdir][:, PEAK_BANDS].mean(axis=0)
        res["peak_curve_dir_code"], res["peak_band_dir_code"] = pkb, int(PEAK_BANDS[np.argmax(pkb)])
    else:
        res["peak_curve_dir_code"], res["peak_band_dir_code"] = None, None
''')
s += '''

def sanity_subject(sub):
    """Checks of the derived data against the trial table and against each other.

    - offsets of each segment's sampleinfo from the trial table's epoch columns;
    - whether overlapping samples of the pre, encmain and proc segments of a trial are equal
      when placed by sampleinfo (one shared clock);
    - whether trialinfo is the same in the three segments and equals the trial table's columns;
    - the trial-averaged evoked signal (RMS over the analysed channels) in 50 ms bins, to show
      where the responses to the start screen, the stimuli and the test cue fall.
    """
    out = {}
    tr = sub["trials"].set_index("trial")
    seg = sub["seg"]
    ti = seg["encmain"]["trialinfo"]
    T = tr.loc[ti[:, 0].astype(int)]
    out["offsets"] = {
        "pre - pre_start": np.unique(seg["pre"]["sampleinfo"][:, 0] - T.pre_start.to_numpy()),
        "encmain - enc_start": np.unique(seg["encmain"]["sampleinfo"][:, 0] - T.enc_start.to_numpy()),
        "proc - post_start": np.unique(seg["proc"]["sampleinfo"][:, 0] - T.post_start.to_numpy()),
    }
    out["trialinfo_same_segments"] = all(np.array_equal(seg[k]["trialinfo"], ti) for k in ("pre", "proc"))
    out["trialinfo_matches_table"] = bool(np.array_equal(
        ti[:, 1:6], T[["accuracy", "trial_type", "condition", "jitter", "rt"]].to_numpy()))
    diffs, overl = [], []
    for a, b in (("pre", "encmain"), ("encmain", "proc")):
        xa, xb = seg[a]["x"], seg[b]["x"]
        md, nov = 0.0, []
        for i in range(xa.shape[0]):
            sa = seg[a]["sampleinfo"][i, 0] + np.arange(xa.shape[-1])
            sb = seg[b]["sampleinfo"][i, 0] + np.arange(xb.shape[-1])
            _, ia, ib = np.intersect1d(sa, sb, return_indices=True)
            nov.append(len(ia))
            if len(ia):
                md = max(md, float(np.abs(xa[i][:, ia] - xb[i][:, ib]).max()))
        diffs.append(md)
        overl.append((min(nov), max(nov)))
    out["overlap_maxdiff"] = dict(zip(["pre/encmain", "encmain/proc"], diffs))
    out["overlap_samples"] = dict(zip(["pre/encmain", "encmain/proc"], overl))
    ev = {}
    for k in ("pre", "encmain", "proc"):
        d = seg[k]
        m = d["x"].mean(axis=0)                              # (ch, T)
        m = m - m[:, d["time"] < -1.0].mean(axis=1, keepdims=True)
        rms = np.sqrt((m ** 2).mean(axis=0))
        edges = np.arange(-1.5, 3.0001, 0.05)
        idx = np.digitize(d["time"], edges) - 1
        ev[k] = np.array([rms[idx == j].mean() if np.any(idx == j) else np.nan for j in range(len(edges) - 1)])
    out["evoked_rms"] = ev
    out["evoked_edges"] = np.arange(-1.5, 3.0001, 0.05)
    out["fs"] = seg["encmain"]["fs"]
    out["n_labels"] = len(seg["encmain"]["labels"])
    out["labels"] = seg["encmain"]["labels"]
    out["time_range"] = {k: (float(seg[k]["time"][0]), float(seg[k]["time"][-1]), len(seg[k]["time"])) for k in seg}
    out["n_samples"] = {k: (int(seg[k]["n_samples"].min()), int(seg[k]["n_samples"].max())) for k in seg}
    out["same_start"] = {k: seg[k]["same_start"] for k in seg}
    out["hdr_fs"] = {k: seg[k]["hdr_fs"] for k in seg}
    out["n_trials_derived"] = int(ti.shape[0])
    out["members"] = sub["members"]
    out["trials"] = sub["trials"]
    out["x_range"] = (float(min(seg[k]["x"].min() for k in seg)), float(max(seg[k]["x"].max() for k in seg)))
    out["load_s"] = sub["load_s"]
    return out


def process_subject(sid, chtab, log=print, **kw):
    """Load one subject, check it and run every per-subject measure; the raw data are dropped."""
    chans = chtab[chtab.subject == sid].reset_index(drop=True)
    sub = load_subject(sid, chans.label.tolist())
    san = sanity_subject(sub)
    res = analyse_subject(sub, chans, log=log, **kw)
    res["sanity"] = san
    res["chans"] = chans
    del sub
    return res
'''
open(p,'w').write(s)
EOF
mkdir -p $TMPDIR/devres; date -u
```

```
Sun Nov  8 21:03:20 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && timeout 1800 python - <<'EOF'
import time, resource, numpy as np, pandas as pd, pickle, os
import fcx2
ch=fcx2.read_channel_table()
r=fcx2.process_subject('s8', ch)
print('mem GB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
s=r['sanity']; print({k:v for k,v in s.items() if k not in ('evoked_rms','trials','labels','evoked_edges')})
for k,v in s['evoked_rms'].items(): print(k, np.round(v,1))
print(len(r['pac']), r['pac'][0]['z'].shape, r.get('theta_band_used'))
pickle.dump(r, open(os.environ['TMPDIR']+'/devres/s8.pkl','wb'))
EOF
```

```
s8: analysed in 17 s; erp 1, power 9, power_test 10, plv 12, psi 15, pac 17
mem GB 0.651952
{'offsets': {'pre - pre_start': array([51.]), 'encmain - enc_start': array([0.]), 'proc - post_start': array([-154.])}, 'trialinfo_same_segments': True, 'trialinfo_matches_table': True, 'overlap_maxdiff': {'pre/encmain': 0.0, 'encmain/proc': 0.0}, 'overlap_samples': {'pre/encmain': (1373, 1399), 'encmain/proc': (1153, 1281)}, 'fs': 512.0, 'n_labels': 43, 'time_range': {'pre': (-1.5, 3.0, 2305), 'encmain': (-1.5, 2.998046875, 2304), 'proc': (-1.5, 3.0, 2305)}, 'n_samples': {'pre': (2305, 2305), 'encmain': (2304, 2304), 'proc': (2305, 2305)}, 'same_start': {'pre': True, 'encmain': True, 'proc': True}, 'hdr_fs': {'pre': 512.0, 'encmain': 512.0, 'proc': 512.0}, 'n_trials_derived': 90, 'members': {'s8/s8_MNI_grid.csv': 49364, 's8/data_primary.mat': 347028413, 's8/data_derived.mat': 210369492, 's8/summary_file_trial.csv': 4730}, 'x_range': (-109.68759155273438, 117.62625122070312), 'load_s': 14.529661178588867}
pre [1.5 1.9 1.2 2.2 1.9 1.6 0.9 1.3 2.  2.1 2.7 3.3 3.6 2.4 1.5 1.2 0.9 1.4
 1.1 1.1 1.6 2.6 2.1 1.7 1.8 1.9 2.8 2.  1.3 2.4 2.2 2.1 1.5 2.7 3.3 2.8
 2.  1.9 1.3 1.3 1.3 1.9 3.  2.7 2.5 2.  2.4 3.  1.4 2.  2.5 2.8 2.7 2.
 1.6 1.3 1.8 2.1 1.6 2.  2.2 1.7 1.5 1.7 1.8 2.3 1.7 1.5 1.8 2.1 1.3 1.1
 0.8 1.9 1.8 1.5 2.3 2.  1.6 2.  2.8 2.7 2.5 1.7 1.4 1.2 1.8 2.1 2.  1.7]
encmain [2.3 2.1 1.  1.1 1.2 1.7 2.7 2.3 2.2 1.7 2.9 3.5 2.1 1.8 2.8 2.9 2.5 1.7
 1.8 1.5 1.7 1.8 1.4 2.4 2.4 1.5 1.1 1.3 1.8 2.5 2.  1.7 1.6 1.9 1.2 1.5
 1.3 2.  2.2 1.9 2.  2.4 2.1 2.  2.1 2.3 2.4 1.5 1.5 1.9 2.1 2.4 2.2 1.9
 1.4 1.2 1.6 1.6 1.7 2.4 2.5 1.5 1.7 1.2 1.3 1.1 0.6 1.4 2.  1.4 1.  1.3
 1.1 1.4 2.4 2.1 1.5 1.6 1.8 1.8 1.1 1.6 2.3 2.3 2.  1.4 1.9 1.5 1.8 1.9]
proc [1.9 1.5 1.4 1.4 1.5 1.  1.9 2.  1.4 0.9 1.5 1.9 1.8 1.8 1.9 1.4 1.4 2.
 1.8 1.  0.7 1.1 1.  1.6 1.2 1.1 1.4 1.3 1.1 1.2 1.  1.3 0.9 0.9 1.9 2.5
 2.4 2.1 2.  2.1 1.5 1.4 1.3 1.3 1.1 1.1 2.  1.6 1.5 1.4 1.1 1.1 1.2 0.9
 0.8 1.5 1.4 1.3 1.1 1.
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='fcx2.py'; s=open(p).read()
s=s.replace('''    out["evoked_rms"] = ev
''','''    out["evoked_rms"] = ev
    # high-gamma (70-150 Hz) amplitude, all trials, per delay length (jitter), 50 ms bins,
    # relative to the mean over the segment: the test cue comes 250 ms later after the long
    # delay, so the two time courses must part where the test cue appears
    hg = {}
    for k in ("pre", "encmain", "proc"):
        d = seg[k]
        a = _filter_chunks(d["x"], d["fs"], np.arange(d["x"].shape[-1]), np.array([[70.0, 150.0]]), "abs")[:, :, 0]
        a = a / a.mean(axis=(0, 2), keepdims=True)
        edges = np.arange(-1.5, 3.0001, 0.05)
        idx = np.digitize(d["time"], edges) - 1
        for jit in (900, 1150):
            m = a[d["trialinfo"][:, 4] == jit].mean(axis=(0, 1))
            hg[(k, jit)] = np.array([m[idx == j].mean() if np.any(idx == j) else np.nan for j in range(len(edges) - 1)])
    out["hg"] = hg
''')
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && cat > $TMPDIR/devrun.py <<'EOF'
import time, resource, numpy as np, pandas as pd, pickle, os, sys
sys.path.insert(0, 'entries/crcns-fcx-2-johnson-2018')
import fcx2
ch=fcx2.read_channel_table()
T=time.time()
for sid in sys.argv[1:]:
    r=fcx2.process_subject(sid, ch)
    print(sid, 'load', round(r['sanity']['load_s']), 'cum', round(time.time()-T), 'mem GB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, 'pac', len(r['pac']), flush=True)
    pickle.dump(r, open(os.environ['TMPDIR']+f'/devres/{sid}.pkl','wb'))
EOF
timeout 600 python $TMPDIR/devrun.py s8 && python - <<'EOF'
import pickle, os, numpy as np
r=pickle.load(open(os.environ['TMPDIR']+'/devres/s8.pkl','rb'))
for k,v in r['sanity']['hg'].items(): print(k, np.round(v,2)[::2])
EOF
```

```
s8: analysed in 17 s; erp 1, power 9, power_test 10, plv 12, psi 15, pac 17
s8 load 14 cum 32 mem GB 0.651796 pac 24
('pre', 900) [1.2  1.   1.1  1.01 0.99 1.   1.01 1.04 0.98 0.99 0.98 1.   0.97 0.99
 0.98 0.97 1.   0.99 0.99 0.98 0.99 0.97 0.98 0.95 0.96 1.   1.03 1.02
 1.08 1.03 0.98 0.98 1.   1.   0.98 1.   1.   0.97 0.97 0.98 1.   0.98
 1.01 1.   0.97]
('pre', 1150) [1.22 0.98 1.03 1.   1.   1.02 0.99 0.99 0.97 0.99 0.97 0.98 0.99 1.
 1.04 0.97 0.98 0.99 0.97 0.98 0.99 0.98 0.96 0.98 0.99 1.   1.   1.01
 0.98 1.04 0.99 1.   1.   0.96 0.99 1.   0.98 0.99 1.01 0.96 1.01 1.01
 1.03 1.03 1.  ]
('encmain', 900) [1.2  0.98 0.99 0.98 0.97 0.95 0.97 1.   1.03 1.02 1.07 1.03 0.99 0.98
 1.01 1.   0.98 1.01 1.01 0.99 0.98 0.99 1.01 0.97 1.01 1.02 0.96 1.
 1.02 0.98 1.   0.99 0.99 0.98 0.98 1.   0.97 0.98 1.   0.99 0.99 0.97
 0.99 1.   1.04]
('encmain', 1150) [1.2  0.98 1.   0.97 0.96 0.99 0.99 1.01 0.99 1.02 1.   1.04 1.   1.
 0.99 0.97 1.   1.02 0.99 0.99 1.01 0.97 1.02 1.03 1.03 1.03 1.02 1.01
 1.03 1.02 1.   1.   1.01 0.99 0.99 0.98 0.96 0.95 0.98 0.97 0.97 0.99
 0.99 1.02 0.99]
('proc', 900) [1.24 0.99 1.01 0.97 1.01 1.02 0.96 1.   1.02 0.98 1.   0.99 0.99 0.98
 0.98 1.   0.97 0.98 1.   0.99 0.99 0.98 0.99 1.   1.03 0.97 1.01 1.03
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && timeout 5400 python $TMPDIR/devrun.py s1 s2 s3 s4 s5 s6 s7 s9 s10 2>&1 | grep -v Warning; date -u
```

```
Sun Nov  8 21:05:03 UTC 2026
s1: analysed in 90 s; erp 3, power 35, power_test 36, plv 46, psi 58, pac 90
s1 load 27 cum 118 mem GB 1.973952 pac 126
s2: analysed in 177 s; erp 6, power 46, power_test 50, plv 67, psi 91, pac 177
s2 load 22 cum 321 mem GB 3.019664 pac 312
s3: analysed in 33 s; erp 2, power 11, power_test 12, plv 15, psi 20, pac 33
s3 load 22 cum 377 mem GB 3.019664 pac 60
s4: analysed in 122 s; erp 5, power 35, power_test 37, plv 50, psi 67, pac 122
s4 load 24 cum 526 mem GB 3.019664 pac 180
s5: analysed in 206 s; erp 7, power 46, power_test 49, plv 65, psi 88, pac 206
s5 load 71 cum 807 mem GB 4.571508 pac 474
s6: analysed in 270 s; erp 11, power 83, power_test 87, plv 114, psi 158, pac 270
s6 load 60 cum 1143 mem GB 5.220592 pac 408
s7: analysed in 124 s; erp 6, power 40, power_test 42, plv 55, psi 75, pac 124
s7 load 32 cum 1301 mem GB 5.220592 pac 180
s9: analysed in 80 s; erp 3, power 22, power_test 25, plv 33, psi 44, pac 80
s9 load 28 cum 1411 mem GB 5.220592 pac 330
s10: analysed in 669 s; erp 12, power 95, power_test 99, plv 147, psi 198, pac 669
s10 load 35 cum 2122 mem GB 5.888464 pac 1782
Sun Nov  8 21:40:26 UTC 2026
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-fcx-2-johnson-2018 && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, os, numpy as np, pandas as pd
import fcx2
R={s:pickle.load(open(os.environ['TMPDIR']+f'/devres/{s}.pkl','rb')) for s in fcx2.SUBJECTS}
for s,r in R.items():
    c=r['chans']; san=r['sanity']
    print(s, 'fs',san['fs'],'ntr',san['n_trials_derived'],'correct',int((r['trialinfo'][:,1]==1).sum()), 'offs',{k:v.tolist() for k,v in san['offsets'].items()}, san['overlap_maxdiff'], san['trialinfo_matches_table'], san['trialinfo_same_segments'])
    print('   excl subj', c.label[r['excluded']].tolist(), c.region[r['excluded']].tolist(), 'excl elec', c.label[(np.minimum(r['pow_enc'].p_electrode, r['pow_post'].p_electrode)<.05).to_numpy()].tolist())
    print('   erp sig subj', int(((r['erp_enc'].p_subject<.05)|(r['erp_post'].p_subject<.05)).sum()), 'elec', int(((r['erp_enc'].p_electrode<.05)|(r['erp_post'].p_electrode<.05)).sum()), 'peak', r['peak_band_all'], r['peak_band_dir'], r['peak_band_dir_code'])
U=pd.concat([pd.DataFrame([{k:v for k,v in u.items() if not k.startswith('zf')} for u in r['units']]).assign(subject=s) for s,r in R.items()])
print(U.groupby('system').agg(n=('z_post_mtmfft','size'), main=('z_post_mtmfft',lambda v:(v>1.96).sum()), code=('z_post_code',lambda v:(v>1.96).sum()), prec_main=('z_pre_mtmfft',lambda v:(v>1.96).sum()),prec_code=('z_pre_code',lambda v:(v>1.96).sum()), mpre=('z_pre_mtmfft','mean'), mpost=('z_post_mtmfft','mean'), cpre=('z_pre_code','mean'), cpost=('z_post_code','mean')))
# hg
edges=np.arange(-1.5,3.0001,0.05)
for k in ['pre','encmain','proc']:
    for j in [900,1150]:
        m=np.nanmean([r['sanity']['hg'][(k,j)] for r in R.values()],axis=0)
        print(k,j,' '.join(f'{v:.2f}' for v in m[::2]))
EOF
```

```
s1 fs 1000.0 ntr 111 correct 102 offs {'pre - pre_start': [101.0, 102.0], 'encmain - enc_start': [0.0], 'proc - post_start': [-300.0]} {'pre/encmain': 0.0, 'encmain/proc': 0.0} True True
   excl subj [] [] excl elec ['ROF2', 'ROF8']
   erp sig subj 0 elec 0 peak 1 None 1
s2 fs 1000.0 ntr 113 correct 109 offs {'pre - pre_start': [101.0, 102.0], 'encmain - enc_start': [0.0], 'proc - post_start': [-300.0]} {'pre/encmain': 0.0, 'encmain/proc': 0.0} True True
   excl subj [] [] excl elec ['RC9', 'LAH7', 'LAH8', 'RC12']
   erp sig subj 0 elec 0 peak 2 None 3
s3 fs 1000.0 ntr 115 correct 96 offs {'pre - pre_start': [104.0, 105.0], 'encmain - enc_start': [0.0], 'proc - post_start': [-300.0]} {'pre/encmain': 0.0, 'encmain/proc': 0.0} True True
   excl subj [] [] excl elec []
   erp sig subj 0 elec 0 peak 4 None 4
s4 fs 1000.0 ntr 118 correct 110 offs {'pre - pre_start': [100.0, 101.0], 'encmain - enc_start': [0.0], 'proc - post_start': [-300.0]} {'pre/encmain': 0.0, 'encmain/proc': 0.0} True True
   excl subj [] [] excl elec ['LCI5', 'ROF7', 'LCI7', 'LCI9']
   erp sig subj 0 elec 2 peak 6 None 4
s5 fs 1000.0 ntr 120 correct 95 offs {'pre - pre_start': [105.0, 106.0, 107.0, 108.0], 'encmain - enc_start': [0.0], 'proc - post_start': [-300.0]} {'pre/encmain': 0.0, 'encmain/proc': 0.0} True True
   excl subj ['LTG41'] ['PFC'] excl elec ['LTG17', 'LTG35', 'LTG41', 'OFG8', 'LTG42', 'LTG43', 'LTG44', 'OFG17']
   erp sig subj 1 elec 5 peak 1 None 1
s6 fs 1000.0 ntr 108 correct 103 offs {'pre - pre_start': [98.0, 99.0], 'encmain - enc_start': [0.0], 'proc - post_start': [-300.0]} {'pre/encmain': 0.0, 'encmain/proc': 0.0} True True
   excl subj ['AOF1', 'AOF5', 'POF5', 'FG22', 'FG23'] ['OFC', 'OFC', 'OFC', 'PFC', 'PFC'] excl elec ['AOF1', 'PF3', 'PF6', 'AOF5', 'FG4', 'MOF3', 'FG7', 'MOF4', 'MOF5', 'FG12', 'POF1', 'FG13', 'POF2', 'POF5', 'FG3', 'FG10', 'FG22', 'FG23', 'FG25', 'FG26', 'FG29']
   erp sig subj 0 elec 4 peak 6 None 6
s7 fs 1000.0 ntr 100 correct 100 offs {'pre - pre_start'
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cd entries/crcns-fcx-2-johnson-2018 && timeout 900 python - <<'EOF'
import requests, tarfile, io, h5py, numpy as np, scipy.io as sio
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/data_indiv/s8.tar.gz"
r=requests.get(url, stream=True)
tf=tarfile.open(fileobj=r.raw, mode="r|gz", bufsize=2**20)
for m in tf:
    if m.name.endswith('data_primary.mat'): prim=tf.extractfile(m).read()
    if m.name.endswith('data_derived.mat'): der=tf.extractfile(m).read()
print(prim[:120])
try:
    P=sio.loadmat(io.BytesIO(prim)); print({k:(getattr(v,'shape',None)) for k,v in P.items()})
except NotImplementedError:
    fp=h5py.File(io.BytesIO(prim)); print(list(fp.keys()), {k:fp[k].shape for k in fp.keys() if isinstance(fp[k],h5py.Dataset)})
EOF
```

```
Sun Nov  8 21:40:52 UTC 2026
b'MATLAB 7.3 MAT-file, Platform: GLNXA64, Created on: Thu Feb 22 11:23:18 2018 HDF5 schema 1.00 .                     \x00\x00\x00\x00'
['#refs#', 'elec_labels', 'gdat_clean_filt'] {'elec_labels': (1, 101), 'gdat_clean_filt': (445952, 101)}
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-fcx-2-johnson-2018 && timeout 900 python - <<'EOF'
import requests, tarfile, io, h5py, numpy as np
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/data_indiv/s8.tar.gz"
r=requests.get(url, stream=True)
tf=tarfile.open(fileobj=r.raw, mode="r|gz", bufsize=2**20)
for m in tf:
    if m.name.endswith('data_primary.mat'): prim=tf.extractfile(m).read()
    if m.name.endswith('data_derived.mat'): der=tf.extractfile(m).read()
fp=h5py.File(io.BytesIO(prim)); fd=h5py.File(io.BytesIO(der))
s=lambda f,ref: ''.join(map(chr,f[ref][()].ravel()))
plab=[s(fp,x) for x in fp['elec_labels'][()].ravel()]
G=fp['gdat_clean_filt'][()]  # (samples, ch)
print(plab[:20], G.shape)
g=fd['data_encmain']; dl=[s(fd,x) for x in g['label'][()].ravel()]
tr=fd[g['trial'][0,0]][()]; si=g['sampleinfo'][()].T[0]
print('derived first label', dl[:6], 'sampleinfo', si)
for name in ['CL_02','BR_03','FOAL_04']:
    j=dl.index(name); y=tr[:,j]
    base=name.rsplit('_',1)[0]; num=int(name.rsplit('_',1)[1])
    cands=[c for c in plab if c.startswith(base+'_')]
    a=plab.index(name); 
    nxt=f"{base}_{num+1:02d}"; b=plab.index(nxt) if nxt in plab else None
    x=G[:,a]-G[:,b] if b is not None else G[:,a]
    best=[]
    for start in range(int(si[0])-2000, int(si[0])+2000):
        seg=x[start-1:start-1+len(y)]
        c=np.corrcoef(seg,y)[0,1]
        best.append((c,start))
    best.sort(reverse=True); print(name, nxt, 'best corr,start', best[:2], 'si0', si[0], 'diff', best[0][1]-si[0])
EOF
```

```
['TOL_01', 'TOL_02', 'TOL_03', 'TOL_04', 'TOL_05', 'AL_01', 'AL_02', 'AL_03', 'AL_04', 'AL_05', 'AL_06', 'AL_07', 'AL_08', 'AL_09', 'AL_10', 'AL_11', 'AL_12', 'CL_01', 'CL_02', 'CL_03'] (445952, 101)
derived first label ['TOL_02', 'TOL_03', 'TOL_04', 'TOL_05', 'AL_09', 'AL_10'] sampleinfo [5796. 8099.]
CL_02 CL_03 best corr,start [(np.float64(0.9999999902605177), 5796), (np.float64(0.9874693252832574), 5795)] si0 5796.0 diff 0.0
BR_03 BR_04 best corr,start [(np.float64(0.999999999845671), 5796), (np.float64(0.9776536182663884), 5795)] si0 5796.0 diff 0.0
FOAL_04 FOAL_05 best corr,start [(np.float64(0.5098073425888532), 5810), (np.float64(0.5093670617667965), 5809)] si0 5796.0 diff 14.0
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cd entries/crcns-fcx-2-johnson-2018 && timeout 900 python - <<'EOF' 2>&1 | grep -v Warn
import numpy as np, fcx2
ch=fcx2.read_channel_table()
edges=np.arange(-1.5,3.0001,0.1)
acc={}
for sid in ['s1','s4','s7']:
    c=ch[ch.subject==sid].reset_index(drop=True)
    sub=fcx2.load_subject(sid, c.label.tolist())
    for k in ['encmain','proc','pre']:
        d=sub['seg'][k]; fs=d['fs']
        y=fcx2.lowpass_erp(d['x'], fs, np.arange(d['x'].shape[-1]))
        j=d['trialinfo'][:,4]
        a9=y[j==900].mean(0); a11=y[j==1150].mean(0)
        idx=np.digitize(d['time'],edges)-1
        diff=np.sqrt(((a9-a11)**2).mean(0)); tot=np.sqrt(((y.mean(0)-y.mean(0)[:, :].mean(1,keepdims=True))**2).mean(0))
        # null for diff: split trials randomly
        rng=np.random.default_rng(0); perm=rng.permutation(len(j)); h=len(j)//2
        dn=np.sqrt(((y[perm[:h]].mean(0)-y[perm[h:]].mean(0))**2).mean(0))
        b=lambda v: np.array([v[idx==i].mean() for i in range(len(edges)-1)])
        acc.setdefault(k,[]).append((b(diff)/b(dn).mean(), b(tot)/b(tot).mean()))
for k,v in acc.items():
    d=np.mean([x[0] for x in v],0); t=np.mean([x[1] for x in v],0)
    print(k,'jitter diff/null:', ' '.join(f'{edges[i]:.1f}:{d[i]:.2f}' for i in range(len(d))))
    print(k,'evoked rms     :', ' '.join(f'{edges[i]:.1f}:{t[i]:.2f}' for i in range(len(t))))
EOF
```

```
Sun Nov  8 21:42:00 UTC 2026
encmain jitter diff/null: -1.5:1.03 -1.4:0.99 -1.3:0.93 -1.2:1.13 -1.1:1.04 -1.0:0.94 -0.9:0.97 -0.8:1.19 -0.7:1.08 -0.6:1.16 -0.5:1.14 -0.4:1.02 -0.3:1.26 -0.2:0.92 -0.1:0.95 0.0:1.35 0.1:1.28 0.2:1.00 0.3:1.14 0.4:1.51 0.5:0.85 0.6:1.10 0.7:1.16 0.8:0.99 0.9:0.95 1.0:0.89 1.1:1.22 1.2:1.16 1.3:1.05 1.4:0.94 1.5:1.04 1.6:1.00 1.7:1.05 1.8:1.17 1.9:1.21 2.0:1.00 2.1:0.93 2.2:1.12 2.3:1.05 2.4:1.26 2.5:0.91 2.6:0.92 2.7:0.93 2.8:0.98 2.9:0.82
encmain evoked rms     : -1.5:0.92 -1.4:0.95 -1.3:1.13 -1.2:1.02 -1.1:1.22 -1.0:1.37 -0.9:1.14 -0.8:1.00 -0.7:1.13 -0.6:1.16 -0.5:1.25 -0.4:1.32 -0.3:1.27 -0.2:0.82 -0.1:1.05 0.0:1.12 0.1:1.01 0.2:0.84 0.3:0.91 0.4:0.86 0.5:0.99 0.6:0.88 0.7:0.90 0.8:0.89 0.9:0.97 1.0:0.80 1.1:0.77 1.2:0.88 1.3:0.86 1.4:0.94 1.5:0.92 1.6:0.98 1.7:0.84 1.8:1.06 1.9:1.19 2.0:0.87 2.1:1.00 2.2:1.00 2.3:1.05 2.4:1.08 2.5:1.01 2.6:0.78 2.7:0.91 2.8:1.03 2.9:0.92
proc jitter diff/null: -1.5:0.95 -1.4:0.93 -1.3:0.87 -1.2:0.86 -1.1:0.96 -1.0:0.95 -0.9:0.98 -0.8:1.08 -0.7:0.98 -0.6:1.00 -0.5:0.88 -0.4:1.01 -0.3:1.06 -0.2:1.21 -0.1:1.25 0.0:1.00 0.1:1.27 0.2:1.26 0.3:0.98 0.4:0.91 0.5:1.09 0.6:0.94 0.7:0.99 0.8:0.98 0.9:0.89 1.0:0.96 1.1:0.85 1.2:1.09 1.3:1.14 1.4:1.16 1.5:0.99 1.6:0.95 1.7:0.99 1.8:0.98 1.9:1.13 2.0:0.99 2.1:1.00 2.2:0.94 2.3:1.05 2.4:1.06 2.5:0.94 2.6:1.35 2.7:1.01 2.8:1.08 2.9:0.95
proc evoked rms     : -1.5:0.96 -1.4:1.07 -1.3:0.95 -1.2:0.97 -1.1:1.05 -1.0:1.06 -0.9:1.08 -0.8:0.91 -0.7:0.93 -0.6:0.87 -0.5:1.18 -0.4:1.01 -0.3:0.96 -0.2:1.08 -0.1:1.19 0.0:0.96 0.1:1.19 0.2:1.15 0.3:0.97 0.4:0.82 0.5:1.03 0.6:0.89 0.7:0.80 0.8:0.95 0.9:0.92 1.0:1.21 1.1:1.03 1.2:0.96 1.3:1.21 1.4:1.08 1.5:0.86 1.6:1.06 1.7:0.89 1.8:1.00 1.9:1.00 2.0:0.98 2.1:0.85 2.2:1.01 2.3:0.89 2.4:1.01 2.5:0.98 2.6:0.80 2.7:1.16 2.8:1.02 2.9:1.02
pre jitter diff/null: -1.5:1.11 -1.4:1.21 -1.3:1.00 -1.2:1.00 -1.1:1.22 -1.0:1.02 -0.9:1.03 -0.8:1.16 -0.7:1.05 -0.6:1.09 -0.5:1.05 -0.4:0.98 -0.3:1.13 -0.2:0.95 -0.1:0.99 0.0:1.04 0.1:0.92 0.2:0
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cd entries/crcns-fcx-2-johnson-2018 && timeout 900 python - <<'EOF' 2>&1 | grep -v Warn
import numpy as np, fcx2
from scipy import stats
ch=fcx2.read_channel_table()
edges=np.arange(-1.5,3.0001,0.1)
res={}
for sid in ['s1','s2','s4','s7']:
    c=ch[ch.subject==sid].reset_index(drop=True)
    sub=fcx2.load_subject(sid, c.label.tolist())
    for k in ['encmain','proc']:
        d=sub['seg'][k]; fs=d['fs']
        a=fcx2._filter_chunks(d['x'], fs, np.arange(d['x'].shape[-1]), np.array([[70.,150.]]), "abs")[:,:,0]
        a=np.log(a)
        idx=np.digitize(d['time'],edges)-1
        A=np.stack([a[...,idx==i].mean(-1) for i in range(len(edges)-1)],-1)  # trials, ch, bins
        j=d['trialinfo'][:,4]
        t=stats.ttest_ind(A[j==900],A[j==1150],axis=0).statistic  # ch, bins
        res.setdefault(k,[]).append(t)
        # event-locked rise relative to first 0.3 s
        z=(A-A[...,:3].mean(-1,keepdims=True)).mean(0)
        res.setdefault(k+'rise',[]).append(z)
for k in ['encmain','proc']:
    T=np.concatenate(res[k],0)
    print(k,'n ch',T.shape[0],'frac |t|>2.5 per bin:',' '.join(f'{edges[i]:.1f}:{(np.abs(T[:,i])>2.5).mean():.2f}' for i in range(T.shape[1])))
    Z=np.concatenate(res[k+'rise'],0)
    print(k,'mean log-HG change   :',' '.join(f'{edges[i]:.1f}:{Z[:,i].mean():.2f}' for i in range(Z.shape[1])))
EOF
```

```
Sun Nov  8 21:44:09 UTC 2026
encmain n ch 83 frac |t|>2.5 per bin: -1.5:0.00 -1.4:0.01 -1.3:0.05 -1.2:0.01 -1.1:0.05 -1.0:0.01 -0.9:0.04 -0.8:0.01 -0.7:0.00 -0.6:0.01 -0.5:0.04 -0.4:0.01 -0.3:0.00 -0.2:0.00 -0.1:0.02 0.0:0.02 0.1:0.01 0.2:0.01 0.3:0.01 0.4:0.01 0.5:0.01 0.6:0.01 0.7:0.00 0.8:0.00 0.9:0.02 1.0:0.01 1.1:0.00 1.2:0.00 1.3:0.02 1.4:0.01 1.5:0.01 1.6:0.01 1.7:0.01 1.8:0.06 1.9:0.02 2.0:0.02 2.1:0.02 2.2:0.04 2.3:0.02 2.4:0.02 2.5:0.04 2.6:0.05 2.7:0.08 2.8:0.02 2.9:0.01
encmain mean log-HG change   : -1.5:0.04 -1.4:-0.02 -1.3:-0.02 -1.2:-0.02 -1.1:-0.02 -1.0:-0.02 -0.9:-0.02 -0.8:-0.02 -0.7:-0.01 -0.6:-0.01 -0.5:-0.02 -0.4:-0.02 -0.3:-0.02 -0.2:-0.02 -0.1:-0.02 0.0:-0.01 0.1:-0.02 0.2:-0.01 0.3:-0.01 0.4:-0.01 0.5:-0.02 0.6:-0.01 0.7:-0.01 0.8:-0.01 0.9:-0.01 1.0:-0.01 1.1:-0.01 1.2:-0.02 1.3:-0.01 1.4:-0.02 1.5:-0.01 1.6:-0.02 1.7:-0.02 1.8:-0.01 1.9:-0.02 2.0:-0.01 2.1:-0.02 2.2:-0.01 2.3:-0.01 2.4:-0.01 2.5:-0.01 2.6:-0.01 2.7:-0.01 2.8:-0.02 2.9:0.05
proc n ch 83 frac |t|>2.5 per bin: -1.5:0.01 -1.4:0.01 -1.3:0.02 -1.2:0.00 -1.1:0.01 -1.0:0.00 -0.9:0.00 -0.8:0.00 -0.7:0.00 -0.6:0.02 -0.5:0.02 -0.4:0.00 -0.3:0.01 -0.2:0.02 -0.1:0.05 0.0:0.04 0.1:0.02 0.2:0.04 0.3:0.04 0.4:0.07 0.5:0.05 0.6:0.01 0.7:0.01 0.8:0.00 0.9:0.01 1.0:0.01 1.1:0.01 1.2:0.01 1.3:0.02 1.4:0.00 1.5:0.01 1.6:0.04 1.7:0.00 1.8:0.02 1.9:0.01 2.0:0.00 2.1:0.00 2.2:0.00 2.3:0.01 2.4:0.01 2.5:0.00 2.6:0.01 2.7:0.00 2.8:0.00 2.9:0.01
proc mean log-HG change   : -1.5:0.04 -1.4:-0.02 -1.3:-0.02 -1.2:-0.02 -1.1:-0.02 -1.0:-0.02 -0.9:-0.02 -0.8:-0.03 -0.7:-0.03 -0.6:-0.03 -0.5:-0.02 -0.4:-0.03 -0.3:-0.03 -0.2:-0.03 -0.1:-0.03 0.0:-0.03 0.1:-0.02 0.2:-0.02 0.3:-0.02 0.4:-0.02 0.5:-0.03 0.6:-0.03 0.7:-0.02 0.8:-0.03 0.9:-0.02 1.0:-0.03 1.1:-0.03 1.2:-0.03 1.3:-0.03 1.4:-0.03 1.5:-0.03 1.6:-0.03 1.7:-0.03 1.8:-0.03 1.9:-0.03 2.0:-0.03 2.1:-0.04 2.2:-0.03 2.3:-0.03 2.4:-0.03 2.5:-0.03 2.6:-0.03 2.7:-0.03 2.8:-0.03 2.9:0.04
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='fcx2.py'; s=open(p).read()
s=s.replace('''            o, zc = psi_code(A, the[:, u["amp"]], rng)
            u[f"z_{w}_code"], u[f"raw_{w}_code"] = float(zc.mean()), float(o.mean())
''','''            o, zc = psi_code(A, the[:, u["amp"]], rng)
            u[f"z_{w}_code"], u[f"raw_{w}_code"] = float(zc.mean()), float(o.mean())
            if w == "post":
                u["zf_post_code"] = zc[:16].copy()
''')
s=s.replace('''            rows.append({"effect": e, "df": df, "F": F, "p": stats.f.sf(F, df, res_df)})
        return pd.DataFrame(rows), res_df''','''            rows.append({"effect": e, "df": df, "ss": ss, "F": F, "p": stats.f.sf(F, df, res_df)})
        out = pd.DataFrame(rows)
        out.attrs.update(res_ss=res_ss, res_df=res_df)
        return out, res_df''')
s=s.replace('''            rows.append({"effect": name, "df": df, "F": F, "p": stats.f.sf(F, df, res_df)})
    return pd.DataFrame(rows), res_df''','''            rows.append({"effect": name, "df": df, "ss": ss, "F": F, "p": stats.f.sf(F, df, res_df)})
    out = pd.DataFrame(rows)
    out.attrs.update(res_ss=res_ss, res_df=res_df)
    return out, res_df''')
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && python - <<'EOF'
# test within_unit_anova against statsmodels OLS with unit fixed effects on a small synthetic table
import numpy as np, pandas as pd, fcx2, statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
rng=np.random.default_rng(1)
U,a,b,c=6,2,3,4
Y=rng.normal(size=(U,a,b,c))+rng.normal(size=(U,1,1,1))*3
Y[:,1]+=0.5
tab,dfr=fcx2.within_unit_anova(Y); print(tab.round(4), dfr)
rows=[dict(u=u,A=i,B=j,C=k,y=Y[u,i,j,k]) for u in range(U) for i in range(a) for j in range(b) for k in range(c)]
d=pd.DataFrame(rows)
m=smf.ols('y~C(u)+C(A,Sum)*C(B,Sum)*C(C,Sum)',d).fit()
print(anova_lm(m,typ=3).round(4))
g=np.array([0,0,0,1,1,1]); Y[3:,1]+=1
tab,dfr=fcx2.within_unit_anova(Y,g); print(tab.round(4))
d=pd.DataFrame([dict(u=u,D=g[u],A=i,B=j,C=k,y=Y[u,i,j,k]) for u in range(U) for i in range(a) for j in range(b) for k in range(c)])
m=smf.ols('y~C(u)+C(D,Sum):(C(A,Sum)*C(B,Sum)*C(C,Sum))+C(A,Sum)*C(B,Sum)*C(C,Sum)',d).fit()
print(anova_lm(m,typ=3).round(4))
EOF
```

```
Exit code 1
      effect  df      ss       F       p
0       (0,)   1  7.3882  8.7600  0.0037
1       (1,)   2  1.0021  0.5941  0.5537
2       (2,)   3  1.1555  0.4567  0.7131
3     (0, 1)   2  0.6225  0.3691  0.6922
4     (0, 2)   3  2.5760  1.0181  0.3874
5     (1, 2)   6  4.1628  0.8226  0.5546
6  (0, 1, 2)   6  4.5842  0.9059  0.4933 115
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/patsy/compat.py", line 40, in call_and_wrap_exc
    return f(*args, **kwargs)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/patsy/eval.py", line 179, in eval
    return eval(code, {}, VarLookupDict([inner_namespace] + self._namespaces))
  File "<string>", line 1, in <module>
TypeError: 'Series' object is not callable

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
[... 53 more lines not kept]
```

**Agent**

Column named C clashes with patsy; rename.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && python - <<'EOF' 2>&1 | grep -v Warn
import numpy as np, pandas as pd, fcx2, statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
rng=np.random.default_rng(1)
U,a,b,c=6,2,3,4
Y=rng.normal(size=(U,a,b,c))+rng.normal(size=(U,1,1,1))*3
Y[:,1]+=0.5
tab,dfr=fcx2.within_unit_anova(Y); print(tab[['effect','F','p']].round(4).to_string())
d=pd.DataFrame([dict(u=u,X=i,Z=j,W=k,y=Y[u,i,j,k]) for u in range(U) for i in range(a) for j in range(b) for k in range(c)])
m=smf.ols('y~C(u,Sum)+C(X,Sum)*C(Z,Sum)*C(W,Sum)',d).fit()
print(anova_lm(m,typ=3)[['F','PR(>F)']].round(4))
g=np.array([0,0,0,1,1,1,1]); Y=np.concatenate([Y,Y[:1]+rng.normal(size=(1,a,b,c))]); U=7; Y[3:,1]+=1
tab,dfr=fcx2.within_unit_anova(Y,g); print(tab[['effect','F','p']].round(4).to_string())
d=pd.DataFrame([dict(u=u,D=g[u],X=i,Z=j,W=k,y=Y[u,i,j,k]) for u in range(U) for i in range(a) for j in range(b) for k in range(c)])
m=smf.ols('y~C(u,Sum)+C(D,Sum):C(X,Sum)+C(D,Sum):C(Z,Sum)+C(D,Sum):C(W,Sum)+C(D,Sum):C(X,Sum):C(Z,Sum)+C(D,Sum):C(X,Sum):C(W,Sum)+C(D,Sum):C(Z,Sum):C(W,Sum)+C(D,Sum):C(X,Sum):C(Z,Sum):C(W,Sum)+C(X,Sum)*C(Z,Sum)*C(W,Sum)',d).fit()
print(anova_lm(m,typ=3)[['F','PR(>F)']].round(4))
EOF
```

```
effect       F       p
0       (0,)  8.7600  0.0037
1       (1,)  0.5941  0.5537
2       (2,)  0.4567  0.7131
3     (0, 1)  0.3691  0.6922
4     (0, 2)  1.0181  0.3874
5     (1, 2)  0.8226  0.5546
6  (0, 1, 2)  0.9059  0.4933
                                      F  PR(>F)
Intercept                        2.6853  0.1040
C(u, Sum)                      117.1855  0.0000
C(X, Sum)                        8.7600  0.0037
C(Z, Sum)                        0.5941  0.5537
C(W, Sum)                        0.4567  0.7131
C(X, Sum):C(Z, Sum)              0.3691  0.6922
C(X, Sum):C(W, Sum)              1.0181  0.3874
C(Z, Sum):C(W, Sum)              0.8226  0.5546
C(X, Sum):C(Z, Sum):C(W, Sum)    0.9059  0.4933
Residual                            NaN     NaN
          effect        F       p
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '1,60p' paper/../../../paper/10.1371-journal.pbio.2004274.txt 2>/dev/null | head -5; grep -n "^## " paper/10.1371-journal.pbio.2004274.txt | head -30; ls questions | head; cat attempts/001453-fouke-2025-01.yaml | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\nimport sys\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Johnson et al. (2018) from CRCNS fcx-2\n\n**Paper.** Johnson EL, Adams JN, Solbakk A-K, Endestad T, Larsson PG, Ivanovic J, Meling TR, Lin JJ,\nKnight RT (2018). Dynamic frontotemporal systems process space and time in working memory. *PLoS\nBiology* 16, e2004274. [doi:10.1371/journal.pbio.2004274](https://doi.org/10.1371/journal.pbio.2004274).\nThe claims file was written from the version of record (PMC5895055, full text with Methods and\nfigure legends; the supplementary tables were not supplied).\n\n**Data set.** CRCNS [fcx-2](https://crcns.org/data-sets/pfc/fcx-2),\n[doi:10.6080/K0VX0DQD](https://doi.org/10.6080/K0VX0DQD), read from the public bucket\n`crcnsarchive` under `fcx-2/live/`. CRCNS data sets are not versioned, so the version is recorded\nas `unversioned`. The paper cites the data set by its DOI and no version. The bucket holds the live\nfiles and, under `fcx-2/orig/ver_0_6/`, only the documents and scripts of version 0.6; the data\nfiles exist once, under `live/`, which is the published version 0.61 (descriptor of April 4, 2018,\nwhose change from 0.6 is an updated `psianalysis.m`). This is the only version of the data, so it is\npinned. MD5 sums of the files read, from the data set's `checksums.md5`:\n\n| file | md5 |\n|---|---|\n| data_indiv/s1.tar.gz | 0bbbcce3cc2738bc7ce5545b27843d4c |\n| data_indiv/s2.tar.gz | 5ead31d89d1ae4a50adae20054bb6572 |\n| data_indiv/s3.tar.gz | 740991d34257dabc1fdd8a467f1e80a2 |\n| data_indiv/s4.tar.gz | 306d554f9e9ec77a35b68879f301f6b1 |\n| data_indiv/s5.tar.gz | 66673b1504648aff5ea1f2e0bea6fcdd |\n| data_indiv/s6.tar.gz | 68608a2237469bc285b928298b1e8f3f |\n| data_indiv/s7.tar.gz | 639d8e97e026f9b8dea08610c51af00e |\n| data_indiv/s8.tar.gz | 6aa467667c0fec9566f49fd19c8461e8 |\n| data_indiv/s9.tar.gz | bfd6d72c7663db18db4f0fe90cea63c7 |\n| data_indiv/s10.tar.gz | 5eb078815470c8d1b70b06d8f2be5300 |\n| docs/summary_channel_analysis.csv | 79adb25db44e195ad952359ed43d9a3a |\n| docs/summary_file.csv | 6d214de444bf222cee1c3291b6191a6f |\n| analysis_scripts.tar.gz | 8b5b07094a3a31e8bb4828afcdffd2f2 (read for the methods, not run) |\n\n**What the data set holds.** For each of the 10 subjects, the preprocessed bipolar data\n(`data_derived.mat`: segments `pre`, `encmain` and `proc` with 1.5 s of data on each side, and a\ntrial table per segment), the filtered monopolar data, a per-trial table and electrode\ncoordinates; the analysed channels per region and hemisphere (`summary_channel_analysis.csv`); a\nbehaviour table per subject; and the MATLAB analysis scripts. The tar files are streamed and read\nin memory; only the derived data of the 254 analysed channels are kept.\n\n**Methods.** Everything not in the claims file is taken from the paper's Methods or from the\nanalysis code deposited with the data, as the helper module `fcx2.py` says parameter by parameter.\n\n| claim | tested | rests on an assumption |\n|---|---|---|\n| behavior-proficient | yes | |\n| behavior-no-difficulty-difference | yes | accuracy model on subject-level logits |\n| electrode-counts | yes | |\n| correct-trial-counts | yes | |\n| erp-no-condition-difference | yes | |\n| power-theta-sustained | yes | |\n| power-condition-exclusions | yes | |\n| plv-theta-peak | yes | |\n| psi-theta-shift | yes | |\n| crossspectral-shift | yes | |\n| phase-directing-counts | yes | |\n| crossspectral-equal-strength | yes | unit selection by the code's PSI |\n| theta-peak-bands | yes | |\n| pac-* (8 claims) | yes | unit selection by the code's PSI |\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport warnings\n\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport statsmodels.formula.api as smf\nfrom scipy import stats\n\nimport fcx2\n\nwarnings.filterwarnings(\"ignore\")\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 60)\npd.set_option(\"display.max_rows\", 400)\n\nstarted = time.time()\nchtab = fcx2.read_channel_table()\nsummary = fcx2.read_summary_file()\nR = {}\nfor sid in fcx2.SUBJECTS:\n    R[sid] = fcx2.process_subject(sid, chtab)\nprint(f\"streamed and analysed {len(R)} subjects in {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\nrows = []\nfor sid, r in R.items():\n    s = r[\"sanity\"]\n    ti = r[\"trialinfo\"]\n    rows.append({\n        \"subject\": sid, \"fs\": s[\"fs\"], \"hdr_fs\": sorted(set(s[\"hdr_fs\"].values())),\n        \"derived_labels\": s[\"n_labels\"], \"analysed\": len(r[\"chans\"]),\n        \"trials_table\": len(s[\"trials\"]), \"trials_derived\": s[\"n_trials_derived\"],\n        \"correct_derived\": int((ti[:, 1] == 1).sum()),\n        \"samples_pre\": s[\"n_samples\"][\"pre\"], \"samples_enc\": s[\"n_samples\"][\"encmain\"],\n        \"samples_proc\": s[\"n_samples\"][\"proc\"],\n        \"time_enc\": s[\"time_range\"][\"encmain\"][:2], \"same_start\": all(s[\"same_start\"].values()),\n        \"x_min_uV\": round(s[\"x_range\"][0], 1), \"x_max_uV\": round(s[\"x_range\"][1], 1),\n        \"load_s\": round(s[\"load_s\"]),\n    })\ninfo = pd.DataFrame(rows)\nprint(info.to_string(index=False))\nprint(\"\\nmembers of each tar file:\")\nfor sid, r in R.items():\n    print(sid, {k.split('/')[-1]: v for k, v in r[\"sanity\"][\"members\"].items()})\nprint(\"\\nAll analysed channels of docs/summary_channel_analysis.csv found among the derived labels: yes \"\n      \"(load_subject raises otherwise)\")\nprint(\"Channels per region in the channel table:\", chtab.region.value_counts().to_dict(), \"total\", len(chtab))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe descriptor says the derived structures have `fsample: 1000`; s8 and s9 are at 512 Hz, as its\nnote on the trial table says and as the paper says for the Oslo subjects. Trials differ in length by at\nmost a sample or two within a segment; the analysis keeps the samples all trials share, from the\ncommon first time (-1.5 s).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor sid, r in R.items():\n    s = r[\"sanity\"]\n    rows.append({\"subject\": sid, **{k: np.round(v, 2).tolist()[:4] + ([\"...\"] if len(v) > 4 else []) for k, v in s[\"offsets\"].items()},\n                 \"overlap_maxdiff\": s[\"overlap_maxdiff\"], \"overlap_samples\": s[\"overlap_samples\"],\n                 \"trialinfo_same_in_segments\": s[\"trialinfo_same_segments\"],\n                 \"trialinfo_equals_trial_table\": s[\"trialinfo_matches_table\"]})\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe three derived segments of a trial are cut from one continuous recording: placed by their\n`sampleinfo`, their overlapping samples are identical (largest difference 0) in every subject. In\nnine subjects the first sample of `encmain` is the trial table's column H (\"encoding and pre-cue\ndelay epoch start\"), the first sample of `proc` is 0.3 s before column I (\"post-cue delay epoch\nstart\") and the first sample of `pre` is 0.1 s after column G (\"pretrial epoch start, 1000 ms before\ntrial start\"). In s10 the offsets are not whole samples and vary over trials (the table's columns\nfor s10 are not on the derived data's sample grid; for two trials `pre` is 114 samples after G), so\nfor s10 the table does not place the derived segments exactly. In every subject `trialinfo` is the\nsame in the three segments and equals the trial table's columns, except s10, where the\ntrial-table check fails as printed above.\n\nThis bears on where time 0 is. Each derived segment runs from -1.5 s to 3.0 s, and its first sample\n(-1.5 s) is the table's epoch start. The analysis code takes encoding as [0, 1.5] s of `encmain`, the\npostcue delay as [0.3, 1.2] s of `proc` and the baseline as [0.65, 0.85] s of `pre` (\"-250 to 50 ms\npretrial\"), which places stimulus onset at 0 s, 1.5 s after the table's column H. The descriptor\nplaces stimulus onset at column H itself, 1.5 s earlier. While preparing, a derived trial of s8 was\ncompared with the monopolar data in `data_primary.mat` (not run here, as it streams the primary files):\nthe bipolar `CL_02` and `BR_03` traces equal the difference of adjacent contacts from sample H on\n(correlation 1.0 at zero lag), so `sampleinfo` indexes the primary data as the table does. The\ndata and the code therefore disagree with the descriptor by 1.5 s on where the events are. The\ncheck below looks for task-locked responses to decide between the two.\n\"\"\")\n\ncode(r\"\"\"\nedges = R[\"s1\"][\"sanity\"][\"evoked_edges\"]\ncentres = edges[:-1] + 0.025\nfor seg in (\"pre\", \"encmain\", \"proc\"):\n    hg9 = np.nanmean([r[\"sanity\"][\"hg\"][(seg, 900)] for r in R.values()], axis=0)\n    hg11 = np.nanmean([r[\"sanity\"][\"hg\"][(seg, 1150)] for r in R.values()], axis=0)\n    ev = np.nanmean([r[\"sanity\"][\"evoked_rms\"][seg] / np.nanmean(r[\"sanity\"][\"evoked_rms\"][seg]) for r in R.values()], axis=0)\n    print(f\"{seg}: high-gamma amplitude relative to its mean, 900 ms delay trials, 100 ms steps from -1.5 s:\")\n    print(\"  \", \" \".join(f\"{v:.2f}\" for v in hg9[::2]))\n    print(\"   1150 ms delay trials:\")\n    print(\"  \", \" \".join(f\"{v:.2f}\" for v in hg11[::2]))\n    print(\"   evoked RMS over channels relative to its mean:\")\n    print(\"  \", \" \".join(f\"{v:.2f}\" for v in ev[::2]))\n    print(f\"   range of the high-gamma curves {np.nanmin([hg9, hg11]):.3f} to {np.nanmax([hg9, hg11]):.3f}; \"\n          f\"largest 900 vs 1150 difference {np.nanmax(np.abs(hg9 - hg11)):.3f} at {centres[np.nanargmax(np.abs(hg9 - hg11))]:.2f} s\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nPooled over subjects, the high-gamma amplitude (70 to 150 Hz) and the evoked response show no\ntask-locked modulation large enough to place the stimuli or the test cue: apart from the first\n50 ms bin (the edge of the segment), the curves stay within a few percent of their mean, and the\n900 ms and 1150 ms delay trials do not part at any time. So the clock of the derived data relative\nto the task events could not be established from the data in any subject. The analysis follows the\ntime axes of the derived data, as the deposited code does; the descriptor's placement of the\nevents (1.5 s earlier) is recorded as a finding, and every outcome below rests on the code's\nreading of the time axes.\n\"\"\")\n\ncode(r\"\"\"\n# behaviour tables: the trial table against docs/summary_file.csv\nrows = []\nfor sid, r in R.items():\n    t = r[\"sanity\"][\"trials\"]\n    row = {\"subject\": sid, \"n_trials\": len(t), \"per_condition\": t.condition.value_counts().sort_index().tolist(),\n           \"jitters\": sorted(t.jitter.unique().tolist())}\n    srow = summary.set_index(\"subject\").loc[sid]\n    for c, name in ((1, \"identity\"), (2, \"spatial\"), (3, \"temporal\")):\n        tc = t[t.condition == c]\n        row[f\"acc_{name}\"] = round(tc.accuracy.mean(), 3)\n        row[f\"acc_{name}_doc\"] = srow[f\"acc_{name}\"]\n        row[f\"rt_{name}\"] = round(tc[tc.accuracy == 1].rt.mean(), 1)\n        row[f\"rt_{name}_doc\"] = round(srow[f\"rt_{name}\"], 1)\n    rows.append(row)\nbeh = pd.DataFrame(rows)\nprint(beh.to_string(index=False))\nacc_ok = all(np.isclose(beh[f\"acc_{n}\"], beh[f\"acc_{n}_doc\"], atol=1e-3).all() for n in (\"identity\", \"spatial\", \"temporal\"))\nrt_ok = all(np.isclose(beh[f\"rt_{n}\"], beh[f\"rt_{n}_doc\"], atol=0.5).all() for n in (\"identity\", \"spatial\", \"temporal\"))\nprint(\"\\naccuracy in summary_file.csv equals the trial tables (all 120 trials):\", acc_ok)\nprint(\"response time in summary_file.csv equals the mean over correct trials of the trial tables:\", rt_ok)\nprint(\"subjects' age and sex:\", summary[[\"subject\", \"age\", \"sex\"]].values.tolist())\nprint(f\"age mean {summary.age.mean():.1f} SD {summary.age.std():.1f} range {summary.age.min()}-{summary.age.max()}; males {(summary.sex == 'M').sum()}\")\n# recordings deposited more than once\nsig = {sid: (tuple(r[\"sanity\"][\"trials\"].rt.tolist()), tuple(np.round(r[\"erp_mean\"][\"enc\"][0, :50], 4))) for sid, r in R.items()}\ndups = [(a, b) for i, a in enumerate(sig) for b in list(sig)[i + 1:] if sig[a][0] == sig[b][0] or sig[a][1] == sig[b][1]]\nprint(\"subjects with identical response-time sequences or identical evoked traces:\", dups or \"none\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe behaviour table in `docs/summary_file.csv` agrees with the per-trial tables (accuracy over all\n120 trials, response time over correct trials), and age and sex match the paper's description (37\n± 13 years, 22 to 69, 7 males) as printed. No subject's data appear twice.\n\"\"\")\n\n# ---------------------------------------------------------------- claims\nmd(r\"\"\"\n## behavior-proficient\n\n> All ten subjects performed the task well above chance, with accuracy from 0.79 to 0.97 (chance\n> 0.5).\n\"\"\")\ncode(r\"\"\"\nacc_all = {sid: r[\"sanity\"][\"trials\"].accuracy.mean() for sid, r in R.items()}\nacc_kept = {sid: (r[\"trialinfo\"][:, 1] == 1).mean() for sid, r in R.items()}\ntab = pd.DataFrame({\"all_120_trials\": acc_all, \"kept_trials\": acc_kept}).round(3)\nprint(tab.to_string())\nfor col in tab:\n    v = tab[col]\n    print(f\"{col}: min {v.min():.3f} (expected 0.79 +- 0.079), max {v.max():.3f} (expected 0.97 +- 0.097), \"\n          f\"all in [0.711, 1.0]: {bool(((v >= 0.711) & (v <= 1.0)).all())}; \"\n          f\"min ok {abs(v.min() - 0.79) <= 0.079}, max ok {abs(v.max() - 0.97) <= 0.097}\")\n\"\"\", tags=[\"claim:behavior-proficient\"])\nmd(r\"\"\"\n**Result: reproduced.** Over all 120 trials (reading a) accuracy runs from the printed minimum to the\nprinted maximum, every subject inside 0.711 to 1.0, and both bounds within tolerance of 0.79 and\n0.97; reading (b) on the kept trials is printed alongside.\n\"\"\")\n\nmd(r\"\"\"\n## behavior-no-difficulty-difference\n\n> Accuracy and correct-trial response time did not differ between the identity, spatial and\n> temporal conditions (mean accuracy 0.90, 0.92, 0.89; mean response time 1659, 1335, 1475 ms).\n\nThe models are fitted on one value per subject and condition (30 rows), as the paper's F(1,28)\nimplies; accuracy enters as the empirical logit, log((k + 0.5) / (n - k + 0.5)), as some subjects\nare at 100% in a condition (an assumption: the paper's \"logit mixed-effects model\" is not\nspecified further). Readings: (a) each relation condition against identity, (b) one 3-level\ncondition term (Wald test), and as a variant condition as a numeric 1-2-3 term, which has the\npaper's single numerator degree of freedom. A trial-level variant of response time (all correct\ntrials, subject random intercept) is shown too.\n\"\"\")\ncode(r\"\"\"\ndef behaviour_rows(kept):\n    rows = []\n    for sid, r in R.items():\n        if kept:\n            ti = r[\"trialinfo\"]\n            t = pd.DataFrame({\"accuracy\": ti[:, 1], \"condition\": ti[:, 3], \"rt\": ti[:, 5]})\n        else:\n            t = r[\"sanity\"][\"trials\"]\n        for c in (1, 2, 3):\n            tc = t[t.condition == c]\n            k, n = tc.accuracy.sum(), len(tc)\n            rows.append({\"subject\": sid, \"cond\": c, \"acc\": k / n, \"k\": k, \"n\": n,\n                         \"elogit\": np.log((k + 0.5) / (n - k + 0.5)), \"rt\": tc[tc.accuracy == 1].rt.mean()})\n    return pd.DataFrame(rows)\n\n\ndef lmm_tests(d, y):\n    out = {}\n    m = smf.mixedlm(f\"{y} ~ C(cond)\", d, groups=d[\"subject\"]).fit(reml=True)\n    out[\"spatial_vs_identity_p\"] = m.pvalues[\"C(cond)[T.2]\"]\n    out[\"temporal_vs_identity_p\"] = m.pvalues[\"C(cond)[T.3]\"]\n    w = m.wald_test(\"C(cond)[T.2] = 0, C(cond)[T.3] = 0\", scalar=True)\n    out[\"three_level_chi2\"], out[\"three_level_p\"] = float(w.statistic), float(w.pvalue)\n    mn = smf.mixedlm(f\"{y} ~ cond\", d, groups=d[\"subject\"]).fit(reml=True)\n    out[\"numeric_z\"], out[\"numeric_p\"] = mn.tvalues[\"cond\"], mn.pvalues[\"cond\"]\n    return out\n\n\nfor kept in (False, True):\n    d = behaviour_rows(kept)\n    label = \"kept trials (b)\" if kept else \"all 120 trials (a)\"\n    means = d.groupby(\"cond\")[[\"acc\", \"rt\"]].agg([\"mean\", \"std\"]).round(3)\n    print(f\"--- {label}: mean and SD over subjects\\n{means.to_string()}\")\n    for y in (\"elogit\", \"rt\"):\n        print(f\"  {y}:\", {k: round(v, 4) for k, v in lmm_tests(d, y).items()})\nrows = []\nfor sid, r in R.items():\n    t = r[\"sanity\"][\"trials\"]\n    t = t[t.accuracy == 1]\n    rows += [{\"subject\": sid, \"cond\": c, \"rt\": v} for c, v in zip(t.condition, t.rt)]\ndt = pd.DataFrame(rows)\nmt = smf.mixedlm(\"rt ~ C(cond)\", dt, groups=dt[\"subject\"]).fit()\nw = mt.wald_test(\"C(cond)[T.2] = 0, C(cond)[T.3] = 0\", scalar=True)\nprint(\"trial-level response time variant: p spatial\", round(mt.pvalues[\"C(cond)[T.2]\"], 4), \"p temporal\",\n      round(mt.pvalues[\"C(cond)[T.3]\"], 4), \"3-level p\", round(float(w.pvalue), 4))\nd = behaviour_rows(False)\nexp = {1: (0.90, 0.04, 1659, 701), 2: (0.92, 0.09, 1335, 574), 3: (0.89, 0.09, 1475, 734)}\nfor c, (a, ta, rt, trt) in exp.items():\n    ma, mr = d[d.cond == c].acc.mean(), d[d.cond == c].rt.mean()\n    print(f\"condition {c}: accuracy {ma:.3f} vs {a} +- {ta}: {abs(ma - a) <= ta}; rt {mr:.0f} vs {rt} +- {trt}: {abs(mr - rt) <= trt}\")\n\"\"\", tags=[\"claim:behavior-no-difficulty-difference\"])\nmd(r\"\"\"\n**Result: not reproduced.** The means are within the paper's SDs (printed above), but under reading\n(a) the accuracy model finds a condition effect at p < 0.05, so the paper's test finds a difference\n(the printed p-values for each reading and the numeric-term variant show which). See the record for\nthe numbers under each reading.\n\"\"\")\n\nmd(r\"\"\"\n## electrode-counts\n\n> After bipolar rereferencing there were 254 electrodes, 36 MTL, 116 lateral PFC and 102 OFC; MTL\n> and PFC were covered in the same hemisphere in 9 of 10 subjects and MTL and OFC in 7 of 10.\n\"\"\")\ncode(r\"\"\"\ncnt = chtab.region.value_counts()\nprint(\"electrodes per region:\", cnt.to_dict(), \"total\", len(chtab))\nper = chtab.groupby([\"subject\", \"region\", \"hemi\"]).size().unstack([\"region\", \"hemi\"]).fillna(0).astype(int)\nprint(per.to_string())\ndef same_hemi(a, b):\n    return sum(any(((chtab.subject == s) & (chtab.region == a) & (chtab.hemi == h)).any() and\n                   ((chtab.subject == s) & (chtab.region == b) & (chtab.hemi == h)).any() for h in \"LR\")\n               for s in fcx2.SUBJECTS)\nn_pfc, n_ofc = same_hemi(\"MTL\", \"PFC\"), same_hemi(\"MTL\", \"OFC\")\nprint(\"subjects with MTL and PFC in one hemisphere:\", n_pfc, \"(expected 9)\")\nprint(\"subjects with MTL and OFC in one hemisphere:\", n_ofc, \"(expected 7)\")\npr = chtab.groupby([\"subject\", \"region\"]).size().unstack().fillna(0)\nfor reg in (\"MTL\", \"PFC\", \"OFC\"):\n    v = pr[reg][pr[reg] > 0]\n    print(f\"{reg} per subject with any: mean {pr[reg].mean():.1f} SD {pr[reg].std():.1f}; range {int(v.min())}-{int(v.max())} in {len(v)} subjects\")\n\"\"\", tags=[\"claim:electrode-counts\"])\nmd(r\"\"\"\n**Result: reproduced.** The channel table lists 36 MTL, 116 PFC and 102 OFC electrodes (254), and\nthe same-hemisphere subject counts are 9 and 7, as printed.\n\"\"\")\n\nmd(r\"\"\"\n## correct-trial-counts\n\n> The final data held on average 100 correct trials per subject, 33 +- 3 identity (26 to 37), 34 +- 4\n> spatial (28 to 39) and 33 +- 3 temporal (28 to 37), and 10 +- 8 incorrect trials (0 to 25).\n\"\"\")\ncode(r\"\"\"\nrows = []\nfor sid, r in R.items():\n    ti = r[\"trialinfo\"]\n    c = ti[:, 1] == 1\n    rows.append({\"subject\": sid, \"correct\": int(c.sum()), \"identity\": int((c & (ti[:, 3] == 1)).sum()),\n                 \"spatial\": int((c & (ti[:, 3] == 2)).sum()), \"temporal\": int((c & (ti[:, 3] == 3)).sum()),\n                 \"incorrect\": int((~c).sum()), \"kept\": len(ti)})\ntc = pd.DataFrame(rows).set_index(\"subject\")\nprint(tc.to_string())\nprint(tc.agg([\"mean\", \"std\", \"min\", \"max\"]).round(2).to_string())\nchecks = {\"correct\": (100, 10, None), \"identity\": (33, 3, (26, 37)), \"spatial\": (34, 4, (28, 39)),\n          \"temporal\": (33, 3, (28, 37)), \"incorrect\": (10, 8, (0, 25))}\nfor k, (v, tol, rg) in checks.items():\n    m = tc[k].mean()\n    line = f\"{k}: mean {m:.1f} vs {v} +- {tol}: {abs(m - v) <= tol}\"\n    if rg:\n        lo, hi = rg[0] - 0.1 * rg[0], rg[1] + 0.1 * rg[1]\n        line += f\"; all subjects in [{lo:.1f}, {hi:.1f}]: {bool(((tc[k] >= lo) & (tc[k] <= hi)).all())}\"\n    print(line)\n\"\"\", tags=[\"claim:correct-trial-counts\"])\nmd(r\"\"\"\n**Result: reproduced.** Every mean is within the paper's SD and every subject's per-condition count is\ninside the widened ranges, as printed.\n\"\"\")\n\nmd(r\"\"\"\n## erp-no-condition-difference\n\n> ERPs did not differ between identity, spatial and temporal conditions in any electrode, over\n> encoding, precue or postcue intervals.\n\nThe test is run per subject as `erp_compute.m` does (all of a subject's analysed electrodes in one\ntest, so the null is the largest cluster over the subject's electrodes), and per electrode (the\nMethods' \"clustered per electrode\") as a variant.\n\"\"\")\ncode(r\"\"\"\nrows = []\nfor sid, r in R.items():\n    for test in (\"erp_enc\", \"erp_post\"):\n        d = r[test]\n        rows.append({\"subject\": sid, \"test\": test, \"n_el\": len(d), \"sig_subject_null\": int((d.p_subject < 0.05).sum()),\n                     \"sig_electrode_null\": int((d.p_electrode < 0.05).sum()), \"min_p_subject\": round(d.p_subject.min(), 3),\n                     \"min_p_electrode\": round(d.p_electrode.min(), 3)})\nerp = pd.DataFrame(rows)\nprint(erp.to_string(index=False))\nn_el = len(chtab)\nfor col in (\"sig_subject_null\", \"sig_electrode_null\"):\n    sig_any = sum(int(((R[s][\"erp_enc\"].p_subject if col == \"sig_subject_null\" else R[s][\"erp_enc\"].p_electrode) < 0.05).to_numpy().__or__(\n        ((R[s][\"erp_post\"].p_subject if col == \"sig_subject_null\" else R[s][\"erp_post\"].p_electrode) < 0.05).to_numpy()).sum()) for s in R)\n    print(f\"{col}: electrodes with a significant cluster in either test: {sig_any} of {n_el}\")\nprint(f\"expected false positives at alpha 0.05 over {n_el} electrodes and two tests, per-electrode null: {0.05 * 2 * n_el:.1f}\")\n\"\"\", tags=[\"claim:erp-no-condition-difference\"])\nmd(r\"\"\"\n**Result: see the record.** The outcome follows the paper's test as the code runs it (subject-wide null):\nthe counts of electrodes with a significant cluster are printed above.\n\"\"\")\n\nmd(r\"\"\"\n## power-theta-sustained\n\n> Task-induced power showed sustained theta band (3 to 7 Hz) activity in MTL, PFC and OFC over\n> encoding and delay, with transient activity above 16 Hz, and alpha (8 to 13 Hz) desynchronized in\n> the MTL.\n\nTheta is the four filters centred at 3.5 to 6.5 Hz; alpha the three centred at 8 to 11.5 Hz. Time\npoints: the 31 points of encoding and precue (0 to 1.5 s) and the 19 of the postcue delay, at 50 ms.\nAll 254 analysed electrodes (the claim is about the power before the exclusions).\n\"\"\")\ncode(r\"\"\"\nTH = [2, 3, 4, 5]\nAL = [6, 7, 8]\nHI = [i for i, c in enumerate(fcx2.CENTRES) if c > 16]\n\n\ndef zcurve(r, idx, bands):\n    zs = np.concatenate([r[\"power_z_mean\"][\"enc\"][idx][:, bands].mean(axis=1),\n                         r[\"power_z_mean\"][\"post\"][idx][:, bands].mean(axis=1)], axis=-1)\n    return zs                                                # (electrodes, 50 time points)\n\n\nrows, el_rows = [], []\nfor sid, r in R.items():\n    c = r[\"chans\"]\n    for reg in (\"MTL\", \"PFC\", \"OFC\"):\n        idx = np.where(c.region == reg)[0]\n        if len(idx) == 0:\n            continue\n        th = zcurve(r, idx, TH)\n        al = zcurve(r, idx, AL)\n        hi = np.concatenate([r[\"power_z_mean\"][\"enc\"][idx][:, [h for h in HI if h < r[\"power_z_mean\"][\"enc\"].shape[1]]],\n                             r[\"power_z_mean\"][\"post\"][idx][:, [h for h in HI if h < r[\"power_z_mean\"][\"post\"].shape[1]]]], axis=-1)\n        rows.append({\"subject\": sid, \"region\": reg, \"n\": len(idx),\n                     \"theta_frac_above\": (th.mean(axis=0) > 1.96).mean(), \"theta_median_z\": np.median(th.mean(axis=0)),\n                     \"alpha_frac_below\": (al.mean(axis=0) < -1.96).mean(), \"alpha_median_z\": np.median(al.mean(axis=0)),\n                     \"el_theta_sustained\": ((th > 1.96).mean(axis=1) >= 0.5).mean(),\n                     \"el_alpha_desync\": ((al < -1.96).mean(axis=1) >= 0.5).mean(),\n                     \"el_any_high_above\": int((hi > 1.96).any(axis=(1, 2)).sum()),\n                     \"theta_z_range\": (round(th.min(), 1), round(th.max(), 1))})\npw = pd.DataFrame(rows)\nprint(pw.round(3).to_string(index=False))\nfor reg in (\"MTL\", \"PFC\", \"OFC\"):\n    d = pw[pw.region == reg]\n    print(f\"{reg}: (a) subjects with region-average theta z > 1.96 at >= half the time points: {(d.theta_frac_above >= 0.5).sum()} of {len(d)}; \"\n          f\"(b) electrodes meeting the rule: {np.sum(d.el_theta_sustained * d.n):.0f} of {d.n.sum()}\")\nd = pw[pw.region == \"MTL\"]\nprint(f\"MTL alpha: (a) subjects with alpha z < -1.96 at >= half the time points: {(d.alpha_frac_below >= 0.5).sum()} of {len(d)}; \"\n      f\"(b) electrodes {np.sum(d.el_alpha_desync * d.n):.0f} of {d.n.sum()}\")\nprint(\"electrodes with any z > 1.96 above 16 Hz:\", int(pw.el_any_high_above.sum()), \"of\", int(pw.n.sum()))\n\"\"\", tags=[\"claim:power-theta-sustained\"])\nmd(r\"\"\"\n**Result: see the record.** The counts of subjects and electrodes meeting the claim's rule are printed\nabove for each region.\n\"\"\")\n\nmd(r\"\"\"\n## power-condition-exclusions\n\n> Power did not differ between conditions at any time and frequency in 246 of 254 electrodes; the 8\n> that differed (5 PFC and 3 OFC, in 4 of 10 subjects) were excluded from further analysis.\n\nThe baseline z is an affine map of power per electrode and frequency, shared by all trials, so the t\nand F statistics, and the test, are the same on z and on raw power (readings a and b of the claim\ngive one result).\n\"\"\")\ncode(r\"\"\"\nrows = []\nfor sid, r in R.items():\n    c = r[\"chans\"]\n    for null in (\"p_subject\", \"p_electrode\"):\n        sig = (np.minimum(r[\"pow_enc\"][null], r[\"pow_post\"][null]) < 0.05).to_numpy()\n        for i in np.where(sig)[0]:\n            rows.append({\"null\": null, \"subject\": sid, \"label\": c.label[i], \"region\": c.region[i],\n                         \"p_enc\": round(r[\"pow_enc\"][null][i], 3), \"p_post\": round(r[\"pow_post\"][null][i], 3)})\nex = pd.DataFrame(rows)\nprint(ex.to_string(index=False))\nfor null in (\"p_subject\", \"p_electrode\"):\n    d = ex[ex.null == null]\n    print(f\"{null}: {len(d)} electrodes ({d.region.value_counts().to_dict()}) in {d.subject.nunique()} subjects; expected 8 (5 PFC, 3 OFC) in 4\")\n\"\"\", tags=[\"claim:power-condition-exclusions\"])\nmd(r\"\"\"\n**Result: see the record.** The counts under the code's subject-wide null and under the per-electrode\nnull are printed above; the subject-wide set is excluded from the analyses that follow.\n\"\"\")\n\nmd(r\"\"\"\n## plv-theta-peak\n\n> Phase-locking values over the delays peaked in the theta band within the MTL and between MTL and\n> frontal (PFC and OFC) electrodes, with broader synchrony in the alpha range.\n\nReadings: (a) imaginary PLV, |Im(mean over trials of exp(i(phi1 - phi2)))|; (b) the phase-lag index;\nand the code's own form (`plvanalysis.m`: the PLV of the imaginary parts of the analytic signals\ntaken as angles) as a variant. Spectra are averaged over time and over the two delays; a peak is a\nfilter centred at 3.5 to 6.5 Hz larger than both neighbours.\n\"\"\")\ncode(r\"\"\"\ncent = fcx2.CENTRES[fcx2.PLV_BANDS]\nprint(\"filter centres:\", cent.tolist())\nrows = []\nfor sid, r in R.items():\n    for g in (\"MTL-MTL\", \"MTL-PFC\", \"MTL-OFC\"):\n        if len(r[\"pairs\"][g]) == 0:\n            continue\n        for rd in (\"implv\", \"pli\", \"code\"):\n            spec = (r[\"plv\"][\"pre\"][g][rd].mean(axis=0) + r[\"plv\"][\"post\"][g][rd].mean(axis=0)) / 2\n            peaks = [cent[i] for i in range(1, len(spec) - 1) if spec[i] > spec[i - 1] and spec[i] > spec[i + 1]]\n            rows.append({\"subject\": sid, \"group\": g, \"reading\": rd, \"pairs\": len(r[\"pairs\"][g]),\n                         \"theta_peak\": any(3 <= p <= 7 for p in peaks), \"peaks_Hz\": peaks,\n                         \"max_at_Hz\": cent[int(np.argmax(spec))], \"alpha_over_theta\": spec[7:9].mean() / spec[2:6].mean(),\n                         \"spectrum\": np.round(spec / spec.max(), 2).tolist()})\npl = pd.DataFrame(rows)\nprint(pl.drop(columns=\"spectrum\").to_string(index=False))\nprint(pl.groupby([\"reading\", \"group\"]).theta_peak.agg([\"sum\", \"size\"]).to_string())\nprint(pl[pl.reading == \"implv\"][[\"subject\", \"group\", \"spectrum\"]].to_string(index=False))\n\"\"\", tags=[\"claim:plv-theta-peak\"])\nmd(r\"\"\"\n**Result: see the record.** The number of subjects with a theta peak, per group and reading, is\nprinted above.\n\"\"\")\n\nmd(r\"\"\"\n## psi-theta-shift\n\n> Theta-band PSI showed frontal-to-MTL leads during the precue delay and shifted toward MTL leads (a\n> bidirectional network) after the test cue, for MTL to PFC and MTL to OFC pairs.\n\nReadings of the spectral step: the code's single Hanning window (`mtmfft`, main), sliding 3-cycle\nwindows (Methods), and the code's own form of PSI (`psianalysis.m`, per-trial PSI against a null\nof trial-mean coherency). Readings of M7: the response is the PSI z or the raw PSI. Positive PSI\nmeans the MTL leads.\n\"\"\")\ncode(r\"\"\"\ndef pair_table(key):\n    rows = []\n    for sid, r in R.items():\n        for g in (\"MTL-PFC\", \"MTL-OFC\"):\n            for a, b in r[\"pairs\"][g]:\n                for w in (\"pre\", \"post\"):\n                    d = r[\"psi\"][(w, key)]\n                    rows.append({\"subject\": sid, \"net\": g, \"pair\": f\"{sid}-{a}-{b}\", \"interval\": w,\n                                 \"z\": d[\"z\"][a, b], \"raw\": d[\"raw\"][a, b]})\n    return pd.DataFrame(rows)\n\n\ndef lmm_interval(d, y):\n    d = d.copy()\n    d[\"post\"] = (d.interval == \"post\").astype(float)\n    m = smf.mixedlm(f\"{y} ~ post\", d, groups=d[\"subject\"], vc_formula={\"pair\": \"0 + C(pair)\"}).fit(reml=True)\n    return m.params[\"post\"], m.tvalues[\"post\"], m.pvalues[\"post\"]\n\n\nrows = []\nfor key in (\"mtmfft\", \"sliding\", \"code\"):\n    pt = pair_table(key)\n    for g in (\"MTL-PFC\", \"MTL-OFC\"):\n        d = pt[pt.net == g]\n        pre = d[d.interval == \"pre\"]\n        post = d[d.interval == \"post\"]\n        for y in (\"z\", \"raw\"):\n            b, t, p = lmm_interval(d, y)\n            rows.append({\"reading\": key, \"net\": g, \"pairs\": len(pre), \"subjects\": pre.subject.nunique(), \"response\": y,\n                         \"pre_mean_z\": pre.z.mean(), \"pre_below\": int((pre.z < -1.96).sum()), \"pre_above\": int((pre.z > 1.96).sum()),\n                         \"post_mean_z\": post.z.mean(), \"post_below\": int((post.z < -1.96).sum()), \"post_above\": int((post.z > 1.96).sum()),\n                         \"post_minus_pre\": b, \"t\": t, \"p\": p})\nps = pd.DataFrame(rows)\nprint(ps.round(4).to_string(index=False))\nprint(\"expected pairs: MTL-PFC 172 +- 17.2, MTL-OFC 303 +- 30.3\")\n\"\"\", tags=[\"claim:psi-theta-shift\"])\nmd(r\"\"\"\n**Result: see the record.** Part (1) and part (2) of the criterion are printed for every reading.\n\"\"\")\n\nmd(r\"\"\"\n## crossspectral-shift\n\n> Theta phase to amplitude directionality (cross-spectral PSI) was absent in the precue delay and\n> shifted to theta phase leading amplitude after the test cue, within MTL, PFC and OFC and in all four\n> interregional directions.\n\nReadings: the PSI of the Methods (Nolte et al. 2008) from the code's single window (main), and the\ncode's own form of PSI as a variant; M7 response z or raw.\n\"\"\")\ncode(r\"\"\"\nunits = []\nfor sid, r in R.items():\n    for i, u in enumerate(r[\"units\"]):\n        units.append({\"subject\": sid, \"uid\": f\"{sid}-{u['ph']}-{u['amp']}\", \"pair\": f\"{sid}-{min(u['ph'], u['amp'])}-{max(u['ph'], u['amp'])}\",\n                      \"idx\": i, **{k: v for k, v in u.items() if not k.startswith(\"zf\")}})\nU = pd.DataFrame(units)\nSYSTEMS = [\"MTL\", \"PFC\", \"OFC\", \"MTL->PFC\", \"PFC->MTL\", \"MTL->OFC\", \"OFC->MTL\"]\nrows = []\nfor key in (\"mtmfft\", \"code\"):\n    for sname in SYSTEMS:\n        d = U[U.system == sname]\n        long = pd.concat([pd.DataFrame({\"subject\": d.subject, \"pair\": d.uid, \"interval\": w,\n                                        \"z\": d[f\"z_{w}_{key}\"], \"raw\": d[f\"raw_{w}_{key}\"]}) for w in (\"pre\", \"post\")])\n        for y in (\"z\", \"raw\"):\n            b, t, p = lmm_interval(long, y)\n            rows.append({\"reading\": key, \"system\": sname, \"units\": len(d), \"subjects\": d.subject.nunique(), \"response\": y,\n                         \"pre_mean_z\": d[f\"z_pre_{key}\"].mean(), \"post_mean_z\": d[f\"z_post_{key}\"].mean(),\n                         \"pre_above_1.96\": int((d[f\"z_pre_{key}\"] > 1.96).sum()),\n                         \"pre_frac_above\": (d[f\"z_pre_{key}\"] > 1.96).mean(), \"post_minus_pre\": b, \"t\": t, \"p\": p})\ncx = pd.DataFrame(rows)\nprint(cx.round(4).to_string(index=False))\nprint(\"expected electrodes in the models: MTL 36 +- 3.6, PFC 111 +- 11.1, OFC 99 +- 9.9\")\nfor key in (\"mtmfft\", \"code\"):\n    for y in (\"z\", \"raw\"):\n        d = cx[(cx.reading == key) & (cx.response == y)]\n        print(f\"{key}/{y}: systems with post > pre at p < 0.05: {int(((d.post_minus_pre > 0) & (d.p < 0.05)).sum())} of 7; \"\n              f\"systems with at most 5% precue units above 1.96: {int((d['pre_frac_above'] <= 0.05).sum())} of 7\")\n\"\"\", tags=[\"claim:crossspectral-shift\"])\nmd(r\"\"\"\n**Result: see the record.** The number of systems meeting each part of the criterion is printed for\nevery reading.\n\"\"\")\n\nmd(r\"\"\"\n## phase-directing-counts\n\n> In the postcue delay, theta phase significantly led higher-frequency amplitude in 13 MTL, 52 PFC\n> and 38 OFC electrodes, and in 56 MTL to PFC, 85 PFC to MTL, 93 MTL to OFC and 115 OFC to MTL\n> electrode pairs.\n\"\"\")\ncode(r\"\"\"\nEXP = {\"MTL\": 13, \"PFC\": 52, \"OFC\": 38, \"MTL->PFC\": 56, \"PFC->MTL\": 85, \"MTL->OFC\": 93, \"OFC->MTL\": 115}\nEXP_SUBJ = {\"MTL\": 8, \"PFC\": 8, \"OFC\": 8, \"MTL->PFC\": 9, \"PFC->MTL\": 9, \"MTL->OFC\": 5, \"OFC->MTL\": 5}\nrows = []\nfor key in (\"mtmfft\", \"code\"):\n    for sname in SYSTEMS:\n        d = U[(U.system == sname) & (U[f\"z_post_{key}\"] > 1.96)]\n        rows.append({\"reading\": key, \"system\": sname, \"count\": len(d), \"expected\": EXP[sname],\n                     \"within_10pct\": abs(len(d) - EXP[sname]) <= 0.1 * EXP[sname],\n                     \"subjects\": d.subject.nunique(), \"expected_subjects\": EXP_SUBJ[sname],\n                     \"per_subject\": d.subject.value_counts().to_dict()})\npdc = pd.DataFrame(rows)\nprint(pdc.to_string(index=False))\nprint(pdc.groupby(\"reading\").within_10pct.sum().to_string())\n\"\"\", tags=[\"claim:phase-directing-counts\"])\nmd(r\"\"\"\n**Result: not reproduced.** With the PSI of the Methods no unit passes z > 1.96; with the code's form\nthe counts are of the paper's order but most fall outside 10%, as printed.\n\"\"\")\n\nmd(r\"\"\"\n## crossspectral-equal-strength\n\n> Among phase-directing pairs, the strength of theta phase directionality did not differ across\n> amplitude frequencies or between the MTL to frontal and frontal to MTL directions.\n\nThe PSI of the Methods selects no pairs, so the phase-directing pairs are those of the code's form of\nPSI (an assumption, see the record), and the per-frequency z is the code's. Frequency (16 levels) is\nwithin pair, direction between pairs. With random intercepts and every pair having all 16\nfrequencies, the mixed model's tests of frequency and frequency x direction are the within-pair F\ntests computed by `fcx2.within_unit_anova`; the direction main effect is tested on the pair means\nwith a subject random intercept.\n\"\"\")\ncode(r\"\"\"\nZF = {}\nfor sid, r in R.items():\n    for i, u in enumerate(r[\"units\"]):\n        ZF[(sid, i)] = u.get(\"zf_post_code\")\n\n\ndef direction_tests(d, Y, groups):\n    tab, res_df = fcx2.within_unit_anova(Y, groups)\n    m = pd.DataFrame({\"y\": Y.reshape(len(Y), -1).mean(axis=1), \"dir\": groups, \"subject\": d.subject.to_numpy()})\n    md_ = smf.mixedlm(\"y ~ dir\", m, groups=m[\"subject\"]).fit(reml=True)\n    return tab, res_df, md_.params[\"dir\"], md_.pvalues[\"dir\"]\n\n\nfor net, (a, b) in {\"MTL-PFC\": (\"MTL->PFC\", \"PFC->MTL\"), \"MTL-OFC\": (\"MTL->OFC\", \"OFC->MTL\")}.items():\n    d = U[U.system.isin([a, b]) & (U.z_post_code > 1.96)]\n    Y = np.stack([ZF[(s, i)][:16] for s, i in zip(d.subject, d.idx)])\n    g = (d.system == b).astype(int).to_numpy()\n    tab, res_df, bdir, pdir_ = direction_tests(d, Y, g)\n    ss_f, ss_df_ = tab.loc[0, \"ss\"], tab.loc[1, \"ss\"]\n    res_ss = tab.attrs[\"res_ss\"]\n    F_main = (ss_f / 15) / ((res_ss + ss_df_) / (res_df + 15))\n    print(f\"{net}: {len(d)} pairs ({(g == 0).sum()} {a}, {(g == 1).sum()} {b}) in {d.subject.nunique()} subjects\")\n    print(f\"  (b) with interaction: frequency F(15,{res_df}) = {tab.loc[0, 'F']:.2f}, p = {tab.loc[0, 'p']:.3g}; \"\n          f\"frequency x direction F = {tab.loc[1, 'F']:.2f}, p = {tab.loc[1, 'p']:.3g}\")\n    print(f\"  (a) main effects only: frequency F(15,{res_df + 15}) = {F_main:.2f}, p = {stats.f.sf(F_main, 15, res_df + 15):.3g}\")\n    print(f\"  direction (pair means, subject random intercept): {b} minus {a} = {bdir:.3f}, p = {pdir_:.3g}\")\n    print(\"  mean z per frequency:\", np.round(Y.mean(axis=0), 2).tolist())\nfor reg in (\"MTL\", \"PFC\", \"OFC\"):\n    d = U[(U.system == reg) & (U.z_post_code > 1.96)]\n    if len(d) < 2:\n        print(reg, \"local variant: fewer than 2 electrodes\")\n        continue\n    Y = np.stack([ZF[(s, i)][:16] for s, i in zip(d.subject, d.idx)])\n    tab, res_df = fcx2.within_unit_anova(Y)\n    print(f\"local variant {reg}: {len(d)} electrodes, frequency F(15,{res_df}) = {tab.loc[0, 'F']:.2f}, p = {tab.loc[0, 'p']:.3g}\")\n\"\"\", tags=[\"claim:crossspectral-equal-strength\"])\nmd(r\"\"\"\n**Result: see the record.** The frequency, direction and interaction tests for both networks are printed\nabove.\n\"\"\")\n\nmd(r\"\"\"\n## theta-peak-bands\n\n> Individual theta peaks were found at 2 to 5 Hz in 3 subjects, 3 to 6 Hz in 2, 4 to 7 Hz in 2 and 5\n> to 8 Hz in 3.\n\nThe six filters are 1.5-4, 2-5, 3-6, 4-7, 5-8 and 6-10 Hz. A maximum at 1.5-4 or 6-10 Hz has no\n3 Hz wide band of the paper's list; it is counted apart, and for PAC the nearest band of the list is\nused (2-5 or 5-8 Hz, an assumption).\n\"\"\")\ncode(r\"\"\"\nnames = {1: \"1.5-4\", 2: \"2-5\", 3: \"3-6\", 4: \"4-7\", 5: \"5-8\", 6: \"6-10\"}\nrows = []\nfor sid, r in R.items():\n    rows.append({\"subject\": sid, \"a_all_electrodes\": names[r[\"peak_band_all\"]],\n                 \"b_directing_methods_psi\": names.get(r[\"peak_band_dir\"], \"none\") if r[\"peak_band_dir\"] else \"no electrodes\",\n                 \"b_directing_code_psi\": names.get(r[\"peak_band_dir_code\"], \"none\") if r[\"peak_band_dir_code\"] else \"no electrodes\",\n                 \"z_curve_all\": np.round(r[\"peak_curve_all\"], 2).tolist(), \"theta_band_used_for_PAC\": r.get(\"theta_band_used\")})\npk = pd.DataFrame(rows)\nprint(pk.to_string(index=False))\nexp = {\"2-5\": 3, \"3-6\": 2, \"4-7\": 2, \"5-8\": 3}\nfor col in (\"a_all_electrodes\", \"b_directing_methods_psi\", \"b_directing_code_psi\"):\n    vc = pk[col].value_counts().to_dict()\n    overlap = sum(min(vc.get(k, 0), v) for k, v in exp.items())\n    print(f\"{col}: {vc}; all four counts match: {all(vc.get(k, 0) == v for k, v in exp.items())}; overlap with the paper's counts {overlap} of 10\")\n\"\"\", tags=[\"claim:theta-peak-bands\"])\nmd(r\"\"\"\n**Result: see the record.** The counts per band and their overlap with the paper's are printed for each\nreading.\n\"\"\")\n\nmd(r\"\"\"\n## PAC (claims pac-mtl-spatial to pac-mtl-ofc-direction)\n\nPAC z is computed for every unit that is phase-directing under either form of PSI; the models use\nthe units of the code's form (the Methods' form selects none). Readings of the surrogate: (a)\namplitudes permuted across trials (code), (b) amplitude bands shuffled within trials. Models as in\nM10, computed as within-unit F tests (`fcx2.within_unit_anova`); a direction main effect on unit\nmeans with a subject random intercept.\n\"\"\")\ncode(r\"\"\"\nPAC = {}\nfor sid, r in R.items():\n    for p in r[\"pac\"]:\n        PAC[(sid, p[\"unit\"], p[\"cond\"], p[\"reading\"])] = p[\"z\"][:16]\nAMP_C = fcx2.CENTRES[fcx2.AMP_BANDS][:16]\nTBIN = np.arange(19) * 0.05\nEFF = {(0,): \"condition\", (1,): \"frequency\", (2,): \"time\", (0, 1): \"cond x freq\", (0, 2): \"cond x time\",\n       (1, 2): \"freq x time\", (0, 1, 2): \"cond x freq x time\"}\n\n\ndef pac_units(system):\n    d = U[(U.system == system) & (U.z_post_code > 1.96)]\n    return d\n\n\ndef pac_array(d, cond, rd):\n    return np.stack([np.stack([PAC[(s, i, 1, rd)], PAC[(s, i, cond, rd)]]) for s, i in zip(d.subject, d.idx)])  # (u, 2, 16, 19)\n\n\ndef pac_model(system, cond, rd):\n    d = pac_units(system)\n    Y = pac_array(d, cond, rd)\n    tab, res_df = fcx2.within_unit_anova(Y)\n    diff = (Y[:, 1] - Y[:, 0]).mean(axis=0)                 # (16, 19), relation minus identity\n    out = {\"system\": system, \"model\": {2: \"spatial\", 3: \"temporal\"}[cond], \"reading\": rd, \"units\": len(d),\n           \"subjects\": d.subject.nunique(), \"res_df\": res_df, \"mean_diff\": diff.mean(),\n           \"peak_freq\": AMP_C[int(np.argmax(diff.mean(axis=1)))], \"peak_freq_idx\": int(np.argmax(diff.mean(axis=1))),\n           \"peak_time\": TBIN[np.unravel_index(np.argmax(diff), diff.shape)[1]],\n           \"peak_tf_freq_idx\": int(np.unravel_index(np.argmax(diff), diff.shape)[0])}\n    for _, row in tab.iterrows():\n        out[EFF[row.effect]] = row.p\n    return out\n\n\nrows = []\nfor system in SYSTEMS:\n    for cond in (2, 3):\n        for rd in (\"a\", \"b\"):\n            rows.append(pac_model(system, cond, rd))\nPM = pd.DataFrame(rows)\nprint(\"Bonferroni threshold 0.05/7 =\", round(0.05 / 7, 5))\nprint(PM.to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))\n\n\ndef dir_model(a, b, cond, rd):\n    da, db = pac_units(a), pac_units(b)\n    d = pd.concat([da, db])\n    Y = np.concatenate([pac_array(da, cond, rd), pac_array(db, cond, rd)])\n    g = np.r_[np.zeros(len(da), int), np.ones(len(db), int)]\n    tab, res_df = fcx2.within_unit_anova(Y, g)\n    m = pd.DataFrame({\"y\": Y.mean(axis=(1, 2, 3)), \"dir\": g, \"subject\": d.subject.to_numpy()})\n    fit = smf.mixedlm(\"y ~ dir\", m, groups=m[\"subject\"]).fit(reml=True)\n    out = {\"network\": f\"{a}/{b}\", \"model\": {2: \"spatial\", 3: \"temporal\"}[cond], \"reading\": rd,\n           \"units\": f\"{len(da)}+{len(db)}\", \"direction\": fit.pvalues[\"dir\"],\n           \"mean_a\": Y[g == 0].mean(), \"mean_b\": Y[g == 1].mean(),\n           \"diff_a\": (Y[g == 0][:, 1] - Y[g == 0][:, 0]).mean(), \"diff_b\": (Y[g == 1][:, 1] - Y[g == 1][:, 0]).mean()}\n    for _, row in tab.iterrows():\n        e = row.effect\n        name = (\"direction x \" if e[0] == \"D\" else \"\") + EFF[tuple(x for x in e if x != \"D\")]\n        out[name] = row.p\n    return out\n\n\nrows = []\nfor a, b in ((\"MTL->PFC\", \"PFC->MTL\"), (\"MTL->OFC\", \"OFC->MTL\")):\n    for cond in (2, 3):\n        for rd in (\"a\", \"b\"):\n            rows.append(dir_model(a, b, cond, rd))\nDM = pd.DataFrame(rows)\nprint(\"\\nDirection models, Bonferroni threshold 0.05/15 =\", round(0.05 / 15, 5))\nprint(DM.T.to_string(float_format=lambda v: f\"{v:.3g}\"))\n\"\"\", tags=[\"claim:pac-mtl-spatial\", \"claim:pac-frontal-no-condition\", \"claim:pac-mtl-pfc-spatial\",\n           \"claim:pac-mtl-pfc-temporal\", \"claim:pac-pfc-mtl-no-condition\", \"claim:pac-mtl-ofc-spatial\",\n           \"claim:pac-mtl-pfc-direction\", \"claim:pac-mtl-ofc-direction\"])\n\ncode(r\"\"\"\nB7, B15 = 0.05 / 7, 0.05 / 15\nCONDFX = [\"condition\", \"cond x freq\", \"cond x time\", \"cond x freq x time\"]\nALLFX = list(EFF.values())\n\n\ndef sel(system, model, rd):\n    return PM[(PM.system == system) & (PM.model == model) & (PM.reading == rd)].iloc[0]\n\n\nverdict = {}\nfor rd in (\"a\", \"b\"):\n    s, t = sel(\"MTL\", \"spatial\", rd), sel(\"MTL\", \"temporal\", rd)\n    p1 = s[\"condition\"] < B7 and s[\"cond x freq\"] < B7 and s.mean_diff > 0\n    p2 = abs(s.peak_freq_idx - 5) <= 1 or abs(s.peak_freq_idx - 11) <= 1\n    p3 = all(t[f] >= B7 for f in CONDFX)\n    verdict[(\"pac-mtl-spatial\", rd)] = (p1, p2, p3)\n    verdict[(\"pac-frontal-no-condition\", rd)] = all(sel(sy, mo, rd)[f] >= B7 for sy in (\"PFC\", \"OFC\") for mo in (\"spatial\", \"temporal\") for f in CONDFX)\n    s = sel(\"MTL->PFC\", \"spatial\", rd)\n    q1 = all(s[f] < B7 for f in CONDFX) and s.mean_diff > 0\n    q2 = 1 <= s.peak_tf_freq_idx <= 4 and (0.1 <= s.peak_time <= 0.25 or 0.8 <= s.peak_time <= 0.9)\n    verdict[(\"pac-mtl-pfc-spatial\", rd)] = (q1, q2, s[\"condition\"] < B7 and s.mean_diff > 0)\n    t = sel(\"MTL->PFC\", \"temporal\", rd)\n    verdict[(\"pac-mtl-pfc-temporal\", rd)] = t[\"condition\"] < B7 and t.mean_diff > 0\n    verdict[(\"pac-pfc-mtl-no-condition\", rd)] = all(sel(\"PFC->MTL\", mo, rd)[f] >= B7 for mo in (\"spatial\", \"temporal\") for f in CONDFX)\n    s, t = sel(\"MTL->OFC\", \"spatial\", rd), sel(\"MTL->OFC\", \"temporal\", rd)\n    r1 = s[\"condition\"] < B7 and s[\"cond x freq\"] < B7 and s.mean_diff > 0\n    r2 = s.peak_freq_idx <= 1\n    r3 = all(t[f] >= B7 for f in CONDFX) and all(sel(\"OFC->MTL\", mo, rd)[f] >= B7 for mo in (\"spatial\", \"temporal\") for f in CONDFX)\n    verdict[(\"pac-mtl-ofc-spatial\", rd)] = (r1, r2, r3)\n    for net, key in ((\"MTL->PFC/PFC->MTL\", \"pac-mtl-pfc-direction\"), (\"MTL->OFC/OFC->MTL\", \"pac-mtl-ofc-direction\")):\n        out = []\n        for mo in (\"spatial\", \"temporal\"):\n            d = DM[(DM.network == net) & (DM.model == mo) & (DM.reading == rd)].iloc[0]\n            out.append({\"model\": mo, \"cond_x_dir\": d[\"direction x condition\"], \"cond_x_dir_larger_MTL_first\": d.diff_a > d.diff_b,\n                        \"direction\": d[\"direction\"], \"higher\": \"first (MTL->)\" if d.mean_a > d.mean_b else \"second (->MTL)\",\n                        \"any_effect_below\": any(d[c] < B15 for c in d.index if c not in (\"network\", \"model\", \"reading\", \"units\", \"mean_a\", \"mean_b\", \"diff_a\", \"diff_b\"))})\n        verdict[(key, rd)] = out\nfor k, v in verdict.items():\n    print(k, v)\n\"\"\", tags=[\"claim:pac-mtl-spatial\", \"claim:pac-frontal-no-condition\", \"claim:pac-mtl-pfc-spatial\",\n           \"claim:pac-mtl-pfc-temporal\", \"claim:pac-pfc-mtl-no-condition\", \"claim:pac-mtl-ofc-spatial\",\n           \"claim:pac-mtl-pfc-direction\", \"claim:pac-mtl-ofc-direction\"])\nmd(r\"\"\"\n**Result: see the record.** For each PAC claim the parts of its criterion are printed above under both\nsurrogate readings, with the model p-values in the tables before them.\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\nOutcomes are in the attempt record. The analysis follows the claims file and, for details it lacks,\nthe paper's Methods and the analysis code deposited with the data. The main differences from the\npaper: the data's time axes are taken as the code takes them, although the trial table and the\ndescriptor place the events 1.5 s earlier and no task-locked response could settle it; the\nphase-directing units for the PAC models come from the code's form of PSI, as the Methods' PSI\nselects none; the mixed models use random intercepts.\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\"\"\")\ncode(r\"\"\"\nprint(f\"total run time {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, sys.argv[1])\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python build_nb.py entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb && cd entries/crcns-fcx-2-johnson-2018 && cat > $TMPDIR/devnb.py <<'EOF'
import json, pickle, os, sys
nb=json.load(open('reproduce_johnson_2018.ipynb'))
codes=[''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code']
g={}
exec(codes[0].split('started = time.time()')[0], g)
exec("""
import pickle, os, time
started=time.time()
chtab = fcx2.read_channel_table()
summary = fcx2.read_summary_file()
R={s:pickle.load(open(os.environ['TMPDIR']+f'/devres/{s}.pkl','rb')) for s in fcx2.SUBJECTS}
for r in R.values():
    for u in r['units']:
        u.setdefault('zf_post_code', u['zf_post_mtmfft'])
""", g)
for i,c in enumerate(codes[1:],1):
    if len(sys.argv)>1 and str(i) not in sys.argv[1:]: continue
    print(f'======== cell {i}')
    exec(c, g)
EOF
timeout 1200 python $TMPDIR/devnb.py 2>&1 | head -400
```

```
Sun Nov  8 21:50:27 UTC 2026
Traceback (most recent call last):
  File "/tmp/claude-1001/build_nb.py", line 1, in <module>
    import nbformat as nbf
ModuleNotFoundError: No module named 'nbformat'
python: can't open file '/tmp/claude-1001/devnb.py': [Errno 2] No such file or directory
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q nbformat && python build_nb.py entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb && cd entries/crcns-fcx-2-johnson-2018 && cat > $TMPDIR/devnb.py <<'EOF'
import json, pickle, os, sys
nb=json.load(open('reproduce_johnson_2018.ipynb'))
codes=[''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code']
g={}
exec(codes[0].split('started = time.time()')[0], g)
exec("""
import pickle, os, time
started=time.time()
chtab = fcx2.read_channel_table()
summary = fcx2.read_summary_file()
R={s:pickle.load(open(os.environ['TMPDIR']+f'/devres/{s}.pkl','rb')) for s in fcx2.SUBJECTS}
for r in R.values():
    for u in r['units']:
        u.setdefault('zf_post_code', u['zf_post_mtmfft'])
""", g)
for i,c in enumerate(codes[1:],1):
    if len(sys.argv)>1 and str(i) not in sys.argv[1:]: continue
    print(f'======== cell {i}')
    exec(c, g)
EOF
timeout 1200 python $TMPDIR/devnb.py 2>&1 | head -300
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/devnb.py", line 5, in <module>
    exec(codes[0].split('started = time.time()')[0], g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 10, in <module>
ModuleNotFoundError: No module named 'fcx2'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-fcx-2-johnson-2018 && PYTHONPATH=. timeout 1200 python $TMPDIR/devnb.py 2>&1 | head -300
```

```
======== cell 1
subject     fs   hdr_fs  derived_labels  analysed  trials_table  trials_derived  correct_derived  samples_pre  samples_enc samples_proc         time_enc  same_start  x_min_uV  x_max_uV  load_s
     s1 1000.0 [1000.0]              33        15           120             111              102 (4501, 4501) (4501, 4502) (4501, 4501)      (-1.5, 3.0)        True    -155.9     163.9      27
     s2 1000.0 [1000.0]              31        25           120             113              109 (4501, 4501) (4502, 4503) (4501, 4501)    (-1.5, 3.001)        True    -116.7     181.2      22
     s3 1000.0 [1000.0]              14         7           120             115               96 (4501, 4501) (4498, 4499) (4501, 4501)    (-1.5, 2.997)        True    -208.6     191.9      22
     s4 1000.0 [1000.0]              34        19           120             118              110 (4501, 4501) (4502, 4504) (4501, 4501)    (-1.5, 3.001)        True    -763.3     642.5      24
     s5 1000.0 [1000.0]             118        28           120             120               95 (4501, 4501) (4496, 4498) (4501, 4501)    (-1.5, 2.995)        True    -840.7     733.7      71
     s6 1000.0 [1000.0]              74        48           120             108              103 (4501, 4501) (4505, 4506) (4501, 4501)    (-1.5, 3.004)        True    -621.2    1053.4      60
     s7 1000.0 [1000.0]              57        24           120             100              100 (4501, 4501) (4498, 4499) (4501, 4501)    (-1.5, 2.997)        True    -557.6     399.6      32
     s8  512.0  [512.0]              43         9           120              90               86 (2305, 2305) (2304, 2304) (2305, 2305) (-1.5, 2.998047)        True    -109.7     117.6      14
     s9  512.0  [512.0]              57        27           120             120              101 (2305, 2305) (2304, 2304) (2305, 2305) (-1.5, 2.998047)        True    -944.9    1446.8      28
    s10 1000.0 [1000.0]              57        52     
[... 288 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cd entries/crcns-fcx-2-johnson-2018 && timeout 900 python - <<'EOF' 2>&1 | grep -v Warn
import numpy as np, fcx2
ch=fcx2.read_channel_table()
for sid in ['s1','s2','s4']:
    c=ch[ch.subject==sid].reset_index(drop=True)
    sub=fcx2.load_subject(sid, c.label.tolist())
    pre,enc=sub['seg']['pre'],sub['seg']['encmain']; fs=enc['fs']
    cor=enc['trialinfo'][:,1]==1
    rng=np.random.default_rng(0)
    for name,(b0,b1,e0,e1) in {'code axes':(0.65,0.85,0,1.5),'table axes (-1.5 s)':(-0.85,-0.65,-1.5,0.0)}.items():
        bsel=fcx2.window_index(pre['time'],b0,b1); esel=fcx2.window_index(enc['time'],e0,e1)
        bp=fcx2._filter_chunks(pre['x'][cor],fs,bsel,fcx2.BANDS[:12],'power')
        m,s=fcx2.baseline_bootstrap(bp,int(cor.sum()),rng)
        ep=fcx2._filter_chunks(enc['x'][cor],fs,esel,fcx2.BANDS[:12],'power')
        z=((ep-m[None,:,:,None])/s[None,:,:,None]).mean(0)  # ch, band, T
        for reg in ['MTL','PFC','OFC']:
            idx=np.where(c.region==reg)[0]
            if len(idx)==0: continue
            th=z[idx][:,2:6].mean(1).mean(0)  # T
            al=z[idx][:,6:9].mean(1).mean(0)
            print(sid,name,reg,'theta z: median %.2f frac>1.96 %.2f | alpha z median %.2f frac<-1.96 %.2f'%(np.median(th),(th>1.96).mean(),np.median(al),(al<-1.96).mean()))
EOF
```

```
Sun Nov  8 21:51:05 UTC 2026
s1 code axes MTL theta z: median 1.00 frac>1.96 0.00 | alpha z median 0.25 frac<-1.96 0.00
s1 code axes PFC theta z: median 0.06 frac>1.96 0.00 | alpha z median 0.37 frac<-1.96 0.00
s1 code axes OFC theta z: median -0.50 frac>1.96 0.00 | alpha z median 0.11 frac<-1.96 0.00
s1 table axes (-1.5 s) MTL theta z: median -0.46 frac>1.96 0.00 | alpha z median -0.43 frac<-1.96 0.02
s1 table axes (-1.5 s) PFC theta z: median 0.28 frac>1.96 0.00 | alpha z median -0.10 frac<-1.96 0.02
s1 table axes (-1.5 s) OFC theta z: median -0.27 frac>1.96 0.00 | alpha z median -0.06 frac<-1.96 0.03
s2 code axes MTL theta z: median 1.01 frac>1.96 0.00 | alpha z median 0.57 frac<-1.96 0.00
s2 code axes PFC theta z: median -0.01 frac>1.96 0.00 | alpha z median -0.00 frac<-1.96 0.00
s2 code axes OFC theta z: median -0.94 frac>1.96 0.00 | alpha z median -0.52 frac<-1.96 0.00
s2 table axes (-1.5 s) MTL theta z: median 0.06 frac>1.96 0.00 | alpha z median -0.55 frac<-1.96 0.01
s2 table axes (-1.5 s) PFC theta z: median 0.99 frac>1.96 0.00 | alpha z median 0.48 frac<-1.96 0.02
s2 table axes (-1.5 s) OFC theta z: median -0.23 frac>1.96 0.00 | alpha z median 0.24 frac<-1.96 0.00
s4 code axes MTL theta z: median -0.13 frac>1.96 0.00 | alpha z median -0.12 frac<-1.96 0.00
s4 code axes PFC theta z: median -0.62 frac>1.96 0.00 | alpha z median -0.35 frac<-1.96 0.00
s4 code axes OFC theta z: median -1.02 frac>1.96 0.00 | alpha z median -0.40 frac<-1.96 0.00
s4 table axes (-1.5 s) MTL theta z: median 0.84 frac>1.96 0.07 | alpha z median 1.86 frac<-1.96 0.00
s4 table axes (-1.5 s) PFC theta z: median 0.87 frac>1.96 0.00 | alpha z median 1.20 frac<-1.96 0.00
s4 table axes (-1.5 s) OFC theta z: median -0.14 frac>1.96 0.00 | alpha z median -0.03 frac<-1.96 0.01
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cd entries/crcns-fcx-2-johnson-2018 && PYTHONPATH=. timeout 1200 python $TMPDIR/devnb.py 11 12 13 14 15 16 17 18 19 20 2>&1 | grep -v "^p_electrode\|^  p_subject" | head -300
```

```
Sun Nov  8 21:53:28 UTC 2026
======== cell 11
       null subject   label region  p_enc  p_post
p_subject: 12 electrodes ({'PFC': 6, 'OFC': 5, 'MTL': 1}) in 5 subjects; expected 8 (5 PFC, 3 OFC) in 4
======== cell 12
filter centres: [2.0, 2.75, 3.5, 4.5, 5.5, 6.5, 8.0, 9.5, 11.5, 13.5, 16.0]
subject   group reading  pairs  theta_peak               peaks_Hz  max_at_Hz  alpha_over_theta
     s1 MTL-MTL   implv      1        True       [4.5, 8.0, 11.5]       2.00          1.067105
     s1 MTL-MTL     pli      1        True  [4.5, 6.5, 9.5, 13.5]       4.50          0.901038
     s1 MTL-MTL    code      1        True             [3.5, 6.5]      16.00          1.452785
     s1 MTL-PFC   implv     16        True             [3.5, 9.5]       3.50          0.877468
     s1 MTL-PFC     pli     16        True             [3.5, 9.5]       3.50          0.914037
     s1 MTL-PFC    code     16        True       [3.5, 6.5, 11.5]       6.50          0.993770
     s1 MTL-OFC   implv     10        True       [3.5, 8.0, 13.5]       3.50          0.897458
     s1 MTL-OFC     pli     10        True             [3.5, 6.5]       3.50          0.906447
     s1 MTL-OFC    code     10        True        [3.5, 5.5, 9.5]       3.50          1.007722
     s2 MTL-MTL   implv     21        True                  [3.5]       3.50          0.648271
     s2 MTL-MTL     pli     21        True             [3.5, 5.5]       3.50          0.668034
     s2 MTL-MTL    code     21       False                 [11.5]      11.50          1.137358
     s2 MTL-PFC   implv     28        True       [4.5, 9.5, 13.5]       2.00          0.967365
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='build_nb.py'; s=open(p).read()
old=s[s.index('def lmm_interval(d, y):'):s.index('rows = []\nfor key in ("mtmfft", "sliding", "code"):')]
new='''def lmm_interval(d, y):
    """Postcue minus precue with random intercepts for subject and pair: with two intervals per
    pair, the mixed model's F test of interval is the within-pair F test, F = t^2 of the paired
    differences (fcx2.within_unit_anova)."""
    w = d.pivot_table(index="pair", columns="interval", values=y)
    Y = w[["pre", "post"]].to_numpy()
    tab, res_df = fcx2.within_unit_anova(Y)
    diff = (Y[:, 1] - Y[:, 0]).mean()
    return diff, float(tab.loc[0, "F"]), float(tab.loc[0, "p"])


'''
s=s.replace(old,new)
s=s.replace('"post_minus_pre": b, "t": t, "p": p})\nps = pd.DataFrame(rows)','"post_minus_pre": b, "F": t, "p": p})\nps = pd.DataFrame(rows)')
s=s.replace('"pre_frac_above": (d[f"z_pre_{key}"] > 1.96).mean(), "post_minus_pre": b, "t": t, "p": p})','"pre_frac_above": (d[f"z_pre_{key}"] > 1.96).mean(), "post_minus_pre": b, "F": t, "p": p})')
open(p,'w').write(s)
EOF
grep -n '"t": t' build_nb.py; . dev/bin/activate && python build_nb.py entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb && cd entries/crcns-fcx-2-johnson-2018 && PYTHONPATH=. timeout 1200 python $TMPDIR/devnb.py 13 14 15 16 17 18 19 20 2>&1 | head -300
```

```
Exit code 1
  File "/tmp/claude-1001/build_nb.py", line 577
    pair, the mixed model's F test of interval is the within-pair F test, F = t^2 of the paired
                         ^
SyntaxError: unterminated string literal (detected at line 577)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace('''    """Postcue minus precue with random intercepts for subject and pair: with two intervals per
    pair, the mixed model's F test of interval is the within-pair F test, F = t^2 of the paired
    differences (fcx2.within_unit_anova)."""''','''    # Postcue minus precue with random intercepts for subject and pair: with two intervals per
    # pair, the mixed model's F test of interval is the within-pair F test, F = t^2 of the
    # paired differences (fcx2.within_unit_anova).''')
open(p,'w').write(s)
EOF
. dev/bin/activate && python build_nb.py entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb && cd entries/crcns-fcx-2-johnson-2018 && PYTHONPATH=. timeout 1200 python $TMPDIR/devnb.py 13 14 15 16 17 18 19 20 2>&1 | head -300
```

```
======== cell 13
reading     net  pairs  subjects response  pre_mean_z  pre_below  pre_above  post_mean_z  post_below  post_above  post_minus_pre        F      p
 mtmfft MTL-PFC    172         9        z     -0.1379          6          3      -0.0225           9          10          0.1154   1.2177 0.2714
 mtmfft MTL-PFC    172         9      raw     -0.1379          6          3      -0.0225           9          10          0.0002   0.0008 0.9781
 mtmfft MTL-OFC    302         7        z     -0.1276          7         14      -0.1756          17           5         -0.0480   0.3438 0.5581
 mtmfft MTL-OFC    302         7      raw     -0.1276          7         14      -0.1756          17           5         -0.0009   0.2620 0.6091
sliding MTL-PFC    172         9        z     -0.2537         58         43       0.1901          48          58          0.4438   3.4356 0.0655
sliding MTL-PFC    172         9      raw     -0.2537         58         43       0.1901          48          58          0.0048   3.1192 0.0792
sliding MTL-OFC    302         7        z     -0.3866        115         70      -0.3607         112          73          0.0259   0.0221 0.8820
sliding MTL-OFC    302         7      raw     -0.3866        115         70      -0.3607         112          73          0.0025   4.9359 0.0270
   code MTL-PFC    172         9        z     -3.9095         98         53       7.9657          53         105         11.8752  13.8742 0.0003
   code MTL-PFC    172         9      raw     -3.9095         98         53       7.9657          53         105          0.0834  34.8513 0.0000
   code MTL-OFC    302         7        z    -10.7334        196         76       7.6854         110         169         18.4188  37.1811 0.0000
   code MTL-OFC    302         7      raw    -10.7334        196         76       7.6854         110         169          0.1391 113.1365 0.0000
expected pairs: MTL-PFC 172 +- 17.2, MTL-OFC 303 +- 30.3
======== cell 14
reading   system  units 
[... 157 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='build_nb.py'; s=open(p).read()
old='''d = behaviour_rows(False)
exp = {1:'''
new='''# the per-subject response times of docs/summary_file.csv, whose means are the paper's
sf = summary.melt(id_vars="subject", value_vars=["rt_identity", "rt_spatial", "rt_temporal"], var_name="c", value_name="rt")
sf["cond"] = sf.c.map({"rt_identity": 1, "rt_spatial": 2, "rt_temporal": 3})
print("summary_file.csv response time, mean and SD over subjects:", sf.groupby("cond").rt.agg(["mean", "std"]).round(1).to_dict("index"))
print("  rt (summary_file.csv):", {k: round(v, 4) for k, v in lmm_tests(sf, "rt").items()})
d = behaviour_rows(False)
exp = {1:'''
assert old in s
s=s.replace(old,new)
open(p,'w').write(s)
EOF
. dev/bin/activate && python build_nb.py entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb && cd entries/crcns-fcx-2-johnson-2018 && PYTHONPATH=. timeout 1200 python $TMPDIR/devnb.py 6 2>&1 | tail -8; date -u
```

```
elogit: {'spatial_vs_identity_p': np.float64(0.1599), 'temporal_vs_identity_p': np.float64(0.5002), 'three_level_chi2': 1.9765, 'three_level_p': 0.3722, 'numeric_z': np.float64(0.6651), 'numeric_p': np.float64(0.506)}
  rt: {'spatial_vs_identity_p': np.float64(0.0), 'temporal_vs_identity_p': np.float64(0.0), 'three_level_chi2': 26.2517, 'three_level_p': 0.0, 'numeric_z': np.float64(-3.3878), 'numeric_p': np.float64(0.0007)}
trial-level response time variant: p spatial 0.0 p temporal 0.0 3-level p 0.0
summary_file.csv response time, mean and SD over subjects: {1: {'mean': 1659.3, 'std': 701.3}, 2: {'mean': 1335.5, 'std': 574.3}, 3: {'mean': 1475.4, 'std': 733.9}}
  rt (summary_file.csv): {'spatial_vs_identity_p': np.float64(0.0018), 'temporal_vs_identity_p': np.float64(0.0769), 'three_level_chi2': 9.7556, 'three_level_p': 0.0076, 'numeric_z': np.float64(-1.5537), 'numeric_p': np.float64(0.1203)}
condition 1: accuracy 0.900 vs 0.9 +- 0.04: True; rt 1744 vs 1659 +- 701: True
condition 2: accuracy 0.920 vs 0.92 +- 0.09: True; rt 1237 vs 1335 +- 574: True
condition 3: accuracy 0.890 vs 0.89 +- 0.09: True; rt 1292 vs 1475 +- 734: True
Sun Nov  8 21:54:38 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='build_nb.py'; s=open(p).read()
rep = {}
rep['''**Result: not reproduced.** The means are within the paper's SDs (printed above), but under reading
(a) the accuracy model finds a condition effect at p < 0.05, so the paper's test finds a difference
(the printed p-values for each reading and the numeric-term variant show which). See the record for
the numbers under each reading.''']='''**Result: not reproduced.** The condition means are within the paper's SDs (accuracy 0.900, 0.920,
0.890 over all trials; response time 1744, 1237, 1292 ms from the trial tables). Accuracy shows no
effect under the 3-level term (p = 0.054 over all trials, 0.37 over kept trials), though spatial
differs from identity over all trials (p = 0.023). Response time differs by condition under both of
the criterion's readings, with the trial tables (p < 0.001) and with the per-subject values of
`summary_file.csv` (3-level p = 0.0076; spatial against identity p = 0.0018), whose means are the
paper's (1659, 1335, 1475 ms). Only with condition entered as one numeric term, which has the
paper's single numerator degree of freedom, is the response-time effect absent (p = 0.12 on
`summary_file.csv`, the paper's "p > 0.12"); that reading is not among the criterion's. The trial
tables' response times differ from `summary_file.csv` in 7 of 10 subjects.'''
rep['''**Result: see the record.** The outcome follows the paper's test as the code runs it (subject-wide null):
the counts of electrodes with a significant cluster are printed above.''']='''**Result: not reproduced.** With the code's subject-wide null, one electrode of 254 (in s5, postcue F
test, cluster p = 0.034) has a significant cluster, and the criterion allows none. With a
per-electrode null, 13 electrodes have one, fewer than the 25.4 expected by chance over two tests.'''
rep['''**Result: see the record.** The counts of subjects and electrodes meeting the claim's rule are printed
above for each region.''']='''**Result: not reproduced.** No subject has a region-average theta z above 1.96 over half the time
points in any region (0 of 10 MTL, 0 of 9 PFC, 0 of 9 OFC), and no subject shows MTL alpha below
-1.96 over half the time points (0 of 10). Per electrode, 1 of 36 MTL, 1 of 116 PFC and 11 of 102
OFC electrodes meet the theta rule. 239 of 254 electrodes have some z above 1.96 above 16 Hz.'''
rep['''**Result: see the record.** The counts under the code's subject-wide null and under the per-electrode
null are printed above; the subject-wide set is excluded from the analyses that follow.''']='''**Result: not reproduced.** The code's subject-wide null finds 12 electrodes (6 PFC, 5 OFC, 1 MTL) in 5
subjects, against 8 (5 PFC, 3 OFC) in 4; the per-electrode null finds many more, as printed. The 12
are excluded from the analyses that follow, which leaves 35 MTL, 110 PFC and 97 OFC electrodes.'''
rep['''**Result: see the record.** The number of subjects with a theta peak, per group and reading, is
printed above.''']='''**Result: reproduced.** With the imaginary PLV (reading a), the mean spectrum has a local maximum in
3 to 7 Hz in 7 of 9 subjects for MTL to MTL pairs, 8 of 9 for MTL to PFC and 4 of 7 for MTL to OFC;
the phase-lag index gives 9 of 9, 8 of 9 and 3 of 7. The rule asks for one subject per group, a weak
test; the peaks are often one of several local maxima, and the largest value is in 3 to 7 Hz in
fewer subjects (column max_at_Hz).'''
rep['''**Result: see the record.** Part (1) and part (2) of the criterion are printed for every reading.''']='''**Result: not reproduced.** With the PSI of the Methods and the code's single window, precue PSI is
slightly negative in both networks (mean z -0.14 and -0.13), with more frontal than MTL leads among
MTL-PFC pairs (6 against 3) but not among MTL-OFC pairs (7 against 14), and postcue does not exceed
precue (p = 0.27 and 0.56 on z). With sliding windows part (1) holds in both networks and part (2)
only for MTL-OFC on raw PSI (p = 0.027; MTL-PFC p = 0.079), which the criterion calls partial. With
the code's own form of PSI both parts hold in both networks (precue mean z -3.9 and -10.7;
postcue minus precue p = 0.0003 and < 0.0001 on z). The pair counts are 172 and 302 (expected 172
and 303).'''
rep['''**Result: see the record.** The number of systems meeting each part of the criterion is printed for
every reading.''']='''**Result: not reproduced.** With the PSI of the Methods no precue electrode or pair passes z > 1.96,
but postcue exceeds precue in only 1 of 7 systems on z (MTL to OFC, p = 0.036) and 0 of 7 on raw
PSI. With the code's form, 2 of 7 systems (MTL to PFC and MTL to OFC) show the shift, and 24% to 55%
of precue units per system pass z > 1.96. The models hold 35 MTL, 110 PFC and 97 OFC electrodes
(expected 36, 111 and 99, all within tolerance).'''
rep['''**Result: not reproduced.** With the PSI of the Methods no unit passes z > 1.96; with the code's form
the counts are of the paper's order but most fall outside 10%, as printed.''']='''**Result: not reproduced.** With the PSI of the Methods no electrode or pair passes z > 1.96 in the
postcue delay (0 of 7 counts within 10%). With the code's form of PSI the counts are 21 MTL, 43 PFC,
38 OFC, 106 MTL to PFC, 70 PFC to MTL, 200 MTL to OFC and 168 OFC to MTL (expected 13, 52, 38, 56,
85, 93, 115): 1 of 7 within 10%, and the subject counts for MTL electrodes and MTL to OFC pairs are 9
and 5 (expected 8 and 5).'''
rep['''**Result: see the record.** The counts per band and their overlap with the paper's are printed for each
reading.''']='''**Result: not reproduced.** Over all analysed electrodes (reading a) the maxima are at 1.5-4 Hz in 3
subjects, 6-10 Hz in 3, 2-5 Hz in 2, 4-7 Hz in 1 and 5-8 Hz in 1: 6 subjects peak outside the
paper's four bands, and the overlap with the paper's counts is 4 of 10. On the phase-directing
electrodes of the code's PSI (reading b) the overlap is 5 of 10; the Methods' PSI selects no
electrodes. The power curves are flat (z within about -1.2 to 1.7), so the maxima are weak.'''
rep['''**Result: see the record.** For each PAC claim the parts of its criterion are printed above under both
surrogate readings, with the model p-values in the tables before them.''']='''**Result: none of the eight PAC claims is reproduced, under either surrogate reading** (on the units
selected by the code's PSI; the Methods' PSI selects none).

- pac-mtl-spatial: the MTL spatial model's condition effect is p = 0.0072 (a) and 0.016 (b), just above
  and above 0.05/7 = 0.0071, and condition x frequency is p = 0.20 and 0.14; spatial is above identity
  (mean difference 0.038), with the largest difference at 38.5 Hz.
- pac-frontal-no-condition: condition effects pass 0.05/7 in PFC (condition x time p = 3.7e-06) and in
  OFC (condition p = 1.8e-06).
- pac-mtl-pfc-spatial and pac-mtl-pfc-temporal: MTL to PFC condition p = 0.19 and 0.36 (a), with
  spatial and temporal PAC below identity (mean differences -0.008 and -0.006).
- pac-pfc-mtl-no-condition: PFC to MTL temporal condition p = 5.8e-06 (a).
- pac-mtl-ofc-spatial: MTL to OFC spatial condition p = 0.015 (a), above 0.05/7, though the largest
  difference is at 9.5 Hz.
- pac-mtl-pfc-direction: condition x direction passes 0.05/15 in both models under (a) (p = 0.0029 and
  3.9e-05), but the relation minus identity difference is larger in the PFC to MTL direction, and the
  direction effect is p = 0.32 and 0.96.
- pac-mtl-ofc-direction: direction p = 0.13 and condition x direction p = 0.17 in the spatial model,
  and the temporal model has effects below 0.05/15.'''
for k,v in rep.items():
    assert k in s, k[:60]
    s=s.replace(k,v)
s=s.replace('''**Result: see the record.** The frequency, direction and interaction tests for both networks are printed
above.''','''**Result: EQUAL_STRENGTH_RESULT**''')
s=s.replace('''**Result: reproduced.** Over all 120 trials (reading a) accuracy runs from the printed minimum to the
printed maximum, every subject inside 0.711 to 1.0, and both bounds within tolerance of 0.79 and
0.97; reading (b) on the kept trials is printed alongside.''','''**Result: reproduced.** Over all 120 trials (reading a) accuracy runs from 0.792 to 0.967, every
subject inside 0.711 to 1.0, both bounds within tolerance of 0.79 and 0.97. Over kept trials
(reading b) it runs from 0.792 to 1.000, also within tolerance.''')
s=s.replace('''**Result: reproduced.** The channel table lists 36 MTL, 116 PFC and 102 OFC electrodes (254), and
the same-hemisphere subject counts are 9 and 7, as printed.''','''**Result: reproduced.** The channel table lists 36 MTL, 116 PFC and 102 OFC electrodes (254), all
present in the derived data, and MTL shares a hemisphere with PFC in 9 subjects and with OFC in 7.''')
s=s.replace('''**Result: reproduced.** Every mean is within the paper's SD and every subject's per-condition count is
inside the widened ranges, as printed.''','''**Result: reproduced.** The kept trials hold on average 100.9 correct trials per subject (32.9
identity, 34.8 spatial, 33.2 temporal) and 10.2 incorrect, each within the paper's SD, and every
subject's count lies in the widened ranges (identity 26 to 37, spatial 28 to 39, temporal 28 to 37,
incorrect 0 to 25).''')
open(p,'w').write(s)
EOF
grep -c "see the record" build_nb.py; date -u
```

```
1
Sun Nov  8 21:55:25 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python3 tools/entry.py --help 2>&1 | head -20; grep -n "def check" -A80 tools/entry.py | grep -n "error\|fail\|must" | head -60; cat entries/001453-fouke-2025/README.md | head -30
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

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

[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 175,260p tools/entry.py
```

```
# Datasets are related as <archive>:<id>/<version> (docs/archives.md); papers as doi:, entries as entry:.
    used = [r["id"].split(":", 1)[1].partition("/")
            for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))]
    archives = {r["id"].split(":", 1)[1].partition("/")[0]: r["id"].split(":", 1)[0]
                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
    dandisets = [d for d, _, _ in used]
    versions = {d: v for d, _, v in used}
    if entry.get("type") in ("orientation", "reproduction"):
        if not dandisets:
            report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dataset")
        for d, v in versions.items():
            if not v:
                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
    helper_code = "\n".join((entry_dir / h).read_text() for h in helpers if (entry_dir / h).is_file())

    for name in [n for n in listed if n in present]:
        path = entry_dir / name
        nb = nbformat.read(path, as_version=4)
        if any(c.cell_type == "code" and (c.get("outputs") or c.get("execution_count")) for c in nb.cells):
            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "def _derivation_checks" -A40 tools/entry.py | head -60; grep -n "def run\b\|timeout\|max_minutes\|executed" tools/entry.py | head -20
```

```
320:def _derivation_checks(report: Report, where, code: str) -> None:
321-    if EMBEDDED_IMAGE.search(code):
322-        report.error(where, "contains an encoded image; figures must be computed from the data")
323-    if READS_A_FIGURE.search(code):
324-        report.error(where, "reads an image file; figures must be computed from the data")
325-    if any(not _local_data(code, m.start() + 1) for m in LOCAL_PATH.finditer(code)):
326-        report.error(where, "names a local path; stream the data from the archive")
327-    if LONG_LITERAL.search(code):
328-        report.error(where, f"contains a literal of more than {MAX_LITERAL_NUMBERS} numbers; "
329-                            "results must be computed from the data")
330-
331-
332-# --- lock and run -------------------------------------------------------------
333-
334-def lock(entry_dir: Path) -> int:
335-    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
336-                        "requirements.in", "-o", "requirements.lock.txt"], cwd=entry_dir)
337-    if r.returncode == 0:
338-        print(f"wrote {(entry_dir / 'requirements.lock.txt').relative_to(ROOT)}")
339-    return r.returncode
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-2-johnson-2018 && python3 - <<'EOF'
p='fcx2.py'; s=open(p).read()
s=s.replace('''BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live"''','''DATASET = "fcx-2"
VERSION = "unversioned"   # CRCNS data sets are not versioned; the files read are under live/
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live"''')
open(p,'w').write(s)
EOF
cat > $TMPDIR/eqs.py <<'EOF'
import sys, pickle, os, numpy as np
sys.path.insert(0,'entries/crcns-fcx-2-johnson-2018')
import fcx2
ch=fcx2.read_channel_table()
out={}
for sid in fcx2.SUBJECTS:
    r=pickle.load(open(os.environ['TMPDIR']+f'/devres/{sid}.pkl','rb'))
    units=[(i,u) for i,u in enumerate(r['units']) if u['z_post_code']>1.96]
    if not units: continue
    c=ch[ch.subject==sid].reset_index(drop=True)
    sub=fcx2.load_subject(sid,c.label.tolist())
    proc=sub['seg']['proc']; fs=proc['fs']; cor=proc['trialinfo'][:,1]==1
    x=sub['seg']['proc']['x'][cor]; x=x-x.mean(0,keepdims=True)
    _,sel=fcx2.segment(sub,'post')
    nab=fcx2.n_amp_bands(fs); ab=fcx2.BANDS[fcx2.AMP_BANDS[:nab]]
    env=fcx2._filter_chunks(x,fs,sel,ab,'abs')
    th=fcx2.theta_fourier(x[...,sel].astype(np.float64),fs,'mtmfft')
    n,nch,nbb,T=env.shape
    the=fcx2.theta_fourier(env.reshape(n,nch*nbb,T).astype(np.float64),fs,'mtmfft').reshape(n,nch,nbb,5,1)
    for i,u in units:
        rng=np.random.default_rng(fcx2.seed_for(f"cspsi-code|post|{u['ph']}|{u['amp']}", sid))
        A=np.repeat(th[:,[u['ph']]],nbb,axis=1)
        o,zc=fcx2.psi_code(A,the[:,u['amp']],rng)
        assert abs(zc.mean()-u['z_post_code'])<1e-9, (zc.mean(),u['z_post_code'])
        out[(sid,i)]=zc[:16].copy()
    print(sid,len(units),flush=True)
pickle.dump(out,open(os.environ['TMPDIR']+'/devres/zf_code.pkl','wb'))
EOF
cd $TMPDIR && . dev/bin/activate && date -u && timeout 1800 python eqs.py 2>&1 | grep -v Warn; date -u
```

```
Sun Nov  8 21:55:55 UTC 2026
s1 21
s2 52
s3 10
s4 30
s5 79
s6 68
s7 30
s8 4
s9 55
s10 297
Sun Nov  8 22:05:20 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed -i "s/        u.setdefault('zf_post_code', u\['zf_post_mtmfft'\])/        pass/" devnb.py && python - <<'EOF'
s=open('devnb.py').read()
s=s.replace("""for r in R.values():
    for u in r['units']:
        pass""","""zfc=pickle.load(open(os.environ['TMPDIR']+'/devres/zf_code.pkl','rb'))
for sid,r in R.items():
    for i,u in enumerate(r['units']):
        u['zf_post_code']=zfc.get((sid,i))""")
open('devnb.py','w').write(s)
EOF
python build_nb.py entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb && cd entries/crcns-fcx-2-johnson-2018 && PYTHONPATH=. timeout 1200 python $TMPDIR/devnb.py 14 16 2>&1 | grep -A30 "cell 16"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-fcx-2-johnson-2018 && PYTHONPATH=. timeout 1200 python $TMPDIR/devnb.py 14 16 2>&1 | tail -30
```

```
======== cell 14
Traceback (most recent call last):
  File "/tmp/claude-1001/devnb.py", line 20, in <module>
    exec(c, g)
    ~~~~^^^^^^
  File "<string>", line 15, in <module>
NameError: name 'lmm_interval' is not defined
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-fcx-2-johnson-2018 && PYTHONPATH=. timeout 1200 python $TMPDIR/devnb.py 13 14 16 2>&1 | grep -A20 "cell 16"
```

```
======== cell 16
MTL-PFC: 176 pairs (106 MTL->PFC, 70 PFC->MTL) in 9 subjects
  (b) with interaction: frequency F(15,2610) = 1.94, p = 0.0157; frequency x direction F = 2.88, p = 0.000162
  (a) main effects only: frequency F(15,2625) = 1.92, p = 0.0172
  direction (pair means, subject random intercept): PFC->MTL minus MTL->PFC = -1.874, p = 0.214
  mean z per frequency: [13.39, 13.88, 13.4, 14.08, 10.51, 7.82, 19.69, 14.95, 13.6, 13.32, 18.04, 15.9, 12.23, 15.77, 15.47, 18.23]
MTL-OFC: 368 pairs (200 MTL->OFC, 168 OFC->MTL) in 7 subjects
  (b) with interaction: frequency F(15,5490) = 3.03, p = 6.94e-05; frequency x direction F = 3.61, p = 2.64e-06
  (a) main effects only: frequency F(15,5505) = 3.01, p = 7.79e-05
  direction (pair means, subject random intercept): OFC->MTL minus MTL->OFC = 0.279, p = 0.828
  mean z per frequency: [9.42, 17.05, 21.09, 19.18, 17.0, 18.6, 15.22, 20.73, 19.56, 18.56, 16.83, 18.29, 14.09, 11.54, 13.38, 16.24]
local variant MTL: 21 electrodes, frequency F(15,300) = 0.85, p = 0.625
local variant PFC: 43 electrodes, frequency F(15,630) = 1.16, p = 0.297
local variant OFC: 38 electrodes, frequency F(15,555) = 0.58, p = 0.89
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace('**Result: EQUAL_STRENGTH_RESULT**','''**Result: not reproduced.** On the pairs selected by the code's PSI (106 MTL to PFC and 70 PFC to MTL;
200 MTL to OFC and 168 OFC to MTL), the strength of directionality differs across amplitude
frequencies in both networks (frequency p = 0.017 and 7.8e-05 with main effects only, 0.016 and
6.9e-05 with the interaction), and the frequency x direction interaction is significant too (p =
0.00016 and 2.6e-06). The direction main effect is not (p = 0.21 and 0.83).''')
old='''R = {}
for sid in fcx2.SUBJECTS:
    R[sid] = fcx2.process_subject(sid, chtab)
print(f"streamed and analysed {len(R)} subjects in {(time.time() - started) / 60:.1f} min")
""")
'''
new='''R = {}
""")

for group in (["s1", "s2", "s3", "s4"], ["s5", "s6"], ["s7", "s8", "s9"], ["s10"]):
    code(f"""
# one subject at a time: stream, check, run every per-subject measure, keep only the results
for sid in {group!r}:
    R[sid] = fcx2.process_subject(sid, chtab)
print(f"{{len(R)}} subjects done after {{(time.time() - started) / 60:.1f}} min")
""")
'''
assert old in s
s=s.replace(old,new)
open(p,'w').write(s)
EOF
grep -n "EQUAL" build_nb.py; . dev/bin/activate && python build_nb.py entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb && python - <<'EOF'
import json
nb=json.load(open('entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb'))
for c in nb['cells'][:7]: print(c['cell_type'], ''.join(c['source'])[:200].replace('\n',' | '))
EOF
```

```
markdown # Reproducing Johnson et al. (2018) from CRCNS fcx-2 |  | **Paper.** Johnson EL, Adams JN, Solbakk A-K, Endestad T, Larsson PG, Ivanovic J, Meling TR, Lin JJ, | Knight RT (2018). Dynamic frontotemporal syst
code import time | import warnings |  | import numpy as np | import pandas as pd | import matplotlib.pyplot as plt | import statsmodels.formula.api as smf | from scipy import stats |  | import fcx2 |  | warnings.filterwarnings(
code # one subject at a time: stream, check, run every per-subject measure, keep only the results | for sid in ['s1', 's2', 's3', 's4']: |     R[sid] = fcx2.process_subject(sid, chtab) | print(f"{len(R)} subject
code # one subject at a time: stream, check, run every per-subject measure, keep only the results | for sid in ['s5', 's6']: |     R[sid] = fcx2.process_subject(sid, chtab) | print(f"{len(R)} subjects done after
code # one subject at a time: stream, check, run every per-subject measure, keep only the results | for sid in ['s7', 's8', 's9']: |     R[sid] = fcx2.process_subject(sid, chtab) | print(f"{len(R)} subjects done
code # one subject at a time: stream, check, run every per-subject measure, keep only the results | for sid in ['s10']: |     R[sid] = fcx2.process_subject(sid, chtab) | print(f"{len(R)} subjects done after {(ti
markdown ## Data check
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='build_nb.py'; s=open(p).read()
old='''The behaviour table in `docs/summary_file.csv` agrees with the per-trial tables (accuracy over all
120 trials, response time over correct trials), and age and sex match the paper's description (37
± 13 years, 22 to 69, 7 males) as printed. No subject's data appear twice.'''
new='''The accuracies of `docs/summary_file.csv` equal those of the per-trial tables over all 120 trials,
as its descriptor says. Its response times do not equal the mean over correct trials of the
per-trial tables in 7 of 10 subjects (they do in s6, s8 and s9; for s1, identity, 1948 against 2348
ms), although the descriptor says they are "calculated on all correct trials"; the paper's
condition means (1659, 1335, 1475 ms) are those of `summary_file.csv`. Age and sex match the
paper's description (37 ± 13 years, 22 to 69, 7 males). No subject's data appear twice.'''
assert old in s; s=s.replace(old,new)
old='''delay epoch start"), the first sample of `proc` is 0.3 s before column I ("post-cue delay epoch
start") and the first sample of `pre` is 0.1 s after column G ("pretrial epoch start, 1000 ms before
trial start").'''
new='''delay epoch start"), the first sample of `proc` is 0.3 s before column I ("post-cue delay epoch
start") and the first sample of `pre` is about 0.1 s after column G ("pretrial epoch start, 1000 ms
before trial start"; 98 to 108 samples at 1 kHz, 51 at 512 Hz).'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
. dev/bin/activate && python build_nb.py entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb
cd entries/crcns-fcx-2-johnson-2018
cat > requirements.in <<'EOF'
h5py
matplotlib
numpy
pandas
requests
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: crcns-fcx-2-johnson-2018
type: reproduction
title: Frontotemporal theta systems in working memory (Johnson et al. 2018)
description: Tests the findings of Johnson, Adams, Solbakk, Endestad, Larsson, Ivanovic, Meling, Lin and
  Knight (2018) on CRCNS data set fcx-2, which holds the preprocessed intracranial EEG of the 10
  subjects (254 bipolar MTL, PFC and OFC electrodes) in the visuospatial working memory task, their
  trial tables and the paper's analysis scripts. It checks behaviour, electrode and trial counts,
  ERPs, task-induced power, PLV, theta PSI, cross-spectral PSI and theta PAC by condition.
license: Apache-2.0
notebooks:
- path: reproduce_johnson_2018.ipynb
  title: Reproducing Johnson et al. (2018) from CRCNS fcx-2
  runtime_minutes: 45
helpers:
- fcx2.py
related:
- id: crcns:fcx-2/unversioned
  relation: uses_data
- id: doi:10.1371/journal.pbio.2004274
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/crcns-fcx-2-johnson-2018 && python tools/entry.py check entries/crcns-fcx-2-johnson-2018 2>&1 | tail -20; date -u
```

```
Traceback (most recent call last):
  File "tools/entry.py", line 55, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
Sun Nov  8 22:06:06 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q pyyaml jsonschema nbformat && cd  && python tools/entry.py lock entries/crcns-fcx-2-johnson-2018 && python tools/entry.py check entries/crcns-fcx-2-johnson-2018 2>&1 | tail -20
```

```
wrote entries/crcns-fcx-2-johnson-2018/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && date -u && timeout 6000 python tools/entry.py all entries/crcns-fcx-2-johnson-2018 --timeout 3600 2>&1 | tail -30; date -u
```

```
Sun Nov  8 22:06:19 UTC 2026
Installed kernelspec registry-crcns-fcx-2-johnson-2018 in executed/crcns-fcx-2-johnson-2018/.venv/share/jupyter/kernels/registry-crcns-fcx-2-johnson-2018
0 error(s)
pass  reproduce_johnson_2018.ipynb  (2130 s)
Sun Nov  8 22:41:57 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('executed/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    txt=''.join(''.join(o.get('text','')) if 'text' in o else ''.join(o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]))
    if any(t.startswith('claim:') for t in tags) or 'subjects done' in txt or 'total run' in txt:
        lines=txt.splitlines()
        keep=[l for l in lines if any(k in l for k in ['subjects done','total run','min ','three_level','summary_file','electrodes with a significant','(a) subjects','MTL alpha','p_subject:','p_electrode:','implv ','within_10pct','code      ','mtmfft    ','(b) with','(a) main','direction (pair','overlap with','systems with','condition 1','condition 2','condition 3','rt:','elogit'])]
        print(tags[:1], '\n'.join(keep[:40]))
EOF
```

```
[] 4 subjects done after 8.8 min
[] 6 subjects done after 18.9 min
[] 9 subjects done after 23.8 min
[] 10 subjects done after 35.3 min
['claim:behavior-proficient'] all_120_trials: min 0.792 (expected 0.79 +- 0.079), max 0.967 (expected 0.97 +- 0.097), all in [0.711, 1.0]: True; min ok True, max ok True
kept_trials: min 0.792 (expected 0.79 +- 0.079), max 1.000 (expected 0.97 +- 0.097), all in [0.711, 1.0]: True; min ok True, max ok True
['claim:behavior-no-difficulty-difference']   elogit: {'spatial_vs_identity_p': np.float64(0.0228), 'temporal_vs_identity_p': np.float64(0.6603), 'three_level_chi2': 5.8321, 'three_level_p': 0.0541, 'numeric_z': np.float64(0.394), 'numeric_p': np.float64(0.6936)}
  rt: {'spatial_vs_identity_p': np.float64(0.0), 'temporal_vs_identity_p': np.float64(0.0), 'three_level_chi2': 26.5562, 'three_level_p': 0.0, 'numeric_z': np.float64(-3.5113), 'numeric_p': np.float64(0.0004)}
  elogit: {'spatial_vs_identity_p': np.float64(0.1599), 'temporal_vs_identity_p': np.float64(0.5002), 'three_level_chi2': 1.9765, 'three_level_p': 0.3722, 'numeric_z': np.float64(0.6651), 'numeric_p': np.float64(0.506)}
  rt: {'spatial_vs_identity_p': np.float64(0.0), 'temporal_vs_identity_p': np.float64(0.0), 'three_level_chi2': 26.2517, 'three_level_p': 0.0, 'numeric_z': np.float64(-3.3878), 'numeric_p': np.float64(0.0007)}
summary_file.csv response time, mean and SD over subjects: {1: {'mean': 1659.3, 'std': 701.3}, 2: {'mean': 1335.5, 'std': 574.3}, 3: {'mean': 1475.4, 'std': 733.9}}
  rt (summary_file.csv): {'spatial_vs_identity_p': np.float64(0.0018), 'temporal_vs_identity_p': np.float64(0.0769), 'three_level_chi2': 9.7556, 'three_level_p': 0.0076, 'numeric_z': np.float64(-1.5537), 'numeric_p': np.float64(0.1203)}
condition 1: accuracy 0.900 vs 0.9 +- 0.04: True; rt 1744 vs 1659 +- 701: True
condition 2: accuracy 0.920 vs 0.92 +- 0.09: True; rt 1237 vs 1335 +- 574: True
condition 3: accuracy 0.890 vs 0.89 +- 0.09: True; rt 1292 vs 1475 +- 734: True
['claim:elec
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('executed/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    txt=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    if 'claim:psi-theta-shift' in tags or 'claim:pac-mtl-spatial' in tags:
        print('\n'.join(l for l in txt.splitlines() if (' a ' in l and 'spatial' in l) or 'MTL-' in l or 'pac-' in l)[:5000])
EOF
```

```
mtmfft MTL-PFC    172         9        z     -0.1379          6          3      -0.0225           9          10          0.1154   1.2177 0.2714
 mtmfft MTL-PFC    172         9      raw     -0.1379          6          3      -0.0225           9          10          0.0002   0.0008 0.9781
 mtmfft MTL-OFC    302         7        z     -0.1276          7         14      -0.1756          17           5         -0.0480   0.3438 0.5581
 mtmfft MTL-OFC    302         7      raw     -0.1276          7         14      -0.1756          17           5         -0.0009   0.2620 0.6091
sliding MTL-PFC    172         9        z     -0.2537         58         43       0.1901          48          58          0.4438   3.4356 0.0655
sliding MTL-PFC    172         9      raw     -0.2537         58         43       0.1901          48          58          0.0048   3.1192 0.0792
sliding MTL-OFC    302         7        z     -0.3866        115         70      -0.3607         112          73          0.0259   0.0221 0.8820
sliding MTL-OFC    302         7      raw     -0.3866        115         70      -0.3607         112          73          0.0025   4.9359 0.0270
   code MTL-PFC    172         9        z     -3.9095         98         53       7.9657          53         105         11.8752  13.8742 0.0003
   code MTL-PFC    172         9      raw     -3.9095         98         53       7.9657          53         105          0.0834  34.8513 0.0000
   code MTL-OFC    302         7        z    -10.7334        196         76       7.6854         110         169         18.4188  37.1811 0.0000
   code MTL-OFC    302         7      raw    -10.7334        196         76       7.6854         110         169          0.1391 113.1365 0.0000
expected pairs: MTL-PFC 172 +- 17.2, MTL-OFC 303 +- 30.3
     MTL  spatial       a     21         9   12140     0.0378       38.5              8        0.2                 8    0.00717     0.0143 0.000197        0.197       0.0076         0.18               0.9
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s,indent=0)[:6000])" 2>/dev/null || ls schemas
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
{
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "One attempt at reproducing the claims of a target",
"description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
"type": "object",
"additionalProperties": false,
"required": [
"schema_version",
"id",
"dataset",
"paper",
"date",
"provenance",
"outcomes"
],
"properties": {
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
for k in ['inputs','findings']: print(k, json.dumps(p[k])[:1500])
print([k for k in p])"; ls questions | grep -i crcns; head -30 questions/000005.yaml
```

```
inputs {"description": "Everything the attempt used that is not in the dataset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}
findings {"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}, "found": {"description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blind, did not report (docs/protocol.md, \"Repeat attempts\").", "enum": ["on_prompt"]}}}}
['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
crcns-ac-2.yaml
crcns-alm-3.yaml
crcns-bf-1.yaml
crcns-bf-3.yaml
crcns-ear-1.yaml
crcns-fcx-1.yaml
crcns-hc-13.yaml
crcns-hc-16.yaml
crcns-hc-24.yaml
crcns-hc-7.yaml
crcns-nac-1.yaml
crcns-ofc-4.yaml
crcns-pfc-1.yaml
crcns-pfc-2.yaml
crcns-ret-1.yaml
crcns-rrf-1.yaml
crcns-ssc-7.yaml
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
head -8 questions/crcns-fcx-1.yaml; date -u
```

```
# Questions from attempt crcns-fcx-1-watson-2016-01 (author revision after verifier round 1,
# 2026-11-07) about claims/crcns-fcx-1/10.1016-j.neuron.2016.03.036.yaml, asked under docs/protocol.md,
# "Hand over for verification". The verifier reported these as places where the claims file misreads
# the paper; the claims were tested as the file has them.
dataset: crcns:fcx-1
paper: doi:10.1016/j.neuron.2016.03.036
questions:
- claim: post-sleep-wake-lower
Sun Nov  8 22:42:18 UTC 2026
```

**Agent**

Now the questions file, attempt record and README.

**Agent calls Write**

```json
{
 "file_path": "questions/crcns-fcx-2.yaml",
 "content": "# Questions from attempt crcns-fcx-2-johnson-2018-01 (author run, 2026-11-08) about\n# claims/crcns-fcx-2/10.1371-journal.pbio.2004274.yaml, asked under docs/protocol.md, Author, step 1.6.\n# The claim was tested as the file has it.\ndataset: crcns:fcx-2\npaper: doi:10.1371/journal.pbio.2004274\nquestions:\n- claim: behavior-no-difficulty-difference\n  asked: 2026-11-08\n  question: Should the criterion also name the reading in which condition enters the two models as a\n    single numeric term? The criterion names (a) each relation condition against identity and (b) one\n    3-level condition term, and notes that the printed F(1,28) does not fit a 3-level factor. One value\n    per subject and condition (30 rows) with an intercept and a single condition slope gives exactly\n    28 residual degrees of freedom and one numerator degree of freedom.\n  passage: 'mixed-effects model, accuracy: F 1,28 < 0.10, p > 0.75; correct-trial response time: F\n    1,28 < 2.55, p > 0.12 (Results, paragraph 2); Accuracy and correct-trial response time data were\n    submitted to logit and linear mixed-effects models, respectively, with 3 condition-fixed effects\n    and 10 subject-random effects (Materials and methods, Behavioral task, paragraph 3)'\n  why: On the per-subject response times of the data set's summary_file.csv, whose condition means\n    are the paper's (1659, 1335, 1475 ms), condition as a numeric term gives p = 0.12 (z = -1.55,\n    z squared 2.41, below the paper's 2.55), the paper's \"p > 0.12\", while readings (a) and (b) find\n    an effect (spatial against identity p = 0.0018; 3-level p = 0.0076). Accuracy as a numeric term\n    gives p = 0.69. The claim is not reproduced under the criterion's readings and would be\n    reproduced under the numeric one.\n"
}
```

```
File created successfully at: questions/crcns-fcx-2.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
ls attempts | grep crcns | head; grep -n "verifications\|findings:" attempts/001453-fouke-2025-01.yaml | head; sed -n '/^findings:/,/^[a-z]/p' attempts/001453-fouke-2025-01.yaml | head -20
```

```
crcns-ac-2-deweese-2004-01.yaml
crcns-alm-1-li-2015-01.yaml
crcns-alm-3-li-2016-01.yaml
crcns-bf-1-nair-2018-01.yaml
crcns-bf-3-moaddab-2021-01.yaml
crcns-ear-1-farrell-2020-01.yaml
crcns-fcx-1-watson-2016-01.yaml
crcns-hc-10-lee-2014-01.yaml
crcns-hc-13-yu-2017-01.yaml
crcns-hc-14-girardeau-2017-01.yaml
243:findings:
309:verifications:
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
- kind: metadata_insufficient
  statement: The stimulus codes 0 to 20 have no names or description in the files or the
[... 12 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/crcns-fcx-2-johnson-2018-01.yaml",
 "content": "schema_version: 2\nid: crcns-fcx-2-johnson-2018-01\ndataset:\n  archive: crcns\n  id: fcx-2\n  version: unversioned\n  doi: 10.6080/K0VX0DQD\npaper: doi:10.1371/journal.pbio.2004274\ndate: 2026-11-08\nentry: crcns-fcx-2-johnson-2018\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/42521152357\noutcomes:\n- claim: behavior-proficient\n  outcome: reproduced\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:behavior-proficient\n  measured:\n  - 0.792\n  - 0.967\n  notes: >-\n    Over all 120 trials (reading a) accuracy runs from 0.792 (s5) to 0.967 (s2), every subject in\n    0.711 to 1.0. Over the trials kept in the derived data (reading b) it runs from 0.792 to 1.000,\n    also within tolerance. The trial tables give the same accuracies as docs/summary_file.csv.\n- claim: behavior-no-difficulty-difference\n  outcome: not_reproduced\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:behavior-no-difficulty-difference\n  measured:\n  - 0.900\n  - 0.920\n  - 0.890\n  - 1744\n  - 1237\n  - 1292\n  notes: >-\n    The condition means are within the paper's SDs (accuracy over all trials 0.900, 0.920, 0.890;\n    correct-trial response time from the trial tables 1744, 1237, 1292 ms; from summary_file.csv\n    1659, 1335, 1475 ms, the paper's values). Accuracy (empirical logit, subject random intercept)\n    shows no 3-level effect (p = 0.054 all trials, 0.37 kept trials), but spatial differs from\n    identity over all trials (p = 0.023). Response time differs by condition under both readings of\n    the criterion, with the trial tables (p < 0.001) and with summary_file.csv (spatial against\n    identity p = 0.0018, 3-level p = 0.0076). Only with condition as one numeric term, which has the\n    paper's single numerator degree of freedom, is the effect absent (summary_file.csv response time\n    p = 0.12, z squared 2.41; accuracy p = 0.69), matching the paper's F(1,28) < 2.55, p > 0.12. That\n    reading is not in the criterion, and a reader is asked about it (questions/crcns-fcx-2.yaml).\n  deviations:\n  - >-\n    Accuracy enters the logit model as the empirical logit of each subject and condition, log((k +\n    0.5) / (n - k + 0.5)), in a linear mixed model on 30 rows, as some subjects are at 100% in a\n    condition; the paper does not specify its logit model further.\n  - >-\n    The response times of the trial tables differ from those of summary_file.csv in 7 of 10\n    subjects; both were tested, and the condition means of summary_file.csv are the paper's.\n- claim: electrode-counts\n  outcome: reproduced\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:electrode-counts\n  measured:\n  - 36\n  - 116\n  - 102\n  - 9\n  - 7\n  notes: >-\n    docs/summary_channel_analysis.csv lists 36 MTL, 116 PFC and 102 OFC bipolar channels (254), all\n    present in the derived data. MTL and PFC share a hemisphere in 9 subjects, MTL and OFC in 7. Per\n    subject 3.6 +- 2.0 (1 to 7) MTL, 11.6 +- 8.3 (4 to 28 in 9 subjects) PFC and 10.2 +- 14.4 (1 to\n    47 in 9 subjects) OFC, as the paper gives them.\n- claim: correct-trial-counts\n  outcome: reproduced\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:correct-trial-counts\n  measured:\n  - 100.9\n  - 32.9\n  - 34.8\n  - 33.2\n  - 10.2\n  notes: >-\n    From the trialinfo of the derived data. Per subject 100.9 +- 7.3 correct trials, 32.9 +- 3.3\n    identity (26 to 37), 34.8 +- 3.7 spatial (28 to 39), 33.2 +- 2.7 temporal (28 to 37) and 10.2 +-\n    8.1 incorrect (0 to 25), the paper's ranges exactly.\n- claim: erp-no-condition-difference\n  outcome: not_reproduced\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:erp-no-condition-difference\n  notes: >-\n    With the code's subject-wide cluster null (all of a subject's electrodes in one test, as\n    erp_compute.m runs it), 1 of 254 electrodes has a significant cluster (s5, postcue F test, p =\n    0.034), and the criterion allows none. With a per-electrode null 13 electrodes do, fewer than the\n    25.4 expected by chance over two tests. The effect is small and isolated, but the criterion is\n    no electrode.\n  deviations:\n  - &timeaxis >-\n    Windows follow the time axes of the derived data as the deposited code does (encoding [0, 1.5] s\n    of encmain, postcue [0.3, 1.2] s of proc, baseline [0.65, 0.85] s of pre). The trial table and\n    the descriptor place the events 1.5 s earlier (the first sample of each segment is the table's\n    epoch start), and no task-locked response in the data settles which is right.\n  - >-\n    FieldTrip's filters and cluster test are reimplemented in Python (fir1 design, two-pass,\n    zero padding to 7.5 s; cluster sums, 1000 permutations, p doubled for the two-tailed t test).\n- claim: power-theta-sustained\n  outcome: not_reproduced\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:power-theta-sustained\n  notes: >-\n    Baseline-z power averaged over trials (code zbaseline.m). No subject has a region-average theta z\n    above 1.96 over half of the 50 encoding and delay time points in any region (0 of 10 MTL, 0 of 9\n    PFC, 0 of 9 OFC); per electrode 1 of 36 MTL, 1 of 116 PFC and 11 of 102 OFC meet the rule. MTL\n    alpha is below -1.96 over half the time points in 0 of 10 subjects (0 of 36 electrodes). 239 of\n    254 electrodes have some z above 1.96 above 16 Hz (reported, not judged). While preparing, the\n    same measure with the windows placed by the trial table (1.5 s earlier) was run on s1, s2 and s4\n    and also showed no sustained theta (not run in the notebook).\n  deviations:\n  - *timeaxis\n- claim: power-condition-exclusions\n  outcome: not_reproduced\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:power-condition-exclusions\n  measured:\n  - 12\n  - 6\n  - 5\n  - 5\n  notes: >-\n    With the code's subject-wide null 12 electrodes differ (6 PFC, 5 OFC, 1 MTL) in 5 subjects (s5,\n    s6, s7, s8, s10), against 8 (5 PFC, 3 OFC) in 4. With a per-electrode null 69 electrodes in 9\n    subjects. The measured values are total, PFC, OFC and subjects; 1 MTL electrode is also\n    excluded. The z and raw readings give the same test, as the z is an affine map of power shared\n    by all trials. The 12 are excluded from the later analyses, leaving 35 MTL, 110 PFC and 97 OFC.\n  deviations:\n  - *timeaxis\n- claim: plv-theta-peak\n  outcome: reproduced\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:plv-theta-peak\n  notes: >-\n    Imaginary PLV (reading a), averaged over time and the two delays: a local maximum at 3.5 to 6.5\n    Hz in 7 of 9 subjects for MTL-MTL, 8 of 9 for MTL-PFC and 4 of 7 for MTL-OFC pairs; the phase-lag\n    index (reading b) gives 9 of 9, 8 of 9 and 3 of 7, and the code's own PLV 7, 8 and 7. The rule\n    needs one subject per group, a weak test; the largest value of the spectrum is often outside\n    theta, and theta is often one of several local maxima. The alpha synchrony is not judged.\n  deviations:\n  - *timeaxis\n- claim: psi-theta-shift\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:psi-theta-shift\n  measured:\n  - 172\n  - 302\n  notes: >-\n    With the PSI of the Methods (Nolte, trial-averaged cross-spectrum, frequencies of one signal\n    shuffled for the null) and the code's single Hanning window, precue mean z is -0.14 (MTL-PFC)\n    and -0.13 (MTL-OFC), with 6 against 3 frontal and MTL leads in MTL-PFC but 7 against 14 in\n    MTL-OFC, and postcue does not exceed precue (p = 0.27 and 0.56 on z; 0.98 and 0.61 on raw PSI).\n    With sliding 3-cycle windows part (1) holds in both networks and part (2) only for MTL-OFC on raw\n    PSI (p = 0.027; MTL-PFC p = 0.079), which the criterion calls partial. With the code's own form\n    of PSI (psianalysis.m, conjugate added) both parts hold in both networks (precue mean z -3.9 and\n    -10.7, 98 against 53 and 196 against 76 leads; postcue minus precue p = 0.0003 and < 0.0001). The\n    pair counts are 172 and 302 (expected 172 and 303). A question for the authors is recorded under\n    findings.\n  deviations:\n  - >-\n    Assumed, the single Hanning window over the 900 ms segment of psi_compute.m (FieldTrip mtmfft),\n    with the Methods' PSI. The Methods' sliding 3-cycle windows cannot be placed inside a 900 ms\n    segment at 3 Hz (a 1 s window); the sliding reading run here lets windows run into the zero\n    padding. The code's own PSI is shown as a variant; it averages per-trial PSI and z-scores it\n    against a null built from trial-averaged coherency, which is not the Methods' procedure.\n  - >-\n    The mixed model with random intercepts for subject and pair is computed as the within-pair F\n    test of interval (equal for two intervals per pair), with all pairs after the 12 exclusions.\n  - *timeaxis\n- claim: crossspectral-shift\n  outcome: not_reproduced\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:crossspectral-shift\n  measured:\n  - 35\n  - 110\n  - 97\n  notes: >-\n    With the PSI of the Methods, no precue electrode or pair passes z > 1.96 (part 2 holds), but\n    postcue exceeds precue in 1 of 7 systems on z (MTL to OFC, p = 0.036) and 0 of 7 on raw PSI.\n    With the code's form, 2 of 7 systems show the shift (MTL to PFC, MTL to OFC), and 24% to 55% of\n    precue units per system pass z > 1.96. The models hold 35 MTL, 110 PFC and 97 OFC electrodes\n    (expected 36, 111, 99) and 172 and 302 pairs.\n  deviations:\n  - >-\n    Cross-spectral PSI uses the code's single window only (the sliding variant was run for theta PSI\n    alone, for time).\n  - *timeaxis\n- claim: phase-directing-counts\n  outcome: not_reproduced\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:phase-directing-counts\n  measured:\n  - 0\n  - 0\n  - 0\n  - 0\n  - 0\n  - 0\n  - 0\n  - 0\n  - 0\n  notes: >-\n    With the PSI of the Methods no electrode or pair passes postcue z > 1.96 (0 of 7 counts within\n    10%). With the code's form of PSI the counts are 21 MTL, 43 PFC, 38 OFC, 106 MTL to PFC, 70 PFC\n    to MTL, 200 MTL to OFC and 168 OFC to MTL (expected 13, 52, 38, 56, 85, 93, 115), 1 of 7 within\n    10%; subjects with directing MTL electrodes 9 (expected 8) and with MTL to OFC pairs 5\n    (expected 5). The measured values are those of the Methods' PSI, the first reading.\n  deviations:\n  - *timeaxis\n- claim: crossspectral-equal-strength\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:crossspectral-equal-strength\n  notes: >-\n    On the pairs selected by the code's PSI (106 MTL to PFC and 70 PFC to MTL in 9 subjects; 200 MTL\n    to OFC and 168 OFC to MTL in 7), the code's per-frequency z differs across amplitude frequencies\n    in both networks (main effects only p = 0.017 and 7.8e-05; with the interaction p = 0.016 and\n    6.9e-05), and frequency x direction is significant (p = 0.00016 and 2.6e-06). Direction is not\n    (p = 0.21 and 0.83). The local variant (frequency only) finds no effect in MTL, PFC or OFC (p =\n    0.63, 0.30, 0.89).\n  deviations:\n  - >-\n    Assumed, the phase-directing pairs of the code's form of PSI, as the Methods' PSI selects no\n    pairs and the paper's counts are approached only under the code's form.\n  - >-\n    The model's frequency and frequency x direction tests are the within-pair F tests (random\n    intercepts, every pair having all 16 frequencies); direction is tested on pair means with a\n    subject random intercept.\n  - *timeaxis\n- claim: theta-peak-bands\n  outcome: not_reproduced\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:theta-peak-bands\n  measured:\n  - 2\n  - 0\n  - 1\n  - 1\n  notes: >-\n    Over all analysed electrodes (reading a) the maxima of the 6 filters fall at 1.5-4 Hz in 3\n    subjects, 6-10 Hz in 3, 2-5 Hz in 2, 4-7 Hz in 1 and 5-8 Hz in 1; 6 subjects peak outside the\n    paper's four bands and the overlap with its counts is 4 of 10 (partial needs 7). On the\n    directing electrodes of the code's PSI (reading b) the overlap is 5 of 10; the Methods' PSI\n    selects none. The curves are flat (trial-, time- and electrode-averaged z between about -1.2 and\n    1.7). The measured values are the counts at 2-5, 3-6, 4-7 and 5-8 Hz under reading (a).\n  deviations:\n  - The paper's visual confirmation of the peaks is not reproducible and is left out.\n  - *timeaxis\n- claim: pac-mtl-spatial\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:pac-mtl-spatial\n  notes: >-\n    21 MTL electrodes in 9 subjects (code's PSI selection). Spatial model condition p = 0.0072\n    (surrogate a) and 0.016 (b), above 0.05/7 = 0.0071; condition x frequency p = 0.20 and 0.14.\n    Spatial is above identity (mean difference 0.038 z), with the largest difference at 38.5 Hz.\n    The temporal model has no condition effect below 0.05/7 (part 3 holds).\n  deviations:\n  - &pacsel >-\n    Assumed, the theta-phase directing units of the code's form of PSI, as the Methods' PSI selects\n    none and the paper's counts are approached only under the code's form.\n  - &pacmodel >-\n    PAC on the individual theta band of reading (a) of theta-peak-bands (a 1.5-4 Hz or 6-10 Hz\n    maximum mapped to 2-5 or 5-8 Hz, an assumption), per condition with the condition's trial mean\n    removed (the code's subtracterp.m selects the temporal trials by column 5 == 2, which no trial\n    meets; the Methods' condition 3 is used). Mixed models with random intercepts computed as the\n    within-unit F tests of the balanced 2 x 16 x 19 design; the direction main effect on unit means\n    with a subject random intercept.\n  - *timeaxis\n- claim: pac-frontal-no-condition\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:pac-frontal-no-condition\n  notes: >-\n    43 PFC and 38 OFC electrodes. Condition effects pass 0.05/7 in the PFC spatial model (condition x\n    time p = 3.7e-06), the PFC temporal model (condition x frequency x time p = 2.9e-06) and the OFC\n    spatial model (condition p = 1.8e-06), under surrogate (a); (b) gives the same pattern.\n  deviations:\n  - *pacsel\n  - *pacmodel\n  - *timeaxis\n- claim: pac-mtl-pfc-spatial\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:pac-mtl-pfc-spatial\n  notes: >-\n    106 MTL to PFC pairs in 7 subjects. Spatial model condition p = 0.19 (a) and 0.17 (b), with\n    spatial PAC below identity (mean difference -0.008); condition x time p = 2.3e-05 (a).\n  deviations:\n  - *pacsel\n  - *pacmodel\n  - *timeaxis\n- claim: pac-mtl-pfc-temporal\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:pac-mtl-pfc-temporal\n  notes: >-\n    106 MTL to PFC pairs. Temporal model condition p = 0.36 (a) and 0.45 (b), temporal below identity\n    (mean difference -0.006).\n  deviations:\n  - *pacsel\n  - *pacmodel\n  - *timeaxis\n- claim: pac-pfc-mtl-no-condition\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:pac-pfc-mtl-no-condition\n  notes: >-\n    70 PFC to MTL pairs in 9 subjects. The temporal model's condition effect is p = 5.8e-06 (a) and\n    7.7e-07 (b), below 0.05/7, with temporal above identity; the spatial model's condition p =\n    0.0059 (a) is also below 0.05/7.\n  deviations:\n  - *pacsel\n  - *pacmodel\n  - *timeaxis\n- claim: pac-mtl-ofc-spatial\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:pac-mtl-ofc-spatial\n  notes: >-\n    200 MTL to OFC pairs in 5 subjects and 168 OFC to MTL pairs in 6. MTL to OFC spatial condition p\n    = 0.015 (a) and 0.031 (b), above 0.05/7; condition x frequency p = 0.61 (a). The largest spatial\n    minus identity difference is at 9.5 Hz (part 2 holds). The MTL to OFC temporal and the OFC to MTL\n    models have condition effects below 0.05/7 (part 3 fails).\n  deviations:\n  - *pacsel\n  - *pacmodel\n  - *timeaxis\n- claim: pac-mtl-pfc-direction\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:pac-mtl-pfc-direction\n  notes: >-\n    106 MTL to PFC and 70 PFC to MTL pairs. Condition x direction passes 0.05/15 in both models under\n    (a) (p = 0.0029 spatial, 3.9e-05 temporal), but the relation minus identity difference is larger\n    in the PFC to MTL direction (0.021 and 0.035 against -0.008 and -0.006). The direction effect is\n    p = 0.32 and 0.96, with MTL to PFC slightly higher.\n  deviations:\n  - *pacsel\n  - *pacmodel\n  - *timeaxis\n- claim: pac-mtl-ofc-direction\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_johnson_2018.ipynb\n  output: claim:pac-mtl-ofc-direction\n  notes: >-\n    200 MTL to OFC and 168 OFC to MTL pairs. In the spatial model direction p = 0.13 and condition x\n    direction p = 0.17 (a); the temporal model has effects below 0.05/15 (condition x direction p =\n    1.9e-06).\n  deviations:\n  - *pacsel\n  - *pacmodel\n  - *timeaxis\nfindings:\n- kind: metadata_error\n  statement: >-\n    The trial table's epoch columns and the derived data's time axes disagree by 1.5 s. The first\n    sample of each derived segment (time -1.5 s) is the table's epoch start (encmain at column H,\n    \"encoding and pre-cue delay epoch start\"; proc 0.3 s before column I; pre about 0.1 s after\n    column G), and a derived trial of s8 matches the primary data from sample H on. The deposited\n    code takes stimulus onset at time 0 of encmain, 1.5 s after column H, while the descriptor\n    places it at H. The data show no task-locked high-gamma or evoked response that settles which\n    is right.\n- kind: metadata_error\n  statement: >-\n    The response times of docs/summary_file.csv, which the descriptor says are \"calculated on all\n    correct trials\", differ from the mean over correct trials of the per-trial tables in 7 of 10\n    subjects (s1 identity 1948 against 2348 ms). The paper's condition means are those of\n    summary_file.csv. Its accuracies do equal the per-trial tables.\n- kind: metadata_error\n  statement: >-\n    For s10 the trial table's epoch columns are not on the derived data's sample grid (offsets of\n    97.1 to 98.1 samples from column G, 114 for two trials, and fractional offsets for H and I),\n    and its trialinfo does not equal the trial table's columns.\n- kind: metadata_error\n  statement: >-\n    The descriptor gives fsample 1000 for the derived structures; s8 and s9 are at 512 Hz (as its\n    note on the trial table says).\n- kind: code_mismatch\n  statement: >-\n    The deposited psianalysis.m multiplies the Fourier coefficients without conjugating one of them,\n    so its \"cross-spectral density\" and phase slope are not the PSI of Nolte et al. that the Methods\n    cite. It also z-scores the trial mean of per-trial PSI against a null built from trial-averaged\n    coherency, which inflates z; with the conjugate added, this form gives z of 5 to 20 where the\n    Methods' PSI gives z near 0, and only this form approaches the paper's counts of phase-directing\n    electrodes.\n- kind: code_mismatch\n  statement: >-\n    subtracterp.m with ncond = 3 selects the temporal trials by trialinfo column 5 == 2 (the delay\n    length column, 900 or 1150), so the temporal condition is empty; pacanalysis.m sizes its\n    amplitude matrix with an undefined variable `freq`; and dirpac_compute.m calls pacanalysis with\n    six arguments while it takes four, so the deposited PAC scripts cannot run as given.\n- kind: paper_inconsistency\n  statement: >-\n    The Methods describe PSI from sliding 3-cycle windows (dt = 3/f) at 3 to 7 Hz on 900 ms segments;\n    a 3-cycle window at 3 Hz is 1 s long and cannot be placed in the segment. The deposited code uses\n    one Hanning window over the segment.\n- kind: paper_inconsistency\n  statement: >-\n    The behavioural models are said to have \"3 condition-fixed effects\" but are reported as F(1,28);\n    with one value per subject and condition, F(1,28) is what condition as a single numeric term\n    gives, and on summary_file.csv that reading gives the paper's p > 0.12 for response time.\n- kind: methods_unavailable\n  statement: >-\n    Question for the authors. Which form of PSI produced the reported PSI z values and the counts of\n    phase-directing electrodes (the Methods' Nolte PSI on the trial-averaged cross-spectrum, or the\n    code's mean of per-trial PSI against trial-averaged coherency), with which spectral window, and\n    where stimulus onset lies on the derived data's time axes (at 0 s, as the code reads them, or at\n    -1.5 s, as the trial table's columns place it)? The Methods' PSI selects no phase-directing\n    units here, so the PAC claims were tested on the units of the code's form, as an assumption.\n"
}
```

```
File created successfully at: attempts/crcns-fcx-2-johnson-2018-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import yaml;d=yaml.safe_load(open('attempts/crcns-fcx-2-johnson-2018-01.yaml'));print(len(d['outcomes']))
c=yaml.safe_load(open('claims/crcns-fcx-2/10.1371-journal.pbio.2004274.yaml'));print(set(x['id'] for x in c['claims'])-set(o['claim'] for o in d['outcomes']))
yaml.safe_load(open('questions/crcns-fcx-2.yaml'))" && python tools/entry.py check entries/crcns-fcx-2-johnson-2018 2>&1 | tail; date -u
```

```
21
set()
0 error(s)
Sun Nov  8 22:43:58 UTC 2026
```

**Agent calls Bash**

```bash
sed -i 's/    97.1 to 98.1 samples from column G, 114 for two trials, and fractional offsets for H and I),/    97.1 to 98.1 samples from column G, about 114 for two trials, and fractional offsets for H and I),/' attempts/crcns-fcx-2-johnson-2018-01.yaml && cat > entries/crcns-fcx-2-johnson-2018/README.md <<'EOF'
# Johnson et al. (2018) from CRCNS fcx-2

Tests the findings of [Johnson et al. (2018)](https://doi.org/10.1371/journal.pbio.2004274) on
CRCNS [fcx-2](https://doi.org/10.6080/K0VX0DQD), which holds the preprocessed intracranial EEG of
the paper's 10 subjects (254 bipolar MTL, PFC and OFC electrodes) in the visuospatial working memory
task, with trial tables and the paper's MATLAB analysis scripts.

| Claim | Outcome |
|---|---|
| All subjects proficient (accuracy 0.79 to 0.97) | Reproduced |
| Accuracy and response time do not differ by condition | Not reproduced |
| 254 electrodes, 36 MTL, 116 PFC, 102 OFC | Reproduced |
| About 100 correct trials per subject | Reproduced |
| ERPs do not differ by condition | Not reproduced |
| Sustained theta power in all regions | Not reproduced |
| 8 electrodes with power condition effects | Not reproduced |
| PLV peaks in theta | Reproduced |
| Theta PSI shifts from frontal to MTL leads | Not reproduced |
| Cross-spectral PSI shifts after the test cue | Not reproduced |
| Counts of theta phase-directing electrodes and pairs | Not reproduced |
| Equal cross-spectral strength across frequencies and directions | Not reproduced |
| Individual theta peak bands | Not reproduced |
| Theta PAC by condition (eight claims) | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The trial table and the descriptor place the task events 1.5 s earlier than the time axes of the
derived data, which the paper's code follows, and the data show no task-locked response that
settles it. The PSI of the paper's Methods selects no phase-directing units; the PAC claims use the
units of the deposited code's own form of PSI. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/crcns-fcx-2-johnson-2018-01.yaml`](../../attempts/crcns-fcx-2-johnson-2018-01.yaml).
EOF
. $TMPDIR/dev/bin/activate && python tools/entry.py check entries/crcns-fcx-2-johnson-2018 2>&1 | tail -3 && python tools/entry.py handover entries/crcns-fcx-2-johnson-2018 2>&1 | tail -5; git status --short; date -u
```

```
0 error(s)
wrote executed/crcns-fcx-2-johnson-2018/handover
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
?? attempts/crcns-fcx-2-johnson-2018-01.yaml
?? entries/crcns-fcx-2-johnson-2018/
?? questions/crcns-fcx-2.yaml
?? scripts
Sun Nov  8 22:44:36 UTC 2026
```

**Agent calls Bash**

```bash
ls -la .bashrc .profile .gitconfig .mcp.json .ripgreprc scripts .idea .vscode 2>&1 | head -20; ls entries/crcns-fcx-2-johnson-2018/
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 20:37 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 20:37 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 20:37 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 20:37 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 20:37 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 20:37 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 20:37 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 20:37 scripts
README.md
__pycache__
entry.yaml
fcx2.py
reproduce_johnson_2018.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
rm -rf entries/crcns-fcx-2-johnson-2018/__pycache__; . $TMPDIR/dev/bin/activate && python tools/entry.py check entries/crcns-fcx-2-johnson-2018 | tail -1; date -u
```

```
0 error(s)
Sun Nov  8 22:44:49 UTC 2026
```

**Agent**

I tested all 21 claims on fcx-2. Five are reproduced and 16 are not; none are blocked. The entry passes `check`, the full notebook ran in 35.5 minutes from a clean environment, and the handover package is built. Nothing is committed.

## 1. Outcomes

| claim | outcome |
|---|---|
| behavior-proficient | reproduced (accuracy 0.792 to 0.967) |
| behavior-no-difficulty-difference | not reproduced (response time differs by condition) |
| electrode-counts | reproduced (36, 116, 102; 9 and 7 subjects) |
| correct-trial-counts | reproduced |
| erp-no-condition-difference | not reproduced (1 of 254 electrodes significant; the criterion allows none) |
| power-theta-sustained | not reproduced (0 subjects in any region) |
| power-condition-exclusions | not reproduced (12 electrodes in 5 subjects, against 8 in 4) |
| plv-theta-peak | reproduced (the rule is weak: one subject per group is enough) |
| psi-theta-shift | not reproduced, rests on an assumption (it holds only under the code's own PSI) |
| crossspectral-shift | not reproduced (shift in 1 of 7 systems; 2 of 7 under the code's PSI) |
| phase-directing-counts | not reproduced (0 units with the Methods' PSI; 1 of 7 counts within 10% with the code's) |
| crossspectral-equal-strength | not reproduced, rests on an assumption |
| theta-peak-bands | not reproduced (4 of 10 subjects match the paper's bands) |
| 8 PAC claims | all not reproduced, all rest on an assumption |

## 2. What was found about the dataset

- **Pinned version:** the live files (descriptor version 0.61). CRCNS does not version data sets, so it is recorded as `unversioned` with the MD5 sums in the notebook header; `orig/ver_0_6` holds only documents and scripts.
- **1.5 s timing conflict:** the trial table and the descriptor place the task events 1.5 s earlier than the time axes of the derived data, which the authors' code follows. I matched a derived trial of s8 against the raw recording to confirm where it starts. No task-locked response in the data settles which is right, so the analysis follows the code. All windowed outcomes depend on this.
- **Response times:** the per-subject response times in `summary_file.csv` differ from the trial tables in 7 of 10 subjects. The paper's condition means are the `summary_file.csv` ones.
- **s10:** its trial table is not on the derived data's sample grid.
- **Analysis code:** the deposited `psianalysis.m` omits the complex conjugate, and its form of PSI inflates z. Three PAC scripts cannot run as given (an empty temporal condition, an undefined variable, a wrong number of arguments).
- **Paper:** the Methods' 3-cycle PSI windows cannot fit a 900 ms segment at 3 Hz. The behaviour models are described with 3 condition levels but reported as F(1,28).

**Assumptions:**
- The code's single Hanning window for PSI.
- PAC units are selected with the code's form of PSI, since the Methods' PSI selects none.
- Empirical logit for accuracy.
- A peak at 1.5–4 or 6–10 Hz is mapped to the nearest of the paper's bands for PAC.

**Question for the authors** (recorded as a finding): which PSI form and window produced the reported values, and where stimulus onset lies on the derived time axes.

**Question for a reader** (`questions/crcns-fcx-2.yaml`): the behaviour criterion leaves out condition as a single numeric term. That reading matches the paper's F(1,28) and gives its p > 0.12 for response time; under it the claim would be reproduced.

## 3. Where the protocol was unclear

1. Clock check: the derived data's time axes and the trial table disagree, and the data have no task-locked response. I did not shift every window, which would have doubled a 35-minute run. I recorded it as a finding and as a deviation on each windowed claim.
2. Methods and code disagree on a method that the Methods describe in a way that cannot run (sliding windows). I used the code's window as the stated assumption and ran the sliding windows as a variant.
3. A claim depends on a selection that is empty under the main reading (no phase-directing units, so no PAC). The protocol does not say whether that blocks the claim or allows another reading. I tested on the code-form units and marked `assumed: true`.
4. archives.md says to use `fsspec`, but the files are `.tar.gz`, not zip. Streaming the tar with `requests` was about 5 times faster (46 against 10 MB/s), so I used it.
5. Dev cache: to develop without re-streaming 14 GB, I kept per-subject results (not raw data) in `$TMPDIR`. One 210 MB member was briefly saved to disk while exploring and then deleted.
6. Absence claims with ambiguous tests (the behaviour F(1,28)): the protocol says to judge on "the paper's test alone", but the paper's test is unclear. I applied the criterion's readings and asked a reader.

## 4. Runtime and failures

The development run took 35 minutes and the final run 35.5 minutes, with peak memory 5.9 GB. Nothing failed in the final run. The notebook exceeds the 10-minute aim because all 14 GB must be streamed and the cluster permutations and PAC surrogates are run in full.

Files are in `entries/crcns-fcx-2-johnson-2018/`:
- `reproduce_johnson_2018.ipynb`
- `fcx2.py`

The record and question are `attempts/crcns-fcx-2-johnson-2018-01.yaml` and `questions/crcns-fcx-2.yaml`.

## End of run

82 turns, 123 minutes, $9.05 at API prices, result: success.
