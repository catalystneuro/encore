# openneuro-ds002778 · author · run 40594416398

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; wc -l docs/protocol.md README.md docs/design.md docs/archives.md; ls claims/openneuro-ds002778 paper entries/001453-fouke-2025 claims/001453
```

```
Tue Oct 27 22:26:42 UTC 2026
  612 docs/protocol.md
  137 README.md
  271 docs/design.md
  287 docs/archives.md
 1307 total
claims/001453:
10.1016-j.cub.2025.04.027.yaml

claims/openneuro-ds002778:
10.1523-eneuro.0151-19.2019.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

[... 4 more lines not kept]
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

**Agent calls Read**

```json
{
 "file_path": "claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml"
}
```

```
1	# Claims for Jackson, Cole, Voytek & Swann (2019), eNeuro 6(3) ENEURO.0151-19.2019, on OpenNeuro ds002778.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
3	# protocol as stated in docs/protocol.md.
4	#
5	# Text read: the version of record, full text from Europe PMC PMC6553574 (main text, Methods, figure
6	# legends, Tables 1 to 3). The only supplement is Extended Data 1, the analysis code, which is the
7	# GitHub repository read below. Figures were not opened; no claim needs a value read off a figure.
8	#
9	# Code read: https://github.com/SwannLab/Jackson_2019 at commit a7c89f50106aa4ccec76ace18bbfa45a5440545e
10	# (2020-05-19). It holds utils.py (loading the preprocessed traces, shape and PAC per recording),
11	# shape.py (zero crossings, peaks and troughs, sharpness, steepness), pac.py (normalized modulation
12	# index, Ozkurt and Schnitzler 2011) and notebooks Figure_1, Figures_2,3 and Figure_4. The notebooks
13	# print the Wilcoxon, rank sum, Spearman and Cohen's d values of Tables 1 and 2 (beta) and Figure 3.
14	# The code starts from preprocessed MATLAB files (AVG_motor.mat, rejectscombined.mat) that are not in
15	# the repository: the MATLAB preprocessing, the manual artifact marks, the mu/alpha analysis, the
16	# bipolar and CSD analyses, the F7/F8 and T7/T8 tests, the power spectra, the topographies and the Q4
17	# effect sizes (Table 3) are not in the code.
18	#
19	# Data the paper used (Methods, Participants and Data collection): resting scalp EEG from a dataset
20	# first published by George et al. (2013) and reanalysed by Swann et al. (2015). 15 PD patients (8
[... 621 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md; sed -n 1,80p docs/design.md; grep -n -A60 "## OpenNeuro" docs/archives.md
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
[... 258 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]); print('----')
print(len(nb['cells']))
"; cat ../../attempts/001453-fouke-2025-01.yaml | head -150
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
[... 350 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,400p attempts/001453-fouke-2025-01.yaml | grep -n -B2 -A30 "findings:" | head -80; ls schemas tools; ls questions | head
```

```
92-  notes: Needs the imaging, the tail tracking and the registration to the mapzebrain atlas, none
93-    of which is in the dandiset.
94:findings:
95-- kind: data_missing
96-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
97-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
98-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
99-    notebooks only. Nine of the paper's main findings cannot be tested.
100-- kind: metadata_insufficient
101-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
102-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
103-    file of its stimulus software.
104-- kind: code_mismatch
105-  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
106-    while its conversion of the stimulus software's names gives the reverse (it carries a remap
107-    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
108-    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
109-    only if the fish turn with lateral motion.
110-- kind: metadata_error
111-  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
[... 55 more lines not kept]
```

**Agent**

Read the protocol and claims (25 claims). Now listing the dataset files.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import requests, json
q='{ snapshot(datasetId: "ds002778", tag: "1.0.5") { description { Name ReferencesAndLinks HowToAcknowledge } files(recursive: true) { filename size annexed id urls } } }'
r=requests.post("https://openneuro.org/crn/graphql",json={"query":q}).json()
json.dump(r,open("files.json","w"))
s=r['data']['snapshot']; print(s['description'])
fs=s['files']; print(len(fs))
for f in fs: print(f['filename'],f['size'],f['annexed'],f['urls'][0][:110] if f['urls'] else None)
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
cd $TMPDIR; which python; python --version; uv venv -q dev 2>&1 | tail -1; . dev/bin/activate; uv pip install -q requests pandas numpy scipy mne fsspec aiohttp matplotlib pyyaml 2>&1 | tail -2; python -c "import mne;print(mne.__version__)"
```

```
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
Python 3.13.16
1.13.2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import requests, json
q='{ snapshot(datasetId: "ds002778", tag: "1.0.5") { description { Name ReferencesAndLinks HowToAcknowledge } files(recursive: true) { filename size annexed id urls } } }'
r=requests.post("https://openneuro.org/crn/graphql",json={"query":q}).json()
json.dump(r,open("files.json","w"))
s=r['data']['snapshot']; print(s['description'])
fs=s['files']; print(len(fs))
for f in fs: print(f['filename'],f['size'],f['annexed'],f['urls'][0][:120] if f['urls'] else None)
EOF
```

```
<persisted-output>
Output too large (59.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6ab43d83-cf94-4395-a194-1d247b291768/tool-results/bz8soi9rk.txt

Preview (first 2KB):
{'Name': "UC San Diego Resting State EEG Data from Patients with Parkinson's Disease", 'ReferencesAndLinks': None, 'HowToAcknowledge': None}
331
CHANGES 379 False https://openneuro.org/crn/datasets/ds002778/objects/93c0178706f0dce951b51a92752546d97114e209?filename=CHANGES
README 4657 False https://openneuro.org/crn/datasets/ds002778/objects/ea8bacc7800903196c71b1038217d70d5d2b5c1f?filename=README
dataset_description.json 354 False https://openneuro.org/crn/datasets/ds002778/objects/e55a148a871db000687a2b0d6bec3600a9c948ce?filename=dataset_descriptio
.gitattributes 284 False https://openneuro.org/crn/datasets/ds002778/objects/cbe8be6ae0096250c16bdc3640e50742989569e1?filename=.gitattributes
participants.json 1273 False https://openneuro.org/crn/datasets/ds002778/objects/341cc89f54cd4457a2752eda38645f7cbe49a015?filename=participants.json
participants.tsv 1658 False https://openneuro.org/crn/datasets/ds002778/objects/6f6c554e7708bc43ffd7e6b4e76e07907272403f?filename=participants.tsv
task-rest_beh.json 215 False https://openneuro.org/crn/datasets/ds002778/objects/996855d79c321dad305d1e340515663974153379?filename=task-rest_beh.json
sub-pd9/ses-on/sub-pd9_ses-on_scans.tsv 74 False https://openneuro.org/crn/datasets/ds002778/objects/3906eac8edefb3c1dae8303463c3c0c7f4915053?filename=sub-pd9_ses-on_sca
sub-pd9/ses-on/eeg/sub-pd9_ses-on_task-rest_channels.tsv 2271 False https://openneuro.org/crn/datasets/ds002778/objects/6f4295b89a4389f8f1f4dbdd492b688b1c9a0a1c?filename=sub-pd9_ses-on_tas
sub-pd9/ses-on/eeg/sub-pd9_ses-on_task-rest_eeg.bdf 11787264 True https://s3.amazonaws.com/openneuro.org/ds002778/sub-pd9/ses-on/eeg/sub-pd9_ses-on_task-rest_eeg.bdf?versionId=6LUL4iF80M
sub-pd9/ses-on/eeg/sub-pd9_ses-on_task-rest_eeg.json 471 False https://openneuro.org/crn/datas
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import json, collections, re, pandas as pd, requests
fs=json.load(open("files.json"))['data']['snapshot']['files']
kinds=collections.Counter(re.sub(r'sub-[a-z]+\d+','sub-X',f['filename']) for f in fs)
for k,v in sorted(kinds.items()): print(v,k)
bdf=[f['size'] for f in fs if f['filename'].endswith('.bdf')]; print(len(bdf), sum(bdf)/1e9, min(bdf),max(bdf))
u={f['filename']:f['urls'][0] for f in fs}
for n in ['CHANGES','README','dataset_description.json','participants.json','task-rest_beh.json','.gitattributes']:
    print('=====',n); print(requests.get(u[n]).text)
EOF
```

```
1 .datalad/.gitattributes
1 .datalad/config
1 .gitattributes
1 CHANGES
1 README
1 dataset_description.json
1 participants.json
1 participants.tsv
16 sub-X/ses-hc/beh/sub-X_ses-hc_task-rest_beh.json
16 sub-X/ses-hc/beh/sub-X_ses-hc_task-rest_beh.tsv
16 sub-X/ses-hc/eeg/sub-X_ses-hc_task-rest_channels.tsv
16 sub-X/ses-hc/eeg/sub-X_ses-hc_task-rest_eeg.bdf
16 sub-X/ses-hc/eeg/sub-X_ses-hc_task-rest_eeg.json
16 sub-X/ses-hc/eeg/sub-X_ses-hc_task-rest_events.tsv
16 sub-X/ses-hc/sub-X_ses-hc_scans.tsv
15 sub-X/ses-off/beh/sub-X_ses-off_task-rest_beh.json
15 sub-X/ses-off/beh/sub-X_ses-off_task-rest_beh.tsv
15 sub-X/ses-off/eeg/sub-X_ses-off_task-rest_channels.tsv
15 sub-X/ses-off/eeg/sub-X_ses-off_task-rest_eeg.bdf
15 sub-X/ses-off/eeg/sub-X_ses-off_task-rest_eeg.json
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import json, pandas as pd, requests
pd.set_option("display.width",250); pd.set_option("display.max_columns",40); pd.set_option("display.max_rows",200)
fs=json.load(open("files.json"))['data']['snapshot']['files']
u={f['filename']:f['urls'][0] for f in fs}
print(pd.read_csv(u['participants.tsv'],sep="\t").to_string())
for s in ['sub-pd3/ses-off','sub-hc1/ses-hc']:
    b=s.replace('/','_')
    for suf in ['eeg/%s_task-rest_eeg.json','eeg/%s_task-rest_events.tsv','eeg/%s_task-rest_channels.tsv','beh/%s_task-rest_beh.json','beh/%s_task-rest_beh.tsv','%s_scans.tsv']:
        n=s+'/'+suf%b; print('=====',n); print(requests.get(u[n]).text[:3000])
EOF
```

```
participant_id  age gender hand  MMSE  NAART  disease_duration                                                                 rl_deficits                                                                       notes
0         sub-hc1   54      f    r    30     48               NaN                                                                         NaN                                                                         NaN
1         sub-hc2   50      f    r    30     55               NaN                                                                         NaN                                                                         NaN
2         sub-pd3   52      f    r    29     44               9.0                                                                           R                                                                         NaN
3         sub-hc4   50      f    r    30     52               NaN                                                                         NaN                                                                         NaN
4         sub-pd5   67      f    r    29     48               2.0                                               No clear side, perhaps more L                                                                         NaN
5         sub-pd6   62      f    r    30     42               8.0                                                  L OFF meds, more R ON meds  Used preprocessed data from EEGLAB .mat file instead of raw data for pd on
6         sub-hc7   54      f    r    26     48               NaN                                                                         NaN                                                                         NaN
7         sub-hc8   71      f    r    29     41               NaN                                                                         NaN                                                                         NaN
8         sub-pd9   55      f    r    28 
[... 220 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*; grep -n -i "method\|preprocess\|artifact\|filter\|reference\|CSD\|UPDRS" paper/10.1523-eneuro.0151-19.2019.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 21,28p paper/10.1523-eneuro.0151-19.2019.txt; sed -n 32,39p paper/10.1523-eneuro.0151-19.2019.txt; sed -n 45,58p paper/10.1523-eneuro.0151-19.2019.txt; sed -n 64,79p paper/10.1523-eneuro.0151-19.2019.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 64,78p paper/10.1523-eneuro.0151-19.2019.txt | cut -c1-3000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "Waveform shape\|Relationships between\|Table 3\|Q4\|Figure 2\.\]\|Figure 3\.\]\|Figure 4\.\]" paper/10.1523-eneuro.0151-19.2019.txt | cut -c1-200; awk 'NR>=82 && NR<=100' paper/10.1523-eneuro.0151-19.2019.txt | cut -c1-2500
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 60,61p paper/10.1523-eneuro.0151-19.2019.txt | cut -c1-1500; cd $TMPDIR; git clone -q https://github.com/SwannLab/Jackson_2019 j19 2>&1 | tail -2; cd j19 && git log -1 --format=%H && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/j19; cat shape.py pac.py utils.py | grep -v "^\s*$"
```

```
<persisted-output>
Output too large (44.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6ab43d83-cf94-4395-a194-1d247b291768/tool-results/beyc9m5qr.txt

Preview (first 2KB):
"""
shape.py
Tools for quantifying the waveform shape of oscillations
"""
from __future__ import division
import numpy as np
import pac
#import pacpy #wasn't here before
from scipy import io
from scipy.signal import firwin2, firwin
from scipy.signal import filtfilt
"""
def filtandremove(x,rejects, f_osc, Fs=512., w=3, boundary=0):
        # Filter in narrow band
    from pacpy.filt import firf #in filt.py#pacpy.filt
    xn = firf(x, f_osc, Fs, w=w, rmvedge=False)
[... 49 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6ab43d83-cf94-4395-a194-1d247b291768/tool-results/beyc9m5qr.txt"
}
```

```
1	"""
2	shape.py
3	Tools for quantifying the waveform shape of oscillations
4	"""
5	from __future__ import division
6	import numpy as np
7	import pac
8	#import pacpy #wasn't here before
9	from scipy import io
10	from scipy.signal import firwin2, firwin
11	from scipy.signal import filtfilt
12	"""
13	def filtandremove(x,rejects, f_osc, Fs=512., w=3, boundary=0):
14	        # Filter in narrow band
15	    from pacpy.filt import firf #in filt.py#pacpy.filt
16	    xn = firf(x, f_osc, Fs, w=w, rmvedge=False)
17	    #remove rejection indices
18	    xn = np.delete(xn, rejects)
19	    return xn
20	"""
[... 1211 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/j19; python - <<'EOF'
import json
for f in ['Figures_2,3.ipynb','Figure_4.ipynb','Figure_1.ipynb']:
    nb=json.load(open(f)); print('#########',f)
    for c in nb['cells']:
        src=''.join(c['source'])
        out=''
        for o in c.get('outputs',[]):
            out+=''.join(o.get('text',''))+''.join(o.get('data',{}).get('text/plain',''))
        print('>>',src[:1200]); 
        if out: print('OUT:',out[:800])
EOF
```

```
######### Figures_2,3.ipynb
>> Imports
>> %config InlineBackend.figure_format = 'retina'
%matplotlib inline
#python packages
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pac

import seaborn as sns
sns.set_style('white')

import imp
import shape
import utils
imp.reload(utils)
imp.reload(shape)
OUT: /anaconda3/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
[... 461 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import json, pandas as pd, requests, collections
from concurrent.futures import ThreadPoolExecutor
fs=json.load(open("files.json"))['data']['snapshot']['files']
u={f['filename']:f['urls'][0] for f in fs}
def get(n): return n, requests.get(u[n]).text
names=[n for n in u if n.endswith(('_channels.tsv','_events.tsv','_beh.json','_eeg.json','_scans.tsv'))]
with ThreadPoolExecutor(16) as ex: res=dict(ex.map(get,names))
json.dump(res,open('small.json','w'))
st=collections.Counter(); 
for n,t in res.items():
    if n.endswith('_channels.tsv'):
        d=pd.read_csv(__import__('io').StringIO(t),sep='\t'); st[(tuple(d.status.unique()), len(d), tuple(d.units.unique()), tuple(d.low_cutoff.unique()),tuple(d.high_cutoff.unique()))]+=1
print(st)
for n,t in sorted(res.items()):
    if n.endswith('_events.tsv'): print(n.split('/')[-1], t.replace('\n',' | '))
for n,t in sorted(res.items()):
    if n.endswith('_eeg.json'):
        j=json.loads(t); print(n.split('/')[-1], j['RecordingDuration'], j['SamplingFrequency'], j['EEGChannelCount'])
for n,t in sorted(res.items()):
    if n.endswith('_scans.tsv'): print(t.split('\n')[1])
EOF
```

```
Counter({(('good',), 41, ('µV', nan), (np.float64(0.0),), (np.float64(104.0),)): 44, (('good',), 41, ('µV',), (np.float64(0.0),), (np.float64(256.0),)): 2})
sub-hc1_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 6.51953125	0.0	1	3338
sub-hc10_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 4.376953125	0.0	1	2241
sub-hc18_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 3.01171875	0.0	1	1542
sub-hc2_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 8.85546875	0.0	1	4534
sub-hc20_ses-hc_task-rest_events.tsv onset	duration	value	sample | 2.029296875	0.0	1	1039
sub-hc21_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 5.884765625	0.0	1	3013
sub-hc24_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 4.697265625	0.0	1	2405
sub-hc25_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 18.173828125	0.0	1	9305
sub-hc29_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 4.072265625	0.0	1	2085
sub-hc30_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 3.279296875	0.0	1	1679
sub-hc31_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 4.59765625	0.0	1	2354
sub-hc32_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 9.87109375	0.0	1	5054
sub-hc33_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 7.4765625	0.0	1	3828
sub-hc4_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0
sub-hc7_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 6.806640625	0.0	1	3485
sub-hc8_ses-hc_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 6.98828125	0.0	1	3578
sub-pd11_ses-off_task-rest_events.tsv onset	duration	value	sample | 0.0	0.0	65536	0 | 3.115234375	0.0	1	1595
sub-pd11_ses-on_task-rest_events.tsv onset	duration	value	sam
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import json
res=json.load(open('small.json'))
for n,t in sorted(res.items()):
    if n.endswith('_beh.json'):
        j=json.loads(t); print(n.split('/')[-1], j['questionairres'])
EOF
```

```
Exit code 1
sub-hc1_ses-hc_task-rest_beh.json {'Beck': 0, 'UPDRS': 0}
sub-hc10_ses-hc_task-rest_beh.json {'Beck': 1, 'UPDRS': 0}
sub-hc18_ses-hc_task-rest_beh.json {'Beck': 1, 'UPDRS': 0}
sub-hc2_ses-hc_task-rest_beh.json {'Beck': 9, 'UPDRS': 0}
sub-hc20_ses-hc_task-rest_beh.json {'Beck': 0, 'UPDRS': 0}
sub-hc21_ses-hc_task-rest_beh.json {'Beck': 8, 'UPDRS': 0}
sub-hc24_ses-hc_task-rest_beh.json {'Beck': 1, 'UPDRS': 0}
sub-hc25_ses-hc_task-rest_beh.json {'Beck': 7, 'UPDRS': 0}
sub-hc29_ses-hc_task-rest_beh.json {'Beck': 2, 'UPDRS': 0}
sub-hc30_ses-hc_task-rest_beh.json {'Beck': 6, 'UPDRS': 0}
sub-hc31_ses-hc_task-rest_beh.json {'Beck': 2, 'UPDRS': 0}
sub-hc32_ses-hc_task-rest_beh.json {'Beck': 1, 'UPDRS': 0}
sub-hc33_ses-hc_task-rest_beh.json {'Beck': 0, 'UPDRS': 0}
sub-hc4_ses-hc_task-rest_beh.json {'Beck': 0, 'UPDRS': 0}
sub-hc7_ses-hc_task-rest_beh.json {'Beck': 5, 'UPDRS': 0}
sub-hc8_ses-hc_task-rest_beh.json {'Beck': 6, 'UPDRS': 0}
sub-pd11_ses-off_task-rest_beh.json {'Beck': 4, 'Brady kinesia UPDRS': 7, 'H&Y': 2, 'Left UPDRS': 5, 'Rest Tremor UPDRS': 2, 'Right UPDRS': 10, 'Rigidity UPDRS': 7, 'Total UPDRS': 20, 'UPDRS 18-26': 19}
sub-pd11_ses-on_task-rest_beh.json {'Beck': 3, 'Brady kinesia UPDRS': 8, 'H&Y': 2, 'Left UPDRS': 4, 'Rest Tremor UPDRS': 2, 'Right UPDRS': 10, 'Rigidity UPDRS': 4, 'Total UPDRS': 20, 'UPDRS 18-26': 17}
sub-pd12_ses-off_task-rest_beh.json {'Beck': 20, 'Brady kinesia UPDRS': 16, 'H&Y': 3, 'Left UPDRS': 15, 'Rest Tremor UPDRS': 0, 'Right UPDRS': 15, 'Rigidity UPDRS': 14, 'Total UPDRS': 47, 'UPDRS 18-26': 35}
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import json, time, io, fsspec, mne, numpy as np
fs=json.load(open("files.json"))['data']['snapshot']['files']
u={f['filename']:f['urls'][0] for f in fs}
n='sub-pd6/ses-on/eeg/sub-pd6_ses-on_task-rest_eeg.bdf'
t=time.time()
with fsspec.open(u[n],block_size=2**22) as f: b=f.read()
print(len(b), time.time()-t)
t=time.time()
raw=mne.io.read_raw_bdf(io.BytesIO(b),preload=True,verbose='error')
print(time.time()-t, raw.info['sfreq'], raw.ch_names, raw.n_times)
d=raw.get_data(picks=raw.ch_names[:32])*1e6
print(d.mean(1)[:5], d.std(1)[:8], np.abs(d.sum(0)).max(), d[:, :3])
EOF
```

```
18210816 0.9328322410583496
0.8153162002563477 512.0 ['Fp1', 'AF3', 'F7', 'F3', 'FC1', 'FC5', 'T7', 'C3', 'CP1', 'CP5', 'P7', 'P3', 'Pz', 'PO3', 'O1', 'Oz', 'O2', 'PO4', 'P4', 'P8', 'CP6', 'CP2', 'C4', 'T8', 'FC6', 'FC2', 'F4', 'F8', 'AF4', 'Fp2', 'Fz', 'Cz', 'EXG1', 'EXG2', 'EXG3', 'EXG4', 'EXG5', 'EXG6', 'EXG7', 'EXG8', 'Status'] 147968
[-0.00867392 -0.0109268  -0.00880889 -0.00341155 -0.00015396] [22.79639467 15.32623229 12.22921397  9.77939541  5.68862222 10.67538917
 16.68922556  6.50669597] 0.04769217059588904 [[-5.36443091e-01 -7.16151183e+00  3.93547831e+00]
 [-1.01992142e-01  5.15417288e+00 -7.16456931e-01]
 [-1.27321080e-01 -2.17649293e+01 -3.75555048e+01]
 [ 2.34366537e-01  3.27349042e+00  1.07066186e+01]
 [ 1.78873106e-01  2.98855157e+00  4.99656594e+00]
 [-1.81043580e-01  3.89409027e+00  1.10173805e+01]
 [ 2.38244083e-01 -4.45596315e+00 -1.79422246e+01]
 [ 1.76329381e-01  2.28861796e+00  5.81373114e+00]
 [ 3.65130144e-01  6.86788594e-01  1.14070255e+00]
 [-2.76529335e-02 -3.69067445e-01 -1.38762074e+00]
 [ 8.84570535e-02 -2.80152235e+00 -2.14646035e+00]
 [ 1.33419953e-01  3.61994659e-03 -2.11762481e-01]
 [ 2.19646744e-01  1.07422519e+00  9.35967030e-01]
 [-1.80149828e-02 -7.81271746e-01  8.59178531e-02]
 [-1.40251865e-02 -8.44436777e-01 -2.99412116e-01]
 [ 1.79874273e-01 -2.44370565e-02 -6.62594667e-01]
 [ 1.89469145e-01  2.54025147e+00  1.57144421e+00]
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
date -u
```

```
Tue Oct 27 22:28:43 UTC 2026
```

**Agent calls Bash**

```bash
nproc; free -g | head -2; cd $TMPDIR; . dev/bin/activate; python -c "
import mne; m=mne.channels.make_standard_montage('biosemi32'); print(m.ch_names)"
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
['Fp1', 'AF3', 'F7', 'F3', 'FC1', 'FC5', 'T7', 'C3', 'CP1', 'CP5', 'P7', 'P3', 'Pz', 'PO3', 'O1', 'Oz', 'O2', 'PO4', 'P4', 'P8', 'CP6', 'CP2', 'C4', 'T8', 'FC6', 'FC2', 'F4', 'F8', 'AF4', 'Fp2', 'Fz', 'Cz']
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/openneuro-ds002778-jackson-2019/waveshape.py",
 "content": "\"\"\"Loading and waveform measures for OpenNeuro ds002778 (UC San Diego resting EEG in Parkinson's disease).\n\nJackson, Cole, Voytek & Swann (2019), eNeuro 6(3) ENEURO.0151-19.2019, doi:10.1523/ENEURO.0151-19.2019.\n\nThe dataset is BIDS: 15 patients recorded off (`ses-off`) and on (`ses-on`) medication and 16\ncontrols (`ses-hc`), one BioSemi BDF file per session (32 scalp electrodes, 8 external EXG\nchannels, a Status channel, 512 Hz). Files are read from the pinned snapshot 1.0.5: the file list\ncomes from OpenNeuro's GraphQL API, each file is opened at its `urls[0]`, which is pinned to that\nsnapshot, and read into memory. Nothing is written to disk.\n\nWhere the parameters come from. \"Claims\" is the claims file `claims/openneuro-ds002778/`, whose\nopening comment cites the paper's Methods and its code (SwannLab/Jackson_2019 at commit a7c89f5);\n\"Methods\" is the paper's Materials and Methods.\n\n- Preprocessing (`preprocess`): each electrode's mean removed, common average over the 32 scalp\n  electrodes, high-pass at 0.5 Hz with a two-way FIR filter (Methods, Data preprocessing: \"each\n  electrode's mean was removed and then a common average reference was applied ... high pass\n  filtered at 0.5 Hz ... using a two-way FIR filter, eegfilt\"). The filter is eegfilt's: firls\n  of order 3 * fix(512 / 0.5) = 3072 with a 15% transition band (claims, opening comment, a\n  standard choice). It is applied forwards and backwards with FFT convolution, with the odd\n  extension and steady-state start of MATLAB's and scipy's filtfilt (a standard choice that\n  only changes rounding). No electrode is excluded and no sample rejected: the dataset holds no\n  bad-channel marks (every channels.tsv says \"good\") and no artifact marks (claims, readings (b)\n  for noisy electrodes and for artifact rejection).\n- Peaks and troughs (`find_extrema`): band-pass with scipy firwin applied with filtfilt; the\n  extremum of the raw signal between consecutive zero crossings of the filtered one; extrema\n  within 100 samples of either end dropped (claims; code shape.findpt and utils.measure_shape,\n  boundaryS=100). Filter length for 13 to 30 Hz: floor(3 * 512 / 13) = 118 taps (code; the\n  Methods' 231 ms is the same 118 samples). For 8 to 12 Hz: 192 taps (3 cycles of 8 Hz, the\n  code's rule) and 118 (the Methods' 231 ms), the two readings of the claims file.\n- Sharpness (`shape_measures`): |mean(x[e] - x[e-3], x[e] - x[e+3])| (claims; code\n  shape.ex_sharp, widthS=3). Steepness: largest first difference from a trough to the next peak\n  (rise) and largest negative first difference from a peak to the next trough (decay), taking\n  len(troughs) - 1 rises and len(peaks) - 1 decays as the code's rd_steep does. Sharpness ratio\n  and steepness ratio are |log10| of the ratio of means; peak-to-trough ratio and rise-to-fall\n  ratio are the signed log10 (claims; code utils.measure_shape and Figure_4).\n- PAC (`pac_ozkurt`): firwin band-pass with filtfilt, Hilbert phase of the low band and\n  amplitude of 50 to 150 Hz, |sum(a exp(i phi))| / (sqrt(N) sqrt(sum a^2)) (claims; code\n  pac.ozkurt). Filter lengths: 118 and 123 samples (Methods, 231 ms and 240 ms at 512 Hz) and\n  231 and 240 taps (code utils.measure_pac), the two readings of the claims file. For 8 to 12 Hz\n  phase: 192, 231 and 118 taps (claims, readings a to c).\n- Bipolar signals C3 - CP1 and C4 - CP2 (claims, bipolar-off-on).\n- Current source density (`csd`): spherical spline surface Laplacian with m = 3 (Methods: \"CSDtoolbox\n  in MATLAB, spline flexibility = 3\"), lambda 1e-5 and 50 Legendre terms (the CSD toolbox's\n  defaults, a standard choice per the claims file), computed with MNE on the BioSemi 32\n  template positions (a standard choice: the dataset holds no digitized positions).\n- Welch spectra (`welch_psd`): Hamming window of 256 samples, overlap 128, nFFT 450 (Methods,\n  Data analysis, pwelch), no detrending, as pwelch.\n- Statistics: Wilcoxon signed rank with the normal approximation and no continuity correction\n  (claims: the code's printed p-values match it), the exact test as a variant; rank sum z\n  (scipy ranksums); Cohen's d with the code's effectsize formula; Benjamini-Hochberg FDR.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport json\nfrom functools import lru_cache\n\nimport mne\nimport numpy as np\nimport pandas as pd\nimport requests\nfrom scipy import signal, stats\n\nDATASET_ID = \"ds002778\"\nSNAPSHOT = \"1.0.5\"\nSNAPSHOT_DOI = \"10.18112/openneuro.ds002778.v1.0.5\"\nGRAPHQL = \"https://openneuro.org/crn/graphql\"\nFS = 512.0\n\nSCALP = ['Fp1', 'AF3', 'F7', 'F3', 'FC1', 'FC5', 'T7', 'C3', 'CP1', 'CP5', 'P7', 'P3', 'Pz', 'PO3',\n         'O1', 'Oz', 'O2', 'PO4', 'P4', 'P8', 'CP6', 'CP2', 'C4', 'T8', 'FC6', 'FC2', 'F4', 'F8',\n         'AF4', 'Fp2', 'Fz', 'Cz']\nBETA = (13.0, 30.0)\nALPHA = (8.0, 12.0)\nGAMMA = (50.0, 150.0)\nBOUNDARY = 100        # code utils.measure_shape, boundaryS\nWIDTH = 3             # code, widthS: samples either side of an extremum\nSHAPE_TAPS = {\"beta\": {\"118\": 118}, \"alpha\": {\"192\": 192, \"118\": 118}}\n# PAC filter readings: name -> (phase taps, amplitude taps)\nPAC_BETA = {\"methods\": (118, 123), \"code\": (231, 240)}\nPAC_ALPHA = {\"a192\": (192, 123), \"b231\": (231, 240), \"c118\": (118, 123)}\nPAC_ALPHA_GAMMA = {\"a192\": \"methods\", \"b231\": \"code\", \"c118\": \"methods\"}\nSIX = ['C3', 'C4', 'F7', 'F8', 'T7', 'T8']\n\n\n# ----------------------------------------------------------------------------- archive\n\n@lru_cache(maxsize=1)\ndef listing() -> pd.DataFrame:\n    \"\"\"Every file of the pinned snapshot, with its size, checksum id and pinned URL.\"\"\"\n    query = ('{ snapshot(datasetId: \"%s\", tag: \"%s\") { files(recursive: true) '\n             '{ filename size annexed id urls } } }' % (DATASET_ID, SNAPSHOT))\n    r = requests.post(GRAPHQL, json={\"query\": query}, timeout=120)\n    r.raise_for_status()\n    body = r.json()\n    if \"errors\" in body:\n        raise RuntimeError(body[\"errors\"])\n    files = body[\"data\"][\"snapshot\"][\"files\"]\n    df = pd.DataFrame([{\"filename\": f[\"filename\"], \"size\": f[\"size\"], \"annexed\": f[\"annexed\"],\n                        \"id\": f[\"id\"], \"url\": f[\"urls\"][0]} for f in files])\n    return df.set_index(\"filename\")\n\n\ndef url(name: str) -> str:\n    return listing().loc[name, \"url\"]\n\n\ndef fetch(name: str) -> bytes:\n    r = requests.get(url(name), timeout=300)\n    r.raise_for_status()\n    return r.content\n\n\ndef read_tsv(name: str) -> pd.DataFrame:\n    return pd.read_csv(io.BytesIO(fetch(name)), sep=\"\\t\")\n\n\ndef read_json(name: str):\n    return json.loads(fetch(name).decode())\n\n\ndef bdf_name(sub: str, ses: str) -> str:\n    return f\"sub-{sub}/ses-{ses}/eeg/sub-{sub}_ses-{ses}_task-rest_eeg.bdf\"\n\n\ndef read_bdf(sub: str, ses: str) -> mne.io.BaseRaw:\n    \"\"\"The session's BDF, read whole into memory from the pinned URL.\"\"\"\n    return mne.io.read_raw_bdf(io.BytesIO(fetch(bdf_name(sub, ses))), preload=True,\n                               verbose=\"error\")\n\n\ndef sessions() -> pd.DataFrame:\n    \"\"\"One row per recording: subject, session, group.\"\"\"\n    names = [n for n in listing().index if n.endswith(\"_eeg.bdf\")]\n    rows = []\n    for n in names:\n        sub, ses = n.split(\"/\")[0][4:], n.split(\"/\")[1][4:]\n        rows.append({\"sub\": sub, \"ses\": ses, \"group\": {\"hc\": \"control\", \"off\": \"off\", \"on\": \"on\"}[ses]})\n    return pd.DataFrame(rows).sort_values([\"group\", \"sub\"]).reset_index(drop=True)\n\n\n# ----------------------------------------------------------------------------- filters\n\ndef _filtfilt_fft(x: np.ndarray, b: np.ndarray) -> np.ndarray:\n    \"\"\"filtfilt(b, 1, x) along the last axis, by FFT convolution.\n\n    Same padding as scipy.signal.filtfilt (odd extension of 3 * len(b) samples) and the same\n    steady-state start (the input held at its first value before the start), so the result\n    equals scipy's to rounding error.\n    \"\"\"\n    n = len(b)\n    pad = 3 * n\n    ext = signal.signaltools.odd_ext(x, pad, axis=-1) if hasattr(signal, \"signaltools\") else None\n    if ext is None:\n        from scipy.signal._arraytools import odd_ext\n        ext = odd_ext(x, pad, axis=-1)\n\n    def causal(y):\n        head = np.repeat(y[..., :1], n, axis=-1)\n        z = signal.fftconvolve(np.concatenate([head, y], axis=-1), b[None, :] if y.ndim == 2 else b,\n                               mode=\"full\", axes=-1)\n        return z[..., n:n + y.shape[-1]]\n\n    y = causal(ext)\n    y = causal(y[..., ::-1])[..., ::-1]\n    return y[..., pad:-pad]\n\n\n@lru_cache(maxsize=None)\ndef eegfilt_highpass_taps(locutoff: float = 0.5, fs: float = FS) -> np.ndarray:\n    \"\"\"eegfilt's high-pass: firls of order 3 * fix(fs / locutoff), transition 15% below locutoff.\"\"\"\n    order = 3 * int(fs / locutoff)\n    nyq = fs / 2\n    return signal.firls(order + 1, [0, locutoff * 0.85 / nyq, locutoff / nyq, 1], [0, 0, 1, 1])\n\n\n@lru_cache(maxsize=None)\ndef bandpass_taps(f_range: tuple, ntaps: int, fs: float = FS) -> np.ndarray:\n    \"\"\"scipy firwin band-pass, as the paper's code (pacpy firf).\"\"\"\n    return signal.firwin(int(ntaps), np.array(f_range) / (fs / 2), pass_zero=False)\n\n\ndef bandpass(x: np.ndarray, f_range: tuple, ntaps: int) -> np.ndarray:\n    return signal.filtfilt(bandpass_taps(tuple(f_range), int(ntaps)), [1.0], x, axis=-1)\n\n\n# ----------------------------------------------------------------------------- preprocessing\n\ndef preprocess(data_uv: np.ndarray) -> np.ndarray:\n    \"\"\"Mean removal, common average over the rows, 0.5 Hz two-way FIR high-pass.\"\"\"\n    x = data_uv - data_uv.mean(axis=1, keepdims=True)\n    x = x - x.mean(axis=0, keepdims=True)\n    return _filtfilt_fft(x, eegfilt_highpass_taps())\n\n\ndef csd(x: np.ndarray) -> np.ndarray:\n    \"\"\"Spherical spline CSD (m = 3, lambda 1e-5, 50 Legendre terms) on the 32 scalp rows.\"\"\"\n    info = mne.create_info(SCALP, FS, \"eeg\")\n    raw = mne.io.RawArray(x * 1e-6, info, verbose=\"error\")\n    raw.set_montage(mne.channels.make_standard_montage(\"biosemi32\"), verbose=\"error\")\n    out = mne.preprocessing.compute_current_source_density(\n        raw, stiffness=3, lambda2=1e-5, n_legendre_terms=50, verbose=\"error\")\n    return out.get_data()\n\n\n# ----------------------------------------------------------------------------- measures\n\ndef find_extrema(x: np.ndarray, f_range: tuple, ntaps: int, boundary: int = BOUNDARY):\n    \"\"\"Peaks and troughs of x between zero crossings of its band-passed copy (code findpt).\"\"\"\n    xn = bandpass(x, f_range, ntaps)\n    pos = xn > 0\n    falls = (pos[:-1] & ~pos[1:]).nonzero()[0]\n    neg = xn < 0\n    rises = (neg[:-1] & ~neg[1:]).nonzero()[0]\n    cross = np.concatenate([rises, falls])\n    kind = np.concatenate([np.ones(len(rises), bool), np.zeros(len(falls), bool)])\n    order = np.argsort(cross, kind=\"stable\")\n    cross, kind = cross[order], kind[order]\n    # a segment from a crossing to the next one: from a rise it holds a peak, from a fall a trough\n    starts, ends = cross[:-1], cross[1:]\n    is_peak = kind[:-1] & ~kind[1:]\n    is_trough = ~kind[:-1] & kind[1:]\n    keep = is_peak | is_trough\n    starts, ends, is_peak = starts[keep], ends[keep], is_peak[keep]\n    seg = x[starts[0]:ends[-1]]\n    offs = starts - starts[0]\n    # extremum per segment: the first argmax (peaks) or argmin (troughs), as np.argmax/argmin\n    lens = ends - starts\n    seg_id = np.repeat(np.arange(len(starts)), lens)\n    idx = np.concatenate([np.arange(s, e) for s, e in zip(starts, ends)]) if False else \\\n        (np.arange(len(seg_id)) - np.repeat(np.cumsum(lens) - lens, lens) + np.repeat(starts, lens))\n    vals = x[idx]\n    signed = np.where(is_peak[seg_id], vals, -vals)\n    best = np.full(len(starts), -np.inf)\n    np.maximum.at(best, seg_id, signed)\n    hit = signed == best[seg_id]\n    first = np.full(len(starts), -1)\n    hit_pos = np.nonzero(hit)[0]\n    _, first_in = np.unique(seg_id[hit_pos], return_index=True)\n    first[np.unique(seg_id[hit_pos])] = idx[hit_pos[first_in]]\n    peaks = first[is_peak]\n    troughs = first[~is_peak]\n    n = len(x)\n    ok = lambda e: e[(e >= boundary) & (e <= n - boundary)]\n    return ok(peaks), ok(troughs)\n\n\ndef shape_measures(x: np.ndarray, f_range: tuple, ntaps: int) -> dict:\n    \"\"\"Sharpness ratio, steepness ratio, peak-to-trough and rise-to-fall ratios of one trace.\"\"\"\n    P, T = find_extrema(x, f_range, ntaps)\n    w = WIDTH\n    psharp = np.abs(((x[P] - x[P - w]) + (x[P] - x[P + w])) / 2)\n    tsharp = np.abs(((x[T] - x[T - w]) + (x[T] - x[T + w])) / 2)\n    # rises (trough to next peak) and decays (peak to next trough), as code rd_steep\n    E = np.sort(np.concatenate([P, T]))\n    is_p = np.isin(E, P)\n    d = np.diff(x)\n    seg_max = np.maximum.reduceat(d, E[:-1])\n    seg_min = np.minimum.reduceat(d, E[:-1])\n    rise = seg_max[~is_p[:-1] & is_p[1:]][:len(T) - 1]\n    decay = -seg_min[is_p[:-1] & ~is_p[1:]][:len(P) - 1]\n    mp, mt, mr, md = psharp.mean(), tsharp.mean(), rise.mean(), decay.mean()\n    return {\"ShR\": abs(np.log10(mp / mt)), \"StR\": abs(np.log10(mr / md)),\n            \"PTR\": np.log10(mp / mt), \"RDR\": np.log10(mr / md),\n            \"n_peaks\": len(P), \"n_troughs\": len(T)}\n\n\ndef pac_ozkurt(x: np.ndarray, f_lo: tuple, n_lo: int, f_hi: tuple = GAMMA, n_hi: int = 123) -> float:\n    \"\"\"Normalized modulation index (Ozkurt and Schnitzler 2011), as code pac.ozkurt.\"\"\"\n    pha = np.angle(signal.hilbert(bandpass(x, f_lo, n_lo)))\n    amp = np.abs(signal.hilbert(bandpass(x, f_hi, n_hi)))\n    return float(np.abs(np.sum(amp * np.exp(1j * pha))) / (np.sqrt(len(pha)) * np.sqrt(np.sum(amp ** 2))))\n\n\ndef welch_psd(x: np.ndarray):\n    \"\"\"pwelch(x, 256, 128, 450, 512): Hamming window, no detrending.\"\"\"\n    return signal.welch(x, fs=FS, window=\"hamming\", nperseg=256, noverlap=128, nfft=450,\n                        detrend=False, axis=-1)\n\n\n# ----------------------------------------------------------------------------- one recording\n\ndef analyse(sub: str, ses: str) -> dict:\n    \"\"\"All measures of one recording: per electrode, bipolar pairs and CSD at C3 and C4.\"\"\"\n    raw = read_bdf(sub, ses)\n    names = raw.ch_names\n    data = raw.get_data(picks=SCALP) * 1e6          # volts to microvolts\n    exg = raw.get_data(picks=[c for c in names if c.startswith(\"EXG\")]) * 1e6\n    status = raw.get_data(picks=[\"Status\"])[0] if \"Status\" in names else None\n    info = {\"sub\": sub, \"ses\": ses, \"n_times\": raw.n_times, \"sfreq\": raw.info[\"sfreq\"],\n            \"channels\": names,\n            \"raw_mean_abs_uv\": float(np.abs(data.mean(axis=1)).mean()),\n            \"raw_sum_over_channels_uv\": float(np.abs(data.sum(axis=0)).max()),\n            \"raw_sd_uv\": dict(zip(SCALP, data.std(axis=1))),\n            \"exg_sd_uv\": exg.std(axis=1).tolist(),\n            \"raw_c3_head\": data[SCALP.index(\"C3\"), :2048].copy()}\n    if status is not None:\n        st = status.astype(np.int64)\n        change = np.nonzero(np.diff(st))[0] + 1\n        info[\"status_changes\"] = [(int(i), int(st[i])) for i in change[:10]]\n        info[\"status_first\"] = int(st[0])\n    x = preprocess(data)\n    info[\"pre_sd_uv\"] = dict(zip(SCALP, x.std(axis=1)))\n\n    rows = []\n    for i, ch in enumerate(SCALP):\n        for band, taps in SHAPE_TAPS.items():\n            f = BETA if band == \"beta\" else ALPHA\n            for tname, nt in taps.items():\n                m = shape_measures(x[i], f, nt)\n                rows.append({\"sub\": sub, \"ses\": ses, \"signal\": ch, \"band\": band, \"taps\": tname, **m})\n    shape = pd.DataFrame(rows)\n\n    prow = []\n    for i, ch in enumerate(SCALP):\n        for rname, (nlo, nhi) in PAC_BETA.items():\n            prow.append({\"sub\": sub, \"ses\": ses, \"signal\": ch, \"band\": \"beta\", \"reading\": rname,\n                         \"PAC\": pac_ozkurt(x[i], BETA, nlo, GAMMA, nhi)})\n        if ch in SIX:\n            for rname, (nlo, nhi) in PAC_ALPHA.items():\n                prow.append({\"sub\": sub, \"ses\": ses, \"signal\": ch, \"band\": \"alpha\", \"reading\": rname,\n                             \"PAC\": pac_ozkurt(x[i], ALPHA, nlo, GAMMA, nhi)})\n\n    # bipolar montage\n    bip = {\"C3-CP1\": x[SCALP.index(\"C3\")] - x[SCALP.index(\"CP1\")],\n           \"C4-CP2\": x[SCALP.index(\"C4\")] - x[SCALP.index(\"CP2\")]}\n    brow = []\n    for name, y in bip.items():\n        m = shape_measures(y, BETA, 118)\n        brow.append({\"sub\": sub, \"ses\": ses, \"signal\": name, \"band\": \"beta\", \"taps\": \"118\", **m})\n        for rname, (nlo, nhi) in PAC_BETA.items():\n            prow.append({\"sub\": sub, \"ses\": ses, \"signal\": name, \"band\": \"beta\", \"reading\": rname,\n                         \"PAC\": pac_ozkurt(y, BETA, nlo, GAMMA, nhi)})\n    shape = pd.concat([shape, pd.DataFrame(brow)], ignore_index=True)\n\n    # current source density\n    xc = csd(x)\n    for ch in (\"C3\", \"C4\"):\n        for rname, (nlo, nhi) in PAC_BETA.items():\n            prow.append({\"sub\": sub, \"ses\": ses, \"signal\": \"CSD \" + ch, \"band\": \"beta\", \"reading\": rname,\n                         \"PAC\": pac_ozkurt(xc[SCALP.index(ch)], BETA, nlo, GAMMA, nhi)})\n    pac = pd.DataFrame(prow)\n\n    freqs, psd = welch_psd(x)\n    return {\"info\": info, \"shape\": shape, \"pac\": pac, \"freqs\": freqs,\n            \"psd\": pd.DataFrame(psd, index=SCALP, columns=np.round(freqs, 4))}\n\n\n# ----------------------------------------------------------------------------- statistics\n\ndef signed_rank(a, b, method: str = \"approx\"):\n    \"\"\"Wilcoxon signed rank of paired a and b: statistic min(W+, W-) and two-sided p.\n\n    method \"approx\" is the normal approximation without continuity correction (old scipy\n    default, which the paper's printed p-values match); \"exact\" is a variant.\n    \"\"\"\n    a, b = np.asarray(a, float), np.asarray(b, float)\n    if method == \"approx\":\n        r = stats.wilcoxon(a, b, method=\"approx\", correction=False, zero_method=\"wilcox\")\n    else:\n        r = stats.wilcoxon(a, b, method=\"exact\", zero_method=\"wilcox\")\n    return float(r.statistic), float(r.pvalue)\n\n\ndef rank_sum(a, b):\n    r = stats.ranksums(np.asarray(a, float), np.asarray(b, float))\n    return float(r.statistic), float(r.pvalue)\n\n\ndef cohen_d(m1, m2) -> float:\n    \"\"\"(mean1 - mean2) / sqrt((sd1^2 + sd2^2) / 2), sample SDs (code effectsize).\"\"\"\n    m1, m2 = np.asarray(m1, float), np.asarray(m2, float)\n    return float((m1.mean() - m2.mean()) / np.sqrt((m1.std(ddof=1) ** 2 + m2.std(ddof=1) ** 2) / 2))\n\n\ndef fdr_bh(p) -> np.ndarray:\n    \"\"\"Benjamini-Hochberg adjusted p-values.\"\"\"\n    p = np.asarray(p, float)\n    n = len(p)\n    order = np.argsort(p)\n    adj = p[order] * n / np.arange(1, n + 1)\n    adj = np.minimum.accumulate(adj[::-1])[::-1]\n    out = np.empty(n)\n    out[order] = np.minimum(adj, 1)\n    return out\n"
}
```

```
File created successfully at: entries/openneuro-ds002778-jackson-2019/waveshape.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds002778-jackson-2019 && python - <<'EOF'
s=open('waveshape.py').read()
a=s.index('def find_extrema'); b=s.index('def shape_measures')
new='''def find_extrema(x: np.ndarray, f_range: tuple, ntaps: int, boundary: int = BOUNDARY):
    """Peaks and troughs of x between zero crossings of its band-passed copy (code findpt).

    A peak is the first maximum of x from a rising zero crossing to the next falling one, a
    trough the first minimum from a falling crossing to the next rising one.
    """
    xn = bandpass(x, f_range, ntaps)
    pos, neg = xn > 0, xn < 0
    falls = (pos[:-1] & ~pos[1:]).nonzero()[0]
    rises = (neg[:-1] & ~neg[1:]).nonzero()[0]
    cross = np.concatenate([rises, falls])
    is_rise = np.concatenate([np.ones(len(rises), bool), np.zeros(len(falls), bool)])
    order = np.argsort(cross, kind="stable")
    cross, is_rise = cross[order], is_rise[order]
    lens = np.diff(cross)
    sign = np.where(is_rise[:-1], 1.0, -1.0)
    seg = x[cross[0]:cross[-1]] * np.repeat(sign, lens)
    best = np.maximum.reduceat(seg, cross[:-1] - cross[0])
    seg_id = np.repeat(np.arange(len(lens)), lens)
    hit = np.nonzero(seg == best[seg_id])[0]
    ids, first = np.unique(seg_id[hit], return_index=True)
    ext = np.full(len(lens), -1)
    ext[ids] = hit[first] + cross[0]
    peak_seg = is_rise[:-1] & ~is_rise[1:]
    trough_seg = ~is_rise[:-1] & is_rise[1:]
    peaks, troughs = ext[peak_seg], ext[trough_seg]
    n = len(x)
    inside = lambda e: e[(e >= boundary) & (e <= n - boundary)]
    return inside(peaks), inside(troughs)


'''
s=s[:a]+new+s[b:]
a=s.index('    n = len(b)\n    pad = 3 * n'); b=s.index('    def causal(y):')
s=s[:a]+'    n = len(b)\n    pad = 3 * n\n    ext = odd_ext(x, pad, axis=-1)\n\n'+s[b:]
s=s.replace("z = signal.fftconvolve(np.concatenate([head, y], axis=-1), b[None, :] if y.ndim == 2 else b,\n                               mode=\"full\", axes=-1)",
 "z = signal.fftconvolve(np.concatenate([head, y], axis=-1), b.reshape((1,) * (y.ndim - 1) + (-1,)),\n                               mode=\"full\", axes=-1)")
s=s.replace("from scipy import signal, stats\n","from scipy import signal, stats\nfrom scipy.signal._arraytools import odd_ext\n")
open('waveshape.py','w').write(s)
EOF
grep -n "odd_ext\|fftconvolve" waveshape.py
```

```
65:from scipy.signal._arraytools import odd_ext
156:    ext = odd_ext(x, pad, axis=-1)
160:        z = signal.fftconvolve(np.concatenate([head, y], axis=-1), b.reshape((1,) * (y.ndim - 1) + (-1,)),
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds002778-jackson-2019; . $TMPDIR/dev/bin/activate; python - <<'EOF'
import numpy as np, time
from scipy import signal
import waveshape as w
rng=np.random.default_rng(0)
x=np.cumsum(rng.normal(size=(2,30000)),axis=1)+rng.normal(size=(2,30000))*5
b=w.eegfilt_highpass_taps()
t=time.time(); y1=w._filtfilt_fft(x,b); print('fft',time.time()-t)
t=time.time(); y2=signal.filtfilt(b,[1],x,axis=-1); print('scipy',time.time()-t)
print('max diff',np.abs(y1-y2).max(), np.abs(y2).max())
# code findpt
def code_findpt(x, f_osc, Fs=512., w_=3, boundary=100):
    Ntaps=int(np.floor(w_*Fs/f_osc[0])); taps=signal.firwin(Ntaps,np.array(f_osc)/(Fs/2),pass_zero=False)
    xn=signal.filtfilt(taps,[1],x)
    pos=xn>0; zerofallN=(pos[:-1]&~pos[1:]).nonzero()[0]
    pos=xn<0; zeroriseN=(pos[:-1]&~pos[1:]).nonzero()[0]
    if zeroriseN[-1]>zerofallN[-1]: P=len(zeroriseN)-1; T=len(zerofallN)
    else: P=len(zeroriseN); T=len(zerofallN)-1
    if T-P==2: T=T-2
    Ps=np.array([np.argmax(x[r:zerofallN[zerofallN>r][0]])+r for r in zeroriseN[:P]])
    Ts=np.array([np.argmin(x[f:zeroriseN[zeroriseN>f][0]])+f for f in zerofallN[:T]])
    n=len(x); keep=lambda E: E[~((E<boundary)|(E>n-boundary))]
    return keep(Ps),keep(Ts)
def code_rd(x,Ps,Ts):
    riseadj=1 if Ps[0]<Ts[0] else 0
    rs=np.array([np.max(np.diff(x[Ts[t]:Ps[t+riseadj]+1])) for t in range(len(Ts)-1)])
    ds=np.array([-np.min(np.diff(x[Ps[p]:Ts[p-riseadj+1]+1])) for p in range(len(Ps)-1)])
    return rs,ds
xx=y2[0]
P,T=w.find_extrema(xx,(13,30),118); P2,T2=code_findpt(xx,(13,30))
print(len(P),len(P2),np.array_equal(P,P2),len(T),len(T2),np.array_equal(T,T2))
rs,ds=code_rd(xx,P2,T2)
m=w.shape_measures(xx,(13,30),118)
print(m, np.log10(rs.mean()/ds.mean()))
EOF
```

```
fft 0.007209300994873047
scipy 0.08757567405700684
max diff 2.7000623958883807e-13 37.41400921719549
1238 1238 True 1239 1239 True
{'ShR': np.float64(0.012813651747244074), 'StR': np.float64(0.005315804779822401), 'PTR': np.float64(-0.012813651747244074), 'RDR': np.float64(0.005315804779822401), 'n_peaks': 1238, 'n_troughs': 1239} 0.005315804779822401
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds002778-jackson-2019; . $TMPDIR/dev/bin/activate; python - <<'EOF'
import time, waveshape as w
t=time.time(); w.listing(); print('list',time.time()-t)
t=time.time(); r=w.analyse('pd3','off'); print('analyse',time.time()-t)
print(r['shape'].query("signal in ['C3','C4','C3-CP1']"))
print(r['pac'].query("signal in ['C3','C4','CSD C3','C3-CP1']"))
print(r['info']['status_changes'], r['info']['status_first'], r['info']['n_times'])
EOF
```

```
list 0.4432229995727539
analyse 3.0722525119781494
    sub  ses  signal   band  ...       PTR       RDR  n_peaks  n_troughs
21  pd3  off      C3   beta  ...  0.068327 -0.063381     4509       4509
22  pd3  off      C3  alpha  ...  0.083555 -0.083681     1980       1979
23  pd3  off      C3  alpha  ...  0.085541 -0.087939     1948       1947
66  pd3  off      C4   beta  ...  0.040681 -0.098663     4397       4397
67  pd3  off      C4  alpha  ...  0.041588 -0.118989     1993       1993
68  pd3  off      C4  alpha  ...  0.039736 -0.117434     2006       2006
96  pd3  off  C3-CP1   beta  ...  0.047949 -0.063332     4365       4364

[7 rows x 11 columns]
    sub  ses  signal   band  reading       PAC
20  pd3  off      C3   beta  methods  0.030079
21  pd3  off      C3   beta     code  0.029652
22  pd3  off      C3  alpha     a192  0.017029
23  pd3  off      C3  alpha     b231  0.015570
24  pd3  off      C3  alpha     c118  0.022316
53  pd3  off      C4   beta  methods  0.029394
54  pd3  off      C4   beta     code  0.029191
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds002778-jackson-2019; . $TMPDIR/dev/bin/activate; time python - <<'EOF'
import time, pickle, waveshape as w
from concurrent.futures import ThreadPoolExecutor
s=w.sessions()
with ThreadPoolExecutor(4) as ex: res=list(ex.map(lambda r: w.analyse(r.sub,r.ses), s.itertuples()))
pickle.dump(res,open(__import__('os').environ['TMPDIR']+'/all.pkl','wb'))
EOF
```

```
real	0m56.153s
user	3m4.434s
sys	0m3.825s
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds002778-jackson-2019; . $TMPDIR/dev/bin/activate; python - <<'EOF'
import pickle, os, pandas as pd, numpy as np, waveshape as w
res=pickle.load(open(os.environ['TMPDIR']+'/all.pkl','rb'))
sh=pd.concat([r['shape'] for r in res]); pc=pd.concat([r['pac'] for r in res])
def comp(df, val, sigs):
    d=df[df.signal.isin(sigs)].groupby(['sub','ses'])[val].mean().unstack()
    return d
for band,taps in [('beta','118'),('alpha','192'),('alpha','118')]:
    for sigs in [['C3','C4'],['F7','F8'],['T7','T8'],['C3-CP1','C4-CP2']]:
        d=sh[(sh.band==band)&(sh.taps==taps)]
        if d[d.signal.isin(sigs)].empty: continue
        for m in ['ShR','StR']:
            c=comp(d,m,sigs); pd_=c.dropna(subset=['off','on'])
            W,p=w.signed_rank(pd_.off,pd_.on); z,p2=w.rank_sum(pd_.off,c.hc.dropna())
            print(band,taps,sigs,m,'W=%.1f p=%.4f d=%.2f | z=%.2f p=%.4f d=%.2f'%(W,p,w.cohen_d(pd_.off,pd_.on),z,p2,w.cohen_d(pd_.off,c.hc.dropna())), 'off>on', (pd_.off>pd_.on).sum())
for band,rd in [('beta','methods'),('beta','code'),('alpha','a192'),('alpha','b231'),('alpha','c118')]:
    for sigs in [['C3','C4'],['F7','F8'],['T7','T8'],['C3-CP1','C4-CP2'],['CSD C3','CSD C4']]:
        d=pc[(pc.band==band)&(pc.reading==rd)]
        if d[d.signal.isin(sigs)].empty: continue
        c=comp(d,'PAC',sigs); pd_=c.dropna(subset=['off','on'])
        W,p=w.signed_rank(pd_.off,pd_.on); z,p2=w.rank_sum(pd_.off,c.hc.dropna())
        print(band,rd,sigs,'PAC W=%.1f p=%.4f d=%.2f dlog=%.2f | z=%.2f p=%.4f'%(W,p,w.cohen_d(pd_.off,pd_.on),w.cohen_d(np.log10(pd_.off),np.log10(pd_.on)),z,p2))
EOF
```

```
beta 118 ['C3', 'C4'] ShR W=13.0 p=0.0076 d=0.73 | z=0.47 p=0.6353 d=0.09 off>on 13
beta 118 ['C3', 'C4'] StR W=16.0 p=0.0125 d=0.70 | z=2.37 p=0.0177 d=0.85 off>on 12
beta 118 ['F7', 'F8'] ShR W=53.0 p=0.6909 d=0.31 | z=-1.26 p=0.2059 d=-0.25 off>on 8
beta 118 ['F7', 'F8'] StR W=36.0 p=0.1728 d=0.57 | z=1.19 p=0.2357 d=0.41 off>on 8
beta 118 ['T7', 'T8'] ShR W=44.0 p=0.3635 d=0.42 | z=-0.24 p=0.8125 d=-0.14 off>on 8
beta 118 ['T7', 'T8'] StR W=59.0 p=0.9547 d=-0.04 | z=-0.99 p=0.3230 d=-0.37 off>on 9
beta 118 ['C3-CP1', 'C4-CP2'] ShR W=15.0 p=0.0106 d=0.55 | z=0.99 p=0.3230 d=0.21 off>on 13
beta 118 ['C3-CP1', 'C4-CP2'] StR W=4.0 p=0.0015 d=0.89 | z=2.37 p=0.0177 d=0.94 off>on 13
alpha 192 ['C3', 'C4'] ShR W=18.0 p=0.0171 d=0.71 | z=0.71 p=0.4768 d=0.19 off>on 11
alpha 192 ['C3', 'C4'] StR W=21.0 p=0.0268 d=0.58 | z=2.45 p=0.0143 d=0.89 off>on 12
alpha 192 ['F7', 'F8'] ShR W=49.0 p=0.5321 d=0.37 | z=-0.47 p=0.6353 d=-0.06 off>on 8
alpha 192 ['F7', 'F8'] StR W=39.0 p=0.2330 d=0.57 | z=1.58 p=0.1138 d=0.56 off>on 8
alpha 192 ['T7', 'T8'] ShR W=50.0 p=0.5701 d=0.28 | z=-0.12 p=0.9056 d=-0.12 off>on 8
alpha 192 ['T7', 'T8'] StR W=56.0 p=0.8203 d=-0.15 | z=-1.15 p=0.2517 d=-0.42 off>on 8
alpha 118 ['C3', 'C4'] ShR W=19.0 p=0.0199 d=0.66 | z=0.36 p=0.7220 d=0.14 off>on 10
alpha 118 ['C3', 'C4'] StR W=21.0 p=0.0268 d=0.59 | z=2.53 p=0.0114 d=0.89 off>on 12
alpha 118 ['F7', 'F8'] ShR W=47.0 p=0.4603 d=0.41 | z=-0.59 p=0.5532 d=-0.04 off>on 7
alpha 118 ['F7', 'F8'] StR W=38.0 p=0.2115 d=0.58 | z=1.58 p=0.1138 d=0.58 off>on 8
alpha 118 ['T7', 'T8'] ShR W=47.0 p=0.4603 d=0.36 | z=-0.12 p=0.9056 d=-0.09 off>on 8
alpha 118 ['T7', 'T8'] StR W=55.0 p=0.7764 d=-0.13 | z=-1.23 p=0.2204 d=-0.45 off>on 8
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  sed -n 1,80p tools/entry.py | head -80; grep -n "def check\|tag\|sanity\|claim:" tools/entry.py | head -40
```

```
Tue Oct 27 22:33:02 UTC 2026
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
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/entry.schema.json'));print(json.dumps(s,indent=1)[:3500])"; grep -n "openneuro\|relation\|uses_data" tools/entry.py | head -20
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "An entry: a directory of notebooks with its metadata (entry.yaml)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "name",
  "type",
  "title",
  "description",
  "license",
  "notebooks",
  "related"
 ],
 "properties": {
  "schema_version": {
   "const": 1
  },
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/nb; cat > $TMPDIR/nb/cells.py <<'EOF'
# cell definitions: list of (type, source, tags)
CELLS = []
def md(s, tags=()): CELLS.append(("markdown", s.strip("\n"), list(tags)))
def code(s, tags=()): CELLS.append(("code", s.strip("\n"), list(tags)))
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/placeholder.txt",
 "content": "x\n"
}
```

```
File created successfully at: /tmp/claude/placeholder.txt (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
echo $TMPDIR; rm -f /tmp/claude/placeholder.txt
```

```
/tmp/claude-1001
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/src.py",
 "content": "# %% [markdown]\n# # Reproducing Jackson, Cole, Voytek & Swann (2019) from OpenNeuro ds002778\n#\n# **Paper.** Jackson N, Cole SR, Voytek B, Swann NC (2019). Characteristics of waveform shape in\n# Parkinson's disease detected with scalp electroencephalography. *eNeuro* 6(3)\n# ENEURO.0151-19.2019. [doi:10.1523/ENEURO.0151-19.2019](https://doi.org/10.1523/ENEURO.0151-19.2019).\n# The claims file was written from the version of record (Europe PMC PMC6553574: main text,\n# Methods, legends, Tables 1 to 3) and the paper's code, SwannLab/Jackson_2019 at commit a7c89f5.\n#\n# **Dataset.** [OpenNeuro ds002778](https://openneuro.org/datasets/ds002778/versions/1.0.5),\n# \"UC San Diego Resting State EEG Data from Patients with Parkinson's Disease\", snapshot 1.0.5,\n# DOI 10.18112/openneuro.ds002778.v1.0.5. The paper (2019) predates the dataset (first snapshot\n# 1.0.0, 2020-05-05) and cites no version. 1.0.5 is the most recent published snapshot. Its\n# CHANGES list fixes to the README, citations, a medication entry of sub-pd22 (1.0.1) and Beck\n# scores (1.0.5); none changes the EEG files, so no earlier snapshot matches the paper better.\n# Files are read from the URLs the OpenNeuro API gives for this snapshot, into memory.\n#\n# **What the dataset holds.** Resting EEG (BioSemi, 32 scalp electrodes and 8 external\n# channels, 512 Hz) of 15 patients off and on medication and 16 controls, with UPDRS and other\n# scores in per-session JSON files. It holds no artifact marks and no bad-channel marks, which\n# the paper's preprocessing used; the analysis here therefore rejects no samples and excludes no\n# electrode (the claims file's reading (b) for both).\n#\n# | Claim | Tested here |\n# |---|---|\n# | fig2-sharpness-off-on, fig2-steepness-off-on, fig2-pac-off-on | tested |\n# | bipolar-off-on | tested |\n# | temporalis-f7f8-null, temporalis-t7t8-null | tested |\n# | fig2c-topography-sensorimotor | tested |\n# | offctrl-sharpness-null, offctrl-steepness, offctrl-pac-null, offctrl-pac-csd | tested |\n# | updrs-improvement | tested |\n# | fig1c-beta-alpha-peaks | tested |\n# | table1-alpha-shape-off-on, table1-alpha-pac-null, table2-alpha-offctrl | tested |\n# | pac-beta-larger-than-alpha | tested |\n# | fig3-sharpness-pac-correlation, fig3-steepness-pac-correlation | tested |\n# | fig4a-sensorimotor-q4, q4-patient-counts, fig4b-temporalis-variable-shape, controls-q4 | tested |\n# | table3-q4-effect-size | tested |\n#\n# No claim is blocked. The measures, filters and statistics are in `waveshape.py`, whose\n# docstring says where each parameter comes from.\n\n# %%\nimport itertools\nimport time\nimport warnings\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport waveshape as ws\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 400)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nfiles = ws.listing()\nrecs = ws.sessions()\nwith ThreadPoolExecutor(4) as pool:\n    results = list(pool.map(lambda r: ws.analyse(r.sub, r.ses), recs.itertuples()))\nprint(f\"OpenNeuro {ws.DATASET_ID} snapshot {ws.SNAPSHOT}: {len(files)} files; \"\n      f\"{len(results)} recordings analysed in {time.time() - started:.0f} s\")\n\nshape = pd.concat([r[\"shape\"] for r in results], ignore_index=True)\npac = pd.concat([r[\"pac\"] for r in results], ignore_index=True)\ninfo = pd.DataFrame([r[\"info\"] for r in results])\nGROUP = {\"off\": \"off\", \"on\": \"on\", \"hc\": \"control\"}\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nkinds = files.index.str.replace(r\"sub-(pd|hc)\\d+\", \"sub-X\", regex=True)\nprint(\"Files by kind in the snapshot:\")\nprint(pd.Series(kinds).value_counts().sort_index().to_string())\nbdf = files[files.index.str.endswith(\".bdf\")]\nprint(f\"\\nBDF files: {len(bdf)}, {bdf['size'].sum() / 1e9:.3f} GB; distinct checksums: {bdf['id'].nunique()}\")\nprint(\"\\nChecksum (id) of every file read:\")\nread = files[files.index.str.endswith((\".bdf\", \"participants.tsv\", \"_beh.json\", \"_events.tsv\",\n                                        \"_channels.tsv\", \"_eeg.json\"))]\nprint(read[\"id\"].to_string())\n\n# %% tags=[\"sanity\"]\nparticipants = ws.read_tsv(\"participants.tsv\")\nparticipants[\"group\"] = np.where(participants.participant_id.str.startswith(\"sub-pd\"), \"PD\", \"control\")\nprint(participants.drop(columns=[\"rl_deficits\", \"notes\"]).to_string(index=False))\nsumm = participants.groupby(\"group\").agg(n=(\"participant_id\", \"size\"),\n                                         female=(\"gender\", lambda g: (g.str.lower() == \"f\").sum()),\n                                         age_mean=(\"age\", \"mean\"), age_sd=(\"age\", \"std\"))\nprint(\"\\n\", summ.round(1).to_string())\nprint(\"Paper (Methods, Participants): 15 PD, 8 female, 63.2 +/- 8.2 years; 16 controls, 9 female, 63.5 +/- 9.6 years.\")\nprint(\"\\nNotes column:\")\nprint(participants.loc[participants.notes.notna(), [\"participant_id\", \"notes\"]].to_string(index=False))\nprint(\"\\nRecordings per group:\", recs.group.value_counts().to_dict())\npd_subs = sorted(recs[recs.ses == \"off\"][\"sub\"], key=lambda s: int(s[2:]))\nprint(\"Patients with both off and on:\", len(set(recs[recs.ses == \"off\"][\"sub\"]) & set(recs[recs.ses == \"on\"][\"sub\"])))\n\n# %% [markdown]\n# The participant counts match the paper (15 patients, 16 controls). The table below checks the\n# recordings: sampling rate, duration against the sidecar, channel names, the units and size of\n# the signals, and the sessions the `notes` column says were exported from preprocessed EEGLAB\n# files.\n\n# %% tags=[\"sanity\"]\nside = {}\nfor r in recs.itertuples():\n    base = f\"sub-{r.sub}/ses-{r.ses}/eeg/sub-{r.sub}_ses-{r.ses}_task-rest\"\n    side[(r.sub, r.ses)] = {\"eeg\": ws.read_json(base + \"_eeg.json\"),\n                            \"events\": ws.read_tsv(base + \"_events.tsv\"),\n                            \"channels\": ws.read_tsv(base + \"_channels.tsv\")}\nrows = []\nfor i in info.itertuples():\n    s = side[(i.sub, i.ses)]\n    ch = s[\"channels\"]\n    sd = pd.Series(i.pre_sd_uv)\n    rows.append({\"sub\": i.sub, \"ses\": i.ses, \"sfreq\": i.sfreq, \"dur_s\": i.n_times / i.sfreq,\n                 \"sidecar_dur_s\": s[\"eeg\"][\"RecordingDuration\"] + 1 / 512,\n                 \"n_chan\": len(i.channels), \"scalp_names_ok\": i.channels[:32] == ws.SCALP,\n                 \"status_all_good\": bool((ch.status == \"good\").all()),\n                 \"units\": \"/\".join(sorted(ch.units.dropna().unique())), \"highcut\": ch.high_cutoff.iloc[0],\n                 \"raw_mean_abs_uv\": round(i.raw_mean_abs_uv, 2),\n                 \"raw_max_abs_sum_uv\": round(i.raw_sum_over_channels_uv, 3),\n                 \"pre_sd_min\": round(sd.min(), 2), \"pre_sd_median\": round(sd.median(), 2),\n                 \"pre_sd_max\": round(sd.max(), 1), \"max_sd_chan\": sd.idxmax(), \"min_sd_chan\": sd.idxmin()})\nrec_tab = pd.DataFrame(rows)\nprint(rec_tab.to_string(index=False))\nprint(\"\\nSampling rate values:\", rec_tab.sfreq.unique().tolist())\nprint(\"Duration equals sidecar RecordingDuration + 1 sample in all:\",\n      bool(np.allclose(rec_tab.dur_s, rec_tab.sidecar_dur_s)))\nprint(\"Duration range (s):\", rec_tab.dur_s.min(), \"to\", rec_tab.dur_s.max(), \"(Methods: at least 3 min)\")\nprint(\"All channels.tsv status 'good':\", bool(rec_tab.status_all_good.all()))\n\n# %% [markdown]\n# Every recording is at 512 Hz, lasts 181 to 292 s (the paper says at least 3 min), and has the\n# 32 scalp electrodes of the BioSemi 32 layout in the order of the montage, 8 EXG channels and a\n# Status channel. No electrode is marked bad. In all raw files but two the electrode means are\n# far from zero and the channels do not sum to zero; in sub-pd6 and sub-pd16 `on` the means are\n# near zero and the 32 channels sum to near zero at every sample, so these two files already\n# carry the common average reference, consistent with the `notes` column (\"Used preprocessed\n# data from EEGLAB .mat file\"). Their channels.tsv give a high cutoff of 256 Hz, where the\n# others give 104 Hz. The preprocessing applied here (mean removal, common average, 0.5 Hz\n# high-pass) leaves a re-referenced signal unchanged apart from the high-pass. Electrode\n# standard deviations after preprocessing are listed for each file; results without these two\n# patients are shown as a variant under the main claims.\n\n# %% tags=[\"sanity\"]\n# events.tsv against the Status channel: the only time base in the files\nrows = []\nfor i in info.itertuples():\n    ev = side[(i.sub, i.ses)][\"events\"]\n    trig = ev[ev.value != 65536]\n    changes = [c for c in i.status_changes if c[1] not in (0, 65536)]\n    rows.append({\"sub\": i.sub, \"ses\": i.ses, \"events\": \"; \".join(f\"{int(a)}:{int(b)}\" for a, b in zip(ev[\"sample\"], ev[\"value\"])),\n                 \"status_first_nonzero_changes\": \"; \".join(f\"{a}:{b}\" for a, b in changes[:3])})\nev_tab = pd.DataFrame(rows)\nprint(ev_tab.to_string(index=False))\n\n# %% [markdown]\n# The events files hold one trigger per recording (value 1, 1 to 30 s into the file; sub-pd6\n# `on` at 95.6 s, sub-pd16 `on` an unexplained value), and the Status channel changes at the same\n# samples. The task is rest, with no trials or conditions in time, so there is no trial table\n# whose clock the EEG has to share; the paper uses the whole recording. What the trigger marks is\n# not described; the analysis uses the whole recording, as the claims file says.\n\n# %% tags=[\"sanity\"]\n# recordings deposited twice: identical raw samples at the start of C3, across all pairs\nheads = {(i.sub, i.ses): i.raw_c3_head for i in info.itertuples()}\ndupes = []\nfor a, b in itertools.combinations(heads, 2):\n    x, y = heads[a], heads[b]\n    if np.allclose(x, y) or abs(np.corrcoef(x - x.mean(), y - y.mean())[0, 1]) > 0.99:\n        dupes.append((a, b))\nprint(\"Pairs of recordings with identical (or r > 0.99) first 4 s of raw C3:\", dupes)\nprint(\"Distinct BDF checksums:\", bdf[\"id\"].nunique(), \"of\", len(bdf))\ncnt = shape[(shape.signal.isin([\"C3\", \"C4\"])) & (shape.band == \"beta\")]\nprint(\"\\nBeta peaks per recording at C3 and C4: %d to %d (whole recordings, 100-sample edges dropped)\"\n      % (cnt.n_peaks.min(), cnt.n_peaks.max()))\ncnt = shape[(shape.signal.isin([\"C3\", \"C4\"])) & (shape.band == \"alpha\")]\nprint(\"Alpha peaks per recording at C3 and C4: %d to %d\" % (cnt.n_peaks.min(), cnt.n_peaks.max()))\n\n# %% tags=[\"sanity\"]\nbeh = {}\nfor r in recs.itertuples():\n    beh[(r.sub, r.ses)] = ws.read_json(f\"sub-{r.sub}/ses-{r.ses}/beh/sub-{r.sub}_ses-{r.ses}_task-rest_beh.json\")\nprint(\"Root task-rest_beh.json:\", ws.read_json(\"task-rest_beh.json\"))\nkeys = sorted({k for v in beh.values() for k in v[\"questionairres\"]})\nprint(\"Questionnaire fields in the beh JSON files:\", keys)\nq = pd.DataFrame([{\"sub\": s, \"ses\": e, **v[\"questionairres\"]} for (s, e), v in beh.items()])\nprint(q[q.ses != \"hc\"].sort_values([\"sub\", \"ses\"]).to_string(index=False))\nprint(\"Controls' UPDRS values:\", sorted(q[q.ses == \"hc\"][\"UPDRS\"].unique().tolist()))\npdq = q[q.ses != \"hc\"]\nprint(\"Total UPDRS minus UPDRS 18-26: %d to %d\" % ((pdq[\"Total UPDRS\"] - pdq[\"UPDRS 18-26\"]).min(),\n                                                   (pdq[\"Total UPDRS\"] - pdq[\"UPDRS 18-26\"]).max()))\n\n# %% [markdown]\n# The UPDRS fields have no description in the dataset (the only `beh` sidecar describes a dummy\n# `trial` column). \"Total UPDRS\" ranges from 16 to 58 and exceeds \"UPDRS 18-26\" by 0 to 14,\n# which fits the motor examination (part III, items 18 to 31) and its items 18 to 26; this is\n# consistent with the values, not shown.\n\n# %% [markdown]\n# ### Tables used below\n#\n# `composite` gives one value per participant and session: the mean of a measure over two\n# signals (C3 and C4 unless stated), as the paper's composite (Methods, Data preprocessing,\n# paragraph 2). Patients are paired by subject id.\n\n# %%\ndef composite(table, value, signals=(\"C3\", \"C4\"), **sel):\n    t = table[table.signal.isin(signals)]\n    for k, v in sel.items():\n        t = t[t[k] == v]\n    out = t.groupby([\"sub\", \"ses\"])[value].mean().unstack(\"ses\")\n    assert (t.groupby([\"sub\", \"ses\"]).size() == len(signals)).all()\n    return out\n\n\ndef paired(c):\n    p = c[[\"off\", \"on\"]].dropna()\n    return p.loc[sorted(p.index, key=lambda s: int(s[2:]))]\n\n\ndef ctrl(c):\n    return c[\"hc\"].dropna()\n\n\ndef offon_row(c, label):\n    p = paired(c)\n    W, pa = ws.signed_rank(p.off, p.on)\n    _, pe = ws.signed_rank(p.off, p.on, method=\"exact\")\n    return {\"test\": label, \"n\": len(p), \"W\": W, \"p\": pa, \"p_exact\": pe, \"off>on\": int((p.off > p.on).sum()),\n            \"d\": ws.cohen_d(p.off, p.on), \"mean_off\": p.off.mean(), \"mean_on\": p.on.mean()}\n\n\ndef offctrl_row(c, label):\n    p = paired(c)\n    z, pz = ws.rank_sum(p.off, ctrl(c))\n    return {\"test\": label, \"n_off\": len(p), \"n_ctrl\": len(ctrl(c)), \"z\": z, \"p\": pz,\n            \"d\": ws.cohen_d(p.off, ctrl(c)), \"mean_off\": p.off.mean(), \"mean_ctrl\": ctrl(c).mean()}\n\n\nSHR = lambda band=\"beta\", taps=\"118\", sig=(\"C3\", \"C4\"): composite(shape, \"ShR\", sig, band=band, taps=taps)\nSTR = lambda band=\"beta\", taps=\"118\", sig=(\"C3\", \"C4\"): composite(shape, \"StR\", sig, band=band, taps=taps)\nPAC = lambda band=\"beta\", reading=\"methods\", sig=(\"C3\", \"C4\"): composite(pac, \"PAC\", sig, band=band, reading=reading)\nEXCL = {\"pd6\", \"pd16\"}   # on sessions exported from preprocessed EEGLAB files\n\n# Table 1 (off against on) under every combination of the filter readings, FDR over its six tests\nt1_rows = []\nfor a_taps, a_pac, b_pac in itertools.product([\"192\", \"118\"], [\"a192\", \"b231\", \"c118\"], [\"methods\", \"code\"]):\n    tests = [offon_row(SHR(\"alpha\", a_taps), \"alpha ShR\"), offon_row(STR(\"alpha\", a_taps), \"alpha StR\"),\n             offon_row(PAC(\"alpha\", a_pac), \"alpha PAC\"), offon_row(SHR(), \"beta ShR\"),\n             offon_row(STR(), \"beta StR\"), offon_row(PAC(\"beta\", b_pac), \"beta PAC\")]\n    q_ = ws.fdr_bh([t[\"p\"] for t in tests])\n    for t, qq in zip(tests, q_):\n        t1_rows.append({\"alpha_shape_taps\": a_taps, \"alpha_pac\": a_pac, \"beta_pac\": b_pac, **t, \"p_fdr\": qq})\ntable1 = pd.DataFrame(t1_rows)\n\nt2_rows = []\nfor a_taps, a_pac, b_pac in itertools.product([\"192\", \"118\"], [\"a192\", \"b231\", \"c118\"], [\"methods\", \"code\"]):\n    tests = [offctrl_row(SHR(\"alpha\", a_taps), \"alpha ShR\"), offctrl_row(STR(\"alpha\", a_taps), \"alpha StR\"),\n             offctrl_row(PAC(\"alpha\", a_pac), \"alpha PAC\"), offctrl_row(SHR(), \"beta ShR\"),\n             offctrl_row(STR(), \"beta StR\"), offctrl_row(PAC(\"beta\", b_pac), \"beta PAC\")]\n    q_ = ws.fdr_bh([t[\"p\"] for t in tests])\n    for t, qq in zip(tests, q_):\n        t2_rows.append({\"alpha_shape_taps\": a_taps, \"alpha_pac\": a_pac, \"beta_pac\": b_pac, **t, \"p_fdr\": qq})\ntable2 = pd.DataFrame(t2_rows)\nMAIN = (table1.alpha_shape_taps == \"192\") & (table1.alpha_pac == \"a192\") & (table1.beta_pac == \"methods\")\nprint(\"Table 1, off against on, main readings (alpha shape 192 taps, alpha PAC 192/123, beta PAC 118/123):\")\nprint(table1[MAIN].drop(columns=[\"alpha_shape_taps\", \"alpha_pac\", \"beta_pac\"]).round(4).to_string(index=False))\nMAIN2 = (table2.alpha_shape_taps == \"192\") & (table2.alpha_pac == \"a192\") & (table2.beta_pac == \"methods\")\nprint(\"\\nTable 2, off against controls, main readings:\")\nprint(table2[MAIN2].drop(columns=[\"alpha_shape_taps\", \"alpha_pac\", \"beta_pac\"]).round(4).to_string(index=False))\n\n\ndef fdr_range(table, test):\n    t = table[table.test == test]\n    return t.p_fdr.min(), t.p_fdr.max()\n\n\ndef show_patients(c, label):\n    p = paired(c)\n    print(f\"{label} per patient (off, on, off - on):\")\n    print(pd.DataFrame({\"off\": p.off, \"on\": p.on, \"off-on\": p.off - p.on}).round(4).T.to_string())\n\n# %% [markdown]\n# ## fig2-sharpness-off-on\n#\n# > Over sensorimotor electrodes (C3 and C4 composite), beta sharpness ratio is higher in PD\n# > patients off medication than on medication. Expected: signed rank 12 (+/- 1.2), d 0.86\n# > (+/- 0.086), FDR corrected p < 0.05 over the six tests of Table 1.\n\n# %% tags=[\"claim:fig2-sharpness-off-on\"]\nc = SHR()\nshow_patients(c, \"Beta sharpness ratio (C3/C4 composite)\")\nr = offon_row(c, \"beta ShR\")\nlo, hi = fdr_range(table1, \"beta ShR\")\nprint(\"\\nSigned rank W = %.1f (expected 12 +/- 1.2), p = %.4f (normal approximation; exact %.4f), d = %.3f (expected 0.86 +/- 0.086)\"\n      % (r[\"W\"], r[\"p\"], r[\"p_exact\"], r[\"d\"]))\nprint(\"FDR corrected p over the six tests of Table 1: %.4f to %.4f across the 12 filter-reading combinations\" % (lo, hi))\nprint(\"Off higher than on in %d of %d patients\" % (r[\"off>on\"], r[\"n\"]))\nex = paired(c).drop(index=list(EXCL))\nW, p = ws.signed_rank(ex.off, ex.on)\nprint(\"Variant without pd6 and pd16 (n = %d): W = %.1f, p = %.4f, d = %.3f\" % (len(ex), W, p, ws.cohen_d(ex.off, ex.on)))\nfig, ax = plt.subplots(figsize=(4, 4))\np_ = paired(c)\nax.scatter(p_.off, p_.on)\nm = max(p_.max())\nax.plot([0, m], [0, m], \"k-\", lw=0.5)\nax.set_xlabel(\"sharpness ratio off\")\nax.set_ylabel(\"sharpness ratio on\")\nplt.show()\nprint(\"Plotted range: off %.4f to %.4f, on %.4f to %.4f; no point outside the axes\" % (p_.off.min(), p_.off.max(), p_.on.min(), p_.on.max()))\n\n# %% [markdown]\n# **Result: partially reproduced.** Sharpness ratio is higher off than on in 13 of 15 patients\n# (W = 13, within 12 +/- 1.2; p = 0.0076; FDR corrected p at most 0.012 under every filter\n# reading), but d = 0.73 is below the tolerance of 0.86 +/- 0.086. No artifact samples were\n# rejected, as the dataset holds no marks.\n\n# %% [markdown]\n# ## fig2-steepness-off-on\n#\n# > Over sensorimotor electrodes, beta steepness ratio is higher in PD patients off medication\n# > than on medication. Expected: signed rank 9 (+/- 0.9), d 0.68 (+/- 0.068).\n\n# %% tags=[\"claim:fig2-steepness-off-on\"]\nc = STR()\nshow_patients(c, \"Beta steepness ratio (C3/C4 composite)\")\nr = offon_row(c, \"beta StR\")\nlo, hi = fdr_range(table1, \"beta StR\")\nprint(\"\\nSigned rank W = %.1f (expected 9 +/- 0.9), p = %.4f (exact %.4f), d = %.3f (expected 0.68 +/- 0.068)\"\n      % (r[\"W\"], r[\"p\"], r[\"p_exact\"], r[\"d\"]))\nprint(\"FDR corrected p over Table 1: %.4f to %.4f across the filter readings\" % (lo, hi))\nprint(\"Off higher than on in %d of %d patients\" % (r[\"off>on\"], r[\"n\"]))\nex = paired(c).drop(index=list(EXCL))\nW, p = ws.signed_rank(ex.off, ex.on)\nprint(\"Variant without pd6 and pd16 (n = %d): W = %.1f, p = %.4f, d = %.3f\" % (len(ex), W, p, ws.cohen_d(ex.off, ex.on)))\n\n# %% [markdown]\n# **Result: partially reproduced.** Steepness ratio is higher off than on in 12 of 15 patients\n# (p = 0.0125, FDR corrected at most 0.0161) and d = 0.70 is within 0.68 +/- 0.068, but W = 16\n# is outside 9 +/- 0.9.\n\n# %% [markdown]\n# ## fig2-pac-off-on\n#\n# > Over sensorimotor electrodes, beta-gamma PAC is higher in PD patients off medication than on\n# > medication. Expected: signed rank 15 (+/- 1.5), d 0.83 (+/- 0.083, Table 1).\n\n# %% tags=[\"claim:fig2-pac-off-on\"]\nrows = []\nfor reading in [\"methods\", \"code\"]:\n    c = PAC(\"beta\", reading)\n    r = offon_row(c, f\"beta PAC, {reading} filters\")\n    p_ = paired(c)\n    r[\"d_log10\"] = ws.cohen_d(np.log10(p_.off), np.log10(p_.on))\n    lo, hi = fdr_range(table1[table1.beta_pac == reading], \"beta PAC\")\n    r[\"p_fdr_min\"], r[\"p_fdr_max\"] = lo, hi\n    rows.append(r)\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nshow_patients(PAC(\"beta\", \"methods\"), \"Beta PAC, Methods filters (118/123 samples)\")\nprint(\"Expected: W 15 +/- 1.5 (13.5 to 16.5); d 0.83 +/- 0.083 (0.747 to 0.913)\")\n\n# %% [markdown]\n# **Result: partially reproduced.** PAC is higher off than on (p = 0.0076 with the Methods'\n# filters and 0.0064 with the code's, FDR corrected at most 0.0161), and d on raw PAC is 0.85\n# and 0.86, within 0.83 +/- 0.083 (on log10 PAC 0.73 and 0.86). The signed rank statistic is 13\n# and 12, outside 15 +/- 1.5 under both filter readings.\n\n# %% [markdown]\n# ## bipolar-off-on\n#\n# > With a bipolar montage (C3-CP1 and C4-CP2), sharpness ratio, steepness ratio and PAC each\n# > differ between PD patients off and on medication (paper: p < 0.004, FDR corrected for each).\n\n# %% tags=[\"claim:bipolar-off-on\"]\nBIP = (\"C3-CP1\", \"C4-CP2\")\nfor reading in [\"methods\", \"code\"]:\n    tests = [offon_row(SHR(sig=BIP), \"bipolar ShR\"), offon_row(STR(sig=BIP), \"bipolar StR\"),\n             offon_row(PAC(\"beta\", reading, BIP), f\"bipolar PAC ({reading})\")]\n    t = pd.DataFrame(tests)\n    t[\"p_fdr3\"] = ws.fdr_bh(t.p)\n    print(t.round(4).to_string(index=False), \"\\n\")\nprint(\"Paper bound: p < 0.004 FDR corrected for each measure.\")\n\n# %% [markdown]\n# **Result: reproduced.** With the bipolar pairs all three measures are higher off than on (13,\n# 13 and 12 or 13 of 15 patients), and all three FDR corrected p-values are below 0.05 under\n# both PAC filter readings (largest 0.0106). Only steepness ratio is below the paper's bound of\n# 0.004 (corrected 0.0045 or 0.0046 against 0.0106 for sharpness and 0.0096 or 0.0081 for PAC).\n\n# %% [markdown]\n# ## temporalis-f7f8-null and temporalis-t7t8-null\n#\n# > Over F7 and F8 (and over T7 and T8), none of sharpness ratio, steepness ratio or PAC differs\n# > between patients off and on medication (paper F7/F8: p = 0.73, 0.394, 0.191 uncorrected).\n\n# %% tags=[\"claim:temporalis-f7f8-null\"]\nFT = (\"F7\", \"F8\")\nrows = [offon_row(SHR(sig=FT), \"F7/F8 ShR\"), offon_row(STR(sig=FT), \"F7/F8 StR\"),\n        offon_row(PAC(\"beta\", \"methods\", FT), \"F7/F8 PAC (methods)\"), offon_row(PAC(\"beta\", \"code\", FT), \"F7/F8 PAC (code)\")]\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"Paper: sharpness p = 0.73, steepness p = 0.394, PAC p = 0.191, uncorrected\")\n\n# %% [markdown]\n# **Result: reproduced.** At F7 and F8 no measure differs at p < 0.05 uncorrected: sharpness\n# ratio p = 0.69 (d 0.31), steepness ratio p = 0.17 (d 0.57), PAC p = 0.0995 with the Methods'\n# filters and 0.078 with the code's (d 0.67).\n\n# %% tags=[\"claim:temporalis-t7t8-null\"]\nTT = (\"T7\", \"T8\")\nrows = [offon_row(SHR(sig=TT), \"T7/T8 ShR\"), offon_row(STR(sig=TT), \"T7/T8 StR\"),\n        offon_row(PAC(\"beta\", \"methods\", TT), \"T7/T8 PAC (methods)\"), offon_row(PAC(\"beta\", \"code\", TT), \"T7/T8 PAC (code)\")]\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\n\n# %% [markdown]\n# **Result: reproduced.** At T7 and T8 no measure differs at p < 0.05 uncorrected (sharpness\n# p = 0.36, steepness p = 0.95, PAC p = 0.11 under both filter readings).\n\n# %% [markdown]\n# ## fig2c-topography-sensorimotor\n#\n# > Scalp topographies of the off against on medication test statistic for each measure are\n# > consistent with a sensorimotor origin. Criterion: for each beta measure, the electrode with\n# > the smallest p is C3, Cz, C4 or a neighbour (FC1, FC2, FC5, FC6, CP1, CP2, CP5, CP6), and none\n# > of F7, F8, T7, T8 is significant (p < 0.05 uncorrected, or FDR over electrodes).\n\n# %% tags=[\"claim:fig2c-topography-sensorimotor\"]\nSENSORI = {\"C3\", \"Cz\", \"C4\", \"FC1\", \"FC2\", \"FC5\", \"FC6\", \"CP1\", \"CP2\", \"CP5\", \"CP6\"}\nTEMPORAL = [\"F7\", \"F8\", \"T7\", \"T8\"]\ntopo = []\nfor label, tab, val, sel in [(\"ShR\", shape, \"ShR\", {\"band\": \"beta\", \"taps\": \"118\"}),\n                             (\"StR\", shape, \"StR\", {\"band\": \"beta\", \"taps\": \"118\"}),\n                             (\"PAC methods\", pac, \"PAC\", {\"band\": \"beta\", \"reading\": \"methods\"}),\n                             (\"PAC code\", pac, \"PAC\", {\"band\": \"beta\", \"reading\": \"code\"})]:\n    t = tab[tab.signal.isin(ws.SCALP)]\n    for k, v in sel.items():\n        t = t[t[k] == v]\n    wide = t.pivot_table(index=[\"sub\", \"ses\"], columns=\"signal\", values=val)\n    for ch in ws.SCALP:\n        cc = wide[ch].unstack(\"ses\")\n        p_ = paired(cc)\n        W, p = ws.signed_rank(p_.off, p_.on)\n        topo.append({\"measure\": label, \"electrode\": ch, \"W\": W, \"p\": p, \"off>on\": int((p_.off > p_.on).sum())})\ntopo = pd.DataFrame(topo)\ntopo[\"p_fdr32\"] = topo.groupby(\"measure\").p.transform(lambda s: ws.fdr_bh(s.values))\nfor m, t in topo.groupby(\"measure\", sort=False):\n    t = t.sort_values(\"p\")\n    best = t.iloc[0]\n    tem = t[t.electrode.isin(TEMPORAL)]\n    print(f\"{m}: smallest p at {best.electrode} (p = {best.p:.4f}); in sensorimotor set: {best.electrode in SENSORI}; \"\n          f\"significant uncorrected: {t[t.p < 0.05].electrode.tolist()}; FDR: {t[t.p_fdr32 < 0.05].electrode.tolist()}\")\n    print(\"   F7/F8/T7/T8 p:\", dict(zip(tem.electrode, tem.p.round(4))), \"\\n   five smallest:\",\n          dict(zip(t.electrode[:5], t.p[:5].round(4))))\nfig, axes = plt.subplots(1, 3, figsize=(12, 3))\nfor ax, m in zip(axes, [\"ShR\", \"StR\", \"PAC methods\"]):\n    t = topo[topo.measure == m].set_index(\"electrode\").loc[ws.SCALP]\n    ax.bar(range(32), -np.log10(t.p))\n    ax.axhline(-np.log10(0.05), color=\"k\", lw=0.5)\n    ax.set_xticks(range(32), ws.SCALP, rotation=90, fontsize=6)\n    ax.set_title(m)\n    ax.set_ylabel(\"-log10 p\")\nplt.tight_layout()\nplt.show()\nprint(\"-log10 p range plotted: %.2f to %.2f; nothing outside the axes\" % ((-np.log10(topo.p)).min(), (-np.log10(topo.p)).max()))\n\n# %% [markdown]\n# **Result: see the summary.** The outcome is judged from the printed electrodes: for each\n# measure the electrode with the smallest p, and the p at F7, F8, T7 and T8.\n\n# %% [markdown]\n# ## offctrl-sharpness-null\n#\n# > Beta sharpness ratio over sensorimotor electrodes does not differ between patients off\n# > medication and controls (paper: rank sum 0.91, p = 0.363; d 0.19).\n\n# %% tags=[\"claim:offctrl-sharpness-null\"]\nr = offctrl_row(SHR(), \"beta ShR, off vs controls\")\nprint(pd.DataFrame([r]).round(4).to_string(index=False))\nprint(\"Paper: z = 0.91, p = 0.3631 uncorrected, d = 0.19 (+/- 0.019)\")\n\n# %% [markdown]\n# **Result: reproduced.** The rank sum test finds no difference (z = 0.47, p = 0.64). d = 0.09\n# is outside the expected 0.19 +/- 0.019; the claim of absence is judged on the test.\n\n# %% [markdown]\n# ## offctrl-steepness\n#\n# > Beta steepness ratio over sensorimotor electrodes is higher in patients off medication than\n# > in controls, with the average reference and with a bipolar montage. Expected: z 2.53\n# > (+/- 0.253), d 0.88 (+/- 0.088); FDR over Table 2 for the average reference; bipolar\n# > significant under one reading (FDR over the three bipolar measures, or the single test).\n\n# %% tags=[\"claim:offctrl-steepness\"]\nr = offctrl_row(STR(), \"beta StR, average reference\")\nlo, hi = fdr_range(table2, \"beta StR\")\nprint(pd.DataFrame([r]).round(4).to_string(index=False))\nprint(\"FDR corrected over the six tests of Table 2: %.4f to %.4f across filter readings\" % (lo, hi))\nfor reading in [\"methods\", \"code\"]:\n    b = [offctrl_row(SHR(sig=BIP), \"bipolar ShR\"), offctrl_row(STR(sig=BIP), \"bipolar StR\"),\n         offctrl_row(PAC(\"beta\", reading, BIP), f\"bipolar PAC ({reading})\")]\n    b = pd.DataFrame(b)\n    b[\"p_fdr3\"] = ws.fdr_bh(b.p)\n    print(\"\\nBipolar montage, off against controls:\")\n    print(b.round(4).to_string(index=False))\nprint(\"\\nPaper: average reference z = 2.53, p = 0.011 (FDR 0.0331), d = 0.88; bipolar p = 0.028 FDR corrected\")\n\n# %% [markdown]\n# **Result: reproduced.** With the average reference steepness ratio is higher off than in\n# controls, z = 2.37 (within 2.53 +/- 0.253), p = 0.018, FDR corrected 0.053 to 0.106 over Table\n# 2 depending on the filter readings, d = 0.85 (within 0.88 +/- 0.088). See the summary for how\n# the FDR result bears on the outcome. With the bipolar pairs z = 2.37, p = 0.018 as a single\n# test, and 0.053 FDR corrected over the three bipolar measures.\n\n# %% [markdown]\n# ## offctrl-pac-null and offctrl-pac-csd\n#\n# > With the average reference, beta PAC does not differ between patients off and controls\n# > (paper p = 0.236). With a current source density montage, beta PAC is higher off than in\n# > controls (paper p = 0.022).\n\n# %% tags=[\"claim:offctrl-pac-null\"]\nrows = [offctrl_row(PAC(\"beta\", rd), f\"beta PAC average reference ({rd})\") for rd in [\"methods\", \"code\"]]\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"Paper: z = 1.19, p = 0.236 uncorrected\")\n\n# %% [markdown]\n# **Result: reproduced.** No difference with the average reference: p = 0.32 with the Methods'\n# filters (z = 0.99) and 0.29 with the code's (z = 1.07).\n\n# %% tags=[\"claim:offctrl-pac-csd\"]\nCSD = (\"CSD C3\", \"CSD C4\")\nrows = [offctrl_row(PAC(\"beta\", rd, CSD), f\"beta PAC, CSD ({rd})\") for rd in [\"methods\", \"code\"]]\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nrows = [offon_row(PAC(\"beta\", rd, CSD), f\"beta PAC, CSD, off vs on ({rd})\") for rd in [\"methods\", \"code\"]]\nprint(\"\\nFor reference, CSD PAC off against on:\")\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"Paper: off against controls p = 0.022\")\n\n# %% [markdown]\n# **Result: not reproduced.** With the CSD montage PAC is higher off than in controls (z = 1.78)\n# but not significantly (p = 0.075 under both filter readings), where the paper reports\n# p = 0.022.\n\n# %% [markdown]\n# ## updrs-improvement\n#\n# > UPDRS is lower on medication than off (paper: signed rank 3.5, p = 0.003). Readings: motor\n# > part (III) total and the total of all parts the dataset holds.\n\n# %% tags=[\"claim:updrs-improvement\"]\nu = q[q.ses != \"hc\"].pivot(index=\"sub\", columns=\"ses\")\nrows = []\nfor field in [\"Total UPDRS\", \"UPDRS 18-26\"]:\n    off, on = u[(field, \"off\")].astype(float), u[(field, \"on\")].astype(float)\n    W, p = ws.signed_rank(off, on)\n    rows.append({\"field\": field, \"n\": len(off), \"W\": W, \"p\": p, \"median_off\": off.median(), \"median_on\": on.median(),\n                 \"lower_on\": int((on < off).sum()), \"equal\": int((on == off).sum()), \"higher_on\": int((on > off).sum())})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"scipy's signed rank (zero_method 'wilcox') drops tied pairs; with 'pratt' or 'zsplit':\")\nfor field in [\"Total UPDRS\", \"UPDRS 18-26\"]:\n    off, on = u[(field, \"off\")].astype(float), u[(field, \"on\")].astype(float)\n    for zm in [\"pratt\", \"zsplit\"]:\n        r_ = stats.wilcoxon(off, on, zero_method=zm, method=\"approx\", correction=False)\n        print(f\"  {field}, {zm}: W = {r_.statistic:.1f}, p = {r_.pvalue:.4f}\")\nprint(\"Paper: W = 3.5, p = 0.003; expected W 3.5 +/- 0.35\")\n\n# %% [markdown]\n# **Result: see the summary.** The statistic and p are printed above for both fields.\n\n# %% [markdown]\n# ## fig1c-beta-alpha-peaks\n#\n# > The average power spectrum of each group shows an oscillation in the beta band and a\n# > prominent mu/alpha oscillation. Criterion: a local maximum between 8 and 12 Hz and one between\n# > 13 and 30 Hz in each group's average Welch spectrum (C3 and C4; all electrodes a variant).\n\n# %% tags=[\"claim:fig1c-beta-alpha-peaks\"]\nfreqs = results[0][\"freqs\"]\nspec = {}\nfor r_, rec in zip(results, recs.itertuples()):\n    spec[(rec.sub, rec.ses)] = r_[\"psd\"]\n\n\ndef group_spectrum(ses, chans):\n    return np.mean([spec[k].loc[list(chans)].values.mean(axis=0) for k in spec if k[1] == ses], axis=0)\n\n\ndef local_max(s, lo, hi):\n    i = np.arange(1, len(s) - 1)\n    peak = (s[i] > s[i - 1]) & (s[i] > s[i + 1]) & (freqs[i] >= lo) & (freqs[i] <= hi)\n    return [round(float(f), 2) for f in freqs[i][peak]]\n\n\nfig, axes = plt.subplots(1, 2, figsize=(10, 3.5))\nfor ax, (label, chans) in zip(axes, [(\"C3 and C4\", [\"C3\", \"C4\"]), (\"all 32 electrodes\", ws.SCALP)]):\n    for ses in [\"off\", \"on\", \"hc\"]:\n        s = group_spectrum(ses, chans)\n        print(f\"{label}, {GROUP[ses]}: local maxima 8-12 Hz {local_max(s, 8, 12)}, 13-30 Hz {local_max(s, 13, 30)}\")\n        keep = freqs <= 45\n        ax.semilogy(freqs[keep], s[keep], label=GROUP[ses])\n    ax.set_title(label)\n    ax.set_xlabel(\"Hz\")\n    ax.set_ylabel(\"power (uV^2/Hz)\")\n    ax.legend()\nplt.tight_layout()\nplt.show()\nprint(\"Frequency resolution %.3f Hz; plotted 0 to 45 Hz\" % (freqs[1] - freqs[0]))\nfor ses in [\"off\", \"on\", \"hc\"]:\n    n_alpha = sum(bool(local_max(spec[k].loc[[\"C3\", \"C4\"]].values.mean(axis=0), 8, 12)) for k in spec if k[1] == ses)\n    n_beta = sum(bool(local_max(spec[k].loc[[\"C3\", \"C4\"]].values.mean(axis=0), 13, 30)) for k in spec if k[1] == ses)\n    n = sum(1 for k in spec if k[1] == ses)\n    print(f\"Per recording, {GROUP[ses]}: alpha local max in {n_alpha}/{n}, beta local max in {n_beta}/{n}\")\n\n# %% [markdown]\n# **Result: see the summary.** The local maxima of each group's spectrum are printed above.\n\n# %% [markdown]\n# ## table1-alpha-shape-off-on\n#\n# > In the mu/alpha band (8 to 12 Hz), sharpness ratio and steepness ratio are also higher off\n# > medication than on. Expected: sharpness W 20 (+/- 2), d 0.70 (+/- 0.07); steepness W 12\n# > (+/- 1.2), d 0.60 (+/- 0.06); FDR corrected p < 0.05 over Table 1.\n\n# %% tags=[\"claim:table1-alpha-shape-off-on\"]\nt = table1[table1.test.isin([\"alpha ShR\", \"alpha StR\"])]\nprint(t.groupby([\"alpha_shape_taps\", \"test\"]).agg(W=(\"W\", \"first\"), p=(\"p\", \"first\"), d=(\"d\", \"first\"),\n      off_gt_on=(\"off>on\", \"first\"), p_fdr_min=(\"p_fdr\", \"min\"), p_fdr_max=(\"p_fdr\", \"max\")).round(4).to_string())\nprint(\"Expected: ShR W 18 to 22, d 0.63 to 0.77; StR W 10.8 to 13.2, d 0.54 to 0.66\")\n\n# %% [markdown]\n# **Result: partially reproduced.** Both alpha measures are higher off than on with FDR corrected\n# p below 0.05 under both shape filter readings (largest 0.0317). Sharpness ratio matches\n# (W = 18 or 19, d = 0.71 or 0.66) and the steepness d matches (0.58 or 0.59), but the steepness\n# W = 21 is outside 12 +/- 1.2.\n\n# %% [markdown]\n# ## table1-alpha-pac-null\n#\n# > In the mu/alpha band, PAC does not differ significantly between patients off and on\n# > medication (FDR corrected over Table 1, at 0.05; paper corrected p = 0.0881, d 0.51).\n\n# %% tags=[\"claim:table1-alpha-pac-null\"]\nt = table1[table1.test == \"alpha PAC\"]\nprint(t.groupby(\"alpha_pac\").agg(W=(\"W\", \"first\"), p=(\"p\", \"first\"), d=(\"d\", \"first\"),\n      p_fdr_min=(\"p_fdr\", \"min\"), p_fdr_max=(\"p_fdr\", \"max\")).round(4).to_string())\nfor rd in [\"a192\", \"b231\", \"c118\"]:\n    p_ = paired(PAC(\"alpha\", rd))\n    print(f\"{rd}: d on log10 PAC = {ws.cohen_d(np.log10(p_.off), np.log10(p_.on)):.3f}\")\nprint(\"Readings: a192 = 192-tap phase filter (3 cycles of 8 Hz) with the Methods' 123-sample gamma filter; \"\n      \"b231 = the code's 231/240 taps; c118 = the Methods' 118 samples with 123\")\n\n# %% [markdown]\n# **Result: see the summary.** The readings differ: the corrected p is printed for each.\n\n# %% [markdown]\n# ## table2-alpha-offctrl\n#\n# > In the mu/alpha band, steepness ratio is higher in patients off medication than in\n# > controls, while sharpness ratio and PAC do not differ after correction. Expected: steepness\n# > z 2.53 (+/- 0.253), d 0.87 (+/- 0.087).\n\n# %% tags=[\"claim:table2-alpha-offctrl\"]\nt = table2[table2.test.str.startswith(\"alpha\")]\nprint(t.groupby([\"test\", \"alpha_shape_taps\", \"alpha_pac\"]).agg(z=(\"z\", \"first\"), p=(\"p\", \"first\"), d=(\"d\", \"first\"),\n      p_fdr_min=(\"p_fdr\", \"min\"), p_fdr_max=(\"p_fdr\", \"max\")).round(4).to_string())\nprint(\"Expected: StR z 2.277 to 2.783, d 0.783 to 0.957, corrected p < 0.05; ShR and PAC corrected p >= 0.05\")\n\n# %% [markdown]\n# **Result: see the summary.** z, d and the corrected p are printed for each reading.\n\n# %% [markdown]\n# ## pac-beta-larger-than-alpha\n#\n# > The off against on difference in PAC is larger in the beta band than in the mu/alpha band\n# > (paper: signed rank 11, p = 0.005). Per patient, composite PAC off minus on in beta and in\n# > alpha, signed rank test of the two differences; raw PAC main, log PAC a variant.\n\n# %% tags=[\"claim:pac-beta-larger-than-alpha\"]\nrows = []\nfor b_rd, a_rd, scale in itertools.product([\"methods\", \"code\"], [\"a192\", \"b231\", \"c118\"], [\"raw\", \"log10\"]):\n    pb, pa = paired(PAC(\"beta\", b_rd)), paired(PAC(\"alpha\", a_rd))\n    f = (lambda v: v) if scale == \"raw\" else np.log10\n    db, da = f(pb.off) - f(pb.on), f(pa.off) - f(pa.on)\n    W, p = ws.signed_rank(db, da)\n    rows.append({\"beta\": b_rd, \"alpha\": a_rd, \"scale\": scale, \"W\": W, \"p\": p,\n                 \"beta_diff_larger\": int((db > da).sum()), \"median_beta_diff\": db.median(), \"median_alpha_diff\": da.median()})\nprint(pd.DataFrame(rows).round(5).to_string(index=False))\nprint(\"Expected: W 11 +/- 1.1 (9.9 to 12.1), p < 0.05, beta difference larger\")\n\n# %% [markdown]\n# **Result: see the summary.** Every filter reading and both scales are printed above.\n\n# %% [markdown]\n# ## fig3-sharpness-pac-correlation and fig3-steepness-pac-correlation\n#\n# > Across patients, beta sharpness ratio (steepness ratio) and PAC over sensorimotor electrodes\n# > are positively correlated both off and on medication. Expected Spearman r: sharpness 0.70\n# > off, 0.74 on; steepness 0.74 off, 0.68 on (each +/- 10%).\n\n# %% tags=[\"claim:fig3-sharpness-pac-correlation\"]\ndef corr_table(measure):\n    rows = []\n    for rd in [\"methods\", \"code\"]:\n        cp, cm = paired(PAC(\"beta\", rd)), paired(measure())\n        for ses in [\"off\", \"on\"]:\n            r_, p_ = stats.spearmanr(cm[ses], cp[ses])\n            rows.append({\"PAC filters\": rd, \"state\": ses, \"n\": len(cm), \"spearman_r\": r_, \"p\": p_})\n    return pd.DataFrame(rows)\n\n\nprint(corr_table(SHR).round(4).to_string(index=False))\nprint(\"Expected: off 0.70 (0.63 to 0.77), on 0.74 (0.666 to 0.814)\")\ncm, cp = paired(SHR()), paired(PAC(\"beta\", \"methods\"))\nfig, axes = plt.subplots(1, 2, figsize=(8, 3.5))\nfor ax, ses in zip(axes, [\"off\", \"on\"]):\n    ax.scatter(cm[ses], cp[ses])\n    ax.set_xlabel(f\"sharpness ratio {ses}\")\n    ax.set_ylabel(f\"PAC {ses}\")\nplt.tight_layout()\nplt.show()\nprint(\"Plotted ranges: sharpness %.4f to %.4f, PAC %.4f to %.4f\" % (cm.min().min(), cm.max().max(), cp.min().min(), cp.max().max()))\n\n# %% [markdown]\n# **Result: see the summary.** The correlations are printed above for both PAC filter readings.\n\n# %% tags=[\"claim:fig3-steepness-pac-correlation\"]\nprint(corr_table(STR).round(4).to_string(index=False))\nprint(\"Expected: off 0.74 (0.666 to 0.814), on 0.68 (0.612 to 0.748)\")\n\n# %% [markdown]\n# **Result: see the summary.** The correlations are printed above for both PAC filter readings.\n\n# %% [markdown]\n# ## fig4a-sensorimotor-q4\n#\n# > Over sensorimotor electrodes, patients' beta waveforms mostly have sharper peaks than troughs\n# > and steeper decays than rises (Q4: log10 peak-to-trough ratio > 0 and log10 rise-to-fall\n# > ratio < 0). One point per patient, electrode (C3, C4) and state: 60 points.\n\n# %% tags=[\"claim:fig4a-sensorimotor-q4\"]\ndef quadrant(ptr, rdr):\n    return np.select([(ptr > 0) & (rdr > 0), (ptr < 0) & (rdr > 0), (ptr < 0) & (rdr < 0), (ptr > 0) & (rdr < 0)],\n                     [\"Q1\", \"Q2\", \"Q3\", \"Q4\"], \"on an axis\")\n\n\npts = shape[(shape.band == \"beta\") & (shape.taps == \"118\") & shape.signal.isin(ws.SCALP)].copy()\npts[\"quadrant\"] = quadrant(pts.PTR.values, pts.RDR.values)\npts[\"group\"] = pts.ses.map(GROUP)\n\n\ndef quad_counts(signals, groups):\n    t = pts[pts.signal.isin(signals) & pts.group.isin(groups)]\n    return t, t.quadrant.value_counts().reindex([\"Q1\", \"Q2\", \"Q3\", \"Q4\"], fill_value=0)\n\n\nt, qc = quad_counts([\"C3\", \"C4\"], [\"off\", \"on\"])\nprint(f\"Patients, C3 and C4, off and on: {len(t)} points\")\nprint(qc.to_string(), \"\\nshare in Q4: %.3f\" % (qc[\"Q4\"] / len(t)))\nprint(\"\\nBy electrode and state:\")\nprint(pd.crosstab([t.signal, t.ses], t.quadrant).to_string())\nprint(\"\\nBy patient (number of the 4 points in Q4):\")\nprint(t.groupby(\"sub\").quadrant.apply(lambda s: int((s == \"Q4\").sum())).to_string())\nfig, axes = plt.subplots(1, 2, figsize=(9, 4))\nfor ax, sig in zip(axes, [[\"C3\", \"C4\"], [\"F7\", \"F8\"]]):\n    tt = pts[pts.signal.isin(sig) & pts.group.isin([\"off\", \"on\"])]\n    for ses, mk in [(\"off\", \"o\"), (\"on\", \"s\")]:\n        u_ = tt[tt.ses == ses]\n        ax.scatter(u_.PTR, u_.RDR, marker=mk, label=ses)\n    ax.axhline(0, color=\"k\", lw=0.5)\n    ax.axvline(0, color=\"k\", lw=0.5)\n    ax.set_xlim(-0.3, 0.3)\n    ax.set_ylim(-0.3, 0.3)\n    ax.set_xlabel(\"log10 peak-to-trough ratio\")\n    ax.set_ylabel(\"log10 rise-to-fall ratio\")\n    ax.set_title(\"/\".join(sig))\n    ax.legend()\n    out = ((tt.PTR.abs() > 0.3) | (tt.RDR.abs() > 0.3)).sum()\n    print(f\"{'/'.join(sig)}: PTR {tt.PTR.min():.3f} to {tt.PTR.max():.3f}, RDR {tt.RDR.min():.3f} to {tt.RDR.max():.3f}; {out} points outside the axes\")\nplt.tight_layout()\nplt.show()\n\n# %% [markdown]\n# **Result: see the summary.** The quadrant counts are printed above.\n\n# %% [markdown]\n# ## q4-patient-counts\n#\n# > Nine of 15 patients have both off and on data in Q4 at C3, eight at C4; eight have both\n# > electrodes in Q4, giving nine patients with at least one electrode in Q4 on and off.\n\n# %% tags=[\"claim:q4-patient-counts\"]\npq = pts[pts.signal.isin([\"C3\", \"C4\"]) & pts.group.isin([\"off\", \"on\"])]\nboth = pq.assign(q4=pq.quadrant == \"Q4\").pivot_table(index=\"sub\", columns=[\"signal\", \"ses\"], values=\"q4\", aggfunc=\"first\")\nmeets = pd.DataFrame({\"C3\": both[(\"C3\", \"off\")] & both[(\"C3\", \"on\")], \"C4\": both[(\"C4\", \"off\")] & both[(\"C4\", \"on\")]})\nprint(meets.astype(int).T.to_string())\nn_c3, n_c4 = int(meets.C3.sum()), int(meets.C4.sum())\nn_both, n_any = int((meets.C3 & meets.C4).sum()), int((meets.C3 | meets.C4).sum())\nprint(f\"\\nPatients meeting the criterion: C3 {n_c3}, C4 {n_c4}, both {n_both}, at least one {n_any}\")\nprint(\"Expected (+/- 1): C3 9, C4 8, both 8, at least one 9; swapped electrode order C3 8, C4 9\")\n\n# %% [markdown]\n# **Result: see the summary.** The four counts are printed above.\n\n# %% [markdown]\n# ## fig4b-temporalis-variable-shape\n#\n# > Electrodes closest to the temporalis muscles (F7 and F8) show a more variable waveform shape\n# > than sensorimotor electrodes. Readings: (a) a lower share of points in the most common\n# > quadrant at F7/F8; (b) a larger spread of the points about their centroid.\n\n# %% tags=[\"claim:fig4b-temporalis-variable-shape\"]\nrows = []\nfor sig in [[\"C3\", \"C4\"], [\"F7\", \"F8\"]]:\n    tt, qc = quad_counts(sig, [\"off\", \"on\"])\n    xy = tt[[\"PTR\", \"RDR\"]].values\n    spread = np.sqrt(((xy - xy.mean(axis=0)) ** 2).sum(axis=1).mean())\n    rows.append({\"electrodes\": \"/\".join(sig), \"n\": len(tt), **qc.to_dict(), \"most_common\": qc.idxmax(),\n                 \"share_most_common\": qc.max() / len(tt), \"rms_distance_to_centroid\": spread,\n                 \"sd_PTR\": tt.PTR.std(), \"sd_RDR\": tt.RDR.std()})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\n\n# %% [markdown]\n# **Result: see the summary.** Both readings are printed above.\n\n# %% [markdown]\n# ## controls-q4\n#\n# > Control participants show the same pattern, their sensorimotor beta waveforms falling mainly\n# > in Q4 (32 points: 16 controls, C3 and C4).\n\n# %% tags=[\"claim:controls-q4\"]\nt, qc = quad_counts([\"C3\", \"C4\"], [\"control\"])\nprint(f\"Controls, C3 and C4: {len(t)} points\")\nprint(qc.to_string(), \"\\nshare in Q4: %.3f\" % (qc[\"Q4\"] / len(t)))\nprint(pd.crosstab(t.signal, t.quadrant).to_string())\n\n# %% [markdown]\n# **Result: see the summary.** The quadrant counts are printed above.\n\n# %% [markdown]\n# ## table3-q4-effect-size\n#\n# > Restricting to patients whose sensorimotor waveforms fall in Q4 both off and on increases the\n# > off against on effect size of all three measures. Expected Q4 d: sharpness 0.95, steepness\n# > 0.70, PAC 0.83 (each +/- 10%); all-patient PAC d in Table 3 0.75.\n\n# %% tags=[\"claim:table3-q4-effect-size\"]\ndef q4_values(table, value, **sel):\n    t = table[table.signal.isin([\"C3\", \"C4\"])]\n    for k, v in sel.items():\n        t = t[t[k] == v]\n    w_ = t.pivot_table(index=\"sub\", columns=[\"signal\", \"ses\"], values=value)\n    out = {}\n    for s in meets.index:\n        el = [e for e in [\"C3\", \"C4\"] if meets.loc[s, e]]\n        if el:\n            out[s] = {ses: np.mean([w_.loc[s, (e, ses)] for e in el]) for ses in [\"off\", \"on\"]}\n    return pd.DataFrame(out).T\n\n\nrows = []\nfor label, table, value, sel, f in [\n        (\"ShR\", shape, \"ShR\", {\"band\": \"beta\", \"taps\": \"118\"}, None),\n        (\"StR\", shape, \"StR\", {\"band\": \"beta\", \"taps\": \"118\"}, None),\n        (\"PAC raw, methods\", pac, \"PAC\", {\"band\": \"beta\", \"reading\": \"methods\"}, None),\n        (\"PAC raw, code\", pac, \"PAC\", {\"band\": \"beta\", \"reading\": \"code\"}, None),\n        (\"PAC log10, methods\", pac, \"PAC\", {\"band\": \"beta\", \"reading\": \"methods\"}, np.log10),\n        (\"PAC log10, code\", pac, \"PAC\", {\"band\": \"beta\", \"reading\": \"code\"}, np.log10)]:\n    allp = paired(composite(table, value, **sel))\n    q4 = q4_values(table, value, **sel)\n    if f is not None:\n        allp, q4 = f(allp), f(q4)\n    rows.append({\"measure\": label, \"n_all\": len(allp), \"d_all\": ws.cohen_d(allp.off, allp.on),\n                 \"n_q4\": len(q4), \"d_q4\": ws.cohen_d(q4.off, q4.on)})\nt3 = pd.DataFrame(rows)\nt3[\"increase\"] = t3.d_q4 > t3.d_all\nprint(t3.round(3).to_string(index=False))\nprint(\"Expected Q4 d: ShR 0.95 (0.855 to 1.045), StR 0.70 (0.63 to 0.77), PAC 0.83 (0.747 to 0.913); all-patient PAC 0.75 (0.675 to 0.825)\")\n\n# %% [markdown]\n# **Result: see the summary.** The effect sizes are printed above.\n\n# %% [markdown]\n# ## Summary\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/src.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds002778-jackson-2019; . $TMPDIR/dev/bin/activate; MPLBACKEND=Agg timeout 900 python $TMPDIR/nb/src.py > $TMPDIR/nb/out.txt 2>&1; echo exit $?; wc -l $TMPDIR/nb/out.txt; head -c 6000 $TMPDIR/nb/out.txt
```

```
exit 1
4 /tmp/claude-1001/nb/out.txt
Traceback (most recent call last):
  File "/tmp/claude-1001/nb/src.py", line 53, in <module>
    import waveshape as ws
ModuleNotFoundError: No module named 'waveshape'
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds002778-jackson-2019; . $TMPDIR/dev/bin/activate; PYTHONPATH=. MPLBACKEND=Agg timeout 900 python $TMPDIR/nb/src.py > $TMPDIR/nb/out.txt 2>&1; echo exit $?; wc -l $TMPDIR/nb/out.txt; tail -30 $TMPDIR/nb/out.txt
```

```
exit 0
718 /tmp/claude-1001/nb/out.txt
C3/C4: PTR -0.015 to 0.099, RDR -0.253 to 0.134; 0 points outside the axes
F7/F8: PTR -0.257 to 0.084, RDR -0.207 to 0.127; 0 points outside the axes
sub  pd11  pd12  pd13  pd14  pd16  pd17  pd19  pd22  pd23  pd26  pd28  pd3  pd5  pd6  pd9
C3      1     0     0     1     0     1     1     1     1     1     0    1    1    1    0
C4      0     1     1     1     0     1     1     0     1     1     1    1    0    1    0

Patients meeting the criterion: C3 10, C4 10, both 7, at least one 13
Expected (+/- 1): C3 9, C4 8, both 8, at least one 9; swapped electrode order C3 8, C4 9
electrodes  n  Q1  Q2  Q3  Q4 most_common  share_most_common  rms_distance_to_centroid  sd_PTR  sd_RDR
     C3/C4 60   6   4   2  48          Q4             0.8000                    0.0763  0.0261  0.0724
     F7/F8 60   1  41  12   6          Q2             0.6833                    0.0926  0.0679  0.0641
Controls, C3 and C4: 32 points
quadrant
Q1     2
Q2     2
Q3     3
Q4    25 
share in Q4: 0.781
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p $TMPDIR/nb/out.txt | grep -v "^MD5E\|^sub-.*MD5E" | cut -c1-260 | sed -n 1,400p | awk 'length>0' | head -300
```

```
<persisted-output>
Output too large (32KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6ab43d83-cf94-4395-a194-1d247b291768/tool-results/bwznji6oy.txt

Preview (first 2KB):
OpenNeuro ds002778 snapshot 1.0.5: 331 files; 46 recordings analysed in 55 s
Files by kind in the snapshot:
filename
.datalad/.gitattributes                                    1
.datalad/config                                            1
.gitattributes                                             1
CHANGES                                                    1
README                                                     1
dataset_description.json                                   1
participants.json                                          1
participants.tsv                                           1
sub-X/ses-hc/beh/sub-X_ses-hc_task-rest_beh.json          16
sub-X/ses-hc/beh/sub-X_ses-hc_task-rest_beh.tsv           16
sub-X/ses-hc/eeg/sub-X_ses-hc_task-rest_channels.tsv      16
sub-X/ses-hc/eeg/sub-X_ses-hc_task-rest_eeg.bdf           16
sub-X/ses-hc/eeg/sub-X_ses-hc_task-rest_eeg.json          16
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb; n=$(grep -n "Checksum (id)" out.txt | cut -d: -f1); m=$(grep -n "participant_id  age" out.txt | cut -d: -f1); sed -n "$((m)),220p" out.txt | cut -c1-230
```

```
participant_id  age gender hand  MMSE  NAART  disease_duration   group
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb; m=$(grep -n "participant_id  age" out.txt | cut -d: -f1); tail -n +$m out.txt | head -150 | cut -c1-240
```

```
participant_id  age gender hand  MMSE  NAART  disease_duration   group
       sub-hc1   54      f    r    30     48               NaN control
       sub-hc2   50      f    r    30     55               NaN control
       sub-pd3   52      f    r    29     44               9.0      PD
       sub-hc4   50      f    r    30     52               NaN control
       sub-pd5   67      f    r    29     48               2.0      PD
       sub-pd6   62      f    r    30     42               8.0      PD
       sub-hc7   54      f    r    26     48               NaN control
       sub-hc8   71      f    r    29     41               NaN control
       sub-pd9   55      f    r    28     50              12.0      PD
      sub-hc10   59      f    r    29     51               NaN control
      sub-pd12   74      m    r    26     53               1.0      PD
      sub-pd11   71      f    r    30     52               1.0      PD
      sub-pd13   62      m    r    29     47               2.0      PD
      sub-pd14   63      m    r    28     35               2.0      PD
      sub-pd16   74      m    r    29     56               2.0      PD
      sub-pd17   55      m    r    30     40               2.0      PD
      sub-hc18   57      m    r    30     57               NaN control
      sub-pd19   69      f    r    29     43               6.0      PD
      sub-hc20   68      m    r    30     58               NaN control
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb; m=$(grep -n "Beta peaks per recording" out.txt | cut -d: -f1); tail -n +$m out.txt | head -330 | cut -c1-250
```

```
Beta peaks per recording at C3 and C4: 3554 to 6132 (whole recordings, 100-sample edges dropped)
Alpha peaks per recording at C3 and C4: 1679 to 2958
Root task-rest_beh.json: {'trial': {'Description': 'There are no trials, this is just a dummy column so that the necessary sidecar file can be included according to BIDS specification. This will be fixed in future versions.'}}
Questionnaire fields in the beh JSON files: ['Beck', 'Brady kinesia UPDRS', 'H&Y', 'Left UPDRS', 'Rest Tremor UPDRS', 'Right UPDRS', 'Rigidity UPDRS', 'Total UPDRS', 'UPDRS', 'UPDRS 18-26']
 sub ses Beck  UPDRS  Brady kinesia UPDRS  H&Y  Left UPDRS  Rest Tremor UPDRS  Right UPDRS  Rigidity UPDRS  Total UPDRS  UPDRS 18-26
pd11 off    4    NaN                  7.0  2.0         5.0                2.0         10.0             7.0         20.0         19.0
pd11  on    3    NaN                  8.0  2.0         4.0                2.0         10.0             4.0         20.0         17.0
pd12 off   20    NaN                 16.0  3.0        15.0                0.0         15.0            14.0         47.0         35.0
pd12  on   19    NaN                 16.0  3.0        15.0                0.0         15.0            14.0         44.0         35.0
pd13 off    3    NaN                 20.0  2.0        19.0                2.0         22.0            13.0         49.0         40.0
pd13  on   13    NaN                 23.0  3.0        21.0                3.0         23.0            14.0         54.0         46.0
pd14 off    2    NaN                 17.0  2.0        11.0                2.0         21.0            10.0         38.0         35.0
pd14  on    2    NaN                 10.0  2.0        12.0                5.0         17.0             9.0         31.0         30.0
pd16 off    5    NaN                 11.0  2.0        14.0                0.0         11.0            12.0         32.0         28.0
pd16  on    3    NaN                  9.0  2.0        12.0                1.0          8.0            1
[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds002778-jackson-2019; . $TMPDIR/dev/bin/activate; python - <<'EOF'
import pickle, os, numpy as np, pandas as pd
res=pickle.load(open(os.environ['TMPDIR']+'/all.pkl','rb'))
f=res[0]['freqs']
sel=(f>=4)&(f<=32)
rows={}
for r in res:
    k=r['info']['sub']+'-'+r['info']['ses']
    rows[k]=r['psd'].loc[['C3','C4']].values.mean(0)
d=pd.DataFrame(rows,index=np.round(f,1)).T
print(d.loc[:, (d.columns>=3)&(d.columns<=32)].iloc[:, ::2].round(1).to_string())
EOF
```

```
3.4    5.7    8.0   10.2  12.5  14.8  17.1  19.3  21.6  23.9  26.2  28.4  30.7
hc1-hc      3.4    1.0    0.5   0.7   0.9   0.5   0.5   0.6   0.6   0.5   0.5   0.4   0.2
hc10-hc     2.2    1.0    1.0   1.7   1.0   0.9   1.2   1.0   0.7   0.5   0.3   0.2   0.1
hc18-hc     0.9    0.4    1.0   2.2   0.7   0.3   0.3   0.2   0.2   0.1   0.1   0.1   0.1
hc2-hc      2.2    0.9    0.6   0.7   0.4   0.4   0.4   0.4   0.3   0.3   0.2   0.1   0.1
hc20-hc     0.8    0.5    0.3   0.3   0.2   0.1   0.1   0.1   0.1   0.1   0.1   0.1   0.1
hc21-hc     3.1    1.0    1.1   1.6   0.6   0.6   0.6   0.6   0.4   0.3   0.2   0.1   0.1
hc24-hc     2.7    0.8    0.9   0.8   0.3   0.2   0.2   0.2   0.1   0.1   0.1   0.1   0.1
hc25-hc     1.5    0.5    0.3   0.2   0.2   0.2   0.2   0.2   0.3   0.3   0.3   0.3   0.2
hc29-hc     2.7    0.9    1.1   2.3   0.9   0.4   0.5   0.4   0.2   0.2   0.2   0.2   0.1
hc30-hc     3.2    0.7    0.4   0.4   0.2   0.2   0.1   0.1   0.1   0.1   0.1   0.1   0.1
hc31-hc     1.2    0.4    0.4   0.5   0.5   0.5   0.5   0.7   0.6   0.6   0.5   0.5   0.5
hc32-hc     0.8    0.4    0.3   0.3   0.3   0.3   0.6   0.9   0.9   0.8   0.6   0.4   0.2
hc33-hc     0.6    0.2    0.3   0.4   0.2   0.3   0.3   0.4   0.4   0.3   0.3   0.3   0.4
hc4-hc      0.9    0.5    0.4   0.4   0.3   0.3   0.3   0.3   0.3   0.2   0.2   0.2   0.1
hc7-hc      1.7    1.2    2.0   1.6   0.7   0.5   0.5   0.3   0.2   0.2   0.2   0.1   0.1
hc8-hc      0.9    0.4    0.5   0.4   0.3   0.3   0.4   0.5   0.6   0.7   0.5   0.4   0.3
pd11-off    1.1    1.8    2.2   2.5   2.2   1.8   1.4   1.0   0.6   0.3   0.2   0.1   0.1
pd12-off    2.6    6.1    6.8   2.5   0.9   0.8   0.6   0.6   0.4   0.3   0.2   0.2   0.1
pd13-off    0.5    0.3    0.6   0.5   0.3   0.2   0.2   0.1   0.1   0.1   0.1   0.1   0.1
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
date -u
```

```
Tue Oct 27 22:39:09 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb; python - <<'EOF'
s=open('src.py').read()
old=s[s.index("# Every recording is at 512 Hz"):s.index("# %% tags=[\"sanity\"]\n# events.tsv")]
new='''# Every recording is at 512 Hz, lasts 181 to 292 s (the paper says at least 3 min), and has the
# 32 scalp electrodes of the BioSemi 32 layout in the order of the montage, 8 EXG channels and a
# Status channel. No electrode is marked bad. The two sessions that the `notes` column says were
# exported from preprocessed EEGLAB files differ from the rest, and from each other:
#
# - sub-pd6 `on`: electrode means are 0 and the 32 channels sum to 0.048 uV at most, so it
#   already carries the common average reference; it lasts 289 s, against 184 to 216 s for the
#   other `on` sessions. After preprocessing its electrode SDs (5.2 to 26.9 uV) are like the
#   others'.
# - sub-pd16 `on`: electrode means are small (23 uV, against thousands in raw files) but the
#   channels do not sum to zero, and after the same preprocessing its electrode SDs are 11.5 to
#   224 uV (median 62.6), about six times those of any other recording. The spectra below show
#   it with about 100 times the power of the others and no alpha peak. The dataset does not say
#   how this file was preprocessed or scaled.
#
# Both have a high cutoff of 256 Hz in channels.tsv, where the others give 104 Hz. Sharpness,
# steepness and PAC are ratios and do not depend on the signal's scale; group spectra do.
# Results without these two patients are shown as a variant under the main claims.

'''
s=s.replace(old,new)
s=s.replace('''# In all raw files but two''','''# In all raw files but two''')
# fig1c variants
old='''for ses in ["off", "on", "hc"]:
    n_alpha ='''
new='''print("\\nVariants (not the criterion): geometric mean over recordings (mean of log10 power), and the arithmetic mean without sub-pd16 on")
for ses in ["off", "on", "hc"]:
    s_log = 10 ** np.mean([np.log10(spec[k].loc[["C3", "C4"]].values.mean(axis=0)) for k in spec if k[1] == ses], axis=0)
    s_ex = np.mean([spec[k].loc[["C3", "C4"]].values.mean(axis=0) for k in spec if k[1] == ses and k != ("pd16", "on")], axis=0)
    print(f"  {GROUP[ses]}: log mean 8-12 Hz {local_max(s_log, 8, 12)}, 13-30 Hz {local_max(s_log, 13, 30)}; "
          f"without pd16 on 8-12 Hz {local_max(s_ex, 8, 12)}, 13-30 Hz {local_max(s_ex, 13, 30)}; "
          f"local maxima 6-13 Hz of the mean {local_max(group_spectrum(ses, ['C3', 'C4']), 6, 13)}")
for ses in ["off", "on", "hc"]:
    n_alpha ='''
assert old in s
s=s.replace(old,new)
open('src.py','w').write(s)
EOF
cd entries/openneuro-ds002778-jackson-2019; . $TMPDIR/dev/bin/activate; PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/nb/src.py > $TMPDIR/nb/out.txt 2>&1; echo $?; grep -A12 "C3 and C4, off: local" $TMPDIR/nb/out.txt
```

```
0
C3 and C4, off: local maxima 8-12 Hz [], 13-30 Hz []
C3 and C4, on: local maxima 8-12 Hz [], 13-30 Hz []
C3 and C4, control: local maxima 8-12 Hz [10.24], 13-30 Hz [18.2]
all 32 electrodes, off: local maxima 8-12 Hz [], 13-30 Hz [17.07, 21.62]
all 32 electrodes, on: local maxima 8-12 Hz [], 13-30 Hz []
all 32 electrodes, control: local maxima 8-12 Hz [9.1], 13-30 Hz [19.34]
Frequency resolution 1.138 Hz; plotted 0 to 45 Hz

Variants (not the criterion): geometric mean over recordings (mean of log10 power), and the arithmetic mean without sub-pd16 on
  off: log mean 8-12 Hz [9.1], 13-30 Hz []; without pd16 on 8-12 Hz [], 13-30 Hz []; local maxima 6-13 Hz of the mean [7.96]
  on: log mean 8-12 Hz [], 13-30 Hz []; without pd16 on 8-12 Hz [], 13-30 Hz []; local maxima 6-13 Hz of the mean []
  control: log mean 8-12 Hz [9.1], 13-30 Hz [17.07]; without pd16 on 8-12 Hz [10.24], 13-30 Hz [18.2]; local maxima 6-13 Hz of the mean [10.24]
Per recording, off: alpha local max in 8/15, beta local max in 9/15
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb; python - <<'EOF'
s=open('src.py').read()
def rep(old,new,count=1):
    global s
    assert s.count(old)>=1, old[:80]
    s=s.replace(old,new,count)
rep("""# (W = 13, within 12 +/- 1.2; p = 0.0076; FDR corrected p at most 0.012 under every filter
# reading), but d = 0.73 is below the tolerance of 0.86 +/- 0.086. No artifact samples were
# rejected, as the dataset holds no marks.""",
"""# (W = 13, within 12 +/- 1.2; p = 0.0076; FDR corrected p = 0.0228 under every filter
# reading), but d = 0.73 is below the tolerance of 0.86 +/- 0.086. No artifact samples were
# rejected, as the dataset holds no marks. Without pd6 and pd16, W = 11, p = 0.016, d = 0.81.""")
rep("""# (p = 0.0125, FDR corrected at most 0.0161) and d = 0.70 is within 0.68 +/- 0.068, but W = 16
# is outside 9 +/- 0.9.""",
"""# (p = 0.0125, FDR corrected 0.0249) and d = 0.70 is within 0.68 +/- 0.068, but W = 16 is
# outside 9 +/- 0.9. Without pd6 and pd16, W = 5, p = 0.0046, d = 0.75.""")
rep("""# filters and 0.0064 with the code's, FDR corrected at most 0.0161), and d on raw PAC is 0.85
# and 0.86, within 0.83 +/- 0.083 (on log10 PAC 0.73 and 0.86). The signed rank statistic is 13
# and 12, outside 15 +/- 1.5 under both filter readings.""",
"""# filters and 0.0064 with the code's, FDR corrected 0.0228), and d on raw PAC is 0.85 and 0.86,
# within 0.83 +/- 0.083 (on log10 PAC 0.73 and 0.86). The signed rank statistic is 13 and 12,
# outside 15 +/- 1.5 under both filter readings.""")
rep("""# 13 and 12 or 13 of 15 patients), and all three FDR corrected p-values are below 0.05 under
# both PAC filter readings (largest 0.0106). Only steepness ratio is below the paper's bound of
# 0.004 (corrected 0.0045 or 0.0046 against 0.0106 for sharpness and 0.0096 or 0.0081 for PAC).""",
"""# 13 and 12 or 13 of 15 patients), and all three FDR corrected p-values are below 0.05 under
# both PAC filter readings (largest 0.0106). Only steepness ratio is below the paper's bound of
# 0.004 (corrected 0.0044, against 0.0106 for sharpness and 0.0096 or 0.0081 for PAC).""")
rep("""# **Result: see the summary.** The outcome is judged from the printed electrodes: for each
# measure the electrode with the smallest p, and the p at F7, F8, T7 and T8.""",
"""# **Result: partially reproduced.** Steepness ratio meets the criterion: the smallest p is at
# C4 (0.023) and none of F7, F8, T7, T8 is significant. PAC meets it with the Methods' filters
# under the FDR reading (smallest p at CP6, 0.027; F7 has p = 0.041 uncorrected, so not under
# the uncorrected reading), but with the code's filters the smallest p is at Fz (0.020).
# Sharpness ratio does not: its smallest p is at P8 (0.0064), then CP6 and AF3. No electrode
# survives FDR correction over the 32 for any measure.""")
rep("""# **Result: reproduced.** With the average reference steepness ratio is higher off than in
# controls, z = 2.37 (within 2.53 +/- 0.253), p = 0.018, FDR corrected 0.053 to 0.106 over Table
# 2 depending on the filter readings, d = 0.85 (within 0.88 +/- 0.088). See the summary for how
# the FDR result bears on the outcome. With the bipolar pairs z = 2.37, p = 0.018 as a single
# test, and 0.053 FDR corrected over the three bipolar measures.""",
"""# **Result: partially reproduced.** With the average reference steepness ratio is higher off
# than in controls with z = 2.37 (within 2.53 +/- 0.253) and d = 0.85 (within 0.88 +/- 0.088),
# p = 0.018 uncorrected, but FDR corrected over the six tests of Table 2 p = 0.0531, just above
# 0.05, under every filter reading. With the bipolar pairs z = 2.37, p = 0.018 as a single test
# (significant) and 0.0531 FDR corrected over the three bipolar measures. The criterion does not
# name this case (bipolar holds, average reference corrected test does not); the effect is
# present with the paper's size but misses the corrected threshold.""")
rep("""# **Result: see the summary.** The statistic and p are printed above for both fields.""",
"""# **Result: reproduced.** "Total UPDRS", the only total in the dataset and by its values the
# motor examination, is lower on medication in 12 patients, equal in 2 and higher in 1:
# W = 3.5, p = 0.0033, the paper's values. Items 18 to 26 alone give W = 6.5, p = 0.011.""")
rep("""# **Result: see the summary.** The local maxima of each group's spectrum are printed above.""",
"""# **Result: not reproduced.** In the average C3 and C4 spectrum only the controls have a local
# maximum between 8 and 12 Hz (10.24 Hz) and between 13 and 30 Hz (18.2 Hz). The off group's
# mean spectrum peaks at 7.96 Hz, just below the band, and the on group's has no peak from 6 to
# 30 Hz; the on mean is dominated by sub-pd16 `on`, but without it there is still none. Over all
# electrodes the off group has beta maxima (17.1 and 21.6 Hz) and still no alpha maximum. Single
# recordings have an alpha maximum in 8 of 15 (off), 8 of 15 (on) and 11 of 16 (controls). The
# paper's spectra were computed after artifact rejection, which is not possible here.""")
rep("""# **Result: partially reproduced.** Both alpha measures are higher off than on with FDR corrected
# p below 0.05 under both shape filter readings (largest 0.0317).""",
"""# **Result: partially reproduced.** Both alpha measures are higher off than on with FDR corrected
# p below 0.05 under both shape filter readings (largest 0.0321).""")
rep("""# **Result: see the summary.** The readings differ: the corrected p is printed for each.""",
"""# **Result: reproduced, resting on an assumption.** With the 192-tap phase filter (reading a)
# alpha PAC does not differ after correction (W = 27, corrected p = 0.0609, d = 0.70), nor with
# the code's 231/240 taps (reading b, corrected p = 0.0783); with the Methods' beta filter length
# of 118 samples (reading c) it does (W = 23, corrected p = 0.0356). Reading a, pacpy's default
# of three cycles of the low cutoff, is adopted as the assumption (see the summary). d is 0.70,
# 0.72 and 0.66, outside 0.51 +/- 0.051 under every reading; the claim of absence is judged on
# the test.""")
rep("""# **Result: see the summary.** z, d and the corrected p are printed for each reading.""",
"""# **Result: partially reproduced.** Alpha steepness ratio is higher off than in controls with
# z = 2.45 (192 taps) or 2.53 (118 samples), within 2.53 +/- 0.253, and d = 0.89, within
# 0.87 +/- 0.087, but its FDR corrected p is 0.0531 under every reading, just above 0.05.
# Sharpness ratio (corrected p 0.57 or 0.72) and PAC (0.12 to 0.41) do not differ after
# correction, as stated.""")
rep("""# **Result: see the summary.** Every filter reading and both scales are printed above.""",
"""# **Result: partially reproduced.** On raw PAC (the main reading) the beta off-on difference is
# larger than the alpha one in 12 or 13 of 15 patients, p = 0.015 to 0.017 under every filter
# reading, but W = 17 or 18 is outside 11 +/- 1.1. On log10 PAC (variant) there is no
# difference (p = 0.26 to 0.73).""")
rep("""# **Result: see the summary.** The correlations are printed above for both PAC filter readings.

# %% tags=["claim:fig3-steepness-pac-correlation"]""",
"""# **Result: partially reproduced.** Sharpness ratio and PAC are positively and significantly
# correlated off and on under both PAC filter readings (r = 0.59 to 0.84, p = 0.0001 to
# 0.022). No reading has both r within tolerance: with the Methods' filters r = 0.59 off is
# below 0.63 to 0.77 (on 0.79, within); with the code's, r = 0.84 on is above 0.666 to 0.814
# (off 0.63, within).

# %% tags=["claim:fig3-steepness-pac-correlation"]""")
rep("""# **Result: see the summary.** The correlations are printed above for both PAC filter readings.

# %% [markdown]
# ## fig4a""",
"""# **Result: partially reproduced.** Off medication steepness ratio and PAC are correlated as
# reported (r = 0.80, p = 0.0003 with the Methods' filters; 0.80, p = 0.0004 with the code's).
# On medication the correlation is weaker: r = 0.45, p = 0.095 with the Methods' filters, and
# r = 0.53, p = 0.041 with the code's, below 0.612 to 0.748.

# %% [markdown]
# ## fig4a""")
rep("""# **Result: see the summary.** The quadrant counts are printed above.

# %% [markdown]
# ## q4-patient-counts""",
"""# **Result: reproduced.** 48 of the 60 patient points at C3 and C4 (80%) are in Q4; Q1 holds 6,
# Q2 4 and Q3 2.

# %% [markdown]
# ## q4-patient-counts""")
rep("""# **Result: see the summary.** The four counts are printed above.""",
"""# **Result: not reproduced.** 10 patients have both off and on in Q4 at C3 and 10 at C4
# (expected 9 and 8 +/- 1), 7 at both (expected 8 +/- 1) and 13 at one or more (expected
# 9 +/- 1). The C4 count and the count of patients with at least one electrode are outside
# tolerance in either electrode order.""")
rep("""# **Result: see the summary.** Both readings are printed above.""",
"""# **Result: reproduced.** Both readings agree: at F7 and F8 the most common quadrant holds 68%
# of the points (41 of 60, in Q2) against 80% (48 of 60, Q4) at C3 and C4, and the RMS distance
# to the centroid is 0.093 against 0.076. The F7/F8 points are mostly in one other quadrant,
# Q2 (sharper troughs, steeper rises), which reads as a different dominant shape more than an
# absence of one.""")
rep("""# **Result: see the summary.** The quadrant counts are printed above.

# %% [markdown]
# ## table3""",
"""# **Result: reproduced.** 25 of the 32 control points (78%) are in Q4 (13 of 16 at C3, 12 of 16
# at C4).

# %% [markdown]
# ## table3""")
rep("""# **Result: see the summary.** The effect sizes are printed above.""",
"""# **Result: partially reproduced.** Restricting to the 13 patients with at least one electrode
# in Q4 off and on raises d for all three measures under every reading (sharpness 0.73 to 0.99,
# steepness 0.70 to 0.82, raw PAC 0.85 to 0.95 with the Methods' filters). Sharpness d (0.99) is
# within 0.95 +/- 0.095; steepness (0.82) and PAC (0.95 to 1.07 across readings) are above
# tolerance. The paper's 9 Q4 patients are 13 here (q4-patient-counts). The all-patient PAC d of
# Table 3 (0.75) matches log10 PAC with the Methods' filters (0.73), as the claims file
# suggests.""")
open('src.py','w').write(s)
print(s.count('see the summary'))
EOF
```

```
1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n -B3 -A3 "see the summary" $TMPDIR/nb/src.py
```

```
687-# alpha PAC does not differ after correction (W = 27, corrected p = 0.0609, d = 0.70), nor with
688-# the code's 231/240 taps (reading b, corrected p = 0.0783); with the Methods' beta filter length
689-# of 118 samples (reading c) it does (W = 23, corrected p = 0.0356). Reading a, pacpy's default
690:# of three cycles of the low cutoff, is adopted as the assumption (see the summary). d is 0.70,
691-# 0.72 and 0.66, outside 0.51 +/- 0.051 under every reading; the claim of absence is judged on
692-# the test.
693-
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/nb/src.py <<'EOF'
#
# | Claim | Outcome |
# |---|---|
# | fig2-sharpness-off-on | partially reproduced (W 13 matches, d 0.73 below 0.86) |
# | fig2-steepness-off-on | partially reproduced (d 0.70 matches, W 16 against 9) |
# | fig2-pac-off-on | partially reproduced (d 0.85 matches, W 13 against 15) |
# | bipolar-off-on | reproduced |
# | temporalis-f7f8-null | reproduced |
# | temporalis-t7t8-null | reproduced |
# | fig2c-topography-sensorimotor | partially reproduced (steepness and PAC, not sharpness) |
# | offctrl-sharpness-null | reproduced |
# | offctrl-steepness | partially reproduced (z and d match, FDR p 0.053) |
# | offctrl-pac-null | reproduced |
# | offctrl-pac-csd | not reproduced (p 0.075) |
# | updrs-improvement | reproduced (W 3.5, p 0.0033) |
# | fig1c-beta-alpha-peaks | not reproduced (only controls have both peaks) |
# | table1-alpha-shape-off-on | partially reproduced (steepness W 21 against 12) |
# | table1-alpha-pac-null | reproduced, resting on an assumption (alpha phase filter of 192 taps) |
# | table2-alpha-offctrl | partially reproduced (steepness z and d match, FDR p 0.053) |
# | pac-beta-larger-than-alpha | partially reproduced (p 0.015, W 17 against 11) |
# | fig3-sharpness-pac-correlation | partially reproduced (one r out of tolerance) |
# | fig3-steepness-pac-correlation | partially reproduced (on medication r 0.45 to 0.53) |
# | fig4a-sensorimotor-q4 | reproduced (80% in Q4) |
# | q4-patient-counts | not reproduced (13 patients against 9) |
# | fig4b-temporalis-variable-shape | reproduced |
# | controls-q4 | reproduced (78% in Q4) |
# | table3-q4-effect-size | partially reproduced (d rises for all three; two values above tolerance) |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# **How the analysis differs from the paper's.** The dataset holds neither the paper's manual
# artifact marks nor its list of excluded electrodes, so no sample is rejected and all 32 scalp
# electrodes enter the common average (readings (b) of the claims file). The paper's measures
# were taken on its preprocessed MATLAB files, which are not public. Filter lengths the paper
# leaves open are run under each reading the claims file names. The CSD uses MNE's spherical
# spline with the CSD toolbox's parameters on template electrode positions.
#
# **Assumption.** For alpha PAC the phase filter length is not given. The readings disagree on
# table1-alpha-pac-null; the 192-tap filter (three cycles of 8 Hz) is adopted, as the default of
# pacpy, the package the Methods name for PAC, and the rule the paper's code uses for its shape
# filters. Two of the three readings give the same outcome.
#
# **What was found about the dataset.** It holds the 15 patients (8 female, mean age 63.3) and 16
# controls (9 female, 63.5) the paper describes, each recording once, with UPDRS scores that
# give the paper's UPDRS test exactly (W = 3.5, p = 0.0033). The artifact marks and excluded
# electrodes of the paper's preprocessing are not in it. Two `on` sessions (sub-pd6, sub-pd16)
# were exported from preprocessed EEGLAB files; sub-pd16 `on` has about six times the amplitude
# of any other recording and no alpha peak, and the dataset does not say how it was processed.
# The UPDRS fields carry no description. Without artifact rejection the main off against on
# results hold, with statistics close to the paper's.
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/convert.py <<'EOF'
import re, sys, nbformat
src = open(sys.argv[1]).read()
cells = []
blocks = re.split(r"^# %%(.*)$", src, flags=re.M)
# blocks: [pre, header1, body1, header2, body2, ...]
for header, body in zip(blocks[1::2], blocks[2::2]):
    body = body.strip("\n")
    tags = re.findall(r'tags=\[(.*?)\]', header)
    tags = [t.strip().strip('"') for t in tags[0].split(",")] if tags else []
    if "[markdown]" in header:
        text = "\n".join(l[2:] if l.startswith("# ") else l[1:] if l.startswith("#") else l for l in body.split("\n"))
        c = nbformat.v4.new_markdown_cell(text)
    else:
        c = nbformat.v4.new_code_cell(body)
    if tags:
        c.metadata["tags"] = tags
    cells.append(c)
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, sys.argv[2])
print(len(cells), "cells")
EOF
cd  python3 -c "import nbformat" 2>/dev/null || . $TMPDIR/dev/bin/activate; . $TMPDIR/dev/bin/activate; uv pip install -q nbformat jsonschema 2>&1|tail -1; python $TMPDIR/nb/convert.py $TMPDIR/nb/src.py entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb; python -c "
import nbformat; nb=nbformat.read('entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb',4)
for c in nb.cells[:4]: print(c.cell_type, c.metadata, c.source[:200]); print('--')
print([c.metadata.get('tags') for c in nb.cells if c.metadata.get('tags')])"
```

```
85 cells
markdown {} # Reproducing Jackson, Cole, Voytek & Swann (2019) from OpenNeuro ds002778

**Paper.** Jackson N, Cole SR, Voytek B, Swann NC (2019). Characteristics of waveform shape in
Parkinson's disease detected 
--
code {} import itertools
import time
import warnings
from concurrent.futures import ThreadPoolExecutor

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

import w
--
markdown {} ## Data check
--
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds002778-jackson-2019; cat > requirements.in <<'EOF'
matplotlib
mne
numpy
pandas
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: openneuro-ds002778-jackson-2019
type: reproduction
title: Beta waveform shape in Parkinson's disease scalp EEG (Jackson et al. 2019)
description: Tests the findings of Jackson, Cole, Voytek and Swann (2019) on OpenNeuro ds002778,
  which holds the resting EEG of 15 patients with Parkinson's disease off and on medication and 16
  controls. It computes beta and alpha sharpness ratio, steepness ratio and phase-amplitude coupling
  over sensorimotor and temporal electrodes, compares medication states and groups, and classifies
  waveform shape by peak-to-trough and rise-to-fall ratios. The paper's manual artifact marks are
  not in the dataset, so no samples are rejected.
license: Apache-2.0
notebooks:
- path: reproduce_jackson_2019.ipynb
  title: Reproducing Jackson et al. (2019) from OpenNeuro ds002778
  runtime_minutes: 3
helpers:
- waveshape.py
related:
- id: openneuro:ds002778/1.0.5
  relation: uses_data
- id: doi:10.1523/eneuro.0151-19.2019
  relation: reproduces
EOF
cd ../..; . $TMPDIR/dev/bin/activate; python tools/entry.py lock entries/openneuro-ds002778-jackson-2019 2>&1 | tail -3; date -u
```

```
wrote entries/openneuro-ds002778-jackson-2019/requirements.lock.txt
Tue Oct 27 22:42:01 UTC 2026
```

**Agent calls Bash**

```bash
cd  grep -rn "openneuro:" tools/*.py | head -10
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  grep -rn -i "openneuro" tools/entry.py tools/datasets.py tools/build_site.py | head -15; grep -rn "uses_data" tools/*.py | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  ls tools/archives; grep -rln -i "openneuro" tools | head; grep -rn "relation\b\|\"related\"\|'related'" tools/*.py tools/archives/*.py | head
```

```
__init__.py
__pycache__
crcns.py
dandi.py
dryad.py
ebrains.py
figshare.py
local.py
openneuro.py
remote.py
tools/build_openneuro_targets.py
tools/archives/openneuro.py
tools/archives/__pycache__/openneuro.cpython-313.pyc
tools/archives/__pycache__/openneuro.cpython-314.pyc
tools/build_dryad_targets.py:64:               "relation": w["relationship"], "resource_type": "JournalArticle" if w["relationship"] ==
tools/build_figshare_targets.py:75:    dois = ([paper] if paper else []) + [r["identifier"].lower() for r in related if r["relation"] in PAPER_RELATIONS]
tools/build_figshare_targets.py:77:    papers = [{"doi": d, "title": title_of(d), "relation": "given" if d == paper else
tools/build_figshare_targets.py:78:               next((r["relation"] for r in related if r["identifier"].lower() == d), "resource_doi"),
tools/build_openneuro_targets.py:144:        papers.append({"doi": d, "title": title_of(d), "relation": "given" if d == paper and d not in found else
tools/build_site.py:279:        related = entry.get("related", [])
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|prefix\|relation\|uses_data\|:%s\|f\"openneuro" tools/archives/openneuro.py | head -30; grep -n "uses_data\|data_id\|def entry_dataset" tools/archives/__init__.py | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  wc -l tools/archives/openneuro.py tools/archives/__init__.py; grep -n "openneuro\|OPENNEURO" tools/archives/*.py | head -20
```

```
24 tools/archives/openneuro.py
  57 tools/archives/__init__.py
  81 total
tools/archives/openneuro.py:1:"""OpenNeuro (openneuro.org), BIDS datasets of human neuroimaging and electrophysiology: docs/archives.md, "OpenNeuro".
tools/archives/openneuro.py:3:A dataset is named by its accession number (OPENNEURO:ds002778, folder openneuro-ds002778) and pinned by a
tools/archives/openneuro.py:4:snapshot's tag (published_version, 1.0.5), each with its own DOI (10.18112/openneuro.<id>.v<tag>). Metadata and
tools/archives/openneuro.py:6:object version in the openneuro.org bucket, or a git object on openneuro.org), so agents read them directly: no
tools/archives/openneuro.py:13:    key="openneuro", label="OPENNEURO", name="OpenNeuro", url="https://openneuro.org/datasets/{id}",
tools/archives/openneuro.py:15:            "says under \"OpenNeuro\": list them by POSTing to https://openneuro.org/crn/graphql the query "
tools/archives/openneuro.py:22:    list="openneuro.json", builder="tools/build_openneuro_targets.py",
tools/archives/openneuro.py:23:    hosts=("openneuro.org", "*.openneuro.org", "*.amazonaws.com"),
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/dev/bin/activate; time python tools/entry.py all entries/openneuro-ds002778-jackson-2019 2>&1 | tail -15
```

```
Installed kernelspec registry-openneuro-ds002778-jackson-2019 in executed/openneuro-ds002778-jackson-2019/.venv/share/jupyter/kernels/registry-openneuro-ds002778-jackson-2019
0 error(s)
pass  reproduce_jackson_2019.ipynb  (97 s)

real	2m1.230s
user	3m33.158s
sys	0m7.054s
```

**Agent calls Bash**

```bash
cd  ls executed/openneuro-ds002778-jackson-2019/; . $TMPDIR/dev/bin/activate; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb',4)
txt=''
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.outputs:
            if o.get('output_type')=='stream': txt+=o['text']
            elif 'data' in o and 'text/plain' in o['data']: txt+=o['data']['text/plain']+'\n'
            elif o.get('output_type')=='error': txt+='ERROR '+o['ename']
open('/tmp/claude-1001/nb/exec.txt','w').write(txt)
EOF
cd $TMPDIR/nb; diff <(grep -v "analysed in" out.txt) <(grep -v "analysed in" exec.txt) | head; echo diff-done
```

```
reproduce_jackson_2019.ipynb
result.json
483a484
> <Figure size 400x400 with 1 Axes>
537a539
> <Figure size 1200x300 with 3 Axes>
586a589
> <Figure size 1000x350 with 2 Axes>
652a656
> <Figure size 800x350 with 2 Axes>
694a699
> <Figure size 900x400 with 2 Axes>
diff-done
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
def show(o,ind=0,depth=0):
    if depth>4: return
    if isinstance(o,dict):
        if 'properties' in o:
            req=o.get('required',[])
            for k,v in o['properties'].items():
                print(' '*ind+k+('*' if k in req else '')+' '+str(v.get('type',''))+' '+str(v.get('enum',''))[:150]+' '+str(v.get('pattern',''))[:80])
                show(v,ind+2,depth+1)
        if 'items' in o: show(o['items'],ind,depth+1)
        for k in ('$defs','definitions'):
            if k in o:
                for n,v in o[k].items(): print(' '*ind+'DEF '+n); show(v,ind+2,depth+1)
show(s)
EOF
```

```
schema_version*   
id* string  ^[a-z0-9]+(-[a-z0-9]+)*$
dataset* object  
  archive* string  ^[a-z][a-z0-9-]*$
  id* string  
  version* string  
  modified string  
  doi string  ^10\.[0-9]{4,9}/.+$
paper* string  ^doi:10\.[0-9]{4,9}/.+$
date* string  
entry string  
deprecated object  
  date* string  
  reason* string  
  superseded_by string  
provenance* object  
  kind*  ['agent', 'person'] 
  accountable* object  
    name* string  
    orcid string  ^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$
[... 55 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/openneuro-ds002778-jackson-2019-01.yaml",
 "content": "schema_version: 2\nid: openneuro-ds002778-jackson-2019-01\ndataset:\n  archive: openneuro\n  id: ds002778\n  version: 1.0.5\n  doi: 10.18112/openneuro.ds002778.v1.0.5\npaper: doi:10.1523/eneuro.0151-19.2019\ndate: 2026-10-27\nentry: openneuro-ds002778-jackson-2019\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-12\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/40594416398\noutcomes:\n- claim: fig2-sharpness-off-on\n  outcome: partially_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:fig2-sharpness-off-on\n  measured:\n  - 13\n  - 0.73\n  notes: Composite C3 and C4 beta sharpness ratio is higher off than on in 13 of 15 patients,\n    signed rank W = 13 (expected 12 +/- 1.2), p = 0.0076 (exact 0.0054), FDR corrected over the\n    six tests of Table 1 p = 0.0228 under all 12 combinations of filter readings. Cohen's d =\n    0.73, below 0.86 +/- 0.086. Without sub-pd6 and sub-pd16, whose on sessions come from\n    preprocessed files, W = 11, p = 0.016, d = 0.81.\n  deviations:\n  - No samples rejected and no electrode excluded, as the dataset holds neither the paper's\n    manual artifact marks nor its excluded electrodes (claims file readings (b); reading (a), the\n    dataset's own marks, has nothing to apply since every channels.tsv says good and the events\n    files hold only a start trigger).\n  - The paper computed its measures on preprocessed MATLAB files that are not public; here the\n    preprocessing of the Methods is applied to the BDF files.\n- claim: fig2-steepness-off-on\n  outcome: partially_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:fig2-steepness-off-on\n  measured:\n  - 16\n  - 0.70\n  notes: Beta steepness ratio is higher off than on in 12 of 15 patients, p = 0.0125 (exact\n    0.0103), FDR corrected 0.0249; d = 0.70 is within 0.68 +/- 0.068 but W = 16 is outside 9 +/-\n    0.9. Without sub-pd6 and sub-pd16, W = 5, p = 0.0046, d = 0.75.\n  deviations:\n  - No artifact rejection or electrode exclusion (as for fig2-sharpness-off-on).\n- claim: fig2-pac-off-on\n  outcome: partially_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:fig2-pac-off-on\n  measured:\n  - 13\n  - 0.85\n  notes: Beta PAC is higher off than on in 13 of 15 patients; W = 13, p = 0.0076 with the\n    Methods' filters (118 and 123 samples) and W = 12, p = 0.0064 with the code's (231 and 240\n    taps); FDR corrected 0.0228. d on raw PAC is 0.85 and 0.86, within 0.83 +/- 0.083; on log10\n    PAC 0.73 and 0.86. The statistic is outside 15 +/- 1.5 under both filter readings. The\n    criterion's last sentence names only the test and d; taken alone it would make the claim\n    reproduced, but the statistic is an expected value of the claim and is out of tolerance, so\n    the outcome is partially reproduced.\n  deviations:\n  - No artifact rejection or electrode exclusion (as for fig2-sharpness-off-on).\n  - The criterion combines \"As for fig2-sharpness-off-on\" (statistic and d within tolerance) with\n    a last sentence naming the test and d only; the expected statistic was kept as part of the\n    judgement.\n- claim: bipolar-off-on\n  outcome: reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:bipolar-off-on\n  notes: With C3-CP1 and C4-CP2, off is higher than on for sharpness ratio (W = 15, p = 0.0106,\n    13 of 15), steepness ratio (W = 4, p = 0.0015, 13 of 15) and PAC (W = 12, p = 0.0064 Methods'\n    filters; W = 11, p = 0.0054 code's). FDR corrected over the three, 0.0106, 0.0044 and 0.0096\n    (0.0081), all below 0.05. Only steepness is below the paper's bound of 0.004 (0.0044 is just\n    above it); sharpness and PAC are not.\n  deviations:\n  - No artifact rejection or electrode exclusion (as for fig2-sharpness-off-on).\n- claim: temporalis-f7f8-null\n  outcome: reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:temporalis-f7f8-null\n  notes: At the F7 and F8 composite, sharpness ratio p = 0.69 (d 0.31), steepness ratio p = 0.17\n    (d 0.57), PAC p = 0.0995 (Methods' filters) and 0.078 (code's), d 0.67; none below 0.05\n    uncorrected. Paper p = 0.73, 0.394 and 0.191.\n  deviations:\n  - No artifact rejection or electrode exclusion. The paper's argument is that these electrodes\n    carry muscle artifact; here artifacts were not removed at any electrode.\n- claim: temporalis-t7t8-null\n  outcome: reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:temporalis-t7t8-null\n  notes: At the T7 and T8 composite, sharpness ratio p = 0.36 (d 0.42), steepness ratio p = 0.95\n    (d -0.04), PAC p = 0.11 under both filter readings (d 0.56 and 0.59).\n  deviations:\n  - No artifact rejection or electrode exclusion.\n- claim: fig2c-topography-sensorimotor\n  outcome: partially_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:fig2c-topography-sensorimotor\n  notes: Signed rank tests at each of the 32 electrodes. Steepness ratio meets the criterion\n    (smallest p at C4, 0.023; F7, F8, T7, T8 p 0.21 to 0.57). PAC with the Methods' filters has\n    its smallest p at CP6 (0.027), and F7 has p = 0.041, so it meets the criterion under the FDR\n    reading only; with the code's filters the smallest p is at Fz (0.020). Sharpness ratio has\n    its smallest p at P8 (0.0064), then CP6 (0.017) and AF3 (0.031); C3 is fourth (0.0995). No\n    electrode survives FDR over 32 for any measure. Two of three measures meet the criterion\n    under one reading, one does not under any.\n  deviations:\n  - No artifact rejection or electrode exclusion.\n  - The paper's topographies were drawn with EEGLAB topoplot from test statistics; here the test\n    at each electrode is listed and plotted as -log10 p, as the criterion uses only the tests.\n- claim: offctrl-sharpness-null\n  outcome: reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:offctrl-sharpness-null\n  measured:\n  - 0.09\n  notes: Rank sum z = 0.47, p = 0.64 (paper z = 0.91, p = 0.363); no difference. d = 0.09 is\n    outside the expected 0.19 +/- 0.019; the claim of absence is judged on the test.\n  deviations:\n  - No artifact rejection or electrode exclusion.\n- claim: offctrl-steepness\n  outcome: partially_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:offctrl-steepness\n  measured:\n  - 2.37\n  - 0.85\n  notes: With the average reference, beta steepness ratio is higher off than in controls, z =\n    2.37 (within 2.53 +/- 0.253), d = 0.85 (within 0.88 +/- 0.088), p = 0.0177 uncorrected, but\n    FDR corrected over the six tests of Table 2 p = 0.0531 under every filter reading, just\n    above 0.05 (the alpha steepness test has p = 0.0143, so the two smallest of six give 0.0531).\n    With the bipolar pairs z = 2.37, p = 0.0177 as a single test (significant), 0.0531 FDR\n    corrected over the three bipolar measures. The criterion names reproduced (average reference\n    corrected test holds, z and d match, bipolar holds) and partially reproduced (only the\n    average reference result holds); here the bipolar result holds under one reading and the\n    average reference test misses the corrected threshold with z and d matching, which is\n    recorded as partially reproduced.\n  deviations:\n  - No artifact rejection or electrode exclusion.\n  - The case found is not one the criterion names; the outcome was judged as an effect present\n    with the paper's size that misses the corrected threshold.\n- claim: offctrl-pac-null\n  outcome: reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:offctrl-pac-null\n  notes: Rank sum z = 0.99, p = 0.32 with the Methods' filters; z = 1.07, p = 0.29 with the code's\n    (paper z = 1.19, p = 0.236). d = 0.20.\n  deviations:\n  - No artifact rejection or electrode exclusion.\n- claim: offctrl-pac-csd\n  outcome: not_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:offctrl-pac-csd\n  notes: With the CSD transform, beta PAC at C3 and C4 is higher off (0.032) than in controls\n    (0.025), z = 1.78, p = 0.075 under both filter readings, d = 0.35, against the paper's p =\n    0.022. The CSD montage increases the off against on difference (d = 1.20, p = 0.0106).\n  deviations:\n  - CSD computed with MNE's spherical spline (stiffness m = 3, lambda 1e-5, 50 Legendre terms, the\n    CSD toolbox's defaults) on the BioSemi 32 template positions, as the dataset holds no\n    digitized positions; the paper used the MATLAB CSD toolbox (Methods, Data preprocessing).\n  - No artifact rejection or electrode exclusion.\n- claim: updrs-improvement\n  outcome: reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:updrs-improvement\n  measured: 3.5\n  notes: The dataset's \"Total UPDRS\" (16 to 58; it exceeds \"UPDRS 18-26\" by 1 to 14, which fits\n    the motor examination, items 18 to 31) is lower on medication in 12 patients, equal in 2,\n    higher in 1. Signed rank W = 3.5, p = 0.0033 (scipy's default drops the two ties), the\n    paper's values. The dataset holds no other part of the UPDRS, so both readings of the\n    criterion give this field. Items 18 to 26 alone give W = 6.5, p = 0.011.\n  deviations:\n  - The UPDRS fields have no description in the dataset; \"Total UPDRS\" is taken as the motor\n    total from its values.\n- claim: fig1c-beta-alpha-peaks\n  outcome: not_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:fig1c-beta-alpha-peaks\n  notes: Welch spectra (Hamming 256, overlap 128, nFFT 450) averaged over C3 and C4 and over the\n    participants of each group. Controls have local maxima at 10.24 Hz and 18.2 Hz. The off\n    group's mean spectrum has its only maximum from 6 to 13 Hz at 7.96 Hz, below the 8 to 12 Hz\n    band, and none from 13 to 30 Hz; the on group's has none. Over all electrodes off has beta\n    maxima at 17.1 and 21.6 Hz and no alpha maximum. The on mean is dominated by sub-pd16 on\n    (about 100 times the power of others), but without it there is still no maximum. With the\n    mean of log power, off has an alpha maximum at 9.1 Hz and no beta maximum. Single recordings\n    have an alpha maximum in 8 of 15 off, 8 of 15 on and 11 of 16 controls, and a beta maximum\n    in 9, 10 and 14.\n  deviations:\n  - Spectra computed without artifact rejection; artifacts weigh on a mean of raw power more\n    than on the ratio measures.\n- claim: table1-alpha-shape-off-on\n  outcome: partially_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:table1-alpha-shape-off-on\n  measured:\n  - 18\n  - 0.71\n  - 21\n  - 0.58\n  notes: With the 192-tap filter, alpha sharpness ratio W = 18, p = 0.0171, d = 0.71 (11 of 15\n    higher off) and alpha steepness ratio W = 21, p = 0.0268, d = 0.58 (12 of 15); with 118\n    samples, W = 19, d = 0.66 and W = 21, d = 0.59. FDR corrected p 0.0256 to 0.0321. Both\n    tests hold and three of four values are within tolerance under both readings; the steepness\n    statistic (21) is outside 12 +/- 1.2.\n  deviations:\n  - No artifact rejection or electrode exclusion.\n- claim: table1-alpha-pac-null\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:table1-alpha-pac-null\n  measured: 0.70\n  notes: FDR corrected over Table 1, alpha PAC off against on gives p = 0.0609 with a 192-tap\n    phase filter (reading a, W = 27), 0.0783 with the code's 231 and 240 taps (reading b, W =\n    29), and 0.0356 with 118 samples (reading c, W = 23). Readings a and b find no difference,\n    reading c does. Reading a is adopted (see deviations). d on raw PAC is 0.70, 0.72 and 0.66,\n    above 0.51 +/- 0.051 under every reading; on log10 PAC 0.84, 0.82, 0.70. The question of the\n    alpha phase filter length is for the paper's authors: the Methods give 231 ms for the beta\n    filter only, and the code holds no alpha analysis.\n  deviations:\n  - Assumed the alpha phase filter is 192 taps, three cycles of 8 Hz, the default filter length\n    of pacpy, the package the Methods name for PAC (\"with the open-source package, pacpy\"), and\n    the rule of the paper's code for its shape filters (shape.findpt, w = 3). The readings give\n    different outcomes; all three are printed.\n  - No artifact rejection or electrode exclusion.\n- claim: table2-alpha-offctrl\n  outcome: partially_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:table2-alpha-offctrl\n  measured:\n  - 2.45\n  - 0.89\n  notes: Alpha steepness ratio, off against controls, z = 2.45 (192 taps) or 2.53 (118 samples),\n    within 2.53 +/- 0.253, d = 0.89, within 0.87 +/- 0.087, p = 0.0143 or 0.0114 uncorrected, FDR\n    corrected 0.0531 under every reading, just above 0.05. Sharpness ratio (corrected 0.57 or\n    0.72) and PAC (0.12 to 0.41) do not differ after correction, as the claim says. The criterion\n    does not name this case (steepness values match but miss the corrected threshold; the other\n    two hold); it is recorded as partially reproduced.\n  deviations:\n  - No artifact rejection or electrode exclusion.\n  - The case found is not one the criterion names.\n- claim: pac-beta-larger-than-alpha\n  outcome: partially_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:pac-beta-larger-than-alpha\n  measured: 17\n  notes: On raw PAC the beta off minus on difference exceeds the alpha one in 12 or 13 of 15\n    patients, W = 17 (18 for the code's beta filters with reading c), p = 0.015 to 0.017, under\n    all six combinations of filter readings. W is outside 11 +/- 1.1. On log10 PAC (variant) W =\n    40 to 54, p = 0.26 to 0.73.\n  deviations:\n  - No artifact rejection or electrode exclusion.\n- claim: fig3-sharpness-pac-correlation\n  outcome: partially_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:fig3-sharpness-pac-correlation\n  measured:\n  - 0.59\n  - 0.79\n  notes: Spearman r between composite beta sharpness ratio and PAC, Methods' filters, off 0.59\n    (p = 0.022, below 0.63 to 0.77) and on 0.79 (p = 0.0005, within); code's filters off 0.63\n    (p = 0.012, within) and on 0.84 (p = 0.0001, above 0.666 to 0.814). Both positive and\n    significant under both readings, with one r out of tolerance in each.\n  deviations:\n  - No artifact rejection or electrode exclusion.\n- claim: fig3-steepness-pac-correlation\n  outcome: partially_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:fig3-steepness-pac-correlation\n  measured:\n  - 0.80\n  - 0.45\n  notes: Methods' filters, off r = 0.80 (p = 0.0003, within 0.666 to 0.814), on r = 0.45 (p =\n    0.095, not significant); code's filters, off r = 0.80 (p = 0.0004), on r = 0.53 (p = 0.041,\n    below 0.612 to 0.748). Under the code's filters both are positive and significant with one r\n    out of tolerance.\n  deviations:\n  - No artifact rejection or electrode exclusion.\n- claim: fig4a-sensorimotor-q4\n  outcome: reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:fig4a-sensorimotor-q4\n  measured: 48\n  notes: Of the 60 patient points (C3 and C4, off and on), 48 (80%) have positive log10\n    peak-to-trough and negative log10 rise-to-fall ratio (Q4); Q1 6, Q2 4, Q3 2. Q4 holds 13, 10,\n    13 and 12 of the 15 points at C3 off, C3 on, C4 off and C4 on.\n  deviations:\n  - No artifact rejection or electrode exclusion.\n- claim: q4-patient-counts\n  outcome: not_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:q4-patient-counts\n  measured:\n  - 10\n  - 10\n  - 7\n  - 13\n  notes: Patients with both off and on in Q4 are 10 at C3, 10 at C4, 7 at both and 13 at one or\n    more, against 9, 8, 8 and 9 (+/- 1). The C3 and both counts are within tolerance, the C4\n    count and the at-least-one count are not, in either electrode order (swapped, C3 10 against\n    8).\n  deviations:\n  - No artifact rejection or electrode exclusion; the selection depends on the shape measures,\n    which the paper computed after rejection.\n- claim: fig4b-temporalis-variable-shape\n  outcome: reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:fig4b-temporalis-variable-shape\n  notes: Reading (a), the most common quadrant holds 68% of the 60 F7 and F8 points (41, Q2)\n    against 80% (48, Q4) at C3 and C4; reading (b), RMS distance to the centroid 0.093 against\n    0.076. Both readings agree. The F7 and F8 points concentrate in Q2 (sharper troughs, steeper\n    rises).\n  deviations:\n  - No artifact rejection or electrode exclusion.\n- claim: controls-q4\n  outcome: reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:controls-q4\n  measured: 25\n  notes: 25 of the 32 control points (78%) are in Q4 (13 of 16 at C3, 12 of 16 at C4); Q1 2, Q2 2,\n    Q3 3.\n  deviations:\n  - No artifact rejection or electrode exclusion.\n- claim: table3-q4-effect-size\n  outcome: partially_reproduced\n  notebook: reproduce_jackson_2019.ipynb\n  output: claim:table3-q4-effect-size\n  measured:\n  - 0.99\n  - 0.82\n  - 0.95\n  - 0.85\n  notes: With the 13 patients who have at least one electrode in Q4 off and on, d rises for all\n    three measures under every reading; sharpness 0.73 to 0.99 (within 0.95 +/- 0.095), steepness\n    0.70 to 0.82 (above 0.70 +/- 0.07), raw PAC with the Methods' filters 0.85 to 0.95 (above\n    0.83 +/- 0.083; code's 0.86 to 0.96, log10 0.73 to 1.06 and 0.86 to 1.07). The all-patient\n    PAC d of Table 3 (0.75) is matched by log10 PAC with the Methods' filters (0.73), not by raw\n    PAC (0.85, given as measured, first reading). The Q4 group has 13 patients where the paper\n    has 9 (q4-patient-counts, not reproduced), which bears on these values.\n  deviations:\n  - No artifact rejection or electrode exclusion.\nfindings:\n- kind: data_missing\n  statement: The manual artifact marks (rejected samples) and the list of excluded noisy\n    electrodes that the paper's preprocessing used are not in the dataset; every channels.tsv\n    marks all channels good and the events files hold only a start trigger. The paper's code\n    loads them from rejectscombined.mat, which is not public. Analyses here run without\n    rejection.\n- kind: metadata_insufficient\n  statement: The questionnaire fields of the beh JSON files (Total UPDRS, UPDRS 18-26, Brady kinesia\n    UPDRS, Rigidity UPDRS, Left and Right UPDRS, H&Y, Beck) have no description; the only beh\n    sidecar describes a dummy trial column. Which part of the UPDRS \"Total UPDRS\" covers has to\n    be inferred from the values.\n- kind: other\n  statement: The sub-pd16 ses-on recording, which participants.tsv says was exported from a\n    preprocessed EEGLAB file, has electrode standard deviations about six times those of every\n    other recording after the same preprocessing (median 62.6 uV), about 100 times their power,\n    and no alpha peak; its means are near zero but its channels are not average referenced. The\n    dataset does not say how it was processed or scaled. The sub-pd6 ses-on file, also exported\n    from EEGLAB, is average referenced and lasts 289 s.\n- kind: metadata_insufficient\n  statement: The events files hold one trigger (value 1) a few seconds into most recordings, and\n    other values in sub-pd16 ses-on (130817) and sub-pd17 ses-off (a second 65536); what the\n    trigger marks is not described.\n- kind: methods_unavailable\n  statement: For the paper's authors. The filter length of the mu/alpha (8 to 12 Hz) phase filter\n    for PAC is not given (the Methods give 231 ms for beta; the code has no alpha analysis). With\n    192 taps (three cycles of 8 Hz, pacpy's default) or the code's 231 taps, alpha PAC off\n    against on is not significant after FDR correction (0.061, 0.078), as Table 1 reports; with\n    118 samples it is (0.036). Which length was used?\n- kind: paper_inconsistency\n  statement: Table 2 gives FDR corrected p = 1 for the three non-significant beta tests and for\n    alpha sharpness ratio, where Benjamini-Hochberg over the six tests of the table, as stated,\n    gives smaller values (about 0.36 for the printed p-values); Table 1's corrected values do\n    match Benjamini-Hochberg. Table 3 gives d = 0.75 for PAC in all patients where Table 1 gives\n    0.83.\n"
}
```

```
File created successfully at: attempts/openneuro-ds002778-jackson-2019-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='attempts/openneuro-ds002778-jackson-2019-01.yaml'
s=open(p).read()
old="""(0.0081), all below 0.05. Only steepness is below the paper's bound of 0.004 (0.0044 is just
    above it); sharpness and PAC are not."""
assert old in s
s=s.replace(old,"""(0.0081), all below 0.05. None is below the paper's bound of 0.004 after correction
    (steepness 0.0044 is closest); uncorrected, only steepness is (0.0015).""")
old="""  statement: Table 2 gives FDR corrected p = 1 for the three non-significant beta tests and for
    alpha sharpness ratio, where"""
assert old in s
s=s.replace(old,"""  statement: Table 2 gives FDR corrected p = 1 for beta sharpness ratio, beta PAC and alpha
    sharpness ratio, where""")
open(p,'w').write(s)
p='/tmp/claude-1001/nb/src.py'
s=open(p).read()
old="""# both PAC filter readings (largest 0.0106). Only steepness ratio is below the paper's bound of
# 0.004 (corrected 0.0044, against 0.0106 for sharpness and 0.0096 or 0.0081 for PAC)."""
assert old in s
s=s.replace(old,"""# both PAC filter readings (largest 0.0106). None is below the paper's bound of 0.004 after
# correction (steepness 0.0044, sharpness 0.0106, PAC 0.0096 or 0.0081); uncorrected, only
# steepness is (0.0015).""")
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/nb/convert.py $TMPDIR/nb/src.py entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb
```

```
85 cells
```

**Agent calls Write**

```json
{
 "file_path": "entries/openneuro-ds002778-jackson-2019/README.md",
 "content": "# Jackson, Cole, Voytek & Swann (2019) from OpenNeuro ds002778\n\nTests the findings of [Jackson et al. (2019)](https://doi.org/10.1523/ENEURO.0151-19.2019) on\n[OpenNeuro ds002778](https://openneuro.org/datasets/ds002778/versions/1.0.5), snapshot 1.0.5, which\nholds the resting EEG of 15 patients with Parkinson's disease off and on medication and 16 controls.\nThe paper's manual artifact marks and excluded electrodes are not in the dataset, so the analysis\nrejects no samples and keeps all 32 scalp electrodes.\n\n| Claim | Outcome |\n|---|---|\n| Beta sharpness ratio, steepness ratio and PAC fall with medication (C3/C4) | Partially reproduced (each test holds; one value per claim out of tolerance) |\n| The same with a bipolar montage | Reproduced |\n| No medication effect at F7/F8 or at T7/T8 | Reproduced |\n| Topographies consistent with a sensorimotor origin | Partially reproduced |\n| Off against controls: no difference in sharpness ratio or PAC | Reproduced |\n| Off against controls: steepness ratio higher | Partially reproduced (FDR p 0.053) |\n| Off against controls: PAC higher with a CSD montage | Not reproduced (p 0.075) |\n| UPDRS improves with medication | Reproduced (W 3.5, p 0.0033) |\n| Alpha and beta peaks in every group's spectrum | Not reproduced |\n| Alpha sharpness and steepness fall with medication | Partially reproduced |\n| Alpha PAC does not change with medication | Reproduced, resting on an assumption |\n| Alpha off against controls | Partially reproduced |\n| PAC change larger in beta than in alpha | Partially reproduced |\n| Shape measures correlate with PAC (two claims) | Partially reproduced |\n| Sensorimotor waveforms mostly in Q4, in patients and in controls | Reproduced |\n| Q4 patient counts | Not reproduced (13 patients against 9) |\n| F7/F8 waveform shape more variable | Reproduced |\n| Effect sizes rise in Q4 patients | Partially reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/openneuro-ds002778-jackson-2019-01.yaml`](../../attempts/openneuro-ds002778-jackson-2019-01.yaml).\n\n- `reproduce_jackson_2019.ipynb`: the analysis. It takes about two minutes, most of it reading the\n  46 BDF files (0.57 GB) into memory.\n- `waveshape.py`: listing and reading the pinned snapshot, the preprocessing, sharpness and\n  steepness ratios, peak-to-trough and rise-to-fall ratios, PAC, the CSD transform and the\n  statistics, with where each parameter comes from. Other notebooks on this dataset can import it.\n"
}
```

```
File created successfully at: entries/openneuro-ds002778-jackson-2019/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/dev/bin/activate; python tools/entry.py all entries/openneuro-ds002778-jackson-2019 2>&1 | tail -4 && python tools/entry.py handover entries/openneuro-ds002778-jackson-2019 2>&1 | tail -4; ls executed/openneuro-ds002778-jackson-2019/handover; date -u
```

```
in "<unicode string>", line 224, column 57:
     ... ength is for the paper's authors: the Methods give 231 ms for th ... 
                                         ^
1 error(s)
wrote executed/openneuro-ds002778-jackson-2019/handover
10.1523-eneuro.0151-19.2019.yaml
reproduce_jackson_2019.ipynb
waveshape.py
Tue Oct 27 22:46:33 UTC 2026
```

**Agent calls Bash**

```bash
cd  grep -n ".: " attempts/openneuro-ds002778-jackson-2019-01.yaml | grep -v "^[0-9]*:\s*-\? *[a-z_]*: "
```

```
224:    alpha phase filter length is for the paper's authors: the Methods give 231 ms for the beta
```

**Agent calls Bash**

```bash
cd  sed -i "224s/paper's authors: the Methods give/paper's authors, since the Methods give/" attempts/openneuro-ds002778-jackson-2019-01.yaml; grep -n "Statement\|statement: For the paper" attempts/openneuro-ds002778-jackson-2019-01.yaml; . $TMPDIR/dev/bin/activate; python tools/entry.py all entries/openneuro-ds002778-jackson-2019 2>&1 | tail -3 && python tools/entry.py handover entries/openneuro-ds002778-jackson-2019 2>&1 | tail -2
```

```
372:  statement: For the paper's authors. The filter length of the mu/alpha (8 to 12 Hz) phase filter
Installed kernelspec registry-openneuro-ds002778-jackson-2019 in executed/openneuro-ds002778-jackson-2019/.venv/share/jupyter/kernels/registry-openneuro-ds002778-jackson-2019
0 error(s)
pass  reproduce_jackson_2019.ipynb  (100 s)
wrote executed/openneuro-ds002778-jackson-2019/handover
```

**Agent calls Bash**

```bash
cd  git status --short; grep -n -i "—\|rather\|actually\|genuinely\|worth noting" attempts/openneuro-ds002778-jackson-2019-01.yaml entries/openneuro-ds002778-jackson-2019/* 2>/dev/null | grep -v lock | head; date -u
```

```
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
?? attempts/openneuro-ds002778-jackson-2019-01.yaml
?? entries/openneuro-ds002778-jackson-2019/
?? scripts
Tue Oct 27 22:48:57 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls -a entries/openneuro-ds002778-jackson-2019/; ls -la .bashrc scripts | head -5
```

```
.
..
.claude
README.md
__pycache__
entry.yaml
reproduce_jackson_2019.ipynb
requirements.in
requirements.lock.txt
waveshape.py
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 22:22 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 22:22 scripts
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds002778-jackson-2019; ls -la .claude; rm -rf __pycache__; ls -a
```

```
total 12
drwxr-xr-x 3 runner runner 4096 Oct 27 22:31 .
drwxr-xr-x 4 runner runner 4096 Oct 27 22:46 ..
drwx------ 2 runner runner 4096 Oct 27 22:31 .cc-writes
.
..
.claude
README.md
entry.yaml
reproduce_jackson_2019.ipynb
requirements.in
requirements.lock.txt
waveshape.py
```

**Agent**

All 25 claims were tested and none is blocked. The entry passes `tools/entry.py all` with 0 errors, and the notebook runs in 100 s. The handover package is built in `executed/openneuro-ds002778-jackson-2019/handover/`. Nothing was committed.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| fig2-sharpness-off-on | partially reproduced: W 13 matches; d 0.73 is below 0.86 ± 0.086 |
| fig2-steepness-off-on | partially reproduced: d 0.70 matches; W 16 is outside 9 ± 0.9 |
| fig2-pac-off-on | partially reproduced: d 0.85 matches; W 13 (Methods' filters) or 12 (code's) is outside 15 ± 1.5 |
| bipolar-off-on | reproduced |
| temporalis-f7f8-null, temporalis-t7t8-null | reproduced |
| fig2c-topography-sensorimotor | partially reproduced: steepness meets the criterion, PAC only under one reading, sharpness not (smallest p at P8) |
| offctrl-sharpness-null, offctrl-pac-null | reproduced |
| offctrl-steepness | partially reproduced: z and d match, but FDR-corrected p is 0.053 |
| offctrl-pac-csd | not reproduced: p 0.075 against the paper's 0.022 |
| updrs-improvement | reproduced: W 3.5, p 0.0033, the paper's values exactly |
| fig1c-beta-alpha-peaks | not reproduced: only the controls' average spectrum has both peaks |
| table1-alpha-shape-off-on | partially reproduced: both tests hold; steepness W 21 is outside 12 ± 1.2 |
| table1-alpha-pac-null | reproduced, resting on an assumption (`assumed: true`) |
| table2-alpha-offctrl | partially reproduced: steepness z and d match, but FDR-corrected p is 0.053 |
| pac-beta-larger-than-alpha | partially reproduced: p 0.015; W 17 is outside 11 ± 1.1 |
| fig3-sharpness-pac-correlation, fig3-steepness-pac-correlation | partially reproduced: one r out of tolerance in each |
| fig4a-sensorimotor-q4, controls-q4, fig4b-temporalis-variable-shape | reproduced |
| q4-patient-counts | not reproduced: 13 patients qualify against the paper's 9 |
| table3-q4-effect-size | partially reproduced: d rises for all three measures; steepness and PAC values are above tolerance |

**2. The dataset**
- It holds what the paper describes: 15 patients off and on medication (8 female, mean age 63.3) and 16 controls (9 female, 63.5). There are 46 BDF files at 512 Hz, with no duplicates.
- The paper's manual artifact marks and its list of excluded electrodes are not in the dataset. No samples were rejected and all 32 scalp electrodes were kept (reading (b) of the claims file). Recorded as `data_missing`.
- The `on` session of sub-pd16 was exported from preprocessed EEGLAB files. After preprocessing it has about 6 times the amplitude of any other recording and no alpha peak, and the dataset does not say how it was processed. The `on` session of sub-pd6 came from the same kind of export; it is already average-referenced and lasts 289 s. Results without these two patients are shown as variants.
- The UPDRS fields and the event trigger have no description. Recorded as `metadata_insufficient`.
- Version: 1.0.5 is the latest snapshot. The paper cites none, and the change log shows no change to the EEG files across snapshots.
- **Assumption and question for the authors:** for alpha PAC the paper gives no phase filter length. I adopted 192 taps (three cycles of 8 Hz), which is the default of pacpy, the package the Methods name, and the rule the paper's code uses for its shape filters. With 192 or 231 taps alpha PAC is not significant (corrected p 0.061 and 0.078); with 118 it is (0.036). This question is recorded as a `methods_unavailable` finding.
- Also recorded as a `paper_inconsistency`: Table 2 prints corrected p = 1 where Benjamini-Hochberg gives about 0.36, and Table 3's all-patient PAC d (0.75) differs from Table 1's (0.83).
- I asked a reader no questions.

**3. Where the protocol was unclear**
1. When a result falls in a case the criterion does not name, the protocol gives no rule. This happened for offctrl-steepness and table2-alpha-offctrl: z and d match but the corrected p is 0.053. I recorded both as partially reproduced and gave the reason as a deviation.
2. When a criterion's last sentence names fewer values than its expected list, it is unclear which governs. For fig2-pac-off-on, the last sentence names only the test and d, while the claim also lists an expected statistic. I kept the statistic in the judgement and noted that the sentence alone would give "reproduced".
3. For continuous rest data the clock check does not apply, since there is no trial table. I checked instead that the Status channel and events.tsv agree on every trigger sample, and said so.
4. The protocol does not say what to do when a reading the claims file names has no data. Reading (a), the dataset's own artifact and bad-channel marks, is empty here; I recorded that reading (b) was the only one that could run.
5. Step 1.6 does not say how to choose among readings when two of three agree. I followed it as written, adopting the best-supported reading as an assumption, and noted that two of the three readings agree.

**4. Runtime and failures**
The run took about 26 minutes (22:23 to 22:49 UTC). The only failure was a YAML colon-space in the attempt record, which I fixed. `git status` also shows untracked dotfiles at the repository root (`.bashrc` and others); these are sandbox device mounts, not files I created.

## End of run

68 turns, 23 minutes, result: success.
