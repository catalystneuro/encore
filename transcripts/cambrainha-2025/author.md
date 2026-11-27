# cambrainha-2025 · author · run 45957776408

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md | wc -l; ls; ls entries claims attempts paper | head -50
```

```
Fri Nov 27 07:26:28 UTC 2026
779
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
[... 63 more lines not kept]
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
[... 760 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/cambrainha-2025.yaml; ls paper; ls entries/fouke-2025; cat papers/datasets/cambrainha-2025.yaml; ls questions | grep camb; ls papers/author-notes | grep camb
```

```
<persisted-output>
Output too large (32.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/768bbedf-c9fe-416e-a472-82ebea5461e2/tool-results/bfo2uu32w.txt

Preview (first 2KB):
# Claims for Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), PRX Life,
# doi:10.1103/w49n-2vz8, "Criticality at Work: Scaling in the Mouse Cortex Enhances
# Performance", on dandiset 000713 (Allen Institute, Visual Behavior, Neuropixels).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-27, protocol pilot-18 as stated in docs/protocol.md.
#
# Text read. arXiv preprint 2410.23508 version 2 (15 Sep 2025), standing in for the PRX Life
# version of record, in paper/10.1103-w49n-2vz8.txt: main text, Appendix (Methods and
# Materials, sections 1 to 6), and the Supplemental Material (sections I to VIII and Figures
# S1 to S8). The PDF was opened to read Figures 3, 4, S1, S5, S7 and S8, whose axes the text
# garbles. Values read from figures are marked as such.
#
# Code read. None. The paper links no analysis code and no repository (the contributions
# statement says D.M.C. provided initial code and G.G.C. refined it, without a location).
#
# Data the paper used (Appendix 1, Figure 1A). The Allen Visual Behavior Neuropixels dataset
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/cambrainha-2025.yaml"
}
```

```
1	# Claims for Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), PRX Life,
2	# doi:10.1103/w49n-2vz8, "Criticality at Work: Scaling in the Mouse Cortex Enhances
3	# Performance", on dandiset 000713 (Allen Institute, Visual Behavior, Neuropixels).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-27, protocol pilot-18 as stated in docs/protocol.md.
6	#
7	# Text read. arXiv preprint 2410.23508 version 2 (15 Sep 2025), standing in for the PRX Life
8	# version of record, in paper/10.1103-w49n-2vz8.txt: main text, Appendix (Methods and
9	# Materials, sections 1 to 6), and the Supplemental Material (sections I to VIII and Figures
10	# S1 to S8). The PDF was opened to read Figures 3, 4, S1, S5, S7 and S8, whose axes the text
11	# garbles. Values read from figures are marked as such.
12	#
13	# Code read. None. The paper links no analysis code and no repository (the contributions
14	# statement says D.M.C. provided initial code and G.G.C. refined it, without a location).
15	#
16	# Data the paper used (Appendix 1, Figure 1A). The Allen Visual Behavior Neuropixels dataset
17	# (ref. 60, DANDI), which the dandiset's title names. Mice trained to lick on an image change.
18	# Each recording about 2 h 25 min, in three phases. Active: about 60 min of natural images in
19	# 250-ms flashes, a change-detection task with reward, lick port present. Non-natural images
20	# (NNI): Gabor patches for 15 min, full-field black and white flashes, and a gray screen for
[... 482 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; wc -c paper/*; ls entries/fouke-2025 entries | head -5; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; ls entries/fouke-2025/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat attempts/fouke-2025-01.yaml | head -150; grep -n -A40 "^## DANDI" docs/archives.md | head -80
```

```
schema_version: 3
id: fouke-2025-01
datasets:
- archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
  relation: primary
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "appendix\|methods and materials\|^[0-9]\. \|window\|CV\|surrogate" paper/10.1103-w49n-2vz8.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1103-w49n-2vz8.txt",
 "offset": 382,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the supplement.

**Agent calls Bash**

```bash
sed -n 780,1000p paper/10.1103-w49n-2vz8.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000713/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000713/versions/" | python -m json.tool | grep -E '"version"|"created"|"status"|"asset_count"|"size"'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import requests, json
url="https://api.dandiarchive.org/api/dandisets/000713/versions/0.240702.1725/assets/?page_size=1000"
assets=[]
while url:
    r=requests.get(url).json(); assets+=r['results']; url=r['next']
print(len(assets))
json.dump(assets,open('assets.json','w'))
import collections
kinds=collections.Counter()
for a in assets:
    p=a['path']
    k='probe' if '_probe-' in p else ('ecephys' if 'ecephys' in p else 'other')
    kinds[k]+=1
print(kinds)
main=[a for a in assets if '_probe-' not in a['path']]
print(len(main))
for a in main[:10]: print(a['path'], a['size']/1e9)
import numpy as np
print(np.sum([a['size'] for a in main])/1e9, np.median([a['size'] for a in main])/1e9)
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
cd $TMPDIR && uv venv -q -p 3.12 venv 2>&1 | tail -2; . venv/bin/activate && uv pip install -q requests h5py remfile pynwb numpy scipy pandas matplotlib dandi nbformat 2>&1 | tail -3; python -c "import pynwb, remfile; print(pynwb.__version__)"; nproc; free -g
```

```
4.2.0
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          10           0           3          14
Swap:              2           0           2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import requests, json, collections, numpy as np
url="https://api.dandiarchive.org/api/dandisets/000713/versions/0.240702.1725/assets/?page_size=1000"
assets=[]
while url:
    r=requests.get(url).json(); assets+=r['results']; url=r['next']
print(len(assets))
json.dump(assets,open('assets.json','w'))
main=[a for a in assets if '_probe-' not in a['path']]
print(len(main))
for a in main[:6]: print(a['path'], a['size']/1e9)
print(np.sum([a['size'] for a in main])/1e9, np.median([a['size'] for a in main])/1e9)
subj=collections.Counter(a['path'].split('/')[0] for a in main); print(len(subj))
EOF
```

```
4293
3424
sub-506940/sub-506940_ses-20200302T102159_image.nwb 0.066536617
sub-506940/sub-506940_ses-20200228T111117_image.nwb 0.051419253
sub-506940/sub-506940_ses-20200304T101331_image.nwb 0.066565672
sub-506940/sub-506940_ses-20200305T100947_image.nwb 0.06655823
sub-506940/sub-506940_ses-20200303T100853_image.nwb 0.06653423
sub-506940/sub-506940_ses-20200306T123640_image.nwb 0.066555132
964.055443869 0.191285718
81
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import json, collections, re
assets=json.load(open('assets.json'))
suf=collections.Counter(re.sub(r'.*ses-[^_]*_','',a['path']) if 'ses-' in a['path'] else a['path'] for a in assets)
print(suf.most_common(20))
eph=[a for a in assets if a['path'].endswith('_ecephys.nwb') or a['path'].endswith('ogen.nwb')]
print(len(eph))
for a in sorted(eph,key=lambda a:a['size'])[:3]+sorted(eph,key=lambda a:a['size'])[-3:]: print(a['path'],a['size']/1e9)
EOF
```

```
[('image.nwb', 3271), ('sub-506940/sub-506940_ses-20200817T222149.nwb', 1), ('probe-1158270877_ecephys.nwb', 1), ('probe-1158270876_ecephys.nwb', 1), ('probe-1158270872_ecephys.nwb', 1), ('sub-506940/sub-506940_ses-20200818T230819.nwb', 1), ('probe-1158270878_ecephys.nwb', 1), ('probe-1160283385_ecephys.nwb', 1), ('probe-1158270879_ecephys.nwb', 1), ('probe-1158270880_ecephys.nwb', 1), ('probe-1160283386_ecephys.nwb', 1), ('probe-1160283388_ecephys.nwb', 1), ('probe-1160283387_ecephys.nwb', 1), ('probe-1160283390_ecephys.nwb', 1), ('probe-1160283389_ecephys.nwb', 1), ('probe-1048089911_ecephys.nwb', 1), ('probe-1048089912_ecephys.nwb', 1), ('sub-509808/sub-509808_ses-20200903T211657.nwb', 1), ('probe-1048089913_ecephys.nwb', 1), ('sub-509808/sub-509808_ses-20200902T215314.nwb', 1)]
869
sub-560964/sub-560964_ses-None_probe-1104212398_ecephys.nwb 1.762569864
sub-563497/sub-563497_ses-None_probe-1104459328_ecephys.nwb 2.040260172
sub-563497/sub-563497_ses-None_probe-1104459326_ecephys.nwb 2.040268928
sub-585329/sub-585329_ses-None_probe-1140256850_ecephys.nwb 5.481306192
sub-585329/sub-585329_ses-None_probe-1140256851_ecephys.nwb 5.481320132
sub-585329/sub-585329_ses-None_probe-1140256853_ecephys.nwb 5.545720568
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import json, collections, numpy as np
assets=json.load(open('assets.json'))
sess=[a for a in assets if a['path'].endswith('.nwb') and not a['path'].endswith('image.nwb') and '_probe-' not in a['path']]
print(len(sess), len(set(a['path'].split('/')[0] for a in sess)))
s=np.array([a['size'] for a in sess])/1e9; print(s.min(), np.median(s), s.max(), s.sum())
json.dump(sess,open('sess.json','w'))
print(sess[0])
EOF
```

```
153 81
1.403963704 2.690058323 4.354046401 419.914358483
{'asset_id': '9c7ce5d4-1f01-4685-a45f-18c3393a50d3', 'blob': '4363eed8-b086-40b0-a3df-5163ffb40f9c', 'zarr': None, 'path': 'sub-506940/sub-506940_ses-20200817T222149.nwb', 'size': 2759138245, 'created': '2023-11-30T06:12:14.792791Z', 'modified': '2024-07-02T17:25:16.459531Z'}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > open1.py <<'EOF'
import json, h5py, remfile, requests, time, sys
sess=json.load(open('sess.json'))
a=sess[0]
def s3url(aid):
    r=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False)
    return r.headers['Location']
t=time.time()
f=h5py.File(remfile.File(s3url(a['asset_id'])),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype)
    elif 'neurodata_type' in obj.attrs: print(name, '<', obj.attrs['neurodata_type'],'>')
f.visititems(show)
print(time.time()-t)
EOF
python open1.py 2>&1 | grep -v "^acquisition/.*\(data\|timestamps\)$" | head -200
```

```
acquisition/EyeTracking < EllipseEyeTracking >
acquisition/EyeTracking/corneal_reflection_tracking < EllipseSeries >
acquisition/EyeTracking/corneal_reflection_tracking/angle (573160,) float64
acquisition/EyeTracking/corneal_reflection_tracking/area (573160,) float64
acquisition/EyeTracking/corneal_reflection_tracking/area_raw (573160,) float64
acquisition/EyeTracking/corneal_reflection_tracking/data (573160, 2) float64
acquisition/EyeTracking/corneal_reflection_tracking/height (573160,) float64
acquisition/EyeTracking/corneal_reflection_tracking/reference_frame () object
acquisition/EyeTracking/corneal_reflection_tracking/width (573160,) float64
acquisition/EyeTracking/eye_tracking < EllipseSeries >
acquisition/EyeTracking/eye_tracking/angle (573160,) float64
acquisition/EyeTracking/eye_tracking/area (573160,) float64
acquisition/EyeTracking/eye_tracking/area_raw (573160,) float64
acquisition/EyeTracking/eye_tracking/data (573160, 2) float64
acquisition/EyeTracking/eye_tracking/height (573160,) float64
acquisition/EyeTracking/eye_tracking/reference_frame () object
acquisition/EyeTracking/eye_tracking/timestamps (573160,) float64
acquisition/EyeTracking/eye_tracking/width (573160,) float64
acquisition/EyeTracking/likely_blink < TimeSeries >
acquisition/EyeTracking/likely_blink/data (573160,) bool
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python open1.py 2>&1 | grep -v "^acquisition" | sed -n '/^processing\/optotagging\/optogenetic_stimulation\/level/,$p' | grep -v "^stimulus/templates" | head -120
```

```
processing/optotagging/optogenetic_stimulation/level (300,) float64
processing/optotagging/optogenetic_stimulation/start_time (300,) float64
processing/optotagging/optogenetic_stimulation/stimulus_name (300,) object
processing/optotagging/optogenetic_stimulation/stop_time (300,) float64
processing/optotagging/optogenetic_stimulation/tags (300,) object
processing/optotagging/optogenetic_stimulation/tags_index (300,) uint16
processing/optotagging/optogenetic_stimulation/timeseries (300,) [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
processing/optotagging/optogenetic_stimulation/timeseries_index (300,) uint16
processing/optotagging/optotagging < TimeSeries >
processing/optotagging/optotagging/data (300,) float64
processing/optotagging/optotagging/timestamps (300,) float64
processing/rewards < ProcessingModule >
processing/rewards/autorewarded < TimeSeries >
processing/rewards/autorewarded/data (95,) bool
processing/rewards/autorewarded/timestamps (95,) float64
processing/rewards/volume < TimeSeries >
processing/rewards/volume/data (95,) float64
processing/rewards/volume/timestamps (95,) float64
processing/running < ProcessingModule >
processing/running/dx < TimeSeries >
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > survey1.py <<'EOF'
import json, h5py, remfile, requests, time, numpy as np, collections
sess=json.load(open('sess.json'))
def s3url(aid):
    r=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False)
    return r.headers['Location']
t=time.time()
f=h5py.File(remfile.File(s3url(sess[0]['asset_id'])),'r')
u=f['units']; e=f['general/extracellular_ephys/electrodes']
eid=e['id'][:]; loc=e['location'][:].astype(str)
pc=u['peak_channel_id'][:]
m=dict(zip(eid,loc)); uloc=np.array([m[c] for c in pc])
print(collections.Counter(uloc).most_common(40))
q=u['quality'][:].astype(str); print(collections.Counter(q))
v=uloc=='VISp'
print('VISp', v.sum(), 'good', (v&(q=='good')).sum())
dflt=(u['isi_violations'][:]<0.5)&(u['amplitude_cutoff'][:]<0.1)&(u['presence_ratio'][:]>0.95)
print('default', (v&dflt).sum(), 'default+good', (v&dflt&(q=='good')).sum())
print(np.where(v)[0])
for k in ['session_description','identifier']: print(k, f[k][()])
print({k:f['general/metadata'].attrs[k] for k in f['general/metadata'].attrs})
for k in f['general/metadata']: print(k, f['general/metadata'][k][()])
for k in f['general/subject']: print(k, f['general/subject'][k][()])
for k in f['general/task_parameters']: print(k, f['general/task_parameters'][k][()])
for name in f['intervals']:
    g=f['intervals'][name]
    if 'stimulus_block' in g:
        b=g['stimulus_block'][:]; st=g['start_time'][:]; sp=g['stop_time'][:]
        for bb in np.unique(b):
            i=b==bb; print(name, bb, i.sum(), st[i].min(), sp[i].max(), g['active'][:][i].mean())
tr=f['intervals/trials']; print(tr['start_time'][0], tr['stop_time'][-1])
print(time.time()-t)
EOF
python survey1.py
```

```
[(np.str_('VISp'), 231), (np.str_('CA1'), 181), (np.str_('APN'), 162), (np.str_('VISam'), 146), (np.str_('VISpm'), 141), (np.str_('VISal'), 135), (np.str_('VISl'), 125), (np.str_('MGv'), 117), (np.str_('SUB'), 112), (np.str_('MB'), 107), (np.str_('TH'), 91), (np.str_('MGm'), 87), (np.str_('LGd'), 86), (np.str_('VISrl'), 86), (np.str_('PIL'), 74), (np.str_('DG'), 54), (np.str_('LP'), 44), (np.str_('SNr'), 42), (np.str_('MGd'), 41), (np.str_('MRN'), 39), (np.str_('CA3'), 31), (np.str_('POL'), 30), (np.str_('DT'), 26), (np.str_('SGN'), 19)]
Counter({np.str_('good'): 1830, np.str_('noise'): 377})
VISp 231 good 194
default 66 default+good 63
[ 654  655  656  660  663  664  665  666  676  677  678  679  680  681
  682  683  684  685  686  687  688  691  692  693  694  695  696  697
  698  699  720  725  726  727  728  729  730  731  732  733  734  735
  736  743  744  745  746  747  750  751  754  763  766  767  768  771
  772  773  774  775  776  777  778  779  780  781  782  783  784  785
  786  787  788  789  790  791  792  798  799  800  801  802  810  811
  812  813  814  815  816  817  820  821  822  823  824  825  833  834
  835  836  855  856  858  859  860  861  862  863  864  865  866  867
  871  872  878  879  880  881  885  886  887  888  889  890  898  899
  900  901  902  903  906  907  908  909  910  911  912  913  916  917
  927  928  929  930  931  932  935  936  937  938  939  940  941  942
  943  944  949  950  951  952  960  961  962  963  964  966  967  968
  969  970  971  972  977  978  979  984  985  986  987  988  989  990
  991  997  998  999 1000 1001 1002 1012 1013 1014 1033 1041 1042 1048
 1049 1050 1051 1052 1053 1054 1055 1058 1059 1060 1061 1062 1063 1064
 1065 1066 1067 1068 1069 1075 1076 1077 1078 1079 1080 1081 1082 1083
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > survey.py <<'EOF'
import json, h5py, remfile, requests, time, numpy as np, collections, pandas as pd
from concurrent.futures import ThreadPoolExecutor
sess=json.load(open('sess.json'))
def s3url(aid):
    r=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False)
    return r.headers['Location']
def one(a):
    f=h5py.File(remfile.File(s3url(a['asset_id'])),'r')
    u=f['units']; e=f['general/extracellular_ephys/electrodes']
    m=dict(zip(e['id'][:],e['location'][:].astype(str)))
    uloc=np.array([m[c] for c in u['peak_channel_id'][:]])
    q=u['quality'][:].astype(str); v=uloc=='VISp'
    dflt=(u['isi_violations'][:]<0.5)&(u['amplitude_cutoff'][:]<0.1)&(u['presence_ratio'][:]>0.95)
    idx=u['spike_times_index'][:]; cnt=np.diff(np.r_[0,idx])
    r=dict(path=a['path'],subject=f['general/subject/subject_id'][()].decode(),
           session_type=f['session_description'][()].decode(), ecephys_id=f['identifier'][()].decode(),
           n_units=len(q), visp=int(v.sum()), visp_good=int((v&(q=='good')).sum()), visp_default=int((v&dflt).sum()),
           visp_default_good=int((v&dflt&(q=='good')).sum()), visp_spikes=int(cnt[v].sum()), total_spikes=int(cnt.sum()),
           n_trials=len(f['intervals/trials/start_time']))
    return r
t=time.time()
with ThreadPoolExecutor(12) as ex: rows=list(ex.map(one,sess))
df=pd.DataFrame(rows); df.to_csv('survey.csv',index=False)
print(time.time()-t)
print(df.describe())
for col in ['visp','visp_good','visp_default','visp_default_good']:
    print(col, '>128', (df[col]>128).sum(), df[df[col]>128].subject.nunique(), '>=128', (df[col]>=128).sum(), df[df[col]>=128].subject.nunique())
print(df.ecephys_id.duplicated().sum(), df.duplicated(['total_spikes']).sum())
EOF
python survey.py
```

```
314.0795433521271
           n_units        visp  ...  total_spikes     n_trials
count   153.000000  153.000000  ...  1.530000e+02   153.000000
mean   2085.052288  140.960784  ...  1.185704e+08   682.359477
std     447.254590   47.686046  ...  2.856484e+07   174.086738
min    1103.000000    0.000000  ...  5.037725e+07   429.000000
25%    1785.000000  113.000000  ...  1.011563e+08   574.000000
50%    2024.000000  144.000000  ...  1.169870e+08   631.000000
75%    2364.000000  169.000000  ...  1.349140e+08   729.000000
max    3388.000000  294.000000  ...  2.033122e+08  1597.000000

[8 rows x 8 columns]
visp >128 97 68 >=128 98 68
visp_good >128 68 54 >=128 70 55
visp_default >128 1 1 >=128 1 1
visp_default_good >128 0 0 >=128 0 0
0 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . venv/bin/activate && python -c "
import pandas as pd; df=pd.read_csv('survey.csv'); print(df.session_type.value_counts()); print(df[['visp','visp_good','visp_default','visp_spikes']].describe())"
```

```
Fri Nov 27 07:34:25 UTC 2026
session_type
EPHYS_1_images_G_3uL_reward    74
EPHYS_1_images_H_3uL_reward    71
EPHYS_1_images_G_5uL_reward     4
EPHYS_1_images_H_5uL_reward     4
Name: count, dtype: int64
             visp   visp_good  visp_default   visp_spikes
count  153.000000  153.000000    153.000000  1.530000e+02
mean   140.960784  121.810458     53.156863  5.456791e+06
std     47.686046   42.672522     23.630410  1.760394e+06
min      0.000000    0.000000      0.000000  0.000000e+00
25%    113.000000   95.000000     38.000000  4.490376e+06
50%    144.000000  125.000000     50.000000  5.502791e+06
75%    169.000000  148.000000     70.000000  6.527293e+06
max    294.000000  268.000000    132.000000  1.014306e+07
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import json, h5py, remfile, requests, numpy as np, collections
sess=json.load(open('sess.json'))
def s3url(aid):
    return requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers['Location']
f=h5py.File(remfile.File(s3url(sess[0]['asset_id'])),'r')
tr=f['intervals/trials']
d={k:tr[k][:] for k in ['go','catch','aborted','auto_rewarded','hit','miss','false_alarm','correct_reject','is_change']}
import pandas as pd
df=pd.DataFrame(d); print(df.groupby(['go','catch','aborted','auto_rewarded']).sum()[['hit','miss','false_alarm','correct_reject']])
print(df.groupby(['go','catch','aborted','auto_rewarded']).size())
ct=tr['change_time_no_display_delay'][:]; print(np.isnan(ct[d['go']]).sum(), ct[:5], tr['start_time'][:5])
ns=f['intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations']
om=ns['omitted'][:]; print(np.nansum(om), np.unique(ns['image_name'][:]))
print(f['units/spike_times'].chunks, f['units/spike_times'].compression)
EOF
```

```
hit  miss  false_alarm  correct_reject
go    catch aborted auto_rewarded                                        
False False False   True             0     0            0               0
            True    False            0     0            0               0
      True  False   False            0     0            7              17
True  False False   False           92    69            0               0
go     catch  aborted  auto_rewarded
False  False  False    True               3
              True     False            781
       True   False    False             24
True   False  False    False            161
dtype: int64
0 [     nan      nan 36.00428      nan      nan] [26.22955 27.73042 29.99901 40.50759 42.009  ]
324.0 [b'im012_r' b'im036_r' b'im044_r' b'im047_r' b'im078_r' b'im083_r'
 b'im111_r' b'im115_r' b'omitted']
None None
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; mkdir -p entries/cambrainha-2025; ls entries/cambrainha-2025; sed -n 1,60p entries/fouke-2025/omr.py
```

```
Fri Nov 27 07:36:24 UTC 2026
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
[... 41 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/cambrainha-2025/criticality.py",
 "content": "\"\"\"Loading and measures for Cambrainha et al. (2025) on dandiset 000713.\n\nCambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), \"Criticality at Work: Scaling in\nthe Mouse Cortex Enhances Performance\", PRX Life, doi:10.1103/w49n-2vz8. Claims in\nclaims/cambrainha-2025.yaml; the codes M1 to M8 and O1 to O11 below refer to the method notes\nat the top of that file.\n\nDandiset 000713 (Allen Institute, Visual Behavior Neuropixels) holds one NWB file per session\n(153 sessions, 81 mice) with the sorted units of all probes (`units`, with the peak channel of\neach unit and the channel's brain structure in `electrodes/location`), the stimulus\npresentations by block (`intervals/*_presentations`, column `stimulus_block`) and the task\ntrials (`intervals/trials`). LFP is in separate probe files, which are not read. Files are\nstreamed from the archive at the pinned version with remfile and h5py (pynwb is slow to open\nthese files over the network and adds nothing here); nothing is written to disk. Only the\nspike times of V1 (VISp) units are read.\n\nWhere the parameters come from:\n\n- `BIN_S` 50 ms, `WIN_S` 30 s, `CV_MAX` 5 (M1, Appendix 1); `NCUT_DIV` 16, the kurtosis at\n  Ncutoff = N/16 (M3, Appendix 3); `KAPPA = <psi^4>/<psi^2>^2` (Appendix 3).\n- Unit sets (O1). `all`: every unit whose peak channel is in VISp (the claims file's main\n  reading). `good`: units with `quality == \"good\"`. `default`: the quality filters the Allen\n  documentation gives as defaults (`isi_violations < 0.5`, `amplitude_cutoff < 0.1`,\n  `presence_ratio > 0.95`).\n- Phases (O4). Active is stimulus block 0 (natural images with `active` true); passive is block\n  5. NNI (a) runs from the end of block 0 to the start of block 5 (gray screen, Gabors, gray\n  screen, flashes); NNI (b) is the Gabor block and the flash block, each tiled on its own.\n  Windows tile a phase from its start without overlap and the last partial window is dropped\n  (a standard choice, O4).\n- Units with no spike in a window are left out of that window's analysis (a standard choice:\n  their binned activity has no variance, so they cannot be normalised in Eq. 5 nor correlated\n  in Eq. 6). The number left out is kept per window.\n- Surrogate (M2, Appendix 2): within each window and unit, the intervals between the window's\n  start, the unit's spikes and the window's end are permuted (a standard implementation of\n  \"shuffling the interspike intervals ... within each time window\"; it keeps the spike count\n  and keeps every spike inside the window).\n- Kurtosis pooling (O3): (a) all psi_i(t) pooled; (b) the mean over units of each unit's\n  kurtosis. Ncutoff = floor(N/16) (O3).\n- CV (O2): (a) the population count per bin; (b) the mean over units of each unit's CV;\n  (c) all unit-bin counts pooled.\n- Real-space coarse graining (M7, Appendix 4; O9): Pearson correlation between binned counts,\n  recomputed among clusters at each step; pairs formed greedily from the most correlated pair\n  down; the cluster left over when the count is odd is dropped. M2 is the variance of the\n  cluster sums averaged over clusters (Eq. 7). P_silence (O9): (a) F = -log of the mean over\n  clusters of each cluster's fraction of silent bins; (b) the mean over clusters of -log of that\n  fraction. tau_c is where the cluster-averaged autocorrelation reaches 1/e, by linear\n  interpolation between 50-ms lags (O9), searched up to `MAX_LAG` lags. Spectra (Eq. 9): for\n  each cluster, the eigenvalues of the covariance of its K original units, averaged over the\n  clusters of that size.\n- Fits (O9) are least squares of log quantities on log K. K range (a) from K = 1 to the largest\n  K with at least two clusters; (b) from K = 1 to N/16. F is fitted only where it is finite\n  (where P_silence > 0), with at least three sizes (a standard choice: -log 0 cannot be\n  fitted). mu (a) is one fit of log lambda on log(rank/K) pooled over all K >= 16; (b) the\n  spectrum at K = 64, ranks 1 to 64. Windows with r^2 < 0.85 lose their mu (Appendix 4c).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport h5py\nimport numpy as np\nimport remfile\n\nDANDISET_ID = \"000713\"\nDANDISET_VERSION = \"0.240702.1725\"\n\nBIN_S = 0.05\nWIN_S = 30.0\nCV_MAX = 5.0\nNCUT_DIV = 16\nMIN_UNITS = 128\nMU_R2_MIN = 0.85\nMAX_LAG = 40           # 2 s of lags for tau_c; a standard search limit\n\nACTIVE_BLOCK, PASSIVE_BLOCK = 0, 5\n\n\n# ----------------------------------------------------------------------------- archive\n\ndef session_assets():\n    \"\"\"The session files (not the probe LFP files) at the pinned version, sorted by path.\"\"\"\n    from dandi.dandiapi import DandiAPIClient\n    client = DandiAPIClient()\n    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n    out = []\n    for a in ds.get_assets():\n        p = a.path\n        if p.endswith(\".nwb\") and \"_probe-\" not in p and not p.endswith(\"_image.nwb\"):\n            out.append(dict(path=p, asset_id=a.identifier, size=a.size))\n    return sorted(out, key=lambda d: d[\"path\"])\n\n\ndef asset_url(asset_id):\n    import requests\n    r = requests.head(f\"https://api.dandiarchive.org/api/assets/{asset_id}/download/\",\n                      allow_redirects=False, timeout=60)\n    return r.headers[\"Location\"]\n\n\ndef open_nwb(asset_id):\n    return h5py.File(remfile.File(asset_url(asset_id)), \"r\")\n\n\ndef _str(x):\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef unit_table(f):\n    \"\"\"Per unit: structure of the peak channel, quality label and the default-filter flag.\"\"\"\n    u = f[\"units\"]\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    eid = e[\"id\"][:]\n    loc = dict(zip(eid, e[\"location\"][:].astype(str)))\n    valid = dict(zip(eid, e[\"valid_data\"][:]))\n    pc = u[\"peak_channel_id\"][:]\n    t = dict(\n        location=np.array([loc[c] for c in pc]),\n        valid_channel=np.array([bool(valid[c]) for c in pc]),\n        quality=u[\"quality\"][:].astype(str),\n        isi_violations=u[\"isi_violations\"][:],\n        amplitude_cutoff=u[\"amplitude_cutoff\"][:],\n        presence_ratio=u[\"presence_ratio\"][:],\n        firing_rate=u[\"firing_rate\"][:],\n        spike_index=u[\"spike_times_index\"][:].astype(np.int64),\n    )\n    t[\"default\"] = ((t[\"isi_violations\"] < 0.5) & (t[\"amplitude_cutoff\"] < 0.1)\n                    & (t[\"presence_ratio\"] > 0.95))\n    return t\n\n\ndef survey(asset):\n    \"\"\"Counts of V1 units per reading of O1, read from metadata only.\"\"\"\n    with open_nwb(asset[\"asset_id\"]) as f:\n        t = unit_table(f)\n        v = t[\"location\"] == \"VISp\"\n        tr = f[\"intervals/trials\"]\n        return dict(\n            path=asset[\"path\"], subject=_str(f[\"general/subject/subject_id\"][()]),\n            session=_str(f[\"identifier\"][()]), session_type=_str(f[\"session_description\"][()]),\n            n_units=len(v), visp_all=int(v.sum()), visp_good=int((v & (t[\"quality\"] == \"good\")).sum()),\n            visp_default=int((v & t[\"default\"]).sum()),\n            visp_valid=int((v & t[\"valid_channel\"]).sum()),\n            visp_good_valid=int((v & t[\"valid_channel\"] & (t[\"quality\"] == \"good\")).sum()),\n            visp_spikes=int(np.diff(np.r_[0, t[\"spike_index\"]])[v].sum()),\n            total_spikes=int(t[\"spike_index\"][-1]),\n            n_trials=len(tr[\"start_time\"]),\n            locations=sorted(set(t[\"location\"])),\n        )\n\n\ndef load_session(asset):\n    \"\"\"V1 spike times, unit flags, phase boundaries, trials and flash onsets of one session.\"\"\"\n    with open_nwb(asset[\"asset_id\"]) as f:\n        t = unit_table(f)\n        v = np.where(t[\"location\"] == \"VISp\")[0]\n        idx = t[\"spike_index\"]\n        starts = np.r_[0, idx][v]\n        ends = idx[v]\n        lo, hi = int(starts.min()), int(ends.max())\n        st = f[\"units/spike_times\"][lo:hi]\n        spikes = [st[s - lo:e - lo] for s, e in zip(starts, ends)]\n        blocks = {}\n        flashes = None\n        for name in f[\"intervals\"]:\n            g = f[\"intervals\"][name]\n            if \"stimulus_block\" not in g:\n                continue\n            b = g[\"stimulus_block\"][:]\n            s0, s1 = g[\"start_time\"][:], g[\"stop_time\"][:]\n            for bb in np.unique(b):\n                i = b == bb\n                blocks[int(bb)] = (name, float(s0[i].min()), float(s1[i].max()), int(i.sum()))\n            if name.startswith(\"Natural_Images\"):\n                act = (b == ACTIVE_BLOCK)\n                om = g[\"omitted\"][:].astype(float)\n                flashes = dict(onset=s0[act], omitted=om[act] > 0)\n        tr = f[\"intervals/trials\"]\n        trials = {k: tr[k][:] for k in [\"start_time\", \"stop_time\", \"go\", \"catch\", \"aborted\",\n                                         \"auto_rewarded\", \"hit\", \"miss\",\n                                         \"change_time_no_display_delay\"]}\n        meta = dict(path=asset[\"path\"], subject=_str(f[\"general/subject/subject_id\"][()]),\n                    session=_str(f[\"identifier\"][()]))\n    units = dict(good=t[\"quality\"][v] == \"good\", default=t[\"default\"][v])\n    return dict(meta=meta, spikes=spikes, units=units, blocks=blocks, trials=trials,\n                flashes=flashes)\n\n\ndef phase_spans(blocks):\n    \"\"\"Phase name -> list of (start, stop) spans to tile, following O4.\"\"\"\n    a, p = blocks[ACTIVE_BLOCK], blocks[PASSIVE_BLOCK]\n    gab = [v for k, v in blocks.items() if v[0].startswith(\"gabor\")]\n    fla = [v for k, v in blocks.items() if v[0].startswith(\"flash\")]\n    return {\n        \"active\": [(a[1], a[2])],\n        \"passive\": [(p[1], p[2])],\n        \"nni_a\": [(a[2], p[1])],\n        \"nni_b\": [(g[1], g[2]) for g in gab] + [(x[1], x[2]) for x in fla],\n    }\n\n\ndef tile(spans, win_s):\n    out = []\n    for s0, s1 in spans:\n        n = int(np.floor((s1 - s0) / win_s + 1e-9))\n        out += [(s0 + i * win_s, s0 + (i + 1) * win_s) for i in range(n)]\n    return out\n\n\n# ----------------------------------------------------------------------------- measures\n\ndef bin_window(spikes, t0, nbins):\n    \"\"\"Counts (units x bins) of 50-ms bins from t0.\"\"\"\n    t1 = t0 + nbins * BIN_S\n    X = np.zeros((len(spikes), nbins), dtype=np.float64)\n    for i, s in enumerate(spikes):\n        a, b = np.searchsorted(s, [t0, t1])\n        if b > a:\n            k = ((s[a:b] - t0) / BIN_S).astype(np.int64)\n            np.add.at(X[i], np.clip(k, 0, nbins - 1), 1)\n    return X\n\n\ndef window_spikes(spikes, t0, t1):\n    out = []\n    for s in spikes:\n        a, b = np.searchsorted(s, [t0, t1])\n        out.append(s[a:b])\n    return out\n\n\ndef isi_shuffle(wspikes, t0, t1, rng):\n    \"\"\"Surrogate (M2): permute the intervals between t0, the spikes and t1, per unit.\"\"\"\n    out = []\n    for s in wspikes:\n        if len(s) == 0:\n            out.append(s)\n            continue\n        iv = np.diff(np.r_[t0, s, t1])\n        iv = rng.permutation(iv)\n        out.append(t0 + np.cumsum(iv[:-1]))\n    return out\n\n\ndef bin_spikes(wspikes, t0, nbins):\n    X = np.zeros((len(wspikes), nbins))\n    for i, s in enumerate(wspikes):\n        if len(s):\n            k = np.clip(((s - t0) / BIN_S).astype(np.int64), 0, nbins - 1)\n            X[i] = np.bincount(k, minlength=nbins)\n    return X\n\n\ndef cv_readings(X):\n    \"\"\"CV of a window (O2): (a) population count per bin, (b) mean unit CV, (c) pooled.\"\"\"\n    pop = X.sum(0)\n    cva = pop.std() / pop.mean() if pop.mean() > 0 else np.inf\n    m = X.mean(1)\n    ok = m > 0\n    cvb = np.mean(X[ok].std(1) / m[ok]) if ok.any() else np.inf\n    cvc = X.std() / X.mean() if X.mean() > 0 else np.inf\n    return cva, cvb, cvc\n\n\ndef _kurt(psi):\n    \"\"\"Pooled (a) and mean-over-units (b) kurtosis of rows of psi (zero mean, unit variance).\"\"\"\n    p2 = psi ** 2\n    ka = np.mean(p2 ** 2) / np.mean(p2) ** 2\n    kb = np.mean(np.mean(p2 ** 2, 1) / np.mean(p2, 1) ** 2)\n    return ka, kb\n\n\ndef momentum_kurtosis(X):\n    \"\"\"Kurtosis after momentum-space coarse graining (M3, Eqs. 2 to 5), and before (kappa_0).\n\n    X holds the binned counts of the units active in the window. Returns\n    (kappa_a, kappa_b, kappa0_a, kappa0_b) under the two poolings of O3.\n    \"\"\"\n    N = X.shape[0]\n    D = X - X.mean(1, keepdims=True)\n    C = D @ D.T / X.shape[1]\n    w, U = np.linalg.eigh(C)\n    k = max(N // NCUT_DIV, 1)\n    Uk = U[:, -k:]                      # top Ncutoff eigenvectors\n    psi = Uk @ (Uk.T @ D)               # Eq. 5, sum over j of P_ij (phi_j - <phi_j>)\n    sd = psi.std(1, keepdims=True)\n    good = sd[:, 0] > 1e-12\n    psi = psi[good] / sd[good]\n    ka, kb = _kurt(psi)\n    z0 = D / D.std(1, keepdims=True)\n    k0a, k0b = _kurt(z0)\n    return ka, kb, k0a, k0b\n\n\ndef _greedy_pairs(R):\n    \"\"\"Pairs of clusters from the most correlated down (Eq. 6); the odd one out is dropped.\"\"\"\n    n = R.shape[0]\n    iu, ju = np.triu_indices(n, 1)\n    r = R[iu, ju]\n    r = np.where(np.isfinite(r), r, -np.inf)\n    order = np.argsort(-r, kind=\"stable\")\n    used = np.zeros(n, bool)\n    pairs = []\n    target = n // 2\n    for o in order:\n        i, j = iu[o], ju[o]\n        if not used[i] and not used[j]:\n            used[i] = used[j] = True\n            pairs.append((i, j))\n            if len(pairs) == target:\n                break\n    return pairs\n\n\ndef _autocorr_tau(Y):\n    \"\"\"tau_c (s): where the cluster-averaged autocorrelation reaches 1/e (O9).\"\"\"\n    Yc = Y - Y.mean(1, keepdims=True)\n    var = (Yc ** 2).mean(1)\n    ok = var > 0\n    Yc, var = Yc[ok], var[ok]\n    T = Y.shape[1]\n    c = [1.0]\n    for lag in range(1, MAX_LAG + 1):\n        c.append(np.mean((Yc[:, :-lag] * Yc[:, lag:]).sum(1) / (T - lag) / var))\n        if c[-1] < 1 / np.e:\n            c0, c1 = c[-2], c[-1]\n            return (lag - 1 + (c0 - 1 / np.e) / (c0 - c1)) * BIN_S\n    return np.nan\n\n\ndef real_space(X):\n    \"\"\"Real-space coarse graining (M7, Eqs. 6 to 10) of one window's counts X (units x bins).\n\n    Returns, per cluster size K = 1, 2, 4, ...: number of clusters, M2, mean silent fraction,\n    mean -log silent fraction (inf when a cluster is never silent), tau_c, and for K >= 16 the\n    mean within-cluster covariance spectrum (descending).\n    \"\"\"\n    members = [[i] for i in range(X.shape[0])]\n    Y = X.copy()\n    out = dict(K=[], n=[], M2=[], Psil=[], Fb=[], tau=[], spectra={})\n    K = 1\n    while True:\n        psil = (Y == 0).mean(1)\n        with np.errstate(divide=\"ignore\"):\n            fb = np.mean(-np.log(psil))\n        out[\"K\"].append(K)\n        out[\"n\"].append(Y.shape[0])\n        out[\"M2\"].append(Y.var(1).mean())\n        out[\"Psil\"].append(psil.mean())\n        out[\"Fb\"].append(fb)\n        out[\"tau\"].append(_autocorr_tau(Y))\n        if K >= 16:\n            sp = []\n            for m in members:\n                Z = X[m]\n                Z = Z - Z.mean(1, keepdims=True)\n                ev = np.linalg.eigvalsh(Z @ Z.T / X.shape[1])[::-1]\n                sp.append(ev)\n            out[\"spectra\"][K] = np.mean(sp, 0)\n        if Y.shape[0] < 2:\n            break\n        sd = Y.std(1)\n        Yc = Y - Y.mean(1, keepdims=True)\n        with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n            Z = Yc / sd[:, None]\n            R = Z @ Z.T / Y.shape[1]\n        pairs = _greedy_pairs(R)\n        if not pairs:\n            break\n        Y = np.array([Y[i] + Y[j] for i, j in pairs])\n        members = [members[i] + members[j] for i, j in pairs]\n        K *= 2\n    for k in [\"K\", \"n\", \"M2\", \"Psil\", \"Fb\", \"tau\"]:\n        out[k] = np.array(out[k], dtype=float)\n    return out\n\n\ndef _fit(x, y):\n    ok = np.isfinite(x) & np.isfinite(y)\n    if ok.sum() < 3:\n        return np.nan, np.nan\n    p = np.polyfit(x[ok], y[ok], 1)\n    yy = np.polyval(p, x[ok])\n    ss = np.sum((y[ok] - y[ok].mean()) ** 2)\n    r2 = 1 - np.sum((y[ok] - yy) ** 2) / ss if ss > 0 else np.nan\n    return p[0], r2\n\n\ndef fit_exponents(rs, N, krange=\"a\", fsil=\"a\", mu=\"a\"):\n    \"\"\"alpha, beta, mu, mu's r^2 and z from one set of real-space quantities (O9 readings).\n\n    `rs` is the output of `real_space` (or its average over windows). `N` is the number of\n    units, which sets the K range of reading (b).\n    \"\"\"\n    K = rs[\"K\"]\n    if krange == \"a\":\n        sel = (rs[\"n\"] >= 2)\n    else:\n        sel = K <= N / NCUT_DIV\n    lk = np.log(K[sel])\n    alpha, _ = _fit(lk, np.log(rs[\"M2\"][sel]))\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        if fsil == \"a\":\n            F = -np.log(rs[\"Psil\"][sel])\n        else:\n            F = rs[\"Fb\"][sel]\n        beta, _ = _fit(lk, np.log(F))\n    z, _ = _fit(lk, np.log(rs[\"tau\"][sel]))\n    m, r2 = np.nan, np.nan\n    if mu == \"a\":\n        xs, ys = [], []\n        for k, sp in rs[\"spectra\"].items():\n            if k >= 16:\n                rank = np.arange(1, len(sp) + 1)\n                pos = sp > 0\n                xs.append(np.log(rank[pos] / k))\n                ys.append(np.log(sp[pos]))\n        if xs:\n            s, r2 = _fit(np.concatenate(xs), np.concatenate(ys))\n            m = -s\n    else:\n        sp = rs[\"spectra\"].get(64)\n        if sp is not None:\n            rank = np.arange(1, len(sp) + 1)\n            pos = sp > 0\n            s, r2 = _fit(np.log(rank[pos] / 64), np.log(sp[pos]))\n            m = -s\n    return dict(alpha=alpha, beta=beta, mu=m, mu_r2=r2, z=z)\n\n\nEXP_READINGS = [(kr, fs, mu) for kr in \"ab\" for fs in \"ab\" for mu in \"ab\"]\n\n\ndef average_rs(rss):\n    \"\"\"O10 (b): the real-space quantities averaged over windows, per K (and spectrum).\"\"\"\n    Ks = sorted(set(k for r in rss for k in r[\"K\"]))\n    out = dict(K=[], n=[], M2=[], Psil=[], Fb=[], tau=[], spectra={})\n    for k in Ks:\n        vals = {q: [] for q in [\"n\", \"M2\", \"Psil\", \"Fb\", \"tau\"]}\n        sps = []\n        for r in rss:\n            i = np.where(r[\"K\"] == k)[0]\n            if len(i):\n                for q in vals:\n                    vals[q].append(r[q][i[0]])\n                if k in r[\"spectra\"]:\n                    sps.append(r[\"spectra\"][k])\n        out[\"K\"].append(k)\n        out[\"n\"].append(np.min(vals[\"n\"]))\n        for q in [\"M2\", \"Psil\", \"tau\"]:\n            out[q].append(np.nanmean(vals[q]))\n        fb = np.array(vals[\"Fb\"])\n        out[\"Fb\"].append(np.mean(fb) if np.all(np.isfinite(fb)) else np.inf)\n        if sps:\n            L = min(len(s) for s in sps)\n            out[\"spectra\"][k] = np.mean([s[:L] for s in sps], 0)\n    for q in [\"K\", \"n\", \"M2\", \"Psil\", \"Fb\", \"tau\"]:\n        out[q] = np.array(out[q], dtype=float)\n    return out\n\n\n# ----------------------------------------------------------------------------- per session\n\ndef analyse_window(spikes, t0, t1, rng_list, do_real_space=True, surr_real_space=True):\n    \"\"\"Everything computed on one window: counts, CVs, kurtosis, surrogates, real space.\"\"\"\n    nb = int(round((t1 - t0) / BIN_S))\n    ws = window_spikes(spikes, t0, t1)\n    X = bin_spikes(ws, t0, nb)\n    active = X.sum(1) > 0\n    Xa = X[active]\n    rec = dict(t0=t0, t1=t1, n_units=int(len(spikes)), N=int(active.sum()),\n               n_silent=int((~active).sum()), rate=float(X.mean()),\n               spikes=int(X.sum()))\n    rec[\"cv_a\"], rec[\"cv_b\"], rec[\"cv_c\"] = cv_readings(X)\n    rec[\"kappa_a\"], rec[\"kappa_b\"], rec[\"kappa0_a\"], rec[\"kappa0_b\"] = momentum_kurtosis(Xa)\n    if do_real_space:\n        rec[\"rs\"] = real_space(Xa)\n    wa = [s for s, a in zip(ws, active) if a]\n    for si, rng in enumerate(rng_list):\n        S = bin_spikes(isi_shuffle(wa, t0, t1, rng), t0, nb)\n        S = S[S.sum(1) > 0]\n        ka, kb, _, _ = momentum_kurtosis(S)\n        rec[f\"surr{si}_kappa_a\"], rec[f\"surr{si}_kappa_b\"] = ka, kb\n        if si == 0 and do_real_space and surr_real_space:\n            rec[\"surr_rs\"] = real_space(S)\n    return rec\n\n\ndef flash_contrast(spikes, flashes):\n    \"\"\"Clock check: V1 population spikes 30 to 130 ms after image onsets minus the 100 ms\n    before, for shown images and for omitted flashes of the active block.\"\"\"\n    allsp = np.sort(np.concatenate(spikes))\n    on = flashes[\"onset\"]\n\n    def cnt(a, b):\n        return np.searchsorted(allsp, on + b) - np.searchsorted(allsp, on + a)\n    resp = cnt(0.03, 0.13) - cnt(-0.10, 0.0)\n    shown, om = resp[~flashes[\"omitted\"]], resp[flashes[\"omitted\"]]\n    return dict(shown_mean=float(shown.mean()), shown_sd=float(shown.std()),\n                n_shown=int(len(shown)), omitted_mean=float(om.mean()) if len(om) else np.nan,\n                omitted_sd=float(om.std()) if len(om) else np.nan, n_omitted=int(len(om)))\n\n\ndef process_session(asset, surr_seeds, strict_seed, strict_sets=()):\n    \"\"\"All per-window results of one session.\n\n    `surr_seeds`: SeedSequences for the surrogate of each window (the first is the claim's\n    seed, the others the four seed variants). `strict_seed`: the SeedSequence for the\n    surrogate of the strict-unit analysis (figs2-strict-units). `strict_sets`: unit sets\n    (\"good\", \"default\") for which the active phase is also analysed.\n    \"\"\"\n    d = load_session(asset)\n    spikes = d[\"spikes\"]\n    spans = phase_spans(d[\"blocks\"])\n    rows = []\n    rngs = [np.random.default_rng(s) for s in surr_seeds]\n    for phase in [\"active\", \"passive\", \"nni_a\", \"nni_b\"]:\n        for wi, (t0, t1) in enumerate(tile(spans[phase], WIN_S)):\n            r = analyse_window(spikes, t0, t1, rngs)\n            r.update(phase=phase, win=wi, length=WIN_S, units=\"all\")\n            rows.append(r)\n    for L in (10.0, 60.0):\n        for wi, (t0, t1) in enumerate(tile(spans[\"active\"], L)):\n            r = analyse_window(spikes, t0, t1, [], do_real_space=False)\n            r.update(phase=\"active\", win=wi, length=L, units=\"all\")\n            rows.append(r)\n    srng = np.random.default_rng(strict_seed)\n    for uset in strict_sets:\n        sub = [s for s, k in zip(spikes, d[\"units\"][uset]) if k]\n        for wi, (t0, t1) in enumerate(tile(spans[\"active\"], WIN_S)):\n            r = analyse_window(sub, t0, t1, [srng], do_real_space=False)\n            r.update(phase=\"active\", win=wi, length=WIN_S, units=uset)\n            rows.append(r)\n    for r in rows:\n        r.update(d[\"meta\"])\n    sorted_ok = all(np.all(np.diff(s) >= 0) for s in spikes)\n    return dict(meta=d[\"meta\"], windows=rows, trials=d[\"trials\"], blocks=d[\"blocks\"],\n                spans=spans, clock=flash_contrast(spikes, d[\"flashes\"]),\n                n_units=len(spikes), n_good=int(d[\"units\"][\"good\"].sum()),\n                n_default=int(d[\"units\"][\"default\"].sum()), spikes_sorted=sorted_ok,\n                rates=np.array([len(s) for s in spikes]))\n"
}
```

```
File created successfully at: entries/cambrainha-2025/criticality.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > t1.py <<'EOF'
import sys, time, json, resource, numpy as np, pandas as pd
sys.path.insert(0,'entries/cambrainha-2025')
import criticality as cr
sv=pd.read_csv('survey.csv'); sess={a['path']:a for a in json.load(open('sess.json'))}
row=sv[sv.visp>128].iloc[0]; a=sess[row.path]; print(row.path,row.visp)
t=time.time(); d=cr.load_session(a); print('load',time.time()-t, len(d['spikes']))
print(d['blocks'])
sp=cr.phase_spans(d['blocks']); 
for k,v in sp.items(): print(k, v, len(cr.tile(v,30)))
rngs=[np.random.default_rng(i) for i in range(5)]
t=time.time()
for (t0,t1) in cr.tile(sp['active'],30)[:10]:
    r=cr.analyse_window(d['spikes'],t0,t1,rngs)
print('per window',(time.time()-t)/10)
print({k:v for k,v in r.items() if k not in ('rs','surr_rs')})
rs=r['rs']; print(rs['K'], rs['n'], rs['M2'], rs['Psil'], rs['Fb'], rs['tau'])
for rd in cr.EXP_READINGS: print(rd, cr.fit_exponents(rs, r['N'], *rd))
print('surr', cr.fit_exponents(r['surr_rs'], r['N']))
t=time.time(); 
for (t0,t1) in cr.tile(sp['active'],30)[:10]: cr.real_space(cr.bin_window(d['spikes'],t0,600))
print('rs only',(time.time()-t)/10)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
python t1.py
```

```
sub-506940/sub-506940_ses-20200817T222149.nwb 231
load 5.468154430389404 231
{0: ('Natural_Images_Lum_Matched_set_ophys_G_2019_presentations', 26.274262977154944, 3628.805384431677, 4799), 5: ('Natural_Images_Lum_Matched_set_ophys_G_2019_presentations', 5181.471246994742, 8783.952539551632, 4799), 4: ('flash_250ms_presentations', 4858.7847132282695, 5157.284359154284, 150), 2: ('gabor_20_deg_250ms_presentations', 3657.779673228269, 4569.792961006314, 3645), 1: ('spontaneous_presentations', 3647.771263228269, 3657.779673228269, 1), 3: ('spontaneous_presentations', 4569.792961006314, 4858.7847132282695, 1)}
active [(26.274262977154944, 3628.805384431677)] 120
passive [(5181.471246994742, 8783.952539551632)] 120
nni_a [(3628.805384431677, 5181.471246994742)] 51
nni_b [(3657.779673228269, 4569.792961006314), (4858.7847132282695, 5157.284359154284)] 39
per window 0.053880715370178224
{'t0': 296.27426297715493, 't1': 326.27426297715493, 'n_units': 231, 'N': 159, 'n_silent': 72, 'rate': 0.15192640692640694, 'spikes': 21057, 'cv_a': np.float64(0.6291104612580972), 'cv_b': np.float64(5.493199818669555), 'cv_c': np.float64(3.6948433837348147), 'kappa_a': np.float64(3.6723441679453694), 'kappa_b': np.float64(3.6723441679453703), 'kappa0_a': np.float64(63.379244784435855), 'kappa0_b': np.float64(63.37924478443587), 'surr0_kappa_a': np.float64(3.4916802247543806), 'surr0_kappa_b': np.float64(3.491680224754382), 'surr1_kappa_a': np.float64(3.4276869325250923), 'surr1_kappa_b': np.float64(3.427686932525092), 'surr2_kappa_a': np.float64(3.399555106565667), 'surr2_kappa_b': np.float64(3.399555106565667), 'surr3_kappa_a': np.float64(3.426159261877743), 'surr3_kappa_b': np.float64(3.4261592618777423), 'surr4_kappa_a': np.float64(3.449736610783499), 'surr4_kappa_b': np.float64(3.4497366107834995)}
[  1.   2.   4.   8.  16.  32.  64. 128.] [159.  79.  39.  19.   9.   4.   2.   1.] [3.56326293e-01 9.41179466e-01 2.47792920e+00 7.02919079e+00
 1.95519843e+01 6.02870264e+01 1.51014661e+02 
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,140p paper/10.1103-w49n-2vz8.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
which pdftoppm mutool gs convert; cd $TMPDIR && . venv/bin/activate && uv pip install -q pymupdf 2>&1|tail -1; python -c "
import fitz; d=fitz.open('paper/10.1103-w49n-2vz8.pdf'); print(len(d))
for i in [2,3,4]:
    d[i].get_pixmap(dpi=110).save(f'p{i}.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p2.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p3.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > t2.py <<'EOF'
import sys, time, json, numpy as np, pandas as pd
sys.path.insert(0,'entries/cambrainha-2025')
import criticality as cr
sv=pd.read_csv('survey.csv'); sess={a['path']:a for a in json.load(open('sess.json'))}
row=sv[sv.visp>128].iloc[0]; a=sess[row.path]
d=cr.load_session(a); sp=cr.phase_spans(d['blocks'])
rng=np.random.default_rng(0)
def variants(X):
    X=X[X.sum(1)>0]; N=len(X); D=X-X.mean(1,keepdims=True); C=D@D.T/X.shape[1]
    w,U=np.linalg.eigh(C); k=N//16; Uk=U[:,-k:]
    psi=Uk@(Uk.T@D)
    def K(p): p2=p**2; return np.mean(p2**2)/np.mean(p2)**2
    A=K(psi/psi.std(1,keepdims=True))
    B=K((Uk.T@D)/(Uk.T@D).std(1,keepdims=True))
    Cc=K(psi)
    # kurtosis per unit then mean
    E=np.mean([K(p/p.std()) for p in psi])
    # uncentered
    psiU=Uk@(Uk.T@X); F=K(psiU/psiU.std(1,keepdims=True))
    # correlation matrix based
    Z=D/D.std(1,keepdims=True); w2,U2=np.linalg.eigh(Z@Z.T/X.shape[1]); U2k=U2[:,-k:]; p2=U2k@(U2k.T@Z); G=K(p2/p2.std(1,keepdims=True))
    return np.round([A,B,Cc,E,F,G],2)
for (t0,t1) in cr.tile(sp['active'],30)[:8]:
    ws=cr.window_spikes(d['spikes'],t0,t1); X=cr.bin_spikes(ws,t0,600)
    S=cr.bin_spikes(cr.isi_shuffle(ws,t0,t1,rng),t0,600)
    print(variants(X), variants(S))
EOF
python t2.py
```

```
[ 5.3   4.07 43.59  5.3   4.26 36.26] [ 3.21  3.39 46.36  3.21  3.05 17.28]
[ 5.65  4.94 28.16  5.65  4.66 57.28] [ 3.29  3.23 48.83  3.29  3.37 36.49]
[ 6.78  4.85 67.32  6.78  5.13 41.6 ] [ 3.57  3.57 59.66  3.57  3.47 40.05]
[ 4.07  4.11 41.25  4.07  3.59 30.45] [ 3.26  3.57 57.15  3.26  3.09 31.79]
[ 5.56  4.95 38.1   5.56  4.32 40.69] [ 3.53  3.87 65.1   3.53  3.61 25.34]
[ 6.26  4.23 41.73  6.26  5.41 26.41] [ 3.48  3.45 52.47  3.48  3.66 23.18]
[  4.45   6.11 299.44   4.45   3.73  30.29] [  3.86   4.84 244.83   3.86   3.6   19.28]
[  5.9    5.01 241.44   5.9    4.95  26.25] [  3.63   4.62 353.94   3.63   3.67  23.22]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025 && cat >> criticality.py <<'EOF'


def _work(args):
    asset, seeds, strict_seed, strict_sets = args
    for attempt in range(3):
        try:
            return process_session(asset, seeds, strict_seed, strict_sets)
        except Exception as e:  # network errors: retry, then report
            err = repr(e)
    return dict(meta=dict(path=asset["path"]), error=err)


def run_sessions(assets, surr_seed, strict_seed, strict_sets_of, workers=4, n_variants=5):
    """Process sessions in parallel. Seeds: each session's generators are children
    (SeedSequence.spawn) of the claim's seed, and of the claim's seed plus 1000, 2000, 3000 and
    4000 for the seed variants, in the order of `assets`."""
    from concurrent.futures import ProcessPoolExecutor
    n = len(assets)
    kids = [np.random.SeedSequence(surr_seed + 1000 * v).spawn(n) for v in range(n_variants)]
    skids = np.random.SeedSequence(strict_seed).spawn(n)
    jobs = [(a, [kids[v][i] for v in range(n_variants)], skids[i], strict_sets_of(a))
            for i, a in enumerate(assets)]
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_work, jobs))
EOF
cd $TMPDIR && . venv/bin/activate && cat > runall.py <<'EOF'
import os
os.environ["OMP_NUM_THREADS"]="1"; os.environ["OPENBLAS_NUM_THREADS"]="1"; os.environ["MKL_NUM_THREADS"]="1"
import sys, time, json, zlib, pickle, resource, numpy as np, pandas as pd
sys.path.insert(0,'entries/cambrainha-2025')
import criticality as cr
sv=pd.read_csv('survey.csv'); sess={a['path']:a for a in json.load(open('sess.json'))}
sel=sv[sv.visp>=128].sort_values('path')
n=int(sys.argv[1]) if len(sys.argv)>1 else len(sel)
assets=[dict(path=p, asset_id=sess[p]['asset_id']) for p in sel.path][:n]
good=dict(zip(sv.path, sv.visp_good)); dfl=dict(zip(sv.path, sv.visp_default))
def ss(a):
    return tuple(k for k,c in (("good",good[a['path']]),("default",dfl[a['path']])) if c>=128)
t=time.time()
res=cr.run_sessions(assets, zlib.crc32(b"cambrainha-2025/fig3a-kurtosis-broader-than-surrogate"),
    zlib.crc32(b"cambrainha-2025/figs2-strict-units"), ss)
print(time.time()-t, sum('error' in r for r in res))
pickle.dump(res, open(f'res_{n}.pkl','wb'))
print(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e6)
EOF
time python runall.py 4
```

```
40.52905535697937 0
0.849408

real	0m40.944s
user	2m1.173s
sys	0m2.758s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import pickle, pandas as pd, numpy as np
res=pickle.load(open('res_4.pkl','rb'))
for r in res:
    print(r['meta'], r['clock'], r['n_units'], r['n_good'], r['spikes_sorted'])
W=pd.DataFrame([{k:v for k,v in w.items() if k not in ('rs','surr_rs')} for r in res for w in r['windows']])
print(W.groupby(['phase','length','units']).agg(n=('t0','size'),k=('kappa_a','median'),kmax=('kappa_a','max'),s=('surr0_kappa_a','median'),smax=('surr0_kappa_a','max'),cva=('cv_a','max'),cvb=('cv_b','median'),cvc=('cv_c','median'),rate=('rate','median'),nsil=('n_silent','median')))
EOF
```

```
{'path': 'sub-506940/sub-506940_ses-20200817T222149.nwb', 'subject': '506940', 'session': '1043752325'} {'shown_mean': 72.55704119042484, 'shown_sd': 37.9843961998881, 'n_shown': 4637, 'omitted_mean': 2.7777777777777777, 'omitted_sd': 18.21849555388462, 'n_omitted': 162} 231 194 True
{'path': 'sub-506940/sub-506940_ses-20200818T230819.nwb', 'subject': '506940', 'session': '1044016459'} {'shown_mean': 113.36621241617998, 'shown_sd': 37.198170283756085, 'n_shown': 4623, 'omitted_mean': 2.480225988700565, 'omitted_sd': 17.843351764980035, 'n_omitted': 177} 168 90 True
{'path': 'sub-510589/sub-510589_ses-20200819T222405.nwb', 'subject': '510589', 'session': '1044389060'} {'shown_mean': 55.45240664796029, 'shown_sd': 37.89978992469821, 'n_shown': 4633, 'omitted_mean': 4.678787878787879, 'omitted_sd': 20.97935142966889, 'n_omitted': 165} 227 190 True
{'path': 'sub-521466/sub-521466_ses-20200909T220423.nwb', 'subject': '521466', 'session': '1049273528'} {'shown_mean': 70.6521456436931, 'shown_sd': 27.685962220328925, 'n_shown': 4614, 'omitted_mean': 1.057591623036649, 'omitted_sd': 15.48252967346657, 'n_omitted': 191} 196 167 True
                         n         k       kmax  ...       cvc      rate  nsil
phase   length units                             ...                          
active  10.0   all    1440  5.902877  17.266618  ...  3.084154  0.183968  54.0
        30.0   all     480  5.865979  23.305575  ...  3.074608  0.183510  38.0
               good    360  6.037529  15.644768  ...  3.012633  0.191154  30.5
        60.0   all     240  6.032472  23.114159  ...  3.076707  0.184435  30.5
nni_a   30.0   all     204  6.693854  19.352376  ...  2.780836  0.213278  22.0
nni_b   30.0   all     156  6.913991  11.972285  ...  2.772427  0.219608  21.0
passive 30.0   all     480  5.503640  11.158788  ...  2.713350  0.226586  18.0

[7 rows x 10 columns]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . venv/bin/activate && time python runall.py; date -u
```

```
Fri Nov 27 07:40:49 UTC 2026
/tmp/claude-1001/venv/lib/python3.12/site-packages/numpy/_core/fromnumeric.py:3862: RuntimeWarning: Mean of empty slice
  return _methods._mean(a, axis=axis, dtype=dtype,
/tmp/claude-1001/venv/lib/python3.12/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
729.9415810108185 0
1.01144

real	12m14.597s
user	39m45.676s
sys	0m53.466s
Fri Nov 27 07:53:03 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import pickle, pandas as pd, numpy as np
res=pickle.load(open('res_98.pkl','rb'))
W=pd.DataFrame([{k:v for k,v in w.items() if k not in ('rs','surr_rs')} for r in res for w in r['windows']])
W.to_pickle('W.pkl')
g=W.groupby(['phase','length','units'])
print(g.agg(n=('t0','size'),k=('kappa_a','median'),kq=('kappa_a',lambda x: x.quantile(.9)),kmax=('kappa_a','max'),s=('surr0_kappa_a','median'),smin=('surr0_kappa_a','min'),smax=('surr0_kappa_a','max')).to_string())
print(g.agg(cva=('cv_a','max'),cvb=('cv_b','median'),cvbx=('cv_b',lambda x:(x>5).mean()),cvc=('cv_c',lambda x:(x>5).mean()),rate=('rate','median'),nsil=('n_silent','median')).to_string())
for i in range(5): print(i, W[(W.length==30)&(W.units=='all')].groupby('phase')[f'surr{i}_kappa_a'].max().round(2).to_dict())
EOF
```

```
n         k         kq        kmax         s      smin       smax
phase   length units                                                                         
active  10.0   all      35282  5.854414   9.091902  198.005025       NaN       NaN        NaN
        30.0   all      11759  6.179532   8.846090   89.805679  3.637962  2.803676  34.292115
               default    120  5.841407   7.087995   35.753234  4.369878  3.106348   9.015854
               good      8399  6.119025   8.722840   80.660837  3.612998  2.755645  52.564096
        60.0   all       5879  6.473776   8.953149   75.770323       NaN       NaN        NaN
nni_a   30.0   all       5108  6.986790  10.604176   45.542098  3.408181  2.907046  25.816971
nni_b   30.0   all       3822  7.214588  10.319783   23.617063  3.451528  2.945838  23.577303
passive 30.0   all      11759  5.536346   7.440435   89.406735  3.405381  2.895733  48.340741
                             cva       cvb      cvbx       cvc      rate  nsil
phase   length units                                                          
active  10.0   all           inf  4.653340  0.294144  0.017941  0.170370  32.0
        30.0   all      2.895528  5.809686  0.830598  0.017774  0.170808  19.0
               default  0.978936  5.312226  0.550000  0.000000  0.237153   2.0
               good     7.000000  5.894909  0.846053  0.012144  0.176804  16.0
        60.0   all      3.739767  6.587006  0.935703  0.017860  0.171500  14.0
nni_a   30.0   all      1.295506  5.570750  0.797377  0.000000  0.196015  13.0
nni_b   30.0   all      1.277550  5.429872  0.756149  0.000000  0.200802  12.0
passive 30.0   all      3.886433  4.968957  0.481504  0.001020  0.221724  11.0
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import pandas as pd, numpy as np
W=pd.read_pickle('W.pkl'); W=W[(W.length==30)&(W.units=='all')]
for cv in ['cv_a','cv_b','cv_c']:
    k=W[W[cv]<=5]
    print(cv, len(k), k.groupby('phase').surr0_kappa_a.agg(['max',lambda x:x.quantile(.999),lambda x:x.quantile(.99),'min',lambda x:x.quantile(.05)]).round(2).to_string())
a=W[W.phase=='active'].sort_values('surr0_kappa_a').tail(8)
print(a[['path','t0','N','rate','kappa_a','surr0_kappa_a','surr1_kappa_a','cv_a','cv_b','cv_c']])
EOF
```

```
cv_a 32448            max  <lambda_0>  <lambda_1>   min  <lambda_2>
phase                                                   
active   34.29       10.38        6.50  2.80        3.16
nni_a    25.82       15.87        6.12  2.91        3.09
nni_b    23.58        8.08        6.03  2.95        3.13
passive  48.34        6.78        5.22  2.90        3.09
cv_b 10056            max  <lambda_0>  <lambda_1>   min  <lambda_2>
phase                                                   
active    8.53        6.98        6.15  2.99        3.13
nni_a    10.30        8.66        6.50  2.92        3.12
nni_b     8.81        8.30        6.49  2.95        3.12
passive   6.82        6.17        5.08  2.90        3.08
cv_c 32227            max  <lambda_0>  <lambda_1>   min  <lambda_2>
phase                                                   
active   34.29        9.18        6.27  2.80        3.15
nni_a    25.82       15.87        6.12  2.91        3.09
nni_b    23.58        8.08        6.03  2.95        3.13
passive  12.21        6.62        5.17  2.90        3.09
                                                path  ...       cv_c
34870  sub-548720/sub-548720_ses-20210203T214934.nwb  ...   4.850098
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025 && cat >> criticality.py <<'EOF'


# ----------------------------------------------------------------------------- analysis

def window_table(results):
    """All windows of all sessions as a table (the real-space results stay in the records)."""
    import pandas as pd
    rows = []
    for r in results:
        for w in r["windows"]:
            rows.append({k: v for k, v in w.items() if k not in ("rs", "surr_rs")})
    return pd.DataFrame(rows)


def session_trials(r, autoreward="a", anchor="change"):
    """Go trials with an outcome (O5): change trials that are hits or misses; catch and aborted
    trials left out. Auto-rewarded trials (a) left out or (b) kept as hits. Each trial is placed
    at its change time (main) or its start time (variant). Returns (times, hit) arrays."""
    t = r["trials"]
    go = t["go"].astype(bool) & ~t["aborted"].astype(bool) & (t["hit"].astype(bool)
                                                             | t["miss"].astype(bool))
    auto = t["auto_rewarded"].astype(bool) & ~t["aborted"].astype(bool)
    keep = go | auto if autoreward == "b" else go
    times = t["change_time_no_display_delay"] if anchor == "change" else t["start_time"]
    hit = t["hit"].astype(bool) | (auto if autoreward == "b" else False)
    return np.asarray(times)[keep], np.asarray(hit)[keep].astype(int)


def trials_per_window(t0s, t1s, times, hit):
    """Hits and trials per window [t0, t1); trials outside every window are dropped."""
    h = np.zeros(len(t0s), int)
    n = np.zeros(len(t0s), int)
    order = np.argsort(t0s)
    s0, s1 = np.asarray(t0s)[order], np.asarray(t1s)[order]
    for tt, hh in zip(times, hit):
        if not np.isfinite(tt):
            continue
        i = np.searchsorted(s0, tt, side="right") - 1
        if i >= 0 and tt < s1[i]:
            n[order[i]] += 1
            h[order[i]] += hh
    return h, n


def hit_curves(kappa, h, n, grid):
    """Eqs. 11 and 12: pooled hit rate over windows above and below each threshold."""
    o = np.argsort(kappa)
    k, hh, nn = kappa[o], h[o].astype(float), n[o].astype(float)
    ch, cn = np.r_[0, np.cumsum(hh)], np.r_[0, np.cumsum(nn)]
    cut = np.searchsorted(k, grid, side="right")     # windows <= th are below
    hb, nb = ch[cut], cn[cut]
    ha, na = ch[-1] - hb, cn[-1] - nb
    with np.errstate(invalid="ignore", divide="ignore"):
        hra, hrb = ha / na, hb / nb
    return hra, hrb, na, nb


def boot_curves(kappa, h, n, grid, rng, B=10_000, chunk=1000, reading="a"):
    """Bootstrap SEs over windows (Appendix 5) of the scaling and no-scaling hit rates and of
    the relative gain (Eq. 13; O8 (c)). Resamples use Poisson(1) weights per window (the
    Poisson bootstrap, which draws each subset with replacement at random size; a standard
    approximation that lets one draw serve every threshold). Reading (a): the pooled hit rate
    of each resample; (b): the mean of the resampled windows' own hit rates (windows with
    trials only)."""
    o = np.argsort(kappa)
    k, hh, nn = kappa[o], h[o].astype(float), n[o].astype(float)
    if reading == "b":
        m = nn > 0
        k, hh, nn = k[m], hh[m] / nn[m], np.ones(m.sum())
    cut = np.searchsorted(k, grid, side="right")
    out_a, out_b, out_g = [], [], []
    for start in range(0, B, chunk):
        b = min(chunk, B - start)
        Wt = rng.poisson(1.0, size=(b, len(k))).astype(np.float32)
        ch = np.concatenate([np.zeros((b, 1), np.float32), np.cumsum(Wt * hh, 1)], 1)
        cn = np.concatenate([np.zeros((b, 1), np.float32), np.cumsum(Wt * nn, 1)], 1)
        hb, nb = ch[:, cut], cn[:, cut]
        ha, na = ch[:, -1:] - hb, cn[:, -1:] - nb
        with np.errstate(invalid="ignore", divide="ignore"):
            ra, rb = ha / na, hb / nb
            out_a.append(ra)
            out_b.append(rb)
            out_g.append((ra - rb) / rb)
    A, Bn, G = (np.concatenate(x, 0) for x in (out_a, out_b, out_g))
    with np.errstate(invalid="ignore"):
        return np.nanstd(A, 0), np.nanstd(Bn, 0), np.nanstd(G, 0)


def swap_shuffle(hit, rng, reps):
    """Appendix 6: for each trial, another trial of the session is drawn at random and their
    outcomes are swapped; `reps` independent repetitions (rows)."""
    n = len(hit)
    H = np.tile(hit, (reps, 1))
    rows = np.arange(reps)
    for i in range(n):
        j = rng.integers(0, n, size=reps)
        a, b = H[rows, i].copy(), H[rows, j].copy()
        H[rows, i], H[rows, j] = b, a
    return H


def session_exponents(rss, Ns, reading, agg="a"):
    """Session exponents (O10): (a) the mean over windows of per-window fits, mu only where
    r^2 >= 0.85; (b) one fit to the window quantities averaged over the session's windows."""
    if not rss:
        return dict(alpha=np.nan, beta=np.nan, mu=np.nan, z=np.nan, n_mu=0)
    if agg == "a":
        fs = [fit_exponents(r, N, *reading) for r, N in zip(rss, Ns)]
        mu = [f["mu"] for f in fs if np.isfinite(f["mu_r2"]) and f["mu_r2"] >= MU_R2_MIN]
        return dict(alpha=np.nanmean([f["alpha"] for f in fs]),
                    beta=np.nanmean([f["beta"] for f in fs]),
                    z=np.nanmean([f["z"] for f in fs]),
                    mu=np.mean(mu) if mu else np.nan, n_mu=len(mu))
    f = fit_exponents(average_rs(rss), int(np.median(Ns)), *reading)
    ok = np.isfinite(f["mu_r2"]) and f["mu_r2"] >= MU_R2_MIN
    return dict(alpha=f["alpha"], beta=f["beta"], z=f["z"], mu=f["mu"] if ok else np.nan,
                n_mu=int(ok))
EOF
python -c "import ast;ast.parse(open('criticality.py').read())"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import pickle
res=pickle.load(open('res_98.pkl','rb'))
r=res[0]; print(r.keys()); print(r['trials'].keys()); print(r['spans'])
EOF
```

```
Fri Nov 27 07:55:00 UTC 2026
dict_keys(['meta', 'windows', 'trials', 'blocks', 'spans', 'clock', 'n_units', 'n_good', 'n_default', 'spikes_sorted', 'rates'])
dict_keys(['start_time', 'stop_time', 'go', 'catch', 'aborted', 'auto_rewarded', 'hit', 'miss', 'change_time_no_display_delay'])
{'active': [(26.274262977154944, 3628.805384431677)], 'passive': [(5181.471246994742, 8783.952539551632)], 'nni_a': [(3628.805384431677, 5181.471246994742)], 'nni_b': [(3657.779673228269, 4569.792961006314), (4858.7847132282695, 5157.284359154284)]}
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part1.py",
 "content": "# %% [md]\n# Reproducing Cambrainha et al. (2025) from dandiset 000713\n\n**Paper.** Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), \"Criticality at Work: Scaling in the Mouse Cortex Enhances Performance\", PRX Life, doi:10.1103/w49n-2vz8. The claims file (`claims/cambrainha-2025.yaml`) was written from the arXiv preprint 2410.23508 version 2 (15 Sep 2025), with its Appendix and Supplemental Material; codes M1 to M8 and O1 to O11 below refer to the method notes at its top.\n\n**Dataset.** DANDI:000713 (Allen Institute, Visual Behavior Neuropixels), version **0.240702.1725** (doi:10.48324/dandi.000713/0.240702.1725). The paper cites the Allen dataset (its ref. 60) without a DANDI version; this is the only published version of the dandiset, and its draft has not changed since (both modified 2024-07-02), so it is pinned as the most recent published version. The files are streamed from the archive; nothing is downloaded.\n\n**What is read.** Per session file: the units table (peak channel, quality metrics, spike times of V1 units only), the electrodes table (structure of each channel), the stimulus presentation tables (stimulus blocks, image onsets and omitted flashes) and the trials table. The probe LFP files are not read.\n\n| claim | tested |\n|---|---|\n| sessions-selected | tested |\n| fig3a-kurtosis-broader-than-surrogate | tested |\n| fig3c-scaling-hit-rate-higher | tested |\n| fig3c-hit-rate-rises-with-threshold | tested |\n| fig3d-relative-gain-24 | tested |\n| figs1-other-window-lengths | tested |\n| figs2-strict-units | tested |\n| fig4a-active-most-scaling | tested |\n| fig4-exponents-active | tested |\n| fig4-exponents-passive | tested |\n| fig4-exponents-nni | tested |\n| fig4bc-static-exponents-trend | tested |\n| figs3-exponents-stable-with-threshold | tested |\n| figs4-initial-kurtosis-poor-predictor | tested |\n| figs5a-firing-rate-order | tested |\n| figs5c-hit-rate-firing-rate-nonmonotonic | tested |\n| figs7-fatigue-halves | tested |\n| figs8-halves-and-phase-order | tested |\n\nEvery claim is tested; none is blocked. The outcomes are in the summary at the end.\n\n# %%\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"MKL_NUM_THREADS\", \"1\")\nimport time\nimport zlib\nimport itertools\nimport resource\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy import stats\n\nimport criticality as cr\n\nPAPER = \"cambrainha-2025\"\n\n\ndef seed(claim):\n    \"\"\"The claim's seed (protocol, author step 3).\"\"\"\n    return zlib.crc32(f\"{PAPER}/{claim}\".encode())\n\n\nSEED_OFFSETS = [0, 1000, 2000, 3000, 4000]\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\nT_START = time.time()\nprint(\"dandiset\", cr.DANDISET_ID, \"version\", cr.DANDISET_VERSION)\n\n# %% [md]\n## Survey of the dataset\n\nEvery session file is opened and its units, electrodes and trials tables are read (metadata and array shapes, not spike times). The V1 units are those whose peak channel's `location` is `VISp`.\n\n# %%\nassets = cr.session_assets()\nwith ThreadPoolExecutor(12) as ex:\n    survey = pd.DataFrame(list(ex.map(cr.survey, assets)))\nsurvey = survey.sort_values(\"path\").reset_index(drop=True)\nprint(\"session files:\", len(survey), \" subjects:\", survey.subject.nunique())\nprint(\"session types:\", survey.session_type.value_counts().to_dict())\nlocs = sorted(set(l for ls in survey.locations for l in ls))\nprint(\"structures with 'VIS' in their name:\", [l for l in locs if \"VIS\" in l])\nprint(\"duplicated session identifiers:\", int(survey.session.duplicated().sum()),\n      \"; sessions sharing total spike count and unit count:\",\n      int(survey.duplicated([\"total_spikes\", \"n_units\"]).sum()))\nprint(survey[[\"n_units\", \"visp_all\", \"visp_good\", \"visp_default\", \"visp_valid\", \"n_trials\"]]\n      .describe().round(1).to_string())\n\n# %% [md]\n## Processing every session\n\nAll sessions with at least 128 V1 units (reading (a) of O1, counting both > 128 and >= 128) are streamed and analysed window by window: binning, the three CVs (O2), the momentum-space kurtosis under both poolings (O3) and before coarse graining (kappa_0), one ISI-shuffled surrogate per window under the claim's seed and under the four seed variants, and the real-space coarse graining of the real and surrogate (claim seed) windows. Active windows of 10 and 60 s, and the active phase with only `good` units or only default-filter units (for sessions keeping at least 128 of them), are analysed too. Timed on four sessions while preparing (40 s with four processes), the whole was estimated at 17 minutes and 1 GB per process.\n\nThe surrogate is the one of `fig3a-kurtosis-broader-than-surrogate`, and every claim that uses the surrogate takes it from there; the strict-unit surrogate is seeded by `figs2-strict-units`.\n\n# %%\nproc = survey[survey.visp_all >= cr.MIN_UNITS].reset_index(drop=True)\nasset_of = {a[\"path\"]: a for a in assets}\nstrict_of = {r.path: tuple(k for k, c in ((\"good\", r.visp_good), (\"default\", r.visp_default))\n                           if c >= cr.MIN_UNITS) for r in proc.itertuples()}\nt0 = time.time()\nresults = cr.run_sessions([asset_of[p] for p in proc.path],\n                          seed(\"fig3a-kurtosis-broader-than-surrogate\"),\n                          seed(\"figs2-strict-units\"), lambda a: strict_of[a[\"path\"]])\nprint(f\"processed {len(results)} sessions in {(time.time() - t0) / 60:.1f} min;\",\n      \"failed:\", [r[\"meta\"][\"path\"] for r in results if \"error\" in r])\nprint(\"peak memory of a worker (GB):\",\n      round(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e6, 2))\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part2.py",
 "content": "# %% [md]\n## Data check\n\n# %%\n# tags: sanity\nok = [r for r in results if \"error\" not in r]\nW_all = cr.window_table(ok)\nsel_gt = set(proc.path[proc.visp_all > cr.MIN_UNITS])\nprint(\"sessions processed:\", len(ok), \"; with > 128 V1 units (the analysis set):\", len(sel_gt),\n      \"from\", proc[proc.path.isin(sel_gt)].subject.nunique(), \"mice\")\nprint(\"V1 units per analysed session: min\", proc[proc.path.isin(sel_gt)].visp_all.min(),\n      \"median\", proc[proc.path.isin(sel_gt)].visp_all.median(),\n      \"max\", proc[proc.path.isin(sel_gt)].visp_all.max())\nprint(\"spike times sorted within every unit:\", all(r[\"spikes_sorted\"] for r in ok))\n\n# Stimulus blocks: names, order and durations\nblk = []\nfor r in ok:\n    for b, (name, s0, s1, n) in sorted(r[\"blocks\"].items()):\n        blk.append(dict(path=r[\"meta\"][\"path\"], block=b, name=name.split(\"_presentations\")[0],\n                        start=s0, dur_min=(s1 - s0) / 60, n=n))\nblk = pd.DataFrame(blk)\nprint(\"\\nstimulus blocks (minutes), over sessions:\")\nprint(blk.groupby([\"block\", \"name\"]).dur_min.describe()[[\"count\", \"min\", \"50%\", \"max\"]].round(2)\n      .to_string())\n\n# Phases (O4) and windows\ndur = pd.DataFrame([dict(path=r[\"meta\"][\"path\"], **{p: sum(b - a for a, b in s) / 60\n                                                    for p, s in r[\"spans\"].items()})\n                    for r in ok])\nprint(\"\\nphase durations (min):\")\nprint(dur.describe().loc[[\"min\", \"50%\", \"max\"]].round(2).to_string())\nprint(\"\\nwindows per phase, length and unit set:\")\nprint(W_all.groupby([\"phase\", \"length\", \"units\"]).size().to_string())\n\n# Trials\ntt = []\nfor r in ok:\n    t = r[\"trials\"]\n    tt.append(dict(go=int((t[\"go\"] & ~t[\"aborted\"]).sum()), hit=int(t[\"hit\"].sum()),\n                   miss=int(t[\"miss\"].sum()), catch=int(t[\"catch\"].sum()),\n                   aborted=int(t[\"aborted\"].sum()), auto=int(t[\"auto_rewarded\"].sum()),\n                   hit_or_miss_not_go=int(((t[\"hit\"] | t[\"miss\"]) & ~t[\"go\"]).sum()),\n                   go_without_change_time=int(np.isnan(t[\"change_time_no_display_delay\"][t[\"go\"]]).sum()),\n                   last_trial_end_min=(t[\"stop_time\"].max() - r[\"spans\"][\"active\"][0][1]) / 60))\ntt = pd.DataFrame(tt)\nprint(\"\\ntrials per session:\")\nprint(tt.describe().loc[[\"min\", \"50%\", \"max\"]].round(2).to_string())\nprint(\"hits + misses equal the non-aborted go trials in every session:\",\n      bool(((tt.hit + tt.miss) == tt.go).all()))\n\n# Units and rates\nprint(\"\\nV1 unit firing rate, spikes per 50-ms bin per unit, averaged over a window: \"\n      f\"min {W_all.rate.min():.3f}, median {W_all.rate.median():.3f}, max {W_all.rate.max():.3f}\")\nprint(\"units silent in a 30-s window (left out of that window): median\",\n      W_all[W_all.length == 30].n_silent.median(), \"max\", W_all[W_all.length == 30].n_silent.max(),\n      \"; units kept per window: min\", W_all[W_all.length == 30].N.min())\n\n# Clock check: response of V1 to image onsets, shown against omitted flashes\nclk = pd.DataFrame([dict(path=r[\"meta\"][\"path\"], **r[\"clock\"]) for r in ok])\nclk[\"z\"] = (clk.shown_mean - clk.omitted_mean) / np.sqrt(clk.shown_sd ** 2 / clk.n_shown\n                                                       + clk.omitted_sd ** 2 / clk.n_omitted)\nprint(\"\\nclock check (V1 spikes 30-130 ms after an image onset minus the 100 ms before):\")\nprint(f\"  shown images: median over sessions {clk.shown_mean.median():.1f} spikes;\"\n      f\" omitted flashes: {clk.omitted_mean.median():.1f};\"\n      f\" sessions where shown exceeds omitted by more than 5 SE: {(clk.z > 5).sum()} of {len(clk)};\"\n      f\" smallest z {clk.z.min():.1f}\")\n\n# CV exclusions (O2)\nW30 = W_all[(W_all.length == 30) & (W_all.units == \"all\") & W_all.path.isin(sel_gt)]\nfor cv in [\"cv_a\", \"cv_b\", \"cv_c\"]:\n    print(f\"windows with {cv} > 5:\",\n          W30.groupby(\"phase\")[cv].apply(lambda x: f\"{(x > 5).sum()} of {len(x)}\").to_dict())\n\n# %% [md]\nThe checks above show:\n\n- 153 session files from 81 mice, no session deposited twice (identifiers unique, and no two sessions share their unit and spike counts).\n- Every session has the blocks the paper describes, but in a different order from the Appendix: block 0 is the active task (about 60 min), then a 10-s gray screen, the Gabor block (about 15 min), a gray screen of about 5 min, the full-field flashes (about 5 min), and block 5, the passive replay (about 60 min). The Appendix says the gray screen comes last, after the flashes; the files put it between the Gabors and the flashes.\n- Hits and misses together are the non-aborted go trials; auto-rewarded trials are flagged apart and are not go trials.\n- Image onsets of the active block evoke a V1 response 30 to 130 ms later and omitted flashes do not, in every session, so the spike times and the stimulus tables share a clock. The trials table is on the same clock as the stimulus table (both from the same stimulus frames); its change times fall inside the active block (checked below when trials are placed in windows).\n\n# %% [md]\n## Common definitions\n\nThe analysis set is the sessions with more than 128 V1 units (O1 (a)). Readings named in the claims file are run as combinations: O2 (`cv` a, b, c), O3 (`kappa` a, b), O5 (auto-rewarded trials a, b), O6 (`surr_max` over the phase or over all phases). The first reading listed in the claims file is the main one (O2 (a), O3 (a), O5 (a), O6 (a), O4 (a)).\n\n# %%\nW = W_all[(W_all.units == \"all\") & W_all.path.isin(sel_gt)].copy()\nmouse_of = dict(zip(survey.path, survey.subject))\nW[\"mouse\"] = W.path.map(mouse_of)\nres_of = {r[\"meta\"][\"path\"]: r for r in ok}\nCVS, KAPS, AUTOS, SMAXS = [\"a\", \"b\", \"c\"], [\"a\", \"b\"], [\"a\", \"b\"], [\"a\", \"b\"]\nGRID_STEP = 0.05\n\n\ndef kept(df, cv):\n    return df[df[f\"cv_{cv}\"] <= cr.CV_MAX]\n\n\ndef surr_max(cv, kap, smax, s=0, nni=\"nni_a\"):\n    \"\"\"kappa_surr_max (O6): (a) over the active phase's kept windows, (b) over all phases.\"\"\"\n    d = kept(W[W.length == 30], cv)\n    phases = [\"active\"] if smax == \"a\" else [\"active\", \"passive\", nni]\n    return d[d.phase.isin(phases)][f\"surr{s}_kappa_{kap}\"].max()\n\n\ndef grid(lo, hi):\n    lo = np.ceil(lo / GRID_STEP - 1e-9) * GRID_STEP\n    return np.round(np.arange(lo, hi + 1e-9, GRID_STEP), 4)\n\n\n# Trials placed in active windows, per session and reading (O5); change time is the main anchor\ndef add_trials(df, auto=\"a\", anchor=\"change\"):\n    h = np.zeros(len(df), int)\n    n = np.zeros(len(df), int)\n    out_of_window = 0\n    for p, idx in df.groupby(\"path\").indices.items():\n        times, hit = cr.session_trials(res_of[p], auto, anchor)\n        hh, nn = cr.trials_per_window(df.t0.values[idx], df.t1.values[idx], times, hit)\n        h[idx], n[idx] = hh, nn\n        out_of_window += len(times) - nn.sum()\n    d = df.copy()\n    d[\"hits\"], d[\"trials\"] = h, n\n    return d, out_of_window\n\n\nACT = W[(W.phase == \"active\") & (W.length == 30)].reset_index(drop=True)\nfor auto in AUTOS:\n    d, lost = add_trials(ACT, auto)\n    ACT[f\"hits_{auto}\"], ACT[f\"trials_{auto}\"] = d.hits, d.trials\n    print(f\"O5 ({auto}): trials placed in active windows {d.trials.sum()}, hits {d.hits.sum()}, \"\n          f\"trials outside every window {lost}; overall hit rate {d.hits.sum() / d.trials.sum():.3f}\")\nprint(\"trials per active window: median\", np.median(ACT.trials_a), \"range\", ACT.trials_a.min(), \"to\",\n      ACT.trials_a.max())\nprint(\"\\nkappa_surr_max under each reading (claim seed):\")\nprint(pd.DataFrame([dict(cv=cv, kappa=k, O6=s, kappa_surr_max=round(surr_max(cv, k, s), 3))\n                    for cv in CVS for k in KAPS for s in SMAXS]).to_string(index=False))\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > dev.py <<'EOF'
import sys, re, pickle, os
sys.path.insert(0,'entries/cambrainha-2025')
os.chdir('/tmp/claude-1001')
def cells(fn):
    txt=open(fn).read(); parts=re.split(r'^# %%(.*)$', txt, flags=re.M)
    out=[]
    for i in range(1,len(parts),2):
        out.append((parts[i].strip(), parts[i+1]))
    return out
c1=cells('nb_part1.py')
g={}
code=[c for h,c in c1 if not h.startswith('[md]')]
exec(code[0], g)
import pandas as pd
sv=pd.read_csv('survey.csv').rename(columns={'visp':'visp_all','ecephys_id':'session'})
sv['visp_valid']=sv.visp_all; sv['locations']=[['VISp']]*len(sv)
g['survey']=sv.sort_values('path').reset_index(drop=True)
g['proc']=g['survey'][g['survey'].visp_all>=128].reset_index(drop=True)
g['results']=pickle.load(open('res_98.pkl','rb'))
g['assets']=[]
if os.path.exists('state.pkl') and len(sys.argv)>2:
    pass
for fn in sys.argv[1:]:
    for h,c in cells(fn):
        if h.startswith('[md]'): continue
        exec(c, g)
EOF
. venv/bin/activate && time python dev.py nb_part2.py 2>&1 | tail -80
```

```
dandiset 000713 version 0.240702.1725
sessions processed: 98 ; with > 128 V1 units (the analysis set): 97 from 68 mice
V1 units per analysed session: min 130 median 164.0 max 294
spike times sorted within every unit: True

stimulus blocks (minutes), over sessions:
                                                   count    min    50%    max
block name                                                                   
0     Natural_Images_Lum_Matched_set_ophys_G_2019   58.0  60.00  60.08  60.19
      Natural_Images_Lum_Matched_set_ophys_H_2019   40.0  59.99  60.06  60.19
1     spontaneous                                   98.0   0.17   0.17   0.17
2     gabor_20_deg_250ms                            98.0  15.20  15.20  15.20
3     spontaneous                                   98.0   4.82   4.82   4.82
4     flash_250ms                                   98.0   4.97   4.98   4.98
5     Natural_Images_Lum_Matched_set_ophys_G_2019   58.0  60.00  60.07  60.19
      Natural_Images_Lum_Matched_set_ophys_H_2019   40.0  59.99  60.06  60.19

phase durations (min):
     active  passive  nni_a  nni_b
min   59.99    59.99  25.86  20.18
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import pandas as pd, numpy as np
W=pd.read_pickle('W.pkl'); W=W[(W.length==30)&(W.units=='all')]
print(W.sort_values('surr0_kappa_a').tail(12)[['path','phase','t0','N','n_silent','rate','spikes','kappa_a','surr0_kappa_a','surr1_kappa_a','cv_a','cv_c']].to_string())
print((W.N<64).sum(), W[W.N<64].path.value_counts().head())
print(np.corrcoef(W.N, W.surr0_kappa_a)[0,1])
EOF
```

```
path    phase           t0    N  n_silent      rate  spikes    kappa_a  surr0_kappa_a  surr1_kappa_a      cv_a       cv_c
10831  sub-527294/sub-527294_ses-20200827T213926.nwb   active   123.203364    3       203  0.000688      85  16.557085      16.207111      13.618768  2.895528  43.955900
52772  sub-560962/sub-560962_ses-20210428T204143.nwb    nni_a  3628.929832  157        26  0.124235   13641  20.914201      17.540217      11.788775  0.474185   3.622153
16720  sub-536211/sub-536211_ses-20201028T205130.nwb    nni_a  4830.421301  127        21  0.117590   10442  28.370648      18.621678      23.230762  0.770019   3.316562
57160  sub-563326/sub-563326_ses-20210505T201456.nwb    nni_a  4769.350454  150        17  0.125639   12589  26.760961      18.878550      14.790521  0.815027   4.083430
16715  sub-536211/sub-536211_ses-20201028T205130.nwb    nni_a  4680.421301  130        18  0.133423   11848  36.292849      19.473831      20.541117  0.737564   3.161196
10830  sub-527294/sub-527294_ses-20200827T213926.nwb   active    93.203364  199         7  0.137816   17034  36.763126      22.890934      22.467263  1.643040   5.242372
25969  sub-544838/sub-544838_ses-20201123T233032.nwb    nni_b  4502.630691  130         4  0.184254   14814  19.343725      23.577303       9.335969  0.601746   2.948304
16713  sub-536211/sub-536211_ses-20201028T205130.nwb    nni_a  4620.421301  131        17  0.130890   11623  27.362235      25.816971      25.561774  0.748142   3.176833
30652  sub-546508/sub-546508_ses-20210128T225050.nwb   active   688.267593  131        26  0.116783   11001  39.485220      26.939861      25.149579  2.621465   6.937578
1658   sub-510589/sub-510589_ses-20200819T222405.nwb   active  1167.613733  182        45  0.169831   23131  22.663552      34.292115      16.203110  0.528741   3.375155
26521  sub-545994/sub-545994_ses-20201209T215912.nwb  passive  5243.164171   12       159  0.001706     175  39.273810      36.497244      41.839888  3.167050  40.956712
26520  s
[... 7 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part3.py",
 "content": "# %% [md]\nThe two poolings of O3 give the same number: psi is normalised to unit variance for every unit (Eq. 5), so the pooled <psi^4>/<psi^2>^2 is the mean of the units' fourth moments, which is the mean of their kurtoses. The check below confirms it, and the analyses use reading (a) alone.\n\n# %%\nd = W[W.length == 30]\nprint(\"largest |kappa_a - kappa_b| over windows:\", float(np.abs(d.kappa_a - d.kappa_b).max()),\n      \"; surrogate:\", float(np.abs(d.surr0_kappa_a - d.surr0_kappa_b).max()))\n\n# %% [md]\n## sessions-selected\n\n> Of the dataset's sessions, 62 (from 44 mice) have more than 128 recorded V1 units, and these are the sessions analysed.\n\nCriterion: V1 units counted per session under O1 (a) (all units) and (b) (the dataset's default quality filters), with > 128 and >= 128; reproduced when, under one reading, both counts are within tolerance (62 +/- 6.2 sessions, 44 +/- 4.4 mice). The `good` label and the valid-channel flag are shown as variants.\n\n# %%\n# tags: claim:sessions-selected\nrows = []\nfor col, label in [(\"visp_all\", \"O1 (a) all V1 units\"), (\"visp_default\", \"O1 (b) default quality filters\"),\n                   (\"visp_good\", \"variant: quality == good\"), (\"visp_valid\", \"variant: on valid channels\"),\n                   (\"visp_good_valid\", \"variant: good and on valid channels\")]:\n    if col not in survey:\n        continue\n    for op in [\">\", \">=\"]:\n        m = survey[col] > cr.MIN_UNITS if op == \">\" else survey[col] >= cr.MIN_UNITS\n        ns, nm = int(m.sum()), survey[m].subject.nunique()\n        rows.append(dict(reading=label, rule=f\"{op} 128\", sessions=ns, mice=nm,\n                         sessions_ok=abs(ns - 62) <= 6.2, mice_ok=abs(nm - 44) <= 4.4))\nsel_tab = pd.DataFrame(rows)\nprint(sel_tab.to_string(index=False))\nmain_rows = sel_tab[sel_tab.reading.str.startswith(\"O1\")]\nprint(\"\\nreproduced under a reading of the criterion:\",\n      bool((main_rows.sessions_ok & main_rows.mice_ok).any()))\nprint(\"V1 units per session over all 153: quantiles 10/50/90 %:\",\n      survey.visp_all.quantile([.1, .5, .9]).tolist(), \"; sessions with no V1 unit:\",\n      int((survey.visp_all == 0).sum()))\n\n# %% [md]\n**Result: not reproduced.** No reading gives both counts: all V1 units give 97 sessions from 68 mice (> 128), the default quality filters leave a single session, and the `good` label (a variant) gives 68 sessions, within tolerance of 62, but from 54 mice, out of tolerance of 44. The analyses below use the 97 sessions of reading (a).\n\n# %% [md]\n## fig3a-kurtosis-broader-than-surrogate\n\n> Across windows of all sessions, the kurtosis of the coarse-grained activity spans a broad range that overlaps the surrogate distribution and extends well above it; some windows have kurtosis well above any surrogate value, others look like surrogates. Surrogate kurtoses are lowest around 6.\n\nCriterion: per window kurtosis (M1 to M3, readings O2 and O3), the active phase (all phases pooled as a variant). The lowest surrogate kurtoses, as (a) the minimum or (b) the 5th percentile, within 6 +/- 0.6; the real windows' IQR larger than the surrogate's; some real windows below kappa_surr_max (O6) and a majority above it. Partially reproduced when the spread is larger and some windows exceed kappa_surr_max but the lowest surrogate kurtoses are out of tolerance.\n\n# %%\n# tags: claim:fig3a-kurtosis-broader-than-surrogate\n\n\ndef fig3a_row(cv, smax, s=0, phases=(\"active\",)):\n    d = kept(W[(W.length == 30) & W.phase.isin(phases)], cv)\n    real, sur = d.kappa_a.values, d[f\"surr{s}_kappa_a\"].values\n    ksm = surr_max(cv, \"a\", smax, s)\n    iqr = lambda x: np.subtract(*np.percentile(x, [75, 25]))\n    return dict(cv=cv, O6=smax, seed_offset=SEED_OFFSETS[s], phases=\"+\".join(phases),\n                windows=len(d), surr_min=sur.min(), surr_p5=np.percentile(sur, 5),\n                surr_median=np.median(sur), kappa_surr_max=ksm, real_median=np.median(real),\n                real_p95=np.percentile(real, 95), real_max=real.max(), iqr_real=iqr(real),\n                iqr_surr=iqr(sur), frac_below_ksm=np.mean(real < ksm), frac_above_ksm=np.mean(real > ksm))\n\n\nf3a = pd.DataFrame([fig3a_row(cv, sm) for cv in CVS for sm in SMAXS])\nf3a_all = pd.DataFrame([fig3a_row(cv, sm, phases=(\"active\", \"passive\", \"nni_a\"))\n                        for cv in CVS for sm in SMAXS])\nfor t in (f3a, f3a_all):\n    t[\"lowest_min_ok\"] = (t.surr_min - 6).abs() <= 0.6\n    t[\"lowest_p5_ok\"] = (t.surr_p5 - 6).abs() <= 0.6\n    t[\"spread_larger\"] = t.iqr_real > t.iqr_surr\n    t[\"some_below\"] = t.frac_below_ksm > 0\n    t[\"majority_above\"] = t.frac_above_ksm > 0.5\n    t[\"some_above\"] = t.frac_above_ksm > 0\nprint(\"active phase:\")\nprint(f3a.round(3).to_string(index=False))\nprint(\"\\nvariant, all phases pooled:\")\nprint(f3a_all.round(3).to_string(index=False))\nfull = (f3a.lowest_min_ok | f3a.lowest_p5_ok) & f3a.spread_larger & f3a.some_below & f3a.majority_above\npart = f3a.spread_larger & f3a.some_above\nprint(\"\\nreproduced under some reading:\", bool(full.any()), \"; partial conditions under some reading:\",\n      bool(part.any()))\nprint(\"\\nseed variants (main reading, cv a, O6 a):\")\nf3a_seeds = pd.DataFrame([fig3a_row(\"a\", \"a\", s) for s in range(5)])\nprint(f3a_seeds[[\"seed_offset\", \"surr_min\", \"surr_p5\", \"kappa_surr_max\", \"frac_above_ksm\"]].round(3)\n      .to_string(index=False))\nprint(\"\\nkappa_surr_max per reading and seed:\")\nprint(pd.DataFrame([dict(cv=cv, O6=sm, **{f\"+{SEED_OFFSETS[s]}\": round(surr_max(cv, \"a\", sm, s), 2)\n                                         for s in range(5)}) for cv in CVS for sm in SMAXS])\n      .to_string(index=False))\nprint(\"\\nreal and surrogate kurtosis by session (active, cv a): sessions whose largest real window \"\n      \"exceeds their largest surrogate:\",\n      int((W[(W.length == 30) & (W.phase == \"active\")].groupby(\"path\")\n           .apply(lambda g: g.kappa_a.max() > g.surr0_kappa_a.max())).sum()), \"of\", len(sel_gt))\n\nfig, ax = plt.subplots(figsize=(6, 3.5))\nd = W[(W.length == 30) & (W.phase == \"active\")]\nbins = np.linspace(2, 15, 131)\nax.hist(d.surr0_kappa_a, bins, density=True, alpha=.6, label=\"surrogate\")\nax.hist(d.kappa_a, bins, density=True, histtype=\"step\", color=\"k\", label=\"data\")\nax.set_xlabel(\"kappa (N/16)\")\nax.set_ylabel(\"density\")\nax.legend()\nprint(\"windows outside the plotted range 2 to 15: data\", int(((d.kappa_a < 2) | (d.kappa_a > 15)).sum()),\n      \", surrogate\", int(((d.surr0_kappa_a < 2) | (d.surr0_kappa_a > 15)).sum()), \"of\", len(d))\nplt.show()\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part3.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && MPLBACKEND=Agg python dev.py nb_part2.py nb_part3.py 2>&1 | sed -n '/largest |kappa/,$p'
```

```
largest |kappa_a - kappa_b| over windows: 1.4210854715202004e-14 ; surrogate: 8.881784197001252e-15
                       reading   rule  sessions  mice  sessions_ok  mice_ok
           O1 (a) all V1 units  > 128        97    68        False    False
           O1 (a) all V1 units >= 128        98    68        False    False
O1 (b) default quality filters  > 128         1     1        False    False
O1 (b) default quality filters >= 128         1     1        False    False
      variant: quality == good  > 128        68    54         True    False
      variant: quality == good >= 128        70    55        False    False
    variant: on valid channels  > 128        97    68        False    False
    variant: on valid channels >= 128        98    68        False    False

reproduced under a reading of the criterion: False
V1 units per session over all 153: quantiles 10/50/90 %: [79.0, 144.0, 197.8] ; sessions with no V1 unit: 2
active phase:
cv O6  seed_offset phases  windows  surr_min  surr_p5  surr_median  kappa_surr_max  real_median  real_p95  real_max  iqr_real  iqr_surr  frac_below_ksm  frac_above_ksm  lowest_min_ok  lowest_p5_ok  spread_larger  some_below  majority_above  some_above
 a  a            0 active    11639     2.804    3.156        3.639          34.292        6.184    10.116    89.806     1.981     0.643           1.000           0.000          False         False           True        True           False        True
 a  b            0 active    11639     2.804    3.156        3.639          48.341        6.184    10.116    89.806     1.981     0.643           1.000           0.000          False         False           True        True           False        True
 b  a            0 active     1937     2.985    3.133        3.525           8.532        5.950     8.626    19.254     1.551     0.518           0.945           0.055          False         False           True        True           False        True
 b  b            0 active     1937
[... 34 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part4.py",
 "content": "# %% [md]\n## fig3c-scaling-hit-rate-higher\n\n> In the active phase, for any kurtosis threshold above the surrogate values, the hit rate pooled over scaling windows is higher than over no-scaling windows and higher than the trial-shuffled control.\n\nCriterion: hit rates as in M5 (Eqs. 11 and 12), the trial shuffle of M6 (500 repetitions), active windows with trials as in O5, at each kappa_th of the grid of O7 (step 0.05) from kappa_surr_max (O6) to 12.5. Reproduced when, under one reading, the scaling hit rate exceeds both the no-scaling hit rate and the mean trial-shuffled hit rate at every grid point; partially reproduced when it holds at 90% or more of points and every failure is within one bootstrap SE (O8) of the comparator; not reproduced otherwise. A reading whose grid is empty (kappa_surr_max above 12.5) cannot meet the criterion. The SE used for a failure is the bootstrap SE of the scaling hit rate (reading (a) of O8), 10^4 resamples. Trials are placed by change time; the trial start is shown as a variant.\n\n# %%\n# tags: claim:fig3c-scaling-hit-rate-higher\nREPS = 500\n\n\ndef shuffled_hits(df, auto, rng, reps=REPS):\n    \"\"\"Per window, the hits of each trial-shuffle repetition (Appendix 6); reps x windows.\"\"\"\n    out = np.zeros((reps, len(df)))\n    for p, idx in df.groupby(\"path\").indices.items():\n        times, hit = cr.session_trials(res_of[p], auto)\n        H = cr.swap_shuffle(hit, rng, reps)\n        o = np.argsort(df.t0.values[idx])\n        s0, s1 = df.t0.values[idx][o], df.t1.values[idx][o]\n        wi = np.searchsorted(s0, times, side=\"right\") - 1\n        inside = (wi >= 0) & (times < s1[np.clip(wi, 0, None)])\n        for k in np.where(inside)[0]:\n            out[:, idx[o[wi[k]]]] += H[:, k]\n    return out\n\n\ndef shuffled_curve(kappa, SH, n, g):\n    o = np.argsort(kappa)\n    k = kappa[o]\n    cut = np.searchsorted(k, g, side=\"right\")\n    csh = np.concatenate([np.zeros((SH.shape[0], 1)), np.cumsum(SH[:, o], 1)], 1)\n    cn = np.r_[0, np.cumsum(n[o])]\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        r = (csh[:, -1:] - csh[:, cut]) / (cn[-1] - cn[cut])\n    return np.nanmean(r, 0), np.nanstd(r, 0)\n\n\ndef fig3c_eval(df, cv, auto, smax, rng_sh, rng_bs, ksm=None, hi=12.5, sh_cache=None):\n    d = kept(df, cv).reset_index(drop=True)\n    ksm = surr_max(cv, \"a\", smax) if ksm is None else ksm\n    g = grid(ksm, hi)\n    out = dict(cv=cv, auto=auto, O6=smax, kappa_surr_max=ksm, grid_points=len(g))\n    if len(g) == 0:\n        return dict(out, verdict=\"no grid\", frac_pass=np.nan), None\n    k, h, n = d.kappa_a.values, d[f\"hits_{auto}\"].values, d[f\"trials_{auto}\"].values\n    hra, hrb, na, nb = cr.hit_curves(k, h, n, g)\n    SH = shuffled_hits(d, auto, rng_sh) if sh_cache is None else sh_cache(d, auto)\n    shm, shs = shuffled_curve(k, SH, n, g)\n    valid = (na > 0) & (nb > 0)\n    pas = valid & (hra > hrb) & (hra > shm)\n    frac = pas[valid].mean() if valid.any() else np.nan\n    se = cr.boot_curves(k, h, n, g, rng_bs)[0]\n    fails = valid & ~pas\n    within = np.all((np.maximum(hrb, shm) - hra)[fails] <= se[fails]) if fails.any() else True\n    verdict = (\"reproduced\" if valid.any() and pas[valid].all() else\n               \"partially_reproduced\" if frac >= 0.9 and within else \"not_reproduced\")\n    out.update(points_with_trials=int(valid.sum()), frac_pass=frac, failures_within_SE=bool(within),\n               hr_scaling_lo=hra[0], hr_noscaling_lo=hrb[0], hr_shuffled_lo=shm[0],\n               hr_scaling_hi=hra[valid][-1] if valid.any() else np.nan,\n               hr_noscaling_hi=hrb[valid][-1] if valid.any() else np.nan,\n               trials_above_hi=na[valid][-1] if valid.any() else np.nan, verdict=verdict)\n    curves = pd.DataFrame(dict(kappa_th=g, hr_scaling=hra, hr_noscaling=hrb, hr_shuffled=shm,\n                               hr_shuffled_sd=shs, se_scaling=se, trials_above=na, trials_below=nb))\n    return out, curves\n\n\nS3C = seed(\"fig3c-scaling-hit-rate-higher\")\nf3c_rows, f3c_curves = [], {}\nfor cv in CVS:\n    for auto in AUTOS:\n        for sm in SMAXS:\n            row, cur = fig3c_eval(ACT, cv, auto, sm, np.random.default_rng(S3C),\n                                  np.random.default_rng(S3C + 1))\n            f3c_rows.append(row)\n            f3c_curves[(cv, auto, sm)] = cur\nf3c = pd.DataFrame(f3c_rows)\nprint(f3c.round(3).to_string(index=False))\n# The full grid of thresholds (from the lowest kappa), main reading, for the shape of the curves\nrow, cur_full = fig3c_eval(ACT, \"a\", \"a\", \"a\", np.random.default_rng(S3C), np.random.default_rng(S3C + 1),\n                           ksm=3.0, hi=15)\nprint(\"\\nmain reading (cv a, O5 a) on the full range of thresholds 3 to 15 (not the criterion's grid):\")\nprint(cur_full.iloc[::20].round(3).to_string(index=False))\nprint(\"points from 3 to 15 where scaling > no-scaling and > shuffled:\",\n      f\"{row['frac_pass']:.3f} of {row['points_with_trials']}\")\n# Trial start as anchor (variant)\nACT_start = ACT.copy()\nd_, _ = add_trials(ACT, \"a\", anchor=\"start\")\nACT_start[\"hits_a\"], ACT_start[\"trials_a\"] = d_.hits, d_.trials\nrows = []\nfor cv in CVS:\n    rows.append(fig3c_eval(ACT_start, cv, \"a\", \"a\", np.random.default_rng(S3C),\n                           np.random.default_rng(S3C + 1))[0])\nprint(\"\\nvariant, trials placed by start time:\")\nprint(pd.DataFrame(rows)[[\"cv\", \"O6\", \"kappa_surr_max\", \"grid_points\", \"frac_pass\", \"verdict\"]]\n      .round(3).to_string(index=False))\n\n# %%\n# tags: claim:fig3c-scaling-hit-rate-higher\n# Seed variants: the trial shuffle, the bootstrap and kappa_surr_max (surrogate seed variants)\nrows = []\nfor s in range(5):\n    for cv in CVS:\n        for sm in SMAXS:\n            ksm = surr_max(cv, \"a\", sm, s)\n            r, _ = fig3c_eval(ACT, cv, \"a\", sm, np.random.default_rng(S3C + SEED_OFFSETS[s]),\n                              np.random.default_rng(S3C + 1 + SEED_OFFSETS[s]), ksm=ksm)\n            rows.append(dict(seed_offset=SEED_OFFSETS[s], **{k: r[k] for k in\n                                                             [\"cv\", \"O6\", \"kappa_surr_max\", \"grid_points\",\n                                                              \"frac_pass\", \"verdict\"]}))\nf3c_seeds = pd.DataFrame(rows)\nprint(f3c_seeds.round(3).to_string(index=False))\nbest = f3c_seeds.groupby(\"seed_offset\").verdict.apply(\n    lambda v: \"reproduced\" if (v == \"reproduced\").any() else\n    \"partially_reproduced\" if (v == \"partially_reproduced\").any() else \"not_reproduced\")\nprint(\"\\nbest verdict over readings, per seed:\", best.to_dict())\n\nfig, ax = plt.subplots(1, 2, figsize=(10, 3.5))\nc = f3c_curves[(\"b\", \"a\", \"a\")]\nfor a_, cur, title in [(ax[0], cur_full, \"cv a, thresholds 3 to 15\"), (ax[1], c, \"cv b, criterion grid\")]:\n    if cur is None:\n        continue\n    a_.plot(cur.kappa_th, cur.hr_scaling, label=\"scaling\")\n    a_.plot(cur.kappa_th, cur.hr_noscaling, label=\"no scaling\")\n    a_.plot(cur.kappa_th, cur.hr_shuffled, label=\"trial shuffled\")\n    a_.set_xlabel(\"kappa_th\")\n    a_.set_ylabel(\"hit rate\")\n    a_.set_title(title)\n    a_.set_ylim(0, 1)\nax[0].legend()\nplt.show()\nprint(\"plotted hit rates lie in [0, 1]; points without trials are not drawn\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part4.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && time MPLBACKEND=Agg python dev.py nb_part2.py nb_part4.py 2>&1 | sed -n '/kappa_surr_max  grid_points/,$p'
```

```
cv auto O6  kappa_surr_max  grid_points        verdict  frac_pass  points_with_trials failures_within_SE  hr_scaling_lo  hr_noscaling_lo  hr_shuffled_lo  hr_scaling_hi  hr_noscaling_hi  trials_above_hi
 a    a  a          34.292            0        no grid        NaN                 NaN                NaN            NaN              NaN             NaN            NaN              NaN              NaN
 a    a  b          48.341            0        no grid        NaN                 NaN                NaN            NaN              NaN             NaN            NaN              NaN              NaN
 a    b  a          34.292            0        no grid        NaN                 NaN                NaN            NaN              NaN             NaN            NaN              NaN              NaN
 a    b  b          48.341            0        no grid        NaN                 NaN                NaN            NaN              NaN             NaN            NaN              NaN              NaN
 b    a  a           8.532           80 not_reproduced      0.675                80.0              False          0.641            0.600           0.691            1.0            0.602              7.0
 b    a  b          10.302           44     reproduced      1.000                44.0               True          0.778            0.601           0.723            1.0            0.602              7.0
 b    b  a           8.532           80 not_reproduced      0.662                80.0              False          0.647            0.602           0.692            1.0            0.604              7.0
 b    b  b          10.302           44     reproduced      1.000                44.0               True          0.778            0.603           0.733            1.0            0.604              7.0
 c    a  a          34.292            0        no grid        NaN                 NaN                NaN            NaN              NaN             NaN            NaN              N
[... 65 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part5.py",
 "content": "# %% [md]\n## fig3c-hit-rate-rises-with-threshold\n\n> As the threshold rises and only windows of higher kurtosis count as scaling, the hit rate over the scaling windows rises.\n\nCriterion: the scaling hit rate of fig3c-scaling-hit-rate-higher on the grid of O7. Reproduced when the Spearman correlation between kappa_th and the scaling hit rate over the grid from kappa_surr_max to 12.5 is positive and the hit rate at 12.5 exceeds that at kappa_surr_max by more than the sum of their bootstrap SEs (O8). Run under every reading of fig3c-scaling-hit-rate-higher; the bootstrap is this claim's (10^4 resamples).\n\n# %%\n# tags: claim:fig3c-hit-rate-rises-with-threshold\nS3R = seed(\"fig3c-hit-rate-rises-with-threshold\")\n\n\ndef rises_eval(df, cv, auto, smax, rng, ksm=None, hi=12.5, lo_override=None):\n    d = kept(df, cv)\n    ksm = surr_max(cv, \"a\", smax) if ksm is None else ksm\n    g = grid(ksm if lo_override is None else lo_override, hi)\n    out = dict(cv=cv, auto=auto, O6=smax, kappa_surr_max=ksm, lo=g[0] if len(g) else np.nan,\n               grid_points=len(g))\n    if len(g) < 2:\n        return dict(out, verdict=\"no grid\")\n    k, h, n = d.kappa_a.values, d[f\"hits_{auto}\"].values, d[f\"trials_{auto}\"].values\n    hra, _, na, _ = cr.hit_curves(k, h, n, g)\n    se = cr.boot_curves(k, h, n, g, rng)[0]\n    v = np.isfinite(hra)\n    rho = stats.spearmanr(g[v], hra[v])[0]\n    last = np.where(v)[0][-1]\n    diff = hra[last] - hra[0]\n    ok = (rho > 0) and (diff > se[last] + se[0])\n    return dict(out, spearman=rho, hr_lo=hra[0], hr_hi=hra[last], kappa_hi=g[last],\n                trials_hi=na[last], se_lo=se[0], se_hi=se[last], diff=diff,\n                verdict=\"reproduced\" if ok else \"not_reproduced\")\n\n\nrr = pd.DataFrame([rises_eval(ACT, cv, auto, sm, np.random.default_rng(S3R))\n                   for cv in CVS for auto in AUTOS for sm in SMAXS])\nprint(rr.round(3).to_string(index=False))\nprint(\"\\nvariant (not the criterion): main reading over the thresholds 3 to 12.5\")\nprint(pd.DataFrame([rises_eval(ACT, \"a\", \"a\", \"a\", np.random.default_rng(S3R), lo_override=3.0)])\n      .round(3).to_string(index=False))\nrows = []\nfor s in range(5):\n    for cv in CVS:\n        for sm in SMAXS:\n            r = rises_eval(ACT, cv, \"a\", sm, np.random.default_rng(S3R + SEED_OFFSETS[s]),\n                           ksm=surr_max(cv, \"a\", sm, s))\n            rows.append(dict(seed_offset=SEED_OFFSETS[s], cv=cv, O6=sm, grid_points=r[\"grid_points\"],\n                             spearman=r.get(\"spearman\"), diff=r.get(\"diff\"), verdict=r[\"verdict\"]))\nrr_seeds = pd.DataFrame(rows)\nprint(\"\\nseed variants (O5 a):\")\nprint(rr_seeds.round(3).to_string(index=False))\n\n# %% [md]\n## fig3d-relative-gain-24\n\n> The relative performance gain of scaling over no-scaling windows grows with the threshold and reaches up to 24% plus or minus 3%.\n\nCriterion: relative performance (Eq. 13) on the grid of O7 with the readings of O2 to O6. The maximum is taken (a) over the plotted range, kappa_surr_max to 12.5, or (b) over all thresholds at which both scaling and no-scaling windows hold trials. Reproduced when, under one reading, the maximum is within 24 +/- 3 % and the gain at kappa_th = 12 is larger than at kappa_th = 8. The bootstrap SE of the gain (O8 (c)) is shown, with this claim's seed.\n\n# %%\n# tags: claim:fig3d-relative-gain-24\nS3D = seed(\"fig3d-relative-gain-24\")\nrows = []\nfor cv in CVS:\n    d = kept(ACT, cv)\n    k = d.kappa_a.values\n    for auto in AUTOS:\n        h, n = d[f\"hits_{auto}\"].values, d[f\"trials_{auto}\"].values\n        gall = grid(np.floor(k.min() * 20) / 20, np.ceil(k.max() * 20) / 20)\n        hra, hrb, na, nb = cr.hit_curves(k, h, n, gall)\n        gain = (hra - hrb) / hrb * 100\n        both = (na > 0) & (nb > 0)\n        g8, g12 = gain[np.isclose(gall, 8)][0], gain[np.isclose(gall, 12)][0]\n        for sm in SMAXS:\n            ksm = surr_max(cv, \"a\", sm)\n            inr = both & (gall >= ksm - 1e-9) & (gall <= 12.5 + 1e-9)\n            for rng_name, m in [(\"a plotted range\", inr), (\"b all thresholds\", both)]:\n                if m.any():\n                    i = np.where(m)[0][np.nanargmax(gain[m])]\n                    mx, at, nab = gain[i], gall[i], na[i]\n                else:\n                    mx, at, nab = np.nan, np.nan, np.nan\n                ok = np.isfinite(mx) and abs(mx - 24) <= 3 and g12 > g8\n                rows.append(dict(cv=cv, auto=auto, O6=sm, range=rng_name, kappa_surr_max=ksm,\n                                 max_gain_pct=mx, at_kappa=at, trials_above_at_max=nab,\n                                 gain8_pct=g8, gain12_pct=g12, verdict=\"reproduced\" if ok else \"not_reproduced\"))\nf3d = pd.DataFrame(rows)\nprint(f3d.round(2).to_string(index=False))\nd = kept(ACT, \"a\")\nk, h, n = d.kappa_a.values, d.hits_a.values, d.trials_a.values\ng = grid(3, 15)\nhra, hrb, na, nb = cr.hit_curves(k, h, n, g)\nse_g = cr.boot_curves(k, h, n, g, np.random.default_rng(S3D))[2]\ngain = (hra - hrb) / hrb * 100\nprint(\"\\nmain reading (cv a, O5 a): relative gain (%) and its bootstrap SE (%) at thresholds 3 to 15\")\nprint(pd.DataFrame(dict(kappa_th=g, gain_pct=gain, se_pct=se_g * 100, trials_above=na)).iloc[::20]\n      .round(2).to_string(index=False))\nprint(\"range of the gain over 4 to 15 (%):\", np.nanmin(gain[g >= 4]).round(2), \"to\",\n      np.nanmax(gain[g >= 4]).round(2))\nrows = []\nfor s in range(5):\n    for cv in CVS:\n        for sm in SMAXS:\n            ksm = surr_max(cv, \"a\", sm, s)\n            sub = f3d[(f3d.cv == cv) & (f3d.O6 == sm) & (f3d.auto == \"a\")]\n            dd = kept(ACT, cv)\n            kk, hh, nn = dd.kappa_a.values, dd.hits_a.values, dd.trials_a.values\n            gg = grid(ksm, 12.5)\n            if len(gg):\n                a_, b_, na_, nb_ = cr.hit_curves(kk, hh, nn, gg)\n                gn = (a_ - b_) / b_ * 100\n                mx = np.nanmax(np.where((na_ > 0) & (nb_ > 0), gn, np.nan))\n            else:\n                mx = np.nan\n            rows.append(dict(seed_offset=SEED_OFFSETS[s], cv=cv, O6=sm, kappa_surr_max=ksm,\n                             max_gain_plotted_range=mx))\nprint(\"\\nseed variants of kappa_surr_max (reading (a) of the range, O5 a):\")\nprint(pd.DataFrame(rows).round(2).to_string(index=False))\nfig, ax = plt.subplots(figsize=(6, 3.5))\nax.plot(g, gain)\nax.fill_between(g, gain - se_g * 100, gain + se_g * 100, alpha=.3)\nax.axhline(0, color=\"k\", lw=.5)\nax.set_xlabel(\"kappa_th\")\nax.set_ylabel(\"relative gain (%)\")\nax.set_ylim(-60, 60)\nprint(\"points of the plotted gain outside -60 to 60 %:\", int(((gain < -60) | (gain > 60)).sum()))\nplt.show()\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part5.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && time MPLBACKEND=Agg python dev.py nb_part2.py nb_part5.py 2>&1 | sed -n '/auto O6  kappa_surr_max  lo/,$p'
```

```
cv auto O6  kappa_surr_max  lo  grid_points  spearman  hr_lo  hr_hi  kappa_hi  trials_hi  se_lo  se_hi   diff        verdict
 a    a  a          34.292 3.0          191     -0.64  0.641  0.587      12.5      344.0  0.004  0.035 -0.054 not_reproduced

seed variants (O5 a):
 seed_offset cv O6  grid_points  spearman  diff    verdict
           0  a  a            0       NaN   NaN    no grid
           0  a  b            0       NaN   NaN    no grid
           0  b  a           80     0.917 0.359 reproduced
           0  b  b           44     0.784 0.222 reproduced
           0  c  a            0       NaN   NaN    no grid
           0  c  b            0       NaN   NaN    no grid
        1000  a  a            0       NaN   NaN    no grid
        1000  a  b            0       NaN   NaN    no grid
        1000  b  a           99     0.955 0.395 reproduced
        1000  b  b           50     0.832 0.288 reproduced
        1000  c  a            0       NaN   NaN    no grid
        1000  c  b            0       NaN   NaN    no grid
        2000  a  a            0       NaN   NaN    no grid
        2000  a  b            0       NaN   NaN    no grid
        2000  b  a           74     0.898 0.341 reproduced
[... 98 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part6.py",
 "content": "# %% [md]\n## figs1-other-window-lengths\n\n> With 10-s and 60-s windows the results are similar; hit rate over scaling windows rises with the threshold, and the relative gain departs from zero around kappa of 7.\n\nCriterion: the analysis of fig3c and fig3d repeated with 10-s and 60-s windows, with no surrogate range. For each length the test passes when the scaling hit rate exceeds the no-scaling hit rate at every grid point from kappa_th = 8 to 12 and the relative gain at 12 exceeds that at 8. The onset is the smallest kappa_th above which the relative gain stays more than one bootstrap SE (O8 (c)) above zero, judged within 0.7 of 7. Reproduced when both lengths pass and both onsets are within 0.7 of 7; partially reproduced when both pass with an onset out of range, or when one length passes. The onset is searched over thresholds from 3 (the Gaussian value) to 12, a standard choice; the CV readings of O2 and the trial readings of O5 apply.\n\n# %%\n# tags: claim:figs1-other-window-lengths\nSS1 = seed(\"figs1-other-window-lengths\")\nlens = {}\nfor L in (10.0, 60.0):\n    d = W[(W.phase == \"active\") & (W.length == L)].reset_index(drop=True)\n    for auto in AUTOS:\n        dd, lost = add_trials(d, auto)\n        d[f\"hits_{auto}\"], d[f\"trials_{auto}\"] = dd.hits, dd.trials\n    lens[L] = d\n    print(f\"{L:.0f}-s windows: {len(d)}; trials placed {d.trials_a.sum()}; \"\n          f\"windows with CV > 5 under a, b, c: {[(d[f'cv_{c}'] > 5).sum() for c in CVS]}\")\nrows = []\ng812 = grid(8, 12)\ngon = grid(3, 12)\nfor L, d0 in lens.items():\n    for cv in CVS:\n        d = kept(d0, cv)\n        k = d.kappa_a.values\n        for auto in AUTOS:\n            h, n = d[f\"hits_{auto}\"].values, d[f\"trials_{auto}\"].values\n            hra, hrb, na, nb = cr.hit_curves(k, h, n, g812)\n            gain = (hra - hrb) / hrb\n            okp = np.all(hra > hrb)\n            ok12 = gain[-1] > gain[0]\n            ga, gb, _, _ = cr.hit_curves(k, h, n, gon)\n            gg = (ga - gb) / gb\n            se = cr.boot_curves(k, h, n, gon, np.random.default_rng(SS1))[2]\n            above = gg - se > 0\n            # smallest threshold from which every later point stays above\n            tail = np.flip(np.cumprod(np.flip(above)).astype(bool))\n            onset = gon[np.argmax(tail)] if tail.any() else np.nan\n            rows.append(dict(length=L, cv=cv, auto=auto, windows=len(d),\n                             frac_scaling_gt_noscaling_8_12=np.mean(hra > hrb), gain8_pct=gain[0] * 100,\n                             gain12_pct=gain[-1] * 100, trials_above_12=na[-1], passes=bool(okp and ok12),\n                             onset=onset, onset_ok=bool(abs(onset - 7) <= 0.7) if np.isfinite(onset) else False))\ns1 = pd.DataFrame(rows)\nprint(s1.round(3).to_string(index=False))\n\n\ndef s1_verdict(t):\n    best = \"not_reproduced\"\n    for cv in CVS:\n        for auto in AUTOS:\n            x = t[(t.cv == cv) & (t.auto == auto)]\n            p = x.passes.values\n            o = x.onset_ok.values\n            if p.all() and o.all():\n                return \"reproduced\"\n            if p.all() or p.any():\n                best = \"partially_reproduced\"\n    return best\n\n\nprint(\"\\nverdict over readings (one reading for both lengths):\", s1_verdict(s1))\n# Seed variants of the bootstrap (onset only)\nrows = []\nfor s in range(5):\n    for L, d0 in lens.items():\n        d = kept(d0, \"a\")\n        k, h, n = d.kappa_a.values, d.hits_a.values, d.trials_a.values\n        ga, gb, _, _ = cr.hit_curves(k, h, n, gon)\n        gg = (ga - gb) / gb\n        se = cr.boot_curves(k, h, n, gon, np.random.default_rng(SS1 + SEED_OFFSETS[s]))[2]\n        tail = np.flip(np.cumprod(np.flip(gg - se > 0)).astype(bool))\n        rows.append(dict(seed_offset=SEED_OFFSETS[s], length=L,\n                         onset=gon[np.argmax(tail)] if tail.any() else np.nan))\nprint(\"\\nonset under the seed variants (cv a, O5 a):\")\nprint(pd.DataFrame(rows).pivot(index=\"seed_offset\", columns=\"length\", values=\"onset\").to_string())\n\n# %% [md]\n## figs2-strict-units\n\n> Using only units passing stricter sorting criteria, 43 sessions keep more than 128 units, and the performance results stay qualitatively the same.\n\nCriterion: units under the strict readings of O1, (i) the dataset's default quality filters and (ii) units labelled good. Reproduced when, under one reading, the session count is within 43 +/- 4.3 and, on those sessions with those units, the test of fig3c-scaling-hit-rate-higher is at least partially reproduced and the relative gain at kappa_th = 12 is positive. Partially reproduced when the result holds but no reading gives a count within tolerance. The strict analysis has its own surrogate (one per window, this claim's seed); kappa_surr_max is taken over its active windows (O6 (a); the other phases were not analysed with strict units).\n\n# %%\n# tags: claim:figs2-strict-units\nSS2 = seed(\"figs2-strict-units\")\nrows = []\nfor uset, col in [(\"default\", \"visp_default\"), (\"good\", \"visp_good\")]:\n    for op in (\">\", \">=\"):\n        m = survey[col] > cr.MIN_UNITS if op == \">\" else survey[col] >= cr.MIN_UNITS\n        rows.append(dict(units=uset, rule=f\"{op} 128\", sessions=int(m.sum()),\n                         mice=survey[m].subject.nunique(), count_ok=abs(int(m.sum()) - 43) <= 4.3))\ns2c = pd.DataFrame(rows)\nprint(s2c.to_string(index=False))\nrows = []\nfor uset, col in [(\"default\", \"visp_default\"), (\"good\", \"visp_good\")]:\n    paths = set(survey.path[survey[col] > cr.MIN_UNITS])\n    d = W_all[(W_all.units == uset) & W_all.path.isin(paths) & (W_all.phase == \"active\")].reset_index(drop=True)\n    if len(d) == 0:\n        rows.append(dict(units=uset, sessions=0, verdict=\"no sessions\"))\n        continue\n    for auto in AUTOS:\n        dd, _ = add_trials(d, auto)\n        d[f\"hits_{auto}\"], d[f\"trials_{auto}\"] = dd.hits, dd.trials\n    for cv in CVS:\n        dk = kept(d, cv)\n        ksm = dk.surr0_kappa_a.max()\n        r, cur = fig3c_eval(d, cv, \"a\", \"a\", np.random.default_rng(SS2), np.random.default_rng(SS2 + 1), ksm=ksm)\n        k, h, n = dk.kappa_a.values, dk.hits_a.values, dk.trials_a.values\n        a_, b_, na_, nb_ = cr.hit_curves(k, h, n, np.array([12.0]))\n        g12 = ((a_ - b_) / b_)[0]\n        rows.append(dict(units=uset, sessions=d.path.nunique(), cv=cv, windows=len(dk), kappa_surr_max=ksm,\n                         grid_points=r[\"grid_points\"], frac_pass=r[\"frac_pass\"], fig3c_verdict=r[\"verdict\"],\n                         gain12_pct=g12 * 100, trials_above_12=na_[0]))\ns2 = pd.DataFrame(rows)\nprint(s2.round(3).to_string(index=False))\n# Shape of the curves on good units, from kappa 3, cv a\nd = W_all[(W_all.units == \"good\") & W_all.path.isin(set(survey.path[survey.visp_good > cr.MIN_UNITS]))\n          & (W_all.phase == \"active\")].reset_index(drop=True)\ndd, _ = add_trials(d, \"a\")\ng = grid(3, 15)\na_, b_, na_, nb_ = cr.hit_curves(d.kappa_a.values, dd.hits.values, dd.trials.values, g)\nprint(\"\\ngood units, cv a, relative gain (%) at thresholds 4 to 14 (variant, not the criterion's grid):\")\nprint(pd.DataFrame(dict(kappa_th=g, gain_pct=(a_ - b_) / b_ * 100, trials_above=na_)).iloc[20::40]\n      .round(2).to_string(index=False))\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part6.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && time MPLBACKEND=Agg python dev.py nb_part2.py nb_part4.py nb_part6.py 2>&1 | sed -n '/^10-s windows/,$p'
```

```
10-s windows: 34922; trials placed 22633; windows with CV > 5 under a, b, c: [np.int64(3), np.int64(10368), np.int64(633)]
60-s windows: 5819; trials placed 22626; windows with CV > 5 under a, b, c: [np.int64(0), np.int64(5449), np.int64(105)]
 length cv auto  windows  frac_scaling_gt_noscaling_8_12  gain8_pct  gain12_pct  trials_above_12  passes  onset  onset_ok
   10.0  a    a    34919                           0.506     -0.201       5.451            879.0   False  10.55     False
   10.0  a    b    34919                           0.630      0.482       6.811            916.0   False  10.30     False
   10.0  b    a    24554                           0.074     -1.278      -0.439            349.0   False    NaN     False
   10.0  b    b    24554                           0.123     -0.938       0.356            356.0   False    NaN     False
   10.0  c    a    34289                           0.481     -0.705       6.394            802.0   False  10.55     False
   10.0  c    b    34289                           0.519     -0.106       7.487            831.0   False  10.40     False
   60.0  a    a     5819                           0.099     -1.457      -8.094            405.0   False    NaN     False
   60.0  a    b     5819                           0.370     -0.692      -3.628            440.0   False    NaN     False
   60.0  b    a      370                           0.519      6.721         NaN              0.0   False    NaN     False
   60.0  b    b      370                           0.519      6.559         NaN              0.0   False    NaN     False
   60.0  c    a     5714                           0.173     -1.735      -4.224            316.0   False    NaN     False
   60.0  c    b     5714                           0.370     -1.276      -1.576            334.0   False    NaN     False

verdict over readings (one reading for both lengths): not_reproduced

onset under the seed variants (cv a, O5 a):
length        10.0  60.0
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025 && python - <<'EOF'
s=open('criticality.py').read()
s=s.replace('''def process_session(asset, surr_seeds, strict_seed, strict_sets=()):''','''def process_session(asset, surr_seeds, strict_seeds, strict_sets=()):''')
s=s.replace('''    `surr_seeds`: SeedSequences for the surrogate of each window (the first is the claim's
    seed, the others the four seed variants). `strict_seed`: the SeedSequence for the
    surrogate of the strict-unit analysis (figs2-strict-units). `strict_sets`: unit sets''','''    `surr_seeds`: SeedSequences for the surrogate of each window (the first is the claim's
    seed, the others the four seed variants). `strict_seeds`: the same for the surrogate of
    the strict-unit analysis (figs2-strict-units). `strict_sets`: unit sets''')
s=s.replace('''    srng = np.random.default_rng(strict_seed)
    for uset in strict_sets:''','''    srngs = [np.random.default_rng(s) for s in strict_seeds]
    for uset in strict_sets:''')
s=s.replace('''            r = analyse_window(sub, t0, t1, [srng], do_real_space=False)''','''            r = analyse_window(sub, t0, t1, srngs, do_real_space=False)''')
s=s.replace('''    asset, seeds, strict_seed, strict_sets = args
    for attempt in range(3):
        try:
            return process_session(asset, seeds, strict_seed, strict_sets)''','''    asset, seeds, strict_seeds, strict_sets = args
    for attempt in range(3):
        try:
            return process_session(asset, seeds, strict_seeds, strict_sets)''')
s=s.replace('''    skids = np.random.SeedSequence(strict_seed).spawn(n)
    jobs = [(a, [kids[v][i] for v in range(n_variants)], skids[i], strict_sets_of(a))''','''    skids = [np.random.SeedSequence(strict_seed + 1000 * v).spawn(n) for v in range(n_variants)]
    jobs = [(a, [kids[v][i] for v in range(n_variants)], [skids[v][i] for v in range(n_variants)],
             strict_sets_of(a))''')
open('criticality.py','w').write(s)
EOF
grep -n "strict" criticality.py | head -20
```

```
502:def process_session(asset, surr_seeds, strict_seeds, strict_sets=()):
506:    seed, the others the four seed variants). `strict_seeds`: the same for the surrogate of
507:    the strict-unit analysis (figs2-strict-units). `strict_sets`: unit sets
525:    srngs = [np.random.default_rng(s) for s in strict_seeds]
526:    for uset in strict_sets:
543:    asset, seeds, strict_seeds, strict_sets = args
546:            return process_session(asset, seeds, strict_seeds, strict_sets)
552:def run_sessions(assets, surr_seed, strict_seed, strict_sets_of, workers=4, n_variants=5):
559:    skids = [np.random.SeedSequence(strict_seed + 1000 * v).spawn(n) for v in range(n_variants)]
561:             strict_sets_of(a))
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && cat >> nb_part6.py <<'EOF'
rows = []
for s in range(5):
    col = f"surr{s}_kappa_a"
    d = W_all[(W_all.units == "good") & W_all.path.isin(set(survey.path[survey.visp_good > cr.MIN_UNITS]))
              & (W_all.phase == "active")].reset_index(drop=True)
    if col not in d or d[col].isna().all():
        continue
    dd, _ = add_trials(d, "a")
    d["hits_a"], d["trials_a"] = dd.hits, dd.trials
    for cv in CVS:
        dk = kept(d, cv)
        r, _ = fig3c_eval(d, cv, "a", "a", np.random.default_rng(SS2 + SEED_OFFSETS[s]),
                          np.random.default_rng(SS2 + 1 + SEED_OFFSETS[s]), ksm=dk[col].max())
        rows.append(dict(seed_offset=SEED_OFFSETS[s], cv=cv, kappa_surr_max=dk[col].max(),
                         grid_points=r["grid_points"], frac_pass=r["frac_pass"], verdict=r["verdict"]))
print("\nseed variants, good units (strict surrogate, shuffle and bootstrap):")
print(pd.DataFrame(rows).round(3).to_string(index=False))
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part7.py",
 "content": "# %% [md]\n## fig4a-active-most-scaling\n\n> For any threshold, the fraction of windows above it is largest in the active phase, smaller in the passive phase and smallest in the non-natural image phase; most non-natural image windows still have higher kurtosis than surrogates.\n\nCriterion: the complementary cumulative distribution of window kurtosis, pooled over sessions, per phase (O4), on the grid from kappa_surr_max (O6) to 15, at points where any phase is above zero. Reproduced when, under one reading, F_active > F_passive > F_NNI at every such point and F_NNI at kappa_surr_max is above 0.5. Partially reproduced when the order holds at 90% or more of points, or holds everywhere but the NNI fraction is 0.5 or below.\n\n# %%\n# tags: claim:fig4a-active-most-scaling\n\n\ndef ccdf(x, g):\n    x = np.sort(x)\n    return 1 - np.searchsorted(x, g, side=\"right\") / len(x)\n\n\ndef order_eval(groups, g, strict_first=None):\n    \"\"\"Fractions above each threshold per group; the order holds where each group's fraction\n    exceeds the next (>= for pairs listed in `strict_first`).\"\"\"\n    F = {k: ccdf(v, g) for k, v in groups.items()}\n    keys = list(groups)\n    anyp = np.any([F[k] > 0 for k in keys], 0)\n    ok = np.ones(len(g), bool)\n    for a, b in zip(keys[:-1], keys[1:]):\n        ok &= (F[a] >= F[b]) if strict_first and (a, b) in strict_first else (F[a] > F[b])\n    return F, anyp, ok\n\n\nrows = []\nfor cv in CVS:\n    d = kept(W[W.length == 30], cv)\n    for nni in [\"nni_a\", \"nni_b\"]:\n        for sm in SMAXS:\n            ksm = surr_max(cv, \"a\", sm, nni=nni) if sm == \"b\" else surr_max(cv, \"a\", \"a\")\n            g = grid(ksm, 15)\n            if len(g) == 0:\n                rows.append(dict(cv=cv, O4=nni, O6=sm, kappa_surr_max=ksm, points=0, verdict=\"no grid\"))\n                continue\n            groups = {p: d[d.phase == p].kappa_a.values for p in [\"active\", \"passive\", nni]}\n            F, anyp, ok = order_eval(groups, g)\n            frac = ok[anyp].mean() if anyp.any() else np.nan\n            fn = F[nni][0]\n            v = (\"reproduced\" if anyp.any() and ok[anyp].all() and fn > 0.5 else\n                 \"partially_reproduced\" if anyp.any() and (frac >= 0.9 or ok[anyp].all()) else \"not_reproduced\")\n            rows.append(dict(cv=cv, O4=nni, O6=sm, kappa_surr_max=ksm, points=int(anyp.sum()), frac_order=frac,\n                             F_active_lo=F[\"active\"][0], F_passive_lo=F[\"passive\"][0], F_nni_lo=fn, verdict=v))\nf4a = pd.DataFrame(rows)\nprint(f4a.round(4).to_string(index=False))\ng = grid(3, 15)\nd = kept(W[W.length == 30], \"a\")\nF = {p: ccdf(d[d.phase == p].kappa_a.values, g) for p in [\"active\", \"passive\", \"nni_a\", \"nni_b\"]}\nprint(\"\\nfraction of windows above kappa_th, cv a, thresholds 3 to 15 (not the criterion's grid):\")\nprint(pd.DataFrame(dict(kappa_th=g, **F)).iloc[::20].round(4).to_string(index=False))\nprint(\"\\nmedian window kurtosis per phase and session, then over sessions (cv a):\")\nprint(d.groupby([\"phase\", \"path\"]).kappa_a.median().groupby(\"phase\").describe().round(2).to_string())\npp = d.groupby([\"path\", \"phase\"]).kappa_a.median().unstack()\nprint(\"sessions with median kurtosis active > passive:\", int((pp.active > pp.passive).sum()), \"of\", len(pp),\n      \"; active > NNI (a):\", int((pp.active > pp.nni_a).sum()), \"; passive > NNI (a):\",\n      int((pp.passive > pp.nni_a).sum()))\nrows = []\nfor s in range(5):\n    for cv in CVS:\n        for sm in SMAXS:\n            ksm = surr_max(cv, \"a\", sm, s)\n            g_ = grid(ksm, 15)\n            rows.append(dict(seed_offset=SEED_OFFSETS[s], cv=cv, O6=sm, kappa_surr_max=round(ksm, 2), points=len(g_)))\nprint(\"\\nseed variants change only the start of the grid:\")\nprint(pd.DataFrame(rows).pivot_table(index=[\"cv\", \"O6\"], columns=\"seed_offset\", values=\"kappa_surr_max\").to_string())\nfig, ax = plt.subplots(figsize=(6, 3.5))\nfor p, f in F.items():\n    ax.plot(g, f, label=p)\nax.set_xlabel(\"kappa_th\")\nax.set_ylabel(\"fraction of windows above\")\nax.legend()\nplt.show()\n\n# %% [md]\n## figs8-halves-and-phase-order\n\n> Kurtosis is lower in the second half of the active phase than in the first, yet both halves keep more windows above threshold than the passive and non-natural image phases; the non-natural image phase, though it precedes the passive phase, has the lowest kurtosis.\n\nCriterion: complementary cumulative distributions for active first 30 min, active last 30 min, passive and NNI, on the grid from kappa_surr_max to 15. Reproduced when, at every point where any group is above zero, active first half >= active second half > passive > NNI. Partially reproduced when the order of the second half over passive, or the first half over the second, fails at some points. The first half is the windows ending within 30 min of the active block's start, the second half the windows starting at or after 30 min (a standard choice); O2, O4 and O6 readings are run.\n\n# %%\n# tags: claim:figs8-halves-and-phase-order\na0 = {p: res_of[p][\"spans\"][\"active\"][0][0] for p in res_of}\n\n\ndef halves(df):\n    st = df.path.map(a0)\n    return df[df.t1 <= st + 1800 + 1e-6], df[df.t0 >= st + 1800 - 1e-6]\n\n\nrows = []\nfor cv in CVS:\n    d = kept(W[W.length == 30], cv)\n    h1, h2 = halves(d[d.phase == \"active\"])\n    for nni in [\"nni_a\", \"nni_b\"]:\n        for sm in SMAXS:\n            ksm = surr_max(cv, \"a\", sm, nni=nni) if sm == \"b\" else surr_max(cv, \"a\", \"a\")\n            g = grid(ksm, 15)\n            groups = {\"first\": h1.kappa_a.values, \"second\": h2.kappa_a.values,\n                      \"passive\": d[d.phase == \"passive\"].kappa_a.values, \"nni\": d[d.phase == nni].kappa_a.values}\n            if len(g) == 0:\n                rows.append(dict(cv=cv, O4=nni, O6=sm, kappa_surr_max=ksm, points=0, verdict=\"no grid\"))\n                continue\n            Fh, anyp, ok = order_eval(groups, g, strict_first={(\"first\", \"second\")})\n            pair = lambda a, b, ge=False: float(np.mean((Fh[a] >= Fh[b] if ge else Fh[a] > Fh[b])[anyp]))\n            tail_ok = pair(\"passive\", \"nni\") == 1.0\n            v = (\"reproduced\" if ok[anyp].all() else\n                 \"partially_reproduced\" if tail_ok else \"not_reproduced\")\n            rows.append(dict(cv=cv, O4=nni, O6=sm, kappa_surr_max=ksm, points=int(anyp.sum()),\n                             first_ge_second=pair(\"first\", \"second\", True), second_gt_passive=pair(\"second\", \"passive\"),\n                             passive_gt_nni=pair(\"passive\", \"nni\"), verdict=v))\ns8 = pd.DataFrame(rows)\nprint(s8.round(3).to_string(index=False))\nd = kept(W[W.length == 30], \"a\")\nh1, h2 = halves(d[d.phase == \"active\"])\nprint(\"\\nmedian kurtosis (cv a): first half\", round(h1.kappa_a.median(), 3), \", second half\",\n      round(h2.kappa_a.median(), 3), \", passive\", round(d[d.phase == \"passive\"].kappa_a.median(), 3),\n      \", NNI (a)\", round(d[d.phase == \"nni_a\"].kappa_a.median(), 3), \", NNI (b)\",\n      round(d[d.phase == \"nni_b\"].kappa_a.median(), 3))\nprint(\"Mann-Whitney first against second half: p =\", f\"{stats.mannwhitneyu(h1.kappa_a, h2.kappa_a).pvalue:.2e}\")\n\n# %% [md]\n## figs4-initial-kurtosis-poor-predictor\n\n> The kurtosis of the activity before coarse graining is a very poor predictor of the kurtosis after coarse graining.\n\nCriterion: kappa_0 at Ncutoff = N (the z-scored binned counts, pooled as in O3), kappa_final at N/16, per window; active phase (all phases pooled as a variant). Spearman correlation across windows; reproduced when its magnitude is below 0.3, partially reproduced between 0.3 and 0.5.\n\n# %%\n# tags: claim:figs4-initial-kurtosis-poor-predictor\nrows = []\nfor cv in CVS:\n    for ph, phases in [(\"active\", [\"active\"]), (\"all phases\", [\"active\", \"passive\", \"nni_a\"])]:\n        d = kept(W[(W.length == 30) & W.phase.isin(phases)], cv)\n        rho, p = stats.spearmanr(d.kappa0_a, d.kappa_a)\n        rows.append(dict(cv=cv, phases=ph, windows=len(d), spearman=rho, p=p,\n                         kappa0_median=d.kappa0_a.median(), kappa0_range=f\"{d.kappa0_a.min():.1f} to {d.kappa0_a.max():.1f}\",\n                         verdict=\"reproduced\" if abs(rho) < 0.3 else \"partially_reproduced\" if abs(rho) < 0.5\n                         else \"not_reproduced\"))\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nd = kept(W[(W.length == 30) & (W.phase == \"active\")], \"a\")\nper = d.groupby(\"path\").apply(lambda x: stats.spearmanr(x.kappa0_a, x.kappa_a)[0])\nprint(\"\\nwithin-session Spearman (active, cv a): median\", round(per.median(), 3), \"range\", round(per.min(), 3),\n      \"to\", round(per.max(), 3))\n\n# %% [md]\n## figs5a-firing-rate-order\n\n> Mean firing rate over windows above a kurtosis threshold varies almost monotonically with the threshold within each phase (the legend expects it to decrease), and is ordered active < NNI < passive for any threshold, unlike the kurtosis order of Figure 4A.\n\nCriterion: per window, the mean over units of spike counts per bin; averaged over a mouse's windows above kappa_th, then over mice, on the grid from 5 to 12 at points where every phase has windows. Reproduced when active < NNI < passive at every point and, within each phase, the Spearman correlation of rate against kappa_th is negative with magnitude at least 0.8. Partially reproduced when the order holds at 90% or more of points. The rate is over all V1 units of the session, silent ones included.\n\n# %%\n# tags: claim:figs5a-firing-rate-order\ng5 = grid(5, 12)\n\n\ndef rate_curve(d, g):\n    k, r, m = d.kappa_a.values, d.rate.values, d.mouse.values\n    out = np.full(len(g), np.nan)\n    for i, th in enumerate(g):\n        s = k > th\n        if s.any():\n            out[i] = pd.Series(r[s]).groupby(m[s]).mean().mean()\n    return out\n\n\nrows = []\ncurves5 = {}\nfor cv in CVS:\n    d = kept(W[W.length == 30], cv)\n    for nni in [\"nni_a\", \"nni_b\"]:\n        R = {p: rate_curve(d[d.phase == p], g5) for p in [\"active\", nni, \"passive\"]}\n        curves5[(cv, nni)] = R\n        allp = np.all([np.isfinite(R[p]) for p in R], 0)\n        order = (R[\"active\"] < R[nni]) & (R[nni] < R[\"passive\"])\n        rhos = {p: stats.spearmanr(g5[np.isfinite(R[p])], R[p][np.isfinite(R[p])])[0] for p in R}\n        frac = order[allp].mean() if allp.any() else np.nan\n        mono = all(rhos[p] < 0 and abs(rhos[p]) >= 0.8 for p in R)\n        v = (\"reproduced\" if allp.any() and order[allp].all() and mono else\n             \"partially_reproduced\" if frac >= 0.9 else \"not_reproduced\")\n        rows.append(dict(cv=cv, O4=nni, points=int(allp.sum()), frac_order=frac,\n                         **{f\"rho_{p}\": rhos[p] for p in R}, verdict=v))\nprint(pd.DataFrame(rows).round(3).to_string(index=False))\nR = curves5[(\"a\", \"nni_a\")]\nprint(\"\\nrate (spikes per bin per unit), cv a, NNI (a):\")\nprint(pd.DataFrame(dict(kappa_th=g5, **R)).iloc[::20].round(4).to_string(index=False))\nd = kept(W[W.length == 30], \"a\")\nprint(\"\\nall windows, mean rate per phase:\", d.groupby(\"phase\").rate.mean().round(4).to_dict())\n\n# %% [md]\n## figs5c-hit-rate-firing-rate-nonmonotonic\n\n> The hit rate over windows below a firing-rate threshold is not a monotonic function of the threshold.\n\nCriterion: active windows split by their mean firing rate at rho_th on a grid of step 0.0025 from 0.05 to 0.20; hit rate pooled as in M5. Reproduced when the below-threshold hit rate rises by more than one bootstrap SE (O8) between two grid points and falls by more than one SE between two others; not reproduced when it is monotonic within that margin. A change between two points counts when it exceeds the larger of their two SEs (this notebook's reading of \"one bootstrap SE\"; the smaller is shown as well). Bootstrap: this claim's seed, 10^4 resamples.\n\n# %%\n# tags: claim:figs5c-hit-rate-firing-rate-nonmonotonic\nS5C = seed(\"figs5c-hit-rate-firing-rate-nonmonotonic\")\ngr = np.round(np.arange(0.05, 0.20 + 1e-9, 0.0025), 4)\n\n\ndef nonmono(hr, se, use=np.maximum):\n    v = np.isfinite(hr) & np.isfinite(se)\n    hr, se = hr[v], se[v]\n    D = hr[None, :] - hr[:, None]          # D[i, j] = hr_j - hr_i\n    S = use(se[None, :], se[:, None])\n    up = np.triu(D > S, 1).any()\n    down = np.triu(-D > S, 1).any()\n    return bool(up), bool(down)\n\n\ndef s5c_eval(cv, auto, rng):\n    d = kept(ACT, cv)\n    r, h, n = d.rate.values, d[f\"hits_{auto}\"].values, d[f\"trials_{auto}\"].values\n    _, hrb, _, nb = cr.hit_curves(r, h, n, gr)\n    se = cr.boot_curves(r, h, n, gr, rng)[1]\n    up, down = nonmono(hrb, se)\n    up2, down2 = nonmono(hrb, se, np.minimum)\n    return dict(cv=cv, auto=auto, windows=len(d), rate_range=f\"{r.min():.3f} to {r.max():.3f}\",\n                windows_below_0_05=int((r <= 0.05).sum()), hr_min=np.nanmin(hrb), hr_max=np.nanmax(hrb),\n                rises=up, falls=down, rises_minSE=up2, falls_minSE=down2,\n                verdict=\"reproduced\" if up and down else \"not_reproduced\"), (hrb, se, nb)\n\n\nrows, s5c_cur = [], {}\nfor cv in CVS:\n    for auto in AUTOS:\n        r_, c_ = s5c_eval(cv, auto, np.random.default_rng(S5C))\n        rows.append(r_)\n        s5c_cur[(cv, auto)] = c_\nprint(pd.DataFrame(rows).round(3).to_string(index=False))\nhrb, se, nb = s5c_cur[(\"a\", \"a\")]\nprint(\"\\nbelow-threshold hit rate, cv a, O5 a:\")\nprint(pd.DataFrame(dict(rho_th=gr, hit_rate_below=hrb, se=se, trials_below=nb)).iloc[::6].round(4)\n      .to_string(index=False))\nprint(\"\\nseed variants (cv a, O5 a):\",\n      [s5c_eval(\"a\", \"a\", np.random.default_rng(S5C + o))[0][\"verdict\"] for o in SEED_OFFSETS])\n\n# %% [md]\n## figs7-fatigue-halves\n\n> In each half of the active phase (first and last 30 min), the scaling hit rate still rises above the no-scaling hit rate as the threshold grows, though the overall hit rate is lower in the second half.\n\nCriterion: the analysis of fig3c, separately for windows in the first and the last 30 min of the active phase. Reproduced when, in each half, the relative gain (Eq. 13) is positive at every grid point from kappa_th = 8 to 12 and larger at 12 than at 8, and the overall hit rate (all windows) of the second half is lower than that of the first. Partially reproduced when the gain holds in one half. Halves as in figs8-halves-and-phase-order; O2 and O5 readings are run.\n\n# %%\n# tags: claim:figs7-fatigue-halves\nrows = []\nfor cv in CVS:\n    h1, h2 = halves(kept(ACT, cv))\n    for auto in AUTOS:\n        res_h = {}\n        for name, d in [(\"first\", h1), (\"second\", h2)]:\n            k, h, n = d.kappa_a.values, d[f\"hits_{auto}\"].values, d[f\"trials_{auto}\"].values\n            a_, b_, na_, nb_ = cr.hit_curves(k, h, n, g812)\n            gain = (a_ - b_) / b_\n            res_h[name] = dict(pos=bool(np.all(gain > 0)), frac_pos=float(np.mean(gain > 0)), g8=gain[0] * 100,\n                               g12=gain[-1] * 100, overall=h.sum() / n.sum(), trials12=na_[-1])\n            res_h[name][\"holds\"] = res_h[name][\"pos\"] and gain[-1] > gain[0]\n        lower = res_h[\"second\"][\"overall\"] < res_h[\"first\"][\"overall\"]\n        v = (\"reproduced\" if res_h[\"first\"][\"holds\"] and res_h[\"second\"][\"holds\"] and lower else\n             \"partially_reproduced\" if res_h[\"first\"][\"holds\"] or res_h[\"second\"][\"holds\"] else \"not_reproduced\")\n        rows.append(dict(cv=cv, auto=auto, **{f\"{h}_{k}\": v_ for h in res_h for k, v_ in res_h[h].items()},\n                         second_lower=lower, verdict=v))\nprint(pd.DataFrame(rows).round(3).T.to_string())\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part7.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && time MPLBACKEND=Agg python dev.py nb_part2.py nb_part7.py 2>&1 | sed -n '/^cv  O4/,$p'
```

```
real	0m41.699s
user	0m34.434s
sys	0m7.240s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && MPLBACKEND=Agg python dev.py nb_part2.py nb_part7.py 2>&1 | sed -n '/kappa_surr_max under each/,$p' | sed -n '15,400p'
```

```
cv    O4 O6  kappa_surr_max  points        verdict  frac_order  F_active_lo  F_passive_lo  F_nni_lo
 a nni_a  a         34.2921       0        no grid         NaN          NaN           NaN       NaN
 a nni_a  b         48.3407       0        no grid         NaN          NaN           NaN       NaN
 a nni_b  a         34.2921       0        no grid         NaN          NaN           NaN       NaN
 a nni_b  b         48.3407       0        no grid         NaN          NaN           NaN       NaN
 b nni_a  a          8.5316     130 not_reproduced         0.0       0.0542        0.0316    0.1843
 b nni_a  b         10.3024      94 not_reproduced         0.0       0.0108        0.0073    0.0783
 b nni_b  a          8.5316     130 not_reproduced         0.0       0.0542        0.0316    0.1676
 b nni_b  b          8.8063     124 not_reproduced         0.0       0.0408        0.0253    0.1433
 c nni_a  a         34.2921       0        no grid         NaN          NaN           NaN       NaN
 c nni_a  b         34.2921       0        no grid         NaN          NaN           NaN       NaN
 c nni_b  a         34.2921       0        no grid         NaN          NaN           NaN       NaN
 c nni_b  b         34.2921       0        no grid         NaN          NaN           NaN       NaN

fraction of windows above kappa_th, cv a, thresholds 3 to 15 (not the criterion's grid):
 kappa_th  active  passive  nni_a  nni_b
      3.0  1.0000   1.0000 1.0000 1.0000
      4.0  0.9894   0.9680 0.9727 0.9997
      5.0  0.8478   0.7106 0.8948 0.9725
      6.0  0.5537   0.3444 0.7245 0.8131
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import re
txt=open('nb_part7.py').read()
i=txt.index('## figs7-fatigue-halves'); j=txt.rfind('# %% [md]',0,i)
pre="# %%\ng812 = grid(8, 12)\n"
open('nb_part7b.py','w').write(pre+txt[j:])
EOF
MPLBACKEND=Agg python dev.py nb_part2.py nb_part7b.py 2>&1 | tail -30
```

```
units silent in a 30-s window (left out of that window): median 14.0 max 203 ; units kept per window: min 2

clock check (V1 spikes 30-130 ms after an image onset minus the 100 ms before):
  shown images: median over sessions 62.1 spikes; omitted flashes: 0.7; sessions where shown exceeds omitted by more than 5 SE: 96 of 98; smallest z 4.0
windows with cv_a > 5: {'active': '0 of 11639', 'nni_a': '0 of 5057', 'nni_b': '0 of 3783', 'passive': '0 of 11639'}
windows with cv_b > 5: {'active': '9702 of 11639', 'nni_a': '4048 of 5057', 'nni_b': '2876 of 3783', 'passive': '5632 of 11639'}
windows with cv_c > 5: {'active': '209 of 11639', 'nni_a': '0 of 5057', 'nni_b': '0 of 3783', 'passive': '12 of 11639'}
O5 (a): trials placed in active windows 22628, hits 14507, trials outside every window 43; overall hit rate 0.641
O5 (b): trials placed in active windows 22919, hits 14798, trials outside every window 43; overall hit rate 0.646
trials per active window: median 2.0 range 0 to 4

kappa_surr_max under each reading (claim seed):
cv kappa O6  kappa_surr_max
 a     a  a          34.292
 a     a  b          48.341
 a     b  a          34.292
 a     b  b          48.341
 b     a  a           8.532
 b     a  b          10.302
 b     b  a           8.532
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
txt=open('nb_part7.py').read()
i=txt.index('## figs7-fatigue-halves'); j=txt.rfind('# %% [md]',0,i)
pre='''# %%
g812 = grid(8, 12)
a0 = {p: res_of[p]["spans"]["active"][0][0] for p in res_of}
def halves(df):
    st = df.path.map(a0)
    return df[df.t1 <= st + 1800 + 1e-6], df[df.t0 >= st + 1800 - 1e-6]
'''
open('nb_part7b.py','w').write(pre+txt[j:])
EOF
MPLBACKEND=Agg python dev.py nb_part2.py nb_part7b.py 2>&1 | tail -22
```

```
c     a  b          34.292
 c     b  a          34.292
 c     b  b          34.292
                              0               1           2                     3               4               5
cv                            a               a           b                     b               c               c
auto                          a               b           a                     b               a               b
first_pos                 False           False        True                 False           False           False
first_frac_pos              0.0             0.0         1.0                 0.963             0.0             0.0
first_g8                 -7.982           -7.15       3.008                 3.824          -7.758           -7.21
first_g12               -11.221          -9.038      40.263                39.382          -4.573          -3.676
first_overall             0.749           0.755       0.714                 0.718           0.752           0.758
first_trials12            294.0           315.0         4.0                   4.0           234.0           245.0
first_holds               False           False        True                 False           False           False
second_pos                False           False        True                  True           False           False
second_frac_pos           0.012           0.012         1.0                   1.0             0.0             0.0
second_g8                -6.771          -6.771       2.146                 2.146          -7.062          -7.062
second_g12              -20.319         -20.319      48.412                48.412         -20.615         -20.615
second_overall            0.548           0.548       0.562                 0.562           0.548           0.548
second_trials12           144.0           144.0         6.0                   6.0           140.0           140.0
second_holds              False           False        True                  True           F
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025 && cat >> criticality.py <<'EOF'


def window_fits(rs, N):
    """Per-window exponents under every reading of O9, fitting each quantity once:
    alpha_<K range>, z_<K range>, beta_<K range><P_silence>, mu_<mu reading>, mu_r2_<mu reading>."""
    out = {}
    for kr in "ab":
        for fs in "ab":
            f = fit_exponents(rs, N, kr, fs, "a" if fs == "a" else "b")
            out[f"beta_{kr}{fs}"] = f["beta"]
            if fs == "a":
                out[f"alpha_{kr}"], out[f"z_{kr}"] = f["alpha"], f["z"]
                if kr == "a":
                    out["mu_a"], out["mu_r2_a"] = f["mu"], f["mu_r2"]
            elif kr == "a":
                out["mu_b"], out["mu_r2_b"] = f["mu"], f["mu_r2"]
    return out


def reading_columns(kr, fs, mu):
    return dict(alpha=f"alpha_{kr}", beta=f"beta_{kr}{fs}", z=f"z_{kr}", mu=f"mu_{mu}",
                mu_r2=f"mu_r2_{mu}")
EOF
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import sys,pickle,time
sys.path.insert(0,'entries/cambrainha-2025')
import criticality as cr
res=pickle.load(open('res_4.pkl','rb'))
ws=[w for w in res[0]['windows'] if 'rs' in w][:100]
t=time.time()
for w in ws: f=cr.window_fits(w['rs'],w['N']); g=cr.window_fits(w['surr_rs'],w['N'])
print((time.time()-t)/100, f)
EOF
```

```
0.0014716482162475586 {'beta_aa': np.float64(0.7483175228165664), 'alpha_a': np.float64(1.508376317402662), 'z_a': np.float64(0.19361929601366598), 'mu_a': np.float64(1.7818765444635587), 'mu_r2_a': np.float64(0.3134220726190303), 'beta_ab': np.float64(0.7167257927505262), 'mu_b': np.float64(1.6222311126739668), 'mu_r2_b': np.float64(0.7776107463591035), 'beta_ba': np.float64(0.7759001688223611), 'alpha_b': np.float64(1.4711584846315573), 'z_b': np.float64(0.12894348941295852), 'beta_bb': np.float64(0.7891561024903792)}
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part8.py",
 "content": "# %% [md]\n## Real-space exponents (fig4 claims)\n\nPer window, the real-space quantities (M7) are fitted under every reading of O9: K range (a) to the largest K with two clusters or (b) to N/16; P_silence (a) or (b); mu (a) pooled spectra K >= 16 or (b) K = 64. Session values follow O10: (a) the mean of per-window fits (mu only from windows with r^2 >= 0.85) or (b) one fit to the session's averaged quantities. Phases as in O4; windows kept by the CV readings of O2. The same is done on each window's surrogate (claim seed of fig3a-kurtosis-broader-than-surrogate), for the lighter bars of Figure 4.\n\n# %%\nt0 = time.time()\nfit_rows = []\nfor r in ok:\n    if r[\"meta\"][\"path\"] not in sel_gt:\n        continue\n    for w in r[\"windows\"]:\n        if \"rs\" not in w:\n            continue\n        base = dict(path=r[\"meta\"][\"path\"], phase=w[\"phase\"], t0=w[\"t0\"], kappa_a=w[\"kappa_a\"],\n                    cv_a=w[\"cv_a\"], cv_b=w[\"cv_b\"], cv_c=w[\"cv_c\"], N=w[\"N\"])\n        fit_rows.append(dict(base, kind=\"real\", **cr.window_fits(w[\"rs\"], w[\"N\"])))\n        fit_rows.append(dict(base, kind=\"surrogate\", **cr.window_fits(w[\"surr_rs\"], w[\"N\"])))\nFITS = pd.DataFrame(fit_rows)\nprint(f\"per-window fits: {len(FITS)} in {time.time() - t0:.0f} s\")\ncols = [c for c in FITS if c.split(\"_\")[0] in (\"alpha\", \"beta\", \"z\", \"mu\") and \"r2\" not in c]\nprint(\"windows with a failed fit (NaN), per quantity, real windows:\")\nprint(FITS[FITS.kind == \"real\"][cols].isna().sum().to_dict())\nprint(\"mu windows with r^2 >= 0.85 (real): reading a\",\n      f\"{(FITS[FITS.kind == 'real'].mu_r2_a >= cr.MU_R2_MIN).mean():.3f},\",\n      \"reading b\", f\"{(FITS[FITS.kind == 'real'].mu_r2_b >= cr.MU_R2_MIN).mean():.3f}\")\nrs_of = {}\nfor r in ok:\n    for w in r[\"windows\"]:\n        if \"rs\" in w:\n            rs_of[(r[\"meta\"][\"path\"], w[\"phase\"], w[\"t0\"])] = (w[\"rs\"], w[\"surr_rs\"], w[\"N\"])\n\nEXP = [\"alpha\", \"beta\", \"mu\", \"z\"]\nREAD9 = cr.EXP_READINGS\n\n\ndef session_values(phase, cv, reading, agg, kind=\"real\", kmin=None):\n    \"\"\"Session exponents for one phase under one reading (O9) and aggregation (O10).\"\"\"\n    d = FITS[(FITS.phase == phase) & (FITS.kind == kind) & (FITS[f\"cv_{cv}\"] <= cr.CV_MAX)]\n    if kmin is not None:\n        d = d[d.kappa_a > kmin]\n    c = cr.reading_columns(*reading)\n    out = []\n    for p, x in d.groupby(\"path\"):\n        if agg == \"a\":\n            mu = x[c[\"mu\"]][x[c[\"mu_r2\"]] >= cr.MU_R2_MIN]\n            out.append(dict(path=p, alpha=x[c[\"alpha\"]].mean(), beta=x[c[\"beta\"]].mean(),\n                            z=x[c[\"z\"]].mean(), mu=mu.mean() if len(mu) else np.nan, windows=len(x)))\n        else:\n            rr_ = [rs_of[(p, phase, t)] for t in x.t0]\n            rss = [a if kind == \"real\" else b for a, b, _ in rr_]\n            v = cr.session_exponents(rss, [n for _, _, n in rr_], reading, \"b\")\n            out.append(dict(path=p, alpha=v[\"alpha\"], beta=v[\"beta\"], z=v[\"z\"], mu=v[\"mu\"], windows=len(x)))\n    return pd.DataFrame(out).set_index(\"path\")\n\n\nSV = {}\nfor cv in [\"a\", \"b\", \"c\"]:\n    for reading in READ9:\n        for agg in \"ab\":\n            for phase in [\"active\", \"passive\", \"nni_a\", \"nni_b\"]:\n                SV[(phase, cv, reading, agg)] = session_values(phase, cv, reading, agg)\nprint(\"session values computed:\", len(SV), f\"({time.time() - t0:.0f} s)\")\nEXPECTED = {\"active\": dict(alpha=(1.41, .05), beta=(.77, .04), mu=(.73, .08), z=(.3, .1)),\n            \"passive\": dict(alpha=(1.37, .04), beta=(.78, .04), mu=(.61, .05), z=(.36, .06)),\n            \"nni\": dict(alpha=(1.28, .03), beta=(.82, .03), mu=(.38, .04), z=(.4, .1))}\n\n\ndef means_table(phase, key):\n    rows = []\n    for cv in CVS:\n        for reading in READ9:\n            for agg in \"ab\":\n                s = SV[(phase, cv, reading, agg)]\n                row = dict(cv=cv, O9=\"\".join(reading), O10=agg, sessions=len(s), sessions_mu=int(s.mu.notna().sum()))\n                within = 0\n                for e in EXP:\n                    m, sd = s[e].mean(), s[e].std()\n                    row[f\"{e}_mean\"], row[f\"{e}_sd\"] = m, sd\n                    ok_ = abs(m - EXPECTED[key][e][0]) <= EXPECTED[key][e][1]\n                    row[f\"{e}_ok\"] = bool(ok_)\n                    within += ok_\n                row[\"within\"] = within\n                rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# %% [md]\n## fig4-exponents-active\n\n> In the active phase the real-space scaling exponents are alpha 1.41 +/- 0.05, beta 0.77 +/- 0.04, mu 0.73 +/- 0.08 and z 0.3 +/- 0.1 (mean and SD across sessions).\n\nCriterion: exponents as in M7 with the readings of O9 and O10, on active windows (O2). Reproduced when, under one reading, all four means are within tolerance; partially reproduced when three are. Main reading: O9 (a, a, a), O10 (a), O2 (a).\n\n# %%\n# tags: claim:fig4-exponents-active\nMA = means_table(\"active\", \"active\")\nshow = [\"cv\", \"O9\", \"O10\", \"sessions\", \"sessions_mu\"] + [f\"{e}_mean\" for e in EXP] + [f\"{e}_sd\" for e in EXP] + [\"within\"]\nprint(MA[show].round(3).to_string(index=False))\nprint(\"\\nlargest number of means within tolerance under a reading:\", MA.within.max(), \"; readings with 3 or more:\",\n      int((MA.within >= 3).sum()), \"of\", len(MA))\nprint(\"per exponent, readings within tolerance:\", {e: int(MA[f\"{e}_ok\"].sum()) for e in EXP})\ns = SV[(\"active\", \"a\", (\"a\", \"a\", \"a\"), \"a\")]\nprint(\"\\nmain reading, session values (active):\")\nprint(s[EXP].describe().round(3).to_string())\nsu = session_values(\"active\", \"a\", (\"a\", \"a\", \"a\"), \"a\", kind=\"surrogate\")\nprint(\"\\nsurrogate, main reading:\", {e: f\"{su[e].mean():.3f} +/- {su[e].std():.3f}\" for e in EXP})\n\n# %% [md]\n## fig4-exponents-passive\n\n> In the passive phase the exponents are alpha 1.37 +/- 0.04, beta 0.78 +/- 0.04, mu 0.61 +/- 0.05 and z 0.36 +/- 0.06, differing significantly from the active phase for alpha, z and mu but not for beta.\n\nCriterion: exponents as in fig4-exponents-active on passive windows; Mann-Whitney U between session values, two-sided at 0.05 (O11 (a)). Reproduced when all four means are within tolerance under one reading, alpha, z and mu differ significantly with passive alpha lower, z higher and mu lower, and beta does not differ (p >= 0.05). Partially reproduced when the tests agree but one mean is out of tolerance, or the means hold and one test disagrees. Window values pooled (O11 (b)) are shown as a variant for the main reading.\n\n# %%\n# tags: claim:fig4-exponents-passive\n\n\ndef mwu(a, b):\n    a, b = np.asarray(a, float), np.asarray(b, float)\n    a, b = a[np.isfinite(a)], b[np.isfinite(b)]\n    if len(a) < 2 or len(b) < 2:\n        return np.nan\n    return stats.mannwhitneyu(a, b, alternative=\"two-sided\").pvalue\n\n\nMP = means_table(\"passive\", \"passive\")\nrows = []\nfor cv in CVS:\n    for reading in READ9:\n        for agg in \"ab\":\n            A, P = SV[(\"active\", cv, reading, agg)], SV[(\"passive\", cv, reading, agg)]\n            t = {e: mwu(A[e], P[e]) for e in EXP}\n            sign = dict(alpha=P.alpha.mean() < A.alpha.mean(), z=P.z.mean() > A.z.mean(), mu=P.mu.mean() < A.mu.mean())\n            tests_ok = (all(t[e] < 0.05 and sign[e] for e in [\"alpha\", \"z\", \"mu\"]) and t[\"beta\"] >= 0.05)\n            n_tests = sum(t[e] < 0.05 and sign[e] for e in [\"alpha\", \"z\", \"mu\"]) + (t[\"beta\"] >= 0.05)\n            rows.append(dict(cv=cv, O9=\"\".join(reading), O10=agg, **{f\"p_{e}\": t[e] for e in EXP},\n                             tests_agree=n_tests, tests_ok=tests_ok))\nTP = pd.DataFrame(rows)\nMPT = MP.merge(TP, on=[\"cv\", \"O9\", \"O10\"])\nMPT[\"verdict\"] = np.where((MPT.within == 4) & MPT.tests_ok, \"reproduced\",\n                          np.where(((MPT.within == 3) & MPT.tests_ok) | ((MPT.within == 4) & (MPT.tests_agree == 3)),\n                                   \"partially_reproduced\", \"not_reproduced\"))\nprint(MPT[show + [\"p_alpha\", \"p_beta\", \"p_mu\", \"p_z\", \"tests_agree\", \"verdict\"]].round(4).to_string(index=False))\nprint(\"\\nverdicts over readings:\", MPT.verdict.value_counts().to_dict())\nfa = FITS[(FITS.kind == \"real\") & (FITS.cv_a <= 5)]\nprint(\"\\nvariant O11 (b), window values pooled, main reading:\",\n      {e: f\"{mwu(fa[fa.phase == 'active'][c], fa[fa.phase == 'passive'][c]):.2e}\"\n       for e, c in [(\"alpha\", \"alpha_a\"), (\"beta\", \"beta_aa\"), (\"mu\", \"mu_a\"), (\"z\", \"z_a\")]})\n\n# %% [md]\n## fig4-exponents-nni\n\n> With non-natural images the exponents are alpha 1.28 +/- 0.03, beta 0.82 +/- 0.03, mu 0.38 +/- 0.04 and z 0.4 +/- 0.1, all significantly different from both natural image phases.\n\nCriterion: exponents on NNI windows (O4 readings); Mann-Whitney U as in M8 under O11 (a), two-sided at 0.05. Reproduced when all four means are within tolerance under one reading and all eight comparisons are significant with NNI alpha and mu lower, beta and z higher than both other phases. Partially reproduced when at least six comparisons hold and at least three means are within tolerance.\n\n# %%\n# tags: claim:fig4-exponents-nni\nrows = []\nfor nni in [\"nni_a\", \"nni_b\"]:\n    M = means_table(nni, \"nni\")\n    M[\"O4\"] = nni\n    for i, row in M.iterrows():\n        reading = tuple(row.O9)\n        Nn = SV[(nni, row.cv, reading, row.O10)]\n        nholds = 0\n        ps = {}\n        for other in [\"active\", \"passive\"]:\n            O = SV[(other, row.cv, reading, row.O10)]\n            for e, lower in [(\"alpha\", True), (\"mu\", True), (\"beta\", False), (\"z\", False)]:\n                p = mwu(Nn[e], O[e])\n                ps[f\"p_{e}_{other}\"] = p\n                direction = Nn[e].mean() < O[e].mean() if lower else Nn[e].mean() > O[e].mean()\n                nholds += bool(p < 0.05 and direction)\n        rows.append(dict(row.to_dict(), comparisons_hold=nholds, **ps))\nMN = pd.DataFrame(rows)\nMN[\"verdict\"] = np.where((MN.within == 4) & (MN.comparisons_hold == 8), \"reproduced\",\n                         np.where((MN.within >= 3) & (MN.comparisons_hold >= 6), \"partially_reproduced\", \"not_reproduced\"))\nprint(MN[[\"O4\"] + show + [\"comparisons_hold\", \"verdict\"]].round(3).to_string(index=False))\nprint(\"\\nverdicts over readings:\", MN.verdict.value_counts().to_dict())\nm = MN[(MN.O4 == \"nni_a\") & (MN.cv == \"a\") & (MN.O9 == \"aaa\") & (MN.O10 == \"a\")].iloc[0]\nprint(\"\\nmain reading p-values:\", {k: f\"{v:.2e}\" for k, v in m.items() if str(k).startswith(\"p_\")})\n\n# %% [md]\n## fig4bc-static-exponents-trend\n\n> In the active phase alpha and beta deviate significantly from their trivial values of 1; in the passive phase they lie closer to the trivial values, and closer still with non-natural images, while z moves away from its trivial value 0 from active to passive to non-natural images.\n\nCriterion: the deviation test is (a) session alpha and beta of the active phase against those of the surrogate windows, Mann-Whitney U, or (b) a one-sample two-sided Wilcoxon signed-rank test against 1. Reproduced when, under one reading, active alpha and beta differ significantly (p < 0.05) from trivial with alpha above 1 and beta below 1, and the mean distances |alpha - 1|, |1 - beta| and z are ordered active > passive > NNI for alpha, active >= passive > NNI for beta and active < passive < NNI for z. Partially reproduced when the deviation holds and one ordering fails.\n\n# %%\n# tags: claim:fig4bc-static-exponents-trend\nrows = []\nfor cv in CVS:\n    for reading in READ9:\n        for agg in \"ab\":\n            A = SV[(\"active\", cv, reading, agg)]\n            Su = session_values(\"active\", cv, reading, agg, kind=\"surrogate\") if (agg == \"a\") else None\n            P = SV[(\"passive\", cv, reading, agg)]\n            for nni in [\"nni_a\", \"nni_b\"]:\n                Nn = SV[(nni, cv, reading, agg)]\n                da = [abs(x.alpha.mean() - 1) for x in (A, P, Nn)]\n                db = [abs(1 - x.beta.mean()) for x in (A, P, Nn)]\n                dz = [x.z.mean() for x in (A, P, Nn)]\n                o_alpha = da[0] > da[1] > da[2]\n                o_beta = db[0] >= db[1] > db[2]\n                o_z = dz[0] < dz[1] < dz[2]\n                p_w = (stats.wilcoxon(A.alpha.dropna() - 1).pvalue, stats.wilcoxon(A.beta.dropna() - 1).pvalue)\n                p_s = (mwu(A.alpha, Su.alpha), mwu(A.beta, Su.beta)) if Su is not None else (np.nan, np.nan)\n                dev_w = p_w[0] < .05 and p_w[1] < .05 and A.alpha.mean() > 1 and A.beta.mean() < 1\n                dev_s = (p_s[0] < .05 and p_s[1] < .05 and A.alpha.mean() > Su.alpha.mean() and A.beta.mean() < Su.beta.mean()\n                         and A.alpha.mean() > 1 and A.beta.mean() < 1) if Su is not None else False\n                nord = o_alpha + o_beta + o_z\n                for test, dev, ps in [(\"a surrogate\", dev_s, p_s), (\"b Wilcoxon vs 1\", dev_w, p_w)]:\n                    if test.startswith(\"a\") and Su is None:\n                        continue\n                    v = \"reproduced\" if dev and nord == 3 else \"partially_reproduced\" if dev and nord == 2 else \"not_reproduced\"\n                    rows.append(dict(cv=cv, O9=\"\".join(reading), O10=agg, O4=nni, test=test, p_alpha=ps[0], p_beta=ps[1],\n                                     deviation=dev, d_alpha=np.round(da, 3).tolist(), d_beta=np.round(db, 3).tolist(),\n                                     z=np.round(dz, 3).tolist(), order_alpha=o_alpha, order_beta=o_beta, order_z=o_z,\n                                     verdict=v))\nBC = pd.DataFrame(rows)\nprint(BC[(BC.cv == \"a\") & (BC.O4 == \"nni_a\")].to_string(index=False))\nprint(\"\\nverdicts over all readings:\", BC.verdict.value_counts().to_dict())\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part8.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && time MPLBACKEND=Agg python dev.py nb_part2.py nb_part8.py 2>&1 | sed -n '/per-window fits/,$p' | cut -c1-260
```

```
<persisted-output>
Output too large (34.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/768bbedf-c9fe-416e-a472-82ebea5461e2/tool-results/b4y3up5dz.txt

Preview (first 2KB):
per-window fits: 64236 in 42 s
windows with a failed fit (NaN), per quantity, real windows:
{'beta_aa': 1, 'alpha_a': 1, 'z_a': 1, 'mu_a': 9, 'beta_ab': 54, 'mu_b': 14, 'beta_ba': 14, 'alpha_b': 14, 'z_b': 14, 'beta_bb': 69}
mu windows with r^2 >= 0.85 (real): reading a 0.017, reading b 0.043
session values computed: 192 (60 s)
cv  O9 O10  sessions  sessions_mu  alpha_mean  beta_mean  mu_mean  z_mean  alpha_sd  beta_sd  mu_sd  z_sd  within
 a aaa   a        97           44       1.481      0.760    1.575   0.156     0.053    0.056  0.181 0.043       1
 a aaa   b        97            1       1.489      0.755    1.531   0.161     0.053    0.054    NaN 0.042       1
 a aab   a        97           88       1.481      0.760    1.567   0.156     0.053    0.056  0.185 0.043       1
 a aab   b        97            2       1.489      0.755    1.451   0.161     0.053    0.054  0.179 0.042       1
 a aba   a        97           44       1.481      0.740    1.575   0.156     0.053    0.058  0.181 0.043       1
 a aba   b        97            1       1.489      0.769    1.531   0.161     0.053    0.065    NaN 0.042       1
 a abb   a        97           88       1.481      0.740    1.567   0.156     0.053    0.058  0.185 0.043       1
 a abb   b        97            2       1.489      0.769    1.451   0.161     0.053    0.065  0.179 0.042       1
 a baa   a        97           44       1.442      0.769    1.575   0.099     0.048    0.041  0.181 0.023       2
 a baa   b        97            1       1.445      0.768    1.531   0.100     0.047    0.040    NaN 0.022       2
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && f=/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/768bbedf-c9fe-416e-a472-82ebea5461e2/tool-results/b4y3up5dz.txt; grep -n -A3 "largest number\|verdicts\|main reading\|surrogate, main\|variant O11" $f | cut -c1-300; grep -n "aaa   a" $f | cut -c1-300
```

```
56:largest number of means within tolerance under a reading: 2 ; readings with 3 or more: 0 of 48
57-per exponent, readings within tolerance: {'alpha': 24, 'beta': 46, 'mu': 0, 'z': 0}
58-
59:main reading, session values (active):
60-        alpha    beta      mu       z
61-count  97.000  97.000  44.000  97.000
62-mean    1.481   0.760   1.575   0.156
--
70:surrogate, main reading: {'alpha': '1.068 +/- 0.007', 'beta': '0.968 +/- 0.007', 'mu': '1.840 +/- 0.191', 'z': '0.037 +/- 0.011'}
71-cv  O9 O10  sessions  sessions_mu  alpha_mean  beta_mean  mu_mean  z_mean  alpha_sd  beta_sd  mu_sd   z_sd  within  p_alpha  p_beta   p_mu    p_z  tests_agree        verdict
72- a aaa   a        97           19      1.4652     0.7638   1.4263  0.1516    0.0572   0.0603 0.3838 0.0393       1   0.0279  0.4835 0.0000 0.4102            3 not_reproduced
73- a aaa   b        97            0      1.4700     0.7554      NaN  0.1557    0.0578   0.0604    NaN 0.0397       1   0.0162  0.7013    NaN 0.3902            2 not_reproduced
--
121:verdicts over readings: {'not_reproduced': 48}
122-
123:variant O11 (b), window values pooled, main reading: {'alpha': '1.80e-66', 'beta': '1.19e-08', 'mu': '0.00e+00', 'z': '8.95e-09'}
124-   O4 cv  O9 O10  sessions  sessions_mu  alpha_mean  beta_mean  mu_mean  z_mean  alpha_sd  beta_sd  mu_sd  z_sd  within  comparisons_hold        verdict
125-nni_a  a aaa   a        97            7       1.398      0.836    1.338   0.192     0.047    0.045  0.084 0.056       1                 7 not_reproduced
126-nni_a  a aaa   b        97            0       1.418      0.826      NaN   0.203     0.051    0.046    NaN 0.061       1                 6 not_reproduced
--
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_part8.py').read()
s=s.replace("nord = o_alpha + o_beta + o_z","nord = int(o_alpha) + int(o_beta) + int(o_z)")
open('nb_part8.py','w').write(s)
EOF
cat > $TMPDIR/nb_part9.py <<'EOF'
# %% [md]
## figs3-exponents-stable-with-threshold

> Exponents computed only from windows with kurtosis above the threshold vary only slightly with the threshold and stay within their error bars.

Criterion: per phase, exponents as in fig4-exponents-active, the session value over the session's windows with kappa > kappa_th (sessions with no such window left out), on the grid from kappa_surr_max to 12. Reproduced when, for every phase and exponent, the mean across sessions stays within one SD across sessions (at kappa_th = kappa_surr_max) of its all-window value, at every grid point with at least 10 sessions contributing. Partially reproduced when it holds for three of the four exponents. Main reading of O9 and O10 (a); the CV readings and O6 are run; the thresholds 4 to 12 are shown as a variant.

# %%
# tags: claim:figs3-exponents-stable-with-threshold


def stable_eval(cv, g, reading=("a", "a", "a"), phases=("active", "passive", "nni_a")):
    rows = []
    for ph in phases:
        base = SV[(ph, cv, reading, "a")]
        sd0 = session_values(ph, cv, reading, "a", kmin=g[0]) if len(g) else None
        for e in EXP:
            allv = base[e].mean()
            sd = sd0[e].std() if sd0 is not None and len(sd0) else np.nan
            worst, npts = 0.0, 0
            for th in g:
                s_ = session_values(ph, cv, reading, "a", kmin=th)
                if s_[e].notna().sum() < 10:
                    continue
                npts += 1
                worst = max(worst, abs(s_[e].mean() - allv))
            rows.append(dict(cv=cv, phase=ph, exponent=e, all_windows=allv, sd_at_lo=sd, points=npts,
                             largest_departure=worst, within=bool(npts > 0 and worst <= sd)))
    return pd.DataFrame(rows)


rows = []
for cv in CVS:
    for sm in SMAXS:
        ksm = surr_max(cv, "a", sm)
        g = grid(ksm, 12)[::10]
        rows.append(dict(cv=cv, O6=sm, kappa_surr_max=ksm, grid_points=len(grid(ksm, 12))))
        if len(g):
            t = stable_eval(cv, g)
            print(f"cv {cv}, O6 {sm}, grid {g[0]} to 12 (every 10th point of the 0.05 grid):")
            print(t.round(3).to_string(index=False))
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("\nvariant, thresholds 4 to 12 in steps of 0.5, cv a:")
VS3 = stable_eval("a", np.arange(4, 12.01, 0.5))
print(VS3.round(3).to_string(index=False))
EOF
cd $TMPDIR && . venv/bin/activate && time MPLBACKEND=Agg python dev.py nb_part2.py nb_part8.py nb_part9.py 2>&1 | sed -n '/^verdicts over all/,$p' | cut -c1-200
```

```
verdicts over all readings: {'partially_reproduced': 144}
cv b, O6 a, grid 8.55 to 12 (every 10th point of the 0.05 grid):
cv   phase exponent  all_windows  sd_at_lo  points  largest_departure  within
 b  active    alpha        1.495     0.063       5              0.021    True
 b  active     beta        0.748     0.082       5              0.022    True
 b  active       mu        1.438     0.114       0              0.000   False
 b  active        z        0.172     0.052       5              0.014    True
 b passive    alpha        1.473     0.058       7              0.030    True
 b passive     beta        0.757     0.075       7              0.013    True
 b passive       mu        1.335     0.139       0              0.000   False
 b passive        z        0.161     0.069       7              0.039    True
 b   nni_a    alpha        1.438     0.055       7              0.020    True
 b   nni_a     beta        0.819     0.066       7              0.014    True
 b   nni_a       mu        1.337     0.016       0              0.000   False
 b   nni_a        z        0.222     0.119       7              0.052    True
cv b, O6 b, grid 10.35 to 12 (every 10th point of the 0.05 grid):
cv   phase exponent  all_windows  sd_at_lo  points  largest_departure  within
 b  active    alpha        1.495     0.048       2              0.013    True
 b  active     beta        0.748     0.048       2              0.016    True
 b  active       mu        1.438       NaN       0              0.000   False
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/fouke-2025/README.md | head -30; python tools/entry.py --help 2>&1 | head -30; grep -n "python" entries/fouke-2025/entry.yaml; ls attempts | grep cambr; ls questions | head -3
```

```
# Fouke, He, Loring & Naumann (2025) from dandiset 001453

Tests the findings of [Fouke et al. (2025)](https://doi.org/10.1016/j.cub.2025.04.027) that can be
tested on [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), which holds the
freely swimming tracking of 25 zebrafish and 12 *Danionella cerebrum* larvae (Figure 1 and Figure
S1). The imaging and head-fixed tail tracking of Figures 2 to 4 are not in it.

| Claim | Outcome |
|---|---|
| The stimulus codes can be linked to the paper's stimuli through its code | Reproduced |
| DC swim faster than ZF, over all stimulus codes | Reproduced |
| Median speed over whole-field stimuli, DC 9.8 and ZF 6.4 mm/s | Reproduced |
| ZF are faster to forward motion than to a static grating (8.8 against 5.0 mm/s) | Reproduced |
| DC do not modulate speed with stimulus direction | Not reproduced |
| DC are faster than ZF for oblique stimuli | Reproduced |
| Both species turn in the direction of motion | Partially reproduced |
| ZF have higher angular acceleration than DC | Not reproduced |
| DC turn less than ZF to monocular stimuli | Reproduced |
| ZF swim in bouts, DC continuously | Reproduced |
| Values from representative trials (Figure 1C, E, F) | Blocked: metadata insufficient |
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "timeout\|max.minutes\|max_minutes" tools/entry.py | head -20
```

```
29:that takes longer than --max-minutes fails, even if it ran without error.
553:def upgrade_python(entry_dir: Path, version: str, before: Path, output_dir: Path, timeout: int,
554:                   max_minutes: float) -> int:
560:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
607:def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
618:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
625:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
627:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
656:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
663:        if ok and seconds > max_minutes * 60:
665:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
731:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
732:    parser.add_argument("--max-minutes", type=float, default=60,
773:                              args.timeout, args.max_minutes)
783:    return run(entry_dir, output_dir, args.timeout, args.max_minutes, args.fresh)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_part1.py').read()
old=s[s.index('| claim | tested |'):s.index('# %%\nimport os')]
new='''| claim | tested or blocked |
|---|---|
| sessions-selected | tested |
| fig3a-kurtosis-broader-than-surrogate | tested |
| fig3c-scaling-hit-rate-higher | analysed; blocked (methods_underspecified) after the analysis |
| fig3c-hit-rate-rises-with-threshold | analysed; blocked (methods_underspecified) after the analysis |
| fig3d-relative-gain-24 | tested |
| figs1-other-window-lengths | tested |
| figs2-strict-units | tested |
| fig4a-active-most-scaling | analysed; blocked (methods_underspecified) after the analysis |
| fig4-exponents-active | tested |
| fig4-exponents-passive | tested |
| fig4-exponents-nni | tested |
| fig4bc-static-exponents-trend | tested |
| figs3-exponents-stable-with-threshold | analysed; blocked (methods_underspecified) after the analysis |
| figs4-initial-kurtosis-poor-predictor | tested |
| figs5a-firing-rate-order | tested |
| figs5c-hit-rate-firing-rate-nonmonotonic | tested |
| figs7-fatigue-halves | tested |
| figs8-halves-and-phase-order | analysed; blocked (methods_underspecified) after the analysis |

The dataset holds everything the claims need, so every claim was analysed. Five are blocked after the analysis because, under the readings adopted, their threshold grid starts at a surrogate maximum above the plotted range (see "How readings decide"). The outcomes are in the summary at the end.

'''
s=s.replace(old,new)
open('nb_part1.py','w').write(s)
EOF
grep -n "Every claim" nb_part1.py
```

```
(Bash completed with no output)
```

**Agent**

Now the decision-rule cell, conclusions and summary, then build the notebook.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > concl.py <<'PYEOF'
C = {}
C["rules"] = '''## How readings decide

The claims file lists readings of details the paper leaves open (O1 to O11). Following the protocol (reader, step 3; author, step 1.6), two kinds are told apart:

- Readings of which trials, windows or subset a reported number counts (O1, O4, O5, and the two ranges of fig3d-relative-gain-24) decide as the criteria say: the claim is reproduced when the result matches under any of them.
- Readings of a method detail (O2, the CV; O6, kappa_surr_max; O8 to O10) decide only when they all give the same outcome. Where they differ, the reading the paper best supports is adopted as an assumption, and the outcome is marked as resting on it. The adopted readings are O2 (a), the CV of the population count: the Appendix describes the CV exclusion as removing rare artefacts ("such high values are not typically observed in awake mice"), and reading (b) removes 9702 of 11639 active windows (printed in the data check) while (a) removes none and (c) 209. O6 (a) for Figure 3 claims, and (b) for Figures 4A and S8, whose shaded area is one for all phases. O9 (a, a, a) and O10 (a), the first listed.

Where the adopted reading leaves a criterion's threshold grid empty, because kappa_surr_max lies above the top of the plotted range, the criterion cannot be applied. The paper's surrogate reference (lowest kurtoses around 6, kappa_surr_max about 7) is far from the one computed here (minimum 2.80, median 3.64, maximum 34.29 in the active phase), so the procedures differ, and such a claim is blocked as `methods_underspecified` (protocol, "Record the attempt", on chance levels), with the result of every reading shown.'''
C["fig3a"] = '''**Result: partially reproduced**, resting on the CV reading (a), an assumption. Real windows spread more than surrogate windows (interquartile range 1.98 against 0.64, active phase), and some real windows exceed kappa_surr_max (largest real 89.8 against 34.29), but the lowest surrogate kurtoses are 2.80 (minimum) and 3.16 (5th percentile), far from 6 +/- 0.6, and the majority condition fails (a fraction of 0.000 of windows, to three decimals, lies above kappa_surr_max). The median kurtosis is 6.18 for real windows against 3.64 for surrogates, and the largest real window exceeds the largest surrogate in 96 of 97 sessions. Under CV reading (c) no real window exceeds kappa_surr_max (31.9 against 34.29), which gives not reproduced; under (b), partially reproduced. Under the five seeds kappa_surr_max ranges from 24.45 to 35.46 and the outcome under CV (a) stays the same.'''
C["fig3c"] = '''**Result: blocked (methods_underspecified).** Under the adopted readings (CV (a); kappa_surr_max over the active surrogate windows, 34.29) the grid from kappa_surr_max to 12.5 is empty, and so it is under CV (c). Only CV (b), which keeps 1937 of 11639 active windows, gives a grid: from 8.55 the scaling hit rate exceeds both comparators at 67.5% of 80 points (not reproduced), and from 10.30 (O6 (b)) at all 44 points (reproduced), with 7 trials above 12.5; under the seed variants that reading gives partially reproduced (seeds +1000 and +4000), not reproduced (+2000) and no grid (+3000). Over thresholds 3 to 15 under the main reading (not the criterion's grid), the scaling hit rate is above both comparators at none of 236 points; it is 0.625 against 0.645 (no scaling) at 8 and 0.591 against 0.642 at 12.'''
C["rises"] = '''**Result: blocked (methods_underspecified)**, for the reason of fig3c-scaling-hit-rate-higher: under CV (a) and (c) the grid is empty. Under CV (b) the scaling hit rate rises (Spearman 0.917 from 8.55, 0.784 from 10.30), which would reproduce the claim. Over thresholds 3 to 12.5 under the main reading (a variant) the Spearman correlation is -0.64 and the scaling hit rate falls from 0.641 to 0.587.'''
C["fig3d"] = '''**Result: not reproduced.** No reading reaches 24 +/- 3 % with a larger gain at 12 than at 8. Under the adopted CV (a), the plotted range is empty and over all thresholds the largest gain is -1.19 % (at 9.85); the gain is -2.99 % at 8 and -7.91 % at 12. CV (c) gives at most 11.54 %. CV (b) gives 66.14 % at 12.40, with 7 trials above it, out of tolerance, and an infinite gain at 3.55 where the no-scaling hit rate is 0. Over thresholds 4 to 15 the main reading's gain ranges from -26.88 to -1.19 %.'''
C["figs1"] = '''**Result: not reproduced.** Neither length passes under any reading. With 10-s windows (CV (a), O5 (a)), the scaling hit rate exceeds the no-scaling one at 50.6 % of the points from 8 to 12, the gain is -0.20 % at 8 and 5.45 % at 12, and the onset is 10.55, outside 7 +/- 0.7. With 60-s windows the scaling hit rate exceeds the no-scaling one at 9.9 % of the points, the gain goes from -1.46 % at 8 to -8.09 % at 12, and there is no onset. The onsets are the same under the five seeds.'''
C["figs2"] = '''**Result: not reproduced**, resting on CV (a), an assumption. No strict reading gives 43 +/- 4.3 sessions: the default quality filters leave 1 session and the good label 68 (from 54 mice). On the 68 sessions with good units, the relative gain at kappa_th = 12 is -15.92 % under CV (a) and -13.30 % under (c), so the result does not hold. Under CV (b) the fig3c test is partially reproduced (93.8 % of 96 points) and the gain at 12 is 66.08 %, resting on 4 trials, which would give partially reproduced.'''
C["fig4a"] = '''**Result: blocked (methods_underspecified).** Under the adopted readings the grid from kappa_surr_max (48.34 over all phases) to 15 is empty, as it is under every reading of CV (a) and (c). Where a grid exists (CV (b)), the order active > passive > NNI holds at none of the points (0 of 130 and of 94), because the NNI phase has the most windows above threshold. Over thresholds 3 to 15 (CV (a), not the criterion's grid), the NNI fraction exceeds the active fraction at each printed threshold from 5 (0.895 against 0.848 at 5; 0.321 against 0.167 at 8), and active exceeds passive; the median kurtosis of a session is higher in the active phase than in NNI (a) in only 16 of 97 sessions, and higher than in passive in 88.'''
C["figs8"] = '''**Result: blocked (methods_underspecified)**, for the grid, as fig4a-active-most-scaling. Where a grid exists (CV (b)), the second half lies above passive at every point, passive lies above NNI at none, and the first half is at or above the second at 60 to 68 % of points. Median kurtosis (CV (a)): first half 6.389, second half 6.026 (Mann-Whitney p = 1.4e-42), passive 5.534, NNI 6.994 (a) and 7.216 (b). The second half is lower than the first, as the paper says, but the NNI phase has the highest kurtosis, not the lowest.'''
C["fig4act"] = '''**Result: not reproduced.** No reading puts more than two of the four means within tolerance (none of 48 readings has three). Under the main reading (O9 (a, a, a), O10 (a), CV (a)) alpha is 1.481 +/- 0.053, beta 0.760 +/- 0.056, mu 1.575 +/- 0.181 (44 sessions have a window with r^2 >= 0.85) and z 0.156 +/- 0.043: beta is within tolerance, alpha is above 1.41 +/- 0.05, mu is about twice the paper's value and z about half. Beta is within tolerance under 46 readings, alpha under 24, mu and z under none. The surrogate windows give alpha 1.068 and beta 0.968.'''
C["fig4pas"] = '''**Result: not reproduced.** All 48 readings fail. Under the main reading alpha is 1.465, beta 0.764, mu 1.426 (19 sessions) and z 0.152, with one mean (beta) within tolerance. Against the active phase (Mann-Whitney, session values): alpha is lower (p = 0.028), beta does not differ (p = 0.48), as the paper says, mu is lower (p < 0.0001), and z does not differ (p = 0.41), where the paper reports passive z higher.'''
C["fig4nni"] = '''**Result: not reproduced.** All 96 readings fail, as none puts three means within tolerance. Under the main reading (NNI (a)) alpha is 1.398, beta 0.836, mu 1.338 (7 sessions) and z 0.192; only beta is within tolerance. Seven of the eight comparisons hold in the stated direction (alpha, beta and z against both phases, mu against active; p from 3.3e-4 to 6.5e-20); mu against passive does not (p = 0.74).'''
C["fig4bc"] = '''**Result: partially reproduced.** Under every reading the deviation holds and one ordering fails. Under the main reading active alpha is above 1 and beta below 1 (Wilcoxon against 1, p = 1.2e-17 for each; against the surrogate session values, p = 2.5e-33 for each), and the distances from the trivial values are ordered active > passive > NNI for alpha (0.481, 0.465, 0.398) and for beta (0.240, 0.236, 0.164). z does not move away from 0 in the stated order: 0.156 active, 0.152 passive, 0.192 NNI.'''
C["figs3"] = '''**Result: blocked (methods_underspecified).** Under CV (a) and (c) the grid from kappa_surr_max (34.29) to 12 is empty. Under CV (b) (grids from 8.55 and 10.35) alpha, beta and z stay within one SD of their all-window values in every phase, and mu has no grid point with 10 sessions. On thresholds 4 to 12 (CV (a), a variant), alpha and beta stay within one SD in every phase, mu and z in the active and passive phases; in NNI, z departs by 0.083 against an SD of 0.056, and mu has no point with 10 sessions.'''
C["figs4"] = '''**Result: reproduced.** The Spearman correlation between kappa_0 and the kurtosis at N/16 across active windows is 0.178 (CV (a), 11639 windows) and 0.190 with all phases; its magnitude is below 0.3 under every reading. Within sessions it ranges from -0.263 to 0.58 (median 0.136).'''
C["figs5a"] = '''**Result: reproduced**, resting on CV (a), an assumption. Under CV (a), at all 141 thresholds from 5 to 12 the mouse-averaged rate is ordered active < NNI < passive (0.166, 0.199 and 0.223 spikes per bin per unit at 5; 0.135, 0.183 and 0.193 at 12), and it decreases with the threshold in every phase (Spearman -0.991 active, -0.976 NNI (a), -0.998 NNI (b), -0.991 passive). CV (c) gives the same. Under CV (b) the order holds at 97.2 % (NNI (a)) or 86.5 % (NNI (b)) of points and the active and passive correlations are -0.58 and -0.53.'''
C["figs5c"] = '''**Result: reproduced.** Under every reading the hit rate below rho_th changes direction by more than one SE. Under CV (a) it rises from 0.601 at 0.05 to 0.751 at 0.11 and falls to 0.654 at 0.20 (SEs 0.037, 0.012 and 0.005). The verdict is the same under the five seeds.'''
C["figs7"] = '''**Result: not reproduced**, resting on CV (a), an assumption. Under CV (a) the relative gain is negative at every point from 8 to 12 in the first half (-7.98 % at 8, -11.22 % at 12) and at all but 1.2 % of the points in the second (-6.77 %, -20.32 %); the overall hit rate is lower in the second half (0.548 against 0.749), as the paper says. CV (c) gives the same. Under CV (b), with 4 and 6 trials above 12, the gain is positive throughout both halves (reproduced with O5 (a)).'''
PYEOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > summary.md <<'EOF'
## Summary

| claim | outcome |
|---|---|
| sessions-selected | not reproduced |
| fig3a-kurtosis-broader-than-surrogate | partially reproduced (assumed) |
| fig3c-scaling-hit-rate-higher | blocked: methods underspecified |
| fig3c-hit-rate-rises-with-threshold | blocked: methods underspecified |
| fig3d-relative-gain-24 | not reproduced |
| figs1-other-window-lengths | not reproduced |
| figs2-strict-units | not reproduced (assumed) |
| fig4a-active-most-scaling | blocked: methods underspecified |
| fig4-exponents-active | not reproduced |
| fig4-exponents-passive | not reproduced |
| fig4-exponents-nni | not reproduced |
| fig4bc-static-exponents-trend | partially reproduced |
| figs3-exponents-stable-with-threshold | blocked: methods underspecified |
| figs4-initial-kurtosis-poor-predictor | reproduced |
| figs5a-firing-rate-order | reproduced (assumed) |
| figs5c-hit-rate-firing-rate-nonmonotonic | reproduced |
| figs7-fatigue-halves | not reproduced (assumed) |
| figs8-halves-and-phase-order | blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** The paper links no code. The kurtosis follows Eqs. 2 to 5 as written, and on these data the ISI-shuffled surrogates give kurtoses around 3.6 (minimum 2.80), where the paper reports surrogate kurtoses no lower than about 6 and a surrogate maximum of about 7; the real windows lie about 2.5 above the surrogates here, so the kurtosis scale of the paper is not reached and the fixed thresholds of the criteria (8, 12, 12.5) do not mean the same here. The surrogate maximum is set by a few windows (34.29 in the active phase), which leaves the plotted threshold ranges above it empty. The analysis set has 97 sessions from 68 mice, not 62 from 44. Units silent in a window are left out of that window. Bootstrap SEs use 10^4 Poisson resamples, not 10^5 resamples of fixed size. The readings of the claims file are all run; where method readings disagree, CV (a) is adopted as an assumption.

**What was found about the dataset.** 153 sessions from 81 mice; no session is deposited twice. 97 sessions (68 mice) have more than 128 V1 units, the `good` label gives 68 (54 mice) and the default quality filters give 1; the paper's 62 sessions (44 mice) and 43 strict sessions match no reading. The stimulus blocks are in the order active, gray screen (10 s), Gabors, gray screen (about 5 min), flashes, passive, where the Appendix puts the gray screen last. Image onsets evoke V1 responses and omitted flashes do not, in every session, so spikes and stimulus tables share a clock. Active windows hold 0 to 4 go trials (median 2), not the "three to five" of the Appendix. A few windows have most V1 units silent (up to 203 of 206 in one window).
EOF
python - <<'EOF'
exec(open('concl.py').read())
parts={i:open(f'nb_part{i}.py').read() for i in range(1,10)}
def before(txt, heading, key):
    m="# %% [md]\n"+heading
    assert m in txt, heading
    return txt.replace(m, "# %% [md]\n"+C[key]+"\n\n"+m,1)
p=parts
p[2]=p[2]+"\n# %% [md]\n"+C["rules"]+"\n"
p[3]=p[3]+"\n# %% [md]\n"+C["fig3a"]+"\n"
p[4]=p[4]+"\n# %% [md]\n"+C["fig3c"]+"\n"
p[5]=before(p[5],"## fig3d-relative-gain-24","rises")+"\n# %% [md]\n"+C["fig3d"]+"\n"
p[6]=before(p[6],"## figs2-strict-units","figs1")+"\n# %% [md]\n"+C["figs2"]+"\n"
for h,k in [("## figs8-halves","fig4a"),("## figs4-initial","figs8"),("## figs5a-firing","figs4"),("## figs5c-hit","figs5a"),("## figs7-fatigue","figs5c")]:
    p[7]=before(p[7],h,k)
p[7]+="\n# %% [md]\n"+C["figs7"]+"\n"
for h,k in [("## fig4-exponents-passive","fig4act"),("## fig4-exponents-nni","fig4pas"),("## fig4bc-static","fig4nni")]:
    p[8]=before(p[8],h,k)
p[8]+="\n# %% [md]\n"+C["fig4bc"]+"\n"
p[9]+="\n# %% [md]\n"+C["figs3"]+"\n\n# %% [md]\n"+open('summary.md').read()+"\n# %%\nprint(f'notebook run time: {(time.time() - T_START) / 60:.1f} min')\n"
full="\n".join(p[i] for i in range(1,10))
open('nb_full.py','w').write(full)
import re, nbformat
cells=[]
for chunk in re.split(r'^# %%', full, flags=re.M)[1:]:
    head, _, body = chunk.partition("\n")
    body=body.strip("\n")
    if head.strip().startswith("[md]"):
        cells.append(nbformat.v4.new_markdown_cell(body))
    else:
        tags=[]
        lines=body.split("\n")
        if lines and lines[0].startswith("# tags:"):
            tags=[t.strip() for t in lines[0][7:].split(",")]
            lines=lines[1:]
        c=nbformat.v4.new_code_cell("\n".join(lines))
        if tags: c.metadata["tags"]=tags
        cells.append(c)
nb=nbformat.v4.new_notebook(); nb.cells=cells
nb.metadata["kernelspec"]={"name":"python3","display_name":"Python 3","language":"python"}
nbformat.write(nb,'entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb')
print(len(cells), sum(1 for c in cells if c.cell_type=='code'))
print([c.metadata.get('tags') for c in cells if c.metadata.get('tags')])
EOF
```

```
73 27
[['sanity'], ['claim:sessions-selected'], ['claim:fig3a-kurtosis-broader-than-surrogate'], ['claim:fig3c-scaling-hit-rate-higher'], ['claim:fig3c-scaling-hit-rate-higher'], ['claim:fig3c-hit-rate-rises-with-threshold'], ['claim:fig3d-relative-gain-24'], ['claim:figs1-other-window-lengths'], ['claim:figs2-strict-units'], ['claim:fig4a-active-most-scaling'], ['claim:figs8-halves-and-phase-order'], ['claim:figs4-initial-kurtosis-poor-predictor'], ['claim:figs5a-firing-rate-order'], ['claim:figs5c-hit-rate-firing-rate-nonmonotonic'], ['claim:figs7-fatigue-halves'], ['claim:fig4-exponents-active'], ['claim:fig4-exponents-passive'], ['claim:fig4-exponents-nni'], ['claim:fig4bc-static-exponents-trend'], ['claim:figs3-exponents-stable-with-threshold']]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -i 's/A few windows have most V1 units silent (up to 203 of 206 in one window)./In a few windows most V1 units are silent (up to 203 units in one window)./' $TMPDIR/summary.md && grep -c "up to 203 units" $TMPDIR/summary.md; cat > entries/cambrainha-2025/requirements.in <<'EOF'
dandi
h5py
matplotlib
numpy
pandas
remfile
requests
scipy
EOF
cat > entries/cambrainha-2025/entry.yaml <<'EOF'
schema_version: 1
name: cambrainha-2025
type: reproduction
title: Kurtosis of coarse-grained V1 activity and task performance (Cambrainha et al. 2025)
description: Tests the findings of Cambrainha, Castro, de Vasconcelos, Carelli and Copelli (2025)
  on dandiset 000713, the Allen Institute Visual Behavior Neuropixels data. It computes, per 30-s
  window of V1 spiking, the kurtosis after momentum-space coarse graining and its ISI-shuffled
  surrogate, relates it to the hit rate of the change-detection task, compares the active,
  passive and non-natural image phases, and fits the real-space renormalization exponents.
license: Apache-2.0
notebooks:
- path: reproduce_cambrainha_2025.ipynb
  title: Reproducing Cambrainha et al. (2025) from dandiset 000713
  runtime_minutes: 30
helpers:
- criticality.py
related:
- id: dandi:000713/0.240702.1725
  relation: uses_data
- id: doi:10.1103/w49n-2vz8
  relation: reproduces
EOF
date -u
```

```
1
Fri Nov 27 08:12:56 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > build.py <<'EOF'
exec(open('concl.py').read())
parts={i:open(f'nb_part{i}.py').read() for i in range(1,10)}
def before(txt, heading, key):
    m="# %% [md]\n"+heading
    assert m in txt, heading
    return txt.replace(m, "# %% [md]\n"+C[key]+"\n\n"+m,1)
p=parts
p[2]=p[2]+"\n# %% [md]\n"+C["rules"]+"\n"
p[3]=p[3]+"\n# %% [md]\n"+C["fig3a"]+"\n"
p[4]=p[4]+"\n# %% [md]\n"+C["fig3c"]+"\n"
p[5]=before(p[5],"## fig3d-relative-gain-24","rises")+"\n# %% [md]\n"+C["fig3d"]+"\n"
p[6]=before(p[6],"## figs2-strict-units","figs1")+"\n# %% [md]\n"+C["figs2"]+"\n"
for h,k in [("## figs8-halves","fig4a"),("## figs4-initial","figs8"),("## figs5a-firing","figs4"),("## figs5c-hit","figs5a"),("## figs7-fatigue","figs5c")]:
    p[7]=before(p[7],h,k)
p[7]+="\n# %% [md]\n"+C["figs7"]+"\n"
for h,k in [("## fig4-exponents-passive","fig4act"),("## fig4-exponents-nni","fig4pas"),("## fig4bc-static","fig4nni")]:
    p[8]=before(p[8],h,k)
p[8]+="\n# %% [md]\n"+C["fig4bc"]+"\n"
p[9]+="\n# %% [md]\n"+C["figs3"]+"\n\n# %% [md]\n"+open('summary.md').read()+"\n# %%\nprint(f'notebook run time: {(time.time() - T_START) / 60:.1f} min')\n"
full="\n".join(p[i] for i in range(1,10))
open('nb_full.py','w').write(full)
import re, nbformat
cells=[]
for chunk in re.split(r'^# %%', full, flags=re.M)[1:]:
    head, _, body = chunk.partition("\n")
    body=body.strip("\n")
    if head.strip().startswith("[md]"):
        cells.append(nbformat.v4.new_markdown_cell(body))
    else:
        tags=[]
        lines=body.split("\n")
        if lines and lines[0].startswith("# tags:"):
            tags=[t.strip() for t in lines[0][7:].split(",")]
            lines=lines[1:]
        c=nbformat.v4.new_code_cell("\n".join(lines))
        if tags: c.metadata["tags"]=tags
        cells.append(c)
nb=nbformat.v4.new_notebook(); nb.cells=cells
nb.metadata["kernelspec"]={"name":"python3","display_name":"Python 3","language":"python"}
nbformat.write(nb,'entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb')
print(len(cells))
EOF
. venv/bin/activate && python build.py && cd  && python tools/entry.py lock entries/cambrainha-2025 2>&1 | tail -5 && python tools/entry.py check entries/cambrainha-2025 2>&1 | tail -20
```

```
73
wrote cambrainha-2025/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import sys, time
sys.path.insert(0,'entries/cambrainha-2025')
import criticality as cr
t=time.time(); a=cr.session_assets(); print(len(a), time.time()-t, a[0])
print(cr.survey(a[0]))
EOF
```

```
153 2.448676109313965 {'path': 'sub-506940/sub-506940_ses-20200817T222149.nwb', 'asset_id': '9c7ce5d4-1f01-4685-a45f-18c3393a50d3', 'size': 2759138245}
{'path': 'sub-506940/sub-506940_ses-20200817T222149.nwb', 'subject': '506940', 'session': '1043752325', 'session_type': 'EPHYS_1_images_G_5uL_reward', 'n_units': 2207, 'visp_all': 231, 'visp_good': 194, 'visp_default': 66, 'visp_valid': 231, 'visp_good_valid': 194, 'visp_spikes': 7868260, 'total_spikes': 117633702, 'n_trials': 969, 'locations': [np.str_('APN'), np.str_('CA1'), np.str_('CA3'), np.str_('DG'), np.str_('DT'), np.str_('LGd'), np.str_('LP'), np.str_('MB'), np.str_('MGd'), np.str_('MGm'), np.str_('MGv'), np.str_('MRN'), np.str_('PIL'), np.str_('POL'), np.str_('SGN'), np.str_('SNr'), np.str_('SUB'), np.str_('TH'), np.str_('VISal'), np.str_('VISam'), np.str_('VISl'), np.str_('VISp'), np.str_('VISpm'), np.str_('VISrl')]}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd  && python tools/entry.py all entries/cambrainha-2025 2>&1 | tail -20; date -u
```

```
Fri Nov 27 08:13:25 UTC 2026
    return pd.DataFrame(rows)
------------------


[31m---------------------------------------------------------------------------[39m
[31mIndexError[39m                                Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[21][39m[32m, line 4[39m
[32m      1[39m t0 = time.time()
[32m      2[39m fit_rows = []
[32m      3[39m [38;5;28;01mfor[39;00m r [38;5;28;01min[39;00m ok:
[32m----> [39m[32m4[39m     [38;5;28;01mif[39;00m r[[33m"meta"[39m][[33m"path"[39m] [38;5;28;01mnot[39;00m [38;5;28;01min[39;00m sel_gt:
[32m      5[39m         [38;5;28;01mcontinue[39;00m
[32m      6[39m     [38;5;28;01mfor[39;00m w [38;5;28;01min[39;00m r[[33m"windows"[39m]:
[32m      7[39m         [38;5;28;01mif[39;00m [33m"rs"[39m [38;5;28;01mnot[39;00m [38;5;28;01min[39;00m w:

[31mIndexError[39m: invalid index to scalar variable.


0 error(s)
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/^ok = \[r for r in results if "error" not in r\]/ok = [r for r in results if "error" not in r]\nsessions_ok = ok/' nb_part2.py && sed -i 's/^for r in ok:/for r in sessions_ok:/' nb_part8.py && grep -n "sessions_ok" nb_part2.py nb_part8.py && grep -n "in ok\b\|in ok:" nb_part*.py
```

```
nb_part2.py:7:sessions_ok = ok
nb_part8.py:9:for r in sessions_ok:
nb_part8.py:28:for r in sessions_ok:
nb_part2.py:15:print("spike times sorted within every unit:", all(r["spikes_sorted"] for r in ok))
nb_part2.py:19:for r in ok:
nb_part2.py:31:                    for r in ok])
nb_part2.py:39:for r in ok:
nb_part2.py:61:clk = pd.DataFrame([dict(path=r["meta"]["path"], **r["clock"]) for r in ok])
nb_part2.py:93:res_of = {r["meta"]["path"]: r for r in ok}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
ls executed/cambrainha-2025/ && python - <<'EOF'
import nbformat
nb=nbformat.read('executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    txt="".join(o.get('text','') for o in c.get('outputs',[]) if o.get('output_type')=='stream')
    if i<12 or 'claim:sessions-selected' in str(c.metadata) or 'figs2' in str(c.metadata):
        print('=== cell',i,c.metadata.get('tags')); print(txt[:3500])
EOF
```

```
Exit code 1
result.json
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 169, in read
    buf = fp.read()
          ^^^^^^^
AttributeError: 'str' object has no attribute 'read'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 171, in read
    with open(fp, encoding="utf8") as f:  # noqa: PTH123
         ~~~~^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && time MPLBACKEND=Agg python dev.py nb_part2.py nb_part3.py nb_part4.py nb_part5.py nb_part6.py nb_part7.py nb_part8.py nb_part9.py > devall.txt 2>&1; tail -5 devall.txt; grep -n "Error\|Traceback" devall.txt | head
```

```
real	4m55.308s
user	4m16.610s
sys	0m38.522s
 a passive        z        0.152     0.040      17              0.022    True
 a   nni_a    alpha        1.398     0.046      17              0.036    True
 a   nni_a     beta        0.836     0.045      17              0.010    True
 a   nni_a       mu        1.338     0.084       0              0.000   False
 a   nni_a        z        0.192     0.056      17              0.083   False
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python build.py && cd  && date -u && python tools/entry.py all entries/cambrainha-2025 2>&1 | tail -6; date -u
```

```
73
Fri Nov 27 08:42:10 UTC 2026
Installed kernelspec registry-cambrainha-2025 in executed/cambrainha-2025/.venv/share/jupyter/kernels/registry-cambrainha-2025
0 error(s)
pass  reproduce_cambrainha_2025.ipynb  (1445 s)
Fri Nov 27 09:06:29 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF' > $TMPDIR/exec_out.txt
import nbformat
nb=nbformat.read(open('executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'),4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    txt="".join(o.get('text','') for o in c.get('outputs',[]) if o.get('output_type')=='stream' and o.get('name')=='stdout')
    print('=== cell',i,c.metadata.get('tags')); print(txt)
EOF
wc -l $TMPDIR/exec_out.txt; sed -n 1,75p $TMPDIR/exec_out.txt
```

```
888 /tmp/claude-1001/exec_out.txt
=== cell 1 None
dandiset 000713 version 0.240702.1725

=== cell 3 None
session files: 153  subjects: 81
session types: {'EPHYS_1_images_G_3uL_reward': 74, 'EPHYS_1_images_H_3uL_reward': 71, 'EPHYS_1_images_G_5uL_reward': 4, 'EPHYS_1_images_H_5uL_reward': 4}
structures with 'VIS' in their name: [np.str_('VIS'), np.str_('VISal'), np.str_('VISam'), np.str_('VISl'), np.str_('VISp'), np.str_('VISpm'), np.str_('VISrl'), np.str_('VISrll')]
duplicated session identifiers: 0 ; sessions sharing total spike count and unit count: 0
       n_units  visp_all  visp_good  visp_default  visp_valid  n_trials
count    153.0     153.0      153.0         153.0       153.0     153.0
mean    2085.1     141.0      121.8          53.2       141.0     682.4
std      447.3      47.7       42.7          23.6        47.7     174.1
min     1103.0       0.0        0.0           0.0         0.0     429.0
25%     1785.0     113.0       95.0          38.0       113.0     574.0
50%     2024.0     144.0      125.0          50.0       144.0     631.0
75%     2364.0     169.0      148.0          70.0       169.0     729.0
max     3388.0     294.0      268.0         132.0       294.0    1597.0

=== cell 5 None
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 75,330p $TMPDIR/exec_out.txt | cut -c1-250
```

```
O5 (b): trials placed in active windows 22919, hits 14798, trials outside every window 43; overall hit rate 0.646
trials per active window: median 2.0 range 0 to 4

kappa_surr_max under each reading (claim seed):
cv kappa O6  kappa_surr_max
 a     a  a          34.292
 a     a  b          48.341
 a     b  a          34.292
 a     b  b          48.341
 b     a  a           8.532
 b     a  b          10.302
 b     b  a           8.532
 b     b  b          10.302
 c     a  a          34.292
 c     a  b          34.292
 c     b  a          34.292
 c     b  b          34.292

=== cell 13 None
largest |kappa_a - kappa_b| over windows: 1.4210854715202004e-14 ; surrogate: 8.881784197001252e-15
[... 236 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 330,600p $TMPDIR/exec_out.txt | cut -c1-220
```

```
0  c  b           34.29                     NaN
        1000  a  a           25.15                     NaN
        1000  a  b           52.01                     NaN
        1000  b  a            7.58                   66.14
        1000  b  b           10.03                   66.14
        1000  c  a           16.58                     NaN
        1000  c  b           27.03                     NaN
        2000  a  a           25.47                     NaN
        2000  a  b           46.34                     NaN
        2000  b  a            8.81                   66.14
        2000  b  b            8.81                   66.14
        2000  c  a           19.93                     NaN
        2000  c  b           22.32                     NaN
        3000  a  a           24.45                     NaN
        3000  a  b           52.57                     NaN
        3000  b  a           13.37                     NaN
        3000  b  b           13.37                     NaN
        3000  c  a           15.73                     NaN
        3000  c  b           20.74                     NaN
        4000  a  a           35.46                     NaN
[... 251 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "verdicts\|largest number\|per exponent\|surrogate, main\|main reading p-values\|variant O11\|notebook run time\|aaa   a" $TMPDIR/exec_out.txt | cut -c1-250; sed -n '/claim:fig4bc/,/verdicts over all/p' $TMPDIR/exec_out.txt | head -8 | cut -c1-250
```

```
582: a aaa   a        97           44       1.481      0.760    1.575   0.156     0.053    0.056  0.181 0.043       1
598: b aaa   a        64           20       1.495      0.748    1.438   0.172     0.060    0.067  0.105 0.062       1
614: c aaa   a        97           44       1.482      0.760    1.565   0.156     0.053    0.055  0.175 0.042       1
631:largest number of means within tolerance under a reading: 2 ; readings with 3 or more: 0 of 48
632:per exponent, readings within tolerance: {'alpha': 24, 'beta': 46, 'mu': 0, 'z': 0}
645:surrogate, main reading: {'alpha': '1.068 +/- 0.007', 'beta': '0.968 +/- 0.007', 'mu': '1.840 +/- 0.191', 'z': '0.037 +/- 0.011'}
649: a aaa   a        97           19      1.4652     0.7638   1.4263  0.1516    0.0572   0.0603 0.3838 0.0393       1   0.0279  0.4835 0.0000 0.4102            3 not_reproduced
665: b aaa   a        91           17      1.4734     0.7573   1.3347  0.1606    0.0594   0.0632 0.0693 0.0426       1   0.0170  0.3901 0.0013 0.3512            3 not_reproduced
681: c aaa   a        97           18      1.4653     0.7638   1.3401  0.1516    0.0571   0.0603 0.0813 0.0392       1   0.0297  0.4491 0.0000 0.4030            3 not_reproduced
698:verdicts over readings: {'not_reproduced': 48}
700:variant O11 (b), window values pooled, main reading: {'alpha': '1.80e-66', 'beta': '1.19e-08', 'mu': '0.00e+00', 'z': '8.95e-09'}
704:nni_a  a aaa   a        97            7       1.398      0.836    1.338   0.192     0.047    0.045  0.084 0.056       1                 7 not_reproduced
720:nni_a  b aaa   a        69            7       1.438      0.819    1.337   0.222     0.051    0.051  0.095 0.067       1                 7 not_reproduced
736:nni_a  c aaa   a        97            7       1.398      0.836    1.338   0.192     0.047    0.045  0.084 0.056       1                 7 not_reproduced
752:nni_b  a aaa   a        97           10       1.436      0.821    1.360   0.198     0.049    0.046  0.103 0.055       1            
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_part2.py').read()
s=s.replace('''print(dur.describe().loc[["min", "50%", "max"]].round(2).to_string())''','''print(dur.describe().loc[["min", "50%", "max"]].round(2).to_string())
print("sessions with more than 30 min between the active and passive blocks:",
      dur[dur.nni_a > 30][["path", "nni_a"]].round(2).to_dict("records"))''')
old=s[s.index("The checks above show:"):s.index("# %% [md]\n## Common definitions")]
new='''The checks above show:

- 153 session files from 81 mice, no session deposited twice (identifiers unique, and no two sessions share their unit and spike counts). Units are assigned to structures by their peak channel; besides VISp, some channels are labelled only `VIS` (a visual area not named), and those units are not counted as V1.
- Every analysed session has the blocks the paper describes, but in a different order from the Appendix: block 0 is the active task (about 60 min), then a 10-s gray screen, the Gabor block (about 15 min), a gray screen of about 5 min, the full-field flashes (about 5 min), and block 5, the passive replay (about 60 min). The Appendix says the gray screen comes last, after the flashes; the files put it between the Gabors and the flashes. In one session (printed above) the time between the active and passive blocks is 80.8 min, not about 26, so its NNI (a) phase holds more windows.
- Hits and misses together are the non-aborted go trials; auto-rewarded trials are flagged apart and are not go trials. An active window holds 0 to 4 go trials with an outcome (median 2), fewer than the "three to five trials" of Appendix 5.
- Image onsets of the active block evoke a V1 response 30 to 130 ms later and omitted flashes do not: the difference is at least 4.0 standard errors in every session, and more than 5 in 96 of 98. The spike times and the stimulus tables therefore share a clock, as far as this check shows. The trials table comes from the same stimulus frames; 43 of its outcome trials fall outside every active window (printed below).

'''
s=s.replace(old,new)
open('nb_part2.py','w').write(s)
c=open('concl.py').read()
c=c.replace("CV (c) gives at most 11.54 %.","With auto-rewarded trials kept as hits (O5 (b)) the largest gain is 54.89 % at 39.50, resting on 2 trials, and the gain at 12 (-5.63 %) is below that at 8 (-2.21 %). CV (c) gives at most 11.54 %.")
open('concl.py','w').write(c)
EOF
grep -c "54.89" $TMPDIR/concl.py
```

```
1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_part2.py').read()
s=s.replace("In one session (printed above) the time between the active and passive blocks is 80.8 min, not about 26, so its NNI (a) phase holds more windows.","Where the time between the active and passive blocks is longer than the usual 26 min (sessions printed above, up to 80.8 min), the NNI (a) phase holds more windows.")
open('nb_part2.py','w').write(s)
EOF
cd  ls schemas; sed -n '/^findings:/,$p' attempts/fouke-2025-01.yaml | head -60
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
- kind: metadata_insufficient
  statement: The stimulus codes 0 to 20 have no names or description in the files or the
    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
    file of its stimulus software.
- kind: code_mismatch
  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
    while its conversion of the stimulus software's names gives the reverse (it carries a remap
    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
    only if the fish turn with lateral motion.
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required')); print(list(s['properties']))
d=s.get('\$defs',s.get('definitions',{}))
for k in d: print(k, d[k].get('required'), list(d[k].get('properties',{}))[:30])
" | head -60
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs', 'findings_review']
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
print(json.dumps(p['provenance'],indent=0)[:1500])
o=p['outcomes']['items']; print(o.get('required'), list(o['properties']))
print(json.dumps(o['properties'].get('blocked_by'))[:400])
f=p['findings']['items']; print(json.dumps(f)[:1500])
"
```

```
{
"type": "object",
"additionalProperties": false,
"required": [
"kind",
"accountable"
],
"properties": {
"kind": {
"enum": [
"agent",
"person"
]
},
"accountable": {
"description": "The person or organisation responsible for this attempt.",
"type": "object",
"additionalProperties": false,
"required": [
"name"
[... 61 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "content": "schema_version: 3\nid: cambrainha-2025-01\ndatasets:\n- archive: dandi\n  id: \"000713\"\n  version: 0.240702.1725\n  doi: 10.48324/dandi.000713/0.240702.1725\n  relation: primary\npaper: doi:10.1103/w49n-2vz8\ndate: 2026-11-27\nentry: cambrainha-2025\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-18\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/encorescience/encore-registry/actions/runs/45957776408\noutcomes:\n- claim: sessions-selected\n  outcome: not_reproduced\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:sessions-selected\n  measured:\n  - 97\n  - 68\n  notes: With all units whose peak channel is in VISp (O1 (a)), 97 sessions from 68 mice have more\n    than 128 V1 units (98 with at least 128). The default quality filters (O1 (b); ISI violations\n    below 0.5, amplitude cutoff below 0.1, presence ratio above 0.95) leave 1 session. As variants,\n    the `good` label gives 68 sessions (within 62 +/- 6.2) but from 54 mice (outside 44 +/- 4.4),\n    and the valid-channel flag changes nothing. No reading gives both counts. The 97 sessions of\n    reading (a) are the analysis set of every other claim.\n  deviations:\n  - The paper does not say how units were assigned to V1 or which sessions were dropped; units are\n    assigned by the structure of their peak channel (`electrodes.location == VISp`).\n- claim: fig3a-kurtosis-broader-than-surrogate\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig3a-kurtosis-broader-than-surrogate\n  measured:\n  - 2.80\n  notes: Active phase, CV reading (a). The real windows spread more than their surrogates\n    (interquartile range 1.98 against 0.64; median kurtosis 6.18 against 3.64), and some real\n    windows exceed kappa_surr_max (largest real 89.8 against 34.29), but the lowest surrogate\n    kurtoses are 2.80 (minimum) and 3.16 (5th percentile), far from 6 +/- 0.6, and fewer than 0.1%\n    of windows lie above kappa_surr_max, so the majority condition fails. The largest real window\n    exceeds the largest surrogate in 96 of 97 sessions. CV reading (c) gives not reproduced (no\n    real window above 34.29, largest 31.9); reading (b) gives partially reproduced. All phases\n    pooled give the same. Over the five seeds kappa_surr_max is 34.29, 25.15, 25.47, 24.45 and\n    35.46 and the minimum 2.80, 2.57, 2.55, 2.82 and 2.83; the outcome is the same under each. The\n    two poolings of O3 give identical values (psi has unit variance per unit, so the pooled\n    kurtosis is the mean of the unit kurtoses).\n  deviations:\n  - CV readings disagree (a and b partially reproduced, c not reproduced); reading (a), the CV of\n    the population count, is adopted as an assumption. The Appendix describes the CV > 5 exclusion\n    as removing rare artefacts not seen in awake mice; reading (b) removes 9702 of 11639 active\n    windows, (a) none and (c) 209.\n  - Units with no spike in a window are left out of that window (median 14 per window), a standard\n    choice, since they cannot be normalised (Eq. 5).\n  - The surrogate permutes the intervals between the window start, the unit's spikes and the window\n    end, a standard implementation of the Appendix 2 shuffle.\n- claim: fig3c-scaling-hit-rate-higher\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig3c-scaling-hit-rate-higher\n  notes: The criterion's grid runs from kappa_surr_max to 12.5. Under the adopted CV reading (a),\n    kappa_surr_max is 34.29 (O6 (a)) or 48.34 (O6 (b)), and under (c) 34.29, so the grid is empty\n    and the criterion cannot be applied. The surrogate reference here (minimum 2.80, median 3.64,\n    maximum 34.29) is far from the paper's (lowest about 6, maximum about 7), so the procedures\n    differ, and the claim is blocked as the protocol asks for a reference far from the paper's.\n    Only CV reading (b), which keeps 1937 of 11639 active windows, gives a grid. From 8.55 the\n    scaling hit rate beats both comparators at 67.5% of 80 points (not reproduced); from 10.30\n    (O6 (b)) at all 44 points (reproduced), with 7 trials above 12.5. Under the seed variants that\n    reading gives partially reproduced (+1000, +4000), not reproduced (+2000) and no grid (+3000).\n    Over the thresholds 3 to 15 under CV (a), not the criterion's grid, the scaling hit rate is\n    above both comparators at none of 236 points (0.625 against 0.645 for no scaling at 8, 0.591\n    against 0.642 at 12; trial-shuffled 0.596 and 0.602). Trials placed by start time give 31.2%\n    of points under CV (b). Question for the authors. How is the kurtosis computed so that\n    surrogate windows give values of 6 or more, and is kappa_surr_max the maximum over every\n    surrogate window or a summary less sensitive to single windows?\n  deviations:\n  - Readings of method details (O2, O6) decide only where they agree, and otherwise the reading\n    the paper best supports is adopted (protocol, reader step 3 and author step 1.6), though the\n    criterion says reproduced under one reading. Taken as written, the criterion would give\n    reproduced, from CV (b) with O6 (b) alone, under the claim seed only.\n  - Bootstrap SEs use 10^4 Poisson resamples over windows, not 10^5 resamples of fixed size (a\n    standard approximation that lets one draw serve every threshold).\n  - The trial shuffle follows Appendix 6 as written (each trial swaps its outcome with a random\n    trial of the session), 500 repetitions.\n- claim: fig3c-hit-rate-rises-with-threshold\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig3c-hit-rate-rises-with-threshold\n  notes: Blocked for the reason of fig3c-scaling-hit-rate-higher; under CV (a) and (c) the grid\n    from kappa_surr_max to 12.5 is empty. Under CV (b) the scaling hit rate rises (Spearman 0.917\n    from 8.55 and 0.784 from 10.30, rises of 0.359 and 0.222 against SE sums of 0.039 and 0.073;\n    reproduced, and so under four seed variants, with no grid under +3000). Over 3 to 12.5 under\n    CV (a), a variant, the Spearman correlation is -0.64 and the hit rate falls from 0.641 to 0.587.\n  deviations:\n  - As for fig3c-scaling-hit-rate-higher.\n- claim: fig3d-relative-gain-24\n  outcome: not_reproduced\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig3d-relative-gain-24\n  measured:\n  - -1.19\n  notes: No reading gives a maximum within 24 +/- 3% together with a larger gain at 12 than at 8.\n    Under CV (a) the plotted range (reading (a)) is empty; over all thresholds (reading (b)) the\n    largest gain is -1.19% (at 9.85), given as measured, with -2.99% at 8 and -7.91% at 12. With\n    auto-rewarded trials as hits (O5 (b)) the largest is 54.89% at 39.50, on 2 trials, and the gain\n    falls from 8 to 12. CV (c) gives at most 11.54%. CV (b) gives 66.14% at 12.40 on 7 trials, and\n    an infinite gain at 3.55 where the no-scaling hit rate is 0. Over 4 to 15 under CV (a) the gain\n    ranges from -26.88% to -1.19%, with bootstrap SEs of 1.2% to 7.8%.\n  deviations:\n  - Bootstrap SEs use 10^4 Poisson resamples (the error of Eq. 13, O8 (c)).\n- claim: figs1-other-window-lengths\n  outcome: not_reproduced\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs1-other-window-lengths\n  notes: Neither length passes under any reading. 10-s windows (CV (a), O5 (a)) have the scaling hit\n    rate above the no-scaling one at 50.6% of the points from 8 to 12, a gain of -0.20% at 8 and\n    5.45% at 12, and an onset of 10.55 (out of 7 +/- 0.7). 60-s windows have it at 9.9% of points,\n    a gain of -1.46% at 8 and -8.09% at 12, and no onset. The onsets are the same under the five\n    seeds.\n  deviations:\n  - The onset is searched from kappa 3 (the Gaussian value) to 12, a standard choice; the\n    criterion gives no lower end.\n- claim: figs2-strict-units\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs2-strict-units\n  measured:\n  - 1\n  notes: Neither strict reading gives 43 +/- 4.3 sessions. The default quality filters (reading\n    (i), given as measured) leave 1 session, the good label (ii) 68 from 54 mice. On the 68\n    sessions with their good units, the relative gain at kappa_th = 12 is -15.92% under CV (a) and\n    -13.30% under (c), so the result does not hold either. Under CV (b) the fig3c test is partially\n    reproduced (93.8% of 96 points) and the gain at 12 is 66.08% on 4 trials, which would give\n    partially reproduced; across the five seeds of the strict surrogate that reading gives\n    partially reproduced or reproduced. On the single default-filter session the gain at 12 is\n    -100% on 2 trials.\n  deviations:\n  - CV readings disagree (a and c not reproduced, b partially reproduced); reading (a) is adopted\n    as an assumption, as for fig3a-kurtosis-broader-than-surrogate.\n  - kappa_surr_max of the strict analysis is taken over its own active surrogate windows (O6 (a));\n    the other phases were not analysed with strict units.\n- claim: fig4a-active-most-scaling\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig4a-active-most-scaling\n  notes: Under the adopted readings (CV (a), O6 (b)) the grid from kappa_surr_max (48.34) to 15 is\n    empty, as under every reading of CV (a) and (c), for the reason given under\n    fig3c-scaling-hit-rate-higher. Where a grid exists (CV (b)), the order active > passive > NNI\n    holds at none of the points (0 of 130 and of 94), as the NNI phase has the most windows above\n    every threshold. Over 3 to 15 under CV (a), a variant, the NNI fraction is above the active one\n    at every printed threshold from 5 (0.895 against 0.848 at 5, 0.321 against 0.167 at 8), and\n    active is above passive. The median kurtosis of a session is higher in the active phase than\n    in NNI (a) in 16 of 97 sessions and higher than in the passive phase in 88.\n  deviations:\n  - As for fig3c-scaling-hit-rate-higher.\n- claim: fig4-exponents-active\n  outcome: not_reproduced\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig4-exponents-active\n  measured:\n  - 1.481\n  - 0.760\n  - 1.575\n  - 0.156\n  notes: No reading of O2, O9 and O10 puts more than two of the four means within tolerance (none of\n    48 has three). Main reading, mean +/- SD over 97 sessions, alpha 1.481 +/- 0.053, beta 0.760\n    +/- 0.056, mu 1.575 +/- 0.181 (44 sessions with a window of r^2 >= 0.85; 1.7% of windows pass\n    that rule) and z 0.156 +/- 0.043. Beta is within tolerance under 46 readings, alpha under 24,\n    mu and z under none. Surrogate windows give alpha 1.068 and beta 0.968.\n  deviations:\n  - F is fitted only over cluster sizes where P_silence > 0 (with at least three sizes), as -log 0\n    cannot be fitted; with 50-ms bins large clusters are never silent.\n  - tau_c is searched up to 2 s of lags, a standard limit.\n- claim: fig4-exponents-passive\n  outcome: not_reproduced\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig4-exponents-passive\n  measured:\n  - 1.465\n  - 0.764\n  - 1.426\n  - 0.152\n  notes: All 48 readings fail. Main reading, alpha 1.465, beta 0.764, mu 1.426 (19 sessions) and z\n    0.152, with beta alone within tolerance. Mann-Whitney against the active phase on session\n    values, alpha lower (p = 0.028), beta no difference (p = 0.48, as in the paper), mu lower\n    (p < 0.0001), z no difference (p = 0.41), where the paper reports a higher passive z (p = 6e-5).\n    With window values pooled (O11 (b)) every comparison is significant.\n- claim: fig4-exponents-nni\n  outcome: not_reproduced\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig4-exponents-nni\n  measured:\n  - 1.398\n  - 0.836\n  - 1.338\n  - 0.192\n  notes: All 96 readings fail, as none puts three means within tolerance. Main reading (NNI (a)),\n    alpha 1.398, beta 0.836, mu 1.338 (7 sessions) and z 0.192, with beta alone within tolerance.\n    Seven of the eight comparisons hold in the stated direction (p from 3.3e-4 to 6.5e-20); mu\n    against passive does not (p = 0.74).\n- claim: fig4bc-static-exponents-trend\n  outcome: partially_reproduced\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig4bc-static-exponents-trend\n  notes: Every reading gives partially reproduced. Main reading, active alpha above 1 and beta below\n    1, deviating significantly (Wilcoxon against 1, p = 1.2e-17 for each; against surrogate session\n    values, p = 2.5e-33 for each). Distances from the trivial values are ordered active > passive >\n    NNI for alpha (0.481, 0.465, 0.398) and beta (0.240, 0.236, 0.164). z is 0.156 active, 0.152\n    passive and 0.192 NNI, so it does not move away from 0 from active to passive. The surrogate\n    exponents use the claim seed of the fig3a surrogate only; the Wilcoxon reading needs no\n    surrogate and gives the same outcome.\n- claim: figs3-exponents-stable-with-threshold\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs3-exponents-stable-with-threshold\n  notes: Under CV (a) and (c) the grid from kappa_surr_max (34.29) to 12 is empty, for the reason\n    given under fig3c-scaling-hit-rate-higher. Under CV (b) (grids from 8.55 and 10.35) alpha, beta\n    and z stay within one SD of their all-window values in every phase, and mu has no point with 10\n    sessions. On thresholds 4 to 12 under CV (a), a variant, alpha and beta stay within one SD in\n    every phase, mu and z in the active and passive phases; in NNI z departs by 0.083 against an SD\n    of 0.056 and mu has no point with 10 sessions.\n  deviations:\n  - The grid was evaluated at every tenth point of the 0.05 grid, to keep the run short.\n- claim: figs4-initial-kurtosis-poor-predictor\n  outcome: reproduced\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs4-initial-kurtosis-poor-predictor\n  measured:\n  - 0.178\n  notes: The Spearman correlation between kappa_0 and the kurtosis at N/16 across active windows is\n    0.178 (CV (a), 11639 windows) and 0.190 over all phases; its magnitude is below 0.3 under every\n    reading. Within sessions it ranges from -0.263 to 0.58 (median 0.136). kappa_0 ranges from 25.0\n    to 349.1 in the active phase.\n- claim: figs5a-firing-rate-order\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs5a-firing-rate-order\n  notes: Under CV (a), at all 141 thresholds from 5 to 12 the mouse-averaged rate is ordered active <\n    NNI < passive (0.166, 0.199 and 0.223 spikes per bin per unit at 5; 0.135, 0.183 and 0.193 at\n    12) and falls with the threshold in every phase (Spearman -0.991 active, -0.976 NNI (a), -0.998\n    NNI (b), -0.991 passive). CV (c) gives the same. Under CV (b) the order holds at 97.2% (NNI (a))\n    or 86.5% (NNI (b)) of the points, with correlations of -0.58 and -0.53 in the active and passive\n    phases (partially reproduced or not reproduced).\n  deviations:\n  - CV reading (a) is adopted as an assumption, as for fig3a-kurtosis-broader-than-surrogate.\n  - The rate is over all V1 units of the session, units silent in the window included.\n- claim: figs5c-hit-rate-firing-rate-nonmonotonic\n  outcome: reproduced\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs5c-hit-rate-firing-rate-nonmonotonic\n  notes: Under every reading the hit rate below rho_th changes direction by more than one SE. Under\n    CV (a) it rises from 0.601 at 0.05 to 0.751 at 0.11 and falls to 0.654 at 0.20 (SEs 0.037,\n    0.012 and 0.005). The verdict is the same under the five seeds and with the smaller of two SEs.\n  deviations:\n  - A change between two grid points counts when it exceeds the larger of their two bootstrap SEs\n    (10^4 Poisson resamples); the criterion does not say which SE.\n- claim: figs7-fatigue-halves\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs7-fatigue-halves\n  notes: Under CV (a) the relative gain is negative at every point from 8 to 12 in the first half\n    (-7.98% at 8, -11.22% at 12) and at all but 1.2% of points in the second (-6.77%, -20.32%). The\n    overall hit rate is lower in the second half (0.548 against 0.749), as the paper says. CV (c)\n    gives the same. Under CV (b), with 4 and 6 trials above 12, the gain is positive throughout\n    both halves (reproduced with O5 (a), partially reproduced with O5 (b)).\n  deviations:\n  - CV reading (a) is adopted as an assumption, as for fig3a-kurtosis-broader-than-surrogate.\n  - The first half is the windows ending within 30 min of the active block's start, the second the\n    windows starting at or after 30 min, a standard choice.\n- claim: figs8-halves-and-phase-order\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs8-halves-and-phase-order\n  notes: Blocked for the grid, as fig4a-active-most-scaling. Where a grid exists (CV (b)), the\n    second half lies above passive at every point, passive above NNI at none, and the first half at\n    or above the second at 60 to 68% of points. Median kurtosis (CV (a)), first half 6.389, second\n    half 6.026 (Mann-Whitney p = 1.4e-42), passive 5.534, NNI 6.994 (a) and 7.216 (b). The second\n    half is lower than the first, as the paper says, but the NNI phase has the highest kurtosis,\n    not the lowest.\n  deviations:\n  - As for fig3c-scaling-hit-rate-higher.\nfindings:\n- kind: selection_undocumented\n  about: data\n  severity: major\n  statement: The paper analyses 62 sessions from 44 mice with more than 128 V1 units, and 43\n    sessions under stricter sorting criteria. In the dandiset 97 sessions from 68 mice have more\n    than 128 units whose peak channel is in VISp, 68 sessions (54 mice) with units labelled good,\n    and 1 session with the default quality filters. No documented rule gives the paper's sessions,\n    and the files do not say which were used.\n- kind: methods_unavailable\n  statement: Following Eqs. 2 to 5 as printed, ISI-shuffled surrogate windows have kurtoses around\n    3.6 (minimum 2.80) and real windows around 6.2, where the paper reports surrogate kurtoses no\n    lower than about 6 and a surrogate maximum of about 7. The kurtosis scale of the paper is not\n    reached, so the fixed thresholds of its figures (8, 12) and its surrogate range cannot be\n    matched. Question for the authors. What exactly is pooled and normalised when the kurtosis is\n    computed (Eq. 5 prints phi_i inside the sum), and how are silent units handled?\n- kind: methods_unavailable\n  statement: The surrogate maximum kappa_surr_max (about 7 in Figure 3) is, as defined here, set by a\n    few windows (34.29 in the active phase, 24.45 to 35.46 over seeds), which leaves every plotted\n    threshold range empty and blocks five claims. Question for the authors. Is kappa_surr_max the\n    maximum over every surrogate window of all sessions, one surrogate per window, or another\n    summary?\n- kind: methods_unavailable\n  statement: The CV of Appendix 1 (\"of the activity across the window\") is not defined. The CV of\n    the population count never exceeds 5 here (no window excluded), the pooled unit-bin CV excludes\n    209 of 11639 active windows, and the mean unit CV excludes 9702. Question for the authors. Which\n    activity is the CV computed on?\n- kind: methods_unavailable\n  statement: The real-space details are not given. The K range of the fits, how P_silence is\n    averaged over clusters, which spectra enter the fit of mu, and the r^2 rule (which only 1.7% of\n    active windows pass here, for the fit pooled over K >= 16). Here alpha and beta come out near\n    the paper's values (1.48 and 0.76 active), mu about twice (1.58) and z about half (0.16).\n    Question for the authors. Over which K and ranks are the exponents fitted?\n- kind: other\n  about: data\n  severity: minor\n  statement: The stimulus blocks are, in every session, active task, 10-s gray screen, Gabors (15.2\n    min), gray screen (4.8 min), full-field flashes (5.0 min) and passive replay. The Appendix puts\n    the gray screen last, after the flashes. In some sessions the time between the active and\n    passive blocks is up to 80.8 min, against about 26 in most.\n- kind: other\n  about: data\n  severity: minor\n  statement: Active 30-s windows hold 0 to 4 go trials with a hit or miss outcome (median 2), where\n    Appendix 5 says three to five trials are performed in each window; the paper's count may\n    include aborted or catch trials.\n- kind: other\n  about: data\n  severity: minor\n  statement: Some units are assigned to a structure labelled only `VIS` (a visual area not named),\n    and in a few windows almost all V1 units are silent (up to 203 units in one window; 14 windows\n    of 3 sessions keep fewer than 64 active units), which looks like a recording dropout. Both are\n    evident from the values.\n- kind: other\n  about: data\n  severity: none\n  statement: No session is deposited twice (unique identifiers; no two sessions share unit and spike\n    counts). Spike times are sorted within every unit. V1 responds to image onsets and not to\n    omitted flashes in every analysed session (at least 4.0 standard errors), so spikes and\n    stimulus tables share a clock. Hits and misses are exactly the non-aborted go trials.\n- kind: paper_inconsistency\n  statement: In Supplement V the last p-value is labelled \"mu1 vs mu2\", a second time; the pair mu1\n    against mu3 is missing from the list. Eq. 5 prints phi_i inside the sum over j, which would make\n    psi_i a rescaled copy of phi_i.\n"
}
```

```
File created successfully at: attempts/cambrainha-2025-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_part2.py').read()
old='''print("units silent in a 30-s window (left out of that window): median",'''
new='''w30 = W_all[(W_all.length == 30) & (W_all.units == "all")]
print("30-s windows keeping fewer than 64 active V1 units:", int((w30.N < 64).sum()), "in",
      w30[w30.N < 64].path.nunique(), "sessions")
print("units silent in a 30-s window (left out of that window): median",'''
assert old in s
s=s.replace(old,new,1)
open('nb_part2.py','w').write(s)
EOF
cd  && python - <<'EOF'
p='attempts/cambrainha-2025-01.yaml'
s=open(p).read()
s=s.replace("(which only 1.7% of\n    active windows pass here","(which only 1.7% of\n    windows pass here")
s=s.replace("ranges from -26.88% to -1.19%, with bootstrap SEs of 1.2% to 7.8%.","ranges from -26.88% to -1.19%, with bootstrap SEs of 1.2% to 7.8% at the printed thresholds.")
s=s.replace("holds at none of the points (0 of 130 and of 94), as the NNI phase has the most windows above\n    every threshold.","holds at none of the points (0 of 130 and of 94).")
open(p,'w').write(s)
import yaml; d=yaml.safe_load(open(p)); print(len(d['outcomes']))
EOF
grep -n "1.7% of\|printed thresholds\|0 of 130" attempts/cambrainha-2025-01.yaml
```

```
18
120:    ranges from -26.88% to -1.19%, with bootstrap SEs of 1.2% to 7.8% at the printed thresholds.
163:    holds at none of the points (0 of 130 and of 94). Over 3 to 15 under CV (a), a variant, the NNI fraction is above the active one
180:    +/- 0.056, mu 1.575 +/- 0.181 (44 sessions with a window of r^2 >= 0.85; 1.7% of windows pass
328:    averaged over clusters, which spectra enter the fit of mu, and the r^2 rule (which only 1.7% of
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
d=yaml.safe_load(open('attempts/cambrainha-2025-01.yaml'))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str):
        for bad in [': ','—','rather',' #']:
            if bad in x: print(path, repr(bad), x[max(0,x.index(bad)-40):x.index(bad)+20])
walk(d)
EOF
cd $TMPDIR && python - <<'EOF'
c=open('concl.py').read()
c=c.replace("holds at none of the points (0 of 130 and of 94), because the NNI phase has the most windows above threshold.","holds at none of the points (0 of 130 and of 94); at the start of the grid the NNI fraction is the largest (0.184 against 0.054 active).")
open('concl.py','w').write(c)
import re
for f in ['concl.py','summary.md']+[f'nb_part{i}.py' for i in range(1,10)]:
    t=open(f).read()
    for bad in ['—','rather','**']:
        for m in re.finditer(re.escape(bad),t):
            ctx=t[max(0,m.start()-30):m.start()+30].replace('\n',' ')
            if bad=='**' and ('**Result' in t[m.start():m.start()+9] or 'Result: ' in t[m.start()-30:m.start()] or '**Paper' in ctx or '**Dataset' in ctx or '**What' in ctx or '**How' in ctx ): pass
            print(f, repr(bad), ctx)
EOF
```

```
concl.py '**' ing shown.''' C["fig3a"] = '''**Result: partially reproduced
concl.py '**' **Result: partially reproduced**, resting on the CV reading 
concl.py '**'  the same.''' C["fig3c"] = '''**Result: blocked (methods_und
concl.py '**' cked (methods_underspecified).** Under the adopted readings 
concl.py '**' 642 at 12.''' C["rises"] = '''**Result: blocked (methods_und
concl.py '**' ocked (methods_underspecified)**, for the reason of fig3c-sc
concl.py '**'  to 0.587.''' C["fig3d"] = '''**Result: not reproduced.** No
concl.py '**' = '''**Result: not reproduced.** No reading reaches 24 +/- 3
concl.py '**' o -1.19 %.''' C["figs1"] = '''**Result: not reproduced.** Ne
concl.py '**' = '''**Result: not reproduced.** Neither length passes under
concl.py '**' ive seeds.''' C["figs2"] = '''**Result: not reproduced**, re
concl.py '**'  = '''**Result: not reproduced**, resting on CV (a), an assu
concl.py '**' eproduced.''' C["fig4a"] = '''**Result: blocked (methods_und
concl.py '**' cked (methods_underspecified).** Under the adopted readings 
concl.py '**' ive in 88.''' C["figs8"] = '''**Result: blocked (methods_und
concl.py '**' ocked (methods_underspecified)**, for the grid, as fig4a-act
concl.py '**'  lowest.''' C["fig4act"] = '''**Result: not reproduced.** No
concl.py '**' = '''**Result: not reproduced.** No reading puts more than t
concl.py '**' a 0.968.''' C["fig4pas"] = '''**Result: not reproduced.** Al
concl.py '**' = '''**Result: not reproduced.** All 48 readings fail. Under
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
for f in ['nb_part1.py','summary.md']:
    t=open(f).read()
    for a,b in [('**Paper.**','Paper.'),('**Dataset.**','Dataset.'),('**0.240702.1725**','0.240702.1725'),('**What is read.**','What is read.'),("**How the analysis differs from the paper's.**","How the analysis differs from the paper's."),('**What was found about the dataset.**','What was found about the dataset.')]:
        t=t.replace(a,b)
    open(f,'w').write(t)
EOF
grep -c '\*\*' $TMPDIR/nb_part1.py $TMPDIR/summary.md
```

```
/tmp/claude-1001/nb_part1.py:0
/tmp/claude-1001/summary.md:0
```

**Agent**

Now the README, then rebuild and run the final notebook.

**Agent calls Write**

```json
{
 "file_path": "entries/cambrainha-2025/README.md",
 "content": "# Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025) from dandiset 000713\n\nTests the findings of [Cambrainha et al. (2025)](https://doi.org/10.1103/w49n-2vz8), \"Criticality\nat Work: Scaling in the Mouse Cortex Enhances Performance\", on\n[DANDI:000713](https://dandiarchive.org/dandiset/000713/0.240702.1725), the Allen Institute Visual\nBehavior Neuropixels data. For each 30-s window of V1 spiking it computes the kurtosis after\nmomentum-space coarse graining and an ISI-shuffled surrogate, relates it to the hit rate of the\nchange-detection task, compares the active, passive and non-natural image phases, and fits the\nreal-space renormalization exponents.\n\n| Claim | Outcome |\n|---|---|\n| 62 sessions (44 mice) have more than 128 V1 units | Not reproduced |\n| Kurtosis spans a broad range above the surrogates, lowest surrogates around 6 | Partially reproduced (assumed) |\n| Hit rate over scaling windows is higher than over no-scaling windows and the shuffle | Blocked: methods underspecified |\n| Hit rate over scaling windows rises with the threshold | Blocked: methods underspecified |\n| Relative performance gain reaches 24% | Not reproduced |\n| Similar results with 10-s and 60-s windows | Not reproduced |\n| Similar results with strictly sorted units (43 sessions) | Not reproduced (assumed) |\n| More windows above threshold in active than passive than non-natural images | Blocked: methods underspecified |\n| Exponents of the active phase | Not reproduced |\n| Exponents of the passive phase, and their differences from active | Not reproduced |\n| Exponents with non-natural images, and their differences | Not reproduced |\n| Static exponents approach trivial values from active to passive to non-natural | Partially reproduced |\n| Exponents stable with the kurtosis threshold | Blocked: methods underspecified |\n| Kurtosis before coarse graining is a poor predictor of kurtosis after | Reproduced |\n| Firing rate ordered active < non-natural < passive and falls with the threshold | Reproduced (assumed) |\n| Hit rate below a firing-rate threshold is not monotonic | Reproduced |\n| Relation between kurtosis and performance holds in both halves of the active phase | Not reproduced (assumed) |\n| Second half has lower kurtosis, non-natural images the lowest | Blocked: methods underspecified |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe paper links no code. Computed as its equations describe, the surrogate kurtoses here are around\n3.6, where the paper reports surrogate kurtoses of 6 or more and a surrogate maximum of about 7, so\nthe paper's kurtosis scale is not reached. The surrogate maximum here is set by a few windows\n(34.29), which leaves the threshold ranges of five claims empty; they are blocked, with every\nreading shown in the notebook. Over the whole range of thresholds the hit rate over high-kurtosis\nwindows is below that over low-kurtosis windows, and the non-natural image phase has the highest\nkurtosis. The attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/cambrainha-2025-01.yaml`](../../attempts/cambrainha-2025-01.yaml).\n"
}
```

```
File created successfully at: entries/cambrainha-2025/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python build.py && cd  && date -u && python tools/entry.py all entries/cambrainha-2025 2>&1 | tail -4; date -u
```

```
73
Fri Nov 27 09:09:10 UTC 2026
Installed kernelspec registry-cambrainha-2025 in executed/cambrainha-2025/.venv/share/jupyter/kernels/registry-cambrainha-2025
0 error(s)
pass  reproduce_cambrainha_2025.ipynb  (1435 s)
Fri Nov 27 09:33:19 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF' > $TMPDIR/exec_out2.txt
import nbformat
nb=nbformat.read(open('executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'),4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    txt="".join(o.get('text','') for o in c.get('outputs',[]) if o.get('output_type')=='stream' and o.get('name')=='stdout')
    print('=== cell',i,c.metadata.get('tags')); print(txt)
EOF
diff <(grep -v "processed 98\|per-window fits\|session values computed\|run time\|peak memory" $TMPDIR/exec_out.txt) <(grep -v "processed 98\|per-window fits\|session values computed\|run time\|peak memory" $TMPDIR/exec_out2.txt); grep -n "notebook run time" $TMPDIR/exec_out2.txt
```

```
42a43
> sessions with more than 30 min between the active and passive blocks: [{'path': 'sub-585329/sub-585329_ses-20211111T220915.nwb', 'nni_a': 80.79}]
62a64
> 30-s windows keeping fewer than 64 active V1 units: 14 in 3 sessions
889:notebook run time: 23.8 min
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/cambrainha-2025-01.yaml'
s=open(p).read()
old="""In some sessions the time between the active and
    passive blocks is up to 80.8 min, against about 26 in most."""
assert old in s
s=s.replace(old,"""In one session (sub-585329, 2021-11-11) the time
    between the active and passive blocks is 80.8 min, against about 26 in the others.""")
open(p,'w').write(s)
EOF
python tools/entry.py check entries/cambrainha-2025 2>&1 | tail -5; python tools/entry.py handover entries/cambrainha-2025 2>&1 | tail -5; ls executed/cambrainha-2025/handover/
```

```
0 error(s)
wrote executed/cambrainha-2025/handover
cambrainha-2025.yaml
criticality.py
reproduce_cambrainha_2025.ipynb
```

**Agent calls Bash**

```bash
git status --short | grep -v "^ M tools\|^?? tools\|^?? docs/outside" ; date -u
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
?? attempts/cambrainha-2025-01.yaml
?? entries/cambrainha-2025/
?? scripts
Fri Nov 27 09:33:49 UTC 2026
```

**Agent**

I finished steps 1 to 6 on DANDI:000713, pinned at version 0.240702.1725. Of the 18 claims, 3 are reproduced, 2 partially reproduced, 8 not reproduced and 5 blocked. `entry.py all` passed on the final run (notebook 23.8 min, the check found no errors) and the handover package is in `executed/cambrainha-2025/handover/`.

**1. Outcomes**

| claim | outcome |
|---|---|
| sessions-selected | not reproduced (97 sessions from 68 mice, against 62 from 44) |
| fig3a-kurtosis-broader-than-surrogate | partially reproduced, assumed (lowest surrogate kurtosis is 2.80, not about 6) |
| fig3c-scaling-hit-rate-higher | blocked, methods_underspecified |
| fig3c-hit-rate-rises-with-threshold | blocked, methods_underspecified |
| fig3d-relative-gain-24 | not reproduced (largest gain −1.19%) |
| figs1-other-window-lengths | not reproduced |
| figs2-strict-units | not reproduced, assumed |
| fig4a-active-most-scaling | blocked, methods_underspecified |
| fig4-exponents-active / passive / nni | not reproduced (alpha and beta near the paper's values, mu about twice, z about half) |
| fig4bc-static-exponents-trend | partially reproduced (z order fails) |
| figs3-exponents-stable-with-threshold | blocked, methods_underspecified |
| figs4-initial-kurtosis-poor-predictor | reproduced (Spearman 0.178) |
| figs5a-firing-rate-order | reproduced, assumed |
| figs5c-hit-rate-firing-rate-nonmonotonic | reproduced |
| figs7-fatigue-halves | not reproduced, assumed |
| figs8-halves-and-phase-order | blocked, methods_underspecified |

The five blocked claims judge their result over thresholds that start at the largest surrogate kurtosis. Here that maximum is 34.29, set by a few windows, against about 7 in the paper. That leaves the plotted range (up to 12.5 or 15) empty, so the criterion cannot be applied. I blocked them under the protocol's rule that a reference level far from the paper's means the procedures differ.

The notebook also shows each blocked claim over all thresholds from 3 to 15, outside its criterion:
- The hit rate over high-kurtosis windows is below the low-kurtosis hit rate at every one of 236 thresholds.
- The non-natural image phase has the most high-kurtosis windows, where the paper finds the fewest.

**2. Dataset, assumptions, questions**
- **Dataset:** 153 sessions from 81 mice, no duplicates.
  - **Unit counts:** 97 sessions have more than 128 V1 units; with the `good` label 68 sessions (54 mice); with the default quality filters only 1. No reading gives the paper's 62 sessions or its 43 strict sessions.
  - **Block order:** the gray screen comes between the Gabors and the flashes, not last as the Appendix says. One session (sub-585329) has 80.8 min between the active and passive phases instead of about 26.
  - **Trials:** active windows hold 0 to 4 go trials (median 2), against the paper's "three to five".
  - **Clock:** image onsets evoke a V1 response and omitted flashes do not, in every session, so spikes and stimulus tables share a clock.
  - **Version:** this is the only published version, and the draft has not changed since.
- **Assumption:** I adopted CV reading (a), the CV of the population count. Reading (b) would exclude 9702 of 11639 active windows, which contradicts the paper's description of the exclusion as removing rare artefacts. Four outcomes rest on it (marked "assumed"); under reading (b) several of these come out reproduced, resting on 4 to 7 trials.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - How is the kurtosis computed so that surrogates reach 6 or more? Followed as written, surrogates here sit around 3.6.
  - Is the surrogate maximum taken over every surrogate window?
  - Which activity is the CV computed on?
  - Over which cluster sizes and ranks are the real-space exponents fitted?
- **Questions to a reader:** none.

**3. Protocol points**
1. The protocol has two rules for readings: "reproduced under any reading" for which trials or subset a number counts, and "they must agree, else adopt the best-supported reading" for method details. The claims file's criteria say "under one reading" for method-detail readings too (the CV, the surrogate maximum). I applied the protocol's rule for method details and recorded it as a deviation. Taken literally, fig3c would be "reproduced", from the CV (b) reading under the claim seed only.
2. There is no rule for a criterion whose threshold grid is empty. I used the chance-level rule and blocked as methods_underspecified.
3. "A claim that depends on a blocked claim is blocked" would cascade from fig3c and fig4a to claims whose own tests could still be run (fig3d, figs1, figs5a, figs7 and others). I applied the cascade only where the block reason carries over and recorded that choice.
4. Seeds for many parallel sessions: the protocol says nothing on this. I gave each session a child seed spawned from the claim's seed.
5. Rating a mismatch between the paper and correct files "about data" fits awkwardly when the paper's description is simply wrong (the block order). I filed it about data, minor.
6. The bootstrap uses 10^4 Poisson resamples instead of 10^5 of fixed size, so that one draw serves every threshold; this is recorded as a deviation.

**4. Runtime and failures**
The run went from 07:21 to about 09:34 UTC. The first full run failed in the exponent section because a variable was overwritten; I fixed it and re-ran (24 min). The re-runs gave identical numbers. In the notebook's data-check text, one sentence says "sessions printed above" where only one session is printed; I fixed this in the record but did not re-run the notebook for it.

Files are in `entries/cambrainha-2025/`:
- reproduce_cambrainha_2025.ipynb
- criticality.py
- entry.yaml
- README.md
- requirements.in
- requirements.lock.txt

The record is `attempts/cambrainha-2025-01.yaml`.

## End of run

91 turns, 128 minutes, $8.43 at API prices, result: success.
